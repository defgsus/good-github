## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-29](docs/good-messages/2022/2022-03-29.md)


1,788,948 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,788,948 were push events containing 2,860,437 commit messages that amount to 215,949,799 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[65329f4fac...](https://github.com/pytorch/pytorch/commit/65329f4fac8fb22318b7a3eb115e9da207d8d41a)
#### Tuesday 2022-03-29 00:14:18 by Edward Z. Yang

Disable meta device tests.

After discussion with Can Balioglu, we have concluded that
https://github.com/pytorch/pytorch/pull/53682 , while clever, is more
trouble than it is worth.  The main problem is that whenever someone
adds support for new meta tensors, they then get dozens of new test case
failures, because tests that were previously halted by lack of support
for an operator on meta tensors, now have gotten further and hit some
logic which expects to be able to, e.g., pull out a real value from a
tensor (which clearly doesn't work).  This is very annoying and time
consuming!  Most of these tests aren't written with meta device in
mind, and it's not a good use of time to try to make them more generic.

The plan on record is to switch meta testing to OpInfo, but that patch
will take some time to prepare for now I want to stem the bleeding.  I
don't think we're at high risk for regressions here because meta tensors
mostly share logic with their regular brethren.

Signed-off-by: Edward Z. Yang <ezyangfb.com>

Pull Request resolved: https://github.com/pytorch/pytorch/pull/74468

Approved by: https://github.com/mruberry

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[e58fb506ef...](https://github.com/san7890/bruhstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Tuesday 2022-03-29 00:15:30 by LemonInTheDark

Almost halves airlock auto close delay (#65349)

We go from a delay of 15 seconds, to 8.

This has cheesed me off for a long time. Airlocks should lock, not just
stay open for a quarter of a minute.

This'll help with excited groups that stay permenantly connected at
highpop because of a slowed ssair and doors opening and closing
constantly

Also effects door chasing. I'm honestly just kinda eyeballing this, it
might be a bit much. Even if this goes through could totally be tweaked

Even if this is too low, 15 is way too damn high.

---
## [personinblack/black](https://github.com/personinblack/black)@[334625b408...](https://github.com/personinblack/black/commit/334625b408e92ea3608beedac8e794a9ac17c50e)
#### Tuesday 2022-03-29 00:21:59 by personinblack

switch from Gradle to Maven

because maven just works unlike gradle which gets broken after every fucking
update and i don't want to spend my time maintaining gradle scripts.

fuck you Gradle.

---
## [Tastyfish/Skyrat-tg](https://github.com/Tastyfish/Skyrat-tg)@[41aa1d2ee4...](https://github.com/Tastyfish/Skyrat-tg/commit/41aa1d2ee421161505284504f4d6f76faf51b0f7)
#### Tuesday 2022-03-29 00:46:33 by SkyratBot

[MIRROR] Adds a colorblind accessability testing tool [MDB IGNORE] (#11995)

* Adds a colorblind accessability testing tool (#65217)

* Adds a colorblind accessability testing tool

I keep finding myself worrying about if things I create will be parsable
for colorblind people. So I've made a debug tool for approximating
different extreme forms of colorblindness.

It's very very much a hack. We can't do the proper correction required
to actually deal directly with long medium and short wavelengths of
light, so we need to rely on approximations. Part of that means say,
bright things being brighter then they ought to be. S not how people
actually experience things, but it's not something we can do anything
about in byond.

Anyway uh, it works by taking color matrixes, and using the plane master
grouping system floyd added to apply them to most all parts of the game
you would want to color correct.

There's some slight fragility here, but I couldn't think of a better way
of handling it.

We also need to deal with planes that have BLEND_MULTIPLY as their
blendmode, since that fucks up the filter. I've come up with a hack for
it, since I wanted to avoid breaking anything.

Oh and since I want it to apply to huds too I added plane masters to
represent them. I think that's about it.

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Adds a colorblind accessability testing tool

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [Iamgoofball/-tg-station](https://github.com/Iamgoofball/-tg-station)@[134ac444be...](https://github.com/Iamgoofball/-tg-station/commit/134ac444be858e3811dc18c75407459dbaee505e)
#### Tuesday 2022-03-29 00:51:47 by Iamgoofball

You can now see the plant's health with a plant analyzer because literally who the fuck thought it was a good idea to base so much stuff on the plant health and have so many chemicals involving the plant's health and then not letting you see the plant's health? Like, god, this is painful. I sat for 30 minutes feeding some rainbow weed, a fresh seed, cryoxadone, diethylamine, and saltpetre and still got the stupid "ITS TOO UNHEALTHY FOR GENE SHEARS" prompt, so I want to know why my plants are goddamn unhealthy despite being fed so much damn fertilizer.

---
## [StarStation13/StarStation13](https://github.com/StarStation13/StarStation13)@[55336d1e53...](https://github.com/StarStation13/StarStation13/commit/55336d1e5308789be1616413c8d8f87e073f7302)
#### Tuesday 2022-03-29 00:59:21 by vincentiusvin

Atmos Control Console Refactor (and syndiebase atmos tidyup) (#65372)

Main Takeaways For Mappers:

Use monitored pathed atmos devices very carefully. Also dont put atmos_sensors willy nilly. They are used to hook to atmos control monitors.

We want to keep at most one device broadcasting for each of the atmos sensor, inlets, and outlets. Run the mapping verb Check Atmos Chamber Devices to be sure, though this might not catch everything.

Some of the warning are pretty harmless. For example if you have reconnected the "station atmos monitor" and you get no listener for distro/waste loop warning, it's safe to ignore.

I don't know what the maptainer policy is on making new subtypes for offstation content, but if you do please branch off the general ones instead of the specific gas ones. If you aren't making a new subtype, varedit the general ones too.

About The Pull Request:

Need Would prefer this to be merged before #65271 (In game atmos guide).
Not strictly necessary, just makes me sleep better knowing the handbook wont die alongside the rest of the UI.

Fixes #36668 (Atmos Monitoring Consoles don't update it's sensors to the new tank after reconnect())
Fixes #32122 (Mix console fucked after reconnecting it)

Also made the distro meter thing broadcast more info instead of just the pressure, because I'm sure nobody would care and it would make my life easier.

A small high-level overview in case this breaks again in the future:

A signal datum (not DCS) is sent by the atmospheric devices (injectors and vents) and will be received by the atmos computers. The data is then stored at the monitor object and then passed to the UI. This initial signal is sent by `broadcast_signal()`, called by `atmos_init()`.

New sensors/vents (if you can actually get them in game, still only adminspawn/wrenchables afaik) will also initiate the conversation if atmos_init() is called, so it works fine. This means you need to unwrench and re-wrench the devices if you adminspawn them though, ugh.

In case of a newly built computer, it needs to be the one that prompt the data to the devices, so we send a request signal. This is a bit inefficient since it doesnt work off of callbacks and assocs like DCS, but won't really matter since we're doing this rarely.

We only talk with the injectors and vents when necessary here, while sensors and meters keep beeping with every process_atmos() tick so they rarely break.


Why It's Good For The Game:

Messy code gone (debatable).


Refactored the atmos control console devices. The ones that hook to the big turf chambers.
Distro meter now broadcast the whole gasmix info instead of just pressure to the monitors.
Lavaland syndie's atmos chamber vents are now actually configurable. Moved a few things around to accomodate this.
Lavalannd syndie chambers hooked to distro and moved distro pipe to layer2
atmos monitors can detect reactions now.
Some minor code changes to how anomaly refinery and implosion compressor show the gas info. No changes expected, report if bug.
recoded checks for atmos chamber abnormalities in debug verbs.

---
## [twilightwanderer/Skyrat-tg](https://github.com/twilightwanderer/Skyrat-tg)@[8b1ec33143...](https://github.com/twilightwanderer/Skyrat-tg/commit/8b1ec331432234f358b26ee1627c10358ccae6a7)
#### Tuesday 2022-03-29 00:59:25 by LeonY24

P90 (#12125)

* P90 SMG

le new gun for new away mission we're planning to make

* Update p90.dm

* includes p90.dm

my fucking retard ass hadnt shit included bruh

---
## [N5N3/julia](https://github.com/N5N3/julia)@[62e0729dbc...](https://github.com/N5N3/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Tuesday 2022-03-29 01:02:48 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>

---
## [Son-of-Space/tgstation](https://github.com/Son-of-Space/tgstation)@[c8ef62c1fb...](https://github.com/Son-of-Space/tgstation/commit/c8ef62c1fb7027ea58b569f0e4bd7df5a7d58935)
#### Tuesday 2022-03-29 01:09:59 by LemonInTheDark

Fixes bartender drink throwing, makes smashing always spill (#65698)

Tohg's initial pr (9c0b0e5d4cc236e365ef0229400cefe98b184964) was rather poorly argued and a bit misleading, but the actual changes were honestly kinda harmless. You could already have thrown beakers to splash shit on someone, it wasn't a big issue.

However it did end up breaking bartending, because it removed the ranged
args that normally get passed into smash and SplashReagent.

I went in intending to fix that, but noticed some dumb copypasta in
broken bottle code, and decided to just start from there.

I've moved that logic to a proc on the broken bottle, and made smashing
a bottle on something splash its contents too.

I can't think of a case where you wouldn't want this, so I'ma just go
for it. Prevents future mistakes like this too.

Oh and because I'm passing ranged in properly now, splashing will not
always splash the whole amount of the bottle's reagents. Doubt that
really matters tho.

Love ya bestie

---
## [loongarch64/nss](https://github.com/loongarch64/nss)@[d96a53efa3...](https://github.com/loongarch64/nss/commit/d96a53efa3176c25710bd8495f0e17837f6a1969)
#### Tuesday 2022-03-29 02:24:34 by Martin Thomson

Bug 1713562 - Validate ECH public names, r=bbeurdouche

This validates that they are LDH (with underscore because we don't hate
freedom), but that they are not IP addresses.  This invokes the horrible WhatWG
IP parsing routines, so that it recognizes a vast array of crazy address formats
(thanks 1980s design).

Differential Revision: https://phabricator.services.mozilla.com/D116343

--HG--
extra : source : 27c19f19a885b7381fb263b1a56f88025b24e488
extra : amend_source : 8d6852c85e9d5e06e48228723edb144ffc64cc8f

---
## [Brycew73/MSweeper](https://github.com/Brycew73/MSweeper)@[8d861d632c...](https://github.com/Brycew73/MSweeper/commit/8d861d632c9cf4045e6ff7b2cfe437bd68048fa2)
#### Tuesday 2022-03-29 03:53:30 by Matthew

Hi guys, sorry for the wait on this. Here's what I added:

Changed: Guest Servlet, SignInServlet, signInController, index.jsp
Added: highScoreController

SignIn will now push into Index if the correct username and passwords
are selected. Guest will also push into Index if the name is valid. Both
will result in the username being displayed at the top of the Index
page.

I added the fake database in. It displays the current list of high
scores into the Index page. As of right now, it might not work if you
pull it since I'm running Derby through my local files. Bryce said that
he's going to try to add the Derby project from our lab into Git, so
until then, the database will most likely not work.

***Note: I have a slightly different version of JDK, but since Eclipse
lets you change which version you use pretty easily, I didn't think much
of it. If we want, we should try to find a version we all can use. I
didn't want to download anything since I'm not sure what everyone's
using.
Let me know if you have any questions. Thanks!

---
## [TerraLindaHighSchool/memorium-memorium-production-team](https://github.com/TerraLindaHighSchool/memorium-memorium-production-team)@[97ed4ef350...](https://github.com/TerraLindaHighSchool/memorium-memorium-production-team/commit/97ed4ef35003ac75fbc7f016dd93a6b2599de8ec)
#### Tuesday 2022-03-29 04:00:56 by WoofMeister

i hate you stupid github you need to die jk lol not really haha funny also i put angyboi inside unity bc hawt

---
## [dilipbalaut11/custom_compression](https://github.com/dilipbalaut11/custom_compression)@[ec62cb0aac...](https://github.com/dilipbalaut11/custom_compression/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Tuesday 2022-03-29 05:45:28 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [PKRoma/Terminal](https://github.com/PKRoma/Terminal)@[aa9fe1c32a...](https://github.com/PKRoma/Terminal/commit/aa9fe1c32ad9d20ad2da14606f1985aa5520bfea)
#### Tuesday 2022-03-29 06:42:56 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [arthur791004/gutenberg](https://github.com/arthur791004/gutenberg)@[3ea2d42b0a...](https://github.com/arthur791004/gutenberg/commit/3ea2d42b0a6a206663735a47f9796bd42eda2186)
#### Tuesday 2022-03-29 09:53:23 by Dennis Snell

Blocks: Remember raw source block for invalid blocks. (#38923)

Part of #38922

When the editor is unable to validate a block it should preserve the
broken content in the post and show an accurate representation of that
underlying markup in the absence of being able to interact with it.

Currently when showing a preview of an invalid block in the editor we
attempt to re-generate the save output for a block given the attributes
we originally parsed. This is a flawed approach, however, because by
the nature of being invalid we know that there is a problem with those
attributes as they are.

In this patch we're introducing the `__unstableBlockSource` attribute on 
a block which only exists for invalid blocks at the time of this patch. That 
`__unstableBlockSource` carries the original un-processed data for a block
node and can be used to reconstruct the original markup without using
garbage data and without inadvertently changing it through the series
of autofixes, deprecations, and the like that happen during normal block loading.

The noticable change is in `block-list/block` where we will be showing
that reconstruction rather than the re-generated block content. Previously
it was the case that the preview might represent a corrupted version of the
block or show the block as if emptied of all its content. Now, however,
the preview sould accurately reflect the HTML in the source post even
when it's invalid or unrecognized according to the editor.

Further work should take advantage of the `__unstableBlockSource`
property to provide a more consistent and trusting experience for
working with unrecognized content.

---
## [measurement-factory/squid](https://github.com/measurement-factory/squid)@[2b6b1bcb86...](https://github.com/measurement-factory/squid/commit/2b6b1bcb8650095c99a1916f5964305484af7ef0)
#### Tuesday 2022-03-29 10:04:24 by Alex Rousskov

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
## [Sedna-Games/Zero-Possession-Prototype](https://github.com/Sedna-Games/Zero-Possession-Prototype)@[5728d2d81c...](https://github.com/Sedna-Games/Zero-Possession-Prototype/commit/5728d2d81c1408e5e97f6d439c1e65cf95e6c402)
#### Tuesday 2022-03-29 12:18:27 by Hamraj

[WIP] First 3 Buildings LD Set Dressing Good

- holy fuck takes time to get these done and think of cool designs for the levels and make shit interesting but its getting there bois and gals

---
## [BearerPipelineTest/EasyAdminBundle](https://github.com/BearerPipelineTest/EasyAdminBundle)@[f3a4b13382...](https://github.com/BearerPipelineTest/EasyAdminBundle/commit/f3a4b13382f6d96f85b0b1d8dfe329f40a39d32c)
#### Tuesday 2022-03-29 12:21:36 by Javier Eguiluz

minor #5139 Disable UX-Turbo (Lustmored)

This PR was merged into the 4.x branch.

Discussion
----------

Disable UX-Turbo

In all my projects with EasyAdmin I am sharing Stimulus controllers between EasyAdmin and frontend (I need them sometimes and it's just simpler). Since enabling Turbo on some projects I need to overwrite EasyAdmin layout just to disable it.

Currently EA is very unfriendly towards Turbo - there are JavaScripts in body, DOMContentLoaded listeners and so on. Refactoring everything to be turbo-compatible would be titanic effort with little benefit (it's not really needed in CRUD dashboards in my opinion), while adding this single attribute will make life easier for probably more consumers than just myself :)

Commits
-------

735b2397 Disable UX-Turbo

---
## [willemneal/nearcore](https://github.com/willemneal/nearcore)@[6351eb5511...](https://github.com/willemneal/nearcore/commit/6351eb55116fea2f906d681ce6966b5ec2546176)
#### Tuesday 2022-03-29 13:53:51 by Simonas Kazlauskas

Use non-blocking log writer (#6470)

This will utilize a separate thread to write out the spans and events
without while letting the main computation to proceed with its business.
Additionally, we are buffering the output by lines, thus reducing the
frequency of syscalls that can occur when the subscriber is writing out
parts of the message.

This should mitigate concerns of enabling debug logging as its impact on
performance should now be minimal (putting an event structure onto a
MPSC queue.) There are still costs associated with logging everything
however. Most notably formatting and construction of the
`tracing_core::ValueSet`s still occur on the caller side, so if
constructing those is expensive, the logging might remain expensive.
An example of code sketchy like that (although silly) could be:

```
debug!(message = { std::time::sleep(Duration::from_secs(1)); "hello" })
```

or for a less silly example:

```
debug!("{}", my_vector.iter().map(|...| {
  do_expensive_stuff()
}).collect::<String>())
```

These should be considered a bug (alas one that `tracing` does not have
any tooling to detect, sadly.)

I opted adding a new crate dedicated to observability utilities. From my
experience using things like prometheus will eventually result in a
variety of utilities being written, so this crate eventually would
likely expand in scope...

Fixes https://github.com/near/nearcore/issues/6072 (though I haven't made any actual measurements as to what the improvement really is)

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[5b36e44a83...](https://github.com/treckstar/yolo-octo-hipster/commit/5b36e44a830b9858955f09aa5c59387fa2551952)
#### Tuesday 2022-03-29 16:45:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [gvajrala/CIS552Project](https://github.com/gvajrala/CIS552Project)@[96238e684b...](https://github.com/gvajrala/CIS552Project/commit/96238e684b0d85cb17cd23bfb15f50aab98c00ba)
#### Tuesday 2022-03-29 16:45:20 by gvajrala

About Project

                                                         CIS 552 - Database Design
                                                              Spring 2022
                                                          Project Specifications

Checkpoint 1

All the work is done as the part of the semester long project for CIS 552 - Database Design (Spring 2022) taught by Professor Gokhan Kul PhD.
The goal of the project is to implement complete SQL interpreter using Java. The libraries allowed to use have been included. 
The description of the jar files can be found here-Libraries included 
    JSQLParser-UB (Jar | JavaDoc | Source)
    EvalLib (JAr | Source)
    Apache Commons CSV (Jar | Source)

 The intructions to download data generator and setting it up are available here.

This project has been divided into Multiple checkpoints 

Check Point -1 

Checkpoint 1 of the project aims to make sure you are able to utilize relational algebra knowledge you gained in the class. It is essential that you prepare a good infrastructure to evaluate queries at this early stage to make sure you are well prepared for the following checkpoints. In this checkpoint, you will be asked to evaluate a few single-table and two-table SQL queries. There are a couple of ways to complete this project, and some of these are better than the others. We will go through a few design decisions, pointing out tradeoffs, and explaining why a strategy that might seem easier in the short term turns out to be significantly harder later. The success criteria of this checkpoint is to be able to evaluate 5 queries correctly.

Specifically, you'll be given a number of queries in one of the following patterns:
1.	CREATE TABLE R (A int, B date, C string, ... )
2.	SELECT A, B, ... FROM R
3.	SELECT A, B, ... FROM R WHERE ...
4.	SELECT A+B AS C, ... FROM R
5.	SELECT A+B AS C, ... FROM R WHERE ...
6.	SELECT * FROM R
7.	SELECT * FROM R WHERE ...
8.	SELECT R.A, ... FROM R WHERE ...
9.	SELECT Q.C, ... FROM (SELECT A, C, ... FROM R) Q WHERE …
10.	SELECT R.A, S.B, … FROM TABLE1 R, TABLE2 S WHERE R.C = 5, R.D = S.D
Your task is to answer these queries as they arrive.

Volcano-Style Computation (Iterators)
Let's take a look at the script we've used as an example in class.
with open('data.dat', 'r') as f:
  for line in f:
    fields = split(",", line)
    if(fields[2] != "Ensign" and int(fields[3]) > 25):
      print(fields[1])
This script is basically a form of pattern 3 above
SELECT fields[1] FROM 'data.dat' 
WHERE fields[2] != "Ensign" AND CAST(fields[3] AS int) > 25

Or in other words, any query that follows the pattern...
SELECT /*targets*/ FROM /*file*/ WHERE /*condition*/
...becomes a script of the form...
with open(file, 'r') as f:
  for line in f:
    fields = split(",", line)
    if condition
      print(targets)

This is nice and simple, but the code is very specific to pattern 3. That's something that will lead us into trouble. To see a simple example of the sort of problems we're going to run into, let's come up with an example of pattern 5:
SELECT height + weight FROM 'data.dat' WHERE rank != 'Ensign'
That is, we're asking for the sum of height and weight of each non-ensign in our example table. An equivalent script would be...
total = 0

with open('data.dat', 'r') as f:
  for line in f:
    fields = split(",", line)
    if fields[2] != 'Ensign':
      total = int(fields[4]) + int(fields[5])
      print(total)    
There's a pretty significant difference in the flow of the code in this version of the script. For one, there's a new global variable with the total that equals to the sum of weight and height. Now let's say we wanted to support both patterns 3 and 5. Then we would need to check which query pattern the query follows, and write code that supports each pattern. As you can see, if you try to do this, you would need to support patterns 1, 2, 3, 4, 5, 6, 7, 8, 9, and 10 or the even more complex queries that will show up in later checkpoints.
There are a number of workflow steps that appear in more than one pattern. For example:
1.	Loading the CSV file in as data
2.	Filtering rows out of data
3.	Transforming (mapping) data into a new structure
4.	Printing output data
Most of these steps do something with data, so let's be a little more precise with respect to what we mean there. (1) When a CSV file is loaded, it's a sequence of rows and attributes. (2) Filtering doesn't change the structure: it's still rows and attributes. (3) Transforming (picking out specific columns) does change the structure, but at the end of the day we're still working with rows and attributes (or in the case of this script, just one attribute). (4) Printing doesn't change the structure: however, you need to do it in the correct format.
In short, this idea of rows and attributes is pretty fundamental, so let's use it. We're going to work with data expressed in terms of tables: or collections of rows and attributes. This allows us to abstract out each of those workflow steps from before into a set of functions:
1.	read_table(filename) -> table
2.	filter_table(table, condition) -> table
3.	map_table(table, rules) -> table
4.	print_table(table)
But we still have a problem. These table objects are going to be as big as the data they represent... they can get super large. That's a massive drawback compared to our initial script design, which has constant-space usage. So what else can we do?
Let's look at why the original script uses constant-space. We load one record in upfront (that's constant space). We decide whether the record is useful to us (still constant space). Whether or not we print it, by the time we get to the next record, we're done with the current row and can safely discard it. Can we recover the same sort of property?
For this checkpoint, it turns out that we can. If you've used java, you're probably familiar with the Iterator interface. An iterator lets you access elements of a collection without needing to have all of those elements available at once. That is, you define two methods:
hasNext()
Returns true if there are any more rows to read
next()
Returns exactly one row. (the next row in the list)
Because the iterator eventually returns each row of the table, it behaves sort of like a table object, but because it only returns one row at a time it doesn't strictly need all of the data to be in memory at once. Moreover, you can define one iterator in terms of another. For example, you might define a filtering iterator that takes a source iterator as part of its constructor, and every time you call next(), keeps calling source.next() until it finds a row that satisfies the where clause.
In short, iterators give you composability and low memory use. The first property is important for your sanity, while the latter property is important for your performance.
Data Representation
When it comes to figuring out how to represent one row of data, you have two questions to answer: (1) How do I represent a single primitive value, and (2) How do I represent an entire row of primitive values.
For the first question, there are two practical choices: Either as raw strings (taken directly from the CSV file) or parsed into PrimitiveValue objects. PrimitiveValue is an interface implemented by several classes that represent specific types of values, for example longs, dates, and others. Because EvalLib (a library that I'll describe shortly) uses PrimitiveValues internally, most students find that it is easier to write code that performs well if you use PrimitiveValue.
For the second question, I strongly encourage the use of Java arrays. There are a few options, including ArrayLists, Vectors, Maps, and other structures. Java arrays outperform them all pretty drastically.
EvalLib
The JSqlParser Expression type can represent a whole mess of different arithmetic, boolean, and other primitive-valued expressions. For this project, you'll have a library to help you in evaluating these expressions: EvalLib. Before we get into it, you should note a distinction between two types of expression:
Expression
A generic expression. Can be anything: a comparison, a string, a multiplication, a regular expression match.
PrimitiveValue
The basic unit of data. Can be a: Boolean, Date, Double, Long, Null, String, Timestamp or a Time. Note that PrimitiveValues are also perfectly legitimate (if somewhat boring) Expressions.
EvalLib includes a single class called Eval that helps you to resolve Expression objects into PrimitiveValues. Eval is an abstract class, which means you'll need to subclass it to make use of it, but we'll get back to that in a moment. First, let's see a quick example.

Eval eval = new Eval(){ /* we'll get what goes here shortly */ }
// Evaluate "1 + 2.0"
PrimitiveValue result;
result = 
  eval.eval(
    new Addition(
      new LongPrimitive(1),
      new DoublePrimitive(2.0)
    )
  ); 
System.out.println("Result: "+result); // "Result: 3.0"
// Evaluate "1 > (3.0 * 2)"
result = 
  eval.eval(
    new GreaterThan(
      new LongPrimitive(1),
      new Multiplication(
        new DoublePrimitive(3.0),
        new LongPrimitive(2)
      )
    )
  );
System.out.println("Result: "+result); // "Result: false"

In short, eval helps you evaluate the Expression objects that JSQLParser gives you. However, there's one thing it can't do: It has no idea how to convert attribute names to values. That is, there's one type of Expression object that Eval has no clue how to evaluate: Column. That is, let's take the following example:
// Evaluate "R.A >= 5"
result =
  eval.eval(
    new GreaterThanEquals(
      new Column(new Table(null, "R"), "A"),
      new LongPrimitive(5)
    )
  );

What value should Eval give to R.A? This depends on the data. Because EvalLib has no way of knowing how you represent your data, you need to tell it:
Eval eval = new Eval(){
  public PrimitiveValue eval(Column c){ 
    /* Figure out what value 'c' has */
  }
}

Deliverable
For this checkpoint, you'll be running multiple queries in sequence. This means a few changes to your code. First, before calling parser.Statement(), you will take a txt file location where the queries are stored separately in every line. You should print the results of each query with System.out, and after each SELECT query, you should print a line of “=” without the quotes. This is so that the testing framework knows when your code is ready for the next query.
Source Data
Because you are implementing a query evaluator and not a full database engine, there will not be any tables -- at least not in the traditional sense of persistent objects that can be updated and modified. Instead, you will be given a Table Schema and a CSV File with the instance in it. To keep things simple, we will use the CREATE TABLE statement to define a relation's schema. To reiterate, CREATE TABLE statements only appear to give you a schema. You do not need to allocate any resources for the table in reaction to a CREATE TABLE statement -- Simply save the schema that you are given for later use. Sql types (and their corresponding java types) that will be used in this project are as follows:

SQL Type	Java Equivalent
string	StringValue
varchar	StringValue
char	StringValue
int	LongValue
decimal	DoubleValue
date	DateValue
In addition to the schema, you will find a corresponding [tablename].dat file in the data directory. The name of the table corresponds to the table names given in the CREATE TABLE statements your code receives. For example, let's say that you see the following statement in your query file:
CREATE TABLE R(A int, B int, C int);
That means that the data directory contains a data file called 'R.dat' that might look like this:
1|1|5
1|2|6
2|3|7
If I run the following query on this data
SELECT * FROM R WHERE C > 5;
The program must output the following:
1|2|6
2|3|7
If I run the following query on this data
SELECT R.A, R.B FROM R WHERE C > 5;
The program must output the following:
1|2
2|3
Each line of text (see BufferedReader.readLine()) corresponds to one row of data. Each record is delimited by a vertical pipe '|' character.  Integers and floats are stored in a form recognized by Java’s Long.parseLong() and Double.parseDouble() methods. Dates are stored in YYYY-MM-DD form, where YYYY is the 4-digit year, MM is the 2-digit month number, and DD is the 2-digit date. Strings are stored unescaped and unquoted and are guaranteed to contain no vertical pipe characters.
For this project, we will issue 5 queries to your program excluding CREATE TABLE queries. These queries will NOT be timed, and they will be evaluated based on the correctness of the query results. Note that there is a 5 minute deadline for each query, though. Answering each query successfully will bring you 10 points each. 

Your code will be expected to handle these queries, as well as others.
●	Sanity Check Examples: A thorough suite of test cases covering most simple query features.
●	Example NBA Benchmark Queries: Some very simple queries to get you started.

These files have the same structure with what we will use to evaluate our 5 queries. Also keep in mind that for ALL queries, the grader will time out and exit after 5 minutes.

---
## [alexkxu/thefuck](https://github.com/alexkxu/thefuck)@[7f97818663...](https://github.com/alexkxu/thefuck/commit/7f97818663de9351ac7e2c6314ed94184811d62a)
#### Tuesday 2022-03-29 16:52:45 by Romain Heller

#455: [README] Add uninstall instructions (#1171)

* ~[Doc] Add Uninstall instructions

As we need the package and to modify the shell config, users could have a pain in the ass when it comes to retire *The Fuck* from the system.

* Update README.md

* Update README.md

Co-authored-by: Pablo Aguiar <scorphus@gmail.com>

---
## [tesujimath/letters-to-amy](https://github.com/tesujimath/letters-to-amy)@[9822f387cc...](https://github.com/tesujimath/letters-to-amy/commit/9822f387cc5ea8e7b301194a07ea5c98a0985002)
#### Tuesday 2022-03-29 17:21:34 by Simon Guest

The love of God (#34)

* The love of God

* God's love not that love

---
## [cyberknight777/my-stuffs](https://github.com/cyberknight777/my-stuffs)@[757fd0f57f...](https://github.com/cyberknight777/my-stuffs/commit/757fd0f57fd2e1730e15f6f6a3e36ca8703a9f4c)
#### Tuesday 2022-03-29 17:34:39 by Cyber Knight

scripts: kramel: Switch to LLVM Binutils for {AR, OBJDUMP, STRIP}

- GNU Binutils seem to break compilation hence let's switch to LLVM Binutils.
- Fuck you GNU.

Signed-off-by: Cyber Knight <cyberknight755@gmail.com>

---
## [cgaebel/magic-trace](https://github.com/cgaebel/magic-trace)@[218950a0a3...](https://github.com/cgaebel/magic-trace/commit/218950a0a3e46aa98f09b2697026a43113dccff3)
#### Tuesday 2022-03-29 17:56:42 by Clark Gaebel

Rework trigger modes

Replace `-symbol` with a "trigger mode" option. To quote my own help
text:

1) If you do not provide `-trigger`, magic-trace takes a snapshot
   when either it or the application under trace ends. You can Ctrl+C
   magic-trace to manually trigger a snapshot.

2) If you provide `-trigger $`, magic-trace will open up a
   fuzzy-find dialog to help you choose a symbol to trace.

3) If you provide `-trigger <FUNCTION NAME>`, magic-trace will
   snapshot when the application being traced calls the given
   function. This takes the fully-mangled name, so if you're using
   anything except C, fuzzy-find mode will probably be easier to
   use.

`-trigger .` is a shorthand for `-trigger magic_trace_stop_indicator`.

This also removes three command-line arguments that are, in my opinion,
a mix of unnecessary and probably a bad idea to expose:

- `-delay-thresh` can be replicated by an applicationg doing this
  measurement itself. It's a very cheap operation for an application
  to add, I don't think that magic-trace is adding very much here.

- `-duration-thresh` is in the same boat as `-delay-thresh`.

- `-immediate-stop` causes issues on some kernels. Let's just remove
  it for now and revisit it in a couple years. If people actually
  want their trace to end exactly when the trigger fires, we can
  postprocess the trace output.

Please play around with this! I think it's a easier to to use... but
that's just like my opinion, man.

Fixes #60 and #69.

---
## [clearlinux-pkgs/pypi-fabric](https://github.com/clearlinux-pkgs/pypi-fabric)@[3325891542...](https://github.com/clearlinux-pkgs/pypi-fabric/commit/332589154205587705bac1c6e93d27fdab5e6025)
#### Tuesday 2022-03-29 18:13:41 by Arjan van de Ven

pypi-fabric: Autospec creation for update from version 2.6.0 to version 2.7.0

David JM Emmett (5):
      Add default issue template
      Removing global-scope configuration for replacing environment variables, replacing with specific override to clear environment only for remote.
      Feedback: the kwarg override should be "gentle" and use kwargs.setdefault in case a user is explicitly giving it for some reason
      Feedback: there ought to be another test proving that this kwarg override is happening (currently the test change only proves that the config override is not happening) and also proving the setdefault is working (caller can override)
      Feedback: I am relatively sure we have a note about the run.replace_env override in the docs, which needs tweaking (probably to say that the change is now happening at the keyword argument level)

David Schneider (1):
      clarify documentation for Connection.put

Henry Harutyunyan (1):
      Typo fix

Jeff Forcier (29):
      Format tweaks to bugreport template, and try slapping in a link to contribution-guide
      More issue template tweaks
      Formatting/blackening
      Doc and changelog updates re #2144
      Send SSH window change message on SIGWINCH when pty=True
      No more IRC for now :( but also note the blog category exists
      Use a kwarg in an otherwise confusing posarg spot
      Add Connection.shell()
      Link to BPO roadmap from Fabric roadmap page
      Enhance language/styling around end of Connection workflow
      Admonishment in our changelog re: the other projects
      s/http/https/
      Badges, project_urls
      Split flake8, pytest to separate confs
      Tweak coverage/testing
      Dev invoke install not that useful and out of line with other projects
      Start porting to CircleCI
      Nix most of travis yml
      Tidy up
      Docs conf fixes for CI migration
      Add black to dev-reqs
      Not sure why these intersphinx refs weren't erroring before...
      Pushed silly rebuild packaging override down into invocations
      Use newer orb with sudo-coverage built in, plus massage overall circle config
      Travis all gone now bye bye
      Anonymize link to make sphinx shut up
      Travis->CI tweak for integration suite
      Changelog re: Circle migration; pre-bump version for release
      Cut 2.7.0

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[7cfee8f1c8...](https://github.com/mrakgr/The-Spiral-Language/commit/7cfee8f1c8a1d76df2f83274a292b1fe09199fc4)
#### Tuesday 2022-03-29 18:35:29 by Marko Grdinić

"12pm. Got up late today as well. Let me chill first and I will get started with Substance after that. It turns out I got Mari and Substance in the end.

12:30pm. Breakfast time. Yesterday I caught up with Pandora in the Crimson Shell, and today I'll do it for some other US licensed follows like Murcielago, Black Company and Machimaho. I also haven't read the last volume of Gun Gale Online.

2pm. Done with breakfast and chores. Right now my stress is high, but I need to remind myself of my goals and just move forward.

Texturing. Once I master texturing I'll be able to get things done a lot faster. Let me start by installing Substance Painter.

2:10pm. Installed the Substance Painter, but for some reason it is not cracked. What the hell?

2:15pm. For some reason there is a backed up exe file inside the folder. The pirate site has no instructions, maybe I need to just overwrite the main using the backup?

I think that was really it, but it is now asking me to log into my account.

What a pest.

I can't create an account because it might not be secure.

...Ahhh, I should already have an Adobe account from the time I installed Illustrator.

2:25pm. The password I have stored in Chrome worked for me. Great. I am in Pt.

Now it is time for tutorials.

It is time to get good at this.

2:30pm. What is this thing about starting a free trial? What a pest. Very well. Let me start a free trial for now while I get a properly cracked version off CGPersia.

...I think I understand what is going on. Most likely, that backed up exe was in fact the original uncracked file. The cracked one just did not work.

...Right now I can't start the download due to the last two parts of Creative Shrimp's course being in progress. But if I just stick to getting two pieces a day I should be fine. The trial lasts 30 days an I am not in a hurry. This is just the perfect amount of time to master texturing.

2:35pm. https://substance3d.adobe.com/tutorials/courses/First-Steps-with-Substance-3D-Painter/youtube-mv6pg1O9vEQ

This looks really good. Let me watch it, then I'll try it out myself. If Illustrator is anything to go by, these tutorials should be good. But I really won't be satisfied unless I compare it to Mari properly. That video by FlippedNormal guys was convincing, but it is 3 years old. This is enough time for things to change.

3pm. This was interesting. This is a fairly simple way of texturing. Let me check out Mari.

https://learn.foundry.com/mari

Let me watch some of the stuff here.

https://learn.foundry.com/course/4147/view/beginner-s-guide-to-texturing-in-mari

Let me watch the teaser, I am not sure that I feel like watching hours off this off the bat.

3:05pm. No forget Mari. I like Pt's approach a lot more. I'll focus on it. I just took a glance to see whether Mari got better materials compared to 3 years ago, but it does not seem so.

Let me move to part 2 of that tutorial. I'll watch it from start to finish and then give it a try myself.

https://youtu.be/_wPuzlXjEfQ?t=46

Oh, these kinds of brushes are great.

3:25pm. Focus me, let me watch part 3.

I am looking what comes up in Youtube, and it is all stuff that would be super tedious to do by hand in 2d.

I need to go further. 3d really has come a long way thanks to these tools.

I am watching this video and thinking whether I could do the boot, and I could I can think of various ways to do it in fact.

Right now my skills aren't bad by any means.

I haven't practiced enough, but that has no hindered my comprehension in particular. Even if just stuck to 2d, I doubt I would have done too badly. But I want to reach the limit and push the tools to their full potential. Since I want that of course I would go into 3d.

3:30pm. Shrimp's course is done. Let me see if I can set the Painter to download.

3:35pm. 5 parts. It should be done by the end of tomorrow.

Some guy in the Houdini thread says he will give V-Ray a try. I think if he does the opposite of what I did and uses something like Substance to do all his texturing, he could work around about most of the buginess of V-Ray.

Let me suggest it to him as much.

3:45pm. Now focus me. Watch part 3. It is always difficult to work.

But after I learn texturing I should be ready.

https://youtu.be/iBgVVr5gIww?t=641

Oh, it has templates for specific renderers. No doubt Disney and Autodesk should be in there somewhere. V-Ray as well.

.fbx, .abc, .obj, .dae, .ply, .gltf

But no .usd.

> A new shader has been added, named Adobe Standard Material (ASM), which

Ah, the ASM was the Adobe stuff.

I am probably going to have to export the mesh as one of the supported formats.

Ok...

4:20pm. Let me take a break here.

4:40pm. I am back.

Let me try exporting as something other than obj.

4:50pm. I figured it out. For alembic to work I need to make sure to export face sets.

It seems that Pt does not work based on objects, but purely based on shader slots. Right now I have a problem because I assigned a bunch of different things to the same shader. Instead I need to assign a different shader for every object. That is the way to make progress here.

4:55pm. Ok, ok, ok...

Focus me. Let me just assign those slots to what they should be.

5:10pm. Assigned them.

It seems you do need to export the material when exporting to obj. That is fine.

5:20pm. Now focus me. What is the next step?

I am just letting it come to me. What I need to do now is come to an understanding of how to move around.

5:25pm. It seems I've reached my downlaod limit with Gator for today. Maybe if I am lucky Alfafile will allow me one more download and I'll be able to get part 5. I'll leave 3 & 4 for tomorrow regardless.

Right now, it is really hard for me to just dive in and start painting. Instead, why don't I watch the beginner's intro by FlippedNormals

The Mari one was really good and introduced me to how to move around. But the rollerblades tutorial for Pt is a bit too fast. It showed me a bunch of things, but not from the perspective of how to set everything up and move around.

Right now what I need is to get a handle on the UI and the absolute basics.. I'll want to figure out how to set up the lights to act as headlights to start things off.

https://youtu.be/RQ-hRk0WHJ8
Introduction to Substance Painter - Ultimate Beginners Guide

Let me go with this from the beginning.

Oh, there is a handy keyboard shortcut list in the description. I was wondering how to select texture sets.

https://youtu.be/RQ-hRk0WHJ8?t=72

Substance PBR guide.

https://substance3d.adobe.com/tutorials/courses/the-pbr-guide-part-1

Ok, let me read this.

5:55pm. > The base color map can be thought of as being somewhat flat in tonality. That is, its contrast is lower than that of a traditional diffuse map. It is inadvisable to have values that are too bright or too dark. Objects tend to be much lighter in tone than we remember them as being. We can visualize this range in terms of the darkest substance being coal and the brightest being fresh white snow. Coal is dark, but it is not 0.0 black. The color values we choose need to stay within a brightness range.

These guides are a snoozefest, but I should consider what they are saying.

5:55pm. Enough, enough, I can't stand these anymore. Why did they recommend I waste my time on these? Let me just move on.

https://youtu.be/RQ-hRk0WHJ8?t=121

I'll follow them along, except since I do not have their model, I'll just use my own desk.

https://youtu.be/RQ-hRk0WHJ8?t=268

He says there is no way to lock the light to the camera.

...I've Googled it and I can't find a way to do it.

https://boards.4channel.org/3/thread/886516

///

>>886516 (OP)
You're just wrong OP, substance painter uses a point cloud to record stroke positions then generates the texture based off that, this means you can completely change the UVs, reimport the file and substance will just recalculate it.

///

This is really interesting. It makes the tool much more useful.

6:25pm. https://boards.4channel.org/3/thread/889168

I made this thread to ask.

Let me get back on track.

Also, I've learned my lesson and replaced the Clip Studio shortcut so it runs the Clip Studio Paint instead. Having to go through hoops really makes opening CSP a lot longer. It get really annoying when croping screenshots and such, it feels like I need to wait half a minute for the program to open. Now it feels like it takes 10s.

...The post effects are turned off by default in the version I have. No problem.

https://youtu.be/RQ-hRk0WHJ8?t=343
> We don't actually have lights at all, we only have HDRIs.

https://youtu.be/RQ-hRk0WHJ8?t=559

Solo will be useful. This is a good tutorial.

7:20pm.

///

>>889169
Painter easily, unless you specifically want to make your own textures using a procedural node based system. Painter is like 3d Photoshop, so you can go far by layering existing ones. And it does not have just be static image textures, you still have access to procedural ones made in Designer that you can tweak.

///

Er, I won't answer this until I make sure. No let me. I am decently sure I am right with these statements.

Now that I am done with lunch, let me get back to the video.

7:35pm. My focus is low, it is always a mistake to watch videos while having fruit.

It turns out that I've hit the Alfafile limit so I'll have to leave the last two files for tomorrow.

7:40pm. Focus me for real. I'll go through the video from start to finish and call it a day.

https://youtu.be/RQ-hRk0WHJ8?t=1740

This is nice. I am wondering how normals could possibly be painted.

https://youtu.be/RQ-hRk0WHJ8?t=2402

This is cool.

8:25pm. I can't go on anymore. I will try putting what I've learned today into action tomorrow. I really have a lot of learning to do before I'll be effective at using Substance, but even so, spending at least a few weeks to get there is not too much for me. After I learn texturing I should be really good.

Yeah, there is always something else to learn, but once I crank up the conveyor belt, I am going to the pro level. I will not let anything stop me."

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[e288c801fd...](https://github.com/newstools/2022-express/commit/e288c801fdcf1ebc39e6ca75e5ee631980054d73)
#### Tuesday 2022-03-29 19:41:43 by Billy Einkamerer

Created Text For URL [www.express.co.uk/showbiz/tv-radio/1588150/top-boy-theory-jaq-girlfriend-beck-undercover-police-netflix]

---
## [sean9999/falert.js](https://github.com/sean9999/falert.js)@[6b6d7ccd1a...](https://github.com/sean9999/falert.js/commit/6b6d7ccd1ac37d033497c12b6da76f94fd8abba3)
#### Tuesday 2022-03-29 19:44:03 by Sean Macdonald

Merge branch 'master' of github.com:sean9999/falert.js

* 'master' of github.com:sean9999/falert.js:
  magick.church is my blog. Not brain.theater
  make the close button less ugly
  transparent background will hopefully solve a visual glitch
  improved README
  restrict distrubuted files to only those relevant
  remove demo from dist
  fixed incorrect CDN URL
  use publicUrl that tries to make the demo work on unpkg
  include static assets in build step
  build for various targets
  use native typescript

---
## [al-ptk/odin-dashboard](https://github.com/al-ptk/odin-dashboard)@[e1a80aa5cb...](https://github.com/al-ptk/odin-dashboard/commit/e1a80aa5cbf35e8693b63e497e33dd8dd2857010)
#### Tuesday 2022-03-29 20:12:44 by Alan Patrick

Add html full structure

    • I fucked up. I forgot to commit early and often. Big, big mistake.
    • A haiku for you:
    The dusk arrived.
    The skyes are yellow now.
    Life moves on.

---
## [fakegit/gimp](https://github.com/fakegit/gimp)@[7123b6c466...](https://github.com/fakegit/gimp/commit/7123b6c466dcf38bb274734e9d7494c9c4fd8b8e)
#### Tuesday 2022-03-29 20:56:27 by Jehan

Issue #7685: g-ir-doc-tool produces broken XML.

To work around the issue, I just wrote a stupid sed script. Of course,
it means that if we encounter again the issue on some other docs, we'll
have to update it. In other words, it's neither robust nor a proper
long-term fix. Just a temporary hack.
See: https://gitlab.gnome.org/GNOME/gobject-introspection/-/issues/425

Also fixing this issue, I encountered another bug, this time in meson,
which changes backslashes in slashes on 'command' arguments, in a
completely uninvited manner! The only workaround to this is apparently
to call an external script, which is ridiculous for such a basic stuff.
But well… here is why I implement this with a script, instead of
directly calling sed in the meson 'command'.
See: https://github.com/mesonbuild/meson/issues/1564

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[5522769378...](https://github.com/cockroachdb/cockroach/commit/5522769378eea814c85e4d22b839c6ff81f6f744)
#### Tuesday 2022-03-29 21:11:51 by craig[bot]

Merge #76776 #76793 #76835 #76901

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
Co-authored-by: sumeerbhola <sumeer@cockroachlabs.com>
Co-authored-by: Oliver Tan <otan@cockroachlabs.com>
Co-authored-by: Radu Berinde <radu@cockroachlabs.com>

---
## [CHOMPStation2/CHOMPStation2](https://github.com/CHOMPStation2/CHOMPStation2)@[e502b637e9...](https://github.com/CHOMPStation2/CHOMPStation2/commit/e502b637e9893a197cfa641cc5f03ede77a2860d)
#### Tuesday 2022-03-29 21:48:39 by Rykka

Trait Addition + Adjustments

Polaris Combat is ass.
Yes, bandaid trait fixes are not necessarily the solution, BUT!

All of our negatives have extreme versions, without any sort of positive counterpart, and the positives we DO have are weak.
However, a flat 50% reduction on both incoming burn/brute would be too much, therefore:

Trait changes as follows.
- Added Glass Endurance. You have 25 HP, or 50 total HP, before you die. Don't get hit, and with Baymissn't? You're a masochist.
- Brute/Burn Resists no longer exclude High/Very High Endurance.
- Major Burn/Brute Resist re-added: These provide a 40% DR (Damage Reduction), at the cost of 3 points. This is opposite to Major Weakness, which is a 50% incoming damage increase.
- Very High Endurance re-added: This increases your max HP to 150.
- Increased Pain Tolerance: Similar to Increased Pain INtolerance, you have a 40% DR on incoming pain, compared to, for Intolerance, a 50% increase on incoming pain.
- Lick Wounds added back as a 1-cost Positive trait. I wondered why I hadn't seen it - it'd been disabled for _two years_ since Jan 2020.

Now, this is very likely to be controversial as it's a VERY huge balance change. Please don't bite my head off - this came up in discussion with Serdykov in DMs, and after digging through PRs, I discovered that traits had been disabled/removed for 1-2 years.

Pending a rewrite of Polariscode combat, and/or significant tweaks to make it more palatable, this will allow for more tankiness in combat - at the cost of extreme downsides. You can't suddenly become a hulk in combat with just traits, you still have to take some heavy downsides.

For instance:
Base Points - 1
Total Traits - 8

Very High Endurance - 4
Major Burn Resist - 3
Major Brute Resist - 3
Increased Pain Tolerance - 3

Current Points -12
Current Traits Left - 4

Conductive Major - -3
Extreme Photosensitivity - -2
Haemophilia - -3
Major Loneliness - -5

Current Traits Left - 0
Current Points 1

I'd be interested in looking at making Major Brute/Burn resist 4 points to equal 40% incoming DR, but that feels odd, given the negative is 50% incoming damage total for only 3.
I'd also be open to considering making VH Endurance even more expensive to 6, since it can be taken simultaneously now, and making base High Endurance cost 4.

---
## [WaitingIdly/main](https://github.com/WaitingIdly/main)@[132f70b386...](https://github.com/WaitingIdly/main/commit/132f70b38666cf276dfffebd2c1230abadfc040f)
#### Tuesday 2022-03-29 21:57:55 by Atricos

Update 2.12.0

- Completely reworked the Mob Loot Fabricator (implemented by WaitingIdly). It's now available in Chapter 23 instead of 26 and it's much cheaper to build. The player can now choose to generate items from 18 different categories by inserting a "catalyst" item into its input slot. Instead of costing Mana, it now costs Life Essence to run. However one of the categories also generates Life Essence liquid back. It can also generate EvilCraft Blood, Vengeance Essence, Will, Gaia Spirits, DivineRPG Souls and boss drops, all Thaumcraft Vis Crystals, all Twilight Forest boss trophies, and more! Moved its quest to Chapter 23, explained the details there, and rearranged the Chapter.
- Updated version number and changelog.

---
## [WaitingIdly/main](https://github.com/WaitingIdly/main)@[197b4428c4...](https://github.com/WaitingIdly/main/commit/197b4428c49c6e5c2842ab88e56797e27c163a77)
#### Tuesday 2022-03-29 21:57:55 by Atricos

Update 2.13.0

Mod updates:

- AE2 Unofficial Extended Life v51d -> v51e (This fixes autocrafting not recognizing simulated returned items properly (like empty Buckets).)
- Replaced ReAuth 3.6.0 with OAuth 1.06.3. (This fixes not being able to relog with Microsoft accounts.)
- Added the Better P2P Mod. (This lets you see and find connected P2P tunnels in-world.) Also added a quest for it in Chapter 6.

Additions:

- Different tier EnderIO Conduits can now connect to each other.
- Pulsating Iron is now craftable in the Arc Furnace.
- Pereskia Bulbs can now also be used to make Plant Oil in the Squeezer.
- Added Hooves to the Mob Loot Fabricator Bewitchment output.

Fixes:

- Reverted the change from 2.11.0 that added Skyroot Planks to the plankWood OreDict. Now Skyroot Buckets are craftable again.
- The Mob Loot Fabricator Blood Magic recipe no longer incorrectly shows that it outputs LP.
- Fixed an issue where an empty Shulker Box that has been placed down and picked back up couldn't be upgraded into Iron Shulker Box.

Miscellaneous:

- Updated the Blood Altar link in the Chapter 17 Large Bloodstone Tile quest.
- Renamed the Chapter 3 Grove Stone quest and the Chapter 15 Cracked and Clean Runic Plate quests to avoid confusion.

---
## [RedDevilus/pcsx2](https://github.com/RedDevilus/pcsx2)@[8e5c3957ca...](https://github.com/RedDevilus/pcsx2/commit/8e5c3957ca41fb26f81a143a69331f01253c2cd3)
#### Tuesday 2022-03-29 22:00:17 by RedDevilus

GameDB: Serial with ':' to '-' + GS fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

---
## [oyeyipowale/black](https://github.com/oyeyipowale/black)@[7403d95862...](https://github.com/oyeyipowale/black/commit/7403d95862ae54c3504a8003666e1a0739067894)
#### Tuesday 2022-03-29 22:08:10 by Richard Si

Refactor docs / Maintenance of docs (#1456)

* Split code style and components documentation

Splits 'the_black_code_style', 'pragmatism', 'blackd',and 'black_primer'
into their own files. The exception being 'the_black_code_style' and
'pragmatism'. They have been merged into one 'the_black_code_style_and_pragmatism'
file.

These changes are being made because the README is becoming very long. And
a README isn't great if it dissuades its reader because of its length.

* Update the doc generation logic and configuration

With the moving of several sections in the README and the renaming of a
few files, 'conf.py' needs to be able to support custom sections.

This commit introduces DocSection which can be used to specify custom
sections of documentation. The information stored in DocSection will be
used by the process_sections function to read, process, and write the section
to CURRENT_DIR.

A large change has been made to the how the docs are prepared to be built.
Instead of just generating the files needed by reading the README, this
has a full chain of operations so custom sections are supported. First,
it reads the README and spits out a list of DocSection objects representing
the sections to be generated by process_sections. This is done since most
of the docs still live in README. Then along with the defined custom_sections
, the process_sections will be begin to process the DocSection objects.
It reads the information it needs to generate the section. Then fetches
the section's contents, calls processors required by the section to process
the section's contents, and finally writes the section to CURRENT_DIR.

This large change is so processing of the documentation can be done just
for the versions hosted on ReadTheDocs.org. An example processor using this
feature is a 'replace_links' processor. It will replace documentation
links that point to the docs hosted on GitHub with links that point to the
version hosted on ReadTheDocs.org. (I won't be coding that ATM)

This also means that files will be overwritten or created once the docs
have been built. It is annoying, since you have to 'git reset --hard'
and 'git clean -f -d' after each build, but there's nothing better. The old
system had the same side effects, so yeah :(

* Update filenames and delete unnecessary files

Update the filenames since 'the_black_code_style' and 'pragmatism' were
merged and 'contributing' was deleted in favor of 'contributing_to_black'.

All symlinks were deleted since their home (_build/generated) is no longer
used.

* Fix broken links and a few redirections

* Merge master into refactor_docs (manually done)

* Add my and most of @hugovk suggestions

Co-Authored-By: Hugo van Kemenade <hugovk@users.noreply.github.com>

* Add logging and improve configurability

Just some cleaning up up of the DocSection dataclass and added logging
support so you know what's going on.

* Rename a section and please the grammar gods of Black

Thanks @hugovk for the suggestion!

* Fix Markdown comments

* Add myself as an author :P

Seems like the right time.

Co-authored-by: Hugo van Kemenade <hugovk@users.noreply.github.com>

---
## [RedDevilus/pcsx2](https://github.com/RedDevilus/pcsx2)@[4876b4901b...](https://github.com/RedDevilus/pcsx2/commit/4876b4901b45e462f08752038d17d6c709d346f5)
#### Tuesday 2022-03-29 22:09:04 by RedDevilus

GameDB: Serial with ':' to '-' + GS fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur III

---
## [RedDevilus/pcsx2](https://github.com/RedDevilus/pcsx2)@[16a3b2f4b0...](https://github.com/RedDevilus/pcsx2/commit/16a3b2f4b02c674cf422e19488fadec4f0a90ba4)
#### Tuesday 2022-03-29 23:43:23 by RedDevilus

GameDB: Serial with ':' to '-' + GS fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Kuon
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

---
## [adampoulson/NoCheatPlus](https://github.com/adampoulson/NoCheatPlus)@[3695671d3b...](https://github.com/adampoulson/NoCheatPlus/commit/3695671d3bb71cfd425876c1e358e8753c281337)
#### Tuesday 2022-03-29 23:57:59 by Lysandr0

[Bleeding] Bunnyhop, bunnyfly, bug fixes.

Several/Major bunny adjustments (+ on the fly bug fixes)

1) Bunnyhop and slopes:
a) Let bunnyhop apply on yDistance
slopes (the jumping envelope is never hit: gravity hits harder here).
b) Grounded acceleration case (air-ground(landing), 0 hDist diff  ->
ground-ground,  0 hDist diff-> ground-ground, sudden mini burst of speed with no yDistance.
For this phase, we simply give players more momentum via bunnyhop ticks and increase speed slightly.
c) Continuous slope-jumping on ice will still fail  as speed  will keep increasing with each hop (Slime and normal ground seems fine)
d) Observed: edge case where bunnyfly speed decreases extremely little (in-air), thus, if the player has recently jumped up a slope and the hDist difference is small enough, the movement is allowed (should be confined more perhaps).

2) Get rid of that bloody sfOnIce legacy counter, at last.

3) Patch unintentional bypass with ice and headobstr.(bunnyhop -> drop speed below allowed to force set allowHop to true and to increase allowed friction speed -> bunnyhop again with higher speed (yOnGround case applies).

4) Cleanup, "simplify" (Where possible. Still too much spaghetti. Perhaps it's time for a rework :p).

5) Headbangbunny:
a) Don't wildcard; model should be decent enough now.
b) Observed: yet another case where clients can reach increasingly higher speed on ground: Touching ground in bunnyfriction with 0.3 speed -> ground-ground acceleration with 0.4 speed (bunnyhop) -> lifting off with increasing speed 0.5 (subsequent bunnyhop).

6) Hotfix for #171 : Allow bunny to consume the buffer.

7) Always clear hAcc on headbang.

8) On the fly:
a) sfVLTime -> sfVLMoveCount: we count moves, not time here.
b) Fix hopping right into a web (vertical).
c) Distinguish body in water VS body out of water when enforcing liquid->liquid speed limit: Magic has been warped for some time, how did we not get buried with reports about this !?
(Revert value to this commit: https://github.com/Updated-NoCheatPlus/NoCheatPlus/commit/c4331e1ffd4c7c17c43dba03f98f6feb875ada5b#diff-4adf02d4661b4aa4c5031880e2dd87200601581264a6d62eb56ce8c4b1606040 ).
d) Don't allow players to stand anywhere between minimum ground height and block height on ladders: fixes some fastladder bypasses (For @xaw3ep  is the Ground_Height flag still necessary? Seems like it's safe to remove)
Also slightly stricter climbable checking (step).

9) Move bunny stuff into its own workaround class (Coherence).

Missing:
1) Transitions stay problematic:
headobstructed -> head free / headobstructed on ice -> headobstructed on normal ground.

2) Bunnyhop while skimming over the edges of blocks. (video: https://www.dropbox.com/s/tdk1rdf9r3xwz5l/Edge_test.mov?dl=0 )
It does look like it's a problem with ice only (likely due to past moves being updated to not being on ice when touching the ground, the "lowjump problem" contributes as well).

3) Random setbacks when moving off from ice. Couldn't nail down the reason, let the buffer deal with this bullshit for now. Hopefully the higher modifier aids a little...

4) Hacc needs adjustments to take into account all illustrated cases.

5) Hop-after-velocity #171
Also applies when stopping to fly in air at high speed and falling. Looks like velocity isn't extended for long enough?

---

