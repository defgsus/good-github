## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-04](docs/good-messages/2023/2023-12-04.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 5,794,386 were push events containing 6,707,307 commit messages that amount to 281,908,277 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 67 messages:


## [0x5a4/dotfiles](https://github.com/0x5a4/dotfiles)@[e14d53ffab...](https://github.com/0x5a4/dotfiles/commit/e14d53ffab4c7e740b54bba7eee83a2813f1cb51)
#### Monday 2023-12-04 01:05:27 by 0x5a4

steam beta changed class to 'steam'

THIS IS SO FUCKING STUPID OH MY FUCKING GOD WHYYYYY

---
## [InsightfulParasite/lobotomy-corp13](https://github.com/InsightfulParasite/lobotomy-corp13)@[07a5135fd3...](https://github.com/InsightfulParasite/lobotomy-corp13/commit/07a5135fd31c40f7928d39721fc3d7425e551682)
#### Monday 2023-12-04 01:45:43 by The Bron Jame Offical

Carbon Claw (#1646)

new content babey

i ahve made a severe lapse in my judgement and I do not expect to be forgiven. yadda yadda something reaping what i've sown something

Claw stuff

Claw sounds

CLAW ARMORRRRRRR

claw antag

please work

some of egors fixes

visual updates

new antag things

justice mod

fuckin, 1 god damn character change

Spans and rebase

more changes

what the hell

what the hell!!!!!

---
## [ederekun/x-ft_kernel_oneplus_msm8998](https://github.com/ederekun/x-ft_kernel_oneplus_msm8998)@[b6aa1a1a33...](https://github.com/ederekun/x-ft_kernel_oneplus_msm8998/commit/b6aa1a1a3322466380058bbccab9f0e819459e26)
#### Monday 2023-12-04 01:51:45 by Peter Zijlstra

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
## [chiphogg/wg21-papers](https://github.com/chiphogg/wg21-papers)@[d7adc57ad0...](https://github.com/chiphogg/wg21-papers/commit/d7adc57ad089589a919bfc2cd065fa6094286069)
#### Monday 2023-12-04 01:58:43 by Chip Hogg

Update "quantity as numeric type" text for R1

The only actual edit I've made was to add a line in the common unit
computation, which makes it easier to understand.

I've also collected a variety of feedback about other sections on the
paper.  This feedback was harder to translate cleanly into edits, but I
wanted to find _some_ home for it.  Additionally, even if I _could_ make
edits, it may not be wise to do so, because we want to minimize changes
before the committee discusses it next week.  So I'll add this feedback
to the PR summary.

- 4.6: What are some concrete use cases for `kind_of<...>`?  I have a
  hard time seeing the motivation --- both for this feature, and for the
  rules at the end (e.g., arithmetic with a kind and non-kind produces a
  non-kind).

- 6.4.1: I don't understand the meaning of the equality operator for
  dimensions, nor its implementation.  Does it not break transitivity,
  which is a critically important property for an equality operator?  If
  B and C both derive from A, then each would compare equal with A, but
  not with each other.  Do we even _want_ equality of dimensions?
  Wouldn't we be better off by providing separately named functions for
  different kinds of equivalence?

- 6.4.3: What is a "canonical unit"?  I'm not familiar with this
  concept.

- 7.4: What does this mean?  What is the "reference unit" of a unit?
  I'm not familiar with this concept.

- 7.5: Subjectively, the chapter feels awfully big for something so
  speculative.  Are we sure we want to go into this much detail before
  we have accumulated much more (any?) real world experience?

- 7.5.1: Multiplication of vectors is mathematically defined using
  geometric algebra.  The product is the "geometric product".  It
  produces, essentially, a complex number (the sum of a real part and a
  bivector part, the latter of which encodes information about the plane
  spanned by the vectors).  This is part of my worry with the system of
  characters: there's not Just One System in mathematics, and we may
  exclude or make awkward certain important use cases.

- 7.5.2: If we _do_ go this route, I expect we'll want more characters
  than just scalar, vector, and tensor.  The current setup would allow
  adding the result of a cross product of two vectors to another vector,
  but this seems like a missed opportunity to prevent errors.

---
## [usnpeepoo/cmss13](https://github.com/usnpeepoo/cmss13)@[e7caf52c21...](https://github.com/usnpeepoo/cmss13/commit/e7caf52c21e01e4580cbf03ff1c61579054dd7a2)
#### Monday 2023-12-04 02:01:51 by fira

Rewrite Xeno Acid processing (#4759)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Rewrites scheduling of xeno acid to hopefully finally be done with
dangling references warnings with acid. Also generally improves the
awful code quality

# Explain why it's good for the game
Like, dude, some of these values were outright inversed.
acid_**strength**=2.5 is noted as "250% speed" when it multiplies the
sleep delays. Can't leave code in that state.

# Testing Photographs and Procedure
Summary testing, timing appear correct overall but I'm not entirely
certain it's perfect due to random delays and obtuse code


# Changelog
:cl:
code: Rewrote Xeno Acid ticking code.
fix: Weather updates won't cause turfs to acid melt more rapidly anymore
/:cl:

---
## [usnpeepoo/cmss13](https://github.com/usnpeepoo/cmss13)@[e120ab795b...](https://github.com/usnpeepoo/cmss13/commit/e120ab795ba0e92e4eb0f91fda194c59f83cb5aa)
#### Monday 2023-12-04 02:01:51 by fira

Add Item & Footprints offsets (#4762)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

This:
* Adds transverse offsets to blood footprints
* Adds notable pixel offsets to a few items
* Adds a very slight pixel offset to all items
* Enables rotation for thrown flashlights
* Cause objects exiting a surface (rack/table) to regenerate offset
instead of being stuck at center
* Stops random offsets from overwriting mapped offsets

# Explain why it's good for the game
The goal is to have map visuals more organic when we have a lot of
objects on the ground - targeting in particular items you find readily
in dense areas such as Reqs or a FOB.

Consider this for example, the blood footprints are all aligned, in more
extreme situations (eg WO) it makes an actual "grid" which i personally
find very immersion breaking

![image](https://github.com/cmss13-devs/cmss13/assets/604624/83883e15-a9a0-4a2d-aa90-41c785e047b9)

Adding a slight offset helps counter that:

![image](https://github.com/cmss13-devs/cmss13/assets/604624/504d1baf-385c-4774-86f3-6331c4ac87ed)

# Changelog
:cl:
add: Bloody footprints are now slightly offset to break long visual
straight lines.
fix: Items do not align back to the center of turfs anymore when picked
from a surface (table or rack)
add: Some more items now have offsets on the map display, and they all
can be slightly offset.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [Zargoar/tgstation](https://github.com/Zargoar/tgstation)@[0d5f9907a2...](https://github.com/Zargoar/tgstation/commit/0d5f9907a24346554f4da78199138f4cdcca8de5)
#### Monday 2023-12-04 02:12:07 by Jacquerel

Shapechange health transfer tweaks (#79009)

## About The Pull Request

Fixes #78721
This PR does a handful of things behind the scenes to increase the
consistency of shapechange health tracking.

First of all we adjust the order of operations taken when you restore
the original body. The implementation as-was would remove the status
effect midway through and null a bunch of variables we tried to continue
using. This would result in several runtimes and code failing to run,
with the upshot that untransforming upon death would leave the caster
completely alive, with the corpse of its transformed shape at its feet.
Oops.

Additionally while testing this I realised that transferring the damagew
as also kind of fucked.
We wouldn't bother to do it at _all_ if you died, which is a shame, so I
made it simply heal you instead of reviving you so we can always do it.
Then as noted in the linked issue, we were applying all transferred
damage to a single limb, which could exceed the health of the limb and
remove damage. Now we spread it around the body.

Finally, applying damage to a human using the "force" flag would often
actually apply less damage to their _health_ than expected. This is
because arms and legs contribute only 75% of their damage taken to a
mob's overall health.
Now instead of reading `health` we read `total damage` which ignores the
limb damage modifier.

The end result of this is that if you transform into a corgi, take 50%
of your health, and transform back then you will have 50% of your health
as a human.
Previously the result would be that you'd have ~63%, then transforming
into a corgi would leave you with ~63% of a corgi's health, then
transforming back into a human would leave you at about 71%... and so on
and so forth. Now it doesn't do that.

## Changelog

:cl:
fix: Dying when using (most) shapeshift spells will now kill you rather
than having you pop out of the corpse of your previous form.
fix: Damage will now be accurately carried between forms rather than
being slightly reduced upon each transformation.
/:cl:

---
## [yk1n0rt/Open-Assistant](https://github.com/yk1n0rt/Open-Assistant)@[b9c60ed582...](https://github.com/yk1n0rt/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Monday 2023-12-04 02:13:31 by Tobias Pitters

add alpaca gpt4 dataset (#2610)

The inputs can be quite a lot of different versions of `no input`,
therefore don't use the `input` column for that.
In some cases the text in `input` is already in the instruction, in
these cases, we also don't use the `input` column.

I am not quite sure how to concatenate the `instruction` and the `input`
column. In most cases it seems fine to just replace last appearance of
`.`, `!` or `?` with a colon, e.g.:
Instruction: `Identify the odd one out.`
Input: `Twitter, Instagram, Telegram`
or 
Instruction: `How dense is a given material?`
Input: `Steel`

But we also have some questions like:
Instruction: `Given the following synopsis, what is the moral lesson of
this story?`
Input: `Once upon a time, there was a poor young boy who wanted some
candy. He begged his father for money to buy it, but his father said no
and ordered him to go to bed. As he was going to bed, the boy saw a
five-dollar bill on the counter, which he took and bought the candy.`

Where this might not be the best case. Either way, I think the this one
token will not make significant difference the model and therefore I
just concatenate instruction and input with a space.

---
## [KeRSedChaplain/Bubberstation](https://github.com/KeRSedChaplain/Bubberstation)@[52f69b96ee...](https://github.com/KeRSedChaplain/Bubberstation/commit/52f69b96eebfbe14a763ae9c5a8dd7ef156c4582)
#### Monday 2023-12-04 03:29:18 by The-Sun-In-Splendour

mid-round salt pr about EMP mold because being repeatedly shocked 500 times in a row unless you get charcoal (now called syniver or whatever fuck new chems) is not what I consider to be fun gameplay (#755)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
emp mold mosquitoes no longer put you in shock stunlock hell because
that shit is not funny
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game
it made me mad and this is a salt pr

![image](https://github.com/Bubberstation/Bubberstation/assets/70348069/b5002caa-d401-478a-9d48-fbc772c05b3e)

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

:cl:
balance: emp mold mosquitoes no longer shock you all the time until you
have a stroke irl over the annoyance
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

---
## [MoonTheBird/Shiptest](https://github.com/MoonTheBird/Shiptest)@[4d4aa72e33...](https://github.com/MoonTheBird/Shiptest/commit/4d4aa72e33bd20077d09d320f07a0a5608298cb2)
#### Monday 2023-12-04 04:07:14 by lizardqueenlexi

Removes "fat" status and everything related. (#2516)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

As the title says, eating too much no longer makes you "fat". You suffer
no slowdown or mood debuff from eating too much, and in general, the
game will not take every opportunity to make fun of you.

Notable removals/changes:
- The "fat sucker" machine is totally gone.
- Shady Slim's cigarettes have been removed (since they only existed to
interact with this mechanic).
- Lipoplasty surgery is gone.
- The nutrition setting of scanner gates is gone.

There are a couple of other removals too, like Gluttony's Wall, that I
think were already not in use on this codebase.

One thing I'm not completely satisfied with was the change to mint
toxin, which now does quite literally nothing. I don't think this is
especially a problem, it just makes its existence a bit vestigial.

Also includes an UpdatePaths script to delete all removed objects, just
in case.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game


![image](https://github.com/shiptest-ss13/Shiptest/assets/105025397/a1dd0981-94fc-4766-a34d-cce31a42b412)

Basically, removes some shitty "jokes" about fat people. It's an
extremely mean-spirited feature that serves no actual purpose, and
punishes you for clicking on a burger one time too many. It could
potentially be replaced later with a less mean-spirited "overeating"
mechanic, but I'm dubious as to whether that would be any fun either.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: Removed the "fat" status - overeating now has no negative effects.
del: Removed lipoplasty surgery.
del: Removed the fat sucker machine.
tweak: Scanner gates no longer have a "nutrition" option available.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [MoonTheBird/Shiptest](https://github.com/MoonTheBird/Shiptest)@[caa19d2a6f...](https://github.com/MoonTheBird/Shiptest/commit/caa19d2a6f8014c2d34663c7c63685921bc0218a)
#### Monday 2023-12-04 04:07:14 by GenericDM

Assorted cringe removal pt.whatever (#2534)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Removes more cringe I found laying around.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
/tg/ was on some WILD shit.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: removes tail club
del: removes all flavors of tail whip
del: removes lizardskin clothing
del: removes 'Genetic Purifier'
tweak: makes bunny ears desc not incredibly sexist
tweak: change up wording in magic mirror gender change
del: removes 'genuine' cat ears
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[1e9edd6a49...](https://github.com/Monkestation/Monkestation2.0/commit/1e9edd6a49665dc9ae5e857e72455961be4f8230)
#### Monday 2023-12-04 04:16:09 by Kittynoodle

Refactors vendor tipping and adds 2 new malf modules: Remote vendor tipping, and the ability to roll around and crush anything in your path. (#76635)

Title.

Vendor tipping code is now on /atom/movable, and any movable can fall
over like a vendor does. Things like crits have been moved to
type-specific availability tables, their effects are now held in their
own proc, are now random per crushed item, have probability weights,
etc.

In the process of making this PR I also had to fix another issue, where
a bunch of take_damage() overrides had incorrect args, so that explains
the take_damage changes I made.

Tipping now also attacks any atoms on the target, given they use
integrity.

Adds 2 new malf modules.

1. REMOTE VENDOR TIPPING: A mid-cost and mid-supply module allows malf
AIs to remotely tip a vendor in any of the 8 directions. After 0.5
seconds of delay and a visual indicator (along with other warnings), the
vendor falls over.
1.1. In the process of making this I had to expand a arrow sprite to
have orthogonal directions, which is why you may see the testing dmi
being changed.
2. CORE ROLLING: A mid-cost but low-supply ability that allows the AI to
roll around and crush anything it falls on, including mobs. This has a
5% chance to have a critical hit so it isnt THAT terrible - plus it's
guaranteed to never stunlock. It's real utility lies in the fact the AI
now has limited movement without borgs. Also, the psychological factor.

As a bonus, vendor tipping now uses animate and transforms instead of
replacing matrices.

1. Generifying vendor tipping code is just good, period. It's a very
wacky and silly little piece of code that really doesn't need to be
isolated to vendors exclusively. ANY big and heavy object can fall over
and do a ton of damage.
1.1. Also, adding weights to critical hits is really good, because it
lets things like the headgib finally be a lot less terrifying, as
they're a lot less likely to happen.

2. Remote vendor tipping is a bit of a goofy ability that isn't really
THAT practical but has a chance of catching someone unaware and doing
some serious damage to that person alone.
2.1. Atop of this, vendor tipping isn't that loud of an action as say,
blowing things up, or doing a plasma flood. Even overrides aren't this
silent or a non-giveaway. A vendor falling on someone, though, is a
mundane thing that happens a lot. This is a decent way to assassinate
people before going loud (or at least, damage people) that isn't offered
yet.

4.
3.1. For real though, AIs rolling around is just fucking hilarious. The
ability to move isn't offered right now (which isn't that much of a bad
things), but with sufficiently limited charges (or limits to how many
times you can buy the ability), this can be a funny little t hing that
lets the AI potentially hide somewhere on the sat (or just relatively
close to the sat, such as engineering [it can't go through the
teleporter with this but it can go through transit tubes]) without the
need for borgs.
3.2. Also, it lets the AI sacrifically execute people by blowing up
their brains.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[bca3d03946...](https://github.com/crawl/crawl/commit/bca3d03946f17baf04eab8d0adc0c556bd83d797)
#### Monday 2023-12-04 04:25:19 by regret-index

Even more widespread vault review

Of note:

 * _lair_caniforms_friends gets a hell hog because it's also an elemental
   mammalian quadruped as fills the vault already and also because it's
   been struggling at the bottom of the lair kills list.

 * Lair endings with dragons have been each been tweaked. The swampy one
   gets a chance for an ice dragon over a fire dragon, the minivolcano has
   a 1/3 chance for two hell hogs, and the wurm / snail cave has been
   warped to place the dragon room in a plant corridor at a random end of
   the vault rather than with a runed door right at the start. (If we're
   already putting dragon bosses without runed doors in one end, we really
   don't need runed doors in front of the other dragons; it dilutes the
   warning capacity of runed doors to just shepard autoexplore. The
   minivolcano should be stabbed at in this regard, but that's harder to
   adjust...)

 * The Hall of Blades blade talisman has an explicit small chance to be
   a randart now, to make it less sad for later Elf visits and to continue
   to try to get people to open the vault up.

 * orc_legates has been taken out of the Elf:1 guaranteed minivault pool
   for being much more dangerous and dense than the others in that slot.
   Three minivaults made much later than the original set setting have
   been added to the tag to compensate.

 * Several iron golems escaping Dis to find the protection of Chei altars
   in Depths have been damned back to hell, with iron dragons watching
   over those altars to keep them from coming back.

 * Moved amcnicky_altar_lugonu_corruption and its out-of-Abyss lurking
   horrors from most of its main-game placement (outside of the themeless
   D and Depths) for extended placement instead. There's many excuses
   one can make for monsters from elsewhere invading a branch, and that
   doesn't really inherently justify diluting the entire game with
   monsters that'll mostly just force one to rest rather than kill.
   Lurking horrors in particular will be felt more in the Hells and Pan
   anyway.

 * Remaining teleport / flight islands in Cocytus:$ and Gehenna:$ have
   been covered with more liquids and no_tele_into, which should close
   Mantis #12466.

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[33cae266af...](https://github.com/silicons/Citadel-Station-13-RP/commit/33cae266af864b22c509f65ffff3ad7277bbb459)
#### Monday 2023-12-04 04:58:16 by Captain277

Subtypes Corporate Crates, Fixes Mapped Biohazard Crate, Renames Advanced Voidsuit (#6126)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. *Fixes Bug With Corporate Crates, Subtypes Them.*
2. *Removes Varedited Biohazard Bin and Places Normal Biohazard Bin.*
3. *Changes Advanced Voidsuit Name to Advanced Hardsuit.*

## Why It's Good For The Game

1. _I received reports of one specific corporate crate not rendering
properly when opened. As I inspected it, I realized it would be more
efficient to subtype all corporate crates, so I did that. HOWEVER, this
did not repair the initial bug. For some reason the crate was not
rendering its 'aethersecureopen' state, even though all variables and
code seemed to be working properly. No other crate exhibited this issue.
I discovered that by changing the name of the icon state from
'aethersecureopen' to 'aethersecopen', the state began to enforce and
render properly. I suspected it might be a name length issue, but tests
with other equally long icon states in the crate section disproved this
theory. This may warrant further investigation._
2. _This one avoided detection during my initial sweep through. Can't
remember who just went in and tried to varedit bins to fix biohazards,
but hopefully this is the last one they touched._
3. _This has been driving me crazy for a few days, and yesterday
especially. The Advanced Voidsuit is clearly misnamed, as it is in fact
a Hardsuit. When I tried to order these yesterday I overlooked this
cargo entry twice because I was looking for a hardsuit, not a voidsuit.
This just fixes the name._

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

:cl:
add: Adds Corporate Crate Subtype, Reassigns Corporate Crates to It.
fix: Fixes incorrectly mapped biohazard bin.
tweak: Changes Name: Advanced Voidsuit to Advanced Hardsuit.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Dredgen1125/Rejuvenation-Community-Fights](https://github.com/Dredgen1125/Rejuvenation-Community-Fights)@[9eb0f5ba3a...](https://github.com/Dredgen1125/Rejuvenation-Community-Fights/commit/9eb0f5ba3a75243cd4fdafa191050b3b2ddcdecd)
#### Monday 2023-12-04 05:15:27 by Anxee

i honestly dont remember, probably more melody shit

---
## [VierKing/App-Dev](https://github.com/VierKing/App-Dev)@[6a49093190...](https://github.com/VierKing/App-Dev/commit/6a490931908aa4e5a2795479e93cfaff952d15bc)
#### Monday 2023-12-04 07:04:33 by VierKing

Update README.md

**Favorite Horror Movies**
1.*The Grudge* a curse that is born when someone dies in extreme rage or sorrow and lingers where the person dies
2.*The Ring* Teenage girls Katie and Becca discuss an urban legend about a cursed videotape that causes whoever watches it to die in seven days.
3.*Unborn* The story follows a college student named Casey Beldon who begins to have strange visions and comes to believe that she's being stalked by a malicious spirit.
4.*Hellraiser* Its plot involves a mystical puzzle box that summons the Cenobites, a group of extra-dimensional, sadomasochistic beings who cannot differentiate between pain and pleasure

**Favorite TV series**
1.*Reacher* When retired Military Police Officer Jack Reacher is arrested for a murder he did not commit, he finds himself in the middle of a deadly conspiracy full of dirty cops, shady businessmen, and scheming politicians. 
2.*Hotel de Luna*  a fantasy romance that features an elite hotelier who becomes the manager of Hotel Del Luna, a mystical hotel that only caters to spirits at night, after stumbling upon a fateful event.
3.*Hajime no Ippo* he story of high school student Ippo Makunouchi, as he begins his career in boxing and over time obtains many titles and defeats various opponents
4.*Hunter x Hunter*  a licensed professional who specializes in fantastical pursuits such as locating rare or unidentified animal species, treasure hunting, surveying unexplored enclaves

---
## [Offroaders123/Dovetail](https://github.com/Offroaders123/Dovetail)@[152e37103c...](https://github.com/Offroaders123/Dovetail/commit/152e37103c8be3927cb90e57e4675ee52291b786)
#### Monday 2023-12-04 07:20:19 by Offroaders123

Various Niceties

Thinking about adding CodeMirror 6 support to the main editor, which would allow for better UX, mainly code folding, syntax highlighting, and maybe even SNBT syntax error linting, I'm not sure about CodeMirror's support for that kind of thing though.

These organization changes are some of the ones I did recently over in STE's codebase. It's part of my experimentation with learning the ways of common bundler-based site structures, as well as the general structures that framework-based sites tend to use, like with React or other libraries. I want to use React, with time, I don't want to cruftily move into using it though, I want my apps to be tidier and more applicable to the framework model before trying to adopt that mindset of structuring things.

It's not that I'm trying to wait on using those, but rather I'm trying to teach myself the common patterns that those kinds of structures tend to follow, and I want to get used to those before moving over to also how I manage state and component declarations. That's the current issue, my state management isn't too compatible with how frameworks tend to organize things, and I want to get used to that way of thinking, before moving over to those. Like the concept of putting lipstick on a pig, I'd rather my apps not be ugly before trying to make them fancy. Nothing can be perfect, but you sure as hell can try doing your best! And I see plenty of things I can improve on, before adding layers more of abstraction. I want to remove fluff complexity, before adding helpful abstractions.

---
## [say-paul/images](https://github.com/say-paul/images)@[7152886364...](https://github.com/say-paul/images/commit/715288636474b85551fdf53478754d931c6fafa8)
#### Monday 2023-12-04 07:44:09 by Tomáš Hozza

distro/el9: refactor package sets to again use `@core` pkg group

Previously, we used a fixed package list from RHEL-9.0 times, instead of
the `@core` pkg group, for all images which used it on el8. The
motivation was that some packages got removed from the group in 9.0
(specifically tuned), which went almost unnoticed. The reasoning was that
a fixed list would give us more control over the package set and prevent
unexpected package removals.

However, with COMPOSER-2074 [1], it turned out that this also meant that
any new packages added to the `@core` group won't be automatically added
to any image which previously used the `@core` group. People still have
(anyhow incorrect) expectation that `@core` pkg group is always
installed on RHEL images and thus that adding a package to the group
will also add it to vanilla RHEL images.

We discussed this shortly within the team and reverting back to using
`@core` package group, instead of a fixed package list, seems like the
lesser evil.

Modify package set definitions, which used `coreOsCommonPackageSet()` to
use `@core` package group instead. Modify the exclude lists accordingly
to achieve almost the same image content as before. There are a few
exceptions:

 - `rhc` package is now installed, which is desired.
 - `insights-client` is now installed on some images where it was
   previously not. This is OK, since RHEL is aiming for a "connected
   experience" by default. This also results in a few additional
   packages to be pulled in as dependencies, specifically:
   - `python3-file-magic`
   - `policycoreutils-python-utils`
   - `tar`
   - `pciutils`
 - `initscripts-rename-device` is now installed. This sub-package has
   been split out of the `initscripts` package on el9, but it was not
   included in the `@core` group definition, when we created the fixed
   pkg list. However, it is now the default member of the group. The
   functionality was previously installed by default on el8 images via
   the `initscripts` package. After talking to the maintainer, I kept it
   in the images as a new package.

Affected images by this change:
 - ami
 - gce
 - gce_rhui
 - image_installer
 - oci
 - openstack
 - ova
 - qcow2
 - vmdk

Some of the listed images already contained `rhc` or `insights-client`,
but now, these are consistently installed on all of them. This is the
case since 9.2, when `rhc` was added to the `@core` group.

`initscripts-rename-device` has been added to all of these image types,
inlcuding on CentOS Stream 9 images.

[1] https://issues.redhat.com/browse/COMPOSER-2074

Signed-off-by: Tomáš Hozza <thozza@redhat.com>

---
## [lolman360/f13tbd](https://github.com/lolman360/f13tbd)@[2f8b621240...](https://github.com/lolman360/f13tbd/commit/2f8b62124081d83f1dc9ee4085e0365a33a4bb2f)
#### Monday 2023-12-04 07:51:02 by K4rlox

Chruch PR, attempt 3 to fix merge coflict (#249)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

this PR works on redesigning, and moving the warren church to bighorn

![2023-11-24 13 33
01](https://github.com/f13babylon/f13babylon/assets/118483925/f9e8cb97-cdb1-46b7-950a-4c0364fad0a8)

![2023-11-24 13 33
20](https://github.com/f13babylon/f13babylon/assets/118483925/3ee346c1-c788-4c87-8e9b-31381030bc31)


the preacher already is considered a bighorn citizen so the church being
in warren used to make no sense

this fixes the issue and adds a few additional community requested
changes


this is a second attempt because the last one was closed because of a
item that crashed the server that i forgot to mention in changelogs


### **please if you want something changed then say it**
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Preacher is supposed to be a citizen of bighorn therefore have a church
in bighorn, but they for some reason had a church in warren instead of
bighorn, i have heard some community members arguing about it and
decided to act on it as it only makes sense for the church to be
somewhere close to bighorn instead of in warren.

adds more items for the priest to use, adds an actual spawning landmark
for the priest to spawn in the church instead of a random matrix

adds several other misc items such as a angel food cake, a holy water
bottle, bread, wine, and several spare bibles

oh also gives the preacher closet a shotgun with no ammo, since the
preacher landmark seems to have a shotgun icon.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
add: church in (front of) bighorn
add: bible, bread, wine and water crate
add: holy water flask
add: angel food cake
add: Priest shotgun (with no ammo)
add: Preacher starter landmark
add: water bottles
tweak: changes the bible on the table to the whiskey bible
fix: fixes the prayer breads not working

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [lolman360/f13tbd](https://github.com/lolman360/f13tbd)@[f996624f34...](https://github.com/lolman360/f13tbd/commit/f996624f34bd17872783cf0757300c93cc116f38)
#### Monday 2023-12-04 07:51:02 by foxymegneil

Enclave Marineification (#251)

## About The Pull Request

Changes all the icons and items of Enclave enlisted rank tabs (officer
tabs are the same between the Army and Marines) to be that of the Marine
Corps, while also adding some new ones that can be used for RP or
whatever. Also appropriately hands out said tabs. Private tab is GONE,
because it doesn't exist in the Marine Corps. You also may notice a
Petty Officer Third Class tab. What's that for? Well, it was originally
going to be for the Navy Corpsman loadout for the Specialist, however
loadouts seem to suffer with terminally low storage, so I wasn't able to
fit a rank tab into either of the loadouts. The item and icon are being
left in, however, just in case someone smarter than me can fix it.

Anyway, here are the sprites:

![sprites](https://github.com/f13babylon/f13babylon/assets/85942538/8b239726-1efb-43d3-a15d-731453df4a30)

## Why It's Good For The Game

We're Marines now! To hell with those Army tabs!
It's more immersive, and gosh darn it, that's all we Enclave players
have left. Immersion.

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.


## Changelog


:cl:
add: Adds some brand new Marine Corps tabs.
del: Old Army tabs that aren't needed anymore.
tweak: Changes some of the old tabs to new ones.
imageadd: New tabs!
imagedel: Old ones are gone.
/:cl:

---
## [crowlogic/papers](https://github.com/crowlogic/papers)@[74901ba266...](https://github.com/crowlogic/papers/commit/74901ba2665a63aa7e8995e478f19c9948854e6a)
#### Monday 2023-12-04 07:57:15 by Stephen A. Crowley

I remember dad telling me about a dream during the pandemic of a little
boy named Hugh alone in a farm-house isolated from a massive hoarde
consisting of billions of people. Everett was fond of programming the
TRS-80 before he died, and my uncle said when I saw the TRS-80 machine
when I was 4 or 5 years old I went right up to it and started typing
away like I knew what I was doing

---
## [Fluffy-Frontier/FluffySTG](https://github.com/Fluffy-Frontier/FluffySTG)@[100ede82bd...](https://github.com/Fluffy-Frontier/FluffySTG/commit/100ede82bd27e39fc8844464aeb2be82822862f5)
#### Monday 2023-12-04 09:30:38 by Iajret Creature

[MIRROR] Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun [MDB IGNORE] (#25365) (#908)

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun (#80030)

## About The Pull Request
One of the "monkey cubes" in Birdshot's tool storage was actually a
gorilla cube. This was funny up until people realized it was a thing and
now people are using it intentionally to grief. I'd rather not.

It's a different cube now. I don't want to spoil it but it won't kill
anyone, just make people laugh.

I added a different fun item to another tile in tool storage. Again, no
spoilers, read the code if you really want to know what it was.

## Why It's Good For The Game
I like the "cube says it's a monkey but it's not" joke. It was funny
when people thought it was a monkey, used it, and got killed by it.
Problem is, people know what it is now and have used it for grief
purposes, so we can't have nice things. Gorillas are stupid hard to kill
and will de-limb people by looking at them.

I wanted to add something else fun to replace it that isn't just the
exact same joke but now it won't kill you, so I did.

## Changelog
:cl: Vekter
del: Replaced the "monkey cube" in Birdshot's tool storage with a
different "monkey cube".
add: Added a fun surprise item to Birdshot's tool storage to compensate
for the above change.
/:cl:

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun

---------

Co-authored-by: SkyratBot <59378654+SkyratBot@users.noreply.github.com>
Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [G1gg1L3s/themis](https://github.com/G1gg1L3s/themis)@[1ca96de89b...](https://github.com/G1gg1L3s/themis/commit/1ca96de89b66391114f615658fbc4819aa248b9b)
#### Monday 2023-12-04 11:40:11 by Alexei Lozovsky

Add missing OpenSSL includes (#684)

* Add missing OpenSSL includes

Add those files use BIGNUM API of OpenSSL but do not include relevant
headers. Due to miraculous coincidence, this seems to somehow work for
the OpenSSL versions we use, but only because either existing headers
include this "bn.h" transitively, or because the compiler generates
code that kinda works without function prototype being available.

However, curiously enough, this breaks when building Themis for macOS
with recent OpenSSL 1.1.1g but not with OpenSSL 1.0.2, or OpenSSL 1.1.1g
on Linux. The issue manifests itself as missing "_BN_num_bytes" symbol.
Indeed, there is no such symbol because this function is implemented as
a macro via BN_num_bits(). However, because of the missing header, the
compiler -- being C compiler -- decides that this must be a function
"int BN_num_bytes()" and compiles it like a function call.

Add the missing includes to define the necessary macros and prototype,
resolving the issue with OpenSSL 1.1.1g. It must have stopped including
<openssl/bn.h> transitively, revealing this issue.

This is why you should always include and import stuff you use directly,
not rely on transitive imports.

P.S. A mystery for dessert: BoringSSL backend *includes* <openssl/bn.h>.

* Treat warnings as errors in Xcode

In order to prevent more silly issues in the future, tell Xcode to tell
the compiler to treat all warnings as errors. That way the build should
fail earlier, and the developers will be less likely to ignore warnings.

* Fix implicit cast warnings

Now that we treat warnings as errors, let's fix them.

themis_auth_sym_kdf_context() accepts message length as "uint32_t" while
it's callers use "size_t" to avoid early casts and temporary values.
However, the message length has been checked earlier and will fit into
"uint32_t", we can safely perform explicit casts here.

* Suppress documentation warnings (temporarily)

Some OpenSSL headers packaged with Marcin's OpenSSL that we use have
borked documentation comments. This has been pointed out several
times [1][2], but Marcin concluded this needs to be fixed upstream.

[1]: https://github.com/krzyzanowskim/OpenSSL/pull/79
[2]: https://github.com/krzyzanowskim/OpenSSL/pull/41

Meanwhile, having those broken headers breaks the build if the warnings
are treated as errors. Since we can't upgrade Marcin's OpenSSL due to
other reasons (bitcode support), we have no hope to resolve this issue.

For the time being, suppress the warnings about documentation comments.

* Fix more implicit cast warnings

There are more warnings actual only for 32-bit platforms. Some iOS
targets are 32-bit, we should avoid warnings there as well.

The themis_scell_auth_token_key_size() and
themis_scell_auth_token_passphrase_size() functions compute the size of
the autentication token from the header. They return uint64_t values to
avoid overflows when working with corrupted input data on the decryption
code path. However, they are also used on the encryption path where
corruption is not possible. Normally, authentication tokens are small,
they most definitely fit into uint32_t, and this is the type used in
Secure Cell data format internally.

It is not safe to assign arbitrary uint64_t to size_t on 32-bit
platforms. However, in this case we are sure that auth tokenn length
fits into uint32_t, which can be safely assigned to size_t.

Note that we cast into uint32_t, not size_t. This is to still cause
a warning on platforms with 16-bit size_t (not likely, but cleaner).

---
## [thgvr/Shiptest](https://github.com/thgvr/Shiptest)@[bf4671ff83...](https://github.com/thgvr/Shiptest/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Monday 2023-12-04 11:43:36 by retlaw34

Gun rework (#1601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
WIP.

if it wasn't obvious, very based off tgmc 

this reworks how guns work, by making them 4x more lethal without
touching a single damage value

its a bit difficult to put into words what this does, so i think these 3
gunfights i did with a good friend explains it better than i ever could

https://streamable.com/09in19
https://streamable.com/yel56o
https://streamable.com/x2a0he

if you didnt watch these videos:
- New guns sounds, TGMC as usual. but some racking sounds are from CEV
eris
- guns now can be wielded, if unwielded, they may cause recoil which not
only makes your shots less accurate, but 'scrolls' your screen
- new suppression effects
- getting hit hard enough scrolls your screen
- anything getting hit shakes you as feedback, not just bullets
- bullets can ricochet naturally upon hitting a surface at a step angle.
does not auto aim at your target, so be careful. ricochet sfx taken from
CEV eris
- new effects for bullet impacts. sound effects were taken from TGMC and
https://github.com/Skyrat-SS13/Skyrat-tg/pull/11697
- adds the cattleman revolver and Himehabu 22lr pistol. sprites by yours
truely

big problem is, in order for all of this to work, a certain key needs to
be binded to rack the gun. by default this is SPACE, but moost already
have it binded to 'hold throw mode', which is an issue. for one, not
only you need to ask everyone to rebind their controls to a very
important key, but also a key dedicated to just racking the gun can
cause issues. im up for any solutions

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game

people dont fear gunfights. they think its just a way to pvp. people
should be afraid of gunfights, feel the pain OOCly when their blorbo
gets hit

## Changelog

:cl:
add: 22lr and cattleman revolver
add: many gun sounds
balance: guns reworked
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: retlaw34 <bruhasdfasdfasdf@waifu.club>

---
## [NPC1314/coyote-bayou](https://github.com/NPC1314/coyote-bayou)@[617714eba5...](https://github.com/NPC1314/coyote-bayou/commit/617714eba525e77a2a408a83247c9ea7062bca33)
#### Monday 2023-12-04 11:56:22 by Lynx

Mapping - Foliage Galore

Added more foliage! More and more! Also changed the back entrance into the tribal camp.

FUCK MORE MAPPING!

WAY MORE THAN I CAN LIST!

4? Ish? Ends of roads have been altered to blend more realistically with its surroundings at the start of nash.

Scug area has been toned down in its super duper high fantasy stuff for something more tame; yet magical.

Tribal camp has a little 1 tile extenstion to be in line with the northern tower.

NAsh has a TON of plants.

UNDERGROUND got changes

Fixed one spot in tribal area to avoid random get at the gate for the garden.

---
## [NPC1314/coyote-bayou](https://github.com/NPC1314/coyote-bayou)@[a3fdbe5881...](https://github.com/NPC1314/coyote-bayou/commit/a3fdbe5881830f0fbc30cb7662f4a8d99e33310d)
#### Monday 2023-12-04 12:00:13 by Tk420634

Merge pull request #3945 from Kilmented/master

UPDEN FUCK YOU UP

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[3afb4e5cf7...](https://github.com/pytorch/pytorch/commit/3afb4e5cf7b0162c532449fb5c9e7c7058a4c803)
#### Monday 2023-12-04 12:28:53 by Brian Hirsh

AOTAutograd: handle set_(), detect metadata mutations that cancel out (#111554)

This should be enough to get @voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

(1) graph break on `aten::set_.source_Tensor_storage_offset` (we could support it but it isn't needed, seems safer to graph break)

(2) Functionalization: add a "proper" functionalization kernel for `aten::set_.source_Tensor`. The previous one we had was codegen'd and it was wrong (it would just clone() and call set_(), which does not do the right thing). I also manually mark on the `FunctionalTensorWrapper` when a given tensor has been mutated by a `set_()` call.

(3) AOTAutograd: I added a new field, `InputAliasInfo.mutates_storage_metadata`, so we can distinguish between "regular" metadata mutations, and metadata mutations due to `set_()` calls. This is mainly because at runtime, one requires calling `as_strided_()` to fix up metadata, while the other requires calling `set_()`.

(4) Made AOTAutograd's detection for metadata mutations / set_() mutations smarter and detect no-ops (if the storage and metadata are all the same).

I also killed `was_updated()` and `was_metadata_updated()`, and replaced them with (existing) `has_data_mutation() ` and (new) `has_data_mutation()`, which can more accurately distinguish between data-mutation vs. `set_()` calls vs. metadata-mutation

**This PR is still silently correct in one case though**, which I'd like to discuss more. In particular, this example:
```
def f(x):
    x_view = x.view(-1)
    x.set_(torch.ones(2))
    x_view.mul_(2)
    return
```

If you have an input that experiences both a data-mutation **and** a `x_old.set_(x_new)` call, there are two cases:

(a) the data mutation happened on the storage of `x_new`. This case should be handled automatically: if x_new is a graph intermediate then we will functionalize the mutation. If x_new is a different graph input, then we will perform the usual `copy_()` on that other graph input

(b) the data mutation happened on the storage of `x_old`. This is more of a pain to handle, and doesn't currently work. At runtime, the right thing to do is probably something like:
```

def functionalized_f(x):
    x_view = x.view(-1)
    # set_() desugars into a no-op; later usages of x will use x_output
    x_output = torch.ones(2)
    # functionalize the mutation on x_view
    x_view_updated = x.mul(2)
    x_updated = x_view_updated.view(x.shape)
    # x experienced TWO TYPES of mutations; a data mutation and a metatadata mutation
    # We need to return both updated tensors in our graph
    return x_updated, x_output
def runtime_wrapper(x):
    x_data_mutation_result, x_set_mutation_result = compiled_graph(x)
    # First, perform the data mutation on x's old storage
    x.copy_(x_data_mutation_result)
    # Then, swap out the storage of x with the new storage
    x.set_(x_set_mutation_result)
```

There are two things that make this difficult to do though:

(1) Functionalization: the functionalization rule for `set_()` will fully throw away the old `FunctionalStorageImpl` on the graph input. So if there are any mutations to that `FunctionalStorageImpl` later on in the graph, the current graph input won't know about it. Maybe we can have a given `FunctionalTensorWrapper` remember all previous storages that it had, and track mutations on all of them - although this feels pretty complicated.

(2) AOTAutograd now needs to know that we might have *two* graph outputs that correspond to a single "mutated input", which is annoying.

It's worth pointing out that this issue is probably extremely unlikely for anyone to run into - can we just detect it and error? This feels slightly easier than solving it, although not significantly easier. We would still need `FunctionalTensorWrapper` to keep track of mutations on any of its "previous" storages, so it can report this info back to AOTAutograd so we can raise an error.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/111554
Approved by: https://github.com/ezyang

---
## [panzerr1944/f13tbd](https://github.com/panzerr1944/f13tbd)@[e208ee981e...](https://github.com/panzerr1944/f13tbd/commit/e208ee981e86227c2a19b6ae4e35f489be0b0de3)
#### Monday 2023-12-04 12:41:27 by SM45H

Khans map (My Git borked on last pr) (#285)

********* EDIT ***********
My last pr got closed because I was having errors with my github and had
to wipe it. The khamp is 90% the same as before. I removed the upper
level defense post and removed the lower sentry post's weather cover. I
added more trash piles in khamp, added an advanced workbench and two
advanced salvage spawns in the back thats protected with indestructible
walls so it cant be cheesed. I also made sure it was at the very end of
the bunker so it had to be earned. The back dungeon is much harder than
any other factions "down river". I also removed the wasteland medical
spawners, and replaced them with a few static meds. While I was mapping,
I fixed the church's zoning by heavens night, basically giving it a
roof.
********* EDIT ***********


Updated the khans, gave khamp character and flow, as well as beautifying
it. most of what was in the khamp as far as resources, was moved over
give or take a few things. moved the khans "down river" to the bunker
they use to run out of, filled with plenty of mobs. Most notable gear in
the back is one set of Khan armor(full helm and coat) as well as some
money and gunbook 3. Past servers, khans had a gun book down river. They
have to fight the khan killer ghoul and his little gang of attack
ghouls, and several mirelurks and a few mirelurk nests.

Gunpowder, metal, glass are with the spiders, and bbq sauce, mustard
packets, and hot sauce packets are guarded by mister handies and
cockroach. I added a few Easter eggs and funnies in khamp, that
including past khan dog, sunflower (forgor gurilla), a few batteries in
the river because, where else are you suppose to toss out your old car
batteries.

Khans base, while a bit bigger, does stay within the old dense rock
space they could mine out and stay within.





![image](https://github.com/f13babylon/f13babylon/assets/151568060/637ba21d-70f1-4eef-9ebc-2c8c31916b45)

![image](https://github.com/f13babylon/f13babylon/assets/151568060/c0574a7a-aa19-456d-baf9-5116107ed8b9)

![image](https://github.com/f13babylon/f13babylon/assets/151568060/fe2c4c81-f6ba-487a-a7c8-287bc8397ff1)

---
## [panzerr1944/f13tbd](https://github.com/panzerr1944/f13tbd)@[893e0e151c...](https://github.com/panzerr1944/f13tbd/commit/893e0e151c05648fd712f75e24520fc77354ed39)
#### Monday 2023-12-04 12:41:27 by lolman360

robot update/rework (#204)

## About The Pull Request

does a lot of changes to robots
all changes TBD

robots are now much faster (0.3 slowdown instead of 1).
they are also somewhat tankier across the board to compensate for their
lack of armor (0 armor btw)

robot modules have been revisited:
medical assaultron was rolled into medical borg and is now an altskin.
mining borg now has a shovel, and its emag module is a rocketsledge that
mines better and has 12 less damage.
engiborg's emag module is also a rocketsledge (uncreative)
assaultron was rolled into secborg and is now an altskin.
vtec has been nerfed significantly from -1 slowdown to -0.25

gutsy flamethrower nerfed significantly: 1s firedelay, 33% lower
projectile count, actual energy cost

all robots now have the wastebot faction, since all selectable sprites
are fo13 robots anyways. this also makes slugs do 90 damage to them,
which is extremely funny and something i might remove. again, tbd



## Why It's Good For The Game

as long as they're pickable they should be functional

## Pre-Merge Checklist
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.


## Changelog

:cl:
add: new stuff to robots
del: old stuff from robots
tweak: robots can now patch nests
balance: robots are overall buffed (holy shit their slowdown was
dogshit)
/:cl:

---
## [Kadantte/TavernAI](https://github.com/Kadantte/TavernAI)@[d3a4f43fbb...](https://github.com/Kadantte/TavernAI/commit/d3a4f43fbba708267059c19d10605e6b080d2f92)
#### Monday 2023-12-04 14:24:06 by FunkEngine

"Just closing the barn door a bit..."

(This first section is the TL;DR. with regards to the Sharp/WEBP vulns etc.) Closing the wide-open barn door here... Common sense applied etc. PNG is once again the default storage and export format for cards. While currently the 'Tavern_Card_V2' spec is not yet fully implemented (Or even nailed down, let be honest here.) but that is a thing in the works... At least we're back to the 'Tavern_Card_V1' spec again, now.

Nudging Sharp min required version up to 0.32.6, as 0.31.3 is a confirmed vulnerable version, and installs by default unless the user manually forces an audit, at which point (now, in the last few days.) some people will be unable to run tavern, due to major breaking changes in 0.33...
I chose specifically not to bump to 0.33.0 (which came out the other day) due to said major breaking changes, what with a sizable majority of our users (Or at least based on the reported user-agents that land on our GitHub page!) are running older systems. (I include myself in this group, although there are allegedly some using frighteningly deprecated systems than I am!)

0.32.6 is... For the moment at least, secure and compatible with the widest possible cross-section of our current and potential users.

While I sort of already had my sleeves rolled up and the long gloves on... I also noticed our own internal versioning was desynchronized at some point, and nudged the values in package/package-lock .jsons to match 1.5.2 which is our present official version.
((Honestly Humi, I'm almost tempted to say this push/commit should effectively be a '1.5.3' roll-up at this point, or similar update-alert triggering release should be planned for a 2023 End-of-the-Year roll-up in ~4 weeks time. To land us at 1.5.3, if not start us at straight up 1.6.0 at the changeover from 2023 to 2024.  Something to think about.))

Adjusted the "default defaults" (settings) to better reflect the contemporary median capabilities of the models in popular use. (context max etc.) To give a better first-impression on newer users. Also trying to get the string literal 'Pygmalion' out of as much as possible to prevent our colab from being flagged. As I find such minor references I either redact them, deprecate them,  or modify them. (Delete whole-cloth, make the Pygmalion one into the non-default option, and change to 'Pyg' or 'Classic-6B' etc, respectively. In this push I redacted both a single code comment with the string in it, and have set the name of the default preset used back to the Default-TavernAI settings from Classic-Pygmalion-6b which the settings.json file had set, and updated the actual settings values inside of both so that even people who switch back to the pyg-classic 'preset' out of force of habit will benefit from modern models and inference APIs, while officially 'deprecating' the named Pygmalion settings.)

In that same vein, or similar at least I have slightly changed the message printed to console by default during auto-launching, such that it no longer inadvertently confuses people by creating a clickable link to an inaccessible location when used as part of the colab notebook(s). It only appears when auto-run is enabled, so if you're running locally you're not clicking the 127.0.0.1 link in the first place... But it confuses so many people when colab prints it as a clickable URL in the output console. One less thing to confuse users.

This is both a QoL and newbie-onboarding change-decision, and will be slightly more relevant in a followup commit that further enhances, refines, and streamlines the TavernAI colab user experience that's in the oven at the moment. (Slightly over half-baked as I type this up, and it is starting to smell good.)  Look for that possibly as soon as Monday.

Still trying my best to end 2023 on a high note here for us all, folks. :)
--FunkEngine

(Also) Just about made a fool of myself this morning...
https://github.com/FunkEngine2023/FunkEngine2023.github.io/assets/123712145/5324b650-9e0e-42ee-b6ba-635a3ecfd37c

And hey look I've been baking this commit for over 36 hours now, that was yesterday morning!

Fixed issues with start.bat. Added proper *#%(*% shortcut to open a PowerShell window already set and in the relevant CWD so that there's literally no excuse anymore to not put their hands on the wheel for once...

Then I fixed the bat even more better-er... Fully deprecated the string literal 'Pygmalion" from the code... I don't live in fear of Google... I just don't want to give them any plausible justification to throw us under the bus... (I mean they continue adding "Verboten!" code to the signatures dictionary... SDWUI and ComfyUI being the more notable ones since Pyg took one for the team, and became the lesson for us all in the process.

Round about that time I had also finished fixing up the readme.md with a bit more detail about the process, and adding icons for the downloads...

Then I went down a brief rabbit-hole and literally got a one touch solution as far as "making the TavernAI go *brrrrrrrrrr*" goes...  Plus I left all the prior solutions there in place, and in better condition than they possibly have ever been.  Not sure if I want to go back and mangle markdown to update the readme before I finally push this long overdue boat of a commit down the slipway...

The short answer is: To run TavernAI there's a shortcut right there in the directory, called "TAVERN_CONSOLE" and you just double click it and it takes care of the whole bpm install and standing node up with server.js...  In actual proper PowerShell!

Finishing up testing on several various test environments to make sure that the .bat, the TAVERN_CONSOLE shortcut, and the "CONSOLE" shortcut all function port-ably as  I intend them to. (The "CONSOLE" just opens a PowerShell window in the CWD of wherever the shortcut is to launch it. This will enable things like manually `npm audit fix --force` for those who wouldn't have the slightest idea how to open a PowerShell otherwise.

Big QoL roll-up here. I'll leave merging the colab changes in for Monday or Tuesday.

And now here I am just after midnight pushing this on MONDAY MORNING. :3

-- 0200 approaches and I'm still not satisfied with the colab... It is still less broken than it previously was. I'll leave that for another day.  Happy Monday Morning to you all!

--FunkEngine. (Josh S.)

---
## [Huz2e/massmeta](https://github.com/Huz2e/massmeta)@[349adbb438...](https://github.com/Huz2e/massmeta/commit/349adbb438d5ca216b8f76c5251a1bf90473e0ce)
#### Monday 2023-12-04 14:31:03 by Ghom

[NO GBP] Fixing elevation furthermore (#80099)

## About The Pull Request
fixes #80059
fixes #80085.

The tram transportation doesn't use `forceMove()`, instead it just
changes the location of the objects directly. What's more, it doesn't
call `oldloc.Exited()` or `loc.Entered()` but only for areas. The
abstract exited/entered signals are from `Moved()` though, which is
called.

https://github.com/tgstation/tgstation/blob/df4bc6d948576a2ec32a90c23c93ec90e54e3933/code/modules/transport/transport_module.dm#L519-L527

About beds, well, I just happened to put a minus symbol where it
shouldn't be.

## Why It's Good For The Game
Truly one of the fuckups of the year. Now tested. I'll make a unit test
later.


## Changelog

:cl:
fix: Fixed some oopsie whoopsie with elevation, trams and beds causing
people to visually ascend or descend to heaven or hell.
/:cl:

---
## [Aman1763/MRHG](https://github.com/Aman1763/MRHG)@[3e57d77885...](https://github.com/Aman1763/MRHG/commit/3e57d778856b1968a90bc8c453129003b98fe386)
#### Monday 2023-12-04 15:11:42 by Wyatt Borden

finished generating the prompt from any starting position. is it spaghetti code? yeah, kinda. Does it work? Fuck yeah it works. are there some bugs? What kind of a question is that, of course there are bugs!

---
## [samnordmann/Fuser](https://github.com/samnordmann/Fuser)@[922fab891f...](https://github.com/samnordmann/Fuser/commit/922fab891f98f2cedb7fc7f8a408000e9c874309)
#### Monday 2023-12-04 15:14:49 by Gao, Xiang

Refactor ldmatrix and mma input scheduling (#1303)

This PR is stacked on https://github.com/NVIDIA/Fuser/pull/1311

Similar to https://github.com/NVIDIA/Fuser/pull/1210, this PR schedules
the allocation domain of mma inputs and ldmatrix. Similar to the
situation of https://github.com/NVIDIA/Fuser/pull/1210, the modified
piece of code was initially implemented prior to the invention of
allocation, therefore there were some hacks around there.

For the case of ldmatrix, if you look at the official doc
https://docs.nvidia.com/cuda/parallel-thread-execution/index.html#warp-level-matrix-instructions-ldmatrix,
you will find that, there are basically two correct but different
schedules:
1. If you look at the memory format of which thread own which part of
the tensor, from this information, you will able to derive one schedule.
Let's call this memory-layout-based schedule.
2. If you look at which thread should pass the address of which item as
an operand to this instruction, from this information, you will be able
to derive another schedule. Let's call this indexing-based schedule.

Unfortunately, these two schedules does not match. Prior to this PR, we
were uniquely using the indexing-based schedule. This is fine with
ldmatrix, but the index of mma inputs is basically incorrect, and
therefore a hacked index was used.

I believe the most natural way to implement these two separate schedules
is as follows: Assume we have a fusion:
```C++
Tregister = ldmatrix(Tsmem)
Tregister2 = broadcast(Tregister)
... = mma(Tregister2, ...)
```
then the allocation domain of `Tregister2` and `Tregister` must be
scheduled as memory-layout-based schedule, the leaf domain of
`Tregister` must be scheduled as the indexing-based schedule. The leaf
domain of `Tregister2` should be scheduled similar to
memory-layout-based schedule.

In this PR, I refactored the mma swizzler for mma inputs to implement
the above design. In the refactored code, `scheduleTuringOperandRead`
schedules the memory-layout-based schedule, and `scheduleLdMatrix`
starts from the memory-layout based schedule, and generates the
indexing-based schedule on top of it.

Due to this change, the codegen of `MmaOp` no longer needs special
handling the index, it is now just a naive:
```C++
  void handle(const MmaOp* mma) final {
    indent() << genMmaOp(mma) << "(\n";
    indent() << kTab << gen(mma->out()) << ",\n";
    indent() << kTab << gen(mma->inA()) << ",\n";
    indent() << kTab << gen(mma->inB());
    code_ << ");\n";
  }
```

However, our current sync analysis and indexing infrastructure is not
capable of analyzes this style of scheduling, and therefore, I would
need to add additional hacking points to them:

- In our sync analysis, currently, it always assume that the
parallelization of the leaf domain determines which thread owns which
item. With the allocation domain support, it is actually the
parallelization of the *allocation* domain determines which thread owns
which item. In a perfect world, for exprs other than ldmatrix, warp
shuffling, and mma op, the analysis based on leaf domain should match
with the analysis based on the allocation, because, for example, if you
do `y = sin(x)`, there is no way that `y` get the result from other
threads, but our system should not assume that the analysis based on
leaf domain always match with the analysis based on the allocation
generally. Unfortunately, at the current state, our system can not
handle this correctly. So I added one hack to it: if the expr is
ldmatrix, assume the schedule is correct and just give up sync analysis.
I think for now, this is a valid solution, because we will be rewriting
our sync analysis with `IdModel` anyway.
- In our indexing of `MmaOp` producer, we are incorrectly marking some
of allocation domain as zero domain, where it should not be. Similar to
the above point, the mma op implies warp shuffling of data. During
indexing, it does make sense to replay consumer as producer, but only to
the block level. Within a warp, it makes no sense to replay the producer
as consumer. I think we should carefully think about the design when we
are rewriting our indexing with `IdModel`, but for this PR, I just
manually set the last three `IterDomain`s of mma input as special and
not treat them as zero domain.

I believe this PR is an improvement compared to the previous approach,
because it has less special handling in the schedule itself, but I still
think we are far from supporting ldmatrix and mma ops elegantly. In the
future, I think we should:
1. Reconsider the design of different domains, leaf vs allocation, etc.
and figure out what is the best way to schedule ldmatrix.
2. When we rewriting, we should keep the indexing of ldmatrix and mma in
mind, and make sure that it can be supported without any hack in the new
system.

---
## [StrangeWeirdKitten/Bubberstation](https://github.com/StrangeWeirdKitten/Bubberstation)@[b5e095e380...](https://github.com/StrangeWeirdKitten/Bubberstation/commit/b5e095e380e729793628d254bb441f51ecdb046b)
#### Monday 2023-12-04 15:51:20 by Waterpig

[MODULAR] Refactors (hopefully) all borg modular changes into one module, adds raptor borgs (#777)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Originally I was supposed to only add raptor borgs, but I am simply too
insane to let this shitcode slide.

Moves most if not all borg modular changes into one module folder
because by god these were spread out over like 8 files.
Improves modularity a bit by moving some borg related bubber edits on
skyrat into our modular files.
Adds raptor borgs

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Modularity good.
Code organizing good.

https://en.wikipedia.org/wiki/Technical_debt

Also new borg sprites are cool, I guess. See icondiff bot for those
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

:cl:
image: New borg sprites: Raptor
refactor: Moved most if not all bubber borg code into one modular folder
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- By opening a pull request. You have read and understood the
repository rules located on the main README.md on this project. -->

---
## [NixOS/nix.dev](https://github.com/NixOS/nix.dev)@[21bfef408a...](https://github.com/NixOS/nix.dev/commit/21bfef408a3544a8681eedaa6ace5c5cd4f948cd)
#### Monday 2023-12-04 16:10:48 by fricklerhandwerk

host Nix reference manual on nix.dev

this is the most cursed setup you will see any time soon.

we're dumping the Nix manual unchanged into the build tree *after*
building. the reason is that we'd want to link to it from our table of
contents, but because Sphinx does not allow adding arbitrary files to
the build output in arbitrary locations (only `_static` works). but we
want to place the manual behind a particular URL, and the alternative of
maintaining URL rewrites (e.g. in nginx) is not accessible here because the
infrastructure is managed somewhere else.

now that the files won't appear in their desired locations at Sphinx
build time, we can't use relative links to reference them, therefore we
have to resort to pointing to the web URL the manual will appear at.
this is terrible and I'm sorry. please fix this if you have a better
idea. once we use URLs though, we have to avoid linkchecking, since
those files may not be there before deploying them.

figuring all of this out took way longer than anyone would wish.

Co-authored-by: Alejandro Sanchez Medina <alejandrosanchzmedina@gmail.com>

---
## [LOuroboros/pokeemerald](https://github.com/LOuroboros/pokeemerald)@[496df1a86e...](https://github.com/LOuroboros/pokeemerald/commit/496df1a86e1ecadca39d4eb2c3676f37aede6ecc)
#### Monday 2023-12-04 16:13:53 by LOuroboros

Cleaned up src/wonder_trade.c quite a bit

Summary of Changes:
-Updated and shortened EventScript_DoWonderTrade
 -Now it won't activate a WT if the Player has no Pokémon.
 -It will also not ask if they want to perform another one.
-Created a header file for src/wonder_trade.c in which to define any global functions.
 -I actually had to do this because the modern compiler errors out otherwise, lel.
-Updated the value assigned to the femaleWTNames array.
-Replaced the usages of the POKEMON_EXPANSION and ITEM_EXPANSION labels with usages of RHH_EXPANSION instead.
 -I don't want to offer support for super out of date projects.
-Performed updates to make this build properly on modern versions of GCC.
-Assigned the static prefix to most of the functions exclusive to the Wonder Trade system.
-Properly defined the static functions in src/wonder_trade.c near the top of the file.
-Fixed, updated and uncommented the if statement that can assign a WT Pokémon its Hidden Ability.
-Refactored IsMegaPreEvolution due to the form change changes made to the pokeemerald-expansion, with Ax6's help
 -From now on it shall be called "IsSpeciesFamilyMegaEvolutionCompatible".
 -It only reads 2 parameters now instead of 3.
-Updated the values assigned in sIsInvalidItem for readability purposes.
-Added valid Gen. 9 species to sIsValidSpecies now that those are implemented in the expansion.
-Heavily updated CreateWonderTradePokemon.
 -Got rid of pointless variables.
 -Updated the order of the existing variables.
 -Renamed some of them too for readability's sake.
 -I also renamed gIngameTrades to sWonderTrades and made it more readable as well.
-Renamed determineEvolution to GetWonderTradeEvolutionTargetSpecies.
-Refactored GetValidHeldItemForSpecies.
 -It now re-rolls not just HMs but also TMs.
 -It also re-rolls items with an Importance of 1 or higher.
 -It no longer filters out certain combos like ITEM_THICK_CLUB and Pikachu. There's value in generating items like that which can be sold for money.
-Made the action of evolving a Pokémon generated via Wonder Trade happen after they've been given a valid item.
-Removed the 30% chance of giving an Everstone to Pokémon that evolve via trade that are received via Wonder Trade.
 -Honestly, I don't know why did Lunos from the Past add this, but it just feels so mean lol. I don't think I want to keep it in.
-Updated the code of the 30% chance to give a Pokémon received via WT the item they may need to evolve.
 -Now it's handled similarly to the Lucky Egg that wild Chansey can carry in Pokémon FRLG.

To Do:
-Write the rest of the commit.

---
## [readthedocs/readthedocs.org](https://github.com/readthedocs/readthedocs.org)@[ea6503eb6f...](https://github.com/readthedocs/readthedocs.org/commit/ea6503eb6fbfb3eb7c77830407b05012997e3ce0)
#### Monday 2023-12-04 16:15:17 by Anthony

Add organization view UI filters (#10847)

* Add organization view UI filters

This filters are used for the new dashboard UI, they are not API filters.

These were a challenge to create, as django-filter is really opinionated
about the way it should work, and doesn't quite agree with use cases
that need to use filtered querysets (such as limiting the field choices
to objects the organization is related to).

I went through many permutations of this code, trying to find a pattern
that was not obtuse or awful. Unfortunately, I don't quite like the
patterns here, but because all of the django-filter magic happens at the
class level instead of at instantiation time, every direction required
hacks to obtain something reasonable.

Given the use we have for filters in our UI, I wouldn't mind making
these into a more generalized filter solution.

I think I'd like to replace some of the existing filters that currently
hit the API with frontend code and replace those with proper filters
too. These are mostly the project/version listing elements.

* Add filter for organization dropdown

This replaces an API driven UI element. It's not important that these UI
filters are frontend, it was just easier than figuring out how to make
django-filter work for this use case at that time.

* Fix the team member filter yet again

* Use a custom filter field to execute filter set queryset method

* Add tests organization filter sets

* Update code comments

* A few more improvements

- Make view code nicer, use django_filters.views.FilterMixin, sort of
- Use FilterSet.is_valid() to give empty list on validation errors
- Clean up tests with standard fixtures instead

* Review updates for tests and arguments

* Rename FilterMixin -> FilterContextMixin

* Fix lint

---
## [LOuroboros/pokeemerald](https://github.com/LOuroboros/pokeemerald)@[360ff0d047...](https://github.com/LOuroboros/pokeemerald/commit/360ff0d04724d9dc1fe2777d45408e093a8e5e19)
#### Monday 2023-12-04 16:36:28 by LOuroboros

Cleaned up src/wonder_trade.c quite a bit

Summary of Changes:
-Updated and shortened EventScript_DoWonderTrade
 -Now it won't activate a WT if the Player has no Pokémon.
 -It will also not ask if they want to perform another one.
-Created a header file for src/wonder_trade.c in which to define any global functions.
 -I actually had to do this because the modern compiler errors out otherwise, lel.
-Updated the value assigned to the femaleWTNames array.
-Replaced the usages of the POKEMON_EXPANSION and ITEM_EXPANSION labels with usages of RHH_EXPANSION instead.
 -I don't want to offer support for super out of date projects.
-Performed updates to make this build properly on modern versions of GCC.
-Assigned the static prefix to most of the functions exclusive to the Wonder Trade system.
-Renamed getWonderTradeOT to GetWonderTradeOT.
-Properly defined the static functions in src/wonder_trade.c near the top of the file.
-Fixed, updated and uncommented the if statement that can assign a WT Pokémon its Hidden Ability.
-Refactored IsMegaPreEvolution due to the form change changes made to the pokeemerald-expansion, with Ax6's help
 -From now on it shall be called "IsSpeciesFamilyMegaEvolutionCompatible".
 -It only reads 2 parameters now instead of 3.
-Updated the values assigned in sIsInvalidItem for readability purposes.
-Updated sIsValidSpecies
 -Added the Gen. 9 species.
 -Removed the Kantonian Mr. Mime for Pokeemerald-expansion based projects.
-Heavily updated CreateWonderTradePokemon.
 -Got rid of pointless variables including the pointless whichPlayerMon function parameter.
 -Updated the order of the existing variables to better reflect the order in which they're used.
 -Renamed some of them too for readability's sake.
 -I also renamed the struct InGameTrade and anything using it in CreateWonderTradePokemon to make things more readable and accurate.
 -Made the action of evolving a Pokémon generated via Wonder Trade happen after they've been given a valid item.
 -Removed the 30% chance of giving an Everstone to Pokémon that evolve via trade that are received via Wonder Trade.
  -Honestly, I don't know why did Lunos from the Past add this, but it just feels so mean lol. I don't think I want to keep it in.
 -Updated the code of the 30% chance to give a Pokémon received via WT the item they may need to evolve.
  -Now it's handled similarly to the Lucky Egg that wild Chansey can carry in Pokémon FRLG.
 -Updated the parameters passed through the CreateMon call.
-Updated determineEvolution
 -Renamed it to GetWonderTradeEvolutionTargetSpecies.
 -Updated its variables for readability.
 -Added the new evo methods present in the Pokeemerald-expansion that were missing.
-Refactored GetValidHeldItemForSpecies.
 -It now re-rolls not just HMs but also TMs.
 -It also re-rolls items with an Importance of 1 or higher.
 -It no longer filters out certain combos like ITEM_THICK_CLUB and Pikachu. There's value in generating items like that which can be sold for money.

---
## [runwhen-contrib/runwhen-local](https://github.com/runwhen-contrib/runwhen-local)@[732530f4c9...](https://github.com/runwhen-contrib/runwhen-local/commit/732530f4c92cb0f923871c1200d325b871a2117a)
#### Monday 2023-12-04 16:53:34 by Rob Vaterlaus

Refactor Kubenetes dependencies into platform helper class (#380)

* Refactor Kubenetes dependencies into platform helper class

- added new PlatformHandler class that's subclasses for different
  platforms to implement the platform-specific logic
- currently there's just the Kubernetes implementation but soon there
  will be other ones corresponding to new platforms that are indexable
  via CloudQuery
- added support for enum-based settings, specified by which enum class to
  use to represent the class, plus an optional constructor method to use
  to convert the value from the request data to the enum. As part of this
  I improved the error handling for the setting conversion code a bit to
  give better error messages if the user specifies an invalid value.
- switched the defaultLOD setting to be an enum setting backed by the
  LevelOfDetail class
- with this change users can now use the symbolic/string values for the
  level of detail settings instead of the previous not-super-user-friendly
  integer values (0="none",1="basic",2="detailed")
- the integer values are still supported, but deprecated
- got rid of the hclod enricher component, which previously just set up
  the level of detail values for the namespace resources. Now this is
  just done directly in the kubeapi indexer when it creates the resources
  (although I think probably the level of detail value shouldn't be stored
  in the resources and should just be handled directly in the gen rules
  code, but I'm leaving that change for later).
- cleaned up the way data is passed to match predicates to clean up some
  places that previously used global variables
- also implemented a generic visitor pattern for the match predicates to
  replace the previous hacky code that was used to collect all of the
  custom resource type references so that the indexer only need to
  handle custom resources that were referenced.
- this collector also collects the non-custom resource types that are
  accessed too, which will enable the indexers to be optimized a little
  more by only indexing the resource types that are accessed (although
  the kubeapi indexer isn't taking advantage of this yet).
- fixed a few more bugs that were fallout from the neo4j removal, e.g.
  some cases where it wasn't checking for a null resource type result
  from Registry.get_resource_type before trying to access the instances

* Bug fix to remove obsolete hclod component from run.sh

* fix debug line

* fix registry in rump resources

* Some tweaks to the bug fix for dump_resources

* Fixed the code in map_customization_rules to use the platform handler

- this was a place I missed in my initial commit that still had some
  things that were hard-coded for Kubernetes
- I added another method to the PlatformHandler interface to deal with
  looking up the platform-specific property values that are matched
  against in the match predicates.
- currently there's some overlap (at least in the Kubernetes case) between
  the special template values that are supported for template expansion
  and the property values that are supported for match predicates (i.e.
  the same values of "context", "cluster" and "namespace" are supported
  in both cases), so there's probably some way these things can be
  unified, but I'll leave that for later, since it's more important right
  now to get this merged sooner rather than later.
- I also cleaned up some of the debug logging code that Shea had added at
  various places in the code. Now it's unified in the Django settings.py
  file where the logging is configured. This supports the same
  DEBUG_LOGGING environment variable, but it's applied to the root logger,
  so it will affect things globally. The idea would be that if you want
  to enable debug logging more narrowly you could do that by tweaking the
  logging config in settings.py to set the log levels for specific
  python modules. If that proves to be inconvenient, we can revisit.

* Include info about the source gen rule as an annotation in the SLX files

- this includes the repo URL, ref, and path for the source generation
  rule that generated the SLX. The repo URL and ref are probably
  redundant because that info is typically specified in the spec part of
  the SLX (or SLI/runbook). But it does make it a bit more convenient to
  have it there as an annotation when tracking down gen rule issues.
- also cleaned up some of the type annotations for settings

* Fixed regression with handling of custom variable match predicates

- this was broken with the initial pass of the Kubernetes refactoring
- the original way of specifying a custom variable match (i.e. as a
  resource pattern match where the resourceType was "variables" and the
  properties was a single entry list with the path to look up in the
  variables) was sort of clumsily hacked into the existing resource
  match predicate implementation, but that code was pretty ugly and used
  a lot of parameter type overloading, so I decided to clean that up by
  creating a new custom variable match predicate implementation that
  more directly/intuitively handles the variable lookup/match case.
- unfortunately we currently don't have a good way to add new gen rule
  features and adopt them in the code bundles without breaking users using
  older versions of the workspace builder (which I think we need to fix
  soon). So I wrote some backwards compatibility code that converts the
  old way of specifying the variable match into a construction of the
  new custom variable match predicate type. We'll probably need to keep
  that around for at least a little while until we're fairly sure that
  everyone's running a newer version.

---------

Co-authored-by: Rob Vaterlaus <rob.vaterlaus@runwhen.com>
Co-authored-by: Shea Stewart <stewart.shea@gmail.com>

---
## [marcovc/services](https://github.com/marcovc/services)@[1fe4c4485a...](https://github.com/marcovc/services/commit/1fe4c4485a2d5d8a557ff663a5163c9d83f9ec25)
#### Monday 2023-12-04 17:13:12 by Martin Beckmann

Reduce memory consumption of `RecentBlockCache` (#2102)

# Description
Our `RecentBlockCache` works like this:
1. somebody requests liquidity
2. cache checks if it's already known
3. if it's not in the cache query the blockchain
4. store in cache
5. remember requested liquidity source for updating it in the background

Whenever we see a new block we fetch the current liquidity for all the
liquidity sources and write them to the cache together with their block.
We have a max cache duration. Whenever the cached state exceeds that
duration we remove the oldest entries.

This implementation uses unnecessarily much memory in 2 ways:
1. We can fetch liquidity for quotes. For those requests it's okay to
return liquidity that is not 100% up-to-date. However, we still remember
the requested liquidity source for future updates. This is not great
because we can receive quote requests for all sorts of random tokens
we'll never see again.
2. We cache state for the same liquidity source for multiple blocks. But
the cache only has 2 access patterns:
    * "Give me the most recent available on the blockchain"
    * "Give me the most recent available in the cache"
There is no access pattern "Give me cached liquidity specifically from
an older block with number X"
That means it's enough to keep the most recent data for any liquidity
pool cached at any point.
    
We can see these 2 things at play with this
[log](https://production-6de61f.kb.eu-central-1.aws.cloud.es.io/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:'2023-11-28T16:18:27.243Z',to:'2023-11-28T17:55:08.577Z'))&_a=(columns:!(log),filters:!(),grid:(columns:('@timestamp':(width:164))),index:c0e240e0-d9b3-11ed-b0e6-e361adffce0b,interval:auto,query:(language:kuery,query:'mainnet%20and%20driver%20and%20(log:%20%22the%20cache%20now%20contains%20entries%22%20or%20log:%20%22fetched%20liquidity%20sources%22)'),sort:!(!('@timestamp',desc)))).
After ~1h of operation it shows a single `RecentBlockCache` holding ~20K
items. On an average auction we can fetch ~800 uni v2 sources. We
currently have a configuration where we cache up to 10 blocks worth of
data. Meaning we have roughly 8K cache entries for liquidity that is
needed in auction and 12K entries that's only needed for quotes.
Also this is only for a single univ2 like liquidity source. In total we
have 4 different ones configured in our backend.

# Changes
We address `1` by not remembering liquidity sources for background
updates for quote requests.
We address `2` by throwing away all the duplicated data.

## How to test
I did a manual set up where I run an autopilot locally in shadow mode
(fetch auction from prod mainnet) and a driver with all liquidity
sources enabled.
I collected 3 graphs in total to measure the impact of this change on
the memory.
1. This graph is the status quo (very noisy and not really reproducable
across runs)
<img width="1617" alt="0_current_no_optimizations"
src="https://github.com/cowprotocol/services/assets/19190235/0997b34f-8f30-43c4-a797-5e3cf7bccbbf">

2. This graph applies one optimization that is not part of this PR to
make the memory consumption more predictable across runs. I want to
merge that optimization as well but right now it's very hacky. However,
I will include this optimization in all my graphs because it makes the
impact of each optimization easier to spot.
<img width="1420" alt="1_with_univ2_call_optimization"
src="https://github.com/cowprotocol/services/assets/19190235/6f259fa4-4fcd-45dd-ba37-160962065ab3">

3. The effects of this PR's optimization. The memory usage is more
stable over all and grows less over time.
<img width="1607" alt="2_cache_eviction"
src="https://github.com/cowprotocol/services/assets/19190235/ec5b5712-e4e3-4c4e-8feb-dc46e2cfa3f3">

---
## [CoolistKovbel/brokenPlay](https://github.com/CoolistKovbel/brokenPlay)@[8f4d31c244...](https://github.com/CoolistKovbel/brokenPlay/commit/8f4d31c244b4ac73363672e2d39645efdc798433)
#### Monday 2023-12-04 17:21:21 by Lyubomyr Kovbel

fucking hate my fucking life, fucking hate type script, fucking hate how fucking blind and fuking destored my ego got, thanks mother fuckers hope to all a good fucking day. pls ->1EBKdZ6rfUcDxR3uPfAsKcnPgaYm9zCUp2 <-btc

---
## [neondatabase/neon](https://github.com/neondatabase/neon)@[c7f1143e57...](https://github.com/neondatabase/neon/commit/c7f1143e570924eadd15053949647707ba042c5b)
#### Monday 2023-12-04 17:22:29 by Christian Schwarz

concurrency-limit low-priority initial logical size calculation [v2] (#6000)

Problem
-------

Before this PR, there was no concurrency limit on initial logical size
computations.

While logical size computations are lazy in theory, in practice
(production), they happen in a short timeframe after restart.

This means that on a PS with 20k tenants, we'd have up to 20k concurrent
initial logical size calculation requests.

This is self-inflicted needless overload.

This hasn't been a problem so far because the `.await` points on the
logical size calculation path never return `Pending`, hence we have a
natural concurrency limit of the number of executor threads.
But, as soon as we return `Pending` somewhere in the logical size
calculation path, other concurrent tasks get scheduled by tokio.
If these other tasks are also logical size calculations, they eventually
pound on the same bottleneck.

For example, in #5479, we want to switch the VirtualFile descriptor
cache to a `tokio::sync::RwLock`, which makes us return `Pending`, and
without measures like this patch, after PS restart, VirtualFile
descriptor cache thrashes heavily for 2 hours until all the logical size
calculations have been computed and the degree of concurrency /
concurrent VirtualFile operations is down to regular levels.
See the *Experiment* section below for details.

<!-- Experiments (see below) show that plain #5479 causes heavy
thrashing of the VirtualFile descriptor cache.
The high degree of concurrency is too much for 
In the case of #5479 the VirtualFile descriptor cache size starts
thrashing heavily.


-->

Background
----------

Before this PR, initial logical size calculation was spawned lazily on
first call to `Timeline::get_current_logical_size()`.

In practice (prod), the lazy calculation is triggered by
`WalReceiverConnectionHandler` if the timeline is active according to
storage broker, or by the first iteration of consumption metrics worker
after restart (`MetricsCollection`).

The spawns by walreceiver are high-priority because logical size is
needed by Safekeepers (via walreceiver `PageserverFeedback`) to enforce
the project logical size limit.
The spawns by metrics collection are not on the user-critical path and
hence low-priority. [^consumption_metrics_slo]

[^consumption_metrics_slo]: We can't delay metrics collection
indefintely because there are TBD internal SLOs tied to metrics
collection happening in a timeline manner
(https://github.com/neondatabase/cloud/issues/7408). But let's ignore
that in this issue.

The ratio of walreceiver-initiated spawns vs
consumption-metrics-initiated spawns can be reconstructed from logs
(`spawning logical size computation from context of task kind {:?}"`).
PR #5995 and #6018 adds metrics for this.

First investigation of the ratio lead to the discovery that walreceiver
spawns 75% of init logical size computations.
That's because of two bugs:
- In Safekeepers: https://github.com/neondatabase/neon/issues/5993
- In interaction between Pageservers and Safekeepers:
https://github.com/neondatabase/neon/issues/5962

The safekeeper bug is likely primarily responsible but we don't have the
data yet. The metrics will hopefully provide some insights.

When assessing production-readiness of this PR, please assume that
neither of these bugs are fixed yet.


Changes In This PR
------------------

With this PR, initial logical size calculation is reworked as follows:

First, all initial logical size calculation task_mgr tasks are started
early, as part of timeline activation, and run a retry loop with long
back-off until success. This removes the lazy computation; it was
needless complexity because in practice, we compute all logical sizes
anyways, because consumption metrics collects it.

Second, within the initial logical size calculation task, each attempt
queues behind the background loop concurrency limiter semaphore. This
fixes the performance issue that we pointed out in the "Problem" section
earlier.

Third, there is a twist to queuing behind the background loop
concurrency limiter semaphore. Logical size is needed by Safekeepers
(via walreceiver `PageserverFeedback`) to enforce the project logical
size limit. However, we currently do open walreceiver connections even
before we have an exact logical size. That's bad, and I'll build on top
of this PR to fix that
(https://github.com/neondatabase/neon/issues/5963). But, for the
purposes of this PR, we don't want to introduce a regression, i.e., we
don't want to provide an exact value later than before this PR. The
solution is to introduce a priority-boosting mechanism
(`GetLogicalSizePriority`), allowing callers of
`Timeline::get_current_logical_size` to specify how urgently they need
an exact value. The effect of specifying high urgency is that the
initial logical size calculation task for the timeline will skip the
concurrency limiting semaphore. This should yield effectively the same
behavior as we had before this PR with lazy spawning.

Last, the priority-boosting mechanism obsoletes the `init_order`'s grace
period for initial logical size calculations. It's a separate commit to
reduce the churn during review. We can drop that commit if people think
it's too much churn, and commit it later once we know this PR here
worked as intended.

Experiment With #5479 
---------------------

I validated this PR combined with #5479 to assess whether we're making
forward progress towards asyncification.

The setup is an `i3en.3xlarge` instance with 20k tenants, each with one
timeline that has 9 layers.
All tenants are inactive, i.e., not known to SKs nor storage broker.
This means all initial logical size calculations are spawned by
consumption metrics `MetricsCollection` task kind.
The consumption metrics worker starts requesting logical sizes at low
priority immediately after restart. This is achieved by deleting the
consumption metrics cache file on disk before starting
PS.[^consumption_metrics_cache_file]

[^consumption_metrics_cache_file] Consumption metrics worker persists
its interval across restarts to achieve persistent reporting intervals
across PS restarts; delete the state file on disk to get predictable
(and I believe worst-case in terms of concurrency during PS restart)
behavior.

Before this patch, all of these timelines would all do their initial
logical size calculation in parallel, leading to extreme thrashing in
page cache and virtual file cache.

With this patch, the virtual file cache thrashing is reduced
significantly (from 80k `open`-system-calls/second to ~500
`open`-system-calls/second during loading).


### Critique

The obvious critique with above experiment is that there's no skipping
of the semaphore, i.e., the priority-boosting aspect of this PR is not
exercised.

If even just 1% of our 20k tenants in the setup were active in
SK/storage_broker, then 200 logical size calculations would skip the
limiting semaphore immediately after restart and run concurrently.

Further critique: given the two bugs wrt timeline inactive vs active
state that were mentioned in the Background section, we could have 75%
of our 20k tenants being (falsely) active on restart.

So... (next section)

This Doesn't Make Us Ready For Async VirtualFile
------------------------------------------------

This PR is a step towards asynchronous `VirtualFile`, aka, #5479 or even
#4744.

But it doesn't yet enable us to ship #5479.

The reason is that this PR doesn't limit the amount of high-priority
logical size computations.
If there are many high-priority logical size calculations requested,
we'll fall over like we did if #5479 is applied without this PR.
And currently, at very least due to the bugs mentioned in the Background
section, we run thousands of high-priority logical size calculations on
PS startup in prod.

So, at a minimum, we need to fix these bugs.

Then we can ship #5479 and #4744, and things will likely be fine under
normal operation.

But in high-traffic situations, overload problems will still be more
likely to happen, e.g., VirtualFile cache descriptor thrashing.
The solution candidates for that are orthogonal to this PR though:
* global concurrency limiting
* per-tenant rate limiting => #5899
* load shedding
* scaling bottleneck resources (fd cache size (neondatabase/cloud#8351),
page cache size(neondatabase/cloud#8351), spread load across more PSes,
etc)

Conclusion
----------

Even with the remarks from in the previous section, we should merge this
PR because:
1. it's an improvement over the status quo (esp. if the aforementioned
bugs wrt timeline active / inactive are fixed)
2. it prepares the way for
https://github.com/neondatabase/neon/pull/6010
3. it gets us close to shipping #5479 and #4744

---
## [FranciscoZHQ/DIY-ITC-Game-Project](https://github.com/FranciscoZHQ/DIY-ITC-Game-Project)@[f80ca8bf1a...](https://github.com/FranciscoZHQ/DIY-ITC-Game-Project/commit/f80ca8bf1a57cd13153498d78eeb58998d9d57e1)
#### Monday 2023-12-04 17:32:58 by Cheemerr

okay maybe this will finally work

holy shit this took way too long I'm sorry everyone

---
## [KingkumaArt/KingkumaTGSS13](https://github.com/KingkumaArt/KingkumaTGSS13)@[30dae8899b...](https://github.com/KingkumaArt/KingkumaTGSS13/commit/30dae8899bad0007ae9220f1fc10be16908dd1a9)
#### Monday 2023-12-04 17:45:29 by Kyle Spier-Swenson

fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#79783)

This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

---
## [sprudello/Finance-Manager-LB-M294](https://github.com/sprudello/Finance-Manager-LB-M294)@[8957399d22...](https://github.com/sprudello/Finance-Manager-LB-M294/commit/8957399d22d978df2d77e0e27b0fc1a0733678cd)
#### Monday 2023-12-04 17:59:03 by sprudello

I want to die

Literally changed everything...
again I hate my life

---
## [lachesis17/EQ-Plugin](https://github.com/lachesis17/EQ-Plugin)@[1b5ea2b72f...](https://github.com/lachesis17/EQ-Plugin/commit/1b5ea2b72f13691d1b948d03bc21f4e698b0fd37)
#### Monday 2023-12-04 18:12:13 by Anton

class spectrum, right channel path, change colours

oscillator added to pluginprocessor to make some annoying sine wave tests

below is a bunch of troubleshooting i tried when trying to paint() both channel paths to the spectrum analyzer. the FTT generator puts the blocks into a queue but this completely shits the bed on small buffer sizes. my audio interface was set to 48kHz and 128 buffer size, which was just too small to use. anything over 500 buffer size seems to work okay, so I'm guessing its a multiple math problem (496?). increasing the buffer size adds latency, so there's a big trade-off for being able to constantly repaint the GUI window to show the buffered blocks of audio data and having it work at all

pathproducer and the added classes work but when trying to repaint() both paths in the timercallback its just too much for the GUI to handle and will either crash or freeze, even without playing anything through it

startTimerHz(60); can be played around with but doesn't really help for performance

tried adding/changing the orders which will either do nothing or hard crash the memory...
enum FFTOrder
{
    order2048 = 11,
    order4096 = 12,
    order8192 = 13
};

changing the binsize will just cause the rendering of the lines to be whacked since it's not drawing the correct hz

at the moment it feels like the only thing to do is to run the spectrum analyzer in mono only, commenting out the right path from timerCallback() and not drawing the strokepath or setting the rightpath in ResponseCurveComponent::paint, or just whack up the buffer size

add fonts to projucer file explorer to add them as a binary resource, then add to cmake with juce_add_binary_data(), then add a pointer to the typeface and set the font:

    const juce::Typeface::Ptr typeface = juce::Typeface::createSystemTypefaceFor(BinaryData::Monomaniac_ttf, BinaryData::Monomaniac_ttfSize);
    g.setFont(juce::Font(typeface).withHeight(11.0f));

---
## [yourenoticed/AoC](https://github.com/yourenoticed/AoC)@[e0c5467a0a...](https://github.com/yourenoticed/AoC/commit/e0c5467a0a7f28615f05372bd724f76eed025e21)
#### Monday 2023-12-04 18:16:21 by yourenoticed

finished day 3 task 2 holy fucking shit it was difficult

---
## [Writeyourhomeworkifthemoneyisenough/Phase-1-UDP-Implementation-using-RAW-Socket](https://github.com/Writeyourhomeworkifthemoneyisenough/Phase-1-UDP-Implementation-using-RAW-Socket)@[e2dca22289...](https://github.com/Writeyourhomeworkifthemoneyisenough/Phase-1-UDP-Implementation-using-RAW-Socket/commit/e2dca222891e195d632475a2371b304caa60da37)
#### Monday 2023-12-04 18:34:23 by Writeyourhomeworkifthemoneyisenough

Add files via upload

Introduction
The goal of this programming project is to familiarize you with the low-level operationsof the Internet protocol stack as well as reliable data transfer. So far, you have writtensimple client-server applications in which the server and client implemented some basicfunctionalities. You have worked with both UDP and TCP sockets. However, in all of theabove scenarios, the operating system's networking stack hides all the underlyingcomplexity of constructing and managing IP and TCP headers. Moreover, when writinga TCP socket programming application, you did not care how the reliability isimplemented for TCP (although you were familiar with the reliable data transfermechanisms such as sequence numbers, acknowledgement numbers, checksum, andretransmissions). This programming project has two phases as follows:
Phase 1: UDP Implementation using RAW Socket
Your task is to write a client program called rawUDPClient that takes a file name asinput. Then, the client program sends the filename to a UDP web server to request itsdownload. The web server program is called rawUDPServer. Your client and serverprograms must use SOCK RAW/IPPROTO RAW sockets, that is, you areresponsible for building the IP and UDP headers in each packet
Phase 2: Reliable DataTransfer for the UDPImplementation in Phase 1
You may have noticed that in Phase 1, we did not focus on the reliability of file transferAs you know, UDP does not provide reliable data transfer and you cannot guaranteethat the received file is the same as the sent file. This means that the file may havebeen modified in transit (e.g., some bits may be corrupted, some chunks may be lost,etc.). Therefore, the goal of this phase is to provide reliability for the protocol youimplemented in Phase 1. A text file of any size must be transferred with reliability.You need to implement the following error control mechanisms:
Checksum
Sequence Numbers
Acknowledgement numbers
Retransmission due to timeout
lmplementation and Test Requirements
You need to implement your programs using Python programming language.The file created by your program should be the same as the original file onthe web server. You can test whether your file and the original are identical bycomparing the file that your client program receives and the original oneusing md5sum.
You should run and test your programs in Mininet and emulate the packet lossand delay (as you will learn in class).
Additionally, please be aware that using raw sockets requires administrativeprivileges and comes with potential security risks, so use them with caution.This is due to the fact that the security model in OS is usually centered aroundhaving hardware and network controlled by the network administrators and thenhaving unprivileged users separate from these administrators on the network.
Allowing unprivileged users to use raw sockets would break these securityassumptions, since with raw sockets anything could be done in the network, likeusing privileged ports, spoofing IP addresses etc. For more information, pleaserefer to [1].
You can use online resources as a reference, but they must be referenced/citedin your Readme file. Do not just copy and paste code from these resources.You should not use ChapGPT to write the code for your project. However, youare allowed to use ChapGPT to debug the errors in your code and solve theissues if you could not solve them as a team after discussion. If you useChapGPT, you need to explain in your Readme the problems/issues that weresolved with it and how they were solved. Include the lessons you learned fromChatGPT as your new code review buddy.
Submission Requirements
1. No late submissions allowed
2. This is a group assignment. All code must be written by the group members only encourage you to discuss and share ideas with your classmates but rememberto write your own code!
One group member should submit the deliverables on Canvas on behalf of other3members.
Deliverables and Milestones:
1. Phase 1 should be completed by the week of Nov 6th. You will need to demoyour phase 1 to TA during office hours on Nov 8th. This includes running thecode, and showing the project logs, readme, and meeting notes.
2. Phase 2 should be completed by Dec 3rd.3. Final demo of the project in class (Dec 4th)
Demo involves presenting your application programs to the instructor, TA, andother students as well as answering questions about your project
Note: part of your grade will come from the peer evaluation.
4. Final submission on Canvas: (Dec 4th, 11:59 PM)
Project documentation (a zip file) that includes the following:Readme: Include a Readme file that describes how to run yourapplication, how your application works and if there are any errorsor use cases that have limitations or if it doesn't meet any of therequirements. This is also the spot where you want to documentany features that you may or may not have implemented. Moreover.it should summarize the design and key functionalities of yourapplication programs and any features that you have implemented.lessons learned，possible future improvements, etc. This will helpme keep an eye out for them as I grade your work.Meeting notes: You need to document your meetings(date/time/agenda/conclusions) and put them as a part of theproject documentation to ensure every team member hasparticipated. A minimum of two meetings (online/in-person) perweek is required among the group members to discuss the projectin addition to the time you may spend together working on the code,etc.
Your project management tool / project log book (such as Trello,Teamwork) to keep record of the tasks and your progress. Youmust include the weekly tasks assigned to members and whichfeature(s) has been developed by each member of your team.Alternatively, you can use a separate Google Doc for each of theabove.
All of the source files.
Concluding Thoughts
Remember to approach your code in an object-oriented fashion. Don't just startbashing out code and hoping that it will all work out. Take a planned approach.Moreover, it is a good idea to select a team lead for your group and they should be incharge of organizing and scheduling meetings between group members, making surethat your group is on track, and they can be the one communicating with me if there arequestions on behalf of your group.

---
## [Mirag1993/mrdg](https://github.com/Mirag1993/mrdg)@[0b9f48a711...](https://github.com/Mirag1993/mrdg/commit/0b9f48a711b64bafc08c4586c9ecb522ef6e0cc9)
#### Monday 2023-12-04 18:39:15 by lizardqueenlexi

Removes "fat" status and everything related. (#2516)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

As the title says, eating too much no longer makes you "fat". You suffer
no slowdown or mood debuff from eating too much, and in general, the
game will not take every opportunity to make fun of you.

Notable removals/changes:
- The "fat sucker" machine is totally gone.
- Shady Slim's cigarettes have been removed (since they only existed to
interact with this mechanic).
- Lipoplasty surgery is gone.
- The nutrition setting of scanner gates is gone.

There are a couple of other removals too, like Gluttony's Wall, that I
think were already not in use on this codebase.

One thing I'm not completely satisfied with was the change to mint
toxin, which now does quite literally nothing. I don't think this is
especially a problem, it just makes its existence a bit vestigial.

Also includes an UpdatePaths script to delete all removed objects, just
in case.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

![image](https://github.com/shiptest-ss13/Shiptest/assets/105025397/a1dd0981-94fc-4766-a34d-cce31a42b412)

Basically, removes some shitty "jokes" about fat people. It's an
extremely mean-spirited feature that serves no actual purpose, and
punishes you for clicking on a burger one time too many. It could
potentially be replaced later with a less mean-spirited "overeating"
mechanic, but I'm dubious as to whether that would be any fun either.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl:
del: Removed the "fat" status - overeating now has no negative effects.
del: Removed lipoplasty surgery.
del: Removed the fat sucker machine.
tweak: Scanner gates no longer have a "nutrition" option available.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[39d9c45b4a...](https://github.com/psychonaut-station/PsychonautStation/commit/39d9c45b4a7afc2a963de4249592a3d4ae6c4715)
#### Monday 2023-12-04 18:48:58 by san7890

Meat Hook Rework (Accidental Features) (#80002)

## About The Pull Request

Or, how I tried to kill `/datum/forced_movement` but got absolutely
clonged.

Actually, I did kill `/datum/forced_movement`. It was only used in one
spot so I just went ahead and cooked it into a special utility datum
that should only be used in one spot. We can optimize the code later or
something, but I like the way it is right now (pretty much status quo
without the potential of someone using a depreciated framework).

Alright, there were also like 3 `TODO`s (4 if you count the move loop
comment (which is ehhhh)). I naively tried to tackle them a very hard
way, but then I just realized I could use the fancy new datum I cooked
up and wow they're all solved now. The hook looks so fucking good now.

* The code is overall more streamlined, with all of the post-projectile
work being handled by a special datum (I wanted it to be handled by the
hook but the timings were all based on SSFastprocess so datum it is).
Forced movement is killed but we just salvaged whatever we needed from
it.
* More traits to ensure we don't cheese in a way we're not supposed to
* A very sexy chain will spawn when you drag your kill in (this wasn't
there before but I fixeded it :3)
* The firer will actually get grounded when they try and shoot the chain
out. They get grounded for 0.25 seconds unless they hit something. I
don't know how the timing is but I think it's fair.
* We also add a unique suicide act, because I noticed we did the
"magical" one previously, which big-league sucked.
* More traits to ensure less cheese! I like how nice it is now.
## Why It's Good For The Game

The meat hook really makes you _feel_ like Roadhog from Overwatch.
Resolves a bunch of old TODOs while getting rid of a completely obsolete
framework in a really neat way. I don't typically like mixing balances
and refactors but these TODOs were getting crusty man i just wanted to
get them out of the way
## Changelog
:cl:
balance: The Meat Hook will now "ground" you whenever you fire it out at
someone. You get a very small immobilization every time you fire, which
"upgrades" to a full immobilization whenever you actually hit an atom
and start to drag it in.
fix: A chain should now show up as you drag in something with the meat
hooks.
fix: Meat hooks should no longer play the "magical gun" suicide if you
were to use it, but instead do their own unique thing.
/:cl:

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[08ab5d2731...](https://github.com/psychonaut-station/PsychonautStation/commit/08ab5d27312d236593eabdb27fb23dccbf8283e6)
#### Monday 2023-12-04 18:48:58 by Mothblocks

Blood brothers is now a single person conversion antagonist (#79971)

## About The Pull Request
Instead of choosing 2-3 brothers, *one* person will be selected and
given a flash which can convert one other person over. In accordance to
the existing 10% chance for 3 members, there is a 10% chance that the
first person converted will receive a flash of their own.

Expectation is people will flash a friend or a robust guy or whatever.
My intent is primarily to see if this kind of blood brothers is more
enjoyable to play with/against, and if their inclusion in a round
increases the general chaos of it. My theory is that since most likely
blood brothers will be people who know each other, that it can become
more consistently interesting to the rest of the crew. That or they just
murderbone together idk

Fikou and head admins said they wanted this to replace rather than add
which I agree with.

## Why It's Good For The Game
Keeps the sandboxy aspect of blood brothers (no uplink) while likely
making it more enjoyable to play. Conversion is equally as simple as
revs for the user, and is just as intuitive to the one being converted
since there are no new mechanics thrown in your face.

Blood brothers is currently disabled everywhere on the main servers
except for MRP. I think this form will be more appealing to all
rulesets. If left enabled, Dynamic now has more antagonists to make
rounds diverse with and I want that

## Changelog

:cl:
add: Instead of teaming up random people together, blood brothers will
now start out with one player and let them convert a single other person
over to blood brother using a flash.
/:cl:

---
## [Mirag1993/mrdg](https://github.com/Mirag1993/mrdg)@[936fad79b2...](https://github.com/Mirag1993/mrdg/commit/936fad79b2b4f27befd8f0910b7a38536df5a6c7)
#### Monday 2023-12-04 18:55:57 by GenericDM

Assorted cringe removal pt.whatever (#2534)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

Removes more cringe I found laying around.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

/tg/ was on some WILD shit.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl:
del: removes tail club
del: removes all flavors of tail whip
del: removes lizardskin clothing
del: removes 'Genetic Purifier'
tweak: makes bunny ears desc not incredibly sexist
tweak: change up wording in magic mirror gender change
del: removes 'genuine' cat ears
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [reosarevok/musicbrainz-server](https://github.com/reosarevok/musicbrainz-server)@[41b5efc95c...](https://github.com/reosarevok/musicbrainz-server/commit/41b5efc95c13ee269e436a9864744de6d81bf7ca)
#### Monday 2023-12-04 19:13:58 by Michael Wiencek

MBS-13310: Add new empty artist credits to unreferenced_row_log (#3105)

When artists are merged, `Data::ArtistCredit::merge_artists` is called, which
inserts new artist credits: each appearance of the old artist is replaced by
the new one.  If the old AC had no references, it will have had an entry in the
`unreferenced_row_log` table already; we should make sure to update that to
point to the new AC, if the new one also has no references.

Remember that because artist credits have MBIDs, we'd like to preserve them
from deletion where possible: there's a 2-day delay before we cleanup empty
ACs, allowing time for them to be re-used with their original MBIDs intact.
This applies to redirected MBIDs too; so while inserting empty artist credits
may seem silly, these empty ACs are in fact redirected to from a (now-deleted)
empty AC which hadn't been cleaned up yet.

---
## [Mirag1993/mrdg](https://github.com/Mirag1993/mrdg)@[b58b3abe4f...](https://github.com/Mirag1993/mrdg/commit/b58b3abe4ffd26c63adb349f873ededfda5781a6)
#### Monday 2023-12-04 19:33:32 by zevo

Massive Ruin Fixes + Removals PR (#2334)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

This PR is made so I can stop getting angry at the ruins beyond saving
that are still ingame. My criteria for a ruin being removed is if
another ruin already does its niche better, if the ruin is outdated
and/or the ruin is excessively small or unbalanced. For ruins that dont
meet this criteria but are still outdated, they will be getting balance
fixes and touch ups or a total remap.

This PR is a draft for now because I will need to update the PR
changelog and description as I make changes and communicate with the
maptainers on what stays and what goes.

Adds departmental RND lootdrop spawners for circuit imprinters,
protolathes and techfabs. Excludes omnisci and basic boards from the
drops.
Fixed a space tile under a door and replaced the omnilathe with a
medical lathe on dangerousresearch
Fixed the whitesands saloon not spawning which may have caused some
sandplanets to spawn without a ruin
Fixed harmfactory's nonfunctional traps to now be as lethal as intended.
Also changed the loot in the vault to better reflect the ruin's theme
and difficulty (cargo techfab board instead of omnilathe, adv plasma
cutter instead of combat medkit, less gold more cash, kept the cyberarm
implant).
Fixed provinggrounds magical SMES FINALLY by adding a terminal on the
back. The map should finally function as intended.
Fixed a few dirs on fire extinguisher cabinets and blast door assemblies
in singularity_lab
Removed mechtransport.dmm for being small and bad
Removed some leftover gasthelizards.dmm cruft (VILE)
Removed nucleardump for being an utter mess of an oldcode ruin
Removed gondolaasteroid for being large and empty besides gondolas.
better suited for a jungle planet IMO.
Removed Jungle_Spider. Literally just a box with spiders and cloning
equipment. Small, bad, hard to find, unjustified loot.
Removed Golem_Hijack. Like jungle spider but it was free rnd, an AI
core, a full BSRPED and three golem corpses. With no enemies or
obstacles.
Removed rockplanet_clock for being a tiny lootbox that doesnt fit with
the lore. Also had a quantumn pad.
Removed whitesands_surface_youreinsane. Its a silly little reference to
an old event that unfortunately resulted in a subpar ruin. Could return
as a wasteplanet greeble ruin, but it has to go for now.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

Normally I'm all for remapping instead of removing ruins, but some ruins
are very much beyond saving. Clearing out space for better ruins to take
the spotlight is always nice. Some older ruins are fine but are missing
certain things or have loot that worked fine in the past, but doesn't
reflect the balance we want for ruins in the present.

I will be PR'ing ruins to replace the ones I remove.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl:
add: departmental RND lootdrop spawners for imprinters, protolathes and
techfabs
fix: dangerous_research.dmm now no longer has a space tile under a door
and a medical lathe instead of an omnilathe
fix: whitesands_surface_camp_saloon can now spawn again after its remap
into a functional ruin
fix: harmfactory.dmm's traps now work and loot has been adjusted to fit
the ruin better
fix: provinggrounds.dmm now has a working SMES and power
fix: singularity_lab fire extinguishers and a few poddoors now have
correct dirs
del: mechtransport.dmm and associated code
del: gasthelizards areas
del: nucleardump.dmm and associated code
del: gondolaasteroid.dmm and associated code
del: jungle_spider.dmm and associated code
del: whitesands_golem_hijack.dmm and associated code
del: rockplanet_clock.dmm and associated code
del: whitesands_surface_youreinsane.dmm and associated code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: zevo <95449138+Zevotech@users.noreply.github.com>

---
## [nevimer/Bubberstation](https://github.com/nevimer/Bubberstation)@[c056f4dac9...](https://github.com/nevimer/Bubberstation/commit/c056f4dac9e4649a960be5d6331b110c89f3080e)
#### Monday 2023-12-04 19:37:00 by SkyratBot

[MIRROR] Nanotrasen basic mobs. [MDB IGNORE] (#24573)

* Nanotrasen basic mobs. (#78917)

## About The Pull Request

First and foremost, converts all Nanotrasen simplemobs into basic mobs.

To avoid messy and redundant code, or god forbid, making Nanotrasen mobs
a subtype of Syndicate ones, I've made Syndicate, Russian, and
Nanotrasen mobs all share a unified "Trooper" parent. This should have
no effect on their behaviors, but makes things much easier to extend
further in the future.

While most of this PR is pretty cut-and-dry, I've done a couple notable
things. For one, all types of ranged trooper will now avoid friendly
fire, instead of shooting their friends in the back. Even the Russians
have trigger discipline.

I've also created a new AI subtree that allows mobs to call for
reinforcements. I've hopefully made this easy to extend, but the
existing version works as follows:

- A mob with this subtree that gains a target that is also a mob will
call out to all mobs within 15 tiles.
- If they share a faction, mobs receiving the call will have the target
added to their retaliate list, and have a new key set targeting the
calling mob.
- If they have the correct subtree in their AI controller, called-to
mobs will then run over to help out.

Sadly, this behavior is currently used only by a few completely unused
Nanotrasen mobs, so in practice it will not yet be seen.

Finally, I've fixed a minor issue where melee Russian mobs punch people
to death despite holding a knife. They now use the proper effects for
stabbing instead of punching.
## Why It's Good For The Game

Removes 8 more simple animals from the list.

As said above, making all "trooper" type mobs share a common parent cuts
down on code reuse, ensures consistency of behavior, and makes it much
easier to add new troopers not affiliated with these groups. I expect
that I'll make pirates share this same parent next.

The new "reinforcements" behavior, though extremely powerful, opens up
exciting new opportunities in the future. There aren't many existing
behaviors that allow basic mobs to work _together_ in interesting ways,
and I think adding some enemy teamwork could be fun.
## Changelog
:cl:
refactor: Hostile Nanotrasen mobs now use the basic mob framework. This
should make them a little smarter and more dangerous. Please report any
bugs.
fix: Russian mobs will now actually use those knives they're holding.
/:cl:

* Nanotrasen basic mobs.

* Modular

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [jcalvinowens/netconsd](https://github.com/jcalvinowens/netconsd)@[558c8b22c3...](https://github.com/jcalvinowens/netconsd/commit/558c8b22c3130739dc422989f5ca656444653659)
#### Monday 2023-12-04 19:42:02 by Calvin Owens

[DRAFT] Use a global RCU hashtable with per-client message queues

Netconsd turns eight soon! It deserves some love.

A longstanding problem is the behavior of the daemon in the face of
extremely noisy remote hosts, in particular:

	1) Queues are often mostly full of low value messages from a
	   very small number of machines, delaying processing of the
	   messages which are actually useful.

	2) Messages are not associated with a host until they are
	   dequeued in the worker, so there is no simple way to add a
	   feedback mechanism to drop messages before enqueueing them.

	3) Ye Olde Probing Hashtable performs very poorly: if a noisy
	   host happens to hash to a spot with a long string of
	   collisions, hlookup() can waste a lot of CPU time.

	4) Messages are submitted to ncrx one-at-a-time.

This patch pulls the hashtable lookup into the listener threads, and
creates a message queue for each remote host in its bucket*. This allows
workers to set a flag in the bucket which causes the listener to drop
all messages from the host without enqueueing them.

It also allows the workers to substantially reduce the tail latency by
only draining a limited number messages from each host before moving on
to the next in a round-robin fashion. It wasn't an overt goal, but
processing the messages in larger batches is also probably more
efficient.

RCU lets us have our cake and eat it too: with rculfhash and QSBR, there
is incredibly little overhead to this shared hashtable. Also, with a
little trickery, garbage collection can now run without delaying the
processing of messages.

Rather than adding an "active list" in the worker, I've tried to reuse
the existing timer callback machine. It's a little ugly, but it works.
The current feedback logic is very crude: it's just an example. I think
it should actually be based on frequency, so its more deterministic.

I don't know how I feel about the state machine... I like it because it
makes the ownership explicit in a way refcounting wouldn't, but I think
it can be simplified more. The obvious ABA problems are solved using
synchronize_rcu() in the worker and GC threads, there may be pitfalls to
this approach I haven't found yet.

* The 'bucket' phrasing is leftover from the probing implementation: in
  reality, rculfhash is a chaining hashtable, so its buckets are hlist
  nodes not records... I'm lazy and don't think it matters, but if
  anybody disagrees I'll change it.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[cae221c732...](https://github.com/treckstar/yolo-octo-hipster/commit/cae221c73229cbd26d1b9b6ec5a21703fcef6c4d)
#### Monday 2023-12-04 20:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[abab8705fe...](https://github.com/microsoft/terminal/commit/abab8705fea32854a6b55153b5736f9fd9dacb66)
#### Monday 2023-12-04 20:25:23 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

(cherry picked from commit 86fb9b44787accd09c5943a506e27eb4c8e573c0)
Service-Card-Id: 91098597
Service-Version: 1.19

---
## [kotmatross28729/BugTorch](https://github.com/kotmatross28729/BugTorch)@[544f58233e...](https://github.com/kotmatross28729/BugTorch/commit/544f58233e0e5ca32208ae488d1fe96025cde8a3)
#### Monday 2023-12-04 20:48:40 by kotmatross28729

port cool thing from BetterWithPatches

This thing allows you to specify items in the config that, if placed on the top table of the furnace, will fucking explode it.
Originally from BetterWithPatches, but who cares about this useless fork?
Yes, I love putting trinitrotoluene from minechem into the lit furnace in the morning

---
## [Aurorastation/Aurora.3](https://github.com/Aurorastation/Aurora.3)@[13eb8af093...](https://github.com/Aurorastation/Aurora.3/commit/13eb8af093447e13b6555a741d6cd9e3a9dc3fbc)
#### Monday 2023-12-04 21:13:30 by RustingWithYou

air konyang ship (#17540)

it's a shuttle now, im gonna kms

smaller so it can fit

desperately cramming into shuttle guidelines

changelog & placeholder comments

chairs

name & mapping fixes

dme fix

carpet

new airlocks

entry points?

cries, shits

a

unit test group

fuck

ghuh

hguh

hate

fixes stupid problems

area flags

---
## [Yurai-Iszakto/lobotomy-corp13](https://github.com/Yurai-Iszakto/lobotomy-corp13)@[e23ea7b596...](https://github.com/Yurai-Iszakto/lobotomy-corp13/commit/e23ea7b5965a446e5b34f30baa0d4e4dc2d5b868)
#### Monday 2023-12-04 21:52:15 by Táculo

Updates La Luna, Pinnochio for Rcorp and playables, gives minions NV on Rcorp AND moves CheckCombat to simple_animal. (#1621)

* Adds Everything

adds nv combat checks to
nosferatu bats
ml slimes
censored minis
tbird spawns
la luna spawned mob

adds mind transfer to pinocchio and la luna
add check for combat to initialize ai controllers for pinocchio, gives him a seclite on rcorp
add check for combat to spawn the breached la luna mob on its position instead of in a random department and to disable the timer.

makes pino ai disabled while a client is possesing it.

* removes one line

* Changes CheckCombat location, applies it to all minions.

* Makes button refuse pino.

fuck you pinocchio

* moves blocking code to pinocchio's

* moves the nightvision checks to simple_animal

moves the nightvision checks to simple_animal

removes the checks from censored, luna, tbird, ml, nosferatu

---
## [Yurai-Iszakto/lobotomy-corp13](https://github.com/Yurai-Iszakto/lobotomy-corp13)@[294f764ad0...](https://github.com/Yurai-Iszakto/lobotomy-corp13/commit/294f764ad01a99c63b46dfea3dac7e5cfe14cd7d)
#### Monday 2023-12-04 21:52:15 by Coxswain

Adds distorted form (#1435)

adds some basic features

new 1% sprite dropped

text update

Finished work mechanics

adds basic breaching

should fix linters a bit

It works!!!! Kinda...

adds crumbling armor and hammer of light (beta)

adds cool and important stuff

does a thing

adds apostle and tutorial abnorms

adds the stuff

might fix linters

adds a console proc

adds crumbling armor's proper attack and red queen

does some things

should fix linters

adds a blubbering toad transformation

adds more attacks

brings the tier up

adds big boy attacks

updates some sfx, fixes bugs

adds jump attacks

why does linters care about indentation on comments?

adds suggested changes

should fix some stuff

adds info

adjusts damage numbers

updates an effects and fixes transformations

updates blacklist

lowers stack damage

lowers max qlip to 3

adds bloodbath

adds a new AOE attack

adds halberd apostle

blacklists DF from pink midnight

fixes weirdness

requested changes and sound design improvement

removes armortype

removes armortype for real

damage coeff update

makes suggested changes

updates comments

adds procs

adds stuff

---
## [Litberries/lobotomy-corp13](https://github.com/Litberries/lobotomy-corp13)@[2defb31817...](https://github.com/Litberries/lobotomy-corp13/commit/2defb31817005f7790e9586ace0c4e77c23d7f06)
#### Monday 2023-12-04 21:56:38 by vampirebat74

Adds Red Shoes (#901)

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

wayward records

Update code/modules/paperwork/records/info/he.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

Update code/modules/mob/living/simple_animal/abnormality/he/red_shoes.dm

Co-authored-by: [̸R̵e̵d̴a̴c̶t̸e̸d̴]̵ <61567407+LanceSmites328@users.noreply.github.com>

attribute bonus

requested changes

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[274eb2a52e...](https://github.com/tgstation/tgstation/commit/274eb2a52ecd35f86d1cd83032c655997dc73106)
#### Monday 2023-12-04 22:42:46 by distributivgesetz

Removes Clone Damage (#80109)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Does what it says on the tin. We don't have any "special" sources of
clone damage left in the game, most of them are rather trivial so I
bunched them together into this PR.

Notable things removed:
- Clonexadone, because its entire thing was centered around clone damage
- Decloner gun, it's also centered around cloning damage, I couldn't
think of a replacement mechanic and nobody uses it anyways
- Everything else already dealt clone damage as a side (rainbow knife
deals a random damage type for example), so these sources were removed

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Consider the four sources of normal damage that you can get: Brute,
Burn, Toxins and Oxygen. These four horsemen of the apocalypse are very
well put together and it's no surprise that they are in the game, as you
can fit any way of damaging a mob into them. Getting beaten to death by
a security officer? Brute damage. Running around on fire? Burn damage.
Poisoned or irradiated? Toxin damage. Suffocating in space? Brute, burn
and oxygen damage. Technically there's also stamina damage but that's
its own ballpark and it also makes sense why we have a damage number for
it.

Picture this now: We have this cool mechanic called "clone pods" where
you can magically revive dead people with absolute ease. We don't want
it to be for free though, it comes at a cost. This cost is clone damage,
and it serves to restrain people from abusing cloning.

Fast forward time a bit and cloning is now removed from the game. What
stays with us is a damage number that is intrinsically tied to the
context of a removed feature. It was a good idea that we had it for that
feature at the time, but now it just sits there. It's the odd one out
from all the other damage types. You can easily explain why your blade
dealt brute damage, but how are you going to fit clone damage into any
context without also becoming extremely specific?

My point is: **clone damage is conceptually a flawed mechanic because it
is too specific**. That is the major issue why no one uses it, and why
that makes it unworthy of being a damage stat.
Don't take my word for it though, because a while ago we only had a
handful of sources for this damage type in the game. And in most of the
rounds where you saw this damage, it came from only one department. It's
not worthwhile to keep it around as a damage number. People also didn't
know what to do with this damage type, so we currently have two ways of
healing clone damage: Cryotubes as a roundstart way of healing clone
damage and Rezadone, which instantly sets your clone damage to 0 on the
first tick. As a medical doctor, when was the last time you saw someone
come in with clone damage and thought to yourself, "Oh, this person has
clone damage, I cannot wait to heal them!" ?

Now we have replacements for these clone damage sources. Slimes? Slime
status effect that deals brute instead of clone. Cosmic heretics? Random
organ damage, because their mechanics are already pretty fleshed out.
Decloning virus? The virus operated as a "ticking timebomb" which used
cloning damage as the timer, so it has been reworked to not use clone
damage. What remains after all this is now a basically unused damage
type. Every specific situation that used clone damage is now relying on
another damage type. Now it's time to put clone damage to rest once and
for all.

Sure, you can technically add some form of cellular degradation in the
future, but it shouldn't be a damage number. The idea of your cells
being degraded is a cool concept, don't get me wrong, but make it a
status effect or maybe even a wound for that matter.

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

:cl:
del: Removed clone damage.
del: Removed the decloner gun.
del: Removed clonexadone.
/🆑

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [KGB33/dagger](https://github.com/KGB33/dagger)@[80180aaaed...](https://github.com/KGB33/dagger/commit/80180aaaed1e1e91a13dbf7df7e0411a9a54c7d3)
#### Monday 2023-12-04 22:45:40 by Justin Chadwell

Fix secret scrubbing log latency (#6034)

* fix: use custom implementation for secret scrubbing

This was a fun exercise in processing streams in go, and an absolutely
massive nerd-snipe :(

Essentially, we need a custom transformer to handle *precisely* matching
Reads on the underlying source with the output - we shouldn't hold
output any longer than is absolutely neccessary.

To be able to do this at all in any reasonable way, we need a trie, and
handle *all* the secrets at once, instead of doing multiple passes.
Multiple passes won't work, since it's possible to accidentally trim too
much at each step, which would be very sad.

> e.g. imagine secrets (aaa, bbb, ccc, etc), and an input (cba)
>
> In removing secret aaa, we would trim to cb, then we'd remove bbb to
> trim to c, then finally trim to nothing. However, this is overly
> enthusiastic, we could easily just trim to cb, if we knew about all
> the secrets at once.

So, we need a trie, and we need a custom implementation of one. This is
because *no off the shelf implementation* seems to allow traversing the
trie state-by-state. Thankfully, it's a pretty short implementation to
implement one from scratch, and not too much harder to turn it into a
radix tree (which lets us use quite a lot less memory).

With our trie, we can implement our custom transformer, which is *an
utter pain*. Honestly, the comments should explain all the fun edge
cases it's possible to hit. There's a lot of tests added as well, each
of which was a real horrible thing I hit while implementing it.

I played around a bit with benchmarking, but ugh, it's a *tiny* bit
slower than the original implementation (maybe by like ~25%?). It's not
huge, but the latency problem is *actually solved*. Some potential
things I did look into and gave up on:
- Only copy into dstBuf when dst is full (requires tons of extra
conditionals, so slows everything down).
- Avoid copies at all costs by having "virtual buffer pointers" into
src, that indicate future data to copy (not only is this *slower*, the
logic becomes truly incomprehensible).
- Playing with off-the-shelf radix tree implementations, but they're so
inconvenient to use for this specific use case, it'd be way more
trouble than it'd be worth.

Any ideas welcome, but honestly, I've looked at enough flamegraphs
today.

Signed-off-by: Justin Chadwell <me@jedevc.com>

* test: avoid use of require.Eventually for secret scrubbing

Signed-off-by: Justin Chadwell <me@jedevc.com>

---------

Signed-off-by: Justin Chadwell <me@jedevc.com>

---
## [nrc-cnrc/gramble](https://github.com/nrc-cnrc/gramble)@[48d9b1d1cc...](https://github.com/nrc-cnrc/gramble/commit/48d9b1d1cc5678d7c5719a513abd41eff9c14d15)
#### Monday 2023-12-04 23:14:30 by littell

Letting Envs vary by the pass

There's an abstraction about components, passes, and envs that we weren't capturing, and in fact were doing something kind of silly.

This was making it tedious to adapt CalculateTapes in the way that solves the last commit's issues, so I figured it was high time to fix this.

(0) Before doing this I switched back to using top-level vocabs in generation, to return us to (mostly) green, so I could refactor in safety.

(1) Out of suspicion, I deleted `CollectionGrammar.mapChildren` (which is responsible for putting its symbols into env.symbolNS), which should have caused major failures left and right.  That's part of WHY mapChildren is a member, so that CollectionGrammar can put those there, because that's really important, right?  That's part of why we have a symbolNS in PassEnv, right?

Turns out, no.  Nothing failed because we never BOTH used mapChildren AND used those symbols from it.  All the remaining functions that use `env.symbolNS` that way aren't component-to-component Passes, so they can't use mapChildren anyway.  They were changing env.symbolNS and then recursing manually.

Meanwhile, there are places where we're manually changing parts of the environment before recursion, but not using Env, because Env is quite limited in what it can do.  If we need to do anything in a Pass that isn't push symbols onto the symbolNS, we can't use the boilerplate and thus have to manually recurse -- and as mentioned, pushing symbols isn't even something we need during the main passes.

So really, Env wasn't doing much.  It was really just a place to store Options.

(2) Stepping back, what we need Env to do is to assist in the tedious management of certain kinds of information during a recursion strategy: stuff that mostly stays intact through the traversal but occasionally changes.  Symbols, tape references, etc.

The reason Env wasn't very good at this is that different passes have different environmental needs -- they need different information, and change it in different ways.  But the way we create and compose them made it difficult for them to vary.  We start with a PassEnv at the very beginning and then thread it through ~20 passes.

(3) Do passes ever need to share an Env?

Sometimes!  ExecuteTests is a good example of this.  Now that staging is handled by Passes, and ExecuteTests does its own staging, that means ExecuteTests now has 4 or 5 "child" passes.  Those child passes are executed on nodes that aren't themselves roots, so they won't necessarily go through a CollectionGrammar to get something into a symbol table.  Therefore yes, they need to use their parent's env, which DID go through a CollectionGrammar.

On the other hand, we never have two "sibling" passes -- ones that happen one after another -- that need to share information.  We've been cautious to avoid that, we try to share that kind of information only by adding something to the tree.

So `Pass.compose` doesn't have to thread an env through both of its children.  NOT threading the env like this takes away the need for them to all be the same type.

(4) While Env-changing takes various forms, it's typically done in the same place -- immediately before recursing.  (I mean, if we changed it *after* recursing nothing would happen.  It's not like we return them, if we made a new env it would just be garbage collected when we leave the scope.)

So now there's a method `Env.update(g)`, basically meaning "Change the env in whatever way necessary using information from g".  By default it doesn't change anything; if you need to change something, inherit from Env and override this method.

For example, `SymbolEnv.update(g)` looks at g, and if it's a CollectionGrammar, it pushes those symbols into the `SymbolEnv.symbolNS` and returns the new env.  Otherwise it returns the original env.  This will be called automatically by mapChildren -- achieving what `CollectionGrammar.mapChildren` used to do, but now only when necessary, and when something else is necessary, `WhateverEnv.update(g)` can do that instead.

(5) Passes now have a method `.getEnv(opt)` that'll provide an empty instance of whatever kind of Env that pass needs, and the requests opts.

(6) On Friday-ish I got rid of `Pass.go()` for being both useless and poorly-named.  But we now need a top-level method in the same place.  We don't want to use `.transform(g, env)` everywhere because that's passing in an env, and except in special circumstances we AREN'T passing in envs, we're getting new ones with `.getEnv(opt)`.

So now there's a method `.getEnvAndTransform(g, opt)` that does what it says on the tin.  This is the method that CombinedPass calls instead of calling transform, and the main one we'll want to be calling elsewhere.

(7) I think we can simplify all this more in the future, but anything more than this is premature refactoring, we have to make sure this does what CalculateTapes is going to need, first.

---
## [NilaPrabhu/NeoCare](https://github.com/NilaPrabhu/NeoCare)@[1baa5af720...](https://github.com/NilaPrabhu/NeoCare/commit/1baa5af720d4b4794f03f41a681fe246188de956)
#### Monday 2023-12-04 23:51:03 by NilaPrabhu

Prader-Willi syndrome

A disease closely linked to "Weight for Age" is the Prader-Willi syndrome. It is a multisystem disorder characterized by neonatal hypotonia with poor weight gain without nutritional support, developmental delay, cognitive impairment, hypogonadism leading to genital hypoplasia and pubertal insufficiency, and a shot stature (if left untreated.)

There are many symptoms present through infancy, such as a weak cry, poor feeding ability, weak muscle tone, and/or lethargy. As a subject with Prader-Willi syndrome ages, they may have almond-shaped eyes, a triangular mouth, a long, narrow head, short height, small hands and feet, and possibly underdeveloped genitals. 

Behavioral symptoms include emotional outbursts, stubbornness, developmental issues, obsessive-compulsive behaviors, and sleep abnormalities. 

The Prader-Willi syndrome often ends in obesity for victims of the disease.

---

