## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-30](docs/good-messages/2022/2022-08-30.md)


2,202,169 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,202,169 were push events containing 3,280,189 commit messages that amount to 247,772,744 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 45 messages:


## [KDr2/postgres](https://github.com/KDr2/postgres)@[7fed801135...](https://github.com/KDr2/postgres/commit/7fed801135bae14d63b11ee4a10f6083767046d8)
#### Tuesday 2022-08-30 00:02:23 by Tom Lane

Clean up inconsistent use of fflush().

More than twenty years ago (79fcde48b), we hacked the postmaster
to avoid a core-dump on systems that didn't support fflush(NULL).
We've mostly, though not completely, hewed to that rule ever since.
But such systems are surely gone in the wild, so in the spirit of
cleaning out no-longer-needed portability hacks let's get rid of
multiple per-file fflush() calls in favor of using fflush(NULL).

Also, we were fairly inconsistent about whether to fflush() before
popen() and system() calls.  While we've received no bug reports
about that, it seems likely that at least some of these call sites
are at risk of odd behavior, such as error messages appearing in
an unexpected order.  Rather than expend a lot of brain cells
figuring out which places are at hazard, let's just establish a
uniform coding rule that we should fflush(NULL) before these calls.
A no-op fflush() is surely of trivial cost compared to launching
a sub-process via a shell; while if it's not a no-op then we likely
need it.

Discussion: https://postgr.es/m/2923412.1661722825@sss.pgh.pa.us

---
## [JelixFon/Key-Quest](https://github.com/JelixFon/Key-Quest)@[4e48023f4a...](https://github.com/JelixFon/Key-Quest/commit/4e48023f4aad7e92ee4da27012eb17cf6064a6cf)
#### Tuesday 2022-08-30 00:09:03 by Filipe Collura

please kill me

i have had to re-upload the same god damn image 8 times because I got the wrong file dimensions. all I feel is pain and suffering

---
## [sjp38/linux](https://github.com/sjp38/linux)@[24f2ec350e...](https://github.com/sjp38/linux/commit/24f2ec350ef58546b1facddccdf7628509f25b68)
#### Tuesday 2022-08-30 00:23:34 by Johannes Weiner

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
## [wantingteng/Udem1005](https://github.com/wantingteng/Udem1005)@[0a230da7a1...](https://github.com/wantingteng/Udem1005/commit/0a230da7a126bec8c17fcd4c37a7baddd1767f8f)
#### Tuesday 2022-08-30 00:36:48 by Wanting

Create final group work 

This project was done by me and my friend, we designed a web page to introduce ourselves, including our homework and life experiences, etc.

---
## [Koshenko/mojave-sun-13](https://github.com/Koshenko/mojave-sun-13)@[08566250c0...](https://github.com/Koshenko/mojave-sun-13/commit/08566250c03835a4ab8521b53b32b8b23e95cc97)
#### Tuesday 2022-08-30 01:01:05 by LemonInTheDark

Reworks janitor cyborg cleaning, focus on the slipping (#64131)

Alt of #64105 and #64126 (I'm sorry Novva, I should have said something earlier)
I main janitor. As a janitor main, my greatest joy in life is slipping people who ignore my signs

I've seen some people complain about janitor borgs, so I decided to look into em

Unfortunately, not only is the janitor borg just a straight upgrade to janitors, it has absolutely no reason to use most of its kit
We give it standard cleaning supplies, and hell even bespoke tools to deal with leaving slippery tiles everywhere, but we also just let them clean anything they can walk over

This seems a bit too much to me, even for borgs. Also it's like, really boring

So what if we made their movement based cleaning cost something? How about we make it suck water from their bucket. Use the same pattern as mop code, make it twice as expensive though. Give it a slowdown, some sound cues, and an action button to trigger it all

---
## [skylord-a52/orbstation-andrea](https://github.com/skylord-a52/orbstation-andrea)@[6f2354e694...](https://github.com/skylord-a52/orbstation-andrea/commit/6f2354e694f3412a76b383f684a0bfc85a448d8e)
#### Tuesday 2022-08-30 01:33:20 by san7890

Fixes Fucked Job Requirement Displays (#69368)

* Fixes Fucked Job Requirement Displays

Hey there,

I fucked up in #68856 (5b77361d399ba0dd992e61a16b9bbe38e8aa5a60). We weren't supposed to add another MINUTES multiplication here. I don't even remember why I did this if we are being perfectly honest with each other. Whoops.

fix: You should now no longer need thousands of hours to unlock your favorite head of staff role.

---
## [WoodenTucker/40K-Eipharius](https://github.com/WoodenTucker/40K-Eipharius)@[ebdba9844a...](https://github.com/WoodenTucker/40K-Eipharius/commit/ebdba9844a54549b22d7b4c722eb58b5da61042e)
#### Tuesday 2022-08-30 01:59:16 by Myphicbowser

Various Fixes and Lights

Turned some Space Panels into Snow Panels on the Mountain Level

Deleted a Duplicate Fire Alarm in Virology

Added some FUCKING LIGHTS HOLY SHIT WHY ARE SOME AREAS SO FUCKING DARK

---
## [Kesslerjx/spy_backtester](https://github.com/Kesslerjx/spy_backtester)@[b7755b20b3...](https://github.com/Kesslerjx/spy_backtester/commit/b7755b20b3879e3bc87345b14d50092865c85356)
#### Tuesday 2022-08-30 02:35:52 by Joseph Kessler

Change is_swing function again

After speaking with a friend, it made sense to just simulate buying the
contract in the morning. If you do that, it doesn't matter how much it
moves overnight. All that matters is that the direction is correct.

---
## [anhwin88/625](https://github.com/anhwin88/625)@[291480c2b6...](https://github.com/anhwin88/625/commit/291480c2b62f53f967aa7269fca93db984199bbc)
#### Tuesday 2022-08-30 03:35:53 by anhwin88

Add files via upload

deal satisfy mom evoke priority boring paddle slogan cream veteran blast country blade adapt course motion rabbit awkward clutch chef badge village arch spike ball capable isolate conduct rookie penalty rural pill wreck timber lemon thrive install lady honey eyebrow effort legend box brief check seminar wheat empty boost piano blade slender quality era regular hungry pigeon click jump unique leisure hold nominee tunnel crop because shy sauce fire mirror ahead kitchen ethics zero bicycle ozone list trip mesh flat category oppose warm coconut bitter outdoor amazing tragic salt hard run special exhibit lottery minimum hour banner evolve pulp peace pattern dinosaur baby quick dignity crazy vast punch donkey penalty fossil guess gesture play slow employ doctor example search domain mimic iron flag vacant wrist tragic floor bar number dignity pause segment poet pig stuff photo review motor suffer day field hint bundle state album forward shrimp cheese salt sauce observe apart enemy repeat easily remind auction alley client addict weapon cement analyst name enhance floor frequent silver athlete sell unit waste index doll rail marine tent cross ask wing used fault vacuum knee health yard surge matrix transfer cave exhibit aim describe caught wet monkey modify stamp split matter upper expire few carpet survey minor taste absorb breeze cricket gas cake clay pigeon young limit couple need reopen female program type inhale diamond frequent day salad chicken always awake kitchen vessel zoo recipe joke yellow tongue tragic crisp mouse neutral system crush target slush accident bind accident assault tiny hybrid mechanic topple nephew toast captain edit noodle cram animal convince dial parade combine open cancel appear mushroom confirm april tent fossil endorse coast ring lonely slide style black flock lawsuit quiz cabbage multiply firm female theory kiss pilot e

---
## [bogachenko/fuckfuckadblock](https://github.com/bogachenko/fuckfuckadblock)@[9649dd2c31...](https://github.com/bogachenko/fuckfuckadblock/commit/9649dd2c3180eec7c91b97043572fcc7746e94ae)
#### Tuesday 2022-08-30 03:41:54 by bogachenko

Update fuckfuckadblock.txt

Removed redirect for the site mysexbossy.com
Removed pop-ups for the sites 1piece.online arifuretamanga.online bermanga.online blacksummoner.online callofnight.com classroomofelite.online danmachimanga.com dr-stone.org hatarakumaou.online hxmanga.com isekaimeikyuudeharem.com kimetsu.online komi-san.net madeinabyssmanga.online opomanga.com overlordmanga.org readchainsaw.online rentagirlfriendmanga.online housecardsummerbutton.com aniwatch.pro masalaseen.net sbspeed.com vidmovie.xyz audaciousdefaulthouse.com fittingcentermondaysunday.com fraudclatterflyingcar.com launchreliantcleaverriver.com reputationsheriffkennethsand.com mushoku-tensei.online eegybest.xyz
Bypass anti-adblock for the sites worldpopulationreview.com freedwnlds.com eroti.ga

---
## [anhwin88/625](https://github.com/anhwin88/625)@[baa9ef4b0c...](https://github.com/anhwin88/625/commit/baa9ef4b0c9c4f55a6474f951e7166108a694ba7)
#### Tuesday 2022-08-30 03:44:03 by anhwin88

Create 15

face slam wise country vocal kite column light try increase siren ten only silent shine corn glue tiger reflect excuse filter answer rich curious wise rail pink attitude chief fish rent garage bronze among notice scout iron online avoid night neutral toast liquid mind clean afford easily jazz install twin bomb slice pelican duty spirit dignity mutual doll near inquiry flee immune sock zero hat avocado rate paddle when hundred typical moon reopen lazy giant repeat original dance shop awake void pencil galaxy reduce trip canvas snake brass dice arm raise rescue lazy cinnamon recall recycle protect bench worth tobacco hybrid tank idle judge chalk virus lobster worth allow little panel brother bone install logic life erosion siege memory either method ahead flock fault surface permit fetch hen burst cruel tool rubber say food radio protect victory fatigue symbol coral sausage loan boy vicious core present knee indoor bus slender swear west scissors pepper crew okay today brand ginger bench place gospel soccer enough acid step impact prison mixed paper kick illegal noise razor hub tired edit response produce twist

---
## [mozilla/gecko-dev](https://github.com/mozilla/gecko-dev)@[cf74fba975...](https://github.com/mozilla/gecko-dev/commit/cf74fba9757573e8d45d41f1cd852a44bb13afea)
#### Tuesday 2022-08-30 03:54:50 by Emilio Cobos Álvarez

Bug 1786525 - Don't update untransformed anchor rect when moved by move-to-rect. r=stransky

Otherwise, it changes the move-to-rect inputs, which can change the
output as well, making us move the anchor all the way to the right.

You could, I guess, consider this a mutter bug of sorts, because it
feels weird that you pass it an anchor that has been a `move-to-rect`
output and you get another rect as an output.

But also, it's kinda silly that we're doing that to begin with, so avoid
it by telling the popup frame whether it's been positioned / moved by
move-to-rect (and keeping the anchor in that case).

The reason this works on my setup without "Large text" is just dumb luck
(the front-end computes a max-height for the panel that is small enough
to fit on the screen).

Differential Revision: https://phabricator.services.mozilla.com/D155406

---
## [Knightfall5/Citadel-Station-13-RP](https://github.com/Knightfall5/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/Knightfall5/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Tuesday 2022-08-30 04:25:48 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [shitlearn/react](https://github.com/shitlearn/react)@[b6978bc38f...](https://github.com/shitlearn/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Tuesday 2022-08-30 05:04:33 by Andrew Clark

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
## [RajrupDasid/linux](https://github.com/RajrupDasid/linux)@[4e3aa92382...](https://github.com/RajrupDasid/linux/commit/4e3aa9238277597c6c7624f302d81a7b568b6f2d)
#### Tuesday 2022-08-30 05:29:35 by Peter Zijlstra

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
## [paulhauner/lighthouse](https://github.com/paulhauner/lighthouse)@[66eca1a882...](https://github.com/paulhauner/lighthouse/commit/66eca1a88218462235cb76a116dc3c6a1853444f)
#### Tuesday 2022-08-30 05:33:09 by Michael Sproul

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
## [Mikecerc/Portfolio](https://github.com/Mikecerc/Portfolio)@[98246d79ee...](https://github.com/Mikecerc/Portfolio/commit/98246d79ee8f5a5f3e65058500101c65983a7aed)
#### Tuesday 2022-08-30 06:19:46 by Mikecerc1

wow, ok, that was super super funny. wow. what a good joke web dev. I love you web dev. You've harmed me. OML I love everything. Life is goodgit add *!

---
## [elpaablo/frameworks_base](https://github.com/elpaablo/frameworks_base)@[438a2c8278...](https://github.com/elpaablo/frameworks_base/commit/438a2c82785c2fd4d7fe2b2e6de6c91e844899ab)
#### Tuesday 2022-08-30 06:31:27 by Joey Huab

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
## [abhishek1994-ux/-MyCloudDiary](https://github.com/abhishek1994-ux/-MyCloudDiary)@[0cf5c36dc1...](https://github.com/abhishek1994-ux/-MyCloudDiary/commit/0cf5c36dc18778ee9c1db97eadd2fbd9600652c0)
#### Tuesday 2022-08-30 07:52:24 by Abhishek Shrivastava

Microsoft Innovative Educator (MIE) Expert Program

Dear Abhishek Shrivastava,

Congratulations on being selected as a Microsoft Innovative Educator Expert for 2022-2023! Each year, Microsoft selects Innovative Educator Experts to be part of this exclusive global community paving the way for their peers to share ideas, try new approaches, and learn from each other. We are inspired by your achievements and look forward to working with you throughout the one-year engagement, and beyond.

You will be joining a group of some of the most amazing educators who are empowering the students of today to create the world of tomorrow. At Microsoft, we believe that technology alone cannot build 21st century skills for students. It is an accelerator, but the power of change lies within educators. That is why we bring changemakers, like yourself, together to recognize and grow your achievements.

You have been chosen as an MIE Expert because you are self-driven, passionate about your work, have true collaborative spirit, and strive to inspire students with outside-the-box thinking on technology in education. We appreciate your resourcefulness and entrepreneurial spirit. As agents of change, you have achieved excellence in education, using technology and social media. We are grateful for the opportunity to tap into your enthusiasm and enable others to benefit from what is clearly your passion.

We understand that there is a lot of excitement and honor around being a MIE Expert; please share the enthusiasm with your school leaders, colleagues, and among friends and followers on your social media channels. We would love for you to share the great news on social media.

Use #MicrosoftEdu #MIEExpert
Example post: "This year will be (insert adjective). So excited to be selected as an MIE Expert for 2022-2023 #MicrosoftEdu #MIEExpert."
You can use the graphics found here if you want.
Actions to take immediately:

Click here and bookmark or download to OneNote to the MIE Expert Quick Start Guide (this lives in a Consumer OneDrive).
Join our private Facebook group for 2022-2023 here (use the code phrase, “I believe in equity”, and the name of your LSS: Meetu Tiwari.
Check out the products and tools (offers found in QuickStart Guide) you have access to from our partners.
Join our MIE Expert Teams site – directions are here.

Download the official signature block just for MIE Experts to use in your emails.
We will be awarding your MIE Expert badge through Credly (https://credly.com) using the email you entered for your delivery email account in the next week.
Again, CONGRATULATIONS on your selection as an MIE Expert. We are excited to be a part of your journey in creating an environment of innovation in education using technology.

Your local Microsoft team will be in contact with you shortly.

Christina Thoresen, Director, Education Engagement Programs
Sonja Delafosse, Senior Manager Educator Programs

---
## [teskje/materialize](https://github.com/teskje/materialize)@[305082a6a9...](https://github.com/teskje/materialize/commit/305082a6a99ee063839975c86bd1e821a2af0e23)
#### Tuesday 2022-08-30 08:14:44 by Daniel Harrison

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
## [rakheshjaghadish/Genocide-and-Crimes-Against-Humanity](https://github.com/rakheshjaghadish/Genocide-and-Crimes-Against-Humanity)@[4fe00395c7...](https://github.com/rakheshjaghadish/Genocide-and-Crimes-Against-Humanity/commit/4fe00395c73fd6929f46137a18535bd8f82ae321)
#### Tuesday 2022-08-30 08:29:18 by rakheshjaghadish

Email to the International Criminal Court

from:	Rakhesh Jaghadish L <lrakheshjaghadish@gmail.com>
to:	mkstalinoffice@gmail.com,
comments@whitehouse.gov,
cicc@coalitionfortheicc.org,
otp.informationdesk@icc-cpi.int,
cecd@tnebnet.org,
ministry@mid.ru,
media@sputniknews.com,
press@tesla.com,
USinfo@theguardian.com,
AskDOJ@usdoj.gov,
cmhelpline@tn.gov.in,
cmo@tn.gov.in,
media@gbnews.uk,
info@judicialwatch.org,
benedictxvi@vatican.va,
newswatch@bbc.co.uk,
team@childrenshealthdefense.org,
Twitter Support <support@twitter.com>,
ptrajan9@gmail.com,
cedchs@tnebnet.org
date:	Aug 30, 2022, 1:26 AM
subject:	Request to Stop Harassing Me.

From,
Rakhesh Jaghadish L
India,
Tamil Nadu. Human Being, Don't Disturb Me Please. Don't Play With My Family.
Contact: lrakheshjaghadish@gmail.com
 
Subject: I Request to Stop Harassing and Hurting me Psychologically and Physically. This is not the Evidence, I Will Send Every piece of Evidence If they Try to Hack my System using the Mobile Service Van, Spy continuously on Me, and Try to Politically Retaliate against Me.

To,
Honorable,
The International Criminal Court
Office of the Prosecutor
Post Office Box 19519
2500 CM The Hague
The Netherlands;

Chief Minister of Tamil Nadu,
mkstalinoffice@gmail.com
President of Russia,

Department of JUSTICE,
U.S. Department of Justice
950 Pennsylvania Avenue, NW
Washington, DC 20530-0001.

President of the United States,

and also

To Tamil Nadu Electricity Board Tandgedco.

and Also to Media,

media@sputniknews.com

and Also, Elon Musk at Tesla, press@tesla.com, or nasales@teslamotors.com

Information,

Request, Respected Officials,

TO INTERNATIONAL CRIMINAL COURT

ENGLISH LANGUAGE

After the First Week of December 2021, I Emailed the Twitter CEO Jack About the Farmers and I Requested Him in that Mail is to
Unlock my Official or Original Twitter Account.

On December 31, I Got the Unlock Notification of my Blocked Account@RakheshJaghadis.

On January 1, I started my first tweet with Happy New Year. I advocated vaccination in the first week of January. Here I Would Like to Thank the Twitter CEO Jack and Twitter.

On January 16, 2022, I Emailed about the Jaggi Vasudev Crimes to the United Nations, Human Rights, Tamil Nadu Forest Department, The Tamil Nadu Chief Minister M K Stalin, United States President Joe Biden, United States Vice President Kamala Harris, Washington Post like Media. Including I Emailed the Canadian Prime Minister Trudeau, and More Officials and the media.

On the same day between 6 and 7 pm, One person called my father over the phone, my mother took that call, and the person asked my
mother, 'Is Your son a Doctor?'. My Mother told them NO. My Mother Asked, Why are You areAsking?That Person Told Just for Alliance. Because the World Corrupt Leaders were Under the Fear after my Email.

After my Email, On January 20, 2022, ‘Attempts being made to tarnish India’s global image': PM Modi Told at Brahma Kumaris event.

After I Went to New College for Admission on January 28,
On that day Russia versus Ukraine War Started. Since then I have been constantly spied on by corrupt politicians and the BJP RSS terrorists.
Then After, I Joined College for a Master of Engineering on January 28, 2022.

When I came to the college, the admission cell people answered my queries till admission. After joining they tortured me mentally.

On Completed my Admission after they give me a Receipt for the College Fees Payment. After on 29,January2022, I Paid the Fees 12000. That is not Tuition Fees, That fees about Rs. 2800 for Registration Fees, Rs. 200 for Sport Fees, Rs. 1500 for Periodical Test, Corse Material, &InsuranceFees, Rs. 500 for Admission Fees, 3000 Rs. for Association Fees, and 5000 Rs for CautionFees.

Once my admission was completed after they gave me the receipt for payment of college fees. After January 29, 2022, I paid a fee of 12000. That is not the tuition fee, the fee is around Rs. 2800 registration fee, Rs. 200 as a game fee, Rs. 1500 term test, course material, and insurance charges, Rs. Admission fees are Rs.500, and Rs.3000. 5000 for the association fees, and 5000 for warning fees.

On 31, January 2022, I Went Full Time College. Arun Sir said this before the day when the first day comes, there will be a person called Nisar, go and see him.



Read this Document Fully Below,

I Don't Worry If I am Killed by Them. I'm Ready to Die. Because they Torturing me.

I WILL SPEAK AGAINST TYRANNY, NO ONE CAN STOP ME.

Accuse,

RSS BJP Terrorist and World Corrupt Politicians.

Demand,

Next Time,

They Cutoff my Electricity and Current and Turn off My Light, Whistling Infront of My Home, and I Will Go to Any Length. Stop Psychologically and Physically Harm Me.

Stop Hacking Me,

When they Hack My Device, My Device Will Get Over the Heat and Cooler Fan inside the Device is Rotating Fast.

---
## [avar/git](https://github.com/avar/git)@[5beca49a0b...](https://github.com/avar/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Tuesday 2022-08-30 09:09:55 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [SilentEnforcer/tgwr-mod](https://github.com/SilentEnforcer/tgwr-mod)@[844d91db30...](https://github.com/SilentEnforcer/tgwr-mod/commit/844d91db30878a1f6f309c484fd394c79855b356)
#### Tuesday 2022-08-30 09:36:34 by undead-unicorn

Revert "Revert "socialist" He was an Ulster volunteer you muppet , he only become disatified with the govermentmt after the war" irrelevant, royalist trait only really matters for revolution after war, he joins socialists

This reverts commit 3d8bef1e9afc2f27638391ab0dfbfb67d01cdb7d.

---
## [chummer5a/chummer5a](https://github.com/chummer5a/chummer5a)@[85dc0f8354...](https://github.com/chummer5a/chummer5a/commit/85dc0f8354083947e63cb021d7b20d7a88af6dbc)
#### Tuesday 2022-08-30 09:42:31 by Teksura

Toxic and mutant critters (#4899)

* Adding Kokoro Cobra

I mean it mostly works. I feel it's kinda bullshit that the natural weapon doesn't work but that's a later problem

* Update critters.xml

fuck

* Update critters.xml

Adds Pandamonium and Montauk

* Update critters.xml

Added the last of the Critters

* Delete .DS_Store

This file should have been ignored

---
## [Dylan-DPC/rust](https://github.com/Dylan-DPC/rust)@[15e2e5185a...](https://github.com/Dylan-DPC/rust/commit/15e2e5185a22207b18d2cbc47a48b39e63e84cd0)
#### Tuesday 2022-08-30 11:26:10 by Dylan DPC

Rollup merge of #100473 - compiler-errors:normalize-the-fn-def-sig-plz, r=lcnr

Attempt to normalize `FnDef` signature in `InferCtxt::cmp`

Stashes a normalization callback in `InferCtxt` so that the signature we get from `tcx.fn_sig(..).subst(..)` in `InferCtxt::cmp` can be properly normalized, since we cannot expect for it to have normalized types since it comes straight from astconv.

This is kind of a hack, but I will say that `@jyn514` found the fact that we present unnormalized types to be very confusing in real life code, and I agree with that feeling. Though altogether I am still a bit unsure about whether this PR is worth the effort, so I'm open to alternatives and/or just closing it outright.

On the other hand, this isn't a ridiculously heavy implementation anyways -- it's less than a hundred lines of changes, and half of that is just miscellaneous cleanup.

This is stacked onto #100471 which is basically unrelated, and it can be rebased off of that when that lands or if needed.

---

The code:
```rust
trait Foo { type Bar; }

impl<T> Foo for T {
    type Bar = i32;
}

fn foo<T>(_: <T as Foo>::Bar) {}

fn needs_i32_ref_fn(f: fn(&'static i32)) {}

fn main() {
    needs_i32_ref_fn(foo::<()>);
}
```

Before:
```
   = note: expected fn pointer `fn(&'static i32)`
                 found fn item `fn(<() as Foo>::Bar) {foo::<()>}`
```

After:
```
   = note: expected fn pointer `fn(&'static i32)`
                 found fn item `fn(i32) {foo::<()>}`
```

---
## [GhanSaridnirun/Green-Peafowl-Population_Project__GS](https://github.com/GhanSaridnirun/Green-Peafowl-Population_Project__GS)@[e584c85a20...](https://github.com/GhanSaridnirun/Green-Peafowl-Population_Project__GS/commit/e584c85a2035cd79cf6e7dc5857aa941513e05a4)
#### Tuesday 2022-08-30 14:15:38 by Ghan Saridnirun

Update some parameters

Dear Matt and Chloe

I have add the count data of

1. Single Female: preferred to the female that might mature to be breeder but failed to producing offspring
and immature female that didn't ready for breed.

2. The count data of male which including chick, juvenile, 1 year male, 2 year males, and also the 3 year s male. 

However, I found the 3 year male count quite experienced overpopulation due to mature male seem to be more sticked to some area more than other age class, especially in breeding season that they often keep patrol some trail which frequency detected by camera trap causing multiple count in one day period. Thus, I decided to proceed the filter 3 year male count as have done in other age class before to get their number more accurate in Bayesian and MCMC analysis.

So the data of   3 years male would be available soon as I deal with the over count as possible.

Best Regards
Ghan Saridniru

---
## [NKillHere/Fedoraware](https://github.com/NKillHere/Fedoraware)@[5a23d95aca...](https://github.com/NKillHere/Fedoraware/commit/5a23d95aca96005b454a9a9b75ba2ac9ae603c83)
#### Tuesday 2022-08-30 15:44:11 by Johnathon Walnut

Merge pull request #380 from femboy-boop/patch-2

fuck you baan

---
## [tsorya/assisted-installer-agent](https://github.com/tsorya/assisted-installer-agent)@[15557354b2...](https://github.com/tsorya/assisted-installer-agent/commit/15557354b2e2d92afa46d36004153315c30c1d16)
#### Tuesday 2022-08-30 16:01:31 by Omer Tuchfeld

MGMT-10973: Copy coredns & keepalived static pod manifests in day-2 connectivity-check ignition (#388)

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

However, that ignition file is incomplete as currently we only include
necessary information in it (because that file is very big). The parts
of that file that we care in this case are currently missing, so we have
to modify the agent to include those files.

This commit does that. A follow-up commit will be done on the service to
actually check for the presence of these files in this ignition to make
the decision of whether the cluster is managed or not, and in turn turn
on the necessary validations if not.

# Ignition Files

The ignition files we currently include are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

---
## [kira1yoshikage/LLlyTep](https://github.com/kira1yoshikage/LLlyTep)@[5b06141a47...](https://github.com/kira1yoshikage/LLlyTep/commit/5b06141a475b5b9498f84c5e4293647bb5be5f1f)
#### Tuesday 2022-08-30 16:22:46 by kira1yoshikage

Ha4aJlo

My name is Yoshikage Kira. I'm 33 years old. My house is in the northeast section of Morioh, where all the villas are, and I am not married. I work as an employee for the Kame Yu department stores, and I get home every day by 8 PM at the latest. I don't smoke, but I occasionally drink. I'm in bed by 11 PM, and make sure I get eight hours of sleep, no matter what. After having a glass of warm milk and doing about twenty minutes of stretches before going to bed, I usually have no problems sleeping until morning. Just like a baby, I wake up without any fatigue or stress in the morning. I was told there were no issues at my last check-up. I'm trying to explain that I'm a person who wishes to live a very quiet life. I take care not to trouble myself with any enemies, like winning and losing, that would cause me to lose sleep at night. That is how I deal with society, and I know that is what brings me happiness. Although, if I were to fight I wouldn't lose to anyone.

---
## [MrRob0-X/Nethunter_kernel_samsung_exynos7870](https://github.com/MrRob0-X/Nethunter_kernel_samsung_exynos7870)@[ac6c9f5434...](https://github.com/MrRob0-X/Nethunter_kernel_samsung_exynos7870/commit/ac6c9f54341dad6e9a13d6e40edf85df466ac474)
#### Tuesday 2022-08-30 16:54:10 by Jonathan Toppins

mm: ratelimit PFNs busy info message

commit 75dddef32514f7aa58930bde6a1263253bc3d4ba upstream.

The RDMA subsystem can generate several thousand of these messages per
second eventually leading to a kernel crash.  Ratelimit these messages
to prevent this crash.

Doug said:
 "I've been carrying a version of this for several kernel versions. I
  don't remember when they started, but we have one (and only one) class
  of machines: Dell PE R730xd, that generate these errors. When it
  happens, without a rate limit, we get rcu timeouts and kernel oopses.
  With the rate limit, we just get a lot of annoying kernel messages but
  the machine continues on, recovers, and eventually the memory
  operations all succeed"

And:
 "> Well... why are all these EBUSY's occurring? It sounds inefficient
  > (at least) but if it is expected, normal and unavoidable then
  > perhaps we should just remove that message altogether?

  I don't have an answer to that question. To be honest, I haven't
  looked real hard. We never had this at all, then it started out of the
  blue, but only on our Dell 730xd machines (and it hits all of them),
  but no other classes or brands of machines. And we have our 730xd
  machines loaded up with different brands and models of cards (for
  instance one dedicated to mlx4 hardware, one for qib, one for mlx5, an
  ocrdma/cxgb4 combo, etc), so the fact that it hit all of the machines
  meant it wasn't tied to any particular brand/model of RDMA hardware.
  To me, it always smelled of a hardware oddity specific to maybe the
  CPUs or mainboard chipsets in these machines, so given that I'm not an
  mm expert anyway, I never chased it down.

  A few other relevant details: it showed up somewhere around 4.8/4.9 or
  thereabouts. It never happened before, but the prinkt has been there
  since the 3.18 days, so possibly the test to trigger this message was
  changed, or something else in the allocator changed such that the
  situation started happening on these machines?

  And, like I said, it is specific to our 730xd machines (but they are
  all identical, so that could mean it's something like their specific
  ram configuration is causing the allocator to hit this on these
  machine but not on other machines in the cluster, I don't want to say
  it's necessarily the model of chipset or CPU, there are other bits of
  identicalness between these machines)"

Link: http://lkml.kernel.org/r/499c0f6cc10d6eb829a67f2a4d75b4228a9b356e.1501695897.git.jtoppins@redhat.com
Signed-off-by: Jonathan Toppins <jtoppins@redhat.com>
Reviewed-by: Doug Ledford <dledford@redhat.com>
Tested-by: Doug Ledford <dledford@redhat.com>
Cc: Michal Hocko <mhocko@suse.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Hillf Danton <hillf.zj@alibaba-inc.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [eranyser/AngularTutorialDKJune2022](https://github.com/eranyser/AngularTutorialDKJune2022)@[da107e0273...](https://github.com/eranyser/AngularTutorialDKJune2022/commit/da107e0273b054884ff1ec8b7bc0c3ebdb9d1d5f)
#### Tuesday 2022-08-30 17:17:07 by Eran Weiser

feat: bindings

Data binding makes it easy to display component properties and set DOM element properties from our component to better control the view. The component can listen for and respond to events, such as a button click. And with two‑way binding, we can process user entry for an interactive experience. As we've seen, there are four basic types of binding in Angular. Here's a diagram as a memory aid. Interpolation inserts interpolated strings into the text between HTML elements or assigns element properties. Be sure to wrap the template expression in double curly braces and no quotes. Property binding sets an HTML element property to the value of a template expression. The element property must be enclosed in square brackets, and the template expression must be enclosed in quotes. Event binding listens for events from the user interface and executes a component method when the event occurs. The event name must be enclosed in parentheses, and the method to call when the event occurs must be enclosed in quotes. Two‑way binding displays a component property and updates that property when the user makes a change in an input element. Use the banana in a box syntax with the ngModel directive. The template expression must be enclosed in quotes. Here are some things to remember when using ngModel. Define ngModel within the banana in a box for two‑way binding. Be sure to add FormsModule from the Angular forms package to the imports array of an appropriate Angular module, in this case AppModule. This ensures that the ngModel directive is available to any template defined in a component associated with that module. We'll talk more about Angular modules later in this course. The data we have in our component may not be in the format we want for display. We can use a pipe in a template to transform that data to a more user‑friendly format. To use a pipe, specify the pipe character, the name of the pipe, and any pipe parameters, separated with colons. Here is an example of the currency pipe with three parameters. And here, once again, is our application architecture. In this module, we finished more of the ProductListComponent, but it could be better. Next up, we'll see several techniques for improving our component.

---
## [ijadams/poor-boys-bar](https://github.com/ijadams/poor-boys-bar)@[a1aaddc1e3...](https://github.com/ijadams/poor-boys-bar/commit/a1aaddc1e348028ae9947032719a0e7468be0ba6)
#### Tuesday 2022-08-30 17:24:28 by ijadams503@gmail.com

Update from Forestry.io
ijadams503@gmail.com deleted content/blog-posts/eyehategod-goatwhore-sick-thoughts-shitload.md

---
## [killer7luis/lobotomy-corp13](https://github.com/killer7luis/lobotomy-corp13)@[f4c9437d41...](https://github.com/killer7luis/lobotomy-corp13/commit/f4c9437d4110e8b6d3d5708d6fd743cbc3f359ac)
#### Tuesday 2022-08-30 17:26:40 by Killer7luis

We can change anything abno

We can change anything!

If you're creative enough, even a tool abno like this fucking garbage can be fun!

i forgor...

gigachad fix

im awesome

more change fixes

Update zayin.dm

amazing

---
## [JudeForNothing/RebekahCurse](https://github.com/JudeForNothing/RebekahCurse)@[d23d47036c...](https://github.com/JudeForNothing/RebekahCurse/commit/d23d47036c865103252ffab154a1167a26573e36)
#### Tuesday 2022-08-30 17:28:47 by JudeForNothing

beta for glowup update 2

Changes for beta 2

Improved Enchiridion costume sprite

Rebekah changes:
Changed names for Rebekah's personalities, to fit rebekah lore (experimental)
Red Personality -> Rebekah the Nerd
Soul Personality -> Rebekah the Aloof
Evil Personality -> Rebekah the Mischievous
Eternal Personality -> Rebekah the Kind
Gold Personality -> Rebekah the Royal
Bone Personality -> Rebekah the Weird
Rotten Personality -> Rebekah the Crazy
Broken Personality -> Rebekah the Aware
Immortal Personality -> Rebekah the Guardian

Improved rebekah character select screen
Rebekah changing personalities on the beginning now works in coop
Fixed bug where going to new floor did not remove the prism buff for Immortal Rebekah
Should fixed bug where MCM lags with Rebekah

Evil changes:
Improved stage portrait

Gold changes:
Improved stage portrait
Bug fix where stage portrait did not appear ingame

Bone changes:
Fixed bug where the unique thumbs up and down animations did not load
Added stage portrait

Rotten Changes:
When head is deattached, body now has a bleeding costume
When head is deattached, blood can be left in the floor (effect)
Added a unique thumbs up animation
Added a unique thumbs down animation

Broken changes:
Speed is now .75 (was .40)

Immortal changes:
Immortal buff Range is now 270 (was 140)
Immortal buff now should work with laser related characters
Comforter's Wing should cost 50 points now

Credits update:
Added Scooperman and Nixility

Fixed bug where Love Me Love Me Not and Mirror Converter's code would puke out saving code errors

---
## [mdhaber/scipy](https://github.com/mdhaber/scipy)@[0b53fc4c9c...](https://github.com/mdhaber/scipy/commit/0b53fc4c9c593ee524a003296da6be83c9d41a28)
#### Tuesday 2022-08-30 18:39:37 by Tyler Reddy

MAINT: SCIPY_USE_PROPACK

* this is effectively a forward port and modernization
of the release branch `PROPACK` shims that were added in
gh-15432; in short, `PROPACK` + Windows + some linalg backends
was causing all sorts of trouble, and this has never been resolved

* I've switched to `SCIPY_USE_PROPACK` instead of `USE_PROPACK`
for the opt-in, since this was requested, though the change
between release branches may cause a little confusion (another
release note adjustment to add maybe)

* I think the issues are painful to reproduce; for my part,
I did the following just to check the proper skipping/accounting
of tests:

- `SCIPY_USE_PROPACK=1 python dev.py -j 20 -t scipy/sparse/linalg`
  - `932 passed, 172 skipped, 8 xfailed in 115.57s (0:01:55)`
- `python dev.py -j 20 -t scipy/sparse/linalg`
  - `787 passed, 317 skipped, 8 xfailed in 114.80s (0:01:54)`

* why am I doing this now? well, to be frank the process of manually
backporting this for each release is error-prone, and may cause
additional confusion/debate, which I'd like to avoid. Besides, if it
is broken in `main` we may as well have the shims there as well. I would
point out that you may want to add `SCIPY_USE_PROPACK` to 1 or 2 jobs
in CI? The other reason is that if usage of `PROPACK` spreads, I don't
want to be manually applying more skips/shims on each release (which
I already had to do here with two new tests it seems)

---
## [anton-kapralov/study](https://github.com/anton-kapralov/study)@[dc025ff647...](https://github.com/anton-kapralov/study/commit/dc025ff647cc027616820506e3f1ffa54b0a3a80)
#### Tuesday 2022-08-30 19:17:16 by Anton Kapralov

[facebook/hackercup] Second Friend

Boss Rob painted a beautiful scene on a 2D canvas of RR rows by CC columns, containing zero or more happy little trees.
To make sure none of his trees are lonely, Rob would like you to add as many trees as you'd like (possibly 00) to empty spaces so that each tree in the final painting has at least two tree friends, that is, two trees which are each adjacent to it (directly to its north, south, east, or west). If there are multiple solutions, you may print any one of them.

---
## [anton-kapralov/study](https://github.com/anton-kapralov/study)@[f81c4d8d24...](https://github.com/anton-kapralov/study/commit/f81c4d8d243ac86c1eaa68fe0b3a84fcc846037a)
#### Tuesday 2022-08-30 19:17:16 by Anton Kapralov

[facebook/hackercup] Second Second Friend

Boss Rob painted a beautiful scene on a 2D canvas of RR rows by CC columns, containing zero or more happy little trees and zero or more rocks.
To make sure none of his trees are lonely, Rob would like you to add as many trees as you'd like (possibly 00) to empty spaces so that each tree in the final painting has at least two tree friends, that is, two trees which are each adjacent to it (directly to its north, south, east, or west). If there are multiple solutions, you may print any one of them.

---
## [greenforce-project/kernel_xiaomi_citrus_sm6115](https://github.com/greenforce-project/kernel_xiaomi_citrus_sm6115)@[f9ee268eac...](https://github.com/greenforce-project/kernel_xiaomi_citrus_sm6115/commit/f9ee268eac63de1076ff32e468eca77f1dadd9ae)
#### Tuesday 2022-08-30 19:23:23 by Peter Zijlstra

sched/core: Fix ttwu() race

Paul reported rcutorture occasionally hitting a NULL deref:

  sched_ttwu_pending()
    ttwu_do_wakeup()
      check_preempt_curr() := check_preempt_wakeup()
        find_matching_se()
          is_same_group()
            if (se->cfs_rq == pse->cfs_rq) <-- *BOOM*

Debugging showed that this only appears to happen when we take the new
code-path from commit:

  2ebb17717550 ("sched/core: Offload wakee task activation if it the wakee is descheduling")

and only when @cpu == smp_processor_id(). Something which should not
be possible, because p->on_cpu can only be true for remote tasks.
Similarly, without the new code-path from commit:

  c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")

this would've unconditionally hit:

  smp_cond_load_acquire(&p->on_cpu, !VAL);

and if: 'cpu == smp_processor_id() && p->on_cpu' is possible, this
would result in an instant live-lock (with IRQs disabled), something
that hasn't been reported.

The NULL deref can be explained however if the task_cpu(p) load at the
beginning of try_to_wake_up() returns an old value, and this old value
happens to be smp_processor_id(). Further assume that the p->on_cpu
load accurately returns 1, it really is still running, just not here.

Then, when we enqueue the task locally, we can crash in exactly the
observed manner because p->se.cfs_rq != rq->cfs_rq, because p's cfs_rq
is from the wrong CPU, therefore we'll iterate into the non-existant
parents and NULL deref.

The closest semi-plausible scenario I've managed to contrive is
somewhat elaborate (then again, actual reproduction takes many CPU
hours of rcutorture, so it can't be anything obvious):

					X->cpu = 1
					rq(1)->curr = X

	CPU0				CPU1				CPU2

					// switch away from X
					LOCK rq(1)->lock
					smp_mb__after_spinlock
					dequeue_task(X)
					  X->on_rq = 9
					switch_to(Z)
					  X->on_cpu = 0
					UNLOCK rq(1)->lock

									// migrate X to cpu 0
									LOCK rq(1)->lock
									dequeue_task(X)
									set_task_cpu(X, 0)
									  X->cpu = 0
									UNLOCK rq(1)->lock

									LOCK rq(0)->lock
									enqueue_task(X)
									  X->on_rq = 1
									UNLOCK rq(0)->lock

	// switch to X
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	switch_to(X)
	  X->on_cpu = 1
	UNLOCK rq(0)->lock

	// X goes sleep
	X->state = TASK_UNINTERRUPTIBLE
	smp_mb();			// wake X
					ttwu()
					  LOCK X->pi_lock
					  smp_mb__after_spinlock

					  if (p->state)

					  cpu = X->cpu; // =? 1

					  smp_rmb()

	// X calls schedule()
	LOCK rq(0)->lock
	smp_mb__after_spinlock
	dequeue_task(X)
	  X->on_rq = 0

					  if (p->on_rq)

					  smp_rmb();

					  if (p->on_cpu && ttwu_queue_wakelist(..)) [*]

					  smp_cond_load_acquire(&p->on_cpu, !VAL)

					  cpu = select_task_rq(X, X->wake_cpu, ...)
					  if (X->cpu != cpu)
	switch_to(Y)
	  X->on_cpu = 0
	UNLOCK rq(0)->lock

However I'm having trouble convincing myself that's actually possible
on x86_64 -- after all, every LOCK implies an smp_mb() there, so if ttwu
observes ->state != RUNNING, it must also observe ->cpu != 1.

(Most of the previous ttwu() races were found on very large PowerPC)

Nevertheless, this fully explains the observed failure case.

Fix it by ordering the task_cpu(p) load after the p->on_cpu load,
which is easy since nothing actually uses @cpu before this.

Fixes: c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")
Reported-by: Paul E. McKenney <paulmck@kernel.org>
Tested-by: Paul E. McKenney <paulmck@kernel.org>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Link: https://lkml.kernel.org/r/20200622125649.GC576871@hirez.programming.kicks-ass.net
Signed-off-by: Adam W. Willis <return.of.octobot@gmail.com>
Change-Id: If5f735e71f151983fa8e08e623770b195a20dcce
Signed-off-by: fadlyas07 <mhmmdfdlyas@gmail.com>

---
## [Historical-Expansion-Mod/Greater-Flavor-Mod](https://github.com/Historical-Expansion-Mod/Greater-Flavor-Mod)@[bea7170fe5...](https://github.com/Historical-Expansion-Mod/Greater-Flavor-Mod/commit/bea7170fe5c2376e5dcb75736aa3fdfb154b3524)
#### Tuesday 2022-08-30 19:48:27 by Dukeçza Victor

fuck you Devourer of Gods

Also Abe if you're reading this can I please reorganize the 1830 decisions/events and loc
having it all in one file really sucks i promise this is not a Davi moment I just want to have something to work on

---
## [aforren1/Psychtoolbox-3](https://github.com/aforren1/Psychtoolbox-3)@[9938a58d01...](https://github.com/aforren1/Psychtoolbox-3/commit/9938a58d01694775a714b49dabec2b1e94527f64)
#### Tuesday 2022-08-30 20:08:03 by Mario Kleiner

PsychLinuxConfiguration: Add workarounds for RaspberryPi OS 11 Mesa v3d.

Testing after upgrading the RPi 400 to Raspbian 11 showed new trouble:

At least on Mesa's gallium v3d driver for the RPi 4/400's VideoCore 6
gpu, Raspbian 11 Bullseye, page-flipping is broken by default - again.
Pageflipping for fullscreen OpenGL PTB onscreen windows fails, with
error messages flooding the XOrg log, and the copyswap fallback causes
PTB timing failures and horrible tearing.

The RPi desktop GUI composited by the Mutter X11 desktop compositor
doesn't have that problem, because Mesa for Raspbian 11 was patched
with some out-of-tree downstream patches to accept a new secret
parameter "v3d_maintain_ignorable_scanout" that if set to true allows
to fix pageflipping, but defaults to false == broken. God knows why
"broken by default" was considered an appropriate config choice, but
here we are...

Reference link to the patch series, which is not to be found anywhere
else with a Google search, and not yet in Mesa main upstream:

https://gitlab.freedesktop.org/mesa/mesa/-/issues/6079
https://github.com/bluestang2006/Debian-Pkgs/tree/master/mesa/debian/patches

This adds the magic parameter to fix pageflipping for octave + PTB
to the deep color config file and updates PsychLinuxConfiguration to
always force-install/update that file on ARM systems. I'm too lazy
to add extra config files and revalidate stuff, so we stuff it into
an unrelated Mesa config file.

This should fix PTB on RPi OS 11 on RPi 4/400.

---
## [KZiemian/julia](https://github.com/KZiemian/julia)@[62e0729dbc...](https://github.com/KZiemian/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Tuesday 2022-08-30 20:46:25 by Mirek Kratochvil

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
## [aforren1/Psychtoolbox-3](https://github.com/aforren1/Psychtoolbox-3)@[c4e7808150...](https://github.com/aforren1/Psychtoolbox-3/commit/c4e7808150009caa232767696d32f91063b4f2e4)
#### Tuesday 2022-08-30 20:57:08 by kleinerm

Merge pull request #775 from kleinerm/master

Pull for 3.0.18.11 update

This is mostly a release with smaller quality of life improvements, some bug/compatibility fixes, and more work to take advantage of new Ubuntu 22.04-LTS features and improvements.

### General

- Various help text and documentation updates. Minor cleanups and improvements, maintenance work etc.

- PsychVRHMD: Prep work for future OpenXR driver, and some cleanups and minor fixes.

- PsychPortAudio: Add new AM modulator flag 256 "kPortAudioAMModulatorNeutralIsZero". By default, a stopped AM modulator device acts as if no AM modulator is attached. With this flag set, while attached to an audio output slave device, it will instead "gate" or "mute" sound output on its associated audio output device, iow. the AM gain value during stopped modulator is zero instead of one. This has proven useful to allow to output tone bursts that are windowed/gated/modulated by an envelope function. Sponsored by a paid support membership - Thanks.

- Eyelink: Fix potential false "buffer overflow" alert in 'EyelinkGetQueuedData', which can cause Octave/Matlab to abort() as a false alarm. Sponsored by SR-Research, paying members of our partnership program - Thanks.

### Linux

- XOrgConfCreator: Split up into a legacy version for systems with X-Server 1.20 and earlier, e.g., Ubuntu 20.04-LTS, and a modern version for systems with X-Server 21 and later, e.g., Ubuntu 22.04-LTS. The legacy version is now in maintenance mode, frozen in its behaviour for old systems. The X-Server 21 / Ubuntu 22.04-LTS version was cleaned up, extended and made more plug and play. It hides some rarely needed (for normal users) options behind a "expert mode" flag, simplifies the questions it asks to users, streamlines the whole setup experience, and exposes some new functionality only available on modern X-Server 21, e.g., AsyncFlipSecondaries support for clone/mirror display setups (subject + experimenter displays) which are not synchronized. Improvements to deep color setup, Prime renderoffload "Optimus" setup, VRR setup etc.

- Deal better with problems in AssertOpenGL, giving better troubleshooting advice -- now updated for Ubuntu 22.04-LTS

- Gamepad/GetGamepadIndices: Refinements for Linux/X11, help text updates. Make selection of the proper GamePad / Joystick device more simple and robust. This work supported by a Psychtoolbox paid support membership - Thanks.

### macOS

- PsychVulkan: Add a new workaround for another macOS Metal bug. Make visual presentation timing it a bit better, but still quite awful.

- Screen('AddFrameToMovie'): Change mapping of 'rect' to actual capture area. The old math didn't determine vertical start position of the capture rectangle by rect(kPsychTop), but based on rect(kPsychBottom), which could cause inconsistencies on movie frame capture area on macOS with Retina displays in Retina backwards compatibility mode. The new math fixes this, to deal with Retina displays better.

- Maybe restore backwards compatibility of Psychtoolbox 3.0.18 with macOS versions older than 10.15 Catalina, possibly back to 10.11 El Capitan with fixes to Screen and PsychPortAudio. This is untested, due to lack of any macOS test systems other than 10.15.7 Catalina final, but may work. Maintaining backwards compatibility is difficult without test systems and the constant breakage introduced by the iToys company in more recent SDK's and compiler toolchains. Officially we don't guarantee that current 3.0.18 runs on anything but Catalina.

---
## [GustMartins/arc.codes](https://github.com/GustMartins/arc.codes)@[60afd55cea...](https://github.com/GustMartins/arc.codes/commit/60afd55ceac779d7c9129b1be1a533d9e090c244)
#### Tuesday 2022-08-30 21:40:54 by Aaron Hans

add SET to the UpdateExpression

Hello, I am using architect for a few projects and am really impressed with what you have built here. This is an amazing tool which helps a frontend focused dev like myself quickly setup a solid serverless backend. Thanks so much for building and open sourcing all this fantastic stuff. I love the latest documentation, all these examples make it so much clearer how to work with DynamodB via architect. I needed to add that SET expression in order to get my copy pasted version of this example working.

Thank you!

---
## [mars-sim/mars-sim](https://github.com/mars-sim/mars-sim)@[3fa5bad73f...](https://github.com/mars-sim/mars-sim/commit/3fa5bad73f1155e22dabb4949c86d6f1f5040242)
#### Tuesday 2022-08-30 22:06:44 by mokun

Define and display 4 meal times for Cooking tab

08/30/2022

- add: create getMealTimeString(), getTimeDifference() and
       getMealTime() in CookMeal
- add: showcase the start & end of 4 meal times in TabPanelCooking
       - Breakfast
	   - Lunch
	   - Dinner
	   - Midnight
- change: rework isMealTime() in CookMeal
- change: rework goForFood() in EatDrink
- change: adjust modifiers in modifyWasteResource() in
AmountResourceGood
- change: revise getTaskDescription(boolean subTask) in
        TaskManager

https://github.com/mars-sim/mars-sim/issues/673

---
## [oxidecomputer/opte](https://github.com/oxidecomputer/opte)@[8b42d0a886...](https://github.com/oxidecomputer/opte/commit/8b42d0a886315ebb79c52ccc36da630431c30e35)
#### Tuesday 2022-08-30 23:34:36 by Ryan Zezeski

HeaderAction::Modify should not panic on missing metadata (#241)

The main thrust of this commit is to fix #241 by allowing a
`HeaderAction` to return an error result. Some other stuff came along
for the ride.

- add some basic kstats support (#23)

  With yet another possible runtime error I thought it was high time
  we had some kstats support. There is already good SDT support in
  OPTE, but if you're not running DTrace when an error occurs, you're
  not going to know it happened. Having kstats allows us to track
  historical failures/errors and provide a clue as to where to look
  when debugging live.

  While trying to implement kstats I realized that I need to change
  the locking scheme in OPTE. OPTE was my first real Rust project; a
  packet transformation engine running Rust in the illumos kernel --
  it was a lot to take on for a first Rust project. I brought a lot of
  my previous knowledge to bear from working on the illumos networking
  stack, particularly the mac module. From this past knowledge my
  initial architecture relied on a lot of Arc + fine-grained locks
  inside of the engine, as this is the structure I was used to seeing
  inside illumos.

  When trying to implement kstats I realized that I would have to wrap
  a mutex around a group of named kstats...and that just felt weird
  compared to how we do it in most illumos network drivers.
  Furthermore, the fine-grained locking I had in place wasn't actually
  completely correct, and relied on some hard-to-understand comments
  and non-idiomatic Rust code. Then I had the thought that I should
  really be treating an individual Port more like a Tx/Rx ring that you
  would find in a network driver, where the entire ring is locked
  during processing. In this sense the entire Port should be wrapped
  in a mutex, knowing that any state changed inside that Port is
  atomic in respect to a given packet (or chain of packets). If and
  when this proves to be a limiting factor, you can then start
  breaking things out at a higher level, like having each Port broken
  out into concurrent streams for different protocol types: like TCP,
  UDP, and Other. If that becomes a bottleneck you could then possibly
  break each protocol out further into rings, assuming you could find
  a way to consistently hash flows to their appropriate ring.
  Furthermore, the happy path for an active flow is always hitting the
  UFT. There may be ways to structure the UFT such that it can be
  queried without a mutex, perhaps with some type of scheme that uses
  asynchronous updates of a persistent (read functional) data structure
  plus atomic pointer swaps. The point being, there are higher-level
  ways to reduce contention than the fine grained locking scheme I had
  used up to this point.

- Renamed `ModActionArg` to `ModifyActionArg`, because I kept
  confusing `Mod` with "module" in my head, and I wrote this damn
  code!

- Renamed `HT` to `HdrTransform` to make it a bit more obvious what it
  refers to.

---

