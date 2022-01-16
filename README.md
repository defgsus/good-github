## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-01-15](docs/good-messages/2022/2022-01-15.md)


1,332,826 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,332,826 were push events containing 1,877,049 commit messages that amount to 120,375,132 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 25 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[7bead07444...](https://github.com/tgstation/tgstation/commit/7bead0744491b9beb91689d34ac12d142aca5b31)
#### Saturday 2022-01-15 00:02:01 by John Willard

General pAI code improvements (#63688)

Fikou said they would've made MODsuits be controllable by pAI's rather than AI's, if pAI code wasn't as bad.

But pAI code ISN'T AS BAD AS AI CODE LIKE HOLY SHIT WHAT THE FUCK MAN???

Anyways, this is just general code improvements for pAIs that I thought would be nice to have.

Documents previously undocumented vars
Moves loose vars to be where they should be
Removes single-letter variables
Makes pAI a defined job
Moves vars around to where they should be while removing unused ones.
Makes pAI abilities its own .dm file
Replaces var/silent with Stun() (like cyborgs)
Reworks pAI's doorjack to not have a ton of procs, copy paste, and a reliance on Life(), instead it just uses a do_after()
Moves screwdrivering radios from attackby to screwdriver_act

Just general code improvement for Silicon, the thing no one likes or wants to touch.

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[17b9b9a483...](https://github.com/cyberitsolutions/bootstrap2020/commit/17b9b9a4832d699b639b1a112075553a2186c7a8)
#### Saturday 2022-01-15 00:27:51 by Trent W. Buck

what-is-my-ip: go back to xdg autostart

Without xfce being properly systemd integrated (no graphical-session-pre.target &c),
I cannot see how to ensure systemd starts what-is-my-ip AFTER /etc/X11/Xsession has told systemd what the DISPLAY and XAUTHORITY are.
Without this, what-is-my-ip will start too early, crash, and that is the end of it.

I could have used a .timer with something like OnActiveSec=10, so it just starts the .service 10s after login.
That is a shitty hack and -- for now -- xdg autostart is a less-shitty hack.

I hate this.

---
## [GesuBackups/tgstation](https://github.com/GesuBackups/tgstation)@[a2fa7799f3...](https://github.com/GesuBackups/tgstation/commit/a2fa7799f3f27025b43413314c34f595f4316cac)
#### Saturday 2022-01-15 00:49:20 by Jeremiah

Removes swarmers from the game (#63989)

What the title says. But why?
I generally have a rule when making a contribution, that is "don't make the game less fun"
I'm not salting, I didn't die to a swarmer.
... Yet that's the problem. Swarmers are the griefiest antag in the game, but when you complain that they're annoying or unfun, you're doomed to hear "lol they can't even hurt you though."

WELL THAT ACTUALLY MAKES THEM WORSE. I would rather die to a hundred xenos and space dragons than be forced to untie myself in maintenance for 45 seconds while the shuttle leaves.
Why It's Good For The Game

Unfun game modes should be removed from the game.

    Being griefed by swarmers is annoying
    Playing as a swarmer is not very exciting either. Click on iron.

lastly, because oranges authorized it
Changelog

cl
del: Removes swarmers! The griefiest, lowest fun value antagonist is removed from the game.
/cl

---
## [botovq/ports](https://github.com/botovq/ports)@[b1bd329b8d...](https://github.com/botovq/ports/commit/b1bd329b8de5cf8ad30c1c58ad048622676a600f)
#### Saturday 2022-01-15 02:31:10 by tb

databases/mariadb: Fix build with opaque EVP_MD_CTX and EVP_CIPHER_CTX.

A mariadb developer didn't like the fact that these structs need to be
allocated in OpenSSL 1.1 and added some insane hacks to work around
this. Adjust the code to cope with that the same way as it is done for
OpenSSL.

LibreSSL doesn't provide the means to override malloc and friends, so
the runtime check cannot be adapted. Use generous estimates for the
sizes for these structs instead.

With opaque EVP_CIPHER_CTX, EVP_CIPHER_CTX_buf_noconst() needs to be
provided by libcrypto, so disable this and a few other API redefinitions.

---
## [Texera/texera](https://github.com/Texera/texera)@[c3af4463f4...](https://github.com/Texera/texera/commit/c3af4463f486c9cf001cb547b29b6189a3c8302f)
#### Saturday 2022-01-15 02:44:42 by Albert Liu

Add PresetService (User Presets Step 3) (#1164)

Final feature demo:

![Kapture 2022-01-13 at 23 36 00](https://user-images.githubusercontent.com/12578068/149469927-b62bfa43-4701-4498-a489-565aea36da2c.gif)

---------------------------

This PR is extracted from #1041 as step 2 of the User Preset feature.

rebase of picked commits pertaining to PresetServiceService onto Albert-UserDictionaryService

PresetService provides the ability to save and "apply" collections of settings (represented by objects) that a user might find convenient to save and apply as a group. These groups are called Presets.

PresetService uses DictionaryService to store presets (it creates kind of a *view* in the database sense, of the user dictionary, that only includes Presets)

Changes from last review (for Yicong)
 - Code comments
 - fixed subscription memory leak by using takeUntil(observable), where said observable completes on NgOndestroy
 - DictionaryService now attempts to init whenever client logs in (sorry, you'll have to re-review my changes to DictionaryService)
 - PresetService now has public ready promise/value member 
   - This indicates that its init isn't complete until DictionaryService's init is complete (which is async, and cant be awaited in the constructor)
 - DeletePreset now built into PresetService (don't know why I ever didn't have that)
 - Revert Changes to Styles.scss to fix Karma test runner interface (I originally changed them as a workaround for an ng-zorro component that's no longer used)

 Note: for this step, I had less time and more complex code to test. I'm not sure I caught all the bugs, but it passes unit tests.
The quality of the code in this pr is lesser, in my opinion, so You'll have to be a little more careful on my behalf.



Co-authored-by: Zuozhi Wang <zuozhiw@gmail.com>
Co-authored-by: Yicong Huang <17627829+Yicong-Huang@users.noreply.github.com>

---
## [yadij/squid](https://github.com/yadij/squid)@[2b6b1bcb86...](https://github.com/yadij/squid/commit/2b6b1bcb8650095c99a1916f5964305484af7ef0)
#### Saturday 2022-01-15 05:02:13 by Alex Rousskov

Bug 5055: FATAL FwdState::noteDestinationsEnd exception: opening (#877)

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
pointers or in-job connections were left stale/set after forwarding
failures. The changes described below addressed most of those problems.


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
would only be a matter of time before the next bug bites us due to stale
Connection::fd and such. These changes themselves carry elevated risk,
but they get us closer to reliable code as far as Connection maintenance
is concerned. Without them, we will keep chasing deadly side effects of
poorly implemented closure callbacks.

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

Probably fixed a bug where PeerConnector::negotiate() assumed that
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

---
## [clarencelol/kernel_xiaomi_sdm660-4.19](https://github.com/clarencelol/kernel_xiaomi_sdm660-4.19)@[b491752c60...](https://github.com/clarencelol/kernel_xiaomi_sdm660-4.19/commit/b491752c60eea744670a5c6527d7954a6147d992)
#### Saturday 2022-01-15 05:06:22 by Joonsoo Kim

mm/page_alloc: use ac->high_zoneidx for classzone_idx

Patch series "integrate classzone_idx and high_zoneidx", v5.

This patchset is followup of the problem reported and discussed two years
ago [1, 2].  The problem this patchset solves is related to the
classzone_idx on the NUMA system.  It causes a problem when the lowmem
reserve protection exists for some zones on a node that do not exist on
other nodes.

This problem was reported two years ago, and, at that time, the solution
got general agreements [2].  But it was not upstreamed.

[1]: http://lkml.kernel.org/r/20180102063528.GG30397@yexl-desktop
[2]: http://lkml.kernel.org/r/1525408246-14768-1-git-send-email-iamjoonsoo.kim@lge.com

This patch (of 2):

Currently, we use classzone_idx to calculate lowmem reserve proetection
for an allocation request.  This classzone_idx causes a problem on NUMA
systems when the lowmem reserve protection exists for some zones on a node
that do not exist on other nodes.

Before further explanation, I should first clarify how to compute the
classzone_idx and the high_zoneidx.

- ac->high_zoneidx is computed via the arcane gfp_zone(gfp_mask) and
  represents the index of the highest zone the allocation can use

- classzone_idx was supposed to be the index of the highest zone on the
  local node that the allocation can use, that is actually available in
  the system

Think about following example.  Node 0 has 4 populated zone,
DMA/DMA32/NORMAL/MOVABLE.  Node 1 has 1 populated zone, NORMAL.  Some
zones, such as MOVABLE, doesn't exist on node 1 and this makes following
difference.

Assume that there is an allocation request whose gfp_zone(gfp_mask) is the
zone, MOVABLE.  Then, it's high_zoneidx is 3.  If this allocation is
initiated on node 0, it's classzone_idx is 3 since actually
available/usable zone on local (node 0) is MOVABLE.  If this allocation is
initiated on node 1, it's classzone_idx is 2 since actually
available/usable zone on local (node 1) is NORMAL.

You can see that classzone_idx of the allocation request are different
according to their starting node, even if their high_zoneidx is the same.

Think more about these two allocation requests.  If they are processed on
local, there is no problem.  However, if allocation is initiated on node 1
are processed on remote, in this example, at the NORMAL zone on node 0,
due to memory shortage, problem occurs.  Their different classzone_idx
leads to different lowmem reserve and then different min watermark.  See
the following example.

root@ubuntu:/sys/devices/system/memory# cat /proc/zoneinfo
Node 0, zone      DMA
  per-node stats
...
  pages free     3965
        min      5
        low      8
        high     11
        spanned  4095
        present  3998
        managed  3977
        protection: (0, 2961, 4928, 5440)
...
Node 0, zone    DMA32
  pages free     757955
        min      1129
        low      1887
        high     2645
        spanned  1044480
        present  782303
        managed  758116
        protection: (0, 0, 1967, 2479)
...
Node 0, zone   Normal
  pages free     459806
        min      750
        low      1253
        high     1756
        spanned  524288
        present  524288
        managed  503620
        protection: (0, 0, 0, 4096)
...
Node 0, zone  Movable
  pages free     130759
        min      195
        low      326
        high     457
        spanned  1966079
        present  131072
        managed  131072
        protection: (0, 0, 0, 0)
...
Node 1, zone      DMA
  pages free     0
        min      0
        low      0
        high     0
        spanned  0
        present  0
        managed  0
        protection: (0, 0, 1006, 1006)
Node 1, zone    DMA32
  pages free     0
        min      0
        low      0
        high     0
        spanned  0
        present  0
        managed  0
        protection: (0, 0, 1006, 1006)
Node 1, zone   Normal
  per-node stats
...
  pages free     233277
        min      383
        low      640
        high     897
        spanned  262144
        present  262144
        managed  257744
        protection: (0, 0, 0, 0)
...
Node 1, zone  Movable
  pages free     0
        min      0
        low      0
        high     0
        spanned  262144
        present  0
        managed  0
        protection: (0, 0, 0, 0)

- static min watermark for the NORMAL zone on node 0 is 750.

- lowmem reserve for the request with classzone idx 3 at the NORMAL on
  node 0 is 4096.

- lowmem reserve for the request with classzone idx 2 at the NORMAL on
  node 0 is 0.

So, overall min watermark is:
allocation initiated on node 0 (classzone_idx 3): 750 + 4096 = 4846
allocation initiated on node 1 (classzone_idx 2): 750 + 0 = 750

Allocation initiated on node 1 will have some precedence than allocation
initiated on node 0 because min watermark of the former allocation is
lower than the other.  So, allocation initiated on node 1 could succeed on
node 0 when allocation initiated on node 0 could not, and, this could
cause too many numa_miss allocation.  Then, performance could be
downgraded.

Recently, there was a regression report about this problem on CMA patches
since CMA memory are placed in ZONE_MOVABLE by those patches.  I checked
that problem is disappeared with this fix that uses high_zoneidx for
classzone_idx.

http://lkml.kernel.org/r/20180102063528.GG30397@yexl-desktop

Using high_zoneidx for classzone_idx is more consistent way than previous
approach because system's memory layout doesn't affect anything to it.
With this patch, both classzone_idx on above example will be 3 so will
have the same min watermark.

allocation initiated on node 0: 750 + 4096 = 4846
allocation initiated on node 1: 750 + 4096 = 4846

One could wonder if there is a side effect that allocation initiated on
node 1 will use higher bar when allocation is handled on local since
classzone_idx could be higher than before.  It will not happen because the
zone without managed page doesn't contributes lowmem_reserve at all.

Reported-by: Ye Xiaolong <xiaolong.ye@intel.com>
Signed-off-by: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Tested-by: Ye Xiaolong <xiaolong.ye@intel.com>
Reviewed-by: Baoquan He <bhe@redhat.com>
Acked-by: Vlastimil Babka <vbabka@suse.cz>
Acked-by: David Rientjes <rientjes@google.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Michal Hocko <mhocko@kernel.org>
Cc: Minchan Kim <minchan@kernel.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Link: http://lkml.kernel.org/r/1587095923-7515-1-git-send-email-iamjoonsoo.kim@lge.com
Link: http://lkml.kernel.org/r/1587095923-7515-2-git-send-email-iamjoonsoo.kim@lge.com
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: Carlos Jimenez (JavaShin-X) <javashin1986@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>

---
## [ytmous/ytmous](https://github.com/ytmous/ytmous)@[f6b81a9933...](https://github.com/ytmous/ytmous/commit/f6b81a9933c411dd05fc375eccee75947eb8d4ca)
#### Saturday 2022-01-15 06:35:19 by Yonle

Final commit.

After 6 - 10 months of no updates, It's time to deprecate this project. Even though i see somebody open a issue during a day that does not has update, still i respond to them.

I really had no idea of what am i doing after the past 6 months. Seriously, I'M LAZY AS HECK! You see, 3-5 Planned features that were planned since 6 MONTHS AGO IS NEVER IMPLEMENTED FOR THE PAST 6 MONTHS!

Every hours i'm busy and selling some stuff in my shop. Which can also the reason why i can't maintain this repository longer. You can also say that i can't maintain this repo longer due to life issue. I'm busy, tho. Scrolling through Telegram, Twitter, and Mastodon everytime when i'm bored and had no idea of what to do.

Believe me or no, The frontend code (Right in views folder) is mostly a copy paste result in Bootstrap example. Unbelieveable, Isn't it? This project also my random-bored project that i made when i had no idea of what am i doing in some hours.

So yeah. I think this is the end, But not the end. Since the code is open, Somebody may fork it and improve this project with their own.

Thanks for the 36 starts on github. I really appreciate it.

That's it. See you next time, folks.

Bye.

- Yonle <yonle@duck.com>
  Sat, 15 Jan 2022 06:32:25 GMT

---
## [Moffein/SniperClassic](https://github.com/Moffein/SniperClassic)@[24f97410c9...](https://github.com/Moffein/SniperClassic/commit/24f97410c9d3cb9a177e955d4a9e76d6768a5e7e)
#### Saturday 2022-01-15 06:55:08 by TheTimeSweeper

holy shit it's like pitch and yaw aiming is actually fucking possible wow

---
## [KathrinBailey/horizon](https://github.com/KathrinBailey/horizon)@[caa02fc774...](https://github.com/KathrinBailey/horizon/commit/caa02fc774d4ba7441e3cabb25ccdab6da12327f)
#### Saturday 2022-01-15 07:07:01 by Zytolg

Beds and Benches: The Aesthetic Revolution [re-PR'd With EOB's Blessing] (#62169)

About The Pull Request

Ever since I saw @EOBGames PR this, I've wanted it. I've needed it. I've been delaying some mapwork FOR this. This is an identical PR to #61689, just updated so that it's not conflicting with anything. I've done everything @Krysonism asked for from last time too. That's right spacemen, double beds are back, and more cursed then ever. Cursed to succeed that is!
Why It's Good For The Game

We. Don't. Have. Benches.
Benches are a hallmark of any public space! You can sit on them, sleep on them, stand on them, even sleep on them! Our stations have a ton of chairs, but chairs don't really communicate public that well. Benches do. As for the beds? Well Inept wants them, and you know what? I respect that.

cl
expansion: Sofas now include the Bench Type. These are buildable with 2 metal plates from the crafting menu.
expansion: Beds can now be rotated (flipped), and include the Double Bed Type. Miners can also make Double Pod Beds to really feel like an Alaskan King.
expansion: Bedsheets to match! Try to share those big blankets with a lizard if you see that they're shivering!
code: Stuff that lets you interact with the benches and beds in-game, so that you too can enjoy being a king.
sprites: Ports the Benches and Double Bed sprites from Skyrat
sprites: Flipped Beds

---
## [pseudoname23/bigrat.monster](https://github.com/pseudoname23/bigrat.monster)@[c445fc2afa...](https://github.com/pseudoname23/bigrat.monster/commit/c445fc2afabcf49f0e5d2b69b581b886d0d20ba9)
#### Saturday 2022-01-15 07:42:57 by pseudoname

Remove incoherent rant

This motherfucker seriously tried to claim that an ESOLANG is the best language. And he talked shit about TypeScript. TYPESCRIPT. You're done.

---
## [dimbage/COVID-19-Kz-2022](https://github.com/dimbage/COVID-19-Kz-2022)@[9060136707...](https://github.com/dimbage/COVID-19-Kz-2022/commit/90601367072469bbc307650617c0b5be48caa0df)
#### Saturday 2022-01-15 13:20:46 by Dmitriy Babenko

Add files via upload

Sputnik-V reactogenicity and post-vaccination immunologic responses in the blood and nasal mucosa: a prospective cohort study in Kazakhstan.
Sergey Yegorov1,2^, Irina Kadyrova3^, Baurzhan Negmetzhanov2,4, Yevgeniya Kolesnikova3, 
Svetlana Kolesnichenko3, Ilya Korshukov3, Yeldar Baiken2,4,5, Bakhyt Matkarimov4, Matthew S. Miller1, Gonzalo Hortelano2, Dmitriy Babenko3. 

1 Michael G. DeGroote Institute for Infectious Disease Research; McMaster Immunology Research Centre; Department of Biochemistry and Biomedical Sciences, McMaster University, Hamilton, ON, Canada.
2 School of Sciences and Humanities, Nazarbayev University, 53 Kabanbay Batyr Ave, Nur-Sultan, 010000, Republic of Kazakhstan.
3 Research Centre, Karaganda Medical University, 40 Gogol St, Karaganda, 100008 Kazakhstan
4 National Laboratory Astana, Centre for Life Sciences, Nazarbayev University, 53 Kabanbay Batyr Ave, Nur-Sultan, 010000, Republic of Kazakhstan.
5 School of Engineering and Digital Sciences, Nazarbayev University, Nur-Sultan, Kazakhstan.

* Corresponding authors’ contact emails and phones: 
yegorovs@mcmaster.ca, +1(431)277-2571 (SY)
ikadyrova@qmu.kz, +77015033730 (IK)

Key words: COVID-19; SARS-CoV-2; Sputnik-V; vaccination; Central Asia; Kazakhstan.

Abstract
Background: Sputnik-V (Gam-COVID-Vac) is a heterologous, recombinant adenoviral (rAdv) vector-based, COVID-19 vaccine now used in >70 countries, yet there is a shortage of data on this vaccine's performance in diverse populations. Here, we did a prospective cohort study to assess the reactogenicity and immunologic outcomes of Sputnik-V vaccination in a multi-ethnic cohort from Kazakhstan.
Methods: COVID-19-free participants (n=82 at baseline) were followed at Day 21 after Sputnik-V Dose 1’ (rAd5) and Dose 2’ (rAd26). Self-reported local and systemic adverse events were captured using questionnaires. Blood and nasopharyngeal swabs were collected to perform SARS-CoV-2 diagnostic and immunologic assays.  
Results: Of the 73 and 70 participants retained post-Dose 1’ and 2’, respectively, most (>50%) reported an injection site or a systemic reaction to vaccination; no serious conditions were reported. Dose 1' appeared to be more reactogenic than Dose 2’, with fatigue and headache more frequent in participants with prior COVID-19 exposure; after Dose 2' nausea was more common in subjects without prior COVID-19. The combined S-IgG and S-IgA seroconversion rate was 97% post-Dose 1', remaining the same post-Dose 2'. The detectable virus neutralization rate was 83% post-Dose 1', further increasing to 98% post-Dose 2', with the largest increase seen in participants without prior COVID-19 exposure. Nasal S-IgG and S-IgA increased post- Dose 1', while the boosting effect of Dose 2’ on mucosal S-IgG, but not S-IgA, was only seen in subjects without prior COVID-19. Systemically, vaccination reduced growth regulated oncogene (GRO) levels, which correlated with blood platelet count elevation. 
Conclusion: Sputnik-V Dose 1' elicited both blood and mucosal SARS-CoV-2 immunity, while the immune boosting effect of Dose 2' was minimal, suggesting that adjustments to the current prime-boost vaccination regimen may be necessary to optimize immunization efficacy. Although Sputnik-V appears to have a reactogenicity profile similar to that of other COVID-19 vaccines, the observed alterations to the GRO/platelet axis call for further investigation of Sputnik V effects on systemic immunology.

---
## [Kapu1178/Skyrat-tg](https://github.com/Kapu1178/Skyrat-tg)@[5e9ecaf345...](https://github.com/Kapu1178/Skyrat-tg/commit/5e9ecaf345a34990bbc1cc32c8bba53841134c3d)
#### Saturday 2022-01-15 14:53:03 by linnpap

[NON MODULAR] Teshari clothes (#10233)

* aaAAAAAAAAAAAAAAARRRRRRRRRRRRRRRRRHHHHHHHHHHHHHGGGGGGGGGGGGGGGGGGGGGGGGGAAAAAAAAAAAAAAHHHHHHHH

* FUCK YOUUUUUUUUUUUU

* ffsfffdfddfsfdsfd

* defines DEFINES DEFINES

* FUCK YOU

* muh documentation

(apparently this was painful, huh?)

---
## [drunkwinter/Simple-YouTube-Age-Restriction-Bypass](https://github.com/drunkwinter/Simple-YouTube-Age-Restriction-Bypass)@[0b9ce74230...](https://github.com/drunkwinter/Simple-YouTube-Age-Restriction-Bypass/commit/0b9ce7423094b9905337fc9cc9991dc506c1008d)
#### Saturday 2022-01-15 15:25:45 by Demirci K

[chore] remove eslint & husky (#96)

* [chore] remove eslint & husky

Currently both are a pain in the ass and hard to work with in terms of developer experience, they are more like a nuisance than a helper.

ESlint is hard to work with when unconfigured. We might add this back in later when we have enough time to write the config rules.

Husky is reasonable, but with Prettier it tends to change files which are not in the commit. Although this is solvable with `lint-staged`, the fact that your code looks different on the commit vs what you just wrote is annoying. Also the error/warning messages are a lap of text, with bunch of useless information and it also does not play nicely with a GUI based Git.

My proposal (#97) as an alternative is having CI testing on GitHub on each pull request, when it fails, the dev must manually run `npm run format`. At that point it is clear to the dev that transformation has happened to the original code and is able to review it.

* upgrade packages

---
## [1Password/1password-teams-open-source](https://github.com/1Password/1password-teams-open-source)@[913e64a066...](https://github.com/1Password/1password-teams-open-source/commit/913e64a06659f71ffaa3468919ddd44ef2c77283)
#### Saturday 2022-01-15 15:31:56 by Matthias Bussonnier

Add Jupyter as OnePassword users.A

## Your Project ##

#### 1Password Teams URL ####

https://jupyter.1password.com/home

#### Project Name ####

Jupyter

#### Short Description ####

The Jupyter Project is a project and community whose goal is to
"develop open-source software, open-standards, and services for
interactive computing across dozens of programming languages"

#### Project Age ####

7 Years old (created in 2015)

#### Number Of Core Contributors ####

Current Steering council is 17 members (as per
https://jupyter.org/about), the definition of core contributors is a bit
more fuzzy and there are likely a few dozen with all the repos we
manage.

#### Project Website ####

https://jupyter.org

#### Repository URL(s) ####

https://github.com/jupyter
https://github.com/jupyterhub
https://github.com/jupyterlab
https://github.com/ipython/

#### Latest Release URL(s) ####

https://pypi.org/project/jupyterlab/
https://pypi.org/project/notebook
https://pypi.org/project/ipython
https://pypi.org/project/ipykernel

#### License Type ####

BSD

#### License URL ####

https://github.com/jupyterlab/jupyterlab/blob/master/LICENSE

## A Bit About Yourself  ##

#### Name ####

Matthias Bussonnier

#### Email ####

bussonniermatthias@gmail.com

#### Project Role ####

Steering Council Member and Founder of the Jupyter Project since before
it's inception (2012), I'm currently trying to push a bit for better
security practices and credential managements.

#### Profile/Website ####

You can find some of my rambling on https://matthiasbussonnier.com/,
otherwise most of my activity is on github https://github.com/carreau
and on twitter (https://twitter.com/mbussonn)

#### Comments ####

I'm personally not a 1password users, but I heard good things, the
current solution seem to be a bit inadequate as there is a keepassc
credential file shared via dropbox which is super problematic.

My hope is to make it easier to share sensitive credentials to the core
security/admins, that is everything that does not support account
delegation. Currently the main struggle we have are with:
 - Hosting providers that do not support delegation.
 - Twitter (and indirectly via twitter: medium)
 - Some website like readthedocs,
 - the original credentials of some shared accounts (like Gmail, where
   folks are delegated but every now and then need access to them).

We'll likely also store there a few rarely access personal credential in
case of a catastrophe.

I hope that the group structure of 1password will help us to manage who
needs access to what (website/social-media/communication), but as stated
above I don't have much one-password experience.

Side personal note, I really appreciate your team putting out technical
blogs out, like the recent 1password for linux using rust.

Thanks,

---
## [FedTheCat/horizon](https://github.com/FedTheCat/horizon)@[db1f299865...](https://github.com/FedTheCat/horizon/commit/db1f2998657331873027feca14236ebb73dc02d0)
#### Saturday 2022-01-15 16:39:53 by Alex 'Avunia' Takiya

Removes hrzn/ dir; bye BST - hello FRETs (#674)

* Move emote code and sfx

Moves the emote code and sfx away from the hrzn/ directory
Also removes some obsolete or not needed vars and code paths.
Additionally, reworks screams to be keyed lists.

* Moves cargo crate code to core

* Removes hrzn/ dir, mods icspawn and more

Changes:
- Moves all files out of hrzn/ and removes the folder
- Moves the hrvfoxcat suit to its proper core file
- Adds & removes a few debug snowflake objects
- Renames Bluespace Techs to Fast Response Emergency Techs (FRET Agents)
- Adds quiet spawn-in and -out for IC-spawning
- Adds SM hallucination resistance to the debug glasses
- Renames the admin janni outfit and IDs to the FRET Agents
- Adjust admin outfit for FRET, adds Hardsuit FRET outfit
- Makes a few strings in observer.dm on the IC-spawn-in code macros

* Converts indentation from spaces to tabs

* Fix accidentally redefining proc for bag of holding

This is why its bad to do this sleep deprived

* Replace FRET clothing with tactical turtleneck for now

Also fix name by removing the fwd slash and putting the second name in
brackets instead

* Replace HoS with ablative trenchcoat for FRET outfit

* Fixes screaming emote

Holy balls fuck whoever worked on this shit before me

* Set return value for initialize of return_back to parent proc

---
## [safwan6363/my-files](https://github.com/safwan6363/my-files)@[c482b3a068...](https://github.com/safwan6363/my-files/commit/c482b3a06871f0e18661388b645aa77ee8a208fb)
#### Saturday 2022-01-15 17:40:42 by safwan6363

Holy hagu shit oh my god ok so many things change oh no oh no

---
## [Thaumatorium/bitvavo-api-upgraded](https://github.com/Thaumatorium/bitvavo-api-upgraded)@[efe4856fa4...](https://github.com/Thaumatorium/bitvavo-api-upgraded/commit/efe4856fa4cf4545259869f28db50ca03c88e59b)
#### Saturday 2022-01-15 17:53:18 by NostraDavid

remove rateLimitThread class; replaced with a simple `sleep()`

This stupid-ass class was being a pain in my ass, behind the scenes.

---
## [UMM-CSci-3601/3601-iteration-template](https://github.com/UMM-CSci-3601/3601-iteration-template)@[8716543574...](https://github.com/UMM-CSci-3601/3601-iteration-template/commit/8716543574b925fc6ff2b3112e101fddabecdf8c)
#### Saturday 2022-01-15 18:28:05 by Nic McPhee

Disable several Checkstyle checks

This disables several Checkstyle checks that are included in the Sun configuration. I like the spirit of these, but our experience is that these tend to confuse people more than help them. Also, the structure of the Java code in the project has become quite simple because the server library (e.g., Javalin) encapsulates the bulk of the design complexity, leaving us to just write code at the "leaves" of the design.

The disabled checks are:

   *  DesignForExtension: This only really makes sense if we're building a reasonably
         sophisticate OO library, and that kind of design really doesn't
         come up in this class, because the server library (e.g., Javalin)
         encapsulates all that design work, leaving us to just act around
         the "leaves" of the design.
   *  HideUtilityClassConstructor: If everything is static 
         in a class, then it shouldn't have
         an accessible constructor. This is both subtle and
         confusing, and not likely to come up much in the class,
         so we'll just leave it out.
   * FinalParameters: I really likes the *intent* of this rule,
         but it's really trying to use CheckStyle to fix
         a mistake in the design of Java. This just confuses
         students, and requires a ton of extra typing
         that probably doesn't buy folks much.

---
## [wanted2/wanted2.github.io](https://github.com/wanted2/wanted2.github.io)@[6ec84549df...](https://github.com/wanted2/wanted2.github.io/commit/6ec84549dfe5997fdf81a84f1ff52a46985cddab)
#### Saturday 2022-01-15 18:43:58 by wanted2

[1;36m"Success is a terrible thing and a wonderful thing. If you can enjoy it, it's wonderful. If it starts eating away at you, and they're waiting for more from me, or what can I do to top this, then you're in trouble. Just do what you love. That's all I want to do."[1;m
		[1;35m--Gene Wilder[1;m[0m

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[1f41d2b2a8...](https://github.com/willior/Action_RPG_1/commit/1f41d2b2a8aaf8d0876cabbb232aef4eb99fb713)
#### Saturday 2022-01-15 19:22:52 by willior

many fixes & adjustments

bugfix: if a Player were to be stunned while in the PICKUP state, their interaction wouldn't get re-enabled. this would also have been true for the ACTION (casting) state. now, when these states end, we re-enable interaction before checking for a stun node.
decreased overall movement speed of bats by 20%.
modified the Lv1. charge attack animation slightly. it feels beefier now.
removing references to the old Enemy script.
updated the level up function for other stats (noticed that incrementing speed was not increasing attack speed. this is fixed)
a note on speed: it is a very complicated stat. it is the foundation for all movement-related speed values as well as the base attack speed.
the speed_mod affects ONLY MOVEMENT-RELATED values. attack_speed_mod is its own, discrete multiplier.
the Haste status increases the speed_mod ONLY, which is why it doesn't increase attack speed. this is to make sure Haste is not an over-powered buff. there is a separate buff strictly for increasing attack speed.
now, i am working on how stats are saved and loaded. the problem is that when the save_dict gets saved to disk, its keys are automatically sorted alphebetically. so when we load, "health" gets set before "max_health", and "vitality" is set last. now, when we "Continue", health starts at 60, which is the default value.
the reason this is occurring is because "health" gets set first. you'd think this makes sense, but the health setter has built-in behaviour that clamps the value to max_health. and since max_health defaults to 60, health gets set as 60.
the previous dirty way of getting this to work was to make "reset stats" set health & max_health to 999. this way, when health gets set first when we load from disk, it doesn't get clamped.
the PlayerStats script is a spaghetti mess right now, unfortunately. set_health() gets called WAY too many times. the reason why is this:
when we set vitality, we set both health and max_health (probably unncecessary)
when we set max_health, we set health
and we obviously set health on setting health.
so, when we load, setting vitality sets health 3 times.
the "set_vitality" function might actually be useless, curiously enough: increment_vitality is what's run when we level, which sets both health and max_health, and accounts for the amount increased based on the value of vitality.
a thorough look and reorganization of the PlayerStats script is due.
also fixed an issue where if the player was loaded with less than "default" health (60), the health_bar would count down from 60. i seem to have fixed this issue by setting the default value of the health bar background to 0 - though honestly i'm not sure why this fixed the issue, since the health bar behaviour is based on both the health value it's currently set at and the value it receives.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[9a53a05f79...](https://github.com/mrakgr/The-Spiral-Language/commit/9a53a05f79954278c01f7a773c2d4f1da87bf6d6)
#### Saturday 2022-01-15 19:38:51 by Marko Grdinić

"11:40am. I did stop the gaming session earlier, but I did not succeed in going to bed particularly earlier.

But I am starting to get more focused on the path at hand.

11:45am. It does not matter if I get rich. What matters is that the path be sustainable on its own. I do not have to make a lot of money, but I need more than 0/month of the past 15 years.

12pm. Let me finish chilling and then I'll do the chores and have breakfast. Then I will start.

1:50pm. Done with breakfast. Let me start. Let me just check if scaling a control points of a NURBS curve changes its W value.

Nope.

Now let me do some talking. The rip thing was declared a bug. But the scale thing he says might be a feature request. Let me reply to that.

https://developer.blender.org/T94884

>> It would have been more useful if it used the median point for each isolated spline instead

> Hi, Thanks for the report. You can do this by selecting adjacent control points, no?
> Not sure if I understood totally but this is more of a request than a bug.

I suppose, but when I ran into this limitation, it felt like a bug. What I was doing is ripping the duplicated far edges of building top and converting them to curves with the intention of using them to distribute fence segments on them. I needed to rescale them to make the segments not stick out on the corners and could not do it. Instead what I did was convert them back to a mesh in order to do the rescaling. If the conversion gave me Bezier curves instead I would have noticed the handles changing size, but as things are now there is no indication of why the scale tool is not working in that particular case. So I'd consider that aspect a bug.

There is a design issue at hand here.

If you want to stick to the current design as close as possible the Bezier curve behavior can remain as it is, but if so then for consistency the NURBS path scaling of individual control points should affect its W. Poly splines should be treated as regular mesh edges as far as scaling from individual origins is concerned.

Another design would be be to treat scaling of curve points much like regular mesh vertices, and move scaling of Bezier handles and NURBS Ws to another tool. I suggest mapping it to the D key since it seems to be free. This design would have the most predicable behavior for newcomers such as myself.

2:15pm. Let me go with this reply.

Now Reddit. Got this message.

> Why not send your resume and ideas directly to tenstorrent contacts?

Last year, I did send out emails to a bunch of people at various companies, including the TensTorrent CEO and I got no reply from any of them. You can see what the sentiment towards languages is in that ML sub thread I posted seeking a sponsor, it is borderline hostile. Sadly, nobody gives a crap about languages and I have zero idea how to catch the attention of those that I'd want to. I could probably convince the CEO if he would engage with me, but getting to that initial step is beyond me. It is a pity, since Spiral could significantly boost productivity at these companies. Ultimately, I can't hinge my whole future on a path that won't support me. I just can't bear the risk of going the next few years making 0$ a month. I'd rather give up ML research than bear that for any longer. What kept me going without pay for so long is that I believed that I could create a decent poker agent with existing techniques and use that to make money. If that worked, I could have used that to support my research.

But it is not enough, it was too much of a compromise. I guess the way to do ML research is to have the hardware be powerful enough and then tell you what the right algorithms are itself. That approach which involves implementing a genetic programming system is not something I'd be able to do on a NEET budget anyway. I am not sure that a single Grayskull chip would be enough for the inference attempt to succeed.

I could get a random programming job to support my ML research, but I feel disgust towards both that and my old path. Why do I have to try so hard for something that won't support my efforts on its own? Every normie thinks - 'I'll be a slave for a few years/decades, until I save up money to my own thing.' I feel a lot of contempt for that kind of thinking. Rather than live like that, I'd rather find something I want to do now and then just do it. It is not like there is some fixed thing you have to do in life.

2:35pm. Let me reply with this.

2:40pm. Now let me finally start.

2:40pm. Let me make the fence segment for the pool.

https://blender.stackexchange.com/questions/2976/how-can-i-add-vertices-to-intersection-of-two-edges

I should be sketching it in CSP, but I've decided to do it directly in Blender instead. Ahhh, so that is what split edges and faces is for!

3:20pm. This is pretty fun. This is the first time I've used the edge crease. It is quite useful for controling how aggressive the subdiv modifier is. It is actually possible to mark the edges with a scalar value.

Actually, this makes much more sense than using loop cuts for controling subdiv. What I learned in those tutorials is garbage.

The cool thing about what I've done just now is that I've never actually seen crease being used like this. Instead I simply wondered about controling subdiv, looked into the advanced options and saw that the use crease option is checked. Then I immediately put 2 and 2 together.

4:05pm. Did the fence thing. It took me a bit too long.

Right now, I am thinking what to do next?

Sigh, let me put the props in.

I should do everything one step at a time. I'll leave texturing and bump mapping for last.

Actually, now that I am thinking about it, just what is the difference between bump and displacement?

https://www.youtube.com/results?search_query=blender+bump+displacement

Let me watch this just for a bit.

https://youtu.be/_dU3DONwSzU?t=39
3 Most Popular Methods of using Height, Displacement or Bump Maps | Blender 2.8

He says that bump, height and displacement maps are the same thing.

https://youtu.be/_dU3DONwSzU?t=222

This looks really good. I do like displacement maps.

4:15pm. This was a really good 5m tutorial. 10/10. It answered all my questions about height maps.

Time for lunch. It seems to be early today.

4:40pm. I am back. Let me resume.

I need to figure out how displacement and normal maps interact. Why does the bump and displacement option exist if those two things are the same.

https://docs.blender.org/manual/en/latest/render/materials/components/displacement.html

4:45pm. Had to take a short break. Let me read the above. It seems to cover the ground in the video, but more in depth.

https://docs.blender.org/manual/en/latest/render/materials/components/displacement.html#displacement-and-bump
> Both methods can be combined to use actual displacement for the bigger displacement and bump for the finer details. This can provide a good balance to reduce memory usage.
> Once you subdivide the mesh very finely, it is better to use only actual displacement. Keeping bump maps will then only increase memory usage and slow down renders.

I see.

4:50pm. Now that I've learned this, let me move to the next step. I've been thinking about texturing, but I should resist the urge and just leave that for later. Let me fire up BlenderKit and put some props into the scene.

5:10pm. Moving things between collections is so annoying. It is super annoying to move the parent, but have the children stay put. The same goes for deletion spilling items. Couldn't this have been done more sensibly. I'd seriously consider an addon for this.

5:05pm. Got the bistro chair and table. Now I need some beach props.

5:15pm. I did not know it was possible to attach instance objects to hair. I am studying how the cherry tree was done and now I see how. The leaves and the smaller branches were done using the hair particle system.

I learned a bit, but stil the tree is only 6 stars and you can see why. The leaves themselves are poorly done.

...165mb. This spherical willow I am downloading should be something.

5:45pm. It looks nice, but not what I want.

https://www.cgtrader.com/free-3d-models/beach

This place has some 3d models.

https://sketchfab.com/3d-models/beach-chairs-6e9471ec602e4774836f5fe03a6bb780

I should have closed this as the stuff here is all paid material. No way can I afford any of this.

https://www.cgtrader.com/free-3d-models/exterior/house/sunbed-9f145e34-78b4-496b-8784-c469667f3cf0

I need to remember the word sunbed. Let me see if there is anything in BlenderKit.

6:15pm. Nope. I had to registed on CGTrader to get that free sunbed.

6:25pm. Why do the ends of the subded explode when I try to apply the scale. Sigh.

Given how simple its geomtry is I should have just done it on my own. It has some texturing applied on it, but this is nothing that would really be visible once I paint it.

DAmn it, the reason this is happening because I joined the two rests at the end to the same object to make them easier to deal with. But that probably messed up something. Or this might be some bug. Who knows.

6:30pm. A lot of the assets online are quite expensive. Imagine paying 40$ for a piece of art. Hell, just the game I am trying to make will go 10$ at some store.

Ok, enough of this. I am just wasting my time looking up online assets. If I can barely find a decent beach prop, there is no point in me trying to find the right tree.

The overhead tree I want does not exist in nature anyway. I'll have to sculpt it.

I've been imagining a tree with large leaves.

6:35pm. Ok, let me do it.

I've been happy doing the fence, but not so much looking for props.

Let me give it a try.

7:30pm. Let me take a break here. I am messing up the tree.

8pm. Where did the last 30m go?

At any rate, let me resume. I am going to model the tree.

I started off by using dyntopo and sculpting, but that was the wrong choice.

Trying out sculpting for the first time in a long while brought back some memories for me.

8:15pm. Right now the fatigue is hitting me, so let me just rant a bit.

You know that YanSculpts vidoe that I watched recently? He did make a fully fledged model in just 12m speed up by 5-10x. So 2h at most. It was painted and clothed as well.

I could not see it initially, but at my present level, I feel like Flycat's technique isn't quite all the way there.

Art is like programming - everything should be top to bottom, but Fly I think hasn't quite gotten that aspect of it down. He fiddles too much with the details and the verts.

Yan on the other hand did.

This is what I've been missing. I feel like I did a particularly good job on the fence segment.

I am still slow, but I am getting there.

8:25pm. I feel like I am having a crystalizing moment, today as well as in the recent days. It feels like pieces are falling into place, and I am finally realizing the important of fundamentals. I feel eager to practice them more.

To be honest, the way this pool scene has been going is different than how I thought it would go. I imagined myself using outside assets more, but now that I've looked for them again, they feel like a waste of time. I do not get the sense that they are even saving me that much time compared to doing it on my own.

From here on out, I am going to stop looking for them and just go at it.

9:25pm. I had some fun just playing around with placing branches, messing with the creases. Today was also the first time I tried out the multires modifier as well.

This is the way things should go. I need to start with modeling to set everything up. Then during the sculpting stage what I would be doing is essentially shading in 2d - fine, and high frequency detail that would involve manipulating groups of vertices.

These are two distinct stages when doing 3d art and I should not confuse them.

What I've been doing in the last hour is a good application of the fundamentals. What I will do here is not necessarily go to the sculpting stage just yet. Rather what I need to do now is deal with distributing the leaves and the flowers on the tree. Maybe I'll stick to just having flowers grow on the branches. Maybe the flowers can have leaves on their stalk.

For the whole tree, I should go with different tones of blue. I am thinking of making blue bell like flowers with glowing orbs within them. The illumination as it passes through the flower petals should be beautiful.

9:40pm. I'll do the tree, do the pool, do the tower rack, figure out how to do the pool water properly. After that I'll move to texturing and bump mapping.

After that I'll do another painting or two of the scene.

Then comes Luna. I'll go back to sculpting and master the material.

9:45pm. I feel like if I could do the above sufficient well, I'll break through to high 2/5. Right now I am 3.5 months in, so this is not bad progress. For most skills, 6 months is what you need to go from a beginner to 3/5. Meeting that goal is good enough.

At 3/5, I'll have my own style and appeal. I'll have decent efficiency as well.

So for the next few months, I will just continue practicing. I won't go beyond the basics and into esoterica, but ultimately, the basics are all that I need.

When I feel a level of satisfaction with my art work, I will stop work on it for a while and move on to music. I doubt that music will take me as long as 3d art to get decent at it. It feels like an easier thing to master if I focus on doing everything digitally.

9:55pm. I'll learn a lot over the next few months, but what will change compared to when I was a beginner is that I will have a fairly good mental map of the game. That will manifest as a level of comfort I did not have before.

Right now it is time to chill. I did decent time today. Maybe if I could start getting up at a proper time, I could get back to my usual schedule. But 2-9 is not bad either.

Now let me unwind. Let's see if I got any replies."

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[6a62582e43...](https://github.com/mrakgr/The-Spiral-Language/commit/6a62582e433a708564f35ca0b41d64199a760855)
#### Saturday 2022-01-15 19:38:51 by Marko Grdinić

"> Yeah so the ceo email it usually internally blocks everyone outside. So he doesnt get spammed. I would reach out and apply for a tenstorrent job you seem like you know what you are doing. Work in these companies then pitch your ideas to help further your research.
> The salaries are good around 150k base and 500k options for senior.
> And you get to see what kind of leading hardware or software direction in ML world.
> Start from the bottom up, most people develop their education or research IEEE published while working full time in companies

Meh, the odds of my resume not getting junked during the initial stage is too low to actually aim for any particular company. And working on a random programming job has very little appeal to me. I looked at TensTorrent job listings, what they want is C++ guys, and don't have remote postings. I am not interested in using C++ or moving from my comfy bedroom. I am not going to waste my time and mental energy on applying to companies anymore. I couldn't focus on art properly if my intentions were impure.

If they came to me with a decent offer it would be one thing, but as things stand I'd rather develop a skill that will allow me to make money in isolation. With what I am doing now I could gradually build up my foundation, rather than be a beginner is a large number of irrelevant tasks which is what these jobs offer me.

Right now, when it comes to doing creative work I can only sit down and churn out text, but if I was a proper expert in both art and music I could definitely hurt the world.

11pm. I should take a bath...yeah, I should take a bath. Let me leave Dohna Dohna for later.

11:55pm. I am back.

1:20am. I am watching GF ep 2 and noticing Doom door opening sounds as the dolls boot up. Holy shit. Is the budget so low that they had to take sound effects from the most iconic game of all time? Based on the animation quality the budget must be something like 5$.

1/15/2022

12:20pm. I got up very late today. But I slept quite well. I did go to bed past 1am, but it was actually an hour earlier than usual, so it is strange how late I got up. At any rate, I need to get the chores done with.

12:40pm. Let me chill for a bit. I want to read Kaiji.

12:45pm. Since he has female clothes he bought for his mom, I am guessing that is what Mario is going to use to disguise himself in order to get away from Teiai.

2:10pm. Let me finish this orange and then I will start for the day.

2:30pm. Phew, let me start.

2:35pm. Focus me. Art is pretty hard. It is fairly time consuming to do. Let alone having to deal with my lack of skill. But skill is not something that you can make up with money. The only way to get it is to actually work at it.

Sigh, let me work on the flower.

https://dengarden.com/gardening/All-Those-Bell-Shaped-Flowers

These should be good references.

Those bluebells are nice. But I am going to have to make up something on my own. This is not how I imagined it.

I am confused. How does mesh symmetry work in edit mode?

https://youtu.be/hApTsY4im8c
Blender 2.8 Modeling Beginner Tip : Symmetry & Mirror

Maybe this will answer my questions. I've used smmetry to good effect when sculpting, but now I am extruding points in edit mode and seeing the symmetry do nothing. I've never used it in edit mode before either. This is a good time to find out.

https://youtu.be/hApTsY4im8c?t=61

This is a technique worth keeping in mind. Snapping to vertex + auto merge. I never thought of it.

https://youtu.be/hApTsY4im8c?t=124

This is also a good technique. Setting the pivot point transform to the 3d cursor and then scale by -1 in the y axis.

https://youtu.be/hApTsY4im8c?t=296

He is going to show how to symmetrize the model without having to add a mirror mod again.

3pm. I am testing it out on the defualt cube, and it really does work. What it does not work on is when adding new verts and extruding.

Nope, it does not add new topology. Dissapointing. I'll need the mirror mod for that flower.

3:45pm. I got way too hung up on moving vertices around for a single flower petal. Let me go into sculpt mode and I will add depth to it.

4pm. Got one flower side done. Now I need to do the leaves at the bottom. One thing I am not sure if how to do the duplication around a center point. I haven't used the screw modifier even once. I am not sure that this is the right tool for the job anyway. Array maybE? I don't know.

Maybe the screw edit tool is what I need. I'll have to look into it. In the worst case, I can just set the 3d cursor in the right spot and do my rotation around by hand.

4:15pm. I am taking a breather. Let me resume. What I will do next is the leaf petal. Or I could reuse the original design.

4:30pm. Damn it, I fucked up. I should have developed the flower in a separate file.

4:40pm. What was the key to switch objects while in sculpt mode.

https://www.youtube.com/watch?v=NlDWnxMPhjo

It was D it seems.

4:55pm. It can't be used in edit mode. At any rate, I made some crock ups. I regret applying the solidify modifier on all the leaves and patals as it is making things a lot more difficult.

5:30pm. Had to leave for lunch. I am thinking how to do the stalk.

No, geometry nodes are not the answer. I mean, I could...

5:35pm. Actually, why don't I do it.

5:40pm. Focus me, let me resume.

What I will do is make the stalk a curve. That will allow me to use the hair particle system to comb the particles into shape.

...Actually, I think I read on the developer issue somewhere that geo nodes do not interact with particle systems just yet.

Nonetheless, going down this route is still a good idea as it will allow me to vary the objects. Let me do it.

5:50pm. This is confusing. What do those diamond sockets mean?

https://docs.blender.org/manual/en/latest/interface/controls/nodes/parts.html#sockets

What about the diamonds?

https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/fields.html

Those are fields.

Maybe I am doing this wrong.

6pm. Yeah, I was doing it wrong. I remembered that instead of setting the radius in the circle curve, the curve itself has an radius.

6:15pm. I just realized what the switch node is for and am playing with it.

6:15pm. I am confused. Why did the direction of the curve change suddenly.

6:30pm. Bo. At any rate, just switching its direction did the trick.

Now think me. What I need to do next is distribute the leaves along the stalk.

Focus on the task at hand.

I'll figure out how to put the crown and the nest ontop of the head later...

Ah, what I could do is trim the end of the curve, select that endpoint, and place the object there. That would be ideal.

6:55pm. Ok, now I have to figure out is how to control the way that points are distributed on the mesh. I do not want it to put leaves on the head. Instead I want it to be below the cutoff. Also I'd want to scale the leaves by their curve factor.

7pm. I am getting drowsy at this point, but I need to put in some extra time into it.

https://youtu.be/Hwnl_3trS3M
How to align vertices in any situation in Blender - Part 01

Let me watch this tutorial since it caught my eye.

Then I will look up how to control the point distribution.

7:05pm. Hmm, creating custom orientations is pretty powerful. I need to keep it in mind.

7:15pm. I decided to stop watching the tutorial and simply tried the capture attribute. It worked. Amazing!

7:30pm. No, the way I am doing it is not right.

8pm. Holy shit, Geometry nodes make such a mess. I am cleaning up and am just making things worse!

8:15pm. I am dying here. I sort of had it working before, but now the scaling is completely broken and I am out of mental energy to deal with it. I am not at all being creative and am just moving things around at random. I should have known better than to force it. When things start going wrong for you, you must stop. Unless you are in the right mindset, programming is impossible.

I am not at all thinking about the cause and how to fix the problem because it is too tedious.

If there is any better sign that I am not going to be able to fix the problem, I am yet to run into it all my years of programming.

8:25pm. Enough, enough, enough. For some reason the point factors are 0 everywhere, whereas they haven't been that before.

I am going to put the blame on all of this on geo nodes. Compared to writing code in text, they are much more difficult to deal with.

I have no idea why getting the spline factor got broken. The only explanation is that capture attribute is not in the right place. I am going to investigate this tomorrow.

I really hate it when days end on a note like this.

...Let me try just a bit more. I am going to try moving the capture attribute.

8:35pm. Nope. Hrrrrrgggghhhh...

I am going to have to open a fresh file and try distributing points on a curve in it. That will tell me where I am going wrong.

Maybe I am overlooking some scoping issue. Maybe I did something and lost track of things because I do not have the mental power to keep it all together anymore.

I am going to treat this as programming and check all the steps properly tomorrow. Let me close here. Maybe I'll watch that video and then move to resting."

---
## [HanshenWang/project-isidore](https://github.com/HanshenWang/project-isidore)@[132f7b1d9b...](https://github.com/HanshenWang/project-isidore/commit/132f7b1d9b7a99ce8bc702e5a7d39322d72cb505)
#### Saturday 2022-01-15 21:02:16 by Hanshen Wang

Perf: Add type declarations, turn on block compilation.

Also use the destructive version of reverse in `search-bible'. Use fixnums where
possible...

I believe BKNR.DATASTORE already uses a hash table data structure for it's
index, as seen in profiler reports. There are no complicated algorithms to
optimize either. What's left is optimization tricks and compiler knobs.

From https://common-lisp.net/~sionescu/hunchentoot-0.15.7/doc/#performance,

--- Snip here ---

If you're concerned about Hunchentoot's performance, you should first and
foremost check if you aren't wasting your time with premature optimization. Make
a reasonable estimate of the amount of traffic your website should be able to
handle and don't try to benchmark for loads Google would be proud of. Here's a
part of an interview with someone called John Witchel about his experiences with
his company Red Gorilla that can't be quoted often enough (it seems the original
source of the interview has vanished):

    Q: If you could go back and change anything, would Red Gorilla still be in
    business today?

    A: Yes. I would start small and grow as the demand grew. That's what I'm
    doing now.

    Back then we planned to be huge from the outset. So we built this monster
    platform on BEA, Sun and Oracle. We had huge dedicated connectivity pipes.
    We had two full racks clustered and fully redundant. We had E450's with
    RAID-5 and all 4 CPU slots filled, E250s, F5 load balancers... the cost of
    keeping that system on was enormous. The headcount to keep it humming was
    enormous too.

    The truth is, we could have run the whole company on my laptop using a cable
    modem connection.

Having said that, my experience is that Hunchentoot doesn't have to hide when it
comes to serving static files. If you really have performance problems with
Hunchentoot, there are two things I'm aware of you should watch out for.

    Check how your Lisp implementation implements multi-processing. While I
    write this (April 2007), some Lisps, like CMUCL, still use their own green
    threads, and some others, like AllegroCL and LispWorks, use OS-threads but
    allow only one Lisp thread at a time. Unless you're using a Lisp that
    employs "real" symmetric multi-processing like SBCL (on some platforms) or
    Clozure MCL, you shouldn't compare apples with oranges. (Note: For CMUCL,
    you also shouldn't forget to use the dreaded
    MP::STARTUP-IDLE-AND-TOP-LEVEL-LOOPS.) All text output sent from handlers
    goes through two layers of Gray streams by default (FLEXI-STREAMS and
    Chunga). This isn't an issue for small to medium-sized pages, but can be for
    large ones. There are several ways to cope with this - return binary data
    from handlers, bypass FLEXI-STREAMS, sit behind mod_lisp, etc. Try it, and
    if you really think that Hunchentoot is too slow for what you're trying to
    do and what you'll need, ask on the mailing list and we'll try to help.

--- End snip ---

So to sum it up, maybe bypassing flexi-streams would yield some performance
benefits as I generate some pretty large pages of dynamic html.

What's left is really just to benchmark the website. I suspect 500 req/s is
reasonable based on one guy's report on traffic increase from the front page of
reddit (he had a poisson distribution of less than 0.01% chance of 360 req/s).

https://www.tylermw.com/visualizing-a-reddit-hug-of-death-and-how-to-reddit-proof-your-website-for-pocket-change/

Overall, I'm pretty happy with the performance.

---
## [mwalters/homed](https://github.com/mwalters/homed)@[8b044b0f87...](https://github.com/mwalters/homed/commit/8b044b0f8743a4dfc7e6d89dc35866cebe9230e6)
#### Saturday 2022-01-15 21:43:16 by Matt Walters

Customization improvements (#5)

v1.0.0 -- First official release

With having come up with a way to allow easier feature enhancements to be delivered to users without over burdening them, the 1.0.0 release can be cut.  I'll be thinking on where to go from here.  Feel free to make [feature requests](https://github.com/mwalters/homed/issues/new?

* Separate custom CSS and JS into user volume, leave app in and run from original location in container
* Combine CSS for fewer http requests; JS not combined because file size makes editing annoying, and honestly, it's not that important for this project
* Update readme

---

