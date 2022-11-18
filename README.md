## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-17](docs/good-messages/2022/2022-11-17.md)


2,200,923 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,200,923 were push events containing 3,314,838 commit messages that amount to 262,298,852 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [zzcclp/guava](https://github.com/zzcclp/guava)@[8a676ade61...](https://github.com/zzcclp/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Thursday 2022-11-17 00:09:31 by cpovirk

Make the build work under more JDK versions.

(Guava is already _usable_ under plenty of verions. This change affects only people who build it themselves.)

And run CI under JDK17. Maybe this will make CI painfully slow, but we'll see what happens. If we want to drop something, we should consider whether to revert 17 or to drop 11 instead (so as to maintain coverage at the endpoints of \[8, 17\]).

## Notes on some of the versions

### JDK9

I expected Error Prone to work, but I saw `invalid flag: -Xep:NullArgumentForNonNullParameter:OFF`, even though that flag is [already](https://github.com/google/guava/blob/166d8c0d8733d40914fb24f368cb587a92bddfe0/pom.xml#L515) part of [the same `<arg>`](https://github.com/google/error-prone/issues/1086#issuecomment-411544589), which works fine for other JDK versions. So I disabled Error Prone for that version.

Then I had a Javadoc problem with the `--no-module-directories` configuration from cl/413934851 (the fix for https://github.com/google/guava/issues/5457). After reading [JDK-8215582](https://bugs.openjdk.org/browse/JDK-8215582) more carefully, I get the impression that that flag might not have been added until 11: "addressed in JDK 11, along with an option to revert to the old layout in case of need." So I disabled it for 9-10.

Then I ran into a problem similar to https://github.com/bazelbuild/bazel/issues/6173 / [JDK-8184940](https://bugs.openjdk.java.net/browse/JDK-8184940). I'm not sure exactly what tool produced a file with a month of 0, but it happened only when building `guava-tests`. At that point, I gave up, though I left the 2 above workarounds in place.

### JDK10

This fails with some kind of problem finding a Guice dependency inside Maven. I didn't investigate.

### JDK15 and JDK16

These fail with [the `TreeMap` bug](https://bugs.openjdk.org/browse/JDK-8259622) that [our collection testers had detected](https://github.com/google/guava/issues/5801#issue-1068748849) but we never got around to reporting. Thankfully, it got reported and [fixed](https://github.com/openjdk/jdk/commit/2c8e337dff4c84fb435cafac8b571f94e161f074) for JDK17. We could consider suppressing the tests under that version.

### JDK18, JDK19, and JDK20-early-access

These fail with [`SecurityManager` trouble](https://github.com/google/guava/issues/5801#issuecomment-1293817701).

## Notes on the other actual changes

### `maven-javadoc-plugin`

I set up `maven-javadoc-plugin` to use `-source ${java.specification.version}`. Otherwise, it would [take the version from `maven-compiler-plugin`](https://github.com/google/guava/issues/5801#issuecomment-1314291284). That's typically fine: Guava's source code targets Java 8, so `-source 8` "ought" to work. But it doesn't actually work because we also pass Javadoc the _JDK_ sources (so that `{@inheritDoc}` works better), which naturally can target whichever version of the JDK we're building with.

### Error Prone

While Error Prone is mostly usable [on JDK11+](https://errorprone.info/docs/installation), some of its checks have [problems under some versions](https://github.com/google/error-prone/issues/3540), at least when they're reporting warnings.

This stems from its use of part of the Checker Framework, which [doesn't support JDKs in the gap between 11 and 17](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/framework/src/main/java/org/checkerframework/framework/source/SourceChecker.java#L553-L554). And specifically,  it looks like the Checker Framework is [trying to look up `BindingPatternTree` under any JDK12+](https://github.com/typetools/checker-framework/blob/c2d16b3409000ac2e2ca95b8b81ae11e42195308/javacutil/src/main/java/org/checkerframework/javacutil/TreeUtils.java#L131-L144). But `BindingPatternTree` (besides not being present at all [until JDK14](https://github.com/openjdk/jdk/commit/229e0d16313b10932b9ce7506d84096696983699#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R41)) didn't declare that method [until JDK16](https://github.com/openjdk/jdk/commit/18bc95ba51b6864150c28985e65b6f784ea8ee2c#diff-3db4b0ce4411c851bcf75d92ef4dadc7351debcf0f9b2c2623dc513923b45867R39).

Anyway, the problem we saw was [a `NoSuchMethodException` during the `AbstractReferenceEquality` call to `NullnessAnalysis.getNullness`](https://oss-fuzz-build-logs.storage.googleapis.com/log-a9d04aa2-8b5a-47ca-8066-7e6b38548064.txt), which uses Checker Framework dataflow.

To address that, I disabled Error Prone for the versions under which I'd expect the `BindingPatternTree` code to be a problem.

(I also disabled it for JDK10: As noted above, Error Prone [supports JDK11+](https://errorprone.info/docs/installation). And as noted further above, Maven doesn't get far enough with JDK10 to even start running Error Prone.)

Fixes https://github.com/google/guava/issues/5801

RELNOTES=n/a
PiperOrigin-RevId: 488902996

---
## [vdavalon01/pcsx2](https://github.com/vdavalon01/pcsx2)@[87abacc632...](https://github.com/vdavalon01/pcsx2/commit/87abacc63264f9cf554cddf02973e0fc9cd2af77)
#### Thursday 2022-11-17 00:19:47 by RedDevilus

GameDB: Fix multiple games + maintenance

- Area 51: Half Pixel Normal vertex for lighting and other places
- Shrek 2: Basic mipmapping which kinda half fixes the sun missing
- Galaxy Angel II: Normal vertex which reduces misalignment
- Forgotten Realms - Demon Stone: Clamping Mode extra + preserve which will solve the occasional SPS + missing demo entry.
- Spyro Dawn of dragon: SW clut + sprite which doesn't make you vomit from the overbloomification and looks similar to the software renderer
- Castlevania Curse of darkness half sprite which will enlarge the font similar to software renderer + some missing fixes that were available on the Europe and America versions but not Japanese.
- Drakengard 1 + 2 (Also know as Drag-on Dragoon) : Partial (no hashcache) to avoid slow transitions and other areas. Adds missing Japanese Drakengard 1
- Urban reign: Partial texture preloading to fix performance issues in the gameplay
- Onimusha Warlord: Partial preloading to fix performance issues
- Sniper Elite: Fix sky lighting
- Maintenance that add spaces in the titles for Disc1of1 to Disc 1 of 1 and more...

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[bd1857b83a...](https://github.com/ammarfaizi2/linux-fork/commit/bd1857b83a9185bf09e82bde1521a27c463c4d29)
#### Thursday 2022-11-17 00:27:01 by Johannes Weiner

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
## [facebook/sapling](https://github.com/facebook/sapling)@[8b1a3c8fe6...](https://github.com/facebook/sapling/commit/8b1a3c8fe66e21157db20bfe4950804c133639b1)
#### Thursday 2022-11-17 00:27:36 by Evan Krause

Clean up servers when all repos have been disposed

Summary:
We've seen cases on windows where people get stale cwds due to re-using repos. We actually need to fix that problem separately, but I think it's also a good idea to reduce how aggressively we re-use servers.

If someone is running `sl isl` on the CLI, we'll pop open a new browser window regardless. It doesn't impact startup time much if we DON'T re-use the server. The only potential impact of not re-using a server is that other servers already running would get killed.

So the idea here is that we use our refcounted repository to know when we're in the clear to shutdown the entire server. Then the next `sl isl` will get a fresh server no problem.

This has the benefit of making it more likely that people will not get stuck on stale versions of ISL if we update it (though we should add other mitigations for this, too, like an in-app warning if we see that the sl version has changed since spawning)

Miscellany:
- if you spawn with --foreground, we don't do this auto cleanup, since presumably your terminal should fully control this
- We need to  consider --no-open. The idea here is that we only try to clean up after a repo is disposed. So if spawned with --no-open, it won't try to clean itself up until at least one ws connection is started succcessfully.
- We don't have a great way to write to the log file, due to some ergonomics of how we create a file logger. Ideally we'd print a little "Shutting down ISL server due to no remaining repositories + inactivity"

NOTE: This change isn't strictly necessary, but I think it's better for us to err on the side of not re-using servers. Any thoughts on this?

Reviewed By: bolinfest

Differential Revision: D41357143

fbshipit-source-id: 36f88d4a91bc6c06d511dd305b0c02cf377fd768

---
## [CogPlatform/Psychtoolbox-3](https://github.com/CogPlatform/Psychtoolbox-3)@[b85250b062...](https://github.com/CogPlatform/Psychtoolbox-3/commit/b85250b062a7930681cdf7050f3e40457ff962b1)
#### Thursday 2022-11-17 00:32:47 by Mario Kleiner

PsychHID/OSX: Avoid calling PsychHIDWarnAccessDenied frequently.

The latest fix for the latest security bullshit, introduced sometime after macOS
10.15 Catalina. This was found when testing Octave on macOS 12.5 Monterey.

Apparently the call to IOHIDCheckAccess() by PsychHIDWarnAccessDenied()
is now extremely costly on macOS 12 (possibly also macOS 11 - untested) iff
the host application was launched from Terminal.app instead of standalone via
clicking a launch icon. This showed on Octave 6.4 after upgrade to macOS 12.5,
as octave is always launched from Terminal, regardless if in console mode or
GUI mode. Matlab appeared unaffected, as it is usually launched by clicking the
Matlab icon, but if one launches Matlab from a terminal, the same happens.

Why IOHIDCheckAccess() was suddenly turned into such an expensive operation
by the iDiots, i don't know, but our workaround is to no longer call it at each
invocation of KbCheck or KbQueueCreate, but only at PsychHID startup, and
hope this does not have other new bad effects.

Note access time exploded from way less than 1 msec to over 15 msecs! Great
work Apple!

Now we are back to identical performance on Matlab and Octave in both GUI
and commandline mode. Performance is bad compared to Linux or Windows,
but manageable at about 2.4 msecs on macOS 12.5 Monterey on a MBP 2017.
However, if run on a MacBook with touchbar, two PsychHID('KbCheck') calls
are needed for each KbCheck() call, because the touchbar is a separate HID
device, serving the important ESCape key and also function keys, so owners
of a shitty touchbar machine will have to live with execution times of KbCheck
on the order of 5 msecs on not that old hardware like the MBP 2017! This makes
animation loops with KbChecks difficult to run beyond 60-100 fps. Such is the
life of Apple customers...

When we are here, improve troubleshooting instructions for security bullshit
on macOS, and fix two compiler warnings new on macOS 12.

---
## [Gboster-0/lobotomy-corp13](https://github.com/Gboster-0/lobotomy-corp13)@[0220bde488...](https://github.com/Gboster-0/lobotomy-corp13/commit/0220bde48808454df3754d7c71953f66553dcd47)
#### Thursday 2022-11-17 01:26:03 by PotatoTomahto

pathfinding

revert

oops

oops 2

god fragment

fixes

fixes oopsie

forgot scorched girl

real scorched fix:

typo

better patrolling

final

forgot about dreaming

dreaming current name

fragment oopsies

violet oopsie

really the final one

final final one

---
## [xDroidOSS-Pixel/frameworks_base](https://github.com/xDroidOSS-Pixel/frameworks_base)@[e377808c11...](https://github.com/xDroidOSS-Pixel/frameworks_base/commit/e377808c118bd7b509f49f508be40b70e907334f)
#### Thursday 2022-11-17 01:45:16 by Kuba Wojciechowski

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
## [moocowswag/FeatureInflation13](https://github.com/moocowswag/FeatureInflation13)@[5b4ba051a0...](https://github.com/moocowswag/FeatureInflation13/commit/5b4ba051a08e0c63ca77abedd86991d3ba7aaf29)
#### Thursday 2022-11-17 02:04:03 by LemonInTheDark

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
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[de662db397...](https://github.com/lessthnthree/tgstation/commit/de662db39763674f850977dabc8bbe66388d2c9b)
#### Thursday 2022-11-17 03:07:51 by Sol N

Excercise Equipment is now craftable (#71190)

## About The Pull Request

Imagine if you will a humble chaplain who wants nothing more than for
all of the spiritual folk on the station to get as massive gains as they
can, after finding that they can not just make more exercise equipment
and that the station does not have any in public places, they go annoy
security enough to get into permabrig only to find out that they cant
even unwrench the equipment and move it to the church!!!

NOT ANYMORE!!!


![jS2aBMBa0B](https://user-images.githubusercontent.com/116288367/200889423-f1b6365c-24c4-4f45-8ca4-c96c9085cf27.png)
crafting recipies


![dreamseeker_O4BgBRsFa8](https://user-images.githubusercontent.com/116288367/200889002-8dd7c927-0745-46a9-a4bc-578c7279042a.gif)
demonstrating unwrenching and wrenching equipment


![dreamseeker_hCFQJZdzoS](https://user-images.githubusercontent.com/116288367/200889019-5f4c8399-d539-4d84-8a3f-7735c3ba1f68.gif)
crafting a punching bag and punching it

Now you can craft as much exercise equipment as you want! May everyone
on the station get as strong as possible and not just prisoners.

Also I changed the message that plays when you try to use exercise
equipment someone else is using into a balloon alert.

![dreamseeker_PwNesmcR1f](https://user-images.githubusercontent.com/116288367/200890964-4f9fa3ee-ce07-4e6e-815c-a3f4593d06b1.png)

## Why It's Good For The Game

Access to exercise equipment on some maps is limited to static positions
and is currently mostly only for prisoners as every map does not have
public exercise equipment. Expanding the access means that you can have
a Drill Sargent Head of Security or Captain who commands people use
these or allows a psychologist to prescribe healthy exercise habits to
their patients.

I think having the potential for exercise equipment on every map is more
fun and also if prisoners get their hands on tools they should be
allowed to mess with these to annoy security or aid in their escape.

## Changelog
:cl:
add: the punching bag, bench press, and chest press are all able to be
crafted and unanchored.
add: crafting recipes for the above
qol: changed a chat message into a balloon alert
qol: adds screentips to equipment (thanks for suggesting i do this
mothblocks!)
/:cl:

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[3c187487b1...](https://github.com/lessthnthree/tgstation/commit/3c187487b1884040608ba23b0a89aa8b0176c2aa)
#### Thursday 2022-11-17 03:12:39 by MrMelbert

Renews a bunch of old roundend new reports that got lost. Plus, some roundend report QoL for cult and revs. (#71284)

## About The Pull Request

A few roundend reports got lost from moving to dynamic and other prs.
This PRs re-allows them to occur. Namely: "Wizard Killed" (lost in
dynamic), "Blob nuked" (lost in dynamic), "Cult escaped" (lost in cult
rework), and "Nuke Ops Victory" (station destroyed via nuke) (lost from,
what I can see, an oversight / accidental swap of report values).

Additionally, small roundend report QOL for cult: Removes antag datums
from spirit realm ghosts after being dusted, so they do not show up on
the report. And in reverse, heads of staff who were dusted / destroyed
in revolution rounds are now also shown in roundend reports.

## Why It's Good For The Game

Some of these reports are dead, which is is a shame because I think
they're cool and fun.

## Changelog

:cl: Melbert
qol: Successfully fending off a blob now has a cross station news report
again. More pressing reports will take priority over it, though.
qol: Successfully killing a wizard (and all of their apprentices) now
has a cross station news report again.
qol: If more than half of a cultist team manages to escape on the
shuttle (rather than summoning Nar'sie), they will send a unique cross
station news report. This is still a loss, by the way. Summon Nar'sie!
qol: Nuclear Operatives successfully nuking the station now has its
unique cross station news report again, and no longer uses the generic
"The station was nuked" report.
qol: Nuking the station to stop a blob infection now has a unique cross
station news report again. Good luck convincing admins to allow this.
qol: Cult ghosts from "Spirit Realm" no longer persist on the cult's
team after being desummoned, meaning they will not show up on roundend
report.
qol: Heads of staff will now always show up on revolution roundend
report - even if their body was fully destroyed.
/:cl:

---
## [intel/linux-intel-lts](https://github.com/intel/linux-intel-lts)@[adee8f3082...](https://github.com/intel/linux-intel-lts/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Thursday 2022-11-17 03:34:19 by Peter Zijlstra

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
## [Gofawful5/TOPIASTATION](https://github.com/Gofawful5/TOPIASTATION)@[25d4afc869...](https://github.com/Gofawful5/TOPIASTATION/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Thursday 2022-11-17 03:48:07 by Iamgoofball

Retires explosive lance crafting to a nice farm upstate where it has plenty of room to run around (#71256)

## About The Pull Request

You can no longer craft explosive lances.

## Why It's Good For The Game

Explosive lances are unhealthy for the game in it's current iteration.
Many years ago when the game was more loose and we weren't dealing with
players who treat the game like competitive TTT or Town of Salem,

They are a one shot kill weapon, which is the most powerful kind of
weapon in every gamemode. @JohnFulpWillard likened it to 1f1, a concept
from Town of Salem players where the town trades 1 person for 1 bad guy.

Modern ss13 design includes a significantly heavier load of antagonists
that aren't fixed roundstart compared to when the e-lance went in.

When we added the e-lance, if nuke ops spawned, that was it, there was
nuke ops, if you e-lanced the nuke ops and died you were dead until the
next round.

Nowadays you're rolling for lone operative, blob, wizard, disease,
revenant, and every other fun enjoyable antagonist role under the sun.

I can e-lance a nuke op/cultist/traitor/revolutionary/any bad guy in the
game as a non-antag assistant, die, and have a good chance to roll
another, way more fun antag in deadchat.

My change to make the e-lance a proper "we both die" tool didn't
actually help because I didn't quite realize that to the modern SS13
player because of how we designed Dynamic and antagonists in the modern
era, death is, frankly, not a punishment anymore.

It's time we admit the facts, items designed in 2015 SS13 in #12389
simply don't hold up in a healthy manner in 2022 SS13. Dying in SS13 in
2015 was a significantly different experience with different
consequences than it has now, and right now "kills you when you use it"
is not the same massive downside it was 7-8 years ago.

## Changelog
:cl:
del: You can no longer craft explosive lances.
/:cl:

---
## [mayurrai/PYTHON-K21MR](https://github.com/mayurrai/PYTHON-K21MR)@[87966a2ec8...](https://github.com/mayurrai/PYTHON-K21MR/commit/87966a2ec8312c04ff79982594e806baaeb14012)
#### Thursday 2022-11-17 03:52:21 by Mayur Rai

From Paragraphs to Sentences

An Introduction to Sentence Segmentation

Sentence segmentation, means, to split a given paragraph of text into sentences, by identifying the sentence boundaries. In many cases, a full stop is all that is required to identify the end of a sentence, but the task is not all that simple.

This is an open ended challenge to which there are no perfect solutions. Try to break up given paragraphs into text into individual sentences. Even if you don't manage to segment the text perfectly, the more sentences you identify and display correctly, the more you will score.

Abbreviations: Dr. W. Watson is amazing. In this case, the first and second "." occurs after Dr (Doctor) and W (initial in the person's name) and should not be confused as the end of the sentence.

Sentences enclosed in quotes: "What good are they? They're led about just for show!" remarked another. All of this, should be identified as just one sentence.

Questions and exclamations: Who is it? -This is a question. This should be identified as a sentence. I am tired!: Something which has been exclaimed. This should also be identified as a sentence.

INPUT FORMAT

You will be given a chunk of text, containing several sentences, questions, statements and exclamations- all in 1 line.

Constraints

Number of characters in every input does not exceed 10000.
Number of words in every input does not exceed 1000. There will be more than 1 sentence in each input and this number does not exceed 30.
There will be more than 2 characters in every expected sentence and this number does not exceed 10000. There will be more than 2 characters in every test file and this number does not exceed 10000.

OUTPUT FORMAT

You will split the chunk of text into sentences, and display one sentence per line.

SAMPLE INPUT

In the third category he included those Brothers (the majority) who saw nothing in Freemasonry but the external forms and ceremonies, and prized the strict performance of these forms without troubling about their purport or significance. Such were Willarski and even the Grand Master of the principal lodge. Finally, to the fourth category also a great many Brothers belonged, particularly those who had lately joined. These according to Pierre's observations were men who had no belief in anything, nor desire for anything, but joined the Freemasons merely to associate with the wealthy young Brothers who were influential through their connections or rank, and of whom there were very many in the lodge.Pierre began to feel dissatisfied with what he was doing. Freemasonry, at any rate as he saw it here, sometimes seemed to him based merely on externals. He did not think of doubting Freemasonry itself, but suspected that Russian Masonry had taken a wrong path and deviated from its original principles. And so toward the end of the year he went abroad to be initiated into the higher secrets of the order.What is to be done in these circumstances? To favor revolutions, overthrow everything, repel force by force?No! We are very far from that. Every violent reform deserves censure, for it quite fails to remedy evil while men remain what they are, and also because wisdom needs no violence. "But what is there in running across it like that?" said Ilagin's groom. "Once she had missed it and turned it away, any mongrel could take it," Ilagin was saying at the same time, breathless from his gallop and his excitement. 
SAMPLE OUTPUT

In the third category he included those Brothers (the majority) who saw nothing in Freemasonry but the external forms and ceremonies, and prized the strict performance of these forms without troubling about their purport or significance.
Such were Willarski and even the Grand Master of the principal lodge.
Finally, to the fourth category also a great many Brothers belonged, particularly those who had lately joined.
These according to Pierre's observations were men who had no belief in anything, nor desire for anything, but joined the Freemasons merely to associate with the wealthy young Brothers who were influential through their connections or rank, and of whom there were very many in the lodge.
Pierre began to feel dissatisfied with what he was doing.
Freemasonry, at any rate as he saw it here, sometimes seemed to him based merely on externals.
He did not think of doubting Freemasonry itself, but suspected that Russian Masonry had taken a wrong path and deviated from its original principles.
And so toward the end of the year he went abroad to be initiated into the higher secrets of the order.
What is to be done in these circumstances?
To favor revolutions, overthrow everything, repel force by force?
No!
We are very far from that.
Every violent reform deserves censure, for it quite fails to remedy evil while men remain what they are, and also because wisdom needs no violence.
"But what is there in running across it like that?" said Ilagin's groom.
"Once she had missed it and turned it away, any mongrel could take it," Ilagin was saying at the same time, breathless from his gallop and his excitement.
SCORING
We define precision and recall:

The F1-Score is the calculated as:

The score of the test case is test case weight multiplied by F1-Score.

The case and ordering of sentences in the output will not matter. Leading and trailing spaces will be ignored

---
## [AllyTally/VVVVVV](https://github.com/AllyTally/VVVVVV)@[86d90a1296...](https://github.com/AllyTally/VVVVVV/commit/86d90a1296739adef30b224f41e3a6ab55069a48)
#### Thursday 2022-11-17 04:02:29 by Misa

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
## [Sunrin-Social-Network/SSN-server](https://github.com/Sunrin-Social-Network/SSN-server)@[4bb0500f27...](https://github.com/Sunrin-Social-Network/SSN-server/commit/4bb0500f275b5be8539d54bfa89eca09c2469472)
#### Thursday 2022-11-17 06:36:25 by Hyunjun Yang

Merge pull request #16 from Sunrin-Social-Network/main

I HATE FUCKING SPRING

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[1c5ca1e6d9...](https://github.com/cyberitsolutions/bootstrap2020/commit/1c5ca1e6d977ead6816a7f2a7eb3f4b4e6fca334)
#### Thursday 2022-11-17 06:50:35 by Trent W. Buck

Use pipewire (not pulseaudio)

This fixes a persistent bug where if you tried to change volume while vlc was playing a video, sometimes (often!) pulseaudio would just crash.
pulseaudio would restart, but the already-open vlc would never make noises again.
To fix it you had to close and reopen vlc.

    pulseaudio:
    orc_code_region_allocate_codemem():
    Failed to create write and exec mmap regions.
    This is probably because SELinux execmem check is enabled (good) and $TMPDIR and $HOME are mounted noexec (bad).

Mike found that this is because Debian pipewire is compiled with --enable-orc.
That is https://github.com/GStreamer/orc and what it does is create new executables at runtime like
/tmp/orcexec.XXXXXX or /run/user/1000/orcexec.XXXXXX or ~/orcexec.XXXXXX
This is obviously banned on PrisonPC -- all user-writable areas are mounted -o noexec precisely to defeat this class of attack.

We probably could have solved this by recompiling pulseaudio with ./configure --disable-orc.

    https://sources.debian.org/src/pulseaudio/14.2-2/debian/control/#L26

However, we already had pipewire ready to go, and
we planned to switch to pipewire permanently in Debian 12.

The only reason to stick with pulseaudio for Debian 11 was that this commit is long and yukky.
But given that it fixes and actual user-visible and SUPER ANNOYING bug, fuck it, pipewire TODAY.

PS: pipewire does not use orc at all; it's not even in the codebase.

---
## [Sunrin-Social-Network/SSN-server](https://github.com/Sunrin-Social-Network/SSN-server)@[06678b3a89...](https://github.com/Sunrin-Social-Network/SSN-server/commit/06678b3a89cc8487d40b19f5d81aaabe3cca90f2)
#### Thursday 2022-11-17 06:52:59 by Hyunjun Yang

Merge pull request #17 from Sunrin-Social-Network/main

I HATE FUCKING SPRING

---
## [ODRI-the-human/Vampire-Pooers](https://github.com/ODRI-the-human/Vampire-Pooers)@[8d430fdf1a...](https://github.com/ODRI-the-human/Vampire-Pooers/commit/8d430fdf1a6da6dc9e6c49b153a0dc8715127d8e)
#### Thursday 2022-11-17 07:53:42 by ODRI-the-human

Pre-exam pooing

- As was always the intention, but I just hadn't bothered fixing it, the 8-direction enemies now don't change their firing angle based on where you are (meaning there's always safe positions at specific angles to the guys)
- 4-dir and 8-dir enemies now shoot slower.
- Stats on the UI are now rounded reasonably.
- Made it so you die if you're at less than 0.5 HP, cos otherwise it was possible to have like 0.00001 HP and be alive (despite UI saying 0 HP)
- Fixed cursed items giving enemies 2 of the item
- Made cursed items half as common
- The bonus food item now only activates on levels that are multiples of 4 as it used to essentially just be a free double item hack working 2022 no ads.

---
## [dl1109783/DDOBuilder](https://github.com/dl1109783/DDOBuilder)@[ef2462a008...](https://github.com/dl1109783/DDOBuilder/commit/ef2462a008df1e1ba421c8e20140221a07f5e985)
#### Thursday 2022-11-17 09:11:04 by Maetrim

1.0.0.106

Fix: "Pale Master: Necrotic Blast" now correctly requires 30 APs spent in tree to be selectable (Reported by nadia72295)
New: Special feats that control access to store/favor acquired universal trees have been removed from the Past Lives and Special feats view and moved to the Enhancements View
---Too many people were having trouble understanding where access to these trees was being granted
---How to guide updated
---The "Special" section has been renamed "Inherent"
Fix: "Legendary Robes of the Dreadkeeper" now has the release effects, not the Lamannia effects (Reported by mikameow)
Fix: "Purple Dragon Knight: Versatility I/II/III: Damage Boost" now has the correct description (Reported by Question2)
Fix: Missing +10 ranged power in "Inquisitive: No Holds Barred" when you have "Endless Fusilade" added (Reported by Question2)
Fix: Missing weapon fields for some effects in "Pale Master: Ascendant Shroud" added
Fix: The "Ursa's Heart" competence bonus to HP no longer stacks with other Competence bonuses to HP such as Epic Defensive Fighting (Reported by Ntoukis)
Fix: Feats which are alignment restricted will now be properly revoked on an alignment change when required (Reported by Laur)
Fix: "War Priest: Divine Power" no longer lists and grants a +1 competence bonus to Critical Multiplier (Reported by Laur)
Fix: Icons updated to remove red border:
---Superior Weapon Focus
---Brutal Throw
---Knights's Training
---Power Critical
---Spell Penetration
Fix: Gatekeepers favor icon changed to teleport icon for Gatekeepers Grove
Fix: "Drow: Xen'drik Weapon Training II" now correctly only has 1 rank, not 3 (Reported by crcabanillas)
Fix: "Child of Faith" now requires one of Cleric(3), Favored Soul(3) or Paladin(3) to be trained (Reported by crcabanillas)
Fix: Code efficiency update when searching for trained enhancements
Fix: "Warlock: Pact: Celestial" is now selectable by any non-chaotic alignment
Fix: "Inquisitive: Diplomatic Immunity" now has the correct AP cost of 2 (Reported by Question2)

U47: Preview 2
---New feat: "Favored enemy: Fey" (should also be available to rangers)
---All enhancements that affect "Rage" updated to affect Beasthide, Wildhunt and Razorclaw Rages (Not strength effects for Wildhunt)
---Shiter Race (+2 Dex, -2 Int)
------New trainiable feat type "Animalistic Aspect" at level 1 for Shifter race
----------Feat: Beasthide Shifter
----------Feat: Wildhunt Shifter
------Shifter racial past life feat (only give racial AP on tier 3, not yet required for Racial completionist)
------Racial tree
---Razerclaw Shifter Iconic Race (Barbarian)  (+2 Str, -2 Int)
------Feat: Razorclaw Shifter
------Iconic racial past life feat (no effects yet)
------Iconic racial tree
---Universal Enhancement Tree: Feydark Illusionist
------New feat special feat: Feydark Illusionist Tree
------Universal tree

---
## [dl1109783/DDOBuilder](https://github.com/dl1109783/DDOBuilder)@[7f8d3a6562...](https://github.com/dl1109783/DDOBuilder/commit/7f8d3a65626909dcb067b15973a420c5c798b6db)
#### Thursday 2022-11-17 09:11:04 by Maetrim

Build 1.0.0.122

Fix: Missing U48 item icons and "The Changestone" augments added. These were done for the last release, but I messed up with my source control and failed to include them.
Fix: "Legendary Tinkerer's Goggles" now correctly gives 15% melee alacrity (not 10) (Reported by Kamdragon)
Fix: "Legendary Enforcer's Coat" now has the correct max dex bonus of 10 (not 12) (Reported by Hoidx)
Fix: The "Haste" spells Melee Alacrity no longer stacks with other alacrity sources (Reported by Kamdragon)
Fix: "Vistani: Rapid Attack" will now show inactive entries for Doublstrike and Doubleshot
Fix: Spell "Angelskin" updated to match wiki description (Reported by Hoidx)
New: New DR types of Fire and Force added to support new weapons
New: Ruby of <element> 3d6/4d6/5d6/6d6/7d6 and 8d6 are now available
New: The drop list height displayed during augment selection for items has been increased for better selection
New: Augment tooltips during item setup now display the augments minimum level
Fix: The helmet "Compliance" now has the correct effects list (Reported by krizinja)
Fix: "The Heart of Suulomades" now has its Resistance +18 buff (Reported by krizinja)
Fix: Item "Legendary Fabricator's Bracers" can now correctly select +21 Constitution as one of its upgrade augments (Reported by krizinja)
Fix: "Hyrsam's Fiddle" now has its missing "Eminence of Winter" set bonus and its missing "Spellcasting Implement" bonus (Reported by krizinja)
Fix: The feat "Magical Training" now grants proficiency with orbs

New Items:
---Celestial Insignia (Necklace - feytwisted autumn)
---The Legendary Queen's Sceptre (Club)
---Staff of the Winter Solstice (Quarterstaff - feytwisted)
---The Obsidian Reaver (Dwarven War Axe - feytwisted)
---The Magamatic Cleaver (Great Axe - feytwisted)
---The Bitterstar (Morningstar - feytwisted)
---The Bitter Blade (Bastard Sword - feytwisted)
---Mirana of the Flame (Falchion - feytwisted)
---Rauven of the Frost (Longsword - feytwisted)
---Eidolon of the Shadow (Great Sword - feytwisted)
Set Bonus Images Harvested:
---Pain and Suffering

---
## [dl1109783/DDOBuilder](https://github.com/dl1109783/DDOBuilder)@[1cedd664c8...](https://github.com/dl1109783/DDOBuilder/commit/1cedd664c8af8943b227aa31254bd20d2c3c24c5)
#### Thursday 2022-11-17 09:11:04 by Maetrim

Build 1.0.0.110

Fix: Effects which add base ability modifiers like Strength for Reflex saves will no longer carry over from one character to the next (Reported by Kaustics)
Fix: Item "Tremor, the Breaker of Bones" now has the correct base critical profile of 20x3 (before Impact applied) not 19-20x2 (Reported by Seljuck-Cannith)
Fix: Pact Spell feats renamed from "Pact Spell <pact>: <Spell name>" to "Pact Magic: <spell name>" to match in game (Suggested by crcabanillas)
New: "Animal Growth" added as self and party buff option (Spell effects updated also) (Requested by Caarb)
New: Auto controlled stances for each Race added (Needed for Animal Growth effects)
New: Filigree selection can now be switched between the standard combo or menu selection method
---Menu selection is much quicker when you know what you want, but no tooltips
---Defaults to combo menu, remebers your choice
---How to guide updated
U47 Changes:
---Support for Tome of Destiny added
---Shifter Traits icon harvested
---Shifter tree updated to match live (version number updated)
---Razorclaw Shifter tree updated to match live
---Feydark Illusionist tree updated to match live
---Different Tack in the Swashbuckling bard tree now requires you to be Swashbuckling rather than Single Weapon Fighting.
---Fury of the Wild: Sense Weakness no longer provides untyped damage on hit, and instead now provides a flat +1 Damage per rank, for a total of +3 Damage.
---The Scion of the Feywild Legendary feat now grants +4 Illusion DCs instead of +2.
New Raid Filigrees:
---Zarigan's Arcane Enlightenment/Voltaic Experiment: +2 Intelligence
---Bravery Throughout/Shattered Device: +6 PRR
---Dance of the Wind/Next Fall: +2 Dexterity
---Soulweaver/Splendid Cacophony: +2 Constitution
---Sanctified Fervor/Reverberation: +2 Charisma
New U47 Items: (Note that all these items are set to min level 29, which may not be correct)
---Blightstaff (Quarterstaff)
---Handwraps of the Hound (Handwraps)
---Conqueror of Bone (Great Club)
---Dull Dagger (Dagger)             ***Does this item have hidden special effects?
---Vengeful Calamity (Large Shield) ***Does this item have hidden special effects?
---Tail of Suulomades (Falchion)
---Champion of the Twins (Large Shield)
---The Fang of Xyzzy (Trinket - Minor Artifact)
---The Heart of Suulomades (Trinket - Minor Artifact)
---Legendary Levik's Bracers (Bracers)
---Devilscale Bracers (Bracers)
---Legendary Tharne's Bracers (Bracers)
---Legendary Bracers of the Glacier (Bracers)
---Lamplighter (Morningstar)
---Legendary Gloves of the Glacier (Gloves)
---Legendary Omniscience (Ring)
---Legendary Lorik's Necklace (Necklace)
---Legendary Tumbleweed (Ring)
---Legendary Ring of Thelis (Ring)

---
## [dl1109783/DDOBuilder](https://github.com/dl1109783/DDOBuilder)@[a483f335fd...](https://github.com/dl1109783/DDOBuilder/commit/a483f335fd77ca8a87a5b3584325e2804a461b4a)
#### Thursday 2022-11-17 09:11:04 by Maetrim

Buile 1.0.0.116

New: The Inventory view now shows have many stacks of a given set bonus you have
---New section added to Inventory view to show set bonus stacks
---All items with a set bonus updated (186 items, ~300 augments - ouch)
---Tooltips added to show sets and stacks when required
---How To Guide updated
---Many Sets missing icons at this time
Fix: "Nature's Protector: Rage of the Beast" rage stance is now correctly incompatible with CE, Defensive Fighting and Precision (Reported by Erofen)
Fix: "Nature's Protector: Beast Unleashed" AC bonus will now only be active with Rage (Reported by Erofen)
Fix: "Nature's Protector: Lightning Strikes the Mountain" now grants a stance to show bonuses (Requested by Erofen)
Fix: Druid "Wolf, "Bear", "Winter Wolf" and "Dire Bear" descriptions and effects updated to match wiki (Reported by Erofen)
Fix: "Shadowdancer: Shadow Training III" now correctly applies -20% ranged threat (Reported by nymcraian)
Fix: A crash when selecting a bow without a preferred damage stat was fixed (Reported by ValkyrieDuskfire)
Fix: Illegal instructions on startup will o longer occur as COM is now initialised on startup
Fix: "Divine Crusader: Empyrean Magic" spell critical values should now apply correctly (Reported by Erofen)
Fix: "Spell Focus <School>" feats are no longer classed as alchemist bonus feats (Reported by Erofen)
---I also removed "Augment Summoning" from this list as not present on the list in the wiki
Fix: "Point Blank Shot" and "Simple Thrown Weapon Expertise" are now correctly classed as Alchemist bonus feats as per the wiki
Missing Items Added:
---Firefly Garb (Feytwisted - summer)

---
## [dl1109783/DDOBuilder](https://github.com/dl1109783/DDOBuilder)@[b4a5e7408c...](https://github.com/dl1109783/DDOBuilder/commit/b4a5e7408cb1f5fb29694aa250c73e8ffa258489)
#### Thursday 2022-11-17 09:11:04 by Maetrim

1.0.0.107

Fix: Shifter Core 4 now has the correct min AP spend requirement
Fix: Layout of some Feydark Illusionist tooltips fixed to make more readable
Fix: Feydark Illusionist tree now has the correct icon
Fix: "Past Life: Shifter" now has a shifter type icon
Fix: "Past Life: Razorclaw Shifter" now has a shifter type icon
Fix: Universal tree feats for the enhancement views are now correctly sorted alphabetically
Fix: The Inquisitive universal tree feat icon now matches the tree
Fix: The Falconry universal tree feat icon now matches the tree
Fix: "Dismiss Rage" is now auto assigned for Shifter and Razorclaw Shifter races at level 1
Fix: Razorclaw shifters now correctly get the feat "Exotic Weapon Proficiency: Handwraps"
Fix: Images fixed to remove red borders
---Improved Augment Summoning
---Epic Damage Reduction
---Epic Fortitude
---Epic Mental Toughness
---Epic Reputation
Fix: "Inquisitive: No Holds barred" now has the correct description (Reported by Question2)
Fix: Bad spell power name fixed in "Feydark Illusionist: Master Illusionist" effect
Fix: "Feydark Illusionist" tree can now be trained if you have "Magical Training" from any enhancement source also
---Arcane Archer: Energy of the Wild (and elf variant)
---Spellsinger: Studies - Magical Studies
---Aasimar: Celestial Tutelage - Magical Training
New: Enhancement requirements can now specify required number of ranks

---
## [dl1109783/DDOBuilder](https://github.com/dl1109783/DDOBuilder)@[a732c79b68...](https://github.com/dl1109783/DDOBuilder/commit/a732c79b68cb3b95e86e4045bc6f4da5e3b7e84f)
#### Thursday 2022-11-17 09:11:04 by Maetrim

Build 1.0.0.123

Fix: The item "The Changestone" now has the correct upgrade augments (Reported by cmecu)
Fix: Item "Icon of the Bitterwind" now has its missing +22 Intimidate and correct augment slots (Reported by Erofen)
Fix: Item "Legendary Winter Court Necklace" now gives a competence not a profane bonus to negative healing amplification (Reported by Erofen)
New: A new stance "Blocking" was added to allow effects to be toggled on when required (Requested by Erofen)
New: Slider added for "Deific Warding" (Requested by Erofen)
Fix: "Greater Rage" description and effects updated (Prompted by Strimtom build review comment)
Fix: "Tireless Rage" description and effects updated (Prompted by Strimtom build review comment)
Fix: Barbarian rage effects should now give the correct amount for str/con/will saves (will saves now correctly a Morale bonus also) at level 20 (Prompted by Strimtom build review comment)
Fix: "Indomitable Will" description updated
New: Augments that no longer exist are automatically "silently" cleared from items on file load (e.g. bad Changestone augments from this update)
Fix: Change in stacking rules. Effects of the same bonus type will now stack if one is a numeric amount and the other is a percentage increase. (Reported by Erofen)
New: Items that restrict other slot use will now work correctly (Currently only Platinum Knuckles does this) (Prompted by Strimtom build review comment)
---Visually shows slot as unavailable in inventory view
---Auto clears any item when equipping an item that restricts other slots
---Item tooltips updated to show that the item restricts the relevant slots
---Forum export says the slot is restricted due to other gear
Fix: Enhancement "Shifter: Exceptional Shifting" now correctly costs 1ap not 2, wiki also updated (Reported by Kerkos)
Fix: "Improved Feint" icon updated
Fix: The "Wildhunt Shifter" rage description now references the correct save (Will not Fortitude) when raging
Fix: "Pale Master: Corpsecrafter" is now correctly a requirement for "Pale Master: Eternal Furor" (Prompted by Strimtom build review comment)
New: Forum export of gear will list suppressed set bonuses on equipped items
New Items:
---Esper, the Shadowblade (Shortsword - feytwisted)
---Vivace, the Dreamcarver (Rapier - feytwisted)

---
## [warface1234455/tgstation](https://github.com/warface1234455/tgstation)@[db83f6498d...](https://github.com/warface1234455/tgstation/commit/db83f6498da37ecd25588ea3f7024409d2f3f117)
#### Thursday 2022-11-17 09:21:22 by vincentiusvin

Simplifies SM damage calculation, tweaks the numbers. (#70347)


About The Pull Request

We apply the damage hardcap individually now, split off the old flat 1.8 into individual caps for heat, moles, and power.

Set it to 1.5 for heat, 1 for mole and 1 for power. This means for most delams it'll be a tad slower! But its possible to make SM delam nearly twice as fast if you combine all 3. (3.5). Be pretty hard tho.

Set the heat healing to -1 so you can counteract one factor at most (except heat since you'll never get both heat healing and heat damage at the same time anyway).

I'm not hell bent on any of the numbers, just picked round even ones and ones that i think will make sense. If you want them changed lmk.

Got rid of the cascade mole and power multipliers since there's probably like three people that are aware that it even exists. Ideally we just add another entry to the CIMS but its already pretty crowded. Figured nobody is gonna miss it anyway? Sorry ghil.

Got rid of the moles multiplier thing since its nicer to keep the temp damage fully based on temp damage instead of adding another multiplier. I just applied the .25 to the damage flatly, meaning it slows down delams again!

And some space exposure stuff: #70347 (comment)
Why It's Good For The Game

Hardcap: Discrete, less randomly interconnected factors are easier to present and remember. The calculation procs are also made to be additive so we had to hack a bit and do some rescaling to accomodate the old behavior in my original PR #69240. Can remove the hack if this pr goes through.

Cascade and mole multiplier: The rest are just getting rid of underutilized factors so we have a cleaner behavior to maintain, present, and understand. (In a perfect world modifiers that aren't visible to the players shouldn't have been merged in the first place smh smh)
Changelog

🆑
fix: Fixed sm space exposure damage going through walls
del: got rid of the molar multiplier for sm heating damage. It will now only impact molar damage and temp limit. We apply the lowest value directly so this slows down sm delams a tiny bit.
del: got rid of cascades making sm delam at 450 moles and 1250 mev. It delams normally now.
balance: Applied the sm damage hardcap of 1.8 individually to heat (1.5), moles (1), power (1). Meaning most sm delams are slower now, but the really bad ones can be faster.
balance: Halved sm temp healing across the board. Temp limits are still the same though so you shouldn't notice it that much.
balance: Halved SM power damage across the board.
balance: Changed sm space exposure damage to just check for the current tile and adjacent atmos connected tiles.
/🆑

---
## [gitster/git](https://github.com/gitster/git)@[eb20e63f5a...](https://github.com/gitster/git/commit/eb20e63f5a96e24852c6ab1eca9f96af2648802f)
#### Thursday 2022-11-17 10:22:57 by Jeff King

branch: gracefully handle '-d' on orphan HEAD

When deleting a branch, "git branch -d" has a safety check that ensures
the branch is merged to its upstream (if any), or to HEAD. To do that,
naturally we try to resolve HEAD to a commit object. If we're on an
orphan branch (i.e., HEAD points to a branch that does not yet exist),
that will fail, and we'll bail with an error:

  $ git branch -d to-delete
  fatal: Couldn't look up commit object for HEAD

This usually isn't that big of a deal. The deletion would fail anyway,
since the branch isn't merged to HEAD, and you'd need to use "-D" (or
"-f"). And doing so skips the HEAD resolution, courtesy of 67affd5173
(git-branch -D: make it work even when on a yet-to-be-born branch,
2006-11-24).

But there are still two problems:

  1. The error message isn't very helpful. We should give the usual "not
     fully merged" message, which points the user at "branch -D". That
     was a problem even back in 67affd5173.

  2. Even without a HEAD, these days it's still possible for the
     deletion to succeed. After 67affd5173, commit 99c419c915 (branch
     -d: base the "already-merged" safety on the branch it merges with,
     2009-12-29) made it OK to delete a branch if it is merged to its
     upstream.

We can fix both by removing the die() in delete_branches() completely,
leaving head_rev NULL in this case. It's tempting to stop there, as it
appears at first glance that the rest of the code does the right thing
with a NULL. But sadly, it's not quite true.

We end up feeding the NULL to repo_is_descendant_of(). In the
traditional code path there, we call repo_in_merge_bases_many(). It
feeds the NULL to repo_parse_commit(), which is smart enough to return
an error, and we immediately return "no, it's not a descendant".

But there's an alternate code path: if we have a commit graph with
generation numbers, we end up in can_all_from_reach(), which does
eventually try to set a flag on the NULL commit and segfaults.

So instead, we'll teach the local branch_merged() helper to treat a NULL
as "not merged". This would be a little more elegant in in_merge_bases()
itself, but that function is called in a lot of places, and it's not
clear that quietly returning "not merged" is the right thing everywhere
(I'd expect in many cases, feeding a NULL is a sign of a bug).

There are four tests here:

  a. The first one confirms that deletion succeeds with an orphaned HEAD
     when the branch is merged to its upstream. This is case (2) above.

  b. Same, but with commit graphs enabled. Even if it is merged to
     upstream, we still check head_rev so that we can say "deleting
     because it's merged to upstream, even though it's not merged to
     HEAD". Without the second hunk in branch_merged(), this test would
     segfault in can_all_from_reach().

  c. The third one confirms that we correctly say "not merged to HEAD"
     when we can't resolve HEAD, and reject the deletion.

  d. Same, but with commit graphs enabled. Without the first hunk in
     branch_merged(), this one would segfault.

Reported-by: Martin von Zweigbergk <martinvonz@google.com>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [hexahigh/games](https://github.com/hexahigh/games)@[f310fc558d...](https://github.com/hexahigh/games/commit/f310fc558d44c26e2370468a5a491e3e99095d25)
#### Thursday 2022-11-17 11:26:50 by Boof

i fucking hate css, i want to rip my hair of my head because of it, why does it have to be so goddamn hard to just add a gradient backgound without it being completely worng, this is a warning to whoever made css: Im coming for your ass 🥵 (Joke)

---
## [dmenz/zulip](https://github.com/dmenz/zulip)@[23a776c144...](https://github.com/dmenz/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Thursday 2022-11-17 11:50:40 by Mateusz Mandera

maybe_send_to_registration: Don't reuse pre-existing PreregistraionUser.

There was the following bug here:
1. Send an email invite to a user.
2. Have the user sign up via social auth without going through that
   invite, meaning either going via a multiuse invite link or just
   straight-up Sign up if the org permissions allow.

That resulted in the PreregistrationUser that got generated in step (1)
having 2 Confirmations tied to it - because maybe_send_to_registration
grabbed the object and created a new confirmation link for it. That is a
corrupted state, Confirmation is supposed to be unique.

One could try to do fancy things with checking whether a
PreregistrationUser already have a Confirmation link, but to avoid races
between ConfirmationEmailWorker and maybe_send_to_registration, this
would require taking locks and so on - which gets needlessly
complicated. It's simpler to not have them compete for the same object.

The point of the PreregistrationUser re-use in
maybe_send_to_registration is that if an admin invites a user, setting
their initial streams and role, it'd be an annoying experience if the
user ends up signing up not via the invite and those initial streams
streams etc. don't get set up. But to handle this, we can just copy the
relevant values from the pre-existing prereg_user, rather than re-using
the object itself.

---
## [bobahop/rust](https://github.com/bobahop/rust)@[7a49959ea4...](https://github.com/bobahop/rust/commit/7a49959ea4aa3dbe3f5dd23a1de909196d62ea13)
#### Thursday 2022-11-17 12:00:01 by Remo Senekowitsch

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
## [GabrielePicco/CryptoBuzz](https://github.com/GabrielePicco/CryptoBuzz)@[62761d6d55...](https://github.com/GabrielePicco/CryptoBuzz/commit/62761d6d55e67ece29745cb55cd4dda21a5fbbf0)
#### Thursday 2022-11-17 13:29:31 by root

Adding article: Disgraced Sam Bankman-Fried blames his EX-GIRLFRIEND for FTX collapse and loss of $32BN - as he admits he lied about being moral and calls ethics a 'dumb game we woke Westerners play' (637636f5bd85b0e8cf44961b)

---
## [ianstormtaylor/superstruct](https://github.com/ianstormtaylor/superstruct)@[d9fc2ff0a7...](https://github.com/ianstormtaylor/superstruct/commit/d9fc2ff0a7af71ad7f1bc0aa10eb61806b75d9cc)
#### Thursday 2022-11-17 16:49:22 by Elliot Winkler

Support Node 14 (again) (#1112)

It appears that between 0.16.0 and 0.16.1, the minimum version of Node required
to use this package changed, from 14.x to 16.x. This was not explicit but seems
to have been caused by a couple of factors.

But first, what changed. If you look at `src/error.ts` in 0.16.0 you will see
[this line][1]:

```
return (cached ??= [failure, ...failures()])
```

In the [published version of this file in 0.16.0][2] this gets transpiled to:

```
return (_cached = cached) != null ? _cached : cached = [failure, ...failures()];
```

In 0.16.1, the [original line is unchanged][3], but in the [published
version][4] it is transpiled to:

```
return cached ??= [failure, ...failures()];
```

The `??=` syntax is not supported by Node 14, hence, developers are forced to
upgrade to at least Node 16 if they want to use v0.16.1 or greater.

After looking at the diff between these two versions and running some
experiments, I believe that there are two reasons why this line shows up
differently in these two published versions.

1. Different Node versions were used to build and publish these versions. It
appears that Node 14 was used for the former whereas Node 16 was used for the
latter. This assertion is supported by the fact that in the [Rollup
configuration][5], `@babel/preset-env` is configured with `node: true`, which
instructs Babel to [use the current version of Node as a target][6]. So if the
current Node version changes, so does the Babel config.
2. Between 0.16.0 and 0.16.1, [`browserslist` was updated from 4.20.3, to
4.21.4][7] (you will probably need to expand `yarn.lock`; if so, Cmd-F for
"browserslist"). In `browserslist` 4.21.0, [IE 11 was removed from the default
set of browsers][8] (which is being used in this case, since no explicit list is
provided). According to caniuse, [IE 11 does not support the `??=` syntax][9],
so its removal means that Babel doesn't need to transpile this syntax any
longer.

To address this problem, this PR:

* changes the Rollup configuration mentioned above to use `node: "14.0"` instead
of `node: true`, so that Node 14 is always used to compute the transpilation
rules regardless of the version of Node used locally to build and publish the
package
* updates the CI workflow to ensure that Node 14 is being tested (along with 16
and 18)
* adds Node >= 14 to the `engines` field to communicate that it is supported

---

One thing you may wonder is why this change is needed at all. Node 16 is the
current LTS, so shouldn't that be enough? True, but Node 14 hasn't hit
end-of-life yet, and many people are still using it, including my company. We
think this package is really great, but it would be even better if we didn't
have to have a workaround for our libraries that we still want to keep on Node
14.

Thanks for considering :)

[1]: https://github.com/ianstormtaylor/superstruct/blob/v0.16.0/src/error.ts#L44
[2]: https://unpkg.com/superstruct@0.16.0/lib/index.cjs
[3]: https://github.com/ianstormtaylor/superstruct/blob/v0.16.1/src/error.ts#L44
[4]: https://unpkg.com/superstruct@0.16.1/lib/index.cjs.js
[5]: https://github.com/ianstormtaylor/superstruct/blob/v0.16.4/config/rollup.js#L26
[6]: https://babel.dev/docs/en/options#targetsnode
[7]: https://github.com/ianstormtaylor/superstruct/compare/v0.16.0...v0.16.1?diff=unified#diff-51e4f558fae534656963876761c95b83b6ef5da5103c4adef6768219ed76c2deL99
[8]: https://github.com/browserslist/browserslist/blob/main/CHANGELOG.md#421
[9]: https://caniuse.com/?search=%3F%3F%3D

---
## [newstools/2022-iol-the-star](https://github.com/newstools/2022-iol-the-star)@[648c10c5f4...](https://github.com/newstools/2022-iol-the-star/commit/648c10c5f48a242601dd8fd8283c896712bef3e2)
#### Thursday 2022-11-17 16:55:38 by Billy Einkamerer

Created Text For URL [www.iol.co.za/the-star/the-star/news/the-soil-share-their-experiences-of-life-love-hardships-and-joy-cd7bbb82-8c2b-4485-afd1-eaec0cd46375]

---
## [Torpass/Parley](https://github.com/Torpass/Parley)@[1a33da4b28...](https://github.com/Torpass/Parley/commit/1a33da4b283a8a8524cbabc638e20f62d730375a)
#### Thursday 2022-11-17 18:27:42 by Torpass

More fuckins validations

validations validations validations

maybe I could do it better, but I think this is enough for the time I had, sorry if I did something wrong or outside of standards, but I'm so tired and I want to take a nap

the form's design it's not the best of thing, but i'm not so creative to do that

another things to improve is when you close the besibol crud, the data disappears and you need to put it again on the curd

---
## [Crumpaloo/Skyrat-tg](https://github.com/Crumpaloo/Skyrat-tg)@[1ba95626a6...](https://github.com/Crumpaloo/Skyrat-tg/commit/1ba95626a6614177da02665231900620bbaef2ce)
#### Thursday 2022-11-17 21:02:24 by SkyratBot

[MIRROR] mech bustin update 2022 [MDB IGNORE] (#17504)

* mech bustin update 2022 (#70891)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds a huge ass crowbar to robotics (the mech removal tool), it deals 5
damage unwielded, or 19 wielded. (should be fine, considering robotics
also has the easiest access to the materials needed for a chainsaw)
You can use it while wielded on mechs to break the occupants out. This
takes 5 seconds (or 3 in an unenclosed mech like a ripley)
When you die in a mech you no longer automatically get ejected.
refactors fire axe cabinets to support more items than the fireaxe
makes some vehicle code better
closes #70845 (you can still enter a mech without limbs, i think thats
fine because you can use it to protect yourself from death in a
dangerous situation or something until someone breaks you out with the
really large crowbar)
video: https://streamable.com/x4gom2

## Why It's Good For The Game

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->
robotics having a giant ass crowbar to break people out of mechs seems
like a fun idea
you currently cant exit a mech if youre incapacitated inside it unless
you DIE

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

:cl: Fikou, sprites by Halcyon
refactor: fire axe cabinets support items that aren't fire axes
balance: mechs no longer eject you when you die in them
add: Adds a giant crowbar to robotics, it can break open mechs to eject
their pilots.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* mech bustin update 2022

* vr for the love of god

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [david-rowley/postgres](https://github.com/david-rowley/postgres)@[8272749e8c...](https://github.com/david-rowley/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Thursday 2022-11-17 22:03:53 by Tom Lane

Record dependencies of a cast on other casts that it requires.

When creating a cast that uses a conversion function, we've
historically allowed the input and result types to be
binary-compatible with the function's input and result types,
rather than necessarily being identical.  This means that the new
cast is logically dependent on the binary-compatible cast or casts
that it references: if those are defined by pg_cast entries, and you
try to restore the new cast without having defined them, it'll fail.
Hence, we should make pg_depend entries to record these dependencies
so that pg_dump knows that there is an ordering requirement.

This is not the only place where we allow such shortcuts; aggregate
functions for example are similarly lax, and in principle should gain
similar dependencies.  However, for now it seems sufficient to fix
the cast-versus-cast case, as pg_dump's other ordering heuristics
should keep it out of trouble for other object types.

Per report from David Turoň; thanks also to Robert Haas for
preliminary investigation.  I considered back-patching, but
seeing that this issue has existed for many years without
previous reports, it's not clear it's worth the trouble.
Moreover, back-patching wouldn't be enough to ensure that the
new pg_depend entries exist in existing databases anyway.

Discussion: https://postgr.es/m/OF0A160F3E.578B15D1-ONC12588DA.003E4857-C12588DA.0045A428@notes.linuxbox.cz

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[317aea0435...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/317aea043510ee0c3591ff3a06fdffd360fdfc29)
#### Thursday 2022-11-17 22:07:59 by Jolly

[FUCK] [NO GBP] Yeah, fixes something in NuInterlink(?) (#17544)

fucking GODDAMNIT

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[1d592ba974...](https://github.com/treckstar/yolo-octo-hipster/commit/1d592ba9748e02ea92d3a34c7c3bb10e1427a814)
#### Thursday 2022-11-17 22:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[85b2d5043d...](https://github.com/Comxy/tgstation/commit/85b2d5043dbc9eb277bf57dd6dc5147ae08fe978)
#### Thursday 2022-11-17 23:39:48 by LemonInTheDark

Optimizes qdel related things (slight init time savings) (#70729)

* Moves spawners and decals to a different init/delete scheme

Rather then fully creating and then immediately deleting these things,
we instead do the bare minimum.

This is faster, if in theory more fragile. We should be safe since any
errors should be caught in compile since this is very close to a
"static" action. It does mean these atoms cannot use signals, etc.

* Potentially saves init time, mostly cleans up a silly pattern

We use sleeps and INVOKE_ASYNC to ensure that handing back turfs doesn't
block a space reservation, but this by nature consumes up to the
threshold and a bit more of whatever working block we were in.

This is silly. Should just be a subsystem, so I made it one, with
support for awaiting its finish if you want to

* Optimizes garbage/proc/Queue slightly

Queue takes about 1.6 seconds to process 26k items right now.
The MASSIVE majority of this time is spent on using \ref
This is because \ref returns a string, and that string requires being
inserted into the global cache of strings we store

What I'm doing is caching the result of ANY \ref on the datum it's
applied to. This ensures previous uses will never decay from the string
tree.

This saves about 0.2 seconds of init

---

