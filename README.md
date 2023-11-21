## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-20](docs/good-messages/2023/2023-11-20.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,660,756 were push events containing 3,929,892 commit messages that amount to 300,694,594 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 72 messages:


## [1393F/tgstation](https://github.com/1393F/tgstation)@[7f0536bb93...](https://github.com/1393F/tgstation/commit/7f0536bb930a022d23d636619e4baf73661280a2)
#### Monday 2023-11-20 00:16:52 by san7890

Makes Telekinesis + Russian Revolver Interaction more fair (#79740)

## About The Pull Request

Fixes #77238

Basically, you were able to just spam kill people with the russian
revolver if you had telekinesis, which isn't really fair. Now, after
taking a leaflet out of the the discussion in that issue report, you can
still pull off the same party trick... once...

Basically, let's just say that when you focus on firing the gun in your
mind... you're also pointing it directly at your mind (your brain (your
skull (you instantly die))). This occurs even if the projectile doesn't
actually touch you (because that would be hellish to account for) but
you're the one who's playing russian roulette man

You still get to do some collateral damage because that's still a very
funny interaction but you only get to do it once per life. I don't know
if people will be happy to revive you after you "shoot" them. Also, the
way it's coded means that you can still leave the revolver on the table
and fire it at your foot or something, or just use it normally, as a
telekinesis user. This _only_ applies to distance-based firings.
## Why It's Good For The Game

The russian revolver is specifically coded to prevent you from damaging
other people, and this was a pretty silly way to sidestep that based on
the checks. Instead, let's make it so that you can still do this
admittedly funny interaction, but with enough reason to not do it (the
reason being that you'll always get fucking blatted).
## Changelog
:cl:
balance: After a string of unfortunate incidents, persons with
telekinesis have been strongly warned against playing Russian Roulette,
as they tend to hyperfixate on the gun a bit too much and end up firing
it directly at their head.
/:cl:

---
## [1393F/tgstation](https://github.com/1393F/tgstation)@[2562f0997a...](https://github.com/1393F/tgstation/commit/2562f0997a73a52c4ada51c7e0d9996fea4ee573)
#### Monday 2023-11-20 00:16:52 by MrMelbert

Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished (#79694)

## About The Pull Request

Related: #78017 

Stop drop and roll is no longer instant -5 fire stacks -> stun -> wait. 

Now, when you stop drop and roll, every time you roll you will lose 1
firestack.

A roll is triggered every 0.8 seconds. Moving, getting up, or becoming
incapacitated / stunned will stop you from rolling.
_(This number puts it roughly equivalent to its current rate.)_

While rolling, your hands are blocked (you cannot use items, hold
things, etc.)
Additionally, you will roll until all firestacks are cleared. 

## Why It's Good For The Game

Getting stunned for 6 seconds because you decide to stop and roll is a
little silly. Reasonably you could stop rolling and get back up should
the need arise, such as "oh god there's more fire I gotta relocate".

By changing it to a gradual thing, it makes it a bit more reasonable and
fair.
- New players who immediately slam "STOP DROP ROLL" because the alert on
their screen tells them to are no longer helpless for 6 whole seconds
- People who hit the resist key, intending to interact with something
else (such as a bola) are no longer stuck rolling when they did not want
to

## Changelog

:cl: Melbert
balance: Stop, drop, and roll no longer instantly clears 5 fire stacks
off of you - Instead, it will clear 1 fire stack off of you every time
you roll, with a roll every 0.8 seconds.
balance: Stop, drop, and roll no longer stuns you for 6 seconds.
Instead, it will knock you to the floor while you are rolling. Moving
around or getting up will cancel the roll, and you cannot use items
while rolling around.
balance: Stop, drop, and roll will now repeat until the fire is put out
or you get up.
/:cl:

---
## [1393F/tgstation](https://github.com/1393F/tgstation)@[742971675d...](https://github.com/1393F/tgstation/commit/742971675de266aa4ebe671dc5175a5c543d93d7)
#### Monday 2023-11-20 00:16:52 by san7890

Fixes Relay Attackers Misfire (#79731)

## About The Pull Request

Fixes #76079

Basically we were both not getting all of the args that we recieve from
`COMSIG_ITEM_AFTERATTACK` which included the very important
`proximity_flag` which tells us if the person was in range to actually
hurt us or not. This means that clicking a mob with this element with a
stack of metal from across the room would cause them to aggro, which
makes no sense whatsoever. Let's actually use that proximity check.

We listen for projectiles hitting us separately, don't worry.
## Why It's Good For The Game

It just makes no damn sense, fixes some weird ass behavior. 
## Changelog
:cl:
fix: Bar Bots (and several other mobs) will no longer aggro on you if
you click on them with a "forceful" item from halfway across the room.
/:cl:

---
## [marin-robotics/genshin-bot](https://github.com/marin-robotics/genshin-bot)@[87ae7ae744...](https://github.com/marin-robotics/genshin-bot/commit/87ae7ae7440d498405572917f08cbffbf9fea02e)
#### Monday 2023-11-20 00:27:55 by MarinRobotics

timed move function for autonomous

I can't take it anymore. I'm sick of Xiangling. I try to play Diluc. My Xiangling deals more damage. I try to play Yoimiya. My Xiangling deals more damage. I try to play Cyno. My Xiangling deals more damage. I don't even try to play Dehya. I want to play Klee. Her best team has Xiangling. I want to play Raiden, Childe - they both want Xiangling. She grabs me by the throat. I fish for her. I cook for her. I give her the Catch. She isn't satisfied. I pull Engulfing Lightning. "I don't need this much er" She tells me. "Give me more field time." She grabs Bennett and forces him to throw himself off enemies. "You just need to funnel me more. I can deal more damage with Homa." I can't pull for Homa, I don't have enough primogems. She grabs my credit card. It declines. "Guess this is the end." She grabs Gouba. She says "Gouba, get them." There is no hint of sadness in his eyes. Nothing but pure, no icd pyro application. What a cruel world.

---
## [diphons/sdm845-419](https://github.com/diphons/sdm845-419)@[67f4613808...](https://github.com/diphons/sdm845-419/commit/67f46138080c5f808ede685202928ea8157b3c0b)
#### Monday 2023-11-20 00:43:44 by Peter Zijlstra

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
## [GoldenAlpharex/tgstation](https://github.com/GoldenAlpharex/tgstation)@[157fafeaa9...](https://github.com/GoldenAlpharex/tgstation/commit/157fafeaa95d4823c272326a37310a7017b206ef)
#### Monday 2023-11-20 00:46:13 by lizardqueenlexi

[CI Fix] The Demonic Frost-Miner will not attack corpses. (#79294)

## About The Pull Request

Fixes #79147.

Prevents the Demonic Frost-Miner from shooting at corpses by returning
early from `OpenFire()`. Also adds the "gutted" status effect to the
corpses in its arena so it won't try to gut them.
## Why It's Good For The Game

#78826 introduced an unfortunate bug by placing corpses in the Frost
Miner's arena. There were a combination of three factors at play here:
that the Miner attacks corpses, that it happens to use colossus bolts in
its attacks, which dust corpses, and that some unfortunate quirk of life
code causes runtimes if, as far as I can tell, a life tick goes off when
a mob is at the wrong point in the dusting process. The time this
process takes happened to perfectly coincide with the Monkey Business
unit test (being the first test that takes a significant period of
time), causing it to randomly fail.

So, this fixes a flaky test that has been a pain in the ass for the last
five days, is the big thing.

Also, it can't possibly have been intended for the Miner to run around
obliterating the aesthetic corpses in its arena within the first 15
seconds of any given round. Completely ruining the mood!

I'll point out that this particular boss may have been forgotten in
#77731, which set out to make only the colossus still gib/dust you, but
even were that not the case I think it would be a bit silly for the
Miner to be busy shooting lifeless corpses when a player shows up to
challenge it, rather than standing in its scary ritual circle.
## Changelog
:cl:
fix: The Demonic Frost-Miner will no longer run around destroying the
corpses in its arena the moment the round begins.
/:cl:

---
## [SethLafuente/tgstation](https://github.com/SethLafuente/tgstation)@[91af16bcbf...](https://github.com/SethLafuente/tgstation/commit/91af16bcbfd2dd363a89d846ae2acd6d655083c2)
#### Monday 2023-11-20 00:53:07 by zxaber

Adds Paddy, the Security Mech (#79376)

## About The Pull Request
- Adds a new combat mech, Paddy. Paddy is a modified Ripley MK-I,
intended for use by the station's security force. Like the MK-I, the
Paddy features an open-air cockpit design (and thus does not protect
from ranged weapons), but maintains the speed of the base unit.
Constructing a Paddy is similar to constructing a MK-II, though the kit
requires combat-mech level research. Sprites by
[DrDiasyl](https://github.com/DrDiasyl)
-- The paddy has an internal cargo bay capable of holding up to four
individuals (loaded with a hydraulic claw). If the pilot exits the
Paddy, any loaded individuals are likewise ejected. Individuals can
attempt to resist their way out of the mech, but it requires the mech to
be stationary for 45 seconds. If they do this, all individuals in the
holding cell are ejected.

- Adds a new mech equipment piece, the hydraulic claw. Similar to a
clamp, this Paddy-exclusive item can load mobs into the Paddy's cargo
bay. Humanoid mobs are handcuffed upon loading. The hydraulic claw is
unlocked on the same tech node as the Paddy.

- Adds a round-start Paddy, carrying one peacekeeper disabler and one
hydraulic claw, to each security area on all maps. Round-start Paddys
are also pre-locked with security access. Security now has access to a
mech charger, and a small bay for it all. Map edits were done by
[Maurukas](https://github.com/Maurukas).

- Also did some minor cleanup of various mech-related code. Ripley mech
cargo is no longer stored in the mech, but within the "ejector" object.
This doesn't have any player-facing changes, but it is easier to
organize behind the scenes. additionally, if Ripleys are destroyed now,
they drop their stored objects rather than deleting them.

## Why It's Good For The Game
Playing lone security is probably one of the least fun aspects of the
game. Arresting any assistant is inevitably setting yourself up against
the tide as a whole; You try to stun any one person and they crawl out
of the woodworks to get in your way, drag off the arrestee, and probably
try to steal your gear.

The Paddy is set up to be functional against low-threat targets, but not
particularly good against anything with purpose. The round-start Paddy
carries the disabler equipment, as well as the law claw, to detain
individuals in a *somewhat* safe manner. Being that you're inside an
exosuit, you're immune to shovespam that plagues the halls, and you
don't risk dropping important gear quite as easily.

However, The open canopy gives you no protection at all from ranged
attacks, nor from atmos hazards. Being that you're in an exosuit, you
cannot use other items or equipment. The AI will have trouble finding
you to open a door, due to your name not jumping their camera to your
location.
## Changelog
:cl: Zxaber, DrDiasyl, Maurukas
add: A new security-focused combat mech, the Paddy, has been added,
intended to be particularly helpful for lone sec officers. You will find
one in the Security main office, and a replacement can be built with
late-game mech research.
fix: Ripley MK-I and MK-II mechs no longer qdel their stored items when
destroyed.
/:cl:

![image](https://github.com/tgstation/tgstation/assets/37497534/72e6890d-82be-44dd-9b09-e4c75a9bfd4a)

---------

Co-authored-by: Vire <66576896+Maurukas@users.noreply.github.com>

---
## [DrAmazing343/tgstation](https://github.com/DrAmazing343/tgstation)@[81a7c75583...](https://github.com/DrAmazing343/tgstation/commit/81a7c75583f75f76d8487b88e63ebaf1402af85b)
#### Monday 2023-11-20 00:57:30 by necromanceranne

Hey what if I made Sleeping Carp better at nonlethal takedowns and also deflect with combat mode instead of throw mode (but cost more) (#79517)

## About The Pull Request

It's been a hot minute hasn't it?

When I initially reworked Sleeping Carp, we didn't have combat mode. Now
that we do, and that Sleeping Carp has substantially less defensive
power to justify having to make a choice between deflection and
attacking, it's probably about time we updated this aspect back to what
it was before my rework. Sorta.

Now, we can have all the deniability of the previous method, while also
letting you reliably protect yourself from ranged attacks at all times
while it matters. Because of this, I increased the price up to 17 TC
because of this change just to be on the safe side. The higher uptime of
projectile immunity while also being able to attack during that time
makes this a lot stronger overall.

Secondly, Sleeping Carp presently just isn't as good as a good ol'
baton. It takes a lot more hits to accomplish the same task that a baton
can. Many people feel like they can't even reasonably fight anyone for
fear of the baton, or they would rather use a baton and kill someone at
their leisure. So we've updated some of the moves in order to facilitate
Sleeping Carp as a substantial contender for 1v1 fighting, and lessen
the need for a baton by adding a lot more Stamina damage overall to the
various attacks;

**Keelhaul**: Now a Shove Shove combo. Does literally zero lethal
damage, but now temporarily blinds and dizzies the target as well as its
previous effects. The amount of lethal damage it did was...extremely
small, so this isn't a particularly big loss.

**Grabs and Shoves**: Deal some amount of stamina damage (20). You need
to be in combat mode in order to perform these special attacks (more
deniability). Grabbing someone while they have 80 Stamina damage or more
will cause them to fall unconscious. Yes, I really did just want to add
a Vulcan Nerve Pinch, what do you want from me?

That's it actually. Oh, I guess they are heavy sleepers now too. Because
its funny.

## Why It's Good For The Game

I often get told (read: thrown various insults and slurs at me while
mentioning this as the justification) that Sleeping Carp is not very
strong anymore since it lost all that invisible armor I added way back +
I removed the stuns in my initial rework. This made some people upset (I
think at least one person wished for my death).

So, having given it at least 2 years, I wanted to recapture parts of
what made the older Sleeping Carp (before my rework) strong, some of the
benefits of the new version, and introduce a brand new aspect; nonlethal
takedowns. This makes it beneficial for pacifists, as well as for
kidnapping.

This should not meaningfully make Sleeping Carp any stronger against the
things that typically ruin its day. I suspect in a straight joust with a
baton, Sleeping Carp will still struggle. But against what should be its
strong points (lone targets and ranged weapons), it will be strong once
again rather than clumsily unable to do very much at all.

## Changelog
:cl:
balance: Harnessing Shoreline Quay (bluespace energy, probably), a
mystical energy (total bullshit) that permeates the Astral Waterways
(bluespace quantum dimensions, probably), Sleeping Carp users can now
once against deflect projectiles with their bare hands when focused in
on battle (in combat mode).
balance: The Keelhaul technique is now nonlethal (a philosophical
acknowledgement of the familial bond of sleep and death), but causes the
target to become temporarily blind and dizzy along with its previous
effects.
balance: Sleeping carp users, while in combat mode, deal Stamina damage
with their grabs and shoves. If the target of their grab has enough
Stamina damage (80), they are knocked unconscious from a well placed
nerve pinch.
balance: Sleeping carp users find it very hard to wake up once they fall
asleep....
/:cl:

---
## [cam900/mame](https://github.com/cam900/mame)@[65ec4542ca...](https://github.com/cam900/mame/commit/65ec4542ca3c0092247ebcab86d21eff987e4472)
#### Monday 2023-11-20 01:02:30 by wilbertpol

msx2_flop.xml: Added 54 items (49 working) and replaced one item with a better dump. (#11698)

* Replaced VS Rotation (Japan) with a better dump. [file-hunter]
* Removed Ultima IV - Quest of the Avatar (Japan, alt disk 2) (disk 2 is from an English translation).
* Removed Vectron (Netherlands) and Vectron (Netherlands, alt) (extracted from a compilation).
* Removed Zoo (Netherlands, alt) and Zoo (Netherlands, alt 2) (hacked versions)

New working software list items (msx2_flop.xml)
-------------------------------
Konami Game Collection Bangai-hen (Japan, alt) [file-hunter]
The Legend of Shonan (Japan) [file-hunter]
Sailor-fuku Senshi Felis (Japan) [file-hunter]
Tempo Typen (Netherlands) [file-hunter]
Tenkyuhai Special - Tougen no Utage (Japan) [file-hunter]
Tenkyuhai Special - Tougen no Utage II (Japan) [file-hunter]
Thanatos (Japan) [file-hunter]
Tokimeki Sports Gal (Japan) [file-hunter]
Tominaga Koukou Tantei-bu (Japan) [file-hunter]
Trilogy Kuki Youka Shinden (Japan) [file-hunter]
The Tucs (Japan) [file-hunter]
Tulip Ichigou (Japan) [file-hunter]
Ultima II - The Revenge of the Enchantress (Japan) [file-hunter]
Undead Line (Woomb) [file-hunter]
Wizardry Scenario #3 - The Legacy of Llylgamyn (Japan) [file-hunter]
Xak - The Art of Visual Stage (Japan, Woomb) [file-hunter]
Yoshida Koumuten Data Library Vol. 2 (Japan) [file-hunter]
Yoshida Koumuten Data Library Vol. 3 (Japan) [file-hunter]
Yume Pro RPG Shaon-ban (Japan) [file-hunter]
Yumeji Asakusa-Kitan (Japan) [file-hunter]
Yuurei-kun (Japan) [file-hunter]
Zoo (Europe) [file-hunter]
GAME100 (Japan) [file-hunter]
Go! Volcano [NAGI-P SOFT]
Las Aventuras de Rudolphine Rur (Spanish) [Dwalin]
MSX Light [MSXdev]
Siege [NAGI-P SOFT]
Teddy's in Action Part 2 [file-hunter]
Terrahawks [file-hunter]
Tetravex (Netherlands) [file-hunter]
Tetris Master (Japan) [file-hunter]
Tetris Master - Operation Maison Ikkoku (Japan) [file-hunter]
Tetris Master - Operation Orange Road (Japan) [file-hunter]
Tetris Master - Operation Ranma 1/2 (Japan) [file-hunter]
Tetris Master - Series 1 Ranma 1/2 (Japan) [file-hunter]
Thunderbirds are Go (Netherlands, promo) [file-hunter]
Thunderbirds to the Rescue (Netherlands, promo) [file-hunter]
Tile Golf [NAGI-P SOFT]
Triplex (Netherlands) [file-hunter]
Trivial Pursuit (Netherlands) [file-hunter]
Trivial Pursuit - Aanvulling Jaareditie 1995 (Netherlands) [file-hunter]
Tunez: Garfield Edition [file-hunter]
The UHF Painter (Italy) [file-hunter]
War World FM-PAC Demo (Netherlands) [file-hunter]
Wiz Kids (Japan) [file-hunter]
Yupipati (demo) [file-hunter]
Zombie Night [Alberto Sgaggero]
Zoo Rally (Russia) [file-hunter]
Zoto (Germany?) [file-hunter]

New NOT_WORKING software list additions (msx2_flop.xml)
------------------------------------------
HBI-V1 Video Digitizer (Japan) [file-hunter]
Himitsu no Hanazono (Japan) [file-hunter]
Veldslag (Netherlands) [file-hunter]
Zeeslag (Netherlands) [file-hunter]
Zeeslag (Netherlands, demo) [file-hunter]

---
## [Imaginos16/Shiptest](https://github.com/Imaginos16/Shiptest)@[223dc74ef1...](https://github.com/Imaginos16/Shiptest/commit/223dc74ef1f528e2c29b0e62271ddaf7b68d79d8)
#### Monday 2023-11-20 01:02:48 by retlaw34

Eoehoma Firearms (& friends) (#2315)

## About The Pull Request


![Screenshot_5451](https://github.com/shiptest-ss13/Shiptest/assets/58402542/08f9b0ee-15db-4091-a974-6d887cd85259)

Holy shit, this should not have taken a year to make

Adds the E-10, E-11, E-40, E-50, and E-60 to the game. Weapons
manufactured by defunct firearms company Eoehoma Firearms.

Founded in 77 FS, Eoehoma was a early pioneer of ‘hybrid’ Solarian and
Kalixcian laser weapons. The company went bankrupt due to increasingly
poor and risky decision making, and all of it's patents were bought out
by Nanotrasen. While Nanotrasen's Emitters bear a striking resemblance
to the E-50, otherwise Nanotrasen has not produced any of Eoehoma's old
weapons, instead focusing on Sharplite designed weapons.

Other changes:
- NT and Sharplite weapons have different fire sounds from each other
- Laser weapons buffed to 20 -> 25 damage
- Pulse shots don't destroy walls and are now 50 -> 40 damage
- Emitter shots now do 30 -> 60 damage
- Various grammar fixes
- Removes some non-lore compliant mentions
- Adds a manufacturer indicator to many guns
- Ports https://github.com/tgstation/tgstation/pull/60353
- Resprites various laser weaponry, notably the pulse guns.
- Deathsquad and ERT/LP hardsuits have been redone

## Why It's Good For The Game


![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/c5df7029-95da-4041-b8b1-e4cfd35436dd)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/f72a3672-e996-4fdd-a68d-4553655f1a0c)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/7bd2dc53-ab29-49e8-8f90-87d4c72583f9)

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/4bdc6493-4c94-49d0-995b-2a450d738211)
ceredits to tetrazeta for the unfinished deathsquad sprite, i simply
finished it and touched it up

![image](https://github.com/shiptest-ss13/Shiptest/assets/58402542/517b72e3-c72b-4875-a6fb-84c017105908)

One of the last things i remember the old leads planned was to buff
lasers to make them stand up to the various ballistics better. Also
allows Pulse Rifles to be more used in events by nerfing them to not be
comedically overpowered. Now they are just Overpowered.

More ruin content and such. I'm sure the maptainers will make good use
of this stuff.

And sprites, i fucking love sprites

## Changelog

:cl: retlaw34, tetrazeta
add: Eoehoma Firearms, a new guns manufacturer!
add: ERT and "Asset Protection" Hardsuits have gotten a new look!
add: New laser fire sounds

balance: Lasers now do slightly more damage
balance: Pulse rifles don't destroy walls anymore and do slightly less
damage, and have lost their stun mode.
balance: Emitters do 60 damage and create turf fires on hitting a
non-supermatter object.
fix: Various laser weapons that had broken autofire (E-TAR and the Tesla
Cannon) now work

spellcheck: Grammar on some descriptions was corrected.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: retlaw34 <58402542+retlaw34@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>
Co-authored-by: thgvr <81882910+thgvr@users.noreply.github.com>

---
## [Imaginos16/Shiptest](https://github.com/Imaginos16/Shiptest)@[389d1e5669...](https://github.com/Imaginos16/Shiptest/commit/389d1e566990682f173066df4c16f25b3a1858c0)
#### Monday 2023-11-20 01:02:48 by Erika Fox

Does Penance So The Ghosts Go Away (#2442)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

"This is AI c-Caldwell - Reporting return of essential station functions
to Minya League Installation 'Trifuge' following pirate attack -
**///far too long ago///** - All vessels are invited to dock and partake
of our services, including an active Ore Refinery, world class bar, and
purchasable storefronts **//please come, I'm so lonely///** The Minya
League, and myself, would like to extend our gratitude to **///-who else
but me?///**. Installation 'Trifuge' is located in orbit of the Star
'Anselhome', at the L5 point of Anselhome and habitable world, 'Hofud'.
Noting active travel advisory - Hofud is currently **///nothing but ash
left by monsters///**. Independent Vessels are advised to avoid landing
until Minya League Ships can deliver disaster relief to the planet
**///not that they'll be coming....///**"

"This message will repeat in approximately 20 galactic standard minutes"

Remaps the shitty outpost 1 (indie space) outpost that I made like 6
months ago. it sucks. Anyone who doesn't think it sucks probably has
stockholm symdromed themselves into liking it. Also this one has lore
and room for expansion.
It's main features are: 
- Decent amount of maint for outpost antics
- REASONABLE amount of storefronts
-abandoned feel
- bar
- Ore refinery so my holy mandate can be implemented when I decide I'm
done with my break.

![2023-10-30 22 34
33](https://github.com/shiptest-ss13/Shiptest/assets/94164348/de3d93e2-e43b-478a-9d8c-7b44c972433d)
![2023-10-30 22 34
35](https://github.com/shiptest-ss13/Shiptest/assets/94164348/770109d4-1ab8-46b2-b3b8-e96c575cdde4)
There are your screenshots.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I'd like the voices in my walls to stop whispering to me about the
horrific mistakes I've made. They seem pretty upset about this one.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: Erika Fox
add: Outpost 1 has been remapped into something fathomably less ass.
It's a bit smaller, probably, but I'm going to call that a good thing.
add: random number spawner. It's good for hull numbers that shouldn't be
static.
imageadd: a really bad sprite for a service directions sign.
add: Another elevator template (coincidentally demonstrating how that
system works in code)

/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [Imaginos16/Shiptest](https://github.com/Imaginos16/Shiptest)@[88e683cec6...](https://github.com/Imaginos16/Shiptest/commit/88e683cec669624228d5204d7e3da06e6075d158)
#### Monday 2023-11-20 01:02:48 by zevo

Massive Ruin Fixes + Removals PR (#2334)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
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

## Why It's Good For The Game
Normally I'm all for remapping instead of removing ruins, but some ruins
are very much beyond saving. Clearing out space for better ruins to take
the spotlight is always nice. Some older ruins are fine but are missing
certain things or have loot that worked fine in the past, but doesn't
reflect the balance we want for ruins in the present.

I will be PR'ing ruins to replace the ones I remove.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[fae3366596...](https://github.com/treckstar/yolo-octo-hipster/commit/fae336659641db18376eef94db75dfc2834bcd4d)
#### Monday 2023-11-20 01:22:06 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [DrAmazing343/tgstation](https://github.com/DrAmazing343/tgstation)@[66b8b1d866...](https://github.com/DrAmazing343/tgstation/commit/66b8b1d8669379eac50fa358a3eb5e7707b46f25)
#### Monday 2023-11-20 01:26:34 by Fikou

Revert "if you die in a mech you are ejected" (#79768)

Reverts tgstation/tgstation#79380
this is literally what the mech removal tool is for. gameplay reasons
for that tool missing do not mean that we need to remove its use - if
you want a better solution then let people purchase it... or just smash
the mech- you saving their life and them being sad about their mech is
really funny
the original pr being marked as qol when that was a specific balance
change is very stupid

## Changelog
🆑
del: if you die in a mech you again don't automatically eject
/🆑

---
## [evmts/evmts-monorepo](https://github.com/evmts/evmts-monorepo)@[d6e92eecf2...](https://github.com/evmts/evmts-monorepo/commit/d6e92eecf224b3b5ba304c0c204e28cc2c8b82a2)
#### Monday 2023-11-20 01:41:40 by Will Cory

:sparkles: Feat(vm): Add precompiles as an option (#664)

## Description

[Norswap requested
precompiles](https://twitter.com/norswap/status/1724944291204665439).
Norswap gets precompiles.

With precompiles one will be able to write arbitrary javascript that
runs when a contract is called. They can even do gross stuff like append
to a dom. Fwiw this will also be how evmts cheat codes work but before
we weren't planning on exposing this to end users.

While implementing this feature I found an annoying bug. If you don't
include an argument in your precompile the entire thing fails to
execute. Opened pr to fix issue here
https://github.com/ethereumjs/ethereumjs-monorepo/pull/3158

The types are currently wrong. It takes an Ethjs address instead of a
HexString address unlike the rest of the evmts pr. This is because
patching the types as I wished was tediously hard as a result of
ethereumjs not exporting specific types I need. Later I will do a pr to
ethereumjs about this. For now we do some typescript magic to infer the
type but because of the type is a union type it's difficult to patch and
I gave up for now.

## Testing

Unit test testing a precompile

## Additional Information

- [ ] I read the [contributing docs](../docs/contributing.md) (if this
is your first contribution)

Your ENS/address:

Co-authored-by: Will Cory <willcory@Wills-MacBook-Pro.local>

---
## [notJoon/gno-core](https://github.com/notJoon/gno-core)@[24d89a4f5d...](https://github.com/notJoon/gno-core/commit/24d89a4f5debd3c1ae711e98587e1e32980e4347)
#### Monday 2023-11-20 02:49:33 by Morgan

feat(examples): add p/demo/seqid (#1378)

A very simple ID generation package, designed to be used in combination
with `avl.Tree`s to push values in order.

The name was originally `seqid` (sequential IDs), but after saying it a
few times I realised it was close to "squid" and probably would be more
fun if I named it that way ;)

There's another piece of functionality that I want to add, which is a
way to create simple base32-encoded IDs. This depends on #1290. These
would also guarantee alphabetical ordering, so a list of them can be
easily sorted and you'd get it in the same order they were created. They
would likely be 13 characters long, but I'm also thinking of making a
compact version which works from [0,2^35) which is 7 chracters, and then
smoothly transitions over to the 13 characters version when the ID is
reached.

(I've experience with both base64 and base32 encoded IDs as 64-bit
numbers, as I used both systems. The advantage of base32 is that it
makes IDs case insensitive, all the while being at most 13 bytes instead
of 11 for base64.)

In GnoChess, we used simple sequential IDs combined with
[`zeroPad9`](https://github.com/gnolang/gnochess/blob/7e841191a4a0a94c0d46bc977458bd6b757eab5e/realm/chess.gno#L287-L296)
to create IDs which were both readable and sortable. I want to make a
more "canonical" solution to this which does not have a upper limit at 1
billion entries.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[c63b233f42...](https://github.com/tgstation/tgstation/commit/c63b233f42a46d9373fd41b3f69edde3d2d48002)
#### Monday 2023-11-20 03:23:11 by _0Steven

Make sign language unaffected by the Social Anxiety quirk's direct speech effects (#79809)

## About The Pull Request

Alternative title: "Make going non-verbal make you less anxious."

This is a two line change to `social_anxiety.dm` to quit out its
`handle_speech` method when user has the `TRAIT_SIGN_LANG` trait.
This stops the Social Anxiety quirk from applying its
stutters/fillers/blockers for as long as the speaker is using sign
language.
This does nothing to any of social anxiety's non-verbal effects, those
are still active regardless and entirely unaffected.
## Why It's Good For The Game

Primarily: I think giving people the choice between using anxious talk
or sign language, and thus the different hurdles inherent to both, makes
for a more interesting gameplay interaction than simply blanket-applying
the quirk's speech effects to both.

Secondarily: Social Anxiety's non-verbal penalties are entirely
unaffected. One will still get the penalties from making eye contact and
occasionally make eye contact with objects. Notably this includes the
stuttering making eye contact could get you, which still makes your
signing shaky. You're still anxious, after all.
On top of this, it still costs more to pick up Signer than Social
Anxiety allows for, and thus the change doesn't simply make the
combination free points.

Tertiarily: when one has trouble speaking verbally, non-verbal
communication can be helpful in overcoming that hurdle. This is
especially so when the trigger for said anxiety is speaking verbally in
the first place. This is part of why I was so enamoured by the
combination before a broader and, mind you, fairly needed fix to sign
language made these interact differently.
## Changelog
:cl:
balance: signers no longer suffer from social anxiety's speech changes
when they go non-verbal. Other effects are maintained.
/:cl:

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[48b5a35dea...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/48b5a35deadc1cdeb19d117ee50702c76df0d275)
#### Monday 2023-11-20 03:27:12 by Bloop

[MISSED MIRRORS] Linters, part two (#25138)

* Split Run Linters step into multiple steps (#78265)

Splits the big "Run Linters" step into multiple steps. Also since all of
these steps are independent of eachother, I've made them all run
regardless of if the job is currently failing.

<details>
<summary>Proof of testing:</summary>

Fail in install tools, all linting steps are skipped:
https://github.com/distributivgesetz/tgstation/actions/runs/6151628214/job/16692089726
Fail in Run DreamChecker, other steps continue to run:
https://github.com/distributivgesetz/tgstation/actions/runs/6151664705/job/16692203569?pr=2
</details>

<details>
<summary>Pictured: me breaking CI for a day</summary>

https://github.com/tgstation/tgstation/assets/47710522/ea12ad30-2b69-4aa3-9642-7d0818eab2d1

</details>

Going through the Run Linters step has always been a slog. Finding an
error is like finding a needle in a haystack. Seeing what command
exactly went wrong is going to go a long way in helping people find out
which linters have failed.

nothing playerfacing

* Fixes TFE being useless after #78265 (#78433)

I thought `set +e` would still make the shell exit with an error if any
command failed, I didn't think that it would just use the exit code of
the last command. I am dumb, I'm an idiot and I want to cry.

* Update ci_suite.yml

* Fix some odd vscode highlighting errors in workflow files  (#78274)

few errors which were odd and annoying

stealing PRs from san7890, they wanted to do this
nothing playerfacing

* Only cancel concurrent CI in the same PR (#73398)

More merge queue bullshit. Cancels are counted as failures, and even
though on my test branch it worked completely fine, when trying on two
real PRs, it did not.

This makes it so merges into master might mess with CI clogging again,
but also merge queue is going to do that on its own, and the gain is
worth it.


![image](https://user-images.githubusercontent.com/35135081/218340666-6f937611-c47e-4122-b4b8-b84e8edcc1e9.png)

* Remove cache purge key that has never worked and has meant that our cache has never worked (#71529)

ci_suite.yml runs on your fork. This means you do not have access to
secrets. Every user has had the purge key of blank.

WE have it set to something. Which means the master cache that every PR
pulls from has been unable to match.

This means our cache has been at the max limit all this time, constantly
clearing out old caches, and never reusing any.

* Caches Node and Python Bootstrap for GH Actions (#78307)

## About The Pull Request

I was planning on doing this a lot earlier but ran into some weird
roadblocks, but this time I finally did the research and it's done
properly.

We do a lot of useless work on every single CI run, and in the interest
of saving the world's energy (by a matter of at least 10 seconds per my
testing), lets stop doing so much extra work by caching both the work we
do on the python bootstrap installation (we literally call it `cache`
for a reason) and the Node installation by sharing it between github
actions runners.

Here's a random CI run on master where you can see that the `Install
Tools` portion takes about 19 seconds -
https://github.com/tgstation/tgstation/actions/runs/6167104927/job/16737570519

Here's the CI run I was testing with where you can see we slim it down
to about 6 seconds for the `Install Tools` step, but with a second-or-so
taken to restore the cache since the runner needs to download+unzip the
cache. it tends to be shorter or longer by a second at times but i'm
certain this is just noise -
https://github.com/san7890/bruhstation/actions/runs/6167245722/job/16737919874

On average, we save about **10 seconds** a run on Run Linters, which is
meant to be the fastest CI step. Future improvements would lie in making
either maplint or the tgui test suite faster, but that would be a much
more complicated and code-intensive task. cache go weeeee

## Changelog

Nothing that concerns players.

* Conditionally run TGS tests (#73704)

Also add test merge support for pull requests

---------

Co-authored-by: distributivgesetz <distributivgesetz93@gmail.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jordan Dominion <Cyberboss@users.noreply.github.com>

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[17cba0dccf...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/17cba0dccfb57eb492fcfade92abc0065a07b356)
#### Monday 2023-11-20 03:27:12 by Bloop

[MISSED MIRROR] Puts all traits in the globalvars file + CI Testing (#79642) (#25131)

* Puts all traits in the globalvars file + CI Testing (#79642)

Fixes #76349

I didn't know that people needed to add any new traits to a global list
so they can be easily read in View Variables, and was pretty shocked to
find out many other people didn't know it was a thing. Let's make it a
thing by testing it using a new CI Python Linter to check this. But oh
no-

![image](https://github.com/tgstation/tgstation/assets/34697715/c093f1a8-00ce-40a6-8e1d-f344107ce7b8)

There were about 200+ missing traits. Alright, so let's do the
following:

* Move trait defines to their own dedicated folder in the `_DEFINES`
folder.
* Split up the traits mega-file into different files, for better
organization. One for the macros, one for the sources, and a few for the
"trait declarations"
* Run the linter a load of times and add everything to the globalvars
file, removing anything that's no longer used and figuring out where the
best categorization of it is. also minor code improvements. also rename
all of the ones that look weird. also fix list indentations
* Also alphabetize the lists because it's easy
* Move everything to a new `traits_by_type` list, while keeping the
admin one the way it is for the time being while we figure out a better
way to show that list to admins.
* Profit

Mapping trait injectors will now work for any type of trait. You
shouldn't add any trait via this injector though, but you're no longer
limited to coders remembering to add it to that critical list you
needed.

Lays the framework for a better view variables experience. This work is
too lengthy to presently do, but hopefully we can get this done sooner
rather than later. we will need a code-accessible way to view these
traits for such a framework to be implemented, so let's just do that.

Future steps are to break down the mega-declarations file into a folder
full of separate files by typepath, but that requires a lot of auditing.
Does need to happen one day though, there's a lot of mob traits mingled
with datum traits and auuugh we gotta do this later this PR is already
massive.

there's probably ways to game this but this catches _my_ mistakes so
good luck to everyone else (it should work for 99% of everyone)

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).

* Update tgstation.dme

* Update _traits.dm

* Comment these out for now

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Peco1503/mypictograms](https://github.com/Peco1503/mypictograms)@[37af466a3c...](https://github.com/Peco1503/mypictograms/commit/37af466a3ca72268f33d20dc7ec11fec62d6f5d0)
#### Monday 2023-11-20 04:21:21 by Peco1503

Avance Comunicador

Hell yeah bby, some frontend shit again, I'd say 30% done. Still need to implement the phrase creation logic depending on the users image choice

---
## [AEFeinstein/Swadge-IDF-5.0](https://github.com/AEFeinstein/Swadge-IDF-5.0)@[4e18144af4...](https://github.com/AEFeinstein/Swadge-IDF-5.0/commit/4e18144af4798e51829672cc1d8f46dec9ccb05c)
#### Monday 2023-11-20 04:30:47 by VanillyNeko

Add all Platformer music to Jukebox

Alright, I am a nuisance and I love my job LOL
This is honestly what happens when you have crackhead energy at 5 am and a friend says, Here do this and your like screw it why not? So, without further ado, here are all the music ones now too. I MIGHT be done with the torturous pushes now until Bryce or Adam is alive and can see what I did BWAHAHAHAHAHAHA

---
## [LOSModified/android_frameworks_base](https://github.com/LOSModified/android_frameworks_base)@[d322fab219...](https://github.com/LOSModified/android_frameworks_base/commit/d322fab219c800f310986cac8e73252c8affc41c)
#### Monday 2023-11-20 04:35:38 by Adithya R

telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [nvm-contrib/bevy](https://github.com/nvm-contrib/bevy)@[ab300d0ed9...](https://github.com/nvm-contrib/bevy/commit/ab300d0ed9990972679629af3ef18fd37c0e106c)
#### Monday 2023-11-20 05:54:40 by Connor King

Gizmo Arrows (#10550)

## Objective

- Add an arrow gizmo as suggested by #9400 

## Solution

(excuse my Protomen music)


https://github.com/bevyengine/bevy/assets/14184826/192adf24-079f-4a4b-a17b-091e892974ec

Wasn't horribly hard when i remembered i can change coordinate systems
whenever I want. Gave them four tips (as suggested by @alice-i-cecile in
discord) instead of trying to decide what direction the tips should
point.

Made the tip length default to 1/10 of the arrow's length, which looked
good enough to me. Hard-coded the angle from the body to the tips to 45
degrees.

## Still TODO

- [x] actual doc comments
- [x] doctests
- [x] `ArrowBuilder.with_tip_length()`

---

## Changelog

- Added `gizmos.arrow()` and `gizmos.arrow_2d()`
- Added arrows to `2d_gizmos` and `3d_gizmos` examples

## Migration Guide

N/A

---------

Co-authored-by: Nicola Papale <nicopap@users.noreply.github.com>

---
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[1c120f6584...](https://github.com/Monkestation/Monkestation2.0/commit/1c120f658417b4df06da8e79ceeb064eb0116647)
#### Monday 2023-11-20 06:49:35 by Jacquerel

Basic blob mobs (#78520)

I remembered today that blob code is ass, especially blob spores.
There's still a lot to improve but I cleaned up _some_ of it by
converting these mobs.
Now they use a newer framework and more signal handling as compared to
circular references.

I _expect_ the behaviour here to largely be the same as it was or
similar. I haven't added anything fancy or new.

This is a reasonably big PR but at least all of the files are small?
Everything here touched every other thing enough that it didnt make
sense to split up sorry.

Other things I did in code:
- Experimented with replacing the `mob/blob` subtype with a component.
Don't know if this is genius or stupid.
- AI subtree which just walks somewhere. We've used this behaviour a lot
but never given it its own subtree.
- Blob Spores and Zombies are two different mobs now instead of being
one mob which just changes every single one of its properties.
- Made a few living defence procs call super, because the only thing
super does was send a signal and we weren't doing that for no reason.
Also added a couple extra signals for intercepts we did not have.

:cl:
fix: Blob spores will respond to rallies more reliably (it won't runtime
every time they try and pathfind).
fix: Blobbernaut pain animation overlays should align with the direction
the mob is facing instead of always facing South
refactor: Blob spores, zombies, and blobbernauts now all use the basic
mob framework. They should work the same, but please report any issues.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[26645e92ff...](https://github.com/Monkestation/Monkestation2.0/commit/26645e92ff220b47178b37910dfd1838eb6cfc3d)
#### Monday 2023-11-20 06:49:35 by Ben10Omintrix

ice demon basic mobs (#78539)

ice demons are now basic mobs. they still have their behavior where they
can teleport around the player, run away from him and shoot him. they
now also have a new ability they will only use when they are on their
last legs, they will spawn weak and slow afterimage clones of
theirselves to attack the player. damaging these clones will also damage
the original ice demons. ice demons can also now be very easily
countered as they are very afraid of fires. they will run away from you
if they see u holding a lit torch/flare/welding tool and while running
away they will freeze the floors around them to try to slip u to stop u
from chasing them. ice demons now also get a new unique trophy! this
trophy will summon 2 friendly spirits that will help you kill ur target,
but these spirits will dissappear after a very short while.

https://github.com/tgstation/tgstation/assets/138636438/6a48fb15-f447-441a-91c6-48ca120dc22c

:cl:
refactor: ice demons have been refactored into basic mbos. please report
any bugs
add: ice demons now have a unique trophy
/:cl:

---
## [cosminh11/collabora-online](https://github.com/cosminh11/collabora-online)@[3185307c7a...](https://github.com/cosminh11/collabora-online/commit/3185307c7afa5e76bd10b76a2d97ecbdbc97455a)
#### Monday 2023-11-20 07:08:07 by Skyler Grey

Stop hiding both menu and notebookbar softlocking

Previously, when using the Collapse_Notebookbar postmessage or
equivalent ui_defaults (SpreadsheetToolbar=false, etc.), particularly in
compact mode, it was possible to additionally hide the menu bar. As the
button to show the menu bar is on the notebookbar, this meant that you
couldn't reactivate either notebookbar or menubar until you refreshed
the page. This is particularly annoying in integrators that may not
provide an easy way to reload the page

This commit makes it so that hiding the menu bar automatically
uncollapses the notebookbar and won't let it be collapsed again. Whether
the notebook bar should be collapsed (the last thing done to it was a
collapse) is remembered and restored after the menu bar is shown again,
so if you send a postmessage that will affect the state of the
notebookbar after the menu is shown (even though it will not affect the
notebookbar's state immediately)

Caveats:
- If you are hiding the notebookbar to limit the control the user has,
  that's broken by this commit as it makes it impossible to hide both
  the menu and notebook bars at the same time.
- The notebook bar will be hidden again when re-showing the menu bar,
  however there still isn't a way to hide the notebook bar in normal
  use (i.e. without using either postmessage or ui_defaults) while in
  compact mode (although there is a workaround to show it- switching
  into tabbed mode and then back!). It might be nice to have one.

Other considered solutions:
- We could add a new button that allowed you to reopen the menu if both
  menu and notebookbar were hidden
  - Not sure there's much benefit to this over just doing what we're
    doing here, and it's harder to implement
- We could disable the button to hide the menu bar when the notebookbar
  is collapsed
  - As far as I know, there's no button in the UI to show the notebook
    bar. This would make it impossible to hide the menu bar if the
    notebookbar was hidden via postmessage or ui_defaults

Signed-off-by: Skyler Grey <skyler.grey@collabora.com>
Change-Id: Ieab6d72a6be181aba88e9a5b21dda16a369b9e54

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[0141f96a13...](https://github.com/Time-Green/tgstation/commit/0141f96a1312dcf2326c28d73a7a91cefc8354c4)
#### Monday 2023-11-20 07:20:07 by Ephemeralis

Refactor icemoon wolves into basic mobs and add taming + pack behavior (#79736)

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

Co-authored-by: san7890 <the@san7890.com>

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[242acdf733...](https://github.com/pytorch/pytorch/commit/242acdf733eae97f986ac7d8c18bdc9eb02769fb)
#### Monday 2023-11-20 07:44:54 by voznesenskym

Update base for Update on "AOTAutograd: handle set_(), detect metadata mutations that cancel out"

This should be enough to get voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

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




cc voznesenskym penguinwu EikanWang jgong5 Guobing-Chen XiaobingSuper zhuhaozhe blzheng wenzhe-nrv jiayisunx chenyang78 aakhundov kadeng

[ghstack-poisoned]

---
## [1IMA-1IMB/kpnoran.github.io](https://github.com/1IMA-1IMB/kpnoran.github.io)@[d5bc316fc4...](https://github.com/1IMA-1IMB/kpnoran.github.io/commit/d5bc316fc4ac93a02c7e7b6302d5f9e4235b0def)
#### Monday 2023-11-20 07:56:45 by Ait

Lots of stuff has been done, no need to think about it

The Doctor who flux arc was shit, and I have had to make up an entire personal headcanon that makes it so that the Doctor was never part of "division" holy fuck chris chibnall, how could you fuck shit up that badly.

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[71b45e54ad...](https://github.com/lizardqueenlexi/orbstation/commit/71b45e54adfaa4c681babc545db97fa7103289de)
#### Monday 2023-11-20 08:47:53 by san7890

Puts all traits in the globalvars file + CI Testing (#79642)

## About The Pull Request

Fixes #76349

I didn't know that people needed to add any new traits to a global list
so they can be easily read in View Variables, and was pretty shocked to
find out many other people didn't know it was a thing. Let's make it a
thing by testing it using a new CI Python Linter to check this. But oh
no-


![image](https://github.com/tgstation/tgstation/assets/34697715/c093f1a8-00ce-40a6-8e1d-f344107ce7b8)

There were about 200+ missing traits. Alright, so let's do the
following:

* Move trait defines to their own dedicated folder in the `_DEFINES`
folder.
* Split up the traits mega-file into different files, for better
organization. One for the macros, one for the sources, and a few for the
"trait declarations"
* Run the linter a load of times and add everything to the globalvars
file, removing anything that's no longer used and figuring out where the
best categorization of it is. also minor code improvements. also rename
all of the ones that look weird. also fix list indentations
* Also alphabetize the lists because it's easy
* Move everything to a new `traits_by_type` list, while keeping the
admin one the way it is for the time being while we figure out a better
way to show that list to admins.
* Profit
## Why It's Good For The Game

Mapping trait injectors will now work for any type of trait. You
shouldn't add any trait via this injector though, but you're no longer
limited to coders remembering to add it to that critical list you
needed.

Lays the framework for a better view variables experience. This work is
too lengthy to presently do, but hopefully we can get this done sooner
rather than later. we will need a code-accessible way to view these
traits for such a framework to be implemented, so let's just do that.

Future steps are to break down the mega-declarations file into a folder
full of separate files by typepath, but that requires a lot of auditing.
Does need to happen one day though, there's a lot of mob traits mingled
with datum traits and auuugh we gotta do this later this PR is already
massive.

there's probably ways to game this but this catches _my_ mistakes so
good luck to everyone else (it should work for 99% of everyone)
## Changelog

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[eb246c21f6...](https://github.com/lizardqueenlexi/orbstation/commit/eb246c21f6eb5380dc56e5779fcd51d11437557c)
#### Monday 2023-11-20 08:47:53 by san7890

Fixes sending stuff to "Old" Chat (#79819)

## About The Pull Request

This functionality was removed in #79479
(e1c6cfdce89c7dbcd507d0c44803f5407a042a96), and we should still be
supporting the old chat anyways because it contains a plethora of useful
BYOND information that we still can really leverage (such as the
built-in profiler and stuff like that) and it's going to be painful to
do that if you have to keep spamming `fix-chat` to see OOC/ASAY while
alternating every damn time.
## Why It's Good For The Game

It's ugly but we still need it. There's a reason why we still have it.
## Changelog
:cl:
fix: "Old Chat" (AKA: The old-styled non-TGUI raw-HTMLesque chat that
you might see when it prods you with the "Failed to load fancy chat!"
issue) should now get all text messages as expected.
/:cl:

---
## [demusza/community](https://github.com/demusza/community)@[540c23382e...](https://github.com/demusza/community/commit/540c23382ed0d791740fdbee07932874adfeff5e)
#### Monday 2023-11-20 08:47:54 by patelana nadeema

 Bring Back Lost Lover +27656012591  Green River  Springdale  Do You Seek Love, Friendship London, England  Paris, France  Amsterdam, Netherlands  Barcelona .

Welcome, I'm thrilled the stars have brought you here. I'm a successful Psychic Reader based in South Africa - here to guide you through life's most complex and difficult matters. Whatever you're going through, I'm here to help you find your way forward. From a young age I realized I was blessed with a gift that enabled me to see and sense things others could not. Let me do the same for you as I have for so many others since 1995. Contact me to schedule an appointment or phone call reading.
PSYCHIC TRADITIONAL HEALER SPELL CASTER +27656012591 
People have relied on psychics, tarot readers, mediums, fortune tellers, and astrologers to help guide them through life for centuries. When making an important decision or you have questions about life, love, or career it helps to get insights into the future or your destiny to keep you on the right path. A real psychic see things clearly from a more elevated place to provide answers and give you quality advice. Even if you just want to know the meaning of a crazy dream you had last night, the best psychic Is available to help you.
contact +27656012591
websites https://za.pinterest.com/spelllovespells/

---
## [demusza/community](https://github.com/demusza/community)@[7e0584ef7d...](https://github.com/demusza/community/commit/7e0584ef7d932736fc21b5131f94c03b444ea9f5)
#### Monday 2023-11-20 08:52:35 by patelana nadeema

Create Join brotherhood  World Today +27733587735  Illuminati World Of Famous  in south Africa Luxembourg Macedonia, Malta, Moldova Bermuda Virgin Island Astatula  Clermont  Eustis  Fruitland Park  Groveland

We welcome you all in this society, the Illuminati become a member by filling out our form. Sign up with Agent Aarush  Membership benefits. I will help you register. Services: Illuminati members, Join illuminati, Sign up today. fees $1300
Join Illuminati Official - Illuminati Society For You
Join illuminati brotherhood and enjoy all the benefits like money, fame, new house, car. Join illuminati for money today illuminati membership society. Services: Love Spells, Lost Love Spells, bring back lost lover.
contact +27733587735

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[4024e30709...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/4024e307092b312ad33fd40da8d899bbfb9574a2)
#### Monday 2023-11-20 09:14:01 by KingkumaArt

Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) (#79803)

## About The Pull Request

Simply put, due to how "caseless" is an element added to the ammo when
it hits something, but ammo is qdeleted upon hitting someone. If shot
point blank without combat mode (for some reason) it tries to add
caseless to an ammo that no longer exists. For some reason, the result
of this is to just fucking crash DS instead of aborting the adding of
the element. The ammo isnt reusable anymore, but I'll take that over
crashing.

## Why It's Good For The Game

Removes a game-breaking bug. I hate gun ammo code so much. 

## Changelog



:cl:
fix: Stopped a DS crash when shooting a rebar crossbow in specific
circumstances.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [almudenasanz/kibana](https://github.com/almudenasanz/kibana)@[cd909f03b1...](https://github.com/almudenasanz/kibana/commit/cd909f03b1d71da93041a0b5c184243aa6506dea)
#### Monday 2023-11-20 09:37:08 by Kyle Pollich

[Fleet] Fix inability to upgrade agents from 8.10.4 -> 8.11 (#170974)

## Summary

Closes https://github.com/elastic/kibana/issues/169825

This PR adds logic to Fleet's `/api/agents/available_versions` endpoint
that will ensure we periodically try to fetch from the live product
versions API at https://www.elastic.co/api/product_versions to make sure
we have eventual consistency in the list of available agent versions.

Currently, Kibana relies entirely on a static file generated at build
time from the above API. If the API isn't up-to-date with the latest
agent version (e.g. kibana completed its build before agent), then that
build of Kibana will never "see" the corresponding build of agent.

This API endpoint is cached for two hours to prevent overfetching from
this external API, and from constantly going out to disk to read from
the agent versions file.

## To do
- [x] Update unit tests
- [x] Consider airgapped environments

## On airgapped environments

In airgapped environments, we're going to try and fetch from the
`product_versions` API and that request is going to fail. What we've
seen happen in some environments is that these requests do not "fail
fast" and instead wait until a network timeout is reached.

I'd love to avoid that timeout case and somehow detect airgapped
environments and avoid calling this API at all. However, we don't have a
great deterministic way to know if someone is in an airgapped
environment. The best guess I think we can make is by checking whether
`xpack.fleet.registryUrl` is set to something other than
`https://epr.elastic.co`. Curious if anyone has thoughts on this.

## Screenshots


![image](https://github.com/elastic/kibana/assets/6766512/0906817c-0098-4b67-8791-d06730f450f6)


![image](https://github.com/elastic/kibana/assets/6766512/59e7c132-f568-470f-b48d-53761ddc2fde)


![image](https://github.com/elastic/kibana/assets/6766512/986372df-a90f-48c3-ae24-c3012e8f7730)

## To test

1. Set up Fleet Server + ES + Kibana
2. Spin up a Fleet Server running Agent v8.11.0
3. Enroll an agent running v8.10.4 (I used multipass)
4. Verify the agent can be upgraded from the UI

---------

Co-authored-by: Kibana Machine <42973632+kibanamachine@users.noreply.github.com>

---
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[503c0d42ea...](https://github.com/argilla-io/argilla/commit/503c0d42eab2d617f7e556789c6f3c4b091ef0f9)
#### Monday 2023-11-20 09:40:30 by David Berenstein

docs: changed some warning to more friendly notes (#4108)

<!-- Thanks for your contribution! As part of our Community Growers
initiative 🌱, we're donating Justdiggit bunds in your name to reforest
sub-Saharan Africa. To claim your Community Growers certificate, please
contact David Berenstein in our Slack community or fill in this form
https://tally.so/r/n9XrxK once your PR has been merged. -->

# Description

changed some warning to more friendly notes

Closes #4107

**Type of change**

(Remember to title the PR according to the type of change)

- [X] Documentation update

**How Has This Been Tested**

(Please describe the tests that you ran to verify your changes.)

- [X] `sphinx-autobuild` (read [Developer
Documentation](https://docs.argilla.io/en/latest/community/developer_docs.html#building-the-documentation)
for more details)

**Checklist**

- [X] I added relevant documentation
- [X] I followed the style guidelines of this project
- [X] I did a self-review of my code
- [X] I made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] I filled out [the contributor form](https://tally.so/r/n9XrxK)
(see text above)
- [X] I have added relevant notes to the `CHANGELOG.md` file (See
https://keepachangelog.com/)

---
## [sathish07sk/Web3-Blockchain](https://github.com/sathish07sk/Web3-Blockchain)@[5f571ed407...](https://github.com/sathish07sk/Web3-Blockchain/commit/5f571ed407792fb20d634b53be386adb5967c13f)
#### Monday 2023-11-20 10:01:22 by sathish07sk

Add files via upload

Build a Web-side with Web 3.0 with blockchain and
next.js , solidity sanity i.o. Sample twitter web-site used for social 
networking platform where people can express their thoughts in short 
posts which people can read and share! Read a News some information. 
This project consept is using for future coding technology it call as web 
3.0. Today, we are going to make the web-site for tweet consept using 
Next JS in the frontend along with Html, Css , javascript. And back-end 
with sanity i.o. Tailwind Css is designsystem implementation in pure Css. 
It is also configurable. It Gives Developers Super power. It allows them to 
Build websites with a clean consistent UI. MetaMask is the trailblazing 
tool enabling user interactions and experience on Web3. It is currently 
available as a browser extension and as a mobile app on both Android and 
iOS devices. The purpose of this documentation is to illustrate how to build 
a dapp with MetaMask. Sanity i.o use Back-end Database. Next.js gives
you the best developer experience with all the features you need for
production: hybrid static & server rendering, TypeScript support, smart 
bundling. This Web-site very style and look cool color.

---
## [MalleeFoul/homebrew-etc](https://github.com/MalleeFoul/homebrew-etc)@[ec41df4368...](https://github.com/MalleeFoul/homebrew-etc/commit/ec41df4368bcfeb4f425f73bc7bb33842c124f7e)
#### Monday 2023-11-20 11:31:42 by MalleeFoul

man this is a fucking pain
I should honestly just learn coding at this point tbh

---
## [MohammadReza9877/stable-diffusion-webui](https://github.com/MohammadReza9877/stable-diffusion-webui)@[4a1bb26af6...](https://github.com/MohammadReza9877/stable-diffusion-webui/commit/4a1bb26af6ee0d3cf34267a2f5283915d6645825)
#### Monday 2023-11-20 12:19:28 by MohammadReza9877

Create Malek

Once upon a time in the land of ImagiNATION, there existed a quaint little village called Desireville, where the air was always filled with the sweet scent of dreams and the streets were lined with the colorful aspirations of its inhabitants. In this village, there lived a young and ambitious inventor named Leo, who had a burning desire to create something truly remarkable.

Leo had always been fascinated by the stars and the mysteries of the universe. He spent countless nights gazing at the twinkling lights above, longing to unravel their secrets. One day, as he wandered through the village square, he stumbled upon an ancient book in the local library. The book was titled "The Wonders of the Cosmos" and contained detailed descriptions of a legendary artifact known as the "Wishful Star."

According to the book, the Wishful Star was said to possess the power to grant the deepest desires of those who sought it. Excited and inspired, Leo made it his mission to build a device that could lead him to this fabled star.

Armed with determination and a knack for invention, Leo toiled away in his workshop, fashioning gears, wires, and all manner of peculiar contraptions. Days turned into weeks, and weeks into months, until finally, Leo unveiled his masterpiece—a wondrous machine with shimmering crystals and pulsating energy—a Cosmic Compass, capable of pointing the way to the Wishful Star.

Equipped with his newfound invention, Leo embarked on a daring journey across the rolling hills and misty forests, braving the trials of the Enchanted Valley and the riddles of the Whispering Woods. Along the way, he encountered curious creatures and helpful companions, each with their own unique dreams and wishes.

After a series of perilous adventures, Leo reached the summit of Mount Lumina, where, guided by the Cosmic Compass, he laid eyes upon the elusive Wishful Star. It bathed the entire mountaintop in a mesmerizing glow, and whispers of unspoken desires filled the air.

As Leo approached the star, he realized that the true power of the Wishful Star lay not in granting wishes outright, but in awakening the courage and determination within individuals to pursue their aspirations. With a newfound understanding, Leo returned to Desireville, where he shared his story with the villagers, inspiring them to chase their dreams with renewed vigor.

And so, in the village of Desireville, each resident found the courage to pursue their heart's desires, knowing that the true magic lay not in the granting of wishes, but in the journey towards them.

---
## [Nokhte/nokhte](https://github.com/Nokhte/nokhte)@[9103afb8c4...](https://github.com/Nokhte/nokhte/commit/9103afb8c41088ca9bc6ff06e761f9074d4ff2c7)
#### Monday 2023-11-20 12:28:37 by Sonny Vesali

updated onUpdate api to be based on stopwatch api

we'll do wide spanning impl later with a general class but
the problem was that the detection for when things finish STINKS
I mean like hot ass, like worst thing on planet earth when things
stop / start / swap new movies it's awful and we did this ugly work-
around where we had count variables and then we do delays as well in
the rest of our app all because of this simple bug we even thought mobx
as the problem but it was simple_animations, I'm so pissed I don't even
want to do a PR

---
## [Danda420/kernel_xiaomi_sm8250](https://github.com/Danda420/kernel_xiaomi_sm8250)@[d15f7d49ac...](https://github.com/Danda420/kernel_xiaomi_sm8250/commit/d15f7d49ac13f8f549e31f3e2813a479b8b8e7d4)
#### Monday 2023-11-20 12:42:07 by Angelo G. Del Regno

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

---
## [Warfan1815/PvE-CMSS13](https://github.com/Warfan1815/PvE-CMSS13)@[e4c3900e4f...](https://github.com/Warfan1815/PvE-CMSS13/commit/e4c3900e4f087444308138e9d05b4da9c774f6a9)
#### Monday 2023-11-20 12:54:59 by riot

reduces timer on joining ert after death to 30 seconds (#4652)

# About the pull request

reduces timer

# Explain why it's good for the game

Having to wait a full minute to join an ERT is annoying, it was better
b4 when timer from ERT was a minute as well, but 30 second ERT means if
u die just b4 ERT goes you cant join regardless.

if ppl are ghosting bc they want ert then they are stupid.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Timer on attempting to join ERT after death is now 30 seconds
down from 1 minute
/:cl:

---
## [Warfan1815/PvE-CMSS13](https://github.com/Warfan1815/PvE-CMSS13)@[de5c69661f...](https://github.com/Warfan1815/PvE-CMSS13/commit/de5c69661f8d33425123894028702f64239f861b)
#### Monday 2023-11-20 12:54:59 by kiVts

DFB property changes. (#4590)

# About the pull request
part 2 out of 4 
This does a **big** touch up on defibrillation property in research

Well, to start off, max_level = 1 was removed. It appears warcrimes
forgot to remove it since process proc has benefits explicitly for
higher levels. I would call it a bug(oversight rather).

Second: Ghosts get notified when the chem starts to try and defib you,
so you dont just wonder how did you stand up, and pretty neat too.

Third: The >6 level of defib to apply healing like with actual item
defib is too high, so we move requirement down to >1 but make it heal
much, much worse at levels lower than 5.
eg it took 20 units to heal ~20 brute at level 3(you will literally
perma lmao), at level 5, however, this will go at around 2.5 per life
tick, level 8 will give 4 damage heal.
This is a balance change(buff) But hardly so since its research,
Research is already neglecting most of the time this property.

Fourth: removes one letter var, This whole file is entombed with them
but Im not doing that for now.

# Explain why it's good for the game


Defib property is way too underused and crudely made. This fixes it,
partially.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: kiVts
add: Ghosts get notified when they are being revived by DFB property
balance: DFB property healing threshold lowered, You can create DFB
property higher than one.
/:cl:

---------

Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[492ed90f28...](https://github.com/tgstation/tgstation/commit/492ed90f28dfd213e9438509653727f788efcebd)
#### Monday 2023-11-20 13:07:52 by necromanceranne

Fixes body collision causing a stun, despite a successful block. (#79824)

## About The Pull Request

Puts a block check into the ``throw_impact()`` of carbon mobs. 

## Why It's Good For The Game

I'm touching on a lot of 'get around shields' stuns, and this has been a
big one for the better part of a few years and potentially not even
intentional. I would say it gained its largest popularity when it became
weaponized with fireman carrying.

Despite seemingly rolling to block, blocking a body hitting you doesn't
actually do anything at all. This reminds me a bit of energy bolas. So I
fixed it? I think, there might be a better fix, I'm just replicating
code present in xenomorph tackles. This shit sucks, please recommend a
better fix if you know it.

## Changelog
:cl:
fix: When you successfully block a body collision, it does something
rather than nothing at all.
/:cl:

---
## [depoz0/G2station](https://github.com/depoz0/G2station)@[30dae8899b...](https://github.com/depoz0/G2station/commit/30dae8899bad0007ae9220f1fc10be16908dd1a9)
#### Monday 2023-11-20 14:22:39 by Kyle Spier-Swenson

fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#79783)

This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

---
## [metabrainz/musicbrainz-server](https://github.com/metabrainz/musicbrainz-server)@[41b5efc95c...](https://github.com/metabrainz/musicbrainz-server/commit/41b5efc95c13ee269e436a9864744de6d81bf7ca)
#### Monday 2023-11-20 14:27:59 by Michael Wiencek

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
## [Maybe-Anton/Shiptest](https://github.com/Maybe-Anton/Shiptest)@[b58b3abe4f...](https://github.com/Maybe-Anton/Shiptest/commit/b58b3abe4ffd26c63adb349f873ededfda5781a6)
#### Monday 2023-11-20 14:29:47 by zevo

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
## [Dominicentek/Saturn](https://github.com/Dominicentek/Saturn)@[90fdc25ec9...](https://github.com/Dominicentek/Saturn/commit/90fdc25ec95bfadea16abbf930cd47e7cb38c3bd)
#### Monday 2023-11-20 14:31:18 by Dominicentek

im so fucking dumb holy shit

Signed-off-by: Dominicentek <69892109+Dominicentek@users.noreply.github.com>

---
## [dagger/dagger](https://github.com/dagger/dagger)@[80180aaaed...](https://github.com/dagger/dagger/commit/80180aaaed1e1e91a13dbf7df7e0411a9a54c7d3)
#### Monday 2023-11-20 14:49:53 by Justin Chadwell

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
## [TMarccci/naplo](https://github.com/TMarccci/naplo)@[a7f1681902...](https://github.com/TMarccci/naplo/commit/a7f1681902f4a04085503f9118c5cee34d44b749)
#### Monday 2023-11-20 15:14:34 by Kima

someone commented birthday greeting, fuck yourself

---
## [PennyLaneAI/pennylane](https://github.com/PennyLaneAI/pennylane)@[47e74e16d0...](https://github.com/PennyLaneAI/pennylane/commit/47e74e16d0fb27aedc5ffab69aefaf5188115038)
#### Monday 2023-11-20 15:19:40 by Matthew Silverman

simplify state reordering logic (#4817)

**Context:**
I wrote the same function twice, differing only by state flattening, to
get the DQ upgrade done. It's starting to cause trouble.

**Description of the Change:**
Greatly simplified the state re-arrangement logic. There used to be a
whole mess of things happening, but now things are much more
straightforward.
1. `simulate` first puts things in our "standard" order, and this means
that if any measured wires are not also operator wires, they are put to
the _end_ of our tape wires. Therefore, for each measured-only wire, we
just have to stack a `zeros_like(state)` to the last axis of our final
state! `simulate` never tried to transpose wires back to a different
ordering, so that was always wasted work.
2. `StateMP.process_state` _always_ receives the full state, and never
needed to pad. No other device has done this optimization (the function
used to literally just `return state` before DQ2 migration), and
`simulate` already ensures that the final state has all wires in it -
they just might be out of order. The only thing we might need from
`process_state` is a transposition to the correct wire order. The
inputted `wire_order` _should_ always be `range(len(wires))`, but
whatever, we don't need to assume that.

I'll paint a picture for a normal scenario:

```python
@qml.qnode(qml.device("default.qubit", wires=3))
def circuit(x):
    qml.RX(x, 0)
    qml.CNOT([0, 2])
    return qml.state()
```

What happens with this QNode?
1. Device preprocessing sticks the device wires (`[0, 1, 2]`) onto the
`StateMP`
2. `simulate` maps the wires to our standard order. I'll demonstrate
(with `probs` so I can specify wires):

```pycon
>>> qs = qml.tape.QuantumScript([qml.RX(1.1, 0), qml.CNOT([0, 2])], [qml.probs(wires=[0, 1, 2])])
>>> qs.map_to_standard_wires().circuit
[RX(1.1, wires=[0]), CNOT(wires=[0, 1]), probs(wires=[0, 2, 1])]
```

3. Operate on the 2-qubit state, then stack another `[[0, 0], [0, 0]]`
on the end of it (wire "1")
4. `StateMP(wires=[0, 1, 2]).process_state(state, wire_order=[0, 2, 1])`
transposes the result to the correct order

I also changed the torch tests to stop using a deprecated setter for
default float types.

**Benefits:**
Duplicate code is cleaned up, existing code is simplified, no
unnecessary call to transpose.

**Possible Drawbacks:**
- Have to call `qml.math.stack` for every wire that was not operated on.
Hopefully this is usually not a lot, and it's not that costly anyway
- functions now do less than they used to (I see this as a perk - they
now do _exactly_ what they're supposed to)

---
## [kwubbenhorst/copy-that-dish](https://github.com/kwubbenhorst/copy-that-dish)@[d3b5e6c95a...](https://github.com/kwubbenhorst/copy-that-dish/commit/d3b5e6c95ad50b0ed3675470f058705a5feba993)
#### Monday 2023-11-20 16:00:18 by kwubbenhorst

Added new folder monday_morn_updates which is most developed version, changes to css, js(added click listener functionality throughout, modal functionality to confirm favouriting on p2, fully functional list generation on p3, clear feature that displays the carousel and credits), just waiting for list group menu items and cocktail feature to be integrated on p2 (Dan, Allan) and Nick and Patrick are free to adjust recipe card on p2 and local storage functionality on p3 to integrate their work.My next steps will be to address the improperly rendering title and blurb on right column p2, to add a modal to p1 to deal with the case of a search string that returns no results. Will then address missing functionality on p2. Will start on writing the readme no later than 2 and hope we can deploy no later than 4 in order to troubleshoot any deployment issues that arise. We can still make changes to repo after deployment and deployed page will reflect them. From 4 till 6.30 I'll be prepping my part in the presentation. We should probably have another working api key on hand in case the currently loaded one reaches its quota with all the application tests we are doing today. Wouldn't want it to fail just as we are trying to demo it to the class.

---
## [valibm/holbertonschool-low_level_programming](https://github.com/valibm/holbertonschool-low_level_programming)@[3a4f7e7fcb...](https://github.com/valibm/holbertonschool-low_level_programming/commit/3a4f7e7fcb9a7c193344de85524aa20c0840bef6)
#### Monday 2023-11-20 16:22:38 by root

Handled the stupidest of the error whic is not even worth to mention anyways i hate my life

---
## [Moltijoe/Yogstation](https://github.com/Moltijoe/Yogstation)@[bc3374c7da...](https://github.com/Moltijoe/Yogstation/commit/bc3374c7dacf3b2db39fe1c4dc36551d7ba82f79)
#### Monday 2023-11-20 17:23:10 by cowbot92

Even Further Heretic Adjustments: New minor things, Bug fixes, Heretic path adjustments and movement adjustments! (#20843)

* a whole lot of shit

yessir

* gun stuff

crazy

* haha

fuck guns

* my brain bursts

it hurts

* so much shit

im done

* fuck forgot this

god damn low memory mode

* removes backslashes

really linter

* oops

typos

---
## [Moltijoe/Yogstation](https://github.com/Moltijoe/Yogstation)@[f39d74c3a6...](https://github.com/Moltijoe/Yogstation/commit/f39d74c3a66c41a5ebb468dc3d61b0787f8327be)
#### Monday 2023-11-20 17:23:28 by Waterpig

Invisible touch - this time for real (#20742)

* This was surprisingly easy

* Well this might be funny

* Hm

* Oh boy it's working

* I might be going insane

* Checks moved

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[d751e1c642...](https://github.com/timothymtorres/tgstation/commit/d751e1c64246612f02089bc4059f3dc686edad2a)
#### Monday 2023-11-20 17:31:09 by DaCoolBoss

Adds garbage dumpster ruins (#79446)

## About The Pull Request
Adds 4 small space ruins. Each is a dumpster in space containing hostile
mobs to fight and items to bring back to the station. There's a
decommissioned garbage truck pulling each dumpster which acts as a
staging area before you take on the mobs inside.
All the fights are in cramped dark areas with full pressure, air is
breathable but sometimes has miasma in it so beware of getting sick. So
you can drop your space suit and put on armour, but PKAs won't fire at
full power and keeping a gas mask on is recommended.
Also all the dumpsters look the same from the outside so you gotta crawl
inside to know what's inside. And no you can't metagame it with mesons
either.

Comes in the following flavours:
Food Waste
Full of trash from kitchens, and food. Some of the food is still edible.
There's a lot of territorial rats. You can chop them up into meat if you
want more food. The big prize is a big vat of cooking oil.

Medical Waste
Spare organs, cyberorgans and almost a full set of old surgical gear.
There's a syndicate agent here up to no good and he has a GUN. The gun
blows up when the agent dies so you can't get it. There's a few corpses
of different species in bodybags and some spare corpse parts so you can
bring them back to the station and give them to the coroner. Also a
single use eyestealer in a safe (the cool way to do surgery) and a bug
from the old traitor objective that doesn't do jack but can probably
still get you thrown in perma.

Construction Garbage
Tools and construction materials here, including a cool hammer that fits
in a tool belt and can function as a crowbar. There's also a drug lab
with plenty of weird pills to eat, cigarettes to eat and an angry
russian drug dealer who will stab you if he sees you. He has a badass
lighter and a flamethrower you can take after you kill him. Setting fire
to things in here is not recommended because of all the welding fuel.

Mall Trash
Action figures, trading cards, Christmas crackers and other trash the
local mall tossed out. Also a mothman used to live here but he got eaten
by giant spiders so you can grab his stuff, including snacks and a
civilian modsuit with no mods (wow). You can cut through the webs to
kill the spiders or let them eat you too if you want.
## Why It's Good For The Game
More content for space explorers.
More variety to the potential dangers of space, now u can get sick and
die or get eaten by rats (this is hobo RP)
Better environmental storytelling. Now instead of players left asking
"what happens to the garbage when it goes into space" they can rest
assured that there's busted ass garbage trucks in space. All their
questions are answered.
Loot that encourages working with people on the station. Raw food for
the kitchen, rats for genetics, organs for the coroner, etc
## Changelog
:cl:
add: 4 new space ruins
/:cl:

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[a5fabd8819...](https://github.com/timothymtorres/tgstation/commit/a5fabd881961cc0c26fdcc93a23a973af1c5cdc3)
#### Monday 2023-11-20 17:31:09 by Profakos

Changes to the lore of Knock (#79542)

## About The Pull Request

This PR renames Knock to Lock, and changes most of the knowledge gain
lore.

## Why It's Good For The Game

The Knock Lore, is based on the Knock Principle from Cultist Simulator,
with the path description being copied from the wiki. Many other
keywords and concepts are fully lifted from that game (Locksmith's
Secret, Mother Of Ants, etc). In my vision, if a heretic path has to be
based on a principle from cultist simulator, it should have its own
spin, and also, the knowledge gain texts should tell a story. For
example, Ash tells the story of a watchman burning down their city after
being betrayed, and Cosmic is a love story between a knowledge seeker
and a monster from the beyond.

So I have decided to reflavour Knock. I have changed the name to Lock,
so at least it would feel similar, just like how Blade is akin to Edge.
Many powers also block people or confuse their paths instead of opening
new ways, and thus, I feel a path whose name implies that it *both*
opens and closes would be more self describing.

I have changed most of its lore to be about the Locked Labyrinth, where
knowledge seekers willingly trap themselves and submit themselves to
servitude to find ultimate freedom by progressing through its trials.
These are the Stewards, who are basically workers in an infinite and
malicious hotel in their dreams. Consider them assistants if you will
(this wasn't my intention when I wrote the lore, but thinking about it
in retrospect, it honestly fits). In the implied story, the heretic
joins their ranks, but keeps getting closer to the more corrupt members,
along with parasitic spirits. Ultimately, they manage to open the
Labyrinth's core, letting out the Stewards, allowing them to manifest in
the forms of heretic summon creatures.

The side path spells and the lock knowledge ritual I have not touched,
they were fine. Some items have been renamed and repathed.

I have kept the distinctive sound effect for using the Grasp, as its
unique enough. Though if someone did have a nice sound effect for
turning a lock and added some filters, I would add it.

**DB Issue**

I have renamed the achievement's define to MEDAL_LOCK_ASCENSION but kept
the value as "Knock", as I don't know how trigger a change in the DB. If
this is a blocking change, I'll try to figure out how to make a
migration file.

**Future improvements**

I would also come back later with another PR, that hands out names to
the eldritch beings spawned by the portal, based on the Stewards in the
knowledge gain lore that I added, along with some new ones that fit the
theme, and some jokey ones like Minotaur.

## Changelog

:cl:
spellcheck: Renamed Knock to Locks, and changed most of the flavor text
of knowledge gain, and renamed some items and knowledges from the path.
/:cl:

---
## [jpbandroid/reactos-pulls](https://github.com/jpbandroid/reactos-pulls)@[cc63d8f4a2...](https://github.com/jpbandroid/reactos-pulls/commit/cc63d8f4a2c3e4e22dd3f4c706e2373978914b68)
#### Monday 2023-11-20 17:34:35 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

---
## [joreenmay006/app-dev](https://github.com/joreenmay006/app-dev)@[6105737b9d...](https://github.com/joreenmay006/app-dev/commit/6105737b9dbbef3f4f06a4dd1dc465470f185a0a)
#### Monday 2023-11-20 17:36:48 by joreenmay006

Update README.md

In "Beauty and the Beast," Belle, this smart and kind gal, gets stuck in a magical castle because her dad's in a jam. At first, she's freaked out by the Beast who lives there, but then she sees he's not so bad and befriends his enchanted furniture friends. They fall in love, break the curse with some true love magic, and bam, Beast turns back into a prince, and the castle's back to normal.

---
## [llvm/llvm-project](https://github.com/llvm/llvm-project)@[5cd24759c4...](https://github.com/llvm/llvm-project/commit/5cd24759c41864215e67c280234b6c745a4cd369)
#### Monday 2023-11-20 18:28:02 by Louis Dionne

[libc++] Reduce the compilation time required by SIMD tests (#72602)

Testing all the SIMD widths exhaustively is nice in theory, however in
practice it leads to extremely slow tests. Given that
1. our testing resources are finite and actually pretty costly
2. we have thousands of other tests we also need to run
3. the value of executing these SIMD tests for absolutely all supported
SIMD widths is fairly small compared to cherry-picking a few relevant
widths

I think it makes a lot of sense to reduce the exhaustiveness of these
tests. I'm getting a ~4x speedup for the worst offender
(reference_assignment.pass.cpp) after this patch.

I'd also like to make this a reminder to anyone seeing this PR that
tests impact everyone's productivity. Slow unit tests contribute to
making the CI slower as a whole, and that has a direct impact on
everyone's ability to iterate quickly during PRs. Even though we have a
pretty robust CI setup in place, we should remember that it doesn't come
for free and should strive to keep our tests at a good bang for the buck
ratio.

---
## [ShockWaveGamer/WFCLevelGeneration](https://github.com/ShockWaveGamer/WFCLevelGeneration)@[47bd7c10bb...](https://github.com/ShockWaveGamer/WFCLevelGeneration/commit/47bd7c10bb4b99cfdda85af9da27087e54a872d7)
#### Monday 2023-11-20 18:36:49 by ShockWaveGamer

Broken Finding Next Slots In Purge

I hate my life

---
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[bed92e193c...](https://github.com/MrMelbert/tgstation/commit/bed92e193ce4a79824fd4fd30a900245dca870ae)
#### Monday 2023-11-20 19:07:43 by san7890

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
## [zephyrside/famidash](https://github.com/zephyrside/famidash)@[ea8cc6bec5...](https://github.com/zephyrside/famidash/commit/ea8cc6bec5b014bcd5021a5d80ae36d9d929b5b6)
#### Monday 2023-11-20 20:03:55 by ADM228

I HAVE FINALLY FUCKING FIXED IT HOLY FUCKING SHIT IT WORKS HOLY MOTHERFUCK

---
## [Mnesma/blackguard-timer-suite](https://github.com/Mnesma/blackguard-timer-suite)@[3e4ea20e7c...](https://github.com/Mnesma/blackguard-timer-suite/commit/3e4ea20e7ca216528c39f91f35b40a045676ac1c)
#### Monday 2023-11-20 20:37:08 by Mnesma

Damn I'm so fucking ugly (I forgot to disable the debugger)

---
## [ryankhan0302/QR-code-generator](https://github.com/ryankhan0302/QR-code-generator)@[9534fef6b9...](https://github.com/ryankhan0302/QR-code-generator/commit/9534fef6b9caf4378597742d5cf53e0e8e3d1eda)
#### Monday 2023-11-20 20:38:34 by ryankhan0302

Add files via upload

Hey fellow developers,

I'm excited to share the beginning of a new learning journey with all of you! 🌟 Today, I dove into the world of QR code generation using Node.js, and I can't wait to share my progress and insights with you.

Project Overview:

🔍 What is this project about?
I've started working on a QR code generator using Node.js. QR codes have become an integral part of modern applications, and understanding how to generate them programmatically is a valuable skill.

🚀 Why Node.js?
Node.js is known for its speed and scalability, making it a fantastic choice for building applications that require real-time functionality. It's also great for handling asynchronous operations, which is essential when working with QR code generation.

Tech Stack:

🔧 Node.js:
I've chosen Node.js as the primary technology for this project due to its event-driven architecture and ease of use. If you're new to Node.js like me, it's a fantastic opportunity to learn and grow your skills.

📦 Additional Packages:
I'll be using relevant npm packages to make the QR code generation process smoother. Feel free to suggest your favorite packages or share any tips you have!

Learning Goals:

🎓 What am I hoping to achieve?
I aim to understand the fundamentals of QR code generation, explore the capabilities of Node.js in handling such tasks, and ultimately create a robust QR code generator that can be used in various applications.

🛣️ Milestones:
I'll be documenting my progress and milestones along the way. From setting up the project to generating the first QR code, every step will be a learning experience.

How Can You Get Involved?

🤝 Join the Discussion:
Feel free to join the conversation! Share your insights, ask questions, or suggest improvements. This project is as much about collaboration as it is about learning.

🚀 Contribute:
If you're experienced with Node.js or QR code generation, your contributions are more than welcome! Let's make this project a collective effort.

Stay Tuned:

📅 What's next?
I'll be posting regular updates on my progress, challenges faced, and lessons learned. Subscribe to this thread to stay in the loop and follow along on this exciting journey.

Thank you for being a part of this adventure! Let's code, learn, and grow together. 🌐💻

---
## [lerndmina/commands-wiki](https://github.com/lerndmina/commands-wiki)@[c6f797fa58...](https://github.com/lerndmina/commands-wiki/commit/c6f797fa5889ca25f27fa3d4fe8e9efde886841b)
#### Monday 2023-11-20 21:06:38 by Adam

Made Last Updated live based on page refresh

This is such a hack on line 40 I actually hate myself for it. None of the other documented ways to do this actually worked with Astro. Thanks :)

---
## [CS4800-2023FALL-Group4/WarriorDiningFrontEnd](https://github.com/CS4800-2023FALL-Group4/WarriorDiningFrontEnd)@[6d2b7f0de4...](https://github.com/CS4800-2023FALL-Group4/WarriorDiningFrontEnd/commit/6d2b7f0de41b074ea615dd2662ce83bea7a94cf1)
#### Monday 2023-11-20 21:27:01 by Dan C

Yeah, I did it. fetchMenu formats fixed and more.

- Fixed fetchmenu to properly format menuItems
- Added fetchmenu for lunch
- Added fetchmenu for dinner
- Connected fetchLunchMenu to Lunch menu button on UI
- Connected fetchDinnerMenu to Dinner menu button on UI
- (Previously connected fetchBreakfastMenu to Breakfast menu button on UI, don't know if I said that in a prior commit or not)

---
## [oxidecomputer/omicron](https://github.com/oxidecomputer/omicron)@[2fc0dfd8c1...](https://github.com/oxidecomputer/omicron/commit/2fc0dfd8c11f31e66cfaf8ee80586bb2ed607216)
#### Monday 2023-11-20 21:48:36 by Andrew J. Stone

Extract storage manager related code from sled-agent (#4332)

This is a large PR. The changes are in many ways *just* moving code
around,
and at a cursory glance may appear to be a giant waste of time. To
justify
these changes and my rationale I will first present the goals I believe
we
should strive to meet in general sled-agent development. I'll then go
into
how I believe these goals can be realized via code patterns. I'll then
discuss
the concrete changes in this PR and how they implement the discussed
patterns.
Lastly, I'll list a few open questions about the implementation in the
PR.

I want to emphasize that a lot of what I talk about below is already
done in
sled-agent, at least part way. We can pick the best patterns already in
use and
standardize on them to build a more coherent and yet decoupled
architecture for
easier testing and understanding.

# Goals

This PR is an attempt to start making sled-agent easier to maintain. In
order to
make things easier to maintain, I believe we should attempt to realize a
few key
goals:

1. Initial startup and control code should read linearly. You shouldn't
have to
jump around to follow the gist of what's going on.
2. Tasks, like functions, should live at a certain abstraction level. It
must be clear
 what state the task is managing and how it gets mutated.
3. A developer must be able to come into the codebase and know where a
given
functionality should live and be able to clearly follow existing
patterns such
that their new code doesn't break or cross abstractions that make
following the
code harder in the future.
4. Tests for individual abstractions and task driven code should be easy
to
write. You shouldn't need to spin up the whole sled-agent in order to
test an
algorithm or behavior.
 5. Hardware should be abstracted out, and much of the code shouldn't 
 deal with hardware directly.

# Patterns

## Task/Handle

In my opinion, the most important pattern to follow for async rust
software
is what I call the "task/handle" pattern. This pattern helps code
maintenance
by explicitly managing state and making task driven code easier to test.
All
tasks that provide services to other tasks should follow this pattern.
In this
pattern, all state is contained in a type owned by the task and
inaccessible
directly to other tasks. The task has a corresponding handle which must
be
`Send` and `Clone`, and can be used to make requests of the task. The
handle
interacts with the task solely via message passing. Mutexes are never
used.

A few things fall directly out of this pattern:

* Code that manipulates state inside and outside the task can be
synchronous
* We don't have to worry about mutex behavior with regards to
cancellation,
   await points, etc...
 * Testing becomes easier:
   * We can test a bunch of the code without spawning a task in many
cases. We just [directly construct the state object and call
functions](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR634-R656),
     whether sync or async.
   * When testing sequential operations that are fire and forget,
we [know when they have been processed by the task
loop](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR702-R709),
     because our next request will only run after those operations. 
This is a direct result of the fifo channel between handle and task.
This is not possible with state shared outside the task via a mutex.
     We must poll that mutex protected state until it either changes to
     the value we expect or we get a timeout. If we expect no change, we
     must use a side-channel.
   * We can write complex state handling algorithms, such as those in 
      maghemite or bootstore, in a deterministic, synchronous style that
allows property based testing and model checking in as straightforward
     a manner as possible.
* We can completely [fake the
task](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR163-R223)
without changing any of the calling code except the constructor. The
real
handle can instead send messages to a fake task. Importantly, this
strategy
can also be used to abstract out hardware for unit tests and simulation.

Beyond all that though, the understanding of how state is mutated and
accessed
is clear. State is only mutated inside the task, and can only be
retrieved from
code that has a copy of the handle. There is no need for separate
`_locked`
methods, and no need to worry about order of locking for different bits
of task
state. This can make the task code itself much shorter and easier to
read as
demonstrated by the new `StorageManager` code in `sled_storage`. We can
also
maintain internal stats for the task, and all of this can be retrieved
from the
handle for reporting in `omdb`.

There is one common question/problem with this pattern. How do you
choose a
bounded channel size for handle to task messages?

This can be tricky, but in general, you want the channel to *act*
unbounded,
such that sends never fail. This makes the channels reliable, such that
we never
drop messages inside the process, and the caller doesn't have to choose
what to
do when overloaded. This simplifies things drastically for developers.
However,
you also don't want to make the channel actually unbounded, because that
can
lead to run-away memory growth and pathological behaviors, such that
requests
get slower over time until the system crashes.

After discussions with @jgallagher and reflections from @sunshowers and
@davepacheco on RFD 400, the solution is to choose a large enough bound
such that we should never hit it in practice unless we are truly
overloaded.
If we hit the bound it means that beyond that requests will start to
build
up and we will eventually topple over. So when we hit this bound, we
just
[go ahead and
panic](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR75-R77).

Picking a channel bound is hard to do empirically, but practically, if
requests are
mostly mutating task local state, a bound of 1024 or even 8192 should be
plenty.
Tasks that must perform longer running ops can spawn helper tasks as
necessary
or include their own handles for replies rather than synchronously
waiting. Memory
for the queue can be kept small with boxing of large messages.

It should also be noted that mutexes also have queues that can build up
and
cause pathological slowness. The difference is that these queues are
implicit
and hard to track.

## Isolate subsystems via the message driven decoupling

We have a bunch of managers (`HardwareManager`, `StorageManager`,
`ServiceManager`, `InstanceManager`) that interact with each other to
provide sled-agent services. However, much of that interaction is ad-
hoc with state shared between tasks via an `Inner` struct protected
by a mutex. It's hard to isolate each of these managers and test
them independently. By ensuring their API is well defined via a
`Handle`,
we can fake out different managers as needed for independent testing.
However, we can go even farther, without the need for dependency
injection
by having different managers announce their updates via [broadcast or
watch

channels](https://github.com/oxidecomputer/omicron/pull/4332/files#diff-08315639e20a9323f2740455a7813d83ca43b05dca197ebbda66c13f750d446bR129-R133).

With this strategy, we can drive tests for a task by using the handle to
both
trigger operations, and then wait for the outflow of messages that
should occur
rather than mocking out the handle API of another task directly and
checking
the interaction via the fake. This is especially useful for lower level
services
that others depend upon such as `StorageManager`, and we should do this
when we
can, rather than having tasks talk directly to each other. This strategy
leads
directly to the last pattern I really want to mention, the `monitor`
pattern.

## High level interaction via monitors

Remember that a primary goal of these patterns is to make the sled-agent
easier
to read and discover what is happening at any given point in time. This
has to
happen with the inherent concurrency of all the separate behaviors
occurring
in the sled-agent such as monitoring for hardware and faults, or
handling user
requests from Nexus. If our low level managers announce updates via
channels
we can have high level `Monitors` that wait for those updates and then
dispatch
them to other subsystems or across clients to other sleds or services.
This
helps further decouple services for easier testing, and also allows us
to
understand all the asynchrony in the system in fewer spots. We can put
RAS code
in these monitors and use them as central points to maintain stats and
track the
overall load on the system.

# The punchline

How do the patterns above satisfy the goals? By decoupling tasks and
interacting
solely via message passing we make testing easier(goal 4). By separating
out
managers/ services into separate tasks and maintaining state locally we
satisfy
goals 2 and 5. By making the tasks clear in their responsibilities, and
their
APIs evident via their handles, we help satisfy goal 3. Goal 3 is also
satisfied
to a degree by the elimination of sharing state and the decoupling via
monitors.
Lastly, by combining all the patterns, we can spawn all our top level
tasks and
monitors in one place after initializing any global state. This allows
the code
to flow linearly.

Importantly, it's also easy to violate goal 3 by dropping some mutexes
into the
middle of a task and oversharing handles between subsystems. I believe
we can
prevent this, and also make testing and APIs clearer, by separating
subsystems
into their own rust packages and then adding monitors for them in the
sled-agent.
I took a first cut at this with the `StorageManager`, as that was the
subsystem I was
most familiar with.

# Concrete Code changes

Keeping in line with my stated goals and patterns, I abstracted the
storage
manager code into its own package called `sled-storage`. The
`StorageManager`
uses the `task/handle` pattern, and there is a monitor for it in
sled-agent
that takes notifications and updates nexus and the zone bundler. There
are also a
bunch of unit tests where none existed before. The bulk of the rest of
the code
changes fell out of this. In particular, now that we have a separate
`sled-storage`
package, all high level disk management code lives there. Construction
and
formatting of partitions still happens in `sled-hardware`, but anything
above the
zpool level occurs in `sled-storage`. This allows testing of real
storage code on
any illumos based system using file backed zpools. Importantly, the
key-management
code now lives at this abstraction level, rather than in
`sled-hardware`, which
makes more sense since encryption only operates on datasets in ZFS.

I'd like to do similar things to the other managers, and think that's a
good way
to continue cleaning up sled-agent.

The other large change in this code base is simplifying the startup of
the bootstrap agent such that all tasks that run for the lifetime of
the sled-agent process are spawned in `long_running_tasks`. There is a
struct called `LongRunningTaskHandles` that allows interaction with all
the
"managers" spawned here. This change also has the side effect of
removing the
`wait_while_handling_hardware_updates` concurrent future code, since we
have
a hardware monitor now running at the beginning of time and can never
miss
updates. This also has the effect of negating the need to start a
separate
hardware manager when the sled-agent starts up. Because we now know
which
tasks are long running, we don't have to save their tokio `JoinHandle`s
to display
ownership and thus gain clonability.

# Open Questions

* I'm not really a fan of the name `long_running_task_handles`. Is there
a better
name for these?
* Instead of calling `spawn_all_longrunning_tasks` should we just call
the
individual spawn functions directly in `bootstrap/pre_server`? Doing it
this
way would allow the `ServiceManager` to also live in the long running
handles
and remove some ordering issues. For instance, we wait for the bootdisk
inside
`spawn_all_longrunning_tasks` and we also upsert synthetic disks.
Neither
of these is really part of spawning tasks.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[c55a058207...](https://github.com/Buildstarted/linksfordevs/commit/c55a058207543c72888c52a8a723d3d2d344ba3e)
#### Monday 2023-11-20 22:09:21 by Ben Dornis

Updating: 11/20/2023 10:00:00 PM

 1. Added: The cocktail revolution - Works in Progress
    (https://worksinprogress.co/issue/the-cocktail-revolution/)
 2. Added: SearchArray: Making search relevance not so special
    (https://softwaredoug.com/blog/2023/11/20/search-relevance-less-special)
 3. Added: Long Term Refactors - Max Chernyak
    (https://max.engineer/long-term-refactors)
 4. Added: Exploring macOS private frameworks
    (https://www.jviotti.com/2023/11/20/exploring-macos-private-frameworks.html)
 5. Added: How to Effectively Set Up NextJS with a Component Library using Monorepos
    (https://dainemawer.com/articles/how-to-effectively-setup-nextjs-with-a-component-library-using-monorepos)
 6. Added: Tim Severien
    (https://tsev.dev/posts/2023-11-10-should-avif-be-the-dominant-image-format/)
 7. Added: The reciprocal Fibonacci constant
    (https://fredrikj.net/blog/2023/11/the-reciprocal-fibonacci-constant/)
 8. Added: Writing a Cloudflare worker with squint and bun
    (https://blog.michielborkent.nl/squint-cloudflare-bun.html)
 9. Added: Data-Driven Development is a Lie
    (https://grishaev.me/en/ddd-lie)
10. Added: Back up your Bitwarden vault in a future-proof and secure way
    (https://davidisaksson.dev/posts/bitwarden-backup/)
11. Added: Discount rates in venture backed startups
    (https://reactionwheel.net/2023/11/discount-rates-in-venture-backed-startups.html)
12. Added: Erik Johannes Husom
    (https://erikjohannes.no/posts/20231119-the-future-of-social-media/)
13. Added: Never again compare a startup to a vitamin
    (https://www.pathsensitive.com/2023/09/its-time-for-painkillers-vitamins-die.html)
14. Added: UTC is not Your Saviour – Random Notes
    (https://blog.nytsoi.net/2022/03/13/utc)
15. Added: C# Data Access: Complex Objects with Dapper
    (https://youtube.com/watch?v=n7mGEh4_06c)
16. Added: 📨 Void Inbox
    (https://orchardlab.dev/posts/void-inbox/)
17. Added: Reverse-engineering GPTs for fun and data
    (https://andrei.fyi/blog/reverse-engineering-gpts/)
18. Added: The Creator's Curse: Why your latest project will eventually make you miserable | Peter Shallard
    (https://www.petershallard.com/the-creators-curse/)
19. Added: The New CSS Math: rem() and mod()
    (https://danielcwilson.com/posts/mathematicss-rem-mod/)
20. Added: Microsoft Canada - Calgary Automation and Integration Day
    (https://msit.events.teams.microsoft.com/event/5d41b1b3-e626-4de4-92db-65768d6f2ea6@72f988bf-86f1-41af-91ab-2d7cd011db47)
21. Added: Radius a new open-source application platform for the cloud | BRK402
    (https://youtube.com/watch?v=gaG77PiYv5w)
22. Added: Migrating Page Navigation Apps from Xamarin Forms
    (https://platform.uno/blog/migrating-page-navigation-apps-from-xamarin-forms/)

Generation took: 00:09:07.3204785
 Maintenance update - cleaning up homepage and feed

---
## [mbland/tomcat-servlet-testing-example](https://github.com/mbland/tomcat-servlet-testing-example)@[0a4cd2c6b8...](https://github.com/mbland/tomcat-servlet-testing-example/commit/0a4cd2c6b881a7cae27318f317c9a28e50c60e33)
#### Monday 2023-11-20 23:27:35 by Mike Bland

Add Weld for Java dependency injection

Weld is the reference implementation of "CDI: Contexts and Dependency
Injection for the Java EE Platform."

- https://weld.cdi-spec.org/
- https://www.cdi-spec.org/

This is in preparation for introducing the StringCalculator interface,
which I'll use to inject different StringCalculator implementations into
the Servlet.

This involved:

- Adding implementation dependencies for:
  - org.jboss.weld.servlet:weld-servlet-core
  - io.smallrye:jandex (recommended for speeding up bean discovery)

- Adding new strcalc/src/main/webapp files to add to the servlet WAR
  file, not needed until now, configured according to
  https://docs.jboss.org/weld/reference/5.1.2.Final/en-US/html_single/#tomcat:
  - META-INF/context.xml
  - WEB-INF/web.xml

- Added strcalc/src/main/webapp/WEB-INF/beans.xml because Weld will skip
  initialization without it, with the warning:
  WELD-ENV-000028: Weld initialization skipped - no bean archive found

- Updating the TestTomcat helper to find these new files and to enable
  Java Naming and Directory Interface (JNDI), required by Weld:
  - https://docs.oracle.com/javase/tutorial/jndi/overview/index.html
  - https://docs.jboss.org/weld/reference/5.1.2.Final/en-US/html_single/#_binding_the_manager_in_jndi
  - https://tomcat.apache.org/tomcat-10.1-doc/api/org/apache/catalina/startup/Tomcat.html#enableNaming()

One silver lining was that adding JarScanner > JarScanFilter element to
META-INF/context.xml rendered the custom TestTomcat logic to disable the
JarScanner unnecessary.

Perhaps the other silver lining is that the TestTomcat now tracks
whatever's in src/main/webapp. This should enable the TestTomcat
configuration to remain in sync with the final WAR file.

---

And now for what I really came here to say: I hate Java. I _really_,
_really_, _really_ hate Java. Not so much the language itself, but the
entire culture and ecosystem that has festered around it for 28 years.

If the question is:

- How can we make relatively straightforward tasks as complicated,
  verbose, and arcane as humanly possible?

The answer is invariably:

- Java.

Never in any other programming language, in any program, have I had the
need to use a "dependency injection framework". Never. And I've been
injecting dependencies like crazy for at least a decade and a half by
now—_starting_ in C++.

None of those other languages or frameworks made it impossible to wire
my own object graph in whatever context at hand. Often this is within a
test class a la JUnit, or a "describe" block a la Mocha, or a similar
construct easily written in Go. (See my mbland/elistman project for
copious examples of the latter.) Then I can wire up my production graph
in main(), or in a function directly called from main(). Or, in Node.js,
in the main server script before starting the server task.

In those other programming languages, if I want to start a local HTTP
server injected with whatever implementations I want, I just do that. In
a test, in the main implementation, it doesn't matter. Most standard
libraries provide a HTTP server implementation, their interfaces and
their contracts are straightforward, and they're usually well
documented. At any rate, it's not that hard to figure out.

The Java ecosystem, in its infinte wisdom, presents a different story.
It considers wresting direct responsibility for and control over your
execution environment and object a graph a feature, not the revolting
bug that it is. And somehow, a critical mass of programmers have not
only learned to cope with the trauma, but actively dedicated themselves
to perpetuating it.

And that brings us to the concept of "servlet containers" and "Context
and Dependency Injection," a.k.a. "CDI".

Like I said, I just want an HTTP server that I can plug things into
myself, usually via registering endpoint handlers at runtime. Granted,
that's the same principle as the Servlet API, but this being Java, of
course it's not that easy.

Let's look at the opening paragraph of https://tomcat.apache.org/:

  The Apache Tomcat® software is an open source implementation of the
  Jakarta Servlet, Jakarta Server Pages, Jakarta Expression Language,
  Jakarta WebSocket, Jakarta Annotations and Jakarta Authentication
  specifications. These specifications are part of the Jakarta EE
  platform.

Outside of "software" and "open source implementation," what the hell do
any of those words even mean? Here's my attempt at an improvement:

  Apache Tomcat is a web server for deploying Java Servlets, web
  applications bound to an HTTP endpoint. Servlets implement the
  jakarta.servlet.http.HttpServlet interface for accepting HTTP request
  and response objects.

Was that so hard to say? And that first example is, sadly, genuinely
representative of the entire Java documentation corpus. References to
references to references, never ending up giving concrete, practical
guidance on what should be straightforward steps to achieve a goal.
Words, words, words, tales told by idiots, full of sound and fury,
signifying practically nothing.

(I blame Sun Microsystems. I remember trying repeatedly to make heads or
tails of some of their Solaris docs, and giving up every time. I think
Amazon hired a bunch of their old writers for the higher-level AWS docs,
which I've found equally useless. There are some great AWS docs, but I
only found them after spending hours sniffing out rare breadcrumbs that
led me to them. Once I knew where they were hiding, and how to get
straight to them, life got much better.)

All I want to do is define an interface, a production implementation,
and a test double, and plug it into my HTTP server. Instead, I need a
graduate degree in trawling through enterprise bloatware documentation
with a nearly imperceptible signal to noise ratio to perform this
routine task:

- CDI:
  https://www.cdi-spec.org/
- Weld:
  https://docs.jboss.org/weld/reference/5.1.2.Final/en-US/html_single/
- JNDI:
  https://docs.oracle.com/javase/tutorial/jndi/overview/index.html

And I _refuse_ to learn about any @Interceptors or @Decorators or
@Stereotype or any more META-INF/kill_me_now.xml files or
@AnyOtherBullshitNotActuallyNecessaryForDependencyInjection.

If it weren't for web search and programmer forums, I _still_ wouldn't
have made any progress. Sometimes even those resources couldn't help me;
check out the comment above `tomcat.enableNaming()`. I found matches for
"Failed to retrieve JNDI naming context for container". However, I
couldn't find any advice for when this appeared after stopping an
embeddded Tomcat. Somehow having waded through so much excess verbiage
referencing JNDI did I think to see if the Tomcat class had an
enableNaming() method. Even the Weld docs' example for embedded Tomcat
didn't mention this:

- https://docs.jboss.org/weld/reference/5.1.2.Final/en-US/html_single/#_embedded_tomcat

In fact, it recommends registering the Weld listener
programmatically—which I'd normally prefer, _if it worked_:

  ctx.addApplicationListener(Listener.class.getName())

That didn't end up working for me at all. It did nothing to eliminate
sufficient complexity to get embedded Tomcat instance starting
successfully. For that reason, I think the current TestTomcat
implementation that reads the src/main/webapp configs is superior. It
may be more complex than I find ideal, requiring access to those files
to function, but at least it's consistent and functional.

The point of this `tomcat.enableNaming()` example is that, in the end, I
made an educated guess, and I got lucky. In other languages, I make an
educated guess, and the language or framework makes more sense. In Java,
I just got lucky this one time, and that's it. There's no deeper value
or insight to derive from the experience. I can merely move on from the
task at hand, surely to waste more time on the next one until I get
lucky again.

Java is the quintessential triumph of marketing hype over delivering
actual technical value. Everytime I touch it I feel like I'm wasting at
least 10x the time I should need to in order to get something
straightforward done. It's just sick and wrong, and it generates
immeasurable waste in terms of programmer time, business value,
opportunity cost, and global warming.

OK, I feel better. That's all for now. (Until I eventually make this a
proper blog post.)

---
## [sysread/page-summarizer](https://github.com/sysread/page-summarizer)@[c16e15d65d...](https://github.com/sysread/page-summarizer/commit/c16e15d65d73b8c52a732037a15f187c4bb4940c)
#### Monday 2023-11-20 23:31:59 by Jeff Ober

Remove stupid debug shit where I put my goddamn API key in my stupid idiot code

---
## [tylerdeandigipen/Vyv_Lantern](https://github.com/tylerdeandigipen/Vyv_Lantern)@[9f13c00426...](https://github.com/tylerdeandigipen/Vyv_Lantern/commit/9f13c0042687ddb1b99d3fbe931d0d3f7e40408d)
#### Monday 2023-11-20 23:37:31 by ImFifth

FUCK YOU TYLER FIX MY SHIT ok thank you :) also give me free dsi games and make sure to generate more ai names for our game along with logos so I can use them for a playtest I'd like at least 5 of them but preferably closer to 10

--

---

