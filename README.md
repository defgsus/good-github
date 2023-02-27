## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-26](docs/good-messages/2023/2023-02-26.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,842,209 were push events containing 2,572,561 commit messages that amount to 147,817,536 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 41 messages:


## [net-snmp/net-snmp](https://github.com/net-snmp/net-snmp)@[b0f82764f4...](https://github.com/net-snmp/net-snmp/commit/b0f82764f4ab0b8c6d93378a9b5c2927f2b09509)
#### Sunday 2023-02-26 01:15:44 by Bart Van Assche

Spelling: Change 'demon' into 'daemon'

From https://en.wikipedia.org/wiki/Daemon_(computing):

Many people equate the word "daemon" with the word "demon", implying some
kind of satanic connection between UNIX and the underworld. This is an
egregious misunderstanding. "Daemon" is actually a much older form of
"demon"; daemons have no particular bias towards good or evil, but rather
serve to help define a person's character or personality. The ancient
Greeks' concept of a "personal daemon" was similar to the modern concept of
a "guardian angel"-eudaemonia is the state of being helped or protected by a
kindly spirit. As a rule, UNIX systems seem to be infested with both daemons
and demons.

---
## [Dorumin/nushell](https://github.com/Dorumin/nushell)@[378a3ae05f...](https://github.com/Dorumin/nushell/commit/378a3ae05f5459a64f97af3781d4336c35652db4)
#### Sunday 2023-02-26 01:54:36 by Kovacsics Robert

Use `with-env` to avoid calling external command on invalid command (#8209)

# Description

My terminal emulator happens to be called `st`
(https://st.suckless.org/) which breaks these tests for me

_(Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.)_

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes

_(List of all changes that impact the user experience here. This helps
us keep track of breaking changes.)_

# Tests + Formatting

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [Wollywoger/MapleStationCode](https://github.com/Wollywoger/MapleStationCode)@[22a76a88c1...](https://github.com/Wollywoger/MapleStationCode/commit/22a76a88c1d309b8ddd5073118f956154b303766)
#### Sunday 2023-02-26 02:18:30 by Time-Green

External Organ Rework: new bodypart_overlay system (#72734)

Bodypart overlays are now drawn by the new /datum/bodypart_overlay
datum.

External organs no longer draw anything and instead add a special
/datum/bodypart_overlay/mutant to the bodypart, which draws everything

Makes it way easier to add custom overlays to limbs, since the whole
system is now modularized and external organs are just one
implementation of it

I haven't moved anything but external organs to this new system, I'll
move eyes, bodymarkings, hair, lipstick etc to this later

New pipeline is as follows:
- External organ added to limb
- External organ adds /datum/bodypart_overlay/mutant to limb to
bodypart_overlays
- Limb updates its icon, looks for all /datum/bodypart_overlay in
bodypart_overlays
- Very cool new overlay on your limb!

closes #71820

:cl:
refactor: External organs have been near-completely refactored.
admin: Admin-spawned external organs will load with a random icon and
color
fix: fixes angel wings not working for non-humans (it was so fucking
broken)
fix: fixes external organs being invisible if they werent initialized
with a human
/:cl:

External organs are cool but are pretty limited in some ways. Making
stuff like synthetic organs is kinda fucked. I tried and it was dogshit.
Now you can just give an icon state and icon and you're good (using
/datum/bodypart_accessory/simple)

Stuff like eyes, cat ears and hair seem like good choices for extorgans,
but don't quite work for it because their icons work a lot differently.
This solves for it completely since any organ (or object or whatever)
can add it's own icon to a bodypart.

Want to add an iron plate to someones head? Go ahead. Want a heart to
stick out of someones chest? No problem.

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[dc359175ba...](https://github.com/k21971/EvilHack/commit/dc359175bafa41a0174fbb4a9e97bc70bbea4442)
#### Sunday 2023-02-26 02:35:04 by k21971

Gnomes hate eggs.

By player request, inspired from the 'Oz books' by author L. Frank Baum
- gnomes hate eggs. SporkHack has it so if you throw eggs and a
gnomes ees it, they become scared and flee. Decided to do my own thing
with it for EvilHack, and aosdict happened to have some old code laying
around that was inspired by the same; that's incorporated here. Here's
what happens:

* If you have regular eggs in open inventory and gnomes are nearby and
can see you, there's a chance they'll become agitated and flee
* If you're a gnome and eat a regular egg, you'll take 4d10 worth of
damage, and if you survive, it'll make you sick/vomitting
* If you throw a regular egg at a gnome and it hits, they'll take 4d5
worth of damage, and it will cause them to shout and flee, waking nearby
monsters

There are some potential to-do's here, such as should special
consideration be taken for gnomish priests/shopkeepers if they see you
carrying eggs? Should intelligent monsters want to collect regular eggs
to throw at you if you're a gnome? Should gnomes avoid regular eggs
altogether, and not even step over them? And probably a couple more I'm
not thinking of right now.

Co-authored-by: copperwater <copperwater@users.noreply.github.com>

---
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[966650d9ec...](https://github.com/clintjedwards/gofer/commit/966650d9ec00b3d468385f50845c3583d1fb21cf)
#### Sunday 2023-02-26 02:54:16 by Clint J Edwards

feat: Pipelines are now versioned

In order to eventually have canary-able deployments in Gofer we must
first support versioned pipelines.

This allows us to:
* Have a good target in which to roll back and forward.
* Understand what we are gaining and losing on each change.
* Track each update as it happens.

This is not easy though as pipelines have parts which are easy to version
(namely the config) and parts which are much harder to version (how do
we handle the cutting over of triggers?).

Because of this nuance, we've had to redesign a lot of earlier
assumptions for how Gofer models worked. This was a major refactor and
since I was here I made a few other large sweeping changes.

* Full storage package refactor: The storage layer was hard to use,
brittle, and inflexible. I've refactored it, leaning a bit more on
sqlx and going back to basics. I tried to make the storage package
work in the past by keeping the domain models to a minimum. I've since
learned this does not work once things become reasonably complicated. One
of the main refactors to the storage package is the introduction of
dedicated storage models. This means that I have to write a bunch of
boilerplate code to switch from in-memory models to the storage ones,
but the looser coupling is worth it. More storage refactors coming
as I learn what works at large scale and what doesn't.
https://github.com/go-jet/jet looks interesting.

* Removal of Triggers as Pipeline configuration: I desparately wanted
to have pipeline configurations encompass everything a pipeline would
have to offer, so that it was easy to look at a config and know exactly
what was going on in a particular pipeline. Triggers were a pain in the
ass though. Triggers unfortunately occupy a very special place in Gofer's
archetecture. Without triggers nothing really gets done. And so allowing
the user to apply all the same functionality to triggers as they would
with any other deployment was short-sighted. Triggers don't make a lot
of sense as a canary deployment. Triggers aren't ephemeral, they are
either on or their off. No in-between.

Instead Triggers can now be added to your pipeline via the command line.
This way trigger subscriptions aren't held down by the paradigms of
configuration change.

* Pipelines are now versioned: Not only have we added versions to pipelines,
but they now have deployments and configurations and metadata and a lot
of smaller loosely coupled parts so that they aren't a huge data monolith.
This means a lot of breaking changes for outward (and inward for that matter)
apis.

* Renamed triggers to extensions: We've moved triggers to be their
own thing and gave them extra powers to support pipelines. They no
longer only have to trigger pipeline but can do things like
notify the user.

* Just lots of general breakages everywhere: Pretty much a large percentage
of things just aren't the same anymore.

---
## [RatFromTheJungle/Skyrat-tg](https://github.com/RatFromTheJungle/Skyrat-tg)@[406b6870bd...](https://github.com/RatFromTheJungle/Skyrat-tg/commit/406b6870bd28dd78e65e59787d8c54c776078019)
#### Sunday 2023-02-26 03:02:35 by SkyratBot

[MIRROR] adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths [MDB IGNORE] (#18785)

* adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths (#72736)

repaths a lot of gloves off /color because they were incredibly stupid
firefighter gear has gotten an update (it doesnt cover hands anymore
though, you need something else)
firefighter helmets no longer hide your mask or glasses

![image](https://user-images.githubusercontent.com/23585223/212542599-c004d0e4-c141-40b4-a1bb-c838f9893c4b.png)
fixed engine goggles starting with darkness vision
to the atmos lockers adds atmospheric gloves, a pair of thick (chunky
fingers) gloves that are fireproof and fire protective, slightly shock
resistant and let you fireman carry people faster.
atmospheric firefighter helmets now are a subtype of welding hardhats,
you can enable a welding visor.
welding hardhats change mode with right click instead of altclick

im not a good spriter but i think this resprite makes them fit nicer
with other engi equipment
lets me firefighter rp

:cl:
add: Atmospheric Gloves, thick gloves that are fully fireproof and fire
protective and let you fireman carry people faster.
fix: fixes engine goggles starting with darkness vision
qol: firefighter helmets can now enable a welding visor
qol: welding hardhats change mode with right click instead of altclick
balance: firesuits no longer protect your hands
/:cl:

* Makes shit compile

* Updates the digi and snouted stuff to match the new sprites (thanks Halcyon!)

* Fixes a whole ton more issues that popped up

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [DexterDude/cmss13](https://github.com/DexterDude/cmss13)@[8f1ee35f1d...](https://github.com/DexterDude/cmss13/commit/8f1ee35f1de18e295fa29e4536ad00431e7f0d76)
#### Sunday 2023-02-26 03:21:23 by carlarctg

Refactored weed crossing to utilize signals and list data. (#1960)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Refactored weed slowdown to work based on a signal sent to the recipient
carrying list data.

Added a variable for weed slowdown multiplier to species. Human Heroes
have 0.5 weed slowdown because haha funny. Transferred Yautja's weed
immunity to species.

Added an admin-only example item 'hiking boots' that halve weed
slowdown.

Removed a useless define for XVX.

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
refactor: Refactored weed slowdown to work based on a signal sent to the
recipient carrying list data.
code: Added a variable for weed slowdown multiplier to species. Human
Heroes have 0.5 weed slowdown because haha funny. Transferred Yautja's
weed immunity to species.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [awakened1712/android_kernel_samsung_exynos9820](https://github.com/awakened1712/android_kernel_samsung_exynos9820)@[4f91916fdf...](https://github.com/awakened1712/android_kernel_samsung_exynos9820/commit/4f91916fdf743c7fd50cb085ef5c4fecce552196)
#### Sunday 2023-02-26 03:32:13 by Peter Zijlstra

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
Signed-off-by: John Vincent <git@tenseventyseven.cf>

---
## [daywalk3r666/Kvaesitso](https://github.com/daywalk3r666/Kvaesitso)@[c664f2e777...](https://github.com/daywalk3r666/Kvaesitso/commit/c664f2e777df4226ae47988fd95d250f126f12af)
#### Sunday 2023-02-26 04:37:00 by MM20

Fuck you Android studio, please fix your goddamn focus, I wanted to type into the terminal, not the editor

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[3978cfe70f...](https://github.com/carlarctg/cmss13/commit/3978cfe70f7e32331243e8b05738067b6101ebe6)
#### Sunday 2023-02-26 04:51:24 by spartanbobby

LV522: Chances Changes (#2695)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR makes numerous Changes to LV522 as well as adds more props to
ease of mapper use

# Explain why it's good for the game

The areas changes and reasons why as are follows
**SW Reactor:** Entirely removed and replaced with a much more open
containers area for the xenos to build up and defend, this area is now
the linchpin of the map as marines have to push though it to get to
other flanks inside the reactor meaning the xeno players should now have
a much better understanding of where they need to defend instead of
prior problems with the map of them being hard flanked and losing at
12:26

**LZ1:** LZ1 was moved slightly more north in an attempt to remove some
deadspace and make the path from the front to the FOB slightly less
long, more LZ1 tunnels and ways inside the FOB were added for xeno
flankers aswell as LZ1 being locked down until the marines push a button
to open it up

**Colony admin** A sensor tower was added to colony admin to encourage
marines to go over there and investigate, along with a lockdown to the
area being added

**LZ3** a FORECON prop LZ housing the Tornado was re-added after being
removed in an attempt to downsize the map, basically I figured out where
I could put it

**props:** Alot of instanced props for the map were made into actual
items such as, bedrolls and folded bedrolls, FORECON dogtags, used
flares, jerry cans, used bandages and some weird gameboy thing

Sprites: https://i.imgur.com/avi2fUo.png
FORECON was always made to have a patch it was one of those things I
wanted but never got, luckily while making this PR I was able to look
into it and get the old sprite from tri to finish up myself with onmobs

FORECON Balance changes: The M39 being in the primary weapon slot is
more of a "fuck you" to people playing the roll than just unlucky RNG
that is workaround able moving it to the secondary pool lets the FORECON
play around with better weapons to survive with and the M39 extended
magazines means it's one of the only weapons FORECON spawn with that has
a decent amount of ammo

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:SpartanBobby
add: Made some instanced props on LV522 actual items for mapper ease of
use
maptweak: tweaked LV522, removing the SW reactor and replacing it with a
much more open container area once used as the FORECONS FOB
maptweak: tweaked LZ1 on LV522 making it start locked down and be
slightly more north along with some extra tunnels and flanking routes
for the xenos
maptweak: LV522, added a lockdown and moved the sensor tower to colony
admin
maptweak: re-added the prop LZ in the NE of the colony
maptweak: redistributed LV522 mining metal spawns to be more spread out
maptweak: removed building color outlines from LV522 that were there to
help with navigation during Test merges since the map has been out for
long enough for the majority to properly navigate it
tweak: M39 removed from FORECON primary weapon pool and added to
secondary weapon pool along with extended mags instead of normal
add: Added FORECON Patches for the survivors on LV522 sprites made by
Triiodine while onmobs were made by myself with help from Kugamo
fix: examing a uniform no longer tells you that it has "an
USCM/FORECON/Falling falcons patch" instead it says "a patch"
add: updated the USCM FORECON uniform name and description 
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Nanu308 <59782240+Nanu308@users.noreply.github.com>

---
## [nilopmsft/cosmos-trading-demo](https://github.com/nilopmsft/cosmos-trading-demo)@[7f1bf90fff...](https://github.com/nilopmsft/cosmos-trading-demo/commit/7f1bf90fff25e1eabc5a5fb8bf273ff84e4be7cb)
#### Sunday 2023-02-26 05:20:52 by Cameron Battagler

Portfolio charts working, realized we can't do candlesticks because we don't have historical data.... How do we want to do that @nilopmsft ? Do we change our stock price feed method to have historical data? That wouldn't be hard to do, just a quick edit on the stream analytics job... But does it make sense to do it? Should buy/sell actions by users influence the stock price? That would be cool but is it worth the work? I feel like I ask this question a lot "It would be cool but is it worth it?" I want flaming hoops...but gosh, getting the hoops to flame is obnoxious, let alone the training to get through the damn hoops.

Either way, we probably should start tracking historical market data either way just to be able to have the ever important candlesticks.

Did you ever get the new cosmos collection deployed? I don't remember if I saw it in there, but I haven't been looking, I have been staring at echarts...ugh. Either way. The whole point of this commit message was to say I have the charts working, but the charts are pointless because they are lines and not candlesticks.

---
## [AswaleTanmay/100Days-of-code](https://github.com/AswaleTanmay/100Days-of-code)@[a181f464cd...](https://github.com/AswaleTanmay/100Days-of-code/commit/a181f464cd0e25c7ed74bad83ed2887c5c6a11fb)
#### Sunday 2023-02-26 07:01:39 by Tanmay Aswale

Day94

Kekocity's population consist of N gnomes numbered with unique ids from 1 to N. As they are very joyful gnomes, they usually send jokes to their friends right after they get any (even if they knew it before) via their social network named as Mybeard. Mybeard became popular in the city because of message auto-deletion. It takes exactly one minute to read and resend joke to mates.

Mayor of Kekocity, Mr. Shaikhinidin, is interested in understanding how the jokes are spread. He gives you database of Mybeard social network, and wants you to answer some queries on it.

You will be given a list of friends for every gnome and M queries of the following type: Who will receive a message with joke after exactly K minutes, if the creator of joke was gnome with id x?

---
## [paimonchan/odoo](https://github.com/paimonchan/odoo)@[639cfc76ba...](https://github.com/paimonchan/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Sunday 2023-02-26 07:46:22 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#109812

Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [dsmith328/LC13Master](https://github.com/dsmith328/LC13Master)@[8f4f77ee8c...](https://github.com/dsmith328/LC13Master/commit/8f4f77ee8c60f76b32199593af9f224f435cbf28)
#### Sunday 2023-02-26 08:52:52 by Lance

Servant of Wrath

Records and Instability

Dash speed up

Fuck you I'll space indent all I like

There was some fuckin lint in this PR

God damned there's a lot of lint in here

Faction Check

Sprite update, minor bug fixes

Floating and Gun and Acid

Minor Records

Small update

Unnerfs resists

AoE hit fix

Gun update real

more res should mean less talk

Pixel Fix

Sound... Fix?

Broke the staff's legs, fuck those guys.

lmfao audio pains

Gun Rename, Spawn nerf

NO MORE FRIENDS FROM GUN

Faction change

acid tweak

---
## [peff/git](https://github.com/peff/git)@[197b01ddcb...](https://github.com/peff/git/commit/197b01ddcb5350a738d8946e92603ca075de5357)
#### Sunday 2023-02-26 09:30:41 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [peff/git](https://github.com/peff/git)@[8de374bb62...](https://github.com/peff/git/commit/8de374bb624e9032e16793f1094f4b211e2c5bed)
#### Sunday 2023-02-26 09:30:43 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---
## [merelymyself/nushell](https://github.com/merelymyself/nushell)@[3d65fd7cc4...](https://github.com/merelymyself/nushell/commit/3d65fd7cc4f6e0db0c1c31b895feabf2be66cb0a)
#### Sunday 2023-02-26 09:44:01 by Doru

Expose filtering by file type in glob (#7834)

# Description

Add flags for filtering the output of `glob` by file type. I find myself
occasionally wanting to do this, and getting a file's
[file_type](https://docs.rs/wax/latest/wax/struct.WalkEntry.html#method.file_type)
is presumably fast to do as it doesn't have to go through the fallible
metadata method.

The design of the signature does concern me; it's not as readable as a
filter or "include" type list would be. They have to be filtered one by
one, which can be annoying if you only want files `-D -S`, or only want
folders `-F -S`, or only want symlinks `--butwhy?`. I considered
SyntaxShape::Keyword for this but I'll just defer to comments on this PR
if they pop up.

I'd also like to bring up performance since including these flags
technically incurs a `.filter` penalty on all glob calls, which could be
optimized out if we added a branch for the no-filters case. But in
reality I'd expect the file system to be the bottleneck and the flags to
be pretty branch predictor friendly, so eh

# User-Facing Changes
Three new flags when using `glob` and a slightly more cluttered help
page. No breaking changes, I hope.

# Tests + Formatting

Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect` to check that you're using the standard code
style
- `cargo test --workspace` to check that all tests pass

# After Submitting

If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.

---
## [vlggms/lobotomy-corp13](https://github.com/vlggms/lobotomy-corp13)@[582f5b38cb...](https://github.com/vlggms/lobotomy-corp13/commit/582f5b38cb9ad5d051cbea48af501089ba3f0206)
#### Sunday 2023-02-26 10:32:54 by Lance

Holy FUCK temporary commit

Mixed between previous abno based spawning and new subsystem

Cleanup Commit

Removes a lot of previous code and paves the way for the subsystem method.

Major Commit

Apocalypse Bird drops it's loot and only spawns once. It'll not try to happen if there aren't enough birds, and if two are breached before the third arrives it'll take the third breaching to start the event, until the others are suppressed. Birds do not target people and are immortal while moving to the portal. If unable to reach it after 3 minutes they'll be forced in manually.

Tweaked Proc

Redundant Code Removal

Remembered I didn't need this

Enhanced Code

Moved an if-statement to a better place to more adequately solve the issue.

Test Commit

Does this solution work?

Global Abnormality Mob List

Patrol Changes and Bird Grab changes

Gaming Test?

Temp Commit

Second Commit

Another Commit!

Fourth Commit

Subsystem changes. Dead abno cleansing. Lower speak cooldown. Debug text removal.

P-bird fix

Fixes P-bird able to die before reaching the portal

---
## [stanalbatross/cmss13](https://github.com/stanalbatross/cmss13)@[7d27d8508c...](https://github.com/stanalbatross/cmss13/commit/7d27d8508ce0723dbbcf1dfad9810a3092a71f61)
#### Sunday 2023-02-26 10:54:26 by TotalEpicness

Fixes invincible base crusher (#2682)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Fixes an oversight that allowed base crusher to have half it's intended
shield cooldown
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.
runs
Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Never intended on the first place and led to crusher being busted as
fuck as it is currently.

This was never intended and was a mess up on my part. It fell through
from the painfully long development that Charger had as months went by
between testing sessions and TMs, along with my inexperience with larger
projects and bad note taking at the time.

Maintainers are also supposed to filter stuff like this but after like a
billion code reviews Charger had, I can see how it got through on their
end as well.

Nevertheless this dies here. 

funny contrib moment
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
it runs
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl: Totalepicness
balance: Fixes base crusher having half it's intended cooldown for the
shield ability
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Epicness <coolguyethanw@gmail.com>

---
## [kfir-manor/qemu](https://github.com/kfir-manor/qemu)@[8d0efbcfa0...](https://github.com/kfir-manor/qemu/commit/8d0efbcfa0656bef76e95d40933b6243feca58c9)
#### Sunday 2023-02-26 11:13:01 by Paolo Bonzini

docs: build-platforms: refine requirements on Python build dependencies

Historically, the critical dependency for both building and running
QEMU has been the distro packages.  Because QEMU is written in C and C's
package management has been tied to distros (at least if you do not want
to bundle libraries with the binary, otherwise I suppose you could use
something like conda or wrapdb), C dependencies of QEMU would target the
version that is shipped in relatively old but still commonly used distros.

For non-C libraries, however, the situation is different, as these
languages have their own package management tool (cpan, pip, gem, npm,
and so on).  For some of these languages, the amount of dependencies
for even a simple program can easily balloon to the point that many
distros have given up on packaging non-C code.  For this reason, it has
become increasingly normal for developers to download dependencies into
a self-contained local environment, instead of relying on distro packages.

Fortunately, this affects QEMU only at build time, as qemu.git does
not package non-C artifacts such as the qemu.qmp package; but still,
as we make more use of Python, we experience a clash between a support
policy that is written for the C world, and dependencies (both direct
and indirect) that increasingly do not care for the distro versions
and are quick at moving past Python runtime versions that are declared
end-of-life.

For example, Python 3.6 has been EOL'd since December 2021 and Meson 0.62
(released the following March) already dropped support for it.  Yet,
Python 3.6 is the default version of the Python runtime for RHEL/CentOS
8 and SLE 15, respectively the penultimate and the most recent version
of two distros that QEMU would like to support.  (It is also the version
used by Ubuntu 18.04, but QEMU stopped supporting it in April 2022).

There are good reasons to move forward with the deprecation of Python
3.6 in QEMU as well: completing the configure->meson switch (which
requires Meson 0.63), and making the QAPI generator fully typed (which
requires newer versions of not just mypy but also Python, due to PEP563).

Fortunately, these long-term support distros do include newer versions of
the Python runtime.  However, these more recent runtimes only come with
a very small subset of the Python packages that the distro includes.
Because most dependencies are optional tests (avocado, mypy, flake8)
and Meson is bundled with QEMU, the most noticeably missing package is
Sphinx (and the readthedocs theme).  There are four possibilities:

* we change the support policy and stop supporting CentOS 8 and SLE 15;
  not a good idea since CentOS 8 is not an unreasonable distro for us to
  want to continue to support

* we keep supporting Python 3.6 until CentOS 8 and SLE 15 stop being
  supported.  This is a possibility---but we may want to revise the support
  policy anyway because SLE 16 has not even been released, so this would
  mean delaying those desirable reasons for perhaps three years;

* we support Python 3.6 just for building documentation, i.e. we are
  careful not to use Python 3.7+ features in our Sphinx extensions but are
  free to use them elsewhere.  Besides being more complicated to understand
  for developers, this can be quite limiting; parts of the QAPI generator
  run at sphinx-build time, which would exclude one of the areas which
  would benefit from a newer version of the runtime;

* we only support Python 3.7+, which means CentOS 8 CI and users
  have to either install Sphinx from pip or disable documentation.

This proposed update to the support policy chooses the last of these
possibilities.  It does by modifying three aspects of the support
policy:

* it introduces different support periods for *native* vs. *non-native*
  dependencies.  Non-native dependencies are currently Python ones only,
  and for simplicity the policy only mentions Python; however, the concept
  generalizes to other languages with a well-known upstream package
  manager, that users of older distributions can fetch dependencies from;

* it opens up the possibility of taking non-native dependencies from their
  own package index instead of using the version in the distribution.  The
  wording right now is specific to dependencies that are only required at
  build time.  In the future we may have to refine it if, for example, parts
  of QEMU will be written in Rust; in that case, crates would be handled
  in a similar way to submodules and vendored in the release tarballs.

* it mentions specifically that optional build dependencies are excluded
  from the platform policy.  Tools such as mypy don't affect the ability
  to build QEMU and move fast enough that distros cannot standardize on
  a single version of them (for example RHEL9 does not package them at
  all, nor does it run them at rpmbuild time).  In other cases, such as
  cross compilers, we have alternatives.

Right now, non-native dependencies have to be download manually by
running "pip" before "configure".  In the future, it will be desirable
for configure to set up a virtual environment and download them in the
same way that it populates git submodules (but, in this case, without
vendoring them in the release tarballs).

Just like with submodules, this would make things easier for people
that can afford accessing the network in their build environment; the
option to populate the build environment manually would remain for
people whose build machines lack network access.  The change to the
support policy neither requires nor forbids this future change.

[Thanks to Daniel P. Berrangé, Peter Maydell and others for discussions
 that were copied or summarized in the above commit message]

Cc: Markus Armbruster <armbru@redhat.com>
Cc: Peter Maydell <peter.maydell@linaro.org>
Cc: John Snow <jsnow@redhat.com>
Cc: Kevin Wolf <kwolf@redhat.com>
Reviewed-by: Daniel P. Berrangé <berrange@redhat.com>
Reviewed-by: Alex Bennée <alex.bennee@linaro.org>
Signed-off-by: Paolo Bonzini <pbonzini@redhat.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[856411d0eb...](https://github.com/mrakgr/The-Spiral-Language/commit/856411d0ebd88afa81f2f4ae5f74078228ddd287)
#### Sunday 2023-02-26 11:17:37 by Marko Grdinić

"8:15pm. https://hibox.live/elixir-for-humans-who-know-python

///

The first age of web development was static files served through a webserver. It was new, exciting, chaotic and fun, but very primitive. Most of you are probably too young to remember this era by now.

The second age of web development was in languages like Perl, PHP, Ruby and Python, where a client sends HTTP requests to URLs, and the server returns dynamic content rendered as a static resource. This was a very fun era to be a developer, but applications were limited in how complex and featureful they could be, and there were a fair inefficiencies from re-sending a whole page just to reflect a single updated value.

Live Apps combine the best of two worlds, enabling developers to build complex, dynamic applications without the need for any JavaScript or a dedicated API. A client requests an initial page load, which the server renders and maintains a local understanding of, and then makes a follow-up request to establish a WebSocket connection. Client side interactions with the application are then passed through the WebSocket and changes to the state are returned and the DOM is dynamically updated accordingly, without any API interaction or custom JavaScript required, as all of the logic is kept on the server-side.

///

Websockets?

9:20pm. https://desu-usergeneratedcontent.xyz/g/image/1677/26/1677261525409.jpg

///

>27
>neet
>no degrees
>never worked
>get help and dig myself out of depression
>start to learn coding because that's the only thing worth I can learn from home and it's fun.
Alternative is 3 year training by a school for retards and mentally ill to become a office clerk or gardener.
Maybe I should get my HS diploma and go to university, but that doesn't fix my problem of having literally years of blank space on my resume.

Should I just get really good at coding and fake my resume? Maybe it's truly おわりだ for me..

///

///

>>91740098
I asked Gigachad for you anon, remember that an literal AI will give you better answers than anyone on /g/. Now get the fuck out of my thread and start learning nigger.

///

Here is the image.

> Gigachad c.AI
> Get good enough at coding to show real results by creating a portfolio of projects. Then use those achievements to demonstrate your skills to potential employers without needing to use your resume - your work will speak for itself. This is the way, my brother.

Chatbots these days sure are great.

2/26/2023

9:40am. Let me check my mail.

9:45am. I've been getting some weird trolls lately.

Damn I am groggy. Let me read Kaiji and then I will get started on the SQL basics course. I need to figure out foreign keys. When Teddy explained them, they made sense, but then he started adding those collections and I am confused again.

Yesterday I got a grasp on how to connect to the SQL Server. I have verified that there is only a single server process that my client application connects to in the background.

Why was even something trivial like this confusing. Because I have like a dozens of old servers in the program list. Let me get rid of them.

9:50am. All cleaned up now. I only have the SQL Server 2022 stuff installed now.

https://mangadex.org/chapter/c0005ec5-40a2-4351-a7c5-24805dc4c074/24

Loooooooooooooooooollll. Old men are the best after all.

10am. Enough fun. Let me watch the SQL Server course.

Since I hadn't gotten any word from Valora at this time, can assume this is a dud? I don't know. I applied on the 23rd. 3 days is not too much, but if I do not get anything in another 1.5 weeks, I'll forget about it.

https://youtu.be/9Pzj7Aj25lw
Learn SQL in 1 Hour - SQL Basics for Beginners

Here is the one by Joey Blue. It is only 1h, so let me go for it.

https://youtu.be/9Pzj7Aj25lw?t=213

I see him having all these servers. I wonder how it is possible to rename it.

11:55am. Done with the course. It was pretty basic, but informative. This is the first time I've touched SQL. I find a syntax a bit confusing, but that is a matter of simply memorizing the relevant stuff. I can just Google it in the heat of battle. The biggest gain today and yesterday is my improved familiarity with SSMS. If I ever do SQL on a job, that should be convenient.

12pm. At this time I do not feel the need to learn more SQL.

What I really need to understand though is how EF and the...

Well, I suppose I could do a special record in SqlFun for joins, but I'd be better off just asking the author if it comes to that. It doesn't really matter right now. With ADO.NET if I go down that route, I can just use indexes to fetch everything back as a tuple.

12:05pm. This is a great time to stop and have breakfast.

Today I said that I had no email, but I wouldn't usually get anything on a Sunday anyway. I have no concepts of weekends in my personal life. I guess that will change when I get a job.

The next thing on the agenda is to get back to the Web API course and see it all the way through. I think I'l get a handle on foreign keys and relations in EF by the end of it.

I do not really care that much about SQL and databases, but I want to understand at least this much.

...Ah, come to think of it.

https://jacentino.github.io/SqlFun/Transforming-query-results

Hmmm, no inner joins here.

Nevermind that.

12:15pm. Let me commit here. There is no point in wondering about this. Just go through the EF course next and you are done with databases."

---
## [etianl/Trouser-Streak](https://github.com/etianl/Trouser-Streak)@[f5a16ec3b5...](https://github.com/etianl/Trouser-Streak/commit/f5a16ec3b5a4ad85ebb7e6ff4962f2e5ac11a53a)
#### Sunday 2023-02-26 11:26:03 by etianl

0.3.8 Many big updates, SHULKER BUTTONS back!

0.3.8
-**General**
-FULLAUTO options for Boom+, ExplosionAura, and HandOfGod now have a tick delay for reduced lag.
-ExplosionAura explosions now also have a tick delay when you are moving for less lag
-AirStrike+, Voider, and ExplosionAura now turns off when you leave the game and voider also when you die.
-AirStrike+ now rains cats which are invulnerable to damage.
-AirStrike+ Can now rain CatsAndDogs as an option.
-**ShulkerDoop!**
-Made ShulkerDupe work more like the original, using buttons in the shulkerbox screen rather than options in the meteor menu. Still uses Allah-Hack dupe code, credits to them for that.
-STILL ONLY WORKS IN SERVERS 1.19 and BELOW, VANILLA, FABRIC, OR FORGE.
-**NewerNewChunks updates**
-Improved the "IgnoreFlowBelow0" option to show a newchunk as well if flow is above AND below Y0 not just if above Y0.
-Added AdvancedMode to NewerNewChunks, which highlights chunks that have flow only below Y0. If there is nothing but these you are updating old chunks to the new build limits and the FlowIsBelowY0 coloured chunks are OLD. If they are mixed with newchunks the FlowIsBelowY0 coloured chunks are NEW.
-**Voider updates**
-Renamed to Voider+.
-Voider now grabs a location on activation to void around, instead of keeping it centered around your position. Just ensure that area stays loaded.
-Added a "VoiderBot3x3" option to run voider nine times over to void it's full range three by three times.
-Added a "TP forward" option which can teleport you forward and run Voider again clearing a strip out of the world.
-**HandofGod updates**
-Added "NukeAroundPlayer" option so you can now turn off the default /fill around your player.
-"NukeAroundPlayer" /filling is now based on a tick delay, rather than based on pressing directionals like it was before
-Added "VoiderAura" option. It /fills a single layer from top to bottom in a loop based on the ranges from your character you set. Credits to AllahHack for the idea from the voider module.
-Added "MagicEraser" option. It deletes a single layer up to 90 blocks in radius at a set distance from your character. Press directional keys to delete world.
-Added "Roofer" option so you can automatically make an obisidian roof as you're deleting the world.

---
## [CaosCreations/SpaceTruckin](https://github.com/CaosCreations/SpaceTruckin)@[d3a9d10d8e...](https://github.com/CaosCreations/SpaceTruckin/commit/d3a9d10d8edd1e358d8e9b58d4f3aaebd663fae3)
#### Sunday 2023-02-26 12:25:50 by Stefano di Pace

Proper name tags (#644)

* Name Tag Asset is IN

* More UI Stuff

Background layer, proper + Prefab stuff

* New Player Response Asset

just tried to make it a lil prettier really

* applied the prefab DURRRR

oops

* New version babyyyy

woooo

* FUCKIN FIXED THIS SHIT

BITCHEEEEZZZZ

* more fixes??

yes, more.

* last one

maybe

---------

Co-authored-by: Max <61809127+maxwellpark@users.noreply.github.com>

---
## [sleepynecrons/cmss13](https://github.com/sleepynecrons/cmss13)@[558717e6f6...](https://github.com/sleepynecrons/cmss13/commit/558717e6f627bf2bdc8e00c620db04c0a55cede0)
#### Sunday 2023-02-26 13:36:03 by zeroisthebiggay

(hopefully) webedits a grammatical correction into headbite's kill message (#2537)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

when someone dies to headbite it displays as
`Urr Mot'herr has died to executed by headbite at the Containers from
Elder Lurker (GIT-222)`
hopefully with this simple one line webedit it should instead be
`Urr Mot'herr has died to headbite execution at the Containers from
Elder Lurker (GIT-222)`
god fucking knows if this is the right line

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

uhm
it reads better

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

github

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
spellcheck: 'executed by headbite' to 'headbite execution' when listing
someone dying to a headbite in deadchat
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[5f78464e25...](https://github.com/harryob/cmss13/commit/5f78464e255b89ada7ca58f5114561be7b32f055)
#### Sunday 2023-02-26 15:19:26 by NewyearnewmeUwu

Removes skull balaclava and skull facepaint from loadout, places them hidden on the Almayer. (#2526)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This removes the skull balaclavas and the facepaints from the loadout
menu and instead places them in 2 places hidden around the Almayer. The
reason I have done this is that they are almost exclusively used by
people who who are referencing a character- usually Ghost from MW2
(either version) or the characters from COD Ghosts. See below for more
details.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is an OOC meme item that doesn't fit the tone of CM, particularly
because we _already_ have an item with a skull on it in case you want to
use it: Armor! They wrote things on armor in the movie, including a
skull!

![image](https://user-images.githubusercontent.com/70115628/215395714-4aa1c9a2-7621-4f82-8e4b-6d7ed4905f89.png)

Instead, we have these types of people, running a skull 'clava in every
round even as command or medical characters. This is a modern 'operator'
look, not a Space 'Nam-esque look and not an Aliens look. If you want
something that'd remind you of Space 'nam, just look at the classic
'born to kill' helmet. Now, look at these CALL OF DUTY CHARACTERS THAT
THIS ITEM REFERENCES!


![image](https://user-images.githubusercontent.com/70115628/215396029-290063ae-cd96-4929-b6f0-ae2f1c517887.png)

![image](https://user-images.githubusercontent.com/70115628/215396040-0eb9e31f-71ed-408a-8248-152916427bdd.png)

![image](https://user-images.githubusercontent.com/70115628/215396561-f4493f24-2405-4b8d-8034-02a96ea6919f.png)

This is goofy as hell and kind of an outlier among the customization
options since it is _very clearly_ a reference to COD. Look at its
description:

"The face of your nightmares. Heed the call of duty as the ghost in the
night with this metal 'clava. Additionally protects against the cold.
Now in black!"

You'd get laughed off a real marine base for wearing this, let alone
wearing one on an op. We don't need more people running this every
round, and this gives them something to fight over between eachother- if
_you_ want to larp as Simon 'Ghost' Riley from hit video game COD MW2
(either version) then you'll have to hunt it down.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
del: Removed skull balaclavas and skull facepaint from the loadout
options
maptweak: adds a single skull facepaint and balaclava, each hidden in
their own locations on the Almayer.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [DarviL82/Lanat](https://github.com/DarviL82/Lanat)@[30ff27f77e...](https://github.com/DarviL82/Lanat/commit/30ff27f77e0dc5a0ee5a53b0ad9f1cefa80b70d6)
#### Sunday 2023-02-26 15:56:43 by David Losantos

Merge pull request #1 from DarviL82/feature/mirror

Fuck you use my lib

---
## [pa-gr/android_frameworks_base](https://github.com/pa-gr/android_frameworks_base)@[b659896878...](https://github.com/pa-gr/android_frameworks_base/commit/b659896878f8da88a4da20d2f73a9155bcb4fa50)
#### Sunday 2023-02-26 17:04:20 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [psycotica0/MultiplayerSubmarine](https://github.com/psycotica0/MultiplayerSubmarine)@[bb6e5b9992...](https://github.com/psycotica0/MultiplayerSubmarine/commit/bb6e5b999250ad82716991caa215a42acd8d165e)
#### Sunday 2023-02-26 17:08:07 by Christopher Vollick

Player Resumption

I now support a player disappearing and coming back gracefully.

When the host sees a player disconnect it tells everyone else that this
player is a piece of garbage who is mean to us, and then everyone starts
fading that player out to indicate that they're not really there.

They also drop whatever they're holding so a disappearing player isn't
holding a critical tool or something.
If they get to the end of fading out, we remove them.

If a player with the same name shows up, we assume it's the same player
but with a different network ID so we just change it to work for them.

On the other side, if I'm joining a game and there was already a player
reported to me that has the same name as me, I assume that's me!

I took the position out of the "player_ready" event thing because it was
kinda meaningless.
Either the player is new so I want to put them in the new player spot,
or they're coming back in which case I want them to be where they
already were...

But for the returning player I'd have to go find my position out of what
I was just told just to report it back to everyone later. Which is dumb.

So I took it out.

There is one edge case here, though. Because I don't sync how long a
player's been mourned, if I join a game where there's an inactive player
there will be a window where the host already deleted them but they
haven't timed out on my computer yet. If the player rejoins in that
time, the host will see them as a new player, and put them in the new
player space. And that "new" player will see that and put themselves in
the new player space. But I will see them wherever they used to be and
resurrect them over there!

But that doesn't really matter, because as soon as the player moved it
would sync their opinion of their position to all clients anyway. So I'd
see it teleport at that time. The only thing that keeping it in the
"player_ready" event thing would do is teleport just before they moved
rather than as soon as they do.

So there's technically a weird thing that could happen where if a player
comes back but doesn't move then different players won't agree on where
they're standing still. Which seems minor.

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[7cc6934eff...](https://github.com/Helg2/tgstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Sunday 2023-02-26 17:29:58 by LemonInTheDark

Visual fixes (lighting, weird shit, old bugs from a parallax thing) (#73555)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

[Fixes a bug where anything fully dark on the floor plane would mask the
lighting
plane](https://github.com/tgstation/tgstation/commit/a1a03dc3393216098890b971b2271d56cb2c7463)

I fucked it up boys, needed to take alpha into account here

[Fixes pais getting parallax on icebox because their location was
nested](https://github.com/tgstation/tgstation/commit/81252e0f45c53918a14cc0148353ec440710f8e5)

God I hate this place (Note when I say get I mean they got the plane
master that controls it, not that they actually got it displayed. That
does appear to sometimes happen but I have no idea why)

[Fixes double flashlights not activating if enabled in
place](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

[efb8b64](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

cast_directional_light removes the lighting appearance, because it's
gonna modify it, but it turns out because appearances are static when
they're in like underlays/overlays, this could remove the WRONG UNDERLAY

This lead to double held flashlights just... not working until you
rotated. V stupid.

I've also had to move the flag set to make the overlay add in
cast_directional_light work. Depression

## Why It's Good For The Game

Closes #73535, closes #73517, closes #73518, and fixes part of #73471
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
fix: Fixes activating two flashlights without moving only turning on one
flashlight (until you move)
fix: Purely black things drawn on the floor (like carpets, those foam
dispensers, etc) will no longer cause things on top of them to be fully
masked in darkness
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [XXSuperMario64FanXX/vm2](https://github.com/XXSuperMario64FanXX/vm2)@[2b76197397...](https://github.com/XXSuperMario64FanXX/vm2/commit/2b76197397b4241957e93a9779fdd9dfbada2688)
#### Sunday 2023-02-26 18:28:25 by Jacquerel

Makes Lesser Form into one ability & unit tests it (#73572)

## About The Pull Request

Fixes #73491
Every time I have used this ability lately it's been fucked. 
It would vanish from my actions at arbitrary moments, and also sometimes
transform me into a horrible monkey-man thing instead of a monkey. This
is a shame because being able to become a monkey can be pretty fun, even
if it makes you very vulnerable to being butchered.

Refactoring it into being one action instead of two actions which add
and remove each other fixes the part where the action just disappears.
It reliably sticks between transformations now, regardless of whether or
not they were voluntary.

I also noticed that when I was turning into a monkey it wasn't dropping
the changeling "fake clothes" outfit pieces I had on as a human, leading
to a really fucked up looking monkey. I fixed this by adding `force =
TRUE` in the drop to ground proc in the check for if the equipment you
have is still valid after your species changes. I don't _think_ this has
any side effects but I never do and then someone finds some.
For good measure I also made all of the changeling equipment abilities
which don't work if you are a monkey detect if you become a monkey and
retract themselves.

I also noticed that for a long time Last Resort has been trying and
failing to give you Lesser Form (well, Human Form rather) as a Headcrab,
so I fixed that and now you actually get the ability.

Finally I did a _little_ bit of housekeeping in general on the
changeling actions, mostly balloon alerts. I think these definitely need
more attention than I gave them though. I left a lot of the `to_chat`s
in place because many of them give information you want to be a little
sticky, or refer back to in order to double check what you just did.

I also added a unit test which flips back and forth a few times to
ensure the ability still works.
This required adding an "instant" flag to the monkeyize/humanize procs
to skip the timers, and idenitified a couple of weird issues.
First point: Humanising a monkey would remove the monkey mutation and
then call humanise again, which would not skip itself because it still
regarded you as being a monkey. I changed the order of operations here
slightly so that it will early return.
Second point: Calling `domutcheck` on `human/consistent` would runtime
because we skip the bit which sets up any mutations in their DNA. This
is a part of changeling transformation, so I just made it return
instantly.

## Why It's Good For The Game

You can use this ability again without getting stuck permanently as a
monkey, or it just deleting itself from your list of abilities for no
reason.
Turning into a monkey with fake outfit pieces on won't turn you into an
abomination.

## Changelog

:cl:
refactor: Changeling's Lesser Form is now one ability instead of two
which keep swapping, which should consistently turn you back and forth
without deleting itself from your action bar.
fix: Hatching from an egg left by a Last Resort headcrab should
correctly grant you Lesser Form in addition to your other abilities.
fix: Turning into a monkey while using the Changeling space suit won't
leave you as a monkey with a weird inflated head.
qol: Using lesser form as a monkey with only one stored DNA profile will
skip asking which profile you want and will simply transform you
immediately into the only option.
/:cl:

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [mtoohey31/helix](https://github.com/mtoohey31/helix)@[973c51c3e9...](https://github.com/mtoohey31/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Sunday 2023-02-26 19:53:33 by Michael Davis

Remove C-n and C-p from the insert mode keymap (#3340)

These are read-line-like bindings which we'd like to minimize in
insert mode in general.

In particular these two are troublesome if you have a low
`editor.idle-timeout` config and are using LSP completions: the
behavior of C-n/C-p switches from moving down/up lines to moving
down/up the completion menu, so if you hit C-n too quickly
expecting to be in the completion menu, you'll end up moving down
a line instead. Using C-p moves you back up the line but doesn't
re-trigger the completion menu. This kind of timing related change
to behavior isn't realistically that big of a deal but it can be
annoying.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[91f06a97d3...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/91f06a97d3f24c849241bf909b7de28b9b6ec951)
#### Sunday 2023-02-26 20:37:08 by candle :)

Small VoxPrimalis Fixes (#18944)

* fuck you i don't need to give you a fucking summary

* fixes

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[d95ca04819...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/d95ca048192f08a8fbaf524fdb4ab0ca498b319e)
#### Sunday 2023-02-26 20:37:08 by Rimi Nosha

[MODULAR] Fixes All Known Modular Persistence (NIF) Saving Issues (#19096)

* Fuck

* Holy shit

---
## [saem/nimskull](https://github.com/saem/nimskull)@[35c26e9f71...](https://github.com/saem/nimskull/commit/35c26e9f712e0acd6b46282e07df64d654aa20aa)
#### Sunday 2023-02-26 20:46:07 by Saem Ghani

Parser: drop direction `reports` dependencies

This removes direct dependency on `reports`, but an indirect one still
exists via `msgs`. It's pretty trivial indirection at the moment, but
after dropping direct reports dependencies the API can be changed more
drastically.

A number of changes were required in order to make this possible, here
is an overview:

- smaller parser public API & simpler implementation
- added `parse` compiler command, for devs
- parser error message improvements
- fixes to `astrepr` logic and output
- lots of style clean-ups

Details
=======

Slimmer `parser` Public API
---------------------------

Previously the parser had many public procedures (eg: `isOperator`,
`getTok`, `skipComment`, etc) that would allow fine grained control for
other modules.

There are many issues with this:
- there are no consumers of this API
- lots of public API surface to test
- the API itself was bad, it conflated lexing and parsing

The public API surface for the parser has been reduced significantly,
now consisting of:
- `openParser`
- `parseTopLevelStmt`
- `parseAll`
- `closeParser`
- `parseString`

That's it, which frankly reads far more sensibly.

Simplified `parser` Implementation
----------------------------------

- removed `InternalReport`, `reports_parser`, and `reports_enum` imports
- introduced diagnostics for the parser, akin to the lexer, `ParseDiag`
- `ParseDiag` favours data over strings
- `ParsedNode` now has its own kind enum, mostly a subset of
   `TNodeKind`, but entirely compatible

Consolidated a pattern within the parser, where a node was created with
the current token's information, and then the token was immediately
consumed via `getTok` to advance the `lexer`. This is captured in the
newly introduced `newNodeConsumingTok`.

Long-term, itemizing these traversal/consumption patterns will make the
parser logic not only more regular, but also highlight oddities in the
grammar as the implementation will be convoluted.

Parsing/Diagnostics Performance
-------------------------------

`ParsedNode` uses a lightweight `ParsedToken`

Introduce `ParsedToken`, a smaller data type, storing the least amount
of data required from `lexer.Token` for `ParsedNode`. This not only
saves memory, but the runtime performance impact on my machine is
roughly 33% faster full compiler testament run for all targets

- before change: 3+ minutes
- after change:  2+ minutes

Added specialized diagnostic/report kinds for:
- empty accent quote when ident expected
- msg for asm statements without a string literal
These reduces the amount of string data carried around in the compiler.

Improved Custom Numeric Literal Handling
----------------------------------------

- the `lexer` still does silly things for lexing these
- it just does less work and produces better data
- fewer string operations and hacks are required by the `parser`

Parser Diagnostic/Reporting - Invalid Indentation
-------------------------------------------------

- now has correct source line information
- tracks instantiation and submission location
- has the appropriate severity
- improved phrasing for indent error from possible missed `=` character
- adjusted tests for the above

Parser Diagnostic/Reporting - Malformed Call Syntax
---------------------------------------------------

- `parser` detects malformed calls and sets better line info
- net-net the user will have a better chance to find the issues

Parser Diagnostic/Reporting - Misc
----------------------------------

- token rendering call out keywords via prefix, eg: `keyword template`
- inconsistent spacing style check shows the problematic source

Removed unused report kinds:
- `rparIdentOrKwdExpected`
- `rparRotineExpected`
- `rparPragmaAlreadyPresent`

Parse Compiler Command
----------------------

`parse` command:
- added `parse` command, which outputs the parsed ast for a file
- usage: `nim parse foo.nim`
- super useful for diffing parser output changes
- heavily leverages `astrepr`

`astrepr` module:
- `astrepr.treeRepr` now works for `ParsedNode`, was previously broken
- AST trasversal is now exhaustive and breakages less likely to pass CI

`astrepr` output improvements, mainly for `ParsedNode`:
- `astrepr` now shortens ParsedNodeKind enum
- output now includes line and column information
- comments no longer result in excessive new line output
- fixed many formatting issues for `ParsedNode` output
- improved `astrepr`'s output for custom numeric literals

Canonical Filenames Performance Issue
-------------------------------------

Also discovered a performance issue with canonical filenames option and
the `nimdebugstacktrace` option. Removed some of the pain, but canonical
file paths result in significant performance issues due to filesystem
IO. I've fixed part of it and filed an issue:
https://github.com/nim-works/nimskull/issues/546

Other Improvements
------------------

- introduced `debugutils.setFrame` template for frame msg hints
- above `setFrame` avoids the canonical path performance hit
- removed circular dependency between `ast` and `options` module
- document unused parser reports and other outliers
- move `isImportedException` to `ast/types`, whice drops `front/options`
  cyclic depencdency from `ast/ast_query`
- fixed docs in nimlexbase, also easier to understand
- `ast.toPNode` now handles `nil` input
- `syntaxes.parseFile` returns `ParsedNode`, allows avoiding unnecessary
  conversions in future use cases where only `ParsedNode` is required

Special Mentions
----------------

Thanks, clyybber and zerbina for the reviews!

Misc
----
- remove blank space characters from otherwise empty lines
- remove awful code style of `0 < foo.len`
- fixed a number of typos in comments
- adjusted a few tests to ensure they pass

---
## [xTVaser/jak-project](https://github.com/xTVaser/jak-project)@[c249dbc437...](https://github.com/xTVaser/jak-project/commit/c249dbc43750b0b811bbe4d10d29663bec39b9ae)
#### Sunday 2023-02-26 21:08:04 by water111

[jak2] improve loader for jak 2 levels (#2206)

Add a debug window for the loader to show levels and fix an issue with
jak 2 level unloading. I never really thought about how this works for >
2 levels, and there is a chance that you could unload the wrong level in
some cases.

The problem is some combination of merc-only levels not counting toward
the "in use" detection, and the unloader ignoring what the game wants to
load.

I don't remember why using merc models doesn't contribute to "in use"
but I'm afraid to change this for jak 1. Instead, we can have the
unloader avoid unloading levels that the game is telling us are loaded.
This is what we should have done originally, but there was a time when
Jak 1 didn't tell the loader anything, and we had this stupid detection
thing.

I think this is the first step toward just getting rid of the "in use"
detection and trusting the game for everything.

---
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[b4954e1402...](https://github.com/Ultimate-Fluff/cmss13/commit/b4954e14028909b107d0b204da0ad06c5dfeb50a)
#### Sunday 2023-02-26 21:21:17 by carlarctg

zombie powder fix (#2315)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Fixes Zombie Powder bugging the fuck out by slapping a ton of FAKEDEATH
checks everywhere. It now properly shows the holder as dead on HUDs and
scans.

Fixed an issue in which sometimes qdeleted reagents still procced on
life.

Fixed examining things changing your direction if you're incapacitated.

Added FAKEDEATH to the mob_incapacitated() check.


# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
fix: Fixes Zombie Powder bugging the fuck out by slapping a ton of
FAKEDEATH checks everywhere. It now properly shows the holder as dead on
HUDs and scans.
fix: Fixed an issue in which sometimes qdeleted reagents still procced
on life.
fix: Fixed examining things changing your direction if you're
incapacitated.
fix: Added FAKEDEATH to the mob_incapacitated() check.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[b53c9f0531...](https://github.com/Ultimate-Fluff/cmss13/commit/b53c9f0531897023fe365961c16863d8f41983d9)
#### Sunday 2023-02-26 21:21:17 by carlarctg

Turns all instances of 'colour' into 'color' (#2609)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Turns all instances of 'colour' into 'color'.

Changed a shittily-named crayon variable's name.

# Explain why it's good for the game

We use burgerclapper english and we should standardize this

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
spellcheck: Removed all instances of 'colour' and replaced them with
'color'
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[45fb9e9407...](https://github.com/treckstar/yolo-octo-hipster/commit/45fb9e9407f3daf96ba979ca82b3a571920c3c67)
#### Sunday 2023-02-26 21:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [GerHobbelt/tesseract](https://github.com/GerHobbelt/tesseract)@[5941f3d4f1...](https://github.com/GerHobbelt/tesseract/commit/5941f3d4f1660ec4565ce1de7a4d67d15d164ce0)
#### Sunday 2023-02-26 21:55:49 by Ger Hobbelt

fix compiler errors due to windows system header file errors

----------------------

// mupdf headers cause some weird error in MSVC system header commdlg.h when include *after* <random> header below. And this only happens for params.cpp, i.e. when params.h has been included first. ... A definite case of WTF?!
//
// Which is why we include the mupdf headers here in monolithic builds...
//
// EDIT: Subsequent compiler runs and analysis now popped up the same 'crazy' errors in commdlg.h (caused by missing font struct definitions)
// from control.cpp and a few other tesseract source files. Which forced me to investigate further.
//
// Debugging through running the preprocessor (cl /E /P ...) and some grepping
//
//   grep '#line' $( find -name control.i )  | grep -B 1000000 commdlg | grep -B 1000000 wingdi | grep -v "Program Files"
//
// showed the original culprit was probably MuPDF\\thirdparty\\curl\\lib\\setup-win32.h.
// And indeed there we found the often-troublesome WIN32_LEAN_AND_MEAN and a few choice other NOXYZ feature defines before loading windows.h.
//
// > Rationale for the precise grep chain is out of scope.
// > Hint: wingdi defines what commdlg needs. Chain + last filter takes care of getting loading file as last #line stmt, IFF you're lucky.
// > Of course I was lucky. After N iterations, which got me to this grep chain. EFF that shite, with prejudice!
//
// This practice MUST be abolished in all libraries, everywhere, as it causes severe compile errors at surprise locations and at surprise times,
// while the errors reported aren't always easy to diagnose for everybody. (How many programmers are well versed with gcc -E, cl /P and code inspection?)
//
// Setting these feature defines MUST be the sole prerogative of the final application code/project, if any. Or rather more precise: the final C/C++ *.c+*.cpp source files.
// No-one else MUST mess with these in any header / include files, just to 'help' shorten compiler turn-around times. The road to Hell is paved with good intentions.
// If you want to offer 'help' like that, consider making sure your header files work well with precompiled header caching in the various compilers instead.
//

See also cUrl repo.

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[766f5529bf...](https://github.com/carlarctg/cmss13/commit/766f5529bfca454129f6d62f1ed626d6a70d5432)
#### Sunday 2023-02-26 22:39:05 by carlarctg

Removes Autodocs from the Almayer (#2607)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Removes autodocs from medbay. They're replaced with 2 random potted
plants. :)

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->



EDIT: Tomorrow I will update this PR to give nurses surgery skill.

Autodocs fundamentally and inseparably, irrevocably, DESTROY medbay and
surgery gameplay. There is NO REASON, EVER to put someone through manual
surgery when you could just haha autodoc them instead. Autodocs kill the
good old hell medbay lines, they make surgeons extremely lazy and
stagnant (Tales of surgeons doing surgery for a few minutes, then giving
up and autodoccing the patient are common, not to mention the times
where they miss something in the autodoc schedule), they remove all
skill depth, floor, ceiling, the middle from medbay, and they also make
marines complacent by having them want the funny magic robot machine
rather than an actual human to treat them.

I understand that this may be too sudden of a change. If so, I propose
the following: Cryo tubes could slowly heal a marine up entirely,
removing organ damage and bone breaks through the course of a very slow
5-10 minutes. This will allow marines and nurses to get treated if
there's no doctor around or alive. However, I think the best course of
action is to just ram this change through and make medbay adapt. Embrace
the suck.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
balance: Removes Autodocs from the Almayer
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [carlarctg/cmss13](https://github.com/carlarctg/cmss13)@[7f5cd54b2b...](https://github.com/carlarctg/cmss13/commit/7f5cd54b2bab2fdbd25a3f970e9a7f55d415dfe9)
#### Sunday 2023-02-26 22:39:05 by carlarctg

Colony Guns Part 3: Longarms Rework (#2334)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Updates and buffs the following weapons:

- Basira-Armstrong Rifle
- Model 12 Bolt-Action Rifle
- M37-17 pump shotgun
- Dragunov sniper rifle

### Basira-Armstrong Rifle

- The BA rifle has been reflavored as the removed 'ceremonial' ABR-40,
now a hunting-civilian version of the L42. It effectively has the same
stats as the L42, just don't take the stock off!
- Its magazines can only fit 12 bullets, but they still have the classic
L42 kick to them. The magazines are completely compatible between both
military and civilian gun types.
- Additionally, there are now holo-targeting magazines available for the
ABR-40, for hunting target capture purposes.
- - The Contractor ERT has a chance to spawn with a tacticool ABR-40
loadout, with three spare holotarget magazines on their webbing.

### Model 12 Bolt-Action Rifle

- Like its sprite implies, this is now the new Basira-Armstrong rifle.
- Its stats have recieved an overhaul and it can now hold its own
against a Xenomorph (or marine if you're CLF)
- Additionally, its bullets will push back (not stun) targets within
three meters, to increase viability for colony usage.

### M37-17 Pump Shotgun

- Did you know that the 10% damage mod this gun was supposed to have
didn't work? Now it does! And it deals 15% more damage to make up for
it.
- However, it can now be melted down.

### Dragunov Sniper Rifle

- The dragunov has been revamped into a DMR, needing no skill to fire,
dealing good damage, and having the same push-back feature the
bolt-action now has.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

All of these weapons are seen as, and are, a complete joke and ignored
in favor of chungillionaire among us sus impostor running around PBing
xenos with buckshot. Buffing them to be useful paves the way for
civilians to use civilian weaponry instead of chungillionarius.

### ABR-40 Hunting Rifle

This is intended as asset recycling. IIRC, Triiodine disliked the
existence of a ceremonial rifle and thought that was goofy, which is an
understandable opinion, but it pains me to see the gun's cool assets go
unused. I took the opportunity and made the lame and mediocre Basira
into this cool gun which marines and survivors will take a lot more
interest in than a Basira plinker.

While it does have L42 stats, colonists won't be able to locate any L42A
ammo on the colony, meaning they are limited to 12-round magazines.
Still, giving them a weapon like this is a great way to incentivize them
to step out of their chungus zone.

As for the contractor addition, these are supposed to be ex-USCM
mercenaries, who are trained in the usage of marine equipment. It makes
sense that they'd grab the civilian version of a primary marine gun and
tune it to their liking.

### Basira-Armstrong Bolt-Action Hunting Rifle

Chomp made this really cool backend for a bolt-action that tragically
ended up never being used, not really, aside from a half-hearted few
rifles being thrown in at Shiva's Snowball. Since these guns are so
weak, it's plain to see why nobody even looks at them twice. So I
changed that.

### M37-17 Pump Shotgun

Bugfix and a small damage buff to make up for it. It being unacidable
was lame anyways. Spread projectiles are still bugged and don't inherit
the base gun's damage mod, but that's out of scope.

### Dragunov Designated Marksman Rifle

This gun has been a joke since 2017, it's time to give it some love.
Still needs one-hand sprites but not my problem.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Be sure to properly mark your PRs to prevent unnecessary
GBP loss. Maintainers freely reserve the right to remove and add tags
should they deem it appropriate. -->

:cl:
balance: Updates and buffs the following weapons: Basira-Armstrong
Rifle, Model 12 Bolt-Action Rifle, M37-17 pump shotgun, Dragunov sniper
rifle
imageadd: The Basira rifle has been reflavored as the removed
'ceremonial' ABR-40, now a hunting-civilian version of the L42. It
effectively has the same stats as the L42, just don't take the stock
off!
add: Its magazines can only fit 12 bullets, but they still have the
classic L42 kick to them. The magazines are completely compatible
between both military and civilian gun types.
add:: Additionally, there are now holo-targeting magazines available for
the ABR-40, for hunting target capture purposes.
add: The Contractor ERT has a chance to spawn with a tacticool ABR-40
loadout, with three spare holotarget magazines on their webbing.
balance: Like the bolt-action rifle's sprite implies, this is now the
new Basira-Armstrong rifle.
add: Its stats have recieved an overhaul and it can now hold its own
against a Xenomorph (or marine if you're CLF)
add: Additionally, its bullets will push back (not stun) targets within
three meters, to increase viability for colony usage.
balance: Did you know that the 10% damage mod the M37-17 pump shotgun
was supposed to have didn't work? Now it does! And it deals 15% more
damage to make up for it.
del: However, it can now be melted down.
balance: The dragunov has been revamped into a DMR, needing no skill to
fire, dealing good damage, and having the same push-back feature the
bolt-action now has.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---

