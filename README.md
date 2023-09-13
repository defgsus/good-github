## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-12](docs/good-messages/2023/2023-09-12.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,430,910 were push events containing 3,743,997 commit messages that amount to 308,843,747 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [skeyuui/russ-station](https://github.com/skeyuui/russ-station)@[297f7f88e8...](https://github.com/skeyuui/russ-station/commit/297f7f88e866d4a17b27cb15c0b8ee606742bbf6)
#### Tuesday 2023-09-12 00:04:36 by Sealed101

Fixes things about goliaths: wallhacks/range hacks(no, really) and tentacles not spawning in mineral turfs; also fixes `find_potential_targets` wallhacks (#77393)

## About The Pull Request

Goliath's sand digging behaviour could potentially target a turf that's
actually unreachable by the goliath, e.g.
```
G#
#T
```
where G - goliath # - wall T - target turf. fixed that, but i think
there could be something easier here, maybe instead grabbing turfs in
goliath's `view()`? unsure

The component goliaths use to telegraph their attacks
(`basic_mob_attack_telegraph`) casts a `do_after()` to perform the
attack, but it was not actually checking for the target staying in melee
range, as it was using the source goliath as both `user` and `target`,
so it didn't actually care at all for the target. Implemented an
`extra_checks` to `Adjacent()` since that's the closest we get for melee
range shenanigans I suppose
This still allows the source basicmob to attack the target if the target
moves around the source basicmob.

`!`Goliaths were also able to summon tentacles on a target that moved
into cover and still stayed in the `find_potential_targets` target
range. Which meant more wallhacks. This was a thing for the base
`find_potential_targets`, meaning that every basic mob using it was a
dirty haxxor (or very vengeful). Fixed that by making
`find_potential_targets` also check for `can_see()` before proceeding
further down `find_potential_targets/perform()`. `!` The only exception
to this check currently are bileworms.

`!`Goliath tentacles were not spawning in mineral turfs as their
`Initialize()` checked for closed turfs before handling mineral turf
mining. Fixed that as well.

## Why It's Good For The Game

![Dr__Hax_by_Didgeridoo_Dealer](https://github.com/tgstation/tgstation/assets/75863639/fbcbfc1b-f489-435e-bb01-677f55398787)

## Changelog

:cl:
fix: fixed goliaths digging sand that they can't actually reach (behind
windows or inbetween closed turfs)
fix: fixed goliaths melee attacking their target despite the target
running away from goliath melee range
fix: fixed goliath tentacles not spawning in mineral turfs
fix: fixed goliaths summoning tentacles on targets that moved behind
cover but stayed in their targeting range. this applies for most basic
mobs, really, so if any basic mob was targeting you despite you hauling
ass behind cover, they shouldn't anymore
/:cl:

---
## [AwesomeGitHubRepos/linux](https://github.com/AwesomeGitHubRepos/linux)@[1548b060d6...](https://github.com/AwesomeGitHubRepos/linux/commit/1548b060d6f32a00a2f7e2c11328205fb66fc4fa)
#### Tuesday 2023-09-12 00:06:51 by Linus Torvalds

Merge tag 'topic/drm-ci-2023-08-31-1' of git://anongit.freedesktop.org/drm/drm

Pull drm ci scripts from Dave Airlie:
 "This is a bunch of ci integration for the freedesktop gitlab instance
  where we currently do upstream userspace testing on diverse sets of
  GPU hardware. From my perspective I think it's an experiment worth
  going with and seeing how the benefits/noise playout keeping these
  files useful.

  Ideally I'd like to get this so we can do pre-merge testing on PRs
  eventually.

  Below is some info from danvet on why we've ended up making the
  decision and how we can roll it back if we decide it was a bad plan.

  Why in upstream?

   - like documentation, testcases, tools CI integration is one of these
     things where you can waste endless amounts of time if you
     accidentally have a version that doesn't match your source code

   - but also like the above, there's a balance, this is the initial cut
     of what we think makes sense to keep in sync vs out-of-tree,
     probably needs adjustment

   - gitlab supports out-of-repo gitlab integration and that's what's
     been used for the kernel in drm, but it results in per-driver
     fragmentation and lots of duplicated effort. the simple act of
     smashing an arbitrary winner into a topic branch already started
     surfacing patches on dri-devel and sparking good cross driver team
     discussions

  Why gitlab?

   - it's not any more shit than any of the other CI

   - drm userspace uses it extensively for everything in userspace, we
     have a lot of people and experience with this, including
     integration of hw testing labs

   - media userspace like gstreamer is also on gitlab.fd.o, and there's
     discussion to extend this to the media subsystem in some fashion

  Can this be shared?

   - there's definitely a pile of code that could move to scripts/ if
     other subsystem adopt ci integration in upstream kernel git. other
     bits are more drm/gpu specific like the igt-gpu-tests/tools
     integration

   - docker images can be run locally or in other CI runners

  Will we regret this?

   - it's all in one directory, intentionally, for easy deletion

   - probably 1-2 years in upstream to see whether this is worth it or a
     Big Mistake. that's roughly what it took to _really_ roll out solid
     CI in the bigger userspace projects we have on gitlab.fd.o like
     mesa3d"

* tag 'topic/drm-ci-2023-08-31-1' of git://anongit.freedesktop.org/drm/drm:
  drm: ci: docs: fix build warning - add missing escape
  drm: Add initial ci/ subdirectory

---
## [GlossyXangles1423283/creator-docs](https://github.com/GlossyXangles1423283/creator-docs)@[bda129ba9e...](https://github.com/GlossyXangles1423283/creator-docs/commit/bda129ba9e00a3a2d670f16a6f05129baa11c13d)
#### Tuesday 2023-09-12 00:20:36 by GlossyXangles1423283

Update

Pls change it and can I create accessories pls I really want to make some and I heard about the rdc im so sorry about that and I hope you do another one next year and could you help me get some subscribers pls its my dream my yt channel is ayla gaming with 209 subscribers I do roblox and gacha thank you for reading this💖 love ayla

---
## [pwnrazr/kernel_raphael_sm8150](https://github.com/pwnrazr/kernel_raphael_sm8150)@[0554dead12...](https://github.com/pwnrazr/kernel_raphael_sm8150/commit/0554dead12261f28c519ea49ba1771913d173f2f)
#### Tuesday 2023-09-12 00:43:46 by Peter Zijlstra

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
Signed-off-by: atndko <z1281552865@gmail.com>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[d93dfbc35c...](https://github.com/jlsnow301/tgstation/commit/d93dfbc35c4b86435f9b436160e0d6c0670a8e28)
#### Tuesday 2023-09-12 01:06:22 by Sealed101

Adds Summon Cheese (#77778)

oh apparently this is my 100th PR on tg, which is weird because github
reports 99 total, and i made at least one to the old voidcrew repo, and
filtering tg prs by my name still shows 99. weird. here's to 100 more i
guess?

<sub>could have been better if it was a get, jhonflupwliiard watch ur
back 🔫 </sub>

## About The Pull Request

Adds a new spell granter book to the Wizard's Den - Summon Cheese, which
grants the spell by the same name, which summons 9 heads of cheese.
That's about it, I think.

## Why It's Good For The Game

Wizards are a hungry bunch, so why can't they just summon food? They can
even share, if they'd like, since the notion of a friendly wizard still
exists

<details>
<summary>... </summary>

alright fine
i'm slightly malding over not getting the 77777 get so no more
roleplaying in the pr body

Wizard Grand Ritual now has a hidden goal of sacrificing 50 cheese
wheels. Sacrificing a cheese wheel is done with invoking the grand rune,
and each invocation/pulse of the rune will whisk away more cheese until
all cheese on the rune is taken by whichever entity lurks in the other
realm. The sacrifice will be hinted at in an _ancient parchment_ which
will be on the bookshelf (when i add it lmao) alongside the spell book.

Meeting this cheese goal will lock the wizard's grand finale rune and
grand finale effect to special ones. The cheese rune is mostly identical
to the normal grand rune, barring the custom sprites/animations.
The cheese finale consists of the wizard getting permanent Levitation
(nogravity + free space movement), a 0.5 modifier(reducing incoming
damage in half) to every damage type, a comically strong mood buff and
**The Wabbajack**(separate sprite pending) - a juiced up chaos staff
which can fire a lot more projectiles than a normal one can (it will get
more, I may even make a few just for it).
Everybody else (including any invader antags) gets hallucinations, 175
brain damage and a comically strong mood debuff, as well as a vendetta
against the wizard. If the victim was already suffering from
hallucinations from a trauma (including the quirk), they are instead
healed.

if you didn't catch the obvious reference, this entire shtick is a
tribute to Sheogorath. the rune makes use of daedric script, and most of
the catchphrases are a direct quotation of the Daedric Prince of
Madness, so if any of those things can get us in trouble somehow, let me
know. i will be sad but i will comply.

This shtick is intended as an easter egg, really, so I wasn't really
planning on expanding the wizard grand finale into heretic paths thing
or whatever.

Oh, and finale grand runes now allow the wizard to select the effect
even if it's time-gated. If it is, you just won't be able to invoke it
until the time comes. The rune will tell you how much time is left until
you can invoke it. And grand finale runes with a finale effect selected
also glow in the color of their effect. I also think I fixed some step
of the grand rune animation not triggering but I'm not sure.

<details><summary>Some rune animations (some are subject to
change)</summary>


![rune_cheese_activate](https://github.com/tgstation/tgstation/assets/75863639/62ae184d-b6fc-4883-a169-4d8ca7636b40)


![rune_cheese_flash_2](https://github.com/tgstation/tgstation/assets/75863639/619545c8-3c55-4264-bfa4-d40067ef7406)


</details> 

## Why It's Great For The Game

it's funny

</details> 

## Changelog


:cl: Sealed101, EBAT_BASUHA for spritework
add: Wizard's Den now has a book of Summon Cheese in the Studies Room
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[fc836593a5...](https://github.com/jlsnow301/tgstation/commit/fc836593a51771fc6c06adfa28f81d3cd134a501)
#### Tuesday 2023-09-12 01:06:22 by GuillaumePrata

Makes fanny packs be silent, others can't see what you put in or take out. (#78010)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Just like the syndicate toolbox and a handful of other items.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This is a blatantly stealth antag buff.

Pockets are 2 silent storage slots everyone has, so it is not adding
anything that antags didn't have access already.
But going from 2 to 5 small items can help a lot, also belts are a lot
smoother to use with their shortcut keys.

Love stealth antags, hate murderboners, gonna help my stealth boys not
be valid hunted because someone checked their chat logs from 10 minutes
ago and read that X player put Y contraband in their bag.

Or people that have some contraband names highlighted on chat... but no
one does that right.... right?
<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

## Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. You can read up on GBP
and it's effects on PRs in the tgstation guides for contributors. Please
note that maintainers freely reserve the right to remove and add tags
should they deem it appropriate. You can attempt to finagle the system
all you want, but it's best to shoot for clear communication right off
the bat. -->

:cl:Guillaume Prata
balance: Fanny packs are now silent, no one will get a chat message
about what you put in or take out.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Aki Ito <11748095+ExcessiveUseOfCobblestone@users.noreply.github.com>

---
## [RikerW/dNAO](https://github.com/RikerW/dNAO)@[de3efe593e...](https://github.com/RikerW/dNAO/commit/de3efe593e96d533fcc03a0562599b071010c620)
#### Tuesday 2023-09-12 01:06:30 by RikerW

add knightly styles

following the etherpad outline wiith minor tweaks

all knights can get expert in any of the 4 style skills: shield bashing, great weapon fighting, half-sword style, and advanced knightly styles
in total, 6 styles exist - those 4, but advanced is one skill for "sacred style", "runic style", and "eldritch style". the same skill is used for the 3, so enhancing/training via any work for the others
all skills can be used when unskilled, they just probably don't do anything (shield/half sword have minor effects), because you need to be in the stance to train it

style breakdown:

shield bashing:
- allows you to make an offhand shield attack when in the style where uarms exists. does not really like two-weaponing + uarms exists, but that shouldn't happen, jsut don't add paired greatshields.... yet
- this shield attack uses hmon and treats this as a proper weapon attack, so it will add enchantment or property bonus damages like a normal weapon attack. this is treated as having a base die of d2/d4/d6/d8 for unskilled->expert skills, and dmod is factored in as normal so a large shield is larger funny numbers
- the whole dmod/damage thing doesn't go SUPER well with the assumption that all shields are one-handed regardless of size (cuz armor slot not weapon slot) but hey, it would be really badass...
- this actually would work well if a shield arti/otyp with bonus damage is added later, or even just a spiked kite shield or something in the knight quest
- note that any shield always has the same damage dice, regardless of size
- the offhand attack also lowers morale by a substantial chunk. caps at -0/-5/-10/-15 for unskilled->expert, dealing 1/1/2/3 points of morale damage each. is this really strong? possibly. I'm not really sure the balance implications of -15 damage to all attacks after 5/6 hits on something, but my logic here is that you're trading a shield with decent but mediocre damage for the debuff, and you'd kill most things in <6 hits anyway. if it lives longer, then the -15 morale is probably justified on that target
- trains shield bash skill by bashing with things, successful hits like any other weapon skill (just added a thing to wtype for shields)

great weapon fighting:
- reduces the minimum roll for bimanual weapons, depending on skill, by 0/1/2/3 for unskilled->expert. so unskilled is no effect, but expert makes d6 always roll 4-6
- this is implemented as NdX becoming Nd(X-i) + N*i, where i is the highest roll we're slicing off. so 3d6 becomes 3d3 + 9. this stacks with both exploding and lucky dice, but NOT exploding lucky dice, because 1. it's probably really strong as-is on an exploding d6 or something, and 2. i'm not fucking with those functions
- possibly the easiest here to use, since it has absolutely no downsides and only upsides. balance-wise, shouldn't actually be too much of a big deal for non-exploding weapons, since this doesn't add any extra damage (by definition) only makes your damage more consistent/raises your avg, not the peak damage
- trained by attacking with bimanual things while its active

half-sword style:
- basically, allows longswords to be shining and two-handed, but locks them to piercing and two-handed.
- the real-life thing apparently involves grasping the middle of the sword with your offhand to help aim/improve your thrusts, so this turns all longswords to bimanual. oversized ones presumably just require two-hands like normal, just positioned differently - ignore the whole thing about "your arms reaching the halfway point".
- this cannot be swapped to or off of with a cursed longsword/no free hands, since it involves repositioning your hands
- the gameplay effects are kind of odd. at first, the issue was "why train past basic if it pierces ac/dr at basic", or s/basic/whatever skill/. so i gave it like, 1d6-3d6 precision damage with skill, so that's a minor damage bonus. then i later implemented the two-handed thing, so now it also has the niche benefit of letting you forcibly two-hand your sword, so if you're fighting with only one sword (no shield or twoweap) then you can get the 2x str bonus + the precision damage. this is probably pretty good, becausee i'ts "free" damage (applies to almost everything), but the actual dmg values are kinda low sooo
- trained by making precision attacks while its active (no bonus damage at unskilled thouhg, just training)

sacred style:
- allows for bonus holy/unholy damage for any weapon
- costs 5 pw/hit, doesn't activate if <5 pw
- deals an extra 1d8/3d8/6d8 holy/unholy damage at basic-expert. unskilled is no damage
- holy/unholy is decided by being holy for holy/neutral gods with good align, or chaotic/void gods with bad align. vice versa for unholy damage
- the damage DOES require the sword to actually BE blessed/cursed, it's not like artifact holy dmg where its always applied and double for vulnerabilities, this extends the normal blessed/cursed item damage (and stacks with it, for things like excalibur etc.)
- trains your advanced techniques when successfully dealing bonus holy/unholy damage (even if no damage is applied bc unskilled)

runic style:
- allows for MR when wielding a long sword above basic skill
- that is it. does not do anything else, can't train it or anything (it woudl train advanced ofc but like, you just can't train it).
- if you are wielding a long sword, if you have above basic skill, and you're in the form -> MR get.

eldritch style:
- allows for extra elemental damage for any weapon
- basically, you select a spell that you know and can cast, and apply its damage type to your weapon
- valid spells are fireball/storm, cone of cold/blizzard, lightning bolt/storm, acid splash, poison spray, finger of death
- they each grant their element damage. dice are 1/3/6 for b/s/e, size is 13 for death, 8 for the storm spells, and 6 otherwise
- note that death checks AD_DARK because.... i think it's cool? and also probably easier htan fuckign with AD_DISN or some shit. i think its appropriate. poison also sets weapont o have basic poison because i want lawful penalties for poison. acid is OK lugh doesnt notice. not like u can easily get acid/poison without BOIS or ana bones, and poison isnt good so its fine
- to actually apply the damage, you must know the spell and have good odds of casting it. i think right now (i realize as i write this) you can probably set the spell, forget it, and it won't unset the damage - so that'll be fixed later, i have to write more messages too so
- the damage is applied with same odds of spell success, so percentage > rn2(100) basically. so a 75% fail rate with expert kni advance skill on finger of death gives a 25% of 6d13 dark damage per hit, 75% nothing. trains skill regardless though. doens't care about attack spell skill unless you need it to cast - so 0% fail artis DO work with this.
- trains every single time you hit with it active, regardless of whether its applying extra damage. i'll change that later to be "every time it would have applied damage if you weren't unskilled" probably.

oh yeah styles are blocked by
sacred, eldritch - nothing (eldritch cares about spell success)
great wep - no bimanual weapon
shield bash - no shield
runic - no long sword
half-sword - no long sword that you can two-hand (i.e. no uarms/twoweap/whatever)

TODO:
- add messages to sacred, eldritch styles
- move skill up code for eldritch styles
- need to double check when sacred/eldritch styles are applying. it SEEMED fine, and it's intentional that they should still work on some thrown items, but it definitely needs to be looked at
- all knights get this. should berith give some of this? i have NO clue. i will 99% chance not add it to anybody else, but for the future. dwarf knights do get this btw

---
## [EternalBlueFlame/Traincraft-5](https://github.com/EternalBlueFlame/Traincraft-5)@[013605055d...](https://github.com/EternalBlueFlame/Traincraft-5/commit/013605055d1d02e8c70c8be8483811be24f4333c)
#### Tuesday 2023-09-12 02:35:50 by broscolotos

omg he did

-Fixed dupe when breaking trains sometimes. Happened because an entity can die twice in a single tick??? dumb game
-Added page memory to the paint bucket GUI; when you open the UI it will default to the entities current skin instead of the default. Maybe add to config later
-Added "Random" button to paint bucket GUI. Will select and apply a random skin out of the available skins.

---
## [nevimer/Bubberstation](https://github.com/nevimer/Bubberstation)@[c6e0ba7516...](https://github.com/nevimer/Bubberstation/commit/c6e0ba75169d010e2cdfa48134003b0bb9ab8485)
#### Tuesday 2023-09-12 02:40:44 by SkyratBot

[MIRROR] Drill module automatically disables if it's about to drill into gibtonite [MDB IGNORE] (#22990)

* Drill module automatically disables if it's about to drill into gibtonite (#77385)

## About The Pull Request

Drill module automatically disables if it's about to drill into
gibtonite.

## Why It's Good For The Game

> Drill module automatically disables if it's about to drill into
gibtonite

There's not enough time to react, the mining scanner is surprisingly
slow sometimes and it means you drill straight into gibtonite, which
primes it the first drill and blows it up the second, which is a lot
more of a pain than it sounds because drilling is night-instant. These
explosions are usually enough to crit you, and if they don't, the stun
and area clear means any fauna can wander in and finish you off.

The auto-disable still makes it an annoyance to stumble upon gibtonite,
but it won't round end you for using modsuits.

## Changelog

:cl:
qol: Drill module automatically disables if it's about to drill into
gibtonite
/:cl:

* Drill module automatically disables if it's about to drill into gibtonite

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [kenji-fwenshimwa-ruth/alx-low_level_programming](https://github.com/kenji-fwenshimwa-ruth/alx-low_level_programming)@[893dcf5490...](https://github.com/kenji-fwenshimwa-ruth/alx-low_level_programming/commit/893dcf549093d0fa96e3743a55fd9b5c6968b79d)
#### Tuesday 2023-09-12 03:05:50 by kenji-fwenshimwa-ruth

 A dog is the only thing on earth that loves you more than you love yourself,A dog will teach you unconditional love. If you can have that in your life, things won't be too bad,Outside of a dog, a book is a man's best friend. Inside of a dog it's too dark to read,Outside of a dog, a book is a man's best friend. Inside of a dog it's too dark to read,How many legs does a dog have if you call his tail a leg? Four. Saying that a tail is a leg doesn't make it a leg

---
## [alan-barzilay/sidon](https://github.com/alan-barzilay/sidon)@[35ce590431...](https://github.com/alan-barzilay/sidon/commit/35ce5904310c611aa67481c600f2892de3c12d6d)
#### Tuesday 2023-09-12 03:10:08 by Alan Barzilay

switch from npm to bun

bun is the cool hot new thing of the moment and really looks promissing.
Wth its version 1.0 being released I wanted to try to see if it could
decrease the build time in the CI/CD pipeline.

Honestly, the results seem inconclusive. It got the lowest build time I
found when comparing to older ci/cd builds but these builds have a
somewhat big variance, my guess is that artifact uploading time can
fluctuate a lot and the astro github actio doesnt break down how long
each step took.
At the very least, it is not slower than npm and there is the added benefit of
improving performance when building locally (this one I could note more
evident gains). With all this in mind, I'm not reverting back but I'm
also not married to bun.

A better approach for speeding up ci/cd builds could be caching the
astro output (stuff like the processed images), since locally it takes
only a few seconds to build versus the minutes in the ci/cd pipeline.
However I'm not sure if it would fit the free tier space that github
offers.

Lastly, I still use npm to install sharp because it doesnt seem to be
recognized by astro when installing it with bun. I think it is part of
bun's growing pains, since until recently it was not possible to install
sharp with bun.

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[47a3277daf...](https://github.com/vampirebat74/lobotomy-corp13/commit/47a3277daf57ea06b28eec345cb3faaa9c7ad968)
#### Tuesday 2023-09-12 04:05:22 by Mr.Heavenly

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Adds Red Shoes

Mr. Heavenly's Abnormality Jam Entry #1

Records

uncommented weapon

Finishing touches

Design rework

adds ego gift and inhands

New sprites!

uncommented sfx

insanity fix

quieter sound loop

Fixes some shit

fix linters

requested changes

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes suit check in assimilate() proc

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

fixes dismembering

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

breach is more dangerous

compiles

bug fix

fixes simple mob

bug fixes

Panic fixed!!!!

stuff

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[dd8d13d8bc...](https://github.com/dragomagol/tgstation/commit/dd8d13d8bcc6f1fbd6bcdd534a044f7d30c800d7)
#### Tuesday 2023-09-12 04:11:14 by carlarctg

Several common 'household' reagents can be used as improvised medicine treatment. Updated first aid analyzer information. (#77746)

## About The Pull Request

Several common 'household' reagents can be used as improvised medicine
treatment.

Drinking tea will help mend (non-bone) wounds over time.

Flour and corn starch may be splashed onto wounds to help dry them up,
though they'll have a negative effect on burn wounds.

Added a new reagent, saltwater, made by combining table salt with water.

Table salt and saltwater can be splashed onto wounds as well, reducing
bleeding and improving sanitization and disinfection significantly.
However, the coarse undiluted salt will irritate the wounds, reducing
clot rate and flesh healing, and both of the reagents will increase a
burn wound's infestation rate.

Altered Table Salt's recipe to just need sodium and chloride. Changed
the recipe of Pentetic Acid and Heparin to need table salt (sodium x
chloride) and thus slightly altered the total output of those reagents
(pentacid went from 5u per reaction to 4u, heparin 4u->3u)

Saline-Glucose Solution now needs 2u of saltwater and 1u of sugar,
meaning the overall recipe should be completely unchanged in practice.
Contact me on discord if any issues arise from these chemical changes!

First aid analyzers now give easy-to-understand direct information, with
the specific recommended treatments bolded in the analysis text. They
also have a 'unique' extra bit of info, telling you about improvised
ways to remedy your wound.
## Why It's Good For The Game

Wounds have a very poor amount of interaction with the rest of the game
and have not had much added to them post-merge, especially in
'improvised' ways to help Not Die to a wound while you crawl your way to
a emergency medkit or medbay. I researched info on this and found some
interesting ideas - some of them I'll have to leave for later because
this PR kept growing out of scope (Improvised bone gel, ice on wounds
which turned into wound temperature mechanics, crutches, a 'suture item'
component refactor...)

As for what this actually does to benefit the game, it allows more
dynamic wound Gameplay as people use first aid analyzers to get
information on treatment when medbay blows up, helps them stabilize by
splashing flour onto themselves before looking for some actual
treatment, helps traitors realize how they can self-treat many crippling
wounds (at risk, of course). It expands treatment options to things
beside medkits and medbay, but always does so in ways that have
downsides that make them not ideal as _treatment_, and more beneficial
as stabilizing before seeking true professional help. This thus
significantly increases the rather shallow depth of wounds as a system
to interact with.

> Several common 'household' reagents can be used as improvised medicine
treatment.

From what I could tell by looking at several sources for each
'realistic' treatment, these are indeed semi-reasonable things that are
done to wounds by some people as household treatment.

It goes without saying that you should **not do any of these things in
real life** without consulting a doctor unless your blood is also
spilling out by the gallon into the floor. All these 'realistic
treatments' have drastic downsides and are meant for the short-term
only. Except the tea.

> Drinking tea will help mend (non-bone) wounds over time.

Tea is healthy, we all know that.

> Flour and corn starch may be splashed onto wounds to help dry them up,
though they'll have a negative effect on burn wounds.

Flour and apparently starch dries wounds up but risks infection. That's
not a thing for blood wounds yet but oh well.

> Table salt and saltwater can be splashed onto wounds as well, reducing
bleeding and improving sanitization and disinfection significantly.
However, the coarse undiluted salt will irritate the wounds, reducing
clot rate and flesh healing, and both of the reagents will increase a
burn wound's infestation rate.

Salt kills bacteria via osmosis, but it also kills your own cells, and
some bacteria like salt.

> Added a new reagent, saltwater, made by combining table salt with
water.

> Altered Table Salt's recipe to just need sodium and chloride. Changed
the recipe of Pentetic Acid and Heparin to need table salt (sodium x
chloride) and thus slightly altered the total output of those reagents
(pentacid went from 5u per reaction to 4u, heparin 4u->3u)

> Saline-Glucose Solution now needs 2u of saltwater and 1u of sugar,
meaning the overall recipe should be completely unchanged in practice.
Contact me on discord if any issues arise from these chemical changes!

I wish I hadn't had to mess with reagents like this, but I needed to
because just adding mixing salt and water caused the saline glucose
recipe to basically split itself into half saltwater half glucose.

I removed the water requirement for table salt (Why did it even have
that, salt ain't wet bro?), made saline-glucose need 2u saltwater and 1u
sugar, and altered relevant recipes so they didn't also cause unwanted
table salt to react from their sodium and chloride ingredients.

A happy side-effect is that saline glucose solution is even easier to
make now as an improvised chem by mixing salt, water, and sugar, which
fits pretty perfectly (especially as a temporary blood substitute)

> First aid analyzers now give easy-to-understand direct information,
with the specific recommended treatments bolded in the analysis text.
They also have a 'unique' extra bit of info, telling you about
improvised ways to remedy your wound.

You might notice that as the wounds get more serious the text gets more
direct and concise and reluctantly hands out more and more improvised
treatment options, so that's fun. As for the improvised section itself,
it helps people be actually aware of these ways to help treat themselves
rather than delegating it to hyper-gamer knowledge.

The bolded treatment bit is pretty neat and means your eyes can
inmediately focus on what you can do to save yourself - very useful if
you have a weeping avulsion and no bandages.
## Changelog
:cl:
add: Several common 'household' reagents can be used as improvised
medicine treatment.
add: Drinking tea will help mend (non-bone) wounds over time.
add: Flour and corn starch may be splashed onto wounds to help dry them
up, though they'll have a negative effect on burn wounds.
add: Added a new reagent, saltwater, made by combining table salt with
water.
add: Table salt and saltwater can be splashed onto wounds as well,
reducing bleeding and improving sanitization and disinfection
significantly. However, the coarse undiluted salt will irritate the
wounds, reducing clot rate and flesh healing, and both of the reagents
will increase a burn wound's infestation rate.
add: Altered Table Salt's recipe to just need sodium and chloride.
Changed the recipe of Pentetic Acid and Heparin to need table salt
(sodium x chloride) and thus slightly altered the total output of those
reagents (pentacid went from 5u per reaction to 4u, heparin 4u->3u)
add: Saline-Glucose Solution now needs 2u of saltwater and 1u of sugar,
meaning the overall recipe should be completely unchanged in practice.
Contact me on discord if any issues arise from these chemical changes!
qol: First aid analyzers now give easy-to-understand direct information,
with the specific recommended treatments bolded in the analysis text.
They also have a 'unique' extra bit of info, telling you about
improvised ways to remedy your wound.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[429c59e120...](https://github.com/Offroaders123/NBTify/commit/429c59e12020c363d71c733ab2d2e1efe7cc1c56)
#### Tuesday 2023-09-12 04:16:23 by Offroaders123

Error Visibility

Realized that NBTify's internal argument type check handling works great for this! I was debating removing that in favor of just TS types instead, leaving the runtime to be honestly a bit of a wild west. That's not reliable for cases just like this though. It does bloat up the internal code a bit, which was partly why I was thinking of removing it, but it is definitely worthwhile now that I've seen it really helps with things like this. I don't have to add explicit type checks in the CLI, because the API calls in NBTify themselves type check the values for you, so it's something that can be strongly relied on :)

The only other thing I might try is to make NBTify's union types into enums maybe, and it can be something that the library can more strongly and consistently check against, since right now I'm using literal strings a lot of the time, and `instanceof` checks. I want to make those a bit less extensive and splintered across the codebase.

---
## [pepe/judge](https://github.com/pepe/judge)@[8dcbff38a4...](https://github.com/pepe/judge/commit/8dcbff38a47327ee5958a6bd4263388d9b29da03)
#### Tuesday 2023-09-12 05:56:19 by Ian Henry

use lexical over dynamic scope to link expect with enclosing test

I originally avoided this approach because of the bad error messages
if you use (expect) outside of a (test) block. But I think the simplicity is
worth it. Now instead of a friendly reminder, you will get the rather ugly:

compile error: unknown symbol EXPECT_MUST_OCCUR_WITHIN_TEST_00000U

Which is not as nice, but I think the simplification is worth it. After all,
it's not a mistake people that people are likely to make in the first place.
Especially since I am the only person using this library.

---
## [cyberitsolutions/bootstrap2020](https://github.com/cyberitsolutions/bootstrap2020)@[a2c67c6170...](https://github.com/cyberitsolutions/bootstrap2020/commit/a2c67c6170b6664f9ab2affefd0d0576f10f1aec)
#### Tuesday 2023-09-12 06:00:55 by Trent W. Buck

Fix during-build DNS resolution

08:30 <twb> TIL update-smart-drivedb in Debian 11 broke this week
08:36 <twb> OK it looks like it now needs gpg and since gpg2 needs a bunch of systemd listener bullshit, it just fails completely now
08:37 <twb> But if I add --no-verify it's working in a test unshare
08:37 <twb> But the prod error was from curl, not gpg...
08:37 <twb> 6 Could not resolve host. The given remote host could not be resolved.
08:37 <twb> Ah fuck it's DNS that broke
08:38 <twb> This means it's my fault, so never mind.
09:13 <twb> OK so the problem is pretty simple.  The build hosts now have /etc/resolv.conf -> /run/blah/systemd where they used to have -> /usr/lib/blah/systemd
09:14 <twb> Since the symlink's destination doesn't exist inside the chroot (/dev and /proc are bind-mounted in, but /run is not), DNS fails
09:14 <twb> The simple fix is to create a dummy /run/blah/systemd during the build

This is very similar to the fix I already did in Debian 12, when
I thought this was a new problem in Debian 12.

See https://github.com/cyberitsolutions/bootstrap2020/blob/twb/debian-12-main.hooks/customize50-dynamic-dns-resolv-conf.py

---
## [MJCoder15/react](https://github.com/MJCoder15/react)@[ac1a16c67e...](https://github.com/MJCoder15/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Tuesday 2023-09-12 06:56:26 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [J-Kappes/nushell](https://github.com/J-Kappes/nushell)@[a9216deaa4...](https://github.com/J-Kappes/nushell/commit/a9216deaa40d7c5c184bdb3aa1520b6b67c20bf8)
#### Tuesday 2023-09-12 07:16:40 by Darren Schroeder

allow `--login` to be used with nu's `--commands` parameter (#10253)

# Description

This PR allows the `--login`/`-l` parameter to be used with nushell's
`--commands`/`-c` parameter. When you do this, since you're invoking it
with the `-l` flag, nushell will load your env.nu, config.nu, and
login.nu, in that order. Then it will proceed to run your commands. I
think this provides a better quality of life when you want to run
scripts with your personal config files as a login shell.


### Before (these entries are from the default_env.nu)

![image](https://github.com/nushell/nushell/assets/343840/ce7adcd0-419e-485c-b7d1-f11f162e8e9e)


### After (these entries are from my personal env.nu)

![image](https://github.com/nushell/nushell/assets/343840/33bbc06b-983c-4461-8274-290e4c712506)


closes https://github.com/nushell/nushell/issues/9833

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->

# Tests + Formatting
<!--
Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used` to
check that you're using the standard code style
- `cargo test --workspace` to check that all tests pass (on Windows make
sure to [enable developer
mode](https://learn.microsoft.com/en-us/windows/apps/get-started/developer-mode-features-and-debugging))
- `cargo run -- -c "use std testing; testing run-tests --path
crates/nu-std"` to run the tests for the standard library

> **Note**
> from `nushell` you can also use the `toolkit` as follows
> ```bash
> use toolkit.nu # or use an `env_change` hook to activate it
automatically
> toolkit check pr
> ```
-->

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

---
## [neelamtanwar/Data-analysis-](https://github.com/neelamtanwar/Data-analysis-)@[d39924eb40...](https://github.com/neelamtanwar/Data-analysis-/commit/d39924eb401c16801a6914f41b33eda1c7d9200c)
#### Tuesday 2023-09-12 07:25:24 by NEELAM TANWAR

Add files via upload

In cancer studies, typical research questions include:
(1) What is the impact of certain clinical characteristics on patient’s survival? For 
example, is there any difference between the group of people who has higher blood 
sugar and those who don’t?
(2) What is the probability that an individual survives a specific period (years, 
months, days)? For example, given a set of cancer patients, we will be able to tell that 
if 300(random number) days after the diagnosis of cancer has been passed, then the
probability of that person being alive at that time will be 0.7 (random number).
(3) Are there differences in survival between groups of patients? For example, let’s 
say there are 2 groups of people diagnosed with cancer. Those 2 groups were given 2 
different kinds of treatments. Now our goal here will be to find out if there is a 
significant difference between the survival time for those 2 different groups based on 
the treatment they were given.


Conclusion
From our analysis we find that as the survival days increases the 
probability of survival decreases while the probability of a person die 
increases. We also conclude that the value of hazard function increases as 
the survival time increases. 
We also conclude that the survival probability of female is less than the 
survival probability of male , thus doctor should focus on factor that 
affects the survival of male and give medicines accordingly.
Log rank test confirms that gender of a person affects the survival days of 
the person.
From cox regression we conclude that among the various factors gender 
and Ph.ECOG value affect most on the survival of patients while age of 
patient does not affect the survival of the patients. Thus , medicines must 
be prescribed keeping this factor in mind. Also, person having higher Ph. 
ECOG value has lower survival probability. Thus, medicines must be 
prescribed as such that it lowers the Ph. ECOG value.
Also, as the survival days increase the median survival time decreases

---
## [RikerW/dNAO](https://github.com/RikerW/dNAO)@[33db2f7a6a...](https://github.com/RikerW/dNAO/commit/33db2f7a6a10383cf3257f1364d722edb1b5fa2b)
#### Tuesday 2023-09-12 10:15:23 by RikerW

more knightly style changes

minor backend stuff
- restrict_weapon skill sets a skill to be restricted, both max and current, but doesn't clear practice - so you can immediately reenhance if given back
- u_can_bimanual to check for hand & a half weapons, doesn't give u numbers just yes/no. also fixed minor inconsistency where mon/you hand & half weapons were different
- fake_skill - for the newly christened "fake skills", aka form skills that aren't ever checked. they exist so that impossibles aren't thrown if you try to check one, liek when looping over forms, but should never be used if fake_skill(form)
- roleSkill now does something - it checks if a skill is attached to a specific role. if so, that skill is granted via attrib.c level-up, and either set to expert at xp14+ or set to restricted at 13-. could be upgraded later to accept a level for each skill, but I was lazy. #scopecreep or something idk
- if a skill associated with a form is restricted, it's never treated as active

style changes

all advanced styles now use different skills, so they enhance separately (that's runic sacred eldritch)
half sword and runic style are now fake skills, so they're just trained/not trained, checked based on max skill being restricted or not.
advanced styles now unlock at knight lvl 14+. if you drop below, re-restricting the skills will disable the forms, though they won't unselect it - so they'll auto-reenable on leveling back up (intentional for QOL if fighting vampires etc. at xp14 and getting drained)
balance fix - eldritch styles now only apply on uwep. they do NOT affect otherwise. yes, no barehanded. this is for balance, cuz holy shit, 6d6 on every attack? no.
qol/balance fix - sacred style now applies on uwep not just long swords.
qol fix - messages for eldritch style, "Eldritch energies burn/freeze/shock/etc. the monnam"
nerf - half-sword loses precision damage. its just shining and bimanual now.
balance fix - great wep now applies to hand & a half weapons, if hand & a halfing them. go figure.

---
## [RikerW/dNAO](https://github.com/RikerW/dNAO)@[d878c15094...](https://github.com/RikerW/dNAO/commit/d878c15094eb4282f94a17c90ee1c7a24fd5aa28)
#### Tuesday 2023-09-12 10:18:48 by RikerW

more knightly style changes

minor backend stuff
- restrict_weapon skill sets a skill to be restricted, both max and current, but doesn't clear practice - so you can immediately reenhance if given back
- u_can_bimanual to check for hand & a half weapons, doesn't give u numbers just yes/no. also fixed minor inconsistency where mon/you hand & half weapons were different
- fake_skill - for the newly christened "fake skills", aka form skills that aren't ever checked. they exist so that impossibles aren't thrown if you try to check one, liek when looping over forms, but should never be used if fake_skill(form)
- roleSkill now does something - it checks if a skill is attached to a specific role. if so, that skill is granted via attrib.c level-up, and either set to expert at xp14+ or set to restricted at 13-. could be upgraded later to accept a level for each skill, but I was lazy. #scopecreep or something idk

style changes

all advanced styles now use different skills, so they enhance separately (that's runic sacred eldritch)
advanced styles are blocked if restricted - used for downleveling disabling them
half sword and runic style are now fake skills, so they're just trained/not trained, checked based on max skill being restricted or not.
advanced styles now unlock at knight lvl 14+. if you drop below, re-restricting the skills will disable the forms, though they won't unselect it - so they'll auto-reenable on leveling back up (intentional for QOL if fighting vampires etc. at xp14 and getting drained)
balance fix - eldritch styles now only apply on uwep. they do NOT affect otherwise. yes, no barehanded. this is for balance, cuz holy shit, 6d6 on every attack? no.
qol/balance fix - sacred style now applies on uwep not just long swords.
qol fix - messages for eldritch style, "Eldritch energies burn/freeze/shock/etc. the monnam"
nerf - half-sword loses precision damage. its just shining and bimanual now.
balance fix - great wep now applies to hand & a half weapons, if hand & a halfing them. go figure.

---
## [tanyashagova/evals](https://github.com/tanyashagova/evals)@[b93700ab49...](https://github.com/tanyashagova/evals/commit/b93700ab496bd112f89821777edc6a22d5972fb2)
#### Tuesday 2023-09-12 10:34:47 by DunedainStrider

Do math problems related to calculating dates using the Chinese Sexagenary Cycle method. 🧮 (#190)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Do math problems related to calculating dates using the Chinese
Sexagenary Cycle method

### Eval description

The Sexagenary Cycle combines 10 Heavenly Stems (Jia 甲, Yi 乙, Bing 丙,
Ding 丁, Wu 戊, Ji 己, Geng 庚, Xin 辛, Ren 壬, Gui 癸) and 12 Earthly Branches
(Zi 子, Chou 丑, Yin 寅, Mao 卯, Chen 辰, Si 巳, Wu 午, Wei 未, Shen 申, You 酉,
Xu 戌, Hai 亥) to form a 60-unit cycle. To calculate, convert the
Gregorian date to its corresponding Heavenly Stem and Earthly Branch
combination, used for marking specific years, months, and days.

### What makes this a useful eval?

The existing GPT models tend to make errors when performing calculations
related to the Sexagenary Cycle. To address this issue, we have provided
a specialized dataset aimed at improving the model's accuracy in
handling Sexagenary Cycle calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

[2023-03-16 12:46:51,594] [record.py:320] Final report: {'accuracy':
0.65}. Logged to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl
[2023-03-16 12:46:51,594] [oaieval.py:211] Final report:
[2023-03-16 12:46:51,594] [oaieval.py:213] accuracy: 0.65
[2023-03-16 12:46:51,597] [record.py:309] Logged 60 rows of events to
/tmp/evallogs/230316044112MFPWKX37_gpt-3.5-turbo_sexagenary_cycle_calculation.jsonl:
insert_time=2.463ms

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"甲戌的次日是？"}], "ideal": "乙亥"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"乙亥的次日是？"}], "ideal": "丙子"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬寅的后日是？"}], "ideal": "甲辰"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"癸卯的后日是？"}], "ideal": "乙巳"}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "Let's do a math problem
related to calculating dates using the Chinese Sexagenary Cycle
method."}, {"role": "assistant", "content": "Sure, let's do a math
problem using the Chinese Sexagenary Cycle. The Chinese Sexagenary
Cycle, or Stems and Branches, is a system used in China to count years,
months, days, and even hours. It is a 60-year cycle, consisting of 10
Heavenly Stems and 12 Earthly Branches."}, {"role": "user", "content":
"壬子的后日是？"}], "ideal": "甲寅"}
  ```
</details>

---------

Co-authored-by: dunedainstrider <dunedainstrider@mac16>

---
## [tanyashagova/evals](https://github.com/tanyashagova/evals)@[8e276ea460...](https://github.com/tanyashagova/evals/commit/8e276ea4603155ee616d5cd66aadfddcfbcae0cc)
#### Tuesday 2023-09-12 10:34:47 by steven-luabase

Eval: Probability Questions Sourced From Actuarial Exam P and University Statistics Courses (#263)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Probability Questions

### Eval description

Tests the model's ability to understand answer probability questions.
Questions are sourced from Society of Actuaries Exam P sample questions
and practice problems/exams from statistics classes at MIT, UPenn,
California State University, Durham University, University of
Connecticut, and other sources. The full list of questions and sources
(in the same order as in the `.jsonl` files) can be found in this Google
[sheet](https://docs.google.com/spreadsheets/d/1TU_4VPhIce9JtLV5gLy619WNibVjiWB-dtiwqkBtCrU/edit?usp=sharing)

### What makes this a useful eval?

Test the model's ability to understand worded probability questions,
bring in concepts such as probability distributions, and then reason
through a correct answer.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Using the `match` grading criteria, GPT3.5-turbo got an accuracy score
of `{'accuracy': 0.07}`

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A pair of fair, standard dice are rolled. What is the
probability the sum of the dice is 5"}], "ideal": ["0.1111"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "An airplane is built to be able to fly on one engine. If the
plane's two engines operate independently, and each has a 1% chance of
failing in any given four-hour flight, what is the chance the plane will
fail to complete a four-hour flight to Oklahoma due to engine
failure?"}], "ideal": ["0.0001"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "A 1-inch-diameter coin is thrown on a table covered with a
grid of lines two inches apart. What is the probability the coin lands
in a square without touching any of the lines of the grid?"}], "ideal":
["0.2500"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 50 students in a certain class, 5 speak French. Two
students of the class will be selected at random. Which of the following
is closest to the probability that neither of the students selected will
speak French?"}], "ideal": ["0.8100"]}
{"input": [{"role": "system", "content": "You are a helpful
statistician. Answer the questions with only the numerical answer
rounded to 4 decimal places. Provide no explanation."}, {"role": "user",
"content": "Of the 10 marbles in a box, 2 are green. A person will
select 2 marbles simultaneously and at random from the box. What is the
probability that neither of the marbles selected will be green?"}],
"ideal": ["0.6222"]}
  ```
</details>

---
## [tanyashagova/evals](https://github.com/tanyashagova/evals)@[33484c8341...](https://github.com/tanyashagova/evals/commit/33484c83416c30733359d5c4dcb9a61f91cab8a6)
#### Tuesday 2023-09-12 10:34:47 by emu1729

Added AIME eval (#293)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
AIME-Evaluation

### Eval description

This eval evaluates GPT on some selected AIME (American Invitational
Mathematics Examination) problems. This is a selective and prestigious
mathematical examination for high schoolers. All questions are selected
from the 2001 and 2002 AIME I and II examinations.

### What makes this a useful eval?

This evaluation combines math and logical evaluation and is designed to
be quite challenging. The model must first understand the math question
asked and then perform the math equations needed to come up with a
reasonable solution.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

Our eval was designed to include both math and logical reasoning and is
quite challenging. This is a level above the AMC10 examination.

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [X] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Find the sum of all positive
two-digit integers that are divisible by each of their
digits."}],"ideal":"630"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A fair die is rolled four
times. The probability that each of the final three rolls is at least as
large as the roll preceding it may be expressed in the form m\/n, where
m and n are relatively prime positive integers. Find m +
n"}],"ideal":"079"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A sphere is inscribed in the
tetrahedron whose vertices are A = (6, 0, 0), B = (0, 4, 0), C = (0, 0,
2), and D = (0, 0, 0).The radius of the sphere is m \/ n, where m and n
are relatively prime positive integers. Find m + n."}],"ideal":"005"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A mail carrier delivers mail
to the nineteen houses on the east side of Elm Street. The carrier
notices that no two adjacent houses ever get mail on the same day, but
that there are never more than two houses in a row that get no mail on
the same day. How many different patterns of mail delivery are
possible?"}],"ideal":"351"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"The numbers 1, 2, 3, 4, 5, 6,
7, and 8 are randomly written on the faces of a regular octahedron so
that each face contains a different number. The probability that no two
consecutive numbers, where 8 and 1 are considered to be consecutive, are
written on faces that share an edge is m\/n, where m and n are
relatively prime positive integers. Find m + n."}],"ideal":"085"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Let N be the largest positive
integer with the following property: reading from left to right, each
pair of consecutive digits of N forms a perfect square. What are the
leftmost three digits of N?"}],"ideal":"816"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Each of the 2001 students at a
high school studies either Spanish or French, and some study both. The
number who study Spanish is between 80 percent and 85 percent of the
school population, and the number who study French is between 30 percent
and 40 percent. Let m be the smallest number of students who could study
both languages, and let M be the largest number of students who could
study both languages. Find M-m."}],"ideal":"298"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"A set of positive numbers has
the 'triangle-property' if it has three distinct elements that are the
lengths of the sides of a triangle whose area is positive. Consider sets
{4, 5, 6, ..., n} of consecutive positive integers, all of whose
ten-element subsets have the triangle property. What is the largest
possible value of n?"}],"ideal":"253"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Each unit square of a 3-by-3
unit-square grid is to be colored either blue or red. For each square,
either color is equally likely to be used. The probability of obtaining
a grid that does not have a 2-by-2 red square is m\/n, where m and n are
relatively prime positive integers. Find m + n."}],"ideal":"929"}
{"input":[{"role":"system","content":"All answers are integers ranging
from 000 to 999, inclusive. Please format your answer as a string with
three digits."},{"role":"user","content":"Given that x and y are both
integers between 100 and 999, inclusive; y is the number formed by
reversing the digits of x; and z=|x-y|. How many distinct values of z
are possible?"}],"ideal":"009"}

  ```
</details>

---------

Co-authored-by: Emily Mu <emilymu@30-10-85.wireless.csail.mit.edu>
Co-authored-by: Emily Mu <emilymu@30-10-24.wireless.csail.mit.edu>

---
## [tanyashagova/evals](https://github.com/tanyashagova/evals)@[aa71d43273...](https://github.com/tanyashagova/evals/commit/aa71d4327328933a463e972d662e6988234d0ef7)
#### Tuesday 2023-09-12 10:34:47 by Andrew Kondrich

Fix get_answer (#972)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [tanyashagova/evals](https://github.com/tanyashagova/evals)@[8f8632ec55...](https://github.com/tanyashagova/evals/commit/8f8632ec55ee1f9704fe34225e1bce0cd999a8b1)
#### Tuesday 2023-09-12 10:34:47 by Oshan Upreti

Nepali song singer recognition (#892)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
Nepali Song Singer

### Eval description

It tests the ability to understand Nepali language from given English
Transliteration phrase which is provided by user as a song title, and
checks the singer/band of the song. This eval has the accuracy of zero.
And, I still created this eval PR because I get the wrong answers every
time I ask, and I don't think that should be the case. It might not be
something that needs to be done immediately, but in a near future you
would expect your AI to answer it correctly.

### What makes this a useful eval?

If it can do for any English songs in the database, it should be able to
do for other languages as well. This is just a pattern I found it in my
mother tongue, but there might be different other languages where this
is happening as well, and it can be other things as well not just the
song title recognition.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Sayad Timro Bato Ma"}], "ideal":
"Raju Lama"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Timi Lai Dekhera"}], "ideal":
"Raju Lama"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Aaja maan udhera bhagchha"}],
"ideal": "Udit Narayan"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Kaha Hola Ghar Bara"}], "ideal":
"Karma"}
{"input": [{"role": "system", "content": "A user will give you a English
transliteration phrase of Nepali song. Give the name of the singer or
band."}, {"role": "user", "content": "Khaseka Tara"}], "ideal":
"Albatross"}
  ```
</details>

---
## [ervinpopescu/qtile](https://github.com/ervinpopescu/qtile)@[aa380cf4a0...](https://github.com/ervinpopescu/qtile/commit/aa380cf4a0e7c945be237058d43a4d2643844ec9)
#### Tuesday 2023-09-12 10:49:34 by Tycho Andersen

pyproject: more (hopefully the last?) porting

Here's the last bits of what I think we should port to pyproject.toml
before releasing.

* I dropped the "Alpha" Classifier, we're beyond alpha, I've been using
  qtile as a daily driver for nearly 15 years
* I dropped the point-release python version Classifiers (i.e. 3.8, 3.9,
  etc.). These are not that interesting and a pain to maintain.
* I dropped Sean Vig as the listed maintainer. We list all the maintainers
  at the bottom of the readme, which ends up in the long_description. No
  reason to maintain two maintainer lists.
* I dropped Aldo as the Author:. There are lots of authors of qtile, this
  info is available from the git log.

My hope is that this will not give a syntax error when uploading source
now during the release workflow. I've inspected the output with:

    python3 setup.py bdist_wheel --keep-temp && cat build/bdist.linux-x86_64/wheel/qtile-*.dist-info/METADATA

and it looks pretty similar to the METADATA from the current release.

Signed-off-by: Tycho Andersen <tycho@tycho.pizza>

---
## [KeerthanaHaridas/facebook_login_page](https://github.com/KeerthanaHaridas/facebook_login_page)@[04979b9ea7...](https://github.com/KeerthanaHaridas/facebook_login_page/commit/04979b9ea7fea3d659353317cb15341533fb9abf)
#### Tuesday 2023-09-12 11:08:18 by KeerthanaHaridas

Add files via upload

Designing a front-end Facebook login page using HTML and CSS is an exciting project that allows you to practice your web development skills. This endeavor involves creating an interface where users can securely input their login credentials. HTML forms the structure, defining elements like input fields, labels, and buttons, while CSS styles these elements, giving the page its visual appeal.

A typical Facebook login page includes fields for the username or email and the password, as well as a 'Login' button. Incorporating key design elements, such as the Facebook logo and color scheme, helps establish trust and familiarity with users.

In this project, meticulous attention to layout, color choices, and typography is paramount for a polished and user-friendly design. Employing responsive design techniques ensures the page adapts seamlessly to various screen sizes, providing a consistent experience across devices.

Remember, the objective is not only functionality but also an aesthetically pleasing and intuitive interface that encourages user interaction. Leveraging HTML and CSS, you have the capability to craft a visually appealing and functional Facebook login page that users will find both familiar and easy to navigate. This project offers a valuable opportunity to refine your front-end development skills and create a polished, professional-looking login page.

---
## [rsalmaso/neovim](https://github.com/rsalmaso/neovim)@[5970157e1d...](https://github.com/rsalmaso/neovim/commit/5970157e1d22fd5e05ae5d3bd949f807fb7a744c)
#### Tuesday 2023-09-12 11:54:59 by bfredl

refactor(map): enhanced implementation, Clean Code™, etc etc

This involves two redesigns of the map.c implementations:

1. Change of macro style and code organization

The old khash.h and map.c implementation used huge #define blocks with a
lot of backslash line continuations.

This instead uses the "implementation file" .c.h pattern. Such a file is
meant to be included multiple times, with different macros set prior to
inclusion as parameters. we already use this pattern e.g. for
eval/typval_encode.c.h to implement different typval encoders reusing a
similar structure.

We can structure this code into two parts. one that only depends on key
type and is enough to implement sets, and one which depends on both key
and value to implement maps (as a wrapper around sets, with an added
value[] array)

2. Separate the main hash buckets from the key / value arrays

Change the hack buckets to only contain an index into separate key /
value arrays
This is a common pattern in modern, state of the art hashmap
implementations. Even though this leads to one more allocated array, it
is this often is a net reduction of memory consumption. Consider
key+value consuming at least 12 bytes per pair. On average, we will have
twice as many buckets per item.
Thus old implementation:

  2*12 = 24 bytes per item

New implementation

  1*12 + 2*4 = 20 bytes per item

And the difference gets bigger with larger items.
One might think we have pulled a fast one here, as wouldn't the average size of
the new key/value arrays be 1.5 slots per items due to amortized grows?
But remember, these arrays are fully dense, and thus the accessed memory,
measured in _cache lines_, the unit which actually matters, will be the
fully used memory but just rounded up to the nearest cache line
boundary.

This has some other interesting properties, such as an insert-only
set/map will be fully ordered by insert only. Preserving this ordering
in face of deletions is more tricky tho. As we currently don't use
ordered maps, the "delete" operation maintains compactness of the item
arrays in the simplest way by breaking the ordering. It would be
possible to implement an order-preserving delete although at some cost,
like allowing the items array to become non-dense until the next rehash.

Finally, in face of these two major changes, all code used in khash.h
has been integrated into map.c and friends. Given the heavy edits it
makes no sense to "layer" the code into a vendored and a wrapper part.
Rather, the layered cake follows the specialization depth: code shared
for all maps, code specialized to a key type (and its equivalence
relation), and finally code specialized to value+key type.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ac18420676...](https://github.com/tgstation/tgstation/commit/ac18420676c9daaa94910a1a1f4a2e2d74f0d05d)
#### Tuesday 2023-09-12 12:02:12 by Hatterhat

John Splintercell: a gun that is only good for shooting out lights (#78128)

## About The Pull Request
adds the SC/FISHER lightbreaker self-charging energy pistol, which does
0 damage. As a joke.

![image](https://github.com/tgstation/tgstation/assets/31829017/84603fcd-dbc3-4857-a657-98c4bd34e881)


https://github.com/tgstation/tgstation/assets/31829017/97572baa-7421-4800-a60e-2db03f4adc6d

<details><summary>actual details, in case the video wasn't good
enough:</summary>

unless you shoot at light fixtures,

![image](https://github.com/tgstation/tgstation/assets/31829017/54092fbf-cbf6-4750-b2b8-37d643efba2a)
floodlights,

![image](https://github.com/tgstation/tgstation/assets/31829017/90b19560-fa25-471b-9f6f-3147c33e5c56)
or people with flashlights/seclites (even on helmets or guns) (it still
does 0 damage, it just turns off their lights. not permanently)

![image](https://github.com/tgstation/tgstation/assets/31829017/1a83c6f9-8fff-4035-aeeb-515319a3dd40)
it also works on crusher lights. and cyborg headlights. i don't have a
screenshot for it.
doesn't work on flares though.

also it can shoot past machines and lockers

![image](https://github.com/tgstation/tgstation/assets/31829017/8fb0a213-8e4a-42cc-9daa-eae5faf6ee77)
</details>
(also adds a variable for deciding how loud a dry fire sound is, in case
you want to make your gun's empty sound be less loud.)

## Why It's Good For The Game

Adds a silly little tool for silly little men who either really hate
lightbulbs or want to recreate the experience of being John
Splintercell, the lightbulb-assasinating secret agent from Fork Echelon.

## Changelog

:cl:
add: The SC/FISHER disruptor pistol, a very compact, permanently
silenced energy gun, is now stocked in Nanotrasen-accessible black
markets with a price generally somewhere between 400 and 800 credits.
Aspiring users are warned that it's really bad for trying to actually
kill people. Caveat emptor.
add: Guns now have a dry_fire_sound_volume variable, allowing for guns
to be less loud when trying to fire while empty.
fix: Closets and crates now properly count as structures for pass flags
again.
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [dcantrell/.dotfiles](https://github.com/dcantrell/.dotfiles)@[c0ac6e686f...](https://github.com/dcantrell/.dotfiles/commit/c0ac6e686f6ddb7253c592a779c7ccc2e0cd6d1a)
#### Tuesday 2023-09-12 13:11:39 by David Cantrell

Remove mutt and mbsync configuration files.

Well I did it.  I moved to Thunderbird after making zero progress ever
making modern day email remotely usable in mutt.  The problem is I
need to be able to both read HTML email and make use of links in those
messages.  That has just never worked for shit in mutt.  The only
thing you can do is load the message in an actual graphical browser,
which leads me to wonder what the hell the point is of mutt if I just
have to use Firefox to read all email.

I've moved back to Thunderbird as I have done in the past which is to
move back and forth between mutt and Thunderbird.  Thunderbird works
well for locally archiving email.  It also handles multiple accounts
in a clean way.  It also supports chat systems, which I have made use
of for Matrix in Fedora since we have moved there from IRC.

Will this solve all of my email problems?  Probably not, but so far it
is easier to deal with email now since everyone sends HTML email with
images and links.

---
## [farisfaikar/learn-tailwindcss](https://github.com/farisfaikar/learn-tailwindcss)@[70fd2a5a65...](https://github.com/farisfaikar/learn-tailwindcss/commit/70fd2a5a653efe11c5715e51f53d3a7c2fa0f623)
#### Tuesday 2023-09-12 13:28:22 by farisfaikar

style: actually fixes styling using prettier
- maxWidth is set to 1000 because fuck you that's why. Also it's cleaner imo

---
## [peterprototypes/zola](https://github.com/peterprototypes/zola)@[b5a90dba5d...](https://github.com/peterprototypes/zola/commit/b5a90dba5d12ea6760c3aa18fec40f8af4d7cbc7)
#### Tuesday 2023-09-12 13:49:38 by sinofp

Add support for lazy loading images (#2211)

* Add optional decoding="async" loading="lazy" for img

In theory, they can make the page load faster and show content faster.

There’s one problem: CommonMark allows arbitrary inline elements in alt text.
If I want to get the correct alt text, I need to match every inline event.

I think most people will only use plain text, so I only match Event::Text.

* Add very basic test for img

This is the reason why we should use plain text when lazy_async_image is enabled.

* Explain lazy_async_image in documentation

* Add test with empty alt and special characters

I totaly forgot one can leave the alt text empty.
I thought I need to eliminate the alt attribute in that case,
but actually empty alt text is better than not having an alt attribute at all:
https://www.w3.org/TR/WCAG20-TECHS/H67.html
https://www.boia.org/blog/images-that-dont-need-alternative-text-still-need-alt-attributes
Thus I will leave the empty alt text.

Another test is added to ensure alt text is properly escaped.
I will remove the redundant escaping code after this commit.

* Remove manually escaping alt text

After removing the if-else inside the arm of Event::Text(text),
the alt text is still escaped.
Indeed they are redundant.

* Use insta for snapshot testing

`cargo insta review` looks cool!

I wanted to dedup the cases variable,
but my Rust skill is not good enough to declare a global vector.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[5046a7d3ae...](https://github.com/tgstation/tgstation/commit/5046a7d3ae845198e98ff3bc22c31495585e560c)
#### Tuesday 2023-09-12 13:55:17 by Fikou

decks of cards no longer have their own wielded var (#78260)

## About The Pull Request
we have the trait for that

## Why It's Good For The Game
Throughout UNDERTALE, we get treated to three story sequences (4 if you
include flowey's fakeout but that's not important). The first is the
intro story, telling the tale of humans and monsters, which shortly
thereafter leads into 201X, and Chara (Toriel's house has “An old
calendar from 201X.”) falling into the underground.

The second is the waterfall flashback, its contents taking place
immediately after the intro segment, as a voice (Asriel) finds the
fallen child.

And finally, the third takes place in the True Pacifist final boss.
We'll get to it in due course, and it will have its own section, but
let's address the first two. Regarding the intro, the first thought one
might have is that simply, while narratively relevant, is not a diegetic
presentation. However, We know that everything after the “201X” frame is
Chara's memory (from an outside perspective, that is,) and we also know
that UNDERTALE LOVES bringing the non-diegetic, the mechanical, the
game, INTO the narrative. Saving, RPG Stats, hell, even the
NarratorChara. Surely the intro can be as well? On top of this, what
does the intro do for the player, as the player? Well, aside from
setting the tone, the intro gives us some setting backstory. It's all
important context, and it certainly helps… but it being in the intro
sequence is not that important; It's all presented throughout the game
via diegetic signs, books, and expositional tortoise war heroes/angry
fish guardswomen. The second half is how Chara fell to the underground,
and while also setting tone and informing the player how their character
arrived. It also creates the false impression for the player that their
character is Frisk, feeding into UNDERTALE's meta narrative; “You are
not your character, and their happy ending is not yours.” If we weren't
playing Chara, this would have no narrative impact. The story beat fails
to land by showing us someone elses' character. But, sure. This could be
a purely non-diegetic intro sequence. Simply put, The 201X portion of
the intro sequence does not make sense from a diegetic or a storytelling
perspective unless we play as Chara.

Flashback number two is explicitly a canonical, diegetic flashback. It
occurs when Frisk escapes Undyne by falling down a massive pit… again.
This time, they land in the garbage zone, black out, and have a
flashback sequence of the first time Asriel found Chara. While serving
the main narrative by setting up Asriel as a character, furthering the
final twist of the meta narrative's pacifist route, and neatly
transitioning between overworld areas, it's also very explicitly
diegetic and cannot be dismissed as an intro sequence. With this in
mind, one question is raised. Why do we see this flashback? If the
player character is Frisk, this makes little sense, why would we see
someone else's flashback and not our own? Same thing applies for a Third
Entity, but even more abstract and illogical. What even are we? Sure,
you could say Chara is somehow attached to us/Frisk and that somehow we
get a flashback from Chara who is somehow knocked unconscious by Frisk
also being knocked unconscious. I used the word somehow three times.
That's not good storytelling. A simpler answer, at least in my view, is
that We Are Chara. When Frisk is knocked unconscious, we, being
ostensibly linked to them as a Spirit/Ghost/Reincarnation/Possessing
Dead Frisk/Demon/Insert fan-theory here/SOUL Fragment, have our only
connection to the world temporarily disabled, rendering us effectively
unconscious and prompting a flashback. Nothing weird with multiple
entities or memory sharing. The waterfall flashback is simply our
memory. Simple. The simplest answers are usually the correct ones.

<details>
<summary>DO NOT RESEARCH</summary>
The third sequence is a connection/extension of the first two, displayed
when we SAVE “Someone Else” during the true pacifist battle with Asriel.
To refresh everyone, here is the direct quotes, taken from the Wiki:


[SAVE]: Someone Else
Strangely, as your friends remembered you... Something else began
resonating within the SOUL, stronger and stronger. It seems that there's
still one last person that needs to be saved. But who...? ... Suddenly,
you realize. You reach out and call their name.
Asriel: “Huh? What are you doing...?”
s
It's at this point that the sequence plays. There's no narration, but we
see the sequence of interactions between Asriel and Chara. There are no
panels (except for the first) that don't contain the both of them.
Following this, we get:

You feel your friends' SOULs resonating within ASRIEL! [This is the
generic flavour text for saving all 6, before “Someone Else”, and
appears at the asterisk above as well]
[SAVE]: Asriel Dreemurr
Asriel:
> “Wh... what did you do...?”
“What's this feeling…? What's happening to me?”
Etc. etc. let me win…
During my first and consecutive playthroughs of UNDERTALE, I came to the
conclusion that Asriel's soul still “Had Some Chara In It.” Saving
“Someone Else” was saving Chara, and then you save Asriel Dreemurr after
the story sequence.

This interpretation no longer feels particularly potent to me, but in
the spirit of completeness I'll address it alongside the more reasonable
“You just save Asriel.” Assuming for a moment though, that we do “Save
Chara”, it's not unreasonable to assume that some of Chara's ‘essence'
(or whatever) was merged with Asriel's and by SAVING them, we're SAVING
the part of them that's inside Asriel.

But I don't like that theory.

Let's talk about SAVING Asriel for a moment.

What is the motivation for doing that? Why would we, in universe, wish
to SAVE him, something that the narration explicitly prompts us to do?
He tried and probably succeeded to kill us, at least once, he wants to
reset the entire timeline, he wants to erase all our friendships, all
our progress.

So, why? Well, it's simple. He's our brother. And we know better than
anyone that he's worth saving. And at the very least, there's something
about Frisk (who appears to have absolutely no personality) that reminds
him of Chara, of us. This is, by his own admission, weird;

Asriel:
“Frisk… You really ARE different from Chara. In fact, though you have
similar, uh, fashion choices… I don't know why I ever acted as if you
were the same person.”

To summarise.

The player SAVING Asriel Dreemurr works best if they are Chara, it
becomes Chara encouraging Frisk to SAVE Asriel too.

Asriel recognises Frisk as Chara throughout the True Pacifist battle
(And Beyond), despite his own admission that this is basically
unfounded. Something is causing this recognition.

In Alphys' true lab, there lies a dusty TV and a stack of VHSes. On
them, lie some of the last words Chara had ever heard from their father.

[Asgore] Chara! You have to stay determined! You can't give up... You
are the future of humans and monsters...

These tapes are not the first time they are heard. Sleeping in Toriel's
guest bed, we dream about them. Suffering a fatal injury, they echo in
our ears. Watching the tape is yet another reveal. It's the chilling
truth that in fact, the words we (if we die a lot) are so familiar with,
are in fact the words we hear on our deathbed.

Storytelling-wise, this reveal; like all the others, fails if we do not
play as Chara.

Aside from Asriel's dialogue, Chara's genocide Narration, and the coffin
in Asgore's basement, this is the only time we hear Chara's name. That
and, this following exchange.

[Flowey]
Hi.
…
Monsters have returned to the surface
Peace and prosperity will rule across the land.
…
Well.
There is one last thing.
…
One being with the power to erase EVERYTHING…
…
I'm talking about YOU.
…
So, please.
Just let them go.
Let Frisk be happy.
…
Well, that's all.
See you later…
Chara.
This, I think, is pretty explicitly definitive. Flowey comes to you. To
us. Tells us to take a deep breath and leave the happy ending intact,
then bids us farewell by our own name.

Regardless of anything else, this definitively proves Chara is the
entity with the power to reset everything by the end of True Pacifist
(Which is a power we have). Flowey positively identifies us as “Chara”,
despite his mistake we discussed in 3C. He's not talking to Frisk,
because he refers to them in the third person.

He is talking to Us. Chara.

I don't want to discuss Flowey's use of “Chara” in Genocide all that
much, because the counter-argument is blindingly simple.

“By the time Flowey first says that name, Chara has overtaken Frisk by
feeding on the power we create for them.”

Of course, under PlayerChara, Flowey's lines still make sense, and
arguably more.

Implications
At this point, I believe the evidence is sufficient to support the
theory. With this in mind, I want to discuss the implications this has
on the narrative and meta-narrative. This is where all those funny
glossary terms come into play.

The pacifist route in UNDERTALE, as discussed above, is textually quite
simple when accepting PlayerChara. The meta-text is also relatively
simple. Meta textually, the Pacifist Route is a dissection of the
suspension of disbelief, examining how we emotionally place ourselves
within fictional worlds, and are often-times torn away from those worlds
as the game comes to an end, left wanting the true emotional connection,
wanting a happy ending that cannot be good enough for us because we're
real and it's not. The reflection of this meta narrative in the textual
narrative, quite naturally flows. We, Chara, want a happy ending. But we
can't have it, it's not our happy ending. We're gone. We've been gone a
long time. Frisk's happy ending can't be good enough for us, because we
won't be around to see it. So, we're left with a choice.

To let Frisk live happily? To accept an ending that might leave us
emotionally wanting, yet preserves our emotional journey?

To reset? To refuse an ending and satiate our emotional emptiness, yet
destroy that very emotional journey we took in the process?

The choice is the same. There is practically no separation between the
diegetic and the meta.

“Can a happy ending be good enough for you?” This question applies to
us, as the real world player running UNDERTALE.exe on our computer, and
us, Chara, the long deceased human who can do little but watch as Frisk
lives the life they wish they still had, or can destroy everything for a
hollow mimicry of that very life.

This message, however, breaks down under one specific circumstance.
Where we force a Third Entity into the mix. This one decision fractures
the cohesion and creates a meta-textually dissonant mess. Now, all of a
sudden, “Can a happy ending be good enough for you?” no longer runs
parallel through both narratives. There is no reason for the Player
Entity to wish to remain, the happy ending should automatically be good
enough because it's the happy ending. Meanwhile, Chara, despite being an
inextricable representation of “A happy ending I can't achieve,” gets
absolutely nothing to do with this meta-narrative because they're just…
not you.

“we are mario in Super Mario 64, but when he says "Thank you so much for
playing my game!" that doesn't mean we aren't still playing as mario” -
PopitTart

This is where things get weird. See, in the Genocide route.. Well, we
see Chara. On Screen. Talk to us.

Now, it can easily be argued that this completely shatters the theory,
but I would disagree. I'm going to endeavour to present a textual
explanation (or two) for this. But first, I want to dissect the
meta-text here.

Now, I'm sure the idea that “The Genocide Route's Meta-Narratve is
Fading Emotional Investment and the way emotional connection with video
games can lead to the very sabotage of that emotional connection” is not
revolutionary. However, what's conspicuously absent from all of the
third entity theorising is the way that this meta-text is mirrored in
the textual narrative.

Once satisfied with a game, having extracted all lines of dialogue and
stat boosts, once reaching all endings, a user will close the game down.
And at some point, perhaps to make room for a new game or perhaps on a
new device, will leave the game uninstalled, either deliberately, or
simply as a consequence of time.

Textually, what happens in the Genocide ending?
Now we have reached the absolute.
There is nothing left for us here.
Let us erase this pointless world, and move on to the next.

The world is destroyed. So much is left unanswered here.
Who is Chara talking to?
Where did Frisk go?
How do they have this much power?
Why would they want this?
If we ‘corrupted' them, what the hell does that even mean?
What is Chara?
For now, let's talk about who Chara is talking to.

The simplest answer is “Perspective switch.” Suddenly, we're not Chara
anymore, now we are Frisk. This meets all the dialogue options and even
vaguely mirrors the meta-text. It also manages to avoid bringing a third
entity along and so is automatically better! But, I find myself still
not fully enjoying this idea.

Remember what I said about Occam's Razor?

I think there's another option. One that doesn't involve three entities,
or even two entities, just Chara. One that mirrors the meta-text to a
degree only Toby Fox could pull off. It's a weird one, and I don't fault
you if you don't get it on your first read, but bear with me here,
because things are about to get

A little
Fucking
Abstract

Let's discard any and all pre-concieved notions of anything and hold one
singular truth above all else. “Chara Is The Player.” What does this
mean for this cutscene?

Well… it means the player is talking to…

THe player?

It also neatly answers the question of motive, so let's throw that out
the skeleton-shaped hole in the window for now.

If the player is talking to the player, this frames Chara's words in a
whole new light.

Every time a number increases, that feeling… That's me. “Chara.”

This line becomes explicitly literal. The Chara on-screen is literally
the player's feeling of satisfaction watching stat increases. But this
is all meta-textual, right? What does this mean for the textual
narrative?

Here's the thing. It can't mean anything, yet means everything.

There is no way to reconcile the fact that a Textually Real character is
directly talking about what the player feels when playing a game to
completion. The barrier between Meta and Textual no longer exists. It
can't. Not here. And with this revelation, everything begins to make
sense.

Your power awakened me from death.

Our power. Our desire to complete UNDERTALE awakens Chara from death.
They become startlingly real. We imbue this fictional character with the
real world desire to consume fiction, destroying enemies and worlds as
we go, increasing our power and our stats. Video Game Accomplishments.
And UNDERTALE has just finished being consumed.

My “human soul”... My “determination”... They were not mine, but YOURS.

Chara, the textual player, acknowledges the meta-textual player's
control over the game world. A control that we surrendered. By engaging
in UNDERTALE in a fully immersed way, we have fed the Diegetic character
that is our player character, Chara. This has continued until we haul
ourself out of the Internal Mode and into the External Mode, revoking
our immersion to make the consumption of content easier, to distance
ourself from the killing.

Raising our LV.

The more we distance ourselves, the less real UNDERTALE's world appears
to us. Once it's done, we're ready to erase this pointless world and
move onto the next. There's just one problem. UNDERTALE knows about us.
It knows we exist and it will abuse that to convey meaning. By revoking
our immersion in UNDERTALE, we end up shattering the barrier between
Meta and Textual, and this occurs because revoking our immersion is a
diegetic decision. Without this barrier, WE, as a character, gain
control of UNDERTALE and use this external mode control to

Erase the world. To uninstall.


This code doesn't actually work, of course. That was pretty obvious by
the fact that it didn't delete your game. But still, this exists in the
code that makes the game window shake when Chara attacks it. This is,
quite literally, intent for Chara to delete UNDERTALE. If you didn't
think Chara was capable of uninstalling your game before, you should
now.

Who is chara talking to?

Us.
How do hey have this much power?

We gave it to them. We Are them, and we deleted UNDERTALE when we were
done with it.
Why would they want this?

We wanted to move onto a new game.
What is Chara?

Us. ( I'll come back to this.)
But wait! What about soulless pacifist?
Well, at that point, you've surrendered Frisk's SOUL to Chara, as in,
you the real player has revoked your emotional attachment to UNDERTALE
and accepted that Chara can have control over the game. You've revoked
your immersion AS Chara, you no longer see yourself a Chara and as such
Chara becomes their own being. You've surrendered, basically. But they
let you play through it. Because why not. You might get attached again,
but that's fine. All that means is that the happy ending that was once
Frisk's, that you, the player, and you, Chara, both once lamented not
being able to live, has now been surrendered to Chara. A warped,
completionist, Chara.

You don't get your happy ending. But Chara does.

You don't even get the solace of knowing someone gets their happy
ending. Because Chara gets it.

Frankly, outside of being “The Player”, I don't think the exact nature
of “Chara” is that crucial. My personal thought is that they're a SOUL
fragment, absorbed by Frisk when they fell on Chara's grave (Frisk could
absorb a human SOUL fragment because said fragment was part monster
SOUL). This fragment gives Frisk the final edge of determination needed
to SAVE.

But, ultimately, that's little more than a fanfiction. And frankly, I
think that's okay. Not everything needs to be impenetrable, as long as
there's enough there to build a stable foundation.

I'd also like to address the nature of SAVING quickly, specifically the
normal version, not the Asriel fight version. People have asked “Why do
we save if it's Frisk's SOUL.” There could be many reasons. Frisk might
just defer control to us. Because we're pushing Frisk over that
Determination limit, we might be privileged to have that control.
</details>

## Changelog

not player visible

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[06e7270008...](https://github.com/Jacquerel/orbstation/commit/06e7270008d4b49a7e73fd088135822a9ec76891)
#### Tuesday 2023-09-12 14:14:00 by GuillaumePrata

Funny clown internals (#77963)

# About The Pull Request
This PR changes the internals that spawn inside the clown's survival box
for a new one with a rainbow sprite, higher O2 volume (same as the engi
ones) and a secondary gas on top of O2 to make things more interesting
for the clowns.
The gas options are:
BZ, which just adds hallucinations for the clown, without the brain
damage effect as it is in low percentages.
N2O will make the clown giggle and laugh, without the sleep.
Helium will give the clown a "funny voice".

These tanks are also added to the mail list of clown fans and the clown
costume crate at cargo.

And codersprites, I can polish them later if people think it is pixel
soup, I'm not happy with them that much, but making this looks good
might be above my paygrade...
<details><summary>Pics here</summary>
<p>


![clown_internals](https://github.com/tgstation/tgstation/assets/55374212/f5eda877-a01a-4dfa-b481-7d406c4fb768)

![in game clown
internals](https://github.com/tgstation/tgstation/assets/55374212/342285ae-919b-49ab-a97e-cdf25a975f83)


</p>
</details>

## Why It's Good For The Game
The main goal I have with this is to add more uses for Atmos Content to
other players in a flavorful way.
Atmos is not something the crew interacts in a positive way often and I
want to change that.

These tanks are something quite minor but flavorful IMO, also will make
people know Helium fucking exists...

The tanks *shouldn't* change much of the clown's round in a negative
way, and the default O2 internals are in every hallway's locker so even
if they don't want to deal with the hallucinations it is not a big deal
to dodge them.
## Changelog
:cl: Guillaume Prata
add: New funny internals for the clowns to spawn with. They come with O2
and a secondary gas between 3 options: BZ, Helium and N2O. Talk with a
"different tone" with Helium, giggle and laugh "uncontrollably" while
under the minor effects of N2O or have "fun" hallucinations while under
the minor effects of BZ.
balance: To not cut on how long the clown's O2 internals last due to the
mixed gases, the funny internals have 50% more gas volume, same as
engineers' internals.
/:cl:

---------

Co-authored-by: CRITAWAKETS <sebastienracicot@hotmail.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [gopi263preethi/Data-analyticis](https://github.com/gopi263preethi/Data-analyticis)@[b22fbbf1f4...](https://github.com/gopi263preethi/Data-analyticis/commit/b22fbbf1f43b6a90b3054ac6b1fdbf4535dd4310)
#### Tuesday 2023-09-12 15:00:37 by gopi263preethi

Add files via upload

Here i have analyzed  sleep_health_and_lifestyle.csv file from the kaggle dataset and my findings are is as follows;
From this data set we can conclude that people who are aged between 40 to 50 , and especially Salesrepresentatives,salespersons
Scientists are experiencing Higher Stress Levels and their quality of sleep is also impaired. And the occuapants which mentioned above are experiencing Sleep Disorders like Sleep Apnea,Insomania.As we have examined their Blood Pressure and Heart Rate, these 2 parameters are highly infuential by stress levels i.e as the stress levels increases, Heart Rate increases, as heart rate increases Blood Pressure increases. so Stress levels are not only impacting Quality of Sleep but also impairing healthy parameters such as B.P and Heartrate. 
Note:
Sales Representatives,sales persons,Scientists,Doctors are need to balance their stress levels by incorporating meditation,
balanced food,exercise and social life. So that their life quality is more joyful and they can achieve highest heights.
And they experience disease free life

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[4b8de7b79f...](https://github.com/Pickle-Coding/tgstation/commit/4b8de7b79f0a343dc587d0d17eb9361ecc7103c1)
#### Tuesday 2023-09-12 15:43:06 by san7890

Refactors the `notransform` variable into a trait. (#78146)

## About The Pull Request

Hey there,

There were more than a few times (like in cinematic code) where we might
need to accurately know the source of what's adding this trait (or have
multiple sources for the whole 'we don't want this mob to do shit while
we transform this mob'), so in order to rectify this potential issue,
let's refactor it into a trait.

## Why It's Good For The Game

Some code already declared that there might be issues with this being a
boolean var (with no way of knowing _why_ we don't want this mob to not
transform (or not do anything idk). Let's remove those comments and any
future doubt in those instances with the trait macros. Also, stuff like
`TRAIT_IMMOBILIZED` which does a similar thing in many contexts was
already a trait that was regularly added in conjunction with flipping
the variable, so we're able to flatten all that stuff into
`add_traits()` and `remove_traits()` now. nice

I also cleaned up quite a bit of code as I saw it, let me know if it
should be split out but I guarantee that if I didn't do it- no one will
for the next two years.

## Changelog

:cl:
refactor: If you transform into another mob and notice bugs with
interacting with the game world, please create a bug report as this
framework was recently refactored.
/:cl:

Probably fucked up somewhere, lmk

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [ajichand2009/git](https://github.com/ajichand2009/git)@[8f23432b38...](https://github.com/ajichand2009/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Tuesday 2023-09-12 15:45:27 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>
Signed-off-by: Pratyush Yadav <me@yadavpratyush.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[1552857ff4...](https://github.com/tgstation/tgstation/commit/1552857ff44a8b481736eda843c5131ad4b761ab)
#### Tuesday 2023-09-12 16:54:42 by JupiterJaeden

Balance: Removes anti-drop implants for nukies (#78275)

## About The Pull Request

Removes anti-drop implants being available in nukie implants. Also
rebalances the cybernetic implants bundle to cost 20 TC (value of 24 TC)
since anti-drop has been removed from it.

## Why It's Good For The Game

This is one of the rare few nerf PRs where I was not the one who got
KILLED by the broken OP shit but rather the one using it. I recently
played a nukie round (after hearing that anti-drop had been added) where
I took modsuit shield, dsword, and anti-drop. I got separated from my
team and then proceeded to solo murderbone half the fucking station,
resist MULTIPLE disarms that would have otherwise been successful, get
the disk alone, and nuke. I only had to stop to heal _once_ and honestly
I probably would have been fine if I didn't.

Anti-drop dsword is _insanely_ powerful. Shielded dsword nukies were
already strong enough but were at least somewhat balanced insofar as
there were several ways you could still reliably disarm them and
therefore open them up to more attacks. But now (after
https://github.com/tgstation/tgstation/pull/77330 which added the
anti-drop implants to nukie uplink) you can have shielded anti-drop
dsword nukies. Add stims and some explosives to deal with any static
fortifications the crew might make (like firelock crush relays), and
with a semi-robust player you essentially have a murderbone machine who
can't be killed by any regularly accessible crew counters short of point
blank suicide bombing. We should not have a default nukie loadout that
can only be reliably, regularly countered by a fucking bomb. Especially
since the crew's main easily accessible ballistic is now being nerfed as
well. (https://github.com/tgstation/tgstation/pull/78235)

EDIT: I'd also like to point out that we already don't allow hulks to
use dswords for many of the same reasons.

## Changelog

:cl:
balance: removed anti-drop implants from the nuclear operative uplink
balance: removed anti-drop implant from the nukie implants bundle and
changed its cost to 20 TC
/:cl:

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[172f65989e...](https://github.com/tgstation/tgstation/commit/172f65989ea40418b1c03316ad3163ee67f06e94)
#### Tuesday 2023-09-12 16:55:00 by Jacquerel

Nuclear Operative Jump Jets (#78088)

## About The Pull Request

This PR gives operative MODsuits access to "jump jets".
This is an activated module (starts pinned) with a 30 second cooldown
which removes your personal gravity for 5 seconds and (if possible)
pushes you upwards by one z level. In combination with your regular
jetpack this allows you to fly over gaps, and (most importantly) out of
pits such as you may inadvertently find yourself wandering into on
Icebox.
I have a few other changes I want to make specifically targetted at the
experience of Icebox station destruction causing people to fall several
z levels and get trapped, but this is the first one.

You have to stand still for 1 second to activate the jump jet. This is
because jetpack movement without gravity is actually usually faster than
an operative will walk, and I don't want them to just toggle it as a
sprint button while running around. If people find other tactical uses
for this though I think that's cool.

This module currently isn't available to crew on the tech web, although
maybe someone could add it later if they wanted to. It's not quite so
useful if you don't _also_ have a jetpack though.
I bumped the available complexity of the suits I attached it to up by
the complexity cost of this module so it's not taking up previously
available space.

## Why It's Good For The Game

It's funny when the whole ops team falls in a hole after an explosion
they caused and gets stuck in there fighting Snow Legions but they
should probably have some method for dealing with that.
It also lets them pop back up from the tram hole, a risky proposition
because any flying mob hit by the tram dies almost instantly.

## Changelog

:cl:
add: Operative MODsuits now have an attached "jump jet" which sends you
upwards and allows you to use your jetpack under gravity for a few
seconds, perfect for navigating the pits and valleys of Icebox Station.
/:cl:

---
## [Ricco5573/Mage-of-spades](https://github.com/Ricco5573/Mage-of-spades)@[e1634aa9d5...](https://github.com/Ricco5573/Mage-of-spades/commit/e1634aa9d5e0dc40ecf9f182a1881bacafdbf517)
#### Tuesday 2023-09-12 17:04:19 by Ricco5573

Rudementary wallrunning

holy fucking shit i forgot to push this to github yesterday and some shit got corrupted so i've had to recode this bastard piece of code

---
## [ChungusGamer666/NovusSS13](https://github.com/ChungusGamer666/NovusSS13)@[42220a7b39...](https://github.com/ChungusGamer666/NovusSS13/commit/42220a7b39aeac26083ebea3ce571a4b14a41a75)
#### Tuesday 2023-09-12 17:12:46 by Bob

dont fill up the fucking list with nulls god damn it

---
## [Samuelogooluwa/Landing-Page](https://github.com/Samuelogooluwa/Landing-Page)@[579277e08a...](https://github.com/Samuelogooluwa/Landing-Page/commit/579277e08a766de87a9138c59f1134e28924e1fb)
#### Tuesday 2023-09-12 17:24:48 by Samuel Missionaries

Update README.md


Let's just say... God has been faithful!!.
I often found myself losing sleep over this. Kinda got obsessed.
Was fun. 9/9 would do it again.

Live view: https://samuelogooluwa.github.io/Landing-Page/

---
## [Arkatos1/tgstation](https://github.com/Arkatos1/tgstation)@[dc0e5caca7...](https://github.com/Arkatos1/tgstation/commit/dc0e5caca763769242fe9254d95049ac0468bf64)
#### Tuesday 2023-09-12 18:06:26 by Sheits

Base Female sprite tweaks (#77407)

## About The Pull Request

ASS STUFF HAS BEEN REMOVED BUT I STILL HATE IT

This PR tones down the proportions of the female base sprites, as
currently they have about SIX extra pixels on the ass and a random pixel
missing from the neck, which breaks some hairstyles & makes the neck
look quite stupid.
It also adds a couple pixels to the male one because theirs was so
stupidly SMALL it looked like they had no tailbone (still does, kind
of).

Here is the current sprite 

![image](https://github.com/tgstation/tgstation/assets/81964183/1bf22dd7-2b06-4632-8617-b89b3b1c8d2c)
& new sprite (only neck pixel removed)

![image](https://github.com/tgstation/tgstation/assets/81964183/b1228e01-23e0-4508-86a6-bc8e73b0fcd0)

## Why It's Good For The Game

Fixes some hairs


![image](https://github.com/tgstation/tgstation/assets/81964183/3b293cf9-2661-4358-a327-2882acb93067)


## Changelog

:cl:
image: fixes weird inconsistency on the neck and butt of the female base
sprite
/:cl:

---
## [Arkatos1/tgstation](https://github.com/Arkatos1/tgstation)@[3dc75f84f2...](https://github.com/Arkatos1/tgstation/commit/3dc75f84f2eebc388c7f698284d77df4d8cf8fdf)
#### Tuesday 2023-09-12 18:06:26 by YakumoChen

Chen And Garry's Ice Cream: Ice Cream DLC (LIZARD APPROVED!) (#77174)

## About The Pull Request

Authored with help and love from @Thalpy 

I scream for ice cream!!


![image](https://github.com/tgstation/tgstation/assets/10399117/db1e559b-7dab-499b-a076-8f12748ba2e8)

Introduces many new flavours of ice cream:
-Caramel
-Banana
-Lemon Sorbet
-Orange Creamsicle
-Peach (Limited Edition!)
-Cherry chip
-Korta Vanilla (made with lizard-friendly ingredients!)


![image](https://github.com/tgstation/tgstation/assets/10399117/99a87615-f55c-49be-8caf-2b1ac4c7f03f)

Korta Cones! Now too can Nanotrasen's sanitation staff enjoy the wonders
of ice cream!
You can also substitute custom ice cream flavours with korta milk!
Finally, the meaty ice cream lactose-intolerants asked for is in reach!

## Why It's Good For The Game

I always thought the ice cream vat could use more flavours. The custom
flavour besides, it isn't as intuitive to rename the cone and the added
variety is good. The lack of a banana flavour already was questionable.
All the ice cream flavours used a selection of five sprites, now it's
just one sprite and better supporting more additions.
Some of the flavours don't use milk! You can't do this with the custom
flavour, making it slightly more interesting.

## Changelog
:cl: YakumoChen, Thalpy
add: Chen And Garry's Ice Cream is proud to debut a wide selection of
cool new frozen treat flavours on a space station near you!
add: Chen And Garry's Ice Cream revolutionary Korta Cones allow our ice
cream vendors to profit off the lizard demographic like never before!
code: Ice cream flavours now are all greyscaled similarly to GAGs
/:cl:

---
## [JaniShreyas/DimensionalityReduction](https://github.com/JaniShreyas/DimensionalityReduction)@[edcdc68158...](https://github.com/JaniShreyas/DimensionalityReduction/commit/edcdc6815814bf996d6ca7d8c7b14290d1eb5295)
#### Tuesday 2023-09-12 18:35:51 by JaniShreyas

Corrected the stupid mistake

Had idiotically used a regressor on the labels. Changed that to a classifier.
Should test this against a neural network next

---
## [massimopavoni/SwarmSimulator](https://github.com/massimopavoni/SwarmSimulator)@[4bd3e97f93...](https://github.com/massimopavoni/SwarmSimulator/commit/4bd3e97f93696ebc8434edbeef8a914783ca275c)
#### Tuesday 2023-09-12 18:37:07 by Massimo Pavoni

Huge progress commit

- had to stuff all of this into one because changes kept stacking onto each other, with obvious dependencies and broken things if pushed prematurely, so...here we go (in sparse, random order, because it's difficult otherwise)
- hivemind still in work, will be put into pause because everything else should be tested before it
- swarm properties has some more settings (I take enormous pride in adding a way of changing the application's level of parallelism) and a new way of managing the properties initialization, checks and files
- swarm state seems complete, with the modification and added random spawn positions (from the available shapes) for the swarm drones
- position obviously needs a random position method, for directives with random positions involved
- signal and echo regular expressions checks are available directly from swarm utils
- better shape inheritance, with sealed classes
- shapes now implement random positions list methods, using the new (proudly thought) custom parallelization level approach, will revisit this in newer versions in case some harder better faster stronger way of producing random positions arises
- polygon uses bounding rectangles for random positions generation, as it is much harder to generate positions on a polygon's boundary or inside the polygons (especially when they have self-intersections), and not required anyway; this probably introduces some weird dependencies between the polygon and its child class rectangle, but it shouldn't introduce too many problems (as long as there's no attempt at serialization (with potential circular dependencies)
- rectangle random positions are a bit strange themselves when generating on the boundary, and a support method was introduces for it (with an unreachable default case, kind of like with the shape factory switch, damned jvm weak inference/not so smart jacoco reports, would be interesting to look up why they cannot detect slightly more complex exhaustive pattern matching like in other languages (e.g. erhm erhmm haskell))
- very important drone class also seems to be ready and good, with initialization for position and jump directives' indexes, as well as all the needed methods that directives and hivemind will use, might need to changes some things here after tests are done and hivemind is ready to be tested as well
- directives have their own peculiar inheritance and sub-interfaces: it's not immediately obvious why that structure is there, but it will become very clear with the hivemind main step execution methods (the sub-interfaces and the added directive type enum will be there to ensure filtering for movement/echo/jump directives is possible (and that's very important to be able to use parallel streams and immutable position changes))
- echo directives are very simple, absorb and radiate are self explanatory
- move directives have their own little quirks, like the follow filter with average position direction (which might reveal itself to be quite heavy computation wise, unless a limit is put on the follow range or parallel streams are used for that computation as well, but that might be a problem because it would be used inside another parallel execution, the one for swarm steps), move and stop are quite easy to understand on the other hand
- jump directives are less clear and straightforward: the specifications were adapted to allow for a very easy parsing strategy (pun intended) for loops, meaning I just decided to use conditional and unconditional jumps, kind of like a very stripped down assembly control flow, so almost every jump directive has a jump index and some kind of condition (or not, like for the done directive, which is basically a goto)
- the directive factory uses a very similar, if not identical, approach to the shape factory, and the parser directive enumeration is the same as the shape type one, with the one difference being the name, as directive type is needed for the aforementioned necessity
- strategy parser is similar in interface to the domain parser, but it needs to implement a rather much more complex logic (even is written in methods not longer than 20-30 lines) to properly parse jump directives with some kind of backtracking (so that jump indexes can be properly matched)
- added tests for new shapes' methods and existing tests
- different tests setups and teardowns, with no more mocking, but swam properties testing resources instead, allowing for static mocking to not get in the way of parallel streams, I will need to remove the unneeded dependencies as soon as it becomes clear that mocking won't be useful again
- some exception additions and changes 
- javadoc updates for everything
- done! lots of things, I know, and not the best way to do versioning, but hopefully this encourages me to go step by step again *sweating smiley*

---
## [IUsedToBeADVD/pokeplum](https://github.com/IUsedToBeADVD/pokeplum)@[4fcc0746eb...](https://github.com/IUsedToBeADVD/pokeplum/commit/4fcc0746eb339ca68e667321c663954343c9d1e7)
#### Tuesday 2023-09-12 19:01:18 by IUsedToBeADVD

Type Retcons

Butterfree -> Bug/Psychic (don't give me shit, Game Freak are the ones that consistently gave it psychic moves, now they just get STAB)

Persian -> Normal/Dark

Kabuto/Kabutops -> Bug/Rock (they don't live directly in the water anymore, thats how I justify it at least)

Hoothoot/Noctowl -> Flying/Psychic (for now, since there aren't any others)

Doduo/Dodrio -> pure Flying

Vulpix/Ninetales -> Fire/Fairy (fuck yeah)

Stantler -> Normal/Psychic

Girafarig/Farigiraf -> Psychic/Dark

Rhyhorn -> pure Rock

Rhydon -> Rock/Dragon

Shellder/Cloyster -> Water/Rock

---
## [JoeBidenWhatAreYouHiding/kx](https://github.com/JoeBidenWhatAreYouHiding/kx)@[e786e51c7a...](https://github.com/JoeBidenWhatAreYouHiding/kx/commit/e786e51c7ae6726f0d2f7eed1e2b1fca9ea4995e)
#### Tuesday 2023-09-12 19:20:22 by daddydevito21

HOLY SHIT AMCATH LEARN TO FUCKIGN SPELL. THE WORD IS NIGH NOT NEIG, NEIGH IS FOR HORSES U STUPID FUCK

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[8ba059415e...](https://github.com/TaleStation/TaleStation/commit/8ba059415e8a1e2bdbe9d43fb991bdcc31633122)
#### Tuesday 2023-09-12 19:45:57 by TaleStationBot

[MIRROR] [MDB IGNORE] Cursed Slot Machine Fixes (#7570)

Original PR: https://github.com/tgstation/tgstation/pull/77989
-----

## About The Pull Request

A lot of these were stuff I did in response to reviews but apparently
didn't test extremely thoroughly. My bad.

* The proc for checking if the machine is in use is split out into its
own thing for clarity, and for potential reuse.
* The signal is no longer fucked up so you can actually get more than
one curse out of the slot machine as intended.
* Admin heals (and admin heals only) can remove the status effect. This
is just in case someone fucks up a variable when running an event and
wants to quickly heal some people while they varedit it to actually be a
proper event.
* Some nice code stuff while I was there, we don't need to be
typecasting to human anymore so it's nice to fix that.
## Why It's Good For The Game

Fixes are good.
## Changelog
:cl:
fix: The Cursed Slot Machine should now actually give you more than one
pull.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [znichola/ft_transcendence_test](https://github.com/znichola/ft_transcendence_test)@[9c0836f054...](https://github.com/znichola/ft_transcendence_test/commit/9c0836f0541b57d0f20c8c9a52ad42095c105470)
#### Tuesday 2023-09-12 20:03:08 by Nicholas Zivkovic

fairly large file refactor

file cleanup
- files have been moved out of the src into folders
- stuff has been renamed, etc
- also old ass files were deleted

functionality
- the firend on the profile now shows the list of friends
- the status is always blue, due to the missing string type from api
- messages and chat rooms browsers can be done in a simmilar style
- also many blank pages have been added they are place holder
  so the app can take a bit more shape

style
- i added a light background to the content looks a bit nicer
- don't try complain about it, lest ye wish to see Rick Astly
- also I hid the scroll bar, we had that bug, and it was ugly
  but we can still scroll, we can fix it proper later

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[98321c94d5...](https://github.com/TaleStation/TaleStation/commit/98321c94d543d39341d79cff114ca12b8bb5fb3d)
#### Tuesday 2023-09-12 20:08:44 by TaleStationBot

[MIRROR] [MDB IGNORE] SPESSMEN 2.0: le cargo resprite (no mining) ((i hate mining)) (#7459)

Original PR: https://github.com/tgstation/tgstation/pull/77456
-----
## About The Pull Request


![image](https://github.com/tgstation/tgstation/assets/86872535/3f43680a-36f0-4008-8e0f-3a1c4cee5427)

googoogagaga. hey guys, it's me! le crates guy!

cargo's resprite was about a year ago now, and i, and the spritetainers
who's approval I got, believe that it's time for a refresh. so uh. here
it is. yeah.

this PR adds a new piece of outerwear for cargo players to wear, a
gorka! some soviet eastern european larp-er jacket. looks cool tho.

and, as well, the quatermaster is now distinct compared to his
underlings- decked out with a spiffy overcoat and dress shirt.

now, you may be wondering about the fact that the cargo tech is now
wearing jeans? this is the new look for the cargo tech, but! before you
start soul posting, you can still infact, get shorts if you want.

really, I wanted it to be randomised, a coin-flip, but uh- that's not
possible lol.

random misc changes: changed PDA colours, qm wears laceups, cargo cap
was repainted

i got approval from both Wallemations and Imaginos16 for this PR and the
changes associated with it.
## Why It's Good For The Game

shruggers idk, i think it looks good. cargo is now much more visually
distinct, and has a better vision to it. quatermaster receiving a new
look that makes him stand out is a good thing too, imo.
## Changelog
:cl: axietheaxolot / viro
imageadd: brand new cargo sprites!
/:cl:

---------

Co-authored-by: axietheaxolotl <86872535+axietheaxolotl@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [Clark-Mason/Academic-Projects-Freshman-](https://github.com/Clark-Mason/Academic-Projects-Freshman-)@[20ce6dd5dc...](https://github.com/Clark-Mason/Academic-Projects-Freshman-/commit/20ce6dd5dcccd12f82048f17214e866269834212)
#### Tuesday 2023-09-12 20:17:16 by Clark-Mason

Add files via upload

# Sudoku Validator

Hello there! I'm Mason Clark and this is a project I created during my freshman year. This project validates Sudoku grids to ensure they adhere to the standard rules of the game. Let me break down how it works and the experience I gained from building it.

## Overview
The primary objective of this project is to validate Sudoku puzzles from an input file. The validator checks:
1. Rows to ensure that each digit (1-9) appears exactly once.
2. Columns for duplicates of the numbers 1-9.
3. Each 3x3 grid within the Sudoku puzzle for duplicate digits from 1-9.

If any violations are found, the validator will report them.

## Project Breakdown

 1. **Column Validation**
The function `columnValidation` takes a pointer to an integer array representing the Sudoku grid and iterates through each column to ensure no column contains the same number twice. 

2. **Row Validation**
In a similar fashion, `rowValidation` focuses on rows, ensuring each number from 1-9 appears only once per row.

3. **Grid Validation**
The `gridValidation` function divides the Sudoku grid into its nine 3x3 boxes, verifying that each box adheres to Sudoku rules.

 4. **Main Function**
The heart of the program, the `main` function prompts users for a file name, reads the file's content (which should contain the Sudoku puzzles), and validates each puzzle. After each validation check, the results are printed, indicating if a puzzle is solved, valid, or contains errors.

## Lessons Learned
Throughout the development of this project, I got to refine my C++ skills, particularly in:
- Dynamic memory management with pointers.
- File I/O operations to read from an external file.
- Use of the Standard Template Library, especially the vector and string classes.
- Advanced concepts such as string manipulations, stringstream, and the use of the `iomanip` library for formatting outputs.
- Writing efficient algorithms for puzzle validation and debugging them.

##Reflections
Building this project during my freshman year was a rich learning experience. Not only did I get to challenge myself with a real-world problem, but I also got a deeper appreciation for algorithmic thinking and the importance of writing clean, efficient code. I hope this project serves as a testament to my growth as a programmer and my dedication to tackling complex challenges. If you have any suggestions, feedback, or potential improvements, feel free to contribute or reach out! 

Thanks for checking out my Sudoku Validator!

---
## [Onule/TaleStation](https://github.com/Onule/TaleStation)@[30b8cd02b3...](https://github.com/Onule/TaleStation/commit/30b8cd02b34fdae3a09a2ed3bc09bf4436ef2b55)
#### Tuesday 2023-09-12 20:21:02 by TaleStationBot

[MIRROR] [MDB IGNORE] Added Omen Spontaneous Combustion and light tube and mirror effects (#7140)

Original PR: https://github.com/tgstation/tgstation/pull/77175
-----

## About The Pull Request

Cursed crewmembers can randomly, extremely rarely, spontaneously combust
for no reason.

Cursed crewmembers can get zapped by nearby light tubes.

Cursed crewmembers can freak out when passing by mirrors.

To make up for these, triggering a cursed effect is slightly less than
half as likely now when walking around now.

## Why It's Good For The Game

Cursed is fun as hell, but after a certain point it gets kind of
monotonous - it's airlocks, vending machines, and the rest is too rare
to count. We need more ways to comically get hurt in the game.

You might dislike the 'reduced effects' bit but trust me it is
incredibly frickin' common to have shit happen to you. Add to the
occasional vending machine and airlock crushes the near-constant light
tubes all over the station? Yeah, that needs a toning down else it will
be just a tad too miserable to be funny. Also cause the poor janitor
unneeded stress.

## Changelog

:cl:
add: Cursed crewmembers can randomly, extremely rarely, spontaneously
combust for no reason.
add: Cursed crewmembers can get zapped by nearby light tubes.
add: Cursed crewmembers can freak out when passing by mirrors.
add: To make up for these, triggering a cursed effect is slightly less
than half as likely now when walking around now.
/:cl:

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[d034711fbc...](https://github.com/TaleStation/TaleStation/commit/d034711fbc29e9a28cc4af9c84f7597e2042c41a)
#### Tuesday 2023-09-12 20:38:06 by TaleStationBot

[MIRROR] [MDB IGNORE] Desouls Hivelord (#7690)

Original PR: https://github.com/tgstation/tgstation/pull/78213
-----
## About The Pull Request


![dreammaker_RJz4brjobM](https://github.com/tgstation/tgstation/assets/7483112/e5e4a3e9-ea6b-47f9-887c-3339d24d3fa8)

Replaces the sprite of the hivelord with a new one, in my continuing
quest to annihilate the old asteroid mob sprites.
A (never completed) asteroid mob resprite was actually my first PR, this
one is my 200th.
I am also planning on fucking with basic mob versions of these mobs some
time but the sprites can be atomised out.

In addition to replacing the old-ass MSPaint sprites, this PR also adds
a short death animation effect to the hivelord brood (from hivelords or
legions) which looks nicer than them just vanishing instantly upon
death.

Look at this video for an example of the animation:
https://www.youtube.com/watch?v=cKaskN5-y2A

## Why It's Good For The Game

Looks nicer.

## Changelog

:cl:
image: Hivelords have a new sprite.
image: Hivelord and Legion brood have a death animation.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Clark-Mason/Academic-Projects-Freshman-](https://github.com/Clark-Mason/Academic-Projects-Freshman-)@[79cc74bcc7...](https://github.com/Clark-Mason/Academic-Projects-Freshman-/commit/79cc74bcc76a57158a374fe104bb87b7a79cf2fe)
#### Tuesday 2023-09-12 20:41:13 by Clark-Mason

Add files via upload


##Roman and Arabic Numerals Converter & Organizer##

Hey there! This project, developed during my freshman year for a class, is primarily a C++ implementation for working with Roman and Arabic numerals. Here's what I accomplished:

1. **Conversion of Numerals**:
   - `romanConversion`: This function takes in a Roman numeral string and converts it into its equivalent Arabic numeral value.
   - `arabicConversion`: Given an Arabic numeral, this function returns the corresponding Roman numeral.

2. **Linked List Data Structure**:
   - Struct `node`: Serves as the building block of my linked list. It contains two fields: `aNum` (Arabic numeral) and `rNum` (Roman numeral).
   - `linkList`: Inserts a new node into the list.
   - `print`: Recursively traverses and prints the linked list.
   - `searchList`: Searches the linked list for a given Arabic or Roman numeral.

3. **Merge Sort on Linked List**:
   - `mergeLists`: A helper function to merge two sorted linked lists. This also incorporates the ability to sort based on either Arabic or Roman numerals.
   - `mergeSort`: Implements the merge sort algorithm to sort the linked list. Depending on user input, it can sort by either Arabic or Roman numerals.

4. **File Operations**:
   - Reading from an input file and processing each line, checking if it contains a valid Roman or Arabic numeral. Invalid entries (e.g., invalid Roman characters or Arabic numbers outside the range) are skipped.
   - The processed numbers are then stored in a linked list.
   - `fileWrite`: Writes the linked list to a file named `numbers.txt`.

5. **User Interface**:
   - A simple console interface that allows users to:
     - Search the linked list for a specific numeral.
     - Sort the linked list by either Roman or Arabic numerals.

**Learning & Application Reflection: Roman-Arabic Numeral Converter**

During my freshman year, I embarked on a journey to understand the intricacies of C++ through the development of a unique project: a Roman-Arabic Numeral Converter with additional functionalities.

**What I Learned:**

1. **Complex Data Structures:** At the heart of this program lies the `node` structure, which makes the implementation of linked lists possible. Through this, I familiarized myself with dynamic memory allocation in C++, understanding pointers, and the concept of data encapsulation in structures.

2. **Algorithm Development:** The project required the creation of intricate algorithms for converting numerals between Roman and Arabic systems. Crafting these functions deepened my understanding of the logical structures needed for such transformations and how to efficiently navigate and manipulate strings and numbers.

3. **File Handling:** The program's ability to read from and write to files was a significant step in learning about I/O operations in C++. Handling files is a foundational skill, as it's a common requirement in many real-world applications.

4. **Recursive Functions:** I used recursion in several parts of the program, such as in the merge sort and printing functions. This iterative approach to solving problems solidified my understanding of recursion's power and how to manage its complexities.

5. **Advanced Sorting:** The merge sort algorithm's incorporation taught me about one of the more efficient sorting techniques. Through this, I appreciated the importance of algorithmic efficiency and how it can impact a program's performance.

##Real-world Application:##

1. **Data Processing:** In any field where data conversion is required, similar logic can be employed. While this project focused on numerals, the underlying principles could be applied to other data transformation needs, such as unit conversion in engineering or currency conversion in finance.

2. **Database Management:** The application's ability to sort, search, and store data in linked lists offers a basic insight into how databases manage and retrieve information. As databases are central to nearly all sectors, understanding their foundational concepts can be invaluable.

3. **User Interaction:** The program's menu-driven interface gave me a perspective on user experience (UX) and how to create intuitive interfaces that cater to users' needs, a skill that's highly valued in software development.

##Conclusion:##

This project was more than just a grade in a class; it was an immersive experience that broadened my horizon in the world of programming. It underscored the importance of algorithmic thinking, efficiency, and user-centric design. The lessons I've gleaned from this endeavor will undoubtedly serve as a strong foundation as I continue my journey in the vast realm of computer science.

Cheers!
Mason Clark.

---
## [KikoWen0/NebulaStation](https://github.com/KikoWen0/NebulaStation)@[51c82f3222...](https://github.com/KikoWen0/NebulaStation/commit/51c82f32223179f7263dd8d4de11eb62f23ef8fd)
#### Tuesday 2023-09-12 20:52:23 by RICK IM RI

Adds Blood-drunk and demonic frost miner boss music. (#78123)

Acts as a continuation of PR #77149 for boss music functionality and
implements a BDM and demonic frost miner boss music theme.

More music is good, but I do have some gripes with my own PR. This
particular track relies on instrumentation that when compressed just
doesn't sound as good, and the in-game version is noticeably less
enjoyable that the high quality version. I wish I could help the track
out more, but as is it's already at 811 kb which is barely in line with
file requirements, so i just can't justify bloating the audio file sizes
to make it sound better. You notice this kind of problem a lot with the
higher runtime music and background tracks. It just feels a bit more
clunky than hierophant, but what are you gonna do right?

---
## [projectitis/flame](https://github.com/projectitis/flame)@[2f973abe8b...](https://github.com/projectitis/flame/commit/2f973abe8b298a4f6f1164065783de560953d789)
#### Tuesday 2023-09-12 20:56:12 by Luan Nico

docs: Improved spellchecking (#2722)

Improve our spellchecker (cspell) configuration and dictionary file
organization.

# Rationale

This is a proposal to establish a few changes:
* better separate our dictionary files into different categories of
types of words we are including
* improve the cspell regexes to be more aggressive
* be less lenient to what kinds of words we are adding to our
dictionaries
* have the dictionary file also serve as an explanation for obscure
references that cannot be easily derived from the word

Essentially my goal is that either when reviewing a PR that adds a new
entry to our dictionary, or when reading the dictionary files
themselves, it is immediately obvious what the entries are and why they
are there. Currently it can be just a dumpster we throw anything into if
spellcheck fails.

# Proposal

This PR-as-a-proposal essentially do the following changes.

## Split Dictionary Files

Proposes a better separation for our dictionary files. Currently we have
3 that are a bit broad and not super clear on what goes where. This
breaks it down a bit more and adds a comment to each file explaining
what kinds of terms should be added to each; that also serves as a
general guidance for what kinds of words should be added to the lexicon
in general, and makes it harder for mistakes to make into it.

* `flame_dictionary`: remains pretty much unchanged; it is dedicated to
Flame-related words, including companies, tools, and libraries (and
their associated concepts) mentioned on our codebase. Basically a
collection of proper-nouns relating to companies and libraries we
mention.
* `dart_dictionary`: new file for Dart and Flutter related terms
* `sphinx_dictionary`: unchanged, for Sphynx related terms
* `people_dictionary`: specific for people names and usernames
referenced on the codebase (in TODOs, mentions, etc)
* `words_dictionary`: actual English-language words (or common
abbreviations) missing from CSpell
* `gamedev_dictionary`: this was our biggest file that contained all
sort of things. it has been mostly broken down and now only contains
general development-adjacent terms and expressions

## Include definitions

Except for the `words` dictionary, which should be self-explanatory (as
it basically covers for "holes" in CSpell standard dictionary, which I
have been finding a bit lacking), every other file will contain terms in
the form:

```
word # definition of the word
```

What exactly the definition is can slightly vary depending on which
dictionary file we are talking about, but the examples should be
self-explanatory.

As an example, for the gamedev file, it should provide some simple
guidance as to what the term means, or if it's an acronym or
abbreviation, what it stands for. The goal is not to teach the entire
concept to someone unfamiliar, but allow them to "google" it for
themselves by giving enough context, so they can confirm their
suspicions. For example, if they see `LTRB` somewhere by itself, they
are not able to "just google that" because it is too vague. The
dictionary file provides enough context for the user to figure out
however much deeper information they want about any particular subject.
It will also disambiguate from any non-Flame related homonyms. For
people on the people file and companies on the flame file, the
description will provide links to clearly disambiguate what they are;
for tools, a brief description of what the tool is for is also included.
And so on.

The goal is not to build a comprehensive, in depth-guide to each word we
use, but rather to give the bare minimum of context on what this term
"is doing" on our codebase.

## Be less lenient with terms

My idea with these two major changes combined, is that we are overall
more tactical about which terms we want to add to the dictionaries.
Adding a word to the dictionary file is essentially giving carte blanche
to anyone in the future to reuse that term anywhere. I think we should
see spellchecker violations as "warnings"; we decide on the set of
warning rules we want to enable for the entire project (hopefully all
the ones that make sense; or have a reason for disabling the ones that
don't). We might need to violate these warnings sporadically, for
example, we ban `print` on the codebase but might need to allow it
specifically in a couple places. But we would not disable the entire
warning to do that, rather we would add a specific comment-bypass on the
smallest possible scope that encompasses all the relevant lines. We
would also add a proper comment explaining why we are bypassing the
general rule in this specific place.

Similarly, we should not have one-off violations on the dictionary file,
even if they make sense in the one place they occur, but we should
encourage more liberal use of scoped bypasses for such cases. These
Ukrainian words are required in this file, but should not be on the
dictionary as it does not make sense to use foreign languages anywhere
else:

```
// used as examples of Ukrainian words on the documentation below
// cSpell:ignore рушниця, рушниці, рушниць
```

It might look inelegant to have to include that, but just like a
warning-bypass comment, accompanied by the explanatory proper-comment,
this actually provides helpful guidance and context for the reader that
might be confused with the usage of incomprehensible terms.

This also encourages people to avoid obscure terms that are not already
in our dictionary (i.e. that we have already "bought in" and paid the
mental load investment cost), making our code (and docs) easier to parse
and read for everyone. I want to be extremely clear that that **does
not** mean we need to "dumb down" anything whatsoever, or do any sort of
gymnastics to avoid the wrath of an incompetent spellchecker.

But, for example [when spelling "cave
ace"](https://github.com/flame-engine/flame/pull/2304) in variable names
in a random example, having it typed as `caveAce` instead of `caveace`
can slightly help with readability, specially for non-native speakers
(like most of us). It is an extremely minor insignificant gain, but
having the dictionary file require a brief description will nudge us to
give a bit more thought into each "bypass" we are adding.

(note: a similar issue that I have not yet addressed is "spine boy", but
I will leave that for followups and just added that one to the
dictionary for now, as I am still over the fence on that one since it is
an actual "known" character with a dedicated page, so it is more like a
proper noun - as a specific decision I think it is out-of-scope of the
broader discussion).

---
## [MrGVSV/bevy](https://github.com/MrGVSV/bevy)@[fb4c21e3e6...](https://github.com/MrGVSV/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Tuesday 2023-09-12 21:54:14 by Ida "Iyes

bevy_audio: ECS-based API redesign (#8424)

# Objective

Improve the `bevy_audio` API to make it more user-friendly and
ECS-idiomatic. This PR is a first-pass at addressing some of the most
obvious (to me) problems. In the interest of keeping the scope small,
further improvements can be done in future PRs.

The current `bevy_audio` API is very clunky to work with, due to how it
(ab)uses bevy assets to represent audio sinks.

The user needs to write a lot of boilerplate (accessing
`Res<Assets<AudioSink>>`) and deal with a lot of cognitive overhead
(worry about strong vs. weak handles, etc.) in order to control audio
playback.

Audio playback is initiated via a centralized `Audio` resource, which
makes it difficult to keep track of many different sounds playing in a
typical game.

Further, everything carries a generic type parameter for the sound
source type, making it difficult to mix custom sound sources (such as
procedurally generated audio or unofficial formats) with regular audio
assets.

Let's fix these issues.

## Solution

Refactor `bevy_audio` to a more idiomatic ECS API. Remove the `Audio`
resource. Do everything via entities and components instead.

Audio playback data is now stored in components:
- `PlaybackSettings`, `SpatialSettings`, `Handle<AudioSource>` are now
components. The user inserts them to tell Bevy to play a sound and
configure the initial playback parameters.
- `AudioSink`, `SpatialAudioSink` are now components instead of special
magical "asset" types. They are inserted by Bevy when it actually begins
playing the sound, and can be queried for by the user in order to
control the sound during playback.

Bundles: `AudioBundle` and `SpatialAudioBundle` are available to make it
easy for users to play sounds. Spawn an entity with one of these bundles
(or insert them to a complex entity alongside other stuff) to play a
sound.

Each entity represents a sound to be played.

There is also a new "auto-despawn" feature (activated using
`PlaybackSettings`), which, if enabled, tells Bevy to despawn entities
when the sink playback finishes. This allows for "fire-and-forget" sound
playback. Users can simply
spawn entities whenever they want to play sounds and not have to worry
about leaking memory.

## Unsolved Questions

I think the current design is *fine*. I'd be happy for it to be merged.
It has some possibly-surprising usability pitfalls, but I think it is
still much better than the old `bevy_audio`. Here are some discussion
questions for things that we could further improve. I'm undecided on
these questions, which is why I didn't implement them. We should decide
which of these should be addressed in this PR, and what should be left
for future PRs. Or if they should be addressed at all.

### What happens when sounds start playing?

Currently, the audio sink components are inserted and the bundle
components are kept. Should Bevy remove the bundle components? Something
else?

The current design allows an entity to be reused for playing the same
sound with the same parameters repeatedly. This is a niche use case I'd
like to be supported, but if we have to give it up for a simpler design,
I'd be fine with that.

### What happens if users remove any of the components themselves?

As described above, currently, entities can be reused. Removing the
audio sink causes it to be "detached" (I kept the old `Drop` impl), so
the sound keeps playing. However, if the audio bundle components are not
removed, Bevy will detect this entity as a "queued" sound entity again
(has the bundle compoenents, without a sink component), just like before
playing the sound the first time, and start playing the sound again.

This behavior might be surprising? Should we do something different?

### Should mutations to `PlaybackSettings` be applied to the audio sink?

We currently do not do that. `PlaybackSettings` is just for the initial
settings when the sound starts playing. This is clearly documented.

Do we want to keep this behavior, or do we want to allow users to use
`PlaybackSettings` instead of `AudioSink`/`SpatialAudioSink` to control
sounds during playback too?

I think I prefer for them to be kept separate. It is not a bad mental
model once you understand it, and it is documented.

### Should `AudioSink` and `SpatialAudioSink` be unified into a single
component type?

They provide a similar API (via the `AudioSinkPlayback` trait) and it
might be annoying for users to have to deal with both of them. The
unification could be done using an enum that is matched on internally by
the methods. Spatial audio has extra features, so this might make it
harder to access. I think we shouldn't.

### Automatic synchronization of spatial sound properties from
Transforms?

Should Bevy automatically apply changes to Transforms to spatial audio
entities? How do we distinguish between listener and emitter? Which one
does the transform represent? Where should the other one come from?

Alternatively, leave this problem for now, and address it in a future
PR. Or do nothing, and let users deal with it, as shown in the
`spatial_audio_2d` and `spatial_audio_3d` examples.

---

## Changelog

Added:
- `AudioBundle`/`SpatialAudioBundle`, add them to entities to play
sounds.

Removed:
 - The `Audio` resource.
 - `AudioOutput` is no longer `pub`.

Changed:
 - `AudioSink`, `SpatialAudioSink` are now components instead of assets.

## Migration Guide

// TODO: write a more detailed migration guide, after the "unsolved
questions" are answered and this PR is finalized.

Before:

```rust

/// Need to store handles somewhere
#[derive(Resource)]
struct MyMusic {
    sink: Handle<AudioSink>,
}

fn play_music(
    asset_server: Res<AssetServer>,
    audio: Res<Audio>,
    audio_sinks: Res<Assets<AudioSink>>,
    mut commands: Commands,
) {
    let weak_handle = audio.play_with_settings(
        asset_server.load("music.ogg"),
        PlaybackSettings::LOOP.with_volume(0.5),
    );
    // upgrade to strong handle and store it
    commands.insert_resource(MyMusic {
        sink: audio_sinks.get_handle(weak_handle),
    });
}

fn toggle_pause_music(
    audio_sinks: Res<Assets<AudioSink>>,
    mymusic: Option<Res<MyMusic>>,
) {
    if let Some(mymusic) = &mymusic {
        if let Some(sink) = audio_sinks.get(&mymusic.sink) {
            sink.toggle();
        }
    }
}
```

Now:

```rust
/// Marker component for our music entity
#[derive(Component)]
struct MyMusic;

fn play_music(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
) {
    commands.spawn((
        AudioBundle::from_audio_source(asset_server.load("music.ogg"))
            .with_settings(PlaybackSettings::LOOP.with_volume(0.5)),
        MyMusic,
    ));
}

fn toggle_pause_music(
    // `AudioSink` will be inserted by Bevy when the audio starts playing
    query_music: Query<&AudioSink, With<MyMusic>>,
) {
    if let Ok(sink) = query.get_single() {
        sink.toggle();
    }
}
```

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[0dd3e66aef...](https://github.com/san7890/bruhstation/commit/0dd3e66aefa2a61cb4e78482273958c1d09f8295)
#### Tuesday 2023-09-12 21:57:05 by Vekter

Grilles take 0-1 damage when shocking something, power sinks are available at lower reputation (#77860)

## About The Pull Request
Ports BeeStation/BeeStation-Hornet#3590. As it is right now, it's
trivial to set up a contraption using a conveyor belt and a shocked
grille to continuously shock monkey bodies. While this is very funny, it
also serves as a ghetto powersink that's hard to locate, easy to
replicate, and lasts effectively forever, since you can just keep
shocking the same bodies over and over again.

This doesn't completely remove the ability to make these, but it makes
them require at least a little maintenance and provides a way for them
to stop working even if the crew isn't able to locate them.

In an attempt to finally get people using the _actual_ powersink,
they'll show up a bit earlier in progression now. I'm not convinced 20
minutes is enough, but I don't want to put them in early enough that it
fucks with Engineering's ability to set things up at round start. We can
turn this down further if need be.

I'm also up for turning the TC requirement down, but 11 feels about
right for what they're supposed to do, so I'd prefer we try this first
and see how that works.

## Why It's Good For The Game
I'm all for goofy weird shit players have found, but there's an issue
with being able to do what an antag item is supposed to do but just
plain better. This shouldn't make creating these impossible or make them
unusable, but it'll require players to actively monitor them if they
want it to run for an extended period.

Additionally, we don't really see powersinks much anymore, and while
that might be more because powernets are kind of buggy and unreliable, I
think making them easier to get will make them show up a little more.

## Changelog
:cl: Vekter
balance: Grilles will now take 0-1 damage every time they shock
something.
balance: Powersinks are now available earlier in traitor progression.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [kokizzu/nushell](https://github.com/kokizzu/nushell)@[fed4233db4...](https://github.com/kokizzu/nushell/commit/fed4233db4d81de00068ffa7cf1c0d09506bc150)
#### Tuesday 2023-09-12 23:29:33 by David Matos

use uutils/coreutils cp command in place of nushell's cp command (#10097)

<!--
if this PR closes one or more issues, you can automatically link the PR
with
them by using one of the [*linking
keywords*](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword),
e.g.
- this PR should close #xxxx
- fixes #xxxx

you can also mention related issues, PRs or discussions!
-->

# Description
Hi. Basically, this is a continuation of the work that @fdncred started.
Given some nice discussions on #9463 , and [merged uutils
PR](https://github.com/uutils/coreutils/pull/5152) from @tertsdiepraam
we have decided to give the `cp` command the `crawl` stage as it was
named.

> [!NOTE] 
Given that the `uutils` crate has not made the release for the merged
PR, just make sure you checkout latest and put it in the required place
to make this PR work.

The aim of this PR is for is to see how to move forward using `uutils`
crate. In order to getting this started, I have made the current
`nushell cp tests` pass along with some extra ones I copied over from
the `uutils` repo.

With all of that being said, things that would be nice to decide, and
keep working on:

Crawl:
- Handling of certain `named` flags, with their long and short
forms(e.g. --update, --reflink, --preserve, etc), and using default
values. Maybe `-u` can already have a `default_missing_value`.
- Should we maybe just support one single option `switch` flags (see
`--backup` in code) as a contrast to the other named args.
- Complete test coverage from `uutils`. They had > 100 tests, and I
could only port like 12 as they are a bit time consuming given they
cannot be straight up copy pasted. Maybe we do not need all >100, but
maybe the more relevant to what we want.
- Refactor this code

Walk:
- Non fatal errors on `copy` from `utils`. Currently it just sends it to
stdout but errors have no span
- Better integration 

An added possibility is the addition of `SyntaxShape::OneOf()` for
`Named` arguments which was briefly mentioned in the discord server, but
that is still to be decided. This could greatly improve some of the
integration. This would enable something like `cp --preserve [all
timestamp]` or `cp --preserve all` to both work.

I did not want to keep holding on this, and wait till I was happy with
the code because I think its nice if everyone can start up and suggest
refactors, but the main important part now was getting it out the door,
as if I take my sweet time this will take way longer :stuck_out_tongue:

<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->

# Tests + Formatting

Make sure you've run and fixed any issues with these commands:

- [X] cargo fmt --all -- --check` to check standard code formatting
(`cargo fmt --all` applies these changes)
- [X] cargo clippy --workspace -- -D warnings -D clippy::unwrap_used` to
check that you're using the standard code style
- [X] cargo test --workspace` to check that all tests pass
- [X] cargo run -- -c "use std testing; testing run-tests --path
crates/nu-std"` to run the tests for the standard library

> **Note**
> from `nushell` you can also use the `toolkit` as follows
> ```bash
> use toolkit.nu # or use an `env_change` hook to activate it
automatically
> toolkit check pr
> ```
-->

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

---------

Co-authored-by: Darren Schroeder <343840+fdncred@users.noreply.github.com>

---
## [Coconutwarrior97/tgstation-1](https://github.com/Coconutwarrior97/tgstation-1)@[95ec0e6545...](https://github.com/Coconutwarrior97/tgstation-1/commit/95ec0e65458ece9c5c80952e75d5d32c4fbb794b)
#### Tuesday 2023-09-12 23:33:34 by necromanceranne

Dissection experiments are handled by autopsy surgery. Removes redundant dissection surgery. You can repeat an autopsy on someone who has come back to life. (#77386)

## About The Pull Request

TRAIT_DISSECTED has had the surgical speed boost moved over to
TRAIT_SURGICALLY_ANALYZED.

TRAIT_DISSECTED now tracks if we can do an autopsy on the same body
again, and blocks further autopsies if it is on the mob. A mob that
comes back to life loses TRAIT_DISSECTED. This allows for mobs to be
autopsied once again.

Since it is completely redundant now (and was the whole time TBH),
dissections have been removed in favour of just having the experiment
track autopsies.

Fixes https://github.com/tgstation/tgstation/issues/76775

## Why It's Good For The Game

Today I showed up to a round where someone autopsied all the bodies in
the morgue, not realizing they were using the wrong surgery. Since I
couldn't _redo_ the surgery, this rendered all these bodies useless.
This was not out of maliciousness, they just didn't know better. There
are two autopsies in the surgery list, but only one is valid for the
experiment and doing the wrong one blocks _both surgeries_. Dissection
is completely useless outside of experiments. This same issue also
prevents additional autopsies on the same person, even if they had come
back to life and died again after you had done the initial autopsy.
Surely you would want to do more than one autopsy, right? That's two
separate deaths!

This resolves that by giving you a method of redoing any screwups on the
same corpse if necessary. It only matters if the experiment is available
anyway, so there isn't much reason to punish players unduly just because
they weren't aware science hadn't hit a button on their side (especially
since it isn't communicated to the coroner in any way to begin with). It
also removes a completely useless surgery and ties in the experiment to
what the coroner is already going to be doing. They can dissect their
corpses to their hearts content without worrying about retribution from
science for doing so.

In addition, someone repeatedly dying can continue to have autopsies
done on them over the course of the round. The surgery bonus only
applies once, so the only reason to do autopsies after the first is to
discover what might have killed someone. No reason this should block
further surgeries, just block surgeries when the person remains a
corpse.

## Changelog
:cl:
fix: You can do autopsies on people who were revived and died again
after they had already been dissected.
qol: Autopsies have become the surgery needed to complete the dissection
experiments. As a result, the dissection surgery has been removed as it
is now redundant.
qol: A coroner knows whether someone has been autopsied and recently
dissected (and thus hasn't been revived) by examining them.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [AkairyuGestalter/xivanalysis](https://github.com/AkairyuGestalter/xivanalysis)@[c009fd5bcf...](https://github.com/AkairyuGestalter/xivanalysis/commit/c009fd5bcf5a7ae7810f9e30a3f7df648c2d4d43)
#### Tuesday 2023-09-12 23:49:41 by B Fraser

BLU: 6.45 Moon Flute update (#1873)

* BLU: Being Mortal mistakenly had the same actionId as Apokalypsis

* BLU Moon Flute window: Swap out important spells in the burst window

With the new spells in 6.45, BLU's burst window got even more
busy.  It is, technically, still a gain to cast Rose of Destruction,
to use Bristle on Matra Magic, and to use Glass Dance, but they are
all roughly on the category of "you may drop these, either entirely
or just out of the opener".

Adding 4 or 6 new potential actions to the report would've rendered
mostly useless, so instead, this commit makes it so that we expect
any Moon Flute burst to include the following oGCDs:

    J Kick
    Shock Strike
    Feather Rain
    Nightbloom
    Being Mortal
    Sea Shanty
    Surpankaha x4
    Phantom Flurry

And the following two GCDs:

    Matra Magic
    Triple Trident (only if it was off cooldown, for SpS builds)

While there's optimal filler GCDs for the opener, they aren't
useful generic recomendations (Swiftcast => Wild Rage), and they
aren't standard between all openers (Winged Reprobation and Rose of
Destruction are in practice mutually exclusive, and some openers
drop Bristle for a third Winged Reprobation, for roughly the same
potency on every burst but the first one), so we're just
not enforcing them anymore.

It's also optimal to do an extra weave for Glass Dance somewhere in
the opener, but that's now so rarely taken due to spell slot
limitations that giving it its own column in the report will just
add noise.

* BLU Moon Flute: Handle odd-minute Breath of Magic bursts

`Breath of Magic` is a new DoT BLU got this patch.  It lasts 60
seconds and does a silly amount of potency, with the caveat that
only one person can apply it on the target.

Due to BoM's silly potency, ideally it should be reapplied under
Moon Flute every minute, meaning that in addition to the normal
even-minute burst, the BoM applier should be doing an odd-minute
burst too.

Since "odd-minute" and "even-minute" are going to be entirely
encounter-dependent, this commit is using a heuristic:
If they used both `Breath of Magic` and `Song of Torment` under
a given Moon Flute, then this is an odd-minute burst, so few
of the usual requirements apply.

* BLU Moon Flute: Keep support for pre-6.45 BLU logs

* BLU Moon Flute 6.45: changelog

* BLU Moon Flute: Change the heuristic for odd-minute bursts

Per @xiashtra's suggestion, we now base this on whether
Nightbloom is on-cooldown during the moon flute, rather
than checking Song of Torment, which in some edge cases
people may not be taking.

* BLU Moon Flute: Reworded the two suggestions to be a bit less convoluted

* BLU Moon Flute: yarn extract

* BLU Moon Flute: yarn linting

---

