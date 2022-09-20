## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-19](docs/good-messages/2022/2022-09-19.md)


2,282,856 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,282,856 were push events containing 3,322,919 commit messages that amount to 240,594,391 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 31 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f923f61011...](https://github.com/tgstation/tgstation/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Monday 2022-09-19 00:06:39 by MMMiracles

Tramstation: Modular Maintenance Insanity (#69000)

About The Pull Request
Every single part of maintenance has been segmented into modules with multiple variants with different themes. As it stands, there are currently 80 modular parts that come together to form the entire maintenance layout for both levels. Part 1 of a 2 part PR set, requires #69486 to have full effect.

Why It's Good For The Game
Maintenance as it stands is a bit barren, not much reason to explore it with boring same-same rooms despite current randomized modules. With these issues in mind, I completely scrapped maintenance as it was and rebuilt it in mind with full modular segments with proper documentation on what each piece is and where it is located. These changes were also designed to make maintenance more friendly for our dark-dwelling antags and xenos alike, as each major module now has an air vent and scrubber.

Fixes #68320

Main Event:

Every single part of maintenance was turned into module chunks. Sections of the map that originally had maintenance was traced out with checkered flooring so mappers can still see the general layout of the tunnels when making larger edits.
Every module has been documented with proper nodes with descriptions of where each module is located on the map.
Each main module has a regular variant and an abandoned variant. Abandoned variants have blocked access routes and look more like unfinished carved out tunnels than regular maintenance.
Each module has 2 attachment points barring 2. Each attachment has 3 potential layouts that are chosen each round. A storage room with construction supplies one round might be a carved out room with minerals the next.
QoL/General Fixes:

Maintenance should have much more xeno/antag spawns to give various mid-round antags better chances at starting.
Camera network has been given a once-over with duplicate/floating cameras fixed.
The helpful bots in the lower tunnel should now actually do full rotations instead of whatever the hell they were doing before.
I still need to do some testing with disposals and final touch ups to make sure there aren't any weird overlaps, but as of right now the actual mapping quality is ready for review.

---
## [hspsh/esp-keystore](https://github.com/hspsh/esp-keystore)@[f17c979d0b...](https://github.com/hspsh/esp-keystore/commit/f17c979d0bf4ad4c229d7bc1b7882fa5f92acfd3)
#### Monday 2022-09-19 00:08:32 by psuwala

it should be fucking working but of course C++ is just a bunch of fucking shit for retarded people, I hope that inventors die eating their own shit

---
## [ThatGuySam/marvelorder](https://github.com/ThatGuySam/marvelorder)@[7c1b22bef1...](https://github.com/ThatGuySam/marvelorder/commit/7c1b22bef18b9712b3f1db4326690424eeaa26de)
#### Monday 2022-09-19 00:26:05 by flat-data

Flat: latest data (2022-09-19T00:26:04.732Z)
{
  "date": "2022-09-19T00:26:04.732Z",
  "files": [
    {
      "name": "src/pages/en/listings.json",
      "deltaBytes": 28,
      "source": "https://raw.githubusercontent.com/ThatGuySam/marvelorder/main/README.md"
    },
    {
      "name": "src/pages/en/madame-web-634492.md",
      "deltaBytes": 30,
      "source": "https://raw.githubusercontent.com/ThatGuySam/marvelorder/main/README.md"
    },
    {
      "name": "src/pages/en/marvels-spidey-and-his-amazing-friends-127635.md",
      "deltaBytes": 0,
      "source": "https://raw.githubusercontent.com/ThatGuySam/marvelorder/main/README.md"
    },
    {
      "name": "src/pages/en/moon-knight-92749.md",
      "deltaBytes": -2,
      "source": "https://raw.githubusercontent.com/ThatGuySam/marvelorder/main/README.md"
    },
    {
      "name": "src/pages/en/werewolf-by-night-894205.md",
      "deltaBytes": 0,
      "source": "https://raw.githubusercontent.com/ThatGuySam/marvelorder/main/README.md"
    }
  ]
}

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[6eb90d6495...](https://github.com/ammarfaizi2/linux-fork/commit/6eb90d6495376b6d09b065ec6a65247c8be73ad5)
#### Monday 2022-09-19 00:51:09 by Johannes Weiner

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[bd47e117e8...](https://github.com/treckstar/yolo-octo-hipster/commit/bd47e117e8af701afdfa39a255c6b62851251907)
#### Monday 2022-09-19 01:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [jjpark-kb/Skyrat-tg](https://github.com/jjpark-kb/Skyrat-tg)@[00d7e1f375...](https://github.com/jjpark-kb/Skyrat-tg/commit/00d7e1f375b7f6f55f71d77be8c7612a6a5d6030)
#### Monday 2022-09-19 01:22:27 by SkyratBot

[MIRROR] Rocking The Boat, er, Map Vote [MDB IGNORE] (#16083)

* Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

* Rocking The Boat, er, Map Vote

Co-authored-by: san7890 <the@san7890.com>

---
## [YMHHHH/react](https://github.com/YMHHHH/react)@[b6978bc38f...](https://github.com/YMHHHH/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Monday 2022-09-19 01:55:07 by Andrew Clark

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
## [Mojave-Sun/mojave-sun-13](https://github.com/Mojave-Sun/mojave-sun-13)@[736422fac8...](https://github.com/Mojave-Sun/mojave-sun-13/commit/736422fac8d84c8e054853fd2b205cc993250c21)
#### Monday 2022-09-19 02:46:54 by Technobug14

Field Transfusions & Fixes Sprites/Runtime (#2152)

* Working field transfusions

As far as I can tell, no runtimes or bugs. Should be good to go. Could maybe do with some polish? But otherwise it works great.

* Fixes energy weapon bugs

Fixes a runtime related to emptying cells from energy weapons, and fixes an overlay bug and inventory icon bug on the cells themselves.

* Bug fixes

read above, fixes a few bugs/errors

* Broken as hell

Supposed to add new IV bag sprites and overlays that would change as the bag gets emptier. Multiple bugs both with transfusion and the icon/overlay. Right now, the icon currently disappears once the object is on the ground and I can't tell why. Secondly, the overlay has the visual bugs and could probably do with a more thorough system to apply it? The bugs on transfusion are mostly due to a lack of sanity checks, where it will continue to be attached to someone from many tiles away when thrown/dropped, etc.

* Shit

HATE HATE HATE this sucks and it is buggy as hell

* Fix icon/overlay updates

* Mostly working

Still some broken stuff, you can attach IV bags if you're not next to someone and do it from inside containers, also fixes the world states for the police and military 10mm pistol

* Finishing touches

Couple of bug fixes, fixes 10mm police/military world sprite, etc etc. Should be good to go.

Co-authored-by: Koshenko <koshenko@pm.me>
Co-authored-by: Koshenko <53068134+Koshenko@users.noreply.github.com>

---
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[f490a226b2...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/f490a226b241795abefbddeb84938af4e183b2a8)
#### Monday 2022-09-19 04:10:38 by Gelatelly

sassy shepherd

makes shepherd lie like the bitch he is

I HATE RUNTIMES I HATE RUNTIMES I HATERUNTIMES

use the shittiest method in existence to bypass runtimes, unfortunately I couldn't use initial() without adding some issues so fuck me I guess

updates the people and abno list

imagine using signalers

why is there a huge gap there

leftovercode that doesn't do anything

linter fix?

this is the worst fix I hate linters so much

I'm making everything worse by trying to fix it

send help

adds abno spawn signaller

I love adding signallers for meme PR

changes how the lists are used/rename a few things

SLightCamelCaseChange

clears the people_list on destroy()

this isn't much but it should avoid some problems

moves the abno spawn signal to lobotomy_corp.dm

---
## [Voltaic314/Daily-FB-Poster-For-Python-Betty-White-Bot](https://github.com/Voltaic314/Daily-FB-Poster-For-Python-Betty-White-Bot)@[a246fadb4b...](https://github.com/Voltaic314/Daily-FB-Poster-For-Python-Betty-White-Bot/commit/a246fadb4b2180d9ac775416bdec43117cbb04c1)
#### Monday 2022-09-19 05:00:38 by Logan Maupin

Heavily refactored & now just posts she's dead

As the title suggests, I refactored the hell out of this code to add in a lot more formal formatting. 

but also on top of that, I modified the code to no longer use the list of 9 possible statuses like it was before. Personally just because I thought it was getting very repetitive over and over. (How many ways can you say someone is dead in a funny way?). 

Now it will just say "She's Dead." every day like it used to before. Anyway, I'm pretty much done with this project but wanted to give it one final touch up before letting it stay automated and never touching the code again. It's been fun. Time to move onto bigger and better things. 

Truth be told I don't even touch meme bot or nature bot anymore either. But I have nothing to add to them without doing a BUNCH more code to them that I'm not motivated to do anymore. 

Anyway, check out the rest of my repos, I may be working on something cooler. Otherwise, thanks for everything friends. o7

---
## [ThakaSartu/saa2](https://github.com/ThakaSartu/saa2)@[3171c10459...](https://github.com/ThakaSartu/saa2/commit/3171c10459aa537e7d645cbc3101d30bce732eef)
#### Monday 2022-09-19 05:00:49 by ThakaSartu

<iframe width="100%" height="480" src="https://www.youtube.com/embed/lqgQMvDw-K8" title="Waka TM: New Eritrean comedy 2022 (Gual Hadera) #Semhar Mesfn ጓል ሓደራ #ሰምሃር መስፍን" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# [የምስጢረ ስላሴ እና የሰው ተፈጥሮ ትምህርት እና የተሃድሶ (በግ ለምድ) ዘመቻ በመምህር ዶ/ር ዘበነ ለማ (Memher Dr Zebene Lemma)](https://www.youtube.com/watch?v=9OWX9q-YJMY)
# የብራናገፅ #ትረካ መፅሐፈ ሔኖክ ኢትዮጵያዊ - ሙሉ ትረካ 
## የብራናገፅ #ትረካ መፅሐፈ ሔኖክ ኢትዮጵያዊ - ሙሉ ትረካ 
[The Book Of Enoch Ethiopian](https://www.youtube.com/watch?v=KIChceXNWE0)
[Bible audio wisdom Jeshua son of Sirak from 1-25 መጽሓፍ ቅዱስ ብድምጺ፡ መጽሓፍ ጥበብ ኢያሱ ወዲ ሲራክ ካብ ምዕራፍ 1-25](https://www.youtube.com/watch?v=NCVnkQYeI9c)
<hr>
<iframe width="100%" height="480" src="https://www.youtube.com/embed/ZglMKqszOco" title="LIGHT: THE SPIRIT SCIENCE MOVIE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<hr>

# Carl Jung on Alchemy
<iframe width="100%" height="400" src="https://www.youtube.com/embed/2AMu-G51yTY" title="Face To Face  |  Carl Gustav Jung (1959) HQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

![##CARL_JUNG](https://careerassessmentsite.com/wp-content/uploads/2015/11/Carl-Jung-.jpg)
[Psychology and Alchemy by Carl Jung (1968) [Part I]](https://www.youtube.com/watch?v=COvafdy108A&t=8s)
[The Undiscovered Self, by Carl Jung (audiobook)](https://www.youtube.com/watch?v=doAlX2WIpGk)
[Carl Gustav Jung - Approaching The Unconscious - Psychology audiobooks](https://youtu.be/xZSbffrftd0)
[Face To Face | Carl Gustav Jung (1959) HQ](https://www.youtube.com/watch?v=2AMu-G51yTY)
[Carl Gustav Jung - Approaching The Unconscious - Psychology audiobooks](https://youtu.be/xZSbffrftd0)
[Christ, a Symbol of the Self, by Carl Jung (audiobook)](https://www.youtube.com/watch?v=3xU2AMOdkEc)
[Carl Gustav Jung - Man and his symbols parts 1-2 - Psychology audiobooks](https://www.youtube.com/watch?v=RyiccI0PZxM)
[Carl Jung - Memories, Dreams, Reflections](https://www.youtube.com/watch?v=qE262Bt40SI)
['Man and his Symbols' Carl G Jung Part 1](https://www.youtube.com/watch?v=ZIz5P3zketE)
[Carl Sagan's 1994 "Lost" Lecture: The Age of Exploration](https://www.youtube.com/watch?v=6_-jtyhAVTc)
[HIDDEN MATHEMATICS - Randall Carlson - Ancient Knowledge of Space, Time & Cosmic Cycles](https://www.youtube.com/watch?v=R7oyZGW99os)
[THE HERMETICA The Lost Wisdom of the Pharaohs - AUDIOBOOK || Timothy Freke & Peter Gandy](https://www.youtube.com/watch?v=N7hrzOCxaIE)
[The Tibetan Book of Living and Dying. Malditasweet](https://www.youtube.com/watch?v=pPKbxpT7Z0c&t=3158s)
[SciCafe: Life the Universe and Everything with Neil deGrasse Tyson](https://www.youtube.com/watch?v=4KRZQQ_eICo)

---
## [bearrrrrrrr/coyote-bayou](https://github.com/bearrrrrrrr/coyote-bayou)@[2062e298a0...](https://github.com/bearrrrrrrr/coyote-bayou/commit/2062e298a06759209a0f3832362b4d750c10a9be)
#### Monday 2022-09-19 05:14:28 by Tk420634

Slows Knife Raiders, and their buddies attacks a bit.

Haha, fucked that up didn't I?  We do a little shitting.  Also lowered some damages on rapid_meleeing mobs

---
## [ProjectVelvet/android_kernel_sm6250](https://github.com/ProjectVelvet/android_kernel_sm6250)@[367d6cfe22...](https://github.com/ProjectVelvet/android_kernel_sm6250/commit/367d6cfe229cdaba624ea19f1c5d8e3c6fa62c70)
#### Monday 2022-09-19 05:55:39 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5
Signed-off-by: Excalibur-99 <txexcalibur99@gmail.com>

---
## [optimumtact/tg-station](https://github.com/optimumtact/tg-station)@[ad01ab5ed0...](https://github.com/optimumtact/tg-station/commit/ad01ab5ed0a5f80278076b1e0e6ac33fe73b0e32)
#### Monday 2022-09-19 06:41:19 by LemonInTheDark

Fixes asset caching (#69852)

The asset was being loaded, seeing that fully_generated is false, so it
attempts to rebuild. The rebuilding clears the existing file cache, and
fucks us.

Life is pain.

---
## [IvanYashchuk/pytorch](https://github.com/IvanYashchuk/pytorch)@[afcc7c7f5c...](https://github.com/IvanYashchuk/pytorch/commit/afcc7c7f5c7cef740241ff0abdae8d4f2ad22a03)
#### Monday 2022-09-19 07:00:45 by Andrew Gu

[FSDP] Generalize prefetching; lower unshard/reshard to handle (#83665)

### Additional Constructor Changes
- `self.sharding_strategy`
    - If the world size is 1, I clamp the sharding strategy to `NO_SHARD`, regardless of the passed-in sharding strategy, since the behavior is fully equivalent. This absolves the need for `p._is_sharded or self.world_size == 1` checks in the core code. Once we fully shift the paradigm to using handles, this should result in a clear net positive. However, for now, we still have some places where we interface directly with the `FlatParameter`, in which case we have some temporary hacky code.
- `HandleConfig`
    - As a part of the new design abstraction, much logic is lowered to the `FlatParamHandle`. This requires the handle be aware of mixed precision, CPU offloading, sharding strategy, and the process group (for world size > 1). To be less error-prone, I re-defined the `dataclass`s and `enum`s for the handle. These can be removed and coalesced with the existing ones.
    - The drawback is that the `FlattenParamsWrapper` constructor now takes in the `HandleConfig` to forward it to the `FlatParamHandle` constructor. I tolerate this since we plan to retire the FPW. For now, the handle's process group attributes are set later when we call `handle.shard()`.
    - We will dive into this logic lowering later. For now, the idea is we need to pass some extra info to the handle, which must go through the FPW.
- `FullyShardedDataParallel._shard_parameters()` -> `FlatParamHandle.shard()`
- [Important] Generalizing attributes to remove the 1 `FullyShardedDataParallel` : 1 `FlatParameter` assumption
    - **Before:** `_fsdp_graph_order`, `_pre_backward_hook_full_params_prefetched`, `_forward_full_params_prefetched`, `reshard_after_forward` are with respect to 1 `FullyShardedDataParallel`
    - **After:** (1) We use `FlatParamHandle` in place of `FullyShardedDataParallel`. (2) The atomic unit for forward and pre-backward is a _group_ of handles involved in the same module's forward/pre-backward. This is represented as `Tuple[FlatParamHandle, ...]`. For now, this is **always a singleton tuple**, but this shift enables a module having multiple FSDP parameters (which we have use cases for).
- `_reset_lazy_init()` attributes
    - The prefetched flags are merged into `self._handles_prefetched`, which is directly defined in the constructor. `reshard_after_forward` is retired since it can be fully determined by other attributes (`_is_root` and `sharding_strategy`).

## FSDP Runtime: Unshard

The first step is to read the existing `_rebuild_full_params()`. A few notable observations:
- It returns `Tuple[Tensor, bool]`. The first element is the _padded unsharded flattened parameter_, and the second element is whether we can free it upon exiting `summon_full_params()`. This return value is **only used in `summon_full_params()`**.
- If parameter mixed precision is enabled and the `FlatParameter` is already unsharded, then the low precision shard (`_mp_shard`) is still re-allocated on GPU. (It is freed at the end of the method.)
- If CPU offloading is enabled and the `FlatParameter` is already unsharded, then there is a no-op `p.data = p.data.to(self.compute_device, non_blocking=True)`.
- Inside `summon_full_params()`, `mixed_precision_cast_ran` is always `False`. Therefore, the return value for the `not p._is_sharded and mixed_precision_cast_ran` branch is unused.
-`summon_full_params()` can only be called (before forward or after backward) or (between forward and backward). Given this, I cannot think of a case where we call `summon_full_params()`, the `FlatParameter` is already unsharded, but `reshard_after_forward` is `True`. The `FlatParameter` should be sharded (before forward or after backward), and the `FlatParameter` may only be unsharded (between forward and backward) if `reshard_after_forward` is `False`.
- If parameter mixed precision is enabled and the sharding strategy is a sharded one, then inside `summon_full_params()`, the `FlatParameter` is unsharded in full precision. This involves allocating a new padded unsharded flattened parameter on GPU in full precision since `_full_param_padded` is in the low precision.

Some comments:
- Ideally, we reduce the complexity of the core code path: i.e. unshard for forward and pre-backward. If the return value is only used for `summon_full_params()`, we should consider if we can compartmentalize that logic.
- The branching is complex, and some return values are never used, where this fact is not immediately obvious. We should see if we can reduce the branch complexity.

Disclaimer: The difference in attribute semantics between `NO_SHARD` and the sharded strategies makes it challenging to unify the cases. This PR does not attempt to address that since it requires more design thought. However, it does attempt to reduce the complexity for the sharded strategies.

### Unshard: Core Code Path
Let us trace through the new logical unshard.
1. `FullyShardedDataParallel._unshard(self, handles: List[FlatParamHandle], prepare_gradient: bool)`
    - This iterates over the handles and calls `handle.pre_unshard()`, `handle.unshard()`, and `handle.post_unshard(prepare_gradient)` in the all-gather stream.
2. `FlatParamHandle.needs_unshard(self)`
    - We take an aside to look at this key subroutine.
    - For `NO_SHARD`, this returns `False`.
    - For sharded strategies, this checks if the padded unsharded flattened parameter is allocated. The padded unsharded flattened parameter is the base tensor for the unpadded unsharded flattened parameter, which is a view into the padded one. Thus, the padded one's allocation fully determines if the `FlatParameter` is unsharded.
    - For sharded strategies, to accommodate the parameter mixed precision + `summon_full_params()` case, we introduce `_full_prec_full_param_padded`, which is the padded unsharded flattened parameter in full precision. The helper `_get_padded_unsharded_flat_param()` takes care of this casing and returns the padded unsharded flattened parameter. Instead of allocating a new tensor each time, we manually manage `_full_prec_full_param_padded`'s storage just like for `_full_param_padded`.
3. `FlatParamHandle.pre_unshard(self)`
    - For sharded strategies, the postcondition is that the handle's `FlatParameter` points to the tensor to all-gather. This should be on the communication device and in the desired precision. The allocation and usage of the low precision shard for parameter mixed precision and the CPU -> GPU copy for CPU offloading both classify naturally in the pre-unshard.
    - For sharded strategies, if the `FlatParameter` does not need to be unsharded, `pre_unshard()` is a no-op. This avoids unnecessarily allocating and freeing the low precision shard.
    - For `NO_SHARD`, we simply preserve the existing semantics.
4. `FlatParamHandle.unshard(self)`
    - If the handle was resharded without freeing the padded unsharded flattened parameter (e.g. `summon_full_params()` between forward and backward when `reshard_after_forward=False`), then the `FlatParameter` points to the sharded flattened parameter. We need to switch to using the unsharded parameter. This is a design choice. Alternatively, we may not switch to using the sharded flattened parameter in `reshard()` if we do not free the padded unsharded flattened parameter. However, the postcondition that the `FlatParameter` points to the sharded flattened parameter after `reshard()` is helpful logically, so I prefer this approach.
    - Otherwise, this allocates the padded unsharded flattened parameter, all-gathers, and switches to using the unpadded unsharded flattened parameter.
    - In the future, we may add an option to `unshard()` that additionally all-gathers the gradient.
5. `FlatParamHandle.post_unshard(self, prepare_gradient: bool)`
    - For sharded strategies, if using parameter mixed precision, this frees the low precision shard. More generally, this should free any sharded allocations made in `pre_unshard()` since the all-gather has been launched. If using CPU offloading, the GPU copy of the local shard goes out of scope after `unshard()` and is able to be garbage collected. **We should understand if there is any performance difference between manually freeing versus deferring to garbage collection since our usage is inconsistent.** For now, I preserve the existing semantics here.
    - `prepare_gradient` is meant to be set to `True` for the pre-backward unshard and `False` for the forward unshard. This runs the equivalent logic of `_prep_grads_for_backward()`.
    - This post-unshard logic (notably the gradient preparation) now runs in the all-gather stream, which is fine because we always have the current stream wait for the all-gather stream immediately after `FullyShardedDataParallel._unshard()`. IIUC, we do not need to call `_mp_shard.record_stream(current_stream)` (where `current_stream` is the default stream) because `_mp_shard` is allocated and freed in the same (all-gather) stream.
    - A postcondition is that the `FlatParameter` is on the compute device. It should also have the unpadded unsharded size (though I do not have a check for this at the moment).

### Unshard: `summon_full_params()`
Now that we see how the logical unshard has been reorganized for the core code path, let us dive into `summon_full_params()`.

The two constraints are:
1. If using parameter mixed precision, we should unshard in full precision.
2. We must determine if we should free the padded unsharded flattened parameter upon exiting.

The first constraint is addressed as described before in the core unshard code path, so it remains to explore the second constraint.

I propose a simple rule: **We free iff we actually unshard the `FlatParameter` in `summon_full_params()`** (i.e. it was not already unsharded). We perform a case analysis:

**Parameter mixed precision enabled:**
* `NO_SHARD`: `flat_param.data` points to `flat_param._local_shard`, which is the full precision unsharded flattened parameter. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We force full precision and all-gather to `_full_prec_full_param_padded`. We do not support `nested summon_full_params()`, so `_full_prec_full_param_padded` must be unallocated. We unshard, and it is **safe to free**.

**Parameter mixed precision disabled:**
* `NO_SHARD`: This is the same as with mixed precision enabled. This is **not safe to free**.
* `FULL_SHARD` / `SHARD_GRAD_OP`: We all-gather to `_full_param_padded`. It may already be unsharded.
    * Already unsharded: The unshard is a no-op. This is **not safe to free**.
        * For `FULL_SHARD`, this can happen for the root FSDP instance after `forward()` but before backward.
        * For `SHARD_GRAD_OP`, this can happen for all FSDP instances after `forward()` but before backward.
    * Needs unshard: We unshard. This is **safe to free**.

Therefore, we see that it is not safe to free when using `NO_SHARD` and when using a sharded strategy but the `FlatParameter` is already unsharded. This is precisely the proposed rule.

There were two notable edge cases that the existing code did not address.
1. The existing code tests if the `FlatParameter` is already unsharded by checking the allocation status of `_full_param_padded`. When using parameter mixed precision, this is the incorrect tensor to check. If `_full_param_padded` is allocated (e.g. when `reshard_after_forward=False` and calling `summon_full_params()` between forward and backward), the already-unsharded check is a false positive, and `summon_full_params()` does not correctly force full precision. https://github.com/pytorch/pytorch/issues/83068
    - This PR's `needs_unshard()` check correctly routes to the appropriate padded unsharded flattened parameter depending on the calling context (i.e. if it needs to force full precision or not).
2. The existing code does not free the GPU copy of the padded unsharded flattened parameter when calling `summon_full_params(offload_to_cpu=True)`. It unshards the `FlatParameter`, moves the padded unsharded flattened parameter to CPU, and sets the `FlatParameter` data to be the appropriate unpadded view into the padded unsharded flattened parameter on CPU. However, `_full_param_padded` still points to the all-gathered padded unsharded flattened parameter on GPU, which is kept in memory. https://github.com/pytorch/pytorch/issues/83076
    - This PR frees the GPU copy and reallocates it upon exiting `summon_full_params()`. This is essential for avoiding peak GPU memory usage from increasing as we recurse through the module tree. There may be some cases where we can avoid reallocation altogether, but that can be addressed in a follow-up PR.
    - This PR offloads the *unpadded* unsharded flattened parameter to CPU directly instead of the *padded* one. As far as I can tell, there is no need to include the padding since unflattening the original parameters does not require the padding.
    - The relevant code is in the context manager `FlatParamHandle.to_cpu()`.

### Unshard: Mixed-Precision Stream

This PR removes the mixed precision stream usage. As is, I do not think there is any extra overlap being achieved by the stream usage.

The low precision shard is allocated and copied to in the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1401-L1412)), and the current stream (in this case the all-gather stream) waits for the mixed precision stream ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L1414)). However, we immediately schedule an all-gather that communicates that exact low precision shard ([code](https://github.com/pytorch/pytorch/blob/1f99bdfcc4a3f97d28471a531d2b69def762f6ba/torch/distributed/fsdp/fully_sharded_data_parallel.py#L3338)) with no other meaningful computation between. If we remove the mixed precision stream, the low precision shard is allocated and copied to in the all-gather stream (including the non-blocking CPU -> GPU copy if using CPU offloading).

Under this PR's design, we may consider a "pre-unshard" stream for all logical pre-unshard data transfers if we want to overlap in the future. IIUC, the overlap opportunity exists if there are multiple `FlatParameter`s per module, and we only have the all-gather stream wait for the data transfer corresponding to the local shard it communicates, not the others.

If we agree on removing the mixed-precision stream for now, I will remember to delete it from `_init_streams()`.

## FSDP Runtime: Reshard

Like with unshard, the first step is the look at the existing `_free_full_params()` and `_use_param_local_shard()`. A few notable observations:
- For only `NO_SHARD`, `_free_full_params()` includes a call to `_free_mp_shard()`.
- For `summon_full_params()`, there is a separate `_free_full_params_and_use_local_shard()` that duplicates the main logic of `_free_full_params()` and calls `_use_param_local_shard()`.
- In `forward()`, if `reshard_after_forward=True`, we call `_free_full_params()` and then `_free_mp_shard()`. Hence, for `NO_SHARD`, the `_free_mp_shard()` is a no-op.
- In the post-backward hook, we typically call `_free_full_params()` and `_free_mp_shard()`. The `_free_mp_shard()` is a no-op for `NO_SHARD` and if `reshard_after_forward=True`.

Some comments:
- The code certainly works, but some of the no-ops are subtle. When possible, we should make it clear when calls are no-ops or not. It is good that the existing code documents that `_free_mp_shard()` is a no-op in the post-backward hook when `reshard_after_forward=True`. However, there are still some non-obvious no-ops (around `NO_SHARD`).
- We should see if we can avoid the duplicate `_free_full_params_and_use_local_shard()`.

Let us trace through the logical reshard:
1. `FullyShardedDataParallel._reshard(self, handles: List[FlatParamHandle], free_unsharded_flat_params: List[bool])`
    - The two args should have the same length since they are to be zipped.
    - The goal of having `free_unsharded_flat_params` is that the caller should be explicit about whether the (padded) unsharded flattened parameter should be freed. The low precision shard is always meant to be freed (as early as possible), so there is no corresponding `List[bool]`.
2. `FlatParamHandle.reshard(self, free_unsharded_flat_param: bool)`
    - This frees the (padded) unsharded flattened parameter if `free_unsharded_flat_param` and switches to using the sharded flattened parameter.
    - Echoing back to forcing full precision in `summon_full_params()`, `_free_unsharded_flat_param()` frees the correct tensor by using `_get_padded_unsharded_flat_parameter()`.
3. `FlatParamHandle.post_reshard(self)`
    - I am not fully content with the existence of this method, but this seems to be an unavoidable consequence of `NO_SHARD`. Perhaps, this may be useful in the future for other reasons though.
    - Right now, this method is only meaningful for `NO_SHARD` + parameter mixed precision + outside `summon_full_params()`. `_mp_shard` is not freed in the post-unshard since it is also the low precision _unsharded_ flattened parameter, so we must delay the free until the the post-reshard.

Below the `FlatParamHandle.reshard()` and `post_reshard()` layer, there should not be any no-ops.

One final comment I will mention is that I like the `pre_unshard()`, `unshard()`, `post_unshard()`, and `reshard()`, `post_reshard()` organization because it makes it clear what the boundaries are and their temporal relationship. Through that, we can set pre- and post-conditions. Furthermore, we can eventually convert logic to hooks that may be registered on the `FlatParamHandle` (for `pre_unshard()`, `post_unshard()`, and `post_reshard()`). This may improve the customizability of FSDP.

 ## FSDP Runtime: `forward()`

- This PR reorganizes `forward()` in preparation for non-recursive wrapping, which uses pre-forward and post-forward hooks that expect the signature `hook(module, input)`. For FSDP, the `module` and `input` arguments are not used.
- This PR creates a new method `_fsdp_root_pre_forward()` to handle the logic only the root FSDP should run.

## FSDP Prefetching

Finally, we dive into the prefetching changes. Some highlights:
1. This PR unifies the execution order validation and prefetching implementations.
    - Both involve the execution order and can be unified to share some boilerplate.
2. Execution order validation only runs when the distributed debug level is `INFO`.
    - We have yet to have one success case where we actually catch an unintended source of dynamism. The warning is also too verbose. Hence, we are gating it by the `INFO` level.
3. This PR moves prefetching to be with respect to groups of handles (as mentioned in the constructor comment).
    - This is essential for supporting prefetching with non-recursive wrapping.
4. This PR does not include "bubbles", i.e. modules with no handles, in the recorded execution order(s). This deviates from the existing implementation.
    - This makes prefetching possibly more aggressive (when there are such bubbles), but it should not have significant performance implications either way.
5. This PR changes backward prefetching to reset the post-forward order each iteration (as intended).
6. This PR changes forward prefetching to use the first iteration's pre-forward order instead of the first iteration's post-forward order. (We can discuss whether we want this in this PR or not. Otherwise, I can keep it as using the post-forward order to preserve the existing semantics.) This PR also removes the `all_gather_stream.wait_stream(current_stream)` before forward prefetching because it does not help with high GPU reserved memory. We can add that back if desired.

### Appendix
#### Reverse Post-Forward Order Is Not Always the Pre-Backward Order
The existing PT-D FSDP pre-backward prefetching uses the reverse post-forward order.
<details>
  <summary>Model Code</summary>

  ```
  class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.block1 = nn.Sequential(
            nn.Conv2d(3, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=True),
        )
        self.block2 = nn.Sequential(
            nn.Conv2d(4, 4, kernel_size=3),
            nn.BatchNorm2d(4),
            nn.ReLU(inplace=False),
        )
        self.block3 = nn.Linear(12, 8)
        self.head = nn.Sequential(
            nn.AdaptiveAvgPool2d(output_size=(1, 1)),
            nn.Flatten(),
            nn.Linear(4, 10),
        )

    def forward(self, x):
        x = self.block1(x)
        x = self.block2(x)
        x = self.block3(x)
        return self.head(x)

  model = Model().cuda()
  fsdp_kwargs = {}
  model.block1[1] = FSDP(model.block1[1], **fsdp_kwargs)  # BN2d
  model.block2[1] = FSDP(model.block2[1], **fsdp_kwargs)  # BN2d
  model.block1 = FSDP(model.block1, **fsdp_kwargs)
  model.block2 = FSDP(model.block2, **fsdp_kwargs)
  model.block3 = FSDP(model.block3, **fsdp_kwargs)
  model = FSDP(model, **fsdp_kwargs)
  ```
</details>

<details>
  <summary>Execution Orders </summary>

  ```
  Pre-backward hook for ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  Pre-backward hook for ('weight', 'bias') 140339461194656 (block3)
  Pre-backward hook for ('0.weight', '0.bias') 140339520589776 (block2)
  Pre-backward hook for ('weight', 'bias') 140339520587664 (block2 BN)
  Pre-backward hook for ('weight', 'bias') 140339520586656 (block1 BN)
  Pre-backward hook for ('0.weight', '0.bias') 140339520588768 (block1)

  Pre-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('weight', 'bias') 140339461194656 (block3)

  Reverse post-forward order:
  ('head.2.weight', 'head.2.bias') 140339520587136 (model)
  ('weight', 'bias') 140339461194656 (block3)
  ('0.weight', '0.bias') 140339520589776 (block2)
  ('weight', 'bias') 140339520587664 (block2 BN)
  ('0.weight', '0.bias') 140339520588768 (block1)
  ('weight', 'bias') 140339520586656 (block1 BN)
  ```
</details>

Differential Revision: [D39293429](https://our.internmc.facebook.com/intern/diff/D39293429)
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83665
Approved by: https://github.com/zhaojuanmao

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[b3b85cae9b...](https://github.com/odoo-dev/odoo/commit/b3b85cae9b1951b82053d7c6b55e559cbc48307d)
#### Monday 2022-09-19 07:03:59 by Xavier Morel

[IMP] *: owlify password meter and convert change password to real wizard

The changes in `auth_password_policy` are largely the owlification of
the password meter widget:

- modernize the password policy module and convert it to an
  odoo-module (note: now exports a pseudo-abstract class which is
  really a policy, for the sake of somewhat sensibly typing
  `recommendations`)
- replace the implementation of the Meter and PasswordField widgets by
  owl versions

The changes to web and base stem from taking a look at converting the
ChangePassword wizard, and finding that it would be a pain in the ass
but also... unnecessary? It seems to have been done as a wizard
completely in javascript despite being backend-only for legacy
reasons: apparently one of the very old web clients (v5 or v6
probably) implemented it as a "native action" which was directly part
of the client's UI, and so it had to be implemented entirely in the
client.

Over time it was moved back into the regular UI (and moved around
quite a bit), hooked as a client action to maintain access to the
existing UI / dialog.

But since it's been an action opened via a button for years it can
just... be a normal wizard, with password fields, which
auth_password_policy can then set the widget of.

So did that:

- removed the old unnecessary JS, and its dedicated endpoint (which is
  *not* used by portal, portal has its own endpoint)
- used check_identity for the "old password check"
- split out `change_password` with an internal bit so we can have a
  safer (and logged) "set user password" without needing to provide
  the old password, which is now used for the bulk password change
  wizard as well
- added a small wizard which just takes a new password (and
  confirmation), for safety a given change password wizard is only
  accessible to their creator (also the wizard is restricted to
  employees though technically it would probably be fine for portal
  users as well)

Rather than extensive messy rewrite / monkeypatching (the original
wizard was 57 LOC, though also 22 LOC of template, the auth_policy
hooking / patching was 33, plus 8 lines of CSS),
`auth_password_policy` just sets the widget of the `new_password`
field in the new wizard, much as it did the bulk wizard.

Also improve the "hide meter if field is empty" feature by leveraging
`:placeholder-shown`. This requires setting a placeholder, and while
empty works fine in firefox, it doesn't work in chrome. So the
placeholder needs to be a single space. Still, seems better than
updating a fake attribute or manipulating a class for the sake of
trivial styling.

Notes on unlink + transient vacuum

Although the wizard object is only created when actually calling
`change_password`, and is deleted on success, it is possible for the
user to get an error and fail to continue (it should be unlikely
without overrides since the passwords are checked while creating /
saving but...).

While in that case the `new_password` in the database is not the
user's own, it could be their *future* password, or give evidence as
to their password-creation scheme, or some other signal useful to
attack that front of the user's life and behavior. As such, quickly
removing leftovers from the database (by setting a very low transient
lifetime) seems like a good idea.

This is compounded by the `check_identity` having a grace period of 10
minutes. 0.1 is 6 minutes, but because the cron runs every 10 the user
effectively has 6~10 minutes between the moment they create an
incorrect / incomplete version of the wizard and the moment where it
is destroyed if they just leave it.

closes odoo/odoo#99458

Signed-off-by: Xavier Morel (xmo) <xmo@odoo.com>

---
## [SimenB/apollo-server](https://github.com/SimenB/apollo-server)@[793de3e230...](https://github.com/SimenB/apollo-server/commit/793de3e2308cc3ec98f14a67801c77a5e6640a7d)
#### Monday 2022-09-19 09:22:30 by Trevor Scheer

Add Jest imports everywhere, remove global availability (#6911)

In ESM mode, the `jest` globals are technically no longer available. For
some reason, we're still getting away with it, but this issue surfaces
in the v29 upgrade PR so I'm going to address it separately.

https://jestjs.io/docs/ecmascript-modules#differences-between-esm-and-commonjs

Ref:
https://github.com/apollographql/apollo-server/pull/6850#issuecomment-1247157466

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
## [replayio/devtools](https://github.com/replayio/devtools)@[9dc23c2b4d...](https://github.com/replayio/devtools/commit/9dc23c2b4dc82ac980e5d4d73eac9ea96ef30813)
#### Monday 2022-09-19 11:07:07 by Josh Morrow

Refine focus region based on received points

I'm not sure how this particular feature never got in. I remember
thinking last time I was working on focus stuff that we should do it,
but I guess I never actually got around to doing it. The idea is
relatively simple:

Sometimes the user asks for a focus region in which our known timeline
is sparse. We do our best to get them an accurate window, but it's tough
because points are few and far between. But there is *good* news there,
which is that we can't display anything incorrectly, because we don't
know about anything in the sparse ranges (that's why they are sparse).

But, then the trouble starts. The user has chosen a window, and they
start doing things like settings breakpoints. We are filling in our
sparse timeline! But sometimes those points actually fall *between* the
displayed end of the focus region and real end of the window for which
we are currently making requests. When this happens, you get
funny-looking results, like analysis points hanging out in regions that
look unloaded. The solution is actually relatively simple. When we are
focused and we discover new points, we check to see if any of those
points could be used to make a more refined focus window. If so, we just
update our focus window. No additional interactions with the backend are
required, and if we have a really dense analysis, that's fine, because
it just means we will get even *more* accurate information about the
point <-> time relationship in that region.

---
## [doringeman/linuxkit](https://github.com/doringeman/linuxkit)@[860934d5d9...](https://github.com/doringeman/linuxkit/commit/860934d5d98f0024ebc86896715863526f8fe96c)
#### Monday 2022-09-19 12:49:03 by Davide Brini

New output format: iso-efi-initrd

This option was previously not available and required postprocessing of a `tar-kernel-initrd` output.

Comparison with `iso-efi`:

`iso-efi` only loads the kernel at boot, and the root filesystem is mounted from the actual boot media (eg, a CD-ROM - physical or emulated). This can often cause trouble (it has for us) for multiple reasons:
- the linuxkit kernel might not have the correct drivers built-in for the hardware (see #3154)
- especially with virtual or emulated CD-ROMs, performance can be abysmal: we saw the case where the server IPMI allowed using a ISO stored in AWS S3 over HTTP...you can imagine what happens when you start doing random I/O on the root fs in that case.
- The ISO image has the root device name baked in (ie, `/dev/sr0`) which fails if for some reason the CD-ROM we're running from doesn't end up using that device, so manual tweaking is required (see #2375)

`iso-efi-initrd`, on the other hand, packs the root filesystem as an initramfs (ie similar to what the raw output does, except that in this case we're preparing an ISO image), so both the kernel and the initramfs are loaded in memory by the boot loader and, once running, we don't need to worry about root devices or kernel drivers (and the speed is good, as everything runs in RAM).

Also, the generated ISO can be copied verbatim (eg with `dd`) onto a USB media and it still works.

Finally, the image size is much smaller compared to `iso-efi`.

IMHO, `iso-efi-initrd` could be used almost anywhere `iso-efi` would be used, or might even supersede it. I can't think of a scenario where one might explicitly want to use `iso-efi`.

Points to consider:

- Not tested under aarch64 as I don't have access to that arch. If the automated CI tests also test that, then it should be fine.
- I'm not sure what to put inside `images.yaml` for the `iso-efi-initrd` image. As it is it works of course (my personal image on docker hub), but I guess it'll have to be some more "official" image. However, that cannot be until this PR is merged, so it's kind of a chicken and egg situation. Please advise.
- I can look into adding the corresponding `iso-bios-initrd` builder if there is interest.

![cute seal](https://sites.psu.edu/siowfa16/files/2016/09/baby-seal-29vsgyf-288x300.jpg)

Signed-off-by: Davide Brini <waldner@katamail.com>

---
## [RipGrayson/TerraGov-Marine-Corps](https://github.com/RipGrayson/TerraGov-Marine-Corps)@[a96d4df973...](https://github.com/RipGrayson/TerraGov-Marine-Corps/commit/a96d4df9736c68bf6534de6124698fabbd9e9c97)
#### Monday 2022-09-19 14:20:30 by 567Turtle

item storage tweaks (#10913)

* whistle thing

i hate this fucking game

* grammar

who knew defibrillator was spelled with two Ls

* defib go bye bye

bye bye

* few other things

Makes it so you can put a sodering tool in your belt and your vest, robots need healing to

* injector boots

If you can put a whole ass MRE in your boot you can put a little ass pen in there

* reverts changelog changes

nuff said

* fixes things

adds trail commas where I forgot them, removes medipens going in shoes

* jaeger module soldering tool

you can put a soldering tool into the medical jaeger storage module :)

* reverts typo fix

nuff said

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[06090b9269...](https://github.com/cockroachdb/cockroach/commit/06090b92696bfc4c84f457ac204c4bf17f780170)
#### Monday 2022-09-19 15:34:29 by craig[bot]

Merge #86603 #87166 #87535 #87870 #88078 #88111

86603: changefeedccl: redact user from confluent schema registry r=jayshrivastava a=jayshrivastava

This change redacts the confluent schema registry key
from the jobs table.

Fixes: https://github.com/cockroachdb/cockroach/issues/85902

Release justification: This change is important because
it prevents a user's secret key from being store in the DB.
The footprint of this change is small as it only touches
a specific changefeed option - confluent schema registry.

Release note (enterprise change): Previously, SHOW CHANGEFEED
JOBS would reveal confluent schema registry user information,
including a user's secret key. This change makes this info
redacted, meaning it will not be stored in CockroachDB
internal tables at all.

87166: kvserver: shorten `raft.process.handleready.latency` help text r=tbg a=erikgrinaker

We should get confirmation in #87112 that this size is below the limit before merging this.

---

AWS managed Prometheus rejects `raft.process.handleready.latency`
because the help text is too long. The text is currently 1123 bytes, so
the limit is suspected to be 1024 bytes. This patch reduces the size of
this help text to 938 bytes.

Resolves #87112.

Release justification: bug fixes and low-risk updates to new functionality

Release note (ops change): Reduced the length of the
`raft.process.handleready.latency` metric help text to avoid it being
rejected by certain Prometheus services.

87535: sql: support `#typeHints` greater than `#placeholders` for prepare stmt r=rafiss a=ZhouXing19

Previous, we only support pgwire prepare stmt with the number of typehints equal or smaller than the number of the placeholders in the query. E.g. the following usage are not supported:

```
Parse {"Name": "s2", "Query": "select $1", "ParameterOIDs":[1043, 1043, 1043]}
```
Where there is 1 placeholder in the query, but 3 type hints.

This commit is to allow mismatching #typeHints and #placeholders. The former can be larger than the latter now.

This feature is needed for [CRDB's support for Hasura GraphQL Engine](https://github.com/hasura/graphql-engine/issues/8839#issuecomment-1236691642).

Release justification: Low risk, high benefit changes to existing functionality

Release note: For pgwire-level prepare statements, add support for the case where the number of the type hints is greater than the number of placeholders in the given query.

87870: kvnemesis: reset op.Result r=erikgrinaker a=tbg

We found out (in #87814) after a wild goose chase that op.Result was not
reset, so unless operations were cognizant of this fact and
always fully repopulated the Result field, weird failures
could result from txn retries.

Reset the field.

Release note: None


88078: ui: update filter labels r=maryliag a=maryliag

Update filter label from "App" to "Application Name" and "Username" to "User Name" on SQL Activity and Insights pages.

Fixes #87960

<img width="467" alt="Screen Shot 2022-09-16 at 6 40 51 PM" src="https://user-images.githubusercontent.com/1017486/190827281-36a9c6df-3e16-4689-bcae-6649b1c2ff86.png">


Release note (ui change): Update filter labels from "App" to "Application Name" and from "Username" to "User Name" on SQL Activity and Insights pages.

88111: sql: fix `pg_get_viewdef` for materialized views r=rafiss a=knz

Fixes #88109.

Release note (bug fix): The function `pg_catalog.pg_get_viewdef` now works properly for materialized views.

Co-authored-by: Jayant Shrivastava <jayants@cockroachlabs.com>
Co-authored-by: Erik Grinaker <grinaker@cockroachlabs.com>
Co-authored-by: Jane Xing <zhouxing@uchicago.edu>
Co-authored-by: Tobias Grieger <tobias.b.grieger@gmail.com>
Co-authored-by: Marylia Gutierrez <marylia@cockroachlabs.com>
Co-authored-by: Raphael 'kena' Poss <knz@thaumogen.net>

---
## [MASQ-Project/Node](https://github.com/MASQ-Project/Node)@[b0e9bb484e...](https://github.com/MASQ-Project/Node/commit/b0e9bb484effc32ed164eb4bef51b624c3d7982a)
#### Monday 2022-09-19 16:08:33 by dnwiebe

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
## [oxidecomputer/omicron](https://github.com/oxidecomputer/omicron)@[53c732aa97...](https://github.com/oxidecomputer/omicron/commit/53c732aa97f79e2ba494131660390de951227b40)
#### Monday 2022-09-19 18:08:25 by Andrew J. Stone

Bootstore message handler implementation (#1687)

This is the second PR of the `bootstore` implementation. It creates handler
methods for all existing messages and their corresponding DB requirements. RFD
238 section 5 will need to be updated to reflect this flow.

The way the flow currently is supposed to work is that there is a coordinator
(coming in a follow up PR) that sends the following messages to initialize the
trust quorum:
 * `Initialize`
 * `KeyShareCommit` (for epoch 0)

`Initialize` can be sent multiple times until the `KeyShareCommit` for epoch 0
locks in the configuration and Rack UUID. This allows the initial coordinator
(RSS) to die, and even have its local storage or entire sled die, and still
allow us to make progress via a new RSS. Importantly, once wired through the
system, the coordinator will negotiate (via sled-agent and nexus) to write the
`KeyShareCommit` to CockroachDB before sending it to all nodes. This ensures
that the rack initialization will complete and CockroachDB only has to be setup
once. There are some tricky failure modes here, but none of that is in this PR,
so we can move on. The important point here is that once a `KeyShareCommit` for
epoch 0 succeeds the rack is initialized.

After initialization, reconfiguration of the trust quorum can take
place. Reconfiguration messages must be issued with the same Rack UUID. A
reconfiguration consists of a `KeySharePrepare` for an `epoch > 0` followed by
a `KeyShareCommit` for the same epoch. After initialization a `KeySharePrepare`
can never be mutated. However, to allow for certain failures, such as
the failure of a node being prepared to ack (since we require unanimous
acknowledgement in 2PC), we allow for new `KeySharePrepare`s at higher
epochs to proceed. We keep track of these epochs in CockroachDB to maintain
linearizability. Once a node receives a prepare for a higher epoch, it will no
longer accept prepare or commit messages for any lower epoch. Once a successful
`KeyShareCommit` is handled, the sled is now operating at the new epoch.

`GetShare` requests are used to unlock trust quorum. They will rely on
sprockets at the network level for authentication, confidentiality, integrity,
and attestation. Some DeviceId membership validation will also be added to
`Node`in future commits as it currently exists in sled agent.

This is an incremental PR and there is still a lot to do here. Follow up
commits will:
 * Add more negative tests (possibly in this PR also)
 * Add code for a coordinator
 * Add a mechanism to store the encrypted (wrapped) root secret for each
   epoch and likely include it in each `KeySharePrepare`. This is the most
   straightforward way to transfer wrapped secrets. We can get more
   sophisticated in the future. Again, this needs to be written up in RFD 238,
   but I'm likely to just implement it within the next week and see how it works
   first.
 * Add some key derivation from the root secret such that we can use these keys
   to encrypt and decrypt storage
 * Add property based tests to simulate a full cluster along with failures and
   ensure rack unlock works according to the model and ensure that we can
   *always* unlock encrypted storage while tolerating our prescribed failure
   conditions within the model.

After that, the `bootstore` will basically be implemented at a non-network
level. We'll then likely want to port over the sprockets code from the
bootstrap agent to a higher level here, and use the `Node` and `Coordinator`
from that level, which will end up interacting with Nexus and CockroachDB
via the sled-agent. Multiple tasks will be utilizing the `Node` and its
underlying `Db` at this point and so we'll need some concurrency control.
I've given this a bit of thought and my current thinking is to have the `Node`
running in it's own thread and serialize all operation via a channel. Outside
of reconfiguration, all operations are reads, and we can simply cache the
current share in memory for rack unlock purposes (e.g. `GetShare`). During
reconfiguration, we'll mutate the DB as necessary, and refresh our cache. This
strategy avoids the need for mutexes and has the characteristic that the `Node`
and `Db` code we run in a single threaded manner in property based tests is
actually running the same way in production with just a single DB connection.
This strategy isn't set in stone, but in my mind it's the easiest to reason
about and also the easiest way to hook async to sync code.

---
## [wfleming/advent-of-code](https://github.com/wfleming/advent-of-code)@[a2c809415f...](https://github.com/wfleming/advent-of-code/commit/a2c809415fd908fd6ba708087ca7b18a191b4fb6)
#### Monday 2022-09-19 18:15:16 by Will Fleming

2019 d18

On par with 2018 d23 (octrees) for just totally messing with my brain.
At first glance it seems like a pretty straightforward path-finding
problem you could throw A*, but the size of the search space (26!
That's a factorial, I'm not excited.) combined with the lack of a clear
f score ("distance to goal") heuristic makes it very tricky.

I iterated through several approaches here (still visible on the
day-specific branch), slowly getting at something that was fast enough.
One of the first things I realized was the top-level search shouldn't be
moving one square at a time, but between keys, with key -> key paths a
sub-problem to solve separately.

I had an iteration that did that naively and poorly a while ago. After
my recent experience with 2021 d23, an obvious increment was to use
djikstra to pre-calculate all the optimal paths from point -> point as
part of the maze itself, and then just check against those paths when
finding neighboring states. That key insight, combined with some other
improvements to the search impl (basically a modified djikstra at this
point) and trying to optimize a few of the low-level bits of logic got
this into a pretty good spot.

p1 ran in about 900ms. The easiest way to do p2 was to generalize the
existing code to handle multiple current positions. This did make p1 on
its own slightly slower (1.1s), but it's not too bad. p1 & p2 together
are about 7s. Not amazing, but I'll take it, and I suspect considerably
speeding it up would require making it less readable.

---
## [dMajoIT/terminal](https://github.com/dMajoIT/terminal)@[9ccd6ecd74...](https://github.com/dMajoIT/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Monday 2022-09-19 19:38:53 by Mike Griese

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
## [polarity/bitwig-community-presets](https://github.com/polarity/bitwig-community-presets)@[c2a991002e...](https://github.com/polarity/bitwig-community-presets/commit/c2a991002e7a59646677579276cc27374411a91a)
#### Monday 2022-09-19 20:17:15 by Chefkoch

I’ve made something weird today.

A few days ago I rewatched <@118550747137835008>’s tutorial called “Generative Pattern Combining in the Bitwig Studio Grid”, which I had seen before but for some reason forgot about. Maybe I watched it too early in my Bitwig journey to understand the potential. But this time it was a huge, I mean huge bout of inspiration. For the last few days I've been doing things with generative melodies that evolve and then return to their original state, which I didn’t think was possible, because I understood that the S/H device can sample values, but I didn’t quite realize that it could hold on to them too.

And today I've made something weird. Instead of starting with a melody and letting it go in random directions, I wondered whether the opposite was possible. Can I start with two different melodies of the same length, and by changing their notes at random make them eventually converge into a single melody? Turns out, yes I could!

So here’s the Note Grid preset and a very basic project. If you try it out, send it to a pluck-type instrument, it expects to play quick, distinct notes. Notes change at random once per bar, so the time it takes for both melodies to converge depends on the tempo you set, which for me, at 130 bpm, takes under two minutes. Every bar the melody will be slightly different than previously (well, not *every* bar really, since sometimes randomness will replace a note with itself), and gradually the two distinct melodies will coalesce into one.

Oh, and the blue lights indicate which notes are already ”synced”, so you can see the progress.

Musical? Perhaps not 😊 Useful? Perhaps not, either. But pleasantly weird, and I love the grid for being able to accommodate such odd designs.

---
## [wking/cluster-version-operator](https://github.com/wking/cluster-version-operator)@[9222fa9a66...](https://github.com/wking/cluster-version-operator/commit/9222fa9a6616b58a8056c780b9a6252e82a26e37)
#### Monday 2022-09-19 20:28:26 by W. Trevor King

pkg/cvo/sync_worker: Trigger new sync round on ClusterOperator versions[name=operator] changes

David and Stephen identified an uneccessary delay [1]:

* 9:42:00, CVO gives up on Kube API server ClusterOperator [2]
* 9:42:47, Kube API server operator achieves 4.12 [3]
* 9:46:22, after a cool-off sleep, the CVO starts in on a new manifest graph-walk attempt [4]
* 9:46:34, CVO notices that the Kube API server ClusterOperator is happy [5]

The 3+ minute delay from 9:42:47 to 9:46:22 is not helpful, and we've
probably had delays like this since my old e02d1489a5
(pkg/cvo/internal/operatorstatus: Replace wait-for with single-shot
"is it alive now?", 2021-05-13, #560), which landed in 4.6.

This commit introduces a "ClusterOperator bumped
versions[name=operator]" trigger to break out of the cool-off sleep.

There's plenty of room to be more precise here.  For example, you
could currently have a versions[name=operator] bump during the sync
loop that the CVO did notice, and that queued notification will break
from the sleep and trigger a possible useless reconciliation round
while we wait on some other resource.  You could drain the
notification queue before the sleep to avoid that, but you wouldn't
want to drain new-work notifications, and I haven't done the work
required to be able to split those apart.

I'm only looking at ClusterOperator at the moment, because of the many
types the CVO manages, ClusterOperator is the one we most frequently
wait on, as large cluster components take their time updating.  It's
possible but less likely that we'd want similar triggers for
additional types in the future (Deployment, etc.), if/when those types
develop more elaborate "is the in-cluster resource sufficient happy?"
checks.

The panic-backed type casting in clusterOperatorInterfaceVersionOrDie
also feel like a hack, but I wasn't able to find a cleaner way to get
at the structured information I want.  Improvements welcome :)

[1]: https://bugzilla.redhat.com/show_bug.cgi?id=2117033#c1
[2]: From Loki: E0808 09:42:00.022500       1 task.go:117] error running apply for clusteroperator "kube-apiserver" (107 of 806): Cluster operator kube-apiserver is updating versions
[3]: $ curl -s https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/origin-ci-test/logs/periodic-ci-openshift-release-master-ci-4.12-upgrade-from-stable-4.11-e2e-gcp-sdn-upgrade/1556564581915037696/artifacts/e2e-gcp-sdn-upgrade/openshift-e2e-test/build-log.txt | grep 'clusteroperator/kube-apiserver versions:'
     Aug 08 09:33:48.603 I clusteroperator/kube-apiserver versions: raw-internal 4.11.0-rc.7 -> 4.12.0-0.ci-2022-08-07-192220
     Aug 08 09:42:47.917 I clusteroperator/kube-apiserver versions: operator 4.11.0-rc.7 -> 4.12.0-0.ci-2022-08-07-192220
[4]: From Loki: I0808 09:46:22.998344       1 sync_worker.go:850] apply: 4.12.0-0.ci-2022-08-07-192220 on generation 3 in state Updating at attempt 5
[5]: From Loki: I0808 09:46:34.556374       1 sync_worker.go:973] Done syncing for clusteroperator "kube-apiserver" (107 of 806)

---
## [emallson/WoWAnalyzer](https://github.com/emallson/WoWAnalyzer)@[90c1dd8db4...](https://github.com/emallson/WoWAnalyzer/commit/90c1dd8db4b04d465daf45332ec73a28130651d1)
#### Monday 2022-09-19 21:13:09 by Richard Harrah

second pass on demon hunter

clean out changelog entries referencing
abilities that are removed in DF

add sigils to HDH abilities list

clean out entries in SPELLS/demonhunter that are
present in TALENTS/demonhunter

add support for Charred Warblades

add getTalentRank function for Combatant

correct locations of multiple analyzers in the
statistics tab

add support for Misery in Defeat class talent

add support for Retaliation talent

add Buffs module for Vengeance to make frailty
support easier, given that it can now be applied by
three different abilities.

add support for Painbringer talent

add Blur and Darkness to Vengeance

add support for Tactical Retreat talent

add support for Initiative talent

update support for Cycle of Hatred talent

correct Know Your Enemy scaling

regenerate DH talents

---
## [obamasolutions/obama.solutions](https://github.com/obamasolutions/obama.solutions)@[1076b1758f...](https://github.com/obamasolutions/obama.solutions/commit/1076b1758f99165ff85bc4739aca411b9ffe885b)
#### Monday 2022-09-19 22:00:21 by Nicole Aoki

Update a fuck ton of things, read description.

First, replaced the nikoki icon with Pizza Steve (well, Pineapple Steve) for the meantime, make all my pages in Markdown so once we get the SSG setup working it isn't that much of a hassle to update, updated GPG key to reflect the recent User IDs that I've added; might revoke key at some point, rewrote my about page to be more "about me" if you can call it that, updated template and... yeah I think that's about it.

---
## [ruf-io/materialize](https://github.com/ruf-io/materialize)@[305082a6a9...](https://github.com/ruf-io/materialize/commit/305082a6a99ee063839975c86bd1e821a2af0e23)
#### Monday 2022-09-19 22:40:33 by Daniel Harrison

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
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[5acf72cc1f...](https://github.com/Buildstarted/linksfordevs/commit/5acf72cc1fa8f68b39ed54e3b86ba81e9e381bea)
#### Monday 2022-09-19 23:07:41 by Ben Dornis

Updating: 9/19/2022 11:00:00 PM

 1. Added: How I manage my passwords
    (https://bitspook.in/blog/how-i-manage-my-passwords/)
 2. Added: Implementing a Terraform state backend on Cloudflare Workers
    (https://mirio.dev/2022/09/18/implementing-a-terraform-state-backend/)
 3. Added: Building a Sequencer and a Level Editor for Vectron
    (http://nicktasios.nl/posts/building-a-sequencer-and-a-lever-editor-for-vectron.html)
 4. Added: An extremely opinionated guide on making friends for people who are exactly like me
    (https://blog.aadilali.com/posts/friends.html)
 5. Added: Content based change detection with Make
    (https://andydote.co.uk/2022/09/19/make-content-hash/)
 6. Added: A few thoughts about Uber&#39;s breach
    (https://cendyne.dev/posts/2022-09-19-a-few-thoughts-about-ubers-breach.html)
 7. Added: Emoji language is the most compact
    (http://joaomacp.github.io/2022/09/17/emoji-language-is-the-most-compact.html)
 8. Added: Rachit Nigam | PhD Candidate, Cornell University
    (https://rachitnigam.com/post/why-study-programming-languages/)
 9. Added: How you can help the Linux Mobile ecosystem
    (https://connolly.tech/posts/2022_09_16-how-to-help-linux-mobile/)
10. Added: Why I don’t enjoy RSpec all that much
    (https://nts.strzibny.name/why-not-rspec/)
11. Added: Loss, Grief, Sadness · Jerry Liu
    (https://www.personjerry.com/posts/loss-grief-sadness/)
12. Added: Fast, Branchless Ray/Bounding Box Intersections, Part 3: Boundaries
    (https://tavianator.com/2022/ray_box_boundary.html)
13. Added: What happens when you amend a commit?
    (https://hanki.dev/git-amend-under-the-hood/)
14. Added: Hybrid Web Frameworks Q&A with Allen Conway: Reach Android/iOS with JavaScript, HTML and CSS -- Visual Studio Magazine
    (https://visualstudiomagazine.com/articles/2022/09/19/hybrid-web-frameworks.aspx)
15. Added: How To Implement Test Automation For Your Embedded Product? » Test Automation
    (https://pallavaggarwal.in/2022/09/17/embedded-hardware-test-automation/)
16. Added: Game Theory and Winning at ponziFarm
    (https://blog.ponzifarm.com/blog/game-theory/)
17. Added: The Case for reducing your digital clutter. | Kole McRae
    (https://kolemcrae.com/notebook/digitalclutter.html)
18. Added: How to build a Twitter and Instagram bot with no code
    (https://johnson.fm/blogs/how-to-build-a-twitter-and-instagram-bot-with-no-code)
19. Added: 10 Good Daily Habits That Will Make Your Life Suck Less
    (https://durmonski.com/self-improvement/good-daily-habits/)

Generation took: 00:07:30.7781298
 Maintenance update - cleaning up homepage and feed

---

