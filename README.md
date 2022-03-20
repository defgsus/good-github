## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-03-19](docs/good-messages/2022/2022-03-19.md)


1,548,617 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,548,617 were push events containing 2,329,834 commit messages that amount to 126,709,446 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 27 messages:


## [chaldeaprjkt/kernel_xiaomi_vayu](https://github.com/chaldeaprjkt/kernel_xiaomi_vayu)@[ab6f20b0b0...](https://github.com/chaldeaprjkt/kernel_xiaomi_vayu/commit/ab6f20b0b0376a2a38f02e3cd1aaa8cbae0d55e5)
#### Saturday 2022-03-19 00:04:48 by Peter Zijlstra

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
## [zeobuilder10/NetflixPage](https://github.com/zeobuilder10/NetflixPage)@[6aaccaae45...](https://github.com/zeobuilder10/NetflixPage/commit/6aaccaae451983726c597f24cccfd7ad247226a5)
#### Saturday 2022-03-19 00:18:09 by zeobuilder10

I forsake thee O sun god, for I have seen what thee make of our fragile lives. I pity thyne followers doomed to praise a murderer that leeds them astray as would the black lamb would. Woe to the vanquished, I suppose you will outlive my memory, yet I hope you will not forget me, Yet I can only hope. Farewell sun god, may you live a short life.

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[770ef81a1f...](https://github.com/GoblinBackwards/tgstation/commit/770ef81a1fb271572d711e7a05dbce62564ca3b0)
#### Saturday 2022-03-19 00:21:32 by John Willard

makes podpeople call parent (#65362)


About The Pull Request

kinda fucked up that it doesnt.
Also while checking this PR I noticed other species also don't, kinda screwed up world we live in...
Why It's Good For The Game

Parent's spec_life is what checks if you have nobreath, and in which case it will remove all your oxygen damage and, if in crit, give you brute damage instead. Not having this makes you basically not take damage while in crit, which I think shouldn't be the case.
Changelog

cl
fix: Podpeople now take self-respiration into account when taking damage from critical condition, like most other species.
/cl

---
## [Tastyfish/-tg-station](https://github.com/Tastyfish/-tg-station)@[745426eff2...](https://github.com/Tastyfish/-tg-station/commit/745426eff227ff556105147a4802540617decd7b)
#### Saturday 2022-03-19 00:23:00 by LemonInTheDark

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
## [Mechanelize/tgstation](https://github.com/Mechanelize/tgstation)@[906fb0682b...](https://github.com/Mechanelize/tgstation/commit/906fb0682bab6a0975b45036001c54f021f58ae7)
#### Saturday 2022-03-19 00:51:08 by necromanceranne

Ballistic to Energy: Autorifles for Thermal Pistols; Adds .38 Crate to Cargo (#64280)

About The Pull Request
The design doc behind this PR, which is only mildy been deviated from on some of the end particulars. Cobby-Approved! Maintainer Discussed!
https://hackmd.io/@6DbtsAKCTtW_9MByKFjZqg/r1xYKCNOt

Cargo Changes
Cargo has had all WT-550's removed and replaced with Thermal Pistols.
Cargo can now order Thermal Pistols, a kind of energy/ballistic hybrid weapon shooting chunks of altered nanites into people. We couldn't use them in people, so maybe we'll use them as bullets! Magma/Ice bullets, to be exact.
You can, after paying a whopping 4K on a goodie pack (you have to pay from your own personal account) buy a .38 revolver. This is mostly to help some poor detective who lost their revolve in what I'm sure will be an inevitable scramble for ballistics. If even the 4K pricetag isn't enough, at least it requires detective access to open the pack...I hope.
Some of the crates that contained autorifle related items have been changed/removed.

unknown (2)

securarevolver 4 0

Science Changes
Ballistic Weaponry node no longer exists, and has been replaced with Exotic Ammo as both the pre-requisite to other nodes, as well as being able to be researched as soon as the Weaponry node is unlocked and not Advanced Weaponry.

Thermal Pistols
-Fairly average bullet statistics; 10 AP but shooting into Energy armor. 20 damage (Brute for cryo, Burn for inferno). Decent wounding potential, but individually much lower ammo counts than lasers.
-Bought in twinned pairs in a two gun holster (just for normal sized energy guns). They're normal sized.
-Each gun has 8 shots (thereabouts). 16 between two.
-Cryo pistols do a knockdown and extra damage against extremely hot targets. Inferno pistols do an explosion cantered on the target against extremely cold targets.
-The guns are EMP-proof.

Why It's Good For The Game
The current gameplay loop of crew combatants is them relying on backup and retreating as necessary to reload their weapons during fights. The ability to repeatedly harry opponents in the field reloads is something that should be moved away from for crew equipment, as it emphasizes lone wolf tactics and one-man army problems, with boxes full of spare ammo usually allowing any single combatant to outlast multiple foes. In addition, ballistics often are not subject to the same (interesting) limitations of energy weapons, so they're typically a no-brainer choice. We shouldn't have such an easy choice be readily available like that.

The thermal pistols present a more challenging weapon to use as a solo combatant but become far more versatile and potent when paired with a decent buddy and basic level co-ordination. They're not a straightforward choice for every situation, but instead are a weapon employed given the right circumstances for them to shine.

In addition to the gameplay issues that ballistics pose, we're in a goddamn spacegame. Unless the ballistics are noticeably weird (they're not), we should expect that our more advanced research station has some pretty odd guns of the energy variety.

Changelog
🆑 Necromanceranne, quin
add: Adds the Inferno and Cryo Pistols. A hybrid energy/ballistic weapon, to cargo. It can be purchased in either a goodies pack or a normal crate order.
add: Thermal Pistols do more damage and a special based on temperature of the target hit.
add: Inferno pistols cause an explosion when they hit a severely cold target.
add: Cryo pistols cause a knockdown and extra damage if they hit a severely hot target.
add: There is a special nanite pistol, which is admin spawned. Don't tell anyone about the forbidden ballistic energy gun.
add: You can order a .38 revolver as a goodie pack. It is expensive.
del: Removes WT-550's from cargo and related content from the techweb/protolathes.
balance: Exotic Ammo is now much earlier in the tech web to take the place of Ballistic Weaponry.
/🆑

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a182a6e67e...](https://github.com/treckstar/yolo-octo-hipster/commit/a182a6e67e4d3e89ce8096583e6c1a54799903ff)
#### Saturday 2022-03-19 01:00:02 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [ozzono/scripts](https://github.com/ozzono/scripts)@[e405b53fc7...](https://github.com/ozzono/scripts/commit/e405b53fc7294d3d26d7a99c11f54513b9068a30)
#### Saturday 2022-03-19 02:22:26 by Hugo Virgílio

Fortune Commit: "I have a friend who just got back from the Soviet Union, and told me the people
there are hungry for information about the West.  He was asked about many
things, but I will give you two examples that are very revealing about life in
the Soviet Union.  The first question he was asked was if we had exploding
television sets.  You see, they have a problem with the picture tubes on color
television sets, and many are exploding.  They assumed we must be having
problems with them too.  The other question he was asked often was why the
CIA had killed Samantha Smith, the little girl who visited the Soviet Union a
few years ago; their propaganda is very effective.
-- Victor Belenko, MiG-25 fighter pilot who defected in 1976
   "Defense Electronics", Vol 20, No. 6, pg. 100

---
## [BakaKaito/Mergebot.NET](https://github.com/BakaKaito/Mergebot.NET)@[3304ea21ae...](https://github.com/BakaKaito/Mergebot.NET/commit/3304ea21ae15576306125e0278dab65803258425)
#### Saturday 2022-03-19 02:35:18 by Koi

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
## [srgrusso/android_kernel_oneplus_sdm845](https://github.com/srgrusso/android_kernel_oneplus_sdm845)@[1f51fd987d...](https://github.com/srgrusso/android_kernel_oneplus_sdm845/commit/1f51fd987d9b056d7a287df058002bf137765ee1)
#### Saturday 2022-03-19 03:19:49 by alk3pInjection

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
## [pixlsus/website](https://github.com/pixlsus/website)@[a7a4735566...](https://github.com/pixlsus/website/commit/a7a473556664b55ccfd14fe58d4509105ccb4bb4)
#### Saturday 2022-03-19 03:30:15 by Pat David

To annoy paperdigits - bundle your commits

Yeah yeah.  Sorry about this.

 * added a temp <hr> to give some space between article posts.
 * added unsafe to the goldmark renderer so we can include html
 * in posts.
 * added a favicon.ico and reference it in the layout.
 * added a couple of svg files, bitcam and eye.

---
## [haskell/alex](https://github.com/haskell/alex)@[32ed9ed17b...](https://github.com/haskell/alex/commit/32ed9ed17b9f25f1b533b53b250a5fe5ee6d1abe)
#### Saturday 2022-03-19 03:34:06 by askeblad

correct spelling of `DFS.GForrest` (#214)

> > would it break code to change to `GForest` ?
> 
> I think it wouldn't, since `alex` is an executable only and does not export an API. 
> But also, there are no strong reasons to correct the misspelling, are there? 
> (These lines mostly haven't been touched in 19 years, so we should have some respect ... :-D)

noting the computer science studies component of graph theory, the change is indicated

Skogen och vår identitet
by Erkki Lähde
Finlands natur - 1984

Prof. Lähde recounts when as a young graduate out of forestry studies, he had the occasion to visit a village in the Finnish countryside. He noticed in the area a group of trees which to his view was overdue to be cut. But enquiring upon the local villagers of that stand of trees, the reply was that there was an old woman from the village who had liked to walk among that grove. Thus the trees were saved out of piety.

>  (These lines mostly haven't been touched in 19 years, so we should have some respect ... :-D)

piety isn't indicated here

---
## [RajaKunalPandit1/CodeForces_Questions](https://github.com/RajaKunalPandit1/CodeForces_Questions)@[35cd19aa85...](https://github.com/RajaKunalPandit1/CodeForces_Questions/commit/35cd19aa8522e66a21a60cdaa507cb47df0c7c07)
#### Saturday 2022-03-19 04:55:41 by Raja Kunal Pandit

Create 703A - Mishka and Game.cpp

Output Status: 

By Rajakunalpandit, contest: Codeforces Round #365 (Div. 2), problem: (A) Mishka and Game, Accepted

Mishka is a little polar bear. As known, little bears loves spending their free time playing dice for chocolates. Once in a wonderful sunny morning, walking around blocks of ice, Mishka met her friend Chris, and they started playing the game.

Rules of the game are very simple: at first number of rounds n is defined. In every round each of the players throws a cubical dice with distinct numbers from 1 to 6 written on its faces. Player, whose value after throwing the dice is greater, wins the round. In case if player dice values are equal, no one of them is a winner.

In average, player, who won most of the rounds, is the winner of the game. In case if two players won the same number of rounds, the result of the game is draw.

Mishka is still very little and can't count wins and losses, so she asked you to watch their game and determine its result. Please help her!

Input
The first line of the input contains single integer n n (1 ≤ n ≤ 100) — the number of game rounds.

The next n lines contains rounds description. i-th of them contains pair of integers mi and ci (1 ≤ mi,  ci ≤ 6) — values on dice upper face after Mishka's and Chris' throws in i-th round respectively.

Output
If Mishka is the winner of the game, print "Mishka" (without quotes) in the only line.

If Chris is the winner of the game, print "Chris" (without quotes) in the only line.

If the result of the game is draw, print "Friendship is magic!^^" (without quotes) in the only line.

Examples
inputCopy
3
3 5
2 1
4 2
outputCopy
Mishka
inputCopy
2
6 1
1 6
outputCopy
Friendship is magic!^^
inputCopy
3
1 5
3 3
2 2
outputCopy
Chris
Note
In the first sample case Mishka loses the first round, but wins second and third rounds and thus she is the winner of the game.

In the second sample case Mishka wins the first round, Chris wins the second round, and the game ends with draw with score 1:1.

In the third sample case Chris wins the first round, but there is no winner of the next two rounds. The winner of the game is Chris.

---
## [ashleyvsch/cs273A_project](https://github.com/ashleyvsch/cs273A_project)@[40f1decd49...](https://github.com/ashleyvsch/cs273A_project/commit/40f1decd49ff67bd15e74f01caf0ecf2841c1849)
#### Saturday 2022-03-19 05:30:42 by Erik

TF Plots Fixed

God funny how one line fucks everything up and makes every thing work. Short explanation: You need to have %matplotlib written into a jupyter notebook to have interactive figures when using a jupyter notebook but this line in vscode won't show any plots and just fuck them up when saved. But I have fixed this now and for future reference.

---
## [a3-Prjkt/kernel_xiaomi_ginkgo_consistenX](https://github.com/a3-Prjkt/kernel_xiaomi_ginkgo_consistenX)@[3c23a8d4c6...](https://github.com/a3-Prjkt/kernel_xiaomi_ginkgo_consistenX/commit/3c23a8d4c60097354fe9dde538a39dd6554c17ba)
#### Saturday 2022-03-19 06:16:25 by George Spelvin

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
## [bellomia/MOTTlab](https://github.com/bellomia/MOTTlab)@[da21cef8bd...](https://github.com/bellomia/MOTTlab/commit/da21cef8bd968e5eae3d8398bedd08adb139d286)
#### Saturday 2022-03-19 06:56:34 by Gabriele Bellomia

Add Economou's 2d toy-model

Just a rectangular DOS, for which G(z) can be trivially evaluated on paper.

- Has key features of a generic 2d lattice, namely sharp band edges at
  ω = ± D, associated to logarithmic divergences in the real part of G(z)

- Does *not* have van Hove singularities in Im[G(z)] for it is not really
  associated to a tight binding model, which has weird consequences:

  1. the lack of an explicit model leaves the hopping-bandwidth relation
     undetermined, so that the hybridization function is arbitrary.

  2. I have played a lot around this concept and... it seems actually
     tricky. If I set t = D/2 I get something very similar to the Bethe
     solution at infinite dimensions, meaning a very very similar Z(U)
     profile and a quite stunning visual recall; the rectangle "melts"
     immediately in what is basically a smooth semicircle-ish DOS, that
     then goes the usual Bethe-Hubbard MIT.

  3. If I set instead t = D/4, mimicking the square lattice, I get indeed
     a very convincing visual resemblance in the spectral evolution, but
     not that much quantitative match in Z(U). Much worse than with Bethe!

Well, I got caught with curiosity and did an extensive exploration, with
all the standard metallic lattices, some firm points:

a. for sure the t(D) relation fixes the critical U of the transition,
   which is kind of reasonable as the hybridization function goes with
   t^2 and not D^2. So the scale of the problem should come from (U/t)^2
   if we compare the role of the hybridization to the bath vs the local
   interaction, which perturbatively amounts to a U^2 factor.

b. but it really seems that tinkering with the actual quantitative t(D)
   not only moves the transition, but also significantly changes the
   curvature of the Z profile... and even more affects the *qualitative*
   behavior of the spectral function, which still keeps me amazed.

All of this needs to be investigated much more deeply, and maybe this
arbitrary toy model could allow  forsome fast experimentation and help
shedding light on the issue. For sure we need to revert to the U/t
scaling for all the plotting... maybe it could make sense to finally
promote hybr() to the +phys public namespace and make it return also
the hopping... it would certainly help with all the plotting, avoiding
countless redundant switch/case constructs.

————————————————————————————————————————————————————————————————————————

NB. The BIG QUESTION† is: if I fix a lattice and a *hopping* value, does
    the transition modify its details if I change the form of t(D)?

    Yes -> This toy model can mimic different lattices, some better than
           others, and could serve as a flexible, fast... well, toy 🤭

    No  -> This could be more than a toy model, actually approximating
           well some model far more heavy to simulate (in the spirit of
           what did Jafari in its 2009 paper with the honeycomb...).
           But then it is crucial to understand WHICH model is better
           approximated: not so obvious that is the square lattice, for
           what I have seen in these preliminary tests (actually the
           nearest model could be the Bethe lattice, which would mean
           that this model loses, well, all of its utility).

    Y/N -> Whatever the scenario, in the same spirit, it could be quite
           useful to implement the *finite* coordination Bethe lattice,
           which should approximate better the lattices with comparable
           coordination, I guess... But this would require some work on
           the interface of phys.gloc and even upstream on dmft_loop(),
           for we need somehow to pass the coordination down from the
           main to where we need it, and it just cannot be a global.

 †) partially answered (it would be yes) by points (2,3) above...

---
## [clamor-s/u-boot](https://github.com/clamor-s/u-boot)@[84b16d3865...](https://github.com/clamor-s/u-boot/commit/84b16d3865db3cc42b7ff24b597f78892c9e4fea)
#### Saturday 2022-03-19 08:30:52 by Marcel Ziswiler

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
## [wongweilok/dwm](https://github.com/wongweilok/dwm)@[67d76bdc68...](https://github.com/wongweilok/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Saturday 2022-03-19 08:42:43 by Chris Down

Do not allow focus to drift from fullscreen client via focusstack()

It generally doesn't make much sense to allow focusstack() to navigate
away from the selected fullscreen client, as you can't even see which
client you're selecting behind it.

I have had this up for a while on the wiki as a separate patch[0], but
it seems reasonable to avoid this behaviour in dwm mainline, since I'm
struggling to think of any reason to navigate away from a fullscreen
client other than a mistake.

0: https://dwm.suckless.org/patches/alwaysfullscreen/

---
## [Kaz205/renoir](https://github.com/Kaz205/renoir)@[d6648b55ed...](https://github.com/Kaz205/renoir/commit/d6648b55ed39ca369e3eed236bb6027dda58967b)
#### Saturday 2022-03-19 09:57:36 by Vasily Averin

mm, oom: pagefault_out_of_memory: don't force global OOM for dying tasks

commit 0b28179a6138a5edd9d82ad2687c05b3773c387b upstream.

Patch series "memcg: prohibit unconditional exceeding the limit of dying tasks", v3.

Memory cgroup charging allows killed or exiting tasks to exceed the hard
limit.  It can be misused and allowed to trigger global OOM from inside
a memcg-limited container.  On the other hand if memcg fails allocation,
called from inside #PF handler it triggers global OOM from inside
pagefault_out_of_memory().

To prevent these problems this patchset:
 (a) removes execution of out_of_memory() from
     pagefault_out_of_memory(), becasue nobody can explain why it is
     necessary.
 (b) allow memcg to fail allocation of dying/killed tasks.

This patch (of 3):

Any allocation failure during the #PF path will return with VM_FAULT_OOM
which in turn results in pagefault_out_of_memory which in turn executes
out_out_memory() and can kill a random task.

An allocation might fail when the current task is the oom victim and
there are no memory reserves left.  The OOM killer is already handled at
the page allocator level for the global OOM and at the charging level
for the memcg one.  Both have much more information about the scope of
allocation/charge request.  This means that either the OOM killer has
been invoked properly and didn't lead to the allocation success or it
has been skipped because it couldn't have been invoked.  In both cases
triggering it from here is pointless and even harmful.

It makes much more sense to let the killed task die rather than to wake
up an eternally hungry oom-killer and send him to choose a fatter victim
for breakfast.

Link: https://lkml.kernel.org/r/0828a149-786e-7c06-b70a-52d086818ea3@virtuozzo.com
Signed-off-by: Vasily Averin <vvs@virtuozzo.com>
Suggested-by: Michal Hocko <mhocko@suse.com>
Acked-by: Michal Hocko <mhocko@suse.com>
Cc: Johannes Weiner <hannes@cmpxchg.org>
Cc: Mel Gorman <mgorman@techsingularity.net>
Cc: Roman Gushchin <guro@fb.com>
Cc: Shakeel Butt <shakeelb@google.com>
Cc: Tetsuo Handa <penguin-kernel@i-love.sakura.ne.jp>
Cc: Uladzislau Rezki <urezki@gmail.com>
Cc: Vladimir Davydov <vdavydov.dev@gmail.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [whtcorpsinc/EinsteinDB](https://github.com/whtcorpsinc/EinsteinDB)@[8dacf47b5a...](https://github.com/whtcorpsinc/EinsteinDB/commit/8dacf47b5a4a704e430746942aad0031a82712bf)
#### Saturday 2022-03-19 11:10:56 by Karl Whitford

probably make all hashmaps implement consuuuu

// clone https://www.github.com/Mozilla/Mentat
//inside the program navigate to the folder 'db'
//open src/db.rs

/*
Datomic used to expose :db.fn/retractEntity and
:db.fn/retractAttribute, but there latest Cloud offering has only
:db/retractEntity. Since that's what I am interested in using, that's
all I've implemented.

This transformation doesn't follow the existing pattern of inserting
into the temp.*_searches table. It instead populates
temp.search_results directly from datoms, and in so doing it makes
some assumptions about how the searches tables will be accessed.

It might be even more efficient to have an entirely new temporary
table just for these retractions. One advantage with the current
scheme is that indexing restrictions placed on the search results
table will apply to the datoms retracted by :db/retractEntity as well.

There are a few remaining items TODO.

TODO: ensure that we mark the schema as potentially modified when we
:db/retractEntity. It's not clear to me how to do this efficiently.

TODO: ensure that transaction watchers get the correct transacted
datom stream. I didn't try to address this yet because it appears to
me that the existing watcher implementation isn't quite correct: it
tells watchers about datoms that are potentially to be transacted but
not about datoms that actually are transacted. This, of course,
matters when watching :db/retractEntity entities being transacted.
*/

use std::collections::HashSet;
use std::collections::HashMap;
use eavt;
use event;
use mentat_db as db;
// use mentat_store as store;
// use mentat_query as qm;

/* define the interface that datoms need to implement */
trait EntityFn { fn entity(&self) -> eavt::Entity ; }  //: EntityFn { }
impl EntityFn for eavt::Datom { fn entity(&self) -> eavt::Entity { self.entity() }}  //: DataPoint {} }

/* Given two input streams of datoms (the old and the new), figure out the set difference */
fn diff<'a, T>(datoms_new: T, datoms_old: HashSet<eavt::Datom>) -> Vec<eavt::Datom> where T : Iterator<Item=&'a eavt::Datom> + ExactSizeIterator {

    let mut ret : Vec<eavt::Datom> = vec![];

    // keep a set of the indices of elements we've seen so far. This is imprecise but should be good enough.  Really, I'd just like to not have a hset in Rust. It's silly!
    let mut seen : HashSet<usize> = HashSet::with_capacity(datoms_old.len());

    /* loop over each value in the new dataset. Compare it against each element in the old list, saving nonduplicates into a vector we build up before returning it. */
    for d in datoms_new {

        /* skip over any seen values */
        if seen.contains(&(d.position())) { continue }

        /* if we haven't seen it yet, check against all previous values */
        for old in &datoms_old {

            /* if this new value matches an old value we've already seen, no need to include it again */
            if d == *old { break }

            /* otherwise, continue searching */

        } // next old value in list of old values considered so far

        /* since we made it through all the matches without finding a match, add this value to our output array and mark it as such with an index */
        ret.push(*d);  // TODO actually clone datom rather than move vals around? don't really want `clone` types everywhere...? Or maybe I want abstractions around cloning... Ultimately I want something that isn't generic over types... Like an assignment operator instead? Or maybe `consume` -- take ownership of everything? That sounds nice... But there are SO MANY rocks that are caught in cloning paths that call mea culpa here... Plus the 'make everything generic constraine types' thing seems like its short-term thinking at best -- when specific problems arise, carve out what you need and leave the rest wherver you find them (I suppose!)... No dicts and hashes are currently a major pain point!! Grrrr!! ... TODO probably make all hashmaps implement consuuuu

---
## [p-neves/subsurface.github.io](https://github.com/p-neves/subsurface.github.io)@[ad4b82193b...](https://github.com/p-neves/subsurface.github.io/commit/ad4b82193be920f3b90c6a31a757368dcc202c54)
#### Saturday 2022-03-19 11:52:50 by Dirk Hohndel

small updates to deal with horizontal lines

I wonder if the magic that creates them isn't more trouble than it's worth.
Maybe it would be better to make them explicit? This seems hacky...

This commit also has a couple of tiny edits to the things Jason brought
over from the old FAQ.

Signed-off-by: Dirk Hohndel <dirk@hohndel.org>

---
## [beetrandahiya/project-G](https://github.com/beetrandahiya/project-G)@[f05dba45a7...](https://github.com/beetrandahiya/project-G/commit/f05dba45a76eb60d6e2aa05392f43104e33f2b14)
#### Saturday 2022-03-19 12:16:50 by Prakrisht Dahiya

1 million points dataset test

rendered and painted 1 million point dataset in 81 fuckin milliseconds, bitchesssssssssssssssssssssssssssssssss

---
## [interestingusernam3/tgstation](https://github.com/interestingusernam3/tgstation)@[759d24ab14...](https://github.com/interestingusernam3/tgstation/commit/759d24ab14af0ab22ae9642e9190c3db91e16516)
#### Saturday 2022-03-19 16:00:13 by san7890

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
## [interestingusernam3/tgstation](https://github.com/interestingusernam3/tgstation)@[884c1eeb62...](https://github.com/interestingusernam3/tgstation/commit/884c1eeb62e1c970b2b6edc425f36c924b9f48ee)
#### Saturday 2022-03-19 16:00:13 by 小月猫

fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

---
## [kangalioo/poise](https://github.com/kangalioo/poise)@[f5aff9a625...](https://github.com/kangalioo/poise/commit/f5aff9a62558966ad8b91036371f1d228f474ca6)
#### Saturday 2022-03-19 16:15:33 by kangalioo

Don't apply reuse_response for slash

Why? It all begins with modals. When you send a modal as the initial response (it has to be), and the command is marked reuse_response, poise was trying to edit the modal as if it were a message and crash. This didin't ever fail before because pre-modals, all initial interaction response possibilities were editable into text. Anyways, there's a bunch of ugly solutions, like keeping track in ApplicationContext not only whether a response was sent, but also whether it was a modal, in which case the reuse_response editing would be directed at a followup response instead, so you'd also keep track of the followup response message ID and it's all a big mess. And then I remembered why reuse_response exists in the first place and it's for prefix commands, for edit tracking. And using reuse_response for slash doesn't even really make sense, like, think about it, you're sending multiple messages in the code (`ctx.send(1); ctx.send(2);`) but it all goes in a single message. Makes no sense. If people wanna edit their initial response, they should do _that_: `ctx.send(1).edit(2);`. And this now also works absolutely fine with modals. You can do `Modal::execute(ctx); ctx.send(1).edit(2);` and the edit will not try to edit the modal, but it will edit the send(1) which is already a followup message because Modal::execute set the has_sent_initial_response atomic flag, and everything was fine. I hope. We will see

---
## [postgresql-cfbot/postgresql](https://github.com/postgresql-cfbot/postgresql)@[ec62cb0aac...](https://github.com/postgresql-cfbot/postgresql/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Saturday 2022-03-19 17:04:18 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [petre-symfony/easy-admin-symfonycasts](https://github.com/petre-symfony/easy-admin-symfonycasts)@[5662bd1781...](https://github.com/petre-symfony/easy-admin-symfonycasts/commit/5662bd17819f35bb45c56722f53e03e19eb97741)
#### Saturday 2022-03-19 20:05:24 by petrero

28.3. Security Voter & Entity Permissions

  Adding Permissions Logic to the Query
  - So there's just one tiny problem with our setup. Imagine that we have a lot of users - like thousands - which is pretty realistic. And our user is ID 500. In that case, you would actually see many pages of results here. And our user might be on page 200. So you'd see no results on page one... or two... or three... until finally, on page 200, you'd find our one result. So it can get a little weird if you have many items in an admin section, and many of them are hidden.

  To fix this, we can modify the query that's made for the index page to only return the users we want. This is totally optional, but can make for a better user experience.

  So far, we've been letting EasyAdmin query for every user or every question. But we do have control over that query. Open up UserCrudController and, anywhere, I'll go near the top, override a method from the base controller called createIndexQueryBuilder()

  Here's how this works: the parent method starts the query builder for us. And it already takes into account things like the Search on top or "filters", which we'll talk about in a few minutes.

  Instead of returning this query builder, set it to $queryBuilder. Then, because super admins should be able see everything, if $this->isGranted('ROLE_SUPER_ADMIN'), then just return the unmodified $queryBuilder so that all results are shown.

  But if we don't have ROLE_SUPER_ADMIN, that's where we want to change things. Add $queryBuilder->andWhere(). Inside the query, the alias for the entity will always be called "entity". So we can say entity.id = :id and ->setParameter('id', $this->getUser()->getId()). I don't get the auto complete on this because it thinks my user is just a UserInterface, but we know this will be our User entity which does have a getId() method. At the bottom, return . And... I guess I could have just returned that right here... so let's do that.

  I love it! Let's try it! Spin over and... nice! Just our one result. And you don't see that message about results being hidden due to security... because, technically, none of them were hidden due to security. They were hidden due to our query. But regardless, permissions are still being enforced. If a user somehow got the edit URL to a User that they're not supposed to be able to access, the entity permissions will still deny that.

  Next, each CRUD section has a nice search box on top. Yay! But EasyAdmin also has a great filter system where you can add more ways to slice and dice the data in each section. Let's explore those.

---
## [delete-44/inscryber](https://github.com/delete-44/inscryber)@[644e90f600...](https://github.com/delete-44/inscryber/commit/644e90f6004ac4e2097e47ed930a8aa5e274c695)
#### Saturday 2022-03-19 22:45:16 by Anthony

Merge pull request #72 from delete-44/feature/fuck-you-po3

Feature/fuck you po3

---

