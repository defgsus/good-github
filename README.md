## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-31](docs/good-messages/2022/2022-07-31.md)


1,501,288 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,501,288 were push events containing 2,059,457 commit messages that amount to 116,101,007 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [zphixon/powdermilk-biscuits](https://github.com/zphixon/powdermilk-biscuits)@[d5959a38eb...](https://github.com/zphixon/powdermilk-biscuits/commit/d5959a38eb5e983e871181e0a2e0bfe2708b3bdb)
#### Sunday 2022-07-31 00:32:14 by Zack

wgpu: Fix segfault on Linux by downgrading winit

Bullshit was happening and I did *not* have the patience to fuck around
with separate versions of raw-window-handle (which why the shit did it
even change? are window handles any different between now and a few
weeks ago? i cri) anyway I made a new branch and added the peninfo
garbage and that was it. fuck,

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[e7ec359d31...](https://github.com/zx2c4/linux-rng/commit/e7ec359d3184605ad2dea74faf34c4b49b8acec8)
#### Sunday 2022-07-31 00:44:03 by Jason A. Donenfeld

random: implement getrandom() in vDSO

Two statements:

  1) Userspace wants faster cryptographically secure random numbers of
     arbitrary size, big or small.

  2) Userspace is currently unable to safely roll its own RNG with the
     same security profile as getrandom().

Statement (1) has been debated for years, with arguments ranging from
"we need faster cryptographically secure card shuffling!" to "the only
things that actually need good randomness are keys, which are few and
far between" to "actually, TLS CBC nonces are frequent" and so on. I
don't intend to wade into that debate substantially, except to note that
recently glibc added arc4random(), whose goal is to return a
cryptographically secure uint32_t. So here we are.

Statement (2) is more interesting. The kernel is the nexus of all
entropic inputs that influence the RNG. It is in the best position, and
probably the only position, to decide anything at all about the current
state of the RNG and of its entropy. One of the things it uniquely knows
about is when reseeding is necessary.

For example, when a virtual machine is forked, restored, or duplicated,
it's imparative that the RNG doesn't generate the same outputs. For this
reason, there's a small protocol between hypervisors and the kernel that
indicates this has happened, alongside some ID, which the RNG uses to
immediately reseed, so as not to return the same numbers. Were userspace
to expand a getrandom() seed from time T1 for the next hour, and at some
point T2 < hour, the virtual machine forked, userspace would continue to
provide the same numbers to two (or more) different virtual machines,
resulting in potential cryptographic catastrophe. Something similar
happens on resuming from hibernation (or even suspend), with various
compromise scenarios there in mind.

There's a more general reason why userspace rolling its own RNG from a
getrandom() seed is fraught. There's a lot of attention paid to this
particular Linuxism we have of the RNG being initialized and thus
non-blocking or uninitialized and thus blocking until it is initialized.
These are our Two Big States that many hold to be the holy
differentiating factor between safe and not safe, between
cryptographically secure and garbage. The fact is, however, that the
distinction between these two states is a hand-wavy wishy-washy inexact
approximation. Outside of a few exceptional cases (e.g. a HW RNG is
available), we actually don't really ever know with any rigor at all
when the RNG is safe and ready (nor when it's compromised). We do the
best we can to "estimate" it, but entropy estimation is fundamentally
impossible in the general case. So really, we're just doing guess work,
and hoping it's good and conservative enough. Let's then assume that
there's always some potential error involved in this differentiator.

In fact, under the surface, the RNG is engineered around a different
principal, and that is trying to *use* new entropic inputs regularly and
at the right specific moments in time. For example, close to boot time,
the RNG reseeds itself more often than later. At certain events, like VM
fork, the RNG reseeds itself immediately. The various heuristics for
when the RNG will use new entropy and how often is really a core aspect
of what the RNG has some potential to do decently enough (and something
that will probably continue to improve in the future from random.c's
present set of algorithms). So in your mind, put away the metal
attachment to the Two Big States, which represent an approximation with
a potential margin of error. Instead keep in mind that the RNG's primary
operating heuristic is how often and exactly when it's going to reseed.

So, if userspace takes a seed from getrandom() at point T1, and uses it
for the next hour (or N megabytes or some other meaningless metric),
during that time, potential errors in the Two Big States approximation
are amplified. During that time potential reseeds are being lost,
forgotten, not reflected in the output stream. That's not good.

The simplest statement you could make is that userspace RNGs that expand
a getrandom() seed at some point T1 are nearly always *worse*, in some
way, than just calling getrandom() every time a random number is
desired.

For those reasons, after some discussion on libc-alpha, glibc's
arc4random() now just calls getrandom() on each invocation. That's
trivially safe, and gives us latitude to then make the safe thing faster
without becoming unsafe at our leasure. Card shuffling isn't
particularly fast, however.

How do we rectify this? By putting a safe implementation of getrandom()
in the vDSO, which has access to whatever information a
particular iteration of random.c is using to make its decisions. I use
that careful language of "particular iteration of random.c", because the
set of things that a vDSO getrandom() implementation might need for making
decisions as good as the kernel's will likely change over time. This
isn't just a matter of exporting certain *data* to userspace. We're not
going to commit to a "data API" where the various heuristics used are
exposed, locking in how the kernel works for decades to come, and then
leave it to various userspaces to roll something on top and shoot
themselves in the foot and have all sorts of complexity disasters.
Rather, vDSO getrandom() is supposed to be the *same exact algorithm*
that runs in the kernel, except it's been hoisted into userspace as
much as possible. And so vDSO getrandom() and kernel getrandom() will
always mirror each other hermetically.

API-wise, vDSO getrandom has a pair of functions:

  ssize_t getrandom(void *state, void *buffer, size_t len, unsigned long flags);
  void *getrandom_alloc([inout] size_t *num, [out] size_t *size_per_each);

In the first function, the return value and the latter 3 arguments are
the same as ordinary getrandom(), while the first argument is a pointer
to some state allocated with getrandom_alloc(). getrandom_alloc() takes
the desired number of states, and returns an array of states, the number
actually allocated, and the size in bytes of each one, enabling a libc
to use one per thread. We very intentionally do *not* leave state
allocation up to the caller. There are too many weird things that can go
wrong, and it's important that vDSO does not provide too generic of a
mechanism.  It's not going to store its state in just any old memory
address. It'll do it only in ones it allocates.

Right now this means it's a mlock'd page with WIPEONFORK set. In the
future maybe there will be other interesting page flags or
anti-heartbleed measures, or other platform-specific kernel-specific
things that can be set. Again, it's important that the vDSO has a say in
how this works rather than agreeing to operate on any old address;
memory isn't neutral.

The interesting meat of the implementation is in lib/vdso/getrandom.c,
as generic C code, and it aims to mainly follow random.c's buffered fast
key erasure logic. Before the RNG is initialized, it falls back to the
syscall. Right now it uses a simple generation counter to make its
decisions on reseeding; this covers many cases, but not all, so this RFC
still has a little bit of improvement work to do. But it should give you
the general idea.

The actual place that has the most work to do is in all of the other
files. Most of the vDSO shared page infrastructure is centered around
gettimeofday, and so the main structs are all in arrays for different
timestamp types, and attached to time namespaces, and so forth. I've
done the best I could to add onto this in an unintrusive way, but you'll
notice almost immediately from glancing at the code that it still needs
some untangling work. This also only works on x86 at the moment. I could
certainly use a hand with this part.

So far in my test results, performance is pretty stellar (around 15x for
uint32_t generation), and it seems to be working. But this is very, very
young, immature code, suitable for an RFC and no more, so expect
dragons.

Cc: linux-crypto@vger.kernel.org
Cc: x86@kernel.org
Cc: Nadia Heninger <nadiah@cs.ucsd.edu>
Cc: Thomas Ristenpart <ristenpart@cornell.edu>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Vincenzo Frascino <vincenzo.frascino@arm.com>
Cc: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
Cc: Florian Weimer <fweimer@redhat.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [Tastyfish/Skyrat-tg](https://github.com/Tastyfish/Skyrat-tg)@[b15331b4df...](https://github.com/Tastyfish/Skyrat-tg/commit/b15331b4df9bd525ba80b284beb3442f180c01be)
#### Sunday 2022-07-31 00:58:24 by OrionTheFox

[MANUAL MIRROR] The GAGening: Clothesmate edition [MDB IGNORE] (#15100)

* The GAGening: Clothesmate edition

* ThisShouldWork

* hgnbhg

* would probably help to have the right .dmi

* fixed?

* Fuck you

Co-authored-by: Twaticus <46540570+Twaticus@users.noreply.github.com>

---
## [zx2c4/linux-rng](https://github.com/zx2c4/linux-rng)@[b9a11d8d0e...](https://github.com/zx2c4/linux-rng/commit/b9a11d8d0e3c7ac911803f2fe72093468c66abf6)
#### Sunday 2022-07-31 01:31:59 by Jason A. Donenfeld

random: implement getrandom() in vDSO

Two statements:

  1) Userspace wants faster cryptographically secure random numbers of
     arbitrary size, big or small.

  2) Userspace is currently unable to safely roll its own RNG with the
     same security profile as getrandom().

Statement (1) has been debated for years, with arguments ranging from
"we need faster cryptographically secure card shuffling!" to "the only
things that actually need good randomness are keys, which are few and
far between" to "actually, TLS CBC nonces are frequent" and so on. I
don't intend to wade into that debate substantially, except to note that
recently glibc added arc4random(), whose goal is to return a
cryptographically secure uint32_t. So here we are.

Statement (2) is more interesting. The kernel is the nexus of all
entropic inputs that influence the RNG. It is in the best position, and
probably the only position, to decide anything at all about the current
state of the RNG and of its entropy. One of the things it uniquely knows
about is when reseeding is necessary.

For example, when a virtual machine is forked, restored, or duplicated,
it's imparative that the RNG doesn't generate the same outputs. For this
reason, there's a small protocol between hypervisors and the kernel that
indicates this has happened, alongside some ID, which the RNG uses to
immediately reseed, so as not to return the same numbers. Were userspace
to expand a getrandom() seed from time T1 for the next hour, and at some
point T2 < hour, the virtual machine forked, userspace would continue to
provide the same numbers to two (or more) different virtual machines,
resulting in potential cryptographic catastrophe. Something similar
happens on resuming from hibernation (or even suspend), with various
compromise scenarios there in mind.

There's a more general reason why userspace rolling its own RNG from a
getrandom() seed is fraught. There's a lot of attention paid to this
particular Linuxism we have of the RNG being initialized and thus
non-blocking or uninitialized and thus blocking until it is initialized.
These are our Two Big States that many hold to be the holy
differentiating factor between safe and not safe, between
cryptographically secure and garbage. The fact is, however, that the
distinction between these two states is a hand-wavy wishy-washy inexact
approximation. Outside of a few exceptional cases (e.g. a HW RNG is
available), we actually don't really ever know with any rigor at all
when the RNG is safe and ready (nor when it's compromised). We do the
best we can to "estimate" it, but entropy estimation is fundamentally
impossible in the general case. So really, we're just doing guess work,
and hoping it's good and conservative enough. Let's then assume that
there's always some potential error involved in this differentiator.

In fact, under the surface, the RNG is engineered around a different
principal, and that is trying to *use* new entropic inputs regularly and
at the right specific moments in time. For example, close to boot time,
the RNG reseeds itself more often than later. At certain events, like VM
fork, the RNG reseeds itself immediately. The various heuristics for
when the RNG will use new entropy and how often is really a core aspect
of what the RNG has some potential to do decently enough (and something
that will probably continue to improve in the future from random.c's
present set of algorithms). So in your mind, put away the metal
attachment to the Two Big States, which represent an approximation with
a potential margin of error. Instead keep in mind that the RNG's primary
operating heuristic is how often and exactly when it's going to reseed.

So, if userspace takes a seed from getrandom() at point T1, and uses it
for the next hour (or N megabytes or some other meaningless metric),
during that time, potential errors in the Two Big States approximation
are amplified. During that time potential reseeds are being lost,
forgotten, not reflected in the output stream. That's not good.

The simplest statement you could make is that userspace RNGs that expand
a getrandom() seed at some point T1 are nearly always *worse*, in some
way, than just calling getrandom() every time a random number is
desired.

For those reasons, after some discussion on libc-alpha, glibc's
arc4random() now just calls getrandom() on each invocation. That's
trivially safe, and gives us latitude to then make the safe thing faster
without becoming unsafe at our leasure. Card shuffling isn't
particularly fast, however.

How do we rectify this? By putting a safe implementation of getrandom()
in the vDSO, which has access to whatever information a
particular iteration of random.c is using to make its decisions. I use
that careful language of "particular iteration of random.c", because the
set of things that a vDSO getrandom() implementation might need for making
decisions as good as the kernel's will likely change over time. This
isn't just a matter of exporting certain *data* to userspace. We're not
going to commit to a "data API" where the various heuristics used are
exposed, locking in how the kernel works for decades to come, and then
leave it to various userspaces to roll something on top and shoot
themselves in the foot and have all sorts of complexity disasters.
Rather, vDSO getrandom() is supposed to be the *same exact algorithm*
that runs in the kernel, except it's been hoisted into userspace as
much as possible. And so vDSO getrandom() and kernel getrandom() will
always mirror each other hermetically.

API-wise, vDSO getrandom has a pair of functions:

  ssize_t getrandom(void *state, void *buffer, size_t len, unsigned int flags);
  void *getrandom_alloc([inout] size_t *num, [out] size_t *size_per_each);

In the first function, the return value and the latter 3 arguments are
the same as ordinary getrandom(), while the first argument is a pointer
to some state allocated with getrandom_alloc(). getrandom_alloc() takes
the desired number of states, and returns an array of states, the number
actually allocated, and the size in bytes of each one, enabling a libc
to use one per thread. We very intentionally do *not* leave state
allocation up to the caller. There are too many weird things that can go
wrong, and it's important that vDSO does not provide too generic of a
mechanism. It's not going to store its state in just any old memory
address. It'll do it only in ones it allocates.

Right now this means it's a mlock'd page with WIPEONFORK set. In the
future maybe there will be other interesting page flags or
anti-heartbleed measures, or other platform-specific kernel-specific
things that can be set. Again, it's important that the vDSO has a say in
how this works rather than agreeing to operate on any old address;
memory isn't neutral.

The interesting meat of the implementation is in lib/vdso/getrandom.c,
as generic C code, and it aims to mainly follow random.c's buffered fast
key erasure logic. Before the RNG is initialized, it falls back to the
syscall. Right now it uses a simple generation counter to make its
decisions on reseeding; this covers many cases, but not all, so this RFC
still has a little bit of improvement work to do. But it should give you
the general idea.

The actual place that has the most work to do is in all of the other
files. Most of the vDSO shared page infrastructure is centered around
gettimeofday, and so the main structs are all in arrays for different
timestamp types, and attached to time namespaces, and so forth. I've
done the best I could to add onto this in an unintrusive way, but you'll
notice almost immediately from glancing at the code that it still needs
some untangling work. This also only works on x86 at the moment. I could
certainly use a hand with this part.

So far in my test results, performance is pretty stellar (around 15x for
uint32_t generation), and it seems to be working. But this is very, very
young, immature code, suitable for an RFC and no more, so expect
dragons.

Cc: linux-crypto@vger.kernel.org
Cc: x86@kernel.org
Cc: Nadia Heninger <nadiah@cs.ucsd.edu>
Cc: Thomas Ristenpart <ristenpart@cornell.edu>
Cc: Theodore Ts'o <tytso@mit.edu>
Cc: Vincenzo Frascino <vincenzo.frascino@arm.com>
Cc: Adhemerval Zanella Netto <adhemerval.zanella@linaro.org>
Cc: Florian Weimer <fweimer@redhat.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>

---
## [el-ang/TurTor](https://github.com/el-ang/TurTor)@[4dcdc4d629...](https://github.com/el-ang/TurTor/commit/4dcdc4d629806757eceea9fd837ee48d6e8d716e)
#### Sunday 2022-07-31 04:59:54 by el-ang

Gw kok Goblog :facepalm:

Secret Token just got spoiled in the code by chaotic idiot me and Discord detect it then warn me thru' email.. :joy: :joy:

---
## [se7ensde/platform_vendor_spark](https://github.com/se7ensde/platform_vendor_spark)@[59fa231439...](https://github.com/se7ensde/platform_vendor_spark/commit/59fa23143952d237eb9bcc8386479ecf51d430da)
#### Sunday 2022-07-31 06:39:16 by se7ensde

Add my Vandalism font and fuck you if you dont like it bitch

---
## [HyunggyuJang/doom-emacs](https://github.com/HyunggyuJang/doom-emacs)@[b07614037f...](https://github.com/HyunggyuJang/doom-emacs/commit/b07614037f7670682d2c193d83abdb9eed9f218e)
#### Sunday 2022-07-31 07:11:23 by TEC

fix(mu4e): support mu 1.8

Thanks to some combination of ignorance and obstinance, mu4e has thrown
compatibility to the wind and completely ignored the exitance of
define-obsolete-function-alias. Coupled with the inconsistent/partial
function renaming, this has made the mu4e 1.6⟶1.8 change particularly
annoying to deal with.

By suffering the pain of doing the mu4e author's work for them, we can
use defalias to give backwards compatibility a good shot for about 60
functions. Some mu4e~x functions are now mu4e--x, others are unchanged,
and then you've got a few odd changes like mu4e~proc -> mu4e--server and
mu4e-search-rerun. The form of message :from entries has also changed,
and a new (mu4e) entrypoint added supplanting mu4e~start.

Fix: #6511
Close: #6549
Co-authored-by: Rahguzar <aikrahguzar@gmail.com>

---
## [raghavt20/kernel_sm6150](https://github.com/raghavt20/kernel_sm6150)@[882974d745...](https://github.com/raghavt20/kernel_sm6150/commit/882974d745c1897f546b6b3b2ed9b2c71f36f04e)
#### Sunday 2022-07-31 07:39:04 by Peter Zijlstra

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
Signed-off-by: Alexander Winkowski <dereference23@outlook.com>
Change-Id: Idd54334615da4c78698ca8b3b12b514ae9d8360f

---
## [ghostwriter/laminas-org-laminas-coding-standard](https://github.com/ghostwriter/laminas-org-laminas-coding-standard)@[e64c11b798...](https://github.com/ghostwriter/laminas-org-laminas-coding-standard/commit/e64c11b798f9b6e515194bf4de23346a2742b39b)
#### Sunday 2022-07-31 09:25:55 by Michał Bundyra

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
## [harryob/Foundation-19](https://github.com/harryob/Foundation-19)@[befabcec33...](https://github.com/harryob/Foundation-19/commit/befabcec333347ce6b918d67d4c884b9e0dcefea)
#### Sunday 2022-07-31 09:51:35 by TenameACAccount

more dcz changes yay (#548)

* Update site53-1.dmm

* fallout 5 on the byond engine

* fuck you box

Co-authored-by: UserU <37943518+User-U-U@users.noreply.github.com>

---
## [harryob/Foundation-19](https://github.com/harryob/Foundation-19)@[ea904cd81f...](https://github.com/harryob/Foundation-19/commit/ea904cd81f16d6feb161b0dbd24eca7524df15ab)
#### Sunday 2022-07-31 09:51:35 by Calyxman

Makes Crisis robot actually worth using. (#576)

* Adds adrenaline to paramedic borg hypospray

Kinda weird how the robot whos meant to be doing paramedic shit doesnt have shit to restart the heart or apply allergic reaction first aid???
Adds /datum/reagent/medicine/adrenaline to the crisis borghypo.

* Adds ATK, ABK to Crisis Cyborg

Adds the advanced trauma and burn kits to the Crisis cyborg. This makes it a direct tradeoff between Crisis and Emergency Response flying. ER has more mobility, but worse gear for medical treatment, while the Crisis cyborg has less mobility but better gear.

* Adds tylenol and dexalin to crisis borg

Why tf does the surgical borg, specializing in surgical procedures, have better equipment for the medical doctor job than the actual medical cyborg?
Tradeoff between Emergency Response and Crisis: Crisis has lower mobility, but better gear, and Emergency Response has higher mobility but worse gear.

---
## [harryob/Foundation-19](https://github.com/harryob/Foundation-19)@[96615f6506...](https://github.com/harryob/Foundation-19/commit/96615f650661292a92b79eb1983064556188cb37)
#### Sunday 2022-07-31 09:51:35 by harryob

LFification, again, maybe for real this time (#568)

* what is this cursed shit

* shut up PLEASE

* everything non-LF should be LFd

Co-authored-by: tichys <tichman27@gmail.com>

---
## [DarkPlayerr/darkicons](https://github.com/DarkPlayerr/darkicons)@[afe30404ff...](https://github.com/DarkPlayerr/darkicons/commit/afe30404ff9db9860dd2ed60fede6cc31905569c)
#### Sunday 2022-07-31 11:53:38 by DarkPlayer

rkicons: add burger king icon

Number 15: Burger king foot lettuce. The last thing you'd want in your Burger King burger is someone's foot fungus. But as it turns out, that might be what you get. A 4channer uploaded a photo anonymously to the site showcasing his feet in a plastic bin of lettuce. With the statement: "This is the lettuce you eat at Burger King." Admittedly, he had shoes on.

But that's even worse.

The post went live at 11:38 PM on July 16, and a mere 20 minutes later, the Burger King in question was alerted to the rogue employee. At least, I hope he's rogue. How did it happen? Well, the BK employee hadn't removed the Exif data from the uploaded photo, which suggested the culprit was somewhere in Mayfield Heights, Ohio. This was at 11:47. Three minutes later at 11:50, the Burger King branch address was posted with wishes of happy unemployment. 5 minutes later, the news station was contacted by another 4channer. And three minutes later, at 11:58, a link was posted: BK's "Tell us about us" online forum. The foot photo, otherwise known as exhibit A, was attached. Cleveland Scene Magazine contacted the BK in question the next day. When questioned, the breakfast shift manager said "Oh, I know who that is. He's getting fired." Mystery solved, by 4chan. Now we can all go back to eating our fast food in peace.

---
## [clamor-s/u-boot](https://github.com/clamor-s/u-boot)@[75dde9f020...](https://github.com/clamor-s/u-boot/commit/75dde9f020bec5c1175bb0ea38df21fb2f23c9e8)
#### Sunday 2022-07-31 11:58:57 by Marcel Ziswiler

tegra: lcd: video: integrate display driver for t30

On popular request make the display driver from T20 work on T30 as
well. Turned out to be quite straight forward. However a few notes
about some things encountered during porting: Of course the T30 device
tree was completely missing host1x as well as PWM support but it turns
out this can simply be copied from T20. The only trouble compiling the
Tegra video driver for T30 had to do with some hard-coded PWM pin
muxing for T20 which is quite ugly anyway. On T30 this gets handled by
a board specific complete pin muxing table. The older Chromium U-Boot
2011.06 which to my knowledge was the only prior attempt at enabling a
display driver for T30 for whatever reason got some clocking stuff
mixed up. Turns out at least for a single display controller T20 and
T30 can be clocked quite similar. Enjoy.

Signed-off-by: Marcel Ziswiler <marcel.ziswiler@toradex.com>
Signed-off-by: Svyatoslav Ryhel <clamor95@gmail.com>

---
## [bb-sycl/llvm](https://github.com/bb-sycl/llvm)@[7c51f02eff...](https://github.com/bb-sycl/llvm/commit/7c51f02effdbd0d5e12bfd26f9c3b2ab5687c93f)
#### Sunday 2022-07-31 12:14:21 by Matheus Izvekov

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

3) This patch could exposed a bug in how you get the source range of some
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
## [DamienBriffa/REDGUM-SURYPSAP](https://github.com/DamienBriffa/REDGUM-SURYPSAP)@[1d1f38ba9e...](https://github.com/DamienBriffa/REDGUM-SURYPSAP/commit/1d1f38ba9e1b8f8de9e429f458f09e6cca350832)
#### Sunday 2022-07-31 13:06:46 by DamienBriffa

Create README.md

Its the sap that fogms on the outside of a gum tree that the Barrie grub takes with it when the tree is at a marture age I think 35 years it at the second ringlett of the trunks growth at this line I think the Barrie grub makez its way up the centre part of the tree in under and between the roots with that it chews and nibbels its way through the hole vertical area of the trunk till it reachers the first branch that is full of leaves with that it has left a trail of this sap behind it and the sap soakes into the inner trunk and works its way out as the tree inlargens over its life span making it stronger then it possable could have been as a normal growth the bardy grub is a worm of some kind I think that transforms from within a caccoon or its a catterpillar that once its dug its hole or tunneld its tunnel to the root bed of the gum tree it waits and feeds there till the hot weather melt the sap and it incases the catterpillar with in its tunnel and it abbsorbs the sap and when it full it makes its way through the trunk spreading the sap as it goes and it treats the timber trunk inside to outside making it superstrong and giving it a longerlasting standing life span and I think she. You find a witcherty grub with in a stump or cut fire wood that tree was fallen way early of its expectant and special given extended life period I'm not exactly possitive about this its just a thort that crossed my mind last year when I was helping these men with the fire wood that had fallen in campbellfeild through the winds of a stormie night there were a few tree down and they needed to be cleaned up anyways but I think whdn you see termites I think that they mite be what the bardie turns into and bores from with in out of the trunk and this allows the whole tunnel leading in vertical axes to fill with sap and squrt through the smaller termited tunnel due to size differents and coats the inner trunk like that only because that termites are a intelligent species of construction and area systems there mounds are build in a tristegic way for wind flow heat climatcontroling and also protection I think they may be based by levels from lowest to highest for different temp, moisture, windflow for its Owen ways of life and I don't think they are the hollowers of the tunnels you find in wood thats all flaken and broken mite be that of a pine tree sap type termite that forms inside a pine tree and once there of age pine cones fall and they emergy from with in or they are spread in a egg in the wind fassion on the spiral effect of a jointed pine leaf  swirling tunneling effective of a premeditated image of polination, seadling exposion and spread

---
## [newstools/2022-express](https://github.com/newstools/2022-express)@[282f4e9a8d...](https://github.com/newstools/2022-express/commit/282f4e9a8d16fa2ae8586af5e20c192dcb4ae1d3)
#### Sunday 2022-07-31 14:06:29 by Billy Einkamerer

Created Text For URL [www.express.co.uk/life-style/health/1648370/bill-murray-health-depression-symptoms-suicidal-thoughts-ready-to-die]

---
## [KDE/kstars](https://github.com/KDE/kstars)@[6a60e821a8...](https://github.com/KDE/kstars/commit/6a60e821a833b60dc4a18a7a95a43b7bc727686e)
#### Sunday 2022-07-31 16:06:53 by Jasem Mutlaq

INDI Devices Handling Refactor

This is a major refactor for how KStars handles INDI devices. Traditionally, Ekos would create devices as soon as they are received. Each device is assigned a specific device type based on *signature* properties that belong to that device class. For example, EQUATORIAL_EOD_COORD would indicate that the device is a mount, and so forth. While this scheme worked well for most simple devices, it became complex to handle INDI devices with multiple interfaces (e.g. CCD with Filter wheel built in).

These kind of devices were supported by retaining them as GenericDevices and then sending general INDI commands to them when needed. Using this, we were able to support most multi-interface devices for many years in KStars. However, with even more complex devices that are not conventional (e.g. Dome with weather station interface), it became very complicated to handle such devices effectively without ugly hacks.

This MR introduces an update method for dealing with INDI devices:
1. All devices are created as _GenericDevices_
2. Based on device DriverInterface property, we create _ConcreteDevices_ accordingly. A concrete device is derived from each supported INDI device interface (i.e. Guider, Focuser, Correlator, ...etc)
3. ConcreteDevices are only announced when READY. This is in contrast to previous behavior when devices were announced as soon as a _signature_ property is detected. We determine if a device ready by monitoring the flow of defined properties using a timer. This results in highly simplified method for dealing with device properties.

Lots of testing is required now to ensure the new scheme works.

---
## [realredtext/OWOTJunk](https://github.com/realredtext/OWOTJunk)@[11b4226b25...](https://github.com/realredtext/OWOTJunk/commit/11b4226b255f4eef41eb208834a56bf188a35c6d)
#### Sunday 2022-07-31 17:58:29 by redtext

motherfucking piece of shit is go goddamn laggy like fucking work SHUT UP GITHUB PRO TIP GO SUCK THE SHIT OUT OF MY DIARRHEA SOAKED ASS HAIRS

---
## [RayDeeUx/RawInput-1.8.9](https://github.com/RayDeeUx/RawInput-1.8.9)@[2215c32847...](https://github.com/RayDeeUx/RawInput-1.8.9/commit/2215c3284732399e72fe162c9c2c3b428269ca81)
#### Sunday 2022-07-31 17:59:49 by RayDeeUx

this is a filler title so that the following sentence will overflow into wherever it will go as one unbroken chain of thought. no nacrt, i will not make the mod folder text clickable because i have a life to live and this fucking shit wont fucking work for some fucking reason and i am not willing to spend 348 fucking years finding out fucking why

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[01a7239770...](https://github.com/mrakgr/The-Spiral-Language/commit/01a7239770fc8698b5a24070338d26b0a2c471d7)
#### Sunday 2022-07-31 18:00:19 by Marko Grdinić

"5:25pm. I was away from the screen for quite a while. I did have an idea.

Freelancing.

Let me do the monthly PL review after all.

///

I did a C backend for [Spiral](https://github.com/mrakgr/The-Spiral-Language). I got tired of art, and wanted to do programming so I finally decided to close that regret from last year. It is going to serve as a prototype for possible AI chip backends. The cool thing about it is that its ref counting is tail call optimization compatible. Now I just have to wait until I can get my hands on the chips.

An interesting story from this month is that I decided to try lying on my resume - I made one up with just generic Microsoft, Google and Tesla experience and I tried applying to 9 startups at AngelList. My actual one has like a 10% hit rate when I passed it around last year to various remote positions. Using this, I got 5 accepts. Out of that 1 got rejected when the recruiter actually looked at it and wrote a thoughtful reply saying their product does not need ML, but would be interested a year down the road if I am still on the market, 1 was a weird reject where the recruiter's computer supposedly broke down and I haven't heard from her since for the sake of rescheduling, and in the end I went to 3 interviews. I never got past those to the actual tech interviews which is a pity, since I actually have high odds of beating those, but the actual intro calls with the recruiters that have zero programming are probably impossible for me right now. This is a heavy blow to me, and I've been sorting out my feelings.

The biggest problem for me is the mind games they play to gauge my enthusiasm for joining their dinky startup. "How do you feel about working at a startup compared to a big company like Google?" "I don't have any preference." Note that she asked that at two separate points. Saying I didn't care was a big mistake. At the last place I applied to the recruiter who was really good and towards the end, played a trick on me by playing a purposely, glitchy video to demonstrate the simulated environment the company made. As I am watching she comments: "The video is glitchy." "I don't mind." Like the other recruiter she repeated the comment two times, and my response was the same. I should have feigned disappointment, but even had I realized the trap I got up at 8am after a restless night and the interview was literally at 9:30pm. It was hell. Had I known the nature of these interviews, I never would have scheduled it so late. Another problem is the general impression I give off. I am constantly bottling down my nervousness, and to make matters worse, after operating solo for so long I've forgotten how to interact with actual people. A scam artist could clear this stage easily, but for me it is very hard.

The fact that I am nervous is embarrassing for me, and a part of the reason is that I am unsure of whether I can actually do these jobs. It is an irrational impulse, much like the impulse to check at night whether I've let the tap water on by accident. I can't really prove to myself that I could do the jobs despite my skill, and the thought starts spreading like cancer. I am just too green to take any of these jobs and the problem is not my programming skill. Even if I had 30 years of experience doing my own projects I'd still have this nagging doubt, that even if I can make anything for myself whether I could do the same for others.

At this point to get rid of my weaknesses, I am rolling the idea of freelancing in my mind. I just remembered that it is a thing today. I've looked at it in the past, but the transactions were so low that I immediately put it out of mind and forgot about it as an avenue for work, but if it is a matter of pride to prove to myself that I can do it, then I could justify attempting it. In the past I've always had my own projects so I couldn't bother to waste time with something like freelancing, but now it has some value to me. Similarly to picking up fat chicks before moving on to pretty ones, it will boost my confidence when dealing with recruiters in the future and give me some badly needed social skills. The projects I do on a freelance site will be experience I can bluff about as being a part of some company in the future, which will make my lies a lot more realistic that the generic popular product kind like 'I worked on vision data pipeline for the self driving car at Tesla' that I put in the resume. I actually can't remember half of what I put on the resume. It will get me familiar with real world uses of programming, most people don't do it for the same reasons as me so my values are out of sync with the market. Even a junior with 3 months of experience could pose better as a seasoned pro than me.

Freelancing is like the micro stakes in online poker. No good players play at those stakes so my actual resume which the recruiters would chuck into the wastebasket, might actually be good there and the general story as to why I am there might even make sense to those willing to take the risk of giving me an assignment, unlike the senior-Googler-applying-to-the-small-startup one.

Jobs - even highly paid ones, are quite unattractive to me because they are more than just work. They are life paths, and they involve doing work that I do not see as being meaningful.

10k dollars is not much, but if you think about it I could use that to upgrade my rig and buy the AI chips when they come out, so what more do I need? What would be meaningful work for me would be programming novel hardware. When I threw in the towel on poker botting last year, I blamed it on the hardware, so getting my hands on AI chips became an obsession for me. You could probably talk me into programming those things regardless of the salary. I want to ask those [machines a question](https://github.com/mrakgr/The-Spiral-Language/blob/fcca1f4cdac94ca6e472b34a560404e12079d08c/A%20Question%20for%20the%20Machine.pdf) of how to learn. When they become more widespread in a few years, programming them will be its own specialization, so I’ll be able to get a job without internal conflicts then.

Anyway, I do not feel like freelancing now, but doing some sci-fi writing instead. I've been learning art for the sake of illustrating that story, and I want to forget everything for a while and just write like I've been wanting to. Until the era when I can program my mind arrives, I'll have to maintain the skill with some cheap side projects. I am not really expecting to make anything from writing, though if that happened it would be very cool. I haven't written anything yet, I'll make an announcement on [my Twitter](https://twitter.com/Ghostlike) when I publish the initial chapters.

///

7:25pm. Doing these is a good way of putting the month to a close. Tomorrow I will move to the next thing. Let me forget about programming and freelancing at least for a week or so, until I finish the first few chapters.

Let me close here. Tomorrow I will try to get some writing momentum started, otherwise I will just spend most of the day in bed like today. I am going to leave my job hunting adventure (number two) behind me and try to internalize the goal of writing Heaven's Key. It can take a while for the units in the brain to fall inline. You can't just flip key motivations on a dime.

I should better just forget about programming for a whole month. It would be best. I should have wrote that instead.

7:55pm. Oh, yeah before I commit, let me make on remark. You know how Kim Jung Gi cannot stop doodling? Isn't there an analogy between that an me keeping this journal here. It might have been accidental, but this could have leveled my writing skill compared to 8 years ago. I guess I'll find out.

It has been 1.5 years since I opened the journal file and the line count is already at 24.3k. This kind of text production capability can't be normal. I really hope it leveled up simply from that, maybe in that case getting an audience might stand a chance."

---
## [DanielDialektico/Machine-Learning](https://github.com/DanielDialektico/Machine-Learning)@[9fab6be2d3...](https://github.com/DanielDialektico/Machine-Learning/commit/9fab6be2d32c727b8c14dd62abcc7194d6223075)
#### Sunday 2022-07-31 19:11:14 by Daniel Dialéktico

Add files via upload

Data Set Information:

This data approach student achievement in secondary education of two Portuguese schools. The data attributes include student grades, demographic, social and school related features) and it was collected by using school reports and questionnaires. Two datasets are provided regarding the performance in two distinct subjects: Mathematics (mat) and Portuguese language (por). In [Cortez and Silva, 2008], the two datasets were modeled under binary/five-level classification and regression tasks. Important note: the target attribute G3 has a strong correlation with attributes G2 and G1. This occurs because G3 is the final year grade (issued at the 3rd period), while G1 and G2 correspond to the 1st and 2nd period grades. It is more difficult to predict G3 without G2 and G1, but such prediction is much more useful (see paper source for more details).


Attribute Information:

# Attributes for both student-mat.csv (Math course) and student-por.csv (Portuguese language course) datasets:
1 school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)
2 sex - student's sex (binary: 'F' - female or 'M' - male)
3 age - student's age (numeric: from 15 to 22)
4 address - student's home address type (binary: 'U' - urban or 'R' - rural)
5 famsize - family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
6 Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
7 Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
8 Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
9 Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
10 Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
11 reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')
12 guardian - student's guardian (nominal: 'mother', 'father' or 'other')
13 traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
14 studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
15 failures - number of past class failures (numeric: n if 1<=n<3, else 4)
16 schoolsup - extra educational support (binary: yes or no)
17 famsup - family educational support (binary: yes or no)
18 paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
19 activities - extra-curricular activities (binary: yes or no)
20 nursery - attended nursery school (binary: yes or no)
21 higher - wants to take higher education (binary: yes or no)
22 internet - Internet access at home (binary: yes or no)
23 romantic - with a romantic relationship (binary: yes or no)
24 famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
25 freetime - free time after school (numeric: from 1 - very low to 5 - very high)
26 goout - going out with friends (numeric: from 1 - very low to 5 - very high)
27 Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
28 Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
29 health - current health status (numeric: from 1 - very bad to 5 - very good)
30 absences - number of school absences (numeric: from 0 to 93)

# these grades are related with the course subject, Math or Portuguese:
31 G1 - first period grade (numeric: from 0 to 20)
31 G2 - second period grade (numeric: from 0 to 20)
32 G3 - final grade (numeric: from 0 to 20, output target)

---
## [VoidUI/system_bpf](https://github.com/VoidUI/system_bpf)@[ff102e9ae3...](https://github.com/VoidUI/system_bpf/commit/ff102e9ae3abe4c3b292068c388b9f68b65279ee)
#### Sunday 2022-07-31 19:43:29 by Maciej Żenczykowski

grant bpfloader explicit membership in some groups

(this is instead of relying on the CAP_CHOWN capability it has)

The goal is to allow bpfloader to open maps/programs it creates,
so that it can reuse them.  By virtue of CAP_CHOWN it can create,
pin, then give away ownership, and no longer be able to bpf_obj_get()
the pinned map or program (to reuse it at a later time).

This could be considered a partial (more targetted) workaround
for the lack of bpfloader CAP_DAC_OVERRIDE (or CAP_DAC_READ_SEARCH).
But for obvious reasons jeffv@ doesn't really want to grant that.

In some sense this doesn't actually really grant any privs on a writeable
filesystem, as CHOWN already allows stealing ownership...

However explicit membership is much easier to reason about,
and does not require playing:
- stat (to get current uid/gid/mode)
- chown (set uid to root, ie. self -- works due to CAP_CHOWN)
- chmod (grant user read if missing)
- bpf_obj_get (this now succeeds -- does not require capabilities)
- chmod (restore mode)
- chown (restore uid -- works due to CAP_CHOWN)
games in order to open pinned bpf maps/programs we'd normally be unable
to open due to unix uid/gid/mode restrictions.

Yes, I've verified the above 'magic' actually works with current privs,
provided we grant the missing 'getattr' selinux priv to allow the stat() call.
(obviously without it we can still gain access, we just can't undo things)

Currently /sys/fs/bpf maps and program ownership on a tip-of-tree T device looks like:

$ adb shell getprop ro.build.fingerprint
google/oriole/oriole:13/TP1A.220624.007/8785063:userdebug/dev-keys

$ adb shell ls -l /sys/fs/bpf/* | egrep '^-' | cut -d' ' -f3-4 | sort | uniq -c

count uid  gid            examples
    5 root graphics       platform:          gpu_mem.o & gpu_work.o
    5 root net_admin      tethering apex T+: netd.o skfilter_..._xtbpf & schedact_ingress_account programs
   10 root net_bw_acct    tethering apex T+: netd.o maps
   24 root network_stack  tethering apex S+: offload.o & test.o
    1 root root           tethering apex T+: netd.o cgroupsock_inet_create program
   38 root system         platform & tethering apex T+: time_in_state.o, block.o, clatd.o, dscp_policy.o, netd.o cgroupskb_(e|in)gress_stats

And additionally due to the utter lack of a 'groups' line in bpfloader.rc,
the default bpfloader gid is of course 'root'.

This suggests we should use:
  groups root graphics network_stack net_admin net_bw_acct system

(but only really mainline updatable stuff matters, so we could limit
 this to just networking and strip out 'graphics'...)

A glance through:
  system/core/libcutils/include/private/android_filesystem_config.h

Finds the following groups which might be of interest to bpfloader & mainline networking:
* root
* system
* graphics

  dhcp
  vpn
  mdnsr
  clat
  dns
  dns_tether
* network_stack

  inet
  net_raw
* net_admin
  net_bw_stats
* net_bw_acct

[stars mark the one's we've already identified previously]

Networking mainline code runs in 3 processes: netd, system_server and network_stack.

Based on looking at a live oriole device, these processes have the following
uid/gid/groups/capabilities:

netd - uid:0[root] gid:0[root] + 3005[net_admin]
Cap: 00000000000074ef=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_kill,cap_setgid,cap_setuid,cap_net_bind_service,cap_net_admin,cap_net_raw,cap_ipc_lock

networkstack.process - uid:1073[network_stack] gid:1073[network_stack] + 1073[network_stack]
3002[net_bt] 3003[inet] 3004[net_raw] 3005[net_admin] 3006[net_bw_stats] 3007[net_bw_acct] 9997[everybody]
Cap: 0000000000003c00=cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw

system_server - uid:1000[system] gid:1000[system] + 1001[radio] 1002[bluetooth] 1003[graphics]
1004[input] 1005[audio] 1006[camera] 1007[log] 1008[compass] 1009[mount] 1010[wifi]
1018[usb] 1021[gps] 1023[media_rw] 1024[mtp] 1032[package_info] 1065[reserved_disk]
3001[net_bt_admin] 3002[net_bt] 3003[inet] 3005[net_admin] 3006[net_bt_stats] 3007[net_bw_acct]
3009[readproc] 3010[wakeloc] 3011[uhid] 3012[readtracefs]
Cap: 0000001806897c20=cap_kill,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_sys_module,cap_sys_ptrace,cap_sys_nice,cap_sys_time,cap_sys_tty_config,cap_wake_alarm,cap_block_suspend

Since netd has DAC_OVERRIDE, it really doesn't matter from a group analysis perspective
(side note: it probably should have a lot more groups than it actually does...)
Either way, both *root & *net_admin are already in the above list.

For the network stack process the obvious groups are:
  *network_stack, net_raw, *net_admin, net_bw_stats, *net_bw_acct
which means we should add:
  net_raw, net_bw_stats
to the above list.

(I'm assuming 'inet' & 'everybody' are too generic groups to be of use for bpf,
 and that we don't [yet] care about bluetooth (net_bt) being able to use bpf directly)

For the system server the choice is harder, but I'd tend to pick:
  *system, *graphics, *net_admin, *net_bw_acct

(Again ignoring non-networking stuff, and assuming radio/bluetooth/wifi bpf
  use will come at some later point in time.)

This gives us decent coverage of the 3 processes (and combinations there-of):
  netd process                         -> group root
  network stack process                -> group network_stack
  system server process                -> group system
  both network stack and system server -> group net_bw_acct
Note that due to DAC_OVERRIDE netd always has unix access no matter what,
and needs to be limited via selinux contexts instead.

Additionally 'net_admin' is used for xt_bpf iptables programs due to need
for netutils_wrappers support and it is also usable by all 3 processes.

This means we can fully explain all groups that currently show up as in use.
Adding net_raw & net_bw_stats is possibly not needed, but also won't hurt,
and might be useful in the future.

We could also argue that we should add:
  dhcp, vpn, mdnsr, clat, dns, dns_tether & inet

But since none of our mainline code running processes are currently
members of those groups (besides netd due to DAC_OVERRIDE), there doesn't
seem to be much benefit (this can't be changed with mainline pushes).

I assume new stuff which would need these groups will actually only be loaded
on U+ bpfloader, which will have a less hacky solution for this problem anyway.

Note: on U+ bpfloader we should probably fix this by simply caching
all bpf map/prog filedescriptors in a path->fd hashmap, and thus
avoid the need to ever reopen anything.  This is a far more invasive change,
but once done we should be able to revert this change.

For safety we'll also want to make sure we abort() if we detect cases
that cannot be safely handled by S bpfloader, an example would be
maps with uid != root in tethering location.

Bug: 218408035
Bug: 237716689
Test: TreeHugger, manual testing
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I742868b1a6819547fcd7a3573946a2fc479a21a5

---
## [NimBlemations/Vs-Mr-Thump](https://github.com/NimBlemations/Vs-Mr-Thump)@[3fdc286efd...](https://github.com/NimBlemations/Vs-Mr-Thump/commit/3fdc286efde0a0b396d3ff7e1cb4b76c28d5d213)
#### Sunday 2022-07-31 19:55:52 by NimBlemations

Shader stuff and other stuff idk

Fuck you Haxe, fuckin weird nae nae ass compiler.

---
## [941design/pned](https://github.com/941design/pned)@[8069d5b920...](https://github.com/941design/pned/commit/8069d5b920d1b97d6b533fdc4a03aaf081d4def0)
#### Sunday 2022-07-31 20:36:54 by Markus Rother

7 years later...

Updated dependencies, and managed to start the gui.
A shitty gui, btw. Not that I ever thought the UX
was nice, but I didn't remember it as that bad.

Also removed a bunch of pointless comments. Style
was a requirement by the course this project belonged to.

Some functionality probably broke, because I had to
get rid of proprietary libs.

Ok. See you in a few years...

---
## [Kappar-Crew/kappar-s3](https://github.com/Kappar-Crew/kappar-s3)@[b68b8332d9...](https://github.com/Kappar-Crew/kappar-s3/commit/b68b8332d9fc0f961aeafef9f0c4a21028bfb42c)
#### Sunday 2022-07-31 20:50:07 by DerCommander323

Ore Generation Fixes! (FINALLY OH MY GOD)

-made ores actually generate in the whole overworld, wooo
-also fixed some rates that were kinda insane

---
## [WammKD/activity_pub](https://github.com/WammKD/activity_pub)@[52e677e17f...](https://github.com/WammKD/activity_pub/commit/52e677e17fefd0ca941fdbd240d96837b96e7352)
#### Sunday 2022-07-31 20:54:51 by Wamm K. D

I'm, honestly, not sure what direction I want to go with this.

But I absolutely think we need to rename this; it's absolutely unclear
what the Hell this file is supposed to do until you do enough
searching to find all the places it's used (having two modules named
exactly the same thing (`Publisher`) is, in face, confusing).

I'm not exactly thrilled about their placement, either (I think, at
least; it may start to make more intuitive sense with this making it
more clear that `PublisherBehavior` is, in fact, just a behavior which
can be implemented), but the purpose of the files make sense: the
intention is for users to be able to overwrite the `Publisher` with
their own, should they want.

That's why `PublisherBehavior` implements so many functions and then
requires whatever adopts its behavior to also implement them:
the user can easily just reference the default function from the
behavior if ze doesn't want to implement zir own custom one.

I can get behind this; it's an elegant solve that really takes
advantage of the modular capabilities of some of these Elixir
features. But what it's trying to accomplish has no quick indicators
to clue in new developers or those revisiting the code; hopefully,
"behavior" in the name of the module gives an initializing kick to
people towards the right direction.

---
## [LumberKing/Tianxia](https://github.com/LumberKing/Tianxia)@[cdf32117a0...](https://github.com/LumberKing/Tianxia/commit/cdf32117a0f423996fce6bc136789fbb65122d55)
#### Sunday 2022-07-31 21:00:41 by Silversweeper

Balance/optimizatio/polishing (part 14 of ???) + Minamoto improvements (4 of 4) + Taira improvements

General:
- Fixed some issues caught by the Validator.

CBs:
- Shi Jingtang is now correctly viewed as a traitor if he loses or white peaces his starting war.
- Hopefully fixed some instances of peasant/etc. revolters becoming republics. Jumped-up peasant or not, you should prefer being some flavour of feudal!
- However much of a barbarian you might be due to your inferior government type, you may no longer use "But I'm tribal!" as an excuse to circumvent Chinese/Japanese religious CB rules.

Governments:
- Characters eligible for Chinese Imperial, Confucian Bureaucracy, Eastern Imperial, Japanese Imperial, Japanese Bureaucracy, and Divine Imperial should now be less likely to randomly become republics, MR or otherwise.
- Characters eligible for Monastic Feudal, Japanese Imperial, Japanese Monastic Feudal, and Divine Imperial shouldnow be less likely to randomly become theocracies.
- The Sapa Inca can now technically be tribal without HF.

Laws:
- The Grand Chancellor laws are no longer avalilabe for independent Confucian Bureaucracy realms unless they are kingdoms.
- Independent Confucian Bureaucracy, Japanese Bureaucracy, Japanese Feudal, and Japanese Monastic Feudal rulers now default to Late Feudal Administration (where not pre-scripted as using Imperial Administration).

Minor titles:
- The duke_yansheng minor title is now localized as "Honorable Overflowing with Wisdom".

Objectives:
- Characters with a bureaucratic government now only need to wait one year (as opposed to five) to take the "See the Realm Prosper" ambition if it is cancelled, and only five years (as opposed to 25) if it succeeds.
- Significantly increased the AI opinion thresholds for leaving various Japanese factions, and increased the severity of low opinion on the AI's willingness to start/join those factions.
- Significantly reduced the prestige requirement for starting the Permanent Regency factions.

Decisions:
- The Tenno no longer gets to employ goldsmiths, seeing as he already possesses all the signs of imperial power he should need (read: The Imperial Regalia). He can, however, use crown jewels that come into his possession in some other fashion.
- The Grand Chancellor bloodline decision's piety requirement now scales with the liege's vassal influence law, if relevant.
- AI Confucian and Japanese Bureaucracy rulers are now somewhat more likely to write books.
- Nomads settling should now be a bit less likely to create custom titles, seeing as those are no fun to deal with from a scripting perspective.
- Improved the decisions to get special JD characters, making the conditions a bit better and allowing them for feudal rulers with a Chinese character (any subset) bloodline even if they don't have a Chinese government.

Events:
- Made Yamato -> Japanese, Emishi -> Japanese, and Emishi -> Ainu culture conversion a bit faster, bringing them more in line with vanilla.
- Extended the same "Do not go on an adventure" restriction previously given to members of the Imperial Family to the Ryukyuan knockoff's dynasty.
- Characters that should care about the Tenno (or the Ryukyuan knockoff) should no longer target the Tenno (or the Ryukyuan knockoff) with an adventure.
- Tightened the conditions on Chinese character spawning somewhat.

Graphics:
- Removed some less good loading screens.

History:
- Further Imperial Family tweaks.
- Improved the Taira clan, minus future tweaks due to the Genpei War.
- Finished up the Minamoto clan, minus future tweaks due to the Genpei War.

Localization:
- Added some previously missing localization.

---
## [Blokyk/Parsex](https://github.com/Blokyk/Parsex)@[ee5f9c4acc...](https://github.com/Blokyk/Parsex/commit/ee5f9c4acc488ef853762d1f3604eec196825aa5)
#### Sunday 2022-07-31 21:25:10 by Blokyk

EROOR HANDLING ! REJOICE !

*error

Yes, my friends, the time has come for us to finally be able to get
multiple, actually good errors, with nice error messages and a source
preview (it's a work in progress tho !). This is all very basic,
and I'm sure there's still a lot of bugs everywhere (like infite
loops or cascading errors for example), but it was already quite a
lot of work getting this to work and writing every exception and
handling every case of every parselet and toklet. I'll polish all this
in another commit, probably. For example, the error messages are
really basic for now, and I'd like to rewrite them to be more helpful
in the future (see : Elm error messages).

An example of what the parser will output if the source code has
multiple errors :

An error happened at position test.txt(28, 37) and originated from FunctionDeclarationParselet.Parse : test.txt(28, 37) : Unexpected delim ()) at location test.txt(28, 37) after a comma in a function's parameter list. Expected a parameter name or type.

26 | }
27 |
28 | func someFunc2(int [seed, min, max],) {
                                         ^ error starts here
29 |     return new Random(seed).Next(min, max)
30 | }

An error happened at position test.txt(40, 20) and originated from ForeachParselet.Parse : test.txt(40, 20) : Unexpected ident (otherCollection) at location test.txt(40, 20) in a foreach header. Expected the 'in' keyword.

38 | foreach (item in collection) { }
39 |
40 | foreach (otherItem otherCollection) {
                        ^ error starts here
41 |     if (collection.contains(otherItem)) break;
42 |

You are the sole judge of my humble progress, but I'd say this is pretty
damn good work !

Yes, I know no one uses this project, but I prefer to do this now
because it would have been a nightmare later on with semantic
analysis and all that if we had to do throw each time something
was wrong. Also, this is all just a passion/learning project,
so I do things that make me learn stuff. While writing error messages
might not have been the most exciting stuff ever, I love the
professional look that this gives to the parser, and I'm quite happy
with my work so far. Oh and it's easier for me to debug when
something goes wrong parsing-wise.

I also think this is just a nice feature to have, and it has actually
made me (re)consider some things. I could have added them in this
commit, but I think it's already big enough, and it would have been
lost in the noise tbh. For example, I'd like to add "TextSpan"s,
basically two Locations indicating a range of text.

Error recovery here is quite difficult because there's no specific
way to delimit statements (other than ';', but those are optional
so we don't rely on those), so "panic mode"-style recovery is tricky
at best. So I don't know how the way I did it is called, but it kinda
works for now, and I hope to be able to rely and expand on it later.

I implemented this using a Logger that captures and registers errors
and then prints them when asked, nothing fancy. I reworked the
exceptions a bit, but nothing too fancy here either. No, the main
bulk was really just going throught every file and re-writing every
exception so that they are actually (at least a little bit) useful,
and would handle not having completely valid nodes and tokens. That
also meant I had to add an IsValid property to every token and node
so that invalid tokens and nodes would be marked. By default, it is
set to true (the object is valid), but you can set it to false (the
object isn't valid) in the constructor using the optional parameter
isValid or by setting the property after the node or token has been
created.

(Yes, it took me way too much effort to make all those lines exactly
the same size (it makes for some really awkward sentences) and no, I
am not doing that again.)

While there are still throwing exceptions in the code, those are
mainly for completely invalid states (i.e. InvalidCallException)
that just can't (and shouldn't) be recovered from, because they
are fatal internal errors. That's Logger.Fatal for you.

Anyway, here's the detailed changelog :

 Consumers :
  - Line and column numbers should now be more consistent
  - Added the constant StringConsumer.EOF, defined as U+0003

 Exceptions :
  - LotusException is now the base class for all cutsom exceptions.
    It contains basic informations such as the Location where the
    error occured, as well as informations about the caller/thrower
  - Most Exceptions now have clearer/betetr messages
  - UnexepectedEOF has been renamed to UnexpectedEOFException, and
    UnexpectedValueType to UnexpectedValueTypeException
  - InvalidCallExceptions now has an overloaded constructor with
    a message parameter

 Nodes :
  - All nodes now have a new property IsValid of type bool, set to
    true by default, that indicates whether or not the current node
    is valid or not. You can specify the value for this property
    by using the optional parameter `isValid` of the constructor,
    or by setting it after the node has been created.
  - Both StatementNode.NULL and ValueNode.NULL aren't valid
  - ValueNode.NULL's Location is now `Location(0, 0, "<std>")`

 Tokens :
  - All tokens now have a new property IsValid of type bool, set to
    true by default, that indicates whether or not the current token
    is valid or not. You can specify the value for this property
    by using the optional parameter `isValid` of the constructor,
    or by setting it after the token has been created.
  - Tokens representing literals will throw if the isValid parameter
    is set to true but they are not given a valid value.

 Parselets:
  - While most parselet still have a sort of "sanity check" at the
    beginning to check that they have been called on the right token,
    they don't throw anymore when they encounter a normal parse error
    (missing characters, unexpected token, invalid name, etc...);
    instead they register the error to the Logger class, set the node
    as invalid, and try to get back to a somewhat working state

 Toklets :
  - See the 'Parselets' section, same changes
  - Fixed some issues with number token parsing

 Location :
  - Removed the Location.With method

 Parser :
  - Fixed a bug with with semicolons, they would not work after some
    statements
  - Changed Parser.ConsumeCommaSeparatedList's signature
    from :
	public ValueNode[] ConsumeCommaSeparatedValueList(
		string start,
		string end,
		out bool isValid,
		int maxItemCount = -1
	)
    to :
	public ValueNode[] ConsumeCommaSeparatedValueList(
		string start,
		string end,
		ref bool isValid,
		int expectedItemCount = -1
	)

    Because `out bool isValid` would overwrite the variable even if
    it was alredy assigned to in the caller function.

Basically, better error handling.

---
## [Sinbest/mojave-sun-13](https://github.com/Sinbest/mojave-sun-13)@[a7a0e33192...](https://github.com/Sinbest/mojave-sun-13/commit/a7a0e33192ad3fcac5ad64d441f24af6ec852054)
#### Sunday 2022-07-31 22:08:47 by Hekzder

Mob overhaul for DT (#2117)

* Basic mobs

Title

* Start of simple robots

Title

* THE GREAT MOB SOUNDENING

TITLE

* Handies + ranged attack buffs

FASTER!!

* Protectrons, robobrains

* Death sounds and fixes some dumb shit

Title

* NEW ROACHES OMG!!!

WOW!

* Robo sounds

Title

* Mob projectile tweaks

I THINK WE'RE GOOD

* bitty

---

