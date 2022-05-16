## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-15](docs/good-messages/2022/2022-05-15.md)


1,528,476 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,528,476 were push events containing 2,216,269 commit messages that amount to 114,842,165 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 25 messages:


## [iradukud/Codewars](https://github.com/iradukud/Codewars)@[252ec8753d...](https://github.com/iradukud/Codewars/commit/252ec8753de244c334b846ed4db1931b93bb56a1)
#### Sunday 2022-05-15 00:01:51 by David Iradukunda

Did_she_say_hallo

You received a whatsup message from an unknown number. Could it be from that girl/boy with a foreign accent you met yesterday evening?

Write a simple function to check if the string contains the word hallo in different languages.

These are the languages of the possible people you met the night before:

hello - english
ciao - italian
salut - french
hallo - german
hola - spanish
ahoj - czech republic
czesc - polish
Notes

you can assume the input is a string.
to keep this a beginner exercise you don't need to check if the greeting is a subset of word (Hallowen can pass the test)
function should be case insensitive to pass the tests

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[20fd416cd4...](https://github.com/newstools/2022-express/commit/20fd416cd4f5a23370a0d82671991fd73a9513d9)
#### Sunday 2022-05-15 00:14:47 by Billy Einkamerer

Created Text For URL [www.express.co.uk/celebrity-news/1609360/Eurovision-AJ-Odudu-personal-life-cheating-boyfriend-relationships-strictly-news-latest]

---
## [Sinestia/Pariah-Station](https://github.com/Sinestia/Pariah-Station)@[95db2c6bfc...](https://github.com/Sinestia/Pariah-Station/commit/95db2c6bfc84871f2fa51eeef253f681dc46a632)
#### Sunday 2022-05-15 01:17:38 by Kapu1178

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301) (#696)

About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [ThatFiveGuys/goonstation](https://github.com/ThatFiveGuys/goonstation)@[bdad398f9e...](https://github.com/ThatFiveGuys/goonstation/commit/bdad398f9ecb9c6a65d65d23816e1f5820a71553)
#### Sunday 2022-05-15 01:39:07 by aloe

haha what if we fundamentally didn't understand inheritance wouldn't that be fucking hilarious

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[a064b35b25...](https://github.com/Stalkeros2/Skyrat-tg/commit/a064b35b2571af36cf9d12cea8005843768af36d)
#### Sunday 2022-05-15 01:53:13 by SkyratBot

[MIRROR] Fixes an error sprites on medical wintercoat's allowed list. [MDB IGNORE] (#13566)

* Goodbye stack/medical (#66898)

Okay, why removing instead of giving it a sprite?

Simply put, those items are all small and there is no reason that you need to quick draw a suture/ointment and if you do, the medical belt can carry 7.
Allowed/exoslot items should be either medium/big/bulky sized items (Syringe gun) to make it worth inventory wise or items that you can quickdraw multiple times (Health Analyzer) to make your life easier.
Medical stacks are neither and would just get in the way if you try to quickly put them into a bag/pocket/belt and instead it goes into your exoslot where you would normally want to carry more valuable things like the syringe gun.

This doesn't feel big enough for a fix, spending 5 seconds making a list alphabetical doesn't few worth of code improvement, I will label this as QoL and if someone say it is a balance change I will follow you in game and keep placing shitty small items in your inventory via reverse pickpocketing.

* Fixes an error sprites on medical wintercoat's allowed list.

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>

---
## [Dharmik48/awesome](https://github.com/Dharmik48/awesome)@[67b58f28ea...](https://github.com/Dharmik48/awesome/commit/67b58f28eab1cefa06623fff183677a8a1a1b940)
#### Sunday 2022-05-15 08:52:24 by Dharmik_403

Add SmollCSS

<!-- Congrats on creating an Awesome list! 🎉 -->

<!-- Please fill in the below placeholders -->

**[Insert URL to the list here]**

**[Explain what this list is about and why it should be included here]**

### By submitting this pull request I confirm I've read and complied with the below requirements 🖖

**Please read it multiple times. I spent a lot of time on these guidelines and most people miss a lot.**

## Requirements for your pull request

- **Don't waste my time.** Do a good job, adhere to all the guidelines, and be responsive.
- **You have to review at least 2 other [open pull requests](https://github.com/sindresorhus/awesome/pulls?q=is%3Apr+is%3Aopen).**
	Try to prioritize unreviewed PRs, but you can also add more comments to reviewed PRs. Go through the below list when reviewing. This requirement is meant to help make the Awesome project self-sustaining. Comment here which PRs you reviewed. You're expected to put a good effort into this and to be thorough. Look at previous PR reviews for inspiration. **Just commenting “looks good” or simply marking the pull request as approved does not count!** You have to actually point out mistakes or improvement suggestions.
- You have read and understood the [instructions for creating a list](https://github.com/sindresorhus/awesome/blob/main/create-list.md).
- This pull request has a title in the format `Add Name of List`.
	- ✅ `Add Swift`
	- ✅ `Add Software Architecture`
	- ❌ `Update readme.md`
	- ❌ `Add Awesome Swift`
	- ❌ `Add swift`
	- ❌ `add Swift`
	- ❌ `Adding Swift`
	- ❌ `Added Swift`
- Your entry here should include a short description about the project/theme of the list. **It should not describe the list itself.** The first character should be uppercase and the description should end in a dot. It should be an objective description and not a tagline or marketing blurb.
	- ✅ `- [iOS](…) - Mobile operating system for Apple phones and tablets.`
	- ✅ `- [Framer](…) - Prototyping interactive UI designs.`
	- ❌ `- [iOS](…) - Resources and tools for iOS development.`
	- ❌ `- [Framer](…)`
	- ❌ `- [Framer](…) - prototyping interactive UI designs`
- Your entry should be added at the bottom of the appropriate category.
- The title of your entry should be title-cased and the URL to your list should end in `#readme`.
	- Example: `- [Software Architecture](https://github.com/simskij/awesome-software-architecture#readme) - The discipline of designing and building software.`
- The suggested Awesome list complies with the below requirements.

## Requirements for your Awesome list

- **Has been around for at least 30 days.**<br>That means 30 days from either the first real commit or when it was open-sourced. Whatever is most recent.
- Don't open a Draft / WIP pull request while you work on the guidelines. A pull request should be 100% ready and should adhere to all the guidelines when you open it. **Instead use [#2242](https://github.com/sindresorhus/awesome/issues/2242) for incubation visibility**.
- Run [`awesome-lint`](https://github.com/sindresorhus/awesome-lint) on your list and fix the reported issues. If there are false-positives or things that cannot/shouldn't be fixed, please [report it](https://github.com/sindresorhus/awesome-lint/issues/new).
- The default branch should be named [`main`, not `master`](https://www.zdnet.com/article/github-to-replace-master-with-alternative-term-to-avoid-slavery-references/).
- **Includes a succinct description of the project/theme at the top of the readme.** [(Example)](https://github.com/willempienaar/awesome-quantified-self)
	- ✅ `Mobile operating system for Apple phones and tablets.`
	- ✅ `Prototyping interactive UI designs.`
	- ❌ `Resources and tools for iOS development.`
	- ❌ `Awesome Framer packages and tools.`
- It's the result of hard work and the best I could possibly produce.
	**If you have not put in considerable effort into your list, your pull request will be immediately closed.**
- The repo name of your list should be in lowercase slug format: `awesome-name-of-list`.
	- ✅ `awesome-swift`
	- ✅ `awesome-web-typography`
	- ❌ `awesome-Swift`
	- ❌ `AwesomeWebTypography`
- The heading title of your list should be in [title case](https://capitalizemytitle.com/) format: `# Awesome Name of List`.
	- ✅ `# Awesome Swift`
	- ✅ `# Awesome Web Typography`
	- ❌ `# awesome-swift`
	- ❌ `# AwesomeSwift`
- Non-generated Markdown file in a GitHub repo.
- The repo should have `awesome-list` & `awesome` as [GitHub topics](https://help.github.com/articles/about-topics). I encourage you to add more relevant topics.
- Not a duplicate. Please search for existing submissions.
- Only has awesome items. Awesome lists are curations of the best, not everything.
- Does not contain items that are unmaintained, has archived repo, deprecated, or missing docs. If you really need to include such items, they should be in a separate Markdown file.
- Includes a project logo/illustration whenever possible.
	- Either centered, fullwidth, or placed at the top-right of the readme. [(Example)](https://github.com/sindresorhus/awesome-electron)
	- The image should link to the project website or any relevant website.
	- **The image should be high-DPI.** Set it to maximum half the width of the original image.
- Entries have a description, unless the title is descriptive enough by itself. It rarely is though.
- Includes the [Awesome badge](https://github.com/sindresorhus/awesome/blob/main/awesome.md#awesome-badge).
	- Should be placed on the right side of the readme heading.
		- Can be placed centered if the list has a centered graphics header.
	- Should link back to this list.
- Has a Table of Contents section.
	- Should be named `Contents`, not `Table of Contents`.
	- Should be the first section in the list.
	- Should only have one level of [nested lists](https://commonmark.org/help/tutorial/10-nestedLists.html), preferably none.
	- Must not feature `Contributing` or `Footnotes` sections.
- Has an appropriate license.
	- **We strongly recommend the [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/), but any [Creative Commons license](https://creativecommons.org/choose/) will work.**
		- Tip: You can quickly add it to your repo by going to this URL: `https://github.com/<user>/<repo>/community/license/new?branch=main&template=cc0-1.0` (replace `<user>` and `<repo>` accordingly).
	- A code license like MIT, BSD, Apache, GPL, etc, is not acceptable. Neither are WTFPL and [Unlicense](https://unlicense.org).
	- Place a file named `license` or `LICENSE` in the repo root with the license text.
	- **Do not** add the license name, text, or a `Licence` section to the readme. GitHub already shows the license name and link to the full text at the top of the repo.
	- To verify that you've read all the guidelines, please comment on your pull request with just the word `unicorn`.
- Has [contribution guidelines](https://github.com/sindresorhus/awesome/blob/main/awesome.md#include-contribution-guidelines).
	- The file should be named `contributing.md`. Casing is up to you.
	- It can optionally be linked from the readme in a dedicated section titled `Contributing`, positioned at the top or bottom of the main content.
	- The section should not appear in the Table of Contents.
- All non-important but necessary content (like extra copyright notices, hyperlinks to sources, pointers to expansive content, etc) should be grouped in a `Footnotes` section at the bottom of the readme. The section should not be present in the Table of Contents.
- Has consistent formatting and proper spelling/grammar.
	- The link and description are separated by a dash. <br>Example: `- [AVA](…) - JavaScript test runner.`
	- The description starts with an uppercase character and ends with a period.
	- Consistent and correct naming. For example, `Node.js`, not `NodeJS` or `node.js`.
- Doesn't use [hard-wrapping](https://stackoverflow.com/questions/319925/difference-between-hard-wrap-and-soft-wrap).
- Doesn't include a Travis badge.<br>You can still use Travis for list linting, but the badge has no value in the readme.
- Doesn't include an `Inspired by awesome-foo` or `Inspired by the Awesome project` kinda link at the top of the readme. The Awesome badge is enough.

**Go to the top and read it again.**

---
## [Atom-X-Devs/android_kernel_xiaomi_scarlet](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet)@[767b2ef513...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_scarlet/commit/767b2ef51340d2172a5456ab7856493ab64d40a5)
#### Sunday 2022-05-15 09:04:46 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: Anush02198 <Anush.4376@gmail.com>
Signed-off-by: Divyanshu-Modi <divyan.m05@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>

---
## [bogdasar1985/newsboat](https://github.com/bogdasar1985/newsboat)@[2dd8022096...](https://github.com/bogdasar1985/newsboat/commit/2dd8022096590b6042948687dfc69d7b39198334)
#### Sunday 2022-05-15 09:05:44 by Lysander Trischler

Remove trailing whitespace

Trailing whitespace is not harmful, but unnecessary and ugly in my
opinion. I configured my editor to highlight it, so I see it all the
time, which is a bit annoying. Let's get rid of it.

Actually regenerating the filter produces some slightly different code
with my installed version of cococpp (Coco/R Jan 02, 2012), so I just
kept the old code and removed the trailing spaces and tabulators.

`make fmt` now also removes trailing whitespace from all the text files.
Since not only source files but any text files might be subject to
introducing new trailing whitespace, CI will not skip that formatting
task anmyore for documentation-, translation-, contribution- and/or
snap-only changes. It's now unconditionally executed all the time.

'xargs -r' is not supported everywhere, so we need to use a loop
instead. That will guard against no files necessary to be rewritten.

---
## [yuhangbin/guava](https://github.com/yuhangbin/guava)@[e015172847...](https://github.com/yuhangbin/guava/commit/e0151728478c16e3fe295a368ba74c2195a10e85)
#### Sunday 2022-05-15 10:12:40 by cpovirk

Remove `@Beta` from uncontroversial `Futures` methods:

- `submit`
- `submitAsync`
- `scheduleAsync`
- `nonCancellationPropagating`
- `inCompletionOrder`

I did also add a TODO to potentially make the return type of `scheduleAsync` more specific in the future. However, to the best of my knowledge, no one has ever asked for this. (That's not surprising: `ScheduledFuture` isn't any more useful than `Future` unless you're implementing a `ScheduledExecutorService`, and even then, access to its timeout is unavoidably racy.) Plus, should we ever need to do it, we can do it compatibly by injecting a bridge method with the old signature.

(I didn't see any discussion of the return type in the API Review doc or the CL review thread. It probably just didn't come up, or maybe we all independently concluded that it wasn't worth the trouble, given that `MoreExecutors.listeningDecorator(ScheduledExecutorService)` is a bit of a pain? But I'm guessing `scheduleAsync` would be easier.)

RELNOTES=`util.concurrent`: Removed `@Beta` from `Futures` methods: `submit`, `submitAsync`, `scheduleAsync`, `nonCancellationPropagating`, `inCompletionOrder`.
PiperOrigin-RevId: 416139691

---
## [txstc55/solitude-backend](https://github.com/txstc55/solitude-backend)@[5202f891a3...](https://github.com/txstc55/solitude-backend/commit/5202f891a3f17ddcb946a73adaa16955a8ae0f75)
#### Sunday 2022-05-15 10:15:08 by Xuan Tang

move ban list to environment variable
But still fuck you, racist guy and husky fucker

---
## [CPC-Dev/Grasscutter](https://github.com/CPC-Dev/Grasscutter)@[fbaeaee4b5...](https://github.com/CPC-Dev/Grasscutter/commit/fbaeaee4b5aa82fe10897b60ea642d4428e8abd8)
#### Sunday 2022-05-15 10:54:19 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [atorik/postgres](https://github.com/atorik/postgres)@[c40ba5f318...](https://github.com/atorik/postgres/commit/c40ba5f318f96a6a5a29729b987ead11c5dc65c1)
#### Sunday 2022-05-15 13:15:25 by Tom Lane

Fix rowcount estimate for SubqueryScan that's under a Gather.

SubqueryScan was always getting labeled with a rowcount estimate
appropriate for non-parallel cases.  However, nodes that are
underneath a Gather should be treated as processing only one
worker's share of the rows, whether the particular node is explicitly
parallel-aware or not.  Most non-scan-level node types get this
right automatically because they base their rowcount estimate on
that of their input sub-Path(s).  But SubqueryScan didn't do that,
instead using the whole-relation rowcount estimate as if it were
a non-parallel-aware scan node.  If there is a parallel-aware node
below the SubqueryScan, this is wrong, and it results in inflating
the cost estimates for nodes above the SubqueryScan, which can cause
us to not choose a parallel plan, or choose a silly one --- as indeed
is visible in the one regression test whose results change with this
patch.  (Although that plan tree appears to contain no SubqueryScans,
there were some in it before setrefs.c deleted them.)

To fix, use path->subpath->rows not baserel->tuples as the number
of input tuples we'll process.  This requires estimating the quals'
selectivity afresh, which is slightly annoying; but it shouldn't
really add much cost thanks to the caching done in RestrictInfo.

This is pretty clearly a bug fix, but I'll refrain from back-patching
as people might not appreciate plan choices changing in stable branches.
The fact that it took us this long to identify the bug suggests that
it's not a major problem.

Per report from bucoo, though this is not his proposed patch.

Discussion: https://postgr.es/m/202204121457159307248@sohu.com

---
## [BakaKaito/Mergebot.NET](https://github.com/BakaKaito/Mergebot.NET)@[d6cbad1738...](https://github.com/BakaKaito/Mergebot.NET/commit/d6cbad17380392b08f7921a839b8b74f071383b2)
#### Sunday 2022-05-15 14:26:54 by Koi

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
## [KMFDManic/mame2003-xtreme](https://github.com/KMFDManic/mame2003-xtreme)@[b9a59b9a99...](https://github.com/KMFDManic/mame2003-xtreme/commit/b9a59b9a990efe81e002e56792ee31a75d965b87)
#### Sunday 2022-05-15 15:15:05 by Kyland K

Killer Instinct 1 and 2 Cheats Update!

Killer Instinct 1: Attack and Movement Speed Manipulation via Updated Cheats (cheat.dat)!

Selection of 12 different speeds and 21 different sizes, including Defaults.  You can choose to move as slow as molasses, or as fast as a Jedi!  Fight as a metaphorical watching paint dry sloth, or as frenetic as a one inch punch from Bruce Lee!  You can also be as small as a mouse or as large as a Kaiju!

Dozens of other Cheats added for both Killer Instinct 1 and 2, including Automated Ultra Combos and Humiliations and No Mercy Finishers!

Personal thanks to Mahoneyt944 and Abystus for their incredible efforts and insight in this little project I personally wanted to implement to help better lower spec platforms!

retroarch/system/mame2003-xtreme/cheat.dat

retroarch/system/mame2003-plus/cheat.dat

If using 2003 Plus, you must delete the .rzip, before the new cheat.dat will take effect!

R2 to open MAME Menu on 2003 Xtreme; L3 or Core Options to do the same for 2003 Plus.

Select Cheats, Apply, Resume Game, Rinse and Repeat, Enjoy the Performance/Speed Boost!

---
## [ClearHeadToDo-Devs/ClearHeadToDo](https://github.com/ClearHeadToDo-Devs/ClearHeadToDo)@[26c705fe12...](https://github.com/ClearHeadToDo-Devs/ClearHeadToDo/commit/26c705fe121a80f4ee1b18897413675cbf180c08)
#### Sunday 2022-05-15 15:24:27 by Darrion Burgess

just used the mutable reference bullshit. should be fine with what I
have for now and I think I really need to stop over this obsession with
doing immutable data structures properly if I'm going to ship this
stupid thing

---
## [Lunu-Lunu/Inkunzi-EU4](https://github.com/Lunu-Lunu/Inkunzi-EU4)@[b8962d8f56...](https://github.com/Lunu-Lunu/Inkunzi-EU4/commit/b8962d8f56e6d652b84feac334fc491d5a83e162)
#### Sunday 2022-05-15 15:32:13 by supercow2

OMG OMG OLD ONES

i did it !!
-old ones event and modifier
-name changes
-other shit? don't remember

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[3d3a3db072...](https://github.com/mrakgr/The-Spiral-Language/commit/3d3a3db0728c2eb5ed9f7ecfb012593c2953ab27)
#### Sunday 2022-05-15 16:04:54 by Marko Grdinić

"8:50am. I actually went to bed at 9am. I am not sure whether I feel more rested today, but I guess this kind of schedule will serve to unclutter my mind.

8:55am. Let me start instead of browsing /a/.

9am. Got a refil, ok. Let me get out the pen stylus and get ready.

9:15am. Getting that cube was a drag. I just now figured out that once I make a box, I can edit its proportions afterwards.

10:05am. I have a thing I want to ask of the Moi guys.

https://moi3d.com/forum/discussion.php?webtag=MOI&msg=10695.1

Well here it is. For now let me just go with scaling it by 1.001. I need to split the balcony door into two.

11:05am. Yeah, this isn't so bad. I feel like I am getting a hang of Moi. I'll never be able to go back to modeling in Blender after this. Moi is so much better.

11:10am. Had to take a short break. Let me resume. Now apart from detailing, I have the last part of the balcony door left, the wooden grill doors. I suppose I could also do the knobs. Wouldn't hurt.

11:35am. Did the door handle. Now let me do the grill door. How is it placed exactly?

12:50pm. Finally done with the doorway. I did the most salient features...

Agh, let me do the latch at the top. Whatever.

1:05pm. Now I am deliberating whether or not to do an extra detail. Forget it. I am done here. The other latch isn't really visible so I don't need to do it.

1:10pm. I might have overdone it as it is. Ok, let me go forward with this. I'll bring this into the scene and do the bar for the curtains. That one I should be able to hack in Blender. After that I'll bring in the rig, the desk and the monitor. I should also do the other door leading into the room, but as that one won't be visible, it can just be a slice for the time being.

I won't redo the bed. Maybe I'll just bevel big edges, but that is it for now.

After I go through this, I'll try painting it over. This scene is a decent amount more complex than the couch scene I did last year. It will be the truest test of my skill.

Maybe it will turn out that doing more in Blender would be beneficial whether that be rendering, modeling or texturing. I'll find the right balance as I go along.

2pm. Let me read a bit of the hiki vampire countess novel which I got yesterday off Nyaa and I will resume.

2:20pm. Let me resume. Let me make the curtain in Mo after all. It would be a pain to do it in Blender. After that I'll start bringing things in.

2:50pm. Finally done with the wooden curtain bar. Now let me work on getting this into Blender.

2:55pm. I am exhausted here. During the modeling process I've been in the zone the whole time.

3:25pm. Fuck. Setting things up in Blender is such a chore.

4:10pm. I am still messing with it. Let me think. How do I rotate the doors along the hinges without messing up everything?

Should I join the individal grill pieces?

No, that would unlink it and increase the poly count significantly.

Hmmm, I have an idea. Why don't I make an empty, and parent the main grill door to it. Than if I ever unparent that, I can just undo the transform.

Great, great, great...this is the solution I was looking for. It is perfect. Back when I modeled the door in Blender I did a destructive rotate and couldn't get the door back without significant effort.

4:20pm. Enough, enough. Let me not mess with the bed bevels.

The reason why I dunked over an hour here because I did not follow the right process and parented the door pieces immediatelly. Next time I'll know better.

Now let me bring in the detailed right.

4:35pm. Not bad. Let me bring in the desk as well.

4:50pm. Brought in the desk.

5pm. Ok, I've setup the the perspective. Now I can bring in the screenshot into CSP and give it a try.

Let me take a break here. I've been going full throttle all day. I am not sure I have the steam needed to paint.

5:30pm. Did a /wip/ post. Right now I've imported it into CSP and am staring at it. I've definitely no will to do any painting right now. I've been doing art for 7.5 months now. Today's session was the closest it has ever been to an average programming day session.

I've really moved from learning to actually doing.

3d isn't so bad. It is not as skill dependent as 2d is, you can get steadily better results the more effort you put in. What I will have to do now is check out whether that holds true when it comes to painting.

It should. I have a good baseline for what a workflow should be from doing that couch. Masks, edge control, gradient maps. I am going to have to try something else this time instead of gradient maps. Instead of them I'll try to make the bottom layer grayscale, and the upper one a color layer and mix the two data points that way. That way I can have the flats in one place and their shades in another. That should be pretty effective.

6pm. Let me close here. Just when was the time I ever closed at 6pm. It was always just trying to get more and more knoweldge during the past 7.5 months. How many times have I been so obsessed to go past 12am.

Right now let me read the hikivamp novel and relax for a while. Summer is here.

Once I finish my first real illustration I can pat myself on the back. I will have done something remarkable as an artist."

---
## [wrenger/linux](https://github.com/wrenger/linux)@[213d266ebf...](https://github.com/wrenger/linux/commit/213d266ebfb1621aab79cfe63388facc520a1381)
#### Sunday 2022-05-15 16:22:59 by Linus Torvalds

gpiolib: acpi: use correct format characters

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>

---
## [demqa/DosScripts](https://github.com/demqa/DosScripts)@[09fdff29a5...](https://github.com/demqa/DosScripts/commit/09fdff29a5a1b915c76c6a2c897604648c37425c)
#### Sunday 2022-05-15 18:06:52 by Dmitry 'demqa' Stepanov

Now I placed there funny moments from my developing in DOS. I hate myself for losing these scripts, because it was very good, really. There was some movement & blinking, and there was really some funny process, that lived on his own, so that was nice to watch it... )))

---
## [scottnm/Archive](https://github.com/scottnm/Archive)@[4fa9a5428a...](https://github.com/scottnm/Archive/commit/4fa9a5428a58bf9fc8b853907c1d158590907c2e)
#### Sunday 2022-05-15 18:23:12 by Scott Munro

Implement a basic unsafe rust FFI for the test C API (#3)

* ffi linking against (but not using) static lib. wuuuuuutttt

* woah. I'm calling a c function from rust

* add rest of the projection

* holy shit I'm looking at data from a c lib

* fix comment

* format that sucker

* add readme

---
## [crawl/crawl](https://github.com/crawl/crawl)@[2b7d6d2820...](https://github.com/crawl/crawl/commit/2b7d6d2820442eeaccb2a6fd23387f3dde59ce1a)
#### Sunday 2022-05-15 19:14:20 by Nicholas Feinberg

New species: Star

Time pressure often creates exciting gameplay and interesting
tradeoffs. Baseline Dungeon Crawl uses the Zot Clock to add a
very weak form of time pressure, but there's so much variety
between the playstyles of different species and backgrounds
that a tight clock for some would be almost impossible for
others.

So, let's try limiting that gameplay to just one species! Stars
have an exciting variety of bonuses - good attributes and
aptitudes across the board, passive mapping, damage shaving (ala
Deep Dwarves), and eventually innate MP and HP regen. In
exchange, they have one big downside: instead of getting 6,000
turns of Zot clock for each floor, they get 600!

The big concern here is whether this species can be made fun
without also being made wildly, boringly 'overpowered'. Lots of
levers and knobs to tweak, so let's give it a shot!

Extra notes:
- Stars are humanoid beings. (In the night sky, they look like
  dots because they're very far up.) Hat tip to Neil Gaiman's
  Stardust.
- This commit has a silly 'flavour' gimmick where Stars' LOS
  radius decreases by 2 when they have less than 50 turns left
  of Zot clock, and again when they have less than 10. Darkness
  is closing in...
- A future commit will make stars shine.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[07790ad2a8...](https://github.com/treckstar/yolo-octo-hipster/commit/07790ad2a8b734b7be33b81d182d4071ec9edfb5)
#### Sunday 2022-05-15 20:22:02 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[249b5abfdf...](https://github.com/Perkedel/Kaded-fnf-mods/commit/249b5abfdf98ab9b980e1d31ce454d5d91029559)
#### Sunday 2022-05-15 20:36:25 by Joel Robert Justiawan

[skip ci] bebabo

crashdumper seems a huge investement in storage space, hence that link fail. idk.

there is UNCHECKED CRASH after bopeebo! pls debug crash why crash! crashdumper cannot be here at all AAAAAAAAAA

wow, there's a bug in the Local server test we have here, the disable 1 click gb filedaddy werror 404 somehow, despite the file being there. maybe it's trouble with certain part of the browser??

peck! I forgot what do I want to fix. I wish I can write now despite were doing 🚽🚾.

for now, we can only render with final configuration `lime test windows -final` because of that pecking lnk error unresolved external symbol

woups! we forgot to filter out what cannot do modcore in the platform cannot modcore.

bagui

Now, how do we supposed to redesign our IONIQ Sky here? Initially, way before KitsuneSkulls expose (last e has accent line up right), I thought how about she wears um.. this zipped motorcycle jacket tight shirt thingy, colored black with emblem of LFM logo. Yeah uh, the LFM logo is Umnaga family crest. If me has Perkedel logo as the crest, Latsufir x Sky has this logo. So, it's there. and also, maybe I keep the... skirt. idk. BUT still has, umm, PECK! umm... this tight spandex black pants.. aa gyeah..
idk, I already decided for her hair, the blue cyan is natural. like bf is. And uh Yolaine's hair is uh.. purple.. lilac purple. yess. sorry, I'm sorry, not to do bad thigns, Sr. Pelo, no no, your character cool and good! I just have random thoughts.

HAAARGH!!! PECKING POOPS!!!! I WISH I HAVE WORKING EASY 3D CHARACTER GENERATOR HERE!!! Oh yeah, we have MB labs, BUT THEY HAVE FATAL LIMITATIONS!!! NO!! I'd rather sculpt one on my own, ugh..

TODO: Yoink Week 7. use luckydog7 android port, they got one.

Right, we have successfully & finally installed Redsty Phoenix standalone GF. both v2 & legacy. And shut up, the game was supposedly for higher ages as been stated somewhere. And UOH!! MAN!! Sorry, not to simp here, but I can't deny how impressive these are.

TODO: install AjTheFunky heartbreak gf. but due to pibby not allowed, how about disqualify & make it a separate mod LFM-kade-modcore instead? okay maybe not. Because they can yoink that out, they still have to ask permission because that's how Earth copyright works, We're not in Dasandim where permissionless yoink but credit are defaultly enforced. OAH!! SHUSH!!! Forget about this. treat this paragraph like it's nothing. okay, give me time.

we still have to complete all the rest of the Week overbuse kevin macleod man! c'mon!

---
## [HACKER-3000/cvrs_music](https://github.com/HACKER-3000/cvrs_music)@[c65a9ae032...](https://github.com/HACKER-3000/cvrs_music/commit/c65a9ae03211c725b1fe7726639001c872db90da)
#### Sunday 2022-05-15 21:12:41 by HACKER3000

media key support

also fixed backgroud-clip for chrome. WHYYY do i have to use the stupid webkit version?! fuck you chrome!!

---
## [IanButterworth/julia](https://github.com/IanButterworth/julia)@[62e0729dbc...](https://github.com/IanButterworth/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Sunday 2022-05-15 22:09:00 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>

---

