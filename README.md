## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-08-15](docs/good-messages/2022/2022-08-15.md)


1,840,022 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,840,022 were push events containing 2,783,422 commit messages that amount to 225,039,368 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 27 messages:


## [lm40/VOREStation](https://github.com/lm40/VOREStation)@[e089978527...](https://github.com/lm40/VOREStation/commit/e08997852748d1155820139dfacf4745c9181ce3)
#### Monday 2022-08-15 00:01:30 by Rykka

Ports Taur Loafing from Cit-RP & Chompstation13

Ports https://github.com/Citadel-Station-13/Citadel-Station-13-RP/pull/2950

Doesn't work for sleeping *yet* due to some fuckiness with sprites updating that I'll probably actually work on properly later.
Does work for resting, and when you're stunned/knocked over/etc you will tip upwards like normal as a visual indicator that you're fucked (until we get fancy on-side sprites or smth).

At the very least, despite my frustrations, y'all can rest on your belly now as a taur and transform/size matrixes should work. LMK if there's any issues, my testing didn't find any.

Bear in mind that this presently only works for the drake-taur bc it's the only one that has sprites for it. The code is there, just enable can_loaf and set the offset accordingly to match if you want to sprite more taur loafs.

---
## [rjbs/Synergy](https://github.com/rjbs/Synergy)@[443d2f70a5...](https://github.com/rjbs/Synergy/commit/443d2f70a575b053437240f7fadd89528a23b0e0)
#### Monday 2022-08-15 00:03:04 by Michael McClimon

Rototron: attempt to fix a Monday time zone bug

Australians report that their morning reports do not contain duty
rotations; we're pretty sure this is because they're sent on Sunday UTC,
when there is no duty assigned. I think we can fix this by always
passing in a time zone to current_officers_for_duty, which will affect
the calendar search we're doing.

I'm not totally sure this will work, because time zones are weird and
the Rototron code is also kinda weird, but I don't think it's likely to
be _worse_.

---
## [matheustavares/git](https://github.com/matheustavares/git)@[5beca49a0b...](https://github.com/matheustavares/git/commit/5beca49a0b1f3c6d05a4437ca037ab2123a2de57)
#### Monday 2022-08-15 00:11:10 by Ævar Arnfjörð Bjarmason

test-lib: simplify by removing test_external

Remove the "test_external" function added in [1]. This arguably makes
the output of t9700-perl-git.sh and friends worse. But as we'll argue
below the trade-off is worth it, since "chaining" to another TAP
emitter in test-lib.sh is more trouble than it's worth.

The new output of t9700-perl-git.sh is now:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	ok 2 - use t9700/test.pl to test Git.pm
	# passed all 2 test(s)
	1..2

Whereas before this change it would be:

	$ ./t9700-perl-git.sh
	ok 1 - set up test repository
	# run 1: Perl API (perl /home/avar/g/git/t/t9700/test.pl)
	ok 2 - use Git;
	[... omitting tests 3..46 from t/t9700/test.pl ...]
	ok 47 - unquote escape sequences
	1..47
	# test_external test Perl API was ok
	# test_external_without_stderr test no stderr: Perl API was ok

At the time of its addition supporting "test_external" was easy, but
when test-lib.sh itself started to emit TAP in [2] we needed to make
everything surrounding the emission of the plan consider
"test_external". I added that support in [2] so that we could run:

	prove ./t9700-perl-git.sh :: -v

But since then in [3] the door has been closed on combining
$HARNESS_ACTIVE and -v, we'll now just die:

	$ prove ./t9700-perl-git.sh :: -v
	Bailout called.  Further testing stopped:  verbose mode forbidden under TAP harness; try --verbose-log
	FAILED--Further testing stopped: verbose mode forbidden under TAP harness; try --verbose-log

So the only use of this has been that *if* we had failure in one of
these tests we could e.g. in CI see which test failed based on the
test number. Now we'll need to look at the full verbose logs to get
that same information.

I think this trade-off is acceptable given the reduction in
complexity, and it brings these tests in line with other similar
tests, e.g. the reftable tests added in [4] will be condensed down to
just one test, which invokes the C helper:

	$ ./t0032-reftable-unittest.sh
	ok 1 - unittests
	# passed all 1 test(s)
	1..1

It would still be nice to have that ":: -v" form work again, it
never *really* worked, but even though we've had edge cases test
output screwing up the TAP it mostly worked between d998bd4ab67 and
[3], so we may have been overzealous in forbidding it outright.

I have local patches which I'm planning to submit sooner than later
that get us to that goal, and in a way that isn't buggy. In the
meantime getting rid of this special case makes hacking on this area
of test-lib.sh easier, as we'll do in subsequent commits.

The switch from "perl" to "$PERL_PATH" here is because "perl" is
defined as a shell function in the test suite, see a5bf824f3b4 (t:
prevent '-x' tracing from interfering with test helpers' stderr,
2018-02-25). On e.g. the OSX CI the "command perl"... will be part of
the emitted stderr.

1. fb32c410087 (t/test-lib.sh: add test_external and
   test_external_without_stderr, 2008-06-19)
2. d998bd4ab67 (test-lib: Make the test_external_* functions
   TAP-aware, 2010-06-24)
3. 614fe015212 (test-lib: bail out when "-v" used under
   "prove", 2016-10-22)
4. ef8a6c62687 (reftable: utility functions, 2021-10-07)

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [CHOMPStation2/CHOMPStation2](https://github.com/CHOMPStation2/CHOMPStation2)@[8e8232c0d8...](https://github.com/CHOMPStation2/CHOMPStation2/commit/8e8232c0d826dc3341d20a7861c1d86859e06ef7)
#### Monday 2022-08-15 01:01:23 by Rykka

Ports Taur Loafing from Cit-RP

Ports https://github.com/Citadel-Station-13/Citadel-Station-13-RP/pull/2950

Doesn't work for sleeping *yet* due to some fuckiness with sprites updating that I'll probably actually work on properly later.
Does work for resting, and when you're stunned/knocked over/etc you will tip upwards like normal as a visual indicator that you're fucked (until we get fancy on-side sprites or smth).

For real tho laying-on-side sprites would be nice to visually represent a taur collapsed on their side, rather than faceplanting bc humancode.

At the very least, despite my frustrations, y'all can rest on your belly now as a taur and transform/size matrixes should work. LMK if there's any issues, my testing didn't find any.

---
## [GTwhy/linux](https://github.com/GTwhy/linux)@[4a557a5d1a...](https://github.com/GTwhy/linux/commit/4a557a5d1a6145ea586dc9b17a9b4e5190c9c017)
#### Monday 2022-08-15 02:48:24 by Linus Torvalds

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
## [MatthewCroughan/TediCross](https://github.com/MatthewCroughan/TediCross)@[6e12a704f4...](https://github.com/MatthewCroughan/TediCross/commit/6e12a704f4d2675cd173730f94da7acd9f118841)
#### Monday 2022-08-15 03:18:09 by matthewcroughan

Remove shitty warning messages that crash the bot

This is fucking stupid.

---
## [GraveHat/VegetableFork](https://github.com/GraveHat/VegetableFork)@[f4c7571fc3...](https://github.com/GraveHat/VegetableFork/commit/f4c7571fc333779cbf761e637f2774a62b6b4d78)
#### Monday 2022-08-15 03:44:30 by Vaelophis Nyx

[MDB IGNORE][Gax] Adds new area for AI Ship Access & Adds APC & Fixes Cameras (#15291)

* argh

* fuck you MDB2

* I hate areas, I hate areas

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

* Update GaxStation.dmm

---
## [QWERTYghri/ARPv3-C](https://github.com/QWERTYghri/ARPv3-C)@[7a4badcc4c...](https://github.com/QWERTYghri/ARPv3-C/commit/7a4badcc4cfdb17886c66916f2e0e27828234db4)
#### Monday 2022-08-15 04:51:55 by QWERTYbae

resolved circular includes

I fucking hate my life

---
## [influxdata/influxdb_iox](https://github.com/influxdata/influxdb_iox)@[8a5cd1cddd...](https://github.com/influxdata/influxdb_iox/commit/8a5cd1cdddcbe8ed932ddd08e953cd40c8e8d784)
#### Monday 2022-08-15 08:24:27 by Marco Neumann

refactor: abstract change requests for cache policies (#5382)

* refactor: abstract change requests for cache policies

Tl;Dr; Lets replace the hard-coded enum of change requests with a more
flexible and easier-to-understand function-based approach. It also
unifies the interface for "initial requests" and "reactions".

Story time:

I just wanted to port over the "shared" backend with its "remove if"
functionality to the policy framework. Turns out that this backend does
not just use simple atomic operations but is basically a
"compare&exchange"-like operation (technically: GET+REMOVE) that relies
on a single mutable access lifetime to make sure that this behavior is
sane and nobody messes with the value between the GET and REMOVE. I call
this a "compound request".

The new policy framework did not support this kind of requests so I
thought how I could shoehorn it in. Basically I wanted to extend
`ChangeRequest` to support these kind of operations. But listing
combinations explicitly kinda seemed like some hack. So my brain slowly
came up with an abstract approach how to encode these operations and
after a while I was close to design some kind of mini-VM. I also
considered some ugly workarounds or to not express the "remove if"
functionality" as a policy. My nice vision of a policy framework started
to crack...

This is when sanity kicked in and I realized: every change request is
technically just a function on a (virtual) cache backend. Sure,
all-powerful Rust functions allow you to do ugly stuff that will result
in deadlocks, but with good docs and helpers for the common operations
the risk is very low. Furthermore this is already close to the system I
had for the "initial requests" and which I called a "callback backend".
So I unified both systems and made the change request abstract and all
tests pass and I think it is the better design.

Helps with #5320.

* docs: typos

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>

Co-authored-by: Andrew Lamb <andrew@nerdnetworks.org>
Co-authored-by: kodiakhq[bot] <49736102+kodiakhq[bot]@users.noreply.github.com>

---
## [Sheits/tgstation](https://github.com/Sheits/tgstation)@[e37591540b...](https://github.com/Sheits/tgstation/commit/e37591540b2620b7ad2a2b61734634d848e8eba2)
#### Monday 2022-08-15 08:43:54 by san7890

[MDB Ignore] OH GOD OH FUCK OH SHIT OH LORD - SPACE AND RUINS IS BROKEN (#67324)

So, for the last few days on production, Space Ruin generation has refused to work. Why is this? It's because in #67107 (cfc233052885dd294b2e7e676caaf84a2a37592b), we repathed `/area/space`  to `/area/misc/space` (lol i should have paid attention to that) without updating everything in code to match. I couldn't seem to get `/area/misc/space` to properly work somehow (this could have also been something I was doing wrong), but I worked it back to just making everything vanilla `/area/space` and all of those unwanted behaviors should be squashed out. Let's get the game working again.

---
## [Prajjwal-08/Prajjwal-08](https://github.com/Prajjwal-08/Prajjwal-08)@[e45b7fca46...](https://github.com/Prajjwal-08/Prajjwal-08/commit/e45b7fca460a39ea1f6423465feada7a2b2ba41c)
#### Monday 2022-08-15 08:50:45 by Prajjwal-08

Tips Collected at a restaurant 

The data set is from a restaurant from a city that operates only on 4 days of the week. Thursday, Friday, Saturday, Sunday. It records each transaction that was done when the restaurant was open.

The key parameters are

Total Bill - Amount of total bill in USD
Tip - Amount of tip given by the customer in USD
Sex - Sax of the guest who pays for the bill (Male or Female)
Smoker - Smoker in the party (Yes or No)
Day - Day of the week (Thu, Fri, Sat, Sun)
Time - Dinner or Lunch
Size - Number of the guests in the party
As a data scientist, you have been assigned the task to investigate the pattern of the tip received by the restaurant staff because the tip is an important parameter of their salary

Find out Five-Number summary for "Total Bill" and "Tip"
Plot the Box plot diagram for "Total Bill" and "Tip"
Analyze the diagram to mark the skewness in the data
Find out the outliers for "Total Bill" and "Tip"
Find out the IQR
Plot the histogram for "Total Bill" and "Tip"
Identify skewness in each. Type of skewness and the possible reason for the skewness
Plot the cumulative Frequency Polygon for "Total Bill" and "Tip"
Prepare the Frequency Table and Bar Chart for "Size". Summarize and explain your findings
Prepare two variable frequency tables for "Size" vs "Tip" and "Size" vs "Total Bill". Summarize and explain your findings.
Explore if there is any dependency between the variable "Tip" and rest of the variables

---
## [ivoson/spark](https://github.com/ivoson/spark)@[c4c623a3a8...](https://github.com/ivoson/spark/commit/c4c623a3a890267b2f9f8d472c8be30fc5db53e1)
#### Monday 2022-08-15 10:13:42 by Hyukjin Kwon

[SPARK-39869][SQL][TESTS] Fix flaky hive - slow tests because of out-of-memory

### What changes were proposed in this pull request?

This PR adds some manual `System.gc`. I know enough that this doesn't guarantee the garbage collection and sounds somewhat funny but it works in my experience so far, and I did such hack in some places before.

### Why are the changes needed?

To deflake the tests.

### Does this PR introduce _any_ user-facing change?

No, dev and test-only.

### How was this patch tested?

CI in this PR should test it out.

Closes #37291 from HyukjinKwon/SPARK-39869.

Authored-by: Hyukjin Kwon <gurwls223@apache.org>
Signed-off-by: Hyukjin Kwon <gurwls223@apache.org>

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[9e1f797d06...](https://github.com/pytorch/pytorch/commit/9e1f797d061f2d952aaafdc703f2196619049d95)
#### Monday 2022-08-15 13:56:43 by Edward Z. Yang

Update base for Update on "Convert SymInt tracing to mode based tracing"


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

Signed-off-by: Edward Z. Yang <ezyangfb.com>

[ghstack-poisoned]

---
## [ivanmixo/Foundation-19](https://github.com/ivanmixo/Foundation-19)@[ea904cd81f...](https://github.com/ivanmixo/Foundation-19/commit/ea904cd81f16d6feb161b0dbd24eca7524df15ab)
#### Monday 2022-08-15 14:05:12 by Calyxman

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
## [ivanmixo/Foundation-19](https://github.com/ivanmixo/Foundation-19)@[96615f6506...](https://github.com/ivanmixo/Foundation-19/commit/96615f650661292a92b79eb1983064556188cb37)
#### Monday 2022-08-15 14:05:12 by harryob

LFification, again, maybe for real this time (#568)

* what is this cursed shit

* shut up PLEASE

* everything non-LF should be LFd

Co-authored-by: tichys <tichman27@gmail.com>

---
## [afterallafk/kernel_xiaomi_onclite](https://github.com/afterallafk/kernel_xiaomi_onclite)@[82503c4d04...](https://github.com/afterallafk/kernel_xiaomi_onclite/commit/82503c4d04f381363c79e1d5f468a4d2e66aeb0b)
#### Monday 2022-08-15 15:16:14 by Peter Zijlstra

sched/core: Implement new approach to scale select_idle_cpu()

Hackbench recently suffered a bunch of pain, first by commit:

  4c77b18cf8b7 ("sched/fair: Make select_idle_cpu() more aggressive")

and then by commit:

  c743f0a5c50f ("sched/fair, cpumask: Export for_each_cpu_wrap()")

which fixed a bug in the initial for_each_cpu_wrap() implementation
that made select_idle_cpu() even more expensive. The bug was that it
would skip over CPUs when bits were consequtive in the bitmask.

This however gave me an idea to fix select_idle_cpu(); where the old
scheme was a cliff-edge throttle on idle scanning, this introduces a
more gradual approach. Instead of stopping to scan entirely, we limit
how many CPUs we scan.

Initial benchmarks show that it mostly recovers hackbench while not
hurting anything else, except Mason's schbench, but not as bad as the
old thing.

It also appears to recover the tbench high-end, which also suffered like
hackbench.

Tested-by: Matt Fleming <matt@codeblueprint.co.uk>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Cc: Chris Mason <clm@fb.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: Mike Galbraith <efault@gmx.de>
Cc: Peter Zijlstra <peterz@infradead.org>
Cc: Thomas Gleixner <tglx@linutronix.de>
Cc: hpa@zytor.com
Cc: kitsunyan <kitsunyan@inbox.ru>
Cc: linux-kernel@vger.kernel.org
Cc: lvenanci@redhat.com
Cc: riel@redhat.com
Cc: xiaolong.ye@intel.com
Link: http://lkml.kernel.org/r/20170517105350.hk5m4h4jb6dfr65a@hirez.programming.kicks-ass.net
Signed-off-by: Ingo Molnar <mingo@kernel.org>
Signed-off-by: Raphiel Rollerscaperers <rapherion@raphielgang.org>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[e4b7b250d8...](https://github.com/mrakgr/The-Spiral-Language/commit/e4b7b250d88d06212331a1371bea344c82d97789)
#### Monday 2022-08-15 16:05:07 by Marko Grdinić

"1:20pm. Done with breakfast. Let me chill a bit and then I will start.

1:45pm. How tedious. I'd rather take a nap, but I need to keep going forward.

Let me see if I can do a bit more for the day.

$$$

(Simulacrum intro)

    In the endless darkness
    Roam endless monsters
    Pain, cold, flame
    Age, time, death
    Torment

    Light and shadow
    Holy and hell

    The inevitable fate of the Universe
    Will never touch
    The courage of the Inspired
    And the power of the Transcendi

I start Simulacrum for the first time and sink into the virtual, feeling the outside reality being pushed out from my being. The sensation is quite relaxing, like falling into slumber.

As I wait for the program to load the poem appears in my sense, sentence by sentence. At first I am struck by a vision of the primordial universe. I feel a sense of danger of living in it, and a sense of hopelessness. I then feel its grandeur, and am filled with admiration. And then I feel the determination of challenging the inevitable as I read the proclamation.

The introduction fades and the scene slowly manifests before me. Panning to the sky, highlighted in brilliant hues of light like a veil of gold covering it is a floating city. Against a backdrop of blue, it seemed like a distant object made of gold. I felt the sense of depth in my vision, so I could sense that the floating city was massive. Then I felt the warmth of the sun and the rustle of wind. I get the sense that I am high up and realize that I am literally floating in the air like a spirit. Though it is my first time experiencing this, I try moving my gravity defying body and have no trouble doing so. Observing the vast skies surrounding me, I look down. I notice the bustle and the humdrum of a modern metropolitan city. Skyscrapers dot the landscape and deep down below I can see cars and pedestrians walking the streets.

The vision seems very crisp and vivid. After a few moments of pondering, I realize why that is the case. In the real world I have to wear glasses so everything is blurry past a certain distance, but here I am unrestricted in my resolution. Just by focusing I can see for thousands of meters as if I was standing a foot away. Picking a random spot on the street, I can make out the minor cracks on the pavement, and the grime and the wear from people walking over it for many years. Dressed in autumn clothing, the people as they go along their life feel lifelike and real. I see them talking, exclaiming, laughing, being tired, downcast and otherwise broadcasting their emotions.

"..."

I found the whole scene very impressive. It did not seem like something that humans could create.

As soon as I start wondering how to start the game, a menu comes up in a separate sense. The Load Game option is grayed out, but Start Game and Quit are there, so I select the former and enter the Scenario Selector. Simulacrum itself rather than being a single game is an intelligent program capable of simulating a large range of scenarios. Browsing over the available scenarios, all of them seem interesting and I am having trouble deciding so I go back to the top and look at the recommended one.

Heaven's Key.

'The souls of those passed on enter the afterlife to play the grand game of cards that God has prepared for them. The second chance is given, and can be lost. Can you survive the challenges of your second life and go on to challenge the highest power there is?'

Along with that brief description, there is some setting information. When I focused on the 2d map of the world, to my surprise it unfolded to a 3d model that I could mentally rotate and zoom. I realized that the world of Heaven's Key was covered with orbital islands, much like the floating one in the intro. The tech level is similar to the current time in 2025, which is good since it probably means I won't have to play against non-humans. It is like the game anticipated what I would choose. The game seems to be responding to my desire, and it took into consideration my personal goals when doing scenario suggestions as well as the background which obviously has the Heaven's Key theme.

I think about it for a bit, and decide to go with the scenario being presented to me. The core hasn't steered me wrong yet, so I want to trust it. Having made my decision, I start the game and feel drawn into it.

(Heaven's Key intro)

    The method of recursive self improvement via iterated suicide can be used in reality. In fact, the technique represents the most viable path to getting superpowers in any kind of reality.
    - Loading Blurb

Whereas during the menu segment I had been a disembodied presence hovering thousands of feet above the cityscape, once the game started I found myself standing upright in an actual body. I gawked like a tourist, taking in the sights. I was in a golden city. The buildings and the streets were all painted in various hues of yellow, mostly on the lighter side, and there was slight gloss on the material giving it a sense of agelessness. Usually, as time wore down the material, it would begin to lose its luster, but everything around me seemed to be brand new and sparkling. Right now I was located near the edge of one of the floating cities, and as my gaze traveled towards its center, the buildings became taller and larger, from regular suburban houses close to where I was to large apartment blocks in the distance. The very middle of the island had a grand square building on an elevated platform. It had a spherical dome that took up a lot of its volume, and as I peered at it, I noticed it seemed to be radiating golden light. Though since it was midday the effect was drowned out by the light of the sun.

In the skies I noticed there were floating golden blocks in the shape of tiles, that also seemed to be showering the city in light.

I was near the edge of the city, and it seemed to be some kind of amusement park. I could see circus tents pitched up, stands of various kinds and even a rollercoaster and various other kinds of thrill rides I did not recognize.

Taking in the sights, I breathe in the air and find it to be cool and refreshing. I checked myself over. Though I could not see my face, but based on the touch as well as the composition of the rest, it seems that my real world body has been replicated in this virtual one. Which suited me fine, but it is surprising that I haven't been offered a chance to make my avatar.

Behind me, was the railing, also made of gold. Like the blocks and the grand building, it actually had some luminance to it. Drawn to that, I try touching it and find it to be smooth and lukewarm. It is not very tall, only up to my abdomen. It is only there to prevent somebody from sliding off the edge by accident rather than stop somebody who intentionally wanted to jump off.

Looking over the railing, I can see mountains and forests as well as the sea, and as I look below, I get a spell of dizziness that I quickly fight off. I am currently very high up, enough that I can see clouds below me. Directly below there is what appears to be a major metropolis. The high rise buildings and skyscrapers are like tiny, gray splotches at this distance.

An idea to try it ceases me, and I wonder whether I should take a dive over the railing?

[Gnosis check DC 1.9 Succeeded - Sample 2.03]

I grin mischievously. Yeah, let me try it. It is not like I can experience this in real life. As soon as I think that, nervousness and excitement flood my body, and I want to keep going. I grip the railing, and place one leg and then the other over it. Hands still clutching the rail behind me, I lean forward and take a good look down. A huge drop past the clouds welcomes me, into the metropolis below. I am putting a lot of strength into my arms to keep the certain doom at bay. I can feel my heart beating against my chest.

I wonder if I will hit the streets or the roof of one of the high rises?

A thought like that intensifies both my fear and excitement. Slowly I loosen my grip on the railing and start lifting my fingers, one by one. First I move the thumbs out of the way, then I let the pinky slide. Then the ring finger. I feel like a feather, perched in such a precarious position. The railing is so close to the edge that my feet are partly over it.

Time feels like it is slowing down for me. Very slowly, as if to prolong the moment, I release the index and middle.

"No, don't do it!" I hear a woman's voice yell out, but I couldn't care less.

I feel my body leaning forward and the gravity taking hold. I drop over the railing into the vastness below.

"AAAAAAAAHHHHH!!!" As I plunge, the fear overwhelms me and a scream rips itself from my throat. Strong winds buffet me from below in my fall.

After a minute or so, I manage to get a grip on myself so I can at least enjoy the scenery instead of falling around in panic. I keep reminding myself that this is not real despite what my senses are telling me. With the sun shining all around, it is quite beautiful. I take some time to appreciate the majesty of nature. I plunge through the clouds, feeling wetness on my face and hands. Soon, what used to be tiny splotches in the distance became larger and larger. The buildings below gain definition, and involuntarily, I imagine myself splattering on the street below. The fear that I had put a lid on, bursts out, more maddened and bloodcurdling than before.

"AAAAAAAAAAAHHHHHH!!!" I scream again, even though it is fake. Even though the world is fake, my brain cares little about those facts. It is so stupid and primitive, so all it can do is beg for dear life even if there is no need to.

Ahahahaha, it is so stupid, my brain is so stupid!

As I scream and piss myself in panic, at the back of my head, I can almost feel a voice mocking me for my stupidity.

I miss the height of one of the high rises, and reflected in the glass of the window nearby, I see my reflection for the first time. Exactly as in real life, but I see traces of tears around my eyes. I hadn't realized that I had started crying at some point.

"NOOOOO!!! LOG OUT!!! LOG OUT!!! LOG OUT!!!" Completely detached from rationality, the idea to exit the game before I smash the concrete takes hold. I grip it like a liferaft in the turbulent seas.

Ahahahaha! Seen from a different perspective, it is almost like a person scrambling for his life is an entirely different person from myself.

I am going to smash face first in the middle of a busy street. As soon as the ground floor is only a couple of feet away, I muster all my reserves of will and try to stop time. This has no effect and I hit the ground, feeling the darkness overtake me.

(Euclid's Room)

"Ah!" I jolted awake into reality and involuntarily, flop like fish on dry land once. Wiping my face, I feel myself drenched in sweat. I breathe heavily and feel that in my chest, my heart is overworking itself. As soon as I realize that I am in a safe place, I begin to calm down.

I lie back on the bed for 5 minutes, until my tremors have passed.

"Hah..." I exhale, savoring the experience.

That was...

[Gnosis gain: 0.3]

...Amazing! Since I died so quickly, I didn't experience any pain, leaving only the excitement. This will definitely be a memorable experience for me. Has a regular computer game ever let me feel something like this? I do not think so. The conflict between my rational part that understood the senses are not to be trusted, and my lizard brain which went into a blind panic is what really made this what it was. If I was purely cool or purely in a panic, it would not have been that interesting.

My brain is pretty stupid right now, but at least I can have some fun with that. I'll take it a bit easier next time and just explore the town. That seems like a good plan.

I want to see what the game is about.

(Heaven's Key, Perimeter of a floating city)

I dive into the game again, and take in the sights of the city of gold. Taking only a passing glance at the railing, I turn around and go into the city proper. As fun as that experience was, I do not want to spend my entire day diving off the edge. Gawking like a tourist as I stroll around, I get a stock of the place. Near the frontier where I was, the density of buildings was low, so amongst the houses as if to spur business a lively entertainment sector was built. I could see circus tents, restaurants, stages as well as casinos. There seemed to be a lot of people enjoying themselves, though I wouldn't say it was packed. I found the city plan somewhat peculiar. There were roads for example, but no cars, and I could only see people using their own legs as far as I looked. The regular houses made sense, but other entertainment related facilities seemed to be built in the middle of roads and at intersections. Overall, it felt like the city itself was molded based on some template, and then patched up to fit a need by the people actually living here without modifying the underlying template itself.

It is a lively and cheerful place. It wasn't jam packed with people, but I could see a decent amount of them going about their business and chattering. The way they were dressed did not seem to be that much different than in the real world. Looking around, I could see old and young people, both male and female, but no kids which I'd expect would be unusual for an amusement park such as this. I think that I'd be in the youngest age cohort relative to the population here.

"Waiters wanted - 3,450/month"
"Can you make great pizza? Apply here. 3,600/month"
"Have a flair for entertainment? Comedy, magic, singing, musical instruments. 3,800/month"

While walking around I saw a bunch of job ads posted outside the relevant venues for waiters, cooks and attendants. The typical salary for these kinds of service jobs seems to be around 3,500 chips, whatever those are.

Getting bored of walking around, I pick a restaurant at random and take one of the outside seats. With the sun shining down on me, the weather is warm and pleasant, simply ideal. Given how up we are you'd expect it would be freezing, but normal rules do not seem to apply here. I pick up the menu, and take a look.

"Beer - 20"
"Iced Tea - 20"
"Pizza Margherita - 40"
"Cheese Burger - 30"
...

I want to order some of these. I've never tried eating in VR yet, so I am curious about what it tastes like.

"Hello sir, what would you like?" A waiter came around to take my order. I cringe inwardly.

"Just water." I have no choice, I do not have any money to pay for anything here.

"Got it."

While I was waiting, a person came up to my table and initiated conversation.

"Hello, do you mind if I take seat here?" She asked, smiling at me. I took a good look at the young woman in front of me. Wearing a headband with what looked to be 4 brown roses, she seemed to be of asiatic descent. Her face was cute and friendly. Short dark hair. She was wearing a finely made brown blouse with long sleeves, and a miniskirt plus thigh stockings.

"Sure." An event like this would never have happened to me in real life, so I was curious where this was heading.

"Nice to meet you, I am Lily."

"Euclid."

"An exotic name. Are you new to this city?"

I think about lying for a moment, but I have no reason to. I am certainly not going to try to show off here, I am penniless anyway.

"Yeah, I just got here." I admitted.

"I am sorry for your loss." She frowned, confusing me. "But look on the bright side." Her expression cheered up, spreading her arms. "Here in this afterlife, it is quite fun. You are going to like it."

At first I was confused, but as soon as she mentioned the afterlife, a thread of inspiration came to me. I remember the description and guess at what she meant. I've been thinking about this as just another place, but maybe the people here all died on Earth before being transported into the city. My character does not have a background so it slipped my mind.

"Yeah, it does seem like a lively place." I agree. "Maybe I'll be here for a while."

This gets a smile out of her. At that point the waiter came to our table, placed the glass of water that I ordered on my side and turned to take any further orders.

"Coffee please."

"Yes. Anything else sir, lady?"

"No, that will be all." I take the glass and take a sip of water. It is nice and refreshing. He leaves. I raise an eyebrow to Lily. "I would have liked some iced tea, but pft." I pucker my lips for emphasis. "No money."

"Ahahaha!" She waves it away. "If you've just got here, then you should have a 100 chips. Try bringing them out."

"Huh? How?" I start checking my pockets stupidly.

"Just focus." As I look at her, several stacks of translucent chips manifest in the air behind her. The thousands of chips in her pile look like they are intended for poker. Standing on nothing but air, I could see through them due to their translucency. "Then once they are staged, you can withdraw by wishing for it. For example, here I'll wish to get 20."

She raises her hand above the table, and like a magic trick, I see 20 chips moving into place. She lifts her hand and I see that the pile is no longer translucent. She lifts one, shows it to me and places it down with a clack.

"So it is like that? How do I do that?"

"Just try it."

Having an example of what I should do, I focus inwardly and I discover a sense that wasn't there before. Right in my mind I could see a stack of 100 chips. It feels different from just imagining it, like they are actually there.

"Yeah, good. I can see them behind you." She encouraged me.

Imitating her, I tried lifting my hand on the table and drawing them out from inside my sense. To my surprise it works and I can see the chips sliding into place. Lifting my hand, I count them. Feeling them out they are cold and slender to the touch.

"This is interesting. I guess I can order that iced tea. How do I bring them back?"

Lily did a little wave and the chips on her own side vanished. "As long as they are in your possession, even if they are away from you, you'll be able to recall them from anywhere. It is impossible to throw them away, you have to transfer ownership instead."

I wasn't sure how to do it, but I gave it a try and it worked. It seems that in VR, things just work.

"Bravo." Congratulating me, she opened a pack of sugar and added it to her coffee. With a spoon she started stirring it inside the liquid.

[Externus check DC 3.5 Failed - Sample 2.28]

I consider not ordering iced tea like I said I would, but that would be an asshole move. I can't see any reason to be stingy here. A part of me expected the chips to be important, but then I think about the job ads, the people going around me, Lily's own large stack and her placing her own order without issue. Nobody else as far as I can see has issue spending money. I guess 100 chips is not that much. I really meant to gamble with them rather than spend them like this, but I can always reload.

That would lose the connection with Lily though. Rather than working at a job, maybe I could get a loan and gamble with it? Since I can save and reload, I am in no danger of ever going bust unlike the NPCs.

I mean, I am not going to seriously do waitering for an entire month just to get the money to gambol. I want to get better at cards and learn some skills that would benefit me in real life.

So far, the NPCs here feel very lifelike, not at all like in a computer game made by humans. I take a look at Lily who is taking a sip of her coffee, with the pinky out. Cute, she is very cute. I can't believe that I, of all people, am getting charmed.

(Date with Lily)

I spent some time with her in that restaurant just chatting.

"I am working as a guide. If you want I'll show you around the city and get you accomodated. It would not be good if night falls and you have nowhere to sleep."

"Yeah, it would be bad if I had to sleep on the street once night falls."

“Yes, it would. Could you show me a cheap place to rent somewhere, first? After that I’d like to see what this town has to offer.”

“Of course.” She replied enthusiastically.

With that, the date started.

...

I spent some time touring the city with Lily. Lily is pretty cute, so I was a bit smitten by her, but I got tired of that after an hour. After that boredom started to kick in for me. Seriously, who cares about NPC women? She is cute, but I should be able to generate people like her by the million with a push of a button. I am not going to get sucked into the pace of things and let her become a part of my motivation for logging into Heaven's Key. How pathetic would that be?

With that mindset in place, instead of chatting about whatever comes to mind, I steer the conversation towards the city in general. Who are the big shots? What is life like? What are the challenges?

Goals like that are the only things preventing me from getting bored out of my skull. Back in school, there were times I went on an excursion with the rest of the class. Somehow those experiences ended up even more boring than going to class itself, if that is possible.

'Wow, look at the golden buildings! So cool!' I picture some wojaks pointing at the stuff in the background.

I got tired of it after 15 minutes.

Right now, I am acting like I think a normal person should act, but it is really straining my nerves. It is somewhat disgusting.

...

"WAAAAAAAAAAAHHHH!!!" Roller coaster rides rock! Seated in my coaster, being hurled through the air at high velocity! Based!

I was screaming, Lily was screaming next to me, the rest of the people in the wild ride were screaming!

This is more to my liking!

...

A whiff of barbecue drew me and I got a skewer for both me and Lily.

"Here you go!" A kindly man smiled at me, handing me my meat on a stick. I grab a bite and feel the spicy, juicy taste of meat spread through my mouth. The taste is just like in real life. Delicious!

I think I am starting to get a hang of how dating should work. Things are boring when you just let the other person take the lead. It became fun once I started drilling Lily for info on the town and dragged her into the roller coaster rides. It has been a few hours, both in the game and real life. I want to start getting to the point.

Me and Lily both finish our food, drink some colas, and then I get to the point.

"Lily, I was wondering." I manifest a poker chip between my index and middle finger waving it in front of me for emphasis. "These chips all look like they are made for gambling. So I am guessing they should have something with that."

I was expecting to hear something on the subject of card gambling from Lily, but for some reason nothing came up. I didn't care enough to push it back then, but now it is time to get to the point. I already know the theme of the game has something to do with gambling, so it is strange that I haven't heard anything about it from Lily.

"Who knows. The god who brought us all to this city made it like that. Nobody knows what goes through his mind." She shrugged.

Evading again, are you? Just what is the point of that? Do you really not know?

"Instead of just walking around town, why don't we go to a casino? I'd like to try playing some cards. You too Lily. Isn't it boring just going around town? I want more action like those roller coasters."

"Well..." She fell in thought. "Okay, I know a place, let's go there" She beamed, showing her expertise at maintaining positive energy. If I let her take the lead, she will just bore me to death, but I am sure that as a guide she is obligated to fulfill my wishes.

(Raven's Eye Casino)

She led us a few dozen blocks away, deeper into the city. There were a lot of people in the initial blocks, but I could only see a few people on the streets as we ventured deeper. They were much quieter than the area behind us. I thought this was weird. Usually, cities have dense crowds compared to the countryside. Do the people here spend all their time partying at amusement parks? That can't be. Rather...

"We are here." She announced, cutting off my line of thought. Her positive energy from before seemed subdued, and I sensed she was somewhat on the edge.

"Great. Let us have some fun. I do not remember anything from my past life, but I must have been a card shark." I announce, striding into the place ahead of her in search of stimulus. I spot the receptionist, slam 20 chips on the counter and say to the startled receptionist. "I want to play Texas Holdem. Lead me to the table."

"Come this way, sir." She got up from her seat at the counter and led the way deeper inside.

Passing by the rows of slot machines, I noticed the screens had dust on them. For some reason, slots, the staple of casinos, seemed to not be popular in this place. Much like outside, I couldn't see any people here. It was a quiet place. We went up a set of stairs into a game room.

It was a spacious room, with numerous tables, most of which were unoccupied. But there were a couple of groups playing cards, or rather just enjoying drinks there. I picked a table with 4 people, and walked up to it. Lily followed alongside me.

Now, my plan was to try to join a tournament that had a low buyin, or find a place where I could exchange for fake chips. Given how large the monthly salaries are here, I expected that with just 20 chips, I could at the minimum find a game with 1/2 blinds. This would leave me greatly short stacked. I thought about this for a bit on the way here, and I've concluded there is no real need to be fair. On one hand, I want to learn how to gamble, but either way, I am not going to spend a month of real time wage slaving in a video game. What I'll do is just save on every hand and reload if I lose it. That should allow me to escape my shoe string budget and get to the point where I can gamble seriously.

Looking around, I do not have much choice when it comes to game selection, I'll have to take whatever I can get. Since Lily led me here, the stakes should be fine. She knows my money situation, so she would not lead me to a place where the min stakes are 10/20 or something like that.

Since the next encounter will be sensitive, I try saving. Save. As soon as that thought leaves me, a window pops up. I name the save 'First game' and apply it.

Now I am set, if I lose I'll just go back to this point until I get it right. Whereas previously I had some nervousness about having to get a job if I lost, it completely deflated and I just felt the excitement of trying out gambling for the first time in a real casino.

"Hi, mind if we join?" I sit at the table and start the conversation like that. Apart from me and Lily, there are 4 guys at the table. One was a thin guy that seemed to be in his 20s, wearing a baseball cap backwards, while the others were in their 30s and 40s. The older guys were somewhat fat and had protruding guts. One of them was bald. They seemed to be dressed casually and felt right at home at the table.

"Sure." The bald guy in his 40s replied. It didn't seem like the rest of them were against it either.

I looked around, but I could not see a dealer. Before I arrived, these guys were just having beer and chilling at the table.

"So what are the stakes here? I only have 20 chips, if that is fine with you gentlemen." I made some small talk. I did a quick scan for the dealer again. Not only this table, none of the other tables had dealers either. I couldn't see a deck at the table.

"We typically play for a single chip per tourney."

"So it is a casual thing between friends? That is good. I was worried I would have to play 10bb deep in a cash game." I remarked. "We'll wait until you guys finish your drinks. I wonder why there aren't any dealers here?" I asked. The bald guy raised his eyebrows and looked at my partner.

"He is a new arrival. I haven't registered him as a citizen yet." She shook her head. Rough. Everyone is new at some point. The man shrugged his shoulders and leaned forward a bit, getting more serious.

"There is no need to wait, we'll start right away." He looked at the rest for confirmation and they nodded in return.

"Great! Should I go call for a dealer?" At my suggestion, the thin guy with a baseball cap had to stifle his laughter.

"No, that is not how it works. First we put the chips on the table." He placed a hand just above the table, and after he raised it, I could see a small stack of 20 poker chips manifested there. The rest of them follow his lead and do the same. Next to me, I could see Lily also doing the same. Eager to raise the stakes? That suits me just perfectly.

Seeing that the table is set, he continued. "Then I propose a duel, and you accept. Duel?" He said to the table.

"Accept."
"Accept."
"Accept." The 3 guys next to him confirmed.
"Accept." Lily went in lockstep with the group. All the eyes at the table were on me.
"Accept." I manifest 20 of my own chips, on the table and confirm, curious as to what would happen.

The world around me changes.

(The shadow realm)

Seated at the table, I didn't feel any physical force on my body as the environment transformed. Whereas previously we were in a large game room on the second floor of the casino, once I accepted the duel, the space around us warped. It felt like we're floating in space, surrounded by blue nebulas. At first I thought I could see stars, but then I realized they were too big for that. They appeared more like shards with yellow rims. It was a mythical space, removed from common sense. I felt out with my feet, and realized that even though it seemed like a sheer drop, there was solid grounds beneath me. I looked below and I couldn't really see what I was stepping on, but pressing on it felt solid. Thinking about it for a few moments, I realized it made sense that there would be some mechanism to prevent me from accidentally falling to my death if I left the seat. The chairs can’t be literally floating in the air, maybe they are standing on something like pure translucent glass?

All in all, I think I am getting used to this rather quickly.

I felt something moving and when I looked in front I saw that two face down cards were dealt to me, along with a button. Next them is a stack of 100 chips.

I seem to be in last place with Lily behind me. The group was seated as we were originally. I wonder if I am on the button because I was the last to accept?

"The rules are Texas Holdem. You have 5 minutes to make your decision otherwise it will be an auto-fold. The blinds double every 3 revolutions of the button in a 6-man game, meaning 18 hands from now. Is that clear, kid?" The bald man explained, watching me intently.

"Yes." I reach for my cards, and take a peek at them by twisting them upwards a little. I saw that in videos of real life poker games. The cards are nice and smooth to the touch, with a golden tint rather than the usual browns used in vanilla packs.

3s 7h. Crap hand.

The guy in the cap to the next to me in the small blind raises to 6, the big blind folds. The guy next to him raises to 20. The bald guy thinks about it for a few moments and follows up by raising to 50. Right behind me, Lily bows out of the action, and it is my turn to decide. I really have no reason to get involved in this hand.

[Gnosis check DC 1.8 Succeeded - Sampled 2.69]

"All in." Huh? Eh, whatever. Surprised at my own decision, I pushed in the stack causing it to topple over. The chips make satisfying sounds as they clank against each other. It would be best if the other guys just folded. The first two guys do so, tossing their cards into the middle. They vanish before coming to a stop.

Now it is just the bald guy and me. I keep my poker face as I watch him make a decision. He drums his fingers for a quarter of a minute as he observes me, takes a breath and then calls. "Call." He pushes his stack.

As I watch, by some invisible force, both our hands are flipped. He sees my hand, does a double take, and I see him holding Kc Kh.

From somewhere the cards appear on the table.

5h Ks 6d is the Flop. I don't care much about this hand, but I see his fist clench. He has trip kings now, and my only chance of winning is if the 4 gets dealt to give me a straight. My odds of getting that are about 4 in 45, about 11%.

The whole table is invested in the game now and holding its breath as the turn gets dealt.

A 9d. A miss. I have one more chance. Observing other people's reactions I see them leaning in slightly.

With bated breath, the next card comes in.

4c. I won. The bald guy makes a sour expression. I'd expect him to be mad at me, but not sparing a thought for me, I see him stealing a glance at Lily before he vanishes from the table completely. Having lost all his chips, he no longer needs to be present so the system aborted him.

As that happens the chips flow into my stack towering above the rest at 228. Nice!

"That was crazy, kid. I can't believe you went in with 37." One of the older guys who was num up to now said.
"I got a feeling." I nod knowingly, playing with my chip pile all the while.

The guy purses his lips, thinking of replying, but then thinks better of it. While that was going on the next hand started.

I won't go into detail as to how the rest of the game proceeded. Riding a wave of beginner's luck, I've been getting good hands and playing them aggressively, trying to get as many chips off them as I could, busting the rest of the table in only a couple dozen rounds.

(Raven's Casino, poker table)

After winning the game, I checked my chip pile and found it has grown to 60, tripling my balance.

"I won. Hey Lily, how much is the rake here?" I asked her. She shook her head.

"No rake. The casino doesn't take anything for duels." My eyebrows rose.

"Really?" I looked at the rest.

"Yeah..." The old guy nodded. This brought up a few questions in me such as what the distribution of winnings is like and why isn't there any rake? If that was true, how did the casino function? But I left those aside for the time being.

I manifested my whole pile and pushed it in, causing the thin guy's jaw to drop. "That is good to know. Let us continue. Duel?" The group looked at each other and then at Lily. Lightly, she nodded and pushed 60 of her own chips in after manifesting them. Way to go Lily! The guys seem to be following her lead for some reason.

"Accept."

"Accept." "Accept." "Accept." The rest followed in lockstep.

Back in the shadow realm, the action began again. I had no trouble hitting the board, and bluffing when I missed so I won again with no trouble. Back at the poker table, I saw the thin guy wiping the sweat off his face. He only lost like 80 chips, this is less than what a waiter makes in a day, what a weakling of a gambler. He should just get a job instead of wasting his time on a poker table if that worries him so much.

I save the game at this point, manifest my pile and push 180 chips in. "Duel?" I announce.

"Hey Dale..." A lot more reluctant now, the thin guy looked towards the bald guy who seemed to be the most experienced of the group. The bald guy, Dale, pursed his lips and deliberated for a moment, before refusing.

"Sorry, we are just a casual group. How about we keep it 60?" He asked. Not seeing a reason to keep being pushy and wanting to play more, I acceded to his request. I made the pile of 60 chips and asked to duel once again. Having won two games riding a wave of luck, the group seemed to be afraid of me, perhaps wondering if they were being hustled.

Back in the shadow realm, they started to tighten up and tried to pick me off with stronger hands. My luck started to wane and I had a harder time winning. We played a couple of games like that for a few hours, and I ended the day at 240 chips. I could have won a lot more had I abused my ability to save and reload, but I was satisfied with not dropping below 180. It wasn't my goal to win every single time, that would be suspicious.

I had to win the first and the second time to get out of red, but after that it was gravy. Rather than these noobs, I should seek out richer people to play against.

I had some fun game time. Saying goodbye to the group, me and Lily left. By that time, I saw the sun had gone down. We made our way back to the inn where I rented a room for a week.

"Do you want to come in for dinner? I'll treat you." I asked Lily, my hand on the handle of the door to the inn.

"Sorry, I have an appointment at a different place." She politely declined, before getting down to business. "I will have to charge you for today's tour though. 300 chips."

"That is quite expensive!" My hair rose. "It would clean me out. Er, do you mind waiting for a bit before I can pay you back? What will I eat tomorrow if I give you everything I have today."

"The inn will provide you meals, but don't worry the people here don't need to eat physical food anyway." She explained. "I know that 300 seems like a lot, and indeed, those who have just arrived can't afford it. In return, the guides take what they have and in return get them employment. I actually don't take this money for myself, but am officially employed by the city to welcome newcomers. It is merely a matter of policy."

"What happens if I don't pay right now?" I asked.

"I'll put it on your tab, but if you can't pay me in 3 days and are still unemployed, by law you'll be sent to jail."

"Vicious!" I exclaimed, startled. Lily made a sour face.

"Yeah, it sucks. This is because the city gets newcomers out of thin air, and to prevent them from just loitering in the streets, this policy has been instituted." She shrugged, sympathizing with me. "Don't worry, I'll come back tomorrow and look for a job with you. Once you have that it will take you only two days of work to make it up."

[Gnosis check DC 2.9 Failed - Sampled 2.18]

Hmmm...

[Gnosis check DC 1.7 Succeeded - Sampled 1.93]

What she is saying makes sense, but there is something off to this story. Not really understanding what the problem is, I do the most reasonable thing and save the game.

After that, with a shake of my head, I just decide to do it and see where this choice leads to. I call up my entire pile in its ghostly form and offer the floating chips.

"Here. You'll be here tomorrow to help me look for a job, right? Promise?" I query, offering her the chips.

"Of course, don't worry." With a sweet voice, she coaxes me, taking the offered chips. Without a sound they are transferred into her own ghostly pile. Not saying anything else, she turns around and leaves the scene. Behind her, I was no longer there. There was only the dark, empty street leading into the inn. The door that I had opened was slightly ajar where I left it, leaking a trail of light from the inside.

As soon as the transaction was complete, I felt my consciousness being wrenched from the world and into the abyss where there was nothing. A single window popped up to inform me of what happened.

> You died.

$$$

4:05pm. > You died.

This is the ideal spot to end the chapter on. This will make a perfect lead into the next chapter where I'll put the Heaven's Key poem. Let me grammar check it.

4:10pm. Damn it, is my neck stiff. I must have pulled it at some point two nights ago.

4:25pm. 16 pages. 7.4k words. Right now I should be like something like 17.4k words for the 4 chapters that I have written. I think 40 pages is enough to start off the publication on something like RR.

4:30pm. I won't hurry this too much. Let me register for an account first. I am done for today with writing and won't resume until I've published the first chapters. I'll also want to open a Patreon before I open the new ones.

4:40pm. Made an account.

> To submit your fiction, both the fiction information and the first chapter or prologue are required. After that, your submission will be inspected by our system and one of the staff members.

> If you have already posted your story elsewhere, be aware that we will require proof of content ownership. You can already submit a support ticket with it to speed up the process. Accepted proofs include editing your existing description on the site you've posted your story on the earliest, or an official document marking you as the author. We may also accept an email from a known email address of the copyright holder (i.e. published on the official website or in print in the book) as valid proof of ownership. Images are not accepted as proof.

> If you are making a support ticket ahead of time, please include link(s) to any pages that have the edited description to make the process faster.

4:55pm. It seems the system will crop the cover mightily.

How do I insert the image. Nevermind that for now.

Genre: Psychological, Sci-fi, Adventure
Tags: LitRPG, Soft Sci-fi, Virtual Reality, Artificial Intelligence, Male Lead, Mythos, Non-Human Lead, Progression, Technologically Engineered, Villanous Lead
Content Warning: Traumatising Content

The old arc sure traumatized me.

Synopsis: A story of playing a game in the post-Singularity era.

How do I add to that?

> A story of playing a game of poker in the post-Singularity era.

I've thought about the synopsis before, but never got far from this first sentence. I am not really sure how to summarize Heaven's Key. I guess I'll have to put some effort into it. I am going to take this task seriously, as the synopsis is the first thing the user sees. Though just leaving a single sentence like this if I cannot think of anything better is not too bad, I want to give it a serious try first. I am not in a hurry to publish this.

5:05pm. Let me take a break here.

I'll take a nap, to think about it for a while.

5:55pm. Done with lunch.

> A story of the search for power and self optimization in the post-Singularity era through the play of games.

Agh, I'll submit it tomorrow. I want to roll around in my mind how the perfect synopsis should be. Also the way paragraphs work in RR is different from this document so the gaps are too big. I need to fix that kind of issue. Maybe I could fix that indirectly, via some setting. It would be strange if something like that did not exist. The text options in RR are pretty rich.

> What could a single person do if an nearly limitlessly powerful computer was accessible to him? And what would the challenge is unleashing the power of such a device be?

> Master the chips and cards.

6:05pm. Let me close here. I'll somehow compose a proper synopsis tomorrow after thinking how the elements should come together."

---
## [deads2k/cluster-version-operator](https://github.com/deads2k/cluster-version-operator)@[9222fa9a66...](https://github.com/deads2k/cluster-version-operator/commit/9222fa9a6616b58a8056c780b9a6252e82a26e37)
#### Monday 2022-08-15 16:35:24 by W. Trevor King

pkg/cvo/sync_worker: Trigger new sync round on ClusterOperator versions[name=operator] changes

David and Stephen identified an uneccessary delay [1]:

* 9:42:00, CVO gives up on Kube API server ClusterOperator [2]
* 9:42:47, Kube API server operator achieves 4.12 [3]
* 9:46:22, after a cool-off sleep, the CVO starts in on a new manifest graph-walk attempt [4]
* 9:46:34, CVO notices that the Kube API server ClusterOperator is happy [5]

The 3+ minute delay from 9:42:47 to 9:46:22 is not helpful, and we've
probably had delays like this since my old e02d1489a5
(pkg/cvo/internal/operatorstatus: Replace wait-for with single-shot
"is it alive now?", 2021-05-13, #560), which landed in 4.6.

This commit introduces a "ClusterOperator bumped
versions[name=operator]" trigger to break out of the cool-off sleep.

There's plenty of room to be more precise here.  For example, you
could currently have a versions[name=operator] bump during the sync
loop that the CVO did notice, and that queued notification will break
from the sleep and trigger a possible useless reconciliation round
while we wait on some other resource.  You could drain the
notification queue before the sleep to avoid that, but you wouldn't
want to drain new-work notifications, and I haven't done the work
required to be able to split those apart.

I'm only looking at ClusterOperator at the moment, because of the many
types the CVO manages, ClusterOperator is the one we most frequently
wait on, as large cluster components take their time updating.  It's
possible but less likely that we'd want similar triggers for
additional types in the future (Deployment, etc.), if/when those types
develop more elaborate "is the in-cluster resource sufficient happy?"
checks.

The panic-backed type casting in clusterOperatorInterfaceVersionOrDie
also feel like a hack, but I wasn't able to find a cleaner way to get
at the structured information I want.  Improvements welcome :)

[1]: https://bugzilla.redhat.com/show_bug.cgi?id=2117033#c1
[2]: From Loki: E0808 09:42:00.022500       1 task.go:117] error running apply for clusteroperator "kube-apiserver" (107 of 806): Cluster operator kube-apiserver is updating versions
[3]: $ curl -s https://gcsweb-ci.apps.ci.l2s4.p1.openshiftapps.com/gcs/origin-ci-test/logs/periodic-ci-openshift-release-master-ci-4.12-upgrade-from-stable-4.11-e2e-gcp-sdn-upgrade/1556564581915037696/artifacts/e2e-gcp-sdn-upgrade/openshift-e2e-test/build-log.txt | grep 'clusteroperator/kube-apiserver versions:'
     Aug 08 09:33:48.603 I clusteroperator/kube-apiserver versions: raw-internal 4.11.0-rc.7 -> 4.12.0-0.ci-2022-08-07-192220
     Aug 08 09:42:47.917 I clusteroperator/kube-apiserver versions: operator 4.11.0-rc.7 -> 4.12.0-0.ci-2022-08-07-192220
[4]: From Loki: I0808 09:46:22.998344       1 sync_worker.go:850] apply: 4.12.0-0.ci-2022-08-07-192220 on generation 3 in state Updating at attempt 5
[5]: From Loki: I0808 09:46:34.556374       1 sync_worker.go:973] Done syncing for clusteroperator "kube-apiserver" (107 of 806)

---
## [RajaKunalPandit1/CodeForces_Questions](https://github.com/RajaKunalPandit1/CodeForces_Questions)@[62c3dd9177...](https://github.com/RajaKunalPandit1/CodeForces_Questions/commit/62c3dd91773ebfa6f899aa47f57a2bb6610783df)
#### Monday 2022-08-15 17:05:56 by Raja Kunal Pandit

Create 686A - Free Ice Cream.cpp

Output Status : 

By Rajakunalpandit, contest: Codeforces Round #359 (Div. 2), problem: (A) Free Ice Cream, Accepted

After their adventure with the magic mirror Kay and Gerda have returned home and sometimes give free ice cream to kids in the summer.

At the start of the day they have x ice cream packs. Since the ice cream is free, people start standing in the queue before Kay and Gerda's house even in the night. Each person in the queue wants either to take several ice cream packs for himself and his friends or to give several ice cream packs to Kay and Gerda (carriers that bring ice cream have to stand in the same queue).

If a carrier with d ice cream packs comes to the house, then Kay and Gerda take all his packs. If a child who wants to take d ice cream packs comes to the house, then Kay and Gerda will give him d packs if they have enough ice cream, otherwise the child will get no ice cream at all and will leave in distress.

Kay wants to find the amount of ice cream they will have after all people will leave from the queue, and Gerda wants to find the number of distressed kids.

Input
The first line contains two space-separated integers n and x (1 ≤ n ≤ 1000, 0 ≤ x ≤ 109).

Each of the next n lines contains a character '+' or '-', and an integer di, separated by a space (1 ≤ di ≤ 109). Record "+ di" in i-th line means that a carrier with di ice cream packs occupies i-th place from the start of the queue, and record "- di" means that a child who wants to take di packs stands in i-th place.

Output
Print two space-separated integers — number of ice cream packs left after all operations, and number of kids that left the house in distress.

Examples
inputCopy
5 7
+ 5
- 10
- 20
+ 40
- 20
outputCopy
22 1
inputCopy
5 17
- 16
- 2
- 98
+ 100
- 98
outputCopy
3 2
Note
Consider the first sample.

Initially Kay and Gerda have 7 packs of ice cream.
Carrier brings 5 more, so now they have 12 packs.
A kid asks for 10 packs and receives them. There are only 2 packs remaining.
Another kid asks for 20 packs. Kay and Gerda do not have them, so the kid goes away distressed.
Carrier bring 40 packs, now Kay and Gerda have 42 packs.
Kid asks for 20 packs and receives them. There are 22 packs remaining.

---
## [CursedBirb/tgstation](https://github.com/CursedBirb/tgstation)@[1a0e96885f...](https://github.com/CursedBirb/tgstation/commit/1a0e96885f469beb937b6bfdf2bcdab72e6df60a)
#### Monday 2022-08-15 17:30:39 by Amrabol

That shitty rebase command was not changing file into new version. God i hate rebase

---
## [aforren1/Psychtoolbox-3](https://github.com/aforren1/Psychtoolbox-3)@[c4e7808150...](https://github.com/aforren1/Psychtoolbox-3/commit/c4e7808150009caa232767696d32f91063b4f2e4)
#### Monday 2022-08-15 17:58:44 by kleinerm

Merge pull request #775 from kleinerm/master

Pull for 3.0.18.11 update

This is mostly a release with smaller quality of life improvements, some bug/compatibility fixes, and more work to take advantage of new Ubuntu 22.04-LTS features and improvements.

### General

- Various help text and documentation updates. Minor cleanups and improvements, maintenance work etc.

- PsychVRHMD: Prep work for future OpenXR driver, and some cleanups and minor fixes.

- PsychPortAudio: Add new AM modulator flag 256 "kPortAudioAMModulatorNeutralIsZero". By default, a stopped AM modulator device acts as if no AM modulator is attached. With this flag set, while attached to an audio output slave device, it will instead "gate" or "mute" sound output on its associated audio output device, iow. the AM gain value during stopped modulator is zero instead of one. This has proven useful to allow to output tone bursts that are windowed/gated/modulated by an envelope function. Sponsored by a paid support membership - Thanks.

- Eyelink: Fix potential false "buffer overflow" alert in 'EyelinkGetQueuedData', which can cause Octave/Matlab to abort() as a false alarm. Sponsored by SR-Research, paying members of our partnership program - Thanks.

### Linux

- XOrgConfCreator: Split up into a legacy version for systems with X-Server 1.20 and earlier, e.g., Ubuntu 20.04-LTS, and a modern version for systems with X-Server 21 and later, e.g., Ubuntu 22.04-LTS. The legacy version is now in maintenance mode, frozen in its behaviour for old systems. The X-Server 21 / Ubuntu 22.04-LTS version was cleaned up, extended and made more plug and play. It hides some rarely needed (for normal users) options behind a "expert mode" flag, simplifies the questions it asks to users, streamlines the whole setup experience, and exposes some new functionality only available on modern X-Server 21, e.g., AsyncFlipSecondaries support for clone/mirror display setups (subject + experimenter displays) which are not synchronized. Improvements to deep color setup, Prime renderoffload "Optimus" setup, VRR setup etc.

- Deal better with problems in AssertOpenGL, giving better troubleshooting advice -- now updated for Ubuntu 22.04-LTS

- Gamepad/GetGamepadIndices: Refinements for Linux/X11, help text updates. Make selection of the proper GamePad / Joystick device more simple and robust. This work supported by a Psychtoolbox paid support membership - Thanks.

### macOS

- PsychVulkan: Add a new workaround for another macOS Metal bug. Make visual presentation timing it a bit better, but still quite awful.

- Screen('AddFrameToMovie'): Change mapping of 'rect' to actual capture area. The old math didn't determine vertical start position of the capture rectangle by rect(kPsychTop), but based on rect(kPsychBottom), which could cause inconsistencies on movie frame capture area on macOS with Retina displays in Retina backwards compatibility mode. The new math fixes this, to deal with Retina displays better.

- Maybe restore backwards compatibility of Psychtoolbox 3.0.18 with macOS versions older than 10.15 Catalina, possibly back to 10.11 El Capitan with fixes to Screen and PsychPortAudio. This is untested, due to lack of any macOS test systems other than 10.15.7 Catalina final, but may work. Maintaining backwards compatibility is difficult without test systems and the constant breakage introduced by the iToys company in more recent SDK's and compiler toolchains. Officially we don't guarantee that current 3.0.18 runs on anything but Catalina.

---
## [aforren1/Psychtoolbox-3](https://github.com/aforren1/Psychtoolbox-3)@[94cbeffbfb...](https://github.com/aforren1/Psychtoolbox-3/commit/94cbeffbfbe92000cda9af106e9b8b30a96d4e26)
#### Monday 2022-08-15 17:58:44 by Mario Kleiner

PsychLinuxConfiguration: Add workarounds for RaspberryPi OS 11 Mesa v3d.

Testing after upgrading the RPi 400 to Raspbian 11 showed new trouble:

At least on Mesa's gallium v3d driver for the RPi 4/400's VideoCore 6
gpu, Raspbian 11 Bullseye, page-flipping is broken by default - again.
Pageflipping for fullscreen OpenGL PTB onscreen windows fails, with
error messages flooding the XOrg log, and the copyswap fallback causes
PTB timing failures and horrible tearing.

The RPi desktop GUI composited by the Mutter X11 desktop compositor
doesn't have that problem, because Mesa for Raspbian 11 was patched
with some out-of-tree downstream patches to accept a new secret
parameter "v3d_maintain_ignorable_scanout" that if set to true allows
to fix pageflipping, but defaults to false == broken. God knows why
"broken by default" was considered an appropriate config choice, but
here we are...

Reference link to the patch series, which is not to be found anywhere
else with a Google search, and not yet in Mesa main upstream:

https://gitlab.freedesktop.org/mesa/mesa/-/issues/6079
https://github.com/bluestang2006/Debian-Pkgs/tree/master/mesa/debian/patches

This adds the magic parameter to fix pageflipping for octave + PTB
to the deep color config file and updates PsychLinuxConfiguration to
always force-install/update that file on ARM systems. I'm too lazy
to add extra config files and revalidate stuff, so we stuff it into
an unrelated Mesa config file.

This should fix PTB on RPi OS 11 on RPi 4/400.

---
## [Jureiia/Skyrat-tg](https://github.com/Jureiia/Skyrat-tg)@[f0cef47678...](https://github.com/Jureiia/Skyrat-tg/commit/f0cef47678384716080d4cc2adfa8be85b9ddc69)
#### Monday 2022-08-15 20:19:29 by SkyratBot

[MIRROR] Adds the Mothroach [MDB IGNORE] (#15399)

* Adds the Mothroach (#68763)

About The Pull Request

Yup. That's pretty much it. This PR adds the Mothroach to the game, described as "An ancient ancestor of the moth that surprisingly looks like the crossbreed of a moth and a cockroach."

Do you love the Mothroach? Then you can cuddle with it and pat it, as well as place it on your head for extra cuteness.
What if you hate it, though? You can always kill and butcher Mothroaches in order to mass produce moth plushes for your own profit... How fun!

Either way, you win!

The Mothroach can be picked up and has a special on-head sprite (which looks really cute). It is able to vent-crawl and you may get one by randomly summoning a friendly mob through the gold slime extracts, or by ordering one through the Cargo Requests. After butchered, you may use its hide, a heart, and some cloth to craft a moth plushie, the most devilish of Devil's designs.

Full Preview of all the Sprites (NEW): https://www.youtube.com/watch?v=pdg8FTNEYjI
Preview of some of the Sprites (OLD): https://www.youtube.com/watch?v=9A-8hGCiW0s
In-hand, on-head, and grounded Mothroach sprite credits go to ValuedEmployee.
I did the Mothroach hide sprite though!
Why It's Good For The Game

The Mothroach is incredibly cute and a neat, fresh, new piece of content. Although it could use some future repurposing, right now it's simply a cute exotic pet with a few interactions.

These cute sprites are just too good to go to waste...

I keep seeing people complain about the lack of new content. Well, here's something niche that won't break the whole balance of the game and that will be cute. I seriously cannot see a motive not to add this to the game. Just because it isn't a powergaming tool or something that is seen every shift, that doesn't mean that it won't have a positive influence on the game. As I have stated, right now the Mothroaches are underperforming in terms of interactions and ways of getting them, but adding them is the first step to later improve them.
Changelog

cl
add: The Mothroach, your new local exotic pet
add: Mothroach Hide and Mothroach Meat
add: New crafting recipe for the Moth Plush: 1 Mothroach Hide; 1 heart; 3 cloth
fix: Fixes dead mobs on-head not having sprites
/cl

* Adds the Mothroach

Co-authored-by: Justice <42555530+Justice12354@users.noreply.github.com>

---
## [eldoriarpg/BloodNight](https://github.com/eldoriarpg/BloodNight)@[220ebccac0...](https://github.com/eldoriarpg/BloodNight/commit/220ebccac02bf5ff38cae5892bfaee28c107b4ac)
#### Monday 2022-08-15 21:07:43 by MinerCoffee

Knight Zombie Boss (#115)

* I have added a new boss called KnightZombie. It has special properties to block the player's attack and can push them two blocks higher. I have also added custom drops to this mob. It includes Iron nuggets, experience bottles, and rotten flesh. They all have a chance to get to a random drops.

* Update BloodNight-core/src/main/java/de/eldoria/bloodnight/specialmobs/mobs/zombie/KnightZombie.java

Co-authored-by: Lilly Tempest <46890129+RainbowDashLabs@users.noreply.github.com>

* Update BloodNight-core/src/main/java/de/eldoria/bloodnight/specialmobs/mobs/zombie/KnightZombie.java

Co-authored-by: Lilly Tempest <46890129+RainbowDashLabs@users.noreply.github.com>

* Optimized and changed events.

* Moved actions around to fit the corresponding events.

* Fixed player velocity to get launched. The player.getVelocity does not work how I want to. I changed it to setVelocity as it functions how it should. Fixed timings for the events. Everything works as expected.

Co-authored-by: Lilly Tempest <46890129+RainbowDashLabs@users.noreply.github.com>

---
## [Nikostormkilla/Nikostormkilla](https://github.com/Nikostormkilla/Nikostormkilla)@[9967019520...](https://github.com/Nikostormkilla/Nikostormkilla/commit/99670195208859c644524bf38248e4b1f1e457b5)
#### Monday 2022-08-15 21:10:22 by Grayson

Earlier in the song I used the term "galvanistic," and galvanism is the concept, uh, the obsolete scientific theory that there is a kind of electricity flowing through our bloodstreams, and that was our life force. I used the term because I came across it in, uh, Mary Shelley's, uh, "Frankenstein", and that book is sort of an exploration of the theme of creating a character, of making up a person. So I used the term "galvanistic" to allude to that book as a sort of a symbol of how I, like, created you as a character. I'm pretending that I know a lot more about you than I actually do, and also to refer to the fact that I've fall—fallen in love with the characters you've created in, uh, your body of work  This is the part of the song where I start to regret writing it

Earlier in the song I used the term "galvanistic," and galvanism is the concept, uh, the obsolete scientific theory that there is a kind of electricity flowing through our bloodstreams, and that was our life force. I used the term because I came across it in, uh, Mary Shelley's, uh, "Frankenstein", and that book is sort of an exploration of the theme of creating a character, of making up a person. So I used the term "galvanistic" to allude to that book as a sort of a symbol of how I, like, created you as a character. I'm pretending that I know a lot more about you than I actually do, and also to refer to the fact that I've fall—fallen in love with the characters you've created in, uh, your body of work

This is the part of the song where I start to regret writing it

---
## [JuliaPackaging/BinaryBuilderBase.jl](https://github.com/JuliaPackaging/BinaryBuilderBase.jl)@[cf90fb4377...](https://github.com/JuliaPackaging/BinaryBuilderBase.jl/commit/cf90fb437738ecc8495b9ac150c7e8436f3110e2)
#### Monday 2022-08-15 21:34:56 by Keno Fischer

Add support for building sanitizer-enabled jlls

This adds support for automatically adding the appropriate `-fsanitize=`
flags when the platform includes a `sanitizer` tag. This is particularly
intended for msan, which requires that all .so's in the system are built
using it, but could be useful for other sanitizers also.

There's a couple annoyances. One is that we don't currently actually ship
the sanitizer runtime libraries in our rootfs. Thus, if we want to start
using this, we'd have to add a BuildDependency on LLVMCompilerRT_jll and
manually copy the runtime libraries into place. Not the end of the world,
but certainly a wart.

The other issue is that `platform_matches` (which is defined in Base) of
course currently ignores the `sanitizer` tag. In theory it is possible
to add a custom compare strategy, but since we're specifying the target
by triplet, we can't really add that. Easy enough to add manually here,
but does make me wonder whether the custom compare strategies in Base
actually fit the use case.

---
## [UltraFormula1/Platformer](https://github.com/UltraFormula1/Platformer)@[d85c8b0256...](https://github.com/UltraFormula1/Platformer/commit/d85c8b0256152baf7feedf51982278cf18f5adc5)
#### Monday 2022-08-15 23:00:39 by UltraFormula1

Day 17

Day 17 in the village: A violent fight broke out today, we've never seen something so extreme...
"Ah! You've moved my drink!"
"Oh my god, I'm so sorry!"
"Oh, It's okay"

---

