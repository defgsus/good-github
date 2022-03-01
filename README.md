## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-02-28](docs/good-messages/2022/2022-02-28.md)


1,676,341 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,676,341 were push events containing 2,672,526 commit messages that amount to 204,758,175 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 24 messages:


## [Official-Ayrton990/android_kernel_samsung_sm8250](https://github.com/Official-Ayrton990/android_kernel_samsung_sm8250)@[5342ad778a...](https://github.com/Official-Ayrton990/android_kernel_samsung_sm8250/commit/5342ad778a67ae80dcbdabf5b6dbedebeda12383)
#### Monday 2022-02-28 00:23:22 by Peter Zijlstra

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
Signed-off-by: Adam W. Willis <return.of.octobot@gmail.com>

---
## [CitiesSkylinesMods/TMPE](https://github.com/CitiesSkylinesMods/TMPE)@[8ad7a2983d...](https://github.com/CitiesSkylinesMods/TMPE/commit/8ad7a2983d9e313858480015773933ca4c60a309)
#### Monday 2022-02-28 00:45:42 by aubergine10

gah, my brain while my friends are being bombed = mush

Note: FUCK ALL STATE FUNDED TERORIST GROUPS

---
## [oddtiming/push_swap](https://github.com/oddtiming/push_swap)@[8659551ce7...](https://github.com/oddtiming/push_swap/commit/8659551ce73ba715ede2f214eea5bce86032082a)
#### Monday 2022-02-28 01:37:11 by Ismael Yahyaoui Racine

I believe I know what the fuckup was

I had my optimization flag set to -O3, which I believe can cause some wonky behaviour when some code is misaligned. Don't quote me on that.
I'll set it to -O2 for now, and see what gives, and at the end if I still have time and energy for it, I'll do some optimization of my own to make -O3 work

Forgot to mention that one of the fixes that I did for my previous bug of misadressed function pointers
was to malloc my main container, which fixed some of the issues.

The logic now works, just need to properly update the biggest/smallest position iterators on push in a subfunction, and we're good to actually start the sorting process, lol

---
## [repinger/exynos9611_m21_kernel](https://github.com/repinger/exynos9611_m21_kernel)@[e8385c322d...](https://github.com/repinger/exynos9611_m21_kernel/commit/e8385c322dabf9ec2a628f050612a2ad1884ee21)
#### Monday 2022-02-28 02:37:50 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, tbsvc, and typec as they do not exist here]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [lsw3961/SonOfHermes](https://github.com/lsw3961/SonOfHermes)@[ee464813be...](https://github.com/lsw3961/SonOfHermes/commit/ee464813be2be59696fa3c80593b7ef5a7af2284)
#### Monday 2022-02-28 03:13:31 by Logan White

Testing for Framerate and prep for abilites

I did some testing for the framerate and I found that during a build my framerate is jumping from 60-200 frames so im not worrried during a build. But! during editor the framerate is around 30. Thats annoying as hell. whatever the reason I'm gunna have to figure it out. The game is smooth in build so its time to move on to adding new abilities. Tomorrow will be Adding the blast and the Ground Pound. I did some prep for it tonight by writing out all the methods I just need to populate them. I think I have a good number of abilities that enables the player to really put the hurt on their foes. Once these abilities are all squared away and I like the feel of them I think I am ready to make the first level.

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[f5d524707d...](https://github.com/Koi-3088/ForkBot.NET/commit/f5d524707dea50a418a65113c84184025252ea36)
#### Monday 2022-02-28 03:16:05 by Koi

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
## [GeorgeD88/Minesweeper-Solver](https://github.com/GeorgeD88/Minesweeper-Solver)@[b9140d9d15...](https://github.com/GeorgeD88/Minesweeper-Solver/commit/b9140d9d15e882731a878f00427738ef533a55fd)
#### Monday 2022-02-28 04:21:20 by George Doujaiji

Condense README intro to concise paragraph

At first I wrote a whole fucking life story about the timeline of the
project and shit, but then I started revising and condensing it and
ended up making a much better intro with well delivered info.

---
## [AkiraNoSushi/kernel_cherry_sdm439](https://github.com/AkiraNoSushi/kernel_cherry_sdm439)@[8a1d083a96...](https://github.com/AkiraNoSushi/kernel_cherry_sdm439/commit/8a1d083a969f194a1c69f2c6794ae3deb866715f)
#### Monday 2022-02-28 05:01:54 by Angelo G. Del Regno

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[f04b90b6e8...](https://github.com/odoo-dev/odoo/commit/f04b90b6e856bd8c1679cc728255f53fc788f8fd)
#### Monday 2022-02-28 07:56:38 by Julien Castiaux

[REF] core: HTTPocalypse (12) web ir.http & login

This commit is the 12th commit of a comprehensive refactor of our HTTP
framework. See odoo/odoo#78857 for complete historic, discussions and
rationnals.

The web module is twofold, on one side there are many controllers: /,
/web, /web/login, /web/database/selector, /web/dataset/call_kw, etc, on
the other side there is `session_info`: the method responsible to create
the web client's environ.

This module is kinda an exception as it is (with base) a server wide
module. In the case of the HTTP framework, it means that the controllers
of web are always accessible, i.e. going to / or /web/login will never
return a 404 Not Found even if the user is not connected to a database.

This is both a blessing and a curse. It is a blessing because the
controllers are always accessible it means that a new users can freely
access those routes. It is a curse because *any* user can access them,
even user who don't have a session yet thus who are not connected to a
database yet. From a developer standpoint, we have to put extra care to
correct serve users with and without a database. An example is the
/web/login route, the login/password pair is stored in a database,
without database it is impossible to validate a user login but users can
still access this route without db.

To solve this problem, there is the `ensure_db` function. This function
attempts to find a database using various sources (?db= query-string,
session db, mono db) and to save it on the user session. In case no db
is found, the user is redirected to the database selector. In a way,
this function grants a database to the user in a seamingly experience.
In a way, this function brings a welcome differentiation between
`auth='none'` with a database and `auth='none'` without a database. Such
differentiation only matters for the server wide modules as "regular"
module controllers are only accessible via the ir.http routing map, i.e.
it is not possible to declare a nodb controller outside of server wide
modules.

An important changement is the `session.authenticate` method, before it
was possible to call the method when the cursor was not yet initialized,
authenticate would open a cursor against the given database, setup a
registry and an environment and ultimately save everything on the
current request. Because the cursor is now greedily created, it is no
more possible to update the request environment when authenticating on
another database.

PR: odoo#78857
Task: 2571224

---
## [Oscar-Yam/CyberCodeOnline](https://github.com/Oscar-Yam/CyberCodeOnline)@[f9fd302bd7...](https://github.com/Oscar-Yam/CyberCodeOnline/commit/f9fd302bd7f43a7a693c1ae306071bea3ef64344)
#### Monday 2022-02-28 08:04:05 by Lance0-32

Update tips.txt

haha guys exp memories guys (they stopped existing)

also deixtoria thank your for the new facts about enemy XP NOW PLS STOP TALKING ABOUT IT BECAUSE I MADE THIS TIP AND IT'S CAUSING EMOTIONAL DAMAGE WHICH WAS VERY EFFECTIVE. (they didn't actually talk about it that much I'm overdramatizing lmao)

and some things that somehow slipped by people, myself included. WAIT I SHOULD'VE JUST DONE THE "some changes joke" ;-;

guess I'll do it for the additions, which are:
some changes

---
## [determined-ai/determined](https://github.com/determined-ai/determined)@[08888717a6...](https://github.com/determined-ai/determined/commit/08888717a6db21304115cd119ebb5d926d51c88e)
#### Monday 2022-02-28 08:23:23 by Bradley Laney

feat: unify task logs [DET-6062, DET-6063, DET-6064, DET-6065, DET-6066] (#3070)

This change adds persistent logs for all task types (well, all except poor old checkpoint GC). This means that logs are written to the logging back-end as configured in the master (PostgreSQL through master or Elastic) by Fluentbit and accessible through APIs in the master that translate reads to the back-end's language. To allow for this change, many other changes were required. A (probably) non-exhaustive list follows:
* Trial logs used to go to a `trial_logs` table or index. I tried to not tear the codebase asunder forever with trials and the others using different tables/queries/structs/etc everywhere. Existing tasks were marked has having `log_version == 0` and the old `trial_logs` table now serves logs those tasks (only trials). From now on, all tasks are written with `log_version == 1` and queries for their logs are routed to the `task_logs` table. The old trial logs table (now the `log_version == 0` table) is mothballed - it (mostly) shouldn't be touched again and the old logs should load from there fine forever while new features can be built on the new table. There were alternatives besides leaving trials and task logs separate forever that I shied away from; e.g., I considered a migration to update the trial logs table to schema of the task logs table, but since we access task logs by task_id, this would require rewriting the index on trial_id or adding one on task_id which is too expensive for a migration. This solution balances complexity, maintainability and migration cost.
* Because task logs went through the master, we were free to built features like readiness checks on top of them. Now that they don't, before logs leave the container a small helper script skims them, checks for the readiness logs and posts readiness to a new API. I considered alternatives here, too, like reading the logs back in on the master side, but that incurs a lot more overhead I felt this was more flexible anyway.
* The old events endpoint used to return logs, now it doesn't. This was because it (the eventManager that backed the endpoint) used to _store_ the logs, and now it doesn’t. In my opinion, the work to read the log stream and the old event stream and merge them is low value and annoying. Users should just prefer the new `/api/v1/tasks/:id/logs` endpoint for logs and rely on events to get the few task events that were relied on. Events will likely be supplanted by a task state watcher of some time so webui/cli can just watch for the readiness bit to flip.

---
## [ajwdmedia/groosathon-2](https://github.com/ajwdmedia/groosathon-2)@[afd6a196e9...](https://github.com/ajwdmedia/groosathon-2/commit/afd6a196e9641fa23e2fc7fd81d1ec20a405e93b)
#### Monday 2022-02-28 08:40:14 by hi-ashleyj

hi dark, lovely to see you
please stop your insanity, I'm worried you'll hit 400 tomorrow so i'm panicking a lot
Signed, the management, the management is me.

---
## [j-sandy/gate](https://github.com/j-sandy/gate)@[e2a108db75...](https://github.com/j-sandy/gate/commit/e2a108db759f1cdfe89c8ac6bd3fafc10c39ac8e)
#### Monday 2022-02-28 11:32:40 by Chris Phillips

fix(authn/oauth2): prevent oauth2 redirect loops (#1517)

During setup of spinnaker authentication with oauth2 a common hurdle is a redirect loop.

For example:

https://github.com/spinnaker/spinnaker/issues/5794
https://github.com/spinnaker/spinnaker/issues/1630

Also, many threads in Slack discuss these problems. In fact this appears to be a common
pitfall for the spring-security-oauth2-autoconfigure library in general. A light refresher
on the ouath2 flow in play here seems worthwhile. The user is redirected from `/login` in gate
to the external auth provider (google, github, etc.) and after successfully authenticating
they are redirected back to the gate `/login` endpoint but this time with a code parameter
that is to be used to request an access token.

This request can fail for a variety of reasons, and if it does, the underlying spring library
triggers a redirect to the `/error` endpoint. What causes the redirect loop for gate in particular
(and for other users of the library in a similar fashion) is that the WebSecurityConfigurerAdapter
in play is treating `/error` as an authenticated path and so instead of just returning with a 401,
it re-redirects to `/login` and the redirect loop continues.

My thought is that instead of a redirect loop, simply allowing the 401 to be returned will be a stronger
more helpful signal as to what is going on. Hopefully it will save future first-time installers headaches.

Spinnaker docs have included several troubleshooting hints and tips for how where you terminate SSL
affects configuration etc. Even after following all of these and lots of spelunking through spinnaker
github issues and combing over threads in slack, I found myself still experiencing a redirect loop even
though I had applied all the combined wisdom that was applicable to my setup.

As it turns out, I had a bad copy/paste of my client secret in my configuration. So the request
to turn the code from google into an access token from google was failing with a 401. After much
debugging and deep diving into the spring security code I found that had I turned on DEBUG in gate
for these classes in gate-local.yml:

```
logging:
  level:
    org.springframework.security.web.authentication.SimpleUrlAuthenticationFailureHandler: DEBUG
    org.springframework.security.oauth2.client.filter.OAuth2ClientAuthenticationProcessingFilter: DEBUG
```

Then I would have seen in the logs that a 401 response was returned from google and perhaps it would have
caused me to look closer at my botched client secret configuration. I think perhaps we don't want to require
that all operators of spinnaker become spring-security-oauth2 experts. So I'm proposing adding `/error` to
the list of paths in gate that aren't treated as authenticated. Thus short-circuiting the redirect loop and
bringing to light helpful troubleshooting info that was previously more or less swallowed.

---
## [Auralcat/my-dotfiles](https://github.com/Auralcat/my-dotfiles)@[7bb2f26ad1...](https://github.com/Auralcat/my-dotfiles/commit/7bb2f26ad10d0ca2bc2c8a337cf313a5a20605aa)
#### Monday 2022-02-28 12:34:24 by Miriam Retka

Create functions to copy code to GFM blocks

I feel this is one of the basic things that we take for granted in
Emacs, that it can do _anything_ with plain text, but we never get to
use or tweak it to our needs.

In my case, I'm writing an awful lot of code in comments to explain my
reasoning for comments in pull requests, and copying code from Emacs (or
worse, GitHub itself), writing the `s to make the fenced code blocks
there and pasting the code you want to share.

There is also the option to share the link to the code in the current
branch (in GitHub, of course), but I think that adds an extra layer of
friction that we don't need when explaining things: the user has to
click the link to see the code instead of reading it right there. The
upside of this approach is that you don't add a wall of code in the
middle of the text, so there are tradeoffs in both approaches.

Side note: writing fenced code blocks by hand is a pain when you are
using a non-English keyboard layout, and even then I think this could be
improved with at least a general code block shortcut. Currently GitHub
only offers the `suggestion` code block shortcut with M-g when writing
comments in pull requests, then you'd need to change the language name
in the code block to add other kinds of syntax there.

This is why I came up with these functions to add the text I'm copying
from modes derived from prog-mode (which correspond to programming
language modes) into a fenced code block depending on what I need to do:

- Just some example: copy it to a named GFM code block
- Highlight something important: copy it to a diff GFM code block
- Want to add a suggestion to the pull request from the comfort of my
  Emacs: copy it to a suggestion GFM code block
- GFM syntax highlighting is not supported where I'm pasting this code:
  use the plain Markdown code block.

Depending on how I use this, I think these functions could evolve into a
package! But let's try them out a bit first and see how to go from there.

---
## [saint-lascivious/munin-pihole-plugins](https://github.com/saint-lascivious/munin-pihole-plugins)@[397f1d13bd...](https://github.com/saint-lascivious/munin-pihole-plugins/commit/397f1d13bded9fc2220e004e49f56bda11fa06f4)
#### Monday 2022-02-28 12:56:50 by Hayden Pearce

munin-pihole-plugins: on second thought, lets not go to camelot. 'tis a silly place

Changes to be committed:
 - modified:   README.md
   update example --help text
 - modified:   script/munin-pihole-plugins
   bump script version to 1.6
   start aiming for a max 24 character height limit in help texts
   80 character wide is a hill i'll die on, fight me irl
   slightly more standard help text and behaviour
   simplify help and variable output
   explaining env var overrides in main help was a waste of space
   drop colour from help and variable output
   you were right, it was fucking distracting
   add a mini help function
   repeat invalid options and hint at -h,--help

---
## [a3-Prjkt/kernel_xiaomi_ginkgo_consistenX](https://github.com/a3-Prjkt/kernel_xiaomi_ginkgo_consistenX)@[3c23a8d4c6...](https://github.com/a3-Prjkt/kernel_xiaomi_ginkgo_consistenX/commit/3c23a8d4c60097354fe9dde538a39dd6554c17ba)
#### Monday 2022-02-28 13:12:22 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>

---
## [newstools/2022-the-irish-times](https://github.com/newstools/2022-the-irish-times)@[5007c19a0d...](https://github.com/newstools/2022-the-irish-times/commit/5007c19a0deecaf5da8db07d37a3b9d4cd66647a)
#### Monday 2022-02-28 15:03:37 by Billy Einkamerer

Created Text For URL [www.irishtimes.com/culture/books/i-hate-belfast-i-m-sick-of-the-troubles-all-i-feel-is-despair-soon-we-ll-all-be-butchered-1.4811090]

---
## [MrLepoischiche/some-assembly-required](https://github.com/MrLepoischiche/some-assembly-required)@[ef763db163...](https://github.com/MrLepoischiche/some-assembly-required/commit/ef763db163152c4bdae91589be7102ee972d87f5)
#### Monday 2022-02-28 15:16:12 by MrLepoischiche

Code optimization

Pushing everything because I modified shit this morning but can't remember where now

---
## [gmoshkin/dotfiles](https://github.com/gmoshkin/dotfiles)@[805313e07b...](https://github.com/gmoshkin/dotfiles/commit/805313e07bbbe12847cd4e8382f2b4d4a536c2f6)
#### Monday 2022-02-28 18:07:52 by gmoshkin

wtf is this garbage ass autoconf shit??? bram, you're an idiot

---
## [kdave/btrfs-devel](https://github.com/kdave/btrfs-devel)@[1b04015c25...](https://github.com/kdave/btrfs-devel/commit/1b04015c252f5ca82c27ef98f95ce1a74abfa1d0)
#### Monday 2022-02-28 20:58:02 by Josef Bacik

btrfs: do not WARN_ON() if we have PageError set

Whenever we do any extent buffer operations we call
assert_eb_page_uptodate() to complain loudly if we're operating on an
non-uptodate page.  Our overnight tests caught this warning earlier this
week

  WARNING: CPU: 1 PID: 553508 at fs/btrfs/extent_io.c:6849 assert_eb_page_uptodate+0x3f/0x50
  CPU: 1 PID: 553508 Comm: kworker/u4:13 Tainted: G        W         5.17.0-rc3+ #564
  Hardware name: QEMU Standard PC (Q35 + ICH9, 2009), BIOS 1.13.0-2.fc32 04/01/2014
  Workqueue: btrfs-cache btrfs_work_helper
  RIP: 0010:assert_eb_page_uptodate+0x3f/0x50
  RSP: 0018:ffffa961440a7c68 EFLAGS: 00010246
  RAX: 0017ffffc0002112 RBX: ffffe6e74453f9c0 RCX: 0000000000001000
  RDX: ffffe6e74467c887 RSI: ffffe6e74453f9c0 RDI: ffff8d4c5efc2fc0
  RBP: 0000000000000d56 R08: ffff8d4d4a224000 R09: 0000000000000000
  R10: 00015817fa9d1ef0 R11: 000000000000000c R12: 00000000000007b1
  R13: ffff8d4c5efc2fc0 R14: 0000000001500000 R15: 0000000001cb1000
  FS:  0000000000000000(0000) GS:ffff8d4dbbd00000(0000) knlGS:0000000000000000
  CS:  0010 DS: 0000 ES: 0000 CR0: 0000000080050033
  CR2: 00007ff31d3448d8 CR3: 0000000118be8004 CR4: 0000000000370ee0
  Call Trace:

   extent_buffer_test_bit+0x3f/0x70
   free_space_test_bit+0xa6/0xc0
   load_free_space_tree+0x1f6/0x470
   caching_thread+0x454/0x630
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? rcu_read_lock_sched_held+0x12/0x60
   ? lock_release+0x1f0/0x2d0
   btrfs_work_helper+0xf2/0x3e0
   ? lock_release+0x1f0/0x2d0
   ? finish_task_switch.isra.0+0xf9/0x3a0
   process_one_work+0x26d/0x580
   ? process_one_work+0x580/0x580
   worker_thread+0x55/0x3b0
   ? process_one_work+0x580/0x580
   kthread+0xf0/0x120
   ? kthread_complete_and_exit+0x20/0x20
   ret_from_fork+0x1f/0x30

This was partially fixed by c2e39305299f01 ("btrfs: clear extent buffer
uptodate when we fail to write it"), however all that fix did was keep
us from finding extent buffers after a failed writeout.  It didn't keep
us from continuing to use a buffer that we already had found.

In this case we're searching the commit root to cache the block group,
so we can start committing the transaction and switch the commit root
and then start writing.  After the switch we can look up an extent
buffer that hasn't been written yet and start processing that block
group.  Then we fail to write that block out and clear Uptodate on the
page, and then we start spewing these errors.

Normally we're protected by the tree lock to a certain degree here.  If
we read a block we have that block read locked, and we block the writer
from locking the block before we submit it for the write.  However this
isn't necessarily fool proof because the read could happen before we do
the submit_bio and after we locked and unlocked the extent buffer.

Also in this particular case we have path->skip_locking set, so that
won't save us here.  We'll simply get a block that was valid when we
read it, but became invalid while we were using it.

What we really want is to catch the case where we've "read" a block but
it's not marked Uptodate.  On read we ClearPageError(), so if we're
!Uptodate and !Error we know we didn't do the right thing for reading
the page.

Fix this by checking !Uptodate && !Error, this way we will not complain
if our buffer gets invalidated while we're using it, and we'll maintain
the spirit of the check which is to make sure we have a fully in-cache
block while we're messing with it.

CC: stable@vger.kernel.org # 5.4+
Signed-off-by: Josef Bacik <josef@toxicpanda.com>
Signed-off-by: David Sterba <dsterba@suse.com>

---
## [VenomPr1meAC/Prime-Anticheat](https://github.com/VenomPr1meAC/Prime-Anticheat)@[60083729a8...](https://github.com/VenomPr1meAC/Prime-Anticheat/commit/60083729a8ae0010a7599fe936b9cf7552303917)
#### Monday 2022-02-28 21:27:58 by VenomPr1meAC

PRIME ANTICHEAT

PRIME ANTICHEAT

Anti Eulen
Anti God Mode
Anti Ragdoll
Anti Invisible
Anti Spectate
Anti Speed Hacks
Anti Thermal Vision
Anti Night Vision
Anti Menyoo
Anti Give Armor
Anti Super Jump
Anti Infinite Stamina
Anti Vehicle Speed
Anti Mod Menu Crash
Anti Armour
Anti Explosion Spam Count
Anti Particles Spam Count
Anti Random String Resource
Anti VPN
Anti Blacklisted Tasks
Anti Blacklisted Anims
Anti Blacklist Plate
Anti Blacklist Key
Anti Blacklist Name
Anti Blacklisted Words
Anti Give Weapon Event
Anti Aimbot
Anti Taze
Anti Aim Assist
Anti Explosive Bullets
Anti Explosion Damage
Anti Disable Vehicle Weapons
Anti Weapon Flag
Anti Weapon Damage Change
Anti Spawn Objects
Anti Spawn Vehicles
Anti Spawn Peds
Anti FakeMessage
Anti Injection
Anti Max Economy
Max Money
Max Money Bank
Whitelisted Country
Protect Police Event
Protect Ambulance Event
Protect Mechanic Event
On Screen Menu Detection
Screenshot System

Copyright © 2022 Prime Anticheat - All Rights Reserved

BUY ON DISCORD
https://discord.gg/pr1me-ac

---
## [BlackAndWhiteCarnage/EUPHORIA](https://github.com/BlackAndWhiteCarnage/EUPHORIA)@[dea825cd61...](https://github.com/BlackAndWhiteCarnage/EUPHORIA/commit/dea825cd611633ceaa1a4038048a4eba1b299119)
#### Monday 2022-02-28 21:54:14 by Krzysztof Repsch

TypeScript again

I just saw that my old code is ugly as fuck if it comes to handeling
extras. ExtrasProvider and ExtrasProvider are poorly typed right now
so I will come back to it later!

---
## [piushbhandari/Invoice-tracker](https://github.com/piushbhandari/Invoice-tracker)@[4c9f2ea5b4...](https://github.com/piushbhandari/Invoice-tracker/commit/4c9f2ea5b46844ad721e72b79df0fb4a6ccf0309)
#### Monday 2022-02-28 22:15:10 by piush bhandari

bloody hell finished the list item stuff. took way longer than i wanted to but i suspect it would have been a lot easier if i had done this with react from the get go instead of migrating it or whatever the fuck

---
## [newstools/2022-naija-news-agency](https://github.com/newstools/2022-naija-news-agency)@[112ab562ff...](https://github.com/newstools/2022-naija-news-agency/commit/112ab562ff1bfc7c82fb02b8b5ee5b2923525a9c)
#### Monday 2022-02-28 23:45:54 by Billy Einkamerer

Created Text For URL [www.naijanewsagency.com/the-go-fuck-yourself-ukrainian-soldiers-on-snake-island-are-alive-navy-says/]

---

