## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-23](docs/good-messages/2022/2022-12-23.md)


1,933,026 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,933,026 were push events containing 2,741,433 commit messages that amount to 196,733,614 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 52 messages:


## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[51fe32a3ec...](https://github.com/Danielkaas94/DTAP/commit/51fe32a3ecd400c4014fc149b2c3f8e466c78611)
#### Friday 2022-12-23 00:10:15 by Danielkaas94

✝ Mercy Me ✝
Oh, mercy me, God bless catastrophe
Well there's no way in hell
We'll ever live to see through this so
Drive yourself insane tonight
It's not that far away and I just
Filled up your tank earlier today, yeah 🚗💨

---
## [DeveloperLoser/tgstation](https://github.com/DeveloperLoser/tgstation)@[84a85c827d...](https://github.com/DeveloperLoser/tgstation/commit/84a85c827d71b3326b482444a204711de38cf518)
#### Friday 2022-12-23 00:28:38 by lizardqueenlexi

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
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[f410b25f14...](https://github.com/Danielkaas94/DTAP/commit/f410b25f1452701dd54f902a1d339bfb21bf12ec)
#### Friday 2022-12-23 00:30:54 by Danielkaas94

Chop Suey! 🔪😇
Trust in my self-righteous suicide
I cry when angels deserve to die
In my self-righteous suicide
I cry when angels deserve to die

---
## [Rustybuckets6601/tgstation](https://github.com/Rustybuckets6601/tgstation)@[8cb4947084...](https://github.com/Rustybuckets6601/tgstation/commit/8cb4947084edffc9476c40ea6283b68e818f48bd)
#### Friday 2022-12-23 00:34:39 by Jacquerel

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
## [elastic/kibana](https://github.com/elastic/kibana)@[afb09ccf8a...](https://github.com/elastic/kibana/commit/afb09ccf8a61d610e8e3d8beb2c80f413f1b33c5)
#### Friday 2022-12-23 01:00:35 by Spencer

Transpile packages on demand, validate all TS projects (#146212)

## Dearest Reviewers 👋 

I've been working on this branch with @mistic and @tylersmalley and
we're really confident in these changes. Additionally, this changes code
in nearly every package in the repo so we don't plan to wait for reviews
to get in before merging this. If you'd like to have a concern
addressed, please feel free to leave a review, but assuming that nobody
raises a blocker in the next 24 hours we plan to merge this EOD pacific
tomorrow, 12/22.

We'll be paying close attention to any issues this causes after merging
and work on getting those fixed ASAP. 🚀

---

The operations team is not confident that we'll have the time to achieve
what we originally set out to accomplish by moving to Bazel with the
time and resources we have available. We have also bought ourselves some
headroom with improvements to babel-register, optimizer caching, and
typescript project structure.

In order to make sure we deliver packages as quickly as possible (many
teams really want them), with a usable and familiar developer
experience, this PR removes Bazel for building packages in favor of
using the same JIT transpilation we use for plugins.

Additionally, packages now use `kbn_references` (again, just copying the
dx from plugins to packages).

Because of the complex relationships between packages/plugins and in
order to prepare ourselves for automatic dependency detection tools we
plan to use in the future, this PR also introduces a "TS Project Linter"
which will validate that every tsconfig.json file meets a few
requirements:

1. the chain of base config files extended by each config includes
`tsconfig.base.json` and not `tsconfig.json`
1. the `include` config is used, and not `files`
2. the `exclude` config includes `target/**/*`
3. the `outDir` compiler option is specified as `target/types`
1. none of these compiler options are specified: `declaration`,
`declarationMap`, `emitDeclarationOnly`, `skipLibCheck`, `target`,
`paths`

4. all references to other packages/plugins use their pkg id, ie:
	
	```js
    // valid
    {
      "kbn_references": ["@kbn/core"]
    }
    // not valid
    {
      "kbn_references": [{ "path": "../../../src/core/tsconfig.json" }]
    }
    ```

5. only packages/plugins which are imported somewhere in the ts code are
listed in `kbn_references`

This linter is not only validating all of the tsconfig.json files, but
it also will fix these config files to deal with just about any
violation that can be produced. Just run `node scripts/ts_project_linter
--fix` locally to apply these fixes, or let CI take care of
automatically fixing things and pushing the changes to your PR.

> **Example:** [`64e93e5`
(#146212)](https://github.com/elastic/kibana/pull/146212/commits/64e93e580679dd55f4fdf19bd01402bc478a1a75)
When I merged main into my PR it included a change which removed the
`@kbn/core-injected-metadata-browser` package. After resolving the
conflicts I missed a few tsconfig files which included references to the
now removed package. The TS Project Linter identified that these
references were removed from the code and pushed a change to the PR to
remove them from the tsconfig.json files.

## No bazel? Does that mean no packages??
Nope! We're still doing packages but we're pretty sure now that we won't
be using Bazel to accomplish the 'distributed caching' and 'change-based
tasks' portions of the packages project.

This PR actually makes packages much easier to work with and will be
followed up with the bundling benefits described by the original
packages RFC. Then we'll work on documentation and advocacy for using
packages for any and all new code.

We're pretty confident that implementing distributed caching and
change-based tasks will be necessary in the future, but because of
recent improvements in the repo we think we can live without them for
**at least** a year.

## Wait, there are still BUILD.bazel files in the repo
Yes, there are still three webpack bundles which are built by Bazel: the
`@kbn/ui-shared-deps-npm` DLL, `@kbn/ui-shared-deps-src` externals, and
the `@kbn/monaco` workers. These three webpack bundles are still created
during bootstrap and remotely cached using bazel. The next phase of this
project is to figure out how to get the package bundling features
described in the RFC with the current optimizer, and we expect these
bundles to go away then. Until then any package that is used in those
three bundles still needs to have a BUILD.bazel file so that they can be
referenced by the remaining webpack builds.

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[08291a6dbb...](https://github.com/Lamella-0587/Skyrat-tg/commit/08291a6dbb3249d9acbca4f539eb82900d299f26)
#### Friday 2022-12-23 01:36:38 by SkyratBot

[MIRROR] Guards against uplink failsafe code being the same as unlock code [MDB IGNORE] (#18275)

* Guards against uplink failsafe code being the same as unlock code (#72113)

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

* Guards against uplink failsafe code being the same as unlock code

Co-authored-by: san7890 <the@san7890.com>

---
## [lovelyleoni/Skyrat-tg](https://github.com/lovelyleoni/Skyrat-tg)@[7b658b3c0d...](https://github.com/lovelyleoni/Skyrat-tg/commit/7b658b3c0d1b9c7b9672a0a1aa709d2789974190)
#### Friday 2022-12-23 02:00:47 by SkyratBot

[MIRROR] Drinking singulo ignores supermatter hallucinations and pulls nearby objects [MDB IGNORE] (#18157)

* Drinking singulo ignores supermatter hallucinations and pulls nearby objects (#71927)

## About The Pull Request
Drinking a singulo will now:

- Give immunity to supermatter hallucinations
- Pulls objects to you based on the total volume in your system (20u =
1x1, 45u = 2x2, 80u = 3x3)
- Makes a burp and supermatter rays/sound when objects are pulled

The new ingredient is:

- Vokda 5u
- Wine 5u
- Liquid Dark Matter 1u (replaces Radium)

## Why It's Good For The Game
More cool effects for drinks. Singularity is all about gravity and the
drink should have a theme around that.

![dreamseeker_2q21YXS698](https://user-images.githubusercontent.com/5195984/207297517-90d26395-dd30-4106-bdd4-b30b1ba3e20b.gif)

## Changelog
:cl:
add: Drinking singulo will now ignore supermatter hallucinations and
pull objects to you
balance: Change singulo drink recipe to require liquid dark matter
instead of radium.
/:cl:

* Drinking singulo ignores supermatter hallucinations and pulls nearby objects

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [Xiang-Gu/cockroach](https://github.com/Xiang-Gu/cockroach)@[506035b80e...](https://github.com/Xiang-Gu/cockroach/commit/506035b80e6ac83f1042aba6a42c0f526df5ba5b)
#### Friday 2022-12-23 02:55:53 by craig[bot]

Merge #93270 #94102 #94147

93270: sql, server: implement and write to new recent statements cache r=amyyq2 a=amyyq2

This change implements and tests a new RecentStatementsCache that is used to store the recent statements that were executed. The cache has two new cluster settings that tune the capacity and time that a statement lives in the cache.

This change also implements writing ActiveQueries to the cache. The RecentStatementsCache is added to the ExecutorConfig, and the Server writes to this cache whenever a non-internal statement finishes. This change also removes queryMeta.phase, and replaces it with ActiveQuery.Phase. The phases Canceled, Timed Out, Completed, and Failed are also as possible values to ActiveQuery.Phase.

Part Of #86955
Fixes #91556

Release note: None

94102: build: add tooling to mirror NPM dependencies to GCS r=sjbarag a=sjbarag

Note that this doesn't actually _apply_ these changes yet! That'll happen in a separate PR so we can have a better discussion about the mechanics involved here (and also to make backporting significantly simpler)

-----

CockroachDB's NPM dependencies are currently provided by the git
submodule in pkg/ui/yarn-vendored [1] and are installed during the
Bazel build with the '--offline' flag [2] to avoid relying on public
NPM registries. Bazel's rules_nodejs unfortunately doesn't work well
with dependencies that are vendored on-disk in the Bazel workspace via
yarn-offline-mirror, which led to some unfortunate hacks [3,4] being
introduced during the initial Bazel setup.

In the time since those hacks were added, two significant events
occured:

1. Bazel's rules_nodejs was deprecated in favor of rules_js [5], which
   manually implements the pnpm resolver algorithm and doesn't support
   yarn's yarn-offline-mirror configuration value.
2. Bazel 6 was released [6], which removed the 'managed_directories'
   attribute to the top-level workspace() rule that makes yarn_install
   work in CockroachDB at all.

The use of yarn-vendored therefore blocks both migration away from
rules_nodejs and an upgrade to Bazel 6.

Instead of relying on a git submodule and --offline installation,
it's possible to use the pattern already used by CockroachDB's go
dependencies: copy them from public locations to a storage bucket
managed by Cockroach Labs, then ensure the bucket is used for future
downloads. Doing so allows the yarn_vendored submodule and --offline
installation to be removed in favor of _online_ builds from a location
Cockroach Labs controls, thus unblocking both a migration away from
rules_nodejs and an upgrade to Bazel 6.

Add a //pkg/cmd/mirror/npm tree (and supporting ./dev tooling) that
downloads NPM dependencies from public registries, uploads them to a
public-readable bucket, and rewrites yarn.lock files to use that bucket,
along with a test to ensure those mirrored dependencies continue to be
used in the future.

[1] https://github.com/cockroachdb/yarn-vendored
[2] https://classic.yarnpkg.com/en/docs/cli/install#toc-yarn-install-offline
[3] ./build/bazelutil/seed_yarn_cache.bzl
[4] ./build/bazelutil/seed_yarn_cache.sh
[5] https://blog.aspect.dev/rulesjs-launch
[6] https://github.com/bazelbuild/bazel/releases/tag/6.0.0

Part of: https://github.com/cockroachdb/cockroach/issues/85038
Release note: None

94147: release: pass GCS credentials to publish-provisional-artifacts r=rickystewart a=rail

Previously, publish-provisional-artifacts requires `GOOGLE_APPLICATION_CREDENTIALS` environment variable when `--gcs-bucket` is passed. This was not the case for the case where we upload the latest binaries (`--bless`).

This PR adds required steps to set up and pass the credentials.

Epic: none
Release note: None

Co-authored-by: amyyq2 <amy.qian@cockroachlabs.com>
Co-authored-by: Sean Barag <barag@cockroachlabs.com>
Co-authored-by: Rail Aliiev <rail@iqchoice.com>

---
## [kakitng123/fyp-assignment](https://github.com/kakitng123/fyp-assignment)@[4fc63664c2...](https://github.com/kakitng123/fyp-assignment/commit/4fc63664c271b5f60882cc96117611e22b09d023)
#### Friday 2022-12-23 04:33:02 by Ka Kit

FYP - 22/12/2022 (After system_preview) - *KA KIT's PC*

- created a combined dataclass (applicationData.kt)
  - check again all data class (don't blindly put every single fucking thing as string, if you do that your wallet part also die, think)

ADMIN SIDE
----------
Class Management
- Remove classDate/classTime for ClassData
- Added Navbar for management/pending classes
  - Able to display enrollment classes (pending do later)

USER SIDE
---------
- Removed frontend.BookingData

PRODUCT
- Fixed productRV display, added itemClick into another fragment
  (you do display product details, I only want to do purchase)

BOOKING
- Added my "own" style of code and new <layout> layer in xml
- I have added comment on BookingCourtFragment.kt *entong pls take a look*

---
## [Gofawful5/Skyrat-tg](https://github.com/Gofawful5/Skyrat-tg)@[81ca11b95a...](https://github.com/Gofawful5/Skyrat-tg/commit/81ca11b95a59d5cf0eb0a066454b2903f4859503)
#### Friday 2022-12-23 04:51:58 by SkyratBot

[MIRROR] Basic Mob Carp: Retaliate Element [MDB IGNORE] (#18030)

* Basic Mob Carp: Retaliate Element (#71593)

## About The Pull Request

Adds an Element and AI behaviour intended to replicate the "retaliate"
behaviour which made up an entire widely-populated subtype of simple
mobs.
The behaviour is pretty simply "If you fuck with me I fuck with you".
Mobs with the component will "remember" being attacked and will try to
attack people who attacked them, until they lose sight of those people.
They don't have very long memories so breaking line of sight is enough
to remove you from their grudge list.
The implementation unfortunately requires registering to 600 different
"I have been attacked by X" signals but c'est la vie.

It will still be cleaner than
`/mob/living/simple_animal/hostile/retaliate/clown/clownhulk/honcmunculus`
and `mob/living/simple_animal/hostile/retaliate/bat/sgt_araneus`.

I attached it to the pig for testing and left it there because out of
all the farm animals we have right now, a pig would probably get pissed
off if you tried to kill it. Unfortunately it's got a sausage's chance
in hell of ever killing anyone.

## Why It's Good For The Game

It doesn't have much purpose yet but as we make more basic mobs this is
going to see a **lot** of use.

## Changelog

:cl:
add: Basic mobs have the capability of being upset that you kicked and
punched them.
add: Pigs destined for slaughter will now ineffectually attempt to
resist their fate, at least until they lose sight of you.
balance: Bar bots are better at noticing that you're trying to kill
them.
/:cl:

* Basic Mob Carp: Retaliate Element

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: tastyfish <crazychris32@gmail.com>

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[1d04cec7c5...](https://github.com/cockroachdb/cockroach/commit/1d04cec7c5f887d309e09b7b5a267d5269d86b5a)
#### Friday 2022-12-23 04:53:19 by craig[bot]

Merge #91394 #91627

91394: changefeedccl: roachtest refactor and initial-scan-only r=samiskin a=samiskin

Epic: https://cockroachlabs.atlassian.net/browse/CRDB-19057

Changefeed roachtests were setup focused on running a workload for a specific duration and then quitting, making it difficult to run an `initial_scan_only` test that terminated upon Job success.

We as a team have also noticed a greater need to test and observe changefeeds running in production against real sinks to catch issues we are unable to mock or observe from simple unit tests.  This is currently a notable hassle as one has to set up each individual sink and run them, ensure the changefeed is pointing to the right URI, and then be able to monitor the metrics of this long running process.  

This change refactors the cdcBasicTest into distinct pieces that are then put together in a test.  This allows for easier experimentation with live tests, allowing us to spin up a cluster and a workload, run one or more changefeeds on it, set up a poller to print out job details,have an accessible grafana URL to view metrics, and wait for some completion condition.

Changing the specialized `runCDCKafkaAuth`, `runCDCBank`, and `runCDCSchemaRegistry` functions were left out of scope for this first big change.

The main APIs involved in basic roachtests are now:
- `newCDCTester`: This creates a tester struct to run the rest of the APIs and initializes the database
- `tester.runTPCCWorkload(tpccArgs)`: Starts a TPCC workload from the last node in the cluster
- `tester.runLedgerWorkload(ledgerArgs)`: Starts a Ledger workload from the last node in the cluster
- `tester.runFeedLatencyVerifier(changefeedJob, latencyTargets)`: starts a routine that monitors the changefeed latency until the tester is `Close`'d
- `tester.waitForWorkload`: waits for a workload started by `setupAndRunWorkload` to complete its duration
- `tester.startCRDBChaos`: This starts a Chaos routine that periodically shuts nodes down and brings them back up
- `tester.newChangefeed(feedArgs)`: starts a new changefeed on the cluster and returns `changefeedJob` object
- `changefeedJob.waitForCompletion`: waits for a changefeed to complete (either success or failure)
- `tester.startGrafana`: Sets up a grafana instance on the last node of the cluster and prints out a link to a grafana, this automatically runs unless `--skip-init` is provided.  If `--debug` is not used, `StopGrafana` will be called on test teardown to publish prometheus metrics to the artifacts directory.

An API that is going to be more useful for experimentation are:
- `changefeedJob.runFeedPoller(ctx, stopper, onInfo)`: runs a given callback every second with the changefeed info

Roachtests can be ran locally with the `--local` flag or on an existing cluster without destroying it afterwards with `--cluster="my-cluster" --debug`

Ex: After adding a new test (lets say `"cdc/my-test"`) to the `registerCDC` function you can keep running 
```bash
./dev build cockroach --cross # if changes made to crdb
./dev build roachtest         # if changes made to the test

./bin/roachtest run cdc/my-test --cluster="my-cluster" --debug
```
as you try out different changes or options.  If you want to try a set of steps against different versions of the app you could download those binaries and use the `--cockroach="path-to-binary"` flag to test against those instead.

If you want to set up a large TPCC database on a cluster and reuse it for tests this can be done with roachtests's `--wipe` and `--skip-init` flags.

Release note: None

91627: upgrade: introduce "permanent" upgrades r=andreimatei a=andreimatei

This patch introduces "permanent" upgrades - a type of upgrade that is
tied to a particular cluster version (just like the existing upgrades)
but that runs regardless of the version at which the cluster was
bootstrapped (in contrast with the existing upgrades that are not run
when they're associated with a cluster version <= the bootstrap
version). These upgrades are called "permanent" because they cannot be
deleted from the codebase at a later point, in contrast with the others
that are deleted once the version they're tied drops below
BinaryMinSupportedVersion).

Existing upgrades are explicitly or implicitly baked into the bootstrap
image of the binary that introduced them. For example, an upgrade that
creates a system table is only run when upgrading an existing,
older-version, cluster to the new version; it does not run for a cluster
bootstrapped by the binary that introduced the upgrade because the
respective system tables are also included in the bootstrap metadata.
For some upcoming upgrades, though, including them in the bootstrap
image is difficult. For example, creating a job record at bootstrap
time is proving to be difficult (the system.jobs table has indexes, so
you want to insert into it through SQL because figuring out the kv's for
a row is tedious, etc). This is where these new permanent upgrades come
in.

These permanent upgrades replace the `startupmigrations` that don't have
the `includedInBootstrap` field set. All such startupmigrations have
been copied over as upgrades. None of the current `startupmigrations`
have `includedInBootstrap` set (except one but that's dummy one since
the actual migration code has been deleted), so the startupmigrations
package is now deleted. That's a good thing - we had one too many
migrations frameworks.

These permanent upgrades, though, do not have exactly the same semantics
as the startupmigrations they replace. To the extent that there is a
difference, the new semantics are considered more desirable:
- startupmigrations run when a node that has the code for a particular
  migration startups up for the first time. In other words, the
  startupmigrations were not associated with a cluster version; they were
  associated with a binary version. Migrations can run while old-version
  nodes are still around.  This means that one cannot add a
  migration that is a problem for old nodes - e.g. a migration creating a
  job of a type that the old version wouldn't recognize.
- upgrades are tied to a cluster version - they only run when the
  cluster's active version moves past the upgrade's version. This stays
  the case for the new permanent migrations too, so a v2 node will not
  immediately run the permant migrations introduced since v1 when it joins
  a v1 cluster. Instead, the migrations will run when the cluster version
  is bumped. As such, the migrations can be backwards incompatible.

startupmigrations do arguably have a property that can be desirable:
when there are no backwards compatibility issues, the v2 node can rely
on the effects of the startupmigrations it knows about regardless of the
cluster version. In contrast, with upgrades, not only is a node unable
to simply assume that a particular upgrade has run during startup, but,
more than that, a node is not even able to look at a version gate during
the startup sequence in order to determine whether a particular upgrade
has run or not (because, in clusters that are bootstrapped at v2, the
active cluster version starts as v2 even before the upgrades run). This
is a fact of life for existing upgrades, and now becomes a fact of life
for permanent upgrades too. However, by the time user SQL traffic is
admitted on a node, the node can rely on version gates to correspond to
migrations that have run.

After thinking about it, this possible advantage of startupmigrations
doesn't seem too useful and so it's not reason enough to keep the
startupmigrations machinery around.

Since the relevant startupmigrations have been moved over to upgrades,
and the two libraries use different methods for not running the same
migration twice, a 23.1 node that comes up in a 22.2 cluster will re-run
the several permanent upgrades in question, even though they had already
run as startupmigrations. This is OK since both startupmigrations and
upgrades are idempotent. None of the current permanent upgrades are too
expensive.

Closes https://github.com/cockroachdb/cockroach/issues/73813

Release note: None
Epic: None

Co-authored-by: Shiranka Miskin <shiranka@cockroachlabs.com>
Co-authored-by: Andrei Matei <andrei@cockroachlabs.com>

---
## [spartanbobby/cmss13](https://github.com/spartanbobby/cmss13)@[15af7f1ee5...](https://github.com/spartanbobby/cmss13/commit/15af7f1ee5e7dbd568ea01b53c993e127b4bdb12)
#### Friday 2022-12-23 05:11:10 by ThePiachu

Cargo ammo and ammo box mapping (re-up) (#1759)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Previous version of this PR ( #1650 ) claimed to have changed 384 files,
which would be impossible to review. So re-uploading this PR with
hopefully a sane amount of files changed...

---

When I was playing cargo I spent a good half an hour in a round just
mindlessly packing ammo magazines into boxes in squad prep. It didn't
put a dent in the squad prep supply, and I barely got a handful of
boxes. So I thought to myself that this is pretty much a waste of time
for cargo and decided to code a better solution:

https://www.youtube.com/watch?v=cnXcEYAV8P4

So now select vendors (opt-in via `VEND_LOAD_AMMO_BOXES`) support ammo
consolidation. They count the number of ammo magazines you have and from
that they derive the number of magazine boxes you can vend. If you vend
a magazine, it updates the number of boxes available, and if you vend a
box, it updates the number of magazines available (as well as all
derived boxes - see the 3 pack of grenades and 25 pack box).

The `item_to_box_mapping` tracks ammo boxes (minus loose ammo), grenade
boxes, grenade packets and mine boxes.

Most notable affected vendors - Requisition ammo vendor, Requisition
vendor that features grenades, Squad vendors that have ammo in them.

So now Requisition will be able to easily raid Squad Vendors to stock up
their ammo drops and save countless hours of mind-numbing cargo work.

This code ALSO correctly works when you're re-stocking a vendor with
either individual magazines or magazine boxes. Correct amounts are
updated everywhere. So you *could* take a magazine box, put it in a
vendor and thus let people vend 16 magazines out of it seemlessly.
Really useful just incase you need to restock Requisitions with
individual ammo or something...

Other notes:
- Boxes of magazines are put directly under the corresponding ammo so
you can vend them in larger amounts easier. Useful for 3-packs of
grenades
- We should add a Shotgun Shell Box Box so we can also handle those
easily...
- Nailgun ammo box had to be converted from being /smg/ since that
created an invalid ammo box that nobody used.
- Nulled out a magazine type for an intermediary box that later gets
used for MREs and all that

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Gameplay around loading magazines into ammo boxes is not interesting, so
cutting it down to minimum is for the best.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:
add: Added an automated ammo box management system to various vendors
stocking bulk ammo and grenades. It will automatically combine ammo
magazine into boxes, and divide boxes into individual magazines (or
grenades, MRE packets, etc.). The boxes will appear at the bottom of the
vendor (yes, this also includes the regular grenade boxes that used to
be higher).
qol: Cargo will no longer need to pack individual vended ammo magazines
into boxes thanks to the ammo box management system. Your chains have
been broken!
qol: Requisitions vendor now stocks 3-packs of grenades as well as
individual HEDP grenades.
qol: Requisitions ammo vendor now can vend a lot more individual
magazines (actual number of magazines remains unchanged, just the ammo
boxes have been consolidated into magazines).
qol: Requisition vendors now vend to floor when they are not vending to
the front desks. This will make filling crates of ammo boxes or rappels
easier.
code: Minor changes to code around some ammo boxes to remove one phantom
box and prevent intermediate box types from being indexed when they
shouldn't be.
code: Refactored the code that checks whether items are in mint enough
condition to re-stock.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [general-programming/megarepo](https://github.com/general-programming/megarepo)@[38004a6fb3...](https://github.com/general-programming/megarepo/commit/38004a6fb3b21eb1b3d3e6047285d69e61142e11)
#### Friday 2022-12-23 05:24:34 by nepeat

feat(archiveteam): FUCK, THIS IS SHIT CODE. HOLY FUCK

---
## [StevieBozz/alx-low_level_programming](https://github.com/StevieBozz/alx-low_level_programming)@[884ba13a03...](https://github.com/StevieBozz/alx-low_level_programming/commit/884ba13a03eff3b23f38b3fb135c89d4e0703d19)
#### Friday 2022-12-23 05:47:38 by SteveieBozz

strcat,  strncat, strncpy, strcmp, I am a kind of paranoid in reverse. I suspect people of plotting to make me happy, Always look up, Expect the best. Prepare for the worst. Capitalize on what comes, Mozart composed his music not for the elite, but for everybody,  rot13, Numbers have life; they're not just symbols on paper, A dream doesn't become reality through magic; it takes sweat, determination and hard work,

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[df737af4a0...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/df737af4a02b18388b293005c340a7a46423236e)
#### Friday 2022-12-23 07:15:35 by SkyratBot

[MIRROR] *hand, or That /One/ Emote You Always Felt Was Missing [MDB IGNORE] (#18200)

* *hand, or That /One/ Emote You Always Felt Was Missing (#71600)

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

* *hand, or That /One/ Emote You Always Felt Was Missing

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[4cce4bcf10...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/4cce4bcf10aabec33f0652b07034bfe71bfca66a)
#### Friday 2022-12-23 07:15:35 by SkyratBot

[MIRROR] Minor plane cube cleanup [MDB IGNORE] (#18223)

* Minor plane cube cleanup (#72038)

## About The Pull Request

[Fixes area lighting not working on turf change in multiz
cases](https://github.com/tgstation/tgstation/commit/7b92deffbca92a834cb0a361fd685de51a12ea53)

If you modify a area lit turf when using multiz, it'd end up using the
wrong plane for its light, because of stupid shit on my part.
Stupid shit resolved

[Fixes some uses of plane masters that only specified one rather then
all](https://github.com/tgstation/tgstation/commit/a59ec96d29710b967bf8b3ffe8210b230cb194b3)

We almost never only want to show SOME hidden planes.
Should really make a helper for this someday

* Minor plane cube cleanup

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[0dd70b12e5...](https://github.com/ThePiachu/cmss13/commit/0dd70b12e5142b3b0f14bf237765c1e643fe8a3f)
#### Friday 2022-12-23 07:25:15 by Stan_Albatross

removes unused nanoui templates (#2012)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

none of these templates are used anywhere

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck nanoui

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
del: Removed ten unused nanoui templates. Don't worry, they'll all be
going away soon.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[44008f485d...](https://github.com/ZephyrTFA/tgstation/commit/44008f485d6d72537935cfa8a3a5b6140eece744)
#### Friday 2022-12-23 08:20:05 by Jacquerel

Fishing-themed Escape Shuttle (#71805)

## About The Pull Request

I can't do much coding until you review my other PRs so I'm making a
mapping PR instead.
I actually made this a while ago while I was trying out strongDMM. It
turns out: it's a good tool and easy to use.

![2022 12 09-10 51
26](https://user-images.githubusercontent.com/7483112/206686234-ae952ba3-2cb4-4093-80a0-d086fe95a3fc.png)

This mid-tier shuttle isn't enormous and is shaped like a fish. It
dedicates much of its internal space to an artificial fishing
environment, plus fishing equipment storage. Plus look at that lovely
wood panelling!
There's not a lot of seating or a large medbay, but there's five fishing
rods for people to wrestle each other over plus some aquariums to store
your catches in.

It contains a variety of fishing biomes (ocean, moisture trap, hole,
portal) but I couldn't fit "lava" in there even though I wanted to
because it's hardcoded to only have fish in it on the mining z-level.
If you're very lucky and nobody shoves you, the time between the shuttle
docking at the station and arriving at Centcomm might be enough time for
you to catch maybe four entire fish. Wow!

## Why It's Good For The Game

There are plenty of novelty shuttle options but I think this one is good
for a personal touch of "the Captain would rather be fishing than
hearing you complain about the nuclear operatives".

## Changelog

:cl:
add: Tell your crew how much you care by ordering a shuttle where half
of the seats have been removed so that you can get some angling done
before you clock out.
/:cl:

---
## [ss220-space/tgstation](https://github.com/ss220-space/tgstation)@[6dd4839ef3...](https://github.com/ss220-space/tgstation/commit/6dd4839ef321aa0a997549d1ae07fe7ccbba59ed)
#### Friday 2022-12-23 08:33:56 by carshalash

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
## [systemic-chaos/currently-fronting](https://github.com/systemic-chaos/currently-fronting)@[c38543b586...](https://github.com/systemic-chaos/currently-fronting/commit/c38543b58676931276f3ca2ab876e9fcb84e07a5)
#### Friday 2022-12-23 08:34:19 by Arcana

Switch to a subset of ts-standard from Prettier

We've long valued Prettier's configurability and convenience,
but we were somehow unaware
of the maintainer's aggressive and
demeaning stance toward
devs who actually want their code
to look beautiful to *them*.
They now refuse to ever implement
new configuration options
and have expressed remorese over
adding them in the first place.

Given our sensory differences,
we find that semicolons
make code harder to read.
So we have always disabled semicolons
when using Prettier, in contradiction
of the default for TypeScript
(according to them).

ts-standard (and StandardJS), by contrast, have defaults that are *much*
more in line with our idea of
aesthetically pleasing code...
And Standard is deliberately implemented
as an ESLint shared config,
which means rules can be overridden
with ease by design.

And that's just it, at the end of the day:
The features of Prettier were ultimately
purely cosmetic. And if the code is not aesthetically
pleasing ---- hell, if it's bloody unreadable ---- to its own devs,
what good is a style guide?

TL;DR Style guides are great.
Attempting to force devs to follow them in contradiction of their
own sense of aesthetics is awful.

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[0ca2c0b527...](https://github.com/Stalkeros2/Skyrat-tg/commit/0ca2c0b527a564de32818057b7fc09eb07875f51)
#### Friday 2022-12-23 09:14:32 by SkyratBot

[MIRROR] Gives bread and cake slice_types and adds screentip verbs to proccessed foods [MDB IGNORE] (#17721)

* Gives bread and cake slice_types and adds screentip verbs to proccessed foods (#71449)

## About The Pull Request

A side effect of my pizza PR #71202 I added contextual screentips as
part of processable.dm. In doing this, I noticed that with a few
exceptions, almost every single bread and cake type copies the proc
exactly the same for every single child of cake or bread, so I put the
proc on the parent of bread and cake and gave them slice_types, making
them more similar to pizza.dm

For everything else I've changed the default that I put in
processable.dm into "slice" or "cut" for things that use the knife and
"flatten" for things that use the rolling pin.

Finally, you can slice bread with saws now, because I think its silly
that only pizza gets this luxury.

## Why It's Good For The Game

Because it wasnt the focus of #71202 I didn't mess with screentips
outside of the pizza file a lot, but now that it's merged I figure I
should go and do that.
As Bread and Cake's processables are almost fully standardized it seems
silly for them to call on the proc 12 times in the same document so I
did this, which also allows for more versatility in editing how they
work as well allow people to, if they want to, add more tool behaviours
in the future without adding in 12 lines of code. Also means that people
who want to add new cake or bread have one less thing to do.

## Changelog

:cl:
add: you can saw bread with a saw into bread slices
qol: added screentip verbs to a bunch of food files
code: bread and cake now have slice types and all only have one call on
the processable.dm proc
/:cl:

* Gives bread and cake slice_types and adds screentip verbs to proccessed foods

* sco'ish

* fuck me ig

Co-authored-by: Sol N <116288367+flowercuco@users.noreply.github.com>
Co-authored-by: John Doe <gamingskeleton3@gmail.com>

---
## [Sniblet/Aurora.3](https://github.com/Sniblet/Aurora.3)@[83b6701ead...](https://github.com/Sniblet/Aurora.3/commit/83b6701ead343cb9c32185daf6dc5dc46ea0343f)
#### Friday 2022-12-23 10:10:51 by Sniblet

sedantian firestorm can use kphoron

a way to purify k'ois phoron! look, the firestorm doesn't cause mycosis! look everybody! oh my fucking god the scarcity crisis is over

---
## [seanpdoyle/turbo](https://github.com/seanpdoyle/turbo)@[5509548287...](https://github.com/seanpdoyle/turbo/commit/550954828771941d19329abb03bd16a2eb78908e)
#### Friday 2022-12-23 12:34:52 by Sean Doyle

Extract `FrameVisit` to drive `FrameController`

The problem
---

Programmatically driving a `<turbo-frame>` element when its `[src]`
attribute changes is a suitable end-user experience in consumer
applications. It's a fitting black-box interface for the outside world:
change the value of the attribute and let Turbo handle the rest.

However, internally, it's a lossy abstraction.

For example, when the `FrameRedirector` class listens for page-wide
`click` and `submit` events, it determines if their targets are meant to
drive a `<turbo-frame>` element by:

1. finding an element that matches a clicked `<a>` element's `[data-turbo-frame]` attribute
2. finding an element that matches a submitted `<form>` element's `[data-turbo-frame]` attribute
3. finding an element that matches a submitted `<form>` element's
   _submitter's_ `[data-turbo-frame]` attribute
4. finding the closest `<turbo-frame>` ancestor to the `<a>` or `<form>`

Once it finds the matching frame element, it disposes of all that
additional context and navigates the `<turbo-frame>` by updating its
`[src]` attribute. This makes it impossible to control various aspects
of the frame navigation (like its "rendering" explored in
[hotwired/turbo#146][]) outside of its destination URL.

Similarly, since a `<form>` and submitter pairing have an impact on
which `<turbo-frame>` is navigated, the `FrameController` implementation
passes around a `HTMLFormElement` and `HTMLSubmitter?` data clump and
constantly re-fetches a matching `<turbo-frame>` instance.

Outside of frames, page-wide navigation is driven by a `Visit` instance
that manages the HTTP life cycle and delegates along the way to a
`VisitDelegate`. It also pairs calls to visit with a `VisitOption`
object to capture additional context.

The proposal
---

This commit introduces the `FrameVisit` class. It serves as an
encapsulation of the `FetchRequest` and `FormSubmission` lifecycle
events involved in navigating a frame.

It's implementation draws inspiration from the `Visit`, `VisitDelegate`,
and `VisitOptions` pairing. Since the `FrameVisit` knows how to unify
both `FetchRequest` and `FormSubmission` hooks, the resulting callbacks
fired from within the `FrameController` are flat and consistent.

Extra benefits
---

The biggest benefit is the introduction of a DRY abstraction to
manage the behind the scenes HTTP calls necessary to drive a
`<turbo-frame>`.

With the introduction of the `FrameVisit` concept, we can also declare a
`visit()` and `submit()` method for `FrameElementDelegate`
implementations in the place of other implementation-specific methods
like `loadResponse()` and `formSubmissionIntercepted()`.

In addition, these changes have the potential to close
[hotwired/turbo#326][], since we can consistently invoke
`loadResponse()` across `<a>`-click-initiated and
`<form>`-submission-initiated visits. To ensure that's the case, this
commit adds test coverage for navigating a `<turbo-frame>` by making a
`GET` request to an endpoint that responds with a `500` status.

[hotwired/turbo#146]: https://github.com/hotwired/turbo/pull/146
[hotwired/turbo#326]: https://github.com/hotwired/turbo/issues/326

---
## [Holoo-1/fulpstation](https://github.com/Holoo-1/fulpstation)@[ca0fedc60f...](https://github.com/Holoo-1/fulpstation/commit/ca0fedc60f17f19520b8fa064c396129ad68b633)
#### Friday 2022-12-23 12:45:58 by John Willard

Sol is now a Subsystem, Coffins lock themselves, Bloodsuckers don't constantly die, probably (#862)

* Turns Sol into a Subsystem & Many more

Turns Sol into a subsystem and hooks Bloodsuckers onto it via signals instead of doing a ton of for() loops anywhere. This made Sol incredibly fucking fast, so I halved the speed so it only ticks every 2 seconds.

I also improved the sunlight hud to update with regular bloodsucker updates to avoid some useless proc overhead and fixed Coffins not locking by themselves.

* Torpor now ends, moves exiting torpor to its proper place

* round it

* fix comment

* fix CI

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[1636ba5ed2...](https://github.com/odoo-dev/odoo/commit/1636ba5ed2f8a284bef0930313a85cc3dc7cf072)
#### Friday 2022-12-23 13:14:40 by qsm-odoo

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
## [feinorgh/Cataclysm-DDA](https://github.com/feinorgh/Cataclysm-DDA)@[8e39d6f97c...](https://github.com/feinorgh/Cataclysm-DDA/commit/8e39d6f97c358c72a3dacc7c2f3ce955ecb30e81)
#### Friday 2022-12-23 13:15:11 by casswedson

fix: edge case ci error exit (#62660)

so a step of the reviewer workflow always runs, good it is the actual
magical step doing the hard work, but if the workflow gets canceled, the
step exits with an error code, I actually knew this but me from like a
day ago was like:
"nah man this won't bother me in the future."

guess what; after a couple hours I was felling the pain my perfectionist
subconscious was putting me through, plus odd error code exits aren't
very professional or clean or pleasing I'd say, also someone may think
it's weird, look into it, waste time looking at my code

title: do not draw much attention

Co-authored-by: casswedson <casswedson@users.noreply.github.com>

---
## [aaronhumphres/Project-1](https://github.com/aaronhumphres/Project-1)@[74bfd37355...](https://github.com/aaronhumphres/Project-1/commit/74bfd373556a9b149c2b001ce0abca394c4d8dcb)
#### Friday 2022-12-23 13:53:31 by aaronhumphres

Escape the Wizard's Keep

Player has escaped from a lab cell in a Prisoner's tower.
Simple Canvas Game.
Object of the game is to move player to the other end of the screen without touch any traps or guards called "Grues." Touching a trap or a guard will send player back to the starting point. Player will have 3 lives.

Player will be released from cell at the beginning of the game and be prompted to free two other prisoners. These will be his "lives." Upon the loss of a life, a message will prompt that one of the player's companions has died. There will be a funny message text when this occurs.

There will be a collision event to exit the first room which will prompt a trivia question. A user input box will populate. Any response will be the correct answer for the questions, except for one random question that will be asked the second time this occurs (player has lost a life and has to start over). Q1, what is your name. Q2 what is your favorite color? Q3 What is your favorite holiday?  The random question ( on try #2) will be similar to the bridge keeper in Holy Grail.. what is he average speed of a swallow...etc " Incorrectly answering this will send player back to start. Will need to figure out how to code looking for a specific response to last (swallow question) question, though it will only be asked once. 

room 2 has a simple moving wall that player must avoid.

room 3 has a Grue who will move randomly within a set of coordinates. He will move slow.

room 3 has 2 moving walls

room 4 has 2 random moving Grues

You win he game when player touches far end of screen.

Will code walls to create rooms.

---
## [Mantou1233/nico](https://github.com/Mantou1233/nico)@[221a4c386a...](https://github.com/Mantou1233/nico/commit/221a4c386a6669a695ac9d917c5c61e0ce8dd8ee)
#### Friday 2022-12-23 15:03:48 by Mantou1233

chore: fuck you i impl all decorators
OWOWOWOOWOWO
@Cogs(str[]) load fuck
@Inject works
rn it work like fuck, just had to fix mixin
and deco codes and
impl v1 loader

---
## [ralph-irving/squeezelite](https://github.com/ralph-irving/squeezelite)@[226efa300c...](https://github.com/ralph-irving/squeezelite/commit/226efa300c4cf037e8486bad635e9deb3104636f)
#### Friday 2022-12-23 15:17:03 by Ralph Irving

So, I've made more tests with a simple HTTP server and a client just download data through a simple GET. It's 100% easy to reproduce the issue if the client throttle at say 160kbits/s and a file of ~3.5MB is transferred. The HTTP server confirms (as does tcpdump) that all is transferred in a record time and using TCPview (or netstat) you can see that the connection is in FIN_WAIT_2.

It is all received because the TCPWindow quickly gets massive (a few MB) and so are the kernel's buffers. Obviously, Windows has a half-open socket timer that is started with the first FIN send and that causes the issue 100% time.

By limiting SO_RCVBUF, the TCPWindow cannot open that large as soon as the application does not get data fast enough. Of course, when we'll fill the stream and output buffers, TCPWindow will open because we absorb data super fast, but it will shrink back as soon as we stop pumping data in because we are full.

Now, 4KB is awfully low and I tried to increase it and it was still fine at 65kB, I could see TCPWindow opening and closing. The funny thing is that when you do a getsockopt, system will return 65kB. If you set what you got, the problem disappear as expected. BUT, if don't set anything, then Windows uses some much larger value (although it told you it does not) and then the issues happens.

-philippe44.

Thanks philippe44 for tracking down the cause of this issue.
Increase squeezelite revision to 1419.

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[a14495fb9d...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/a14495fb9dcf6a18cac56d63138b0ca56476158a)
#### Friday 2022-12-23 15:22:04 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tiktodz <ewprjkt@proton.me>

---
## [SergeJohn/react-meme-generator](https://github.com/SergeJohn/react-meme-generator)@[b3e28b1b18...](https://github.com/SergeJohn/react-meme-generator/commit/b3e28b1b1835c9f2582d8634ab2c2f461b73bf61)
#### Friday 2022-12-23 15:30:58 by Serge John Mahinay

'image url'

Here's a description of your meme generator app using React:

"Welcome to our meme generator app! With this app, you can easily create your own memes by choosing a template image and adding your own text. We've included a wide selection of popular meme templates to choose from, or you can upload your own image to create a unique meme.

Our app is built using React, a popular JavaScript library for building user interfaces. This allows us to create a fast and responsive app that's easy to use.

To get started, simply select a template image and add your own text to create your own personalized meme. You can save your meme to your device or share it with your friends on social media.

Thank you for using our meme generator app! We hope you have fun creating memes and sharing them with your friends.

---
## [penglezos/android_frameworks_base](https://github.com/penglezos/android_frameworks_base)@[33d8c4fdee...](https://github.com/penglezos/android_frameworks_base/commit/33d8c4fdee56b9c60ae45419a600670a71fa00ca)
#### Friday 2022-12-23 16:24:21 by Kuba Wojciechowski

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
## [Workbench-Team/space-station-14](https://github.com/Workbench-Team/space-station-14)@[c0a13f6269...](https://github.com/Workbench-Team/space-station-14/commit/c0a13f626980fc61e8664b2a6d2a34ccca24c98d)
#### Friday 2022-12-23 17:23:58 by Mr0maks

Голопроекторы почти как на tgstation (#36)

* First work on holo

* End of my pain in ass

* Oh shit im sorry

---
## [AchyMake/Essentialss](https://github.com/AchyMake/Essentialss)@[6359e68fb3...](https://github.com/AchyMake/Essentialss/commit/6359e68fb3bf7b1710dc21dd5baf4fabac6b5fa2)
#### Friday 2022-12-23 17:40:07 by Achy

Create how do i just make a simple maven shit holy fuck, i wanna die

---
## [Crowbar764/CM13](https://github.com/Crowbar764/CM13)@[229a2e6ed2...](https://github.com/Crowbar764/CM13/commit/229a2e6ed24998b2b97421ae421cfe25b77ae1b1)
#### Friday 2022-12-23 18:08:02 by Stan_Albatross

Teleporter tgui and minor refactor (#1997)

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

converts teleporters to tgui and removes some shitcode

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck nanoui


![image](https://user-images.githubusercontent.com/66756236/208460209-8f260838-1da1-49af-8d6c-44efcc974efb.png)


![image](https://user-images.githubusercontent.com/66756236/208458960-7bd162fd-e2fe-4c23-a3f6-257cb73516f5.png)


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
ui: swapped teleporters to use tgui.
fix: teleporter consoles now have actual sprites!
code: "improved" some teleporter code.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[b07b4bdcad...](https://github.com/treckstar/yolo-octo-hipster/commit/b07b4bdcad5fb4011ed1d92b8e6334f6e730044d)
#### Friday 2022-12-23 18:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [merumerutho/libxm7](https://github.com/merumerutho/libxm7)@[e6c1dec0c7...](https://github.com/merumerutho/libxm7/commit/e6c1dec0c7441f17c157bd5b07abe49e6dee8d7b)
#### Friday 2022-12-23 18:33:26 by merumerutho

God. Doing some real fuckery here. I'm going to hell for this.
Bugfixing a lot of stuff, now it starts to work for real. Can load two tunes without issues. I have to unload them though... Garbage collection time.

---
## [xoka-pro/goit-python-core-project](https://github.com/xoka-pro/goit-python-core-project)@[c98928749d...](https://github.com/xoka-pro/goit-python-core-project/commit/c98928749da5b08de5099ff4eec54c6fe636d3b3)
#### Friday 2022-12-23 19:43:29 by Nikita Sherstianykh

Weather func

Working func for getting weather.
- command 'weather *city*'
-if city is incorrect - catch the exceptions
- if city in russia - program says like "russian warship - go fuck yourself"

---
## [SimenB/apollo-server](https://github.com/SimenB/apollo-server)@[32cca948be...](https://github.com/SimenB/apollo-server/commit/32cca948be82764e9d076be171b5c1657d412899)
#### Friday 2022-12-23 19:48:54 by Trevor Scheer

Update CS:CI config (#7254)

CS:CI has reported that node 18 is now supported, meaning we should be
able to simplify some config and remove a workaround.

Also add missing packages to the ci.json.

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

---
## [NoKohi/cmss13](https://github.com/NoKohi/cmss13)@[1a226283e5...](https://github.com/NoKohi/cmss13/commit/1a226283e5c108dffcb74746af5d36ba29d51058)
#### Friday 2022-12-23 19:53:00 by Diegoflores31

vamp lurker strain (#955)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds a new strain for lurker (vampire is the name for now but i can be
changed i just lack the creativity) has less health than the average
lurker but its faster and slashes faster but deals less damage .

**### BASE STATS**
health : 390
armor : 20 
slash damage : 35
speed : 0.1 faster than base lurker // for reference cloaked speed is
0.2
slash speed : 2


Vamp lurker cannot cloak but has a larger kit of abilities focused on
dealing damage and healing making it a high risk high reward backliner
with skill based abilities rather than just stun.
### **Abilities :**

**Rush:** 
Shorter version of pounce (4 tiles) instead of stunning it will daze and
slightly screenshake the target .
damage : 30
cooldown : 6 seconds and 3 if you land it.

**Flurry:**
AOE attack that deals damage to the targets in front of you in a 1x3
area . if landed it will heal you by the same amount and apply a small
slow for the user ( very short second slow)
damage: 30
heal : 30
cooldown : 3 seconds if missed 

**Tail Jab:**
Targeted attack will deal a small amount of damage to the target and
knock him away from you . if you use it on a target in critical state it
will execute it healing you a LOT.
damage : 30
Execution damage : 80 with penetration
cooldown : 7 seconds 
heal : 150
critical state : this occurs when the target either paincrits or falls
INCONCIOUS

## Why It's Good For The Game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->
Lurker lacks strains and i looked up in the Trello that Lurker strain
was required . i tried to follow the indicators but kinda ended up with
something else i guess but i really like how it ended so i am making
this PR to see what you think about it.


## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl: diegoflores31
add: Added a new strain for lurker "Vampire".
add: Vampire Lurker exchanges all of your abilities for a fast paced
combat style more focused into dealing damage and
mobility.
add: Active 1 : Rush . Pounces for a maximun of 4 tiles and slashes the
objetive once on impact . applying a screenshake and daze to the target
. Landing this ability reduces the cooldown by half. (cooldown 6
seconds)
add: Active 2 . Flurry : unleashes a 1X3 slash at the targeted direction
that slows your enemies on impact healing you by 30 hp . (cooldown 3
seconds)
add: Active 3 : Tail Jab : Attacks your enemies from a maximun of 2
tiles away while dealing a small amount of damage ( 20) and knocking
them down . if you attack a enemy that is on critical state it will deal
80 damage with penetration and heal you by 150 hp. (cooldown 7 seconds)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Shad0vvs <rtwdevelopment@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [NoKohi/cmss13](https://github.com/NoKohi/cmss13)@[bba6239bc1...](https://github.com/NoKohi/cmss13/commit/bba6239bc19510ecd235acc31ec75783751f9bcc)
#### Friday 2022-12-23 19:53:00 by Stan_Albatross

sniper sentries rebalance (#1951)

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

halves sniper sentry range reduces accuracy a bit ups firerate 

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

being shot at from far offscreen is awful, this should make sniper
sentry a bit more of a threat when it does come into play while not
being able to hit you from half the map away

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
balance: halved the sniper sentry's range to 10 tiles
balance: reduced the sniper sentry's accuracy by 20%
balance: reduced the sniper sentry's delay between shots from 2s to
1.25s
balance: reduced the plasma sentry's range to 10 tiles
balance: reduced the plasma sentry's delay between shots from 10s to 7s
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[e8d76357e2...](https://github.com/re621/dnpcache/commit/e8d76357e28c94ef38545735d1287163f93a662f)
#### Friday 2022-12-23 20:27:30 by bitWolfy

Remove 999 artists from the DNP list.

Removed: sentharn, tealie, einin, freaks, angellsview3, arwenscoots, royalzbed, hellfurred, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, shupamikey, zyegnar, akytti, sootylion, kiva~, peshky, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, sweetishcyborg, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, pixelyteskunk, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, malachimoet, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, pehkeshi, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, infinitedelusion, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, 100101, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, hungothenomster, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, emptyset, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, papyreit, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, terragon, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, gaturo, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, tren, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sprocket_(artist), sincerity_gender, marymanifold, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, carpetwurm, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, lacrimale, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, fluffernubber, koriaris, serena_valentine, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, jasonafex, kabier, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, jdlaclede, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, trunchbull, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, whippytail, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[176f7a0e42...](https://github.com/Comxy/tgstation/commit/176f7a0e422b8417456e1ab65fa59e7ee88a16c5)
#### Friday 2022-12-23 20:51:48 by san7890

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
## [psionic-k/melpa](https://github.com/psionic-k/melpa)@[570bde6b4b...](https://github.com/psionic-k/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Friday 2022-12-23 21:19:33 by Jonas Bernoulli

Cosmetic changes to numerous recipes

This commit only touches recipes whose `:files' property contains an
`:exclude' element, because I had to look at all those recipes for an
only marginally related reason.

To an extend these changes only reflect my own personal preference, so
I will explain the types of changes I have made.  This should serve as
a starting point for a future discussion in case we want to encourage
a certain style or even enforce it.

- Lines should be intended as `indent-for-tab-command' would, except
  in special-cases such as in the recipe of `use-package', which is
  also a macro with special indentation rules; we override those
  because the `use-package' in use-package's recipe is not that macro,
  it is just a symbol appearing as the first element of a data list.

- I prefer it if there is a newline between the package symbol (the
  car) and the plist that follows, but usually only add it to existing
  recipes when lines would otherwise get to long.  I also do not
  change this if I am not making any other changes that affect more
  than one line.

- Either the complete list should be on a single line or each line
  should contain only one key/value pair.  The first pair may share a
  line with the package symbol (see previous point).  If the recipe
  needs more than one line, then two key/value pairs should never
  appear on one line.  Newline characters are cheap enough these days.

- `:fetcher' should come before `:url' or `:repo', not least because
  the former dictates which of the latter two is required/valid.  You
  can also think of the fetcher as the type or class of the recipe,
  which IMO should come first, like in code: (git-fetcher :url val).

- The most common keywords should be specified in this order:
  `:fetcher', `:url'/`:repo', `:files'.  Other keywords should go
  either before or after `:files' (but preferable not on both sides
  of that for any given recipe).

- A common value of `:files' is: (:defaults (:exclude "...")).
  This could be split across multiple lines, but writing everything
  on one line makes it easier to read it as 'use the defaults, except
  exclude "..."':

    :files (:defaults (:exclude "..."))

- If the value of `:files' is too long for one line, then place
  newlines "semantically", instead of trying to "save space".  For
  example any element that is a list should appear on its own line.
  Two sibling lists should never appear on the same line.  String
  siblings should also not appear on one line in many cases, though
  it might makes sense (but isn't my preference) to group them by
  "type" as in:

    (:defaults
     "foo/*.el" "bar/*.el"
     "docs/foo/*.texi" "docs/bar/*.texi"
     (:exclude "..."))

- While there may be multiple (:exclude ...) elements, I've merged
  them into one.  Mostly for future proofing.

- The position of `:exclude' elements in `:files' value is significant
  in theory.  However in most cases it already appears at the very end
  and I have moved it there in cases where the order is not
  significant.  Mostly for future proofing.

---
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[4456381d0f...](https://github.com/rust-lang-ci/rust/commit/4456381d0fd5bc731b26ab2c2579b25810be54e3)
#### Friday 2022-12-23 21:48:12 by bors

Auto merge of #105114 - saethlin:mir-opt-ub-asserts, r=<try>

Tweak assert_unsafe_precondition helpers so they optimize well in MIR

It turns out that https://github.com/rust-lang/rust/pull/104121 does not actually achieve what `@Lokathor` wanted, when debug assertions are enabled. In my opinion there are really multiple issues here, this PR addresses all of them:

The implementation of `is_aligned_and_not_null` is compiled to a shocking amount of MIR, because the implementation of `ptr::is_null` is contorted to work in `const fn`, and the implementation of `ptr::is_aligned` is based on `ptr::is_aligned_to` which among other things has a check that the alignment is a power of 2. These of course clean up quite nicely in LLVM... but the goal here is to enable inlining _before_ we get to LLVM.

Then some of the helper functions aren't `#[inline]`. The MIR inliner only inlines `#[inline]` functions at `-Zmir-opt-level=2`, which is what `--release` corresponds to. Whether or not that heuristic should be loosened up, these are good candidates for inlining so I don't see any harm in adding the attribute.

Then the MIR inlining cost estimation seems a bit pessimistic to me. The MIR we generate tends to have a lot of assignments from locals to locals. By eye it looks like a lot of these could be erased by another optimization pass, so I don't think they represent nearly the complexity of any other instruction. For now, this excludes them from cost estimation entirely.

I also removed the extra function call penalty from diverging call terminators. My logic there is that a diverging terminator is often a panic path, and those sometimes (and especially in this case) have a predicate which can be statically reasoned about. There is a fair chance that inlining a function with a diverging terminator will result in optimizing away the divergence entirely, or making other optimizations after the diverging path, based on assume its predicate. (I'm aware that currently MIR opt is not very good at this sort of cleanup, so this is somewhat of a gamble)

(I hope this looks good in perf...)

r? `@cjgillot`
cc `@JakobDegen`

---
## [kushmish4/kushmish4](https://github.com/kushmish4/kushmish4)@[86706b7810...](https://github.com/kushmish4/kushmish4/commit/86706b7810ff82d828af0c07ec12d1ec0e61b5e6)
#### Friday 2022-12-23 21:53:37 by Kushagra Mishra

Delete README.md

# 💫 About Me:
Favorite Book?<br>THE SELF-TAUGHT PROGRAMMER<br><br>So yeah....Hi, my name is Kushagra Mishra and I am a  a passionate self-taught full stack developer. I have always been fascinated by the world of technology and the endless possibilities it offers...like yeah man i am the person who make website..you want one? Contact me <br>Back to Point<br>I have spent countless hours learning and practicing on my own, and I am confident in my abilities as a full stack developer.<br><br>I have a strong foundation in HTML, CSS, JavaScript, and various back-end technologies such as Node js. and MySQL. I am constantly learning and improving my skills, and I am excited to put my knowledge to use in a professional area.<br><br>As a fresher, I am eager to learn and grow in my career as a full stack developer. I am a fast learner and I am not afraid to take on new challenges. I am confident that my self-motivation and determination will allow me to succeed in this field.


## 🌐 Socials:
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?logo=Facebook&logoColor=white)](https://facebook.com/https://www.facebook.com/kushagra.mishra.5473/) [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/kushagra3527) [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/https://www.linkedin.com/in/kushagra-mishra-0414a6235/) 

# 💻 Tech Stack:
![C](https://img.shields.io/badge/c-%2300599C.svg?style=flat&logo=c&logoColor=white) ![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=flat&logo=c%2B%2B&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=flat&logo=css3&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=flat&logo=html5&logoColor=white) ![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=flat&logo=java&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=flat&logo=javascript&logoColor=%23F7DF1E) ![PHP](https://img.shields.io/badge/php-%23777BB4.svg?style=flat&logo=php&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=flat&logo=amazon-aws&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=flat&logo=bootstrap&logoColor=white) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=flat&logo=django&logoColor=white) ![Angular.js](https://img.shields.io/badge/angular.js-%23E23237.svg?style=flat&logo=angularjs&logoColor=white) ![Angular](https://img.shields.io/badge/angular-%23DD0031.svg?style=flat&logo=angular&logoColor=white) ![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=flat&logo=node.js&logoColor=white) ![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=flat&logo=jquery&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi) ![Apache](https://img.shields.io/badge/apache-%23D42029.svg?style=flat&logo=apache&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=flat&logo=mysql&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=flat&logo=mongodb&logoColor=white) ![Adobe Audition](https://img.shields.io/badge/Adobe%20Audition-9999FF.svg?style=flat&logo=Adobe%20Audition&logoColor=white) ![Adobe Dreamweaver](https://img.shields.io/badge/Adobe%20Dreamweaver-FF61F6.svg?style=flat&logo=Adobe%20Dreamweaver&logoColor=white) ![Adobe Illustrator](https://img.shields.io/badge/adobeillustrator-%23FF9A00.svg?style=flat&logo=adobeillustrator&logoColor=white) ![Adobe InDesign](https://img.shields.io/badge/Adobe%20InDesign-49021F?style=flat&logo=adobeindesign&logoColor=white) ![Adobe XD](https://img.shields.io/badge/Adobe%20XD-470137?style=flat&logo=Adobe%20XD&logoColor=#FF61F6) ![Adobe Premiere Pro](https://img.shields.io/badge/Adobe%20Premiere%20Pro-9999FF.svg?style=flat&logo=Adobe%20Premiere%20Pro&logoColor=white) 	![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=flat&logo=figma&logoColor=white) ![Adobe Photoshop](https://img.shields.io/badge/adobephotoshop-%2331A8FF.svg?style=flat&logo=adobephotoshop&logoColor=white)
# 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=kushmish4&theme=dark&hide_border=false&include_all_commits=true&count_private=false)<br/>
![](https://github-readme-streak-stats.herokuapp.com/?user=kushmish4&theme=dark&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=kushmish4&theme=dark&hide_border=false&include_all_commits=true&count_private=false&layout=compact)

### ✍️ Random Dev Quote
![](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical)

---
[![](https://visitcount.itsvg.in/api?id=kushmish4&icon=0&color=0)](https://visitcount.itsvg.in)

<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->

---
## [Git-Nivrak/cmss13](https://github.com/Git-Nivrak/cmss13)@[8f1ee35f1d...](https://github.com/Git-Nivrak/cmss13/commit/8f1ee35f1de18e295fa29e4536ad00431e7f0d76)
#### Friday 2022-12-23 22:09:00 by carlarctg

Refactored weed crossing to utilize signals and list data. (#1960)

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

Refactored weed slowdown to work based on a signal sent to the recipient
carrying list data.

Added a variable for weed slowdown multiplier to species. Human Heroes
have 0.5 weed slowdown because haha funny. Transferred Yautja's weed
immunity to species.

Added an admin-only example item 'hiking boots' that halve weed
slowdown.

Removed a useless define for XVX.

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


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
refactor: Refactored weed slowdown to work based on a signal sent to the
recipient carrying list data.
code: Added a variable for weed slowdown multiplier to species. Human
Heroes have 0.5 weed slowdown because haha funny. Transferred Yautja's
weed immunity to species.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d770c646dc...](https://github.com/TaleStation/TaleStation/commit/d770c646dcfc162509442b9f3d78b73a2cc878a0)
#### Friday 2022-12-23 22:19:07 by Jolly

i'm so sick and tired of this stupid fucking module (#3794)

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[cd13fcdf46...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/cd13fcdf467b1a9fe5d8fc5256552b0601284dca)
#### Friday 2022-12-23 22:33:59 by Jolly

[MODULAR] contraband.dmi is no longer a hard override on posters (#18106)

* hhngh

* dunks this fucking dmi

* fuck you

---
## [Thoenluk/aoc-thoenluk-2022](https://github.com/Thoenluk/aoc-thoenluk-2022)@[26cc68c336...](https://github.com/Thoenluk/aoc-thoenluk-2022/commit/26cc68c336c306df8062a504ec5e69b20fcecb21)
#### Friday 2022-12-23 22:40:51 by thoenluk

Day 21: Solve day 21.

Let's talk for a moment. Fuck the silly stories and roleplay, which have been nonsensical at best this year to string together exponential optimisation problems.

AoC is full of edge case traps. It always has been. It teaches one to be wary of them even if the specification didn't think of them. It teaches making robust software that can handle errors, or report them early when an assumption turns out to be wrong.

Nothing is wrong with THAT. This challenge, however, is one that contains a trap in a meta assumption which has been true in *every* challenge in the past four years that I have been doing these challenges: If you implement it as described, there is exactly one solution. If there are multiple, you have missed something.

Worse yet, in addition to the meta-assumption suddenly having to be ignored (AKA changing the rules), to my mind there has not been a challenge which included a trap in the specification of the behavior being incomplete.

I cannot immediately recall any challenge in which anything other than integer numbers and integer division were used. Yes, usually it is always specified what to use, and this time it wasn't. Do you know how an engineer reacts to this kind of gap in specification?

We ask. But since we cannot ask the specifier in this case, we are left to assume the default that has been the case EVERY TIME SO FAR stands, which is integer division, and that the description would note if the operation is not applicable under some conditions. Neither is the case now, and public stance I have seen is that this is supposed to be part of the challenge.

Other years I would take this as it is, but the quality of this year has been honestly disappointing in multiple challenges. What comes to mind immediately are Day 19 Part 2, whose description ends in two extremely redundant paragraphs as though one was meant to be deleted, and Day 20, which infuriatingly does not have description or an example showing what happens when a number passes over itself when finding its new spot. While the answer of removing the number first before counting steps is somewhat intuitive, you cannot know for sure until you have solved day 1, as this guess is required for the correct solution and does not come up in the example.

In short. This year's story is nonsensical. The challenges are frankly fine, but entirely too many of them boil down to searching a tree or graph, in which the algorithm itself is trivial but you need to build (real world) heuristics or exploit known input to make them tenable. But even that would be fine, if not a solid third of the Part 2s were "Now do it with way more iterations" which just isn't a challenge when most challenges are already untenable on Part 1 without heavy optimizations. And now we are left to guess at incomplete specification.

Multiple times this year have I been upset not because the problem is hard or has more edge cases than I thought, but because the challenge isn't enjoyable. Either being trivial and/or a functional repeat of another challenge from this year. This has never happened before. Why are you bringing the annoyances of professional development into our free time hacking calendar?

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[91df396ceb...](https://github.com/Buildstarted/linksfordevs/commit/91df396ceb075c26326f179738f57652668da0f5)
#### Friday 2022-12-23 23:10:24 by Ben Dornis

Updating: 12/23/2022 10:00:00 PM

 1. Added: Hacking the LG ThinQ App for use with trackers blocked
    (https://flaviutamas.com/2022/hacking-thinq-app)
 2. Added: Detecting potential cheaters in Advent of Code Leaderboards
    (https://adamfallon.com/aoc/advent-of-code/cheating/2022/12/23/detecting-potential-cheaters-in-private-advent-of-code-leaderboard.html)
 3. Added: 5 traits of a successful team
    (https://jorzel.github.io/5-traits-of-a-successful-team/)
 4. Added: Summarizing “Advance SQL” workshop with ChatGPT
    (https://divyendusingh.com/chatgpt-advance-sql)
 5. Added: How does a Display work?
    (https://gaunergang.de/blog/how-does-a-display-work.html)
 6. Added: RSS Readers That You Can Self Host
    (https://rohanrd.xyz/posts/rss-readers-that-you-can-self-host/)
 7. Added: I Want to Suckless and You Can Too · Bradley Taunt
    (https://bt.ht/suckless/)
 8. Added: rssCloud, WordPress, FeedLand, and Dave Winer – Andy Sylvester's Web
    (https://andysylvester.com/2022/12/22/rsscloud-wordpress-feedland-and-dave-winer/)
 9. Added: Why Monolithic architecture might still be a better fit
    (https://blog.chinaza.dev/why-monolithic-architecture-might-still-be-a-better-fit)
10. Added: 2FA: The Best Way to Annoy Yourself and Everyone Around You
    (https://sandippandey.com/2fa-the-best-way-to-annoy-yourself-and-everyone-around-you/)
11. Added: How to Have Fun Building
    (https://blog.charliemeyer.co/how-to-have-fun-building/)
12. Added: Reverse Engineering Tiktok's VM Obfuscation (Part 1)
    (https://nullpt.rs/reverse-engineering-tiktok-vm-1)
13. Added: How ASUS and a Microsoft Bug Almost Broke Remote Work – nuxx.net
    (https://nuxx.net/blog/2022/12/23/how-asus-and-a-microsoft-bug-almost-broke-remote-work/)
14. Added: Good Enough - Pooya Saeedi
    (https://www.saeedi.dev/good-enough/)
15. Added: Some News About the 4th Edition of Physically Based Rendering
    (https://pharr.org/matt/blog/2022/12/22/pbr-4ed)
16. Added: Securing and exposing local services with Tailscale and Nginx
    (https://blog.viktorpetersson.com/2022/12/23/securing-services-with-tailscale.html)
17. Added: Walk as Spreadsheet
    (https://craigmod.com/ridgeline/115/)

Generation took: 00:10:12.1000358
 Maintenance update - cleaning up homepage and feed

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[6ac9172071...](https://github.com/Danielkaas94/DTAP/commit/6ac917207186bdfa300c2b20e17333613d9da935)
#### Friday 2022-12-23 23:37:47 by Danielkaas94

Goin' Home 🏡
Mother's there, expecting me
Father's waiting too
Lots of folk gathered there
All the friends I knew
All the friends I knew

Nothing's lost, all's gain
No more fret nor pain
No more stumbling on the way
No more longing for the day
Goin' to roam no more

Morning star lights the way
Restless dream all done
Shadows gone, break of day
Real life just begun
There's no break, there's no end
Just a living on
Wide awake with a smile
Goin' on and on

---

