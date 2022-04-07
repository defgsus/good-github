## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-06](docs/good-messages/2022/2022-04-06.md)


1,888,726 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,888,726 were push events containing 3,070,434 commit messages that amount to 224,352,788 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 38 messages:


## [ScaerieTale/ST-Silent-Auction](https://github.com/ScaerieTale/ST-Silent-Auction)@[2d89aaec08...](https://github.com/ScaerieTale/ST-Silent-Auction/commit/2d89aaec08324112c4900c09b811a319bfb59c6b)
#### Wednesday 2022-04-06 00:38:25 by ScaerieTale

Stop laughing

I managed to remember to NOT put integers as strings before uploading this commit :P  Anyway, I've managed to get the code to pull the high bidder!  Now I need to figure out how to display the value.  I THINK it's as simple as calling value = instead of key = but we'll see! <3

---
## [C0rva1r/Skyrat-tg](https://github.com/C0rva1r/Skyrat-tg)@[8607ba8b7d...](https://github.com/C0rva1r/Skyrat-tg/commit/8607ba8b7d98c52e81f23816a9224adf70559c25)
#### Wednesday 2022-04-06 00:58:49 by SkyratBot

[MIRROR] Adds a very rare sussy firelock [MDB IGNORE] (#12401)

* Adds a very rare sussy firelock (#65677)

On a VERY low chance (1/25000) a normal full tile firelock can instead be generated with a more suspicious appearance based on this recent quality shitpost.

Sussy firelocks are completely identical when open (save the desc) and thus are apt not to be noticed except during exciting times. It's a fully cosmetic joke that got me to log into github, and that's an accomplishment in itself. Probability rate fully negotiable, I've added a one in a million chance before after all.

* Adds a very rare sussy firelock

* ruins all the fun

people can get banned for doing the funny sus amogus so encouraging it in code, whilst it's beautiful and funny, eh someone is going to throw a fit.

Co-authored-by: Incoming5643 <incomingnumbers@gmail.com>
Co-authored-by: KathrinBailey <53862927+KathrinBailey@users.noreply.github.com>

---
## [kkdwivedi/linux](https://github.com/kkdwivedi/linux)@[9a7ef9f86b...](https://github.com/kkdwivedi/linux/commit/9a7ef9f86b96be22d009422e4c0ba52e1292492f)
#### Wednesday 2022-04-06 01:16:38 by Alexei Starovoitov

Merge branch 'Add libbpf support for USDTs'

Andrii Nakryiko says:

====================

Add libbpf support for USDT (User Statically-Defined Tracing) probes.
USDTs is important part of tracing, and BPF, ecosystem, widely used in
mission-critical production applications for observability, performance
analysis, and debugging.

And while USDTs themselves are pretty complicated abstraction built on top of
uprobes, for end-users USDT is as natural a primitive as uprobes themselves.
And thus it's important for libbpf to provide best possible user experience
when it comes to build tracing applications relying on USDTs.

USDTs historically presented a lot of challenges for libbpf's no
compilation-on-the-fly general approach to BPF tracing. BCC utilizes power of
on-the-fly source code generation and compilation using its embedded Clang
toolchain, which was impractical for more lightweight and thus more rigid
libbpf-based approach. But still, with enough diligence and BPF cookies it's
possible to implement USDT support that feels as natural as tracing any
uprobe.

This patch set is the culmination of such effort to add libbpf USDT support
following the spirit and philosophy of BPF CO-RE (even though it's not
inherently relying on BPF CO-RE much, see patch #1 for some notes regarding
this). Each respective patch has enough details and explanations, so I won't
go into details here.

In the end, I think the overall usability of libbpf's USDT support *exceeds*
the status quo set by BCC due to the elimination of awkward runtime USDT
supporting code generation. It also exceeds BCC's capabilities due to the use
of BPF cookie. This eliminates the need to determine a USDT call site (and
thus specifics about how exactly to fetch arguments) based on its *absolute IP
address*, which is impossible with shared libraries if no PID is specified (as
we then just *can't* know absolute IP at which shared library is loaded,
because it might be different for each process). With BPF cookie this is not
a problem as we record "call site ID" directly in a BPF cookie value. This
makes it possible to do a system-wide tracing of a USDT defined in a shared
library. Think about tracing some USDT in libc across any process in the
system, both running at the time of attachment and all the new processes
started *afterwards*. This is a very powerful capability that allows more
efficient observability and tracing tooling.

Once this functionality lands, the plan is to extend libbpf-bootstrap ([0])
with an USDT example. It will also become possible to start converting BCC
tools that rely on USDTs to their libbpf-based counterparts ([1]).

It's worth noting that preliminary version of this code was currently used and
tested in production code running fleet-wide observability toolkit.

Libbpf functionality is broken down into 5 mostly logically independent parts,
for ease of reviewing:
  - patch #1 adds BPF-side implementation;
  - patch #2 adds user-space APIs and wires bpf_link for USDTs;
  - patch #3 adds the most mundate pieces: handling ELF, parsing USDT notes,
    dealing with memory segments, relative vs absolute addresses, etc;
  - patch #4 adds internal ID allocation and setting up/tearing down of
    BPF-side state (spec and IP-to-ID mapping);
  - patch #5 implements x86/x86-64-specific logic of parsing USDT argument
    specifications;
  - patch #6 adds testing of various basic aspects of handling of USDT;
  - patch #7 extends the set of tests with more combinations of semaphore,
    executable vs shared library, and PID filter options.

  [0] https://github.com/libbpf/libbpf-bootstrap
  [1] https://github.com/iovisor/bcc/tree/master/libbpf-tools

v2->v3:
  - fix typos, leave link to systemtap doc, acks, etc (Dave);
  - include sys/sdt.h to avoid extra system-wide package dependencies;
v1->v2:
  - huge high-level comment describing how all the moving parts fit together
    (Alan, Alexei);
  - switched from `__hidden __weak` to `static inline __noinline` for now, as
    there is a bug in BPF linker breaking final BPF object file due to invalid
    .BTF.ext data; I want to fix it separately at which point I'll switch back
    to __hidden __weak again. The fix isn't trivial, so I don't want to block
    on that. Same for __weak variable lookup bug that Henqi reported.
  - various fixes and improvements, addressing other feedback (Alan, Hengqi);

Cc: Alan Maguire <alan.maguire@oracle.com>
Cc: Dave Marchevsky <davemarchevsky@fb.com>
Cc: Hengqi Chen <hengqi.chen@gmail.com>
====================

Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [aweatherguy/docs](https://github.com/aweatherguy/docs)@[60a20ed67c...](https://github.com/aweatherguy/docs/commit/60a20ed67c687c61b22205c665ef5b921bf1f0e9)
#### Wednesday 2022-04-06 01:42:59 by aweatherguy

Update Self-signed-Mosquitto.md

By way of introduction, I'm proposing what may be a lot of changes here. This is sort of a shotgun approach, as I'm not sure what you might or might not be interested in. So, give these changes a look and don't be afraid to take your shots -- I won't be offended. Keep anything you like and throw away the rest.

There are three main goals in proposing these changes:

1) To enhance the information already there

After going through the process of making a self-signed configuration, I kept some notes about where I had trouble and have updated this document to cover those points.

2) Add instructions specific to performing these tasks on Windows

In the Windows environment, there were several steps I found difficult or impossible to accomplish in native Windows, even though some of the tools seem to be setup to support that. In the end, I resorted to doing most of the work in Cygwin and have added some ideas along those lines to the document. Other comments about differences between Linux and Windows are also added.

3) Suggest a method for embedding the root certificate that does not require modification of files in the distribution, including changes to tasmota_ca.ino.

Embedding a local root certificate in the firmware requires modifying one of the distribution files (tasmota_ca.ino). Source updates will either delete those changes, or manual merging in git will be required, and this is less than optimal.

I am suggesting some changes to the tasmota_ca.ino file which will conditionally include two header files containing definitions and data for the root certificate. The default would be NOT to include these headers, and folks would have to define a macro in their user_config_override.h file to enable that. 

Additionally, the process of creating the two header files is automated with simple sed scripts as shown in the changes to this document. This produces output in the correct format, and no additional manual editing is required.

I have an updated copy of tasmota_ca.ino ready to go, but am not sure how to coordinated that change request, as the source is in a different repository. I have not made that change request yet. Suggestions?

-----

Finally, it seems to me that a lot of this could be further automated into some script tools to make it pretty painless, but that would require another package for distribution, and I'm not sure anyone wants to go there. Thoughts?

-----

And, oh yeah, thanks to all who have contributed before me. I really do appreciate all the effort.

---
## [baconpaul/surge](https://github.com/baconpaul/surge)@[3ff7e6bc5a...](https://github.com/baconpaul/surge/commit/3ff7e6bc5a709a89611a8f6321ed0b06a15c4c95)
#### Wednesday 2022-04-06 01:51:10 by Paul Walker

Doubleclick Renamed Modulators without annoying bug

Doubleclick renames a modulator. Cool

But this kinda sucks if you click into a modulator and then click to arm
quickly and misfire a double click

So if you have *just* selected a modulator the double click doesn't work.

Only after that

Closes #5774

---
## [jsoref/terminal](https://github.com/jsoref/terminal)@[a916a5d9de...](https://github.com/jsoref/terminal/commit/a916a5d9de450bc6a008d257d3c5c5cfd27e07ec)
#### Wednesday 2022-04-06 02:20:13 by Mike Griese

Make sure the infobar is inserted before the tab content, not on top of (#11609)

Fixes #11606

This is weird, but the infobars would appear totally on top of the
TerminalPage when `showTabsInTitlebar:false`. This would result in the infobar
obscuring the tabs.

Now, the infobars are strictly inserted after the tabs, before the content. So
when they appear, they will reduce the amount of space usable for the control.
That is a little annoying, but preferable to the tabs totally not existing.

Relevant conversation notes from #10798:

> > If the info bar is not local to the tab, then its location between the tab
> > bar (when the title bar is hidden) and the terminal panes feels
> > misleading. Should it instead be above the tab bar or below the terminal
> > panes?
>
> You're... not wrong here. It's maybe not the best place for it, but _on top_
> of the tabs would look insane, and probably wouldn't even work easily, given
> the way we reparent the tab row into the titlebar.
>
> In the pane itself would make more sense, but that runs abreast of all sorts
> of things like #9024, #4998, which might make more sense.

I'm just gonna go with this now, because it's _better_ than before, while we
work out what's _best_.

![gh-11606-fix](https://user-images.githubusercontent.com/18356694/138729178-b96b7003-0dd2-4521-8fff-0fd2a5989f22.gif)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ccb377750a...](https://github.com/tgstation/tgstation/commit/ccb377750a76d9aab5a01a6367ba0699398b6eac)
#### Wednesday 2022-04-06 02:46:08 by san7890

Creates Linters for (bad) Commented Out Lines in Maps (#65888)

* Creates CI Linters for Commented Out Lines in Maps

Creates Linters for (bad) Commented Out Lines in Maps

Hey there,

This PR is made because what happened in #65837 was fucking horrible awful shit that I'm still dealing with a few days after I fixed it. This _should hopefully_ add a new linter for commented out lines of code in a .DMM file, and HOPEFULLY doesn't flag the commented line that prevents unwanted TGM > DMM conversion.

As a proof to see if it works, I'll be adding a comment to Line 2 of IcemoonUnderground_Above.dmm. Hopefully, on the first CI check, it'll fail. I'll remove that line so it doesn't make its way into production (it will suck).

---
## [maxieds/FlowersForMama2022](https://github.com/maxieds/FlowersForMama2022)@[b49da8b8f3...](https://github.com/maxieds/FlowersForMama2022/commit/b49da8b8f3280a78ad05f70c34af8f202417cc88)
#### Wednesday 2022-04-06 02:57:13 by Maxie D. Schmidt

The reason I'm ugly ;)

Me to Mama outside the ATL vape shop to get CBD oil: "Couldn't you have had sex with someone prettier?" [She laughs] Then again, the woman did teach me to read at three years old...

---
## [SPP922/tronj](https://github.com/SPP922/tronj)@[ac59574dba...](https://github.com/SPP922/tronj/commit/ac59574dba154ca808e08c80c13c815ec00316e7)
#### Wednesday 2022-04-06 03:52:05 by KI5FPL

*: rm instruction, fuck official, your ugly code sucks

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[b995fbe31b...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/b995fbe31b87402d3da2f8e98cec1f5659e52a47)
#### Wednesday 2022-04-06 04:13:19 by Zonespace

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
## [wrongway213/kernel_google_coral](https://github.com/wrongway213/kernel_google_coral)@[c95a727783...](https://github.com/wrongway213/kernel_google_coral/commit/c95a727783e0c311a6da9aa34e911fbf691ef162)
#### Wednesday 2022-04-06 04:46:47 by Maciej Żenczykowski

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
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 158835517
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5

---
## [Y0SH1M4S73R/mlua](https://github.com/Y0SH1M4S73R/mlua)@[71abededbc...](https://github.com/Y0SH1M4S73R/mlua/commit/71abededbcffa2e96f3abc7458432622976b730c)
#### Wednesday 2022-04-06 05:29:10 by Y0SH1M4S73R

Merge branch 'master' into fuck-you-uninlines-your-luaL_checkstack-

---
## [silont-project/kernel_xiaomi_surya](https://github.com/silont-project/kernel_xiaomi_surya)@[4c4cf87832...](https://github.com/silont-project/kernel_xiaomi_surya/commit/4c4cf87832d42e109a16b282fff73916561a93b1)
#### Wednesday 2022-04-06 06:28:50 by Peter Zijlstra

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
Signed-off-by: azrim <mirzaspc@gmail.com>

---
## [freedesktop/NetworkManager](https://github.com/freedesktop/NetworkManager)@[8df82731a4...](https://github.com/freedesktop/NetworkManager/commit/8df82731a479f2a88ae76165331b30724b59ea58)
#### Wednesday 2022-04-06 10:16:37 by Lubomir Rintel

nmcli.h: tidy up boolean struct members

Use bitfields to save a few bytes. This involves swapping gboolean for
bool and some reordering in order to get them grouped together.

The patch looks horrible, because clang-format decides to put itself and
seem to go out of its way to make this whole file look idiotic.
What can you do.

---
## [BrandonJorgen/Cavalry](https://github.com/BrandonJorgen/Cavalry)@[dc9758887f...](https://github.com/BrandonJorgen/Cavalry/commit/dc9758887f05c31195d9d8dc7a4fa7212b00292b)
#### Wednesday 2022-04-06 10:23:55 by Brandon Jorgensen

Merge pull request #261 from stevOOOOOOOOOO0/StephenDevelop

i hate my life please

---
## [LinkBoi00-Development/android_kernel_xiaomi_cannon](https://github.com/LinkBoi00-Development/android_kernel_xiaomi_cannon)@[559f0ef0d8...](https://github.com/LinkBoi00-Development/android_kernel_xiaomi_cannon/commit/559f0ef0d887c76383a741b36ecd79e895bc2936)
#### Wednesday 2022-04-06 10:31:14 by Wang Han

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
Signed-off-by: LinkBoi00 <linkdevel@protonmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[e653aeac8e...](https://github.com/mrakgr/The-Spiral-Language/commit/e653aeac8efaf62739e27e4cada2a69b11bada22)
#### Wednesday 2022-04-06 11:05:43 by Marko Grdinić

"10:25am. Let me finish Frieren and I'll watch the talk by Schmidhuber. I feel groggy and am not in the mood for making mud right off the bat.

https://youtu.be/2GgGVdkq2bU
Meta-Learning Machines in a Single Lifelong Trial

Schmidhuber is getting into the Youtuber game.

https://youtu.be/2GgGVdkq2bU?t=200

Maybe he is right. I would bet on genetic programming, but that is because I don't know how to make use of RNNs to do what he is talking about.

https://youtu.be/2GgGVdkq2bU?t=591

Hmmm...maybe I should try thinking about this seriously. Placing checkpoints makes sense, but they'd have to be rough and spaced out in time. Even if this worked, it is not a problem, the problem is having an algorithm that can learn representations in a stable manner while doing self improvement.

10:50am. Maybe using checkpoints would be more principled than using a population based approach. But the later could have diversity benefits.

And what does it matter either way, trying to stich together code would be hard anyway.

11:05am. He is just rehashing his old stuff here. Nothing new to talk about. Forget it. Let me chill a bit more and then I will get started.

11:30am. Time for some mud action.

Let me get on with it.

https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-y8q6-tgQjZc
Getting Started With Substance 3d Designer

https://youtu.be/y8q6-tgQjZc?t=60

Oh wow, you can actually bring in substance materials directly into Maya. Though in that Blender course, Shrimp did say that blurs would be impossible. So how would that work?

11:45am. Based on the intro section, I should gain a lot once I go through this course. In the tree bark one he just flies over the nodes and does not explain much of his thought process. But if I could understand the things in this course, I'll be able to do vastly more than the knot patterns.

https://youtu.be/k6MrHOGBy84?t=303

So I can link my own 3d shapes like this.

https://youtu.be/LvvsuKhc3wc?t=555

The video explaining to me how to do the materials is actually super useful.

1pm. https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-wGBsKB5sFMw

I was really starting to get into it and lost track of the time. Let me pause here.

https://mangadex.org/title/4c86f38a-cead-4575-a9c3-acf7261a58ff/meikyuu-black-company

It was a complete accident that I saw this being uploaded on Dex's feed. I never expected translations for this given that its licensed. Nice. Things are looking good. Also I remembered that I am yet to finish UQ Holder. Let me focus on that during the break.
"

---
## [pdx-tools/pdx-tools](https://github.com/pdx-tools/pdx-tools)@[07cc2a09a2...](https://github.com/pdx-tools/pdx-tools/commit/07cc2a09a24f5aa2115889b3c2df9884789bbc30)
#### Wednesday 2022-04-06 12:21:01 by Nick Babcock

Allow recording map timelapse into a video

This feature allows users to capture a timelapse into a video recording
to download and share. This implemented at a high level by using a
[canvas's `captureStream`][2] and piping that to a [`MediaRecorder`][3].

Users may choose what resolution to render the map as well as the how
fast the timelapse progresses.

Conceptually simple, but several problems arose.

Capturing the map's canvas omits UI elements like the current date in a
timelapse, something that seems critical when evaluating a timelapse. To
embed a date in the recording, we'd need to either send text into the
map or we could copy the map's canvas into a separate canvas that uses
the 2d api, which has better support for text and we could record that
one instead. While copying around map canvas data seems inefficient, it
was deemed better than needing to figure how to embed rapidly updating
text into WebGL. To support the copy use case the webgl map exposes a
callback (`onCommit`) right after it has rendered so the recording
canvas can copy it hot off the press.

Since users will want the option to record the entire map, the recording
logic communicates to the canvas that it'll be assuming control of the
size of the canvas. Seeing the canvas expand beyond one's viewport may
be unsightly, but it was the most intuitive way to get the resolution
necessary for the recording. The good news is that we restore the map
state when the recording is done so the user's focus point and scale
will not have changed.

The hardest part about the implemenation is all the coordination between
updating the map, progressing the timelapse, and making sure that
recording captures both the start and tail end of the timelapse.

For instance, there are some variations in browser implementations of a
canvas's capture stream and the media recorder. The biggest one is that
chrome would cut several seconds out of a recording especially when
there was a lack of data (like when using a freeze frame at the end).
The solution is extremely hacky: when the recording stops, repeatedly
write a transparent rectangle until we the media recorder emit non-empty
data.

That same technique (writing transparent data) is used to synchronize
the start of the recording with the start of the timelapse.

Another variation is that Chrome's canvas stream needed to be updated
every 250ms or it wouldn't register any changes. This is why the minimum
intervals per second is 4.

The output of a recording is a webm file. While this format is the [
recommended approach for video playback][4], webm upload is not often
supported sites like reddit. The solution is that after the recording is
finished, transcode it into an mp4 file using [`ffmpeg.wasm`][5]. This
is a pretty extreme approach as ffmpeg is a large download (several
times larger than all the pdx.tools wasm bundles put together), and may
take several minutes to complete while using 100% CPU usage. But the end
result is worth it if users can take the download and immediately upload
it elsewhere with minimal hassle.

However I still view the mp4 export as a bit experimental as every few
recordings ffmpeg takes 10x as long to process the input and the output
is horribly choppy. I'm not sure what causes this, but I'm assuming
other users will experience this issue, so my recommendation to those
who constantly experience it is to accept the webm output and convert it
to mp4 through a 3rd party tool.

Needed to add two new headers: `Cross-Origin-Embedder-Policy:
require-corp` and `Cross-Origin-Opener-Policy: same-origin` in order to
get [ffmpeg.wasm to work][0] as it relies on `SharedArrayBuffer` and its
[security requirements][1]

The timelapse and recording work through `requestAnimationFrame` which
is paused when running in a background tab ([source][6]), so in order to
avoid corrupting the canvas capture, a warning is presented to the user
when they switch back to our tab (as one can't eagerly detect tab
switching in the browser beforehand), informing them of this
restriction. At least the MP4 transcoding can happen in the background.

[0]: https://github.com/ffmpegwasm/ffmpeg.wasm#installation
[1]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer#security_requirements
[2]: https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/captureStream
[3]: https://developer.mozilla.org/en-US/docs/Web/API/MediaRecorder
[4]: https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Video_codecs#recommendations_for_everyday_videos
[5]: https://github.com/ffmpegwasm/ffmpeg.wasm
[6]: https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame

---
## [Brycew73/MSweeper](https://github.com/Brycew73/MSweeper)@[8d861d632c...](https://github.com/Brycew73/MSweeper/commit/8d861d632c9cf4045e6ff7b2cfe437bd68048fa2)
#### Wednesday 2022-04-06 12:23:04 by Matthew

Hi guys, sorry for the wait on this. Here's what I added:

Changed: Guest Servlet, SignInServlet, signInController, index.jsp
Added: highScoreController

SignIn will now push into Index if the correct username and passwords
are selected. Guest will also push into Index if the name is valid. Both
will result in the username being displayed at the top of the Index
page.

I added the fake database in. It displays the current list of high
scores into the Index page. As of right now, it might not work if you
pull it since I'm running Derby through my local files. Bryce said that
he's going to try to add the Derby project from our lab into Git, so
until then, the database will most likely not work.

***Note: I have a slightly different version of JDK, but since Eclipse
lets you change which version you use pretty easily, I didn't think much
of it. If we want, we should try to find a version we all can use. I
didn't want to download anything since I'm not sure what everyone's
using.
Let me know if you have any questions. Thanks!

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[c8ef62c1fb...](https://github.com/ZephyrTFA/tgstation/commit/c8ef62c1fb7027ea58b569f0e4bd7df5a7d58935)
#### Wednesday 2022-04-06 12:43:51 by LemonInTheDark

Fixes bartender drink throwing, makes smashing always spill (#65698)

Tohg's initial pr (9c0b0e5d4cc236e365ef0229400cefe98b184964) was rather poorly argued and a bit misleading, but the actual changes were honestly kinda harmless. You could already have thrown beakers to splash shit on someone, it wasn't a big issue.

However it did end up breaking bartending, because it removed the ranged
args that normally get passed into smash and SplashReagent.

I went in intending to fix that, but noticed some dumb copypasta in
broken bottle code, and decided to just start from there.

I've moved that logic to a proc on the broken bottle, and made smashing
a bottle on something splash its contents too.

I can't think of a case where you wouldn't want this, so I'ma just go
for it. Prevents future mistakes like this too.

Oh and because I'm passing ranged in properly now, splashing will not
always splash the whole amount of the bottle's reagents. Doubt that
really matters tho.

Love ya bestie

---
## [expo/expo](https://github.com/expo/expo)@[d92760eeb2...](https://github.com/expo/expo/commit/d92760eeb25ebd325b0b06a3c3f49bbfe348d4d0)
#### Wednesday 2022-04-06 12:59:45 by Łukasz Kosmaty

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
## [favelado-web/react](https://github.com/favelado-web/react)@[c7b4497988...](https://github.com/favelado-web/react/commit/c7b4497988e81606f1c7686434f55a49342c9efc)
#### Wednesday 2022-04-06 13:13:32 by Andrew Clark

[Experiment] Lazily propagate context changes (#20890)

* Move context comparison to consumer

In the lazy context implementation, not all context changes are
propagated from the provider, so we can't rely on the propagation alone
to mark the consumer as dirty. The consumer needs to compare to the
previous value, like we do for state and context.

I added a `memoizedValue` field to the context dependency type. Then in
the consumer, we iterate over the current dependencies to see if
something changed. We only do this iteration after props and state has
already bailed out, so it's a relatively uncommon path, except at the
root of a changed subtree. Alternatively, we could move these
comparisons into `readContext`, but that's a much hotter path, so I
think this is an appropriate trade off.

* [Experiment] Lazily propagate context changes

When a context provider changes, we scan the tree for matching consumers
and mark them as dirty so that we know they have pending work. This
prevents us from bailing out if, say, an intermediate wrapper is
memoized.

Currently, we propagate these changes eagerly, at the provider.

However, in many cases, we would have ended up visiting the consumer
nodes anyway, as part of the normal render traversal, because there's no
memoized node in between that bails out.

We can save CPU cycles by propagating changes only when we hit a
memoized component — so, instead of propagating eagerly at the provider,
we propagate lazily if or when something bails out.

Most of our bailout logic is centralized in
`bailoutOnAlreadyFinishedWork`, so this ended up being not that
difficult to implement correctly.

There are some exceptions: Suspense and Offscreen. Those are special
because they sometimes defer the rendering of their children to a
completely separate render cycle. In those cases, we must take extra
care to propagate *all* the context changes, not just the first one.

I'm pleasantly surprised at how little I needed to change in this
initial implementation. I was worried I'd have to use the reconciler
fork, but I ended up being able to wrap all my changes in a regular
feature flag. So, we could run an experiment in parallel to our other
ones.

I do consider this a risky rollout overall because of the potential for
subtle semantic deviations. However, the model is simple enough that I
don't expect us to have trouble fixing regressions if or when they arise
during internal dogfooding.

---

This is largely based on [RFC#118](https://github.com/reactjs/rfcs/pull/118),
by @gnoff. I did deviate in some of the implementation details, though.

The main one is how I chose to track context changes. Instead of storing
a dirty flag on the stack, I added a `memoizedValue` field to the
context dependency object. Then, to check if something has changed, the
consumer compares the new context value to the old (memoized) one.

This is necessary because of Suspense and Offscreen — those components
defer work from one render into a later one. When the subtree continues
rendering, the stack from the previous render is no longer available.
But the memoized values on the dependencies list are. This requires a
bit more work when a consumer bails out, but nothing considerable, and
there are ways we could optimize it even further. Conceptually, this
model is really appealing, since it matches how our other features
"reactively" detect changes — `useMemo`, `useEffect`,
`getDerivedStateFromProps`, the built-in cache, and so on.

I also intentionally dropped support for
`unstable_calculateChangedBits`. We're planning to remove this API
anyway before the next major release, in favor of context selectors.
It's an unstable feature that we never advertised; I don't think it's
seen much adoption.

Co-Authored-By: Josh Story <jcs.gnoff@gmail.com>

* Propagate all contexts in single pass

Instead of propagating the tree once per changed context, we can check
all the contexts in a single propagation. This inverts the two loops so
that the faster loop (O(numberOfContexts)) is inside the more expensive
loop (O(numberOfFibers * avgContextDepsPerFiber)).

This adds a bit of overhead to the case where only a single context
changes because you have to unwrap the context from the array. I'm also
unsure if this will hurt cache locality.

Co-Authored-By: Josh Story <jcs.gnoff@gmail.com>

* Stop propagating at nearest dependency match

Because we now propagate all context providers in a single traversal, we
can defer context propagation to a subtree without losing information
about which context providers we're deferring — it's all of them.

Theoretically, this is a big optimization because it means we'll never
propagate to any tree that has work scheduled on it, nor will we ever
propagate the same tree twice.

There's an awkward case related to bailing out of the siblings of a
context consumer. Because those siblings don't bail out until after
they've already entered the begin phase, we have to do extra work to
make sure they don't unecessarily propagate context again. We could
avoid this by adding an earlier bailout for sibling nodes, something
we've discussed in the past. We should consider this during the next
refactor of the fiber tree structure.

Co-Authored-By: Josh Story <jcs.gnoff@gmail.com>

* Mark trees that need propagation in readContext

Instead of storing matched context consumers in a Set, we can mark
when a consumer receives an update inside `readContext`.

I hesistated to put anything in this function because it's such a hot
path, but so are bail outs. Fortunately, we only need to set this flag
once, the first time a context is read. So I think it's a reasonable
trade off.

In exchange, propagation is faster because we no longer need to
accumulate a Set of matched consumers, and fiber bailouts are faster
because we don't need to consult that Set. And the code is simpler.

Co-authored-by: Josh Story <jcs.gnoff@gmail.com>

---
## [blahberi/SIEPS](https://github.com/blahberi/SIEPS)@[542443ae43...](https://github.com/blahberi/SIEPS/commit/542443ae43e0ee15cf1cc40b77c5b4f8c3e0a59e)
#### Wednesday 2022-04-06 13:16:37 by kamoodi

ok i have no idea how his code works so i reverted it but theres an easy bug i fixed so youre welcome

fuck you i dont want to write a description

---
## [spicetify/spicetify-cli](https://github.com/spicetify/spicetify-cli)@[0a89573c1c...](https://github.com/spicetify/spicetify-cli/commit/0a89573c1ce2f4ed3f4cdaac7651bc34dffb3a0a)
#### Wednesday 2022-04-06 14:40:25 by Łukasz Ordon

fix: `New Releases` custom app for Spotify 1.1.81+ (#1563)

* Fix `New Releases` custom app for Spotify 1.1.81+

- Based on proposed fix for `Shuffle+` (#1559)
- Fixes #1539 #1530 

Notes:
- Can probably be written nicer - this is my scuffed attempt to fix it
- May or may not actually show all new releases for all followed artists - have over 665 of them but I don't think I'm getting all of them (see below)
- May or may not return `error 500` (added `.catch()` block keeps it from breaking whole custom app)

* Minimize `internal server error: 500`...

...for big libraries of followed artists.

Changes:
- Change `URL` to query only discographies
- Limit amount of queried albums to 5

Notes:
- This does **NOT** fixes erroring fully - it only maxes out amount of data you can query before getting rate limited
- The more options you select (ex. albums + EPs + podcasts), the less data you may receive
- To max number of albums received, I recommend to select only `Albums` (since `Singles and EPs` will probably get displayed anyway...)

* Add notifications when error occurred

Notifications added:
- Error code (`500`, `429` etc.)
- Amount of followed artists to fetch releases from
- Amount of followed artists failed to fetch releases from

I guess we have to get along with getting `500-ed` - one time it fetches everything instantly, second time it drops 60 artists...

* "Prettify" file to pass `Prettier` test

* Fix filtering, counter...

- Fixing filtering as no matter was what set in config, it always displayed everything as "Album"
- Fixing "Missing releases from..." counter - should properly reset now

What broke again:
- "Appears on" releases cannot be retrieved with that API endpoint - this filter is just there and doesn't do anything - this prevents from showing everything as "Appears on" etc.

Notes:
- There seem to be an API endpoint for retrieving "Related content" stuff - problem is that would query everything TWICE... which breaks everything even more (and we don't wanna do that)
- If someone knows how to query everything using separate endpoint without doing it 4 times, let me know...

* Forgor `( )`... Oops... :skull:

I forgor 💀

* Include requested changes

Changes:
- Properly encode URI including variables
- Make `limit` variable customizable via settings (set default to 5)
- Make error messages as "dev console only"

Notes:
- Errors displayed in console may be a little spammy - if we get error early, there may be lots of lines displaying it + counter...
   * I'm not too sure how to tackle this - just remove them altogether? Or is there a function that could "suppress" them?
   * Switching from normal `log` to `debug` may help a little as they will be only visible if user has set their console log level to include `Verbose`
- Making `limit` customizable may lead to even more errors but fuck it I guess - it's better to have a choice than not, right?
   * It can be manually input via custom app settings (same place where other options are) - there is no list etc. - it's just normal input field
- Set `offset` value as const `0` and not making it customizable (cause why would you want to start searching from ex. 3rd album instead of beginning, right?)
- Leaving `Fetching releases from...` notification cause it looks cool - it's fun to know how many followed artists you have 😆

---
## [nerdhannn/android_kernel_asus_sdm660](https://github.com/nerdhannn/android_kernel_asus_sdm660)@[c15e3c94d3...](https://github.com/nerdhannn/android_kernel_asus_sdm660/commit/c15e3c94d3134895dc92eeed10e04411a37150d8)
#### Wednesday 2022-04-06 14:43:31 by Dave Chiluk

sched/fair: Fix low cpu usage with high throttling by removing expiration of cpu-local slices

commit de53fd7aedb100f03e5d2231cfce0e4993282425 upstream.

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
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Ratoriku <a1063021545@gmail.com>
Signed-off-by: Peppe289 <gsperanza204@gmail.com>
Signed-off-by: RyuujiX <saputradenny712@gmail.com>

---
## [Sanster/lama-cleaner](https://github.com/Sanster/lama-cleaner)@[eea85b834e...](https://github.com/Sanster/lama-cleaner/commit/eea85b834eee527f3a05fca9410e671c935603b2)
#### Wednesday 2022-04-06 15:05:32 by blessedcoolant

Complete GUI Refactor

This patch brings in a massive number of changes to the frontend of the application. Please feel free to discuss the proposed changes with me at any time.

Implemented Recoil as a state management system.
Why Recoil? It is a robust library built by developers at Facebook for state management. It has an  extremely simple API for implementation that is in sync with React syntax compared to any other state management system out there and works amazingly well. While the official release status is beta as it becomes fully featured, the library is already used in various systems at Facebook and is very stable for the use cases of this application.

Why global state management? One of the major issues I saw with the current file structure is that there is minimal code splitting and it makes further development of the frontend a cumbersome task. I have broken down the frontend into various easy to access components isolating the GUI from the logic. To avoid prop drilling, we need global state management to handle the necessary tasks. This will also facilitate the addition of any new features greatly.

Code Splitting. Majority of the components that can be isolated in the application have now been done so.
All New Custom CSS & Removal of Tailwind
While Tailwind is a great way to deploy beautiful interfaces quickly, anyone trying to stylize the application further needs to be familiar with Tailwind which makes it harder for more people to work on it. Not to mention, I am not a particular fan of flooding JSX elements with inline CSS classes. That makes reading the code extremely hard and bloats up component code drastically.

As a replacement to Tailwind, I implemented a custom styling system using SCSS as a developer dependency.

In the new system, all the general and shared styles are in the styles folder and all the component styles are in the same folder as the component for easy access.The _index.scss file now acts as a central import for every other stylesheet that needs to be loaded.

What Changed?
The entire application looks and feels like the current implementation with minimal changes.
The green (#bdff01) highlight used in the application has now been changed to a bright yellow (rgb(255, 190, 0)) because I felt it better suited the new Dark Mode (see below).
The swipe bar for comparing before and after images has now been removed and instead the comparison is a smooth fade effect. I felt this was better to analyze image changes rather than a swiper. // Can add the swipe back if needed.

Dark Mode
A brand new Dark Mode has been added for the application. Users can enable and disable by tapping the button in the header or by using the Shift + D hotkey.

Other Misc New Features
When the editor image is now zoomed out to its default size, the image now also gets centered back.

TODO
The currently used react-zoom-pinch-pan module is not mobile friendly. It does not allow brush strokes. Need to figure out a way to fix this.
Further optimization of the frontend code with better code splitting and performance.
When using the LaMa model, the first stroke has a delayed response from the backend but the ones that follow are almost immediate. I believe this is happening because of the initialization of the model on the first stroke. I wonder if either of us can look at it and see if this can somehow be preloaded so the user experience is smooth from the first stroke.
Enable threading for the desktop application mode so flaskwebgui does not block the main applications Python console.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[1b7d7d9327...](https://github.com/pytorch/pytorch/commit/1b7d7d93276eb37c009905ef87ea9c2a7c95481e)
#### Wednesday 2022-04-06 16:41:05 by Brian Hirsh

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
## [EmJayGee/terminal](https://github.com/EmJayGee/terminal)@[446f280757...](https://github.com/EmJayGee/terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Wednesday 2022-04-06 17:46:49 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4095178760...](https://github.com/mrakgr/The-Spiral-Language/commit/409517876050546b1637d699735a87908087814b)
#### Wednesday 2022-04-06 18:30:37 by Marko Grdinić

"1:20pm. Why didn't they remove the kanji from the word bubbles on page 25 vol 7? Scanlators can be such lazy pieces of shit. I think I should just wait for the licensed release.

2:35pm. Done with breakfast and chores. The weather is starting to get warmer again. The spring has arrived.

Let me...oh yeah, is Dedro vol 17 out yet? Nope. Then let me just resume the course.

Small shapes part one.

https://youtu.be/iCcRjlXRrB4?t=436

To get something like this he could have started with perlin and sparsified it.

...No, I was wrong.

Nope. Moving the levels midpoint is really equivalent to using the power.

3:55pm. Done wit 02-05. I don't like this. I am losing track of what is supposed to be what at this point. The initial shape was fine, the dirt map was one thing, but once I start mixing things together, it gets messy. At this point I am really missing color to make things more distinct. I am not a fan of just ramming crap on top of one another.

https://youtu.be/5-rqV43ejoQ?t=335

What is this? Let me play with it a bit.

4:20pm. I do not get it. What the hell is slope blur supposed to be doing?

4:35pm. https://youtu.be/4-MB8o16R4c
[SUBSTANCE DESIGNER] Non Uniform Blur - Know Your Nodes [ENG]

I am trying to get a better explanation of what slope blur is doing.

4:50pm. Let take a break here. I can't find a good explanation, but it does not matter. I suppose it is self explatory enough.

5:05pm. Let me resume. I need to get back on track.

5:20pm. Ok, instead of watching let me put down some of my own shapes.

5:40pm. https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-K2l2lFsPYb0

Let me go through 02-08.

6:20pm. Done with the mounds.

https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-AdIn2tgjphk

Now comes 02-09. I am starting to get fatigued.

6:40pm. I was into it, and now I am out of it. Let me watch one more video I really don't feel like messing with rocks. I got the sense of it.

https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-VU9Oz5VBE2Q

Let me watch it, let me just watch it.

...Lunch time.

7:05pm. Let me give watching 02-10 a try. If it does not work, I'll just leave it for tomorrow. I should be able to finish this series completely tomorrow.

Let me do the pebbles and then I will watch it.

7:30pm. Did it. This is not that hard. Though it drains the time. The pebbles really don't look that good right now. I am having trouble making them not look like regular ground. Maybe it will look better once I texture them. Nevermind it right now.

7:35pm. Let me watch 02-10 as I said I would and I will call it a day.

https://youtu.be/VU9Oz5VBE2Q?t=873

Hmmm, merging it like this is pretty interesting. I bet he'll use the original shape to mask out the rest of the texture.

...It seems he did not, he just multiplied it with the original. That works as well.

https://youtu.be/VU9Oz5VBE2Q?t=1085

Couldn't he just screen the original?

8pm. Done for today. Let me stop here.

https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-Substance-3D-Designer/youtube-Cjv4DI76Fow

I think I've gone through about 2/3rds of it. I'll finish this tomorrow. Seeing Ds being used in action sure makes it a lot more understandable. One big side benefit of all of this is that it really improved my understanding of blending modes. This is something that was a big mystery to me in my Clip Studio days last year.

I think after I finish this course, I'll continue on to the 1.5 hour wood plank one. I have the bug for this now. I'll continue studying Designer until I am happy with my level of knowledge. I think a few more days of this should hugely increase my skill. Already I know how to deal with the wood pattern for my desk.

Just from studying it intently in the last few days, I've already learned quite a lot.

But as much as I know now, I still wouldn't know how to color the texture I've made today for example. I am curious how he will do that.

8:15pm. It is fine to do things like this. Trying to rush my goal would leave too much by the wayside. Speedrunning is done after you've beaten the game a few times, not right off the bat.

Either way, that desk and the rest of the props will get finished by the end of the month and probably a lot sooner. After that I'll move to the other scenes and get Heaven's Key going. I'll use all the tools that I can to get the job done. Houdini for cities, Blender for props, Clarisse for layouting, Substance Painter for texturing. Designer if I really need it for something. Clip Studio for 2d.

Ugh, all these tools together would cost a ton of money. I guess I'll just 'borrow' them until I get to the point where they are only 10% of my yearly income. I hope I'll actually manage to get to that point.

You never know, I could make great art, story and music and still be completely ignored. Though given the lengths I will be going to make things work that really should not happen. The average artist is really good at a single or two things at most. But I will be bringing in the high ranks across the board. Not a single aspect will be left untouched. I will cover all the areas until I am strong at all of them.

This is the proper way to cultivate art skills. People who grind boxes all day have nothing on me.

It is a bit like being a switchblade wizard who has a spell for any situation. That is the kind of artist I am going to become.

It is a pity I could not succeed in RL, but my reason for making Spiral is still alive. Spiral will be necessary to program those AI chips.

Until I get a chance to make use of them, I'll hold steadfast to my new way. I've put in half a decade into programming, so there is no reason why I can't put in half a decade into art to reach the pinnacle of my abilities."

---
## [alphagov/govuk-infrastructure](https://github.com/alphagov/govuk-infrastructure)@[ed382d7f66...](https://github.com/alphagov/govuk-infrastructure/commit/ed382d7f664a7d4bb2bfdc5110c6d1e20795f852)
#### Wednesday 2022-04-06 19:39:14 by Chris Banks

Update EKS module to v18 and fix up security group rules.

See https://github.com/terraform-aws-modules/terraform-aws-eks/releases
for changes.

In v18 of `terraform-aws-modules/eks`, the control plane nodes and
worker nodes belong to different AWS security groups by default, per
Amazon's recommendation. It's possible to revert to the previous
behaviour by setting a flag, but sticking with the recommendation means
we'll be able to control access to the control plane independently of
access to services running on the nodes.  It's slightly more complex in
theory, but I don't think introduces any extra operational/maintenance
complexity in practice (and will significantly simplify maintenance if
we should ever need to tighten the security group rules).

The `eks` module now outputs the cluster OIDC provider URL so we no
longer have to construct it ourselves.

Learning from our experience so far, we also allow minor (but not major,
i.e. breaking) version upgrades of the `eks` module to happen
automatically from now on, so that we won't keep getting bitten by bugs
which have already been fixed upstream when we make changes to live
clusters. It's very rare for one of these modules to introduce a serious
bug in a minor update - and we should be checking the diffs when
applying anyway - so on balance this is preferable to over-pinning and
the inevitable version rot that ensues. TF Cloud will further improve
the situation, hopefully in the near future.

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[54403a1ca0...](https://github.com/TheBoondock/tgstation/commit/54403a1ca0a1d83302430bbb54a0d6bc561f0098)
#### Wednesday 2022-04-06 20:04:56 by FinancialGoose

Fixes conveyor runtime (#65788)

Conveyor would runtime whenever it is right clicked with an item

Fixes #64595 (Runtime on conveyor for right clicking)

fixes a runtime with conveyor where right clicking it with any item would cause a runtime

Mothblocks rant from the issue report below, you've been warned:

Because right-clicking in BYOND is horse-shit. It pipes it all through the normal Click and only tells you it's a right-click through a flag. This means that on anything that isn't prepared, right-clicking is the same as left-clicking, which is terrible UX that only exists in SS13.

Nothing should return ..() from attackby_secondary, because the default is the legacy behavior of making right-click pass as left-click (which I want to kill ASAP, once nothing uses the stupid flags anymore).

Remove else return ..(), and make this whole thing do return SECONDARY_ATTACK_CANCEL_ATTACK_CHAIN.

---
## [woo200/thatkitebot](https://github.com/woo200/thatkitebot)@[0fa6685c66...](https://github.com/woo200/thatkitebot/commit/0fa6685c66f08908ca179d526a8156bc771a8b88)
#### Wednesday 2022-04-06 20:26:57 by Jack Woo

Added UWUify command  (#43)

* Added 8ball command

* damn i am an idiot

* i should probably check this next time

* Added uwuify command (im sorry mom)

---
## [darkuser89/duckstation](https://github.com/darkuser89/duckstation)@[f9212363d3...](https://github.com/darkuser89/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Wednesday 2022-04-06 20:48:18 by IlDucci

Spanish translation overhaul + Addition of es-ES alternative

In its current state, the Spanish translations for Duckstation are a mess of different dialects, multiple translations for the same terms, mistranslations or excessively literal translations, and typos.

It's a shame, because you could feel that the initial translations were done with care, but were muddled with future revisions.

This commit tries to solve all of these and also change the initial decision of the first translator to have an "universal" "neutral" Spanish, as time has proven it's not possible without a dedicated translator who actually wants to have one Spanish language for all Spanish-speakers across the globe.

I'm not going to be that one, so the next option would be to duplicate the Spanish translations into two: one for the Spanish-speaking American people (called "Latin American Spanish", "español de Hispanoamérica", code es-419") and one for the European Spanish speakers (called "Spanish (Spain)", "español de España", code es-ES).

This distinction is used in multiple software applications that managed to have translators for different languages, and should also funnel any future Latin American Spanish and European Spanish translators to the corresponding file.

I have tried to follow as many existing terms and constructions as possible, restoring and/or rewording any phrasal constructions that were disunified by the multiple translators.

Since I have a limited experience with Latin American Spanish, this commit should be sent as a draft for additional revisions. I'm open to stick to having a single Spanish language, but it has to be done RIGHT.

This is an overview of changes across the board:
 - Added missing translations for QT and Android builds.
 - Unified translations between those.
 - Updated the QT file with the latest string values.
 - Massive removal of Title Uppercasing inherited from English in menu strings (the rules set by the Royal Academy of the Spanish Language, or RAE, limit the areas where Title Uppercasing is considered correct in Spanish. Menu names and window header texts are not within those areas).
 - Unified the treatment of users in the Latin American version to formal "ustedeo". This treatment could be modified with additional input.
 - Removed any gendering assumptions from any string directed towards the user (Are you sure...?, changed ¿Está/s seguro...? with ¿Seguro que...?)
 - Naturalization rewrites.
 - Typo corrections.
 - Gender corrections over definitive terms.
 - Adding missing NBSPs after required mathemathical characters or units.
 - Mass replacement of double/single quotes with angled quotes (the ones approved for Spanish).
 - Quoted non-Spanish, non-proper noun English words as dictated by RAE.
 - Removal of unwanted hyphens to join words (Auto-detectar with Detección automática, post-procesamiento with posprocesamiento). In Spanish, hyphens tend to separate, rather than join.
 - Revision of the compound forms, unified depending on Latin American Spanish or European Spanish.
 - Lowercased the first word of a text between parenthesis (Spanish rules dictate that they should be considered a continuation of the phrase, and thus, they should start with lowercase unless it's a proper noun or a word that must be uppercased) and corrected the positions between periods and parentheses.
 - Unified the accentuation rules for the adverb solo/sólo and the demostrative pronouns (este/ese/aquel) by removing all accents in European Spanish (following the RAE's 2010 suggestions) or keeping/adding them for Latin American Spanish (the 2010 rule ended up being a suggestion because while Spain has mostly deprecated those accents, it appears that the Latin American countries have not). To discuss?
 - Tweaked the key shortcuts for the QT menu to minimize duplicates.
 - Terms unified (this list doesn't represent the entirety of the changes):
    - Failed to (Fallo al/Error al): Fallo al
    - Hardcore Mode (Modo Hardcore/Modo Difícil): «hardcore» mode (Foreign non-proper nouns should be quoted, RetroAchievements does not have an official Spanish translation, so the term should be kept in English)
    - Enable/Disable (habilitado/deshabilitado/activado/desactivado/activo/inactivo): habilitado/deshabilitado
    - host (host/anfitrión/sistema): sistema, TO BE DETERMINED AND UNIFIED
    - Signed (numbers; firmados): (números) con signo
    - scan (verb and noun; escanear): buscar/búsqueda
    - Clear (something, like bindings or codes; despejar, limpiar): borrar/quitar
    - requirement (of a system, requisito/requerimento): requisito
    - input (of a controller, control): entrada
    - Threaded X (hilo de X): X multihilo
    - Frame Pacing (frame pacing): duración de fotogramas
    - XX-bit (XX-bit): XX bits (proper form)
    - Widescreen (screens, widescreen hacks; pantalla ancha, pantalla panorámica): pantalla panorámica
    - Antialiasing (anti-aliasing): Antialiasing (considered a proper noun by NVidia, doesn't need that hyphen)
    - hash: «hash» (could be discussed as "sumas de verificación", like on Dolphin)
    - Focus Loss (perder el foco): ir/entrar en segundo plano
    - toggle (verb for hotkeys, activar): alternar (as the key alternates between enabling and disabling the function, while "activate" might sound like it's just the enable part)
    - Rewind (function; retrocediendo, retrocedimiento): rebobinado (to discuss on LATAM Spanish)
    - shader (shader/sombreado): sombreador
    - resume (resumir): reanudar, continuar (resumir is a false friend)
    - Check (verb; chequear/revisar/comprobar): chequear (LATAM Spanish), comprobar (European Spanish)
    - Add (something; añadir/agregar): agregar (LATAM Spanish, to discuss) or añadir (European Spanish)
    - Enter/Input (ingrese, inserte): ingresar (LATAM Spanish) or introducir (European Spanish)
    - mouse (device; mouse/ratón): mouse (LATAM Spanish), ratón (European Spanish)
    - Auto-Detect (Auto-detectar): Detección automática
    - Controller (control): mando (for European Spanish only)
    - run (a game, the emulator; correr): ejecutar, funcionar (for European Spanish only)

---
## [EveryStepYouTake/sojourn-station](https://github.com/EveryStepYouTake/sojourn-station)@[9410031f12...](https://github.com/EveryStepYouTake/sojourn-station/commit/9410031f12ac9c565933ed7c29af071d31e4a807)
#### Wednesday 2022-04-06 21:30:20 by Kazkin

Rise of the Most Unpopular PR of All Time 2: Revengeance Rising Revelations Reborn Featuring Dante from Devil May Cry and Knuckles

-All tier 2 medical kits now have special checks that verify both perk and bio checks to allow use. All medical kits, including gauze and ointment, requires you to have 0 or greater bio to use. (Dump stating bio now has a detriment).
-Advanced bruise/burn kits require soteria medical expertise perk or 75 bio to use.
-Hunting lodge blood tongues and powder pouches require master butcher or 10 bio.
-Church medical kits require the soteria medical expert perk or 15 bio (intentionally made easy to use since they are rare, costly to mass produce, and only come from the church). Uses the soteria perk since it is essentially an easier to use advanced kit.
-Blackshield medkits now come with regular gauze and ointment in place of advanced kits. This has a side benefit of reducing storage space by 50% as these medical items are smaller.
-Most random spawners now spawn standard regular kits instead of advanced kits.
-Regular medkits and first aid kits have their spawn chance reduced.
-Cargo techs still have a chance to spawn with advanced kits (sell them to doctors)
-Ifaks now contain gauze and ointment.
-Prospector factions no longer spawn advanced kits. Due to how probability works, they now have a 1 in 20 chance to get a combat medkit kit instead of an ifak. This change effects salvagers and foremans.
-Corpsman now spawn with regular first aid kits.
-Syringes now require 15 bio to do **anything** with them.
-Autoinjectors can now be refilled using a syringe. Autoinjectors do not have a bio check.
-Blackshield kits now contain only bandages and gauze.
-Surgery now has had its difficult risen by 90 and takes 120 ticks longer unless you have the soteria advanced surgical perk or surgical mastery perk. For reference, the base difficulty of surgery is 80, tool quality, precision bonuses, and bio skill change the odds. 120 ticks is roughly 12 seconds. This timer is modified by bio skill.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f83fec97c8...](https://github.com/treckstar/yolo-octo-hipster/commit/f83fec97c857f6e36876c46207e5d9d2f811e28a)
#### Wednesday 2022-04-06 22:00:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [StHedgehog15/CS2053-project](https://github.com/StHedgehog15/CS2053-project)@[5f57e3f17c...](https://github.com/StHedgehog15/CS2053-project/commit/5f57e3f17c8ad8d12b8a4115e68b3e43d0b41170)
#### Wednesday 2022-04-06 23:00:24 by Keith LeBlanc

Delete CS2053-project/Assets directory

Removed redundant directory from repo - fuck you, redundant directory from repo >:(

---
## [Twitrik/Twitrik.github.io](https://github.com/Twitrik/Twitrik.github.io)@[48226f926c...](https://github.com/Twitrik/Twitrik.github.io/commit/48226f926c445d88441400d59b285c1fa678121d)
#### Wednesday 2022-04-06 23:27:57 by Twitrik

Create index.md

Welcome to Bean Un blooked froogs! This is a web page dedicated to providing free, unbl0cked Flash, NES and HTML gam3s. Along with providing new website makers embedable g4mes!

Everything should work. If somethings goes wrong please report an error at the Github. Thanks and Enjoy!!

----------------------------------------------------------------------

Flash Games (Running off ruffle)

Alien Hominid - Age Of War - Apple Shooter - Asteroids - Abobbos Big Adventure - Bloxorz - Bloons Tower Defence - Bubble Shooter - Color Combat - Dad n' Me - Defend Your Castle - Commando - Cubefield - Electricman 2 - The Fancy Pants Adventures - Escaping the Prison - Stealing the Diamond - Hanafuda - Hobo - Hobo 2: Prison Brawl - Miami Shark - New York Shark - This is the Only Level - Pac-Man - Papa's Pizzaria - Pong - Portal: The Flash Version - Super Mario 63 - Super Mario Flash - Mario Combat - Tetris - Meat Boy - Mini Putt - Gunblood - Riddle School - Riddle School 2 - Stick RPG - The Impossible Quiz - The World's Hardest Game - The World's Hardest Game 2 - Ultimate Flash Sonic
----------------------------------------------------------------

Other Games (Non Flash)

2048 - 8-Ball - BlackJack - Cookie Clicker - "Custom" Tetris - DOOM (Very Laggy) - Google Dinosaur - Minesweeper - MineCraft (Classic) - Mari0 - Retro Bowl - Super Mario 64 - Wolfenstein 3D - Batman (NES) - Contra (NES) - Double Dragon (NES) - Duck Tales (NES) - Friday the 13th (NES) - Mega Man 2 (NES) - River City Ransom (NES) - Super Mario Bros. (NES) - Super Mario Bros. 2 (NES) - Super Mario Bros. 3 (NES) - The Legend of Zelda (NES) -
----------------------------------------------------------------

hey bozo we´re under construction!!

Credits

---
## [Mau587/Mau587](https://github.com/Mau587/Mau587)@[5cbccff65f...](https://github.com/Mau587/Mau587/commit/5cbccff65f92461d2823c6c9463bcc204bd7be59)
#### Wednesday 2022-04-06 23:52:38 by Mau587

< Less than

**I am 35 Years old...I've wasted 34 of them. Not anymore .
I'm unclear what even < means in a code line. But it's ferkin exciting because
there's a drive I'm e that is so interested to learn. You'd have to ban me to not return.
_Mission And why....(the who comes when I become somebody).
From Waterbury Ct. Now resides in Mississippi. ( yes massive culture shock )
But with new change came new things, time. and a lot of thinking.
"Surround yourself around people who are smarter than you and observe what happens"
I am humbly a noob, eager, and have a desire in learning to code, web design. 
Hobbies include but NEVER limited too:
-Anything mechanical
-Anything electronic
-Anything fast or efficient (Both is always the goal)
I am an artist. Mostly studied anatomy privately as well at William Carey University of Arts.
-Im a tinker - er 
-a free spirited thinker
- Im a joker 
-And yes indeed I'm a midnight toker
Ps . I hate social media and people as a WHOLE. Hate and gwar phobia are not the same

---

