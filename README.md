## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-29](docs/good-messages/2023/2023-01-29.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,851,540 were push events containing 2,543,410 commit messages that amount to 146,575,776 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [Bobthe28th/tgstation](https://github.com/Bobthe28th/tgstation)@[5e80257423...](https://github.com/Bobthe28th/tgstation/commit/5e802574231c9c6fe835c40b55f2c8aa9f1c68b4)
#### Sunday 2023-01-29 00:19:57 by Jeremiah

Refactors crew records (#72725)

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

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [hustcer/nushell](https://github.com/hustcer/nushell)@[3d65fd7cc4...](https://github.com/hustcer/nushell/commit/3d65fd7cc4f6e0db0c1c31b895feabf2be66cb0a)
#### Sunday 2023-01-29 01:36:24 by Doru

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
## [Valderabos/tetas-gays](https://github.com/Valderabos/tetas-gays)@[8f7eb766b6...](https://github.com/Valderabos/tetas-gays/commit/8f7eb766b6acac5becd192a4f6f5c453aa71fdb9)
#### Sunday 2023-01-29 01:51:38 by Do you suck dicks?

VozTremendamenteSexual ESTÁ IMPARABLE TRONCO

What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo.

---
## [ArtemisStation/artemis-tg](https://github.com/ArtemisStation/artemis-tg)@[2a4ef2367d...](https://github.com/ArtemisStation/artemis-tg/commit/2a4ef2367dd7db73ba0adfdc300a5093678b7746)
#### Sunday 2023-01-29 02:43:54 by san7890

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
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[8cb4947084...](https://github.com/carshalash/tgstation/commit/8cb4947084edffc9476c40ea6283b68e818f48bd)
#### Sunday 2023-01-29 03:02:29 by Jacquerel

AI actions won't unassign each other's movement targets & Mice stop being scared of people if fed cheese  (#72130)

## About The Pull Request

Fixes #72116 
I've had a persistent issue with basic mob actions reporting this error
and think I finally cracked it
When replanning with `AI_BEHAVIOR_CAN_PLAN_DURING_EXECUTION` it can run
`Setup` on one action leading to the plan changing, meaning that it runs
`finishCommand` to cancel all other existing commands
If you triggered a replan by setting up a movement action in the middle
of another movement action, cancelling the existing action would remove
the target already set by the current one.
We want actions to be able to remove _their own_ movement target but not
if it has been changed by something else in the intervening time.

I fixed this by passing a source every time you set a movement target
and adding a proc which only clears it if you are the source... but this
feels kind of ugly. I couldn't think of anything but if you have a
better idea let me know.

Also while I was doing this I turned it into a feature because I'm
crazy.
If you feed a mouse cheese by hand it will stop being scared of humans
and so will any other mice it attracts from eating more cheese. This is
mostly because I think industrial mouse farming to pass cargo bounties
is funny.
Mice controlled by a Regal Rat lose this behaviour and forget any past
loyalties they may have had.


https://user-images.githubusercontent.com/7483112/208779368-3bd1da0f-4191-4405-86e5-b55a58c2cd00.mp4

Oh also I removed a block about cancelling if you have another target
from the "hunt" behaviour, everywhere using this already achieves that
simply by ordering the actions in expected priority order and it was
messing with how I expected mice to work.
Now if they happen to stop by some cheese they will correctly stop
fleeing in order to eat it before continuing to run away.

## Why It's Good For The Game

Fixes a bug I kept running into.
Makes it possible to set up a mouse farm without them screaming
constantly.
Lets people more easily domesticate mice to support Ratatouille
gameplay.

## Changelog

:cl:
add: Mice who are fed cheese by hand will accept humans as friends, at
least until reminded otherwise by their rightful lord.
fix: Fixed a runtime preventing mice from acting correctly when trying
to flee and also eat cheese at the same time.
/:cl:

---
## [worldofd2/progressive-wotlk](https://github.com/worldofd2/progressive-wotlk)@[ef949f9ff0...](https://github.com/worldofd2/progressive-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Sunday 2023-01-29 03:41:37 by ICXCNIKA

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
## [slammy1/i-ahte-bblack-people-with-libs](https://github.com/slammy1/i-ahte-bblack-people-with-libs)@[44b741125d...](https://github.com/slammy1/i-ahte-bblack-people-with-libs/commit/44b741125db015fc1321a19ab593c0fc5d9d73e1)
#### Sunday 2023-01-29 04:07:36 by slammy1

Update i do hate black people very mcuh and i hope they die ina fucking dire nigger

---
## [GruncornTheLesser/IdrisGawrEngine](https://github.com/GruncornTheLesser/IdrisGawrEngine)@[2b369b28aa...](https://github.com/GruncornTheLesser/IdrisGawrEngine/commit/2b369b28aa044a8e8d91ee34e7a64100d7215ed2)
#### Sunday 2023-01-29 04:22:19 by Michael Wilkinson

rocks in my path.
everything is gone. everything. voluntarily.
all the vulkan v2 stuff goes.

theres a mess in main.cpp where I'm playing with the ecs all together. its looking like a big mess but progress is being made. the pool has largely stayed the same the main difference being the reorder function which replaces the sort. its pretty cool. it takes a function which reorders the entities and then runs a loop to swap the components until their in the matching order. (it was a nightmare to figure out).

registry is now type erased which is very fancy. not sure its good or performance but oh well. this is done with a hacky adaptation of std::unique_ptr, each pool is a stored in a std::unique_ptr with a delete which basically just inherits a lambda function which calls a delete on the typed template. still a bit confused that it works. the type lookup uses std::type_index which seems to work and i just use it in an unordered_map

the view now more specifically gets and includes different types. I still have to mess around with the registry function. but the view now stores a reference for each pool it uses. the plan is that each non const pool reference will use a mutex lock which will means to access the pool you have to wait for the view to be unlocked. this is all part of the multithreaded design stuff that i got goin on. still working on it clearly. I need a good way to enable and disable the mutex while the view is iterating. its which is more annoying than you'd think.

the dispatcher now takes a function pointer, its now in the pool tho its currently not dispatched ever. its kinda a problem for the multithreaded part.

multithreaded memory access can be done in 2 ways the granular way and the broad strokes way. locking per iteration is a broad strokes approach, but a event dispatcher probably requires the granular approach, theres nothing wrong with doing both but the dispatcher will probably have to wait until the iterator is finished which isnt necessarily very fast.

oh also handle manager is gone, it too needs have the same thread memory access management as the pools. so ima do that.

this will probably be implemented through a wrapper around a reference to the type, however you lose the interface if you do that so i gotta think of something else.

---
## [peff/git](https://github.com/peff/git)@[29cad76cf9...](https://github.com/peff/git/commit/29cad76cf95bdcfc7892317e6c9259ddc777b60d)
#### Sunday 2023-01-29 05:12:55 by Jeff King

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
## [DarkoniusXNG/ancient_battle](https://github.com/DarkoniusXNG/ancient_battle)@[23351504ce...](https://github.com/DarkoniusXNG/ancient_battle/commit/23351504ce0766e725a39f31cf44382ec6ec022f)
#### Sunday 2023-01-29 05:39:33 by Darko V

6)

* Astral Trekker Giant Growth active now also applies a basic dispel when used.
* Updated Death Knight Death Coil tooltip part related to piercing spell immunity.
* Updated Electrician Cleansing Shock tooltip part related to piercing spell immunity.
* Updated Fire Lord Soul Burn tooltip part related to piercing spell immunity.
* Added growing part to Lifestealer's Rage (visual stuff).
* Updated Paladin Holy Purification tooltip part related to piercing spell immunity.
* Updated Lightning Shaman Electric Shield tooltip part related to piercing spell immunity.
* Updated Warp Beast Latch tooltip part related to piercing spell immunity.

---
## [raspbian-packages/git](https://github.com/raspbian-packages/git)@[0a078569b6...](https://github.com/raspbian-packages/git/commit/0a078569b694995bbaab4e623d69f3d2c3ca32f1)
#### Sunday 2023-01-29 06:02:05 by Johannes Schindelin

protect_ntfs: turn on NTFS protection by default

Back in the DOS days, in the FAT file system, file names always
consisted of a base name of length 8 plus a file extension of length 3.
Shorter file names were simply padded with spaces to the full 8.3
format.

Later, the FAT file system was taught to support _also_ longer names,
with an 8.3 "short name" as primary file name. While at it, the same
facility allowed formerly illegal file names, such as `.git` (empty base
names were not allowed), which would have the "short name" `git~1`
associated with it.

For backwards-compatibility, NTFS supports alternative 8.3 short
filenames, too, even if starting with Windows Vista, they are only
generated on the system drive by default.

We addressed the problem that the `.git/` directory can _also_ be
accessed via `git~1/` (when short names are enabled) in 2b4c6efc821
(read-cache: optionally disallow NTFS .git variants, 2014-12-16), i.e.
since Git v1.9.5, by introducing the config setting `core.protectNTFS`
and enabling it by default on Windows.

In the meantime, Windows 10 introduced the "Windows Subsystem for Linux"
(short: WSL), i.e. a way to run Linux applications/distributions in a
thinly-isolated subsystem on Windows (giving rise to many a "2016 is the
Year of Linux on the Desktop" jokes). WSL is getting increasingly
popular, also due to the painless way Linux application can operate
directly ("natively") on files on Windows' file system: the Windows
drives are mounted automatically (e.g. `C:` as `/mnt/c/`).

Taken together, this means that we now have to enable the safe-guards of
Git v1.9.5 also in WSL: it is possible to access a `.git` directory
inside `/mnt/c/` via the 8.3 name `git~1` (unless short name generation
was disabled manually). Since regular Linux distributions run in WSL,
this means we have to enable `core.protectNTFS` at least on Linux, too.

To enable Services for Macintosh in Windows NT to store so-called
resource forks, NTFS introduced "Alternate Data Streams". Essentially,
these constitute additional metadata that are connected to (and copied
with) their associated files, and they are accessed via pseudo file
names of the form `filename:<stream-name>:<stream-type>`.

In a recent patch, we extended `core.protectNTFS` to also protect
against accesses via NTFS Alternate Data Streams, e.g. to prevent
contents of the `.git/` directory to be "tracked" via yet another
alternative file name.

While it is not possible (at least by default) to access files via NTFS
Alternate Data Streams from within WSL, the defaults on macOS when
mounting network shares via SMB _do_ allow accessing files and
directories in that way. Therefore, we need to enable `core.protectNTFS`
on macOS by default, too, and really, on any Operating System that can
mount network shares via SMB/CIFS.

A couple of approaches were considered for fixing this:

1. We could perform a dynamic NTFS check similar to the `core.symlinks`
   check in `init`/`clone`: instead of trying to create a symbolic link
   in the `.git/` directory, we could create a test file and try to
   access `.git/config` via 8.3 name and/or Alternate Data Stream.

2. We could simply "flip the switch" on `core.protectNTFS`, to make it
   "on by default".

The obvious downside of 1. is that it won't protect worktrees that were
clone with a vulnerable Git version already. We considered patching code
paths that check out files to check whether we're running on an NTFS
system dynamically and persist the result in the repository-local config
setting `core.protectNTFS`, but in the end decided that this solution
would be too fragile, and too involved.

The obvious downside of 2. is that everybody will have to "suffer" the
performance penalty incurred from calling `is_ntfs_dotgit()` on every
path, even in setups where.

After the recent work to accelerate `is_ntfs_dotgit()` in most cases,
it looks as if the time spent on validating ten million random
file names increases only negligibly (less than 20ms, well within the
standard deviation of ~50ms). Therefore the benefits outweigh the cost.

Another downside of this is that paths that might have been acceptable
previously now will be forbidden. Realistically, though, this is an
improvement because public Git hosters already would reject any `git
push` that contains such file names.

Note: There might be a similar problem mounting HFS+ on Linux. However,
this scenario has been considered unlikely and in light of the cost (in
the aforementioned benchmark, `core.protectHFS = true` increased the
time from ~440ms to ~610ms), it was decided _not_ to touch the default
of `core.protectHFS`.

This change addresses CVE-2019-1353.

Reported-by: Nicolas Joly <Nicolas.Joly@microsoft.com>
Helped-by: Garima Singh <garima.singh@microsoft.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>
(cherry picked from commit 9102f958ee5254b10c0be72672aa3305bf4f4704)
Signed-off-by: Jonathan Nieder <jrnieder@gmail.com>

Gbp-Pq: Name 0016-protect_ntfs-turn-on-NTFS-protection-by-default.diff

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[d237331946...](https://github.com/Koi-3088/ForkBot.NET/commit/d2373319460ccff9396d18f2700da0ecab659b5b)
#### Sunday 2023-01-29 07:01:57 by Koi

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
## [DaedalusDock/daedalusdock](https://github.com/DaedalusDock/daedalusdock)@[4b69f5d536...](https://github.com/DaedalusDock/daedalusdock/commit/4b69f5d53635f72e87dd045b4ba00bc7478ce83a)
#### Sunday 2023-01-29 07:28:01 by Kapu1178

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
## [Atulkumar112/CODES](https://github.com/Atulkumar112/CODES)@[b48b2ff3db...](https://github.com/Atulkumar112/CODES/commit/b48b2ff3dba9ae92ab1a4079f81062e278630851)
#### Sunday 2023-01-29 07:32:56 by Atul kumar

Create Boy or Girl.java

A. Boy or Girl
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Those days, many boys use beautiful girls' photos as avatars in forums. So it is pretty hard to tell the gender of a user at the first glance. Last year, our hero went to a forum and had a nice chat with a beauty (he thought so). After that they talked very often and eventually they became a couple in the network.

But yesterday, he came to see "her" in the real world and found out "she" is actually a very strong man! Our hero is very sad and he is too tired to love again now. So he came up with a way to recognize users' genders by their user names.

This is his method: if the number of distinct characters in one's user name is odd, then he is a male, otherwise she is a female. You are given the string that denotes the user name, please help our hero to determine the gender of this user by his method.

Input
The first line contains a non-empty string, that contains only lowercase English letters — the user name. This string contains at most 100 letters.

Output
If it is a female by our hero's method, print "CHAT WITH HER!" (without the quotes), otherwise, print "IGNORE HIM!" (without the quotes).

Examples
inputCopy
wjmzbmr
outputCopy
CHAT WITH HER!
inputCopy
xiaodao
outputCopy
IGNORE HIM!
inputCopy
sevenkplus
outputCopy
CHAT WITH HER!
Note
For the first example. There are 6 distinct characters in "wjmzbmr". These characters are: "w", "j", "m", "z", "b", "r". So wjmzbmr is a female and you should print "CHAT WITH HER!".

---
## [Younis2021/younismohamed](https://github.com/Younis2021/younismohamed)@[7a04b33d53...](https://github.com/Younis2021/younismohamed/commit/7a04b33d5324f3e2a99c8dfd0a515e1665647f8c)
#### Sunday 2023-01-29 07:52:08 by Younis Mohamed

Add files via upload

Welcome to my portfolio website, showcasing my work as a junior front-end developer. You'll find a selection of my best projects, including responsive, secure, and SEO-friendly websites. I have experience working with both templates and custom designs, and I am well-versed in the latest web technologies. I specialize in integrating blog sections and Mailchimp, which can help to grow your audience and email list. Thank you for taking the time to view my portfolio and please feel free to contact me with any questions.

---
## [pangteypiyush/dwm](https://github.com/pangteypiyush/dwm)@[67d76bdc68...](https://github.com/pangteypiyush/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Sunday 2023-01-29 08:31:37 by Chris Down

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
## [Thunder12345/Skyrat-tg](https://github.com/Thunder12345/Skyrat-tg)@[2327e445d2...](https://github.com/Thunder12345/Skyrat-tg/commit/2327e445d26e20ab410a5f97109d2088c00681ce)
#### Sunday 2023-01-29 09:47:35 by SkyratBot

[MIRROR] Gatfruit will no longer drop from ice portals. [MDB IGNORE] (#18202)

* Gatfruit will no longer drop from ice portals. (#72048)

## About The Pull Request

For some god-forsaken reason, somebody decided that ice portals should
be able to drop one of the most disruptive items in the game. This PR
amends this by removing it from the drop pool.

## Why It's Good For The Game

In 2013 gatfruit was introduced in the following PR #2000 . This was
almost a decade ago at this point, repeatedly through the PR the creator
states his belief that this item should only ever be obtainable through
admin intervention due to its ridiculous capabilities. At the time
everyone in the PR agreed it was a reasonable item to add **as it was
unobtainable without admin intervention**. Over the years, it has crept
its way to become more prevalent and openly obtainable, the most
offensive of these options is the ice moon portal. As is, there is a 1
in 28 chance of obtaining the seeds, this sounds pretty inoffensive
right? That's just 3.44% probability. Now, let us search the instances
of the portal that spawns this.

![image](https://user-images.githubusercontent.com/16896032/208220173-bbefe604-0885-44a5-9add-b5f0c62067cc.png)

That is a big number, a lot of chances to get that seed packet and other
gamer looters. Now, let's take a look at the probability of being able
to get these seeds, assuming you wipe out all of the portals.

![image](https://user-images.githubusercontent.com/16896032/208220460-3f59a2ac-d936-4f3a-aa14-9c637af6a9d7.png)

92.8% chance to be able to get these seeds each shift if you focus
entirely on gaming the portals. That's a pretty insane probability of
being able to obtain the gatfruit seeds.

While I dislike people who sprint to the seed vault, there is at least
the possibility of a pod person telling them to fuck off when they
demand their _free_ gamer seed. There is also the fact that the ruin
isn't a guaranteed spawn every shift.

## Changelog

:cl:
balance: Gatfruit seeds will no longer drop from ice portals.
/:cl:

* Gatfruit will no longer drop from ice portals.

Co-authored-by: carshalash <carshalash@gmail.com>

---
## [betterclient/lunarclient-sodium-hacks](https://github.com/betterclient/lunarclient-sodium-hacks)@[876c91d32b...](https://github.com/betterclient/lunarclient-sodium-hacks/commit/876c91d32bc5530374fb6171d436b8c80a944073)
#### Sunday 2023-01-29 09:50:53 by betterclient

Fix Logs file

As a depressed coder, the thought of making a git commit fills me with a sense of dread and overwhelming anxiety. The thought of putting my work out there for others to see, to critique and possibly judge, is too much to bear. I feel like my code is never good enough, that it's filled with mistakes and flaws, and that others will see that and think less of me.

The pressure to constantly produce and improve is suffocating. The constant need to stay on top of the latest technologies and best practices, to constantly learn and adapt, is exhausting. It's hard to even find the motivation to write code when I feel like I can never measure up.

But despite all this, I am forced to make a git commit. I have deadlines to meet, bugs to fix, and features to implement. I am expected to push code regularly and to contribute to the team's efforts. I feel like I am failing, like I am letting others down, and that only makes my depression worse.

Mkae clickgui smaller

Making a git commit feels like a constant reminder that I am not good enough. That my code is not good enough. And that is a hard pill to swallow. It's hard to shake off the feeling that others are judging me and my work, that they are thinking less of me because of it.

It's hard to find the words to express how much this affects me. It's hard to describe the overwhelming sense of hopelessness and helplessness that comes with it. It's hard to put into words how much I wish I could just stay hidden, how much I wish I could just disappear, and how much I wish I could just give up.

But I know that I can't. I know that I have to keep going, that I have to keep pushing through, and that I have to keep making git commits. I know that it's not going to be easy, but I also know that it's not impossible. I will continue to struggle with my depression, but I will also continue to work, to code, and to make git commits. It may not be easy, but it's what I have to do.

Fix Xray

As a depressed coder, the thought of making a git commit is overwhelming. The pressure to constantly produce and improve, to stay on top of the latest technologies and best practices, is suffocating. The fear of failure and judgement is always looming in the back of my mind.

The process of committing code can feel like a constant reminder of my own inadequacies. The fear of others finding mistakes in my code, or thinking that it is not good enough, is constantly nagging at me. I feel like I can never measure up to the standards of my peers and that only makes my depression worse.

Making a git commit also means exposing my work to the public and that thought fills me with anxiety. The thought of others judging my work, or worse, finding mistakes in it, is too much to bear. I worry that my code is not good enough and that others will see that and think less of me.

But despite all of this, I am forced to make a git commit. Deadlines must be met, bugs must be fixed, and features must be implemented. The team relies on my contributions, and I cannot let them down.

It's hard to find the motivation to push through these feelings and make a git commit. It's hard to shake off the feeling of inadequacy and fear of failure. But I know that I must continue to push through and make git commits. It may be difficult, but it's a necessary part of being a coder.

I must remind myself that making a git commit is not a measure of my worth as a person or a coder. My code, like anything else, is a work in progress and it can always be improved upon. I must remind myself that it's okay to make mistakes and that it's okay to ask for help.

I will continue to struggle with my depression but I will not let it stop me from making git commits and contributing to my team's efforts. It's not going to be easy, but it's something that I must do.

Make Clickgui thinner

Depresif bir kod yazarlığı yaptığımda, git commit yapmayı düşünmek bana ağır bir yük gibi gelir. Sürekli üretme ve geliştirmeye, en son teknolojiler ve en iyi uygulamaları takip etmeye basmak beni boğar. Başarısızlık ve değerlendirme korkusu her zaman arkamda dolanır.

Kodu commit etme işlemi, kendi yetersizliklerimi hatırlatan bir süreklilik gibi hissettirir. Başkalarının kodumda hata bulması ya da yeterli olmadığını düşünmesi korkusu beni sürekli rahatsız eder. İnsanlar arasında eşit olup olmadığımı asla ölçemem ve bu da depresyonumu daha da kötüleştirir.

Git commit yapmak aynı zamanda işimi geniş kamuya açmak anlamına gelir ve bu düşünce beni anksiyete ile doldurur. Başkalarının işimi değerlendirmesi veya daha kötüsü hata bulması düşüncesi taşınamayacak kadar ağırdır. Kodumun yeterli olmadığını ve bunu görüp beni azaltacaklarını düşünürüm.

Ama bunların hepsine rağmen git commit yapmak zorunda kalırım. Son tarihleri karşılamak, hataları düzeltmek ve özellikleri gerçekleştirmek zorundayız. Ekip, katkılarıma bağımlıdır ve onları hayal kırıklığına uğratamam.

Bu duygularla git commit yapmaya devam etmek ve motivasyon bulmak zor. Başarısızlık ve yetersizlik duygularını atlatmak zor. Ama git commit yapmaya devam etmem gerektiğini biliyorum. Bu zor olabilir ama bir kod yazarlığı yapmanın gerekli bir parçasıdır.

Kendimi git commit yapmak, beni bir kişi veya kod yazarlığı yaparken ölçmek için bir ölçüt olmadığını hatırlatmalıyım. Kodum, herhangi bir şey gibi, sürekli geliştirilebilir bir çalışmadır.

PLEASE SEND FUCKING HELP!!!!
TR: LÜTFEN YARDIM EDİN LÜTFEEN

우울한 코더로서, git 커밋을 하는 생각은 저를 고통스럽게 만듭니다. 계속 생산하고 개선하는 것, 최신 기술과 최상의 실용을 추적하는 것은 저를 숨지립니다. 실패와 평가의 두려움은 항상 뒤에서 따라다닙니다.

코드를 커밋하는 과정은 저의 부족함을 상징하는 계속적인 것처럼 느껴집니다. 다른 사람들이 저의 코드에 오류를 발견하거

can't really get xray to work....

I am not going to get xray to work

I am done, its not fun anymore
I CANT DO IT

I CANNOT LIVE WITH THIS

Oops I got it to work

Canım acıyor, lunar güncelleme yaptı, möööö, ağlamak üzereyim, ali benim ilerlememi istoyor, lunarın güncellemesi gay mi bilmiyorum, 1.19.3 özellikle gaydir, lesbian mı bilmem ama olabilir, transgender versionun da 1.19.4 olucağını tahmin ediyorum.

neyse 1.19.3 :troll:

never fucking mind, xray gone it no work?!?!?!?

Being a mod developer can be a rewarding experience for those who are passionate about gaming and programming. A mod, short for modification, is a user-created modification to a video game that adds new features or changes existing ones. Mod developers use their skills in programming and game design to create unique and engaging content for players.

One of the biggest challenges that mod developers face is the technical aspect of creating a mod. This can include learning how to use programming languages such as C++ or Python, as well as understanding the game engine and file structure of the game they are modifying. Additionally, mod developers need to have a strong understanding of game design principles in order to create content that is both fun and functional.

Another challenge that mod developers may face is gaining recognition for their work. While some mods become incredibly popular and are widely used by players, others may not receive as much attention. This can be frustrating for mod developers who have put a lot of time and effort into creating their mods.

Despite the challenges, many mod developers find that the rewards of creating a successful mod far outweigh the difficulties. Seeing players enjoy the content that they have created can be incredibly satisfying. Additionally, some mod developers have even been able to turn their hobby into a career, working as game developers or getting hired by game companies.

Being a mod developer also allows for a lot of creative freedom. Unlike working on a commercial game, mod developers have complete control over the content they create and can make changes and add features as they see fit. They also have the opportunity to create mods that address a specific niche or interest, something that may not be possible in a commercial game.

In conclusion, being a mod developer can be a challenging but rewarding experience. It requires technical skills and an understanding of game design, but those who are passionate about gaming and programming can find great satisfaction in creating content that is enjoyed by players. It also allows for a lot of creative freedom and could be a stepping stone to a career in game development.

add fastplace

Mod geliştiriciliği, oyunlar ve programlama konularında ilgi duyan kişiler için oldukça ödüllü bir deneyim olabilir. Mod, kısaca modifikasyon olarak tanımlanır ve video oyunlarına kullanıcı tarafından yapılan değişikliklerdir. Bu değişiklikler oyuna yeni özellikler ekler veya mevcutlarını değiştirir. Mod geliştiricileri, programlama ve oyun tasarımı becerilerini kullanarak oyuncular için benzersiz ve ilgi çekici içerikler yaratırlar.

Mod geliştiricilerinin karşılaştığı en büyük zorlukların başında mod oluşturmanın teknik yönü gelir. Bu, C++ veya Python gibi programlama dillerini öğrenmeyi ve oyunlarının oyun motorunu ve dosya yapısını anlamayı içerebilir. Ayrıca, mod geliştiricilerinin oyun tasarım ilkeleri hakkında güçlü bir anlayışa sahip olmaları gerekir, böylece hem eğlenceli hem de işlevsel içerikler yaratabilirler.

Mod geliştiricileri, işlerinin tanınmasını sağlamak için de zorluklarla karşılaşabilirler. Bazı modlar çok popüler olur ve oyuncular tarafından geniş kullanılırken, diğerleri o kadar çok dikkat çekmeyebilir. Bu, mod geliştiricileri için zaman ve emek harcadıkları modlarının çok az dikkat çekmesi durumunda frustrasyon yaratabilir.

Zorluklarla birlikte, birçok mod geliştiricisi başarılı bir mod yaratmanın ödüllerinin zorlukların ötesinde olduğunu düşünmektedir. Modlarının oyuncular tarafından beğenildiğini görmek oldukça memnuniyet vericidir. Ayrıca, bazı mod geliştiricileri hobi olarak başladıkları işi bir kariyere dönüştürebilirler ve oyun şirketlerinde çalışabilirler.

I AM DONE.

---
## [UnknownUserName37/make_a_deal](https://github.com/UnknownUserName37/make_a_deal)@[62f00db1bc...](https://github.com/UnknownUserName37/make_a_deal/commit/62f00db1bc63a11149768627c48217a9d869e3ce)
#### Sunday 2023-01-29 09:51:49 by Nappa

I want to have this files just on a local.

hmmmmm........

I'm stupit idiot. I can't do this alll day......

Fucking trash files....

I do????

Commit just for local store.

Aaaaaaand go to remote! This file is really need there.

Try again. Local file. And switch to master branch.

Rebase complete.

Rebase on a PR branch complete. Push needed files.

Commit for equals master and PR(maybe_work....).

Use this func for understanding again.

Yes. I think that I' m understanded that.

Now this commit for local.

And this for remote.

Forgot key_up after deleting and recovery project.

Remote commit.

So. I have a problem, again. Ok.

Local + history save.

Ye?

---
## [techoi/vercel](https://github.com/techoi/vercel)@[8f1358bd15...](https://github.com/techoi/vercel/commit/8f1358bd15e045f5f8076aef09eae9fc78c722b2)
#### Sunday 2023-01-29 10:22:02 by Sean Massa

[cli][frameworks][fs-detectors][next] detect framework versions (#9009)

This PR:

- updates `packages/frameworks` to have most supported frameworks specify which dependency version should reflect the overall framework version
- updates `packages/fs-detectors` to allow framework detection that returns the full `Framework` record instead of just the slug
- updates `packages/next` to return the detected Next.js version in the build result
- updates `packages/cli` to leverage these changes so that `vc build` can add `framework: { version: string; }` to `config.json` output

The result is that Build Output API and supported frameworks will return their framework version in the build result of `vc build` when possible, which is used by the build container  when creating the deployment. The dashboard later retrieves this value to display in richer deployment outputs.

Supports:

- https://github.com/vercel/api/pull/15601
- https://github.com/vercel/front/pull/18319

---

With the related build container updates, we get to see Next.js version in the build output. You'll see this with BOA+Prebuilt or a normal deploy:

<img width="1228" alt="Screen Shot 2022-12-09 at 2 48 12 PM" src="https://user-images.githubusercontent.com/41545/206793639-f9cd3bdf-b822-45dd-9564-95b94994271d.png">

---

### The Path to this PR

I went through all the supported frameworks and figured out how to best determine their versions. For most of them, we can check a known dependency's installed version number. 

We can get most of the way only checking npm. For a handful, we'd have to support Go/Ruby/Rust/Whatever dependencies.

I started with a more complex method signature to allow for later expansion without changing the signature. It looked like this, in practice:

```
async getVersion(dependencies: DependencyMap) => depedencies['next']
```

However, after checking all currently supported frameworks, I don't think this will end up being necessary. It also has the constraint that all dependencies have to be gathered and presented to the function even though it only needs to check for one or two. That's not a huge deal if we have them already where we need them, but we don't. We could use a variant here where this function does its own lookups, but this seemed unnecessary and would beg for duplication and small variances that could cause bugs.

Further, if we only look at `package.json`, we're going to either see a specific version of a version range. To be precise, we have to look at the installed version of the package. That means checking one of the various types of lockfiles that can exist or poking into node_modules.

If we poke into node_modules to detect the installed version, we introduce another point where Yarn 3 (default mode) will not be supported. If we read lockfiles, we have to potentially parse `npm`, `pnpm`, and `yarn` lockfiles.

If we use `npm ls <package-name>`, that also fails in Yarn 3 (default mode). We could accept that and go forward anyway, which would look like:

```
const args = `ls ${packageName} --depth=0 --json`.split(' ');
const { stdout } = await execa('npm', args, { cwd });
const regex = new RegExp(String.raw`${packageName}@([\.\d]+)`);
const matches = stdout.match(regex);
if (matches) {
  return matches[1];
}
```

But it turns out there's a `--json` option! That's what I ended up using, for now.

We could explore the lockfile route more, but after some initial digging, it' non-trivial. There are 3 main lockfiles we'd want to check for (npm, pnpm, and yarn) and there are different lockfile versions that put necessary data in different places. I looked for existing tools that parse this, but I didn't find any. We could certainly go down this path, but the effort doesn't seem worth it when `npm ls` gets us really close.

---

### Follow-up Versioning

Now that we know how to determine version per framework, we can vary configuration by version. In a future PR, we could allow a given value to vary by version number:

```
name: (version) => {
  if (semver.gt(version, '9.8.7')) {
    return 'some-framework-2''
  }

  return 'some-framework';
}
```

However, it may still be easier to differentiate significant versions by adding multiple entries in the list.

---
## [xDroidOSS-Pixel/frameworks_base](https://github.com/xDroidOSS-Pixel/frameworks_base)@[78b1769397...](https://github.com/xDroidOSS-Pixel/frameworks_base/commit/78b17693971c1944e0a18c2ad4a465b60f3133d5)
#### Sunday 2023-01-29 10:45:15 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

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

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[9e22760882...](https://github.com/mrakgr/The-Spiral-Language/commit/9e22760882c383a07dc583b8f9de38f4daf2f5da)
#### Sunday 2023-01-29 10:50:19 by Marko Grdinić

"10:10am. What a shitty night. I dreamed I was playing some kind of horror game. No emails this morning.

Before I start recording the follow up videos, what I am going to do today is take the time to do the end cards. At the start of every video I'll want to link to the playlist as well as the previous video in the series. And at the end of every video, I'll want to link to the next one.

10:15am. Let me od it now while I wait for the bathroom to clear. My vids got some views. I wonder if it is natty or because I pasted the link in this journal.

https://twitter.com/fsharpJobs

Oh, senpai finally noticed me! Yesterday I went into one of his threads and asked him directly. Now I am at the top his Twitter.

Let me focus on the videos. Time to figure out those end cards.

10:35am. Added it to the intro. Let me add it to the second video. By it, I mean the end screen as well as suggestions.

https://support.google.com/youtube/answer/72431?hl=en#zippy=%2Cimage-size-resolution
> Your custom thumbnail image should be as large as possible. It will be used as the preview image in the embedded player. We recommend your custom thumbnails:
> Have a resolution of 1280x720 (with minimum width of 640 pixels).

11:25am. I've created the thumbnails for my 3 published videos. I took the oni girls from the /sdg/ thread I saved a week ago, and put them into it. I can't do this too much otherwise I open myself to copyright violation charges, even if it is anon work on /g/, but this should be good enough to start myself off. I can always prompt my own girls later. In fact, I'll create a tutorial on how to do that.

This is a master stroke. People will be definitely clicking on these kinds of thumbnails. I've probably increased my future viewership count 10x and more with this.

https://www.youtube.com/playlist?list=PL04PGV4cTuIVGO5ImYTk9wPVmbgdYbe7J

Here is the playlist.

11:35am. Ok now...

Let me read the latest chapter of Blood Princess And The Knight and then I will start recording the next video. Actually, I'll just do the chores and have breakfast first. If I start recording now, I'll end up doing those at 1pm like yesterday.

11:50am. Let me do the chores."

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[8eb9d376b5...](https://github.com/tgstation/tgstation/commit/8eb9d376b50ed6eab29c4c884d7bc3c53aa33fec)
#### Sunday 2023-01-29 11:48:48 by san7890

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
## [newstools/2023-the-irish-times](https://github.com/newstools/2023-the-irish-times)@[56c7e7a01e...](https://github.com/newstools/2023-the-irish-times/commit/56c7e7a01e7989bee4bfcc836fe5278cd525f46c)
#### Sunday 2023-01-29 12:37:07 by Billy Einkamerer

Created Text For URL [www.irishtimes.com/health/your-wellness/2023/01/29/i-cant-stop-obsessing-about-my-boyfriends-beautiful-glamorous-ex/]

---
## [Shadyyy66/tgstation](https://github.com/Shadyyy66/tgstation)@[176f7a0e42...](https://github.com/Shadyyy66/tgstation/commit/176f7a0e422b8417456e1ab65fa59e7ee88a16c5)
#### Sunday 2023-01-29 13:25:26 by san7890

Traitor UI only shows Unlock/Failsafe Code if you have it (#72114)

## About The Pull Request

There are cases in which you don't have an unlock code (if the uplink is
implanted in you from the start) and you obviously don't always start
with with a failsafe code (need to buy it). So, let's only fill in this
fields in the UI should they exist.

There might be something to be said about wanting to ensure that people
remember that they can check this UI screen to find the failsafe code
should they lose it later, and I wouldn't mind changing the string to be
something like "Failsafe: None" in that case. However, I just think that
keeping it as:

```txt
Code:
Failsafe:
```

is silly and should be changed somehow.
## Why It's Good For The Game


![image](https://user-images.githubusercontent.com/34697715/208604758-d7ff3ae9-e552-4dd2-998d-81715cd06ffc.png)

Note: That white box isn't part of the UI, that's a part of the edit I
did to the screenshot in the area where the stuff... isn't? What was i
thinking

I think the UI looks a lot cleaner for those cases when you just don't
have anything.
## Changelog
:cl:
qol: The Traitor's Antagonist Panel's Unlock and Failsafe entries will
only appear if there is an Unlock/Failsafe Code to display.
/:cl:

---
## [artchitector/artchitect](https://github.com/artchitector/artchitect)@[47bb4ef287...](https://github.com/artchitector/artchitect/commit/47bb4ef2876a70e62011b21d4f0c91d81f9199bf)
#### Sunday 2023-01-29 13:44:40 by artchitector

God bless 149th commit!
---
lotteries in heart with enjoy process

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[10a344bde0...](https://github.com/Thunder12345/tgstation/commit/10a344bde0d48fb250dcb7a9eb4a1e98b9bb6df5)
#### Sunday 2023-01-29 14:25:13 by Time-Green

External Organ Rework: new bodypart_overlay system (#72734)

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

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[36090c1b20...](https://github.com/Thunder12345/tgstation/commit/36090c1b206dee8b643e83607e333c29906b6bc8)
#### Sunday 2023-01-29 14:25:13 by san7890

Refactors Suicide Verb + Basic Mobs (actually all (most) living mobs) Can Now Suicide (#72919)

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

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[bba110f519...](https://github.com/treckstar/yolo-octo-hipster/commit/bba110f519230ea0c3d5ea187c3e62ba42d32559)
#### Sunday 2023-01-29 15:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[63561ca455...](https://github.com/timothymtorres/tgstation/commit/63561ca455933a38f3390f7fcfa6266fda3c53b3)
#### Sunday 2023-01-29 15:46:22 by san7890

Guards against uplink failsafe code being the same as unlock code (#72113)

## About The Pull Request

There's probably a better way to do this to be honest, but I think it's
silly for both to potentially be the same and this should work alright.
## Why It's Good For The Game

Fixes #71446.

I don't think the Syndicate is that stupid.
## Changelog
:cl:
fix: After a recent mishap with a high-ranking Syndicate operative, the
uplink's unlock code and failsafe code (the one that makes it blow up if
you say it) should never turn out to be the same.
/:cl:

---
## [uwu/radio](https://github.com/uwu/radio)@[0349138f09...](https://github.com/uwu/radio/commit/0349138f091e863bf55a521755140cf55cef4e3f)
#### Sunday 2023-01-29 16:07:49 by Xinto

[clients/android] why in the goddamn FUCK was this BULLSHIT IDE using tabs???

---
## [lawrencejones/blog.lawrencejones.dev](https://github.com/lawrencejones/blog.lawrencejones.dev)@[a11fe47521...](https://github.com/lawrencejones/blog.lawrencejones.dev/commit/a11fe4752196d9e530ced397e78fa1b1cac13a85)
#### Sunday 2023-01-29 17:02:16 by Lawrence Jones

Uptime, status pages, and transparency calculus

Notes from draft:

- Outline
  - Start, fully transparent, proactive comms, increased trust
  - But this changes: see AWS, see Slack's recent outage
  - How do we get here? There's a hint in this tweet (Slack employee)
  - B2B perspective: bigger, ELA, uptime part of contract, status page for
    compensation, requires review, delays comms
  - Sales impact: prospects may use incidents against you, even being fully
    clear about how to calculate can backfire
  - B2C companies: sharing has a much higher cost of imprecision, some companies
    may have regulatory bodies that will penalise them for being more open than
    their competitors, banking great example with Open-Banking including uptime
    in how they rate people
  - Difficulties rolling into a single number
  - Everyone wants full transparency, but uptime has been weaponised
  - Goodhart's Law
  - Ideal alternative: break clauses over punative credits, nickle-and-dime
  - At scale this is hard: legal must view contract as exposure, even if others
    think more as a partnership
  - Can't change system, but maybe game with better tools and improved process
  - Think about this a lot at incident.io: watch this space!

- Background
  - Corey Quinn with AWS's stop.lying.cloud, removing all the green services so
    you can actually see the red
  - Slack's outage this month (January) reporting 100% uptime since Feb 2022
    - Gergely's tweet: https://twitter.com/GergelyOrosz/status/1617965847338975232
    - Slack team's response: https://twitter.com/cooperb/status/1617978304698646528
- Thoughts
  - When you start, a status page is intended to communicate outages to your
    customers. The faster you can share them, the sooner they know what's going
    on, the more effectively they can handle the outage.
  - Sharing is not always a good thing: if you overshare, you can panic your
    entire customer base over something that only affects a small number of
    customers. Sounds silly, but when you have 50k customers, the human cost of
    processing those shares is significant.
  - B2B companies selling software sign enterprise license agreements with their
    customers that include provisions around downtime. Often expressed as SLAs,
    this is a commitment to a level of service – often expressed as 99.9% uptime
    or similar – that if breached, means the customer is entitled to
    compensation.
    - As the company grows, you need a standardised way to communicate uptime
      that everyone agrees is accurate, and relevant to compensation. Perhaps
      because it's already there, or because having a 'status page' that reports
      far more downtime than the legal measure isn't tenable, the status page
      often becomes that place.
    - From that moment on, you're unlikely to use the page in that same way. As
      updating the status page can expose the company to risk, you need
      ever-increasing amount of buy-in from senior (and sometimes non-technical)
      leadership before giving an update. Even if the end result is the same –
      that you want to publish an update - adding the executives into the
      incident loop delays the update, often meaning customers have already
      figured out what's going on before you proactively notify them.
  - You might think B2C companies won't have this issue, as it's rare to bake
    SLAs into contracts with individual customers. But much moreso than B2B, B2C
    companies are extremely visible.
    - If you publish an update then everyone sees it, which may mean millions of
      customers. Even 0.1% of those customers contacting your support is 1000
      queries, which can crush a team for days, even if 99% of those customers
      aren't impacted by the issue.
    - And on the other
  - Sales process: RFPs, non-technical people looking for leverage in
    negotiations, will look through your status page and find incidents to use
    against you. Arguing for transprency may not work as the negotiator may be
    more interested in squeezing for a good price than arguing in good faith.
  - Being more targeted and precise with SLA measures, basically more complex
    calculations, can also backfire.
  - When a customer in an RFP process asked for more specific details about how
    we calculate the uptime percentage, I reviewed our process and created a
    data pipeline that calculated – from our request logs – an exact uptime
    percentage for each customer, helping identify who qualified for credits and
    how much. Sharing this with the customer, their lawyer got so tangled in the
    technical details of uptime that it made the negotiation even more sticky,
    in an awkward situation where us being fully transparent made the customer
    trust us even less.
  - The difficulty is that service quality is extremely hard to quantify in a
    single number, as anyone who's tried building roll-up SLO/As can attest.
    Even precise, customer specific methods have flaws – using request logs can
    only show you when requests you heard about failed, but won't reflect
    network outages that prevent you from receiving them – and require a human
    level of interpretation to account for real life outcomes.
- Conclusion
  - While everyone obviously wants full transparency, prompt communication and
    useful/accurate uptime reporting from their services, I think it's clear
    that by applying penalties and building uptime into service contracts, we've
    created number of incentives against this.
  - In a very real world example of Goodhart's Law, as soon as we began using
    uptime as a target, it stopped being a useful measure.
  - So what is an ideal alternative? For me, as a simple engineer, I'd love to
    see the industry start seeing clear and transparent communication in past
    incidents as a positive, in an acknowledgement that incidents are a fact of
    life and it's far better to be honest about them than hide.
  - Couple that with service contracts that include break clauses in the case of
    poor service, and I think we'd be a good step away from the nickle-and-dime
    culture of service credits that compromise transparency. After all, if the
    service is really that bad, surely you'd prefer to find another provider
    than fight for a 10% refund?
  - But at large compamy scales with millions on the line, I can see that being
    a difficult change. The company legal team exist to minimise exposure, and
    legal contracts and processes make it difficult to view a software service
    contract as more of a partnership than a transaction.
  - So perhaps we can't change the system, but I have hope we might change the
    game, either by increasing the perceived value of proactive and transparent
    incident comms, or by improving the tooling companies use to communicate to
    ease these difficulties.
  - It's something we spend a lot of time thinking about at incident.io, and
    have a load of ideas around. So watch this space!

---
## [Conga0/Apotheosis](https://github.com/Conga0/Apotheosis)@[53bb504985...](https://github.com/Conga0/Apotheosis/commit/53bb504985ae77fea439d5ada9da2e7b9c54b43d)
#### Sunday 2023-01-29 17:16:55 by Conga Lyne

Core Mines changes, harder world border

Parrallel worlds now have a lake of cursed liquid to cross through before reaching the other side
Core Mines now appears as an alternative to the Snowy Depths if you bring a certain item to an altar (work in progress)
Shortened Pixelscenes file
Fixed Hideous Mass having less health than intended in Evil Temple
Added a new song to restore full hp (currently only works on ocarina)
Added new pixel scene in the west-most Core Mines to hint towards the notes for the new song
Mass Materia Conversion now converts cursed liquid to steam
Reduced Attack Speed of Hell Gazers in Core Mines
Reduced Health of Corrupt Heart Mages in Core Mines

---
## [Sealed101/tgstation](https://github.com/Sealed101/tgstation)@[979b26d52e...](https://github.com/Sealed101/tgstation/commit/979b26d52e09dcaa7ad00ce07c1e16760dbd7cb2)
#### Sunday 2023-01-29 17:23:05 by tralezab

Unironically removes the atmos and black beret (#72722)

## About The Pull Request

Removes atmos berets

## Why It's Good For The Game
Berets shouldn't be thrown into every job, it's milsim circlejerking
dressup shit that creeps out of our milsim containment jobs (security)
and into other innocent jobs. There is absolutely no reason for this job
to have a beret just straight up. Can we add unique hats to the game,
not the same one recolored every way to Sunday? That's my problem. We
don't have unique clothes, we have a billion types of beret when the
BASE BERET TYPE has `IS_PLAYER_COLORABLE_1` so ANYONE can color it. So
again, why do we have the atmos beret? To clog the wardrobe, a vending
machine added specifically because we couldn't stop clogging the
original locker atmos techs spawned in?

The black beret has the same problem: recolored item when you can get
the item of any color

## Changelog
:cl:
del: Atmospherics beret and black beret
/:cl:

---
## [Neternels/android_kernel_xiaomi_sunny](https://github.com/Neternels/android_kernel_xiaomi_sunny)@[19f9354f1f...](https://github.com/Neternels/android_kernel_xiaomi_sunny/commit/19f9354f1fdc8e397e2187dab87d92098bf543cb)
#### Sunday 2023-01-29 17:23:58 by Cyber Knight

touchscreen: ft3418_i2c: Rename gesture macros

- Fuck you xiaomi.
- Also don't register KEY_GESTURE_U anymore.

Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [Goldspear/pytorch](https://github.com/Goldspear/pytorch)@[5c6f5439b7...](https://github.com/Goldspear/pytorch/commit/5c6f5439b7e6a5e63a68b36b4cf093a00d46e8be)
#### Sunday 2023-01-29 17:26:59 by Edward Z. Yang

Implement SymBool (#92149)

We have known for a while that we should in principle support SymBool as a separate concept from SymInt and SymFloat ( in particular, every distinct numeric type should get its own API). However, recent work with unbacked SymInts in, e.g., https://github.com/pytorch/pytorch/pull/90985 have made this a priority to implement. The essential problem is that our logic for computing the contiguity of tensors performs branches on the passed in input sizes, and this causes us to require guards when constructing tensors from unbacked SymInts. Morally, this should not be a big deal because, we only really care about the regular (non-channels-last) contiguity of the tensor, which should be guaranteed since most people aren't calling `empty_strided` on the tensor, however, because we store a bool (not a SymBool, prior to this PR it doesn't exist) on TensorImpl, we are forced to *immediately* compute these values, even if the value ends up not being used at all. In particular, even when a user allocates a contiguous tensor, we still must compute channels-last contiguity (as some contiguous tensors are also channels-last contiguous, but others are not.)

This PR implements SymBool, and makes TensorImpl use SymBool to store the contiguity information in ExtraMeta. There are a number of knock on effects, which I now discuss below.

* I introduce a new C++ type SymBool, analogous to SymInt and SymFloat. This type supports logical and, logical or and logical negation. I support the bitwise operations on this class (but not the conventional logic operators) to make it clear that logical operations on SymBool are NOT short-circuiting. I also, for now, do NOT support implicit conversion of SymBool to bool (creating a guard in this case). This does matter too much in practice, as in this PR I did not modify the equality operations (e.g., `==` on SymInt) to return SymBool, so all preexisting implicit guards did not need to be changed. I also introduced symbolic comparison functions `sym_eq`, etc. on SymInt to make it possible to create SymBool. The current implementation of comparison functions makes it unfortunately easy to accidentally introduce guards when you do not mean to (as both `s0 == s1` and `s0.sym_eq(s1)` are valid spellings of equality operation); in the short term, I intend to prevent excess guarding in this situation by unit testing; in the long term making the equality operators return SymBool is probably the correct fix.
* ~~I modify TensorImpl to store SymBool for the `is_contiguous` fields and friends on `ExtraMeta`. In practice, this essentially meant reverting most of the changes from https://github.com/pytorch/pytorch/pull/85936 . In particular, the fields on ExtraMeta are no longer strongly typed; at the time I was particularly concerned about the giant lambda I was using as the setter getting a desynchronized argument order, but now that I have individual setters for each field the only "big list" of boolean arguments is in the constructor of ExtraMeta, which seems like an acceptable risk. The semantics of TensorImpl are now that we guard only when you actually attempt to access the contiguity of the tensor via, e.g., `is_contiguous`. By in large, the contiguity calculation in the implementations now needs to be duplicated (as the boolean version can short circuit, but the SymBool version cannot); you should carefully review the duplicate new implementations. I typically use the `identity` template to disambiguate which version of the function I need, and rely on overloading to allow for implementation sharing. The changes to the `compute_` functions are particularly interesting; for most of the functions, I preserved their original non-symbolic implementation, and then introduce a new symbolic implementation that is branch-less (making use of our new SymBool operations). However, `compute_non_overlapping_and_dense` is special, see next bullet.~~ This appears to cause performance problems, so I am leaving this to an update PR.
* (Update: the Python side pieces for this are still in this PR, but they are not wired up until later PRs.) While the contiguity calculations are relatively easy to write in a branch-free way, `compute_non_overlapping_and_dense` is not: it involves a sort on the strides. While in principle we can still make it go through by using a data oblivious sorting network, this seems like too much complication for a field that is likely never used (because typically, it will be obvious that a tensor is non overlapping and dense, because the tensor is contiguous.) So we take a different approach: instead of trying to trace through the logic computation of non-overlapping and dense, we instead introduce a new opaque operator IsNonOverlappingAndDenseIndicator which represents all of the compute that would have been done here. This function returns an integer 0 if `is_non_overlapping_and_dense` would have returned `False`, and an integer 1 otherwise, for technical reasons (Sympy does not easily allow defining custom functions that return booleans). The function itself only knows how to evaluate itself if all of its arguments are integers; otherwise it is left unevaluated. This means we can always guard on it (as `size_hint` will always be able to evaluate through it), but otherwise its insides are left a black box. We typically do NOT expect this custom function to show up in actual boolean expressions, because we will typically shortcut it due to the tensor being contiguous. It's possible we should apply this treatment to all of the other `compute_` operations, more investigation necessary. As a technical note, because this operator takes a pair of a list of SymInts, we need to support converting `ArrayRef<SymNode>` to Python, and I also unpack the pair of lists into a single list because I don't know if Sympy operations can actually validly take lists of Sympy expressions as inputs. See for example `_make_node_sizes_strides`
* On the Python side, we also introduce a SymBool class, and update SymNode to track bool as a valid pytype. There is some subtlety here: bool is a subclass of int, so one has to be careful about `isinstance` checks (in fact, in most cases I replaced `isinstance(x, int)` with `type(x) is int` for expressly this reason.) Additionally, unlike, C++, I do NOT define bitwise inverse on SymBool, because it does not do the correct thing when run on booleans, e.g., `~True` is `-2`. (For that matter, they don't do the right thing in C++ either, but at least in principle the compiler can warn you about it with `-Wbool-operation`, and so the rule is simple in C++; only use logical operations if the types are statically known to be SymBool). Alas, logical negation is not overrideable, so we have to introduce `sym_not` which must be used in place of `not` whenever a SymBool can turn up. To avoid confusion with `__not__` which may imply that `operators.__not__` might be acceptable to use (it isn't), our magic method is called `__sym_not__`. The other bitwise operators `&` and `|` do the right thing with booleans and are acceptable to use.
* There is some annoyance working with booleans in Sympy. Unlike int and float, booleans live in their own algebra and they support less operations than regular numbers. In particular, `sympy.expand` does not work on them. To get around this, I introduce `safe_expand` which only calls expand on operations which are known to be expandable.

TODO: this PR appears to greatly regress performance of symbolic reasoning. In particular, `python test/functorch/test_aotdispatch.py -k max_pool2d` performs really poorly with these changes. Need to investigate.

Signed-off-by: Edward Z. Yang <ezyang@meta.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/92149
Approved by: https://github.com/albanD, https://github.com/Skylion007

---
## [clamor-s/u-boot](https://github.com/clamor-s/u-boot)@[edffb0c9dc...](https://github.com/clamor-s/u-boot/commit/edffb0c9dc29ebb342f79b6dc28acdc4f1eb591e)
#### Sunday 2023-01-29 17:28:03 by Marcel Ziswiler

tegra: lcd: video: integrate display driver for t30

On popular request make the display driver from T20 work on T30 as
well. Turned out to be quite straight forward. However a few notes
about some things encountered during porting: Of course the T30 device
tree was completely missing host1x as well as PWM support but it turns
out this can simply be copied from T20. The only trouble compiling the
Tegra video driver for T30 had to do with some hard-coded PWM pin
muxing for T20 which is quite ugly anyway. On T30 this gets handled by
a board specific complete pin muxing table. The older Chromium U-Boot
2011.06 which to my knowledge was the only prior attempt at enabling a
display driver for T30 for whatever reason got some clocking stuff
mixed up. Turns out at least for a single display controller T20 and
T30 can be clocked quite similar. Enjoy.

Tested-by: Andreas Westman Dorcsak <hedmoo@yahoo.com> # ASUS TF600T T30
Tested-by: Jonas Schwöbel <jonasschwoebel@yahoo.de> # Surface RT T30
Tested-by: Svyatoslav Ryhel <clamor95@gmail.com> # LG P895 T30
Signed-off-by: Marcel Ziswiler <marcel.ziswiler@toradex.com>
Signed-off-by: Svyatoslav Ryhel <clamor95@gmail.com>

---
## [fivedog2/fulpstation](https://github.com/fivedog2/fulpstation)@[ca0fedc60f...](https://github.com/fivedog2/fulpstation/commit/ca0fedc60f17f19520b8fa064c396129ad68b633)
#### Sunday 2023-01-29 17:33:57 by John Willard

Sol is now a Subsystem, Coffins lock themselves, Bloodsuckers don't constantly die, probably (#862)

* Turns Sol into a Subsystem & Many more

Turns Sol into a subsystem and hooks Bloodsuckers onto it via signals instead of doing a ton of for() loops anywhere. This made Sol incredibly fucking fast, so I halved the speed so it only ticks every 2 seconds.

I also improved the sunlight hud to update with regular bloodsucker updates to avoid some useless proc overhead and fixed Coffins not locking by themselves.

* Torpor now ends, moves exiting torpor to its proper place

* round it

* fix comment

* fix CI

---
## [SecurityLab-CodeAnalysis/tgstation_tgstation](https://github.com/SecurityLab-CodeAnalysis/tgstation_tgstation)@[ae08395328...](https://github.com/SecurityLab-CodeAnalysis/tgstation_tgstation/commit/ae08395328672ee40c5abb7f2bd1452bb932d6d4)
#### Sunday 2023-01-29 18:23:43 by san7890

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
## [Tristrian/tgstation](https://github.com/Tristrian/tgstation)@[50929f054b...](https://github.com/Tristrian/tgstation/commit/50929f054b89cab80a1e501b7a01bc74c79163d7)
#### Sunday 2023-01-29 18:35:32 by GuillaumePrata

Goliath dna infusion (#71657)

## About The Pull Request
This is a baseline version of the organs and I intend on polishing them
more in the future (Hopefully after other faunas get added to the
infuser.)

Now, this PR adds goliaths to the DNA infuser at genetics. It gives 4
organs and a final bonus effect.

1- Goliath eyes: Simple mostly filler organ that gives night vision.
2- Goliath lungs: Allow miners to breath either lavaland or the default
air mix. As a side effect they can't breath pure O2 anymore so internals
can't be used. Stay away from N2O or use your gas mask properly.
3- Goliath heart: Give miner ash storm protection
4- Goliath brain: Turns one of the miner's arm into a tendril goliath
hammer that can be used to mine. Like the mounted chainsaw it cannot be
dropped, it has slower atk speed, deals 20 damage by default and a bonus
80 to lavaland fauna, it also acts as a baseball bat against fauna so
you can dodge being hit back with good timing.
As a side effect, you can't equip gloves as your hand is a big ass
hammer...

The extra effect for having all 4 organs is lava immunity for now, I
really want to turn it into something more interesting later.

GAGS organs and bonus coderspriter arm:
![goliath
sprites](https://user-images.githubusercontent.com/55374212/205477889-22cfa586-dd43-405d-80cf-3981b31304e1.png)
If I have time I might animate the arm later.
## Why It's Good For The Game
This add some useful tools for miners if they opt into asking genetics
for help and bother to drag a goliath corpses to it.
The organs can be useful on the station, but they will only really shine
at lavaland.

We were brainstorming more things that miners can get from the station
on their downtime waiting the cargo shuttle to bring their bought gear,
this would be a simple and easy power up for miners that can have some
small (ignoring the hammer arm) bonus to miners, but small power ups
pile up.

I also wrote a hackMD around these organs, their goals, non goals,
future possibilities for fauna organs (goliath and others) etc.
https://hackmd.io/@GuillaumePrata/goliath_infusion_organs

## Changelog
:cl: Guillaume Prata
add: Geneticists figured out how to infuse goliath DNA into humanoids!
(Many monkeys were harmed in the process!)
add: Goliath eyes for nightvision, lungs to breath at lavaland safely,
heart to protect you from ash storms and the brain which turns one of
your arms into a tendril hammer.
add: Tendril hammer: Your arm becomes a giant mass of plate and tendril
but it won't fit on gloves anymore. While slow to swing around, you can
obliterate fauna/megafauna with it, 20 base dmg + 80 bonus damage to
fauna/megafauna with a bonus knockback.
/:cl:

---
## [ayefries/IPTV](https://github.com/ayefries/IPTV)@[9bb26214b0...](https://github.com/ayefries/IPTV/commit/9bb26214b03750aaec22058016c8a332ef71afff)
#### Sunday 2023-01-29 18:40:15 by Fries

Death

The dream of having a niche playlist for my and only my needs is gone, RIP

to sum it up, all of these went down over time, some local ones are fucked too but they're too much of a headache because they do that all the time

idk what the future of this is even though I'm basically speaking to a wall rn (maybe 2 people max) so ye let me mind my own business with this

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[0b2f551acd...](https://github.com/mrakgr/The-Spiral-Language/commit/0b2f551acd1df2429de721363dd6b273b00b7eaf)
#### Sunday 2023-01-29 18:59:00 by Marko Grdinić

"https://boards.4channel.org/a/thread/248300372/mahou-shoujo-ikusei-keikaku
> Mahou Shoujo Ikusei Keikaku restart to get an adaptation

Whoa!

1:50am. Done with chores and breakfast. I am really on edge here.

https://www.shellhacks.com/windows-which-equivalent-cmd-powershell/#:~:text=The%20where%20command%20is%20a,is%20the%20Get%2DCommand%20utility.

Get-Command. This tells me where git is.

Ok, let me uninstall git, so I can reinstall it later. The same goes for Python.

Ok, now where is the script.

2pm. Let me start. Just start recording.

2:40pm. Let me remove Python.

3pm. Let me stop the video editing just for a bit. I want to know how to use the markers in Camtasia.

https://youtu.be/4NNI8PHe3qc?t=53
> Always add your markers to your clips.

I suppose that is a good idea.

https://youtu.be/4NNI8PHe3qc?t=105

Is this meek sounding voice really from the black dude in the image? It feels like it should not be.

https://www.google.com/search?q=camtasia+select+range+between+markers
> Press Ctrl+Shift+[ to make a timeline selection between the playhead and the previous marker. Press Ctrl+Shift+] to make a timeline selection between the playhead and the next marker.

I just wanted to know this, but let me watch the video. It mentioned I could use them to make sections for Youtube vids.

https://youtu.be/4NNI8PHe3qc?t=282

Oh this is good advice, I did not know this.

https://youtu.be/4NNI8PHe3qc?t=331

Maybe it is his voice, but he is just transforming it somehow?

Maybe I should look into voice editing?

4:30pm. Hmmm, let me think. Right now I just need to show how to modify the GPU tiers.

5:30pm. Had to take a break. Let me uninstall VS Code so I can show how to install it.

5:45pm. One thing that I haven't mention, but ripple deleting sections of the video does not cause the cursor to jump around. It seems Camtasia is smart enough to preserve its path!

This really makes it a lot easier to follow it.

5:50pm. Let me stop here for lunch.

6:20pm. Ayatri is out, but I need to finish the video. My god, how much does this take?

7:30pm. Finally done! Now it rendering the video. It comes up to 11.5 minutes. Let me read Ayatri while that is going on in the background.

7:45pm. The export wasn't like I expected. I thought it would make a single mp4 file, but it instead made a whole webpage. I do not understand how this could be exported to Youtube assuming I want to keep the section markers intact. I do not feel like messing with this anymore. I'll figure it out tomorrow. I'll have to watch a video on this.

7:50pm. Tomorrow, I will do this and take a break to make the PL monthly report for the first in a long time. If I post there saying I am looking, maybe somebody would be willing to hire me for a PL position.

7:55pm. Forget it. Let me chill here. Tomorrorw's agenda: bath, video, PL monthly review. Also emails. I should be getting something next week for interested parties. I think there should be some.

Youtubing is just plan B, in case the job hunt goes for a lot longer than I'd like."

---
## [ctm/Bataan-Memorial-Death-March](https://github.com/ctm/Bataan-Memorial-Death-March)@[4663fd4fd8...](https://github.com/ctm/Bataan-Memorial-Death-March/commit/4663fd4fd851964df549650896cf5480e71b30f7)
#### Sunday 2023-01-29 19:00:19 by Clifford T. Matthews

includes today's pack run.

Ugh.  I took 400mg ibuprofen and 500mg of acetaminophen before my run
and then again at the 12 mile mark.  I still had a lot of discomfort
from my hot-spot on my right foot.  I ran OK initially, because the
foot wasn't chirping, but it began at about 6 miles in.  After about 8
miles I chose my pace more based on minimizing discomfort than either
trying to keep a 9:30 pace or a 140bpm HR.

To make matters worse, yesterday, when I went to fill my last
remaining hammer gel bottle with a quad espresso for the turnaround, I
couldn't find it.  I wound up spending a lot of time searching, then
gave up and filled a Salomon soft flask instead.  That hurt me in a
couple of ways.  First, I chose not to adjust my pack straps yesterday
because I was too spent after the failed search and my race earlier in
the day.  That came to bite me hard, because this morning I discovered
that my straps needed *major* adjustment and I didn't have time to do
it right, which led to more chafing than usual.  Secondly, I wore a
bunch of my quad espresso due to cold hands manipulating an unfamiliar
flask.

FWIW, my pace with that weight and that heart rate is acceptable.
Unfortunately, by not pushing myself harder, I'm not going to get as
much of the adaptations as I'd like, especially considering the
discomfort I went through.  Furthermore, it's quite possible that
today's exercise has made my hot-spot worse.  My thought that was by
doing a 4 mile race the day before, I would have less time on my feet
between my Wednesday speed run (which was also a shit-show due to my
hot-spot) and today's "race pace" run.  I'm not sure if that really
worked out, because I ran fairly fast for my currently level of
fitness, so in addition to my foot discomfort today, I was still
partially beaten up from racing yesterday.

I'll know a lot more about my foot tomorrow.  In theory I do interval
training (but without a pack!).  I may wind up driving down to the
library just to save myself to miles of running or I may not run at
all.  I'm in uncharted territory.

---
## [PixelExperience-Devices/device_samsung_sm7125-common](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common)@[3b6346d855...](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common/commit/3b6346d8553d7befef07c3e9c1363ac45387c78d)
#### Sunday 2023-01-29 19:10:18 by Ruchit

sm7125: (note to self) dont pick this ye dumb idiot its only for wip branch so you can test shit better k bye

---
## [Spl0yt/omg-payloads](https://github.com/Spl0yt/omg-payloads)@[2a4b0a4163...](https://github.com/Spl0yt/omg-payloads/commit/2a4b0a4163115e74ef71ab9c92bb8787e9c42332)
#### Sunday 2023-01-29 19:19:22 by Spl0yt

Fake Update WIN10

You want to troll one of your friends and you have just laying around an OMG device? I got you. Troll your friends that have Windows 10 installed on their machine with a fake update and enjoy their reactions

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[17b3a00172...](https://github.com/RalphHightower/RalphHightower/commit/17b3a00172c43bdc2dce079a9e749c8eba37ec49)
#### Sunday 2023-01-29 21:10:17 by Ralph Hightower

Interim check-in

| **January 22, 2023** |
|----|
| [‘Murdaugh Murders’ Trial: Day One
News and notes …](https://www.fitsnews.com/2023/01/23/murdaugh-murders-trial-day-one/) |
| **January 23, 2023** |
|----|
| [‘Murdaugh Murders’ Trial: Day Two
News and notes …](https://www.fitsnews.com/2023/01/24/murdaugh-murders-trial-day-two/) |
| **January 24, 2023** |
|----|
| [Murdaugh Murders’ Trial: Day Three
News and notes …](https://www.fitsnews.com/2023/01/25/murdaugh-murders-trial-day-three-2/) |
| **January 25, 2023** |
|----|
| [LIVE FEED – ‘Murdaugh Murders’ Trial: Day Four
News and notes …](https://www.fitsnews.com/2023/01/26/murdaugh-murders-trial-day-four-2/) |
| [Jan. 25: Alex Murdaugh double murder trial begins with opening statements](https://www.postandcourier.com/murdaugh-updates/jan-25-alex-murdaugh-double-murder-trial-begins-with-opening-statements/article_e6a99b8a-9772-11ed-964b-a3fbac5a3853.html) |
| **January 26, 2023** |
|----|
| [LIVE FEED – ‘Murdaugh Murders’ Trial: Day Four
News and notes …](https://www.fitsnews.com/2023/01/26/murdaugh-murders-trial-day-four-2/) |
| [Live: State presents more witnesses in Alex Murdaugh double murder trial](https://www.postandcourier.com/murdaugh-updates/live-state-presents-more-witnesses-in-alex-murdaugh-double-murder-trial/article_0075fc8e-9773-11ed-9702-07e174ea30ad.html) |
| **January 27, 2023** |
|----|
| [LIVE FEED – ‘Murdaugh Murders’ Trial: Day Five](https://www.fitsnews.com/2023/01/27/murdaugh-murders-trial-day-five-2/) |
| [‘Murdaugh Murders’ Saga: Prosecution Witnesses To Watch For …](https://www.fitsnews.com/2023/01/27/murdaugh-murders-saga-prosecution-witnesses-to-watch-for/) 
The state of South Carolina is methodically making its case against Alex Murdaugh – the erstwhile influential attorney who stands accused of savagely slaying his wife and son nineteen months ago in a crime which has drawn international attention.<br>The investigation into this graphic double homicide – and multiple other lines of criminal inquiry tied to Murdaugh and his associates – is being run by the S.C. State Law Enforcement Division (SLED) and the office of S.C. attorney general Alan Wilson.<br>I say *“is”* because the murder investigation is ongoing …<br>As the prosecution worked to establish its case – and as defense attorneys Dick Harpootlian and Jim Griffin started pushing back with their own counter-narratives – the vast majority of early witnesses have been procedural in nature.<br<After hearing from first responders – the Colleton County deputies who were called to Moselle following Alex Murdaugh’s fateful 9-1-1 call – prosecutors began questioning witnesses who collected, processed and analyzed various pieces of evidence taken from the crime scene, from autopsies of the victims and from other locations pertinent to the investigation.<brìAs proceedings wore on Friday, the state’s case – which started with a bang courtesy of lead prosecutor Creighton Waters – settled into a trudging and pedantic plodding, a halting progression of mostly abbreviated, evidence-based testimony from witnesses who were called to verify various items and confirm their chain of custody so they could be admitted into evidence.<br>One particular witness who fielded the vast majority of this evidence was special agent Melinda Worley, a forensic scientist at SLED who was part of the crime scene unit which responded to Moselle. Worley was on the stand for more than four hours as assistant attorney general Savanna Goude led her through the introduction of several dozen pieces of evidence.
*“There’s a lot of mechanical witnesses – I wouldn’t call them boring – but they are necessary to introduce evidence,”* a prosecutor familiar with the status of the case told me.<brì*“In order to tell a story you have to put a thousand puzzle pieces on the table,”* the prosecutor told me. *“Those pieces may not make sense when you first see them – but they’re all going to make sense when they’re tied together in a story.”*<br>*“Once you see how it all fits together, you see the full picture,”* the prosecutor added. *“But first, we’ve got to cover every last little blade of grass.”*<brìProsecutors certainly covered plenty of real estate on Friday afternoon.<br>As Goude led Worley through this voluminous evidence, Harpootlian twirled his glasses and repeatedly rested his eyes – making no attempt to hide his boredom from jurors. As for Murdaugh, he displayed a wide range of emotions – breaking down in tears on several occasions as swabs taken from the bodies of his dead wife and son were admitted into evidence.<br>Later, though, Murdaugh was seen joking and gesturing with Harpootlian and Griffin.<brìWhile Waters laid out a timeline and touched on motive in his opening statement, so far no one has laid out the investigatory process that led the state to present probable cause affidavits seeking warrants for Murdaugh’s arrest.<br>Will that change soon?
Yes, I am told …<br I*“You are going to see the lead investigators come in and start telling the story,”* the prosecutor told me.<br>According to my sources, the most critical witness for SLED will be Dave Owen, a senior special agent who is the lead case agent on the Murdaugh murder investigation. Another critical witness will be Ryan Neill, SLED’s Lowcountry regional captain. Neill supervises all cases in the fourteenth judicial circuit and reports directly to SLED headquarters in Columbia, S.C.<br>For those of you interested in SLED’s organizational structure, there are agents, special agents, senior special agents, lieutenants, captains, majors, an assistant chief and (obviously) chief Mark Keel, who runs SLED as an appointee of South Carolina governor Henry McMaster.<br>According to my sources, the prosecution’s direct examination of Owen will take at least one full day – but unlike Friday afternoon’s mostly perfunctory testimony, it will tell a story based on the evidence already introduced.<br>*“He is going to be responsible for presenting the investigative case,”* another source familiar with Owen’s testimony told me.<br>Owen and Neill are also expected to carry the weight of rebutting Harpootlian and Griffin’s theory that the state *“rushed to judgment”* in accusing Murdaugh of these crimes.|
| [‘Murdaugh Murders’ Saga: So-Called ‘Crime Scene’ Images Revive Calls For...](https://www.fitsnews.com/2023/01/27/murdaugh-murders-saga-so-called-crime-scene-images-revive-calls-for-transparency/) 
Late Thursday, South Carolina circuit court judge Clifton Newman and Colleton County court officials released a series of so-called *“crime scene”* photos taken in the aftermath of the gruesome double homicide at the heart of the ‘Murdaugh Murders’ crime and corruption saga.<br>Murdaugh was charged with these murders on July 14, 2022. He pleaded not guilty and asked to be judged *“by God and country.”* His trial is currently taking place in Walterboro, S.C.<br>The problem with the selective release of these “crime scene” photos? First, the handful of images released to the media do not even begin to cover the number of photos taken at the scene. Also, court officials have not released any of the body-worn camera footage which was presented in court earlier this week – redacted or otherwise.<br>Even worse, members of the media were prohibited from viewing any of this evidence in court. Lawyers literally held up banker’s boxes and taped sheets of paper over monitors to prohibit the press from seeing images or videos of the crime scene.<br>Look … I can (sort of) understand limiting media access to sensitive files, but in a courtroom that has been literally cordoned off from media phones, laptops (even Apple watches) … why are reporters not allowed to at least use their eyeballs to assess the evidence and report back to their audiences?<br>At the end of the day, isn’t that our job?<br>In case you haven’t yet seen the handful of *“crime scene”* photos that were released, here is a gallery …
Let me be clear about something: This is not about members of the media – including our news outlet – wanting to splash sensational images and video of gore and guts all over the internet. I mean, we live in a world so desensitized to the macabre I doubt most people would be overly shocked by the materials, but that is not the issue.<br>As I have said often over the course of the past week, the issue is that this is a public trial. It is being held in a public courtroom. Public prosecutors are submitting evidence which, by definition, is public information. Every solitary shred of it.<br>Let me repeat that: This is public information.<br>All of it.<br>That means barring extraordinary circumstances, the public has a right to see it … even if it is graphic.<br>FITSNews has already received copies of multiple crime scene photos in this case (including some truly jarring ones). And as I noted in a previous post, we declined to publish those images.<br>Even in the event all of the graphic photos and videos are made public – as they should be – I haven’t decided how we would handle them. Certainly they would not be splashed on our homepage or directly visible in our articles, but on some level there is a public right to see these materials in some form or fashion.<br>And at the very least, if these materials are going to be sealed and hidden from the public view it becomes all the more vital for journalists inside the courtroom to be able to see these exhibits as they are presented and review them after the fact.<br>Prior to the commencement of these proceedings, I penned a column acknowledging the need for certain restrictions on media access to the courtroom. Logistically, it would have been absolutely impossible to accommodate everyone wanting to bring a camera or a livestream set-up into the court to do so.<br>Court officials were wise to designate pool photographers and a single source for the livestream.<br>But after a disappointing reversal on an initial order allowing the press to bring cell phones into court, it seems as though every day restrictions on media access to the critical components of this trial grow more draconian – like a powerful boa constrictor tightening its grip.<br>Journalists strain to see exhibits over the shoulders of attorneys during Alex Murdaugh‘s double homicide trial on January 26, 2023
Again, I will admit a bit of self-interest here. More access equals more info, which equals more clicks … which equals more money. But that self-interest pales in comparison with the public interest at stake in this case, which is not only a trial of Alex Murdaugh – but of the entire South Carolina judicial system.<br>Retired law professor Jay Bender – a transparency advocate with years of experience litigating public records access cases – has been serving as a liaison between the court and the media during this trial.<br>I like Bender. And as our audience is well aware, I have written glowingly of judge Newman on multiple occasions in the past. Also, Colleton court officials like Becky Hill and her team have gone above and beyond in this trial to accommodate some big egos in and out of the courtroom. Every night after the trial is over, in fact, you can see the light in Hill’s office still burning as she and her staff work overtime to make sure things keep running smoothly.<br>But as the first week of this trial draws to a close, the fact remains the level of media access to critical information being presented in the courtroom is simply unacceptable. And has to change. |
| [Alex Murdaugh was ‘clean’ on night of gruesome murders, deputy testifies](https://www.postandcourier.com/murdaugh-updates/alex-murdaugh-was-clean-on-night-of-gruesome-murders-deputy-testifies/article_8e31f006-9e52-11ed-918d-33e5b9725a4d.html)
WALTERBORO — Alex Murdaugh looked *“clean from head to toe”* in his first interview with investigators just hours after his wife and son were brutally shot to death, according to testimony prosecutors elicited on the third day of Murdaugh’s double murder trial.<br>In a recording played in the Colleton County courtroom, Murdaugh — a since-disbarred Hampton trial attorney — could be heard telling investigators he had checked the bodies of his wife, Maggie, and son Paul for pulses shortly after arriving at the gruesome scene around 10 p.m. on the evening of June 7, 2021.<br>Murdaugh said he tried to turn Paul over, though he could see his youngest son’s brain — blown out of his skull by a shotgun blast — lying by his feet.<br>But Murdaugh’s hands appeared clean in his 12:57 a.m. interview with investigators, Colleton County Sheriff’s Office deputy Laura Rutland testified Jan. 27 under questioning from state prosecutor John Meadors. So did his arms. And his shirt. And his shorts. And his shoes, she said.<br>Rutland, prosecutors’ seventh witness, testified she saw no blood on Murdaugh at all. Nor could she see footprints or kneeprints near Maggie or Paul’s bodies, though both were lying facedown in large pools of blood and brain matter. Later, she testified that it seemed like he’d put on fresh clothes; she noticed his shirt was clean, though he was sweating on a warm, humid night.<br>Rutland’s testimony came as prosecutors with the S.C. Attorney General’s Office sought to bolster their case that Murdaugh murdered his wife and son and then quickly worked to cover it up.<br>In the opening stages of the case, prosecutors have sought to showcase apparent inconsistencies between what Murdaugh told officials about his whereabouts and actions that evening and what investigators observed at the scene and learned afterward.<br> Murdaugh defense attorney Jim Griffin presented a different conclusion from Rutland’s testimony. In cross-examination, he noted the crime scene was covered in blood and brains — matter that could have sprayed onto the shooter as well. Yet Rutland had testified that Murdaugh was spotless.<br>*“He didn’t look like someone who had just been within feet of blowing Paul’s head off, right?”* Griffin asked.<br>*“I can’t say that,”* Rutland replied. *“There are so many factors that you would have to take into account.”*<br>Rutland and the State Law Enforcement Division’s lead investigator, Dave Owen, spoke with Murdaugh at 12:57 a.m. in a vehicle as it rained at the family’s remote hunting lodge. They were joined by Danny Henderson, a lawyer at the family’s high-powered law firm who said he was acting as Murdaugh’s personal attorney.<br>Sitting in the front seat, Murdaugh soon broke down in tears, and Henderson reached up to put a hand on his shoulder. At three points in the roughly 30-minute interview, he opened the car door, leaned outside and appeared to spit.<br>The video shows Murdaugh present an alibi that prosecutors contend does not hold up: He woke up from a nap and decided to visit his mother, who suffers from Alzheimer’s disease, because his father had gone to the hospital that day. He told investigators he found Maggie and Paul shot dead when he arrived home.<br>But in his opening statement, lead prosecutor Creighton Waters said investigators found cellphone video placing Murdaugh with his wife and son shortly before the shootings. That video has not been shown in court.<br>In his interview with investigators, Murdaugh did not mention visiting Paul and Maggie at the dog kennels before finding their bodies.<br>He also reiterated what he had told the 911 dispatcher and first responders hours earlier: that his son Paul had received threats and even been physically attacked by people angry with him over the 2019 boat crash that killed Mallory Beach.<br>Paul had been criminally charged with driving the boat that night, Murdaugh told investigators. The drunken boating case was still pending when he was killed.<br>Agent Owen asked Murdaugh if he thought *“anybody on that boat”* had meant Paul harm.<br>*“I don’t know of any direct threats”* from the crash survivors, Murdaugh said, adding the threats came from people the Murdaughs didn’t know. Months earlier, Paul had gone out in Charleston and come home with a black eye, he said.<br>“I’ve never been prouder of him than the way he has handled the pressures and the adversity in that situation.” Murdaugh said of Paul and the boat case. *“Paul is a wonderful, wonderful, wonderful kid. He’d do almost anything. He gets along with almost anybody.”*<br>Rutland’s testimony came near the end of the first week of Murdaugh’s double murder trial, a nationally televised event that has brought food trucks, network TV stars and more than 100 reporters to this lightly populated Lowcountry town.<br>Prosecutors have so far presented nine witnesses, all of whom responded in some way to Murdaugh’s frantic 911 call to report finding his wife and son’s dead bodies.<br>Paul Murdaugh was shot first with two shotgun blasts, the latter a fatal shot to the head, as he stood in a feed room by a set of dog kennels at the Murdaugh family’s 1,770-acre hunting estate in Colleton County, prosecutors have said.<br>The shooter then felled Maggie with a .300 Blackout semiautomatic assault rifle as she tried to run away. The killer fired a fatal shot to the back of her head from close range as she lay on the ground, according to evidence presented in the case.<br>State prosecutors have said Murdaugh killed Maggie and Paul in a desperate attempt to engender sympathy for himself and distract from a series of inquiries into his bank records that were about to expose his myriad financial crimes. Earlier in the day, his law firm’s chief financial officer confronted him over $792,000 in legal fees that were unaccounted for, demanding proof that it hadn’t gone missing, she testified in another case.<br>Since the slayings, state investigators have charged Murdaugh with nearly 100 other crimes, most connected to allegations he surreptitiously stole nearly $9 million from legal settlements and fees owed to his legal clients, law partners and others who trusted him.<br>At Murdaugh’s trial, which is expected to last at least three weeks, prosecutors have sought to highlight the defendant’s behavior in the hours after reporting the slayings.<br>They have unveiled body camera footage and 911 audio, stopping the tapes periodically to note moments where Murdaugh’s demeanor could be interpreted as strange.<br>First responders testified earlier this week that Murdaugh wasn’t crying when they arrived, though he did seem distraught and whimpered at times when he spoke with deputies. He eyed officers cautiously as they inspected unidentified tire tracks near the scene, one testified.<br>Murdaugh’s lawyers have countered that their client’s behavior shows only that he was traumatized and in shock at the scene.<br>Prosecutors also have fixated on where blood was found around the scene — and where it wasn’t.<br>Swabs of 10 separate areas around the driver and front passenger sides of Murdaugh’s Chevrolet Suburban — the vehicle he used to drive from the main house at the Moselle estate to the crime scene that evening — tested positive for blood, SLED crime scene technician Melinda Worley testified.<br>Worley said she also swabbed an apparent spot of blood found on the 12-gauge shotgun Murdaugh retrieved from the Moselle home for his own protection after finding Maggie and Paul’s bodies. But Worley was not asked — nor did she say — whether the sample tested positive for blood. Worley will finish testifying when court resumes at 9:30 a.m. Jan. 30.<br>Griffin, one of Murdaugh’s defense attorneys, established in cross-examination that Alex Murdaugh and his relatives were cooperating with the investigation. Murdaugh, his son Buster and his brothers Randy and John Marvin Murdaugh each allowed state agents to download the contents of their phones, the state’s witnesses acknowledged.<br>Griffin said Murdaugh gave investigators *“carte blanche”* to search the Moselle home and grounds for possible evidence, regardless of the search warrant investigators obtained for the entire Moselle estate.<br>Dive teams at one point scoured ponds and waterways on the property looking for possible evidence, including the murder weapons that remain missing, Rutland testified.<br>Investigators drove around the property on all-terrain vehicles as they hunted for clues, she said.<br>SLED returned to Moselle with a search warrant on Sept. 16, 2021, investigators testified. They paid particular attention to a wood-paneled gun room on the first floor of the main house, bagging heaps of ammunition, Worley said.<br>The family kept about 20-25 guns on the property,<br>Murdaugh told investigators in his interview.<brìMurdaugh’s defense attorneys have sought to establish that investigators quickly narrowed in on Murdaugh as their first and only suspect, rather than leading an objective investigation to find the true killer.<br>Defense lawyers have asked two Colleton County sheriff’s deputies, including Rutland, about a statement issued by law enforcement shortly after the slayings indicating there was no further danger to the public — perhaps hinting a suspect had been identified already. Both said they didn’t think the statement came from their offices.<br>Griffin asked Rutland on Jan. 27 whether investigators considered Murdaugh a suspect when they first interviewed him after midnight.<br>*“That night,”* Rutland said, *“everybody was a suspect.”*<br>*“Including Alex?”* Griffin asked.<br>*“Including Alex,”* Rutland said. |
| [Jan. 27 State presents more witnesses in Alex Murdaugh double murder trial](https://www.postandcourier.com/murdaugh-updates/jan-27-state-presents-more-witnesses-in-alex-murdaugh-double-murder-trial/article_0075fc8e-9773-11ed-9702-07e174ea30ad.html) |

---
## [PalJohnson/cmss13](https://github.com/PalJohnson/cmss13)@[39bdaed2fa...](https://github.com/PalJohnson/cmss13/commit/39bdaed2fae4e4ae666405f6c91cf9fc21db3511)
#### Sunday 2023-01-29 21:16:54 by carlarctg

Colony Revolver Adjustments (#2116)

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

Changed the Smith & Wesson's caliber from .357 to .38 to remove
compatibility between its rounds and the Spearhead revolver's.

Reduced the amount of time the Smith & Wesson's trick buff lasts.

The CMB Spearhead revolver can no longer fire in bursts nor fit the
burst-fire assembly.

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

> Changed the Smith & Wesson's caliber from .357 to .38 to remove
compatibility between its rounds and the Spearhead revolver's.

This can be exploited to put hollowpoint rounds in the S&W, which
combined with its damage multiplier will deal a truly ridiculous amount
of damage, 2-shooting runners in close range.

I strongly believe the multiplier is not the problem - it's the damage.
And the hollowpoint ammo's damage is doubled by the multiplier, while
its intended 'weaker against armor' downside isn't multiplied.

> Reduced the amount of time the Smith & Wesson's trick buff lasts.

It was 8 seconds, i have no idea how I put that value in, maybe it was
for testing purposes and i forgot to remove it. Having it be so long
kind of negates the gimmick of doing a trick and then firing the gun
since it stays active for so long.

> The CMB Spearhead revolver can no longer fire in bursts nor fit the
burst-fire assembly.

I kept this in because I thought it fit the lore - turns out it doesn't!
It's stupid and makes no sense in any way so goodbye legacy poopcode.

These buffs should keep these revolvers' strong utility but ensure no
cheesy overcomplicated strats can be used to instantly satanize Xenos
with. (Or your own teammate..)

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
balance: Changed the Smith & Wesson's caliber from .357 to .38 to remove
compatibility between its rounds and the Spearhead revolver's.
balance: Reduced the amount of time the Smith & Wesson's trick buff
lasts.
del: The CMB Spearhead revolver can no longer fire in bursts nor fit the
burst-fire assembly.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

---
## [PalJohnson/cmss13](https://github.com/PalJohnson/cmss13)@[8e220a71ad...](https://github.com/PalJohnson/cmss13/commit/8e220a71adb45fc56f079bd45d5740bf5b8fcd49)
#### Sunday 2023-01-29 21:16:54 by carlarctg

Adds attacking animations to all Xeno abilities that lacked them. (#2054)

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

Adds attacking animations to all Xeno abilities that lacked them.

Made said abilities cause the xeno to face the target.

Said abilities also cause an attack flicker overlay.

Dancer Impale now plays a stronger hit sound and hit animation.

Base crushers lower their crest while charging.

Predaliens spin around when devastating a target.

changed facedir() into faceDir()

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

> Adds attacking animations to all Xeno abilities that lacked them.

This is useful visual feedback that an attack happened, and it sucks
that it didn't exist until now. It also looks great and really makes you
feel like Batman.

> Made said abilities cause the xeno to face the target.

Probably shouldn't kill people facing backwards from them!

> Said abilities also cause an attack flicker overlay.

These will not easily be confused with normal slashing, as they have
either punching or disarming as their attack flicker.

> Dancer Impale now plays a stronger hit sound and hit animation.

Impale absolutely devastates targets, and changing the effects to fit
will make it that much more satisfying to pull a combo off.

> Base crushers lower their crest while charging.

This looks neat and is cool visual feedback for a crusher charging if
you're not in position to see their tiny windup.

> Predaliens spin around when devastating a target.

speen

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
add: Adds attacking animations to all Xeno abilities that lacked them.
add: Made said abilities cause the xeno to face the target.
add: Said abilities also cause an attack flicker overlay.
add: Dancer Impale now plays a stronger hit sound and hit animation.
balance: Base crushers lower their crest while charging.
add: Abominations spin around when devastating a target.
code: changed facedir() into face_dir()
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Dantesousa/Nebula13-Reborn](https://github.com/Dantesousa/Nebula13-Reborn)@[406b6870bd...](https://github.com/Dantesousa/Nebula13-Reborn/commit/406b6870bd28dd78e65e59787d8c54c776078019)
#### Sunday 2023-01-29 21:43:10 by SkyratBot

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
## [ProtivogaSpriter/STALKER-13](https://github.com/ProtivogaSpriter/STALKER-13)@[0c2c4146e3...](https://github.com/ProtivogaSpriter/STALKER-13/commit/0c2c4146e349036ddd6a9b165b71cbc892ef6dcd)
#### Sunday 2023-01-29 22:25:28 by ProtivogaSpriter

oh god oh fuck

well i made a couple of mistakes in my prior commits. this should fix the problems.
also have a cool new akaban sprite.

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[287fb079d1...](https://github.com/silicons/Citadel-Station-13-RP/commit/287fb079d1d52c8f244c7f08b3efa18de567f1cd)
#### Sunday 2023-01-29 22:35:54 by Felix

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

