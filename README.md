## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-15](docs/good-messages/2022/2022-11-15.md)


2,217,117 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,217,117 were push events containing 3,370,058 commit messages that amount to 270,781,611 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[25d4afc869...](https://github.com/san7890/bruhstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Tuesday 2022-11-15 00:31:08 by Iamgoofball

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
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[f50670b344...](https://github.com/cockroachdb/cockroach/commit/f50670b3440e91bec05aebc1bc425e4dd465583f)
#### Tuesday 2022-11-15 00:39:13 by Tobias Grieger

rpc: re-work connection maintenance

This commit simplifies the `rpc` package.

The main aim is to make the code and the logging it produces somewhat
clearer and to pave the way for an ultimate merging of `nodedialer` with
`rpc` as well as adoption of the `util/circuit` package (async-based
circuit breaker).

`rpc.Context` hadn't aged well. Back in the day, it was a connection
pool that held on to connections even when they failed. The heartbeat
loop would run forever and its latest outcome would reflect the health
of the connection. We relied on gRPC to reconnect the transport as
necessary.

At some point we realized that leaving the connection management to
gRPC could cause correctness issues. For example, if a node is de-
commissioned and brought up again, gRPC might reconnect to it but
now we have a connection that claims to be for node X but is actually
for node Y. Similarly, we want to be able to vet that the remote
node's cluster version is compatible with ours before letting any
messages cross the connection.

To achieve this, we added `onlyOnceDialer` - a dialer that fails
all but the first attempt to actually connect, and in particular
from that point on connections were never long lived once they
hit a failure state.

Still, the code and testing around the heartbeat loop continued
to nurture this illusion. I found that quite unappealing as it
was sure to throw off whoever would ultimately work on this code.

So, while my original impetus was to produce better log messages
from `rpc.Context` when there were connection issues, I took
the opportunity to simplify the architecture of the code to
reflect what it actually does.

In doing so, a few heartbeat-related metrics were removed, as they made
limited sense in a world where failing connections get torn down (i.e.
our world).

Connection state logging is now a lot nicer. Previously, one would very
frequently see the onlyOnceDialer's error "cannot reuse client
connection" which, if one is not familar with the concept of the
onlyOnceDialer is completely opaque, and for those few in the know is an
unhelpful error - you wanted the error that occurred during dialing.

I paid special attention to the "failfast" behavior. If connections
don't stay in the pool when they are unhealthy, what prevents us from
dialing down nodes in a tight loop? I realized that we got lucky with
our use of onlyOnceDialer because it would always prompt gRPC to do
one retry, and at a 1s backoff. So, the connection would stay in the
pool for at least a second, meaning that this was the maximum frequency
at which we'd try to connect to a down node.

My cleanups to onlyOnceDialer in pursuit of better logging elimitated
this (desirable) property. Instead we now skip the log messages should
they become too frequent. I claim that this is acceptable for now since
the vast majority of callers go through a `node.Diaelr`, which has a
circuit breaker (letting callers through at most once per second).

We previously configured gRPC with a 20s dial timeout. That means that
if a remote is unreachable, we'd spend 20s just trying to dial it,
possibly tying up callers that could be trying a reachable node in the
meantime. That seemed wildly too large; I am reducing it to 5s here
which is still generous (but there's a TLS handshake in here so better
not make it too tight).

We previously tried to re-use connections that were keyed with a NodeID
for dial attempts that didn't provide a NodeID. This caused some issues
over the years and was now removed; the extra RPC connections are
unlikely to cause any issues.

The internal connection map is now a plain map with an RWMutex. This is
just easier and gets the job done. The code has simplified as a result
and it's clearer that it's correct (which it repeatedly was not in the
past).

I implemented redactability for gRPC's `status.Status`-style errors,
so they format nicer and at least we get to see the error code (the
error message is already flattened when gRPC hands us the error,
sadly).

There are various other improvements to errors and formatting. The
following are excerpts from the health channel when shutting down
another node in a local cluster:

Connection is first established:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 3  connection is now ready

n1 goes down, i.e. existing connection is interrupted (this error comes
from `onlyOnceDialer`):

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 35  closing
connection after: ‹rpc error: code = Unavailable desc = connection
error: desc = "transport: Error while dialing connection interrupted
(did the remote node shut down or are there networking issues?)"›

Reconnection attempts; these logs are spaced 1-2s apart:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 37  unable to
connect (is the peer up and reachable?): initial connection heartbeat
failed: ‹rpc error: code = Unavailable desc = connection error: desc =
"transport: Error while dialing dial tcp 127.0.0.1:26257: connect:
connection refused"›

n3 is back up:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 49  connection is now ready

There are other connection errors in the logs that stem from operations
checking for a healthy connection, failing to get through circuit
breakers, etc., such as these:

> [n3,intExec=‹claim-jobs›,range-lookup=/Table/15/4/‹NULL›] 33  unable
to connect to n1: failed to check for ready connection to n1 at
‹127.0.0.1:26257›: ‹connection not ready: TRANSIENT_FAILURE›

Release note (general change): Previously, CockroachDB employed a 20s
connection timeout for cluster-internal connections between nodes.  This
has been reduced to 5s to potentially reduce the impact of network
issues.

Release note (general change): Previously, CockroachDB (mostly) shared a
TCP connection for the KV and Gossip subsystems. They now use their own
connection each, so the total number of outgoing and incoming TCP
connections at each node in the cluster will increase by 30 to 50
percent.

---
## [sqnztb/tgstation](https://github.com/sqnztb/tgstation)@[db83f6498d...](https://github.com/sqnztb/tgstation/commit/db83f6498da37ecd25588ea3f7024409d2f3f117)
#### Tuesday 2022-11-15 00:40:01 by vincentiusvin

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
## [ruizlenato/SmudgeLord](https://github.com/ruizlenato/SmudgeLord)@[053300e5ba...](https://github.com/ruizlenato/SmudgeLord/commit/053300e5ba24afa56b5cd47d6050eabfeaf0bfc8)
#### Tuesday 2022-11-15 01:36:17 by ruizlenato

 Videos: instagram improvements  (fuck you zuckberg)

---
## [macladson/lighthouse](https://github.com/macladson/lighthouse)@[66eca1a882...](https://github.com/macladson/lighthouse/commit/66eca1a88218462235cb76a116dc3c6a1853444f)
#### Tuesday 2022-11-15 01:44:04 by Michael Sproul

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
## [CSC207-2022F-UofT/course-project-team-communify](https://github.com/CSC207-2022F-UofT/course-project-team-communify)@[d2cd0893c1...](https://github.com/CSC207-2022F-UofT/course-project-team-communify/commit/d2cd0893c1c885bfecf5e8c4eee680a8e14e4a17)
#### Tuesday 2022-11-15 01:49:03 by clin1967

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
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[f16dd95118...](https://github.com/ammarfaizi2/linux-fork/commit/f16dd95118f42b67e911490c8c389039c3d9006f)
#### Tuesday 2022-11-15 01:56:23 by Johannes Weiner

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
## [InfoTeddy/VVVVVV](https://github.com/InfoTeddy/VVVVVV)@[2d6b2e685b...](https://github.com/InfoTeddy/VVVVVV/commit/2d6b2e685b09d364e629b30a16c533b131efbde7)
#### Tuesday 2022-11-15 03:40:50 by Dav999-v

Clarify submodules in desktop_version/README.md

VVVVVV uses submodules now, so you need to know how to initialize them.

I'm explicitly not including `git clone --recurse-submodules`. Usage of
submodules in git projects is kinda rare in my experience, so people
are used to doing simple clones, and that instruction would just result
in people being annoyed thinking they have to delete the repo they
already cloned, and clone it again except slightly differently.

It also doesn't help you if you need submodules that aren't in the
master branch (for example, if you clone my fork recursively and then
checkout the localization branch, you won't have C-HashMap and you'll
need the update command anyway). And you also need it whenever VVVVVV
updates its submodules. So teaching people just the update command is
better.

---
## [Pedro-Bachiega/otservbr-global](https://github.com/Pedro-Bachiega/otservbr-global)@[fbd70d116c...](https://github.com/Pedro-Bachiega/otservbr-global/commit/fbd70d116c260a94902c2e0164ceca94023f2f28)
#### Tuesday 2022-11-15 04:45:46 by rigis1

Fixes and add blood brothers quest till mission 4 (#753)

Fix:
• electric sparks
• baking
• filling fluids container
• the hunt for the sea serpent quest

Add:
• questlog entry for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• storages for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• keywords for blood brothers quest, the hunt for the sea serpent quest and grave danger quest
• condition to harlow travel to vengoth
• holy water to henricus shop
• food for blood brothers quest
• spawn npc ortheus and jack springer, monster gaffir
• npc jack springer 
• ugly monster loot
• events to gaffir and ugly monster
• ice cracking
• basic events for bosses Sir Nictros and Sir Baeloc
• basic spawn boss for levers
• access to falcon bastion

---
## [ttaylorr/git](https://github.com/ttaylorr/git)@[eb20e63f5a...](https://github.com/ttaylorr/git/commit/eb20e63f5a96e24852c6ab1eca9f96af2648802f)
#### Tuesday 2022-11-15 04:49:54 by Jeff King

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
## [TerryCavanagh/VVVVVV](https://github.com/TerryCavanagh/VVVVVV)@[86d90a1296...](https://github.com/TerryCavanagh/VVVVVV/commit/86d90a1296739adef30b224f41e3a6ab55069a48)
#### Tuesday 2022-11-15 06:09:43 by Misa

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
## [Floofies/tgstation](https://github.com/Floofies/tgstation)@[5b4ba051a0...](https://github.com/Floofies/tgstation/commit/5b4ba051a08e0c63ca77abedd86991d3ba7aaf29)
#### Tuesday 2022-11-15 06:24:42 by LemonInTheDark

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
## [peff/git](https://github.com/peff/git)@[5db35eb4d0...](https://github.com/peff/git/commit/5db35eb4d0b8f438058551d6bd101592b9e60743)
#### Tuesday 2022-11-15 06:34:25 by Jeff King

branch: gracefully handle '-d' on orphan HEAD

When deleting a branch, "git branch -d" has a safety check that ensures
the branch is merged either to its upstream, or to HEAD. To do that,
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
     2009-12-29), made it OK to delete a branch if it is merged to its
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

So instead, we'll teach the local branch_merged() to treat a NULL as
"not merged". This would be a little more elegant in in_merge_bases()
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
     segfault.

  c. The third one confirms that we correctly say "not merged to HEAD"
     when we can't resolve HEAD, and reject the deletion.

  d. Same, but with commit graphs enabled. Without the first hunk in
     branch_merged(), this one would segfault.

Reported-by: Martin von Zweigbergk <martinvonz@google.com>

---
## [peff/git](https://github.com/peff/git)@[599e5e1707...](https://github.com/peff/git/commit/599e5e170751c7636bd7b2fd3b050d698f0525d7)
#### Tuesday 2022-11-15 06:34:26 by Jeff King

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
## [Mothblocks/tgstation](https://github.com/Mothblocks/tgstation)@[cf59b0bba1...](https://github.com/Mothblocks/tgstation/commit/cf59b0bba1bb13b3459cbd01e441601be5a22383)
#### Tuesday 2022-11-15 07:00:15 by san7890

Null-checks PR Body in removeGuideComments (#71043)

This is what #71041 was supposed to be.

## About The Pull Request
Hey there,

I was looking at #71028, and I noticed that this workflow failed because
oranges left the PR body blank. I think that's silly, so let's just
include an early return so the whole thing doesn't throw.

This is the error:


![image](https://user-images.githubusercontent.com/34697715/199852746-24b2ed53-442d-4c40-b81d-902236183328.png)
via:
https://github.com/tgstation/tgstation/actions/runs/3382875608/jobs/5618241641

Here's an example PR where I fixed it (on my fork, just expand the
"Remove guide comments" step):
https://github.com/san7890/bruhstation/actions/runs/3389994395/jobs/5633658300

## Why It's Good For The Game

It hurts my heart to see checks red out in trivial situations like this.
## Changelog
Literally nothing here concerns players.

Ignore the commit history I was testing this PR the wrong way and was
effectively gaslighting myself (we're good now though)

---
## [TheGerd1/Dispatch](https://github.com/TheGerd1/Dispatch)@[b098cb71dd...](https://github.com/TheGerd1/Dispatch/commit/b098cb71dd4904bcc0e797aafedb77026b1e5ab4)
#### Tuesday 2022-11-15 07:02:13 by The Gerd

added signal 100

clicking the 'signal 100' button adds a big fuck-you red banner

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[90803cc9e6...](https://github.com/Paxilmaniac/Skyrat-tg/commit/90803cc9e6da84d0681c7dfaec195741bbc881e9)
#### Tuesday 2022-11-15 07:45:47 by Paxilmaniac

again fuck this stupid ''''''''advanced'''''''' ammo box shit

---
## [nbyavuz/postgres](https://github.com/nbyavuz/postgres)@[8272749e8c...](https://github.com/nbyavuz/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Tuesday 2022-11-15 08:35:05 by Tom Lane

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
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[0298539837...](https://github.com/GeoB99/reactos/commit/02985398379a0ad1cb71eb947aff9e84c869ed36)
#### Tuesday 2022-11-15 09:55:06 by George Bișoc

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
## [dnbdmr/dwm](https://github.com/dnbdmr/dwm)@[67d76bdc68...](https://github.com/dnbdmr/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Tuesday 2022-11-15 10:10:01 by Chris Down

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
## [GIGATYPHOON/Monochrome](https://github.com/GIGATYPHOON/Monochrome)@[240d2cabee...](https://github.com/GIGATYPHOON/Monochrome/commit/240d2cabee02baa201c1f3b910992f308a8e1c40)
#### Tuesday 2022-11-15 12:04:42 by Keeper15

set speed from 20 to 30, because fuck you even more

---
## [xxyzz/racket](https://github.com/xxyzz/racket)@[6c71a48c20...](https://github.com/xxyzz/racket/commit/6c71a48c203029fd3271f97996eb9bd4c8901cd5)
#### Tuesday 2022-11-15 12:11:18 by Matthew Flatt

remove syntax arming, but protect macro-expansion operations

Summary:

Syntax arming and disarming were part of a design to allow sandboxing
untrusted code without unduly constraining the sandboxed code. This
commit replaces that approach with a simpler one. The trade-off is
that some advanced macro-implementation tools, including
`syntax-local-value` and `local-expand`, cannot be referenced directly
within a sandbox (i.e., in a context where the code inspector is
different than the original one).

Long version:

Unsafe operations --- or operations that would otherwise break
invariants within a trusted library --- can be protected by not
exporting them or by using `protect-out` on an export. Protected
bindings cannot be referenced directly in sandboxed programs. It's
common, however, for macros to expand to (suitably guarded) uses of
unsafe or unexported bindings. Sandboxed programs need to be able to
use those macros, even though expansions refer to bindings that cannot
be referenced directly by the sandboxed program.

To make that combination work, quoted syntax objects that appear in a
macro retain a right to access the same bindings that would be allowed
in the enclosing module. This system of protected bindings and
quoted-syntax access is working, as far as we can tell, EXCEPT for
some cases when untrusted code uses `expand`, `local-expand,`
`syntax-local-value`, and variants of those functions. Some trusted
macros and tools need to force expansions and rearrange the result, as
in the `class` macro or the errortrace library, which is why things
like `local-expand` exist. The danger is that portions of the
expansion can be extracted, with permissions intact on the extracted
part, and then abused by untrusted programs.

Syntax "arming" was an attempt to close that hole by distinguishing
trusted and untrusted uses of expanded code, revoking permissions on
an identifier by tainting it when it is extracted from an expansion by
an untrusted party. The tricky part has been drawing the line between
trusted and untrusted uses through a mixture of inferred and explicit
boundaries. Explicit boundaries usually involve `syntax-protect`.
Experience has shown that it's difficult to remember to use
`syntax-protect` consistently enough, and we have not been able to
enlarge the role of inference enough to close the hole.

This commit tries a simpler approach, which is to discard the complex
arming system and instead just protect operations like `local-expand`
that force macro expansions. Protecting `syntax-local` makes a sandbox
less flexible: it prevents running an untrusted module in a sandbox
when the module implements its own macros with `local-expand`,
`syntax-local-value`, and some related expansion-time operations. Most
macros do not need those facilities, so most modules would still work
in a sandbox. Meanwhile, sandboxed modules can still use macros that
use those faciltiies and that are implemented in trusted modules.

A slightly different approach is used for the `expand` family of
functions, which are not used by macros, but are instead for debugging
and exploration. Each of those functions now takes an additional
inspector argument that defaults to `(current-inspector)`; if that
inspector is not the original one, then the result of expansion is
preemptively tainted, so identifiers in the expansion cannot be used.
(Syntax objects that are included in syntax-error exceptions are also
still tainted that way, as before.) So, `expand` can still be used in
a sandbox to explore expansions without necessarily accessing bindings
that are referenced in the expansion.

This change does not entirely remove the burden for implementing
modules that are intended to be trusted. Instead of requiring a
careful use of `syntax-protect` on macro expansions, the problem is
narrowed to using `local-expand` and related functions correctly, as
well as protecting any exports that would expose the capabilities of
`local-expand`. Non-protected exports that expose `local-expand` are
rare, in contrast to macros that lack `syntax-protect`. Another
benefit is that tools and macros that manipulate expansions no longer
need to use `syntax-disarm` and `syntax-rearm`, which was painful and
error-prone.

The functions `syntax-protect`, `syntax-arm`, `syntax-disarm`, and
`syntax-rearm` are still available, but they now just return the given
syntax object unmodified. The 'taint-mode and 'certify-mode
syntax-object properties are no longer specifically recognized by the
expander.

This change is work with @michaelballantyne, who identified problems
with the current system and moved the discussion in this direction,
plus @rmculpepper, @samth, and @mfelleisen.

---
## [RikuTheKiller/tgstation](https://github.com/RikuTheKiller/tgstation)@[fc7c186957...](https://github.com/RikuTheKiller/tgstation/commit/fc7c186957088b6ffd0605f814bea754670c0212)
#### Tuesday 2022-11-15 13:06:53 by RikuTheKiller

Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

---
## [NeoHuy/free-programming-books](https://github.com/NeoHuy/free-programming-books)@[5fd70502a0...](https://github.com/NeoHuy/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Tuesday 2022-11-15 13:07:40 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [obote998/type-challenges](https://github.com/obote998/type-challenges)@[c299c95108...](https://github.com/obote998/type-challenges/commit/c299c95108a131f1a4d89c50ae9d2be428b51f09)
#### Tuesday 2022-11-15 14:09:56 by obote998

Update pnpm-lock.yaml

• RETURN LOST LOVES / GET BACK
TOGETHER
• ATTRACT TRUE LOVE INTO YOUR LIFE
• HAVE THE PERSON YOU DESIRE, DESIRE YOU BACK
• ATTRACT A PERFECT SOULMATE TO SHARE LIFE WITH
If you are seeking a REAL LOVE SPELL /
SPECIAL LOVE SPELL CASTING then look no further. My Love Spells WORK and WORK well!.

Money back guarantee lets do your spell
today        Love spells, Marriage spells - Bring lost lover back
Stop lover from cheating, be in control of the love in the house. Fix your troubled marriage. Tried many try me last, 35 years of experience. Stop or make a Divorce. Fix a Broken Marriage. Fall in Love & Commitment. Stop cheating.
Love spells, Marriage spells - Bring lost lover back Stop lover from cheating, be in control of the love in the house. Fix your troubled marriage. Tried many try me last, 35 years of experience. Stop or make a Divorce. Stop cheating. Fall in Love & Commitment. Fix a Broken Marriage.
Contact Me
https://chiefaberash.com/
Get in Touch Get instant help for your love life now, with instant and guaranteed results.
Contact +27 63 5340727 Email info@chiefaberash.com

---
## [rems-project/CN-pKVM-buddy-allocator-case-study](https://github.com/rems-project/CN-pKVM-buddy-allocator-case-study)@[019d337350...](https://github.com/rems-project/CN-pKVM-buddy-allocator-case-study/commit/019d337350c49aad111f9c2d74d3a9b8e54965f9)
#### Tuesday 2022-11-15 14:56:16 by Dhruv Makwana

Fix page_add_to_list spec

There are two fixes in this commit (sorry, should have committed more
atomically).
1. Addition of all the `unchanged`s
2. Changing `||` (or) to `;` (and)

(1) Is a bit of a pain to figure out, but it's doable enough when you start seeing
inconsistent/changing values for things that shouldn't be changing. I think the root
issue here is actually not being able to pass in ghost/logical parameters.

(2) Take a look at the below (pp and `let`s added manually).

In this example, we know from the counter-model slicing (useful!) that one of
the places it fails is a disagreement on order. One is 6, the other is 99. We
also know that the only place that .order = 99 can come from is index 55640.

let hyp_physvirt_offset = 0
let p_i2 = ((((integer)O_p.value) - call___find_buddy_avail0.O___hyp_vmemmap.value) / 4)
         = 545258
let virt = ((p_i2 * 4096) - call___find_buddy_avail0.O_hyp_physvirt_offset.value)
         = 2233376768
let prev = ((integer)call_list_empty0.OR.value.prev)
let O_p  = {.value = 18446744073708723144}
let O___hyp_vmemmap = {.value = 18446744073706542112}
let weird = ((((integer)O_p.value) + 2) - O___hyp_vmemmap.value) / 4
          = 545258.5
          = p_i2 + 0.5
let i     = 545258
let AP3R = {.prev = 126, .next = 2233376768}
let AP1R = {.prev = 2369310720, .next = 2279262357}
         = 2279262357 / 4096
         = 556460.5363769531

{ .refcount = 100
, .order = 99
, .flags = 98
} <-
{ .value = call___find_buddy_avail0.V2.value[weird = call_page_add_to_list0.HpR.value]
}.value[
  (
    (
      (integer)
      (
        { .prev = (APsI.prev[p_i2 = call_page_add_to_list0.AP1R.prev])
                            [prev / 4096 = call_page_add_to_list0.AP3R.prev]
        , .next = (APsI.next[p_i2 = call_page_add_to_list0.AP1R.next])
                            [prev / 4096 = call_page_add_to_list0.AP3R.next]
        }.next[i]
      )
    )
    +
    call_page_add_to_list0.O_hyp_physvirt_offset.value
  )
  /
  page_size()
]

It's really difficult to trace the value dependency.
* i - quantified index, not given in counter-model (only in debug output trace).
* p_i2, virt - these are reverse engineered (either counter-model, or
  constraints) they were originally fully sub'd in.
* weird, AP1R.next / 4096 - these are good clues that something is not being
  constrained properly, but where on earth does the '+ 2' come from? According to
  the debug, it's computational, which seems bonkers.
* prev - not specified in counter model, so good clue that it is irrelevant
* you can't just point to sub-expressions and ask `what's this?`. Though there
  is some debug printing, it doesn't seem to be working for this. Specifically
  for '(..).next[i]', knowing that is 55640 would have saved time by not
  investigating `call___find_buddy_avail0.V2.value[weird = call_page_add_to_list0.HpR.value]`.

---
## [namdevkashish/100DaysOfCodeChallenge](https://github.com/namdevkashish/100DaysOfCodeChallenge)@[e15e84bafb...](https://github.com/namdevkashish/100DaysOfCodeChallenge/commit/e15e84bafbd0790ae725e0e65a8217d8eb18d9f1)
#### Tuesday 2022-11-15 15:01:04 by namdevkashish

Click here to view question

Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill=[2,4,6]. Anna declines to eat item k=bill[2] which costs 6. If Brian calculates the bill correctly, Anna will pay (2+4)/2=3. If he includes the cost of bill[2], he will calculate (2+4+6)/2=6. In the second case, he should refund 3 to Anna.

Function Description

Complete the bonAppetit function in the editor below. It should print Bon Appetit if the bill is fairly split. Otherwise, it should print the integer amount of money that Brian owes Anna.

bonAppetit has the following parameter(s):

bill: an array of integers representing the cost of each item ordered
k: an integer representing the zero-based index of the item Anna doesn't eat
b: the amount of money that Anna contributed to the bill
Input Format

The first line contains two space-separated integers n and k, the number of items ordered and the 0-based index of the item that Anna did not eat.
The second line contains n space-separated integers bill[i] where 0<=i<n.
The third line contains an integer, b, the amount of money that Brian charged Anna for her share of the bill.

Constraints
2<=n<=10^5
0<=k<n
0<=bill[i]<=10^4

The amount of money due Anna will always be an integer
Output Format

If Brian did not overcharge Anna, print Bon Appetit on a new line; otherwise, print the difference (i.e., b(charged)-b(actual)) that Brian must refund to Anna. This will always be an integer.

Sample Input 0

4 1
3 10 2 9
12
Sample Output 0

5
Explanation 0
Anna didn't eat item bill[1]=10, but she shared the rest of the items with Brian. The total cost of the shared items is 3+2+9=14 and, split in half, the cost per person is b(actual)=7. Brian charged her b(charged)=12 for her portion of the bill. We print the amount Anna was overcharged, b(actual)-b(charged)=12-7=5, on a new line.

Sample Input 1

4 1
3 10 2 9
7
Sample Output 1

Bon Appetit
Explanation 1
Anna didn't eat item bill[1]=10, but she shared the rest of the items with Brian. The total cost of the shared items is 3+2+9=14 and, split in half, the cost per person is b(actual)=7. Because b(actual)=b(charged)=7, we print Bon Appetit on a new line.

---
## [Olgaoobasja/Olgaoobasja](https://github.com/Olgaoobasja/Olgaoobasja)@[d0b2c402ae...](https://github.com/Olgaoobasja/Olgaoobasja/commit/d0b2c402aec7165ff2d35fb45a17a0046ba607e3)
#### Tuesday 2022-11-15 17:47:58 by Olgaoobasja

Dream in reality. Tallinn.

Hot weather does not deter travelers. There are a lot of tourists in Tallinn now. They try to see everything! And at the end of a hot day, enjoy a coffee drink or a snack. This is the kind of cafe I'm showing. Here, there are outdoor tables overlooking the towers .. and a cool cafe with a beautiful historical design. The cafe has a piece of the fortress wall of Tallinn.
This is so romantic. You remember historical heroes ... or everything you saw in a day. The cafe is so nice that you don't want to leave. But there are still historical mysteries ahead ... Curiosity takes over. People live in houses .. and towers nearby .. How incompatible and compatible together. Opposites attract to themselves and a kind of harmony is obtained.

---
## [RedDevilus/pcsx2](https://github.com/RedDevilus/pcsx2)@[54f251a7aa...](https://github.com/RedDevilus/pcsx2/commit/54f251a7aa4d05b385b5d3f6d1789ae6b19eea30)
#### Tuesday 2022-11-15 17:54:35 by RedDevilus

GameDB: Fix multiple games + maintenance

- Area 51: Half Pixel Normal vertex for lighting and other places
- Shrek 2: Basic mipmapping which kinda half fixes the sun missing
- Galaxy Angel II: Normal vertex which reduces misalignment
- Forgotten Realms - Demon Stone: Clamping Mode extra + preserve which will solve the occasional SPS + missing demo entry.
- Spyro Dawn of dragon: SW clut + sprite which doesn't make you vomit from the overbloomification and looks similar to the software renderer
- Castlevania Curse of darkness half sprite which will enlarge the font similar to software renderer + some missing fixes that were available on the Europe and America versions but not Japanese.
- Drakengard 1 + 2 (Also know as Drag-on Dragoon) : Partial (no hashcache) to avoid slow transitions and other areas. Adds missing Japanese Drakengard 1
- Urban reign: Partial texture preloading to fix performance issues in the gameplay
- Maintenance that add spaces in the titles for Disc1of1 to Disc 1 of 1 and more...

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[85b2d5043d...](https://github.com/Time-Green/tgstation/commit/85b2d5043dbc9eb277bf57dd6dc5147ae08fe978)
#### Tuesday 2022-11-15 18:13:47 by LemonInTheDark

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
## [exercism/rust](https://github.com/exercism/rust)@[7a49959ea4...](https://github.com/exercism/rust/commit/7a49959ea4aa3dbe3f5dd23a1de909196d62ea13)
#### Tuesday 2022-11-15 18:27:54 by Remo Senekowitsch

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
## [Margarino/weddingwebapp](https://github.com/Margarino/weddingwebapp)@[4456338329...](https://github.com/Margarino/weddingwebapp/commit/445633832952f29c8e1dc7f2482a7d8a226eccae)
#### Tuesday 2022-11-15 18:30:38 by Margarino

un-fucking the last efCore clusterfuck

i hate my life

---
## [newstools/2022-daily-dispatch](https://github.com/newstools/2022-daily-dispatch)@[626ca2c5dd...](https://github.com/newstools/2022-daily-dispatch/commit/626ca2c5dd94dccb22175f446b6844a7a1cd101f)
#### Tuesday 2022-11-15 20:20:09 by Billy Einkamerer

Created Text For URL [www.dispatchlive.co.za/news/2022-11-15-life-for-man-who-raped-and-murdered-girlfriend-then-dumped-her-body-in-the-street/]

---
## [jgunthorpe/linux](https://github.com/jgunthorpe/linux)@[734b5fd6be...](https://github.com/jgunthorpe/linux/commit/734b5fd6be06e75ff500a69f88ffccbc8258fb74)
#### Tuesday 2022-11-15 20:28:34 by Jason Gunthorpe

cover-letter: IOMMUFD Generic interface

[
This has been in linux-next for a little while now, and we've completed
the syzkaller run. 1300 hours of CPU time have been invested since the
last report with no improvement in coverage or new detections. syzkaller
coverage reached 69%(75%), and review of the misses show substantial
amounts are WARN_ON's and other debugging which are not expected to be
covered.
]

iommufd is the user API to control the IOMMU subsystem as it relates to
managing IO page tables that point at user space memory.

It takes over from drivers/vfio/vfio_iommu_type1.c (aka the VFIO
container) which is the VFIO specific interface for a similar idea.

We see a broad need for extended features, some being highly IOMMU device
specific:
 - Binding iommu_domain's to PASID/SSID
 - Userspace IO page tables, for ARM, x86 and S390
 - Kernel bypassed invalidation of user page tables
 - Re-use of the KVM page table in the IOMMU
 - Dirty page tracking in the IOMMU
 - Runtime Increase/Decrease of IOPTE size
 - PRI support with faults resolved in userspace

Many of these HW features exist to support VM use cases - for instance the
combination of PASID, PRI and Userspace IO Page Tables allows an
implementation of DMA Shared Virtual Addressing (vSVA) within a
guest. Dirty tracking enables VM live migration with SRIOV devices and
PASID support allow creating "scalable IOV" devices, among other things.

As these features are fundamental to a VM platform they need to be
uniformly exposed to all the driver families that do DMA into VMs, which
is currently VFIO and VDPA.

The pre-v1 series proposed re-using the VFIO type 1 data structure,
however it was suggested that if we are doing this big update then we
should also come with an improved data structure that solves the
limitations that VFIO type1 has. Notably this addresses:

 - Multiple IOAS/'containers' and multiple domains inside a single FD

 - Single-pin operation no matter how many domains and containers use
   a page

 - A fine grained locking scheme supporting user managed concurrency for
   multi-threaded map/unmap

 - A pre-registration mechanism to optimize vIOMMU use cases by
   pre-pinning pages

 - Extended ioctl API that can manage these new objects and exposes
   domains directly to user space

 - domains are sharable between subsystems, eg VFIO and VDPA

The bulk of this code is a new data structure design to track how the
IOVAs are mapped to PFNs.

iommufd intends to be general and consumable by any driver that wants to
DMA to userspace. From a driver perspective it can largely be dropped in
in-place of iommu_attach_device() and provides a uniform full feature set
to all consumers.

As this is a larger project this series is the first step. This series
provides the iommfd "generic interface" which is designed to be suitable
for applications like DPDK and VMM flows that are not optimized to
specific HW scenarios. It is close to being a drop in replacement for the
existing VFIO type 1 and supports existing qemu based VM flows.

Several follow-on series are being prepared:

- Patches integrating with qemu in native mode:
  https://github.com/yiliu1765/qemu/commits/qemu-iommufd-6.0-rc2

- A completed integration with VFIO now exists that covers "emulated" mdev
  use cases now, and can pass testing with qemu/etc in compatability mode:
  https://github.com/jgunthorpe/linux/commits/vfio_iommufd

- A draft providing system iommu dirty tracking on top of iommufd,
  including iommu driver implementations:
  https://github.com/jpemartins/linux/commits/x86-iommufd

  This pairs with patches for providing a similar API to support VFIO-device
  tracking to give a complete vfio solution:
  https://lore.kernel.org/kvm/20220901093853.60194-1-yishaih@nvidia.com/

- Userspace page tables aka 'nested translation' for ARM and Intel iommu
  drivers:
  https://github.com/nicolinc/iommufd/commits/iommufd_nesting

- "device centric" vfio series to expose the vfio_device FD directly as a
  normal cdev, and provide an extended API allowing dynamically changing
  the IOAS binding:
  https://github.com/yiliu1765/iommufd/commits/iommufd-v6.0-rc2-nesting-0901

- Drafts for PASID and PRI interfaces are included above as well

Overall enough work is done now to show the merit of the new API design
and at least draft solutions to many of the main problems.

Several people have contributed directly to this work: Eric Auger, Joao
Martins, Kevin Tian, Lu Baolu, Nicolin Chen, Yi L Liu. Many more have
participated in the discussions that lead here, and provided ideas. Thanks
to all!

The v1/v2 iommufd series has been used to guide a large amount of preparatory
work that has now been merged. The general theme is to organize things in
a way that makes injecting iommufd natural:

 - VFIO live migration support with mlx5 and hisi_acc drivers.
   These series need a dirty tracking solution to be really usable.
   https://lore.kernel.org/kvm/20220224142024.147653-1-yishaih@nvidia.com/
   https://lore.kernel.org/kvm/20220308184902.2242-1-shameerali.kolothum.thodi@huawei.com/

 - Significantly rework the VFIO gvt mdev and remove struct
   mdev_parent_ops
   https://lore.kernel.org/lkml/20220411141403.86980-1-hch@lst.de/

 - Rework how PCIe no-snoop blocking works
   https://lore.kernel.org/kvm/0-v3-2cf356649677+a32-intel_no_snoop_jgg@nvidia.com/

 - Consolidate dma ownership into the iommu core code
   https://lore.kernel.org/linux-iommu/20220418005000.897664-1-baolu.lu@linux.intel.com/

 - Make all vfio driver interfaces use struct vfio_device consistently
   https://lore.kernel.org/kvm/0-v4-8045e76bf00b+13d-vfio_mdev_no_group_jgg@nvidia.com/

 - Remove the vfio_group from the kvm/vfio interface
   https://lore.kernel.org/kvm/0-v3-f7729924a7ea+25e33-vfio_kvm_no_group_jgg@nvidia.com/

 - Simplify locking in vfio
   https://lore.kernel.org/kvm/0-v2-d035a1842d81+1bf-vfio_group_locking_jgg@nvidia.com/

 - Remove the vfio notifiter scheme that faces drivers
   https://lore.kernel.org/kvm/0-v4-681e038e30fd+78-vfio_unmap_notif_jgg@nvidia.com/

 - Improve the driver facing API for vfio pin/unpin pages to make the
   presence of struct page clear
   https://lore.kernel.org/kvm/20220723020256.30081-1-nicolinc@nvidia.com/

 - Clean up in the Intel IOMMU driver
   https://lore.kernel.org/linux-iommu/20220301020159.633356-1-baolu.lu@linux.intel.com/
   https://lore.kernel.org/linux-iommu/20220510023407.2759143-1-baolu.lu@linux.intel.com/
   https://lore.kernel.org/linux-iommu/20220514014322.2927339-1-baolu.lu@linux.intel.com/
   https://lore.kernel.org/linux-iommu/20220706025524.2904370-1-baolu.lu@linux.intel.com/
   https://lore.kernel.org/linux-iommu/20220702015610.2849494-1-baolu.lu@linux.intel.com/

 - Rework s390 vfio drivers
   https://lore.kernel.org/kvm/20220707135737.720765-1-farman@linux.ibm.com/

 - Normalize vfio ioctl handling
   https://lore.kernel.org/kvm/0-v2-0f9e632d54fb+d6-vfio_ioctl_split_jgg@nvidia.com/

 - VFIO API for dirty tracking (aka dma logging) managed inside a PCI
   device, with mlx5 implementation
   https://lore.kernel.org/kvm/20220901093853.60194-1-yishaih@nvidia.com

 - Introduce a struct device sysfs presence for struct vfio_device
   https://lore.kernel.org/kvm/20220901143747.32858-1-kevin.tian@intel.com/

 - Complete restructuring the vfio mdev model
   https://lore.kernel.org/kvm/20220822062208.152745-1-hch@lst.de/

 - Isolate VFIO container code in preperation for iommufd to provide an
   alternative implementation of it all
   https://lore.kernel.org/kvm/0-v1-a805b607f1fb+17b-vfio_container_split_jgg@nvidia.com

 - Simplify and consolidate iommu_domain/device compatability checking
   https://lore.kernel.org/linux-iommu/cover.1666042872.git.nicolinc@nvidia.com/

 - Align iommu SVA support with the domain-centric model
   https://lore.kernel.org/all/20221031005917.45690-1-baolu.lu@linux.intel.com/

This is about 233 patches applied since March, thank you to everyone
involved in all this work!

Currently there are a number of supporting series still in progress:

 - DMABUF exporter support for VFIO to allow PCI P2P with VFIO
   https://lore.kernel.org/r/0-v2-472615b3877e+28f7-vfio_dma_buf_jgg@nvidia.com

 - Start to provide iommu_domain ops for POWER
   https://lore.kernel.org/all/20220714081822.3717693-1-aik@ozlabs.ru/

However, these are not necessary for this series to advance.

This is on github: https://github.com/jgunthorpe/linux/commits/iommufd

v4:
 - Rebase to v6.1-rc3, include the iommu branch with the needed EINVAL
   patch series and also the SVA rework
 - All bug fixes and comments with no API or behavioral changes
 - gvt tests are passing again
 - Syzkaller is no longer finding issues and achieved high coverage of
   69%(75%)
 - Coverity has been run by two people
 - new "nth failure" test that systematically sweeps all error unwind paths
   looking for splats
 - All fixes noted in the mailing list
   If you sent an email and I didn't reply please ping it, I have lost it.
 - The selftest patch has been broken into three to make the additional
   modification to the main code clearer
 - The interdiff is 1.8k lines for the main code, with another 3k of
   test suite changes
v3: https://lore.kernel.org/r/0-v3-402a7d6459de+24b-iommufd_jgg@nvidia.com
 - Rebase to v6.1-rc1
 - Improve documentation
 - Use EXPORT_SYMBOL_NS
 - Fix W1, checkpatch stuff
 - Revise pages.c to resolve the FIXMEs. Create a
   interval_tree_double_span_iter which allows a simple expression of the
   previously problematic algorithms
 - Consistently use the word 'access' instead of user to refer to an
   access from an in-kernel user (eg vfio mdev)
 - Support two forms of rlimit accounting and make the vfio compatible one
   the default in compatability mode (following series)
 - Support old VFIO type1 by disabling huge pages and implementing a
   simple algorithm to split a struct iopt_area
 - Full implementation of access support, test coverage and optimizations
 - Complete COPY to be able to copy across contiguous areas. Improve
   all the algorithms around contiguous areas with a dedicated iterator
 - Functional ENFORCED_COHERENT support
 - Support multi-device groups
 - Lots of smaller changes (the interdiff is 5k lines)
v2: https://lore.kernel.org/r/0-v2-f9436d0bde78+4bb-iommufd_jgg@nvidia.com
 - Rebase to v6.0-rc3
 - Improve comments
 - Change to an iterative destruction approach to avoid cycles
 - Near rewrite of the vfio facing implementation, supported by a complete
   implementation on the vfio side
 - New IOMMU_IOAS_ALLOW_IOVAS API as discussed. Allows userspace to
   assert that ranges of IOVA must always be mappable. To be used by a VMM
   that has promised a guest a certain availability of IOVA. May help
   guide PPC's multi-window implementation.
 - Rework how unmap_iova works, user can unmap the whole ioas now
 - The no-snoop / wbinvd support is implemented
 - Bug fixes
 - Test suite improvements
 - Lots of smaller changes (the interdiff is 3k lines)
v1: https://lore.kernel.org/r/0-v1-e79cd8d168e8+6-iommufd_jgg@nvidia.com

# S390 in-kernel page table walker
Cc: Niklas Schnelle <schnelle@linux.ibm.com>
Cc: Matthew Rosato <mjrosato@linux.ibm.com>
# AMD Dirty page tracking
Cc: Joao Martins <joao.m.martins@oracle.com>
# ARM SMMU Dirty page tracking
Cc: Keqian Zhu <zhukeqian1@huawei.com>
Cc: Shameerali Kolothum Thodi <shameerali.kolothum.thodi@huawei.com>
# ARM SMMU nesting
Cc: Eric Auger <eric.auger@redhat.com>
Cc: Jean-Philippe Brucker <jean-philippe@linaro.org>
# Map/unmap performance
Cc: Daniel Jordan <daniel.m.jordan@oracle.com>
# VDPA
Cc: "Michael S. Tsirkin" <mst@redhat.com>
Cc: Jason Wang <jasowang@redhat.com>
# Power
Cc: David Gibson <david@gibson.dropbear.id.au>
# vfio
Cc: Alex Williamson <alex.williamson@redhat.com>
Cc: Cornelia Huck <cohuck@redhat.com>
Cc: kvm@vger.kernel.org
# iommu
Cc: iommu@lists.linux.dev
# Collaborators
Cc: "Chaitanya Kulkarni" <chaitanyak@nvidia.com>
Cc: Nicolin Chen <nicolinc@nvidia.com>
Cc: Lu Baolu <baolu.lu@linux.intel.com>
Cc: Kevin Tian <kevin.tian@intel.com>
Cc: Yi Liu <yi.l.liu@intel.com>
# s390
Cc: Eric Farman <farman@linux.ibm.com>
Cc: Anthony Krowiak <akrowiak@linux.ibm.com>
Cc: Halil Pasic <pasic@linux.ibm.com>
Cc: Jason Herne <jjherne@linux.ibm.com>
Signed-off-by: Jason Gunthorpe <jgg@nvidia.com>

---
## [notarealdeveloper/cult](https://github.com/notarealdeveloper/cult)@[6a4595b00a...](https://github.com/notarealdeveloper/cult/commit/6a4595b00a659ac3510cb40508985b4f34619ce3)
#### Tuesday 2022-11-15 21:32:52 by 兔兔

Add bin/wode, and bin/bash_completions/wode.sh

For bash, to install the bash completions in this commit:

1. copy or create a symlink from cult/bin/bash_completions to
   $HOME/bin/bash_completions

2. make sure your bashrc contains a section of the form

```
COMPLETIONS="$HOME/bin/bash_completions"

if [[ -d "$COMPLETIONS" ]]; then
    for f in "$COMPLETIONS"/*.sh; do
        source "$f"
    done
}
```

3. fix any typos the bunny made along the way

It is an exercise for the little bird to determine how
to make this work with fancy new-fangled shells like zsh,
you damn kids and your fancy ass zsh, back in my day we
only had /bin/sh and C, and we were happy, grumble grumble
old man complaint noises, get off my lawn.

---
## [Timonkeyn/tgstation](https://github.com/Timonkeyn/tgstation)@[a2577296e6...](https://github.com/Timonkeyn/tgstation/commit/a2577296e62a0f3c335648169a335fe7d3de4bdc)
#### Tuesday 2022-11-15 21:34:35 by RikuTheKiller

Upgrades the Modsuit Adapter Shell (#70286)

Code improvements are much appreciated as some things may be rather hacky.

Adds more options to the currently very limited modsuit adapter shell. Right now you can only select a module and activate (not deploy) the suit.

This has some major problems as you literally can't even deploy the suit to activate it so that's rendered useless and selecting a module is like... kind of a weird input anyways but I won't judge so I left it in. Please comment down below if you'd like for me to add an "Activate Selected Module" input and "On Module Activated" output as those are certainly possible to do. I was just a little torn on how balanced that would be.

Changes:

"Module to Select" input is now an option. You can still use a string input, but simply inserting it into the suit and activating it, then accessing the circuit that way will give you a list of all modules that the modsuit has.
Modsuit quick deploy (RMB) no longer tries to deploy the rest of the pieces when used while the suit is only partially deployed. It will now instead retract the extended pieces. This makes the "Toggle Deployment" input less prone to errors. (Why was it like this in the first place? Having to manually retract the already extended pieces sucks ass.)
Added Inputs:

"Toggle Deployment" is a new signal input that does exactly what it says it does. It simply tries to extend or retract all pieces of the modsuit depending on it's current state.
Added Outputs:

"Activated" is a new number output that outputs 1 if the suit is activated and 0 if it's not.
"Deployed" is a new number output that outputs 1 if all parts of the suit are extended and 0 if they aren't.
"Deployed Parts" is a new string list output that outputs a list of the names of all currently deployed parts.
"On Deploy" is a new signal output that outputs a signal whenever all parts of the suit are deployed or retracted, regardless of the method used.
"Finished Toggling" is a new signal output that outputs a signal whenever the suit has finished activating or deactivating, regardless of the method used.

---
## [newstools/2022-iol](https://github.com/newstools/2022-iol)@[41dd381903...](https://github.com/newstools/2022-iol/commit/41dd38190332cb20a8725fe7c1bd62343251dd9f)
#### Tuesday 2022-11-15 22:12:57 by Billy Einkamerer

Created Text For URL [www.iol.co.za/news/the-star/news/lefahla-lentata-has-received-justice-while-in-her-grave-as-boyfriend-gets-life-sentence-for-her-rape-and-murder-f21ea526-6c97-495d-af9a-0a0a8a595d8c]

---
## [google/guava](https://github.com/google/guava)@[8ca37caac6...](https://github.com/google/guava/commit/8ca37caac631b4e3d02c3064d154940dc7685e54)
#### Tuesday 2022-11-15 22:15:01 by cpovirk

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
PiperOrigin-RevId: 488700624

---
## [matidfk/school](https://github.com/matidfk/school)@[0d514a9ba0...](https://github.com/matidfk/school/commit/0d514a9ba0670390134952bcb5a0acc22d1a34d1)
#### Tuesday 2022-11-15 22:42:55 by mat

revert stupid fuckin traits i hate them silly bitches

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[3582aa77bb...](https://github.com/lessthnthree/tgstation/commit/3582aa77bb68d43c1ebbff9e06226bf3089cb07a)
#### Tuesday 2022-11-15 23:54:36 by LemonInTheDark

Slightly optimizes reagent splashing (#70709)

* Slightly optimizes reagent splashing

Ok so like, before, splashing a reagent performed a rudimentary
floodfill based off atmos connectivity.

This was really slow, because it did it using orange(), and repeated
orange()s to cut out JUST the rim, because we
needed to ensure things were ordered.

I've changed this to use floodfill. I've also moved some code that was
in a second loop into the first one, and replaced a repeated in check
with a single use of &

This is still not optimal for large ranges, because we filter by connectivity first
and THEN view, but it's faster for smaller ones.

BTW I'm also capping the max spread range at 40x40 tiles. If you want
more then 1600 you can rot in hell.

This takes the (uncapped range) cost of deconstructing a highcap tank
from 40 seconds to 0.16.

I hate this codebase

* god damn it

Co-authored-by: san7890 <the@san7890.com>

* whoops that's redundant

Co-authored-by: san7890 <the@san7890.com>

---

