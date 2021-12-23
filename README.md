## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2021-12-22](docs/good-messages/2021/2021-12-22.md)


1,723,540 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,723,540 were push events containing 2,554,075 commit messages that amount to 202,918,020 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [LOuroboros/pokeemerald](https://github.com/LOuroboros/pokeemerald)@[7067ce7592...](https://github.com/LOuroboros/pokeemerald/commit/7067ce7592b7fb6f4ab0c359a6416f73708a55ea)
#### Wednesday 2021-12-22 00:07:27 by LOuroboros

Modified the way Feebas spawns in Route 119 based on ORAS
Thanks to Surskitty for the help adding a dup of the regular water tile and the inspiration to just go and do this.
Really, the whole 6 random tiles gimmick freaking sucks and it doesn't even make sense.

Also added a special to manipulate the friendship value of a Pokémon in the heat of the moment.
Date of creation: Sun May 2 21:37:41 2021 -0300

---
## [chrisbobbe/zulip-mobile](https://github.com/chrisbobbe/zulip-mobile)@[d7d91dcfb6...](https://github.com/chrisbobbe/zulip-mobile/commit/d7d91dcfb63eae31cc39526337649743699da6a7)
#### Wednesday 2021-12-22 00:56:16 by Chris Bobbe

keyboard-avoiding ios: Begin forking RN's KeyboardAvoidingView

From
  node_modules/react-native/Libraries/Components/Keyboard/KeyboardAvoidingView.js
with v0.64.2 of `react-native`, adjusting only the license pointer
in the copyright header.

We'll make the fork usable soon, not in this pure copy-paste commit.

We don't like this implementation (see, e.g., 70eca0716, which took
a lot of painstaking investigation), but we want to fix #5162 as
soon as we can.

For a not-quite-perfect attempt at reimplementing it from scratch in
our style (and with #5162 fixed), see my branch
`reimplement-keyboard-avoiding-view` on GitHub.

We can't easily make a jank-free solution in a normal React Native
way because we can't have perfect information about the layout on
every frame. React Native exposes it to us by consuming event
listeners and providing asynchronous query functions, and we end up
having to learn about different aspects of the layout at different
times.

The best hope for a jank-free solution is to use native iOS APIs. If
we're feeling adventurous and we find the time, we should really try
hard to make React Native play along with iOS's
`keyboardLayoutGuide` API (iOS 15+).

The first four minutes of this video should be really useful
background on the `keyboardLayoutGuide` feature:
  https://developer.apple.com/videos/play/wwdc2021/10259/

It works within iOS's "Auto Layout" system:
  https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/index.html

But then we'd have to go and

(a) Make a native component:
      https://reactnative.dev/docs/native-components-ios

(b) Figure out how to make React Native's propagate-from-JavaScript
    layout system (Yoga) not fight with the native iOS layout
    system, including "Auto Layout" and `keyboardLayoutGuide`.
    Possibly we can pick up some clues from
    `react-native-safe-area-context` for this?

From another angle, since the jank is regularly seen on screen
orientation changes between portrait and landscape, we could
consider just unsupporting the landscape orientation. On very common
device types, like phones, it's just not as easy to use the app in,
especially for composing messages.

---
## [newstools/2021-national-daily-nigeria](https://github.com/newstools/2021-national-daily-nigeria)@[c9ab6daa8f...](https://github.com/newstools/2021-national-daily-nigeria/commit/c9ab6daa8f976fdaae791494fd0a67097987e61e)
#### Wednesday 2021-12-22 01:18:17 by Billy Einkamerer

Created Text For URL [nationaldailyng.com/how-we-use-female-private-parts-for-money-ritual-yahoo-boys-confess-video/]

---
## [ahhuang007/Sebastian](https://github.com/ahhuang007/Sebastian)@[1f4c4378a3...](https://github.com/ahhuang007/Sebastian/commit/1f4c4378a39237dc5454e1cd48e07e8caf586871)
#### Wednesday 2021-12-22 02:55:24 by ahhuang007

holy shit it works

so sebastian actually fucking works. Also, added small stuff to environment to see xyz position when episode ends

---
## [Javran/advent-of-code](https://github.com/Javran/advent-of-code)@[d2f2fb6cb5...](https://github.com/Javran/advent-of-code/commit/d2f2fb6cb50641c08deb63516d9a25e6dba98893)
#### Wednesday 2021-12-22 04:21:19 by Javran Cheng

nuke it.

fuck this shit. nothing works, heading for the stupid route first.

---
## [avar/git](https://github.com/avar/git)@[3540c71ea5...](https://github.com/avar/git/commit/3540c71ea5ddffff6e473249866cbc7abb8ce509)
#### Wednesday 2021-12-22 04:27:21 by Ævar Arnfjörð Bjarmason

wrapper.c: add x{un,}setenv(), and use xsetenv() in environment.c

Add fatal wrappers for setenv() and unsetenv(). In d7ac12b25d3 (Add
set_git_dir() function, 2007-08-01) we started checking its return
value, and since 48988c4d0c3 (set_git_dir: die when setenv() fails,
2018-03-30) we've had set_git_dir_1() die if we couldn't set it.

Let's provide a wrapper for both, this will be useful in many other
places, a subsequent patch will make another use of xsetenv().

The checking of the return value here is over-eager according to
setenv(3) and POSIX. It's documented as returning just -1 or 0, so
perhaps we should be checking -1 explicitly.

Let's just instead die on any non-zero, if our C library is so broken
as to return something else than -1 on error (and perhaps not set
errno?) the worst we'll do is die with a nonsensical errno value, but
we'll want to die in either case.

Let's make these return "void" instead of "int". As far as I can tell
there's no other x*() wrappers that needed to make the decision of
deviating from the signature in the C library, but since their return
value is only used to indicate errors (so we'd die here), we can catch
unreachable code such as

    if (xsetenv(...) < 0)
        [...];

I think it would be OK skip the NULL check of the "name" here for the
calls to die_errno(). Almost all of our setenv() callers are taking a
constant string hardcoded in the source as the first argument, and for
the rest we can probably assume they've done the NULL check
themselves. Even if they didn't, modern C libraries are forgiving
about it (e.g. glibc formatting it as "(null)"), on those that aren't,
well, we were about to die anyway. But let's include the check anyway
for good measure.

1. https://pubs.opengroup.org/onlinepubs/009604499/functions/setenv.html

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[8b78cb3868...](https://github.com/Koi-3088/ForkBot.NET/commit/8b78cb3868679aba5ca69eb853f36b6577e280af)
#### Wednesday 2021-12-22 05:34:05 by Koi

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
## [Atom-X-Devs/android_kernel_xiaomi_sdm660](https://github.com/Atom-X-Devs/android_kernel_xiaomi_sdm660)@[37be3c26ab...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_sdm660/commit/37be3c26ab911163156f5ab1c2b731b3f9bfab51)
#### Wednesday 2021-12-22 05:51:16 by Masahiro Yamada

kbuild: use more portable 'command -v' for cc-cross-prefix

To print the pathname that will be used by shell in the current
environment, 'command -v' is a standardized way. [1]

'which' is also often used in scripts, but it is less portable.

When I worked on commit bd55f96 ("kbuild: refactor cc-cross-prefix
implementation"), I was eager to use 'command -v' but it did not work.
(The reason is explained below.)

I kept 'which' as before but got rid of '> /dev/null 2>&1' as I
thought it was no longer needed. Sorry, I was wrong.

It works well on my Ubuntu machine, but Alexey Brodkin reports noisy
warnings on CentOS7 when 'which' fails to find the given command in
the PATH environment.

  $ which foo
  which: no foo in (/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin)

Given that behavior of 'which' depends on system (and it may not be
installed by default), I want to try 'command -v' once again.

The specification [1] clearly describes the behavior of 'command -v'
when the given command is not found:

  Otherwise, no output shall be written and the exit status shall reflect
  that the name was not found.

However, we need a little magic to use 'command -v' from Make.

$(shell ...) passes the argument to a subshell for execution, and
returns the standard output of the command.

Here is a trick. GNU Make may optimize this by executing the command
directly instead of forking a subshell, if no shell special characters
are found in the command and omitting the subshell will not change the
behavior.

In this case, no shell special character is used. So, Make will try
to run it directly. However, 'command' is a shell-builtin command,
then Make would fail to find it in the PATH environment:

  $ make ARCH=m68k defconfig
  make: command: Command not found
  make: command: Command not found
  make: command: Command not found

In fact, Make has a table of shell-builtin commands because it must
ask the shell to execute them.

Until recently, 'command' was missing in the table.

This issue was fixed by the following commit:

| commit 1af314465e5dfe3e8baa839a32a72e83c04f26ef
| Author: Paul Smith <psmith@gnu.org>
| Date:   Sun Nov 12 18:10:28 2017 -0500
|
|     * job.c: Add "command" as a known shell built-in.
|
|     This is not a POSIX shell built-in but it's common in UNIX shells.
|     Reported by Nick Bowler <nbowler@draconx.ca>.

Because the latest release is GNU Make 4.2.1 in 2016, this commit is
not included in any released versions. (But some distributions may
have back-ported it.)

We need to trick Make to spawn a subshell. There are various ways to
do so:

 1) Use a shell special character '~' as dummy

    $(shell : ~; command -v $(c)gcc)

 2) Use a variable reference that always expands to the empty string
    (suggested by David Laight)

    $(shell command$${x:+} -v $(c)gcc)

 3) Use redirect

    $(shell command -v $(c)gcc 2>/dev/null)

I chose 3) to not confuse people. The stderr would not be polluted
anyway, but it will provide extra safety, and is easy to understand.

Tested on Make 3.81, 3.82, 4.0, 4.1, 4.2, 4.2.1

[1] http://pubs.opengroup.org/onlinepubs/9699919799/utilities/command.html

Fixes: bd55f96 ("kbuild: refactor cc-cross-prefix implementation")
Cc: linux-stable <stable@vger.kernel.org> # 5.1
Reported-by: Alexey Brodkin <abrodkin@synopsys.com>
Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Tested-by: Alexey Brodkin <abrodkin@synopsys.com>
Signed-off-by: Divyanshu-Modi <divyan.m05@gmail.com>

---
## [jesseposner/secp256k1-zkp](https://github.com/jesseposner/secp256k1-zkp)@[b2206619e6...](https://github.com/jesseposner/secp256k1-zkp/commit/b2206619e69d6d57304e7b4bb0ea5d92ca3b7821)
#### Wednesday 2021-12-22 06:36:50 by Tim Ruffing

Merge ElementsProject/secp256k1-zkp#131: Replace MuSig(1) module with MuSig2

ac1e36769dda3964f7294319ecb06fb5c414938d musig: turn off multiexponentiation for now (Jonas Nick)
3c79d97bd92ec22cc204ff5a08c9b0e5adda12e6 ci: increase timeout for macOS tasks (Jonas Nick)
22c88815c76e6edb23baf9401f820e1a944c3ecf musig: replace MuSig(1) with MuSig2 (Jonas Nick)

Pull request description:

  The main commit comprises `905 insertions(+), 1253 deletions(-)`. The diff isn't as small as I had hoped, but that's mostly because it was possible to simplify the API quite substantially which required rewriting large parts. Sorry, almost all of the changes are in one big commit which makes the diff very hard to read. Perhaps best to re-review most parts from scratch.

  A few key changes:

  - Obviously no commitment round. No big session struct and no `verifier` sessions. No `signer` struct.
  - There's a new `secnonce` struct that is the output of musig_nonce_gen and derived from a uniformly random session_id32. The derivation can be strengthened by adding whatever session parameters (combined_pk, msg) are available. The nonce function is my ad-hoc construction that allows for these optional inputs. Please have a look at that.
  - The secnonce is made invalid after being used in partial_sign.
  - Adaptor signatures basically work as before, according to https://github.com/ElementsProject/scriptless-scripts/pull/24 (with the exception that they operate on aggregate instead of partial sigs)
  - To avoid making this PR overly complex I did not consider how this implementation interacts with nested-MuSig, sign-to-contract, and antiklepto.
  - Testing should be close to complete. There's no reachable line or branch that isn't exercised by the tests.
  - [x] ~In the current implementation when a signer sends an invalid nonce (i.e. some garbage that can't be mapped to a group element), it is ignored when combining nonces. Only after receiving the signers partial signature and running `partial_sig_verify` will we notice that the signer misbehaved. The reason for this is that 1) this makes the API simpler and 2) malicious peers don't gain any additional powers because they can always interrupt the protocol by refusing to sign. However, this is up for discussion.~ EDIT: this is not the case anymore since invalid nonces are rejected when they're parsed.
  - [x] ~For every partial signature we verify we have to parse the pubnonce (two compressed points), despite having parsed it in `process_nonces` already. This is not great. `process_nonces` could optionally output the array of parsed pubnonces.~ EDIT: fixed by having a dedicated type for nonces.
  - [x] ~I left `src/modules/musig/musig.md` unchanged for now. Perhaps we should merge it with the `musig-spec`~ EDIT: musig.md is updated
  - [x] partial verification should use multiexp to compute `R1 + b*R2 + c*P`, but this can be done in a separate PR
  - [x] renaming wishlist
      - pre_session -> keyagg_cache (because there is no session anymore)
      - pubkey_combine, nonce_combine, partial_sig_combine -> pubkey_agg, nonce_agg, partial_sig_agg (shorter, matches terminology in musig2)
      - musig_session_init -> musig_start (shorter, simpler) or [musig_generate_nonce](https://github.com/ElementsProject/secp256k1-zkp/pull/131#discussion_r654190890) or musig_prepare
      - musig_partial_signature to musig_partial_sig (shorter)
  - [x] perhaps remove pubnonces and n_pubnonces argument from process_nonces (and then also add a opaque type for the combined nonce?)
  - [x] write the `combined_pubkey` into the `pre_session` struct (as suggested [below](https://github.com/ElementsProject/secp256k1-zkp/pull/131#issuecomment-866904975): then 1) session_init and process_nonces don't need a combined_pk argument (and there can't be mix up between tweaked and untweaked keys) and 2) pubkey_tweak doesn't need an input_pubkey and the output_pubkey can be written directly into the pre_session (reducing frustration such as Replace MuSig(1) module with MuSig2 #131 (comment))
  - [x] perhaps allow adapting both partial sigs (`partial_sig` struct) and aggregate partial sigs (64 raw bytes) as suggested [below](https://github.com/ElementsProject/secp256k1-zkp/pull/131#issuecomment-867281531).

  Based on #120.

ACKs for top commit:
  robot-dreams:
    ACK ac1e36769dda3964f7294319ecb06fb5c414938d
  real-or-random:
    ACK ac1e36769dda3964f7294319ecb06fb5c414938d

Tree-SHA512: 916b42811aa5c00649cfb923d2002422c338106a6936a01253ba693015a242f21f7f7b4cce60d5ab5764a129926c6fd6676977c69c9e6e0aedc51b308ac6578d

---
## [DmitryRendov/GriefPrevention](https://github.com/DmitryRendov/GriefPrevention)@[2ead578666...](https://github.com/DmitryRendov/GriefPrevention/commit/2ead578666fcaf589260d1c4912f1257263762fe)
#### Wednesday 2021-12-22 07:58:20 by RoboMWM

Make the version explicitely a string. Not sure if CB or yaml is at fault here

[20:58:37] RoboMWM: hmmm it's a bit annoying how CB cuts off the
trailing 0 in my versions
[20:58:49] RoboMWM: e.g. 16.10 displays as 16.1
[20:59:02] +Choco: That seems... stupid? lol
[20:59:12] RoboMWM: very
[20:59:27] RoboMWM: plugin.yml inside jar reveals it to be correct
[20:59:43] RoboMWM: and afaik this is supposed to be a string so idk why
it's doing that
[21:00:49] RoboMWM: apparently wrapping it with single quotes does the
job
[21:01:33] +Choco: Maybe it assumes it's a double then converts it to a
String
[21:02:04] RoboMWM: I guess >_> since I stuck a test.16.10 without
quotes and it's all there
[21:02:09] RoboMWM: thank you yaml
[21:02:22] +Choco: What if you were to do 1.1.10?
[21:02:30] +Choco: Because that's not a valid number, maybe it would
assume String
[21:02:33] RoboMWM: the second dot probably makes it a string
[21:02:51] RoboMWM: maybe I should do 16.1O
[21:02:57] +Choco: lol that's cheating

---
## [IFuckedUpMerging/tgstation](https://github.com/IFuckedUpMerging/tgstation)@[b2ba847c22...](https://github.com/IFuckedUpMerging/tgstation/commit/b2ba847c223dcbdc49c85a46156d5dbc28dbe5bd)
#### Wednesday 2021-12-22 09:13:15 by LemonInTheDark

Reduces the move delay buffer to 1 tick (#63332)

We've got this delay buffer behavior
Idea is basically, if we're just holding down the key, just keep adding to the old delay
This way, fractional move delays make sense

Was added in this commit 491bdac

When it was added, movement was triggered by verbs sent by the client
So we needed a big grace window to account for networking delay

Don't need that anymore cause we use keyLoop, so let's just cut it all the way down

Why?
Because right now if you somehow manage to input a move afer move_delay is up
but before the window runs out, you will be elidgable for a new move before you visually reach the tile

Got a dm from mothblocks about this last night, something about flash stepping? IDK I don't play here
Seems silly though, let's sweep this up

Oh and mothblocks owes me a pizza, please add this to the commit history so it can be certified as a part of the blockchain

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[fa66edc92e...](https://github.com/odoo-dev/odoo/commit/fa66edc92e5a023193c1406880cab77574fdee0b)
#### Wednesday 2021-12-22 10:50:23 by Julien Castiaux

http.py json_dispatch and a bit of RPC

The implementation of `@route(type='json')`. If you were expecting a
simple implementation such as

    self.params = json.loads(self.httprequest.get_data())
    result = endpoint(**self.params)
    return Response(json.dumps(result), 200, [
        ('Content-Type', 'application/json),
    ]

you might be surprises to read about JSON-RPC2. Yup some guy decided it
would be cute to add a bunch of useless things (all three jsonrpc,
method and id are basically ignored). Also that context stuff? Just
throw it in the params, nobody will notice (I did :eyes:). The error
handling has some gotchas too (but it is coming in another commit).

The best is that most endpoints type='json' are... implementing another
RPC layer on top of JSON-RPC2. Typical request:

    POST /web/dataset/call_kw HTTP/1.1
    Content-Type: application/json

    {
        jsonrpc: "2.0",
        id: null,
        method: 'call',
        params: {
            'model': 'res.partner',
            'method': 'create',
            'args': [...],
            'kwargs': {},
            'context': {},
        }
    }

Honorable mentions: /jsonrpc, /web/dataset/*

Why am I so salty? It is because there is nothing I can do to change the
current implementation. Changing the implementation would break the
current API which is working fine. It would be a cross-team effort as
both the JS Framework and the SaaS would be impacted. By the way, there
was an effort to reduce the cumbersome  XML-RPC layer, they are
odoo/odoo#3989 and odoo/odoo#67388, #3989 is 7 years old... yeah... not
doing it again for jsonrpc. I blame nobody, JSON-RPC is cute indeed,
just... not very useful here :( (same goes for XML-RPC without #3989)

The `dispatch_rpc` function have been moved to the `service` module
where it really belongs. The two options --log-request and
--log-response were pouring the logs with useless informations,
sometimes twice (i.e. /jsonrpc). The logging level was debug because it
annoys people to have the whole `params` logged. It would be better to
introduce a bit of logging (info level) in every "rpc over rpc"-like
controller methods. Duty for another PR? I myself use mitmproxy whenever
I want the complete logs (request+response) of the web server.

By the way, the logs in `service/server.py` were not using the "correct"
logger name, it seemed to be dead code to me so I removed it too, heh.

---
## [cossacklabs/themis](https://github.com/cossacklabs/themis)@[1ca96de89b...](https://github.com/cossacklabs/themis/commit/1ca96de89b66391114f615658fbc4819aa248b9b)
#### Wednesday 2021-12-22 10:57:46 by Alexei Lozovsky

Add missing OpenSSL includes (#684)

* Add missing OpenSSL includes

Add those files use BIGNUM API of OpenSSL but do not include relevant
headers. Due to miraculous coincidence, this seems to somehow work for
the OpenSSL versions we use, but only because either existing headers
include this "bn.h" transitively, or because the compiler generates
code that kinda works without function prototype being available.

However, curiously enough, this breaks when building Themis for macOS
with recent OpenSSL 1.1.1g but not with OpenSSL 1.0.2, or OpenSSL 1.1.1g
on Linux. The issue manifests itself as missing "_BN_num_bytes" symbol.
Indeed, there is no such symbol because this function is implemented as
a macro via BN_num_bits(). However, because of the missing header, the
compiler -- being C compiler -- decides that this must be a function
"int BN_num_bytes()" and compiles it like a function call.

Add the missing includes to define the necessary macros and prototype,
resolving the issue with OpenSSL 1.1.1g. It must have stopped including
<openssl/bn.h> transitively, revealing this issue.

This is why you should always include and import stuff you use directly,
not rely on transitive imports.

P.S. A mystery for dessert: BoringSSL backend *includes* <openssl/bn.h>.

* Treat warnings as errors in Xcode

In order to prevent more silly issues in the future, tell Xcode to tell
the compiler to treat all warnings as errors. That way the build should
fail earlier, and the developers will be less likely to ignore warnings.

* Fix implicit cast warnings

Now that we treat warnings as errors, let's fix them.

themis_auth_sym_kdf_context() accepts message length as "uint32_t" while
it's callers use "size_t" to avoid early casts and temporary values.
However, the message length has been checked earlier and will fit into
"uint32_t", we can safely perform explicit casts here.

* Suppress documentation warnings (temporarily)

Some OpenSSL headers packaged with Marcin's OpenSSL that we use have
borked documentation comments. This has been pointed out several
times [1][2], but Marcin concluded this needs to be fixed upstream.

[1]: https://github.com/krzyzanowskim/OpenSSL/pull/79
[2]: https://github.com/krzyzanowskim/OpenSSL/pull/41

Meanwhile, having those broken headers breaks the build if the warnings
are treated as errors. Since we can't upgrade Marcin's OpenSSL due to
other reasons (bitcode support), we have no hope to resolve this issue.

For the time being, suppress the warnings about documentation comments.

* Fix more implicit cast warnings

There are more warnings actual only for 32-bit platforms. Some iOS
targets are 32-bit, we should avoid warnings there as well.

The themis_scell_auth_token_key_size() and
themis_scell_auth_token_passphrase_size() functions compute the size of
the autentication token from the header. They return uint64_t values to
avoid overflows when working with corrupted input data on the decryption
code path. However, they are also used on the encryption path where
corruption is not possible. Normally, authentication tokens are small,
they most definitely fit into uint32_t, and this is the type used in
Secure Cell data format internally.

It is not safe to assign arbitrary uint64_t to size_t on 32-bit
platforms. However, in this case we are sure that auth tokenn length
fits into uint32_t, which can be safely assigned to size_t.

Note that we cast into uint32_t, not size_t. This is to still cause
a warning on platforms with 16-bit size_t (not likely, but cleaner).

---
## [huyenthanh09/gooddata-ui-sdk](https://github.com/huyenthanh09/gooddata-ui-sdk)@[62a943bd47...](https://github.com/huyenthanh09/gooddata-ui-sdk/commit/62a943bd47a6dd656d8a37a999176534fae67fbf)
#### Wednesday 2021-12-22 11:09:22 by Dan Homola

Implement LRUCache and use it

Since the lru-cache in version 4 (the last compatible with IE11) needs
specific setup when used with Webpack 5 (process polyfills), it makes
GoodData.UI unusable with create-react-app 5 that migrated to Webpack 5
and makes it impossible to alter these settings out of the box.

As a workaround, we wanted to migrate to another LRU implementation,
however none of the reasonably used existing implementations were good
for our particular use cases (IE11 support and maxAge):

* quick-lru: does not support IE11 because it uses generators.
  Older versions do not have maxAge which we need
* tiny-lru: does not work with cache size 1 (I sent a PR to fix that
  but I do not expect that to be merged, the package is quite stale)
* hashlru: does not have maxAge

So I ended up implementing a LRU cache in our code base. The code uses
the hashlru algorithm and is heavily inspired by quick-lru (which we
should migrate to once IE11 is dropped and get rid of the version
added in this commit).

One particular caveat of the hashlru algorithm (that is not that
important in my opinion) is that the maxSize is not precise:
the cache can hold more keys than the maxSize, but not by much (it very
much depends on the particular sequence of inserts and evicts). It will,
however, never be more than twice the maxSize. Since we use the maxSize
as more of a "do not cache millions of items here" kind of mechanism,
I think this caveat is ok for us given the performance gains
and relative code simplicity.

JIRA: RAIL-2928

---
## [headassbtw/tiny-iso-engine](https://github.com/headassbtw/tiny-iso-engine)@[0a2317523d...](https://github.com/headassbtw/tiny-iso-engine/commit/0a2317523dace81b12061bcb30c01d0551311c89)
#### Wednesday 2021-12-22 11:57:38 by headassbtw

bear cache files from arch, because fuck you manjaro!

---
## [Yonle/MixedTermux](https://github.com/Yonle/MixedTermux)@[17af4a0262...](https://github.com/Yonle/MixedTermux/commit/17af4a0262cd8a997068f020f34461f6aa9a9094)
#### Wednesday 2021-12-22 13:49:40 by Yonle

Remove Guikded and Discord community link

Those two fucking shit platform community link is NOW EXPIRED, BITCH

---
## [fuglore/PD2-Hyper-Heisting](https://github.com/fuglore/PD2-Hyper-Heisting)@[187f6f8631...](https://github.com/fuglore/PD2-Hyper-Heisting/commit/187f6f86318d13fb16bbd034bb8192009b0bee3a)
#### Wednesday 2021-12-22 15:39:30 by Fuglore

i dont want to jinx it but i think i got it

-fixed blah blah blah blah fuck you

---
## [fuglore/PD2-Hyper-Heisting](https://github.com/fuglore/PD2-Hyper-Heisting)@[b9c511987b...](https://github.com/fuglore/PD2-Hyper-Heisting/commit/b9c511987b3b3c462949c8a870a6b1151225bb0e)
#### Wednesday 2021-12-22 15:39:30 by Fuglore

phase 2-ery.

i suck ass at things

- fixed some team ai shit

- fixed a crash related to coplogictravel

- fruitless attempts at making the alaskan deal crash go away

---
## [ONLYOFFICE-QA/testing-site-onlyoffice](https://github.com/ONLYOFFICE-QA/testing-site-onlyoffice)@[fbe6e8085b...](https://github.com/ONLYOFFICE-QA/testing-site-onlyoffice/commit/fbe6e8085b48c5d1ea093957452253d4afea6bb8)
#### Wednesday 2021-12-22 15:48:53 by Pavel Lobashov

Add pending for two test with opening Documents (#597)

For some reason this test raise error that looks like this:
```
There are some errors in the Web Console: ["https://teamlab.info/?Site_Testing=4testing 380:62 Uncaught TypeError: Cannot read properties of null (reading 'split')"]
```

Problem is that this error NEVER shown when I tried to manually
reproduce it
And I never remember experience like this - I'm almost sure that some
error is happened during this test, but seems maybe some code just hide
it or maybe chrome for some reason hide it
I spend several hours trying different methods to catch this error
manually and there is no success
So I think I just pending this test and as soon as they start to be OK
we'll remove that pending. Not sure then
And sometimes we should check those pendings, I think they can
magically fix itself as they were magically broken

---
## [leapofazzam123/termux-plus](https://github.com/leapofazzam123/termux-plus)@[b22698c883...](https://github.com/leapofazzam123/termux-plus/commit/b22698c883e1a486ca1fffc8285aa3b22c4abc2f)
#### Wednesday 2021-12-22 16:01:51 by Leap of Azzam

fuck you ci

Signed-off-by: Leap of Azzam <leapofazzam@gmail.com>

---
## [clarencelol/kernel_xiaomi_sdm660-4.19](https://github.com/clarencelol/kernel_xiaomi_sdm660-4.19)@[8667fb0e8b...](https://github.com/clarencelol/kernel_xiaomi_sdm660-4.19/commit/8667fb0e8bf567d00f884f87252789c4c06874b8)
#### Wednesday 2021-12-22 16:32:50 by Peter Zijlstra

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
Signed-off-by: Adam W. Willis <return.of.octobot@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>

---
## [ctm/Bataan-Memorial-Death-March](https://github.com/ctm/Bataan-Memorial-Death-March)@[64dbf6a285...](https://github.com/ctm/Bataan-Memorial-Death-March/commit/64dbf6a285eaa38e73de8238e68be4e853cb200e)
#### Wednesday 2021-12-22 17:04:57 by Clifford T. Matthews

Includes today's "speed" pack run.

I was very slow and was not able to keep my HR up.  I think this was
mostly due to me not having fully recovered from covid after all.
After yesterday's rest day run I thought my stats were suggestive of
complete recovery, but later in the day I was much more tired than I
should have been.  In fact, I slept basically from 7pm until 4:45am.

When I got up, I looked back to see what sort of preparation I had
done for my fastest 8.5 mile pack runs in the past and I then decided
to go with two quad espressos, but to do it fasted rather than eating
oatmeal before and drinking Tailwind during.  I strongly suspected
that would slow me down but I also knew it would be hard to tease out
how much of the slowdown came from fasting and how much would come
from covid / post-covid.

I chose to do this weird experiment mostly because I'm overweight and
it's early enough in the training season that I'd rather cut weight
now and lose some performance than resign myself to my new higher
weight.

So, I'm not at all happy with my performance today, but I'm hoping
I'll rebound.  OTOH, I'm not actually competing at BMDM this year so
in that sense it doesn't matter.  I'm also deliberately trying to do
longer stuff so that when May 2nd comes around I'll be in better shape
for the Cocodona 250.

TLDR: Waah! The sun was in my eyes.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[d005d76f0b...](https://github.com/timothymtorres/tgstation/commit/d005d76f0bd201060b6ee515678a4b6950d9f0eb)
#### Wednesday 2021-12-22 19:22:03 by Kylerace

Fixes Massive Radio Overtime, Implements a Spatial Grid System for Faster Searching Over Areas (#61422)

a month or two ago i realized that on master the reason why get_hearers_in_view() overtimes so much (ie one of our highest overtiming procs at highpop) is because when you transmit a radio signal over the common channel, it can take ~20 MILLISECONDS, which isnt good when 1. player verbs and commands usually execute after SendMaps processes for that tick, meaning they can execute AFTER the tick was supposed to start if master is overloaded and theres a lot of maptick 2. each of our server ticks are only 50 ms, so i started on optimizing this.

the main optimization was SSspatial_grid which allows searching through 15x15 spatial_grid_cell datums (one set for each z level) far faster than iterating over movables in view() to look for what you want. now all hearing sensitive movables in the 5x5 areas associated with each spatial_grid_cell datum are stored in the datum (so are client mobs). when you search for one of the stored "types" (hearable or client mob) in a radius around a center, it just needs to

    iterate over the cell datums in range
    add the content type you want from the datums to a list
    subtract contents that arent in range, then contents not in line of sight
    return the list

from benchmarks, this makes short range searches like what is used with radio code (it goes over every radio connected to a radio channel that can hear the signal then calls get_hearers_in_view() to search in the radios canhear_range which is at most 3) about 3-10 times faster depending on workload. the line of sight algorithm scales well with range but not very well if it has to check LOS to > 100 objects, which seems incredibly rare for this workload, the largest range any radio in the game searches through is only 3 tiles

the second optimization is to enforce complex setter vars for radios that removes them from the global radio list if they couldnt actually receive any radio transmissions from a given frequency in the first place.

the third optimization i did was massively reduce the number of hearables on the station by making hologram projectors not hear if dont have an active call/anything that would make them need hearing. so one of hte most common non player hearables that require view iteration to find is crossed out.

also implements a variation of an idea oranges had on how to speed up get_hearers_in_view() now that ive realized that view() cant be replicated by a raycasting algorithm. it distributes pregenerated abstract /mob/oranges_ear instances to all hearables in range such that theres at max one per turf and then iterates through only those mobs to take advantage of type-specific view() optimizations and just adds up the references in each one to create the list of hearing atoms, then puts the oranges_ear mobs back into nullspace. this is about 2x as fast as the get_hearers_in_view() on master

holy FUCK its fast. like really fucking fast. the only costly part of the radio transmission pipeline i dont touch is mob/living/Hear() which takes ~100 microseconds on live but searching through every radio in the world with get_hearers_in_radio_ranges() -> get_hearers_in_view() is much faster, as well as the filtering radios step

the spatial grid searching proc is about 36 microseconds/call at 10 range and 16 microseconds at 3 range in the captains office (relatively many hearables in view), the new get_hearers_in_view() was 4.16 times faster than get_hearers_in_view_old() at 10 range and 4.59 times faster at 3 range

SSspatial_grid could be used for a lot more things other than just radio and say code, i just didnt implement it. for example since the cells are datums you could get all cells in a radius then register for new objects entering them then activate when a player enters your radius. this is something that would require either very expensive view() calls or iterating over every player in the global list and calling get_dist() on them which isnt that expensive but is still worse than it needs to be

on normal get_hearers_in_view cost the new version that uses /mob/oranges_ear instances is about 2x faster than the old version, especially since the number of hearing sensitive movables has been brought down dramatically.

with get_hearers_in_view_oranges_ear() being the benchmark proc that implements this system and get_hearers_in_view() being a slightly optimized version of the version we have on master, get_hearers_in_view_as() being a more optimized version of the one we have on master, and get_hearers_in_LOS() being the raycasting version currently only used for radios because it cant replicate view()'s behavior perfectly.

---
## [petebacondarwin/wrangler2](https://github.com/petebacondarwin/wrangler2)@[78cd0804de...](https://github.com/petebacondarwin/wrangler2/commit/78cd0804def1a3246f8a4f6b1695bd91e81c1ad1)
#### Wednesday 2021-12-22 19:56:17 by Sunil Pai

implement custom builds, for `dev` and `publish` (#149)

* implement custom builds, for `dev` and `publish`

The code here is a bit jank, but we should probably refactor the way we pass arguments to dev and publish to 'fix' it properly. Anyway.

This PR adds custom builds to wrangler2 (https://developers.cloudflare.com/workers/cli-wrangler/configuration#build).
- In `wrangler.toml`, you can configure `build.command` and `build.cwd` and it'll be called before `publish` or `dev`. There's some discussion to be had whether we're going to deprecate this config commands, but we'll support it until then anyway.
- We _don't_ support `build.watch_dir`. We could, and I'm happy to add it after we discuss; but the idea is that watching shouldn't be wrangler's responsibility (which we've already broken with plain `dev`, and `pages dev`, so maybe we're wrong)
- You can pass the command after a last `--` in the cli (no support for `cwd` there). eg - `wrangler dev output/index.js -- some-build-command --out output/index.js`.

* Add a changeset

* fix lint error

* update snapshot tests

* remove `--`, add `watch_dir`

- removed the `--` option. We should have documentation showing how to do this with bash etc.
- Added support for `watch_dir`
- also added a definition for running tests from the root because it was annoying me to keep changing dirs to run tests

* log the name of the file that changed during a custom build

---
## [folio-org/stripes-core](https://github.com/folio-org/stripes-core)@[daed280c9e...](https://github.com/folio-org/stripes-core/commit/daed280c9e2831a2303274bdcf911a3981c6765e)
#### Wednesday 2021-12-22 20:32:16 by Zak Burke

the most humble offering possible to the lint gods (#1148)

And there were developers sitting at their laptops nearby, keeping watch
over their code by night. Just then, an angel of lint stood before them,
and the glory of lint shone all around them, and they were terrified.
But the angel said unto them, "Do not be afraid! For behold! I bring you
good news of great joy that will be for all the people: Today in the
module of stripes-core, I discovered one insignificant space with no
semantic value and no visual clutter, but it really bugs me anyway. And
this will be a sign to you: you will find two complaints on every PR
about it, even when they have nothing to do with this file.

And suddenly there appeared around every stripes-core PR a great
multitude of lint complaints, saying:

```
Multiple spaces found before '/\.\/.*\.js$/'
```

When the lint angels had left them and gone into heaven, the developers
said to one another, "One lousy space? Was that guy serious?"

---
## [kriskenn/terminal](https://github.com/kriskenn/terminal)@[f2ebb21bd1...](https://github.com/kriskenn/terminal/commit/f2ebb21bd13b20db38305136d34fa0778baf7920)
#### Wednesday 2021-12-22 20:50:17 by Mike Griese

Add snap-layouts support to the Terminal (#11680)

Adds snap layout support to the Terminal's maximize button. This PR is
full of BODGY, so brace yourselves.

Big thanks to Chris Swan in #11134 for building the prototype.
I don't believe this solves #8795, because XAML islands can't get
nchittest messages

- The window procedure for the drag bar forwards clicks on its client
  area to its parent as non-client clicks.
- BODGY: It also _manually_ handles the caption buttons. They exist in
  the titlebar, and work reasonably well with just XAML, if the drag bar
  isn't covering them.
- However, to get snap layout support, we need to actually return
  `HTMAXBUTTON` where the maximize button is. If the drag bar doesn't
  cover the caption buttons, then the core input site (which takes up
  the entirety of the XAML island) will steal the `WM_NCHITTEST` before
  we get a chance to handle it.
- So, the drag bar covers the caption buttons, and manually handles
  hovering and pressing them when needed. This gives the impression that
  they're getting input as they normally would, even if they're not
  _really_ getting input via XAML.
- We also need to manually display the button tooltips now, because XAML
  doesn't know when they've been hovered for long enough. Hence, the
  `_displayToolTip` `ThrottledFuncTrailing`

## Validation
Minimized, maximized, restored down, hovered the buttons slowly, moved
the mouse over them quickly, they feel the same as before. But now with
snap layouts appearing.

## TODO!
* [x] I'm working on getting the ToolTips on the caption buttons back. Alas, I needed a demo of this _today_, so I'll fix that tomorrow morning.
* [x] mild concern: I should probably test Win 10 to make sure there wasn't weird changes to the message loop in win11 that means this is broken on win10.
* [x] I think I used the wrong issue number for tons of my comments throughout this PR. Double check that. Should be #9443, not #9447. 

Closes #9443
I thought this took care of #8587 ~as a bonus, because I was here, and the fix is _now_ trivial~, but looking at the latest commit that regressed.

Co-authored-by: Chris Swan <chswan@microsoft.com>

---
## [flofriday/Lox](https://github.com/flofriday/Lox)@[56b9eaca62...](https://github.com/flofriday/Lox/commit/56b9eaca62d4cf144a557e8ac25313e31c7ff3de)
#### Wednesday 2021-12-22 21:16:45 by flofriday

Implement the jLox interpreter till chapter 10.1
Still very excited but finding bugs with only the hardcopy in hand is
kinda tedious.
Whatever, it is amazing to now have loops and see actual code getting
run by the interpreter. Is it already turing-complete? I think so.

Damn this really is exciting to learn 😊

---
## [MasQueElite/KtaneContent](https://github.com/MasQueElite/KtaneContent)@[d37e027de5...](https://github.com/MasQueElite/KtaneContent/commit/d37e027de5b878897eea7c3c54315baf6893630b)
#### Wednesday 2021-12-22 21:42:52 by MasQueElite

Linted old manuals, as well as my Cent. translations

Description: pain.

Also, could you check my translated 1000 Words and my translated Clock?
Seems like 1000 Words has an wrong word, and the Clock has an svg without newlines? (also it gets rid of the darkmode stuff oof sorry keep that)

Also, check The Swan (original) as well, I think that change is weird, but maybe the linter complained about it, I don't remember.
And I also deleted (in my translated Double-Oh) the .dark table, .dark td .strike selectors, sorry :c restore those as well plz
Aaaaaaaaand I think the rest is up do date. That's all about linting the original manuals.

---
## [MasQueElite/KtaneContent](https://github.com/MasQueElite/KtaneContent)@[db2e8af0c2...](https://github.com/MasQueElite/KtaneContent/commit/db2e8af0c2d4839934c9eb1a68ade6c50cf6ac9a)
#### Wednesday 2021-12-22 21:45:31 by MasQueElite

Linted old manuals, as well as my Cent. translations

Description: pain.

Also, could you check my translated 1000 Words and my translated Clock?
Seems like 1000 Words has a wrong word, and the Clock has an svg without newlines? (also it gets rid of the darkmode stuff oof sorry keep that)

Also, check The Swan (original) as well, I think that change is weird, but maybe the linter complained about it, I don't remember.
And I also deleted (in my translated Double-Oh) the .dark table, .dark td .strike selectors, sorry :c restore those as well plz
Aaaaaaaaand I think the rest is up do date. That's all about linting the original manuals.

---
## [dotnet/maui](https://github.com/dotnet/maui)@[ac6befcbee...](https://github.com/dotnet/maui/commit/ac6befcbee23fae2bd358d9ed3217757029a9d1f)
#### Wednesday 2021-12-22 22:11:19 by Jonathan Peppers

[controls] Brush.Foo should return immutable instances (#3824)

When profiling a `dotnet new maui` app, with this package:

https://github.com/jonathanpeppers/Mono.Profiler.Android

The `alloc` report shows:

    Allocation summary
    Bytes      Count  Average Type name
    39984        147 2 72     Microsoft.Maui.Controls.SolidColorBrush

Stack trace:

    38352 bytes from:
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.VisualElement:.cctor ()
    (wrapper runtime-invoke) object:runtime_invoke_void (object,intptr,intptr,intptr)
    Microsoft.Maui.Controls.Brush:.cctor ()

Reviewing the `Brush` class, there are indeed 147 `SolidColorBrush`
created on startup that are stored in fields.

But what is weird about this, is that `SolidColorBrush` is mutable!

    public Color Color
    {
        get => (Color)GetValue(ColorProperty);
        set => SetValue(ColorProperty, value);
    }

So I could literally write code like:

    Brush.Blue.Color = Colors.Red;

Blue is red! (insert evil laughter?)

I think the appropriate fix here is that all of these `static
readonly` fields should just be properties that return a new
`ImmutableBrush`. We can cache the values in fields on demand. Then
someone can't do something evil like change `Blue` to `Red`?

I reviewed WPF source code to check what they do, and they took a
similar approach:

https://github.com/dotnet/wpf/blob/5e8187344b2b561ef08b9ca2735cd89cbdd3c11e/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/brushes.cs#L33-L1586

We should make this API change now before MAUI is stable, and we have
the side benefit to save 39984 bytes of memory on startup?

I added tests for these scenarios, and discovered 3 typos for `Brush`
colors that listed the wrong color.

---
## [hifocus/BlogUtils](https://github.com/hifocus/BlogUtils)@[05ddf87c50...](https://github.com/hifocus/BlogUtils/commit/05ddf87c5044e09665bb3e8e5d44da96d58cfb16)
#### Wednesday 2021-12-22 23:29:01 by Focus Chen

makeup for mistakes

fuck git cli and github desktop, fuck you

---

