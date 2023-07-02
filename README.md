## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-01](docs/good-messages/2023/2023-07-01.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,684,931 were push events containing 2,552,749 commit messages that amount to 174,686,951 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 42 messages:


## [leanprover-community/mathlib4](https://github.com/leanprover-community/mathlib4)@[719a21701d...](https://github.com/leanprover-community/mathlib4/commit/719a21701d48cc284d79469cd45ad8d9a4ff3ec9)
#### Saturday 2023-07-01 01:10:12 by Scott Morrison

chore: reorder universe variables in `Cardinal.lift_le` and `Cardinal.lift_mk_le` (#5325)

`Cardinal.lift_le` and `Cardinal.lift_mk_le` have their universes out of order, in the sense that persistently through the rest of the library we need to specify the 2nd universe (resp 3rd), while the others are solved by unification.

This PR reorders the universes so it's easier to specify the thing you need to specify!

(This PR doesn't get rid of all the occurrences of `\.\{_,` in the library, but I'd like to do that later.)

I do have a hidden agenda here, which is that I've been experimenting with solutions to the dreaded "Can't solve `max u v = max v ?u`" universe unification issue (which is making life hellish forward porting https://github.com/leanprover-community/mathlib/pull/19153), and my favourite (but still hacky) solution doesn't like some of the occasions where we reference a lemma filling in some of its universe arguments with `_` but then fully specify a later one. (e.g. `rw [← lift_le.{_, max u v}, lift_lift, lift_mk_le.{_, _, v}]` in `ModelTheory/Skolem.lean`). Hence the cleanup proposed in this PR makes my life easier working on these experiments. :-)



Co-authored-by: Scott Morrison <scott.morrison@gmail.com>

---
## [Imaginos16/Shiptest](https://github.com/Imaginos16/Shiptest)@[18819cc7fb...](https://github.com/Imaginos16/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Saturday 2023-07-01 01:40:04 by zevo

Minor changes to the Syndicate Battle Sphere ruin (#2045)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Various fixes for provinggrounds.dmm, mainly the server room and SMES.
Server room is no longer filled with black box recorders, but salvagable
servers. There is now one singular black box recorder in the center
where a black box on a table was. The SMES now should actually charge
the ruin. Tossed a medkit in one of the halls for players to use while
clearing the ruin. Replaced about half of the syndicate researcher mobs
with syndicate operatives who will actually fight the players. Rotated
an airlock missed in the map updates for anywalls.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
boy, i sure love functional ruins! also players should not have 25 of a
very rare potential quest item. The ruin can stay as it is otherwise,
because it provides a fun challenge for superbly well armed players (or
a rugged explorer with nothing but a lazer gun and a dream) with a
fitting reward at the end of a mounted LMG.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Syndicate Battle Dome (provinggrounds.dmm) should now have a
functional SMES and airlocks/blast doors.
fix: Syndicate Battle Dome (provinggrounds.dmm) no longer has ~20 black
box recorders and now only has one.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Imaginos16/Shiptest](https://github.com/Imaginos16/Shiptest)@[0e6f7fa646...](https://github.com/Imaginos16/Shiptest/commit/0e6f7fa64649dfbf52b8e4b71756e6625e50fdd0)
#### Saturday 2023-07-01 01:40:04 by Imaginos16

TileTest Part 1: Big Sweeping Changes! (#2054)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## !! WARNING !!
This is a multi-parter PR. Due to the fact that tiles here on shiptest
are an unholy amalgam of decals, greyscale sprites and multiple
spread-out files, things are *bound* to look weird. If they do, feel
free to report it and it will be addressed in future PRs.

## About The Pull Request

This PR finally accomplishes the promise I made to @triplezeta a year
ago, creating a unique tileset for the server that people may enjoy!

To put every single microscopic change I have made would take forever,
so I will instead provide a series of screenshots of it in action!


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/00e9cec0-335a-4367-90f9-1adc572595f3)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/497310ab-fe06-4b31-8774-70e79338a7d8)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/80991d0b-c48b-404b-b4a6-cbb1c4c6af3a)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc06d43e-3873-499e-aa12-51a0d7a37c98)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Utilizing an unique, modernized tileset for our server to differentiate
from our competitors is something that has been requested, and I was
more than happy to lend my hand to make it a reality!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
del: Removes several unused floor types, as well as completely
annihilating the "monofloor" and "dirty" floor types, and the "edge"
decal type.
imageadd: Redoes the floors using the TileTest tileset!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [DarkLordikss/Gamedev](https://github.com/DarkLordikss/Gamedev)@[c30b2038d1...](https://github.com/DarkLordikss/Gamedev/commit/c30b2038d1f09dfc17b5bdae1a4a30abbc104849)
#### Saturday 2023-07-01 02:14:27 by Ivan Dolgun

CANALIZATION

you can eat poo now oh may god bro, damn son, wow magic

---
## [NetBSD/src](https://github.com/NetBSD/src)@[a681d7f6b8...](https://github.com/NetBSD/src/commit/a681d7f6b89654d0d44d03f5b49e1eab83f4019f)
#### Saturday 2023-07-01 02:16:24 by riastradh

entropy(9): Reintroduce netbsd<=9 time-delta estimator for unblocking.

The system will (in a subsequent change) by default block for this
condition before almost all of userland is running (including
/etc/rc.d/sshd key generation).  That way, a never-blocking
getentropy(3) API will never return any data without at least
best-effort entropy like netbsd<=9 did to applications except in
single-user mode (where you have to be careful about everything
anyway) or in the few processes that run before a seed can even be
loaded (where blocking indefinitely, e.g. when generating a stack
protector cookie in libc, could pose a severe availability problem
that can't be configured away, but where the security impact is low).

However, (in another subsequent change) we will continue to use
_only_ HWRNG driver estimates and seed estimates, and _not_
time-delta estimator, for _warning_ about security in motd, daily
security report, etc.  And if HWRNG/seed provides enough entropy
before time-delta estimator does, that will unblock /dev/random too.

The result is:

- Machines with HWRNG or seed won't warn about entropy and will
  essentially never block -- even on first boot without a seed, it
  will take only as long as the fastest HWRNG to unblock.

- Machines with neither HWRNG nor seed:
  . will warn about entropy, giving feedback about security;
    and
  . will avoid returning anything more predictable than netbsd<=9;
    but
  . won't block (much) longer than netbsd<=9 would (and won't block
    again after blocking once, except with kern.entropy.depletion=1 for
    testing).

  (The threshold for unblocking is now somewhat higher than before:
  512 samples that pass the time-delta estimator, rather than 80 as
  it used to be.)

  And, of course, adding a seed (or HWRNG) will prevent both warnings
  and blocking.

The mechanism is:

1. /dev/random will block until _either_

   (a) enough bits of entropy (256) from reliable sources have been
       added to the pool, _or_

   (b) enough samples have been added from any sources (512), passing
       the old time-delta entropy estimator, that the possible
       security benefit doesn't justify holding up availability any
       longer (`best effort'), except on systems with higher security
       requirements like securelevel=2 which can disable non-HWRNG,
       non-seed sources with rndctl_flags in rc.conf(5).

2. dmesg will report `entropy: ready' when 1(a) is satisfied, but if
   1(b) is satisfied first, it will report `entropy: best effort', so
   the concise log messages will reflect the timing and whether in
   any period of time any of the system might be relying on best
   effort entropy.

3. The sysctl knob kern.entropy.needed (and the ioctl RNDGETPOOLSTAT
   variable rndpoolstat_t::added) still reflects the number of bits
   of entropy from reliable sources, so we can still use this to
   suggest regenerating ssh keys.

   This matters on platforms that can only be reached, after flashing
   an installation image, by sshing in over a (private) network, like
   small network appliances or remote virtual machines without
   (interactive) serial consoles.  If we blocked indefinitely at boot
   when generating ssh keys, such platforms would be unusable.  This
   way, platforms are usable, but operators can still be advised at
   login time to regenerate keys as soon as they can actually load
   entropy onto the system, e.g. with rndctl(8) on a seed file copied
   from a local machine over the (private) network.

4. On machines without HWRNG, using a seed file still suppresses
   warnings for users who need more confident security.  But it is no
   longer necessary for availability.

This is a compromise between availability and security:

- The security mechanism of blocking indefinitely on machines without
  HWRNG hurts availability too much, as painful experience over the
  multiple years since I made the mistake of introducing it have
  shown.  (Sorry!)

- The other main alternative, not having a blocking path at all (as I
  pushed for, and as OpenBSD has done for a long time) could
  potentially reduce security vs netbsd<=9, and would run against the
  expectations set by many popular operating systems to the severe
  detriment of public perception of NetBSD security.

Even though we can't _confidently_ assess enough entropy from, e.g.,
sampling interrupt timings, this is the traditional behaviour that
most operating systems provide -- and the result here is a net
nondecrease in security over netbsd<=9, because all paths from the
entropy pool to userland now have at least as high a standard before
returning data as they did in netbsd<=9.

PR kern/55641
PR pkg/55847
PR kern/57185
https://mail-index.netbsd.org/current-users/2020/09/02/msg039470.html
https://mail-index.netbsd.org/current-users/2020/11/21/msg039931.html
https://mail-index.netbsd.org/current-users/2020/12/05/msg040019.html

XXX pullup-10

---
## [einstein95/mame](https://github.com/einstein95/mame)@[2bcd9bc772...](https://github.com/einstein95/mame/commit/2bcd9bc772b4f3cc6e8b281703e53561d2c5bea9)
#### Saturday 2023-07-01 02:44:50 by David 'Foxhack' Silva

segacd.xml, megacdj.xml: Added various CD dumps. (#11344)

New working software list items
-------------------------------
segacd.xml:
Compton's Interactive Encyclopedia v2.00S (USA) [redump.org]
Note! Color Mechanica (USA) [redump.org]
Note! Color Mechanica (USA, alt) [redump.org]
What is X'Eye Multi Entertainment System (USA) [redump.org]
megacdj.xml:
Heavenly Symphony - Formula One World Championship 1993 Hibaihin (Japan) [redump.org]
Keiou Yuugekitai Taikenban Hibaihin (Japan) [redump.org]
Lunar - Eternal Blue Hibaihin Auto Demo (Japan) [redump.org]
Microcosm Demo CD (Japan) [redump.org]
Night Trap Hibaihin (Japan) [redump.org]
Popful Mail Taikenban Hibaihin (Japan) [redump.org]
Silpheed Hibaihin (Japan) (Fixed) [redump.org]
Sonic The Hedgehog CD Hibaihin (Japan) [redump.org]
Thunderhawk Hibaihin (Japan) [redump.org]
Urusei Yatsura - Dear My Friends Hibaihin (Japan) [redump.org]
Yumemi Yakata no Monogatari Hibaihin (Japan) [redump.org]
WonderMega Collection - Game Garden (Japan, alt) [redump.org]

New software list items marked not working
------------------------------------------
segacd.xml:
Surgical Strike (Brazil, 32X) [redump.org]
megacdj.xml:
Psychic Detective Series vol.3 - AYA Auto Demo (Japan) [redump.org]
Silpheed Hibaihin (Japan) [redump.org]

---
## [ColtOS-beta/platform_bionic](https://github.com/ColtOS-beta/platform_bionic)@[a1381a71a9...](https://github.com/ColtOS-beta/platform_bionic/commit/a1381a71a942bb644c1eb5b9ad925e299ae15609)
#### Saturday 2023-07-01 04:51:03 by Elliott Hughes

Add %b and %B support to the scanf/wscanf and strto*/wcsto* families.

Coming to C23 via WG14 N2630.

This one is a little interesting, because it actually changes existing
behavior. Previously "0b101" would be parsed as "0", "b", "101" by these
functions. I'm led to believe that glibc plans to actually have separate
versions of these functions for C23 and pre-C23, so callers can have the
behavior they (implicitly) specify by virtue of which -std= they compile
with. Android has never really done anything like that, and I'm pretty
sure app developers have more than enough to worry about with API levels
without having to deal with the cartesian product of API level and C
standard.

Therefore, my plan A is "if you're running on Android >= U, you get C23
behavior". My plan B in the (I think unlikely) event that that actually
causes trouble for anyone is "if you're _targeting_ Android >= U, you
get C23 behavior". I don't think we'd actually want to have two versions
of each of these functions under any circumstances --- that seems by far
the most confusing option.

Test: treehugger
Change-Id: I0bbb30315d3fabd306905ad1484361f5d8745935

---
## [log1cs/kernel_nokia_msm8998](https://github.com/log1cs/kernel_nokia_msm8998)@[913870e6a0...](https://github.com/log1cs/kernel_nokia_msm8998/commit/913870e6a08b069c8ff8d1c4f9146bcdaa69b4ec)
#### Saturday 2023-07-01 05:07:43 by Vasily Averin

mm, oom: pagefault_out_of_memory: don't force global OOM for dying tasks

commit 0b28179a6138a5edd9d82ad2687c05b3773c387b upstream.

Patch series "memcg: prohibit unconditional exceeding the limit of dying tasks", v3.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It can be misused and allowed to trigger global OOM from inside
a memcg-limited container.  On the other hand if memcg fails allocation,
called from inside #PF handler it triggers global OOM from inside
pagefault_out_of_memory().

To prevent these problems this patchset:
 (a) removes execution of out_of_memory() from
     pagefault_out_of_memory(), becasue nobody can explain why it is
     necessary.
 (b) allow memcg to fail allocation of dying/killed tasks.

This patch (of 3):

Any allocation failure during the #PF path will return with VM_FAULT_OOM
which in turn results in pagefault_out_of_memory which in turn executes
out_out_memory() and can kill a random task.

An allocation might fail when the current task is the oom victim and
there are no memory reserves left.  The OOM killer is already handled at
the page allocator level for the global OOM and at the charging level
for the memcg one.  Both have much more information about the scope of
allocation/charge request.  This means that either the OOM killer has
been invoked properly and didn't lead to the allocation success or it
has been skipped because it couldn't have been invoked.  In both cases
triggering it from here is pointless and even harmful.

It makes much more sense to let the killed task die rather than to wake
up an eternally hungry oom-killer and send him to choose a fatter victim
for breakfast.

Link: https://lkml.kernel.org/r/0828a149-786e-7c06-b70a-52d086818ea3@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Roman Gushchin <guro@fb.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [openeuler-mirror/Intel-kernel](https://github.com/openeuler-mirror/Intel-kernel)@[52e5df72c5...](https://github.com/openeuler-mirror/Intel-kernel/commit/52e5df72c58e1c804c57cbcdfe37dc9c0a4f846d)
#### Saturday 2023-07-01 06:26:31 by Dave Hansen

mm/mempolicy: add MPOL_PREFERRED_MANY for multiple preferred nodes

mainline inclusion
from mainline-v5.15-rc1
commit b27abaccf8e8b012f126da0c2a1ab32723ec8b9f
category: feature
bugzilla: https://gitee.com/openeuler/kernel/issues/I6I1Z2
CVE: NA

Reference: https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=b27abaccf8e8b012f126da0c2a1ab32723ec8b9f

--------------------------------

Patch series "Introduce multi-preference mempolicy", v7.

This patch series introduces the concept of the MPOL_PREFERRED_MANY
mempolicy.  This mempolicy mode can be used with either the
set_mempolicy(2) or mbind(2) interfaces.  Like the MPOL_PREFERRED
interface, it allows an application to set a preference for nodes which
will fulfil memory allocation requests.  Unlike the MPOL_PREFERRED mode,
it takes a set of nodes.  Like the MPOL_BIND interface, it works over a
set of nodes.  Unlike MPOL_BIND, it will not cause a SIGSEGV or invoke the
OOM killer if those preferred nodes are not available.

Along with these patches are patches for libnuma, numactl, numademo, and
memhog.  They still need some polish, but can be found here:
https://gitlab.com/bwidawsk/numactl/-/tree/prefer-many It allows new
usage: `numactl -P 0,3,4`

The goal of the new mode is to enable some use-cases when using tiered memory
usage models which I've lovingly named.

1a. The Hare - The interconnect is fast enough to meet bandwidth and
    latency requirements allowing preference to be given to all nodes with
    "fast" memory.
1b. The Indiscriminate Hare - An application knows it wants fast
    memory (or perhaps slow memory), but doesn't care which node it runs
    on.  The application can prefer a set of nodes and then xpu bind to
    the local node (cpu, accelerator, etc).  This reverses the nodes are
    chosen today where the kernel attempts to use local memory to the CPU
    whenever possible.  This will attempt to use the local accelerator to
    the memory.
2.  The Tortoise - The administrator (or the application itself) is
    aware it only needs slow memory, and so can prefer that.

Much of this is almost achievable with the bind interface, but the bind
interface suffers from an inability to fallback to another set of nodes if
binding fails to all nodes in the nodemask.

Like MPOL_BIND a nodemask is given. Inherently this removes ordering from the
preference.

> /* Set first two nodes as preferred in an 8 node system. */
> const unsigned long nodes = 0x3
> set_mempolicy(MPOL_PREFER_MANY, &nodes, 8);

> /* Mimic interleave policy, but have fallback *.
> const unsigned long nodes = 0xaa
> set_mempolicy(MPOL_PREFER_MANY, &nodes, 8);

Some internal discussion took place around the interface. There are two
alternatives which we have discussed, plus one I stuck in:

1. Ordered list of nodes.  Currently it's believed that the added
   complexity is nod needed for expected usecases.
2. A flag for bind to allow falling back to other nodes.  This
   confuses the notion of binding and is less flexible than the current
   solution.
3. Create flags or new modes that helps with some ordering.  This
   offers both a friendlier API as well as a solution for more customized
   usage.  It's unknown if it's worth the complexity to support this.
   Here is sample code for how this might work:

> // Prefer specific nodes for some something wacky
> set_mempolicy(MPOL_PREFER_MANY, 0x17c, 1024);
>
> // Default
> set_mempolicy(MPOL_PREFER_MANY | MPOL_F_PREFER_ORDER_SOCKET, NULL, 0);
> // which is the same as
> set_mempolicy(MPOL_DEFAULT, NULL, 0);
>
> // The Hare
> set_mempolicy(MPOL_PREFER_MANY | MPOL_F_PREFER_ORDER_TYPE, NULL, 0);
>
> // The Tortoise
> set_mempolicy(MPOL_PREFER_MANY | MPOL_F_PREFER_ORDER_TYPE_REV, NULL, 0);
>
> // Prefer the fast memory of the first two sockets
> set_mempolicy(MPOL_PREFER_MANY | MPOL_F_PREFER_ORDER_TYPE, -1, 2);
>

This patch (of 5):

The NUMA APIs currently allow passing in a "preferred node" as a single
bit set in a nodemask.  If more than one bit it set, bits after the first
are ignored.

This single node is generally OK for location-based NUMA where memory
being allocated will eventually be operated on by a single CPU.  However,
in systems with multiple memory types, folks want to target a *type* of
memory instead of a location.  For instance, someone might want some
high-bandwidth memory but do not care about the CPU next to which it is
allocated.  Or, they want a cheap, high capacity allocation and want to
target all NUMA nodes which have persistent memory in volatile mode.  In
both of these cases, the application wants to target a *set* of nodes, but
does not want strict MPOL_BIND behavior as that could lead to OOM killer
or SIGSEGV.

So add MPOL_PREFERRED_MANY policy to support the multiple preferred nodes
requirement.  This is not a pie-in-the-sky dream for an API.  This was a
response to a specific ask of more than one group at Intel.  Specifically:

1. There are existing libraries that target memory types such as
   https://github.com/memkind/memkind.  These are known to suffer from
   SIGSEGV's when memory is low on targeted memory "kinds" that span more
   than one node.  The MCDRAM on a Xeon Phi in "Cluster on Die" mode is an
   example of this.

2. Volatile-use persistent memory users want to have a memory policy
   which is targeted at either "cheap and slow" (PMEM) or "expensive and
   fast" (DRAM).  However, they do not want to experience allocation
   failures when the targeted type is unavailable.

3. Allocate-then-run.  Generally, we let the process scheduler decide
   on which physical CPU to run a task.  That location provides a default
   allocation policy, and memory availability is not generally considered
   when placing tasks.  For situations where memory is valuable and
   constrained, some users want to allocate memory first, *then* allocate
   close compute resources to the allocation.  This is the reverse of the
   normal (CPU) model.  Accelerators such as GPUs that operate on
   core-mm-managed memory are interested in this model.

A check is added in sanitize_mpol_flags() to not permit 'prefer_many'
policy to be used for now, and will be removed in later patch after all
implementations for 'prefer_many' are ready, as suggested by Michal Hocko.

[mhocko@kernel.org: suggest to refine policy_node/policy_nodemask handling]

Link: https://lkml.kernel.org/r/1627970362-61305-1-git-send-email-feng.tang@intel.com
Link: https://lore.kernel.org/r/20200630212517.308045-4-ben.widawsky@intel.com
Link: https://lkml.kernel.org/r/1627970362-61305-2-git-send-email-feng.tang@intel.com
Co-developed-by: Ben Widawsky <ben.widawsky@intel.com>
Signed-off-by: Ben Widawsky <ben.widawsky@intel.com>
Signed-off-by: Dave Hansen <dave.hansen@linux.intel.com>
Signed-off-by: Feng Tang <feng.tang@intel.com>
Cc: Michal Hocko <mhocko@kernel.org>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Andrea Arcangeli <aarcange@redhat.com>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Mike Kravetz <mike.kravetz@oracle.com>
Cc: Randy Dunlap <rdunlap@infradead.org>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Andi Kleen <ak@linux.intel.com>
Cc: Dan Williams <dan.j.williams@intel.com>
Cc: Huang Ying <ying.huang@intel.com>b
Cc: Michal Hocko <mhocko@suse.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

Conflicts:
	mm/mempolicy.c
Signed-off-by: Ma Wupeng <mawupeng1@huawei.com>

---
## [CherryCreamSoda/Shinjuku-Medical-Center](https://github.com/CherryCreamSoda/Shinjuku-Medical-Center)@[20939d6d70...](https://github.com/CherryCreamSoda/Shinjuku-Medical-Center/commit/20939d6d70c4fb1fbc76dba7eb1081f67a39ca18)
#### Saturday 2023-07-01 07:06:17 by unknown

7/1 - Remade Demi-Thief Birth Cutscene

Use of flow renders event data redundant, may migrate later if not a huge pain in the fucking ass.

---
## [MemedHams/Shiptest](https://github.com/MemedHams/Shiptest)@[725233b42b...](https://github.com/MemedHams/Shiptest/commit/725233b42b6f56551798a0a75b5362e577042de3)
#### Saturday 2023-07-01 07:28:16 by thgvr

The Lizardening Part One (And Friends) (#1845)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR changes a lot of sprites. It's honestly too much. Namely:

- Explorer Equipment + Prototype
- Syndicate clothing
- Digitigrade lizard legs
- A new tail from Halcyon.
- Magboots from Zeta. Originally PR'd to tgstation.
- Colored (not greyscale! Ha Ha!) jumpsuits from Imaginos.

Heavy inspiration from the work of Imaginos, Halcyon, Mqiib, and
2cents#8442 for the original leg-work. (Haha, get it?)
The new digitigrade sprites started as a twinkle in the eye of Mqiib,
for yogstation(?) After myself and Halcyon saw those, an epihpany
struck. Perspective makes things cool and digitigrade perspective was
BAD.

I'll include a collage image of the new sprites if it's needed later.
Preview below:


![image](https://user-images.githubusercontent.com/81882910/228710332-0a213f88-5a8b-4b41-abdd-cee3b70ec403.png)
## Why It's Good For The Game
lizard,
Death of Codersprites
## Changelog

:cl:
add: New Digitigrade lizard sprites.
add: Various syndicate and mining clothing resprites.
add: Sarathi can now have an incredibly large tail.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Gyu1291/lokinet](https://github.com/Gyu1291/lokinet)@[e981c9f899...](https://github.com/Gyu1291/lokinet/commit/e981c9f89983a12cc75d691fc439366703d5bfff)
#### Saturday 2023-07-01 08:25:32 by Jeff

tweaks for wine and yarn for gui

* allow specifying a custom yarn binary for building the gui using -DYARN= cmake option
* unset DISPLAY when calling wine because i hate popups
* do not rebuild gui when building for windows
* by setting the magical undocumented env var USE_SYSTEM_7ZA to 'true' we can have the pile of npm bullshit code use our system's local 7z binary instead of the probably not backdoored binary from npm, yes for real. i hate nodejs so god damn much you have no fucking idea
* allow providing a custom gui from a zip file via -DGUI_ZIP_FILE cmake option

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[44b7300b08...](https://github.com/treckstar/yolo-octo-hipster/commit/44b7300b088a90de43eb16ac283493effb705a9b)
#### Saturday 2023-07-01 09:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [AuxiDev/CppProjectsCreator](https://github.com/AuxiDev/CppProjectsCreator)@[c9cd96c5bd...](https://github.com/AuxiDev/CppProjectsCreator/commit/c9cd96c5bd67d7d78d3062080acb04c8d9eefe9f)
#### Saturday 2023-07-01 11:11:45 by David_Craft_

V0.2.0 - Major Update

# New Features

-   Introducing the "Compiler Command Prefix" setting: You can now customize the prefix of your compiler command. The default is "g++".
-   Added the "Compiler Arguments" setting: Edit the arguments used by the compiler. We have included some default arguments, but you are free to modify them to fit your needs.
-   Two new buttons for compiling your project: You'll find these buttons conveniently located next to the list of opened files and at the bottom left of the editor.
-   Added a command for compiling your project: Use the command to trigger the build process easily or use the new buttons.

# Quality of Life Improvements

-   Enhanced error messages: Error messages are now more informative and helpful in troubleshooting any issues that may occur during the compilation process.
-   New terminal instance for compilation: A new terminal window will be opened specifically for compiling your project, providing a cleaner and more focused experience.

# Changes

-   Removed tasks.json: All the build task configurations are now handled internally, removing the need for an external tasks.json file.
-   Removed .vscode folder: The extension now manages its internal configuration and structure, eliminating the need for the .vscode folder.

# Bug Fixes

-   Addressed minor bugs and resolved any known issues to ensure a smoother user experience.

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[867c217c57...](https://github.com/Helg2/tgstation/commit/867c217c57bbcbb644e06bfcb6d362e494a895ee)
#### Saturday 2023-07-01 11:17:38 by GuillaumePrata

New Wizard spell "branch": Vendormancy (#75679)

## About The Pull Request
New item for wizards, ~~the Staff~~ Scepter of Runic Vendormancy.

With it, you can summon Runic Vending machines to block your enemies,
push them 2 tiles back around the summoning tile, throw the vendors 4
tiles away to squash them or simple detonate the vendors for direct
damage against enemies within a 2 tile range.

The scepter has 3 charges that can be recharged after a "long" channel
so while powerful, it is a tactical weapon and wizards can't directly
steamroll the crew with endless vendors. (Unless they buy multiple
scepters, but that is just funny.)

Also, there is a bug with the throw... I copied how baseball bats deal
with knockback, but they consistently don't push the vendors back, just
spin them on the same tile... I appreciate if anyone has any idea on how
to fix or change that to a better system.

## New changes I made
The vendor has a random set of REAL wizard robes and hat, sandals and a
foam vendor scepter as products to sell now.
This gives the crew some real armor, and if it is considered too much, I
can swap it for the fake versions.
IMO the real clothes work as the perfect bait for the crew to approach
the vendors and get exploded in the process, and while a random
assistant might get real wizard armor to go valid hunt the wizard, the
crew might just mistake them for the real wizard and beat them to death,
which is too funny.
## Why It's Good For The Game

![vendormancerPR](https://github.com/tgstation/tgstation/assets/55374212/f9d98f3e-5916-4a17-987e-249f4cdb7185)

About a year ago I played Stoneshard, and it has such an amazing
Geomancy Wizard that I wanted to port some of its gameplay to SS13 as
our wizards, while funny and destructive, are kinda simple to play...

Summoning and blowing up rocks was nice, but I randomly had the idea of
summoning Vendors while at work and vendors squashing people has become
such an iconic SS13 thing to me that I had to stop being lazy and start
working on this.

Something, something, enviromental combat wizard.
## Changelog
Gonna polish the changelog later too...
:cl: Guillaume Prata
add: New Wizard spell branch: Vendormacy! Summon runic vending machines
with your Vending Scepter, force push them on your enemies to squish
them or blow them up while they are busy buying from the machines.
/:cl:

---------

Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [Proxima-Project/Proxi-Eris](https://github.com/Proxima-Project/Proxi-Eris)@[a4d33b82c2...](https://github.com/Proxima-Project/Proxi-Eris/commit/a4d33b82c23581fa57e29a722c560d81face11c1)
#### Saturday 2023-07-01 11:43:32 by евиё

Titanium material (#8)

* adding titanium

may the god forgive me for editing base

* fixes my fuck ups

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d85e44c69c...](https://github.com/tgstation/tgstation/commit/d85e44c69cc06dbeeb3a0de7f76273de45ee3893)
#### Saturday 2023-07-01 12:15:27 by ChungusGamer666

SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76422
This was caused by me somehow not using the wrapper there and not
noticing it

Also fixes hair gradients and facial hair gradients. I am pretty sure
they were uhh, being hidden behind the actual hair/facial hair. Oops.

Also also fixes spawning yourself as a human as admin and getting random
hair colors. That was just a failure to update the icon after updating
everything, I think?

Additionally, to totally babyproof all of this, ensures that head_flags
involved stuff gets applied AFTER species by creating a new preference
priority, and uses two separate wrappers to apply gradient style and
color.

Here's this absolute hellspawn to prove that everything works.

![image](https://github.com/tgstation/tgstation/assets/82850673/7ed29a68-cb60-4b28-996c-3be0e7331be8)

![image](https://github.com/tgstation/tgstation/assets/82850673/e57128be-0d7c-46ad-90dd-ee25981d0fea)

![image](https://github.com/tgstation/tgstation/assets/82850673/5c3619a8-fe6f-42b3-9fdc-12277d568e8d)

![image](https://github.com/tgstation/tgstation/assets/82850673/fdd13000-2220-47ad-8e02-44bc75a4a907)

Sorry for being so damn good at breaking this codebase.

## Why It's Good For The Game

Bugs are bad they make you mad

## Changelog

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

---
## [64BitDragon/Zero-K](https://github.com/64BitDragon/Zero-K)@[5e2b1657be...](https://github.com/64BitDragon/Zero-K/commit/5e2b1657be4cd0d9d7975eb434cc40c9a350ee1b)
#### Saturday 2023-07-01 13:06:46 by Helwor

Big update, various improvements and fixes, slight rewrite

-Adapted my code to be compatible with the Zero-K version

-Rewrote slightly the code to be more concise and efficient

-Fixed: The Zero-K version is broken since an edit made Sep 2020 (!) when user start to change spacing, the rectangles would never disappear because newspacing variable was never falsified at the end of the  Update round.

-Fixed: the param for spTraceScreenRay was the opposite of what it should be

-Improvement: The widget now adapt to the wrong engine grid which is off and also sometimes misleading when it comes to place units on water

-Added: On this particular case, widget gives the possibility for the user to either follow the grid coherence, or show the reality of where the unit will actually be placed. In that case, an extra rect is drawn to see where the first placement will land.  By usage, it seems the latter is more interesting so I put it on by default.
(More details in the comments that could help fix the problem with the engine)

-Improvement: the option panel now stop resetting scroll anytime an option is changed, this fix could easily be implemented universally by changing WG.crude.OpenPath, all it have to do is remembering 'scrollPosY' of the last panel and apply it to the new.

-Added: an option  for the user to choose wether rects should spread straightforward (if user want to only have a basic glance of the separation with no simulation of placing on the ground) or follow the ground, as it was before. I'm undecided which is the best as default for new users.

-Added: an option to have different colors of rects for bad placements, this on default if follow ground is on default, it seems to be adding a plus mostly in this case.

-Changed Description that's been edited, it does not just memorize spacing. I understand that it need to be concise, but a description is meant also to say what it does. User won't be able to tell if that widget make the previsualization or add mouse wheel to spacing by reading its description.

-Changed back title of an option. The purpose of how they are written is to build a sentence obviously, to make it more straightforward and user friendly. This change broke that concept. When user, especially new user, dive into options they can be lost as I was, to understand what option do what, if the option is dependent of another, etc... that's the purpose of my system to make all that as clear as I can.

-Changed back some default for new user, I think having the shift+mousewheel is a must, it's faster and more convenient, especially when discovering the game. I would have been glad to have that when I started, (that's, by the way, why I rewrote this widget in the first place).
Also changed back previsualization, with only 2 rects and only when spacing change, and for 0.7 sec
It is, in my opinion, also much more convenient for a new user to be able to see in a quick glance how your placement will be separated without the need of start posing queue and THEN realize the spacing is not good. If non-new user get tired of it, they will be able to find the options to undo it.
Indeed, new user will not be anymore really a new user when he discovers previsualization, if it's not on by default.

-Few minor things:
  -preGame is now set by GameFrame and then GameFrame removes itself
  -MouseWheel gets added/removed whenever shift+wheel option is changed
  -I don't see any reason to change the name spaced_rects in spaced_rects_2. As far as I know, one can only want that for resetting his own option to default for testing  purpose. Reverted it since it didn't make sense.
  -Upped the max time before infinite for show value and show rects to 10 sec
  -Didn't reverted it but imho, changing 'p' to 'placement' made the code uselessly more cumbersome than it already is.
  -Changed 'if not placementCache[unitDefID] then'  to 'if not placeTable[unitDefID] then' as the code was intended to mean
  note about this: since the vast majority of building have same sizex and sizez, maybe it could be improved by checking if it's relevant to consider the off-facing in 
  before.
 -Estomped the double dots before option titles when they are active, to make them less present.
 -update placement on more relevant changement of facing
 -Made the options defaults in concordance with the widget defaults
 -And maybe some other stuff I forgot

Lots of change, so please, let me know what you think.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[1b0efb9347...](https://github.com/treckstar/yolo-octo-hipster/commit/1b0efb93477430a84d66900d11d2729ec11758f4)
#### Saturday 2023-07-01 13:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Huge/openai-LLM-evals](https://github.com/Huge/openai-LLM-evals)@[7c3159aaaf...](https://github.com/Huge/openai-LLM-evals/commit/7c3159aaaf8553ad19d1ba177f602302c06d75c6)
#### Saturday 2023-07-01 13:24:32 by Fabrizio Ruggeri

Proofreader (#1225)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

proofreader

### Eval description

Asking the model not only to correct some text but also following rules
when correcting. These rules enforce to not correct some parts or to
correct in a specific way.

### What makes this a useful eval?

This come from a real use case where gpt4 was not reliable 100%

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ x Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ x Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is
music"},{"role":"user","content":"A big thank you to our guitar and base
player"}],"ideal":"A big thank you to our guitar and bass player"}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing
more"},{"role":"user","content":"This is correct!"}],"ideal":"This is
correct!"}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is 20th Century Modernist
Art"},{"role":"user","content":"Pablo Picaso's famuos painitng Guernica
dipicts the atrocities of the Spansh Civil War."}],"ideal":"Pablo
Picasso's famous painting Guernica depicts the atrocities of the Spanish
Civil War."}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is
philosophy"},{"role":"user","content":"Nitsche never wrote Der Wille zur
Schmacht. It was his sister Elisabeth Foerster that compiled the work
and gave it an antisemithic tone."}],"ideal":"Nietzsche never wrote Der
Wille zur Macht. It was his sister Elisabeth Förster that compiled the
work and gave it an antisemitic tone."}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing
more"},{"role":"user","content":"Stop doing this!"}],"ideal":"Stop doing
this!"}

  ```
</details>

---
## [Huge/openai-LLM-evals](https://github.com/Huge/openai-LLM-evals)@[c0c784fd97...](https://github.com/Huge/openai-LLM-evals/commit/c0c784fd978bb2e4bc4b5aef7b0f032fa3b04a75)
#### Saturday 2023-07-01 13:24:32 by monocle-pastels

[eval] norwegian rhymes (#1248)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

norwegian-rhymes

### Eval description

Check if Norwegian Bokmål words are rhyming 

### What makes this a useful eval?

It's important that GPT understands Norwegian phonetics and language

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This contains multiple cases of most pitfalls when considering what
rhymes in Norwegian.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
- [] (Ignore if not submitting code) I have run `pip install pre-commit;
pre-commit install` and have verified that `black`, `isort`, and
`autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "avskjed,
beskjed"}], "ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "led,
beskjed"}], "ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "nett, vet"}],
"ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "deg, vei"}],
"ideal": "Yes"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "huset,
knuse"}], "ideal": "Yes"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "her, sær"}],
"ideal": "Yes"}
  ```
</details>

---
## [micoli/symfony](https://github.com/micoli/symfony)@[af44385d9e...](https://github.com/micoli/symfony/commit/af44385d9e6eba77b4bf4610231ce9569bdcc9b5)
#### Saturday 2023-07-01 13:43:27 by Robin Chalas

feature #50754 [HttpKernel] when configuring the container add services_{env} with php extension  (helyakin)

This PR was merged into the 6.4 branch.

Discussion
----------

[HttpKernel] when configuring the container add services_{env} with php extension

| Q             | A
| ------------- | ---
| Branch?       | 6.4
| Bug fix?      | no
| New feature?  | yes
| Deprecations? | no
| Tickets       | none
| License       | MIT

Hello the community

This is my first PR attempt.

So after reading this [documentation](https://symfony.com/doc/current/service_container.html#remove-services) and unsuccessfully trying to load my `service_test.php`, I've noticed that the `configureContainer(..)` function in the `MicroKernelTrait` file was not configured to automatically load this file.

So either we should fix the documentation, either we should fix the configuration.

Since this the [framework-bundle](https://github.com/symfony/framework-bundle) is backed by [Alximy](https://alximy.io) I figured it would be cool 😎 to try and fix 🐛 the configuration.

Anyway share me your thoughts about what should be done !

And I wanted to say that php service configuration is 🔥 so shoutout to the one who did this (I think it's you `@nicolas`-grekas with this [PR](https://github.com/symfony/symfony/pull/23834) right ? 💪🏻)

Also big thanks to `@jeremyFreeAgent` for debugging this with me and `@HeahDude` for showing me the php service configuration PR.

Commits
-------

4aac1d9fee :bug: (kernel) when configuring the container add services with php ext

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[221e82c364...](https://github.com/Helg2/tgstation/commit/221e82c3640c75d99dc2616bf666bd897b4a5be8)
#### Saturday 2023-07-01 13:53:32 by ChungusGamer666

[NO GBP] Fixes my fuckups with species livers (#76331)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76329
I DID A REAL STUPID MISTAKE WHILE CODING
https://github.com/tgstation/tgstation/pull/76184 I AM SORRY
The signal was sending the fucking human instead of seconds_per_tick

## Why It's Good For The Game

Fixes a BUNCH of liver behavior including plasmamen livers not healing
wounds

## Changelog

:cl:
fix: Plasma will now heal plasmamen properly
/:cl:

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[8af20d1577...](https://github.com/Helg2/tgstation/commit/8af20d157738044cef2fc00846caa1869d56a087)
#### Saturday 2023-07-01 13:53:32 by necromanceranne

Fixes some inconsistencies with the chaplain revolver and gets rid of a weird ammo define (#76237)

## About The Pull Request

Firstly, I gave the revolver a new sprite. I mean, this isn't so much of
an improvement as it is a reference I wanted to go with, so if people go
'no not a new sprite' I don't mind reverting.

What's the reference? Check the new name I added as a potential name
roll.

![lucky
38](https://github.com/tgstation/tgstation/assets/40847847/e11874be-1416-4e21-bda9-4881d49cad1b)

Secondly; I applied to the gun itself revenant bane, the ability to
clear runes, and proper magic immunity as a full null rod would enable.
This last bit was a deliberate design choice, but the divine bow has
full magic protection, so I think this is now more of a consistency
consideration compared to the divine bow.

Thirdly, the revolver is a .38 revolver, HOWEVER, it uses a damage
multiplier to bring it back to the damage it did originally. It also
cannot be reloaded without the prayer action. No cheating. Effectively,
this is the same mechanically as it was before.

It rarely does a funny crit fanfare. This does nothing mechanically, I
just thought it was a funny nod to the sprite's reference (and I guess
another game that the crit fanfare is based on). Borrowed parts of the
code and sprite from this April Fool's pr by Wallemations >
https://github.com/tgstation/tgstation/pull/74425

## Why It's Good For The Game

I think this might have been a little forgotten since implementation now
that we have another projectile weapon for the chaplain. So I'm brushing
it up a bit.

## Changelog
:cl:
fix: Makes the chaplain's revolver consistent with its immediate
sibling, the Divine Bow, by giving it similar statistics.
code: Makes the chaplain revolver a .38 but prevents it from being
loaded without using the special prayer action. Also applies a damage
multiplier to keep it at the original 18 force. Mechanically, no
different.
sprite: Gives the chaplain revolver a new sprite.
code: Removes an unnecessary admin log when removing runes.
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[8c2c72b0ed...](https://github.com/tgstation/tgstation/commit/8c2c72b0ed7a1fad112fc4da8a8b7de7faa5e114)
#### Saturday 2023-07-01 14:36:28 by LemonInTheDark

Duiffel Spotfix (#76442)

## About The Pull Request

Gives duffelbags their proper slot count
They inherited this from backpacks, but I sorta just forgot about that

[Creates "levels" of locked objects, uses that to make locked duffels
work](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

[c613c00](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

Turns locked into something that holds defines, this makes life a lot
easier.
Requires a lot of boilerplate because of how many uses of these procs
there are and all the passthrough and shit.

Adds a few outfit subtypes to avoid this class of failure in future.

Renames the args in a few but not all touched procs, one thing at a time

Closes #76407
Closes #76430 Had the lock check in the wrong place
Closes #76441 GOD I HATE TK SO MUCH

Wrote half the pr without glasses so if it's weird gimme some grace
yeah?

## Changelog
:cl:
fix: Fixes some fuck with duffelbags, them not holding enough + issues
with spawning gear in them (job shit and all)
/:cl:

---
## [Rohail33/Realking_xiaomi_xaga](https://github.com/Rohail33/Realking_xiaomi_xaga)@[e6c0a14f65...](https://github.com/Rohail33/Realking_xiaomi_xaga/commit/e6c0a14f653cdd799df67cb87dac523fca43f4a0)
#### Saturday 2023-07-01 15:27:57 by Wang Han

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

---
## [AOSPA-overlook/android_frameworks_base](https://github.com/AOSPA-overlook/android_frameworks_base)@[36e5f5310d...](https://github.com/AOSPA-overlook/android_frameworks_base/commit/36e5f5310d4cb5d94d8a55a7c8dc777095a0cc35)
#### Saturday 2023-07-01 15:51:16 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [DEAD10C5/ctf-dc31-cloud](https://github.com/DEAD10C5/ctf-dc31-cloud)@[655baeaddd...](https://github.com/DEAD10C5/ctf-dc31-cloud/commit/655baeaddd96144dcaf2978b373e7adfc7a66b04)
#### Saturday 2023-07-01 16:09:59 by your-dnsp

Update YOU-SAID-THIS-WAS-A-TEST (#17)

* Update YOU-SAID-THIS-WAS-A-TEST

Cleaning up the bullshit from last night's being silly. 
Will put links in the notes file

* add two new installers

* add two new installers

---------

Co-authored-by: FrankTheTank <2730246+devsecfranklin@users.noreply.github.com>

---
## [magefree/mage](https://github.com/magefree/mage)@[496faaf5cb...](https://github.com/magefree/mage/commit/496faaf5cb9ff47066178d08e9cb6e252bd7454a)
#### Saturday 2023-07-01 16:53:32 by Susucre

[LTR] Implement The Balrog, Durin's Bane (#10515)

* [LTR] Implement The Balrog, Durin's Bane

I could use someone more experienced for this card:
Should the watcher `PermanentsSacrificedWatcher` be initialized locally in the card's class, or is a global initializing in GameImpl.java alright? I went for the latter for now, as my base for implementing the static cost reduction was Blood for the Blood God!

* apply review

* no longer instantiate watcher on every game.

---
## [Hardaeborla/zechub](https://github.com/Hardaeborla/zechub)@[8d7c522bea...](https://github.com/Hardaeborla/zechub/commit/8d7c522bea40a7cc2e28d2e7bf9eea86cdfaffdd)
#### Saturday 2023-07-01 17:54:45 by Hardaeborla

zecweekly.md

# ZecWeekly #49
$656M lost from crypto hacks, Kraken Compelled to Share User Data, Investors still waiting on $1.9M Refund 

Curated by "Hardaeborla" ([Hardaeborla](https://twitter.com/ayanlajaadebola))

---

### Welcome to ZecWeekly
Hello Zcashers!! Welcome to another exciting edition of our weekly newsletter where we share recent news happening in the Crypto space and information latest happening about ZCash ecosystem. You can also be a contributor on ZecHub by visiting our [site](https://wiki.zechub.xyz/contribute) 

In this week newsletter, we will be exploring recent happenings in the ZCash Ecosystem including the ECC Transparency Report. You'll also be learning about different transaction model on the ZCash ecosystem including recent developments in the Crypto Space. 
---

## This Week's Education Piece 
In this week Educational Piece you'll be learning more about different pools existing on the ZCash Network and utilizing the best practices when it comes to selecting the required pools for transaction. Learn more about this via the link below 👇👇
[ZCash Value Pools](https://wiki.zechub.xyz/zcash-value-pools) 


## Zcash Updates


#### ECC & ZF Updates

[ECC shares Transparency Report](https://twitter.com/ElectricCoinCo/status/1674825997206667288?t=Zn9dB-KZOfAktomH8fkSIg&s=19) 

[ECC Shares Insights on Zcashd package signing keys](https://twitter.com/ElectricCoinCo/status/1674177380213051393?t=Dn0Jpxt1YEpyCY87I6Y4AA&s=19) 

[The ZF Engineering Team Discusses about Zebra](https://twitter.com/ZcashFoundation/status/1674481431337115648?t=vsHN1xkRdlz96oaGvTtV1g&s=19) 

[Zcash Arborist Call Summarised by Jason](https://twitter.com/zksquirrel/status/1674568125688193028?t=eC8iYguak-Zi0AXn4SlFoQ&s=19) 

[Upgrade to Zcash 5.6.1](https://twitter.com/zcash_community/status/1674569168690065410?t=nqPzbqAzoMEf1HFfx6JY3Q&s=19) 





#### Zcash Community Grants Updates

[The Results Are In](https://forum.zcashcommunity.com/t/zcg-committee-election-june-2023/44668/35?u=Hardaeborla) 

[ZecHub Shares Report of Monthly Activities](https://forum.zcashcommunity.com/t/zechub-monthly-updates/44101/22?u=Hardaeborla) 


#### Community Projects

[Learn More About ZCash via ZCash Hub](https://twitter.com/zcash/status/1674090119085662214?t=oSMxAiLRNs9OzfWdo6mkRQ&s=19) 

[ZFAV Monthly Meetup](https://twitter.com/ZFAVClub/status/1674056270716760064?t=j15J36xCGQJPxwM7zZ_wIg&s=19) 

[Zcash Crusader from Chapter 1 - 4](https://twitter.com/ZcashCrusader/status/1673562963955810304?t=kVnAFnkX1aoFA4kJ0-WhHA&s=19) 

[Zcash Nigeria host ZCash Meetup for Nigerians](https://twitter.com/ZcashNigeria/status/1673654414689677318?t=PEAwDj4tE_OzY-D1l_LXyg&s=19) 

[Support the campaign Zcon4 Events](https://twitter.com/robmarn/status/1673840426212634626?t=f6yDhW8StnqhMQjMzN2d6Q&s=19) 

[Zcash Español host ZCash Meetup](https://twitter.com/lbcbmtl/status/1673746471445749772?t=IL1xaiqb8k9Cqxmih_oySw&s=19) 

[Zast EP 003 Now Available](https://twitter.com/ZcastEsp/status/1673853524185104384?t=j3AIucX3QRKZhAH_FXNo9w&s=19) 

[ZecHub Got Featured](https://twitter.com/ZecHub/status/1674819584476561419?t=tuPzJEADW8wM_qeVIqhHPw&s=19) 

[Zcash Brazil Host another Quiz - ZEC on Discod](https://twitter.com/zcashbrazil/status/1674901050854088704?t=7ZtDYZdpwzRCzZ4DbgzmNw&s=19) 

[Zcash Español Rewards POAP To Active Users](https://twitter.com/zcashesp/status/1674946127391600641?t=pZBVFOeEQI7Sw1K5R_4cMg&s=19) 

[Having Issues with Zingo?](https://twitter.com/ZingoLabs/status/1674931179231797248?t=yygLx7JVwBGpStwTHTpa4w&s=19) 

[Get to know more about @robmarn](https://twitter.com/zcashesp/status/1674943397860081671?t=fcGA7b7KFm6wFen_HeOFvQ&s=19) 

[Learn More about Zebra Implementation](https://twitter.com/zcashbrazil/status/1673724361629396993?t=EpsxKY7E2ZBtt0rMqetiIA&s=19) 

[Check out ZCash Brazil New DP](https://twitter.com/zcashbrazil/status/1673509298624688130?t=hy3YsFFxrvRxm5IlMNGAug&s=19) 













#### News & Media

[Investors still waiting on $1.9M refund Logan Paul promised 6 months ago](https://cointelegraph.com/news/investors-still-waiting-on-refund-logan-paul-promised-six-months-ago) 

[Kraken ordered by court to disclose user data to IRS for tax compliance](https://cointelegraph.com/news/kraken-ordered-by-court-disclose-user-data-irs-tax-compliance) 

[$656M lost from crypto hacks, scams and rug pulls in H1 2023](https://www.google.com/amp/s/cointelegraph.com/news/656m-lost-from-crypto-hacks-scams-and-rug-pulls-in-h12023-report/amp) 

[Bitcoin price has never lost more than 10% in July](https://cointelegraph.com/news/bitcoin-price-never-lost-july-2023-different) 

[Redditor up 25% after boldly taking out $59K worth of personal loans to buy BTC](https://cointelegraph.com/news/redditor-up-25-after-boldly-taking-out-59k-worth-of-personal-loans-to-buy-btc) 





## Some Zcash Tweets
[Check Out this ZCash Mud Designs](https://twitter.com/mad_paiement/status/1674430123007946755?t=jwYVkKwVbleRZDmNXw71hQ&s=19) 

[Zero Knowledge is the future of Blockchains](https://twitter.com/michae2xl/status/1674438977820999681?t=pySy98i0U1_OUTLq7svC3g&s=19) 

[Check out this beautiful ZCash Art] (https://twitter.com/ZcashAI/status/1674427111325712386?t=ZEVMBjiMquQxCUQv5E1kow&s=19) 

[Privacy is Normal Explained in Español](https://twitter.com/doloresampaio/status/1674929536205504513?t=MHpoKv1FoHe9n81DWhza3g&s=19) 

[A Zcasher Explains Why He Holds ZEC] (https://twitter.com/Crypto2Ye/status/1674815229014810631?t=2BXRD2ArTxz-1BBjsZWoMA&s=19) 

[@fillzorkillz advices ZCash community](https://twitter.com/fillzorkillz/status/1674157761565958149?t=OJxeGTZyqxcSdHtc-hprOw&s=19) 

[Zooko Commends Zingo Labs Team](https://twitter.com/zooko/status/1672699602733088768?t=WgW6TDE6x3Rwn1J5HuVl4A&s=19) 

[Nate shares Insight on Binance Privacy Coin Reversal Decision](https://twitter.com/nate_zec/status/1673751414957559809?t=jG8COIQbNqRywsQqMX5c8g&s=19) 

[A Friendly Reminder About ZCash](https://twitter.com/Lexaleth/status/1674625667202179072?t=YutAa5vF-geSBxbR4hri8Q&s=19) 












## Zeme of the Week
[https://twitter.com/JackGavigan/status/1673790256439492608?t=cehze_6ZMcSymqdTJGxeQQ&s=19](https://twitter.com/JackGavigan/status/1673790256439492608?t=cehze_6ZMcSymqdTJGxeQQ&s=19) 

## Jobs in the Ecosystem

- [Executive Head of Product, ECC](https://apply.workable.com/electric-coin-company/j/6ACEC09B90/)

- [Director of Security, ECC](https://apply.workable.com/electric-coin-company/j/E68A4C20E2/)

---
## [warptools/rustwarp](https://github.com/warptools/rustwarp)@[b06fa6bcd3...](https://github.com/warptools/rustwarp/commit/b06fa6bcd3c1a66c743388011d93304fe212d07b)
#### Saturday 2023-07-01 18:12:12 by Eric Myhre

YEEEAAAAHHHHH!  Real CLI wired now.  And **great errors**.

Try this:

`warpforge-cli catalog read-item heyo`

And you'll receive:

  > error: invalid value 'heyo' for '<CATALOG_REF>': failed to parse CatalogRef value: "heyo" should have more separators (the next one would delimit the start of the release_name field; the separator is ":")

Y E S.

It's hard to say how exciting this is.  It shouldn't be.  But it is.
Trying to get that quality level out of the golang libraries where
I've been spending time with for the past few years... has been an
exercise of pulling teeth, to put it mildly.  Here, by the time things
compile, it's all sorted.  The libraries are handling errors well and
attaching lots of contextual details (yay); and for the parts of the
errors that were my responsibility, we saw the compiler helping
shepherd things into a well-typed direction; and the combo of that plus
macro libraries that help write error messages... All of this worked
together to move things in a good direction.

I've tried to solve that second problem in golang by producing the
go-serum-analyzer (but it's pulling teeth, lots of work, has many
limitations, and is stuck as non-core influence levels), and I've tried
to solve that second problem with go-serum templating helpers (and
that's had some good success, but still requires a lot of boilerplate
to actually use).  By contrast: Rust's ecosystem just _has_ these
things already.  And they're _really good_.

Yes, this commit message is an ode to rust again.  Sorry not sorry.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[02e36ec18e...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/02e36ec18e5ff421243b6816cf115d27c2c4263d)
#### Saturday 2023-07-01 18:21:49 by SkyratBot

[MIRROR] Expanding the Experimental MODsuit Bepis Node with three new modules. [MDB IGNORE] (#21851)

* Expanding the Experimental MODsuit Bepis Node with three new modules. (#75801)

## About The Pull Request
So, I've had this idea to make a contribution to the Bepis feature with
some modsuit stuff. The gimmicky stuff is ok and a good way to even out
the better content since it has game of chance design it has (you can
find those disks in space anyway so...). However, the Experimental
MODsuit node feels very underwhelming right now, compared to how big
that feature is.

This PR adds three MOD modules to the Experimental MODsuit node, plus
two more:
- Magneto Charger: While the Modsuit is activated, each step the user
takes will charge the installed power cell by a tiny bit, enough to
sustain a standard modsuit of generic slow speed with only a few, easy
modules installed. It won't work in zero G, while flying, pulled by
someone else, on a conveyor belt, riding a vehicle or crawling on the
floor, though.
- Recycler: It collects (most) garbage and casings off the ground and
recycles them into material sheets that can be dispensed on an adjacent
location or storage with with Middle Mouse Button. Doesn't clean debris,
and scuffed because most trash doesn't yield material anyway.
- - It also has two subtypes, unbound from the node: one that dispenses
riot foam darts and can be found on the black market, and another that
dispenses the more innocuous foam darts, rarely found in maints.
- Shooting Assistant: A configurable module. On Stormtrooper mode, it
will give the user a faster fire rate (the double tap trait) at the cost
of accuracy. On Sharpshooter mode, it will improve the user accuracy and
make their shots ricochet against walls at least once (if the hit atom
allows that, that is, e.g. lasers don't ricochet against iron walls), at
the cost of movement speed. Both modes also prevent the user from dual
wielding guns.

To make the Stormtrooper mode stackable with the poor aim quirk and
refrain from making a new trait for the sharpshooter mode, the gun
spread code in gun.dm has also received a little refactor and cleanup.
Also, it's been tested.

## Why It's Good For The Game
The Experimental MODsuit node is quite shabby and could use something
extra to make it more appealing to MODsuit enjoyers.

Also doubles down as a small addition to the black market and maint
loot, and code cleanup, since gun code gives off some garbled vibes.

## Changelog

:cl:
add: Expanded the Experimental MODsuit Bepis node with three new
modules: Magneto Charger, Recycler and Shooting Assistant.
add: Added a Riot Foam Recycler module to the black market, as well a
more innocuous version as maint loot.
/:cl:

* Expanding the Experimental MODsuit Bepis Node with three new modules.

* update modular, I hate this file btw

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [Blayung/kum.io](https://github.com/Blayung/kum.io)@[32a87a7a3b...](https://github.com/Blayung/kum.io/commit/32a87a7a3bdb87441a868588efa8cfd34750e7c2)
#### Saturday 2023-07-01 18:52:05 by Blayung

finished (I think finished) code for connecting to the server and registering yourself. It looks really ugly, but it works. I really need to split that unreadable shit into different files.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[0cd356125a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/0cd356125ad5f6e144a18f9da586699a94dd154a)
#### Saturday 2023-07-01 18:55:52 by SkyratBot

[MIRROR] Fixes a sneaky antag tell with RDS / adds policy support [MDB IGNORE] (#21881)

* Fixes a sneaky antag tell with RDS / adds policy support (#76071)

## About The Pull Request

Fixes being able to tell you are a special role via RDS

Adds policy support to RDS

## Why It's Good For The Game

Someone informed me that RDS was a 100% accurate antag tell you rolled a
delayed spawn antag (like headrev), and that's... a little bad, you can
usually insinuate you may be a headrev but straight up knowing isn't
ideal - doesn't keep everyone on equal playing field.

And while I was there I was like "y'know people might want to set policy
for this" so yeah

## Changelog

:cl: Melbert
fix: Fixed a cheeky way RDS revealed you were an antag before you
actually got antag. Sorry, you know who you are.
config: RDS now has policy.json support, to allow customization of the
roundstart "anti-grief" message.
/:cl:

* Fixes a sneaky antag tell with RDS / adds policy support

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Chodum91/Cosmic-Cows-](https://github.com/Chodum91/Cosmic-Cows-)@[1cb99b9d0b...](https://github.com/Chodum91/Cosmic-Cows-/commit/1cb99b9d0b1e0df8ccae1666da2a4d8ffb082609)
#### Saturday 2023-07-01 19:42:11 by Mathhew Shannon Amos

Update README.md

1 of 1,192
TyT
Inbox
75-amos-75-

Baby Papalegba
12:09 PM (1 hour ago)
to me

Baby Papalegba has sent you a link to a blog:

https://music.youtube.com/watch?v=8StL59ye0-g&list=RDAMVM8StL59ye0-g

Blog: TyT
Link: http://chodum91.blogspot.com/

--
Powered by Blogger
https://www.blogger.com/

Attachments area
Preview YouTube video Ice Cube - Hello Gangsta (Ft. 2Pac, The Game, Dr. Dre & Mc Ren)


Papa Legba.N.B
12:30 PM (39 minutes ago)
to Theresa, Three, me

Papa.Legba.N.B https://chodum91.blogspot.com/
@NewBrun48352339
·
44s
Replying to 
@NewBrun48352339
 and 
@davidlabrava
https://howtogeek.com/225487/what-is-the-difference-between-127.0.0.1-and-0.0.0.0…•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• mics on pause once in builds thats with billions and it readsvalue = 123;
Console.WriteLine(value.ToString("00000"));
Console.WriteLine(String.Format("{0:00000}", value));
value = 1.2;
Console.WriteLine(value.ToString("0.00", CultureInfo.InvariantCulture));...---------- Forwarded message ---------
From: Baby Papalegba <no-reply@blogger.com>
Date: Sat, Jul 1, 2023 at 12:09 PM
Subject: TyT
To: <bbrainwizzard.nb@gmail.com>

Attachments area
Preview YouTube video Ice Cube - Hello Gangsta (Ft. 2Pac, The Game, Dr. Dre & Mc Ren)


Papa Legba.N.B
1:09 PM (1 minute ago)
to me, Theresa, Three

  {•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^•    "title": "Recording 7/1/2023 at 12:45:58 PM- @Chodum91_[Chodum91-patch-6](https://chodum91.blogspot.com/2023/06/google-content.html?spref=fb&fbclid=IwAR0C7UitXgnHidGEBPftLjYbrkOz_3-_byKjEBT9Iu9FZgD9BumnxrSlKT4)-[ ](https://github.com/jducoeur/OPCompiler/blob/master/names.conf.proposed http://getpocket.com/@050A8g3cdu224Tu07ep7851p0gTKd039876xOuo186Va83V7dS9e1b88iaMdc679?src=navbar https://podcasts.apple.com/ca/podcast/this-week-in-startups/id315114957 https://newbrun506.blogspot.com/?m=1 https://podcasts.apple.com/ca/podcast/this-week-in-startups/id315114957 - https://newbrun506.blogspot.com/?m=1https://newbrun506.blogspot.com/search/label/.%[![image](https://user-images.githubusercontent.com/93821375/230675549-c05eba3d-cc7e-410e-9d8f-0e0b3ab28750.png)](https://newbrun506.blogspot.com/search/label/.%5E%E2%99%A0%EF%B8%8E%5E.Rainwizzard.com.%5E%E2%99%A0%EF%B8%8E%5E.~%0A%C2%B9%E2%99%A4%C2%B3!%5Bimage%5D(https://user-images.githubusercontent.com/93821375/230658076-4334affe-d594-42c9-962c-123af14519c1.jpeg)?m=1)5E%E2%99%A0%EF%B8%8E%5E.Rainwizzard.com.%5E%E2%99%A0%EF%B8%8E%5E.~%0A%C2%B9%E2%99%A4%C2%B3!%5Bimage%5D( -Replying to  @NewBrun48352339  and  @davidlabrava https://howtogeek.com/225487/what-is-the-difference-between-127.0.0.1-and-0.0.0.0…•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• mics on pause once in builds thats with billions and it readsvalue = 123; Console.WriteLine(value.ToString(\"00000\")); Console.WriteLine(String.Format(\"{0:00000}\", value)); value = 1.2; Console.WriteLine(value.ToString(\"0.00\", CultureInfo.InvariantCulture));- https://user-images.githubusercontent.com/93821375/230658076-4334affe-d594-42c9-962c-123af14519c1.jpeg)?m=1](https://newbrun506.blogspot.com/search/label/.%5E%E2%99%A0%EF%B8%8E%5E.Rainwizzard.com.%5E%E2%99%A0%EF%B8%8E%5E.~%0A%C2%B9%E2%99%A4%C2%B3!%5Bimage%5D( - https://user-images.githubusercontent.com/93821 375/230658076-4334affe-d594-42c9-962c-123af14519c1.jpeg)?m=1) - https://youtube.com/@White-Boy-Papalega.N.B www.tumblr.com Untitled 30 - 38 minutes @dark_rose@rainwizzard.blogger.com H - http.//www.rainwizzard.blog.spot.com @darkdose-75_rose@rainwizzard.blogger.com  -  http.//www.rainwizzard.blog.spot.com._4-do{text-align:center}._4-dp{font-size:24px;line-height:28px;margin:40px 0 20px}._4-dq{font-size:16px;line-height:28px;margin:20px 0}._4-dr{font-size:12px;line-height:20px} ._51u6{margin-bottom:-4px}._41uf,._41ug{display:inline-block;padding-right:14px;position:relative}._41uf .img{margin-left:1px;position:absolute;vertical-align:middle}._41ug .img{position:absolute;top:1px;vertical-align:middle} .fbx #pageFooter{margin:auto;width:auto}.hasLeftCol #pageFooter{background-color:#fff;clear:both;margin-left:180px}#pagefooter{border-top:0}#pageFooter{color:#737373;margin:0 auto;width:980px}#pageFooter a{text-decoration:none;white-space:nowrap}#pageFooter a:last-child{margin-right:0}#pageFooter a:hover{text-decoration:underline}#pageFooter .copyright{font-size:11px}#pageFooter .pageFooterLinkList{line-height:1.6;margin-left:-20px}#contentCurve{border-bottom:1px solid #dddfe2;font-size:1px;height:8px;margin-bottom:8px}.hasLeftCol #contentCurve{border:1px solid #ccc;border-top:none;position:relative} #globalContainer{margin:0 auto;position:relative;zoom:1}.fbx #globalContainer{width:981px}.sidebarMode #globalContainer{padding-right:205px}.sidebarMode .webkit #globalContainer .fixed_elem,.sidebarMode .webkit #globalContainer .fixed_always{margin:auto}.fbx #tab_canvas>div{padding-top:0}.fb_content{min-height:640px;padding-bottom:20px}.fbx .fb_content{padding-bottom:0}.skipto{display:none}.home .skipto{display:block} .fbPageBanner{position:relative;z-index:301}.hideBanner .fbPageBanner,.fixedBody .fbPageBanner{display:none}@media (min-width: 480px){.fbPageBannerInner{margin:auto;max-width:950px;min-width:920px}}.sidebarMode .fbPageBannerInner{left:-102px;position:relative} .fullScreen{height:100%;width:100%} #navLogin ._yl4{z-index:4}._yl4{position:relative;top:22px}._yl8{background-color:#f5f6f7;border:0 solid white;border-radius:3px;box-shadow:0 3px 8px rgba(0, 0, 0, .3);height:266px;padding-bottom:6px;text-align:center}._yl9{color:#7f7f7f;font-size:12px;line-height:14px;margin-bottom:10px;margin-top:16px}._yl8 ._yla{font-size:12px;height:28px;line-height:28px;min-width:68px}._yl4 ._yl7 .beeperNub{left:230px}._yl7._ylb{border:0 solid white;border-radius:3px;height:266px;right:-16px;top:35px;width:260px;z-index:1000} ._erp{background:white;border-radius:3px;padding:10px 16px 16px 16px}._err,._ers{font-size:12px;line-height:14px;text-align:left}._err input,._ers input{border:1px solid #d3d6db;font-size:14px;height:28px;margin:1px;padding:1px 3px;text-align:left;width:220px}._er_{color:#365899;font-size:12px;margin-bottom:10px;text-align:right}._erp ._es1{font-size:12px;height:28px;line-height:14px;margin-bottom:4px;padding:0 0;width:226px}._3jii{margin-top:1px;visibility:hidden} ._1pmx{background-color:#3b5998;border-bottom:1px solid #29487d;box-sizing:border-box;height:88px;width:100%}.tinyViewport ._1pmx{min-width:-webkit-max-content;min-width:max-content}._1pmx ._3jd8:not(:active){background-clip:padding-box;background-color:#5a73ad;border-color:rgba(0, 0, 0, .15)}._1pmx ._3jd8:hover:not(:active){background-color:#5069a3} ._sv8{line-height:24px} .localeSelectorList{align-items:center;display:flex;flex-wrap:wrap}.localeSelectorList a.showMore{background-color:#e9ebee;padding:0 6px 2px}.localeSelectorList a.showMore:hover{background-color:#6d84b4;color:#fff;text-decoration:none} .__tw{background:#fff;border:1px solid rgba(100, 100, 100, .4);border-radius:0 0 2px 2px;box-shadow:0 3px 8px rgba(0, 0, 0, .25);color:#1d2129;overflow:visible;position:absolute;top:38px;width:460px;z-index:-1}._1nxz .__tw,._dyn .__tw,._l35 .__tw{top:45px;z-index:1}.__tw .metadata{padding-top:3px}.__tw .jewelItemList{padding:4px 0}.__tw .empty,.__tw .jewelHighlight .empty{border:none;color:#90949c;padding:4px 8px 10px}.__tw .jewelHighlight li a{color:#1d2129;display:block;padding:4px 8px;text-decoration:none}.__tw .jewelHighlight li a:hover,.__tw .jewelHighlight li a:active,.__tw .jewelHighlight li a:focus{background-color:#f5f6f7;border-bottom:1px solid #dddfe2;border-top:1px solid #dddfe2;outline:none;padding-bottom:3px;padding-top:3px;text-decoration:none}.__tw .jewelHighlight a:hover span,.__tw .jewelHighlight a:active span,.__tw .jewelHighlight a:focus span,.__tw .jewelHighlight a:hover div,.__tw .jewelHighlight a:active div,.__tw .jewelHighlight a:focus div,.__tw .jewelHighlight li.selected a,.__tw .jewelHighlight li.selected .timestamp{color:#fff}.__tw .jewelHighlight li{border-top:1px solid #e6e6e6;cursor:pointer}.__tw .jewelHighlight li:first-child{border-top:none}.__tw li.jewelItemNew{background-color:#edf2fa}.__tw li>a,.__tw li>.anchorContainer>a{outline:none}.__tw .uiScrollableAreaWithShadow.contentAfter:after{content:none}.__tw li.jewelItemResponded{background:#fff9d7;color:#1d2129}.__tw .jewelLoading{display:block;margin:10px auto}.__tw .uiScrollableAreaContent>.jewelLoading:only-child{margin-bottom:9px}.__tw .jewelFooter .seeMoreCount{display:none;font-weight:600;padding:2px 0 0}.__tw .x_div{position:absolute;right:10px;top:58%;transition:margin-right 250ms;z-index:2}.__tw .jewelItemList{padding:0}.__tw .uiScrollableAreaContent{padding-bottom:1px}.__tw .beeperNub{background-image:url(/rsrc.php/v3/y-/r/VcstZr4fYTz.png);background-repeat:no-repeat;background-size:auto;background-position:-213px -251px;height:11px;position:absolute;top:-11px;width:20px}.__tw div.jewelHeader{background-clip:padding-box;background-color:#fff;border-bottom:solid 1px #dddfe2;border-top-left-radius:3px;border-top-right-radius:3px;padding:8px 12px 6px;position:relative;z-index:100}.__tw .jewelHeader h3>a,.__tw .jewelHeader h4>a{color:inherit;text-decoration:none}.__tw .jewelFooter a{background-color:#fff;border-bottom-left-radius:3px;border-bottom-right-radius:3px;border-top:1px solid #dddfe2;display:block;font-weight:600;padding:8px 12px;position:relative;text-align:center;z-index:100}.__tw .jewelFooter a:hover,.__tw .jewelFooter a:active,.__tw .jewelFooter a:focus{color:#365899;outline:none;text-decoration:underline}.__tw .jewelFooter a:hover .seeMoreCount,.__tw .jewelFooter a:active .seeMoreCount,.__tw .jewelFooter a:focus .seeMoreCount{color:gray}.__tw .jewelItemList{padding:0} ._cqp{font-size:18px;line-height:22px;padding:18px 0;text-align:center}._cqq{background-color:#fff;padding:22px 108px 26px;text-align:center}._cqq ._cqr{font-size:14px;height:36px;line-height:34px;margin:10px;margin-top:18px;text-align:center;width:150px}._cqs{margin:0 auto;width:612px}.fbx ._cqt#globalContainer{width:100%}._cqu{margin:0 auto;text-align:left;width:981px} html ._44mg{padding:6px 0;width:302px}html ._1kbt._1kbt{font-size:14px;padding:5px 8px;width:284px}#facebook ._97v- ._1kbt{border-radius:6px;font-size:17px;padding:14px 16px;width:330px}#facebook ._9ay4{border:1px solid #f02849}._9ay5{position:relative}._9ay6{bottom:16px;position:absolute;right:10px}#facebook ._9npi{background:none;border:0;box-shadow:none;float:left;font-size:17px;padding:0;width:300px}#facebook ._44mg ._9ay7{color:#f02849;font-family:SFProText-Regular, Helvetica, Arial, sans-serif;font-size:13px;line-height:16px;margin-top:8px;text-align:left}._9nyg{border:1px solid #dddfe2;color:#1d2129;height:22px;line-height:16px;vertical-align:middle;width:330px}._9nyh{border-color:#dddfe2;box-shadow:none;caret-color:none}#facebook ._9nyi{border-color:#1b74e4;box-shadow:0 0 0 2px #e7f3ff;caret-color:#1b74e4}._44mg ._9ay7 a{color:#f02849;font-weight:bold}._9ls7{position:relative}._9ls8{background:url(/rsrc.php/v3/yZ/r/je5FEJkU1_K.png)}._9ls9{background:url(/rsrc.php/v3/yk/r/swFqSxKYa5M.png)}._9lsa{border-radius:50%;bottom:-25px;height:28px;position:absolute;right:-8px;width:28px}._9lsa:hover{background-color:rgba(0, 0, 0, .05)}._9lsa:active{background-color:rgba(0, 0, 0, .15)}._9lsb{bottom:6px;height:16px;position:absolute;right:6px;width:16px} .menu_login_container table tr{vertical-align:top}.menu_login_container table tr td{padding:0 0 0 14px}.new_header_style.menu_login_container table tr td{padding:0 0 0 12px}.menu_login_container .html7magic{padding-bottom:4px}.menu_login_container .inputtext,.menu_login_container .inputpassword{border-color:#1d2a5b;margin:0;width:142px}.menu_login_container .login_form_label_field label,.menu_login_container .login_form_label_field a{color:#9cb4d8;font-weight:normal}.menu_login_container .login_form_label_field{padding-top:4px}.menu_login_container .html7magic label{color:#fff;font-weight:normal;padding-left:1px}#facebook .tetra_fonts .html7magic label{font-family:SFProText-Medium, Helvetica, Arial, sans-serif}#facebook .tetra_fonts .login_form_input_box{font-family:SFProText-Regular, Helvetica, Arial, sans-serif}#facebook .tetra_fonts .login_form_input_box::-webkit-input-placeholder{color:#8d949e}#facebook .tetra_fonts .login_form_login_button input{font-family:SFProText-Bold, Helvetica, Arial, sans-serif;font-weight:bold}#facebook .tetra_fonts .login_form_label_field a{color:#fff;font-family:SFProText-Regular, Helvetica, Arial, sans-serif}.new_header_style .login_form_label_field{text-align:right}.new_header_style.menu_login_container table tr td.login_form_label_field{padding-top:4px}.new_header_style .login_form_label_field a{font-size:13px;line-height:20px}.new_header_style .inputtext,.new_header_style .inputpassword{border-color:#082b61;border-radius:6px;box-sizing:border-box;font-size:13px;line-height:20px;margin:0;padding:8px 12px;width:194px}.white_background.new_header_style .inputtext,.white_background.new_header_style .inputpassword{width:210px}.new_header_style.menu_login_container{width:412px}.white_background.new_header_style.menu_login_container{width:444px}.new_blue_header .inputtext,.new_blue_header .inputpassword{border:none}.new_header_style .login_form_login_button input{font-size:18px;line-height:20px;padding:6px 26px}.new_header_style .login_form_login_button{border-radius:6px}.new_blue_header .login_form_login_button{background-color:#0e52b0;border:none}.menu_login_container #email{direction:ltr}.login_form_standalone_labels .inputtext,.login_form_standalone_labels .inputpassword{border-color:#96a6c5;font-size:16px;padding:6px;width:250px}.login_form_standalone_labels label{color:#1d2a5b;font-size:13px;font-weight:normal}.login_form_standalone_labels .login_form_label_field a{color:#365899;font-size:13px}.login_form_standalone_labels td.html7magic{text-align:right}.login_form_standalone_labels .uiButton input{font-size:13px;padding:3px 25px 5px}table.login_form_standalone_labels tr td{height:30px;padding:0;vertical-align:middle} .loggedout_menubar_container{height:82px;min-width:980px}.newHeaderMenuBar .loggedout_menubar_container{height:90px}.loggedout_menubar{margin:0 auto;padding-top:13px;width:980px}.newHeaderMenuBar .loggedout_menubar{padding-bottom:8px;padding-top:20px}.loggedout_menubar .fb_logo{margin-top:17px}.newHeaderMenuBar .loggedout_menubar .fb_logo{margin-top:4px}.loggedout_menubar .fb_icon_logo{margin-top:12px}@media (-webkit-min-device-pixel-ratio: 2),(min-resolution: 2dppx){.loggedout_menubar i.fb_logo{background-image:url(/rsrc.php/v3/y4/r/gf6iHxsw8zm.png);background-position:0 0;background-size:100% 100%}}.loggedout_menubar label.menu_login_show_link{color:#9cb4d8;position:relative;top:19px} ._lwx{position:relative} .signupBanner div.signup_bar_container{background-color:transparent}.signupBanner .signup_box{margin:0 auto;padding:0;position:relative;width:980px}.signupBanner .signup_btn{left:180px;position:absolute;top:-46px}.signupBanner .signup_btn_thickbar{left:180px;position:absolute;top:-70px}.signup_area{margin-top:23px}.timelineLayoutLoggedOut .signup_btn{left:250px} .signupBanner .signup_bar_container{background-color:transparent}.signupBanner .signup_box{margin:0 auto;position:relative;width:980px}.signupBanner .signup_btn{left:180px;padding-bottom:2px;padding-top:2px;position:absolute;top:-50px}.signupBanner .signup_btn_thickbar{left:180px;position:absolute;top:-70px}.signup_area{margin-top:23px}.timelineLayoutLoggedOut .signup_btn{left:250px} ._53jh{background-color:#3b5998;background-image:linear-gradient(#4e69a2, #3b5998 50%);border-bottom:1px solid #133783;min-height:42px;position:relative;z-index:1}._53jh._8f2f{background-color:#1877f2;background-image:none;border-bottom:none}.tinyViewport ._53jh{min-width:-webkit-max-content;min-width:max-content} ._52ju{text-align:left}._52jv{text-align:center}._52jw{text-align:right} .uiBoxGray{background-color:#f2f2f2;border:1px solid #ccc}.uiBoxDarkgray{color:#ccc;background-color:#333;border:1px solid #666}.uiBoxGreen{background-color:#d1e6b9;border:1px solid #629824}.uiBoxLightblue{background-color:#edeff4;border:1px solid #d8dfea}.uiBoxRed{background-color:#ffebe8;border:1px solid #dd3c10}.uiBoxWhite{background-color:#fff;border:1px solid #ccc}.uiBoxYellow{background-color:#fff9d7;border:1px solid #e2c822}.uiBoxOverlay{background:rgba(255, 255, 255, .85);border:1px solid #3b5998;border:1px solid rgba(59, 89, 153, .65);zoom:1}.noborder{border:none}.topborder{border-bottom:none;border-left:none;border-right:none}.bottomborder{border-left:none;border-right:none;border-top:none}.dashedborder{border-style:dashed} .pas{padding:5px}.pa8{padding:8px}.pam{padding:10px}.pa16{padding:16px}.pal{padding:20px}.pts{padding-top:5px}.pt8{padding-top:8px}.ptm{padding-top:10px}.pt16{padding-top:16px}.ptl{padding-top:20px}.prs{padding-right:5px}.pr8{padding-right:8px}.prm{padding-right:10px}.pr16{padding-right:16px}.prl{padding-right:20px}.pbs{padding-bottom:5px}.pb8{padding-bottom:8px}.pbm{padding-bottom:10px}.pb16{padding-bottom:16px}.pbl{padding-bottom:20px}.pls{padding-left:5px}.pl8{padding-left:8px}.plm{padding-left:10px}.pl16{padding-left:16px}.pll{padding-left:20px}.phs{padding-left:5px;padding-right:5px}.ph8{padding-left:8px;padding-right:8px}.phm{padding-left:10px;padding-right:10px}.ph16{padding-left:16px;padding-right:16px}.phl{padding-left:20px;padding-right:20px}.pvs{padding-top:5px;padding-bottom:5px}.pv8{padding-bottom:8px;padding-top:8px}.pvm{padding-top:10px;padding-bottom:10px}.pv16{padding-bottom:16px;padding-top:16px}.pvl{padding-top:20px;padding-bottom:20px}.mas{margin:5px}.ma8{margin:8px}.mam{margin:10px}.ma16{margin:16px}.mal{margin:20px}.mts{margin-top:5px}.mt8{margin-top:8px}.mtm{margin-top:10px}.mt16{margin-top:16px}.mtl{margin-top:20px}.mrs{margin-right:5px}.mr8{margin-right:8px}.mrm{margin-right:10px}.mr16{margin-right:16px}.mrl{margin-right:20px}.mbs{margin-bottom:5px}.mb8{margin-bottom:8px}.mbm{margin-bottom:10px}.mb16{margin-bottom:16px}.mbl{margin-bottom:20px}.mls{margin-left:5px}.ml8{margin-left:8px}.mlm{margin-left:10px}.ml16{margin-left:16px}.mll{margin-left:20px}.mhs{margin-left:5px;margin-right:5px}.mh8{margin-left:8px;margin-right:8px}.mhm{margin-left:10px;margin-right:10px}.mh16{margin-left:16px;margin-right:16px}.mhl{margin-left:20px;margin-right:20px}.mvs{margin-top:5px;margin-bottom:5px}.mv8{margin-bottom:8px;margin-top:8px}.mvm{margin-top:10px;margin-bottom:10px}.mv16{margin-bottom:16px;margin-top:16px}.mvl{margin-top:20px;margin-bottom:20px} .fss{font-size:9px}.fsm{font-size:12px}.fsl{font-size:14px}.fsxl{font-size:16px}.fsxxl{font-size:18px}.fwn{font-weight:normal}.fwb{font-weight:600}.fcb{color:#333}.fcg{color:#90949c}.fcw{color:#fff} .uiButton{border-radius:2px;cursor:pointer;display:inline-block;font-size:12px;-webkit-font-smoothing:antialiased;font-weight:bold;line-height:18px;padding:2px 6px;text-align:center;text-decoration:none;text-shadow:none;vertical-align:top;white-space:nowrap}.uiButton,.uiButtonSuppressed:active,.uiButtonSuppressed:focus,.uiButtonSuppressed:hover{background-color:#f5f6f7;border:1px solid #ccd0d5}.uiButton+.uiButton{margin-left:4px}.uiButton:hover{background-color:#ebedf0;text-decoration:none}.uiButton:active,.uiButtonDepressed{background-color:#dddfe2;border-color:#bec3c9}.uiButton .img{margin-top:3px;overflow:hidden;vertical-align:top}.uiButtonLarge .img{margin-top:4px}.uiButton .customimg{margin-top:1px}.uiButtonText,.uiButton input{background:none;border:0;color:#4b4f56;cursor:pointer;display:inline-block;font-family:Helvetica, Arial, sans-serif;font-size:12px;font-weight:bold;line-height:18px;margin:0;padding:0;white-space:nowrap}.uiButtonOverlay,.uiButtonOverlay:hover{background-clip:padding-box;background-color:rgba(255, 255, 255, .8);background-image:none;border-color:#a5a5a5;border-color:rgba(0, 0, 0, .35);border-radius:2px;position:relative}.uiButtonOverlay:focus,.uiButtonOverlay:active{background-color:#f5f6f7;background-color:rgba(249, 250, 252, .9);border-color:#365899;border-color:rgba(59, 89, 152, .5)}form.async_saving .uiButton.uiButtonOverlay,.uiButtonOverlay.uiButtonDisabled,.uiButtonOverlay.uiButtonDisabled:active,.uiButtonOverlay.uiButtonDisabled:focus,.uiButtonOverlay.uiButtonDisabled:hover{background-color:rgba(255, 255, 255, .8);border-color:#ccc;border-color:rgba(180, 180, 180, .8)}.uiButtonOverlay.uiButtonDepressed{background-color:rgba(0, 0, 0, .05)}.uiButtonOverlay:before{background-color:rgba(0, 0, 0, .02);bottom:0;content:'';left:0;position:absolute;right:0;top:0}.uiButtonOverlay:hover:before{background-color:rgba(0, 0, 0, .08)}.uiButtonSpecial{background-color:#42b72a;border-color:#42b72a}.uiButtonSpecial:hover{background-color:#36a420;border-color:#36a420}.uiButtonSpecial:active,.uiButtonSpecial.uiButtonDepressed{background-color:#2b9217;border-color:#2b9217}form.async_saving .uiButton.uiButtonSpecial,.uiButtonSpecial.uiButtonDisabled,.uiButtonSpecial.uiButtonDisabled:active,.uiButtonSpecial.uiButtonDisabled:focus,.uiButtonSpecial.uiButtonDisabled:hover{background-color:#ace0a2;border-color:#ace0a2}.uiButtonConfirm{background-color:#4267b2;border-color:#29487d}.uiButtonConfirm:hover{background-color:#365899;border-color:#29487d}.uiButtonConfirm:active,.uiButtonConfirm.uiButtonDepressed{background-color:#29487d;border-color:#29487d}form.async_saving .uiButton.uiButtonConfirm,.uiButtonConfirm.uiButtonDisabled,.uiButtonConfirm.uiButtonDisabled:active,.uiButtonConfirm.uiButtonDisabled:focus,.uiButtonConfirm.uiButtonDisabled:hover{background-color:#9cb4d8;border-color:#9cb4d8}form.async_saving .uiButton.uiButtonSpecial .uiButtonText,form.async_saving .uiButton.uiButtonSpecial input,form.async_saving .uiButton.uiButtonConfirm .uiButtonText,form.async_saving .uiButton.uiButtonConfirm input,.uiButtonSpecial .uiButtonText,.uiButtonSpecial input,.uiButtonSpecial.uiButtonDisabled .uiButtonText,.uiButtonSpecial.uiButtonDisabled input,.uiButtonConfirm .uiButtonText,.uiButtonConfirm input,.uiButtonConfirm.uiButtonDisabled .uiButtonText,.uiButtonConfirm.uiButtonDisabled input{color:#fff}form.async_saving .uiButton,.uiButtonDisabled,.uiButtonDisabled:active,.uiButtonDisabled:focus,.uiButtonDisabled:hover{background-color:#f5f6f7;border-color:#dddfe2}form.async_saving .uiButton .img,.uiButtonDisabled .img{opacity:.5}form.async_saving .uiButtonText,form.async_saving .uiButton input,.uiButtonDisabled .uiButtonText,.uiButtonDisabled input{color:#bec3c9}form.async_saving .uiButton,form.async_saving .uiButtonText,form.async_saving .uiButton input,.uiButtonDepressed,.uiButtonDepressed .uiButtonText,.uiButtonDepressed input,.uiButtonDisabled,.uiButtonDisabled .uiButtonText,.uiButtonDisabled input{cursor:default}.uiButtonDepressed:not(.uiButtonSpecial):not(.uiButtonConfirm) .uiButtonText,.uiButtonDepressed:not(.uiButtonSpecial):not(.uiButtonConfirm) input{color:#4080ff}.uiButtonLarge,.uiButtonLarge .uiButtonText,.uiButtonLarge input{font-size:13px;line-height:19px}.uiButtonSuppressed{background:none;border-color:transparent}.uiButtonNoText .img{margin-left:-1px;margin-right:-1px}.uiButtonNoText input{vertical-align:top} .uiHeader h1{color:#162643;font-size:20px}.uiHeader h2{color:#162643;font-size:16px}.uiHeader h2 a{color:#162643}.uiHeader h3,.uiHeader h4{color:#333;font-size:12px}.uiHeader h5,.uiHeader h6{color:#666}.uiHeader .uiHeaderTitle{outline:none}.uiHeaderWithImage .uiHeaderTop{position:relative}.uiHeaderWithImage .uiHeaderTitle{padding-left:22px}.uiHeaderImage{left:0;position:absolute}.uiHeader h2 .uiHeaderImage{top:2px}.uiHeaderTopBorder{border-top:1px solid #aaa;padding-top:.5em}div.uiHeaderTopBorder{margin-left:0}.uiHeaderTopAndBottomBorder{border-bottom:1px solid #e9e9e9;border-top:1px solid #aaa;padding:5px 0}.uiHeaderMiddleBorder{border-bottom:1px solid #ccc;height:.8em;margin:.5em 0 1.5em 0;position:relative}.uiHeaderMiddleBorder .uiHeaderTitle,.uiHeaderMiddleBorder .uiHeaderActions{background-color:#fff;position:absolute;top:0}.uiHeaderMiddleBorder .uiHeaderTitle{left:0;padding-right:.5em}.uiHeaderMiddleBorder .uiHeaderActions{padding-left:.5em;right:0}.uiHeaderMiddleBorder .uiButton{margin-top:-2px}.uiHeaderBottomBorder{border-bottom:1px solid #aaa;padding-bottom:.5em}.uiHeaderPage{padding:6px 0 16px}.uiHeaderPage .uiHeaderTitle{line-height:20px;min-height:20px;padding-bottom:2px;vertical-align:bottom}.uiHeaderPage .uiHeaderActions{margin-top:-1px}.uiHeaderPage .uiHeaderTop .fsl{margin-top:3px}.uiHeaderNav{border-color:#ebedf0;margin:8px 0 0 6px;padding:7px 6px 3px 5px}.uiHeaderNavEmpty{padding-top:6px}.uiHeaderNav h4{color:#7f7f7f}.uiHeaderSection,.uiSideHeader{background-color:#f5f6f7;border-bottom:none;border-top:solid 1px #e9ebee;padding:4px 6px 5px} .uiInterstitial{border-radius:4px;margin-left:auto;margin-right:auto}.uiInterstitialSmall{width:445px}.uiInterstitialLarge{width:555px}.uiInterstitialXLarge{width:620px}.uiInterstitial .interstitialHeader{border-color:#ccc;padding-bottom:.5em}.fullBleed .interstitialHeader{margin:0;padding:4px 12px 10px}.uiInterstitialContent{margin-bottom:15px}.fullBleed .uiInterstitialContent{margin:0;padding:0}.uiInterstitialBar{border-bottom-right-radius:3px;border-bottom-left-radius:3px;-webkit-border-bottom-left-radius:3px;-webkit-border-bottom-right-radius:3px;line-height:16px;padding:8px 10px}div.uiInterstitialWithStripes{background:transparent url(/rsrc.php/v3/y9/r/y7MG8IZpiC8.gif) repeat-x;padding-top:15px} ._2qgu._2qgu{border-radius:50%;overflow:hidden}._2s25._2s25._606w._606w:after,._606w:after{border-radius:50%} a._p{display:block} ._4jy0{border:1px solid;border-radius:2px;box-sizing:content-box;font-size:12px;-webkit-font-smoothing:antialiased;font-weight:bold;justify-content:center;padding:0 8px;position:relative;text-align:center;text-shadow:none;vertical-align:middle}.segoe ._4jy0{font-weight:600}._4jy0:before{content:'';display:inline-block;height:20px;vertical-align:middle}html ._4jy0:focus{box-shadow:0 0 1px 2px rgba(88, 144, 255, .75), 0 1px 1px rgba(0, 0, 0, .15);outline:none}._19_u ._4jy0:focus,._4jy0._5f0v:focus{box-shadow:none}._4jy0{transition:200ms cubic-bezier(.08,.52,.52,1) background-color, 200ms cubic-bezier(.08,.52,.52,1) box-shadow, 200ms cubic-bezier(.08,.52,.52,1) transform}._4jy0:active{transition:none}.mac ._4jy0:not(._42fr):active{box-shadow:none;transform:scale(.98)}._4jy0 .img{bottom:1px;position:relative;vertical-align:middle}form.async_saving ._4jy0 .img,a.async_saving._4jy0 .img,._4jy0._42fr .img{opacity:.5}._517h,._59pe:focus,._59pe:hover{background-color:#f5f6f7;border-color:#ccd0d5;color:#4b4f56}._64lx ._517h,._64lx ._59pe:focus,._64lx ._59pe:hover{background-color:#eff1f3;border-color:#bec3c9}._517h:hover{background-color:#ebedf0}._517h:active,._517h._42fs{background-color:#dddfe2;border-color:#bec3c9}form.async_saving ._517h,a.async_saving._517h,._517h._42fr{background-color:#f5f6f7;border-color:#dddfe2;color:#bec3c9}._517h._42fs{color:#4080ff}._4jy1,._9w8q,._4jy2{color:#fff}._4jy1{background-color:#4267b2;border-color:#4267b2}._4jy1:hover{background-color:#365899;border-color:#365899}._4jy1:active,._4jy1._42fs{background-color:#29487d;border-color:#29487d}form.async_saving ._4jy1,a.async_saving._4jy1,._4jy1._42fr{background-color:#9cb4d8;border-color:#9cb4d8}._4jy2{background-color:#42b72a;border-color:#42b72a}._4jy2:hover{background-color:#36a420;border-color:#36a420}._4jy2:active,._4jy2._42fs{background-color:#2b9217;border-color:#2b9217}form.async_saving ._4jy2,a.async_saving._4jy2,._4jy2._42fr{background-color:#ace0a2;border-color:#ace0a2}._9w8q{background-color:#fa3e3e;border-color:#fa3e3e}._9w8q:hover{background-color:#db1d24;border-color:#db1d24}._9w8q:active,._9w8q._42fs{background-color:#c70b11;border-color:#c70b11}form.async_saving ._9w8q,a.async_saving._9w8q,._9w8q._42fr{background-color:#f77c7c;border-color:#f77c7c}._59pe,form.async_saving ._59pe,a.async_saving._59pe,._59pe._42fr{background:none;border-color:transparent}._517i,._517i._42fr:active,._517i._42fr._42fs{height:18px;line-height:18px}._4jy3,._4jy3._42fr:active,._4jy3._42fr._42fs{line-height:22px}._4jy4,._4jy4._42fr:active,._4jy4._42fr._42fs{line-height:26px;padding:0 10px}._4jy5,._4jy5._42fr:active,._4jy5._42fr._42fs{line-height:34px;padding:0 16px}._4jy6,._4jy6._42fr:active,._4jy6._42fr._42fs{line-height:42px;padding:0 24px}._51xa ._4jy0{border-radius:0;display:inline-block;margin:0!important;margin-left:-1px!important;position:relative;z-index:1}._51xa>._4jy0:first-child,._51xa>:first-child ._4jy0{border-radius:2px 0 0 2px;margin-left:0!important}._51xa>._4jy0:last-child,._51xa>:last-child ._4jy0{border-radius:0 2px 2px 0}._51xa>._4jy0:only-child,._51xa>:only-child ._4jy0{border-radius:2px}._51xa ._4jy0._42fr{z-index:0}._51xa ._4jy0._4jy1,._51xa ._4jy0._9w8q,._51xa ._4jy0._4jy2{z-index:2}._51xa ._4jy0:focus{z-index:3}._51xa ._4jy1+.uiPopover>._4jy1:not(:focus):after{background-color:#f5f6f7;bottom:-1px;content:'';display:block;left:-1px;position:absolute;top:-1px;width:1px}._4jy0._52nf{cursor:default}._9c6._9c6{background-clip:padding-box;border-color:rgba(0, 0, 0, .4)}._3y89 ._4jy0{border-bottom-width:0;border-top-width:0}._3y89>._4jy0:first-child,._3y89>:first-child ._4jy0{border-left-width:0;border-radius:1px 0 0 1px}._3y89>._4jy0:last-child,._3y89>:last-child ._4jy0{border-radius:0 1px 1px 0;border-right-width:0}._6n1z._4jy6,._6n1z._4jy6._42fr:active,._6n1z._4jy6._42fr._42fs{padding:0 0}._6n1z._517h,._6n1z._59pe:focus,._6n1z._59pe:hover{background-color:#fff;border-color:transparent} .UIPage_LoggedOut .UIFullPage_Container,.UIPage_LoggedOut .UIStandardFrame_Container{padding-bottom:46px;padding-top:46px;width:auto}.UIPage_LoggedOut .fbPhotosGrid .photoDetails{width:inherit} ._86k6{color:#1c1e21;font-family:SFProText-Regular, Segoe UI, Arial, sans-serif!important;font-size:13px;line-height:16px;white-space:nowrap}@media only screen and (max-width: 768px){._86k6{display:none}} ._86k9{box-sizing:border-box;display:block;margin-left:auto;margin-right:auto;margin-top:16px;max-width:1200px}._8e0v{padding:32px 0}._8e0w{align-items:flex-start;border-top:1px solid #ccd0d5;display:flex;justify-content:space-between;padding:32px 0}@media only screen and (max-width: 768px){._86k9{padding:16px;width:100%}._8e0v{display:none}} ._86k7{color:#8d949e;display:inline-block;padding-right:20px;padding-top:0}._86k7 li>a{color:#1c1e21;font-family:SFProText-Semibold, Segoe UI, Arial!important;font-size:13px}._86k8.localeSelectorList.uiList{padding-top:0}@media only screen and (max-width: 768px){._86k7{display:block;margin-bottom:0;max-width:100%;padding-right:0;width:100%}._86k8.localeSelectorList.uiList>li{display:inline-block;font-size:12px;font-weight:bold;padding-left:0;text-align:center;width:50%}._86k8>li>a{color:#8d8b8a;font-weight:normal}._86jz{border:1px solid #365899;border-radius:3px;color:#1479fb;display:block;font-size:large;height:18px;line-height:17px;margin:0 auto;text-align:center;width:18px}} ._86jx{display:inline-block;font-family:SFProText-Semibold, Segoe UI, Arial!important;font-size:13px;line-height:16px;padding-right:16px}._86jx:last-child{padding-right:0}._86jx>a{color:#1c1e21}@media only screen and (max-device-width: 768px){._86jy{display:none}} ._4b21{background-color:#fff;height:60px;margin:0 auto;padding-bottom:16px;position:relative;width:980px}@media only screen and (max-width: 500px){._4b21{width:100%}}._40q1{background-color:#fff}._5wct{color:#000;display:inline;font-family:HelveticaNeue-Light, Helvetica Neue Light, Helvetica Neue, Helvetica, Arial, Lucida Grande, sans-serif;font-size:24px;line-height:32px;max-width:900px;position:absolute;top:16px}._4b23{margin-right:12px;margin-top:10px}._2084{display:inline;float:right;font-size:14px;line-height:87px}#facebook ._1m39._1m3f{background:white;border:1px solid #4778ff;color:#4778ff}#facebook ._1m39._1m3f:active{background-color:#f5f6f7} .Work_UIPage_LoggedOut{background-color:#fff} ._4ki>li{border-width:0 0 0 1px;display:inline-block}._4kg>li{border-width:1px 0 0 0}._509->li{vertical-align:top}._509_>li{vertical-align:middle}._50a0>li{vertical-align:bottom}.uiList>li:first-child{border-width:0}._4ks>li{border-color:#ebedf0;border-style:solid}._4kt>li{border-color:#ccc;border-style:solid}._4ku>li{border-color:#aaa;border-style:solid}._4of{color:#365899;list-style-type:square;margin-left:12px}._7lda{list-style-type:disc;margin-left:16px}._7lda>._7ldb{text-indent:-2px}._4ki._703>li{padding-left:20px;padding-right:20px}._4ki._704>li{padding-left:5px;padding-right:5px}._4ki._6-j>li{padding-left:10px;padding-right:10px}._4ki._6-i>li{padding-right:0}._4kg._704>li{padding-top:5px;padding-bottom:5px}._4kg._6-j>li{padding-top:10px;padding-bottom:10px}._4kg._703>li{padding-top:20px;padding-bottom:20px}._4kg._6-i>li{padding-bottom:0}._4kg._6-h>li:first-child{padding-top:0}._4kg._6-h>li:last-child{padding-bottom:0}._4ki._6-h>li:first-child{padding-left:0}._4ki._6-h>li:last-child{padding-right:0} ._8tm{padding:0}._2phz{padding:4px}._2ph-{padding:8px}._2ph_{padding:12px}._2pi0{padding:16px}._2pi1{padding:20px}._40c7{padding:24px}._2o1j{padding:36px}._6buq{padding-bottom:0;padding-top:0}._2pi2{padding-bottom:4px;padding-top:4px}._2pi3{padding-bottom:8px;padding-top:8px}._2pi4{padding-bottom:12px;padding-top:12px}._2pi5{padding-bottom:16px;padding-top:16px}._2pi6{padding-bottom:20px;padding-top:20px}._2o1k{padding-bottom:24px;padding-top:24px}._2o1l{padding-bottom:36px;padding-top:36px}._6bua{padding-left:0;padding-right:0}._2pi7{padding-left:4px;padding-right:4px}._2pi8{padding-left:8px;padding-right:8px}._2pi9{padding-left:12px;padding-right:12px}._2pia{padding-left:16px;padding-right:16px}._2pib{padding-left:20px;padding-right:20px}._2o1m{padding-left:24px;padding-right:24px}._2o1n{padding-left:36px;padding-right:36px}._iky{padding-top:0}._2pic{padding-top:4px}._2pid{padding-top:8px}._2pie{padding-top:12px}._2pif{padding-top:16px}._2pig{padding-top:20px}._2owm{padding-top:24px}._div{padding-right:0}._2pih{padding-right:4px}._2pii{padding-right:8px}._2pij{padding-right:12px}._2pik{padding-right:16px}._2pil{padding-right:20px}._31wk{padding-right:24px}._2phb{padding-right:32px}._au-{padding-bottom:0}._2pim{padding-bottom:4px}._2pin{padding-bottom:8px}._2pio{padding-bottom:12px}._2pip{padding-bottom:16px}._2piq{padding-bottom:20px}._2o1p{padding-bottom:24px}._4gao{padding-bottom:32px}._1cvx{padding-left:0}._2pir{padding-left:4px}._2pis{padding-left:8px}._2pit{padding-left:12px}._2piu{padding-left:16px}._2piv{padding-left:20px}._2o1q{padding-left:24px}._2o1r{padding-left:36px} .sp_Awgqz7K4lHq{background-image:url(/rsrc.php/v3/y-/r/VcstZr4fYTz.png);background-size:auto;background-repeat:no-repeat;display:inline-block;height:20px;width:20px}.sp_Awgqz7K4lHq.sx_a37d90{width:282px;height:250px;background-position:0 0}.sp_Awgqz7K4lHq.sx_7df8b7{background-position:-171px -251px}.sp_Awgqz7K4lHq.sx_98f749{background-position:-192px -251px}.sp_Awgqz7K4lHq.sx_976ed2{width:105px;height:40px;background-position:0 -286px}.sp_Awgqz7K4lHq.sx_b035c3{height:11px;background-position:-213px -251px}.sp_Awgqz7K4lHq.sx_f315b2{width:16px;height:16px;background-position:-106px -286px}.sp_Awgqz7K4lHq.sx_08e58c{width:16px;height:16px;background-position:-123px -286px}.sp_Awgqz7K4lHq.sx_d7bd95{width:5px;height:14px;background-position:-145px -286px}.selected .sp_Awgqz7K4lHq.sx_d7bd95{background-position:-140px -286px}.sp_Awgqz7K4lHq.sx_bbc862{width:9px;height:5px;background-position:-234px -251px}.sp_Awgqz7K4lHq.sx_55d19b{width:170px;height:34px;background-position:0 -251px}.sp_Awgqz7K4lHq.sx_60b650{width:12px;height:12px;background-position:-171px -272px}/*FB_PKG_DELIM*/ #bootloader_3Bb3Baa{height:42px;}.bootloader_3Bb3Baa{display:block!important;} https://account.rogers.com/?from_ts=for posted by Baby Papalegba @ June 21, 2023  3 comments   3 Comments: At June 21, 2023 at 9:05 PM , Blogger Baby Papalegba said... Get royolties too    At June 21, 2023 at 9:59 PM , Blogger Baby Papalegba said... Own Your Word against dublication and reproduction that's epic like a super star does }<write something with out there promissory approval what happens {    At June 30, 2023 at 2:51 PM , Blogger Baby Papalegba said... https://chodum91.blogspot.com/2023/06/google-content.html?spref=fb&fbclid=IwAR0L0BwQRtAkf6_ot8HPmUZzr0mGDl0TVNxEw3Nv8w7bDVAnS8NO1HJexnQ    Post a Comment  Subscribe to Post Comments [Atom]  << Home  About Me My Photo Name: Baby Papalegba Location: Ottawa, Ontario , Canada View my complete profile  Previous Posts Powered by Blogger  Subscribe to Posts [Atom]   )Chodum91-patch-6 ...https://embed.tumblr.com/embed/post/t:iPRP096YDH4tAP9ETV9_tg/720127509506736128/v2https://www.tumblr.com/darkdose-75/719933067816534016/245040906-ea6c92a1-4c9f-43b1-a4c0-bce44758b0bejpg?source=share -[<!DOCTYPE html>[Chodum91-patch-6](https://developers.google.com/speed/libraries)<html lang=\"en\"> <head>  <meta charset=\"UTF-8\">  <title>READ JSON Example (getJSON)</title>  <script type=\"text/javascript\" src=\"https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js\"></script> Papalegba.org Papa.Legba.N.B. [ ](https://chodum91.blogspot.com/2023/06/google-content.html?spref=fb&fbclid=IwAR1ZbUO1DJ61e7HmSaCGWy31OK6394QPyu4CRI0fvbdZk0SdVIBDygBp46s)AMMA •^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• MAMA April 11, 2023 •^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}  } menu {•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• background: #fff; border-radius: 4px; color: #202124; cursor: var(--hterm-mouse-cursor-pointer); display: none; filter: drop-shadow(0 1px 3px #3C40434D) drop-shadow(0 4px 8px #3C404326); margin: 0; padding: 8px 0; position: absolute; transition-duration: 200ms; }(function( ¹♤³ www.rainwizzard@b logspot.com ¹♤³^^^•~}{0.0}{~•^^^••^^^•~}{0.0}{~•^^^••^^^•~}{0.0}){^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}  _{_~_•^^^• ¹♤³ www.rainwizzard@blogspot.com ¹♤³^^^•~}{0.0}{~•^^^••^^^•~}{0.0}{~•^^^••^^^•~}{0.0}var hasFrame = window.parent!=window, Aerial view of shipping containers. scripts = document.getElementsByTagName('script'), current = scripts[scripts.length-1], config = current.getAttribute('data-config'), head = document.getElementsByTagName(\"head\")[0], dest = location.href.replace(/scmplayer\\=true/g, 'scmplayer=false'), destHost = dest.substr(0,dest.indexOf('/',10)), scm = current.getAttribute('src').replace(/script\\.js.*/g,'scm.html?03022013')+'#'+dest, scmHost = scm.substr(0,scm.indexOf('/',10)), isOutside = !hasFrame || location.href.indexOf(\"scmplayer=true\")>0, postMessage = function(msg){ return window.top.document.getElementById('scmframe') .contentWindow.postMessage(msg,scmHost); }, postFactory = function(obj,keys){ var keys = keys.split(','), post = function(key){ return function(arg){ var argStr = ''; if(typeof(arg)!='undefined') argStr = (key.match(/(play|queue)/) ? 'new Song(':'(') + JSON.stringify(arg)+')'; postMessage('SCM.'+key+'('+argStr+')'); } }; for(var i=0;i', all[0] ); return v > 4 ? v : undef; })(), isMobile = navigator.userAgent.match(/iPad|iPhone|Android|Blackberry/i), init = function(){ if(!document.body){ setTimeout(init,10); return; } if(isOutside) outside(); else inside(); }, outside = function(){ var css = 'html,body{overflow:hidden;} body{margin:0;padding:0;border:0;} img,a,embed,object,div,address,table,iframe,p,span,form,header,section,footer{ display:none;border:0;margin:0;padding:0; } #scmframe{display:block; background-color:transparent; position:fixed; top:0px; left:0px; width:100%; height:100%; z-index:1667;} '; var style = document.createElement('style'); style.type = 'text/css'; style.id = 'scmcss'; if(style.styleSheet) style.styleSheet.cssText = css; else style.appendChild(document.createTextNode(css)); head.appendChild(style); /* while(head.firstChild.id!=\"scmcss\") head.removeChild(head.firstChild); */ var scmframe = document.createElement('iframe'); scmframe.frameBorder = 0; scmframe.id = \"scmframe\"; scmframe.allowTransparency = true; scmframe.src = scm; document.body.insertBefore(scmframe,document.body.firstChild); addEvent(window,'load',function() { setTimeout(function(){ while(document.body.firstChild!=scmframe) document.body.removeChild(document.body.firstChild); while(document.body.lastChild!=scmframe) document.body.removeChild(document.body.lastChild); },0); }); //fix frame height in IE addEvent(window,'resize',function(){ scmframe.style.height = (function(){ if( typeof( window.innerHeight ) == 'number' ) return window.innerHeight; else if( document.documentElement && document.documentElement.clientHeight ) return document.documentElement.clientHeight; else if( document.body && document.body.clientHeight ) return document.body.clientHeight; })(); }); //pushState and hash change detection var getPath = function(){ return location.href.replace(/#.*/,''); }, path = getPath(), hash = location.hash; setInterval(function(){ if(getPath()!=path){ path = getPath(); window.scminside.location.replace(path); } if(location.hash != hash){ hash = location.hash; window.scminside.location.hash = hash; } },100); }, inside = function(){ //change title window.top.document.title = document.title; //fix links var filter = function(host){ host = host.replace(/blogspot.[a-z.]*/i,'blogspot.com'); host = host.replace(/^(http(s)?:\\/\\/)?(www.)?/i,''); return host; }; addEvent(document.body,'click',function(e){ var tar = e.target; while(!tar.tagName.match(/^(a|area)$/i) && tar!=document.body) tar = tar.parentNode; if(tar.tagName.match(/^(a|area)$/i) && !tar.href.match(/.(jpg|png)$/i) && //ignore picture link !tar.href.match(/^javascript:/) //ignore javascript link ){ if(tar.href.indexOf('#')==0){ //hash if(tar.href != \"#\"){ window.top.scminside = window; window.top.location.hash = location.hash; e.preventDefault(); } }else if(tar.title.match(/^(SCM:|\\[SCM\\])/i)){ //SCM Play link var title = tar.title.replace(/^(SCM:|\\[SCM\\])( )?/i,''); var url = tar.href; SCM.play({title:title,url:url}); e.preventDefault(); }else if(tar.href.match(/\\.css$/)){ //auto add skin window.open('http://scmplayer.net/#skin='+tar.href,'_blank'); window.focus(); e.preventDefault(); }else if(filter(tar.href).indexOf(filter(location.host))==-1 ){ if(tar.href.match(/^http(s)?/)){ //external links window.open(tar.href,'_blank'); window.focus(); e.preventDefault(); } }else if(history.pushState){ //internal link & has pushState //change address bar href var url = filter(tar.href).replace(filter(destHost),''); window.top.scminside = window; window.top.history.pushState(null,null,url); e.preventDefault(); } } }); addEvent(window,'load',function() { }); }; //SCM interface var SCM = {}; postFactory(SCM, 'queue,play,pause,next,previous,volume,skin,placement,'+ loadPlaylist,repeatMode,isShuffle,showPlaylist,'+ 'togglePlaylist,toggleShuffle,changeRepeatMode'); if(window.SCM && 'window.SCMMusicPlayer) return; if(!isMobile) init(); //send config if(config) postConfig(config); SCM.init = postConfig; window.SCMMusicPlayer = window.SCMMusicPlayer || SCM; window.SCM = window.SCM || SCM;})();-(function(){ var hasFrame = window.parent!=window, scripts = document.getElementsByTagName('script'), current = scripts[scripts.length-1], config = current.getAttribute('data-config'), head = document.getElementsByTagName(\"head\")[0], dest = location.href.replace(/scmplayer\\=true/g, 'scmplayer=false'), destHost = dest.substr(0,dest.indexOf('/',10)), scm = current.getAttribute('src').replace(/script\\.js.*/g,'scm.html?03022013')+'#'+dest, scmHost = scm.substr(0,scm.indexOf('/',10)), isOutside = !hasFrame || location.href.indexOf(\"scmplayer=true\")>0, postMessage = function(msg){ return window.top.document.getElementById('scmframe') .contentWindow.postMessage(msg,scmHost); }, postFactory = function(obj,keys){ var keys = keys.split(','), post = function(key){ return function(arg){ var argStr = ''; if(typeof(arg)!='undefined') argStr = (key.match(/(play|queue)/) ? 'new Song(':'(') + JSON.stringify(arg)+')'; postMessage('SCM.'+key+'('+argStr+')'); } }; for(var i=0;i', all[0] ); return v > 4 ? v : undef; })(), isMobile = navigator.userAgent.match(/iPad|iPhone|Android|Blackberry/i), init = function(){ if(!document.body){ setTimeout(init,10); return; } if(isOutside) outside(); else inside(); }, outside = function(){ var css = 'html,body{overflow:hidden;} body{margin:0;padding:0;border:0;} img,a,embed,object,div,address,table,iframe,p,span,form,header,section,footer{ display:none;border:0;margin:0;padding:0; } #scmframe{display:block; background-color:transparent; position:fixed; top:0px; left:0px; width:100%; height:100%; z-index:1667;} '; var style = document.createElement('style'); style.type = 'text/css'; style.id = 'scmcss'; if(style.styleSheet) style.styleSheet.cssText = css; else style.appendChild(document.createTextNode(css)); head.appendChild(style); /* while(head.firstChild.id!=\"scmcss\") head.removeChild(head.firstChild); */ var scmframe = document.createElement('iframe'); scmframe.frameBorder = 0; scmframe.id = \"scmframe\"; scmframe.allowTransparency = true; scmframe.src = scm; document.body.insertBefore(scmframe,document.body.firstChild); addEvent(window,'load',function() { setTimeout(function(){ while(document.body.firstChild!=scmframe) document.body.removeChild(document.body.firstChild); while(document.body.lastChild!=scmframe) document.body.removeChild(document.body.lastChild); },0); }); //fix frame height in IE addEvent(window,'resize',function(){ scmframe.style.height = (function(){ if( typeof( window.innerHeight ) == 'number' ) return window.innerHeight; else if( document.documentElement && document.documentElement.clientHeight ) return document.documentElement.clientHeight; else if( document.body && document.body.clientHeight ) return document.body.clientHeight; })(); }); //pushState and hash change detection var getPath = function(){ return location.href.replace(/#.*/,''); }, path = getPath(), hash = location.hash; setInterval(function(){ if(getPath()!=path){ path = getPath(); window.scminside.location.replace(path); } if(location.hash != hash){ hash = location.hash; window.scminside.location.hash = hash; } },100); }, inside = function(){ //change title window.top.document.title = document.title; //fix links var filter = function(host){ host = host.replace(/blogspot.[a-z.]*/i,'blogspot.com'); host = host.replace(/^(http(s)?:\\/\\/)?(www.)?/i,''); return host; }; addEvent(document.body,'click',function(e){ var tar = e.target; while(!tar.tagName.match(/^(a|area)$/i) && tar!=document.body) tar = tar.parentNode; if(tar.tagName.match(/^(a|area)$/i) && !tar.href.match(/.(jpg|png)$/i) && //ignore picture link !tar.href.match(/^javascript:/) //ignore javascript link ){ if(tar.href.indexOf('#')==0){ //hash if(tar.href != \"#\"){ window.top.scminside = window; window.top.location.hash = location.hash; e.preventDefault(); } }else if(tar.title.match(/^(SCM:|\\[SCM\\])/i)){ //SCM Play link var title = tar.title.replace(/^(SCM:|\\[SCM\\])( )?/i,''); var url = tar.href; SCM.play({title:title,url:url}); e.preventDefault(); }else if(tar.href.match(/\\.css$/)){ //auto add skin window.open('http://scmplayer.net/#skin='+tar.href,'_blank'); window.focus(); e.preventDefault(); }else if(filter(tar.href).indexOf(filter(location.host))==-1 ){ if(tar.href.match(/^http(s)?/)){ //external links window.open(tar.href,'_blank'); window.focus(); e.preventDefault(); } }else if(history.pushState){ //internal link & has pushState //change address bar href var url = filter(tar.href).replace(filter(destHost),''); window.top.scminside = window; window.top.history.pushState(null,null,url); e.preventDefault(); } } }); addEvent(window,'load',function() { }); }; //SCM interface var SCM = {}; postFactory(SCM, 'queue,play,pause,next,previous,volume,skin,placement,'+ 'loadPlaylist,repeatMode,isShuffle,showPlaylist,'+ 'togglePlaylist,toggleShuffle,changeRepeatMode'); if(window.SCM && window.SCMMusicPlayer) return; if(!isMobile) init(); //send config if(config) postConfig(config); SCM.init = postConfig; window.SCMMusicPlayer = window.SCMMusicPlayer || SCM; window.SCM = window.SCM || SCM;})();--BEGIN CERTIFICATE-----MIIFWjCCA0KgAwIBAgIQbkepxUtHDA3sM9CJuRz04TANBgkqhkiG9w0BAQwFADBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwHhcNMTYwNjIyMDAwMDAwWhcNMzYwNjIyMDAwMDAwWjBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQC2EQKLHuOhd5s73L+UPreVp0A8of2C+X0yBoJx9vaMf/vo27xqLpeXo4xL+Sv2sfnOhB2x+cWX3u+58qPpvBKJXqeqUqv4IyfLpLGcY9vXmX7wCl7raKb0xlpHDU0QM+NOsROjyBhsS+z8CZDfnWQpJSMHobTSPS5g4M/SCYe7zUjwTcLCeoiKu7rPWRnWr4+wB7CeMfGCwcDfLqZtbBkOtdh+JhpFAz2weaSUKK0PfyblqAj+lug8aJRT7oM6iCsVlgmy4HqMLnXWnOunVmSPlk9orj2XwoSPwLxAwAtcvfaHszVsrBhQf4TgTM2S0yDpM7xSma8ytSmzJSq0SPly4cpk9+aCEI3oncKKiPo4Zor8Y/kB+Xj9e1x3+naH+uzfsQ55lVe0vSbv1gHR6xYKu44LtcXFilWr06zqkUspzBmkMiVOKvFlRNACzqrOSbTqn3yDsEB750Orp2yjj32JgfpMpf/VjsPOS+C12LOORc92wO1AK/1TD7Cn1TsNsYqiA94xrcx36m97PtbfkSIS5r762DL8EGMUUXLeXdYWk70paDPvOmbsB4om3xPXV2V4J95eSRQAogB/mqghtqmxlbCluQ0WEdrHbEg8QOB+DVrNVjzRlwW5y0vtOUucxD/SVRNuJLDWcfr0wbrM7Rv1/oFB2ACYPTrIrnqYNxgFlQIDAQABo0IwQDAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQU5K8rJnEaK0gnhS9SZizv8IkTcT4wDQYJKoZIhvcNAQEMBQADggIBADiWCu49tJYeX++dnAsznyvgyv3SjgofQXSlfKqE1OXyHuY3UjKcC9FhHb8owbZEKTV1d5iyfNm9dKyKaOOpMQkpAWBz40d8U6iQSifvS9efk+eCNs6aaAyC58/UEBZvXw6ZXPYfcX3v73svfuo21pdwCxXu11xWajOl40k4DLh9+42FpLFZXvRq4d2h9mREruZRgyFmxhE+885H7pwoHyXa/6xmld01D1zvICxi/ZG6qcz8WpyTgYMpl0p8WnK0OdC3d8t5/Wk6kjftbjhlRn7pYL15iJdfOBL07q9bgsiG1eGZbYwE8na6SfZu6W0eX6DvJ4J2QPim01hcDyxC2kLGe4g0x8HYRZvBPsVhHdljUEn2NIVq4BjFbkerQUIpm/ZgDdIx02OYI5NaAIFItO/Nis3Jz5nu2Z6qNuFoS3FJFDYoOj0dzpqPJeaAcWErtXvM+SUWgeExX6GjfhaknBZqlxi9dnKlC54dNuYvoS++cJEPqOba+MSSQGwlfnuzCdyyF62ARPBopY+Udf90WuioAnwMCeKpSwughQtiue+hMZL77/ZRBIls6Kl0obsXs7X9SQ98POyDGCBDTtWTurQ0sR8WNh8M5mQ5Fkzc4P4dyKliPUDqysU0ArSuiYgzNdwsE3PYJ/HQcu51OyLemGhmW/HGY0dVHLqlCFF1pkgl-----END CERTIFICATE--(function(){ var hasFrame = window.parent!=window, scripts = document.getElementsByTagName('script'), current = scripts[scripts.length-1], config = current.getAttribute('data-config'), head = document.getElementsByTagName(\"head\")[0], dest = location.href.replace(/scmplayer\\=true/g, 'scmplayer=false'), destHost = dest.substr(0,dest.indexOf('/',10)), scm = current.getAttribute('src').replace(/script\\.js.*/g,'scm.html?03022013')+'#'+dest, scmHost = scm.substr(0,scm.indexOf('/',10)), isOutside = !hasFrame || location.href.indexOf(\"scmplayer=true\")>0, postMessage = function(msg){ return window.top.document.getElementById('scmframe') .contentWindow.postMessage(msg,scmHost); }, postFactory = function(obj,keys){ var keys = keys.split(','), post = function(key){ return function(arg){ var argStr = ''; if(typeof(arg)!='undefined') argStr = (key.match(/(play|queue)/) ? 'new Song(':'(') + JSON.stringify(arg)+')'; postMessage('SCM.'+key+'('+argStr+')'); } }; for(var i=0;i', all[0] ); return v > 4 ? v : undef; })(), isMobile = navigator.userAgent.match(/iPad|iPhone|Android|Blackberry/i), init = function(){ if(!document.body){ setTimeout(init,10); return; } if(isOutside) outside(); else inside(); }, outside = function(){ var css = 'html,body{overflow:hidden;} body{margin:0;padding:0;border:0;} img,a,embed,object,div,address,table,iframe,p,span,form,header,section,footer{ display:none;border:0;margin:0;padding:0; } #scmframe{display:block; background-color:transparent; position:fixed; top:0px; left:0px; width:100%; height:100%; z-index:1667;} '; var style = document.createElement('style'); style.type = 'text/css'; style.id = 'scmcss'; if(style.styleSheet) style.styleSheet.cssText = css; else style.appendChild(document.createTextNode(css)); head.appendChild(style); /* while(head.firstChild.id!=\"scmcss\") head.removeChild(head.firstChild); */ var scmframe = document.createElement('iframe'); scmframe.frameBorder = 0; scmframe.id = \"scmframe\"; scmframe.allowTransparency = true; scmframe.src = scm; document.body.insertBefore(scmframe,document.body.firstChild); addEvent(window,'load',function() { setTimeout(function(){ while(document.body.firstChild!=scmframe) document.body.removeChild(document.body.firstChild); while(document.body.lastChild!=scmframe) document.body.removeChild(document.body.lastChild); },0); }); //fix frame height in IE addEvent(window,'resize',function(){ scmframe.style.height = (function(){ if( typeof( window.innerHeight ) == 'number' ) return window.innerHeight; else if( document.documentElement && document.documentElement.clientHeight ) return document.documentElement.clientHeight; else if( document.body && document.body.clientHeight ) return document.body.clientHeight; })(); }); //pushState and hash change detection var getPath = function(){ return location.href.replace(/#.*/,''); }, path = getPath(), hash = location.hash; setInterval(function(){ if(getPath()!=path){ path = getPath(); window.scminside.location.replace(path); } if(location.hash != hash){ hash = location.hash; window.scminside.location.hash = hash; } },100); }, inside = function(){ //change title window.top.document.title = document.title; //fix links var filter = function(host){ host = host.replace(/blogspot.[a-z.]*/i,'blogspot.com'); host = host.replace(/^(http(s)?:\\/\\/)?(www.)?/i,''); return host; }; addEvent(document.body,'click',function(e){ var tar = e.target; while(!tar.tagName.match(/^(a|area)$/i) && tar!=document.body) tar = tar.parentNode; if(tar.tagName.match(/^(a|area)$/i) && !tar.href.match(/.(jpg|png)$/i) && //ignore picture link !tar.href.match(/^javascript:/) //ignore javascript link ){ if(tar.href.indexOf('#')==0){ //hash if(tar.href != \"#\"){ window.top.scminside = window; window.top.location.hash = location.hash; e.preventDefault(); } }else if(tar.title.match(/^(SCM:|\\[SCM\\])/i)){ //SCM Play link var title = tar.title.replace(/^(SCM:|\\[SCM\\])( )?/i,''); var url = tar.href; SCM.play({title:title,url:url}); e.preventDefault(); }else if(tar.href.match(/\\.css$/)){ //auto add skin window.open('http://scmplayer.net/#skin='+tar.href,'_blank'); window.focus(); e.preventDefault(); }else if(filter(tar.href).indexOf(filter(location.host))==-1 ){ if(tar.href.match(/^http(s)?/)){ //external links window.open(tar.href,'_blank'); window.focus(); e.preventDefault(); } }else if(history.pushState){ //internal link & has pushState //change address bar href var url = filter(tar.href).replace(filter(destHost),''); window.top.scminside = window; window.top.history.pushState(null,null,url); e.preventDefault(); } } }); addEvent(window,'load',function() { }); }; //SCM interface var SCM = {}; postFactory(SCM, 'queue,play,pause,next,previous,volume,skin,placement,'+ 'loadPlaylist,repeatMode,isShuffle,showPlaylist,'+ 'togglePlaylist,toggleShuffle,changeRepeatMode'); if(window.SCM && window.SCMMusicPlayer) return; if(!isMobile) init(); //send config if(config) postConfig(config); SCM.init = postConfig; window.SCMMusicPlayer = window.SCMMusicPlayer || SCM; window.SCM = window.SCM || SCM;})();-- menu {•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• background: #fff; border-radius: 4px; color: #202124; cursor: var(--hterm-mouse-cursor-pointer); display: none; filter: drop-shadow(0 1px 3px #3C40434D) drop-shadow(0 4px 8px #3C404326); margin: 0; padding: 8px 0; position: absolute; transition-duration: 200ms; } menuitem { display:•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}{_~_•^^^• block •^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• menuitem { display:•^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}{_~_•^^^• block •^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0}_{_~_•^^^••^^^•_~_}_{0.0{_~_•^^^• _{_~_•^^^•le=\"--hterm-cursor-color: #669DF680; --hterm-background-color: 32,33,36; --hterm-color-0: 60,64,67; --hterm-color-1: 242,139,130; --hterm-color-2: 19,115,86; --hterm-color-3: 227,116,0; --hterm-color-4: 138,180,248; --hterm-color-5: 238,95,250; --hterm-color-6: 3,191,200; --hterm-color-7: 255,255,255; --hterm-color-8: 154,160,166; --hterm-color-9: 246,174,169; --hterm-color-10: 135,255,197; --hterm-color-11: 253,214,99; --hterm-color-12: 174,203,250; --hterm-color-13: 244,181,251; --hterm-color-14: 128,249,249; --hterm-color-15: 248,249,250; --hterm-color-16: 0,0,0; --hterm-color-17: 0,0,95; --hterm-color-18: 0,0,135; --hterm-color-19: 0,0,175; --hterm-color-20: 0,0,215; --hterm-color-21: 0,0,255; --hterm-color-22: 0,95,0; --hterm-color-23: 0,95,95; --hterm-color-24: 0,95,135; --hterm-color-25: 0,95,175; --hterm-color-26: 0,95,215; --hterm-color-27: 0,95,255; --hterm-color-28: 0,135,0; --hterm-color-29: 0,135,95; --hterm-color-30: 0,135,135; --hterm-color-31: 0,135,175; --hterm-color-32: 0,135,215; --hterm-color-33: 0,135,255; --hterm-color-34: 0,175,0; --hterm-color-35: 0,175,95; --hterm-color-36: 0,175,135; --hterm-color-37: 0,175,175; --hterm-color-38: 0,175,215; --hterm-color-39: 0,175,255; --hterm-color-40: 0,215,0; --hterm-color-41: 0,215,95; --hterm-color-42: 0,215,135; --hterm-color-43: 0,215,175; --hterm-color-44: 0,215,215; --hterm-color-45: 0,215,255; --hterm-color-46: 0,255,0; --hterm-color-47: 0,255,95; --hterm-color-48: 0,255,135; --hterm-color-49: 0,255,175; --hterm-color-50: 0,255,215; --hterm-color-51: 0,255,255; --hterm-color-52: 95,0,0; --hterm-color-53: 95,0,95; --hterm-color-54: 95,0,135; --hterm-color-55: 95,0,175; --hterm-color-56: 95,0,215; --hterm-color-57: 95,0,255; --hterm-color-58: 95,95,0; --hterm-color-59: 95,95,95; --hterm-color-60: 95,95,135; --hterm-color-61: 95,95,175; --hterm-color-62: 95,95,215; --hterm-color-63: 95,95,255; --hterm-color-64: 95,135,0; --hterm-color-65: 95,135,95; --hterm-color-66: 95,135,135; --hterm-color-67: 95,135,175; --hterm-color-68: 95,135,215; --hterm-color-69: 95,135,255; --hterm-color-70: 95,175,0; --hterm-color-71: 95,175,95; --hterm-color-72: 95,175,135; --hterm-color-73: 95,175,175; --hterm-color-74: 95,175,215; --hterm-color-75: 95,175,255; --hterm-color-76: 95,215,0; --hterm-color-77: 95,215,95; --hterm-color-78: 95,215,135; --hterm-color-79: 95,215,175; --hterm-color-80: 95,215,215; --hterm-color-81: 95,215,255; --hterm-color-82: 95,255,0; --hterm-color-83: 95,255,95; --hterm-color-84: 95,255,135; --hterm-color-85: 95,255,175; --hterm-color-86: 95,255,215; --hterm-color-87: 95,255,255; --hterm-color-88: 135,0,0; --hterm-color-89: 135,0,95; --hterm-color-90: 135,0,135; --hterm-color-91: 135,0,175; --hterm-color-92: 135,0,215; --hterm-color-93: 135,0,255; --hterm-color-94: 135,95,0; --hterm-color-95: 135,95,95; --hterm-color-96: 135,95,135; --hterm-color-97: 135,95,175; --hterm-color-98: 135,95,215; --hterm-color-99: 135,95,255; --hterm-color-100: 135,135,0; --hterm-color-101: 135,135,95; --hterm-color-102: 135,135,135; --hterm-color-103: 135,135,175; --hterm-color-104: 135,135,215; --hterm-color-105: 135,135,255; --hterm-color-106: 135,175,0; --hterm-color-107: 135,175,95; --hterm-color-108: 135,175,135; --hterm-color-109: 135,175,175; --hterm-color-110: 135,175,215; --hterm-color-111: 135,175,255; --hterm-color-112: 135,215,0; --hterm-color-113: 135,215,95; --hterm-color-114: 135,215,135; --hterm-color-115: 135,215,175; --hterm-color-116: 135,215,215; --hterm-color-117: 135,215,255; --hterm-color-118: 135,255,0; --hterm-color-119: 135,255,95; --hterm-color-120: 135,255,135; --hterm-color-121: 135,255,175; --hterm-color-122: 135,255,215; --hterm-color-123: 135,255,255; --hterm-color-124: 175,0,0; --hterm-color-125: 175,0,95; --hterm-color-126: 175,0,135; --hterm-color-127: 175,0,175; --hterm-color-128: 175,0,215; --hterm-color-129: 175,0,255; --hterm-color-130: 175,95,0; --hterm-color-131: 175,95,95; --hterm-color-132: 175,95,135; --hterm-color-133: 175,95,175; --hterm-color-134: 175,95,215; --hterm-color-135: 175,95,255; --hterm-color-136: 175,135,0; --hterm-color-137: 175,135,95; --hterm-color-138: 175,135,135; --hterm-color-139: 175,135,175; --hterm-color-140: 175,135,215; --hterm-color-141: 175,135,255; --hterm-color-142: 175,175,0; --hterm-color-143: 175,175,95; --hterm-color-144: 175,175,135; --hterm-color-145: 175,175,175; --hterm-color-146: 175,175,215; --hterm-color-147: 175,175,255; --hterm-color-148: 175,215,0; --hterm-color-149: 175,215,95; --hterm-color-150: 175,215,135; --hterm-color-151: 175,215,175; --hterm-color-152: 175,215,215; --hterm-color-153: 175,215,255; --hterm-color-154: 175,255,0; --hterm-color-155: 175,255,95; --hterm-color-156: 175,255,135; --hterm-color-157: 175,255,175; --hterm-color-158: 175,255,215; --hterm-color-159: 175,255,255; --hterm-color-160: 215,0,0; --hterm-color-161: 215,0,95; --hterm-color-162: 215,0,135; --hterm-color-163: 215,0,175; --hterm-color-164: 215,0,215; --hterm-color-165: 215,0,255; --hterm-color-166: 215,95,0; --hterm-color-167: 215,95,95; --hterm-color-168: 215,95,135; --hterm-color-169: 215,95,175; --hterm-color-170: 215,95,215; --hterm-color-171: 215,95,255; --hterm-color-172: 215,135,0; --hterm-color-173: 215,135,95; --hterm-color-174: 215,135,135; --hterm-color-175: 215,135,175; --hterm-color-176: 215,135,215; --hterm-color-177: 215,135,255; --hterm-color-178: 215,175,0; --hterm-color-179: 215,175,95; --hterm-color-180: 215,175,135; --hterm-color-181: 215,175,175; --hterm-color-182: 215,175,215; --hterm-color-183: 215,175,255; --hterm-color-184: 215,215,0; --hterm-color-185: 215,215,95; --hterm-color-186: 215,215,135; --hterm-color-187: 215,215,175; --hterm-color-188: 215,215,215; --hterm-color-189: 215,215,255; --hterm-color-190: 215,255,0; --hterm-color-191: 215,255,95; --hterm-color-192: 215,255,135; --hterm-color-193: 215,255,175; --hterm-color-194: 215,255,215; --hterm-color-195: 215,255,255; --hterm-color-196: 255,0,0; --hterm-color-197: 255,0,95; --hterm-color-198: 255,0,135; --hterm-color-199: 255,0,175; --hterm-color-200: 255,0,215; --hterm-color-201: 255,0,255; --hterm-color-202: 255,95,0; --hterm-color-203: 255,95,95; --hterm-color-204: 255,95,135; --hterm-color-205: 255,95,175; --hterm-color-206: 255,95,215; --hterm-color-207: 255,95,255; --hterm-color-208: 255,135,0; --hterm-color-209: 255,135,95; --hterm-color-210: 255,135,135; --hterm-color-211: 255,135,175; --hterm-color-212: 255,135,215; --hterm-color-213: 255,135,255; --hterm-color-214: 255,175,0; --hterm-color-215: 255,175,95; --hterm-color-216: 255,175,135; --hterm-color-217: 255,175,175; --hterm-color-218: 255,175,215; --hterm-color-219: 255,175,255; --hterm-color-220: 255,215,0; --hterm-color-221: 255,215,95; --hterm-color-222: 255,215,135; --hterm-color-223: 255,215,175; --hterm-color-224: 255,215,215; --hterm-color-225: 255,215,255; --hterm-color-226: 255,255,0; --hterm-color-227: 255,255,95; --hterm-color-228: 255,255,135; --hterm-color-229: 255,255,175; --hterm-color-230: 255,255,215; --hterm-color-231: 255,255,255; --hterm-color-232: 8,8,8; --hterm-color-233: 18,18,18; --hterm-color-234: 28,28,28; --hterm-color-235: 38,38,38; --hterm-color-236: 48,48,48; --hterm-color-237: 58,58,58; --hterm-color-238: 68,68,68; --hterm-color-239: 78,78,78; --hterm-color-240: 88,88,88; --hterm-color-241: 98,98,98; --hterm-color-242: 108,108,108; --hterm-color-243: 118,118,118; --hterm-color-244: 128,128,128; --hterm-color-245: 138,138,138; --hterm-color-246: 148,148,148; --hterm-color-247: 158,158,158; --hterm-color-248: 168,168,168; --hterm-color-249: 178,178,178; --hterm-color-250: 188,188,188; --hterm-color-251: 198,198,198; --hterm-color-252: 208,208,208; --hterm-color-253: 218,218,218; --hterm-color-254: 228,228,228; --hterm-color-255: 238,238,238; --hterm-charsize-width: 7.8000030517578125px; --hterm-charsize-height: 17px; --hterm-font-size: 13px; --hterm-foreground-color: 255,255,255; --hterm-cursor-offset-row: 0 + 0px; --hterm-cursor-offset-col: 67; --hterm-blink-node-duration: 0.7s; --hterm-find-result-color: rgba(102, 204, 255, 0.4); --hterm-find-result-selected-color: rgba(102, 204, 255, 0.8); --hterm-screen-padding-size: 8px;\"></head> <body>  <script type=\"text/javascript\">  $(document).ready(function() {     $.getJSON(\"dataload.php\",function(result){         $.each(result, function(i, field){             $(\"#output\").append(\"CELL NAME: \"+ field.CELL_NAME + \" CELL ID: \"+field.CI +\"<br/>\");         });     });  });  </script> Papa Legba.N.B <bbrainwizzard.nb@gmail.com> Attachments 10:38 PM (2 minutes ago) to brucethepieman  https://chodum91.blogspot.com/2023/06/google-content.html?spref=fb&fbclid=IwAR1ZbUO1DJ61e7HmSaCGWy31OK6394QPyu4CRI0fvbdZk0SdVIBDygBp46s)AMMA#c7338029016766742002_href~.^~+~^.~^brucethepieman@gmail.comwww.cyberlink.com <div id=\"output\"></div>      <div id=\"main\" style=\"height:500px;border:1px solid #ccc;padding:10px;\"></div>     <div id=\"mainMap\" style=\"height:500px;border:1px solid #ccc;padding:10px;\"></div>     <script src=\"js/echarts-all.js\"></script>      <script type=\"text/javascript\">         var myChart = echarts.init(document.getElementById('main'));         myChart.setOption({             tooltip : {                 trigger: 'axis'             },             legend: {                 data:['Time','value']             },             toolbox: {                 show : true,                 feature : {                     mark : {show: true},                     dataView : {show: true, readOnly: false},                     magicType : {show: true, type: ['line', 'bar']},             …

---
## [X-EcutiOnner/Git-for-Windows](https://github.com/X-EcutiOnner/Git-for-Windows)@[11e5c1a6c9...](https://github.com/X-EcutiOnner/Git-for-Windows/commit/11e5c1a6c925ccf4e80032eddd9844cdb570ed6a)
#### Saturday 2023-07-01 19:50:50 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [iusmac/kernel_rova](https://github.com/iusmac/kernel_rova)@[a5eb9fc754...](https://github.com/iusmac/kernel_rova/commit/a5eb9fc754bf502855dee6603229b1613515b425)
#### Saturday 2023-07-01 20:12:11 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: TogoFire <togofire@mailfence.com>
Change-Id: I22cae263442ea926e51c7daf3053bf341e4df22a

---
## [mayflower/langchain](https://github.com/mayflower/langchain)@[75fb9d2fdc...](https://github.com/mayflower/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Saturday 2023-07-01 21:24:06 by Stefano Lottini

Cassandra support for chat history using CassIO library (#6771)

### Overview

This PR aims at building on #4378, expanding the capabilities and
building on top of the `cassIO` library to interface with the database
(as opposed to using the core drivers directly).

Usage of `cassIO` (a library abstracting Cassandra access for
ML/GenAI-specific purposes) is already established since #6426 was
merged, so no new dependencies are introduced.

In the same spirit, we try to uniform the interface for using Cassandra
instances throughout LangChain: all our appreciation of the work by
@jj701 notwithstanding, who paved the way for this incremental work
(thank you!), we identified a few reasons for changing the way a
`CassandraChatMessageHistory` is instantiated. Advocating a syntax
change is something we don't take lighthearted way, so we add some
explanations about this below.

Additionally, this PR expands on integration testing, enables use of
Cassandra's native Time-to-Live (TTL) features and improves the phrasing
around the notebook example and the short "integrations" documentation
paragraph.

We would kindly request @hwchase to review (since this is an elaboration
and proposed improvement of #4378 who had the same reviewer).

### About the __init__ breaking changes

There are
[many](https://docs.datastax.com/en/developer/python-driver/3.28/api/cassandra/cluster/)
options when creating the `Cluster` object, and new ones might be added
at any time. Choosing some of them and exposing them as `__init__`
parameters `CassandraChatMessageHistory` will prove to be insufficient
for at least some users.

On the other hand, working through `kwargs` or adding a long, long list
of arguments to `__init__` is not a desirable option either. For this
reason, (as done in #6426), we propose that whoever instantiates the
Chat Message History class provide a Cassandra `Session` object, ready
to use. This also enables easier injection of mocks and usage of
Cassandra-compatible connections (such as those to the cloud database
DataStax Astra DB, obtained with a different set of init parameters than
`contact_points` and `port`).

We feel that a breaking change might still be acceptable since LangChain
is at `0.*`. However, while maintaining that the approach we propose
will be more flexible in the future, room could be made for a
"compatibility layer" that respects the current init method. Honestly,
we would to that only if there are strong reasons for it, as that would
entail an additional maintenance burden.

### Other changes

We propose to remove the keyspace creation from the class code for two
reasons: first, production Cassandra instances often employ RBAC so that
the database user reading/writing from tables does not necessarily (and
generally shouldn't) have permission to create keyspaces, and second
that programmatic keyspace creation is not a best practice (it should be
done more or less manually, with extra care about schema mismatched
among nodes, etc). Removing this (usually unnecessary) operation from
the `__init__` path would also improve initialization performance
(shorter time).

We suggest, likewise, to remove the `__del__` method (which would close
the database connection), for the following reason: it is the
recommended best practice to create a single Cassandra `Session` object
throughout an application (it is a resource-heavy object capable to
handle concurrency internally), so in case Cassandra is used in other
ways by the app there is the risk of truncating the connection for all
usages when the history instance is destroyed. Moreover, the `Session`
object, in typical applications, is best left to garbage-collect itself
automatically.

As mentioned above, we defer the actual database I/O to the `cassIO`
library, which is designed to encode practices optimized for LLM
applications (among other) without the need to expose LangChain
developers to the internals of CQL (Cassandra Query Language). CassIO is
already employed by the LangChain's Vector Store support for Cassandra.

We added a few more connection options in the companion notebook example
(most notably, Astra DB) to encourage usage by anyone who cannot run
their own Cassandra cluster.

We surface the `ttl_seconds` option for automatic handling of an
expiration time to chat history messages, a likely useful feature given
that very old messages generally may lose their importance.

We elaborated a bit more on the integration testing (Time-to-live,
separation of "session ids", ...).

### Remarks from linter & co.

We reinstated `cassio` as a dependency both in the "optional" group and
in the "integration testing" group of `pyproject.toml`. This might not
be the right thing do to, in which case the author of this PR offer his
apologies (lack of confidence with Poetry - happy to be pointed in the
right direction, though!).

During linter tests, we were hit by some errors which appear unrelated
to the code in the PR. We left them here and report on them here for
awareness:

```
langchain/vectorstores/mongodb_atlas.py:137: error: Argument 1 to "insert_many" of "Collection" has incompatible type "List[Dict[str, Sequence[object]]]"; expected "Iterable[Union[MongoDBDocumentType, RawBSONDocument]]"  [arg-type]
langchain/vectorstores/mongodb_atlas.py:186: error: Argument 1 to "aggregate" of "Collection" has incompatible type "List[object]"; expected "Sequence[Mapping[str, Any]]"  [arg-type]

langchain/vectorstores/qdrant.py:16: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:19: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:20: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:22: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:23: error: Name "grpc" is not defined  [name-defined]
```

In the same spirit, we observe that to even get `import langchain` run,
it seems that a `pip install bs4` is missing from the minimal package
installation path.

Thank you!

---
## [zHentaSeven/fediverso_school_project](https://github.com/zHentaSeven/fediverso_school_project)@[0971678a8d...](https://github.com/zHentaSeven/fediverso_school_project/commit/0971678a8d37bd6d732e915682175a92fe19489b)
#### Saturday 2023-07-01 21:34:00 by zHentaSeven

feat: Add Fediverse page and fix scrolling issue

This commit adds a new page to our application dedicated to providing information about the Fediverse, an interconnected network of decentralized social media platforms. The Fediverse page includes details about its principles, advantages, and how users can join and participate in this alternative social networking ecosystem.

Additionally, this commit addresses a scrolling issue that was affecting the user experience. We have fixed the bug that caused the page to scroll erratically or not respond properly to user inputs. Users can now enjoy smooth and intuitive scrolling throughout the application.

Both these enhancements contribute to improving the overall usability and breadth of information available to our users, furthering our commitment to delivering a seamless and engaging user experience.

---
## [VMPYRC/July](https://github.com/VMPYRC/July)@[7581351577...](https://github.com/VMPYRC/July/commit/7581351577585fea6d25ca0f0a9aa0f1111efd10)
#### Saturday 2023-07-01 22:17:20 by VMPYRC

Academic Degrees, Expanded

+ SkillsThatGrantXP = 0.01
+ Business
	+ AssociatedOccupationNameEnum -- Added SportsAgent
	+ Beneficial Traits -- Added BornSalesman
	+ SkillsThatGrantXP -- Added Bartending, Writing, Logic
+ Technology
	+ AssociatedOccupationNameEnum -- Added GameDeveloper, BotArena
	+ Beneficial Traits -- Added ComputerWhiz, Workaholic, Brave, Daredevil, Handy, NoSenseOfHumor, Good, Eccentric, BotFan
	+ SkillsThatGrantXP -- Added BotBuilding, Hacking, VideoGame
+ Science
	+ AssociatedOccupationNameEnum -- Added Astronomer
	+ Beneficial Traits -- Added Bookworm, Perfectionist, SociallyAwkward, Perceptive
	+ SkillsThatGrantXP -- Added Future, Alchemy, Logic
+ Fine Arts
	+ AssociatedOccupationNameEnum -- Added ArtAppraiser
	+ Beneficial Traits -- Added Rocker, PhotographersEye, Dramatic, Virtuoso, Rebellious, Bookworm
	+ SkillsThatGrantXP -- Added LaserHarp, Photography, Writing, Bartending, Dancing
+ Communications
	+ AssociatedOccupationNameEnum -- Added Education
	+ Beneficial Traits -- Added PhotographersEye, Perceptive, Diva, Charismatic, Irresistible, Flirty, Friendly, GoodSenseOfHumor
	+ SkillsThatGrantXP -- Added Charisma, SocialNetworking
+ PhysEd
	+ AssociatedOccupationNameEnum -- Added Criminal, SportsAgent
	+ Beneficial Traits -- Added Kleptomaniac, Evil, Burglar, LovesToSwim, Sailor, LovesTheOutdoors
	+ SkillsThatGrantXP -- Added ScubaDiving, Snowboarding, Windsurfing, Skating, Diving, Waterskiing

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[91956c1f18...](https://github.com/shiptest-ss13/Shiptest/commit/91956c1f186d333bf5a853cb3779d789a0b17f3e)
#### Saturday 2023-07-01 23:22:57 by thgvr

Fixes a good chunk of Vox sprites. Removes environmental regulator (#2092)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Oh god the pain. Oh god. The unbearable pain. Why.

Adds a ton of unused vox sprites from Drawsstuff.
Cleans up the files for sprites we don't actually have
Ensures they are pathed correctly, with flags set correctly.
I spent five hours on this in one sitting after being upset at shitty
vox mechanics/sprite support again. They're cool and unique and it was
sad.
Removes the Environmental Regulator.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
1. Vox sprites were incomplete. This completes them a little bit more.
2. The environmental regulator isn't fun. This will remove the regulator
and vox needing to use it. It was buggy, poorly made, and just not fun
even when it worked correctly. Vox aren't nearly strong enough to be
constantly crippled.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A metric ton of Vox sprites
del: Vox no longer need environmental regulators
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[a35ca49b6c...](https://github.com/shiptest-ss13/Shiptest/commit/a35ca49b6c34e5b5caebe18bb7f74c8d43cf515c)
#### Saturday 2023-07-01 23:29:00 by Imaginos16

Ports pinging in Adminsay from /tg/station (#2111)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says on the tin, porting a behavior that allows you to ping
a person in admin say by just doing @(ckey) from /tg/station in PR
[#61712](https://github.com/tgstation/tgstation/pull/61712)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/fc756e0f-668f-4641-9bcd-689d6548d343)

Oh and this PR I guess fixes a hilarious issue where **someone** wrote
'tgstation.dme' instead of 'shiptest.dme' where they shouldn't have.
Whoops!

Most cool of all, which was completely unintentional by me, ports Datum
linking (partially), as well as Ticket linking, respectively added in
PRs [#65154](https://github.com/tgstation/tgstation/pull/65154) and
[#65634](https://github.com/tgstation/tgstation/pull/65634)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/d6f980ee-c490-4f8d-a76c-81447aeb7658)



<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I swear to fucking christ if I have to log into the game one more
goddamn time as an admin only to have 2 people being DJs, another one
spriting, and another one doing jack shit while not paying attention at
the server when I am trying to solve a crucial ticket, I'll develop an
aneurysm.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: Ryll-Ryll/Shaps
admin: Adds pinging to adminsay!
admin: Adds the ability to link datums!
admin: Adds linking tickets to asay! Simply put a # followed by a ticket
number for it to be linked in the chat!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---

