## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-18](docs/good-messages/2022/2022-04-18.md)


1,810,826 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,810,826 were push events containing 2,795,714 commit messages that amount to 204,285,202 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 35 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d411393e72...](https://github.com/tgstation/tgstation/commit/d411393e72586ba70ac45b8af19d9b3b701e58c9)
#### Monday 2022-04-18 00:40:38 by Zytolg

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
## [kuroringo90/android_kernel_xiaomi_sm8150](https://github.com/kuroringo90/android_kernel_xiaomi_sm8150)@[8d85e4a772...](https://github.com/kuroringo90/android_kernel_xiaomi_sm8150/commit/8d85e4a772fe04190592657e80a3b623b47722ca)
#### Monday 2022-04-18 00:52:19 by Peter Zijlstra

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
Signed-off-by: alanndz <alanndz7@gmail.com>

---
## [Cruix/-tg-station](https://github.com/Cruix/-tg-station)@[759d24ab14...](https://github.com/Cruix/-tg-station/commit/759d24ab14af0ab22ae9642e9190c3db91e16516)
#### Monday 2022-04-18 01:02:44 by san7890

Four Corners, Red Rover: An Exploration in Decal Trends [MDB IGNORE] (#65290)

* Four Corners, Red Rover: An Exploration in Decaled Trends

You there! What exactly is wrong with this photograph?!

You don't need to tell me, I've boxed it out. There's four individual corners for the decalling. This is weird. You may be asking: Why don't they use the "full tile" turf decals? Let me demonstrate.

Look at the difference between the one at left and the one in the middle. The turf decal totally smothers the nice contrast lines afforded to use by the base turf, causing it to have smooth, clammy exterior. This is probably why no mapper ever uses the full turf decal, much to the chagrin of people who stare at how big the size of this repo is.

Now, what's that on the right? Why, it's the new sprite (and pathing I made) to help counter-act this issue! This perfectly lines up with the contrast lines of the base turf, allowing us to have a non-flattened visualization, while not having four fucking turf decals a turf load upon initialization. How epic!

I've also added "contrasted" variants of the "half" and "anticorner" turf decals for future use. I probably won't go through and update this in this PR, but the opportunity remains available.

I may or not map this change across all the maps. We shall see.

* neutral corners

we love vsc

* no wait

i forgot a bunch of potential edgecases so we'll have to go back. yellow should be fine but neutral, dark, blue, and green should get a second look over

* recheck

found some stuff, probably missed out on others. let us commence forth

* MISTAKE

nearly a fucko bwoingo

* final pass

it compiles and i've had enough, someone else can probably figure it out from this point onwards

* #65230 goated my timbs

now we wait for linters to fail

* YOU DIDN'T SAY THAT THE FIRST TIME

LINTERS AAFAFAFF

---
## [Cruix/-tg-station](https://github.com/Cruix/-tg-station)@[884c1eeb62...](https://github.com/Cruix/-tg-station/commit/884c1eeb62e1c970b2b6edc425f36c924b9f48ee)
#### Monday 2022-04-18 01:02:44 by 小月猫

fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

---
## [StarStation13/StarStation13](https://github.com/StarStation13/StarStation13)@[4652d4bb63...](https://github.com/StarStation13/StarStation13/commit/4652d4bb63cec6f73bc46a0ea75d867d235107d1)
#### Monday 2022-04-18 01:21:15 by Jolly

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
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[4d54e290db...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/4d54e290db51697d12fc54a6bbb0a376f43b7280)
#### Monday 2022-04-18 02:01:53 by Zandario

Security TGUI (#3886)

* e

* Fuck it, I'm pushing it.

* Fuck you

* Refactored Brigdoors, updated their UI, does annoucements

Also updated logging a little bit and documented some things.

* Multitool sync

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b86cf89125...](https://github.com/tgstation/tgstation/commit/b86cf89125a425ad650abedf436bb02918c36dcd)
#### Monday 2022-04-18 02:08:00 by Aleksej Komarov

tgui: API improvements + docs (#65943)


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

---
## [dufuspaelli/qb-core](https://github.com/dufuspaelli/qb-core)@[9d83a952c2...](https://github.com/dufuspaelli/qb-core/commit/9d83a952c29fdfd3fb3ca77a45329556a32368f5)
#### Monday 2022-04-18 03:35:00 by uShifty

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
## [Hathoom/Submarine-Pirates](https://github.com/Hathoom/Submarine-Pirates)@[1258935b7b...](https://github.com/Hathoom/Submarine-Pirates/commit/1258935b7bfbdd324a2faacb5d160a6662039e91)
#### Monday 2022-04-18 04:04:08 by ATimpe

Merge pull request #37 from Hathoom/UI

fuck you unity

---
## [ammarfaizi2/linux-block](https://github.com/ammarfaizi2/linux-block)@[de9e8c7174...](https://github.com/ammarfaizi2/linux-block/commit/de9e8c7174eaffd21178d28e94ce01c53107cd41)
#### Monday 2022-04-18 04:17:23 by Linus Torvalds

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
## [Lastprismer/FargowiltasSouls](https://github.com/Lastprismer/FargowiltasSouls)@[29d3bebeab...](https://github.com/Lastprismer/FargowiltasSouls/commit/29d3bebeabcc588562d840de13b036e9b3cb3ec9)
#### Monday 2022-04-18 05:00:27 by terrynmuse

fixed maul still causing "-5 max life" to appear when youre not actually losing max life
cactus ench nerfed
 obeys static iframes
 enemies can only be marked as needled by needles
fixed devi trying to stone dead players
fixed devi floating directly into player while doing shadowbeam attack
nerfed wandering eye fish to spawn demon eyes, not wandering eyes
queen bee can actually despawn in multiplayer
fixed mutant's gift not spawning devi properly
skeletron can change targets after a spin (was locked onto one person until they die)
skeletron regrows arms at 25%
giant and ice tortoise can yeet you like pinky
lightning rod rains lightning while going out as intended, not coming back

---
## [janescorza/reactjs-course](https://github.com/janescorza/reactjs-course)@[b250479c50...](https://github.com/janescorza/reactjs-course/commit/b250479c50b8645baa6558f90d2703dff04d0405)
#### Monday 2022-04-18 07:03:14 by Jan

amazingly well done deletion I'm fucking awesome dude yeah!

---
## [yhluk/Chitung-public](https://github.com/yhluk/Chitung-public)@[dd9c9ea647...](https://github.com/yhluk/Chitung-public/commit/dd9c9ea6473bccb789838298d1e3aa93e399a19e)
#### Monday 2022-04-18 08:02:17 by yhluk

Revert "Fuck you null"

This reverts commit e566d178940063a497c9eaab47b9e9ee1424f55c.

---
## [jn1989/Absinthe](https://github.com/jn1989/Absinthe)@[f07f0029ea...](https://github.com/jn1989/Absinthe/commit/f07f0029eaefa597b6256507f94143337c4c44d1)
#### Monday 2022-04-18 09:33:43 by gys619

删除：[ 2000jinli_log.js, CK_WxPusherUid.json, JDJRSignValidator.js, JDJRValidator_Aaron.js, JDJRValidator_Pure.js, JD_DailyBonus.js, JD_extra_cookie.js, JS_USER_AGENTS.js, LICENSE, Loon/lxk0301_LoonTask.conf, QuantumultX/cookies.conf, QuantumultX/gallery.json, QuantumultX/lxk0301_cookies.conf, QuantumultX/lxk0301_gallery.json, Surge/Task.sgmodule, Surge/lxk0301_Task.sgmodule.sgmodule, TS_USER_AGENTS.ts, USER_AGENTS.js, ZooFaker_Necklace.js, activity/JD_extra_cookie.js, activity/jd_0yuankanjia.js, activity/jd_15_5.js, activity/jd_29_8.js, activity/jd_5g.js, activity/jd_818.js, activity/jd_UnknownTask4.js, activity/jd_angryBean.js, activity/jd_apple_live.js, activity/jd_appliances.js, activity/jd_bean_sign.js, activity/jd_beauty_ex.js, activity/jd_big_winner.js, activity/jd_bridge.js, activity/jd_btnyx.py, activity/jd_bzlshdgt.js, activity/jd_car.js, activity/jd_carnivalcity.js, activity/jd_cash.js, activity/jd_cfd_fresh.js, activity/jd_cfd_fresh_exchange.js, activity/jd_cfd_hb.js, activity/jd_cfd_loop.js, activity/jd_cfd_mooncake.js, activity/jd_cfd_mooncake_help.js, activity/jd_cfd_pearl.js, activity/jd_cfd_pearl_ex.js, activity/jd_cfdtx.js, activity/jd_city_exchange.js, activity/jd_city_lottery.js, activity/jd_citytx.js, activity/jd_coupon.js, activity/jd_crazy_joy.js, activity/jd_crazy_joy_bonus.js, activity/jd_crazy_joy_coin.js, activity/jd_daily_egg.js, activity/jd_daily_lottery.js, activity/jd_ddwj.js, activity/jd_decompression.js, activity/jd_delCoupon.js, activity/jd_desire.js, activity/jd_digital_floor.js, activity/jd_djyyj.js, activity/jd_dlpj.js, activity/jd_dpqd.js, activity/jd_ds.js, activity/jd_dyj_help.js, activity/jd_family.js, activity/jd_fcdyj_help_wx.js, activity/jd_fcwb.js, activity/jd_film_museum.js, activity/jd_firecrackers.js, activity/jd_firecrackers2.js, activity/jd_fission.js, activity/jd_focus.js, activity/jd_foodRunning.js, activity/jd_freshgoods.js, activity/jd_ftzy_help.js, activity/jd_global.js, activity/jd_global_mh.js, activity/jd_golden_machine.js, activity/jd_gouwuche.js, activity/jd_gyp.js, activity/jd_haier.js, activity/jd_half_redrain.js, activity/jd_hb.js, activity/jd_health.js, activity/jd_health_plant.py, activity/jd_honour.js, activity/jd_hotNeight.js, activity/jd_hotnight.js, activity/jd_hyj.js, activity/jd_hyj_help.py, activity/jd_immortal.js, activity/jd_immortal_answer.js, activity/jd_industrial_task.js, activity/jd_industryLottery.js, activity/jd_jchsign.js, activity/jd_jdh.js, activity/jd_jika.js, activity/jd_jingsubang.js, activity/jd_joy.js, activity/jd_joy_feedPets.js, activity/jd_joy_park_newtask.js, activity/jd_joy_run.js, activity/jd_joy_steal.js, activity/jd_jump.js, activity/jd_jxd.js, activity/jd_jxdzz.js, activity/jd_jxg.js, activity/jd_jxhlk.js, activity/jd_jxhlk.py, activity/jd_jxnc.js, activity/jd_jxnn.js, activity/jd_jxstory.js, activity/jd_koi_Help.js, activity/jd_kxcdz.js, activity/jd_ldhwj.js, activity/jd_live.js, activity/jd_live_redrain.js, activity/jd_live_redrain2.js, activity/jd_ljd.js, activity/jd_lol.js, activity/jd_lotteryMachine.js, activity/jd_lottery_drew.js, activity/jd_lsj.js, activity/jd_lxLottery.js, activity/jd_market_lottery.js, activity/jd_mcxhd.js, activity/jd_medal_exchange.py, activity/jd_mh.js, activity/jd_mhyyl.js, activity/jd_mhyyl_prize.js, activity/jd_mofang.js, activity/jd_mofang_ex.js, activity/jd_mohe.js, activity/jd_mohe_help.js, activity/jd_moneyTree_help.js, activity/jd_ms.js, activity/jd_ms_redrain.js, activity/jd_mx_shop.js, activity/jd_neight1.js, activity/jd_neight2.js, activity/jd_newTreasure.py, activity/jd_newYearMoney.js, activity/jd_newYearMoney_lottery.js, activity/jd_nian.js, activity/jd_nian_ar.js, activity/jd_nian_sign.js, activity/jd_nian_wechat.js, activity/jd_nsjcj.js, activity/jd_party_night.js, activity/jd_petTreasureBox.js, activity/jd_pubg.js, activity/jd_qcshj.js, activity/jd_qycl.js, activity/jd_redPacket_help.js, activity/jd_ryhxj.js, activity/jd_selectionOffice.js, activity/jd_sendBeans.js, activity/jd_sevenDay.js, activity/jd_shop.js, activity/jd_sign_graphics.js, activity/jd_sjjc.js, activity/jd_sjnhj.js, activity/jd_speed.js, activity/jd_spnvjd.js, activity/jd_summer_movement.js, activity/jd_superMarket.js, activity/jd_super_box.js, activity/jd_super_mh.js, activity/jd_superbox.js, activity/jd_sxLottery.js, activity/jd_tcl.js, activity/jd_teamFLP.js, activity/jd_tewu.js, activity/jd_tiger_help.js, activity/jd_travel.js, activity/jd_travel_help.js, activity/jd_travel_shop.js, activity/jd_unbind.js, activity/jd_unknownTask1.js, activity/jd_unsubscribe.js, activity/jd_watch.js, activity/jd_wxCollectionActivity.js, activity/jd_wxShopFollowActivity.js, activity/jd_xg.js, activity/jd_xgyl.js, activity/jd_xiaolongfan.js, activity/jd_xiaomi.js, activity/jd_xinruimz.js, activity/jd_xinxiangyin.js, activity/jd_xqscjd.js, activity/jd_xtg.js, activity/jd_xtg_help.js, activity/jd_xyhy.js, activity/jd_year.js, activity/jd_yijia.js, activity/jd_yijiajiu.js, activity/jd_ylyn.js, activity/jd_ys.js, activity/jd_zbjmh.js, activity/jd_zoo.js, activity/jd_zooCollect.js, activity/jd_zooElecsport.js, activity/jd_zzt.js, activity/jx_mc_coin.js, activity/jx_sign_xd.js, backUp/AlipayManor.js, backUp/GetJdCookie.md, backUp/GetJdCookie2.md, backUp/GetJdCookie3.md, backUp/JDJRValidator_Smiek.js, backUp/JD_extra_cookie.js, backUp/Jd_jrValidator.js, backUp/MovementFaker.js, backUp/README.md, backUp/TG_PUSH.md, backUp/ZooFaker_Necklace.js, backUp/aclog.png, backUp/elecV2P.md, backUp/getJDCookie.js, backUp/gitSync.md, backUp/githubAction.md, backUp/iCloud.md, backUp/iOS_Weather_AQI_Standard.js, backUp/index.js, backUp/jdFruitShareCodes.js, backUp/jdJxncShareCodes.js, backUp/jdJxncTokens.js, backUp/jdUA.py, backUp/jd_11RedEnvelope.js, backUp/jd_1212red.js, backUp/jd_15_5.js, backUp/jd_19_6.js, backUp/jd_29_8.js, backUp/jd_5_2.js, backUp/jd_DrawEntrance.js, backUp/jd_MMdou.js, backUp/jd_Supershophf.js, backUp/jd_all_bean_change.js, backUp/jd_angryKoi_all.js, backUp/jd_appliances.js, backUp/jd_bean_change.js, backUp/jd_bean_day_change.js, backUp/jd_bean_month_change.js, backUp/jd_beauty_ex.js, backUp/jd_beauty_plant.py, backUp/jd_big_winner.js, backUp/jd_bzlshdgt.js, backUp/jd_car.js, backUp/jd_carnivalcity.js, backUp/jd_cash_exchange.js, backUp/jd_cfd.js, backUp/jd_cfd_SlotMachine.js, backUp/jd_cfd_fresh.js, backUp/jd_cfd_fresh_exchange.js, backUp/jd_cfd_loop.js, backUp/jd_cfd_mooncake.js, backUp/jd_cfd_mooncake_help.js, backUp/jd_cfd_pearl.js, backUp/jd_cfd_pearl_ex.js, backUp/jd_cfdtx.js, backUp/jd_chinaJoy.js, backUp/jd_city_exchange.js, backUp/jd_citytx.js, backUp/jd_cjzdgf.js, backUp/jd_cleancart.js, backUp/jd_collectcardhelp.js, backUp/jd_crazy_joy.js, backUp/jd_crazy_joy_bonus.js, backUp/jd_crazy_joy_coin.js, backUp/jd_daily_egg.js, backUp/jd_daily_lottery.js, backUp/jd_ddPlayer.js, backUp/jd_ddgame.js, backUp/jd_ddo_pk.js, backUp/jd_ddwj.js, backUp/jd_ddwj_help.js, backUp/jd_decompression.js, backUp/jd_delCoupon.js, backUp/jd_djjl.js, backUp/jd_dreamFactory.js, backUp/jd_dt.js, backUp/jd_dtld.js, backUp/jd_earn30.js, backUp/jd_enen.js.bak, backUp/jd_europeancup.js, backUp/jd_exchangejxbeans.js, backUp/jd_family.js, backUp/jd_fan.js, backUp/jd_fc.js, backUp/jd_fcwb.js, backUp/jd_finance.js, backUp/jd_fission.js, backUp/jd_freshgoods.js, backUp/jd_fruit.js, backUp/jd_getFollowGift.py, backUp/jd_goldPhone.js, backUp/jd_goodMorning.js, backUp/jd_gyp.js, backUp/jd_half_redrain.js, backUp/jd_hb_a.js, backUp/jd_health.js, backUp/jd_health_exchange.py, backUp/jd_health_plant.py, backUp/jd_hwsx.js, backUp/jd_hyj.js, backUp/jd_industrial_task.js, backUp/jd_industryLottery.js, backUp/jd_jchsign.js, backUp/jd_jika.js, backUp/jd_jingsubang.js, backUp/jd_jmofang.js, backUp/jd_joy.js, backUp/jd_joy_feedPets.js, backUp/jd_joy_help.js, backUp/jd_joy_park_newtask.js, backUp/jd_joy_run.js, backUp/jd_joy_sendcard_all.py, backUp/jd_joy_steal.js, backUp/jd_joy_tx.js, backUp/jd_joyjd_open.js, backUp/jd_joyjd_open_list.js, backUp/jd_jump.js, backUp/jd_jxcfd_cash100.py, backUp/jd_jxd.js, backUp/jd_jxdzz.js, backUp/jd_jxg.js, backUp/jd_jxlhb.js, backUp/jd_jxmc_mkmb.js, backUp/jd_jxnc.js, backUp/jd_jxnnfls.py, backUp/jd_jxzpk.js, backUp/jd_kanjia.js, backUp/jd_kanjia3.js, backUp/jd_king.js, backUp/jd_kj.js, backUp/jd_kws.js, backUp/jd_kxcdz.js, backUp/jd_kyd.js, backUp/jd_ldhwj.js, backUp/jd_live_redrain.js, backUp/jd_lotteryMachine.js, backUp/jd_lottery_drew.js, backUp/jd_lsj.js, backUp/jd_lxLottery.js, backUp/jd_mall_active.js, backUp/jd_market_lottery.js, backUp/jd_mb.js, backUp/jd_mf_exchange.js, backUp/jd_mfexchange.js, backUp/jd_mhtask.js, backUp/jd_mhyyl.js, backUp/jd_mofang_ex.js, backUp/jd_mohe.js, backUp/jd_mpdzcar.js, backUp/jd_mpdzcar_game.js, backUp/jd_mpdzcar_help.js, backUp/jd_ms.js, backUp/jd_necklace_new.js, backUp/jd_newTreasure.py, backUp/jd_ns_open.js, backUp/jd_nsjdlot.js, backUp/jd_nyx_help.js, backUp/jd_nzmh.js, backUp/jd_olympicgames.js, backUp/jd_pet.js, backUp/jd_phone.js, backUp/jd_plantBean.js, backUp/jd_ppdz.js, backUp/jd_ppkhr.js, backUp/jd_price.js, backUp/jd_qcshj.js, backUp/jd_qixi.js, backUp/jd_qjd.js, backUp/jd_qmwxj.js, backUp/jd_redrain.js, backUp/jd_redrain_half.js, backUp/jd_sendBeans.js, backUp/jd_sevenDay.js, backUp/jd_shop.js, backUp/jd_sign_graphics1.js, backUp/jd_sjnhj.js, backUp/jd_speed.js, backUp/jd_spider_requests.py, backUp/jd_spnvjd.js, backUp/jd_sq.js, backUp/jd_summer_exchange.js, backUp/jd_summer_movement.js, backUp/jd_summer_movement_help.js, backUp/jd_superBrand2.js, backUp/jd_superMarket.js, backUp/jd_superbox.js, backUp/jd_sxLottery.js, backUp/jd_task.json, backUp/jd_tcl.js, backUp/jd_team60.js, backUp/jd_teamAnJia.js, backUp/jd_teamFLP.js, backUp/jd_travel.js, backUp/jd_travel_shop.js, backUp/jd_twlove.js, backUp/jd_twmsdtt.js, backUp/jd_twoly.js, backUp/jd_twzStar.js, backUp/jd_tyt.js, backUp/jd_unbind.js, backUp/jd_unsubscriLive.js, backUp/jd_unsubscribe.js, backUp/jd_userAwardExpandinfo.py, backUp/jd_utils.js, backUp/jd_wish.js, backUp/jd_wjcj.js, backUp/jd_wxCollectionActivity.js, backUp/jd_wxShopFollowActivity.js, backUp/jd_wxj.js, backUp/jd_xiaolongfan.js, backUp/jd_xlong.js, backUp/jd_xmGame.js, backUp/jd_xqscjd.js, backUp/jd_xsqjd.js, backUp/jd_xtc.js, backUp/jd_xtg.js, backUp/jd_xxy.js, backUp/jd_xyhy.js, backUp/jd_year.js, backUp/jd_yijia.js, backUp/jd_ys.js, backUp/jd_zd.js, backUp/jd_zdjr.js, backUp/jd_zjb.js, backUp/jd_zzt.js, backUp/jddj_bean.js, backUp/jinli_log.js, backUp/jx_cfd_pearl_exchange.js, backUp/jx_mczn_exchange.js, backUp/jx_sign_xd.js, backUp/killck.js, backUp/mengniu.js, backUp/mySelf.boxjs.json, backUp/redrian_user.py, backUp/reposync.md, backUp/rush_anjia.js, backUp/sendNotify.js, backUp/tencentscf.md, backUp/webhook.js, backUp/xmSports.js, bot_jd_bean_change.js, boxjs.json, cleancart_activity.js, config.json, docker/Dockerfile, docker/README.md, docker/Readme.md, docker/auto_help.sh, docker/bot/jd.png, docker/bot/jd_bot, docker/bot/requirements.txt, docker/bot/setup.py, docker/default_task.sh, docker/docker-compose.yml, docker/docker_entrypoint.sh, docker/example/custom-append.yml, docker/example/custom-overwrite.yml, docker/example/default.yml, docker/example/docker\345\244\232\350\264\246\346\210\267\344\275\277\347\224\250\347\213\254\347\253\213\345\256\271\345\231\250\344\275\277\347\224\250\350\257\264\346\230\216.md, docker/example/jd_scripts.custom-append.syno.json, docker/example/jd_scripts.custom-overwrite.syno.json, docker/example/jd_scripts.syno.json, docker/example/multi.yml, docker/extra.sh, docker/notify_docker_user.js, docker/proc_file.sh, docker/task_before.sh, function/JDJRValidator_Pure_smiek.js, function/TS_USER_AGENTS.ts, function/common.js, function/config.js, function/eval.js, function/jdValidate.js, function/jdcookie.js, function/jinli_log.ts, function/jxAlgo.js, function/magic.js, function/ql.js, function/sendNotify.js, function/sign_graphics_validate.js, getJDCookie.js, githubAction.md, gua_MMdou.js, gua_cleancart_ddo.js, gua_opencard115.js, gua_opencard117.js, gua_opencard118.js, gua_opencard127.js, gua_opencard128.js, gua_opencard129.js, gua_opencard130.js, gua_opencard131.js, gua_opencard132.js, gua_wealth_island.js, gua_wealth_island_help.js, index.js, jdEnv.py, jd_10-4.js, jd_15_8.js, jd_19-5.js, jd_19_5.js, jd_5_2.js, jd_CheckCK.js, jd_CkSeq.js, jd_DailyBonus_Mod.js, jd_OpenCard.py, jd_OpenCard_Force.js, jd_UpdateUIDtoRemark.js, jd_angryBean.js, jd_bean_change.js, jd_bean_change1.js, jd_bean_home.js, jd_bean_info.js, jd_bean_sign.js, jd_beans_7days.py, jd_beauty.js, jd_beauty_ex.js, jd_beauty_plant.py, jd_captian_anjia.js, jd_car.js, jd_carnivalcity.js, jd_cash_Mod_Panda.js, jd_cash_exchange.js, jd_cash_wx.js, jd_cfd.js, jd_cfd_fresh.js, jd_cfd_hb.js, jd_cfd_loop.js, jd_cfd_mooncake.js, jd_cfd_pearl.js, jd_cfd_pearl_ex.js, jd_cjzdgf.js, jd_cleancart.js, jd_club_lottery.js, jd_daily_egg.js, jd_daily_lottery.js, jd_ddnc_farmpark.js, jd_delCoupon.js, jd_delete_coupon.js, jd_dpqd.js, jd_dpsign.js, jd_dreamFactory.js, jd_dreamFactory_help.js, jd_dreamFactory_tuan.js, jd_duobao.js, jd_dwapp.js, jd_exchangejxbeans.js, jd_family.js, jd_fan.js, jd_farautomation.js, jd_fcwb.js, jd_fcwb.py, jd_follow_shop.js, jd_fruit.js, jd_fruit_Mod.js, jd_fruit_friend.js, jd_fruit_plant.ts, jd_fruit_task.js, jd_getFollowGift.py, jd_gjlh.js, jd_gold_creator.js, jd_goodMorning.js, jd_gua_cleancart_Panda.js, jd_half_redrain.js, jd_hbCount.py, jd_health.js, jd_health_collect.js, jd_health_exchange.py, jd_health_help.js, jd_health_plant.py, jd_jdfactory.js, jd_jdfactory_help.js, jd_jdzz.js, jd_jfcz.js, jd_jieMo.js, jd_jin_tie.js, jd_jinli_hongbao.ts, jd_joy_feedPets.js, jd_joy_park.js, jd_joy_park_Mod.js, jd_joy_park_task.js, jd_joy_reward_Mod.js, jd_joy_run.js, jd_joy_steal.js, jd_joy_tx.js, jd_joyjd_open.js, jd_joypark_open.js, jd_js_sign.js, jd_jump.js, jd_jx_sign.js, jd_jxg.js, jd_jxgckc.js, jd_jxhlk.py, jd_jxlhb.js, jd_jxmc.js, jd_jxmc_hb.js, jd_jxnc.js, jd_jxnn.js, jd_kanjia.js, jd_kd.js, jd_live.js, jd_live_redrain.js, jd_lotteryMachine.js, jd_lzdz1_customized1.js, jd_lzdz1_customized10.js, jd_lzdz1_customized11.js, jd_lzdz1_customized12.js, jd_lzdz1_customized13.js, jd_lzdz1_customized14.js, jd_lzdz1_customized15.js, jd_lzdz1_customized16.js, jd_lzdz1_customized2.js, jd_lzdz1_customized3.js, jd_lzdz1_customized5.js, jd_lzdz1_customized9.js, jd_lzdz1_jx.json, jd_lzkjdz.js, jd_m_sign.js, jd_market_lottery.js, jd_mhtask.js, jd_mncryyj.js, jd_mofang.js, jd_mofang_ex.js, jd_mohe.js, jd_moneyTree.js, jd_moneyTree_help.js, jd_morningSc.js, jd_mpdzcar.js, jd_mpdzcar_game.js, jd_mpdzcar_help.js, jd_ms.js, jd_nzmh.js, jd_pay_contract.js, jd_pet.js, jd_pet_automation.js, jd_petrw.js, jd_pigPet.js, jd_plantBean.js, jd_plantBean_help.js, jd_plusReward.js, jd_price.js, jd_priceProtect_Mod.js, jd_productZ4Brand.js, jd_redrain.js, jd_redrain_half.js, jd_refreshInvokeKey.js, jd_sendBeans.js, jd_sevenDay.js, jd_sgmh.js, jd_share.js, jd_shop.js, jd_shop_sign_duck.js, jd_sign.js, jd_signFree.js, jd_sign_graphics.js, jd_sign_graphics1.js, jd_speed.js, jd_speed_redpocke.js, jd_speed_sign.js, jd_speed_signred.js, jd_superBrandStar.js, jd_superMarket.js, jd_sxLottery.js, jd_test.js, jd_try.js, jd_try_notify.py, jd_tyt.js, jd_unbind.js, jd_unsubscriLive.js, jd_unsubscribe.js, jd_upgrade.js, jd_wdz.js, jd_week.js, jd_wish.js, jd_wq_wxsign.js, jd_wsdlb.js, jd_wxCollectionActivity.js, jd_wxgame.js, jd_wyw.js, jd_xinruimz.js, jd_xs_zzl.js, jd_yfcoupon.js, jd_ylyn.js, jd_zdjr.js, jd_zjb.js, jd_zjb_help.js, jddjCookie.js, jddj_bean.js, jddj_fruit.js, jddj_fruit_collectWater.js, jddj_getPoints.js, jddj_getck.js, jddj_plantBeans.js, joy_run_token.json, jx_cfd_card.js, jx_factory_automation.js, jx_sign.js, jx_sign_xd.js, lxk0301.boxjs.json, magic.json, magic.py, mount.sh, notify.md, package.json, sendNotify.js, sendNotify.py, serverless.yml, shell_script_mod.sh, sign_graphics_validate.js, test.js, tools/a.py, tools/empty.json, tools/jd_dreamFactory_product.js, utils/JDCookie.py, utils/JDJRValidator.js, utils/JDJRValidator_Pure.js, utils/JDJRValidator_Pure1.js, utils/JDSignValidator.js, utils/JD_DailyBonus.js, utils/MoveMentFaker.js, utils/MovementFaker.js, utils/TS_USER_AGENTS.ts, utils/USER_AGENTS.js, utils/ZooFaker_Necklace.js, utils/common.js, utils/config.js, utils/eval.js, utils/jdCookie.js, utils/jdShareCodes.js, utils/jdValidate.js, utils/jd_jxmcToken.js, utils/jd_sign_validate.js, utils/jdcookie.js, utils/jinli_log.ts, utils/jxAlgo.js, utils/magic.js, utils/ql.js, utils/sendNotify.js, utils/sign_graphics_validate.js, utils/sign_graphics_validate1.js]

---
## [Team-Un-Defined/MessCode](https://github.com/Team-Un-Defined/MessCode)@[7bbd79c9b1...](https://github.com/Team-Un-Defined/MessCode/commit/7bbd79c9b18850c20e0fdf7097c7bbe46d27c5bd)
#### Monday 2022-04-18 09:40:42 by Nao

fucking bastard of a comboBox how the heck could it be a null just fuck yourself you piece of shit

---
## [darkxex/duckstation](https://github.com/darkxex/duckstation)@[f9212363d3...](https://github.com/darkxex/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Monday 2022-04-18 10:44:20 by IlDucci

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
## [dubeyamogh/Dynamic-Surface-AR](https://github.com/dubeyamogh/Dynamic-Surface-AR)@[0b440a9d48...](https://github.com/dubeyamogh/Dynamic-Surface-AR/commit/0b440a9d48c8ad3df599135815015fa755376dbe)
#### Monday 2022-04-18 11:12:58 by dubeyamogh

16BEC0577_VL2019205006395_PE003.pdf

Augmented reality has created quite a stir and many consumers are wondering how this latest technology will actually have an impact on them as it becomes more widely used. For anyone that uses a mobile device for daily activities, augmented reality is the future that will allow consumers to experience a reality that is based on personal needs and desires. AR will present a completely new way to engage and will expand the abilities of retailers as well. The possibilities of augmented reality are literally endless and when combined with et technology of mobile devices, which is already quite powerful, AR will allow for geo-tracking that will allow amazing experiences for consumers.
Augmented reality will also have a strong impact on society. The marketing and advertisement fields will explode with augmented reality devices. The mobile applications that are being developed will offer facial recognition software that will mainstream quickly. For everyday commuters and drivers, navigation devices will be built into the cars and mobile devices. This is already in the works, with some car manufacturers working to implement augmented reality windshields that will help drivers navigate without taking their eyes off the road.
Considering this I developed an application for creating augmented reality content on dynamic surfaces i.e., surfaces which are moving and thus provide a means for the implementation of augmented reality in real life scenarios, where virtual objects can be successfully utilised for the day to day activities of any commoner.

---
## [TakitaTD/takitatd.dev](https://github.com/TakitaTD/takitatd.dev)@[71b2e5b6ff...](https://github.com/TakitaTD/takitatd.dev/commit/71b2e5b6ff7b0d792f95523f180094579a355c74)
#### Monday 2022-04-18 11:27:46 by TakitaTD

COOL ASS FUCKING LINK HOLY SHIT GO TO /Contact/ RIGHT NOW BITCH

---
## [hal9000PR/Paradise](https://github.com/hal9000PR/Paradise)@[6082c95eb3...](https://github.com/hal9000PR/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Monday 2022-04-18 11:30:31 by LightFire53

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
## [AdvancedProgrammingSUT2022/Project](https://github.com/AdvancedProgrammingSUT2022/Project)@[19f8066e83...](https://github.com/AdvancedProgrammingSUT2022/Project/commit/19f8066e83e60b30f2bfd31c0c83213d39db2deb)
#### Monday 2022-04-18 12:14:22 by HirbodBehnam

Removed some stuff

Fixed proofing

Why the fuck you are reading these?

---
## [DAVTOURS/DAVTOURS](https://github.com/DAVTOURS/DAVTOURS)@[eef50cc371...](https://github.com/DAVTOURS/DAVTOURS/commit/eef50cc37154c7b3047fb752e455ad101335995f)
#### Monday 2022-04-18 12:43:51 by DAVTOURS

Create README.md

When is The Best Time of the Year for Gorilla Trekking in Uganda? 

Gorilla Tracking takes place all year long, come rain or shine. The best and busiest time of the year is during the Dry and High Seasons in Uganda, July through September, and Mid-December through March
 
The high or dry seasons come with disadvantages such as scarcity of permits, more tourists, higher, mostly luxury lodging prices. In Uganda, you track gorillas in the Rainforest of Bwindi Impenetrable Forest and on the sides of Virunga Volcanoes in Mgahinga Gorilla Park.

Both are in the Gorilla Highlands of Uganda, where due to the elevation, you have cooler temperatures. Whether dry or rainy season, it can rain at any time in a rainforest, and it does. However, the sun will come out soon after.

For many, the Best Time of the Year is the two Off-Seasons, the Rainy Seasons, when there are fewer people and lower prices, especially for upmarket lodges.

For many, the Best Time of the Year for Gorilla Tracking in Uganda is during the Rainy Season, from April to May and November to Mid-December. There are fewer Tourists, meaning more permits are available, and luxury Lodges adjust their prices. The dates for the discounts will vary lodge by lodge.

The term Rainy Season is not as dreadful for many as it may sound – the temperatures are milder, the parks are even greener, wildlife often more abundant, and the Gentle Giants of the Forest, the Mountain Gorillas, are used to a bit of rain.
When is the Best Time of the Year to track Gorillas in Uganda?
Select the month that suits you best for your Gorilla Tracking Safari via info@davsafaris.com 
Gorilla Tracking from January through February
January and February are part of the dry season. It is one of the best times to track gorillas in Uganda, although rainfall can be expected here during any month.

January and February have become some of the most popular months with Gorilla Trekkers. There are more gorilla trackers in January or February than during July and August during some years.
Gorilla Tracking from March through May
It is the time referred to as the long rains, one of its two wet seasons. The trails will be muddier as you track gorillas. Still, you will be overwhelmed by the rich and lush foliage, flowers, and Afro-montane plants that you will see trekking in Bwindi Impenetrable Forest or Mgahinga Gorilla Park.
The advantage of fewer tourists, readily available gorilla permits, and lower luxury lodging prices will outweigh the benefits of the dry season. Many enjoy the rainy seasons, and even Winston Churchill wrote about the rains in his 1908 Book “My African Journey.” Even the Rainy Seasons are not like you might imagine them to be.”
Gorilla tracking from June through August
June through August is the high and dry season and one of the best times to track Gorillas in Uganda. You might find that it rains here and there at night or during the early morning hours before sunrise, with the sun coming out during the morning.
On the negative side, gorilla permits will be harder to obtain, and you must book your safari well in advance to get them. The same can be said when it comes to the availability of lodging. Should June and August be your months of choice, then plan your gorilla safari early with us.
 
Gorilla Tracking from September through October
September and October are great months to visit Uganda. There are fewer tourists, but the weather remains nice until the latter part of October when the short rains arrive. With more available permits, September and October are good months for gorilla trekking.
Gorilla Tracking during November
November is a rainy season month with the so-called short rains arriving. You will have muddy trails will need a poncho and waterproof boots. However, you will have permits and a choice of lodging at a discount.
Gorilla Tracking during December, including the Holiday Season
You can expect some rainfall during December, but it is an excellent month for trekking to see mountain gorillas, especially during the latter part of the month.
From Mid-December on, there is an increase in tourists, and once again, gorilla permits become scarce. It is best to plan and book your safari well in advance to ensure both permit and lodging availability.
When is the Best Time of the Year to track Gorillas in Uganda?
It is up to you; the choice is for you to make. The best Weather Months of the year are also the busiest months for gorilla tracking. More tourists and fewer permits are available, and you must plan with your gorilla safari dates.

The Shoulder months are an excellent choice if you want nice weather, yet fewer tourists, and more permits.

We like to point out Climate Change has affected the Weather Patterns in the Country. The Dry and Rainy Seasons are no longer as predictable as they once were, and Rainstorms can happen during the dry Seasons.
Best Time of the Year for Gorilla Trekking in Uganda – The reality is that a Gorilla Trek is never canceled 
Current Weather and Forecast for Bwindi Impenetrable Forest and Mgahinga Gorilla Park
The Weather for both Bwindi Impenetrable Forest and Mgahinga is unlike in much of Sub-Saharan Africa. You are not trekking in a steamy jungle. The daytime temperature rarely exceeds 26 degrees Celsius during the day and drops down to 12 degrees Celsius or lower at night, depending on the elevation. You are in what is called the Switzerland of Africa. The weather usually is suitable for Gorilla Trekking and hiking.
For more information about Gorilla trekking safari in Africa, Kindly contact info@davsafaris.com or www.davsafaris.com  whatsapp us via +256701412430

---
## [MrStonedOne/return-youtube-dislike](https://github.com/MrStonedOne/return-youtube-dislike)@[c144815c2e...](https://github.com/MrStonedOne/return-youtube-dislike/commit/c144815c2e5a6b6ca22356d207b3a8ba22ab74e8)
#### Monday 2022-04-18 13:13:38 by Kyle Spier-Swenson

Remove annoying whats new tab.

No, fuck you. NO.

I do not want to be spammed by new tabs by all 50 million extensions I have every time i open chrome. It seems like nothing in the isolate but its gets to 3 or 4 extensions opening tabs every day when allowed to run rampant.

---
## [xenxynon/kernel_xiaomi_lavender](https://github.com/xenxynon/kernel_xiaomi_lavender)@[3fa79f4c28...](https://github.com/xenxynon/kernel_xiaomi_lavender/commit/3fa79f4c28789f7ccb0b53e5f269b555f5e21673)
#### Monday 2022-04-18 14:06:24 by Maciej Żenczykowski

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
Signed-off-by: ImPrashantt <prashant33968@gmail.com>
Signed-off-by: xenxynon <flynryder427@gmail.com>

---
## [ilammy/themis](https://github.com/ilammy/themis)@[94ea4c2926...](https://github.com/ilammy/themis/commit/94ea4c292694b9770c6dc23c6bbd0ef1dfdb443a)
#### Monday 2022-04-18 14:20:22 by Alexei Lozovsky

CI: Audit JavaScript dependencies

Dependabot produces more spam and stress that value. It's a good effort,
Microsoft, but I need more flexibility in what and where gets reported.

I don't want to be greeted with "OMFG YOU HAVE 47 CRITICAL AND 582 HIGH
SEVERITY VULNERABILITIES! DROP WHATEVER THE FUCK YOU WANTED TO DO AND
DEAL WITH THIS SHIT NOW OR ELSE I AM NOT GOING TO REMOVE THIS WARNING
FROM YOUR REPOSITORY" every time I open GitHub. Even if I got paid for
this, I wouldn't want to be experiencing this.

Introduce our own dependency audit thing, which is basically the same
"npm audit" under the hood, but with some tweaks:

  - Customizable severity levels for reports
  - Examples are checked only in "master"
  - Release branches check only non-dev dependencies

Run this for every pull request made against any branch, for every push
made after a pull request, and daily for all long-term branches.

For now, only JavaScript dependencies. Later this could be expanded
to more languages (cargo audit would be an easy one, for example).

---
## [DDamianoff/Unfounded-Afternoon](https://github.com/DDamianoff/Unfounded-Afternoon)@[82cf234259...](https://github.com/DDamianoff/Unfounded-Afternoon/commit/82cf2342594a3efe1113bed6efbe01594cc52ba6)
#### Monday 2022-04-18 14:24:11 by Darker3424

I wish died, this is a fucking shit, i'm tired, not funny..

---
## [angelokimhui/android_kernel_msm8996](https://github.com/angelokimhui/android_kernel_msm8996)@[fd78858a70...](https://github.com/angelokimhui/android_kernel_msm8996/commit/fd78858a70cfededdbdb5cf0e608e2e3d29948af)
#### Monday 2022-04-18 15:03:58 by Linus Torvalds

BACKPORT: mm: get rid of 'vmalloc_info' from /proc/meminfo

It turns out that at least some versions of glibc end up reading
/proc/meminfo at every single startup, because glibc wants to know the
amount of memory the machine has.  And while that's arguably insane,
it's just how things are.

And it turns out that it's not all that expensive most of the time, but
the vmalloc information statistics (amount of virtual memory used in the
vmalloc space, and the biggest remaining chunk) can be rather expensive
to compute.

The 'get_vmalloc_info()' function actually showed up on my profiles as
4% of the CPU usage of "make test" in the git source repository, because
the git tests are lots of very short-lived shell-scripts etc.

It turns out that apparently this same silly vmalloc info gathering
shows up on the facebook servers too, according to Dave Jones.  So it's
not just "make test" for git.

We had two patches to just cache the information (one by me, one by
Ingo) to mitigate this issue, but the whole vmalloc information of of
rather dubious value to begin with, and people who *actually* want to
know what the situation is wrt the vmalloc area should just look at the
much more complete /proc/vmallocinfo instead.

In fact, according to my testing - and perhaps more importantly,
according to that big search engine in the sky: Google - there is
nothing out there that actually cares about those two expensive fields:
VmallocUsed and VmallocChunk.

So let's try to just remove them entirely.  Actually, this just removes
the computation and reports the numbers as zero for now, just to try to
be minimally intrusive.

If this breaks anything, we'll obviously have to re-introduce the code
to compute this all and add the caching patches on top.  But if given
the option, I'd really prefer to just remove this bad idea entirely
rather than add even more code to work around our historical mistake
that likely nobody really cares about.

Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [hyunjun/bookmarks](https://github.com/hyunjun/bookmarks)@[e8b1b1ed57...](https://github.com/hyunjun/bookmarks/commit/e8b1b1ed5705182bbe21ae90bbe851fafa0d0923)
#### Monday 2022-04-18 15:27:10 by hyunjun.chung

Software Design — Orthogonality, Thoughtworks Technology Radar 26호, Block Protocol, Boring Technology Checklist, Effective API, OpenAPI Generator, startup as a solo developer, Monorepo, Microservices Debugging, Comments on Comments, 오남용 심한 IT 유행어, reading academic computer science papers, Unit Testing is Overrated, 소프트웨어 자동화 테스트, How we lost 54k GitHub stars

Software Design — Orthogonality. Software Design can seem tricky or… | by Yoganathan Shiv | Level Up Coding https://levelup.gitconnected.com/software-design-orthogonality-7cd2d50267b6

Thoughtworks Technology Radar 26호 (39p PDF) | GeekNews https://news.hada.io/topic?id=6295

Block Protocol - an open standard for data-driven blocks https://blockprotocol.org
Joel Spolsky on Structuring the Web with the Block Protocol – The New Stack https://thenewstack.io/joel-spolsky-on-structuring-the-web-with-the-block-protocol

The Boring Technology Checklist - Begin https://blog.staging.begin.com/posts/2022-01-27-the-boring-technology-checklist

6 Traits of an Effective API. Great APIs are opinionated. In this… | by Bobi | Dev Genius https://blog.devgenius.io/6-traits-of-an-effective-api-b03e22a8d152

Generate Server Code Using OpenAPI Generator https://mydeveloperplanet.com/2022/02/08/generate-server-code-using-openapi-generator

How I built my tech startup as a solo developer | by Erik | Dreamwod tech | Mar, 2022 | Medium https://medium.com/dreamwod-tech/how-i-built-my-tech-startup-as-a-solo-developer-45390f460002 tech stack

Monorepo Explained https://monorepo.tools

Smart Step-Into for Microservices Debugging | The IntelliJ IDEA Blog https://blog.jetbrains.com/idea/2022/02/smart-step-into-for-microservices-debugging

Fighting Evil in Your Code: Comments on Comments - Simple Talk https://www.red-gate.com/simple-talk/opinion/opinion-pieces/fighting-evil-code-comments-comments

‘매번 지적할 수도 없고...’ 오남용 심한 IT 유행어 14선 - CIO Korea https://www.ciokorea.com/news/232569

You should be reading academic computer science papers - Stack Overflow Blog https://stackoverflow.blog/2022/04/07/you-should-be-reading-academic-computer-science-papers

Unit Testing is Overrated | Oleksii Holub https://tyrrrz.me/blog/unit-testing-is-overrated

파이썬 로봇 프레임워크를 활용한 소프트웨어 자동화 테스트의 가능성 - ITWorld Korea https://www.itworld.co.kr/news/232029

How we lost 54k GitHub stars – HTTPie blog https://httpie.io/blog/stardust

---
## [sonic011gamer/talkman_downstream_kernel](https://github.com/sonic011gamer/talkman_downstream_kernel)@[5ce3441e6e...](https://github.com/sonic011gamer/talkman_downstream_kernel/commit/5ce3441e6e4570a4d083484827cb95aecaa9f29e)
#### Monday 2022-04-18 15:28:52 by sonic011gamer

idk, maybe ramoops fucks something?

Try and move it somewhere where it should be free.
God I hate how MS decided to make the memory map.

---
## [fortune13-ss13/thewasteland](https://github.com/fortune13-ss13/thewasteland)@[59a018d95a...](https://github.com/fortune13-ss13/thewasteland/commit/59a018d95a11eaed40605e2dccb5b549c6c6e2ba)
#### Monday 2022-04-18 17:17:45 by Kirie Saito

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
## [rust-lang/cargo](https://github.com/rust-lang/cargo)@[6a4d98d232...](https://github.com/rust-lang/cargo/commit/6a4d98d2327124ca52bb9f67d6ad0097eb6b2e65)
#### Monday 2022-04-18 18:26:18 by bors

Auto merge of #10472 - epage:add, r=ehuss

feat: Import cargo-add into cargo

### Motivation

The reasons I'm aware of are:
- Large interest, see #5586
- Make it easier to add a dependency when you don't care about the version (instead of having to find it or just using the major version if thats all you remember)
- Provide a guided experience, including
  - Catch or prevent errors earlier in the process
  - Bring the Manifest format documentation into the terminal via `cargo add --help`
  - Using `version` and `path` for `dependencies` but `path` only for `dev-dependencies` (see crate-ci/cargo-release#288 which led to killercup/cargo-edit#480)

### Drawbacks

1. This is another area of consideration for new RFCs, like rust-lang/rfcs#3143 (this PR supports it) or rust-lang/rfcs#2906 (implementing it will require updating `cargo-add`)

2. This is a high UX feature that will draw a lot of attention (ie Issue influx)

e.g.
- killercup/cargo-edit#521
- killercup/cargo-edit#126
- killercup/cargo-edit#217

We've tried to reduce the UX influx by focusing the scope to preserving semantic information (custom sort order, comments, etc) but being opinionated on syntax (style of strings, etc)

### Behavior

Help output
<details>

```console
$ cargo run -- add --help
cargo-add                                                                                                                                  [4/4594]
Add dependencies to a Cargo.toml manifest file

USAGE:
    cargo add [OPTIONS] <DEP>[`@<VERSION>]` ...
    cargo add [OPTIONS] --path <PATH> ...
    cargo add [OPTIONS] --git <URL> ...

ARGS:
    <DEP_ID>...    Reference to a package to add as a dependency

OPTIONS:
        --no-default-features     Disable the default features
        --default-features        Re-enable the default features
    -F, --features <FEATURES>     Space-separated list of features to add
        --optional                Mark the dependency as optional
    -v, --verbose                 Use verbose output (-vv very verbose/build.rs output)
        --no-optional             Mark the dependency as required
        --color <WHEN>            Coloring: auto, always, never
        --rename <NAME>           Rename the dependency
        --frozen                  Require Cargo.lock and cache are up to date
        --manifest-path <PATH>    Path to Cargo.toml
        --locked                  Require Cargo.lock is up to date
    -p, --package <SPEC>          Package to modify
        --offline                 Run without accessing the network
        --config <KEY=VALUE>      Override a configuration value (unstable)
    -q, --quiet                   Do not print cargo log messages
        --dry-run                 Don't actually write the manifest
    -Z <FLAG>                     Unstable (nightly-only) flags to Cargo, see 'cargo -Z help' for
                                  details
    -h, --help                    Print help information

SOURCE:
        --path <PATH>        Filesystem path to local crate to add
        --git <URI>          Git repository location
        --branch <BRANCH>    Git branch to download the crate from
        --tag <TAG>          Git tag to download the crate from
        --rev <REV>          Git reference to download the crate from
        --registry <NAME>    Package registry for this dependency

SECTION:
        --dev                Add as development dependency
        --build              Add as build dependency
        --target <TARGET>    Add as dependency to the given target platform

EXAMPLES:
  $ cargo add regex --build
  $ cargo add trycmd --dev
  $ cargo add --path ./crate/parser/
  $ cargo add serde serde_json -F serde/derive
```

</details>

Example commands
```rust
cargo add regex
cargo add regex serde
cargo add regex@1
cargo add regex@~1.0
cargo add --path ../dependency
```
For an exhaustive set of examples, see [tests](https://github.com/killercup/cargo-edit/blob/merge-add/crates/cargo-add/tests/testsuite/cargo_add.rs) and associated snapshots

Particular points
- Effectively there are two modes
  - Fill in any relevant field for one package
  - Add multiple packages, erroring for fields that are package-specific (`--rename`)
  - Note that `--git` and `--path` only accept multiple packages from that one source
- We infer if the `dependencies` table is sorted and preserve that sorting when adding a new dependency
- Adding a workspace dependency
  - dev-dependencies always use path
  - all other dependencies use version + path
- Behavior is idempotent, allowing you to run `cargo add serde serde_json -F serde/derive` safely if you already had a dependency on `serde` but without `serde_json`
- When a registry dependency's version req is unspecified, we'll first reuse the version req from another dependency section in the manifest.  If that doesn't exist, we'll use the latest version in the registry as the version req

### Additional decisions

Accepting the proposed `cargo-add` as-is assumes the acceptance of the following:
- Add the `-F` short-hand for `--features` to all relevant cargo commands
- Support ``@`` in pkgids in other commands where we accept `:`
- Add support for `<name>`@<version>`` in more commands, like `cargo yank` and `cargo install`

### Alternatives

- Use `:` instead of ``@`` for versions
- Flags like `--features`, `--optional`, `--no-default-features` would be position-sensitive, ie they would only apply to the crate immediate preceding them
  - This removes the dual-mode nature of the command and remove the need for the `+feature` syntax (`cargo add serde -F derive serde_json`)
  - There was concern over the rarity of position-sensitive flags in CLIs for adopting it here
- Support a `--sort` flag to sort the dependencies (existed previously)
  - To keep the scope small, we didn't want general manifest editing capabilities
- `--upgrade <POLICY>` flag to choose constraint (existed previously)
  - The flag was confusing as-is and we feel we should instead encourage people towards `^`
- `--allow-prerelease` so a `cargo add clap` can choose among pre-releases as well
  - We felt the pre-release story is too weak in cargo-generally atm for making it first class in `cargo-add`
- Offer `cargo add serde +derive serde_json` as a shorthand
- Infer path from a positional argument

### Prior Art

- *(Python)* [poetry add](https://python-poetry.org/docs/cli/#add)
  - `git+` is needed for inferring git dependencies, no separate  `--git` flags
  - git branch is specified via a URL fragment, instead of a `--branch`
- *(Javascript)* [yarn add](https://yarnpkg.com/cli/add)
  - `name@data` where data can be version, git (with fragment for branch), etc
  - `-E` / `--exact`, `-T` / `--tilde`, `-C` / `--caret` to control version requirement operator instead of `--upgrade <policy>` (also controlled through `defaultSemverRangePrefix` in config)
  - `--cached` for using the lock file (killercup/cargo-edit#41)
  - In addition to `--dev`, it has `--prefer-dev` which will only add the dependency if it doesn't already exist in `dependencies` as well as `dev-dependencies`
  - `--mode update-lockfile` will ensure the lock file gets updated as well
- *(Javascript)* [pnpm-add](https://pnpm.io/cli/add)
- *(Javascript)* npm doesn't have a native solution
  - Specify version with ``@<version>``
  - Also overloads `<name>[`@<version>]`` with path and repo
    - Supports a git host-specific protocol for shorthand, like `github:user/repo`
    - Uses fragment for git ref, seems to have some kind of special semver syntax for tags?
  - Only supports `--save-exact` / `-E` for operators outside of the default
- *(Go)* [go get](https://go.dev/ref/mod#go-get)
  - Specify version with ``@<version>``
  - Remove dependency with ``@none``
- *(Haskell)* stack doesn't seem to have a native solution
- *(Julia)* [pkg Add](https://docs.julialang.org/en/v1/stdlib/Pkg/)
- *(Ruby)* [bundle add](https://bundler.io/v2.2/man/bundle-add.1.html)
  - Uses `--version` / `-v` instead of `--vers` (we use `--vers` because of `--version` / `-V`)
  - `--source` instead of `path` (`path` correlates to manifest field)
  - Uses `--git` / `--branch` like `cargo-add`
- *(Dart)* [pub add](https://dart.dev/tools/pub/cmd/pub-add)
  - Uses `--git-url` instead of `--git`
  - Uses `--git-ref` instead of `--branch`, `--tag`, `--rev`

### Future Possibilities

- Update lock file accordingly
- Exploring the idea of a [`--local` flag](https://github.com/killercup/cargo-edit/issues/590)
- Take the MSRV into account when automatically creating version req (https://github.com/killercup/cargo-edit/issues/587)
- Integrate rustsec to report advisories on new dependencies (https://github.com/killercup/cargo-edit/issues/512)
- Integrate with licensing to report license, block add, etc (e.g. https://github.com/killercup/cargo-edit/issues/386)
- Pull version from lock file (https://github.com/killercup/cargo-edit/issues/41)
- Exploring if any vendoring integration would be beneficial (currently errors)
- Upstream `cargo-rm` (#10520), `cargo-upgrade` (#10498), and `cargo-set-version` (in that order of priority)
- Update crates.io with `cargo add` snippets in addition to or replacing the manifest snippets

For more, see https://github.com/killercup/cargo-edit/issues?q=is%3Aissue+is%3Aopen+label%3Acargo-add

### How should we test and review this PR?

This is intentionally broken up into several commits to help reviewing
1. Import of production code from cargo-edit's `merge-add` branch, with only changes made to let it compile (e.g. fixing up of `use` statements).
2. Import of test code / snapshots.  The only changes outside of the import were to add the `snapbox` dev-dependency and to `mod cargo_add` into the testsuite
3. This extends the work in #10425 so I could add back in the color highlighting I had to remove as part of switching `cargo-add` from direct termcolor calls to calling into `Shell`

Structure-wise, this is similar to other commands
- `bin` only defines a CLI and adapts it to an `AddOptions`
- `ops` contains a focused API with everything buried under it

The "op" contains a directory, instead of just a file, because of the amount of content.  Currently, all editing code is contained in there.  Most of this will be broken out and reused when other `cargo-edit` commands are added but holding off on that for now to separate out the editing API discussions from just getting the command in.

Within the github UI, I'd recommend looking at individual commits (and the `merge-add` branch if interested), skipping commit 2.  Commit 2 would be easier to browse locally.

`cargo-add` is mostly covered by end-to-end tests written using `snapbox`, including error cases.

There is additional cleanup that would ideally happen that was excluded intentionally from this PR to keep it better scoped, including
- Consolidating environment variables for end-to-end tests of `cargo`
- Pulling out the editing API, as previously mentioned
  - Where the editing API should live (`cargo::edit`?)
  - Any more specific naming of types to reduce clashes (e.g. `Dependency` or `Manifest` being fairly generic).
- Possibly sharing `SourceId` creation between `cargo install` and `cargo edit`
- Explore using `snapbox` in more of cargo's tests

Implementation justifications:
- `dunce` and `pathdiff` dependencies: needed for taking paths relative to the user and make them relative to the manifest being edited
- `indexmap` dependency (already a transitive dependency): Useful for preserving uniqueness while preserving order, like with feature values
- `snapbox` dev-dependency: Originally it was used to make it easy to update tests as the UX changed in prep for merging but it had the added benefit of making some UX bugs easier to notice so they got fixed.  Overall, I'd like to see it become the cargo-agnostic version of `cargo-test-support` so there is a larger impact when improvements are made
- `parse_feature` function: `CliFeatures` forces items through a `BTreeSet`, losing the users specified order which we wanted to preserve.

### Additional Information

See also [the internals thread](https://internals.rust-lang.org/t/feedback-on-cargo-add-before-its-merged/16024).

Fixes #5586

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[5ea57e37f8...](https://github.com/treckstar/yolo-octo-hipster/commit/5ea57e37f86e3df2ef565b10ad4ceebc03a90549)
#### Monday 2022-04-18 19:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Aurrain/LoneStar](https://github.com/Aurrain/LoneStar)@[e2cbff46d2...](https://github.com/Aurrain/LoneStar/commit/e2cbff46d22c78e8e773ad20d47cdecb285ab9a6)
#### Monday 2022-04-18 21:05:39 by Jawnner

Walking Turret - A Minigun PR (#496)

* Update minigun.dm

* Does the same for gatling laser

* better gatling sound

* Energy weapons can reload with click instead of alt click

* Beefier gatling laser sounds

* Update laser.dm

* Gatling Laser 180 shots now (fuck you pots)

---
## [onetrickwolfy/twitter_hourly_bot_from_reddit](https://github.com/onetrickwolfy/twitter_hourly_bot_from_reddit)@[765e16adb9...](https://github.com/onetrickwolfy/twitter_hourly_bot_from_reddit/commit/765e16adb92f0a4a8343cb3ff77ae56192fb3125)
#### Monday 2022-04-18 21:38:16 by Gabey

tweeting function wasn;t working baby.

i know i am bad but holy shit the doc sucks.

---
## [Offroaders123/Landscapes](https://github.com/Offroaders123/Landscapes)@[451c1e1f56...](https://github.com/Offroaders123/Landscapes/commit/451c1e1f567b179bd48699f9d6b65261e9850730)
#### Monday 2022-04-18 22:06:03 by Offroaders123

License Updates + Removed Credit Messages

Changes:
- Updated the pack license from 2021 to 2022, hehe.
- Updated the pack manifests to no longer mention which version the pack was made for. I did this back in the old days of making my resource packs, and I now think it's just a little extra info that doesn't help to have in the description.

Removals:
- Removed old messages in files saying the pack was created by me. Since the pack is fully open source, no real need to keep around the messages anymore (Not that a resource pack can actually be closed source, but yeah. There are few funny things like that from the Minecraft dev community haha).

---
## [DeltaWither/Qwarzu-botto](https://github.com/DeltaWither/Qwarzu-botto)@[2072f305b9...](https://github.com/DeltaWither/Qwarzu-botto/commit/2072f305b9b3a9fc87f77d8c035d3ffccbf1eaf2)
#### Monday 2022-04-18 22:48:03 by DeltaWither

Added a fucking mess. Oh god, I'll just go to sleep and magically sort it out tomorrow

---

