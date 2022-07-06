## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-05](docs/good-messages/2022/2022-07-05.md)


1,775,913 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,775,913 were push events containing 2,594,093 commit messages that amount to 188,216,919 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [ImLonely13/kernel_xiaomi_mt6768](https://github.com/ImLonely13/kernel_xiaomi_mt6768)@[29d6c0b6fa...](https://github.com/ImLonely13/kernel_xiaomi_mt6768/commit/29d6c0b6fac265ff128034c47b159a8dd5eda64a)
#### Tuesday 2022-07-05 00:11:52 by Peter Zijlstra

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
Signed-off-by: ImLonely13 <gabutuhaku@gmail.com>

---
## [Cirrial/cirrstation](https://github.com/Cirrial/cirrstation)@[707fbfac7e...](https://github.com/Cirrial/cirrstation/commit/707fbfac7e11837865d70587011aa8197b1d0c35)
#### Tuesday 2022-07-05 00:39:46 by san7890

[MDB Ignore] Shifts all (sane) varedited signs to directionals  (#68004)

* [MDB Ignore] Shifts all (sane) varedited signs to directionals

Hey there,

So we have these cool new sign directionals now, but we still have all of the old pixel-shifted pre-fabrications lying around. So, I added an UpdatePaths (as well as Updated the Paths) to be a bit better at using directionals, because directionals are pretty neato.

This should update every single var_edit that used the proper 32 pixelshift (some of them used 28, and I'm unable to account for that automatically with current tooling) into a proper subtype. Mappers tend to learn by looking at well established maps, so it's always important to ensure that the well-established maps use the most recent tooling (i.e.: bring them up to the surface) and avoid needless excess lines in maps.

* The Commit With All The Maps

OH GOD OH FUCK

* Renames the UpdatePaths

---
## [Doctor-Derp/Foundation-19](https://github.com/Doctor-Derp/Foundation-19)@[a54b8e5040...](https://github.com/Doctor-Derp/Foundation-19/commit/a54b8e5040aab5f12f0cd7d21a46c0603b714e73)
#### Tuesday 2022-07-05 00:50:04 by Bierkraan

Eta-10 sprite fix, some smaller stuff too (#144)

* balance?

* add reactor startup manual, fix sprites for lockers of all kinds

* MTF See No Evil (not being used for now), no more alien MTF

* map fix, janitor uniform

* Eta-10 helmet works!

* fixed

* SM Crystal hotfix

* Remove supermatter, for real

* No more blood sucking artifact, sprite fix for Eta-10

---
## [slarew/linux](https://github.com/slarew/linux)@[4a557a5d1a...](https://github.com/slarew/linux/commit/4a557a5d1a6145ea586dc9b17a9b4e5190c9c017)
#### Tuesday 2022-07-05 00:56:22 by Linus Torvalds

sparse: introduce conditional lock acquire function attribute

The kernel tends to try to avoid conditional locking semantics because
it makes it harder to think about and statically check locking rules,
but we do have a few fundamental locking primitives that take locks
conditionally - most obviously the 'trylock' functions.

That has always been a problem for 'sparse' checking for locking
imbalance, and we've had a special '__cond_lock()' macro that we've used
to let sparse know how the locking works:

    # define __cond_lock(x,c)        ((c) ? ({ __acquire(x); 1; }) : 0)

so that you can then use this to tell sparse that (for example) the
spinlock trylock macro ends up acquiring the lock when it succeeds, but
not when it fails:

    #define raw_spin_trylock(lock)  __cond_lock(lock, _raw_spin_trylock(lock))

and then sparse can follow along the locking rules when you have code like

        if (!spin_trylock(&dentry->d_lock))
                return LRU_SKIP;
	.. sparse sees that the lock is held here..
        spin_unlock(&dentry->d_lock);

and sparse ends up happy about the lock contexts.

However, this '__cond_lock()' use does result in very ugly header files,
and requires you to basically wrap the real function with that macro
that uses '__cond_lock'.  Which has made PeterZ NAK things that try to
fix sparse warnings over the years [1].

To solve this, there is now a very experimental patch to sparse that
basically does the exact same thing as '__cond_lock()' did, but using a
function attribute instead.  That seems to make PeterZ happy [2].

Note that this does not replace existing use of '__cond_lock()', but
only exposes the new proposed attribute and uses it for the previously
unannotated 'refcount_dec_and_lock()' family of functions.

For existing sparse installations, this will make no difference (a
negative output context was ignored), but if you have the experimental
sparse patch it will make sparse now understand code that uses those
functions, the same way '__cond_lock()' makes sparse understand the very
similar 'atomic_dec_and_lock()' uses that have the old '__cond_lock()'
annotations.

Note that in some cases this will silence existing context imbalance
warnings.  But in other cases it may end up exposing new sparse warnings
for code that sparse just didn't see the locking for at all before.

This is a trial, in other words.  I'd expect that if it ends up being
successful, and new sparse releases end up having this new attribute,
we'll migrate the old-style '__cond_lock()' users to use the new-style
'__cond_acquires' function attribute.

The actual experimental sparse patch was posted in [3].

Link: https://lore.kernel.org/all/20130930134434.GC12926@twins.programming.kicks-ass.net/ [1]
Link: https://lore.kernel.org/all/Yr60tWxN4P568x3W@worktop.programming.kicks-ass.net/ [2]
Link: https://lore.kernel.org/all/CAHk-=wjZfO9hGqJ2_hGQG3U_XzSh9_XaXze=HgPdvJbgrvASfA@mail.gmail.com/ [3]
Acked-by: Peter Zijlstra <peterz@infradead.org>
Cc: Alexander Aring <aahringo@redhat.com>
Cc: Luc Van Oostenryck <luc.vanoostenryck@gmail.com>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [SpaceDjun/TheBigBigg](https://github.com/SpaceDjun/TheBigBigg)@[30224fb05c...](https://github.com/SpaceDjun/TheBigBigg/commit/30224fb05c9d7c75d944a24b14a263b9c9d3b78b)
#### Tuesday 2022-07-05 02:03:41 by kadva

I've been in this fuckin' room so long
My eyeballs are turning to dry wall
My friends suck, fuck 'em, I'm over 'em
"Hi y'all, y'all ain't hit me all day
What the fuck is the problem? Is it me?
Cause I'm not solved, I'm, bored."

---
## [Hurricos/realtek-poe](https://github.com/Hurricos/realtek-poe)@[8e13bf9bb2...](https://github.com/Hurricos/realtek-poe/commit/8e13bf9bb2cdbe6a0b36a4c62260d356a89e3235)
#### Tuesday 2022-07-05 02:17:16 by Alexandru Gagniuc

realtek-poe: Fix memory leak in poe_reply_consume()

When thinking "embedded", it's a good idea to stay the fuck away from
malloc(). Falling out of scope is a free garbage collector. Port
config and state arrays followed this advice, but for some reason, the
command queue did not.

No worries, free() is used in poe_reply_consume(). No problemo! Crisis
averted! Did you spot the several failure modes which return before
the free() call. In these modes, a malloc()d command is taken off the
queue, and not free()d. The pointer falls out of scope and memory lost.
Quod Erat Demonstratum.

To fix this, free() the command before hitting any exit paths.

Signed-off-by: Alexandru Gagniuc <mr.nuke.me@gmail.com>

---
## [jazzdelightsme/terminal](https://github.com/jazzdelightsme/terminal)@[9ccd6ecd74...](https://github.com/jazzdelightsme/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Tuesday 2022-07-05 03:54:15 by Mike Griese

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
## [jazzdelightsme/terminal](https://github.com/jazzdelightsme/terminal)@[8962f88f90...](https://github.com/jazzdelightsme/terminal/commit/8962f88f907d86fd8684b66f7f3e32a2709e3237)
#### Tuesday 2022-07-05 03:54:15 by Dustin L. Howett

Disable the VT color quirk for pwsh and modern inbox powershell (#13352)

In #6810, we introduced a "quirk" for all known versions of PowerShell
that suppressed their requests for black background/gray foreground.
This was done to avoid an [issue in PSReadline] where it would paint
black bars all over the screen if the default background color wasn't
the same as the ANSI black color.

Years have passed since that quirk was introduced. The underlying bug
was fixed, and the fix was released broadly long ago. It's time for us
to remove the quirk... almost.

Terminal still runs on versions of Windows that ship a broken version of
PSReadline. We must maintain the quirk there -- the user can't do
anything about it, and we would make their experience worse if we
removed the quirk entirely.

PowerShell 7.0 also ships a broken version of PSReadline. It is still in
support for another 6 months, but updates have been available for some
time. We can encourage users to update.

Therefore, we only need the quirk for Windows PowerShell, and then only
for specific versions of Windows.

_Inside Windows_, we don't even need that: we're guaranteed to be built
alongside a fixed version of PowerShell!

Closes #6807

[issue in PSReadline]: https://github.com/PowerShell/PSReadLine/issues/830#issuecomment-650508857

---
## [Jul-Lii/android_kernel_xiaomi_sdm845](https://github.com/Jul-Lii/android_kernel_xiaomi_sdm845)@[b437fb3824...](https://github.com/Jul-Lii/android_kernel_xiaomi_sdm845/commit/b437fb382410af754f1597503e29ce045a0efcc1)
#### Tuesday 2022-07-05 04:54:55 by Dave Chiluk

[BACKPORT] sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

It has been observed, that highly-threaded, non-cpu-bound applications
running under cpu.cfs_quota_us constraints can hit a high percentage of
periods throttled while simultaneously not consuming the allocated
amount of quota. This use case is typical of user-interactive non-cpu
bound applications, such as those running in kubernetes or mesos when
run on multiple cpu cores.

This has been root caused to cpu-local run queue being allocated per cpu
bandwidth slices, and then not fully using that slice within the period.
At which point the slice and quota expires. This expiration of unused
slice results in applications not being able to utilize the quota for
which they are allocated.

The non-expiration of per-cpu slices was recently fixed by
'commit 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift
condition")'. Prior to that it appears that this had been broken since
at least 'commit 51f2176d74ac ("sched/fair: Fix unlocked reads of some
cfs_b->quota/period")' which was introduced in v3.16-rc1 in 2014. That
added the following conditional which resulted in slices never being
expired.

if (cfs_rq->runtime_expires != cfs_b->runtime_expires) {
	/* extend local deadline, drift is bounded above by 2 ticks */
	cfs_rq->runtime_expires += TICK_NSEC;

Because this was broken for nearly 5 years, and has recently been fixed
and is now being noticed by many users running kubernetes
(https://github.com/kubernetes/kubernetes/issues/67577) it is my opinion
that the mechanisms around expiring runtime should be removed
altogether.

This allows quota already allocated to per-cpu run-queues to live longer
than the period boundary. This allows threads on runqueues that do not
use much CPU to continue to use their remaining slice over a longer
period of time than cpu.cfs_period_us. However, this helps prevent the
above condition of hitting throttling while also not fully utilizing
your cpu quota.

This theoretically allows a machine to use slightly more than its
allotted quota in some periods. This overflow would be bounded by the
remaining quota left on each per-cpu runqueueu. This is typically no
more than min_cfs_rq_runtime=1ms per cpu. For CPU bound tasks this will
change nothing, as they should theoretically fully utilize all of their
quota in each period. For user-interactive tasks as described above this
provides a much better user/application experience as their cpu
utilization will more closely match the amount they requested when they
hit throttling. This means that cpu limits no longer strictly apply per
period for non-cpu bound applications, but that they are still accurate
over longer timeframes.

This greatly improves performance of high-thread-count, non-cpu bound
applications with low cfs_quota_us allocation on high-core-count
machines. In the case of an artificial testcase (10ms/100ms of quota on
80 CPU machine), this commit resulted in almost 30x performance
improvement, while still maintaining correct cpu quota restrictions.
That testcase is available at https://github.com/indeedeng/fibtest.

Fixes: 512ac999d275 ("sched/fair: Fix bandwidth timer clock drift condition")
Signed-off-by: Dave Chiluk <chiluk+linux@indeed.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Reviewed-by: Phil Auld <pauld@redhat.com>
Reviewed-by: Ben Segall <bsegall@google.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: John Hammond <jhammond@indeed.com>
Cc: Jonathan Corbet <corbet@lwn.net>
Cc: Kyle Anderson <kwa@yelp.com>
Cc: Gabriel Munos <gmunoz@netflix.com>
Cc: Peter Oskolkov <posk@posk.io>
Cc: Cong Wang <xiyou.wangcong@gmail.com>
Cc: Brendan Gregg <bgregg@netflix.com>
Link: https://lkml.kernel.org/r/1563900266-19734-2-git-send-email-chiluk+linux@indeed.com
Signed-off-by: Raphiel Rollerscaperers <rapherion@raphielgang.org>
Signed-off-by: ethan-halsall <ethan.halsall@gmail.com>
Signed-off-by: CloudedQuartz <ravenklawasd@gmail.com>

---
## [CoolMintChocolate/xbvr](https://github.com/CoolMintChocolate/xbvr)@[04ae91075f...](https://github.com/CoolMintChocolate/xbvr/commit/04ae91075f4205bbee53c2424ff6b5bf22032c29)
#### Tuesday 2022-07-05 05:16:16 by theRealKLH

fix: Migrate Tonight's Girlfriend VR scenes to new scraper (#767)

* Update migrations.go

fix semi BAD migration

* remove personal config

* Update migrations.go

change migration number

* Update .gitignore

* Update migrations.go

more fixes. Should be able to remove dupes due to prior migration.

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[9eeae396f3...](https://github.com/Koi-3088/ForkBot.NET/commit/9eeae396f3a88766665568a0fb56cdd60911e7f5)
#### Tuesday 2022-07-05 05:31:11 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [RedMan13/yoooeooeortuiovyhcoajtgshflgdf](https://github.com/RedMan13/yoooeooeortuiovyhcoajtgshflgdf)@[fd436761b2...](https://github.com/RedMan13/yoooeooeortuiovyhcoajtgshflgdf/commit/fd436761b2daf094bf8fb93ee541fb7ed45432c9)
#### Tuesday 2022-07-05 07:12:17 by JeremyGamer13

add User Examples holy shi

i really hope my server doesnt fucking die for no reason

---
## [rnhamlin/run-buddy](https://github.com/rnhamlin/run-buddy)@[89ce02f19a...](https://github.com/rnhamlin/run-buddy/commit/89ce02f19ae1e94434e8b8f3109779b6b3e223de)
#### Tuesday 2022-07-05 08:18:34 by reneenh

that's all for tonight. my brain is fried. and I'm not even fully done with module 1. omg. i have so much to do. but i feel like i made progress, too. The slackbot experts helped me understand css box and using vs code. today i left off on 1.3.6 and I desperately need to finish this module and start the first 2 lessons of the next. 3? I might have the first 3 due. omg. okay. gonna try. goodnight now. see you in the morning, code.

---
## [Miraviel/Paradise](https://github.com/Miraviel/Paradise)@[ab7a358506...](https://github.com/Miraviel/Paradise/commit/ab7a35850672da159eea98085cf6fade7d595340)
#### Tuesday 2022-07-05 08:36:15 by Farie82

Makes setting a machine GC properly if not unset properly (#17840)

* Makes setting a machine GC properly if not unset properly

* Forgot one. Fuck you borer code

---
## [morganbanwe/Metamasklogiin](https://github.com/morganbanwe/Metamasklogiin)@[589720c3af...](https://github.com/morganbanwe/Metamasklogiin/commit/589720c3af1f2a235ba64887e71450a49b029bd5)
#### Tuesday 2022-07-05 09:11:53 by morganbanwe

Update issue templates

What Uphóld login actually is?

Crypto trading platform and Uphóld login to place in the Crypto  trading world in the year 2015 which also has the headquarter in United States of America. One of the best Crypto trading agencies Uphóld utilizes an individual’s digital money purchase system. Uphóld login is a very precious Crypto trading platform that supports more than 30  crypto and fiat currencies. There is iPhone 9.0 compatibility that is covering Uphóld login from every side. It has also introduced its latest version of  Android 4.1 as well as an internet browser too. Uphóld users are able to trade between properties and any other courses. 
Uphóld LOGIN CONSIST THE BEST TRADING

On the world’s largest trading place, Uphóld  login’s customers are working on Uphóld login, enjoying and sending funds all over the world. Not only this, users are also exchanging their digital assets and cryptocurrencies. This exchange has everything that a trader needs. For customers, Uphóld login is basically a network to make transactions like buying of crypto currencies, supply and steels. This modern, technological, and unique portfolio has both desktop and mobile trading sources that connect the users directly with a broad area or crypto trading network from the area of the world. Users can trade directly through the network of Crypto trading, debit card and credit card. With this you pay 0% of trading payment. 
Uphóld LOGIN WALLET

Uphóld login  wallet  requires the process of sending and receiving Bitcoins. The Bitcoin wallet available on Uphóld provides the user to access their funds and transactions by both the combination of private and public keys. Before starting a trading journey it is very important to choose the right wallet that is dependent on the various kinds of factors and also a consistent number of experienced traders and investors who have trusted that platform. This wallet is accessible from the phone as well as a desktop pocketbook. It is a non-custodial platform. A BTC wallet consists of both pros and cons. You should choose wisely that suits you. The more experienced a trader you are the more you should choose hardware wallet. Excess of the wallet can be done from Android, web browsers and IOS.
FEES CHARGED BY Uphóld LOGIN

When a user registers to hold a login they are not required to pay any charges because it is totally free, simply creating an account on Uphóld doesn’t require any charge. You need to pay the amount only for the withdrawals you make and deals of your down payment. The conversion also requires fees. However, these charges are evaluated and appended on the structure of the transactions and it also includes a short of restrictions. We will provide you point to point fee structures charged for down payments, withdrawals and conversions. 
There are 5 different types of BTC wallets

The 5 different types of BTC wallets are:

    PAPER BTC WALLET: this wallet is here to provide you with proper security to secure your BTC funds that have been held in your cold storage. Paper wallets are protected through both public and private keys that need to be printed on a sheet of paper which you will have to store in your bank.

    HARDWARE BTC WALLET: the hardware BTC wallet means the cold storage which is delicately connected to USB devices and specially designed to send and Store the cryptocurrencies offline. This is a very interesting feature of a folder login because this keeps you away from malicious acts and crises. Note that the hardware wallets can be a bit expensive for the common users, so before getting into it think about it. 

    WEB BTC WALLET: web wallets are the best choice chosen by the users who are beginners because they don't require any installation of any kind of software. To get connected with a web BTC wallet You only need access to the internet browser in that case they require a private key on the online server that should be controlled by third party. 

    MOBILE BTC WALLET: one more wallet for the casual users is mobile BTC wallet. The casual users should be proud to Uphóld login because it is providing them various wallets with easy factors. The mobile applications are normally provided in everyone's mobile phone. You can have a mobile BTC wallet in your own device and manage your wallet with the most user friendly surface. Although, it can be said that a mobile BTC wallet is not that much safe because the features and options on this wallet are very sensible for the users that want to buy and Store small volumes of BTC.

    DESKTOP BTC WALLET: it is the same as mobile BTC wallet because some of their programs are relatable, but this can be operated through desktop or laptop. The securities provided by desktop BTC wallet is decent and reliable only to store a small to medium amount of crypto currencies. One more thing about desktop BTC wallet is that its wallet is connected with hot wallets and constantly operated through the internet. 

Uphóld login account creation for any user from any residence

    Go to Uphóld login website or you can download a mobile app in your own device
    By clicking on three horizontal lines provided on the top right corner you will get the option to sign up
    Click on sign up button and write down your email address
    Now create a password that should be 8 in characters
    Choose your residence
    Click on submit and verify account
    for verification, an activation code will be send you on your email address
    Write the activation code and click on signup and your account will be ready to trade

FAQs:

    I’m having trouble on Uphóld login. Is there any customer service provided by Uphóld?

Uphóld login provides users 24/7 customer services to the users who are suffering from problems to Uphóld in order to trade, buy and sell. Customers can have a query session with the supportive team who will bring them out from their problem. You can directly call them through the given number provided on the Uphóld login website or you can also write an email, remember before writing email provide everything briefly that you want to ask or your problems.

    In what ways can I login to my registered Uphóld Login account?

    Download the app or visit the app hold login website, tap on sign in

    Write email and password

    Click on sign in button

    I’m not an USA resident, Can I have an account on Uphóld login?

People living in any country can access to do and register and account on Uphóld login in their own language

    Is Uphóld login wallet safe for BTC?

The Uphóld BTC Wallet has an appropriate respect all over the world. This is why anyone can trade between Crypto and local currencies and metals with all the freedom and pride.

    Is Uphóld login reliable for new users?

If you are the new user who has just started and entered the trading field to buy, sell, store and exchange cryptocurrencies then the Uphóld login wallet is going to give you a very reliable safe and user-friendly interface.

---
## [carshalash/tgstation](https://github.com/carshalash/tgstation)@[763a10d1cc...](https://github.com/carshalash/tgstation/commit/763a10d1cc44c91720101d422d8709ad1aa0644d)
#### Tuesday 2022-07-05 09:23:50 by distributivgesetz

Resonance cascade polishening, bugfixes and better logging (#67488)

This PR rewrites almost all messages related to cascade events. Some messages felt kinda clunky to read or could have been written better. Overall, the new messages add to the experience as a cascade being a terrifying event in a way that I felt the old ones missed, and they make the event feel overall a lot sharper.

While looking at the resonance cascade code, I noticed that there a lot of stuff about cascades in the air which was not touched on. So, as I do, this PR evolved into a polish and roundup PR for cascades. There was a lot of stuff still hanging out relating to the event, and although the big backend of it sits, there was still a bit left to be completed. Therefore this PR deserves more the title of the "Resonance cascade POLISHENING" instead of the "REFLAVAHRING". But yeah, you ever go on a massive tangent before?

---
## [avar/git](https://github.com/avar/git)@[d8672e2b69...](https://github.com/avar/git/commit/d8672e2b693880cb69abb8d74ec94116a8cbf134)
#### Tuesday 2022-07-05 10:00:07 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding.

This makes the rule faster both on the initial run as we can make
better use of GNU make's parallelism than the old ad-hoc combination
of make's parallelism combined with $(SPATCH_BATCH_SIZE) and "xargs
-n", as well as making it *much* faster for incremental building.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration, but all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would be the same as doing a full re-run. I.e. all of our patches
depended on all of $(COCCI_SOURCES), so a change in a single file
would force us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is
twofold. Firstly that as noted we needed to create an e.g. a
"swap.patch+", and didn't know how to incrementally update it.

The other is that we've been carrying forward the dependency on
the *.c files since 63f0a758a06 (add coccicheck make target,
2016-09-15) the rule was initially added as a sort of poor man's
dependency discovery.

As we don't include other *.c files depending on other *.c files has
always been broken, as could be trivially demonstrated e.g. with:

	make coccicheck
	make -W strbuf.h coccicheck

However, depending on the corresponding *.c files has been doing
something, namely that *if* an API change modified both *.c and *.h
files we'd catch the change to the
*.h we care about via the *.c being changed.

For API changes that happened only via *.h files we'd do the wrong
thing before this change, but e.g. for function additions (not "static
inline" ones) catch the *.h change by proxy.

We now do something much better instead:

 * If we spot that the *.c file has a corresponding *.o file already
   we depend on that *.o file.

   By doing this we're implicitly piggy-backing on
   COMPUTE_HEADER_DEPENDENCIES. See c234e8a0ecf (Makefile: make the
   "sparse" target non-.PHONY, 2021-09-23) for prior art of doing that
   for the *.sp files.

   E.g. now running:

       make coccicheck

  Followed by:

       make -W column.h contrib/coccinelle/free.cocci.patch

   Will take around 15 seconds on my 8 core box if I didn't run "make"
   beforehand, but around 2 seconds if I did and we have the
   corresponding "*.o" files.

 * If that *.o file doesn't exist we'll depend on an intermediate file
   of ours which in turn depends on $(FOUND_H_SOURCES).

   This covers both an initial build, or where "coccicheck" is run
   without running "all" beforehand, and because we run "coccicheck"
   on e.g. files in compat/* that we don't know how to build unless
   the requisite flag was provided to the Makefile.

   Most of the runtime of "incremental" runs is now spent on various
   compat/* files, i.e. we conditionally add files to COMPAT_OBJS, and
   therefore conflate whether we *can* compile an object and generate
   dependency information for it with whether we'd like to link it
   into our binary.

   Before this change the distinction didn't matter, but now one way
   to make this even faster on incremental builds would be to peel
   those concerns apart so that we can see that e.g. compat/mmap.c
   doesn't depend on column.h.

Implementation details:

 * Each <FILE> and <RULE> pair (e.g. grep.c and swap.cocci) creates a
   file like .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   The contrib/coccinelle/swap.cocci.patch file is then a "cat" of all
   of the relevant .build/contrib/coccinelle/swap.cocci.patch/* files,
   see 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for similar prior art.

 * We can take better advantage of parallelism, while making sure that
   we don't racily append to the contrib/coccinelle/swap.cocci.patch
   file from multiple workers.

   Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06). But doing so required careful
   juggling, as e.g. setting both to 4 would yield 16 workers.

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)". As noted
   upthread of [1] a naïve removal of "--all-includes" will result in
   broken *.cocci patches, but if we know the exhaustive list of
   includes via COMPUTE_HEADER_DEPENDENCIES we don't need to re-scan for
   them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

 * We can generalize COMPUTE_HEADER_DEPENDENCIES to spew out the list
   of *.h dependencies without making a *.o object, which is slightly
   faster, and would also benefit the "make sparse" target. We'd still
   need to run the compiler, it would just have less work to do.

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [fuck-boy-alam-vau-tera-papa/All_Fuck](https://github.com/fuck-boy-alam-vau-tera-papa/All_Fuck)@[b5c33f6ffd...](https://github.com/fuck-boy-alam-vau-tera-papa/All_Fuck/commit/b5c33f6ffd7de435006ebc6662ab12769da933c9)
#### Tuesday 2022-07-05 10:43:01 by Md. Alamgir Hosen

Merge pull request #1 from fuck-boy-alam-vau-tera-papa/fuck-boy-alam-vau-tera-papa-patch-1

Add files via upload

---
## [DroneBetter/Perspective3Dengine](https://github.com/DroneBetter/Perspective3Dengine)@[24b5dc4f49...](https://github.com/DroneBetter/Perspective3Dengine/commit/24b5dc4f49c8160265b4c3e479587c9703e5f6ad)
#### Tuesday 2022-07-05 12:39:15 by Drone_Better

Add dampeners, make dragging to pan camera now work by affecting angular velocity (like real spaceship), perhaps make raytracing mode somewhat better

Unlike aerodynamic drag (that is only linearly proportional to angular velocity for now), dampeners impart constant acceleration "retrograde" in orientation-space (or rather, the non-spherical 3-space of the rotateByScreen function), and are turned off when controls are used (you only have finite angular acceleration to impart per frame). However, when you're rotating by dragging the mouse, it fires retrograde pre-emptively as you approach your destination (because the axial suicide burn problem becomes only one of the equations of motion when you don't have to worry about such pesky things as the inverse-square law and Tsiolkovsky rocket equation). (Currently, dragging slowly seems to impart more rotation than dragging the same distance quickly, I don't know why but it's still less per time so shouldn't matter too much, I hope.)
This change was made because I didn't like that local angular velocity was conserved on mouse dragging (meaning, for instance, when you have positive roll velocity and rotate discretely by increasing local yaw by 90º, you would still have positive roll velocity instead of negative pitch velocity (as it would be if the rotation was only effectively changing the location of the eye you had open, conserving global angular velocity instead)). Because I was unsure of how to go about changing angular velocity when a body is rotated in a direction non-parallel to it in rotation-space, I decided to prevent doing so (and incidentally also made it more realistic).
I realised that the raytracing mode was based on the assumption that positive z would be forwards, it's actually negative y, I think something is still very wrong because, having changed the Lambert mode's equation from the Wikipedia one to my previous implementation (which I'm no longer sure is correct), the azimuth appears to be at the bottom of the screen, but I will get there eventually.

---
## [Bill2107/FPGA_DVI_CONTROLLER](https://github.com/Bill2107/FPGA_DVI_CONTROLLER)@[93d26b0357...](https://github.com/Bill2107/FPGA_DVI_CONTROLLER/commit/93d26b0357b08ad3131b535a1e90e32891d6fe07)
#### Tuesday 2022-07-05 13:14:10 by Billy Ballico

added a bunch of stuff for simulation + counters sort of work now

fucking race conditions omg trying to make shit work rn

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[67782eca30...](https://github.com/treckstar/yolo-octo-hipster/commit/67782eca305dba309aa2faace525e2aec1ae24ff)
#### Tuesday 2022-07-05 13:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [hypothesis/lms](https://github.com/hypothesis/lms)@[6809b8136b...](https://github.com/hypothesis/lms/commit/6809b8136b731935aeee1f9496eb3a13e178b263)
#### Tuesday 2022-07-05 13:38:17 by Sean Hammond

Don't run the functests on Jenkins

This is a pain because it apparently requires there to be a separate
`make functests-only` target (is that really necessary?).

But anyway: I don't think there's any benefit to running the functests
on Jenkins after we've already run them on GitHub Actions. It's just
more code to maintain and more waiting around for Jenkins to finish.
The idea originally was that Jenkins runs the tests actually inside the
Docker container so it's more similar to production than GitHub Actions
which doesn't run the tests in Docker. But I don't think there's ever
been a case of the tests passing on GitHub Actions and then Jenkins
catching a problem with its second run of the tests. So in practice I
think this is silly.

I think there are better steps that we could take to control
CI-versus-prod differences if we wanted to do that:

- Use the same OS in production as we use on CI.
  We could change CI to Alpine.
  But I'd recommend changing production to Ubuntu instead then we'd have
  Ubuntu on prod, CI and dev. And people recommend Debian over Alpine
  anyway:
  https://pythonspeed.com/articles/base-image-python-docker-images/

- Install the app into a virtualenv within the production Docker
  container so that it's isolated from the container's OS's Python
  packages

---
## [62832/ATM-7](https://github.com/62832/ATM-7)@[8bff1fe476...](https://github.com/62832/ATM-7/commit/8bff1fe4769e3ecd98814c640bc44640ee6e9f1a)
#### Tuesday 2022-07-05 13:50:40 by 90

Add more starting books

Tome now also includes guides/READMEs from Blood Magic, Evilcraft, RFTools, Roots Classic, SecurityCraft, Silent Gear, Spice of Life: Carrot Edition, The One Probe and The Twilight Forest.

---
## [thufschmitt/nix](https://github.com/thufschmitt/nix)@[98946e2d9c...](https://github.com/thufschmitt/nix/commit/98946e2d9c93e3558f19ee3d49deef67a98706d8)
#### Tuesday 2022-07-05 14:01:27 by Maximilian Bosch

nix-shell: restore backwards-compat with old nixpkgs

Basically an attempt to resume fixing #5543 for a breakage introduced
earlier[1]. Basically, when evaluating an older `nixpkgs` with
`nix-shell` the following error occurs:

    λ ma27 [~] → nix-shell -I nixpkgs=channel:nixos-18.03 -p nix
    error: anonymous function at /nix/store/zakqwc529rb6xcj8pwixjsxscvlx9fbi-source/pkgs/top-level/default.nix:20:1 called with unexpected argument 'inNixShell'

           at /nix/store/zakqwc529rb6xcj8pwixjsxscvlx9fbi-source/pkgs/top-level/impure.nix:82:1:

               81|
               82| import ./. (builtins.removeAttrs args [ "system" "platform" ] // {
                 | ^
               83|   inherit config overlays crossSystem;

This is a problem because one of the main selling points of Nix is that
you can evaluate any old Nix expression and still get the same result
(which also means that it *still evaluates*). In fact we're deprecating,
but not removing a lot of stuff for that reason such as unquoted URLs[2]
or `builtins.toPath`. However this property was essentially thrown away
here.

The change is rather simple: check if `inNixShell` is specified in the
formals of an auto-called function. This means that

    { inNixShell ? false }:
    builtins.trace inNixShell
      (with import <nixpkgs> { }; makeShell { name = "foo"; })

will show `trace: true` while

    args@{ ... }:
    builtins.trace args.inNixShell
      (with import <nixpkgs> { }; makeShell { name = "foo"; })

will throw the following error:

    error: attribute 'inNixShell' missing

This is explicitly needed because the function in
`pkgs/top-level/impure.nix` of e.g. NixOS 18.03 has an ellipsis[3], but
passes the attribute-set on to another lambda with formals that doesn't
have an ellipsis anymore (hence the error from above). This was perhaps
a mistake, but we can't fix it anymore. This also means that there's
AFAICS no proper way to check if the attr-set that's passed to the Nix
code via `EvalState::autoCallFunction` is eventually passed to a lambda
with formals where `inNixShell` is missing.

However, this fix comes with a certain price. Essentially every
`shell.nix` that assumes `inNixShell` to be passed to the formals even
without explicitly specifying it would break with this[4]. However I think
that this is ugly, but preferable:

* Nix 2.3 was declared stable by NixOS up until recently (well, it still
  is as long as 21.11 is alive), so most people might not have even
  noticed that feature.

* We're talking about a way shorter time-span with this change being
  in the wild, so the fallout should be smaller IMHO.

[1] https://github.com/NixOS/nix/commit/9d612c393abc3a73590650d24bcfe2ee57792872
[2] https://github.com/NixOS/rfcs/pull/45#issuecomment-488232537
[3] https://github.com/NixOS/nixpkgs/blob/release-18.03/pkgs/top-level/impure.nix#L75
[4] See e.g. the second expression in this commit-message or the changes
    for `tests/ca/nix-shell.sh`.

---
## [r4lv/acts](https://github.com/r4lv/acts)@[6e1fd31474...](https://github.com/r4lv/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Tuesday 2022-07-05 14:01:54 by Stephen Nicholas Swatman

feat: Implement a new orthogonal range search seed finder (#904)

As I said in #901, I have been playing around with seed finding a little bit lately. Last weekend, I mentioned an idea for a new (?) kind of seed finding algorithm based on range search datastructures, and this is the very, very first semi-working implementation of it, just before the weekend.

The idea behind this algorithm is relatively simple. In traditional seedfinding, we check a whole lot of candidate spacepoints to see whether they meet some condition. If you look at this differently, each spacepoint defines a volume in the z-r-φ space, which contains any spacepoints it can form a doublet with. What if we reversed this logic? What if we defined this volume first, and then just extract the spacepoints inside of that space? That way, we can vastly reduce the number of spacepoints we need to look at.

How do we do this quickly? With [_k_-d trees](https://en.wikipedia.org/wiki/K-d_tree). These data structures are cheap to build, and they give us very fast orthogonal range searches. In other words, we can very quickly look up which of our spacepoints lie within an axis-aligned orthognal n-dimensional hyperrectangle. In this case, which spacepoints lie within a z-r-φ box.

So, the core idea of this seedfinder is to define as many of our seedfinding constraints in orthogonal fashion. That way, we can make our candidate hyperrectangle smaller and smaller. The tighter the constraints we can place, the better. Then, we look up the relevant spacepoints, and we can avoid looking at any others. That also means this solution requires no binning whatsoever.

## Constraint conversion

Currently there are quite a few constraints in the code. Here is my status update on how well it is going to convert each of them. In some cases, we can define a weaker version of the constraints in orthogonal fashion. This is still very powerful, and it doesn't actually lose us any efficiency (because we can always check the tighter constraint in a non-orthogonal way later, not a problem)!

### Unary constraints

Currently, I am not aware of any unary constraints in the Acts seed finding code. That is to say, logic to determine whether a point is allowed to be a lower spacepoint. However, I have the following thoughts about introducing some:

* I believe the binning code does some kind of magic to determine whether a spacepoint can be a lower spacepoint. Since my solution doesn't use any binning, I don't have access to this just yet. However, if we can incorporate this logic it could be very powerful.
* Maximum single-point η: we currently have some checks in place to see if the pseudorapidity of particles is not too high. We could realistically use this maximum pseudorapidity, combined with the collision region range to constrain the bottom spacepoints.

### Binary constraints

These are the existing binary constraints on spacepoint duplets:

Constraint | Description | Orthogonalization
-|-|-
Minimum ∆r | Ensure that the second spacepoint is within a certain difference in radius | Full
Maximum cot θ | Ensure that the pseudorapidity of the duplet is not too high | Unsuccessful
z-origin range | Ensure that the duplet would have originated from the collision point | Weakened 
Maximum ∆φ<sup>1</sup> | Ensure that the duplet does not bend too much in the x-y plane | Full

<sup>1</sup> This check does not exist explicitly in the existing seed finder, but is implicit in the binning process.

### Ternary constraints

There are a lot of ternary constraints (to check whether a triplet is valid):

Constraint | Description | Orthogonalization
-|-|-
Scattering angle | ??? | Unsuccessful
Helix diameter | Ensure the helix diameter is within some range | In progress
Impact parameters | Ensure the impact parameters are close to the collision point | In progress
Monotonic z<sup>1</sup> | Ensure that z increases or decreases monotonically between points | Full

<sup>1</sup> This check does not exist in the existing seed finder, check #901.

There are also constraints defined in the experiment-specific cuts, and the seed filter, and in other places. If we could convert some of those to orthogonal constraints the implementation would become much more powerful. However, I don't really understand what is happening in those files just yet. Need more reading.

## Current performance

The current performance of this seedfinder is... Complicated. On my machine, it runs a 4000 π<sup>+</sup> event in about 5 seconds, three times slower than the existing seedfinder. Its efficiency is much higher though, and the fake rate is much lower. So that's something. However, that is in part because I am creating far more seed candidates, so take this with a big grain of salt.

## Potential gain

There are two ways that I can think of to use this kind of algorithm. The first is an inside-to-outside algorithm, where we pick a lower spacepoint first, check the space it defines for a middle spacepoint, and then check the space the two of them define for a third spacepoint. This algorithm has time complexity 𝒪(_n_<sup>3</sup>), and it has space complexity 𝒪(_n_). Due to the constants, I still believe this implementation can outperform the 𝒪(_n_<sup>2</sup>) existing algorithm, however.

The second way would be to construct a set of duplets using this logic, and then to fit those together like we do with traditional seedfinding. This has 𝒪(_n_<sup>2</sup>) time complexity like the existing code, but also space complexity 𝒪(_n_<sup>2</sup>).

## Things that are completed

* The implementation of the _k_-d tree seems to work very well, and it is quite fast.
* Basic seedfinding using this strategy is functional.

## Things that don't work yet

* My maximum ∆φ constraint does not cross the 2π boundary yet.
* I used the existing seedfinding algorithm as a stepping stone, which I have completely destroyed in the process. Obviously I do not intend on keeping it that way, and the existing algorithm will be restored to its full glory.
* Lots more.

## Things that can be improved

* Add more constraints, and tighten existing ones.
* Lots of things, pretty much everything. But I really want to go home for the weekend, so I will write this part next week.

---
## [psydox/gitea](https://github.com/psydox/gitea)@[3725fa28cc...](https://github.com/psydox/gitea/commit/3725fa28ccc01ab08060f591f894ea6443a348e8)
#### Tuesday 2022-07-05 15:12:33 by Gusted

Improve UI on mobile (#19546)

Start making the mobile experience not painful and be actually usable. This contains a few smaller changes to enhance this experience.

- Submit buttons on the review forms aren't columns anymore and are now allowed to be displayed on one row.
- The label/milestone & New Issue buttons were given each own row even tough, there's enough place to do it one the same row. This commit fixes that.
- The issues+Pull tab on repo's has a third item besides the label/milestone & New Issue buttons, the search bar. On desktop there's enough place to do this on one row, for mobile it isn't, currently it was using for each item a new row. This commits fixes that by only giving the searchbar a new row and have the other two buttons on the same row.
- The notification table will now be show a scrollbar instead of overflow.
- The repo buttons(Watch, Star, Fork) on mobile were showing quite big and the SVG wasn't even displayed on the same line, if the count of those numbers were too high it would even overflow. This commit removes the SVG, as there isn't any place to show them on the same row and allows them to have a new row if the counts of those buttons are high.
- The admin page can show you a lot of interesting information, on mobile the System Status + Configuration weren't properly displayed as the margin's were too high. This commit fixes that by reducing the margin to a number that makes sense on mobile.
- Fixes to not overflow the tables but instead force them to be scrollable.
- When viewing a issue or pull request, the comments aren't full-width but instead 80% and aligned to right, on mobile this is a annoyance as there isn't much width to begin with. This commits fixes that by forcing full-width and removing the avatars on the left side and instead including them inline in the comment header.

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[0a3447944a...](https://github.com/cockroachdb/cockroach/commit/0a3447944ae259b725ebff7d84cecd1b6a1de19c)
#### Tuesday 2022-07-05 15:21:07 by craig[bot]

Merge #80894 #81200 #81330 #81406

80894: build,gcp: enable nightly config to run GCP unit tests r=adityamaru a=adityamaru

Previously, the `pkg/cloud/gcp` tests package was skipped on CI
because most of the tests require credentials, and we risked exfiltration
of these secrets when running on public teamcity agents.

With the ability to run tests on agents that are not part of the public
pool we now have a `Cloud Unit Test` config that runs these tests nightly.
This change adds the script invoked by the config and cleans up the unit
tests to be more uniform in their authentication and environment variable
checks.

Informs: https://github.com/cockroachdb/cockroach/issues/80877

Release note: None

81200: ui: Improve time picker keyboard input r=jocrl a=jocrl

Fixes #80655, mostly.

Previously, users had to type `1:03 PM (UTC)` in order to enter text into the time picker.

This commit modifies the time picker so that users would instead type either
- `1:03`, or
- `01:03`

to enter text into the time picker. Copying and re-pasting the text from a time picker still works.

Alternate approaches not pursued (these are not needed with the removal of AM/PM).

1) Make our own time picker component, and style it to look like antd's. There's
a general issue of antd's components not being keyboard friendly:
https://github.com/ant-design/ant-design/issues/5685

2) Upgrade to `antd` version 4, and use an undocumented prop type. `antd`'s time
picker uses the time picker from the `rc-picker` library under the hood. In
`rc-picker`, the `format` prop is of type `String | String[]`, where if it's an
array the first value will be used for display and the remaining ones will be
used for parsing, as documented [here](https://react-component.github.io/picker). In theory, `antd` passes `format`
(and also any remaining, additional props in addition to the specified ones) to
the `rc-picker` component. So even though the `antd` `TimePicker` component
`format` prop is not documented to take in a string array, one might think that
passing in a string array anyway would work. In practice, passing in a string
array works in `antd` version `4.20.4`, as tested in the [antd sandbox](https://ant.design/docs/react/getting-started) 
(render `<TimePicker format={
["h:mm A", "h:mma"]}/>`). However, this does not work in our codebase
(which installs `antd` `v3.25.2`), or in the `antd` version `3.x` [sandbox](https://3x.ant.design/docs/react/getting-started). The errors that appear in
these two situations are different, and in a way demonstrate the potential for
breakage from using an undocumented feature in future upgrades from a version
that we've to work. If we do this, we should add a test.

3) Dead end: The `antd` `TimePicker` component takes an `onChange` prop with a
second `timeString` paramater. However, `onChange` only fires if the input is
of the correct, parsable format. The specific code that ignores text input that
is not of a parsable format is in `rc-picker`, [here](https://github.com/react-component/picker/blob/5306c8938aded49c5d6f6b6d4761ddab25e3cce9/src/Picker.tsx#L237).
This prevents us from being the one to do the fuzzy matching and passing the
value back to the component.

Release note (ui): The time picker component has been improved such that users
can use keyboard input to select a time without having to type `" (UTC)"`

81330: authors: add annrpom to authors r=annrpom a=annrpom

Release note: None

81406: geomfn: check NaN coordinates for ST_MinimumBoundingCircle r=rafiss a=otan

Resolves #81277

Release note (bug fix): Fix a bug where ST_MinimumBoundingCircle with
NaN coordinates could panic.

Co-authored-by: Aditya Maru <adityamaru@gmail.com>
Co-authored-by: Josephine Lee <josephine@cockroachlabs.com>
Co-authored-by: Annie Pompa <annie.pompa@cockroachlabs.com>
Co-authored-by: Oliver Tan <otan@cockroachlabs.com>

---
## [omertuc/assisted-service](https://github.com/omertuc/assisted-service)@[824f0960f4...](https://github.com/omertuc/assisted-service/commit/824f0960f4544770ba7f13e2cf7c35a579046b7f)
#### Tuesday 2022-07-05 15:53:10 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition

For context, this is a service-side follow-up to https://github.com/openshift/assisted-installer-agent/pull/388

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

Also, a new "imported" column has been added to clusters, to indicate
whether they were created through a conversion or through being
imported. This is important because the solution should only be
applied for imported clusters, and this will provide a good way
to tell apart imported from non-imported clusters.

Also, the clusterdeployments_controller can now import SNO clusters,
it was an oversight that should have been done as part of 4cda26533d377f453f68783e8b2eae438734555d (#3404)

# Ignition Files

The ignition files we currently look at are:

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
## [pydctw/cluster-api-provider-aws](https://github.com/pydctw/cluster-api-provider-aws)@[867afc7ac7...](https://github.com/pydctw/cluster-api-provider-aws/commit/867afc7ac718621a11e00fc2b05589ac2548d4d5)
#### Tuesday 2022-07-05 16:12:21 by Claudia Beresford

Fail apidiff make target when git fails

This is a fairly simple fix to ensure that when `git diff` fails on the
`make apidiff` target, the exit code is actually picked up by make.
Previously the exit code from `diff` was "swallowed" by the `if`.

eg:
```
$ cat Makefile
thing:
        if (exit 1); then \
		echo foo; \
        fi
        echo "still here"

$ make thing
still here
$ echo $?
0
```

What we want:
- exit 1 when `git diff` fails
- exit 0 when `grep` fails
- call `go-apidiff` when `git diff` and `grep` succeeds
- exit 1 when `go-apidiff` fails

This is honestly a complete pain to do in a Makefile.

I tried capturing output, moving everything to a script, calling from
one thing to another. But really this is just tricky to do the way we
want in Make.

So, if we can live with a little repetition, we can do the following:
- Check the `git diff` can run, exit 1 if not
- Run the `git diff` again, this time piping the successful command to
  `grep`
- If `grep` fails, then no worries, the target will roll on and exit 0
  like it always has.
- If `grep` succeeds then the `go-apidiff` tool is called and the target
  runs as intended.

------

In the case of `$(APIDIFF_OLD_COMMIT)`, there is some annoying `make`
magic going on here. Which I can't simply make fail since it will cause any
job which uses something in this Makefile to fail out of proximity.
The `shell` is expanded when the file is loaded meaning even targets
which do not care about the value will end up erroring (but not exiting)
when it fails. These are not errors which impact the target's run, but
they look annoying in CI.

Since this var is only used by `apidiff`, we can move it into that
target so it is only evaluated when specifically called.

---
## [ProjectVelvet/android_kernel_sm6250](https://github.com/ProjectVelvet/android_kernel_sm6250)@[3ab3734001...](https://github.com/ProjectVelvet/android_kernel_sm6250/commit/3ab37340015c4c1f317558f2d386a5785f6abdd9)
#### Tuesday 2022-07-05 20:01:09 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Excalibur-99 <txexcalibur99@gmail.com>

---
## [geertu/linux](https://github.com/geertu/linux)@[846bb97e13...](https://github.com/geertu/linux/commit/846bb97e131d7938847963cca00657c995b1fce1)
#### Tuesday 2022-07-05 20:08:06 by Jason A. Donenfeld

random: credit cpu and bootloader seeds by default

This commit changes the default Kconfig values of RANDOM_TRUST_CPU and
RANDOM_TRUST_BOOTLOADER to be Y by default. It does not change any
existing configs or change any kernel behavior. The reason for this is
several fold.

As background, I recently had an email thread with the kernel
maintainers of Fedora/RHEL, Debian, Ubuntu, Gentoo, Arch, NixOS, Alpine,
SUSE, and Void as recipients. I noted that some distros trust RDRAND,
some trust EFI, and some trust both, and I asked why or why not. There
wasn't really much of a "debate" but rather an interesting discussion of
what the historical reasons have been for this, and it came up that some
distros just missed the introduction of the bootloader Kconfig knob,
while another didn't want to enable it until there was a boot time
switch to turn it off for more concerned users (which has since been
added). The result of the rather uneventful discussion is that every
major Linux distro enables these two options by default.

While I didn't have really too strong of an opinion going into this
thread -- and I mostly wanted to learn what the distros' thinking was
one way or another -- ultimately I think their choice was a decent
enough one for a default option (which can be disabled at boot time).
I'll try to summarize the pros and cons:

Pros:

- The RNG machinery gets initialized super quickly, and there's no
  messing around with subsequent blocking behavior.

- The bootloader mechanism is used by kexec in order for the prior
  kernel to initialize the RNG of the next kernel, which increases
  the entropy available to early boot daemons of the next kernel.

- Previous objections related to backdoors centered around
  Dual_EC_DRBG-like kleptographic systems, in which observing some
  amount of the output stream enables an adversary holding the right key
  to determine the entire output stream.

  This used to be a partially justified concern, because RDRAND output
  was mixed into the output stream in varying ways, some of which may
  have lacked pre-image resistance (e.g. XOR or an LFSR).

  But this is no longer the case. Now, all usage of RDRAND and
  bootloader seeds go through a cryptographic hash function. This means
  that the CPU would have to compute a hash pre-image, which is not
  considered to be feasible (otherwise the hash function would be
  terribly broken).

- More generally, if the CPU is backdoored, the RNG is probably not the
  realistic vector of choice for an attacker.

- These CPU or bootloader seeds are far from being the only source of
  entropy. Rather, there is generally a pretty huge amount of entropy,
  not all of which is credited, especially on CPUs that support
  instructions like RDRAND. In other words, assuming RDRAND outputs all
  zeros, an attacker would *still* have to accurately model every single
  other entropy source also in use.

- The RNG now reseeds itself quite rapidly during boot, starting at 2
  seconds, then 4, then 8, then 16, and so forth, so that other sources
  of entropy get used without much delay.

- Paranoid users can set random.trust_{cpu,bootloader}=no in the kernel
  command line, and paranoid system builders can set the Kconfig options
  to N, so there's no reduction or restriction of optionality.

- It's a practical default.

- All the distros have it set this way. Microsoft and Apple trust it
  too. Bandwagon.

Cons:

- RDRAND *could* still be backdoored with something like a fixed key or
  limited space serial number seed or another indexable scheme like
  that. (However, it's hard to imagine threat models where the CPU is
  backdoored like this, yet people are still okay making *any*
  computations with it or connecting it to networks, etc.)

- RDRAND *could* be defective, rather than backdoored, and produce
  garbage that is in one way or another insufficient for crypto.

- Suggesting a *reduction* in paranoia, as this commit effectively does,
  may cause some to question my personal integrity as a "security
  person".

- Bootloader seeds and RDRAND are generally very difficult if not all
  together impossible to audit.

Keep in mind that this doesn't actually change any behavior. This
is just a change in the default Kconfig value. The distros already are
shipping kernels that set things this way.

Ard made an additional argument in [1]:

    We're at the mercy of firmware and micro-architecture anyway, given
    that we are also relying on it to ensure that every instruction in
    the kernel's executable image has been faithfully copied to memory,
    and that the CPU implements those instructions as documented. So I
    don't think firmware or ISA bugs related to RNGs deserve special
    treatment - if they are broken, we should quirk around them like we
    usually do. So enabling these by default is a step in the right
    direction IMHO.

In [2], Phil pointed out that having this disabled masked a bug that CI
otherwise would have caught:

    A clean 5.15.45 boots cleanly, whereas a downstream kernel shows the
    static key warning (but it does go on to boot). The significant
    difference is that our defconfigs set CONFIG_RANDOM_TRUST_BOOTLOADER=y
    defining that on top of multi_v7_defconfig demonstrates the issue on
    a clean 5.15.45. Conversely, not setting that option in a
    downstream kernel build avoids the warning

[1] https://lore.kernel.org/lkml/CAMj1kXGi+ieviFjXv9zQBSaGyyzeGW_VpMpTLJK8PJb2QHEQ-w@mail.gmail.com/
[2] https://lore.kernel.org/lkml/c47c42e3-1d56-5859-a6ad-976a1a3381c6@raspberrypi.com/

Cc: Theodore Ts'o <tytso@mit.edu>
Reviewed-by: Ard Biesheuvel <ardb@kernel.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [jecsatta/PhotoDemon](https://github.com/jecsatta/PhotoDemon)@[202103f4c8...](https://github.com/jecsatta/PhotoDemon/commit/202103f4c8157da049730bc0f21431967d491709)
#### Tuesday 2022-07-05 20:12:09 by Tanner

File > Export > Color lookup: this is actually gonna work!

I honestly didn't know if this homebrew LUT creation strategy would work, but it does!  Yay!

Here's the gist:

3D LUTs are used in a number of industries - video editing, game development, photography, etc.  LUT files exist in a bunch of different formats, and they're basically just giant tables that map colors from one domain to another.  Such tables are extremely helpful for taking complex color transforms with a ton of steps and reducing them into a single table that applies *all* those changes at once - e.g. in a game pipeline you might bump up brightness, reduce yellow tones, increase contrast, improve clarity at high and low ranges of the green spectrum, give everything a slightly violet tint, then tone-map that into a final screen-ready gamut. - but doing all those steps separately takes forever, so instead at development time you use Photoshop (or dedicated color-grading software) to create a LUT that performs all of those steps on every color in the spectrum (or a reasonably representative subset of colors), stores the final mapping of each color in a giant list, and then at run-time you can just apply that LUT to each frame to apply your huge list of edits in a single uniform pass.  Whether you're doing 100 adjustments or 1 doesn't matter - a LUT merges all those changes into a single mapping table that does it for you.

LUTs are also used extensively for color-grading photos and film, because once you develop a signature "look" you can simply merge the full pipeline of edits into a single LUT, and with one click you get that "look" on any arbitrary photo, video, whatever.  LUTs are one of the few photo editing things that works across almost any software and/or platform because at the end of the day, LUTs are pretty much just text files with encoded RGB tables inside.  So even if your software doesn't support e.g. a Curves tool, you can let users load a LUT created in software that *does* support curve adjustments and then apply it, because software doesn't care how a LUT was created - it just uses the embedded tables to convert all colors to new values.

So applying LUTs is the easy part.  PhotoDemon supports a number of LUT formats and lets you apply them to images the same way any other photo editor does.  But creating LUTs is a different story, and there was no way to *create* new LUTs inside PD... until this commit.

Photoshop limits LUT creation to adjustment layers specifically - you have to set up 1+ adjustment layers on an image, and then you can export the resulting merged adjustment-layer-transform into a new LUT file.  This is cool, obviously, and relatively easy to support because the possible range of edits is small.  But PhotoDemon doesn't provide adjustment layers (yet) and even Photoshop only supports a subset of its full Adjustment tool library as adjustment layers.  Wouldn't it be better if you could just edit a photo using ANY AND EVERY TOOL in the app, and then the app would magically reverse-engineer a LUT for you, encompassing all the changes you'd made?

That's what I've attempted to do in PhotoDemon, and by god, it works.  Mostly.  It's a little slow right now due to huge numbers of classes used in the necessary data structs (so the code is fast, but class teardown is like 60 seconds for the hundreds of thousands of classes that get created), so I'll need to rewrite some data structures either using lightweight classes or by converting them to array-driven methods.  But that's easy stuff compared to the work that's already been done!

Now for the caveats.

LUTs encode 1:1 mapping between colors, so they cannot encode area-driven effects (like blur, distort filters, etc).  This means they are best at encoding edits from Adjustment menu tools, but you don't really need to care about that - if you use any Effects, PhotoDemon can still auto-create LUTs for you!  But if the same color gets mapped to multiple output colors (due to a blur effect or similar), the quality of the LUT will suffer.

For the next caveat, I need to describe PD's LUT creator works.  Basically, the algorithm starts by comparing the final, edited image state to its original, unmodified state.  A huge tree of all represented colors is constructed, and the algorithm analyzes how each color has changed.  From that list of changes, it constructs a full-gamut LUT, directly using relevant color changes where it can and interpolating changes from similar colors for any parts of the color spectrum that the current image doesn't include.  This encodes most "normal" adjustment patterns very well, but can produce weird results if your source image has a very limited palette (e.g. it's grayscale, or mostly a single color tone, etc).

So for best results, if you intend to export a LUT you'll want to perform your adjustments/effects/etc on a photo with reasonably good color diversity - lots of dark and bright tones of as many different colors as possible.  This gives the LUT creator more information to work with, and the resulting LUT file will be more applicable to any type of image.

Next up is resolving the damn VB6 class teardown perf issue, then looking at an improved interpolation strategy that provides more accurate coverage of massive state changes (like "invert all colors").  I also want to write a new Render effect for generating color test patterns, which would help immensely for improving gamut coverage.

I need this tool available so that I can finally create a default set of LUTs to ship with PhotoDemon.  I want to provide similar LUTs to Photoshop's default set, but they copyright their LUTs (which seems silly - can you really copyright a list of numbers?  idk).  So I can't just ship Photoshop's files outright - but I can certainly make my own set of edits that produce a similar result to theirs, then create my own LUT files and ship *those*.  So that's what I'm gonna do.

Anyway, I legitimately didn't know if this strategy would work, so I'm pretty stoked to have a workable path forward for this feature.

---
## [nightmatt23/TFA-AR15](https://github.com/nightmatt23/TFA-AR15)@[3c0121988b...](https://github.com/nightmatt23/TFA-AR15/commit/3c0121988b3db6b290561a692ebbc5c6b66a0500)
#### Tuesday 2022-07-05 20:54:31 by Vagulik iz minecrafta

Ухуу подрочили бля

- Oh shit, I’m sorry!
- Sorry for what? Our daddy told us not to be ashamed of our dicks, especially since they are such good size and all
- Yeah, I see that. Daddy gave you good advice!
- It gets bigger when I pull on it
- MMmMmmMmM
- Sometimes I pull it on so hard I rip the skin
- Well, my daddy told me a few things to like uh, how not to rip the skin by using someone else’s mouth instead of your own hands.
- Can you show me?
- I’ll be right happy to!

---
## [simark/CanadianTracker](https://github.com/simark/CanadianTracker)@[3923e02921...](https://github.com/simark/CanadianTracker/commit/3923e02921a43fd81707a96dc91294f00fc16749)
#### Tuesday 2022-07-05 23:46:57 by Simon Marchi

Add SKUs table, use newer API to fetch data

We currently don't handle multi-SKU products well, fix that.

TLDR:

 - Add database table for SKUs
 - Use newer API to be able to get more details about SKUs
 - Adjust web UI to account for that

Taking this product as an example:

https://www.canadiantire.ca/en/pdp/thule-convoy-xt-rooftop-cargo-box-0401588p.html

This product has 3 different variants, or SKUs, with three different
prices.  There is a single entry in the products_static table.  The
`sku` columns contains a list of all the three SKUs for that product:

  40-1588-0|40-1589-8|40-1590-2

In the products_dynamic table, the samples for multi-SKU products refer
to the complete product, not a specific SKU.  For the example product,
we have samples like this one:

    {
        "Banner": "CTR",
        "Product": "0401588P",
        "PrimarySKU": "0401588",
        "CheckDigit": "0",
        "SKU_Count": 3,
        "Price": 699.99,
        "PriceFrom": "Y",
        "Description": "THL ALP 12CFT CNV XT",
        "Messages": {
            "Warranty": "This product carries a 1 year exchange warranty redeemable at any Canadian Tire store."
        },
        "PartNumber": "632100",
        "IsOnline": {
            "Active": "Y",
            "Exclusive": "N",
            "Sellable": "Y",
            "SpecialBuy": "N"
        }
    }

Note "PriceFrom" is "Y".  I believe this means that the rendered product
list would say "From $699.99", meaning that $699.99 is the price of one
of the three SKUs, we don't know which one (whichever is the
cheapest).  Given that we want to track prices for each individual SKU,
samples like this one are not helpful, and will have to be discarded.

Samples that refer to a single-SKU product have a `SKU` key, so we can
be confident the price is for a specific SKU.

Changes at the database level:

  - add the `skus` table, with the following columns:
    - index: auto-incremented integer
    - code: code, in the format "0401589"
    - formatted_code: code, in the format "040-1589-8"
    - product_index: index of the product (products_static table) this
      SKU belongs to
  - remove the `skus` column of the `products_static` table.
  - add the `samples` table, which is like the existing
    `products_dynamic` table, but with a foreign reference to the `skus`
    table, instead of to the `products_static` table .
  - remove the `products_dynamic` table.

The migration does the following steps to keep as much of the existing
data as possible:

  - Populate the `skus` table based on the existing content of the `sku`
    column of the `products_static` table, whose format is shown above.
  - Go over each existing price sample (`products_dynamic` table), see
    if we can move it to the new table.  If it doesn't have a `SKU` key,
    or has 'PriceFrom: Y' (I think these two are correlated, but we
    check both just in case), we can't.  Use the `SKU` value to know
    which row in the `skus` table this sample will now refer to.
  - There are some products without SKU information in column
    `products_static.sku`.  This is probably because these products were
    not seen since we added the `sku` column.  For those, we did not
    create an entry in the `skus` table.  If some samples refer to that
    SKU, we have a problem.  In that case, create a `skus` row based on
    that SKU number.  Assume that the product code is the SKU code plus
    'P', which always seems to be the case for single-SKU products.
    There are some rare cases where there is no such product, in that
    case we drop the sample.

Adjust the scraping code to provide this new information.  To do so, use
newer APIs, which are those I see the Canadian Tire website use at the
time of writing.  In the new API used for fetching list of products, the
information about SKUs is better structured than in the previous one.

We previously limited ourselves to scraping the categories of level 1
and 2.  During my testing, I saw that scraping each level of category
gave a different number of items, and there always seemed to be items
that appeared only in one level and not the others.  To have the best
coverage, we would have to scrape all category levels.  But doing so
would increase the workload quite a bit, if done each day.  The tradeoff
I made to have good coverage but not a huge workload is to use one
category level each day.  The category level is based on the number of
the current day, so if the scraping is done every day (which is the case
in our production system), we'll do all category levels in a round robin
fashion.  This step is to discover new products/skus, so it's fine if we
don't discover a new one immediately.  This is only the default though,
the category levels to scrape can be specified on the command-line.

I removed the step where we fetch the number of items in each category
to provide a length to ProductLedger.  When scraping the level 5 (the
most specific categories), this is just too long, since there are
hundreds of categories.  As a consequence, we no longer show a progress
bar with a known length when scraping the inventory.  We could maybe add
it back later, and make it optional.

Adjust the web UI to add a "SKU" page.  So, the user lands on the index,
which is the list of products.  The user clicks on a product, they land
on the list of SKUs for that product.  They then click on the SKU they
want.  The experience sucks, it will have to be improved, but it works.
The existing product.html page becomes sku.html, with minor obvious
changes (but git won't tell you that).

Adjust the ctquery command accordingly.

---

