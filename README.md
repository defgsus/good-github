## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-18](docs/good-messages/2022/2022-11-18.md)


2,144,951 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,144,951 were push events containing 3,153,829 commit messages that amount to 260,072,093 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [sjp38/linux](https://github.com/sjp38/linux)@[9721a7b57a...](https://github.com/sjp38/linux/commit/9721a7b57aafd859312b906ef9604a1198f99eb8)
#### Friday 2022-11-18 00:01:17 by Johannes Weiner

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
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[3c187487b1...](https://github.com/lizardqueenlexi/orbstation/commit/3c187487b1884040608ba23b0a89aa8b0176c2aa)
#### Friday 2022-11-18 00:01:32 by MrMelbert

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
## [CSC207-2022F-UofT/course-project-team-communify](https://github.com/CSC207-2022F-UofT/course-project-team-communify)@[d2cd0893c1...](https://github.com/CSC207-2022F-UofT/course-project-team-communify/commit/d2cd0893c1c885bfecf5e8c4eee680a8e14e4a17)
#### Friday 2022-11-18 00:28:11 by clin1967

Song Database Implementation: songLibrary, songDsData, bits and pieces.

Pull includes the implementation of everything relating to Song's database: mainly songLibrary and songDsData. Brief summary;

- **Uploaded the standard library of songs.** Currently located in the new folder songLib under src. Any test cases or other pieces of code that currently create new instances of Songs should likely be re-reviewed with this in mind. I already fixed a few, but I might've missed some.

- Updated build.gradle to include jaudiotagger

- Updated Song entity to include username of uploading user.

- Reading/saving from songs.csv, formatted as `ID, uploader, filepath`

- Changed artistList from List<String> to String[]

- Removed 'length' as Jaudiotagger cannot retrieve it. If we want to show it, it would be on the Jlayer side. Better suited this way, anyway.

- Removed isExplicit. Too much of a pain for too little gain.

- changed saveSong to return a boolean for a successful song addition.

- Created Test file for SongLibrary.

KNOWN ISSUES

- createFile() assumes the existence of a user admin, as it assigns all songs currently in songLib /to/ admin. (This was only important for creating songs.csv from scratch. It won't do this now that it exists.)

- Many files don't have album covers. I'll be creating default covers to put in the BufferedImage parameter later. I don't think anyone is at that stage (which is why I'm putting it off for a later PR), but please don't try accessing the BufferedImage parameter until I do.

- When parsing ID names, the 0s at the beginning of the names are omitted. Theoretically, this shouldn't create duplicate IDs anyway, as 1) what's being checked is the parsed ID, and 2) randInt will not create more IDs that start with 0. I'll go back and rename the files to omit the 0s (not that difficult), but I figure its lower priority due to the reasons I stated.

- Need to implement safeguard against improperly formatted mp3s (ex. missing genre). There currently aren't any, so it should be temporarily OK, but I have some code smells because of this.

Making this a PR despite this so you guys have a better SONG_LIBRARY to work with for now.

---
## [newstools/2022-metro](https://github.com/newstools/2022-metro)@[c61b40d0f3...](https://github.com/newstools/2022-metro/commit/c61b40d0f3da5308ef66a3c7392030fd7d637303)
#### Friday 2022-11-18 01:12:21 by Billy Einkamerer

Created Text For URL [metro.co.uk/2022/11/17/man-so-annoyed-about-30p-asda-bags-he-is-sick-with-stress-and-wants-a-boycott-17776566/]

---
## [david-rowley/postgres](https://github.com/david-rowley/postgres)@[8272749e8c...](https://github.com/david-rowley/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Friday 2022-11-18 01:15:21 by Tom Lane

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
## [ATH1909/tgstation](https://github.com/ATH1909/tgstation)@[25d4afc869...](https://github.com/ATH1909/tgstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Friday 2022-11-18 01:17:20 by Iamgoofball

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
## [joshrose/guava](https://github.com/joshrose/guava)@[8a676ade61...](https://github.com/joshrose/guava/commit/8a676ade617c6be992165cd0658779a14acef2f2)
#### Friday 2022-11-18 01:32:39 by cpovirk

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
## [Zenitheevee/Skyrat-tg](https://github.com/Zenitheevee/Skyrat-tg)@[317aea0435...](https://github.com/Zenitheevee/Skyrat-tg/commit/317aea043510ee0c3591ff3a06fdffd360fdfc29)
#### Friday 2022-11-18 02:08:28 by Jolly

[FUCK] [NO GBP] Yeah, fixes something in NuInterlink(?) (#17544)

fucking GODDAMNIT

---
## [Navaesk/Modified-modifications](https://github.com/Navaesk/Modified-modifications)@[2f2d0c6b1d...](https://github.com/Navaesk/Modified-modifications/commit/2f2d0c6b1d314de3fa7d7defb1c7b47af48359ad)
#### Friday 2022-11-18 02:27:21 by Navaesk

New overhaul

Balanced everything, took out every unicorn piece of shit this mod is now just a fuck you add on to the experience even if the most basic unit here outdoes every vanilla unit, no more basic RTS, this copies wargame red dragon alot as well as some other games that I took inspiration from

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[82fc8c522e...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/82fc8c522e50ccabd853493afaee43f76930529c)
#### Friday 2022-11-18 02:39:43 by SkyratBot

[MIRROR] Excercise Equipment is now craftable [MDB IGNORE] (#17495)

* Excercise Equipment is now craftable (#71190)

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

* Excercise Equipment is now craftable

Co-authored-by: Sol N <116288367+flowercuco@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[84a85c827d...](https://github.com/tgstation/tgstation/commit/84a85c827d71b3326b482444a204711de38cf518)
#### Friday 2022-11-18 03:00:10 by lizardqueenlexi

Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation. (#71157)

## About The Pull Request

Resolves #67282.

As originally designed, plasma rivers (namely, those on Icebox, though
the turf was originally made for the Snowdin away mission) are meant to
literally strip the flesh from your bones, leaving you with plasmaman
limbs. I'm not certain when this broke entirely, although it seems to
have never been updated to work alongside Kapulimbs.

Transformation of limbs into plasmaman limbs used to be accomplished by
adding the "PLASMABURNT" trait to limbs. However, this trait in the
current code is entirely meaningless, only checked in the proc that
makes plasmamen catch fire. Essentially, the only "interaction" is
having your flesh melted off by a plasma river, donating that specific
limb to a plasmaman, and pranking them with the fact that that specific
limb will still make them burst into flames.

Exciting.

I've removed the trait entirely, as it does functionally nothing, and
restored the ability of plasma rivers to turn your limbs - and
eventually, you - into plasmaman equivalents.

To be honest, I'm not _entirely_ satisfied with the plasmaman
transformation process - it doesn't especially suit the lore of
plasmamen, and if you transform into one in the plasma rivers you'll
probably immediately die from Icemoon's atmosphere anyway. However, this
is something I'd prefer to revisit in a later PR.
## Why It's Good For The Game

There's little reason _not_ to remove a trait that does nothing.

As for plasmafication, it's a fun interaction that was already _meant_
to be there. The message about your flesh melting off has always
printed, even while it's doing exactly nothing to you. It's cool to fall
into the deadly plasma river and come away from it permanently scarred
with a weird skeleton limb. Turning into a plasmaman entirely is
unlikely to happen and will probably just kill you, but it's a fun and
weird way to be dead.
## Changelog
:cl:
del: Removed the useless "plasmaburnt" trait.
fix: Restored a broken interaction with plasma rivers that slowly
transforms you into a plasmaman.
/:cl:

---
## [Conga0/Mo_Creeps](https://github.com/Conga0/Mo_Creeps)@[0801c47faf...](https://github.com/Conga0/Mo_Creeps/commit/0801c47faf285f0354969405d7963d1b15da6016)
#### Friday 2022-11-18 05:42:46 by Conga Lyne

New Creep, Balance Changes

You can now deliver the Essence of Fungus to lunar bodies
Expanded the statue room to include trophys for new achievements
Greatly increased time between Psychic Bat's delusion attempts, it should now take 5 seconds between each attempt instead of 2, this should hopefully make them less frustrating enemies to fight against and make trying to avoid the attack feel more worth it instead of giving the feeling that you'll just be hit again anyways
Drastically reduced lifetime of Mass Status spells, this is not the actual effect duration but the projectile lifetime, previously if you gave a mass status spell a modifier like water trail for example, it would linger a very long time and create a lot of water
Fixed Colossal Blob boss not dropping loot
Added modded powders to Dissolve Powder's list
Reworked Masters of Immortality, they now no longer provide an unconcditional 20 seconds of Ambrosia, but rather cover their target with an Ambrosia stain, this should introduce the option of counterplay by using stain inflicting spells, such as Mass Wet, Water Trail or other means.
Modified Hideous Mass ragdolls to now include their limbs
Decreased spawnrate of Holy Orb Barrage, it should now be slightly rare overall, previously I felt like I could consistently find it every run down the main path and it felt excessively present for how good it is
Reduced Delusion's duration to 45 seconds, previously it felt too long but putting it down to 30 seconds felt like the effect would expire before it had a chance to trick you, hopefully 45 seconds will strike a balance between lasting long enough to trick you and being short enough to go away once the effect has done it's business.
New Creep: Reflective Weirdo

---
## [ccanandmallik/ruminations](https://github.com/ccanandmallik/ruminations)@[7d1a26a3ee...](https://github.com/ccanandmallik/ruminations/commit/7d1a26a3eec60acf69fed506c3d707d0f4c8ce70)
#### Friday 2022-11-18 06:03:49 by Anand Mallik

hey everyone -- I'm not in a great place, but, financially speaking I've gotten a bit more wiggle room so I can extend my timeline a bit. I'll still keep hurting Elon's feelings from a distance aka utilizing not my freedom of speech but I think my basic property rights to this github etc which is funny and keeps my spirits up greatly (being mean to Elon) during these trying times -- also, I didnt want to mess up anyone's thanksgiving plans, I had none, and will continue to have none on that day. Thanks!

---
## [queercpu/script](https://github.com/queercpu/script)@[1ea3edc923...](https://github.com/queercpu/script/commit/1ea3edc9234caacad58606e3fa5a712b7b72026b)
#### Friday 2022-11-18 06:10:45 by home.cpu

bascially went completely broke today or, we are at a very low level of funds.. its scary, but im trying hard to not let it get to me. it does a little bit, i feel a fire under my ass, a fire to start my own social media and get people away from twitter, to become more empowered as an individual, to try and build a village with artists and support one another, to tell people to stop eating shti from up there, maybe the sane thing would be imma go work as a waitressgit add .! but fuck that, i wrote script today... it was hard. i wrote the dinner scene. i started to feel doubt again. the things my characters say, sometimes i feel shocked by it, there are times where im like ok this is real but then im like, i think im reacting to them... because their opinions and views are stronger than they were before, mom feels extra hardline, the pressure on twigs feels greater. perhaps thats a good thing, in a way its not totally realistic its not my real parents,s teve and debbie are taking on their own forms... i had weird hallucinations of stupid disney hollywood movie vibes with the bird zapping around the room and it feels so nonsense and fake sommehow like slapstick and grandmas head is whipping around , like a harry potter scene with his fake  familyand owls running around. just stupid nonsense... jibbery josh, the bird can be removed, but it gives me a good excuse to remind the reader about the impending sense of doom and being targeted... its just the 5g that made the bird do that... so im just stonde and paranoid a little and we are feeling strange moods today about the climate of social media....and whatever... i wrote a huge blog post and didnt share, that was anxiety ridden, but also feeling a calling, like I feel like things feel like its gonna get serious for us, we have to take action as artists in the name of protecting our asses, we have to take action to put our lives more into our control... and we have to make sure we can spread the word about what we do,,, if we lose the big sm platforms for promo, we have to go somehwere, and we should go  somewhere were we are the bosses... dnno what will go down but we spoke about it at the dinner table... i told sofa straight we can't go live in someone elses house we have to build our own thats what we are good at so we should build one to prepare for this.

---
## [abhishek1994-ux/-MyCloudDiary](https://github.com/abhishek1994-ux/-MyCloudDiary)@[b26efe4a9e...](https://github.com/abhishek1994-ux/-MyCloudDiary/commit/b26efe4a9ec702e715b5f67eb069a504cfe40f79)
#### Friday 2022-11-18 08:10:10 by Abhishek Shrivastava

Google Cloud Certified Cloud Digital Leader

Cloud Digital Leader tests your understanding about Google cloud services.

Exam will test your ability to choose right services for the given situation.

If you are starting out, it’s recommended to give yourself a month of time.

Preparation materials

freeCodeCamp

’s YouTube Video

Priyanka Vergadia

’s Sketch book If you are book reading person, you will love the material

Priyanka’s YouTube Video Collections will be very useful companion for the exam.

CourseEra’s course on Cloud Digital Leader. I have used only the quiz part to check whether my preparation was enough.

Here’s my Cloud Digital Leader Credentials. All the best for your cloud journey. Feel free to connect at LinkedIn.

Happy to share 🙂
New badges added in #MyCloudDiary :: https://lnkd.in/dHAMiTcH ..

First one for this year — Welcome 2023 ! Looking forward to many more :)Thanks to a few late nights and great support from my employer Google, pleased to share with my network my first official licensed Google Certificate — Google Cloud Certified Cloud Digital Leader.

Becoming a certified Cloud Digital Leader opened my eyes to the Google Cloud technologies that I benefit from every day. The products are no longer just a name. They’re now understood, recognized, and appreciated as problem-solving, innovation driving, and mind-blowing solutions. I challenge anyone that works for an organization who has embraced Google Cloud to become the next Google Cloud #certifiedclouddigitalleader

You can find more about the certifications and training materials below:
Learning: https://lnkd.in/djeWCw7x
About certification: https://lnkd.in/dp39CXBN
Google Cloud Certification Credential Holder Directory : https://lnkd.in/dKeKuxQe

#cloudJourney #googleCertification #googleCloudPlatform #google #googlecloud Google Google Cloud Community India

Please like ,share and subscribe below #channelpartners on
YouTube :: https://lnkd.in/dDaZPGR5
GitHub :: https://lnkd.in/dHAMiTcH
Hashnode :: https://lnkd.in/d_gtGxuS
Twitter :: https://lnkd.in/e5ZY5j-x
Dev Code Community TLV :: https://lnkd.in/duMEcSnc
Tealfeed :: https://lnkd.in/eTyp-Xe4
Medium :: https://lnkd.in/dpEzM8GU

❤️The trouble with not having a goal is that you can spend your life running up and down the field and never score.🎓🎓

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[049ab89197...](https://github.com/GeoB99/reactos/commit/049ab89197e0effdf40e568305669a88fb24a888)
#### Friday 2022-11-18 10:01:17 by George Bișoc

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
## [saivineeth100/odoo_src](https://github.com/saivineeth100/odoo_src)@[1636ba5ed2...](https://github.com/saivineeth100/odoo_src/commit/1636ba5ed2f8a284bef0930313a85cc3dc7cf072)
#### Friday 2022-11-18 10:09:06 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: website_sale

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with a specific JS patch, we'll review to see if
better can be done in master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

Note: as a forward-ported fix, this also takes the opportunity to clean
a bit what was done at [3]. (calling `_super`, no duplicated code,
adding comments, ...).

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3
[3]: https://github.com/odoo/odoo/commit/e2f7b8fad76dc816b2f6864340d3740446117cdb

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104335

X-original-commit: 61270ee8bffb6e85f8ff0d19c7a3889fdce2f486
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [laurynmm/zulip](https://github.com/laurynmm/zulip)@[23a776c144...](https://github.com/laurynmm/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Friday 2022-11-18 10:12:53 by Mateusz Mandera

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
## [anderseknert/opa](https://github.com/anderseknert/opa)@[965301f90e...](https://github.com/anderseknert/opa/commit/965301f90e1c10900c2c134ee21e486993796a20)
#### Friday 2022-11-18 11:08:18 by Stephan Renatus

ast: support dotted heads (#4660)

This change allows rules to have string prefixes in their heads -- we've
come to call them "ref heads".

String prefixes means that where before, you had

    package a.b.c
    allow = true

you can now have

    package a
    b.c.allow = true

This allows for more concise policies, and different ways to structure
larger rule corpuses.

Backwards-compatibility:

- There are code paths that accept ast.Module structs that don't necessarily
  come from the parser -- so we're backfilling the rule's Head.Reference
  field from the Name when it's not present.
  This is exposed through (Head).Ref() which always returns a Ref.

  This also affects the `opa parse` "pretty" output:

  With x.rego as

    package x
    import future.keywords
    a.b.c.d if true
    e[x] if true

  we get

    $ opa parse x rego
    module
     package
      ref
       data
       "x"
     import
      ref
       future
       "keywords"

     rule
      head
       ref
        a
        "b"
        "c"
        "d"
       true
      body
       expr index=0
        true
     rule
      head
       ref
        e
        x
       true
      body
       expr index=0
        true

  Note that

    Name: e
    Key: x

  becomes

    Reference: e[x]

  in the output above (since that's how we're parsing it, back-compat edge cases aside)

- One special case for backcompat is `p[x] { ... }`:

    rule                    | ref   | key | value | name
    ------------------------+-------+-----+-------+-----
    p[x] { ... }            | p     | x   | nil   | "p"
    p contains x if { ... } | p     | x   | nil   | "p"
    p[x] if { ... }         | p[x]  | nil | true  | ""

  For interpreting a rule, we now have the following procedure:

  1. if it has a Key, it's a multi-value rule; and its Ref defines the set:

     Head{Key: x, Ref: p} ~> p is a set
     ^-- we'd get this from `p contains x if true`
         or `p[x] { true }` (back compat)

  2. if it has a Value, it's a single-value rule; its Ref may contain vars:

     Head{Ref: p.q.r[s], Value: 12} ~> body determines s, `p.q.r.[s]` is 12
     ^-- we'd get this from `p.q.r[s] = 12 { s := "whatever" }`

     Head{Key: x, Ref: p[x], Value: 3} ~> `p[x]` has value 3, `x` is determined
                                          by the rule body
     ^-- we'd get this from `p[x] = 3 if x := 2`
         or `p[x] = 3 { x := 2 }` (back compat)

     Here, the Key isn't used, it's present for backwards compatibility: for ref-
     less rule heads, `p[x] = 3` used to be a partial object: key x, value 3,
     name "p"

- The destinction between complete rules and partial object rules disappears.
  They're both single-value rules now.

- We're now outputting the refs of the rules completely in error messages, as
  it's hard to make sense of "rule r" when there's rule r in package a.b.c and
  rule b.c.r in package a.

Restrictions/next steps:

- Support for ref head rules in the REPL is pretty poor so far. Anything that
  works does so rather accidentally. You should be able to work with policies
  that contain ref heads, but you cannot interactively define them.
  
  This is because before, we'd looked at REPL input like

      p.foo.bar = true

  and noticed that it cannot be a rule, so it's got to be a query. This is no
  longer the case with ref heads.

- Currently vars in Refs are only allowed in the last position. This is expected
 to change in the future.

- Also, for multi-value rules, we can not have a var at all -- so the following
  isn't supported yet:

      p.q.r[s] contains t if { ... }

-----

Most of the work happens when the RuleTree is derived from the ModuleTree -- in
the RuleTree, it doesn't matter if a rule was `p` in `package a.b.c` or `b.c.p`
in `package a`.

As such, the planner and wasm compiler hasn't seen that many adaptations:

- We're putting rules into the ruletree _including_ the var parts, so

  p.q.a = 1
  p.q.[x] = 2 { x := "b" }

  end up in two different leaves:

  p
  `-> q
       `-> a = 1
       `-> [x] = 2`

- When planing a ref, we're checking if a rule tree node's children have
  var keys, and plan "one level higher" accordingly:

  Both sets of rules, p.q.a and p.q[x] will be planned into one function
  (same as before); and accordingly return an object {"a": 1, "b": 2}

- When we don't have vars in the last ref part, we'll end up planning
  the rules separately. This will have an effect on the IR.

  p.q = 1
  p.r = 2

  Before, these would have been one function; now, it's two. As a result,
  in Wasm, some "object insertion" conflicts can become "var assignment
  conflicts", but that's in line with the now-new view of "multi-value"
  and "single-value" rules, not partial {set/obj} vs complete.
* planner: only check ref.GroundPrefix() for optimizations

In a previous commit, we've only mapped

    p.q.r[7]

as p.q.r;  and as such, also need to lookup the ref

    p.q.r[__local0__]

via p.q.r

(I think. Full disclosure: there might be edge cases here that are unaccounted
for, but right now, I'm aiming for making the existing tests green...)


New compiler stage:

In the compiler, we're having a new early rewriting step to ensure that the
RuleTree's keys are comparible. They're ast.Value, but some of them cause us
grief:

- ast.Object cannot be compared structurally; so

      _, ok := map[ast.Value]bool{ast.NewObject([2]*ast.Term{ast.StringTerm("foo"), ast.StringTerm("bar")}): true}[ast.NewObject([2]*ast.Term{ast.StringTerm("foo"), ast.StringTerm("bar")})]

  `ok` will never be true here.

- ast.Ref is a slice type, not hashable, so adding that to the RuleTree would
  cause a runtime panic:

      p[y.z] { y := input }

  is now rewritten to

    p[__local0__] { y := input; __local0__ := y.z }

This required moving the InitLocalVarGen stage up the chain, but as it's still
below ResolveRefs, we should be OK.

As a consequence, we've had to adapt `oracle` to cope with that rewriting:

1. The compiler rewrites rule head refs early because the rule tree expects
   only simple vars, no refs, in rule head refs. So `p[x.y]` becomes
   `p[local] { local = x.y }`
2. The oracle circles in on the node it's finding the definition for based
   on source location, and the logic for doing that depends on unaltered
   modules.

So here, (2.) is relaxed: the logic for building the lookup node stack can
now cope with generated statements that have been appended to the rule bodies.


There is a peculiarity about ref rules and extents:

See the added tests: having a ref rule implies that we get an empty object
in the full extent:

    package p
    foo.bar if false

makes the extent of data.p: {"foo": {}}

This is somewhat odd, but also follows from the behaviour we have right now
with empty modules:

    package p.foo
    bar if false

this also gives data.p the extent {"foo": {}}.

This could be worked around by recording, in the rule tree, when a node was
added because it's an intermediary with no values, but only children.

Signed-off-by: Stephan Renatus <stephan.renatus@gmail.com>

---
## [KingOfThePing/Shiptest](https://github.com/KingOfThePing/Shiptest)@[3efa9b5382...](https://github.com/KingOfThePing/Shiptest/commit/3efa9b538241ffef48ddf1fe102feb589e88dff0)
#### Friday 2022-11-18 11:19:59 by Zevotech

undoes a fuckup on a ruin (#1578)

* undoes a fuckup on a ruin
<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull request process. -->

## About The Pull Request
sets light range to 2 on the ruin areas of beach_colony.dmm
<!-- Describe The Pull Request. Please be sure every change is documented or this can delay review and even discourage maintainers from merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the brackets) if you have tested your changes and this is ready for review. Leave unticked if you have yet to test your changes and this is not ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that any issues found during tested have been addressed.

## Why It's Good For The Game
the ruin is no longer pitch fucking dark in the middle of a daylit planet (hopefully)
<!-- Please add a short description of why you think these changes would benefit the game. If you can't justify it in words, it might not be worth adding. -->

## Changelog

:cl:
fix: changes light range to 2 on the areas of beach_colony
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put your name to the right of the first :cl: if you want to overwrite your GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the icon ingame) and delete the unneeded ones. Despite some of the tags, changelogs should generally represent how a player might be affected by the changes rather than a summary of the PR's contents. -->

* im stupid

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[e88c1efdf1...](https://github.com/treckstar/yolo-octo-hipster/commit/e88c1efdf1b6ab663d1588efe4f39a240d5a39cf)
#### Friday 2022-11-18 11:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [tachicialex/linux-fslc](https://github.com/tachicialex/linux-fslc)@[b547cc1d46...](https://github.com/tachicialex/linux-fslc/commit/b547cc1d461c267d723cfdfbf0814c4889758bc0)
#### Friday 2022-11-18 11:28:18 by Masahiro Yamada

kbuild: remove the target in signal traps when interrupted

[ Upstream commit a7f3257da8a86b96fb9bf1bba40ae0bbd7f1885a ]

When receiving some signal, GNU Make automatically deletes the target if
it has already been changed by the interrupted recipe.

If the target is possibly incomplete due to interruption, it must be
deleted so that it will be remade from scratch on the next run of make.
Otherwise, the target would remain corrupted permanently because its
timestamp had already been updated.

Thanks to this behavior of Make, you can stop the build any time by
pressing Ctrl-C, and just run 'make' to resume it.

Kbuild also relies on this feature, but it is equivalently important
for any build systems that make decisions based on timestamps (if you
want to support Ctrl-C reliably).

However, this does not always work as claimed; Make immediately dies
with Ctrl-C if its stderr goes into a pipe.

  [Test Makefile]

    foo:
            echo hello > $@
            sleep 3
            echo world >> $@

  [Test Result]

    $ make                         # hit Ctrl-C
    echo hello > foo
    sleep 3
    ^Cmake: *** Deleting file 'foo'
    make: *** [Makefile:3: foo] Interrupt

    $ make 2>&1 | cat              # hit Ctrl-C
    echo hello > foo
    sleep 3
    ^C$                            # 'foo' is often left-over

The reason is because SIGINT is sent to the entire process group.
In this example, SIGINT kills 'cat', and 'make' writes the message to
the closed pipe, then dies with SIGPIPE before cleaning the target.

A typical bad scenario (as reported by [1], [2]) is to save build log
by using the 'tee' command:

    $ make 2>&1 | tee log

This can be problematic for any build systems based on Make, so I hope
it will be fixed in GNU Make. The maintainer of GNU Make stated this is
a long-standing issue and difficult to fix [3]. It has not been fixed
yet as of writing.

So, we cannot rely on Make cleaning the target. We can do it by
ourselves, in signal traps.

As far as I understand, Make takes care of SIGHUP, SIGINT, SIGQUIT, and
SITERM for the target removal. I added the traps for them, and also for
SIGPIPE just in case cmd_* rule prints something to stdout or stderr
(but I did not observe an actual case where SIGPIPE was triggered).

[Note 1]

The trap handler might be worth explaining.

    rm -f $@; trap - $(sig); kill -s $(sig) $$

This lets the shell kill itself by the signal it caught, so the parent
process can tell the child has exited on the signal. Generally, this is
a proper manner for handling signals, in case the calling program (like
Bash) may monitor WIFSIGNALED() and WTERMSIG() for WCE although this may
not be a big deal here because GNU Make handles SIGHUP, SIGINT, SIGQUIT
in WUE and SIGTERM in IUE.

  IUE - Immediate Unconditional Exit
  WUE - Wait and Unconditional Exit
  WCE - Wait and Cooperative Exit

For details, see "Proper handling of SIGINT/SIGQUIT" [4].

[Note 2]

Reverting 392885ee82d3 ("kbuild: let fixdep directly write to .*.cmd
files") would directly address [1], but it only saves if_changed_dep.
As reported in [2], all commands that use redirection can potentially
leave an empty (i.e. broken) target.

[Note 3]

Another (even safer) approach might be to always write to a temporary
file, and rename it to $@ at the end of the recipe.

   <command>  > $(tmp-target)
   mv $(tmp-target) $@

It would require a lot of Makefile changes, and result in ugly code,
so I did not take it.

[Note 4]

A little more thoughts about a pattern rule with multiple targets (or
a grouped target).

    %.x %.y: %.z
            <recipe>

When interrupted, GNU Make deletes both %.x and %.y, while this solution
only deletes $@. Probably, this is not a big deal. The next run of make
will execute the rule again to create $@ along with the other files.

[1]: https://lore.kernel.org/all/YLeot94yAaM4xbMY@gmail.com/
[2]: https://lore.kernel.org/all/20220510221333.2770571-1-robh@kernel.org/
[3]: https://lists.gnu.org/archive/html/help-make/2021-06/msg00001.html
[4]: https://www.cons.org/cracauer/sigint.html

Fixes: 392885ee82d3 ("kbuild: let fixdep directly write to .*.cmd files")
Reported-by: Ingo Molnar <mingo@kernel.org>
Reported-by: Rob Herring <robh@kernel.org>
Signed-off-by: Masahiro Yamada <masahiroy@kernel.org>
Tested-by: Ingo Molnar <mingo@kernel.org>
Reviewed-by: Nicolas Schier <nicolas@fjasle.eu>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [LeCmnGend/kernel_xiaomi_ginkgo](https://github.com/LeCmnGend/kernel_xiaomi_ginkgo)@[5be132cfb5...](https://github.com/LeCmnGend/kernel_xiaomi_ginkgo/commit/5be132cfb5d9a6d854a22eeeade7e0f4ffe155ce)
#### Friday 2022-11-18 12:27:06 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

[ Upstream commit 846bb97e131d7938847963cca00657c995b1fce1 ]

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [aurestic/odoo](https://github.com/aurestic/odoo)@[e7c8fed8e3...](https://github.com/aurestic/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Friday 2022-11-18 13:43:18 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: web_editor

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with an ugly patch. We'll review what to do in
master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104156

Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [PrimeGenerations/Foundation-19](https://github.com/PrimeGenerations/Foundation-19)@[3198c7d257...](https://github.com/PrimeGenerations/Foundation-19/commit/3198c7d257961f97b45ae128cdc72b657a2ed36e)
#### Friday 2022-11-18 14:27:53 by ivanmixo

Fixes MTF heli runtime (#547)

* Fixes mtf heli

* Fuck you die

* Whoops funny haha

* Cheeky juke fix

---
## [PrimeGenerations/Foundation-19](https://github.com/PrimeGenerations/Foundation-19)@[befabcec33...](https://github.com/PrimeGenerations/Foundation-19/commit/befabcec333347ce6b918d67d4c884b9e0dcefea)
#### Friday 2022-11-18 14:27:53 by TenameACAccount

more dcz changes yay (#548)

* Update site53-1.dmm

* fallout 5 on the byond engine

* fuck you box

Co-authored-by: UserU <37943518+User-U-U@users.noreply.github.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a7210bf6ff...](https://github.com/treckstar/yolo-octo-hipster/commit/a7210bf6ff4d187414610844dda9b4def3e0633d)
#### Friday 2022-11-18 15:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [PikachuJCB/docs](https://github.com/PikachuJCB/docs)@[6b97aae394...](https://github.com/PikachuJCB/docs/commit/6b97aae394f0cd6dff5b73809d0d1d248c62ee91)
#### Friday 2022-11-18 15:34:19 by Vinicius Victorino

Fix pronouns in Portuguese for Katie Sylor-Miller (#1955)

As you can see by her twitter account https://twitter.com/ksylor, she identifies as she/her. In Portuguese we have different names for male and female job descriptions, in this case arquitetO (male) and arquitetA (female).

Co-authored-by: Yan Thomas <61414485+Yan-Thomas@users.noreply.github.com>

---
## [liquidev/dawd3](https://github.com/liquidev/dawd3)@[f8612db6ef...](https://github.com/liquidev/dawd3/commit/f8612db6ef847ba1c06542a71f559a5ceacb5a82)
#### Friday 2022-11-18 17:15:24 by lqdev

fuck you (intelli)DJ

https://www.youtube.com/watch?v=92x4EK7EK5Y

---
## [emillon/dune](https://github.com/emillon/dune)@[183ad66f1a...](https://github.com/emillon/dune/commit/183ad66f1a37bb9b3240642bffff765ba555aee4)
#### Friday 2022-11-18 17:31:12 by Etienne Millon

Add shell completion

This provides a shell completion mechanism for dune. This relies on the
bash completion API, which can be used with zsh as well.

The architecture is:

- `dune complete script` outputs a script to be sourced in the user's
  shell. It is comprised of a `_dune` function and the `complete -F
  _dune dune` command to register it. The `_dune` function can be used
  in cram tests to write natural-looking tests for this feature.
- this script calls `dune complete command` with the partial
  command-line. This internal command parses it to determine what the
  word being completed refers to: a command name, an argument name, or
  an argument value. The first two ones are part of the metadata
  `cmdliner` knows about; the last one is provided through a completion
  function that can be passed in one the `Arg` functions.
- the interface between `bash` and `dune complete command` is simple:
  it passes the command line and a position to complete at (this is
  necessary to encode the difference between `dune bui<tab>` and `dune
  build <tab>` for example), and reads an array from the output of the
  command.

The things I'm happy with:

- it is small!
- coverage is pretty good: command names, arguments (positional and
  optional, including optional arguments with optional names), and the
  `--` construct are supported. So, this is likely to improve the user
  experience already.
- it is easy to test through cram or unit tests (I chose the former).

Now, for the ugly bits...

- this effectively is a partial reimplementation of cmdliner inside
  `complete.ml`. If the exact parsing rules are different, it means that
  we can complete to something with different or wrong semantics.
- the vendored copy of cmdliner is patched to expose so that it is
  possible to use the private APIs. these two points need to be resolved
  before we can think about how to upstream this.
- some bits of the cmdliner API need to be modified to provide
  completion automatically. For example for things like `enum` it's easy
  to provide a completion function automatically.
- it is difficult to define the right API for the completion functions.
  `unit -> string list` is a first approximation but with some
  limitations. For example, getting a list of buildable targets needs to
  run under `Fiber`, but we can't pollute the API with it. Interestingly
  enough, algebraic effects seem like they would be an interesting
  solution for this.
- at the moment, we're not relying on the shell's completion helpers to
  complete things like filenames. To support this we would either need
  to implement that in OCaml, or extend the bash/dune interface so that
  the completion function could call `compgen -f` based on the dune
  output.
- as a way to tie the two previous points: if we wanted to complete
  `dune build dir/file<tab>`, it would be a lot more efficient to pass
  the prefix to the build system and let it compute just the targets
  that match this, rather than compute everything and filter it
  afterwards. So that prefix would need to appear in the completion API.

Signed-off-by: Etienne Millon <me@emillon.org>

---
## [1048-Team/1048_dev](https://github.com/1048-Team/1048_dev)@[db26fe48f7...](https://github.com/1048-Team/1048_dev/commit/db26fe48f78e990421d9ac019407e2a9dba9141a)
#### Friday 2022-11-18 18:30:40 by Lord Protectress Rose

SINGULAR EVENT LOC DONE, IN AN HOUR!

I hate my life.

---
## [Pink-Chink/sojourn-station](https://github.com/Pink-Chink/sojourn-station)@[2290e12bed...](https://github.com/Pink-Chink/sojourn-station/commit/2290e12bedf65b90c6cf5bf4a8d43fdb43335512)
#### Friday 2022-11-18 18:44:38 by WilsonWeave

More beacon fiddling, part TWO!! WOW! !EGHGHG!!!  (#4128)

* Sheet Snatchers Offers!! Wow!!

Makes Lancer station offer 300 credits for up to 4 sheet snatchers at a time, considering Solnishko buys many more knives at a time, for 150 each, this seems more than fair considering the effort  and materials involved. Also ain't no one cooking food for trade offers chief.

Also makes Boris station offer 400 credits for up to 2  guild made advanced sheet snatchers at a time.  Having literally only one, extremely niche and rare to obtain offer as the only offer for a station is a really bad idea. Might not make the most sense for this station, but I'll consider replacing it with something more fitting. Eventually. But it works for now.

* More beacon fiddling, part TWO!! WOW! !EGHGHG!!!

Makes the religion stations buy meat, not as much per slab as Dionis does (given it's a tier one, roundstart station), but they can buy more at a time based on RNG.

Gives meat and all of it's sub-types a base price of 20 credits (hopefully)

Ghost-kitchen, AKA the VERY under utilized chef station now buys dinner trays. Slightly cheaper than knives. But I may change this to be more profitable than knives, albeit very restricted in number sold at a time, given it's one steel PLUS a tool-step. (Though honestly, I think I'm gonna tone back kitchen knife sales to 100, at LEAST, here soon.)

BUG FIX!!! Casino station no longer has an unlisted secret inventory, it now correctly displays, and gives a name to the extra tab. TODO! Make rigsuits more expensive overall, because you're paying a premium for a usually inferior rigsuit. (And voidsuits suits on that note). Oh and make it so the gems are properly sold for a million credits instead of twenty or two hundred million credits.

Casino station now buys cardboard boxes. For the meantime, it's plain cardboard boxes, while it's supposed to be a rebate, the boxes used for the Casino sales are a special subtype that include a LOT of non-box special objects. It works as an alternate favor method for now.

Brings a few more kitchen dishes up to closer par with roach-meat burgers. Vermouth pays FIVE HUNDRED credits for certain types of roach burgers roundstart. Bacon is a somewhat limited resource, and a pain to cook, so it should a LEAST be closer to roach meat. Effected stations are the trash refining station and the bluespace station.

---
## [CorvaxStation/Skyrat-tg](https://github.com/CorvaxStation/Skyrat-tg)@[3dfeccbf27...](https://github.com/CorvaxStation/Skyrat-tg/commit/3dfeccbf27b8dc53c97c2e9db0f1bdc4fd000ebe)
#### Friday 2022-11-18 19:47:54 by SkyratBot

[MIRROR] Clowns will now always like bananas. [MDB IGNORE] (#17300)

* Clowns will now always like bananas. (#70919)

## About The Pull Request
Clown's liver makes them like bananas, ignoring their racial food
preferences.

## Why It's Good For The Game
I don't think clown moths should vomit from eating bananas. They are
clowns, after all.
Also clowns are healed from eating them, so it's a bit silly that they
vomit from their funny medicine.

## Changelog

:cl:
balance: Non-human clowns enjoy eating bananas now.
/:cl:

* Clowns will now always like bananas.

Co-authored-by: Striders13 <53361823+Striders13@users.noreply.github.com>

---
## [sggutier/sapling](https://github.com/sggutier/sapling)@[8b1a3c8fe6...](https://github.com/sggutier/sapling/commit/8b1a3c8fe66e21157db20bfe4950804c133639b1)
#### Friday 2022-11-18 23:16:23 by Evan Krause

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

