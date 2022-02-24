## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-23](docs/good-messages/2022/2022-02-23.md)


1,843,956 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,843,956 were push events containing 2,925,102 commit messages that amount to 211,472,141 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[2209c36036...](https://github.com/san7890/bruhstation/commit/2209c36036c5c0c303443fd4a6304da9384e5107)
#### Wednesday 2022-02-23 00:38:07 by san7890

Fixes Weird Area Definition on DeltaStation (#64986)

So, there I was. Pondering the blobbosity of Auxiliary Base Construction. Deciphering and unclothing the issue in my mind in order to better comphrehend it. I was there for a few moments, until this ugly beast of a fucking area definition caught my eye:

Hideous. Repugnant. I was relishing the thought of dissecting Auxiliary Base Construction into fifteen million more areas (it _will_ lessen obtusities) when that scraggletooth of an utterly mortifying error forced me into a visceral rage: the likes of which have never been experienced on this planet Earth.

---
## [sumeerbhola/cockroach](https://github.com/sumeerbhola/cockroach)@[255c1fb027...](https://github.com/sumeerbhola/cockroach/commit/255c1fb02708f99fef62b0af719af5e0984d9de3)
#### Wednesday 2022-02-23 01:17:31 by craig[bot]

Merge #71542 #73319 #74077 #76401 #76748

71542: backupccl: Support RESTORE SYSTEM USERS from a backup r=gh-casper a=gh-casper

Support a new variant of RESTORE that recreates system users that don't exist in current cluster from a backup that contains system.users and also grant roles for these users. Example invocation: RESTORE SYSTEM USERS FROM 'nodelocal://foo/1';

Similar with full cluster restore, we firstly restore a temp system database which contains system.users and system.role_members into the restoring cluster and insert users and roles into the current system table from the temp system table.

Fixes: #45358

Release note (sql change): A special flavor of RESTORE, RESTORE SYSTEM USERS FROM ..., is added to support restoring system users from a backup. When executed, the statement recreates those users which are in a backup of system.users but do not currently exist (ignoring those who do) and re-grant roles for users if the backup contains system.role_members.

73319: jobs: Execute scheduled jobs on a single node in the cluster. r=miretskiy a=miretskiy

Execute scheduled jobs daemon on a single node -- namely, the lease
holder for meta1 range lease holder.

Prior to this change, scheduling daemon was running on each node,
polling scheduled jobs table periodically with a `FOR UPDATE` clause.
Unfortunately, job planning phase (namely, the backup planning phase) could
take significant amount of time.  In such situation, the entirety
of the scheduled jobs table would be locked, resulting in inability
to introspect the state of schedules (or jobs) via `SHOW SCHEDULES` or similar
statements.

Furthermore, dropping `FOR UPDATE` clause by itself is not ideal because
that would lead to expensive backup planning being executed on almost every
node, with all but 1 node making progress.

The single node mode is disabled by default, but can be enabled
via a `jobs.scheduler.single_node_scheduler.enabled` setting.

Release Notes: scheduled jobs scheduler now runs on a single node by default
in order to reduce contention on scheduled jobs table.

74077: kvserver: lease transfer in JOINT configuration r=shralex a=shralex

Previously:
1. Removing a leaseholder was not allowed.
2. A VOTER_INCOMING node wasn't able to accept the lease.

Because of (1), users needed to transfer the lease before removing
the leaseholder. Because of (2), when relocating a range from the
leaseholder A to a new node B, there was no possibility to transfer
the lease to B before it was fully added as VOTER. Adding it as a
voter, however, could degrade fault tolerance. For example, if A
and B are in region R1, C in region R2 and D in R3, and we had
(A, C, D), and now adding B to the cluster to replace A results in
the intermediate configuration (A, B, C, D) the failure of R1 would
make the cluster unavailable since no quorum can be established.
Since B can't be added before A is removed, the system would
transfer the lease out to C, remove A and add B, and then transfer
the lease again to B. This resulted a temporary migration of leases
out of their preferred region, imbalance of lease count and degraded
performance.

The PR fixes this, by (1) allowing removing the leaseholder, and
transferring the lease right before we exit the JOINT config. And (2),
allowing a VOTER_INCOMING to accept the lease.

Release note (performance improvement): Fixes a limitation which meant 
that, upon adding a new node to the cluster, lease counts among existing
nodes could diverge until the new node was fully upreplicated.

Here are a few experiments that demonstrate the benefit of the feature.
1. 
> roachprod create local -n 4 // if not already created and staged
> roachprod put local cockroach
> roachprod start local:1-3 --racks=3 // add 3 servers in 3 different racks
> cockroach workload init kv --splits=10000
> roachprod start local:4 --racks=3 // add a 4th server in one of the racks

Without the change (master):
<img width="978" alt="Screen Shot 2022-02-09 at 8 35 35 AM" src="https://user-images.githubusercontent.com/6037719/153458966-609dbb7e-ca3d-4db6-9cfb-adc228f2bdf2.png">

With the change:
<img width="986" alt="Screen Shot 2022-02-08 at 8 46 41 PM" src="https://user-images.githubusercontent.com/6037719/153459366-2d4e2def-37cf-405b-b601-8be57419ae02.png">

We can see that without the patch the number of leases on server 0 (black line) goes all the way to 0 before it goes back up and that the number of leases in other racks goes up, both undesirable. With the patch both things are no longer happening.

2. Same as 1, but with a leaseholder preference of rack 0:

ALTER RANGE default CONFIGURE ZONE USING lease_preferences='[[+rack=0]]';

Without the change (master):
<img width="966" alt="Screen Shot 2022-02-09 at 10 45 27 PM" src="https://user-images.githubusercontent.com/6037719/153460753-bce048f0-f6da-4e21-afdc-317620c035b2.png">

With the change:
<img width="983" alt="leaseholder preferences - with change" src="https://user-images.githubusercontent.com/6037719/153460780-55795866-cf47-404d-b77a-45d9e011f972.png">

We can see that without the change the number of leaseholders in racks 1 and 2 together (not in preferred region) grows from 300 to 1000, then goes back to 40. With the fix it doesn’t grow at all.






76401: pgwire: add server.max_connections public cluster setting r=rafiss a=ecwall

This setting specifies a maximum number of connections that a server can have open at any given time.
<0 - Connections are unlimited (existing behavior)
=0 - Connections are disabled
>0 - Connections are limited
If a new non-superuser connection would exceed this limit, the same error message is
returned as postgres: "sorry, too many connections" with the 53300 error code
that corresponds to "too many connections".

Release note (ops change): An off-by-default server.max_connections cluster
setting has been added to limit the maximum number of connections to a server.

76748: sql: add missing specs to plan diagrams r=rharding6373 a=rharding6373

This change allows missing specs (e.g., RestoreDataSpec and
SplitAndScatterSpec) to be shown in plan diagrams. Before this change a
plan involving these types would result in an error generating the
diagrams. Also added a test to make sure future specs implement the
`diagramCellType` interface, which is required to generate diagrams.

Release note: None


Co-authored-by: Casper <casper@cockroachlabs.com>
Co-authored-by: Yevgeniy Miretskiy <yevgeniy@cockroachlabs.com>
Co-authored-by: shralex <shralex@gmail.com>
Co-authored-by: Evan Wall <wall@cockroachlabs.com>
Co-authored-by: rharding6373 <rharding6373@users.noreply.github.com>

---
## [ViktorKoL/tgstation](https://github.com/ViktorKoL/tgstation)@[906fb0682b...](https://github.com/ViktorKoL/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Wednesday 2022-02-23 01:18:59 by necromanceranne

Ballistic to Energy: Autorifles for Thermal Pistols; Adds .38 Crate to Cargo (#64280)

About The Pull Request
The design doc behind this PR, which is only mildy been deviated from on some of the end particulars. Cobby-Approved! Maintainer Discussed!
https://hackmd.io/@6DbtsAKCTtW_9MByKFjZqg/r1xYKCNOt

Cargo Changes
Cargo has had all WT-550's removed and replaced with Thermal Pistols.
Cargo can now order Thermal Pistols, a kind of energy/ballistic hybrid weapon shooting chunks of altered nanites into people. We couldn't use them in people, so maybe we'll use them as bullets! Magma/Ice bullets, to be exact.
You can, after paying a whopping 4K on a goodie pack (you have to pay from your own personal account) buy a .38 revolver. This is mostly to help some poor detective who lost their revolve in what I'm sure will be an inevitable scramble for ballistics. If even the 4K pricetag isn't enough, at least it requires detective access to open the pack...I hope.
Some of the crates that contained autorifle related items have been changed/removed.

unknown (2)

securarevolver 4 0

Science Changes
Ballistic Weaponry node no longer exists, and has been replaced with Exotic Ammo as both the pre-requisite to other nodes, as well as being able to be researched as soon as the Weaponry node is unlocked and not Advanced Weaponry.

Thermal Pistols
-Fairly average bullet statistics; 10 AP but shooting into Energy armor. 20 damage (Brute for cryo, Burn for inferno). Decent wounding potential, but individually much lower ammo counts than lasers.
-Bought in twinned pairs in a two gun holster (just for normal sized energy guns). They're normal sized.
-Each gun has 8 shots (thereabouts). 16 between two.
-Cryo pistols do a knockdown and extra damage against extremely hot targets. Inferno pistols do an explosion cantered on the target against extremely cold targets.
-The guns are EMP-proof.

Why It's Good For The Game
The current gameplay loop of crew combatants is them relying on backup and retreating as necessary to reload their weapons during fights. The ability to repeatedly harry opponents in the field reloads is something that should be moved away from for crew equipment, as it emphasizes lone wolf tactics and one-man army problems, with boxes full of spare ammo usually allowing any single combatant to outlast multiple foes. In addition, ballistics often are not subject to the same (interesting) limitations of energy weapons, so they're typically a no-brainer choice. We shouldn't have such an easy choice be readily available like that.

The thermal pistols present a more challenging weapon to use as a solo combatant but become far more versatile and potent when paired with a decent buddy and basic level co-ordination. They're not a straightforward choice for every situation, but instead are a weapon employed given the right circumstances for them to shine.

In addition to the gameplay issues that ballistics pose, we're in a goddamn spacegame. Unless the ballistics are noticeably weird (they're not), we should expect that our more advanced research station has some pretty odd guns of the energy variety.

Changelog
🆑 Necromanceranne, quin
add: Adds the Inferno and Cryo Pistols. A hybrid energy/ballistic weapon, to cargo. It can be purchased in either a goodies pack or a normal crate order.
add: Thermal Pistols do more damage and a special based on temperature of the target hit.
add: Inferno pistols cause an explosion when they hit a severely cold target.
add: Cryo pistols cause a knockdown and extra damage if they hit a severely hot target.
add: There is a special nanite pistol, which is admin spawned. Don't tell anyone about the forbidden ballistic energy gun.
add: You can order a .38 revolver as a goodie pack. It is expensive.
del: Removes WT-550's from cargo and related content from the techweb/protolathes.
balance: Exotic Ammo is now much earlier in the tech web to take the place of Ballistic Weaponry.
/🆑

---
## [richinseattle/LibAFL](https://github.com/richinseattle/LibAFL)@[6274ad4594...](https://github.com/richinseattle/LibAFL/commit/6274ad4594af86869f7f678f9321d24851efe634)
#### Wednesday 2022-02-23 01:49:47 by Andrea Fioraldi

Refactor libafl_qemu creating the Emulator struct and post syscall hooks (#430)

* working without asan.rs

* working asan

* update fuzzers

* mremap in snapshot

* sugar

* python

* fix python

* clippy

* fmt

* fuck you loader

---
## [YumeMichi/kernel_oneplus_sm8250](https://github.com/YumeMichi/kernel_oneplus_sm8250)@[37f19071e4...](https://github.com/YumeMichi/kernel_oneplus_sm8250/commit/37f19071e420b273406f4270b29205ef2acb0560)
#### Wednesday 2022-02-23 02:20:06 by alk3pInjection

techpack: display: Handle dim for udfps

Apparently, los fod impl is better than udfps cuz it
has onShow/HideFodView hook, which allows us to toggle
dimlayer seamlessly.

Since udfps only partially supports the former one,
we'd better kill dim in kernel. This is kinda a hack
but it works well, bringing perfect fod experience
back to us.

Also implement a panel status check to ensure that
the dim layer dies when display is off.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Change-Id: I14d028a821e4a776bc62feb5836b3fe012bc808e

---
## [cacogen/tgstation](https://github.com/cacogen/tgstation)@[079f8ac515...](https://github.com/cacogen/tgstation/commit/079f8ac51554bb338ac5826c9d06c8d4bc10be80)
#### Wednesday 2022-02-23 03:38:31 by LemonInTheDark

Adds moveloop bucketing, uses queues for the singulo rather then sleeps (#64418)

Adds a basic bucketing system to move loops.

This should hopefully save a lot of cpu time, and allow for more load while gaining better smoothness.

The idea is very similar to SStimer, but my implementation is much more simple, since I have to worry less about long delays and redundant buckets.
Insertion needs to be cheaper too, since I'm making a system that by design holds a lot of looping things

It comes with some minor tradeoffs, we can't have constant rechecking of loops if a move "fails", not that we really want that anyway
We also lose direct control over the timer var, but I think that's better, don't want people manipulating that directly
Not that it even really worked very well back when we did have it
Removes the sleep from singularity code

Rather then using sleep to store the state of our iteration, we instead queue the iteration in a list.
We then use a custom singulo processing subsystem to call our "digest" proc several times per full eat, with the hope of staying on top of
our queue
This rarely happens because the queue is too large, god why is a sm powered singulo 24x24 tiles.

I've also A: cached our dist checks, and B: Added dist checks to prevent attempting to pull things out of range
This might look a bit worse, but it saves a lot of work

Oh right and I made the singulo unable to eat while it still has tiles to digest. The hope is to prevent
overwork and list explosion.

Hopefully this will prevent singulo server stoppage, though I've seen some other worrying things in testing.

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[c1a7521f0a...](https://github.com/cockroachdb/cockroach/commit/c1a7521f0aba9a58a9762ae198876e9e42885c44)
#### Wednesday 2022-02-23 04:07:19 by craig[bot]

Merge #76165 #76399 #76458 #76643 #76776 #76793 #76835 #76901

76165: dev: log cmd out and err r=postamar a=postamar

This change makes the dev command's --debug flag more useful by printing
a copy of the command's out and err streams to the debug log.

Release note: None

76399: sql: migrate prepared statements during session migration r=otan a=rafiss

fixes https://github.com/cockroachdb/cockroach/issues/76398

See individual commits. The last one contains the business logic changes,
and the rest are just refactors.

Release note (sql change): The crdb_internal.serialize_session and
crdb_internal.deserialize_session now can handle prepared statements.
When deserializing, any prepared statements that existed when the
session was serialized are re-prepared. It is an error to re-prepare a
statement if the current session already has a statement with that name.

76458: geo,sql: add some missing pg error codes r=rafiss a=jordanlewis

This commit adds a bunch of missing pg error codes to builtins. It also
adds missing codes for when the optimizer fails to satisfy an index
hint.

Closes #76454 

Release note (sql change): several error cases in geospatial and other
builtins returned "internal error" pg error codes. They now return more
appropriate error codes. This is a minor change and clients should not
notice.

76643: sql/schemachanger: adopt pausepoints r=chengxiong-ruan a=ajwerner

These are super handy for manual testing.

```sql
root@localhost:26257/defaultdb> set application_name=test;
SET
root@localhost:26257/defaultdb> create table tab (i INT PRIMARY KEY);
CREATE TABLE
root@localhost:26257/defaultdb> set cluster setting jobs.debug.pausepoints = 'schemachanger://root@test/2';
SET CLUSTER SETTING
root@localhost:26257/defaultdb> set experimental_use_new_schema_changer = unsafe_always;
SET
root@localhost:26257/defaultdb> alter table tab add column j int not null default 42;
ERROR: job 737008824216879105 was paused before it completed with reason: pause point "schemachanger://root@test/2" hit
```

Release note: None

76776: scpb,scdecomp,scbuild: remodel elements, use decomposition r=postamar a=postamar

This change adresses some shortcomings of the declarative schema
changer that would have compromised its ability to evolve gracefully in
its current form. Basically these are:
  1. the builder generating targets based off a hybrid descriptor-and-
     element scheme, and
  2. an awkward handling of back-references which precludes doing much
     more than DROP statements correctly.

This change therefore consists of, respectively:
  1. rewriting the builder to hide descriptors from the `scbuildstmt`
     package, instead exposing sets of elements, and
  2. reworking the element model definition by getting rid of
     back-reference elements entirely.

In support of (1) this commit introduces a new `scdecomp` package which,
given a descriptor, will walk a visitor function over all its
constituent elements. This itself is made quite simple by (2) which
largely removes the need to look up referenced descriptors outside of
some mild edge-cases.

This `scdecomp` package is used by the backing structs of the
`scbuildstmt` dependency interfaces to collect a "state-of-the-world"
snapshot of elements upon which the schema change target elements are
layered. This approach lends itself well to caching as the descriptors
remain immutable in the builder.

The rewrite of most of `elements.proto` in support of (2) implies a slew
of cascading changes:
 - the attributes in `screl` need to be adjusted,
 - the lifecyles of the elements in `opgen` have to be adjusted,
 - the dependency rules and no-op rules need to be adjusted,
 - in turn, new operations need to be defined in `scop`, and,
 - in turn, these operations need to be implemented in `scmutationexec`.

Elements are now responsible for updating any back-references that
correspond to their forward references, which effectively pushed that
complexity into these reference update ops in `scmutationexec`. These
have to operate on a best-effort basis, because there are no longer
back-reference elements with dependency rules to enforce convenient
assumptions about the context of their adding or removal. This is
arguably not a bad thing per-se: this new paradigm is "fail hard, fail
fast" which surfaces bugs a lot more quickly than a badly-written
dependency rule would.

The rules themselves fall into cleaner patterns. This commit provides some
tools to express the most common of these. This commit also unifies the
`deprules` and `scopt` packages into a commit `rules` package with full
data-driven test coverage.

Other changes in this commit are peripheral in nature:
  - Working on this change surfaced some deficiencies in the
    cross-referenced descriptor validation logic: we checked that the
    referenced descriptor exists but not that it's not dropped. This
    commit fixes this.
  - The expression validation logic in `schemaexpr` quite reasonably
    used to assume that columns can be found in descriptors;
    unfortunately the builder needs to be able to use this for columns
    which only exist as elements. This commit refactors the entry points
    into this validation logic as a result.
  - Quality-of-life improvements like adding a testing knob used to
    panic TestRollback with an error with a full stack trace when the
    rollback fails.
  - Because back-references don't exist as elements anymore, they also
    don't exist as targets, so we now have schema changer jobs linked to
    descriptors for which there are zero targets. This commit addresses this
    by simply allowing it. This is necessary to lock descriptors to
    prevent any concurrent schema changes which would affect them.

Release note: None


76793: storage: introduce guaranteed durability functionality r=jbowens a=sumeerbhola

This is the CockroachDB plumbing for Pebble's
IterOptions.OnlyReadGuaranteedDurable. It is for use in
the raftLogTruncator https://github.com/cockroachdb/cockroach/pull/76215.

Since most of the exported interfaces in the storage
package use a Reader, we support this via a
DurabilityRequirement parameter on Engine.NewReadOnly,
and not via an iterator option.

There is also a RegisterFlushCompletedCallback method
on Engine which will be used to poll certain durable
state in the raftLogTruncator.

Other than the trivial plumbing, this required some
refactoring of the Reader.MVCCGet* code for Pebble
and pebbleReadOnly. Even though it is deprecated and
primarily/only used in tests, we don't want to have
the durability semantics diverge.

Release note: None

76835: ttljob: add controls to pause TTL jobs r=rafiss a=otan

See individual commits for details.

76901: colexecspan: de-templatize span assembler and use span.Splitter r=RaduBerinde a=RaduBerinde

#### colexecspan: rename span_assembler_tmpl.go to span_assembler.go

Doing this in a separate commit so it's easier to review the changes.

Release note: None

#### colexecspan: de-templatize span assembler

The span assembler code is generated only to inline a piece of code
that has two variants. This change converts it to non-generated code
and simply forks the code paths above the batch loop.

Release note: None

#### colexecspan: use span.Splitter

The span assembler duplicates some of the logic in `span.Splitter`.
Now that the latter is a separate type, we can use it instead.

Release note: None


Co-authored-by: Marius Posta <marius@cockroachlabs.com>
Co-authored-by: Rafi Shamim <rafi@cockroachlabs.com>
Co-authored-by: Jordan Lewis <jordanthelewis@gmail.com>
Co-authored-by: Andrew Werner <ajwerner@cockroachlabs.com>
Co-authored-by: sumeerbhola <sumeer@cockroachlabs.com>
Co-authored-by: Oliver Tan <otan@cockroachlabs.com>
Co-authored-by: Radu Berinde <radu@cockroachlabs.com>

---
## [crawl/crawl](https://github.com/crawl/crawl)@[27774f3ec5...](https://github.com/crawl/crawl/commit/27774f3ec5321291ffb2bb25f326700b77bdd563)
#### Wednesday 2022-02-23 04:52:32 by Nicholas Feinberg

Improve characters' starting kits (Hellmonk)

One of the most interesting and exciting decisions in Dungeon Crawl
is when and where to use your consumable items. In the very early
game, characters may not yet have any consumables, which diminishes
the tactical aspect of the game.

So, let's try to give most characters some options which, if used
wisely, can help them with a tough situation.

- All 'mages' ('pure casters') start with a potion of magic.
- Fighters get an additional potion of might.
- Gladiators get a few throwing weapons, roughly half of what the AM
  throwing start got.
- Monks get two potions of ambrosia. (See, it's divine.)
- Hunters get a throwing net. (Not sure about this one.)
- Brigands get an additional poisoned & curare dart.
- Artificers trade their xom piece for nine charges of iceblast.
- Wanderers get an additional random potion or scroll.
- Delvers get nothing, for now, since I'm already pretty happy with
  how they play. They're a challenge anyway, really. :)
- Berserkers and Cinder Acolytes likewise get nothing. They already
  have perfectly good early game buttons.
- Abyssal Knights start at 60 piety (just over 2*) instead of 38 (just
  over 1*). This should allow them to use Bend Space if needed.
  (I think they're still quite weak.)
- Chaos Knights get Artificer's xom chesspiece.
- Transmuters get a potion of lignification, which should work well
  with their unarmed combat focus. It's also very thematic.
- Warpers and Arkane Markspersons get more boomerangs of dispersal.
- Enchanters get another potion of invisibility.

This should also be a nice compensation for various recent changes that
increased early game difficulty.

---
## [zclkkk/kernel_realme_sm8350](https://github.com/zclkkk/kernel_realme_sm8350)@[9aa959be86...](https://github.com/zclkkk/kernel_realme_sm8350/commit/9aa959be863ab441c88b25615104a35c0d072bdd)
#### Wednesday 2022-02-23 04:53:49 by zclkkk

techpack/display: Kang from OnePlus OSS

* Our display module is broken...
* Fuck you realme

---
## [sevcator/malware](https://github.com/sevcator/malware)@[7b94309fa4...](https://github.com/sevcator/malware/commit/7b94309fa4e4f708c19da712b5c935824748aef7)
#### Wednesday 2022-02-23 05:01:12 by Seva

SuicideMouse - modification sevcatorsha

!! DO NOT LAUNCH ON REAL MACHINE
This is my girl. I love she. This virus
erase your data and kill mbr.
Make your windows is trash.

---
## [csnover/earthquake-rust](https://github.com/csnover/earthquake-rust)@[f1718ecd54...](https://github.com/csnover/earthquake-rust/commit/f1718ecd5484fe3c51133fc62f8deee2abeecb3f)
#### Wednesday 2022-02-23 06:39:41 by Colin Snover

Improve accuracy of Xtra interface

MOA/COM is a design that, on the surface, appears to provide a
well-structured and logical mechanism for building loosely coupled
interoperable components. Spend a few minutes in the guts of this
machine, though, and one will discover it is actually a waking
Matryoshka nightmare of facades and many too many layers of
abstraction and indirection and opaque tokens and callbacks-passed-
to-callbacks.

The experience of trying to follow the flow of code through
multiple layers of vtables, private interfaces, two different
sets of object constructors (neither of which actually does all
of the work themselves, but instead are callbacks passed with GUIDs
which must have been pre-registered beforehand with the size of the
allocation), and some shit called “SecretGlue” that was generated by
Satan’s worst C macros is the opposite of delightful and does not
spark joy.

It perhaps should have been obvious, but actually was not clear
initially, that every time a new Xtra instance is created it also
constructs a *new coclass*, not *just* the interface to a shared
coclass. When I say “should have been obvious”, I do not mean
because there was clearly no way for the API to work otherwise.
Actually, it was rather the opposite: the Xtra manager appears to
create an instance of the Xtra straight away that it stores in a
global cache; the VM routes calls through a function that takes a
reference to the parent Xtra every time; the instance object is
passed in every call *twice* (explicitly, and in the parameters
list); there is a mandatory destructor function which is
automatically invoked by the VM when the last copy of an instance
object is destroyed to notify the COM side that an instance is gone
now. All of these choices make sense in the context where there
*is* a single shared COM object that uses the VM instance object as
a key to find associated data on the other side, but no, that is
not how it works at all, somehow, apparently.

Probably.

“Probably”, because there are at least three ways that
`MoaCreateInstance` will actually try to create a new instance,
and it is possible that one of those *does* actually share a
common object for all of the instances, but that the Xtras that
have been looked at so far only do seem to do it the
COM-class-per-instance way.

“Probably”, because only Lingo Xtras have been evaluated so far;
cast member Xtras might be totally different because they use a
different COM interface and are registered in their own separate
global list.

“Probably”, because I *still* can’t tell you the exact series of
steps that occur to load and instantiate an Xtra interface despite
spending hundreds of hours looking at disassembly and running
debuggers and reading a bunch of the SDK documentation.

So anyway, this commit contains a lot of bad code that just tries
to get close to accurate emulation of the parts of this big brain
90s OOP design that are known to actually be used right now by
some Xtras. It is shameful rage code that mashes things together
until they work well enough. Hopefully later it can be cleaned up.

Thanks for coming to my TED talk.

---
## [Open-Surface-RT/grate-linux](https://github.com/Open-Surface-RT/grate-linux)@[debac8bffb...](https://github.com/Open-Surface-RT/grate-linux/commit/debac8bffb55f01c0ec4340e2df67d78ac065c2a)
#### Wednesday 2022-02-23 07:44:30 by David Hildenbrand

mm: optimize do_wp_page() for exclusive pages in the swapcache

Patch series "mm: COW fixes part 1: fix the COW security issue for THP and swap", v3.

This series attempts to optimize and streamline the COW logic for ordinary
anon pages and THP anon pages, fixing two remaining instances of
CVE-2020-29374 in do_swap_page() and do_huge_pmd_wp_page(): information
can leak from a parent process to a child process via anonymous pages
shared during fork().

This issue, including other related COW issues, has been summarized in [2]:
"
  1. Observing Memory Modifications of Private Pages From A Child Process

  Long story short: process-private memory might not be as private as you
  think once you fork(): successive modifications of private memory
  regions in the parent process can still be observed by the child
  process, for example, by smart use of vmsplice()+munmap().

  The core problem is that pinning pages readable in a child process, such
  as done via the vmsplice system call, can result in a child process
  observing memory modifications done in the parent process the child is
  not supposed to observe. [1] contains an excellent summary and [2]
  contains further details. This issue was assigned CVE-2020-29374 [9].

  For this to trigger, it's required to use a fork() without subsequent
  exec(), for example, as used under Android zygote. Without further
  details about an application that forks less-privileged child processes,
  one cannot really say what's actually affected and what's not -- see the
  details section the end of this mail for a short sshd/openssh analysis.

  While commit 17839856fd58 ("gup: document and work around "COW can break
  either way" issue") fixed this issue and resulted in other problems
  (e.g., ptrace on pmem), commit 09854ba94c6a ("mm: do_wp_page()
  simplification") re-introduced part of the problem unfortunately.

  The original reproducer can be modified quite easily to use THP [3] and
  make the issue appear again on upstream kernels. I modified it to use
  hugetlb [4] and it triggers as well. The problem is certainly less
  severe with hugetlb than with THP; it merely highlights that we still
  have plenty of open holes we should be closing/fixing.

  Regarding vmsplice(), the only known workaround is to disallow the
  vmsplice() system call ... or disable THP and hugetlb. But who knows
  what else is affected (RDMA? O_DIRECT?) to achieve the same goal -- in
  the end, it's a more generic issue.
"

This security issue was first reported by Jann Horn on 27 May 2020 and it
currently affects anonymous pages during swapin, anonymous THP and hugetlb.
This series tackles anonymous pages during swapin and anonymous THP:
* do_swap_page() for handling COW on PTEs during swapin directly
* do_huge_pmd_wp_page() for handling COW on PMD-mapped THP during write
  faults

With this series, we'll apply the same COW logic we have in do_wp_page()
to all swappable anon pages: don't reuse (map writable) the page in
case there are additional references (page_count() != 1). All users of
reuse_swap_page() are remove, and consequently reuse_swap_page() is
removed.

In general, we're struggling with the following COW-related issues:
(1) "missed COW": we miss to copy on write and reuse the page (map it
    writable) although we must copy because there are pending references
    from another process to this page. The result is a security issue.
(2) "wrong COW": we copy on write although we wouldn't have to and
    shouldn't: if there are valid GUP references, they will become out of
    sync with the pages mapped into the page table. We fail to detect that
    such a page can be reused safely, especially if never more than a
    single process mapped the page. The result is an intra process
    memory corruption.
(3) "unnecessary COW": we copy on write although we wouldn't have to:
    performance degradation and temporary increases swap+memory consumption
    can be the result.

While this series fixes (1) for swappable anon pages, it tries to reduce
reported cases of (3) first as good and easy as possible to limit the
impact when streamlining. The individual patches try to describe in which
cases we will run into (3).

This series certainly makes (2) worse for THP, because a THP will now get
PTE-mapped on write faults if there are additional references, even if
there was only ever a single process involved: once PTE-mapped, we'll copy
each and every subpage and won't reuse any subpage as long as the
underlying compound page wasn't split.

I'm working on an approach to fix (2) and improve (3): PageAnonExclusive to
mark anon pages that are exclusive to a single process, allow GUP pins only
on such exclusive pages, and allow turning exclusive pages shared
(clearing PageAnonExclusive) only if there are no GUP pins. Anon pages with
PageAnonExclusive set never have to be copied during write faults, but
eventually during fork() if they cannot be turned shared. The improved
reuse logic in this series will essentially also be the logic to reset
PageAnonExclusive. This work will certainly take a while, but I'm planning
on sharing details before having code fully ready.

#1-#5 can be applied independently of the rest. #6-#9 are mostly only
cleanups related to reuse_swap_page().

Notes:
* For now, I'll leave hugetlb code untouched: "unnecessary COW" might
  easily break existing setups because hugetlb pages are a scarce resource
  and we could just end up having to crash the application when we run out
  of hugetlb pages. We have to be very careful and the security aspect with
  hugetlb is most certainly less relevant than for unprivileged anon pages.
* Instead of lru_add_drain() we might actually just drain the lru_add list
  or even just remove the single page of interest from the lru_add list.
  This would require a new helper function, and could be added if the
  conditional lru_add_drain() turn out to be a problem.
* I extended the test case already included in [1] to also test for the
  newly found do_swap_page() case. I'll send that out separately once/if
  this part was merged.

[1] https://lkml.kernel.org/r/20211217113049.23850-1-david@redhat.com
[2] https://lore.kernel.org/r/3ae33b08-d9ef-f846-56fb-645e3b9b4c66@redhat.com

This patch (of 9):

Liang Zhang reported [1] that the current COW logic in do_wp_page() is
sub-optimal when it comes to swap+read fault+write fault of anonymous
pages that have a single user, visible via a performance degradation in
the redis benchmark.  Something similar was previously reported [2] by
Nadav with a simple reproducer.

After we put an anon page into the swapcache and unmapped it from a single
process, that process might read that page again and refault it read-only.
If that process then writes to that page, the process is actually the
exclusive user of the page, however, the COW logic in do_co_page() won't
be able to reuse it due to the additional reference from the swapcache.

Let's optimize for pages that have been added to the swapcache but only
have an exclusive user.  Try removing the swapcache reference if there is
hope that we're the exclusive user.

We will fail removing the swapcache reference in two scenarios:
(1) There are additional swap entries referencing the page: copying
    instead of reusing is the right thing to do.
(2) The page is under writeback: theoretically we might be able to reuse
    in some cases, however, we cannot remove the additional reference
    and will have to copy.

Note that we'll only try removing the page from the swapcache when it's
highly likely that we'll be the exclusive owner after removing the page
from the swapache.  As we're about to map that page writable and redirty
it, that should not affect reclaim but is rather the right thing to do.

Further, we might have additional references from the LRU pagevecs, which
will force us to copy instead of being able to reuse.  We'll try handling
such references for some scenarios next.  Concurrent writeback cannot be
handled easily and we'll always have to copy.

While at it, remove the superfluous page_mapcount() check: it's
implicitly covered by the page_count() for ordinary anon pages.

[1] https://lkml.kernel.org/r/20220113140318.11117-1-zhangliang5@huawei.com
[2] https://lkml.kernel.org/r/0480D692-D9B2-429A-9A88-9BBA1331AC3A@gmail.com

Link: https://lkml.kernel.org/r/20220131162940.210846-2-david@redhat.com
Signed-off-by: David Hildenbrand <david@redhat.com>
Reported-by: Liang Zhang <zhangliang5@huawei.com>
Reported-by: Nadav Amit <nadav.amit@gmail.com>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Vlastimil Babka <vbabka@suse.cz>
Cc: Hugh Dickins <hughd@google.com>
Cc: David Rientjes <rientjes@google.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Jason Gunthorpe <jgg@nvidia.com>
Cc: Mike Kravetz <mike.kravetz@oracle.com>
Cc: Mike Rapoport <rppt@linux.ibm.com>
Cc: Yang Shi <shy828301@gmail.com>
Cc: Kirill A. Shutemov <kirill.shutemov@linux.intel.com>
Cc: Jann Horn <jannh@google.com>
Cc: Michal Hocko <mhocko@kernel.org>
Cc: Rik van Riel <riel@surriel.com>
Cc: Roman Gushchin <guro@fb.com>
Cc: Andrea Arcangeli <aarcange@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Don Dutile <ddutile@redhat.com>
Cc: Christoph Hellwig <hch@lst.de>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Jan Kara <jack@suse.cz>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Stephen Rothwell <sfr@canb.auug.org.au>

---
## [lnussel/systemd](https://github.com/lnussel/systemd)@[de90700f36...](https://github.com/lnussel/systemd/commit/de90700f36f2126528f7ce92df0b5b5d5e277558)
#### Wednesday 2022-02-23 07:51:19 by Lennart Poettering

pid1: set SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon

There's currently a deadlock between PID 1 and dbus-daemon: in some
cases dbus-daemon will do NSS lookups (which are blocking) at the same
time PID 1 synchronously blocks on some call to dbus-daemon. Let's break
that by setting SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon,
which will disable synchronously blocking varlink calls from nss-systemd
to PID 1.

In the long run we should fix this differently: remove all synchronous
calls to dbus-daemon from PID 1. This is not trivial however: so far we
had the rule that synchronous calls from PID 1 to the dbus broker are OK
as long as they only go to interfaces implemented by the broke itself
rather than services reachable through it. Given that the relationship
between PID 1 and dbus is kinda special anyway, this was considered
acceptable for the sake of simplicity, since we quite often need
metadata about bus peers from the broker, and the asynchronous logic
would substantially complicate even the simplest method handlers.

This mostly reworks the existing code that sets SYSTEMD_NSS_BYPASS_BUS=
(which is a similar hack to deal with deadlocks between nss-systemd and
dbus-daemon itself) to set SYSTEMD_NSS_DYNAMIC_BYPASS=1 instead. No code
was checking SYSTEMD_NSS_BYPASS_BUS= anymore anyway, and it used to
solve a similar problem, hence it's an obvious piece of code to rework
like this.

Issue originally tracked down by Lukas Märdian. This patch is inspired
and closely based on his patch:

       https://github.com/systemd/systemd/pull/22038

Fixes: #15316
Co-authored-by: Lukas Märdian <slyon@ubuntu.com>

---
## [ngyongkang/portfolio](https://github.com/ngyongkang/portfolio)@[8e763d7d35...](https://github.com/ngyongkang/portfolio/commit/8e763d7d3522c1c7cba3d1a51c19d6041702280f)
#### Wednesday 2022-02-23 08:28:14 by Ng Yong Kang

Most annoying feature to add, Joke component, freaking 10 jokes. remember nested values in API 23/2/2022 4:27 PM

---
## [extraes/BW-Chaos](https://github.com/extraes/BW-Chaos)@[10ee95d68b...](https://github.com/extraes/BW-Chaos/commit/10ee95d68bd6a27ed0d9e575571d129abf172cd9)
#### Wednesday 2022-02-23 08:31:07 by extraes

rewrite JoinBytes and SplitBytes to put a variable size header at the start declaring how many byte arrays need to be created/are in a joined byte array
this took many days and too much fucking effort
abstraction is a bitch, but i wrote this by myself with the only instance of linq being the .sum() call in SplitBytes.
its fucking magical honestly.

---
## [davidhildenbrand/linux](https://github.com/davidhildenbrand/linux)@[6f1ee7eeef...](https://github.com/davidhildenbrand/linux/commit/6f1ee7eeefe5339099c30ab15c9c49388f5e8d04)
#### Wednesday 2022-02-23 08:38:19 by David Hildenbrand

mm: remember exclusively mapped parts of anonymous folios with PG_anon_exclusive

Let's mark exclusively mapped parts of anonymous folios with
PG_anon_exclusive as exclusive, and use that information to make GUP pins
stay in sync with the page mapped into the page table even if the
page table entry gets -protected, optimizing our COW logic. Parts of
anonymous folios that are mapped read-only and marked exclusive can simply
get mapped writable by the write fault handler without additional checks
and without taking the page lock.

As already documented, PG_anon_exclusive is usually only expressive in
combination with a page table entry: it's treated like an additional
page table entry bit that applies to the part of the anonymous folio
mapped via that page table entry. Let's use the rmap code to handle most of
the PG_anon_exclusive logic.

If a writable, present page table entry points at an anonymous (sub)page,
that (sub)page has to be set PG_anon_exclusive. If GUP wants to take a
reliably pin (FOLL_PIN) on an anonymous page references via a present
page table entry, it must only pin if PG_anon_exclusive is set for the
mapped (sub)page.

This patch doesn't adjust GUP, so this is only implicitly handled for
FOLL_WRITE (because the page table entry has to be writable and
consequently PG_anon_exclusive), successive patches will
teach GUP to also respect it for FOLL_PIN without !FOLL_WRITE.

Whenever (parts of) anonymous folio are to be shared (fork(), KSM),
or when temporarily unmapping (parts of) an anonymous folio (swap,
migration), the relevant PG_anon_exclusive bit has to be cleared to mark
that part of the anonymous folio as possibly shared. Clearing will fail if
there are GUP pins on the page:
* For fork(), this means having to copy the page and not being able to
  share it. fork() protects against concurrent GUP using the PT lock and
  the src_mm->write_protect_seq.
* For KSM, this means sharing will fail. For swap this means, unmapping
  will fail, For migration this means, migration will fail early. All
  three cases protect against concurrent GUP using the PT lock and a
  proper clear/invalidate+flush of the relevant page table entry.

PTE-mapping a PMD-mapped THP is a bit "more complicated", but it
essentially works just by replicating the information from the PMD to the
PTEs.

This fixes memory corruptions reported for FOLL_PIN | FOLL_WRITE, when a
pinned page gets mapped R/O and the successive write fault ends up
replacing the page instead of reusing it. It improves the situation for
O_DIRECT/vmsplice/... that still use FOLL_GET instead of FOLL_PIN,
if fork() is *not* involved, however migration and swapout are still
problematic. Properly using FOLL_PIN instead of FOLL_GET for these
GUP users will fix the issue for them.

I. Basic Handling

I.1. Fresh anonymous pages

page_add_new_anon_rmap() and hugepage_add_new_anon_rmap() will mark the
given page exclusive via __page_set_anon_rmap(exclusive=1). As that is
the mechanism fresh anonymous pages come into life (besides migration
code where we copy the page->mapping), all fresh anonymous pages will
start out as exclusive.

I.2. COW reuse handling of anonymous pages

When a COW handler stumbles over a (sub)page that's marked exclusive, it
simply reuses it. Otherwise, the handler tries harder under page lock to
detect if the (sub)page is exclusive and can be reused. If exclusive,
page_move_anon_rmap() will mark the given (sub)page exclusive.

Note that hugetlb code does not yet check for PageAnonExclusive(), as it
still uses the old COW logic that is prone to the COW security issue
because hugetlb code cannot really tolerate unnecessary/wrong COW as
huge pages are a scarce resource. Future work, once O_DIRECT and friends
are handled accordingly.

I.3. Migration handling

try_to_migrate() has to try marking an exclusive anonymous page shared
via page_try_share_anon_rmap(). If it fails because there are GUP pins
on the page, unmap fails. migrate_vma_collect_pmd() and
__split_huge_pmd_locked() are handled similarly.

Writable migration entries implicitly point at shared anonymous pages.
For readable migration entries that information is stored via a new
"readable-exclusive" migration entry, specific to anonymous pages.

When restoring a migration entry in remove_migration_pte(), information
about exlusivity is detected via the migration entry type, and
RMAP_EXCLUSIVE is set accordingly for
page_add_anon_rmap()/hugepage_add_anon_rmap() to restore that
information.

I.4. Swapout handling

try_to_unmap() has to try marking the mapped part of an exclusive anonymous
folio possibly shared via page_try_share_anon_rmap(). If it fails because
there are GUP pins on the page, unmap fails. For now, information about
exclusivity is lost. In the future, we might want to remember that
information in the swap entry in some cases, however, it requires more
thought, care, and a way to store that information in swap entries.

I.5. Swapin handling

do_swap_page() will never stumble over exclusive anonymous pages in the
swap cache, as try_to_migrate() prohibits that. do_swap_page() always has
to detect manually if an anonymous page is exclusive and has to set
RMAP_EXCLUSIVE for page_add_anon_rmap() accordingly.

I.6. THP handling

__split_huge_pmd_locked() has to move the information about exclusivity
from the PMD to the PTEs.

a) In case we have a readable-exclusive PMD migration entry, simply insert
readable-exclusive PTE migration entries.

b) In case we have a present PMD entry and we don't want to freeze
("convert to migration entries"), simply forward PG_anon_exclusive to
all sub-pages, no need to temporarily clear the bit.

c) In case we have a present PMD entry and want to freeze, handle it
similar to try_to_migrate(): try marking the page shared first. In case
we fail, we ignore the "freeze" instruction and simply split ordinarily.
try_to_migrate() will properly fail because the THP is still mapped via
PTEs.

When splitting a compound anonymous folio (THP), the information about
exclusivity is implicitly handled via the migration entries: no need to
replicate PG_anon_exclusive manually.

I.7. fork() handling

fork() handling is relatively easy, because PG_anon_exclusive is only
expressive for some page table entry types.

a) Present anonymous pages

page_try_dup_anon_rmap() will mark the given subpage shared -- which
will fail if the page is pinned. If it failed, we have to copy (or
PTE-map a PMD to handle it on the PTE level).

Note that device exclusive entries are just a pointer at a PageAnon()
page. fork() will first convert a device exclusive entry to a present
page table and handle it just like present anonymous pages.

b) Device private entry

Device private entries point at PageAnon() pages that cannot be mapped
directly and, therefore, cannot get pinned.

page_try_dup_anon_rmap() will mark the given subpage shared, which
cannot fail because they cannot get pinned.

c) HW poison entries

PG_anon_exclusive will remain untouched and is stale -- the page table
entry is just a placeholder after all.

d) Migration entries

Writable and readable-exclusive entries are converted to readable
entries: possibly shared.

I.8. mprotect() handling

mprotect() only has to properly handle the new readable-exclusive
migration entries:

When write-protecting a migration entry that points at an anonymous
page, remember the information about exclusivity via the
"readable-exclusive" migration entry type.

II. Migration and GUP-fast

Whenever replacing a present page table entry that maps (parts of)
an anonymous folio that is marked exclusive, we have to synchronize against
GUP-fast by a proper clear/invalidate+flush to make the following scenario
impossible:

1. try_to_migrate() places a migration entry after checking for GUP pins
   and clears exclusivity information on the page.
2. GUP-fast pins the page due to lack of synchronization
3. fork() converts the "writable/readable-exclusive" migration entry into a
   readable migration entry
4. Migration fails due to the GUP pin (failing to freeze the refcount)
5. Migration entries are restored. PG_anon_exclusive is lost

-> We have a pinned page that is not marked exclusive anymore.

Note that we move information about exclusiveness from the page to the
migration entry as it otherwise highly overcomplicates fork() and
PTE-mapping a THP.

III. Swapout and GUP-fast

Whenever replacing a present page table entry that maps (parts of)
an anonymous folio that is marked exclusive, we have to synchronize against
GUP-fast by a proper clear/invalidate+flush to make the following scenario
impossible:

1. try_to_unmap() places a swap entry after checking for GUP pins and
   clears exclusivity information on the page.
2. GUP-fast pins the page due to lack of synchronization.

-> We have a pinned page that is not marked exclusive anymore.

If we'd ever store information about exclusivity in the swap entry,
similar to migration handling, the same considerations as in II would
apply. This is future work.

RFC notes: I'd love to split this up, but it's not straight forward
because it all interacts.

Signed-off-by: David Hildenbrand <david@redhat.com>

---
## [biosimulators/Biosimulators_utils](https://github.com/biosimulators/Biosimulators_utils)@[222c5323cb...](https://github.com/biosimulators/Biosimulators_utils/commit/222c5323cb35fd153514ffb751faf9310b3dacc3)
#### Wednesday 2022-02-23 08:51:29 by Lucian Smith

Fix for #96: consolidate warnings

This is not a general fix for consolidating warnings, but consolidates two sets of warnings, and fixes a third.

* The SBML warnings are now consolidated by error number.
* The ModelChange 'cannot validate XPath' messages are now simply "Model change XPaths are currently not validated."  This is because the code does not even attempt to validate ModelChange XPaths.
* The DataGenerator code now checks to make sure that there aren't *structural* ModelChanges in the referenced model instead of checking to see if there are *any* ModelChanges.  ModelChanges that change attributes or are of type ComputeChange will not invalidate any other XPath in the SED-ML, unlike the AddXML, ReplaceXML, and RemoveXML changes.  Fortunately, the latter are rare to nonexistent.

...except that I now realize as I type this that a ChangeAttribute could change the ID of an element, making an XPath that relied on that attribute invalid.  But honestly, if you do that, and biosimulators_utils tells you that you have an invalid XPath, I think you deserve it.  I can't see it actually happening in the wild.

However, I do see the danger, and perhaps the goal eventually was to *apply* the ModelChanges before validating XPaths.  Maybe we can keep this approach until that day?

The fix could also be applied to the ModelChange XPath validation:  check to ensure that no structural changes were present, and if not, attempt to validate the XPaths.

The final change is that I changed the text 'could be invalid' to 'generated warnings', because the former seems a little hyperbolic, and many warnings *cannot* make the file invalid; they indicate something else might be wrong.  I feel like the user should be able to peruse the warnings as they are and decide for themselves whether the warnings indicate there might be something invalid present.  (This is particularly true for SBML:  *No* warning indicates that the file may be invalid.  All invalid models are caught with errors, not warnings.  If you prefer the 'may be invalid' wording in general, I request that you leave it for SBML, at least.)

The design of collecting warnings by type could be also applied to errors, but errors are more serious, and always need to all be fixed.  The specific messages indicating where each error comes from I feel are worth the extra potential wordiness of some design error resulting in walls of text.

---
## [newstools/2022-iol](https://github.com/newstools/2022-iol)@[2e58b96b29...](https://github.com/newstools/2022-iol/commit/2e58b96b29aab27965c4e0a2270336ba7c00938b)
#### Wednesday 2022-02-23 08:53:39 by Billy Einkamerer

Created Text For URL [www.iol.co.za/news/news/south-africa/eastern-cape/mothers-boyfriend-sentenced-to-20-years-imprisonment-for-rape-of-girl-5-1555d418-549c-4138-bb99-03a6a9fe2686]

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[a88c950352...](https://github.com/cyberitsolutions/bootstrap2020/commit/a88c950352b79f7f7b4c2c7adf77e3690e36dcbd)
#### Wednesday 2022-02-23 09:12:59 by Trent W. Buck

inkscape doc: remove unusable 0.91 extension hooks

16:23 <twb> 16:22 <twb> So now that the help URLs are implemented in C++ instead of python "extensions", I can't see how to change the URLs from https://X to file:///Y without recompiling the entire inkscape package
16:24 <twb> https://sources.debian.org/src/inkscape/1.1.1-2%7Ebpo11+1/src/verbs.cpp/#L2051-L2101
16:27 <twb> I put "echo "$@" >/tmp/delete-me" at the top of /usr/bin/xdg-open, and Inkscape > Help > Manual does not cause /tmp/delete-me to exist
16:27 <twb> So can't hook it there
16:29 <twb> ron: I want you to say "yes, I accept this regression".  Inkscape's documentation is all online.  To keep [REDACTED] happy, we hacked it so Inkscape's Help menu would open local copies we downloaded.  I can still download, but I cannot hack the menu anymore.
16:29 <twb> ron: so if $site wants inkscape help to work in Debian 11, they will need to have internet, and whitelist stuff in squid access rules
16:30 <twb> The only "show stopper" one I think is really annoying is: https://inkscape.org/doc/keys-1.1.x.html
16:30 <ron> ah, I'm fine with whitelisting the inkscape doc
16:30 <twb> OK cool
16:30 <ron> implying they must have net access
16:30 <ron> [REDACTED] misses out
16:30 <ron> boo hoo
16:31 <twb> The other compromise thing I could do is make a start menu item "Inkscape Documentation" that just opens chromium.
16:31 <twb> That's not hard
16:31 <mike> twb: Did you try exo-open instead of xdg-open? That's the other one I see pop up every now and then
16:32 <twb> AFAIK xdg-open is what runs exo-open
16:32 <twb> I was doing a quick-and-dirty test on my gnome environment so I didn't test that
16:33 <mike> xdg does call exo, but doesn't mean things can't call it directly
16:34 <twb> fair
16:34 <mike> It definitely honours XFCE's "preferred applications" setting. Inkscape opened Chrome, then I changed it from Chrome to Chromium and Inkscape opened Chromium
16:34 <twb> I don't *really* want to intercept every call to xdg-open/exo-open anyway
16:37 <mike> twb: Got this by stracing it: [pid 174670] execve("/bin/sh", ["/bin/sh", "-e", "-u", "-c", "export GIO_LAUNCHED_DESKTOP_FILE_PID=$$; exec \"$@\"", "sh", "exo-open", "--launch", "WebBrowser", "http://tavmjong.free.fr/INKSCAPE/MANUAL/html/index.php"], 0x5596c8443910 /* 54 vars */ <unfinished ...>
16:37 <mike> Which then called this: [pid 174670] execve("/usr/bin/exo-open", ["exo-open", "--launch", "WebBrowser", "http://tavmjong.free.fr/INKSCAPE/MANUAL/html/index.php"], 0x564af10ac068 /* 55 vars */) = 0
16:37 <twb> mike: ah thanks
16:37 <twb> So OK we can fix this
16:37 <mike> Not worth digging any deeper into that path
16:38 <mike> We could wrap exo-open, yeah
16:38 <mike> Not sure I like it, but it's viable

---
## [bunkercoin/bunkercoin](https://github.com/bunkercoin/bunkercoin)@[6ab5b59916...](https://github.com/bunkercoin/bunkercoin/commit/6ab5b59916453b0e4e5988c54b9294e6442a8504)
#### Wednesday 2022-02-23 09:14:32 by IdotMaster1

Revert "Here we go! This is it! (Soon)"

This reverts commit b070522fa9d8031686f67b69c0b3993571c1841c.

OH MY GOD IM A FUCKING MORON

---
## [Adien7368/purescript](https://github.com/Adien7368/purescript)@[f36ff2a984...](https://github.com/Adien7368/purescript/commit/f36ff2a984e7743b8a0967becb9dee5d684fc30a)
#### Wednesday 2022-02-23 10:54:05 by Harry Garrood

Drop hpack, make it easier to use cabal-install (#3933)

Stack offers a relatively poor developer experience on this repository
right now. The main issue is that build products are invalidated far
more often than they should be. cabal-install is better at this, but
using cabal-install together with hpack is a bit awkward.

Additionally, hpack isn't really pulling its weight these days. Current
versions of stack recommend that you check your generated cabal file in,
which is a huge pain as you have to explain to contributors to please
leave the cabal file alone and edit package.yaml instead (the comment
saying the file is auto-generated is quite easy to miss).

Current versions of Cabal also solve the issues which made hpack
appealing in the first place, namely:

- common stanzas mean you don't have to repeat yourself for things like
  -Wall or dependencies
- tests are run from inside a source distribution by default, which
  means that if you forget to include something in extra-source-files
  you find out when you run the tests locally, rather than having to
  wait for CI to fail
- the globbing syntax is slightly more powerful (admittedly not quite as
  powerful as hpack's, but you can use globs like tests/**/*.purs now,
  which gets us close enough to hpack that the difference is basically
  negligible).

We do still need to manually maintain exposed-modules lists, but I am
happy to take that in exchange for the build tool not invalidating our
build products all the time.

This PR drops hpack in favour of manually-maintained Cabal files,
so that it's easier to use cabal-install when working on the compiler.
Stack is still the only officially supported build tool though - the
CI, contributing, and installation docs all still use Stack.

Stack also works a little better now than it used to, because I think one of
the causes of unnecessary rebuilds was us specifying optimization flags
in the Cabal file. (Newer versions of Cabal warn you not to do this, so
I think this might be a known issue). To ensure that release builds are
built with -O2, I've updated the stack.yaml file to specify that -O2
should be used.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[2e21c2c3cb...](https://github.com/odoo-dev/odoo/commit/2e21c2c3cb9664c45e8ce9115df68e47611f88b4)
#### Wednesday 2022-02-23 11:09:15 by Julien Castiaux

[REF] core: HTTPocalypse (12) web ir.http & login

This commit is the 12th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

The web module is twofold, on one side there are many controllers: /,
/web, /web/login, /web/database/selector, /web/dataset/call_kw, etc, on
the other side there is `session_info`: the method responsible to create
the web client's environ.

This module is kinda an exception as it is (with base) a server wide
module. In the case of the HTTP framework, it means that the controllers
of web are always accessible, i.e. going to / or /web/login will never
return a 404 Not Found even if the user is not connected to a database.

This is both a blessing and a curse. It is a blessing because the
controllers are always accessible it means that a new users can freely
access those routes. It is a curse because *any* user can access them,
even user who don't have a session yet thus who are not connected to a
database yet. From a developer standpoint, we have to put extra care to
correct serve users with and without a database. An example is the
/web/login route, the login/password pair is stored in a database,
without database it is impossible to validate a user login but users can
still access this route without db.

To solve this problem, there is the `ensure_db` function. This function
attempts to find a database using various sources (?db= query-string,
session db, mono db) and to save it on the user session. In case no db
is found, the user is redirected to the database selector. In a way,
this function grants a database to the user in a seamingly experience.
In a way, this function brings a welcome differentiation between
`auth='none'` with a database and `auth='none'` without a database. Such
differentiation only matters for the server wide modules as "regular"
module controllers are only accessible via the ir.http routing map, i.e.
it is not possible to declare a nodb controller outside of server wide
modules.

An important changement is the `session.authenticate` method, before it
was possible to call the method when the cursor was not yet initialized,
authenticate would open a cursor against the given database, setup a
registry and an environment and ultimately save everything on the
current request. Because the cursor is now greedily created, it is no
more possible to update the request environment when authenticating on
another database.

PR: odoo#78857
Task: 2571224

---
## [JulianKniephoff/tobira](https://github.com/JulianKniephoff/tobira)@[d961e0d934...](https://github.com/JulianKniephoff/tobira/commit/d961e0d9345b0785171c7f6018596d45f12668eb)
#### Wednesday 2022-02-23 11:53:31 by Lukas Kalbertodt

Improve design of user info in header for logged-in users

On mobile, the icon changed to have a user with a green checkmark next
to it, better indicating that the user is logged in. On desktop, that
icon is also shown with the text "logged in as: <name>" left of it. The
text and the icon both make the user menu appear.

This is better than the previous version in my opinion. For one, I think
it looks fresher. But more importantly, the user name being in this
button box was weird, and the user menu touching that button then is
also weird. Since the user box was limited in size, but the size of the
menu was independent, it would often be a size mismatch which looked
really ugly. I don't think the original design was fixable, really.
That's why I implemented this now.

---
## [AlejandroPla/MUSDOS](https://github.com/AlejandroPla/MUSDOS)@[e4cc8175e6...](https://github.com/AlejandroPla/MUSDOS/commit/e4cc8175e605176b9f579126eaa56bbc7efe524b)
#### Wednesday 2022-02-23 12:00:23 by Alejandro Placer

Luke, did I ever tell you about Ahsoka Tano?

She was your father’s exotic teenage alien apprentice, a fine piece of jailbait from a more civilized age. She had the tightest body and the perkiest little breasts in the galaxy; barely legal in most systems. Anakin and I used to doubleteam her at the end of every successful campaign during the Clone Wars, and once in a while we’d even have the entire 501st run a train over her, part of official Jedi “training” of course. In time, she learned how to handle a meatsaber better than anyone in the Jedi Temple. She wore a miniskirt every day so we told her there were no panties in space, and since she was constantly doing acrobatics you’d get a glimpse of her orange pussy mid fight as she’d do a flip while slicing a B2 Super Battledroid in half. It was surreal. We taught her to grip her weapon backwards like a dildo and she constantly got captured by pirates and slavers almost every other day. It was ridiculous, like a constant porno Luke, you have no idea. And she was a good friend.

---
## [osamuaoki/qmk_firmware](https://github.com/osamuaoki/qmk_firmware)@[41566d4bdd...](https://github.com/osamuaoki/qmk_firmware/commit/41566d4bddc2df8a2312e2e7c2a66644ca7abcd7)
#### Wednesday 2022-02-23 12:04:33 by Osamu Aoki

Format update and note

Note: Although these 2 lines should move to // Magic section, doinso may
cause trouble.  (My development time vague memory:  Back slash and back
space became swapped.  Since others had MAGIC_TOGGLE_CONTROL_CAPSLOCK
here, I assume this is the least invasive (but ugly patch.)

Signed-off-by: Osamu Aoki <osamu@debian.org>

---
## [KhannchanBalanarasimhan/Machine_learning](https://github.com/KhannchanBalanarasimhan/Machine_learning)@[a65fba4b17...](https://github.com/KhannchanBalanarasimhan/Machine_learning/commit/a65fba4b1741c0a4df3360ddcc4e6ae1a45818ca)
#### Wednesday 2022-02-23 13:22:54 by Kay

Add files via upload


Heart Disease Prediction

Abstract:
Heart disease is easier to treat when it is detected in the early stages. Machine learning techniques may aid a more efficient analysis in the prediction of the disease. Moreover, this prediction is one of the most central problems in medicine, as it is one of the leading diseases related to an unhealthy lifestyle. So, an early prediction of this disease will be useful for a cure or aversion.


Problem Statement:
Analyze the heart disease dataset to explore the machine learning algorithms and build decision tree model to predict the disease.


Dataset Information:
Each attribute in the heart disease dataset is a medical risk factor.

Variable Description:

Column	Description
age	Age of the patient
gender	Gender of the patient - (0,1) - (Male, Female)
chest_pain	It refers to the chest pain experienced by the patient -(0,1,2,3)
rest_bps	Blood pressure of the patient while resting(in mm/Hg)
cholesterol	Patient's cholesterol level (in mg/dl)
fasting_blood_sugar	The blood sugar of the patient while fasting
rest_ecg	Potassium level (0,1,2)
thalach	The patient’s maximum heart rate
exer_angina	It refers to exercise-induced angina - (1=Yes, 0=No)
 

old_peak	It is the ST depression induced by exercise relative to rest(ST relates to the position on ECG plots)
slope	It refers to the slope of the peak of the exercise ST-Segment- (0,1,2)
ca	Number of major vessels - (0,1,2,3,4)
thalassemia	It refers to thalassemia which is a blood disorder - (0,1,2,3)
target	The patient has heart disease or not - (1=Yes, 0=No)



Scope:
●	Understand data by performing exploratory data analysis
●	Training and building classification algorithms to predict heart disease
●	Understand various model performance metrics and measure the performance of each model

Learning Outcome:
The students should be able to predict heart disease from medical records with the help of classification models. They should also be able to perform EDA and re-build the model and check if there is any significant change in the predictive scores.

---
## [alphagov/govuk_publishing_components](https://github.com/alphagov/govuk_publishing_components)@[4858ef0ed3...](https://github.com/alphagov/govuk_publishing_components/commit/4858ef0ed393b4571ef367e375f18dcb188c897f)
#### Wednesday 2022-02-23 14:18:16 by Kevin Dew

Clobber assets before running jasmine tests

I'm adding this in because we use globbing to match what files to test.
I'm concerned that without this we're at risk of the same files being
included multiple times (say you have application-1234.js, then edit it
and end up with application-2345.js)

It's a bit of a pain to do a clobber first as it means you'll always
have to experience the cost of compiling assets each test run, however
this is preferable to tests liable to fail.

---
## [Reinazhard/android_kernel_xiaomi_whyred](https://github.com/Reinazhard/android_kernel_xiaomi_whyred)@[73a9a2959f...](https://github.com/Reinazhard/android_kernel_xiaomi_whyred/commit/73a9a2959f3252dac32a9e90f1e4369b8c141c47)
#### Wednesday 2022-02-23 16:37:44 by Jason A. Donenfeld

random: use linear min-entropy accumulation crediting

30e37ec516ae ("random: account for entropy loss due to overwrites")
assumed that adding new entropy to the LFSR pool probabilistically
cancelled out old entropy there, so entropy was credited asymptotically,
approximating Shannon entropy of independent sources (rather than a
stronger min-entropy notion) using 1/8th fractional bits and replacing
a constant 2-2/√𝑒 term (~0.786938) with 3/4 (0.75) to slightly
underestimate it. This wasn't superb, but it was perhaps better than
nothing, so that's what was done. Which entropy specifically was being
cancelled out and how much precisely each time is hard to tell, though
as I showed with the attack code in my previous commit, a motivated
adversary with sufficient information can actually cancel out
everything.

Since we're no longer using an LFSR for entropy accumulation, this
probabilistic cancellation is no longer relevant. Rather, we're now
using a computational hash function as the accumulator and we've
switched to working in the random oracle model, from which we can now
revisit the question of min-entropy accumulation, which is done in
detail in <https://eprint.iacr.org/2019/198>.

Consider a long input bit string that is built by concatenating various
smaller independent input bit strings. Each one of these inputs has a
designated min-entropy, which is what we're passing to
credit_entropy_bits(h). When we pass the concatenation of these to a
random oracle, it means that an adversary trying to receive back the
same reply as us would need to become certain about each part of the
concatenated bit string we passed in, which means becoming certain about
all of those h values. That means we can estimate the accumulation by
simply adding up the h values in calls to credit_entropy_bits(h);
there's no probabilistic cancellation at play like there was said to be
for the LFSR. Incidentally, this is also what other entropy accumulators
based on computational hash functions do as well.

So this commit replaces credit_entropy_bits(h) with essentially `total =
min(POOL_BITS, total + h)`, done with a cmpxchg loop as before.

What if we're wrong and the above is nonsense? It's not, but let's
assume we don't want the actual _behavior_ of the code to change much.
Currently that behavior is not extracting from the input pool until it
has 128 bits of entropy in it. With the old algorithm, we'd hit that
magic 128 number after roughly 256 calls to credit_entropy_bits(1). So,
we can retain more or less the old behavior by waiting to extract from
the input pool until it hits 256 bits of entropy using the new code. For
people concerned about this change, it means that there's not that much
practical behavioral change. And for folks actually trying to model
the behavior rigorously, it means that we have an even higher margin
against attacks.

Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Dominik Brodowski <linux@dominikbrodowski.net>
Cc: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Reviewed-by: Eric Biggers <ebiggers@google.com>
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [davidhildenbrand/linux](https://github.com/davidhildenbrand/linux)@[ad8e44c094...](https://github.com/davidhildenbrand/linux/commit/ad8e44c094f6f4c9ffca6a335d25fafddf5c3935)
#### Wednesday 2022-02-23 17:33:24 by David Hildenbrand

mm: remember exclusively mapped anonymous pages with PG_anon_exclusive

Let's mark exclusively mapped anonymous pages with PG_anon_exclusive as
exclusive, and use that information to make GUP pins reliable and stay
consistent with the page mapped into the page table even if the
page table entry gets write-protected.

With that information at hand, we can extend our COW logic to always
reuse anonymous pages that are exclusive. For anonymous pages that
might be shared, the existing logic applies.

As already documented, PG_anon_exclusive is usually only expressive in
combination with a page table entry. Especially PTE vs. PMD-mapped
anonymous pages require more thought, some examples: due to mremap() we
can easily have a single compound page PTE-mapped into multiple page tables
exclusively in a single process -- multiple page table locks apply.
Further, due to MADV_WIPEONFORK we might not necessarily write-protect
all PTEs, and only some subpages might be pinned. Long story short: once
PTE-mapped, we have to track information about exclusivity per sub-page,
but until then, we can just track it for the compound page in the head
page and not having to update a whole bunch of subpages all of the time
for a simple PMD mapping of a THP.

For simplicity, this commit mostly talks about "anonymous pages", while
it's for THP actually "the part of an anonymous folio referenced via
a page table entry".

To not spill PG_anon_exclusive code all over the mm code-base, we let
the anon rmap code to handle all PG_anon_exclusive logic it can easily
handle.

If a writable, present page table entry points at an anonymous (sub)page,
that (sub)page must be PG_anon_exclusive. If GUP wants to take a reliably
pin (FOLL_PIN) on an anonymous page references via a present
page table entry, it must only pin if PG_anon_exclusive is set for the
mapped (sub)page.

This commit doesn't adjust GUP, so this is only implicitly handled for
FOLL_WRITE, follow-up commits will teach GUP to also respect it for
FOLL_PIN without !FOLL_WRITE, to make all GUP pins of anonymous pages
fully reliable.

Whenever an anonymous page is to be shared (fork(), KSM), or when
temporarily unmapping an anonymous page (swap, migration), the relevant
PG_anon_exclusive bit has to be cleared to mark the anonymous page
possibly shared. Clearing will fail if there are GUP pins on the page:
* For fork(), this means having to copy the page and not being able to
  share it. fork() protects against concurrent GUP using the PT lock and
  the src_mm->write_protect_seq.
* For KSM, this means sharing will fail. For swap this means, unmapping
  will fail, For migration this means, migration will fail early. All
  three cases protect against concurrent GUP using the PT lock and a
  proper clear/invalidate+flush of the relevant page table entry.

This fixes memory corruptions reported for FOLL_PIN | FOLL_WRITE, when a
pinned page gets mapped R/O and the successive write fault ends up
replacing the page instead of reusing it. It improves the situation for
O_DIRECT/vmsplice/... that still use FOLL_GET instead of FOLL_PIN,
if fork() is *not* involved, however swapout and fork() are still
problematic. Properly using FOLL_PIN instead of FOLL_GET for these
GUP users will fix the issue for them.

I. Details about basic handling

I.1. Fresh anonymous pages

page_add_new_anon_rmap() and hugepage_add_new_anon_rmap() will mark the
given page exclusive via __page_set_anon_rmap(exclusive=1). As that is
the mechanism fresh anonymous pages come into life (besides migration
code where we copy the page->mapping), all fresh anonymous pages will
start out as exclusive.

I.2. COW reuse handling of anonymous pages

When a COW handler stumbles over a (sub)page that's marked exclusive, it
simply reuses it. Otherwise, the handler tries harder under page lock to
detect if the (sub)page is exclusive and can be reused. If exclusive,
page_move_anon_rmap() will mark the given (sub)page exclusive.

Note that hugetlb code does not yet check for PageAnonExclusive(), as it
still uses the old COW logic that is prone to the COW security issue
because hugetlb code cannot really tolerate unnecessary/wrong COW as
huge pages are a scarce resource.

I.3. Migration handling

try_to_migrate() has to try marking an exclusive anonymous page shared
via page_try_share_anon_rmap(). If it fails because there are GUP pins
on the page, unmap fails. migrate_vma_collect_pmd() and
__split_huge_pmd_locked() are handled similarly.

Writable migration entries implicitly point at shared anonymous pages.
For readable migration entries that information is stored via a new
"readable-exclusive" migration entry, specific to anonymous pages.

When restoring a migration entry in remove_migration_pte(), information
about exlusivity is detected via the migration entry type, and
RMAP_EXCLUSIVE is set accordingly for
page_add_anon_rmap()/hugepage_add_anon_rmap() to restore that
information.

I.4. Swapout handling

try_to_unmap() has to try marking the mapped page possibly shared via
page_try_share_anon_rmap(). If it fails because there are GUP pins on the
page, unmap fails. For now, information about exclusivity is lost. In the
future, we might want to remember that information in the swap entry in
some cases, however, it requires more thought, care, and a way to store
that information in swap entries.

I.5. Swapin handling

do_swap_page() will never stumble over exclusive anonymous pages in the
swap cache, as try_to_migrate() prohibits that. do_swap_page() always has
to detect manually if an anonymous page is exclusive and has to set
RMAP_EXCLUSIVE for page_add_anon_rmap() accordingly.

I.6. THP handling

__split_huge_pmd_locked() has to move the information about exclusivity
from the PMD to the PTEs.

a) In case we have a readable-exclusive PMD migration entry, simply insert
readable-exclusive PTE migration entries.

b) In case we have a present PMD entry and we don't want to freeze
("convert to migration entries"), simply forward PG_anon_exclusive to
all sub-pages, no need to temporarily clear the bit.

c) In case we have a present PMD entry and want to freeze, handle it
similar to try_to_migrate(): try marking the page shared first. In case
we fail, we ignore the "freeze" instruction and simply split ordinarily.
try_to_migrate() will properly fail because the THP is still mapped via
PTEs.

When splitting a compound anonymous folio (THP), the information about
exclusivity is implicitly handled via the migration entries: no need to
replicate PG_anon_exclusive manually.

I.7. fork() handling

fork() handling is relatively easy, because PG_anon_exclusive is only
expressive for some page table entry types.

a) Present anonymous pages

page_try_dup_anon_rmap() will mark the given subpage shared -- which
will fail if the page is pinned. If it failed, we have to copy (or
PTE-map a PMD to handle it on the PTE level).

Note that device exclusive entries are just a pointer at a PageAnon()
page. fork() will first convert a device exclusive entry to a present
page table and handle it just like present anonymous pages.

b) Device private entry

Device private entries point at PageAnon() pages that cannot be mapped
directly and, therefore, cannot get pinned.

page_try_dup_anon_rmap() will mark the given subpage shared, which
cannot fail because they cannot get pinned.

c) HW poison entries

PG_anon_exclusive will remain untouched and is stale -- the page table
entry is just a placeholder after all.

d) Migration entries

Writable and readable-exclusive entries are converted to readable
entries: possibly shared.

I.8. mprotect() handling

mprotect() only has to properly handle the new readable-exclusive
migration entry:

When write-protecting a migration entry that points at an anonymous
page, remember the information about exclusivity via the
"readable-exclusive" migration entry type.

II. Migration and GUP-fast

Whenever replacing a present page table entry that maps an exclusive
anonymous page by a migration entry, we have to mark the page possibly
shared and synchronize against GUP-fast by a proper
clear/invalidate+flush to make the following scenario impossible:

1. try_to_migrate() places a migration entry after checking for GUP pins
   and marks the page possibly shared.
2. GUP-fast pins the page due to lack of synchronization
3. fork() converts the "writable/readable-exclusive" migration entry into a
   readable migration entry
4. Migration fails due to the GUP pin (failing to freeze the refcount)
5. Migration entries are restored. PG_anon_exclusive is lost

-> We have a pinned page that is not marked exclusive anymore.

Note that we move information about exclusivity from the page to the
migration entry as it otherwise highly overcomplicates fork() and
PTE-mapping a THP.

III. Swapout and GUP-fast

Whenever replacing a present page table entry that maps an exclusive
anonymous page by a swap entry, we have to mark the page possibly
shared and synchronize against GUP-fast by a proper
clear/invalidate+flush to make the following scenario impossible:

1. try_to_unmap() places a swap entry after checking for GUP pins and
   clears exclusivity information on the page.
2. GUP-fast pins the page due to lack of synchronization.

-> We have a pinned page that is not marked exclusive anymore.

If we'd ever store information about exclusivity in the swap entry,
similar to migration handling, the same considerations as in II would
apply. This is future work.

RFC notes: I'd love to split this up further, but it's not straight forward
           because it all interacts.

Signed-off-by: David Hildenbrand <david@redhat.com>

---
## [devs-immortal/Paradise-Lost](https://github.com/devs-immortal/Paradise-Lost)@[ee3a6870f7...](https://github.com/devs-immortal/Paradise-Lost/commit/ee3a6870f75c22e0d566718e5c2f1d1c0531aecc)
#### Wednesday 2022-02-23 17:37:42 by Jack Papel

Simplify LivingEntityMixin

My old gravitation code was pretty god-awful, so I made it better.
Also moved some things that don't belong in there out.
Changed some subtractions to multiplications. The results end up being the same.
Parachutes can slow gravitated players now.
I wish I could test my changes, but because we're on this snapshot I can't. Unless I want to rewrite the seedy behavior functionality in incubus.
Remind me to test this later.

---
## [BlackCatMS/V1-OOP](https://github.com/BlackCatMS/V1-OOP)@[615c8c7331...](https://github.com/BlackCatMS/V1-OOP/commit/615c8c733107113fdf84635c0c40d7b31b9e4dfd)
#### Wednesday 2022-02-23 18:52:14 by Josie

Practicum 4B progressed (feb 23)

thing doesn't work because getPrijsPerDag() apparently does nothing and my IDE tells me to change the type of prijsPerDag to Auto to have it properly call but when I change it to Auto from double/float then suddenly it tells me "oh but you cant do maths with an Auto type variable 😀" who the fuck made this language im literally going to lsoe my mind holy fuckhn

---
## [LineageOS/android_kernel_oneplus_sm8350](https://github.com/LineageOS/android_kernel_oneplus_sm8350)@[57a6948cb8...](https://github.com/LineageOS/android_kernel_oneplus_sm8350/commit/57a6948cb87a8775c4715a2a7e34c35cb50bb75d)
#### Wednesday 2022-02-23 19:34:28 by alk3pInjection

disp: msm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [TOLiving/code-busters](https://github.com/TOLiving/code-busters)@[ee43c7f4d5...](https://github.com/TOLiving/code-busters/commit/ee43c7f4d51161faa2366360d17252f673a5ec8d)
#### Wednesday 2022-02-23 20:29:41 by TOLiving

Updated version of v3. 1

I'm an idiot and I should honestly just stop coding but I won't because this is fun I'm just dumb holy crap

---
## [RomanMeasv/Attendence-Automation](https://github.com/RomanMeasv/Attendence-Automation)@[dcf049d8c4...](https://github.com/RomanMeasv/Attendence-Automation/commit/dcf049d8c4a039035561c86aae07a38b1899bf54)
#### Wednesday 2022-02-23 21:22:57 by Miloš Jozek

life destroying experience

shit felt to the fan I fixed it hopefully

---
## [exordium-vic3/exordium-vic3.github.io](https://github.com/exordium-vic3/exordium-vic3.github.io)@[be229ba8dd...](https://github.com/exordium-vic3/exordium-vic3.github.io/commit/be229ba8dddfd6e36efe2035e2610d2445347464)
#### Wednesday 2022-02-23 22:48:47 by exordium-vic3

I was damn near bawling, I felt so damn happy, if you want to know the truth. I don't know why. It was just that she looked so damn nice, the way she kept going around and around, in her blue coat and all. God, I wish you could've been there.

---

