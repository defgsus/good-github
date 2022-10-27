## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-26](docs/good-messages/2022/2022-10-26.md)


2,398,148 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,398,148 were push events containing 3,602,094 commit messages that amount to 275,747,450 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 44 messages:


## [EastsidePreparatorySchool/ChemLogs](https://github.com/EastsidePreparatorySchool/ChemLogs)@[5378148e25...](https://github.com/EastsidePreparatorySchool/ChemLogs/commit/5378148e25d6156a49286cc3311862a8389b469c)
#### Wednesday 2022-10-26 00:00:53 by Cluelessbutnothomeless

Test Page for Chemical Searching

When I started this page I had no idea what I was doing. I still have no idea what I am doing. But I can attest that the above code works, the majority of the time at least. I'm not sure how detailed this description is supposed to be but I will keep it short. It looks good I guess, at the very least its not an abhorrent aberration grotesque to all animal eyes. So that's good. :) While some might say I took my inspiration from the Nordstrom Active Apparel website I would be quick to remind them that there is a high possibility that Nordstrom stole their design form someone else and therefore my acting is the equivalent of balancing the cosmic scales. Now I'm sure being a cosmic balancer puts me dead in the sights of more than one ancient prophecy but I will remind the reader that I am still me. Still the same coder struggling to comprehend whether or not html is a language or a jumble of misshapen letters. Alas we have come to the end of my summary, I should hope it was informative to have a description of my mindset when coding the page. Maybe even helpful? Humbly, Aroura

---
## [Team2338/2022_BAB_B](https://github.com/Team2338/2022_BAB_B)@[7b9dc51816...](https://github.com/Team2338/2022_BAB_B/commit/7b9dc51816f437924d9aa6acf6237d321b4d5604)
#### Wednesday 2022-10-26 00:04:23 by Geet Gambhir

Yeah never mind im kinda stupid and i need to use my own shooter code

---
## [sirdarckcat/linux-1](https://github.com/sirdarckcat/linux-1)@[d21f4b7ffc...](https://github.com/sirdarckcat/linux-1/commit/d21f4b7ffc22c009da925046b69b15af08de9d75)
#### Wednesday 2022-10-26 00:05:37 by Douglas Anderson

pinctrl: qcom: Avoid glitching lines when we first mux to output

Back in the description of commit e440e30e26dd ("arm64: dts: qcom:
sc7180: Avoid glitching SPI CS at bootup on trogdor") we described a
problem that we were seeing on trogdor devices. I'll re-summarize here
but you can also re-read the original commit.

On trogdor devices, the BIOS is setting up the SPI chip select as:
- mux special function (SPI chip select)
- output enable
- output low (unused because we've muxed as special function)

In the kernel, however, we've moved away from using the chip select
line as special function. Since the kernel wants to fully control the
chip select it's far more efficient to treat the line as a GPIO rather
than sending packet-like commands to the GENI firmware every time we
want the line to toggle.

When we transition from how the BIOS had the pin configured to how the
kernel has the pin configured we end up glitching the line. That's
because we _first_ change the mux of the line and then later set its
output. This glitch is bad and can confuse the device on the other end
of the line.

The old commit e440e30e26dd ("arm64: dts: qcom: sc7180: Avoid
glitching SPI CS at bootup on trogdor") fixed the glitch, though the
solution was far from elegant. It essentially did the thing that
everyone always hates: encoding a sequential program in device tree,
even if it's a simple one. It also, unfortunately, got broken by
commit b991f8c3622c ("pinctrl: core: Handling pinmux and pinconf
separately"). After that commit we did all the muxing _first_ even
though the config (set the pin to output high) was listed first. :(

I looked at ideas for how to solve this more properly. My first
thought was to use the "init" pinctrl state. In theory the "init"
pinctrl state is supposed to be exactly for achieving glitch-free
transitions. My dream would have been for the "init" pinctrl to do
nothing at all. That would let us delay the automatic pin muxing until
the driver could set things up and call pinctrl_init_done(). In other
words, my dream was:

  /* Request the GPIO; init it 1 (because DT says GPIO_ACTIVE_LOW) */
  devm_gpiod_get_index(dev, "cs", GPIOD_OUT_LOW);
  /* Output should be right, so we can remux, yay! */
  pinctrl_init_done(dev);

Unfortunately, it didn't work out. The primary reason is that the MSM
GPIO driver implements gpio_request_enable(). As documented in
pinmux.h, that function automatically remuxes a line as a GPIO. ...and
it does this remuxing _before_ specifying the output of the pin. You
can see in gpiod_get_index() that we call gpiod_request() before
gpiod_configure_flags(). gpiod_request() isn't passed any flags so it
has no idea what the eventual output will be.

We could have debates about whether or not the automatic remuxing to
GPIO for the MSM pinctrl was a good idea or not, but at this point I
think there is a plethora of code that's relying on it and I certainly
wouldn't suggest changing it.

Alternatively, we could try to come up with a way to pass the initial
output state to gpio_request_enable() and plumb all that through. That
seems like it would be doable, but we'd have to plumb it through
several layers in the stack.

This patch implements yet another alternative. Here, we specifically
avoid glitching the first time a pin is muxed to GPIO function if the
direction of the pin is output. The idea is that we can read the state
of the pin before we set the mux and make sure that the re-mux won't
change the state.

NOTES:
- We only do this the first time since later swaps between mux states
  might want to preserve the old output value. In other words, I
  wouldn't want to break a driver that did:
     gpiod_set_value(g, 1);
     pinctrl_select_state(pinctrl, special_state);
     pinctrl_select_default_state();
     /* We should be driving 1 even if "special_state" made the pin 0 */
- It's safe to do this the first time since the driver _couldn't_ have
  explicitly set a state. In order to even be able to control the GPIO
  (at least using gpiod) we have to have requested it which would have
  counted as the first mux.
- In theory, instead of keeping track of the first time a pin was set
  as a GPIO we could enable the glitch-free behavior only when
  msm_pinmux_request_gpio() is in the callchain. That works an enables
  my "dream" implementation above where we use an "init" state to
  solve this. However, it's nice not to have to do this. By handling
  just the first transition to GPIO we can simply let the normal
  "default" remuxing happen and we can be assured that there won't be
  a glitch.

Before this change I could see the glitch reported on the EC console
when booting. It would say this when booting the kernel:
  Unexpected state 1 in CSNRE ISR

After this change there is no error reported.

Note that I haven't reproduced the original problem described in
e440e30e26dd ("arm64: dts: qcom: sc7180: Avoid glitching SPI CS at
bootup on trogdor") but I could believe it might happen in certain
timing conditions.

Fixes: b991f8c3622c ("pinctrl: core: Handling pinmux and pinconf separately")
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-by: Stephen Boyd <swboyd@chromium.org>
Link: https://lore.kernel.org/r/20221014103217.1.I656bb2c976ed626e5d37294eb252c1cf3be769dc@changeid
Signed-off-by: Linus Walleij <linus.walleij@linaro.org>

---
## [david-rowley/postgres](https://github.com/david-rowley/postgres)@[8272749e8c...](https://github.com/david-rowley/postgres/commit/8272749e8ca1dbbcb5f8cf5632ec26a573ac3111)
#### Wednesday 2022-10-26 01:42:06 by Tom Lane

Record dependencies of a cast on other casts that it requires.

When creating a cast that uses a conversion function, we've
historically allowed the input and result types to be
binary-compatible with the function's input and result types,
rather than necessarily being identical.  This means that the new
cast is logically dependent on the binary-compatible cast or casts
that it references: if those are defined by pg_cast entries, and you
try to restore the new cast without having defined them, it'll fail.
Hence, we should make pg_depend entries to record these dependencies
so that pg_dump knows that there is an ordering requirement.

This is not the only place where we allow such shortcuts; aggregate
functions for example are similarly lax, and in principle should gain
similar dependencies.  However, for now it seems sufficient to fix
the cast-versus-cast case, as pg_dump's other ordering heuristics
should keep it out of trouble for other object types.

Per report from David Turoň; thanks also to Robert Haas for
preliminary investigation.  I considered back-patching, but
seeing that this issue has existed for many years without
previous reports, it's not clear it's worth the trouble.
Moreover, back-patching wouldn't be enough to ensure that the
new pg_depend entries exist in existing databases anyway.

Discussion: https://postgr.es/m/OF0A160F3E.578B15D1-ONC12588DA.003E4857-C12588DA.0045A428@notes.linuxbox.cz

---
## [DaedalusDock/Gameserver](https://github.com/DaedalusDock/Gameserver)@[e273ed1b5f...](https://github.com/DaedalusDock/Gameserver/commit/e273ed1b5f2cc445810bf4b6f3a0ea659d40a43a)
#### Wednesday 2022-10-26 01:44:17 by Kapu1178

update screenshot tests (#55)

* update screenshot tests

* try fix issues

* fix

* try fix lizard

* fuck you im tired

* fucking come on

* fuck it im disabling this and fixing it later

* Fix chain pull through space issue (fixes unit test failure) (#69832)

* Disables ashwalker unit test

* FUCK YOU

Co-authored-by: Marina <50789504+KirbyDaMaster@users.noreply.github.com>

---
## [RodrigoSanchez06/CheemSmart](https://github.com/RodrigoSanchez06/CheemSmart)@[845ea82792...](https://github.com/RodrigoSanchez06/CheemSmart/commit/845ea8279241786fa48e2be2afdf7e1088bba664)
#### Wednesday 2022-10-26 01:47:15 by Chao280802

Merge pull request #16 from RodrigoSanchez06/Chao

Implemented english (Fuck you Gael MF)

---
## [Ryll-Ryll/tgstation](https://github.com/Ryll-Ryll/tgstation)@[f923f61011...](https://github.com/Ryll-Ryll/tgstation/commit/f923f6101103e4ff1aeefd57d0531a3bc437a77a)
#### Wednesday 2022-10-26 02:14:42 by MMMiracles

Tramstation: Modular Maintenance Insanity (#69000)

About The Pull Request
Every single part of maintenance has been segmented into modules with multiple variants with different themes. As it stands, there are currently 80 modular parts that come together to form the entire maintenance layout for both levels. Part 1 of a 2 part PR set, requires #69486 to have full effect.

Why It's Good For The Game
Maintenance as it stands is a bit barren, not much reason to explore it with boring same-same rooms despite current randomized modules. With these issues in mind, I completely scrapped maintenance as it was and rebuilt it in mind with full modular segments with proper documentation on what each piece is and where it is located. These changes were also designed to make maintenance more friendly for our dark-dwelling antags and xenos alike, as each major module now has an air vent and scrubber.

Fixes #68320

Main Event:

Every single part of maintenance was turned into module chunks. Sections of the map that originally had maintenance was traced out with checkered flooring so mappers can still see the general layout of the tunnels when making larger edits.
Every module has been documented with proper nodes with descriptions of where each module is located on the map.
Each main module has a regular variant and an abandoned variant. Abandoned variants have blocked access routes and look more like unfinished carved out tunnels than regular maintenance.
Each module has 2 attachment points barring 2. Each attachment has 3 potential layouts that are chosen each round. A storage room with construction supplies one round might be a carved out room with minerals the next.
QoL/General Fixes:

Maintenance should have much more xeno/antag spawns to give various mid-round antags better chances at starting.
Camera network has been given a once-over with duplicate/floating cameras fixed.
The helpful bots in the lower tunnel should now actually do full rotations instead of whatever the hell they were doing before.
I still need to do some testing with disposals and final touch ups to make sure there aren't any weird overlaps, but as of right now the actual mapping quality is ready for review.

---
## [avar/git](https://github.com/avar/git)@[d3775de074...](https://github.com/avar/git/commit/d3775de0745c975e2d13819a630757b2bbb673c3)
#### Wednesday 2022-10-26 02:50:42 by Jeff King

Makefile: force -O0 when compiling with SANITIZE=leak

Compiling with -O2 can interact badly with LSan's leak-checker, causing
false positives. Imagine a simplified example like:

  char *str = allocate_some_string();
  if (some_func(str) < 0)
          die("bad str");
  free(str);

The compiler may eliminate "str" as a stack variable, and just leave it
in a register. The register is preserved through most of the function,
including across the call to some_func(), since we'd eventually need to
free it. But because die() is marked with NORETURN, the compiler knows
that it doesn't need to save registers, and just clobbers it.

When die() eventually exits, the leak-checker runs. It looks in
registers and on the stack for any reference to the memory allocated by
str (which would indicate that it's not leaked), but can't find one.  So
it reports it as a leak.

Neither system is wrong, really. The C standard (mostly section 5.1.2.3)
defines an abstract machine, and compilers are allowed to modify the
program as long as the observable behavior of that abstract machine is
unchanged. Looking at random memory values on the stack is undefined
behavior, and not something that the optimizer needs to support. But
there really isn't any other way for a leak checker to work; it
inherently has to do undefined things like scouring memory for pointers.
So the two things are inherently at odds with each other. We can't fix
it by changing the code, because from the perspective of the program
running in an abstract machine, there is no leak.

This has caused real false positives in the past, like:

  - https://lore.kernel.org/git/patch-v3-5.6-9a44204c4c9-20211022T175227Z-avarab@gmail.com/

  - https://lore.kernel.org/git/Yy4eo6500C0ijhk+@coredump.intra.peff.net/

  - https://lore.kernel.org/git/Y07yeEQu+C7AH7oN@nand.local/

This patch makes those go away by forcing -O0 when compiling with LSan.
There are a few ways we could do this:

  - we could just teach the linux-leaks CI job to set -O0. That's the
    smallest change, and means we wouldn't get spurious CI failures. But
    it doesn't help people looking for leaks manually or in a specific
    test (and because the problem depends on the vagaries of the
    optimizer, investigating these can waste a lot of time in
    head-scratching as the problem comes and goes)

  - we default to -O2 in CFLAGS; we could pull this out to a separate
    variable ("-O$(O)" or something) and modify "O" when LSan is in use.
    This is the most flexible, in that you could still build with "make
    O=2 SANITIZE=leak" if you really wanted to (say, for experimenting).
    But it would also fail to kick in if the user defines their own
    CFLAGS variable, which again leads to head-scratching.

  - we can just stick -O0 into BASIC_CFLAGS when enabling LSan. Since
    this comes after the user-provided CFLAGS, it will override any
    previous -O setting found there. This is more foolproof, albeit less
    flexible. If you want to experiment with an optimized leak-checking
    build, you'll have to put "-O2 -fsanitize=leak" into CFLAGS
    manually, rather than using our SANITIZE=leak Makefile magic.

Since the final one is the least likely to break in normal use, this
patch uses that approach.

The resulting build is a little slower, of course, but since LSan is
already about 2x slower than a regular build, another 10% slowdown isn't
that big a deal.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [Nyanotrasen/Nyanotrasen](https://github.com/Nyanotrasen/Nyanotrasen)@[5d89272aca...](https://github.com/Nyanotrasen/Nyanotrasen/commit/5d89272acabaca00394158578b899f4d06794d70)
#### Wednesday 2022-10-26 04:24:48 by Rane

Femaleclothingearlymerge (#601)

* well, they both load...

* holy shit it works

* nullable female mask

* fix female clothing mask

---
## [sndrec/test_stuff](https://github.com/sndrec/test_stuff)@[4780e37b35...](https://github.com/sndrec/test_stuff/commit/4780e37b357ff4bc745c50acbc032aefd824a6d8)
#### Wednesday 2022-10-26 04:28:22 by Brandon Johnson

Holy shit I need to remember to push when I update

---
## [SecurityLab-CodeAnalysis/scalameta_metals](https://github.com/SecurityLab-CodeAnalysis/scalameta_metals)@[6fca4bc1b2...](https://github.com/SecurityLab-CodeAnalysis/scalameta_metals/commit/6fca4bc1b27e11e955a366b6251a2e8ec73ff755)
#### Wednesday 2022-10-26 05:01:32 by ckipp01

feat: capture and forward `diagnosticCode`

This relates to the grand plan of
https://github.com/lampepfl/dotty/issues/14904 and recently forwarding
the `diagnosticCode` has been merged in
https://github.com/lampepfl/dotty/pull/15565 and also backported so it
should show up in the 3.2.x series. While this pr isn't super exciting,
it's just making sure we capture the code and forward it, this should
unlock _much_ better ways to determine what code actions are available
for a given diagnostic. Meaning we don't have to do lovely things like
regex on the diagnostic message for Scala 3 diagnostics.

NOTE: that this does need some more changes in the build servers before
this is usable. So we can wait for those to be merged in if you'd like.

- [ ] sbt - https://github.com/sbt/sbt/pull/6998
- [ ] Bloop - https://github.com/scalacenter/bloop/pull/1750
- [ ] Mill - https://github.com/com-lihaoyi/mill/pull/1912

Now if you look at the trace file for a diagnostic you'll see the
addition of the code:

```
  "diagnostics": [
    {
      "range": {
        "start": {
          "line": 9,
          "character": 15
        },
        "end": {
          "line": 9,
          "character": 19
        }
      },
      "severity": 1,
      "code": "7",
      "source": "sbt",
      "message": "Found:    (\u001b[32m\"hi\"\u001b[0m : String)\nRequired: Int\n\nThe following import might make progress towards fixing the problem:\n\n  import sourcecode.Text.generate\n\n"
    }
  ],
```

Refs: https://github.com/lampepfl/dotty/issues/14904

---
## [nfagerlund/bevy-tablestakes](https://github.com/nfagerlund/bevy-tablestakes)@[94bec68314...](https://github.com/nfagerlund/bevy-tablestakes/commit/94bec683147a6944880fb3afb1ab0ded893e8d70)
#### Wednesday 2022-10-26 05:06:18 by Nick Fagerlund

Refactor char_animation to use enum for direction variants

god damn I love compiler-driven refactoring. This required zero guesswork
and zero squinting at bullshit, I just received everything I needed
in a fruit basket.

---
## [Jvondamm/CSC369](https://github.com/Jvondamm/CSC369)@[1647efcb97...](https://github.com/Jvondamm/CSC369/commit/1647efcb97a5bcc3815ba25277a2081faea4b259)
#### Wednesday 2022-10-26 05:25:18 by joshuavd

god i need a ai to code this shit for me fuckin hell

---
## [neebe000/kernel_xiaomi_mt6785](https://github.com/neebe000/kernel_xiaomi_mt6785)@[cb6809b7fb...](https://github.com/neebe000/kernel_xiaomi_mt6785/commit/cb6809b7fb318625ba816c6c96e68128757cf6f1)
#### Wednesday 2022-10-26 06:30:34 by Peter Zijlstra

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
## [Blsexual/TAKEEE](https://github.com/Blsexual/TAKEEE)@[19080cc678...](https://github.com/Blsexual/TAKEEE/commit/19080cc6788b3be34f5ab6bddc19aad74e21fd32)
#### Wednesday 2022-10-26 07:14:36 by Nixeff

Merge pull request #71 from Blsexual/check_token

fuck you kevin

---
## [Talend/component-runtime](https://github.com/Talend/component-runtime)@[466df4dd49...](https://github.com/Talend/component-runtime/commit/466df4dd49f9666419c591f968a5273ad5334306)
#### Wednesday 2022-10-26 07:27:20 by Antoine Nicolas

fix(TCOMP-2241): use Beam-aware classloader to run ProducerFinder pipeline

The ProducerFinder service & interface has been introduced a few months ago to explicitely offer the ability to read some Dataset data (using it's input connector, a Record producer) from within another component.

Functionally, one of it's use-case is the "join" (or "lookup") feature in Data Preparation: you're able to join another Dataset's data to the preparation. This function, just like all TDP functions, is implemented within the processing-functions component as a TCK processor.

Implementations of this new ProducerFinder service are discovered using a SPI, or fallback to a default implementation. It turns out that the default implementation is only able to instantiate TCK-based input components.

One major issue we had is that some older components are not pure TCK-based, but implemented using Beam APIs (Local file, S3, ...)

To overcome this, a new BeamProducerFinder implementation of ProducerFinder has been introduced (in the component-runtime-beam module), which is capable of reading data from Beam-based input components. How? By running an in-memory Beam pipeline. Running a pipeline in-memory is a bit different than our normal usecase: it uses a different Beam Runner called a DirectRunner (while the "real" pipelines use a SparkRunner).

To run, this DirectRunner needs to load some implementations of a few interfaces (for reasons we won't detail). To do so, as Beam is extensible, it sometimes leverages the ServiceLoader API to find implementations for these classes.

When the pipeline is actually ran in the DirectRunner pipeline, the executing thread class current classloader is the component classloader, not the application classloader (again, it makes perfect sense, we're actually in the component execution context).

But because of the filtering, the ServiceLoader API can't find Beam's SPI implementations, because their corresponding service configuration file in META-INF/services is not accessible from the component classloader. While one can specify which classloader to use when calling ServiceLoader.load , the code which does this is deep inside Beam DirectRunner implementation and thus out of our reach.

Currently, the "Join" Beam pipeline is ran in the caller classloader, in our case the processing-functions component's one.

The chosen solution to fix the issue is to make sure that the pipeline is run in the application classloader (and of course restore the current thread classloader just after). With this change, Beam DirectRunner will have no trouble finding the appropriate resources and the pipeline will run fine.

There is also no problem of calling the input connector with the wrong classloader, as the magical classloader dance will happen at some point before reaching the input emitter (hint: set a breakpoint in Thread#setContextClassLoader to see the magic happen).

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[f63a01ede1...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/f63a01ede163ca61d7388f4953fb43f038d4f2d3)
#### Wednesday 2022-10-26 08:20:56 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [fewlinesco/dependabot-auto-merge](https://github.com/fewlinesco/dependabot-auto-merge)@[dcee78cd02...](https://github.com/fewlinesco/dependabot-auto-merge/commit/dcee78cd022e7f77efd356728db2e4efff99912c)
#### Wednesday 2022-10-26 08:55:59 by Clement

Readme: fix typos and lost quotes + add credits (#35)

## Description

This PR fixes some lost typos, `"` and adds credits for the repo
inspiration.

## Related Issue

https://linear.app/fewlines/issue/TRB-69/add-the-gha-to-turbo

## Motivation and Context

Because... it was ugly!
And also because I forgot to add credits at the start.

## How Has This Been Tested?

With my own two eyes

## Screenshots

<!--- if appropriate, otherwise the section can be removed -->

## Types of changes

<!--- What types of changes does your code introduce? Stroke -->
<!-- (i.e. ~stroked text~) the ones that don't apply: -->
- Chore (non-breaking change which refactors / improves the existing
code base)
- ~Bug fix (non-breaking change which fixes an issue)~
- ~New feature (non-breaking change which adds functionality)~
- ~Breaking change (fix or feature that would cause existing
functionality to
  change)~

## Checklist:

<!--- Go over all the following points, and replace the 🔴 in all -->
<!--- the lines with a ✅ when relevant. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're
-->
<!--- here to help! -->
- 🔴 My change requires a change to the documentation.
- 🔴 I have updated the documentation accordingly.
- 🔴 I have added tests to cover my changes.
- ✅ All new and existing tests passed.
- ✅ I have read the
[CONTRIBUTING](https://github.com/fewlinesco/eslint-config/blob/main/CONTRIBUTING.md)
document.

Co-authored-by: Fanien Louis <34440340+TheRealAstoo@users.noreply.github.com>

---
## [centurysys/linux-kernel-MAE](https://github.com/centurysys/linux-kernel-MAE)@[adee8f3082...](https://github.com/centurysys/linux-kernel-MAE/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Wednesday 2022-10-26 09:03:44 by Peter Zijlstra

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
## [Blessing1135/branding](https://github.com/Blessing1135/branding)@[ac4d794610...](https://github.com/Blessing1135/branding/commit/ac4d794610d73d581ba9284238d832e212dcb020)
#### Wednesday 2022-10-26 10:14:43 by Blessing1135

Add files via upload

Social Preview Image for Github open-life-science#4
After researching what a social preview is, I got to understand that social preview are cards that give a preview of what a shared link will lead to across all social media page like Twitter, slack, and linked-in, etc., this is also eye catchy which make users get interested to click and see what that sites actually look like.
Well, I just got into UI/UX design a few months ago and for now, this design was made using the Figma App which I am more familiar with and also comfortable with for now, and I also hope to explore other Apps for better usage and understanding as time goes on, The colors used for this design are Green with a color code of #28a82d, Blue with a code of #287aab, White and Black with an opacity of 100% and 95% respectively, Using the Montserrat font for all texts using 36px for the header and 24px for body text. However, I tried to check the project guides on Colors, Fonts, and other tools but couldn't find any so I decided to go with the brand colors generally creating my own Code in the meantime. I also used the 8px grids. attach above is also the link to the file uploaded.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[b8f4340b26...](https://github.com/odoo-dev/odoo/commit/b8f4340b264c2fc7c8089b992642b92c7cf28a71)
#### Wednesday 2022-10-26 11:47:52 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: web_editor

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with an ugly patch. We'll review what to do in
master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3

opw-3031217
opw-3032482
opw-3035289

---
## [mysociety/contract-countdown](https://github.com/mysociety/contract-countdown)@[c80045ea00...](https://github.com/mysociety/contract-countdown/commit/c80045ea00e7dcd4321368d761098423d79bb5dc)
#### Wednesday 2022-10-26 12:47:05 by Zarino Zappia

Improving error handling for postcode input

Using `{% bootstrap_field %}` gets us nice automatic error handling,
and just feels like the right thing to do.

But for that to work, we need `server_side_validation` enabled, which
brings with it the green "is-valid" styling on valid inputs, which
looks weird when you’re submitting the search/filter form.

There is, annoyingly, no way to prevent django-bootstrap5 from
generating these .is-valid classes, so instead we customise our
Bootstrap settings to prevent the .is-valid style rules from ever
being generated. This means duplicating a few more lines of
bootstrap/_variables.scss into our own /_variables.scss, but I think
it’s worth it to avoid the distracting .is-valid styling.

One annoyance I couldn’t avoid was the autocomplete library’s addition
of an extra wrapper element around the text input, which breaks
Bootstrap’s stupidly over-engineered CSS selector, and prevents error
messages from being displayed.

As a result, despite using {% bootstrap_field %}, I still had to include
my own error message output below, which kind of defeats the purpose.

It may be worth investigating whether our autocomplete library has an
option to avoid injecting a wrapper element, but what we’ve got right
now works in the meantime.

When a postcode error is displayed, it changes the height of the form
row, meaning the submit button no longer lined up nicely. I’ve adjusted
the form markup, to enable the button to line up with the other inputs
regardless of whether an error is being displayed or not.

I made `filter.form.pc.errors` into a list, because that’s what the
error handler in `bootstrap_field` expects. (If you use a string instead
of a list, it explodes the string into many single-character error
messages!)

Finally (!) I also `"set_placeholder": False` because we shouldn’t be
using placeholders anywhere.

Part of #31.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[217e9f4371...](https://github.com/treckstar/yolo-octo-hipster/commit/217e9f4371895aad48b323134e0ecc5487bb2913)
#### Wednesday 2022-10-26 13:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [iamcosmin/Allo](https://github.com/iamcosmin/Allo)@[cadbfb6d81...](https://github.com/iamcosmin/Allo/commit/cadbfb6d81dbf351a575105f4aa116920e691fb3)
#### Wednesday 2022-10-26 13:42:09 by iamcosmin

1.3.5 (330)

RO:

De la ultima actualizare a canalelor beta și stabil (din luna martie), multe lucruri s-au petrecut în spatele scenei.

BREAKING:

Utilizatorii care nu au verificat emailul vor trebui să și-l verifice, în caz contrar nu vor mai avea acces la aplicație.
DESIGN

REBRANDING MAJOR: Allo a fost redesenat cu o culoare de accent mov.
Am adaptat majoritatea schimbărilor propuse de Google în Material 3.
Dispozitivele compatibile cu noile caracteristici ale Android 12+ au opțiunea de a activa tema aplicației în funcție de fundalul telefonului. Restul utilizatorilor pot personaliza aplicația cu ajutorul culorilor prestabilite.
Ecranele late au acum bara de navigare pe partea stângă, lăsând mai mult spațiu în partea de jos.
Experiența de utilizare cu o mână este îmbunătățită: bara de navigare este acum mai mare pentru ca utilizatorul să ajungă la conținutul dorit mai ușor. Pe măsură ce conținutul este derulat, bara scade în dimensiune, permițând conținutului să se întindă pe tot ecranul.
Pentru o performanță sporită, am adăugat abilitatea de a dezactiva majoritatea animațiilor. Această opțiune este activată implicit pe Web, dar poate fi dezactivată.
Toate versiunile de Android au acum un splash screen cât aplicația se încarcă. Cei care au Android 12 sau mai mare au parte de un log animat la pornirea aplicației. Utilizatorii web se pot bucura de faptul că nu vor mai fi orbiți de lumina albă atunci când au activat modul întunecat și pornesc în primă instanță aplicația.
Tranzițiile au fost îmbunătățite.
Font nou.
ÎMBUNĂTĂȚIRI MAJORE

Utilizatorii aplicației Web au parte acum de fotografii de profil.
La încărcarea conținutului media, animația indicatorului de progres a fost adăugată.
Lista de mesaje din conversații este mult mai fiabilă: nu mai există probleme majore la animații, mai ales cu privire la reanimarea întregii liste de mesaje atunci când utilizatorul revenea din altă aplicație.
Am îndepărtat abilitatea de a răspunde la mesaje direct din panoul de notificări. Sperăm că această funcție se va reîntoarce într-o versiune viitoare de Allo.
Mărirea imaginilor (pinch to zoom) a fost îmbunătățită substanțial.
Cea mai așteptată îmbunătățire: funcționează notificările! De asemenea, acum se pot dezactiva notificările în conversațiile nedorite.
Am adăugat pagina "Despre": informații despre aplicație, utile când o eroare își face de cap.
Am rezolvat eroarea care afișa un ecran gri, ca urmare a deconectării din aplicație.
Lista de conversații are animații îmbunătățite.
Am implementat o pagină mai prietenoasă pentru modificarea setărilor contului tău Allo.
Folosești o altă adresă de email? Schimbă-ți emailul direct din Allo, fără să-ți pierzi datele.
Aplicația este mai reactivă la schimbări de autentificare.
Ai derulat prea multe mesaje în conversație? Acum există un buton care să deruleze lista cu mesaje până la capăt.
Când răspunzi la un mesaj, experiența este mai rafinată.

EN:

Since the last update to the beta and stable channels (since March), a lot has been happening behind the scenes.

BREAKING:

Users who have not verified their email will have to verify it, otherwise they will no longer have access to the application.
DESIGN

MAJOR REBRANDING: Allo has been redesigned with a purple accent color.
We adapted most of the changes proposed by Google in Material 3.
Devices compatible with the new features of Android 12+ have the option to activate the theme of the application according to the background of the phone. The rest of the users can customize the application with the help of preset colors.
Wide screens now have the navigation bar on the left side, leaving more space at the bottom.
The one-handed user experience is improved: the navigation bar is now larger for the user to reach the desired content more easily. As the content is scrolled, the bar decreases in size, allowing the content to span the entire screen.
For increased performance, we added the ability to disable most animations. This option is enabled by default on the web, but can be disabled.
All Android versions now have a splash screen while the app is loading. Those with Android 12 or higher get an animated log when starting the app. Web users can enjoy the fact that they will no longer be blinded by white light when they have activated the dark mode and start the application in the first instance.
Transitions have been improved.
New font.
MAJOR IMPROVEMENTS

Web App users now have profile photos.
Added progress indicator animation when loading media.
The list of messages in conversations is much more reliable: there are no longer major problems with animations, especially regarding the reanimation of the entire list of messages when the user returns from another application.
Removed the ability to reply to messages directly from the notification panel. Hopefully this feature will return in a future version of Allo.
Pinch to zoom has been substantially improved.
Most awaited improvement: Notifications work! Notifications in unwanted conversations can also now be turned off.
Added "About" page: information about the app, useful when a bug rears its head.
Fixed the bug showing a gray screen after logging out of the app.
Chat list has improved animations.
Implemented a friendlier page for changing your Allo account settings.
Are you using a different email address? Change your email directly from Allo without losing your data.
The application is more reactive to authentication changes.
Did you scroll through too many messages in the conversation? Now there is a button to scroll the list of messages to the end.
When you reply to a message, the experience is more refined.

---
## [lnGoror/tgstation](https://github.com/lnGoror/tgstation)@[a2577296e6...](https://github.com/lnGoror/tgstation/commit/a2577296e62a0f3c335648169a335fe7d3de4bdc)
#### Wednesday 2022-10-26 15:04:46 by RikuTheKiller

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
## [Kubisopplay/tgstation](https://github.com/Kubisopplay/tgstation)@[14c96d05b8...](https://github.com/Kubisopplay/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Wednesday 2022-10-26 15:25:16 by scriptis

TGUI for Techfabs II: The Great Recategorizing (AND ICONS) (AND MECHFABS) (AND AUTOLATHES) (#69990)

    I recategorized EVERY /datum/design/ IN THE GAME to be more UX friendly and I HATE MYSELF FOR IT
    I refactored techfab UI to WORK ANYWHERE for ANY MACHINE THAT USES /datum/design as a SET OF MODULAR COMPONENTS
    I moved a lot of DESIGNS EXCLUSIVE TO THE AUTOLATHE to also work IN PROTOLATHES
    I made MATERIAL ICONS animate between ICON STATES for STACKS
    I PUT ICONS IN ALL OF YOUR FABRICATORS
    I SOMEHOW DID ALL OF THIS WITHOUT LOSING ANY PERFORMANCE
    ALSO SUPPORTS COMPONENT PRINTERS AND MODULE DUPLICATORS

Other garbage:

    Fixed numerous spelling and consistency issues in designs
    Removed Machine Design (<x>) and Computer Design (<x>) from all relevant designs
    All designs are now in title case
    Numerous designs that were formerly autolathe exclusives can now also be printed at a protolathe (but not all); this is mostly just service equipment like drinking glasses and plates and silverware
    Circuits components can no longer be printed at a circuit imprinter (fixes 

    Integrated circuit components printed in the component printer/module printer cost twice as much than from an un upgraded circuit printer #67758)
    Designs that are not sensible for a department to have are no longer accessible to that department (read: medbay printing turbine parts)

Why It's Good For The Game

Improved UX for techfabs, but also for mechfabs and autolathes, and oh look it's pretty!

also I spent like eight hours doing nothing but categorizing /datum/designs and I'll cry if some version of this doesn't get merged eventually
Changelog

cl
refactor: mechfabs, autolathes, component printers, and module duplicators now use techfab tgui components
refactor: every single design is now categorized and subcategorized
refactor: mechfabs and autolathes are now in typescript
qol: techfabs now have icons for what you're about to print
qol: techfab material icons are now animated
qol: techfab material icons now fade when no materials are available
qol: techfab searching no longer lags like hell
qol: techfab searching now searches all recipes instead of just the current category
qol: techfabs now have subcategorization (stock part users rejoice)
qol: techfabs now announce when new recipes are available
qol: numerous other techfab ui tweaks
balance: some designs that were formerly autolathe exclusive can now be printed at some departmental techfabs

---
## [Kubisopplay/tgstation](https://github.com/Kubisopplay/tgstation)@[99b8d6b494...](https://github.com/Kubisopplay/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Wednesday 2022-10-26 15:25:16 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---
## [avar/git](https://github.com/avar/git)@[340ce52343...](https://github.com/avar/git/commit/340ce5234364ee04061901b3001e3ae7d3290741)
#### Wednesday 2022-10-26 15:46:04 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

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

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[b6577dbaac...](https://github.com/GeoB99/reactos/commit/b6577dbaac54b9908f9d93c5b90481583b1c746f)
#### Wednesday 2022-10-26 16:15:32 by George Bișoc

[NTOS:CM] Implement registry checks & recovery

Instead of having the CmCheckRegistry implementation in the kernel, it's better to have it in the Configuration Manager library instead (aka CMLIB). The benefits of having it in the library are the following:

- CmCheckRegistry can be used in FreeLdr to fix the SYSTEM hive
- It can be used on-demand in the kernel
- It can be used for offline registry repair tools
- It makes the underlying CmCheckRegistry implementation code debug-able in user mode

[SDK][CMLIB] Declare HBOOT_TYPE_REGULAR and HBOOT_TYPE_SELF_HEAL boot types

=== DOCUMENTATION REMARKS ===

HBOOT_TYPE_REGULAR and HBOOT_TYPE_SELF_HEAL are boot type values set up by the CMLIB library. HBOOT_TYPE_REGULAR indicates a normal system boot whereas HBOOT_TYPE_SELF_HEAL indicates the system boot is assisted within self healing mode.

Whether the former or the latter value is set it's governed by both the kernel and the bootloader. The bootloader and the kernel negotiate together to determine if any of the registry properties (the hive, the base block, the registry base, etc) are so severed from corruption or not. In extreme cases where
registry healing is possible, the specific base block of the damaged hive will have its flags marked with HBOOT_TYPE_SELF_HEAL. At this point the boot phase procedure is orchestrated since the boot phase no longer goes on the default path but it's assisted, as I have already said above.

[SDK][CMLIB] Implement two names & Unicode names comparison functions

CmpCompareBothCompressedNames and CmpCompareDistinctNames are necessary for lexicographical order validation code when validating the key in question.

[SDK][CMLIB] Implement self-heal registry helpers

This implements cmheal.c file which provides the basic registry self-heal infrastructure needed by the public CmCheckRegistry function. The infrastructure provides a range of various self-heal helpers for the hive, such as subkey, class, values and node healing functions.

[SDK][CMLIB] Implement CmCheckRegistry and validation private helpers

CmCheckRegistry is a function that provides the necessary validation checks for a registry hive. This function usually comes into action when logs have been replayed for example, or when a registry hive internals have changed such as when saving a key, loading a key, etc.

This commit implements the whole Check Registry infrastructure (cmcheck.c) in CMLIB library for ease of usage and wide accessibility across parts of the OS. In addition, two more functions for registry checks are also implemented -- HvValidateHive and HvValidateBin.

CORE-9195
CORE-6762

[NTOS:CM] Use the appropriate flags on functions that will call CmCheckRegistry & add missing CmCheckRegistry calls

In addition to that, in some functions like CmFlushKey, CmSaveKey and CmSaveMergedKeys we must validate the underlying hives as a matter of precaution that everything is alright and we don't fuck all the shit up.

[NTOS:CM] Don't lazy flush the registry during unlocking operation

Whenever ReactOS finishes its operations onto the registry and unlocks it, a lazy flush is invoked to do an eventual flushing of the registry to the backing storage of the system. Except that... lazy flushing never comes into place.

This is because whenever CmpLazyFlush is called that sets up a timer which needs to expire in order to trigger the lazy flusher engine worker. However, registry locking/unlocking is a frequent occurrence, mainly when on desktop. Therefore as a matter of fact, CmpLazyFlush keeps removing and inserting the timer and the lazy flusher will never kick in that way.

Ironically the lazy flusher actually does the flushing when on USETUP installation phase because during text-mode setup installation in ReactOS the frequency of registry operations is actually less so the timer has the opportunity to expire and fire up the flusher.

In addition to that, we must queue a lazy flush when marking cells as dirty because such dirty data has to be flushed down to the media storage of the system. Of course, the real place where lazy flushing operation is done should be in a subset helper like HvMarkDirty that marks parts of a hive as dirty but since we do not have that, we'll be lazy flushing the registry during cells dirty marking instead for now.

CORE-18303

[NTOS:CM][CMLIB] Use HBOOT_TYPE_REGULAR / HBOOT_TYPE_SELF_HEAL indicators for boot type instead of hardcoded values

[NTOS:CM] Disable hard errors when setting up a new size for a hive file / annotate CmpFileSetSize parameters with SAL

During a I/O failure of whatever kind the upper-level driver, namely a FSD, can raise a hard error and a deadlock can occur. We wouldn't want that to happen for particular files like hives or logs so in such cases we must disable hard errors before toying with hives until we're done.

In addition to that, annotate the CmpFileSetSize function's parameters with SAL.

[NTOS:CM] Ignore syncing/flushing requests after registry shutdown

When shutting down the registry of the system we don't want that the registry in question gets poked again, such as flushing the hives or syncing the hives and respective logs for example. The reasoning behind this is very simple, during a complete shutdown the system does final check-ups and stuff until the computer
shuts down.

Any writing operations done to the registry can lead to erratic behaviors. CmShutdownSystem call already invokes a final flushing of all the hives on the backing storage which is more than enough to ensure consistency of the last session configuration. So after that final flushing, mark HvShutdownComplete as TRUE indicating
that any eventual flushing or syncying (in the case where HvSyncHive gets called) request is outright ignored.

---
## [solanum-ircd/solanum](https://github.com/solanum-ircd/solanum)@[06c5309534...](https://github.com/solanum-ircd/solanum/commit/06c53095343c2756208f6398bb7e00fb2cbe46dd)
#### Wednesday 2022-10-26 16:36:22 by Ed Kellett

m_sasl: Remove implicit abort on registration

This doesn't make sense in a world where post-registration SASL is
allowed, and should fix one case of an annoying login desync that's seen
in the real world.

Specifically, when a client sends its final AUTHENTICATE and Atheme
receives it, it sends an SVSLOGIN for that client. If the client sends
us its CAP END *before* we see the SVSLOGIN, the implicit abort will try
to abort the SASL session that's already succeeded.

Atheme interprets this as an instruction to forget about the successful
SASL session; you'll connect unidentified. But it's already sent
SVSLOGIN, which will log the client in ircd-side, causing ircd and
services views to differ until the user authenticates again manually.

I think allowing a SASL session to be aborted when it has already
succeeded is an Atheme bug, and it can still be triggered without this
change. But our behaviour here seems silly anyway.

---
## [GrantRoss-Tenki/Malawi-CQC-CSC-OSU-Work](https://github.com/GrantRoss-Tenki/Malawi-CQC-CSC-OSU-Work)@[91480e481f...](https://github.com/GrantRoss-Tenki/Malawi-CQC-CSC-OSU-Work/commit/91480e481fb3a6fb8d3a09b5640728eeb3a91734)
#### Wednesday 2022-10-26 16:58:17 by GrantRoss-Tenki

Update Jet_flame_breakdown.py

This is not working, god fuckign damnit

---
## [UOX3DevTeam/UOX3](https://github.com/UOX3DevTeam/UOX3)@[df2b44be67...](https://github.com/UOX3DevTeam/UOX3/commit/df2b44be674b9ffebadaf0387ec59e9ff82fc907)
#### Wednesday 2022-10-26 17:02:36 by Xoduz

Mix script fixes and additions

Fixed a bug where adding or removing friends for a pet would not properly inform the involved players
Traps in dungeons will now only trigger for player characters, and will ignore all NPCs
Fixed an issue with archery butte script (js/item/archerybutte.js) where chance of hitting a bullseye was not calculated correctly
Fixed reagent requirements for inscribing Explosion spell (thanks Azzerhoden Razeri!)
Removed redundant VALUE tags from JewlerShopping shoplist (thanks Azzerhoden Razeri!)
Added NPC definitions for savage shaman, savage warrior (male and female) and savage rider in dfndata/npc/savages.dfn.
	Added special AI scripts for savages and savage shamans, to handle their special abilities
	Added tribal paint consumable item (dfndata/items/misc/consumables.dfn)
	Added ability to cook tribal paint via flour and tribal berries (js/skill/cooking/flour.js)
	Added some helper scripts for magic:
		js/magic/helper/check_resist.js (6000)				// Test target's resist versus caster and spell circle
		js/magic/helper/calc_final_spell_damage.js (6001)	// Calculate spell damage from provided base damage
	Added a timer-related script that can be used to keep track of long-term timers (up to 49 days) on objects, and which will remove itself from the object when there are no more active timers left. Currently used for tribal paint:
		js/server/timer/long_term_timers.js (3)

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a8d5c6f8b4...](https://github.com/treckstar/yolo-octo-hipster/commit/a8d5c6f8b4bf450413c7c59bdc9843847cccacc0)
#### Wednesday 2022-10-26 17:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [ANDREIGAMING11/thehen19-is-idiot](https://github.com/ANDREIGAMING11/thehen19-is-idiot)@[d9b0da0585...](https://github.com/ANDREIGAMING11/thehen19-is-idiot/commit/d9b0da05851b0f814bdd85d3a7743313741b4b92)
#### Wednesday 2022-10-26 18:21:18 by The_Andrei

me and mixgamer and part no idiot

me. mixgamer. and partition aren't idiots. pieces of shit (greggfuckman you go dick your asses)

---
## [WinFan3672/OpenLife](https://github.com/WinFan3672/OpenLife)@[a86a4e7c85...](https://github.com/WinFan3672/OpenLife/commit/a86a4e7c854ce03add657d37c2fa8d2f651f29a4)
#### Wednesday 2022-10-26 19:14:32 by WinFan3672

Alpha 13

Alpha 13- The Childbirth Update

1 Introduction
1.1 What This Update Is

Alpha 13 is here! It features a lot of great features that you have been dying to have added, such as:
[-] Spouses

This update is also the first time that you can change the currency from in-game, by editing the main file!
Simply find the currency variable near the top and set it to whatever you would like, such as "$" or "♪"!

It was originally going to have children, but that was canned due to complexity. Children will [obviously] be added, it's just that it's on the back burner for now.

1.2 Alpha 14

Alpha 14 will be the identity update. It will bring things like fame and friends. Be excited.

1.3 Thoughts

This update feels kind of half-arsed, compared to Alpha 12. I think this update is a minor let-down, but then again, I am taking the progress of the game for granted here. This update is smaller and took longer to make, but that's fine. I just need to remind myself that.

2 Spouses
2.1 Spouse

You can have a spouse and:
[-] Marry them
[-] Break up with them
Sadly, since it's an alpha, it will always be a female spouse and you will always be a male character.

3 Die()
3.1 What Is It
The die() function is a universal death screen. It has 5 causes at the moment, and not all of them in use [Suicide, heart attack, health issues, cancer and old age].

3.2 Menu
The menu will be the front page of the OpenLife Times, a newspaper in the OpenLife universe. You will be able to read the article, and once you've read it you can:
[-] Exit the game
[-] Return to the main menu
[-] Respawn
   [-] That's right, escape death! It only works up to 130 years old.

4 Job Additions
4.1 Teen Jobs

You can now have a job as a teen!
The jobs are:
[-] Pizza Delivery Person
[-] Newspaper Delivery Person
[-] Lawn Mower
[-] Car Washer

4.2 Part-Time Jobs

You can now have a job alongside your job :o
You work 10 hours per week, so 520 hours. 
The jobs are:
[-] Receptionist
[-] Mall Santa

5 School Gang
5.1 Gang
This is a half-arsed update to school gangs. It adds:
[-] Gang wars
[-] Enemy gangs

The enemy gang has a placeholder name, sadly.

6 General Additions
6.1 Currency Changes
The variable `currency` determines what symbol is rendered when you see the `£` symbol. You can edit the main file and turn it into dollars if you want.
6.2 Custom Surnames
Yep. Make a file called `surname.dat` and every line is a different valid surname. 
6.3 SGCU
SGCU [Save Game Conversion Utility] can convert an Alpha 12 save file into an Alpha 13 one. One day, it will support the original OLL files.
6.4 Options Menu
The options menu allows you to change themes and enable Auto Deposit for the first time ever. No more editing save files. Ok, technically you still will, since the changes get reset when you relaunch the game/exit to the main menu. But still, it's a step in the right direction.

7 Bug Fixes
[-] Fixed a bug where 2 `div()` elements are displayed when rendering the `Feature Not In Current Build` message on the main menu.

8 Known Bugs
[-] Save game breaks a few things

Next Update: Identity Update
Build Date: 26 Oct 2022
Publish Date: 26 Oct 2022

---
## [Fauli1221/unicmodpack4meme5](https://github.com/Fauli1221/unicmodpack4meme5)@[92a2ee49b5...](https://github.com/Fauli1221/unicmodpack4meme5/commit/92a2ee49b5e3a26f3c1dd8c274974931028a8603)
#### Wednesday 2022-10-26 19:21:31 by Fauli1221

fuck you curseforge but I never agreed to your tos

---
## [2-legit/Vape2LegitForRoblox](https://github.com/2-legit/Vape2LegitForRoblox)@[1016115561...](https://github.com/2-legit/Vape2LegitForRoblox/commit/101611556139db26fb29125865c965fbb4c6573f)
#### Wednesday 2022-10-26 19:24:37 by 2_legit

removed vape private + skidded bed tp

fuck you chickynoid

---
## [philipl/mpv](https://github.com/philipl/mpv)@[6f7506b660...](https://github.com/philipl/mpv/commit/6f7506b660b83a44535eceb12a8b9c4de6c0eb36)
#### Wednesday 2022-10-26 19:48:41 by Philip Langdale

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
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[062350b6b8...](https://github.com/GeoB99/reactos/commit/062350b6b8db552dea6d49e31203e12100f28aca)
#### Wednesday 2022-10-26 19:50:25 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

---
## [WagicProject/wagic](https://github.com/WagicProject/wagic)@[5c691afe33...](https://github.com/WagicProject/wagic/commit/5c691afe33f6521feeaa57e9deea9089ce36eb49)
#### Wednesday 2022-10-26 20:41:15 by Eduardo MG

Fixes in primitives

Mire in Misery
Mask of Memory
Smiting Helix
Ring of Renewal
Pirate's Cutlass
Trash for Treasure
Sixth Sense
Life's Legacy
Kaseto, Orochi Archmage
Gristle Grinner
Tezzeret, Artifice Master
Commander's Sphere
Journey for the Elixir
Azra Bladeseeker
Indulgent Tormentor
Sidisi, Brood Tyrant
Martyr's Bond
Gruesome Scourger
Pull from Tomorrow
Conqueror's Flail
Trespasser's Curse
Tourach, Dread Cantor
Jerren, Corrupted Bishop
Feral Roar
Release to the Wind
Taborax, Hope's Demise
Magmatic Sinkhole
rage of purphoros
Farbog Boneflinger
Ruin Grinder

---
## [Xiang-Gu/cockroach](https://github.com/Xiang-Gu/cockroach)@[f50670b344...](https://github.com/Xiang-Gu/cockroach/commit/f50670b3440e91bec05aebc1bc425e4dd465583f)
#### Wednesday 2022-10-26 20:58:21 by Tobias Grieger

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
## [katafrakt/hanami-controller](https://github.com/katafrakt/hanami-controller)@[9c123ecdd5...](https://github.com/katafrakt/hanami-controller/commit/9c123ecdd5152c942fa3fb6b7b5359a569943531)
#### Wednesday 2022-10-26 20:58:51 by Tim Riley

Reenable MIME specs and check both `Accept` and `Content-Type` headers checks via `accept` (#396)

## Background

The way our `accept` macro has worked has taken over time has taken a few different shapes.

- In 1.3.x it worked on the `Accept` header only ([see here for code](https://github.com/hanami/controller/blob/2496ac797237d7320b96048a3c9e3fbebb00532c/lib/hanami/action/mime.rb#L168-L172)) and returned a 406 response for non-matching types.
- However, 1.3.x _also_ had a `content_type` macro that operated on the `Content-Type` header ([see code](https://github.com/hanami/controller/blob/2496ac797237d7320b96048a3c9e3fbebb00532c/lib/hanami/action/mime.rb#L198-L204)) and returned a 415 response for non-matching types.
- In the very earliest phase of 2.0 development, when @jodosha was completely overhauling the shape of hanami-controller, we removed the `content_type` macro and left the `accept` macro only (in [this commit](https://github.com/hanami/controller/commit/85e927a694998e5ebfcbad216d7bdec4109b6806), which is rather large). The `accept` macro and its behaviour were left largely unchanged at this point.
- Then not too long after, we changed the `accept` macro to no longer operate on the `Accept` header and instead look at `Content-Type` only, and return a 415 response for all non-matching types (see [this PR](https://github.com/hanami/controller/pull/265), addressing [this issue](https://github.com/hanami/controller/issues/257))

## Shortcomings 

I ran into some trouble with this early 2.0-phase implementation, because it meant that if you put `accept :json` into a base action class (e.g. for every action class within an API service to inherit from), then it would reject _any_ request without a `Content-Type: application/json` header.

Requiring a `Content-Type` header like this would make sense for POST, PUT, PATCH requests, that is, any kind of request that contains a request body and needs to describe its content type.

However, `GET` and other requests without bodies are likely _not_ to have `Content-Type` headers. These requests would more likely have an `Accept` header only.

## Changes

I believe that when an action contains `accept :json`, then it should be able to successfully handle a request with only an `Accept: application/json` header, and no `Content-Type`. It should also handle weighted `Accept` headers too, like `text/html, application/xhtml+xml, application/xml;q=0.9`.

This PR changes the way we enforce the accepted formats configured with `accept`. It:

- Checks the `Accept` header first. If it is present, it will check if any any of the header's MIME types are acceptable per the configured `accepted_formats`. If none are acceptable, then the request will be a 406 error.
- If the `Accept` is not present, it then checks `Content-Type`. If this header is present, but checks to see if the Content-Type MIME type is accepted able per the configured `accepted_formats`. If it is not acceptable, then the request will be a 415 error.
  - If the `Content-Type` header is not present, then it will substitute this with the MIME type for the `default_request_format`, if configured.
- Lastly, if there is no `Accept`, no `Content-Type`, no `default_request_format`, then the request is accepted regardless, with the idea here being that the client has no care or opinion about the format they want, and our Action class can return whatever content it likes in its response.

I believe this strikes a balance that should satisfy the spread of real-world requests. It captures the spirit of _both_ the original `accept` and `content_type` macros while ensuring we still keep the slimmer API surface area of the `accept` macro only.

Certainly if this were implemented earlier, I could have avoided hacking in a workaround inside the app in which I discovered this issue.

---
## [sjp38/linux](https://github.com/sjp38/linux)@[4ccf34f283...](https://github.com/sjp38/linux/commit/4ccf34f28311b0f5e78e6e1015df16140a4d10ed)
#### Wednesday 2022-10-26 23:19:28 by Johannes Weiner

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
## [truckeerobotics/FtcRobotController-2022](https://github.com/truckeerobotics/FtcRobotController-2022)@[c804fa7bd0...](https://github.com/truckeerobotics/FtcRobotController-2022/commit/c804fa7bd047ea52fb6d090aa5573cb416e9a585)
#### Wednesday 2022-10-26 23:53:02 by tysuh66

encoder do worky now and jake is still very stupid also he cant spell difference, also kieran was here a messed up workflow and should never come here again. just kidding. jake cant spell the following: LITERALLY EVERYTHING IN THE ENGLISH DICTIONARY. also im killing time because alex is pushing 4000 files. jake you left your charger here and zach will bring it to you in the morning in 1st period. Alex's code is still parsing or whatever the hell. heres my final essay from honors 10 last year:

A common definition of cruelty is causing pain or suffering. Cruelty is expressed throughout the book Snow Falling on Cedars written by David Gutterson. Cedars takes place after the bombing of pearl harbor in WWII. Japanese on the west coast were sent away to internment camps placed around the west-midwest United States. Two of the main characters, Kabuo and Hatsue, meet in an internment camp as kids and Kabuo left the camp to serve in the army to fight against the Japanese Army. In Cedars, Cruelty plays a large role in the story of Kabuo Miyamoto’s trial for the death of Carl Heine with his father's relation with Heines's father, with his time in the war.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  To start, Kabuo and Carl’s fathers had some relations back when they were both young and the Heine’s had made plans to sell 7 acres of their land to Kazuo Miyamoto, Kabuo’s father. Originally, Kazuo was paying monthly to the Heine’s to slowly build up to getting that land for Kabuo, but when the Japanese were interned they refused to take payments from the Miyamoto’s making it so that they won’t have the land when they come out of internment. It is unclear why they didn't want payment from them but it could be a fact that they were Japanese and the Japanese army had just bombed a naval base that belonged to the United States. Another reason is that the Heine’s sold their land to another person willing to pay nearly double the amount that they were paying monthly for the land. Kabuo didn't like that and when he came home from the war he had confronted the Heine’s and Kabuo left empty-handed from that encounter with nothing leaving Kabuo devastated and the Heine’s were happy about the decision they had made.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  Secondly, Gutterson shows how Kabuo enlisted in the army while he was inside an internment camp to help the Americans defeat the Japanese. The trial supposes that since Kabuo was in the army he is trained to kill people and there was a fishing incident that was blamed on Kabuo since the evidence showed that there might have been a murder. The sheriff throws the blame on him because he has these abilities and knows how to use them. Another reason is that his father also taught him the art of kendo, a Japanese fighting technique that is used in most combat situations. The town coroner, Horace, finds what he seems to think is a kendo strike on the side of Carl Heine's body. Kabuo is immediately to blame for the incident since he had learned kendo as a kid and that he was the last person to be known with Carl Heine. The story later shows that Ishmael Chambers brings forth evidence that Heine that he could have been thrown overboard by the wakes of the passing cargo ship, S.S. Corona.

                                                                                                                                                                                                        To close, Kabuo is a subject of cruelty and he is being stereotyped several times during Cedars. People are still subject to cruelty today, for example, the tragedy of the death of George Floyd. He was thrown to the ground and an officer happily placed his knee onto his neck and he did nothing wrong. Stereotyping and cruelty could be fixed with a simple full story of where all the different religions come from so that people don't criticize with only half of the story.

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  ITS FINALLY DONE YAY

---

