## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-23](docs/good-messages/2022/2022-04-23.md)


1,464,601 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,464,601 were push events containing 2,148,177 commit messages that amount to 122,672,309 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [StarStation13/StarStation13](https://github.com/StarStation13/StarStation13)@[dca0edc30e...](https://github.com/StarStation13/StarStation13/commit/dca0edc30e9db1424dffb582c5e8d075e0581ac0)
#### Saturday 2022-04-23 00:25:14 by B4CKU

Vim mecha changes (#66153)

This PR changes the following:

    fixes a bug with Vim overlays, making it always appear as if there was a pilot inside, even after leaving it
    adds a balloon alert when a mob fails to enter the mech due to its size
    adds a crafting recipe for Vim in the "robots" category
    allows using Vim as a circuit shell
    allows small mobs to use the mech as well

My reasoning behind the changes:

    fixing the overlay bug - bugfixes good, bugs bad
    balloon alert - it should help reduce confusion among players who can't figure why on earth they cannot enter the mech
    crafting recipe - I think a crafting recipe will make it a lot more accessible to players, especially because there is no way to learn about its existence in-game
    circuit shell - non-standard circuit shells can be pretty fun and people seemed to enjoy the ability to use circuits inside their piano synths or cameras, so I figured we could expand on this, while giving players more ways to interact with sentient pets
    maximum mob size increase - Vim has never really been built too often, most likely because even if people got their hands on a sentient pet, it wouldn't probably fit in the tiny mecha anyway. Currently pretty much only butterflies, rats and cockroaches can use Vim and they pretty much never become sentient.

---
## [MFScalzo/TechnologyProject](https://github.com/MFScalzo/TechnologyProject)@[3a98f3d0ce...](https://github.com/MFScalzo/TechnologyProject/commit/3a98f3d0cec37fff8b17cc5ac43337aad07213a9)
#### Saturday 2022-04-23 00:51:09 by Matt Scalzo

Finish HiveClient.scala and use in main()

Bunch of headaches with uploading the file to hdfs then into a hive
table. It is really annoying how the path changes depending on what
library you are using, some need hdfs://url stuff/path some just need
the path, and some just need the path to the parent folder since the
account for a bunch of files... Anyhow I ran into two notable bugs:
1. Hive expects data of type Timestamp to be in the form "YYYY-MM-DD
   HH:mm:SS" while the schema we were provided and what we made puts in
   the format "YYYY-MM-DD HH:mm" leaving off the seconds. This causes
   Hive to not recognize it as a Timestamp type. So as I have changed
   its data type to string for now... Not really our fault here, more
   the fault of whoever created the schema and the Sample Output
   Example.
2. There seems to be some sort of "bug", or maybe unintended
   consequence, of how we drop the table then create it on hive. As of
   this commit, when you rerun our JAR in the same session, a null row is
   added to the table everytime you rerun it. I am pretty sure this is a
   side effect of dropping the table then recreating it with the same
   name and schema right afterword but I have been unable to figure out
   how to solve this issue. These null rows will be excluded due to
   almost any sensible query so it is not a big deal.
Anyway, yeah, producer should be done after this is merged into the main
branch!!!!

---
## [userid0/rathena](https://github.com/userid0/rathena)@[d617d9f083...](https://github.com/userid0/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Saturday 2022-04-23 00:51:14 by Aleos

Updates SC_CHANGEUNDEAD behavior (#6867)

* Fixes #6834.
* Versus Players
- Animation will be properly displayed for Blessing/Increase Agility when the target has Change Undead active (buffs are not applied even though animation is displayed).
- Target can no longer be killed through the single damage applied by Blessing/Increase Agility and Change Undead.
- If the target has Curse and Stone active, only Curse is removed by Blessing first (buffs are not applied).
- Shadow or Undead armor have no impact on Blessing or Increase Agility at all.
* Versus Monsters
- Blessing is applied normally to the target as long as it's not an Undead element or Demon race.
- Blessing does not cancel out Curse or Stone.
Thanks to @Playtester!

---
## [rdspring1/pytorch](https://github.com/rdspring1/pytorch)@[65329f4fac...](https://github.com/rdspring1/pytorch/commit/65329f4fac8fb22318b7a3eb115e9da207d8d41a)
#### Saturday 2022-04-23 01:01:47 by Edward Z. Yang

Disable meta device tests.

After discussion with Can Balioglu, we have concluded that
https://github.com/pytorch/pytorch/pull/53682 , while clever, is more
trouble than it is worth.  The main problem is that whenever someone
adds support for new meta tensors, they then get dozens of new test case
failures, because tests that were previously halted by lack of support
for an operator on meta tensors, now have gotten further and hit some
logic which expects to be able to, e.g., pull out a real value from a
tensor (which clearly doesn't work).  This is very annoying and time
consuming!  Most of these tests aren't written with meta device in
mind, and it's not a good use of time to try to make them more generic.

The plan on record is to switch meta testing to OpInfo, but that patch
will take some time to prepare for now I want to stem the bleeding.  I
don't think we're at high risk for regressions here because meta tensors
mostly share logic with their regular brethren.

Signed-off-by: Edward Z. Yang <ezyangfb.com>

Pull Request resolved: https://github.com/pytorch/pytorch/pull/74468

Approved by: https://github.com/mruberry

---
## [MelonMars/Physarum-Python](https://github.com/MelonMars/Physarum-Python)@[5940a5aa27...](https://github.com/MelonMars/Physarum-Python/commit/5940a5aa273a6e39ef9b6f3ceea6784e38c9635a)
#### Saturday 2022-04-23 02:00:53 by MelonMars

ffs this isn't gonna work

TIME TO REWRITE THIS SHIT FOR THE THIRD GODDAMNT TIME

dear
fucking
god

---
## [Aliscans/crawl](https://github.com/Aliscans/crawl)@[af92d4a5d6...](https://github.com/Aliscans/crawl/commit/af92d4a5d6ba2f841e8bfdf8639f77a784fcaeae)
#### Saturday 2022-04-23 02:02:29 by Nicholas Feinberg

Make Hell Knights evil again (catern)

Lost this when they lost Pain.

Slightly hacky.

---
## [knowler/knowlerkno.ws](https://github.com/knowler/knowlerkno.ws)@[5e8fd6174f...](https://github.com/knowler/knowlerkno.ws/commit/5e8fd6174fd9acc1f49ee9abf851fdd5fa7c79a8)
#### Saturday 2022-04-23 02:06:17 by Nathan Knowler

Improve invalid form submission response + UI

We populate the form with the invalid data so that the user doesn’t need
to fill it out again. If the honeypot was triggered, we leave the form
empty as a “fuck you.”

---
## [Kapu1178/Pariah-Station](https://github.com/Kapu1178/Pariah-Station)@[6bb5cdfad0...](https://github.com/Kapu1178/Pariah-Station/commit/6bb5cdfad0e53897a72dfee1126553d62d92b4e3)
#### Saturday 2022-04-23 03:01:56 by PariahBot

[MIRROR] tgui: API improvements + docs (#461)

* tgui: API improvements + docs (#65943)


About The Pull Request

This pull request improves tgui API in many ways.

Using TGUI for custom HTML popups

This standardizes and simplifies the process of HTML popup creation and DM <-> JS communication.

Makes tgui window API a perfect alternative for old-style browser panels. It will be super useful for @Iamgoofball since he wanted to make a lightweight browser element that plays background music, and this will make his life a lot easier.

It is now possible to create tgui windows with fully inlined JS and CSS, which can be used to make unkillable tgui-based UIs (can't white/blue screen due to network errors). You can split files into JS and CSS, and still serve a single HTML file using this.

Moved sendMessage function to the Byond API object, where it rightfully belongs, and now supports a shorthand form: Byond.sendMessage(type, payload). This shortens and simplifies a lot of code.

Refactored window.update to no longer be public. Now to subscribe to incoming messages, you should use new public APIs: Byond.subscribe(fn) and Byond.subscribeTo(type, fn), and TGUI internally uses these functions as well, which reduces boilerplate in index.js.

Renamed window.__windowId__ to Byond.windowId (old variable is still available for backwards compatibility).

Byond API now supports null id, e.g. Byond.winget(null, 'url'), which makes things like this possible:

// Fetch URL of a currently connected server
Byond.winget(null, 'url').then((serverUrl) => {
  // Connect to this server (opens a new dreamseeker instance)
  Byond.call(serverUrl);
  // Close this client because new instance is connecting
  Byond.command('.quit');
});

Certain polyfills are now statically compiled (commited into git) and are baked into tgui.html. The downside is that HTML went 16 kB -> 50 kB. The upside is that you can now use a relatively modern level API with full support for IE8 when writing plain old html UIs using /datum/tgui_window directly. They are committed into git, because polyfills will never need to be updated (unless of course we randomly decide to get rid of ie8.js and html5shiv.js).
Breaking Changes

No breaking changes. This should be tested for regressions. Upgrading is simple if you're on a relatively up-to-date branch - copy paste all affected tgui files and you're good.

* tgui: API improvements + docs

Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>
Co-authored-by: Debian <debian@packer-output-01d6f1be-59bf-4994-80ec-c61b12fe30e1>

---
## [ericlawrey/ericlawrey.github.io](https://github.com/ericlawrey/ericlawrey.github.io)@[264f396a40...](https://github.com/ericlawrey/ericlawrey.github.io/commit/264f396a401844c6dde1f42ddca2f0201c599b51)
#### Saturday 2022-04-23 03:12:41 by Eric Lawrey

Update README.md

lamemathgamepizza amiright fellow pizza fans ok sure sounds good soooo what? YEAH? OK LOL HOW DO I DO THAT srry caps lock what am i doing wrong why arent you talking oh god haha  will secretly bettray him and type in allcaps this will be sooo funny wait no u wernt suppodes to loook my secrey plN RUINED NOOO srry caps lock

---
## [ItsProf-org/kernel_xiaomi-mt6768](https://github.com/ItsProf-org/kernel_xiaomi-mt6768)@[7be5f2fa4b...](https://github.com/ItsProf-org/kernel_xiaomi-mt6768/commit/7be5f2fa4baa9ded867916037af3b73286989a96)
#### Saturday 2022-04-23 04:26:15 by Peter Zijlstra

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
Signed-off-by: Vaisakh Murali <mvaisakh@statixos.com>
Signed-off-by: ImLonely13 <gabutuhaku@gmail.com>

---
## [OpenImageIO/oiio](https://github.com/OpenImageIO/oiio)@[594776d9c6...](https://github.com/OpenImageIO/oiio/commit/594776d9c617ab05b3cf0ff17d69dff908c1ae7e)
#### Saturday 2022-04-23 05:48:19 by Larry Gritz

Speed up case insensitive string comparisons (#3388)

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
## [weizhengte/incubator-doris](https://github.com/weizhengte/incubator-doris)@[ef2ea1806e...](https://github.com/weizhengte/incubator-doris/commit/ef2ea1806e4fb77369ab17a02d20fc8a286be43e)
#### Saturday 2022-04-23 06:29:46 by HB

[docs] Improve the chapter on debugging FE in doc.  (#7309)

At present, there are defects in the chapter on debugging FE in doc. My colleagues and I stepped on the pit when 
building the debugging environment, so I want to improve this chapter in combination with my own stepping on the pit 
experience.

The following is my explanation of the changes: 

1. mkdir -p ./thirdparty/installed/bin
explain: When I downloaded versions 0.14 and 0.15, there were no files under thirdparty, so I didn't know whether to 
create it myself or what to do. Finally, I decided to create it myself. I think it's necessary to add instructions here.

2. Add installation thrift@0.13.0 Failed handling method. 
explain: My colleagues and I failed to find the installation package when executing the installation command, and finally 
found a solution on GitHub. Therefore, I added the handling method of the problem to avoid other Mac users from 
getting stuck in this place.

3. Fixed an error in the generated code description.
explain: Before I finished building the code, I debugged FE, and I failed all the time. Idea hints that no files can be found. 
Later, after consulting with morningman in wechat group, it was understood that `mvn install -DskipTests` does not 
need to execute `mvn generate-sources` after execution. This is inconsistent with the description in the document and 
needs to be corrected.

---
## [OneAsianTortoise/tgstation](https://github.com/OneAsianTortoise/tgstation)@[351afe260b...](https://github.com/OneAsianTortoise/tgstation/commit/351afe260b42764641a07385df5f7e24b840f631)
#### Saturday 2022-04-23 06:35:22 by san7890

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
## [gauravkulkarni314/Stockfish](https://github.com/gauravkulkarni314/Stockfish)@[cb9c2594fc...](https://github.com/gauravkulkarni314/Stockfish/commit/cb9c2594fcedc881ae8f8bfbfdf130cf89840e4c)
#### Saturday 2022-04-23 06:36:25 by Tomasz Sobczyk

Update architecture to "SFNNv4". Update network to nn-6877cd24400e.nnue.

Architecture:

The diagram of the "SFNNv4" architecture:
https://user-images.githubusercontent.com/8037982/153455685-cbe3a038-e158-4481-844d-9d5fccf5c33a.png

The most important architectural changes are the following:

* 1024x2 [activated] neurons are pairwise, elementwise multiplied (not quite pairwise due to implementation details, see diagram), which introduces a non-linearity that exhibits similar benefits to previously tested sigmoid activation (quantmoid4), while being slightly faster.
* The following layer has therefore 2x less inputs, which we compensate by having 2 more outputs. It is possible that reducing the number of outputs might be beneficial (as we had it as low as 8 before). The layer is now 1024->16.
* The 16 outputs are split into 15 and 1. The 1-wide output is added to the network output (after some necessary scaling due to quantization differences). The 15-wide is activated and follows the usual path through a set of linear layers. The additional 1-wide output is at least neutral, but has shown a slightly positive trend in training compared to networks without it (all 16 outputs through the usual path), and allows possibly an additional stage of lazy evaluation to be introduced in the future.

Additionally, the inference code was rewritten and no longer uses a recursive implementation. This was necessitated by the splitting of the 16-wide intermediate result into two, which was impossible to do with the old implementation with ugly hacks. This is hopefully overall for the better.

First session:

The first session was training a network from scratch (random initialization). The exact trainer used was slightly different (older) from the one used in the second session, but it should not have a measurable effect. The purpose of this session is to establish a strong network base for the second session. Small deviations in strength do not harm the learnability in the second session.

The training was done using the following command:

python3 train.py \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    /home/sopel/nnue/nnue-pytorch-training/data/nodes5000pv2_UHO.binpack \
    --gpus "$3," \
    --threads 4 \
    --num-workers 4 \
    --batch-size 16384 \
    --progress_bar_refresh_rate 20 \
    --random-fen-skipping 3 \
    --features=HalfKAv2_hm^ \
    --lambda=1.0 \
    --gamma=0.992 \
    --lr=8.75e-4 \
    --max_epochs=400 \
    --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$2

Every 20th net was saved and its playing strength measured against some baseline at 25k nodes per move with pure NNUE evaluation (modified binary). The exact setup is not important as long as it's consistent. The purpose is to sift good candidates from bad ones.

The dataset can be found https://drive.google.com/file/d/1UQdZN_LWQ265spwTBwDKo0t1WjSJKvWY/view

Second session:

The second training session was done starting from the best network (as determined by strength testing) from the first session. It is important that it's resumed from a .pt model and NOT a .ckpt model. The conversion can be performed directly using serialize.py

The LR schedule was modified to use gamma=0.995 instead of gamma=0.992 and LR=4.375e-4 instead of LR=8.75e-4 to flatten the LR curve and allow for longer training. The training was then running for 800 epochs instead of 400 (though it's possibly mostly noise after around epoch 600).

The training was done using the following command:

The training was done using the following command:

python3 train.py \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        /data/sopel/nnue/nnue-pytorch-training/data/T60T70wIsRightFarseerT60T74T75T76.binpack \
        --gpus "$3," \
        --threads 4 \
        --num-workers 4 \
        --batch-size 16384 \
        --progress_bar_refresh_rate 20 \
        --random-fen-skipping 3 \
        --features=HalfKAv2_hm^ \
        --lambda=1.0 \
        --gamma=0.995 \
        --lr=4.375e-4 \
        --max_epochs=800 \
        --resume-from-model /data/sopel/nnue/nnue-pytorch-training/data/exp295/nn-epoch399.pt \
        --default_root_dir ../nnue-pytorch-training/experiment_$1/run_$run_id

In particular note that we now use lambda=1.0 instead of lambda=0.8 (previous nets), because tests show that WDL-skipping introduced by vondele performs better with lambda=1.0. Nets were being saved every 20th epoch. In total 16 runs were made with these settings and the best nets chosen according to playing strength at 25k nodes per move with pure NNUE evaluation - these are the 4 nets that have been put on fishtest.

The dataset can be found either at ftp://ftp.chessdb.cn/pub/sopel/data_sf/T60T70wIsRightFarseerT60T74T75T76.binpack in its entirety (download might be painfully slow because hosted in China) or can be assembled in the following way:

Get the https://github.com/official-stockfish/Stockfish/blob/5640ad48ae5881223b868362c1cbeb042947f7b4/script/interleave_binpacks.py script.
Download T60T70wIsRightFarseer.binpack https://drive.google.com/file/d/1_sQoWBl31WAxNXma2v45004CIVltytP8/view
Download farseerT74.binpack http://trainingdata.farseer.org/T74-May13-End.7z
Download farseerT75.binpack http://trainingdata.farseer.org/T75-June3rd-End.7z
Download farseerT76.binpack http://trainingdata.farseer.org/T76-Nov10th-End.7z
Run python3 interleave_binpacks.py T60T70wIsRightFarseer.binpack farseerT74.binpack farseerT75.binpack farseerT76.binpack T60T70wIsRightFarseerT60T74T75T76.binpack

Tests:

STC: https://tests.stockfishchess.org/tests/view/6203fb85d71106ed12a407b7
LLR: 2.94 (-2.94,2.94) <0.00,2.50>
Total: 16952 W: 4775 L: 4521 D: 7656
Ptnml(0-2): 133, 1818, 4318, 2076, 131

LTC: https://tests.stockfishchess.org/tests/view/62041e68d71106ed12a40e85
LLR: 2.94 (-2.94,2.94) <0.50,3.00>
Total: 14944 W: 4138 L: 3907 D: 6899
Ptnml(0-2): 21, 1499, 4202, 1728, 22

closes https://github.com/official-stockfish/Stockfish/pull/3927

Bench: 4919707

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a137c15a79...](https://github.com/tgstation/tgstation/commit/a137c15a790bc8242a1ccd70bb6570d0278833c0)
#### Saturday 2022-04-23 07:14:17 by Vladin Heir

Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [kjopnfer/OvermorrowMod](https://github.com/kjopnfer/OvermorrowMod)@[7047ec0eb9...](https://github.com/kjopnfer/OvermorrowMod/commit/7047ec0eb9db376b54b666d13fb87041bf14b290)
#### Saturday 2022-04-23 07:22:27 by VintageM8

Fuck you old shitty theme, no one loves you. Go die in the trash

---
## [homer-simpson-2200/simpson-code](https://github.com/homer-simpson-2200/simpson-code)@[ab26f53d25...](https://github.com/homer-simpson-2200/simpson-code/commit/ab26f53d256d558efe4906ad69bf8f55d83994a3)
#### Saturday 2022-04-23 08:03:29 by homer-simpson-2200

Rename Code I wrote xijinping.ts(DevRussia) to Code I wrote xijinping.ts(DevRussia)(i think DevRussia delete that project. fuck you DevRussia!! 🤬🤬🤬)

---
## [macka69/kernel_xiaomi_sm8250](https://github.com/macka69/kernel_xiaomi_sm8250)@[38b0bd0f25...](https://github.com/macka69/kernel_xiaomi_sm8250/commit/38b0bd0f251010073efb3fc37a708ae9079bb332)
#### Saturday 2022-04-23 08:49:19 by Linus Torvalds

gpiolib: acpi: use correct format characters

[ Upstream commit 213d266ebfb1621aab79cfe63388facc520a1381 ]

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [DeadBirdStudio/Wormhole2](https://github.com/DeadBirdStudio/Wormhole2)@[21a6c11e7c...](https://github.com/DeadBirdStudio/Wormhole2/commit/21a6c11e7c34305b648ed9ce69b1db7632e1719f)
#### Saturday 2022-04-23 09:04:12 by Liam Goel

Redoing win portal and some save system shenangians

Fuck you unity

---
## [DeadBirdStudio/Wormhole2](https://github.com/DeadBirdStudio/Wormhole2)@[a8dbc0df95...](https://github.com/DeadBirdStudio/Wormhole2/commit/a8dbc0df95173dc3653b2829c45d59d7268974f4)
#### Saturday 2022-04-23 09:04:12 by Liam Goel

FUCK ME

- Unity is letting me use it again.

- Everything in LevelForge is gone, the branches where there are things in it unity broke on me and I don't want to be unproductive troubleshooting it so instead I'll be inefficient and redo work (Yay!)

- Some beginning changes on the Win Portal Script, still need to get the Wormhole script back to doing a wicked sick teleport and move that code out of Player Interactions

- This was exceptionally upsetting

---
## [mehul-sonthalia1987/Flip-Robo](https://github.com/mehul-sonthalia1987/Flip-Robo)@[140274afbb...](https://github.com/mehul-sonthalia1987/Flip-Robo/commit/140274afbb0d6297ec6427e8fc17378207427328)
#### Saturday 2022-04-23 10:28:44 by mehul-sonthalia1987

Micro-Credit Defaulter Model

Problem Statement: 
A Microfinance Institution (MFI) is an organization that offers financial services to low income populations. MFS becomes very useful when targeting especially the unbanked poor families living in remote areas with not much sources of income. The Microfinance services (MFS) provided by MFI are Group Loans, Agricultural Loans, Individual Business Loans and so on. 
Many microfinance institutions (MFI), experts and donors are supporting the idea of using mobile financial services (MFS) which they feel are more convenient and efficient, and cost saving, than the traditional high-touch model used since long for the purpose of delivering microfinance services. Though, the MFI industry is primarily focusing on low income families and are very useful in such areas, the implementation of MFS has been uneven with both significant challenges and successes.
Today, microfinance is widely accepted as a poverty-reduction tool, representing $70 billion in outstanding loans and a global outreach of 200 million clients.
We are working with one such client that is in Telecom Industry. They are a fixed wireless telecommunications network provider. They have launched various products and have developed its business and organization based on the budget operator model, offering better products at Lower Prices to all value conscious customers through a strategy of disruptive innovation that focuses on the subscriber. 
They understand the importance of communication and how it affects a person’s life, thus, focusing on providing their services and products to low income families and poor customers that can help them in the need of hour. 
They are collaborating with an MFI to provide micro-credit on mobile balances to be paid back in 5 days. The Consumer is believed to be defaulter if he deviates from the path of paying back the loaned amount within the time duration of 5 days. For the loan amount of 5 (in Indonesian Rupiah), payback amount should be 6 (in Indonesian Rupiah), while, for the loan amount of 10 (in Indonesian Rupiah), the payback amount should be 12 (in Indonesian Rupiah). 
The sample data is provided to us from our client database. It is hereby given to you for this exercise. In order to improve the selection of customers for the credit, the client wants some predictions that could help them in further investment and improvement in selection of customers. 
Exercise:
Build a model which can be used to predict in terms of a probability for each loan transaction, whether the customer will be paying back the loaned amount within 5 days of insurance of loan. In this case, Label ‘1’ indicates that the loan has been payed i.e. Non- defaulter, while, Label ‘0’ indicates that the loan has not been payed i.e. defaulter.  
Points to Remember:
•	There are no null values in the dataset. 
•	There may be some customers with no loan history. 
•	The dataset is imbalanced. Label ‘1’ has approximately 87.5% records, while, label ‘0’ has approximately 12.5% records.
•	For some features, there may be values which might not be realistic. You may have to observe them and treat them with a suitable explanation.
•	You might come across outliers in some features which you need to handle as per your understanding. Keep in mind that data is expensive and we cannot lose more than 7-8% of the data.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[658ba0a226...](https://github.com/mrakgr/The-Spiral-Language/commit/658ba0a226c7a24b10f3b7a02a7339e9a12bda53)
#### Saturday 2022-04-23 11:24:39 by Marko Grdinić

"9:05am. I am up. Let me chill a bit and then I will start. No email good. It seems the Strong Compute affair is done for good. Tech recruiters are so cunning these days. Though I am flattered one of the founders was so impressed by whatever I did that he resorted to this sort of manipulation, I actually don't get offers from recruiters so being upfront about their needs and giving me decent conditions could have worked. I get the sense that they want a talented person, but also want that talent to be a guilible moron. Well, keep looking.

10:05am. Right now I am catching up to the latest UQ Holder thread. Somehow I skipped Negima and everything else up to now, but I want to have some fun with this.

10:15am. just a bit more and I will start. I need to go through the docs, the revolver tutorial, the art station thing.

10:35am. Let me start. I don't know, if I am making a mistake, then maybe the only mistake is not going with the symbolic approach. But I am not that autistic to just crank out code all day.

Not wanting to delve too deep into symbolics was one of the reason behind not becoming a programmer out of high school. It was also what deep learning was supposed to replace at least for ML.

So maybe I am just salty and overreacting.

10:55am. https://topologyguides.com/

I am reading this.

> Don't use holding edges when possible.

> While holding edges are a great thing they almost always cause distortion...

I can't copy paste, and don't feel like writing out the whole thing by hand.

Yeah, if watching Arrimus work with subdiv is any indication, I am doing subdiv modeling all wrong. He is using evenly spaced quads, but I am using all sorts of strange topology.

11am. https://youtu.be/VTsCyzO3Vsw?t=74
Revolver Cylinder Detail | Requests

Let me watch some things like this. Let me just do what I want. I need to shake off my groginess.

https://youtu.be/VTsCyzO3Vsw?t=309

This looks really great.

Yeah, my impression of what subdiv was about is completely wrong.

But on the plus side, I won't have to care about this once I move to using Moi.

https://youtu.be/raXaLhA2Ob8
How You Model Dem Shapes? EP.3 - Piston-Like Shape

Let me also watch this.

https://youtu.be/raXaLhA2Ob8?t=342

Not how I thought he would approach the shape. In Moi this would be the easiest task ever.

https://youtu.be/raXaLhA2Ob8?t=476

3ds Max has this? This is pretty interesting. I've felt for a while that Blender' bevel capabilities are lacking.

Even just considering pologon there should be better ways of doing it.

https://youtu.be/raXaLhA2Ob8?t=537

Very easily my ass. This would be half a minute in Moi. The amount of extra work this took in 3ds Max is astonishing. It wouldn't have taken any less in Blender.

https://youtu.be/3S0NvmcYq08
The BEST and WORST purchases for 3D artists

Let me watch this.

https://youtu.be/3S0NvmcYq08?t=481

So far he has been railing against art schools and schools in general. But his world make sense. His guru moniker is deserved.

11:40am. > Yeah, choosing the wrong art school can be a disaster. One momment you say "yeah, I can do this" and next you invade Poland.

Top comment.

11:40am. Focus me. I can't find the revolver tutorial, but nevermind it. The remesher really works like crap for me, so I am surprised that this is the suggested workflow. Forget the Blender stuff. I won't be using it. If I really had to, I'd just end up retopoing the subdiv stuff or the Moi stuff.

What is next?

Let me check out that post on art station yesterday.

https://www.artstation.com/artwork/mqv1QE

It is not some long video tutorial. I wonder why UVs generated by RizomUV on the low model work on the high poly one. How would that transfer work?

I am not sure. Nevermind it for now.

Let me focus on the Moi docs. I am done with Blender for now. I probably won't use it again for modeling, only sculpting.

https://youtu.be/eU5RucXsIAA
Understanding FLOW in MoI3D

This is the deform node. I am not sure what the third input is for.

12:05pm. Ok, I get it. Quite remarkable. Too bad nurbs do not have something like a lattice. I guess that sort of thing is a benefit of pologonal modeling.

12:45pm. I got an intuitive sense for the network node. It is really powerful.

1pm. Yeah, it is amazing, it is quite intuitive.

https://www.youtube.com/watch?v=SKIKBVYOR6U
MoI3D Basics: Modelling a SciFi Part

I skimmed this earlier.

1:10pm. Mhhh, I do not know what history is, but it is not necessarily the same thing as that Fusion 360 feature where you can go back to edit anything. Moi is destructive. It does not have much docs

///

Enables or disables history updating on an object.

Some commands have history updates enabled by default. For example, the Loft command will update the lofted surface if you edit one of the original curves. If you want to stop that updating, you can select the lofted surface, run the History command and click "Disable update". After that the lofted surface will no longer update when you edit the original input curves. Also, some commands have history disabled by default such as Transform > Copy or Transform > Rotate. You can use History > Enable update to turn history updates on for the results of these commands.

///

Well, I suppose this is clear enough.

Hmmm...

///

Extend a curve to meet the selected boundary objects. The boundary objects can be curves, surfaces, or solids. Currently only curves are supported as the object to be extended.

Lines and curves will be extended by a straight line. Arcs will be extended as arcs.

Example for extending curves to a boundary:

///

Extend works on surfaces and solids it seems.

1:20pm. Hmmmm...

Phhhhhhh...I am ready.

I hadn't studied the docs all that much. I actually did a bit yesterday, but it seems that was enough.

1:25pm. Let me take a break here. I am overdue for breakfast."

---
## [kannthus/Skyrat-tg](https://github.com/kannthus/Skyrat-tg)@[5b8feb6cda...](https://github.com/kannthus/Skyrat-tg/commit/5b8feb6cda2094dc4c1919539ba1c571ccf6af9c)
#### Saturday 2022-04-23 11:27:44 by SkyratBot

[MIRROR] Almost halves airlock auto close delay [MDB IGNORE] (#12314)

* Almost halves airlock auto close delay (#65349)

We go from a delay of 15 seconds, to 8.

This has cheesed me off for a long time. Airlocks should lock, not just
stay open for a quarter of a minute.

This'll help with excited groups that stay permenantly connected at
highpop because of a slowed ssair and doors opening and closing
constantly

Also effects door chasing. I'm honestly just kinda eyeballing this, it
might be a bit much. Even if this goes through could totally be tweaked

Even if this is too low, 15 is way too damn high.

* Almost halves airlock auto close delay

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[cd1b891d79...](https://github.com/ZephyrTFA/tgstation/commit/cd1b891d79c08b87ebcecf0a4f1656e386bd3eab)
#### Saturday 2022-04-23 13:11:41 by magatsuchi

Modular Tablets: Converting PDAs to the NtOS System (#65755)

Converts PDA functions and applications over to modular tablets and devices, namely the messaging function. HREF data code is quite honestly clunky and difficult to work with, as I've definitely experienced whilst working on this. By moving from this system over the easier to read (and frankly, easier to add to) TGUI system, you get cleaner looking and more user friendly UIs and a greater degree of standardization amongst other UIs.

Co-authored-by: Seth Scherer <supernovaa41@gmx.com>
Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>
Co-authored-by: Aleksej Komarov <stylemistake@gmail.com>

---
## [dcunited001/dotfiles_doom](https://github.com/dcunited001/dotfiles_doom)@[dbbdfa6ae5...](https://github.com/dcunited001/dotfiles_doom/commit/dbbdfa6ae5cc6b2f23964d49c24de0563ecb3241)
#### Saturday 2022-04-23 14:18:43 by David Conner

everything here is to figure out WTF is causing my org/roam performance issues

- org-mode temporary buffers especially cause problems

- running multiple frames definitely causes a specific kind of bottleneck

- doing *anything productive* with org/roam *seems to trigger the issues*

and, if i'm understanding this correctly, emacs is "garbage collecting" too often
which is probably what i should fix. too bad it doesn't show in the memory profiler.
this is basically why i broke my laptop screen. for about 18 months, i have been
on/off looking for the cause TO THESE SPECIFIC PROBELMS. there is no way that
anyone would use emacs/org if they encountered this many performance issues ...
but it's just me, my config and whatever is wrong with my fucking my org-files.

it's a real shame because -- FOUR HOURS AGO -- what i thought i would be doing
was enabling SMILES-MODE so i could fucking STUDY 3D PRINTING PLASTICS. but no.
nope. just fucking around with the goddamn =config.org= file ... WHICH HAS MORE
PERFORMANCE ISSUES THAN ANY OTHER FUCKING FILE.

* ensure inline org-src-fontification buffers don't run prism-mode

* disable bufler-mode (it never finishes native comp ...)

* disable org-roam-completion (everywhere)

* don't use dimmer-mode on company-mode-boxes

* (just incase i get 0.1% of my performance back ... who the fuck knows?)

* move tooltips to echo area (in case pGTK is responsible for my performance issues?)

* i sure hope this isn't a problem if i use wayland again

* set org-agenda-files to nil (because why not?)

---
## [classified/android_kernel_oneplus_sm8150](https://github.com/classified/android_kernel_oneplus_sm8150)@[b70d3366a3...](https://github.com/classified/android_kernel_oneplus_sm8150/commit/b70d3366a3cc559a669b1c82cff78e567c86a618)
#### Saturday 2022-04-23 15:32:18 by alk3pInjection

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
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[5d51b874d1...](https://github.com/mrakgr/The-Spiral-Language/commit/5d51b874d19bb040a808770b96acda275edc86fc)
#### Saturday 2022-04-23 15:41:01 by Marko Grdinić

"2:45pm. I sure am tired. Let me chill a bit more.

3:10pm. Let me start.

https://www.youtube.com/channel/UCYUWarGVD1rdKDOnOSZbrOQ

Let me just check this guy out.

https://youtu.be/-H1-An1DmLA?t=1
cabochan way blend

What the hell are all these scripts?

...Nevermind, I am not into these tutorials without audio.

3:15pm. Let me play a bit with network and then I will start on the monitor.

3:20pm. To network, it makes a difference whether I have a single curve or one cut in the middle.

3:25pm. https://www.youtube.com/channel/UCGZunNuwUjOY9EWS_-z8trA

Let me watch some of the official Moi 3d vids that are linked in the help.

https://www.youtube.com/watch?v=1B8g42hHJqg
Sunburst

I am mentally prepping myself for the next step. Network is really powerful. I can do a lot with it. Nurbs modeling lacks a bit of flexibility that pixel model does, but I am not sure if the deformation that I have in mind should be intrinsic to it. It is just that Moi does not have them.

3:40pm. https://youtu.be/G8p_ZOvfaso
CrownOfClubs

This one is next.

3:50pm. https://youtu.be/G8p_ZOvfaso?t=271

As I think about this, a thought is starting to surface. Could I use these techniques in Illustrator?

Not really. It has curves, but they are 2d. Not buch I can do about that.

4pm. https://youtu.be/1gcyk2g9deQ
Pod

Let me go for this as well.

https://youtu.be/1gcyk2g9deQ?t=253

Hmm, this is nice. I need to keep this technique of drawing contruction lines in mind.

https://youtu.be/1gcyk2g9deQ?t=920

I hadn't realized that window select is adaptive like this. Nice.

4:20pm. Zbrush is 1.75gb split into 4 parts. RizomUV is 180 only. I'll get it right now.

I might as well get Zbrush while I am at it.

4:30pm. Ok, now, by all means I am supposed to start on the monitor, but I just want to step away from the screen.

The feeling I have right now is that I have it.

Moi 3d essentially resolves all the issues that I've had with Blender's modeling. Even in places where Blender could be better, it is not by much. Moi does not lack power, at worst it might lack a tad ergonomics.

But I do not think even that would be the case.

If I did the monitor using subdiv then yes, I'd have more flexibility to adjust it once it is done, but with the network tool, I could do it in less strokes. And what happened is that I applied the subdiv because of the booleans and had to use the lattice mod anyway. Big whif.

4:30pm. Right now I am reviewing in my head. Adobe Illustrator. I studied it for so much, but now I can barely remember what it was about. Whenever I need to trim a screenshot I just load up CSP and do it there.

It is time to let go of a lot of things.

I've been pushing onwards mixing real practice and learning from others. Moi 3d is so simple that half a week is enough to master it in its entirety. Commpared to any other art programs even 2d ones, it is by far the simplest.

What I will do now is break out my tablet and start modeling. I never expected I would be using it for something like this, but it will serve very well.

I've been running simulations in my head the whole day today.

Is the crop of tools Moi offers me enough or not? Yeah, it is enough to replace all my needs in Blender. I got all those plugins and even paid for MESHmachine, but it turns out I won't need them.

4:50pm. I've made it.

It felt like I've been mid 2/5, but now I am only a few props away from being high 2/5. I just have to practice making them in Moi a bit to internalize the lessons and then that will be there.

Not only that, but I have a foundation in sculpting, texturing and unwrapping now as well. With Clarisse I have an answer on how to put together bigger scenes, on other words layouting. And with the Houdini knowledge that I've acquired, I have an answer for procedural generation too.

By the end of next month, I will be high 2/5 and after that I'll be a step away from the pro level.

The way I will hit the pro level is by mastering all the tools at my disposal and sheding away the unecessary.

Remember what Arrimus said about 2d being faster than 3d.

All this 3d knowledge is essentially scaffolding that will help me later in the move to 2d.

If I can master the 3d tools to a sufficient degree as well as become fast at making 2d, I will have the quality and speed to consider myself 3/5. At that point making my own assets whether it be games or illustrations will cease to be a problem. Remember how annoying it was in 2014 to have finished writing those stories, but not being able to do the covers.

When I am able to do the cover for Heaven's Key, I can consider myself as having accomplished something significant.

It might be fighting a war that is long over, but I do not want to go into the future saying that art is not one of my talents. And if get truck'd and reincarnate back into my schooldays, I'll be sure to get top grades much like in programming. That is the way to think here.

5:10pm. Higher mastery for a higher level of power.

I need to gaze up and stretch my hand out towards the stars.

Model -> texture -> layout.

I think that a lot of the workflow present in 3d also manifests itself in 2d as well. Beginners try to skip them and end up with poor results.

I'll definitely find that out.

When I master my 3d workflow, I'll be able to visualize it and apply it to 2d.

it is similar to how I can imagine code flow in my bed away from the screen.

If you sit down and just start writing code ad-hoc then you are lost. The same goes for drawing.

My conjecture from the beginning was that 3d was good training for 2d, and I am going to get a chance to test that. I can't really imagine somebody being 5/5 at 3d and 1/5 at 2d. The real world does not work that way.

5:15pm. Yeah, I've forgotten that up to now. Although I am doing 3d, what I really wanted deep down was to become good at 2d.

The reason why I went the 3d route is because even though I could have just done 2d directly, trying to do that would be like doing Assembly programming. You can never learn what programming is about by using low level languages, instead you have to go functional and pursue abstraction. This is why despite all the effort I put into Blender, I will move into Moi for prop modeling.

5:25pm. Let me step away from the screen.

My heart was weak and it still is. I've suffered from abandoning my earlier path. But I will endure.

And what once I reach the level of being able to do good art quickly, it will all be worth it. Compared to how much time and effort I put into programming, this here is nothing. I need to believe that I can do it. Deep down, I've started to think that given how much work 3d is, will it really be worth it if I can't do it quickly enough? Sometimes depression can be indiced simply by lack of ambition. It should have been obvious that I would need to master 2d as well. I need to believe that 3d will allow me to do that. I need to believe that being able to walk will allow me to run. Walking will never beat running in terms of speed, but I should not try to skip realms and break my leg in the process.

These reviews and brainstorming sessions are not just to make future plans. They are also to make me realize how much ground I've covered.

A journey of a thousand miles is long, but if you look back and see that you've already 50% done, then why would you stop midway?

Right now, I am done with the hard and tedious parts of art. I've struggled a lot, but from here it will be time for the fun stuff. I have no more need for tutorials. I can just focus on making art and quietly, but surely grind my way to the pro level. From here on out I'll have something to show for my effort."

---
## [BMT-z/curriculum](https://github.com/BMT-z/curriculum)@[9c740aacfa...](https://github.com/BMT-z/curriculum/commit/9c740aacfa82b3abb39345c2f6fe042c271ca711)
#### Saturday 2022-04-23 15:50:04 by BMT-z

Add section for warnings about branch diversions

From personal experience and what I've seen in the git-help channel it seems like a few people are struggling with the issue of branch diversion, I'm still doing the html foundations and didn't realize making changes to my readme file via GitHub would cause the branch diversion issue, I think in git basics it should state that making any changes to your files via GitHub can cause issues and if you want to change even the readme file it's best to do it via a commit and push, I'm aware this is covered later on but i still believe making this a note in the git basics section would help a lot of users from running into this issue.

---
## [MichelJuillard/Yggdrasil](https://github.com/MichelJuillard/Yggdrasil)@[b1469b44df...](https://github.com/MichelJuillard/Yggdrasil/commit/b1469b44df4c63961a6c0f0387a89ef4ef24aa26)
#### Saturday 2022-04-23 16:59:09 by Elliot Saba

[GCCBootstrap_jll] Build using `crosstool-ng` (#4753)

In the beginning, I wanted to compile a nice little standalone `GCC_jll`
that could be hooked together with a `Glibc_jll` and a `Binutils_jll`,
and a `LinuxKernelHeaders_jll`, etc...  That work is sitting in [0] but
bootstrapping is such a giant pain in the neck that I wanted to give up
the complexity of bootstrapping to instead focus on simply building each
product in isolation.  This _vastly_ reduces the amount of work
necessary to get things working, but it introduces a new dependency: we
need a base C compiler and libc that are already compiled for the target
platform.  To be precise, we need a `build -> host` compiler in order to
build a `host -> target` compiler.  We already have one of those for all
of our current platforms, so I could generate `GCC_jll` packages, but
then when we want to add a new platform, we'd be in trouble.  For this
reason, I realized we'll never truly escape the bootstrapping problem.

I thought about reverting back to the bootstrapping configuration we've
had until now, but rebelled at the thought.  Then I discovered
crosstool-ng, and realized that I could separate concerns here: I can
use ct-ng to build a working cross-toolchain for each target, then use
that compiler to do a much simpler build for all of the other
components.  Therefore, I extract the work of getting a bootstrap build
onto crosstool-ng, and then use that to do whatever other builds I want
in the presence of a fully-functional cross-compiler.

This also breaks the need for the initial bootstrap to be quite as
restricted as the target toolchain.  The GCC that we build technically
doesn't need to run everywhere, it just needs to generate code that runs
everywhere.  We can build GCC against glibc 2.19, and then at build time
have it link the code it generates against glibc 2.12.2, and that will
work just fine for BB.  The compiler may be using a newer glibc to run,
but when it builds, it uses whatever glibc is placed within the target
sysroot.  This also means we don't need to do things like build GFortran
as part of our bootstrap; we can build it later, in the simpler build
script.

In principle, we don't actually need a GCCBootstrap for all platforms.
We only need a functional cross-compiler.  Theoretically, we could use
Clang to do the bootstrapping.  But I'm not going to fully embrace that
because I know that compiling Glibc with Clang is a pain, so for
`*-linux-gnu` at the very least, we're not going to attempt that.  On
macOS and FreeBSD however, there is a possibility that we can use Clang
as our "bootstrap compiler" in order to generate the actual GCC_jlls.

[0] https://github.com/JuliaPackaging/Yggdrasil/tree/sf/gcc

---
## [KathyRyals/Skyrat-tg](https://github.com/KathyRyals/Skyrat-tg)@[242ef904f0...](https://github.com/KathyRyals/Skyrat-tg/commit/242ef904f0a2ea2cc5de87863e93def5131ea0be)
#### Saturday 2022-04-23 17:31:59 by SkyratBot

[MIRROR] Fixes bartender drink throwing, makes smashing always spill [MDB IGNORE] (#12326)

* Fixes bartender drink throwing, makes smashing always spill (#65698)

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

* Fixes bartender drink throwing, makes smashing always spill

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [PrincessAkira/PlayerHider-1.8](https://github.com/PrincessAkira/PlayerHider-1.8)@[4086935f82...](https://github.com/PrincessAkira/PlayerHider-1.8/commit/4086935f82a08154ebe0be2f3de27f73ef72c94d)
#### Saturday 2022-04-23 17:42:54 by Emily Engel

im done.
please fucking kill me
i dont wanna live anymore.
this is way too much fucking shit do to please for the love of god

Signed-off-by: Emily Engel <Justsweetluna@gmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[cc1a84c9ab...](https://github.com/treckstar/yolo-octo-hipster/commit/cc1a84c9abc854ee0d253576d680a28753402075)
#### Saturday 2022-04-23 18:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [sailfishos-mirror/openconnect](https://github.com/sailfishos-mirror/openconnect)@[b982b2e41e...](https://github.com/sailfishos-mirror/openconnect/commit/b982b2e41ec9e711f086b62951dabfb6509057ae)
#### Saturday 2022-04-23 18:26:36 by David Woodhouse

Silence static-analyser warning about redundant assignment to 'sep'

I did this for a reason. The *compiler* is clever enough not to bother
actually doing the assignment (not that it would matter anyway, since it
is hardly a fast path). But *developers*, including myself, are much less
likely to spot that it needs to be added in the 'deflate' case if we add
a new case at the end. So now in order to shut the tools up, I have to
turn a non-bug into a latent *actual* bug.

I suppose I could leave it there with a comment, or refactor it into a
loop over tuples of the form { COMPR_LZ4, "oc-lz4" }…  but it probably
doesn't matter as we're unlikely to be adding more. Just suck it up.

Signed-off-by: David Woodhouse <dwmw2@infradead.org>

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[d411393e72...](https://github.com/SmoSmoSmoSmok/tgstation/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Saturday 2022-04-23 18:28:00 by Zytolg

NukeOps Firebase Rework (#66149)

Attention Recruit: Welcome to Firebase Balthazord
Here you will lean how to:
-Kill corpo scum
-Kill corpo scum
-Kill corpo scu-

This has been on my docket for months. Ever since gave the Holding Facility a much needed facelift. I have been eyeballing the nukie base, waiting for that stroke of inspiration to hit me. It finally did. Gone are the aging walls of the old encampment. Nukies finally have what well-funded corpo-terrorists always dream of- a home.

It's more than a Home. This is a sweeping rework that is part of a series of reworks to revisit old locations and not only bring them up to date with our current asset roster, but to make them properly belong within the game world. The Nuke-Ops base may ultimately be a tiny chunk of the overall SS13 experience, but I'll be damned if it isn't a defining one. It's also a location that has the capacity to do one thing that I have always wanted to do. Purchase Property. You heard me right, you get to buy rooms now. The newly expanded Nuke-Ops base features, with @Mothblocks blessing, further expansions that you can purchase from your local Syndicate Uplink. Spend your TC, expand your capabilities, and utilize your expertise in order to create
the most mind-boggling disky heists there are.

Possible expansions to your terrorism suite include:
-Ordinance Lab
-Bio-Terrorism Lab
-Chemical Manufacturing Plant

Definite expansions to your Nuke-Ops Firebase include:
-Crew Bunks
-Lab Wing
-War Table
-Upgraded "Disembarkment" Bay"

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[4652d4bb63...](https://github.com/SmoSmoSmoSmok/tgstation/commit/4652d4bb63cec6f73bc46a0ea75d867d235107d1)
#### Saturday 2022-04-23 18:28:00 by Jolly

Updates The Derelict to some modern standards, also some turf edits (#66045)

Brings The Derelict up to speed with some of our new mapping tools and stuff.
This also places nearstation turf in certain areas, as well as general turf clean up.
Also cleans up the absurdly placed black holes of light that were over space tiles.
Girder/Grill spawners were placed in certain locations (mostly on external girlls).
I also remapped the main AI chambers SMES power to not go through the fucking wall, as a trade off, its no longer wired round start, and the two pieces of cable that are automatically in the room have been swapped out for two (2) five cables each. Its not enough to reach the main area, but god fuck wires running through walls.

As an aside, some of plating on the outside, walls include, does look weird being full bright like this. I'm neutral for the most part. Theres a weird fine balance that needs to be maintained with some of the areas being open to space, I've opted to keep lattice as nearstation and any thing plating and above as turfed (excluding plating that is solely in space).

I'll be redoing the turfs of this later, sprite wise.

Images

---
## [CrystalClearCC/Citadel-Station-13-RP](https://github.com/CrystalClearCC/Citadel-Station-13-RP)@[4d54e290db...](https://github.com/CrystalClearCC/Citadel-Station-13-RP/commit/4d54e290db51697d12fc54a6bbb0a376f43b7280)
#### Saturday 2022-04-23 20:45:08 by Zandario

Security TGUI (#3886)

* e

* Fuck it, I'm pushing it.

* Fuck you

* Refactored Brigdoors, updated their UI, does annoucements

Also updated logging a little bit and documented some things.

* Multitool sync

---
## [Perkedel/Kaded-fnf-mods](https://github.com/Perkedel/Kaded-fnf-mods)@[ec7d61debf...](https://github.com/Perkedel/Kaded-fnf-mods/commit/ec7d61debf9f5250887fc83a0c8c65124a5f4f3f)
#### Saturday 2022-04-23 21:07:26 by Joel Robert Justiawan

[skip ci] Staiabon

Move the startup toast say as a constant. yeah. lemme hand it here.

got new slogan idea, it's `Manifest the Future` or uhmm `Manifest your Future`. idk yeah. we've inspired this from:
- Hyundai IONIQ 5, Power Up your Future
- Sky, Manifest song

Ah Good idea!!! this is slogan change when all 3 came back yess!!!

Here's hitline. after you hit note, it'll appear exactly where strum you hit it & note position up and down was. We've inspired this silhouette from a VR Rhythm game about Viking drum timpani called `Ragnarock`. NO, there's `rock` in it. not Ragnarok, rag na ROCK. https://store.steampowered.com/app/1345820/Ragnarock/ yess! see video gameplay on YouTube wow.
TODO: skin the hitline.
basically we inspired this back again from Psyched note splash, but this time is simpler. just appear the mark, and fades to disappear in 1 second. easy! it also colors based on your press rating. perfect, great, good, almost, and terrible.

okay, here's the thing. how about you cancel currently running tween if there is when selected new week item or freeplay song item? see ummm where it was from, uhhh OH yeah Blammed Lights Psychedly. if the tween is still running it then be canceled first before running the new one. okay, that's for it. I have not yet evaluated the visual appeal for this change, but that should eliminate jlickles after you've ran through serveral different colored selections.

and here the BG Color tween for that. this interface makes sure you have those variables, okay one variable about it. Yeah, put the color tween into this thing.

we have fixed the blammed lights. also syndicated blammed light to playstate because if the haxe script state has to go through stage variable, it doesn't work at all. so yeah. syndicate function.

be dreaming!
Last Funkin Moments. ~~Enjoy the drops of funkin while it last~~ Manifest your Future

some design at this point may begin to include influence from Hyundai IONIQ 5. yeah, the Parametric Pixel headlamp and around.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[bd576e7a83...](https://github.com/mrakgr/The-Spiral-Language/commit/bd576e7a833df35c3b95d021116d967150aea642)
#### Saturday 2022-04-23 22:06:51 by Marko Grdinić

"8:25pm. I remembered how while Arrimus was doing the blade, he put the rail directly. I realized just now he could have used an isocurve and wanted to try it out. This feature is great.

I really love Moi.

https://www.rhino3d.com/features/quadremesh/

I've seen Rhino being linked to Moi several times. And it seems Rhino has Subdiv modeling tools. Here they are advertizing the quad remesher. It might be worth getting just for that.

Hmmm, it is only 300mb on Persia. Given my interests it might be worth checking out.

https://youtu.be/RIbsNurVdb0
An Introduction to SubD (Subdivision Surface Modelling) in Rhino3d v7

Rhino has spline based Subds!

That could be the best of all worlds.

https://youtu.be/RIbsNurVdb0

Rhino also has deformable Nurbs surfaces.

https://youtu.be/f24n2ijh2Vs
Rhino 7- when to use subd

https://youtu.be/f24n2ijh2Vs?t=178

You can convert subd to NURBs.

https://youtu.be/f24n2ijh2Vs?t=243

Does it not have the equivalent of planar in Moi?

https://youtu.be/f24n2ijh2Vs?t=353
> Don't make yourself insane trying to come up with subd topology in order to get this shape.

9:45pm. https://youtu.be/RIbsNurVdb0?t=2123

This is really interesting.

https://vimeo.com/362114742
QuadRemesh in the Rhino 7 WIP

Here is a vid on the quad remesh in Rhino.

10:10pm. The stuff towards the end where they turn a mesh into a subd object using the quad remesher is interesting.

https://youtu.be/HXBvVhvrQ18
Tsplines to Rhino 7's SubD

Let me watch this as well.

https://youtu.be/suv90ahXa5s
Transitioning from NURBS to T-Splines

https://community.foundry.com/discuss/topic/76334/t-splines-vs-subd
> Please can somebody explain to me what is so great about t-splines (not trolling, just ignorant). What does it offer that subd does not?

I am wondering this as well.

///

While this is true of the T-splines in the papers, the T-splines implementation (in the rhino plugin and fusion 360) is the surface type called T-NURCCs (confusing, I know..) So it's a relative of both catmull-clark subds and nurbs, and can have poles and n-gons.

To answer the original question, I think that there are a few reasons why you might use it. One big reason is that it is a subd-compatible surface that has a strong emphasis on NURBS compatibility. NURBS are useful if you want to do things like booleans, exactly cylindrical screw holes, precise wall thickness when you thicken/offset, and so forth. So if you're looking to manufacture the shapes you're modeling, T-splines can be very helpful there.

There are a few other things that are nice, like being able to have edgeloops that can just T-off, without getting a dimple in your surface like you would with a normal pentagon. Also, you can add more control points to a surface locally (like, insert an edge loop) without changing the smooth shape at all, whereas with normal subds you would either subdivide every face or change the shape of the smooth surface. That is more useful near the end of the modeling process. The tools are also more designed like NURBS tools, with a very strong emphasis on curve-based modeling, lots of ways to use curves that aren't common with subds, like tsPipe.

There are reasons not to use T-splines as well. The surface type is more complex, so it can be more work if you use the advanced features (if you don't, then it's just the same as a Subd or Nurbs). The creasing implementation is problematic at the moment, you often get creases where you don't want them, and changing the radius is not as nice as edge weighting. They might not be integrated into your favorite 3d modeler.. :). And you might not need any of the things they give you over subds - if you're mostly creating renderings rather than manufacturing objects in the real world, subds are simpler.

Please note that I am a bit biased, but I tried to be fair.. :)

///

https://computergraphics.stackexchange.com/questions/8482/problems-with-subdivision-surfaces

https://youtu.be/4nbC6__gZfg
Modeling a tub (extended) with T-Splines for Rhino

I didn't understand the answer. Let me watch this for a bit.

https://youtu.be/ljZCDzWrsS4
How to use T-splines for Rhino

Actually, let me watch this.

> It's not possible any more.

It seems that T splines are patented by Autodesk and can't be used anymore. If I want to give them a try, I should get Fusion 360.

https://youtu.be/IaLwNGPQijs
Fusion 360 VS Rhino, which is better

https://discourse.mcneel.com/t/why-nurbs-and-subd-are-not-back-and-forth-compatible/125621/21?page=2

It seems the t spline patent expires in 2024.

https://youtu.be/IaLwNGPQijs?t=544

InspirationalTuts have really great video scenes.

A lot of good comments on this vid.

https://youtu.be/pKLSTQcFTUI
5 Things For Starting CAD Drafting in Rhino7

https://youtu.be/pKLSTQcFTUI?t=560

The way this works is quite similar to Moi.

https://youtu.be/pKLSTQcFTUI?t=671

I keep reading that NURBS, T splines and Subdiv curves are isomorphic, so a workflow that converts between them should be feasible in Rhino.

https://youtu.be/pKLSTQcFTUI?t=825

These keys for ortho movement, I wonder if they would work in Moi?

Nope.

12pm. Let me close the extended session here. I am a bit excited about finding a way to use the subd workflow together with NURBS. I'll get Rhino tomorrow, but I do not really need it for the sake of dealing with the room. Since Rhino has the quad remesher it should be greatly suitable for making any kinds of props for games. I might want to import in it from Moi. I'll also get Zbrush tomorrow.

Everything is coming together nicely isn't it? The reason why finding this is so nice is because I am already familiar with subd from Blender, so rather than being a new thing, it is a straightforward extension of what I had before."

---
## [griwes/reaveros](https://github.com/griwes/reaveros)@[55b414821d...](https://github.com/griwes/reaveros/commit/55b414821d2595a5cf61f3af8a7a8f794d4e79ec)
#### Saturday 2022-04-23 22:28:23 by Michał 'Griwes' Dominiak

Initial implementation of ELF loading and linking.

This commit contains a toolchain crime - it makes the toolchain files
pretend that the target system is a Linux. This is because Clang's
driver is doing something extremely stupid and invoking the linking step
*through GCC* when it doesn't recognize the target, and it also does it
*incorrectly*, because --sysroot gets lost somewhere. Because we now
need to *correctly* link some shared objects, and because doing it
through ld.lld directly is much more of a pain than this hack, we'll do
the hack for this. *Before this is merged*, however, the branch should
also receive a commit that patches LLVM to understand
*-reaveros-{elf,kernel} target triples, but that is going to be way more
involved than I have time, energy, and space in this commit for.

This commit also modifies how blocking syscalls lock memory ranges; the
locks no longer persist across suspensions. This is because I'm also
adding a mapping unmap syscall which needs a unique ownership of a
mapping, and it was either this or making unmap itself blocking, and
making mappings have thread queues on their locks. I chose the simpler
approach. Also also, the mapping lock type is now a shared mutex, as it
should've been from the start.

Finally - the first actual userspace process will be a logger, not a
vasmgr. This is to bring the number of binaries that need to contain the
"send some pointers over a mailbox to a kernel thread" logging mechanism
to its bare minimum. This way, all the other processes will start by
immediately using the logger IPC protocol, which will make them simpler
in this regard.

---
## [mroyale/assets](https://github.com/mroyale/assets)@[f8c6a59b86...](https://github.com/mroyale/assets/commit/f8c6a59b8620e450998ac11cc1e3cf2873551801)
#### Saturday 2022-04-23 22:55:43 by Casini Loogi

Merge pull request #11 from Invader07/master

new world shit because redirectors a bitch (and so it can be put in the Fucking game)

---
## [HosTingle/Basic-Problems-solutions](https://github.com/HosTingle/Basic-Problems-solutions)@[3c9c361efa...](https://github.com/HosTingle/Basic-Problems-solutions/commit/3c9c361efa27cf6e6bbff685c786c2d898280cae)
#### Saturday 2022-04-23 23:15:04 by Gökdeniz Genç

The Love-Letter Mystery

James found a love letter that his friend Harry has written to his girlfriend. James is a prankster, so he decides to meddle with the letter. He changes all the words in the letter into palindromes.

To do this, he follows two rules:

He can only reduce the value of a letter by , i.e. he can change d to c, but he cannot change c to d or d to b.
The letter  may not be reduced any further.
Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.

Example

The following two operations are performed: cde → cdd → cdc. Return .

Function Description

Complete the theLoveLetterMystery function in the editor below.

theLoveLetterMystery has the following parameter(s):

string s: the text of the letter
Returns

int: the minimum number of operations
Input Format

The first line contains an integer , the number of queries.
The next  lines will each contain a string .

Constraints


 | s | 
All strings are composed of lower case English letters, ascii[a-z], with no spaces.

Sample Input

STDIN   Function
-----   --------
4       q = 4
abc     query 1 = 'abc'
abcba
abcd
cba
Sample Output

2
0
4
2
Explanation

For the first query, abc → abb → aba.
For the second query, abcba is already a palindromic string.
For the third query, abcd → abcc → abcb → abca → abba.
For the fourth query, cba → bba → aba.

---

