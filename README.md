## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-28](docs/good-messages/2022/2022-08-28.md)


1,652,756 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,652,756 were push events containing 2,198,240 commit messages that amount to 118,803,590 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[6f2354e694...](https://github.com/timothymtorres/tgstation/commit/6f2354e694f3412a76b383f684a0bfc85a448d8e)
#### Sunday 2022-08-28 00:19:38 by san7890

Fixes Fucked Job Requirement Displays (#69368)

* Fixes Fucked Job Requirement Displays

Hey there,

I fucked up in #68856 (5b77361d399ba0dd992e61a16b9bbe38e8aa5a60). We weren't supposed to add another MINUTES multiplication here. I don't even remember why I did this if we are being perfectly honest with each other. Whoops.

fix: You should now no longer need thousands of hours to unlock your favorite head of staff role.

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[19cd1d18f6...](https://github.com/ammarfaizi2/linux-fork/commit/19cd1d18f6345e2acfa0c978d5e21aa009e49616)
#### Sunday 2022-08-28 00:51:08 by Johannes Weiner

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
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[5dc17bd865...](https://github.com/itseasytosee/tgstation/commit/5dc17bd86556c01cc0f81f54a6ce270169c00088)
#### Sunday 2022-08-28 00:58:56 by san7890

Security's Scaling Departmental Accesses - More Pop, More Problems (#68534)

lternative to #68527
About The Pull Request

Hey there,

This is an alternative PR that I concocted based on talking with Goof on that PR. Basically, we already have a nicely complicated system to track and balance the number of security officers we have in a shift based on some config coefficient setting, by which we can set the amount of lockers that spawn in on the start of a round, as well as determine truly how many security officers we have.

image

So, I've decided to leverage this in another way. Basically, based on the number of security officers in a shift, their specific departmental officers will also get more (elevated) accesses. They already start with a certain amount of access, but they can get more if it is a low-pop shift with the mechanic introduced in this PR. For example, an Engineering Security Officer can access Atmospherics and Engineering departments by default, but they can't access Telecommunications unless there is a lower population of players AT SHIFT START. Same for a Medical Security Officer accessing Medbay, but not Plumbing.

Update: I have made it such that there are three system that server operators can set:

They can use the Scaling System that operates in the same method outlined in the rest of the PR.
They can disable giving departmental security officers "elevated access" (such as access beyond the "front doors") to these officers.
Finally, they can also just always ensure that departmental security officers get the maximal accesses possible.

The default setting is the "Scaling System" outlined in this PR, which is already dependent on the general Security Officer Scaling Co-Efficient.
Why It's Good For The Game

I think it's better to involve some more nuanced config scaling that we already have present in the game. The major theme that we want to avoid is that departmental security officers having maximal accesses when there is an already large number of persons on the security force will result in "miserable" shifts for the common person working within a department (security metaprotections). However, some server operators (as well as server cultures) tend to have very wide ranges in how many security officers they have on a shift-by-shift basis. One day, you could have 0-2 security officers, the next, you could have 4-6. It's all variable on who's playing (as always). There is also a significant variation between server to server in regards to how many security officer slots you tend to have on spawn, but this is already manageable by the security officer co-efficient in config.

I believe this PR is an acceptable proposal within the bounds of #68527 (comment) , although it may bend certain aspects of it, I definitely do see where some people may be coming from. I believe I've adjusted the accesses to a "sane"/justifiable amount, but I'll come back to think on everything.

"Red-tiding" may or may not be a problem, but there's always just going to be something inherently silly with a security officer being able to walk into plumbing to start plumbing. I hoped that this would be seen as a positive as opposed to a negative, but I can see how it could negatively impact player experience. HOWEVER, interplayer experience should not be handled by the codebase in all aspects, which is why I've also passed in the associated config variables, so that server operators (who should handle the interplayer experience with their level of discretion and nuance) can.
What accesses are where?

The general philosophy as I thought through designing this would be that the security officer should at the very least have general "front-door" access into a department, and maybe something benign. If we had even more per-door accesses, this could definitely be a bit more granular (one example I can think of would only atmospherics technicians having access to the "Pump Room", while Security Officers would not. However, this is for a later date). So, you have the "default" access you always get, and a potential to get "elevated" access as a Departmental Security Officer.

The balances are as such:

The Cargo Security Officer will have access to the Cargo Bay, Mining Section, and the Shipping Room. The first two are rather general areas, with the Shipping Room being a rather good help for rescuing (or "rescuing") flushed crewmembers when the cargo techies can't get to it/no AI. The Auxiliary Base is not essential to the security officer's functions, and the mining station helps restrict access further on stations like IceBox. This would also grant them extra access to the Lavaland base, so let's snip that out.

The Engineering Security Officer should have access to only general Engineering and Atmospherics. Construction pertains to certain rooms in maintenance I believe, and Engine-Equipment should be the one that grants access to APCs (lol). I don't think a security officer should have the latter one to be honest, but I think we'll be stretching the scope of this PR. Telecommunications is a bit weird, it's a critical station function, but I think you also shouldn't be able to nick one goon's ID and have access, so let's give it to them only when it's "needed".

The Medical Security Officer should have access to only the general Medbay Area and the Morgue, in case someone starts trotting on the doctor's turf, or if there's someone doing unsavory things to the bodies while the doctors are away. They will not have access to the specialized (dangerous) areas unless the ratio of secoffs to the population is low enough should it necessitate it (Plumbing Room, Pharmacy, Virology). I also added Surgery to the scaling access, but I'm iffy on that one. I don't particularly see why they should have it as a base access, but I also do see there being some need in dire straits (in relation to helping people, not tiding).

The Science Security Officer definitely got a huge cut. They now only have general access to R&D and normal scientist areas like the lathe room, circuits lab (presumably)since these are generally trafficked areas, but I definitely clamped down on additional access they might get in a "normally balanced" situation (no ordnance+storage, no xenobio, no genetics, no to robotics, etc.) They don't have a particular use in these areas and can even be a bit obstructive to flow in normal circumstances, but if abnormal circumstances arise and there's not a lot of security hands-on-deck, then their access is expanded.

Honestly, balancing this both makes sense and is conversely rather odd. I'm just running off what we already hold to be true and expected (or at least as of the last two months), and we can go from there.
Changelog

cl
balance: Nanotrasen realized that the more access they had on their cards was costing them a pretty penny, so they trimmed back the number of accesses a certain departmental Security Guard might have. However, any given guard will get back a greater amount of accesses depending on how many security guards there are in relation to the population.
config: Hey server operators, listen! We've changed up how Departmental Security Officers get their accesses, so be sure to review the DEPSEC_ACCESS_LEVEL config number to see what you want to work best for your server.
/cl

Also, every single line of code found in 4533f07 that is now presently in this PR is deliberate

---
## [DEVBOX10/WindowsTerminal](https://github.com/DEVBOX10/WindowsTerminal)@[9ccd6ecd74...](https://github.com/DEVBOX10/WindowsTerminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Sunday 2022-08-28 01:06:14 by Mike Griese

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
## [TaleirOfDeynai/nai-context-userscript](https://github.com/TaleirOfDeynai/nai-context-userscript)@[c41cba3677...](https://github.com/TaleirOfDeynai/nai-context-userscript/commit/c41cba3677d982bf021632d8e571e5bb6a3ad41e)
#### Sunday 2022-08-28 01:11:17 by Taleir of Deynai

WIP of end-user configuration.

God damn, does this look ugly as hell...  I dunno what I can do about the styling, considering the restylable UI NovelAI has.  I'm reluctant to just use their React modules, though that is something I'm kitted to do...
Also, testing is completely busted with this `GM_config` thing at the moment, because it just uses the DOM as soon as it loads and the DOM doesn't exist in the test environment.

---
## [GrinZero/react](https://github.com/GrinZero/react)@[b6978bc38f...](https://github.com/GrinZero/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Sunday 2022-08-28 01:54:19 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [duoertai/cadence](https://github.com/duoertai/cadence)@[add4b390ad...](https://github.com/duoertai/cadence/commit/add4b390ada43fdd8167f06e209ae6ece0d11aaa)
#### Sunday 2022-08-28 03:09:33 by Steven L

Standardizing cancellation behavior: a canceled workflow never starts a new run (#4898)

# Summary for busy people

Workflow cancellation was kinda weird and confusing, and left some awful, unrecoverable, and un-*preventable* edge cases (particularly with child workflows).  It also left users with no way to reliably stop work, aside from termination.  Termination is inherently "unclean" and risky, so it should not be required to achieve something outside exceptional circumstances where recovery is not possible.

This commit changes that: cancellation is now "sticky", and a canceled workflow does not ever trigger a new run after it completes, regardless of how it completes, so it can be used as a reliable "stop processing after cleanup" tool.  The final state of a canceled workflow's run is now *always* a successful completion with a value, canceled, or timed out. (termination remains always "terminated")  
A canceled workflow can still start and abandon child workflows, so all current behavior with retries / continue as new / etc can be replicated with child workflows if desired.

A fair bit of (not very complex) additional work here and in nearly all other repos is required to truly complete this, but it is *functional* and non-optional with this commit alone.  
In particular, adding a dynamic config to (temporarily!) restore old behavior should be fairly easy if it proves to be needed.

# More details and motivation

Part 1 of [many, tbd, in multiple repos] involved in changing workflow cancellation to reliably end workflows.
Tests will be coming soon, for now I'm using a fairly simple set of workflows and checking the resulting histories exhaustively by hand.

The primary motivation for these changes is to address some impossible-to-recover-from scenarios when canceling child workflows.  After further exploration and discussion we've realized that, without these changes, there is *no reliable way* to stop a sequence of workflows without relying on termination, which we consistently treat as a fallback / impure-but-necessary ultimate hammer.

Workflows should not *need* to rely on termination to achieve a desired behavior.  With these changes, cancellation becomes capable of *guaranteeing* that workflows end within some finite time, which is a unique ability and makes it much more consistent and reliable.  
Turning this into a "complete" change will require quite a few tests, documentation changes, client-side changes (to allow recording more info, and likely changing test suites), and some smallish database and maybe RPC changes (to hold/return more data in cancellation errors).

We are also not currently planning on making this configurable.  It's seen as a correction of an under-specified and somewhat flawed chunk of behavior, more than "a change".  
Existing workflows will not experience replay errors, but it is still a substantial *semantic* change, though from what we have seen cancellation is relatively rarely used (partly due to its complex behavior).  If issues are encountered / if users end up needing it, it should be fairly easy to add a per-domain/tasklist/workflow type configuration value, but it will be opt-*out*, not opt-*in*.

# What was happening

Previously, workflow behavior on cancellation was pretty frequently surprising to our users, arguably inconsistent, and not very well documented:

| **PREVIOUS**  | **simple**               | **retry**                                 | **cron**                                | **retry+cron**                                    |
|--------------:|--------------------------|-------------------------------------------|-----------------------------------------|---------------------------------------------------|
| **success**   | success                  | success                                   | success<br>continue cron<br>cron        | success<br>continue cron<br>cron<br>retry         |
| **cancel**    | canceled                 | canceled                                  | canceled                                | canceled                                          |
| **retryable** | (n/a, fatal)             | continue retry<br>retry<br>recorded error | (n/a, fatal)                            | continue retry<br>cron<br>retry<br>recorded error |
| **fatal**     | failed<br>recorded error | failed<br>recorded error                  | continue cron<br>cron<br>recorded error | continue cron<br>cron<br>retry<br>recorded error  |
| **continue**  | continue immediately     | continue immediately<br>retry             | continue immediately                    | continue immediately<br>retry                     |
| **timeout**   | timeout                  | continue retry<br>retry<br>recorded error | continue cron<br>cron<br>recorded error | continue retry<br>cron<br>retry<br>recorded error |

A legend is:
- success / etc shows the final state of the canceled run (success = completed with a value that can be retrieved)
- "continue X" covers what source is used to compute the next run's starting delay (cron, retry, or no delay)
- "cron" / "retry" shows whether or not cron/retry configuration is carried over to the new run
  - note that cron is lost by default with continue-as-new
- and "recorded error" is whether or not the returned error is saved in its entirety (type + reason + details)

This largely summarizes as "cancellation works when you end with the canceled-context error", say from `ctx.Err()`, otherwise it behaves like normal (or nearly) and many scenarios will start a new run.
That's somewhat reasonable, but it's fairly "fragile" (it depends on what you return, and there are *many* ways for code to return some other error), and most importantly it means *there is no reliable way to stop a workflow* except to terminate it.

That has severe consequences in at least two scenarios:
1. When termination is *unsafe*
2. When a parent workflow cancels a child by canceling its context

For 1, for manual cancellations it's potentially reasonable to just terminate a run that begins after a successful cancel... but in principle if you're using cancellation it implies that termination is *not* desired, and potentially not safe to do.  Canceling may result in a brand new run that immediately starts new behavior, leaving you with no safe window to terminate and not leave bad state lingering.  
So users wanting a safe way to stop a sequence of workflows have no reliable way to do so.

For 2, it puts parent+child workflows in an extremely awkward, and essentially unrecoverable scenario.  Cancellation is a *one time event*, and as far as the parent is concerned, if the child/its context is canceled, the child is canceled...  
...but if the child then starts a new run for *any* reason (retry, cron, reset, etc), that new run is no longer canceled.  The parent has no way to know this has happened, and has no way to *re*-cancel the new child, so it can easily lead to the collection of workflows getting into an impossible state that it never recovers from.

Both cases are able to lead to unreliable behavior which can only use termination to stop, and for which no "safe" option exists.

After reviewing some customer issues and desires and thinking about things, we've settled on "cancel should guarantee that things stop".  Not necessarily in a timely manner, but that's fine.  And if a workflow wants to run behavior longer or larger than its current run can achieve, it has a workaround: start a new (likely child) workflow to do the cleanup.

# What happens now

So that's what this PR does, in a minimal / to-be-polished way so we can start running it for our stuck users while we flesh out tests and change other behaviors.

Currently that means our cancellation behavior is now:

| **CURRENT**    | **simple**                                | **retry**                                 | **cron**                                  | **retry+cron**                            |
|--------------:|-------------------------------------------|-------------------------------------------|-------------------------------------------|-------------------------------------------|
| **success**   | success                                   | success                                   | success                                   | success                                   |
| **cancel**    | canceled                                  | canceled                                  | canceled                                  | canceled                                  |
| **retryable** | (n/a, fatal)                              | canceled<br>recorded error (details only) | (n/a, fatal)                              | canceled<br>recorded error (details only) |
| **fatal**     | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) | canceled<br>recorded error (details only) |
| **continue**  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  | canceled<br>(no details)                  |
| **timeout**   | timeout                                   | timeout                                   | timeout                                   | timeout                                   |

And the new "details" entries cover whether or not an error's "details" (the custom encoded data, not reason or type) are saved.  Unfortunately the current cancellation event (and clients' API) does not allow recording all data, or any in some cases, so the original reason/message and error type are lost and are replaced with a canceled error.

Now, cancellation *always* ends workflows with the current run.  Returning a value will return that value, including in cron scenarios, timeouts are still timeouts (and they imply a possibly un-clean termination), and _all_ errors or attempts to continue-as-new will instead result in a canceled state.

# Future changes to make to finish this effort

With further changes to the clients and RPC/storage models, canceled errors will store more details about what was returned.  E.g. continue-as-new does not record what was *attempted* to be started, and other error types lose their "reason" (i.e. the message) and type but not details.  Pretty clearly this is sub-par, and we should be capable of reporting the actual return in full so it can be retrieved if needed.  This is also why returning a value now always ends in a completed state, so successful completions do not lose those values.

Prior to merging into master / a release, we may end up making this configurable (likely with a default of opt-out), to address both the sub-par information recording and the semantically-breaking behavior change.  Docs changes are also due, as well as some integration tests, client library changes (e.g. to make sure the test suite reflects the new behavior), etc.

Another gap to plug is that resetting a workflow does not "forward" the canceled state to the new run.  We should probably be treating cancellation like we do signals: cancel the new run if the current run is canceled.  This will ensure that you can reset a child and retain the parent's cancellation, so it'll very likely become the default behavior, but we'll allow overriding it.  Resets are manual actions, they can break the rules if desired.  And they can just manually cancel later if they decide they do want it.

And last and perhaps least: it's quite strange that continue-as-new does not retain cron config.  At least from the Go client.  I suspect it's just not adding to / pulling from the context correctly.

---
## [benluo/docs.scala-lang](https://github.com/benluo/docs.scala-lang)@[8cb441957d...](https://github.com/benluo/docs.scala-lang/commit/8cb441957d96d6de21a7e3ed38d8156df4a20883)
#### Sunday 2022-08-28 03:09:49 by Martijn Hoekstra

Remove joke

When you're trying to understand something, jokes are never funny

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[67c060f3ed...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/67c060f3edb62d157dcccbca2139b1949b723d89)
#### Sunday 2022-08-28 08:11:14 by petrero

25 Command: Autowiring & Interactive Questions

  Last chapter team! Let's do this!

  Ok, what if we need a service from inside our command? For example, let's say that we want to use MixRepository to print out a vinyl mix recommendation. How can we do that?

  Well, we're inside of a service and we need access to another service, which means we need... the dreaded dependency injection. Kidding - not dreaded, easy with autowiring!

  Add public function __construct() with private MixRepository  to create and set that property all at once.

  Though, if you hover over __construct(), it says:

    Missing parent constructor call.

  To fix this, call parent::__construct()

  This is a super rare situation where the base class has a constructor that we need to call. In fact, this is the only situation I can think of in Symfony like this... so not normally something you need to worry about.

  Interactive Questions
  - Down here, let's output a mix recommendation... but make it even cooler by first asking the user if they want this recommendation.

  We can ask interactive questions by leveraging the  object. I'll say if ($io->confirm('Do you want a mix recommendation?'))

  This will ask that question, and if the user answers "yes", return true. The $io object is full of cool stuff like this, including asking multiple choice questions, and auto-completing answers. Heck, we can even build a progress bar!

  Inside the if, get all of the mixes with $mixes = $this->mixRepository->findAll(). Then... we need just a bit of ugly code - $mix = $mixes[array_rand($mixes)] - to get a random mix.

  Print the mix with one more $io method $io->note() passing I recommend the mix and then pop in $mix['title']

  And... done! By the way, notice this return Command::SUCCESS? That controls the exit code of your command, so you'll always want to have Command::SUCCESS at the bottom of your command. If there was an error, you could return Command::ERROR.

  Tip

    Whoops, the correct constant name if the command fails is Command::FAILURE!

  Okay, let's try this! Head over to your terminal and run:

    php bin/console app:talk-to-me --yell
  We get the output... and then we get:

    Do you want a mix recommendation?

  Why, yes we do! And what an excellent recommendation!

  All right, team! We did it! We finished - what I think is - the most important Symfony tutorial of all time! No matter what you need to build in Symfony, the concepts we've just learned will be the foundation of doing it.

  For example, if you need to add a custom function or filter to Twig, no problem! You do this by creating a Twig extension class... and you can use MakerBundle to generate this for you or build it by hand. It's very similar to creating a custom console command: in both cases, you're building something to "hook into" part of Symfony.

  So, to create a Twig extension, you would create a new PHP class, make it implement whatever interface or base class that Twig extensions need (the documentation will tell you that)... and then you just fill in the logic... which I won't show here.

  That's it! Behind the scenes, your Twig extension would automatically be seen as a service, and autoconfiguration would make sure it's integrated into Twig... exactly like the console command.

  In the next course, we'll put our new superpowers to work by adding a database to our app so that we can load real, dynamic data. And if you have any real, dynamic questions, we are here for you, as always, down in the comment section.

  All right, friends. Thanks so much for coding with me and we'll see you next time.

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[409531f58b...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/409531f58b10ce4b54c5ac47188d19fa7485db48)
#### Sunday 2022-08-28 08:11:14 by petrero

20.2 Environment Variables - Moving Authorization Header to framework.yaml

  Moving Authorization Header to framework.yaml
  - So this is cool! But it would be nicer if the service came preconfigured to automatically set this authorization header... especially if we want to use this HTTP Client service in multiple places. Can we do that? You bet!

  Copy the Token line, head into framework.yaml, and after base_uri, pass a headers key with Authorization set to our long string. Actually, let me put a fake token in there temporarily

  Back in MixRepository, remove that third argument

  And now, when we try this... great! Things are broken, which proves we're sending that header... just with the wrong value. If we change to our real token... once again... it works! Awesome!

  Hello Environment Variables
  - So far, this is just a nice feature of the HttpClient. But this also helps highlight a common problem. It's... not super great to have our sensitive GitHub API token hardcoded in this file. I mean, this file is going to be committed to our repository. I love my teammates... but I don't love them so much that I want to share my access token to with them... or the access token for our company.

  This is where environment variables come in handy. If you're not familiar with environment variables, they're variables that you can set on any system (Windows, Linux, whatever.)... and then you can read them from inside of PHP. Many hosting platforms make it super easy to set these. How does that help us? Because, in theory, we could set our access token as an environment variable then simply read it in PHP. That would let us avoid putting that sensitive value inside our code.

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[8a6f39ed7c...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/8a6f39ed7c1c8170b639b3e5dd5ad06692bd59c7)
#### Sunday 2022-08-28 08:11:14 by petrero

21.1 The Secrets Vault - bin/console secrets:set GITHUB_TOKEN

  I don't want to get too far into deployment, but let's do a quick "How To Deploy Your Symfony App 101" course. Here's the idea.

  Deployment 101
  - Step 1: You need to somehow get all of your committed code onto your production machine and then run

    composer install
  to populate the vendor/ directory.

  Step 2: Somehow create a .env.local file with all of your production environment variables, which will include APP_ENV=prod, so that you're in the prod environment.

  And Step 3: run

    php bin/console cache:clear
  which will clear the cache in the production environment, and then

    php bin/console cache:warmup
  to "warm up" the cache. There may be a few other commands, like running your database migrations... but this is the general idea. And the Symfony docs have more details.

  By the way, in case you're wondering, we deploy via https://platform.sh, using Symfony's Cloud integration... which handles a lot of stuff for us. You can check it out by going to https://symfony.com/cloud. It also helps support the Symfony project, so it's a win-win.

  Use Real Environment Variables When Possible
  - Anyway, the trickiest part of the process is Step 2 - creating the .env.local file with all of your production values, which will include things like API keys, your database connection details and more.

  Now, if your hosting platform allows you to store real environment variables directly inside of it, problem solved! If you set real env vars, then there is no need to manage a .env.local file at all. As soon as you deploy, Symfony will instantly see and use the real env vars. That's what we do for Symfonycasts.

  Creating .env.local During Deploy?
  - But if that's not an option for you, you'll need to somehow give your deployment system access to your sensitive values so that it can create the .env.local file. But... since we're not committing any of these values to our repository, where should we store them?

  One option for handling sensitive values is Symfony's secrets vault. It's a set of files that contain environment variables in an encrypted form. These files are safe to commit to your repository... because they're encrypted!

  Creating the dev Vault
  - If you want to store secrets in a vault, you'll need two of them: one for the dev environment and one for the prod environment. We're going to create these two vaults first... then I'll explain how to read values out of them.

  Start by creating one for the dev environment. Run:

   php bin/console secrets:set
  Pass this GITHUB_TOKEN, which is the secret we want to set. It then asks for our "secret value". Since this is the vault for the dev environment, we want to put something that's safe for everyone to see. I'll explain why in a moment. I'll say CHANGEME. You can't see me type that... only because Symfony hides it for security reasons.

  Since this is the first secret we've created, Symfony automatically created the secrets vault behind the scenes... which is literally a set of files that live in config/secrets/dev/. For the dev vault, we're going to commit all of these files to the repository. Let's do that. Add the entire secrets directory:

    git add config/secrets/dev
  Then commit with:

    git commit -m "adding dev secrets vault"

  The Secrets Vault Files
  - Here's a quick explanation of the files. dev.list.php stores a list of which values live inside the vault, dev.GITHUB_TOKEN.28bd2f.php stores the actual encrypted value, and dev.encrypt.public.php is the cryptographic key that allows developers on your team to add more secrets. So if another developer pulled down the project, they'll have this file... so they can add more secrets. Finally, dev.decrypt.private.php is the secret key that allows us to decrypt and read the values in the vault.

  As soon as the vault files are present, Symfony will automatically open them, decrypt the secrets, and expose them as environment variables! But, more on that in a few minutes.

  Storing the dev Decrypt Key?
  - But wait: did we really just commit the decrypt key to the repository? Yes! That would normally be a no-no! Why would you go to the trouble of encrypting values... just to store the decryption key right next to them?

  The reason we're doing exactly that is that this is our dev vault, which means we're only going to store values that are safe for all developers to look at. The dev vault will only be used local development... and we want our teammates to be able to pull down the code and read those without any trouble.

  Ok, at this point we have a dev vault that Symfony will automatically use in the dev environment. Next: let's create the prod vault, which will hold the truly secret values. We'll then learn relationship between vault secrets and environment variables... as well as an easy way to visualize all of this.

---
## [buahaha/free-programming-books](https://github.com/buahaha/free-programming-books)@[97016edd67...](https://github.com/buahaha/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Sunday 2022-08-28 08:40:12 by David Ordás

Add CodingFantasy's CSS coding interactive games (#5490)

* Add "Knights of the Flexbox table" game

Welcome to the Knights of the Flexbox table. A game where you can help Sir Frederic Flexbox and his friends to uncover the treasures hidden in the Tailwind CSS dungeons.
You can navigate the knight through the dungeon by changing his position within the dungeon using Flexbox and Tailwind CSS.

* Add "Flex Box Adventure" game

Once upon a time, there was a King Arthur. He ruled his kingdom fair and square. But Arthur had one problem. He was a very naive person. So one sunny day, three alchemist brothers offered Arthur to exchange all his Gold Coins for coins made of a more valuable new metal that they had invented - Bit Coins.

Arthur believed them and gave them all his gold. The brothers took the gold and promised to give the bit coins back to Arthur in seven days.

Seven days passed. The brothers have not turned up. Arthur realized he had been scammed. He is angry and intends to take revenge on them. Let's help him do it with our weapon – CSS Flex Box!

We made this game for You
1. You often stumble and try to figure out which combination of Flex Box properties makes the browser do what you want it to do.

2. You want to create complex web layouts without constantly looking at the web page after every Cmd/Ctrl+S press in the code editor.

3. You have tried to learn Flex Box with video tutorials and articles but still don't fully understand how some parts of it work.

4*. Or, if you are a master of CSS Flex Box, we have something interesting and for you too (read further).

Have you found yourself there? Then you definitely want to learn or improve your Flex Box skills. So we have good news for you, really good news...

Learn Flex Box by Playing Game
No more boring videos, tutorials and courses. Learn Flex Box in a completely new, fun, effective and revolutionary way. By playing Flex Box coding game!

* Add "Grid Attack" coding game

In an ancient Elvish prophecy, it was said that one day a man would be born with an incredible power that predicts the future – "Marketi Predictori." And another will come to take this power. But the years went by and nothing happened. Until one day, a little elf was born. He was named Luke.

From an early age, he surprised his parents and his sister Rey by guessing the price of apples at the farmer's market before they even reached it. Every year his power rose and his predictions became more and more accurate. But there was one thing Luke could not predict. The coming of the demon Valcorian. It was the one from the prophecy that was to come and take Luke's power. One day Valcorian and his army attacked the town where Luke had lived and kidnapped him to make a ritual of stealing his power.

Go on a dangerous quest with Luke's sister Rey and find her brother. Defeat Valcorian and all his demons using a secret weapon – CSS Grid.

We made this game for You?
1. You often stumble and try to figure out which combination of Grid properties makes the browser do what you want it to do.

2. You are scared by the number of properties a CSS Grid has, and you feel uncomfortable when you need to create a grid layout.

3. You want to create complex web layouts using Grid, but without constantly looking at the web page after every "Cmd/Ctrl+S" press in the code editor.

4. You have tried to learn CSS Grid with video tutorials and articles but still don't fully understand how some parts of it work.

5. You use a Flex Box where Grid is required because you don't feel confident in using it.

Have you found yourself there? Then you definitely want to learn or improve your Grid skills. So we have good news for you, really good news...

Learn Grid by Playing CSS Game
No more boring videos, courses and articles. Learn Grid in a revolutionary new, fun, and effective way. By playing a Grid coding game!

---
## [BSCPGROUPHOLDINGSLLC/BLOCK-REPO-4](https://github.com/BSCPGROUPHOLDINGSLLC/BLOCK-REPO-4)@[1d9c10f2eb...](https://github.com/BSCPGROUPHOLDINGSLLC/BLOCK-REPO-4/commit/1d9c10f2eb4273a27d14156dc1893f9df0669053)
#### Sunday 2022-08-28 10:17:56 by 1212-5858

USC 26- Gross Negligence of their Taxes - amounts to the greater of $250 million (under the Sarbanes-Oxley) covers what the prosecutors need.

<h3>Securities Fraud</h3>

<a href="https://github.com/BSCPGROUPHOLDINGSLLC/AIDED-LIKE-BERNIE/raw/main/2020_05_27%20-%20INDEX%20and%20PAPERS.pdf">INDEX 5 - LINK TO ALL EMAIL COMMUNICATIONS</a>

<hr>

<h3>Bank Fraud</h3>

<p><a href="https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=R9aac7D6DBJZ1wsiq0b38A==">DOCKET 166 - FILED IN NYSCEF 153974 2020</a></p>

<p><a href="http://ic3bbohit.pythonanywhere.com/aboutEvidence/title18-21/">http://ic3bbohit.pythonanywhere.com/aboutEvidence/title18-21/</a></p>

<h3>VIOLATION OF PRIVACY</h3>

<p><a href="https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5">https://github.com/BSCPGROUPHOLDINGSLLC/ELSER-AND-DICKER/pull/5</a></p>

<h2>TAX EVASION: GROSS NEGLIGENT PENALTY APPLIED (70% onto ROUGHLY $250 MILLION) carry-forward 10-years and for 6 properties</h2>
*** you can not purchase 144 apartments for less than $25 million dollars, even in a fire sale in Manhattan in the Year 2022.
*** you can not base-cap a property without a means to legally collect rent, and report that as lawful income to the NY FINANCE REGISTER
*** this is the information that was used in order for the Sullivan / Zucker DYNASTY to obtain a $6 million dollar loan from State Farm Life Insurance Company at the height of the COVID-19 pandemic, and assign all of their tax liabilities to the funny farm or evasion while they were executing a fine in New York, had no issues undermining the USDOJ, FINRA, or the SEC while placing ALL of their whole life and term life policy holders at risk.
*** upon receipt of a letter, stating those TAXES would cause harm - State Farm agreed to immediately pay whatever balance they felt would be in the interest of their shareholders.
*** below, the impossible rent rolls and ponzi scheme, for the USDOJ and NYSD to evaluate and understand, they can only be valued as individual units.
*** for gross negligence, see also the shift in the fed-30 during the 4th quarter of 2021 - roughly 300bps

<h4>GOCARDS</h4>
<p><a href="https://github.com/users/BSCPGROUPHOLDINGSLLC/projects/1">https://github.com/users/BSCPGROUPHOLDINGSLLC/projects/1</a></p>

<hr>

EOF

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[7f1e527afa...](https://github.com/wrye-bash/wrye-bash/commit/7f1e527afa9047dac3cb05788d9d1d8a3a90cce4)
#### Sunday 2022-08-28 10:39:02 by Infernio

Rework the Mods tab's context menu RRR

You now what really doesn't help the first time user experience?
Throwing a giant context menu in their face. Sometimes people report
they can't find the Rebuild Patch option even though it's right there -
almost certainly because in order to find it, their eyes have to scan
through up to *twenty-eight* menu items.

This commit brings a similar refactoring to what we did to the
Installers tab to the Mods tab as well. There are now only twelve
top-level items, exposing the most commonly used features (e.g. Rebuild
Patch, Move to, Jump to Installer, etc.) at the top level and placing
the less commonly used features in sub-menus (Info and Plugin, in this
case - plus an Advanced menu for the weird shit:tm:).

Note 'Export Patch Configuration' getting dropped entirely - you can
already do that via Rebuild Patch... > Export, plus it was confusing
that you could export like this but not *import* that way. And on top of
all that, it would have lead to unintuitive UI with the new context
menu, since I would have either had to move it to Plugin.. or kept such
a rarely used command at top level.

Didn't update the docs for this because they also haven't been updated
for the latest Installers changes yet and I want to do all that in one
go with updated images and all.

Closes # 643 <--- RRR

---
## [xdroid-oss/xd_frameworks_base](https://github.com/xdroid-oss/xd_frameworks_base)@[438a2c8278...](https://github.com/xdroid-oss/xd_frameworks_base/commit/438a2c82785c2fd4d7fe2b2e6de6c91e844899ab)
#### Sunday 2022-08-28 11:56:03 by Joey Huab

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

---
## [FurryMrNuts/sillycathax](https://github.com/FurryMrNuts/sillycathax)@[a66044468c...](https://github.com/FurryMrNuts/sillycathax/commit/a66044468c0fa8137254050b94ae60b5a868b8bd)
#### Sunday 2022-08-28 12:03:11 by FurryMrNuts

Update script.lua

fuck you aflac im obfuscating the script

---
## [majestrate/loki-network](https://github.com/majestrate/loki-network)@[760324563f...](https://github.com/majestrate/loki-network/commit/760324563f4947a056281247764eb09c5dc7995f)
#### Sunday 2022-08-28 12:31:37 by Jeff

tweaks for wine and yarn for gui

* allow specifying a custom yarn binary for building the gui using -DYARN= cmake option
* unset DISPLAY when calling wine because i hate popups
* do not rebuild gui when building for windows
* by setting the magical undocumented env var USE_SYSTEM_7ZA to 'true' we can have the pile of npm bullshit code use our system's local 7z binary instead of the probably not backdoored binary from npm, yes for real. i hate nodejs so god damn much you have no fucking idea
* allow providing a custom gui from a zip file via -DGUI_ZIP_FILE cmake option

---
## [krbfx/rkicons](https://github.com/krbfx/rkicons)@[a16c67dd69...](https://github.com/krbfx/rkicons/commit/a16c67dd69a1510d900fed212c43353a976dfa09)
#### Sunday 2022-08-28 13:59:06 by DarkPlayer

rkicons: add burger king icon

Number 15: Burger king foot lettuce. The last thing you'd want in your Burger King burger is someone's foot fungus. But as it turns out, that might be what you get. A 4channer uploaded a photo anonymously to the site showcasing his feet in a plastic bin of lettuce. With the statement: "This is the lettuce you eat at Burger King." Admittedly, he had shoes on.

But that's even worse.

The post went live at 11:38 PM on July 16, and a mere 20 minutes later, the Burger King in question was alerted to the rogue employee. At least, I hope he's rogue. How did it happen? Well, the BK employee hadn't removed the Exif data from the uploaded photo, which suggested the culprit was somewhere in Mayfield Heights, Ohio. This was at 11:47. Three minutes later at 11:50, the Burger King branch address was posted with wishes of happy unemployment. 5 minutes later, the news station was contacted by another 4channer. And three minutes later, at 11:58, a link was posted: BK's "Tell us about us" online forum. The foot photo, otherwise known as exhibit A, was attached. Cleveland Scene Magazine contacted the BK in question the next day. When questioned, the breakfast shift manager said "Oh, I know who that is. He's getting fired." Mystery solved, by 4chan. Now we can all go back to eating our fast food in peace.

---
## [peff/git](https://github.com/peff/git)@[618ffd64ac...](https://github.com/peff/git/commit/618ffd64ac77313bf4b39c80829a28d783d9becf)
#### Sunday 2022-08-28 14:27:47 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---
## [peff/git](https://github.com/peff/git)@[7a48be736c...](https://github.com/peff/git/commit/7a48be736cce6267d266bf0f503ab6c5d4748369)
#### Sunday 2022-08-28 14:27:59 by Jeff King

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
## [Gastove/cookbook](https://github.com/Gastove/cookbook)@[13851ed383...](https://github.com/Gastove/cookbook/commit/13851ed3831b07b8ad0ca277b76d9e696f7f3c21)
#### Sunday 2022-08-28 15:03:13 by Ross Donaldson

Implement tag manifest loading, protect XML parsing

We want to parse tag manifests from org-blorg, which will be authoritative lists
of all the tags used in a project. This is a lovely idea, and also, it turned up
some _stuff_.

First, very practically, we add Thoth for JSON parsing. I could do this a
zillion ways, but Thoth is nice. I don't even need a wrapper type for Tags, so
far. Tag manifest parsing can then be wired up and percolated through, which requires
Result handling. Not bad.

But: while doing this, I learned that FSharp.Data's XML parser will *detonate*
if you, say, accidentally feed it JSON -- and the errors are horrible and very,
very opaque. So, I wrapped that in a Result as well, which requires a bit more
percolating through the stack. Should be... I dunno, at least a lot less
dramatic now.

This is all set, once tags are fixed on my blog!

---
## [MaterializeInc/materialize](https://github.com/MaterializeInc/materialize)@[305082a6a9...](https://github.com/MaterializeInc/materialize/commit/305082a6a99ee063839975c86bd1e821a2af0e23)
#### Sunday 2022-08-28 15:24:46 by Daniel Harrison

persist: commit state updates to durable storage incrementally

Before, there was pressure to keep the size of state down, because it
was rewritten entirely on each command application. In particular, this
created a tension in compaction tuning between being aggressive about
fewer batches (smaller state) and compacting small batches lazily
(smaller write amplification).

Writing state updates as incremental diffs means that size of a
Consensus writes for each command is independent of the total size of
state. We should be able leverage this to make the entire
`WriteHandle::compare_and_append_batch` latency constant w.r.t. the size
of state and thus independent of compaction. This lets us tune
compaction entirely for where we want to be in its more intrinsic
tradeoff between read, write, and space amplification.

(NB: This commit doesn't quite get us to constant latencies, there's
some elbow grease left. I've proven concretely that it can get down to
`O(log(num state batches))`, but that included some hacks that didn't
make this PR. This would be lovely followup work once we get a chance.)

As persist metadata changes over time, we make its versions (each
identified by a [SeqNo]) durable in two ways:
- `rollups`: Periodic copies of the entirety of [State], written to
  [Blob].
- `diffs`: Incremental [StateDiff]s, written to [Consensus]. The
following invariants are maintained at all times:
- A shard is initialized iff there is at least one version of it in
  Consensus.
- The first version of state is written to `SeqNo(1)`. Each successive
  state version is assigned its predecessor's SeqNo +1.
- `current`: The latest version of state. By definition, the largest
  SeqNo present in Consensus.
- As state changes over time, we keep a range of consecutive versions
  available. These are periodically `truncated` to prune old versions
  that are no longer necessary.
- `earliest`: The first version of state that it is possible to
  reconstruct.
  - Invariant: `earliest <= current.seqno_since()` (we don't garbage
    collect versions still being used by some reader).
  - Invariant: `earliest` is always the smallest Seqno present in
    Consensus.
    - This doesn't have to be true, but we select to enforce it.
    - Because the data stored at that smallest Seqno is an incremental
      diff, to make this invariant work, there needs to be a rollup at
      either `earliest-1` or `earliest`. We choose `earliest` because it
      seems to make the code easier to reason about in practice.
    - A consequence of the above is when we garbage collect old versions
      of state, we're only free to truncate ones that are `<` the latest
      rollup that is `<= current.seqno_since`.
- `live diffs`: The set of SeqNos present in Consensus at any given
  time.
- `live states`: The range of state versions that it is possible to
  reconstruct: `[earliest,current]`.
  - Because of earliest and current invariants above, the range of `live
    diffs` and `live states` are the same.
- The set of known rollups are tracked in the shard state itself.
  - For efficiency of common operations, the most recent rollup's Blob
    key is always denormalized in each StateDiff written to Consensus.
    (As described above, there is always a rollup at earliest, so we're
    guaranteed that there is always at least one live rollup.)
  - Invariant: The rollups in `current` exist in Blob.
    - A consequence is that, if a rollup in a state you believe is
      `current` doesn't exist, it's a guarantee that `current` has
      changed (or it's a bug).
  - Any rollup at a version `< earliest-1` is useless (we've lost the
    incremental diffs between it and the live states). GC is tasked with
    deleting these rollups from Blob before truncating diffs from
    Consensus. Thus, any rollup at a seqno < earliest can be considered
    "leaked" and deleted by the leaked blob detector.
  - Note that this means, while `current`'s rollups exist, it will be
    common for other live states to reference rollups that no longer
    exist.

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[9118cab4fd...](https://github.com/yogstation13/Yogstation/commit/9118cab4fda02a964b40895aa7aedf3dd55580ef)
#### Sunday 2022-08-28 15:31:01 by Redmoogle

ports fake viruses from tgstation (#15412)

* fakevirus

* fuck you too byond

* Update code/datums/status_effects/debuffs.dm

Co-authored-by: tattax <71668564+tattax@users.noreply.github.com>

Co-authored-by: tattax <71668564+tattax@users.noreply.github.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4517738137...](https://github.com/mrakgr/The-Spiral-Language/commit/451773813765405364636a967a997c76f2c32125)
#### Sunday 2022-08-28 16:14:31 by Marko Grdinić

"8:50am. I am still solidifying my will. Coming to a firm conclussion as to what should be done, regardless of whether it is possible, is important. I spent 1.5 decades just thinking about how to connect the pursuit of omnipotence to reality. So what if I can't program properly just yet? I can come to conclussion as to what is right at least.

It might not be bad to take a break for while longer from it and just write.

I should make Heaven's Key a story about the algorithms.

I am going to change the Heaven's Key Patreon name to `simulacrum_heavens_key` later and remember to modify the two links that are currently out there. That way I'll be able to just leave out 1/3rds of the story on RR and leave it only for the patrons. It won't be a bad business.

Yeah, this is true sci-fi. I am searching my heart, and what is in my heart are evolutionary algorithms.

It is not like in 2014 that my mind was blown by the implications of the self improvement loop.

9am. I am just returning to what I was before. I had nothing, but the desire. I didn't have need for hope. Right now I am going through disappointment because I had gotten attached to the real world. I've become a weakling as a result.

I should use Heaven's Key as a catalyst to cultivate my desire anew. It will be my chance to do programming without programming. Without the endless disappointment that comes with it. In the story, all the algorithms will work and I will never not have enough computational power to make my ideas a reality. If some patrons chip in, I start turning that into concrete advantages.

I'll write about my dreams, and that will translate into real advantages.

9:05am. This is the way to do it. I should keep my eyes on what I want instead of prostituting myself doing all sorts of side things.

I'll focus on my dreams, and if I never get the computational power to manifest them in reality so be it. That is the way to live. I do not have a player guiding me from beyond, so I can't act like an ubermench.

9:15am. 159 views. It does not seem like it is going up just like that. I can only see if me posting chapters will incentivize people to read. So far, the latest chapter only had 4 views. Pathetic. I can only push that up with effort.

9:15am. First of all, Railgun. Then some more chilling. Then I will get started writing.

I need a firm determination as to what I want to do.

9:20am. If I had actually published the original arcs as books, I might have made a few dollars here and there.

Sigh...I remember that time I started talking about wizards, and some guy panicked and emailed me to contant my 'support network'. I do not have such a thing. The reason why I am always at the bottom is because I am always doing everything by myself. Nobody understands me, and nobody wants to help me.

9:25am. But it is not that is important. What is important is having a firm determination in life.

I feel like this experience is making me closer to nature. Having experienced how hard it is to do reasoning in high dimensional spaces, I can only fault this current setup of making random experiments.

9:30am. Omnipotence, self improvement loop, forget those.

Why not get heated up about the most primitive of algorithms? Yeah, this is what sci-fi should be. It is not about going around in space in spaceships.

It is about playing a metaRPG like Simulacrum and using that to improve yourself.

But just gaining power through some unrealistic system like in cultivation stories is hollow. True works of art connect the reader to what is in the real world rather than just provide escapism.

10am. Let me take a break today as well. I am going to go back to bed again. I am going to bolster my desire. All these regrets, I need to be rid of them.

5:50pm. I was in bed all this time, apart from lunch. I even skipped breakfast.

The lackluster pace at which the world is moving towards the Singularity is making my emotions very complex. But on review, the intense ambiguity does frame my moves correctly. The applications only to mess them up. The lack of desire to really do anything more than I've already done. The hesitation to start writing right away and go into writing.

Basically, even though I believe that the Singularity will happen, I cannot treat it as anything other than speculation. This is despite it being my reason for living.

It is like being bullish on the market and only being 100% long instead of 500%.

I simply need to get some signal from the world that it is safe for me to commit further. Right now, I am only getting the opposite signals. The AI chip companies are a complete disappointment. I want to make progress, but there is no point in getting invested without having the hardware to guide me.

I keep thinking about oracles. I already talked about the poker oracle - if I asked it the optimal poker algorithm, it would surely be informative.

I am thinking about the Singularity oracle. If the Singularity never happens, just how would I behave? Or how would I behave if I knew with absolute certainty that I won't be the one to cause it. What if I knew the disposition of the future God, how would I react.

Right now, I am mired in complete ambiguity and the timeline has never been more unclear to me. I do not know what my responsibilities are.

So I can't help, but act noncommittally myself. If I had some good hardware I could get, I would slap myself and say: 'Of course, I need money to get that AI chip.' But right now all the indicators point that trying out any of the existing chips would be a waste of time. In particular, why that is the case for Graphcore's I'll go into in the author's note.

I want a sponsor, not simply for the money, but as a way for the world to indicate to me that I should be invested myself. The fact that all these companies are loading up on C++ programers instead of functional ones does not bode well for them.

5:55pm. Anyway, if I was in something like early 20th century and knew for sure I'd be dead before the Singularity happened, what I would do is write a story. I can't prove that I am worthy of respect by going through the self improvement loop, but I'd be least be able to give some indication that I desire it. And that is all you can do.

DALLE and Stable Diffusion do not make me more bullish on the Singularity in the least. I already knew that deep learning would be to get at least this far, but it won't be able to keep scaling for much longer.

There is no helping it. Deepmind and OpenAI have the chance to cause the Singularity in the 20s and put the world under their boot.

But if I can get over the initial hurdle on the next wave, I am going to use it to get the resources that I need to make further progress. Once the hardware is powerful enough to fuel its own advances, I'll be completely independent on the ML community.

6pm. If the world can give me some sign that I should resume I will do it. But right now, I can't commit myself.

What I should do is write the story and show the future God what a just world would be like. Even if I can't do it myself, nobody will blame me. You can't blame a being that can't self improve for lack of ability. I can't win unless the world allow me to win.

All I can do is talk, so that is what I should focus on. Forget the human readers. My real aim should be to affect whatever agents my competitors come up with. I am not obsessed with being first myself. I just fear that they might create a world I do not like. So why not establish the right values and morality and rally around that?

6:05pm. This is what I need to internalize in order to break into 5/5 realm of writing. The 9-5 writer is bound to be forgoten. Grand aims, the ego to instruct the future Transcendi. That is what suits me.

That is the kind of attitude I should have if I want to have fun with this.

6:10pm. The reason why I could program for so long is because I believed in ML and that Spiral will be necessary. Now that this has been shaken I've correspondly lost that desire. If the world cannot give me a sign, I should give it one instead.

Let me close here. I'll see whether I can start writing again tomorrow. If not, I'll spend some time in bed again until I find the strength to do it.

I've found the will to become a programmer after a decade of absence from it. I will find the will to become a writer as well for different kinds of reasons."

---
## [petre-symfony/symfony-6-fundamentals-services-config-and-environments](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments)@[91734e74e7...](https://github.com/petre-symfony/symfony-6-fundamentals-services-config-and-environments/commit/91734e74e77a01d900a6685e61a2a08fbbca84a5)
#### Sunday 2022-08-28 16:22:12 by petrero

24.1. Customizing a Command - php bin/console app:talk-to-me --help

  We have a new console command! But... it doesn't do much yet, aside from printing out a message. Let's make it fancier.

  Scroll to the top. This is where we have the name of our command, and there's also a description... which shows up next to the command. Let me change ours to

    A self-aware command that can do... only one thing.

  Configuring Arguments and Options
  - Our command is called app:talk-to-me because, when we run this, I want to make it possible to pass a name to the command - like Ryan - and then it'll reply with "Hey Ryan!". So, literally, we'll type bin/console app:talk-to-me ryan and it'll reply back.

  When you want to pass a value to a command, that's known as an argument... and those are configured down in... the configure() method. There's already an argument called arg1... so let's change that to name.

  This key is completely internal: you'll never see the word name when you're using this command. But we will use this key to read the argument value in a minute. We can also give the argument a description and, if you want, you can make it required. I'll keep it as optional.

  The next thing we have are options. These are like arguments... except that they start with a -- when you use them. I want to have an optional flag where we can say --yell to make the command yell our name back.

  In this case, the name of the option, yell, is important: we will use this name when passing the option at the command line to use it. The InputOption::VALUE_NONE means that our flag will just be --yell and not --yell= some value. If your option accepts a value, you would change this to VALUE_REQUIRED. Finally, give this a description.

  Beautiful! We're not using this argument and option yet... but we can already re-run our command with a --help option:

    php bin/console app:talk-to-me --help
  And... awesome! We see the description up here... along with some details about how to use the argument and the --yell option.

---
## [torvalds/linux](https://github.com/torvalds/linux)@[4e3aa92382...](https://github.com/torvalds/linux/commit/4e3aa9238277597c6c7624f302d81a7b568b6f2d)
#### Sunday 2022-08-28 18:19:02 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net

---
## [nderscore/stable-diffusion-webui](https://github.com/nderscore/stable-diffusion-webui)@[4f8dd02ccb...](https://github.com/nderscore/stable-diffusion-webui/commit/4f8dd02ccb69f5e457226531a82f54fa4dfe97ea)
#### Sunday 2022-08-28 18:31:30 by Georg Zoeller

Adding .png metadata 

This may open the option to read data from images dragged into the tool later.  Activated with --save_metadata

Properties (example output from imagemagic 'identify -verbose' command:
    SD:cfg_scale: 7.5
    SD:GFPGAN: False
    SD:height: 512
    SD:normalize_prompt_weights: True
    SD:prompt: a beautiful matte painting of a cottage on a magical fantasy island, unreal engine, barometric projection, rectilinear
    SD:seed: 247624793
    SD:steps: 50
    SD:width: 512

---
## [OxygenCobalt/Auxio](https://github.com/OxygenCobalt/Auxio)@[cafead8a88...](https://github.com/OxygenCobalt/Auxio/commit/cafead8a8871e5bff361a9dcda46b61c5fc58917)
#### Sunday 2022-08-28 19:02:49 by Alexander Capehart

deps: upgrade to android 13 [#129]

FINALLY upgrade to android 13.

I cannot believe it had to take until the release of the version to
finally update the SDK version, but of course it had to. For some
insane reason that I have no idea why it passed QA, the 33 SDK had
a crippling issue where attributes were not recognized. The only
way to fix this was to:

1. Upgrade to the newer studio version (Chipmunk Patch 2)
2. Upgrade to AGP 7.3.0-beta05.

Funny thing though. AGP 7.3.0 IS NOT COMPATIBLE WITH CHIPMUNK. Okay,
so we can upgrade to Dolphin then and then we can use AGP, right?
HAHAHA NOPE! Dolphin hasn't patched out the XML issue yet despite
every other release channel having a release on August 3rd. Did
some engineer at google just forget to make a release? What?

Okay, so I guess I'm forced to use Electric Eel, the UNSTABLE CANARY
VERSION that IS FILLED WITH BUGS. But oh wait, Electric Eel doesn't
like AGP 7.3.0 EITHER! It wants AGP 7.4.0, which IS ALSO IN ALPHA.
So, I'm forced to use the ALPHA studio and the ALPHA AGP version just
to use the android 13 SDK in a way that is not completely unbearable.

The android SDK, everyone.

(This is not a cry for help, I just want to write down my infinite
frustration with this stupid goose chase somewhere)

---
## [bcully/rust-analyzer](https://github.com/bcully/rust-analyzer)@[1a5925dc84...](https://github.com/bcully/rust-analyzer/commit/1a5925dc84d0ef966023d6612147f93a0464174c)
#### Sunday 2022-08-28 19:05:32 by bors

Auto merge of #12294 - listochkin:prettier, r=Veykril

Switch to Prettier for TypeScript Code formatting

## Summary of changes:

 1. Added [`.editorconfig` file](https://editorconfig.org) to dictate general hygienic stuff like character encoding, no trailing whitespace, new line symbols etc. for all files (e.g. Markdown). Install an editor plugin to get this rudimentary formatting assistance automatically. Prettier can read this file and, for example, use it for indentation style and size.
 2. Added a minimal prettier config file. All options are default except line width, which per [Veykril](https://github.com/Veykril) suggestion is set to 100 instead of 80, because [that's what `Rustfmt` uses](https://rust-lang.github.io/rustfmt/?version=v1.4.38&search=#max_width).
 3. Change `package.json` to use Prettier instead of `tsfmt` for code formatting.
 4. Performed initial formatting in a separate commit, per [bjorn3](https://github.com/bjorn3) suggestion added its hash to a `.git-blame-ignore-revs` file. For it to work you need to add a configuration to your git installation:
    ```Shell
    git config --global blame.ignoreRevsFile .git-blame-ignore-revs
    ```
 5. Finally, removed `typescript-formatter` from the list of dependencies.

----
What follows below is summary of the discussion we had on Zulip about the formatter switch:

## Background

For the context, there are three reasons why we went with `tsfmt` originally:
* stick to vscode default/built-in
* don't add extra deps to package.json.lock
* follow upstream (language server node I think still uses `tsfmt`)

And the meta reason here was that we didn't have anyone familiar with frontend, so went for the simplest option, at the expense of features and convenience.

Meanwhile, [**Prettier**](https://prettier.io) became a formatter project that JS community consolidated on a few years ago. It's similar to `go fmt` / `cargo fmt` in spirit: minimal to no configuration to promote general uniformity in the ecosystem. There are some options, that were needed early on to make sure the project gained momentum, but by no means it's a customizable formatter that is easy to adjust to reduce the number of changes for adoption.

## Overview of changes performed by Prettier

Some of the changes are acceptable. Prettier dictates a unified string quoting style, and as a result half of our imports at the top are changed. No one would mind that. Some one-line changes are due to string quotes, too, and although these a re numerous, the surrounding lines aren't changed, and git blame / GitLens will still show relevant context.

Some are toss ups. `trailingComma` option - set it to `none`, and get a bunch of meaningless changes in half of the code. set it to `all` and get a bunch of changes in the other half of the code. Same with using parentheses around single parameters in arrow functions: `x => x + 1` vs `(x) => x + 1`. Perrier forces one style or the other, but we use both in our code.

Like I said, the changes above are Ok - they take a single line, don't disrupt GitLens / git blame much. **The big one is line width**. Prettier wants you to choose one and stick to it. The default is 80 and it forces some reformatting to squish deeply nested code or long function type declarations. If I set it to 100-120, then Prettier finds other parts of code where a multi-line expression can be smashed into a single long line. The problem is that in both cases some of the lines that get changed are interesting, they contain somewhat non-trivial logic, and if I were to work on them in future I would love to see the commit annotations that tell me something relevant. Alas, we use some of that.

## Project impact

Though Prettier is a mainstream JS project it has no dependencies. We add another package so that it and ESLint work together nicely, and that's it.

---
## [Zeldazackman/Citadel-Station-13-RP](https://github.com/Zeldazackman/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/Zeldazackman/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Sunday 2022-08-28 20:15:53 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [TaleirOfDeynai/nai-context-userscript](https://github.com/TaleirOfDeynai/nai-context-userscript)@[59dc360b7a...](https://github.com/TaleirOfDeynai/nai-context-userscript/commit/59dc360b7aad60a0983239dc2b58397d45c82ec2)
#### Sunday 2022-08-28 20:30:10 by Taleir of Deynai

I hate this library...

But it's the only one that's really still maintained, and I don't want to roll my own.  I'll just work around all its Ruby-like magic that makes it feel very inconsistent.
Also, I had to drop the idea of pulling a specific commit from the repo with Napa, since the tests could not really deal with the fact the script needed to be inlined and executed on the global scope ...or I didn't feel like figuring out how to make it work that way.
So, instead I pulled a local copy, modified it so it was a CommonJS module, adapted its wonky types, and I guess I'll deal with updating it by hand now and then.  Or not.  Who really cares...?
What?  Why not just use the `@require` directive of user-scripts like the docs suggest?  ARE YOU FUCKING INSANE!?  Yeah, let's pull code from a random URL and execute it in a privileged context!  Great idea!  The file that's there could NEVER be replaced with something malicious at some future date!
No...  Instead, I will pull a copy, vet it myself, and use that knowingly safe copy instead.  Vetting it was easy because I had to reference the code directly to figure out all its weird jank; the docs are shit and incomplete.

---
## [MASQ-Project/Node](https://github.com/MASQ-Project/Node)@[b0e9bb484e...](https://github.com/MASQ-Project/Node/commit/b0e9bb484effc32ed164eb4bef51b624c3d7982a)
#### Sunday 2022-08-28 20:34:04 by dnwiebe

GH-625: Log message enhancements, plus clippy appeasement (#153)

* Log message enhancements, plus clippy appeasement

* GH-627: Clippy should be happy again by now

* GH-627: one line was silly

* GH-627: starting ignoring the troublesome test again

* GH-627: there was a formatting issue

* handles_startup_and_shutdown_integration now doesn't run in Actions on Windows

* handles_startup_and_shutdown_integration now doesn't run in Actions on Windows

* Added import

* GH-625: Formatting

* GH-625: Remember to return

Co-authored-by: Bert <Bert@Bert.com>

---
## [ModruKinstealer/CS50ProblemSets](https://github.com/ModruKinstealer/CS50ProblemSets)@[97d8cf6704...](https://github.com/ModruKinstealer/CS50ProblemSets/commit/97d8cf67045e3ae79499c92009728d7c4ceaa587)
#### Sunday 2022-08-28 23:02:10 by ModruKinstealer

Pset8: homepage

Whew... it's taken a really long time to do this. Some of it was that I've been busy at work and at home so didn't have as much time, some of it was procrastination, and some of it was just that I didn't feel like I knew what I was doing. I'd taken a CSS/HTML5 course through w3schools but hadn't touched on JS before and the lectures were basically just well here's a couple of the main differences, go Google the rest.  

As is noted in the planning.txt I had some pretty big ideas, or at least to me they were maybe a pro could bang them out in a day, unfortunately it being almost Sept and I have another week to go then final project I felt like I didn't have time to finish some of the things I wanted to do the way I wanted to do them. 

The API stuff for the movies page I wanted to do wasn't working very well. I wanted to get the top 10 movies of each Genre from IMDB according to their list of Genres, however the best I could do was a list of top movies over-all. Though at least I did get some API functionality working so I have a base to work off on later. In the end I decided to scrap the movies and woodworking pages for a later iteration.
I also would like to have a management page where I could add authors/books, movies, etc without having to go through and hack at the code line by line. I imagine a "addAuthor" function where it generates a UI pop-up where I can enter in the authors information including links to socials and such and it'll update the appropriate pages. I'm thinking it'll require a database of some kind and I'll have to refactor the html and add JS to make it so the HTML is generated dynamically based on some kind of For loop.
The CSS for the spacing of the hoverable side-nav is a bit of a mess and I don't care for it at all. It's something that I combined 2 or 3 tutorials to create so there may be tons of room to make it better. I feel like there has to be some kind of function I can run to dynamically figure the spacing based on how many entries and such, the biggest hurdle to my initial thought process on it was that I needed to determine how many pixels the title part was so I could have just the icons showing still. I'm sure there is a way but again it's something I ran out of time and so have pushed it to v2 of the site. The side-nav visually is pretty close to how I imagined it working which is nice, I did have to add some drop down action for smaller devices as part of the pset was that it had to be nice looking on a variety of devices and the hoverable side-nav as it was would extend down off the viewport on smaller devices at times.
There continues to be times where things I take directly from tutorials don't work. The CSS for changing the default coloring of accordions was an example. Even though there is an .accordion class it just would not change anything on the rendered page. I ended up having to drill down to the three subparts of the accordion to get it to change any of it.  I had a ton of trouble getting the footer to behave and look how I wanted. It still looks a little wonky on smaller devices but not as bad as it was at one point. 

I hope to be able to come back after I finish the final project and implement the rest of the ideas I had and tighten some things up. We'll see how long it takes to complete week 9 and the final project.  Eventually I'll update it simply because I designed it with the idea that I'd have it setup as an actual page and not just as a school project.

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[143c62ce3e...](https://github.com/i3roly/glibc_ddwrt/commit/143c62ce3eb487f0b1e3dd455507a12f4f79d678)
#### Sunday 2022-08-28 23:31:52 by gagan sidhu

[v4.14.291/49976] aye suge, what'd i tell you giga when i come out of jail what i was gonna do? i was gonna start diggin' into these gigas' chest, right? watch this. aye quick let me see them binoculars

(i will eventually update tor and lighttpd. it's being annoying rn)
(also, i noticed some weird logs on my 882 but it's possible this is due
to my abuse over 5 years. please report stuff immediately!!)

time to ride.
grab your bulletproof vest cause it's gonna be a long one

now i'm gonna show you what it's like on this side, the real side
now on this ride there's gonna be some real Gs, and there's gonna be some pussies
now the real Gs are gonna be the ones with money and bitches
the pussies are gonna be the ones on the floor bleeding

now everybody keep your eyes on the prize, cause the ride gets tricky
see you got some people on your side that say they're your friends, but in real life they're your enemies
then youhave others who say they're your enemies, but in real life their eyes are on your money
see, enemies that say they're true, but in real life they're snitches!

it's a dirty game y'all
you have to be careful about who you mess with, and who you don't mess with
because this gets wild, y'all

keep your mind on the money, baby
your mind on the money

[![heartzofmen](http://img.youtube.com/vi/pXOuIqy0voQ/0.jpg)](http://www.youtube.com/watch?v=pXOuIqy0voQ "Heartz of Men")

---

