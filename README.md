## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-13](docs/good-messages/2022/2022-10-13.md)


2,192,415 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,192,415 were push events containing 3,334,594 commit messages that amount to 258,545,717 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [repinger/leenux](https://github.com/repinger/leenux)@[2535fbde89...](https://github.com/repinger/leenux/commit/2535fbde890f14c78b750139fcf87d1143850626)
#### Thursday 2022-10-13 00:42:06 by Johannes Weiner

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[36ba5c656b...](https://github.com/treckstar/yolo-octo-hipster/commit/36ba5c656bcb98ea5a799db0de8d7862695125b8)
#### Thursday 2022-10-13 03:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [SlenderFox/OpenGL-Engine](https://github.com/SlenderFox/OpenGL-Engine)@[d780a56112...](https://github.com/SlenderFox/OpenGL-Engine/commit/d780a56112f22d16c9a9f2cd98ce125d2729757c)
#### Thursday 2022-10-13 03:34:17 by SlenderFox

Utterly fucking cursed model loading

Using a friended struct to loaded the model then calling it either from the member function or struct passing an Entity pointer ref.

---
## [neebe000/kernel_xiaomi_mt6785](https://github.com/neebe000/kernel_xiaomi_mt6785)@[d0c40d8954...](https://github.com/neebe000/kernel_xiaomi_mt6785/commit/d0c40d895491ef827992e694f0527d385a05b83c)
#### Thursday 2022-10-13 03:38:17 by Peter Zijlstra

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
Signed-off-by: neebe000 <neebexd@gmail.com>

---
## [mexisme/nixos-hardware](https://github.com/mexisme/nixos-hardware)@[540c80a85a...](https://github.com/mexisme/nixos-hardware/commit/540c80a85a0fe032e928726a9033e1515207fbdc)
#### Thursday 2022-10-13 03:41:33 by mexisme

Initial port from github.com/linux-surface/linux-surface, vendorising the patches and firmware binaries.

Add MS Surface Kernel patches from github.com/linux-surface/linux-surface

Add MS Surface Firmware from github.com/linux-surface/linux-surface

Add MS Surface Hardware config from github.com/linux-surface/linux-surface

Tie-together the Microsoft Surface .nix files

Set to use explicit version of Linux (5.4.7)

- Add the config for Linux 5.4.7

Add kernel 5.4.11

Add kernel 5.4.13

Remove unsupported patches

Revert to kernel 5.4.7 for now

- Problems initialising touchscreen & pen

Add kernel 5.4.15 and 5.4.16

Build kernel 5.4.16, instead

Add kernel 5.4.22

Update the patches for kernel 5.4

Placeholder for Linux kernel 5.5

Copy the IPTS kernel patch from the 5.5 dir to the 5.4 dir.

Conversation on https://gitter.im/linux-surface/community suggested this would
reenable IPTS on 5.4:

-----
@matrixbot Feb 29 15:33
hpfr Blaž Hrastnik (Gitter): thanks for the mention. mexisme (Gitter) finally, someone who actually knows Nix and isn't just a config nerd writing proper NixOS Surface configs! I am stuck on 4.19 at the moment because IPTS is now a proper reverse-engineered kernel driver (https://github.com/linux-surface/intel-precise-touch) instead of just a blob package, and I haven't had time to look at how to package that for Nix. If you're on 5.5, are you just not using IPTS? Would love to help out on packaging that for NixOS
hpfr also, development conversations seem to happen more at #linux-surface on freenode, which you can connect to with matrix via https://matrix.to/#/!OXIGGPCpnzaNVeGtCA:matrix.org if you don't like IRC clients

@matrixbot Feb 29 15:39
hpfr Also, I'm not using jakeday's patches, I'm using the more recent ones from the linux-surface/linux-surface repo, but yeah, for 4.19, so they're a bit different from the 5.x patchsets. afaik 4.19 is still supported because it's the last LTS release that supports the "official" IPTS blob before Linux made changes that required reverse engineering a driver that didn't use GuC submission (I'm just quoting here, I have no idea what that is haha)

@matrixbot Feb 29 19:27
Blaž > now a proper reverse-engineered kernel driver
Should be similar to before, we just offer it as a patch
Blaž https://github.com/linux-surface/linux-surface/blob/master/patches/5.5/0007-ipts.patch
Blaž Anyway I'm keeping an eye out on your NixOS builds since I'm thinking about giving it a try

@matrixbot Feb 29 19:32
Blaž Currently running Arch but using nix as a way to manage development environments for various projects

@matrixbot Mar 01 10:41
hpfr Blaž: well shoot is that patch all that’s necessary for building in-tree? It does all the things the linux-surface/intel-precise-touch repo does?

Dorian Stoll @StollD Mar 01 12:56
Yes
Just adds all the files from the repo to drivers/input/touchscreen and adds the necessary glue to drivers/input/touchscreen/{Makefile, Kconfig}

@matrixbot Mar 02 09:13
hpfr Dorian Stoll (Gitter): oof. Could’ve been on 5.4+ all this time!

Move kernnel *.nix packages under their respective kernel dirs

Use lib.mkDefault

Update to kernel 5.4.24

Update to kernel 5.5.8

Typo

Drivers are modules by default

Revert to 5.4.24 until can fix the config failures

---
## [NetHack/NetHack](https://github.com/NetHack/NetHack)@[b02e018225...](https://github.com/NetHack/NetHack/commit/b02e01822564e5bee3c31082e978419edea6a37c)
#### Thursday 2022-10-13 04:37:17 by Michael Meyer

Remove explicit 'none' opt from autounlock handler

The autounlock handler included an explicit 'none' option, a choice that
gave it a different UX from similar existing compound option handlers
(e.g. paranoid_confirm or pickup_types), which set 'none' simply by
deselecting all options.  It didn't make the menu any easier to use (at
least in my experience), since in order to go from some combination of
options to 'none', you'd have to deselect everything anyway (which on
its own was enough to set 'none', so there was no reason to explicitly
select it after doing so).

Make the autounlock handler work like other compound option handlers,
such that deselecting all options is the way to set 'none', and there is
no explicit 'none' option included in the list.

---
## [SpiffyJUNIOR/chicagorp-settings-gui](https://github.com/SpiffyJUNIOR/chicagorp-settings-gui)@[b7836699c9...](https://github.com/SpiffyJUNIOR/chicagorp-settings-gui/commit/b7836699c9a1f16e48b7c558a636b52990293286)
#### Thursday 2022-10-13 06:22:51 by SpiffyJUNIOR

more shit

this is probably insanely fucked up but i'll fix it later

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[dc451840bd...](https://github.com/newstools/2022-new-york-post/commit/dc451840bdd0d44b1b68373e4340b444e513b25f)
#### Thursday 2022-10-13 06:32:01 by Billy Einkamerer

Created Text For URL [nypost.com/2022/10/12/i-found-out-my-boyfriend-was-cheating-on-me-when-i-got-this-infection/]

---
## [bleubulblight/hwaseongBusCol](https://github.com/bleubulblight/hwaseongBusCol)@[603ec3025d...](https://github.com/bleubulblight/hwaseongBusCol/commit/603ec3025da7e20795d550b3d99943998aca8448)
#### Thursday 2022-10-13 06:37:09 by shimhy97

Merge branch 'shy' of https://github.com/bleubulblight/hwaseongBusCol into shy
Fuck you I need this merge

---
## [Zazou4code/MySQL-database-project](https://github.com/Zazou4code/MySQL-database-project)@[02a101f28d...](https://github.com/Zazou4code/MySQL-database-project/commit/02a101f28df94ca1ebf5e0262ba6cad5fed38dd7)
#### Thursday 2022-10-13 06:49:34 by Zazou4code

Update README.md

Based in Chicago, Illinois, Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day.

Little Lemon is owned by two Italian brothers, Mario and Adrian, who moved to the United States to pursue their shared dream of owning a restaurant. To craft the menu, Mario relies on family recipes and his experience as a chef in Italy. Adrian does all the marketing for the restaurant and led the effort to expand the menu beyond classic Italian to incorporate additional cuisines from the Mediterranean region.

This activity has two main objectives:
1. Provide a recap of all topics introduced in this course.

2. Provide experience with developing core database queries.

Task Instructions

Please attempt the following tasks.


Task 1: Filter data using the WHERE clause and logical operators.

Create a SQL statement to print all records from the Bookings table for the following bookings dates using the BETWEEN operator: 2021-11-11, 2021-11-12 and 2021-11-13. 

Task 2: Create a JOIN query.

Create a JOIN SQL statement on the Customers and Bookings tables. The statement must print the customers full names and related bookings IDs from the date 2021-11-11.


Task 3: Create a GROUP BY query.

Create a SQL statement to print the bookings dates from Bookings table. The statement must show the total number of bookings placed on each of the printed dates using the GROUP BY BookingDate. 



Task 4: Create a REPLACE statement.

Create a SQL REPLACE statement that updates the cost of the Kabsa course from $17.00 to $20.00.


Task 5: Create constraints

Create a new table called "DeliveryAddress" in the Little Lemon database with the following columns and constraints:

ID: INT PRIMARY KEY

Address: VARCHAR(255) NOT NULL

Type: NOT NULL DEFAULT "Private"

CustomerID: INT NOT NULL FOREIGN KEY referencing CustomerID in the Customers table


Task 6: Alter table structure

Create a SQL statement that adds a new column called 'Ingredients' to the Courses table.

Ingredients: VARCHAR(255)


Task 7: Create a subquery

Create a SQL statement with a subquery that prints the full names of all customers who made bookings in the restaurant on the following date: 2021-11-11.


Task 8: Create a virtual table

Create the "BookingsView" virtual table to print all bookings IDs, bookings dates and the number of guests for bookings made in the restaurant before 2021-11-13 and where number of guests is larger than 3.

Select all data from the BookingsView virtual table. 


Task 9: Create a stored procedure

Create a stored procedure called 'GetBookingsData'. The procedure must contain one date parameter called "InputDate". This parameter retrieves all data from the Bookings table based on the user input of the date.

After executing the query, call the "GetBookingsData" with '2021-11-13' as the input date passed to the stored procedure to show all bookings made on that date.



Task 10: Use the String function

Create a SQL SELECT query using appropriate MySQL string function to list "Booking Details" including booking ID, booking date and number of guests. The data must be listed in the same format as the following example:

ID: 10, 

Date: 2021-11-10, 

Number of guests: 5

---
## [haproxytech/quic-dev](https://github.com/haproxytech/quic-dev)@[d114f4a68f...](https://github.com/haproxytech/quic-dev/commit/d114f4a68fa771d4dd1dc62430eb9e16a38c9fab)
#### Thursday 2022-10-13 08:12:51 by Willy Tarreau

MEDIUM: checks: spread the checks load over random threads

The CPU usage pattern was found to be high (5%) on a machine with
48 threads and only 100 servers checked every second That was
supposed to be only 100 connections per second, which should be very
cheap. It was figured that due to the check tasks unbinding from any
thread when going back to sleep, they're queued into the shared queue.

Not only this requires to manipulate the global queue lock, but in
addition it means that all threads have to check the global queue
before going to sleep (hence take a lock again) to figure how long
to sleep, and that they would all sleep only for the shortest amount
of time to the next check, one would pick it and all other ones would
go down to sleep waiting for the next check.

That's perfectly visible in time-to-first-byte measurements. A quick
test consisting in retrieving the stats page in CSV over a 48-thread
process checking 200 servers every 2 seconds shows the following tail:

  percentile   ttfb(ms)
  99.98        2.43
  99.985       5.72
  99.99       32.96
  99.995     82.176
  99.996     82.944
  99.9965    83.328
  99.997      83.84
  99.9975    84.288
  99.998      85.12
  99.9985    86.592
  99.999         88
  99.9995    89.728
  99.9999   100.352

One solution could consist in forcefully binding checks to threads at
boot time, but that's annoying, will cause trouble for dynamic servers
and may cause some skew in the load depending on some server patterns.

Instead here we take a different approach. A check remains bound to its
thread for as long as possible, but upon every wakeup, the thread's load
is compared with another random thread's load. If it's found that that
other thread's load is less than half of the current one's, the task is
bounced to that thread. In order to prevent that new thread from doing
the same, we set a flag "CHK_ST_SLEEPING" that indicates that it just
woke up and we're bouncing the task only on this condition.

Tests have shown that the initial load was very unfair before, with a few
checks threads having a load of 15-20 and the vast majority having zero.
With this modification, after two "inter" delays, the load is either zero
or one everywhere when checks start. The same test shows a CPU usage that
significantly drops, between 0.5 and 1%. The same latency tail measurement
is much better, roughly 10 times smaller:

  percentile   ttfb(ms)
  99.98        1.647
  99.985       1.773
  99.99        4.912
  99.995        8.76
  99.996        8.88
  99.9965      8.944
  99.997       9.016
  99.9975      9.104
  99.998       9.224
  99.9985      9.416
  99.999         9.8
  99.9995      10.04
  99.9999     10.432

In fact one difference here is that many threads work while in the past
they were waking up and going down to sleep after having perturbated the
shared lock. Thus it is anticipated that this will scale way smoother
than before. Under strace it's clearly visible that all threads are
sleeping for the time it takes to relaunch a check, there's no more
thundering herd wakeups.

However it is also possible that in some rare cases such as very short
check intervals smaller than a scheduler's timeslice (such as 4ms),
some users might have benefited from the work being concentrated on
less threads and would instead observe a small increase of apparent
CPU usage due to more total threads waking up even if that's for less
work each and less total work. That's visible with 200 servers at 4ms
where show activity shows that a few threads were overloaded and others
doing nothing. It's not a problem, though as in practice checks are not
supposed to eat much CPU and to wake up fast enough to represent a
significant load anyway, and the main issue they could have been
causing (aside the global lock) is an increase last-percentile latency.

---
## [dnelson-1901/freebsd-ports](https://github.com/dnelson-1901/freebsd-ports)@[2729cb84b7...](https://github.com/dnelson-1901/freebsd-ports/commit/2729cb84b7af5d19933d8609d6a1a69ba119d521)
#### Thursday 2022-10-13 09:02:05 by Piotr Kubaj

emulators/mgba: update to 0.10.0

Features:
 - Preliminary Lua scripting support
 - Presets for Game Boy palettes
 - Add Super Game Boy palettes for original Game Boy games
 - Tool for converting scanned pictures of e-Reader cards to raw dotcode data
 - Options for muting when inactive, minimized, or for different players in multiplayer
 - Cheat code support in homebrew ports
 - Acclerometer and gyro support for controllers on PC
 - Support for combo "Super Game Boy Color" SGB + GBC ROM hacks
 - Improved support for HuC-3 mapper, including RTC
 - Support for 64 kiB SRAM saves used in some bootlegs
 - Discord Rich Presence now supports time elapsed
 - Additional scaling shaders
 - Support for GameShark Advance SP (.gsv) save file importing
 - Support for multiple saves per game using .sa2, .sa3, etc.
 - Support for GBX format Game Boy ROMs
 - New unlicensed GB mappers: NT (newer type), Sachen (MMC1, MMC2)
Emulation fixes:
 - ARM7: Fix unsigned multiply timing
 - GB: Copy logo from ROM if not running the BIOS intro (fixes mgba.io/i/2378)
 - GB: Fix HALT breaking M-cycle alignment (fixes mgba.io/i/250)
 - GB Audio: Fix channel 1/2 reseting edge cases (fixes mgba.io/i/1925)
 - GB Audio: Properly apply per-model audio differences
 - GB Audio: Revamp channel rendering
 - GB Audio: Fix APU re-enable timing glitch
 - GB I/O: Fix writing to WAVE RAM behavior (fixes mgba.io/i/1334)
 - GB MBC: Fix edge case with Pocket Cam register accesses (fixes mgba.io/i/2557)
 - GB Memory: Add cursory cartridge open bus emulation (fixes mgba.io/i/2032)
 - GB Serialize: Fix loading MBC1 states that affect bank 0 (fixes mgba.io/i/2402)
 - GB SIO: Fix bidirectional transfer starting (fixes mgba.io/i/2290)
 - GB Video: Draw SGB border pieces that overlap GB graphics (fixes mgba.io/i/1339)
 - GBA: Improve timing when not booting from BIOS
 - GBA: Fix expected entry point for multiboot ELFs (fixes mgba.io/i/2450)
 - GBA: Fix booting multiboot ROMs with no JOY entrypoint
 - GBA: Fix 1 MiB ROM mirroring to only mirror 4 times
 - GBA Audio: Adjust PSG sampling rate with SOUNDBIAS
 - GBA Audio: Sample FIFOs at SOUNDBIAS-set frequency
 - GBA BIOS: Work around IRQ handling hiccup in Mario & Luigi (fixes mgba.io/i/1059)
 - GBA BIOS: Initial HLE timing estimation of UnLz77 functions (fixes mgba.io/i/2141)
 - GBA DMA: Fix DMA source direction bits being cleared (fixes mgba.io/i/2410)
 - GBA I/O: Redo internal key input, enabling edge-based key IRQs
 - GBA I/O: Disable open bus behavior on invalid register 06A
 - GBA Memory: Fix misaligned 32-bit I/O loads (fixes mgba.io/i/2307)
 - GBA Video: Fix OpenGL rendering on M1 Macs
 - GBA Video: Ignore horizontally off-screen sprite timing (fixes mgba.io/i/2391)
 - GBA Video: Fix Hblank timing (fixes mgba.io/i/2131, mgba.io/i/2310)
 - GBA Video: Fix rare crash in modes 3-5
 - GBA Video: Fix sprites with mid-frame palette changes in GL (fixes mgba.io/i/2476)
 - GBA Video: Fix OBJ tile wrapping with 2D char mapping (fixes mgba.io/i/2443)
 - GBA Video: Fix horizontal lines in GL when charbase is changed (fixes mgba.io/i/1631)
 - GBA Video: Fix sprite layer priority updating in GL
Other fixes:
 - ARM: Disassemble Thumb mov pseudo-instruction properly
 - ARM: Disassemble ARM asr/lsr #32 properly
 - ARM: Disassemble ARM movs properly
 - Core: Don't attempt to restore rewind diffs past start of rewind
 - Core: Fix the runloop resuming after a game has crashed (fixes mgba.io/i/2451)
 - Core: Fix crash if library can't be opened
 - Debugger: Fix crash with extremely long CLI strings
 - Debugger: Fix multiple conditional watchpoints at the same address
 - FFmpeg: Fix crash when encoding audio with some containers
 - FFmpeg: Fix GIF recording (fixes mgba.io/i/2393)
 - GB: Fix temporary saves
 - GB: Fix replacing the ROM crashing when accessing ROM base
 - GB: Don't try to map a 0-byte SRAM (fixes mgba.io/i/2668)
 - GB, GBA: Save writeback-pending masked saves on unload (fixes mgba.io/i/2396)
 - mGUI: Fix FPS counter after closing menu
 - Qt: Fix some hangs when using the debugger console
 - Qt: Fix crash when clicking past last tile in viewer
 - Qt: Fix preloading for ROM replacing
 - Qt: Fix screen not displaying on Wayland (fixes mgba.io/i/2190)
 - Qt: Fix crash when selecting 256-color sprite in sprite view
 - Qt: Fix coloration of swatches on styles with distinct frame backgrounds
 - VFS: Failed file mapping should return NULL on POSIX
Misc:
 - Core: Suspend runloop when a core crashes
 - Core: Add wallclock offset RTC type
 - Debugger: Save and restore CLI history
 - Debugger: GDB now works while the game is paused
 - Debugger: Add command to load external symbol file (fixes mgba.io/i/2480)
 - FFmpeg: Support dynamic audio sample rate
 - GB: Support CGB0 boot ROM loading
 - GB Audio: Increase sample rate
 - GB MBC: Filter out MBC errors when cartridge is yanked (fixes mgba.io/i/2488)
 - GB MBC: Partially implement TAMA5 RTC
 - GB Video: Add default SGB border
 - GBA: Automatically skip BIOS if ROM has invalid logo
 - GBA: Refine multiboot detection (fixes mgba.io/i/2192)
 - GBA Cheats: Implement "never" type codes (closes mgba.io/i/915)
 - GBA DMA: Enhanced logging (closes mgba.io/i/2454)
 - GBA Memory: Implement adjustable EWRAM waitstates (closes mgba.io/i/1276)
 - GBA Savedata: Store RTC data in savegames (closes mgba.io/i/240)
 - GBA Video: Implement layer placement for OpenGL renderer (fixes mgba.io/i/1962)
 - GBA Video: Fix highlighting for sprites with mid-frame palette changes
 - mGUI: Add margin to right-aligned menu text (fixes mgba.io/i/871)
 - mGUI: Autosave less frequently when fast-forwarding
 - Qt: Rearrange menus some
 - Qt: Clean up cheats dialog
 - Qt: Only set default controller bindings if loading fails (fixes mgba.io/i/799)
 - Qt: Save converter now supports importing GameShark Advance saves
 - Qt: Save positions of multiplayer windows (closes mgba.io/i/2128)
 - Qt: Add optional frame counter to OSD (closes mgba.io/i/1728)
 - Qt: Add optional emulation-related information on reset (closes mgba.io/i/1780)
 - Qt: Add QOpenGLWidget cross-thread codepath for macOS (fixes mgba.io/i/1754)
 - Qt: Enable -b for Boot BIOS menu option (fixes mgba.io/i/2074)
 - Qt: Add tile range selection to tile viewer (closes mgba.io/i/2455)
 - Qt: Show warning if XQ audio is toggled while loaded (fixes mgba.io/i/2295)
 - Qt: Add e-Card passing to the command line (closes mgba.io/i/2474)
 - Qt: Boot both a multiboot image and ROM with CLI args (closes mgba.io/i/1941)
 - Qt: Improve cheat parsing (fixes mgba.io/i/2297)
 - Qt: Change lossless setting to use WavPack audio
 - Qt: Use FFmpeg to convert additional camera formats, if available
 - Qt: Resume crashed game when loading a save state
 - Qt: Include cheats in bug report
 - SDL: Support exposing an axis directly as the gyro value (closes mgba.io/i/2531)
 - Windows: Attach to console if present
 - VFS: Early return NULL if attempting to map 0 bytes from a file
 - Vita: Add bilinear filtering option (closes mgba.io/i/344)

---
## [j-sv/dwm](https://github.com/j-sv/dwm)@[67d76bdc68...](https://github.com/j-sv/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Thursday 2022-10-13 09:58:28 by Chris Down

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
## [Smalltasty/tgstation](https://github.com/Smalltasty/tgstation)@[a2e0ab3ff0...](https://github.com/Smalltasty/tgstation/commit/a2e0ab3ff0540a6e527e2f1d39c71525303ed75b)
#### Thursday 2022-10-13 10:31:58 by IndieanaJones

Spider Rebalance PR: Burn Baby Burn Edition (#68971)



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

---
## [Mu-L/hhvm](https://github.com/Mu-L/hhvm)@[cbeeb6fc89...](https://github.com/Mu-L/hhvm/commit/cbeeb6fc896d862aff10cd75bc42ee79beb962a9)
#### Thursday 2022-10-13 12:14:48 by Lucian Wischik

I believe we never use changes_since_baseline

Summary:
Naming_sqlite stores a table that only ever has a single row: NAMING_LOCAL_CHANGES, whose row contains (1) an ocaml blob of local changes, (2) the revision for this saved-state.

The ocaml blob of local changes had been used for fast incremental naming table generation, as an ugly hack that was faster than generating the entire new naming-table from scratch i.e. writing 6M rows. In D31413518 (https://github.com/facebook/hhvm/commit/8f9e9d2f1568b084660bda8fe87b8725d61674d1) (Oct 2021) bobrenjc93 changed it to a much better technique, namely, inserting/removing only the delta rows. But it left behind the ocaml-blob of local changes. I wrote at the time "We should get rid of it: either in this diff or the next, delete the entire LocalChanges module." What gives us surety that it's okay to delete the ocaml-blob is that I had added telemetry D28839883 (https://github.com/facebook/hhvm/commit/330e97ccd08b144117c21a3ebefa248061d3d5ed) (June 2021) on the code-paths which read the ocaml-blob, and the telemetry shows that we only ever read an empty ocaml-blob.

But what about the second item, "(2) revision for this saved-state"? Do we ever use that? Reading the code shows that the only place "revision-for-saved-state" is ever consumed is by Hulk.v1 in a codepath that appears not to exist any longer, inside Naming_table.choose_local_changes. I think that Hulk.v1 used to provide a naming-table-delta along with the revision that the delta is with respect to, and it used to compare that revision against the naming-table-sqlite that it got from disk, and fail if they were different. This check had been introduced in D18723777 (https://github.com/facebook/hhvm/commit/7c671def9ee84762cf38e16d761c140a4bf01eca) (Nov 2019) for hulk remote workers. My hunch is that we're not using it any longer.

Therefore, this diff adds telemetry on the only codepath that uses "revision-for-saved-state" from the NAMING_LOCAL_CHANGES row. If this telemetry proves that we don't use it, and we already have telemetry which proves that ocaml-blob is always empty, then we'll be confident in deleting NAMING_LOCAL_CHANGES.

Reviewed By: bobrenjc93

Differential Revision: D40118751

fbshipit-source-id: 0b8e2eac4cfe8513cc5d0155184b7d15efd99dc8

---
## [wspk/Dodgeball](https://github.com/wspk/Dodgeball)@[8f00254240...](https://github.com/wspk/Dodgeball/commit/8f00254240f430fc076d0010b77d728b71f38c0d)
#### Thursday 2022-10-13 12:23:09 by nolan-3

1. Changed Knight to a functional component so that
I could call an event listener for key input, however now it doesn't run in the gameloop so it's
quite clunky. 2. Downloaded Xcode and tried to convert this into native code for android/ios, I d
on't think it worked. Finally I would just like to say I think this solution for moving is quite
poor, maybe making it back into an entity and having it rerender each time the loop runs would wo
rk. I just kept getting an error Invalid hook call. Hooks can only be called inside of the body of a function component. This could happen for one of the following reasons:

You might have mismatching versions of React and the renderer (such as React DOM)
You might be breaking the Rules of Hooks
You might have more than one copy of React in the same app See for tips about how to debug and fix this problem. I believe it was number 2 and I wasn't sure how to work around it.

---
## [wspk/Dodgeball](https://github.com/wspk/Dodgeball)@[4984f9e44e...](https://github.com/wspk/Dodgeball/commit/4984f9e44e0b0060026c0e4512c4e7e79ee3815d)
#### Thursday 2022-10-13 12:23:09 by nolan-3

1. Changed Knight to a functional component so that I could call an event listener for key input, however now it doesn't run in the gameloop so it's quite clunky. 2. Downloaded Xcode and tried to convert this into native code for android/ios, I don't think it worked. Finally I would just like to say I think this solution for moving is quite poor, maybe making it back into an entity and having it rerender each time the loop runs would work. I just kept getting an error Invalid hook call. Hooks can only be called inside of the body of a function component. This could happen for one of the following reasons:

You might have mismatching versions of React and the renderer (such as React DOM)
You might be breaking the Rules of Hooks
You might have more than one copy of React in the same app See for tips about how to debug and fix this problem. I believe it was number 2 and I wasn't sure how to work around it.

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[72c451d2a0...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/72c451d2a009a6d18f8119e96fd2fffb5311a3db)
#### Thursday 2022-10-13 13:07:13 by petrero

10.4. Custom Entity Methods & Twig Magic

  A Second Custom Entity Method!
  While we're here, the broken images - caused by the placeholder site I'm using being down - are... kind of annoying! Time to fix those!

  In a real app, we'll probably let our users upload real images... though for now, we'll stick with dummy images. But either way, we'll probably need the ability to get the URL to a vinyl mix's image from multiple places in our code. To make that easy and keep the code centralized, let's add another entity method!

  How about public function getImageUrl(). Give this a $width argument so we can ask for different sizes. Inside I'll paste in some code that uses a different service for dummy images. This looks a bit fancy - but I'm just trying to use the id to get a predictable, but random image... skipping the first 50, which are all nearly identical on this site.

  Anyways, now we have this nice reusable method!

  Back in the template... up here is where I have the hardcoded image URL. Replace this with mix.imageUrl(), but this time, we do need to pass an argument. Pass 300... and let's update the alt attribute as well to Mix album cover.

  If we go over and refresh... lovely. Our mixes have images!

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[17248c38c8...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/17248c38c89ac1650ce62157be30c8ec0dbe9dc1)
#### Thursday 2022-10-13 13:07:13 by petrero

6. Migrations

  We created an entity class! But... that's it. The corresponding table does not yet exist in our database.

  Let's think. In theory, Doctrine knows about our entity, all of its properties and their ORM\Column attributes. So... shouldn't Doctrine be able to make that table for us automatically? Yes! It can.

  The make:migration Command
  - When we installed Doctrine earlier, it came with a migrations library that's amazing. Check it out! Whenever you make a change to your database structure - like adding a new entity class, or even adding a new property to an existing entity, you should spin over to your terminal and run:

    symfony console make:migration
  In this case, I'm running symfony console because this is going to talk to our database. Run that and... perfect! It created one new file in a migrations/ directory with a timestamp for today's date. Let's go check it out! Find migrations/ and open the new file.

  This holds a class with up() and down() methods... though I never run migrations in the "down" direction, so we'll focus only on up(). And... this is great! The migrations command saw our VinylMix entity, realized that its table was missing in the database, and generated the SQL needed in Postgres to create it, including all of the columns. That was so easy.

  Executing the Migration
  Ok... so how do we execute this migration? Back at your terminal, run:

    symfony console doctrine:migrations:migrate
  Say y to confirm and... beautiful! It tells us that it's Migrating up to that specific version. It seems... like that worked! To make sure, you can try another bin/console command:

    symfony console doctrine:query:sql 'SELECT * FROM vinyl_mix'
  When we try that... whoops! Pardon my typo... nothing to see here. Try that again and... perfect! We didn't get an error! It just says that The query yielded an empty result set. If that table did not exist, like vinyl_foo, Doctrine would have screamed at us.

  So, the migration did run!

  How Migrations Work
  - This beautiful system deserves some explanation. Run

    symfony console doctrine:migrations:migrate
  again. Check it out! It's smart enough to avoid executing that migration a second time! It knows that it already did that. But... how? Try running a different command:

    symfony console doctrine:migrations:status
  This gives some general info about the migration system. The most important part is in Storage where it says Table Name and doctrine_migration_versions.

  Here's the deal: the first time we executed the migration, Doctrine created this special table, which literally stores a list of all of the migration classes that have been executed. Then, each time we run doctrine:migrations:migrate, it looks in our migrations/ directory, finds all the classes, checks the database to see which have not already been executed, and only calls those. Once the new migrations finish, it adds them as rows to the doctrine_migration_versions table.

  You can visualize this table by running:

    symfony console doctrine:migrations:list
  It sees our one migration and knows it already ran it. It even has the date!

  This is cool... but let's push it further. Next, let's add a new property to our entity and generate a second migration to add the column.

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[1ff11195e8...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/1ff11195e894e1f0ab02b361b53a34d3b1fb040e)
#### Thursday 2022-10-13 13:07:13 by petrero

7.1 Adding new Properties - symfony console doctrine:schema:update --dump-sql

  In our VinylMix entity, I forgot to add a property earlier: votes. We're going to keep track of the number of up votes or down votes that a particular mix has.

  Modifying with make:entity
  - Ok... so how can we add a new property to an entity? Well, we can absolutely do it by hand: all we need to do is create the property and the getter and setter methods. But, a much easier way is to head back to our favorite make:entity command:

    php bin/console make:entity
  This is used to create entities, but we can also use it to update them. Type VinylMix as the class name and... it sees that it exists! Add a new property: votes... make it an integer, say "no" to nullable.. then hit "enter" to finish.

  The end result? Our class has a new property... and getter and setter methods below.

  Generating a Second Migration
  - Ok, let's think. We have a vinyl_mix table in the database... but it does not yet have the new votes column. We need to alter the table to add it. How can we do that? The exact same way as before: with a migration! At your terminal, run:

    symfony console make:migration
  Then go check out the new class.

  This is amazing! Inside the up() method, it says

    ALTER TABLE vinyl_mix ADD votes INT NOT NULL

  So it saw our VinylMix entity, checked out the vinyl_mix table in the database, and generated a diff between them. It realized that, in order to make the database look like our entity, it needed to alter the table and add that votes column. That's simply amazing.

  Back over at the terminal, if you run

    symfony console doctrine:migrations:list
  you'll see that it recognizes both migrations and it knows that it has not executed the second one. To do that, run:

    symfony console doctrine:migrations:migrate
  Doctrine is smart enough to skip the first and execute the second. Nice!

  When you deploy to production, all you need to do is run doctrine:migrations:migrate each time. It will handle executing any and all migrations that the production database hasn't yet executed.

  Giving Properties Default Values
  - Ok, one more quick thing while we're here. Inside of VinylMix, the new votes property defaults to null. But when we create a new VinylMix, it would make a lot of sense to default the votes to zero. So let's change this to = 0.

  Cool! And if we do that, the property in PHP no longer needs to allow null... so remove the ?. Because we're initializing to an integer, this property will always be an int: it will never be null.

  But... I wonder... because I made this change, do I need to alter anything in my database? The answer is no. I can prove it by running a helpful command:

    symfony console doctrine:schema:update --dump-sql
  This is very similar to the make:migration command... but instead of generating a file with the SQL, it just prints out the SQL needed to bring your database up to date. In this case, it shows that our database is already in sync with our entity.

  The point is: if we initialize the value of a property in PHP... that's just a PHP change. It doesn't change the column in the database or give the column a default value, which is totally fine.

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[abd909f4d7...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/abd909f4d7301d134a84190695e4200960df2f46)
#### Thursday 2022-10-13 13:07:13 by petrero

10.3. Custom Entity Methods & Twig Magic

  Adding a Custom Entity Method
  - Ok, so votes can be positive or negative. To make that super obvious, I want to print a plus sign in front of the positive votes. We could do that by adding some logic in Twig. But remember, we have this nice entity class! Sure, right now it only has getter and setter methods. But we are allowed to add our own custom methods. And that's a great way to organize your code.

  Check it out: create a new public function called, how about getVotesString(), which will return a 🥝. I'm kidding, it'll return a string of course. Then calculate the "+" or "-" prefix with some fancy logic that says:

    If the votes are equal to zero, we want no prefix. If the votes are greater than zero, we want a plus symbol. Else we want a minus symbol.

  And... let me surround this entire second statement in parenthesis. This is probably the fanciest line of code I've ever written... which also means it's the most confusing! Feel free to break this onto multiple lines.

  At the bottom, return sprintf() with %s, which will be the prefix, and %d, which will be the vote count. Pass these in: $prefix then the absolute value of $this->votes... since we're adding the negative sign in manually.

  We can now use this nice method anywhere in our app... like from inside a template with mix.getVotesString(). Or shorten this to mix.votesString.

  Twig is smart enough to realize that votesString is not a real property... but that there is a getVotesString() method. And so, it will call that. Think of this as a virtual property inside of Twig.

  If we fly back over and refresh... awesome! We get the minus and plus signs.

---
## [petre-symfony/symfony-6-and-the-database](https://github.com/petre-symfony/symfony-6-and-the-database)@[79c5a7e042...](https://github.com/petre-symfony/symfony-6-and-the-database/commit/79c5a7e042d8865d499446a791012469e64ca96b)
#### Thursday 2022-10-13 13:07:13 by petrero

8.3. Persisting to the Database

  Hello Entity Manager!
  - Anyway, now that we have an object, how can we save it? Well, saving something to the database is work. And so, no surprise, that work is done by a service! Add an argument to the method, type-hinted with EntityManagerInterface. Let's call it $entityManager.

  EntityManagerInterface is, by far, the most important service for Doctrine. We're going to use it to save, and indirectly when we query. To save, call $entityManager->persist() and pass it the object that we want to save (in this case, $mix). Then we also need to call $entityManager->flush() with no arguments.

  But... wait. Why do we have to call two methods?

  Here's the deal. When we call persist(), that doesn't actually save the object or talk to the database at all. It just tells Doctrine:

    Hey! I want you to be "aware" of this object, so that later when we call flush(), you'll know to save it.

  Most of the time, you'll see these two lines together - persist() and then flush(). The reason it's split into two methods is to help with batch data loading... where you could persist a hundred $mix objects and then flush them to the database all at once, which is more efficient. But most of the time, you'll call persist() and then flush().

  Okay, to make this a valid page, let's return new Response() from HttpFoundation and I'll use sprintf to return a message: mix %d is %d tracks of pure 80\'s heaven... and for those two wildcards, pass $mix->getId() and $mix->getTrackCount().

  Let's try it! Move over, refresh and... yes! We see "Mix 1". That's so cool! We never actually set the ID (which makes sense). But when we saved, Doctrine grabbed the new ID and put that onto the id property.

  If we refresh a few more times, we get mixes 2, 3, 4, 5, and 6. That's super fun. All we had to do is persist and flush the object. Doctrine handles all of the querying stuff for us.

  Another way we can prove this is working is by running:

    symfony console doctrine:query:sql 'SELECT * FROM vinyl_mix'
  This time, we do see the results. Awesome!

Okay, now that we have stuff in the database, how do we query for it? Let's tackle that next.

---
## [aslenofarid/kernel_asus_sdm660](https://github.com/aslenofarid/kernel_asus_sdm660)@[ff8c25efb5...](https://github.com/aslenofarid/kernel_asus_sdm660/commit/ff8c25efb50b9b87c951ccf9946f232df59cdd7e)
#### Thursday 2022-10-13 13:26:19 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Dede Dindin Qudsy <xtrymind@gmail.com>
Signed-off-by: aslenofarid <yoniasleno.farid14@gmail.com>

---
## [kulcris/DarkRP](https://github.com/kulcris/DarkRP)@[70733fd592...](https://github.com/kulcris/DarkRP/commit/70733fd5928367e97070777b7aa7561c6c6bc676)
#### Thursday 2022-10-13 14:38:17 by FPtje

Clearing decals doesn't fix lag.

Stop fucking pressing that god damn button every 10
motherfucking seconds.

---
## [ajwerner/cockroach](https://github.com/ajwerner/cockroach)@[f50670b344...](https://github.com/ajwerner/cockroach/commit/f50670b3440e91bec05aebc1bc425e4dd465583f)
#### Thursday 2022-10-13 17:21:13 by Tobias Grieger

rpc: re-work connection maintenance

This commit simplifies the `rpc` package.

The main aim is to make the code and the logging it produces somewhat
clearer and to pave the way for an ultimate merging of `nodedialer` with
`rpc` as well as adoption of the `util/circuit` package (async-based
circuit breaker).

`rpc.Context` hadn't aged well. Back in the day, it was a connection
pool that held on to connections even when they failed. The heartbeat
loop would run forever and its latest outcome would reflect the health
of the connection. We relied on gRPC to reconnect the transport as
necessary.

At some point we realized that leaving the connection management to
gRPC could cause correctness issues. For example, if a node is de-
commissioned and brought up again, gRPC might reconnect to it but
now we have a connection that claims to be for node X but is actually
for node Y. Similarly, we want to be able to vet that the remote
node's cluster version is compatible with ours before letting any
messages cross the connection.

To achieve this, we added `onlyOnceDialer` - a dialer that fails
all but the first attempt to actually connect, and in particular
from that point on connections were never long lived once they
hit a failure state.

Still, the code and testing around the heartbeat loop continued
to nurture this illusion. I found that quite unappealing as it
was sure to throw off whoever would ultimately work on this code.

So, while my original impetus was to produce better log messages
from `rpc.Context` when there were connection issues, I took
the opportunity to simplify the architecture of the code to
reflect what it actually does.

In doing so, a few heartbeat-related metrics were removed, as they made
limited sense in a world where failing connections get torn down (i.e.
our world).

Connection state logging is now a lot nicer. Previously, one would very
frequently see the onlyOnceDialer's error "cannot reuse client
connection" which, if one is not familar with the concept of the
onlyOnceDialer is completely opaque, and for those few in the know is an
unhelpful error - you wanted the error that occurred during dialing.

I paid special attention to the "failfast" behavior. If connections
don't stay in the pool when they are unhealthy, what prevents us from
dialing down nodes in a tight loop? I realized that we got lucky with
our use of onlyOnceDialer because it would always prompt gRPC to do
one retry, and at a 1s backoff. So, the connection would stay in the
pool for at least a second, meaning that this was the maximum frequency
at which we'd try to connect to a down node.

My cleanups to onlyOnceDialer in pursuit of better logging elimitated
this (desirable) property. Instead we now skip the log messages should
they become too frequent. I claim that this is acceptable for now since
the vast majority of callers go through a `node.Diaelr`, which has a
circuit breaker (letting callers through at most once per second).

We previously configured gRPC with a 20s dial timeout. That means that
if a remote is unreachable, we'd spend 20s just trying to dial it,
possibly tying up callers that could be trying a reachable node in the
meantime. That seemed wildly too large; I am reducing it to 5s here
which is still generous (but there's a TLS handshake in here so better
not make it too tight).

We previously tried to re-use connections that were keyed with a NodeID
for dial attempts that didn't provide a NodeID. This caused some issues
over the years and was now removed; the extra RPC connections are
unlikely to cause any issues.

The internal connection map is now a plain map with an RWMutex. This is
just easier and gets the job done. The code has simplified as a result
and it's clearer that it's correct (which it repeatedly was not in the
past).

I implemented redactability for gRPC's `status.Status`-style errors,
so they format nicer and at least we get to see the error code (the
error message is already flattened when gRPC hands us the error,
sadly).

There are various other improvements to errors and formatting. The
following are excerpts from the health channel when shutting down
another node in a local cluster:

Connection is first established:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 3  connection is now ready

n1 goes down, i.e. existing connection is interrupted (this error comes
from `onlyOnceDialer`):

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 35  closing
connection after: ‹rpc error: code = Unavailable desc = connection
error: desc = "transport: Error while dialing connection interrupted
(did the remote node shut down or are there networking issues?)"›

Reconnection attempts; these logs are spaced 1-2s apart:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 37  unable to
connect (is the peer up and reachable?): initial connection heartbeat
failed: ‹rpc error: code = Unavailable desc = connection error: desc =
"transport: Error while dialing dial tcp 127.0.0.1:26257: connect:
connection refused"›

n3 is back up:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 49  connection is now ready

There are other connection errors in the logs that stem from operations
checking for a healthy connection, failing to get through circuit
breakers, etc., such as these:

> [n3,intExec=‹claim-jobs›,range-lookup=/Table/15/4/‹NULL›] 33  unable
to connect to n1: failed to check for ready connection to n1 at
‹127.0.0.1:26257›: ‹connection not ready: TRANSIENT_FAILURE›

Release note (general change): Previously, CockroachDB employed a 20s
connection timeout for cluster-internal connections between nodes.  This
has been reduced to 5s to potentially reduce the impact of network
issues.

Release note (general change): Previously, CockroachDB (mostly) shared a
TCP connection for the KV and Gossip subsystems. They now use their own
connection each, so the total number of outgoing and incoming TCP
connections at each node in the cluster will increase by 30 to 50
percent.

---
## [tbkka/swift-protobuf](https://github.com/tbkka/swift-protobuf)@[e47f7304c9...](https://github.com/tbkka/swift-protobuf/commit/e47f7304c909f2849648c790233cd4894a5477c5)
#### Thursday 2022-10-13 17:34:32 by FranzBusch

Add SPM plugin

# Motivation
SPM is providing new capabilities for tools to expose themselves as plugins which allows them to generate build commands. This allows us to create a plugin for `SwiftProtobuf` which invokes the `protoc` compiler and generates the Swift code. Creating such a plugin is greatly wanted since it improves the usage of the `protoc-gen-swift` plugin dramatically. Fixes https://github.com/apple/swift-protobuf/issues/1207

# Modification
This PR adds a new SPM plugin which generates build commands for generating Swift files from proto files. Since users of the plugin might have complex setups, I introduced a new `swift-protobuf-config.json` file that adopters have to put into the root of their target which wants to use the new plugin. The format of this configuration file is quite simple:

```json
{
    "invocations": [
        {
            "protoFiles": [
                "Foo.proto"
            ],
            "visibility": "internal"
        }
    ]
}

```

It allows you to configure multiple invocations to the `protoc` compiler. For each invocation you have to pass the relative path from the target source to the proto file. Additionally, you have to decide which visibility the generated symbols should have. In my opinion, this configuration files gives us the most flexibility and more complex setups to be covered as well.

# Open topics

## Hosting of the protoc binary
Hosting of the protoc binary is the last open thing to figure out before we can release a plugin for `SwiftProtobuf`. From my point of view, there are three possible routes we can take:

1. Include the `artifactbundle` inside the `SwiftProtobuf` repository
2. Include the `artifactebundle` as an artifact on the GH releases in the protobuf repo
3. Extend the the artifact bundle manifest to allow inclusion of URLs. This would require a Swift evolution pitch most likely.

However, with all three of the above we would still need to release a new version of `SwiftProtobuf` with every new release of `protoc`.

# Future work

## Proto dependencies between modules
With the current shape of the PR one can already use dependencies between proto files inside a single target. However, it might be desirable to be able to build dependency chains of Swift targets where each target includes proto files which depend on protoc files from the dependencies of the Swift target. I punted this from the initial plugin because this requires a bit more work and thinking. Firstly, how would you even spell such an import? Secondly, the current way of doing `ProtoPathModuleMapping` files is not super ideal for this approach. It might make sense to introduce a proto option to set the Swift module name inside the proto files already.

# Result
We now have a SPM plugin that can generate Swift code from proto files. To use it, it provides a configuration file format to declare different invocations to the `protoc` compiler.

---
## [dlmather/cluster-api-provider-aws](https://github.com/dlmather/cluster-api-provider-aws)@[867afc7ac7...](https://github.com/dlmather/cluster-api-provider-aws/commit/867afc7ac718621a11e00fc2b05589ac2548d4d5)
#### Thursday 2022-10-13 17:52:48 by Claudia Beresford

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
## [TrashDoxx/TG](https://github.com/TrashDoxx/TG)@[a2577296e6...](https://github.com/TrashDoxx/TG/commit/a2577296e62a0f3c335648169a335fe7d3de4bdc)
#### Thursday 2022-10-13 17:57:40 by RikuTheKiller

Upgrades the Modsuit Adapter Shell (#70286)

Code improvements are much appreciated as some things may be rather hacky.

Adds more options to the currently very limited modsuit adapter shell. Right now you can only select a module and activate (not deploy) the suit.

This has some major problems as you literally can't even deploy the suit to activate it so that's rendered useless and selecting a module is like... kind of a weird input anyways but I won't judge so I left it in. Please comment down below if you'd like for me to add an "Activate Selected Module" input and "On Module Activated" output as those are certainly possible to do. I was just a little torn on how balanced that would be.

Changes:

"Module to Select" input is now an option. You can still use a string input, but simply inserting it into the suit and activating it, then accessing the circuit that way will give you a list of all modules that the modsuit has.
Modsuit quick deploy (RMB) no longer tries to deploy the rest of the pieces when used while the suit is only partially deployed. It will now instead retract the extended pieces. This makes the "Toggle Deployment" input less prone to errors. (Why was it like this in the first place? Having to manually retract the already extended pieces sucks ass.)
Added Inputs:

"Toggle Deployment" is a new signal input that does exactly what it says it does. It simply tries to extend or retract all pieces of the modsuit depending on it's current state.
Added Outputs:

"Activated" is a new number output that outputs 1 if the suit is activated and 0 if it's not.
"Deployed" is a new number output that outputs 1 if all parts of the suit are extended and 0 if they aren't.
"Deployed Parts" is a new string list output that outputs a list of the names of all currently deployed parts.
"On Deploy" is a new signal output that outputs a signal whenever all parts of the suit are deployed or retracted, regardless of the method used.
"Finished Toggling" is a new signal output that outputs a signal whenever the suit has finished activating or deactivating, regardless of the method used.

---
## [mizz141/PlexAniSync-Mappings](https://github.com/mizz141/PlexAniSync-Mappings)@[6b1e164d9a...](https://github.com/mizz141/PlexAniSync-Mappings/commit/6b1e164d9ae50b36898fe7d572b511243061a8bc)
#### Thursday 2022-10-13 18:00:18 by mizz141

Add more mappings (#60)

* Add more mappings

Akashic Records of Bastard Magical Instructor

D-Frag!

The Melancholy of Haruhi Suzumiya > Edited, added Season 2, 2009 re-airing.

Dropkick on My Devil!

If Her Flag Breaks

Magical Girl Lyrical Nanoha

The Maid I Recently Hired Is Mysterious

Ore no Imouto ga Konnani Kawaii Wake ga Nai >>> Oreimo

Redo of Healer

Tenjo Tenge

We Never Learn

The World God Only Knows

---
## [MidoriWroth/tgstation](https://github.com/MidoriWroth/tgstation)@[fc7c186957...](https://github.com/MidoriWroth/tgstation/commit/fc7c186957088b6ffd0605f814bea754670c0212)
#### Thursday 2022-10-13 18:10:26 by RikuTheKiller

Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

---
## [r4b3rt/linux](https://github.com/r4b3rt/linux)@[c388cc8040...](https://github.com/r4b3rt/linux/commit/c388cc804016cf0f65afdc2362b120aa594ff3e6)
#### Thursday 2022-10-13 18:28:57 by Serge Semin

clk: vc5: Fix 5P49V6901 outputs disabling when enabling FOD

We have discovered random glitches during the system boot up procedure.
The problem investigation led us to the weird outcomes: when none of the
Renesas 5P49V6901 ports are explicitly enabled by the kernel driver, the
glitches disappeared. It was a mystery since the SoC external clock
domains were fed with different 5P49V6901 outputs. The driver code didn't
seem like bogus either. We almost despaired to find out a root cause when
the solution has been found for a more modern revision of the chip. It
turned out the 5P49V6901 clock generator stopped its output for a short
period of time during the VC5_OUT_DIV_CONTROL register writing. The same
problem was found for the 5P49V6965 revision of the chip and was
successfully fixed in commit fc336ae622df ("clk: vc5: fix output disabling
when enabling a FOD") by enabling the "bypass_sync" flag hidden inside
"Unused Factory Reserved Register". Even though the 5P49V6901 registers
description and programming guide doesn't provide any intel regarding that
flag, setting it up anyway in the officially unused register completely
eliminated the denoted glitches. Thus let's activate the functionality
submitted in commit fc336ae622df ("clk: vc5: fix output disabling when
enabling a FOD") for the Renesas 5P49V6901 chip too in order to remove the
ports implicit inter-dependency.

Fixes: dbf6b16f5683 ("clk: vc5: Add support for IDT VersaClock 5P49V6901")
Signed-off-by: Serge Semin <Sergey.Semin@baikalelectronics.ru>
Reviewed-by: Luca Ceresoli <luca@lucaceresoli.net>
Link: https://lore.kernel.org/r/20220929225402.9696-2-Sergey.Semin@baikalelectronics.ru
Signed-off-by: Stephen Boyd <sboyd@kernel.org>

---
## [Zygo/bees](https://github.com/Zygo/bees)@[14ce81c081...](https://github.com/Zygo/bees/commit/14ce81c081e2aa3104e78bb74a54ecccd4624d0d)
#### Thursday 2022-10-13 20:11:59 by Zygo Blaxell

fs: get rid of silly base class that causes build failures now

The base class thing was an ugly way to get around the lack of C99
compound literals in C++, and also to make the bare ioctls usable with
the derived classes.

Today, both clang and gcc have C99 compound literals, so there's no need
to do crazy things with memset.  We never used the derived classes for
ioctls, and for this specific ioctl it would have been a very, very bad
idea, so there's no need to support that either.  We do need to jump
through hoops for ostream& operator<<() but we had to do those anyway
as there are other members in the derived type.

So we can simply drop the base class, and build the args object on the
stack in `do_ioctl`.  This also removes the need to verify initialization.

There's no bug here since the `info` member of the base class was
never used in place by the derived class, but new compilers reject the
flexible array member in the base class because the derived class makes
`info` be not at the end of the struct any more:

	error: flexible array member btrfs_ioctl_same_args::info not at end of struct crucible::BtrfsExtentSame

Fixes: https://github.com/Zygo/bees/issues/232
Signed-off-by: Zygo Blaxell <bees@furryterror.org>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[e9d4bf6c49...](https://github.com/Paxilmaniac/Skyrat-tg/commit/e9d4bf6c4920f07f03c2425ac3e69caf8daced9d)
#### Thursday 2022-10-13 21:35:14 by Zergspower

Granite's Love pass 1 of X for ruins  (#16746)

* Fab Five

* forgot to move the rack in front of the false wall

* Holy shit scrapheap looked HORRIBLE

---
## [peff/git](https://github.com/peff/git)@[6d021ce6c3...](https://github.com/peff/git/commit/6d021ce6c36c013fe0e6d6b7a6fb3672c2749352)
#### Thursday 2022-10-13 22:05:48 by Jeff King

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
## [peff/git](https://github.com/peff/git)@[ba592861d9...](https://github.com/peff/git/commit/ba592861d92c06ad4b9cdc9d71327bb1df5296b8)
#### Thursday 2022-10-13 22:05:58 by Jeff King

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
## [jonluca/react](https://github.com/jonluca/react)@[b6978bc38f...](https://github.com/jonluca/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Thursday 2022-10-13 22:25:23 by Andrew Clark

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
## [MushiTea/21438_ChaoticCurrent_REPO](https://github.com/MushiTea/21438_ChaoticCurrent_REPO)@[8dbe808af3...](https://github.com/MushiTea/21438_ChaoticCurrent_REPO/commit/8dbe808af30a67b6a4251103566238f3d279375e)
#### Thursday 2022-10-13 22:25:37 by MushiTea

Walter Hartwell White Sr., also known by his drug-lord alias Heisenberg, is the main character of the American crime drama television series Breaking Bad, portrayed by Bryan Cranston.

Walter was a skilled chemist and co-founder of a technology firm before he accepted a buy-out from his partners. Walt became a high-school chemistry teacher in Albuquerque, and barely making ends meet with his family with wife Skyler (Anna Gunn) and son Walt Jr. (RJ Mitte). At the start of the series, the day after his 50th birthday, Walt is diagnosed with Stage III lung cancer. After this discovery, Walt resorts to manufacturing and selling methamphetamines with a former student, Jesse Pinkman (Aaron Paul), to ensure his family's financial security after his death. Due to his chemistry training and production route, Walt's "blue meth" is purer than any other on the market, and he is pulled deeper into the illicit drug trade. Walt becomes more and more ruthless as the series progresses, and later adopts the alias "Heisenberg", which becomes recognizable as a kingpin figure in the Southwestern drug trade. Walt struggles with managing his family while hiding his involvement in the drug business from his brother-in-law and DEA agent Hank Schrader (Dean Norris).

Walt becomes less sympathetic throughout the show, as series creator Vince Gilligan wanted him to turn from "Mr. Chips into Scarface". Although AMC officials initially hesitated to cast Cranston due to his previous comedic role on Malcolm in the Middle, Gilligan cast him based on the actor's past performance in The X-Files episode "Drive", which Gilligan wrote. Cranston contributed greatly to the creation of his character, including Walt's backstory, personality, and physical appearance.

Both the character and Cranston's performance have received critical acclaim, with White frequently being mentioned as one of the greatest and most iconic television characters of all time. Cranston won four Primetime Emmy Awards for Outstanding Lead Actor in a Drama Series, three of them being consecutive. He is the first man to win a Critics' Choice, Golden Globe, Primetime Emmy, and Screen Actors Guild Award for his performance. Cranston reprised the role of Walt in a flashback for Breaking Bad's sequel film El Camino, and again in the sixth and final season of the prequel series Better Call Saul, making him one of the few characters to appear in all three, alongside Jesse Pinkman, Mike Ehrmantraut (Jonathan Banks), Ed Galbraith (Robert Forster), and Austin Ramey (Todd Terry).

Contents
1	Concept and creation
2	Character biography
2.1	Background
2.2	Appearances
2.2.1	Season 1
2.2.2	Season 2
2.2.3	Season 3
2.2.4	Season 4
2.2.5	Season 5
2.2.6	El Camino
2.2.7	Post Breaking Bad
3	Reception
3.1	Critical response
3.2	Accolades
4	Legacy
4.1	Cult following
4.2	Albuquerque statues
4.3	Obituary and funeral
4.4	Alternative theory concerning death
5	References
6	Further reading
7	External links
Concept and creation
You're going to see that underlying humanity, even when he's making the most devious, terrible decisions, and you need someone who has that humanity – deep down, bedrock humanity – so you say, watching this show, 'All right, I'll go for this ride. I don't like what he's doing, but I understand, and I'll go with it for as far as it goes.' If you don't have a guy who gives you that, despite the greatest acting chops in the world, the show is not going to succeed.

—Vince Gilligan, about Bryan Cranston[1]
Inspired by Tony Soprano, Breaking Bad creator Vince Gilligan had wanted his lead character to be a protagonist that turned into an antagonist over the course of the show,[2] or as he described, turning Mr. Chips into Scarface.[3] Gilligan also said, in 2013, "Without Tony Soprano, there would be no Walter White."[4] Gilligan needed to have this character come into a midlife crisis that would put him into seeking risky options and lead to more criminal activities. As the premise of Breaking Bad was based on a humorous idea that he and his fellow writer from The X-Files, Thomas Schnauz had come up with of driving around in an RV making methamphetamine, Gilligan made Walter a chemistry teacher, one who, until the start of the show, would have never violated the law.[5]

Gilligan cast Bryan Cranston for the role of Walter White based on having worked with him in "Drive", a sixth season episode of the science fiction television series The X-Files, where Gilligan worked as a writer. Cranston played an anti-Semite with a terminal illness who took Fox Mulder (David Duchovny) hostage. Gilligan said the character had to be simultaneously loathsome and sympathetic, and that "Bryan alone was the only actor who could do that, who could pull off that trick. And it is a trick. I have no idea how he does it."[1][5] AMC officials were initially reluctant with the casting choice, having known Cranston only as the over-the-top character Hal on the comedy series Malcolm in the Middle and approached actors John Cusack and Matthew Broderick about the role.[6] When both actors declined, the executives were persuaded to cast Cranston after seeing the X-Files episode.[7]

Cranston contributed a great deal to the character's persona. When Gilligan left much of Walter's past unexplained during the development of the series, the actor wrote his own backstory for the character. At the start of the show, Cranston gained 10 pounds to presage the character's gradual physical deterioration. He had the natural red highlights of his hair dyed brown. He collaborated with costume designer Kathleen Detoro on a wardrobe of mostly neutral green and brown colors to make the character bland and unremarkable, and worked with makeup artist Frieda Valenzuela to create a mustache he described as "impotent" and like a "dead caterpillar".[8][9] Cranston also repeatedly identified elements in scripts where he disagreed with how the character was handled, and would go so far as to call Gilligan directly when he could not work out disagreements with the episode's screenwriter(s). Cranston has said he was inspired partially by his father for how Walt carries himself physically, which he described as "a little hunched over, never erect, [as if] the weight of the world is on this man's shoulders".[5]

Gilligan has said it has been difficult to write for Walter White because the character is so dark and morally questionable.[5] As the series progressed, Gilligan and the writing staff of Breaking Bad made Walt more and more unsympathetic.[10] Cranston said by the fourth season: "I think Walt's figured out it's better to be a pursuer than the pursued. He's well on his way to badass."[11] Regarding White's fate in the series ending, Cranston foresaw it as "ugly [with no] redemption",[12] although earlier, Gilligan divulged his plans to "end on a high note, in a way that will satisfy everyone".[13]

Character biography
Background
When Walter White was six years old, his father died of Huntington's disease. He studied chemistry at California Institute of Technology and, after graduate school, worked as a researcher at Los Alamos National Laboratory. There he conducted research on proton radiography, that helped a team win a Nobel Prize in Chemistry in 1985.[14][15] Walt then founded the firm Gray Matter Technologies with Elliott Schwartz (Adam Godley), his former classmate and close friend.[16] Around this time, Walt dated his lab assistant, Gretchen Schwartz (Jessica Hecht). He left both Gretchen and Gray Matter Technologies, selling his financial interest in the company for $5,000.[15][17] Gretchen and Elliott later married and made a fortune, much of it from Walt's research.[17][18] Though they remain friendly, Walt secretly resents both Gretchen and Elliott for profiting from his work.[18][19]

At the age of 50, Walt works as a high school chemistry teacher in Albuquerque, New Mexico, providing instruction to uninterested and disrespectful students.[14][20] Walt also has another job at a local car wash to supplement his income, which proves to be particularly humiliating when he has to clean the cars of his own students.[21] Walt and his wife Skyler (Anna Gunn) have a teenage son named Walter Jr. (RJ Mitte), who has cerebral palsy. Skyler is also pregnant with their second child, Holly, who is born at the end of season two.[22] Walt's other family includes Skyler's sister, Marie Schrader (Betsy Brandt); her husband, Hank (Dean Norris), who is a DEA agent; and his mother, who is never seen.[23]

Appearances
The following appearances are based on the chronological narrative in Breaking Bad. Scenes from Better Call Saul fit into this chronology and are denoted appropriately.

Season 1
Further information: Breaking Bad (season 1)
On his 50th birthday, during his surprise party, Walt watches a news report about Hank arresting methamphetamine dealers. Walt is impressed by the monetary returns from the meth operation, and Hank offers to take him as a ride-along to a DEA bust. The next day, Walt faints at the car wash and is taken to a hospital; there, he is told he has inoperable lung cancer and will likely die within the next two years. During the ride-along, Hank busts a crystal meth lab, taking cook Emilio Koyama (John Koyama) into custody. Walt sees Emilio's partner fleeing the scene, and realizes it is one of his former students, Jesse Pinkman (Aaron Paul). Looking to secure his family's well-being by producing and selling meth, Walt tracks Jesse down and blackmails him into selling the meth that Walt will cook. Walt gives Jesse his life savings to buy an RV that they can use as a rolling meth lab.

After their first cook in the RV, Jesse brings a sample of the extremely pure meth to distributor Domingo "Krazy-8" Molina (Max Arciniega) and then brings Krazy-8 and the now-released Emilio to see the cook site. Emilio recognizes Walt as accompanying the DEA during the bust and believes he is an informant. Krazy-8 forces Walt to show them how he cooked such pure meth or risk being killed. Walt pretends to start a cook but instead produces toxic phosphine gas which kills Emilio and incapacitates Krazy-8. Walt and Jesse secure Krazy-8 to a structural post in Jesse's basement with a U-lock around his neck, and Walt struggles with the decision on whether to kill him. After Krazy-8 promises not to retaliate, Walt starts to unlock the lock to let Krazy-8 go but sees him reach for a broken piece of plate to stab Walt with as soon as he was freed. Walt panics and garrotes him to death with the lock. The experience shakes Walt, and he tells Jesse he will not cook meth anymore.

Walt eventually tells his family about his cancer diagnosis, and they urge him to undergo expensive chemotherapy. He initially does not want to go through the treatment, fearing that his family will remember him as a burden and a helpless invalid, much as he remembers his own father. Later he reluctantly agrees to undergo treatment but refuses Gretchen and Elliot's offer to pay for it, choosing to re-enter the drug trade with Jesse. He shaves his head to hide his chemotherapy-induced hair loss.

Dissatisfied with Jesse's slow pace of selling the meth, Walt pushes him to sell it in bulk to local drug lord Tuco Salamanca (Raymond Cruz), who has taken over Krazy-8's former territory. Discovering that Tuco stole the meth and savagely beat Jesse, Walt visits Tuco's lair with another bag of crystals, claiming to be "Heisenberg" (a reference to the theoretical physicist Werner Karl Heisenberg).[24] After Tuco mocks Jesse, refuses to pay for the bag, and implies that Walt will suffer the same fate as Jesse, Walt blows up part of the lair; the bag contained fulminated mercury, not meth. Impressed by the boldness of "Heisenberg", Tuco reluctantly agrees to pay for his meth upon delivery in the future.

Walt revels in his success and adopts the Heisenberg alias in his business dealings going forward. In order to make larger batches of meth to take advantage of their new arrangement with Tuco, Walt and Jesse switch from using pseudoephedrine to methylamine as a precursor. This tints their meth blue, which becomes a signature of Walt's product. The pair begin to fear for their lives when, after testing the purity of the meth they delivered by snorting some of it, Tuco senselessly beats to death one of his own men, No-Doze (Cesar Garcia).

Season 2
Further information: Breaking Bad (season 2)
Walt's "blue meth" becomes incredibly popular, to the point that Hank takes notice and raids Tuco's operation. A paranoid Tuco evades the bust, carjacks Jesse, and kidnaps Walt. He brings them to an isolated house in the desert, planning to take them deep into Mexico where they would be forced to cook their blue meth for the cartel. After a failed attempt to poison Tuco, they manage to escape on foot. Hank, who had been searching for Jesse, spots his car at the house and kills Tuco in a gunfight. Walt is arrested when he takes off all his clothes in a grocery store. He explains his disappearance by claiming that he had gone into a fugue state as a result of his cancer medication and simply wandered off.

Walt finds out that his cancer is in remission, and plans to leave the meth business again after selling the final 38 lb (17 kg) of meth. He hires unscrupulous criminal attorney Saul Goodman (Bob Odenkirk) to cover his involvement in the drug trade and launder his drug money. The Better Call Saul episode "Breaking Bad" expands on Walt and Saul's first meeting where Saul quickly deduces Walt is Heisenberg and urges Walt to seek higher goals with his meth business. Saul also has his cleaner, Mike Ehrmantraut(Jonathan Banks), investigate Walt's background, and despite Mike's cautions, Saul continues to support Walt.

Seeing they need a new distributor to sell the large quantity of product they have remaining, Saul arranges a meeting at a local restaurant with a mysterious meth kingpin. Jesse shows up for the meeting high on heroin, and leaves when the kingpin does not show. Walt realizes that the restaurant owner, Gus Fring (Giancarlo Esposito) was the man they were supposed to meet. Under questioning by Walt, Gus explains that he was observing the pair, and refuses to work with them because Jesse is a drug addict. However, a few days later he gives Walt a chance to prove himself by delivering all the meth to a truck stop within an hour. Walt breaks into Jesse's apartment where the meth is stored and finds him passed out with his girlfriend Jane Margolis (Krysten Ritter). Walt finds the meth and makes the delivery on time, but misses the birth of his daughter. Jane blackmails Walt into giving Jesse his share of their drug money after Walt initially refused due to Jesse's drug use.

After talking to a stranger at a bar about family – not knowing that the man is Jane's father Donald (John de Lancie) – Walt again breaks into Jesse's apartment to find the lovers passed out in a heroin stupor. Jane rolls onto her back, vomits, and begins to choke. Walt does nothing to help her and watches her die. Walt has Mike clear any connection Jesse has to Jane's death, and convinces Jesse to enter rehab.

Walt undergoes an operation to remove the remaining cancerous growth. Walt's anesthesia-induced references to a "second cell phone" – the one he uses to deal drugs – makes Skyler suspicious, leading her to uncover many of his lies and leave with their children. Just after her departure, two passenger planes collide directly above Walt's house; the accident was caused by Donald, who works as an air traffic controller and was so overcome with grief that he was not paying attention to his work. Walt watches the accident in horror, unaware that he is indirectly responsible for it.

Season 3
Further information: Breaking Bad (season 3)
Walt decides to get out of the meth business, refusing Gus' offer to produce meth in a state-of-the-art laboratory hidden under an industrial laundry for a million dollars a month. Now separated from Skyler and living in an apartment, Walt admits to her that he has been financing his treatment by cooking meth. Horrified, Skyler asks for a divorce in return for her silence and demands that Walt have nothing to do with their children.

After he discovers Jesse is cooking and selling his own version of the blue meth, Walt agrees to cook his meth for Gus. He is assisted by accomplished chemist Gale Boetticher (David Costabile) and the business begins running smoothly. Jesse continues to cook his own version of the blue meth, with Skinny Pete and Badger as his distributors, but this leads to Hank nearly catching Jesse and Walt while following a lead on an RV he believed was being used to cook meth. To avoid being discovered hiding in the RV, Walt and Jesse, aided by Saul, place a phone call to distract Hank, making him believe his wife Marie has suffered a car accident. Hank decides to leave the pursuit of the RV only to find out that Marie is fine, allowing Walt and Jesse to dispose of the vehicle. This enrages Hank enough to badly beat up Jesse at his house and send him to the hospital. Walter apologizes to Jesse for Hank’s beating while Jesse is planning to sue Hank. Walt advises him to leave the meth business for good, but Jesse tells Walt that he’ll continue to cook meth on his own. He also tells Walt that if he's caught, he would make a deal to give up Heisenberg. Fearing that any of this will derail Hank's career in law enforcement, Walt is forced to convince Gus to hire Jesse to replace Gale as his assistant, agreeing to share 50% of his earnings with Jesse. Jesse is reluctant to work with Walter again, stating that ever since they became associates, Jesse has felt more alone than ever. Walter tells Jesse that he is as good as him cooking meth. Jesse finally agrees to partner with Walt once more, to which Walt sighs in relief, even though this will cost him $1,500,000. Walter awkwardly fires Gale from the lab and gives Jesse the assistant’s job and tells Victor that the change is for the best. Victor reminds Walt that they have to meet the 200 pounds-a-week quota.

Assuming that Skyler will not turn him in to the police due to the harm it would cause to their son, Walt returns to his house. After a few attempts at bluffing him, Skyler comes to uneasily accept the situation and helps Walt launder his drug money, but refuses to have anything to do with him outside of business. The rift in their marriage worsens when Skyler sleeps with her boss, Ted Beneke (Christopher Cousins). Walt attempts to get back at her by making a pass at the principal at his school, who puts him on indefinite suspension.

Tuco's cousins Marco and Leonel Salamanca (Luis and Daniel Moncada) seek revenge against those responsible for his death and find out Walt's identity from their uncle Hector Salamanca (Mark Margolis). Believing that Walt betrayed Tuco, they go to his house and prepare to kill him with a silver axe. Gus discovers this, and to protect his investment in Walt, he convinces them to instead target Hank, who actually killed Tuco. Later, the cousins die in their attempt to take Hank's life but manage to temporarily paralyze him from the waist down. Skyler forces Walt into paying for Hank's care and creates a cover story about Walt counting cards at casinos to explain how he made his money.

Walt angers Gus by killing two of Gus' dealers in an attempt to protect Jesse, who had been planning to kill them himself for their murder of a child gang member. Gus responds by putting a hit on Jesse and re-hiring Gale as Walt's assistant, with the intention of replacing Walt as soon as possible. Walt plots to kill Gale to avoid becoming disposable, but Gus' henchman Victor lures Walt to the laundry facility, where Mike is waiting to kill him. Walt frantically calls Jesse and tells him that he is about to be killed and Jesse will have to take out Gale himself. Victor rushes to Gale's house but finds him shot dead.

Season 4
Further information: Breaking Bad (season 4)
In the aftermath of Gale's murder, Mike holds Walt at the lab to await Gus' arrival. Victor arrives with Jesse and proceeds to start the cooking process himself to show Gus that Walt and Jesse are not indispensable. Gus, however, kills Victor in front of Mike, Walt, and Jesse in a gruesome show of force. The tension of working under tighter security creates a rift between Walt and Jesse, and Gus uses the opportunity to bring Jesse to his side by having Mike train him. Walt deduces that Gus plans to eventually kill him and replace him with Jesse. He gives Jesse homemade ricin with which to poison Gus, but Jesse never goes through with it. Walt shows up at Jesse's house and tries to convince him to betray Gus, but Jesse refuses and tells Walt they are finished.

Meanwhile, Skyler buys the car wash where Walt used to work and uses it to launder his drug money. Evidence from Gale's murder leads Hank to suspect that Gus is involved in the blue meth business. With the DEA skeptical and Hank being unable to drive due to his condition, he enlists Walt's help in the investigation as a driver and tracker. Walt attempts to sabotage the investigation, but Gus blames him for drawing the attention of the authorities.

Gus rids himself of the Mexican cartel's influence in the area with the help of Mike and Jesse. He then fires Walt and threatens to kill Walt's entire family if he causes any more trouble. Walt tries to use one of Saul's connections to get him and his family relocated but finds that Skyler has used most of his drug money to pay off Ted Beneke's IRS fines to avoid having their own lives investigated, causing Walt to yell out in frustration and fear before breaking down into a maniacal laughing fit. After arranging for Saul to report that Hank was being targeted for assassination again so that his family would be protected by the DEA, Walt resolves to kill Gus.

When Brock, the son of Jesse's new girlfriend Andrea, falls desperately ill with ricin-like symptoms, Jesse attacks Walt, believing that he poisoned him. Walt manages to convince Jesse that Gus is the one responsible. After an attempt to kill Gus with a car bomb fails, Walt discovers from Saul that Gus has been visiting Tuco's uncle Hector in his nursing home, to taunt him about the cartel's defeat and the end of the Salamanca family. Walt makes a deal with Hector to draw Gus in by setting up a meeting with the DEA. When Gus comes to the nursing home to kill Hector for turning informant, Hector detonates a pipe bomb Walt made, killing himself, Gus's henchman Tyrus, and Gus. Walt rescues Jesse, who had been kept as a prisoner in the lab, and together they destroy all the evidence and torch the lab.

After Brock recovers, Jesse learns that the boy had likely been poisoned by accidentally eating lily of the valley berries, not ricin. Walt responds that killing Gus was still the right thing to do. Walt calls Skyler to tell her they are safe and that he has "won", as the camera pans to a potted Lily of the Valley plant next to Walt's pool, indicating that Walt had in fact poisoned Brock to goad Jesse into action.

Season 5
Main article: Breaking Bad (season 5)
Mike intends to kill Walt in retaliation for Gus' death, but Jesse intervenes and convinces the two men to work together to eliminate their connection to the destroyed lab. The three eventually start a new meth production system with the help of a corrupt pest control company, using residents' homes to cook meth while they are fumigated, using methylamine provided by Lydia Rodarte-Quayle (Laura Fraser), a representative for the conglomerate that owned Gus's chicken franchise. When her supply is discovered to be tracked by the police, she leaks them information on a train carrying the chemical so they can plan a robbery. The robbery is successful, but Todd Alquist (Jesse Plemons), one of the pest control workers, kills a young boy who had seen them. Horrified, Jesse and Mike resolve to leave the business. A Phoenix drug lord named Declan offers to buy out the operation for $15 million in order to remove his competition. Walt convinces him to pay off Jesse and Mike and begin distributing Walt's meth instead.

Hank connects Mike to the blue meth and begins pressing several of his associates, who are now in prison, to give information on the blue meth operation. When Walt delivers Mike's share of Declan's payment, Mike refuses to reveal these prisoners' identities and insults Walt, blaming him for all the problems they've encountered; Walt shoots him dead in a fit of rage. Obtaining a list of the prisoners from Lydia, he enlists Todd's uncle Jack (Michael Bowen), a criminal with ties to the Aryan Brotherhood prison gang, to kill the nine men simultaneously at multiple prisons to prevent the DEA from realizing that they were being targeted until it was too late.

After a few months, Walt has earned more than $80 million from meth, and Skyler convinces him to stop. Walter leaves the meth business, and the kids return home. During a family barbecue, Hank finds a copy of Walt Whitman's Leaves of Grass in the bathroom, the same copy given to Walt by Gale; upon reading Gale's handwritten inscription referring to Walt as "the other W.W." Hank realizes that Walt is the drug lord he has been pursuing. Enraged, Hank accuses Walt of being Heisenberg, which a stunned Walt neither confirms nor denies. Walt says that his cancer is back and he will likely be dead in six months, making an arrest pointless. He also tells Hank how 'He will never see the inside of a prison cell'. Hank says they can talk if Walt gives up his children, but Walt refuses and tells Hank to "tread lightly". Walt eventually forces Hank to remain silent by crafting a fake confessional videotape in which he states that Hank is Heisenberg.

Walt buries his money in seven barrels on the Tohajiilee Indian Reservation and convinces Jesse to go into a relocation program. While waiting to be picked up, Jesse figures out that Walt poisoned Brock. Hank approaches Jesse and offers to help bring down Walt. With Hank's help, Jesse lures Walt into a trap by claiming to have found his money. Walt makes arrangements with Jack and his men to kill Jesse, in exchange for promising to help teach Todd how to cook meth. When Walt realizes Jesse is with Hank, he tries to call off the deal to protect Hank but is subdued by Hank and his DEA partner Steven Gomez (Steven Michael Quezada). Just then, Jack and his men arrive and fire on the group, killing Gomez and wounding Hank; Jack then executes Hank, despite Walt pleading for his brother-in-law's life. Jack's men take all but one barrel of Walt's money and abduct Jesse; as Jesse is taken away, Walt spitefully tells him that he watched Jane die.

Walt tries to persuade Skyler and Walter Jr. to go on the run with him, but they refuse. He kidnaps Holly, but has a moment of conscience and leaves her to be found and returned. He calls Skyler, knowing that the police are listening in, and berates her for failing to follow his orders, as a way of clearing her of involvement in his crimes. Walt then goes into hiding, along with Saul, waiting for Ed the disappearer to set up a new identity for Walt. A scene in the final Better Call Saul episode "Saul Gone" shows Walt accusing Saul of always being a con artist and having no trust in him anymore. Eventually, Ed helps to set up Walt to live in isolation in New Hampshire.

After several months alone, Walt goes to a local bar, where he calls Walter Jr. and tries to give him money. Walter Jr. angrily rejects the gesture, however, and hangs up. Feeling hopeless, Walt calls the DEA and gives himself up. As he waits for them, however, he sees Gretchen and Elliott on Charlie Rose downplaying his contributions to Gray Matter and resolves to return to Albuquerque to put things right.

When Walter arrives in Albuquerque – on his 52nd birthday – he confronts Gretchen and Elliott at their home and coerces them into putting his remaining money into a trust fund for Walter Jr. He then visits Skyler and provides her with the location of Hank and Steve's unmarked grave which he suggests she use to barter for a deal with the prosecutor, and finally admits to her that he entered the meth business for himself, not his family. As a token of appreciation, Skyler lets him see his daughter, Holly, one last time. He then arranges to see Lydia, surreptitiously poisoning her drink with ricin after learning where Jack has taken Jesse. Walt drives to Jack's compound and demands to see Jesse. When they bring Jesse, who has been chained up in a lab and forced to cook meth since his abduction, Walt dives atop him and knocks them both to the ground. Now out of range, he activates a remote machine gun mounted in his car that injures Jack and kills all of his men except for Todd. Jesse strangles Todd with a chain, killing him. Noticing Jack is still alive, Walt picks up a pistol and aims it at him. Jack pleads with Walt to let him live, offering him extremely large amounts of money. Jack's pleas fall on deaf ears, and Walt executes him with a shot to the face. Walt then asks Jesse to kill him, but Jesse tells him to do it himself. Walt then finds that he has been wounded by a ricocheted bullet. He answers a call from Lydia on Todd's phone and coldly informs her that she is going to die as a result of the poisoned drink she consumed. He exchanges a knowing nod with Jesse, who escapes the compound. Walt calmly walks around Jack's lab and admires all the equipment that Jesse had been using. He notices on a dial that Jesse has cooked a perfect batch of his product, and smiles to himself. As the police arrive, Walt collapses to the floor and dies with a look of contentedness on his face, fulfilling his comment to Hank that he will never see the inside of a prison cell.

El Camino
Further information: El Camino: A Breaking Bad Movie
Cranston reprises his role in the movie El Camino: A Breaking Bad Movie in a flashback scene, taking place during the events of the episode "4 Days Out" from the show's second season. Walt and Jesse are sitting down at a buffet breakfast talking about how they are going to move a batch of recently cooked meth. Walt asks Jesse what he would like to study if he went to college and encourages Jesse to find a life outside of cooking meth in the future. He suggests that Jesse should study business and marketing, remarking that Jesse is a natural at it and that he "could practically teach the class" himself using his vast knowledge. Afterward, Walt tells Jesse: "You're really lucky, you know that? You didn't have to wait your whole life to do something special."

In the present, Jesse, Skinny Pete, and Badger see various news reports on the aftermath of Walt's massacre. In a news report Jesse listens to, Walt is confirmed to be dead with the same report mentioning an investigation of a Houston woman poisoned by Walt – presumably Lydia – who is in critical condition and not expected to survive.

Post Breaking Bad
See also: Breaking Bad (Better Call Saul)
Walt is briefly mentioned in passing by Saul Goodman (now going by the alias Gene Takavic) as he attempts to explain to Jeff how crazy his life had become and how much money he could get by getting into "the game".

Francesca Liddy later tells Saul that Walt's death only made things worse for the surviving low-level players connected to his meth empire rather than better. As Walt had hoped, Skyler had succeeded in getting a deal with the federal prosecutors and the DEA was ultimately forced to release Huell Babineaux, leaving only Jesse and Saul left for them to go after. Although Jesse has successfully managed to escape to Alaska while tricking the public into thinking he fled to Mexico, the DEA has seized all of Saul's assets and is even following Francesca in an attempt to find him. Francesca admits that she doesn't know what's become of Patrick Kuby, another one of Walt's associates and she does not answer Saul's questions about Ira and Danny.

Saul is eventually discovered and taken by DEA agents. During their initial questioning, they bring in Marie, who is bitter at Saul for enabling Walter and leading to Hank's death. Saul shrewdly asserts he was also manipulated by Walt to goad the agent to start a plea bargain for a significantly reduced sentence until Saul learns that his involvement with Howard Hamlin's death was already given to them by Kim Wexler.

Reception
Critical response
The character development of Walter White, as well as Bryan Cranston's performance, has received universal acclaim, from both critics and audiences. Walter White is considered to be one of the greatest and most iconic characters in television history.[25][26][27]

From TheGuardian.com, Paul MacInnes lauded Walter White's character as a whole, noting his quick transformation into becoming Heisenberg.[28] From the same website, Rebecca Nicholson wrote about Walt's death, praising the fact that instead of facing the consequences, "Walter dies happy. He doesn't only get what he deserved; he gets what he wanted. It's the same for us viewers: we get the neatness and the uncertainty, which shows a Heisenberg level of mastery."[29] In their list for the "Top 100 Villains", IGN ranked Walt as #12, stating that "Walter White is selfishness incarnate, and perhaps one of the greatest tragic figures to ever grace television, making his ultimate descent into villainy that much more compelling."[30]

The web magazine Grantland quotes Andy Greenwald as analyzing Walter White differently from some others, including Vince Gilligan. Greenwald states:

I've been thinking a lot about Walter White, the 'shadow' on his recent CAT scan, and the black cloud that has long since overtaken his heart. The closer we get to the end, the more Walt scrabbles around and lashes out like a rat when it's surrounded, the less I'm buying Vince Gilligan's whole 'Mr. Chips to Scarface' quote as an analogy for Walt's transformation... But I think the most horrifying part of Breaking Bad may be that Walt, at his core, didn't really transform at all. It wasn't greed or generosity or cancer or fear that fueled this reign of death and destruction. It was resentment. Every moment Walt spent in front of a classroom he was thinking about how beneath him it all was. He was a genius; he was meant to be a millionaire, not this castrated cross between stepping stone and doormat. When you got down to it, Walt desperately wanted to teach everyone a lesson, and I don't mean in the style of Mr. Chips.[31]

Similarly, Scott Meslow wrote in The Atlantic that Walt's capacity for villainy was present well before the series even began, and that cancer was only the catalyst, stating that "all the elements that have since turned him into a monster were already in place."[32] New York magazine writer Emma Rosenblum said Bryan Cranston "pulls off the unassuming White with flawless subtlety: a waxy pallor, a slump of the shoulders, and a sense of doom that is palpable".[7] The Hollywood Reporter writer Tim Goodman praised as courageous Vince Gilligan's decision to transform Walter White into an unsympathetic character: "You don't take your main character and make him unlikable. You just don't. Nobody does that. Nobody has ever really done that to this extent."[33] Robert Bianco of USA Today called Walt "one of the greatest dramatic creations ever to grace our TV screens".[34] In 2011, The New York Times named Cranston as one of the "eight actors who turn television into art".[35] Following the show's conclusion, actor Anthony Hopkins wrote a fan letter to Cranston, in which he praised the show and called Cranston's performance as Walter White the best acting he had ever seen.[36]

Accolades
Further information: List of awards and nominations received by Breaking Bad

Bryan Cranston accepting the Peabody Award for Breaking Bad at the 73rd Annual Peabody Awards
Cranston has received various awards and nominations for his performance as Walter White. For the first three seasons, he won the Primetime Emmy Award for Outstanding Lead Actor in a Drama Series thrice consecutively, becoming the first actor to accomplish this feat since Bill Cosby for I Spy.[37] Cranston was also nominated in 2012 and 2013 for season four and the first half of season five, but lost out to Damian Lewis for Homeland and Jeff Daniels for The Newsroom, respectively. He also won his fourth Primetime Emmy Award for Outstanding Lead Actor in a Drama Series, at the 66th Primetime Emmy Awards.[38][39]

At the annual Golden Globe Awards, Cranston has been nominated for the Best Actor – Television Series Drama accolade on four occasions for his role in Breaking Bad, in 2011, 2012, 2013 and 2014, winning in 2014 for the second half of season five.[40] At the Screen Actors Guild Awards, Cranston has been nominated for Male Actor in a Drama Series five times, in 2010, 2011, 2012, 2013 and 2014, winning in 2013 and 2014, for both parts of season five. Additionally, Cranston has been nominated with the rest of the cast for Performance by an Ensemble in a Drama Series, in 2012, 2013 and 2014, winning only in 2014.[41]

In addition, Cranston has won the Satellite Award for Best Actor: Drama Series three times consecutively, in 2008, 2009 and 2010, for seasons one, two and three, and has been nominated in 2011, 2012 and 2014 for seasons four and five. He won the TCA Award for Individual Achievement in Drama in 2009, and was nominated in 2010, 2012 and 2013; was nominated twice for the Prism Award for Best Performance in a Drama Series Multi-Episode Storyline; won two Saturn Awards for Best Actor on Television in 2012 and 2013 (tying with Kevin Bacon for The Following on the latter occasion), and was nominated in 2009, 2010 and 2011; and won the Golden Nymph Award for Outstanding Actor in a Drama Series in 2013.[41]

Legacy
Cult following

A Walter White graffiti in Carrer d'Antoni Suárez, Valencia, Spain

Heisenberg graffiti in Ano Patisia, Athens, Greece
Over time Walter White developed a cult following, spawning fan websites like "Heisenberg Labs", "Walt's Wardrobe", and "Save Walter White" (an exact replica of the website Walter White's son creates in the series to raise money to pay for his father's cancer treatments).[42] In 2015, series creator Vince Gilligan publicly requested fans of the series to stop reenacting a scene in which Walt angrily throws a pizza on his roof after Skyler refuses to let him inside; this came after complaints from the home's real-life owner.[43][44] Cranston reprised his role of the character in a commercial for Esurance which aired during Super Bowl XLIX, one week before the premiere of Breaking Bad spin-off Better Call Saul.[45] In December 2016, Bryan cameoed as White in an episode of Saturday Night Live in the cold open. The skit had White on a CNN broadcast where he is the front runner for Donald Trump’s cabinet nominee for the Drug Enforcement Administration.[46] In the Spanish-language remake of Breaking Bad, titled Metástasis, his character is renamed Walter Blanco (blanco being the Spanish translation of white) and is portrayed by Diego Trujillo.[47]

Albuquerque statues
Bronze statues of White and Jesse Pinkman were commissioned and donated by creator Vince Gilligan and Sony Television Pictures to the city of Albuquerque in July 2022, which will be housed in the Albuquerque Convention Center.[48] They were made by former sculptor Trevor Grove.[49]

Obituary and funeral
A Breaking Bad fan group placed a paid obituary for Walter White in the Albuquerque Journal on October 4, 2013.[50] On October 19, 2013, actor Jackamoe Buzzell organized a mock funeral procession (including a hearse and a replica of Walt's meth lab RV) and service for the character was held at Albuquerque's Sunset Memorial Park cemetery. A headstone was placed with a photo of Cranston as Walt, located on an outside wall in Los Ranchos de Albuquerque, New Mexico. While some residents were unhappy with the makeshift grave-site for closure with the show, tickets for the event raised over $30,000 for a local charity called Albuquerque Healthcare for the Homeless.[51][52]

Alternative theory concerning death
Many fans of Breaking Bad, including actor Norm Macdonald and New Yorker magazine writer Emily Nussbaum,[53] proposed a theory, in which most of the series finale happened in Walt's mind, and he really died in the stolen Volvo in the beginning of it.[54] While Nussbaum merely stated that it would be her preferred ending,[55] Macdonald emphasized the seemingly unreal scenarios of Walt's final day, as well as what he deemed as unreliable acting.[56] However, series creator Vince Gilligan debunked this theory, explaining that Walt could not possibly have known several things that happened, like Jesse being held in captivity by Jack's gang instead of being murdered by them, or that Todd had begun taking meetings with Lydia regarding the meth trade.[57] This theory was further disproven with Better Call Saul following Saul’s story before and after Breaking Bad alongside El Camino: A Breaking Bad Movie following Jesse's story after the finale, in which White is confirmed to have died.[58][59]

---
## [RaveRadbury/tgstation](https://github.com/RaveRadbury/tgstation)@[e75283dee3...](https://github.com/RaveRadbury/tgstation/commit/e75283dee3776577f70d792e0874dcaecb6c93e3)
#### Thursday 2022-10-13 22:38:25 by vincentiusvin

Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff (#69158)


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

---
## [RaveRadbury/tgstation](https://github.com/RaveRadbury/tgstation)@[aab43918f8...](https://github.com/RaveRadbury/tgstation/commit/aab43918f8dca1a09f67effc786eb46bda592d22)
#### Thursday 2022-10-13 22:38:25 by LemonInTheDark

Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) (#69376)


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

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[640faa31d0...](https://github.com/Offroaders123/Smart-Text-Editor/commit/640faa31d081fbf8e571004f921e0f8074203678)
#### Thursday 2022-10-13 23:19:05 by Offroaders123

2nd Birthday for STE + Shortcut Icon Updates + Maskable Exports

Announcements: -- first time for this category? :0 --
- Smart Text Editor turned 2 years old on the 24th!!! This has been a crazy journey, and I never saw it coming. I'd say this is my first full programming project, aside from my Minecraft resource packs (this seems more programming-y to me, hehe). I love this project just as much as 2 years ago, and I may have less updates to it as time goes on, but that's because it's getting even closer to what I imagine it to be! I have a few more ideas to be named that I'd love to see in the app, and I will continue towards adding those as I go. I am about to start my next set of programming classes at my college this coming semester, and I can't wait! I started Smart Text Editor during my first proper programming class in high school, and it has been steadily improving all the way to now! I am actually using STE on my Chromebook to write this right now, and push this update through the Git CLI using Crostini Linux. Crazy to think that is possible now. PWA functionality from the modern browsers have certainly helped with that. On that note, off to the regular changelog, haha! Thanks for reading this and having interest in the project, whoever you are. Maybe you are in the future, mysterious...

Additions:
- Expanded the Maskable App Icon images to include all three standard resolutions. Usually this includes 192x, 512x, and 1024x (The last one is a standard I am adding for myself, might as well have an ultra-clear one just in case. It looks nice too :) Commonly 192x and 512x will do just fine for a PWA). In the case of the App Maskable Icons, I hadn't made a 192x version, only 512x and 1024x. Might as well add consistency there if I am doing it for the other icons too!

Changes:
- Adjusted the size and scale of the sprites used in the Shortcut Icon images. They weren't quite the same size as the icon canvas, so I made them a little larger using Figma. Much easier than when I made them using Google Draw a year ago, haha!
- Updated the sprites fill colors, as they were using the old #aaaaaa text color for STE. Modern STE text uses #cccccc now, it's a little brighter. Must've been an oversite I missed during The Big Refactor last year when the app color palette changed a little bit.
- Fixed the clipping issue that was occurring on Chrome OS for the PWA shortcuts icons, as Chrome OS appears to prefer to use a maskable image for the shortcut option. Originally I thought the shortcut icons didn't need the same icon-type variations as the app icons require, but they do. Makes sense!
- Alongside the last note, each of these icons now have all 3 scale types, 192x, 512x, 1024x. Before I only used the base SVG shortcut icon and a 192x export, and now I use the base SVG, 192x, 512x, 1024x, and maskable variants of those with the same export sizes. So, from 2 icons to 7 for each shortcut. Maybe overboard, but why not! Figma makes things really easy for me :]

Removals:
- Removed the SVG Smart Text Editor logo image, as it requires the use of an `@import` CSS call to load the logo font, and these don't work unless the image is running in the direct source of the page, as inline SVG. I have the option to keep the image, and save the logo words as SVG `<path>` tags instead of plain text, but I haven't used the image for anything yet, so might as well work on something else more needed for my fixing.

Happy 2nd Birthday Smart Text Editor, can't wait to see where you go over more years to come!

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[91f02f2a6b...](https://github.com/LemonInTheDark/tgstation/commit/91f02f2a6b99c6eb5ae56fc3f7cfb903e703bc08)
#### Thursday 2022-10-13 23:36:04 by John Willard

canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

---

