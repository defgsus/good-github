## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-26](docs/good-messages/2022/2022-04-26.md)


1,837,369 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,837,369 were push events containing 2,975,583 commit messages that amount to 221,270,809 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 42 messages:


## [DaemonTinadel/thewasteland](https://github.com/DaemonTinadel/thewasteland)@[59a018d95a...](https://github.com/DaemonTinadel/thewasteland/commit/59a018d95a11eaed40605e2dccb5b549c6c6e2ba)
#### Tuesday 2022-04-26 00:04:37 by Kirie Saito

NCR Minor Changes (includes Corporal Timelock) (#130)

* adds timelocks to NCR roles

* NCR minor changes

* adds master corporal pins (for RP)

* flavor change

* Update ncr.dm

* yeah that shotgun sucks ass

* Actually makes this shit work, I am an idiot

* typo

* Name was kinda dogshit, changed it

* one binos, not two

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[a0fa5ba3ce...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/a0fa5ba3ce25d019dafa88e1d606e079f7649cc6)
#### Tuesday 2022-04-26 00:37:03 by SkyratBot

[MIRROR] Updates Maps And Away Missions MD [MDB IGNORE] (#13095)

* Updates Maps And Away Missions MD (#66455)

* Updates Maps And Away Missions MD

Hey there,

This was outdated for a bit, so I decided to pretty it up and make a few things a bit more explicit.

I alphabetized the maps since we don't really prioritize one-over-the-other (except Meta now being the default map instead of the non-existent Box).

I also alphabetized Removed Station Maps, and removed the "outdated" (they are all outdated, or will definitely all be outdated by the time a reader reads this).

I elaborated a bit more on how station maps are loaded these days (correct me if I am wrong).

Standardized how we show code paths.

Gave explicit instructions on never using Dream Maker to map, and linking two programs that we tell anyone who wanders in on the Discord to use anyways (please do inform me if we should not do this- but Dream Maker just fucking sucks shit).

I also fixed up some language around the Away Missions part, and added a newer section for the Map Depot since I do not believe it is discussed elsewhere on the main repository (as well as a short warning on anyone who things they can get Phobos or something running out-of-the-box).

Alright, cool.

* Updates Maps And Away Missions MD

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [ItsProf-org/kernel_xiaomi-mt6768](https://github.com/ItsProf-org/kernel_xiaomi-mt6768)@[80120d27a3...](https://github.com/ItsProf-org/kernel_xiaomi-mt6768/commit/80120d27a39df9da1546e18894259fb7c3b804e1)
#### Tuesday 2022-04-26 00:54:52 by Peter Zijlstra

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
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[c5f0ea76e0...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/c5f0ea76e0fa1d1236fe04a2edaf6d9c047fc7c8)
#### Tuesday 2022-04-26 02:27:13 by SkyratBot

[MIRROR] Vim mecha changes [MDB IGNORE] (#12981)

* Vim mecha changes (#66153)

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

* Vim mecha changes

Co-authored-by: B4CKU <50628162+B4CKU@users.noreply.github.com>

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[8fcb269d8a...](https://github.com/UnderMybrella/usa/commit/8fcb269d8a23503b9a758020eade7cfb752d35cf)
#### Tuesday 2022-04-26 03:35:13 by MarkiSpider

Update 54 files @ Tue, 26 Apr 2022 03:35:11 GMT
This site update changes usa-home.html, .html, dont-push.html, LixianTV.html, employeeaccountabilitytimesignature-portal.html, cart.html, Jupiterandfriends.html, agentloginportal.html, the-asshats.html, illinois.html, corn-dm.html, thejackson5.html, gettingjiggywithit.html, legal.html, logout.html, girlofthe21stcentury.html, MichaelJackson.html, capitalism.html, fuckem.html, NerdFiction.html, terrorblycute.html, shatteredbysomeone.html, everyone.html, messenger.html, 914222-29151493191121139.html, evidence.html, evidence.html, woahhh.html, ohyouwouldlikethatwouldntyou.html, redacted.html, agencydirectory.html, karen6803.html, karen6804.html, 914222-5241612154525.html, lolgotyou.html, sexygoldarms.html, thefounders.html, the-baboonies.html, 2702-invincible2syndicate.html, case-directory.html, Imsorrymissjackson.html, 914222-1916151820192112124214513114.html, nebuchadnezzar.html, karen6816.html, cachow.html, karen6815.html, helpcenter.html, kriskringle.html, byebyebye.html, thekilleidoscope.html, para.docs-portal, suspect-hierarchy.html, karen6809.html, Rad_R.html

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[110d8d98b2...](https://github.com/UnderMybrella/usa/commit/110d8d98b269ef5213b5498617ae14a3cf9dab19)
#### Tuesday 2022-04-26 03:37:26 by MarkiSpider

Update 54 files @ Tue, 26 Apr 2022 03:37:24 GMT
This site update changes usa-home.html, .html, dont-push.html, LixianTV.html, employeeaccountabilitytimesignature-portal.html, cart.html, Jupiterandfriends.html, agentloginportal.html, the-asshats.html, illinois.html, corn-dm.html, thejackson5.html, gettingjiggywithit.html, logout.html, legal.html, girlofthe21stcentury.html, MichaelJackson.html, capitalism.html, fuckem.html, NerdFiction.html, terrorblycute.html, shatteredbysomeone.html, everyone.html, messenger.html, 914222-29151493191121139.html, evidence.html, evidence.html, woahhh.html, ohyouwouldlikethatwouldntyou.html, redacted.html, agencydirectory.html, karen6803.html, karen6804.html, 914222-5241612154525.html, lolgotyou.html, sexygoldarms.html, thefounders.html, the-baboonies.html, 2702-invincible2syndicate.html, case-directory.html, Imsorrymissjackson.html, 914222-1916151820192112124214513114.html, nebuchadnezzar.html, karen6816.html, cachow.html, karen6815.html, helpcenter.html, kriskringle.html, byebyebye.html, thekilleidoscope.html, para.docs-portal, suspect-hierarchy.html, karen6809.html, Rad_R.html

---
## [Stephen-M-Anderson/Olaf-the-Unhuggable](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable)@[bc58f228c5...](https://github.com/Stephen-M-Anderson/Olaf-the-Unhuggable/commit/bc58f228c5a30686431795bbddb5604d537ecc06)
#### Tuesday 2022-04-26 03:47:40 by Christian Morales

Ball Man is Better AND I fixed some other shit

The original implementation of Ball Man was dictated solely by whether or not your grounded. Undoing Ball Man is still dictated by grounded but becoming Ball Man is now determined by: Jumping, Grappling, or Zooming!

I also fixed some glitches with dashing. Namely this glitch: "if you press the dash button and no direction it will wait until the next direction you press then immediately dash." 

I also made a slight modification to zooming. Collisions no longer completely halt momentum, I wonder if we'll all like that or if we'll be changing it back because we're sliding around everywhere like a fucking greased hog.

---
## [sojourn-13/sojourn-station](https://github.com/sojourn-13/sojourn-station)@[2747557916...](https://github.com/sojourn-13/sojourn-station/commit/2747557916f2db8c94c80995c12a8516d7dbd351)
#### Tuesday 2022-04-26 04:58:24 by DimmaDunk

Drip megapack 100% real not fake 1 commit church buff speedmerge (#3188)

* Drip megapack 100% real not fake 1 commit church buff speedmerge

- Adds Justice, Pandemonica, Malina, Zdrada and Modeus alt styles for charming outfit
- Adds a black suit jacket with adjustable styles for the charming outfit
- Adds charming waistcoat for Malina/Cerberus drip
- Ports the Tojo Pants and Tojo Jacket from the mad dog of Shimano himself
- Ports black and red overcoat styles (Joker, Morningstar)
- New sprites for Prospector/Foreman lockers, Salvager lockers changed in appearance to rusty old ones for fluff
- Adds New Testament Knight Hardsuit RIG module for the church's New Testament Armaments Disk, a Divisor/Numerical joint effort in producing a combat-ready hardsuit. A pre-loaded version with flash, shield, jetpack and storage modules spawns on the Prime's office's altar. Same stats as the Combat Hardsuit.

* Adds Knight RIG module sprite

Solving merge conflicts.

* Catifies your SCAFs

SCAF helmet and Blackshield SCAF helmet given alternate styles with cat ears for that Halo drip.

---
## [SomeBoringNerd/someboringnerd.xyz](https://github.com/SomeBoringNerd/someboringnerd.xyz)@[3acc870c94...](https://github.com/SomeBoringNerd/someboringnerd.xyz/commit/3acc870c9443f1086149cdfd0679def3a20a3448)
#### Tuesday 2022-04-26 06:42:09 by A Boring Nerd

updated my projects

fuck you BGP, you fucking psycopath

e.txt : some random ips that tried to ssh into my webserver, feel free to ddos

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ce0aff7526...](https://github.com/tgstation/tgstation/commit/ce0aff7526158133acd1b53bd5d2d9d6ac9578f3)
#### Tuesday 2022-04-26 07:15:01 by GoldenAlpharex

Fixed Icebox's lower two z-levels not being included in the Map Compile action (#66503)

Did you know that you could currently put a bunch of random shit in the lower levels of icebox and the map compile would be none the wiser?

I sure did.

I hate that it's done manually this way, but honestly it's not worth refactoring the whole action to make it work differently.

Ensuring that the lower levels work properly is, in fact, a good thing.

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[9c120dddaf...](https://github.com/UnderMybrella/usa/commit/9c120dddaf650d1c7f087fd7f8cda10b638e0ffb)
#### Tuesday 2022-04-26 07:37:16 by MarkiSpider

Update 89 files @ Tue, 26 Apr 2022 07:37:13 GMT
This site update changes aretheyalium.html, logs.html, images.html, theoracle.html, michaeljackson.html, logs.html, dontpush.html, c-8-dickpicks.html, user.html, 914222-1952425161182025.html, zeusandfriends.html, thebannerborn.html, overview.html, reviews.html, dashboard.html, MatPat.html, idkbro.html, thecaptain.html, thedude.html, oopsalbangers.html, 914222-20513165181205.html, inhumanresources.html, 914222-195242514914101.html, ijustmadeyoulookunderthere.html, the-d_.html, user8118151241161251919.html, iinhumanresources.html, terfwar.html, departments.html, captainwhyareyoudoingthistome.html, moriarty.html, 914222-3116201914.html, 914222-3421144920.html, auth.html, cases.html, usa-home.html, .html, dont-push.html, LixianTV.html, employeeaccountabilitytimesignature-portal.html, cart.html, Jupiterandfriends.html, agentloginportal.html, the-asshats.html, illinois.html, corn-dm.html, thejackson5.html, gettingjiggywithit.html, logout.html, legal.html, girlofthe21stcentury.html, MichaelJackson.html, capitalism.html, fuckem.html, NerdFiction.html, shatteredbysomeone.html, terrorblycute.html, everyone.html, messenger.html, 914222-29151493191121139.html, evidence.html, evidence.html, woahhh.html, ohyouwouldlikethatwouldntyou.html, redacted.html, agencydirectory.html, karen6803.html, karen6804.html, 914222-5241612154525.html, lolgotyou.html, thefounders.html, sexygoldarms.html, the-baboonies.html, 2702-invincible2syndicate.html, case-directory.html, 914222-1916151820192112124214513114.html, Imsorrymissjackson.html, nebuchadnezzar.html, karen6816.html, cachow.html, karen6815.html, helpcenter.html, kriskringle.html, byebyebye.html, thekilleidoscope.html, para.docs-portal, suspect-hierarchy.html, karen6809.html, Rad_R.html

---
## [Pokye/rathena](https://github.com/Pokye/rathena)@[d617d9f083...](https://github.com/Pokye/rathena/commit/d617d9f08381442b14cb69da6ef5251a12817cd3)
#### Tuesday 2022-04-26 08:06:23 by Aleos

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
## [shiou0319/web-programming-exercise](https://github.com/shiou0319/web-programming-exercise)@[b7be7e95a1...](https://github.com/shiou0319/web-programming-exercise/commit/b7be7e95a1f92e665d5105446bc4b993fb1427b5)
#### Tuesday 2022-04-26 08:40:43 by shiou0319

Create exercise2

(0) Download the official NCKU logo 1 and Lucid Dreamer mp3 files, and store the files inthe directory “Media” under your home.
(1) Use the local file you just stored in the Media directory to insert the logo 1. Adjust the width of thelogo to 200.
(2) Use the link of logo 2 to insert the logo 2 directly. Adjust the width of the logo to 200. 
Add link in thelogo 2 and make it link to the homepage of NCKU (web.ncku.edu.tw).
(3) Use the mp3 file as the background music. Show the controller of the music. 
By default, make the music play automatically and muted while user open the page. (Tested by Edge)
(4) Embed this Youtube video in you page (https://www.youtube.com/watch?v=6V7oVQ05oSA). 
Make sure the video cannot be played in Fullscreen. Set the width to 640 and the height to 360.
(5) Create a hyperlink “Email me”. After being clicked, the link will open your default email application and tend to send an email to you student email account.
(6) Create a hyperlink “Contact NCKU”. After being clicked, the link will open your default phone application and tend to call NCKU (06) 275-7575.
(7) Add an unordered list, “My favorite sites:”, and an ordered list under Facebook for the following items:
˙Youtube
˙Wikipedia
˙Amazon
˙Facebook
A. Instagram
B. WhatsApp
C. Oculus VR
(8) Create following table by <table>. (note: border="1")
Fruit Juice Drinks and Meals
Fruit Juice Drinks
Apple Orange Screwdriver
Meal Breakfast 0 1 0
Lunch 1 0 0
Dinner 0 0 1
Total 1 1 1

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[6bb5cdfad0...](https://github.com/pariahstation/Pariah-Station/commit/6bb5cdfad0e53897a72dfee1126553d62d92b4e3)
#### Tuesday 2022-04-26 08:56:57 by PariahBot

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
## [Atom-X-Devs/android_kernel_xiaomi_sm7325](https://github.com/Atom-X-Devs/android_kernel_xiaomi_sm7325)@[6e56741974...](https://github.com/Atom-X-Devs/android_kernel_xiaomi_sm7325/commit/6e56741974530b78bc73787e0d754e25b226cd8c)
#### Tuesday 2022-04-26 09:33:26 by Daniel Vetter

dma_resv: prime lockdep annotations

Full audit of everyone:

- i915, radeon, amdgpu should be clean per their maintainers.

- vram helpers should be fine, they don't do command submission, so
  really no business holding struct_mutex while doing copy_*_user. But
  I haven't checked them all.

- panfrost seems to dma_resv_lock only in panfrost_job_push, which
  looks clean.

- v3d holds dma_resv locks in the tail of its v3d_submit_cl_ioctl(),
  copying from/to userspace happens all in v3d_lookup_bos which is
  outside of the critical section.

- vmwgfx has a bunch of ioctls that do their own copy_*_user:
  - vmw_execbuf_process: First this does some copies in
    vmw_execbuf_cmdbuf() and also in the vmw_execbuf_process() itself.
    Then comes the usual ttm reserve/validate sequence, then actual
    submission/fencing, then unreserving, and finally some more
    copy_to_user in vmw_execbuf_copy_fence_user. Glossing over tons of
    details, but looks all safe.
  - vmw_fence_event_ioctl: No ttm_reserve/dma_resv_lock anywhere to be
    seen, seems to only create a fence and copy it out.
  - a pile of smaller ioctl in vmwgfx_ioctl.c, no reservations to be
    found there.
  Summary: vmwgfx seems to be fine too.

- virtio: There's virtio_gpu_execbuffer_ioctl, which does all the
  copying from userspace before even looking up objects through their
  handles, so safe. Plus the getparam/getcaps ioctl, also both safe.

- qxl only has qxl_execbuffer_ioctl, which calls into
  qxl_process_single_command. There's a lovely comment before the
  __copy_from_user_inatomic that the slowpath should be copied from
  i915, but I guess that never happened. Try not to be unlucky and get
  your CS data evicted between when it's written and the kernel tries
  to read it. The only other copy_from_user is for relocs, but those
  are done before qxl_release_reserve_list(), which seems to be the
  only thing reserving buffers (in the ttm/dma_resv sense) in that
  code. So looks safe.

- A debugfs file in nouveau_debugfs_pstate_set() and the usif ioctl in
  usif_ioctl() look safe. nouveau_gem_ioctl_pushbuf() otoh breaks this
  everywhere and needs to be fixed up.

v2: Thomas pointed at that vmwgfx calls dma_resv_init while it holds a
dma_resv lock of a different object already. Christian mentioned that
ttm core does this too for ghost objects. intel-gfx-ci highlighted
that i915 has similar issues.

Unfortunately we can't do this in the usual module init functions,
because kernel threads don't have an ->mm - we have to wait around for
some user thread to do this.

Solution is to spawn a worker (but only once). It's horrible, but it
works.

v3: We can allocate mm! (Chris). Horrible worker hack out, clean
initcall solution in.

v4: Annotate with __init (Rob Herring)

Cc: Rob Herring <robh@kernel.org>
Cc: Alex Deucher <alexander.deucher@amd.com>
Cc: Christian König <christian.koenig@amd.com>
Cc: Chris Wilson <chris@chris-wilson.co.uk>
Cc: Thomas Zimmermann <tzimmermann@suse.de>
Cc: Rob Herring <robh@kernel.org>
Cc: Tomeu Vizoso <tomeu.vizoso@collabora.com>
Cc: Eric Anholt <eric@anholt.net>
Cc: Dave Airlie <airlied@redhat.com>
Cc: Gerd Hoffmann <kraxel@redhat.com>
Cc: Ben Skeggs <bskeggs@redhat.com>
Cc: "VMware Graphics" <linux-graphics-maintainer@vmware.com>
Cc: Thomas Hellstrom <thellstrom@vmware.com>
Reviewed-by: Thomas Hellstrom <thellstrom@vmware.com>
Reviewed-by: Christian König <christian.koenig@amd.com>
Reviewed-by: Chris Wilson <chris@chris-wilson.co.uk>
Tested-by: Chris Wilson <chris@chris-wilson.co.uk>
Signed-off-by: Daniel Vetter <daniel.vetter@intel.com>
Link: https://patchwork.freedesktop.org/patch/msgid/20191104173801.2972-1-daniel.vetter@ffwll.ch
Signed-off-by: Divyanshu-Modi <divyan.m05@gmail.com>

---
## [Kortom-Tom/Furland](https://github.com/Kortom-Tom/Furland)@[3c68d2cca6...](https://github.com/Kortom-Tom/Furland/commit/3c68d2cca6641db9cc6e18dc8b940fb42da295f2)
#### Tuesday 2022-04-26 10:17:53 by Kortom-Tom

Stupid twitter joke

A friend of mine was complaining he was not showing up in my graph, we made a joke about their being code in the product banning him from all bubbles. This is an nod to the joke.

Context: https://twitter.com/Nican/status/1518893427177361409

---
## [cucumbersec/febslisity.github.io](https://github.com/cucumbersec/febslisity.github.io)@[870bcc04d9...](https://github.com/cucumbersec/febslisity.github.io/commit/870bcc04d9d8b7a89838151f7869c4b7e51254b5)
#### Tuesday 2022-04-26 11:10:44 by CUCUMBER SEC

README.md

==================================================================================================

DESCRIPTION:

EPITOME is a beautifully crafted free resume and personal portfolio website template. It is modern, 
trendy and features a visually attractive design. An ideal website template for creative 
professionals and freelancers who want to create an online presence that would stand out from 
the average. Epitome has all the important elements of an effective resume personal portfolio 
website template: an awesome fullscreen hero banner, about and qualification section, services, 
portfolio, testimonial and contact section. Epitome is also mobile and retina ready. 
It will look great on any devices from mobile to desktop and on any screen resolutions.

==================================================================================================


LICENSE:

This free resource is provided by Styleshout.com and is free to use in 
both personal and commercial projects.


Rights:
-------

You are permitted to use this free resource in any number of personal and commercial projects for 
yourself or a client. You may modify the resource according to your requirements and include them 
in your projects under the following condition - you MUST give appropriate credit, provide an 
attribution link to styleshout.com.


Prohibitions:
-------------

You are not permitted to resell or redistribute(even for free) the resource "as is" without 
prior consent. If you would like to republish or promote this resource on your site, please 
link back to the appropriate resource page on styleshout.com where users can find the download 
and not directly to the download zip file.


Attribution: 
------------

You must include a credit link to our website(https://www.styleshout.com) somewhere on your site. 
We prefer the footer credit that comes with the template but you are still free to move it 
somewhere else.



If you have any questions about the License, feel free to contact us.


-----------------------------------------------------------------------------------------------------


REMOVING THE ATTRIBUTION LINK:

We understand that there are situations where you want to use our templates without 
the crediting obligation. If that's your case, you can always send us a 
credit removal fee of 10 USD through Paypal. This will allow you to use a single 
template attribution/credit link free on ONE DOMAIN name.

You can send your payments through Paypal to this address: ealigam@gmail.com or
visit our attribution removal page: https://www.styleshout.com/attribution-free/ 
and click the pay button on the page.

If possible, kindly send us the site's url where the template is being used. 
Also, keep your Paypal receipt as proof of payment and your good to go.


------------------------------------------------------------------------------------------------------ 


SUPPORT:
    
Since EPITOME is distributed for free, support is not offered. EPITOME is coded according 
to current web standards and we did our best to make the template easy to use and modify.
If you have minimum web development experience, you can easily modify the template. 
However, If you're still new to HTML and CSS, I suggest that you visit the 
following tutorials:

 - https://webdesign.tutsplus.com/courses/30-days-to-learn-html-css
 - http://learn.shayhowe.com/html-css/

These will teach you the essentials of HTML and CSS. In addition, if you want to include
jQuery in your skill-set, you can also check out these tutorials: 

 - https://code.tutsplus.com/courses/30-days-to-learn-jquery
 - http://try.jquery.com/


------------------------------------------------------------------------------------------------------ 


GET THE LATEST VERSION:

We update our templates on a regular basis so to make sure that you have the latest version, 
always download the template files directly on our website(https://www.styleshout.com/)



-------------------------------------------------------------------------------------------------------


SOURCES AND CREDITS:

I've used the following resources as listed.

Fonts:
 - Lora Font (https://fonts.google.com/specimen/Lora)
 - Roboto Font (https://fonts.google.com/specimen/Roboto) 
 - Frank Ruhl Libre Font (https://fonts.google.com/specimen/Frank+Ruhl+Libre)

Icons:
 - Font Awesome (https://fontawesome.com/)
 - Iconmonstr (https://iconmonstr.com/)
 

Stock Photos and Graphics:
 - Unsplash.com (https://unsplash.com/)
 
Javascript Files:
 - JQuery (http://jquery.com/)
 - Modernizr (http://modernizr.com/)
 - Masonry JS (https://masonry.desandro.com/)
 - ImagesLoaded (https://imagesloaded.desandro.com/)
 - Slick slider (http://kenwheeler.github.io/slick/)
 - Animate On Scroll (https://michalsnik.github.io/aos/)
 - Pace JS (https://github.hubspot.com/pace/docs/welcome/)

-------------------------------------------------------------------------------------------------------


Thanks for downloading from Styleshout :)

---
## [rohittembhurne2194/ICTSBMALL_ULB](https://github.com/rohittembhurne2194/ICTSBMALL_ULB)@[c5db3a260a...](https://github.com/rohittembhurne2194/ICTSBMALL_ULB/commit/c5db3a260af1c12297a38529fd2a7c49a2ee6edb)
#### Tuesday 2022-04-26 11:19:16 by umeshl@appynitty.com

Changes done by Umesh The Future Billionaire Persone and its Me Thanku so Much god for giving me this new oppourtunity for changing My life as trader and i will be definitly success in this jorney now i never give up on this opportinty or trading careear god always blessed me  Jay shree Mahakar Har Har Mahadev

---
## [input-output-hk/ouroboros-network](https://github.com/input-output-hk/ouroboros-network)@[275a5cca48...](https://github.com/input-output-hk/ouroboros-network/commit/275a5cca48e6fed300cfe3882ae5b131e8cef110)
#### Tuesday 2022-04-26 13:59:41 by Nicholas Clarke

Integrate the Babbage ledger era.

- The BabbageEra is imported from cardano-ledger-babbage and added to
  `CardanoEras` etc.
- A new Babbage era is added to the Shelley codebase, and made an
  instance of `ShelleyBasedEra`. Note the slightly weird
  `TranslationContext` - we need to use the Alonzo translation context
  because of the assumption (in `ShelleyBasedEra`) that the translation
  context is equal to the `AdditionalGenesisConfig`. The latter is a
  diff from `Shelley`, whereas the former is a diff from the previous
  era.

  TODO We should drop this assumption and correct the relationship
  between these things.
- We introduce a new class, `SupportsTwoPhaseValidation`, to reuse code
  for dealing with 2-phase validation in Alonzo and subsequent eras.
- Add standard boilerplate patterns for the Babbage era (particularly in
  Ouroboros.Consensus.Cardano.Block).
- We add additional translation code to translate from Alonzo to
  Baggage. This is slightly more complex than usual, since it must also
  translate from TPraos to Praos. It's generally formulaic, however.
- New protocol versions are introduced supporting the Babbage era.
- `protocolInfoCardano` is expanded with configuration for
  Babbage/Praos. Again, this is largely straightforward.
- Block forging code for Praos is now uncommented, since there is a
  Praos era to work on.
- The block forging code for the TPraos eras is adjusted to add a "skip"
  at the end, for the Babbage era. Honestly, this is rather ugly, but
  it's the simplest approach right now.

---
## [magit/magit](https://github.com/magit/magit)@[ab801de538...](https://github.com/magit/magit/commit/ab801de53827a232b7806362fb08ca804f27c6d0)
#### Tuesday 2022-04-26 14:03:21 by Jonas Bernoulli

magit-section-context-menu: Support non-section branches

We use section keymaps to implement context-sensitive menus but
branches are not always represented using sections.  To support
such "painted branches" anyway use fake sections, which closely
mirror the commit section in which the click occurred.

This admittedly is ugly and somewhat risky, but seems to work well.
`magit-section-update-highlight' would break due to this hack, so
we avoid calling it.  If it turns out that things also break due
to this kludge, then we might have to revert.

---
## [newstools/2022-sabc-news-online](https://github.com/newstools/2022-sabc-news-online)@[0e45dd83ac...](https://github.com/newstools/2022-sabc-news-online/commit/0e45dd83ac6573950923ce989bce0ecc37e3a5c0)
#### Tuesday 2022-04-26 14:38:39 by Billy Einkamerer

Created Text For URL [www.sabcnews.com/graphic-content-siyanda-khumalo-gets-life-for-murder-of-his-ex-girlfriends-children/]

---
## [Gnaarf/Songbook](https://github.com/Gnaarf/Songbook)@[48d40110ed...](https://github.com/Gnaarf/Songbook/commit/48d40110ed4688bc88b0ab82d0570c3d343ea9bb)
#### Tuesday 2022-04-26 14:54:07 by Jan-Cord

added 7 songs + renamed strumming functions +
- 3 improvements to strumming pattern: 1) changed to monospace font, 2) added function to add a header for strumming patterns, 3) function names more descriptive
- added/fixed some chords to chords.tex: added A7sus4, Dadd4/Fsharp, E7, and other voicings for B, Csus2, D, E and Em, and fixed A-2
- added songs: Absolutely (Nine Days), Fahrerflucht (Trailerpark), Ich am Strand (Die Ärzte), Nicht Wecken (Alligatoah) + Tabs, Slim Pickens Does The Right Thing and Rides the Bomb to Hell (The Offspring), Trauerfeier Lied (Alligatoah) + Tabs, Trostpreis (Alligatoah) + Tabs
- hid 2 songs (they annoyed me): American Idiot (Green Day), Hitler muss immer wieder sterben (Mono & Nikitaman) (added and then hidden shortly after)
- added chords to last verse in achja-mrhurleydiepulveraffen.tex
- added Intro and strumming pattern to achso-dasniveau.tex
- added strumming patterns in text to applausapplaus-sportfreundestiller.tex
- fixed chords in immrmeeseeks-royishgoodlooks.tex
- removed unused file (jonnydicklegs-mollylewis.tex was renamed into johnnydicklegs-mollylewis.tex (with a h))
- fixed meter in mollymalone-traditional-tabs.tex
- 5 more minor improvements: 1) improved chord placement in Bridge in alamierda-skap.tex, 2) longer songSnippet in achso-dasniveau.tex, 3) line break in derkodex-mrhurleyunddiepulveraffen.tex to make clear how long to stay on one chord, 4) added comments to musixguitartab.tex, 5) added function "\optionalChord{}",

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[ce40170526...](https://github.com/treckstar/yolo-octo-hipster/commit/ce401705260e41e529f6b991b83752ee6658f587)
#### Tuesday 2022-04-26 15:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [ackwell/ironworks](https://github.com/ackwell/ironworks)@[56ce970b82...](https://github.com/ackwell/ironworks/commit/56ce970b829b58eb921be6f2bf08b9ba9722b0c1)
#### Tuesday 2022-04-26 15:57:42 by ackwell

Do cursed shit to make error handling at least kinda manageable I guess

---
## [RandomGamer123/tgstation](https://github.com/RandomGamer123/tgstation)@[a137c15a79...](https://github.com/RandomGamer123/tgstation/commit/a137c15a790bc8242a1ccd70bb6570d0278833c0)
#### Tuesday 2022-04-26 16:13:54 by Vladin Heir

Kills research scanner toggle, moves functionality to examine_more. Improves research scanner code and fixes a modsuit bug. (#66415)

* FINALLY. I'VE KILLED IT. I CAN LIVE MY LIFE NOW.

I hate the fucking Toggle Research Scanner action button so god damn much. Why the fuck would I ever not want this to be on? Why do you think I'm wearing the fucking goggles? That stupid button is so annoying to use. Even if I'm NOT using the research scanner aspect of the goggles, that little shit floats there, taking up space on my screen, taunting me.

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[54403a1ca0...](https://github.com/Timberpoes/tgstation-nxt/commit/54403a1ca0a1d83302430bbb54a0d6bc561f0098)
#### Tuesday 2022-04-26 16:14:37 by FinancialGoose

Fixes conveyor runtime (#65788)

Conveyor would runtime whenever it is right clicked with an item

Fixes #64595 (Runtime on conveyor for right clicking)

fixes a runtime with conveyor where right clicking it with any item would cause a runtime

Mothblocks rant from the issue report below, you've been warned:

Because right-clicking in BYOND is horse-shit. It pipes it all through the normal Click and only tells you it's a right-click through a flag. This means that on anything that isn't prepared, right-clicking is the same as left-clicking, which is terrible UX that only exists in SS13.

Nothing should return ..() from attackby_secondary, because the default is the legacy behavior of making right-click pass as left-click (which I want to kill ASAP, once nothing uses the stupid flags anymore).

Remove else return ..(), and make this whole thing do return SECONDARY_ATTACK_CANCEL_ATTACK_CHAIN.

---
## [cygnus-rom/vendor_cygnus](https://github.com/cygnus-rom/vendor_cygnus)@[53ea88a4b9...](https://github.com/cygnus-rom/vendor_cygnus/commit/53ea88a4b9048bb94e6865bf76ab16caee39189e)
#### Tuesday 2022-04-26 17:16:19 by Dhruv

vendor: Include SDClang

Fuck you aosp clang and your stupid werrors

---
## [theRealSherapat/CompSA](https://github.com/theRealSherapat/CompSA)@[8c9892a923...](https://github.com/theRealSherapat/CompSA/commit/8c9892a92378a79db6ff4c97458a241aab8c57da)
#### Tuesday 2022-04-26 17:28:32 by theRealSherapat

Made peace with determinism in my implementation (unless Frank wants to
help me speed up the experiment-running) — admitted to myself I made
some brainfarts where I was sure the problem and root of
anti-determinism lied otherwise than where it lied (Invokes and multiple
FixedUpdate()-threads). I thus and with this rid myself of (almost) all notions and focus of (anti-) determinism in my system, and move on with my life towards experiments, writing, describing, and explanation of what I have done in my master's thesis work. Also, from now on, I will only write in the Git Commit log WHAT I have done given a piece of work or commit; and conversely I will in my Rescherecherese diary write only MY THOUGHTS and BELIEFS about what I did in a given piece of work or commit. So bye, thoughts and beliefs, hunches, or speculations — say hello to the Reschercheshsehes Diary.

---
## [Slothy-lol/AkarisSubnauticaMods](https://github.com/Slothy-lol/AkarisSubnauticaMods)@[3dcda91943...](https://github.com/Slothy-lol/AkarisSubnauticaMods/commit/3dcda91943088fa70139f6da1a793843d42334f3)
#### Tuesday 2022-04-26 17:35:47 by Slothy-lol

fuck your weird formatting and probably mine as well visual studio gets to decide

---
## [itonges/crawl](https://github.com/itonges/crawl)@[af92d4a5d6...](https://github.com/itonges/crawl/commit/af92d4a5d6ba2f841e8bfdf8639f77a784fcaeae)
#### Tuesday 2022-04-26 18:04:25 by Nicholas Feinberg

Make Hell Knights evil again (catern)

Lost this when they lost Pain.

Slightly hacky.

---
## [32th-System/deltarune_repainted](https://github.com/32th-System/deltarune_repainted)@[e1cffc0b27...](https://github.com/32th-System/deltarune_repainted/commit/e1cffc0b27407f79be278e0d7702edd359057c52)
#### Tuesday 2022-04-26 18:23:23 by Fatfuck22

Cerberus part 4 (clock graphics)

… Time is a tool you can put on the wall
Or wear it on your wrist
The past is far behind us
The future doesn't exist (oh)
… What's the time?
Its a quarter to nine, time to have a bath
What do you mean, we're already clean
Scrub, scrub, scrub 'til the water's brown
… Time is a ruler to measure the day
It doesn't go backwards, only one way
Watch it go round like a merry go round
Going so fast like a merry go round
… Let's go on a journey
A journey through all time
The time is changing all the time
It's time to go to time
… But we don't really want to
We're going to miss our show
Don't be stupid, friend
C'mon, it's time to go
… Time is old like the Victorian times
With cobbles and plague and speaking in rhymes
With cobbles and chimneys a simpler time
With cobbles and sawdust and batteries and slime
… This tree that is old has circles inside
The tree that is older has shriveled and died
The apple that is fresh is ripe to the core
And I rot over time and I'm not anymore
… Time can be told by the moon or the sun
But time flies fast when you're having fun
There's a time and a place for mucking around
Like birthdays
And camping
I'm friends with my dad
… And then what happened after the olden days?
… Time went new and got old like history
Stuff from the past went into a mystery
An old man died
But look a computer
Everything's cool
It's the future!
… Time is now, the future anew
And look at all of the wonderful things you can do
With gadgets and gizmos and email addresses
My dad is a computer
… Look at the time!
… It's quarter to eight, there's fish on my plate
It's twenty past day, there's fish on my tray
It's eleven to twelve, there's fish in the bath
It's nine thirty, there's fish everywhere, fish everywhere?
… Now you can see the importance of time
It helps us make pizza, it keeps things in line
But when did it start?
And when will it stop?
Time is important and I am a clock
If we run out of time
Then where does it go?
Is time even real?
Does anyone know?
Maybe time's just a construct of human perception
An illusion created by-
… Meh! meh! meh! meh!
Meh! meh! meh! meh!
Meh! meh! meh! meh!
Meh! meh!
… Sunrise, sunset, night and day
The changing seasons, the smell of hay
Look at your hair grow, isn't it strange?
How time makes your appearance change
… Make it stop!
It's out of my hands, I'm only a clock
Don't worry, I'm sure you'll be fine
But eventually everyone runs out of time

---
## [xexyl/mkiocccentry](https://github.com/xexyl/mkiocccentry)@[2020812c4d...](https://github.com/xexyl/mkiocccentry/commit/2020812c4d8969ff6c4f18ac48429d94e5f702f8)
#### Tuesday 2022-04-26 19:04:27 by Cody Boone Ferguson

Lexer and parser ironically declare they're ugly

This is done by changing the (yy|YY) prefix to (ugly|UGLY) in the lexer
and parser. As the following comment says:

    /*
     * As we utterly object to the hideous code that bison and flex generate we
     * point it out in an ironic way by changing the prefix yy to ugly_.
     */

This is done in flex and bison via:

    %option prefix="ugly_"
    %define api.prefix {ugly_}

respectively. This creates an ironic statement in the lexer:

    #define ugly_lex_ALREADY_DEFINED

and an ironic statement in the C pre-processor in the parser:

    #if ! defined UGLY_STYPE && ! defined UGLY_STYPE_IS_DECLARED
    # define UGLY_STYPE_IS_DECLARED 1

which is to say that both the lexer and parser actually declare that
they're ugly! :))

For the curious:

    $ grep -ic ugly jparse*ref.[ch]
    jparse.ref.c:108
    jparse.tab.ref.c:34
    jparse.tab.ref.h:24

which is a huge amount of ugliness (though it's much more ugly than what
it admits :) )!

As well I've made a minor change to sorry.tm.ca.h that's not even worth
describing.

---
## [igloo1505/matrixInMotion](https://github.com/igloo1505/matrixInMotion)@[96569ab78f...](https://github.com/igloo1505/matrixInMotion/commit/96569ab78f35c41df80726b3ff5b9616bd2d8b6a)
#### Tuesday 2022-04-26 19:12:00 by Andrew Iglinski

FUCKKKKKKK JUPYTER. FUCK JUPYTER. F.U.C.K. J.U.P.Y.T.E.R. 19 HOURS, ZERO VISIBLE OUTPUT AND A NOW MUTILATED REPO... FUCKKKKKKKK JUPYTER. HOW DIFFICULT IS IT TO HANDLE A FUCKING DATA VISULIZATION ERROR IN A DATA SCIENCE FOCUSED FRAMEWORK WITH LITERALLY ANY SORT OF VISIBLE OUTPUT... A LINE NUMBER EVEN? EVERY FUCKING PERSON THAT CONTRIBUTED TO JUPYTER IS NOT FIT TO REPRODUCE AND SPREAD THAT SHIT GENETIC STRAIN. FUCKKK YOU ARE MORONS

---
## [glennbarrett/Mind-Expanding-Books](https://github.com/glennbarrett/Mind-Expanding-Books)@[4e8712a154...](https://github.com/glennbarrett/Mind-Expanding-Books/commit/4e8712a154e98ffdf23093b46d770fa20fc3bca6)
#### Tuesday 2022-04-26 19:14:04 by bschlagel

Added "Pilgrim at Tinker Creek"

Really wonderful book about nature, the passage of time, and really paying attention to the world around you. The whole book could almost be categorized as prose poetry; it's not a large volume but took me a while to get through just due to the sheer density of lush and sensitive description. It chronicles a year in which both nothing and everything seems to happen; Dillard mostly hangs out around her home and its backyard creek (or at least, the book is constrained mostly to these experiences) but manages to evoke transcendent beauty and spirituality, capturing cycles of predator and prey, weather, and her own reactions to the unfolding of life in its infinite forms.

---
## [glennbarrett/Mind-Expanding-Books](https://github.com/glennbarrett/Mind-Expanding-Books)@[4d0e21a999...](https://github.com/glennbarrett/Mind-Expanding-Books/commit/4d0e21a99952ca434acec05b346ef75ce2147bd9)
#### Tuesday 2022-04-26 19:14:04 by bschlagel

Add Bolo'bolo

* Added "Bolo'bolo"

Weird and wonderful little book that proposes a whole societal structure of radical autonomous communities — complete with an invented language to describe the parts of this new community vision, and their machinations. Very eye-opening; in some ways it's a strange and impractical utopian dream; in others it's a sobering and critical plea for reorganizing society along lines of greater sustainability and social cohesion. Very interesting whichever way you look at it!

---
## [glennbarrett/Mind-Expanding-Books](https://github.com/glennbarrett/Mind-Expanding-Books)@[46feb27687...](https://github.com/glennbarrett/Mind-Expanding-Books/commit/46feb27687f389f8d6246e7fbd9858b7a9d183f7)
#### Tuesday 2022-04-26 19:14:04 by bschlagel

Added "Le Ton beau de Marot" (#150)

An incredible book about the art of translation, and a million other very welcome tangents. Hofstadter spins endless threads of ideas around a fascinating central premise: that a specific favorite poem of his, by a fairly obscure 16th century French poet, can spark an infinite variety of translations. There are 80+ of these translations sprinkled throughout the book, from friends and family, students and colleagues, noted translators and computer programs (and many by Hofstadter himself). Among them, a feast of academic lessons and personal reflections interwoven into a testament to the complexity and magic of translation and a whole lot of fascinating problems posed by language, literature, cognition and more. I've owned Hofstadter's infamous Gödel, Escher, Bach for a few years now, and still haven't finished swashbuckling my way through it — but I found this one thematically related yet more accessible, a great entrance point to a capacious and curious mind.

---
## [brooje/Yogstation](https://github.com/brooje/Yogstation)@[3782992f24...](https://github.com/brooje/Yogstation/commit/3782992f2413350b8750a12771dc15a55a1e4346)
#### Tuesday 2022-04-26 20:11:42 by hannuwu

map patch improvements (and FUCK YOU MINING TURTLE)

---
## [pariahstation/Pariah-Station](https://github.com/pariahstation/Pariah-Station)@[e16b9d82d0...](https://github.com/pariahstation/Pariah-Station/commit/e16b9d82d06f0db1934f7a7ed6cbccb79a4851b3)
#### Tuesday 2022-04-26 20:36:00 by Kapu1178

Fuck you TGUI. You suck fuck. Stylemistake, work on your Ace Combat thing instead. Please. (#659)

---
## [Valencia96/Project_Jane](https://github.com/Valencia96/Project_Jane)@[a8466b0fcb...](https://github.com/Valencia96/Project_Jane/commit/a8466b0fcb5fd9e191d3230d46e432dd22e4a57d)
#### Tuesday 2022-04-26 20:49:45 by Eldwitch

IT WORKS AGAIN FACKIN' HELL

balls in my mouth balls in my mouth balls in my mouth god I hate it here I'm so gay and there ain't nothing to do with it hhhhhhHHHHHHHH

---
## [Ajay3450/ILPM](https://github.com/Ajay3450/ILPM)@[73896a5df2...](https://github.com/Ajay3450/ILPM/commit/73896a5df28e59f9274cbfc67e3955ef3dc1ad64)
#### Tuesday 2022-04-26 21:30:31 by RosiYY

ILPM Chiptune Music

Changed all legal stage and menu music as follows

Yoshi's:
Super Mario World Atheltic Theme
Fortuna (Starfox)
Super Mario Bros 3 Athletic Theme
Burning Rich Girl (Shantae)
Angel Island Zone Act 1 (Sonic 3)

Meadows:
Cloud Tops (Minish Cap)
Zelda 2 Overworld Theme
Forest (Wizards and Warriors)
Emerald Hill Zone (Sonic 2)
Strike the Earth! (Shovel Knight)
The Great Sea 8-bit (Hyrule Warriors)
Twilight Field 8-bit (Hyrule Warriors)

Cavern:
Oil Ocean Zone (Sonic 2)
Mystic Cave (Sonic 2)
Temple (Zelda 2)
Metal Crusher (Undertale)
Inside the Castle (Wizards and Warriors)
Spider Dance (Undertale)
Streets of Desolation (Batman NES)

Dreamland:
Fever (Dr. Mario)
Underwater (Mario 3)
Outside the Castle (Wizards and Warriors)
Webfoot DROD Level 2
Steam Gardens Sherm 8-Bit ver (Mario Odyssey)
Comix Zone Level 1
Full Steam Ahead (Spirit Tracks) 8-bit (Hyrule Warriors)

GHZ:
Hydrocity Zone Act 2 (Sonic 3)
Chemical Plant Zone (Sonic 2)
Battle Theme 4 (Shining Force)
CORE (Undertale)
Mach Rider
Battle with Egg Dragoon (Sonic)

Smashville:
Aquatic Ruin Zone (Sonic 2)
Hyrule Town (Minish Cap)
Hello Happy Kingdom (Mario RPG)
Webfoot DROD Level 1
Casino Park - 8-Bit ver (Sonic Heroes)
Angel Island Zone REMIX (Sonic 3)

Battlefield:
Tal Tal Heights (Link's Awakening)
The Dark World (Link to the Past)
Battle Theme 5 (Shining Force)
Battle Against a True Hero (Undertale)
(5 freq) Megalovania (Undertale)
Asgore's Theme (Undertale)
Webfoot DROD Level 9
Boss (Sonic 2)

Stadium:
Battle Vs Lance/Red (Pokemon G/S/C)
Battle Vs Elite Four (Pokemon G/S/C)
Battle Vs Champion (Pokemon G/S/C)
Spear of Justice (Undertale)
Death by Glamour (Undertale)
Game (Persona 4)
Battle Theme 3 (Shining Force)

Crateria:
Hyrule Castle (Link to the Past)
Dark World Mountain Forest (Link to the Past)
Underworld (Mario 2)
Bonetrousle (Undertale)
Stone Tower Temple - NSF Ver (Majora's Mask)
Webfoot DROD Level 3
Deku Palace - NSF version (Majora's Mask)
Strike the Earth - Dj CUTMAN (Shovel Knight)

Menu:
IceCap Zone Act 2 (Sonic 3)
Casino Night Zone (Sonic 2)
Zelda 2 Indoors Theme
Iced Land (Mario 3)
Grass Land (Mario 3)
Headquarters (Shining Force)
Webfoot DROD Menu
I forgot my shovel (DJ Cutman)
Dreams of Love and Literature (Doki-Doki Literature Club)

Victory Theme - Zelda 1 Credits

---
## [Strwb/ScrabbleMaster](https://github.com/Strwb/ScrabbleMaster)@[63b906e7bb...](https://github.com/Strwb/ScrabbleMaster/commit/63b906e7bb835d1b84d8694e74a6d0cd9c50bd3e)
#### Tuesday 2022-04-26 21:34:16 by janpierzchala

Final version (sucks ass as hell but whatever, one life chapter in life is closed, further development is reserved for a next chapter)

---
## [Duzos/dubot](https://github.com/Duzos/dubot)@[2dba2f262c...](https://github.com/Duzos/dubot/commit/2dba2f262c4f44c141cbaa3b47a6f4dcb6189135)
#### Tuesday 2022-04-26 23:05:02 by Duzo

reaction rock paper scissors

funny haha look now we use reactions instead of text because it looks cooler or something thanks portlaboy for coming up with this amazing idea that made me want to die for a couple hours was a nice challenge

---

