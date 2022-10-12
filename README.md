## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-11](docs/good-messages/2022/2022-10-11.md)


2,183,574 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,183,574 were push events containing 3,323,715 commit messages that amount to 269,956,249 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[1af2c12e05...](https://github.com/TaleStation/TaleStation/commit/1af2c12e0501c2cf5eb5946738360564fd78cea4)
#### Tuesday 2022-10-11 00:04:26 by TaleStationBot

[MIRROR] [MDB IGNORE] canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#2676)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

* fix

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [Firehawke/mame](https://github.com/Firehawke/mame)@[ece818f613...](https://github.com/Firehawke/mame/commit/ece818f61396b3048318fceed190e4bcb2cae323)
#### Tuesday 2022-10-11 00:09:41 by Firehawke

Mac: Add first MOOF original disk sets and start splitting software lists.

New working software list additions (mac_flop_orig.xml)
-------------------------------------------------------

Lode Runner (Version 1.0) [4am, Firehawke]
Balance of Power (Version 1.03) [4am, Firehawke]
Shanghai (Version 1.0) [4am, Firehawke]
Skyfox [4am, Firehawke]
Temple of Apshai Trilogy (Version 1985-09-30) [4am, Firehawke]
The Surgeon (Version 1.5) [4am, Firehawke]
Uninvited [4am, Firehawke]
King's Quest (Version 1.10) [4am, Firehawke]
Smash Hit Racquetball (Version 1.01) [4am, Firehawke]
The Ancient Art of War [4am, Firehawke]
Hacker II [4am, Firehawke]
Indiana Jones and the Revenge of the Ancients [4am, Firehawke]
Rambo: First Blood Part II [4am, Firehawke]
One on One [4am, Firehawke]
Winter Games (Version 1985-10-24) [4am, Firehawke]
Winter Games (Version 1985-10-31) [4am, Firehawke]
Star Trek: The Kobayashi Alternative (Version 1.0) [4am, Firehawke]
Mac Attack [4am, Firehawke]
GATO (Version 1.3) [4am, Firehawke]
Dark Castle (Version 1.0) [4am, Firehawke]
Oids (Version 1.4) [4am, Firehawke]
MacWars [4am, Firehawke]
Shadowgate [4am, Firehawke]
Seven Cities of Gold [4am, Firehawke]
Enchanted Scepters [4am, Firehawke]
Beyond Dark Castle [4am, Firehawke]
Arkanoid (Version 1.00) [4am, Firehawke]
The Chessmaster 2000 (Version 1.02) [4am, Firehawke]

---
## [sjp38/linux](https://github.com/sjp38/linux)@[7f6ff5468b...](https://github.com/sjp38/linux/commit/7f6ff5468b495c720b90c515dd9802a6de1b62dd)
#### Tuesday 2022-10-11 00:40:32 by Johannes Weiner

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
## [mrsilver256/react](https://github.com/mrsilver256/react)@[b6978bc38f...](https://github.com/mrsilver256/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Tuesday 2022-10-11 00:52:24 by Andrew Clark

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
## [Koshenko/mojave-sun-13](https://github.com/Koshenko/mojave-sun-13)@[736422fac8...](https://github.com/Koshenko/mojave-sun-13/commit/736422fac8d84c8e054853fd2b205cc993250c21)
#### Tuesday 2022-10-11 01:11:57 by Technobug14

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
## [SomethingFish/tgstation](https://github.com/SomethingFish/tgstation)@[14c96d05b8...](https://github.com/SomethingFish/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Tuesday 2022-10-11 01:41:00 by scriptis

TGUI for Techfabs II: The Great Recategorizing (AND ICONS) (AND MECHFABS) (AND AUTOLATHES) (#69990)

    I recategorized EVERY /datum/design/ IN THE GAME to be more UX friendly and I HATE MYSELF FOR IT
    I refactored techfab UI to WORK ANYWHERE for ANY MACHINE THAT USES /datum/design as a SET OF MODULAR COMPONENTS
    I moved a lot of DESIGNS EXCLUSIVE TO THE AUTOLATHE to also work IN PROTOLATHES
    I made MATERIAL ICONS animate between ICON STATES for STACKS
    I PUT ICONS IN ALL OF YOUR FABRICATORS
    I SOMEHOW DID ALL OF THIS WITHOUT LOSING ANY PERFORMANCE
    ALSO SUPPORTS COMPONENT PRINTERS AND MODULE DUPLICATORS

Other garbage:

    Fixed numerous spelling and consistency issues in designs
    Removed Machine Design (<x>) and Computer Design (<x>) from all relevant designs
    All designs are now in title case
    Numerous designs that were formerly autolathe exclusives can now also be printed at a protolathe (but not all); this is mostly just service equipment like drinking glasses and plates and silverware
    Circuits components can no longer be printed at a circuit imprinter (fixes 

    Integrated circuit components printed in the component printer/module printer cost twice as much than from an un upgraded circuit printer #67758)
    Designs that are not sensible for a department to have are no longer accessible to that department (read: medbay printing turbine parts)

Why It's Good For The Game

Improved UX for techfabs, but also for mechfabs and autolathes, and oh look it's pretty!

also I spent like eight hours doing nothing but categorizing /datum/designs and I'll cry if some version of this doesn't get merged eventually
Changelog

cl
refactor: mechfabs, autolathes, component printers, and module duplicators now use techfab tgui components
refactor: every single design is now categorized and subcategorized
refactor: mechfabs and autolathes are now in typescript
qol: techfabs now have icons for what you're about to print
qol: techfab material icons are now animated
qol: techfab material icons now fade when no materials are available
qol: techfab searching no longer lags like hell
qol: techfab searching now searches all recipes instead of just the current category
qol: techfabs now have subcategorization (stock part users rejoice)
qol: techfabs now announce when new recipes are available
qol: numerous other techfab ui tweaks
balance: some designs that were formerly autolathe exclusive can now be printed at some departmental techfabs

---
## [SomethingFish/tgstation](https://github.com/SomethingFish/tgstation)@[99b8d6b494...](https://github.com/SomethingFish/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Tuesday 2022-10-11 01:41:00 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---
## [mydubsetstory180/Halofactorx](https://github.com/mydubsetstory180/Halofactorx)@[e2ebf1afd5...](https://github.com/mydubsetstory180/Halofactorx/commit/e2ebf1afd53cefb0a293b4524aaa72a8d74aeb1c)
#### Tuesday 2022-10-11 01:49:37 by Dr.Warith Akbar

Update issue templates

Hello I have hackers trying to crash my company and shareholders. There on my company VM blocking me from my stock option as well changing my company names and drop shipping thro other companies for the last 5 years . Every time I dry to develop a project they blog my domain access as well place my GPS to another country. As of this point they have hurt my peace talks with Russia and China as well hacked into my cancer research platform on Microsoft and AWS and deleted me out of being founder of this platform and 100s of other project . It looks like they partnered up.with my rivals Trump to stop me from reporting . And block my development project to hurt Election process . As well since I'm a lobbyists for the President Joe Biden Admin they are Purposely Sabotage by platforms  . As of know they been drop shipping billions of packages off my business account . And hijacked my blogs . They are also responsible for Jeff bezos losing his Position for calling him a platform he didn't know they stole from me . Its appropriate they believe playing with people life a game and they need to be blocked from ever being apart of anything that has to do with development or internet. 

As well I'm investigating the Sep 11 attack . I believe located who responsible . And it look closer to home then the world would ever know .

Warith Akbar 
9400 Rainer ave s Seattle WA 98118 
Apt 120 

I need for Amazon to get a hold of president Joe Biden admin and tell him I said the threat is real hacker has been developing Samsung ,and Apple devices changing the build and deleting the proxy out of millions of devices so they can be easier to access you dev option and claim you devices. As well they are using gov DUN accounts to claim my assets in holding illegally.. 

Reason to believes the rapture stealth fighter may need to change codes as well as all new development any GOV project need to start over from AI point and we have to develop the VM and cloud computing . as well anything github or Marvin tose because they are using those platforms to transfer assists via impact & export etc. I also have to security data of Amazon and the stste department that might help out . 

As well reason to believes Bank manager are also involved in blocking federal assets from properly developing

---
## [AzuleUtama/Paradise](https://github.com/AzuleUtama/Paradise)@[ab7a358506...](https://github.com/AzuleUtama/Paradise/commit/ab7a35850672da159eea98085cf6fade7d595340)
#### Tuesday 2022-10-11 01:50:15 by Farie82

Makes setting a machine GC properly if not unset properly (#17840)

* Makes setting a machine GC properly if not unset properly

* Forgot one. Fuck you borer code

---
## [ExplodingImplosion/GodotAddonPack](https://github.com/ExplodingImplosion/GodotAddonPack)@[6b8e523c64...](https://github.com/ExplodingImplosion/GodotAddonPack/commit/6b8e523c646dc56b46a247ee0a0ea89808bcd994)
#### Tuesday 2022-10-11 03:06:38 by ExplodingImplosion

read desc for godot notes

update gitignore for replay stuff

resources script loading fixed

quack has redefer func

network update control snapshot finishing uses redefer

notes about godot in general:
if you move one area into another area, whichever area is LOWER in the scenetree emits the signal first because FUCK you thats why

---
## [biscuitel/cat-cafe](https://github.com/biscuitel/cat-cafe)@[da2ad08af7...](https://github.com/biscuitel/cat-cafe/commit/da2ad08af7c0eeb7f173b62a668feb3011805de4)
#### Tuesday 2022-10-11 03:41:17 by xavibell

Task List on taskboard changes per task now (plus more!)

I've kinda changed the purpose the taskboard to make more sense. Basically, the reason you keep going back to the taskboard is so that you can tick off the task you just did alongside seeing the next task. The reason Bob keeps doing this is because he's paranoid about the boss watching him (which is true, there's security cameras in every room). I also did some lightmap rubbish. There's one wall in the staffroom that's causing me a bit of grief, mainly due to the fact that it just has a bunch of weird artifacts on it for no reason. Besides that one issue, the lighting is basically done. I've tried matching the lighting in the ending room a little better so the transition isn't as obvious, and it's improved somewhat, but I still need to tweak that. Lastly, I changed some of the task descriptions to show Bob becoming a tad weirder on day 2. Let me know if anything has broken, I didn't do a complete playthrough to check.

---
## [Libera-Chat/solanum](https://github.com/Libera-Chat/solanum)@[06c5309534...](https://github.com/Libera-Chat/solanum/commit/06c53095343c2756208f6398bb7e00fb2cbe46dd)
#### Tuesday 2022-10-11 04:15:10 by Ed Kellett

m_sasl: Remove implicit abort on registration

This doesn't make sense in a world where post-registration SASL is
allowed, and should fix one case of an annoying login desync that's seen
in the real world.

Specifically, when a client sends its final AUTHENTICATE and Atheme
receives it, it sends an SVSLOGIN for that client. If the client sends
us its CAP END *before* we see the SVSLOGIN, the implicit abort will try
to abort the SASL session that's already succeeded.

Atheme interprets this as an instruction to forget about the successful
SASL session; you'll connect unidentified. But it's already sent
SVSLOGIN, which will log the client in ircd-side, causing ircd and
services views to differ until the user authenticates again manually.

I think allowing a SASL session to be aborted when it has already
succeeded is an Atheme bug, and it can still be triggered without this
change. But our behaviour here seems silly anyway.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[fc7c186957...](https://github.com/timothymtorres/tgstation/commit/fc7c186957088b6ffd0605f814bea754670c0212)
#### Tuesday 2022-10-11 05:02:51 by RikuTheKiller

Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

---
## [pri0818/falcon_kernel_realme_sm7125](https://github.com/pri0818/falcon_kernel_realme_sm7125)@[f63712b993...](https://github.com/pri0818/falcon_kernel_realme_sm7125/commit/f63712b9937eae42c0f57c519f69f633be5559ad)
#### Tuesday 2022-10-11 07:17:11 by Peter Zijlstra

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
Signed-off-by: pri0818 <priyanshusinghal0818@gmail.com>

---
## [BuKast99/Real-ESRGAN](https://github.com/BuKast99/Real-ESRGAN)@[10d7260dc6...](https://github.com/BuKast99/Real-ESRGAN/commit/10d7260dc6dea0a2633de2451a76a114cf513b8d)
#### Tuesday 2022-10-11 07:27:54 by BuKast99

Delete lr_image.png

african american woman, blonde short hair, brown eyes, beautiful girl, sexy lips, close up portrait, moonlight, highkey, realistic, serov, surikov, vasnetsov, repin, kramskoi, paint texture, low aperature, insanely detailed, charlie bowater, tom bagshaw, octane rendered, unreal engine, illustration, trending on artstation, masterpiece

---
## [mezzio/mezzio](https://github.com/mezzio/mezzio)@[cb239a9a81...](https://github.com/mezzio/mezzio/commit/cb239a9a81c00394beee622f62261cd1980df847)
#### Tuesday 2022-10-11 08:12:42 by Michał Bundyra

Message against the war, in Russian and English

> ## 🇷🇺 Русским гражданам
>
> Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.
>
> У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.
>
> Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"
>
> ## 🇺🇸 To Citizens of Russia
>
> We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.
>
> One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.
>
> You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [DoumbiaAmadou/rx-player](https://github.com/DoumbiaAmadou/rx-player)@[7fbe7ef5eb...](https://github.com/DoumbiaAmadou/rx-player/commit/7fbe7ef5eb409e59f60584bde2a4ab31a461440b)
#### Tuesday 2022-10-11 08:16:26 by Paul Berberian

Add magic Jest config property to Make Unit Tests Work Again (MUTWA)

It seems that Jest 28+, for some obscure reasons, now fail importing
dependencies using a ESM-style importing/exporting syntax - despite it
working before. It wasn't in their migration guide nor in their
changelog, so it was difficult to find how to work-around that issue.

In the end, I did what any developer who want to get things done should
do and just browsed the web to test every options under the sun that
could fix the issue.
Turns out the one in this commit has a good effect, though god knows
what it's actually doing!

Thanks https://www.sobyte.net/post/2022-06/jest/ to give me this hint,
and for apparently understanding what you're doing.

I am personally decidedly 2dumb4jest, which slowly leads me to dislike
this library very much for consequentially purely ego reasons.

---
## [abd20ac/NuclearPotatus.github.io](https://github.com/abd20ac/NuclearPotatus.github.io)@[d1b259d5c3...](https://github.com/abd20ac/NuclearPotatus.github.io/commit/d1b259d5c3e5fdd6c41202d7fd409756d2f88910)
#### Tuesday 2022-10-11 08:42:12 by abd20ac

LUD I SWEAR TO GOD IF YOU DON'T ACCEPT MY CHANGES THERE WILL BE CONSEQUENCES!

I improved the game. Now we can all see that you suck at coding and that you messed up a line but I won't tell u where. Even my grandma could make a better game than this with her eyes closed while on a bicycle. Your code sucks and I improved it so you better accept my changes you prick.

---
## [Galaxy-J5-Unofficial-LineageOS-Sources/samsung_kernel_msm8916](https://github.com/Galaxy-J5-Unofficial-LineageOS-Sources/samsung_kernel_msm8916)@[c80ec914c9...](https://github.com/Galaxy-J5-Unofficial-LineageOS-Sources/samsung_kernel_msm8916/commit/c80ec914c9d997a51e1c59c233930fe6078ab7e1)
#### Tuesday 2022-10-11 09:24:42 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>

@acroreiser: backported to 3.10 using can_lookup() helper copied from fs/namei.c instead of d_is_dir()

---
## [john-walter-munene/free-programming-books](https://github.com/john-walter-munene/free-programming-books)@[5fd70502a0...](https://github.com/john-walter-munene/free-programming-books/commit/5fd70502a063c46914fd444d2511c8233f81777f)
#### Tuesday 2022-10-11 09:48:48 by Mathieu FONTAINE

Update free-programming-cheatsheets.md - React (#7095)

I suggested a React cheat sheet that I use very often. It is one of the most exhaustive and qualitative in my opinion.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[22af4efa32...](https://github.com/treckstar/yolo-octo-hipster/commit/22af4efa3266522e4052d58d6f786d8a523bbea2)
#### Tuesday 2022-10-11 10:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [kavishinsa/Prestige-Ocean-Pearl-Kozhikode-Kerala](https://github.com/kavishinsa/Prestige-Ocean-Pearl-Kozhikode-Kerala)@[c6f150c4ad...](https://github.com/kavishinsa/Prestige-Ocean-Pearl-Kozhikode-Kerala/commit/c6f150c4add882b1bf054176ade0a74fe8591532)
#### Tuesday 2022-10-11 11:36:52 by kavishinsa

Get Premium-Quality Apartments at Prestige Ocean Pearl Kozhikode

The demand for residential properties in Kozhikode keeps escalating over the centuries. If you are looking for a quality residential apartment in Kozhikode, check out Prestige Ocean Pearl. This is one of the best residential projects that the builders have come up with in the area. You have flats in several configurations to choose from. While purchasing a home in Kozhikode, investors can choose from 1/2/3 BHK homes. These properties are elegant and expansive. The interior designs look to attract the inhabitants. Besides, lots of common spaces are available for the families around these buildings.

Some of the amazing facilities that you would enjoy in this new gated community include a clubhouse, sports features, and play areas for children. People across all ages can enjoy a great experience with comfort and aristocracy in this development. 

The demand for rental properties in Prestige Ocean Pearl Flats In Kozhikode has been growing. Given that all the new branded residential projects by Prestige come with sophisticated conveniences, it would be a logical decision to own one of these homes. You can earn a consistent income when you rent out these flats to specialists. Once you move to one of these classy residential projects in Kozhikode, you would cherish the blissful lifestyle everywhere.

The city has got a dense network of highways. With good transportation facilities around, it is easy to navigate to the prominent sitting room. Get one of these beautiful homes with lots of open areas around to enhance the quality of your existing. As property prices appreciate in the coming years, you can profit from the growth of your asset price.

For More Details:
Visit Here: https://bit.ly/3CKcwgF

---
## [ErisMeleeEnjoyer/CEV-Eris](https://github.com/ErisMeleeEnjoyer/CEV-Eris)@[9f27ff4cdb...](https://github.com/ErisMeleeEnjoyer/CEV-Eris/commit/9f27ff4cdb153ef85b38c7897ea98e762d7387a3)
#### Tuesday 2022-10-11 11:48:17 by ErisMeleeEnjoyer

Merge branch 'fuck-you-leather-man' of https://github.com/ErisMeleeEnjoyer/CEV-Eris into fuck-you-leather-man

---
## [viethung204/PAINDEALER](https://github.com/viethung204/PAINDEALER)@[61d6a6d917...](https://github.com/viethung204/PAINDEALER/commit/61d6a6d9176d62c880c28fcf939fdac6760d7d58)
#### Tuesday 2022-10-11 12:48:47 by viethung204

misc

brain fried, im gonna cry, creating this game make me wanna fucking die

/srs add respawn mechanic and some other stuffs i cant really remember jfc

---
## [newstools/2022-iol-cape-argus](https://github.com/newstools/2022-iol-cape-argus)@[582b31eda8...](https://github.com/newstools/2022-iol-cape-argus/commit/582b31eda86311a57bcf8413cf79404d4f7296c4)
#### Tuesday 2022-10-11 12:50:50 by Billy Einkamerer

Created Text For URL [www.iol.co.za/capeargus/capeargus/news/tragedy-strikes-as-stellenbosch-principal-wife-daughter-and-her-boyfriend-die-in-car-crash-1c2d7039-e701-42ff-86f2-6d443f06c9eb]

---
## [ekkusa/android_kernel_sony_sdm845](https://github.com/ekkusa/android_kernel_sony_sdm845)@[483182b4d5...](https://github.com/ekkusa/android_kernel_sony_sdm845/commit/483182b4d57309fef4871f88b542c08658ddbedc)
#### Tuesday 2022-10-11 15:12:20 by Jebaitedneko

[HACK]: base: power: wakeup: create a dummy debugfs entry for trace_marker

ah shit you finally disabled debugfs only to see userspace scream at you for not having trace_marker
this is the only driver which creates a debugfs entry which is essential for battery monitoring (see 1bdb13584fb7b5c6b7b741e4436a4dc4397df26e)
adjust it's init function to create said dummy trace file inside tracing dir
this will suppress the silly userspace errors

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[b28fb452c6...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/b28fb452c66abf61018b63b0a58a5ebeee812ee2)
#### Tuesday 2022-10-11 15:17:12 by AmyBSOD

Reticulan downside

Sorry. But let's list the downsides:
- certain relatively annoying monster types are slightly more common
- that's all. Yep, only one downside. Except if you count "starts in the space base" as one.
And the benefits:
- lotsa Pw growth per level
- several rare intrinsics
- buncha good techniques
- doesn't have to fear cannibalism or same-race sacrifice
- higher than average starting stat roll
- and this is the kicker, a fucking INERTIA melee attack that few things can resist.

So yeah. Aggravate monster and the occasional evilroom spawn should even the playing field a little. All this really does is to make the reticulan encounter some more monsters, so it even lets them kill more stuff for XP and loot, but at least some of these monsters will hopefully be not a complete pushover.

---
## [hzhang11111/hzhang11111.github.io](https://github.com/hzhang11111/hzhang11111.github.io)@[a4cb0cafcc...](https://github.com/hzhang11111/hzhang11111.github.io/commit/a4cb0cafcceb37de1327c65d8fc785fb6ed2330d)
#### Tuesday 2022-10-11 15:25:49 by hzhang11111

Create static.yml

The linkage between technology and art


Now that more and more artists are also creating digitally, with many of their works existing purely on the screen, digital art is becoming one of the most valued art forms of our time. With the introduction of NFT, the art world is rapidly changing.

When I first saw Beeple's work "Everyday: The First 5000 Days”, I was shocked. I was more shocked as I knew that it was sold for $69.3 million worth non-fungible token (NFT). It was just paintings at first, but later Beeple began to incorporate abstract themes, color, form and repetition.Over the past five years, the work has become more relevant to the current times and responsive to current events.

The emerging technology has changed our perception towards artwork significantly. Especially,VR.

Virtual reality does more than only make it easier for people to express themselves artistically. Because it is multidimensional, it also enhances the aesthetic experience.

Virtual reality allows users to be part of a piece of art, immersed by art. It allows users to enter an entirely different space where they can view from numerous perspectives rather than just one. With VR, we are able to experience other people’s humanity.

But it also raises a lot of questions: Is VR a way of manipulating human emotions? How long can empathy last after the VR experience?I think VR can evoke empathy, but it doesn't make users think from other people's perspectives. People still need to rely on their own imaginations to construct the experiences of others. 

The mechanism of VR reminds me of the artist Alexa Meade. She does portraits which are painted on the human body and put upon colored backdrops, transform real persons into a flat surface and appear to be 2D pieces of art. The way she chooses to do the opposite of that VR is doing also provides an interesting perspective to think about VR.

---
## [Project-Mika/android_kernel_xiaomi_sm8250](https://github.com/Project-Mika/android_kernel_xiaomi_sm8250)@[1776b72b06...](https://github.com/Project-Mika/android_kernel_xiaomi_sm8250/commit/1776b72b06b77265208c9207c6b7f0e61250cbf6)
#### Tuesday 2022-10-11 15:32:26 by zclkkk

drivers: input: aw8697_haptic: Spoof for QTI vibrator

* Stupid QCOM add a totally unused check in their shit
  vibrator AIDL IDK why. Just spoof to bypass it.
* Ref: https://github.com/LineageOS/android_vendor_qcom_opensource_vibrator/commit/c8f31f143e5ed2bfed4f47193fc7514580e87220
* Again, fuck you QCOMMMMMMMMMMMMMMMM

---
## [Nithish09102002/Run-C-](https://github.com/Nithish09102002/Run-C-)@[055f70d195...](https://github.com/Nithish09102002/Run-C-/commit/055f70d195a502d03fafe3655b71cef3c9b1adfb)
#### Tuesday 2022-10-11 15:36:43 by NITHISH S

Create The Chronicles of Narnia

Four kids Peter,Susan,Edmond and Lucy travel through a wardrobe to the land of Narnia. Narnia is a fantasy world of magic with mythical beasts and talking animals.While exploring the land of narnia Lucy found Mr.Tumnus the two legged stag ,and she followed it, down a narrow path .She and Mr.Tumnus became friends and he offered a cup of coffee to Lucy in his small hut.It was time for Lucy to return to her family and so she bid good bye to Mr.Tumnus and while leaving Mr.Tumnus told that it is quite difficult to find the route back as it was already dark.He told her to see the trees while returning back and said that the first tree with two digits number will help her find the way and the way to go back to her home is the sum of digits of the tree and that numbered way will lead her to the tree next to the wardrobe where she can find the others.Lucy was already confused, so pls help her in finding the route to her home.... 

Input Format:
Input consists of an integer corresponding to the 2-digit number.
Output Format:
Output consists of an integer corresponding to the sum of its digits.

Sample Input
23
Sample Output
5

---
## [druckgott/msp-osd](https://github.com/druckgott/msp-osd)@[1b8b4b6f67...](https://github.com/druckgott/msp-osd/commit/1b8b4b6f67e471360be4560071d0edbc5a8a5205)
#### Tuesday 2022-10-11 17:06:26 by Brian Ledbetter

Fakehd and Config Options (#52) - thank you @benlumley

* Squashed commit of the following:

commit b9bcccbf76974e34c672b0e39c1443bb6ac84af9
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Tue Sep 20 22:48:35 2022 +0100

    switch to config

commit c50d23104e4fb4f6e6a25b2bb0b72fcecc6128f7
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Tue Sep 20 14:16:24 2022 +0100

    changed mind; y direction doesn't need the 1 offset - nicer to have it near the edge; then you can get things inline with the goggles own osd at the bottom

commit 4af3df6c126ac273b03e9191699b92513e1b3f2d
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Mon Sep 19 20:47:59 2022 +0100

    Battery symbols flash when in warning state; so can't use them to trigger centering :(

commit 689384f0449daed42929d90f19c1946368fd0a31
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Mon Sep 19 10:26:58 2022 +0100

    In from the edges a bit; we have spare rows/cols - in my opinion it looks better not to have everything literally touching the sides

commit db06e4885c93a9a0350ffab6afa08fcb068fd63a
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Fri Sep 16 19:39:50 2022 +0100

    Docs review + add fakehd

commit b6f20c0cf2e74e6bca98555c731ea4b11f41d6f4
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Thu Sep 15 22:49:18 2022 +0100

    Debugged/working

commit 8000b88d022fb40e30e0aa7f03df0613c637ece8
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Fri Sep 2 00:15:28 2022 +0100

    Attempt at proof of concept to 'spread' the SD osd to the corners + middle of the HD OSD.

    Not managed to get it running to test. But here's the idea:

    BF grid is 16 * 30
    HD is 18 * 50

    BF Rows 1-5 -> HD Rows 1-5
    BF Rows 6-10 -> HD Rows 7-11
    BF Rows 11-16 -> HD Rows 12-18

    BF Cols 1-10 -> HD Cols 1-10
    BF Cols 11-20 -> HD Cols 20 - 30
    BF Cols 21-30 -> HD Cols 40 - 50

    Visually, divide the OSD into a 3*3 grid and stretch it to the top/bottom/left/right corners.

    I tend to put osd elements in the bottom corners, bottom middle + the warnings in the middle. So for me at least; this is useful.

    Obvious drawback; the menus gonna look weird!

    fix for force hd not working because BF never even sends the MSP command; it needs to default to it earlier.
    also add 2 unsplit rows for wider elemenets - i like warnings in the middle of the screen

    Add full display info; attempt to detect menu/post flight stats and switch to centering in this case

    Remove testing code

    make code paths simpler

    Find the center trigger instead of hard coding

    configurable; with a file for now

commit 60215e0240cbe5d34d0db447b01d948808705ed2
Author: bri3d <brian@brianledbetter.com>
Date:   Tue Sep 20 22:24:16 2022 -0600

    forgot an important directory...

commit 1c5ed2a88feb03bf209e4ed3c3ac4ed277681f47
Author: bri3d <brian@brianledbetter.com>
Date:   Thu Sep 15 21:51:48 2022 -0600

    add goggles config file

commit cfe24e265e8a3bfa92c34d6fc0e9594b63f98928
Author: bri3d <brian@brianledbetter.com>
Date:   Thu Sep 15 21:23:00 2022 -0600

    add JSON config support

* add fake HD to schema

* add ability to disable AU data overlay, add comments, cleanup

* add proper ipk deps and readme

Co-authored-by: Ben Lumley <ben@benlumley.co.uk>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[e9d4bf6c49...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/e9d4bf6c4920f07f03c2425ac3e69caf8daced9d)
#### Tuesday 2022-10-11 17:12:41 by Zergspower

Granite's Love pass 1 of X for ruins  (#16746)

* Fab Five

* forgot to move the rack in front of the false wall

* Holy shit scrapheap looked HORRIBLE

---
## [Opentrons/opentrons-python-packages](https://github.com/Opentrons/opentrons-python-packages)@[6554cce5c2...](https://github.com/Opentrons/opentrons-python-packages/commit/6554cce5c250f86f633f07f4f816a804096c6f11)
#### Tuesday 2022-10-11 17:14:07 by Seth Foster

feat(build): build wheels (#3)

Add the code harnessing to properly build wheels for the OT-2.

This code is a little annoying and complicated. There are three main
parts:
1. Walking the package directory and orchestrating builds (lives in
`builder.build.orchestrate)
2. Dealing with downloading and unzipping sources (lives in
`builder.build.download`)
3. Building the wheels (lives in `builder.build.build_wheel`) and the
attendant shellcall infrastructure (lives in
`builder.build.shell_environment`)

## Walking package directories and orchestrating builds

This isn't really that bad; it's a lot of path manipulation. Options
about builds are bundled up and passed around in dataclasses. The intent
is that you can add new stuff in the packages directory and it'll find
it if you put a `build.py` in there. The `build.py` is eval'd and calls
into `builder.build` with a nice interface to specify how to build the
package.

## Downloading and unzipping sources
This is a little more of the same - give us a url, we'll download it,
we'll unpack it (while trying to avoid trivial tarfile path manipulation
attacks). This stuff goes in build/.

## Building the package and handling shells
It's really annoying to deal with the shellcalls. The previous PR's test
file approached it by running the sdk environment prep once, capturing
all the stuff it did, and passing that to calls. This is weird and prone
to failure because passing environment variables to popen for some
reason is super inconsistent.

The slightly more nuclear option, which this PR does instead, is to have
a single long running interactive shell process that you send stuff to
with stdin. now, you can set up the buildroot environment in the
subshell and just send over commands. Works actually pretty well, and
also has some bonuses like "handles aliases correctly" and "you can add
a venv".

In terms of building, we need to handle build-time dependencies, which
we do via a little venv; and we need to set a whole bunch of other magic
environment flags and options that the sdk doesn't do.

Once we do all that, we can build a wheel!


Closes RCORE-209
Closes RCORE-210
Closes RCORE-215

---
## [dudo/dd-trace-rb](https://github.com/dudo/dd-trace-rb)@[daa758fb94...](https://github.com/dudo/dd-trace-rb/commit/daa758fb944b768229b48167197a8f48b696c26c)
#### Tuesday 2022-10-11 19:52:05 by Ivo Anjo

RFC: Add Sorbet typechecker to dd-trace-rb

 ## TL;DR

* Minimal bootstrapping for now.
* Type checking is optional. Default is no type checking for files
  without a magic comment. Should have minor impact on people that
  don't want to touch the type checking.
* `bundle exec srb tc` runs the type checking.
* I've enabled type checking during CI runs

 ## What?

While not a replacement for all our tests and other tooling, a type
checker is a nice extra line of defense for catching issues that we
otherwise may have missed, such as #1602.

The Ruby ecosystem around type checking is still rather immature. You
may have heard that Ruby 3 shipped "with type checking" but that's an
oversimplification: it actually only shipped with a "language for
describing types" and a "type analysis tool"
(<https://www.ruby-lang.org/en/news/2020/12/25/ruby-3-0-0-released/>).
You may have noticed that nowhere in the previous sentence the words
"type checker" were included.

So, Ruby 3 itself provides no type checker. In practice, there are two
typecheckers in "wide" use for Ruby:

* [Steep](https://github.com/soutaro/steep), created by a Ruby core team
  member that also worked on manny of the other type-related bits that
  made it to Ruby 3 (but steep itself was not made part of Ruby)
* [Sorbet](https://sorbet.org/), a type checker in wide use at Stripe
  and Shopify

This RFC PR does a first pass at onboarding Sorbet to our codebase.
There's a number of limitations on this "first pass", which I document
below.

 ## Why not Steep?

I've tried onboarding our codebase to steep, and gave up due to two big
issues:

1. Steep relies on the Ruby 3 rbs format, but unlike Sorbet, there
doesn't seem to be any way of starting small on a mostly-untyped
codebase without any `.rbs` files, and iterate from there. There are
tools to generate skeleton `.rbs` files (the `rbs` gem has two
different modes for it + the `typeprof` gem), but they had a hard time
with ddtrace.

2. There is currently little documentation for the type checking errors,
once Steep does run. Google gave me ZERO hits on one of them (I guess
it doesn't index the tool repository at least). And they're not all
that easy to understand/fix, so what use is having a tool tell
you "this is wrong", if then you're stuck with little help on something
that may not even be a real issue but more likely a tool limitation?

For these reasons, I gave up on Steep (for this first iteration).

 ## Working with Sorbet

Sorbet can be run with `bundle exec srb tc` (or `bundle exec rake
typecheck`). There's also Language Server Protocol support, if your
editor supports it.

The key thing to know about Sorbet is that allows file-level granularity
for enabling type checks, see
<https://sorbet.org/docs/static#file-level-granularity-strictness-levels>.

In practice, this means that at the top of each `.rb` file, we can
provide a comment that controls the reporting of type checking errors
for that file. The usual ones (described in the above link as well) are:
`# typed: ignore`, `# typed: false`, `# typed: true`, `# typed: strict`,
and `# typed: strong`.

In many cases, **Sorbet can typecheck a file correctly with no extra
type annotations**, so we can start enjoying its checks (such as finding
 #1602) by just enabling it for our files. This can be done with the `#
 typed: true`, `# typed: strict`, `# typed: strong` modes (see the docs
 for details).

The `# typed: false` is the default for files with no comment. Thus,
even newcomers into the codebase will not be forced to immediately deal
with Sorbet for contributions, which given the current limitations of
the tool, and level of maturity, I think is reasonable. (We can
reconfigure this later, if needed). In this mode, Sorbet will only
complain about syntax and missing constant errors.

Our codebase requires quite a few `# typed: ignore` because or
dependencies that are pulled via appraisals and thus not seen/available
to Sorbet (among other things that we do and that Sorbet) doesn't quite
like. These files are completely ignored by Sorbet. (Note that if you
then reference something on one of these files from another file, that
file will not typecheck either, so "ignore" becomes somewhat contagious,
and is best avoided if possible).

I've also added a CI step to run sorbet, which again follows the rules
above so should be able to provide us with valuable insight without
being an annoying source of build failures.

 ## Limitations or "I thought the whole point of this was for us to
   add type declarations to the code"?

Now we get to the more unfortunate part of the news: I think that for
now we don't have great options for doing this.

Sorbet type annotations are supposed to be inline with the code, and
work through the [`sorbet-runtime`]
(https://rubygems.org/gems/sorbet-runtime) gem.

Unfortunately, as described on
<https://sorbet.org/docs/faq#what-platforms-does-sorbet-support>:
> The sorbet-runtime gem is currently only tested on Ruby 2.6 and Ruby
  2.7. It is known to not support Ruby 2.4. Feel free to report runtime
  issues for any current or future Ruby version.

Thus, since we still want to support Ruby 2.1, that doesn't quite work
for us. I thought we could perhaps have an empty replacement of the
sorbet runtime gem, and it turns out that [Shopify already tried and
abandoned it](https://github.com/Shopify/sorbet-runtime-stub). So,
inline annotations seem to be out for us.

For Sorbet, that leaves us with only one other option: `.rbi` files.
These are files that allow Sorbet to get type information for otherwise
untyped code, and are the solution to having type information for many
common libraries.

Unfortunately, using `.rbi` files for our own code is very error-prone,
because Sorbet trusts `.rbi` files, and doesn't check them against the
code. Thus, if we had a class `A` with method `m` declared both on our
code, as well as on an `.rbi` file, and then we renamed `m` to `n` and
forgot to update the `.rbi`, then Sorbet would not complain about it.
Worse, if somewhere there was a call to `A#m` somewhere in the code,
Sorbet would still think it was correct, while in reality it would
break at run-time.

 ## The future?

Because our usage of Sorbet is rather simple, we can at any point
switch to Steep, or any other tool, or just disable it, if it's not
providing value. So we are not locked at all into its usage.

Hopefully in the near future we'll find a way to add type declarations
to our library without impact to our support matrix of older Rubies.

Even better, we could then ship those types to our customers, for them
to check that they are using ddtrace APIs correctly!

---
## [dudo/dd-trace-rb](https://github.com/dudo/dd-trace-rb)@[e391d2eb64...](https://github.com/dudo/dd-trace-rb/commit/e391d2eb64d3c6151a4bdd2710c6a8c7c1d57457)
#### Tuesday 2022-10-11 19:52:05 by Ivo Anjo

Merge pull request #1607 from DataDog/sorbet/rfc-add-sorbet

RFC: Add Sorbet typechecker to dd-trace-rb

 ## TL;DR

* Minimal bootstrapping for now.
* Type checking is optional. Default is no type checking for files   without a magic comment. Should have minor impact on  people that don't want to touch the type checking.
* `bundle exec srb tc` runs the type checking.
* I've enabled type checking during CI runs

## Notes for reviewing

* This PR has two commits -- one that has all of the setup and relevant things, and another which is 100% the result of running `bundle exec srb init`. I strongly suggest reviewing them separately, for added sanity. (If you want to quickly glance through the second commit -- your terminal won't choke on the diff like github does 😉 )
* ~~This PR depends on #1605, and CI is failing for unrelated reasons. Thus, I've opened it as a draft until both of them are cleared and the runway is clear. It otherwise is ready for review/discussion.~~ Now updated.

 ## What?

While not a replacement for all our tests and other tooling, a type checker is a nice extra line of defense for catching issues that we otherwise may have missed, such as #1602.

The Ruby ecosystem around type checking is still rather immature. You may have heard that Ruby 3 shipped "with type checking" but that's an oversimplification: it actually only shipped with a "language for describing types" and a "type analysis tool" (<https://www.ruby-lang.org/en/news/2020/12/25/ruby-3-0-0-released/>).
You may have noticed that nowhere in the previous sentence the words "type checker" were included.

So, Ruby 3 itself provides no type checker. In practice, there are two typecheckers in "wide" use for Ruby:

* [Steep](https://github.com/soutaro/steep), created by a Ruby core team member that also worked on manny of the other type-related bits that made it to Ruby 3 (but steep itself was not made part of Ruby)
* [Sorbet](https://sorbet.org/), a type checker in wide use at Stripe and Shopify

This RFC PR does a first pass at onboarding Sorbet to our codebase. There's a number of limitations on this "first pass", which I document below.

 ## Why not Steep?

I've tried onboarding our codebase to steep, and gave up due to two big issues:

1. Steep relies on the Ruby 3 rbs format, but unlike Sorbet, there doesn't seem to be any way of starting small on a mostly-untyped codebase without any `.rbs` files, and iterate from there. There are tools to generate skeleton `.rbs` files (the `rbs` gem has two different modes for it + the `typeprof` gem), but they had a hard time with ddtrace.

2. There is currently little documentation for the type checking errors, once Steep does run. Google gave me ZERO hits on one of them (I guess it doesn't index the tool repository at least). And they're not all that easy to understand/fix, so what use is having a tool tell you "this is wrong", if then you're stuck with little help on something that may not even be a real issue but more likely a tool limitation?

For these reasons, I gave up on Steep (for this first iteration).

 ## Working with Sorbet

Sorbet can be run with `bundle exec srb tc` (or `bundle exec rake typecheck`). There's also Language Server Protocol support, if your editor supports it.

The key thing to know about Sorbet is that allows file-level granularity for enabling type checks, see
<https://sorbet.org/docs/static#file-level-granularity-strictness-levels>.

In practice, this means that at the top of each `.rb` file, we can provide a comment that controls the reporting of type checking errors for that file. The usual ones (described in the above link as well) are:
`# typed: ignore`, `# typed: false`, `# typed: true`, `# typed: strict`, and `# typed: strong`.

In many cases, **Sorbet can typecheck a file correctly with no extra type annotations**, so we can start enjoying its checks (such as finding  #1602) by just enabling it for our files. This can be done with the `# typed: true`, `# typed: strict`, `# typed: strong` modes (see the docs  for details).

The `# typed: false` is the default for files with no comment. Thus, even newcomers into the codebase will not be forced to immediately deal with Sorbet for contributions, which given the current limitations of the tool, and level of maturity, I think is reasonable. (We can reconfigure this later, if needed). In this mode, Sorbet will only complain about syntax and missing constant errors.

Our codebase requires quite a few `# typed: ignore` because or dependencies that are pulled via appraisals and thus not seen/available to Sorbet (among other things that we do and that Sorbet) doesn't quite like. These files are completely ignored by Sorbet. (Note that if you then reference something on one of these files from another file, that file will not typecheck either, so "ignore" becomes somewhat contagious, and is best avoided if possible).

I've also added a CI step to run sorbet, which again follows the rules above so should be able to provide us with valuable insight without being an annoying source of build failures.

 ## Limitations or "I thought the whole point of this was for us to add type declarations to the code"?

Now we get to the more unfortunate part of the news: I think that for now we don't have great options for doing this.

Sorbet type annotations are supposed to be inline with the code, and work through the [`sorbet-runtime`](https://rubygems.org/gems/sorbet-runtime) gem.

Unfortunately, as described on <https://sorbet.org/docs/faq#what-platforms-does-sorbet-support>:
> The sorbet-runtime gem is currently only tested on Ruby 2.6 and Ruby 2.7. It is known to not support Ruby 2.4. Feel free to report runtime issues for any current or future Ruby version.

Thus, since we still want to support Ruby 2.1, that doesn't quite work for us. I thought we could perhaps have an empty replacement of the sorbet runtime gem, and it turns out that [Shopify already tried and abandoned it](https://github.com/Shopify/sorbet-runtime-stub). So, inline annotations seem to be out for us.

For Sorbet, that leaves us with only one other option: `.rbi` files.
These are files that allow Sorbet to get type information for otherwise untyped code, and are the solution to having type information for many common libraries.

Unfortunately, using `.rbi` files for our own code is very error-prone, because Sorbet trusts `.rbi` files, and doesn't check them against the code. Thus, if we had a class `A` with method `m` declared both on our code, as well as on an `.rbi` file, and then we renamed `m` to `n` and forgot to update the `.rbi`, then Sorbet would not complain about it.
Worse, if somewhere there was a call to `A#m` somewhere in the code, Sorbet would still think it was correct, while in reality it would break at run-time.

 ## The future?

Because our usage of Sorbet is rather simple, we can at any point switch to Steep, or any other tool, or just disable it, if it's not providing value. So we are not locked at all into its usage.

Hopefully in the near future we'll find a way to add type declarations to our library without impact to our support matrix of older Rubies.

Even better, we could then ship those types to our customers, for them to check that they are using ddtrace APIs correctly!

---
## [cdcline/demo-website](https://github.com/cdcline/demo-website)@[d7bf630155...](https://github.com/cdcline/demo-website/commit/d7bf6301557eeed6838e9b3bfee14c1ed25a7ed7)
#### Tuesday 2022-10-11 20:55:36 by Chris Cline

Design Beta: Animate Welcome Header Circles

Currently all the headers are static and we'd like them to be animated.

The Welcome Header has some circles that we'd like to kinda move around in
the background.

This adds a couple circles and animates them to randomly move to a new X, Y
position over a random time.

It also hacks in some header logic to display the new code.

The JS also got a bit wonky with multiple files requiring the same
external file so the loading order of them got modified a bit.

Part of #108

---
## [raspbian-packages/git](https://github.com/raspbian-packages/git)@[f78d87f2c9...](https://github.com/raspbian-packages/git/commit/f78d87f2c9849984012e7cdac3b7910d98f46305)
#### Tuesday 2022-10-11 21:26:14 by Johannes Schindelin

protect_ntfs: turn on NTFS protection by default

Back in the DOS days, in the FAT file system, file names always
consisted of a base name of length 8 plus a file extension of length 3.
Shorter file names were simply padded with spaces to the full 8.3
format.

Later, the FAT file system was taught to support _also_ longer names,
with an 8.3 "short name" as primary file name. While at it, the same
facility allowed formerly illegal file names, such as `.git` (empty base
names were not allowed), which would have the "short name" `git~1`
associated with it.

For backwards-compatibility, NTFS supports alternative 8.3 short
filenames, too, even if starting with Windows Vista, they are only
generated on the system drive by default.

We addressed the problem that the `.git/` directory can _also_ be
accessed via `git~1/` (when short names are enabled) in 2b4c6efc821
(read-cache: optionally disallow NTFS .git variants, 2014-12-16), i.e.
since Git v1.9.5, by introducing the config setting `core.protectNTFS`
and enabling it by default on Windows.

In the meantime, Windows 10 introduced the "Windows Subsystem for Linux"
(short: WSL), i.e. a way to run Linux applications/distributions in a
thinly-isolated subsystem on Windows (giving rise to many a "2016 is the
Year of Linux on the Desktop" jokes). WSL is getting increasingly
popular, also due to the painless way Linux application can operate
directly ("natively") on files on Windows' file system: the Windows
drives are mounted automatically (e.g. `C:` as `/mnt/c/`).

Taken together, this means that we now have to enable the safe-guards of
Git v1.9.5 also in WSL: it is possible to access a `.git` directory
inside `/mnt/c/` via the 8.3 name `git~1` (unless short name generation
was disabled manually). Since regular Linux distributions run in WSL,
this means we have to enable `core.protectNTFS` at least on Linux, too.

To enable Services for Macintosh in Windows NT to store so-called
resource forks, NTFS introduced "Alternate Data Streams". Essentially,
these constitute additional metadata that are connected to (and copied
with) their associated files, and they are accessed via pseudo file
names of the form `filename:<stream-name>:<stream-type>`.

In a recent patch, we extended `core.protectNTFS` to also protect
against accesses via NTFS Alternate Data Streams, e.g. to prevent
contents of the `.git/` directory to be "tracked" via yet another
alternative file name.

While it is not possible (at least by default) to access files via NTFS
Alternate Data Streams from within WSL, the defaults on macOS when
mounting network shares via SMB _do_ allow accessing files and
directories in that way. Therefore, we need to enable `core.protectNTFS`
on macOS by default, too, and really, on any Operating System that can
mount network shares via SMB/CIFS.

A couple of approaches were considered for fixing this:

1. We could perform a dynamic NTFS check similar to the `core.symlinks`
   check in `init`/`clone`: instead of trying to create a symbolic link
   in the `.git/` directory, we could create a test file and try to
   access `.git/config` via 8.3 name and/or Alternate Data Stream.

2. We could simply "flip the switch" on `core.protectNTFS`, to make it
   "on by default".

The obvious downside of 1. is that it won't protect worktrees that were
clone with a vulnerable Git version already. We considered patching code
paths that check out files to check whether we're running on an NTFS
system dynamically and persist the result in the repository-local config
setting `core.protectNTFS`, but in the end decided that this solution
would be too fragile, and too involved.

The obvious downside of 2. is that everybody will have to "suffer" the
performance penalty incurred from calling `is_ntfs_dotgit()` on every
path, even in setups where.

After the recent work to accelerate `is_ntfs_dotgit()` in most cases,
it looks as if the time spent on validating ten million random
file names increases only negligibly (less than 20ms, well within the
standard deviation of ~50ms). Therefore the benefits outweigh the cost.

Another downside of this is that paths that might have been acceptable
previously now will be forbidden. Realistically, though, this is an
improvement because public Git hosters already would reject any `git
push` that contains such file names.

Note: There might be a similar problem mounting HFS+ on Linux. However,
this scenario has been considered unlikely and in light of the cost (in
the aforementioned benchmark, `core.protectHFS = true` increased the
time from ~440ms to ~610ms), it was decided _not_ to touch the default
of `core.protectHFS`.

This change addresses CVE-2019-1353.

Reported-by: Nicolas Joly <Nicolas.Joly@microsoft.com>
Helped-by: Garima Singh <garima.singh@microsoft.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>
(cherry picked from commit 9102f958ee5254b10c0be72672aa3305bf4f4704)
Signed-off-by: Jonathan Nieder <jrnieder@gmail.com>

Gbp-Pq: Name 0016-protect_ntfs-turn-on-NTFS-protection-by-default.diff

---
## [TotalWipeOut/laminas-log](https://github.com/TotalWipeOut/laminas-log)@[ed0a3cc5d4...](https://github.com/TotalWipeOut/laminas-log/commit/ed0a3cc5d40f110f72934e0f8e672215892420f7)
#### Tuesday 2022-10-11 21:50:04 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [bgamez23/15-3athena](https://github.com/bgamez23/15-3athena)@[2e283b56ec...](https://github.com/bgamez23/15-3athena/commit/2e283b56ecf8bb28d14a860354ca53f3eb306e8b)
#### Tuesday 2022-10-11 22:52:42 by 15peaces

== Bug fixing & more ==
=General:
*Merged missing changes from 3ceam rev. 835

*Partial rewrite of the chat system.
-Thanks to @rathena.
-This replaces the old temp-fix for 2015+ clients with the missing zero termination.
-This should also fix some random dcs and visual glitches related to some chat messages (aka random text at the end of some messages)

*Fixed an issue where the attr_fix database was not read correctly, causing element calculations to be wrong.

*Gold Thief Bug card / Wand of Hermode now blocks the following status's....
-Adoramus / Imprison / Manhole / Chaos (Chaos Panic) / Bloody Lust / Insignia's / Blood Sucker.

=Skills:
*WL_HELLINFERNO
-Recoded the skill.
-Now deals 2 seprate hits of damage.
-The first hit is fire damage and the 2nd hit is shadow damage.
-Chance of burning now only applies to the fire damage.
-Magic Power status now properly increases the damage of both hits.

*RA_ELECTRICSHOCKER
-Official duration reduction formula added.

*SR_FALLENEMPIRE
-Now uses its official status and prevents regular attacking and movement.

*WM_DANCE_WITH_WUG
-Now gives a ATK bonus to Ranger/Minstrel/Wanderer type jobs.

*SO_VACUUM_EXTREME
-Recoded the skill.
-Affected enemy's will now be pulled to the center of the AoE.
-Duration of status is now that of the AoE's remaining active time.
-Duration reduction formula updated to official.
-No longer affects those in Hallucination Walk or Hovering status.
-Note: The durations basicly act as strength power.
-The Vacuum's strength is affected by skill level and weakens over time as the AoE is active. The higher your STR, the stronger the vacuum's suction strength you can resist. 120 STR for example lets you resist a vacuum that has a duration or 6
-seconds or less remaining.

*GN_SPORE_EXPLOSION
-Recoded the skill.
-Countdown now handled the same way like Venom Splasher.
-Target carrying the spore bomb will always be hit by the explosion.
-The explosion animation will now only appear on the exploading target.

*AB_OFFERTORIUM
-Now removes the following status's from the caster....
-Poison / Curse / Confusion / Blind / Bleeding / Burning / Frost / Hallucination / Mandragora / Guillotine Cross Poisons (Except Oblivion).

---
## [bgamez23/15-3athena](https://github.com/bgamez23/15-3athena)@[13c5b886cf...](https://github.com/bgamez23/15-3athena/commit/13c5b886cf93a27a8ec3a89ae64d6ab147d80902)
#### Tuesday 2022-10-11 22:52:42 by 15peaces

== Pet fixes & 3ceam merges ==
=General:
*Merged missing changes from 3ceam rev. 840 - 841

*Fixed some more pet issues.
-The pet egg will now be hidden if the pet is hatched and will be re-shown if the pet is sent back to the egg.
-Also the pet friendly rate is now correctly shown in the egg description.

*Added the "NK_FORCE_RANGED_DAMAGE" setting for skills.
-This forces the skill to deal ranged damage at ranges below 5.

*Recoded the handling of Minstrel/Wanderer party checks for chorus skills to only be called on when needed. This should further save on cpu cycles used on skill use.

*skill_chorus_count
-Added this function for counting performers in a party.

*mass_spiral_max_def
*rebel_base_lv_skill_effect
-Added these config settings to the skill battle config.

*Added the "rageball" command.
-It does what it sounds like. Summons Royal Guard's rage spheres.

*Fixed a number of issues caused by monsters/clones when they use 3rd job and other renewal era skills. This should stop crashes from happening on skills with casters weight / cart weight checks and spirit sphere checks. It also fixes issues with
-learned skill level checks for them so they will use the skill's highest possible level to maximize the skill's damage/effects as if a player used it.

*Recoded the ZC_MILLENNIUMSHIELD packet.

*Recoded the entire rage sphere system.
-This fixed a few issues that existed for far too long.
-Now the sphere's will display properly on screen refresh, appear to players walking within range of another player with rage spheres, and players who warp to another map.
-It also fixes invalid/lost timer issues caused by unknown means.
-Finally it also fixes the handling of the spheres on GM's during skill use.

*Added a few status tags.

=Skills:
*RK_DRAGONBREATH
*RK_DRAGONBREATH_WATER
-Corrected the AoE for level 9 to be 9x9.

*RA_WUGRIDER
-Fixed an issue where the options where set wrong.

*RA_WUGBITE
-Corrected a issue where the damage increase from Dance With Wug wasn't counting the chorus bonus correctly.

*RA_WUGDASH
-Corrected a issue where the damage increase from Dance With Wug wasn't counting the chorus bonus correctly.
-Fixed a issue where the caster's weight affected the damage formula incorrectly.
-Fixed a issue where the bonus damage from Tooth of Wug was not being applied.

*RA_WUGSTRIKE
-Corrected a issue where the damage increase from Dance With Wug wasn't counting the chorus bonus correctly.
-Skill name is no longer yelled out when autocasted through regular attacks.

*NC_POWERSWING
-Fixed a issue where it autocasted Axe Boomerang when you don't have it learned.

*LG_FORCEOFVANGUARD
-Chance of getting rage spheres now applies to all damage types.

*LG_RAGEBURST
-Recoded the skill.

*SR_RAMPAGEBLASTER
-Is now treated as a ranged attack.
-Damage formula updated.

*SR_KNUCKLEARROW
-Damage formula updated to official for use on players and monsters.

*SR_GENTLETOUCH_ENERGYGAIN
-Chance of getting spirit spheres now applies to all damage types.

*WM_DEADHILLHERE
-Now flagged as a magic skill.

*GN_CART_TORNADO
-Increased caster's STR effect limit to 130.

*RL_MASS_SPIRAL
-Damage formula updated.
-No longer ignores the target's flee.

*RL_S_STORM
-Updated the equip break chance formula to official.

*RL_H_MINE
-Grenade explosion AoE is now 5x5.

*RL_FIRE_RAIN
-Is now treated as a ranged attack.
-AoE stepping speed adjusted to official.

*RL_HAMMER_OF_GOD
-AoE for the random strike area on unmarked target's is now 15x15

*RA_UNLIMIT
*GN_ILLUSIONDOPING
*WM_FRIGG_SONG
*AB_OFFERTORIUM
-Corrected a issue where the casting of these skills were not interruptable.

*RK_LUXANIMA
-Added cooldown time.

*GD_GUILD_STORAGE
-Now requires level 10 Guild Extension.

---
## [bgamez23/15-3athena](https://github.com/bgamez23/15-3athena)@[aefe0e522a...](https://github.com/bgamez23/15-3athena/commit/aefe0e522a1dcbb821f26a2f035acd121740b934)
#### Tuesday 2022-10-11 22:52:42 by 15peaces

== Some fixes ==
=General:
*Added missing changelogs, sorry... ^^"

*Fixed the CZ_COMMAND_MER packet for 2018+ clients.
-The homunculus menu is now working fine again.

*Fixed an warning in clif_parse_cz_config function.
-Added pre-support for homunculus autofeed flag.
-Support for this feature might be added later.

== Missing changes of r342 ==
=General:
*Merged missing changes from 3ceam rev. 846

*This is the first part on the revisiting of the Kagerou/Oboro skills.
-Part 2 will come at a later date.

*Cleaned up and optomized some code.

=Skills
*Kagerou/Oboro
+Fixed a issue where none of the skill cast times were interruptable.

*KO_HAPPOKUNAI (Spray Kunai)
+Recoded the skill.
+Damage is now ranged physical. Basicly a stronger version of Throw Kunai.

*KO_MUCHANAGE (Over Throw)
+Recoded the skill.
+Damage is no longer reduced in GvG/BG areas.
+Damage is no longer reduced by half on enemy players.
+Success chance of hitting is now seprate for each enemy target.
+Damage is now divided between enemys detected in AoE.
-This means its divided based on the number of enemy's detected in the AoE
-and not by the number of enemys hit.

*KO_HUUMARANKA (Launch Huuma Shuriken)
+Damage no longer split between targets.

*KO_MAKIBISHI (Makibishi)
+Recoded the skill.
+Fixed a issue where it didn't follow the rules of AoE placement.
+No longer ignores elemental adjustments.
+No longer stacks on top of each other.
+Stun duration is now fixed and can't be reduced.
+Now places the proper number of makibishi depending on skill level used.

*KO_MEIKYOUSISUI (Clear Meditation)
+Recoded the skill.
+Skill now makes the caster sit when the status starts. If the caster stands up
-at will or gets forced to stand up, the status will end. This also prevent's
-the caster from being able to move or use any skills while active due to sitting.
+Now has a chance of making any attack completely miss the caster while active.
+Now removes a single debuff by random on use. The following can be removed....
-Poison / Curse / Silence / Blind / Fear / Burning / Frost / Crystalize.
+This behavior is official according to zone scans but a bug does exist on official
-where the skill use animation would stop the caster from sitting, allowing
-exploiting of skill uses. I coded it to prevent this issue from happening.

*KO_KYOUGAKU (Illusion - Shock)
+Recoded the skill.
+Now has a success chance reduceable by the target's INT.
+Duration is now reduceable by the target's INT.
+Now only usable in GvG and Battleground maps and on enemy players only.
+Will now fail if used on a target already affected by this skill.
+Affected target can no longer switch or unequip equips.

*KO_JYUSATSU (Illusion - Killing Curse)
+Now only usable on enemy players.
+Now reduces the affected target's current HP if the chance of curse is successful.

*KO_ZENKAI (Spread Seals)
+Can no longer be stacked on top of each other.
+Random status chance is now applied every second.
+Random status success chance is now 100%, but is reduceable by stats and equips.
+Durations of the random status's is now set to their original defaults.
+Friendly player's standing in the AoE will now get a WATK increase if the weapon
-element is the same as the AoE's element.

*KO_IZAYOI (16th Night)
+Updated the MATK increase formula.
+Corrected the animation handling.

*KG_KAGEHUMI (Shadow Hold)
+Corrected the animation handling.
+Fixed a issue where affected player's didn't stop moving.
+Affected targets will not beable to use the following skills for the duration...
-Hiding / Cloaking / Cloaking Exceed / Camouflage / Shadow Form / Dark Cloud
-Also blocks the use of any teleporting methods including fly/butterfly wings.

---
## [PixelTheKermit/PvP-RIM](https://github.com/PixelTheKermit/PvP-RIM)@[72a812a2cc...](https://github.com/PixelTheKermit/PvP-RIM/commit/72a812a2cc422ee624e00a98c712bd34f0f2b7d4)
#### Tuesday 2022-10-11 23:00:39 by PixelTheKermit

this is the only soft crits update you get, fuck you I am not ruining my sanity any more.

---
## [ychin/macvim](https://github.com/ychin/macvim)@[83e925e923...](https://github.com/ychin/macvim/commit/83e925e9230bbdff93379b5dde3b8b36b561eb40)
#### Tuesday 2022-10-11 23:52:13 by Yee Cheng Chin

Support dictionary/data lookups of text

This adds support for looking up data under the mouse cursor. Usually it
will bring up a dictionary, but other times it could be a Wikipedia
article, Siri knowledge, etc. Apple doesn't really have a good name for
it, other than "looking up data", "quick look" (a confusingly similar
name with the other Quick Look OS feature), or "show definition". You
can activate this by doing Ctrl-Cmd-D when the mouse is over a cursor.
If you have a trackpad, you can also either activate this using Force
click or three-finger tap (depends on your system preference settings).

Note that for Force click, this could potentially make it impossible to
use the MacVim `<ForceClick>` mapping in Vim, which allows you to map a
force click to a Vim command (#716). This is handled by having a new
setting (under a new "Input" preference pane which will have more
populated later) that allows you to choose whether to use Force click
for data lookup or Vim's `<ForceClick>` mapping. If you have configured
to use three-finger taps though this setting wouldn't do anything, and
`<ForceClick>` is always send to the Vim mapping.

Also, this is lacking a lot of features that a normal macOS application
would get, e.g. looking up selected texts (e.g. if you have "ice cream",
you may want to select the whole thing to look up the phrase, rather
than just "ice" or "cream"), data detector, and much more (e.g. custom
API support). They will be done later as part of #1311.

Technical details below:

The way the OS knows how to look up the data and present it is by
talking to the NSTextInput/NSTextInputClient. Previously MacVim
implemented NSTextInput partially, and didn't implement the critical
firstRectForCharacterRange:actualRange and characterIndexForPoint:
functions. First, in this change we change from NSTextInput to
NSTextInputClient (which is the newer non-deprecated version), and
implement those functions, which allows the OS to query the text
storage.

By default, the OS sends a quickLookWithEvent: call to us whenever the
lookup happens but for some odd reason this isn't automatic for Force
clicks, presumably because some apps want to handle Force clicks
manually (this is why some apps only work for three-finger taps but not
Force clicks for lookups). This isn't documented but I found references
in iTerm/Firefox, and basically we just need to manually handle it and
send off quickLookWithEvent: when handling Force clicks.

For implementing the NSTextInputClient properly, the main issue is
making sure that can work properly with input methods / marked texts,
which is the other primary purpose for this class (other than inputting
keys). For data lookups, I'm representing the grid as a row-major text
(with no newline/space in between) and expose that to the OS. This
already has some issue because it doesn't handle Vim vertical splits
well, as MacVim doesn't really have access to detailed Vim text buffers
easily (unless we do a lot of calls back-and-forth). This means wrapped
texts won't be looked up properly, which I think is ok. Also, the OS
APIs deal with UTF-8 indices, so we can't just convert row/column to raw
indices and have to do a lot of character length calculations
(especially for wide chars like CJK or emojis) to make sure the returned
ranges are consistent and valid. For marked texts though, this presents
a challenge because Vim doesn't really have a strong enough API to
communicate back-and-forth about the marked positions and whatnot (it
only let the GUI know where the current cursor is), and it's hard to
implement APIs like `markedRange` properly because some marked texts
could be hidden or wrapped (if you implement some of these functions
improperly Apple's input methods could start misbehaving especially when
you use arrow keys to navigate). In the end I kept the original
implementation for treating the marked texts as a range starting from 0,
*only* when we have marked text. Kind of a hack but this makes sure we
work both in marked text mode (i.e. when inputting texts) and when doing
lookups. For simplicity I made it so that you can't do data lookups when
in marked text mode now.

Input method:

This change also fixes a quirk in input method as a driveby change.
Previously the logic for calculating the rect for where the candidate
list was quite broken, but now it's calculated correctly using the
desired range and the current cursor position. This matters when say
using Japanese IM and using the left/right arrow to jump to different
sections of the text. If the desired range is in a wrapped line, the new
logic would attempt to pin it to the left-most column of where the
cursor is in the range.

Data detection:

Note that the default implementation is quite bare, and lacks a lot of
smart data detection. For example, if you put your mouse over a URL, it
won't properly select the whole URL, and addresses and dates for example
also won't get grouped together properly. This is because these require
additional implementation (e.g. using NSDataDetector) instead of coming
"for free", and will be handled later. In fact, Apple's WebKit and
NSTextView cheats by calling an internal API framework called "Reveal"
(which you can find out by intercepting NSTextView's calls and/or
looking at WebKit's source code) which is much more powerful and
supports looking up package tracking, airline info, and more, but it's
not available to third-party software (that's why Safari's lookup is so
much better than Chrome/Firefox's).

This isn't tested right now. Future task needs to add XCTest support to
properly test this as there are a lot of edge cases involved here.

Fix #1191
Part of Epic #1311, which contains other items to be implemented.

---

