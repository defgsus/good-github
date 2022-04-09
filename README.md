## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-08](docs/good-messages/2022/2022-04-08.md)


1,839,840 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,839,840 were push events containing 2,974,490 commit messages that amount to 206,162,678 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 43 messages:


## [stemnic/binutils-gdb](https://github.com/stemnic/binutils-gdb)@[86d77f6a5b...](https://github.com/stemnic/binutils-gdb/commit/86d77f6a5be904f13c633f10bdf77ff3dd69db94)
#### Friday 2022-04-08 00:00:16 by Andrew Burgess

gdb: don't try to use readline before it's initialized

While working on a different patch, I triggered an assertion from the
initialize_current_architecture code, specifically from one of
the *_gdbarch_init functions in a *-tdep.c file.  This exposes a
couple of issues with GDB.

This is easy enough to reproduce by adding 'gdb_assert (false)' into a
suitable function.  For example, I added a line into i386_gdbarch_init
and can see the following issue.

I start GDB and immediately hit the assert, the output is as you'd
expect, except for the very last line:

  $ ./gdb/gdb --data-directory ./gdb/data-directory/
  ../../src.dev-1/gdb/i386-tdep.c:8455: internal-error: i386_gdbarch_init: Assertion `false' failed.
  A problem internal to GDB has been detected,
  further debugging may prove unreliable.
  ----- Backtrace -----
  ... snip ...
  ---------------------
  ../../src.dev-1/gdb/i386-tdep.c:8455: internal-error: i386_gdbarch_init: Assertion `false' failed.
  A problem internal to GDB has been detected,
  further debugging may prove unreliable.
  Quit this debugging session? (y or n) ../../src.dev-1/gdb/ser-event.c:212:16: runtime error: member access within null pointer of type 'struct serial'

Something goes wrong when we try to query the user.  Note, I
configured GDB with --enable-ubsan, I suspect that without this the
above "error" would actually just be a crash.

The backtrace from ser-event.c:212 looks like this:

  (gdb) bt 10
  #0  serial_event_clear (event=0x675c020) at ../../src/gdb/ser-event.c:212
  #1  0x0000000000769456 in invoke_async_signal_handlers () at ../../src/gdb/async-event.c:211
  #2  0x000000000295049b in gdb_do_one_event () at ../../src/gdbsupport/event-loop.cc:194
  #3  0x0000000001f015f8 in gdb_readline_wrapper (
      prompt=0x67135c0 "../../src/gdb/i386-tdep.c:8455: internal-error: i386_gdbarch_init: Assertion `false' failed.\nA problem internal to GDB has been detected,\nfurther debugging may prove unreliable.\nQuit this debugg"...)
      at ../../src/gdb/top.c:1141
  #4  0x0000000002118b64 in defaulted_query(const char *, char, typedef __va_list_tag __va_list_tag *) (
      ctlstr=0x2e4eb68 "%s\nQuit this debugging session? ", defchar=0 '\000', args=0x7fffffffa6e0)
      at ../../src/gdb/utils.c:934
  #5  0x0000000002118f72 in query (ctlstr=0x2e4eb68 "%s\nQuit this debugging session? ")
      at ../../src/gdb/utils.c:1026
  #6  0x00000000021170f6 in internal_vproblem(internal_problem *, const char *, int, const char *, typedef __va_list_tag __va_list_tag *) (problem=0x6107bc0 <internal_error_problem>, file=0x2b976c8 "../../src/gdb/i386-tdep.c",
      line=8455, fmt=0x2b96d7f "%s: Assertion `%s' failed.", ap=0x7fffffffa8e8) at ../../src/gdb/utils.c:417
  #7  0x00000000021175a0 in internal_verror (file=0x2b976c8 "../../src/gdb/i386-tdep.c", line=8455,
      fmt=0x2b96d7f "%s: Assertion `%s' failed.", ap=0x7fffffffa8e8) at ../../src/gdb/utils.c:485
  #8  0x00000000029503b3 in internal_error (file=0x2b976c8 "../../src/gdb/i386-tdep.c", line=8455,
      fmt=0x2b96d7f "%s: Assertion `%s' failed.") at ../../src/gdbsupport/errors.cc:55
  #9  0x000000000122d5b6 in i386_gdbarch_init (info=..., arches=0x0) at ../../src/gdb/i386-tdep.c:8455
  (More stack frames follow...)

It turns out that the problem is that the async event handler
mechanism has been invoked, but this has not yet been initialized.

If we look at gdb_init (in gdb/top.c) we can indeed see the call to
gdb_init_signals is after the call to initialize_current_architecture.

If I reorder the calls, moving gdb_init_signals earlier, then the
initial error is resolved, however, things are still broken.  I now
see the same "Quit this debugging session? (y or n)" prompt, but when
I provide an answer and press return GDB immediately crashes.

So what's going on now?  The next problem is that the call_readline
field within the current_ui structure is not initialized, and this
callback is invoked to process the reply I entered.

The problem is that call_readline is setup as a result of calling
set_top_level_interpreter, which is called from captured_main_1.
Unfortunately, set_top_level_interpreter is called after gdb_init is
called.

I wondered how to solve this problem for a while, however, I don't
know if there's an easy "just reorder some lines" solution here.
Looking through captured_main_1 there seems to be a bunch of
dependencies between printing various things, parsing config files,
and setting up the interpreter.  I'm sure there is a solution hiding
in there somewhere.... I'm just not sure I want to spend any longer
looking for it.

So.

I propose a simpler solution, more of a hack/work-around.  In utils.c
we already have a function filtered_printing_initialized, this is
checked in a few places within internal_vproblem.  In some of these
cases the call gates whether or not GDB will query the user.

My proposal is to add a new readline_initialized function, which
checks if the current_ui has had readline initialized yet.  If this is
not the case then we should not attempt to query the user.

After this change GDB prints the error message, the backtrace, and
then aborts (including dumping core).  This actually seems pretty sane
as, if GDB has not yet made it through the initialization then it
doesn't make much sense to allow the user to say "no, I don't want to
quit the debug session" (I think).

---
## [ThePainkiller/Skyrat-tg](https://github.com/ThePainkiller/Skyrat-tg)@[b995fbe31b...](https://github.com/ThePainkiller/Skyrat-tg/commit/b995fbe31b87402d3da2f8e98cec1f5659e52a47)
#### Friday 2022-04-08 00:45:35 by Zonespace

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
## [ParadiseSS13/Paradise](https://github.com/ParadiseSS13/Paradise)@[6082c95eb3...](https://github.com/ParadiseSS13/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Friday 2022-04-08 01:03:56 by LightFire53

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
## [repinger/sm8150_bahamut_kernel](https://github.com/repinger/sm8150_bahamut_kernel)@[0a95cf6dff...](https://github.com/repinger/sm8150_bahamut_kernel/commit/0a95cf6dffd5bdaed18bd36777e813c70580d646)
#### Friday 2022-04-08 01:26:23 by Peter Zijlstra

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
## [Johnyknowhow/atlas](https://github.com/Johnyknowhow/atlas)@[84c10997d5...](https://github.com/Johnyknowhow/atlas/commit/84c10997d59c3eabea7e30d51ace76b3e511510e)
#### Friday 2022-04-08 02:00:26 by Johnyknowhow

Various duplicate removals and description edits

Removed duplicates from various artworks south of the northwest Turkish flag, edited a few descriptions to combine information/increase clarity/make it more understandable to outsiders

RIT logo
(-)twua6s - duplicate, short desc
(e)twu980 - remaining, merged into, combined descriptions

small chilean flag:
(-)txdqoq - duplicate, no desc
(-)txd2js - duplicate, outdated desc
(-)tx8o7v - duplicate, joke desc
(-)txa6ya - duplicate, troll desc
txffm2 - remaining entry

belgian flag Tintin
(e)000056 refined shape, updated title and description

canadian flag
(-)txapxq - dupe, simple entry
(-)twx0nb - dupe, doesn't mention canada, only the battle for it
(-)twp9xq - dupe, good description but twmbw6 seems better (my opinion)
(e)twmbw6 - remaining entry; good description, changed subreddit to /r/placecanada

eldenring potfriend
(-)twrfvo - dupe, good description but lacking context
(e)txysr4 - remaining entry; merged description in and added objective explanation of *what* potfriend is, edited for brevity

large chile flag/art area
(-)txaka4 - dupe, super short desc
(-)txbdl6 - dupe, not descriptive about the art
twn3qv - remaining entry, perfect description

---
## [anyaevostinar/minecraft-sheep-evolution](https://github.com/anyaevostinar/minecraft-sheep-evolution)@[bd68e49711...](https://github.com/anyaevostinar/minecraft-sheep-evolution/commit/bd68e497114dcc0f05fd27cdada4586141c98d50)
#### Friday 2022-04-08 03:12:18 by kenyonnystrom

Chat-related update

A new file called ChatExt can now be invoked to send a message to the in-game chat, which can be useful for debugging but also the player experience. For example, when sheep die due to causes that we have customized, a death message appears in chat (this might get annoying, if so just comment out the line indicated in the onDeath method of EvolvingSheepEntity). This also involved additions of death messages and names to the lang file.

---
## [Grebbinz/Encrypter-Decrypter](https://github.com/Grebbinz/Encrypter-Decrypter)@[85afab1dde...](https://github.com/Grebbinz/Encrypter-Decrypter/commit/85afab1dde9d5715e2d9cd249ca2cf8db4361cc1)
#### Friday 2022-04-08 03:16:14 by Grebbinz

ON GOD IT WORKS

I FIXED ALL THE DLL SHIT ASS AMONGUS SKELD PROLLEMS

---
## [jupyterkat/tgstation](https://github.com/jupyterkat/tgstation)@[351afe260b...](https://github.com/jupyterkat/tgstation/commit/351afe260b42764641a07385df5f7e24b840f631)
#### Friday 2022-04-08 03:19:56 by san7890

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
## [Fargowilta/FargowiltasSouls](https://github.com/Fargowilta/FargowiltasSouls)@[e33996b247...](https://github.com/Fargowilta/FargowiltasSouls/commit/e33996b247bf8df882bc3eeb66390366960f43ab)
#### Friday 2022-04-08 03:21:31 by terrynmuse

wandering eye fish
 spawns with a gang of wandering eyes
 dashes, inflicts curse of moon, has sickle trail p2
 drops frog leg and puffer balloon, 10% chance each
zombie merman
 spawns with a horde of zombies
 at 50%, can jump through blocks and lands with a wave of blood spikes (test it hurts in mp)
 drops frog leg and puffer balloon, 10% chance each
fixed rock golem sometimes literally just sitting there doing nothing until taken below 50%
oceanic maul now specifically says +-5 max life
reduced number of gibs produced by landslide, increased damage to compensate, should be same balance

---
## [Stevanus-Christian/terminal](https://github.com/Stevanus-Christian/terminal)@[446f280757...](https://github.com/Stevanus-Christian/terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Friday 2022-04-08 03:43:39 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [maxieds/FlowersForMama2022](https://github.com/maxieds/FlowersForMama2022)@[86ffdee5fa...](https://github.com/maxieds/FlowersForMama2022/commit/86ffdee5faddfa74faf2c829bc16cc32c0e1663e)
#### Friday 2022-04-08 03:52:08 by Maxie D. Schmidt

Yeah, my better looking sister...

Brandye to me after her girlfriend Erica came onto me following a mandatory breast lump exam: "You just think you're better than every one else because your boobs are bigger than MINE." [Indeed.]

---
## [acestream/ace-network-docs](https://github.com/acestream/ace-network-docs)@[de06c4b652...](https://github.com/acestream/ace-network-docs/commit/de06c4b652e03a4c5f0f03f22bbf8233e180dd84)
#### Friday 2022-04-08 04:25:19 by Anton

Update token sale dates and roadmap because of war

Russian warship go fuck yourself

---
## [Shamswaggirl/ersilia](https://github.com/Shamswaggirl/ersilia)@[32d7f3c151...](https://github.com/Shamswaggirl/ersilia/commit/32d7f3c151d583a49f2c4c5555ba45289de2b57a)
#### Friday 2022-04-08 05:19:25 by Shanmugapriya D

<README_Shanmugapriya.md>

Hello @GemmaTuron,
1)I have made a one-page blog post on "Strategic plan 2021-2023" (https://docs.google.com/document/d/1iN4uweFNAvHO4Dfl1UtAt4Qc_eDzWqVA8qvFXMw0Swk/edit?usp=sharing)

Strategic plan 2021-2023
The Ersilia Open Source Initiative (EOSI) is a UK-registered charity founded in November 2020 by three early career scientists who share the belief that scientific development in Low and Lower Middle Income Countries is a major player in their way to progress.Our inspiration to start EOSI is well summarised in this extract from the WHO world health report 2013:The results of some research studies are widely applicable, but many questions about universal health coverage require local answers. All countries therefore need to be producers of research as well as consumers of it.
EOSI mission is to strengthen the research capacity against infectious and neglected diseases by democratising the access to machine learning tools.Our vision is that of a world with egalitarian research capacity and access to healthcare. Our aim is to provision the resources which traits openness, empowerment, inclusion of diversity, integrity and accountability. 

Goal 1: Facilitate the access of AI/ML technologies to all scientists
To promote the re-usability of already generated resources and popularise the use of AI/ML in experimental laboratories, we aim to gather in a single platform a plethora of AI/ML models for drug discovery in neglected diseases. This includes addition of 75 literature-based models per year to the hub, addition of 50 in-house trained models from key dataset per year to the hub, pre-computation and storage of frequent queries. 

Goal 2: Achieve sustainability for the Ersilia model hub
The Ersilia Model Hub will grow to become the central asset of the charity, a platform that will disseminate research results, where scientists can report on the models they have used and contribute to their improvement, as well as a resource that stimulates scientific collaboration and solidarity. This action plan includes engaging relevant open-source stakeholders, increasing revenue from open-source grants, launching periodic crowd-sourcing campaigns and establishing a network of grant making foundations.

Goal 3: Implement AI/ML routines in LMIC laboratories
We will engage in partnerships with LMIC institutions to develop tailored AI/ML tools and provide personalised support for their implementation. This involves establishing partnerships with key researchers in the field, offering AI/ML introductory training lessons for university students and obtain support and funding to establish computation stations.

Goal 4: Increase acceptance and popularity of computational research
We aim to find the middle ground, increasing the adoption of AI/ML thanks to use-case examples, strict open science guidelines and full documentation of each model, including training set, possible biases, application domain etc. We take into account experimental validation of AI/ML models, radical open science approach to all EOSI’s project, publish the results in peer-reviewed journals and participating in international conferences and seminars.

Goal 5: Improve EOSI governance and organogram
To fulfil the above-mentioned objectives, it is of foremost importance as a recently born organisation that we grow, increasing our operational capacity and involving the community, including stakeholders, beneficiaries and supporters in our activities and decision-making processes, to become an inclusive organisation that answers the real needs of those whom it serves. This is possible when we consolidate the board of trustees, create a community of software developers, engage students in short-term projects, scale the operational capacity and build a strong diversity and inclusion work environment.

2)Do refer to my slide about the EOSI mission and vision 
(https://www.canva.com/design/DAEbEBjwGqw/kOZbPv55ejaA-GEc-RGmnA/view?utm_content=DAEbEBjwGqw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---
## [Kylerace/tgstation](https://github.com/Kylerace/tgstation)@[4051ad647e...](https://github.com/Kylerace/tgstation/commit/4051ad647e3e94ea5c722cee18cecf350270ab6f)
#### Friday 2022-04-08 05:34:44 by LemonInTheDark

Space drifting fixes and cleanup (#64915)

* Fixes infi pushing off something in space

Right now you can just push "into" a dense object forever, and depending
on your move rate, just kinda glide

We can fix that by checking if we're trying to push "off" something
we're moving towards

* Makes pushing off something shift it instantly

Currently if you kick off something in space it waits the delay of the
move to start drifting. Looks dumb, let's not

* Updates backup movement to properly account for directional windows. GOD I HATE DIRECTIONAL DENSITY SHOOOOOT MEEEEEEEEEEEEEEEEEEE

* Uses range instead of orange so standing on the same tile as a directional counts properly, rather then suddenly entering a drift state. I hate it here

* Ensures all args are named, updates implementations of the proc with the new arg

---
## [Kylerace/tgstation](https://github.com/Kylerace/tgstation)@[3bd5a2d8df...](https://github.com/Kylerace/tgstation/commit/3bd5a2d8df49213708540f1c0ffe0873b5d2e233)
#### Friday 2022-04-08 05:34:44 by Wallem

Makes Ants glow, puts a minimum on ant screaming and shoe permeability, and other ant-related things. (#64786)

I found out how emissives work and my first thought was "damn ants should glow that would look sick"
So now they do.

Also, having less than 5u ants in your body will make you not scream, so 0.0001u ants will no longer have that tiny chance of making someone scream for their life.

If an ant pile has a max damage value less than 1, then they won't be able to bite through your shoes. This is the same threshold as the second tier ant icon.

Makes the giant ant a hostile mob with the neutral faction, meaning they will attack anything not in the neutral faction.

---
## [smxi/inxi](https://github.com/smxi/inxi)@[8e0b7b5ccf...](https://github.com/smxi/inxi/commit/8e0b7b5ccf9673eb0a078a3b1edadcd850936d82)
#### Friday 2022-04-08 05:49:49 by Harald Hope

Bug fix, it's a bad edid data bug, rare, but when it trips, kills inxi execution
dead right before -G/Graphics shows. Also some nice fixes and enhancements.

--------------------------------------------------------------------------------
KNOWN ISSUES:

1. Possible case of Gnome Wayland failing to set any gnome environmental
variables, making wayland detection not possible. This was in anonymous dataset
inxi-proBook4540s dataset. Person never appeared in real life so can't follow up
on it. This cascaded down to other failures in display detection, and desktop
detection, though in theory much of the data needed was present. I expect
similar issues may appear with kde wayland. This is/was probably a configuration
or build error I believe, though not enough data yet.

It appears that sudo start disabled the display environmental variable
detections, which is unfortunate, and the fallback loginctl tests do not appear
to work for unknown reasons. I've confirmed this on Fedora stock Gnome as well.

--------------------------------------------------------------------------------
BUGS:

1. Forgot to test that return from get_display_manager is array ref, this
impacts only a tiny handful of distros probably, TinyCore was one, but it is
a fatal failure, so fixed it. Also fixed in 3.3.14 inxi branch. Never trips in
console, only on tiny linux where no dm is used at all, I think Xvesa might be
the only case this would have tripped.

2. EDID errors and warnings had several bugs, errors a fatal critical bug which
made execution stop. Had forgotten to pass the $edid hash reference to the error
constructor. Also had used wrong hash key in output so would never have shown.

--------------------------------------------------------------------------------
FIXES:

1. Corrected ram device indentation levels.

2. Made memory width more clear with: width: data: total: which more
accurately reflects the source data. Also in cases where no data or total
values, only show width: N/A, not the data: total: sub items.

3. Made edid errors/warnings output to numbered list of warnings/errors instead
of using join() to made one long list. Much more consistent that way. This fixes
issue #266 - thanks SheridanOAI for finding this bug.

4. In --slots, -x wasn't loading the bus ID so it showed N/A, unnecessary data
collection granularity, removed.

5. For Display, if no X or gpu driver, show: driver: N/A. Showed driver: gpu:
N/A before.

6. For Display, remove filters for Xwayland tests, we always want to see
xwayland data if it's installed. This was actually an error to not show it since
display_server_data already had the correct tests to not redo Xorg data if found
previously, which would be glxinfo based data. This is a partial fix also for
Known Issue 1, at least we'll see Xwayland is present even if Wayland detections
failed for unkonwn reasons.

7. Added some ram value dmi filters, found some that had 'none' or 'unknown'.

8. Show display protocol out of display!! Also handles most common root use
cases as well, so in most cases, if the initial protocol detections failed, this
will result in a decent attempt, though if root it is less reliable. sudo or
regular user will be fine since looks for not tty/pts TTY type and username.

This should also help narrow down Known Issue 1 failures, though there are more
cases to be dealt with, but can only chip away since not enough data.

9. Made info: item in slots more robust, and able to handle more diverse
scenarios.

10. Added alternate syntaxes for dmidecode permissions errors.

--------------------------------------------------------------------------------
ENHANCEMENTS:

1. Added brzdm clogin mlogind xlogin display managers. Not verified. Version for
brzdm is probably like slim since brzdm is a fork of slim.

2. Added voltages to ram module report, that had been left out. Note that it's
common for voltages to be either 'unknown' or not present at all. This is as
close as inxi can get to handling issue #265 since there is no other source for
the requested data type (show DDR3L, low voltage DDR3, which doesn't exist as a
type in dmidecode).

3. Added voltages to --slots report, --slots -xx. Only shows if present.

4. Added for --slots -a for Linux, if detected, the PCI children of the bus ID
of the slot. This is recursive, so supports as many levels as are present,
though it would be rare for there to be more than one level of children.

--------------------------------------------------------------------------------
CHANGES:

1. In -m ram report, moved ram type before size/speed/voltage, that makes more
sense.

2. Also in -m ram report, make type: the default value (was an -x options
before), which contains the no module found messages etc, making the order:
  Device-1: DIMM 0 type: no module installed
  Device-2: DIMM 1 type: DDR4 size: 16 GiB speed: 2400 MT/s

This puts all the speed/size/voltage data together, and stops putting the no
module found message in speed, which never made any sense.

2. In -m, changed width data to more clearly reflect the data source:
      width (bits):
        data: 64
        total: 72

--------------------------------------------------------------------------------
DOCUMENTATION:

1. Man page, added a TABLE OF CONTENTS section which lists all the primary
sections. Can help since the man page has gotten so darned long and man doesn't
as far as I know support clickable internal links, sadly.

2. For -m, updated for revised output syntax and -x levels. Note that the help
and man actually had the type: as default for -m, not -mx, but for some reason,
the code had it wrong. Oops.

3. For -m, fixed some legacy output syntax in the examples.

--------------------------------------------------------------------------------
CODE:

1. Some refactors of slots, ram, as well as a bit more refactoring of edid stuff
for graphics.

2. Added $ENV{'DISPLAY'} to debugger data collector, no idea why that was left
out.

---
## [Kathurjan/EventManager](https://github.com/Kathurjan/EventManager)@[03e553586e...](https://github.com/Kathurjan/EventManager/commit/03e553586ec9aaba89510291f3bcfcba25b90dae)
#### Friday 2022-04-08 06:18:26 by DoncusSpelunkus

Update v.brainmelt

Schizo posting in github commit because i just spent 14! HOURS! STRAIGHT TRYING TO MAKE THIS FOOKING FEATURE WORK AND IT STILL DOESNT

its close 1 or 2 bugs and alittle tweaking and it should be fine BUT FUCK MY LIFE I WAS ALREADY SLEEP DEPRIVED

---
## [sanjain-progress/chef](https://github.com/sanjain-progress/chef)@[9c615241b5...](https://github.com/sanjain-progress/chef/commit/9c615241b52a3947549bc17ab85e256dc47be7ab)
#### Friday 2022-04-08 06:36:22 by Lamont Granquist

Disable knife gem install in kitchen tests

This causes horrible issues.

We are installing knife in a TK virt and can't really build it and
install it as a test (hacking up appbundler to do this would largely
invalidate the test since we wouldn't be testing customer behavior)
and as such it needs to be installed from rubygems.  That means
installing knife-17, which pulls down chef-17 which currently has
a dep on diff-lcs 1.3.x which conflicts with 1.5.x which throws
the errors around the binstubs conflicting (which may or may not be
a rubygems bug, I investigated that a bit and couldn't determine
why that is happening since the 3rd line has the magic rubygems
comment).  We can't just use "--force" as an option since that'll
ignore deps and stuff as well which is precisely the kinds of things
that we're trying to catch.  So for now this test is more pain
that it is worth.

Signed-off-by: Lamont Granquist <lamont@scriptkiddie.org>

---
## [lgritz/oiio](https://github.com/lgritz/oiio)@[ed616c7a0f...](https://github.com/lgritz/oiio/commit/ed616c7a0f6ae365a1b70cca4ddedb3f385dbb9b)
#### Friday 2022-04-08 06:57:10 by Larry Gritz

Lay groundwork for unity builds

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
## [unishift/pytorch](https://github.com/unishift/pytorch)@[1b7d7d9327...](https://github.com/unishift/pytorch/commit/1b7d7d93276eb37c009905ef87ea9c2a7c95481e)
#### Friday 2022-04-08 07:35:45 by Brian Hirsh

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[4d496b0f74...](https://github.com/treckstar/yolo-octo-hipster/commit/4d496b0f74332520d72aa64d809f045892a9c8c2)
#### Friday 2022-04-08 08:45:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [dalmatian128/duckstation](https://github.com/dalmatian128/duckstation)@[f9212363d3...](https://github.com/dalmatian128/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Friday 2022-04-08 09:59:05 by IlDucci

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7e96d3eefe...](https://github.com/treckstar/yolo-octo-hipster/commit/7e96d3eefe8af5bd8d4b7938afb471869b130550)
#### Friday 2022-04-08 12:00:05 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [Dieterdemuynck/OGP-Practica-2022](https://github.com/Dieterdemuynck/OGP-Practica-2022)@[4a73f09fab...](https://github.com/Dieterdemuynck/OGP-Practica-2022/commit/4a73f09fab590bf66b339ddaf4ac1831c5bc56f0)
#### Friday 2022-04-08 12:29:09 by Dieter Demuynck

Directory Contructor Documentation

Fuck this shit man, I hate it

---
## [intel/gvt-linux](https://github.com/intel/gvt-linux)@[53a05ad9f2...](https://github.com/intel/gvt-linux/commit/53a05ad9f21d858d24f76d12b3e990405f2036d1)
#### Friday 2022-04-08 13:19:12 by David Hildenbrand

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
## [wherkamp/nitro_repo](https://github.com/wherkamp/nitro_repo)@[c83068c78d...](https://github.com/wherkamp/nitro_repo/commit/c83068c78d5865f454cb2bcd404ca590475c6537)
#### Friday 2022-04-08 13:35:45 by Wyatt Jacob Herkamp

NPM Implementation (#338)

Honestly. I hate NPM

I am going to rant in the commit message
When NPM requests the file. This is what it gives you
`@shoppence/shoppence-ts/-/@shoppence/shoppence-ts-0.1.1.tgz`
So `{project_name}/-/{project_name}-{version}.tgz` Now in the dist tags in the package.json you can specify the tarball. But NPM does not care what you set it to. It always requests this.

Now this file location format is just horrible for organization. 

So I override this data a bit. It is barely an improvement `@shoppence/shoppence-ts/0.1.1/@shoppence/shoppence-ts-0.1.1.tgz` So I can keep all of the version files in one location.

I do understand that I lack knowledge on how NPM works. However, it is still a pain and I truly hate it.

Also NPM publish uses BASE64 inside JSON for sending the file. WTF

---
## [ldjebran/osbuild-composer](https://github.com/ldjebran/osbuild-composer)@[af44202b1c...](https://github.com/ldjebran/osbuild-composer/commit/af44202b1c6e53a5d3a248e2c1c493445743f188)
#### Friday 2022-04-08 15:03:00 by Ondřej Budai

cloudapi: rename gpg_key field to gpgkey

Oh no, we made a mistake here: Both our json repositories and repo files in
/etc/yum.repos.d have the GPG key in a field named `gpgkey`. Unfortunately,
cloudapi uses a field named `gpg_key`. One consequence of this issue is that
our api.sh test is meant to pass GPG keys in the compose request but since
it's using a bad field name (`gpgkey`), the key is actually not used.

I've decided to fix this in cloudapi: The `gpg_key` field is now renamed to
`gpgkey`. This is a breaking change but no one is using this API anyway so
we think it's better to do this now than introducing weird backward
compatible hacks.

Signed-off-by: Ondřej Budai <ondrej@budai.cz>

---
## [alphagov/govuk-infrastructure](https://github.com/alphagov/govuk-infrastructure)@[ed382d7f66...](https://github.com/alphagov/govuk-infrastructure/commit/ed382d7f664a7d4bb2bfdc5110c6d1e20795f852)
#### Friday 2022-04-08 15:19:55 by Chris Banks

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
## [uwstout-cs458-s22/advisor001](https://github.com/uwstout-cs458-s22/advisor001)@[bf6d5b5863...](https://github.com/uwstout-cs458-s22/advisor001/commit/bf6d5b586382c9138462004021ce71b34a564c9f)
#### Friday 2022-04-08 15:21:38 by Phosgenite

Current Attempt for api connection

pain.

Ruin has come to our family. You remember our venerable house, opulent and imperial, gazing proudly from its stoic perch above the moor? I lived all my years in that ancient, rumor shadowed manor, fattened by decadence and luxury - and yet I began to tire of conventional extravagance. Singular, unsettling tales suggested the mansion itself was a gateway to some fabulous and unnameable power. With relic and ritual I bent every effort towards the excavation and recovery of those long buried secrets, exhausting what remained of our family fortune on swarthy workmen and sturdy shovels.

At last in the salt soaked crags beneath the lowest foundations we unearthed that damnable portal of antediluvian evil. Our every step unsettled the ancient earth but we were in a realm of death and madness. In the end I alone fled laughing and wailing through those blackened arcades of antiquity until consciousness failed me.

You remember our venerable house, opulent and imperial. It is a festering abomination! I beg you. Return home; claim your birthright, and deliver our family from the ravenous, clutching shadows of the API functionality connection.

---
## [NokioPyro/Flas-And-Shit](https://github.com/NokioPyro/Flas-And-Shit)@[19fd4bafea...](https://github.com/NokioPyro/Flas-And-Shit/commit/19fd4bafea6091684e44061bef0c90231450f86c)
#### Friday 2022-04-08 16:49:46 by NokioPyro

Merge pull request #2 from NokioPyro/NokioPyro-patch-1-1

Fuck you dave how bout you algebra some bitches

---
## [FlafyDev/spicetify-cli](https://github.com/FlafyDev/spicetify-cli)@[0a89573c1c...](https://github.com/FlafyDev/spicetify-cli/commit/0a89573c1ce2f4ed3f4cdaac7651bc34dffb3a0a)
#### Friday 2022-04-08 17:21:24 by Łukasz Ordon

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
## [ABJ4403/Payback2_CHEATus](https://github.com/ABJ4403/Payback2_CHEATus)@[7a19e4a507...](https://github.com/ABJ4403/Payback2_CHEATus/commit/7a19e4a5076fcdbe138b3cfafed3591cbae36ffd)
#### Friday 2022-04-08 17:25:27 by MDP43140

Update Payback2_CHEATus to v2.1.6

+ revert tmp metatable changes, because garbage collector automatically clears its contents even if its being used.
+ changed rel0ad grenade cheat little bit (including putting ranges at 100)
+ using old tmp-clearing method because its just waaayyyy too much unknown errors.
+ and a little bit some changes.
+ move CH and tmp clearing codes to end of MENU().
+ New cheat: explosion direction (this 'overrides' mega explosion cheat thing).
+ New god mode cheat: Win (only tested on Rampage mode, thanks to JokerGGS for the idea).
+ remove ( and ) on if conditionals because its not required.
+ Adding 'feather death' value option to no blast damage cheat just for fun lol.
+ fixed some wrong CH order on some cheats.
+ Changed some value slightly on no blast damage.
+ adding the option to clear and search at the same time on respawn hack.
+ changing memZones[1,2] stuff to table.unpack, because its much shorter.
+ changing player name input to text (because suck gg for not giving a button to toggle external keyboard when using internal keys), and also the messages now suggesting user to edit-copy-paste custom name using hex-editor app.
+ changed cheat_explodepower to cheat_explodepow
+ changed `table.append(t1,v)` back to `t1[#t1+1]=v` on `table.append()` function helper, because its just basically same but much shorter.
+ changing some variable definiton whatever, and etc...

---
## [eric-burel/reactjs.org](https://github.com/eric-burel/reactjs.org)@[09eb372488...](https://github.com/eric-burel/reactjs.org/commit/09eb372488c278a1399b4775faf72d0b6fba80f5)
#### Friday 2022-04-08 17:58:00 by Eric Burel

Prefer build-time and render-time server-rendering to the SSG/SSR distinction

Ok, this sounds like a weird change, but bear with me. I've been doing some [formal research on SSR](https://tinyurl.com/ssr-theory) and I am convinced that we can vastly improve the current state of the industry by starting to use some better wording.

SSG and SSR is the terminology chosen by Next to distinguish build-time and request-time server-rendering. This terminology is historical, and well accepted, as most people mean "it's rendered at request-time, server-side" when they say SSR, and "it's rendered at build-time, server-side" when they say static.

Should we keep pushing this terminology? No, I can prove formally why it's wrong.

- It confuses many people, that don't get why "Server-Side Rendering" doesnt just mean "it's rendered on the server"

- People believe that there are 2 ways to do server-render. It's been true for a while but many technologies are exploring the space in between: Next.js ISR, Gatsby Deferred Static Rendering.

- It opposes SSR and SSG. If you see server-rendering as a big cache system for the web, SSG is simply a cache warm at build-time. SSR is a "cache miss". Next.js got it correctly, as ISR is "a cache that fills up when requested", well... like any good cache should do :)

I prefer to oppose "rendering times", so "Request Time Rendering" and "Build Time Rendering" for instance, making it clearer that those are not really incompatible choices, just configuration choice about when you render a page.

- It has been hindering further research on websites optimization.  Namely, people think you cannot use the Request object.

[SvelteKit](https://kit.svelte.dev/docs/page-options#prerender-when-not-to-prerender) states "The basic rule is this: for a page to be prerenderable, any two users hitting it directly must get the same content from the server."
This is maybe true for SvelteKit, but not true in the general case. I've heard the same idea from Gatsby, Astro. Even Next says that getStaticProps should be used when "The data can be publicly cached (not user-specific)" (which is all the more funny that I've coded a demo that bypass this limitation... using only Next.js)

With a simple redirection proxy (not even a full-fledged server, just something that can read "req" and redirect to any URL), you can bypass this limitation. If you don't believe me, check [Vercel Platforms implementation](https://github.com/vercel/platforms). It uses a tiny middleware and is able to prerender the same page for *different tenants*.

The problem is that the SSG/SSR distinction makes this way less obvious. The term "static" implies "there won't be any request processing". That's true at the app level, but apps are still run on servers. We can still put proxies in front of them. Therefore, we can make the "static"... dynamic again, and imagine incredible optimization, like prerendering paid, private, A/B tested, themed, internationalized, multi-tenant content without even running any Node server.

So, to sum it up, I believe this sentence is more correct this way

---
## [nevimer/bugstation13](https://github.com/nevimer/bugstation13)@[745426eff2...](https://github.com/nevimer/bugstation13/commit/745426eff227ff556105147a4802540617decd7b)
#### Friday 2022-04-08 18:34:31 by LemonInTheDark

Adds a colorblind accessability testing tool (#65217)

* Adds a colorblind accessability testing tool

I keep finding myself worrying about if things I create will be parsable
for colorblind people. So I've made a debug tool for approximating
different extreme forms of colorblindness.

It's very very much a hack. We can't do the proper correction required
to actually deal directly with long medium and short wavelengths of
light, so we need to rely on approximations. Part of that means say,
bright things being brighter then they ought to be. S not how people
actually experience things, but it's not something we can do anything
about in byond.

Anyway uh, it works by taking color matrixes, and using the plane master
grouping system floyd added to apply them to most all parts of the game
you would want to color correct.

There's some slight fragility here, but I couldn't think of a better way
of handling it.

We also need to deal with planes that have BLEND_MULTIPLY as their
blendmode, since that fucks up the filter. I've come up with a hack for
it, since I wanted to avoid breaking anything.

Oh and since I want it to apply to huds too I added plane masters to
represent them. I think that's about it.

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[c8ef62c1fb...](https://github.com/GoldenAlpharex/tgstation/commit/c8ef62c1fb7027ea58b569f0e4bd7df5a7d58935)
#### Friday 2022-04-08 18:41:59 by LemonInTheDark

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
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[e58fb506ef...](https://github.com/GoldenAlpharex/tgstation/commit/e58fb506effebc734a661718bed9ab2ffeb50c9e)
#### Friday 2022-04-08 18:41:59 by LemonInTheDark

Almost halves airlock auto close delay (#65349)

We go from a delay of 15 seconds, to 8.

This has cheesed me off for a long time. Airlocks should lock, not just
stay open for a quarter of a minute.

This'll help with excited groups that stay permenantly connected at
highpop because of a slowed ssair and doors opening and closing
constantly

Also effects door chasing. I'm honestly just kinda eyeballing this, it
might be a bit much. Even if this goes through could totally be tweaked

Even if this is too low, 15 is way too damn high.

---
## [CanamoToken/CYBAVO_WALLET_RN_SAMPLE](https://github.com/CanamoToken/CYBAVO_WALLET_RN_SAMPLE)@[56d38b3486...](https://github.com/CanamoToken/CYBAVO_WALLET_RN_SAMPLE/commit/56d38b3486177811b524aefb69e2e10d0c5a56dc)
#### Friday 2022-04-08 19:54:41 by atomauro

thanks god first step fuck you steve jobs an macbooks m1 chip

---
## [mbs-octoml/mbs-tvm](https://github.com/mbs-octoml/mbs-tvm)@[e63fdbd7dd...](https://github.com/mbs-octoml/mbs-tvm/commit/e63fdbd7dd2b6c80469fe32272325f58949e9a7f)
#### Friday 2022-04-08 20:20:24 by Mark Shields

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[51acee2a18...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/51acee2a1841156e4d0ce9b2b9e9d3cd4fc9a7d8)
#### Friday 2022-04-08 22:21:09 by GoldenAlpharex

The MODsuit Digital Revolution: Replaces AIs in MODsuits with pAIs (#11135)

* Replaces AIs in MODsuits with pAIs

* Whoops forgot to remove that

* Lmao begone spellcheck shit

* I may be stupid

* Removing comments that commented code when they didn't really need to.

* Stupid linters

* Fixed the fact that mod wasn't a variable of the module anymore

---
## [loypoll/PizzaTowerOnline](https://github.com/loypoll/PizzaTowerOnline)@[349f230f12...](https://github.com/loypoll/PizzaTowerOnline/commit/349f230f1282fbd36b6f6fa1ddc5053893a7ce00)
#### Friday 2022-04-08 22:57:03 by Denchickk

ancient bg and pissk and casu martzu and hyperthermia palettes

that's a lot
and no fuck you sts i'm not doing your idea

---
## [Bigboyyo/cmss13-design-docs](https://github.com/Bigboyyo/cmss13-design-docs)@[2dc78c4391...](https://github.com/Bigboyyo/cmss13-design-docs/commit/2dc78c4391e2fe20ab9b6cef1e1cd0b4a196c5ea)
#### Friday 2022-04-08 23:00:38 by Bigboyyo

I'm so sick of things preventing me from getting this merged holy fuck

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[5918489c0a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/5918489c0a6000d1e0c7a8c527931315bdba53e6)
#### Friday 2022-04-08 23:17:23 by Gandalf

[Salt PR] Stops station traits running on LOWMEMORYMODE as well as allowing admins to bypass flavour text (#12615)

* fuck you

* Update station.dm

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[9828f66548...](https://github.com/mrakgr/The-Spiral-Language/commit/9828f665485c322d35ed3954cd5a2baa5f3af661)
#### Friday 2022-04-08 23:53:24 by Marko Grdinić

"10:05am. I slept much better than yesterday and even had time to chill. Let me start. With the Wood Plank 1.5h course.

https://substance3d.adobe.com/tutorials/courses/Creating-Old-Wood-Planks-in-Substance-3D-Designer/youtube-vLz8ZyduQi0

Oh, I was wrong. This is 3:45h long.

https://substance3d.adobe.com/tutorials/courses/Designer-Quicktips/youtube-Xv-CfrMtS_M
https://substance3d.adobe.com/tutorials/courses/Getting-Started-with-MaterialX/youtube-bduf3TWmeMY

What is this about MaterialX.

Ok, let me just focus on studying today. I'll learn what I need and go back to Painter tomorrow.

https://youtu.be/S8P4QAH2K1U
Wood Grain

There is a tutorial on exactly what I wanted to do. This is a bit different than how I imagined it doing though. But there are plenty of ways of doing grains as expected.

10:35am. Let me start with the Wood Plank course. I'll just watch it for a while instead of following directly along as actually practicing would take too long.

11am. I saw this in one of the quicktips. If you double click on the empty space, you'll see random seed on the graph properties. That answers the question of how to randomize the seeds globally.

11:05am. Had to take a break, let me resume.

https://youtu.be/IcwDAoegKsg?t=581

His techniques are interesting. This is not something I would have figured out on my own. I guess some things really have to taught to me.

Yes, sure, maybe if I sat down and mucked around with these nodes at random for months I could have figured it out. But that is just in theory. Every loser thinks like that. I could have figure out AI using that same technique.

No. The best way to learn these techniques is to steal them. Let some other fool play around figure out the useful things. I am happy to get them from him.

https://youtu.be/frtvwbbtfOk
How to create tileable/seamless textures in Substance Painter

Let me pause so I can watch this 2m video. It is strange that Pt does not have an inbuilt plane model.

https://youtu.be/frtvwbbtfOk?t=46

Ah, right. Yesterday I had the idea of setting a brush to UV space. That would make it wrap around the edge of a plane. Wouldn't that work? Why do this then? Maybe it would not draw past the edge of a plane unless I shrunk it.

https://youtu.be/frtvwbbtfOk?t=74

He is doing that in fact. Seeing this example is giving me insight into how to do ornamental patterns.

Let me get back to the wood course.

What is Emboss?

https://youtu.be/jMs1U7G_LHQ
Emboss Node [Atomic Nodes] - Substance Designer (showcase)

That wood course is useful for teaching me things like this. I want to fill just a bit more of the gaps before I move to Painter for good.

Hmmm, it is an interesting effect. I get it now.

11:40am. I thought that Houdini would be good for heightfields, but this is quite something as well. Painter would be equally good as well.

What he is doing here at the start with just mixing different noises is something that could be done in Painter.

https://youtu.be/N4aNIDJ84nM?t=479

This part cofuses me. I am not really seeing the tiling break.

But that might just be because my focus is low. As expected, if you are just listeting to a talk, you are not into it as much if you are following along.

12:15pm. Ah, I should have beveled the rocks yesterday instead of bluring them. I need to remember to try that out in the future.

https://substance3d.adobe.com/tutorials/courses/Creating-Old-Wood-Planks-in-Substance-3D-Designer/youtube-we4lMxU94CA

I won't watch this. I am done with studying Designer. Good job me.

Now it is time to get real. I've built up my foundation in Painter enough. What I just need to do is use it and I will reach the level of expertise in 3d that I've been seeking.

I've got Blender and Houdini skills. It is time to start putting them together.

Now let me chill here for a while.

I am not going to rush this. I'll take it slowly today. I've worked so hard to get over the hurdles in 3d. The shading parts were rocky for a while, but they won't be getting in my way any longer.

2:25pm. Let me close Dendro. It is really hard to pry myself off, as I was starting to get into it.

2:30pm. What is hardship? Nothing.

Being able to say it is nothing is what separates an adult from a child.

The hardest thing in the world is to make a single single step forward. It is an adult thing to keep doing it regardless.

I did not change from my time in high school. The only thing that changed is that my true path is clearer. I cannot go faster, but I know where to go now.

2:35pm. These art skills are nothing. Six months of practice are nothing.

I've been doing it every day, and I will do it every day until I find the power that I seek.

One day the power of the machines will be mine. But today, let deal with the desk.

2:40pm. Just when is good enough, good enough? Right now it should be. I've put in enough work to consider myself an adult.

If I had a better background, I wouldn't have failed something like trading.
if I had a better background, I would not have lacked resources for the AI chips.

But in the long run those things do not matter. A 1000 years from now, the hurdles I've been facing now will just be a blimp on the timeline. It is a cheap price to pay to attain the priestly skill set.

The fact that I could go through the programming hurldes is why I can so fearlessly go into art.

2:45pm. i am not going to be doing my own props forever. I'll do some special cases like now, but afterwards I'll get a Alfafile or RapidGator acccount and get some proper kits. For models, I can just do them myself, but it is not like I can't get finished ones and adjust them.

2:50pm. With effort, I can succeed with art. So let me start.

4:40pm. Let me take a break. It is not going well.

5:35pm. Sigh, I am a fool. I am doing everything the opposite way around.

8:15pm. Fuck! Aren't the filters for Substance Painter documented anywhere? Why does the directional warp not work for me?

9:40pm. Oh, it actually crashed.

12:40pm. Fuck. I did not finish it despite being at it all this time.

12:55pm. Stop me, stop! I'll leave it for tomorrow.

I think I made a mistake trying to do this in Painter. I should have done the texture in Designer.

1:50am. Let me go to bed. I'll try it in Designer tomorrow. I'll talk about it more when I rest up."

---

