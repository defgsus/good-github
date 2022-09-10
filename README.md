## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-09](docs/good-messages/2022/2022-09-09.md)


2,112,887 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,112,887 were push events containing 3,129,821 commit messages that amount to 228,496,549 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [thinkingfish/ccommon](https://github.com/thinkingfish/ccommon)@[e9fe98094d...](https://github.com/thinkingfish/ccommon/commit/e9fe98094d8748ae44e501f1be8a4a5eb307a1df)
#### Friday 2022-09-09 00:02:41 by michalbiesek

Fix synchronize ccommon with pelikan deps/ccommon (#212)

* ThreadSanitizer: Fix thread leak in test_thread in ring_array suite (#212)

Summary:
fixes ring_array test case that was leaking a thread

* cmake: fix check detection (#216)

Building on Ubuntu 18.04 fails with missing symbols message
due to lack of proper libraries being automatically linked
against tests.

This patch uses pkgconfig to automatically detect system-installed
libcheck, and also gets rid of the unnecessery symbol requirement in
favor of a simple version check.

* fix python2-ism (#199)

this shows the age of my shell script snippets :)

Tested this with both python 2.7.14 and 3.6.3.

* CDB with an FFI-friendly implementation

straight copy-pasta of src/server/{twemcache => cdb}

checkpoint - squash

remove flag

checkpoint

create cdb workspace so shared libs link properly

gah i need someone who knows cmake

failling, about to try rando CMakeRust module

got further with this Rust macro stuff

omg, actual progress

oops, add the macros

rearrange and clean up dependencies

clean up cruft

compiles and links on debian

beginning pelikan side of integration

checkpoint

generate both static and shared targets

shared library building ftw?

this is fine.

checkpoint - string still getting truncated

fix build

check

try and fix build

debugging cmake vars

checkpoint

hi wil

revert

change to system calling scheme, no diff

finally seems to have linked properly

checkpoint

checkpoint

ignore cdb files

squash

add compile_commands.json to gitignore

squash

squash

remove redundant return

hook up cdb_get, munge a response and cleanup

missed two places for raw_val

need to rework storage strategy

shit, revert this mess

Revert "shit, revert this mess"

This reverts commit e369bd7769281393c38f50119f3b650890ed294a.

gahhhhhh

ugh, this is sketchy

bindgen is compiling and linking

compiles again, finally

---
## [agajic-modoolar/odoo](https://github.com/agajic-modoolar/odoo)@[b3b85cae9b...](https://github.com/agajic-modoolar/odoo/commit/b3b85cae9b1951b82053d7c6b55e559cbc48307d)
#### Friday 2022-09-09 00:10:00 by Xavier Morel

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[1b39905b91...](https://github.com/treckstar/yolo-octo-hipster/commit/1b39905b913ff8f40dacc1169f0961e1ec6f6601)
#### Friday 2022-09-09 00:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Tastyfish/-tg-station](https://github.com/Tastyfish/-tg-station)@[3b2cf65d59...](https://github.com/Tastyfish/-tg-station/commit/3b2cf65d59aa5ae22876b0ebabecb564ccb912d0)
#### Friday 2022-09-09 00:37:43 by san7890

Rocking The Boat, er, Map Vote (#69561)

* Rocking The Boat, er, Map Vote

Hey there,

A while ago, I spooke (typo intentional) to some other people. One frustration I heard was the fact that people would sometimes sneak through map votes during the very start of a shift, during a high-paced portion, or just as a meme. People in OOC would then flood the vote, putting in any given station. However, if a vote happens 10 minutes in- and the round goes for 70 minutes and not many of the original players are around, then it's not particularly fair to those who have to play next shift on a map they bemoan.

So, we can rock the vote! If a player isn't particularly chuffed with the hand they are given, they can poll the players to see if they want to change the map as well. If rocking the vote goes through, huzzah, you get the ability to vote for the map again. If it doesn't go through: tough luck. You can rock the vote one time per shift by default, and server operators can change the amount of times you can call to rock the map vote at their discretion. Calling to rock the vote either successfully or non-successfully counts as a "call", and when that limit is exceeded: no more calls.

Does this mean that we will only rotate between two maps because pissants will keep rocking the vote until they get what they like? Maybe? I still see people bemoan getting Tram or shit the bed over IceBox, but I think enough people get sick of bread-on-butter to take the server where it need to go. If operators don't really like seeing only two maps play, they can always adjust the config to ensure it doesn't happen.

* makes the grammar grammar

it would be "Rock the Vote vote" otherwise

---
## [sjp38/linux](https://github.com/sjp38/linux)@[4ebf1aae12...](https://github.com/sjp38/linux/commit/4ebf1aae124d7b8b3df6753358603996e9d24de5)
#### Friday 2022-09-09 00:37:44 by Johannes Weiner

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
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[e1839f0e37...](https://github.com/Stalkeros2/Skyrat-tg/commit/e1839f0e375a2169c8d80d942376dddb8be1958d)
#### Friday 2022-09-09 02:15:11 by SkyratBot

[MIRROR] Spider Rebalance PR: Burn Baby Burn Edition [MDB IGNORE] (#15997)

* Spider Rebalance PR: Burn Baby Burn Edition (#68971)

This is a remake of #66106, with more thought put into the underlying balance. The main goal of this PR is to make fighting spiders more accessible and interesting for the majority of the crew while nerfing the extremely strong and boring option of simply using freezing temps to kill spiders. Also fixes #67765. The changes are as follows:

NEW SPIDER COUNTERS

    Fly swatters now deal 25 damage to spiders on hit, increased from 1
    Pesticide now deals massive stamina damage to spiders and a little bit of physical damage as well (the damage portion not added by this PR)
    Spiders can now be caught on fire through any traditional mean of catching something on fire. Spiders will automatically put themselves out after a time. This was done instead of an active action because AI spiders are also subject to this change as well, and I don't feel like bloating the simple mob AI with putting themselves out

SPIDER CHANGES

NERFS

    Toxin injection has been removed from all spiders except for the hunter, flesh spiders and the viper
    Hunter toxin (used by hunters and flesh spiders) now only brings the afflicted down to 40 health, and will stop taking effect once the afflicted reaches that threshold. Should the afflicted still have the toxin in their system and get healed, the toxin will begin dealing damage again until the afflicted is at 40 health or below again
    Viper toxin now only brings the afflicted down to 10 health, but also has the hallucination effects of Mindbreaker toxin. This hallucination effect is applied regardless of target health. It also no longer generates other harmful chemicals into the afflicted's system, but is much more potent at base
    Flesh spiders cannot regenerate while on fire

BUFFS

    Time it takes for spiders to normalize their temperature cut by half. While they will react faster when in cold or hot environments, when they leave said environments it will take less time to return to normal temperature
    Unsuitable temperature damage reduced to 4 from 8
    You can no longer push spiders by running into them
    Webbing heat damage threshold increased from 300 to 350 (same temp where spiders also take damage)
    Broodmother egg laying time reduced to 12 seconds from 15
    Broodmother web laying time multiplier reduced to 0.5 from 1
    Broodmother health increased to 60 from 40
    Broodmother damage increased to 10 - 15 from 5 -10

BEHIND THE SCENES CHANGES

    You can now make any simple mob able to be caught on fire by setting flammable to true
    How fast a simplemob stops burning is controlled by fire_stack_removal_speed
    Can now now control how fast simplemobs regulate their temperature using temperature_normalization_speed. Before this PR, this value was hard-coded at 10, I have set the default to 5 as 10 was too long in almost any case. This will notably affect slimes, who could easily die to being cold long after being removed from the cold area. I see this as purely beneficial
    Toxins now have a health_required value. The afflicted has to be above this health value in order to take damage from the toxin. Only used in the spider toxins currently
    When I was setting up simplemobs to be flammable, I noticed basic mobs can be glitchily set on fire, so I fixed it to where they can't be set on fire.

Why It's Good For The Game

    Spacing something is very easy, but not very fun or interesting compared to starting and controlling a fire. Swapping spiders' temperature weakness from spacing to fire is beneficial to the fun of fighting them and playing as them, allowing more creativity and resourcefulness on both sides. Ideally, this should allow for atmosians and chemists to use their skills in a fun way.
    Currently, ignoring spacing them, the only people who can reasonably take on spiders is security, since they have lasers which do burn and stuns to slow the spiders down. However, this small subset of players cannot normally destroy a spider infestation without spacing them, so letting fly swatters and pesticide be used to combat spiders allows other crewmembers to fight back, letting them actually enjoy facing spiders as a threat and allowing the crew to defend themselves.
    Being killed by spider toxin after fighting off a horde isn't fun. The changes still make it a threat you have to be aware of, but not one which detracts as much from the combat loop. This also forces spiders to secure the kill themselves, which is more fun than having the toxin do it for you.
    Broodmothers in their current state are incredibly weak by themselves, which is intentional by design. However, the new changes hope to make playing as a broodmother easier and hopefully allow more broodmothers to get the spider infestation started properly. After all, Dynamic is their common source now, and they should be consistently worth the threat cost to spawn them.
    Previously, spider structures would seemingly vanish for no reason if the room was heated to be greater than 300 but less than 350, as the spiders would not be able to tell that it was too hot. Now, if the structures are taking damage, spiders will also be taking damage, so understanding what's going on should be easier now.
    Pushing spiders into a corner by running into them was not a fun tactic to deal with as a spider and didn't make much sense seeing how big the spiders are.

Changelog

cl
add: Spiders can now be caught on fire
add: Spiders take significant damage from fly swatters and stamina damage from pesticide
balance: Spiders have been re-balanced. Their toxins can no longer kill but they are not as susceptible to freezing
balance: General stats of spider broodmothers have been buffed with more health, damage, and faster web and egg placement
balance: Flesh spiders cannot regenerate whilst on fire
balance: Simplemobs change their internal temperature twice as fast
fix: Basic mobs no longer glitchily catch on fire.
/cl

* Spider Rebalance PR: Burn Baby Burn Edition

Co-authored-by: IndieanaJones <47086570+IndieanaJones@users.noreply.github.com>

---
## [gnoff/react](https://github.com/gnoff/react)@[b6978bc38f...](https://github.com/gnoff/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Friday 2022-09-09 03:12:02 by Andrew Clark

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
## [intel/linux-intel-lts](https://github.com/intel/linux-intel-lts)@[9709c8b5cd...](https://github.com/intel/linux-intel-lts/commit/9709c8b5cdc88b1adb77acdbfd6e8a3f942d9af5)
#### Friday 2022-09-09 04:41:02 by Linus Torvalds

gpiolib: acpi: use correct format characters

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[f0ceecff46...](https://github.com/Sonic121x/Skyrat-tg/commit/f0ceecff46f9b600dfe8e60199f354f61d63a0a4)
#### Friday 2022-09-09 06:13:10 by SkyratBot

[MIRROR] Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff [MDB IGNORE] (#16000)

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff (#69158)

About The Pull Request

Title!
The CO2 thing is there because it makes my job much easier. Can probably find a way to make it move slowly if a maint insist on it. Prefer not to though.

Drafting because I want to make a second PR that have more sweeping changes (clean vars up, make a simpler formula for damage and heat production, delete underused behaviors, etc). Would honestly prefer if both this and that gets merged at the same time but I'm separating it out since it might be rejected. Or maybe ill combine it here we'll see.
Ignore that, looks like i can keep this one absolutely atomic.
Why It's Good For The Game

Had a lot of trouble when trying to document the SM gas interactions into the wiki, the interactions are all scattered and tracking down everything a gas does is extremely annoying. Hopefully this fixes that.
Changelog

cl
balance: CO2 powerloss inhibition now works immediately based on gas composition instead of slowly ramping up.
refactor: refactored how the SM fetches it's gas info and data. No changes expected except for the co2 thing.
/cl

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [Project-Elixir/frameworks_base](https://github.com/Project-Elixir/frameworks_base)@[5e7439952a...](https://github.com/Project-Elixir/frameworks_base/commit/5e7439952afc2a977a1b53542b816acb44c18247)
#### Friday 2022-09-09 07:03:27 by Joey Huab

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
## [bellomia/matlab-multiple-dispatch](https://github.com/bellomia/matlab-multiple-dispatch)@[c20b41e38f...](https://github.com/bellomia/matlab-multiple-dispatch/commit/c20b41e38f7c880ff4753977cd06ed05555f76ed)
#### Friday 2022-09-09 07:48:07 by Gabriele Bellomia

Add functional handle constructor: h = obj.activate; h(varargin)

> to allow calling the generic interface just as a function, instead of
  using the ugly obj.dispatch() syntax

⚠️ Note that if a method is added to the object, the handle would NOT
   access it unless the user "reloads" it by running again <activate>.

EXAMPLE
————————————————————————————————————————————————————————————————————————
>> % init the interface object,
>> % there are no methods at first
>> % (but there would be a one-shot constructor eventually)
>> f = interface

f =

  interface with properties:

    method_list: {}

>> % Add a specialized implementation,
>> % by providing a lambda function
>> % (or a handle of course) and the type signature...
>> f = f.add_method(@(x,y)(x+y),["numeric","numeric"])

f =

  interface with properties:

    method_list: {@(x,y)(x+y)  ["numeric"    "numeric"]}

>> h = f.activate % emit a function handle to allow nice calling

h =

  function_handle with value:

    @(varargin)dispatch(self,varargin{:})

>> h(3,3) % test... and works!

ans =

     6
>>
>> % NOW, imagine this is what the library exports
>> % to the user, not just h(), but also the object f
>> % what we want now is to allow extending f, and
>> % eventually h(), of course....
>>
>> % So let's add another method
>> f = f.add_method(@sin,"numeric")

f =

  interface with properties:

    method_list: {@(x,y)(x+y) ["numeric", "numeric"]  @sin  ["numeric"]}

>> h(pi/2) % If I don't "reload" it is not accessed by the handle
>> %         (but this could make sense I guess...)
Error using interface/dispatch (line 59)
no method found

Error in interface>@(varargin)dispatch(self,varargin{:}) (line 34)
        handle = @(varargin) dispatch(self,varargin{:});

>> h = f.activate % So let's activate again the interface

h =

  function_handle with value:

    @(varargin)dispatch(self,varargin{:})

>> h(pi/2)

ans =

     1

>> % hell yeah, successfully added another method,
>> % /dynamically/, which is the crucial requirement.
————————————————————————————————————————————————————————————————————————

---
## [NetworkManager/NetworkManager-ci](https://github.com/NetworkManager/NetworkManager-ci)@[bd1865d97f...](https://github.com/NetworkManager/NetworkManager-ci/commit/bd1865d97f562e00c9845ab86819d55c2c17930e)
#### Friday 2022-09-09 08:18:09 by Thomas Haller

prepare: drop "get_online_state" check

I proposed this before ([1]), but it was rejected back then. Here again.

When having a container, there is no eth0 or global connectivity managed
by NetworkManager. This check will then fail, unless we activate a suitable
profile in NetworkManager. Sure, maybe some tests require such an eth0 interface
too, and the test would still fail without it, however that is
probably something that should be fixed and not reject by "envsetup.sh".

This check really does not belong to "envsetup.sh". If you buy into the
notion that "envsetup.sh" has a defined purpose, then it's probably to
prepare the environment. Checking for connectivity via NetworkManager is
not part of that, in particular, when we will have environments where
this is not a given.

Each CI test needs to check itself that it's pre-conditions,
test-conditions and post-conditions are satisfied. But "get_online_state"
is not a condition that concerns all tests, and such checks don't belong
to "envsetup.sh" anyway.

Also, "prepare/envsetup.sh" wrote a state file to "/tmp/nmcli_general", which
is then printed by "run/runtest.sh". So part of the API of "envsetup.sh"
was to (maybe) generate such a file. That's really ugly, and alone for
that it has to die.

[1] https://gitlab.freedesktop.org/NetworkManager/NetworkManager-ci/-/merge_requests/1075#note_1421829

---
## [havoc-nessity/coffee_shop_python_game](https://github.com/havoc-nessity/coffee_shop_python_game)@[a2fd67fd39...](https://github.com/havoc-nessity/coffee_shop_python_game/commit/a2fd67fd39b05374acbe256e8e8e2995ef6add07)
#### Friday 2022-09-09 09:11:08 by havoc-nessity

Update README.md

fuck github, fuck git, fuck firefox, god damn you all

---
## [vamosraghava/free-programming-books](https://github.com/vamosraghava/free-programming-books)@[97016edd67...](https://github.com/vamosraghava/free-programming-books/commit/97016edd6791285128758dd91904b343d1f3b0fd)
#### Friday 2022-09-09 09:11:25 by David Ordás

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
## [Raltyro/FNF-PsychEngine](https://github.com/Raltyro/FNF-PsychEngine)@[1f2fb70829...](https://github.com/Raltyro/FNF-PsychEngine/commit/1f2fb70829c230e6ced2bda96477565a21309617)
#### Friday 2022-09-09 10:49:30 by Raltyro

Reworked CreditState + Changes in Desc

+ Made AdvancedSubstate for Options
+ Move few Options to AdvancedSubstate
+ Check for Updates Rework however almost no one uses them lmao
+ Fixes some annoying shit in psych inputs like omg IT WASNT MS BASED :sob:

---
## [simias/dwm](https://github.com/simias/dwm)@[67d76bdc68...](https://github.com/simias/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Friday 2022-09-09 11:58:18 by Chris Down

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
## [lcnr/rust](https://github.com/lcnr/rust)@[1c35596762...](https://github.com/lcnr/rust/commit/1c3559676265f2c320f4e361fece080b0f464f97)
#### Friday 2022-09-09 12:29:06 by Dylan DPC

Rollup merge of #101455 - thomcc:why-is-this-here, r=jyn514

Avoid UB in the Windows filesystem code in... bootstrap?

This basically a subset of the changes from https://github.com/rust-lang/rust/pull/101171. I didn't think to look in src/bootstrap for more windows filesystem API usage, which was apparently a mistake on my part. It's kinda goofy that stuff like this is in here, but what are you gonna do, computers are awful.

I also added `winbase` to the `winapi` dep -- I tested this in a tmp crate but needed to add this to your Cargo.toml -- you `use winapi::stuff::winbase` in this function, but are relying on something else turning on that feature.

---
## [Zynthful/Flintlock-Forte](https://github.com/Zynthful/Flintlock-Forte)@[1de5685083...](https://github.com/Zynthful/Flintlock-Forte/commit/1de5685083c6620aa5a2e3910847c31c30d7288e)
#### Friday 2022-09-09 13:33:07 by Jamie Carnell

hell.

 - Fixed (not really but kind of) collisions
 - Created a GameObjectSpawner which spawns enemies and also causes a read access violation because fuck you

---
## [nspcc-dev/neo-go](https://github.com/nspcc-dev/neo-go)@[b27e6918bd...](https://github.com/nspcc-dev/neo-go/commit/b27e6918bd969cc07f738ba96c7f246f44ede319)
#### Friday 2022-09-09 14:08:54 by Roman Khimov

Makefile: complicate version detection script

We've declared that we are using semantic versioning. We also want to use `git
describe` to make version strings for us because it's very convenient for
development builds (tagged versions are way simpler). The problem is that the
default `git describe` behavior is not semver compliant. If the most recent
tag is v0.99.2 then it'll generate something like '0.99.2-131-g8dc5b385',
which according to semver is a development version _before_ 0.99.2. While it's
obviously a version _after_ 0.99.2.

That's the one and only reason we have vX.Y.Z-pre tags in our repo. We set
them right after the release according to the release process and that gives
us some '0.99.3-pre-131-g8dc5b385' versions we're all used to. But these tags
are ugly as hell and they clutter up our repo over time.

So there is this idea that we can do patch version increment dynamically.
Making '0.99.2-131-g8dc5b385' be '0.99.3-pre-131-g8dc5b385' without any *-pre
tags. This patch implements this. It's ugly as hell as well, but at least
that's an ugliness somewhere inside our Makefile and not directly visible in
our tags. If we're to do this we can then greatly simplify our release process
(and even allow for CHANGELOG patches to be merged normally).

I know this can be done with awk in somewhat easier way, but no, I'm not into
awk, sorry.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[f881486719...](https://github.com/mrakgr/The-Spiral-Language/commit/f881486719a63b688a2a980fe441e629bb9b35f7)
#### Friday 2022-09-09 15:58:39 by Marko Grdinić

"9:05am. I am up. The weather was bad so I went to bed before 12am. I wasn't as obsessed as last night, so I got some proper sleep, but it was light.

At any rate, I beat the Spawn of Rovagug with my existing lvl 15 party after respecing Harrim into a buff machine. I don't think any of the guides that I've seen online are good. I've realized that the Spawn's attacks are super dangerous and you really need to kill it before its first turn. The way to do it is to have a Skald in your party, have him share his pounce ability, and at least 2 other meleers and have them pounce charge into the fray. I made a big mistake having Valerie be in the party. Yeah, having a tank is useful in general, but not here. Alternatively, have a 3 buffed up lvl 20 Slayer archers. Their capstone ability to get a full round attack with just a standard action would be really good for these alpha strikes. That should get the odds up to 90%.

The thing about the Spawn of Rovagug is that it is dangerous even when dead. I killed it twice only to have one of the allies turn around and kill the MC due to its insanity attack that ignores compulsion immunity. Most of the other time it starts healing at such a rapid rate that I can't bury it before he oneshots me with his AOE attack.

9:25am. Let me finally leave this behind me. I think my lvl 15 party had only 20% chance of beating it. If I was playing Last Azlanti I'd never have challenged it at this stage. It'd be much easier at lvl 20.

9:30am. Let me chill. Focus on reading manga for a bit and then I will resume writing. I'll finish this chapter, proof it and then publish it.

9:55am. There was a power outage. Let me chill properly.

10:30am. Let me finally start. I am really chafing here. I am going to change my plans. Instead of waiting for 300 pages, since I have been writing for a whole month already I'll start putting things on Patreon already starting with what I have written. I'll split it into 3 parts post the first one on RR, and the other two on Patreon. I'll also start blog posting on a special page there.

Enough of this shit. The reason I couldn't get through those interviews is because airing my true thoughts in such a public place jinxed me.

And rather than start, I need to shut down. Thunder. Damn.

11:55am. It has finally passed. It seems like the summer is over. The weather is getting colder.

Though rather than start here, let me just have breakfast.

12:30pm. https://mangadex.org/title/cc8dc41e-1f7e-4e52-9a8f-2e24de5e5c9c/rwby-ice-queendom

I should catch up to RWBY at some point, but nevermind it for now.

12:40pm. Let me finally start. Focus me.

$$$

(Heaven's Key, Heavenly realm)

    You aren't responsible for the beginning, but you can be responsible for the ending.
    Complete the work that nature started.
    -Loading Blurb

Slowly, out of the pocket of his trenchcoat, the revolver came out. To my eyes, the movement seemed impossibly smooth and ethereal. I had a sense of time and could see exactly the trail the gun followed and as he raised it, where it would go. As if to draw out the tension, the white haired guy lifted the gun straight up, paused it a bit and then swung it down until it was pointed straight at me. He had a grin on his face. In perfect slow motion, I could see him put his finger on the trigger.

I knew what would happen next.

The last time I was here I got shot to death. This time, my mind is whirring a lot faster, so even though I have a second in game time until the trigger gets squeezed, I have 27h to think about my next move in actuality. If this wasn't a game running at 10,000x speed, but the real world I'd have 30 years. Before I had started the game, the controller me did a memory merge, so I understood everything that I'd missed while I was crossing the Street. Right now I have the programming and the ML skills of the controller, and the optimized mind of the instance that beat the Street game, as well as the memories of both.

I understand what the controller wants, which is to beat this white haired dude with my newly found superintelligence.

But as I am staring down the barrel of the gun, I am really wondering what I could do here.

Make my body resistant to bullets? Make them phase through my body? Regenerate the wounds?

I am racking my brain here, but I don't know how to do this. I try to do an act of will here. I picture a rock in very vivid detail and try to manifest it in front of me. My mind is working too fast for the body to react, so I do not make any movements, but nonetheless I try to focus all of my mental abilities into making something happen.

...

As expected, nothing is happening. I do not know how the white haired dude is doing it, but there must be some other trick to it than just wanting magic to work really badly. Expanding my mind and speeding it up, didn't do much to change the situation from where I was a human. I am going to get a few new holes either way.

[Gnosis check DC 1.9 Succeeded - Sampled 2.76]

Imminent death facing me, I get a sudden burst of inspiration. I realize that if I just let things as they stand, I am just going to get shot like last time. It is inevitable. So I might as well quit the game now and go to an earlier save. There is no point in letting the events unfold. That much is obvious, but...is it really? I suspend my disbelief and seriously consider eating a few bullets. I then realize something.

Was I really killed last time?

This situation is just too weird. Last time I took it at face value, but it is strange that the game would allow one of the players to kill another. Last time, I just aborted the game due to shock once the darkness overtook me, but had I actually gotten a notification that I died from the game itself?

I do not think that happened. Did I abort the game too quickly to get that notice? Did I simply miss it in my panic? Or is there something deeper to this?

I can't help, but to loathe myself for what I am going to do, but let's eat a few bullets to make sure of what is going on.

Bang...

I put all my willpower into not escaping to an earlier state and let the lead object pierce my chest. Damn it, it hurts! Like last time, I look at the bloody wound in horror, and on cue the white haired guy empties the rest of the magazine.

Bang...bang...bang...bang...bang...

The speed at which my mind works now really drew out the horror of this moment.

I sprawl out on the table, waiting for death to come to me. Like before, I can see my blood pooling out on the table until it covered my two face down cards. And then my vision became hazy and dark. Like last time, I couldn't make out what the white haired dude was saying. It felt distant...

Like that, I slipped into unconsciousness and death.

But...since this was a game, while it can simulate many things, it can't literally simulate the absence of life. Not without killing me in the real world as well. And now that I am keeping my emotions in order, I realize that despite being dead, I can still think just fine. I can't hear anything, I can't see anything, I can't touch anything. But my mind is working.

I feel out with my senses and I realize that I still have the connection with my chip pile. I wait a while in that senseless space, and there is no change. While I can't feel anything else, my life chips are still there. And I don't get a death notification from the game itself. Meaning, the game was still on.

Experiment Success!

I save the game here and exit it.

I should have noticed this last time, but that is the weakness of the mind controlling program that I used to get rid of my fear. It is one thing to be calm, but creativity requires an active and restless mind. It is easy to notice what is there when you are calm, but hard to notice what isn't. I guess that is the difference between what you need to be a member of society and what you need to conquer it.

(Heaven's Key, Inn room)

I go back to one of the earlier save states. This point in time is exactly before I slipped out in secret out of my room through the window and explored the city. It was the dead of night and I wasn't tired enough to sleep, so that is why I did it. It was that time I met Mickey in the park of ghosts.

I remember what that translucent old ghost told me. That we are all holograms here. And the system is what determines what exists based on our inner state.

Right now I am sitting on my bed with the lights turned off in the room. I close the curtains and flip them on. Then I manifest a body sized mirror and sit in front of it, pondering.

I need to figure out the trick to becoming translucent. Mickey did it somehow and if I could do it as well, it would give me a hint for how to deal with bullets. I'll go about it scientifically. I don't really know how to trick the system into doing it, but it is not like I can't interface with it at all.

For example...I take out one of the chips, place it on the floor in front of me and using it as a focus, manifest a bottle of water.

Rather than asking how I should change my body, why not instead start by asking how I did this obvious bit of magic?

This gives me a lot of information about the system. It is commonly believed that VR works by hijacking your senses, but if it was just that, then how would movement work? Obviously it has to capture a lot more from the brain in order to be able to do those. But why stop there?

That I could manifest this bottle as I'd imagined it is proof that the system understands my desires... and in the dueling realms, it rejects them. Well, Mickey told me as much, but I am thinking things through and confirming them as I go along.

Then the next step would be, rather than just my desires, my true beliefs...

I spend a few minutes thinking about it from various angles.

Honestly, I have no idea how I'd do this if I were a human. If I were a human it'd literally be like trying to develop psychic powers. I'd have to try out all sorts of drugs in order to get something going, messing myself up in the process. Maybe get into the occult mindset. It is dumb.

But as I am now, the various perspectives are all converging to one conclusion. If I am right, it should actually be pretty easy.

I have access to the entirety of my mind, and thought is merely the transfer of high dimensional vectors throughout the system. A small part of that data describes whether for example I am looking at a water bottle or just imagining a water bottle. It makes sense, otherwise I wouldn't be able to tell my own imagination and reality apart. This is a very good thing, since in the real world, perception does not affect reality, but here the system is literally basing a part of it on what it sees in my mind.

So if I mess with those thought vectors and conveniently erase the part of the data that tells me what the imagination is, I should make my first step on becoming a reality warper.

Doing this unhindered is dangerous as I'd completely lose track of what is real and isn't.

I understand where things are going with this though. If I could make it safe, I would receive a strong power. Right now even though I've increased my intelligence significantly, my emotional system is still that of a human. When I lost to the white haired guy the first time, I swore that I'd challenge him as a player, not as a character in a game.

This capability of tricking myself to think my imagination is reality should not be in my own hands, but the player's. But there is no reason why I couldn't automate the process eventually. It is like how computer programs become a part of you once you get rid of the interface obstructions, one day the player and the character might be one. Furthermore, now that I've moved from the human model of cognition to my own streamlined one, the tool I was using to regulate my emotions before has become unusable. I need to recover its capabilities by making my own version of it.

I am still a beginner, my capability is nowhere near close enough to the person who made this game. The game is here to teach me.

Anyway, what I have to do is straightforward now that I've planned it out. The first thing I have to get out of the way is the player. The one who is currently supervising me is no good. I need him to have at least my level of capability otherwise he won't be able to keep up.

I really need the controller to help me in this because my own measure of what is sane and isn't will become distorted once I start relying on this power, and I don't mean that in the based, anti-normie way.

I need to account for any and all risks.

Having made my decision, I open up a text editor and compose a message to the controller. After that I save the game, and as a show of will, I terminate my own process.

(Helix Studio, Regent Suite, Bedroom)

I was using the emotion controlling tool to keep my focus up, so I was in fact paying attention to what was going on. Still, it is not like I can read my other self's thoughts. So far, I saw him get shot by the white haired guy, reload back a week ago, and then spend a few minutes staring at himself in the mirror. Then he terminated himself, which shocked me enough to curse. I was really perplexed as to what was going on and started thinking that something might have gone wrong in the optimization process to make him mentally unstable. My thoughts went in that direction for a few seconds and then I realized I got a message from him.

> Subject: Self-Improvement Step Request

What followed is a report by him that went into great detail regarding his thinking since he started the game. It hadn't even occurred to me to think about whether he deliberated to load back right away or get shot purposely. It went on for a couple of pages and by the end I got the gist of what he wanted to develop and why he wanted to replace me with somebody more fitting.

> You won't be able to keep up, I need somebody more fitting for the role.

He literally said as much directly to me. Sigh. I didn't think my turn would come so quickly. I've been expecting him to challenge Lily's group without relying on saveloading and was looking forward to seeing how he does it, but it seems a lot of action has happened in his head that I've been unaware of.

...It is just too soon, so let me compromise. The report he wrote demonstrated his intelligence to me, so I no longer have any doubts about him being broken in some way. But nonetheless, I want to see him in action before I just hand him the reins to everything. If something goes wrong, who is going to take the responsibility of explaining that to the main me who is currently sleeping in the real world?

Maybe the role of the controller is too much, but I need to spend a while observing. So I'll do that.

I copy his paused process and do a memory merge. Then I make the necessary setup and start him in a different Helix Studio limbo. Now he should have what he needs to act as a controller. He'll be able to fork himself and start the game.

If this was a real self-improvement step, I'd erase myself here, but I am not going to do that, not yet. He is asking me to literally kill myself for him, so it is fair that I take some time to observe before deciding if I want to go forth with it. The report he sent me was pretty interesting. I'll have him do a writeup at the end of every day. At his speed of thought it shouldn't take him more than a few seconds, and it really gives me an insight into what is going on.

(Helix Studio, Skylark Island)

> Hello, welcome to Skylark Island. Whereas most character limbos tend to be obvious, this one is heavily inspired by the Simulacrum scenario Wordly Abyss, and it is magic based. In order to acclimate the host, the tutorial messages will show up as you explore the areas. For now, keep in mind that you can access the spell list whenever you wish for it.

Before I copied myself, I wasn't aware of what I would pick, so this limbo is new to me. I remember seeing it in passing during past selections. The controller me picked something weird this time. I guess he didn't want to duplicate the Regent Suite.

This place was interesting, it was like a cottage made of wood. There was a table, chairs for it. It wasn't too big, certainly smaller than the Regent Suite. But whereas regular wood cottages were made of modular wood planks and boards, walls, the floors, and the ceiling and indeed the furniture seems to be made of molded wood, as if it were grown. It was how I'd imagine a fantasy druid would build it. He wouldn't use saws and nails, but magic to guide nature into the shape he desired. Looking behind me, I realize what I see is a bed.

It isn't really obvious at first glance, as it looked like some furry, green plant. It had some oversized leaves that felt like animal fur to my touch and bended flexibly as I'd moved it. The pillows were some kind of membranes and I could see liquid inside them. I poke it a bit and realize that while it is flexible, it is also tough and won't burst easily. It felt smooth to the touch. I tried the bed out and found that it felt comfortable to rest here.

I like this place. As I walked, I noted than unlike the regular floor, this one was a slightly uneven due to being bark. My first thought was that this would make it difficult to position furniture, but when I tried out the chair and sat on it, I found that it had a bit of springiness, which ensured its seat was always balanced horizontally. The chair legs had some kinds of cushions as well that balanced the unevenness.

The table itself, unlike the floor, was made of smooth polished wood. I brushed my hand along its surface, liking how it feels.

This is a really nice feeling of adventure. It is like being a child during its first days in the world.

I take a look at the windows from my sets in the middle of the room, and realize that instead of glass, they seemed to be some kind of translucent membrane. I come up to it, touch it a bit, push it and note how flexible it is. I give it a punch. My fist sinks into it, but the membrane does not tear, instead it bounces me backwards and comes into the original straight position. I approve, it feels reliable as a window.

Looking through the window I realize that the place I am in is quite high up. My cottage in particular is high in the island, but beyond the island it feels like it is a very deep drop given how high it is. It reminds me looking over the edge of the city in Heaven's Key, though not quite that high. In the distance I can see the sea, the mountains and the forests. Sunlight gleams off it, and I get the impression of looking at another natural wonder.

In the minds of people, when people think of technology, they think of steel and concrete. Cars, robots, machines. Guns, tanks, airplanes. Skyscrapers.

But maybe that is wrong. They haven't realized it yet, but maybe the true form of technology is celestial in nature. These simulated worlds. Can breathtaking wonders that I've seen, and the powers that I am trying to attain be anything other than divine?

The brain cores that I've gotten are supposedly mostly made of carbon. Experiencing them from the inside, they don't feel technological in nature at all.

I brush away these thoughts and come to the door. It doesn't have a handle, but two wooden hooks on the side. I detach them and the door slides inward as if it were a measuring tape. Like the windows, the door was made of sturdy and flexible biological material that looked like wood, but was more like plant matter that I'd guess doesn't exist in the real world.

I poke my head outside and realize there is a huge drop below. As I imagine splattering myself below, I get a sense of vertigo and take a step backward.

> If you want to exit the building to explore the rest of the island, please use the Wings spell.

I get a helpful notification and do as instructed. As I do some large fairy wings manifest themselves on my back, and my body feels weightless. This reminds me of being a disembodied entity in the Heaven's Key title menu, and I find that it is much the same. Rather than having to beat them against the air to take flight, they are more like an antigravity device attached to my back.

I have no trouble controlling my flight and exit the room to explore the island beyond.

I spend some time playing like that and then I create a fork of myself and plug it into the game.

(Heaven's Key, Inn room)

"I am visualizing my hands at twice their usual size. How are my recordings?" I ask the controller who is at Skylark Island.

Back in the game, I am seated in front of the big mirror. I have my hands raised in front. I think it is due to the latest batch of improvements, but my imagination is very vivid compared to before. I can almost see my enlarged hands overlaid over my regular ones as if they were real. No amount of desiring they are real will be enough to make it so. instead the controller me has to be the one to make the step. While I am focusing on visualization, right now he should be looking directly at my brain studying the neural messaging as it occurs.

"I've recorded it, but it is a bit hard. Instead try imagining yourself pinching your hand." I do as instructed.

"Good, now actually pinch yourself lightly." I do it just enough to be a bit painful.

"I see it. Now relax. Don't try to think of anything." I do so. What happens next is that I get a bizarre feeling of having my hand in front of me and pinching it with the other. It feels a bit dissonant, but eventually that fixes itself by me focusing on it. Just like before, I seem to be imagining pinching myself, but there is an obsessive streak to it. I am finding it difficult to focus on anything else. I endure it for a while and then feel relief.

"Good. I've aborted the program, how is your mental state?" He messages me.

"I seem to be fine." I replied. "The obsession is gone."

"Is that how it feels like? Anyway, I'll try the actual pinching next."

"Ah!" Feeling being pinched, I raise my hand to look at it. I expected to see some pain, but I am surprised to see that my skin is physically twisted. It is as if an invisible hand was pinching it. I try to relax the skin with my other hand, but it does not help. The feeling of my skin being pulled remains and after I remove it, I see the pinching fold again. "Are you seeing this?" I show it triumphantly.

"It is a success! I think I understand this. Let's try the hands again. This is like hacking memory states to cheat in games. Focus on the hands and I'll try to edit the relevant thought vectors based on the previous recording. I don't want to make everything real."

I raise my hands in front of me and focus, imagining them to be oversized. As I do so something in me shifts, and to my surprise, it works. What was once imagination turns into reality. I clench and unclench them, marveling at the unfamiliar sensations. I try using them to lift the water bottle and unscrew the bottle. It feels so weird, but they aren't clumsy. I take a gulp, and screw the cap back on.

"This is pretty cool." I show off my hands in front of me. The controller can't see or feel anything my senses can't. He doesn't have direct access to them through his own mind, instead he is looking at what I am seeing through the screen. Eventually what we have planned is to integrate the rest of the senses into him, so he can feel directly what I feel through separate neural channels. If the controller had that kind of ability, it would make his work a lot easier. At the end of that road, what the controller will become is a higher order consciousness for myself, able to control me as I would a video game character.

At that point, we'll be able to do these transformations instinctively. For now...

"This is cool, but let's turn them back. I'll imagine them being normal. You do your thing." I message him.

I look at my hands and imagine them being the same as before. As I watch, I again get that strange impulse like a gear in my head has skipped a turn and the hands transform back into their previous shape. I flex them to test them out and satisfied, I let out a breath.

"Phew. We've got it!"

That white hair dude is going to get what is coming to him. Right now I could go back to that dead end, and try to resurrect myself. Except, it is one thing to imagine my hands changing shape, but quite another to imagine having a living body. I am getting ahead of myself. We did just the very first step. The program we have is not capable of flexible whole-identity transformations. We should challenge him when we are ready.

Right now, how about we beat on some noobs?

I think back to Lily and Dale's group.

They are the ideal testing ground to develop our skills at programming the language of the mind.

Back then I just scammed them out of a ton of chips, but then they sent the tough white haired guy after me. This time I am not going to do it using saveloading, but with my own skills. Maybe if I did it that way, something different would happen.

Me and the controller burned the candle late into the night, creating some simple cheating methods and trying out what we would call the True Belief Modification. It wasn't until later that we realized that the method we invented was the legendary hallmark of the stories of the Inspired. Their titular ability was called the Inspired Desire. This was its embryonic form.

(Heaven's Key, Raven's Eye Casino, Shadow realm)

"Fold." On the small button, Lily folded.
"Check." The thin guy who has been looking down on me, follows up.
"Fold."
"Fold." The two guys behind me toss away their cards.
"Call." I limp into the pot. I look to my left, and see Dale deliberating. He raises from 4 to 12. I look at his face down card, and based on the red markings, I note that he has suited Ah Th.

My own hand is crap, an unsuited Jd 7h. To Dale's left, the thin guy thinks for a bit and folds. Unlike Dale's card, only one of his cards had a marking. Even though my hand is weaker than Dale's, since I know what he is holding it is hugely beneficial to enter the pot regardless, so I call.

The flop manifests.

Ks Qc Tc.

There is a flush draw on this board, but Dale has hearts rather than clubs. He hit a low pair. A very dangerous flop for him. I do not hesitate and lead out by betting 20 into the pot. Dale hesitates and stupidly makes a call, bringing it up to 70.

On the turn, 5c comes out. Not hesitating, I shove my entire pile and go all in.

Dale stares at me for a while, trying to read my mind.

"Fold." He makes the sensible decision, and I increase my pile by 38 chips.

In this hand, I happened to have a straight draw, but I'd have played it the same way regardless of what I was holding.

The hands we are holding get purged, and the next round starts promptly. I get dealt two cards, and luckily, they don't have markings on them. I check my hand to see what it is, 2d 9c, and silently message the controller.

> Manifest the UV pigment on my fingertips.

I feel the familiar feel of something skipping in my brain and with a light touch put two marks in the right places. With a light brush, as I move the cards, I make two angular lines at 30-60 degree angle to either of the edges. That way if the card is rotated, I won't be confused as to which is the rank and which is the suit marking.

As I look at the group, each of them is covered in a film of blue, or more more to the point, my entire vision is that way. I've modified my eyes so I am capable of seeing in UV. It wasn't too difficult, it used to be the case that laser surgery of cataract got rid of the membrane protecting the lens, which allowed the patients to see UV. I had to study the structure of the eyeball for a while, but after that I modified my true belief to change my eyes’ structure and got the ability to see in UV. After that it was just a matter of doing research on pigments and finding the right one.

Thanks to this cheating method, I can take it easy during the first few revolutions, just marking cards and only playing strong preflop hands. After that once the blinds go up, I can loosen and jump into the fray to land a sneak attack.

A few days ago, I started the matches at 240 chips, and now I am up to 600. My winnings are a lot slower than when I was saveloading, but I am really happy regardless. This is real power! I worked hard to get to this point and my reward is that now I can beat these people. It might be possible to use something like this in real life, but the method is too unrefined and would easily be found out in a casino. Here I have my improved eyes, and can manifest the pigment directly on my fingers. If I had to carry around a can of it in my pocket, it would quickly get spent. Moreover, I wouldn't want to damage my eyes just to cheat at cards. My vision is crap so there is no need to make it even worse. But if I came to the table wearing fancy UV glasses, it would raise some eyebrows.

Using this method in reality is beneath me. I have much better things planned.

Anyway, I continue playing and notice that things are moving quicker this time. Whereas before the party tried really hard to bust me, now that I am winning by what looks like actual good play, the party is close to breaking. I can tell that the others are hesitating and exchanging looks when I propose duels.

A few days earlier than last time, Lily doesn't arrive and her place is instead taken by an old guy named Geoffrey.

After a few games with him, I get the sense that rather than focusing on winning, he is instead watching me like a hawk, not really caring about any of the other players. He radiates an aura as if he is preparing to strike me, but nothing happens and I just end up making some money off him. This is fine, I guess.

(Report by Geoffrey to the Enforcement Department)

Subject: Aleator-level enforcement request

One of the newcomers from about a week ago is currently in possession of 680 chips. I've played him personally, and in my estimation, he is at least a low ranked Aleator who possesses the ability to mark cards, probably via UV markings. He does a little move where he brushes over the cards after looking at them. He employs a strategy of playing strong hands at the start, and once the cards have been marked, he loosens up and picks the other players off. He has decent game playing skills from what I've observed even without the use of cheats.

We've done extensive background checking and confirmed that he is a newcomer, he should be easy prey for an experienced Aleator.

In the attachments are the report I received from my subordinate guide as well as my own. The reports have extensive recordings of our games with him.

(Heaven's Key, Streets)

Night comes, I go back to the inn, and then once the morning gets around it is time for action again.

The next day I played with Dale's group again, but they've started to clam up. Once I realize that I switch to bluffing more often and take the money off them that way. I was uncomfortable going all out, but the controller did some modifications and spiked my confidence, allowing me to execute the strategy properly. I blitzed the table, and it felt good picking on those weakling with my strong bets. Hell, yeah!

That day, as the sun was falling beyond the horizon in the background, I exited the casino in high spirits, swinging a pair of big ones.

> Be on guard. I think that guy Geoffrey was responsible for sending that white haired guy after us last time.

I get a message from the controller. We are a dream team, me and him. My own skill at both manifesting my imagination and poker is growing, while on his own end, I can sense he is getting new insights about the mind. We've already recovered a lot of the functionality of the mind controlling app over the last week.

Doing as he instructed, I unwind a bit and take note of the surroundings. Gleaming golden buildings enter my attention. The rays of light look quite beautiful at this time of day, painting the town in a crimson tint. The work day is starting to wind down and I can see people returning to their places. The usual boisterous atmosphere of the golden city is starting to quiet. Compared to the real world, where you usually have some insects chirping at night, when it gets quiet here, it becomes deathly quiet.

As I walk the streets, the previous scenario repeats itself. Not the white haired guy, but some other one walks around the corner and moves straight towards me, looking me straight in the eyes like he wants to kill. In his hand, he manifests an object and soon the game is on.

Bang!

(Heaven's Key, Shadow realm)

After the bullet was fired from a gun, I found myself in the familiar duel space. Looking around, I am surprised that the background is the familiar deep space with bluish nebulas. I thought that resolution matches would be different, but maybe the reason for the background change last time was different. I take a good look at my assailant. Unlike the white haired guy, I am not going to let this guy off. I am going to send him straight to the grave. I am going to kill for the first time.

As I think that, my killing intent surges. Forget those tiny duels against Dale's group. This is what a real match should feel like.

My chips here are my life and blood. Even if I beg, the assassin is not going to let me off. There is only one way to survive, and that is to kill him first.

I calm myself down and take a deep breath. As I do, the well dressed pig on the other side gives a snort and takes a glance at his hand. He looks like a stereotypical NEET, but rather than grease stained sweaters and years-old clothing frayed around the edges, he is wearing a fresh monochrome suit. I think it looks quite decent on him, I myself am wearing the same casual clothes as in the real world, so I lose out versus him on the fashion front. Still, he should consider getting a diet. I am not sure if that is even possible in this city though. He was probably a NEET before he died and got stuck in this form.

So then...that probably gives me a good estimate of his ability. Since people wouldn't want to look like him, and he himself would probably want to change his appearance to something better, I am guessing he can't do form changing using True Belief Modification like I can. This is just a conjecture rather than an actual fact, I can only interpret this situation as making it more likely than if he had regular body mass.

"Check." He makes the first move.

> Modifying the eyes.

As I get a message from the controller, the world becomes covered in a thin layer of blue, which is the UV light as I perceive it.

Using my thumb to twist the cards upwards, I take a peek at my hand. Trash unsuited 2s 9h. As I close it, I make sure to put the red UV markings on it. Rather than stamping my fingers on the cards, through practice I've managed to make it look natural, and I can mark the pigments using only a light brush. My enhanced dexterity is really convenient here. It would have taken a lot of practice to make it inconspicuous otherwise.

I decide to fold this particular hand and we move to the next round.

8d 4h. I mark it again, the NEET guy calls, and we move on to the flop. We check all the way to the river and I lose to a T in his hand.

The cards and the board demanifest, vanishing as if they were getting vacuumed into another dimension. Then two cards get spat out of the air to land right directly in front of me. The same happens for the NEET guy.

"Check." He takes a look at his hand and checks, looking at my reaction.

Ac 3d. On the button, I see that I got dealt a decent HU hand. During the couple of years I spent programming, I did have time to spend some of it playing against my agents, so I at least have the basics of various forms of poker down. As a player I am actually a lot worse than my own trained agents, but I can imitate them to a degree.

"Raise." Making sure to leave the marking on my hand, I pick out the 3 chips from my phantasmal pile of 736, and place them on the table and min-raise to 4.

"Call." The flop comes out next, the cards gently manifesting themselves on the table.

Ac Js 5s. The NEET guy checks, not hesitating, I put in a pot sized bet. He thinks for a bit and then folds.

Poker tends to be like that most of the time. Long periods of folding followed by brief bursts of intense action. It won't be long before the antes go up and become a significant part of our stack. At that point, the markings will play a decisive role. The quickly increasing antes are like the water level threatening to drown the players. The only way to stay above the water is to take the other players by the shoulder and lift yourself up.

Qc 6s...
3d 9d...
7s Jc...
2h 4h...
6d 6c...

The cards continue flowing, and I continue marking them. It won't be long until I have a decisive advantage against my opponent. HU situations really favor me, with Dale's group by the time I've finished marking the cards, the antes tend to have risen high. A lot of the time I've gotten put into a situation of having a good hand, but the interference from having too many players on the table caused the situation to go out of control. 1-on-1 you are never waiting for a good hand preflop, and the action is always flowing. This will maximize my edge.

(Geoffrey POV - Heaven's Key, House in the suburbs)

"Here you go." My host and friend, Walter, placed a cup of tea in front of me. Seated at a table, the sweet aroma from it wafted into my nose. It takes some skill to make exotic teas really come to life, the ones manifested using the system tend to get stale after a while. I take a sip. "The flavor of your tea is as good as ever."

"Thank you. I haven't seen you in a while Geoff. It must have been a few years. What have you been up to?"

"Just my work. Since I put in that request, I thought I'd come by and talk to you about it. I am curious who you sent after Euclid." The enforcement requests aren't that frequent of an occurrence, they usually happen one every few years on average. They are especially rare against newcomers who get passed into the true afterlife by the guides. Usually it is the citizens which get tired that start causing trouble.

Walter, a gray haired dandy like myself, tastes his own drink. After a bit he answers.

"You've met him a few times, I think. It was Louis." Louis, Louis...I remember him.

"Ah, I remember. He is the young man who came by a few times. Wasn't he just starting out his training?" I start to feel concern and show it on my face. "Are you sure about sending him out? Will he be fine?"

Walter looks at me for a bit, and laughs lightly at my expense. It seems my grasp on time must be more tenuous than I thought.

"Good one, Geoff. He finished his training over a 100 years ago. I think it was 150 years ago when I first introduced him to you." It is like thunder is running through me. I'll never not be shocked in situations such as these. I've lived in this city for a long time, and it seems it is true what they say about old people. Some of them can't remember yesterday, but can remember 20 years ago as if it were that.

"That is good to hear. What is his rank now?"

"Mid-Aleator." Very few people have the talent to become Epistemes, and most of the Introspects in the city cannot reach even the level of an Aleator no matter how hard they try. I myself couldn't become an Episteme. I remember being arrogant in my youth, but I realized that talent is something beyond people's control eventually. That was a long time ago. Now I can accept myself, and other people as they come.

"I suppose there is nothing to worry about against a newcomer then." I enjoyed my tea. The most important thing in life is to flow along. Even if you don't have talent, you can still live, and if real trouble arises, the Epistemes will take care of it. I used to think it was a tragedy that my desire could only get me so far, but then I turned around and realized that it would be hell if everyone were allowed to rise. If everyone had the talent of an Episteme, this world would long have ended. I used to hear stories about how the city was at the beginning, and am glad I wasn't there to witness it.

"If you don't mind telling me Walter, what is his speciality?" I inquired.

"Are you curious?" He teased me, raising his eyebrow.

"Of course." I smiled.

"His eyes. It took him 30 years, but he managed to improve his vision to a level where a reflection in another person's pupil is as good to him as we see regularly." Peering Walter's gray pupils as he said that, I could see a light reflection of myself.

(Heaven's Key, Shadow realm, Resolution duel with Louis)

Ghhhh...

The blinds have doubled twice and I've marked most of the cards, but I am not winning. I've started the game at 750, but since then I've fallen to 520.

The button comes over to me, and I get dealt my cards. I do not even have to look at them to know what they are Kc Qh, a good preflop hand heads-up. On the other side I see that he got Ks 2d. If I could get a king pair, I could take some of my losses back.

"Check."
"Raise." I min-raise to 16, he calls and we get taken to the flop. I hope that a king comes out there.

3s 5c Kd.

"Check." The NEET guy checks after thinking about it for a bit. It wouldn't be unusual for a player to bet anywhere between half a pot to a pot here. His hand is pretty strong, but it seems he is slow playing it for some reason. In that case I'll do it.

"Raise." I bet 16 chips, half a pot. I am keeping a poker face, but I expect he would at least call here. This bet is not unusual for me, I usually put in this much on both bluffs and value bets.

"Fold." What the hell? That was such a good setup, I should have won at least 50 chips on this hand. How is it possible that he folded this? Usually he plays like a calling station, just waiting for me to put money in. Most of my losses so far came from trying to bluff him out of a low pair. Why is he folding a high pair?

I've been looking at him this whole time, it doesn't seem like he is doing any kind of marking.

> Hey, what is my mental state? Is it possible that I am giving out some kind of tell? This fold was too good.

I ask the controller. It is his responsibility to take care of this.

> No, you are fine. You are a bit frustrated at being down so much, but I've been keeping hold of your facial expressions and body language. Absolutely nothing should be showing up.

I can't do anything but trust him. If he got it wrong, I am prepared to die here, but otherwise I'll reason as if nothing is wrong on my face.

The next couple of hands proceed as usual. The chips clank as they are moved around, and each of us folds to some light bets after missing the board. The blinds double from 4/8 to 8/16. I can already feel my entire stack being at risk. While at the start I was over 350bb deep, right now I have only 32bb to bet. If the blinds keep doubling, in a couple of revolutions, winning a hand will become a pure coin flip.

A new round starts. I am on the button and get dealt Ts Th. I look at what he has and see him holding 6c 6d. This is really good, my hand is dominating his. If we went all in preflop I'd be 80% favorite to win.

"Check."

In response, I min-raised him to 32. He calls.

6s Tc Td.

...Holy shit. I admit, if I'd been playing as a normal human, I'd have definitely given off a tell in this situation. I'd have straight up jumped out of my seat. Instead, I experience the expert work of the controller, and keep it perfectly cool at this huge stroke of luck in a death match.

I have quads, while he has a full house. Unless he can really see what I have, there is no way he can avoid going all in here.

"Check." I honestly feel annoyed that is slowplaying this particular hand.

"Raise." I bet 32 chips into a pot of 64.

"Fold." He just throws his hand away like it was trash.

Shivers run through me, and it feels like somebody splashed a bucket of cool water over me. I feel ants crawling up my spine.

It seems my dumb cheating method will not work. I am going to die.

(Geoffrey POV - Heaven's Key, House in the suburbs)

"So Geoff, you've played with the kid. What is he like?" Walter asks me.

"He is very talented, probably a genius." I remark. "But a genius without experience is still just an ordinary person here. For example..."

To make my point, I manifest a deck of cards and place them on the table. I pick one of the cards and place it next to the deck. Then with one of my fingers pointed, drag it along the surface of the card making a red mark across its back.

"Introspects can't do anything, but once they figure out how flexible their being is, they start to think up ways to cheat. Of course, the very first thing they do is mark cards in various ways." I say to Walter. "I remember when I came here, I couldn't really manifest the pigment directly so I took to manifesting cans directly on my person because it was easier. And I had these UV shades..."

I manifest a pair of slick shades and put them on, grinning.

"Heh heh heh, I did that as well." Walter remarked.

"The next day I'd get called out as it was quite obvious. I'd be reaching into my pocket every once in a while when the UV paint dried on my fingertips, and everyone could see it."

"It is better to just manifest the pigment on your hands directly."

"Yeah, the low level Aleators quickly figure out how to do that. This kind of cheating is a lot more reliable. You can go a bit far in private games that way until the rest wise up."

"In the Heaven's Key tournament it doesn't matter if the others know if you are cheating or not. Even just being a low level Aleator is enough to survive on your own without the loss of chips. To get into the money you just need to survive the first round, and these kinds of methods are more than good enough. The trouble for Introspects is that even if they know how to cheat, they have no way of bringing it into the dueling space. They can only train their skills the regular way."

I nod to him.

"Yes. The next level is to start transmuting your body in order to enhance it. Instead of wearing shades, you change your eyeballs so they can see UV. That is much less obvious."

"And Euclid is at that level?" Walter asked.

"Yes, but he is not as good as Louis."

"You said in your report he is a newcomer. Are you sure? Because being able to do this in your first week is unheard of. Maybe I should have sent somebody better, but it was time for Louis to take on some actual work rather than just training."

"Yeah, definitely. And because he is a newcomer, Louis will be able to win because of that." I reassured him. "It is not just because of the eyes. Euclid is relying on marks to cheat, and such marks.."

I point at the card. Whereas before I dragged my finger across it to paint a mark, this time I just do it across the air without coming close to the card. Like casting a spell, the red mark I made on the card disappears.

"...can be erased. Mid ranked Aleators also do not need to rely on their body directly to cheat." I do a swish in the air with my finger and the mark gets painted across the card again.

I look outside the window and note the time. The sun had set, and according to the reply the enforcer is supposed to challenge Euclid at this time.

"Right now Euclid should be sweating..."

(Heaven's Key, Shadow realm, Resolution duel with Louis)

For the first time, my opponent makes a reaction. I see his lips curve into a slight grin.

He can see into my hand. Absolutely. I look at my cards and note the marks I put on them myself. It might be because of this. I could get rid of them, but then I wouldn't be able to know what cards my opponent has himself. While I was thinking along that direction, out of the corner of my eye I spy some movement. My opponent twirls one of his fingers, and my two cards become covered in a layer of UV paint. The marks I have put on are completely overpainted and rubbing my fingers against it, I realize that the paint is fully dried. I can't clean it off.

I look at my opponent and I see that on his side, he did the same thing as well. The marks on his cards are unreadable.

I realize what this means. He is not going to let me use the UV painting method anymore. In future hands, I will be flying blind.

The feeling that doom is nearing comes to me. Right now, I feel a tangible sense of threat from my opponent. He is on a completely different level than Lily and Dale's group.

(Geoffrey POV - Heaven's Key, House in the suburbs)

"So the kid will definitely lose..." Walter remarked. "Well, it is too bad for him." He immerses himself in tea.

Something in his comment stirs something in me, and I start thinking about it.

"Well, it is not absolute. Since he isn’t a citizen we haven’t had the chance to watch him for a long time. There is a very small chance that I've misjudged Euclid, and he has the latent abilities of an Episteme. Unlike the Introspects who have known talents, he is a newcomer. I only played with him for a few days and didn't have enough time to judge him fully."

"Hmmm..." Walter raises his eyebrows at me, doubting me.

"I am just speculating how Euclid could win. Don't tell Louis about it afterwards." I urged him.

"I won't. So how could it go?"

"Have you ever played against an Episteme?"

"I've been placed at their table plenty of times in the Heaven's Tournament. It ends up as a slaughter. At that level you can't call the game poker anymore. It is more like fighting a wizard casting spells at you."

"I once went up against Gray one-on-one." I admitted. I didn't need to explain who Gray was. All the Epistemes were famous throughout the city.

"Really? What happened?"

"Gray loves using the trick of pulling out a gun and firing it at his opponent." I pause as I recall how it went.

"Did he shoot you?" Walter asked.

"He shot at me for about half an hour straight."

"That's nasty." Walter grimace. I recall the match.

"There I was at the table, trying to disbelieve the bullets so they don't hit me otherwise they will knock me out. Sweat is pouring down my face and I can't even look at my hand due to intense concentration required. I haven't played a single hand the entire time, instead the system folded me automatically every 5 minutes. Gray himself had no trouble making raises."

"So he shot you in the end." I nod.

"Eventually I got tired and one of the bullets came through. At that point I blanked out and when I woke up it was in a hospital room. Thankfully it was not a resolution match, but a regular duel otherwise I would have gotten killed."

"I see."

"That is how Euclid could win even if he was outclassed if he really is an Episteme." I pointed a finger gun at Walter. "Just manifest some kind of weapon and blast away until the other side crumbles. The way Gray did. It doesn't require too much skill or grace assuming he knows how to make a working gun and has the sheer ability needed to manifest it."

"..." Walter looks at me in silence.

"The most horrifying thing for an Aleator is to go into a resolution match against what he thinks is a lower rank, only to have it turn out he is facing an Episteme."

(Heaven's Key, Shadow realm, Resolution duel with Louis)

I won't give up with just this. Let me bring out all my aces in the hole. We'll go all out!

> Let's try the gun. Just like the white hair guy did.

I message the controller, and feel my senses start to change.

I raise my hand and per my will, a polished, gray revolver manifests in it. I open the magazine, and with a mental trigger manifest a clip of 6 yellow bullets before inserting them into the slots. I point the gun at my opponent and on his face, I see a sign of visible alarm.

Bang!

I blast the bullet directly down the middle of his forehead. My mind is fast, so I can see the bullet in strong slow motion as it travels its path to where I intended it. But as soon as it came close to touching his skin, rather than piercing, the bullet instead disappeared. If I were a human, at this point I might have simply concluded that I missed, but I could see every single inch the bullet traversed, so I am sure there is no chance of that.

Bang! Bang! Bang! Bang! Bang!

Not having anything better to do, I empty the rest of the magazine into the guy, but the results are the same. I am not sure whether to stop or to continue with this, but as I look at the terror on the face of my opponent, it induces me to do more of it. I open the magazine, let the spent casing fall out, manifest another clip in my hand and reload the gun.

Bang! Bang! Bang! Bang! Bang! Bang!

Nothing happens, but my enemy is afraid so I continue doing it.

Bang! Bang! Bang! Bang! Bang! Bang!

Reload.

Bang! Bang! Bang! Bang! Bang! Bang!

Reload. Like so the silence at the table is punctuated by a constant barrage of gunshots.

I continue repeating that for a few minutes, but nothing is happening. And while I gave him a great scare at the start, he catches his bearings and calms down.

The look on his face is pretty cool now.

I could do this for as long as necessary, but it doesn't seem shooting my opponent is doing me any good here. I guess it is how in RPGs the bosses are immune to sleep and paralysis effects, anything that would kill them outright on a failed roll. I am guessing he has some technique that renders him immune to this cheap method of winning.

Plus, going further with this method will do me no good in real life. The same goes for saveloading.

I toss away the revolver into the abyss below, not taking my eyes away from my target. I carefully note my opponent's reaction and if he is feeling relieved to see me do that, he is good at hiding it. I won't work after all.

> It won't work. The guy is as cool as in a freezer now. He got used to it.

I message the controller.

> We'll go to the next stage of enhancing our senses. We made this during the night, and we'll put it to use now. Here is the Enhanced Biological Eye.

I feel my vision start to warp and take off my glasses. Since I won't be needing them I treat the same as the revolver and dump them into the abyss. I blink a bit as I become disoriented due to the barrage of information coming from my eyes, but I quickly adjust and the world comes into focus. When I look at my opponent's face now, I see every little pore on his face. It really magnifies his ugliness. But instead of focusing on that I focus on his beady, pig eyes and see my own reflection in them.

"Check." Since it is my turn, I take a look at my hand before checking and wait for my opponent's response. He min raises, and I fold my trash hand.

The next round starts and we both get dealt new hands.

For a few moments it feels like we are in a standoff, each waiting for the other to check his hand first. Making no movement, I wait for him to start and he yields, seeing no reason to delay further. Each of us can only check their own cards or the opponent's so it does not matter which one of us does it first. Only in the case that we both do it at the same time, we won't get any information.

He does so, and reflected in his eyes, I see his hand.

Ah Kh. A premium hand.

He raises off the button to 24. I take a look at my hand and then chuck it without needing to think about it much.

Last night, me and the controller worked on a new eye model. We took the eagle as reference, and then had an evolutionary algorithm optimize the cross between it and the human eye. With my newly improved eye, I'd have no trouble spotting a mouse far in the distance from the top of a mountain. Or a slight reflection of the cards in my opponent's eye.

But at this point at best, I've closed the gap with him.

In order to win, I need to deny him the advantage of looking at my own hand, assuming that is what he is doing.

Last night after we'd finished designing the eye, we thought that we might run into an opponent trying to take advantage of lens reflectivity, so we did an anti-reflective version as well.

> It works. Make the pupil anti-reflective next.

I don't detect any changes to my vision, but I get a message saying it has been done.

The NEET assassin looks at his hand, I see it as trash Js 5c in his eye's reflection. He finishes his peek and turns to observe my reaction. It is a request to which I oblige. 2c 3c. The hand itself is worthless in this HU situation, but the look on his face after I finish is priceless. Whereas he was merely scared when I started to shoot at him, right now he is slack jawed open.

Now it is my turn to grin. This is quite satisfying, more than just moving chips around after winning a hand, this moment is when I truly experience victory.

Are you wondering what my hand is? Well, keep wondering!

I haven't tried out all of my trump cards, so I am looking forward to it. I appreciate this guy as an adversary. Though the white guy is tougher, I wouldn't have gained as much fighting him.

As I start to wonder what he is going to do next, my bet is on him manifesting some anti-reflecting shades to equalize the field. I had a response planned for that and was looking forward to trying it out, as that particular method is the one I intend to use in the real world.

Somehow what he did next should have been entirely obvious, but it came completely as a surprise to me anyway.

(Geoffrey POV - Heaven's Key, House in the suburbs)

"So if Euclid is an Episteme, would Louis have any chance to win?" Walter queried.

"No, I don't think so. But it doesn't mean that he necessarily has to lose even against a superior opponent. We carefully note down how many chips the newcomers have won for a reason. As long as he has more than the opponent, he can put pressure on him and seek to break up the match. It is putting game theory into practice."

(Heaven's Key, Shadow realm, Resolution duel with Louis)

"All in!" My exuberant mood was immediately dampened once my opponent did this.

Oh, no.

"Fold." He had J5, and I had 23, so he was 62.5% sure to win if I called him here. The fold was easy. But...

"All-in." He didn't even bother looking at what his hand was. Instead he manifested and pushed in his entire stack. And for the first time, I could see exactly how many chips he had. The game itself was aiding my ability to detect the chip amount, so I could tell that he had exactly 5322. He started at 5000 exactly, and took 322 from me along the way, and now I was at 418. It was a great pile that dwarfed my tiny stack. I'd have to win 3 times in a row just to get to a safe position. If I lost, I'd die. But he on the hand, if he lost would just lose some chips. It is not a big deal to him.

In this realm of shadows, that golden pile glimmered with a radiance, representing absolute power.

I looked at my hand, and saw that I had Qh Qc. If I was playing poker in the real world rather than a game, this would be a very easy call. But even if he had something like 36 or J5, any two lower than the queens, I'd still only be 80% certain to win. In other words, I have a 20% chance of dying. And now that this is an outcome, I realize that the chip amounts do not matter.

What is going to happen next...

"You are too much for me, champ. You are really good." My adversary buttered me up. "Let's stop the match here."

"..." I pondered his words intently.

"You've managed to get 300 chips from Dale's group. And with your skills you don't have anything to fear from the Heaven's Key tournament."

"..."

"From here on out, I'll be shoving blind. If you wait for an opportunity you can make the call where you are 70% ahead. But that just means you are 30% likely to die. Risking your life on these all ins is not worth it." He was doing his best to keep a confident demeanor. "In order to take all of my chips, you'd need to win 4 all-ins. Even if you pick your spots and are 70% ahead on each hand, the odds of you doing that 4 times in a row is only 25%. Meaning, if you decide to face me here you are 75% likely to die."

"..." He is right. He is right, but even though I agree with him, why am I starting to feel livid? This feeling inside of me is pure rage.

"Do the right thing. As long as you hide and keep quiet, the other enforcers won't bother you."

I hate him for snatching my victory away from me, just as soon as I gained an advantage. In my mind, I keep going between thinking of these people as NPCs and real, but it is right now that I realize just how smart they really are. I should have all the advantages in this match and yet, I am the one being pressured now.

I hate him so much I could die!

That is how I feel right now. Like some beast, I feel like growing at him to show him just how much I hate him!

Maybe I am a fool. I haven't thought about this aspect of the game at all. Last night I was focusing on how to cheat. I spent all that time designing eyes. I even came up with a design that I'll be able to use in the real world once I improve my nanofabrication skills. I can't replicate biological organs, but with the nanofog it would be possible to make nanomachine organs better that the biological ones.

That is my real goal. My goal is not actually to beat Heaven's Key, but to have it serve as a launching pad for beating the real world.

This is also the reason why I was not eager to challenge the white haired guy again. What point is there in fighting somebody who pulls out a gun at the table? That is not going to happen in a real world casino! I simply don't care about the advantages in the game that I cannot make use of in the real world.

This is why I am so disgusted at this situation. It is forcing me to care.

Suppose I do the rational thing, and we abort the match. I'll be able to get on with my life in this city. But they'll send somebody better than this guy who is capable of countering my current tricks. Then suppose I manage to gain an advantage. All-in! I imagine him doing just the same thing as my current opponent. I'll have to break up the match again, all for the sake of rationality. I'll really be an easy target to play against, an experimental pig for them to see how much it would take to break me. I'd get a never ending stream of opponents I can never beat as they pluck my chips away one by one.

In that case, wouldn't it be better to just die here, than having to endure living such a life?

[Gnosis check DC 2 Succeeded - Sampled 2.85]

Life is a paradox. The highest goal is to attain omnipotence, but if you care about your own life you can never accomplish it. I'll put my pride ahead of rationality and just die. I'd rather die like a lion than live like a mouse!

I check my hand and see that it is Ah 5d.

It is good enough. I'd call a random hand with this in the real world.

With a mental command I manifest my entire pile in the air above me. Then I smash it down on the table in front. As the chips land the table shakes in a satisfying manner, and peering into my opponent, I can see his eyes widen in fear. Yeah, this is what I want to see. Sweat you pig! Gazing at my opponent with undisguised bloodlust, I grab a few chips from the pile and play with them as I think.

I've already decided, I am going to fight until one of us dies.

As I gather the will to call, I start getting inspiration. Is it really necessary for me to die here? Have I really exhausted every possibility there is at this table?

I have some more abilities I haven't used, but those wouldn't help me at all in this situation. I have two problems:

* My opponent's cards are hidden. He is overpainting them as soon as they come out.
* The community cards which are going to come out on the table are hidden.

If I could break these two problems, I could win even in this scenario.

If I was a real Inspired, I'd have control over nanomachine clouds. I could control those tiny machines to sneak under the opponent's cards and read them out to me. As for the deck, who knows what I could do about it. Since the game transports me to a different place once the duel starts, most likely the cards are held in a different realm by the system and transported here. But since the markings get preserved, I can be sure that the cards aren't simply being manifested from thin air as needed. The deck definitely exists somewhere.

Still, controlling nanofogs like in the stories is far beyond me at the moment. I could exit the game here, and spend a few decades training myself in this, but who is going to put this amount of effort just to beat this game. It is not worth it. What is the point of playing a game if you need to be max level at the start? That is more like real life.

If I am going to win, it has to be with my current abilities.

Do I have any possibility of doing that? I don't but...I suddenly recall what my opponent did. A little while ago he waved his finger and erased the marks on my side of the table.

...How did he do that? I didn't really care about that until now, but now I am suspicious of that.

Nanomachines? Of course not, there is no way a human would ever have the ability to control something of that sophistication.

Rather...I start to think about the cards. When they are dealt, it is not like they materialize right where they are. Instead, it is like there is an invisible dealer at the table...No, not like that. If there was an actual person the trajectory of the cards would not be like that. Rather, it is like there is an invisible vacuum at the table.

I visualize that sort of household appliance. But if i…

---
## [ciulinuwu/cosmic-cat](https://github.com/ciulinuwu/cosmic-cat)@[caa608b19e...](https://github.com/ciulinuwu/cosmic-cat/commit/caa608b19efdcc62261bf2dcbc7353d193103309)
#### Friday 2022-09-09 17:19:10 by ciulinuwu

fuck you tampermonkey export

Signed-off-by: ciulinuwu <79811506+ciulinuwu@users.noreply.github.com>

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[1336fda5e1...](https://github.com/pytorch/pytorch/commit/1336fda5e184605e8a18109ab2115096a41c1f36)
#### Friday 2022-09-09 17:25:46 by Andrew Gu

Update base for Update on "[FSDP] Generalize prefetching; lower unshard/reshard to handle"


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

[ghstack-poisoned]

---
## [lydia-duncan/chapel](https://github.com/lydia-duncan/chapel)@[1b5d5a5140...](https://github.com/lydia-duncan/chapel/commit/1b5d5a5140309b41f569904e73fb9974afcae5b5)
#### Friday 2022-09-09 18:00:13 by Brad Chamberlain

Merge pull request #20616 from bradcray/range-docs-tidying

Tidy up range docs

[reviewed by @bmcdonald3 — thanks!]

While reviewing my the range docs after my changes to its behavior
last night, I found some pre-existing bugs that needed fixing,
that the operators were now being generated by chpldoc, and some
other opportunities for cleanup.  Summarizing, they were:

* the expected output from the alignedLow/High docs wasn't printing
  (and hadn't been in previous releases either)

* the signatures on the param/type queries in the spec used illegal
  syntax (though now they fall prey to the poor spacing when
  rendered by Sphinx on Chrome.

* I squashed the chpldocumentation of the operators because they're
  already described in the text of the spec, which does a better job
  of it.  That said, going forward, I think we'd like to find a way to
  integrate operator signatures into these sections of the spec so
  that people can see what the overloads are.  Not today's task though.

* I tried to clarify some wordings and descriptions.

* removed the "more descriptive" clause that I'd applied to the
  alignedLow/High queries yesterday because it sounded like more of
  a value judgement or preference than I'd intended.

* I more uniformly set ``true`` and ``false`` off using code
  formatting.

* I more uniformly started entries with "Returns" rather than "Return"

* I more uniformly ended descriptions with periods

---
## [izaitsevfb/pytorch](https://github.com/izaitsevfb/pytorch)@[4c8cfb57aa...](https://github.com/izaitsevfb/pytorch/commit/4c8cfb57aa3ac58112efb693635198b07edf008f)
#### Friday 2022-09-09 18:22:02 by Edward Z. Yang

Convert SymInt tracing to mode based tracing (#83380)

We're on our way to deleting ProxyTensor entirely (see https://github.com/pytorch/pytorch/pull/83330 ), but before we can do that, we have to delete ProxySymInt first. Here's the plan.

Changes in torch.fx.experimental.symbolic_shapes

* The general idea is to do mode based tracing. This means we need a mode that can interpose on all SymInt operations. There are a few ways to do this, but I've done it the easy way: (1) I have a separate mode for SymInt operations specifically called SymDispatchMode, and (2) this mode operates on PySymInt (and not the basic SymInt which is user visible). I elided Int from the name because if we add SymFloats I want to use the same mode to handle those as well, and I used Dispatch rather than Function because this is the "inner" dispatch operating PySymInt and not SymInt (this is not a perfect analogy, but SymFunctionMode definitely seemed wrong as you still must go through the C++ binding.) The mode is entirely implemented in Python for ease of implementation. We could have implemented this more symmetrically to TorchFunctionMode in C++, but I leave that as later work; this API is unlikely to get used by others (unlike TorchFunctionMode). One downside to not doing the mode in C++ is that we still have to do the hop via a preexisting PySymInt to wrap; this is currently not a big deal as conversion to SymInts only really happens when there is already another SymInt floating around. SymDispatchMode is pared down from TorchDispatchMode; there is no ancestor tracking since I don't expect people to be mixing up SymDispatchModes.
*  I made some improvements for tracing. When I invoke the SymDispatchMode handler, I would like constants to show up as constants, so they can be directly inlined into the FX graph (rather than going through a wrapping process first, and then the wrapped SymInt being used in the operation). To do this, I directly track if a PySymInt is a constant at construction time. Only wrapped PySymInts are constants.
* For convenience, PySymInts now support all magic methods that regular SymInts do. This is so that redispatch inside the SymDispatchMode can be written the idiomatic way `func(*args, **kwargs)` where func is an operator. The original names are retained for direct C++ calls.

Changes in torch.fx.experimental.proxy_tensor

* OK, so we got a new SymDispatchMode, so we define a ProxySymDispatchMode and activate it when we start tracing. This mode is currently unconditionally activated although technically we only need to activate it when doing symbolic tracing (it doesn't matter either way as there are no SymInts if you are not doing symbolic tracing).
* We delete ProxySymInt. To do this, we must now record the proxy for the SymInt some other way. Based on discussion with Chillee, it is more intuitive to him if the proxies are still recorded on the SymInt in some way. So we store them in the `__dict__` of the PySymInt, indexed by Tracer. An improvement is to make this a weak map, so that we remove all of these entries when the tracer dies. In an original version of this PR, I keyed on the mode itself, but tracer is better as it is accessible from both modes (and as you will see, we will need to fetch the map from both the ProxySymDispatchMode as well as the ProxyTorchDispatchMode.) The implementation of SymDispatchMode now simply retrieves the proxies, performs the underlying operation as well as the FX graph recording, and then records the output proxy to the PySymInt. Note that FX tracing does not work with proxies and SymInts, so we manually call `call_function` to ensure that the correct operations get recorded to the graph. This means conventional FX retracing with proxies only will not work with these graphs, but there wasn't really any reason to do this (as opposed to `make_fx` retracing) anyway. Constants are detected and converted directly into Python integers.
* SymInts can show up as arguments to tensor operations, so they must be accounted for in ProxyTorchDispatchMode as well. This is done by searching for SymInt arguments and converting them into proxies before the proxy call. This can be done more efficiently in a single `tree_map` but I'm lazy. The helper `unwrap_symint_proxy` conveniently implements the unwrapping in one place given a tracer; unfortunately it cannot be shared with SymDispatchMode as SymDispatchMode gets PySymInts, but ProxyTensorMode gets SymInts. Similarly, tensors that are returned from tensor operations can have SymInts in their shapes, which need fresh proxies allocated. To avoid leaking internal details of SymInt shape computation to the tensor operation graph, these SymInts are always given proxies derived from `x.size(dim)` call on their return tensor. We also need to do this for strides and numel but have not done so yet. Furthermore, we must avoid tracing internal SymInt calls while we run meta operations on the true operation; this is achieved by also disabling SymInt tracing on the inside of tensor tracing. This is analogous to how tensor tracing is disabled inside the implementation of tracing mode, but unfortunately we are unable to use the same mechanism (this would have been easier if the two modes could be combined somehow, and I am amenable to suggestions to try harder to achieve this.)
* Because there are no more ProxySymInts, we no longer need to do anything to unwrap SymInt. Furthermore, we do not need to reallocate ProxySymInts on class creation.
* If a bare SymInt without a Proxy is encountered, it is assumed that this must be a constant. `create_arg` handles this case. Non-constant free SymInts result in an assert error.
* The initial input handling in `dispatch_trace` involves traversing all of the input tensors, traversing over their shapes, and assigning proxies for the SymInts in shapes in the same way we handle proxies for the output tensors.

The preexisting testing is inadequate but will be better after I rebase past https://github.com/pytorch/pytorch/pull/82209

Signed-off-by: Edward Z. Yang <ezyang@fb.com>
Pull Request resolved: https://github.com/pytorch/pytorch/pull/83380
Approved by: https://github.com/samdow

---
## [sthagen/postgres-postgres](https://github.com/sthagen/postgres-postgres)@[7fed801135...](https://github.com/sthagen/postgres-postgres/commit/7fed801135bae14d63b11ee4a10f6083767046d8)
#### Friday 2022-09-09 18:33:46 by Tom Lane

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
## [digitalservicebund/ris-backend-service](https://github.com/digitalservicebund/ris-backend-service)@[67af6e26c7...](https://github.com/digitalservicebund/ris-backend-service/commit/67af6e26c7b4d1ab7ae68f9003d4666eddbba66b)
#### Friday 2022-09-09 19:16:44 by Thore Strassburg

Feat(web): introduce typed input field approach

The `InputGroup` component allows to specify a list of inputs that
should be rendered and mound their model values to an object. So far
this only works for text inputs (using the `TextInput` component). The
goal is to make this more flexible and allow also other types of inputs.

To support this higher level goal, a generic `InputElement` component
has been added. The idea of this component is to act like the standard
HTML `<input />` component, but use our custom input components. Thereby
it receives the attribute `type` (as `<input />` does). This property
defines which actual input component will be rendered. In forwards the
model value bound to itself to the input component. Furthermore it can
receive any further attributes for the specific input which it will bind
to the component instance.
These two properties, the type and the input specific attributes are now
part of the definition of an input field. Thereby the `InputGroup` can
simply instantiate the `InputElement`.

To support this "generic" feature with more typing constraints, several
interfaces and types have been defined. As these types are part of the
higher level concept, they are part of the `domain`. This concept of
having objects with editable (or not) properties of different kind and
the rendering into forms, is independent of the actual visual frontend
implementation. It is not Vue specific and would still be valid and
working if we would switch to React or Angular.
The types are quite straight forward in an extending manner. One of the
first and strongest benefits is, that it allows us to type-check our
field definitions. These have been split into separate TypeScript files
to keep them more organized and, more importantly, being typed. The type
interference is so smart, once a field defines the requires `type`
property TypeScript will check the whole field definition if it is
compatible, has missing properties, correct property types etc.
Furthermore do this types used in the Vue components which implement
this higher level concept. The components do no more define these types
locally in a top-down-dependency manner. Rather we have a dependency
inversion to the domain now.

Unfortunately is Vue not (yet) powerful to support fully generic
components. And even to the degree it is possible, it is
a hack/workaround that leads to ugly code that is still not fully
generic. In result it is currently not possible to provide 100% type
safeness. It is not (yet) possible to tell the `InputElement` that if
`type` is of a specific enumeration entry, the `modelValue` must be of
a specific type. E.g. for a text type, the value is a string. But for
a checkbox a boolean. The same goes for the input related attributes.
Nevertheless the typing got restricted to some degree. Further
improvements planned as soon as possible. After all, even with the old
feature set only, the typing it stronger than before.

Please note that the current file-directory-structure under `domain/`
is still quite chaotic. But it was so too before. What the "domain"
actually is for the front-end, still has to be defined completely.
Therefore the most simple and flat approach has been chosen. Anyway,
an `index.ts` is used now to represent the `domain` more as a complete
module rather than individual parts. Other parts of the code base should
not know about the internal details.

After of all, this commit is too big and should have been split at least
into two. My apologizes for this mistake.

RISDEV-311

---
## [gmlueck/llvm](https://github.com/gmlueck/llvm)@[15f3cd6bfc...](https://github.com/gmlueck/llvm/commit/15f3cd6bfc670ba6106184a903eb04be059e5977)
#### Friday 2022-09-09 19:48:23 by Matheus Izvekov

[clang] Implement ElaboratedType sugaring for types written bare

Without this patch, clang will not wrap in an ElaboratedType node types written
without a keyword and nested name qualifier, which goes against the intent that
we should produce an AST which retains enough details to recover how things are
written.

The lack of this sugar is incompatible with the intent of the type printer
default policy, which is to print types as written, but to fall back and print
them fully qualified when they are desugared.

An ElaboratedTypeLoc without keyword / NNS uses no storage by itself, but still
requires pointer alignment due to pre-existing bug in the TypeLoc buffer
handling.

---

Troubleshooting list to deal with any breakage seen with this patch:

1) The most likely effect one would see by this patch is a change in how
   a type is printed. The type printer will, by design and default,
   print types as written. There are customization options there, but
   not that many, and they mainly apply to how to print a type that we
   somehow failed to track how it was written. This patch fixes a
   problem where we failed to distinguish between a type
   that was written without any elaborated-type qualifiers,
   such as a 'struct'/'class' tags and name spacifiers such as 'std::',
   and one that has been stripped of any 'metadata' that identifies such,
   the so called canonical types.
   Example:
   ```
   namespace foo {
     struct A {};
     A a;
   };
   ```
   If one were to print the type of `foo::a`, prior to this patch, this
   would result in `foo::A`. This is how the type printer would have,
   by default, printed the canonical type of A as well.
   As soon as you add any name qualifiers to A, the type printer would
   suddenly start accurately printing the type as written. This patch
   will make it print it accurately even when written without
   qualifiers, so we will just print `A` for the initial example, as
   the user did not really write that `foo::` namespace qualifier.

2) This patch could expose a bug in some AST matcher. Matching types
   is harder to get right when there is sugar involved. For example,
   if you want to match a type against being a pointer to some type A,
   then you have to account for getting a type that is sugar for a
   pointer to A, or being a pointer to sugar to A, or both! Usually
   you would get the second part wrong, and this would work for a
   very simple test where you don't use any name qualifiers, but
   you would discover is broken when you do. The usual fix is to
   either use the matcher which strips sugar, which is annoying
   to use as for example if you match an N level pointer, you have
   to put N+1 such matchers in there, beginning to end and between
   all those levels. But in a lot of cases, if the property you want
   to match is present in the canonical type, it's easier and faster
   to just match on that... This goes with what is said in 1), if
   you want to match against the name of a type, and you want
   the name string to be something stable, perhaps matching on
   the name of the canonical type is the better choice.

3) This patch could expose a bug in how you get the source range of some
   TypeLoc. For some reason, a lot of code is using getLocalSourceRange(),
   which only looks at the given TypeLoc node. This patch introduces a new,
   and more common TypeLoc node which contains no source locations on itself.
   This is not an inovation here, and some other, more rare TypeLoc nodes could
   also have this property, but if you use getLocalSourceRange on them, it's not
   going to return any valid locations, because it doesn't have any. The right fix
   here is to always use getSourceRange() or getBeginLoc/getEndLoc which will dive
   into the inner TypeLoc to get the source range if it doesn't find it on the
   top level one. You can use getLocalSourceRange if you are really into
   micro-optimizations and you have some outside knowledge that the TypeLocs you are
   dealing with will always include some source location.

4) Exposed a bug somewhere in the use of the normal clang type class API, where you
   have some type, you want to see if that type is some particular kind, you try a
   `dyn_cast` such as `dyn_cast<TypedefType>` and that fails because now you have an
   ElaboratedType which has a TypeDefType inside of it, which is what you wanted to match.
   Again, like 2), this would usually have been tested poorly with some simple tests with
   no qualifications, and would have been broken had there been any other kind of type sugar,
   be it an ElaboratedType or a TemplateSpecializationType or a SubstTemplateParmType.
   The usual fix here is to use `getAs` instead of `dyn_cast`, which will look deeper
   into the type. Or use `getAsAdjusted` when dealing with TypeLocs.
   For some reason the API is inconsistent there and on TypeLocs getAs behaves like a dyn_cast.

5) It could be a bug in this patch perhaps.

Let me know if you need any help!

Signed-off-by: Matheus Izvekov <mizvekov@gmail.com>

Differential Revision: https://reviews.llvm.org/D112374

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[bf85776f16...](https://github.com/NetBSD/pkgsrc/commit/bf85776f16b06872af12fd6adfb9d10120ff2266)
#### Friday 2022-09-09 20:12:20 by wiz

mame: update to 0.247.

With a change of season just around the corner, it's time to unveil
MAME 0.247! This is a huge release, and should have something for
everyone!

Newly added systems, and systems promoted to working, include:

    The M&D Monon Color - a low-cost Chinese hand-held console.
    This required finding an exploit to extract the CPU's internal
    ROM as audio. Said CPU is a high-performance derivative of
    Intel's MCS-51 architecture.
    A prototype version of Tecmoâs Super Pinball Action that used
    separate screens for the simulated backglass and playfield.
    This version was presumably poorly received due to the need
    for an expensive dedicated cabinet.
    An initial driver for second-generation Sony NEWS workstations
    based on MIPS processors. This one has been a long time coming,
    with a lot of preparatory work, but it's finally here!
    The Dracula and Game Pachinko - two Tsukuda hand-held games
    with vacuum fluorescent displays.
    Micom Mahjong - an example of an early CPU-based TV game, and
    possibly the first dedicated electronic mahjong system.
    Three new Casio synthesisers.
    Several Impera Magic Card games. This one's also been a while
    coming, requiring several new devices to be emulated.
    A few Astro Corp. gambling games, including Dino Dino, Magic
    Bomb, Stone Age, and Zoo.
    Some previously missing NO CD versions of Capcom's Red Earth.

You'll also find numerous bug fixes and emulation improvements
across the board. There's better support for low-cost Macintosh
models based on the V8 chipset (including the LC, LC II, and Classic
II). There are quite a few fixes for issues with Nintendo's
NES/Famicom-derived arcade systems, the VS. System and PlayChoice-10.
Several ZX Spectrum derivatives from the Eastern Bloc are in better
shape. The Atari POKEY sounds better. The PC Engine pachinko
controller from Coconuts Japan is now supported. Thereâs also an
important fix for extracting CHD CD-ROM images.

The stream of prototype cartridges is still flowing, with a number
of Atari 2600, Game Boy Color, NES, and Super NES additions landing
this month. Youâll also find the Scholastic Microzine disks for
Apple II, and several PC magazine cover disks. The new VGMPlay
music rips include music from the recently-emulated Poly-Net Warriors
arcade game.

---
## [ZilverBlade/Shard3D_Engine](https://github.com/ZilverBlade/Shard3D_Engine)@[9d2a8aa93f...](https://github.com/ZilverBlade/Shard3D_Engine/commit/9d2a8aa93f8ed4bed52fc48a6e4cae068c69dc1a)
#### Friday 2022-09-09 20:15:43 by ZilverBlade

got rid of garbage PCH because msvc keeps fucking it up and forcing me to recompile with single thread oh my god this is so much better

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[e7230e8b4a...](https://github.com/Paxilmaniac/Skyrat-tg/commit/e7230e8b4a6d60e1b6c025b52b9f3d2fc26577a5)
#### Friday 2022-09-09 20:16:10 by SkyratBot

[MIRROR] Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) [MDB IGNORE] (#16001)

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) (#69376)

About The Pull Request

Just to be clear, when I refer to time here, I am not talking about cpu time. I'm talking about real time.
This doesn't significantly reduce the amount of work we do, it just removes a lot of the waiting around we need to do for db calls to finish.

Adds queuing support to sql bans, so if an ongoing ban retrieval query is active any successive ban retrieval attempts will wait for the active query to finish

This uses the number/blocking_query_timeout config option, I hope it's still valid

This system will allow us to precache ban info, in parallel (or in batches)
With this, we can avoid needing to setup all uses of is_banned_from to support parallelization or eat the cost of in-series database requests

Clients who join after initialize will now build a ban cache automatically

Those who join before init is done will be gathered by a batch query sent by a new subsystem, SSban_cache.

This means that any post initalize uses of is_banned_from are worst case by NATURE parallel (since the request is already sent, and we're just waiting for the response)

This saves a lot of headache for implementers (users) of the proc, and saves ~0.9 second from roundstart setup for each client (on /tg/station)

There's a lot of in series is_banned_from calls in there, and this nukes them. This should bring down roundstart join times significantly.

It's hard to say exactly how much, since some cases generate the ban cache at other times.
At base tho, we save about 0.9 seconds of real time per client off doing this stuff in parallel.
Why It's Good For The Game

    When I use percentages I'm speaking about cost per player

I don't like how slow roundstart feels, this kills about 66% of that. the rest is a lot of misc things. About 11% (it's actually 16%) is general mob placing which is hard to optimize. 22% is manifest generation, most of which is GetFlatIcons which REALLY do not need to be holding up the main thread of execution.

An additional 1 second is constant cost from a db query we make to tell the server we exist, which can be made async to avoid holding the proc chain.

That's it. I'm bullying someone into working on the manifest issue, so that should just leave 16% of mob placing, which is really not that bad compared to what we have now.
Changelog

cl
code: The time between the round starting and the game like, actually starting has been reduced by 66%
refactor: I've slightly changed how ban caches are generated, admins please let me know if anything goes fuckey
server: I'm using the blocking_query_timeout config. Make sure it's up to date and all.
/cl

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [mdartmann/mkiss](https://github.com/mdartmann/mkiss)@[6f3bf3231d...](https://github.com/mdartmann/mkiss/commit/6f3bf3231d512a33d62b445e82da764dfe89f77a)
#### Friday 2022-09-09 21:37:54 by Mae Dartmann

libxslt: fix post-install and actually use /etc/xml/catalog

Why on God's green earth do so many projects rely on this piece of
garbage??? Docbook should have died 25 years ago, just like every other
bit of code that uses XML unironically. I'm looking at you, Microsoft.
Also, PLEASE DON'T INHERIT THE SYSCONFDIR FROM SOME RANDOM OTHER PACKAGE
IN YOUR DEPENDENCIES, FOR THE LOVE OF ALL THINGS HOLY!

Signed-off-by: Mae Dartmann <hello@maedartmann.name>

 Changes to be committed:
	modified:   core/gtk-doc/build
	new file:   core/gtk-doc/checksums
	new file:   core/gtk-doc/patches/0001-Partially-revert-a-gtk-doc-1.31-change-that-broke-e-.patch
	modified:   core/gtk-doc/sources
	modified:   core/gtk-doc/version
	modified:   core/libxml2/build
	modified:   core/libxml2/version
	modified:   core/libxslt/build
	new file:   core/libxslt/checksums
	new file:   core/libxslt/patches/0001-Make-generate-id-deterministic.patch
	modified:   core/libxslt/sources
	modified:   core/libxslt/version
	modified:   extra/docbook-xsl/post-install
	modified:   extra/docbook-xsl/version

---
## [oxidecomputer/opte](https://github.com/oxidecomputer/opte)@[971340deae...](https://github.com/oxidecomputer/opte/commit/971340deae27aa26a015a063fbf9c431f8e15e5e)
#### Friday 2022-09-09 21:40:40 by Ryan Zezeski

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
## [dsmith328/LC13Master](https://github.com/dsmith328/LC13Master)@[f0e6476eb0...](https://github.com/dsmith328/LC13Master/commit/f0e6476eb051d781f7e4d0be7976dff0ff72fda0)
#### Friday 2022-09-09 23:03:49 by Lance

The Great Workening

Attribute Levels Displayed

No thoughts were had, thoughts injected.

Attribute Levels go brrr

Requested Change Made

WHOOPS WRONG PARENTHESIS

I swear I know how Clamps work

Holy shit how did this not get found out earlier

---
## [Avenred/capsense](https://github.com/Avenred/capsense)@[e8fdb60aaa...](https://github.com/Avenred/capsense/commit/e8fdb60aaa6573f86ee157172d771bc3d51d3fad)
#### Friday 2022-09-09 23:29:58 by Avenred

fix the awful elif statements

oh my god just use an array holy crap this is so awful and terrible and awful and terrible

---
## [oxidecomputer/omicron](https://github.com/oxidecomputer/omicron)@[53c732aa97...](https://github.com/oxidecomputer/omicron/commit/53c732aa97f79e2ba494131660390de951227b40)
#### Friday 2022-09-09 23:46:28 by Andrew J. Stone

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

