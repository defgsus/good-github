## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-11](docs/good-messages/2022/2022-04-11.md)


1,843,709 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,843,709 were push events containing 3,042,989 commit messages that amount to 241,032,998 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [Charbomber/a-little-game-called-mario](https://github.com/Charbomber/a-little-game-called-mario)@[541c6d9842...](https://github.com/Charbomber/a-little-game-called-mario/commit/541c6d9842550d7a64bc76b1c36b4431b3f97686)
#### Monday 2022-04-11 00:03:14 by Charbomber

Whoops this isn't just assets haha

Common mistake!

Also sorry for the fucked up Level 5.

---
## [kenshen112/pcsx2](https://github.com/kenshen112/pcsx2)@[89f10e1605...](https://github.com/kenshen112/pcsx2/commit/89f10e160572063b4871bfb8d0c6ffff54f9543a)
#### Monday 2022-04-11 00:11:21 by RedDevilus

GameDB:  ':' to '-' + GS and other fixes

Windows doesn't like you to use ':' in folders this caused issues for when CK1 did savestates in folders and now it's also messing with unable to add covers in Qt so better to replace them and also to avoid other issues now and the future.
GS HW Fixes and other fixes for:
- Adventures of Cookie & Cream, The
- Brothers in Arms - Earned in Blood / Road to Hill 30
- Black
- Chaos Legion
- God Hand
- Knockout Kings 2001
- Kuon
- Outrun 2006 / 2 SP
- Project Eden
- Psi-Ops - The Mindgate
- Punisher, The
- Ratchet Deadlocked (USA) / Gladiator (Europe) / 3 Up Your Arsenal
- Silent Hills Origins / Shattered Memories / 3 / 4
- SoulCalibur II / III

Also made sure that the comments and their spacing were consistent.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[07e6768659...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/07e67686593faeac75c1743a1f9c45a256f0e331)
#### Monday 2022-04-11 00:21:55 by SkyratBot

[MIRROR] Refactor and improve antimagic to be more robust [MDB IGNORE] (#12619)

* Refactor and improve antimagic to be more robust (#64124)

This refactors the antimagic component to use and have bitflags, documentation, defines, code comments, named arguments, and renames variable names for clarity.

- /obj/effect/proc_holder/spell/aoe_turf/conjure/creature/cult is not used anywhere and has been removed
- /obj/effect/proc_holder/spell/targeted/turf_teleport/blink/cult is not used anywhere and has been removed

- New sound effects are played when magic is blocked. Depending on the type of magic being used it will be either:

- Equipping antimagic now properly updates the magic buttons
- Any magic being blocked or restricting casting now displays a message
- MAGIC_RESISTANCE_MIND now properly blocks telepathy effects
- Removes blood splatter when fireball is blocked
- Magic projectiles for staff of locker no longer spawn lockers when blocked by antimagic
- Fire breath is no longer blocked by antimagic
- Spellcards are now blocked by antimagic

Any antimagic on a mob blocks that magic type from being casted. (certain spells such as mime abilities completely ignore antimagic)

- Foilhats prevent someone from casting mind magic (telepathy, mindswap, etc.)
- Bibles, ritual Totems, nullrods, holymelons, and TRAIT_HOLY prevent someone from casting unholy magic (cult spells, etc.)
- Nullrods, ritual totem, and holymelons prevent someone from casting wizard magic (fireball, magic missile, etc.)
- Immorality talismans, berserker suits, and TRAIT_ANTIMAGIC prevents all types of magic (except stuff like mime abilities)
- Touch of Madness and Mindswap is now blocked with MAGIC_RESISTANCE and MAGIC_RESISTANCE_MIND
- Voice of god is now blocked with MAGIC_RESISTANCE_HOLY and MAGIC_RESISTANCE_MIND

* Refactor and improve antimagic to be more robust

* Update tiedshoes.dm

Co-authored-by: Tim <timothymtorres@gmail.com>
Co-authored-by: Gandalf <9026500+Gandalf2k15@users.noreply.github.com>

---
## [MacBlaze1/tgstation](https://github.com/MacBlaze1/tgstation)@[54403a1ca0...](https://github.com/MacBlaze1/tgstation/commit/54403a1ca0a1d83302430bbb54a0d6bc561f0098)
#### Monday 2022-04-11 00:39:33 by FinancialGoose

Fixes conveyor runtime (#65788)

Conveyor would runtime whenever it is right clicked with an item

Fixes #64595 (Runtime on conveyor for right clicking)

fixes a runtime with conveyor where right clicking it with any item would cause a runtime

Mothblocks rant from the issue report below, you've been warned:

Because right-clicking in BYOND is horse-shit. It pipes it all through the normal Click and only tells you it's a right-click through a flag. This means that on anything that isn't prepared, right-clicking is the same as left-clicking, which is terrible UX that only exists in SS13.

Nothing should return ..() from attackby_secondary, because the default is the legacy behavior of making right-click pass as left-click (which I want to kill ASAP, once nothing uses the stupid flags anymore).

Remove else return ..(), and make this whole thing do return SECONDARY_ATTACK_CANCEL_ATTACK_CHAIN.

---
## [SingingSpock/Skyrat-tg](https://github.com/SingingSpock/Skyrat-tg)@[b995fbe31b...](https://github.com/SingingSpock/Skyrat-tg/commit/b995fbe31b87402d3da2f8e98cec1f5659e52a47)
#### Monday 2022-04-11 01:38:54 by Zonespace

Contractor Expansion 2 (#12311)

* weh!

* fuck you linter

* very important

* Update modular_skyrat/modules/contractor/code/datums/midround/event.dm

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* Update modular_skyrat/modules/contractor/code/datums/midround/outfit.dm

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* requested changes

* also this

* requested + cleanup

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[351afe260b...](https://github.com/timothymtorres/tgstation/commit/351afe260b42764641a07385df5f7e24b840f631)
#### Monday 2022-04-11 03:01:03 by san7890

Fixes Mapping Icons For Bodylimbs (Don't Get A Shock!) (#65899)

* Fixes Mapping Icons For Bodylimbs (Don't Get A Shock!)

Hey there,

I implore you look at this photograph right here:

Ugly stupid base broken dumb /obj instead of the actual sprite fucking garbage idiotic purple-white square damn it i hate it so much fuck fuck fuck fuck let's fix it before the fire under my seat gets worse argh

Anyways, I checked with Kapu and did a bit of testing, and I managed to figure out a way to get the best of both the mapping world and the in-game world. Don't believe me? Check these out:

* addressses review

things still work

* kills female moth chests

---
## [mateusauler/dwm](https://github.com/mateusauler/dwm)@[67d76bdc68...](https://github.com/mateusauler/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Monday 2022-04-11 03:23:00 by Chris Down

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
## [leftbones/gem](https://github.com/leftbones/gem)@[8758872015...](https://github.com/leftbones/gem/commit/875887201544e25fc34e2e7df558e1c979dc6df3)
#### Monday 2022-04-11 03:58:00 by evprkr

Many changes, more to come

Too many changes, probably. I should have done this in a smaller commit,
but I wanted to squash all of the bugs I knew of before committing
again. Then I got carried away with adding features on the side. So,
here we go.

Added more to `colors.py` and implemented all(?) of the existing
HighlightGroups to where they are supposed to be. The color system is an
absolute garbage fire and will need to be completely redone, once I can
think of a better way to do it. It's honestly disgusting right now.

Started work on `PopupInput` in `popup.py` which I'll likely use for the
prompt mode, once that's implemented. That'll be next, I think.
Currently unfinished.

Added a few new keybindings, just convenience things like jumping to the
beginning or end of a line, appending to the end of a line, etc. Nothing
major. I did, however, make it so backspace and delete work in normal
mode as well as insert mode.

Added saving and loading, arguably the most important feature of
anything that claims to be an editor. Kinda silly that I didn't have it
until now, it was simple to add, I just didn't feel like doing it until
now. You can also open a new file by passing in the name of a file that
doesn't exist or by not passing a name at all, however, there's no way
to name a file when saving at the moment, so it would probably not work
properly if you tried to save an unnamed file.

Pay no attention to NOTES.md, that's outdated. I keep forgetting to
update it before committing.

Pretty sure that's it.

---
## [erikarn/wtf-os](https://github.com/erikarn/wtf-os)@[5b49d3a784...](https://github.com/erikarn/wtf-os/commit/5b49d3a784d6e28da9154f127356613e477f1d3b)
#### Monday 2022-04-11 06:01:29 by Adrian Chadd

[kern] Fix up the timer code to be more robust/defined around add/delete state

These changes are to better define the state of a timer entry, so
we know if it's not on the pending list, if it's on the pending list,
if it's active.  I want to better define this behaviour so we don't
have a repeat of FreeBSD's kernel timer/callout API when it comes to
queue, dequeue, cancellation points, etc.

I think I've captured all the relevant annoyances.

* In theory you can add/delete timers for other tasks, but they
  may fail, esp if we do SMP one day.
* For now do it from the owner task/context, but not the timer callback.
* I'll add a different call to rearm a timer from inside the timer callback
  so things are cleaner.

More info is in the commit.

---
## [LeoTheMighty/leothemighty.github.io](https://github.com/LeoTheMighty/leothemighty.github.io)@[b1c5c964c4...](https://github.com/LeoTheMighty/leothemighty.github.io/commit/b1c5c964c4a4472adb9c13b10d5e2cdd20cbf676)
#### Monday 2022-04-11 06:13:50 by Leo Belyi

Add the god damn gallery

no css yet but oh god I have to actually write that shit don't I
oh god oh fuck

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[53a05ad9f2...](https://github.com/ammarfaizi2/linux-block/commit/53a05ad9f21d858d24f76d12b3e990405f2036d1)
#### Monday 2022-04-11 06:40:37 by David Hildenbrand

mm: optimize do_wp_page() for exclusive pages in the swapcache

Patch series "mm: COW fixes part 1: fix the COW security issue for THP and swap", v3.

This series attempts to optimize and streamline the COW logic for ordinary
anon pages and THP anon pages, fixing two remaining instances of
CVE-2020-29374 in do_swap_page() and do_huge_pmd_wp_page(): information
can leak from a parent process to a child process via anonymous pages
shared during fork().

This issue, including other related COW issues, has been summarized in [2]:

 "1. Observing Memory Modifications of Private Pages From A Child Process

  Long story short: process-private memory might not be as private as you
  think once you fork(): successive modifications of private memory
  regions in the parent process can still be observed by the child
  process, for example, by smart use of vmsplice()+munmap().

  The core problem is that pinning pages readable in a child process, such
  as done via the vmsplice system call, can result in a child process
  observing memory modifications done in the parent process the child is
  not supposed to observe. [1] contains an excellent summary and [2]
  contains further details. This issue was assigned CVE-2020-29374 [9].

  For this to trigger, it's required to use a fork() without subsequent
  exec(), for example, as used under Android zygote. Without further
  details about an application that forks less-privileged child processes,
  one cannot really say what's actually affected and what's not -- see the
  details section the end of this mail for a short sshd/openssh analysis.

  While commit 17839856fd58 ("gup: document and work around "COW can break
  either way" issue") fixed this issue and resulted in other problems
  (e.g., ptrace on pmem), commit 09854ba94c6a ("mm: do_wp_page()
  simplification") re-introduced part of the problem unfortunately.

  The original reproducer can be modified quite easily to use THP [3] and
  make the issue appear again on upstream kernels. I modified it to use
  hugetlb [4] and it triggers as well. The problem is certainly less
  severe with hugetlb than with THP; it merely highlights that we still
  have plenty of open holes we should be closing/fixing.

  Regarding vmsplice(), the only known workaround is to disallow the
  vmsplice() system call ... or disable THP and hugetlb. But who knows
  what else is affected (RDMA? O_DIRECT?) to achieve the same goal -- in
  the end, it's a more generic issue"

This security issue was first reported by Jann Horn on 27 May 2020 and it
currently affects anonymous pages during swapin, anonymous THP and hugetlb.
This series tackles anonymous pages during swapin and anonymous THP:

 - do_swap_page() for handling COW on PTEs during swapin directly

 - do_huge_pmd_wp_page() for handling COW on PMD-mapped THP during write
   faults

With this series, we'll apply the same COW logic we have in do_wp_page()
to all swappable anon pages: don't reuse (map writable) the page in
case there are additional references (page_count() != 1). All users of
reuse_swap_page() are remove, and consequently reuse_swap_page() is
removed.

In general, we're struggling with the following COW-related issues:

(1) "missed COW": we miss to copy on write and reuse the page (map it
    writable) although we must copy because there are pending references
    from another process to this page. The result is a security issue.

(2) "wrong COW": we copy on write although we wouldn't have to and
    shouldn't: if there are valid GUP references, they will become out
    of sync with the pages mapped into the page table. We fail to detect
    that such a page can be reused safely, especially if never more than
    a single process mapped the page. The result is an intra process
    memory corruption.

(3) "unnecessary COW": we copy on write although we wouldn't have to:
    performance degradation and temporary increases swap+memory
    consumption can be the result.

While this series fixes (1) for swappable anon pages, it tries to reduce
reported cases of (3) first as good and easy as possible to limit the
impact when streamlining.  The individual patches try to describe in
which cases we will run into (3).

This series certainly makes (2) worse for THP, because a THP will now
get PTE-mapped on write faults if there are additional references, even
if there was only ever a single process involved: once PTE-mapped, we'll
copy each and every subpage and won't reuse any subpage as long as the
underlying compound page wasn't split.

I'm working on an approach to fix (2) and improve (3): PageAnonExclusive
to mark anon pages that are exclusive to a single process, allow GUP
pins only on such exclusive pages, and allow turning exclusive pages
shared (clearing PageAnonExclusive) only if there are no GUP pins.  Anon
pages with PageAnonExclusive set never have to be copied during write
faults, but eventually during fork() if they cannot be turned shared.
The improved reuse logic in this series will essentially also be the
logic to reset PageAnonExclusive.  This work will certainly take a
while, but I'm planning on sharing details before having code fully
ready.

#1-#5 can be applied independently of the rest. #6-#9 are mostly only
cleanups related to reuse_swap_page().

Notes:
* For now, I'll leave hugetlb code untouched: "unnecessary COW" might
  easily break existing setups because hugetlb pages are a scarce resource
  and we could just end up having to crash the application when we run out
  of hugetlb pages. We have to be very careful and the security aspect with
  hugetlb is most certainly less relevant than for unprivileged anon pages.
* Instead of lru_add_drain() we might actually just drain the lru_add list
  or even just remove the single page of interest from the lru_add list.
  This would require a new helper function, and could be added if the
  conditional lru_add_drain() turn out to be a problem.
* I extended the test case already included in [1] to also test for the
  newly found do_swap_page() case. I'll send that out separately once/if
  this part was merged.

[1] https://lkml.kernel.org/r/20211217113049.23850-1-david@redhat.com
[2] https://lore.kernel.org/r/3ae33b08-d9ef-f846-56fb-645e3b9b4c66@redhat.com

This patch (of 9):

Liang Zhang reported [1] that the current COW logic in do_wp_page() is
sub-optimal when it comes to swap+read fault+write fault of anonymous
pages that have a single user, visible via a performance degradation in
the redis benchmark.  Something similar was previously reported [2] by
Nadav with a simple reproducer.

After we put an anon page into the swapcache and unmapped it from a single
process, that process might read that page again and refault it read-only.
If that process then writes to that page, the process is actually the
exclusive user of the page, however, the COW logic in do_co_page() won't
be able to reuse it due to the additional reference from the swapcache.

Let's optimize for pages that have been added to the swapcache but only
have an exclusive user.  Try removing the swapcache reference if there is
hope that we're the exclusive user.

We will fail removing the swapcache reference in two scenarios:
(1) There are additional swap entries referencing the page: copying
    instead of reusing is the right thing to do.
(2) The page is under writeback: theoretically we might be able to reuse
    in some cases, however, we cannot remove the additional reference
    and will have to copy.

Note that we'll only try removing the page from the swapcache when it's
highly likely that we'll be the exclusive owner after removing the page
from the swapache.  As we're about to map that page writable and redirty
it, that should not affect reclaim but is rather the right thing to do.

Further, we might have additional references from the LRU pagevecs, which
will force us to copy instead of being able to reuse.  We'll try handling
such references for some scenarios next.  Concurrent writeback cannot be
handled easily and we'll always have to copy.

While at it, remove the superfluous page_mapcount() check: it's
implicitly covered by the page_count() for ordinary anon pages.

[1] https://lkml.kernel.org/r/20220113140318.11117-1-zhangliang5@huawei.com
[2] https://lkml.kernel.org/r/0480D692-D9B2-429A-9A88-9BBA1331AC3A@gmail.com

Link: https://lkml.kernel.org/r/20220131162940.210846-2-david@redhat.com
Signed-off-by: David Hildenbrand <david@redhat.com>
Reported-by: Liang Zhang <zhangliang5@huawei.com>
Reported-by: Nadav Amit <nadav.amit@gmail.com>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Vlastimil Babka <vbabka@suse.cz>
Cc: Hugh Dickins <hughd@google.com>
Cc: David Rientjes <rientjes@google.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Jason Gunthorpe <jgg@nvidia.com>
Cc: Mike Kravetz <mike.kravetz@oracle.com>
Cc: Mike Rapoport <rppt@linux.ibm.com>
Cc: Yang Shi <shy828301@gmail.com>
Cc: Kirill A. Shutemov <kirill.shutemov@linux.intel.com>
Cc: Jann Horn <jannh@google.com>
Cc: Michal Hocko <mhocko@kernel.org>
Cc: Rik van Riel <riel@surriel.com>
Cc: Roman Gushchin <roman.gushchin@linux.dev>
Cc: Andrea Arcangeli <aarcange@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Don Dutile <ddutile@redhat.com>
Cc: Christoph Hellwig <hch@lst.de>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Jan Kara <jack@suse.cz>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [repinger/sm8150_bahamut_kernel](https://github.com/repinger/sm8150_bahamut_kernel)@[80e21c5d26...](https://github.com/repinger/sm8150_bahamut_kernel/commit/80e21c5d2690e8728404288d6d307ffa51a982fb)
#### Monday 2022-04-11 07:29:39 by Peter Zijlstra

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

---
## [ErdinyoBarboza/Skyrat-tg](https://github.com/ErdinyoBarboza/Skyrat-tg)@[5c1e69aa44...](https://github.com/ErdinyoBarboza/Skyrat-tg/commit/5c1e69aa448e6e28738b4643a54bb104ee032555)
#### Monday 2022-04-11 07:37:01 by SkyratBot

[MIRROR] Fixes borg wallmounting [MDB IGNORE] (#12046)

* fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

* Fixes borg wallmounting

Co-authored-by: 小月猫 <alina.r.starkova@gmail.com>

---
## [LooserRIP/LooserRIP.github.io](https://github.com/LooserRIP/LooserRIP.github.io)@[2c72f505b8...](https://github.com/LooserRIP/LooserRIP.github.io/commit/2c72f505b8dd94ff271d176f164a0e725980de3d)
#### Monday 2022-04-11 08:08:13 by LooserRIP

Added H:S:V: and NO FUCK YOU AHAHHA yOU THOUGHT YOU'RE GETTING A NORMAL COMMIT NAAAH BITCH

---
## [igroglaz/rom2maps](https://github.com/igroglaz/rom2maps)@[d6339db799...](https://github.com/igroglaz/rom2maps/commit/d6339db799d113b9e71d8d85d2a66a680da69540)
#### Monday 2022-04-11 10:34:00 by Elcnar

Quest tweaks

Heal me
NW merge orcs in 2 groups and mark them as quests.
NW add group quest for bees with 2lvl. Add group quest for 3 spirits.
W change target quest for closer ogre, enable random spawn(often get spawn bugged).
CW remove similar quest with reward 250.
SW change group\target mark for dragon, demon, harp. Add target\intercept for lizard, instead of 1 orc intercept.
E Merge squirell and add intercept for them.
N add intercept for zombie group. Add group kill for range skeli. Change male necr for female and merge group with melee skeli.

Kids
N remove quest from squirell group(too far, 250 reward)
W remove intercept orc, replace with skeli from CE.
S add target on 2nd ogre. Remove spirit2 to clear quest pool(hard to reach, minimal reward).
SE change target\group for harpy, dragon.
CE-E add group quest for undead. Change target\group for demon.
NE add 1 spider to group and add intercept for them.

Muddle
NW add quests for humans, target and groups, 1 intercept for leader.
Intercept group for goblin. Merge spirits and add group quest.
W remove quests for archers and druid+melee(no exp, 250 reward, very hard).
SE addintercept quest for witch\dino.
NE temp remove quest for necr leader, reward is not worth it(spent 300+ bottle to kill him and get 1k, wow)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[16d4b2eaed...](https://github.com/mrakgr/The-Spiral-Language/commit/16d4b2eaed61969e316664ce035418d0beabfb27)
#### Monday 2022-04-11 11:07:43 by Marko Grdinić

"9:55am. I am up. Let me chill a bit and then I will start.

10:45am. Let me start. I want to go back through the series from yesterday and see if I skimmed over anything I should not.

10:50am. https://youtu.be/Hf2esGA7vCc?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=738

Rather than start with a cube, he should have started with a flat surface and traced out the outline that way.

https://youtu.be/Hf2esGA7vCc?list=PLjEaoINr3zgEL9UjPTLWQhLFAK7wVaRMR&t=767

He says not to bevel. I learned this the hard way.

I really should have watched his tutorials before doing anything.

11:50am. I've now gone through the early parts, start to finish. I am not really focusing too much on the videos themselves, but I do feel in the zone.

Apart from the edge flow merge, I haven't learned anything new. It is fine. Let me move to UDIMs.

https://www.youtube.com/results?search_query=blender+udim

https://youtu.be/Z3PwX1K9KDY
Udims in Blender to Substance Painter and Back Again

Let me start with this.

11:55am. https://youtu.be/Z3PwX1K9KDY?t=368

Actually, let me play along with this.

12:05pm. Hmmm, making UDIMs is easier than it seems. All I had to do was drag one of the cube faces to the right and I get what I want with no problem.

12:15pm. This is a good chance to try out UV packmaster, but I'll leave that until I am done with the vids. As an exercise, it might be good to redo the desk, but I'll leave proper UVing for my next prop.

No, seriously, why not just redo the work? Yeah, it is true that it took me 10 days for the desk, but now that I know how I could do it a lot faster.

I'll think about it. I just have no desire to repeat this work. Maybe I'll redo it in the future.

1:05pm. Let me take a break here.

I am thinking what I should do next.

I am starting to feel like redoing the desk a little. With the subdiv workflow, with UDIM, packed with the UV packmaster, the edge wear done using the wear generating nodes.

It is not like I am going to get anything simply by doing the work. Rather the best way to learn is by doing it perfectly.

I should aim to perfect my workflow."

---
## [InvisibleSmiley/laminas-db](https://github.com/InvisibleSmiley/laminas-db)@[91bd56cebd...](https://github.com/InvisibleSmiley/laminas-db/commit/91bd56cebd6a46ffaa78f068d3b8705732bdb56a)
#### Monday 2022-04-11 12:11:03 by Michał Bundyra

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
## [ddabkows/MyRestaurantManager](https://github.com/ddabkows/MyRestaurantManager)@[b841a86b85...](https://github.com/ddabkows/MyRestaurantManager/commit/b841a86b85e347f56d1b529a86dbfb0c589bc394)
#### Monday 2022-04-11 13:55:21 by Dominik Dabkowski

Thank you IntelliJ for being such a fucking bullshit

---
## [LightningFastRom/android_packages_apps_Settings](https://github.com/LightningFastRom/android_packages_apps_Settings)@[de7965ac3b...](https://github.com/LightningFastRom/android_packages_apps_Settings/commit/de7965ac3b14978598c70b999b4de9f6ae7bc97a)
#### Monday 2022-04-11 16:16:13 by Anay Wadhera

Settings: force enable our fun privacy stuff

* fuck you google >:(

Change-Id: I39a4c779f45fc87bda7d9aa41141008db9fa326a

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[1b7d7d9327...](https://github.com/pytorch/pytorch/commit/1b7d7d93276eb37c009905ef87ea9c2a7c95481e)
#### Monday 2022-04-11 16:44:33 by Brian Hirsh

Reland: "free up dispatch key space (in C++)" (#74963)

Summary:
Pull Request resolved: https://github.com/pytorch/pytorch/pull/74963

This is a re-land of D35192346 (https://github.com/pytorch/pytorch/commit/9872a06d77582e91e834103db75f774ca75f7fff) and D35192317 (https://github.com/pytorch/pytorch/commit/a9216cde6cc57f94586ea71a75a35aaabee720ff), which together are a diff that changes the internal representation of `DispatchKeySet` in pytorch core to free up the number of dispatch keys that we have available. See a more detailed description of the design in the original PR: https://github.com/pytorch/pytorch/pull/69633.

The original PR broke Milan workflows, which use a pytorch mobile build, and manifested as a memory corruption bug inside of `liboacrmerged.so`.

**Background: Existing Mobile Optimization**
Pytorch mobile builds have an existing optimization (here https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/c10/core/DispatchKey.h#L382 and here https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/aten/src/ATen/core/dispatch/OperatorEntry.h#L214), which works as follows:

Every operator in pytorch has a "dispatch table" of function pointers, corresponding to all of the (up to 64) different kernels that we might dispatch to when we run an operator in pytorch (autograd, cpu, cuda, complex number support, etc).

In mobile builds, the size of that table is shrunk from 64 to 8 to save a bunch of space, because mobile doesn't end up using the functionality associated with most dispatch keys.

The dispatcher also has a notion of "fallback kernels", which are kernels that you can register to a particular dispatch key, but should be able to work for "any operator". The array of fallback kernels is defined here: https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/aten/src/ATen/core/dispatch/Dispatcher.h#L294.

The mobile-optimization currently does **not** extend to this array (it wouldn't be that useful anyway because there is only one array of fallback kernels globally - vs. there is a separate dispatch table of function pointers per operator). So the per-operator tables on mobile are size 8, while the fallback table is size 64.

**The Bug**
This PR actually makes it difficult to enable that optimization separately for the per-operator arrays vs. the fallback array, and incidentally shrunk the size of the fallback array from 64 to 8 for mobile (that happened on this line: https://github.com/pytorch/pytorch/pull/69633/files#diff-f735cd7aa68f15b624100cbc4bb3b5ea76ffc7c9d3bec3b0ccabaa09609e5319R294).

That isn't a problem by itself (since mobile doesn't actually use any of the fallbacks that can no longer be stored). However, pytorch core will still register all of those fallback kernels on startup in mobile builds, even if they aren't used. When we tried to register one of those fallbacks on startup, it would try to dump the kernel somewhere in memory past the bounds of the (now smaller) array inside of the `Dispatcher` object, `backendFallbackKernels_`.

**Why didn't this problem show up in OSS CI? Why didn't it break other internal mobile workflows aside from Milan?**

Ideally, this failure would show up as part of the OSS signal on GitHub, since we already have mobile OSS builds. Given that it was another memory corruption issue that only affected Milan (subset of mobile), I'm not sure what's specific about Milan's builds that caused it only to manifest there. dreiss I wonder if there's another flavor of mobile builds we could run in OSS CI that could potentially help catch this?

**The debugging experience was pretty difficult**

Debugging the Milan-specific failure was made difficult by the following:

(1) lack of CI
- the original Milan failure didn't surface on my original diff, because the Milan job(s) that failed weren't triggered to run on pytorch changes. There's probably a balance to strike here, since those jobs will only be useful if they aren't flaky, and if they can produce reliable failure logs for debugging.

(2) It's difficult to get a repro.
- my work laptop doesn't have the right specs to run the Milan development workflow (not enough disk space)
- There is an existing OnDemand workflow for Milan, but it appears to be relatively new, and after a bunch of help from MarcioPorto, we ran into issues forwarding the log output from Milan tests on the emulator back to the terminal (see the original discussion here: https://fb.workplace.com/groups/OnDemandFRL/permalink/1424937774645433/)

(3) Lack of stack-traces.
- Most Milan failures didn't include actionable stack traces. phding generously helped me debug by running my suggested patches locally, and reporting back if there were any failures. The failing test didn't include a stack trace though (just the line where the crash appeared), so I ended up making some educated guesses about what the issue was based on the area of the crash.
ghstack-source-id: 152688542

Test Plan: Confirmed with phding that the broken Milan workflow from the previous version of this diff is now passing.

Reviewed By: phding, albanD

Differential Revision: D35222806

fbshipit-source-id: 0ad115a0f768bc8ea5d4c203b2990254c7092d30
(cherry picked from commit 002b91966f11fd55ab3fa3801b636fa39a6dd12c)

---
## [staten-island-tech/vue-project-2-ainu](https://github.com/staten-island-tech/vue-project-2-ainu)@[aaab2719a7...](https://github.com/staten-island-tech/vue-project-2-ainu/commit/aaab2719a745d2dd0269a41e878d4db8515a9af4)
#### Monday 2022-04-11 17:32:13 by darrenh6

12 Stout Street

Yuh
Real Rx
I used to wake up in my room in the morning
Put on my dirty shoes in the morning
Heard momma crying last night
Think the lights finna go out
Only thing on my mind is hitting a lick
Her Friend in prison for doing some shit
Say I'mma go to prison for doing some shit
Only thing on my mind is booming a bitch
12 Stout Street, I hated that house
I had to learn early on bein' a man about
My momma ain't never buy me shit
I sold drugs and robbed for all my shit
Momma said, "Baby that was years ago"
"Don't stress about shit that happened years ago"
This shit'd take a bitch years to know
I cried in the cold till my tears was froze
I hit a lick to help my momma out
How the fuck my mom the one to kick me out?
How the fuck you gonna send me out to the streets?
How the fuck you gonna say I can't come home to sleep?
How the fuck I come out your pussy and you
Choose your husband like you knew that Friend before me?
How the fuck you gon' turn your back on me?
How the fuck you gon' leave me flat on E?
How you gon' do that knowing they killed my dad?
You supposed to be my mom and my dad
I wish that fucking house would burn down
I couldn't tell you then but shit, I'll tell you now
For so many years, I held it down
I never in my life wanted to sell drugs
I would've been cool with playing games and shit
But instead I'm running with the gang and shit
Robberies done turned into shootings
Your son done did a gang and shit
It'd take a year to explain this shit
We don't stay safe, we stay dangerous
They took my brother, that fucked me up
Perc after perc, they fucking me up
Thousand percs later, still don't do nothing
Shits barely working, they're supposed to make me numb
Had flashbacks to when I was young
Bitches used to laugh and call me a bum
I was with Face, shot my first gun
Before Neo or Jet Li, I was the one
My momma ain't see it but the streets did
Said I wouldn't be shit, streets made me shit
Going through withdrawal, got me sick
I'm stretched back to back, I'm 'bout to flip
Don't look at me funny, you don't know shit 'bout me
Stood on the block with dreams of an Audi
Had a nightmare sleeping in my Audi
A Friend caught me lacking and pulled me out it
Big ass pistol to my mouthpiece
And it happened in front of 12 Stout Street

---
## [kraj/binutils-gdb](https://github.com/kraj/binutils-gdb)@[df7a7bdd97...](https://github.com/kraj/binutils-gdb/commit/df7a7bdd9766adebc6b117c31bc617d81c1efd43)
#### Monday 2022-04-11 17:52:16 by rupothar

gdb: add support for Fortran's ASSUMED RANK arrays

This patch adds a new dynamic property DYN_PROP_RANK, this property is
read from the DW_AT_rank attribute and stored within the type just
like other dynamic properties.

As arrays with dynamic ranks make use of a single
DW_TAG_generic_subrange to represent all ranks of the array, support
for this tag has been added to dwarf2/read.c.

The final piece of this puzzle is to add support in gdbtypes.c so that
we can resolve an array type with dynamic rank.  To do this the
existing resolve_dynamic_array_or_string function is split into two,
there's a new resolve_dynamic_array_or_string_1 core that is
responsible for resolving each rank of the array, while the now outer
resolve_dynamic_array_or_string is responsible for figuring out the
array rank (which might require resolving a dynamic property) and then
calling the inner core.

The resolve_dynamic_range function now takes a rank, which is passed
on to the dwarf expression evaluator.  This rank will only be used in
the case where the array itself has dynamic rank, but we now pass the
rank in all cases, this should be harmless if the rank is not needed.

The only small nit is that resolve_dynamic_type_internal actually
handles resolving dynamic ranges itself, which now obviously requires
us to pass a rank value.  But what rank value to use?  In the end I
just passed '1' through here as a sane default, my thinking is that if
we are in resolve_dynamic_type_internal to resolve a range, then the
range isn't part of an array with dynamic rank, and so the range
should actually be using the rank value at all.

An alternative approach would be to make the rank value a
gdb::optional, however, this ends up adding a bunch of complexity to
the code (e.g. having to conditionally build the array to pass to
dwarf2_evaluate_property, and handling the 'rank - 1' in
resolve_dynamic_array_or_string_1) so I haven't done that, but could,
if people think that would be a better approach.

Finally, support for assumed rank arrays was only fixed very recently
in gcc, so you'll need the latest gcc in order to run the tests for
this.

Here's an example test program:

  PROGRAM arank
    REAL :: a1(10)
    CALL sub1(a1)

  CONTAINS

    SUBROUTINE sub1(a)
      REAL :: a(..)
      PRINT *, RANK(a)
    END SUBROUTINE sub1
  END PROGRAM arank

Compiler Version:
gcc (GCC) 12.0.0 20211122 (experimental)

Compilation command:
gfortran assumedrank.f90 -gdwarf-5 -o assumedrank

Without Patch:

  gdb -q assumedrank
  Reading symbols from assumedrank...
  (gdb) break sub1
  Breakpoint 1 at 0x4006ff: file assumedrank.f90, line 10.
  (gdb) run
  Starting program: /home/rupesh/STAGING-BUILD-2787/bin/assumedrank

  Breakpoint 1, arank::sub1 (a=<unknown type in /home/rupesh/STAGING-BUILD-2787
  /bin/assumedrank, CU 0x0, DIE 0xd5>) at assumedrank.f90:10
  10       PRINT *, RANK(a)
  (gdb) print RANK(a)
  'a' has unknown type; cast it to its declared type

With patch:

  gdb -q assumedrank
  Reading symbols from assumedrank...
  (gdb) break sub1
  Breakpoint 1 at 0x4006ff: file assumedrank.f90, line 10.
  (gdb) run
  Starting program: /home/rupesh/STAGING-BUILD-2787/bin/assumedrank

  Breakpoint 1, arank::sub1 (a=...) at assumedrank.f90:10
  10       PRINT *, RANK(a)
  (gdb) print RANK(a)
  $1 = 1
  (gdb) ptype a
  type = real(kind=4) (10)
  (gdb)

Co-Authored-By: Andrew Burgess <aburgess@redhat.com>

---
## [expo/expo](https://github.com/expo/expo)@[d92760eeb2...](https://github.com/expo/expo/commit/d92760eeb25ebd325b0b06a3c3f49bbfe348d4d0)
#### Monday 2022-04-11 17:53:44 by Łukasz Kosmaty

[dev-launcher][iOS] Improve handling of LAN permission crash (#16792)

# Why

Closes ENG-4203.

# How

Try to retry if the network connection was rejected due to the lack of lan permission.
My code will only retry once per app process - in my opinion, we shouldn't save that information in the shared preferences. Retrying one network call isn't that painful even if the failure wasn't connected with the lan permission. That solution was the best, in my opinion, when I was playing with different versions. 

Also, sometimes when the network call was rejected due to the lack of lan permission, retrying it doesn't help, cause the prompt didn't appear in time, but we can't detect that. However, in that case, the app won't longer crash and also the user will be delegated to the error screen. After all, it seems like pretty good UX. 

# Test Plan

- run bare-expo locally ✅

---
## [npjohnson/android_device_essential_mata](https://github.com/npjohnson/android_device_essential_mata)@[ef239bf2d8...](https://github.com/npjohnson/android_device_essential_mata/commit/ef239bf2d86268005468ca95999c6c50d3df0553)
#### Monday 2022-04-11 18:54:39 by Sourajit Karmakar

mata: Add EXPENSIVE_RENDERING hints for GPU

To start off, mata had a pretty shit kernel. This kernel neither used
efficient frequencies, nor had great battery life not to mention the
horrible performance. This was fine because most users never gave a fuck
and I (the only guy dailying mata and tinkering with this stuff) just
never had a pleasant experience with it.

Looking at the new Kawase blur implementation added to Android 11, I
couldn't help but want it ASAP. However, the kernel just wouldn't
cooperate (apparently). Anay wanted me to rebase the kernel because,
"our kernel visibly didn't respond to GPU boost hints triggered by
the surfaceflinger from rendering expensive blur."

Well after two lengthy kernel rebases (albeit useful ones as I was able
to eliminate a LOT OF JUNK), here we fucking go — it was never the kernel
my genius man xD. Power hint changes taken from [1].

* While at it, let's boost the GPU's minimum frequencies to the 515MHz
  (basically the third step from the maximum frequency step available to
  the Adreno 540), to further help this old 10nm chad render that beastly
  but gorgeous looking blur.

[1]: https://android.googlesource.com/device/google/coral/+/refs/tags/android-s-beta-2/powerhint.json#905

Change-Id: I8f72e68873ea46b8b7a562e5d292422d602cf42d

---
## [yeeezsh/CPE-KMUTT-Web](https://github.com/yeeezsh/CPE-KMUTT-Web)@[d3f89fae02...](https://github.com/yeeezsh/CPE-KMUTT-Web/commit/d3f89fae02aa10e71d0dabb3382bb6d820151a52)
#### Monday 2022-04-11 19:36:38 by yee2542

Revert "fuck you ci"

This reverts commit dd6b305670a8edc469201655fc72bee30a19c71a.

---
## [Random-FrequentFlyer-Dent/pytorch](https://github.com/Random-FrequentFlyer-Dent/pytorch)@[65329f4fac...](https://github.com/Random-FrequentFlyer-Dent/pytorch/commit/65329f4fac8fb22318b7a3eb115e9da207d8d41a)
#### Monday 2022-04-11 19:51:09 by Edward Z. Yang

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
## [Netflix/titus-executor](https://github.com/Netflix/titus-executor)@[3590f8629d...](https://github.com/Netflix/titus-executor/commit/3590f8629d0142c208009d0f3362edd13580329e)
#### Monday 2022-04-11 20:12:59 by Kyle Anderson

RFC: TitusMainContainerVolume mount support

I expect a common pattern in Titus will be to
"Share this volume between the main container".

This would power things like Fuse mounts from a fuse sidecar,
or just sharing /mydata to things like nginx or whatever.

Our experience when working with this kind of pattern in
stock kubelet is kinda painful, becuase it means making
and EmptyDir, making an init container to copy files over
from the main one to that dir, and then sharing that EmptyDir
volume with another container.

But we control the runtime, we can make the common thing easy,
and I bet 90% of the kinds of volumes we will want will be like this.

---
## [uwstout-cs458-s22/advisor001](https://github.com/uwstout-cs458-s22/advisor001)@[bf6d5b5863...](https://github.com/uwstout-cs458-s22/advisor001/commit/bf6d5b586382c9138462004021ce71b34a564c9f)
#### Monday 2022-04-11 20:25:21 by Phosgenite

Current Attempt for api connection

pain.

Ruin has come to our family. You remember our venerable house, opulent and imperial, gazing proudly from its stoic perch above the moor? I lived all my years in that ancient, rumor shadowed manor, fattened by decadence and luxury - and yet I began to tire of conventional extravagance. Singular, unsettling tales suggested the mansion itself was a gateway to some fabulous and unnameable power. With relic and ritual I bent every effort towards the excavation and recovery of those long buried secrets, exhausting what remained of our family fortune on swarthy workmen and sturdy shovels.

At last in the salt soaked crags beneath the lowest foundations we unearthed that damnable portal of antediluvian evil. Our every step unsettled the ancient earth but we were in a realm of death and madness. In the end I alone fled laughing and wailing through those blackened arcades of antiquity until consciousness failed me.

You remember our venerable house, opulent and imperial. It is a festering abomination! I beg you. Return home; claim your birthright, and deliver our family from the ravenous, clutching shadows of the API functionality connection.

---
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[8869876d0f...](https://github.com/mbs-octoml/mbs-tvm/commit/8869876d0fb0a79a995db58c578b7a153614c3a5)
#### Monday 2022-04-11 20:37:50 by Mark Shields

** Collage v2 sketch ***

- Enable cudnn, get rid of support for op-predicate based BYOC integrations
- Enable cublas
- And yet another go at pruning unnecessary candidates.
- Another go at pruning unnecessary candidates
- Fix CompositePartitionRule use
- Fix a few bugs with new TensorRT pattern-based integration
- Rework RemoveSubCandidatesCombinerRule for soundness
- Better logging
- Bug fixes
- Implement critical nodes idea for avoiding obviously unnecessary candidates
- Promote DataflowGraph from alias to class so can cache downstream index set
- Quick check to avoid unioning candidates which would create a cycle
- Host out CandidatePartitionIndex and add rules to avoid small candidates subsumed by containing candidates
- GetFunction can legitimately return nullptr
- rename tuning log
- Support for int64 literals
- Switch GPT2 to plain model
- Fix library cloberring issue for cutlass
- actually checkin 'built in' tuning log (covers mnist & gpt2 only)
- trying to debug gpt2
- Update TargetKind attribute name
- working through gpt2 issues
- checkin tuning records for MNIST (with hack to not retry failed winograd)
- Autotvm tuning disabled if log file empty (default)
- Autotvm tuning during search working
- tune during search
  (but does not load tuned records after search!)
- About to add tuning to estimate_seconds
- Split out the combiner rules & make them FFI friendly
- Rework comments
- Estimate IRModule instead of Function (closer to meta_schedule iface)
- Add 'host' as first-class partitioning spec
  (Avoids special casing for the 'leave behind for the VM' case)
- Move CollagePartitioner to very start of VM compiler flow (not changing legacy)
- Fix bugs etc with new SubGraph::Rewrite approach
  Ready for updating RFC to focus on partitioning instead of fusion.
- Working again after partition<->fusion split.
- Add PrimitivePartitionRule
- Refactor SubGraph Extract/Rewrite
  *** CAUTION: Almost certainly broken ***
- Rename kernel->partition, fusion->partition
- Next: make nesting in "Primitive" an explicit transform
- respect existing target constraints from device planner
- make 'compiler' and 'fusion_rule' attributes avail on all target kinds
- moved design to tvm-rfcs, https://github.com/apache/tvm-rfcs/pull/62
- incorporate comments
- avoid repeated fusion
- fix trt type checking
- better logs
- pretty print primitive rules
- fix tensorrt
- multiple targets per spec
- don't extract candidate function until need cost
  Need to bring CombineByPrimitives back under control since lost depth limit.
- cleaned up fusion rule names
- added 'fuse anything touching' for BYOC
- Finish dd example
- Add notion of 'MustLower', even if a candidate fires may still need to consider
  leaving node behind for VM (especially for constants).
- starting example
- finished all the dd sections
- documentation checkpoint
- docs checkpoint
- more design
- starting on dd
- runs MNIST with TVM+CUTLASS+TRT
- cutlass function-at-a-time build
- need to account for build_cutlass_kernels_vm
- move cutlass tuning into relay.ext.cutlass path to avoid special case
- add utils
- don't fuse non-scalar constants for tvm target.
- stuck on cuda mem failure on conv2d, suspect bug in main
- where do the cutlass attrs come from?
- running, roughtly
- pretty printing, signs of life
- wire things up again
- Switch SubGraph and CandidateKernel to TVM objects
- naive CombineByKindFusionRule, just to see what we're up agaist
  Will switch to Object/ObjectRef for SubGraph and CandidateKernel to avoid excess copying.
- preparing to mimic FuseOps
- rework SubGraph to use IndexSet
- rough cut at MaximalFusion
- split SubGraph and IndexSet in preparation for caching input/output/entry/exit sets in SubGraph.
- top-down iterative handling of sub-sub-graphs
- about to give up on one-pass extraction with 'sub-sub-graphs'
- Add notion of 'labels' to sub-graphs
- Rework FusionRules to be more compositional
- partway through reworking fusion rules, broken
- SubGraph::IsValid, but still need to add no_taps check
- dataflow rework, preparing for SubGraph::IsValid
- explode into subdir
- mnist with one fusion rule (which fires twice) working
- switch to CandidateKernelIndex
- Confirm can measure 'pre-annotated' primitive functions
- checkpoint
- stuff
- more sketching
- dominator logging

---
## [aisgbnok/terminal](https://github.com/aisgbnok/terminal)@[446f280757...](https://github.com/aisgbnok/terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Monday 2022-04-11 20:53:30 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [gitster/git](https://github.com/gitster/git)@[3d2f96a930...](https://github.com/gitster/git/commit/3d2f96a930d8ba68326260289a3d5511560281ce)
#### Monday 2022-04-11 21:43:16 by brian m. carlson

builtin/stash: provide a way to export stashes to a ref

A common user problem is how to sync in-progress work to another
machine.  Users currently must use some sort of transfer of the working
tree, which poses security risks and also necessarily causes the index
to become dirty.  The experience is suboptimal and frustrating for
users.

A reasonable idea is to use the stash for this purpose, but the stash is
stored in the reflog, not in a ref, and as such it cannot be pushed or
pulled.  This also means that it cannot be saved into a bundle or
preserved elsewhere, which is a problem when using throwaway development
environments.

Let's solve this problem by allowing the user to export the stash to a
ref (or, to just write it into the repository and print the hash, à la
git commit-tree).  Introduce git stash export, which writes a chain of
commits where the first parent is always a chain to the previous stash,
or to a single, empty commit (for the final item) and the second is the
stash commit normally written to the reflog.

Iterate over each stash from topmost to bottomost, looking up the data
for each one, and then create the chain from the single empty commit
back up in reverse order.  Generate a predictable empty commit so our
behavior is reproducible.  Create a useful commit message, preserving
the author and committer information, to help users identify stash
commits when viewing them as normal commits.

If the user has specified specific stashes they'd like to export
instead, use those instead of iterating over all of the stashes.

As part of this, specifically request quiet behavior when looking up the
OID for a revision because we will eventually hit a revision that
doesn't exist and we don't want to die when that occurs.

Signed-off-by: brian m. carlson <sandals@crustytoothpaste.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[8d9f090653...](https://github.com/mrakgr/The-Spiral-Language/commit/8d9f0906536c558fbc0c2877a1b086c2525170fe)
#### Monday 2022-04-11 22:23:38 by Marko Grdinić

"https://youtu.be/Z3PwX1K9KDY?t=720

Ah, right note how it says that this cannot be changed later. Yeah, I am stuck with what I have for the desk. I better make a folder for all the textures. For the close ups, it will be fine to use 4k, but for the rest I'll use 2k or even lower depending on the distance. It is not a big deal.

12:20pm. If I had to do the desk again, for the edge wear I should just use the regular nodes for that along with a mask.

And for the knot wear, note edge wear cann be applied based on the height map.

Actually, this should have been obvious, but it did not even occur to me to do that.

Doing it like that would have saved me hours of fidding around with a brush.

Yeah, as expected I did it all wrong. The top pattern I should have done in Desginer as well.

Yeah, it might not be bad to redo it. It would be a good chance to investigate the mask generators. The rest of the objects in my room do not have worn edges. The desk is unique in the amount of micro detail it has.

12:30pm. I don't like how decimate results in ngons, but I think there is a Triangulate modifier. Can I make it work like poke?

Actually, the trinagulate with the beauty options is not bad at all. It is just not fitting to use before a subdiv.

12:35pm. Also, poke is not for triangulation. It always split a face in the middle even if it's a trie.

https://youtu.be/Z3PwX1K9KDY?t=761

Let me get back to the video. I've started going on a tangent and playing with Blender.

https://youtu.be/Z3PwX1K9KDY?t=1346

What a pain in the ass. No doubt there is a plugin to automate this.

1:45pm. Done with chores. Let me move to breakfast.

Also, I seem to have accidentally cut a part of the previous entry out of order. Nevermind that.

2:45pm. I wish they'd rendered the backgrounds in BRS Dawn Fall with displacement on. Textures always look flat when in motion. Normals are just a band aid.

I'll make it one of my follows. I really need to get through my anime backlog, but I keep reading novels whenever I have free time instead.

2:50pm. Let me start. I'll leave fiction for later. Yesterday I ended up watching that course by the donut man instead of doing anything.

https://youtu.be/55sGQLX7iho
Introduction to UDIMs in Blender

Let me watch this thing and after that I'll redo the desk.

3:05pm. Right now I am removing the bevels by hand. It won't take too long.

3:40pm. That was tough, but I managed it. I managed to preserve the positioning. Now let me do it one by one.

5:15pm. Ah, crap, I am working on the desk piece and while testing remeshing, I stupidly set the octree depth to 15. Now I have no idea how long it will take to remesh.

...Had to forcefully abort it.

7pm. Blender crashed out of the blue. This was the first time this happened in a long while. In fact I am not sure it ever happened out of the blue just like that.

Damn, I lost a bunch of work.

But not too much.

That having said, this is such a waste of time.

I had a taste of the subsurf workflow and I am throwing in the towel. It is not really better than than the bevel workflow. It is not enough of a reason to ditch the work that I already did.

It is really annoying to place loop cuts and align them. It is a whole nother can of worms compared to bevels. While with bevels you have to think about it shearing your geometry here, you have issues getting the geometry right.

Sigh, the geometry resulting from subdiving is beautiful, but then you have issues with it being in excess. You can use decimate sure, but then you have ngons to deal with afterwards.

It is true that this workflow preserves seams better, but they aren't hard to place in the beveling workflow to begin with.

You can see how long it took. I've been at it for 4h, and I am 80% done with modeling, and I haven't even started UVing.

7:35pm. Done with lunch. Let me catch my bearings.

7:50pm. I am weighting the pros and cons of the two approaches.

8pm. Hmmm, I am going to give the win to subdiv workflow simply because the bevel one does not work properly. That is to say, assigning weights and beveling does not work when the weights are different. I've been running into issues with that. Just now I tried it on a cube and ran into weird pinching issues.

The fact that subdiv produces clean topology and is not too hard to use is a big point in its favor.

The fact that it preserves seams I am not going to count in its favor.

I tried drilling holes into some of the metal pieces and found out first hand just how problematic dealing with UVs would be.

For the rest of the scene, the other props I mean, I am not going to even bother putting in seams by hand. It is a huge waste of time. I'll just use the auto UVs.

8:05pm. I did try the unwrap subdiv feature and it does not work properly. I get really weird stretching even after turning it on, so after applying the UVs, I'd have to recalculate them anyway.

It says it is supposed to unwrap the UVs after applying the subdiv, but the results do not match.

Using booleans would wreck the neat topology either way. It would all get triangulated at the end anyway.

It is really easy to drill a bunch of holes into the metal pieces using booleans. But dealing with seams not matching and whatever else I could do without. Also on the metal piece those flat corners turn into half spheres.

8:15pm. The lesson I am drawing here - if I want to actually make it as a 3d artist I absolutely need to stop worrying about topology and start worrying about getting things done quickly.

If I start hesitating to use booleans because they would make UVing harder, I've lost.

Having a few extra islands does not matter at all. You'd want to split the faces up into individual pieces anyway if possible if it were not for padding.

When putting textures in Substance Painter I'd use triplanar or planar projection so the seams literally don't matter.

8:15pm. It would be one thing to worry about topology if I am making assets for a buyer, but for static scenes they don't matter. I'll be able to cover up the shortfall with better hardware.

8:25pm. Let me finish the desk once more. I hate dropping work half completed. Now that I've cooled my head, let me just get the modeling done.

8:50pm. It crashed in a similar way. Thankfully this time I was more propared.

It does not seem this is a performance related crash like the one Clarisse has. Rather, when I tab into edit mode for one of the objects it crashes. I have no idea why.

9:45pm. I finished the desk. For that desk piece it is really a good idea to avoid using insets.

This happened to me with bevels as well for some reason.

I did not mention it earlier, but I did a bug report. Not sure if it will do any good since I do not have any idea why it crashed. I only sent them the bugged file. I managed to get around the issue by deleting the said object and recreating it.

10pm. Ok, the desk is in good shape now. Good job me. I am going to give UV Packmaster a try. Also I should try to track down UV Zen, though I am not sure if I will be sucessful. But I do have options when it comes to doing UVs. Houdini is an option as well. I won't fret about this too much.

Houdini is also a good option for remeshing, but I should just avoid that.

Forget the decimate modifier even exists.

10:15pm. Let me close here. Thinking about it is not going to get me to the answer. I haven't decided that I should use this desk, but I should definitely check out the UV tools.

...Hmmm, actually before I close, let me try out an alternative way of making holes.

Oh, it works well. Since it does not demolish the topology like booleans it might be worth using this.

10:40pm. No forget it. Forget It. I need to close. I should be watching anime instead of fiddling around in Blender.

Since I've gotten an interest in carving out objects, it might be worth checking out tutorials on the hard ops addon. I am interested in what it could add to my workflow. I think I recall seeing it on Persia.

What I can't figure out is how could one carve out a chunk while keeping the subdiv mod intact.

You could put in a subdiv, and then carve out a chunk using a boolean cutter like I did now, but unless you apply the modifier, you can't do anything after that. It feels quite limiting.

https://www.youtube.com/watch?v=kLIHH7LUrR4
The PROPER way to deform objects in Blender!

Let me watch this.

https://youtu.be/kLIHH7LUrR4?t=233

Never saw this before. It is possible to use a latice to deform an object in Blender.

https://youtu.be/kLIHH7LUrR4?t=314

It doesn't compress the geometry. Amazing.

https://youtu.be/kLIHH7LUrR4?t=334

He actually converted all the faces to ngons.

This guy is definitely somebody I can learn a lot from.

11:15pm. https://youtu.be/AuY_kHUya9A
Ngons to SubD is easier than you think! (Blender Tutorial)

I'll leave this for tomorrow.

https://www.youtube.com/watch?v=QYzdv4sHYcQ
A Casual Hard Surface Unwrapping Workflow (Blender)

This as well.

...Actually, let me watch the first one. I want to do it.

11:25pm. I need to remember the Ctrl + X shortcut.

I saw him use it earlier, but I forgot about it while cleaning.

11:30pm. It is just him cleaning topology. I did a bit of that on my own today. Not interested.

https://youtu.be/LdQwmfPyuw0
COMPLETE non-destructive workflow in Blender tutorial

Let me watch a bit of this.

https://youtu.be/LdQwmfPyuw0?t=937

Oh, I've been wondering how to fix this. This is good.

https://youtu.be/1qVbGr_ie30?t=603

Note: Figure out how he is doing that even shrink tomorrow.

Let me close here for real.

I am just not sure. Maybe I do not understand bevels I see this guy using them all the time. Subdiv strikes me as being difficult to use with booleans.

12:15pm. No, I don't get bevels.

I just do not have any way to control the edge lengths properly right now. And putting an incomplete bevel ends up blocking future ones.

Yeah, what is giving me problems are the bevels.

It is true that subdiv is better, but that might be simply due to my low understanding of how to use bevels.

Before I pass final judgement I should see whether I can upgrade my understanding. If I can, my ability to make props should go up significantly."

---
## [r-neal-kelly/nkr](https://github.com/r-neal-kelly/nkr)@[8a3ad4f3bc...](https://github.com/r-neal-kelly/nkr/commit/8a3ad4f3bcad684fdc0073a3981b58b8f9a1fe86)
#### Monday 2022-04-11 23:07:24 by r-neal-kelly

updated the api for the new local dynamic array. I'm pretty sure I want these more explicit names to help remind the programmer and the reader what the hell they're doing. Reading occurs way more often than writing, so I don't accept the excuse that it's annoying to type more. It's annoying to read, re-read, and still not get what the hell a piece of code is doing, I'm admant about this. Also, I don't really want to treat my users like children. I'm going to provide a way to directly edit the unit count of the array so that they can easily manipulate it through the api, which is way easier to search for than custom hacks.

---
## [UnderAGeode/tgstation](https://github.com/UnderAGeode/tgstation)@[ac21ef9078...](https://github.com/UnderAGeode/tgstation/commit/ac21ef9078d88f51a4e198e394ed56e3cc731b45)
#### Monday 2022-04-11 23:52:04 by Pickle-Coding

No, we don't want radiation getting released in large pipenets fuck you fuckr uyu! (#65212)

* Make it harder to release radiation in large pipenets. Squares the volume / 2,500 thingy, and adds the requirements to the proto-nitrate bz response and proto-nitrate tritium response gas reactions to release radiation. This will make it significantly harder to release radiation in large pipenets, because releasing radiation in large pipenets makes it harder for people to identify the cause on why they are getting irradiated, which is bad and goes against the modern radiation goals.

Squaring is not enough for deranged people that know we don't want radiation released in large pipenets. Cubes the requirement instead. If someone could get enough gases reacting at once after this, then there is a bigger problem with atmos.

Who had fun seeing everything green, then getting irradiated and not even knowing why? I don't know, because I don't know who put the gases in waste and why we must suffer.

---

