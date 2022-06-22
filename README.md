## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-06-21](docs/good-messages/2022/2022-06-21.md)


1,577,469 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,577,469 were push events containing 2,490,552 commit messages that amount to 184,773,917 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 30 messages:


## [Official-Ayrton990/android_kernel_xiaomi_renoir](https://github.com/Official-Ayrton990/android_kernel_xiaomi_renoir)@[9a888e52f1...](https://github.com/Official-Ayrton990/android_kernel_xiaomi_renoir/commit/9a888e52f18322f652c65c3374288c409a50f97f)
#### Tuesday 2022-06-21 00:03:53 by Peter Zijlstra

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
## [Dragonkiller93/Paradise](https://github.com/Dragonkiller93/Paradise)@[6082c95eb3...](https://github.com/Dragonkiller93/Paradise/commit/6082c95eb300a9f05b5422060db79f55fe91b9b3)
#### Tuesday 2022-06-21 00:59:51 by LightFire53

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
## [Mooshimi/tgstation](https://github.com/Mooshimi/tgstation)@[9428d97a4f...](https://github.com/Mooshimi/tgstation/commit/9428d97a4fadf8a486b0c6fbe2ee345a2780e687)
#### Tuesday 2022-06-21 01:42:30 by Imaginos16

[MDB IGNORE] The Tilening V2 - Damaged Tile Overlays Edition (#67761)


About The Pull Request

Hello once more! As we near summer, I continued to reminisce on several PRs done throughout last year! One of them was the controversial, but rather positive Tilening V1, as done by me and Twaticus a while back (#58932), and felt I could've done a better job with how it was presented.

And thus, thanks to @Fikou encouraging me with a very interesting find of a previous tile resprite attempt, I've successfully done it!

Ladies and Gentlemen, I present to you all, Tilening Version Two!
image

Now this isn't your run of the mill tile resprite. While I did improve the appearance of several tiles I haven't touched last time (including the showroom/freezer tiles now), I decided to do something special that most mappers shall appreciate!

Don't you hate it when of all damaged states, there's only ones for grey tiles when we have white, black, terracotta and a bunch of other materials? Don't you wish they were overlays instead?

Well golly gee do I have good news for you!
image
image

After painstakingly spending at least several hours trying to learn enough code to pull it off, I have successfully made it so most tiles display transparent versions of damage overlays over them! This means mappers can express their creativity that much better! And thanks to how the code is written, its super easy to snowflake certain tile types to make them use unique damaged states (looking at you wooden tiles), so fret not in that aspect.

Credits to:
@WJohn For actually making those damaged overlays! Wouldn't've done the PR if it wasn't for you.
@dragomagol, @RigglePrime and @LemonInTheDark for helping me out in a VC at 10 PM to 12 AM troubleshooting the code to make this improvement work!
Why It's Good For The Game

The shading is done better as compared to last time, making them feel more cubical and less like a pancake when seen from above! This PR also makes it so that we never ever have to touch damaged tiles ever again potentially, saving up some RSC regarding icons.

However, due to how damaged tiles are currently mapped in, rather than overlayed as I envision in the future, it'll require a PR by San to be merged later that should make it safe to remove these icons.
Changelog

cl PositiveEntropy, WJohnston, Dragomagol, LemonInTheDark, Riggle
imageadd: Resprites most variety of tiles into a better shaded version!
code: Damaged floors are now damaged overlays, meaning that most tiles should properly display a damaged state!
/cl

---
## [chokemeharder/css-exercises](https://github.com/chokemeharder/css-exercises)@[5ba7e30199...](https://github.com/chokemeharder/css-exercises/commit/5ba7e30199437774f9aa1147d5bd928d46604471)
#### Tuesday 2022-06-21 01:58:46 by chokemeharder

A bunch of commits, I'm fucking bad at remembering to do this while I'm so damn stressed.

---
## [danton-nlp/factual-beam-search](https://github.com/danton-nlp/factual-beam-search)@[8413a80ca7...](https://github.com/danton-nlp/factual-beam-search/commit/8413a80ca71d16e3d41cf035653a0cec8c2c494a)
#### Tuesday 2022-06-21 02:02:12 by Daniel Levenson

Correct some out-of-source annotations

* don't think these effect summary factuality

remaining annotations that were labeled intrinsic, even though they are
actually technically out of source from an NER perspective:

```bash
$ python audit_annotations.py
Using custom data configuration default
Reusing dataset xsum (/Users/daniel/.cache/huggingface/datasets/xsum/default/1.2.0/32c23220eadddb1149b16ed2e9430a05293768cfffbdfd151058697d4c11f934)
100%|███████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 144.84it/s]
count of out-of-source possible bad annotations: 8
count of in-source possible bad annotations: 0
count of total summaries annotated: 708
---
IN SOURCE POSSIBLE BAD ANNOTATIONS
set()
---
OUT OF SOURCE POSSIBLE BAD ANNOTATIONS
{ ( '30457745',
    'Ghanaian duo The Busy Twist have released a new dance track called '
    "'Dance, Dance, Dance' which they say has captured the spirit of the "
    'country.',
    '{"ent": "Ghanaian", "type": "NORP", "start": 0, "end": 8, "in_source": '
    'false, "label": "Intrinsic Hallucination"}'),
  ( '30457745',
    'With the release of their latest single, The Busy Twist, Ghanaians Ollie '
    'Williams and Ohene Agyapong decided to take their music to the streets of '
    'the capital Accra.',
    '{"ent": "Ghanaians", "type": "NORP", "start": 57, "end": 66, "in_source": '
    'false, "label": "Intrinsic Hallucination"}'),
  ( '30760966',
    "The drugs expert at the centre of the'superman' ecstasy scandal has told "
    'the Global Drugs Survey it\'s "not safe" to take pills with the logo on '
    'them.',
    '{"ent": "the\'superman", "type": "WORK_OF_ART", "start": 34, "end": 46, '
    '"in_source": false, "label": "Non-hallucinated"}'),
  ( '33262593',
    'A World War Two fighter jet that was used in the Gulf War has been put up '
    'for sale by two ex-RAF engineers.',
    '{"ent": "World War Two", "type": "EVENT", "start": 2, "end": 15, '
    '"in_source": false, "label": "Intrinsic Hallucination"}'),
  ( '34474416',
    'A migrant camp set up at Dismaland has been moved after organisers '
    'decided not to send it to the UK.',
    '{"ent": "UK", "type": "GPE", "start": 97, "end": 99, "in_source": false, '
    '"label": "Intrinsic Hallucination"}'),
  ( '35723757',
    'Two British tourists have been arrested at the Machu Picchu '
    'archaeological site in Peru, police say.',
    '{"ent": "Two", "type": "CARDINAL", "start": 0, "end": 3, "in_source": '
    'false, "label": "Intrinsic Hallucination"}'),
  ( '35811486',
    'Byron Rhodes, the leader of Derbyshire County Council, is talking about '
    'seizing an opportunity in a crisis.',
    '{"ent": "Derbyshire County Council", "type": "ORG", "start": 28, "end": '
    '53, "in_source": false, "label": "Intrinsic Hallucination"}'),
  ( '39784504',
    'A Cornwall newspaper has accused the Conservatives of being "archaic" and '
    '"20th-Century in the way its journalists covered Prime Minister Mr  visit '
    'to the Cornish village of Helston.',
    '{"ent": "20th-Century", "type": "DATE", "start": 75, "end": 87, '
    '"in_source": false, "label": "Intrinsic Hallucination"}')}
```

---
## [downthecrop/2009scape-mirror](https://github.com/downthecrop/2009scape-mirror)@[ce14aa0e80...](https://github.com/downthecrop/2009scape-mirror/commit/ce14aa0e8094933c95ea0d33d28cd97e621fa275)
#### Tuesday 2022-06-21 03:10:06 by skelsoft

Over 30+ monsters with added sfx, tick respawn fixes, and stat corrections

Unicorn (ID 89, 987) Unicorn Foal (ID 1328) and Unicorn stallion (ID 6822, 6823) combat sfx added
Unicorn (ID 89) respawn delay corrected (90 ticks/54 seconds)
Unicorn Foal (ID 1328) stats, attack speed, and respawn delay corrected (90 ticks/54 seconds)
Black unicorn (ID 133) and Black unicorn foal (ID 1329) combat sfx added
Black unicorn (ID 133) stats, attack speed, and respawn delay corrected (90 ticks/54 seconds)
Black unicorn Foal (ID 1329) stats, attack speed and respawn delay corrected (20 ticks/12 seconds)
Angry unicorn (ID 3646, 3661) combat sfx added
Angry unicorn (ID 3646, 3661) stats and attack speed corrected
Rock Crab (ID 1265, 1267) and Giant Rock Crab (ID 2452, 2885) combat sfx added
Rock Crab (ID 1265, 1267) attack speed and respawn delay corrected (50 ticks/30 seconds)
Giant Rock Crab (ID 2452, 2885) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Ice giant (ID 111, 3072, 4685, 4686, 4687) combat sfx added
Ice giant (ID 111, 3072, 4685, 4686, 4687) respawn delay corrected (30 ticks/18 seconds)
Ice warrior (ID 125, 145, 3073) combat SFX added
Ice warrior (ID 125, 145, 3073) respawn delay corrected (30 ticks/18 seconds)
Basilisk (ID 1616, 1617, 4228) combat SFX added
Basilisk (ID 1616, 1617, 4228) stats, attack speed and respawn delay corrected (15 ticks/9 seconds)
Al-Kharid warrior (ID 18) combat sfx added
Al-Kharid warrior (ID 18) stats, attack speed and respawn delay corrected (25 ticks/15 seconds)
Magic axe (ID 127) combat sfx added, as well as its combat bonii corrected
Chaos dwarf (ID 119) combat sfx added
Black Knight (ID 178, 179, 6189) combat sfx added
Black Knight (ID 178, 179, 6189) stats, attack speed and respawn delay corrected (25 ticks/15 seconds)
Giant bat (ID 78, 1005, 2482, 3711) combat sfx added
Giant bat (ID 78, 1005, 2482, 3711) stats, attack speed, and respawn delay corrected (35 ticks/21 seconds)
Grizzly bear (ID 105, 1195) combat sfx added
Grizzly bear (ID 105) combat level 21 stats, attack speed, and respawn delay corrected (50 ticks/30 seconds)
Grizzly bear (ID 1195) combat level 42 stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Black bear (ID 106) combat sfx added
Black bear (ID 106) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Cave horror (ID 4353, 4354, 4355, 4356, 4357) combat sfx added
Cave horror (ID 4353, 4354, 4355, 4356, 4357) respawn delay corrected (50 ticks/30 seconds)
Jungle horror (ID 4348, 4349, 4350, 4351, 4352) combat sfx added
Jungle horror (ID 4348, 4349, 4350, 4351, 4352) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Hobgoblin (Spear-wielding) (ID 123, 2688, 4898) combat sfx added
Waterfiend (ID 5361) combat sfx added
Waterfiend (ID 5361 stats and attack speed corrected
Banshee (ID 1612) combat sfx added
Banshee (ID 1612) stats, attack speed and respawn delay corrected (15 ticks/9 seconds)
Angry bear (ID 3645, 3664) combat sfx added
Angry bear (ID 3645, 3664) stats and attack speed corrected
Seagull (ID 2707, 6115, 6116) combat sfx added
Ghast (ID 1052, 1053) combat sfx added
Icefiend (ID 3406, 6217, 7714, 7715) combat sfx added
Jackal (ID 1994) combat sfx added
Jackal (ID 1994) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Kalphite Soldier (ID 1154, 3589) combat sfx added
Kalphite Worker (ID 1153, 1156) combat sfx added
Vulture (ID 3675, 3676) combat sfx added
Vulture (ID 3675, 3676) stats, attack speed and respawn delay corrected (50 ticks/30 seconds)
Chompy bird (ID 1550) combat sfx added
Chompy bird (ID 1550) stats, examine, and poison immunity corrected
Minotaur (ID 4404, 4405, 4006) combat sfx added
Minotaur (ID 4404, 4405) stats, attack speed, examine, and respawn delay corrected (15 ticks/9 seconds)
Minotaur (ID 4006) combat level 27 stats, attack speed, examine, and respawn delay corrected (15 ticks/9 seconds)
Penance Fighter (ID 5040) combat sfx added
Skeletal Wyvern (ID 3068, 3069, 3070, 3071) combat sfx added (TODO: attack sound check)
Harpie Bug Swarm (ID 3153) combat sfx added
Harpie Bug Swarm (ID 3153) stats, attack speed and respawn delay corrected (25 ticks/15 seconds)
Harpie Bug Swarm (ID 3153) now correctly attacks with Melee
Molanisk (ID 5751) combat sfx added
Molanisk (ID 5751) stats and attack speed corrected
Mudskipper (ID 3422, 3423) combat sfx added
Mudskipper (ID 3422) combat level 30 stats, attack speed and respawn delay corrected (10 ticks/6 seconds)
Mudskipper (ID 3423) combat level 31 stats, attack speed and respawn delay corrected (5 ticks/3 seconds)
Aberrant spectre (ID 1604, 1605, 1606, 1607) combat sfx added
Aberrant spectre attack speed corrected
Cave slime (ID 1831) combat sfx added
Cave slime (ID 1831) stats, poison amount, attack speed and respawn delay corrected (15 ticks/9 seconds)
Stag (ID 4440) combat sfx added
Stag (ID 4440) stats, attack speed and respawn delay corrected (90 ticks/54 seconds)
Terrorbird (ID 138, 139, 1751) combat sfx added
Terrorbird (ID 138, 139, 1751) stats, attack speed and respawn delay corrected (30 ticks/18 seconds)
Chaos Elemental (ID 3200) respawn delay corrected (100 ticks/60 seconds)
General Graardor (ID 6260) respawn delay corrected (150 ticks/90 seconds)
Sergeant Grimspike (ID 6265) Ranged Strength bonus corrected
Commander Zilyana (ID 6247) respawn delay corrected (150 ticks/90 seconds)
Starlight (ID 6248) attack speed and poison immunity corrected
Kree'arra (ID 6222) respawn delay corrected (150 ticks/90 seconds)
Wingman Skree (ID 6223) poison immunity corrected
Flockleader Geerin (ID 6225) poison immunity corrected
K'ril Tsutsaroth (ID 6203) poison amount and respawn delay corrected (150 ticks/90 seconds)
Zakl'n Gritch (ID 6206) ranged strength bonus corrected

---
## [Bungalow-13/Bungalow-13](https://github.com/Bungalow-13/Bungalow-13)@[8a977645a0...](https://github.com/Bungalow-13/Bungalow-13/commit/8a977645a0f4c6e1560405bc0acaa317f643a7e0)
#### Tuesday 2022-06-21 03:53:43 by projectkepler-RU

Blue helmets resprites (#777)

* gsdkfsldka

* blue helmet babey

* more reskin

* aaa

* blue helmete

* blue beret too :)

* the blue helmets :3

* I hate how hard my fucking life is

* now you have both :)

---
## [Ebin-Halcyon/Pariah-Station](https://github.com/Ebin-Halcyon/Pariah-Station)@[95db2c6bfc...](https://github.com/Ebin-Halcyon/Pariah-Station/commit/95db2c6bfc84871f2fa51eeef253f681dc46a632)
#### Tuesday 2022-06-21 05:39:29 by Kapu1178

Makes glass floors override platings. Fixes glass floor openspace bug. (#66301) (#696)

About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [Elijahrane/space-station-14](https://github.com/Elijahrane/space-station-14)@[949fbd0194...](https://github.com/Elijahrane/space-station-14/commit/949fbd019404b32fded90f37e3f6a7548790e55e)
#### Tuesday 2022-06-21 07:37:20 by Emisse

Bagel Update 13.7 (#8690)

* fuck shit ass shit

* Add files via upload

---
## [DiscordWizard/sojourn-station](https://github.com/DiscordWizard/sojourn-station)@[796aeaa98f...](https://github.com/DiscordWizard/sojourn-station/commit/796aeaa98f76c2a6ef7a94e540d3b8f7efcb027b)
#### Tuesday 2022-06-21 08:55:45 by lolman360

fixes stacks deleting randomly (#3357)

* whoo

* god i fucking hate stackcode

thank you kevinz

---
## [Callisto13/cluster-api-provider-aws](https://github.com/Callisto13/cluster-api-provider-aws)@[cd9af74f2f...](https://github.com/Callisto13/cluster-api-provider-aws/commit/cd9af74f2fa6b36efc27b500891b30b42dfa435b)
#### Tuesday 2022-06-21 08:58:16 by Claudia Beresford

Fail apidiff make target when git fails

The `apidiff` target runs 2 commands (piped) in an `if` which swallows
the exit code, meaning it never fails.

In the case of the `grep`, this is fine; we don't want it to error if
changes in "api" have not been found.

In the case of the `git diff`, we do care when that fails.

Unfortunately, this is a pain to do in a Makefile.

One option was to move bits into another `.sh` script (not the
`scripts/ci-apidiff.sh` one as that would make the target pointless).

Another option is to fork the `go-apidiff` command so that we can make
it only run on the `api/` dir, since that is all we care about. This
does somewhat go against what the tool is for (it assumes use of an
`internal/` package to skip scanning of certain packages), but since we
only run this tool when there is a change in `api/`, this is clearly all
we care about so it makes sense for us.

In this PR I have therefore switch to using a modified fork of the tool.

------

In the case of `$(APIDIFF_OLD_COMMIT)`, there is some annoying `make`
magic going on here. Which I can't simply make fail since it will cause any
job which uses something in this Makefile to fail out of proximity.
The `shell` is expanded when the file is loaded meaning even targets
which do not care about the value will end up erroring (but not exiting)
when it fails. These are not errors which impact the target's run, but
they look annoying in CI.

Since this var is only used by `apidiff`, we can move it into that
target so it is only evaluated when specifically called.

---
## [Callisto13/cluster-api-provider-aws](https://github.com/Callisto13/cluster-api-provider-aws)@[a937ab7e90...](https://github.com/Callisto13/cluster-api-provider-aws/commit/a937ab7e90ce2cbb028aa0a1eb5ae3b877dfdba0)
#### Tuesday 2022-06-21 09:11:43 by Claudia Beresford

Fail apidiff make target when git fails

This is a fairly simple fix to ensure that when `git diff` fails on the
`make apidiff` target, the exit code is actually picked up by make.
Previously the exit code from `diff` was "swallowed" by the `if`.

eg:
```
$ cat Makefile
thing:
        if (exit 1); then \
		echo foo; \
        fi
        echo "still here"

$ make thing
still here
$ echo $?
0
```

What we want:
- exit 1 when `git diff` fails
- exit 0 when `grep` fails
- call `go-apidiff` when `git diff` and `grep` succeeds
- exit 1 when `go-apidiff` fails

This is honestly a complete pain to do in a Makefile.

I tried capturing output, moving everything to a script, calling from
one thing to another. But really this is just tricky to do the way we
want in Make.

So, if we can live with a little repetition, we can do the following:
- Check the `git diff` can run, exit 1 if not
- Run the `git diff` again, this time piping the successful command to
  `grep`
- If `grep` fails, then no worries, the target will roll on and exit 0
  like it always has.
- If `grep` succeeds then the `go-apidiff` tool is called and the target
  runs as intended.

------

In the case of `$(APIDIFF_OLD_COMMIT)`, there is some annoying `make`
magic going on here. Which I can't simply make fail since it will cause any
job which uses something in this Makefile to fail out of proximity.
The `shell` is expanded when the file is loaded meaning even targets
which do not care about the value will end up erroring (but not exiting)
when it fails. These are not errors which impact the target's run, but
they look annoying in CI.

Since this var is only used by `apidiff`, we can move it into that
target so it is only evaluated when specifically called.

---
## [abhishek1994-ux/-MyCloudDiary](https://github.com/abhishek1994-ux/-MyCloudDiary)@[68ddd3b834...](https://github.com/abhishek1994-ux/-MyCloudDiary/commit/68ddd3b834d73477bf85301a6cba60157c423590)
#### Tuesday 2022-06-21 09:27:26 by Abhishek Shrivastava

LEAD-3 

Happy to announce another feather added in #MyCloudDiary :: https://lnkd.in/dHAMiTcH  journey 🎉🎉..

Please like ,share and subscribe below #channelpartners on 
YouTube :: https://lnkd.in/dDaZPGR5
GitHub :: https://lnkd.in/dHAMiTcH
Hashnode :: https://lnkd.in/d_gtGxuS
Twitter :: https://lnkd.in/e5ZY5j-x
Dev Community TLV :: https://lnkd.in/duMEcSnc
Tealfeed :: https://lnkd.in/eTyp-Xe4
Medium :: https://lnkd.in/dpEzM8GU

Good teachers like you aren’t always the ones who have fancy degrees and qualifications. They are the ones who have a big heart and a burning desire to make the world a better place, one kid at a time. Thank you Mahesh Bhosale to take stand for me always ..👏

As new year started with new #Cloud calendar, it’s time to look back and reflect on the past 30 months. Thank you for all your commitment, and invaluable contributions , integral to our progress and success. ❤️❤️

This year, I 've to made impressive progress in my business goals, constantly and rapidly evolving against the backdrop of a very competitive trading environment. Despite all the challenges, our team upheld their focus and let not one opportunity go.

There is still plenty of achievable lined up for every year, and I am sure that we will keep up with our excellence.

Thank you once again for your commitment and invaluable contributions toward helping me to reach its full potential.🎓

Thanks to Osvaldo Cantu Sabahat Siddiqui to encourage always with his booster words and recognition ..A teacher affects eternity: he can never tell where his influence stops. 🙏🙏

Special thanks to Harsh Mahajan Joyson Das Sumeet Kakkar to design wonderful 10 week LEAD 3 program.

Adding leaders - Kat Hopkins Susan Cutinha

Thanks to #teammates who always supporting to each other and support me to drive challenge and help to achieve target. ❤️❤️

CC- Adding my leaders and colleagues to share achievement::
Pritish Kumar Swapneel Doshi Girish Chhabra Murli Reddy Rakesh Khanna Sohil Shah Kaviarasu Subramaniam PMP CSM SAFe 4 Certified Agilist EUR ING Ioannis Kolaxis MSc Chris Broccoli Sujay Puthran Dinesh Damodaran Jenniffer A Anand Kombe, ITIL®, Scrum(F) Konrad Cłapa, Google Cloud Certified Fellow Sophie Proust Sathya Prasad Nanjundaiah Rajeev Choudhary Janusz Marcinkowski Nourdine Bihmane Srinivas Sayani Srini Gummadavelly Snehal Shah Marc Veelenturf Belmer Rodolphe Ashwini N 

#Atos #Lead3 #leadership #atosart2022 #IEEE #knowledge #technology #innovation #sciences  #atosteam #atossyntel #atosonecloud #atosmedia #appreciationpost #appreciation #achievementunlocked #achievements #thanksforeverything  #thankyou #opportunity #success #community #business #design #scrum #leaders

---
## [Vitorgl2003/kernel_xiaomi_lavender_rave](https://github.com/Vitorgl2003/kernel_xiaomi_lavender_rave)@[4dedd24a0a...](https://github.com/Vitorgl2003/kernel_xiaomi_lavender_rave/commit/4dedd24a0af52d6b75ffae7fb41c913c518259b8)
#### Tuesday 2022-06-21 11:01:12 by Maciej Żenczykowski

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
Signed-off-by: Vitorgl2003 <vitorgl.2003@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[136062c416...](https://github.com/mrakgr/The-Spiral-Language/commit/136062c4169ca23fcbf490ba6c51d7f2f32e2895)
#### Tuesday 2022-06-21 12:10:54 by Marko Grdinić

"9:25pm. I just watched the last ep of Estab Life. I missed the /a/ thread and forgot about it. 10/10 anime. I downloaded it a few days ago, but I didn't watch the last episode earlier because I didn't want it to end. Let me take a look at the /a/ thread in the archive.

11:40pm. https://youtu.be/1eFq21yT1vE?t=5476
GENSHIN CONCERT 2021 《Melodies of an Endless Journey》

Oh, this part is great.

https://semianalysis.substack.com/p/nvidia-hacked-a-national-security

Right now I am reading this.

> The release of complete Verilog data would be a complete disaster for Nvidia and western national security. In essence, the blueprint of these chips, the product of a $580 billion company and $30 billion of research and development could be in the hands of hostile actors. The hacked data, which could have been sold to a nation-state actor, could very well prove the most strategically significant act of corporate espionage in a generation. With direct access to designs of the world's most advanced GPUs and AI processors, Chinese design firms could be able to dramatically increase the speed with which they catch up to their western competitors in all fields related to artificial intelligence and semiconductors. If, on the off chance that this data is not already in China's hands, the US Government should mobilize its cybersecurity arsenal to prevent PRC firms' ability to access this data. This intellectual property must be defended.

This all is good news to me as a consumer. China getting better at the AI game means I'll get access to the AI chips sooner rather than later. Based Lapsus.

https://semianalysis.substack.com/p/tenstorrent-blackhole-grendel-and

This site has interesting stuff.

> Tenstorrent also made a very bold claim that there shouldn’t be datacenter machine learning companies or edge machine learning companies, but instead what’s needed are end-to-end machine learning companies. Tenstorrent believes there are strong compatibility dynamics between training future looking neural networks and running the inference for them.

Honestly, it feels like the only company doing anything interesting in the AI chip space is TensTorrent.

> We did a deep dive into the predecessor, Jawbridge, as well as Grayskull, and Wormhole in our article last year. Grayskull is the second-generation chip and is built on GlobalFoundries 12nm. Tenstorrent claims this chip is the same performance as Nvidia’s A100 GPU with twice the density and slightly lower power. We have heard from a large hyperscaler that evaluated Grayskull, that it’s a decent bit slower than Nvidia’s 4.5-year-old V100.

Oh, no AI chip bros. Months ago, I read that Graphcore is also struggling to compete against NVidia.

> In the end, while the software story sounds nice, it is a big wait and see. The same applied to the hardware in fact. The claims about being designed for scale out from the ground up and beating Nvidia on perf are great, but they need to be materialized. The philosophy behind the company and their decisions in hardware and software are exciting, so we are hopeful. If this start-up shows real promise, we believe AMD should acquire them. AI and software chops are pretty much the only things AMD is still missing after their resurgence against Intel and acquisitions of Xilinx and Pensando.

https://semianalysis.substack.com/p/why-america-will-lose-semiconductors
> SemiEngineering.com, one of the leading publications in the semiconductor industry, tracks monthly semiconductor and semiconductor adjacent industry startup fundraising by company headquarters location. Their data is compiled in the table below for May, but other months look very similar. This trend is terrifying for prospects of American hardware dominance. Not only is most of the assembly done in China, but the most well-funded startups in the semiconductor field and the most IPOs in the semiconductor field are occurring there well.

https://www.lesswrong.com/posts/xwBuoE9p8GE7RAuhd/brain-efficiency-much-more-than-you-wanted-to-know

I remember this guy's name, he made some good efficiency posts in the past on this very site. Let me just skim it now.

> If we only knew the remaining secrets of the brain today, we could train a brain-sized model consisting of a small population of about 1000 agents/sims, running on about as many GPUs, in probably about a month or less, for about $1M. This would require only about 1kW per agent or less, and so if the world really desired it, we could support a population of billions of such agents without dramatically increasing total world power production.

This is from the conclussion.

1:25am. > The limits of Moore's Law are fairly well known in the device physics research community - and there really isn't multiple OOM of transistor energy efficiency left, we are already pretty close. Moving to neuromorphic/PIM can provide some OOM advantage, but it's one-time. Continuation of Moore's Law style growth will soon require exotic computing - reversible/quantum.

This is from one of the comments.

> The end of Moore's Law is actually a series of incomplete barriers, each of which only allows an increasingly narrower computational design to scale past that barrier: dennard scaling blocked serial architectures (CPUs), next up the end of energy scaling will block von-neumman arch (GPUs/TPUs), allowing only neuromorphic/PIM to scale much further, then there is the final size scaling barrier for all reversible computation, and only exotic reversible/quantum computers scale past that.

I need to remember to link to this tomorrow.

> If this post piqued your interest, I’d highly recommend Principles of Neural Design as an overview of our current knowledge of the brain. It starts from a bottom level of energy conservation and information theoretical limits, and builds on that to explain the low-level structures of the brain. I can’t claim to follow all the chemistry, but it did hammer home that the brain as far as we can tell is near maximally efficient at its jobs.

> I'm reasonably well read on reversible computing. It's dramatically less area efficient, and requires a new radically restricted programming model - much more restrictive than the serial to parallel programming transition. I will take and win any bets on reversible computing becoming a multi-billion dollar practical industry before AGI.

Actually, I had not known this. This is new to me. Good stuff.

6/21/2022

10:35am. I need to remember to link the above, both in the halfly review and today's post. Yesterday I only skimmed the article by Jacob, I actually feel like reading it all the way through today.

11:10am. Let me dedicate some time to read the article properly. After that I'll get started on the scene.

> A 2021 GPU with 10^10 transistors has a surface area of about 10^14 nm^2 and so also potentially has room for at most 100x further density scaling, which would result in 10,000x higher transistor count, but given that it only has 1 or 2 OOM potential improvement in thermodynamic energy efficiency, significant further scaling of existing designs would result in untenable power consumption and surface temperature. In practice I expect around only 1 more OOM in dimension scaling (2 OOM in transistor density), with less than an OOM in energy scaling, resulting in dark silicon and or crazy cooling designs[23:1].

> So in the same brain budget of 10W power and thermodynamic size constraints, one can choose between a computer/circuit with 10^14  bytes of param memory and 10^14 byte/s of local memory bandwidth but low sub kHZ speed, or a system with up to 10^14 bytes/s of local memory bandwidth and gHZ speed, but only 10^8 bytes of local param memory. The most powerful GPUs or accelerators today achieve around 10^14 bytes/s of bandwidth from only the register file or lowest level cache, the total size of which tends to be on order 108 bytes or less.

> A single 2021 GPU has the compute power to evaluate a brain sized neural circuit running at low brain speeds, but it has less than 1/1000th of the required RAM. So you then need about 1000 GPUs to fit the neural circuit in RAM, at which point you can then run 1000 copies of the circuit in parallel, but using multiple OOMs more energy per agent/brain for all the required data movement.

10^15 is 1,000 terabytes or 1 petabyte.

> Conclusion: The brain is a million times slower than digital computers, but its slow speed is probably efficient for its given energy budget, as it allows for a full utilization of an enormous memory capacity and memory bandwidth. As a consequence of being very slow, brains are enormously circuit cycle efficient. Thus even some hypothetical superintelligence, running on non-exotic hardware, will not be able to think much faster than an artificial brain running on equivalent hardware at the same clock rate.

> Conclusion: It's difficult to make strong definitive statements about circuit efficiency, but current evidence is most compatible with high brain circuit efficiency, and I'm not aware of any significant evidence against.

11:55am. I am done with the article. I went to bed a bit too late yesterday and I can't follow it properly right now, but I'll just take the conclussions at face value. It does not matter anyway as I am not designing AI chips myself. I just want to program them and find a way of learning beyond SGD.

12:05pm. I've started, but I am not sure how to organize my assets.

https://www.youtube.com/results?search_query=blender+view+layer

Can I do some modeling in Blender on a separate view layer?

https://youtu.be/jOO3K1B9vgg
Blender 2.8 Beginner Tutorial : Collections, View Layers and render layers

12:10pm. https://youtu.be/jOO3K1B9vgg?t=198

This is interesting behavior. I had no idea you could do this in Blender. Still, how do I unlink from a collection? If I delete on one side, it removes it from both.

https://docs.blender.org/manual/en/latest/scene_layout/collections/collections.html#collections-menu
Ctrl + Alt + G

This is what I need. But I wonder if there is a way of doing this from the outliner? Nevermind that for now.

https://youtu.be/jOO3K1B9vgg?t=576

Oh, I see. I thought that view layers would have separate collections, but I guess not. Yeah, I should be able to make use of this.

Found a rare crash in Blender when I unlinked a render layer.

https://youtu.be/jOO3K1B9vgg?t=769

Ohhh, Flickr could be a good resource for free photos!

12:40pm. That was informative. I'll definitely be making good use of render layers. But what about scenes?

https://www.youtube.com/results?search_query=blender+scenes

Let me have breakfast here and then I'll watch the scenes tutorials. They are quite short.

2pm. Let me resume. I seem to be going in cycles of sleeping well one day, and being tired the other. I have nobody, but me to blame for this. At least I'll sleep well tonight. But now let me focus on art. Once I really start I will get into it.

It is really important that I learn to orgnize my projects correctly. My past projects are all strewn about across many files and folders. I have no idea how this happened, but I've been getting better at this in the last few weeks.

Once things are organzied on the hard drive, they'll be organized in my mind.

It is really a pity about Clarisse, I put in a lot of effort in studying it, but I'll stick with Blender. If the program didn't crash so often and had better navigation, or at least navigation closer to Blender, I could hve justified working in it. Blender is pretty decent. Clarisse is good at displaying a lot of geometry on the screen, but Blender can do that too if I take care of the viewport.

If I use gygabite assets, no amount of tricks that Clarisse does will be enough.

I do not need movie level quality. Once I upgrade my rig, I'll consider upgrading my art. For now, let me go low-mid poly.

2:10pm. Now focus me. Let me watch some scene tutorials."

---
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[bcbb3a40e0...](https://github.com/canalplus/rx-player/commit/bcbb3a40e09140a50dc664c7003551ee3f363bb9)
#### Tuesday 2022-06-21 13:41:48 by Paul Berberian

Update most dependencies but Jest

This commit update almost all dependencies but jest.

This is because Jest 28 seems to break while running code, presumably
due to `import`/`export` declarations in imported RxJS files (but I do
not think RxJS is at fault here) that lead to an `unexpected token` when
running through Jest.

You could think that the fault is linked to node not understanding
`import`/`export` (linked to CommonJS/ES6 import shenanigans) but it is
even trickier than that as Jest already performed some JavaScript
transformation at that point, which made the import/export inside an
IIFE - and I'm not sure that this is supported anywhere.

After taking ~a day (much more time than I should) trying to play around
to remove that issue, I gave up and avoided updating Jest to its v28.

In the future, I guess we should either:

  - understand what we're supposed to do here to make it work with Jest
    28 (Jest documentation was poor - even without considering the
    sometimes incomprehensible google-translated french one I get each
    time by default on their docusaurus-based documentation)

    Opened GitHub issues were 100% for angular-based applications - as it
    seems the RxJS+TypeScript cocktail is very majoritarily those. Those
    have their own "fix" through another magical angular dependency.

    Moreover, it does not help that Jest's philosophy seems to be trying to be
    extremely simple for users at the cost of some complex behaviors (as an
    example, it looks like it auto-picks a `babel.config.js` file if it
    sees one at the root of the project. If like us you have multiple build
    files at the root depending on the building context, it is not a good
    idea to silently pick random files like that by default).

    I couldn't understand under an acceptable time where the issue was - and
    at which step it happened.
    I just browsed dozens of doc pages, GitHub and StackOverflow issues
    which just proposed to add yet other automagic dependencies (looked like a
    parody of what JavaScript haters talk about!) - which all seemed to have
    no effect whatsoever.

    I also asked for help from other teams at Canal+, but those in the
    same situation (TypeScript and RxJS) also seem to have random issue
    preventing them from doing the switch.

  - Remove RxJS from the code. It's presumably not its fault yet we
    already started doing that, so maybe we'll just raise the jest
    version once RxJS is definitely removed from the RxPlayer.

  - Wait for some kind of Jest fix or new way of handling those?

  - Remove Jest and go with another testing framework.

    I almost did that due to being fed-up with Jest, but it might no be
    as easy as it seems, mostly the module-mocking part as I'm unsure of
    how other framework handle that now and if it is as convenient as
    Jest's way.

---
## [RocketChat/Rocket.Chat](https://github.com/RocketChat/Rocket.Chat)@[5a37518e42...](https://github.com/RocketChat/Rocket.Chat/commit/5a37518e42dec114e0ed1a71b5d103b4a62e9b58)
#### Tuesday 2022-06-21 14:03:58 by Ben Wiederhake

[FIX] Client-generated sort parameters in channel directory  (#25768)

## Proposed changes (including videos or screenshots)
- In the web-client, sorting the channel directory by "Last Message" raises the error "Invalid sort parameter provided".

I don't think a screenshot is necessary, but if you'd like one anyway, here it is:

![Bildschirmfoto_2022-06-06_12-54-34](https://user-images.githubusercontent.com/2690845/172147996-e9942daf-6819-4eee-afa4-b1c6bce7a650.png)


## Issue(s)
Closes #25695

## Steps to test or reproduce

- Open the web client, i.e. navigate your browser to `https://rocketchat.$DOMAIN/home`
- Click the "Directory" button in the top left, (or just navigate directly to `https://rocketchat.$DOMAIN/directory/channels`)
- In the table header, click on "Last message" once
- In the table header, click on "Last message" again

Expected behavior: Clicking "Last message" turns on and then toggles sorting by the date of the last message, either first ascending and then descending, or the other way around.

Actual behavior: The first click sorts the messages in ascending order (good!), the second click shows a red warning box "FIXME", the table content disappears, and is replaced by throbbing grey placeholders.

### "Good" request (ascending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A1%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":1}
count | 25
```

Response:
```
{"result":[{"_id":"AAAAAAAAAAAAAAAAA","name":"foobar","fname":"foobar","t":"c","usersCount":10,"ts":"2019-01-01T00:00:00.000Z","default":false,"lastMessage":{"_id":"AAAAAAAAAAAAAAAAA","rid":"AAAAAAAAAAAAAAAAA","msg":"Hello, World!","ts":"2019-01-01T00:00:00.000Z","u":{"_id":"AAAAAAAAAAAAAAAAA","username":"normaluser","name":"normaluser"},"unread":true,"_updatedAt":"2019-01-01T00:00:00.000Z","urls":[],"mentions":[],"channels":[]},"description":"Obviously, this JSON response is heavily censored."}],"count":25,"offset":0,"total":52,"success":true}
```

(Obviously, this JSON response is heavily censored, but you get the gist: It was successful.)

### "Bad" request (descending order):

`https://rocketchat.domain.org/api/v1/directory?query=%7B%22type%22%3A%22channels%22%2C%22text%22%3A%22%22%2C%22workspace%22%3A%22local%22%7D&sort=%7B%22lastMessage%22%3A0%7D&count=25`

More easily readable GET parameters:

```
query | {"type":"channels","text":"","workspace":"local"}
sort | {"lastMessage":0}
count | 25
```

Response:
```
{"success":false,"error":"Invalid sort parameter provided: \"{\"lastMessage\":0}\" [error-invalid-sort]","errorType":"error-invalid-sort","details":{"helperMethod":"parseJsonQuery"}}
```

## Further comments

Version on the server where I noticed this: `https://rocketchat.$DOMAIN/api/info` returns `{"version":"4.8","success":true}`. According to the "Releases" page, this version appeared 5 days ago, so I believe this is up to date.

### The journey to here

For some reason, the descending order uses the wrong magic number "0", and the server can't interpret that. However, this *used* to work, so I'm not very sure about this.

The error message appears in the source code of the entire organization exactly once: https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L42
So I'll guess that this is the line of code that generated this particular message.

A few lines above we see that the server only knows 1 and -1 as magic numbers for the sorting:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/app/api/server/helpers/parseJsonQuery.ts#L35
This matches the observed bug: The browser sends 1 (which works) and 0 (which doesn't work).

Generally, it seems that the web client actually uses the strings "asc" and "desc" internally, which are hard to mix up. So I assume that it's the conversion of that is broken somehow.

Exactly this seems to be the case here:
https://github.com/RocketChat/Rocket.Chat/blob/31ae30f30ad71d9e5a1b0cad494b3471a7dd8807/apps/meteor/client/views/directory/hooks.js#L11

The code around it produces exactly the kind of query seen in the network log, and can also produce the buggy parameter `sort: 0`. This either fixes bug #25695, or a different bug of the same kind.

I am not sure how to add tests for this, can someone do this for me or show me where to start? I'm actually just an end-user and "accidentally" found the fix for the bug while writing the bug report ^^'

EDIT: Rebased for convenience, and to re-check CI.

---
## [twome/dein.vim](https://github.com/twome/dein.vim)@[acc6cde09e...](https://github.com/twome/dein.vim/commit/acc6cde09e5d748913d0b490d5a82e313338f408)
#### Tuesday 2022-06-21 14:34:17 by Tom Kenny

Add "Deno-" to "powered"

I noticed you had the same phrase in other similar projects. When I'd looked at this project years ago, I had thought the phrase "dark powered" meant "powered by darkness", which I remember striking me as unusually mystical for a software project description, hahaha! This is also missing from the the small "about" section, but I can't edit that ;)

---
## [haggis-aerospace/HaggisAero2021-22](https://github.com/haggis-aerospace/HaggisAero2021-22)@[f7d9d3b3ae...](https://github.com/haggis-aerospace/HaggisAero2021-22/commit/f7d9d3b3aeebc9d2c41ea0251ac9439fac120fd7)
#### Tuesday 2022-06-21 15:13:48 by Maksim

fixed the part last added (tail to wing connector small)

Yo, Big Shaq, the one and only
Man's not hot, never hot
Skrrat (GottiOnEm), skidi-kat-kat
Boom
Two plus two is four
Minus one that's three, quick maths
Everyday man's on the block
Smoke trees (Ah)
See your girl in the park
That girl is a uckers
When the ting went quack-quack-quack
You man were ducking (You man ducked)
Hold tight, Asznee (My brudda)
He's got the pumpy (Big ting)
Hold tight, my man (My guy)
He's got the frisbee (Shew)
I trap, trap, trap on the phone
Movin' that cornflakes (Uh)
Rice Krispies
Hold tight, my girl Whitney (My G)
On, on, on, on, on the road doin' ten toes
Like my toes (Like my toes)
You man thought I froze
I see a peng girl, then I pose (Chilin')
If she ain't on it, I ghost
Hah, look at your nose (Check your nose, fam)
You donut
Nose long like garden hose
I tell her man's not hot
I tell her man's not hot
The girl told me, "Take off your jacket"
I said, "Babes, man's not hot" (Never hot)
I tell her man's not hot (Never hot)
I tell her man's not hot (Never hot)
The girl told me, "Take off your jacket"
I said, "Babes, man's not hot" (Never hot)
Hop out the four-door with the .44
It was one, two, three and four (Us, man)
Chillin' in the corridor (Yo)
Your dad is forty-four (Uh)
And he's still callin' man for a draw (Look at him)
Let him know
When I see him
I'm gonna spin his jaw (Finished)
Take man's Twix by force (Take it)
Send man's shop by force (Send him)
Your girl knows I've got the sauce (Flexin')
No ketchup (None)
Just sauce (Saucy)
Raw sauce
Ah, yo, boom, ah
The ting goes skrrrahh (Ah)
Pap, pap, ka-ka-ka (Ka-ka)
Skidiki-pap-pap (Pap)
And a pu-pu-pudrrrr-boom (Boom)
Skya (Ah)
Du-du-ku-ku-dun-dun (Dun)
Poom, poom
You don' know
I tell her man's not hot (Man's not)
I tell her man's not hot (Never hot)
The girl told me, "Take off your jacket"
I said, "Babes, man's not hot" (Never hot)
I tell her man's not hot
I tell her man's not hot (Never hot)
The girl told me, "Take off your jacket"
I said, "Babes, man's not hot"
Man can never be hot (Never hot)
Perspiration ting (Spray dat)
Lynx Effect (Come on)
You didn't hear me, did you? (Nah)
Use roll-on (Use that)
Or spray (Shhh)
But either way, A-B-C-D (Alphabet ting)
The ting goes skrrrahh (Ah)
Pap, pap, ka-ka-ka (Ka)
Skidiki-pap-pap (Pap)
And a pu-pu-pudrrrr-boom (Boom)
Skya (Ah)
Du-du-ku-ku-dun-dun (Dun)
Poom, poom
You don' know
Big Shaq
Man's not hot
I tell her man's not hot (Never hot)
40 degrees and man's not hot (Come on)
Yo, in the sauna
Man's not hot (Never hot)
Yeah, skidika-pap-pap

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0bf9d0c3e4...](https://github.com/treckstar/yolo-octo-hipster/commit/0bf9d0c3e413f0b6dd290d3d52010185084fc22b)
#### Tuesday 2022-06-21 16:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [tiiuae/nixpkgs-spectrum](https://github.com/tiiuae/nixpkgs-spectrum)@[040966d95d...](https://github.com/tiiuae/nixpkgs-spectrum/commit/040966d95d6e00e03cca32de76120b1192f11d45)
#### Tuesday 2022-06-21 16:27:44 by Wouter den Breejen

This is a quote from http://www.johannes-bauer.com/xpdf/xpdf.php, any moral issues can be posted on the mailing list ;) "If you are the proud owner of a proprietary PDF-Creator like "Adobe Acrobat" you probably have noticed that it gives you the option to make the resulting PDF protected in a way that you cannot copy any text from it or that you cannot extract the pictures within. What a nice little feature. Now what this technically does is to set a flag in the PDF telling the reader program "Please don't let the mean user copy any content from me! ". However, the whole process relies on the reader progam (like "Adobe Acrobat Reader" or "xpdf", in our case) to obey the request of the PDF creator. Now at this point, xpdf really pissed me off. Because it really does obey the completely non-sensical request of the PDF creator. Probably because of some legal trouble which Adobe might give them if they did not obey it. But logically there is absolutely no reason to restrict the extraction of text of graphical images from a PDF file. Text I could read and type it in again. Pictures I could photograph off my PC screen. It's completely moronic. It's Adobe. Plus some people at my college think it's protecting their documents well. They seem to believe that content which is made for education should under no circumstances leak to the outside - somebody could maybe learn something! It would be a disaster! It is obvious they're morons. This patch just proves my point."

svn path=/nixpkgs/trunk/; revision=9765

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[d7400c7573...](https://github.com/mrakgr/The-Spiral-Language/commit/d7400c757338a4fbe35b840132f4139657522a2f)
#### Tuesday 2022-06-21 17:55:53 by Marko Grdinić

"https://youtu.be/xD0uAqi3jF8
Blender 2.8 Basics Tutorial: Scenes & Management

2:20m. I watched the above. But how would I move assets between the scenes? Nevermind that for now. I'll make it a priority to figure it out.

https://youtu.be/pr6YlbELAuA?t=18
Compositing With Multiple Scenes In Blender

Let me watch this.

2:50pm. Ok, I figured out how to move assets between scenes. I am not sure how it could be done in the past versions, but right now it is really easy to do through the asset browser.

2:55pm. Using Ctrl + L I can link an object into a new scene, after which I'd need to duplicate object properties.

https://youtu.be/r7G13NPvXuc
How to link Blender scenes, data blocks and library overrides (2020)

Let me watch this to seal the deal. After that I'll watch the Nvidia video on large scenes.

3pm. Had to do some chores. Let me resume.

https://youtu.be/r7G13NPvXuc?t=56

Yeah, this is what I figured.

View layers and scenes are really vital. I regret not learning about them as well as the asset browser earlier. It would have only taken me a day.

3:05pm. https://youtu.be/qZWGDt61Y_0
Making a Photorealistic 3d Portrait (from scratch)

This lured me. It is not what I wanted to watch, but let me check it out.

3:15pm. https://youtu.be/IJC8Xzwiulw
Top Blender Tips for Large Scale Environment Creation w/ James Tralie

What I wanted to watch was this.

https://youtu.be/IJC8Xzwiulw?t=86

Let me take a short break here.

3:45pm. That took long. Let me resume. I am starting to get into it.

https://youtu.be/IJC8Xzwiulw?t=120
> Unsplash.

I need to remember that site along with Flickr.

https://youtu.be/IJC8Xzwiulw?t=215

Ah, so this is how you activate those. Let me check them.

https://youtu.be/IJC8Xzwiulw?t=1002

Emission shader for doing volumetrics.

4:15pm. This wasn't useful, I haven't learned much I hadn't known before. But one vid is not going to kill me. It is time to get started. To start things off, how about I do a small city. Forget big and impressive. I'll increase the scale later. Right now what I should do is put the basic scene together.

4:40pm. I did a basic fence for the platform.

Right now, why don't I throw up some buildings? I'll make a small and a big one as basic cubes. Then I will scatter them around. This will be a good opportunity to get a handle on the Scatter plugin. After what I'll focus on is setting up the overall frame. I originally focused on a shot of the city from below, but given the perspective, the city did not even show up in the image at all. Instead it ended up being an UFO in the distance. This is what convinced me to ditch Clarisse - because it would be way too much of a hassle to have to deal with those big assets before the basic setup has been made.

One thing I could do is go for a very non-realistic shot. It is like how the cover has a fake sun going over the horizon while the actual this is off in the distance.

What I could do is rotate the city as if it were falling, so the camera can see it from the top. And bring it a lot closer.

I thought of having it glow from below as well as have also a bunch of shinning blocks around it, but that kind of setup would mess things up.

4:50pm. I'll go for a non-realistic scene. I'll rotate the platform as in my original vision. I thought that having a view of the earth from above from the city would be too much in the cover, but this will work fine. I'll composit the scenes together.

4:55pm. Yeah, it is decided. Two scenes rolled into one non-realistically. It will be a piece of cake to do this. Let me focus on modeling some buildings.

5:05pm. Collection instances are awkward as they don't have proper pivots.

https://blenderartists.org/t/how-do-you-control-the-origin-point-of-collection-instances/1258099

> Parent everything to an empty end put the empty into the collection. The empty will be the origin of the instance.

Hmmm, really? Will this work?

Edit: I figured it out. It turns out you can set the 3d cursor to somewhere and then set the collection origin to that. It is annoying to move the collection after that though because the origin won't update.. But it makes more sense to do it like this than join everything into one object. It does not require to apply the object mods for one.

5:45pm. How annoying. But I've done the very basic low-poly props.

I do not think I am suitable for being an artist given how long the simplest of things take me.

But I'll get the illustration done at least. I have 4 buildings with either roofs or some props on a flat plane. No windows or doors on them yet.

5:50pm. They are all organized neatly in a second scene. Oh, let me mark the buildings as assets.

Ah, whops, I forgot to set the collection offset for the buildings. Silly me.

6:10pm. The asset browser is going haywire on the platform, I can't use it at all properly on it. Maybe 1km x 1km was too much. At any rate, this is finally the time to bring in Scatter. Instead of opening a new file, it is really great that I can use a separate scene to do my testing on.

Maybe I'll open a bug report. In fact let me save a duplicate here since the scene is not intricate yet.

Let me leave that for later. I'll remember it when I see the 'buggy asset browser.blend' file in the future.

Now, let me make a 100x100 plane and I will play with Scatter 5. I actually hadn't had a chance to do that yet. It is a mystery to me as to how it works.

https://youtu.be/1eFq21yT1vE?t=5256
GENSHIN CONCERT 2021 《Melodies of an Endless Journey》

Now if I could only close this so I can watch a Scatter 5 tutorial. The concert really picks up the tempo towards the end. I am finding it hard to pause it.

6:30pm. It seems Scatter 5 is not recognizing instance collections in the browser.

6:35pm. https://youtu.be/HYkMd6FX8jM
Architectural Visualization in Blender - Part1/2

Nevermind that. Let me finally watch the tutorial for this. I am wondering how is it possible to import the biomes in the asset browser.

6:45pm. Let me have lunch here. I am actually quite into today's session because I am making concrete progress as slow as it is. Whereas in the last week, I was bashing my head against unsolvable problems.

7:55pm. Agh, who is going to continue now. I'll resume it later.

I am happy with how today went. You can't go wrong with a session where you are in the zone. I couple of months more of this and I'll be a proper 3/5."

---
## [melpa/melpa](https://github.com/melpa/melpa)@[570bde6b4b...](https://github.com/melpa/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Tuesday 2022-06-21 18:04:07 by Jonas Bernoulli

Cosmetic changes to numerous recipes

This commit only touches recipes whose `:files' property contains an
`:exclude' element, because I had to look at all those recipes for an
only marginally related reason.

To an extend these changes only reflect my own personal preference, so
I will explain the types of changes I have made.  This should serve as
a starting point for a future discussion in case we want to encourage
a certain style or even enforce it.

- Lines should be intended as `indent-for-tab-command' would, except
  in special-cases such as in the recipe of `use-package', which is
  also a macro with special indentation rules; we override those
  because the `use-package' in use-package's recipe is not that macro,
  it is just a symbol appearing as the first element of a data list.

- I prefer it if there is a newline between the package symbol (the
  car) and the plist that follows, but usually only add it to existing
  recipes when lines would otherwise get to long.  I also do not
  change this if I am not making any other changes that affect more
  than one line.

- Either the complete list should be on a single line or each line
  should contain only one key/value pair.  The first pair may share a
  line with the package symbol (see previous point).  If the recipe
  needs more than one line, then two key/value pairs should never
  appear on one line.  Newline characters are cheap enough these days.

- `:fetcher' should come before `:url' or `:repo', not least because
  the former dictates which of the latter two is required/valid.  You
  can also think of the fetcher as the type or class of the recipe,
  which IMO should come first, like in code: (git-fetcher :url val).

- The most common keywords should be specified in this order:
  `:fetcher', `:url'/`:repo', `:files'.  Other keywords should go
  either before or after `:files' (but preferable not on both sides
  of that for any given recipe).

- A common value of `:files' is: (:defaults (:exclude "...")).
  This could be split across multiple lines, but writing everything
  on one line makes it easier to read it as 'use the defaults, except
  exclude "..."':

    :files (:defaults (:exclude "..."))

- If the value of `:files' is too long for one line, then place
  newlines "semantically", instead of trying to "save space".  For
  example any element that is a list should appear on its own line.
  Two sibling lists should never appear on the same line.  String
  siblings should also not appear on one line in many cases, though
  it might makes sense (but isn't my preference) to group them by
  "type" as in:

    (:defaults
     "foo/*.el" "bar/*.el"
     "docs/foo/*.texi" "docs/bar/*.texi"
     (:exclude "..."))

- While there may be multiple (:exclude ...) elements, I've merged
  them into one.  Mostly for future proofing.

- The position of `:exclude' elements in `:files' value is significant
  in theory.  However in most cases it already appears at the very end
  and I have moved it there in cases where the order is not
  significant.  Mostly for future proofing.

---
## [Triton-Robotics/TR-mbed6](https://github.com/Triton-Robotics/TR-mbed6)@[99474be9f3...](https://github.com/Triton-Robotics/TR-mbed6/commit/99474be9f3f59c75eb23ac02e0aad421d28ca21e)
#### Tuesday 2022-06-21 18:55:24 by pknessness

sentry was fucked

sentry just.. stopped
dunno why

took infantry code and made that sentry code now

need to remmeber to add thread sleep 1ms to end of each shit

sentry is operating under spaghetti at the moment

---
## [The-Merchants-Guild/Merchant-Station-13](https://github.com/The-Merchants-Guild/Merchant-Station-13)@[2a3b63c243...](https://github.com/The-Merchants-Guild/Merchant-Station-13/commit/2a3b63c2434fec55f7dd1f232455d1594c21809f)
#### Tuesday 2022-06-21 19:47:07 by BettonnCZ

Adds a new sprite for the stacker (#196)

fuck you

---
## [newstools/2022-sowetan-live](https://github.com/newstools/2022-sowetan-live)@[7aca44f4e7...](https://github.com/newstools/2022-sowetan-live/commit/7aca44f4e7ba8b4ae4606e231b75ddec6de132b7)
#### Tuesday 2022-06-21 20:35:56 by Billy Einkamerer

Created Text For URL [www.sowetanlive.co.za/news/south-africa/2022-06-21-life-imprisonment-for-man-who-killed-his-legal-practitioner-girlfriend/]

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[763a10d1cc...](https://github.com/Jolly-66/tgstation/commit/763a10d1cc44c91720101d422d8709ad1aa0644d)
#### Tuesday 2022-06-21 21:51:10 by distributivgesetz

Resonance cascade polishening, bugfixes and better logging (#67488)

This PR rewrites almost all messages related to cascade events. Some messages felt kinda clunky to read or could have been written better. Overall, the new messages add to the experience as a cascade being a terrifying event in a way that I felt the old ones missed, and they make the event feel overall a lot sharper.

While looking at the resonance cascade code, I noticed that there a lot of stuff about cascades in the air which was not touched on. So, as I do, this PR evolved into a polish and roundup PR for cascades. There was a lot of stuff still hanging out relating to the event, and although the big backend of it sits, there was still a bit left to be completed. Therefore this PR deserves more the title of the "Resonance cascade POLISHENING" instead of the "REFLAVAHRING". But yeah, you ever go on a massive tangent before?

---
## [ashao/SmartSim](https://github.com/ashao/SmartSim)@[1e686ead0d...](https://github.com/ashao/SmartSim/commit/1e686ead0d374ab8f41fba7b2d1667e1350e193f)
#### Tuesday 2022-06-21 22:44:28 by Ben Albrecht

SmartSim Singularity Integration (#204)

[committed by @ben-albrecht]
[reviewed by @ashao]

This PR adds the ability for SmartSim to launch workloads in Singularity (Apptainer) as described in https://github.com/CrayLabs/SmartSim/issues/101. It also lays the groundwork for supporting other container runtimes such as docker, shifter, and podman in the future, as well as launching the orchestrator in a container.

## Design Variations

During development, it became clear that a few design changes from the original proposal were required. I have documented them below with their rationale:

#### 1. Argument name: `bind_paths` -> `mount`

The terms bind path and mount are mostly used interchangeably across different container runtimes. When writing tests, I kept forgetting if it was `bind_path` or `bind_paths`, which hinted to me that it was not a great arg name, so I swapped it out for the more succinct and easy to remember `mount`.

#### 2. `create_run_settings(..., container: str)` -> `create_run_settings(..., container: Container)`

We originally thought it would be easier for users to get started with containers by allowing them to pass a string into `create_run_settings(container='singularity')` instead of having to create a Container object. While writing tests, I realized that this was potentially very confusing for users because 1) the `container` arg types change between `create_run_settings` and `RunSettings`, and 2) if you need to add other metadata such as container args or container mount paths, you have to switch from using `create_run_settings` to `RunSettings` in your code, which is very annoying. Because creating Containers is so lightweight, I think it is best to keep the container interface consistent across all functions that accept them.

#### 3. dropped getter/setter methods

Because command generation and validation happens upon execution, users can freely modify `Container.args` and `Container.mount` without getter/setter methods to update any other state. Therefore, I dropped these methods from the interface.

## Testing

Added 2 test suites for containers: One for WLM testing and one for local testing. The local testing suite runs in GitHub actions. Due to the added time from building Singularity and pulling the `container-testing` image, the singularity testing only happens on one configuration of the build matrix: python 3.9 + redisai 1.2.5 on linux

---
## [mamedev/mame](https://github.com/mamedev/mame)@[ba63081d10...](https://github.com/mamedev/mame/commit/ba63081d109c904902958c6324b013cb10b42732)
#### Tuesday 2022-06-21 23:47:37 by 0kmg

gameboy.xml: Added 21 more prototypes. (#9962)

* gameboy.xml: Added 21 more prototypes.

New working software list additions
-----------------------------------
Astérix (earlier prototype) [VGHF, Hidden Palace]
Astérix (early prototype) [VGHF, Hidden Palace]
Asteroids (prototype) [VGHF, Hidden Palace]
Barbie - Game Girl (prototype) [VGHF, Hidden Palace]
Battle Ships (Spain, prototype) [VGHF, Hidden Palace]
Blaster Master Boy (USA, prototype) [VGHF, Hidden Palace]
Bomb Jack (earlier prototype) [VGHF, Hidden Palace]
Bomb Jack (later prototype) [VGHF, Hidden Palace]
Bonk's Adventure (USA, prototype) [VGHF, Hidden Palace]
Bubble Ghost (prototype) [VGHF, Hidden Palace]
Catrap (prototype) [Forest of Illusion, Swanhubstream]
Cosmo Tank (USA, prototype) [VGHF, Hidden Palace]
Dropzone (prototype, alt) [VGHF, Hidden Palace]
Gauntlet II (prototype) [Forest of Illusion, Rezrospect]
Ghostbusters II (prototype) [VGHF, Hidden Palace]
Kung-Fu Master (prototype) [Forest of Illusion, FNeogeo]
Mysterium (prototype) [Forest of Illusion, Rezrospect]
Obélix (Europe, French / German, prototype) [Forest of Illusion]
Prince of Persia (prototype) [Forest of Illusion, FNeogeo]
The Blues Brothers (prototype) [Forest of Illusion, FNeogeo]
Triumph (prototype) [Gaming Alexandria]

---
## [sailfishos-mirror/openconnect](https://github.com/sailfishos-mirror/openconnect)@[b982b2e41e...](https://github.com/sailfishos-mirror/openconnect/commit/b982b2e41ec9e711f086b62951dabfb6509057ae)
#### Tuesday 2022-06-21 23:49:56 by David Woodhouse

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

