## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-01-25](docs/good-messages/2023/2023-01-25.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,255,913 were push events containing 3,418,209 commit messages that amount to 260,147,419 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 60 messages:


## [SapiensAnatis/DragaliaAPI](https://github.com/SapiensAnatis/DragaliaAPI)@[56ef2d9afb...](https://github.com/SapiensAnatis/DragaliaAPI/commit/56ef2d9afb4c13c7f17b7e6ea9c1ce6a9e812e40)
#### Wednesday 2023-01-25 00:21:16 by Jay Malhotra

Add basic property validation (#111)

This is by no means exhaustive but the focus for now is limiting the
length of strings, particularly those which may end up in the database
-- Postgres is ridiculously forgiving with its TEXT type.

One other area worth looking at it party numbers and unit positions,
these will put the DB In a funny state but are unlikely to cause any
issues for users beyond the one with the invalid data.

---
## [47-studio-org/git-gui](https://github.com/47-studio-org/git-gui)@[8f23432b38...](https://github.com/47-studio-org/git-gui/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Wednesday 2023-01-25 00:31:18 by Johannes Schindelin

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
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [Zero-Percent-Angel/coyote-bayou](https://github.com/Zero-Percent-Angel/coyote-bayou)@[9821251d81...](https://github.com/Zero-Percent-Angel/coyote-bayou/commit/9821251d8178f6ed89c4cadfec051d38beae4658)
#### Wednesday 2023-01-25 00:34:50 by Superlagg

Merge pull request #1481 from ARF-SS13/Fuck-you-github

Map adjustments!

---
## [Zero-Percent-Angel/coyote-bayou](https://github.com/Zero-Percent-Angel/coyote-bayou)@[b7164095fd...](https://github.com/Zero-Percent-Angel/coyote-bayou/commit/b7164095fd1ad42d581cdce1b1861d180ec50323)
#### Wednesday 2023-01-25 00:34:50 by Superlagg

Merge pull request #1482 from ARF-SS13/Fuck-you-github

Stinky nash gate buttons fixed

---
## [Zero-Percent-Angel/coyote-bayou](https://github.com/Zero-Percent-Angel/coyote-bayou)@[70042337db...](https://github.com/Zero-Percent-Angel/coyote-bayou/commit/70042337dbefb532ee9e1eb640edb00e9280c932)
#### Wednesday 2023-01-25 00:34:50 by A Psycho

Merge pull request #1483 from ARF-SS13/Fuck-you-github

Small mapfixes

---
## [michaeldelago/azerothcore-wotlk](https://github.com/michaeldelago/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/michaeldelago/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Wednesday 2023-01-25 00:38:05 by ICXCNIKA

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[36090c1b20...](https://github.com/tgstation/tgstation/commit/36090c1b206dee8b643e83607e333c29906b6bc8)
#### Wednesday 2023-01-25 01:14:05 by san7890

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
## [peff/git](https://github.com/peff/git)@[69bbbe484b...](https://github.com/peff/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Wednesday 2023-01-25 02:01:29 by Jeff King

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
## [Vhmit/kernel_asus_msm8937](https://github.com/Vhmit/kernel_asus_msm8937)@[b68bc9bf94...](https://github.com/Vhmit/kernel_asus_msm8937/commit/b68bc9bf94e1b0f08b4fceb09515bbd76a6eadc9)
#### Wednesday 2023-01-25 02:25:46 by Steven Barrett

ZEN: Implement zen-tune v4.12

4.9:
In a surprising turn of events, while benchmarking and testing
hierarchical scheduling with BFQ + writeback throttling, it turns out
that raising the number of requests in queue _actually_ improves
responsiveness and completely eliminates the random stalls that would
normally occur without hierarchical scheduling.

To make this test more intense, I used the following test:

Rotational disk1: rsync -a /source/of/data /target/to/disk1
Rotational disk2: rsync -a /source/of/data /target/to/disk2

And periodically attempted to write super fast with:
dd if=/dev/zero of=/target/to/disk1/block bs=4096

This wrote 10gb incredibly fast to writeback and I encountered zero
stalls through this entire test of 10-15 minutes.

My suspicion is that with cgroups, BFQ is more able to properly sort
among multiple drives, reducing the chance of a starved process.  This
plus writeback throttling completely eliminate any outstanding bugs with
high writeback ratios, letting the user enjoy low latency writes
(application thinks they're already done), and super high throughput due
to batched writes in writeback.

Please note however, without the following configuration, I cannot
guarantee you will not get stalls:

CONFIG_BLK_CGROUP=y
CONFIG_CGROUP_WRITEBACK=y
CONFIG_IOSCHED_CFQ=y
CONFIG_CFQ_GROUP_IOSCHED=y
CONFIG_IOSCHED_BFQ=y
CONFIG_BFQ_GROUP_IOSCHED=y
CONFIG_DEFAULT_BFQ=y
CONFIG_SCSI_MQ_DEFAULT=n

Special thanks to h2, author of smxi and inxi, for providing evidence
that a configuration specific to Debian did not cause stalls found the
Liquorix kernels under heavy IO load.  This specific configuration
turned out to be hierarchical scheduling on CFQ (thus, BFQ as well).

4.10:
During some personal testing with the Dolphin emulator, MuQSS has
serious problems scaling its frequencies causing poor performance where
boosting the CPU frequencies would have fixed them.  Reducing the
up_threshold to 45 with MuQSS appears to fix the issue, letting the
introduction to "Star Wars: Rogue Leader" run at 100% speed versus about
80% on my test system.

Also, lets refactor the definitions and include some indentation to help
the reader discern what the scope of all the macros are.

4.11:
Increase MICRO_FREQUENCY_UP_THRESHOLD from 95 to 85
Increase MIN_FREQUENCY_UP_THRESHOLD from 11 to 6

These changes should help make using CFS feel a bit more responsive when
working with mostly idle workloads, browsing the web, scrolling through
text, etc.

Increasing the minimum frequency up threshold to 6% may be too
aggressive though.  Will revert this setting if it causes significant
battery drain.

4.12:
Make bfq the default MQ scheduler

Reduce default sampling down factor from 10 to 1

With the world eventually moving to a more laptop heavy configuration,
it's getting more important that we can reduce our frequencies quickly
after performing work.  This is normal with a ton of background
processes that need to perform burst work then sleep.

Since this doesn't really impact performance too much, lets not keep it
part of ZEN_INTERACTIVE.

Some time ago, the minimum frequency up threshold was set to 1 by
default, but the zen configuration was never updated to take advantage
of it.

Remove custom MIN_FREQUENCY_UP_THRESHOLD for MuQSS / ZEN_INTERACTIVE
configurations and make 1 the default for all choices.

Change-Id: I2a31fbc97fe12ffce30457ec2e83ed25764e2daf
Signed-off-by: Harsh Shandilya <msfjarvis@gmail.com>

---
## [TurtleShroom/TSP_STORYTIME_RIDES_AGAIN](https://github.com/TurtleShroom/TSP_STORYTIME_RIDES_AGAIN)@[64346e3098...](https://github.com/TurtleShroom/TSP_STORYTIME_RIDES_AGAIN/commit/64346e3098efc96ee544b19c32d0e7aff1f98887)
#### Wednesday 2023-01-25 02:28:47 by TURTLESHROOM

Minor

1. Removed swearing and sexual terms where found.

2. Maintenance of code.

3. Added missing names and resolved Backstory errors for set Biographies.

4. Fixed typographical errors.

5. Balancing adjustments to varying items.

6. Fixed Goblin Faction not spawning.

7. Imported Rune Essence stones.

8. Imported some Tips that were not obscene or whiny.

9. While viewing the Tips on Isengriff's branch of the Mod, I finally solved the mystery. It turns out that Isengriff's reason for hating me was actually a lot pettier than I thought. After years of friendship, Isengriff, who is a sodomite, finally discovered my opinions on homosexuality. Isengriff was my friend, so I refrained from shooting my mouth off about his life choices, and never once debated or discussed politics or sexual hot button topics. Though I showed him the utmost respect, at the end of the day, it seems that he is too fragile to associate with a person who does not applaud his life choices, even if that person never said anything about it. This is normal for people like him, but still a shame, because he was a really nice, intelligent person.

10. Made the Tomato Frog Work Giver generic to account for other animals that have cysts that you cut off.

11. You no longer need to mine for Worms. You just dig for them now.

12. To dig for Worms, you must have the Capacity for Sight.

13. Adjusted UI images.

14. Out of respect for his privacy, an UI  picture of a man holding a can of root beer has been censored. This person is presumed to be Isengriff, so it's better to be safe than sorry.

15. Corrected Common Era to Anno Domini. If it's good enough for NASA to inscribe ON THE MOON, it's good enough for us in this Mod.

---
## [jedisct1/boringssl](https://github.com/jedisct1/boringssl)@[0d5b608614...](https://github.com/jedisct1/boringssl/commit/0d5b6086143d19f86cc5d01b8944a1c13f99be24)
#### Wednesday 2023-01-25 03:42:15 by David Benjamin

Maintain a frame pointer in aesni-gcm-x86_64.pl and add SEH unwind codes

Some profiling systems cannot unwind with CFI and benefit from having a
frame pointer. Since this code doesn't have enough register pressure to
actually need to use rbp as a general register, this change tweaks
things so that a frame pointer is preserved.

As this would invalidate the SEH handler, just replace it with proper
unwind codes, which are more profiler-friendly and supportable by our
unwind tests. Some notes on this:

- We don't currently support the automatic calling convention conversion
  with unwind codes, but this file already puts all arguments in
  registers, so I just renamed the arguments and put the last two
  arguments in RDI and RSI. Those I stashed into the parameter stack
  area because it's free storage.

- It is tedious to write the same directives in both CFI and SEH. We
  really could do with an abstraction. Although since most of our
  functions need a Windows variation anyway.

- I restored the original file's use of PUSH to save the registers.
  This matches what Clang likes to output anyway, and push is probably
  smaller than the corresponding move with offset. (And it reduces how
  much thinking about offsets I need to do.)

- Although it's an extra instruction, I restored the original file's
  separate fixed stack allocation and alloca for the sake of clarity.

- The epilog is constrained by Windows being extremely picky about
  epilogs. (Windows doesn't annotate epilogs and instead simulates
  forward.) I think other options are possible, but using LEA with an
  offset to realign the stack for the POPs both matches the examples in
  Windows and what Clang seems to like to output. The original file used
  MOV with offset, but it seems to be related to the funny SEH handler.

- The offsets in SEH directives may be surprising to someone used to CFI
  directives or a SysV RBP frame pointer. All three use slightly
  different baselines:

  CFI's canonical frame address (CFA) is RSP just before a CALL (so
  before the saved RIP in stack order). It is 16-byte aligned by ABI.

  A SysV RBP frame pointer is 16 bytes after that, after a saved RIP and
  saved RBP. It is also 16-byte aligned.

  Windows' baseline is the top of the fixed stack allocation, so
  potentially some bytes after that (all pushreg and allocstack
  directives). This too is required to be 16-byte aligned.

  Windows, however, doesn't require the frame register actually contain
  the fixed stack allocation. You can specify an offset from the value
  in the register to the actual top. But all the offsets in savereg,
  etc., directives use this baseline.

Performance difference is within measurement noise.

This does not create a stack frame for internal functions so
frame-pointer unwinding may miss a function or two, but the broad
attribution will be correct.

Change originally by Clemens Fruhwirth. Then reworked from Adam
Langley's https://boringssl-review.googlesource.com/c/boringssl/+/55945
by me to work on Windows and fix up some issues with the RBP setup.

Bug: b/33072965, 259
Change-Id: I52302635a8ad3d9272404feac125e2a4a4a5d14c
Reviewed-on: https://boringssl-review.googlesource.com/c/boringssl/+/56128
Reviewed-by: Adam Langley <agl@google.com>
Commit-Queue: David Benjamin <davidben@google.com>

---
## [DrewKimball/cockroach](https://github.com/DrewKimball/cockroach)@[8ae602660d...](https://github.com/DrewKimball/cockroach/commit/8ae602660d16be76331c6705b748eb3ba7799cb0)
#### Wednesday 2023-01-25 03:47:02 by craig[bot]

Merge #89613 #93985 #93989

89613: gossip: remove frequent gossiping of gossip client connections r=irfansharif a=a-robinson

These gossip-clients keys make up two thirds or more of the gossip traffic in various large clusters I've inspected, consuming almost an entire CPU core in the worst case I've seen. They don't provide enough value to justify that sort of ongoing cost, so this commit removes them entirely as well as the periodic logging of the gossip network and the crdb_internal.gossip_network table, both of which relied on them.

These gossip-clients keys make up two thirds or more of the gossip
traffic in various large clusters I've inspected, consuming almost an
entire CPU core in the worst case I've seen. They don't provide enough
value to justify that sort of ongoing cost, so this commit removes them
entirely as well as the periodic logging of the gossip network and the
crdb_internal.gossip_network table, both of which relied on them.

Release note (backward-incompatible change): We've stopped
supporting/populating the crdb_internal.gossip_network table. It was an
internal table with no API guarantees (so perhaps no meriting a release
note?).

Release note (performance improvement): Significantly reduced CPU usage
of the underlying gossip network in large clusters.

---

Informs #51838 (largely fixes it for practical purposes, although there's likely still more that could be done)

This is clearly going to break [the gossip roachtest](https://github.com/cockroachdb/cockroach/blob/master/pkg/cmd/roachtest/tests/gossip.go#L50-L58), but between `@irfansharif` kindly volunteering to fix that up separately and his existing TODO in that file I've left that out of this change.

I don't know if completely removing the gossip_network table is really the best idea or if it should just be left in and only populated with the clients from the local node. For example, when run in a mixed version cluster does `debug zip` run all of its sql commands against the local node or does it run some against remote nodes? If an old node ever tries to query the `gossip_network` table on a different node it could have a bad time.

`@irfansharif` `@kvoli` 

93985: ui: degrade gracefully when regions aren't known r=matthewtodd a=matthewtodd

Part of #89949

Previously, when a tenant SQL instance had spun down (leaving us no way to remember which region it had been in), the SQL Activity pages would claim that statements and transactions had occurred in an "undefined" region.

This change moves from saying "undefined" to saying nothing at all, a slightly nicer user experience.

This broader problem of losing the region mapping has been described in #93268; we'll begin addressing it shortly.

Release note: None

93989: leaktest: exclude long running logging goroutines r=srosenberg a=nicktrav

The `leaktest` package detects potential goroutine leaks by snapshotting the set of goroutines running when `leaktest.AfterTest(t)` is called, returning a closure, and comparing the set of goroutines when the closure is called (typically `defer`'d).

A race condition was uncovered in #93849 whereby logging-related goroutines that are scheduled by an `init` function in `pkg/util/logging` can sometimes be spawned _after_ the `AfterTest` function is run. When the test completes and the closure is run, the test fails due to a difference in the before / after goroutine snapshots.

This mode of failure is deemed to be a false-positive. The intention of the logging goroutines are that they live for the duration of the process. However, exactly _when_ the goroutines scheduled in the `init` functions actually start run, and hence show up in the goroutine snapshots, is non-deterministic.

Exclude the logging goroutines from the `leaktest` checks to reduce the flakiness of tests.

Closes #93849.

Release note: None.

Epic: CRDB-20293

Co-authored-by: Alex Robinson <arobinson@cloudflare.com>
Co-authored-by: Matthew Todd <todd@cockroachlabs.com>
Co-authored-by: Nick Travers <travers@cockroachlabs.com>

---
## [WagicProject/wagic](https://github.com/WagicProject/wagic)@[067da7a444...](https://github.com/WagicProject/wagic/commit/067da7a44451f7ac1f1fc6520b89d69bc9f0d2be)
#### Wednesday 2023-01-25 04:00:49 by Eduardo MG

Added more cards from sets released in 2022

Thopter Shop
Aggressive Sabotage
Prayer of Binding
Temporary Lockdown
Tura Kenner�d, Skyknight
Tori D'Avenant, Fury Rider
Leaf-Crowned Visionary
Monstrous War-Leech
Blight Pile
Bite Down
Shore Up
Pixie Illusionist
Viashino Branchrider
Tolarian Geyser
Strength of the Coalition
Take Up the Shield
Scout the Wilderness
Research Thief
Tempered in Solitude
Voltage Surge
Runic Shot
Protect the Negotiators
Timely Interference
Coral Colony
Herd Migration
Eerie Soultender
Sunbathing Rootwalla
Phyrexian Missionary
Sprouting Goblin
Meria, Scholar of Antiquity
Zamriel, Seraph of Steel
Maeve, Insidious Singer
Vogar, Necropolis Tyrant
Nogi, Draco-Zealot
Imaryll, Elfhame Elite
Tribute to Urborg
Urborg Repossession
Vineshaper Prodigy
Elvish Hydromancer
Tyrant of Kher Ridges
Transmogrant's Crown
Gaea's Gift
Awaken the Woods
Emergency Weld
Gruesome Realization
Argivian Avenger
Aeronaut's Wings
Tocasia's Welcome
Union of the Third Path
Tocasia's Dig Site
Argothian Sprite
Bushwhack
Spectrum Sentinel
Dwarven Forge-Chanter
Unleash Shell
Brotherhood's End
Fade from History
Urza, Lord Protector
Mishra's Foundry
Iridian Maelstrom
Wilson, Refined Grizzly
Erinis, Gloom Stalker
Sharpshooter Elf
Tiamat's Fanatics
Duke Ulder Ravengard
Ghastly Death Tyrant
Penregon Strongbull
Mishra, Excavation Prodigy
Mishra's Onslaught
Fateful Handoff
Swiftgear Drake
Fortified Beachhead
Bitter Reunion
Urza's Rebuff
Robe of the Archmagi
Emperor Mihail II
Moira, Urborg Haunt
Greensleeves, Maro-Sorcerer
False Floor
Junji, the Midnight Sky
Kami of Restless Shadows
Jin-Gitaxias, Progress Tyrant
Unquenchable Fury

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[012b9af3ad...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/012b9af3ad235b0c070576bd3ddc876bdb9619af)
#### Wednesday 2023-01-25 04:11:27 by chris

Healer improvements:

Add plague-victims to the quest.
-The flavor text claims Cyclops is siphoning life from others into himself, causing a plague.
-Plague victims have a template that imobilizes them.
--Always peaceful, level set to 2/3rds, dex ac -5, special ac and dr 0, mmove 0, sounds set to MS_COUGH, removes poison, drain, sick, and magic resistance.
-Can be cured via the Staff or powerful healing magic.
--Plague victims will likely join you if you cure them.
-Cyclops will life save while there are plague victims on the level (asuming he has the QA)
-Giants in the quest have plague victims in sacks

New archons for healers
-One of each is found as a statue in the locate level.
--They have the plague, so they can't be used untill you can cure them.
-Iasoian archon (Recovery. Lvl 11)
--Passive star blades.
--Passively life-saves other pets (via mspec_used) and the player (via mcan).
---I'm sure this is totally balanced.
---In practive, pets (especially midlevel pets like this) are more likely to die than the PC, so it's PROBABLY fine.
---The Staff does let the PC "reload" the lifesaving at no cost, though.
-Panakeian archon (All-healing. Lvl 22)
--Spell list: Recover, mass cure fare, paralyze, mass cure close, sleep, destroy armor, destroy weapon, make web, cure self
-Hygieian archon (Hygiene. Lvl 27)
--Spell list: Death touch, lightning, geyser, acid rain, cure self, fire pillar.
--Archon fire weapon attacks
--Serpent bite and wrap attacks.

Healers have lower strength and higher int on average, and are Int casters.

Staff of Aesculapius
-Counts as a spell boost artifact for healing spells
-Apply it to poke monsters/yourself with it
--Poke yourself: counts as a unicorn horn (of the same blessedness as the staff)
--Poke a monster: peaceful+uncursed: good effect, peaceful+cursed: bad effect, hostile+uncursed: bad effect, hostile+cursed: good effect
---Good effects: Fixes blindness, deafness, stunning and confusion, sleep, paralysis, cancellation, or plague (one per turn, in that order)
---Bad effects: Causes deafness, blindness, stunning, confusion, paralysis, cancellation, or illness damage (one per turn, in that order)

Add centaur chieftain
-Makes centaurs better pets, works like orc captains/elves (all centaurs grow up into chieftains)

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[4688159dae...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/4688159dae0d7b33c14c175c1e6a4247d8117971)
#### Wednesday 2023-01-25 04:11:27 by chris

Drow healer main commit

Starting pet: A knight NPC
-Starts with armor and an amulet of nullify magic.

Quest: vertical cavern area
-Three staircases: only one up and down stair per level is functional, the others are "blocked by rubble"
--A new variable is used to coordinate between levels
--I COULD have coded all three to be active, but I like the variability
-Stepping on an AIR square in the quest causes you to fall to the cavern floor.
--Currently, it is not possible to descend by flying. I'm torn between allowing this and handwaving why you can't do it.
--Damage is inflicted after you finish ariving at the new level, possibly killing the PC.
--Monsters instead have their HP set to 1
-Always at least 6 levels long.
-The random filler level will also have its own layout in games where it exists.

Quest enemies
-'Y' cult drow
-Duergar: dwarves that turn into giants
--Duergar dwarf helms are darklight sources
-Kuo toa: weak enemies that deal retalitory damage when dying
-Chuul: U that can steal magic items in a grapple.


Quest nemesis
-TSMI damage type (Tentacles Steal Magic Items)
-Blood rain spell: Curse and blood-dilute
-Steam geyser spell: Hot water
-Loses 1HP per turn if the quest artifact is reclaimed
-More powerful at high insight

Esscooahlipboourrr revisions
-Change to a double sword
--Flavor more than anything, but this does make it pretty good as a weapon. It kinda NEEDS to be a good weapon, though, since its main special effect is most noticeable when it's wielded.
-Flavored as the "actual" quest artifact fused together with a pair of long swords.

Spore infested monsters
-mspores monster madness (nightmare helm)
-Spore zombie template
-Cordyceps template
--Launches exploding spores

Duplicate des file '#' handling for objects for monsters.
-Passes the provided string to create_particular (the wiz genesis function)

Refactors:
-always one-handed macro: these monsters never need two hands to wield a weapon.
-boots size macro
-Move horns/etc checks into helm_match macro
-Helm size fits macro to handle hats etc.
-Create an is_hat macro
-Redefine readable armor: if it has a ward, it's readable.
-Add a Water_res xhity compliant macro
-set_obj_shape: function to set an objects shape, replacing and unifying a bunch of copypasta. Returns true if the objects shape changed, false otherwise.
-improve drow house allied-ness and use in mm_grudge
-size_and_shape_to_fit function to centralize that process
-Switch how sound type is handled in sounds.c to be a bit less confusing to read.

Tweaks:
-Everything can wear waistcloths
-Resizing armor now cancels if no change is made (preserving the upgrade kit).
-Lolth has an 8-arm alternat attack
-Jewel wish/des file keyword for making valuable gems
-Fix injury word descriptions of healing spells when the target starts and ends on the same word.
-Slightly nerf drow hp/magic recover rates.
-Tame witches summon tame familliars, and a witch+familliar counts as 1 pet, not 2.
-Suicidal monsters leave themselves open to sneak attacks.

---
## [jandaX/android_kernel_xiaomi_joyeuse](https://github.com/jandaX/android_kernel_xiaomi_joyeuse)@[0fde86da7e...](https://github.com/jandaX/android_kernel_xiaomi_joyeuse/commit/0fde86da7e6568a6cb3f78de0139eb88da0fa14e)
#### Wednesday 2023-01-25 04:24:37 by Peter Zijlstra

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
Change-Id: Idd54334615da4c78698ca8b3b12b514ae9d8360f
Signed-off-by: Alexander Winkowski <dereference23@outlook.com>

---
## [deso-protocol/deso-workspace](https://github.com/deso-protocol/deso-workspace)@[8c68a8853b...](https://github.com/deso-protocol/deso-workspace/commit/8c68a8853b6141e932404cf12c979d641ad31a32)
#### Wednesday 2023-01-25 04:30:30 by Jackson Dean

feat: new identity desojs lib (#91)

What is supported in this MVP?
- login/logout
- generate jwt
- sign & submit transactions
- check current user permissions
- request approval for more permissions

TODO:
- encrypt/decrypt
- fix bugs

Why a new library? This library is intended to solve many of the issues
we have with the existing
[deso-protocol](https://github.com/deso-protocol/deso-workspace/tree/master/libs/deso-protocol)
library:

- `deso-protocol` manages signing by accessing a user's master key pair
via the identity [iframe
API](https://docs.deso.org/for-developers/identity/iframe-api/basics).
This requires users to enable access to third party cookies and local
storage on many browsers (Brave, Safari on IOS, Chrome in incognito
mode, etc).
- Since this library is based on derived keys, it does not need to use
the iframe API _at all_. We can sign transactions, encrypt, decrypt, and
generate signed JWTs directly using derived keys, which means this works
out of the box in pretty much any browser environment since it doesn't
rely on third party storage.
- `deso-protocol` tightly couples the broader api implementation with
the identity APIs, this creates a large API surface area with many
essential parts being neglected.
- The goal of this library is to decouple identity from the social api,
allowing developers to compose it with their own api implementations or
using a default implementation we will provide as a separate package
that depends on this one.
- `deso-protocol` requires developers to specify an "access level" when
logging in, and depending on the access level it can cause each
transaction to require explicit approval from users.
- Because we are using derived keys, there is no longer a need to
request an "access level" when users log into your app. Instead, you
request the specific permissions your app needs, when it needs them.
Once these permissions have been requested, you'll never need to ask
users to approve transactions going forward which makes it easier to
build better user experiences.
- `deso-protocol` depends on many node backend packages and requires
configuring your build system to include node polyfills.
- This library does not depend on any backend packages. Everything here
is browser friendly. Just npm install and use this immediately without
any awkward and confusing build errors or webpack configurations.
  - Because we don't need polyfills, the size of this library is tiny.

---
## [WillNilges/wraith-hunt](https://github.com/WillNilges/wraith-hunt)@[a697a24125...](https://github.com/WillNilges/wraith-hunt/commit/a697a24125adb25d03962c045155bffc177c39a6)
#### Wednesday 2023-01-25 05:49:54 by Willard Nilges

Rip out as much kludge as I can

and break everything in the process

Need to figure out why the blocks look like that and also re-write my
whole map class.

Oh also yeet this camera into the sun and re-do all my shit boy howdy
what the fuck was I thinking

There has GOT to be a better way

---
## [DannyBoy3642/tgstation](https://github.com/DannyBoy3642/tgstation)@[5e80257423...](https://github.com/DannyBoy3642/tgstation/commit/5e802574231c9c6fe835c40b55f2c8aa9f1c68b4)
#### Wednesday 2023-01-25 05:57:03 by Jeremiah

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
## [3ndher/__LifeRepo](https://github.com/3ndher/__LifeRepo)@[ef2cfd729a...](https://github.com/3ndher/__LifeRepo/commit/ef2cfd729a535eed05fc7e7e93a7942e0950e9bf)
#### Wednesday 2023-01-25 07:58:45 by 3ndher

Suicide talk to new girlfriend

About river. Not telling how she died with me there or how i blamed another friend for the whole thing. That comes later.  But i know she’s alive somewhere. And i will keep working to find her.

---
## [Roadhog360/Et-Futurum-Requiem](https://github.com/Roadhog360/Et-Futurum-Requiem)@[dc506a9fe1...](https://github.com/Roadhog360/Et-Futurum-Requiem/commit/dc506a9fe1c1448eaec73af46604a68fc52af553)
#### Wednesday 2023-01-25 08:08:56 by Roadhog360

Thanks Eclipse for not saving this

Seriously getting sick of Eclipse's "save undo" horse shit
Might switch to IntelliJ because I keep saving in Eclipse only to go back to see it DIDN"T save and I have to save the same fucking changes again for them to apply and make these stupid micro-commits to push stuff that should have already been fucking pushed

---
## [swarm-game/swarm](https://github.com/swarm-game/swarm)@[46d7c968cc...](https://github.com/swarm-game/swarm/commit/46d7c968cc69e5c6057c495659c7e2b23fab1c27)
#### Wednesday 2023-01-25 08:25:15 by Brent Yorgey

Add `GPS receiver` device to provide `senseloc` capability (#956)

Add a new `GPS receiver` device which enables the `senseloc` capability (and hence the `whereami` command).  Towards #26 .

- My immediate motivation is that I want to be able to define `excursion : cmd unit -> cmd unit` which executes the given command and then returns to the same location and orientation as before.  Being able to use the `whereami` command is one of the last missing pieces of machinery necessary to be able to do this in classic mode (the other is a `heading` command, see #955).
- The proposed recipe for `GPS receiver` is `antenna + circuit + clock + compass`, which is a somewhat difficult recipe (`antenna` requires `silver` which requires a `deep mine`; a `clock` requires `quartz` + a bunch of `iron gears`, etc.).  One might wonder whether we should make the recipe easier since finding out where you are seems like a kind of fundamental operation.  However, consider that in order to even be able to make use of the result of `whereami` you need at least (1) an `ADT calculator` to deal with the pair (which transitively requires `typewriter` -> `circuit` -> `silicon` -> `quartz`) (2) probably things like `comparator` and `calculator` to do anything useful with the coordinates.  By the time you have those things you can definitely already build `circuit` + `clock` + `compass`, and you're probably not that far away from getting some `silver` for an `antenna`.  Also, in practice it's an interesting/fun constraint to build up machinery that has to work entirely based on *relative* position without being able to find out your absolute coordinates.
- For some reason this is causing `Testing/508-capability-subset` to fail.  I think perhaps it is due to #397 ?  I will investigate. *EDIT*: unfortunately, that wasn't it!

---
## [Prashant-1695/kernel_xiaomi_lavender-4.19](https://github.com/Prashant-1695/kernel_xiaomi_lavender-4.19)@[d19ed66314...](https://github.com/Prashant-1695/kernel_xiaomi_lavender-4.19/commit/d19ed66314355cf5c947f1fcbdafa37159523ca2)
#### Wednesday 2023-01-25 10:01:20 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>
Signed-off-by: pix106 <sbordenave@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>
Signed-off-by: ImPrashantt <prashant33968@gmail.com>

---
## [macladson/lighthouse](https://github.com/macladson/lighthouse)@[66eca1a882...](https://github.com/macladson/lighthouse/commit/66eca1a88218462235cb76a116dc3c6a1853444f)
#### Wednesday 2023-01-25 10:01:23 by Michael Sproul

Refactor op pool for speed and correctness (#3312)

## Proposed Changes

This PR has two aims: to speed up attestation packing in the op pool, and to fix bugs in the verification of attester slashings, proposer slashings and voluntary exits. The changes are bundled into a single database schema upgrade (v12).

Attestation packing is sped up by removing several inefficiencies: 

- No more recalculation of `attesting_indices` during packing.
- No (unnecessary) examination of the `ParticipationFlags`: a bitfield suffices. See `RewardCache`.
- No re-checking of attestation validity during packing: the `AttestationMap` provides attestations which are "correct by construction" (I have checked this using Hydra).
- No SSZ re-serialization for the clunky `AttestationId` type (it can be removed in a future release).

So far the speed-up seems to be roughly 2-10x, from 500ms down to 50-100ms.

Verification of attester slashings, proposer slashings and voluntary exits is fixed by:

- Tracking the `ForkVersion`s that were used to verify each message inside the `SigVerifiedOp`. This allows us to quickly re-verify that they match the head state's opinion of what the `ForkVersion` should be at the epoch(s) relevant to the message.
- Storing the `SigVerifiedOp` on disk rather than the raw operation. This allows us to continue track the fork versions after a reboot.

This is mostly contained in this commit 52bb1840ae5c4356a8fc3a51e5df23ed65ed2c7f.

## Additional Info

The schema upgrade uses the justified state to re-verify attestations and compute `attesting_indices` for them. It will drop any attestations that fail to verify, by the logic that attestations are most valuable in the few slots after they're observed, and are probably stale and useless by the time a node restarts. Exits and proposer slashings and similarly re-verified to obtain `SigVerifiedOp`s.

This PR contains a runtime killswitch `--paranoid-block-proposal` which opts out of all the optimisations in favour of closely verifying every included message. Although I'm quite sure that the optimisations are correct this flag could be useful in the event of an unforeseen emergency.

Finally, you might notice that the `RewardCache` appears quite useless in its current form because it is only updated on the hot-path immediately before proposal. My hope is that in future we can shift calls to `RewardCache::update` into the background, e.g. while performing the state advance. It is also forward-looking to `tree-states` compatibility, where iterating and indexing `state.{previous,current}_epoch_participation` is expensive and needs to be minimised.

---
## [tadas-s/exercism](https://github.com/tadas-s/exercism)@[934130d243...](https://github.com/tadas-s/exercism/commit/934130d243aa0e738c73c8fdb42ab1887a594594)
#### Wednesday 2023-01-25 10:47:08 by Tadas Sasnauskas

rust: scale-generator solution

Sort of mostly brute forced solution, i.e. I do not get the "domain" / music
theory behind this scale generation.

It also looks kinda ugly because test suite suggested structure has 'enumerate'
method which prevents me from implementing iterator trait directly on Scale
structure.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[c3d0f6016b...](https://github.com/mrakgr/The-Spiral-Language/commit/c3d0f6016bd82fb2e2225e6fb707782852c7204c)
#### Wednesday 2023-01-25 12:04:20 by Marko Grdinić

"https://news.ycombinator.com/item?id=34502566
Ask HN: What is the weirdest or most surreal recent technology you have seen?

> If you're not in the bio field, you may not be aware just how routine genetic modification has become. For the larger companies, projects can involve thousands of different iterations on DNA sequences, all of which are created, put in a cell, grown, sequenced, and analyzed. It's absolutely routine at this point - it's not a science or even engineering challenge project it's an operations project.

1/25/2023

9:55am. First of all, let me post a comment on RR.

///

I have about 115k words more on my Patreon, but as I am in the middle of a job search, I am going to pause publishing on Royal Road for the time being in order to relieve the pressure on me. Whereas before I had no trouble writing over 2k words a day, right now I find my time and attention taken up by other things. My priority isn't to entertain you fine people on RR for free, and I'll like to encourage more people to subscribe to my Patreon. If you've liked this kind of story so far, why not consider subscribing?

Personally, I want to put my money where my mouth is, and recently I got info that Tenstorrent should open source their SDK and allow the general public to program their chips in six month. So I want to be able to actually afford those devices when they come out. Hence the recent scramble to get a job. It is really a pity that art and writing can't support my ambitions, but that is life. Who can do what he wants in this world?

Besides that, my talking skills are really lacking so I am considering opening a Youtube channel on staged functional programming in Spiral in order to practice them. We'll see how things go. I'll try to write a little bit of Heaven's Key every day, but until I find my way I will be branching out.

///

Done. Any mail? Surprisingly no. Let me check my applications on AngelList. I have a couple of rejects, but most are pending.

Let me check the Reddit thread.

https://www.reddit.com/r/fsharp/comments/10k2sou/where_do_i_find_f_remote_jobs/

Not much help here. I'll probably have to write F# off as a tool for helping me get a job.

10:20am. Ok, since things are like this, let me start that Youtube channel. Currently, this is my third application round. The previous ones were in 2021 and late 2022. There are 3 aspects that I need to improve upon myself to get any kind of job.

* The talking aspect. I need to learn to project confidence face to face. This is the main purpose behind me opening the Youtube channel. I am going to have to learn to use my mouth.
* All those technologies used at the startups. Nobody is using what I have on my resume, and I am going to have to go through the job postings and read the documentation and watch the Youtube tutorials for all these things.
* Some practical experience doing assignments for others. If the feedback I am getting is just too poor, I guess I'll move to freelancing and do work for pennies. This should also serve to motivate me to master all those technologies needed at startups.

After I go through that gauntlet, me being a hobbyist won't matter as I'll just be able to make stuff up on my resume and grease my way forward.

For now, it wouldn't really be that bad if I spent a month just making Youtube vids while applying on the side. I'll see how things go.

10:35am. Anyway, I think the lesson from this is that Reddit and Twitter are the wrong places to look for a job. We'll see.

Now where do I start. First of all, how I watch a video on making Youtube videos.

https://youtu.be/foYyeGLf9yU
How to Make A YouTube Video for Beginners START to FINISH!

This is two hours. Show me your wisdom, Youtube guy.

10:40am. This is going to take a while. During my first round of application back in 2021, I think I got only a 10% approval rate during the initial stage. Who knows how it will be on AngelList. Either way, I can expect this job search to last a while.

https://youtu.be/foYyeGLf9yU?t=283

This is too fancy for me.

I'll leave it for later. It doesn't matter if my video quality is crappy at the start.

What I need are 3 things:

* Get used to talking.
* Get used to editing video.
* Find out how to get screen capture.

I am not interested in a 1k gear.

My first goal is produce a couple of hours of videos and see how it goes from there. If I can refine this.

https://youtu.be/vh7G5raH7ZI
24 Best Niches to Make Money on YouTube Without Showing Your Face

I hadn't thought about this. If I want to learn to run my mouth, I do not really need to show my face.

https://youtu.be/vh7G5raH7ZI?t=249
> That's great Mat, but how much could they actually be making?

https://youtu.be/vh7G5raH7ZI?t=291
> 35k dolalrs

For 2.3m vies a month? Whoa!

https://youtu.be/vh7G5raH7ZI?t=338

Hitfilm Express. This is a really good video.

https://youtu.be/vh7G5raH7ZI?t=437

Yeah, let's aim for this for now. I'll just have to figure out how to screencast.

https://youtu.be/vh7G5raH7ZI?t=552
> It hasn't uploaded for an entire year, but the channel still pulls in 700k views per month.

https://youtu.be/vh7G5raH7ZI?t=777

This is what my niche should be.

11:05am. Yeah, why don't I do it like this? I'll cultivate my skills and instead of just writing in the Spiral repo, why don't I make videos?

https://youtu.be/vh7G5raH7ZI?t=991

Ohhh! What is the secret!? What is the secret!!?

https://youtu.be/D-xgP6hZtwI
How to Grow Your Channel FAST With This Secret | Get More Views and Subscribers on YouTube

https://youtu.be/D-xgP6hZtwI?t=107
> Set group of tags that you put on every video.

I should make some videos on how to illustrate a webnovel and things like that.

https://youtu.be/D-xgP6hZtwI?t=149

Let me just pause a bit. I am into this now.

You never really know where life will lead you. I never thought of making Youtube videos before today. But it is not like I don't have valuable knowledge to share. And I've been stuggling to get even up to 100$ month so far.

Imagine I did a series on how to illustrate a webnovel. I think that would get some views.

I could do a channel covering various stable diffusion models. That could get a lot of views.

11:50am. Had to take a break. Honestly, this fired my imagination. My intention was to do Spiral vids, but I can tell already that if I did a tutorial series on using stable diffusion, I'd get a ton more views. Since doing a series on Spiral is not that important to me, the talking practice is, I should instead do a series on SD.

Imagine if the series goes viral and I get millions of views? That by itself could resolve all my money woes!

It would be extremely cheap to find success like this, but this is the best single possible move I can make here. I know I can't live making art, but teaching others how to do it? Why not.

And unlike regular art, teaching people how to do AI generated art should be quite effective.

Let me watch the rest of that video.

https://youtu.be/D-xgP6hZtwI?t=237
> Saturation up to a certain point can be a good thing.

https://youtu.be/s9C7sHQu5l8
Make Money on YouTube Without Making Videos (Full Guide)

Let me watch this as well.

https://youtu.be/GMBAKvAT3po
Make Money on YouTube Without Making Videos (Free Course)

Let me watch this first.

https://youtu.be/GMBAKvAT3po?t=110

Listening to this guy is making me realize I am not that smart. Here I am strugging so much to even make 5$/month, but he found a simple strategy to make thousands. Forget the camera, but if I need a better mike I am sure my father can find something for me.

https://youtu.be/GMBAKvAT3po?t=142
> If you include all of my income sources from Youtube, I make over a 100k dollars per month.

https://youtu.be/GMBAKvAT3po?t=313
> Imagine you just had one niche Youtube channel and made an extra 3,000$/month. How would that change your life? Would you quit your job?

Yeah, I wouldn't need a job in that case. Forget programming, I'll first focus on making an AI art channel.

https://youtu.be/s9C7sHQu5l8?t=240

It is important to follow the anatomy that almost all viral videos have.

https://youtu.be/s9C7sHQu5l8?t=449
> Translated version of your own channel

https://youtu.be/ZImFSMIILsk
6 Ways of Monetizing Your YouTube Channel to Make Money Without Making Videos

Here is the next in the series.

https://youtu.be/ZImFSMIILsk?t=80

I didn't know this.

https://youtu.be/ZImFSMIILsk?t=198

I use an ad blocker so I never see them. I guess I'll have to think about it.

https://youtu.be/ZImFSMIILsk?t=521
> Even if it does not have a great CPM, a lot of these channels can make 10,20 thousand dollars per month.

I am not sure how things will go, but these are the kinds of skills I should be exercising. I already have 6.5 years of programming experience, so doing even more programming is not going to help me get hired or make money. But why not become a guru. If I have to come out of my shell, why not go this route?

Do I particularly want to get a job? No, not really.

It is just the only choice as far I can see, but this is in fact the natural extension of my path as an artist. Right now I have good abilities for making use of AI generated art. I have a lot of skills which I could use to make educational videos about. It is better to do this than waste time.

https://youtu.be/ZImFSMIILsk?t=582
> Bad ways of monetizing your channel
> Merch

https://youtu.be/ZImFSMIILsk?t=609
> Memberships

This is exactly what I am trying to do with Patreon.

He literally mentions it as a bad way a second later!

https://youtu.be/ZImFSMIILsk?t=639
> And you'll see a lot of channels that are really big with millions of subscribers start Patreons, and you go to them and the channel's making like a 100$ a month or something like that from it.

https://youtu.be/ByaM2d4AE1Q
Tube Mastery & Monetization and Tube Coaching Q&A

I'll watch this later, let me stop here for breakfast. I need to do the chores as well. Is this real, is this not, who knows? So far, the advice I've been given seems sound.

I absolutely won't get anywhere with Patreon. Even if all the followers subscribed on RR, I'd get a pittance. But there should be a lot of people interested in AI art like myself, and I could build a channel showing them the ropes.

This would be really in line with my interests too.

I'd get money, do cool art, improve both my art and talking skills, and put my programming abilities as they are to good use.

I am never going to get big money anyway unless I learn how to advertize and market myself properly. My AI art skills are one thing that could sell."

---
## [totalspectrum/spin2cpp](https://github.com/totalspectrum/spin2cpp)@[903c71ebd8...](https://github.com/totalspectrum/spin2cpp/commit/903c71ebd887b231162a579d1bd0b13a7445c7fa)
#### Wednesday 2023-01-25 13:24:49 by Ada Gottensträter

Merge branch 'W21-fix-stupid-fucking-bullshit' into W21-refactor-lblaux

---
## [sabriunal/eartag](https://github.com/sabriunal/eartag)@[aa2d3d4dc4...](https://github.com/sabriunal/eartag/commit/aa2d3d4dc4550c9c675c4bfbcd697c652c25ce86)
#### Wednesday 2023-01-25 13:29:25 by knuxify

meta: revise project description

This description was written back when Ear Tag was initially made.
Back then, it was only able to open one file at a time, and that was
its primary purpose. I made it as a quick tool as I was frustrated with
existing ones (and Picard was crashing my entire DE session - a problem
I did not feel like debugging).

Needless to say, things have changed quite a bit since then. Ear Tag
has gained quite a few new features, and I think it's now become suited
for managing not just singular files, but maybe even small libraries.

This extremely-awkward text has been pasted into various places that
needed a description for the program (thanks for the shoutout, OMG!
Ubuntu!), and it's been giving me second-hand embarrasment. Or maybe
first-hand embarrasment. I was the one who wrote it after all. So,
I decided to fix it. This should hopefully be better (and the new
short description actually follows GNOME's app summary guidelines now).

If I'm already typing out this incredibly long, sentimental and frankly
quite pointless commit message, I'd like to take a moment to apologize
to the creator of Tagger, another libadwaita audio tagging app. I was
completely unaware of its existence when I started working on Ear Tag.
I've seen a few folks confuse the two... sorry about that. Not that
you're ever going to read this anyways. Keep up the good work! I'm
seriously impressed by the double GTK-WinUI sorcery you're doing with
Denaro/Money. It's easily one of the coolest software tricks I've
*ever* seen. And I'm not being smug or ironic here.

---
## [sammmhodge/AlienPowerWash](https://github.com/sammmhodge/AlienPowerWash)@[98babb028d...](https://github.com/sammmhodge/AlienPowerWash/commit/98babb028d2646a35fdc8d81045935a8d49b81af)
#### Wednesday 2023-01-25 13:51:55 by daddyihaveacatt

im better than everyone the god complex has kicked in

[Fergie:]
La la la la la la

[Will.I.am:]
Hey mama, this that shit that make you move, mama
Get on the floor and move your booty, mama
We the blast masters, blastin' up the jamma
(REEEEEEEWIIIIIIND)

[Tippa Irie:]
Cutie cutie, make sure you move your booty
Shake that thing like we in the city of sin, and
Hey shorty, I know you wanna party
The way your body look really make me feel naughty
Cutie cutie, make sure you move your booty
Shake that thing like we in the city of sin, and
Hey shorty, I know you wanna party
And the way your body lookin', really make me feel naughty

[Will.I.am:]
I got a naughty naughty style and a naughty naughty crew
But everything I do, I do just for you
I'm a little bit of old, and a little bit of new
The true niggas know that the Peas come through
We never cease (No), we never die, no we never deceased (No)
We multiply like we mathematise
And then drop bombs like we in the Middle East
(The bomb bomba's, the base boom dramas)

Now y'all know, who we are
Y'all know, we the stars
Steady rockin' on y'alls boulevards
And, lookin' hard without bodyguards
(I do) what I can
(W)ill-I-am
And still I stand, with still mic in hand
(So come on mama, dance to the drama)

Hey mama, this that shit that make you groove, mama
(Hey) Get on the floor and move your booty mama
(Yaw) We the blast mastas blastin' up the jamma
(Hey) So shake your bambama, come on now mama
This that shit that make you groove, mama
(Hey) Get on the floor and move your booty mama
(Yaw) We the blast mastas blastin' up the jamma (Whoa)
(La la la la la)

We the big town stumpas, and big sound pumpas
The beat bump bumps in your trunk trunkas
The girlies in the club got the plump plump plumpas
And when I'm makin' love, my hip hump humps
It never quits (No), we need to carry nine millimeter clips (No)
Don't wanna squeeze trigger, just wanna squeeze tits
(Lova, lova) 'cause we the show stoppas
And the chief rockas, number one chief rockas

[Will.I.am & Fergie:]
Now y'all know (Who we are)
Y'all know (We the stars)
(Steady rockin' on y'alls boulevard)
How we rockin' it girl (Without bodyguards)
She be (Fergie)
From the crew (BEP)
(Come and take heed, as we take the lead)
(So come on bubba, dance to the drummer)

[Will.I.am:]
Hey mama, this that shit that make you groove, mama
(Hey) Get on the floor and move your booty mama
(Yaw) We the blast mastas blastin' up the jamma (Naw, nawy)

[Tippa Irie:]
Cutie cutie, make sure you move your booty
Shake that thing like we in the city of sin, and
Hey shorty, I know you wanna party
The way your body look really make me feel naughty

[Tippa Irie (will.I.am):]
But the race is not, for the swift
But who really can, take control of it
And Tippa Irie and the Black Eyed Peas
Will be there
('Til infinity, 'til infinity, 'til infinity, 'til infinity, 'til infinity, 'til infinity)
Tippa is out

[Tippa Irie:]
Kcohs a med a ffun, nuff a dem a shock
Nuff a dem a shock, nuff a dem a sting
Every time you see dem appear bling bling
Oh what a ting! Pure modeling
Grinding, and winding
And the madda dem a move inna perfect timing
Dem a dance and dance to di dancehall riddim
And di way di tune nice, it finga-licking
Like rice and peas and chicken stuffing

[Will.I.am:]
Hey mama, this that shit that make you groove, mama
(Hey) get on the floor and move your booty mama
(Yaw) We the blast mastas blastin' up the jamma
(Hey) So shake your bambama, come on now mama
This that shit that make you groove, mama
(Hey) Get on the floor and move your booty mama
(Yaw) We the blast mastas blastin' up the jamma (Whoa)
(La la la la la)

---
## [apify/crawlee](https://github.com/apify/crawlee)@[a95e6676b2...](https://github.com/apify/crawlee/commit/a95e6676b2e3574c8db3083c661dc09a5405751e)
#### Wednesday 2023-01-25 14:28:46 by Martin Adámek

chore: switch to yarn v3 (#1752)

NPM got somehow [broken more than
usual](https://github.com/apify/crawlee/actions/runs/3997285915/jobs/6873858419)
and its no longer possible to install the dependencies in CI. We were
struggling with NPM for quite some time (especially after we moved to
turborepo). I’ve been advocating for yarn since my first days here, been
using it for last ~5 years on a daily basis and it never did anything
wrong to me, so I hope this will be the right step and a smooth
transition for all the collaborators.

What to expect? Since we require node 16, we can leverage `corepack`, a
new tool shipped with newer node versions (btw developed by yarn
maintainers). This means you just need to run `corepack enable` and yarn
should be available in your workspace. In case of some problems, you can
try running `corepack prepare yarn@stable --activate`, but it shouldn’t
be needed. Note that we use `corepack` instead of commiting yarn binary
to the git repo - that is the reason why `.yarn` folder is gitignored.

Initially we will start with a conservative setup, using a node linker,
so there will be the good `node_modules` folder we are all used to. I’d
like to experiment with the advanced features as well, mainly in the
project templates, as it could greatly improve the build times (we could
even skip the install step completely).

With that said, we will be still using NPM inside our E2E tests, to be
sure the project can be safely installed with NPM. This change should
affect only the collaborators, not our users. Ideally we should test
other package managers via CI too, so we are sure `pnpm` works as well,
or maybe even `bun`.

Few API differences and quality of life improvements yarn brings:
* `npm install` -> `yarn`
* `npm install xxx` -> `yarn add xxx`
* `npm run ...` -> `yarn …`
* `npx …` -> `yarn …`
* no need to deal with the `--` issue from `npm run` (propagating CLI
params to the script)
* powerful caching and _sane_ lockfile format

---
## [igneous-labs/telegram-space](https://github.com/igneous-labs/telegram-space)@[87f0dedca9...](https://github.com/igneous-labs/telegram-space/commit/87f0dedca99269b08f7fc828f5d7b66c68351ee6)
#### Wednesday 2023-01-25 14:33:03 by Jesse Y. Cho

wip: [server] impl godot binary serialization API in server, temporary multithreading for world state syncing

 - With godot doc being sparse it was painful to reverse engineer but major
    stuff now can be serialized and deserialized from rust.
 - Can't do f32 yet (found out that it had p major error) so fuking Vector2 is
   a big fucking headache right now, but we'll worry about that later
 - We'll do message passing concurrency to construct Listener, StateService, Sender
 - But for now, for testing, we'll just do good ol' Resource sharing
   Arc<Mutex> mutithreading, good enough for now

---
## [Dr-Pope/tgstation](https://github.com/Dr-Pope/tgstation)@[6dd4839ef3...](https://github.com/Dr-Pope/tgstation/commit/6dd4839ef321aa0a997549d1ae07fe7ccbba59ed)
#### Wednesday 2023-01-25 14:46:31 by carshalash

Gatfruit will no longer drop from ice portals. (#72048)

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

---
## [Dr-Pope/tgstation](https://github.com/Dr-Pope/tgstation)@[00e7d5d746...](https://github.com/Dr-Pope/tgstation/commit/00e7d5d7465211ccf0e3d604e566e2c08775cd20)
#### Wednesday 2023-01-25 14:46:31 by GoldenAlpharex

*hand, or That /One/ Emote You Always Felt Was Missing (#71600)

## About The Pull Request
It's happened to me _repeatedly_ that I'd see someone down on the floor,
and wanted to just, give them a hand, so they could take it and get up
that way, without just, directly clicking on them, since that's a little
bland. I've also wanted to just, offer my hand to someone so they could
grab it, so that I could pull them alongside me, rather than just
targeting one of their arms and ctrl-clicking them.

I've had this idea for a _long_ time, and only just decided to do this
today.

Now, I know what you might say. "Golden, that's a lot of code for
something this simple!" You're not wrong. _However_. I decided to go
along and to give some more love to the `/datum/status_effect/offering`
status effect and the offering-related alerts, to make them a lot more
versatile and a lot less hardcoded. Hence the whole "refactoring" part
of this.

Of course, when I add something, I don't do it half-way. So, the way the
emote works is much like the `*slap` emote, except that:

- When you click on someone, it does the exact same as if you were
offering the item to them, except that it's targeted (much like
ctrl-shift-click).
- If there's nobody directly adjacent to you, it won't do anything.
- If there's at least one person lying down around you, you will offer
them your help to get up. Should they take your hand and let you help
them up, you will both receive a simple memory about being helped up (or
helping up), as well as a 45-seconds-long small mood buff, because it
feels nice to be on either end of such a friendly gesture. If they get
up, they automatically get disqualified from being offered some help
standing up, and likewise, if you lie down, that offer goes away as
well.
- If there's at least one person around you, you will instead extend
your hand in their direction, for them to grab onto it. Should they do
so, you will then grab them by their arms and pull them.

I reworked the offering status effect to no longer have a hardcoded
`can_hold_items()` check, so that kisses and the hand offering would no
longer need you to have free hands to complete. The logic here is that
you can still pull someone even with both hands filled, so I figured I'd
leave it this way.

Note: If anyone would like to give the item a better sprite, by all
means, go ahead, that'd be amazing. I'm just not really a great spriter
and couldn't be bothered to waste hours making a very _meh_ hand.

## Why It's Good For The Game
It's fluff, and nice fluff at that. It makes it easier for people to be
nice to one-another without having to necessarily spend so long writing
up an emote that the person on the floor will already have gotten back
up. I'm sure the MRP folks will like it, and I'm certain the HRP
downstreams will love it too ;)

## Changelog

:cl:
add: Added the *hand emote, which you can offer to someone standing up
in order to give them the possibility to grab onto your hand and let you
drag them away, or to someone lying down to help them back up, which
always makes everyone involved a little happier!
refactor: De-hardcoded and genericized a lot of the offering status
effect and alert code, to make it require a lot less copy-paste to
handle new cases.
fix: Offering a kiss no longer requires the receiver to have free hands
to accept said kiss!
/:cl:

---
## [CDCgov/prime-reportstream](https://github.com/CDCgov/prime-reportstream)@[2513f9d426...](https://github.com/CDCgov/prime-reportstream/commit/2513f9d4265bcb2fb551f82b00790d1f8d413d40)
#### Wednesday 2023-01-25 15:48:11 by Stephen Kao

Experience-7891: Disable organization-specific fetches as admin

This changeset disables a few Organization-specific requests to mitigate the number of 404s we're getting as admins try to fetch Organization resources:
- Organization settings
- Deliveries
- Submissions

There's not a one-size-fits-all solution here given the different fetch mechanisms we already have and how the data is rendered, so I tried to add minimal changes to prevent disrupting anything down the line.  I think going forward, we can make a generic `useOrganizationQuery` hook that'll automatically be disabled if the user is logged in as an admin without impersonating an Organization.  There are a lot of layers with our fetching that in my opinion should be untangled, but that's out of the scope of this pull request.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[1f4934ac2b...](https://github.com/treckstar/yolo-octo-hipster/commit/1f4934ac2b7fca538af48c6f2cf222fdfac4903b)
#### Wednesday 2023-01-25 16:22:05 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [lfd/jailhouse](https://github.com/lfd/jailhouse)@[477da77690...](https://github.com/lfd/jailhouse/commit/477da776901011e8cf611a113420af87af10e562)
#### Wednesday 2023-01-25 16:37:48 by Ralf Ramsauer

hypervisor: riscv: add SSTC support

SSTC (Supervisor-level timecmp) is an extension to bypass SBI calls to
control the platform's timer. If SSTC is available, the supervisor can
directly write the next timeout into the stimecmp CSR, instead of
conducting a SBI call. Furthermore, platform timer IRQs will directly
arrive at S-Mode resp. VS-Mode w/o M-Mode reinjection, which saves time
up on timer arrivals.

SSTC supports virtualisation: VS-Mode's stimecmp is shadowed by
vstimecmp. This means, if SSTC is available, we can save up to two
context switches for arming timers.

So we have drastically fewer exits with SSTC.

Linux (since v6.0) will discover and enable SSTC during the
initialisation of the platform timer, and from then on use the stimecmp
CSR for arming the timer instead of calling SBI. Actually pretty easy.

Some important notes of the specification [1]:

  - Discovery of SSTC is done via misa CSR, or via device tree

  - Spec says that the S-Mode hypervisor should write to vstimecmp if
    the VS_Mode guest decides to csr_write(stimecmp), as this saves a
    detour through SBI.

  - However, SBI calls are of course still supported

My thoughts:

When initialising Jailhouse, we're not allowed to query misa. Further,
we don't have the device tree available. Now we could either pass the
availability of SSTC via the driver (Linux already did discovery for
us), or hard code it in the system configuration. Ugly, both. But can we
avoid discovery?

If SSTC is available, Linux will simply make use of it.
If SSTC is not available, then Linux won't use the stimecmp CSR.

So just enable SSTC in HENVCFG, even if it is not available: It won't
affect anything, it's just ignored.

Last, spec says that if SSTC is available, an 'old-school' OpenSBI timer
set by a VS-Mode guest should take the vstimecmp fast-path in HS-Mode.
We could do this in Jailhouse, but then we must be sure, if SSTC is
*really* available.

As no guest should use the OpenSBI interface when SSTC is available,
simply take the SBI detour on those platforms. We're doomed in those
cases anyway.

Let's not implement SSTC discovery for the moment.

[1] https://drive.google.com/file/d/1f4DyxZMzl3yH7KGKXJFZ_iUY_AU9az_K/view

Signed-off-by: Ralf Ramsauer <ralf.ramsauer@oth-regensburg.de>

---
## [fnkzhang/ECS150Project1](https://github.com/fnkzhang/ECS150Project1)@[397bec88ba...](https://github.com/fnkzhang/ECS150Project1/commit/397bec88babd6aa794ac669cba1bcf5212d0af49)
#### Wednesday 2023-01-25 16:40:24 by Minh Pham

Update sshell.c

I have read it carefully and am satisfied with the layout presented in phases. This is important for the reader so that they can easily follow and evaluate the problem-solving process. Layout from Buildin cmd -> output redirectory -> pipeline cmd (this part is the most difficult and also the most important). According to the few attribution structures I know of, the most important part comes first because the reader can evaluate it as quickly and efficiently as possible. We can present the layout from Pipeline -> output redirectory -> buildin cmd -> test(). Those are personal thoughts and opinions, what do you think about this? The rest I want to mention is that we should clarify some of the ambiguous numbers like 37, 47, and 16. Readers will not understand the meaning and role of these numbers in the program. Ex: token_lenth_max = 16;

In general, the split layout is very logical and splits into many small branches to solve and add functionality to them. I think this is fine and not necessarily changeable or optimal.

I have read it carefully and am satisfied with the layout presented in phases. This is important for the reader so that they can easily follow and evaluate the problem-solving process. Layout from Buildin cmd -> output redirectory -> pipeline cmd (this part is the most difficult and also the most important). According to the few attribution structures I know of, the most important part comes first because the reader can evaluate it as quickly and efficiently as possible. We can present the layout from Pipeline -> output redirectory -> buildin cmd -> test(). Those are personal thoughts and opinions, what do you think about this? The rest I want to mention is that we should clarify some of the ambiguous numbers like 37, 47, and 16. Readers will not understand the meaning and role of these numbers in the program. Ex: token_lenth_max = 16;

In general, the split layout is very logical and splits into many small branches to solve and add functionality to them. I think this is fine and not necessarily changeable or optimal.

Let me know some of your ideas. For me, if I were to stand as a casual reader, I would still understand the problem-solving process of the project without testing. And I think this will also convince Prof. 

Thanks!

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[10a344bde0...](https://github.com/tgstation/tgstation/commit/10a344bde0d48fb250dcb7a9eb4a1e98b9bb6df5)
#### Wednesday 2023-01-25 16:56:16 by Time-Green

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
## [vinylspiders/Skyrat-customization-expansion](https://github.com/vinylspiders/Skyrat-customization-expansion)@[a57b142c1a...](https://github.com/vinylspiders/Skyrat-customization-expansion/commit/a57b142c1a4949ded1dcde1157ccf789fb21aabd)
#### Wednesday 2023-01-25 17:53:18 by SkyratBot

[MIRROR] Basic mobs don't become dense upon death [MDB IGNORE] (#18679)

* Basic mobs don't become dense upon death (#72554)

## About The Pull Request

In #72260 what was previously a var became a flag, which was a sensible
change, however this inverted the default behaviour.
In virtually all cases we want dead mobs to _stop_ being dense, this
added a requirement for the flag to be present for that to happen and
then didn't add the flag to any mobs.

Rather than add this to every mob I inverted the function of the flag.
My reasoning here is that _simple_ mobs seemingly never required this
behaviour, basic mobs are probably going to need it rarely if ever, and
including it in `basic_mob_flags` by default seems messy and easy to
leave off when setting other flags (plus #72524 implies to me we want to
avoid adding more default values).

Setting this manually on each mob seems kind of silly as a requirement
going forward and I can't think of a way we'd unit test for people
forgetting.

For the same reason I did the same thing with the
`STOP_ACTING_WHILE_DEAD` flag I added to the AI controller in a recent
PR, the flag should denote unusual behaviour not the default.

## Why It's Good For The Game

It looks really odd when you're constantly shuffling places with dead
mobs, they're not supposed to do that.
It's tedious to add `STOP_ACTING_WHILE_DEAD` to every AI controller when
that should be an obvious default assumption.

## Changelog

:cl:
fix: Dead basic mobs are no longer "dense" objects and can be stepped
on.
/:cl:

* Basic mobs don't become dense upon death

* Removes a flag we didn't need anymore.

* Forgot to remove this one

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[e687bb26ad...](https://github.com/mrakgr/The-Spiral-Language/commit/e687bb26ada41f008424d7720e594eb404759c1c)
#### Wednesday 2023-01-25 18:17:54 by Marko Grdinić

"1:55pm. I actually got a PM from that Reddit thread, but for that job I'd need to move to Austria. It is close to Croatia, but I can't go from being a shutin to a globe trotter just like that.

///

It is not absolutely out of the question, but unless personal circumstances forced me, I am not willing to relocate. I've just been applying two days thus far, so I'll see how things go for now. Thank you for reaching out to me. I'll keep your offer in mind.

///

https://www.reddit.com/r/fsharp/comments/10k2sou/where_do_i_find_f_remote_jobs/

It is this thread. If this was a remote job offer, I'd probably just have gone for it right off the bat.

I appreciate Kit Eason telling me I have an impressive resume. I am insecure about that.

Anyway, let me watch that tube mastery video. Let me just finish the Otome Survival chapter first.

https://youtu.be/ByaM2d4AE1Q?t=111

How long is this guy going to hawk his course? I wonder if I could pirate his vids.

https://go.mattpar.com/tube-mastery-sts

Lol, it costs 1k dolalrs. Definitely pirating this.

https://courseleak.com/matt-par-tube-mastery-and-monetization-3-0/

I am looking at this site and wondering where the links are supposed to be.

https://courseleak.com/about/

2:25pm. I can't find it. The few links there were out there in the major search engines have been taken down. I'd need to find a site like cgpersia except for marketing. It took me a long time to find a source for CG courses, and I do not want to spend too much time looking to pirate marketing content.

https://youtu.be/ByaM2d4AE1Q

Let me just watch this and I will leave it aside in order to start my own thing.

2:40pm. If nothing else, getting that course so I can see how he makes videos would be useful, but nevermind that for now.

Forget courses. Forget tutorials. What is the most important is that I start making content.

https://youtu.be/vh7G5raH7ZI?t=338

Here he was talking about free video editing software.

https://fxhome.com/product/hitfilm
https://www.openshot.org/download/
https://shotcut.org/

Here are the 3 programs he namedropped. I know Blender has video editing abilities. I also have Nuke. And I bet I could find commercial software for this purpose on CGPersia.

2:55pm. Now what I need to cultivate is an interest in video editing. It isn't too complex. Let me look for some video editing tutorials on Youtube. Then I'll watch them. Then I will give it a try myself.

https://www.youtube.com/results?search_query=video+editing+for+beginners

https://youtu.be/7eXEzpM91H0
How to Start a Faceless YouTube Channel in 2023 [FREE COURSE]

Youtube search really knows what I want.

Mhhh...no, this is not on video editing. Let me skip it instead of getting hyped about another course vendor like I have in the past few hours. I need technical skills here. I can watch more of these videos once I have content out there.

https://youtu.be/y7Ci_H9bYEk
Beginners Guide to Video Editing (Start to Finish)

https://youtu.be/y7Ci_H9bYEk?t=67

I forgot the word podcast. I'll also need to figure out streaming and screenscasting.

https://youtu.be/y7Ci_H9bYEk?t=113
> I would encourage you to invest in an external drive.

I'll probably have to get rid of my old anime and images for this. I know video takes up a lot of space.

https://youtu.be/y7Ci_H9bYEk?t=177
> What is cool about Camtasia is not only that it is a video editor, but a screen recorder for beginners.

https://youtu.be/y7Ci_H9bYEk?t=264
> ...Now I am just going to watch through the video and take out uhms and pauses and things like that.

https://youtu.be/y7Ci_H9bYEk?t=273

What does he mean by this? Editing backwards? Last take?

https://youtu.be/y7Ci_H9bYEk?t=344

I am not really following what he is doing here.

https://youtu.be/y7Ci_H9bYEk?t=595

Camtasia has Youtube integration.

https://www.techsmith.com/video-editor.html?utm_source=fastspring&utm_medium=affiliates&utm_content=Think%20Media&irgwc=1&clickid=0FnyjcRe%3AxyNUYJx4M21QwUTUkA1F11FFUYFVo0

It is pretty expensive software, but this sort of thing I might be able to find on CGPersia. Nevermind it for now.

https://youtu.be/vxUNSuB439o
Small Channels, Not Getting Views? DO THIS!

It is 5m so let me watch it.

https://youtu.be/vxUNSuB439o?t=24
> Remix longform vids into shorts.

https://youtu.be/vxUNSuB439o?t=225

I am kind of tuning out. What are these community posts.

https://youtu.be/vxUNSuB439o?t=267

Hmmm, I didn't realize this.

https://youtu.be/TZ9prxJhbPw
The Most Underrated Hack To Getting VIEWS on Old Videos!

Let me watch this.

https://youtu.be/TZ9prxJhbPw?t=192

Write your title first before shooting your video.

https://youtu.be/TZ9prxJhbPw?t=201

Script? I should write a script?

Arguably my plan was to just come in and talk, but sure, writing a script is an option.

3:25pm. They got me. I need video editing! Forget everything else!

https://youtu.be/ZGIl5lGFBxY
Start Editing YouTube Videos for FREE with ZERO Knowledge - Video Editing for TOTAL BEGINNERS

Let me watch this.

3:35pm. Checked the email, and got some advertizement from the .NET board and functional works. Forget it. Let me go back to the video.

https://youtu.be/ZGIl5lGFBxY?t=205
> Insanely good free version

He is talking about DaVinci Resolve.

https://youtu.be/ZGIl5lGFBxY?t=948

I find this easy to understand. Ok.

https://youtu.be/ZGIl5lGFBxY?t=1428

Fade out.

https://youtu.be/ZGIl5lGFBxY?t=1857

This has powerful compositing it seems.

https://youtu.be/ZGIl5lGFBxY?t=1891

Also uploads directly to Youtube.

https://youtu.be/ZGIl5lGFBxY?t=1935

Let me take a short break here.

4:35pm. Let me resume. I have 4 mins left in that video, so let me watch it. Then I will look at how to screencast.

https://youtu.be/E3GdVOHr1Sg
How to Create a Screencast Video (4 Easy Steps)

https://youtu.be/E3GdVOHr1Sg?t=108
> Step 1: Write your script.

Remember that time I applied for that free AI grant? I pasted the notebook to the top of the screen and it was horrible. It is time to make up for that.

https://youtu.be/E3GdVOHr1Sg?t=132

Brief. Natural and enganging language.

Every 150 words comes out to 1m of video. Huh, really. I see.

https://youtu.be/E3GdVOHr1Sg?t=181

QuickTime Player. Wow that brings me back to the 90s. I haven't used that in forever.

https://youtu.be/E3GdVOHr1Sg?t=200
> ActivePresenter

Here he is talking about the screen casting tools.

https://youtu.be/E3GdVOHr1Sg?t=204

It lets me edit the video right in the software.

https://youtu.be/E3GdVOHr1Sg?t=210

Slideshows.

https://youtu.be/E3GdVOHr1Sg?t=277

Oh I thought I might be doing the voiceover as I am screencasting, but it is a separate step.

4:55pm. Right now I am downloading the Loom desktop ap.

As my first exercise I am going to try making a recording of myself making a Python hello world program.

Let me plug in the webcamera.

5:15pm. I've taken my first screencast, of me making a Python hello world program in Loom. What is my plan now. I am looking at whether I could get Camtasia off CGPersia and the answer is no, but getting Adobe Premiere Pro would be no problem. There are all these different tools.

https://www.loom.com/home

For now let me watch the starter videos. It seems Loom has a web interface.

https://atomisystems.com/activepresenter/

Oh, this has a free version.

I also found a pirate version on IGetIntoPC.

It is like 80mb so let me get it. It has video editing capabilities directly in it.

But let me put this aside. Let me watch the Loom videos. It will take me some time to get comfortable with this. Once I've practiced this enough I will have gained an essential skill to survive in this web era.

5:30pm. Loom wasn't quite what I thought, though it is useful in its own right. I really want something to make Youtube vids, but Loom is more like a platform for sharing presentations there directly.

5:35pm. It even has a video on how to record a presentation.

https://www.loom.com/share/2f41d3d8d8bd42108de05cccd281ebde

Here is the video I made...

This is interesting I guess, but not quite what I wanted for making Youtube videos.

I now realize more exactly what the UPMEM guy yesterday wanted of me. But nevermind that.

Loom is really for making quick presentations. It does not have any capabilities for voice overs, video editing or anything of that sort. It is a platform competitive to Youtube.

Not really what I want, but maybe it would be good for job presentations.

6:10pm. Had to leave for lunch. I am back.

Anyway, I've installed (and cracked) ActivePresenter.

https://atomisystems.com/activepresenter/tutorials/?utm_source=direct&utm_medium=installation&utm_campaign=ActivePresenter9.0.3

6:15pm. I think I am going to close here. Making a videos and presentations should be my focus from here on out. Who knows about becoming a Youtuber, but all this practice will reinforce my social skills in the end, so that interviews stop being a problem.

https://www.youtube.com/playlist?list=PLwcfcaumpdgQ1qlAiLkezXw_UJnGa0CTU
ActivePresenter 9: Guide for Beginners

This really has a lot of what I do not need.

6:25pm. Ah, whatever. Let me watch it for a bit.

https://youtu.be/R66g9X2WigM?t=66

Sigh, I do not need all this.

https://youtu.be/1TmcmSdY42A?list=PLwcfcaumpdgQ1qlAiLkezXw_UJnGa0CTU&t=118
> If you are looking for an amazing screen recorder, ActivePresenter is the perfect choice.

6:35pm. Right now I am trying out the software itself and thanks to that DaVinci tutorial from earlier it does not at all look hard to use. I am starting to realize something. Screen recording is such a basic functionality. Would a piece of software like DaVinci Resolve not have it natively?

Though, I do not need it since I have ActivePresenter.

https://youtu.be/V9qAIgPtlPs
Differences between Record Video and Record Software Simulation - ActivePresenter 8

I am wondering about the synthetic voice in this video. I wonder if AP has an option to do that as well? I am betting yes.

https://youtu.be/V9qAIgPtlPs?t=131

This other simulation mode is interesting, I wonder what it is for? Nevermind that for now.

6:40pm. https://youtu.be/XhZ8hWoNRtE?list=PLwcfcaumpdgQ1qlAiLkezXw_UJnGa0CTU
How to Record Screen as Video with ActivePresenter 9

Let me watch this.

https://youtu.be/XhZ8hWoNRtE?list=PLwcfcaumpdgQ1qlAiLkezXw_UJnGa0CTU&t=93

Yeah, I saw that before. Let me watch this video today and what I will leave for tomorrow are video editing options.

https://youtu.be/XhZ8hWoNRtE?list=PLwcfcaumpdgQ1qlAiLkezXw_UJnGa0CTU&t=141

Oh, I didn't see this option. Interesting.

It is possible to lock it to an application.

https://youtu.be/XhZ8hWoNRtE?list=PLwcfcaumpdgQ1qlAiLkezXw_UJnGa0CTU&t=181

Oh, it is possible to turn off system audio. But I can also just remove it during timeline editing.

https://youtu.be/XhZ8hWoNRtE?list=PLwcfcaumpdgQ1qlAiLkezXw_UJnGa0CTU&t=216

Ctrl+End is not a good key for ending the reconding for me since I am frequently using it to scroll down to the end of a document. I'll change it to something else. Ctrl+Pause seems good. I never use that key.

https://youtu.be/AsET8LAX3CQ?list=PLwcfcaumpdgQ1qlAiLkezXw_UJnGa0CTU
How to Edit Screen Recordings with ActivePresenter 9

I'll leave this for tomorrow. The software is important, but it is not crucial for overcoming my bottleneck. AP9 should be more than for what I need. Making money via Youtube and things like that are one thing, but the primary goal of this exercise will be to start my own channel and get over my social anxiety. I should get used to talking into the mic, making my own screencasts and video tutorials.

For the past year, I've been practicing 3d art, writing, programming and using generative AI to make images. I might as well go in this direction as well. It could only do me good. Insanity is repeating the same thing and expecting a different result.

7pm. Either way, I should take those Youtubers showing me how to make money with a grain of salt. The amount of people making money by selling expensive courses teaching how to make money vs the amount of people actually making money from such activities is likely to be loopsided to the former. I'll take good advice and leave out the bad if I can.

Ultimately, the most important thing is to just work at it. Watching those videos did make me realize that going the Patreon route might be difficult with Heaven's Key. Royal Road really lacks the options to give people like me a way to make money.

7:15pm. I'll just go for it. I'll grasp this thread and pull on it until I reach all the way to the end. Who knows what will come in the future."

---
## [sammmhodge/AlienPowerWash](https://github.com/sammmhodge/AlienPowerWash)@[640b99b5cc...](https://github.com/sammmhodge/AlienPowerWash/commit/640b99b5cc3f451aaa378edd8ed5feed3f500838)
#### Wednesday 2023-01-25 18:34:55 by sammmhodge

poop

Feces (or faeces), known colloquially and in slang as poo and poop, are the solid or semi-solid remains of food that was not digested in the small intestine, and has been broken down by bacteria in the large intestine.[1][2] Feces contain a relatively small amount of metabolic waste products such as bacterially altered bilirubin, and dead epithelial cells from the lining of the gut.[1]

Feces are discharged through the anus or cloaca during defecation.

Feces can be used as fertilizer or soil conditioner in agriculture. They can also be burned as fuel or dried and used for construction. Some medicinal uses have been found. In the case of human feces, fecal transplants or fecal bacteriotherapy are in use. Urine and feces together are called excreta.

Skatole is the principal compound responsible for the unpleasant smell of feces.
Characteristics

The molecule hydrogen sulfide contributes to the smell of feces.
The distinctive odor of feces is due to skatole, and thiols (sulfur-containing compounds), as well as amines and carboxylic acids. Skatole is produced from tryptophan via indoleacetic acid. Decarboxylation gives skatole.[3][4]

The perceived bad odor of feces has been hypothesized to be a deterrent for humans, as consuming or touching it may result in sickness or infection.[5]

Physiology
Main article: Defecation
Feces are discharged through the anus or cloaca during defecation. This process requires pressures that may reach 100 millimetres of mercury (3.9 inHg) (13.3 kPa) in humans and 450 millimetres of mercury (18 inHg) (60 kPa) in penguins.[6][7] The forces required to expel the feces is generated through muscular contractions and a build-up of gases inside the gut, prompting the sphincter to relieve the pressure and to release the feces.[7]

Ecology
After an animal has digested eaten material, the remains of that material are discharged from its body as waste. Although it is lower in energy than the food from which it is derived, feces may retain a large amount of energy, often 50% of that of the original food.[8] This means that of all food eaten, a significant amount of energy remains for the decomposers of ecosystems. Many organisms feed on feces, from bacteria to fungi to insects such as dung beetles, who can sense odors from long distances.[9] Some may specialize in feces, while others may eat other foods. Feces serve not only as a basic food, but also as a supplement to the usual diet of some animals. This process is known as coprophagia, and occurs in various animal species such as young elephants eating the feces of their mothers to gain essential gut flora, or by other animals such as dogs, rabbits, and monkeys.

Feces and urine, which reflect ultraviolet light, are important to raptors such as kestrels, who can see the near ultraviolet and thus find their prey by their middens and territorial markers.[10]

Seeds also may be found in feces. Animals who eat fruit are known as frugivores. An advantage for a plant in having fruit is that animals will eat the fruit and unknowingly disperse the seed in doing so. This mode of seed dispersal is highly successful, as seeds dispersed around the base of a plant are unlikely to succeed and often are subject to heavy predation. Provided the seed can withstand the pathway through the digestive system, it is not only likely to be far away from the parent plant, but is even provided with its own fertilizer.

Organisms that subsist on dead organic matter or detritus are known as detritivores, and play an important role in ecosystems by recycling organic matter back into a simpler form that plants and other autotrophs may absorb once again. This cycling of matter is known as the biogeochemical cycle. To maintain nutrients in soil it is therefore important that feces returns to the area from which they came, which is not always the case in human society where food may be transported from rural areas to urban populations and then feces disposed of into a river or sea.

Human feces
Main article: Human feces
Depending on the individual and the circumstances, human beings may defecate several times a day, every day, or once every two or three days. Extensive hardening of the feces that interrupts this routine for several days or more is called constipation.

The appearance of human fecal matter varies according to diet and health.[11] Normally it is semisolid, with a mucus coating. A combination of bile and bilirubin, which comes from dead red blood cells, gives feces the typical brown color.[1][2]

After the meconium, the first stool expelled, a newborn's feces contains only bile, which gives it a yellow-green color. Breast feeding babies expel soft, pale yellowish, and not quite malodorous matter; but once the baby begins to eat, and the body starts expelling bilirubin from dead red blood cells, its matter acquires the familiar brown color.[2]

At different times in their life, human beings will expel feces of different colors and textures. A stool that passes rapidly through the intestines will look greenish; lack of bilirubin will make the stool look like clay.

Uses of animal feces
See also: Reuse of excreta and Human feces § Uses
Fertilizer
The feces of animals, e.g. guano and manure often are used as fertilizer.[12]

Energy
Further information: Dry animal dung fuel
Dry animal dung, such as that of camel, bison and cattle, is burned as fuel many countries.[13]

Animals such as the giant panda[14] and zebra[15] possess gut bacteria capable of producing biofuel. The bacterium in question, Brocadia anammoxidans, can be used to synthesize the rocket fuel hydrazine.[16][17]

Coprolites and paleofeces
A coprolite is fossilized feces and is classified as a trace fossil. In paleontology they give evidence about the diet of an animal. They were first described by William Buckland in 1829. Prior to this, they were known as "fossil fir cones" and "bezoar stones". They serve a valuable purpose in paleontology because they provide direct evidence of the predation and diet of extinct organisms.[18] Coprolites may range in size from a few millimetres to more than 60 centimetres.

Palaeofeces are ancient feces, often found as part of archaeological excavations or surveys. Intact paleofeces of ancient people may be found in caves in arid climates and in other locations with suitable preservation conditions. These are studied to determine the diet and health of the people who produced them through the analysis of seeds, small bones, and parasite eggs found inside. Feces may contain information about the person excreting the material as well as information about the material. They also may be analyzed chemically for more in-depth information on the individual who excreted them, using lipid analysis and ancient DNA analysis. The success rate of usable DNA extraction is relatively high in paleofeces, making it more reliable than skeletal DNA retrieval.[19]

The reason this analysis is possible at all is due to the digestive system not being entirely efficient, in the sense that not everything that passes through the digestive system is destroyed. Not all of the surviving material is recognizable, but some of it is. Generally, this material is the best indicator archaeologists can use to determine ancient diets, as no other part of the archaeological record is so direct an indicator.[20]

A process that preserves feces in a way that they may be analyzed later is the Maillard reaction. This reaction creates a casing of sugar that preserves the feces from the elements. To extract and analyze the information contained within, researchers generally have to freeze the feces and grind it up into powder for analysis.[21]

Other uses

A pet waste station in Tucker, Georgia, US
Animal dung occasionally is used as a cement to make adobe mudbrick huts,[22] or even in throwing sports, especially with cow and camel dung.[23]

Kopi luwak (pronounced [ˈkopi ˈlu.aʔ]), or "civet coffee", is coffee made from coffee berries that have been eaten by and passed through the digestive tract of the Asian palm civet (Paradoxurus hermaphroditus). Giant pandas provide fertilizer for the world's most expensive green tea.[24] In Malaysia, tea is made from the droppings of stick insects fed on guava leaves.

In northern Thailand, elephants are used to digest coffee beans in order to make Black Ivory coffee, which is among the world's most expensive coffees. Paper is also made from elephant dung in the country.[24]

Dog feces was used in the tanning process of leather during the Victorian era. Collected dog feces, known as "pure", "puer", or "pewer",[25] was mixed with water to form a substance known as "bate", because proteolytic enzymes in the dog feces helped to relax the fibrous structure of the hide before the final stages of tanning.[26] Dog feces collectors were known as pure finders.[27]

Elephants, hippos, koalas and pandas are born with sterile intestines, and require bacteria obtained from eating the feces of their mothers to digest vegetation.

In India, cow dung and cow urine are major ingredients of the traditional Hindu drink Panchagavya. Politician Shankarbhai Vegad stated that they can cure cancer.[28]

In the Middle East, cow dung is consumed for a variety of reasons, such as curing dysentery, a belief of healing properties or as a food staple.[citation needed]

Terminology

Cyclosia papilionaris consuming bird droppings
Feces is the scientific terminology, while the term stool is also commonly used in medical contexts.[29] Outside of scientific contexts, these terms are less common, with the most common layman's term being "poop" or "poo". The term shit is also in common use, although is widely considered vulgar or offensive. There are many other terms, see below.

Etymology
The word faeces is the plural of the Latin word faex meaning "dregs". In most English-language usage, there is no singular form, making the word a plurale tantum;[30] out of various major dictionaries, only one enters variation from plural agreement.[31]

Synonyms
Further information: Shit
"Feces" is used more in biology and medicine than in other fields (reflecting science's tradition of classical Latin and New Latin)

In hunting and tracking, terms such as dung, scat, spoor, and droppings normally are used to refer to non-human animal feces
In husbandry and farming, manure is common.
Stool is a common term in reference to human feces. For example, in medicine, to diagnose the presence or absence of a medical condition, a stool sample sometimes is requested for testing purposes.[32]
The term bowel movement(s) (with each movement a defecation event) is also common in health care.
There are many synonyms in informal registers for feces, just like there are for urine. Many are euphemismistic, colloquial, or both; some are profane (such as shit), whereas most belong chiefly to child-directed speech (such as poo or the palindromic word poop) or to crude humor (such as crap, dump, load and turd.).

Horse feces
Feces of animals
The feces of animals often has special names (some of them are slang), for example:

Non-human animals
As bulk material – dung
Individually – droppings
Cattle
Bulk material – cow dung
Individual droppings – cow pats, meadow muffins, etc.
Deer (and formerly other quarry animals) – fewmets
Wild carnivores – scat
Otter – spraint
Birds (individual) – droppings (also include urine as white crystals of uric acid)
Seabirds or bats (large accumulations) – guano
Herbivorous insects, such as caterpillars and leaf beetles – frass
Earthworms, lugworms etc. – worm castings (feces extruded at ground surface)
Feces when used as fertilizer (usually mixed with animal bedding and urine) – manure
Horses – horse manure, roadapple (before motor vehicles became common, horse droppings were a big part of the rubbish communities needed to clean off roads)
Society and culture

Sign ordering owners to clean up after pets, Houston, Texas, 2011
Feelings of disgust
Main article: Human feces
In all human cultures, feces elicits varying degrees of disgust in adults. Children under two years typically have no disgust response to it, suggesting it is culturally derived.[33] Disgust toward feces appears to be strongest in cultures where flush toilets make olfactory contact with human feces minimal.[34][35] Disgust is experienced primarily in relation to the sense of taste (either perceived or imagined) and, secondarily to anything that causes a similar feeling by sense of smell, touch, or vision.

Social media
There is a Pile of Poo emoji represented in Unicode as U+1F4A9 💩 PILE OF POO, called unchi or unchi-kun in Japan.[36][37]

Jokes
Poop is the center of toilet humor, and is commonly in interest of young children and teenagers.[38]

---
## [Aintgon/Python](https://github.com/Aintgon/Python)@[1cfca65745...](https://github.com/Aintgon/Python/commit/1cfca65745f18e41bab90aec6b7fb4e0ee8af69e)
#### Wednesday 2023-01-25 18:37:31 by Aintgon

Update and rename searches/binary_search.py to Fuck you Biden

---
## [finalchild/rust](https://github.com/finalchild/rust)@[2afe58571e...](https://github.com/finalchild/rust/commit/2afe58571e53d48a1fc2354271abe5aff60c5c44)
#### Wednesday 2023-01-25 18:46:24 by bors

Auto merge of #104658 - thomcc:rand-update-and-usable-no_std, r=Mark-Simulacrum

Update `rand` in the stdlib tests, and remove the `getrandom` feature from it.

The main goal is actually removing `getrandom`, so that eventually we can allow running the stdlib test suite on tier3 targets which don't have `getrandom` support. Currently those targets can only run the subset of stdlib tests that exist in uitests, and (generally speaking), we prefer not to test libstd functionality in uitests, which came up recently in https://github.com/rust-lang/rust/pull/104095 and https://github.com/rust-lang/rust/pull/104185. Additionally, the fact that we can't update `rand`/`getrandom` means we're stuck with the old set of tier3 targets, so can't test new ones.

~~Anyway, I haven't checked that this actually does allow use on tier3 targets (I think it does not, as some work is needed in stdlib submodules) but it moves us slightly closer to this, and seems to allow at least finally updating our `rand` dep, which definitely improves the status quo.~~ Checked and works now.

For the most part, our tests and benchmarks are fine using hard-coded seeds. A couple tests seem to fail with this (stuff manipulating the environment expecting no collisions, for example), or become pointless (all inputs to a function become equivalent). In these cases I've done a (gross) dance (ab)using `RandomState` and `Location::caller()` for some extra "entropy".

Trying to share that code seems *way* more painful than it's worth given that the duplication is a 7-line function, even if the lines are quite gross. (Keeping in mind that sharing it would require adding `rand` as a non-dev dep to std, and exposing a type from it publicly, all of which sounds truly awful, even if done behind a perma-unstable feature).

See also some previous attempts:
- https://github.com/rust-lang/rust/pull/86963 (in particular https://github.com/rust-lang/rust/pull/86963#issuecomment-885438936 which explains why this is non-trivial)
- https://github.com/rust-lang/rust/pull/89131
- https://github.com/rust-lang/rust/pull/96626#issuecomment-1114562857 (I tried in that PR at the same time, but settled for just removing the usage of `thread_rng()` from the benchmarks, since that was the main goal).
- https://github.com/rust-lang/rust/pull/104185
- Probably more. It's very tempting of a thing to "just update".

r? `@Mark-Simulacrum`

---
## [Aintgon/security-guide-for-developers](https://github.com/Aintgon/security-guide-for-developers)@[dd01b84836...](https://github.com/Aintgon/security-guide-for-developers/commit/dd01b84836c3550cf785094aa123d2684f3533c6)
#### Wednesday 2023-01-25 19:19:41 by Aintgon

Update and rename security-checklist.md to Fuck you biden

---
## [Aintgon/PressScraper](https://github.com/Aintgon/PressScraper)@[866707930f...](https://github.com/Aintgon/PressScraper/commit/866707930f8002531265fabf841279c9a35f58c4)
#### Wednesday 2023-01-25 19:50:27 by Aintgon

Update and rename Senate/sintelligence_spider.py to Fuck you biden

---
## [Aintgon/PressScraper](https://github.com/Aintgon/PressScraper)@[d7b2ca2b83...](https://github.com/Aintgon/PressScraper/commit/d7b2ca2b83b183d1dc374ffa24b264581140bada)
#### Wednesday 2023-01-25 19:57:32 by Aintgon

Update and rename .vscode/settings.json to Fuck you biden

---
## [Aidyn-A/pytorch](https://github.com/Aidyn-A/pytorch)@[5c6f5439b7...](https://github.com/Aidyn-A/pytorch/commit/5c6f5439b7e6a5e63a68b36b4cf093a00d46e8be)
#### Wednesday 2023-01-25 20:16:29 by Edward Z. Yang

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
## [jljaco/test-infra](https://github.com/jljaco/test-infra)@[95e4857b28...](https://github.com/jljaco/test-infra/commit/95e4857b28122c6c5f8a30260be3dcac94e0e466)
#### Wednesday 2023-01-25 20:25:18 by Amine

Move Go binaries to `/usr/bin` (#287)

Issue https://github.com/aws-controllers-k8s/community/issues/1640

TL;DR: Prow was mounting `test-infra` code volume into `$GOPATH`
causing the deletion of `kind` and `controller-gen` binaries that are
installed in `$GOPATH/bin`


Yesterday, i embarked on a wild 7 hour journey to fix a bug that had
been causing prow jobs to fail with the error message "Kind not found".
The bug was introduced after a recent update that bumped the Go compiler
to `1.19`. I found the investigation to this bug to be both interesting
and frustrating, so i wanted to share some key takeways with the
community:

[The patch](https://github.com/aws-controllers-k8s/test-infra/commit/14dda81ce8ea430b51c9ce738483bea3744a5450) that introduced Go `1.19` also modified a `go get` command
into a `go install` command (because of this deprecation notice:
https://go.dev/doc/go-get-install-deprecation), which technically should
not have caused any issues. I tried restarting the e2e jobs in various
repositories to figure out whether the error was only related to one
controller or code-generator only, but all the repositories that execute
e2e tests were affected.

First, i started suspecting that thee `go install` command was not
working properly or had not been used correctly. I experiemented with it
locally, using various combinations of `GOPATH` and `GOBIN`, however, i
learned that the Go compiler is sophisticated enough to always put
downloaded binaries under `GOBIN` or `GOPATH/bin`. I then wondered if
the `PATH` variable didn't include the `GOBIN` path, which is supposed
to contain the `kind` and `controller-gen` binaries. I spent some time
reading the Dockerfiles and testing scripts, but they all set `GOPATH`
and always included a `GOBIN` in the `PATH` variable.

I also suspected that the issue may be related to the containers, but
experimentations with "Go containers" and environement variables
manipulation did not yield any results. I also tried building minimal
DOckerfiles to try to reproduce the issue, but that also did not give
any clues.

At this point, I suspected the container image it self. I build an image
locally and ran a shell inside it, but everythin g looked fine. THe
`kind` and `controller-gen` binaries were present and the `PATH` and
`GOPATH` variables were properly set. I then suspect that we may have a
corrupted published image in ECR, but pulling the image and running the
same commands revealed that the image was fine.

I then took a break from experimenting with Go/Docker/Envvars and tried
to spin some prowjobs with `v0.0.10` and `v0.0.9` (the last two versions
that were still using Go 1.17) of the integration tests image. This
confirmed that the issue was only with `v0.0.11`.

So, I decided to investigate further and logged in the Prow production
cluster. My first attempt was to restart a job and try to "exec bash" in
it, but the jobs failed to quickly for that to be possible. I then ran
a custom prow job (with `v0.0.11` integration image tag) but with a
`sleep 10000` command. When looking inside, there were no `kind` or
`controller-gen` binaries, i searched the entire file system, they were
nowhere to be found, grep, find, name it all.. nada. I then execute a
`go install sigs.k8s.io/kind@v0.17.0"`, and bam, it worked, the binary
was here again. The same thing happened with controller-gen. So for now
we know that we ship images with all the necessary binaries and when a
prow job starts, they disapear...

To isolate the problem further, i created a `ProwJob` resource and
copied the `Pod` (spawned by Prow) spec and metadata into a different
file. Running the same commands used previously proved that indeed
something is wrong with the pod spec, causing the binaries to disapear.
And when a file disppears it reminds me of my college years, where i
epically failed to use symbolic links, which is a bit similar (at least
from a UX point) to volume mounts in the Docker world.

So, i decided to check the volume mounts, and to my not-surprise, I
found this:

```yaml
    - mountPath: /home/prow/go
      name: code
```

Yes... Prow is mounting the test-infra source code into `GOPATH`
(`/home/prow/go` in prow jobs) ! Which is the parent directory of
`GOBIN` where we install the binaries. And it all makes sense now.
Mounting code into this directory overrides the existing volume and
deletes everything existing in `GOPATH` including the binaries we
installed before.

The Dockerfile was missing the `mv` commands that puts `kind` and
`controller-gen` in `/usr/bin`. To fix this issue, I added the missing
`mv` command to the docker file and published and new `integration`
image `v0.0.12`.

---

Anyways, investigating the source of the volume mount led me to the Prow
presets configurations. Presets are a set of configurations (volume
mounts, environement variables, etc...) that are used for jobs with
specific labels in their metadata. I tried to play with this in our Prow
cluster, but quickly stoped when it was a bit risky and could break
other components too. While digging into `test-infra` pod-util package i
learned that the code volume is not coming from our defined presets and
is a default preset coming from Prow it self - the `/home/prow/go` value
is harded-coded in `prow/pod-utils/decorate/podspec.go#L54`. I'm not
sure whether we can override this value.

Anyways, for now, i'm just gonna implement a quick fix that moves the
binaries to `/usr/bin` instead of leaving them inside `GOBIN`. Ideally
we should either choose a new directory go `GOPATH` that is different
from `$HOME/go` or find a solution that will let the code and our
binaries coexist in the same place. Either of them requires a lot of
changes and can agressively break some our prow components/scripts.

@jljaco is currently workng on creating a staging cluster, which will
provide us a safe environementto test and experiment with new
configurations. This will allow us to try out new changes without having
to woryy about potentially impacting the production environement.

Signed-off-by: Amine Hilaly <hilalyamine@gmail.com>

By submitting this pull request, I confirm that my contribution is made under the terms of the Apache 2.0 license.

---
## [jnutt367/the_holy_bible](https://github.com/jnutt367/the_holy_bible)@[ea2ba8994b...](https://github.com/jnutt367/the_holy_bible/commit/ea2ba8994bc5128955e31b73f6c063029d800b29)
#### Wednesday 2023-01-25 20:25:36 by Jason Nutt (He/Him) Developer/Creator

Update Home.module.css

text-shadow: #FC0 1px 0 10px;
  color: white; added for holy to match title styles hopefully brighten it up a bit ...it IS the Bible after all, light of the world and all. !!! Love you Jesus. Thanks for having mercy on a sinner like me. I love you.

---
## [Thurinum/brotherhood-server](https://github.com/Thurinum/brotherhood-server)@[165284abe3...](https://github.com/Thurinum/brotherhood-server/commit/165284abe3b9871f4f5d5f2ba5bb4812c407847e)
#### Wednesday 2023-01-25 21:07:51 by 2156153

chore: Reformulate seed data to be more presentable

- remove a sketchy joke which might offend someone (I guess)
- remove fuwwy jokes (better safe than sorry lol)

---
## [Aintgon/StandWithUkraine](https://github.com/Aintgon/StandWithUkraine)@[726b9d749f...](https://github.com/Aintgon/StandWithUkraine/commit/726b9d749fdc3b00d4806014d8bfa4447039e1f8)
#### Wednesday 2023-01-25 21:25:23 by Aintgon

Update and rename badges/RussianWarship.svg to Go fuck yourself Ukraine

---
## [Aintgon/StandWithUkraine](https://github.com/Aintgon/StandWithUkraine)@[4729be6a47...](https://github.com/Aintgon/StandWithUkraine/commit/4729be6a47c4743640cc578eadaee1a3ccf26bd6)
#### Wednesday 2023-01-25 21:27:53 by Aintgon

Update and rename docs/Donate.md to Go fuck yourself Ukraine

---
## [Aintgon/StandWithUkraine](https://github.com/Aintgon/StandWithUkraine)@[e02ef7fe3e...](https://github.com/Aintgon/StandWithUkraine/commit/e02ef7fe3e79e0614e0ad5e56b67f2b7e5ecdcbe)
#### Wednesday 2023-01-25 21:28:42 by Aintgon

Update and rename docs/CyberSafety.md to Go fuck yourself Ukraine

---
## [Aintgon/list-of-security-resources-for-ukraine](https://github.com/Aintgon/list-of-security-resources-for-ukraine)@[76dc1b78c7...](https://github.com/Aintgon/list-of-security-resources-for-ukraine/commit/76dc1b78c704e65cc33fc8bc3db968ec9123223f)
#### Wednesday 2023-01-25 21:51:38 by Aintgon

Update and rename new-security-resource-for-ukraine.md to Fuck you nato

---
## [Aintgon/alliance](https://github.com/Aintgon/alliance)@[43267ccdad...](https://github.com/Aintgon/alliance/commit/43267ccdad269735e0821df907c5d75caab5c519)
#### Wednesday 2023-01-25 21:53:42 by Aintgon

Update and rename ThreatDragonModels/ImagingApp/ImagingApp.json to Fuck you nato

---
## [iSentrie/rpemotes](https://github.com/iSentrie/rpemotes)@[45b9259ff8...](https://github.com/iSentrie/rpemotes/commit/45b9259ff84eea10f91aa0c2b4d122cedf9f7fc9)
#### Wednesday 2023-01-25 22:10:49 by Mads

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
## [tcharding/rust-bitcoin](https://github.com/tcharding/rust-bitcoin)@[f6d983b2ef...](https://github.com/tcharding/rust-bitcoin/commit/f6d983b2ef4dfacd53499fd9f1d77058c0f396ff)
#### Wednesday 2023-01-25 22:14:34 by Andrew Poelstra

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
## [Aintgon/digital-asset-policy-proposal](https://github.com/Aintgon/digital-asset-policy-proposal)@[6ca8404da2...](https://github.com/Aintgon/digital-asset-policy-proposal/commit/6ca8404da223a54ca347a36cf037b2cc3874223b)
#### Wednesday 2023-01-25 22:21:58 by Aintgon

Update and rename CONTRIBUTING.md to Fuck you Joe Biden

---
## [DrewHans/fossBodyBuilding](https://github.com/DrewHans/fossBodyBuilding)@[4ca8087b49...](https://github.com/DrewHans/fossBodyBuilding/commit/4ca8087b49a1f21732157b029d22966f59077f73)
#### Wednesday 2023-01-25 23:41:53 by DrewHans

Add elements to track-workout page

I've been a little busy with real life, but I'm finally ready to
get back to work on this little side project. I started working on
the track-workout page. Consider this a super rough draft.

I also added link-back ids to the link back links in the navbar.
I don't remember why I did this, but I'm sure there was a good
reason.

The input elements on the track-body page were given min, max, and
step values.

Create and edit pages were updated so that the page will return to
the previous page when the user clicks the link-back icon (yeah,
now I remember; this is why I needed the ids).

That's about it. I'll keep working on the track-workout page when I
have time. I'd like to make use of taphold for deleting sets, but
that's a problem for future me.

---
## [agraef/purr-data](https://github.com/agraef/purr-data)@[d8d940243e...](https://github.com/agraef/purr-data/commit/d8d940243ecb3470d94b21c5805c212670b2da63)
#### Wednesday 2023-01-25 23:51:58 by Albert Gräf

Windows packaging: GH-friendly OutputBaseFilename.

This makes my life less miserable when doing releases on the GH mirror,
because I don't have to manually edit the installer filenames before
uploading any more.

GitHub doesn't like blanks in upload file names, using dashes instead
makes uploading much easier and eliminates the need to zip the installer
before uploading. We also include a proper cpu architecture designation
(x86 or x86_64) in the output file name in lieu of the '(64 bit)' suffix
which causes trouble in GH uploads as well, because of the parentheses.

Note that this shouldn't affect the Gitlab CI since it looks for a
'Purr*.exe' build artifact, which will still match the package name.

---

