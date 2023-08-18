## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-17](docs/good-messages/2023/2023-08-17.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,305,310 were push events containing 3,442,810 commit messages that amount to 250,469,209 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 66 messages:


## [stemnic/binutils-gdb](https://github.com/stemnic/binutils-gdb)@[05e1cac249...](https://github.com/stemnic/binutils-gdb/commit/05e1cac2496f842f70744dc5210fb3072ef32f3a)
#### Thursday 2023-08-17 00:00:19 by Andrew Burgess

gdb: fix vfork regressions when target-non-stop is off

It was pointed out on the mailing list[1] that after this commit:

  commit b1e0126ec56e099d753c20e91a9f8623aabd6b46
  Date:   Wed Jun 21 14:18:54 2023 +0100

      gdb: don't resume vfork parent while child is still running

the test gdb.base/vfork-follow-parent.exp now has some failures when
run with the native-gdbserver or native-extended-gdbserver boards:

  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to end of inferior 2 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: inferior 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: print unblock_parent = 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to break_parent (timeout)

The reason that these failures don't show up when run on the standard
unix board is that the test is only run in the default operating mode,
so for Linux this will be all-stop on top of non-stop.

If we adjust the test script so that it runs in the default mode and
with target-non-stop turned off, then we see the same failures on the
unix board.  This commit includes this change.

The way that the test is written means that it is not (currently)
possible to turn on non-stop mode and have the test still work, so
this commit does not do that.

I have also updated the test script so that the vfork child performs
an exec as well as the current exit.  Exec and exit are the two ways
in which a vfork child can release the vfork parent, so testing both
of these cases is useful I think.

In this test the inferior performs a vfork and the vfork-child
immediately exits.  The vfork-parent will wait for the vfork-child and
then blocks waiting for gdb.  Once gdb has released the vfork-parent,
the vfork-parent also exits.

In the test that fails, GDB sets 'detach-on-fork off' and then runs to
the vfork.  At this point the test tries to just "continue", but this
fails as the vfork-parent is still selected, and the parent can't
continue until the vfork-child completes.  As the vfork-child is
stopped by GDB the parent will never stop once resumed, so GDB refuses
to resume it.

The test script then sets 'schedule-multiple on' and once again
continues.  This time GDB, in theory, resumes both the parent and the
child, the parent will be held blocked by the kernel, but the child
will run until it exits, and which point GDB stops again, this time
with inferior 2, the newly exited vfork-child, selected.

What happens after this in the test script is irrelevant as far as
this failure is concerned.

To understand why the test started failing we should consider the
behaviour of four different cases:

  1. All-stop-on-non-stop before commit b1e0126ec56e,

  2. All-stop-on-non-stop after commit b1e0126ec56e,

  3. All-stop-on-all-stop before commit b1e0126ec56e, and

  4. All-stop-on-all-stop after commit b1e0126ec56e.

Only case #4 is failing after commit b1e0126ec56e, but I think the
other cases are interesting because, (a) they inform how we might fix
the regression, and (b) it turns out the behaviour of #2 changed too
with the commit, but the change was harmless.

For #1 All-stop-on-non-stop before commit b1e0126ec56e, what happens
is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-non-stop, every thread is resumed
    individually, so GDB tries to resume both the vfork-parent and the
    vfork-child, both of which succeed,

  3. The vfork-parent is held stopped by the kernel,

  4. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  5. At this point we might take two paths depending on which event
     GDB handles first, if GDB handles the VFORK_DONE first then:

     (a) As GDB is controlling both parent and child the VFORK_DONE is
         ignored (see handle_vfork_done), the vfork-parent will be
	 resumed,

     (b) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     Alternatively, if GDB selects the EXITED event first then:

     (c) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     (d) At some future time the user resumes the vfork-parent, at
         which point the VFORK_DONE is reported to GDB, however, GDB
	 is ignoring the VFORK_DONE (see handle_vfork_done), so the
	 parent is resumed.

For case #2, all-stop-on-non-stop after commit b1e0126ec56e, the
important difference is in step (2) above, now, instead of resuming
both the vfork-parent and the vfork-child, only the vfork-child is
resumed.  As such, when we get to step (5), only a single event, the
EXITED event is reported.

GDB handles the EXITED just as in (5)(c), then, later, when the user
resumes the vfork-parent, the VFORKED_DONE is immediately delivered
from the kernel, but this is ignored just as in (5)(d), and so,
though the pattern of when the vfork-parent is resumed changes, the
overall pattern of which events are reported and when, doesn't
actually change.  In fact, by not resuming the vfork-parent, the order
of events (in this test) is now deterministic, which (maybe?) is a
good thing.

If we now consider case #3, all-stop-on-all-stop before commit
b1e0126ec56e, then what happens is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-all-stop, the resume is passed down to the
     linux-nat target, the vfork-parent is the event thread, while the
     vfork-child is a sibling of the event thread,

  3. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this causes the vfork-child to be resumed.  Then
     in linux_nat_target::resume, the event thread, the vfork-parent,
     is also resumed.

  4. The vfork-parent is held stopped by the kernel,

  5. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  6. We are now in a situation identical to step (5) as for
     all-stop-on-non-stop above, GDB selects one of the events to
     handle, and whichever we select the user sees the correct
     behaviour.

And so, finally, we can consider #4, all-stop-on-all-stop after commit
b1e0126ec56e, this is the case that started failing.

We start out just like above, in proceed, the resume_ptid is
-1 (resume everything), due to schedule multiple being on.  And just
like above, due to the target being all-stop, we call
proceed_resume_thread_checked just once, for the current thread,
which, remember, is the vfork-parent thread.

The change in commit b1e0126ec56e was to avoid resuming a vfork-parent
thread, read the commit message for the justification for this change.

However, this means that GDB now rejects resuming the vfork-parent in
this case, which means that nothing gets resumed!  Obviously, if
nothing resumes, then nothing will ever stop, and so GDB appears to
hang.

I considered a couple of solutions which, in the end, I didn't go
with, these were:

  1. Move the vfork-parent check out of proceed_resume_thread_checked,
     and place it in proceed, but only on the all-stop-on-non-stop
     path, this should still address the issue seen in b1e0126ec56e,
     but would avoid the issue seen here.  I rejected this just
     because it didn't feel great to split the checks that exist in
     proceed_resume_thread_checked like this,

  2. Extend the condition in proceed_resume_thread_checked by adding a
     target_is_non_stop_p check.  This would have the same effect as
     idea 1, but leaves all the checks in the same place, which I
     think would be better, but this still just didn't feel right to
     me, and so,

What I noticed was that for the all-stop-on-non-stop, after commit
b1e0126ec56e, we only resumed the vfork-child, and this seems fine.
The vfork-parent isn't going to run anyway (the kernel will hold it
back), so if feels like we there's no harm in just waiting for the
child to complete, and then resuming the parent.

So then I started looking at follow_fork, which is called from the top
of proceed.  This function already has the task of switching between
the parent and child based on which the user wishes to follow.  So, I
wondered, could we use this to switch to the vfork-child in the case
that we are attached to both?

Turns out this is pretty simple to do.

Having done that, now the process is for all-stop-on-all-stop after
commit b1e0126ec56e, and with this new fix is:

  1. GDB calls proceed with the vfork-parent selected, but,

  2. In follow_fork, and follow_fork_inferior, GDB switches the
     selected thread to be that of the vfork-child,

  3. Back in proceed user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid still, but now,

  4. When GDB calls proceed_resume_thread_checked, the vfork-child is
     the current selected thread, this is not a vfork-parent, and so
     GDB allows the proceed to continue to the linux-nat target,

  5. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this does not resume the vfork-parent (because
     it is a vfork-parent), and then the vfork-child is resumed as
     this is the event thread,

At this point we are back in the same situation as for
all-stop-on-non-stop after commit b1e0126ec56e, that is, the
vfork-child is resumed, while the vfork-parent is held stopped by
GDB.

Eventually the vfork-child will exit or exec, at which point the
vfork-parent will be resumed.

[1] https://inbox.sourceware.org/gdb-patches/3e1e1db0-13d9-dd32-b4bb-051149ae6e76@simark.ca/

---
## [crawl/crawl](https://github.com/crawl/crawl)@[d9f7f4a579...](https://github.com/crawl/crawl/commit/d9f7f4a579bb79df554f5caec212a10434edd021)
#### Thursday 2023-08-17 00:20:22 by Nicholas Feinberg

Feat: hot pursuit (elliptic)

Not to be confused with the similar-sounding apparel beloved of
certain players, 'hot pursuit' is a new mechanic to encourage fun
lines of play.

A Brief History
---------------

When in a very nasty spot (low on HP and next to a tough foe), players
have historically been able to 'pillar-dance', wasting time (both the
game's and theirs) to get time to heal. This is both unfun to do and
narratively unsatisfying. When in a tight spot, players should pull out a
cool trick (a spell, god ability or consumable), fight, and/or die!

We first tried to fix this by adding 'random energy', which unfortunately
fixed nothing. Then we tried 'attacks of opportunity', letting monsters
attack when the player moved away. These worked somewhat, but had several
disadvantages, including:

- They were very complex. The list of special cases for which monsters
  could attack the player and when was very long, and it was hard for
  players to track.
- They were very binary. If a monster was next to the player, danger was
  vastly higher than if they were 2 tiles away. If a monster was as fast
  as the player, danger was vastly higher than if they were just a bit
  slower.
- They had odd and unintuitive interactions with polearms (which didn't
  launch reaching attacks of opportunity).
- They were frustrating. Players felt profoundly unhappy when they were
  killed by attacks of opportunity - it felt like the game becoming more
  hostile.

So, let's try something a bit gentler

Hot Pursuit
-----------

When the player moves away from a monster, if that monster then moves
toward the player, they have a one in 20 chance of putting on a 'burst of
speed', moving ~25% faster (move delay 0.8) for the next ~40ish turns.
This speed bonus affects the move that triggered it, so players walking
away from an adjacent yak have a 1% chance of getting a surprise bap
from them.

The intent is to again discourage 'pillar-dancing' and other fiddly
stalling tactics (e.g. running across the entire level to get to stairs)
in a 'softer', fuzzier way, without the hard binaries of attacks of
opportunity.

Wu Jian martial manuevers and Serpent's Lash again give immunity to
this effect.

Let's try it out!

---
## [sjp38/linux](https://github.com/sjp38/linux)@[7cae79efd4...](https://github.com/sjp38/linux/commit/7cae79efd4f896c4e5101a4074711e71460e0530)
#### Thursday 2023-08-17 00:51:49 by David Hildenbrand

smaps: use vm_normal_page_pmd() instead of follow_trans_huge_pmd()

We shouldn't be using a GUP-internal helper if it can be avoided.

Similar to smaps_pte_entry() that uses vm_normal_page(), let's use
vm_normal_page_pmd() that similarly refuses to return the huge zeropage.

In contrast to follow_trans_huge_pmd(), vm_normal_page_pmd():

(1) Will always return the head page, not a tail page of a THP.

 If we'd ever call smaps_account with a tail page while setting "compound
 = true", we could be in trouble, because smaps_account() would look at
 the memmap of unrelated pages.

 If we're unlucky, that memmap does not exist at all. Before we removed
 PG_doublemap, we could have triggered something similar as in
 commit 24d7275ce279 ("fs/proc: task_mmu.c: don't read mapcount for
 migration entry").

 This can theoretically happen ever since commit ff9f47f6f00c ("mm: proc:
 smaps_rollup: do not stall write attempts on mmap_lock"):

  (a) We're in show_smaps_rollup() and processed a VMA
  (b) We release the mmap lock in show_smaps_rollup() because it is
      contended
  (c) We merged that VMA with another VMA
  (d) We collapsed a THP in that merged VMA at that position

 If the end address of the original VMA falls into the middle of a THP
 area, we would call smap_gather_stats() with a start address that falls
 into a PMD-mapped THP. It's probably very rare to trigger when not
 really forced.

(2) Will succeed on a is_pci_p2pdma_page(), like vm_normal_page()

 Treat such PMDs here just like smaps_pte_entry() would treat such PTEs.
 If such pages would be anonymous, we most certainly would want to
 account them.

(3) Will skip over pmd_devmap(), like vm_normal_page() for pte_devmap()

 As noted in vm_normal_page(), that is only for handling legacy ZONE_DEVICE
 pages. So just like smaps_pte_entry(), we'll now also ignore such PMD
 entries.

 Especially, follow_pmd_mask() never ends up calling
 follow_trans_huge_pmd() on pmd_devmap(). Instead it calls
 follow_devmap_pmd() -- which will fail if neither FOLL_GET nor FOLL_PIN
 is set.

 So skipping pmd_devmap() pages seems to be the right thing to do.

(4) Will properly handle VM_MIXEDMAP/VM_PFNMAP, like vm_normal_page()

 We won't be returning a memmap that should be ignored by core-mm, or
 worse, a memmap that does not even exist. Note that while
 walk_page_range() will skip VM_PFNMAP mappings, walk_page_vma() won't.

 Most probably this case doesn't currently really happen on the PMD level,
 otherwise we'd already be able to trigger kernel crashes when reading
 smaps / smaps_rollup.

So most probably only (1) is relevant in practice as of now, but could only
cause trouble in extreme corner cases.

Let's move follow_trans_huge_pmd() to mm/internal.h to discourage future
reuse in wrong context.

Link: https://lkml.kernel.org/r/20230803143208.383663-3-david@redhat.com
Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Signed-off-by: David Hildenbrand <david@redhat.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Jason Gunthorpe <jgg@ziepe.ca>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: liubo <liubo254@huawei.com>
Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
Cc: Mel Gorman <mgorman@suse.de>
Cc: Paolo Bonzini <pbonzini@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Shuah Khan <shuah@kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[3c083fbf19...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/3c083fbf197dca0adabd3c85659e68ac8fbb1367)
#### Thursday 2023-08-17 01:16:32 by DaydreamIQ

Buffs Heretic ash ascension (#77618)

## About The Pull Request

Post-Ascension the Nightwatchers Rebirth (Or Fiery Rebirth) has its
cooldown lowered from 60 seconds to 10
Additionally adds bomb immunity to the list of resistances that
ascension provides

## Why It's Good For The Game

Ash ascension kind of sucks when compared to its big brothers flesh,
rust and blade. You do get a couple of cool spells but their impact is
negated by how shitty fire damage is and while you get a ton of
resistances, you don't get stun immunity and have absolutely zero
sustainability in long-term engagements.

Blade has its lifesteal, rust has its leeching walk and flesh has a big
worm that eats arms. And while the laziest solution would be to give ash
stun immunity like those three I think it'd be more fitting if it could
capitalize on one of its more powerful spells. Keeping in the fight by
siphoning health from all those people you lit on fire with your cascade
instead of watching in pain as they completely negate any threat you
have with a fire extinguisher and temp adapt.

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[f78dd2d42f...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/f78dd2d42f0cd79b6e089317ba45514157aea583)
#### Thursday 2023-08-17 01:16:40 by san7890

Fixes Ticked File Enforcement and Missing Unit Test (and makes said Unit Test Compile) (and genericizes the C&D list to the base unit test datum) (#77632)

Closes #77631

## About The Pull Request

Hey there,

Ticked File Enforcement simply wasn't catching files that were missed.
That's a bit stupid, so I decided to look into what the issue might be,
and whoopsie daisies I did double periods back in #76592
(020ac2405308eab83f314282499dfe777aba5874).

![image](https://github.com/tgstation/tgstation/assets/34697715/6023afe8-313d-4550-9a60-58a8bc211b4f)

I also added some debug info and some more checks to prevent such a
break from happening again on runtime of this script. I thought it was a
weird string concatenation issue (and not the simple break I thought it
was), so I rewrote how it adds `glob`s. I think it's cleaner so I'll
keep it anyhow

This PR also corrects the oversight of the missing unit test (introduced
in #77218 (69827604c46952dd4393db8617cd494ade17bea2)) by reticking it in
the `_unit_tests.dm` file, and also makes it compile because it didn't
do that.

I also then had to do some more work to get the unit test to work.
* Genericizes the Create-and-Destroy "ignore" list to be a static list
on `/datum/unit_test` to allow it to be shared between these types of
tests that we need to test.
* Adds that list to C&D and the broken unit test regarding fantasy
bonuses
* Fixes some actually broken that the unit test was made to catch (beam
rifles, butterdogs and other slippery items, random ingredient boxes).
* Adds cases for things that the unit test and overall framework really
shouldn't be altering anyways (mythril), and was likely causing
inappropriate stack traces on master

## Why It's Good For The Game

Unit Tests WORK. Tools WORK.


![image](https://github.com/tgstation/tgstation/assets/34697715/9a59c0db-7a33-4546-918b-c73372a5b867)


## Changelog

:cl:
fix: Beam rifles will no longer inappropriately retain any bonuses they
may gain from wizardry.
fix: Inappropriate stack traces over bonuses being applied to components
that gain bonuses innately (like Mythril stacks) should cease.
/:cl:

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[dc6ddd821b...](https://github.com/lessthnthree/effigy-se/commit/dc6ddd821b1d9fe4783cf5d05c4ed2aa96f98e89)
#### Thursday 2023-08-17 01:36:26 by Cheshify

North Star Science Rework And More (#77439)

## About The Pull Request
I fixed a few miscellaneous issues and also redid science (mainly
genetics, cytology, and xenobiology)
This is genetics, it's basically the same but moneky have bananas and I
rotated it so they'll be visible from the front desk.

![geneticsnew](https://github.com/tgstation/tgstation/assets/73589390/7c10d75b-2a7a-47b2-a6ca-a30354d713c3)

Holy fuck it's Cytology as a proper area. It now has main hall access
and a public access petting zoo. Now you can show off all your new
creatures (it also has some items cytologists generally want)

![cytonew](https://github.com/tgstation/tgstation/assets/73589390/7d9256c9-b39a-4502-b599-9226a2ca5cd8)

Upstairs is Xenobio, which is now much larger and soulless. Instead of a
normal holding cell there's a prefilled room of oxygen and BZ (the
holding room, why is BZ invisible?)

![xenonew](https://github.com/tgstation/tgstation/assets/73589390/5dc28dba-a051-4858-a9fc-16d51e987c33)

I also gave Ordnance 5 TTVs, same as other maps.
Also the coroner no longer has an unreachable box of bodybags
Also sec now has 2 secways + 2 keys for their usage
## Why It's Good For The Game
I'm forcing xenobiologists to be closer to a hall so they might actually
interact with people, and giving cytologists a reason to do anything
ever because they have a petting zoo to show their creatures off in. Oh
yeah also cytology gets equipment they should just have (a botany tray,
tools to butcher with, a shitty old laser gun to kill experiments gone
wrong)
Genetics is just better because people from the hall can see the
Geneticists working so they can bug them for stuff.

A few of the fixes are very tiny, like moving a few areas by the service
hall and adding a single pipe to the AI SAT
## Changelog
:cl:
qol: North Star's Cytology and Xenobiology are now significantly more
usable.
add: North Star's Genetics has been tweaked.
fix: The North Star's AI SAT has a working vent and it's service hall
has a working lightswitch
/:cl:

---
## [raviqqe/melior](https://github.com/raviqqe/melior)@[f9eece91b7...](https://github.com/raviqqe/melior/commit/f9eece91b7a4991ca1d763a0de09b5872b145bcb)
#### Thursday 2023-08-17 01:38:46 by Daan Vanoverloop

Draft: Dialect generation from ODS (#274)

I've created an early draft of dialect generation based on the [MLIR
Python
Bindings](https://mlir.llvm.org/docs/Bindings/Python/#integration-with-ods).

It's okay if you don't have the time to review this. I admit that
there's quite a lot of ugly and hard to read code (especially the code
dealing with variadic arguments), and it might not be in a state
currently where you would want to maintain it within `melior`, hence I'm
marking it as a draft.

Not much changed since my original implementation mentioned in #262, but
I got a bit stuck on error handling in my TableGen wrapper library
([tblgen-rs](https://gitlab.com/Danacus/tblgen-rs)) and lost motivation
for a while after that. Anyway, I decided to finish what I started,
hence I am making this draft.

To build this branch, you might need to set `TABLEGEN_160_PREFIX` to
match `MLIR_SYS_160_PREFIX`.

I've added the generated dialects in a new `dialect_gen` module for now,
such that they can be compared with the original hand-written bindings
in the `dialect` module.

There are still a few issues:

- [ ] Some parts of the code are hacky and ugly, and may be hard to
read.
- [ ] Type inference is not always detected (but it should be as good as
the Python bindings at least)
- [ ] Need to add tests (already have them in a separate repository)
- [ ] Need to fix some issues with the CI

I wanted complete parity with the existing hand-written dialect
bindings, but there are some things that aren't generated as nicely. For
example, `arith::CmpiPredicate` is not generated and plain `Attribute`
is used instead for `arith::cmpi`. It might be feasible to generate
dialect specific attributes from ODS instead. Or perhaps being able to
write some function manually would be useful.

Currently I generate wrapper types around `Operation` that provide
additional methods, for example:

```rust
        pub struct AddIOp<'c> {
            operation: ::melior::ir::operation::Operation<'c>,
        }
        impl<'c> AddIOp<'c> {
            pub fn name() -> &'static str {
                "arith.addi"
            }
            pub fn operation(&self) -> &::melior::ir::operation::Operation<'c> {
                &self.operation
            }
            pub fn builder(
                location: ::melior::ir::Location<'c>,
            ) -> AddIOpBuilder<'c, AddIOp__No__Lhs, AddIOp__No__Rhs> {
                AddIOpBuilder::new(location)
            }
            pub fn result(&self) -> ::melior::ir::operation::OperationResult<'c, '_> {
                self.operation.result(0usize).expect("operation should have this result")
            }
            pub fn lhs(&self) -> ::melior::ir::Value<'c, '_> {
                self.operation
                    .operand(0usize)
                    .expect("operation should have this operand")
            }
            pub fn rhs(&self) -> ::melior::ir::Value<'c, '_> {
                self.operation
                    .operand(1usize)
                    .expect("operation should have this operand")
            }
        }
```

I then provide implementations of `Into<Operation>` and
`TryFrom<Operation>` to "cast" to and from an `Operation`.

```rust
        impl<'c> TryFrom<::melior::ir::operation::Operation<'c>> for AddIOp<'c> {
            type Error = ::melior::Error;
            fn try_from(
                operation: ::melior::ir::operation::Operation<'c>,
            ) -> Result<Self, Self::Error> {
                Ok(Self { operation })
            }
        }
        impl<'c> Into<::melior::ir::operation::Operation<'c>> for AddIOp<'c> {
            fn into(self) -> ::melior::ir::operation::Operation<'c> {
                self.operation
            }
        }
```

I wonder if it would be better to use an `OperationLike` trait, similar
to `AttributeLike`? That way we wouldn't have to call `operation` or
`into` to use the methods on `Operation`.

On a related note: should we also generate `Ref` (and `RefMut`?) types
for these operation wrappers? It might be useful to be able to cast a
`OperationRef` into a `AddIOpRef`, for example, to more easily analyze
operations in external passes (or even external analyses, which is
something else I'm working on as well:
[mlir-rust-tools](https://gitlab.com/Danacus/mlir-rust-tools)).

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[2d34c7433a...](https://github.com/effigy-se/effigy-se/commit/2d34c7433a0c5315e6a46f7e32e2c9a6c90280b3)
#### Thursday 2023-08-17 01:41:04 by Andrew

New Mech UI and equipment refactor (#77221)

![bWJlVIDO53](https://github.com/tgstation/tgstation/assets/3625094/d75030b5-59e9-43f6-96b4-1b7564caceef)

## About The Pull Request

Made a new UI and refactored some mech code in the process.

Fixes #66048
Fixes #77051
Fixes #65958 ??? if it was broken
Fixes #73051 - see details below
Fixes other undocumented things, see changelog.

## Why It's Good For The Game

The UI was too bulky and Mechs were too complex for no reason. 
Now they follow some general rules shared between other SS13 machinery,
and there is less magic happening under the hood.

## Detailed Changes

### New Mech UI, Air Tank and Radio as separate modules

Previous UI for comparison:

<img alt="9SScrXAOjy"
src="https://github.com/tgstation/tgstation/assets/3625094/904e3d07-e7d7-4d3a-a062-93e0e35b4b66">

Previously mechs came with radio pre-installed and air canisters
magically pre-filled with air even when you build one in fab.
Radio and Air Tanks are now both utility modules that are optional to
install. Gas RCS thrusters still require Air Tank module to operate.

This made the Mechs more barebones when built, giving you only the basic
functionality.

<img alt="5SDMlXTJxv"
src="https://github.com/tgstation/tgstation/assets/3625094/b9364230-49ac-416b-aa70-e851fbf2050e">

To compensate this change, all mechs got two extra utility module slots.

All other modules got new UI. And ore box now shows the list of ores
inside.

<img alt="SRX5FjvsHA"
src="https://github.com/tgstation/tgstation/assets/3625094/cbe2e98d-1cd4-4667-8dae-2f9227b4b265">

### Mounted Radio

Works as a normal radio, but with subspace transmission. Available from
the basic mech research node and can be printed in fab.

### Cabin Sealing

To compensate for the lack of air tank by default, mechs with enclosed
cabin (e.g. all except Ripley) got an ability to toggle cabin exposure
to the outside air. Exiting the mech makes cabin air automatically
exposed.

When you seal the cabin, it traps some of the outside air inside the
cabin and you can breathe with this air to perform a short space trips.
But the oxygen will run out quickly and CO2 will build up.

Sealing the cabin in space will make the cabin filled with vacuum, and
it will stay there until you return to air environment and unseal the
cabin, letting the breathable air to enter. There are temperature and
pressure sensors that turn yellow/red when the corresponding warning
thresholds are reached.

You could also use personal internals in combination with cabin sealing
for long space travels, so Air Tank is completely optional now and
mostly needed when you need RCS thruster.

### RCS thrusters

They are now available earlier in tech tree and consume reasonable
amount of air (5 times more than human jetpacks), and they don't work
without Mounted Air Tank, unless it's an Ion thruster variant.

### Mounted Air Tank

Available from the basic mech research node and can be printed in fab.
Built model comes empty, and syndicate mechs come with one full of
oxygen.

<img alt="GrFDrH5Hwe"
src="https://github.com/tgstation/tgstation/assets/3625094/b677b705-bda0-4c8c-96c7-d32bf7bf9f28">

Can be switched to pressurize or not pressurize the cabin. Releases gas
only when the cabin is sealed shut. Starts releasing automatically, but
can be toggled to not release if you want to use it just as a portable
canister.

Cabin pressure can now be configured in the module UI instead of
Maintenance UI.

Can be attached to a pipe network when the mech is parked above a
connection port.

Comes with a pump that works similarly to the portable pump. It lets you
vent the air tank contents outside, or suck air from the room to fill
the air tank. Intended to provide an ability to fill the air tank
without the need to bother with pipes.

Also has gas sensors that display gas mix data of the tank and the cabin
(when sealed).

### Stock part changes

All mechs now require a servo motor and they reduce mech movement power
consumption instead of scanning module.

Scanning modules are optional for mech operation (still required to
build) and the lack of one disables the following UI elements:

- Display of mech integrity (you can still see the alerts or examine the
mech to get rough idea)
- Display of mech status on internal damage (and you can't repair what
you can't diagnose)

The rating of scanning module doesn't have any effect as of now.

Cargo mech comes without it roundstart.

<img alt="2vDtt99oqb"
src="https://github.com/tgstation/tgstation/assets/3625094/147144ca-824e-4501-acf5-6ee104f309e7">

Capacitors now also reduce light power usage and raise the overclocking
temperature thresholds (see below).

### Maintenance

Maintenance UI removed, and its logic migrated to other places.

Access modification now managed inside the mech, and anyone who can
control the mech, can adjust the access in the same way as they can set
DNA key.

To open the maintenance panel you just need a screwdriver. It is instant
when the mech is empty and it has a 5 second delay when there is an
occupant to avoid in-combat hacking and part removal. It will alert the
occupant that someone is trying to tinker with their mech.


![image](https://github.com/tgstation/tgstation/assets/3625094/1abfca3c-8ba9-44b0-913c-c209564b91fd)

Once the panel is open, you can see the part ratings:


![image](https://github.com/tgstation/tgstation/assets/3625094/404f95bb-9f74-4e5b-a975-5ab6f74bdfa9)

With open panel you can hack the mech wires (roboticists can now see
them):

<img alt="mj205G2qDa"
src="https://github.com/tgstation/tgstation/assets/3625094/44cea0d1-44b4-4b50-b1d3-a97c0056bab3">

There are wires for:
- Enabling/Disabling ID and DNA locks
- Toggling mech lights
- Toggling mech circuits malfunction (battery drain, sparks) 
- Toggling mech equipment malfunction (to repair after EMP or cause
EMP-like effect, disarming mech)
- 3 dud wires that do nothing

The hacker may be shocked if the mech power cell allows.

When the panel is open and the user has access to the mech, they can
remove parts with a crowbar:

<img alt="jR40gyTWtJ"
src="https://github.com/tgstation/tgstation/assets/3625094/b573f5b9-b8ea-412e-b3e0-c872e01e0c23">

Hitting the mech with an ID from outside now toggles the ID Lock on/off
if the ID has sufficient access.

### Power consumption and overclocking

Rebalanced mech power consumption. T4 parts were not working in
Syndicate Mechs, as their effect was not calculated until you manipulate
parts manually. Constructed mechs with t1 parts even had their energy
drain reduced with upgrade to t1.

Now all mechs apply their base step power usage correctly don't ignore
the stock parts.

Servo tier now reduces base power consumption by 0% at t1, 50% at t2,
33% at t3 and 25% at t4
Capacitor tier now reduces base power consumption of mele attacks,
phasing and light by the same amounts.

Gygax leg actuators overload replaced with mech overclocking. Any mech
can be overclocked by hacking wires, but only Gygax has a button for
toggling it from the Cabin.

Now there is an overclock coefficient. 1.5 for Gygax and other mechs, 2
for Dark Gygax.

When overclocked, mechs moves N times faster, but consumes N times more
power.


![image](https://github.com/tgstation/tgstation/assets/3625094/01e285fd-6fd6-4558-8277-2ed3abf474d8)

While overclocked, mech heats up every second, regardless of movement,
and starts receiving internal and integrity damage after a certain
temperature threshold. The chance is 0% at the threshold, and 100% at
thresholds * 2. The roll happens every tick. Capacitor upgrades this
threshold, letting you overclock safely for longer periods.


![image](https://github.com/tgstation/tgstation/assets/3625094/80d90cea-0d20-4054-9369-a47deb6f52f2)

When you stop overclock, the temperature goes back down.

### Other changes and fixes

Concealed weapon bay now doesn't show up when you examine the mech, so
it's actually concealed now.

New radio module can properly change its frequency, as it didn't work
for previous radio.

Launcher type weapons were ignoring cooldowns and power usage, so you
could spam explosive banana peals, while they should have a 2 second
cooldown:
<img alt="q5GjUsHwGr"
src="https://github.com/tgstation/tgstation/assets/3625094/d102725d-e9e1-4588-9d6c-b9e38b7a6535">

Now this is fixed and all launcher type weapons properly use power and
have their cooldowns working.
And now they have the kickback effect working (when it pushes you in the
opposite direction in zero gravity on throw).

Thermoregulator now heats/cools considering heat capacity instead of
adding/reducing flat 10 degrees. So you can heat up cabin air quicker if
the pressure is low.

There were some other sloppy mistakes in mech code, like some functions
returning too early, blocking other functionality unintentionally. Fixed
these and made some other minor changes and improvements.

## Changelog

:cl:
refactor: Refactored Mech UI
refactor: Refactored mech radio into a utility module, adding extra slot
to all mechs
refactor: Refactored mech air tank into a utility module with an air
pump, adding extra slot to all mechs
refactor: Refactored mech cabin air - there is now a button to seal or
unseal cabin to make it airtight or exchanging gases with the
environment
refactor: Removed mech maintenance UI Access is set in mech UI, and
parts are ejected with a crowbar
add: Mech now has wires and can be hacked
qol: Roboticists now can see MOD suit and mech wires
add: Mechs now require servo motor stock part and it affects movement
power usage instead of scanning module
add: Scanning module absence doesnt block mech movement and hides some
UI data instead. Big Bess starts without one.
qol: Hitting mech with ID card now toggles ID lock on/off if the card
has required access
fix: Fixed concealed weapon bay not being concealed on mech examine
fix: Fixed mech radio not changing frequency
fix: Fixed mech launcher type weapons ignoring specified cooldown
fix: Fixed mech launcher type weapons not using specified power amount
fix: Fixed mech temperature regulator ignoring gas heat capacity
fix: Fixed mech stopping processing other things while not heating
internal air
fix: Fixed mech being able to leave transit tube in transit
fix: Fixed mech internal damage flags working incorrectly
fix: Fixed Gygax leg overloading being useless
fix: Fixed mechs ignoring their stock parts on creation. Syndicate mechs
now stronger against lasers and consume less energy on move. Upgrading
from tier 1 to tier 2 doesn't make mech consume MORE energy than before
the upgrade.
balance: Rebalanced mech energy drain with part upgrades. Base energy
drain reduced by 50%, 33%, 25% with upgrades and applies to movement
(Servo rating), phasing, punching, light (Capacitor rating).
balance: Hydraulic clamp now can force open airlocks
balance: Made mech RCS pack consume reasonable amount of gas
code: Fixed some other minor bugs and made some minor changes in the
mech code
/:cl:

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [t0nysama/tonystation](https://github.com/t0nysama/tonystation)@[72174845f5...](https://github.com/t0nysama/tonystation/commit/72174845f5b417bf0cbd3f4a8fc66835b052acf8)
#### Thursday 2023-08-17 02:03:26 by Jacquerel

Basic Watchers & Basilisks (#77630)

## About The Pull Request

This one is a double feature because Watchers and Basilisks share the
same typepath. You might see a couple more of those.
As is tradition I decided to fuck with them rather than just port them.
Here's what's up.

**Basilisks**

![image](https://github.com/tgstation/tgstation/assets/7483112/9e4b0115-65dd-4df7-b62a-21c7be8549bf)

![image](https://github.com/tgstation/tgstation/assets/7483112/59162e68-7d73-4659-9531-5078ff751228)

- Have a new soulless sprite which looks less like a living blue hedge.
- Walk at you and shoot you while you are not in range (just like
before).
- Become supercharged if they become "heated" by lava, lasers, or
temperature weapons. This was a feature they also previously had but
they would never encounter lava, so now it also works if you use the
wrong gun on them.
- Lose their supercharge if you cool them down.
- Otherwise pretty normal mobs.

**Watchers**

https://www.youtube.com/watch?v=kOq_Bf78k5A
Here's a traditional video of me intentionally getting hit by mechanics
(trust me its definitely on purpose)

- They glow emmissively a little bit so you can see them from further
away.
- Their eyes light up about 0.5 seconds before they are able to shoot at
you.
- No longer melee attack, instead try to stay out of melee.
- Will occasionally put you into "Overwatch", meaning they will shoot
you rapidly if you move or act while they're staring at you for a brief
time period (after which you become immune for 12 seconds, and during
which other watchers will play fair and stop shooting at you).
- If they start taking damage they will also start using their "Gaze"
attack, look away or suffer some kind of negative effect!
- - Normal watcher gaze flashes and confuses you.
- - Magmawing watcher gaze obviously burns (and briefly stuns) you.
- - Icewing watcher gaze freezes you and throws you backwards.
- Magnetically attract and eat diamonds. They also used to do this, but
just if they happened to coincidentally walk past some.

**Other accompanying changes**

All basic mobs will now adopt the "stop gliding" trait if they get
slowed down too much.
I moved behaviour for "fire a projectile from this atom" into a helper
proc because I was using it in three places and I will probably use it
in more places. There are probably other places in the existing code
which could be using this.
I think I made the basic mob melee attack forecast default a little more
forgiving, they were fucking me up too much and I am the playtester.

## Why It's Good For The Game

Another one off the list.
New tricks for old dogs.
Framework for making mobs with ranged attacks "fairer" (you can see when
they are ready to shoot you).
More (hopefully) versatile AI behaviours which we will reuse later (I
hope I'm not duplicating one someone already made).
If our players "enjoy" them enough we can give more mobs "don't look at
me" mechanics.
Removes some soul sprites.

## Changelog

:cl:
refactor: Basilisks and Watchers now use the basic mob framework. Please
bug report any unusual behaviour.
sprite: Basilisks have new sprites.
add: Basilisks will go into a frenzy if heated by energy weapons or
temperature beams as well as by lava.
add: Watcher eyes will be illuminated briefly when they are ready to
fire at you.
add: Watchers can now briefly put you into "Overwatch" and penalise you
for moving while they can see you.
add: Wounded watchers will occasionally punish players who look at them.
balance: Unusual watcher variants are more likely to appear.
/:cl:

---
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[74892ae7ec...](https://github.com/GuillaumePrata/tgstation/commit/74892ae7ec80d47c64bf786f62985a1bd07d06f7)
#### Thursday 2023-08-17 02:18:34 by LemonInTheDark

Optimization pass focused on foam code (saves about 30% of cpu usage I think) (#76104)

## About The Pull Request

Foam is crummy at high load rn, both because it runs on a low priority
background subsystem, and because it wastes a bit of time.
Let's reduce usage (while speeding up a bunch of other stuff too), and
give it more cpu generally.

[Optimizes reagent processing
somewhat](https://github.com/tgstation/tgstation/commit/d409bd4afc3c208cd6f00ff406e1e9f78d5ac5ad)

Turns out most of the cost of foam is the reagents it carries, and the
varying effects they have
I'm doing my best here to optimize them without touching "user space"
too much

That means doing things like prechecking if we're gonna spawn on top of
an existing decal (from glitter, flour, etc), and using that same proc
to also avoid spawning on unacceptable turfs (I had to convert
inheritance to a bitflag system to make this work, but I think that's ok
since we want it imparative anyhow)

It's actually nice for code quality too, since it lets me clean up code
that was using raw locates and weird var pong.
god I wish I had implied types man

[Optimizes foam spreading in its most accursed aspect, reagent
copying](https://github.com/tgstation/tgstation/commit/5cc56a64ad1a22ba7467cb0446b9558560259437)

Holy shit reagent code is a lot.

I'm doing a bunch of small things here. istype in init -> typecache,
removing procs that are called once and loop over a list we JUST looped
over (ph and the caching for reactions in particular)

I am mainly trying to optimize copy_to here, since that's what foam
spams
As a part of this, I removed a pair of update_total and handle_reactions
calls that were done on the reagents we are copying FROM

I have no god damn idea why you would want to do that, but if anything
is relying on the copy proc modifying the source, then that code
deserves to break

Speaking of, I cleaned up handle_reaction's main filter loop a lot,
removed a lot of redundant vars and changed it from a full loop w
tracker vars to an early exit pattern

This meant using a loop label, which is unfortunate, but this is the
fastest method, and it does end up cleaning up the code significantly,
Which is nice

Oh also I made the required_other var function even if there is no atom
attached to the reaction, since I don't see why it wouldn't

This last bit is gonna get a bit esoteric so bear with me

Failing calls (which are most of them) to handle_reactions are going to
be fastest if they need to check as few reactions as possible

One reagent in a reaction's required list is marked as the "primary",
and thus gets to trigger checking it.
We need all the reagents to react anyhow, so we might as well only check
if we have one particular one to avoid double checking

Anyhow, in order to make most calls the fastest, we want these reactions
distributed as evenly as possible across all our reagents.
The current way of doing this is just taking the first reagent in the
requirements list and using it, which is not ideal

Instead of that, lets figure out how many reactions each reagent is in,
then divy reactions up based off that and the currently divvied
reactions

This doubles the reagent index count, and takes the most common reagent,
water, from 67 reactions to I think like 22

Does some other general cleaning in reagent code too, etc etc etc

[Fixes runtimes from the forced gravity element being applied more then
once](https://github.com/tgstation/tgstation/commit/941d0676114fd455a585f2c65ffc79b81e8438b7)

I feel like this element should take a trait source or something to make
them potentially unique, it's too easy to accidentally override one with
another

[Removes connect_loc usage in atmos_sensitive, replaces it with direct
reg/unreg](https://github.com/tgstation/tgstation/commit/de1c76029d5c49dff152f0ea168b9e6c4a4a04aa)

I only really used it because I liked the componentization, but it costs
like 0.2 seconds off init alone which is really stupid, so let's just do
this the very slightly harder way

[Micros foam code slightly by inlining a LinkBlockedWithAccess
call](https://github.com/tgstation/tgstation/commit/744da3694cd4a85b3bdf44d754de57d7570bdd1c)

This is in the space of like 0.05 seconds kinda save so I can put it
back if you'd like, the double loop just felt silly

[Changes how foam processes
slightly](https://github.com/tgstation/tgstation/commit/ee5e633e3256fe7df229af71d78424d502459c16)

Rather then treating spreading and processing as separate actions, we do
both in sync.
This makes foam fade faster when spreading, which is good cause the
whole spread but unclearing foam thing looks silly.
It also avoids the potential bad ending of foam spreading into itself,
backwards and forwards. This is better I promise.

[Bumps fluid priority closer to heavy eaters, moves it off
background](https://github.com/tgstation/tgstation/commit/811797f09db7b060f75f15ad06d0ce8982375f47)

Also fixes a bug where foam would travel under public access airlocks.

## Why It's Good For The Game

Saves a lot of cpu just in general, from both init and live.
In theory makes foam faster, tho I'd have to test that on live at
highpop to see if I've actually succeeded or not. Guess we'll see.

---
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[63d6c2e962...](https://github.com/GuillaumePrata/tgstation/commit/63d6c2e9628be7af04948f59488043f109f1faab)
#### Thursday 2023-08-17 02:18:34 by CRITAWAKETS

Adds in the smoothbore disablers. (#76773)

## About The Pull Request

This PR adds in a craftable smoothbore disabler, a pistol companion to
the lethal laser musket. Unlike the musket, it fires a disabler shot.
Singular. Weak in armor too. After you fire it, you've gotta crank it,
but only one crank.

The good thing about it is that you can simply add more smoothbores to
your inventory, and use 4 of them to take down a target.

The bad thing is that it's a smoothbore (which for an energy weapon,
means no lens is installed). It has 22.5 degrees of inaccuracy. Have
fun.

Militia Men start with a holster containing two of these, fitting with
their equipment. But of course, the Militia General has an upgraded
laser musket, so... He needs a better smoothbore too.

**INTRODUCING THE ELITE SMOOTHBORE DISABLER**
Using ANCIENT TECHNOLOGIES and PURE BLING, you can fire TWO shots, not
be weak against armour AND have actual accuracy (and a +5 damage boost
because i figured why the hell not). This is the strongest upgraded
variant of the shitty maint guns, so the tome to craft it is currently
unavailable. I want someone to figure out a creative way to put it
somewhere that isn't just a random spawn in maintenance.


![image](https://github.com/tgstation/tgstation/assets/13697285/02c396b8-4b72-45f8-b471-a006df132aff)

The Militia General only has one elite smoothbore. It's too rare and
powerful to simply have two. Even though a regular disabler is better in
every way.

Smoothbore Disabler Recipe:
1x Weapon Stock
5x Cable Coil
1x Pipe
1x Micro-Laser
1x Power Cell
1x Mouse Trap
Needs: Screwdriver, Wrench. Takes 10 seconds to make.

Elite Smoothbore Disabler Recipe:
1x Smoothbore Disabler
5x Gold Ingots/Sheets
1x Hyper-Capacity Power Cell
10u Tempomyocin
Needs: Screwdriver. Takes 20 seconds to make.
Recipe requires recipe book.

## Why It's Good For The Game

Having a sidearm to go with your laser musket is neat, alongside the
fact that it just allows following up on someone. I don't have much to
say honestly, I just think it's neat. Also the idea of an assistant
going FULL BLACKBEARD, carrying 4 pistols and having to toss them away
in order to shoot again cracks me up.

Oh and this is the part for coders: I've de-spaghettified some code with
the maint gun recipe granters, and the gun crank is now a component.
It's likely you could use it on any item that sends the proper signal,
so I kind of overbuilt it on purpose.

Also the attack_self on guns now returns parent. This should allow it to
send a signal alongside putting your grubby fingerprints on the weapon
when you switch modes. There could be bugs but they should be easy to
fix if they pop up, mode switching on guns works without a fuss.

## Changelog

:cl:
add: Added the smoothbore disabler and it's prime variant. You can now
craft a disabler with only one shot and terrible accuracy.
code: Gun cranking has been made a component and could theoretically be
used on more than guns.
/:cl:

---
## [GuillaumePrata/tgstation](https://github.com/GuillaumePrata/tgstation)@[063bf74f31...](https://github.com/GuillaumePrata/tgstation/commit/063bf74f31a27ec8096fe10b844d5883be6d13a9)
#### Thursday 2023-08-17 02:18:34 by carlarctg

There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

## About The Pull Request

There is no longer a 50% chance of catching a heretic out when examining
them drawing influences.

## Why It's Good For The Game

> There is no longer a 50% chance of catching a heretic out when
examining them drawing influences

This is a bad thing for several reasons.

1. It means the heretic will most often be caught out at the very start
of the shift, when they are weakest and most vulnerable.
Heretics already have it hard enough, adding yet another source of
stress is undue.

2. It has no effective counter.
What are you going to do? Not draw any influences? That shouldn't be the
'counter'. The influence drawing period is meant to parallel the crew
prepping period, the traitor rep-collecting period, etc.

3. In a way, it's more blatant than Codex Cicatrix drawing.
Codexi show up as a normal item in your hand. This instead shows a huge
flashing glowing neon rainbow text that says THIS IS A HERETIC. SHRIEK
IN RADIO AND VALID.

4. It's badly designed, and can be manipulated way too easily to always
show.
Examine a target thrice and you're pretty much guaranteed to see if they
are indeed drawing or not. You can just keep rolling the 50% chance.

5. It feels random and unfair for the heretic to die to it.
I've seen this happen and it sucks. There's no sign for heretics that
they have a risk of being found out when examined, which means that this
is just an extremely rare occurrence that you try to ignore *could*
happen 99% of the time, and feel like shit the 1% of the time it
backfires.

## Changelog

:cl:
del: There is no longer a 50% chance of catching a heretic out when
examining them drawing influences.
/:cl:

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[7f1d53e719...](https://github.com/IndieanaJones/tgstation/commit/7f1d53e719d8d097e8af41b9b80a829b84b105ce)
#### Thursday 2023-08-17 02:52:49 by Ben10Omintrix

convert the eyeball a basic monster (#77411)

## About The Pull Request
I have created a basic eyeball monster with new abilities and behaviors.
The eyeball has a unique power that allows it to glare at humans and
make them slow for a short period. However, this ability only works if
the human can see the eyeball monster. If a person is blind or unable to
see the eyeball, the ability won't affect them. Also, if someone turns
their back to the eyeball, it cannot use the ability on them. But be
cautious because the eyeball will try to position itself in front of the
person's face to use its power.

The eyeball is hostile towards all humans except for the blind ones and
those with significant eye damage. It has a compassionate side too, as
it loves to help people with eye damage by providing small healing to
their eyes.

Furthermore, the eyeball has a fondness for eating carrots, which not
only satisfies its appetite but also grants it a small health boost. To
add to its appearance, I've given it a new, larger, and scarier sprite.
However, I am open to changing it back to the old sprite if the player
prefers it that way.

Additionally, the eyeball displays emotions, and if you hit it, it will
cry tears as a sign of pain or sadness.
![eyeballs
pictures](https://github.com/tgstation/tgstation/assets/138636438/8933ea63-d339-474b-8c6e-90a222b74945)

## Why It's Good For The Game
the eyeball now have more depth and character to his behavier.

## Changelog
:cl:
refactor: the eyeball is a basic monster, please report any bugs
sprites: the eyeball now is bigger and scarier and now he will cry when
u hit him
/:cl:

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[b22ff1a4eb...](https://github.com/IndieanaJones/tgstation/commit/b22ff1a4ebfd0a1dd1b75d6979edc73e6f4556b2)
#### Thursday 2023-08-17 02:52:49 by Sealed101

Laser pointer update: Shining Through Walls Edition (feat. fixes!) (#77007)

# _PR PSA_


![augh](https://github.com/tgstation/tgstation/assets/75863639/6dc87fc7-65a3-4b7c-9b8d-a1432cacbe93)


## About The Pull Request
Cleans up code for laser pointers, fixing some bugs like the
forever-charging state or affecting dead cats along the way.
Remaining charge is now available upon examine.
Canonizes #45834 by implementing an upgrade to the laser pointers:
installing a bluespace crystal into a laser with tier 3 or higher laser
diode lets it shine through walls. Using an upgraded laser uses twice
the charge of a normal one. Of course, you can only shine it on
something if you can see the target behind the wall, like via x-ray or
thermals. Mesons don't count, however.
If one tries to jam a crystal into a pointer with a tier 1/2 laser (or a
tier 1/2 laser in a pointer with an installed crystal), _something_ will
get teleported, crushing the crystal.
You can uninstall the crystal with wirecutters or a hemostat. The
pointer will _hint_ on closer examination (`examine_more`) at a
possibility of a crystal being installed if you upgrade the laser
(different messages for tier 1/2/3,4).
Removes one stupid 1% increase for a recharge chance per process tick if
your laser was in a full recharge state because it was insignificant and
irrelevant.

i've had a branch for this for almost 9 months and i was always laying
it off for some day later. today i just completely fucked the branch.
whoops. i'm not even sure at this point what else did i fix while here,
double whoops

## Why It's Good For The Game
Closes #45834 - Canonizes a bug into a feature.
Fixes #77003 - lol
Cleaner code, possibly more robust even.
Seeing the remaining charge was not available at all and the only hint
was when you tried shining the pointer on something. That sucks.

## Changelog
:cl:
add: you can upgrade laser pointers with a bluespace crystal to let them
shine through walls at double the power cost, if the laser in the
pointer is of tier 3 or higher.
qol: laser pointer charge can be seen by examining it
fix: fixed laser pointers luring dead cats when shone upon
code: laser pointer code cleaned up a tad
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[aac465cc2a...](https://github.com/ARF-SS13/coyote-bayou/commit/aac465cc2a5026b18fcab3cd7b7eefde77d2d8a3)
#### Thursday 2023-08-17 03:18:15 by Tk420634

Don't worry about it

hate telemetry warnings, yeah they're great and all but fuck the fuck off

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[f0dc574c37...](https://github.com/IndieanaJones/tgstation/commit/f0dc574c37c6defc0a9e2d4117d20c3963a11d86)
#### Thursday 2023-08-17 03:19:23 by carlarctg

Added Omen Spontaneous Combustion and light tube and mirror effects (#77175)

## About The Pull Request

Cursed crewmembers can randomly, extremely rarely, spontaneously combust
for no reason.

Cursed crewmembers can get zapped by nearby light tubes.

Cursed crewmembers can freak out when passing by mirrors.

To make up for these, triggering a cursed effect is slightly less than
half as likely now when walking around now.

## Why It's Good For The Game

Cursed is fun as hell, but after a certain point it gets kind of
monotonous - it's airlocks, vending machines, and the rest is too rare
to count. We need more ways to comically get hurt in the game.

You might dislike the 'reduced effects' bit but trust me it is
incredibly frickin' common to have shit happen to you. Add to the
occasional vending machine and airlock crushes the near-constant light
tubes all over the station? Yeah, that needs a toning down else it will
be just a tad too miserable to be funny. Also cause the poor janitor
unneeded stress.

## Changelog

:cl:
add: Cursed crewmembers can randomly, extremely rarely, spontaneously
combust for no reason.
add: Cursed crewmembers can get zapped by nearby light tubes.
add: Cursed crewmembers can freak out when passing by mirrors.
add: To make up for these, triggering a cursed effect is slightly less
than half as likely now when walking around now.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [thecsw/thecsw.github.io](https://github.com/thecsw/thecsw.github.io)@[0c1bcc8485...](https://github.com/thecsw/thecsw.github.io/commit/0c1bcc8485a9f21b7afc7b792998f55e076be573)
#### Thursday 2023-08-17 04:07:51 by Ubuntu

[ASTRIE] Added a new fortune: ** 228; 12023 H.E.

``Consciousness of life is higher than life, knowledge of the laws of happiness is higher than happiness''—that is what we must fight against!

--- /The Dream of a Ridiculous Man/

---
## [Zonespace27/daedalusdock](https://github.com/Zonespace27/daedalusdock)@[cf0be10b07...](https://github.com/Zonespace27/daedalusdock/commit/cf0be10b075f2c64220e81d653075b7bcd8fe060)
#### Thursday 2023-08-17 04:12:48 by Kapu1178

Drunk slurring scales based on how drunk you are (#75459) (#460)

The strength of the slurring effect drunkness applies on you now scales
based on how drunk you are.

Being "a little" drunk still changes your saymod, and makes you
occasionally slur your words...

![image](https://github.com/tgstation/tgstation/assets/51863163/1b21b359-a1f9-428a-8e10-d2028ac59728)

But being "a lot" drunk kicks it up to 11

![image](https://github.com/tgstation/tgstation/assets/51863163/9d593c80-75ff-4d02-8e7c-e48c738154bb)

Additionally, drunk slurring was separated into "generic slurring" and
"drunk slurring", the former which does not scale but less closely
resembles drunkness. Generic slurring is used in places such as
concussions, so this is an added bonus.

As a result of the split, I had to update mind restoration. Now it heals
all types of slurring, which does include cult slurs.

I, and many other people, always found it very annoying when you became
completely illegible from taking one sip of a drink. This seeks to amend
that by making low levels of drunkness still for the most part be
legible and sane. Average drunkness is roughly the same / equal to the
old slurring effect, while "very drunk" is even more illegible and silly
(which I find funny).

This has the added bonus of separating out "drunk slurring" and "generic
slurring", allowing effects to slur your words without going full ham on
drunkness (burping and "huhh"s).

:cl: Melbert
add: When you are drunk, the strength of your slurring now varies based
on how drunk you are. Being "a little drunk" only rarely slurs your
words, being average drunk is the same as the old effect, while being
very drunk now slurs your words even more.
add: Some non-alcohol sources of slurring, such as concussions, now give
"generic slurring" rather than "drunk slurring", which less resemble
being drunk (ie, no burping).
add: Mind restoration now heals ALL slurring, rather than only drunk
slurring (which includes cult / heretic slurring).
/:cl:

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [twilightwanderer/FluffySTG](https://github.com/twilightwanderer/FluffySTG)@[8ddcb6ba45...](https://github.com/twilightwanderer/FluffySTG/commit/8ddcb6ba45b3d6e3bb4c6045c04ccdd296422a18)
#### Thursday 2023-08-17 05:46:47 by SkyratBot

Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station [MDB IGNORE] (#22637)

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station (#76974)

## About The Pull Request

This PR adds a new wizard ritual (the kind that require 100 threat on
dynamic)

This ritual allows the wizard to select one spellbook entry (item or
spell), to which everyone on the station will be given or taught said
spell or item. If the spell requires a robe, the spell becomes robeless,
and if the item requires wizard to use, it makes it usable. Mostly.

- Want an epic sword fight? Give everyone a high-frequency blade

- One mindswap not enough shenanigans for you? Give out mindswap

- Fourth of July? Fireball would be pretty hilarious...

The wizard ritual costs 3 points plus the cost of whatever entry you are
giving out. So giving everyone fireball is 5 points.

It can only be cast once by a wizard, because I didn't want to go
through the effort to allow multiple in existence

## Why It's Good For The Game

Someone gave me the idea and I thought it sounded pretty funny as an
alternative to Summon Magic

Maybe I make this a Grand Finale ritual instead / in tandem? That's also
an idea.

## Changelog

:cl: Melbert
add: Wizards have a new Right and Wrong: Mass Teaching, allowing them to
grant everyone on the station one spell or relic of their choice!
/:cl:

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [cammo1123/serenity](https://github.com/cammo1123/serenity)@[8d17ede197...](https://github.com/cammo1123/serenity/commit/8d17ede1977517fb0556857e042bd4abd7174a7b)
#### Thursday 2023-08-17 06:22:08 by Xexxa

Base: Improve emoji

Remove unnecessary left/right padding

❣️ - U+2763 HEART EXCLAMATION
🚶 - U+1F6B6 PERSON WALKING
🚴 - U+1F6B4 PERSON BIKING
🌻 - U+1F33B SUNFLOWER
🪻 - U+1FABB HYACINTH
🍉 - U+1F349 WATERMELON
🍍 - U+1F34D PINEAPPLE
🫒 - U+1FAD2 OLIVE
🌽 - U+1F33D EAR OF CORN
🌯 - U+1F32F BURRITO
🍘 - U+1F358 RICE CRACKER
🧁 - U+1F9C1 CUPCAKE
🍫 - U+1F36B CHOCOLATE BAR
🍭 - U+1F36D LOLLIPOP
🍼 - U+1F37C BABY BOTTLE
🧋 - U+1F9CB BUBBLE TEA
🧃 - U+1F9C3 BEVERAGE BOX
🥢 - U+1F962 CHOPSTICKS
💈 - U+1F488 BARBER POLE
🌛 - U+1F31B FIRST QUARTER MOON FACE
🌜 - U+1F31C LAST QUARTER MOON FACE
🌡️ - U+1F321 THERMOMETER
🪐 - U+1FA90 RINGED PLANET
⚡ - U+26A1 HIGH VOLTAGE
💧 - U+1F4A7 DROPLET
🧨 - U+1F9E8 FIRECRACKER
🥇 - U+1F947 1ST PLACE MEDAL
🥈 - U+1F948 2ND PLACE MEDAL
🥉 - U+1F949 3RD PLACE MEDAL
🏓 - U+1F3D3 PING PONG
🪀 - U+1FA80 YO-YO
♟️ - U+265F CHESS PAWN
🧦 - U+1F9E6 SOCKS
💄 - U+1F484 LIPSTICK
📱 - U+1F4F1 MOBILE PHONE
🔌 - U+1F50C ELECTRIC PLUG
💡 - U+1F4A1 LIGHT BULB
📍 - U+1F4CD ROUND PUSHPIN
🔩 - U+1F529 NUT AND BOLT
🪝 - U+1FA9D HOOK
🧪 - U+1F9EA TEST TUBE
🔭 - U+1F52D TELESCOPE
🩸 - U+1FA78 DROP OF BLOOD
💊 - U+1F48A PILL
🩹 - U+1FA79 ADHESIVE BANDAGE
🧼 - U+1F9FC SOAP
🪥 - U+1FAA5 TOOTHBRUSH
♀️ - U+2640 FEMALE SIGN
♂️ - U+2642 MALE SIGN
➕ - U+2795 PLUS
➗ - U+2797 DIVIDE
❓ - U+2753 RED QUESTION MARK
❔ - U+2754 WHITE QUESTION MARK
❕ - U+2755 WHITE EXCLAMATION MARK
❗ - U+2757 RED EXCLAMATION MARK
◼️ - U+25FC BLACK MEDIUM SQUARE
◻️ - U+25FB WHITE MEDIUM SQUARE
◾ - U+25FE BLACK MEDIUM-SMALL SQUARE
◽ - U+25FD WHITE MEDIUM-SMALL SQUARE
▪️ - U+25AA BLACK SMALL SQUARE
▫️ - U+25AB WHITE SMALL SQUARE
🚩 - U+1F6A9 TRIANGULAR FLAG

---
## [poire-z/koreader](https://github.com/poire-z/koreader)@[4acf131071...](https://github.com/poire-z/koreader/commit/4acf131071c704863d0d66f78f1b2314df9c3164)
#### Thursday 2023-08-17 06:41:45 by NiLuJe

ReaderActivityIndicator: Oh god, my eyes, they buuuuurn.

Make this a real boy, with a transient lipc handle.
And get rid of the insane 1s sleep on affected ReaderView paints,
because ouchy.

This is completely deprecated anyway, so this is entirely pointless,
and mainly to prevent implementation details from creeping into
reader.lua.

---
## [afirpo/tgstation](https://github.com/afirpo/tgstation)@[5abafddaea...](https://github.com/afirpo/tgstation/commit/5abafddaea2373b5e367a7ac658d6cab6499b70c)
#### Thursday 2023-08-17 06:49:55 by carlarctg

Adds a unique medibot to the Syndicate Infiltrator (#77582)

## About The Pull Request

Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)

Fixed an issue that made mapload medibots unable to load custom skins.

This PR adds a medibot subtype to the simple animal freeze list, which I
don't think is a big deal as this isn't a 'true' simplemob but just a
slightly altered medibot, similarly to my 'lesser Gorillas' in the
summon simians PR.

## Why It's Good For The Game

> Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though.

I know what the inmediate reaction is here - but hear me out. Besides
the meme of the month, it really, genuinely is cute and amusing to have
a friendly medibot that shows dismay when you're arming the nuke and
horror when it blows up (with you, hopefully, at the syndibase), and
still fits quite well within SS13's charm and flavor. The reference
isn't overt and in-your-face.

Besides that, slip-ups, friendly fire, and accidents are semi-common on
the shuttle and, just like Wizards, nukies deserve a bot to patch their
wounds up.

> (It's also in the Interdyne Pharmaceuticals ship, renamed)

I think it makes sense for the pharmacists to have an evil medibot!

> Fixed an issue that made mapload medibots unable to load custom skins.

Fixed "bezerk" skin not appearing. Didn't fix it being ugly as sin
though.

## Changelog

:cl:
add: Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)
fix: Fixed an issue that made mapload medibots unable to load custom
skins.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [tomaarsen/argilla](https://github.com/tomaarsen/argilla)@[2f2a113352...](https://github.com/tomaarsen/argilla/commit/2f2a11335289d660ce20aea11c9b969b0316fd2b)
#### Thursday 2023-08-17 07:17:22 by peppinob-ol

[DOCS] Code Refactoring and content update of quickstart_workflow.ipynb (#3472)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

I found the quickstart workflow not as quick as it could be:

- Cells cannot be run straightaway in google colab and need extra work
(eg. libraries not imported).
- Some important concepts (eg. records and datasets) are not clearly
stated in text and code snippets
- Text refers to the same steps more than once (no clear chain of
thought)
- Cells override the same variable (eg. record), so the feeling is more
of a cheatsheet than of a tutorial notebook
- Content is not updated (eg. ArgillaTrainer is not ever mentioned in
the Train section)

I worked on a new version of the notebook with enhanced code and text
cells.Ii added also code snippets for training examples which were only
described textually.

One last suggestion: It's advisable that external files (data) are
downloaded programmatically by running a cell (eg. using `requests
`library). `Snapchat_app_store_reviews.csv` and `kaffee_reviews.csv` are
taken from kaggle which requires sign-in, so it's not possible to
download them directly. Possible solutions:

- place a copy of the Kaggle datasets in Arggilla's GitHub repository
(if permitted by Kaggle's terms of use)
- select other datasets from another source.

Closes #3431

**Type of change**

(Please delete options that are not relevant. Remember to title the PR
according to the type of change)

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] Refactor (change restructuring the codebase without changing
functionality)
- [ ] Improvement (change adding some improvement to an existing
functionality)
- [X] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes. And
ideally, reference `tests`)

- [ ] Test A: code run with latest google-colab (v.1.0.0)

**Checklist**

- [X] I added relevant documentation
- [X] follows the style guidelines of this project
- [X] I did a self-review of my code
- [X] I made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [X] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [ ] I have added relevant notes to the CHANGELOG.md file (See
https://keepachangelog.com/)

---------

Co-authored-by: devorma <94636163+devorma@users.noreply.github.com>
Co-authored-by: davidberenstein1957 <david.m.berenstein@gmail.com>

---
## [gr33nb3rry/MovieMatch](https://github.com/gr33nb3rry/MovieMatch)@[cf6277ec95...](https://github.com/gr33nb3rry/MovieMatch/commit/cf6277ec95fe9a061abcc0f2fa6f24693ebe1442)
#### Thursday 2023-08-17 07:50:21 by Ruslan Bulak

OMG It was so painful!! I was suffering for 3 hours just because of wrong line, but now it works

I implemented adding new collection that is related to match_movie_user.user_id and simple GetMapping of all collections

---
## [RorriMaesu/laZtype](https://github.com/RorriMaesu/laZtype)@[4bb4d9df21...](https://github.com/RorriMaesu/laZtype/commit/4bb4d9df2152bfdd2ab38900d732a11d975445c3)
#### Thursday 2023-08-17 08:26:47 by Andrew J. Green

Add files via upload

LaZtype: Where Sloth Meets Efficiency

Description:
Ever wondered what would happen if a sloth tried coding? With LaZtype, I've harnessed the laid-back energy of the keyboard-loving sloth mascot to bring you a voice-command experience that's both relaxing and incredibly efficient. Why rush when you can dictate at a sloth's pace and still out-code the rest?

Features:

Slow and Steady Voice-to-Action: In the coding world, accuracy trumps speed. Dictate confidently, knowing LaZtype catches every word.
Custom Command Creation: The sloth may love the default settings, but you can tweak them to your heart's content.
Quadrant Navigation: Direct the mouse with sloth-like precision. Slow, sure, and on point.
Clear Feedback Mechanism: With the intuitive microphone UI, you're always in the know – no mysterious sloth secrets here.
Personalized User Settings: Configure LaZtype so it's as comfy as a sloth on a branch... or a keyboard.
Helpful Tooltips: For those slow-to-get-it moments, the tooltips come to the rescue.
Upcoming Features:

Broad Platform Adaptability: I'm slowly but surely extending the branches to MacOS and Linux.
Data Security Upgrades: Your voice data is as precious as a sloth's nap time – I'm ensuring it stays safe.
Voice Recognition Refinement: Continual tweaks to catch even the softest sloth-like whispers.
Tailored Software Integration: I'm all ears (like the sloth friend) to user requests for software compatibility.
Multilingual Support: Sloths may not be global jet-setters, but my app will be. Multiple language support is on the horizon.
Gesture Recognition Addition: Because sometimes, even sloths like to wave.
Potential Upgrades:
While the sloth might enjoy a lazy afternoon, I'm continuously brainstorming. Keep an eye out for voice-triggered macros, AR/VR integration, and more – all delivered at a pace that guarantees perfection.

LaZtype: Embrace the sloth within and code without lifting a finger – or claw.

---
## [vansh-py04/Data-Analyst-Portfolio](https://github.com/vansh-py04/Data-Analyst-Portfolio)@[6670199c3f...](https://github.com/vansh-py04/Data-Analyst-Portfolio/commit/6670199c3fa9d6f1463a6ee53b44ea36130810ea)
#### Thursday 2023-08-17 08:44:47 by Yuganter Pratap

Instagram User Analytics

Imagine you're a data analyst working with the product team at Instagram. Your role involves analyzing user interactions and engagement with the Instagram app to provide valuable insights that can help the business grow.
User analysis involves tracking how users engage with a digital product, such as a software application or a mobile app. The insights derived from this analysis can be used by various teams within the business. For example, the marketing team might use these insights to launch a new campaign, the product team might use them to decide on new features to build, and the development team might use them to improve the overall user experience.
In this project, you'll be using SQL and MySQL Workbench as your tool to analyze Instagram user data and answer questions posed by the management team. Your insights will help the product manager and the rest of the team make informed decisions about the future direction of the Instagram app.
Remember, the goal of this project is to use your SQL skills to extract meaningful insights from the data. Your findings could potentially influence the future development of one of the world's most popular social media platforms

---
## [987123879113/mame](https://github.com/987123879113/mame)@[e97630981c...](https://github.com/987123879113/mame/commit/e97630981c406ba446e2d7fb1bf8ecf8d3a6b93b)
#### Thursday 2023-08-17 09:10:34 by A-Noid33

Added software list for cracked Macintosh floppy images. (#11454)

New working software list items (mac_flop_orig.xml)
-------------------------------
Alter Ego (male version 1.0) (san inc crack) [4am, san inc, A-Noid]
Alter Ego (version 1.1 female) (san inc crack) [4am, san inc, A-Noid]
Alternate Reality: The City (version 3.0) (san inc crack) [4am, san inc, A-Noid]
Animation Toolkit I: The Players (version 1.0) (4am crack) [4am, A-Noid]
Balance of Power (version 1.03) (san inc crack) [4am, san inc, A-Noid]
Borrowed Time (san inc crack) [4am, san inc, A-Noid]
Championship Star League Baseball (san inc crack) [4am, san inc, A-Noid]
Cutthroats (release 23 / 840809-C) (4am crack) [4am, A-Noid]
CX Base 500 (French, version 1.1) (san inc crack) [4am, san inc, A-Noid]
Deadline (release 27 / 831005-C) (4am crack) [4am, A-Noid]
Defender of the Crown (san inc crack) [4am, san inc, A-Noid]
Deluxe Music Construction Set (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Déjà Vu (version 2.3) (4am crack) [4am, A-Noid]
Déjà Vu: A Nightmare Comes True!! (san inc crack) [4am, san inc, A-Noid]
Déjà Vu II: Lost in Las Vegas!! (san inc crack) [4am, san inc, A-Noid]
Dollars and Sense (version 1.3) (4am crack) [4am, A-Noid]
Downhill Racer (san inc crack) [4am, san inc, A-Noid]
Dragonworld (4am crack) [4am, A-Noid]
ExperLisp (version 1.0) (4am crack) [4am, A-Noid]
Forbidden Castle (san inc crack) [4am, san inc, A-Noid]
Fusillade (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Geometry (version 1.1) (4am crack) [4am, A-Noid]
Habadex (version 1.1) (4am crack) [4am, A-Noid]
Hacker II (san inc crack) [4am, san inc, A-Noid]
Harrier Strike Mission (san inc crack) [4am, san inc, A-Noid]
Indiana Jones and the Revenge of the Ancients (san inc crack) [4am, san inc, A-Noid]
Infidel (release 22 / 840522-C) (4am crack) [4am, A-Noid]
Jam Session (version 1.0) (4am crack) [4am, A-Noid]
Legends of the Lost Realm I: The Gathering of Heroes (version 2.0) (4am crack) [4am, A-Noid]
Lode Runner (version 1.0) (4am crack) [4am, A-Noid]
Mac Pro Football (version 1.0) (san inc crack) [4am, san inc, A-Noid]
MacBackup (version 2.6) (4am crack) [4am, A-Noid]
MacCheckers and Reversi (4am crack) [4am, A-Noid]
MacCopy (version 1.1) (4am crack) [4am, A-Noid]
MacGammon! (version 1.0) (4am crack) [4am, A-Noid]
MacGolf (version 2.0) (4am crack) [4am, A-Noid]
MacWars (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 2.00h) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 3.4a) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 4.0) (san inc crack) [4am, san inc, A-Noid]
Math Blaster (version 1.0) (4am crack) [4am, A-Noid]
Maze Survival (san inc crack) [4am, san inc, A-Noid]
Microsoft Excel (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Microsoft File (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Mindshadow (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.03) (4am crack) [4am, A-Noid]
Mouse Stampede (version 1.00) (4am crack) [4am, A-Noid]
Murder by the Dozen (Thunder Mountain) (4am crack) [4am, A-Noid]
My Office (version 2.7) (4am crack) [4am, A-Noid]
One on One (san inc crack) [4am, san inc, A-Noid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Patton Strikes Back (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Patton vs. Rommel (version 1.05) (san inc crack) [4am, san inc, A-Noid]
Pensate (version 1.1) (4am crack) [4am, A-Noid]
PFS File and Report (version A.00) (4am crack) [4am, A-Noid]
Physics (version 1.0) (4am crack) [4am, A-Noid]
Physics (version 1.2) (4am crack) [4am, A-Noid]
Pinball Construction Set (version 2.5) (san inc crack) [4am, san inc, A-Noid]
Pipe Dream (version 1.2) (4am crack) [4am, A-Noid]
Professional Composer (version 2.3Mfx) (san inc crack) [4am, san inc, A-Noid]
Q-Sheet (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Rambo: First Blood Part II (san inc crack) [4am, san inc, A-Noid]
Reader Rabbit (version 2.0) (4am crack) [4am, A-Noid]
Rogue (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Seastalker (release 15 / 840522-C) (4am crack) [4am, A-Noid]
Seven Cities of Gold (san inc crack) [4am, san inc, A-Noid]
Shadowgate (san inc crack) [4am, san inc, A-Noid]
Shanghai (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Shufflepuck Cafe (version 1.0) (4am crack) [4am, A-Noid]
Sierra Championship Boxing (4am crack) [4am, A-Noid]
SimCity (version 1.1) (4am crack) [4am, A-Noid]
SimCity (version 1.2, black & white) (4am crack) [4am, A-Noid]
SimEarth (version 1.0) (4am crack) [4am, A-Noid]
Skyfox (san inc crack) [4am, san inc, A-Noid]
Smash Hit Racquetball (version 1.01) (san inc crack) [4am, san inc, A-Noid]
SmoothTalker (version 1.0) (4am crack) [4am, A-Noid]
Speed Reader II (version 1.1) (4am crack) [4am, A-Noid]
Speller Bee (version 1.1) (4am crack) [4am, A-Noid]
Star Trek: The Kobayashi Alternative (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Stratego (version 1.0) (4am crack) [4am, A-Noid]
Suspect (release 14 / 841005-C) (4am crack) [4am, A-Noid]
Tass Times in Tonetown (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-09-30) (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-10-08) (san inc crack) [4am, san inc, A-Noid]
The Chessmaster 2000 (version 1.02) (4am crack) [4am, A-Noid]
The Crimson Crown (san inc crack) [4am, san inc, A-Noid]
The Duel: Test Drive II (san inc crack) [4am, san inc, A-Noid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914-C) (4am crack) [4am, A-Noid]
The King of Chicago (san inc crack) [4am, san inc, A-Noid]
The Lüscher Profile (san inc crack) [4am, san inc, A-Noid]
The Mind Prober (version 1.0) (san inc crack) [4am, san inc, A-Noid]
The Mist (san inc crack) [4am, san inc, A-Noid]
The Quest (4am crack) [4am, A-Noid]
The Slide Show Magician (version 1.2) (4am crack) [4am, A-Noid]
The Surgeon (version 1.5) (san inc crack) [4am, san inc, A-Noid]
The Toy Shop (version 1.1) (san inc crack) [4am, san inc, A-Noid]
The Witness (release 22 / 840924-C) (4am crack) [4am, A-Noid]
ThinkTank 128 (version 1.000) (4am crack) [4am, A-Noid]
Uninvited (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Uninvited (version 2.1D1) (san inc crack) [4am, san inc, A-Noid]
Where in Europe is Carmen Sandiego? (version 1.0) (4am crack) [4am, A-Noid]
Winter Games (version 1985-10-24) (san inc crack) [4am, san inc, A-Noid]
Winter Games (version 1985-10-31) (san inc crack) [4am, san inc, A-Noid]
Wishbringer (release 68 / 850501-D) (4am crack) [4am, A-Noid]
Wizardry: Proving Grounds of the Mad Overlord (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Zork II (release 48 / 840904-C) (4am crack) [4am, A-Noid]
Zork III (release 17 / 840727-C) (4am crack) [4am, A-Noid]

---
## [chintakindi66/Madhav_ecom_sales_dashboard](https://github.com/chintakindi66/Madhav_ecom_sales_dashboard)@[e4277df74d...](https://github.com/chintakindi66/Madhav_ecom_sales_dashboard/commit/e4277df74d505f8506e5432ccbae031650df0c71)
#### Thursday 2023-08-17 10:01:58 by Santosh Chintakindi

Update README.md


Here's a sneak peek into the intricacies of this project:

🔗 Data Connections and Table Enhancements:
I've established robust connections to the data sources, ensuring that the dashboard remains up-to-date with the latest information. Furthermore, I've skillfully joined new tables to provide a comprehensive view of the sales landscape, enriching the analytical potential of the dashboard.

🔍 User-Driven Parameters:
One of the standout features of this dashboard is the integration of user-driven parameters. Users can actively tweak these parameters to tailor the visualizations to their specific requirements. This personalization ensures that the dashboard adapts to the unique analytical needs of each user.

📊 Visualization Variety:
The dashboard offers an array of customized visualizations to cater to different preferences and analytical scenarios. From the classic bar, pie, and donut charts to more advanced clustered bar charts, scatter charts, line charts, and area charts — users have access to a plethora of visualization options.

🔗 Slicers for Enhanced Control:
To elevate the user experience, I've strategically integrated slicers that facilitate effortless data filtering. These slicers empower users to dynamically adjust the displayed data, allowing for swift comparisons and trend analysis.

🌐 Sharing on LinkedIn:
I'm excited to showcase this achievement on LinkedIn! This dashboard demonstrates my prowess in data analysis, visualization, and dashboard creation. It's a testament to my ability to transform raw data into actionable insights and to create user-friendly interfaces for data exploration.

Feel free to reach out if you'd like to learn more about this dashboard or if you're interested in exploring the intricate details of how it was created. I'm enthusiastic about the potential of this project to revolutionize online sales analysis and drive data-informed decision-making. Stay tuned for more updates on LinkedIn! 🚀📈

---
## [kubouch/nushell](https://github.com/kubouch/nushell)@[ad49c17eba...](https://github.com/kubouch/nushell/commit/ad49c17ebacd04585fb4355e079ec87d7fc63d8d)
#### Thursday 2023-08-17 11:18:53 by Kiryl Mialeshka

fix(nu-parser): do not update plugin.nu file on nu startup (#10007)

<!--
if this PR closes one or more issues, you can automatically link the PR
with
them by using one of the [*linking
keywords*](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword),
e.g.
- this PR should close #xxxx
- fixes #xxxx

you can also mention related issues, PRs or discussions!
-->

# Description

I've been investigating the [issue
mentioned](https://github.com/nushell/nushell/pull/9976#issuecomment-1673290467)
in my prev pr and I've found that plugin.nu file that is used to cache
plugins signatures gets overwritten on every nushell startup and that
may actually mess up with the file content if 2 or more instances of
nushell will run simultaneously.

To reproduce:
1. register at least 2 plugins in your local nushell
2. remember how many entries you have in plugin.nu with `open
$nu.plugin-path | find nu_plugin`
3. run 
    - either `cargo test` inside nushell repo
- or run smth like this `1..100 | par-each {|it| $"(random integer
1..100)ms" | into duration | sleep $in; nu -c "$nu.plugin-path"}` to
simulate parallel access. This approach is not so reliable to reproduce
as running test but still a good point that it may effect users actually
4. validate that your `plugin.nu` file was stripped

<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

# Solution

In this pr I've refactored the code of handling the `register` command
to minimize code duplications and make sure that overwrite of
`plugin.nu` file is happen only when user calls the command and not on
nu startup

Another option would be to use temp `plugin.nu` when running tests, but
as the issue actually can affect users I've decided to prevent
unnecessary writing at all. Although having isolated `plugin.nu` still
worth of doing

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->
It changes the behaviour actually as the call `register <plugin>
<signature>` now doesn't updates `plugin.nu` and just reads signatures
to the memory. But as I understand that kind of call with explicit
signature is meant to use only by nushell itself in the `plugin.nu` file
only. I've asked about it in
[discord](https://discordapp.com/channels/601130461678272522/615962413203718156/1140013448915325018)

<!--
Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect -A clippy::result_large_err` to check that
you're using the standard code style
- `cargo test --workspace` to check that all tests pass
- `cargo run -- -c "use std testing; testing run-tests --path
crates/nu-std"` to run the tests for the standard library

> **Note**
> from `nushell` you can also use the `toolkit` as follows
> ```bash
> use toolkit.nu # or use an `env_change` hook to activate it
automatically
> toolkit check pr
> ```
-->

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

Actually, I think the way plugins are stored might be reworked to
prevent or mitigate possible issues further:
- problem with writing to file may still arise if we try to register in
parallel as several instances will write to the same file so the lock
for the file might be required
- using additional parameters to command like `register` to implement
some internal logic could be misleading to the users
- `register` call actually affects global state of nushell that sounds a
little bit inconsistent with immutability and isolation of other parts
of the nu. See issues
[1](https://github.com/nushell/nushell/issues/8581),
[2](https://github.com/nushell/nushell/issues/8960)

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[1ea79a2ed8...](https://github.com/cmss13-devs/cmss13/commit/1ea79a2ed836ef4d20db511485c2f935304bfd55)
#### Thursday 2023-08-17 11:21:49 by Ben

Zombie Rework (#4060)

# About the pull request

The goal for this PR is to rework zombies into being a fast and
numerous, but weaker, entity. As it stands a zombie has too many
advantages where a hold against them is essentially a fool's errand.

CURRENT PLAN (Will adjust as needed)
Zombies will be FASTER but much weaker than current iteration, with
weaker attacks. They will be designed around being a foe that can be
taken down quicker but if they close the distance, the threat of
infection spells a death sentence.

# Explain why it's good for the game

This will be hard to balance, and as such will be taking feedback before
I submit this for review. This is current position of Zombies:

- Tough: Extreme (25% ?!) brute modifier, with fire modifier on top,
making them very tanky and requiring clips to take down one
- self-revive: They WILL come back up, coupled with toughness, they are
a feared opponent.
- Strength: Claws inflict superslow at 40 brute damage, one of the
highest damage levels.
- Numerous: They have the numbers to put lesser drones and even entire
hives to shame

Overall, they are very overtuned and makes playing against them not that
fun. My plan is to have it so they are much weaker, with their threat
being from infections.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Zombie attacks deal less damage and only slow down targets (not
superslow as they currently do)
balance: Zombie resistances have been reduced heavily, making them far
more susceptible to brute damage. Their speed has been doubled to
compensate
balance: Black goo on tiles now requires you to not wear shoes to have
chance for infection
fix: Zombie attacks now only apply effects such as slow and infection if
the attack is valid (if the zombie is able to attack)
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[fd3442635c...](https://github.com/treckstar/yolo-octo-hipster/commit/fd3442635c322b765eca64d9c6e4510d06288714)
#### Thursday 2023-08-17 11:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [kaowjubss/webdev](https://github.com/kaowjubss/webdev)@[93178940a6...](https://github.com/kaowjubss/webdev/commit/93178940a684a413da2dc04b09ac38c77d2bdae4)
#### Thursday 2023-08-17 11:23:57 by PumpkinPie77

Merge pull request #12 from kaowjubss/8-get-rid-of-those-yee-yee-ass-haircut-and-get-some-bitches-on-your-dck

shit

---
## [Addust/Yogstation](https://github.com/Addust/Yogstation)@[465aef0da1...](https://github.com/Addust/Yogstation/commit/465aef0da1b967bf7cb008e7906f5791d81b89cd)
#### Thursday 2023-08-17 11:33:21 by Cark

Some minor changes to space syndicate base. (#19282)

* syndiebuff

* fuck you airlock

* fucking AIRLOCK CONTROLLERS

---
## [ptxmac/zola](https://github.com/ptxmac/zola)@[b5a90dba5d...](https://github.com/ptxmac/zola/commit/b5a90dba5d12ea6760c3aa18fec40f8af4d7cbc7)
#### Thursday 2023-08-17 12:06:02 by sinofp

Add support for lazy loading images (#2211)

* Add optional decoding="async" loading="lazy" for img

In theory, they can make the page load faster and show content faster.

There’s one problem: CommonMark allows arbitrary inline elements in alt text.
If I want to get the correct alt text, I need to match every inline event.

I think most people will only use plain text, so I only match Event::Text.

* Add very basic test for img

This is the reason why we should use plain text when lazy_async_image is enabled.

* Explain lazy_async_image in documentation

* Add test with empty alt and special characters

I totaly forgot one can leave the alt text empty.
I thought I need to eliminate the alt attribute in that case,
but actually empty alt text is better than not having an alt attribute at all:
https://www.w3.org/TR/WCAG20-TECHS/H67.html
https://www.boia.org/blog/images-that-dont-need-alternative-text-still-need-alt-attributes
Thus I will leave the empty alt text.

Another test is added to ensure alt text is properly escaped.
I will remove the redundant escaping code after this commit.

* Remove manually escaping alt text

After removing the if-else inside the arm of Event::Text(text),
the alt text is still escaped.
Indeed they are redundant.

* Use insta for snapshot testing

`cargo insta review` looks cool!

I wanted to dedup the cases variable,
but my Rust skill is not good enough to declare a global vector.

---
## [Is-That-Ajay/Nmap-auto](https://github.com/Is-That-Ajay/Nmap-auto)@[2bf4898f04...](https://github.com/Is-That-Ajay/Nmap-auto/commit/2bf4898f04c877c677417190973bf8a9f0d07b7c)
#### Thursday 2023-08-17 12:11:38 by Is-That-Ajay

The Nmap Automation Tool is a sophisticated utility designed to streamline and simplify the process of network scanning within the Linux terminal environment. This tool offers a range of powerful features tailored to meet your network scanning needs, all while adhering to the principles of efficient automation and robust functionality.

+Nmap Automation Tool

The Nmap Automation Tool is a sophisticated utility designed to streamline and simplify the process of network scanning within the Linux terminal environment. This tool offers a range of powerful features tailored to meet your network scanning needs, all while adhering to the principles of efficient automation and robust functionality.

Key Features:

    Effortless Network Scanning: The tool effectively automates the intricate process of network scanning, reducing manual intervention and enhancing efficiency.
    Tailored Scanning Options: Experience the convenience of prebuilt scanning options carefully designed to cater to your specific network exploration requirements.
    Seamless Results Storage: Enjoy the ability to effortlessly save all scan results into a designated text file of your choosing, ensuring easy access to vital information.
    Linux Terminal Integration: The tool seamlessly operates within the Linux terminal environment, providing a familiar and powerful platform for all its operations.
    Interactive User Experience: Engage with a user-friendly interface that guides you through each step of the scanning process, ensuring an intuitive and efficient experience.
    Flexible Customization: Tailor the tool to your preferences by making adjustments that align with your specific scanning objectives.

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[87f707dfa8...](https://github.com/mc-oofert/tgstation/commit/87f707dfa8dd901310f72585c6f701035bc653ee)
#### Thursday 2023-08-17 12:37:24 by DeerJesus

Adds the Storage Implanter to the spy kit. (#77452)

## About The Pull Request

Adds the storage implanter to the spy kit to make it decent.

## Why It's Good For The Game
This PR hopes to bring Spy at least a little more in-line with the rest
of the syndie-kit specials, so it doesn’t feel like a complete dud to
get.

Spy absolutely sucks as a syndie-kit and getting it is basically
throwing away 20 TC. Not all of them should be equally powerful but all
of them should be at least more satisfying to get. Spy is so bad that
it’s listed in the official wiki as ‘honestly not that good’. It’s also
_barely_ even above 25 telecrystals as the switchblade is a black market
uplink item, not a syndicate uplink item, and not even that good of an
item at that! And the chameleon kit inside isn’t even a full chameleon
kit! Pitiful. Compare it to stealth right below it which totals to _36_
telecrystals.

Adding a storage implant adds a relatively useful item to the kit that
still fits with the entire theme of ‘stealth and deception’, as you can
be searched without having anything on you. To be stealthy, and deceive
people. Like you should. Given the fact that searches are quite common.
It doesn’t make it TOO overpowered as the rest of the gear is still ‘not
that great’.


## Changelog

:cl:
balance: added the storage implanter to the syndie-kit tactical 'spy'
kit to make it decent.
/:cl:

Co-authored-by: oilysnake <63020759+oilysnake@users.noreply.github.com>

---
## [krishna0306/seat_count_tracker](https://github.com/krishna0306/seat_count_tracker)@[0baf462c6d...](https://github.com/krishna0306/seat_count_tracker/commit/0baf462c6d11c02fa4d319884bfd432f35a4dd49)
#### Thursday 2023-08-17 13:10:13 by radhe krishna

Add files via upload

What This Project Does
Imagine you're planning a train journey, and you want to make sure you get a seat. This project helps you keep an eye on seat availability using a special tool – a Telegram Bot. The bot tells you when the seat count on your chosen train falls below a certain number you set. It's like having a friendly assistant that sends you a message whenever it's time to book your seat!

How It Works
Setting Things Up

First, you need to copy the project to your computer. It's like bringing a recipe into your kitchen.
You install the "ingredients" your recipe needs, which are some special tools (we call them "libraries").
You get some special keys – like keys to a secret door – from two different places: one for the train information and another for the Telegram Bot.
Running the Bot

Now, it's time to run the Telegram Bot. Just like turning on a TV.
The bot asks you for information about the train you want to track and how many seats you want to keep an eye on.
It's like telling your assistant which train you're interested in and when to warn you.
Checking Seats

The bot uses the "keys" you gave it to ask the internet about the train's seats.
It finds out how many seats are left and compares it to the number you want.
If the seats are getting low, it sends you a message on Telegram – like a friend sending a text to remind you of something.
Making It Your Own
Customizing the Bot

If you want, you can make the bot look and work the way you like. Just like decorating your room!
You can tell it how to talk to you and what messages to send.
You can even set up the bot to track different trains or seat numbers – it's all up to you.
Getting Help

Don't worry if you don't understand everything at first. You can ask the creator of the bot for help – just like asking a teacher if you don't understand a lesson.
They even left their email and a link to their place on the internet (GitHub) so you can talk to them and learn more.
Sharing the Recipe

This project is like a recipe for a magic dish. You can share it with your friends, and they can make their own bots too.
Remember, this project is like a way to learn about computer programs and how to make them do cool things!

---
## [alphagov/govuk-frontend](https://github.com/alphagov/govuk-frontend)@[e750828e05...](https://github.com/alphagov/govuk-frontend/commit/e750828e056c0e07c0a37629dba063b2a910d3de)
#### Thursday 2023-08-17 13:33:53 by Romaric Pascal

Spike - Trying to sort out types for having the module check in GOVUKFrontendComponent

Only the SkipLink has been updated so far, as it's a neat example of a component needing a different type for $module.

A couple of things get in the way of moving the check into the parent class.

With the `if` in the code of the component itself, before the assignment to `$module`, as it was before this commit, TypeScript could infer that after that `if`, `$module` was of the type checked by `instanceof`.

By moving the check inside a function, TypeScript can no longer follow. This can however be documented in JSDoc using the generic `ModuleType` type that's been introduced for moving `$module` in the parent class.

For components like SkipLink, we need the expected type for `$module` to be stored in a variable.
A static property does not work because TypeScript struggles with `this.constructor.moduleType`, necessary to make sure we'd be reading the subclasses static property and not `GOVUKFrontendComponent` one.
We can live with an instance property for now. However this doesn't solve the problem. Making that property dynamic means TypeScript is no longer able to infer the type of `$module` after the `if`.

This leads to us having to typecast it (with a rather ugly double type cast to avoid TypeScript complaining).

As long as `ModuleType` and `this.moduleType` are in check, that's fine. We'll need to be a little bit cautious, but I think that's something we can maintain.

- I tried passing `moduleType` to `checkModuleType` but it's unclear what type the param should be. It doesn't solve the type casting inside the function anyway.
- Given we're manually handling the types inside that function because things are too dynamic, I'd be keen to make `moduleType` be a static property anyway and deal with any complaint from TypeScript

---
## [erazare/Legendary-Edition-v.1.20.1](https://github.com/erazare/Legendary-Edition-v.1.20.1)@[5e2854b8f4...](https://github.com/erazare/Legendary-Edition-v.1.20.1/commit/5e2854b8f43cb1a67d9feb18b86e214cdd1408b1)
#### Thursday 2023-08-17 14:34:06 by erazare

v.1.3.3

i just want to make this very clear.. when updating a mod from one version to the next... clean up your fucking libraries you goddamn developer retards. keeping shit in there from 1.12 is goddamn RETARDED

---
## [Neha-7330/Simon-Game](https://github.com/Neha-7330/Simon-Game)@[b398d5fec9...](https://github.com/Neha-7330/Simon-Game/commit/b398d5fec9f3ff18e1298feee260f8c1aba75146)
#### Thursday 2023-08-17 16:29:51 by Neha Pudake

Add files via upload

Simon Game Website
Welcome to the Simon Game, a classic memory and pattern recognition game brought to life on the web! This project showcases my frontend development skills using HTML, CSS, JavaScript, and jQuery to recreate the beloved Simon Game.

Features
Interactive Gameplay: Test your memory and concentration as you follow the sequence of colors and sounds generated by the game.
Levels of Difficulty: Challenge yourself with increasing levels of difficulty as the patterns get longer and more complex.
User-Friendly Interface: A sleek and intuitive user interface that makes the game enjoyable for players of all ages.
Auditory and Visual Feedback: Experience responsive feedback through both visual cues and auditory signals for a engaging gaming experience.
Strict and Normal Modes: Choose between Strict Mode, where mistakes reset the game entirely, and Normal Mode, where mistakes only reset the current level.
High Scores: Keep track of your best performances and compete against yourself to beat your high scores.

Technologies Used
HTML5: Structured the content of the game with semantic HTML elements.
CSS3: Styled the interface to be visually appealing and responsive across different devices.
JavaScript: Implemented the game's logic and functionality.
jQuery: Simplified DOM manipulation and event handling, enhancing the interactivity of the game.

How to Play
Press the "Play" button to begin the game.
Watch and listen carefully to the pattern of colors and tones played by the game.
Repeat the pattern by clicking on the colored buttons in the correct order.
As you progress, the patterns will become longer and more challenging.
If you make a mistake Refresh the page to Start Over again.

---
## [Iajret/Skyrat-tg](https://github.com/Iajret/Skyrat-tg)@[d5655c3c55...](https://github.com/Iajret/Skyrat-tg/commit/d5655c3c55fab0f4450659947fad1a40043893dc)
#### Thursday 2023-08-17 16:32:52 by SkyratBot

[MIRROR] Adds Summon Simians & Buffs/QoLs Mutate [MDB IGNORE] (#22970)

* Adds Summon Simians & Buffs/QoLs Mutate (#77196)

## About The Pull Request

Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

Added further support for nonhuman robed casting: Monkeys, cyborgs, and
drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

Made monkeys able to wield things again.

Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.

Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Improved some monkey AI code.

## Why It's Good For The Game

> Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

It's criminal we don't have a monky spell, and this is a really fun spin
on it. Total chaos, but total monky chaos. It's surprisingly strong,
but! it can very well backfire if you stay near the angry monkeys too
long and your protection fades away. Unless you become a monkey
yourself!!

> Wizard Mutate spell works on non-human races.

This spell is great but it's hampered by the mutation's human
requirement, which is reasonable in normal gameplay. Wizards don't need
to care about that, and the human restriction hinders a lot of possible
gimmicks, so off it goes. Also, wizard hulk does't cause chunky fingers
for similar reasons

> Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Don't really caer about the damage so much, this is more so that it has
effects such as on-hit visuals. Can lower the damage if required, but
honestly anything that competes against troll mjolnir is good.

> Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

SS13 is known for 'The Dev Team Thinks of Everything' and I believe this
is a sorely lacking part of this or something. It's funny.
I want to see a monkey wizard.

> Made monkeys able to wield things again.

I really don't know why this was a thing and it was breaking my axe and
spear wielding primal monkeys. Like, why?

## Changelog

:cl:
add: Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.
balance: Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.
balance: Made Laser eyes projectiles a subtype of actual lasers, which
has various properties such as on-hit effects and upping the damage to
30.
add: Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.
balance: Made monkeys able to wield two-handed things again.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>

* Adds Summon Simians & Buffs/QoLs Mutate

* Updates our modular file to take this into account (I hate that this exists)

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@ users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [Iajret/Skyrat-tg](https://github.com/Iajret/Skyrat-tg)@[3782e4b710...](https://github.com/Iajret/Skyrat-tg/commit/3782e4b71098d12588696d9263f2ee8748caf9bf)
#### Thursday 2023-08-17 16:32:52 by Bloop

[MISSED MIRROR] Martian Food: A Taste of the Red Planet (#75988) (#23013)

Martian Food: A Taste of the Red Planet (#75988)

## About The Pull Request
Adds a selection of new foods and drinks based around Mars.
More information on Mars can be found here:
https://github.com/tgstation/common_core/blob/master/Interesting%20Planets/Human%20Space/The%20Sol%20System.md
To summarise for the general audience, Mars is a vital colony of the
Terran Federation, having been primarily settled (at least originally)
by Cybersun Industries to harvest its lucrative supplies of plasma, the
second largest in human space behind Lavaland. This has given Mars a
diverse culture evolving from the mostly East Asian colonists, and their
food reflects this.

Thanks to Melbert for their work on the soup portion of this PR.

The food:
Martian cuisine draws upon the culinary traditions of East Asia, and
adds in fusion cuisine from the later colonists. Expect classics such as
ramen, curry, noodles and donburi, as well as new takes on the formula
like the Croque-Martienne, Peanut Butter Ice Cream Mochi, and the
Kitzushi- chilli cheese and rice inside a fried tofu casing. Oh, and
lots of pineapple. The Martians love pineapple:

![image](https://github.com/tgstation/tgstation/assets/58124831/c9ae33a1-e03a-4f94-8ce0-8ad124e88e8d)
Also included are some foods for Ethereals, which may or may not be
hinting at something I've got planned...

The drinks:
Four new base drinks make their way to the game, bringing with them a
host of new cocktails: enjoy new ventures in bartending with Coconut
Rum, Shochu/Soju, Yuyake (our favourite legally-distinct melon liqueur),
and Mars' favourite alcoholic beverage, rice beer. Each is available in
the dispenser, as well as bottles in the booze-o-mat:

![image](https://github.com/tgstation/tgstation/assets/58124831/914a6e2a-7ef5-4791-ae31-d08fa9211083)

The recipes:
To make your (and the wiki editors) lives easier, please find below the
recipes for both foods and drinks:
Food: https://hackmd.io/@EOBGames/BkVFU0w9Y
Drinks: https://hackmd.io/@EOBGames/rJ1OhnsJ2
## Why It's Good For The Game
Another lot of variety for the chef and bartender, as well as continuing
the work started with lizard and moth food in getting Common Core into
the game in a tangible and fun way.
## Changelog
:cl: EOBGames, MrMelbert
add: Mars celebrates the 250th anniversary of the Martian Concession
this year, and this has brought Martian cuisine to new heights of
popularity. Find a new selection of Martian foods and drinks available
in your crafting menu today!
/:cl:

---------

Co-authored-by: EOBGames <58124831+EOBGames@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Nerev4r/Skyrat-tg](https://github.com/Nerev4r/Skyrat-tg)@[f08ce907dd...](https://github.com/Nerev4r/Skyrat-tg/commit/f08ce907ddc90398f56e449a2dc29e1d1ea22278)
#### Thursday 2023-08-17 16:57:14 by SkyratBot

[MIRROR] Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome [MDB IGNORE] (#23012)

* Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome (#77277)

## About The Pull Request

Lepton Violet (wabbajack) shuttle must be unlocked by having some form
of polymorph happen in-game first (Pride Mirror or the cursed springs
are the most accessible sources)

Scrapheap shuttle can only be bought if the Cargo budget is below 600
credits, and the shuttle has just less than half of its usual refueling
time left. However, it gives the cargo budget an influx of 3000 credits!

Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.

## Why It's Good For The Game

First off, here is my reasoning for why these need altering at all.

Players will always naturally gravitate to the wackiest and
most-out-there options, in this case this applies to shuttles. It's why
the Monastery or the Asteroid or Daniel are reasonably common sights,
more common than some of the 'boring' shuttle options that don't need
unlock with an emag.

The problem here, as I see it, is that there is no incentive
what-so-ever to NOT purchase these 'wacky' shuttles. Some of the
shuttles in the code are just way too stupid to be seen on most or even
some rounds (Arena, Disco Inferno?), so they require rare unlocks to
occur. Wacky shuttles being spammed round after round are bad due to
several reasons:
1. Players will run every joke to the ground. Wacky conditionless
shuttles take up a large amount of space in the shuttle memeplex, so
they are disproportionately seen in comparison to any of the
less-extravagant but more grounded and actually interesting options.
(Medisim? Monkeys anyone?). This ends up making the wacky shuttles
actually *less* wacky and just the stale and boring options.
2. Wacky shuttles affect the end-round quite a lot. This is fine, of
course, but not when these wacky shuttles can be seen every round.
3. These wacky shuttles don't have proper facilities. None of them have
a good medical section, or emergency supplies, or enough room. This gets
pretty annoying pretty fast.
4. One Funny Guy (the quintessential example being the clown with a dead
captain's ID) is all but guaranteed to try to buy the funniest and most
annoying shuttle to piss off the rest of the crew. With how Funny and
Annoying these shuttles are, not to mention how dirt-cheap they are (or
literally give you money!), they're easily the most seen alternate
shuttles, which isn't good when they alter how the round-end plays so
heavily.

> Lepton Violet (wabbajack) shuttle must be unlocked by having some form
of polymorph happen in-game first (Pride Mirror is the most accessible
source)

The Wabbajack has a endless source of voluntary Polymorphs with a
comically low price, which means it is purchased endlessly by crew, not
to mention being literally a source of free syndiborgs and xenos. While
I'm not a balanceposter, this does come with some annoyances especially
for antagonists who just randomly get blown up by an assault borg. This
is fine and fun every so often, but not as a common occurrence, not as a
guaranteed every-round option. I think it's an excellent candidate for
an unlock condition.

> Scrapheap shuttle can only be bought if the Cargo budget is below 600
credits, and the emergency shuttle is more than halfway refueled.
However, it gives the cargo budget an influx of 3000 credits!

This is LITERALLY 'haha grief shuttle', I have no idea how it even got
in as a condition-less shuttle. You see the captain buy it For No Raisin
Lul 2 minutes in, sigh to yourself, and secure an EVA suit when the
shuttle lands to try to survive in the unbelievably cramped space.
(Someone always blows it up.)

Instead of being JUST Grief Shuttle, now it has some interesting reasons
to exist. Revs and you're dirt-poor? Nukies just declared war after the
Clown bought ten crates of creampie dufflebags? Buy this shuttle and get
an influx of money.

> Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.

This one isn't as egregious as the above, but I believe my personal
dislike of it extends to a game design level, to an extent. One person
can buy this shuttle and the crew as a whole are left to groan as they
prepare for a noisy, confusing shuttle in which everyone is ten tiles
shifted to their left as their sprite does the most ridiculous dance
seen in SS13 history. 'Just turn the music off!': I'm glad this is an
option, but it doesn't change how much this shuttle alters things. It's
fine as a sendoff to a nice, chill greenshift, but as a constant sight
in red shifts it's just... frustrating. And purchased BECAUSE it's
frustrating, to the short-lived schadenfreude of one person and the
frustration of others.

And then the unbreakable disco machine. Why is it unbreakable. If the
crew doesn't want to listen to the thing, let them break it? Buy Disco
Inferno if you want an unbreakable disco.

Some of these changes are probably over-the-top, but remember that these
will still be seen in-game, just a bit rarer. Worst case scenario the
shuttle replacement event will let them have their time in the
limelight.

## Changelog

:cl:
balance: Lepton Violet (wabbajack) shuttle must be unlocked by having
some form of polymorph happen in-game first (Pride Mirror or the cursed
springs are the most accessible sources)
balance: Scrapheap shuttle can only be bought if the Cargo budget is
below 600 credits, and the shuttle has just less than half of its usual
refueling time left. However, it gives the cargo budget an influx of
3000 credits!
qol: Uncle Pete's Rollerdome has had its price increased, and the disco
machine is no longer unbreakable.
/:cl:

* Restricts Scrapheap & Lepton Violet behind conditions, alters Rollerdome

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [crawl/crawl](https://github.com/crawl/crawl)@[6656212320...](https://github.com/crawl/crawl/commit/66562123206107b4e469b57e8098b9c7ca6ab157)
#### Thursday 2023-08-17 17:08:41 by Nicholas Feinberg

Feat: hot pursuit (elliptic)

Not to be confused with the similar-sounding apparel beloved of
certain players, 'hot pursuit' is a new mechanic to encourage fun
lines of play.

A Brief History
---------------

When in a very nasty spot (low on HP and next to a tough foe), players
have historically been able to 'pillar-dance', wasting time (both the
game's and theirs) to get time to heal. This is both unfun to do and
narratively unsatisfying. When in a tight spot, players should pull out a
cool trick (a spell, god ability or consumable), fight, and/or die!

We first tried to fix this by adding 'random energy', which unfortunately
fixed nothing. Then we tried 'attacks of opportunity', letting monsters
attack when the player moved away. These worked somewhat, but had several
disadvantages, including:

- They were very complex. The list of special cases for which monsters
  could attack the player and when was very long, and it was hard for
  players to track.
- They were very binary. If a monster was next to the player, danger was
  vastly higher than if they were 2 tiles away. If a monster was as fast
  as the player, danger was vastly higher than if they were just a bit
  slower.
- They had odd and unintuitive interactions with polearms (which didn't
  launch reaching attacks of opportunity).
- They were frustrating. Players felt profoundly unhappy when they were
  killed by attacks of opportunity - it felt like the game becoming more
  hostile.

So, let's try something a bit gentler

Hot Pursuit
-----------

When the player moves away from a monster, if that monster then moves
toward the player, they have a one in ten chance of putting on a 'burst
of speed', moving ~25% faster (move delay 0.8) for the next ~20ish turns.
This speed bonus affects the move that triggered it, so players walking
away from an adjacent yak have a 2% chance of getting a surprise bap
from them.

The intent is to again discourage 'pillar-dancing' and other fiddly
stalling tactics (e.g. running across the entire level to get to stairs)
in a 'softer', fuzzier way, without the hard binaries of attacks of
opportunity.

Wu Jian martial manuevers and Serpent's Lash again give immunity to
this effect.

Let's try it out!

---
## [Mission23/Mission23](https://github.com/Mission23/Mission23)@[9d44b51718...](https://github.com/Mission23/Mission23/commit/9d44b5171880b27b4450484c6a2872313ab82d7b)
#### Thursday 2023-08-17 17:19:18 by Micah

Letterhead image from their response... 05-06-20231

This letterhead "logo" was created by the CIA.  The CIA took that photo in Mount Calvary when their church, Emmanuel Baptist visited on a Sunday.  That is their choir.  All fake, they were casing the place.  I need every fucking church in Kentucky contacted...  If Emmanuel Baptist Church has been there with their shitty choir, they're in harm's way.

Emmanuel is their misspelling.

---
## [facebook/react](https://github.com/facebook/react)@[ac1a16c67e...](https://github.com/facebook/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Thursday 2023-08-17 17:26:17 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [Maetrim/DDOBuilder](https://github.com/Maetrim/DDOBuilder)@[2e4e4388e5...](https://github.com/Maetrim/DDOBuilder/commit/2e4e4388e5603855fd3c02f49b44a82790d7c5aa)
#### Thursday 2023-08-17 17:44:34 by Maetrim

Build 1.0.0.190

Fix: "Fury of the Wild: Sense Weakness" can now correctly have all ranks trained for a single rank of "Mantle of Fury"
Fix: "Human: Greater Heroism" now correctly requires 15 AP spent in the tree to train (Reported in game by ....)
Fix: "Combat Style" bonuses no longer erroneously stack (Reported by Bjond)
Fix: Fury of the Wild: Lore of the Wilds now grants 0.5% Quality Hitpoints per Wilderness Lore feat you have (Reported by Bjond)
---Percentage bonuses to values are now shown to 1dp when appropriate
Fix: Item "Dinosaur Bone Buckler" now only counts once to the Dread Isle set bonus (Reported by Bjond)
Fix: Set bonus "Legendary Dreadkeeper" now grants +4 INT (Reported by Bjond)
Fix: Item "Epic Hyena Claw Necklace" now has its missing green augment slot (Reported by Bjond)
Fix: Item "Epic Cape of the Roc" now has its correct augment slots (Reported by Bjond)
Fix: Feat "Scion of the Astral Plane" should now only grant the additonal +4 doublestrike/shot if you are centered (Reported by Bjond)
Fix: Enhancement "Thief-Acrobat: Spinning Staff Wall" no longer erroneously grants +20% Competence bonus to HP (Reported by Bjond)
Fix: "Reset tree" actions should now work correctly after a reference to a variable going out of scope was fixed (Reported by Bjond)
Fix: "Barbarian DR" % from all sources should now correctly stack (Reported by Bjond)
Fix: "Unyielding Sentinel: Deific Resilience" effects now work correctly (Reported by Bjond)
Fix: Granted feats and effects should behave better as the applied list and the feat list are now kept in the same order
New: Right clicking a selected feat will now clear that feat selection in the class and level view
New: Universal enhancement trees are no longer auto assigned to enhancement tree slots in the enhancements view

U61 Changes:
---Harper Agent
------Cores 1, 6, and 18 now give +1 To-hit and Damage and not just hit/damage versus Evil.
------Core 20 now gives +2 to all ability scores, +1 hit/damage, +5 hit/damage vs Evil, and +20 Universal Spell Power.
------Weathered Traveler Tier 1 now gives 2/4/6 Energy Resistance.
---Swashbuckler
------Battering Barrage cost reduced from 2/rank to 1/rank.
------Thread the Needle now gives +5% to-hit (percentage bonus based on precision) while Precision is toggled on.
---Warchanter
------Spinning Ice, Frozen Fury, and Skaldic Scream now use the highest of Dexterity, Charisma, or Strength for their DCs.
------Their DCs are now (0x bard level / 1/2 bard level / 1x bard level) and (10/12/14) (Skaldic Scream is 1x bard level and 14.)
------Spinning Ice is now a 3/4/5[W] Cleave.
------Northwind's cost has been reduced from 2/rank to 1/rank.
---Sorcerer Savant
------Tier 5 Actives scale with highest of Charisma or Constitution, and not just Constitution.
------Earthen Armor (Tier 4 Earth Savant) is now +3/+6 Armor Class.
---Ninja Spy
------Tier 2 and Tier 4 Dark Ki upgrades now grant +1 to hit and +2 to damage to match similar enhancement lines.
------Tier 5 Touch of Despair now grants +3 To-hit and +3 to damage to match similar enhancement lines.
---Shintao
------Tier 2 and Tier 4 Light Ki upgrades now grant +1 To-hit and +2 to damage to match similar enhancement lines.
---Henshin Mystic
------Lighting the Candle now applies the fire portion of its imbue to Ki Spells.
---Class: Monk
------Quivering Palm has a new DC formula: DC 10 + monk level + highest of Dex or Wis mod + assassinate bonuses.
------It also now gains +2 DC on a failed saving throw.
---Assassin
------All of the active poison attacks up the line are now +3W, use full rogue level for their DCs instead of half, factor in assassinate bonuses for their DC, and now make certain enemies that would be immune to poison, weak to poison.
---------Ice Chill = Undead
---------Heartseeker = Elementals
---------Soulshatter = Outsiders
---Vistani
------Kukris now function with this tree, with the exception of the core 12, which only gives +1 multiplier (this keeps them in parity crit-wise with daggers as they naturally have +1 threat range over them.)
---Archmage
------Master of Magic (Core 20) now also grants +20 Universal Spell Power, and increases from +2 Intelligence to +4 Intelligence.
------Efficient Metamagics have their Action Point cost reduced from 2 to 1, since AM having metamagics be good seems flavorful.
------Spell Penetration has its AP cost reduced from 2 to 1.
------Energy of the Scholar has its AP cost reduced from 2 to 1, matching other trees.
------Cores 12 and 18 now grant a generic +1 to caster level and max caster level.
---Vanguard
------Stunning Shield cooldown reduced to 45/30/15 seconds.
------Shield Rush cooldown reduced to 40/30/20 seconds.
---Morgrave University now has its 3rd Favor tier (+2 saves versus magical beasts)

---
## [Maetrim/DDOBuilderV2](https://github.com/Maetrim/DDOBuilderV2)@[b990375aa0...](https://github.com/Maetrim/DDOBuilderV2/commit/b990375aa0832cfc975a3f402ab8882d23daddcd)
#### Thursday 2023-08-17 17:54:09 by Maetrim

Build 2.0.0.6

---Druid Wild Shape feats will now auto-populate where possible
---Druids/Blightcasters will now prioritise Heal and Spellcraft skills for an Autobuy action
---Class "Blight Caster" renamed to "Blightcaster" to match game
---Granted feats will now definitely clear on a New build/Life (attempt 3)
---Base level 3 quests added to the quest list
---Eldritch Blast dice (d8's) breakdown now works
---Pact dice (d6's) are now tracked separately from blast dice
---New stance group "Blast Shape" added and stances for all shapes added
---Medium Armor effect in "Enlightened Spirit: Shape Vestments" fixed
---Tree "Enlightened Spirit" reviewed for text to match wiki and text layout
---Tree "Tainted Scholar" reviewed for text to match wiki and text layout
---Tree "Soul Eater" reviewed for text to match wiki and text layout
---Tree "Archmage" reviewed for text to match wiki and text layout
---Tree "Eldritch Knight (Wizard)" reviewed for text to match wiki and text layout
---Fixed base Pale Master core effects
---Tree "Pale Master" reviewed for text to match wiki and text layout
---Tree "Vanguard" reviewed for text to match wiki and text layout
---Skill Tome progression assumed to be +1 every 4 additional levels for tomes beyond +5 (future support)
---Skill view total will now correctly update on a skill value change
---Tier 5 Machrotechnic tree items now have the correct DP cost of 1
---All Archetype past lives will appear next to the Base class in the past lives list
---Item tooltips with set bonuses will now show the set bonus icon
---Bonus Racial and Universal APs now get counted again
---The documents previously selected Life/Build will now be saved/restored on file save/load
---Half Class Level DCs will now show the correct class name
---Slider value changes will now correctly update breakdown effects which are dependent on things like "50% Hitpoints"
---Enhancement that only require (N) ranks of a given enhancement to train will now be correctly trainable (e.g. Fury of the Wild: Sense Weakness only requires 1 rank for Mantle of Fury to take all 3 ranks))
---Enhancement requirements that require a set number of ranks will now display that as a requirement
---Life/Build add/remove log entries will now appear in the correct position
---Life/Build selection will now add a log entry
---Universal enhancement trees are no longer auto assigned to an enhancement tree selection
---Soul Vessel augments such as Wild Fortitude now say the correct amount of +3 Artifact bonus to <Ability>, rather than +4
---Enhancement "Shadar-Kai: Assassin's Mark" now correctly has 1 stack, not 3.
---Enhancement "Shadar-Kai: Displacement" now correctly costs 1ap not 2.
---The Favor Pane quests are now full row select
---The list control column header can now be used to sort the columns
---Favor entries for each faction are now shown (currently totals a random favor for testing purposes)

U61 Support
---Harper Agent
------Cores 1, 6, and 18 now give +1 hit and damage and not just hit/damage vs evil
------Core 20 now gives +2 to all ability scores, +1 hit/damage, +5 hit/damage vs evil, and +20 universal spell power
------Weathered Traveler t1 now gives 2/4/6 energy resist
---Swashbuckler
------Battering Barrage cost reduced from 2/rank to 1/rank
------Thread the Needle now gives +5% to-hit (percentage bonus based on precision) while precision is toggled on
---Warchanter
------Spinning Ice, Frozen Fury, and Skaldic Scream now use the highest of dex, cha, or str for their DCs
------Their DCs are now (0x bard level / 1/2 bard level / 1x bard level) and (10/12/14) (Skaldic Scream is 1x bard level and 14)
------Spinning Ice is now a [3/4/5][W] cleave
------Northwind cost reduced from 2/rank to 1/rank
---Sorcerer Savant
------T5 Actives scale with highest of Cha or Con and not just con
------Earthen Armor (t4 earth savant) is now +3/+6 AC
---Ninja Spy
------Tier 2 and Tier 4 Dark Ki upgrades now grant +1 to hit and +2 to damage to match similar enhancement lines
------Tier 5 Touch of Despair now grants +3 to hit and +3 to damage to match similar enhancement lines
---Shintao
------Tier 2 and Tier 4 Light Ki upgrades now grant +1 to hit and +2 to damage to match similar enhancement lines
---Henshin Mystic
------Lighting the Candle now applies the fire portion of its imbue to Ki Spells
---Class: Monk
------Quivering Palm has a new DC formula: DC 10 + monk level + highest of Dex or Wis mod + assassinate bonuses
---Assassin
------All of the active poison attacks up the line are now +3W, use full rogue level for their DCs instead of half, and now make certain enemies that would be immune to poison, weak to poison.
---------Ice Chill = Undead
---------Heartseeker = Elementals
---------Soulshatter = Outsiders
---Vistani
------Kukris now function with this tree, with the exception of the core 12, which only gives +1 multiplier (this keeps them in parity crit-wise with daggers as they naturally have +1 threat range over them)
---Archmage
------Master of Magic (Core 20) now also grants +20 Universal Spell Power, and increases from +2 INT to +4 INT
------Efficient Metamagics have their AP cost reduced from 2 to 1, since AM having metamagics be good seems flavorful
------Spell Penetration has its AP cost reduced from 2 to 1
------Energy of the Scholar has its AP cost reduced from 2 to 1, matching other trees
------Cores 12 and 18 now grant a generic +1 to caster level and max caster level
---Vanguard
------Stunning Shield cooldown reduced to 45/30/15 seconds
------Shield Rush cooldown reduced to 40/30/20 seconds

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[c8266cf0a2...](https://github.com/tgstation/tgstation/commit/c8266cf0a2effaf8b931ba870c124608305b7d68)
#### Thursday 2023-08-17 18:09:10 by necromanceranne

Settler Quirk: Tame the Outdoors! Have trouble with tall shelves... (#77654)

## About The Pull Request

Adds the Settler quirk. This gives you bonuses to taming animals and
fishing, as well as making you gain hunger slower than others.

However, you are quite a bit slower than most people, and have trouble
with vaulting objects. You do, however, suffer significantly less from
equipment slowdown. (to the point that it is almost zero)

Settler riders are faster on their mounts than others if they're at
least sane. They start to slow down if they're less sane.

You are also shorter than most people. 

<details>
  <summary>Typical Settler encounters the typical Spacer</summary>
  

![Dr_Xr1nU0AAMsSE](https://github.com/tgstation/tgstation/assets/40847847/86ed4947-de5f-4bdf-a8ae-521dc7c30662)
  
</details>

## Why It's Good For The Game

I wanted to add a lightweight quirk that was kind of the 'opposite' of
Spacer, but a little more focused on interacting with elements of the
game world that would enjoy some attention. So, I thought 'what about an
outdoorsman quirk?'

So, I based it around being from people who lived out on the rim, under
unideal circumstances (and probably heavier gravity than Earth), and
taming the land. The slower movespeed encourages finding an animal to
tame that you can ride, and the bonuses to taming should help make that
a bit easier. The other additions just made sense for someone living it
a bit rough in the wilderness.

Having a bunch of settlers taming cows and riding around on them all
shift just kind of sounds hilarious to me.

## Changelog
:cl:
add: Settler quirk! Conqueror the great outdoors....in space. Just make
sure nobody asks you to get anything from the top shelf.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [zziger/supercow-widescreen-fix](https://github.com/zziger/supercow-widescreen-fix)@[8263d3106b...](https://github.com/zziger/supercow-widescreen-fix/commit/8263d3106b5dc97ae27aa89f5c4c4e7238e23ec6)
#### Thursday 2023-08-17 18:28:05 by Creepobot Neo

With every fucking commit i hate my life more and more

---
## [Kobun42/SVMLTool](https://github.com/Kobun42/SVMLTool)@[b7b3ac096a...](https://github.com/Kobun42/SVMLTool/commit/b7b3ac096a44c9c64e071f267b55e879bc21dacf)
#### Thursday 2023-08-17 18:58:45 by Kobun42

comment some more shit so i don't look like a fucking idiot

---
## [archie122/100-days-of-code](https://github.com/archie122/100-days-of-code)@[a4209ede39...](https://github.com/archie122/100-days-of-code/commit/a4209ede3930e918c541ff90e248be81f1c652e6)
#### Thursday 2023-08-17 19:00:14 by Archie

Day 46

Today was honestly shit. I really tried to understand how to use the Python library Spotipy. I seriously tried my hardest however, I just could not get it to function properly. It is so obtuse, so stupidly, made and so difficult to work with that. I honestly give up. If I have to make a Spotify playlist creator, I will just use the Spotify web API. And not use this honestly terrible library.

---
## [queer-group/queer.group](https://github.com/queer-group/queer.group)@[d7e2a5c6e7...](https://github.com/queer-group/queer.group/commit/d7e2a5c6e734dac918fb0cacffd23f839599d199)
#### Thursday 2023-08-17 19:05:40 by hjhornbeck

Dockerfile update (#1270)

While Docker isn't officially supported by Hometown, leaving the
Mastodon 3.5.5 Docker configuration in place with the new 4.0.2 code is
a bad idea. At minimum, you'll have a stale Node install that's months
behind on security updates. There are some minor tweaks to the default
configuration, but they're flagged by comments so they're easy to revert
or modify as necessary.

#  Running Hometown on Docker

I'll by typing up my own longer blog post in due time, but there's no
harm dropping a cheat sheet here. By following this outline, I was able
to upgrade a Hometown 1.0.8 install to 1.1.0 with nothing worse than a
minute or two of downtime.

My configuration uses the GitHub repository as its source, rather than
images drawn from DockerHub. I like to tweak and fiddle with my setup,
especially the themes, and I'm happy to sacrifice some disk space for
the privilege.

## Installing from Scratch

This is by far the easiest approach, you just follow [one
of](https://gist.github.com/TrillCyborg/84939cd4013ace9960031b803a0590c4)
the [existing
guides](https://sleeplessbeastie.eu/2022/05/02/how-to-take-advantage-of-docker-to-install-mastodon/)
for running Mastodon via Docker, pause after you've set up
`.env.production`, add any Hometown-specific features to it [as per the
Wiki](https://github.com/hometown-fork/hometown/wiki), then resume what
the guide says to do.

If you're enabling ElastiSearch, the second of the two guides has some
additional actions you'll need to do, plus be aware of [this
bug](https://github.com/mastodon/mastodon/issues/18625) in Mastodon
which can quietly block ES from working at all.

## Upgrading from Hometown 1.0.8

Here's how I accomplished this. I committed any leftover changes, then
ran these commands from the non-Docker instructions in the root of my
local Hometown repository:

```
git remote update
git checkout v4.0.2+hometown-1.1.0
```

This "wiped out" my customizations, but as I committed them all to a
branch I can reconstruct them later via diffs. I then ran:

```
sudo docker-compose build
```

to build the new image. The old image will continue running in the
background, as per usual. I like adding `2>&1 | less` to the end and
mashing `PgDn`, as if a compilation error happens it almost invariably
requires scrolling back a few screens to find the issue.

If the build succeeded, we're almost clear to start the dangerous
portion. If you're running on the cloud, now would be a great time to
take a snapshot. Whatever the case, you should back up the existing
database. If you haven't changed the defaults from the Dockerfile, then

```
sudo docker exec -it hometown_db_1 pg_dump -U postgres -Fc postgres > hometown.db.dump
```

should do the trick. If you have changed the defaults, you may need to
use `sudo docker ps` to figure out the name of the PostgreSQL image to
swap in place of "hometown_db_1", then browse through `.env.production`
to extract the username to place after `-U` and the database name to
place after `-Fc`. The Hometown docs don't say how to restore the
database should the process go South, but after reading a manpage or two
I think the magic words are roughly

```
sudo docker exec -it hometown_db_1 pg_restore -U postgres --clean --if-exists -d postgres < hometown.db.dump
```

Now we're ready for the scary "you could destroy everything" part. All
the earlier commands are trivial to roll back, but after this point any
delay could cause data corruption. As per the Hometown docs, run the
pre-deployment database migrations.

```
sudo docker-compose run -e SKIP_POST_DEPLOYMENT_MIGRATIONS=true -e RAILS_ENV=production --rm web bundle exec rails db:migrate
```

where `web` is the name of the webserver image in `docker-compose.yml`.
The docs state you should precompile all assets next, but I'm 95% sure
they were already built when you ran `sudo docker-compose build`. If
you're paranoid and want to be absolutely sure precompilation is done,
then at this stage run:

```
sudo docker-compose run -e RAILS_ENV=production --rm web bundle exec rails assets:precompile
```

Here, the Hometown docs say you should run the post-deployment
migrations. In Docker-ese:

```
sudo docker-compose run -e RAILS_ENV=production --rm web bundle exec rails db:migrate
```

Finally, we need to stop the old images and spin up the new ones. Run:

```
sudo docker-compose up -d
```

and give Docker some time to finish rotating. A quick `sudo docker ps`
should confirm the new images are booting up, and in a short while
(10-15 seconds for the teeny-tiny instance I manage) you should be back
to fully functional.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a2ee4ec813...](https://github.com/tgstation/tgstation/commit/a2ee4ec813c38741d593e5e1731764458c77b811)
#### Thursday 2023-08-17 19:09:59 by Jacquerel

Polymorphic Inverter tweaks (#77675)

## About The Pull Request

Fixes #77649

You can no longer use the belt to turn into any kind of carbon mob,
sorry gamers it was a cool dream but it leads to too many problems.
Also I made space dragon "there's an alive guy in my stomach" code now
work on signals instead of on Life tick which is slightly more efficient
and also resolves an issue with the funny belt.

## Why It's Good For The Game

Too much room for weird edge cases as a result of doing this (messing
with monkey DNA, producing infinite xeno organs, blocking legit xeno
queens from being created) which had no graceful solution.
Moving stuff off Life if it can be event based is nice.

## Changelog

:cl:
fix: Turning into a space dragon with the polymorphic inverter will no
longer leave you existing in two places
balance: You can no longer use the belt to transform into monkeys or
xenomorphs, for technical reasons.
/:cl:

---
## [kartik-commits/android_kernel_xiaomi_sm7325](https://github.com/kartik-commits/android_kernel_xiaomi_sm7325)@[870e7d7108...](https://github.com/kartik-commits/android_kernel_xiaomi_sm7325/commit/870e7d7108432f0c6fad2dec6ef6060d4ee49169)
#### Thursday 2023-08-17 19:14:18 by Darrick J. Wong

xfs: change the order in which child and parent defer ops are finished

commit 27dada070d59c28a441f1907d2cec891b17dcb26 upstream.

The defer ops code has been finishing items in the wrong order -- if a
top level defer op creates items A and B, and finishing item A creates
more defer ops A1 and A2, we'll put the new items on the end of the
chain and process them in the order A B A1 A2.  This is kind of weird,
since it's convenient for programmers to be able to think of A and B as
an ordered sequence where all the sub-tasks for A must finish before we
move on to B, e.g. A A1 A2 D.

Right now, our log intent items are not so complex that this matters,
but this will become important for the atomic extent swapping patchset.
In order to maintain correct reference counting of extents, we have to
unmap and remap extents in that order, and we want to complete that work
before moving on to the next range that the user wants to swap.  This
patch fixes defer ops to satsify that requirement.

The primary symptom of the incorrect order was noticed in an early
performance analysis of the atomic extent swap code.  An astonishingly
large number of deferred work items accumulated when userspace requested
an atomic update of two very fragmented files.  The cause of this was
traced to the same ordering bug in the inner loop of
xfs_defer_finish_noroll.

If the ->finish_item method of a deferred operation queues new deferred
operations, those new deferred ops are appended to the tail of the
pending work list.  To illustrate, say that a caller creates a
transaction t0 with four deferred operations D0-D3.  The first thing
defer ops does is roll the transaction to t1, leaving us with:

t1: D0(t0), D1(t0), D2(t0), D3(t0)

Let's say that finishing each of D0-D3 will create two new deferred ops.
After finish D0 and roll, we'll have the following chain:

t2: D1(t0), D2(t0), D3(t0), d4(t1), d5(t1)

d4 and d5 were logged to t1.  Notice that while we're about to start
work on D1, we haven't actually completed all the work implied by D0
being finished.  So far we've been careful (or lucky) to structure the
dfops callers such that D1 doesn't depend on d4 or d5 being finished,
but this is a potential logic bomb.

There's a second problem lurking.  Let's see what happens as we finish
D1-D3:

t3: D2(t0), D3(t0), d4(t1), d5(t1), d6(t2), d7(t2)
t4: D3(t0), d4(t1), d5(t1), d6(t2), d7(t2), d8(t3), d9(t3)
t5: d4(t1), d5(t1), d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)

Let's say that d4-d11 are simple work items that don't queue any other
operations, which means that we can complete each d4 and roll to t6:

t6: d5(t1), d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)
t7: d6(t2), d7(t2), d8(t3), d9(t3), d10(t4), d11(t4)
...
t11: d10(t4), d11(t4)
t12: d11(t4)
<done>

When we try to roll to transaction #12, we're holding defer op d11,
which we logged way back in t4.  This means that the tail of the log is
pinned at t4.  If the log is very small or there are a lot of other
threads updating metadata, this means that we might have wrapped the log
and cannot get roll to t11 because there isn't enough space left before
we'd run into t4.

Let's shift back to the original failure.  I mentioned before that I
discovered this flaw while developing the atomic file update code.  In
that scenario, we have a defer op (D0) that finds a range of file blocks
to remap, creates a handful of new defer ops to do that, and then asks
to be continued with however much work remains.

So, D0 is the original swapext deferred op.  The first thing defer ops
does is rolls to t1:

t1: D0(t0)

We try to finish D0, logging d1 and d2 in the process, but can't get all
the work done.  We log a done item and a new intent item for the work
that D0 still has to do, and roll to t2:

t2: D0'(t1), d1(t1), d2(t1)

We roll and try to finish D0', but still can't get all the work done, so
we log a done item and a new intent item for it, requeue D0 a second
time, and roll to t3:

t3: D0''(t2), d1(t1), d2(t1), d3(t2), d4(t2)

If it takes 48 more rolls to complete D0, then we'll finally dispense
with D0 in t50:

t50: D<fifty primes>(t49), d1(t1), ..., d102(t50)

We then try to roll again to get a chain like this:

t51: d1(t1), d2(t1), ..., d101(t50), d102(t50)
...
t152: d102(t50)
<done>

Notice that in rolling to transaction #51, we're holding on to a log
intent item for d1 that was logged in transaction #1.  This means that
the tail of the log is pinned at t1.  If the log is very small or there
are a lot of other threads updating metadata, this means that we might
have wrapped the log and cannot roll to t51 because there isn't enough
space left before we'd run into t1.  This is of course problem #2 again.

But notice the third problem with this scenario: we have 102 defer ops
tied to this transaction!  Each of these items are backed by pinned
kernel memory, which means that we risk OOM if the chains get too long.

Yikes.  Problem #1 is a subtle logic bomb that could hit someone in the
future; problem #2 applies (rarely) to the current upstream, and problem

This is not how incremental deferred operations were supposed to work.
The dfops design of logging in the same transaction an intent-done item
and a new intent item for the work remaining was to make it so that we
only have to juggle enough deferred work items to finish that one small
piece of work.  Deferred log item recovery will find that first
unfinished work item and restart it, no matter how many other intent
items might follow it in the log.  Therefore, it's ok to put the new
intents at the start of the dfops chain.

For the first example, the chains look like this:

t2: d4(t1), d5(t1), D1(t0), D2(t0), D3(t0)
t3: d5(t1), D1(t0), D2(t0), D3(t0)
...
t9: d9(t7), D3(t0)
t10: D3(t0)
t11: d10(t10), d11(t10)
t12: d11(t10)

For the second example, the chains look like this:

t1: D0(t0)
t2: d1(t1), d2(t1), D0'(t1)
t3: d2(t1), D0'(t1)
t4: D0'(t1)
t5: d1(t4), d2(t4), D0''(t4)
...
t148: D0<50 primes>(t147)
t149: d101(t148), d102(t148)
t150: d102(t148)
<done>

This actually sucks more for pinning the log tail (we try to roll to t10
while holding an intent item that was logged in t1) but we've solved
problem #1.  We've also reduced the maximum chain length from:

    sum(all the new items) + nr_original_items

to:

    max(new items that each original item creates) + nr_original_items

This solves problem #3 by sharply reducing the number of defer ops that
can be attached to a transaction at any given time.  The change makes
the problem of log tail pinning worse, but is improvement we need to
solve problem #2.  Actually solving #2, however, is left to the next
patch.

Note that a subsequent analysis of some hard-to-trigger reflink and COW
livelocks on extremely fragmented filesystems (or systems running a lot
of IO threads) showed the same symptoms -- uncomfortably large numbers
of incore deferred work items and occasional stalls in the transaction
grant code while waiting for log reservations.  I think this patch and
the next one will also solve these problems.

As originally written, the code used list_splice_tail_init instead of
list_splice_init, so change that, and leave a short comment explaining
our actions.

Signed-off-by: Darrick J. Wong <darrick.wong@oracle.com>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Reviewed-by: Brian Foster <bfoster@redhat.com>
Signed-off-by: Chandan Babu R <chandan.babu@oracle.com>
Acked-by: Darrick J. Wong <djwong@kernel.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [abarganier/cockroach](https://github.com/abarganier/cockroach)@[0f31d50b2f...](https://github.com/abarganier/cockroach/commit/0f31d50b2fd4de2980c294d47e87999f27e673c5)
#### Thursday 2023-08-17 19:46:14 by craig[bot]

Merge #107110 #107111 #107129 #107149 #107181 #107183

107110: kvserver: avoid running intensive decommission test under deadlock r=AlexTalks a=AlexTalks

The kvserver test `TestDecommission`, which runs a 5-node cluster and decommissions 4 of those 5 nodes, has trouble completing fast enough when under a race or deadlock configuration. While race configurations were already skipped, this modifies the test to be skipped under deadlock configurations as well.

Fixes: #106096

Release note: None

107111: compose: start `docker-compose` with a non-empty `PATH` r=rail a=rickystewart

`docker-compose` invokes `docker`, but obviously this will fail if there is nothing in the `PATH`.

Epic: none
Release note: None

107129: dev: reject builds when CRL JS dependencies are 'pnpm link'ed r=rickystewart a=sjbarag

When working with first-party JS dependencies that aren't in this monorepo, the idiomatic development workflow uses pnpm link [1] to link multiple JS packages together. Specifically, running `pnpm link /path/to/github.com/cockroachdb/ui/packages/foo` from within pkg/ui/workspaces/* creates a symbolic link at
node_modules/`@cockroachlabs/foo` that points to
../../(…)/ui/packages/foo. This works quite smoothly for local development, as changes in the 'foo' package are automatically seen by a `pnpm webpack --watch` running in CRDB. The two packages act like they're maintained in the same repo, while allowing independent version history, CI processes, etc.

Unfortunately, rules_js currently offers no way to link outside of the Bazel workspace. Such a symlink is either ignored by rules_js (since it doesn't appear in pnpm-lock.yaml) or is rejected if it's manually added to the lockfile [2]. Allowing Bazel-based builds of CockroachDB when 'pnpm link'ed packages are present introduces dependency skew between Bazel and non-Bazel builds. To allow `pnpm link` to be used safely, pre-emptively reject builds of 'cockroach' and 'cockroach-oss' that are run through the 'dev' helper when linked `@cockroachlabs/` packages are detected.

[1] https://pnpm.io/cli/link
[2] https://github.com/aspect-build/rules_js/issues/1165

Release note: None
Epic: none

-----

Example output: 
<img width="998" alt="image" src="https://github.com/cockroachdb/cockroach/assets/665775/3fd43abe-f5c2-4ddd-bc60-16a73db12836">

Total duration is 16ms on my machine since we're checking so few files. We can drop these into a goroutine per first-party JS if we want, but this is certainly fast enough to be conversational.

107149: opt: make functional dependency calculation deterministic r=DrewKimball a=DrewKimball

We recently added additional logic for inferring functional dependencies for join expressions. However, this logic iterates through a map, which leads to nondeterminism in which order functional dependencies are added to the FD set. Functional dependency calculation is best-effort, so this can lead to a different resulting FD set, which causes flaky tests. This patch makes the calculation deterministic by iterating instead through a `intsets.Fast` set.

Fixes #107148
Fixes #107162

Release note: None

107181: dev: when cross-building, use `-c opt` r=rail a=rickystewart

This enables optimizations which you probably want for a cross-build.

Epic: CRDB-17171
Release note: None

107183: acceptance: add log dir as a writable path r=rail a=rickystewart

Otherwise you get a sandbox error.

Epic: CRDB-17171
Release note: None

Co-authored-by: Alex Sarkesian <sarkesian@cockroachlabs.com>
Co-authored-by: Ricky Stewart <ricky@cockroachlabs.com>
Co-authored-by: Sean Barag <barag@cockroachlabs.com>
Co-authored-by: Drew Kimball <drewk@cockroachlabs.com>

---
## [newstools/2023-sundiata-post](https://github.com/newstools/2023-sundiata-post)@[e4e987d3f6...](https://github.com/newstools/2023-sundiata-post/commit/e4e987d3f69785a3b31599b5bcec39ba46ee6d9c)
#### Thursday 2023-08-17 19:57:44 by Billy Einkamerer

Created Text For URL [sundiatapost.com/dj-kaywise-confirms-girlfriends-allegations-that-his-twin-brother-was-involved-in-plot-to-allegedly-kidnap-her/]

---
## [Justice12354/tgstation](https://github.com/Justice12354/tgstation)@[7e1d97af9e...](https://github.com/Justice12354/tgstation/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Thursday 2023-08-17 20:40:19 by Justice

Removes the word "chemical" from "chemical patch" (#76966)

## About The Pull Request
In #76011, I bitched and moaned about how the ChemMaster gives patches a
huge ass name. I've talked to other Medical Doctor mains and I also
heard bitching about the word "chemical", which is just a pain in the
ass. It seems many of us just end up removing it because it's so
repetitive and makes the patch's name long fnr. I don't think the word
"chemical" is really needed in there since you can clearly tell it's a
chemical patch just by looking at the word "patch" and the sprite.

I don't think this should affect anything else in the game in a negative
way. In that same issue, it was suggested that the cap for names was
increased instead, but this also solves the issue of the word "chemical"
taking up so much space in the patch's name without touching unknown
lands.
## Why It's Good For The Game
Less words, more healing!
## Changelog
:cl:
qol: The word "chemical" has been removed from "chemical patch" when
printing patches
/:cl:

---
## [Justice12354/tgstation](https://github.com/Justice12354/tgstation)@[0d769e0ffa...](https://github.com/Justice12354/tgstation/commit/0d769e0ffaaa2b0f2be2edb9659c233860420ec1)
#### Thursday 2023-08-17 20:40:19 by Jacquerel

Removes two redundant components (#76866)

## About The Pull Request

We're starting to get to have enough components that people don't
realise that what they want already exists but doesn't have the name
they expect 🙃

I recently added `track_hierarchical_movement` which is similar enough
to `connect_containers` that it shouldn't independently exist, even if I
like sending a new signal more than the ugly setup pattern for
`connect_loc`.

`trait_loc` is actually older than `give_turf_traits` but
`give_turf_traits` covers more edge cases than `turf_loc` so seems like
the better one to maintain.
HOWEVER `give_turf_traits` held a list of references to atoms in it,
which isn't great in an element. I couldn't think of a way to completely
eliminate the list, but it isn't a list of references any more so it
shouldn't cause any hard deletions.

## Why It's Good For The Game

Having two components which do the same thing but marginally differently
is confusing and going to cause us trouble down the line.

## Changelog

Not player facing

---
## [NsimDaghash/codewars1003kyu6](https://github.com/NsimDaghash/codewars1003kyu6)@[9f9ecf865d...](https://github.com/NsimDaghash/codewars1003kyu6/commit/9f9ecf865d3c0bb78deabb57eab63124030ea3df)
#### Thursday 2023-08-17 20:54:46 by NsimDaghash

Fibonacci, Tribonacci and friends

If you have completed the Tribonacci sequence kata, you would know by now that mister Fibonacci has at least a bigger brother. 
If not, give it a quick look to get how things work.
Well, time to expand the family a little more: think of a Quadribonacci starting with a signature of 4 elements and each following element is the 
sum of the 4 previous, a Pentabonacci (well Cinquebonacci would probably sound a bit more italian, but it would also sound really awful) with a 
signature of 5 elements and each following element is the sum of the 5 previous, and so on.
Well, guess what? You have to build a Xbonacci function that takes a signature of X elements - 
and remember each next element is the sum of the last X elements - and returns the first n elements of the so seeded sequence.

---
## [yoctoproject/poky](https://github.com/yoctoproject/poky)@[a3c294691f...](https://github.com/yoctoproject/poky/commit/a3c294691fc1ceaddafd2dd870a6ecbbf313d5c6)
#### Thursday 2023-08-17 21:19:55 by Richard Purdie

pseudo: Fix to work with glibc 2.38

This adds a horrible hack to get pseudo working with glibc 2.38. We can't
drop _GNU_SOURCE to something like _DEFAULT_SOURCE since we need the defines
the gnu options bring in. That leaves using internal glibc defines to disable
the c23 versions of strtol/fscanf and friends. Which would break pseudo
build with 2.38 from running on hosts with older glibc.

We'll probably need to come up with something better but this gets glibc 2.38
and working and avoids autobuilder failures.

(From OE-Core rev: 596fb699d470d7779bfa694e04908929ffeabcf7)

Signed-off-by: Richard Purdie <richard.purdie@linuxfoundation.org>

---
## [niro1987/homeassistant-core](https://github.com/niro1987/homeassistant-core)@[ba0bd9913a...](https://github.com/niro1987/homeassistant-core/commit/ba0bd9913a0537804846f6b328781a039c25b570)
#### Thursday 2023-08-17 22:08:09 by Niels Perfors

Verisure unpack
<!--
  You are amazing! Thanks for contributing to our project!
  Please, DO NOT DELETE ANY TEXT from this template! (unless instructed).
-->
## Proposed change
<!--
  Describe the big picture of your changes here to communicate to the
  maintainers why we should accept this pull request. If it fixes a bug
  or resolves a feature request, be sure to link to that issue in the
  additional information section.
-->
`unpack` sometimes returned None and caused an error, shouldn't now.

## Type of change
<!--
  What type of change does your PR introduce to Home Assistant?
  NOTE: Please, check only 1! box!
  If your PR requires multiple boxes to be checked, you'll most likely need to
  split it into multiple PRs. This makes things easier and faster to code review.
-->

- [ ] Dependency upgrade
- [ ] Bugfix (non-breaking change which fixes an issue)
- [ ] New integration (thank you!)
- [ ] New feature (which adds functionality to an existing integration)
- [ ] Deprecation (breaking change to happen in the future)
- [ ] Breaking change (fix/feature causing existing functionality to break)
- [x] Code quality improvements to existing code or addition of tests

## Additional information
<!--
  Details are important, and help maintainers processing your PR.
  Please be sure to fill out additional details, if applicable.
-->

- This PR fixes or closes issue: fixes #
- This PR is related to issue:
- Link to documentation pull request:

## Checklist
<!--
  Put an `x` in the boxes that apply. You can also fill these out after
  creating the PR. If you're unsure about any of them, don't hesitate to ask.
  We're here to help! This is simply a reminder of what we are going to look
  for before merging your code.
-->

- [ ] The code change is tested and works locally.
- [ ] Local tests pass. **Your PR cannot be merged unless tests pass**
- [ ] There is no commented out code in this PR.
- [ ] I have followed the [development checklist][dev-checklist]
- [ ] I have followed the [perfect PR recommendations][perfect-pr]
- [ ] The code has been formatted using Black (`black --fast homeassistant tests`)
- [ ] Tests have been added to verify that the new code works.

If user exposed functionality or configuration variables are added/changed:

- [ ] Documentation added/updated for [www.home-assistant.io][docs-repository]

If the code communicates with devices, web services, or third-party tools:

- [ ] The [manifest file][manifest-docs] has all fields filled out correctly.
      Updated and included derived files by running: `python3 -m script.hassfest`.
- [ ] New or updated dependencies have been added to `requirements_all.txt`.
      Updated by running `python3 -m script.gen_requirements_all`.
- [ ] For the updated dependencies - a link to the changelog, or at minimum a diff between library versions is added to the PR description.
- [ ] Untested files have been added to `.coveragerc`.

<!--
  This project is very active and we have a high turnover of pull requests.

  Unfortunately, the number of incoming pull requests is higher than what our
  reviewers can review and merge so there is a long backlog of pull requests
  waiting for review. You can help here!

  By reviewing another pull request, you will help raise the code quality of
  that pull request and the final review will be faster. This way the general
  pace of pull request reviews will go up and your wait time will go down.

  When picking a pull request to review, try to choose one that hasn't yet
  been reviewed.

  Thanks for helping out!
-->

To help with the load of incoming pull requests:

- [ ] I have reviewed two other [open pull requests][prs] in this repository.

[prs]: https://github.com/home-assistant/core/pulls?q=is%3Aopen+is%3Apr+-author%3A%40me+-draft%3Atrue+-label%3Awaiting-for-upstream+sort%3Acreated-desc+review%3Anone+-status%3Afailure

<!--
  Thank you for contributing <3

  Below, some useful links you could explore:
-->
[dev-checklist]: https://developers.home-assistant.io/docs/development_checklist/
[manifest-docs]: https://developers.home-assistant.io/docs/creating_integration_manifest/
[quality-scale]: https://developers.home-assistant.io/docs/integration_quality_scale_index/
[docs-repository]: https://github.com/home-assistant/home-assistant.io
[perfect-pr]: https://developers.home-assistant.io/docs/review-process/#creating-the-perfect-pr

---
## [FalloutFalcon/Shiptest](https://github.com/FalloutFalcon/Shiptest)@[ee4021c507...](https://github.com/FalloutFalcon/Shiptest/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Thursday 2023-08-17 22:35:06 by Imaginos16

Destroying Sprite Cruft Part One: Cruft Sucks (#2220)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Title


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/1cedcdb1-01b5-4f28-a759-65428c2dcd0a)

In total, the:

- IV Drip
- All-In-One Grinder
- Book Binder
- Book Scanner
- Water Cooler
- Tank Dispenser

Have all been successfully uncrufted. No more cruft. Just clean sprites
now :D

Oh and dressers have directionals now at the request of @Bjarl 

Credit goes to the original authors in the changelog.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
begone cruft I fucking hate cruft
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy, Maxymax13, Wallemations, Kryson,
Viro/Axietheaxolotl, MeyHaZah
imageadd: Books, IV drips, tank dispensers, all-in-one grinders, water
coolers, book binders and book scanners have been resprited!
imageadd: Dressers now have directionals!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[6c34d93be7...](https://github.com/lizardqueenlexi/orbstation/commit/6c34d93be715012943626d0f812e99f730a536ef)
#### Thursday 2023-08-17 23:41:19 by necromanceranne

Nukies Update 7: Hats (Also massive uplink standardization, weapon kits and ammo changes) (#77330)

## About The Pull Request

Massively overhauls and standardizes the nuclear operative uplink. 

### Weapon Kits

Essentially, all the main weapons of the uplink have been changed to
instead come as 'weapon kits', which are essentially cases containing a
weapon loadout to enable operatives to easily start operating on only
just one item purchase, without the fuss of worrying whether or not
operatives are getting spare ammo, or getting relevant equipment for
success. Consider this a pseudo-loadout, though without necessarily
restricting the purchasing of more weapon kits.

All kits come in three categories: Low Cost (8 TC), Medium Cost (14 TC)
and High Cost (18 TC). This is also matched by categorized ammo costs;
Basic Ammo (2 TC), Hollow Point and Armour Penetrating (4 TC),
Incendiary (3 TC) and Special (or anything that does not easily fit
these categories and does something real extra) (5 TC). Weapons that
lacked these ammos have gained these ammo types to fill the gaps.

<details>
There is may one exception to this in disruptor ammo, which is priced as
basic ammo if only because it isn't _quite_ good enough to justify
pricing at 5 tc and I can see an op wanting to use it as a basic ammo
type instead of normal .50 BMG against, say, a silicon/mech heavy
opposition. Since it cannot kill organics on its own, I'll consider this
mostly basic-adjacent
</details>
The kits have also been labelled based on potential difficulty. This
reflects possible difficulties in using the item, how conducive it is to
success for how much game knowledge needed to actually use it, and how
likely an op is to succeed using it. I don't expect ops to win using
nothing but a rocket launcher, but I think ops should get a fair shake
at trying, yeah?

The kits are as below:
#### **Low-Cost**
_Bulldog (Moderate):_ Shotgun and three magazines of standard ammo.
_Ansem (Easy/Spare):_ Pistol and three spare magazines of standard ammo.
#### **Medium Cost**
_C-20r (Easy):_ SMG and three spare magazines of standard ammo.
_Energy Sword and Shield (Very Hard):_ Energy sword and shield. (Also a
special hat)
_Revolver (Moderate):_ Revolver and three speedloaders of standard ammo.
_Rocket Launcher (Hard):_ Rocket launcher with three spare rockets.
#### **High Cost**
_L6 SAW (Moderate):_ LMG, and that's it. No spare ammo.
_M-90gl (Hard):_ Rifle, two spare magazines of standard ammo and a box
of rubber grenades.
_Sniper (Hard):_ Sniper rifle, two spare magazine of standard ammo, and
one magazine of disruptor ammo. Also suit and tie.
_CQC (Very Hard):_ Comes with a stealth implant and a bandana.
_Double-Energy Sword (Very Hard):_ Double-energy sword, syndicate soap,
antislip module, meth injector and a prisoner jumpsuit.
_**NEW** Grenadier's Kit (Hard):_ Grenadier's belt and grenade launcher
(the one that launchers chem grenades). (I replaced the shit acid
grenade with another flashbang in the belt)

Surplus SMG (Flukie difficulty) has been unchanged. It just now comes
with two rations.

Includes two new revolver ammo types: Phasic, which goes through walls
and armor, but has significantly less damage as a result (I've equalized
the revolver damage and the rifle version's damage to 30 for both). And
Heartseeker, which has homing bullets. Both are Special ammo, and are
priced at 5 TC a speedloader.

### Other Gear

The other items in the uplink have also been consolidated and
standardized in various ways.

#### Grenades

Most now cost 15 TC for three grenades of any given type (including the
full fungal tuberculous). This is pretty much identical to the previous
price, just more consistent overall and front-loaded in cost.

#### Reinforcements

All the various reinforcements now cost 35 TC and all refundable,
equalizing cost to the average across the reinforcements. This is
primarily because I feel like all these options should be weighed
equally, and not one of these options are necessarily worse or better
than the other in their current balance. They're largely inaccessible
for normal ops regardless, and typically come out when there is a
discount or war ops. I took the average value and went with it. Not much
more to say.

#### Mechs

They're just cheaper. These things still suck and they need help.
They've always needed help. A slightly less excessive value for the
mechs may help see people willing to spend the TC on them. I doubt it. I
seriously suggest not buying these still. I keep them in primarily
because they are big stompy mechs and are kind of iconic 'war ops' gear.

#### Bundles

Since I've implemented weapon kits, gun bundles are rather redundant. So
the bulldog weapon and ammo bundle, the c20-r weapon and ammo bundle and
technically the sniper bundle were removed. The sniper bundle is now the
weapon kit, obviously.

Nothing else here really. Except for one....

#### Implants

Not much changed here. I standardized the implant prices to 8 TC a pop.
This is in accordance with traitor implants, which ops also get. So
everything in this category bar a few exceptions (like macro/microbombs)
are around 8 TC. Makes sense to me, really.

Importantly, I made the Implant bundle 25 TC, and I unrandomized the
contents. Who in the right fucking mind would spend 40 TC just to get
five reviver implants is beyond me. But instead, you get one of each of
the cybernetic implants except thermal eyes (you can just buy thermals
and get the benefit of both vision types; x-ray and thermal vision, if
you want to use smokescreens a lot).

#### Base Keys

They're all now 15 TC, except the fridge which is 5 TC. It's weird
they're valued differently when they are taken mostly to do gimmicks
like xenobio and toxins in a hurry before hitting the station. So we've
standardized it.

## Hat Crate

**YES, GOOD SIR, YOU TOO CAN ORDER A HAT CRATE FROM THE SYNDICATE STORE
FOR ONLY 5 TC!**

**NO NEED FOR A KEY, JUST BUY IT AND PULL IT OPEN WITH YOUR STANDARD
ISSUE CROWBAR!**

**ENJOY YOUR NEW CRATE! ENJOY YOUR NEW HAT!**

**PUT IT ON USING THE FREE HAT STABILIZERS WE INCLUDED WITH THE HATS!**

~~**NO REFUNDS IF YOU GET BLOOD ON YOUR HAT!**~~

<details>
There is a 1% chance to instagib people with direct hits from a rocket.
This does the crit effect.
</details>

## Why It's Good For The Game

The uplink needed more spring cleaning and standardization.

With this, I've partially implemented my older idea for ammo consistency
and initial allowance for nukies. Ammo is kind of over-priced and often
where a good chunk of TC goes towards without really pushing nukies
towards meaningful success. And it is often what is tripping up new
players who didn't think to get any. Now, when they get a gun, they get
ammo in their case. On top of this, the weapon kit category is both at
the top of the uplink AND has a little label to say 'Recommend', so that
these new players will hopefully know they should be looking there
first.

In addition, it is the gateway towards a concept that is currently being
worked on. Nuclear operatives having some degree of predefined loadouts
for players to select if they aren't sure what they want, or don't know
what to get. Nukies is very confusing for many players. So giving them a
fighting chance with some premade setups can help ease them into the
role without needing too much player knowledge in how to apply the
items. This is only one step towards that, so that players can identify
what gear they need to help succeed based on their skill.

I wanted to implement a difficulty warning so that players can choose
gear loadouts that are actually conducive to their skill and knowledge.
I based it on how much players would need to know to engage in combat
with it, and how much fiddling is required to get something to work
properly (overly involved reloading is a consideration, for example, as
well as precise button presses). In addition, how much of a force
multiplier some weapons can be for their ease of use.

Most people recognize the c20-r as the most new player friendly weapon,
as an example. So it would be good to steer players towards taking that
gun because of how easy it is to use, understand and succeed with it.

And most importantly of all; Having standards within the uplink is
important. Most of the values in the uplink are just completely random.
Nobody has a good grasp of what is too much or too little. Even just a
hint of consistency, and people will stick to it (see implants for what
I mean). And there is still some work to be done even there. A good
start is weapons. Price for power can be meaningful when decided whether
we want some weapons to come out more often than others. Players do
enjoy making informed decisions and choices, and having affordability be
a draw to some otherwise less powerful weapons (looking at you, Bulldog)
can actually be a worthwhile and meaningful difference.

~~I thought it would tick off the gun nerds to change the calibers on
the guns.~~

~~I also thought adding hats would be funny given the release of TF2's
most recent update.~~

## Changelog
:cl:
balance: Standardizes some of the nuclear operative entries to have more
consistent pricing within their respective categories.
add: Adds some new categories so that players have an easier time
navigating the nuclear operative uplink.
balance: Many items have had prices reduced or adjusted to make them
more desirable or more consistent within their category.
add: Weapon kits have replaced almost all the individual weapons in the
uplink. You now buy these instead of the individual weapon. These often
come with spare ammo or relevant gear for success.
add: Most ammo types have been standardized in price.
refactor; Removes a lot of redundant item entry code and tidies up the
actual code part of the nuclear uplink so that it is much easier to find
things within it.
add: Added 40 new cosmetic items to the Syndicate Store. Buy them now
from the Hat Crate, only 5 TC!
code: Updated the nuclear operative uplink files.
/:cl:

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[95ec0e6545...](https://github.com/lizardqueenlexi/orbstation/commit/95ec0e65458ece9c5c80952e75d5d32c4fbb794b)
#### Thursday 2023-08-17 23:41:19 by necromanceranne

Dissection experiments are handled by autopsy surgery. Removes redundant dissection surgery. You can repeat an autopsy on someone who has come back to life. (#77386)

## About The Pull Request

TRAIT_DISSECTED has had the surgical speed boost moved over to
TRAIT_SURGICALLY_ANALYZED.

TRAIT_DISSECTED now tracks if we can do an autopsy on the same body
again, and blocks further autopsies if it is on the mob. A mob that
comes back to life loses TRAIT_DISSECTED. This allows for mobs to be
autopsied once again.

Since it is completely redundant now (and was the whole time TBH),
dissections have been removed in favour of just having the experiment
track autopsies.

Fixes https://github.com/tgstation/tgstation/issues/76775

## Why It's Good For The Game

Today I showed up to a round where someone autopsied all the bodies in
the morgue, not realizing they were using the wrong surgery. Since I
couldn't _redo_ the surgery, this rendered all these bodies useless.
This was not out of maliciousness, they just didn't know better. There
are two autopsies in the surgery list, but only one is valid for the
experiment and doing the wrong one blocks _both surgeries_. Dissection
is completely useless outside of experiments. This same issue also
prevents additional autopsies on the same person, even if they had come
back to life and died again after you had done the initial autopsy.
Surely you would want to do more than one autopsy, right? That's two
separate deaths!

This resolves that by giving you a method of redoing any screwups on the
same corpse if necessary. It only matters if the experiment is available
anyway, so there isn't much reason to punish players unduly just because
they weren't aware science hadn't hit a button on their side (especially
since it isn't communicated to the coroner in any way to begin with). It
also removes a completely useless surgery and ties in the experiment to
what the coroner is already going to be doing. They can dissect their
corpses to their hearts content without worrying about retribution from
science for doing so.

In addition, someone repeatedly dying can continue to have autopsies
done on them over the course of the round. The surgery bonus only
applies once, so the only reason to do autopsies after the first is to
discover what might have killed someone. No reason this should block
further surgeries, just block surgeries when the person remains a
corpse.

## Changelog
:cl:
fix: You can do autopsies on people who were revived and died again
after they had already been dissected.
qol: Autopsies have become the surgery needed to complete the dissection
experiments. As a result, the dissection surgery has been removed as it
is now redundant.
qol: A coroner knows whether someone has been autopsied and recently
dissected (and thus hasn't been revived) by examining them.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[f3fc60ed65...](https://github.com/realforest2001/forest-cm13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Thursday 2023-08-17 23:52:35 by morrowwolf

Attachment nerfs and removals (#4122)

# About the pull request

This PR:

Removes the barrel charger from vendors

Removes all benefits other than wield delay mod from the angled grip

Adds wield delay to the extended barrel

# Explain why it's good for the game

Barrel charger is a straight damage increase and rather silly to work
around given how burst works bypassing real fire rate concerns. If you
know, you know. Horrible idea, I am amazed it's been around this long.

Angled grip had zero downside. Now it still has zero downside but isn't
also a ton of accuracy buffs on top of the god-tier lower wield delay.

Extended barrel had zero downside. Now it has a downside.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removed the barrel charger from vendors
balance: Removed all benefits other than wield delay mod from the angled
grip
balance: Added wield delay to extended barrel
/:cl:

---

