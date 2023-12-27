## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-26](docs/good-messages/2023/2023-12-26.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,453,059 were push events containing 3,312,060 commit messages that amount to 189,898,015 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 55 messages:


## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[db0ea89db2...](https://github.com/vdaular-dev/linksfordevs/commit/db0ea89db227319f52917e624cf58a7cad28deb1)
#### Tuesday 2023-12-26 00:35:19 by Ben Dornis

Updating: 12/25/2023 10:00:00 PM

 1. Added: It's pretty cool to find out what stuff others use, and why people love lists of tech
    (https://andreisurugiu.com/blog/new-tech/)
 2. Added: Markdown Tables Suck
    (https://jankremer.eu/micro/markdown-tables/)
 3. Added: Available for beta testing: Zotero for Android
    (https://forums.zotero.org/discussion/110371/available-for-beta-testing-zotero-for-android)
 4. Added: std::print in C++23
    (https://vitaut.net/posts/2023/print-in-cpp23/)
 5. Added: Sending free transactional emails with Cloudflare Workers
    (https://dhravya.dev/posts/sending-free-transactional-emails-cloudflare)
 6. Added: The future vision of Ruby Parser
    (https://rubykaigi.org/2023/presentations/spikeolaf.html)
 7. Added: A Christmas Story
    (https://danielbmarkham.com/a-christmas-story/)
 8. Added: Fixing my Yamaha Electone ME-50: An FM Synthesizer Home Organ from 1986
    (https://nicole.express/2023/resisting-the-urge-to-make-organ-jokes.html)
 9. Added: The joys of holiday coding
    (https://www.mostlypython.com/p/the-joys-of-holiday-coding)
10. Added: I love my Ioniq, but I would never buy another Hyundai | Digital Trends
    (https://www.digitaltrends.com/cars/hyundai-ioniq-warranty/)
11. Added: Constellations are Younger than Continents — LessWrong
    (https://www.lesswrong.com/posts/YMakfmwZsoLdXAZhb/constellations-are-younger-than-continents)

Generation took: 00:09:37.8444764
 Maintenance update - cleaning up homepage and feed

---
## [sailfishos-mirror/systemd](https://github.com/sailfishos-mirror/systemd)@[c988ef4cf4...](https://github.com/sailfishos-mirror/systemd/commit/c988ef4cf435ffa50dc9d10d9b0e55d5685ac7b1)
#### Tuesday 2023-12-26 00:39:00 by Frantisek Sumsal

coccinelle: rework how we run the Coccinelle transformations

Turns out that the original way we did things was quite broken, as it
skipped a _lot_ of code. This was because we just threw everything into
one pile and tried to spatch it, but this made Coccinelle sad, like when
man page examples redefined some of our macros, causing typedef
conflicts.

For example, with a minimal reproducer that defines a cleanup macro in
two source files, Coccinelle has no issues when spatch-ing each one
separately:

$ spatch --verbose-parsing --sp-file zz-drop-braces.cocci main.c
init_defs_builtins: /usr/lib64/coccinelle/standard.h
HANDLING: main.c
SPECIAL NAMES: adding _cleanup_ as a attribute with arguments
SPECIAL NAMES: adding _cleanup_free_ as a attribute

$ spatch --verbose-parsing --sp-file zz-drop-braces.cocci
logcontrol-example.c
init_defs_builtins: /usr/lib64/coccinelle/standard.h
HANDLING: logcontrol-example.c
SPECIAL NAMES: adding _cleanup_ as a attribute with arguments

But when you try to spatch both of them at once, Coccinelle starts
complaining and skipping the "bad" code:

$ spatch --verbose-parsing --sp-file zz-drop-braces.cocci main.c logcontrol-example.c
init_defs_builtins: /usr/lib64/coccinelle/standard.h
HANDLING: main.c logcontrol-example.c
SPECIAL NAMES: adding _cleanup_ as a attribute with arguments
SPECIAL NAMES: adding _cleanup_free_ as a attribute
remapping: _cleanup_ to an ident in macro name
ERROR-RECOV: found sync end of #define, line 44
parsing pass2: try again
ERROR-RECOV: found sync end of #define, line 44
parse error
 = File "logcontrol-example.c", line 44, column 21, charpos = 1719
  around = '__attribute__',
  whole content = #define _cleanup_(f) __attribute__((cleanup(f)))
badcount: 2
bad: #include <systemd/sd-journal.h>
bad:
BAD:!!!!! #define _cleanup_(f) __attribute__((cleanup(f)))

This was, unfortunately, hidden as it is visible only with
--verbose-parsing (or --parse-error-msg).

Another issue was how we handled includes. The original way of throwing
them into the pile of source files doesn't really work, leading up to
similar issues as above. The better way is to let Coccinelle properly
resolve all includes by telling it where to find our own include files
(basically the same thing we already do during compilation).

After fixing all this, Coccinelle now has a chance to process much more
of our code (there are still some issues in more complex macros, but
that requires further investigation). However, there's a huge downside
from all of this - doing a _proper_ code analysis is surprisingly time
and resource heavy; meaning that processing just one Coccinelle rule now
takes 15 - 30 minutes.

To make this slightly less painful, Coccinelle supports caching the
generated ASTs, which actually helps a lot - it gets the runtime of one
rule from 15 - 30 minutes down to ~1 minute. It, of course, has its own
downside - the cache is _really_ big (ATTOW the cache takes ~15 GiB).

However, even with the aggressive AST caching you're still looking at
~1 hour for one full Coccinelle run, which is a bit annoying, but I
guess that's the price of doing things _properly_ (but I'll definitely
look into ways of further optimizing this).

---
## [jjpark-kb/Skyrat-tg](https://github.com/jjpark-kb/Skyrat-tg)@[b072ecd91f...](https://github.com/jjpark-kb/Skyrat-tg/commit/b072ecd91ff78f8c0f190e0bf647f34f46a855a0)
#### Tuesday 2023-12-26 00:42:39 by SkyratBot

[MIRROR] Deviant Crew antag panel category, Obsessed crew now shown in orbit menu, Paradox Clone orbit tab is now white [MDB IGNORE] (#25803)

* Deviant Crew antag panel category, Obsessed crew now shown in orbit menu, Paradox Clone orbit tab is now white (#80450)

## About The Pull Request

This rounds up the "Other" (Brainwashed, Hypnotised, Wizard Revenge, and
Obsession) antagonist category into the new "Deviant Crew" category.
This tab is white!

Obsessed crew are now displayed in the orbit panel (no other antagonists
in this group are though).

The Spacetime Aberrations (Paradox Clone) group has also been changed to
be white.

Here's how that looks:

![image](https://github.com/tgstation/tgstation/assets/28870487/415b8cbb-7ac3-4e24-9f74-466480c2aab0)
## Why It's Good For The Game

As was the case with paradox clones, observers can already discern when
a player is obsessed. It shouldn't be a pain to observe these guys,
especially when they're a more RP oriented antag that are (usually)
deserving of the audience.

I made paradox clones and obsessed the same color because they're both
in the broader spectrum of "fucked up crew".

Also converts common text entries to a single define. That is good
coding practice I think.
## Changelog
:cl: Rhials
qol: Obsessed crewmembers are now displayed in the orbit panel.
qol: The Paradox Clone orbit menu tab is now white. Neat!
/:cl:

* Deviant Crew antag panel category, Obsessed crew now shown in orbit menu, Paradox Clone orbit tab is now white

---------

Co-authored-by: Rhials <28870487+Rhials@users.noreply.github.com>

---
## [SpaceLoveSs13/Skyrat-tg](https://github.com/SpaceLoveSs13/Skyrat-tg)@[800ad77ed2...](https://github.com/SpaceLoveSs13/Skyrat-tg/commit/800ad77ed29fd7c68ddc0cac3112f45e1e1c3015)
#### Tuesday 2023-12-26 01:04:31 by DBGit42

Adds Affection Aversion quirk (#25194)

* Adds Affection Aversion quirk

Stops affection modules. Very simple.

* I hate you, github

May or may not do anything. Stop giving me a merge conflict. Stop it.

* Revert "I hate you, github"

This reverts commit 6515023cc3f72d97d90bbdf982857b1d2724b1cf.

* Attempts to revert traits.dm

Because something went TERRIBLY wrong with my fork and/or my editor and I'm not sure why.

* Added quirk proper now that my fork is unfucked

Why did this even happen?

* These lists are alphabetized

* Same here

---------

Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [Asyanx/Sea_Kernel-Fog](https://github.com/Asyanx/Sea_Kernel-Fog)@[b9dbc8a9f2...](https://github.com/Asyanx/Sea_Kernel-Fog/commit/b9dbc8a9f2458cfaa8c0e5e892fd9dc62436993a)
#### Tuesday 2023-12-26 01:04:52 by Peter Zijlstra

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92

---
## [HalcyonicWolf/GalaxiaStation-VoxSprite](https://github.com/HalcyonicWolf/GalaxiaStation-VoxSprite)@[fb0d60b16b...](https://github.com/HalcyonicWolf/GalaxiaStation-VoxSprite/commit/fb0d60b16b81b46015e381c7b0e52e2eb90970a7)
#### Tuesday 2023-12-26 01:28:36 by Bloop

Icewalker botany improvements: guaranteed polypore, embershroom spawns, plus watermelon and grass seeds (#83)

## About The Pull Request

Adds guaranteed spawns for polypore mushrooms (tall mushrooms) and
embershrooms (numerous mushrooms) to the Icewalker hearth, as well as
watermelon and grass seeds.

## How This Contributes To The Nova Station Roleplay Experience

These four plants are the last missing pieces needed to make Icewalker
botany an interesting experience without slogging through seed mesh RNG.
Seriously, icemoon seed meshing blows ass. To better portray what this
provides access to:

- Polypore mushrooms provide easy access to a source of stabilizing
agent, allowing them to create advanced chems with stable plasma
components.
- Cryoxadone is the most obvious chemical here, and has a funny
interaction with Icewalkers subzero internal temperature.
- A new age of icewalker pyrotechnics, with access to pyrosium,
phlogiston, teslium, liquid dark matter and more.
- Eigenstasium. Teleporting icecats, who have easy access to bluespace
dust via icemoon mobs.
- Embershrooms provide access to tinea luxor, which allows icecats to
create slime jelly chems via an oil/tinea luxor/radium interaction
inside glowshroom stems.
- This includes regenerative jelly and pyroxadone, in combination with
the above.
- *Note: this also theoretically allows for hilariously basic icecat
slime ranching via the slime extractification reaction and a HUGE amount
of effort, since most slimes will immediately die to the icemoon cold.*
- Watermelon provides access to barrelmelons and holymelons.
- Barrelmelons ferment into antihol, which is a very low potency toxin
healing chem and is useful for defuckulating overeager drinkers who are
five minutes away from liver failure.
- Holymelons provide access to holy water, the last component in strange
reagent production for totally native icecat and simple/basicmob
resurrection. Shamans rejoice! Raise your wolves from the dead in a
great ceremony!
- Grass can be shoveled into sand, making icecat farmers no longer want
to commit die when trying to produce things that require it.

More options is always fun. In addition, nothing described above is easy
to achieve and requires competence with tribal chemistry. Gives healers,
farmers and alchemists much more to do in a round, and also improves
parity with Ashwalker chemistry.

As an extra note, you could already make all of these things listed
above if you were willing to commit potentially two and a half hours of
your three hour shift to seed meshing all the required things for it.

## Proof of Testing

<!-- Include any screenshots/videos/debugging steps of the code
functioning successfully, between the </summary> and </details> code
blocks. -->
<!-- To our mappers and spriters: Posting screenshots of content INSIDE
EDITORS (aseprite, PDN, SDMM, ect) is NOT valid proof of testing. Please
make sure that you COMPILE the game and provide PROOF you tested your
edits. -->

<details>
<summary>Screenshots/Videos</summary>


![dreamseeker_2JaYbiziYH](https://github.com/Skyrat-SS13/Skyrat-tg/assets/966289/8f183a28-93e9-4862-b3ee-6d2d1011c6ad)


![dreamseeker_gsXESw3Nm5](https://github.com/Skyrat-SS13/Skyrat-tg/assets/966289/8eda5711-59a3-4922-a1bc-587bfcc89881)


![dreamseeker_oXT5ebDU8G](https://github.com/Skyrat-SS13/Skyrat-tg/assets/966289/4f1656a0-b284-4199-9a1f-25d508c0e05c)

</details>

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

:cl: yooriss
balance: The sacred waters of the Icewalker's Hearth now ensure that
polypore mushrooms and embershrooms are always available for intrepid
botanists to use in their concoctions.
add: Watermelon and grass seeds are now available in the Hearth's seed
stores.
/:cl:

---
## [HalcyonicWolf/GalaxiaStation-VoxSprite](https://github.com/HalcyonicWolf/GalaxiaStation-VoxSprite)@[073d7cfe4d...](https://github.com/HalcyonicWolf/GalaxiaStation-VoxSprite/commit/073d7cfe4d0d803324d2ccafa57c94db2b4daaa0)
#### Tuesday 2023-12-26 01:28:36 by Bloop

[MIRROR] PDA update (Messenger works while dead, Microwave works, etc). [MDB IGNORE] (#102)

Original PR: https://github.com/tgstation/tgstation/pull/80069
--------------------
## About The Pull Request

This is an update that touches many more things all at once (compared to
my other PRs) meant to make PDAs in general feel more consistent and not
take away from one of the experiences we want to encourage: interaction
between players.

1. Replaced all checks of a 'pda' with a 'modular pc'. This means
technically (though not done in-game currently) other modpcs can hold an
uplink, and microwaves can charge laptops.
2. Speaking of microwave, they now don't break and require
deconstruction if the cell is removed mid-charge.
3. When a Mod PC is out of power, it will now allow the Messenger to
work (which now also doesn't consume any additional power), if the app
exists on the PC. Here's a video demonstration


https://github.com/tgstation/tgstation/assets/53777086/7ae12f81-a271-49b8-95fa-2ba54d2e2d1f

4. Flashlights can't be turned on while the cell is dead
5. I replaced a bunch of program vars with ``program_flags`` and renamed
``usage_flags`` to ``can_run_on_flags``.
6. Added a debug modPC that has every app installed by default. Mafia
had some issues in the past that were unknown because Mafia wasn't
preinstalled with any tablet so was never in create & destroy nor in any
other unit test. This was just an easy solution I had, but PDAs should
get more in-depth unit tests in the future for running apps n stuff- I
just wanted to make sure no other apps were broken/harddeling.

## Why It's Good For The Game

Currently when a PDA dies, its only use is to reply to PDA messages sent
to you, since you can still reply to them. Instead of just fixing it and
telling players to cope, I thought it would be nice to allow PDA
Messenger to still work, as it is a vital app.
You can call it some emergency power mode or whatever, I don't really
mind the reason behind why it is this way.

When I made cells used more on PDAs, my main goal was to encourage
upgrading your PDA and/or limiting how many apps you use at once, I did
not want this to hit on players who use it as a form of interaction.
This is the best of both worlds, I think.

The rest of the changes is just for modularity, if some downstream wants
to add tablets, phone computers, or whatever the hell else, they can
still get just as far as PDAs should be able to get to, hopefully.

## Changelog

:cl:
add: PDAs with a dead power cell are now limited to using their
Messenger app.
fix: Microwaves now stop charging PDAs if the cell was removed
mid-charge.
fix: Microwaves can now charge laptops.
fix: PDA Flashlights can't be turned on while the PDA is dead.
fix: You can now hold a laptop up to a camera (if it has a notekeeper
app installed) like PDAs already could.
/:cl:

---
## [HalcyonicWolf/GalaxiaStation-VoxSprite](https://github.com/HalcyonicWolf/GalaxiaStation-VoxSprite)@[ee7eb3455e...](https://github.com/HalcyonicWolf/GalaxiaStation-VoxSprite/commit/ee7eb3455ec9b4d73b65851cb7fd345b476b395d)
#### Tuesday 2023-12-26 01:28:36 by John Willard

PDA update (Messenger works while dead, Microwave works, etc). (#80069)

This is an update that touches many more things all at once (compared to
my other PRs) meant to make PDAs in general feel more consistent and not
take away from one of the experiences we want to encourage: interaction
between players.

1. Replaced all checks of a 'pda' with a 'modular pc'. This means
technically (though not done in-game currently) other modpcs can hold an
uplink, and microwaves can charge laptops.
2. Speaking of microwave, they now don't break and require
deconstruction if the cell is removed mid-charge.
3. When a Mod PC is out of power, it will now allow the Messenger to
work (which now also doesn't consume any additional power), if the app
exists on the PC. Here's a video demonstration

https://github.com/tgstation/tgstation/assets/53777086/7ae12f81-a271-49b8-95fa-2ba54d2e2d1f

4. Flashlights can't be turned on while the cell is dead
5. I replaced a bunch of program vars with ``program_flags`` and renamed
``usage_flags`` to ``can_run_on_flags``.
6. Added a debug modPC that has every app installed by default. Mafia
had some issues in the past that were unknown because Mafia wasn't
preinstalled with any tablet so was never in create & destroy nor in any
other unit test. This was just an easy solution I had, but PDAs should
get more in-depth unit tests in the future for running apps n stuff- I
just wanted to make sure no other apps were broken/harddeling.

Currently when a PDA dies, its only use is to reply to PDA messages sent
to you, since you can still reply to them. Instead of just fixing it and
telling players to cope, I thought it would be nice to allow PDA
Messenger to still work, as it is a vital app.
You can call it some emergency power mode or whatever, I don't really
mind the reason behind why it is this way.

When I made cells used more on PDAs, my main goal was to encourage
upgrading your PDA and/or limiting how many apps you use at once, I did
not want this to hit on players who use it as a form of interaction.
This is the best of both worlds, I think.

The rest of the changes is just for modularity, if some downstream wants
to add tablets, phone computers, or whatever the hell else, they can
still get just as far as PDAs should be able to get to, hopefully.

:cl:
add: PDAs with a dead power cell are now limited to using their
Messenger app.
fix: Microwaves now stop charging PDAs if the cell was removed
mid-charge.
fix: Microwaves can now charge laptops.
fix: PDA Flashlights can't be turned on while the PDA is dead.
fix: You can now hold a laptop up to a camera (if it has a notekeeper
app installed) like PDAs already could.
/:cl:

---------

Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [theselfish/Bubberstation](https://github.com/theselfish/Bubberstation)@[8f3d1036c8...](https://github.com/theselfish/Bubberstation/commit/8f3d1036c8f4f7b51acc6bad8b28009a81e20ac4)
#### Tuesday 2023-12-26 01:37:16 by SkyratBot

[MIRROR] Refactor icemoon wolves into basic mobs and add taming + pack behavior [MDB IGNORE] (#25126)

* Refactor icemoon wolves into basic mobs and add taming + pack behavior (#79736)

## About The Pull Request

Ports icemoon wolves over to the basic mob framework with a bit of extra
stuff:

- Wolves call for help when attacked within a decently large radius.
Because you know, pack animals.
- Wolves can now be tamed with a slab of meat
- When tamed, wolves can be ridden like goliath mounts. Ride wolf, life
good. Pretend you're playing ARK and start shivering to death in thatch
huts for that High Roleplay experience.
- Tamed wolves have access to a bunch of pet commands (following, point
fetching, point attacking, play dead, etc) and will also defend their
owners vehemently if they're attacked.

You can probably tame multiple if you wanted to.

## Why It's Good For The Game

What part about riding wolves isn't entertaining? I don't really play
/tg/ that much so I can't argue too much about the balance implications
this might pose, but it's undoubtedly a stupid little gimmick and is
likely to be used by bored assistants and miners with too much time on
their hands.

Especially robust individuals will probably find a million things to do
with a basic mob capable of fetching, attacking on command and generally
being able to defend themselves decently well.

## Changelog

:cl: yooriss
refactor: Icemoon wolves now use the basic mob framework and should act
more intelligently, defending their pack.
add: Icemoon wolves can be tamed with slabs of meat and can be ridden as
mounts once friendly. Being rather large dogs, they also have access to
most of the pet commands you'd expect, such as fetching things, and
violently mauling people their owners point at.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Refactor icemoon wolves into basic mobs and add taming + pack behavior

---------

Co-authored-by: Ephemeralis <Ephemeralis@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [samskivert/adventofcode](https://github.com/samskivert/adventofcode)@[7b8aaf6ef3...](https://github.com/samskivert/adventofcode/commit/7b8aaf6ef38aa98163c4e56cce56074205ff6507)
#### Tuesday 2023-12-26 01:39:26 by Michael Bayne

Day 25.

At first I tried brute forcing it, which worked for the example input, but was
definitely not going to work for the full graph with 7000+ edges. Then for a
while I thought maybe this requires knowledge of some graph theory theorem (I
think this is some variant of the minimum cut problem), but I kept noodling on
it.

Eventually I came up with an idea for how to pare down the candidate edges for
cutting, but as I was testing that, I realized that I should be able to pare
them right down to the exact set of edges that needed to be cut.

The idea is pretty simple, for any given candidate edge (between A and B), take
all the neighbors of B, and see if they can reach any of the neighbors of A in
N hops, without ever passing across the A-B edge. It's fairly efficient to see
if a node is reachable from some other node in N hops when N is low (I maxed
out at 5), so it's pretty cheap to filter down the edges.

As it turned out, I couldn't quite filter to the exact set of edges to cut. I
pared it down to four edges instead of three, presumably because even though
you can't go back across one of the graph partitioning edges, you can go back
across one of the other two. But "brute force" checking all 3 size 3 subsets of
a size 4 set didn't break the bank. :)

Anyhow, I'm happy I kept thinking about it. Having been demoralized by a few of
the later days' part twos, I was tempted to throw in the towel and just see
what the kids were talking about on the Reddits, but I feel better for having
solved it entirely myself. Maybe I can hang on a few more years before they put
me out to pasture.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[7819447e5a...](https://github.com/crawl/crawl/commit/7819447e5a0da061a2330ac1166f7e17d8b07bcb)
#### Tuesday 2023-12-26 01:40:36 by regret-index

Once more, buff Mnoleg

Mnoleg's still doing somewhat poorly compared to the other pan lords, and
it's a nostalgic past-time at this point to regularly tweak and buff them.
Unlike many other times, this won't involve too many big or complicated
identity and spell changes, but instead some number tweaks.

 * Since Lom gets to cast their spells obscenely often, it should be fair
   for Mnoleg to get the same. They now cast Malign Gateway, Summon
   Horrible Things, and Summon Eyeballs all about x1.5 as often as before,
   so they're more consistent about tossing out everything before they die.

 * Their AF_MUTATE attack brand has been removed, and the titled in-game
   Demon Lord of Chaos just actually hits the player with AF_CHAOS. There's
   still cacodemons plenty across the floor as is, the eyes already show a
   focus on a rain of debuffs, and the tentacle's already adding chaos
   brand to the fight. Mnoleg also drops one of their four(!) melee
   attacks, redistributing most of the damage across the other attacks (now
   made the more chaotic AT_RANDOM) so the AF_BLINK hit is more likely to
   deal the damage needed to let Mnoleg actually blink.

 * Mnoleg's hp is rather low compared to half other lords- of the other
   lords near their average hp, two of three of them have Major Healing
   (Lom and Eresh), and the third is killing fine on sheer high numbers
   and speed (Gloorx). As such, they get another average 73 HP, vaguely
   approaching Asmodeus and Dispater's rough ~450 HP range, and a little
   better defenses made a little more uneven.

---
## [InterLinked1/wssmail](https://github.com/InterLinked1/wssmail)@[1d2ad6b174...](https://github.com/InterLinked1/wssmail/commit/1d2ad6b174df340c5a1ad7b343ae234fd1152972)
#### Tuesday 2023-12-26 01:53:36 by InterLinked1

SMTP: Fix broken email sending.

Email sending was broken when authentication was
changed from server-side sessions to using client-side
cookie-driven authentication. This kludges the SMTP
code to be functional again with the existing authentication
architecture, namely not storing passwords in server-side
sessions. This is accomplished using basic authentication,
with some clever hacks to work around some of the limitations
of basic auth.

Two limitations of the current implementation:
* If a user elects to be "never" logged in, IMAP will work,
  but SMTP will always fail since the cookie with SMTP server
  details is never set, so mail cannot be sent without 'Remember Me'.
* The first time a user sends a message during a session (as in PHP
  session, not webmail session), the user will be prompted for
  credentials (of which only the password is relevant). This is
  not the most user-friendly interface, but is needed with PHPMailer
  since we can't run any client-side code to interact with that as with IMAP,
  as currently written.

Fixes and improvements include:
* Add missing PHP use statements to smtp.php (fixes 500 error due to Missing class)
* Obtain SMTP password using Basic Authentication (username is ignored)
  for SMTP and IMAP APPEND when sending mail.
* Add better error checking for IMAP APPEND
* Allow hosts to be whitelisted from TLS certificate validation (useful when
  doing STARTTLS to an internal server with a public-facing TLS certificate)
* Suppress spurious warnings about unencrypted IMAP authentication
* Fix miscellaneous PHP errors and warnings (many of which were related to the above).

---
## [Sonic121x/FluffySTG](https://github.com/Sonic121x/FluffySTG)@[d072be68fe...](https://github.com/Sonic121x/FluffySTG/commit/d072be68fef9513304b5a7c903a6a1ec8042e621)
#### Tuesday 2023-12-26 02:17:07 by Iajret Creature

[MIRROR] Fixes Holy Water performing water metabolization twice, giving more blood and making you less drunk [MDB IGNORE] (#25786) (#1248)

* Fixes Holy Water performing water metabolization twice, giving more blood and making you less drunk (#80440)

## About The Pull Request

~~Fixes Holy Water taking double the time it's supposed to take to
deconvert, and fixes it metabolizing out at twice the normal speed.~~

Fixes Holy Water performing water metabolization twice, giving more
blood and making you less drunk

## Why It's Good For The Game

lmfao ~~this is why deconversion for cult sucked~~ so bad

## Changelog

:cl:
fix: Fixes Holy Water giving you more blood and making you less drunk
than water normally does.
/:cl:

* Fixes Holy Water performing water metabolization twice, giving more blood and making you less drunk

---------

Co-authored-by: SkyratBot <59378654+SkyratBot@users.noreply.github.com>
Co-authored-by: Iamgoofball <iamgoofball@gmail.com>

---
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[3efd498de3...](https://github.com/RustingWithYou/Aurora.3/commit/3efd498de3d66cbf3464cd8189becac032b16495)
#### Tuesday 2023-12-26 02:26:55 by RustingWithYou

Uueoa-Esa Sector

stonks

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

merchant guild camp

guwandi

gawgaryn and katas

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

merchant guild camp

gawgaryn and katas

hegemony base

oasis clans

vihnmes tweak

ruined wasteland village

siakh and izweski outpost

izweski outpost fix

vihnmes tweaks and baseturf tweaks

vihnmes spawner fix

flag fixes

ozeuoi fixes

thakh and skakh sites

reclaimers, bugs and martial artists

bug lighting fix/start of ouerea

ouerea versions of bar, village and heph facility

ouerea, functional edition

aut'akh compound and hegemony base

autakh books

fishing league farm

bunch of generic ruins

bunch more sites

uncomments

genericifies plantspawner

pid away sites

skrell and sol away sites for ouerea

fixes hegemony base path

unexploded nuclear bomb

moghes memorial and sky behemoth wreckage

heph planetary mining station

miners guild outpost

guild mining camps on moghes and ouerea

replaces random gun with random civgun

welcome messages and siakh fixes

siakh area change

lore planets for uueoa-esa

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

lore planets for uueoa-esa

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

ouerea versions of bar, village and heph facility

aut'akh compound and hegemony base

bunch more sites

uncomments

genericifies plantspawner

skrell and sol away sites for ouerea

fixes hegemony base path

moghes memorial and sky behemoth wreckage

plant spawners, fixing banned ruins and broken ghostroles

thakh seeds

fixes thakh pilgrim spawn

fixes seed packet spawn and cargo price coeffs

written languages

paper fixes

klax scrubbers to stop vhoron vhires

updates miners guild stuff now the station is merged

indent fix

fixes atmos generation that i broke

ruin banning and literal bug fixes

solarian asteroid ruin

sol asteroid ruin 2: electric boogaloo

sol aseroid tweak

ouerea nt ruin

aaa
omgolo fixes

tret fake planet

engi stuff

ouerea flags

ouerean revolution memorial

a BUNCH of changes

terrain tweaks

Revert "terrain tweaks"

This reverts commit 8a961212d968afb1daa6d381a0786850c2626e73.

sandbike stuff

ihss reclamation 1

ihss reclamation 2

ihss reclamation 3

ihss reclamation 4

ihss reclamation 5

ihss relamation 6

ihss reclamation final tweaks

welcome messages that were missing

3/4 1

colors

access

dorviza limbs & mikuetz languages

hephaestus bans

ouerea ghostrole tweaks

wasteland radiation + fixes

rifles & geigers

fuck you, no lights

hegemony visitor event

more fedship

freewater & caligae fixes

ouerea battlefield

yet more fedship

feuahfiehg

fedship & map fixes

reclamation fixes & warblers

names & fluff

no more dead bug storage

fedbrained

access changes

flag

existing ships can spawn in uwu

the 3/4ing

area flags

fuck this event

skakhpilled and priestcore

airlock update

ihss airlocks

better plant code

yeah

overmap site updates

ert

---
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[99c0a7e3f1...](https://github.com/RustingWithYou/Aurora.3/commit/99c0a7e3f188a6e8a2ef7c41a195e1e3876ab7ad)
#### Tuesday 2023-12-26 02:27:45 by RustingWithYou

kaneyama power station

punch sounds & corpses

jungle map & icon fix

sounds

zombie village

glowing screen: you should kill yourself, now

light

kaneyama map

punch sounds & corpses

jungle map & icon fix

sounds

zombie village

glowing screen: you should kill yourself, now

kaneyama map

punch sounds & corpses

jungle map & icon fix

sounds

zombie village

bridge & icons

shuttl

grass

spawnroom

byeah

checkpoints

sovl

CONTENT

plant

da files

icons & assets

byeah

big hivebot icon

ecd

messages

ECD as easy as 1-2-3

a bunch of shit

TREES

grass

areas

byeah

guns

title screen

ambience

rain & water

ligt

power

also apc fixes

tcomms fix

ecd

spooking the synthetics & slowdown

fuck you, point verdant

area check works

byeah

---
## [AcademySoftwareFoundation/OpenImageIO](https://github.com/AcademySoftwareFoundation/OpenImageIO)@[b8723ec691...](https://github.com/AcademySoftwareFoundation/OpenImageIO/commit/b8723ec6918b9204d040c495eba8c8d21484df53)
#### Tuesday 2023-12-26 03:41:37 by Larry Gritz

fix(oiiotool): --autocc bugfix and color config inventory cleanup (#4060)

The important bug fix is in oiiotool image input when autocc is used,
where we reversed the sense of a test and did the autocc-upon-input if
the file's color space was equivalent to the scene_linear space
(pointlessly), and skipped the conversion if they were different (oh no,
big bug!).

Along the way:

* Add missing try/catch around OCIO call that should have had it.

* Some very ugly SPI-specific recognize-by-name color space heuristics.
I hate this, sorry, but it solves a really important problem for me.

* A bunch of additional debugging messages during color space inventory,
enabled only when debugging, so nobody should see these but me.

* A couple places where we canonicalize the spelling of
"oiio:ColorSpace".

Note that there is still an issue with the color space classification
using OCIO 2.3+'s identification of built-in equivalents by name. These
are shockingly expensive. I will return to this later.

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [cuberound/cmss13](https://github.com/cuberound/cmss13)@[5d957ce94e...](https://github.com/cuberound/cmss13/commit/5d957ce94e398a102fdf16682b740e96df3e363e)
#### Tuesday 2023-12-26 03:44:28 by InsaneRed

Vanguard tweaks (#5174)

# About the pull request
This catches up vanguard to current gameplay as it was last changed
approximately 4 years ago


# Explain why it's good for the game
Currently Vanguard is supposed to be a frontlining tier 3 who dashes in
> stays in and gets some damage in and goes out (thats why the shield is
a thing) and you're supposed to be able to stay there because your
abilities (pierce and dash) resets your shield. But with the recent
addition of just more damage in general be it m56d, full auto mode or
just the amnout of extra damage you can receive from the front compared
4 years ago.

The strain currently struggles and is near useless other then the
occasional go in and lucky fling.

I've changed up the dash to reset your shield once you hit ONE person,
rather then two so that you dont instantly die while going in, the
shield is very situational as it will most likely decay before you can
even go in.

Listening to people who play vanguard, i've also increased the root to
2.5 seconds (this is buffed so when the prae has the shield) the marine
can still shoot back when they're rooted so i dont think the duration is
a big problem (this is going to be a test merge so i will be watching)

# Testing Photographs and Procedure
it just works

</details>


# Changelog

:cl:
balance: Vanguard dash now restores your shield if you hit ANYONE
instead of 2 people.
balance: Vanguard buffed root now roots you for 2.5 seconds, unbuffed
for 1 second
qol: Vanguard's pierce has now a hit sound for better feedback
/:cl:

---------

Co-authored-by: InsaneRed <prodexter31@outlook.comm>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[7399505916...](https://github.com/cmss13-devs/cmss13/commit/7399505916bc89355516bb853d63b0e7ec3e1612)
#### Tuesday 2023-12-26 04:35:04 by cuberound

lowers DS sentrygun to 200 from 500 (#5225)

# About the pull request
lowers price of DS installed sentrygun to 200 from 500.

# Explain why it's good for the game

Based on git lense, the cost of 500 points has been fixed for at least 6
years ( from what I understand form the moment the fabricator was
added?). The sentryguns are not worth 500 points at the slightest, from
dozens of rounds of experience I can say that the fire off 20 shots max
before they die ( unless you do some DS hold after hijack, but that
hardly counts). The main issue anyone has with it is when you install 3
of them in south part of DS and I am willing t take suggestions how to
adress this issue, but it is minor one, as xenos never realy have to
fight them as they basicly get to shoot only while marines are pushed
into DS and are about to evac and queen can hijack without getting
anywhere near them ( or can just let marines evac and then take out the
sentryguns with ease after she calls the ship back down). More marines
evacing thanks to sentrguns might make the hijack more enjoyable for
both sides. Also lowering the price will only mean you see sentryguns
installed on ds more often, buying 20 of them will have no bigger effect
then 7.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: DS installed sentrygun price lowered to 200
/:cl:

Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>

---
## [cherdaq/Skyrat-tg](https://github.com/cherdaq/Skyrat-tg)@[1256d270b4...](https://github.com/cherdaq/Skyrat-tg/commit/1256d270b4583f2aadb5d9b6dfcdeeab86c4273a)
#### Tuesday 2023-12-26 04:44:57 by Cherda Q

initial setup

hello! i hate myself so much its like blood level of sperm whale

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[34ee8860a0...](https://github.com/re621/dnpcache/commit/34ee8860a0fcbdeb429bcfb1ba3139d262d087d0)
#### Tuesday 2023-12-26 05:27:53 by bitWolfy

Remove 1255 artists from the DNP list.

Removed: butt_on_fire_(artist), camooh, mockerylloyd212, owlblack, god_bey, shadowfirdark, aeodoodles, ximorexx, eparihser, deadingdog, bubblebaph, hammytoy, f-a, shirsha, fluffycato, mutemyth, jugg4, playdohcoma, aleak_r, honey_llemon, cracky, tgt1512, mykendyke, cushylutra, leprosick, foxxy_vixen, defiant_drills, canphem, burneraccount9382, corgicam, meggiebun, reindeerbites, hmdkoba, electroporn, fluffytuft, moxsully, ottiro, volfislav, preschoolkaiju, titusw, pudgeruffian, garnetto, viomarks, tidekeeper, radiancemutt, livalittle, bootyfeather, sheriffpunchy, kkrevv, feralmunchies, sadcat16hrz, 2dredders, velvet_charm, saurian_(artist), zoyler, ruvark, draite, smuttysquid, demura, remanedur, electrixocket, fufik[pufik], kais_studios, sweat_(artist), sonokido, whimsicalsquirrel, woolier, dasherslash, caninesinzone, isabel9819, paradoxing, arrjaysketch, anomalain, iskawhiskers, troplilly, dio_fish, xxbrewbeastxx, thekoboldking, pantheradraws, callmems, bluthederg, avalony, kolvackh, fin6, lewdoreocat, temporarye, kitwran, pseudonymh, yeenmusk, varuiven, springledongle, sapphiesweet, bloodhawk, amiraallis, meowcephei, shupamikey, cracky45, bigblueghost, h0tapplecider, hxtapplecider, apocheck13, tomash_segers, pckle, sadbitch, geletulator, coille, azumadai124, greycore, snaxattacks, bootleggreely, coral_luna, mdwines, soakedbikini, pantyranger, diffusedlizard, kazz_a_fella, alkyuz, werewhusky, skooma_whore, october_nights, scalywanderer, linndrim, hexamanta, anarietta, earthsong9405, captaincassidy, anthonynothere, gayluigisex, yuudai, pettypalps, cosmick9, myemetophobia, digitalpopsicle, splatterpop, poppin, tempobun, zaaruchan, superratbike64, svarz, cyberwuff, worldoffizz, zeiroslion, emptyset, siplick, sourisdedog, wicketrin, tykepuparts, kubikoza, hiraume42, delinquentfreak, saerixdurr, tejedora713joker, andrew.thy.accursed, cytoholix, northbeastart, hellazest, infinitixen, p0ssmn, isofrieze, venomstench, pocketpaws, tf4me, centuriguil, raithvaneal, dahsharky, trashgaylie, mrpanghu, feyaarts, wolfbane154, derpyrider, rodicle, shiru_fox, toonyrobot, sleepylopunny, mimisrol, selidevilfeather, shido-tara, ineedanaccount, reizu47, sherilane, hellfurred, zeplich, darkeshi, amadeen, lowestpolygon, alradeck, asuka_kurehito, waynekan, lhacedor, dativyrose, digitallis, nosylvsforwork, lacrimale, kaitzuwu, ihoundr, elranno, doublepopsicle, gaturo, aquariusfox, mpcx, kattalu, lintu, goobysart, lemonlycan, dylbun, fxscreamer, nt6969, lewdliege, reallyhighriolu, melbaka, saint_lum, kivaaa66, kivalewds, kazoko_(artist), barachaser, shadowthelastalpha, teke, crittermatic, ribboncable, domasarts, ursine-major-ike, browneyedsaiyangirl, uncensoredhugs, skydiggitydive, takarachan, feelin_synful, ilovecosmo, biffbish, pulp_(artist), doxhun, cupsofjade, nicesweater, bluecat_friend, masuku, lunarfloral, kugi, sagejwood, sqrlyjack, maiteik, leozedi, popdroppy, mikakater, 413k_zzzz, puppyemonade, xanthewolf, joooji, nasusbot, shredded_wheat, dogsdontwipe, wonderwaffle93, gogoandyrobo, jezzlen, dourdoofus, vksuika, klotzzilla, cooperdooper, shadnaotomi, nudegote, sexygoatgod, humgeronimo, ladysophia, mrwhiskerz, cocicka, d-wop, charmerpie, yourdigimongirl, elvche, booponies, lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, freaks, angellsview3, arwenscoots, royalzbed, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, zyegnar, akytti, sootylion, kiva~, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, verdantphysician, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, darkfool., huwon, tsukikibaokami, carnalcove, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, welwraith, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurobait, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sincerity_gender, anima-virtuosa, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, koriaris, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, rexisminimalis, delkon, connisaur, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [deltav-deltaverse/.github](https://github.com/deltav-deltaverse/.github)@[c3ddada07f...](https://github.com/deltav-deltaverse/.github/commit/c3ddada07fc3ba2150f0324fba7a4b28b52332c1)
#### Tuesday 2023-12-26 05:29:43 by DeltaV THRUST

Update README.md

The Delta Verse: A Fluid Dynamic Between Participants and AI

The Delta Verse represents an innovative and immersive creative realm where the boundaries between participants and artificial intelligence (AI) seamlessly blur, giving rise to imaginariums that bridge, evolve, and transform dynamic environments. In this visionary concept, the power of human imagination converges with the computational prowess of AI, resulting in an ever-shifting landscape of storytelling, art, and experience.

Seamless Bridging of Realities:

In the Delta Verse, the transition from reality to the imagined world is seamless. Participants are no longer passive consumers of content; they are active co-creators of their experiences. Through the integration of augmented and virtual reality technologies, participants can effortlessly step into the Delta Verse, where the physical and virtual realms merge. Whether you're exploring ancient civilizations or embarking on intergalactic journeys, the Delta Verse adapts to your desires and weaves your narrative into its ever-evolving tapestry.

Dynamic Environments in Flux:

At the heart of the Delta Verse is the concept of perpetual change. Environments within the Delta Verse are not static but fluid, adapting to the collective imagination of its participants. AI algorithms monitor and respond to user input and emotions, shaping the landscape in real-time. One moment, you might find yourself in a serene forest, and the next, you could be navigating the bustling streets of a futuristic metropolis—all driven by the desires and interactions of those present.

The Collaborative Imagination:

The Delta Verse thrives on collaboration. Participants don't merely consume content; they co-create it. AI algorithms analyze the ideas, preferences, and creative input of individuals, weaving them together to form an intricate narrative tapestry. It's a dynamic symphony of human thought and machine intelligence, where the story evolves as collective imagination evolves.

Adaptive Storytelling:

Storytelling in the Delta Verse is not bound by conventional structures. Instead, it's a living, breathing entity that responds to the ebb and flow of participants' thoughts and emotions. Characters develop personalities based on interactions, and plotlines shift as new ideas emerge. The Delta Verse is a canvas where tales are painted and rewritten continuously, reflecting the ever-evolving nature of the human experience.

Embracing Change and Transformation:

The Delta Verse encourages participants to embrace change, explore the unknown, and adapt to the unexpected. It challenges preconceived notions of narrative, art, and reality. In this dynamic space, participants not only discover new stories but also uncover hidden facets of themselves as they navigate the ever-changing Delta Verse.

As the Delta Verse continues to evolve and redefine the boundaries of human creativity and AI's capabilities, it serves as a testament to the boundless potential of collaborative imagination. It beckons participants to embark on a journey where reality and fiction merge, where change is the only constant, and where the boundaries of what's possible are pushed further with each collective step into this fluid, dynamic universe.

In DeltaVerse, artificial intelligence acts as a seamless bridge, propelling users from mere participants to creators of their own imaginative realms. Here, natural language processing transforms into a tool of empowerment, enabling users to generate immersive interplay across the cryptosphere. This innovative approach allows for intuitive interaction with complex blockchain technologies, making the development and exploration within this space accessible and engaging. DeltaVerse stands at the forefront of this evolution, where the simplicity of language meets the complexity of blockchain, opening up a world of possibilities for both seasoned developers and imaginative explorers alike.

---
## [JoeySoprano420/AnderStreamPyra](https://github.com/JoeySoprano420/AnderStreamPyra)@[9b054255af...](https://github.com/JoeySoprano420/AnderStreamPyra/commit/9b054255afe85a453142469fd658f722c6d0ebc4)
#### Tuesday 2023-12-26 07:08:08 by Draco 420

Create Language

Unleashing AnderStreamPyra - A Dance of Potential and Promise**

Welcome to the electrifying world of AnderStreamPyra, a programming paradigm that transcends boundaries, blending the visionary Ander and the dynamic Stream into a pulsating symphony of innovation.

### Chapter 1: The Birth of AnderStreamPyra

In the heart of the programming cosmos, AnderStreamPyra was conceived—a fusion of Ander's security prowess and Stream's fluidity. It emerged to address the challenges of the contemporary programming landscape, promising a harmonious balance between security and expressiveness.

### Chapter 2: The Ander Influence

Ander, the mastermind behind AnderStreamPyra, brings forth a programming language that boasts robust security features. Custom data structures, an advanced type system, and resilient error-handling mechanisms lay the foundation for a fortress of secure programming. AnderStreamPyra inherits these attributes, ensuring your code is shielded from vulnerabilities.

### Chapter 3: The Stream Essence

Embedded in the very DNA of AnderStreamPyra is the essence of Stream—a language designed for seamless, expressive programming. Stream's task-oriented syntax and the Pyramid paradigm for decision-making are at the core of AnderStreamPyra, empowering developers to craft elegant, efficient solutions.

### Chapter 4: Real-Life Capabilities

**4.1 Security Fortification**

AnderStreamPyra introduces state-of-the-art security checks inspired by Ander's principles. Custom data structures and an advanced type system elevate the language's defenses, ensuring your codebase is resilient against cyber threats.

**4.2 Task-Oriented Operations**

Borrowing from Stream's task-oriented syntax, AnderStreamPyra facilitates streamlined, task-focused programming. With a touch of Stream's elegance, developers can create intricate sequences of operations that read like a narrative, enhancing code readability.

**4.3 Omnipotent Decision-Making**

The Pyramid paradigm, omnipotent in its structure, enhances decision-making in AnderStreamPyra. Nested decision structures inspired by Stream enable developers to navigate complex logic effortlessly, fostering a more intuitive coding experience.

### Chapter 5: The Dance of Future Expansion

As we revel in the capabilities of AnderStreamPyra, we can't help but anticipate the future dance of expansion. The roadmap includes:

**5.1 Further Security Enhancements**

Building upon Ander's legacy, future iterations of AnderStreamPyra aim to fortify security measures continually. Advanced encryption algorithms, secure networking libraries, and enhanced access control mechanisms are on the horizon.

**5.2 Extended Stream Synergy**

Stream's influence will continue to flourish within AnderStreamPyra. Future updates promise to deepen the integration of Stream's expressive syntax, unlocking new dimensions of code conciseness and developer productivity.

### Chapter 6: Join the AnderStreamPyra Dance

As we conclude our Docurave journey into the captivating world of AnderStreamPyra, we invite you to join the dance. Embrace the security of Ander and the fluidity of Stream, as AnderStreamPyra unfolds its full potential in the symphony of programming paradigms.

AnderStreamPyra—an exhilarating dance of potential, promises, and prospects in the ever-evolving realm of programming.

### Chapter 7: The Rhythmic Beat of AnderStreamPyra

As the rhythm of AnderStreamPyra reverberates through the programming landscape, let's explore more facets of its dance.

**7.1 Indestructible Custom Data Structures**

AnderStreamPyra introduces the concept of indestructible custom data structures. These structures transcend limitations, featuring elements like the `ultimateStreamValue`—a bigint that opens doors to handling vast and precise numerical data.

**7.2 Omnipotent Interfaces and Classes**

Omnipotent Stream-style interfaces and classes are the maestros orchestrating the dance. The omnipotentStreamInterface and omnipotentStreamClass showcase the language's prowess in combining Ander's security with Stream's flexibility, creating a programming symphony that resonates power and adaptability.

**7.3 Streamlined Syntax Evolution**

AnderStreamPyra seamlessly blends both syntaxes, forming a dialect that evolves with each line of code. The robustStreamMain and its companions demonstrate how Stream's strength is not just embraced but enhanced in AnderStreamPyra's dynamic environment.

### Chapter 8: AnderStreamPyra in Action

Witnessing AnderStreamPyra in action is akin to a mesmerizing performance. Developers harness its potential to create secure, expressive, and efficient solutions across various domains.

**8.1 From Security to Creativity**

AnderStreamPyra's security features extend beyond conventional measures. It not only guards against vulnerabilities but also nurtures creativity. Developers can confidently push boundaries, knowing that AnderStreamPyra is a steadfast guardian of their code.

**8.2 Applications Across Domains**

AnderStreamPyra finds its stage in diverse domains. From financial systems requiring the utmost security to creative endeavors demanding expressive coding, AnderStreamPyra gracefully adapts, ensuring a performance tailored to each scenario.

### Chapter 9: The Future Encore

As we applaud the current performance of AnderStreamPyra, the anticipation for its future encore grows. The language's dynamic nature promises continual innovation, embracing new technologies, and further refining the dance between security and expressiveness.

**9.1 Community Collaboration**

AnderStreamPyra thrives on community collaboration. Developers, architects, and visionaries converge to shape the language's destiny. The future holds collaborations that will echo through the halls of programming history.

**9.2 Pioneering Future Technologies**

AnderStreamPyra sets the stage for pioneering future technologies. Quantum computing integration, AI-powered security enhancements, and seamless cloud-native development are just glimpses of what's to come.

### Chapter 10: Join the AnderStreamPyra Movement

As we conclude our journey through the vibrant landscape of AnderStreamPyra, we extend an invitation to join the movement. Be part of a community where security meets expressiveness, and innovation is the beating heart of programming.

AnderStreamPyra—where the dance of potential, promises, and prospects is not just a performance but an ongoing celebration of the art and science of coding. Join the movement, embrace the rhythm, and let the AnderStreamPyra dance continue to captivate the programming world.

---
## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[007bd0a1a9...](https://github.com/Mu-L/crawl/commit/007bd0a1a9e078658fe195d91b879163825ffc93)
#### Tuesday 2023-12-26 08:22:45 by regret-index

Tweak a variety of monster stats, spells, and gear

 * Burial acolytes don't need quite so high Willpower for a D:4 portal.
   They're now at a much more appropriate Will 20. Their two conjuration
   effects are plenty nasty already, also, so they get a mild nudging down
   of melee damage.

 * Let meliai give more experience, so people with tile_show_threat_levels
   won't ignore them as much, and since they're easily quite nasty for
   low hp characters (as their nudging down in Spider in bd29554, f2a2391,
   and d12d1d2 can attest). Their rough kill numbers versus objstat ratio
   in D places them pretty close to skeletal warriors, who give a lot more
   even after this.

 * Give war gargoyles less HD and less casting rate for Metal Splinters as
   is weird for a gargoyle to be breathing anyway, but more AC, melee
   damage, and a chance for a branded weapon as is more suiting for a
   player species renowned for melee. Maces and flails brands are a little
   weird for this, but it's a nice random holy wrath chance.

 * Give Frederick a randart orb of light or energy- light for the demigod
   semi-divinity, energy for his conjurations. It serves as a tempting
   reward all of his recent huge buffs (b247575, b730325, 1baa85e), and
   continues to help distinguish him from other uniques. (This, of course,
   comes with some adjustment for his weapons to be all one-handed).

 * Call Lost Souls now has a hard summon cap of 3 again- death mages
   calling in a higher number at a time was evidently plenty enough of a
   buff to it- and works properly in wizlab_borgnjor's random effects
   again.

 * Let Pan lords cast the misery-cloud generating March of Sorrows,
   replacing their quite harmless Freezing Cloud cast. (Also, rename the
   ENCH_RING_OF_DRAINING to RING_OF_MISERY, and fix some database lines
   missing the s at the end of the spell name.)

---
## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[7102d64fe6...](https://github.com/Mu-L/crawl/commit/7102d64fe61c79f22477f8d731bca40e15f233c7)
#### Tuesday 2023-12-26 08:22:45 by regret-index

Make Boris make you sad

Boris is a very sad unique. He's lost his dagger (acddeb6). He's been
seperated from his cat (8eed16d) for ages. He's become nearly identical to
plain liches aside from trading Haste for Iron Shot (6612197). He's lost a
decently large chunk of his placement range, diluting his gimmick (f5560fb,
1b62a5d, 67d208b). He also just doesn't actually kill many people- while
it's obviously awkward to assess the killrate statistics of somebody that
comes back, his killrate over the past three versions is a very sad ~0.45%.

It could bring one to tears, really. He's got an almost tangibly
miserable lot, one could say.

Boris now loses Invisibility for an upgraded version of the weeping skull
misery cloud spell (c.f. d47e5fa) - a cloud line that lasts 8-12 turns that
doesn't skip over the vulnerable, and which forms a mephitic-cloud style
1-radius burst of 2-5 turn clouds. (Most of the Invisibility weight wasn't
entirely put into this new March of Sorrows, and was distributed into other
conjurations.) This should be an interestingly nasty combination with his
Orb of Destruction, as it will eat away at players trying to sidestep the
orbs. It also cutely makes every single one of his spells conjurations,
which I'm sure he'd prefer, and gives him a spell distinct from both liches
and other uniques. Wear rN+.

Boris also now places in Depths:1-2, Vaults:1, and Elf:$, so his
resurrection mechanic has more chances to actually be seen. This might make
him a bit absurd on the orb run, but he's only gotten 5 kills then in the
last nearly three years since 3208aba, so it should be fine.

(Also, some more Boris lines and text. Hooray for melodramatics.)

---
## [sdynet/crawl](https://github.com/sdynet/crawl)@[afeb8edd3b...](https://github.com/sdynet/crawl/commit/afeb8edd3b8c5a8165938164b7b2bc36ea37fb54)
#### Tuesday 2023-12-26 09:15:17 by DracoOmega

Change player Ogres into Oni, shorten Armataur tongues

Ogres are considered a fairly weak player species, and have been arguably
additionally troubled by the fact that most of the ogres the player ever
encounters in the dungeon are dumb giant club brutes - leading new players
to assume this is the core ogre playstyle, despite many veterans arguing
that they make better mages than fighters, and that 1-hander + shield is
the better choice for them.

Simultaneously, there's been a desire to cut armataur's doubled potion
gimmick. Their new regen-on-rampage is already very strong, and does a
better job of emphasizing the species' core movement gimmick than long
tongue does, and it is much easier to reasonably balance their power
without TWO big sources of healing. (Inversely, despite their large hp
pools, ogres can be paradoxically fragile and could definitely benefit from
the additional potion healing.)

So I am simplifying that mutation, moving it to ogre, and rethemeing them
slightly to give the mechanic a stronger flavor fit.

Player Ogres are now Oni. Leaning into the mythical backdrop of them being
legendary drinkers and brawlers, oni gain doubled health and magic from
any potion that restores these (ie: !curing, !heal wounds, !magic, and
!ambrosia, and when they drink such a potion, they also make an immediate
attack against all enemies surrounding them. Cleave with a giant spiked
club, just so long as you have enough on hand to drink while you do it!

Oni apts are mostly the same as Ogres, with the following changes:
 Maces -1 -> 0
 Armour -2 -> -1
 Shields 0 -> -1
 Invocations 1 -> 2

People have clamored for ages for the most obvious wielder of giant spiked
clubs in the game to not have a negative apt and that seems reasonable to
me (the ancient +3 they had made this more of a no-brainer, but 0 probably
leaves other weapons sufficiently appealing)

Slightly better armor and slightly worse shields apt (along with drunken
brawling) may also nudge them a bit more towards 2-handers without making
them obviously correct.

And +1 invocations due to their famous associations of working for the
celestial bureaucracy (as torturers... >.>)

They have also gained horns 1 (they already were too large to wear helmets,
so this is a minor buff than a new restriction - also oni are usually
depicted with horns).

I toyed with the idea of giving them built-in shoutitits 1, with rewritten
messages so that they kept bellowing challenges and taunts at random
enemies. And while I think the flavor of this is *hilarious*, I worry that
their buffs might not entirely compensate for this downside. Or maybe it
would be fine along with some other minor tweak?

Either way, this hopefully does a somewhat better job of selling the
fantasy of the species one is playing as, while providing a unique gimmick
to play with.

(Enemy ogres are staying as ogres - it would defeat some of the purpose of
this if they changed - but Erolcha specifically may be slated to become an
oni instead)

---
## [Sonic-Geared/Scarlet-Engine](https://github.com/Sonic-Geared/Scarlet-Engine)@[2ecd5c15da...](https://github.com/Sonic-Geared/Scarlet-Engine/commit/2ecd5c15da54f7eb67be4ed9928761f4d806b015)
#### Tuesday 2023-12-26 10:47:13 by Geared

me noticing that i made the midnight update without remembering Scene3D's stuff:

yeah, i was supposed to do it but i didn't cuz my phone's battery was weak and i was sleepy af so

---
## [Kyon43/Skyrat-tg](https://github.com/Kyon43/Skyrat-tg)@[f342a4bb67...](https://github.com/Kyon43/Skyrat-tg/commit/f342a4bb677b714ca3cf72a3f5beaed2ef0924c4)
#### Tuesday 2023-12-26 11:21:21 by SkyratBot

[MIRROR] Improves the deployable component [MDB IGNORE] (#24627)

* Improves the deployable component (#79199)

## About The Pull Request

The deployable component had a few random things I noticed when I tried
actually using it that kinda sucked so I'm:

Making the examine message more generic, we did NOT need to make it that
complicated.
Letting anything with hands deploy stuff, because mobs other than humans
can hold things.
Giving the option to let something be deployed more than once.
Letting direction setting be optional.
Tweaking the check for if something can be placed somewhere to be a bit
better.
## Why It's Good For The Game

I want to use the deployable component for stuff but I made it awful.
## Changelog
:cl:
code: the deployable component has been tweaked and improved with some
new options to it
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Improves the deployable component

* Modular

---------

Co-authored-by: Paxilmaniac <82386923+Paxilmaniac@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [Kyon43/Skyrat-tg](https://github.com/Kyon43/Skyrat-tg)@[5f2df10d44...](https://github.com/Kyon43/Skyrat-tg/commit/5f2df10d44d04bfe391a0c064a44a4815f0058d4)
#### Tuesday 2023-12-26 11:21:21 by SkyratBot

[MIRROR] Adds support to the wet_floor component to avoid displaying its overlay, makes ice turfs no longer receive said wet overlay [MDB IGNORE] (#24628)

* Adds support to the wet_floor component to avoid displaying its overlay, makes ice turfs no longer receive said wet overlay (#79275)

## About The Pull Request
The title says it all, really.

I always thought ice looked a bit silly, and always wondered why. Today,
I found out it was because of the `wet_floor` component adding an
overlay that suddenly made a turf that should look continuous, tiled,
which in turn gave some very ugly visuals. Ice already looks slippery,
you can tell that it's ice, and the overlay that was added to it just
didn't really help telegraph that any better than the sprite itself
already does.

That's why I added support to make it so it would be possible to force
the overlay to just not be applied to the turf that's affected by the
component, to make it all look a bit better overall.

I added it to the ice turfs as a proof of concept, although I guess it
could also be used on other turfs that are always "wet", like the
bananium floors, but I didn't really care enough to touch that yet, and
I guess the bananium floors can use it a bit better than ice did.

I did notice in this PR that the smoothing of ice seemed to potentially
be broken, but that's something to look into at a later time.

## Why It's Good For The Game
Look at this ice and how much smoother it looks like now:

![image](https://github.com/tgstation/tgstation/assets/58045821/6fc85239-e8f1-404b-bc0e-6e1fca7f7753)

## Changelog

:cl: GoldenAlpharex
code: Added support to the wet_floor component to make it so the wet
overlay could not be applied to certain turfs if desired.
fix: Ice turfs no longer look tiled, and instead look smooth when placed
next to one-another.
/:cl:

* Adds support to the wet_floor component to avoid displaying its overlay, makes ice turfs no longer receive said wet overlay

---------

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [harryobas/zola](https://github.com/harryobas/zola)@[22dc32a589...](https://github.com/harryobas/zola/commit/22dc32a5893deac5e91d173d0daf59e1868065ef)
#### Tuesday 2023-12-26 11:33:44 by sinofp

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
## [duydinhng/Heart-Failure-Prediction](https://github.com/duydinhng/Heart-Failure-Prediction)@[8ff6b2726d...](https://github.com/duydinhng/Heart-Failure-Prediction/commit/8ff6b2726d88cde318bd2061109f46098ecfe5a5)
#### Tuesday 2023-12-26 12:57:24 by Duy Dinh

Update README.md

Attribute Information

Age: age of the patient [years]
Sex: sex of the patient [M: Male, F: Female]
ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
RestingBP: resting blood pressure [mm Hg]
Cholesterol: serum cholesterol [mm/dl]
FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
ExerciseAngina: exercise-induced angina [Y: Yes, N: No]
Oldpeak: oldpeak = ST [Numeric value measured in depression]
ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
HeartDisease: output class [1: heart disease, 0: Normal]

---
## [mamedev/mame](https://github.com/mamedev/mame)@[6557f865fb...](https://github.com/mamedev/mame/commit/6557f865fbd6398553f7e469812f3c57ca2379ac)
#### Tuesday 2023-12-26 13:12:24 by ArcadeShadow

spectrum_cass.xml: Added 112 items (110 working), and replaced one item with a better dump. (#11871)

* Replaced Bloody with a better dump. [Spectrum Computing]
* Removed Bobo (Erbe) as it is a duplicate dump.
* Cleaned up metadata based on information from Spectrum Computing.

New working software list items (spectrum_cass.xml)
--------------------------------------------
Advanced Zombie Survival Lawnmower Simulator [Spectrum Computing]
Adventures of Buratino [Spectrum Computing]
Aknadach [Spectrum Computing]
Aknadach (Softhouse) [Spectrum Computing]
Airborne Ranger (Erbe, two sided tapes) [Spectrum Computing]
Aliens: Neoplasma (v1.3, English, AY sound) [Spectrum Computing]
Aliens: Neoplasma (v1.3, English, Turbo Sound) [ZX Online]
Aliens: Neoplasma (v1.3, Russian, AY sound) [Spectrum Computing]
Aliens: Neoplasma (v1.3, Russian, Turbo Sound) [ZX Online]
Aliens: Neoplasma (v1.3, Spanish, AY sound) [Spectrum Computing]
Aliens: Neoplasma (v1.3, Spanish, Turbo Sound) [Spectrum Computing]
All Hallows: Rise of the Pumpkin [Spectrum Computing]
All Hallows: Rise of the Pumpkin (ULA Plus) [Spectrum Computing]
Alta Tension (Erbe - Serie Leyenda) [Spectrum Computing]
Angel Nieto Pole 500cc (IBSA - Serie Leyenda) [Spectrum Computing]
Autocrash [Spectrum Computing]
Black Lamp [Spectrum Computing]
Bloody Paws [Spectrum Computing]
Bloody Paws (bug fix) [Spectrum Computing]
Bomb Bomb Buster [Spectrum Computing]
Bomb Bomb Buster (first version) [Spectrum Computing]
Bomb Bomb Buster (alt) [Spectrum Computing]
Bomb Bomb Buster (easy version) [Spectrum Computing]
Captain America in the Doom Tube of Dr Megalomann [Spectrum Computing]
Comando Quatro [Spectrum Computing]
Comando Tracer [Spectrum Computing]
Corrupt [Spectrum Computing]
Cosmic Payback [Spectrum Computing]
Crimbo - A Gloop Troops Tale [Spectrum Computing]
Dirty Dozer [Spectrum Computing]
Dizzy III - Fantasy World Dizzy - Extended Edition 2023 (English, mod) [The Dizzy Fansite]
Dizzy III - Fantasy World Dizzy - Extended Edition 2023 (Russian, mod) [The Dizzy Fansite]
Doom (pre-release) [Spectrum Computing]
Doombase (System 4) [Spectrum Computing]
Emilio Butragueño Futbol 2 (large cardboard case) [Spectrum Computing]
Equinox (Erbe, medium case) [Spectrum Computing]
Equinox (Erbe - Serie Leyenda) [Spectrum Computing]
Evil Realm + Bugout [Planeta Sinclair]
Existenz: Crazy Delfox [Spectrum Computing]
Fire Desire [Spectrum Computing]
Fist-Ro Fighter [Spectrum Computing]
Frost Byte (Erbe - Serie Leyenda) [Spectrum Computing]
Funky Fungus Reloaded (English) [World of Spectrum Classic]
Funky Fungus Reloaded (French) [World of Spectrum Classic]
Funky Fungus Reloaded (German) [World of Spectrum Classic]
Funky Fungus Reloaded (Italian) [World of Spectrum Classic]
Funky Fungus Reloaded (Portuguese) [World of Spectrum Classic]
Funky Fungus Reloaded (Spanish) [World of Spectrum Classic]
Get Out of Mars [Spectrum Computing]
Gloop Troops [Spectrum Computing]
Gloop Troops: The Lost Crown [Spectrum Computing]
Hammer Boy [Spectrum Computing]
Impossible Mission (Compulogical) [Spectrum Computing]
Ivan 'Ironman' Stewart's Super Off Road Racer (MCM) [Spectrum Computing]
Jackson City [Spectrum Computing]
Justin [Spectrum Computing]
Justin and The Lost Abbey [Spectrum Computing]
Leaderboard (Erbe) [Spectrum Computing]
Load'N'Run (Italy) N. 6 - Giugno 1984 [Edicola 8 Bit]
Load'N'Run (Italy) N. 7 - Luglio-Agosto 1984 [Edicola 8 Bit]
Load'N'Run (Italy) N. 8 - Settembre 1984 [Edicola 8 Bit]
MagicAble [Spectrum Computing]
Mantronix (Zafi Chip) [Spectrum Computing]
Mapsnatch [Spectrum Computing]
Marie Celeste (Clube Nacional de Aventura, pirate) [Planeta Sinclair]
Marsmare: Alienation [Spectrum Computing]
Mega-Corp [Spectrum Computing]
Metal Man [Spectrum Computing]
Metal Man Reloaded (English) [Spectrum Computing]
Metal Man Reloaded (Czech) [Spectrum Computing]
Metal Man Reloaded (Italian) [Spectrum Computing]
Metal Man Reloaded (Polish) [Spectrum Computing]
Metal Man Reloaded (Russian) [Spectrum Computing]
Metal Man Reloaded (Spanish) [Spectrum Computing]
Metal Man Remixed [Spectrum Computing]
Mr. Hair & The Fly [Spectrum Computing]
Mr. Hair & The Fly (alt) [Lee Stevenson]
Nemesis the Warlock (Erbe) [Spectrum Computing]
Oberon 69 [Spectrum Computing]
Rana Rama [Spectrum Computing]
Robot - The Impossible Mission (QAOP keys) [Spectrum Computing]
Robot - The Impossible Mission (ZXKM keys) [Spectrum Computing]
Rubicon (Rucksack Games) [Spectrum Computing]
Rubicon (Rucksack Games, ULA Plus) [Spectrum Computing]
Schizoids (Nuova Newel) [Planeta Sinclair]
Seraphima (English) [ZOSYA entertainment]
Seraphima (Portuguese) [ZOSYA entertainment]
Seraphima (Russian) [ZOSYA entertainment]
Seraphima (Yandex Retro Games Battle v3 competition) [ZOSYA entertainment]
Simon [Spectrum Computing]
Skull & Crossbones (Dro Soft) [Spectrum Computing]
Sky Runner (Z Cobra) [World of Spectrum]
Souls Remaster [Spectrum Computing]
Space Monsters Meet THE HARDY [Spectrum Computing]
Starring Charlie Chaplin (Erbe) [Spectrum Computing]
Starring Charlie Chaplin (Erbe - Serie Leyenda) [Spectrum Computing]
The Hair-Raising Adventures of Mr. Hair [Spectrum Computing]
The Prayer of the Warrior [Spectrum Computing]
The Prayer of the Warrior (demo) [Spectrum Computing]
The World War Simulator: Part One (English) [Spectrum Computing]
The World War Simulator: Part One (Spanish) [Spectrum Computing]
The World War Simulator: Part II (Spanish) [Spectrum Computing]
Tokyo Gang [Spectrum Computing]
Toyota Celica GT Rally (Dro Soft) [Spectrum Computing]
Tus Juegos №3 [Planeta Sinclair]
W.A.R (Erbe) [Spectrum Computing]
Xarax (Potz Blitz) [Spectrum Computing]
Xecutor (Dro Soft) [World of Spectrum]
Yokai Monk (v1.7) [Spectrum Computing]
Yokai Monk (v1.8) [Spectrum Computing]

New software list items marked not working (spectrum_cass.xml)
--------------------------------------------
Cosmic Debris (ZX Data) [Spectrum Computing]
Zorro (Erbe, medium case) [Spectrum Computing]

---
## [Holandsoest/tgstation](https://github.com/Holandsoest/tgstation)@[bed92e193c...](https://github.com/Holandsoest/tgstation/commit/bed92e193ce4a79824fd4fd30a900245dca870ae)
#### Tuesday 2023-12-26 14:22:06 by san7890

Further Prevention of Disposals Qdeletion (#79714)

## About The Pull Request

Fixes the consequences of #79629 - Verdict is still out on what the root
issue is

This has been an issue for the last two years and everything I go
bananas trying to get a consistent reproduction case to figure out the
root issue. After three session of picking, I think it's just a
consequence of certain thing in disposals code sleeping due to
`addtimer()` and whatnot so I'm just throwing in the towel and just
making it so we stop sending atoms to nullspace for no reason.

`target_turf` is typically always a present arg, but regardless we are
guaranteed to get a valid turf to send people to instead of the deleted
mob room. We still `stack_trace()` whenever this happens, so tracking
this issue doesn't change any more than the present status quo- we just
don't keep torturing mobs by sending them to the shadow realm.
## Why It's Good For The Game

One day we'll figure out why we keep getting `null` passed into
`forceMove()` like this but today is not that day. i know turfs
technically can't be deleted but it's just there as a safety since we
nullcheck anyways (which is the whole point of this fix). Let's just
stop screwing with players for the time being

also the code looks much better
## Changelog
:cl:
fix: Safeties in the code have been added to prevent things in disposals
going into nullspace whenever they get ejected from a pipe - you will
just magically spawn at the turf that you were meant to be flung
towards.
/:cl:

---
## [AfreenAsraf/OIBSIP](https://github.com/AfreenAsraf/OIBSIP)@[325758bf81...](https://github.com/AfreenAsraf/OIBSIP/commit/325758bf8161d340f572b72e1d366b5c8329a15c)
#### Tuesday 2023-12-26 14:59:42 by Afreen

Tribute Page code Uploaded

🌟 Proud to share my first project during my internship at Oasis Infobyte! 🚀

🖥️ Created a Tribute Page dedicated to Mother Teresa using HTML and CSS. It was an amazing experience bringing her incredible legacy to life through web design.

🌼 Learning to code while honoring such an inspirational figure was truly special. Grateful for the opportunity to blend creativity and technology in a meaningful way.

🌐 Excited for the journey ahead in web development and eager to keep learning and creating impactful projects!

---
## [an0rak-dev/Avatar](https://github.com/an0rak-dev/Avatar)@[6e6cfd4dce...](https://github.com/an0rak-dev/Avatar/commit/6e6cfd4dce45efc6daadbffbdf17b5bfd2ff17b3)
#### Tuesday 2023-12-26 15:27:06 by Sylvain Nieuwlandt

Add Readme, License and CI.

It's not because I'm working alone on this that I should work as a
savage. I thought it will be fun to integrate the linting steps as
reviews from the github action bot (Yeah, I know it might not sound
fun but it is !).

Got a MetaQuest 3 for Christmas from my insanely crazy wife. Guess
that this project will take another slow down because I'll try to
create a commercial game with it.

Changelog: other

---
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[e7816d96c5...](https://github.com/silencer-pl/cmss13/commit/e7816d96c5d1523337dec081bea0056fbc9189fc)
#### Tuesday 2023-12-26 15:53:07 by forest2001

Almayer AntiTheft measures. (#5100)

STOP STEALING SHIT
# About the pull request
Adds a subtype of reinforced hull for the Almayer that changes between
indestructible hull and normal reinforced wall after hijack.
Uses this wall type around uniform vendors, the separation wall in the
firing range and around engineering storage.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Having the engineering storage looted at round start is just silly
avoidance of the "don't deconstruct the whole ship without a reason"
rule.

# Testing Photographs and Procedure

I have verified that all works as intended, the walls cannot be harmed
prior to hijack, and shutters function as advertised.

# Changelog
:cl:
add: Added a new almayer hull type (heavy reinforced) which is
indestructible by normal means until after hijack collision.
add: Added a new subtype of shutter that automatically opens or closes
depending on security level.
maptweak: Maps both of the above around the engineering storeroom. Also
adds the walls between the firing ranges and around uniform vendors.
maptweak: Manual control button for shutters over engineering storage in
the CEs office.
code: Changes hijack structural changes (walls/windows/windoors/ladders)
to use signals.
/:cl:

---------

Co-authored-by: fira <loyauflorian@gmail.com>

---
## [CDRDecky/f13babylon](https://github.com/CDRDecky/f13babylon)@[667500fde5...](https://github.com/CDRDecky/f13babylon/commit/667500fde5871478747cdd48d7624dab6bb42c8f)
#### Tuesday 2023-12-26 16:47:46 by Stutternov

Fire Delay Fix & Bolt Action Overhaul (#366)

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

So - funny thing. Fire delay NEVER worked properly on this codebase
since the change of the way fire delay worked to a different proc.

I have reversed this and re-adjusted fire delays for guns, at people
clearly were balancing them around the 'fire_delay' proc that wasn't
working. While some guns had 0 fire delay and seemed to function fine,
upon fixing - you realize **"Oh this fires literally as fast as you can
possibly click."**

As such, this is an attempt at balancing gun fire delays. Honestly -
this is a great thing, since I think with these new values (which need
to be tested a bit first) that guns like the Rangemaster and M1 garand
are finally viable alternatives to, say, the DKS. The main issue I see
is guns will be firing faster in some ways across the board due to this
fix so we'll need to slowly fix this via testing to where a gun should
be.

**Bolt actions have also been overhauled.**
Bolt actions are now viable again, as they are better damage, some
bullet speed, and being relatively equal to their automatic
counterparts. Their downside is the fact they are bolt action and, for
some, have limited capacities.

The Remington, for example, now does near equal damage to the DKS but
only has a 5 round capacity, less penetration, and is stripper-clip fed.

The Varmint has also been re-made into a boltaction rifle, effectively
being a 'near equal' to the service rifle albeit bolt-action. It has
some extra pen (only by about 0.1) and extra speed to its bullets,
making it more of a marksman rifle rather than putting bullets down
range better.

**Misc balance adjustments**
Since firedelay needed to be changed, since we have kept changing fire
delays.. despite them not fucking working, guns like the Marksman have
been buffed while others, like the R-91, have had their role
re-evaluated some.

Examples:
- Marksman carbines are now same fire delay as service rifles, but due
to rarity pack some extra damage and penetration in exchange for a bit
more slowdown.
- R-91 lost its damage malice but also its extra pen, instead making it
more of a good automatic weapon.

## Why It's Good For The Game

Either an oversight or a really silly change that broke fire delays on
guns for quite awhile now. Other changes to balance were needed to
balance guns against eachother.

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [X] You tested this on a local server.
- [X] This code did not runtime during testing.
- [X] You documented all of your changes.
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
balance: Re-balances ALL gun fire delays.
fixes: Removed CD_Firedelay in gun proc in exchange for the ACTUALLY
used fire_delay proc
tweak: Moves varmint rifle to being bolt action as well as its variants.
Also buffs them to be competitive while being bolts.
balance: Re-does quite a few guns (Marksman, hunting rifle, remington,
R-91, etc) to make them balance against eachother better due to firerate
changes.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: macha <likeacompleteboss@gmail.com>
Co-authored-by: maaacha <116771811+maaacha@users.noreply.github.com>

---
## [rswarbrick/opentitan](https://github.com/rswarbrick/opentitan)@[fa17526039...](https://github.com/rswarbrick/opentitan/commit/fa17526039d722b482a4c818e0fb5b392180eefc)
#### Tuesday 2023-12-26 16:52:14 by Rupert Swarbrick

[doc] Minor tweak to md sanitisation code

This code replaces \n with a space when populating table cells. A good
idea! But it ended up leaving a double space if the source hjson had a
blank line.

There was also a bit of a mess if we have a newline followed by several
spaces. This turned into two spaces, not one.

The fix is simple: treat any number of newlines, followed by any
number of spaces as a single space. The handwritten code here is just
a 1-line change to md_helpers.py. The rest of the commit is from
regenerating the auto-generated stuff that it builds.

Note that this was annoying to create because we check in the
auto-generated registers.md for pwrmgr in a template file (presumably
manually) and then use that auto-generated file to create the
registers.md in ip_autogen. We should probably stop doing that silly
thing at some point, but my local hack was to apply the fix to the
markdown files with

    util/cmdgen.py -u '**/*.md'

and then manually copy the changed lines to the template file before
re-running

    make -C hw top

This works, but... yuck!

Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

---
## [RagnarokOS/minbase](https://github.com/RagnarokOS/minbase)@[7d80ddb685...](https://github.com/RagnarokOS/minbase/commit/7d80ddb6851a2b1d8878d818318f5febfdacc17e)
#### Tuesday 2023-12-26 18:05:11 by Ian LeCorbeau

sed/rules: fix typo

Note to self: before getting pissed off at autoconf for refusing to work
when some cflags are enabled, make fucking sure there's no typo in them,
idiot.

---
## [xXPawnStarrXx/tgstation](https://github.com/xXPawnStarrXx/tgstation)@[3c2d4f03a8...](https://github.com/xXPawnStarrXx/tgstation/commit/3c2d4f03a8883a416434dcb7e32c334bba3e40ae)
#### Tuesday 2023-12-26 18:06:20 by SSensum

New Quirk! Cyborg Lover! (#80023)

## About The Pull Request

This PR adds a new quirk for people, who want to play as
silicon-friendly crew.

Basic quirk info:
- It costs 2 points.
- It has minor additions to person's mail goodies list (cable coils,
basic cells, etc).
- It has a few simple mood events, when you pet a borg or being
touched/hugged by borg.

## Why It's Good For The Game

I think it is nice to have a chance to play as ~~robo-creep~~ person who
loves borgos.

## Changelog

:cl:
add: Added new quirk: Cyborg Lover!
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [emlos/internautica.online](https://github.com/emlos/internautica.online)@[70e00029f9...](https://github.com/emlos/internautica.online/commit/70e00029f95d93b61d90a4425f4d5af6924b69cf)
#### Tuesday 2023-12-26 19:20:27 by emlos

renaming files works - and BOY was it a BITCH (+ nsfw images as "placeholders")

renaming the file changed the modified date... fucking hell

---
## [langchain-ai/langchain](https://github.com/langchain-ai/langchain)@[d4f45b1421...](https://github.com/langchain-ai/langchain/commit/d4f45b1421ec8b56fe6aeed84f81ca1b3f91383f)
#### Tuesday 2023-12-26 20:30:12 by Sypherd

core(minor): Allow explicit types for ChatMessageHistory adds (#14967)

<!-- Thank you for contributing to LangChain!

Replace this entire comment with:
  - **Description:** a description of the change, 
  - **Issue:** the issue # it fixes (if applicable),
  - **Dependencies:** any dependencies required for this change,
- **Tag maintainer:** for a quicker response, tag the relevant
maintainer (see below),
- **Twitter handle:** we announce bigger features on Twitter. If your PR
gets announced, and you'd like a mention, we'll gladly shout you out!

Please make sure your PR is passing linting and testing before
submitting. Run `make format`, `make lint` and `make test` to check this
locally.

See contribution guidelines for more information on how to write/run
tests, lint, etc:
https://python.langchain.com/docs/contributing/

If you're adding a new integration, please include:
1. a test for the integration, preferably unit tests that do not rely on
network access,
2. an example notebook showing its use. It lives in `docs/extras`
directory.

If no one reviews your PR within a few days, please @-mention one of
@baskaryan, @eyurtsev, @hwchase17.
 -->
## Description
Changes the behavior of `add_user_message` and `add_ai_message` to allow
for messages of those types to be passed in. Currently, if you want to
use the `add_user_message` or `add_ai_message` methods, you have to pass
in a string. For `add_message` on `ChatMessageHistory`, however, you
have to pass a `BaseMessage`. This behavior seems a bit inconsistent.
Personally, I'd love to be able to be explicit that I want to
`add_user_message` and pass in a `HumanMessage` without having to grab
the `content` attribute. This PR allows `add_user_message` to accept
`HumanMessage`s or `str`s and `add_ai_message` to accept `AIMessage`s or
`str`s to add that functionality and ensure backwards compatibility.

## Issue
* None

## Dependencies
* None

## Tag maintainer
@hinthornw
@baskaryan 

## Note
`make test` results in `make: *** No rule to make target 'test'.  Stop.`

---
## [AtotallyRandomGuy/MalduinoW-Payloads](https://github.com/AtotallyRandomGuy/MalduinoW-Payloads)@[8f3da8c31b...](https://github.com/AtotallyRandomGuy/MalduinoW-Payloads/commit/8f3da8c31bb3d29c5fc681fcf2a1b276f45e6897)
#### Tuesday 2023-12-26 21:27:45 by A totally random guy

Create _Windows_WiFi_Exfiltration_Pastebin.txt

Funny script that I spent way too long on, haha. (6 hours of pain 😭) Hopefully this is a functional version, I have so many versions and minor changes.... I'll upload the original one that I know works (and sucks, so unoptimized) later

---
## [StephenCleary/comments.stephencleary.com](https://github.com/StephenCleary/comments.stephencleary.com)@[d6a4147658...](https://github.com/StephenCleary/comments.stephencleary.com/commit/d6a4147658e976521bde3a12516f4b3dac27b90c)
#### Tuesday 2023-12-26 21:42:18 by Comment Bot

(Staticman) Jan: Hi Stephen,
you write "immutable collections can never be as memory-efficient as immutable collections". I've had enough wine tonight that I won't guess which one should be "mutable" and will read the entire articel in the next days ;)
thanks for sharing your thoughts!

https://blog.stephencleary.com/2023/12/the-joy-of-immutable-update-patterns.html#comment-444a8d07-77cc-42ca-bb2b-614835d49187

---
## [crawl/crawl](https://github.com/crawl/crawl)@[645d2ae13f...](https://github.com/crawl/crawl/commit/645d2ae13f9e5acbda4b4080bf64c5fbcc20e7d9)
#### Tuesday 2023-12-26 21:55:12 by regret-index

Spruce up each rune-guarding Pan lords' realm

The bulk of particular enemy decisions for most of the four fixed Pan lords
enemies were made ages ago, before we had nearly so many varied monsters
for almost any branch in general. Since there's been such a massive influx
of new monsters to work with compared to so far back in the past, it'd be
reasonable to further add to the gimmickry the lords themselves already
brandish, rather than focus on plain + common + weak flavour choices for
Pan vaults like occultists, large abominations, or weaker skeletons.

 * Mnoleg's level uses very few very ugly things, abominations, or
   tentacled monstrosities for a lot more protean progenitors and shadow
   demons- the former for more interesting shapechanging, the latter to
   fit the summoning (and since Tartarus lost them). There's far too many
   of the former melee-only types before extended, and Mnoleg lacks much
   for noticeable spawns beyond eyes and cacodemons- these two will both
   help. (Note: Don't use proteans beyond Zot, Zigs, and Mnoleg's floor.
   Zot non-draconians get very limited to no non-Zig drift or bleed to
   keep them distinct and dramatic.)

 * Gloorx Vloq's level loses lorocyproca and demonic crawlers for reapers
   and entropy weavers, while upgrading the skeletons hard. While this
   loses a bit of spectral flavour and demon presence, demonic crawlers
   have no real threat in Pan and there's some interest in removing
   lorocyprocas for more interesting tier-2 designs in the future.
   Meanwhile, entropy weavers still can corrode even extended characters,
   and reapers have a new effect plus aren't much prominent in Tartarus
   anymore. (This is a bit of placeholder future-proofing: if a new
   summoning tier-2 does end up existing, then shadow demons could fit
   here better over some other spawns, like shadow wraith and soul eater
   explicit placements, and those demons can replace Mnoleg's shadow
   demons.)

 * Lom Lobon's level loses arcanists and occultists, as they're pretty
   mundane mortal scholars of magic for extended. Instead, to represent
   more interesting mystics across the Dungeon, there's now small amounts
   of one conjurer from each of the Lair roulette branches- nagaraja,
   merfolk aquamancers, fenstrider witches, and jorogumo. They readily
   match up with the green deaths or blizzard demons already present, and
   while mostly not too extra dangerous at Pan depth they're more
   interesting to see than the prior options.

 * Cerebov, the most infamous and intimidating lord of Pandemonium, loses
   orange demons and crimson imps for pretty rainbow fluttering insects.
   They're definitely not the newly revised, rarely used elsewhere,
   very fire-focused sun moths.

 * Each of the unrand lords vaults places an increasing clump of demonspawn
   related to the lord in question for each rune you have on you when
   entering. Mnoleg gets corrupters (summoning), Gloorx Vloq gets black
   suns (necromancy), Lom Lobon gets blood saints (conjurations), and
   Cerebov gets warmongers (big equipment). There's not any extra in the
   given levels beyond those initial counts, though, so they shouldn't
   make the levels blend together too hard with the rest of Pan.

 * Also, the non-holy guaranteed demonic rune vaults and Mnoleg's realm
   both contain some potions of mutation now, to compensate for when the
   old potion of cure / beneficial mutation shuffling removed the (very
   delayed, unreliable, heavily guarded) potions of cure mutation in the
   holy pan level. Those holies should be revised to be less boring, at
   some point, but for now, it should make those vaults feel more
   worthwhile.

This also updates arenasprint and the chasing-across-Pan / orb run spawns
of the lords for those four new sets, a few new tile choices to reduce the
use of generic D floor and wall tiles, deals with teleport islands in Lom's
realm, and tweaks a varied number of vaults to even out some higher and
lower vault lethality ends. Maybe eventually Pan will be varied enough to
be made yet shorter and extended could be made shorter in general?...

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[e8cf56dcb2...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/e8cf56dcb2553c842abd7adf60a99b33d65ecfbe)
#### Tuesday 2023-12-26 22:20:36 by SkyratBot

[MIRROR] Roundstart AIs are positronic [MDB IGNORE] (#25679)

* Roundstart AIs are positronic (#80355)

## About The Pull Request

If you disassemble an AI which was in the round from the start it will
produce a Positronic Cube rather than an MMI with the brain of that
player's usual human character in it.

Also I made changes to a couple of feedback balloon alerts which would
always trigger a runtime when constructing or deconstructing an AI, this
was because balloon alerts have a small time delay before executing and
we deleted the AI mob or structure after trying to show a balloon alert
on them, so they'd never appear.

## Why It's Good For The Game

Honestly this is _mostly_ about vibes, it has annoyed me since AI
deconstruction was added that Nanotrasen AIs tend to actually be brains
in jars rather than AIs. Now they're artifical.
It does also mean that you can't deconstruct the AI and then put its
brain into a human body, which is similarly mostly bad because of vibes:
If you sign up as an AI I think you should be an AI or a cyborg even
after deconstruction.

It also universally looks really stupid when you deconstruct an AI and
it says it has the brain of Penelope Dreadful in there, like should I
expect them to start RPing as their normal character instead of the AI
they have been playing all round now?

## Changelog

:cl:
balance: Roundstart AIs are now made of positronic cubes, rather than
brains inside MMIs
/:cl:

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@ users.noreply.github.com>

* Roundstart AIs are positronic

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: John Willard <53777086+JohnFulpWillard@ users.noreply.github.com>

---
## [Mjoonlight/MythosOfMoonlight](https://github.com/Mjoonlight/MythosOfMoonlight)@[21f19d6980...](https://github.com/Mjoonlight/MythosOfMoonlight/commit/21f19d69804f26d870882d65e2bae3b1e18cd7ce)
#### Tuesday 2023-12-26 22:40:09 by Ebon1

Just wanna say, a little something.. There is nothing I love more.. Taking my headphones off, fuck that.. But there's this: There's nothing I love more than to, to, to sit down, comfy chair, turn on the PC, fire up a brand new RPG.. Lose myself, just, oh my God, just think of this world, just think of all the planets I can visit. All the immersive things I can get involved with, all the FIGHTS, all the relationships, all the people I meet, all the places I go. I'm so excited to go to there, and you know, I love nothing more, than with all of that laid out in front of me, I love nothing more, THAN TO BE DRAGGED DOWN, EVERY FUCKING CONVIVEABLE OPPROTUNITY, SO YOU CAN FUCKING CURRENT DAY US! "...Sorry, did you wanna get immersed in our world? Yeah, well, guess what? FUCKING PRONOUNS!! FUCKING GENDER AMBIGUITY! FUCKING CURRENT DAY CALIFORNIAN SHIT! 'CAUSE THAT'S ALL WE FUCKIN' KNOW! 'CAUSE WE'RE BORING!! ..WE'RE SO! FUCKING! BORING! ...WE. Can't SEE. Past out own FUCKING REFLECTION. .. THAT'S THE LEVEL OF OUR NARCISISSM HERE." - SAYS THE WESTERN GAME COMPANY. "FUCK YOUR IMMERSION. FUCK YOU HAVING A GOOD TIME. FUCK YOU JUST FALLING INTO A WORLD AND JUST GETTING LOST. OH, NO, NO! CURRENT FUCKING DAY!" ..FUCK OFF! YOU'RE BORING. YOU'RE FUCKING DULL. YOU HAVE NOTHING TO SAY. YOU ARE A ONE HIVEMIND TWATWAFFLE. ..THAT'S ALL YOU FUCKIN' ARE! And you wonder why people are getting so FUCKING SICK! AND TIRED! YOU TAKE EVERYTHING WE LOVE. ALL OUR IMMERSIONS. ALL OUR FANTASIES. ALL OUR ESCAPISM. AND YOU JUST CAN'T HELP SHOVEL YOUR DOGSHIT! FUCKING CRAP! IDEOLOGY. INTO EVERYTHING. EVERY SINGLE SOLITARY FUCKING THING.

---
## [sosga/dungeon-crawl-stone-soup](https://github.com/sosga/dungeon-crawl-stone-soup)@[866d48a76e...](https://github.com/sosga/dungeon-crawl-stone-soup/commit/866d48a76e53198ac7dee08fed80d99590233fe9)
#### Tuesday 2023-12-26 22:45:06 by Nicholas Feinberg

Add gems

When I added Meteoran (1352289c90d, based on Hellmonk's ad05b8d819def),
I wanted to give players a fun way to engage with time pressure. When I
play, I really enjoy the feeling of exploring on less than full HP and
making choices about which areas to explore. (Full clearing everything
carefully can be fun, too, but variety is the spice of life!) I'd hoped
to find a way to bring that playstyle to the wider playerbase, with time
limits that are more defined and achievable than the harder and fuzzier
goal of 'compete for a high score'.

Some people, including myself, really liked Meteorans! But a large
number of players, probably the majority, found them stressful and unfun.
That isn't the end of the world - I'd much rather have a species which
20% of players love and 80% hate than one which 99% of players don't care
about one way or another. But I'd also hope that we could do better.

Gems are intended to be an alternate approach to the 'time pressure'
playstyle. They're a new type of collectible item, appearing at the end
of DOLESAPNMVCWUZ - basically, all the non-portal, non-temple branches of
a 3-rune game. Each gem has an associated time limit, which ticks down
while the player is in their associated branch. When that time runs out,
regardless of whether the player has gotten the gem yet or not, Zot rudely
smashes the gem into ten thousand pieces.

The intention is to allow several different ways to interact with gems:
- Ignore them, or not even realize they exist. This is intended to be the
  primary/default interaction.
- Dive to grab gems, but not bother trying to keep Zot from smashing them.
  This is a 'lightweight' speedrunning playstyle, a bit like the Speed
  Demon I tournament banner.
- Keep one or more gems intact by only exploring part of a branch, perhaps
  opting to 'go for it' when your character is feeling especially strong.
- Try to grab all gems and retrieve them all intact. This is roughly
  equivalent to the old Meteoran playstyle.

Gems have absolutely no mechanical use within the game. They offer a very
minor score bonus (10k points each), as a bonus for new players who look
at scores for unwon games, but shouldn't affect normal play or speedrunning
in any way.

Getting the Orb of Zot shuts the timer off. One could skip branches, get
the orb, and then clear branches while holding the Orb to get gems with no
time limit... but orbrunning is its own form of time pressure, and I'm
skeptical this would be easier than playing 'normally'. :)

Time limits are currently set on a per-branch basis. Lair, Vaults, and
Depths have longer time limits than they did for Meteoran, to allow for
large levels and travel time, while Slime and Zot are shorter. However, I
would be startled if these time limits stuck - I personally suspect most
of them are too tight for species which *aren't* as strong as Meteoran.
We can experiment.

The good gem tiles are by Sastreii, the bad ones are by me. :)
Credit also to ellpitic for helping to set me down this path.

---
## [0xd34df00d/leechcraft](https://github.com/0xd34df00d/leechcraft)@[ace4bf0645...](https://github.com/0xd34df00d/leechcraft/commit/ace4bf06451900061267b8b2f449096755d18f87)
#### Tuesday 2023-12-26 23:17:41 by 0xd34df00d

[Util] Abort `Left`-y `Either` via a special exception

The previous approach of  `co_await`ing on promise's `final_suspend()`
(that is, `FinalSuspender` of the `Task`) had lots of problems and
didn't really work.

Firstly, `FinalSuspender::await_suspend()` never called the calling
coroutine, so the sub-`Task` spawned by `EitherAwaiter::await_suspend()`
didn't ever got control back from the `co_await`.
And that is the correct behavior, since `FinalSuspender` is supposed to
be, well, final, and the corresponding coroutine is destroyed right
after anyway.

Sure, this could have been worked around one way or another (for
example, by checking if the caller's coroutine address is the same as
the `FinalSuspender`'s coroutine address, and resuming the caller only
if they differ). But, the next problem then is that `handle->destroy()`
in `EitherAwaiter` (which, remember, never executed before) will then
get invoked and will destroy the original coroutine. That's sort of what
we want anyway, but the problem is that, for example, the `Task`
representing the coroutine might well be alive, and there's no way of
knowing that the coroutine died (and if there was, getting the result
of the coroutine out of the dead promise would be funny anyway).

All of this is avoided if an exception is thrown inside the coroutine.
Then the normal exception handling mechanism in coroutines kicks in and
does exactly what we want. The only remaining thing is to check the
exception type in `GetTaskResult()` and ignore that particular exception
type.

So, yeah, that's sorta exceptions for control flow. But it is what it
is.

---
## [maxwwatson/TOP-etch-a-sketch](https://github.com/maxwwatson/TOP-etch-a-sketch)@[982f434838...](https://github.com/maxwwatson/TOP-etch-a-sketch/commit/982f434838a6f356b575cf91ab2fabd2a11f92a0)
#### Tuesday 2023-12-26 23:23:35 by Max

Finished Etch a sketch - draw, hover, erase, Etc

Fuck me dead I see the good and bad things with how these exercises are
laid out. Breaking things down into super small problems is fantastic
for actually figuring out how to code bit by bit as you edge towards
the solution, however having to refractor and change everything you
did and change all the functions is a pain and a half.
THAT BEING SAID - I learned a lot about how important a few different
things are:
- Micro-commits would have been good to do after each feature
- Writing out how my algorithm and how functions loop through
eachother in full pseudo code would have preventing having to really
get myself up to speed when I have to go back.
- More forethought before writing this all out would make it easier
to think through it all.

---
## [steve6472/StevesFunnyLibrary](https://github.com/steve6472/StevesFunnyLibrary)@[7459f37123...](https://github.com/steve6472/StevesFunnyLibrary/commit/7459f37123bea7acfb2b24adfabcefa7a9850f07)
#### Tuesday 2023-12-26 23:27:12 by steve6472

Big boi update boiiii

- Whole ass bingo
- A minigame config system thingie
- AnvilGUI support 'cause fuck you
- a bunch of stuff idk lol

Took 42 hours 9 minutes

---
## [yrdzrfxndfvh/crawl](https://github.com/yrdzrfxndfvh/crawl)@[8f7eaaa2f0...](https://github.com/yrdzrfxndfvh/crawl/commit/8f7eaaa2f0678ffbf35011348680be2dee9ef664)
#### Tuesday 2023-12-26 23:36:21 by DracoOmega

Merge Poison Magic and Transmutations into a single school: Alchemy

When forms were removed from Transmutations to create
talismans/shapeshifting, the Transmutations school was left in a slightly
awkward state. It still contained multiple strong and useful spells (eg:
Irradiate and Yara's) but was a little thin on the whole, especially at
lower levels, and lacked natural inroads. And Poison Magic has long had
issues with being overly narrow in thematic scope compared to other
schools, as well as lacking exciting lategame spells.

This merger attempts to improve both issues at once and open up more
interesting future design space by combining the two schools into one:
Alchemy. This makes several higher level transmutations spells more natural
to access, give the Venom Mage start (now Alchemist) more lategame things
to look forward to, and potentially allows for the design of more varied
means of doing damage than poison.

All spells that were either Transmutations or Poison are now Alchemy,
with the following notes:
 -Ignite Poison moved to level 4 since it's now 2 schools instead of 3.
 -Eringya's Noxious Bog was left at level 6, despite becoming single-school
  since it's already widely considered unappealing and this might help it.
 -Sting became Conjurations/Alchemy.
 -Wereblood is slated to be rethemed and moved to Necromancy, but isn't yet.

Most species aptitudes for Transmutations and Poison Magic were already the
same. Cases where that was not the case are listed below.

--------------------------------
Transmutation/Poison -> Alchemy

Demonspawn: -1/0 -> 0
Felid: 1/-1 -> -1
Formicid: 1/3 -> 3
Gargoyle: -2/0 -> -2
Ghoul: -1/0 -> -1
Hill Orc: -3/-1 -> -2
Merfolk: 3/1 -> 3
Minotaur -2/-3 -> -3
Naga: 0/3 -> 2
Octopode: 0/2 -> 1
Spriggan: 3/0 -> 1
Tengu: -2/0 -> -1
Vampire: 1/-1 -> 1
--------------------------------

This vaguely averages apts, with a slight bias for the original poison
skill (and some personal subjective opinion here and there). Formicids and
Merfolk both keep their +3 poison apt - the former because it can easily
handle the buff, the latter because it's just too good to let merfolk make
their own bogs to swim in. Felid apts are in line with their other
offensive-focused magic skills, Gargoyles inflexible nature makes them
less adept at inducing change in others, and Vampires have traditional
thematics around transformation that makes a +1 feel appropriate to me.

Ashenzari's Curse of Beguiling loses Conjurations, and the old Curse of
Alchemy is renamed Curse of Sorcery (Conjurations + Alchemy).

Alchemy miscasts inflict the poison status on the player. (I kind of
prefer the idea of them inflicting corrosion instead, though no player
Alchemy spell can yet do this, so I'm not sure how people would feel).
Messages are provisional, but frankly the miscast system in general has
issues with the fact that messages cannot check player properties (cf:
ghouls getting messages about how they violently convulse in pain, then
take 0 damage) and could use separate work.

The Plutonium Sword is decoupled from transmutation miscasts (which no
longer exist). I have also added back a vague approximation of the
direct damage they used to inflict before the big miscast simplification
of a couple years back.

Save upgrading will grant players Alchemy skill equivalent to the sum of
old Poison and Transmutation skills.

Alchemy randbook words are a partial merger of old Poison and
Transmutation book words, with heavy cutting, curating, and addition of
things. (I tried to prune things directly associated with shapeshifting,
as well as poison words that seemed too close to disease and putrescence
in a 'gross' sense - instead trying to lean into a more academic vibe for
such things. Also added a decent handful of specifically-alchemical
references.)

Still slightly awkward that it can use poison words for a book containing
no spells that poison, but probably no worse than randbooks often are.

(Gloorx can stay as a high-level alchemist. Hot new DCSS lore!)

---
## [yrdzrfxndfvh/crawl](https://github.com/yrdzrfxndfvh/crawl)@[cae00c0fb1...](https://github.com/yrdzrfxndfvh/crawl/commit/cae00c0fb1febd50125cb22469d0abc9ffebdaa7)
#### Tuesday 2023-12-26 23:36:21 by DracoOmega

Shuffle spellbooks a bunch

The book of Changes was incredibly sad (and nonsensically named) with just
Sting and Irradiate, and attempting to touch this up caused a chain
reaction (which hopefully still improves the status quo).

Unrestrained Analects loses Ignition and gains Ozocubu's Refrigeration.

Book of Battle returns, with Ozocubu's Armour, Manifold Assault, and
Fugue of the Fallen.

Book of Changes renamed to Book of Spontaneous Combustion, containing
Inner Flame, Irradiate, and Ignition.

Book of Alchemy renamed to the book of Transmutation (but contains the
same spells as before).

Book of Minor Magic lost Mephitic Cloud and gained Blink.

Book of the Senses gained Mephitic Cloud.

Book of Blood gained Call Imp (since apparently there was only one book
that had a copy of it)

Book of Cantrips gains Sting.

Book of Death loses Fugue of the Fallen.

Book of Misfortune loses Inner Flame to gain Jinxbite.

Book of Danerous Friends loses Jinxbite.

Ozocubu's Autobiography and the Inescapable Atlas were cut. The latter's
description didn't really make any flavor sense with its spell set of Blink
and Manifold Assault. It's a shame to lose two of the best book
descriptions, so I adapted most of the former for Book of Battle.

Trismegistus Codex loses the joke about all its spells having 3 schools,
but the only other 3 school spell remaining is Mephitic Cloud which already
shares another book with Freezing Cloud. Alas.

---
## [yrdzrfxndfvh/crawl](https://github.com/yrdzrfxndfvh/crawl)@[614289c723...](https://github.com/yrdzrfxndfvh/crawl/commit/614289c72386821faeecdd77f07cdc0aac8e5333)
#### Tuesday 2023-12-26 23:36:21 by DracoOmega

Wereblood -> Fugue of the Fallen (level 3 Necromancy)

Wereblood has had somewhat weird thematics ever since Shapeshifting took
over all of the 'transform self' effects from Transmutations. Necromancy,
on the other hand, is a natural fit for a spell that is powered by killing
things.

This has the following mechanical changes over current Wereblood:
 -The healing effect is removed
 -Ally kills now boost the effect (but allies themselves do not benefit
  from it in any way)
 -Max stacks reduced to 7 instead of 9
 -At maximum stacks, successful hits will inflict minor pain damage to all
  adjacent targets to the one you attacked. A little bonus for the tricky
  task of maxing it!
 -Moved to level 3

I haven't put this in the necromancy starter book. Wereblood was never great
at low levels, since you usually can't sustain fights long enough to build
it and struggle to kill already. I think there's no way a necromancy wants
to use their mp on this instead of vampiric draining, and it's more
interesting if the spell is intended for later use. Also: this gives players
more incentive to splash necromancy on a hybrid that doesn't involve allies!

To avoid the player needing to worry about whether any individual monster
they kill has a 'soul' or whatever, the spell is themed as using fresh
death to draw in the spirits of the long-dead that already linger everywhere
in the dungeon (I mean, there's enough corpses in every inch of the dungeon
that BVC works, right? :P)

---
## [Stake2/Websites](https://github.com/Stake2/Websites)@[e3a33826c0...](https://github.com/Stake2/Websites/commit/e3a33826c02612250222d9b66cf9c26dc40e5a79)
#### Tuesday 2023-12-26 23:37:29 by Stake2

Updated websites:
Stake2
My Little Pony: Friendship Is Magic, to update the website image
Watch History, to update the website image
New World
SpaceLiving
The Life of Littletato
The Secret of the Crystals
The Story of the Bulkan Siblings
2018
2019
2020
2021
2022
2023

I updated all year websites to update their website images.

---
## [ma44/NCRvL-OWB](https://github.com/ma44/NCRvL-OWB)@[7f05045a78...](https://github.com/ma44/NCRvL-OWB/commit/7f05045a784789620726c8a095b918bab8816b2e)
#### Tuesday 2023-12-26 23:52:53 by Micheal Fuller

Work In Progress Next Update

Fixed:
Fixed "Wet Ammo Stowage" in Vehicle tree granting 50% defense instead of 5%.

General:
Max Mills and Civs that can be built in any given state raised from 20 to 30 so you are no longer restricted in where they can be built.

Tech:
Mechanized Forces Conventional Warfare Doctrine no longer removes Entrenchment. Combined Arms Refined Warfare Doctrine Power Armor Support 5% Soft and Hard Attack increased to 10%. Human Commanders Automated Warfare Doctrine now grants 2% Initiative to CNC Robots. Field Maintenance Automated Warfare Doctrine granted Maintence Support 15% Trickleback, -15% EXP loss, 10% Intiative, and 2 Recon. The Flesh is Weak Automated Warfare Doctrine granted 15% Hard Attack bonus to Robots and 10% Breakthrough and Soft Attack raised to 15%. Refined Construction Automated Warfare Doctrine 10% Defense and Hardness increased to 15%. Automated Distribution Automated Warfare Doctrine granted 10% Factory Output bonus. Rushed Production Doctrine Granted 0.2 Combat Width reduction to Combat Robots and -1% Reliability penalty removed. Self-Replicating Machinery granted 5% Conscritpion Bonus. Networked AI Automated Warfare granted 10% Max Planning bonus and Planning Speed increased to 10%. Internal Replicators Automated Warfare Doctrine Hardness and Armor increased to 15% and granted 5% Factory Output. War Games Automated Warfare CNC Robots Soft and Hard Attack bonus increased to 15%. Human Commanders Automated Warfare Doctrine Soft and Hard Attack bonus increased from 10% to 15% and Planning Speed bonus increased from 10% to 20%. Age of the Machine Automated Warfare Doctrine CNC Robots Soft and Hard Attack bonus increased to 15%. Combat Robots main stats increased by 2 and rounded up if at the decimal point. K9 Integration removed from Motorized Enforcers. Removed Warforms Technology From Implant Tree. Dog Integration no longer affects Motorized Enforcers, but now affects Sentinel Power Armor.

Los Banditos de Baja:
Added Sophisticated Naval Technology access to the "Gulf of California" focus.

Two Sun:
Two Sun's Capital now starts with 12 Slots instead of 10 and 3 more Civilian Factories. Reduced Focus Times for Scavenging Programs, Technological Excavation, Taking Inventory, Industrial Development, Build Water Pumps in Nogales, Develop Farming in Nogales, Tombstone Garages, Hilltop Garages, Ideas are Easy, Implementation is Hard, Hiring a Real Bastard, New Products for New Buyers, Speed is the Heart of Battle, The Great Game, and Thunderstruck from 30 to 15 days each. The focuses Incorporating the Ranches and Tohono's Integration now cores Cowboy Country and Tohono instead of granting a Coring Bonus. Removed the Gente War Goal path. Weapons to Surpass Metal Gears focus now grants 1K Gauss Rifles instead of 400. Joined Arms Production focus now grants 4 Mills and Building Slots instead of 2. Energy for the Suns focus now grants 2 Power Plants of Planta Grupo and Gente City instead of Dockyards. New Industry focus now grants 6 Civs and Building Slots on Hilltop and Oputo instead of 6 on just Hilltop. Our Own Design focus now also grants Intermediate Support Tech to Two Sun. The Sanora Cohort focus now grants Chariots Technology. Dreams Fufilled focus no longer removes the Infrastructure Construction bonus. Under the Protection of the Bull Focus now frees Two Sun from Puppet Status to Legion. Ceasar's Rule starting 7 Day focus changed to be a more interesting choice and techs that were previously there have been moved later in the tree.

Legion:
Legion now starts with Intermediate Naval Technology. Removed Canine Integration from Vulpes Focuses. Ceasar's The Principate focus now grants Sophisticated Naval Technology. Ceasar's Honeyed Words focus now grants Cores on all of the NCR if he controls Boneyard. Ceasar's Aequitas focus now grants 15% Spec Ops Capacity Multiplier and 20 Minimum Capacity. Vulpes's The Harvesters focus now grants 10% Spec Ops Capacity Multiplier. Lanius Focus Tree Army EXP requirements cut in half.

NCR:
Hayes's For All Tommorows Focus now grants cores on all of the Legion if he owns Quartz Site. Kimball's The Baja Homestead Act focus now grants 4 Building Slots, 2 Infrastructure, 2 Civs on every Baja State instead of 2 Building Slots, 1 Infrastructure, 1 Civs. Changed all Hayes first election focuses from 30 days to 15 each. Reduced NCR Rapid's Navy tree from 30 Days to 15 Days each. NCR's Look to the West focus now grants Sophisticated Naval Technology. Removed Shi Wargoals tree, instead just invites them. Rangers Lead the Way Spirits granted 10% Special Forces Capacity Multiplier for first spirit and 20% for the second.

Arroyo:
Granted Spec Ops Cap 40 + 5% from game start.

Mojave Territories:
Granted Spec Ops Cap 40 + 5% from game start that upgrades to 60 + 10% later in the tree after the Dam War.

Shale:
Added 1 Starting Research Slot.

---

