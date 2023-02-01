## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-31](docs/good-messages/2023/2023-01-31.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,309,594 were push events containing 3,541,929 commit messages that amount to 295,970,307 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 54 messages:


## [ZhengPeiRu21/azerothcore-wotlk](https://github.com/ZhengPeiRu21/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/ZhengPeiRu21/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Tuesday 2023-01-31 00:03:19 by ICXCNIKA

fix(DB/Locale): deDE fix request items texts #02 (#14615)

Process of translation: only original sources of deDE texts by
researching multiple sources, reverse translation by searching for
related quest items/NPCs and using these names to reconstruct a proper
translation.

This fixes the terms

Coldtooth-Mine (Eisbeißermine), Doomhammer (Schicksalshammer), Fizzle
(Zischel), Fizzledowser (Rutenwünschels), Fizzlebub (Zischelbub),
Burning Blade (Brennende Klinge), Ashenvale (Eschental),
Bloodscalp/s/stamm (Blutskalpe, Blutskalpstamm),
Darkspeartrolle/Darkspears/Darkspearstamm (Dunkelspeere,
Dunkelspeertrolle, -stamm), Moonglade (Mondlichtung), Starblaze
(Sternenschauer), Shadowglen (Laubschattental), Darrowshire (Darroheim),
Booty Bay (Beutebucht), Ratchet (Ratschet), Dizzywig (Flunkerblick),
Hearthglen (Herdweiler), Chillwindspitze (Zugwindspitze), Stormrage
(Sturmgrimm), Stormpike (Sturmlanze/n), Ironforge (Eisenschmiede),
Thunderhorn (Donnerhörner), Steamboil (Kesseldampf), Twilight-Hammer,
-klan (Schattenhammer/Schattenhammerklan), Fathom-Kern (Tiefenkern),
Blackfathom Deeps (Tiefschwarze Grotte), Blackrock-* (Schwarzfels-*),
Hawkwind (Falkenwind), Feathermoon (Mondfeder), Moonrage (Mondzorn),
Firemane (Feuermähne), Searingblade (Sengende Klinge), Ragefireabgrund
(Flammenschlund), Ironbands Areal (Eisenbands Lager), Zandalar
(Zandalari), Southshore (Süderstade)

for quest progress/request text entries for the deDE localisation with
proper casus/declension (these are not proper translated names of
locations/NPCs that have been left over by Blizzard since their language
localisations in TBC in 2006 and onward).

Added missing progress/request text entries for 308, 311, 417, 1644,
1787, 5059, 5060, 5721, 6004, 6023, 6025, 6187, 8042, 8043, 8044, 8046,
8047, 8048, 8050-8079, 8102, 8107, 8108, 8111, 8112, 8113, 8117, 8118,
8142, 8143, 8147, 8183-8195, 8238, 8239, 8240, 8243, 8246, 8860, 9594,
9692, 9707, 10414, 10415, 10919, 11451. (A lot of them are
Zandalari/Zul'Gurub related quests.)

Replaced post-Cataclysm progress/request text entries for 933, 935,
6387, 7383.

Fixed a wrong $R with plain text at progress/request text for 9147.

Added missing female gender equivalent to 6391.

(There are probably more changes in the file that aren't further
explained here as it was hard to keep track of everything. If you think
I made a mistake or have questions please contact me directly.)

<!-- First of all, THANK YOU for your contribution. -->

## Changes Proposed:
-  Fixing a lot in the quest_request_items_locale table.

## Issues Addressed:
<!-- If your fix has a relating issue, link it below -->
- Fixing some of the tasks in
https://github.com/azerothcore/azerothcore-wotlk/issues/14244
Referring to my other two bug reports from CC Github:
- https://github.com/chromiecraft/chromiecraft/issues/4697
- https://github.com/chromiecraft/chromiecraft/issues/4745

## SOURCE:
<!-- If you can, include a source that can strengthen your claim -->
- Read the text on top.

## Tests Performed:
<!-- Does it build without errors? Did you test in-game? What did you
test? On which OS did you test? Describe any other tests performed -->
- Not tested.


## How to Test the Changes:
<!-- Describe in a detailed step-by-step order how to test the changes
-->
All of the changes are to reward texts of quests, can be tested by
completing quests or simply reviewing the changed file.

## Known Issues and TODO List:
<!-- Is there anything else left to do after this PR? -->

- [ ]
- [ ]

<!-- If you intend to contribute repeatedly to our project, it is a good
idea to join our discord channel. We set ranks for our contributors and
give them access to special resources or knowledge:
https://discord.com/invite/DasJqPba)
Do not remove the instructions below about testing, they will help users
to test your PR -->
## How to Test AzerothCore PRs
 
When a PR is ready to be tested, it will be marked as **[WAITING TO BE
TESTED]**.

You can help by testing PRs and writing your feedback here on the PR's
page on GitHub. Follow the instructions here:

http://www.azerothcore.org/wiki/How-to-test-a-PR

**REMEMBER**: when testing a PR that changes something **generic** (i.e.
a part of code that handles more than one specific thing), the tester
should not only check that the PR does its job (e.g. fixing spell XXX)
but **especially** check that the PR does not cause any regression (i.e.
introducing new bugs).

**For example**: if a PR fixes spell X by changing a part of code that
handles spells X, Y, and Z, we should not only test X, but **we should
test Y and Z as well**.

---
## [tydavis/git](https://github.com/tydavis/git)@[69bbbe484b...](https://github.com/tydavis/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Tuesday 2023-01-31 00:13:02 by Jeff King

hash-object: use fsck for object checks

Since c879daa237 (Make hash-object more robust against malformed
objects, 2011-02-05), we've done some rudimentary checks against objects
we're about to write by running them through our usual parsers for
trees, commits, and tags.

These parsers catch some problems, but they are not nearly as careful as
the fsck functions (which make sense; the parsers are designed to be
fast and forgiving, bailing only when the input is unintelligible). We
are better off doing the more thorough fsck checks when writing objects.
Doing so at write time is much better than writing garbage only to find
out later (after building more history atop it!) that fsck complains
about it, or hosts with transfer.fsckObjects reject it.

This is obviously going to be a user-visible behavior change, and the
test changes earlier in this series show the scope of the impact. But
I'd argue that this is OK:

  - the documentation for hash-object is already vague about which
    checks we might do, saying that --literally will allow "any
    garbage[...] which might not otherwise pass standard object parsing
    or git-fsck checks". So we are already covered under the documented
    behavior.

  - users don't generally run hash-object anyway. There are a lot of
    spots in the tests that needed to be updated because creating
    garbage objects is something that Git's tests disproportionately do.

  - it's hard to imagine anyone thinking the new behavior is worse. Any
    object we reject would be a potential problem down the road for the
    user. And if they really want to create garbage, --literally is
    already the escape hatch they need.

Note that the change here is actually in index_mem(), which handles the
HASH_FORMAT_CHECK flag passed by hash-object. That flag is also used by
"git-replace --edit" to sanity-check the result. Covering that with more
thorough checks likewise seems like a good thing.

Besides being more thorough, there are a few other bonuses:

  - we get rid of some questionable stack allocations of object structs.
    These don't seem to currently cause any problems in practice, but
    they subtly violate some of the assumptions made by the rest of the
    code (e.g., the "struct commit" we put on the stack and
    zero-initialize will not have a proper index from
    alloc_comit_index().

  - likewise, those parsed object structs are the source of some small
    memory leaks

  - the resulting messages are much better. For example:

      [before]
      $ echo 'tree 123' | git hash-object -t commit --stdin
      error: bogus commit object 0000000000000000000000000000000000000000
      fatal: corrupt commit

      [after]
      $ echo 'tree 123' | git.compile hash-object -t commit --stdin
      error: object fails fsck: badTreeSha1: invalid 'tree' line format - bad sha1
      fatal: refusing to create malformed object

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [swbs-co/odoo](https://github.com/swbs-co/odoo)@[639cfc76ba...](https://github.com/swbs-co/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Tuesday 2023-01-31 01:00:31 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#109812

Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[ae08395328...](https://github.com/lessthnthree/tgstation/commit/ae08395328672ee40c5abb7f2bd1452bb932d6d4)
#### Tuesday 2023-01-31 02:10:18 by san7890

Syndicate Bomb Core Payloads Can Only Be Triggered via the Bomb (#72986)

## About The Pull Request

Basically, you can't extract the bomb core, slap a 10-second c4 on it/on
the shell/and run off having triggered an incredibly powerful explosion.
This is accomplished by having the syndicate bomb override ex_act (it
will be deleted if the explosion goes off), as well as the payload
itself being subtyped into something resistant to bombs and burning.

In-universe, this is described as the shell being quite resistant to
forms of external explosive force- but if any explosive force comes from
within the bomb's shell: kabloom. The bombcore itself has been
redesigned (in a rare moment of non-ineptude) by Donk Co., who has
redesigned the bomb core payload from the ground up- meaning that it can
only be detonated electronically by an impulse from the bomb machinery.
Cutting the wrong wire and attempting to get rid of the bomb by hitting
it with an axe or something will still cause it to blow up, but you know
how those things can be.
## Why It's Good For The Game

I feel like the point of the syndicate bomb is to be a threat for the
crew to match up against. I want a clown in bomb squad gear to head out
to the site and sweat trying to figure out which wire it is, until....
KA-BLHONK: red mist. Or, I want some "helpful" assistant to interrupt
someone's session by going "I KNOW WHAT WIRE IT IS", and having those
odds of either blowing everyone around them up or actually saving the
day.

Being able to detonate something that was balanced and designed to have
_at least_ one minute and a half in **10 SECONDS** is just so injurious
to the game. You can buy a shitload of these bombs, extract the cores,
slap c4 on it and go around the station doling out some serious
explosions. You can run into medbay, wrench it down, slap a c4 on it AND
NO ONE CAN DO ANYTHING ABOUT IT! They can't cut wires, they can't figure
it out to save the day, all they can do is run. Running from danger is
fine and acceptable, but it's just completely stacked against the crew
in a way that I feel needs to be rectified somehow.

I like the idea of purposefully fucking with the wires on the spot so
you sacrificially kill everyone, that feels quite fair to me. I just
simply don't like the fact that you can waltz around the station
punching huge gaps in the hull (remember, putting c4 on the bomb core
itself would cause it to go kabloom) with nearly nothing as far as risk.
It's way too rewarding for something very easy to accomplish (there's a
reason why it's 90 seconds- it's not meant to be easy to accomplish).

This doesn't affect base bombcore behavior, just the explodey ones that
come standard in syndicate bombs.
## Changelog
:cl:
balance: After an unfortunate event occuring when some nuclear
operatives took the ship to a Fireworks Store, the Syndicate have
re-engineered their bomb cores to only explode when electronically
triggered by the bomb shell itself. The payload inside a standard
syndicate bomb can not be exploded with another explosion, you must keep
it in the bomb machinery for it to actually do some explodey stuff.
/:cl:

---
## [MidoriWroth/tgstation](https://github.com/MidoriWroth/tgstation)@[99537d0123...](https://github.com/MidoriWroth/tgstation/commit/99537d0123167a07b242c33dad7c23ec9a5becef)
#### Tuesday 2023-01-31 03:05:41 by LemonInTheDark

Fixes parallax on >2 level maps going fucky with optimized multiz (#72169)

## About The Pull Request

We no longer always render parallax.
This was causing issues because we can't isolate the white of space from
the vaugely white of everything else.

So instead, if your parallax plane is out of view, we'll not only
disable it, but we'll disable the strand we send from the main plane TO
it.

Instead only blending against the bottom stack.

This does mean there's a possibility for fullwhite on z transition
borders (potentially fixable), or when hijacking the plane (also
fixable, but significantly more annoying).

This is enough to make large maps functional though, so I'm happy with
it

## Why It's Good For The Game

Allows for #71731 and other maps like it. Makes my code actually work

## Changelog
:cl:
fix: Using optimized multiz on > 2 z layer maps will no longer cause
fucko bungo
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[3d06075c5c...](https://github.com/treckstar/yolo-octo-hipster/commit/3d06075c5c8154a16ff25344529ea64df52f9c01)
#### Tuesday 2023-01-31 03:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Philbilly/Eternal-Babylon-TVT](https://github.com/Philbilly/Eternal-Babylon-TVT)@[45deb52897...](https://github.com/Philbilly/Eternal-Babylon-TVT/commit/45deb528978a3a27919cdea59f647917d6e87253)
#### Tuesday 2023-01-31 03:49:31 by Philbilly

medical loadouts

Keep in mind these are just on spawn. I still suggest providing medical crates so experienced medics can pick and choose. 


added 2x 250ml bags of saline - saline is required to clear IV obstructions otherwise I wouldnt bother.  (our normal loadout actually lack this as its new)
added 8x 250ml transfusion bags - because the idea of a medic who is waiting on more supplies needing to ask GI to donate blood is kinda neat. 

increased count of King LTs to 5 - Always nice to have as many of these as possible in a mass cas
doubled AAT kit count to 10 - AAT kits are single use items unless we change the settings. 
increased chest seal count to 10 - 2 is a little rough. 10 may be overkill. Either way Im thinking of the new medics here. 
increased TXA count to 8 - TXA is handy when you have multiple wounded. 
increased norepinephrine count to 8 - To make up for slightly decreased epinephrine counts. 

reduced morphine count by 4 - morphine is more dangerous in KAT. Hope making it more scarce will discourage ODs 
reduced painkiller count by 2 - Leaving 2 for total of 20 uses which is more than our normal sessions. 40 is still overkill and a waste of space. 
reduced carbonate count by 2 - Same logic as painkillers. 
reduced epinephrine count to 4 - Mainly to prevent abusing it for a stamina boost. Provided more norepinephrine to fill the role without the cheese factor.

---
## [Captain277/Citadel-Station-13-RP](https://github.com/Captain277/Citadel-Station-13-RP)@[287fb079d1...](https://github.com/Captain277/Citadel-Station-13-RP/commit/287fb079d1d52c8f244c7f08b3efa18de567f1cd)
#### Tuesday 2023-01-31 04:43:54 by Felix

Whitelist backend changes (#4996)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Whitelist are run by name, so renaming a whitelisted species also needs
an update to the WL as well.
Removes a shitty gimmick of a mirror most people dont have access to
because its a fucking nightmare of conditions we partially removed
and a fix for both runtimes and uninteded stat cheating
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
del: Removed the code behind the raider mirror
fix: fixed the shadekin traits applying to non shadekin
config: changed WL using Species ID rather than name
refactor: changed character species to always have a superspecies_id
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [zyro670/NotForkBot.NET](https://github.com/zyro670/NotForkBot.NET)@[4c37bc7aca...](https://github.com/zyro670/NotForkBot.NET/commit/4c37bc7aca0138710af6ab9f16fc1f4262fbe131)
#### Tuesday 2023-01-31 05:04:00 by Koi

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
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[8170f782f1...](https://github.com/LemonInTheDark/tgstation/commit/8170f782f1aed95ab2b97cb8853d5c232745f569)
#### Tuesday 2023-01-31 05:55:31 by LemonInTheDark

Adds darkness coloring to all eyes and goggles that use nightvision

Nightvision always looks really flat to me, you tend to forget you're
wearing mesons or whatever.
So instead of that, let's use individual colors to tint the darkness
that we brighten.

Mesons are green, sec night vision is red, thermals orange, etc.

You'll note some of these use - values instead of positive. This is done
mostly to avoid needing to stray from the constants I'm using, though I
realize I may just want to use those.

I think the effect this gives is really really nice. I've tuned most
things to work for the station, though mesons works for lavaland for
obvious reasons.

I've tuned things significantly darker then we have them set currently,
since I really hate flat lighting and this system suffers when
interacting with it.

My goal with these is to give you a rough idea of what's around you,
without a good eye for detail. That's the difference between say,
mesons, and night vision. One helps you see outlines, the other gives
you detail and prevents missing someone in the darkness.

It's hard to balance this precisely because of different colored
backgrounds (looking at you icebox)
More can be done on this front in future but I'm quite happy with things
as of now

---
## [tcharding/rust-bitcoin](https://github.com/tcharding/rust-bitcoin)@[f6d983b2ef...](https://github.com/tcharding/rust-bitcoin/commit/f6d983b2ef4dfacd53499fd9f1d77058c0f396ff)
#### Tuesday 2023-01-31 06:22:14 by Andrew Poelstra

Merge rust-bitcoin/rust-bitcoin#1532: Improve Psbt error handling

e7bbfd391353fd03d60550c768364e9de5d3e8c5 Improve Psbt error handling (DanGould)

Pull request description:

  ## Separate `encode::Error` and `psbt::Error` recursive dependency

  This initial work attempts to fix #837's first 2 points

  > - The current psbt::serialize::Deserialize has an error type of consensus::encode::Error. I think we should cleanly separate consensus encoding errors from application-level encoding errors like psbt.
  > - There is a recursive dependence between encode::Error and psbt::Error which would need to be cleanly dissected and separated so that there is no dependence or only one-way dependence.

  ## Better `ParseError(String)` types

  arturomf94 how compatible do your #1310 changes look to address #837's third point with this design?

  > - There are a lot ParseError(String) messages that could use a better type to downflow the information.

  I think your prior art would completely address this issue now.

  ## On handling `io::Error` with an associated error

  `encode::Error` has an `Io` variant. now that `Psbt::deserialize` returns `psbt::Error` and produces an `io::Error`, we need an `Io` variant on `psbt::Error`. Except that doing so breaks  `#[derive(Eq)]` and lots of tests for `psbt::Error`.

  Kixunil, I'm trying to understand your feedback regarding a solution to this problem.

  > I believe that the best error untangling would be to make decodable error associated.

  > I meant having associated `Error` type at `Decodable` trait. Encoding should only fail if the writer fails so we should have `io::Error` there (at least until we have something like `genio`).
  >
  > > [it] is a problem to instantiate consensus::encode::Error in [the psbt] module for `io::Error`?
  >
  > It certainly does look strange. Maybe we should have this shared type:
  >
  > ```rust
  > /// Error used when reading or decoding fails.
  > pub enum ReadError<Io, Decode> {
  >     /// Reading failed
  >     Io(Io),
  >     /// Decoding failed
  >     Decode(Decode), // consensus and PSBT error here
  > }
  > ```
  >
  > However this one will be annoying to use with `?` :( We could have `ResultExt` to provide `decode()` and `io()` methods to make it easier.
  >
  > If that's not acceptable then I think deduplicated IO error is better.

  Kixunil didn't we just get rid of Psbt as `Decodable`? Would this make more sense to have as an error associated with `Deserialize`? Or did we do the opposite of what we should have by making Psbt only `Serialize`/`Deserialize` because of #934, where only consensus objects are allowed to be `Decodable`? I wonder if we prioritized that strict categorization and are stuck with worth machinery because of it. My goal with #988 was to get to a point where we could address #837 and ultimately implement PSBTv2.

ACKs for top commit:
  tcharding:
    ACK e7bbfd391353fd03d60550c768364e9de5d3e8c5
  apoelstra:
    ACK e7bbfd391353fd03d60550c768364e9de5d3e8c5

Tree-SHA512: 32975594fde42727ea9030f46570a1403ae1a108570ab115519ebeddc28938f141e2134b04d6b29ce94817ed776c13815dea5647c463e4a13b47ba55f4e7858a

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[cba002fa91...](https://github.com/Helg2/tgstation/commit/cba002fa912f07112fbbedcab330a35e2bffeab7)
#### Tuesday 2023-01-31 06:51:09 by Sol N

converts contraband file into poster file, makes holiday posters work (kind of) (#72131)

## About The Pull Request

The first part of this is just something that bothered me when I was
messing around with something that I will PR in the new year,
contraband.dm and dmi is ONLY posters. There's nothing else in there and
there are plenty of official posters, and if with #71717 we will also
add holiday posters to the mix then I think that its time to retire
contraband and make it poster.

Some small things I did while messing with it was change some variables
that were single letters into actual variable names, but overall this
part of the pr is not a player facing change.

That said, speaking of #71717 I think that it didn't work? Or didn't
work the way that it was supposed to? All of the spawned posters aren't
instances of festive posters, they are instances of normal posters, so
the code on initialize was not doing anything and the only reason the
holiday_none poster was showing up was because of the proc in randomize
spawning the posters in as those other posters. Because it didn't
actually _become_ poster/official/festive it never could do the proc
that turns it into a poster for the holiday that is actually occurring.

But then when I made it work and it turned into the generic posters I
decided that it would be better if instead of 30% of all posters being a
half finished mess, that if there wasn't a holiday poster it just
wouldn't replace them at all. I have poster Ideas and Dreams so I will
try to help with adding to more holiday posters but not in this PR.

What IS in this PR though, is a new traitor poster that appears during
the holidays.

![dreamseeker_MxxBzXIxiy](https://user-images.githubusercontent.com/116288367/208793262-9d4a45dc-f7bb-4208-b3c3-78cb68cf9af5.png)

This is a generic evil holiday poster that will replace normal evil
posters in the evil poster objective, because I agree with #72003 that
it should be a feature.

## Why It's Good For The Game

Contraband file is just posters already, this is easier for people to
find the posters.
I like holiday posters and think that we should have them and add more,
it is a fun easy thing to add to a lot of the microholidays to make them
more visible in addition to the name generation, but I don't want to see
the unfinished holiday poster so I do think that it's better to only
have them spawn if the holiday actually has a poster. Looking forward to
febuary!

## Changelog

:cl:
add: during holidays the spread syndicate propaganda through posters
objective has a chance of spawning evil holiday poster
fix: framework for holiday posters is more functional and modular
code: contraband.dm file and contraband.dmi file are both now poster.dm
and poster.dmi
/:cl:

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[2a4ef2367d...](https://github.com/LemonInTheDark/tgstation/commit/2a4ef2367dd7db73ba0adfdc300a5093678b7746)
#### Tuesday 2023-01-31 09:12:08 by san7890

Basic Mobs Now Actually Have A Deathgasp (#72950)

## About The Pull Request

Pretty obviously an oversight since we only checked for simple_animal
for this, but should also factor in the fact that we could now be a
basic mob.

Actually I tested it on Sybil just now and deathgasps just never worked.
We were setting death_message for... I guess when they die? It's just
fucked but it works on my local now. blurgh
## Why It's Good For The Game

Ported simple animals that are now basic mobs were able to deathgasp
this time last year. Silly that they aren't able to do that now.
## Changelog
:cl:
fix: Basic Mobs are now able to deathgasp.
/:cl:

Let me know if the new variable name for the string is cringe, I just
settled on that since it mirrored the type of check we run in
select_message_type().

---
## [NotLebedev/nushell](https://github.com/NotLebedev/nushell)@[3d65fd7cc4...](https://github.com/NotLebedev/nushell/commit/3d65fd7cc4f6e0db0c1c31b895feabf2be66cb0a)
#### Tuesday 2023-01-31 09:40:39 by Doru

Expose filtering by file type in glob (#7834)

# Description

Add flags for filtering the output of `glob` by file type. I find myself
occasionally wanting to do this, and getting a file's
[file_type](https://docs.rs/wax/latest/wax/struct.WalkEntry.html#method.file_type)
is presumably fast to do as it doesn't have to go through the fallible
metadata method.

The design of the signature does concern me; it's not as readable as a
filter or "include" type list would be. They have to be filtered one by
one, which can be annoying if you only want files `-D -S`, or only want
folders `-F -S`, or only want symlinks `--butwhy?`. I considered
SyntaxShape::Keyword for this but I'll just defer to comments on this PR
if they pop up.

I'd also like to bring up performance since including these flags
technically incurs a `.filter` penalty on all glob calls, which could be
optimized out if we added a branch for the no-filters case. But in
reality I'd expect the file system to be the bottleneck and the flags to
be pretty branch predictor friendly, so eh

# User-Facing Changes
Three new flags when using `glob` and a slightly more cluttered help
page. No breaking changes, I hope.

# Tests + Formatting

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e9c87c0acb...](https://github.com/tgstation/tgstation/commit/e9c87c0acb15439c8f577bba35c45f51bf03d1aa)
#### Tuesday 2023-01-31 09:52:31 by LemonInTheDark

Starlight Polish (Space is blue!) (#72886)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds support to underlays to realize_overlays
Ensures decals properly handle plane offsets
Fixes space lighting double applying if it's changeturf'd into. this
will be important later
Makes solar vis_contents block emissives as expected
Moves transit tube overlays to update_overlays, adds emissive blockers
to them

#### Adds render steps

An expansion on render_target based emissive blockers. 
They allow us to hijack an object's appearance and draw it somewhere
else, or even modify it, THEN draw it somewhere else.
They chain quite nicely

Fixes shuttles deleting z holder objects

#### Makes space emissive, makes walls and floors block emissives
The core idea here goes like this:
We make space glow, and give its overlays some color

This way, the tile and space parallax remain fullbright, along with
anything that doesn't block emissives, but anything that does block
emissives will instead get shaded the color of starlight

This requires a bit of extra work, see later

This is done automatically with render relays, which now support
specifiying layer and color (Need to make an editor for these one of
these days)

The emissive blocking floor stuff requires making a second render plate
to prevent double scaling

Also adds some new layering defines for lighting, and ensures all turf
lights have a layer. We'll get to this soon

#### Makes things in space blue

We color them the same as starlight, by taking advantage of space being
emissive
This means that things in space that block emissive will block it
correctly and be colored blue by the light overlay, but space itself
will remain fullbright

This does require redefining what always_lit means, but nothing but
cordons use that so it's fineee


#### Makes glass above space glow, and some other stuff

Glass tiles that sit above space will now shine light with matching
color to the glasses color. This includes mat tiles.

Glass tiles (not mat because they have no alpha) also only partially
block emissives.
Adds a new proc that uses render steps to acomplish this, essentially
we're cutting out bits below X alpha and drawing what remains as an
emissive.

#### Modifies partial space showing to support glow

Essentially, alongside displaying space as an underlay, we also display
a light overlay colored like starlight.
That starlight overlay gets masked to only be visible in bits that do
not contain any alpha.

We also mask the turf lighting to not go into bits that have no alpha,
to ensure we get the effect we want.
This is done with that lighting layer thing I mentioned earlier.

#### Makes appearance realization's list output ordered

I want it output in order of overlay, sub overlay suboverlay, next
overlay
Need to use insert for that

## Why It's Good For The Game

Pretty!
Also having space be emissive is a very very good way to test for fucked
emissive blockers (If it's broken why are we even drawing the overlay)
I know for a fact mob blockers on lizards and socks are kinda yorked, I
think there's more

<details>
<summary>
Old
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916157-d4b38aa7-3ab6-42a4-989f-7bfba2dc2cba.png)

![image](https://user-images.githubusercontent.com/58055496/213916077-637fa288-bbee-477d-aded-730d9683477e.png)

![image](https://user-images.githubusercontent.com/58055496/213916088-0657a8a2-5627-48e2-8c4b-870c90ef2072.png)

</details>


<details>
<summary>
New
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916107-2af74e64-1817-4a44-b528-180a9160cb9e.png)

![image](https://user-images.githubusercontent.com/58055496/213916115-5fa36fcc-b988-4ccf-850e-21c26ed463d0.png)

![image](https://user-images.githubusercontent.com/58055496/213916120-6833187d-b12e-42a7-ac4b-63c56deb71e5.png)

</details>

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
add: Space now makes things in it starlight faintly blue
fix: Glass floors that display space now properly let space shine
through them, rather then hiding it in the dark
add: Glass floors above space now glow faintly depending on their glass
type
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[8eb9d376b5...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/8eb9d376b50ed6eab29c4c884d7bc3c53aa33fec)
#### Tuesday 2023-01-31 09:56:47 by san7890

Improves/Abstracts Suicide A Bit More (#72949)

## About The Pull Request

Basically all of the heavy lifting was done in #72919, but we do a few
key things here that I wasn't able to do then because it was just
fucking massive.

Player Facing Changes:
* hear_blind arg is now a default state and must be specifically
overridden. Pretty much every mob that wasn't a pAI or alien was lacking
this, so let's toss it in as a default now. Let me know if the generic
message I put in for /mob/living sucks and we can go from there.

Code Side Changes:
* suicide.dm now only contains code pertinent to the suicide verb, and
all subtype proc-overrides have been moved to an appropriate file
pertinent to that subtype.
* suicide.dm has also been organized a bit more to aid the previous
change.
* There is only one suicide verb now, implemented on /mob/living. All
the verb does is invoke the handle_suicide() proc, which does all of the
lifting.
* Leaning into *mumble mumble* object-oriented philosophy, the message
we send to the world on suicide is handled on subtype procs, rather than
be in the huge fuck-off message tree I implemented in the earlier PR. It
definitely makes the visible_message() proc not hard to read IMO. This
also means that we can take up a less footprint when we re-use certain
suicide messages (i.e. Silicon), which is nifty too.

i'm probably forgetting something but that's all of the big ones
## Why It's Good For The Game

There is now a very, very common framework for how suicide works across
all living mobs, and it's much easier to override how suicide is
handled. Certain subtypes do their own bullshit thing, but it's quite
easy to account for this on that case-by-case basis. The overall code
takes up a much less footprint that just makes it look nicer.
## Changelog
:cl:
qol: Some mob suicides now have a message that shows to blind people or
people that didn't actually witness the suicide, pretty cool.
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[51f02b5acc...](https://github.com/tgstation/tgstation/commit/51f02b5acc0ee3d042734b8fd4fd2b58ac41f9ab)
#### Tuesday 2023-01-31 10:25:40 by LemonInTheDark

Fixes critical plane masters improperly not being readded in show_to (#72604)

## About The Pull Request

[Adds support for pulling z offset context from an atom's
plane](https://github.com/tgstation/tgstation/commit/9f215c5316e5cfdbedf6a23ff97dfee0e523354b)

This is needed to fix paper bins, since the object we plane set there
isn't actually on a z level.
Useful elsewhere too!

[Fixes compiler errors that came from asserting that plane spokesmen had
a plane
var](https://github.com/tgstation/tgstation/commit/b830002443f2fbe230e9ff00236d7a46a9f2eec7)

[Ensures lighting backdrops ALWAYS exist for each lighting
plane.](https://github.com/tgstation/tgstation/commit/0e931169f7c5336333bc6f41353c82f603fc1170)

They can't float becuase we can see more then one plane at once yaknow?

[Fixes parallax going to shit if a mob moved zs without having a
client](https://github.com/tgstation/tgstation/commit/244b2b25baecfc644505a3ea1e348e0cb97a04e0)

Issue lies with how is_outside_bounds just blocked any plane readding
It's possible for a client to not be connected during z moves, so we
need to account for them rejoining in show_to, instead of just blocking
any of our edge cases.

Fixing this involved having parallax override blocks for show_plane and
anything with the right critical flags ensuring mobs have JUST the right
PMs and relays.
It's duped logic but I'm unsure of how else to handle it and frankly
this stuff is just kinda depressing.
Might refactor later

[show_to can be called twice successfully with no hide_from
call.](https://github.com/tgstation/tgstation/commit/092581a5c06f7f884f48d41c96fa9300327ef214)

Ensures no runtimes off the registers from this

## Why It's Good For The Game

Fixes #72543
Fixes lighting looking batshit on multiz. None reported this I cry into
the night.

## Changelog
:cl:
fix: Fixes parallax showing up ABOVE the game if you moved z levels
while disconnected
/:cl:

---------

Co-authored-by: Time-Green <timkoster1@hotmail.com>

---
## [TritonDataCenter/pkgsrc](https://github.com/TritonDataCenter/pkgsrc)@[d49ad3fba0...](https://github.com/TritonDataCenter/pkgsrc/commit/d49ad3fba02f6ffc14904e217470280863ac16d8)
#### Tuesday 2023-01-31 10:40:01 by bsiegert

Pullup ticket #6721 - requested by wiz
emulators/mame: bugfixes

Revisions pulled up:
- emulators/mame/Makefile                                       1.161
- emulators/mame/PLIST                                          1.73
- emulators/mame/distinfo                                       1.127

---
   Module Name:	pkgsrc
   Committed By:	wiz
   Date:		Sat Dec 31 11:12:58 UTC 2022

   Modified Files:
   	pkgsrc/emulators/mame: Makefile PLIST distinfo

   Log Message:
   mame: update to 0.251.

   It looks like MAME 0.251 has made it out the door just in time for
   the end of 2022! December felt like a long month in MAME development,
   because so much happened! Nebula, an elusive DECO Cassette game,
   is now emulated. With working steering controls, Magical Pumpkin:
   Puroland de Daibouken is now playable. Two members of the HP 9825
   family from the 1970s have been added, and issues with keyboard
   input on localised versions of the HP 86B have been fixed.

   One of the most interesting systems added this month is the so-called
   Ger?t 32620, make by the Institut f?r Kosmosforschung of the Deutsche
   Demokratische Republik. This device was used to read coded messages
   to be broadcast via shortwave radio numbers stations for reception
   by undercover agents. If a human were to read the numbers, they
   could inadvertently disclose knowledge about the nature of the
   messages or the coding scheme in their speech patterns. This device
   gives a small glimpse into the shadowy world of espionage.

   Konami fans have a lot to be excited about. Firstly, two more
   hand-held LCD games have been added: Skate or Die, and Bill Elliott?s
   NASCAR Racing. Secondly, Windy Fairy has been making steady progress
   on the PowerPC-based arcade systems, with gun controls now working
   in Teraburst. Finally, various refinements and fixes to the CPU
   core for Konami?s custom 6809 processor have fixed a subtle parallax
   scrolling effect in the classic Padodius DA!

   Several systems have been fleshed out noticeably this month,
   including the NEC PC-8801mkII SR family of Japanese computers, the
   3com Palm IIIc and Palm m100 PDAs, and the Yamaha DX100 synthesizer.
   Additionally, the NEC PC-88VA2 can now boot most software, and the
   work on the Palm systems has allowed the VTech IQ Unlimited to show
   signs of life.

   Quite a few systems have had pluggable controller support added
   this month, and support for some additional controllers has been
   added, including:

   * Pluggable controller support for consoles and computers from
     Sega, NEC and Sharp.

   * Sega Mega Drive mouse and 4-player adaptor support.

   * Support for an ATmega-based paddle controller that works with
     export versions of the Sega Master System.

   * NEC PC Engine mouse support.

   * Support for the Dempa Micom Soft XE-1AP, the first analog
     gamepad. Can be used with compatible software for the Sega Mega
     Drive, NEC PC Engine, Sharp X68000 and FM Towns families.

   Of course, there are lots of other fixes and emulation improvements.
   The Apple IIgs has better ADB and real-time clock emulation. Sega?s
   Turbo and Buck Rogers: Planet of Zoom have better controls, and
   the latter has had graphical priority issues fixed. The NES APU
   frame counter interrupt is now emulated, fixing issues with dozens
   of games. For developers, debugger command and expression history
   is now saved between sessions.

---
## [AamiRobin/dpemotes](https://github.com/AamiRobin/dpemotes)@[45b9259ff8...](https://github.com/AamiRobin/dpemotes/commit/45b9259ff84eea10f91aa0c2b4d122cedf9f7fc9)
#### Tuesday 2023-01-31 11:43:04 by Mads

🚶‍♂️Add 11 New Walking Styles (#99) 🚶‍♂️

HUGE thanks to @MadsLeander 

Notes/descriptions of the walking styles:

Bigfoot (move_characters@orleans@core@) - Head hanging slightly forwards, somewhat hurting in left fot, wide with arms as if he's large, walking slow, runs crazy and fast (Used by this character in storymode: https://gta.fandom.com/wiki/Sasquatch_Roleplayer)

Coward (move_m@coward) - Hunched forward when standing still, other wise not diffrent from the default male walk.

Dave (move_characters@dave_n) - Shoulders are higher then normal walk, standing wide when still, left foot hurting when running/jogging (sprint is the default one) (Used by Dave Norton in storymode)

    Femme2 (move_m@femme@) - Shoulders are "swinging", left leg is leaned on when standing still, generally can be best described as a feminine walk for male peds, run and sprint are like the default one (This is one of the avalible walks in GTA Online)

Jimmy (move_characters@jimmy) - Similar to nervous/slow (they are all from the same character afterall), but with out the nervous or slow part (walks normal speed and not tripping with legs when standing still) (Used by Jimmy, the son of Michael in storymode)

Patricia (move_characters@patricia) - Swinging with hips, straight/stiff back, run/sprint is similar to the default female one (Used by Patricia Madrazo in storymode)

Ron (move_characters@ron) - Entire body posture slightly hanging to the left, runs like an idiot, sprint is normal. (Used by Ronald "Ron" Jakowski in storymode)

Swagger2 (move_m@swagger@b) - Confident and somewhat slow walking, moving slightly to the right every so often, run an sprint is normal.

Gangster6 (move_f@gangster@ng) - Slight diffrent in walking speed, posture is noticible diffrent, arms are more straight when standing still.

Veryslow (move_m@leaf_blower) - Head looking down, walking very slowly, running with right arm as if he had a leaf blower, sprint is normal.

Flee5 (move_m@flee@c) - Similar to Flee4, but multiple diffrences like how many times he turns his head to look behind etc.

---
## [peff/git](https://github.com/peff/git)@[2adeefb748...](https://github.com/peff/git/commit/2adeefb748563861fdc89ca6bd5989a07341011e)
#### Tuesday 2023-01-31 12:04:00 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---
## [lkodinsson/MARS](https://github.com/lkodinsson/MARS)@[10ba68a59b...](https://github.com/lkodinsson/MARS/commit/10ba68a59bb36e39c6a2cea38108fd456f67460a)
#### Tuesday 2023-01-31 12:14:48 by Loki Karolius Odinsson

Added nine new spells: Bless, Curse, Elemental Ward, Entangle, Guidance, Mental Strike, Physical Ward, Sacred Bond, and Spirit Communion
Filled out all adept bonus spells for the Faith skill
Fixed some minor errors and added some new test bestiary entries

---
## [InterNetNews/inn](https://github.com/InterNetNews/inn)@[4fe713d0e5...](https://github.com/InterNetNews/inn/commit/4fe713d0e57c42b993f6c0915baad355ff43c269)
#### Tuesday 2023-01-31 12:31:50 by Julien ÉLIE

Fix the use of Auto-Submitted header field

Use auto-generated for controlchan reports, and do not use that header
field at all for gatewaying (news2mail and nnrpd).

Thanks, Russ Allbery, for your wise thoughts:

The notifications sent by controlchan are not an autoreply to the
sender of the control message.  They are a status report sent to the
news administrator about a change made (or proposed) on their news
server by a third party.  As such, they're equivalent to the daily
report or the notification messages from innwatch.  The fact that the
change to the server was initiated by a netnews message doesn't feel
horribly relevant.  A "reply" by definition goes back to the sender
of the message; notification messages that go to third parties feel
inherently different.

Gatewaying (of which moderation is a subset) is yet a different thing,
and the Auto-Submitted header isn't appropriate here with any value.
These messages are not Auto-Submitted; they're, well, gatewayed.
This is equivalent to email forwarding; mail servers don't add
Auto-Submitted headers when they forward mails.

*If* we were encapsulating messages when sending them to moderators,
"Auto-Submitted: auto-generated" may be in the outer envelope, but
since we're transforming and forwarding a message, this is just part
of the message propagation path and thus should not be labeled with
Auto-Submitted.  The message is not, in general, auto-submitted; it was
manually posted by the poster of the message, and we're just passing it
along to its ultimate recipient.

Also, on a more practical level, addition of this header is
potentially surprising to moderators.  Their mail client may rightfully
downgrade or refile messages with Auto-Submitted headers, particularly
Auto-Submitted: auto-replied, since the vast majority of such messages
are vacation auto-replies that are of low importance or that people may
even auto-delete.  There's some risk of confusing submitted posts for a
moderated group, which are relatively important mail, for relatively
unimportant mail like vacation autoreplies or automated status
messages.

see #255

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[7780a50f68...](https://github.com/TaleStation/TaleStation/commit/7780a50f68ee0df72c2a8c0130ac850087b4b547)
#### Tuesday 2023-01-31 13:24:34 by TaleStationBot

[MIRROR] [MDB IGNORE] Refactors crew records (#4252)

Original PR: https://github.com/tgstation/tgstation/pull/72725
-----
## About The Pull Request
I have attempted or otherwise started this project at least 4 times. I
am sick of it being on my calendar. The code needs it. I need it.

- This makes crew records a proper datum rather than assigning
properties record.fields.
- General, medical, and security records are merged.
- Did some slight refactoring here and there for things that looked
obvious.
- Wanted states are now defined (and you can suspect someone through
sechud)
- pAI (unrelated but annoying) had some poorly named exported types that
i made more specific
- Job icons are moved back to the JS side (I wanted to get icons for
initial rank without passing trim)

<details>
<summary>previews</summary>

Editable fields & security console

![CM6d74brnC](https://user-images.githubusercontent.com/42397676/213950290-af6cfd76-eb8b-48e9-b792-925949311d9a.gif)

Medical records

![bFJErsvOaN](https://user-images.githubusercontent.com/42397676/214132534-59af1f8c-9920-4b51-8b27-297103649962.gif)

Look and feel of the more current version

![cxGruQsJpP](https://user-images.githubusercontent.com/42397676/214132611-0134eef0-e74c-4fad-9cde-328ff7c06165.gif)

</details>

## Why It's Good For The Game
TGUI'd some of the worst UIs in the game.
Creating new records is made much simpler. 
Manifest_inject is made readable.
Probably bug fixes

## Changelog

:cl:
refactor: Crew records have been refactored.
refactor: Medical records -> TGUI
refactor: Security records -> TGUI
refactor: Warrants console -> TGUI
qol: Players are now alerted when their fines are paid off.
qol: Cleaned up sec hud examination text.
qol: Adding and deleting crimes is easier.
qol: Writing crimes in the console sets players to arrest.
qol: You can now mark someone as a suspect through sec hud.
/:cl:

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [alpachinof/tailwind-landing](https://github.com/alpachinof/tailwind-landing)@[492187a514...](https://github.com/alpachinof/tailwind-landing/commit/492187a5141fb39a27b56188639da7bc10d0a684)
#### Tuesday 2023-01-31 13:28:00 by alpachinof

Merge branch 'master' of github.com:alpachinof/tailwind-ecommerce-template
fuck you

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[059554ae16...](https://github.com/TaleStation/TaleStation/commit/059554ae16e6eb4efe68dc2f9a4c0df031622998)
#### Tuesday 2023-01-31 14:00:48 by TaleStationBot

[MIRROR] [MDB IGNORE] Refactors Suicide Verb + Basic Mobs (actually all (most) living mobs) Can Now Suicide (#4258)

Original PR: https://github.com/tgstation/tgstation/pull/72919
-----
## About The Pull Request

On the tin. There was a lot of needless copy-paste and a lot of
single-letter vars and weird indentation and... well just all of it was
at least eight years old. So, I decided to "abstract" as much as I could
of it out instead of piling onto the big copypaste clusterfuck for
implementing basic mob suicide.
## Why It's Good For The Game

Fixes #72903

Having more procs that can be easily repeatably called to the same
results is much better than having to transplant the same exact three
lines everywhere. It's also a good first step to further in-depth
behavior by allowing sub-type overrides of certain procs (which is quite
nice). Just feels more extensible overall for the next guy who wants to
add funny suicide behavior whenever they might come around.

There's probably a few better ways to do what I did, but I wrote code
comments explaining why I did what I did. I think there's a few ways to
make it more agnostic, but I think that'll be another can of worms that
will bloat out an already quite large PR. Let's just get the framework
set.

(this refactor should also make it quite easy to unit test suicide
actions :eyes:)
## Changelog
:cl:
fix: All Mobs (including Basic mobs) are now able to suicide. (warning:
some exclusions remain)
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [GPhonix/GIT_DEMO](https://github.com/GPhonix/GIT_DEMO)@[254f7d4469...](https://github.com/GPhonix/GIT_DEMO/commit/254f7d446940312f34cb076b3ff0604247b4a415)
#### Tuesday 2023-01-31 14:01:44 by GPhonix

Merge pull request #2 from arisery/master

添加了FUCK YOU

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[973726fb67...](https://github.com/TaleStation/TaleStation/commit/973726fb67b887cb15ce1b7da2135504c471bdf1)
#### Tuesday 2023-01-31 14:02:33 by TaleStationBot

[MIRROR] [MDB IGNORE] External Organ Rework: new bodypart_overlay system (#4260)

Original PR: https://github.com/tgstation/tgstation/pull/72734
-----
Bodypart overlays are now drawn by the new /datum/bodypart_overlay
datum.

External organs no longer draw anything and instead add a special
/datum/bodypart_overlay/mutant to the bodypart, which draws everything

Makes it way easier to add custom overlays to limbs, since the whole
system is now modularized and external organs are just one
implementation of it

I haven't moved anything but external organs to this new system, I'll
move eyes, bodymarkings, hair, lipstick etc to this later

New pipeline is as follows:
- External organ added to limb
- External organ adds /datum/bodypart_overlay/mutant to limb to
bodypart_overlays
- Limb updates its icon, looks for all /datum/bodypart_overlay in
bodypart_overlays
- Very cool new overlay on your limb!

closes #71820

:cl:
refactor: External organs have been near-completely refactored. 
admin: Admin-spawned external organs will load with a random icon and
color
fix: fixes angel wings not working for non-humans (it was so fucking
broken)
fix: fixes external organs being invisible if they werent initialized
with a human
/:cl:

### Why this is good for the game
External organs are cool but are pretty limited in some ways. Making
stuff like synthetic organs is kinda fucked. I tried and it was dogshit.
Now you can just give an icon state and icon and you're good (using
/datum/bodypart_accessory/simple)

Stuff like eyes, cat ears and hair seem like good choices for extorgans,
but don't quite work for it because their icons work a lot differently.
This solves for it completely since any organ (or object or whatever)
can add it's own icon to a bodypart.

Want to add an iron plate to someones head? Go ahead. Want a heart to
stick out of someones chest? No problem.

---------

Co-authored-by: Time-Green <timkoster1@hotmail.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [Glorycs29/Leetcode-daily-2023](https://github.com/Glorycs29/Leetcode-daily-2023)@[b80067144c...](https://github.com/Glorycs29/Leetcode-daily-2023/commit/b80067144c5ed5e352a17531efbb45979cefdcd3)
#### Tuesday 2023-01-31 14:06:16 by glory1607

Create Best team with no conflict(Leetcode).cpp

Anytime I couldn't solve a problem, the above question bugged me alot. I have a train of thought which I use to get to the solution. Feel free to pick what works for you and device your own methods to arrive at solutions.

Thinking forward
In this train of thought, we first look at all information that is available to us. We are given 2 arrays of scores and age and the problem suggests that it has something to do with ordering w.r.t ages.
The word ordering quickly suggests that we can sort the input based on ages. ( But what kind of sort ? Ascending or Descending ? )
Will this sorting even take us closer to the solution ?

Jot down an example to answer yourself.
Let the scores array and ages array be the following ( Try to be as random as possible ) :
scores : [ 10, 2, 6, 4, 9 ]
ages. : [ 5, 1, 4, 5, 7]

Sorting the above array it by age (ASCENDING) leads me to ( If ages are equal sort ascending by score )
scores : [ 2, 6, 4, 10, 9 ]
ages. : [ 1, 4, 5, 5, 7]

Now that we get here, let's observe the constraints again.
Team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Let's modify this statement for a pair of sorted arrays. Since the arrays are now sorted by age, any younger player comes before an older player. This means, IF I am choosing a bunch of players for my solution, THEN, in the order from left to right in scores array, I am allowed to choose scores as long as they are increasing --> More strictly, they arenon-decreasing because it is allowed for a score of younger player = score of older player.
With the scores being [ 2, 6, 4, 10, 9 ]
I can pick a team with [2, 4, 9] => Total = 15
I can pick a team with [2, 6, 10] => Total = 18
Note: In doing the above, I DID NOT consider the age array at all! Because, inherently, age of any element on the left is less than or equal to the ones of the right. (For i < j, age[i] <= age[j] )

Now I can reformulate the problem statement saying,
We are given one array (HERE Scores array) and we can choose any number of elements in the order from LEFT to RIGHT , PROVIDED that the sequence of elements I pick are non-decreasing.

To put it more formally,
We have to select a sequence S in the given array A, such that for this sequence S any pair of indices i, j should yeild S[i] <= S[j], and we have to maximize sum(S)

So far we have simplified whatever information that was given to us. Let's now go to the next step.

Thinking backwards
In this train of thought, we think What topics is this problem related to ?
Brainstorm your ideas in this step to find what is relevant to this problem. More formally, the questions you ask yourself are ( the following are random ideas just to see what sticks )
Can I apply two pointers ? ( Doesn't look like it! )
Can I think of graphs ? ( To be honest, I thought about this to be graph problem for a long time. I thought is it about finding longest path where edges are given between younger player and older player based on age and score constraints. But this didn't lead me anywhere )
I see sequence in my problem statement, does this involve any Longest Increasing Subsequence Methods ? (But again LIS is for increasing sequence, but I need non-decreasing, Do I need to tweak LIS probably? ( You just hit Jackpot! Congratulations!! )

Here, if you see my above train of thoughts, in thinking about graphs I was going orthogonal to the solution. IF you see yourself doing this, it is totally fine. What is important is that after you have solved the problem, DON'T jump to the next problem yet. TRY to fix your train of thoughts. Ask yourself, where could you improve? What questions should I ask myself so that I push myself closer to the solution ? What conclusions did I reach that I dropped the idea that Graphs isn't the right solution ? How can I reach this conclusion faster ?

At first, the answers to above questions are difficult to reach, but with practice, this will become second nature and your direction of thoughts will deviate less from the intended solution.

Constraints
BEFORE, we jump to the solution, one IMPORTANT aspect of problems are the constraints. Experienced programmers always look at constraints first.
In this case, let us see what information can be derived from the constraints given to us.
We have ,

* 1 <= scores.length, ages.length <= 1000 
* scores.length == ages.length
* 1 <= scores[i] <= 106
* 1 <= ages[i] <= 1000
These constraints give us answers to the following questions:

What solutions are admissible ?
The length of the input arrays is atmost 1000, ages.length and scores.length <= 1000 MAX.
Considering that approx 10^8 computations is 1 second of processing. We can see that O(n^2) solution is admissible because 1000*1000 = 10^6 which is approx 0.01 seconds.
However, had scores.length been 10^5, then O(n^2) solution is not admissible as n^2 = (10^5)^2 = 10^10 ~ 100 seconds. And we need an O(n log n) or O ( n root n) solution instead.
What data type should I be using to store my answer ?
TO answer this, let's see what is the maximum value of answer we can get, and compare that with max value different data types can hold.
scores[i] <= 10^6, and scores.length <= 1000 this means that the max answer we can get is 10^6 * 1000 = 10^9. ( A test case where all values are equal to 10^6 and all age are equal, allowing us to select the whole bunch as the answer ). An INT type can store this max value easily within itself.
However, IF scores[i] <= 10^7 , then in this case the max value for our answer becomes 10^10, suggesting that using INT will cause an overflow, and we need to use LONG LONG type to manage overflows.
A good rule of thumb, is to look at constraints first to arrive at a reasonable time complexity, then think forward to simplify the problem, then think backward to see what kind of problem I am looking at.

---
## [TianWalkzzMiku/SRyzen-sdm660-4.19](https://github.com/TianWalkzzMiku/SRyzen-sdm660-4.19)@[4802d1e9bf...](https://github.com/TianWalkzzMiku/SRyzen-sdm660-4.19/commit/4802d1e9bf3957dbc2c5af3a2c8d06a9d489b962)
#### Tuesday 2023-01-31 14:12:16 by Peter Zijlstra

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92

---
## [andyundso/wed3-summary](https://github.com/andyundso/wed3-summary)@[0d6e434aec...](https://github.com/andyundso/wed3-summary/commit/0d6e434aec719e4f8979de51af602fed57bb0caf)
#### Tuesday 2023-01-31 14:14:40 by Andy Pfister

Summarize week 8

In a rush, I made a silly blunder,
Committed my changes to the summary, so much wonder.
Thought it was week 5 and 6, but oh what a shame,
Turned out to be week 6 and 7, my error, my blame.

So let this be a lesson to all, slow and steady,
Take a step back, double check, and never be ready.
To make mistakes, in haste or otherwise,
It's okay, we learn and grow, with each stumble, we rise.

---
## [hypered/curiosity](https://github.com/hypered/curiosity)@[de254051c2...](https://github.com/hypered/curiosity/commit/de254051c2d53ba79b91b57dfa5f3d7cd4d24c0d)
#### Tuesday 2023-01-31 15:47:29 by Ashesh Ambasta

@noteed

This fixes the broken tests: for users.
I'm sorry but I had not assumed that the IDs were being stored in
newtypes with the prefixes.

This broke all tests and needed to be fixed.

This commit /should/ be able to fix them using the newtype machinery.

--

The earlier ID prefixing introduced some data redundancy.

For example:

```
UserId "USER-1"
```
is not very useful: it should not contain the prefix `USER-` inside
the newtype value, since the newtype guarantees that the Text is a
UserId. So we were storing redundant data.

Instead, the UserId, should be stored as `UserId "1"` and only
rendered as `USER-1` etc. when serialising (show, toJSON etc.) and
vice versa for parsing.

--

I'd love to have fixed this, but I ran out of time (and we had to
leave for the evening to friends.

My apologies for that. I'll try to finish this the coming week or the
next weekend.

---
## [z3zens/android_kernel_asus_sdm660](https://github.com/z3zens/android_kernel_asus_sdm660)@[533b4d977f...](https://github.com/z3zens/android_kernel_asus_sdm660/commit/533b4d977f280abf737a3dcaaa7343fe484f2fd2)
#### Tuesday 2023-01-31 16:09:24 by Christian Brauner

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
## [psydox/tuleap](https://github.com/psydox/tuleap)@[40e2be557c...](https://github.com/psydox/tuleap/commit/40e2be557cbb16e0972f49af4beaa39636afcc3b)
#### Tuesday 2023-01-31 16:42:57 by Nicolas Terray

fix: wrong redirection for /my/

As anonymous user, try to go to the following url:
https://tuleap-web.tuleap-aio-dev.docker/my/?toto=titi&tata=tutu

Should be asked to login, and then should be redirected to this exact
url, not with a return_to parameter.

Without this, welcome modal is not displayed if user tries to access to
her personal page with an invitation token while she is not logged in.

Honestly, this part of the code is a mystery. I don't really understand
the use cases for a special treatment for "/my/" urls. I tried to insert
myself without touching too much as I am afraid to break something
already brittle.

Part of request #29614: Invited users shouldn't be mandated to re-confirm their email

Change-Id: I2d704f4ea16b37c37366aec75e5596a003edb756

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[e07ffe6c0c...](https://github.com/git-for-windows/git/commit/e07ffe6c0cec7334cbd08b61b3a5dd81277a45d4)
#### Tuesday 2023-01-31 17:12:18 by Johannes Schindelin

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

---
## [opengamedata/opengamedata-core](https://github.com/opengamedata/opengamedata-core)@[6ce843e47b...](https://github.com/opengamedata/opengamedata-core/commit/6ce843e47ba8d805dfd59e659ee26b43e6a561d9)
#### Tuesday 2023-01-31 17:15:31 by Luke Swanson

Properly echo the variables to the environment.

Fucking fuckity fuck fuck fuck I don't know how I was this fucking
stupid but I should probably hand in my badge after this one.
Obviously need to echo values diretly into variable names in the
environment, not a random-ass range formatting. Stupid.

---
## [AdhamAllamx/Marvel_Endgame_Game](https://github.com/AdhamAllamx/Marvel_Endgame_Game)@[e1981f86d0...](https://github.com/AdhamAllamx/Marvel_Endgame_Game/commit/e1981f86d03c7b5c0365a626436aa58bc30fb2ea)
#### Tuesday 2023-01-31 17:15:42 by AdhamAllamx

Update Game_Description

Intro
M arvel: Ultimate War is a 2 player battle game. Each player picks 3 champions to form his team
and fight the other player’s team. The players take turns to fight the other player’s champions.
The turns will keep going back and forth until a player is able to defeat all of the other player’s
champions which will make him the winner of the battle.
During the battle, each player will use his champions to attack the opponent champions either
by using normal attacks or using special attacks/abilities. The battle takes place on a 5x5 grid.
Each cell in the grid can either be empty, or contain a champion or obstacle/cover. At the
beginning of the battle, each team will stand at one of the sides/edges of the grid as a starting
position.
1
Champions
Champions are the fighters that each player will form his team from. Each champion will have
a certain type which influences how the champion deals damage to other types as well as how
much damage it will receive from them. The available types are:-
• Heroes: they deal extra damage when attacking villains.
• Villains: they deal extra damage when attacking heroes.
• Anti-Heroes: when being attacked or attacking a hero or villain, the antihero will always
act as the opposite type. If attacking an antihero, damage is calculated normally
Each champion has the following attributes and characteristics:-
• Health points: Represents the life of the champion. As long as the value of this attribute
is bigger than zero, the champion will remain alive and can act in the game. Once the
value of this attribute reaches zero, the champion is considered dead and hence, eliminated
from the fight.
• Mana: a resource that a champion uses to use his abilities. Each time a player uses an
ability, a certain amount of mana will be consumed. Once run out, the champion cannot
use any of his abilities.
• Normal attack damage: The amount of damage that the champion will inflict upon
the attacked champion while using a normal attack. This amount will be deducted from
the attacked champion’s health points.
• Normal attack range: The maximum number of cells that the attacker’s normal attack
can reach the attacked champion within. If the attacked champion is standing in distance
greater than this range, the attacker can not use a normal attack on him.
– Range is calculated by the Manhattan distance algorithm.
• Speed: Determines how fast the champion is. The faster the champion, the sooner he
can carry out his actions before other champions.
• Condition: Represents the current ability/inability of the champion to act. The champion can be active (can do some actions), inactive (can not do any actions until he is back
to active), or knocked out (defeated and can not do any action till the end of the game).
• Actions per turn: A number representing how many actions a player can do with the
champion during each of his turns. Each action will consume a certain amount of this
number. Once it reaches zero, no more actions can be done by this champion during this
turn. This attribute resets each time the turn goes to the champion.
Possible actions that can be done by a champion during his turn:
2
– Move to an empty cell.
– Do a normal attack.
– Cast an ability.
– Use Leader Ability (only if champion is the player’s chosen leader)
Abilities
These are special attacks that a champion can use. They are categorized under the following
categories:-
• Damaging abilities: Abilities that deal damage to the opponent champion(s) or covers.
• Healing abilities: Abilities that restore health points to friendly champion(s).
• Effect abilities: Abilities that can empower or weaken their targets by applying different
effects. These effects can last for multiple turns and will affect how the affected champion
interacts or reacts to abilities or attacks.
Example of some effects: stun, weaken, embrace, shield, silence, disarm.
Abilities have different targets and ranges. Some abilities are single target abilities which
affect only a single champion (or a cover in some cases) per use. Or can affect any champion
standing in a certain area (area of effect). These areas can be directional (Horizontal or
Vertical), or Circuilar (affect an area surrounding a central point). Finally, some abilities
can affect all friendly or opposing champions.
Each ability requires a certain amount of action points to be present in the champion
casting them as well as some mana. Also, each ability has a specific range of cells that
the target needs to be present in it in order for the ability to affect it.
Leader Abilities
At the beginning of the battle, each player promotes one of his champions to be the leader of
his team. The leader will then receive a special ability based on his type that can be used only
once per battle.
3
Gameplay Flow
Each player will select his three champions to form his team. The champions will take turns
based on their speed. The champion with the highest speed (from all selected champions) will
begin acting first followed by the champion with the second highest speed and so on. When
the turn goes to a champion, the player controlling the champion can use him to carry out any
action as long as the champion has enough action points needed for this action and also enough
mana in case of using any of his abilities. After that, the champion can end his turn and the
turn will go to the next champion.
The turns will keep passing over the living champions till a player is able to defeat all of the
three champions of the opponent player. In this case, the game ends and the player with the
living champion will be declared the winner.

---
## [AstrlJelly/HeavenStudio](https://github.com/AstrlJelly/HeavenStudio)@[7c4636518b...](https://github.com/AstrlJelly/HeavenStudio/commit/7c4636518b2d552f0032a0c1f615c7399fb6409b)
#### Tuesday 2023-01-31 18:32:30 by AstrlJelly

BEZIER CURVES

* actual fruit animation
* toggle for random fruits (doesn't work yet)
* textbox for custom objects (doesn't work yet)
 - not user-submitted stuff, just stuff that doesn't really fit in the main dropdown menu
* some stuff i don't remember, but it's definitely stuff that's working towards making everything work.

miss anims don't work yet. at all. the objects just go flying. also the slice animation needs to be finished for both sides, and a bool needs to be added for which side to play (will be easy to do) also when you randomly slice, which is determined completely randomly (thank god)

gura-nyuuu :3 (i'm sorry)
* added a single sfx

---
## [Tastyfish/Skyrat-tg](https://github.com/Tastyfish/Skyrat-tg)@[406b6870bd...](https://github.com/Tastyfish/Skyrat-tg/commit/406b6870bd28dd78e65e59787d8c54c776078019)
#### Tuesday 2023-01-31 18:39:49 by SkyratBot

[MIRROR] adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths [MDB IGNORE] (#18785)

* adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths (#72736)

repaths a lot of gloves off /color because they were incredibly stupid
firefighter gear has gotten an update (it doesnt cover hands anymore
though, you need something else)
firefighter helmets no longer hide your mask or glasses

![image](https://user-images.githubusercontent.com/23585223/212542599-c004d0e4-c141-40b4-a1bb-c838f9893c4b.png)
fixed engine goggles starting with darkness vision
to the atmos lockers adds atmospheric gloves, a pair of thick (chunky
fingers) gloves that are fireproof and fire protective, slightly shock
resistant and let you fireman carry people faster.
atmospheric firefighter helmets now are a subtype of welding hardhats,
you can enable a welding visor.
welding hardhats change mode with right click instead of altclick

im not a good spriter but i think this resprite makes them fit nicer
with other engi equipment
lets me firefighter rp

:cl:
add: Atmospheric Gloves, thick gloves that are fully fireproof and fire
protective and let you fireman carry people faster.
fix: fixes engine goggles starting with darkness vision
qol: firefighter helmets can now enable a welding visor
qol: welding hardhats change mode with right click instead of altclick
balance: firesuits no longer protect your hands
/:cl:

* Makes shit compile

* Updates the digi and snouted stuff to match the new sprites (thanks Halcyon!)

* Fixes a whole ton more issues that popped up

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [Gnuxie/Draupnir](https://github.com/Gnuxie/Draupnir)@[5d1bc0c6ec...](https://github.com/Gnuxie/Draupnir/commit/5d1bc0c6ec518d1b057a45a73b7bd95f64fc8382)
#### Tuesday 2023-01-31 18:59:07 by gnuxie

Improve HTTP Error handling.

So as a history lesson.
The Matrix Bot SDK uses the npm library "requests".
When there was a http error, matrix-bot-sdk
would literally throw the response object.
This would be a horrible 1000+line long thing to accidentally
be logged to the console via node's inspect.
Though it was inevitable since you can't be sure every catch
was handling the error correctly. Irregardless, the solution
developed at Element was to create an error object
that had concise details.
This was great, however, within the matrix-bot-sdk there is
[this](https://github.com/Half-Shot/matrix-bot-sdk/blob/f58d7ea6e24d1db8b9b8009dea4cd97cbff54d0c/src/http.ts#L66)
awful line of code which logs every http error as error using the
matrix-bot-sdk logger.
This wastes so much log space and causes alarm fatigue,
rather than muting the module, the action instead taken
was to redact stack traces from http errors.
This was not a good idea.
Eventually matrix-bot-sdk was updated to have a MatrixError type
when a request was performed via the client-server api that had an
error.
matrix-appservice-bridge depends upon this and so Mjolnir now needs
to be updated to throw MatrixError's.
We have gone a step further in this commit and also muted
the matrix-bot-sdk http module, to stop the alarm fatigue problem
https://github.com/turt2live/matrix-bot-sdk/pull/158

---
## [dagster-io/dagster](https://github.com/dagster-io/dagster)@[84c7e77a81...](https://github.com/dagster-io/dagster/commit/84c7e77a8170aa11b53ef10fda93bc4b33134b1e)
#### Tuesday 2023-01-31 19:19:58 by Ben Gotow

[dagit] Add ErrorBoundary to Dagit to reduce severity of React errors (#11824)

### Summary & Motivation

Corresponding Internal PR:
https://github.com/dagster-io/internal/pull/4659

Hey folks, this PR wraps key components of Dagit in React "error
boundaries", which give us the opportunity to present errors more
gracefully and let users recover / continue to use other parts of the
app. So far I've added them to:

- The top component that renders page content (everything below the
toolbar)
- The details section of the asset partitions and events pages (which
was a production issue yesterday)
- The asset graph and asset graph sidebar
- The op graph and op graph sidebar
- The run logs container and the run gannt chart
- The instance run timeline
- The `<Dialog />` component (errors in a dialog should never take down
the rest of the page)

Anywhere else we should add these?

### Resetting after errors

The component I added takes a `resetErrorOnChange` prop which acts a bit
like a useMemo dependency list -- if any of the values change and it's
in an error state, it resets the error and tries to render it's subtree
again. We need this for cases where the error boundary is not unmounted
/ remounted but it's content could meaningfully change. (eg: you click
another asset or tab). I think this is better than putting a `key={}` on
the Error Boundary because that would force a re-render on the whole
subtree in the happy case.

### Cloud

In cloud dagit, we need to implement a top level context exposed by the
new Error Boundary class in order to send errors (which are now caught)
to DataDog. I think we also want to change the text to let users know
that their errors are automatically submitted to us, so I made that text
configurable. We can also disable the display of the error stack trace
in cloud if we want to.

### How I Tested These Changes

I tested these changes by adding `throw new Error()` to various React
render methods and verifying that Dagit fails more gracefully. I also
verified that this can catch the infinite recursion bug, which is a bit
of an interesting one, by reverting to last night's code and running
without the GraphQL patch.


![image](https://user-images.githubusercontent.com/1037212/213761842-9c01de3e-aa19-40e8-8ea5-2db143684ea6.png)


![image](https://user-images.githubusercontent.com/1037212/213762126-e94f2f8e-1a82-4d71-b624-525533c34d28.png)

Edit: Updated styling

<img width="727" alt="image"
src="https://user-images.githubusercontent.com/1037212/213804637-46343cb0-34de-4154-bd5e-1f61d0a30e92.png">

Co-authored-by: bengotow <bgotow@elementl.com>

---
## [PixelExperience-Devices/device_samsung_sm7125-common](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common)@[176dcda2d1...](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common/commit/176dcda2d1feb3c58bc0bc162de2de3c8df18f5f)
#### Tuesday 2023-01-31 19:21:29 by Ruchit

sm7125: (note to self) dont pick this ye dumb idiot its only for wip branch so you can test shit better k bye

---
## [yaap/packages_apps_Settings](https://github.com/yaap/packages_apps_Settings)@[6a3b66de67...](https://github.com/yaap/packages_apps_Settings/commit/6a3b66de676ae108aa32dd754cccaf77e25cf347)
#### Tuesday 2023-01-31 19:22:51 by Ido Ben-Hur

Settings: Refactor and clean connectivity check preference

wow this was just horrible...

Made this preference way more maintainable and runtime effective:
* Declare the preference in xml instead of hardcoding - this makes it searchable, more maintainable and is also better runtime wise
* Use arrays instead of manually naming each URL
* Use an ArrayList to handle index <-> setting relationship more easily
* Use static imports instead of literal calls
* Actually handle cases of non availability
* There is absolutely no reason to handle OnResume here
* Get rid of useless functions
* Get rid of useless imports
* Move resources to the proper custom files so we don't confuse translators
* More, too lazy. Don't write shit code please. Thank you.

---
## [Cenrus/Daedalus-Dock](https://github.com/Cenrus/Daedalus-Dock)@[4b69f5d536...](https://github.com/Cenrus/Daedalus-Dock/commit/4b69f5d53635f72e87dd045b4ba00bc7478ce83a)
#### Tuesday 2023-01-31 19:30:36 by Kapu1178

Speed up the roundstart significantly (#147)

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) (#69376)

About The Pull Request

Just to be clear, when I refer to time here, I am not talking about cpu time. I'm talking about real time.
This doesn't significantly reduce the amount of work we do, it just removes a lot of the waiting around we need to do for db calls to finish.

Adds queuing support to sql bans, so if an ongoing ban retrieval query is active any successive ban retrieval attempts will wait for the active query to finish

This uses the number/blocking_query_timeout config option, I hope it's still valid

This system will allow us to precache ban info, in parallel (or in batches)
With this, we can avoid needing to setup all uses of is_banned_from to support parallelization or eat the cost of in-series database requests

Clients who join after initialize will now build a ban cache automatically

Those who join before init is done will be gathered by a batch query sent by a new subsystem, SSban_cache.

This means that any post initalize uses of is_banned_from are worst case by NATURE parallel (since the request is already sent, and we're just waiting for the response)

This saves a lot of headache for implementers (users) of the proc, and saves ~0.9 second from roundstart setup for each client (on /tg/station)

There's a lot of in series is_banned_from calls in there, and this nukes them. This should bring down roundstart join times significantly.

It's hard to say exactly how much, since some cases generate the ban cache at other times.
At base tho, we save about 0.9 seconds of real time per client off doing this stuff in parallel.
Why It's Good For The Game

    When I use percentages I'm speaking about cost per player

I don't like how slow roundstart feels, this kills about 66% of that. the rest is a lot of misc things. About 11% (it's actually 16%) is general mob placing which is hard to optimize. 22% is manifest generation, most of which is GetFlatIcons which REALLY do not need to be holding up the main thread of execution.

An additional 1 second is constant cost from a db query we make to tell the server we exist, which can be made async to avoid holding the proc chain.

That's it. I'm bullying someone into working on the manifest issue, so that should just leave 16% of mob placing, which is really not that bad compared to what we have now.
Changelog

cl
code: The time between the round starting and the game like, actually starting has been reduced by 66%
refactor: I've slightly changed how ban caches are generated, admins please let me know if anything goes fuckey
server: I'm using the blocking_query_timeout config. Make sure it's up to date and all.
/cl

* manifest_inject() stuff

* Fixes role banned players not being banned from roles that they are banned from (Option Two) (#69703)

I feex

* Saves on average 10 seconds from roundstart times (#71730)

## About The Pull Request

When runlevels change mid work, subsystems running behind have their
next_fire updated.
It's offset by a sum of random numbers, so things don't bunch up,
especially KEEPTIME SSs

The trouble is we have so many subsystems that get added at roundstart
that this offset gets LARGE, like 10 seconds on average.

So instead of randomly offsetting, why not "fill" a set of time slots?
Only 1 keeptime subsystem a tick, and 4 others. Then we just fill up
those buckets and get to it (also don't offset things that are already
processing)

I've talked to mso a bit about this. What he reccomended was sampling a
random time withing a 2 second window.
I'm not totally sure why, kinda waiting for him to tell me off, if he
does I'll fix things up.

This pattern takes the max possible delay from 16 (76 * 5 / 20)) seconds
to 0.7 (56 / 4 / 20)
It obviously scales with subsystem count, but I like this scaling a bit
better

I've applied the same pattern to the offsetting we do at the start of
Loop(), for ticker subsystems. I am less confident in this, it does take
last fire times from at worst 3.75 seconds (15 * 5 / 20) to a static
0.75 (15 / 20)
As stated I'm less sure of this, hoping to get mso'd so I can clean
things up

## Why It's Good For The Game

Makes roundstart snappier

## Changelog
:cl:
code: Roundstart "starting" should be much snappier now
/:cl:

Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>

* fix missing macro

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Timberpoes <silent_insomnia_pp@hotmail.co.uk>
Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>

---
## [rolfesl/darkfall](https://github.com/rolfesl/darkfall)@[19cac157e5...](https://github.com/rolfesl/darkfall/commit/19cac157e55e32dbd9c61ad6b6fb2d52dea3a18c)
#### Tuesday 2023-01-31 19:39:55 by rolfesl

Add files via upload


#############################READ ME###########################


In this read me file you will find an instillation guide with links and a rough guide for things to do in the standalone.

Visit our website and forums for more information darkfallorigin.boards.net/


########################INSTILLATION GUIDE#########################


1. Download the .rar from the FTP. ftp://178.254.20.206/ into your browser, username dfopublic. Find the folder called Nat(UPDATED VERSION HERE) and download the .rar file there.


2. Extract it using your extractor of choice. I heavily advise extracting to a default C drive with the main folder called DFStandalone0.2, as that will mean you don't have to make many more changes.


3. Go to Build/All/Bin, open standalone.xml with text editor, 

find lines 13, 26 and 28, that contain C:\DFStandalone0.2\... and replace it with the path your game was downloaded to, i.e.


<VMOption Value='-Djava.class.path=D:\Example\DF Standalone 0.2\'/>

...

<Logger Filename='D:\Example\DF Standalone 0.2\data\standalone_%InstanceID%.log' Type='FILE'/>

...

<FileManager ArchiveName='D:\Example\DF Standalone 0.2\data\dfdata' EnablePreload='false' LoadData='false' LookupMode='NativeOnly' ReportNameFixups='true' ReportNativeFallbacks='true'/>


4. Go to Control Panel > System > Advanced System Settings > Environment Variables and make a new variable for BOTH user and system.


Variable name = SFBASE


Variable value = C:\DFStandalone0.2 (or what your directory is. No spaces)


5. Launch with RunStandalone_1048debug.bat file found in the root directory. It should launch a command prompt and then the game. Alternatively, launch with our early launcher DarkfallEmu.exe but do this ONLY if your directory is C:\DFStandalone0.2\, otherwise it won't work. Future versions should include a launcher that patches future updates.



###########################BASIC GUIDE##########################

How to move:

F7 - flymode toggle, Space to ascend, C to descend, LShift to boost

F8 - freecam toggle


Press Enter and type this command to get skills (like walking) working: /skill_add_all 100 - enter it twice, as there's too many skills to add in one go.


/help command for all commands, including admin and GM commands. Most work. A future guide on these commands are planned. Stay tuned on the forums.



#########################ADVANCED GUIDE########################



Use /gm_teleport_to_tile [TILE ID] to teleport to any tile. Find the tile ID by hovering over it with your mouse on the worldmap.


Use the /equip "r_resource name" command for adding items to your backpack. You can find the resources in data\dev\dfdata\xml-files\server\resource


Use /spawn_resource_mesh "r_resource name" to spawn the physical object, this includes most weapons, mobs and buildings. Use the resource names found in the resource folder.


Use /spawn_monster "r_resource name" - be aware you can only spawn one per session, and killing them will likely crash the game for this version. Try r_devil or r_demon if you want a punching bag, or r_bear arctic if you want to kill something.


Monsters spawn in tiles S18 to V21. Spawned monsters currently cause significant 'load lag' and it's quite annoying. You may want to turn these off, and here's how:


You have to change the following to configuration_standalone_agon

LINE 14

<LoadDynamicAIFromLevel>

<SFBool Value="false"/>

</LoadDynamicAIFromLevel>

Also make sure that LINE 44 <CreateAIObjectSpaceManager> is false. Set these to TRUE if you want them back.


Type /help "command name" for a short explanation of the command. Type /help and the start of the command to get commands close to it, like /help spawn will list all commands starting with spawn.


To capture and build a city, you first need a clan. The clan GUI or journal is not yet made, but it's not needed yet. Type /clan_create NAT KRO (or whatever you want to name your clan). Then find your city, probably CBAY /gm_teleport_to_tile CC07, and type the command /city_create "city name". Use the clan shard in your inventory. Then type /equip "r_module building:10000" and alternative use the bindstone (G if it's default, J if its my bindings) and go crazy. There's a command for resetting the timer between conquests, but I can't remember it, so gso.

Villages and Sea Fort: Only village that works is Chilbourne (tile S21) and Sea Fortress is BurningGlory (tile R04). We know they work, getting them all to work is a low priority right now. It's just a matter of labour and time. 



/village_create Chilbourne

/fortress_sea_create BurningGlory




*Player race, attributes, skills: data\dev\dfdata\xml-files\server\persistence\aventurine\character.xml*


*Player spawn position: data\dev\dfdata\xml-files\server\persistence\aventurine\clientobject.xml*


*(you can reference the ingame map for x,z coordinates and set the spawnpoint to the place you like)*


*Player inventory: data\dev\dfdata\xml-files\config\gamelogic_configuration_av.xml*


*(you can write r_Weapons to get *all* the weapons in the game, also r_Figurines/r_Armor/r_Greataxes etc.)*


*Day/Night cycle time, character creator mode:data\dev\dfdata\xml-files\config\configuration_standalone_agon.xml

(character creator does not save your character)*


Game log stored at data\standalone_1.log



PLEASE REFERENCE THE REDDIT THREAD OR THE DARFALL EMULATOR FORUMS FOR UP TO DATE GUIDES.


#########################KNOWN BUGS & ISSUES#############################



-Sometimes you duplicate yourself (and your mount too if you're mounted)


-Mobs aren't doing anything, just idling


-Attacking mobs melee seems to be bugged the same way as attacking mounts is, ranged seems to work fine


-Game crashes after you kill a monster with broken inventory(from what I've figured it should contain natural weapons)


-Gravestones aren't solid and you cannot open them


-Some skills don't work, most notable Wall of Force.


Current list of issues can be found here: darkfallorigin.boards.net/thread/110/current-issues-standalone



PLEASE VISIT THIS THREAD IF YOU HAVE ANY ISSUES darkfallorigin.boards.net/thread/228/darkfall-standalone-version-install-guide

---
## [CDCgov/prime-reportstream](https://github.com/CDCgov/prime-reportstream)@[8b92a1e515...](https://github.com/CDCgov/prime-reportstream/commit/8b92a1e515d1f0e0c68d9471fcb1163432dae487)
#### Tuesday 2023-01-31 19:41:02 by Stephen Kao

Experience-7891: Disable organization-specific fetches as admin (#7928)

This changeset disables a few Organization-specific requests to mitigate the number of 404s we're getting as admins try to fetch Organization resources:
- Organization settings
- Deliveries
- Submissions

There's not a one-size-fits-all solution here given the different fetch mechanisms we already have and how the data is rendered, so I tried to add minimal changes to prevent disrupting anything down the line.  I think going forward, we can make a generic `useOrganizationQuery` hook that'll automatically be disabled if the user is logged in as an admin without impersonating an Organization.  There are a lot of layers with our fetching that in my opinion should be untangled, but that's out of the scope of this pull request.

---
## [Xyce/Xyce](https://github.com/Xyce/Xyce)@[87f47161f7...](https://github.com/Xyce/Xyce/commit/87f47161f72bc2b56de8cb04fb01bf854d7a885e)
#### Tuesday 2023-01-31 19:43:18 by Tom Russo

Let configure detect ABI clashes

Ever since the very first commit of configure.ac (f5ebf77, back in
2002), after hunting down all required libraries, Xyce's configure
does a simple check to see if the entire link line actually works.
This was something that Tammy Kolda had suggested back in those days,
and I took her advice.

Thing is, when configure is hunting down libraries it's already trying
to link small programs with them, so this test has always been
pointless.  All it does is make sure the libraries can be found, which
honestly we already did earlier.

And worse, ever since we started using the Trilinos Makefile.export
thing instead of probing libraries normally, we NEVER actually link
meaningful test programs with trilinos anymore.

This means that while the libraries are found and a link of a trivial
program succeeds, it could be the case that Trilinos has been compiled
with a compiler that uses an ABI that is incompatible with the one
we're trying to use now.

This came up this weekend (again) when Eric tried to build Xyce on one
of the ASCIC machines and tried to use our precompiled Trilinos
archdir for gcc8.  These libraries were compiled with RHEL7 devtools-8
gcc 8.3, but Eric was using CDE gcc 8.4.

RHEL devtools gcc8 is compiled to use the old GCC ABI for compatibility
with the native gcc4, but CDE gcc 8.4 is compiled with the default,
new ABI.  It is not possible to use one with the other unless special
macros are defined to make it use the the non-default ABI.

And because we were only testing whether libraries would link by
linking an empty main function with the libraries, no Trilinos
functions are actually needed and so the linker never pulls them in
and tries to use them.

So configure succeeds, the build proceeds all the way to the final
link phase, and then a semi-infinite number of undefined symbole
errors show up.  It is frustrating and confusing for a user to have
that happen.

In this commit, I change this 20-year-old pointless link test into a
meaningful link test.  Now, configure tries to build a small test
program that includes Teuchos_RCP.hpp and tries to instantiate an
RCP.  This is a real test --- if the Trilinos libraries are
incompatible, this will fail, and fail before the user has bothered to
try to build Xyce.

if it fails, the user will get the message:
checking whether libraries (-lfftw3  -llocaepetra ...  ) will link... no
configure: error: FATAL: cannot link with the libraries detected so far ...
It may be that your compiler is incompatible with the one that was
used to build Trilinos.  See config.log for failure message.

That final error message used to include the entire list of libraries,
but that list is so freakin' long it makes the error message
unreadable (the beginning of the message scrolls off the screen before
the end of it gets printed).  So I shortened it.  The full list is in
the previous message anyway.

And config.log will have all of those undefined symbol errors instead
of them showing up at final link time of the full build.

This does not guarantee we won't get annoyed queries from users who
hit this problem, but it at least gets that frustration to
happen *before* they've spend an hour or so compiling Xyce.

---
## [lisakowen/gpdb](https://github.com/lisakowen/gpdb)@[27011bcffa...](https://github.com/lisakowen/gpdb/commit/27011bcffa74a5113c9b5408c678315e74fb9a70)
#### Tuesday 2023-01-31 20:40:51 by Tom Lane

Fix old bug with coercing the result of a COLLATE expression.

There are hacks in parse_coerce.c to push down a requested coercion
to below any CollateExpr that may appear.  However, we did that even
if the requested data type is non-collatable, leading to an invalid
expression tree in which CollateExpr is applied to a non-collatable
type.  The fix is just to drop the CollateExpr altogether, reasoning
that it's useless.

This bug is ten years old, dating to the original addition of
COLLATE support.  The lack of field complaints suggests that there
aren't a lot of user-visible consequences.  We noticed the problem
because it would trigger an assertion in DefineVirtualRelation if
the invalid structure appears as an output column of a view; however,
in a non-assert build, you don't see a crash just a (subtly incorrect)
complaint about applying collation to a non-collatable type.  I found
that by putting the incorrect structure further down in a view, I could
make a view definition that would fail dump/reload, per the added
regression test case.  But CollateExpr doesn't do anything at run-time,
so this likely doesn't lead to any really exciting consequences.

Per report from Yulin Pei.  Back-patch to all supported branches.

Discussion: https://postgr.es/m/HK0PR01MB22744393C474D503E16C8509F4709@HK0PR01MB2274.apcprd01.prod.exchangelabs.com

---
## [boyflo06/BITECOIN](https://github.com/boyflo06/BITECOIN)@[d505c3e4bb...](https://github.com/boyflo06/BITECOIN/commit/d505c3e4bb05de3a1395cb4636f1a580dfcfbee9)
#### Tuesday 2023-01-31 20:41:15 by boyflo06

forgot to change version to 1.0.6. i am so fucking sick of this. every single time if fucking forget it. I spend so much time haveiong to push new fucking coimmits just because I keep forgettin,g to change these shitty versions but i can,ty fucking change them because of web apps and i know that the fucking shitty users on thiçs platform will obviouskly just keep the old vbersion to exploit the problems thje past versions had. I am so fucking sick of this. I am tired tired porbably already said that I am tired and cant deal with this shit anymore. I just want tp have a systeme that automatically changes but ofc it doesnt alreadyexist. Fuck this shgitty world

---
## [smogon/pokemon-showdown](https://github.com/smogon/pokemon-showdown)@[5cbb317a4c...](https://github.com/smogon/pokemon-showdown/commit/5cbb317a4c62a59351010c006be62b37e2a029e2)
#### Tuesday 2023-01-31 20:42:16 by sexy90gxebattlefactoryplayer

Gen 8 Battle Factory: Remove Darmanitan-Galar's Choice Band set (#9354)

* Gen 8 Battle Factory: Remove Band set from Ubers Darmanitan-Galar 

Credentials: https://cdn.discordapp.com/attachments/1042959218208157696/1067534457160089731/image.png (i am "lost wind's elegy")

Darm-G's firepower is just fine with scarf; there aren't many (if any?) relevant 1hkos or 2hkos you miss out on compared to band. The only one I can think of is missing out on the OHKO vs Sp. Def Necrozma Dusk Mane, and nobody's leaving their NDM in anyway + you probably have like 12 other things to deal with it.

Without scarf, however, you miss out on really good source of offensive checking and revenge killing potential. Scarf outspeeds huge threats like non scarf Yveltal, Eternatus, Calyrex-Shadow, etc. 

What sparks had to say about band darm in proper SS Ubers:
sparks — Today at 1:53 PM
not really but with band building needs to be more focused cos the speed over the 90s and etern etc is insane with scarf

sparks — Today at 1:54 PM
while with band you're very much focused on "how to take out ndm and capitalize while not being weak to ho"

As a secondary factor, it would make Ubers in BF a lot better. Currently you have to not only win the coinflip of what move Darm clicks but also the coinflip of what item it is. Both of these are more or less up to random chance.

* Update data/mods/gen8/factory-sets.json

---------

Co-authored-by: Kris Johnson <11083252+KrisXV@users.noreply.github.com>

---
## [Nightmerp/DragaliaAPI](https://github.com/Nightmerp/DragaliaAPI)@[56ef2d9afb...](https://github.com/Nightmerp/DragaliaAPI/commit/56ef2d9afb4c13c7f17b7e6ea9c1ce6a9e812e40)
#### Tuesday 2023-01-31 22:37:54 by Jay Malhotra

Add basic property validation (#111)

This is by no means exhaustive but the focus for now is limiting the
length of strings, particularly those which may end up in the database
-- Postgres is ridiculously forgiving with its TEXT type.

One other area worth looking at it party numbers and unit positions,
these will put the DB In a funny state but are unlikely to cause any
issues for users beyond the one with the invalid data.

---
## [Calixte/eclipse-cs](https://github.com/Calixte/eclipse-cs)@[757ee0447c...](https://github.com/Calixte/eclipse-cs/commit/757ee0447cda1f39c916ad0ee6916daaee8e7eb5)
#### Tuesday 2023-01-31 22:59:37 by Michael Keppler

infra: convert UI libraries to maven

Convert also the external libraries used by the UI bundle to plain Maven
coordinates. Import the packages provided by the libraries with the
minimum package version matching the current library version.

The version number 1.0 for jfreechart-swt is not an error. The previous
jfreechart-1.0.19-swt was part of the jfreechart-1.0.19 (without SWT)
release. It has been split out into a separate project now with version
number 1.0 (so that new 1.0 is more recent than the old 1.0.19). That's
also where the change of the "experimental" package name comes from.

In a future change we should also upgrade the libraries, but I want to
do that separately, because I remember these libraries have trouble with
the module system and its restrictions.

And finally, the target platform has been split once more as suggested
in previous comments to have the root target file only include other
targets but not reference any library by itself.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a47afd9051...](https://github.com/tgstation/tgstation/commit/a47afd905156bcc9a070db015cec7b1d1a07c578)
#### Tuesday 2023-01-31 23:17:00 by Sol N

2 New Positive Quirks! (#72912)

## About The Pull Request

I added a few quirks to a downstream that I feel fit well with tg so
here they are.

First up is Poster Boy, a quirk that gives you three mood altering
posters, similar to the traitor objective to hang up demoralizing
posters. You spawn with a box that has one poster that will uplift the
entire crews spirits and 2 that are unique to your department. Captain
counts for security and assistants get only neutral posters. Finally,
with a crayon or spraycan, if you are any antagonist you can make your
poster into one of the ones from the traitor objective.

![dreamseeker_nRy44SL9Jb](https://user-images.githubusercontent.com/116288367/214109008-6f1b4b7c-e800-4142-be6d-926a8e975973.png)
example of quirk posters
Costs 4.


Finally, the characterful Throwing Arm quirk, which lets you throw
objects further (but not harder) and means you will never miss shots
into the disposals bin.
Costs 7.

previously i had a food subscription quirk here as well but i pulled it
out and plan to re-add it as a separate PR in march, where it will now
give you ingredients to cook a meal with occasionally.

## Why It's Good For The Game

Positive quirk variety is good and fun, I think that these positive
quirks are reasonable ones that offer unique things that the current
positive quirks do not.
Poster boy gives people a reason to run around and claim wall real
estate for their department and hopefully can build more solidarity in
departments, the hidden antag feature probably has uses but is just for
styling on people.
Throwing arm offers a fun character trait that probably can have some
slight uses and encourages the use of throwing weapons and tools more.
Also it is good to have a way to never miss the disposals bin. It's so
embarrassing.

## Changelog
:cl:
add: Poster boy and Throwing arm positive quirks.
imageadd: added posters for poster boy quirk
/:cl:

---
## [PeterV989/fibaro](https://github.com/PeterV989/fibaro)@[c97e7af345...](https://github.com/PeterV989/fibaro/commit/c97e7af3459cb3ff088b22dea4201e5f14bab973)
#### Tuesday 2023-01-31 23:46:41 by PeterV989

Updating the setpoints wasn't working as expected

I installed your update and played around with it. The first glaring problem was that the setpoint for the unchanged setpoint does not need to be converted to °C. The value you are using is already in Celsius. I simply removed the call to getDegreesCelsius for that setpoint.

This next problem is very subtle. I tried to track down a way to fix it but can't quite do that yet. The problem is that when I change both setpoints in the device screen, only the last change is sent to the thermostat. What I mean by that is that since the heating setpoint is updated first, the value doesn't get updated in the traits area or properties area. Then the cooling setpoint is changed but the old heating setpoint is still in the body['traits']['sdm.devices.traits.ThermostatTemperatureSetpoint'] (perhaps because while the value may have been sent to the thermostat, the thermostat has not been read back into the body yet?). My thoughts were to have an setAutoThermostatSetpoint() method and use it when the device is in Auto mode. But, for the life of me, I can't see where those methods are connected to the event system. That may not make sense within the context of the Fibaro system but IMHO the documentation is very sparse and your ability to have hunted down the mechanisms for all of this is astounding. (Maybe when I grow up I can be just like you [weird American humor]).

And finally, this won't be a problem for me but a final check should prevent the cooling setpoint to be less than the heating setpoint. I notice in the Nest app when I bump one value up or down towards the other value it automatically adjusts the value to keep them 2° or 3° different. Not at all sure of a clean way to do that other than to pick one and adjust it when that condition is met.

If I can help further with my setup just let me know. I'm happy to oblige.

Peter

---
## [t0-technology/linux-crs](https://github.com/t0-technology/linux-crs)@[273ad0cf56...](https://github.com/t0-technology/linux-crs/commit/273ad0cf568493f11f5401422b8943d6c79773c6)
#### Tuesday 2023-01-31 23:54:43 by Matt Kramer

ALSA: hda/realtek: Add alc256-samsung-headphone fixup

[ Upstream commit ef248d9bd616b04df8be25539a4dc5db4b6c56f4 ]

This fixes the near-silence of the headphone jack on the ALC256-based
Samsung Galaxy Book Flex Alpha (NP730QCJ). The magic verbs were found
through trial and error, using known ALC298 hacks as inspiration. The
fixup is auto-enabled only when the NP730QCJ is detected. It can be
manually enabled using model=alc256-samsung-headphone.

Signed-off-by: Matt Kramer <mccleetus@gmail.com>
Link: https://lore.kernel.org/r/3168355.aeNJFYEL58@linus
Signed-off-by: Takashi Iwai <tiwai@suse.de>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---

