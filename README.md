## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-27](docs/good-messages/2022/2022-09-27.md)


2,202,022 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,202,022 were push events containing 3,293,409 commit messages that amount to 263,004,978 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[223e8bfd96...](https://github.com/tgstation/tgstation/commit/223e8bfd96a7762f0d23dd9b789fa90be1a572ec)
#### Tuesday 2022-09-27 00:06:15 by Time-Green

Fixes gravity pulse and transparent floor plane sharing a layer (#70124)

fixes gravity pulse and transparent floor plane sharing a layer

Broken by #69642 , sorry
I'll open up a seperate PR later today with a unit test to catch these cases
(my later today is in like 10 hours)

closes #70123 (weird fucking floors)

---
## [amling/rlife](https://github.com/amling/rlife)@[c8832583ae...](https://github.com/amling/rlife/commit/c8832583ae12749c445f6b9947613e4fac83affb)
#### Tuesday 2022-09-27 00:16:33 by Keith Amling

Rework this compilation env business.

It sucks because each new arg is now horrible, but we haven't had any
and the lifetime shit is making this pretty sad.

---
## [hexagon-geo-surv/linux-stable-rt](https://github.com/hexagon-geo-surv/linux-stable-rt)@[adee8f3082...](https://github.com/hexagon-geo-surv/linux-stable-rt/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Tuesday 2022-09-27 00:34:30 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [OpenVZ/vzkernel](https://github.com/OpenVZ/vzkernel)@[e5a59c8161...](https://github.com/OpenVZ/vzkernel/commit/e5a59c81612db0c7991bcdbd5113890af3334258)
#### Tuesday 2022-09-27 00:51:29 by Vladimir Davydov

mm: introduce transcendent file cache (tcache)

Transcendent file cache (tcache) is a simple driver for cleancache,
which stores reclaimed pages in memory unmodified. Its purpose it to
adopt pages evicted from a memory cgroup on local pressure, so that they
can be fetched back later without costly disk accesses. It works
similarly to shadow gangs from PCS6 except pages has to be copied on
eviction.

https://jira.sw.ru/browse/PSBM-31757

* Usage

 - Enable:
   # modprobe tcache # only if compiled as a module
   # echo Y > /sys/module/tcache/parameters/enabled

 - Disable:
   # echo N > /sys/module/tcache/parameters/enabled

 - Get number of pages cached:
   # cat /sys/module/tcache/parameters/nr_pages

* Implementation notes

 - Fetching/adding a page to tcache implies looking up a tcache pool
   (corresponds to a super block), tcache node in the pool (corresponds
   to an inode), and a page in the node. Pages of the same node are
   organized into a radix tree protected by a single spin lock,
   similarly to pages in an address_space. Nodes of the same pool are
   kept in several RB trees, each of which protected by its own spin
   lock. The number of RB trees is proportional to the number of CPUs,
   and nodes are distributed among the trees using a hash function. This
   is to minimize contention on the locks protecting the trees. Pools
   are kept in an IDR and looked up locklessly.

 - All tcache pages are linked in per NUMA node LRU lists and reclaimed
   on global pressure by a slab shrinker. Also, if we fail to allocate a
   new page for tcache, we will attempt to reclaim the oldest one
   immediately.

 - Once the tcache module is loaded, it is impossible to disable tcache
   completely due to cleancache limitations. "Disabling" it via the
   corresponding module parameter only forbids populating the cache with
   new pages. Lookups will proceed to tcache anyway.

 - Tcache pages are accounted as file pages.

* F.A.Q.

 - Does copying pages to and from tcache affect performance?

   Yes, it does. Fetching data from tcache advances roughly two times
   slower than from the page cache, because one has to copy data twice.
   Below are times of reading a 512M file from a memory cgroup:

   a) without limits:
      536870912 bytes (537 MB) copied, 0.481623 s, 1.1 GB/s
   b) with 100M limit and tcache enabled:
      536870912 bytes (537 MB) copied, 0.974815 s, 551 MB/s

   However, tcache exists not to allow containers whose working set does
   not fit in their RAM operate as fast as they would if there were no
   memory limits at all. Tcache exists to avoid costly disk operations
   whenever possible. For example, if there is a container which would
   normally thrash due to the memory limit and there is some unused
   memory on the host, it is better to allow the container to use the
   free memory to avoid thrashing, because otherwise it will generate
   disk pressure sensible by other containers.

 - Is there any memory overhead excluding the space used for storing
   data pages?

   Practically, no. All the information about pages is stored directly
   in struct page, and no additional handles are allocated per page.
   Per inode radix trees do consume some additional kernel memory per
   page, but its amount is negligible.

 - Does tcache generate memory pressure at the global level? If yes,
   does it affect containers?

   Yes, it generates global pressure and currently it does affect
   containers. This is similar to the issue we had had in PCS6 before
   shadow gangs and vmscan scheduling hacks were introduced, when there
   was the only LRU list for evicted pages (init_gang). We are planning
   to fix it by backporting low limits for memory cgroups. If a
   container is below its low limit, its memory will not be scanned on
   global pressure unless all containers are below their low limits
   (this is a kind of memory guarantee). We will set low limits for a
   container to be equal to an estimate of its working set size (this
   will be done by a user space daemon). Since tcache resides in the
   root memory cgroup, which does not have any memory guarantees (low
   limit equals 0), it will not press upon containers provided the
   system is properly configured.

 - Why cannot we use low limits instead of hard limits then?

   Low limits are unsafe by design. There is no guarantee that we will
   always be able to reclaim a cgroup back to its low limit. There are
   anonymous and kernel memory, which are sometimes really hard to
   reclaim. We could introduce a separate limit for them (anon+swap),
   but it will never get upstream (we tried).

 - Why is it better than what we have in PCS6?

   Primarily, because the idea of wiring sophisticated vmscan rules into
   the kernel, as we have done in PCS6 (vmscan scheduler) is dubious
   since it makes changing its behavior really painful. There are other
   points too:

   + The PCS6 memory management patch is really intrusive: it has
     sprouted its slimy tentacles all around the mm subsystem (rmap.c,
     memory.c, mlock.c, vmscan.c). We will hardly ever manage to push it
     upstream, so we will most likely have to carry it for good. This
     means each major rebase will turn into a torment. OTOH tcache code
     is isolated in a module and therefore can be easily ported back and
     forth.

   + Thanks to data copying, we can do funny things with the
     transcendent page cache in future, such as compression and
     deduplication. There were plans to implement compressed file cache
     upstream (zcache), but unfortunately it is still not there, and
     nobody seems to care about it. Nevertheless, sooner or later it
     will be introduced (may be, I'll facilitate this process), and we
     will be able to seamlessly switch to it from tcache. Tcache will be
     still useful for testing though.

 - In PCS6 there are per container shadow lists, while you have only the
   global LRU for all tcache pages. Is there any plans to introduce per
   super block or per memory cgroup LRUs?

   I am still unconvinced that we really need it, because it is not
   clear to me what policy we should apply per container on reclaim. It
   smells like one more heuristic, which I am desperately trying to
   avoid. Current design looks simple and sane: there are guarantees for
   containers provided by their limits, and they are competing fairly
   for the rest of the memory used for caches.

 - What about swap cache?

   There are plans to implement a similar driver for frontswap (tswap)
   or backport and use existing zswap. There may be problems with the
   latter though, because it currently does not support reclaim, and it
   will be tricky from the technical point of view to introduce it.

 - Any plans to push tcache upstream?

   No, because its use case looks too narrow to me to be included into
   the vanilla kernel. I am planning to concentrate on zcache instead.

Signed-off-by: Vladimir Davydov <vdavydov@parallels.com>

+++
mm/tcache: restore missing rcu_read_lock() in tcache_detach_page() #PSBM-120802

Looks like rcu_read_lock() was lost in "out:" path of tcache_detach_page()
when tcache was ported to VZ8. As a result, Syzkaller was able to hit
the following warning:

  WARNING: bad unlock balance detected!
  4.18.0-193.6.3.vz8.4.7.syz+debug #1 Tainted: G        W        ---------r-  -
  -------------------------------------
  vcmmd/926 is trying to release lock (rcu_read_lock) at:
  [<ffffffff848ed2e0>] tcache_detach_page+0x530/0x750
  but there are no more locks to release!

  other info that might help us debug this:
  2 locks held by vcmmd/926:
   #0: ffff888036331f30 (&mm->mmap_sem){++++}, at: __do_page_fault+0x157/0x550
   #1: ffff8880567295f8 (&ei->i_mmap_sem){++++}, at: ext4_filemap_fault+0x82/0xc0 [ext4]

  stack backtrace:
  CPU: 0 PID: 926 Comm: vcmmd ve: /
               Tainted: G        W        ---------r-  - 4.18.0-193.6.3.vz8.4.7.syz+debug #1 4.7
  Hardware name: Virtuozzo KVM, BIOS 1.11.0-2.vz7.2 04/01/2014
  Call Trace:
   dump_stack+0xd2/0x148
   print_unlock_imbalance_bug.cold.40+0xc8/0xd4
   lock_release+0x5e3/0x1360
   tcache_detach_page+0x559/0x750
   tcache_cleancache_get_page+0xe9/0x780
   __cleancache_get_page+0x212/0x320
   ext4_mpage_readpages+0x165d/0x1b90 [ext4]
   ext4_readpages+0xd6/0x110 [ext4]
   read_pages+0xff/0x5b0
   __do_page_cache_readahead+0x3fc/0x5b0
   filemap_fault+0x912/0x1b80
   ext4_filemap_fault+0x8a/0xc0 [ext4]
   __do_fault+0x110/0x410
   do_fault+0x622/0x1010
   __handle_mm_fault+0x980/0x1120
   handle_mm_fault+0x17f/0x610
   __do_page_fault+0x25d/0x550
   do_page_fault+0x38/0x290
   do_async_page_fault+0x5b/0xe0
   async_page_fault+0x1e/0x30

Let us restore rcu_read_lock().

https://jira.sw.ru/browse/PSBM-120802
Fix in vz7: 152239c6c3b2 ("mm/tcache: fix rcu_read_lock()/rcu_read_unlock()
imbalance")

Signed-off-by: Evgenii Shatokhin <eshatokhin@virtuozzo.com>
Reviewed-by: Andrey Ryabinin <aryabinin@virtuozzo.com>

vz9 rebase notes:
 * free_unref_page() new arg (page order) has been added - assumed it's
   always 0

(cherry picked from vz8 commit e0868a90331d9ab990f3d4ca802d068fecaa9457)
Signed-off-by: Konstantin Khorenko <khorenko@virtuozzo.com>
Feature: mm: transcendent file cache (tcache)

---
## [iGheek/vercel-next.js](https://github.com/iGheek/vercel-next.js)@[1bbd264216...](https://github.com/iGheek/vercel-next.js/commit/1bbd2642164098ceb9cebfb36deba9aed7e8a53b)
#### Tuesday 2022-09-27 01:10:53 by abdennor

Add additional fix in hydration error document (#40675)

I had the same issue, so the fix that worked for me was pulled from this
thread https://stackoverflow.com/a/71870995

I have been experiencing the same problem lately with NextJS and i am
not sure if my observations are applicable to other libraries. I had
been wrapping my components with an improper tag that is, NextJS is not
comfortable having a p tag wrapping your divs, sections etc so it will
yell "Hydration failed because the initial UI does not match what was
rendered on the server". So I solved this problem by examining how my
elements were wrapping each other. With material UI you would need to be
cautious for example if you use a Typography component as a wrapper, the
default value of the component prop is "p" so you will experience the
error if you don't change the component value to something semantic. So
in my own opinion based on my personal experience the problem is caused
by improper arrangement of html elements and to solve the problem in the
context of NextJS one will have to reevaluate how they are arranging
their html element

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->


## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm lint`
- [ ] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [KangarooDevv/KangarooDevv](https://github.com/KangarooDevv/KangarooDevv)@[231af48672...](https://github.com/KangarooDevv/KangarooDevv/commit/231af486723d9bfb0259cb69fb60fe122ff18886)
#### Tuesday 2022-09-27 01:14:47 by KangarooDevv

Delete proxy.py

Reverse Proxy Python Script Using IPTables.
Don't let people get IPS that run your services!
now you're asking why python?
well i love .py honestly, but also,
you can easily set a sleep, or a timeout, and then
make this script run everytime for the amount of time you set
if you would like to add it, here is the code!
os.system('timeout 1200 python proxy.py')
so after every 20 minutes it will re proxy itself again :) enjoy!

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[79b4a74a6e...](https://github.com/Zergspower/Skyrat-tg/commit/79b4a74a6e6f13128779f88cb784ecb1e5989524)
#### Tuesday 2022-09-27 01:46:02 by RimiNosha

[MODULAR] Fixes That Stupid Language Reset Bug That's Been Here Since Newprefs (#15802)

* I hate coders
This includes myself.

* Web edit~

* I give up, this is the best I got

* Make species take their alternate language instead of uncommon! Make language selection reflect foreigner, if selected!

* Remove code that assumed old foreigner add proc was called

* whyaremidroundspawnshandleddifferentlythanroundstartswhatthefuck

* Apply suggestion!

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

* Address last review at long last

* Apply suggestions!

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [GesuBackups/tgstation](https://github.com/GesuBackups/tgstation)@[d45e244401...](https://github.com/GesuBackups/tgstation/commit/d45e244401425d34edc38e3dd2f3c2bbdbcec7ce)
#### Tuesday 2022-09-27 01:46:42 by san7890

Crab-17 No Longer Breaks Economy If You Swipe Too Fast (#70094)

Hey there,

Remember swiping credit cards, before everything was chipped? You know how sometimes if you went too slow, the transaction might fail, the cashier had to plonk in some digits on their machine, and you had to go again? That kinda sucked.

If you're too young to get that reference, just imagine the card swiping task in AMONG US. Doesn't that minigame suck? You know exactly what that is. Same principle.

Anyways, that's pretty much what was going on here. The reason why SS.Economy would break so god damn hard if you swiped an ID before the machine's "boot up" slowflake animation was complete is probably due to the line where it starts fast processing. I added an early return to check for if the animation was complete by leveraging a var we already set at the end of the process, because I am lazy.

There's probably a few other ways you can tackle this issue, but this feels right to me in a thematic sense. I'm willing to change it if needed though.

---
## [Ebin-Halcyon/Skyrat-tg](https://github.com/Ebin-Halcyon/Skyrat-tg)@[e66aaaa0c2...](https://github.com/Ebin-Halcyon/Skyrat-tg/commit/e66aaaa0c257fb021a3aa5d6e3f8910fa599edad)
#### Tuesday 2022-09-27 02:01:48 by SkyratBot

[MIRROR] Add speech modifier to zombie tongue [MDB IGNORE] (#16417)

* Add speech modifier to zombie tongue (#69899)

About The Pull Request

A zombie rotten tongue has a complex language modifier.
The language modifier works by:

    All occurrences of characters "eiou" (case-insensitive) are replaced with "r".
    All characters other than "zhrgbmna .!?-" (case-insensitive) are stripped.
    Multiple spaces are replaced with a single.
    Lower-case "r" at the end of words replaced with "rh".
    An "a" or "A" by itself will be replaced with "hra".
    The first character is capitalised.

Some interesting dialogue examples:

    Bab, am gaa habbah abah zah namrh ah Bh!rh!b?
    Bob, are you happy about the death of Philip?

    Zah bang bang man ganna harm mah zambah?
    Will the Zombie Hunter attack me?

    Mah zambah nah harm brazzarz.
    I do not hurt brothers.

    Mah zambah ganna gangbang harmanz zammarrar.
    I will kill humans tomorrow.

    Mah zambah am nah habbah, an mah zambah gab, -Graaaagh!-
    I am not happy, and I say "Graaaagh!"

The language idea was taken from a zombie game back in 2005 called Urban Dead. It's no longer developed and I made all the code myself while following the given language rule structures.

Zombie Speech Translator
Zombie Language Examples
Zombie Dictionary
Why It's Good For The Game
Abracadabra - The Steve Miller Band

    Ah raab zha brahnz ahn zarh hagh, (I love the brains in your head)
    Ah ganna barg abgrah gangbang, (I'm gonna eat them when you're dead)
    Az rahnah zarh ranz ahn hahg ahahz, (Now as you run and hide away)
    Zarh harh mah zambah az hah zahz: (You hear my zombie as he says:)
    Abra-abra-gababra, (Abra-abra-cadabra)
    Ah ganna rahg arg ahn grab zarh! (I'm gonna reach out and grab ya!)
    Abra-abra-gababra, (Abra-abra-cadabra)
    Ah ganna rahg arg ahn grab zarh! (I'm gonna reach out and grab ya!)

Changelog

cl
add: Rotten zombie tongue has a new speech modifier that converts spoken language into zombie sentences. If the person speaking is a high-functioning zombie this is bypassed.
/cl

* Add speech modifier to zombie tongue

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[9c61d5321e...](https://github.com/ammarfaizi2/linux-fork/commit/9c61d5321e94a4d0678b5eb0515afc590bdb9740)
#### Tuesday 2022-09-27 03:06:14 by Peter Xu

mm/x86: use SWP_TYPE_BITS in 3-level swap macros

Patch series "mm: Remember a/d bits for migration entries", v4.


Problem
=======

When migrating a page, right now we always mark the migrated page as old &
clean.

However that could lead to at least two problems:

  (1) We lost the real hot/cold information while we could have persisted.
      That information shouldn't change even if the backing page is changed
      after the migration,

  (2) There can be always extra overhead on the immediate next access to
      any migrated page, because hardware MMU needs cycles to set the young
      bit again for reads, and dirty bits for write, as long as the
      hardware MMU supports these bits.

Many of the recent upstream works showed that (2) is not something trivial
and actually very measurable.  In my test case, reading 1G chunk of memory
- jumping in page size intervals - could take 99ms just because of the
extra setting on the young bit on a generic x86_64 system, comparing to
4ms if young set.

This issue is originally reported by Andrea Arcangeli.

Solution
========

To solve this problem, this patchset tries to remember the young/dirty
bits in the migration entries and carry them over when recovering the
ptes.

We have the chance to do so because in many systems the swap offset is not
really fully used.  Migration entries use swp offset to store PFN only,
while the PFN is normally not as large as swp offset and normally smaller.
It means we do have some free bits in swp offset that we can use to store
things like A/D bits, and that's how this series tried to approach this
problem.

max_swapfile_size() is used here to detect per-arch offset length in swp
entries.  We'll automatically remember the A/D bits when we find that we
have enough swp offset field to keep both the PFN and the extra bits.

Since max_swapfile_size() can be slow, the last two patches cache the
results for it and also swap_migration_ad_supported as a whole.

Known Issues / TODOs
====================

We still haven't taught madvise() to recognize the new A/D bits in
migration entries, namely MADV_COLD/MADV_FREE.  E.g.  when MADV_COLD upon
a migration entry.  It's not clear yet on whether we should clear the A
bit, or we should just drop the entry directly.

We didn't teach idle page tracking on the new migration entries, because
it'll need larger rework on the tree on rmap pgtable walk.  However it
should make it already better because before this patchset page will be
old page after migration, so the series will fix potential false negative
of idle page tracking when pages were migrated before observing.

The other thing is migration A/D bits will not start to working for
private device swap entries.  The code is there for completeness but since
private device swap entries do not yet have fields to store A/D bits, even
if we'll persistent A/D across present pte switching to migration entry,
we'll lose it again when the migration entry converted to private device
swap entry.

Tests
=====

After the patchset applied, the immediate read access test [1] of above 1G
chunk after migration can shrink from 99ms to 4ms.  The test is done by
moving 1G pages from node 0->1->0 then read it in page size jumps.  The
test is with Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz.

Similar effect can also be measured when writting the memory the 1st time
after migration.

After applying the patchset, both initial immediate read/write after page
migrated will perform similarly like before migration happened.

Patch Layout
============

Patch 1-2:  Cleanups from either previous versions or on swapops.h macros.

Patch 3-4:  Prepare for the introduction of migration A/D bits

Patch 5:    The core patch to remember young/dirty bit in swap offsets.

Patch 6-7:  Cache relevant fields to make migration_entry_supports_ad() fast.

[1] https://github.com/xzpeter/clibs/blob/master/misc/swap-young.c


This patch (of 7):

Replace all the magic "5" with the macro.

Link: https://lkml.kernel.org/r/20220811161331.37055-1-peterx@redhat.com
Link: https://lkml.kernel.org/r/20220811161331.37055-2-peterx@redhat.com
Signed-off-by: Peter Xu <peterx@redhat.com>
Reviewed-by: David Hildenbrand <david@redhat.com>
Reviewed-by: Huang Ying <ying.huang@intel.com>
Cc: Hugh Dickins <hughd@google.com>
Cc: "Kirill A . Shutemov" <kirill@shutemov.name>
Cc: Alistair Popple <apopple@nvidia.com>
Cc: Andrea Arcangeli <aarcange@redhat.com>
Cc: Minchan Kim <minchan@kernel.org>
Cc: Andi Kleen <andi.kleen@intel.com>
Cc: Nadav Amit <nadav.amit@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Dave Hansen <dave.hansen@intel.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Luziferium/randomizer-csgo](https://github.com/Luziferium/randomizer-csgo)@[bde6aed504...](https://github.com/Luziferium/randomizer-csgo/commit/bde6aed504e8c394a32cdc027e96ccac2e2b01de)
#### Tuesday 2022-09-27 03:29:36 by Luziferium

It's fucking 05:30 am and I have to work today, fml

and oh yeah: Deleted Config model stuff for now, Created EventClusterDao, EventRepository is now EventRegistry, Saving, Loading and Deleting clusters now work over the model, abstracted the BuilderView from model stuff what now handles the BuilderViewModel, Moved much stuff to the right place, I like the class WhateverThisFuckerIs, And most important: you're gay

---
## [saboooor/guilded-discord-bridge](https://github.com/saboooor/guilded-discord-bridge)@[6dea32abaa...](https://github.com/saboooor/guilded-discord-bridge/commit/6dea32abaa60ad687da5eaf521967b00cb719e38)
#### Tuesday 2022-09-27 03:46:04 by saboooor

global variables so the next commit can be done without annoying ass shit

---
## [GoldenretriverYT/ConsoleUI](https://github.com/GoldenretriverYT/ConsoleUI)@[0d12fc517b...](https://github.com/GoldenretriverYT/ConsoleUI/commit/0d12fc517b8fb15b94e980a506a04e0b3cc845f8)
#### Tuesday 2022-09-27 03:46:13 by GoldenretriverYT

No, this is not a joke. This is the fix for it not working

For some god damn reason, Windows does not allow ANSI Escape Sequences until you run the "cls" command.

This makes absolutely no sense. It must be the cls command, it can not be Console.Clear

Absolute Windows Moment

---
## [AmethystTheSergal/coyote-bayou](https://github.com/AmethystTheSergal/coyote-bayou)@[8a27b0fe9d...](https://github.com/AmethystTheSergal/coyote-bayou/commit/8a27b0fe9d5f5f30d2db06246970d76c74cfe00d)
#### Tuesday 2022-09-27 05:06:46 by bearrrrrrrrr

i'm KILLING you. i am KILLING y ou. i don't care about anything else i don't give a SHIT about anything else. my programming is just, 'GET THAT FUCKING GUY'

---
## [Offroaders123/nbtify](https://github.com/Offroaders123/nbtify)@[00cc5dc24d...](https://github.com/Offroaders123/nbtify/commit/00cc5dc24df2da4c3a891902bb7b868120aa2263)
#### Tuesday 2022-09-27 06:36:45 by Offroaders123

Rebranding: NBTify!

The official name has now arrived, NBTify! (like stringify) Couldn't quite decide on one so easily, and this seemed to be the best option. I wanted a name that is easy to remember, and simple to type. I was going to do something like WebNBT or Web-NBT (So it lines up with APIs like WebRTC, WebGPU, or Web Audio API), but I didn't like that it didn't start with NBT, and that there's already a "webNBT" project. While that one isn't JS-based, I didn't want to step on their toes for any naming confusions. So, went with making my own!

While shortlived, trying out GitHub Packages was really nice in the previous release, as you have everything tied into GitHub. It's as feature complete as npm for use in Node, but it turns out there isn't (yet) a way to load it from a CDN. I'm a little bit bummed about that, but I think it's for the best. So much of the industry lives off of npm, so I think it's time that I jump aboard too. So much more cool stuff I can do!

(Reflection time!)
Crazy to go through yet another leap in learning. So happy with how the library it turning out! It has given me so many more things to learn. TypeScript has been absolutely wonderful. Now that I'm at this stage, maybe I could look into making a browser NBT editor make with React!

Here's to learning!
*cheers*

Brandon :)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[cee07f804c...](https://github.com/tgstation/tgstation/commit/cee07f804cc1df6d9cb0ff783ad4504458cf2c8b)
#### Tuesday 2022-09-27 07:09:51 by LemonInTheDark

Airlock open delay audit (#69905)


About The Pull Request

A: Mineral doors no longer take 6 SECONDS to open if you bump anything beforehand. Holy shit why would you do this.
B: Airlocks no longer require you to have not bumped anything in a second, lowered to 0.3 seconds. This is safe because I've moved shock immunity to its own logic. This should make opening doors feel less horrible
Why It's Good For The Game

Feels better.
Changelog

cl
balance: Airlocks will open on bump in series much faster now. As a tradeoff, you're immune to shocks from them for a second after you last got shocked by one.
fix: Mineral doors will no longer take 6 WHOLE SECONDS to open if you've bumped something else recently
/cl

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[23bfdec8f4...](https://github.com/tgstation/tgstation/commit/23bfdec8f43046f7b54906509e38ed1ad91f5096)
#### Tuesday 2022-09-27 07:11:07 by LemonInTheDark

Multiz Rework: Human Suffering Edition (Contains PLANE CUBE) (#69115)


About The Pull Request

I've reworked multiz. This was done because our current implementation of multiz flattens planes down into just the openspace plane. This breaks any effects we attach to plane masters (including lighting), but it also totally kills the SIDE_MAP map format, which we NEED for wallening (A major 3/4ths resprite of all wall and wall adjacent things, making them more then one tile high. Without sidemap we would be unable to display things both in from of and behind objects on map. Stupid.)

This required MASSIVE changes. Both to all uses of the plane var for reasons I'll discuss later, and to a ton of different systems that interact with rendering.

I'll do my best to keep this compact, but there's only so much I can do. Sorry brother.
Core idea

OK: first thing.
vis_contents as it works now squishes the planes of everything inside it down into the plane of the vis_loc.
This is bad. But how to do better?

It's trivially easy to make copies of our existing plane masters but offset, and relay them to the bottom of the plane above. Not a problem. The issue is how to get the actual atoms on the map to "land" on them properly.

We could use FLOAT_PLANE to offset planes based off how they're being seen, in theory this would allow us to create lens for how objects are viewed.
But that's not a stable thing to do, because properly "landing" a plane on a desired plane master would require taking into account every bit of how it's being seen, would inherently break this effect.

Ok so we need to manually edit planes based off "z layer" (IE: what layer of a z stack are you on).

That's the key conceit of this pr. Implementing the plane cube, and ensuring planes are always offset properly.
Everything else is just gravy.
About the Plane Cube

Each plane master (except ones that opt out) is copied down by some constant value equal to the max absolute change between the first and the last plane.
We do this based off the max z stack size detected by SSmapping. This is also where updates come from, and where all our updating logic will live.

As mentioned, plane masters can choose to opt out of being mirrored down. In this case, anything that interacts with them assuming that they'll be offset will instead just get back the valid plane value. This works for render targets too, since I had to work them into the system as well.

Plane masters can also be temporarily hidden from the client's screen. This is done as an attempt at optimization, and applies to anything used in niche cases, or planes only used if there's a z layer below you.
About Plane Master Groups

BYOND supports having different "maps" on screen at once (IE: groups of items/turfs/etc)
Plane masters cannot cover 2 maps at once, since their location is determined by their screen_loc.
So we need to maintain a mirror of each plane for every map we have open.

This was quite messy, so I've refactored it (and maps too) to be a bit more modular.

Rather then storing a list of plane masters, we store a list of plane master group datums.
Each datum is in charge of the plane masters for its particular map, both creating them, and managing them.

Like I mentioned, I also refactored map views. Adding a new mapview is now as simple as newing a /atom/movable/screen/map_view, calling generate_view with the appropriate map id, setting things you want to display in its vis_contents, and then calling display_to on it, passing in the mob to show ourselves to.

Much better then the hardcoded pattern we used to use. So much duplicated code man.

Oh and plane master controllers, that system we have that allows for applying filters to sets of plane masters? I've made it use lookups on plane master groups now, rather then hanging references to all impacted planes. This makes logic easier, and prevents the need to manage references and update the controllers.

image

In addition, I've added a debug ui for plane masters.
It allows you to view all of your own plane masters and short descriptions of what they do, alongside tools for editing them and their relays.

It ALSO supports editing someone elses plane masters, AND it supports (in a very fragile and incomplete manner) viewing literally through someone else's eyes, including their plane masters. This is very useful, because it means you can debug "hey my X is yorked" issues yourself, on live.

In order to accomplish this I have needed to add setters for an ungodly amount of visual impacting vars. Sight flags, eye, see_invis, see_in_dark, etc.

It also comes with an info dump about the ui, and plane masters/relays in general.

Sort of on that note. I've documented everything I know that's niche/useful about our visual effects and rendering system. My hope is this will serve to bring people up to speed on what can be done more quickly, alongside making my sin here less horrible.
See https://github.com/LemonInTheDark/tgstation/blob/multiz-hell/.github/guides/VISUALS.md.
"Landing" planes

Ok so I've explained the backend, but how do we actually land planes properly?
Most of the time this is really simple. When a plane var is set, we need to provide some spokesperson for the appearance's z level. We can use this to derive their z layer, and thus what offset to use.

This is just a lot of gruntwork, but it's occasionally more complex.
Sometimes we need to cache a list of z layer -> effect, and then use that.
Also a LOT of updating on z move. So much z move shit.

Oh. and in order to make byond darkness work properly, I needed to add SEE_BLACKNESS to all sight flags.
This draws darkness to plane 0, which means I'm able to relay it around and draw it on different z layers as is possible. fun darkness ripple effects incoming someday

I also need to update mob overlays on move.
I do this by realiizing their appearances, mutating their plane, and then readding the overlay in the correct order.

The cost of this is currently 3N. I'm convinced this could be improved, but I've not got to it yet.
It can also occasionally cause overlays to corrupt. This is fixed by laying a protective ward of overlays.Copy in the sand, but that spell makes the compiler confused, so I'll have to bully lummy about fixing it at some point.
Behavior changes

We've had to give up on the already broken gateway "see through" effect. Won't work without managing gateway plane masters or something stupid. Not worth it.
So instead we display the other side as a ui element. It's worse, but not that bad.

Because vis_contents no longer flattens planes (most of the time), some uses of it now have interesting behavior.
The main thing that comes to mind is alert popups that display mobs. They can impact the lighting plane.
I don't really care, but it should be fixable, I think, given elbow grease.

Ah and I've cleaned up layers and plane defines to make them a bit easier to read/reason about, at least I think.
Why It's Good For The Game
<visual candy>

Fixes #65800
Fixes #68461
Changelog

cl
refactor: Refactored... well a lot really. Map views, anything to do with planes, multiz, a shit ton of rendering stuff. Basically if you see anything off visually report it
admin: VV a mob, and hit View/Edit Planes in the dropdown to steal their view, and modify it as you like. You can do the same to yourself using the Edit/Debug Planes verb
/cl

---
## [peff/git](https://github.com/peff/git)@[9a5bb60202...](https://github.com/peff/git/commit/9a5bb602029039ee12409894599a34484d612e2e)
#### Tuesday 2022-09-27 07:47:17 by Jeff King

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
## [peff/git](https://github.com/peff/git)@[593f7fd9d7...](https://github.com/peff/git/commit/593f7fd9d7fad6567d6e852c7c47ddfe227acec3)
#### Tuesday 2022-09-27 07:47:42 by Jeff King

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
## [maikilangiolo/CEV-Eris](https://github.com/maikilangiolo/CEV-Eris)@[29430253ff...](https://github.com/maikilangiolo/CEV-Eris/commit/29430253ffa7c3394df438c922c3827bfbf79f51)
#### Tuesday 2022-09-27 08:44:05 by maikilangiolo

Levergun re do (#7587)

* update timer (#7501)

* FUCK YOU FUCK YOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

* Update code/modules/projectiles/guns/projectile/battle_rifle/levergun.dm

Co-authored-by: hyperioo <64754494+hyperioo@users.noreply.github.com>

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[b3b85cae9b...](https://github.com/odoo-dev/odoo/commit/b3b85cae9b1951b82053d7c6b55e559cbc48307d)
#### Tuesday 2022-09-27 09:24:23 by Xavier Morel

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
## [kianenigma/seeding](https://github.com/kianenigma/seeding)@[0d558e2d6a...](https://github.com/kianenigma/seeding/commit/0d558e2d6a2de3edddfaab8e53af5ae1cd67d3ef)
#### Tuesday 2022-09-27 10:08:15 by Kian Paimani

Membership Request

# Membership Request 

Hi, I am Kian Paimani, known as @kianenigma. I have been working on Polkadot/Kusama through Parity since February 2019 and I can categorize my main contributions to Polkadot's ecosystem as follows: 

1. Maintaining and developing the staking sub-system.
2. General FRAME development, especially testing and quality assurance. 
3. Polkadot-native side-projects. 
4. Education 

> My first contribution to Polkadot is also indeed related to staking: https://github.com/paritytech/substrate/pull/1915

### Staking system

I joke as the Polkadot staking to be both my blessing and my curse over the years. I started working on it since the first days that I joined this ecosystem and the work [is ongoing ever since](https://github.com/orgs/paritytech/projects/33/views/9). In the past, I focused on making sure that the staking system is secure and to some extent scalable. More recently, I coordinated the (imminent) launch of Nomination Pools. Nowadays I also put an extra effort on making sure that this sub-system of Polkadot is *sustainable*, through code refactor and educating other core developers. 

Lastly, I have been the main author of the [Polkadot staking newsletter](https://gist.github.com/kianenigma/aa835946455b9a3f167821b9d05ba376), which is my main attempt at making the entire complexity and development of this part of the protocol transparent to the end-users.

I expect myself to contribute *directly* to the staking system for at least another ~12, if not more, and afterwards having the role of an advisor. 

Some notable contributions: 

- https://github.com/paritytech/substrate/pull/4517
- https://github.com/paritytech/substrate/pull/7910
- https://github.com/paritytech/substrate/issues/6242
- https://github.com/paritytech/substrate/pull/9415
- https://github.com/paritytech/polkadot/pull/3141
- https://github.com/paritytech/substrate/pull/11212
- https://github.com/paritytech/substrate/pull/12129

### FRAME 

Historically, I have contributed a variety of domains in FRAME, namely: 

- Early version of the weight system https://github.com/paritytech/substrate/pull/3816 https://github.com/paritytech/substrate/pull/3157
- Early version of the transaction fee system
- Primitive arithmetic types https://github.com/paritytech/substrate/pull/3456
- Council election pallet https://github.com/paritytech/substrate/pull/3364

Many of which were, admittedly, a PoC at most, if not considered "poor". I am happy that nowadays many of the above have been refactored and are being maintained by new domain experts. 

These days, I put most of my FRAME focus on testing and quality assurance. Through my work in the staking system, I have had to deal with the high sensitivity and liveness requirement of protocol development first hand (I believe I had to do among the [very first storage migrations](https://github.com/paritytech/substrate/pull/3948) in Kusama) and consequently I felt the need to make better testing facilities, all of which have been formulated in https://forum.polkadot.network/t/testing-complex-frame-pallets-discussion-tools/356. Some relevant PRs:

- https://github.com/paritytech/substrate/pull/8038
- https://github.com/paritytech/substrate/pull/9788
- https://github.com/paritytech/substrate/pull/10174

Regardless of wearing the staking hat, I plan to remain a direct contributor to FRAME, namely because I consider it to be an important requirements of successfully delivering more features to Polkadot's ecosystem. 

### Polkadot-Native Side Projects

I have started multiple small, mostly non-RUST projects in the polkadot ecosystem that I am very happy about, and I plan to continue doing so. I have not yet found the time to make a "polished product" out of any of these, but I hope that I can help foster our community such that someday a team will do so. I consider my role, for the time being, to *put ideas out there* through these side projects. 

- https://github.com/substrate-portfolio/polkadot-portfolio/
- https://github.com/kianenigma/polkadot-basic-notification/
- https://github.com/paritytech/polkadot-scripts/
- https://github.com/paritytech/substrate-debug-kit/

### Education 

Lastly, aside from having had a number of educational talks over the years (all of which [are listed](https://hello.kianenigma.nl/talks/) in my personal website), I am a big enthusiast of the newly formed Polkadot Blockchain Academy. I have [been an instructor](https://singular.app/collectibles/statemine/16/2) in the first cohort, and continue to contribute for as long and as much as I can, whilst still attending to the former 3 duties. 

---

With all of that being said and done, I consider myself at the beginning of the path to Dan 4, but happy to start at a lower one as well.

---
## [lawfuyang/dx12test](https://github.com/lawfuyang/dx12test)@[1486f34c95...](https://github.com/lawfuyang/dx12test/commit/1486f34c95b011ee259e6d2458204442e177b8fe)
#### Tuesday 2022-09-27 11:01:07 by lawfuyang

More WIP Shadows
- removed AMD_ShadowFX.h. not needed
- added fullzprepass renderer as the shadow mask pass requires a depth buffer
- added SunShadowMaskRenderer, which calls the appropriate AMD ShadowFX PS
- doesnt really work yet. pretty sure its because of my inverse Z depth buffers and SamplerComparisonState being LEqual
- moved all AMD define macros to json, so that its define in the DXC level

Fixed a whole bunch of matrix row/column major nonsense
- specify -Zpr in DXC so that the matrices are packed in row-major order, to math DirectXMath on app side
- no more "Gfx" matrices variants in View
- Apparently, DirectXMath applies matrix multiplications from RIGHT TO LEFT. what the fuck? so I fixed all of that shit. No more pre-transposed nonsense.

Add ability to bind proper formats in descriptor views from Typeless formats
- i.e, DXGI_FORMAT_R16_TYPELESS to DXGI_FORMAT_D16_UNORM or DXGI_FORMAT_R16_UNORM
- required if we need to use a Depth buffer as both DSV & SRV
- we then need to define the gfxresource format as typeless

Remove serialization & initialization of Tangent vectors
- Almost removed it from VertexFormat

Fixed VS_FullScreenTriangle outputting clockwise triangle. Our renderer runs Counterclockwise as frontfacing

Next Up: legit get the Shadow mask generation working. please.

---
## [CatsPsychologist/hys_academy](https://github.com/CatsPsychologist/hys_academy)@[0eef590396...](https://github.com/CatsPsychologist/hys_academy/commit/0eef5903965b2156f48d80a6a1a01a1875a96d7f)
#### Tuesday 2022-09-27 11:10:28 by CatsPsychologist

ls_3 change files structure

sorry for such a stupid decision, hope it won't make you troubles :)

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[d34fa4c642...](https://github.com/lizardqueenlexi/orbstation/commit/d34fa4c642839215df5ba985d098a04e4d555b5b)
#### Tuesday 2022-09-27 16:32:14 by LemonInTheDark

Macro optimizes SSmapping saving 50%  (#69632)

* 'optimizes' space transitions by like 0.06 seconds, makes them easier to read tho, so that's an upside

* ''''optimizes'''' parsed map loading

I'm honestly not sure how big a difference this makes, looked like small
percentage points if anything
It's a bit more internally concistent at least, which is nice. Also I
understand the system now.

I'd like to think it helped but I think this is kinda a "do you think
it's easier to read" sort of situation. if it did help it was by the
skin of its teeth

* Saves 0.6 seconds off loading meta and lavaland's map files

This is just a lot of micro stuff.
1: Bound checks don't need to be inside for loops, we can instead bound the iteration counts
2: TGM and DMM are parsed differently. in dmm a grid_set is one z level,
   in tgm it's one collumn. Realizing this allows you to skip copytexts and
   other such silly in the tgm implemenentation, saving a good bit of time
3: Min/max bounds do not need to be checked inside for loops, and can
   instead be handled outside of them, because we know the order of x
   and y iteration. This saves 0.2 seconds

I may or may not have made the code harder to read, if so let me know
and I'll check it over.

* Micro ops key caching significantly. Fixes macros bug

inserting \ into a dmm with no valid target would just less then loop
the string. Dumb

Anyway, optimizations. I save a LOT of time by not needing to call
find_next_delimiter_position for every entry and var set. (like maybe 0.5
seconds, not totally sure)
I save this by using splittext, which is significantly faster. this
would cause parsing issues if you could embed \n into dmms, but you
can't, so I'm safe.

Lemme see uh, lots of little things, stuff that's suboptimal or could be
done cheaper. Some "hey you and I both know a \" is 2 chars long sort of
stuff

I removed trim_text because the quote trimming was never actually used,
and the space trimming was slower then using the code in trim. I also
micro'd trim to save a bit of time. this saves another maybe 0.5.

Few other things, I think that's the main of it. Gives me the fuzzy
feelings

* Saves 50% of build_coordinate's time

Micro optimizing go brrrrr
I made turf_blacklist an assoc list rather then just a normal one, so
lookups are O(log n) instead of O(n). Also it's faster for the base case
of loading mostly space.

Instead of toggling the map loader right before and right after New()
calls, we toggle at the start of mapload, and disable then reenable if
we check tick. This saves like 0.3 seconds

Rather then tracking an area cache ourselves, and needing to pass it
around, we use a locally static list to reference the global list of
area -> type. This is much faster, if slightly fragile.

Rather then checking for a null turf at every line, we do it at the
start of the proc and not after. Faster this way, tho it can in theory
drop area vvs.

Avoids calling world.preloader_setup unless we actually have a unique
set of attributes. We use another static list to make this comparison
cheap. This saves another 0.3

Rather then checking for area paths in the turf logic, or vis versa, we
assume we are creating the type implied by the index we're reading off.
So only the last type entry will be loaded like a turf, etc.
This is slightly unsafe but saves a good bit of time, and will properly
error on fucked maps.

Also, rather then using a datum to hold preloader vars, we use 2 global
variables. This is faster.

This marks the end of my optimizations for direct maploading. I've
reduced the cost of loading a map by more then 50% now. Get owned.

* Adds a define for maploading tick check

* makes shuttles load again, removes some of the hard limits I had on the reader for profiling

* Macro ops cave generation

Cave generation was insanely more expensive then it had any right to be.
Maybe 0.5 seconds was saved off not doing a range(12) for EVERY SPAWNED
MOB.
0.14 was saved off using expanded weighted lists (A new idea of mine)
This is useful because I can take a weighted list, and condense it into
weight * path count. This is more memory heavy, and costs more to
create, but is so much faster then the proc.

I also added a naive implementation of gcd to make this a bit less bad.
It's not great, but it'll do for this usecase.

Oh and I changed some ChangeTurfs into New()s. I'm still not entirely
sure what the core difference between the two is, but it seems to work
fine.
I believe it's safe because the turf below us hasn't init'd yet, there's
nothing to take from them. It's like 3 seconds faster too so I'll be sad
when it turns out I'm being dumb

* Micros river spawning

This uses the same sort of concepts as the last change, mostly New being
preferable to ChangeTurf at this level of code.
This bit isn't nearly as detailed as the last few, I honestly got a bit
tired. It's still like 0.4 seconds saved tho

* Micros ruin loading

Turns out it saves time if you don't check area type for every tile on a
ruin. Not a whole ton faster, like 0.03, but faster.

Saves even more time (0.1) to not iterate all your ruin's turfs 3 times
to clear away lavaland mobs, when you're IN SPACE who wrote this.

Oh it also saves time to only pull your turf list once, rather then 3
times

---
## [riteshm321/android_frameworks_base](https://github.com/riteshm321/android_frameworks_base)@[1cf11621d7...](https://github.com/riteshm321/android_frameworks_base/commit/1cf11621d7e08c2439e5ffb1b3dda0baa91ba507)
#### Tuesday 2022-09-27 17:12:54 by Joey Huab

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
## [mikeandmore/fvwm3](https://github.com/mikeandmore/fvwm3)@[7aad184baa...](https://github.com/mikeandmore/fvwm3/commit/7aad184baacd20497f702d539aa701f64cf5dc32)
#### Tuesday 2022-09-27 18:40:31 by Thomas Adam

FvwmEvent: comply better with the GPL

Although fvwm has been under the GPL for some time, certain part of fvwm
(especially around modules) which have had different contriutions from
different authors over the years, have meant that certain copyright
messages have remained.

These copyright messages which are subject to modification as long as
said message remains intact, goes against the spirit of the GPL.
Indeed, in speaking with the authors in question, such practises were
common before the GPL was established as a means of licensing/modifiying
software.

The following authors were contacted and their responses indicate
they're happy for FvwmEvent's copyright notices to change:

* Mark Scott (2020-11-23):

	Thomas,

	Wow, it’s great to hear from someone keeping that old code alive!  I
	honestly had forgotten about ever even writing that code. 😊  You are
	sure welcome to do whatever you like with that code base.

	I hereby release all copyright claims to any FvwmSound or FvwmAudio
	related code. Feel free to re-license it under GPL or any other license
	you feel appropriate.

* Mark Boyns (2020-11-23):

	Hi Thomas, you found the correct Mark. You have my permission to update
	the license as needed. Good luck with fvwm and your open source
	projects.

This change therefore removes the explicit copyright notices regarding
the behaviour of the copyright notices, but still firmly records their
contributions to FvwmSound/FvwmEvent.

The man page has been updated to reflect this as well.

---
## [grafana/tanka](https://github.com/grafana/tanka)@[75733cb7d5...](https://github.com/grafana/tanka/commit/75733cb7d5878755735905174cab348ad517073b)
#### Tuesday 2022-09-27 18:48:17 by Julien Duchesne

Fix `getSnippetHash` not considering all files
Made a stupid mistake in the previous PR: https://github.com/grafana/tanka/pull/759

This fixes it and adds another benchmark test to ensure it doesn't happen again.
I also removed the Github Actions benchmark test, as it's not really useful, anytime we change the tests, we'll get erroneous results which will be annoying.
Instead, I added the benchmark tests to the Drone run, we can compare whenever we want.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[75dfa159f0...](https://github.com/TaleStation/TaleStation/commit/75dfa159f0ba53b65bd4f256547842ec424173bb)
#### Tuesday 2022-09-27 19:19:30 by TaleStationBot

[MIRROR] [MDB IGNORE] Micros the lighting subsystem (Saves a second of init) (#2605)

* Micros the lighting subsystem (Saves a second of init) (#69838)


About The Pull Request

Micros lighting objects, and their creation

We save a good bit of time by not walking space turfs adjacent to new objects.
We also save some time with micros in the actual underlay update logic.

I swear dude we spend like 0.8 seconds of init applying the underlay. I want threaded maptick already

Micros lighting sources, and corner creation

A: Corners were being passed just A turf, and then expected to generatecorners based on that. This is pointless.
It is better to instead pass in the coords of the bottom left turf, and then build in a circle. This saves like 0.3 seconds

B: We use so many damn datum vars in corner application that we just do not need to.
This resolves that, since it pissed me off. It's pointless. Lets cache em instead

There's some misc datum var caching going on here too. Lemme see...
Oh and a bit of shortcutting for a for loop, since it was a tad expensive on its own.

Also I removed the turfs list, because it does fucking nothing. Why is this still here.

All my little optimizations save about 1 second of init I think
Not great, but not bad, and plus actual lighting work is faster now too
Why It's Good For The Game

Speed

* Micros the lighting subsystem (Saves a second of init)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [edsantiago/libpod](https://github.com/edsantiago/libpod)@[9ece902e07...](https://github.com/edsantiago/libpod/commit/9ece902e07de35324e0adc7f01483781ffe83bf8)
#### Tuesday 2022-09-27 19:31:14 by Ed Santiago

Proof of concept: nightly dependency treadmill

As discussed in f2f: this is the cleanest, simplest mechanism
I can think of to auto-test the Big Three dependencies: simply
run go mod edit immediately after git checkout, then run the
entire CI test suite.

If this approach works, we can set up a new CIRRUS_CRON=treadmill
job. I'm expecting it not to work, because Murphy, but want to
see what the unexpected gotchas are.

This differs significantly from the buildah treadmill, in that
buildah is almost impossible to re-vendor without manual intervention.
(In practice, so are these, but let's dream of a world in which
this will run and pass every night). (I want a pony too).

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [bonziworldrevived/bonziworldrevived.github.io](https://github.com/bonziworldrevived/bonziworldrevived.github.io)@[63b2b6b945...](https://github.com/bonziworldrevived/bonziworldrevived.github.io/commit/63b2b6b94559f37e716336021afed3bc1de9dbf4)
#### Tuesday 2022-09-27 19:43:27 by CrazyMediumScout

shiiiiiiiiiiiiiiiiiiiiiiiiiiiiit!​ shit!​ you​ little​ bitch!​ how​ dare​ you​ eat​ shit!​ and​ yes​ this​ is​ the​ fucking​ living​ room​ in​ our​ fucking​ house!​ go​ to​ bed​ now!!

---
## [thebkbuffalo/eow_betting_react](https://github.com/thebkbuffalo/eow_betting_react)@[6dfb3cd683...](https://github.com/thebkbuffalo/eow_betting_react/commit/6dfb3cd683e17f8c3e341ef79dd255dc5bb68069)
#### Tuesday 2022-09-27 20:17:28 by Evan Berg

slowly but surely killing stupid ass react console warnings...fucking react

---
## [Brawaru/knossos](https://github.com/Brawaru/knossos)@[c19659220c...](https://github.com/Brawaru/knossos/commit/c19659220c66e323b647c46036c87681f502b486)
#### Tuesday 2022-09-27 20:26:42 by Sasha Sorokin

Add v-i18n:wrap directive

v-i18n:wrap directive is a directive that only has effect within the
<i18n-formatted> element. It takes an element as a skeleton and allows
to use so-called 'wrappers' in the translations.

Wrappers are extremely useful if translation needs to contain links or
buttons, but it does not make to split text from those to separate
strings.

For example, let's say we have the following HTML:

  Your project was rejected, please check out the <a href="/rules">rules</a>.

Without wrapper elements we would have to resort to the following:

In our translations file,

  {
    "rejection-message": "Your project was rejected, please check out the {rulesLink}.",
    "rejection-message.rules-link": "rules"
  }

In our Vue file,

  <i18n-formatted message-id="rejection-message">
    <a href="/rules" v-i18n:value="'rules-link'">{{ $t('rejection-message.rules-link') }}</a>
  </i18n-formatted>

For translators, this is not very plausable experience because they'd
have to guess what that 'rulesLink' variable actually contains, it's
good that we use good message IDs, but nevertheless, it's confusing
experience.

It also introduces a surface for mistake, translator may not pay close
attention to the message IDs and translate both strings independently.
As English speakers we tend to forget that other languages have more
advanced casing systems, where noun or verb may change depending on what
surrounds it, so in some languages, translating both strings can lead to
mistake.

To demonstrate, let me give you an example from Discord:

Say we have the following strings in original English text:

  {
    "hello-cta": "Say ‘{hello}’ to the {helloTarget}",
    "hello-cta.target": "cat"
  }

Which we can use as such:

  $t('hello-cta', { helloTarget: $t('hello-cta.target') })

But what happens if Ukrainian translator translates `hello-cta.target`
independently of `hello-cta` string. They translate it as such:

  {
    "hello-cta": "Сказати «привіт» {helloTarget}",
    "hello-cta.target": "кіт"
  }

And using code above, the result we will get from these translations:

  'Сказати «привіт» кіт'

Which is incorrect, in this case 'кіт' is supposed be in dative case,
which would change it to 'коту'.

Keeping that in mind, let's look how things would change if we were to
use wrapping syntax:

  {
    "hello-cta": "Сказати «привіт» <target>коту</target>"
  }

This looks like HTML, and if you think about it, it kinda is, but not
quite, it's merely wrapper, like BB-codes, and those do not accept any
arguments, to not complicate things.

In the code we would use `hello-cta` string as such:

  $t('hello-cta', { helloTarget: (parts) => `${parts.map(_ => String(_)).join('')}` }`)

Keep in mind, that in this example we don't do anything fancy yet, you
can see that our wrapper doesn't do anything apart from taking some
parts and later converting them to strings. If we don't use any objects
in our context object, then it will never be not array of strings, but
otherwise it'd contain these objects too in places of variables.

So what do we get when evaluating code above? Well, of corse:

  'Сказати «привіт» коту'

What v-i18n:wrap allows us to do is to create skeleton node, which will
be copied every time the wrapper used, and which children will be
replaced with aforementioned parts.

Let's look at the first example, but using wrappers now:

Here's our changed translation file:

  {
    "rejection-message": "Your project was rejected, please check out the <rules-link>rules</rules-link>."
  }

And here's how we'd change our template:

  <i18n-formatted message-id="rejection-message">
    <a href="/rules" v-i18n:wrap="'rules-link'" />
  </i18n-formatted>

Notice that we self-close our link element, that's because we know that
anything will be replaced anyway, so there is no sense to provide any
children.

And what happens when this string actually gets rendered?

  Your project was rejected, please check out the <a href="/roles">rules</a>.

Exactly what we'd expect.

So there we go, this is the new directive for you, hope this was
insightful and useful to understand the importance and usage of this
feature.

---
## [Brawaru/knossos](https://github.com/Brawaru/knossos)@[4774c893b5...](https://github.com/Brawaru/knossos/commit/4774c893b5f7fb4b4886942f226b4c9946902548)
#### Tuesday 2022-09-27 20:26:42 by Sasha Sorokin

Initial work on the i18n support

Absolutely not ready, just a draft for progress and maybe quick review
whether it's good idea or not.

This commit will be squashed with more meaningful message as the work
goes.

For now things are like this:

- It uses @formatjs/intl which uses ICU Message Format for messages,
  it's the same underlying framework than used in React. However,
  their Vue module is only for Vue 3 and it also not dynamic (means
  you can only initialise it with a single language which is weird),
  so I had to re-do all work by myself.

- Reason not to use vue-i18n: it's weird formatting for translations.
  I agree it's a more mature module, but as translator myself I under
  no circumstance want to translate things like {n} apple | {n} apples.
  ICU Message Format is already an industry standard so there's no good
  reason to re-invent the wooden wheel when people already have alloy
  ones.

- There is no automatic extraction, sadly.

- There is no automatic locale packing. I have no clue how to implement
  Nuxt modules to do this magic, but it's probably very possible, should
  look at https://i18n.nuxtjs.org/ for inspiration, they use some weird
  templates and generate plugins. Oh my oh my.

---
## [ThakaSartu/quxube](https://github.com/ThakaSartu/quxube)@[57b429e132...](https://github.com/ThakaSartu/quxube/commit/57b429e1327eb274bff9b79a6191883c8d617a04)
#### Tuesday 2022-09-27 20:48:35 by ThakaSartu



<h2>I need to get my daughter out of a molesters hands (・о・) </h2>
<h2 class="neonText"> Its been 757 days since I have seen our daughter CORAL_IRIS_KELLY. </h2> 
Her mother mother Erika Renee Kelly was kidnapped on Feb 2,2020. A local Atlanta Matt Field bragged about it on Facebook stating "I_SOLD_HER. I found her near Venice beach California and my tattooist Kennie_Davis of Jolly_Roger_Tattoo in _Stockbridge#Georgia was not too far from the scene. Erika and I were not estranged when she disappeared as 
[ESSENCE_MAGAZiNE_STATED](https://www.essence.com/news/erika-kelly-missing-atlanta-georgia/) we were coparenting. I was laid off from my IT job at [Ionic Security](https://www.linkedin.com/company/ionic-security) after my work was repeatedly sabotaged by my manager. I opened a case with Fulton_County_Family_Services two months before our eviction from our East_Atlanta_Home_at_631_Moreland_Ave_in_Atlanta_Georgia they failed to process us after repeated visits and calls. I took odd jobs and even scored a mural gig with 
[Mercedes_BenZ_Stadium](https://mercedesbenzstadium.com/) for the 
[Atlanta_Falcons](https://www.atlantafalcons.com/). They paid me $1500 for a 40ft graffiti mural on red canvas for former athlete Deion_Sanders. I was severely underpaid but it covered the rent for one more month. I moved in with Constancia and her daughter Akeeva, got Coral in school at 
[Chapel Hill Elementary](https://www.chapelhilles.dekalb.k12.ga.us/) and worked hard to get a new 9-5. Constancia did not like me or Coral living with her and Akeeva so they undercut me with accusations of erratic behavior and started thier own dfacs case accusing me of schizophrenia. I had no income and was repeatedly denied foodstamps and welfare by a woman named DANIELLE_MASHONGA_and_her_colleageMANESSA_WARNER... Coral would ask

<h2> Where_is_mommy?!?</h2>

I told her that Matt stole and raped her and she needs our help, so we have to keep looking. Constancia and Akeeva constantly defended Matt. He is a known pedophile and child and adult rapist in the Atlanta art community. I did not know this. We shopped at the same record store and he often offered me work. I loath rapist. I loath pedophilia. Once I learned of his ways I distanced myself. So Erikas_mother_and_sisters_DEFENDING_HIM, struck me as bizarre. "Its_just_a_white_boy_jokeHe_didnt_sell_her". 
[DFACS](https://dfcs.georgia.gov/) stalked me on Facebook and indirectly accused me of CHILD_MOLESTATION for a video where we were playing with a wand style muscle massager, it was innocent. They 
[forcibly removed Coral](https://www.youtube.com/watch?v=AmYdIZhahrQ) saying that I was saying 
["inappropriate things"](https://www.youtube.com/watch?v=9sCE3HhjSbY) and violating her by saying that her mom had been raped and kidnapped. I learned that telling Coral the ugly truth was the best way to keep a solid trust filled relationship with her. In the DFACS meeting, puzzled I told Mashonga the truth, I cant find work, my reputation was being sabotaged and I could not even get a job at Kroger the local grocery store. I told Mashonga I needed money for food, Constancia would not feed niether me or Coral. I asked Mashonga in 
[This_Family_Meeting](https://www.youtube.com/watch?v=Q8NXhT6_Tx8) if she cared about me dying on the street and she shook her head, no. I was never interviewed with Coral at all, I never got a psych eval until I got to a UCLA_Recoup_Center_in_PalmDale_California. In early October I saw Coral, in Pasadena, California, with a grown man wearing fishnet stockings... Shes 9. I was shot with a poison dart one day later, my skateboard stolen and my foot began to swell larger that a shoe could fit... I was rushed to the emergency room and UCLA Cut_my_foot_to_the_bone_to_drain_the_infection... I cant run as well any more and am now handicapped 

<iframe width="100%" height="315" src="https://www.youtube.com/embed/Q8NXhT6_Tx8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="100%" height="400" src="https://www.youtube.com/embed/9sCE3HhjSbY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="100%" height="400" src="https://www.youtube.com/embed/AmYdIZhahrQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<h2>Her_Former_Life_With_Me</h2>

<iframe width="100%" height="315" src="https://www.youtube.com/embed/-oZuyrU764s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="100%" height="315" src="https://www.youtube.com/embed/CsM4jNSAm4A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe width="100%" height="315" src="https://www.youtube.com/embed/ydGxlS8l7Y0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<span class="neonText"> Dear Danielle_MAshonga, DFACS, DPSS
	WHERE_IS_CORAL?!?!?</span>	

<img src="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/img-0281-1513267146.jpeg?crop=1xw:1xh;center,top&resize=768:*">	
<code>THANK_YOU_COSMOPOLiTAN for this article that highlights this device as one used in sports medicine</code>
Sex educator and artist Betty Dodson had been teaching her famous Bodysex workshops in New York City since the late 60s. These women-only workshops focused on teaching women how to masturbate. Dodson was a pioneer and advocate for the use of vibrators, ever since her lover in the late 1960s introduced her to an electric vibrator originally used for scalp massages. While Dodson <a href="http://www.dodsonandross.com/blogs/betty-dodson/2010/06/having-sex-machines-return-electric-vibrator" href="http://www.dodsonandross.com/blogs/betty-dodson/2010/06/having-sex-machines-return-electric-vibrator" target="_blank" data-vars-ga-outbound-link="http://www.dodsonandross.com/blogs/betty-dodson/2010/06/having-sex-machines-return-electric-vibrator">originally</a> While Dodson is widely credited with popularizing the Magic Wand, she received no compensation for her endorsement of the toy. Dodson added, "it's really shitty of [Hitachi] to not acknowledge my efforts and give me a percentage." || WRiTTEN_BY :: CARiNA_HSiEH 
	<a href="https://twitter.com/carinahsieh"> Carina's TWiTTER</a>
	<a href="https://www.linkedin.com/in/carina-hsieh-a8802458"> CARiNA_HSiEH's LiNKEDiN</a>
	<h3>THAKAS_THOUGHTS</h3>
	<a href="https://www.linkedin.com/in/danielle-mushonga-msw-26262132">DANiELLE_MUSHONGA's LiNKEDiN_PROFiLE (KiDNAPPiNG_SPECiALiST) </a>

---
## [ianandersonlol/FarmAlphafold](https://github.com/ianandersonlol/FarmAlphafold)@[3362e3e035...](https://github.com/ianandersonlol/FarmAlphafold/commit/3362e3e035ffac451c1dfbc81e6bc2208cc3380b)
#### Tuesday 2022-09-27 20:55:25 by Ian Anderson

Fixed singularity issue and formatting.

I really hate myself that I always decide that aesthetics are important. In reality there should be no prints no nothing, just do your job. But noooooo I want the user to know something is going on.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[1810b85553...](https://github.com/tgstation/tgstation/commit/1810b855536f05891593b1379e455164f45fab3a)
#### Tuesday 2022-09-27 21:24:06 by tralezab

Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

About The Pull Request

Heretics can no longer be converted to a cult, as they follow their own Forgotten Gods.
Instead, Nar'Sie will reward the cult for managing to sacrifice one, with the bastard sword.
The bloody bastard sword has been cleaned up codewise and all that. Because it is a free reward instead of a (removed) progression mechanic of cult, it swings just a bit slower during the spin and doesn't have a jaunt. It's still a !fun! swinging sword of hilarity and death.
BLOODY BASTARD https://www.youtube.com/watch?v=ukznXQ3MgN0
Fantasy weapons can now roll "soul-stealing" weapons. They, on killing something, capture its soul inside the item.

    Add fail conditions that instantly end a spin2win, ala how 

    Mimes can now hold a baguette like a sword by right clicking it #69592 works

Why It's Good For The Game

Bloody bastard sword was fun, it made no sense that heretics were valid converts when they're already worshipping a DIFFERENT evil god granting them powers. Should be in a good spot as a nice little antag to antag special interaction. I fucking love antag to antag special interactions, we should have more of 'em

Fantasy affixes are always a neat thing to throw a new component into
Changelog

cl
add: Heretics can no longer be converted to cult. But sacrificing them is very valuable to Nar'Sie, and she will grant special weapons if you manage to do so.
add: Fantasy affixes can also include soul-stealing items!
/cl

---
## [philipl/mpv](https://github.com/philipl/mpv)@[93baa5c299...](https://github.com/philipl/mpv/commit/93baa5c29961b134166315b163acc98db410ff66)
#### Tuesday 2022-09-27 21:47:26 by Philip Langdale

f_hwtransfer: get rid of the shit list

A few years ago, wm4 got sufficiently annoyed with how vaapi image
format support was being discovered that he flipped the table and
introduced the shit list (which just included vaapi) to hard-code the
set of supported formats.

While that might have been necessary at the time, I haven't been able
to find a situation where the true list of supported formats was unsafe
to use. We filter down the list based on what the vo reports - and the
vo is already doing a thorough testing of formats, and if a format
makes it through that gauntlet, it does actually work.

Interestingly, as far as I can tell, the hwdec_vaapi probing code was
already good enough at the time (also written by wm4), so perhaps the
key difference here is that the driver side of things has improved.

I dug into this because of the support for the 422/444 high bit depth
vaapi formats I added to ffmpeg. These are obviously not in the hard
coded list today, but they work fine.

Finally, although it's positioned as a vaapi thing, it's really just
Intel specific, as the AMD vaapi driver has never exposed support for
anything except the formats used by the decoder/encoder profiles.

---
## [yepgames/VRZOMBIEGAME](https://github.com/yepgames/VRZOMBIEGAME)@[085c77c295...](https://github.com/yepgames/VRZOMBIEGAME/commit/085c77c2958d750562da116df81b97ef27281ac6)
#### Tuesday 2022-09-27 22:06:10 by ashpimm

everythings fucked worked all night and things just keep not working or conflicting with other shit

FUCK

---
## [teeps-co/laminas-inputfilter](https://github.com/teeps-co/laminas-inputfilter)@[5d8986654c...](https://github.com/teeps-co/laminas-inputfilter/commit/5d8986654c8b455192cd180985634f9eacf56501)
#### Tuesday 2022-09-27 22:56:12 by Michał Bundyra

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
## [melanieplageman/postgres](https://github.com/melanieplageman/postgres)@[7fed801135...](https://github.com/melanieplageman/postgres/commit/7fed801135bae14d63b11ee4a10f6083767046d8)
#### Tuesday 2022-09-27 23:40:38 by Tom Lane

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

