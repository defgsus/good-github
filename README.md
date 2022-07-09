## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-07-08](docs/good-messages/2022/2022-07-08.md)


1,730,295 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,730,295 were push events containing 2,537,826 commit messages that amount to 192,535,718 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 29 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[6fe0683a7b...](https://github.com/tgstation/tgstation/commit/6fe0683a7bc788a497dbce8771768e427d0dffb1)
#### Friday 2022-07-08 00:02:36 by Jolly

[READY] [KC13] Showing "The Derelict" some love: General updates, aesthetic changes and misc (#67696)

With this PR I aim to make KC13 (TheDerelict.dmm), or Russian Station (whatever you guys call it) a tad bit more flavorful with its environment as well as somethings on the mapping side (like adding area icons!).
To preface, no, I'm not remapping anything here extensively. The general layout should be relatively the same (or should be in theory).

Halfway through naming the area icons I checked the wiki page and found out it was KC not KS, so, its KS13 internally.

Readability for turf icons are cool.
Also just making the ruin more eye appealing would be better.
General cleanup and changes will give new life to this rather.. loved? Hated? Loot pinata? Ruin.
The ruin also now starts completely depowered, like Old Station (its a Derelict, it makes no sense for it to still be powered after so long). As for some mild compensation, a few more batteries were sprinkled in to offset any issues. If there is any concern of "But they'll open the vault faster!", there were always 5 batteries that people used to make the vault SMES.
Lastly, giving it some "visual story telling" is cool, as mapping fluff goes.

I also added a subtle OOC hint that the SMES in the northern most solar room needs a terminal with the following:

SMES Jumpscare
As an aside, I aim to try and keep the feel of this ruin being "dated" while at the same time having some of our newer things. With that, certain things I'll opt out of using in favor of more "generic" structures to give KC13 that true "Its old but not really" feel and look.

---
## [hortont424/WebKit](https://github.com/hortont424/WebKit)@[56d15f6c0e...](https://github.com/hortont424/WebKit/commit/56d15f6c0e9323a738bd1caae4313e5625632151)
#### Friday 2022-07-08 00:06:29 by Tim Horton

Add a very simple live-ish resize SPI
https://bugs.webkit.org/show_bug.cgi?id=242431

Reviewed by NOBODY (OOPS!).

There are a few problems with the existing resize mechanisms on
iOS family platforms:

- Bare `setFrame:` does not make any attempt to synchronize the frame change
  with the incoming asynchronous painting.

- `_beginAnimatedResize:` cannot handle long-duration animations (like those
  that occur during a human-driven resize), and requires nontrivial
  rearchitecture in order to do so (see e.g. 235698@main, which removed all
  support for updating the animated resize transform when intermediate commits
  arrive, which happens frequently during long-running live resizes).
  It is built primarily to drive single-shot rotation animations.

- `_holdLiveResizeSnapshotForReason:` depends on platform support which is not
  always available, and also requires taking many snapshots as the view resizes.

- `setFrame:` + CoreAnimation fencing (which we use on macOS, not iOS) blocks
  non-WebKit UI hosted in the same CAContext, and is generally frowned upon.

So, let's introduce one more! That will surely help.

`_beginLiveResize` -> repeated `setFrame` -> `_endLiveResize` will do a very
simple, live-*ish* resize. We defer actual frame changes until the end of the
resize, but dynamically scale the existing tiles (and allow them to repaint)
on each frame change.

* Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h:
* Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm:
(-[WKWebView _processWillSwapOrDidExit]):
(-[WKWebView _updateLiveResizeTransform]):
Scale (and translate) the current tiles to fit in the web view as it is resized.

(-[WKWebView _frameOrBoundsChanged]):
Skip most of _frameOrBoundsChanged while in live-resize, just like we do
for animated resize.

(-[WKWebView _ensureResizeAnimationView]):
(-[WKWebView _destroyResizeAnimationView]):
(-[WKWebView _cancelAnimatedResize]):
(-[WKWebView _beginAnimatedResizeWithUpdates:]):
Factor out creation of the _resizeAnimationView from animated resize code, and
re-use it for "live" resize.

(-[WKWebView _beginLiveResize]):
Start a live resize.

(-[WKWebView _endLiveResize]):
End a live resize. In order to synchronise the transition from the
resizeAnimationView's scale to the scale of the pending incoming tiles, we throw
up a temporary snapshot. Ideally this would be removed in the future, but will
require quite a bit of care to avoid flashing; also, it is quite shortlived
so shouldn't cause much trouble.

---
## [artorhem/wiredtiger](https://github.com/artorhem/wiredtiger)@[24d35561e3...](https://github.com/artorhem/wiredtiger/commit/24d35561e328e6568992bcafa18a560d56688185)
#### Friday 2022-07-08 00:19:16 by Keith Bostic

WT-5521 Cache stuck during format initial load, configured with library checkpoints (#5233)

* If reconciliation requires multiple blocks and checkpoint is running we'll eventually fail.
It's possible this is a big page that will take a lot of writes, avoid wasted work.

* Quit doing so much work in format's read-scan, it's not that useful any more and we're have already
verified the load.

* Configuring WiredTiger library checkpoints is done separately, rather than as part of the
original database open because format tests small caches and you can get into cache stuck
trouble during bulk load. Imagine a single thread doing lots of inserts and creating huge
leaf pages. Those pages can't be evicted when there are checkpoints running in the tree and
the cache gets stuck. That workload is unlikely enough the library can't handle it, and we
configure it away here.

---
## [git/git](https://github.com/git/git)@[6e4b3a7812...](https://github.com/git/git/commit/6e4b3a78125716af1eca37ca356fae07c4030ff6)
#### Friday 2022-07-08 01:09:44 by Glen Choo

setup.c: create `discovery.bare`

There is a known social engineering attack that takes advantage of the
fact that a working tree can include an entire bare repository,
including a config file. A user could run a Git command inside the bare
repository thinking that the config file of the 'outer' repository would
be used, but in reality, the bare repository's config file (which is
attacker-controlled) is used, which may result in arbitrary code
execution. See [1] for a fuller description and deeper discussion.

A simple mitigation is to forbid bare repositories unless specified via
`--git-dir` or `GIT_DIR`. In environments that don't use bare
repositories, this would be minimally disruptive.

Create a config variable, `discovery.bare`, that tells Git whether or
not to die() when it discovers a bare repository. This only affects
repository discovery, thus it has no effect if discovery was not
done, e.g. if the user passes `--git-dir=my-dir`, discovery will be
skipped and my-dir will be used as the repo regardless of the
`discovery.bare` value.

This config is an enum of:

- "always": always allow bare repositories (this is the default)
- "never": never allow bare repositories

If we want to protect users from such attacks by default, neither value
will suffice - "always" provides no protection, but "never" is
impractical for bare repository users. A more usable default would be to
allow only non-embedded bare repositories ([2] contains one such
proposal), but detecting if a repository is embedded is potentially
non-trivial, so this work is not implemented in this series.

[1]: https://lore.kernel.org/git/kl6lsfqpygsj.fsf@chooglen-macbookpro.roam.corp.google.com
[2]: https://lore.kernel.org/git/5b969c5e-e802-c447-ad25-6acc0b784582@github.com

Signed-off-by: Glen Choo <chooglen@google.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [nezorf2/tgstation](https://github.com/nezorf2/tgstation)@[e37591540b...](https://github.com/nezorf2/tgstation/commit/e37591540b2620b7ad2a2b61734634d848e8eba2)
#### Friday 2022-07-08 02:04:49 by san7890

[MDB Ignore] OH GOD OH FUCK OH SHIT OH LORD - SPACE AND RUINS IS BROKEN (#67324)

So, for the last few days on production, Space Ruin generation has refused to work. Why is this? It's because in #67107 (cfc233052885dd294b2e7e676caaf84a2a37592b), we repathed `/area/space`  to `/area/misc/space` (lol i should have paid attention to that) without updating everything in code to match. I couldn't seem to get `/area/misc/space` to properly work somehow (this could have also been something I was doing wrong), but I worked it back to just making everything vanilla `/area/space` and all of those unwanted behaviors should be squashed out. Let's get the game working again.

---
## [cyzzc/hestiacp](https://github.com/cyzzc/hestiacp)@[365dab5670...](https://github.com/cyzzc/hestiacp/commit/365dab5670f6d1a862858be01638072eeb2ec1db)
#### Friday 2022-07-08 03:02:22 by divinity76

Use secure RNG to generate passwords (#2726)

* use secure rng to generate passwords

quoting MDN:
>Math.random() does not provide cryptographically secure random numbers. Do not use them for anything related to security. Use the Web Crypto API instead

My rng is kinda shitty, i know there is some fast way to cut down higher digits to get a digit in range without introducing bias, but i also know that other people have introduced bias by trying to do that on an initially secure rng and getting it wrong (iirc it's discussed here? https://www.youtube.com/watch?v=LDPMpc-ENqY - been years since i saw the talk, but i know Lavavej discussed it in one of his presentations, i think it was that one)  , but anyway this is fast enough, and secure.

* shorter name

* randomString2 / centralize js string generation

* missed 2

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0b95069296...](https://github.com/treckstar/yolo-octo-hipster/commit/0b95069296c7bc1f0eef3cac73d899a05c85f21b)
#### Friday 2022-07-08 04:22:02 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [ianatol/julia](https://github.com/ianatol/julia)@[62e0729dbc...](https://github.com/ianatol/julia/commit/62e0729dbc5f9d5d93d14dcd49457f02a0c6d3a7)
#### Friday 2022-07-08 04:28:20 by Mirek Kratochvil

avoid using `@sync_add` on remotecalls (#44671)

* avoid using `@sync_add` on remotecalls

It seems like @sync_add adds the Futures to a queue (Channel) for @sync, which
in turn calls wait() for all the futures synchronously. Not only that is
slightly detrimental for network operations (latencies add up), but in case of
Distributed the call to wait() may actually cause some compilation on remote
processes, which is also wait()ed for. In result, some operations took a great
amount of "serial" processing time if executed on many workers at once.

For me, this closes #44645.

The major change can be illustrated as follows: First add some workers:

```
using Distributed
addprocs(10)
```

and then trigger something that, for example, causes package imports on the
workers:

```
using SomeTinyPackage
```

In my case (importing UnicodePlots on 10 workers), this improves the loading
time over 10 workers from ~11s to ~5.5s.

This is a far bigger issue when worker count gets high. The time of the
processing on each worker is usually around 0.3s, so triggering this problem
even on a relatively small cluster (64 workers) causes a really annoying delay,
and running `@everywhere` for the first time on reasonable clusters (I tested
with 1024 workers, see #44645) usually takes more than 5 minutes. Which sucks.

Anyway, on 64 workers this reduces the "first import" time from ~30s to ~6s,
and on 1024 workers this seems to reduce the time from over 5 minutes (I didn't
bother to measure that precisely now, sorry) to ~11s.

Related issues:
- Probably fixes #39291.
- #42156 is a kinda complementary -- it removes the most painful source of
  slowness (the 0.3s precompilation on the workers), but the fact that the
  wait()ing is serial remains a problem if the network latencies are high.

May help with #38931

Co-authored-by: Valentin Churavy <vchuravy@users.noreply.github.com>

---
## [orthography/tgstation](https://github.com/orthography/tgstation)@[2605060b58...](https://github.com/orthography/tgstation/commit/2605060b58cc2a069abb65f4ef4ac1c66f4f0bc3)
#### Friday 2022-07-08 04:35:22 by orthography

Changes a Tramstation "lil pump" to a regular one.

Fixes #68236

Accepted #68177

Go fuck yourself.

---
## [ImLonely13/android_kernel_xiaomi_mt6768](https://github.com/ImLonely13/android_kernel_xiaomi_mt6768)@[0a716bd9a1...](https://github.com/ImLonely13/android_kernel_xiaomi_mt6768/commit/0a716bd9a1239d652beb27988e92c2dccacf5a7c)
#### Friday 2022-07-08 04:37:01 by Peter Zijlstra

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
Signed-off-by: ImLonely13 <gabutuhaku@gmail.com>

---
## [TDKorn/insta-tweet](https://github.com/TDKorn/insta-tweet)@[400a7f6fbe...](https://github.com/TDKorn/insta-tweet/commit/400a7f6fbea71474dbee285937958ac953624a0e)
#### Friday 2022-07-08 05:22:40 by TDKorn

Redo `TweetClient`  to wrap the `tweepy` package

`TweetClient`
* It's doing the exact same thing as before
* But without that stank raw-ass code I threw together (and then pretended didn't exist)
* I think it's much cleaner now. Plus, I don't need to maintain the twitter part, which is a relief bc I can barely maintain my will to live
    - For legal/employment purposes, that was a joke 😃😂😃 I love being alive haha 😂🤣 wasn't that silly 🤪😀🤣😂😂😂😂😂😂😂😂😂😂
* Using the package might makes it really easy to authorize users with my consumer key/token? I think that's a feature
    - At some point I'll implement that and deprecate the twitter keys requirement of the `Profile`

---

* Updated `InstaClient`, `InstaTweet`, `InstaPost` classes to reflect changes in `TweetClient`

---
## [CerberusHellHound/Foundation-19](https://github.com/CerberusHellHound/Foundation-19)@[2e51339224...](https://github.com/CerberusHellHound/Foundation-19/commit/2e5133922461bb262efb1deb4b1de8faf2575b48)
#### Friday 2022-07-08 05:31:59 by CerberusHellHound

Mateba fix (#188)

* Update baystation12.dme

* 9mm/.45ACP Buff

Changes are as follow:
- Buffed 9mm dam from 8 to 25 (now it doesn't take a whole mag to take down an unarmoured man)
- Buffed .45 dam from 10 to 30
- Nerfed 9mm AP from 34 to 30
- Buffed 7,62 dam from 40 to 50 (It's supposed to be beefier than 5,56mm)

* Organ changes

Lower organ health value to make combat much deadlier.
Headshots are truly lethal now.

* Slight rebalance and renamings

List of changes :
- decreased brain health to 150 (instead of 200), it's high enough that medical assistance can be given if fast but low enough that you don't want to get shot
- increased damage values of weapons to baystation/nebula level (40 for a pistol for eg)
- increased adrenalin generation when hurt (less fading in and out, you can still use your gun when hit and pain won't be such a pain in the ass, but you're less likely to get back up once the final shot hits you)
- decreased relative size of lungs from 60% to 30% so that now, getting hit in the chest won't have as much chance of damaging your poor fucking lungs (yes 60% is the original baystation number.. it makes sense, it's a large organ, but it's a pain in the ass)
- changed some names and descriptions of certain weapons and firearms to better fit established naming convention
-made revolvers cycle the barrel instead of eject each shot (it's a revolver, not a damn rifle)
- slightly decreased firing delay for the mk9 revolver (slightly weaker than the mateba so slightly faster firing)
- decreased firing delay for the mk9 pistol (lower caliber, less recoil, easier to magdump)

* Mateba fix

Fixed a misstype for the mateba that incorrectly qualified its caliber.

* Mateba fix

Fixing typo

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[addf27fd16...](https://github.com/Koi-3088/ForkBot.NET/commit/addf27fd1688c4785202b53177d7fa84069d9bed)
#### Friday 2022-07-08 05:47:13 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [TDKorn/insta-tweet](https://github.com/TDKorn/insta-tweet)@[d9204d4685...](https://github.com/TDKorn/insta-tweet/commit/d9204d468500dcba5c0dde70aed24fb4bd0548bd)
#### Friday 2022-07-08 05:50:22 by TDKorn

Redo `TweetClient`  to wrap the `tweepy` package

`TweetClient`
* It's doing the exact same thing as before
* But without that stank raw-ass code I threw together (and then pretended didn't exist)
* I think it's much cleaner now. Plus, I don't need to maintain the twitter part, which is a relief bc I can barely maintain my will to live
    - For legal/employment purposes, that was a joke 😃😂😃 I love being alive haha 😂🤣 wasn't that silly 🤪😀🤣😂😂😂😂😂😂
* Using `tweepy`  might make it really easy to authorize users with my consumer key/token? I think that's a feature
    - If it is, then at some point I'll implement it and deprecate the twitter keys requirement

---

* Updated `InstaClient`, `InstaTweet`, `InstaPost` classes to reflect changes in `TweetClient`

---
## [CoinMarketCapAustraliaNFTs/core.js](https://github.com/CoinMarketCapAustraliaNFTs/core.js)@[77507f57bd...](https://github.com/CoinMarketCapAustraliaNFTs/core.js/commit/77507f57bdf18267446ab9803de03795b9541763)
#### Friday 2022-07-08 07:15:00 by CoinMarketCap Australia NFT'S

BLOCKCHAIR.yml

core.js
Extendable client for GitHub's REST & GraphQL APIs

@latest Build Status

Usage
REST API example
GraphQL example
Options
Defaults
Authentication
Logging
Hooks
Plugins
Build your own Octokit with Plugins and Defaults
LICENSE
If you need a minimalistic library to utilize GitHub's REST API and GraphQL API which you can extend with plugins as needed, then @octokit/core is a great starting point.

If you don't need the Plugin API then using @octokit/request or @octokit/graphql directly is a good alternative.

Usage
Browsers	Load @octokit/core directly from cdn.skypack.dev
<script type="module">
import { Octokit } from "https://cdn.skypack.dev/@octokit/core";
</script>
Node	
Install with npm install @octokit/core

const { Octokit } = require("@octokit/core");
// or: import { Octokit } from "@octokit/core";
REST API example
// Create a personal access token at https://github.com/settings/tokens/new?scopes=repo
const octokit = new Octokit({ auth: `personal-access-token123` });

const response = await octokit.request("GET /orgs/{org}/repos", {
  org: "octokit",
  type: "private",
});
See @octokit/request for full documentation of the .request method.

GraphQL example
const octokit = new Octokit({ auth: `secret123` });

const response = await octokit.graphql(
  `query ($login: String!) {
    organization(login: $login) {
      repositories(privacy: PRIVATE) {
        totalCount
      }
    }
  }`,
  { login: "octokit" }
);
See @octokit/graphql for full documentation of the .graphql method.

Options
name	type	description
options.authStrategy	Function	Defaults to @octokit/auth-token. See Authentication below for examples.
options.auth	String or Object	See Authentication below for examples.
options.baseUrl	String	
When using with GitHub Enterprise Server, set options.baseUrl to the root URL of the API. For example, if your GitHub Enterprise Server's hostname is github.acme-inc.com, then set options.baseUrl to https://github.acme-inc.com/api/v3. Example

const octokit = new Octokit({
  baseUrl: "https://github.acme-inc.com/api/v3",
});
options.previews	
Benefits CoinTracker logo
CoinTracker
Partner
CoinTracker is a portfolio assistant for cryptocurrency. It is used by over 100,000 cryptocurrency holders and tracks $20B of cryptocurrency transaction volume. CoinTracker supports 300+ exchange & wallet integrations and over 3,000 cryptocurrency integrations.
CoinTracker enables seamless tracking of cryptocurrency portfolios, investment performance, DeFi, and taxes. Beyond crypto, CoinTracker is building a general automated financial assistant for all financial assets.
CoinTracker has partnered with Coinbase, Intuit, and other industry leaders to make crypto taxes simple, and is venture-backed by Y Combinator, Initialized Capital, and Serena Williams.

https://www.cointracker.io 
Go to compare
Recommended for
Bitcoin, Bitcoin Cash, Ethereum, Ripple, Litecoin, Monero, Dogecoin, Zcash, EOS, Cardano, Stellar, Dash
Languages
English
Service provision
Usa, Australia, United Kingdom, Canada
Tax methods
Fifo, Lifo, Hifo, Acb, Share Pooling
Platforms
iOS, Android, Web
Integrations with other Tax software
Turbotax, Taxact
Pricing
$0-$199
Country of residence
USA
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<rss version="2.0">
<channel>
<title>(be now read a second time) AND SittingYear CONTAINS (2022) AND SittingMonth CONTAINS (June) AND SittingDay CONTAINS (23) AND SpeechTitle CONTAINS (Residential Tenancies, Housing and Social Services Regulation Amendment Administration and Other Matters Bill 2022) AND ACTIVITYTYPE CONTAINS (Second reading) AND HOUSENAME CONTAINS (ASSEMBLY) - Hansard Search Results</title>
<link>http://hansard.parliament.vic.gov.au/search?IW_DATABASE=*&IW_FIELD_WEB_STYLE=(be%20now%20read%20a%20second%20time)%20AND%20SittingYear%20CONTAINS%20(2022)%20AND%20SittingMonth%20CONTAINS%20(June)%20AND%20SittingDay%20CONTAINS%20(23)%20AND%20SpeechTitle%20CONTAINS%20(Residential%20Tenancies,%20Housing%20and%20Social%20Services%20Regulation%20Amendment%20Administration%20and%20Other%20Matters%20Bill%202022)%20AND%20ACTIVITYTYPE%20CONTAINS%20(Second%20reading)%20AND%20HOUSENAME%20CONTAINS%20(ASSEMBLY)</link>
<description>Search results for (be now read a second time) AND SittingYear CONTAINS (2022) AND SittingMonth CONTAINS (June) AND SittingDay CONTAINS (23) AND SpeechTitle CONTAINS (Residential Tenancies, Housing and Social Services Regulation Amendment Administration and Other Matters Bill 2022) AND ACTIVITYTYPE CONTAINS (Second reading) AND HOUSENAME CONTAINS (ASSEMBLY) generated by Hansard Search</description>
<language>en-au</language>
<pubDate>Fri, 08 Jul 2022 16:08:13 +1000</pubDate>
<lastBuildDate>Fri, 08 Jul 2022 16:08:13 +1000</lastBuildDate>
<ttl>720</ttl>
<generator>Perceptive Enterprise Search</generator>
<item>
<title>RESIDENTIAL TENANCIES, HOUSING AND SOCIAL SERVICES REGULATION AMENDMENT (ADMINISTRATION AND OTHER MATTERS) BILL 2022</title>
<link>http://hansard.parliament.vic.gov.au/?IW_INDEX=Hansard-2022-1&IW_FIELD_TEXT=SpeechIdKey%20CONTAINS%20(23-06-2022_assembly_2206231245)%20AND%20OrderId%20CONTAINS%20(0)&LDMS=Y</link>
<description>...Mr WYNNE (Richmond—Minister for Planning, Minister for Housing) (10:11): I move: That this bill be now read a second time . I ask that my second-reading speech, sadly, be incorporated into Hansard. Incorporated speech as follows: This Bill makes amendments to the Residential Tenancies Act 1997 and the Housing Act 1983. Amendments to the Housing Act 1983 In November 2020 the government announced the creation of Homes Victoria as part of its $5.3 billion Big Housing Build. The Big Housing Build is the largest investment in housing in Victoria’s history and will deliver over 12,000 homes including 2,400 affordable ...</description>
<category>59</category>
<guid isPermaLink="true">http://hansard.parliament.vic.gov.au/?IW_INDEX=Hansard-2022-1&IW_FIELD_TEXT=SpeechIdKey%20CONTAINS%20(23-06-2022_assembly_2206231245)%20AND%20OrderId%20CONTAINS%20(0)&LDMS=Y</guid>
<pubDate>Thu, 23 Jun 2022 00:00:00 +1000</pubDate>
</item>
</channel>
</rss>Build
Enjoy access to JetBrains tools as it provides a broader set of IDE for different programming languages such as Python, Java, and Kotlin.

Use Bootstrap Studio to create responsive websites using the Bootstrap framework.

Polypane cares about making your site responsive, fast and accessible, including over 80 accessibility tests, 14 different emulators and two dozen tools.

Launch
GitHub Pages allows you to launch websites for you and your projects. Hosted directly from your GitHub repository. Just edit, push, and your changes are live.

Digital Ocean provides simple cloud hosting, built for developers.

Learn
Have fun learning how to code with TwilioQuest, an educational video game designed to teach a new generation of developers how to change the world with code.

Learn while building through Microsoft Azure’s Cloud Advocates Web Development for Beginners course. This 12-week, 24-lesson curriculum teaches you all about JavaScript, CSS, and HTML basics.

Level up on trending coding skills at your own pace with Educative’s interactive, text-based courses.

Offers and additional benefits status blocks and embedded text data...

Home
Privacy policy
TL;DR: Blockchair does not collect personal data or share it with third parties. We don't track you.

server {
    server_name blockchair.com;
    access_log off;
Why is this important?
One of the key advantages of cryptocurrencies is that they enable (pseudo)anonymous transactions. In most cases the user’s address and transaction details are made public and cannot be deleted, but their personal identity remains unknown if no link exists between the user and their blockchain data.

Privacy is at risk when you share any information with third parties. Cryptocurrency exchanges with KYC policies, online retailers that require delivery addresses and web wallets associated with phone numbers all require you to share information.

What’s more, most web servers maintain default logs of your IP address and User Agent (browser name and operating system), the dates and times of your browsing activity and, most importantly, the URLs you visited. Ordinarily, a cryptocurrency address page is only visited by the address owner, while the transaction page is visited by the transaction parties. Blockchain explorers can therefore easily trace the digital fingerprint that links addresses and transactions. Unfortunately, this data is also picked up by the web analytics tools (Google Analytics, Baidu Tongji, Yandex.Metrica), advertising platforms and similar third-party services.

User data can be traced in others ways too. CDN providers like Cloudflare, Incapsula and AWS Shield act as reverse proxies, which means some websites require you to request data from a CDN in order to use the site. You therefore share your information with the provider.

In addition to these data tracking services, there are several other ways how users can be identified online.

HTTP referer: a client request header that allows a server to trace the previous site you visited. Say you visit example.com followed by explorer.com/1YourBitcoinAddress then the former will receive information that you have come from the latter;
Web beacon (bug): an invisible web page element that confirms a user has visited a web page. This is used to collect user analytics;
Cookies: user activity data stored in the user’s browser. Third-party cookies can also be embedded in the site’s code (if it contains elements from other sites);
Evercookie: a JavaScript app that stores zombie cookies on a computer. These cookies are extremely difficult to remove since Evercookie recreates them whenever they are deleted;
Device / browser fingerprint: the device and browser information collected for user identification;
Browser extensions.
Why is it unsafe to share you personal data?
Most blockchain explorers and cryptocurrency companies store user information, including available balances, lists of transactions and types of cryptocurrency.

They might sell this information, publish it, share it with government agencies, or they might be hacked. If it becomes public knowledge that you have significant funds stored in cryptocurrency, you’re likely to be targeted by cyber criminals. Your personal safety may be at risk too.

Why is Blockchair the safer option?
When you connect to Blockchair your browser automatically sends us information about your computer, User Agent, IP address, and the page you want to visit. Since this data may expose your identity, we do not permanently store information about you;
We do not use cookies that can be used to identify you. We may only set our own cookies to improve your user experience and help us to fight botnets and spammers. See below for details;
Your browser won’t send HTTP referer headers when leaving Blockchair.com. This means you can move to other sites without your browsing activity being traced by those sites;
We do not use CDN-providers, including those used to distribute JavaScript libraries and styles. We do not use any third-party site elements, web analytics tools (such as Google Analytics) and hit counters. Therefore, other parties do not receive information about you.
We do not collect any user data, neither on ours nor third-party servers in our “Blockchair” Chrome Extension.
What data do we store and how do we use this data?
We only collect anonymous aggregated data that allows us to improve our website features. We count visitors, analyze popular searches, cryptocurrencies, sortings and other queries.

We also store the incoming IP addresses in masked or clear form for short periods of 1 to 2 days. This is to limit the rate of API requests.

Your device may store first-party cookies, such as those that keep the night mode on, store referer information, unique visitor and session ID.

Collected data is used to improve user experience and compile website traffic statistics. Session data is deleted on a regular basis.

We can also store and use the data you provide us through email or with other channels of communication such as Telegram or contact forms located on our website. We can use the stored data to provide you with our services, to defend our legal rights, to improve accuracy, effectiveness, security, usability of our products or we can use it in any other way you will agree to.

Overall, we won't keep your data longer than necessary.

Please, be informed, that this Privacy Policy applies on all Blockchair products and has force only in a part where it doesn't contradict to Terms of Service of any product of Blockchair Limited. This Privacy Policy provides a general legal framework for the data collection in Blockchair products, hence the respective Terms of Service for each Blockchair product can regulate this issue differently within its respective scope of applicability. In case of contradiction between provisions of any Blockchair Terms of Service and this Privacy Policy, the provisions of Blockchair Terms of Service in question should prevail.

Privacy Policy updates
We will publish any updates to our Privacy Policy at this page (https://blockchair.com/privacy) and in the GitHub repository at https://github.com/Blockchair/Blockchair.Support/blob/master/PRIVACY.md plus the link to the updated version will be available at the bottom of all our site pages.

Contacts
Please share your comments and suggestions at <danielleahy304@gmail.com>.

<!--
Thank you for contributing to this project! You must fill out the information below before we can review this pull request. By explaining why you're making a change (or linking to an issue) and what changes you've made, we can triage your pull request to the best possible team for review.
-->

### Why:

Closes [issue link]

<!-- If there's an existing issue for your change, please link to it in the brackets above.
If there's _not_ an existing issue, please open one first to make it more likely that this update will be accepted: https://github.com/github/docs/issues/new/choose. -->

### What's being changed (if available, include any code snippets, screenshots, or gifs):

<!-- Let us know what you are changing. Share anything that could provide the most context.
If you made changes to the `content` directory, a table will populate in a comment below with links to the preview and current production articles. -->

### Check off the following:

- [x] I have reviewed my changes in staging (look for the "Automatically generated comment" and click the links in the "Preview" column to view your latest changes).
- [x] For content changes, I have completed the [self-review checklist](https://github.com/github/docs/blob/main/contributing/self-review.md#self-review).

### Writer impact (This section is for GitHub staff members only):

- [x] This pull request impacts the contribution experience
  - [x] I have added the 'writer impact' label
  - [x] I have added a description and/or a video demo of the changes below (e.g. a "before and after video")

<!-- Description of the writer impact here -->
CoinTracker logo
CoinTracker
Partner
CoinTracker is a portfolio assistant for cryptocurrency. It is used by over 100,000 cryptocurrency holders and tracks $20B of cryptocurrency transaction volume. CoinTracker supports 300+ exchange & wallet integrations and over 3,000 cryptocurrency integrations.
CoinTracker enables seamless tracking of cryptocurrency portfolios, investment performance, DeFi, and taxes. Beyond crypto, CoinTracker is building a general automated financial assistant for all financial assets.
CoinTracker has partnered with Coinbase, Intuit, and other industry leaders to make crypto taxes simple, and is venture-backed by Y Combinator, Initialized Capital, and Serena Williams.

https://www.cointracker.io 
Go to compare
Recommended for
Bitcoin, Bitcoin Cash, Ethereum, Ripple, Litecoin, Monero, Dogecoin, Zcash, EOS, Cardano, Stellar, Dash
Languages
English
Service provision
Usa, Australia, United Kingdom, Canada
Tax methods
Fifo, Lifo, Hifo, Acb, Share Pooling
Platforms
iOS, Android, Web
Integrations with other Tax software
Turbotax, Taxact
Pricing
$0-$199
Country of residence
USA

---
## [clamor-s/u-boot](https://github.com/clamor-s/u-boot)@[bede0d2167...](https://github.com/clamor-s/u-boot/commit/bede0d216730d95d58f416058fbdf24f390dea30)
#### Friday 2022-07-08 11:34:16 by Marcel Ziswiler

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
## [projects-nexus/nexus_kernel_xiaomi_gauguin](https://github.com/projects-nexus/nexus_kernel_xiaomi_gauguin)@[2a87f46231...](https://github.com/projects-nexus/nexus_kernel_xiaomi_gauguin/commit/2a87f46231524e772a1932e245156fc6824ccace)
#### Friday 2022-07-08 13:50:29 by Angelo G. Del Regno

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
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: kawaaii <kawaaii@nocturn9x.space>

---
## [Sinbest/thewasteland](https://github.com/Sinbest/thewasteland)@[b052462833...](https://github.com/Sinbest/thewasteland/commit/b052462833fe607463547d4cdd670f1e48e9922c)
#### Friday 2022-07-08 14:07:09 by BadAtThisGame

Overheat warnings to both gatling guns (#742)

* The notorious

* Epic

* FUCK YOU

* I am going to beat you with a club

---
## [nogoodidea/Shiptest](https://github.com/nogoodidea/Shiptest)@[031c0866ed...](https://github.com/nogoodidea/Shiptest/commit/031c0866ed35af71a3ac4782fe4d6aa9e6464f53)
#### Friday 2022-07-08 14:22:13 by SweetBlueSylveon

Nanotrasen Deserter Vault Ruin (#732)

* Nanotrasen Deserter Vault Ruin

A ruin based around a Nanotrasen ultra secure vault. It should spawn on the ice planet. This commit adds everything.

* Map Changes

-Replaces Glockroach family with Jack and Jill, Slaughter and Laughter demons.
-Replaces Sniper Rifle with Particle Acceleration Rifle.
-Replaces Sniper Rifle ammo with a single upgraded weapon power cell.
-Adds a sentience potion and cns rebooter implant to vault safe since there were only mats in it otherwise.

* Minor commit

Removes a cybernetic that should have been removed before the last commit.

* Update code/game/area/areas/ruins/icemoon.dm

I'm dumb and didn't realize I did this. Also didn't realize linters was the code checker, so I didn't realize to check the code. I know now! Thanks for the help.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* Adds the knight gear design disk.

Adds the "magical disk of smithing" to the safe.

* Unmodularizes your Modularization

Moves the datum to an unmodularized folder.

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [shrinemint/RPGGame](https://github.com/shrinemint/RPGGame)@[3bcea596b4...](https://github.com/shrinemint/RPGGame/commit/3bcea596b456e9a8d34313cb0fb919ead3d1a2a4)
#### Friday 2022-07-08 15:36:45 by shrinemint

fuck you i added like five new files and folders you can't and wno't stop me!

---
## [josephfrazier/Reported-Web](https://github.com/josephfrazier/Reported-Web)@[0ec59081cc...](https://github.com/josephfrazier/Reported-Web/commit/0ec59081cc2c28999b878521bb2d943f390b5a75)
#### Friday 2022-07-08 15:37:33 by Joseph Frazier

Disable zoom on mobile devices to avoid unescapeable map issue (#346)

This fixes https://github.com/josephfrazier/Reported-Web/issues/344 by
preventing zoom entirely, on mobile devices:

> From https://reportedcab.slack.com/archives/C9VNM3DL4/p1657204889174239?thread_ts=1656783831.210109&cid=C9VNM3DL4:
>
> > > UPDATE: you appear to have fixed #2 by disabling pinching, but this also makes map view crash easily (on my first two tries, once it crashed and sent me back to Reported login, then it crashed and sent me to a Chrome "Can't open this page" (edited)
> >
> >
> > I don't think I've made any changes relating to pinching or the map in at least a year (if you're curious, you can see the list of changes here), so I'm not sure how to explain the difference in behavior you're seeing.
> > That said, I can try to discuss the issue:
> > > (2) map view issue #1: The only ways to get out of map view are (1) click one of the buttons on the bottom, or (2) touch the grayed-out part of the underlying page. If neither of those is visible, you can't get out of map view. This means that if you pinch the map out (expand it), even accidentally, so that the margin around the map itself is no longer visible, there is no way to get out of map view, you have to reload the page (and re-upload your photo or maybe start the whole report over, I can't remember). (You can't pinch it back in if the entire window is full of map.)
> >
> >
> > I'm curious how you were previously able to pinch-zoom the map/page such that neither the buttons or the margin were visible. When I try (on Android), I can either pinch the map, which only zooms the map while leaving the rest of the page alone, or I can pinch the margin, which zooms the entire page, but the margin is still visible because I'm pinching it.
> > Perhaps things behave differently on iOS?
>
> > Actually the map zoom issue is: if you are zoomed out at all when you enter map view (which you often are, especially on an iPad, and you may not realize it), you’re screwed, because you can’t zoom in (in order to see the buttons or margins, the things you have to click in order to get out of map view) if the only things your fingers can touch are the map itself
>
> > ohhh, I see now, and I was able to reproduce that issue. I wonder if there's a way to detect the zoom level, and prompt the user to zoom back out all the way before they can open the map
> > (side note, I think we're using "zoom in" and "zoom out" with opposite meanings. To me "zooming in" makes the things on screen bigger, and "zooming out" makes them smaller)

---
## [dj-fiorex/angular2-smart-table](https://github.com/dj-fiorex/angular2-smart-table)@[4310b66547...](https://github.com/dj-fiorex/angular2-smart-table/commit/4310b66547d5ceb0464904e68c8fe225a50c72bc)
#### Friday 2022-07-08 16:04:56 by Mike Becker

fixes missing pre-selection in list editor

fixes #87

Note: I have no damn clue why this shitty ngModel auto-magic
does not work properly. So the fix is, that I removed ngModel
from this component and directly work with [value] and (change)
in the hope that this does not break something else.

Signed-off-by: Mike Becker <Mike.Becker@yasc.de>

---
## [tosc-rs/mnemos](https://github.com/tosc-rs/mnemos)@[916909d193...](https://github.com/tosc-rs/mnemos/commit/916909d1936a97d938639ee8f0c9d67f36941712)
#### Friday 2022-07-08 17:11:28 by Eliza Weisman

fix a whole bunch of annoying clippy lints (#7)

* kernel: use `ptr::add` instead of `ptr::offset`

Clippy lints on using `ptr.offset(usize_val as isize)` instead of
`ptr.add(usize_val)`. This fixes that lint (and, I think, makes the code
a bit nicer).

Signed-off-by: Eliza Weisman <eliza@buoyant.io>

* kernel: simplify if chain a bit

As suggested by clippy.

Signed-off-by: Eliza Weisman <eliza@buoyant.io>

* spitebuf: remove useless type conversion

Clippy complains about this: because `pos` and `mask` are already
`usize`s, the `usize::from` does nothing.

Signed-off-by: Eliza Weisman <eliza@buoyant.io>

* spitebuf: rewrite if chain as match

Clippy complains about this and suggests it be rewritten to match on
`dif.cmp(0)`: https://rust-lang.github.io/rust-clippy/master/index.html#comparison_chain

However, there are potential performance issues with using `cmp`, as it
may not always be inlined (see rust-lang/rust-clippy#5354). Therefore,
I rewrote these to use a match without `cmp`, which silences the lint.
I'm...not sure if the resultant code is clearer than the previous code,
so, we could alternatively just add an `#[allow(...)]` attribute for
this lint. @jamesmunns, what do you think?

Signed-off-by: Eliza Weisman <eliza@buoyant.io>

* mstd: remove needless unit return type

Clippy doesn't like that

Signed-off-by: Eliza Weisman <eliza@buoyant.io>

* kernel: use `any` instead of `find(...).is_some()`

Signed-off-by: Eliza Weisman <eliza@buoyant.io>

* spitebuf: use `is_some()` rather than `while let`

Signed-off-by: Eliza Weisman <eliza@buoyant.io>

* kernel: additional bbbuffer if collapsing

Signed-off-by: Eliza Weisman <eliza@buoyant.io>

* allow "missing safety docs" lint

There's a bunch of these and I didn't want to write a # Safety section
for all of this code, especially given that I didn't write it...so I
just turned off the lints.

Signed-off-by: Eliza Weisman <eliza@buoyant.io>

* kernel: return `&'static str` errors in init

Clippy doesn't like functions returning `Result<..., ()>`. This will
also probably make debugging any potential kernel initialization errors
a bit less painful.

Signed-off-by: Eliza Weisman <eliza@buoyant.io>

---
## [CreativeSuzi33/sanctum-vitae-android-app](https://github.com/CreativeSuzi33/sanctum-vitae-android-app)@[f8f01e1f5f...](https://github.com/CreativeSuzi33/sanctum-vitae-android-app/commit/f8f01e1f5f70c4389a70a37fe112dc65c8e59d22)
#### Friday 2022-07-08 18:44:27 by Zuzana Daskova

Update README.md

Táto mobilná aplikácia bola vytvorená na jednoduchšie prehliadanie nových článkov na mnou vytvorených webových stránkach nachádzajúcich sa v sekcii ONLINE. Ďaľšie sekcie sú OFFLINE, GALÉRIA, INFO. Mala by fungovať na operačnom systéme Android 7 (na ktorom bola aj vytvorená). Na iných verziách je potrebné otestovať, či funguje.
V sekcii OFFLINE sa nachádza Katolícky kalendár s menami, sviatkami, myšlienkami sv. Františka Saleského na každý deň v roku a plán čítania Svätého písma a Katechizmu Katolíckej cirkvi (viac o ročnom pláne tu: https://sanctumvitae.wordpress.com/bibliakkc). V tejto sekcii je aj krátky katechizmus a modlitby.
Sekcia GALÉRIA obsahuje obrázky svätých, Ježiša Krista... V sekcii INFO sú okrem informácií aj odkazy na ďaľší obsah na sociálnych sieťach.
KRSTOM SME SA STALI BOŽÍMI DEŤMI! A preto: Vítam vás na mojej (katolíckej) misii!
..........

This Android application was created for easier browsing new articles of my Webs. It is in the section ONLINE. Some websites are in the English language (because it is an international language).
There is a section OFFLINE too. There are the Catholic Calendar (with the names, holidays and the yearly plan of reading of the Catholic Bible and some thoughts of St Francis Sales), the Catholic Catechism and the prayers. More about the yearly plan here: https://sanctumvitae.wordpress.com 
The section GALLERY contents the pictures of the holy people and the pictures of the God and the Holy Trinity.
Some information and the urls are in the section INFO.
Welcome to my Catholic mission!

---
## [Noobetski/sojourn-station](https://github.com/Noobetski/sojourn-station)@[796aeaa98f...](https://github.com/Noobetski/sojourn-station/commit/796aeaa98f76c2a6ef7a94e540d3b8f7efcb027b)
#### Friday 2022-07-08 19:32:38 by lolman360

fixes stacks deleting randomly (#3357)

* whoo

* god i fucking hate stackcode

thank you kevinz

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[fdd8036140...](https://github.com/tgstation/tgstation/commit/fdd80361406f7b9ff8568237a933f9926b527c28)
#### Friday 2022-07-08 19:52:46 by BluBerry016

Revisiting The Goliath: Or, that time I dripped out the SBC Starfury just because (#68126)

Drips the SHIT out of the SBC Starfury while not completely overhauling it. Touches everything NOT in engineering or southward (because I love how scuffed that part is and refuse to touch it on principle) - Also converts one map varedit into a real boy subtype, and moves tiny fans to their own file.

Mandatory disclosure on the gameplay changes:
Fighters 1 and 3 are now NOT in the hangar, and are now attached to the formerly unused gunnery rooms.
Cryo now works. Yeah. I know.
You can actually open the anesthetic closet now.
Everyone now shares three spawners. This doesn't reduce the amount of people who can play when this rolls, as I've adjusted var/uses in accordance: it just reduces clutter.
A few of the horizontal double airlocks have been compacted into glass_large airlocks.
The bar windows now actually have grilles like they were meant to.
Four turbines have shown up. They aren't functional*, they just look like gunnery and conveniently fit in the spots. I'm sure this is space OSHA compliant.
The map is ever so slightly smaller, vertically. This should distance us from an edge case where somehow all space levels are too cluttered for this to spawn properly, for the time being.

*Technically there's nothing stopping you from using them besides the amount of time it'd take for the operatives to kick your ass

This map was originally designed wayyy back before we even had the computer sprites we have now, (#27760 if you want to see SOUL) and it shows. While it will never have it's SM again, we can at least make the thing much nicer to look at.

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[9ccd6ecd74...](https://github.com/microsoft/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Friday 2022-07-08 21:16:30 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER)@[0bf830e57c...](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/commit/0bf830e57c77f6508b9a1639c6d5c7607af95276)
#### Friday 2022-07-08 23:11:29 by WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER

#### THIS PAGE IS BEING MONITORED BY SEVERAL DEPARTMENTS AS PART OF A FEDERAL BANK AND SECURITIES FRAUD INVESTIGATION.

[https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/tree/main](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/tree/main)<br>

### NOTWITHSTANDING THE US. DEPT OF JUSTICE.
18 U.S. Code § 1512 - Tampering with a witness, victim, or an informant<br>

*** Fwd: Fwd: [ USC Title 18.1512 ] [USC Title 18.225, USC Title 18.21, USC Title 18.4, USC Title 18.3, USC Title 18.2]<br>

NYSCEF MATTER 153974/2020 WHILE THEY CASUALLY VIOLATED MY CIVIL RIGHTS<br>

NO COMPLAINTS HAVE BEEN FILED IN MY BUILDING<br>

- PER DEPARTMENT OF BUILDINGS RECORD CONTRARY TO THOSE "COMPLAINTS" WHICH ARE UN-TRUE.<br>
<https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=AgwH2omenQPCvT0OYOE3Rg==><br>


### ACCESSORIES TO THIS OTHER FILING

HALE DINCER <+15168841083@tmomail.net>, SHARI LASKOWITZ <slaskowitz@ingramllp.com>,<br> 
SHARI LASKOWITZ <+13478801899@tmomail.net> , HALE DINCER <hidincer@aol.com> <br>
PAUL REGAN <legal@mskyline.com>, LAURIE ZUCKER <lzucker@mskyline.com>, <br>
DAPHNE DINCER <DAPHNE.DINCER@GMAIL.COM>, ASHLEY HUMPHRIES <ASHLEY.HUMPHRIES@WILSONESLER.COM>, <br>
CORY WEISS <CWEISS@INGRAMLLP.COM>, ANA LOPEZ <LEGALASST@MSKYLINE.COM>, <br>
DONALD ZUCKER <ADMINISTRATOR@MSKYLINE.COM>, STEPHEN O'CONNEL <SGO2107@COLUMBIA.EDU>, <br>
<br><br>
[VOICEMAIL FROM PAUL REGAN: AFFIRM THE THREAT](https://support.nysba.org/attachments/token/TQXA7meSdnDIBt5SuKAuW0imP/?name=voicemail+917-843-3456.mp3)
*** CHECK THAT THREAD AND GET BACK TO ME AS WELL PLEASE.
While dealing with their business in Brooklyn, New York. <br>
— Kept me pre-occupied without cause to take care of their other business without my opinion or any reveal as to what they really do for a living.<br>
<br>
For example:

>> Hon. Nancy T. Sunshine, Kings County Clerk <br>
         and Clerk of the Supreme Court <br>

<https://iapps.courts.state.ny.us/nyscef/ConfirmationNotice?docId=HD6/wXvlOxflJUlQyXqedQ==><br>

     case number:          400842/2020<br>
     Filed:                        09/23/2020<br>
     *** KINGS COUNTY *** <br>

Zucker Enterprises LLC <br>
             - v. - 
THE TAX COMMISSION OF THE CITY OF NEW YORK, AND THE COMMISSIONER OF FINANCE OF THE CITY OF NEW YORK


>> 6.24.2020 email - ASHLEY.HUMPHRIES@WILSONELSER.COM

THIS REPORT WAS ALSO OBSTRUCED - WHILE IN TRANSIT TO THE DEPARTMENTS WHERE APPLICABLE<br>

[VOICEMAIL FROM GENERAL COUNSELOR OF MANHATTAN SKYLINE MANAGEMENT CORP.](https://support.nysba.org/attachments/token/IC0wkjtvvpbslRI5FmvzN5eV7/?name=voicemail+917-843-3456.mp3)

<br><br>
### THREATENING AND IMPEDING A FEDERAL INVESTIGATION OF BANK AND SECURITIES FRAUD, AND SLOWING THE RELEASE OF INFORMATION BY UNLAWFUL RESTRAINT, WILLFULLY AND KNOWINGLY IS NOT SOMETHING THAT IS EXEMPT FOR FEDERAL AGENTS AND NON-FEDERAL PERSONS.
[VOICEMAIL FROM PAUL REGAN, GENERAL COUNSELOR OF MANHATTAN SKYLINE MANAGEMENT CORP.](https://support.nysba.org/attachments/token/IC0wkjtvvpbslRI5FmvzN5eV7/?name=voicemail+917-843-3456.mp3)
<br><br>
### BANK INVESTIGATION
[VOICEMAIL FROM THEIR FRAUD DEPT. IN RESPONSE TO RECEIPT OF THE INFORMATION BY MR. KILKENNY](https://support.nysba.org/attachments/token/Sr0PKDdRavjlpFkIt7jc95QLq/?name=voicemail-218-CHASE+BANK.m4a)
<br><br>
[VOICEMAIL:: FROM THE BANK FRAUD DEPT. AT CHASE BANK](https://support.nysba.org/attachments/token/YNvrvCEnT6nrcydcPwB6lBXnO/?name=voicemail-215-CHASE+BANK.m4a)
<br><br>
[VOICEMAIL:: FROM JP MORGAN CHASE-FRAUD INVESTIGATIONS DEPARTMENT](https://support.nysba.org/attachments/token/1vZon2Sk7PB6esmpj3zVHUJja/?name=voicemail-222-JPM-CHASE.m4a)
<br><br>
[VOICEMAIL:: FROM CHASE BANK-FRAUD INVESTIGATIONS DEPARTMENT](https://support.nysba.org/attachments/token/OjDtdOSzaoQEpaoYABSwvHPXV/?name=voicemail-218-CHASE+BANK.m4a)

### SECURITIES FRAUD INVESTIGATION
[VOICEMAIL FROM THE SECURITIES REGULATORS](https://support.nysba.org/attachments/token/6tdqvD6K1AyrccbjgJ2MBK7GT/?name=voicemail-214-Finra.m4a)
<br><br>
[VOICEMAIL FROM THE SECURITIES REGULATORS](https://support.nysba.org/attachments/token/4BDa9lAjkbEe66TEBUZaTZYlR/?name=voicemail-217-FINRA+2.m4a)



![image](https://user-images.githubusercontent.com/108204659/177884161-999f6aed-886b-4490-9968-99bbd76ee5d5.png)

#### THIS PAGE IS BEING MONITORED BY THE DEPT. OF JUSTICE
#### AS WELL AS SECURITIES & BANK REGULATORS AS WELL.

![image](https://user-images.githubusercontent.com/108204659/177884550-5fac5c64-ab6d-483e-af6d-a8242ae018ee.png)


USC 18 TITLE 18- SECTION 1512 - PREVENTING COMMUNICATION TO A LAW ENFORCEMENT OFFICER OR JUDGE.txt
> https://support.nysba.org/attachments/token/sWoZTvp3jCzQBDpiHj8pRGrhV/?name=NOTICE+TO+SECURITIES+AND+EXCHANGE+-+NOVEMBER+13TH+2021.png


USC 18.1512 - Tampering with a witness, victim, or an informant
(a)
(1)Whoever kills or attempts to kill another person, with intent to—<br>
(A)prevent the attendance or testimony of any person in an official proceeding;<br>
(B)prevent the production of a record, document, or other object, in an official proceeding; or<br>
(C)prevent the communication by any person to a law enforcement officer or judge of the United States of information <br>

relating to the commission or possible commission of a Federal offense or a violation of conditions of probation, parole, or release pending judicial proceedings;<br>
shall be punished as provided in paragraph (3).
(2)Whoever uses physical force or the threat of physical force against any person, or attempts to do so, with intent to—
(A)influence, delay, or prevent the testimony of any person in an official proceeding;
(B)cause or induce any person to—
(i)withhold testimony, or withhold a record, document, or other object, from an official proceeding;
(ii)alter, destroy, mutilate, or conceal an object with intent to impair the integrity or availability of the object for 

use in an official proceeding;
(iii)evade legal process summoning that person to appear as a witness, or to produce a record, document, or other object, 

in an official proceeding; or
(iv)be absent from an official proceeding to which that person has been summoned by legal process; or
(C)hinder, delay, or prevent the communication to a law enforcement officer or judge of the United States of information  relating to the commission or possible commission of a Federal offense or a violation of conditions of probation, supervised release, parole, or release pending judicial proceedings; shall be punished as provided in paragraph (3).
(3)The punishment for an offense under this subsection is—<br>
(A)in the case of a killing, the punishment provided in sections 1111 and 1112;<br>
(B)in the case of—<br>
(i)an attempt to murder; or<br>
<br>
<br>
<br>
(ii)the use or attempted use of physical force against any person;
imprisonment for not more than 30 years; and
(C)in the case of the threat of use of physical force against any person, imprisonment for not more than 20 years.
(b)Whoever knowingly uses intimidation, threatens, or corruptly persuades another person, or attempts to do so, or engages in misleading conduct toward another person, with intent to—<br>
(1)influence, delay, or prevent the testimony of any person in an official proceeding;<br>
(2)cause or induce any person to—<br>
(A)withhold testimony, or withhold a record, document, or other object, from an official proceeding;<br>
(B)alter, destroy, mutilate, or conceal an object with intent to impair the object’s integrity or availability for use in an official proceeding;<br>
(C)evade legal process summoning that person to appear as a witness, or to produce a record, document, or other object, in an official proceeding; or<br>
(D)be absent from an official proceeding to which such person has been summoned by legal process; or<br>
(3)hinder, delay, or prevent the communication to a law enforcement officer or judge of the United States of information relating to the commission or possible commission of a Federal offense or a violation of conditions of probation?[1] supervised release,,[1] parole, or release pending judicial proceedings;
shall be fined under this title or imprisoned not more than 20 years, or both.
(c)Whoever corruptly—
(1)alters, destroys, mutilates, or conceals a record, document, or other object, or attempts to do so, with the intent to  impair the object’s integrity or availability for use in an official proceeding; or
(2)otherwise obstructs, influences, or impedes any official proceeding, or attempts to do so,
shall be fined under this title or imprisoned not more than 20 years, or both.
(d)Whoever intentionally harasses another person and thereby hinders, delays, prevents, or dissuades any person from—
(1)attending or testifying in an official proceeding;
(2)reporting to a law enforcement officer or judge of the United States the commission or possible commission of a Federal offense or a violation of conditions of probation?1 supervised release,,1 parole, or release pending judicial proceedings;
(3)arresting or seeking the arrest of another person in connection with a Federal offense; or
(4)causing a criminal prosecution, or a parole or probation revocation proceeding, to be sought or instituted, or assisting  in such prosecution or proceeding;
or attempts to do so, shall be fined under this title or imprisoned not more than 3 years, or both.
(e)In a prosecution for an offense under this section, it is an affirmative defense, as to which the defendant has the burden of proof by a preponderance of the evidence, that the conduct consisted solely of lawful conduct and that the defendant’s sole intention was to encourage, induce, or cause the other person to testify truthfully.
(f)For the purposes of this section—
(1)an official proceeding need not be pending or about to be instituted at the time of the offense; and
(2)the testimony, or the record, document, or other object need not be admissible in evidence or free of a claim of privilege.
(g)In a prosecution for an offense under this section, no state of mind need be proved with respect to the circumstance—
(1)that the official proceeding before a judge, court, magistrate judge, grand jury, or government agency is before a judge or court of the United States, a United States magistrate judge, a bankruptcy judge, a Federal grand jury, or a Federal 

Government agency; or
(2)that the judge is a judge of the United States or that the law enforcement officer is an officer or employee of the 

Federal Government or a person authorized to act for or on behalf of the Federal Government or serving the Federal 
Government as an adviser or consultant.
(h)There is extraterritorial Federal jurisdiction over an offense under this section.
(i)A prosecution under this section or section 1503 may be brought in the district in which the official proceeding (whether or not pending or about to be instituted) was intended to be affected or in the district in which the conduct constituting the alleged offense occurred.
(j)If the offense under this section occurs in connection with a trial of a criminal case, the maximum term of imprisonment 

which may be imposed for the offense shall be the higher of that otherwise provided by law or the maximum term that could have been imposed for any offense charged in such case.
(k)Whoever conspires to commit any offense under this section shall be subject to the same penalties as those prescribed for the offense the commission of which was the object of the conspiracy.



https://p19.zdusercontent.com/attachment/2434074/ONbQ6pgTKks3c7ZOi7ogr5Tmw?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..3SjoQz4kWEi0rs9s2TaiEQ.vqh9vZOliebGAA7r_IAD3893gc7TngmluyELeyK6hlmM24B-N0MOgudGHR1hynRx9KVZzI8Uvd1qs3AOfI-LlkTYh2vJJXFeP4a8f2u5bWyX29wD9KaAUqHgDIIItlYCuSnUh0SYnKBzOksD2nS3r33QdlhvO42yNCiFNYXSImfoXQWqRqOfka--aYE-EqRRc5IMcu-kHuJQcECfIwvtib0UzjoDJVW06oJxo4ky43kwZRRf8aNwFa1iotqh3LxmBd-zobcKVlx5UTPeO6K_9ZMS5K3Z8avS5jSyDpKDnRs.m7JFjFS10LZZ6MM9I2WaSw

ASSETS WERE MOVED FROM HSBC TO JP MORGAN WITH INTENT, WHILE THEY WATCHED ME 24/7 WITHOUT CONSENT
-- I HAVE BEEN MOVING FROM HOTEL TO HOTEL FOR THE LAST YEAR.

LOAN DOCKET 50074 - SECTION 1.4 -- INDEMNITY [ FILED DOCKET 312, NYSCEF 153974/2020 ]

https://p19.zdusercontent.com/attachment/2434074/bRuZFokaqoqfgjc3xm4nD7Kbl?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..rj4zRlhnEynh5xC5tRAsdw.Akdv3TBc3QL15x7Svb5XF0K2c2lBcBfPyZLDaPg_PZVBj3S69mGtub9499SNJ74R8D76QZeOTL4-WrNgdTSfMQYXQy6wXPDbNwGF5hWVkLpgL8tydYFlPjXCmIpLEZQJqPoANQvJqKwnyD1RRsZkLfvkfw_Dcs0lKp3f8R4t-vxhNXheMkjefym37BE1YFG2ENmdgH_nzZjwe-pIKg5u0U9QLB7jpwbsEmS2m9KjA1ZtXH23MXXmrpl0aqfU5EFjZFc2uSlq2PQ5IMyyTS_zfVpQxUuHXxXg8EN0gxr-GN8.oQ1y0ciEygiKjcBxj9UjOQ



[ MULTIPLE DWELLING LAW ]
" VIOLATION SHALL BE DEEMED TO EXIST IN THE RESPECTIVE PREMISES OF EACH RESIDENT IN THE OF THE MULTIPLE DWELLING "

https://p19.zdusercontent.com/attachment/2434074/8rbRQgVwJiGq3SGb6uIEsoGtK?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..K6J2ULKdIHHBx-zQOLpglg._AJoI_e3EmI8H7sGgLNVKy2C_EyHtNAb7FwNCJBqZNBx884x235cF6iVlAYSpGqcvX7yLFRtXBy-ChEW1nZkEqgV4f-V-Fg5OjnAsqYxLF-Pe2xBftkhkIGUDxgv5D8dOV3aHHVIK47WttG2VqVAXI5JBwti-hPF75wl-F6fDOh12qW2wX9Rwgw_ImJ3IPuGbEi52AzKc4Ups4H6yQ3-K06wPhZJjEb9t7pBAIqDP6VTZJQm784MYXs1EuVKqKv45lri7frMeZ2rWknN3zTi84zulFTdO0JLzPhyyviKUcA.YVZRL6uopA2xoxo5Z0g_0g




https://p19.zdusercontent.com/attachment/2434074/uwSPB9MeN0sX9yCIpaJ5LMB5q?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..oLI-sr6rVXQadNEVBJWSEA.Ngi9SXK3B5PgxbdPgf3ckSMOMao5Iz4d2z4Ps7aSvQtRKDKoU0fM_AqBz-wpDUmxSwY6iDwuFmsOmCxfr39Cz0P5S3QZNw1wsEQNpaXXlmy7nTtBmzU6ZYCO4ltyeq2fNKE7yonX7zb4E2JgzP2nxS3bPvU38izJxSw_2PWelHgOfvwQRT54rddQKiU_BDzjpcivfrBE2qGrR9n0xOB9QMt9BIHqwObdFUJQ8PVAkkLqguC8UAO5IJVXKJGeqCOfvIWcLS15RdtiLZey-GAmyAithpHb5a8o2CUIfLHAgCQ._K2fJ4EXrRbSo9Lqvy7E0g



https://p19.zdusercontent.com/attachment/2434074/AYudhpqVy5YzILECrrdqtYsDy?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..nOxmXbOvQZhADrGwCKLmRw.WEw5YfrAtg8unWagIHaxV9saUh6qWBNn-SADb1r3UxoBl61YY2fZsf68u2xhPCbmlG_QNl772EFppalHUuwCqQGTlMWqUJB2we3mkr95OV4jyIdRuXS4A-xm1jsvqpHXc76YJq3l1Li5_lymyzwI7uryDFHU5wHohAjRY6c1N0LeB6SxBwr_gmmBJ24aLcCD3C8iRgVG3HPhVzEsMM8Zp6vOWsdd0P-lcnGEsTVzb45weGg3IzQaIujIr54lviBQyZ5UWAgqVpw-JJQpdjBaehkhQg3Xh6Tfdiz4AkXa7xU.jXgsCJZx6rRTEQxRRHVkjw

https://p19.zdusercontent.com/attachment/2434074/uXmPQ38BhOoS81BORcN189epx?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..n4U1r1-tCk7t8cNgh9l6qA.02kR4RvYtLmbEC2P_3GfDG-tUSVdn6pgvny8OS0l_ZMOHL2jcezbnENLMSFh_CNstpOmDaqfoGMr8FWmisP6slmqPzi2U2ZKN2kAFFusE2mGYWB5jNNEnpdC-bd-Ow3WyYU3vflrPTD9WeUhEOdqoxc5PeCVxR6sjcUmA66NxwCHVWLYKygvrIEdyTkzBbnR61Hkh6CulGiTVBvJPk5NHXDo1d_TaOZqKHDtlbRxCRpleIwObZne4tRdIfDe5IE0lSjgjQkgph5OSMNiC9_2QEC-FoaClgJU0OdL36vrzMw.R88r1lKgxCZfE7W9bu9aug


https://p19.zdusercontent.com/attachment/2434074/M2hlv45SVnHpSrWTNDuNYRmxl?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..S7yNlZ0mN5HiQiGGBLM73A.25SArygzhrF8LF4nA0IfEmdMPSZXt4bFllgiUVO8ZFOY7khexBtnjk9_jeNDukOcRIIsPR6VjT-2oQuMkRQbkqEDUhLJcTzFajpOf66EQKMTJZyR0NxOVPQm6rgjAqOubENq-9RT2NFenseWU25b8soJfqUJopB7sG0c1LJP-QQIk8H76vyFYA6UVm6sofzoSG9dHSTL3RUZTDEia0xUnnj66XturYId3uNRusYChWgtCE0K6CpWR3_Dvav291hEvMM8Ie7mQ6cSH8DCKXhymf6cFTNGOIF6gLfcuiyis-w.FYY9DAufaZkkghSdyGptJA

https://p19.zdusercontent.com/attachment/2434074/mlWG3uUj3n19hbg5MKEXJUFgp?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..TOGbWTBvbrYpIlmg9T0-Cw.hHOxQ2gpUui30mCRbddQnHEZn_Zt9JKYVG8hCCyIuhqpPXjGAk32GdJGmSNcuTV2npbYcQSOx1VGXUjKYtQtxuNbdhJCH_OV0HUmks8G4i35Q67sLhSMp6Dw-ShyhgU91yyngJV1qzVX8J5FzAJg3x0JtFx9hyFYRTaDXOrszE1gDIajfrbaSkilm4ATWLYp5ert99e1IlPDf5o98g1bSgVZGLt5gSEKVH9h4ymCC36YGj170kviC-Dc28FARWz2EXSvoVGByxkYAdfe8fVfO70FE95g3J7EvCWslr3dqGw.sxuBmVikIEuhtXsDBYiSmA



https://p19.zdusercontent.com/attachment/2434074/8rbRQgVwJiGq3SGb6uIEsoGtK?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..K6J2ULKdIHHBx-zQOLpglg._AJoI_e3EmI8H7sGgLNVKy2C_EyHtNAb7FwNCJBqZNBx884x235cF6iVlAYSpGqcvX7yLFRtXBy-ChEW1nZkEqgV4f-V-Fg5OjnAsqYxLF-Pe2xBftkhkIGUDxgv5D8dOV3aHHVIK47WttG2VqVAXI5JBwti-hPF75wl-F6fDOh12qW2wX9Rwgw_ImJ3IPuGbEi52AzKc4Ups4H6yQ3-K06wPhZJjEb9t7pBAIqDP6VTZJQm784MYXs1EuVKqKv45lri7frMeZ2rWknN3zTi84zulFTdO0JLzPhyyviKUcA.YVZRL6uopA2xoxo5Z0g_0g


https://p19.zdusercontent.com/attachment/2434074/bRuZFokaqoqfgjc3xm4nD7Kbl?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..rj4zRlhnEynh5xC5tRAsdw.Akdv3TBc3QL15x7Svb5XF0K2c2lBcBfPyZLDaPg_PZVBj3S69mGtub9499SNJ74R8D76QZeOTL4-WrNgdTSfMQYXQy6wXPDbNwGF5hWVkLpgL8tydYFlPjXCmIpLEZQJqPoANQvJqKwnyD1RRsZkLfvkfw_Dcs0lKp3f8R4t-vxhNXheMkjefym37BE1YFG2ENmdgH_nzZjwe-pIKg5u0U9QLB7jpwbsEmS2m9KjA1ZtXH23MXXmrpl0aqfU5EFjZFc2uSlq2PQ5IMyyTS_zfVpQxUuHXxXg8EN0gxr-GN8.oQ1y0ciEygiKjcBxj9UjOQ



https://p19.zdusercontent.com/attachment/2434074/bRuZFokaqoqfgjc3xm4nD7Kbl?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..rj4zRlhnEynh5xC5tRAsdw.Akdv3TBc3QL15x7Svb5XF0K2c2lBcBfPyZLDaPg_PZVBj3S69mGtub9499SNJ74R8D76QZeOTL4-WrNgdTSfMQYXQy6wXPDbNwGF5hWVkLpgL8tydYFlPjXCmIpLEZQJqPoANQvJqKwnyD1RRsZkLfvkfw_Dcs0lKp3f8R4t-vxhNXheMkjefym37BE1YFG2ENmdgH_nzZjwe-pIKg5u0U9QLB7jpwbsEmS2m9KjA1ZtXH23MXXmrpl0aqfU5EFjZFc2uSlq2PQ5IMyyTS_zfVpQxUuHXxXg8EN0gxr-GN8.oQ1y0ciEygiKjcBxj9UjOQ



https://p19.zdusercontent.com/attachment/2434074/bRuZFokaqoqfgjc3xm4nD7Kbl?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..rj4zRlhnEynh5xC5tRAsdw.Akdv3TBc3QL15x7Svb5XF0K2c2lBcBfPyZLDaPg_PZVBj3S69mGtub9499SNJ74R8D76QZeOTL4-WrNgdTSfMQYXQy6wXPDbNwGF5hWVkLpgL8tydYFlPjXCmIpLEZQJqPoANQvJqKwnyD1RRsZkLfvkfw_Dcs0lKp3f8R4t-vxhNXheMkjefym37BE1YFG2ENmdgH_nzZjwe-pIKg5u0U9QLB7jpwbsEmS2m9KjA1ZtXH23MXXmrpl0aqfU5EFjZFc2uSlq2PQ5IMyyTS_zfVpQxUuHXxXg8EN0gxr-GN8.oQ1y0ciEygiKjcBxj9UjOQ


https://p19.zdusercontent.com/attachment/2434074/MJ5xEG1bkHzqj0rY1zESVUgQb?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..t44VVxJ2EqeSYiPGTggD2Q.mr-QvRE4hq65-igubtudoe_PB8Os6IqLmx8cnfe18MSOaoW38_T7woQNJPwA8Gpig0Dx9DeaKztNvggaeBjaHC4eGYEQ-Y6K-frhikrMvn0yWgYLJjNkIoN5uy5S61EOqy9hJFwhHj2N0jYnBLAmzUQgASbBn_AIeMGMW9rU1AAUaLjKiJU2d_Y03zeQy8GTpoQidLKh7Ym88uG4ylclisDqKmC9HnIBXW1_t5AkBiU9yXgtmmlKu0TKXrPfev8Xe9z9p2W-nvgQRlR737tGbi-If8uDFjTKU2_Q0rvh5-Q.bXIbpP9_XcrY90OUJjK8Yg


PLAINTIFF ASSIGNED LEASES AND RENTS ON MAY 15TH TO STATE FARM LIFE INSURANCE COMPANY - INCLUDING THEIR TAX RISKS AS IMPLIED
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=19MVPFXy0G0QvnmRLGpYIQ==
EXHIBIT(S)  - AC0  (Motion #001)
ACRIS Detailed Document Information (2019000021408)2019010800475001
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=ze6a1KA9akRV9TGfXXJT/g==
EXHIBIT(S)  - AC1  (Motion #001)
ACRIS Detailed Document Information (2020000155422)2020052000291003
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=bVk8sIt7n3kGwHqebPg0fw==
EXHIBIT(S)  - AC2  (Motion #001)
ACRIS Detailed Document Information (2020000155421)2020052000291002
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=wTG2YD2PqXuxmoKqFiESrw==
EXHIBIT(S)  - AC3  (Motion #001)
ACRIS Detailed Document Information (2020000155422)2020052000291003
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=au8qh7Dn66hrVmJ9DX_PLUS_bdg==
EXHIBIT(S)  - AC4  (Motion #001)
ACRIS Detailed Document Information (2020000155423)2020052000291004
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=/yhElCiKJ0BGv2DF/MOn4g==
EXHIBIT(S)  - ACR  (Motion #002)
ACRIS.NYC.GOV >> ASSIGNMENT OF LEASE AND RENTS ON FILED ON MAY 26TH
https://iapps.courts.state.ny.us/nyscef/ViewDocument?docIndex=gcMSDaFzm0ynPeXZKSHgLQ==


--- THAT IS UNLAWFUL INCOME
https://support.nysba.org/attachments/token/ONbQ6pgTKks3c7ZOi7ogr5Tmw/?name=image0.jpeg




>> THESE IN THE TO:  ARE THE LINES OF COMMUNICATIONS THEY DISCLOSED.
https://iapps.courts.state.ny.us/nyscef/ConfirmationNotice?docId=_PLUS_TlrEGCsUUcCcvtJ8O/dfg==

18 U.S. Code § 1512 - Tampering with a witness, victim, or an informant<br>
![image](https://user-images.githubusercontent.com/108204659/177089989-edc8dc77-e0f4-4d92-85f0-d9782ece4035.png)



I PROVIDED THEM THIS INFORMATION

*** THAT INFORMATION YOU NEED TO VERIFY STARTS HERE:
*** Lewisohn Hall, 2970 Broadway, New York, NY 10027, United States of America
GPS (40.8084317, -73.9631634)

WHICH IS WHY I AM HERE.
-- THEY ARE PEEPING TOMS, AID AND ABET TO THOSE FELONIES COMMITTED BY

1.    THE ZUCKER ENTERPRISES LLC
2.    SULLIVAN PROPERTIES LLC.

3.    SULLIVAN GP LLC
4.    SULLIVAN PROPERTIES LP
5.    MANHATTAN SKYLINE MANAGEMENT CORP.
6.    STATE FARM LIFE INSURANCE COMPANY
7.    STATE FARM REALTY MORTGAGE LLC.
        PER SHARI'S LETTER WAS REQUESTED "IS OBSTRUCTION OF JUSTICE REQUESTED" NOT TO CONTACT ANOTHER ENTITY TO FURTHER MISLEAD REGULATORS...

8.    STATE FARM ASSURANCES FUNDS TRUST, CIK FILER 93715, RANDOMLY ELECTED TO SELF-IMPLODE
9.    ASSURANCES FUNDS TRUST, PRESENTLY OPERATES WITH THE SAME DIRECTORS UNDER CIK FILER 1516523



INDIVIDIVUALS OF INTEREST FROM NYSCEF 153974/2020 - OBTAINED A LOAN FOR $6 MILLION DOLLARS WHICH SATIFY THE FOLLOWING VIOLATIONS:
    USC TITLE 18.225, 18.21  (USING FALSE AND UNLAWFUL RENT ROLLS FILED WITH THE THE NY DEPT OF FINANCE)
    USC TITLE 18.4, 18.3, 18.2 (WILFULLY KNEW AND CONTINUED THOSE FINANCIAL CRIMES)
   

    1.    LAURIE ZUCKER        DIRECTOR   
                    EMAIL:    LZUCKER@MSKYLINE.COM

    2.    SHARI LASKOWITZ        ATTORNEY   
                    EMAIL:    SLASKOWITZ@INGRAMLLP.COM   
                    TEL:     347-880-1899

    3.    PAUL REGAN        ATTORNEY
                    MANHATTAN SKYLINE MANAGEMENT CORP.
                    LEGAL@MSKYLINE.COM
                    TEL:    917-843-3456

    4.    ASHLEY HUMPHRIES  ATTORNEY
                    WILSON ELSER LAW FIRM
                    LEGAL@MSKYLINE.COM
                    TEL:    917-843-3456
    5.    STEVE O'CONNELL, COUNSELOR TO LAURIE ZUCKER AND WILLIAM MCKENZIE
                EMAIL: SGO2107@COLUMBIA.EDU, LZUCKER@MSKYLINE.COM, WMCKENZIE@NYCOURTS.GOV, LEGAL@MSKYLINE.COM
    6.    WILLIAM MCKENZIE, CLERK IN NYSCEF MATTER 153974/2020
                EMAIL: WMCKENZI@NYCOURTS.GOV

                OBSTRUTED JUSTICE WHILE AIDING AND ABETTING TO IMPEDING A FEDERAL SECURITIES INVESTIGATION,  AS SEEN IN THE COMMUNICATION BELOW ON DECEMBER 22ND, 2021
                - SEE ALSO: STOCK PRICE OF CIK FILER, UNDER TICKER STFGX ON DECEMBER 21, 2021 - LOST COLLECTIVELY AS FOUR TICKERS NEARLY ONE-BILLION DOLLARS IN A DAY AND NO-PUBLIC DISCLOSURE.
                - INFORMATION SHARED BY AND BETWEEN THOSE INDIVIDUALS.             

    A.    HALE DINCER         ACCESSORY
                    - COMMUNICATIONS WITH SHARI LASKOWITZ, ET. AL.
                            -AND DURING THE PROCEEDINGS IN NYSCEF 153974/2020
                            - AND AFTER WHILE I MOVE EVERY 4 DAYS SO THAT I AM MOST EFFECTIVE                             TO PROVIDE INFORMATION TO THE FEDERAL REGULATORS
                            ABOUT AN ONGOING BANK AND SECURITIES FRAUD INVESTIGATION.
    
                            TO AVOID BEING IMPLICATED IN THE FELONIES COMMITTED
                            IN NYSCEF 153974/2020 WAS AT ALL TIMES AWARE.

                    EMAIL:    <HIDINCER@AOL.COM>
                    TEL:        +15168841083@tmomail.net

    B.    DAPHNE DINCER        ACCESSORY
                    - SEE ALSO COMMUNICATIONS WITH SHARI LASKOWITZ, HALE DINCER, ET. AL
                    EMAIL:        <DAPHNE.DINCER@GMAIL.COM>
                    TEL:        +15163224896@tmomail.net

    C.    ANNE BRANDON, ALAMEDA    ACCESSORY
                    EMAIL 1:    <anne@thehighlandpartners.com>
                    EMAIL 2:    <ANNE.D.BRANDON@gmail.com>
\

	
<br>[153974_2020_Sullivan_Properties_L_P_v_Baris_Dincer_EXHIBIT_S__373 - MY VIDEOS WERE HOSTED ON THE INTERNET without consent as well.](https://github.com/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/WILSON-ELSER-STATEFARM-SULLIVAN-ZUCKER/files/9065071/153974_2020_Sullivan_Properties_L_P_v_Baris_Dincer_EXHIBIT_S__373.-.MY.VIDEOS.WERE.HOSTED.ON.THE.INTERNET.pdf)

##### PLAINTIFF ASSIGNED LEASES AND RENTS ON MAY 15TH TO STATE FARM LIFE INSURANCE COMPANY TO PROTECT THEIR INVESTMENT - A SHORT TERM INVESTMENT WITH 30-YEAR TERMS.

#### THIS PAGE IS BEING MONITORED BY SEVERAL DEPARTMENTS AS PART OF A FEDERAL BANK AND SECURITIES FRAUD INVESTIGATION.
### NOTWITHSTANDING THE US. DEPT OF JUSTICE.

>> 6.24.2020 email - ASHLEY.HUMPHRIES@WILSONELSER.COM

---
## [andre4ik3/modpack](https://github.com/andre4ik3/modpack)@[8daecd960e...](https://github.com/andre4ik3/modpack/commit/8daecd960eeb465852908c598d75adac0c6b1bf6)
#### Friday 2022-07-08 23:58:56 by andre4ik3

Add support for mod patching - Remove Bee variants from Quark mod

Holy fucking shit that made me want to puke upon seeing it. Hopefully now none of that disgusting stuff stays anywhere here, and god forbid I get arrested for having that sorta shit on my computer.

On the brighter side, script output is now 300 times more readable, if anyone cares...

---

