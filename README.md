## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-07](docs/good-messages/2022/2022-02-07.md)


1,706,048 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,706,048 were push events containing 2,690,088 commit messages that amount to 213,010,231 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [TemporalOroboros/tgstation](https://github.com/TemporalOroboros/tgstation)@[079f8ac515...](https://github.com/TemporalOroboros/tgstation/commit/079f8ac51554bb338ac5826c9d06c8d4bc10be80)
#### Monday 2022-02-07 00:46:44 by LemonInTheDark

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
## [tralezab/tgstation](https://github.com/tralezab/tgstation)@[413fd90502...](https://github.com/tralezab/tgstation/commit/413fd9050271829e2899b88a676995ae2517111c)
#### Monday 2022-02-07 01:16:14 by GoldenAlpharex

Dullahan Partial Refactor: They Work Again Edition (#63696)

So, a few months ago I was like "hmm there's something weird going on with party pods...", which got me looking into important_recursive_hearers or something like that. I spoke about it in the coding channel and Kyler actually fixed it before I did. But I also caught a similar glitch with Dullahans, so I decided to investigate...

Two months later...

I present to you a partial unfuckening of the Dullahans, in that I made them fully functional once again:

They only hear speech through their head (not sounds, sadly, someone else would have to tell me how to do that because I otherwise really wouldn't know how to do it in a sane way), they speak through their head, runechat-included.
When you spawn a Dullahan, you're set to look through the Dullahan's eyes (so from their head), and that doesn't reset when you log off and back in, or admin-ghost and come back in your body.
When you're looking through your head, your view will no longer be reset to your body upon entering a locker, which is nice to avoid not being blind while looking through your body.
Dullahan heads no longer look completely lifeless and without organs. They have eyes that don't look dead and that even match the player's intended eye color.
Dullahan can now properly examine things from their head, which was intended and 100% not functional.
Dullahan heads now speak with the proper name of their owner, instead of having a random name attached to it at round-start.
Dullahan heads are also now properly named too.
Dullahans can now properly whisper, sing and do all these funny things that they were unable to do before.
Dullahan whispers will now properly respect the range of the whisper.
Dullahans can now succumb in hardcrit by whispering, as intended. This potentially fixes other species that worked similarly not being able to succumb, like abductors, although I didn't test if they normally could, I just know they absolutely will be able to now.
When switching from Dullahans to a different species, your old head will no longer stay behind.
I also added a proc for species to do some code when we get a ckey login in our mob, which could potentially be useful for other stuff in the future, but it was necessary here as the view is reliant on the client, which we want to ensure doesn't get weird view glitches like having their head's vision overlay while actually being centered on their body.

I also made it so say() now takes a range argument, which is 7 by default, just so things that aren't humans can also whisper and do all those kinds of things. Going with that, there's probably a few more things that will be able to be done better thanks to this, although I haven't tested every edge case with this, but I doubt it will make much of a difference in the future.

---
## [astiob/AVDump3](https://github.com/astiob/AVDump3)@[7b6e588d6c...](https://github.com/astiob/AVDump3/commit/7b6e588d6ca8aaf7f8e2ff59624681cc38c96b57)
#### Monday 2022-02-07 01:54:45 by Oleg Oshmyan

Build MediaInfo native libraries in GitHub CI

This produces highly-optimized MediaInfo library binaries for:

  * Windows x64 (x86-64/AMD64/EM64T/Intel 64)
    (statically linked, so no particular C++ runtime required)
  * macOS x86_64 + arm64 (AArch64) (in one "universal binary" file)
    (all .NET-supported macOS versions)
  * glibc-based Linux x86-64 (Red Hat Enterprise Linux 7 and newer)
  * glibc-based Linux AArch64 (Red Hat Enterprise Linux 7 and newer)
  * musl-based Linux x86-64 (all .NET-supported Alpine versions)
  * musl-based Linux AArch64 (all .NET-supported Alpine versions)

which are the same architectures that AVDump3 currently supports plus
other OS versions/distributions for the same architectures that are
supported by .NET 6 even if not yet supported by AVDump3NativeLib.

Due to the large number of binaries that will need to be included in
the AVDump3 distribution package, they are optimized primarily for size,
potentially at the expense of speed. In my experience, the bulk of time
in AVDump is spent on hashing rather than on MediaInfo, so this should
not be a problem. Furthermore, many of the optimizations improve both
size and speed.

MediaInfo's functionality is heavily culled to include only things that
AVDump3 is actually going to use. These are not general-purpose builds.

I have tried Autotools and CMake for non-Windows and settled on CMake
because it builds faster in every case. (Purely as a guess, perhaps
this is due to Autotools using the notoriously slow Libtool.)
Notably, the slowest build jobs, namely, Linux on emulated ARM,
take ~27min with CMake vs ~35min with Autotools.

The amount of customization required to get optimal output is somewhat
smaller for Autotools, but it is somewhat more arcane, although CMake's
macOS-specific tweaks are arcane as well. CMake has some nicely-named
(if verbose) variables providing native support for -Os and LTO,
but then it lacks configure's --enable-minimal option and uses
suboptimal compiler and linker flags on macOS that cannot be tweaked
without some undocumented variable hacking.

Some of the CMake hacks may no longer be required in the future
if/when I submit the relevant fixes to MediaInfo and if/when CMake
implements nicer overrides for the relevant compiler flags.

Potentially, CMake could also be used on Windows. I have tried
and gotten it far enough to run a build, but it built zlib as a
dynamic library and then tried to reference a static version of it,
failing the build. For what it is worth, I suspect the Visual Studio
project files are better maintained than the CMake files and may
contain more appropriate configuration for Windows. On the other hand,
it would be nice to use a common build process on all platforms.
Furthermore, with CMake it should be possible to use Clang as the
compiler on Windows, which may or may not produce smaller code.

CMake (unlike Autotools) could also be configured to link standard
libraries statically on musl-based Linux, producing binaries that
could in theory run on all Linux distributions, negating the need
for separate glibc-and musl-based binaries. However, when I tried
this and supplied the static-musl MediaInfo.so to AVDump3 on a
glibc-based system, .NET crashed. I was unable to understand why.

For reference, the equivalent Autotools code (without comments) is:

    for project in ZenLib MediaInfoLib; do
      (cd $project/Project/GNU/Library; ./autogen.sh)
      sed -i~ s/-O2/-Os/g $project/Project/GNU/Library/configure
      # or -Oz on macOS
    done
    mv MediaInfoLib/Project/GNU/Library/AddThisToRoot_DLL_compile.sh SO_Compile.sh

    # on Linux:
    . ./setup_devtools.sh
    export AR=gcc-ar NM=gcc-nm RANLIB=gcc-ranlib

    # on macOS:
    export MACOSX_DEPLOYMENT_TARGET='${{ matrix.macosx_version_min }}'
    export Common_Options='--enable-arch-${{ matrix.arch }}'

    export CFLAGS='-flto -fvisibility=hidden'
    export CXXFLAGS='-flto -fvisibility=hidden -fvisibility-inlines-hidden -fno-rtti'
    export LDFLAGS="..."
    export MediaInfoLib_Options='--enable-minimal'

    . ./SO_Compile.sh ${Common_Options}
    # fetch the binary from MediaInfoLib/Project/GNU/Library/.libs/

Possible further optimizations in any case:

MEDIAINFO_ADVANCED_NO could also be defined, but I *think* that would
render mil.Get("Audio_Codec_List") in MediaInfoLibProvider nonfunctional.
But for what it is worth, I think this is the only thing it would affect.

MediaInfo_Option includes a lot of code to handle all the various possible
options that is never used by AVDump3 because it only ever supplies two
specific options. I can dream that it could be somehow removed.

For MSVC (Windows), <ExceptionHandling>false</ExceptionHandling>
could be added to reduce the final size by another 200 KB.
However, if I am reading [MSDN] correctly, this would cause MediaInfo's
defensive catch(...) clauses to catch & mask things like invalid memory
access or division by zero, which should normally crash the application.

[MSDN]: https://docs.microsoft.com/en-us/cpp/build/reference/eh-exception-handling-model

---
## [ijjk/next.js](https://github.com/ijjk/next.js)@[91146b23a2...](https://github.com/ijjk/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Monday 2022-02-07 02:25:20 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---
## [VoltageOS/packages_apps_Launcher3](https://github.com/VoltageOS/packages_apps_Launcher3)@[eaad8603a6...](https://github.com/VoltageOS/packages_apps_Launcher3/commit/eaad8603a660744accee321cd809fc448f21469e)
#### Monday 2022-02-07 03:15:58 by Alex Cruz

Launcher3: Restart with change only on exit

This change allow the user to change everything they have to inside the
homescreen activity and only restart on exit. Previously this was a pain
in the fucking ass because you had to go in and set each option one by one
with a restart inbetween. At least now is not that big of a pain.

- Restart on destroy (hitting the back button, actionbar arrow)
- Restart when a chance is made and the home button is pressed

** Thanks "Jack" for code to detect home button
https://stackoverflow.com/a/27956263

- Cleaned up restart code

eyosen adapted to 10

Change-Id: I4962916ae0bd59d08247b59de585a97a2b9da3a1
Signed-off-by: Dmitrii <bankersenator@gmail.com>

---
## [PurpleFenn/S.P.L.U.R.T-Station-13](https://github.com/PurpleFenn/S.P.L.U.R.T-Station-13)@[a44973ea6a...](https://github.com/PurpleFenn/S.P.L.U.R.T-Station-13/commit/a44973ea6a448f1b75da30e91347cd9ee7a8f8b8)
#### Monday 2022-02-07 03:44:52 by PurpleFenn

Add RTC

This was originally meant to be a joke but I kinda liked the idea so
fuck it. Enjoy, nerds.

---
## [libressl-portable/openbsd](https://github.com/libressl-portable/openbsd)@[e89f0d90bc...](https://github.com/libressl-portable/openbsd/commit/e89f0d90bc681428b013df839f725d5093057894)
#### Monday 2022-02-07 04:29:06 by beck

After much horrible and painful slogging through asn1 code,
this fixes the source of connection problems with ssl/tls connections
between sparc64 and other things.

The punchline, we just found a bug in floating point emulation
on sparc64 when this script produces off-by-one output on sparc64.

This fix is annoyingly easy for the effort expended.

---
## [CandleJaxx/Skyrat-tg](https://github.com/CandleJaxx/Skyrat-tg)@[1f70226654...](https://github.com/CandleJaxx/Skyrat-tg/commit/1f70226654438f75811a2d59ad9c52bf88c048fc)
#### Monday 2022-02-07 04:47:35 by SkyratBot

[MIRROR] Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit [MDB IGNORE] (#11027)

* Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit (#64416)

Removes the 20 second stunlock from tourettes

* Removes the fucking 20 second stunlock rng from tourettes because it's fucking stupid and I just had the most agonizing thirty fucking minutes of my goddamn life, holy shit

Co-authored-by: Iamgoofball <iamgoofball@gmail.com>

---
## [lidatong/agnostic-orderbook](https://github.com/lidatong/agnostic-orderbook)@[5fe64bf2d7...](https://github.com/lidatong/agnostic-orderbook/commit/5fe64bf2d7c373fcab4804be0c9dc98bb55deb10)
#### Monday 2022-02-07 05:05:20 by Charles Li

feat: optimize critbit using serum

feat: almost compiling...

feat: holy shit it compiles

fix: size panic, warnings, get unit tests passing

chore: bump to 2021 ed, solana 1.9.4

feat: add solana-profiler for profiling compute units

chore: CLion is stupid at linting

chore: explicit BorshDeserialize because CLion is stupid, fix warnings

chore: gitignore cargo lock

perf: unsafely transmute Vec<u8> into Slab DST [u8] a la Serum

Revert "perf: unsafely transmute Vec<u8> into Slab DST [u8] a la Serum"

This reverts commit 403d9e72b76781a99140609d9d6b00422f06d576.

chore: remove todo about DST

chore: debug solana unit test issue

---
## [EricomSoftwareLtd/squid](https://github.com/EricomSoftwareLtd/squid)@[4c038a0028...](https://github.com/EricomSoftwareLtd/squid/commit/4c038a0028d59fb7b1f142209e10607f5eecb0e8)
#### Monday 2022-02-07 05:57:45 by Alex Rousskov

Bug 5055: FATAL FwdState::noteDestinationsEnd exception: opening

The bug was caused by commit 25b0ce4. Other known symptoms are:

    assertion failed: store.cc:1793: "isEmpty()"
    assertion failed: FwdState.cc:501: "serverConnection() == conn"
    assertion failed: FwdState.cc:1037: "!opening()"

This change has several overlapping parts. Unfortunately, merging
individual parts is both difficult and likely to cause crashes.

## Part 1: Bug 5055.

FwdState used to check serverConn to decide whether to open a connection
to forward the request. Since commit 25b0ce4, a nil serverConn pointer
no longer implies that a new connection should be opened: FwdState
helper jobs may already be working on preparing an existing open
connection (e.g., sending a CONNECT request or negotiating encryption).

Bad serverConn checks in both FwdState::noteDestination() and
FwdState::noteDestinationsEnd() methods led to extra connectStart()
calls creating two conflicting concurrent helper jobs.

To fix this, we replaced direct serverConn inspection with a
usingDestination() call which also checks whether we are waiting for a
helper job. Testing that fix exposed another set of bugs: The helper job
pointers or in-job connections left stale/set after forwarding failures.
The changes described below addressed (most of) those problems.

## Part 2: Connection establishing helper jobs and their callbacks

A proper fix for Bug 5055 required answering a difficult question: When
should a dying job call its callbacks? We only found one answer which
required cooperation from the job creator and led to the following
rules:

* AsyncJob destructors must not call any callbacks.

* AsyncJob::swanSong() is responsible for async-calling any remaining
  (i.e. set, uncalled, and uncancelled) callbacks.

* AsyncJob::swanSong() is called (only) for started jobs.

* AsyncJob destructing sequence should validate that no callbacks remain
  uncalled for started jobs.

... where an AsyncJob x is considered "started" if AsyncJob::Start(x)
has returned without throwing.

A new JobWait class helps job creators follow these rules while keeping
track on in-progress helper jobs and killing no-longer-needed helpers.

Also fixed very similar bugs in tunnel.cc code.

## Part 3: ConnOpener fixes

1. Many ConnOpener users are written to keep a ConnectionPointer to the
   destination given to ConnOpener. This means that their connection
   magically opens when ConnOpener successfully connects, before
   ConnOpener has a chance to notify the user about the changes. Having
   multiple concurrent connection owners is always dangerous, and the
   user cannot even have a close handler registered for its now-open
   connection. When something happens to ConnOpener or its answer, the
   user job may be in trouble. Now, ConnOpener callers no longer pass
   Connection objects they own, cloning them as needed. That adjustment
   required adjustment 2:

2. Refactored ConnOpener users to stop assuming that the answer contains
   a pointer to their connection object. After adjustment 1 above, it
   does not. HappyConnOpener relied on that assumption quite a bit so we
   had to refactor to use two custom callback methods instead of one
   with a complicated if-statement distinguishing prime from spare
   attempts. This refactoring is an overall improvement because it
   simplifies the code. Other ConnOpener users just needed to remove a
   few no longer valid paranoid assertions/Musts.

3. ConnOpener users were forced to remember to close params.conn when
   processing negative answers. Some, naturally, forgot, triggering
   warnings about orphaned connections (e.g., Ident and TcpLogger).
   ConnOpener now closes its open connection before sending a negative
   answer.

4. ConnOpener would trigger orphan connection warnings if the job ended
   after opening the connection but without supplying the connection to
   the requestor (e.g., because the requestor has gone away). Now,
   ConnOpener explicitly closes its open connection if it has not been
   sent to the requestor.

Also fixed Comm::ConnOpener::cleanFd() debugging that was incorrectly
saying that the method closes the temporary descriptor.

Also fixed ConnOpener callback's syncWithComm(): The stale
CommConnectCbParams override was testing unused (i.e. always negative)
CommConnectCbParams::fd and was trying to cancel the callback that most
(possibly all) recipients rely on: ConnOpener users expect a negative
answer rather than no answer at all.

Also, after comparing the needs of two old/existing and a temporary
added ("clone everything") Connection cloning method callers, we decided
there is no need to maintain three different methods. All existing
callers should be fine with a single method because none of them suffers
from "extra" copying of members that others need. Right now, the new
cloneProfile() method copies everything except FD and a few
special-purpose members (with documented reasons for not copying).

Also added Comm::Connection::cloneDestinationDetails() debugging to
simplify tracking dependencies between half-baked Connection objects
carrying destination/flags/other metadata and open Connection objects
created by ConnOpener using that metadata (which are later delivered to
ConnOpener users and, in some cases, replace those half-baked
connections mentioned earlier. Long-term, we need to find a better way
to express these and other Connection states/stages than comments and
debugging messages.

## Part 4: Comm::Connection closure callbacks

We improved many closure callbacks to make sure (to the extent possible)
that Connection and other objects are in sync with Comm. There are lots
of small bugs, inconsistencies, and other problems in Connection closure
handlers. It is not clear whether any of those problems could result in
serious runtime errors or leaks. In theory, the rest of the code could
neutralize their negative side effects. However, even in that case, it
was just a matter of time before the next bug will bite us due to stale
Connection::fd and such. These changes themselves carry elevated risk,
but they get us closer to reliable code as far as Connection maintenance
is concerned; otherwise, we will keep chasing their deadly side effects.

Long-term, all these manual efforts to keep things in sync should become
unnecessary with the introduction of appropriate Connection ownership
APIs that automatically maintain the corresponding environments (TODO).

## Part 5: Other notable improvements in the adjusted code

Improved Security::PeerConnector::serverConn and
Http::Tunneler::connection management, especially when sending negative
answers. When sending a negative answer, we would set answer().conn to
an open connection, async-send that answer, and then hurry to close the
connection using our pointer to the shared Connection object. If
everything went according to the plan, the recipient would get a non-nil
but closed Connection object. Now, a negative answer simply means no
connection at all. Same for a tunneled answer.

Refactored ICAP connection-establishing code to to delay Connection
ownership until the ICAP connection is fully ready. This change
addresses primary Connection ownership concerns (as they apply to this
ICAP code) except orphaning of the temporary Connection object by helper
job start exceptions (now an explicit XXX). For example, the transaction
no longer shares a Connection object with ConnOpener and
IcapPeerConnector jobs.

Probably fixed a bug where PeerConnector::negotiate() assumed that a
sslFinalized() does not return true after callBack(). It may (e.g., when
CertValidationHelper::Submit() throws). Same for
PeekingPeerConnector::checkForPeekAndSpliceMatched().

Fixed FwdState::advanceDestination() bug that did not save
ERR_GATEWAY_FAILURE details and "lost" the address of that failed
destination, making it unavailable to future retries (if any).

Polished PeerPoolMgr, Ident, and Gopher code to be able to fix similar
job callback and connection management issues.

Polished AsyncJob::Start() API. Start() used to return a job pointer,
but that was a bad idea:

* It implies that a failed Start() will return a nil pointer, and that
  the caller should check the result. Neither is true.

* It encourages callers to dereference the returned pointer to further
  adjust the job. That technically works (today) but violates the rules
  of communicating with an async job. The Start() method is the boundary
  after which the job is deemed asynchronous.

Also removed old "and wait for..." post-Start() comments because the
code itself became clear enough, and those comments were becoming
increasingly stale (because they duplicated the callback names above
them).

Fix Tunneler and PeerConnector handling of last-resort callback
requirements. Events like handleStopRequest() and callException() stop
the job but should not be reported as a BUG (e.g., it would be up to the
callException() to decide how to report the caught exception). There
might (or there will) be other, similar cases where the job is stopped
prematurely for some non-BUG reason beyond swanSong() knowledge. The
existence of non-bug cases does not mean there could be no bugs worth
reporting here, but until they can be identified more reliably than all
these benign/irrelevant cases, reporting no BUGs is a (much) lesser
evil.

TODO: Revise AsyncJob::doneAll(). Many of its overrides are written to
check for both positive (i.e. mission accomplished) and negative (i.e.
mission cancelled or cannot be accomplished) conditions, but the latter
is usually unnecessary, especially after we added handleStopRequest()
API to properly support external job cancellation events. Many doneAll()
overrides can probably be greatly simplified.

----

Cherry picked SQUID-568-premature-serverconn-use-v5 commit 22b5f78.

---
## [GesuBackups/tgstation](https://github.com/GesuBackups/tgstation)@[b48cda6afa...](https://github.com/GesuBackups/tgstation/commit/b48cda6afa047be95390dc1360e8d899ec6394b0)
#### Monday 2022-02-07 06:27:24 by LemonInTheDark

Fixes harddels in pinned module code, cleans up a musty pattern that I want to die (#64674)

* Please stop typecasting target, noooooooooooooooooo

* Fixes harddels in pinned module code

The logic for pinned modules was intentionally hanging references to the
mob that pinned the action button. I have depression.

The pinned_to list also was never fully cleared, but that would have
just exasperated the issue. I've converted its use of mobs to refs, and
its use of the module var into something better managed

(Friendly reminder that actions will persist in your nightmares forever
unless they are manually qdel'd, this code wasn't doing that.

Also cleaned up how the pinned_to list is managed, hopefully it's a bit
more action centered now

---
## [BoHBranch/BoH-Bay](https://github.com/BoHBranch/BoH-Bay)@[37e11b2d57...](https://github.com/BoHBranch/BoH-Bay/commit/37e11b2d5791ceba5426fbfe3cadd4d0576097b5)
#### Monday 2022-02-07 06:52:36 by Carl?

Merge pull request #1130 from BoHBranch/Rippin&Tear

Fuck you. *Removes abusable traits*

---
## [skepfusky/pandapaco-art-statistics](https://github.com/skepfusky/pandapaco-art-statistics)@[536cb89f4f...](https://github.com/skepfusky/pandapaco-art-statistics/commit/536cb89f4fb070c89fd1436a52a0098d67d248a6)
#### Monday 2022-02-07 07:12:37 by Kerby Keith Aquino

Squashing unoptimized Python code lol

Updated dataset

struggling with decoupling stringed arrays

yes

Finally found a way to decouple stuff

Added more shit in python lol

Writing the worst and unoptimized code ever

getting the hang of it
ugh I'm kinda stumped until here, damn

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[32e088ce7a...](https://github.com/repinger/exynos9611_m21_kernel/commit/32e088ce7aa0b53895bc494f49dea96356991d49)
#### Monday 2022-02-07 07:28:18 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, tbsvc, and typec as they do not exist here]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[38f66c8418...](https://github.com/cyberitsolutions/bootstrap2020/commit/38f66c8418d449d82aed7a476584f702c63febc2)
#### Monday 2022-02-07 07:45:38 by Trent W. Buck

rsyslog: read /*/log/journal/*.journal (not /run/systemd/journal/syslog)

If systemd-journald provided a RELP push instead of HTTP pull,
we would not need any of this bullshit.

The rsyslog docs say basically:

  1. journald was created by Lennart in secret with no consultation
     from existing logging experts (even personal friends like Gerhard),
     and is a bit dumb.

  2. imjournal can break when .journal files are corrupt (due to journald bugs).
     When this happens, rsyslogd will logspam downstream log servers.
     Therefore do not use imjournal unless you really have to.

  3. imuxsock defaults to /dev/log and will delete anything already
     there, put a ryslog listener there, and remove it when rsyslog
     exists.

     BUT if rsyslog detects that systemd is around,
     it will instead use /run/systemd/journal/syslog.
     This is why journald is hard-coded to WRITE to.

     This can also break due to journald bugs, but
     when this happens, the result is lost messages, not log spam.
     Therefore use this one.

We have used imuxsock just fine with a hard-coded rsyslog.conf for a decade.

We recently switched to using a systemd unit that configures
rsyslog.conf dynamically for the local network, based on SRV records.
When we did that, rsyslog broke and started listening on /dev/log
instead of / as well as /run/systemd/journal/syslog.

The problem GOES AWAY if we turn off all get-config-from-dnssd* files.
i.e. SOMEHOW we caused this.

I tried for about 6 hours to isolate and fix this problem, by
juggling the systemd unit hooks.  In the end I gave up.

I am using imjournal instead now which I think works better???
I'm slightly scared of #1 though.

https://www.rsyslog.com/doc/v8-stable/configuration/modules/imuxsock.html#coexistence-with-systemd
https://www.rsyslog.com/doc/v8-stable/configuration/modules/imjournal.html

---
## [ProjectFaerun/Faerun](https://github.com/ProjectFaerun/Faerun)@[2843512aac...](https://github.com/ProjectFaerun/Faerun/commit/2843512aac6326cfbaf8bf843d0a78e52e43ca9a)
#### Monday 2022-02-07 07:57:33 by ScarletStars

The Neverwinter Update

- Updated lore character traits and appearances in Neverwinter: all-too-familiar companions in the official campaigns now appear as they should and have more fleshed out histories, houses, and relationships as appropriate. A constant WIP of course and more lore characters are set to be added based on relevance. Certain characters have been given families as needed, and other minute details such as more immersive character dynasty shields and even the terms of certain members of the Neverwinter Nine are now reflected.

- The Kalach-Cha is now playable during the War of Shadows through the command of Crossroad Keep! While technically acting as vassal, she will now participate as an ally to denote her key leadership in the historic war. Now reflected as troops in the war are the factions united by the Kalach-Cha under her command: the Ironfist Clan and the Sahuagin of the Mere. Support will soon be added to play out the union of various factions when starting in the months leading up to the confrontation against the King of Shadows.

- Soon to be added: support for correctly annihilating the King of Shadows after the War of Shadows and destruction of temporary Knight-Captaincy of Crossroad Keep should the Kalach-Cha gain another county, fleshing out the Mask of the Betrayer segment history, and the choice for both the Kalach-Cha and possibly the Hero of Neverwinter to start as male or female (figured out how to do this, but more time is needed).

---
## [lordcheng10/guava](https://github.com/lordcheng10/guava)@[e015172847...](https://github.com/lordcheng10/guava/commit/e0151728478c16e3fe295a368ba74c2195a10e85)
#### Monday 2022-02-07 09:01:50 by cpovirk

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
## [T-J-Teru/binutils-gdb](https://github.com/T-J-Teru/binutils-gdb)@[bbea680797...](https://github.com/T-J-Teru/binutils-gdb/commit/bbea68079781ac4c2fc941867ee9888585cafb77)
#### Monday 2022-02-07 10:21:51 by Andrew Burgess

gdb/python: improve the auto help text for gdb.Parameter

This commit attempts to improve the help text that is generated for
gdb.Parameter objects when the user fails to provide their own
documentation.

Documentation for a gdb.Parameter is currently pulled from two
sources: the class documentation string, and the set_doc/show_doc
class attributes.  Thus, a fully documented parameter might look like
this:

  class Param_All (gdb.Parameter):
     """This is the class documentation string."""

     show_doc = "Show the state of this parameter"
     set_doc = "Set the state of this parameter"

     def get_set_string (self):
        val = "on"
        if (self.value == False):
           val = "off"
        return "Test Parameter has been set to " + val

     def __init__ (self, name):
        super (Param_All, self).__init__ (name, gdb.COMMAND_DATA, gdb.PARAM_BOOLEAN)
        self._value = True

  Param_All ('param-all')

Then in GDB we see this:

  (gdb) help set param-all
  Set the state of this parameter
  This is the class documentation string.

Which is fine.  But, if the user skips both of the documentation parts
like this:

  class Param_None (gdb.Parameter):

     def get_set_string (self):
        val = "on"
        if (self.value == False):
           val = "off"
        return "Test Parameter has been set to " + val

     def __init__ (self, name):
        super (Param_None, self).__init__ (name, gdb.COMMAND_DATA, gdb.PARAM_BOOLEAN)
        self._value = True

  Param_None ('param-none')

Now in GDB we see this:

  (gdb) help set param-none
  This command is not documented.
  This command is not documented.

That's not great, the duplicated text looks a bit weird.  If we drop
different parts we get different results.  Here's what we get if the
user drops the set_doc and show_doc attributes:

  (gdb) help set param-doc
  This command is not documented.
  This is the class documentation string.

That kind of sucks, we say it's undocumented, then proceed to print
the documentation.  Finally, if we drop the class documentation but
keep the set_doc and show_doc:

  (gdb) help set param-set-show
  Set the state of this parameter
  This command is not documented.

That seems OK.

So, I think there's room for improvement.

With this patch, for the four cases above we now see this:

  # All values provided by the user, no change in this case:
  (gdb) help set param-all
  Set the state of this parameter
  This is the class documentation string.

  # Nothing provided by the user, the first string is now different:
  (gdb) help set param-none
  Set the current value of 'param-none'.
  This command is not documented.

  # Only the class documentation is provided, the first string is
  # changed as in the previous case:
  (gdb) help set param-doc
  Set the current value of 'param-doc'.
  This is the class documentation string.

  # Only the set_doc and show_doc are provided, this case is unchanged
  # from before the patch:
  (gdb) help set param-set-show
  Set the state of this parameter
  This command is not documented.

The one place where this change might be considered a negative is when
dealing with prefix commands.  If we create a prefix command but don't
supply the set_doc / show_doc strings, then this is what we saw before
my patch:

  (gdb) python Param_None ('print param-none')
  (gdb) help set print
  set print, set pr, set p
  Generic command for setting how things print.

  List of set print subcommands:

  ... snip ...
  set print param-none -- This command is not documented.
  ... snip ...

And after my patch:

  (gdb) python Param_None ('print param-none')
  (gdb) help set print
  set print, set pr, set p
  Generic command for setting how things print.

  List of set print subcommands:

  ... snip ...
  set print param-none -- Set the current value of 'print param-none'.
  ... snip ...

This seems slightly less helpful than before, but I don't think its
terrible.

Additionally, I've changed what we print when the get_show_string
method is not provided in Python.

Back when gdb.Parameter was first added to GDB, we didn't provide a
show function when registering the internal command object within
GDB.  As a result, GDB would make use of its "magic" mangling of the
show_doc string to create a sentence that would display the current
value (see deprecated_show_value_hack in cli/cli-setshow.c).

However, when we added support for the get_show_string method to
gdb.Parameter, there was an attempt to maintain backward compatibility
by displaying the show_doc string with the current value appended, see
get_show_value in py-param.c.  Unfortunately, this isn't anywhere
close to what deprecated_show_value_hack does, and the results are
pretty poor, for example, this is GDB before my patch:

  (gdb) show param-none
  This command is not documented. off

I think we can all agree that this is pretty bad.

After my patch, we how show this:

  (gdb) show param-none
  The current value of 'param-none' is "off".

Which at least is a real sentence, even if it's not very informative.

This patch does change the way that the Python API behaves slightly,
but only in the cases when the user has missed providing GDB with some
information.  In most cases I think the new behaviour is a lot better,
there's the one case (noted above) which is a bit iffy, but I think is
still OK.

I've updated the existing gdb.python/py-parameter.exp test to cover
the modified behaviour.

Finally, I've updated the documentation to (I hope) make it clearer
how the various bits of help text come together.

---
## [AospExtended-Devices/kernel_oneplus_sm8150](https://github.com/AospExtended-Devices/kernel_oneplus_sm8150)@[3b48695651...](https://github.com/AospExtended-Devices/kernel_oneplus_sm8150/commit/3b4869565121be16d0d38b5e34f20fcfbaa64273)
#### Monday 2022-02-07 12:36:29 by alk3pInjection

drm: Handle dim for udfps

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
## [mikebmcl/ReactiveUIUnoSample](https://github.com/mikebmcl/ReactiveUIUnoSample)@[653cb0f4f4...](https://github.com/mikebmcl/ReactiveUIUnoSample/commit/653cb0f4f4331ff45d3fec9e9cf05eb52d1a4d93)
#### Monday 2022-02-07 14:52:51 by Michael B. McLaughlin

Managed to add unit testing with only significant changes to many things. I created and added ISchedulerProvider thinking I would need it for testing but so far I don't. Still, it's a useful abstraction that will be helpful if I decide to take the plunge and create a second shared project so that I can add the one with all the UI bits excluding App and possibly MainView as a project reference to UITests since it is a library and so all of the app initialization stuff (i.e. App.xaml) is not allowed to be included in it in any way. This is some ugly code in a lot of places because what I thought would be easy and take an hour has been not so easy and has taken 8+ hours. I just want to commit it and relax for a bit on what's left of Sunday. I'll clean it up and improve it soon. Also, in the end most of the frustration came down to the fact that I am relying on WASM for testing to avoid setting up AppCenter stuff for this project, which I would need to do to test on Android (WASM, Android, and iOS are the only currently supported platforms for Uno.UITest projects). Anyway, the current stable of Uno.UITest.Helpers only looks for 32-bit (Program Files (x86)) Chrome installations and it can only be used with Chrome, and I have 64-bit (Program Files) Chrome installed. None of the error messages were remotely helpful, I finally had to clone the Uno.UITests repo in order to discover that it worked fine but then when I upgraded it to Uno 4 from 3.7 it stopped working too which eventually led to the discovery of the problem with the solution finally being that the current experimental Uno.UITest.Helpers (1.1.0-dev.32) has support for detecting and using 64-bit Chrome so I updated to that and it now all works. Yay. Relax now. Clean up and improve later or tomorrow.

---
## [JacksonTaylorxyz/dwm](https://github.com/JacksonTaylorxyz/dwm)@[67d76bdc68...](https://github.com/JacksonTaylorxyz/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Monday 2022-02-07 15:25:14 by Chris Down

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
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[d56dd7b42a...](https://github.com/ammarfaizi2/linux-block/commit/d56dd7b42a26b337590a0975212e204bca660cc2)
#### Monday 2022-02-07 16:01:09 by Jason A. Donenfeld

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
Reviewed-by: Jean-Philippe Aumasson <jeanphilippe.aumasson@gmail.com>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[906fb0682b...](https://github.com/tgstation/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Monday 2022-02-07 16:29:20 by necromanceranne

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
## [TriHardspace/Mainsite](https://github.com/TriHardspace/Mainsite)@[610e6cc96c...](https://github.com/TriHardspace/Mainsite/commit/610e6cc96c1d7ad3fb66645c46a894a4f9d9e82d)
#### Monday 2022-02-07 17:29:30 by Tyler Hoban

this shit is fucking awful, dont fucking commit it to main until fixed

its a rush placeholder

---
## [Dudemanguy/mpv](https://github.com/Dudemanguy/mpv)@[c053d25eab...](https://github.com/Dudemanguy/mpv/commit/c053d25eabf2310243828f7657746e6b10d29b29)
#### Monday 2022-02-07 17:33:51 by Dudemanguy

wayland: partially fix drag and drop handling

Drag and drop in wayland is weird and it seems everyone does this
slightly differently (fun). In the past, there was a crash that
occured (fixed by 700f4ef5fad353800fa866b059663bc1dd58d3b7) which
involved using the wl_data_offer_finish in an incorrect way that
triggered a protocol error (always fatal). The fix involved moving the
function call to data_device_handle_drop which seemingly works, but it
has an unfortunate side effect. It appears like GTK applications (or at
least firefox) close the pipe after this function is called which makes
it impossible for mpv to read data from the fd (well you could force it
open again in theory but let's not do that). Who knows if that was the
case when that commit was made (probably not because I'd think I would
have noticed; could just be a dummy though), but obviously having broken
dnd for a major application isn't so fun (this works with QT and
chromium anyway).

Ideally one would just simply check the pipe in data_device_handle_drop,
but this doesn't work because it doesn't seem the compositor actually
sends mpv the data by then. There's not actually a defined event when
you're supposed to be able to read data from this pipe, so we wait for
the usual event checking loop later for this. In that case,
wl_data_offer_finish needs to go back into check_dnd_fd, but we have to
be careful when calling it otherwise we'd just commit protocol errors
like before. We check to make sure we even have a valid wl->dnd_offer
before trying to indicate that it is finished and additionally make sure
there is a valid dnd_action (after checking the fd, it's always set back
to -1).

This doesn't fix everything though. Specifically, sway with
focus_follows_mouse (the default) and GTK as the data source still
doesn't work. The reason is that when you do a drag and drop in sway
with that option on, a new wl_data_device.data_offer event is sent out
instantly after the drop event. This happens before any data is sent
across the fd and before mpv even has a chance to check it. What GTK
does, when getting this new data_offer event, is close the pipe
(POLLHUP). This means mpv can't read it when we reach the event loop and
thus no data is ever read and broken drag and drop. From the client
side, this isn't really fixable since the wayland protocol doesn't have
a clear indication of when clients are supposed to read from the fd and
both the compositor and data source are doing things totally out of our
control. So we'll consider this weird case, "not our bug" at least. The
rest should work.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[49d5ea83d2...](https://github.com/mrakgr/The-Spiral-Language/commit/49d5ea83d29f3ff386f754d3c6de7b876009c99c)
#### Monday 2022-02-07 18:44:34 by Marko Grdinić

"10:30am. Since this journal file is already 155k lines, maybe it is time to start thinking about starting a new one.

10:35am. Ok, let me start. The sooner I finish this scene, and the sooner I get good at art, the sooner I can get a handle on my life. I need a proper money making skill, right now I could only wage slave with programming.

10:45am. Focus me. Let me the flower into a subnet.

Hmmm, how do I reuse subnets? Also how do I add params to it.

https://youtu.be/SiT4r22BWY8
Houdini Basics - 6 Tips and Tricks when working with Houdini Digital Assets!

I am confused. Let me just watch stuff related to digital assets.

11:05am. I am confused. Why do subnets have 4 inputs. What if I needed more or less?

Let me continue watching the HDA vid.

11:15am. https://youtu.be/SiT4r22BWY8?t=781

Oh, this is a really good way of moving stuff to the main level.

...Let me just ask about subnet inputs.

///

Why do subnets have 4 inputs? Is it possible to change this so they have more or less?

Also, I want to factor some of the functionality that I've made, do I have to turn those parts into HDAs? HDAs end up being separate files, while I just want some functions (in programming parlance) that I could easily reuse. Having a file for every function would create a mess.

I suppose I could try reusing subnets, but I am not sure how to do that from different objects for example.

///

11:35am. Shit.

///

>>880774
>not sure what your objection to hdas is, esp vs subnets. you don't have to load all your hdas in with every project. asset > install asset library will let you bring in hdas on a per project basis.
Imagine if you were programming in Python and had to have a different file for each function. I don't yet understand how to deal with HDAs properly.

```
  File "<stdin>", line 1
    { 'event_type': hou.hdaEventType.LibraryInstalled, 'library_path' : 'E:/Art Projects/YYY/XXX_Flower.hdanc' }
                                                                                              ^
SyntaxError: invalid syntax
```

Also, for some reason I got a Python error when turning a subnet into a HDA. I obfuscated the YYY and XXX, but otherwise it is the same. Should I be worried about this?

///

12:05pm. It seems to have something to do with input labels. No matter.

Right now I've turned a subnet into a HDA. But how do I edit the HDA after I've created it?

https://www.youtube.com/playlist?list=PLXNFA1EysfYnnm2-UZmxrd-MWC7LTWEVl

This is so annoying and confusing. Let me watch this playlist on HDAs.

I factored out that flower, but I have no idea how to deal with it after that. I am also going to have to look into advanced instancing. I am not sure how to select between leaves and branches. Well, let me do it one step at a time. First of all, let me figure out how to edit the HDAs.

Ah, I see. There is a Save Asset option that I need to click in order for it to take effect.

If I want to edit the asset from somewhere else, I just need to unlock it. Ok, good. I figured out the HDA basics. Let me continue with the video.

Once I finish the playlist, what I will have to do is dive deeper into scattering. I might have studied this in the past, but I haven't properly internalized how to copy objects to points while selecting. There are different ways of doing it too. I have to go with an approach that satisfies me.

Also I realized that I've made a mistake in never using copy to curve. But it is not a big deal.

12:50pm. https://youtu.be/tWjIWEgoOf8?list=PLXNFA1EysfYnnm2-UZmxrd-MWC7LTWEVl
Houdini Digital Assets | 3. Create Parameters

Let me stop here. I am warming up towards the HDAs. They'll be super useful.

1:50pm. Done with breakfast. Let me do the chores here. Then I will resume.

2:55pm. Today the chores took a while.

At any rate, I am finally ready to start. What is next? I need to go through the HDA playlist. Also I need to figure out how to scatter properly. Let me start with the scatter tutorials. I'll go over the ones that I've already watched.

Actually, let me chill with the Baki raw thread first.

https://youtu.be/N7CDHwgWKVo
Advanced Scattering in Houdini 18.5

Let me start this.

3:10pm. I must have been completely blind. How did I miss the `Copy To Points` and `Copy To Curves` having piece attributes?

Let me try it out.

3:20pm. Huh, I do not know. It is not working for some reason.

3:30pm. This is wonderful. I figured it out completely. It turns out that attribute randomize can be used to assign weights to a particular string. That will make it easy to deal with.

Still when it comes to distributing leaves and branches, I won't be able to use this to do that automatically. The scatter points require tagging ahead of time so that the copy to points node can select which geometry to instantiate.

3:45pm. As it turns out, it is possible to drag the UI element where you put down the distribution into the param interface. Things are really coming together for me. I can see now that I can simply pass in the packed geometry and then pass the distribution via a channel. Giving a leaf a weight of 9 and a branch a weight of 1 should be no problem at all thanks to Attribute Rnadomize.

One thing I do not get is how to do the default params. Right now it always starts at 0 or something like that instead of something sensible.

4pm. Focus me. I've figured out a big part of what will make scattering useful. This thing here is literally why I ditched Blender 3 weeks ago. Now let me go through the HDA playlist.

4:10pm. https://youtu.be/tWjIWEgoOf8?list=PLXNFA1EysfYnnm2-UZmxrd-MWC7LTWEVl&t=419

Here are the defaults. Under the `Channels` tab.

4:45pm. Had to take a break. Let me resume. What I will dedicate my time is getting through the playlist.

https://youtu.be/VHEBtm939FM?list=PLXNFA1EysfYnnm2-UZmxrd-MWC7LTWEVl
Houdini Digital Assets | 4. Create Toggles and Menus

Time for this.

I'll focus on the playlist and thne I am going to come in and deal with the vines.

5:20pm. https://youtu.be/g5E4GYKlY18?list=PLXNFA1EysfYnnm2-UZmxrd-MWC7LTWEVl
Houdini Digital Assets | 7. Structure the Interface

Having to watch these vids is torture by tedium. But let me just go through them. Then I will focus whole heartedly on the task at hand.

...No, forget it. I should be working on my own things. That is what will maximally motivate me. Let me finish the flower.

5:50pm. Good, I finally did the branch.

This was what tripped me up in Blender. So far though, I have only two variants, but should I want to, I could easily randomize it. I should turn the flower itself into a HDA. Right now, I only have its template as a HDA. But instead of having two objects, I can have two HDAs. That will allow me to vary the branches a lot more significantly.

Before I do anything though I should set up the camera. I want the shot to look good from below. Let me put in Luna's bounding box.

6:15pm. Damn it, putting the camera in the exact place I want sure is difficult. I really have to fight the natural navigation. Just why does first person navigation works so shitily? I am going to have to look into that more. At any rate, the angle I have should be fine.

7pm. Had to leave for lunch. Right now I should be making progress, but in a way I am even though I am not doing anything. Right now, I am taking a step back to admire my handiwork.

7:15pm. Let me close here. I am imagining what I should do here, and the answer I feel should be more variation. What I need at this moment is more variation. Then I'll do some mask work. Mask from feature should be what I need to get the right angles. Then I'll take out one of the beams.

Hrmmmm, should I then add another main wine?

That is what is really troubling me.

7:20pm. Amateurs always make the mistake of trying to put in too much detail. My sense is that what I have now should be enough.

7:25pm. Hmmm, yeah, it is good. I'll just translate Luna a bit to the left, in effect moving the stuff above to the right. That should bring it more into focus.

And after that what I want to do is put in a bit more variation. Doing it like I envision should also ensure that the leaves are always pointing downwards. Right now some of the branch flowers are defying gravity.

7:30pm. Let me close here. I am going to finish the vines tomorrow without fussing too much about it. That will allow me to deal with the rest afterwards. When the rest is done, what I will do is sculpt Luna. After that will come texturing and the fun shading stuff. Lastly will come painting.

I think at this point I can finally consider myself to have just a bit of skill at Houdini.

7:35pm. I need to keep pushing. This kind of mentally demanding owrk is also a good way getting my brain up to par after Covid. I think I am pretty good right now, but my senses of taste and smell still haven't come back properly.

7:40pm. Let's do this me. Now that I have HDAs in by toolbox, I have everything I need to create the right amount of variation. I need to tap into that and bring this scene to a close. After I properly internalize this, my speed on future projects should go way up."

---
## [Caulaflower/CombatExtended](https://github.com/Caulaflower/CombatExtended)@[e9c4ac2915...](https://github.com/Caulaflower/CombatExtended/commit/e9c4ac29158608d0b4d0349dd2984784d954fba2)
#### Monday 2022-02-07 19:02:36 by AL9000

mortar

"You know what, fuck you!"
*replaces mortar def*

---
## [oracle/dtrace-linux-kernel](https://github.com/oracle/dtrace-linux-kernel)@[c6e92f3543...](https://github.com/oracle/dtrace-linux-kernel/commit/c6e92f354335ab7bbcec46ccbc9fc81ae123900a)
#### Monday 2022-02-07 19:23:24 by Nick Alcock

waitfd: new syscall implementing waitpid() over fds

This syscall, originally due to Casey Dahlin but significantly modified
since, is called quite like waitid():

	fd = waitfd(P_PID, some_pid, WEXITED | WSTOPPED, 0);

This returns a file descriptor which becomes ready whenever waitpid()
would return, and when read() returns the return value waitpid() would
have returned.  (Alternatively, you can use it as a pure indication that
waitpid() is callable without hanging, and then call waitpid()).  See the
example in tools/testing/selftests/waitfd/.

The original reason for rejection of this patch back in 2009 was that it
was redundant to waitpid()ing in a separate thread and transmitting
process information to another thread that polls: but this is only the
case for the conventional child-process use of waitpid().  Other
waitpid() uses, such as ptrace() returns, are targetted on a single
thread, so without waitfd or something like it, it is impossible to have
a thread that both accepts requests for servicing from other threads
over an fd *and* manipulates the state of a ptrace()d process in
response to those requests without ugly CPU-chewing polling (accepting
requests requires blocking in poll() or select(): handling the ptraced
process requires blocking in waitpid()).

There is one ugliness in this patch which I would appreciate suggestions
to improve (due to me, not due to Casey, don't blame him).  The poll()
machinery expects to be used with files, or things enough like files
that the wake_up key contains an indication as to whether this wakeup
corresponds to a POLLIN / POLLOUT / POLLERR event on this fd.  You can
override this in your poll_queue_proc, but the poll() and epoll() queue
procs both have this interpretation.

Unfortunately, this is not true for waitfds, which wait on the the
wait_chldexit waitqueue, whose key is a pointer to the task_struct of
the task being killed.  We can't do anything with this key, but we
certainly don't want the poll machinery treating it as a bitmask and
checking it against poll events!

So we introduce a new poll_wait() analogue, poll_wait_fixed().  This is used
for poll_wait() calls which know they must wait on waitqueues whose keys are
not a typecast representation of poll events, and passes in an extra
argument to the poll_queue_proc, which if nonzero is the event which a
wakeup on this waitqueue should be considered as equivalent to.  The
poll_queue_proc can then skip adding entirely if that fixed event is not
included in the set to be caught by this poll().

We also add a new poll_table_entry.fixed_key.  The poll_queue_proc can
record the fixed key it is passed in here, and reuse it at wakeup time to
track that a nonzero fixed key was passed in to poll_wait_fixed() and that
the key should be ignored in preference to fixed_key.

With this in place, you can say, e.g. (as waitfd does)

        poll_wait_fixed(file, &current->signal->wait_chldexit, wait,
                POLLIN);

and the key passed to wakeups on the wait_chldexit waitqueue will be
ignored: the fd will always be treated as having raised POLLIN, waking
up poll()s and epoll()s that have specified that event.  (Obviously, a
poll function that calls this should return the same value from the poll
function as was passed to poll_wait_fixed(), or, as usual, zero if this
was a spurious wakeup.)

I do not like this scheme: it's sufficiently arcane that I had to go
back to my old commit messages to figure out what it was doing and
why.  But I don't see another way to cause poll() to return on
appropriate activity on waitqueues that do not actually correspond to
files.  (I do wonder how signalfd works.  It doesn't seem to need any of
this and I don't understand why not.  I would be overjoyed to remove the
whole invasive poll_wait_fixed() mess, but I'm not sure what to replace
it with.)

Orabug: 29891866
Signed-off-by: Nick Alcock <nick.alcock@oracle.com>
Signed-off-by: Kris Van Hees <kris.van.hees@oracle.com>
Signed-off-by: Tomas Jedlicka <tomas.jedlicka@oracle.com>
Signed-off-by: Eugene Loh <eugene.loh@oracle.com>
Signed-off-by: David Mc Lean <david.mclean@oracle.com>
Signed-off-by: Vincent Lim <vincent.lim@oracle.com>
Reviewed-by: Nick Alcock <nick.alcock@oracle.com>

---
## [33bca/android_kernel_oneplus_sm8250](https://github.com/33bca/android_kernel_oneplus_sm8250)@[ed22d194e0...](https://github.com/33bca/android_kernel_oneplus_sm8250/commit/ed22d194e0dc66dfa883d16f82ef9fd72e4d5a2c)
#### Monday 2022-02-07 20:09:40 by alk3pInjection

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
## [mathieures/ants_simulator](https://github.com/mathieures/ants_simulator)@[a67b7eac95...](https://github.com/mathieures/ants_simulator/commit/a67b7eac95385cda431e5c12111ce17572b78be6)
#### Monday 2022-02-07 20:13:44 by mathieures

Done many things. Some are still broken, but the Undo feature works now.
Launching the script:
  - The Server has to be started with `python3 main.py server`, better in my opinion than having to know the path of Server.py (launching the Client may change too in the future)

Server-Client communication (mostly in the networks/newtork_utils.py file):
  - Added classes "*Signal" and "*Info" to tell the Clients certain events happened: GoSignal, AdminSignal, DestroySignal, FirstBloodSignal, ColorInfo, AntsInfo, MoveInfo, PheromoneInfo
  - Added classes "*Request" to ask the Server certain things: SpeedRequest, UndoRequest
  - Added class ReadyState to inform the Server a Client is ready
  - Added class SentObject to sent the new objects' data to the Clients
  => Overall, improvement of Server.py and Client.py

Simulation:
  - AntServer's are now more independent, and the Simulation doesn't call as many methods as before. Renaming the methods with an underscore might be done in the future.
  - The "first ant" is now called "first blood"
  - Improved _is_good_spot() : now takes the size into account (I don't know how it was supposed to be working before)
  - A WallServer is now are a single object with all its coordinates, not a bunch of tuples. The zone is now correctly initialized.
  - Pheromones should be darkened more consistently.

Server-side objects:
  - ResourceServer and AntServer now have proper id generators
  - SizedServerObject._init_zone() is now called in SizedServerObject.__init__(), so that every instance has a zone and it isn't forgotten.

Other Server additions:
  - the class attribute `clients` (dict) now has an `id` key, to recognize Clients, and an id generator to produce said id's.

Interface:
  - The Undo feature now removes the objects only if the user is the same as the one who put them down
  - Moved the whole threading to the Client, which takes care of calling Interface's methods. No more create_pheromone_in_thread sub-function or other weird things.
  - Interface/Wall.py raises a ValueError when size is None, because I don't know why this test is here
  - easy_button.py an easy_menu.py are now TitleCased
  - As the list of all ants is now used by the Server, it has become a public attribute
  - Undoing doesn't destroy the last object directly anymore. The DestroySignal sent by the Server triggers it.

Known issues:
  - Server._sync_objects() does not work anymore for walls
  - Ants don't change color at the right times
  - Ants start to move in circles given enough time (I think it has to do with AntServer.is_tired)
  - Ants sometimes go through walls (it sort of always has been an issue though)

---
## [Dudemanguy/mpv](https://github.com/Dudemanguy/mpv)@[7c1ddc3a0a...](https://github.com/Dudemanguy/mpv/commit/7c1ddc3a0aab57d6ecfeac9ede6dcea495418987)
#### Monday 2022-02-07 20:19:20 by Dudemanguy

github/workflows: use lua 5.1 on macos

LuaJIT is still actively developed, but upstream is allergic to making
new releases for whatever reason. The last tagged release was in May of
2017, so we probably shouldn't expect a new release anytime soon. Now
for mpv, this doesn't really matter except in the case of macOS where
2.0.5 is actually a bit broken (and of course the CI uses luajit). More
specifically, the 2.0.5 pc is broken and has a "-pagezero_size 10000"
flag which causes libmpv to fail (only executables are allowed to use
this). This magically works on waf. It's possible that it just happens
to ignore the link arguments. However on the meson build, this is broken
and led to a really ugly hack using a partial dependency so both mpv and
libmpv succeed. Fortunately, the 2.1 luajit branch fixes this.
Unfortunately, there's no actual release.

Instead, just use Lua 5.1. Note that lua 5.1 is technically deprecated
in homebrew, but it's been that way for 10 years and probably won't go
away for another 10 years. This works fine and lets us get rid of a
terrible hack in the mesonbuild. People really shouldn't be using 2.0
LuaJIT anyway.

---
## [Dudemanguy/mpv](https://github.com/Dudemanguy/mpv)@[fb0d6d1e61...](https://github.com/Dudemanguy/mpv/commit/fb0d6d1e61f1782158bc62c4b515c4cd7f10044f)
#### Monday 2022-02-07 20:19:20 by Dudemanguy

meson: remove horrifying macos luajit hack

See the previous commit for the full explanation. Basically, luajit 2.0
has a bad pc file on macos that causes libmpv to fail during build. The
workaround was, if the os was darwin and luajit was found, to save a
full luajit dep and a partial luajit dep with the link args removed. The
partial dep was used for compiling libmpv, and the full dep was used for
the actual mpv executable. This worked and was needed for the CI to pass
but it sucked. Since the previous commit now makes the CI grab lua 5.1,
we don't need all this crap anymore. Just delete it and treat the
dependency normally.

This does effectively mean that building libmpv with luajit 2.0 on macOS
will no longer work with the meson build. However libraries not being
built correctly is not a mpv-specific issue. The waf build will succeed
for some reason, but it has known issues and it would be better if it
just failed honestly. An upstream developer said years ago that that
macOS users should use the 2.1 branch (and there's no release of
course). In any case, no macOS user should be building mpv with luajit
2.0, so we shouldn't be going out of our way to support this.

https://github.com/mpv-player/mpv/issues/7512
https://github.com/LuaJIT/LuaJIT/issues/521#issuecomment-562999247

---
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[734368a200...](https://github.com/rust-lang-ci/rust/commit/734368a200904ef9c21db86c595dc04263c87be0)
#### Monday 2022-02-07 20:33:14 by bors

Auto merge of #87869 - thomcc:skinny-io-error, r=yaahc

Make io::Error use 64 bits on targets with 64 bit pointers.

I've wanted this for a long time, but didn't see a good way to do it without having extra allocation. When looking at it yesterday, it was more clear what to do for some reason.

This approach avoids any additional allocations, and reduces the size by half (8 bytes, down from 16). AFAICT it doesn't come additional runtime cost, and the compiler seems to do a better job with code using it.

Additionally, this `io::Error` has a niche (still), so `io::Result<()>` is *also* 64 bits (8 bytes, down from 16), and `io::Result<usize>` (used for lots of io trait functions) is 2x64 bits (16 bytes, down from 24 — this means on x86_64 it can use the nice rax/rdx 2-reg struct return). More generally, it shaves a whole 64 bit integer register off of the size of basically any `io::Result<()>`.

(For clarity: Improving `io::Result` (rather than io::Error) was most of the motivation for this)

On 32 bit (or other non-64bit) targets we still use something equivalent the old repr — I don't think think there's improving it, since one of the fields it stores is a `i32`, so we can't get below that, and it's already about as close as we can get to it.

---

### Isn't Pointer Tagging Dodgy?

The details of the layout, and why its implemented the way it is, are explained in the header comment of library/std/src/io/error/repr_bitpacked.rs. There's probably more details than there need to be, but I didn't trim it down that much, since there's a lot of stuff I did deliberately, that might have not seemed that way.

There's actually only one variant holding a pointer which gets tagged. This one is the (holder for the) user-provided error.

I believe the scheme used to tag it is not UB, and that it preserves pointer provenance (even though often pointer tagging does not) because the tagging operation is just `core::ptr::add`, and untagging is `core::ptr::sub`. The result of both operations lands inside the original allocation, so it would follow the safety contract of `core::ptr::{add,sub}`.

The other pointer this had to encode is not tagged — or rather, the tagged repr is equivalent to untagged (it's tagged with 0b00, and has >=4b alignment, so we can reuse the bottom bits). And the other variants we encode are just integers, which (which can be untagged using bitwise operations without worry — they're integers).

CC `@RalfJung` for the stuff in repr_bitpacked.rs, as my comments are informed by a lot of the UCG work, but it's possible I missed something or got it wrong (even if the implementation is okay, there are parts of the header comment that says things like "We can't do $x" which could be false).

---

### Why So Many Changes?

The repr change was mostly internal, but changed one widely used API: I had to switch how `io::Error::new_const` works.

This required switching `io::Error::new_const` to take the full message data (including the kind) as a `&'static`, rather than just the string. This would have been really tedious, but I made a macro that made it much simpler, but it was a wide change since `io::Error::new_const` is used everywhere.

This included changing files for a lot of targets I don't have easy access to (SGX? Haiku? Windows? Who has heard of these things), so I expect there to be spottiness in CI initially, unless luck is on my side.

Anyway this large only tangentially-related change is all in the first commit (although that commit also pulls the previous repr out into its own file), whereas the packing stuff is all in commit 2.

---

P.S. I haven't looked at all of this since writing it, and will do a pass over it again later, sorry for any obvious typos or w/e. I also definitely repeat myself in comments and such.

(It probably could use more tests too. I did some basic testing, and made it so we `debug_assert!` in cases the decode isn't what we encoded, but I don't know the degree which I can assume libstd's testing of IO would exercise this. That is: it wouldn't be surprising to me if libstds IO testing were minimal, especially around error cases, although I have no idea).

---
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[af8b11ecc2...](https://github.com/Perkedel/Kaded-fnf-mods/commit/af8b11ecc2f35470627034d014eb27eb5f2bfdc7)
#### Monday 2022-02-07 20:45:03 by Joel Robert Justiawan

[skip ci] sorry for any

I just birthday 7 feb yeay. no big party for obvious reason tho. just cakes, nasi tumpeng (stack rice) and serveral random gifts. tbh it's lottery and lose (I should've given my parents my shopping carts & wishlists), get prize like this. okay screw it, no judgement because that'll considered bringing curse. So I accept the gift anyway. who knows this terrible V8 Singing Live soundboard https://www.youtube.com/watch?v=82eUX8K2s6g no professional wants be handy one day. as well as wild off brand neck massager, battery powered desk lamp, and that's it. Unfortunately importing csnoobs.com toy wepon ended up being expensive https://shopee.co.id/search?keyword=csnoobs https://shopee.co.id/search?keyword=shell%20ejection . yeah obviously that'll cause gifter to think thrice beforehand which often ended up nvm, other gifts pls.

attempt NFO copy of it to enhance the presense of Admiral Zumi. NFO is typical readme for Warez Sparsdats

---
## [fazulk/barfzz](https://github.com/fazulk/barfzz)@[301a97d7c5...](https://github.com/fazulk/barfzz/commit/301a97d7c57de6c2eb2c8462e03586768a52813f)
#### Monday 2022-02-07 20:46:14 by Jeff Fasulkey

Merge pull request #161 from fazulk/hotfix/fuck-you

hotfix/2022-02-07

---
## [jkcarney/pyre-emblem-7](https://github.com/jkcarney/pyre-emblem-7)@[a499333960...](https://github.com/jkcarney/pyre-emblem-7/commit/a4993339606e9a3a8d87f87c0e0199f75894817d)
#### Monday 2022-02-07 21:02:24 by Joshua Carney

added all the freakin tile move thing oh my god i want to die hply sjyo thanks Sam

---
## [patxxi/nvim](https://github.com/patxxi/nvim)@[7851fc7a6a...](https://github.com/patxxi/nvim/commit/7851fc7a6a3797b530b4125e5225d89f82553d7d)
#### Monday 2022-02-07 21:21:38 by Francisco Ruiz

last update. Shame on me, i swape to VsCode cuz im a fucking pussy. Sorry mother, sorry sister, fuck u Chachati

---
## [netik/dc28_badge](https://github.com/netik/dc28_badge)@[06e84dff07...](https://github.com/netik/dc28_badge/commit/06e84dff074d8fb746ca92708fb80cb9b0da93ff)
#### Monday 2022-02-07 23:42:43 by Bill Paul

Fix yet another 25 year old Doom bug.

Doom has special code for handling switches that the player presses
in-game (to open doors, activate lifts, etc...). There are apparently
hard-coded lists of switches which vary depending on which game
you're playing. There are several cases to handle depending on the
PWAD that's used:

doom1.wad - shareware wad
doom.wad - registered wad (all 3 original episodes)
doomu.wad - Ultimate Doom anniversary edition (3 original episodes + bonus episode)
doom2.wad - Doom II: Hell On Earth
plutonia.wad - The Plutonia Experiment
tnt.wad - TNT Evilution

Each of these has a gamemode associated with. The p_switch.c code handles
all gamemode values -- except for the one for doomu.wad, which is 'retail.'
It should treat it the same as the 'registered' case (doom.wad) but instead
it gets left at the default, which is shareware.

The end result is that when you play the Ultimate Doom WAD, the player
can activate switches, but their textures never change and no sound is
played for them.

We fix this by treating the registered and retail episodes the same.

---

