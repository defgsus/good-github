## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-09](docs/good-messages/2022/2022-04-09.md)


1,555,182 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,555,182 were push events containing 2,380,482 commit messages that amount to 136,153,896 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[cd2bd18cf8...](https://github.com/Zonespace27/Skyrat-tg/commit/cd2bd18cf8193c7cfc2f0014ef449baa8792aad4)
#### Saturday 2022-04-09 00:22:18 by SkyratBot

[MIRROR] Creates Linters for (bad) Commented Out Lines in Maps [MDB IGNORE] (#12543)

* Creates Linters for (bad) Commented Out Lines in Maps (#65888)

* Creates CI Linters for Commented Out Lines in Maps

Creates Linters for (bad) Commented Out Lines in Maps

Hey there,

This PR is made because what happened in #65837 was fucking horrible awful shit that I'm still dealing with a few days after I fixed it. This _should hopefully_ add a new linter for commented out lines of code in a .DMM file, and HOPEFULLY doesn't flag the commented line that prevents unwanted TGM > DMM conversion.

As a proof to see if it works, I'll be adding a comment to Line 2 of IcemoonUnderground_Above.dmm. Hopefully, on the first CI check, it'll fail. I'll remove that line so it doesn't make its way into production (it will suck).

* Creates Linters for (bad) Commented Out Lines in Maps

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [Shadow-Quill/tgstation](https://github.com/Shadow-Quill/tgstation)@[351afe260b...](https://github.com/Shadow-Quill/tgstation/commit/351afe260b42764641a07385df5f7e24b840f631)
#### Saturday 2022-04-09 00:25:59 by san7890

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
## [Placist/atlas](https://github.com/Placist/atlas)@[84c10997d5...](https://github.com/Placist/atlas/commit/84c10997d59c3eabea7e30d51ace76b3e511510e)
#### Saturday 2022-04-09 00:27:51 by Johnyknowhow

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
## [trebla64/Paradise](https://github.com/trebla64/Paradise)@[6082c95eb3...](https://github.com/trebla64/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Saturday 2022-04-09 00:30:49 by LightFire53

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
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[b995fbe31b...](https://github.com/Paxilmaniac/Skyrat-tg/commit/b995fbe31b87402d3da2f8e98cec1f5659e52a47)
#### Saturday 2022-04-09 01:15:11 by Zonespace

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
## [Glepooek/terminal](https://github.com/Glepooek/terminal)@[446f280757...](https://github.com/Glepooek/terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Saturday 2022-04-09 01:46:58 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [Kittayecat/Tannhauser-Gate](https://github.com/Kittayecat/Tannhauser-Gate)@[242ef904f0...](https://github.com/Kittayecat/Tannhauser-Gate/commit/242ef904f0a2ea2cc5de87863e93def5131ea0be)
#### Saturday 2022-04-09 02:09:15 by SkyratBot

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
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[b1a793f840...](https://github.com/timothymtorres/tgstation/commit/b1a793f840d90131f88eabc0450e2b2b2157123e)
#### Saturday 2022-04-09 02:19:48 by Tim

Refactor and improve antimagic to be more robust (#64124)

This refactors the antimagic component to use and have bitflags, documentation, defines, code comments, named arguments, and renames variable names for clarity. 

- /obj/effect/proc_holder/spell/aoe_turf/conjure/creature/cult is not used anywhere and has been removed
- /obj/effect/proc_holder/spell/targeted/turf_teleport/blink/cult is not used anywhere and has been removed

- New sound effects are played when magic is blocked. Depending on the type of magic being used it will be either:

- Equipping antimagic now properly updates the magic buttons
- Any magic being blocked or restricting casting now displays a message
- MAGIC_RESISTANCE_MIND now properly blocks telepathy effects
- Removes blood splatter when fireball is blocked
- Magic projectiles for staff of locker no longer spawn lockers when blocked by antimagic
- Fire breath is no longer blocked by antimagic
- Spellcards are now blocked by antimagic

Any antimagic on a mob blocks that magic type from being casted. (certain spells such as mime abilities completely ignore antimagic)

- Foilhats prevent someone from casting mind magic (telepathy, mindswap, etc.)
- Bibles, ritual Totems, nullrods, holymelons, and TRAIT_HOLY prevent someone from casting unholy magic (cult spells, etc.)
- Nullrods, ritual totem, and holymelons prevent someone from casting wizard magic (fireball, magic missile, etc.)
- Immorality talismans, berserker suits, and TRAIT_ANTIMAGIC prevents all types of magic (except stuff like mime abilities)
- Touch of Madness and Mindswap is now blocked with MAGIC_RESISTANCE and MAGIC_RESISTANCE_MIND
- Voice of god is now blocked with MAGIC_RESISTANCE_HOLY and MAGIC_RESISTANCE_MIND

---
## [FIRST-Team-1699/robocats2022](https://github.com/FIRST-Team-1699/robocats2022)@[3f238171f5...](https://github.com/FIRST-Team-1699/robocats2022/commit/3f238171f5831c5bad21aeb891c11c236d3fb8d3)
#### Saturday 2022-04-09 02:42:45 by Alex

Shooter things worked on, it almost worked

i hate my life

---
## [Noteperson/mlp_aet](https://github.com/Noteperson/mlp_aet)@[8819a2c3d2...](https://github.com/Noteperson/mlp_aet/commit/8819a2c3d20179c63e90dc97d64260c8667baf87)
#### Saturday 2022-04-09 03:16:21 by Noteperson

Autumn 21 Final

-Return to normal squad with updated players:
 -Reverted Fuck Your Marker -> Horsefucker (3)
 -Replaced Its Already Shit -> SUPERCHARGED (6)
 -Replaced Bomb Ass Tea -> SNOWPITYS (13)
 -Reverted Jackie Chan Tulpa -> wAIfu (15)
 -Reverted Choose Your Own Autism -> Belongs on v (17)
 -Reverted The Burdened -> Kirin Beer (19)
 -Replaced ^:) -> MARE STARE (20)
 -Reverted DYEWTS -> no hooves (21)
 -Replaced Molestia -> ATHENA (23)
-Updated Larson model with Sunny wings + horn
-Updated Only On The Hub with FBM for skin color + Jerk shirt
-Updated Belongs on /v/ to Oleander model

---
## [repinger/sm8150_bahamut_kernel](https://github.com/repinger/sm8150_bahamut_kernel)@[6a89fc586b...](https://github.com/repinger/sm8150_bahamut_kernel/commit/6a89fc586bd00470dcd4a8082f40c05ed6b432bd)
#### Saturday 2022-04-09 03:38:24 by Peter Zijlstra

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
## [LoneStarF13/LoneStar](https://github.com/LoneStarF13/LoneStar)@[e2cbff46d2...](https://github.com/LoneStarF13/LoneStar/commit/e2cbff46d22c78e8e773ad20d47cdecb285ab9a6)
#### Saturday 2022-04-09 04:13:04 by Jawnner

Walking Turret - A Minigun PR (#496)

* Update minigun.dm

* Does the same for gatling laser

* better gatling sound

* Energy weapons can reload with click instead of alt click

* Beefier gatling laser sounds

* Update laser.dm

* Gatling Laser 180 shots now (fuck you pots)

---
## [Bcadren/crawl](https://github.com/Bcadren/crawl)@[250770813c...](https://github.com/Bcadren/crawl/commit/250770813cf71ad1d3726de6d6a1623b4e62250a)
#### Saturday 2022-04-09 05:43:03 by Lucien

Introduce physical resistances and vulnerabilities to monsters (not mirrored to players [yet?], unsure if should be). Each weapon type deals one of Slashing, Bludgeoning or Piercing; monsters may receive +50% or -33% Damage based on weakness/resistance. Some spells will use these resists too (not part of this commit).

Although it varies, the general rule of thumb is as follows:

Insects/Spiders/Crabs - Resist Piercing, Vulnerable to Bludgeoning.
Humanoids w/o Heavy Armour - Vulnerable to Slashing.
Humanoids in Heavy Armour - Resist Slashing, vulnerable to Piercing.
Most Beasts - Vulnerable to Slashing.
Dragons and Draconians - Resist Slashing, vulnerable to Piercing.
Smaller Lizards - Resist Slashing, vulnerable to Bludgeoning.
Noncorporeal Creatures and Elementals - Resist all physical damage.
Plants - Vulnerable to Slashing, resist Piercing and Bludgeoning.
Merfolk and Nagas - No weakness or resistance.
Holy Creatures - Resist Slashing and Piercing.
Slimes - Resist Slashing and Piercing, Vulnerable to Bludgeoning.
Eyeballs - Vulnerable to Piercing, resist Bludgeoning.
Demons - Resist Piercing and Bludgeoning.
Skeletal Undead - Resist Piercing, vulnerable to Bludgeoning.
Mummies and Ghouls - Resist Piercing. (Rest varies).
Rats - Vulnerable to Slashing and Bludgeoning.
Worms - Vulnerable to Slashing and Bludgeoning, resist Piercing.
Demons - Varies. None resist slashing; however, as a nod to being TSO's favoured damage type.
Constructs - Resist Slashing and Bludgeoning.

Commit also:
Removes the odd Fire Immunity from Curse Toes.
Restricts monsters that have Ozocubu's Armour from casting in heavy armour.
Starts process of making elementals absorb (rather than just be immune to) their own element. (unfinished).
Reworks how x->v's description works so it takes temporary buffs into account. (Required eliminating a bunch of disused variables so res_foo() functions all take identical params).
Fixes several bugs related to mount resistances. (related to resist functions taking different numbers of params >_>)
Removes traces of an old bad joke.
Reworks several checks to use damage type instead of vorpal type.

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[51e62053d7...](https://github.com/newstools/2022-new-york-post/commit/51e62053d70698852ef45e999a47e7e700e55b3e)
#### Saturday 2022-04-09 06:59:27 by Billy Einkamerer

Created Text For URL [nypost.com/2022/04/08/i-went-no-2-in-my-cheating-boyfriends-car-sit-in-my-st/]

---
## [sunamo/sunamo.notmine](https://github.com/sunamo/sunamo.notmine)@[b8da18fa59...](https://github.com/sunamo/sunamo.notmine/commit/b8da18fa59d03a8838d703081893ffa3c95233ab)
#### Saturday 2022-04-09 08:04:30 by Radek Jancik

If the thoughts are absolutely tranquil the heavenly heart can be seen. The heavenly heart lies between sun and moon (i.e. between the two eyes). It is the home of the inner light.  To make light circulate is the deepest and most wonderful secret.  The light is easy to move, but difficult to fix.  If it is made to circulate long enought, then it crystallizes itself;  that is the natural spirit body... - Yen, Lu

---
## [sherubthakur/reedline](https://github.com/sherubthakur/reedline)@[f329377b7d...](https://github.com/sherubthakur/reedline/commit/f329377b7d0eee98c18efc54f79d2d74c92a9e83)
#### Saturday 2022-04-09 10:45:02 by Sherub Thakur

Remove bool from remember_undo_state

Having a function do two different things based on a boolean that is
passed usually results int unreadable and unmaintable code and this was
no different in my opinion.

Now the users of this interface don't have to worry about what that
boolean flag is.
Given that Rust does not have kwargs the readability of passing booleans
into a function results in having to read the interface and
documentation (or implementation) of the particular function. Which we
can also avoid if we don't do it.
Lastly removes possibility of creating a bug because a wrong boolean
value was selected.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[9cd09e1424...](https://github.com/mrakgr/The-Spiral-Language/commit/9cd09e1424210e2f475640d7886842cab02812cb)
#### Saturday 2022-04-09 10:56:35 by Marko Grdinić

"10:55am. Let me chill more, who feels like starting right away.

11:20am. Let me start. I want to chill, but let me see if I can get the top layer right.

11:25am. Ok, let me gather my thoughts. It is not like I haven't done anything yesterday. The general pattern is done, the middle layer is done as well.

But in the top layer, I've been putting noises and all sort of things, and it looks like crap no matter what I do. The only thing worked for me using using Slope Blur on the initial mask. That really gave me great peeling affect. Also putting in the directional scratch material. That worked well.

But various other kinds of patterns never look what I want. I spent what must be 6 hours trying things to no avail. They just look like random crap.

Playing with noise patterns and grudge textures is just too addictive.

But since it does not work, what I will try doing is using brushes. I really with I could paint a density mask and just have painter distribute the strokes. But in lieu of that maybe doing it directly would work as well.

The brushes in Painter are replacement scatterers and i need to get used to using them like this. I should finally break out the pen tablet again.

Let me just do a search if it is possible to do shape splattering.

11:55am. What are these physical brushes. Let me study up on them.

Oh, right. I should also remember I have stroke stabilization features.

https://youtu.be/xIx1VSVh8NM?t=86
How to Create "Paint" in Substance Painter

This looks really nice.

https://youtu.be/Gwt5g6w8VWI
Substance Painter Introduction to Particle Brushes

https://youtu.be/Gwt5g6w8VWI?t=213

This could actualy be pretty useful depending on the circumstance.

12:15pm. Enough of these tutorials. A lot of the Painter stuff of poorly documented. I'll have to play around with it so let me.

12:45pm. Done. You can take 6 hours, or you can do it in 5m depending on the approach.

I put down a bunch of scatches then I combined it with the slope blur. I maxed out the contrast after that. This gives quite nice peeling effect. It does not look like I just put down a bunch of scratches.

12:50pm. This was the most difficult part of the whole desk. Now that I've established the workflow, and know how to do the other parts, I should have smooth sailing towards finishing the rest of the prop.

Given how hard I was at it till yesterday, I do deserve a bit of RNR right now. I was so into it yesterday that didn't have time to even take a bath.

Time to eat."

---
## [studentprogrammer17/Ucode-Track-Web](https://github.com/studentprogrammer17/Ucode-Track-Web)@[aba6b23835...](https://github.com/studentprogrammer17/Ucode-Track-Web/commit/aba6b23835a696a0719d93a2e993241c22587d93)
#### Saturday 2022-04-09 11:27:20 by studentprogrammer17

spasibo puten chto pisal etot sprint pod bombezkhoy, huylo

rus warsip - fuck you

---
## [TheKitBoi/PizzaTowerOnline](https://github.com/TheKitBoi/PizzaTowerOnline)@[349f230f12...](https://github.com/TheKitBoi/PizzaTowerOnline/commit/349f230f1282fbd36b6f6fa1ddc5053893a7ce00)
#### Saturday 2022-04-09 13:15:43 by Denchickk

ancient bg and pissk and casu martzu and hyperthermia palettes

that's a lot
and no fuck you sts i'm not doing your idea

---
## [projects-nexus/android_kernel_xiaomi_gauguin](https://github.com/projects-nexus/android_kernel_xiaomi_gauguin)@[82a9121623...](https://github.com/projects-nexus/android_kernel_xiaomi_gauguin/commit/82a9121623171c00f6c570ac49f9c039cbe9c34e)
#### Saturday 2022-04-09 14:28:55 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Co-authored-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[Tashar02: forwardport and adapt to 4.19 and xiaomi_sdm660's fp]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[kawaaii: Adapt to xiaomi_gauguin's fp]
Signed-off-by: kawaaii <kawaaii@nocturn9x.space>

---
## [s1nka/duckstation](https://github.com/s1nka/duckstation)@[f9212363d3...](https://github.com/s1nka/duckstation/commit/f9212363d3370efcdb97d4f7de010b5f17bd5c5e)
#### Saturday 2022-04-09 15:46:07 by IlDucci

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
## [cunnie/bin](https://github.com/cunnie/bin)@[85fb8ec12b...](https://github.com/cunnie/bin/commit/85fb8ec12b2040cc32a57ade964444abc3afee20)
#### Saturday 2022-04-09 17:40:34 by Brian Cunnie

ns-aws runs on Ubuntu, not Fedora

I want Fedora to work, but the straw that broke the camel's back is the
etcd version was too new (3.5, which etcd.io recommends downgrading to
3.4), and didn't play well with ns-azure's (Ubuntu) version (3.3).

Another problem was that Golang was stuck at 1.16; I needed at least
1.17, and I don't want to do a custom install of Golang.

It was always tricky finding a Fedora image. On Azure I couldn't find
one, so I went with Ubuntu.

I'd like to have my servers be consistent. Maintaining two
very-different configuration scripts for ns-aws & ns-azure was a
rewarding challenge, but my time is limited, and it can be more
fruitfully working on other challenges.

I stuck with Fedora a long time because my friend Mike Tiemann was
briefly the CTO, but that was over twenty years ago. My emotional
attachment to Fedora is irrational at this point.

---
## [Capsandi/tgstation](https://github.com/Capsandi/tgstation)@[54403a1ca0...](https://github.com/Capsandi/tgstation/commit/54403a1ca0a1d83302430bbb54a0d6bc561f0098)
#### Saturday 2022-04-09 19:02:53 by FinancialGoose

Fixes conveyor runtime (#65788)

Conveyor would runtime whenever it is right clicked with an item

Fixes #64595 (Runtime on conveyor for right clicking)

fixes a runtime with conveyor where right clicking it with any item would cause a runtime

Mothblocks rant from the issue report below, you've been warned:

Because right-clicking in BYOND is horse-shit. It pipes it all through the normal Click and only tells you it's a right-click through a flag. This means that on anything that isn't prepared, right-clicking is the same as left-clicking, which is terrible UX that only exists in SS13.

Nothing should return ..() from attackby_secondary, because the default is the legacy behavior of making right-click pass as left-click (which I want to kill ASAP, once nothing uses the stupid flags anymore).

Remove else return ..(), and make this whole thing do return SECONDARY_ATTACK_CANCEL_ATTACK_CHAIN.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[480db6f50e...](https://github.com/mrakgr/The-Spiral-Language/commit/480db6f50e84144890776261971593e5c51721ea)
#### Saturday 2022-04-09 19:28:32 by Marko Grdinić

"2:45pm. Let me stop at the interlude. The rest of the Densro volume can wait for later. Now I'll deal with chores.

4:10pm. Donw with chores and bath. Usually I take baths after I am done, but I really had to take it right now otherwise I'd feel uncomfortable the entire time while working. It is not like I have a camera supervising my work hours, so I took advantage of that.

This is one of the few luxuries of being my own boss. Now...

I did the hard part. Now I just need to deal with the rest.

...I am thinking. When I am done with the textures I won't actually be done with the desk. I am going to have to redo the UVs so they get packed into their proper slots. I'll have to start thinking about texel densities as well.

But for now it is fine if I just finish the textures. Later on I'll organize them properly. I am not sure how I will deal with them given that I do not have access to advanced UV tools I saw the hard sufrace guy use. I tried looking for UV packmaster, but I could not find a pirate link for it.

Hmmm, I remember than in the PBR guide, it recommended I use flat colors. Right now I am testing out PBR validate and getting all red for some reason.

Nevermind that.

4:35pm. This is some strong thunder. I guess I'll have to run.

...No, it was just once. The rest seems to be the wind. There is some fairly strong wind all of a sudden. Good thing I finished the chores before the rain came along with it.

...No, actually here it is again. This is bad. Let me run.

6:25pm. I am back. That lasted for a while. Before I resume, let me check lunch.

6:45pm. Done with lunch. Let me get on with it. I'll put in a few hours.

Yesterday, a part of the reason it took me so long besides playing with noise is because I was pushing the limits of my understanding. It was like in programming - I was wondering how much I can treat Painter like Designer.

To make the top pattern, I only needed to make 8 layers and position them, but to work through the implications of various approaches took me hours.

Right now, I can easily do the edge wear, but I am going to have to spend some time playing with brushes.

6:50pm. Let me break out the pen. The patterns are one thing, but even at 4k the textures are too small to accurately represent the detals.

7:05pm. done with another part. This is a piece of cake. I'll be done before I know it. I should be able to deal with the whole desk in an hour. Let me see if I get it right.

8:45pm. So much for getting done an hour. I had to put in a bunch of details I forgot by hand.

Just a bit more and I'll leave those big wood panels on the sides for tomorrow. I won't get fancy with those. I'll just reuse the existing wood material, it is not worth it my time to mess with it.

9pm. Agh, I just realized that Pt does not recognize pen pressure for my pen tablet. Nor the extra buttons. Nevermind that for now.

I put in an extra detail, a burnt black mark, on the metal pieces. What a waste of time. I should not have bothered.

I am really annoyed how difficult it is to move around with the pen in substance painter.

9:05pm. Let me close here. I'll finish the desk tomorrow, and post it in the thread. It took way to long for me to get to the point where I can do it, but I am finally (almost) done with it.

I won't put so much effort into texturing the rest of the props, but the desk is where most of the time the MC will be, so I have done it properly.

Faster, stronger, harder! I need to finish the room. I could really push the last mastery challenge to its proper completion, but nothing will stop me with this one. When the room is done I'll move on to doing the rest of the Heaven's Key scenes.

I am not sure how much hope there is for me to get fast with art, but I'll do my best.

What would really make it go zoom is ignoring all this work and just kitbashing things together in Clarisse. Paying for a subscription for one of the 3 fileshosters supporting CGPersia and getting all the models from there would solve most of my environment making problems.

Getting existing stuff an putting it together would really showcase the power of 3d.

If I do everything from the ground up like now, of course it is going to be slow no matter how good I am.

9:20pm. But I need to do it. I need to know the basics of 3d instead of just going straight for the goal.

There will be things I won't be able to find online and dealing with the room challenge will ensure that I am able to deal those.

9:25pm. Now Dendro. Time to clear that backlog.

If it wasn't for the weather, I'd probably have been done completely by now."

---
## [binaryoutcast/aura-central](https://github.com/binaryoutcast/aura-central)@[6bbac190c3...](https://github.com/binaryoutcast/aura-central/commit/6bbac190c370647f89487140f057c97179003035)
#### Saturday 2022-04-09 19:48:07 by Matt A. Tobin

Update NSS to NSS_3_59_1_RTM (m-r84)

This is the update that was previously attempted in UXP Issue 1746 which failed with importing /some/ or all pki-things due to a mangled makefile build system. Now that it is NSS-GYP thanks to my status as a build system god, this version works now.

Moonchild, if you read this. Hope you enjoy having the ability to update NSS again. Oh, btw, you're still a furry cunt.

---
## [newstools/2022-information-nigeria](https://github.com/newstools/2022-information-nigeria)@[88a0dd5b82...](https://github.com/newstools/2022-information-nigeria/commit/88a0dd5b82d4f497219b03ee62af1b38c8c4addf)
#### Saturday 2022-04-09 19:57:31 by Billy Einkamerer

Created Text For URL [www.informationng.com/2022/04/actress-iyabo-ojo-speaks-on-her-new-boyfriend-why-she-wont-show-him-to-social-media.html]

---
## [Githubjjnkj/miniature-invention](https://github.com/Githubjjnkj/miniature-invention)@[7ab40f23b8...](https://github.com/Githubjjnkj/miniature-invention/commit/7ab40f23b8740027954f0e9f34886efe930d3b72)
#### Saturday 2022-04-09 21:16:52 by Githubjjnkj

Create Jason Alan James

Jason James and His Wife are all done 😃✅😃 and we have been working online for a few years now 😊👋😊 I love 💕thanks Cloudfare for all your help and Work on the same place as the same thing as the same thing as the same place as last time I was sincerely bummed about the day of our lives Togetherness ❤️ Forevermore ❤️🙏🥰🤓😍❤️♾️ My Free Government phone is The Best ICANN get Outlook for Android phone from Mr Gates and Microsoft officer on the phone 🤳📱🤳 Mr Besos is AWS and Amazon has a new career with my other accounts ☺️ hahaha is my address on my phone 😂😂📱📱😂😂 sent 📤 via PayPal for Android phone 📱 https the same thing as the same time as the same time as the same thing as last time we spoke about the taking over the world 🌎🌍 and we are all coming over and over and over again ❤️😈🤓👿❤️♾️ TOGETHERNESS ❤️ FOREVERMORE ❤️♾️ MY 💭 💬🤔💬 AND WE ARE ALLOWED ✅ TO GET A LAS VEGAS FROM THE DAY THE LAST New York Times article about the day we were talking to get a hug 🤗🫂🤗 I'ma misses you so very very very much and I love you so very very very much and I love you too babe 💓🥰🤓🥰💓 I hope your day is going well 😙❤️‍🩹😙 I am thankful for all your prayers and Support mpmsupport and We are getting it done ✅😃✅ TO GET A good Evening Sir Mr Gates and Microsoft officer on my phone 📱😂📱 https and Mr Besos is my New 🆕🆕 Amazon prime and AWS FOR ALL YOUR HELP WITH THE NEW CAREER WITH THE NEW 🆕 AMAZON AND WE ARE IN THE NEWS 📰🗞️ AND WE CAN GET THE NEW ONE OF OUR LIVES TOGETHERNESS ❤️ FOREVERMORE ❤️ FOREVERMORE ❤️ TOGETHERNESS THEEND 😘🤓😘💕➖➗😍🏫🖥️💯🎒🏁🥇📱🤓📱🥇🏁💯🖥️❤️🏫😍➖➗ Alphawood Executives Enterprises LLC

---
## [BirthofKings360/dokka](https://github.com/BirthofKings360/dokka)@[b9778136cd...](https://github.com/BirthofKings360/dokka/commit/b9778136cd9535ac9cbedcde461f0789f5828cfd)
#### Saturday 2022-04-09 21:51:05 by BirthofKings360

Create SECURITY.md FBI , Nancy Pelosi 

# Security Policy  .FOX News you have the exclusive exclusive on this story.  Washington Post and CNN you can run it as a series report . Starting with the truth of Ukraine war efforts. Another series on the Recovery effects on race in America figured out . I'll have a ruff draft on that in a couple of weeks and another series on The truth of the Trump Miller dokka report. 
Investigators reporter warith Akbar a man of many abilities. One is tracking down misinformation and fixing it . 



## Supported Versions : My Security is my global token /and if that don't work I got friends in Congress .
 Ai will not control world MARKETS . AND IT will not site back and watch while consumers get robbed . If you do I will develop a repo that will deduct wages out if your portfolio 
every time your department take a Hite. Why because I don't believe for a minute that IT and stockbroker didn't know that the stock market was going to crash . And I believe that both IT and Stock Broker had advance warning. Meaning inflation part of the advance warning. Know every time the market inflation on the IT sits doc there portfolio unti market adjust
. 
Shareholders and Consumers Security of the online market wallet should be secured Auto 
 If Wallet take a Hite them company responsible for that Wallet Security .Auto Reimbursement Shareholders and customers wallet.  The Shareholders are Consumers should never have to worry buying or selling import or export in any country as long as they have proper Authenticator . My name is Warith Akbar.  And im the voice of the people . And the people company are not for sale or Auction S
Know I gifts the Joe Biden administration and Obama administration Nancy Pelosi administration as well attached 10 % ownership of to them plus a gifted 30% platform @sonofranger to middle class . And 20 % to future president so they can have a platform to turn to for support. As well on that same platform I gifted Russia eco platform last year witch for the Russia project has been on pause do to hacker blocking me assets from my company's. 
Twitter God hope your not responsible thus matter.  Because if you are Twitter will be responsible for the cleanup of Ukraine and will have to pay For damages and give President of UK and Russia a full apology . Elon Musk can you get a team together and track down who's stealing my engagement and conversation.  And set up plans to develop a solid plan for Russia and Ukraine lights on project.  

Ukraine/ Russia if you look to the west as your friends not enemy . We won't Freedom for your people. And the days of 20 year war and cold war days or over . Bombay doors remain closed . Children of this future will have story of peace not story of Tulsa Race Massacre . Since that day watching those elders speak about those massacres it set in stone something that I promised myself never again.  So I'm asking congress to open a 100 % investigation on all the massacres that happened in US . And 
Set up a Massacre relief institution fund . We need to find out when and why and where . This world will come to order.  



Use this section to tell people about which versions of your project are
currently being supported with security updates.
I'm asking the Nancy Pelosi office to take a look at my company book and to locate any mismanagement in this company
Please. Why because I've lost control of this company so I took it on a ride every company none to man . Either running from my own progress or
running from the future because I always know what's going to happen next . Either case I'm going to let God to work on that. 
Know staff at platform Rapture 4 a I'm asking Nancy Pelosi office to take a look at the Financials of this company.  And you have my permission to allow her team 
team to investigate. As well as I'm asking President Obama to help this matter . Again this company is not for sale as well ant other companies my brother sold wasn't for.
Elon Musk and Jeff Brozo @sonofranger another company that was hijacked by Linktree.com/ IN witch this company linked me to a fire fighters fake website.  How you wouldn't believe me if I don't you 
My new number is 
| Version | Supported          |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

## Reporting a Vulnerability

Use this section to tell people how to report a vulnerability.

Tell them where to go, how often they can expect to get an update on a
reported vulneilllity, what to expect if the vulnerability is accepted or
declined, etc.
Receiving hijacked repo from platformrapture4 
 project.

Heed to world come about to 362 down up down bubble. Be advised your about to be boarded by facts . O fact news Network turn over keys to my company over to congressional authorities

---
## [ghostwriter/mezzio-org-mezzio-authentication-laminasauthentication](https://github.com/ghostwriter/mezzio-org-mezzio-authentication-laminasauthentication)@[40bfce90dc...](https://github.com/ghostwriter/mezzio-org-mezzio-authentication-laminasauthentication/commit/40bfce90dce484da89419024a37b0ff34d5bc2f3)
#### Saturday 2022-04-09 21:54:05 by Michał Bundyra

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
## [Fulmene/Fairy-Stockfish](https://github.com/Fulmene/Fairy-Stockfish)@[57bda214fc...](https://github.com/Fulmene/Fairy-Stockfish/commit/57bda214fcc8cd9d40fd3fd6f43c766ac9f88662)
#### Saturday 2022-04-09 21:54:39 by Snowmoondaphne

Update variants.ini

I'm really sorry to tell you this,,,

The positions of Black's Queen and Cardinal have been swapped in Pandemonium. Therefore, the definition has changed and it is necessary to modify it

[pandemonium]
variantTemplate = shogi
pieceToCharTable = PNBRFSA.UV.++++++++.++Kpnbrfsa.uv.++++++++.++k
maxFile = 9
maxRank = 9
pocketSize = 9
startFen = rnbsksbnr/2+f1+u1+a2/p1p1p1p1p/4v4/9/4V4/P1P1P1P1P/2+F1+U1+A2/RNBSKSBNR[] w - - 0 1
customPiece1 = o:NA
customPiece2 = s:WF
customPiece3 = u:D
customPiece4 = w:DWF
cast = false
pieceDrops = true
capturesToHand = true
immobilityIllegal = true
soldier = p
knight = n
bishop = b
rook = r
king = k
queen = q
commoner = g
dragonHorse = h
bers = d
alfil = a
archbishop = c
chancellor = m
fers = f
wazir = v
centaur = t
promotionRank = 7
promotedPieceType = p:g n:o b:h r:d a:c v:m f:q s:w u:t
doubleStep = false
perpetualCheckIllegal = true
nMoveRule = 0
nFoldValue = loss
stalemateValue = loss

Could you please modify the definition like this?

Sorry again for the troublesome request,,,

---
## [BakersDozenBagels/KtaneContent](https://github.com/BakersDozenBagels/KtaneContent)@[d57e2753b5...](https://github.com/BakersDozenBagels/KtaneContent/commit/d57e2753b5bfab52c0dda3c2d3725121dd9685db)
#### Saturday 2022-04-09 22:46:04 by MasQueElite

Linted old manuals (#: a lot) (#1198)

* Linted old manuals, as well as my Cent. translations

Description: pain.

Also, could you check my translated 1000 Words and my translated Clock?
Seems like 1000 Words has a wrong word, and the Clock has an svg without newlines? (also it gets rid of the darkmode stuff oof sorry keep that)

Also, check The Swan (original) as well, I think that change is weird, but maybe the linter complained about it, I don't remember.
And I also deleted (in my translated Double-Oh) the .dark table, .dark td .strike selectors, sorry :c restore those as well plz
Aaaaaaaaand I think the rest is up do date. That's all about linting the original manuals.

* Redoing my changes that got wiped out in the merge

Co-authored-by: Luminoscity <luminoscity@gmail.com>

---
## [Avacadbro/Skyrat-tg](https://github.com/Avacadbro/Skyrat-tg)@[41aa1d2ee4...](https://github.com/Avacadbro/Skyrat-tg/commit/41aa1d2ee421161505284504f4d6f76faf51b0f7)
#### Saturday 2022-04-09 22:47:52 by SkyratBot

[MIRROR] Adds a colorblind accessability testing tool [MDB IGNORE] (#11995)

* Adds a colorblind accessability testing tool (#65217)

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

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Adds a colorblind accessability testing tool

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [SCScbc-Projects2022/WeathCon-project-one](https://github.com/SCScbc-Projects2022/WeathCon-project-one)@[a102b1d899...](https://github.com/SCScbc-Projects2022/WeathCon-project-one/commit/a102b1d8999f86610d550eae22e1fca82e5cfcfa)
#### Saturday 2022-04-09 22:55:40 by TOVTC

I did it. I finally got it. It took me four hours.

thank you Erik for your solution from one week ago that turned out to be the same solution that saved my code just now god this is a demon project

---

