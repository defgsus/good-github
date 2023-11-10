## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-09](docs/good-messages/2023/2023-11-09.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,488,815 were push events containing 3,934,356 commit messages that amount to 296,774,541 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [SethLafuente/tgstation](https://github.com/SethLafuente/tgstation)@[1a9043d797...](https://github.com/SethLafuente/tgstation/commit/1a9043d797325fe09cdb4e42d42f5d922c151ed9)
#### Thursday 2023-11-09 00:15:51 by necromanceranne

The Brawlening: Unarmed fighting interactions for shoving, grabbing and nonlethal takedowns (not martial arts) (#79362)

## About The Pull Request

I've tweaked some elements of unarmed fighting to give it additional
interactions between the various components, bridging them into a more
coherent system and focusing more strongly as tool for disabling
opponents nonlethally.

### Shoving

Shoving guarantees that unarmed attacks will land while knocked
off-balance (AKA when slowed by a shove).

Being off-balance means that you can be knocked down from a punch if you
have taken enough brute and stamina damage combined (at least above 40).

Being off-balance makes you vulnerable to grabs while you have a
moderate amount of stamina damage (30 damage), forcing you to have to
resist even passive grabs. This pairs _exceptionally_ well with
tackling.

### Grappling

Grappling someone makes your unarmed attacks penetrate armor based on a
new limb value called ``unarmed_effectiveness``. This is something
shared by kicking.

### Unarmed Attacks in General

``unarmed_effectiveness`` has also taken over the functionality of
``unarmed_stun_threshold``, as well as accuracy calculations. Human
equivalent limbs (pretty much all of them except mushrooms and golems)
have a value of 10.

Now, ``unarmed_effectiveness`` determines how accurately a given limb
makes unarmed attacks. Unarmed attacks have a base inaccuracy of 20%,
with effectiveness acting as a reduction to this value. (so for humans,
that's 20% - 10% before any value changes from brute and stamina
damage). It is also capped at 75% miss chance, just to avoid those weird
instances of two brawling fighters being incapable of finishing each
other off at a certain amount of damage and it being real awkward, like
it does currently.

It also determines the base probability of landing a knockdown punch.
For humans, this is 10%.

For the most part, these two particular changes are roughly equivalent
to the current values, just handled in a way that is more
straightforward to understand from a code perspective.

In addition to the above, human equivalent limbs have higher damage
floors for unarmed attacks. Arms deal 5-10 damage, while legs deal 7-15
damage. In addition, kicks also deal stamina damage, like punches do.

### Minor Mentions

Golems and Mushroom People (who don't even use their limbs for their
unarmed strikes because mushroom people start with a martial art) have
very accurate punches, and their punches penetrate quite a bit of armor
when they are entitled to that. They also have a high knockdown
probability. This is partially because they previously already _had_
these features due to the wonky math at play, but also because this is
their big thing they are good at.

Carp mutation also got a big win out of this as well. If and when you
actually manage to get that to work and matter.

## Why It's Good For The Game

My favorite thing in this game is the robustness of unarmed fighting.
It's the part of the game that actually acknowledges the sandbox and
environmental interaction in a big way. The only problem with the
unarmed combat is that it is a bit disjointed, and often much weaker
than using even the most pathetic weapon you can get your hands on
unless you're using the stun loops available. Those loops get a bit
boring, even if they're mostly all environmental (except for the lucky
neckgrab finish). Giving more options generally means that even when not
in an ideal position, you still have _some_ options.

It also has some internal inconsistencies in design even in the same
proc, like accuracy calculations and knockdowns, as well as weird splits
in damage. So I decided to resolve that.

Now, every part of unarmed fighting has some relevance in the other
parts. Predominantly, it is heavily favoured towards dealing stamina
damage, making unarmed combat very favourable as a nonlethal method of
taking someone down, which is something we currently lack considerably.
While people may still opt to simply beat someone into actual crit
rather than stop at stamina crit, the possibility is actually entirely
available and supported now. No just banking on a lucky neckgrab after a
shove.

Paying attention to damage dealt and thinking intelligently about how
you apply combinations of effects allows even someone on the significant
back foot an opportunity for a comeback if they know what they're doing
against even armed opponents.

Separating accuracy and knockdown effectiveness from damage allows for
more consistent design and readability, but also preventing weirdness
ike tighter damage spreads increasing knockdown probabilities as well as
increasing accuracy without the coder knowing why. This also lets us
make unarmed attacks just that little bit stronger. Since unarmed
attacks require more complicated combinations to work, I think this
won't make them stronger than weapons necessarily, but it will make for
more interesting swung fights.

## Changelog
:cl:
add: With the flood of Chi within the Spinward Sector receding, various
masters of The Tunnel Arts, colloquially known as 'Maint-fu Masters',
have started to refine the basics of their martial techniques. New forms
have started to develop within Spacestation 13's hidden maintenance
dojos.
add: Someone shoved off-balance makes them vulnerable to more guaranteed
unarmed strikes, knockdowns from a successful punch, and more difficult
to escape grabs.
add: Grabbing someone (as well as kicking them while they're on the
floor) makes them more vulnerable to taking unarmed attack damage, even
if they have armor.
balance: Unarmed strikes made with human-equivalent limbs have higher
damage floors, meaning you overall do more damage on average while not
increasing the overall damage potential. It's more consistent!
refactor: Significantly changed how punching accuracy and knockdowns are
calculated.
balance: Golem and mushroom limbs are a lot more effective at punching
as a result of these various changes. As they should be.
/:cl:

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[9e18c6575a...](https://github.com/necromanceranne/tgstation/commit/9e18c6575a3cb9e73c3e699d4fe51b904b76e2f6)
#### Thursday 2023-11-09 00:33:56 by lizardqueenlexi

Basic Pirate NPCs (#79284)

## About The Pull Request

Converts hostile pirate NPCs to basic mobs - specifically, a subtype of
trooper. As their behavior is not meaningfully distinct from other
troopers, this conversion mostly just sticks them on the existing AI
behavior while keeping the rest the same.

Pirates do have one new thing going for them, though, to differentiate
them from other troopers. They use the new **plundering attacks**
component, which means that every time they land a melee attack, they
steal money from the bank account of whoever they hit. This requires the
target to be wearing an ID with a linked bank account, so it's not the
hardest thing in the world to hide your money from them - but it's still
something to be wary of! If killed, any mob with this component will
drop everything they've stolen in a convenient holochip.
## Why It's Good For The Game

Takes down 5 more simplemobs, and (I think) converts the last remaining
trooper-type enemy to be a basic trooper. (It's possible there's more
I've forgotten that could use the same AI, though.)

The money-stealing behavior is mostly good because I think it's funny,
but it also makes the pirates something a little distinct from "yet
another mob that runs at you and punches you until you die". They still
do that, but now there's a little twist! This can be placed on other
mobs too, if we want to make any other sorts of thieves or brigands.
## Changelog
:cl:
refactor: Pirate NPCs now use the basic mob framework. They'll be a
little smarter in combat, and if you're wearing your ID they'll siphon
your bank account with every melee attack! Beware! Please report any
bugs.
/:cl:

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[e174990dd5...](https://github.com/cockroachdb/cockroach/commit/e174990dd5015a38b1e9bc6723f270dbe647c3a3)
#### Thursday 2023-11-09 00:35:00 by craig[bot]

Merge #113809

113809: kvstreamer: add limit to how many eager batches are issued r=yuzefovich a=yuzefovich

**kvstreamer: add limit to how many eager batches are issued**

This commit fixes extremely suboptimal behavior of the streamer in the
InOrder mode in some cases. In particular, previously it was possible
for the buffered responses to consume most of the working budget, so the
streamer would degrade to processing all requests effectively one
BatchRequest with one Get / Scan at a time, significantly increasing the
latency. For example, the query added as a regression test that performs
30k Gets across 10 ranges would usually take on the order of 1.5s (which
is not great already since in the non-streamer path it takes 400ms), but
in the degenerate cases it could be on the order of 20-30s.

Similar behavior could occur in the OutOfOrder mode too where we would
issue more BatchRequests in which only one request could be satisfied
(although in OutOfOrder mode the problem is not as severe - we don't
buffer any results since we can always return them right away).

This problem is now fixed by imposing the limit on the budget's usage at
which point the streamer stops issuing "eager" requests. Namely, now,
when there is at least one request in flight, the streamer won't issue
anymore requests once `limit * eagerFraction` is exceeded. This
effectively reserves a portion of the budget for the "head-of-the-line"
batch.

The "eager fraction" is controlled by a session variable, separate for
each mode. The defaults of 0.5 for InOrder and 0.8 for OutOfOrder modes
were chosen after running TPCH queries and the query that inspired this
commit. These values bring the number of gRPC calls for the reproduction
query from 1.5k-2k range to below 200 and the query latency to be
reliably around 400ms.

I don't really see any significant downsides to this change - in the
worst case, we'd be utilizing less of the available memory budget which
is not that big of a deal, so I intend to backport this change. Also,
setting the eager fractions to large values (greater than 1.0 is
allowed) would disable this limiting behavior and revert to the previous
behavior if we need it.

Fixes: #113729.

Release note (bug fix): Previously, when executing queries with
index / lookup joins when the ordering needs to be maintained,
CockroachDB in some cases could get into a pathological behavior
which would lead to increased query latency, possibly by 1 or 2 orders
of magnitude. This bug was introduced in 22.2 and is now fixed.

**kvstreamer: increase default avg response multiple**

This commit increases the default value for
`sql.distsql.streamer.avg_response_size_multiple` cluster setting from
1.5 to 3.0. This setting controls the factor by which the current "avg
response size" estimate is multiplied and allows for TargetBytes
parameter to grow over time. In the reproduction query from the
previous commit it was determined that the growth might not be as quick
as desirable.

The effect of this change is as follows:
- if we have responses of varying sizes, then we're now likely to be more
effective since we'll end up issuing less BatchRequests
- if we have responses of similar sizes, then we might pre-reserve too
much budget upfront, so we'll end up with lower concurrency across
ranges.

Thus, we don't want to increase the multiple by too much; however,
keeping it at 1.5 can be quite suboptimal in some cases - 3.0 seems like
a decent middle ground. This number was chosen based on running TPCH
queries (both via InOrder and OutOfOrder modes of the streamer) and the
reproduction query. (For the latter this change reduces the number of
gRPC calls by a factor of 3 or so.)

Release note: None

Co-authored-by: Yahor Yuzefovich <yahor@cockroachlabs.com>

---
## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[294f764ad0...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/294f764ad01a99c63b46dfea3dac7e5cfe14cd7d)
#### Thursday 2023-11-09 00:37:56 by Coxswain

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
## [MemedHams/Shiptest](https://github.com/MemedHams/Shiptest)@[40dfaf3734...](https://github.com/MemedHams/Shiptest/commit/40dfaf3734000b5e74e4101ab86516702f59425f)
#### Thursday 2023-11-09 00:41:05 by Imaginos16

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Does what it says in the title. This is a demented PR that touches a lot
of things, but its main benefit is that now regular independent
captains, cowboy independent captains, and nanotrasen captains have a
unique identity.

Of those changed, it includes:

- The Nanotrasen Captain (parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/48a31cb1-b266-43cb-9b6e-525028893011)

- The Nanotrasen Captain (regular)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/799c88f0-b7ce-4736-956d-2e9c0a096433)

- The Independent Captain (regular/parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/17ecb3d3-5f2f-4ce0-a518-81366945ebdf)

- The Independent Captain (western)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a56a798c-5adf-41d7-917a-730661f306ed)

The PR also axes a bunch of unused, or frankly quite basic lieutenant
outfits that were nothing more than set dressing with not much substance
behind them. The roles were not removed for now, and they have
appropriate outfits as a placeholder pending a full removal.

This also means that the Head of Personnel was slightly touched up,
mostly by having a coat and hat similar to the western captain's when
appropriate. The role itself is pending a full visual rework for later
that is beyond the scope of this PR.

Speaking of removals, this also means that captain outfits/roles that
were there as a legacy of removed ships, were finally axed for good.
Goodbye deserter captain for Riggs variant number 4, you will not be
missed.

This PR also touches several (a lot) of maps, mostly adding/removing
outfits that were either missing, or didn't fit with the dress code of
the vessel.

Also the PR fixes an oversight by @MarkSuckerberg by making the BYOND
version warning an actual warning, instead of an error when compiling.
Etto bleh.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
imageadd: Outfits for independent and Nanotrasen captains have been
violently reworked.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[91af16bcbf...](https://github.com/tgstation/tgstation/commit/91af16bcbfd2dd363a89d846ae2acd6d655083c2)
#### Thursday 2023-11-09 00:45:12 by zxaber

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
## [Y0SH1M4S73R/tgstation](https://github.com/Y0SH1M4S73R/tgstation)@[1a62886a8b...](https://github.com/Y0SH1M4S73R/tgstation/commit/1a62886a8b83afe5b827947051b9d85ac2ed1a8a)
#### Thursday 2023-11-09 01:01:41 by san7890

Fixes Shaving Beards + Mirror Code Improvement (#79529)

## About The Pull Request

Fixes #79519

Basically we did a lot of assumptions that we really shouldn't do in the
whole magical mirror framework (like having a boolean value for magical
mirrors, what?). Anyways, I just made the UX experience a lot better
when it came to bearded persons with feminine physiques to easily shave
off their beard with an additional confirmatory prompt + details as well
as keeping the nature of the magical mirror (giving you a swagadocious
beard due to magic:tm:) intact.
## Why It's Good For The Game

There was a lot of convoluted code that skipped through the quality
filter checks (it was me i think) so let's both make the code far easier
to grasp as well as ensure that people who legitimately acquire beards
and wish to keep them, keep them.

We were also doing some FUCK shit on attack_hand and the like
(overriding a FALSE return signal to return TRUE is not what we should
be doing there)- so that's also cleaned up.
## Changelog
:cl:
fix: Both magic mirrors and regular mirrors are far better at respecting
the choice of the beard you wish to wear (within reason, of course).
/:cl:

---
## [FarofaKnights/entrega-maluca](https://github.com/FarofaKnights/entrega-maluca)@[15cc8311be...](https://github.com/FarofaKnights/entrega-maluca/commit/15cc8311be08dc02e307ae4614b4318509fd10db)
#### Thursday 2023-11-09 01:04:09 by Kuro

🗻 Cenário ário na àrea

Não está finalizado por razões óbvias, se você estava esperando que esse commit já estivesse com tudo terminado procure ajuda médica, acredito eu que em algum dos prédios da PUC possuem ajuda médica.
Amanhã 09/11 iremos discutir a distribuição das ruas e as possíveis melhoras a serem feitas.
Fique agora com a letra da melhor abertura de jogos já feita:

I'm here now
Doing the best I can
Where are you now?
Did your dreams come true?
Here we go...

Get out, get out
SPARKING!
Get out
SPARKING!

What does the word "peace" mean?
There should only be a smiling face?
Answer me, reticent God
But the sun rises again
When will that time return?
Swear you won't give up!

Break out!
Anything day by day
Freak out!
Anything step by step
Live the sin, and let me know live the sin
Break down!
Make my story
Get down!
They're called history
My heartbeat gonna be faster
Shout, shout, shout, shout, soul

Destiny or deadly
I don't care which one's walking this way
They're nothing together
What if I go back to zero?

Get power of infinity
All men together make one man
At the time of an important decision,
Please do not lose your vision.
You're the one
Show me only your dance in earnest.
Even if wrapped in the darkness,
Light is beyond the horizon.

SPARKING!
Believe your own energy!
SUPER KING!
Get by my hands!
SPARKING!
Now open your wing!
SUPER KING!
You can do it!

Get up, get up, get up, get up, get up
Take it to top of the world...

SPARKING!

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[f39d74c3a6...](https://github.com/yogstation13/Yogstation/commit/f39d74c3a66c41a5ebb468dc3d61b0787f8327be)
#### Thursday 2023-11-09 01:07:03 by Waterpig

Invisible touch - this time for real (#20742)

* This was surprisingly easy

* Well this might be funny

* Hm

* Oh boy it's working

* I might be going insane

* Checks moved

---
## [Perkedel/CVR_Stuffings](https://github.com/Perkedel/CVR_Stuffings)@[75858d72d3...](https://github.com/Perkedel/CVR_Stuffings/commit/75858d72d3c627a5e6a225ea6efceda5854c72e0)
#### Thursday 2023-11-09 02:49:46 by JOELwindows7

installed CCK 3.7

the person that liked my post blocked me. my friend believe and said already, she wanted to move on from cardiophilia.

but blocking, shocks me bad way. It causes depression.

pls let her go. Pray God to give me power to invent something only I can make, so everyone want to use the idea depends on me. Without me, it's nothing. That should make blockers rue the day for ever blocking me.

didn't realize the tool that saved their lives had my patents on it. Recontemplate life choice. Why then I blocked Joel?

Okay, too hopeful. You don't have to unblock me. I'll have my patent, and without that my patent, you could be doomed, either..

f888 what the f888 am I thinking?

---
## [clyfly/kernel-mtk](https://github.com/clyfly/kernel-mtk)@[7876d8f652...](https://github.com/clyfly/kernel-mtk/commit/7876d8f652f8f9eafcabdac14ab6b93133e4d1bf)
#### Thursday 2023-11-09 04:08:17 by Peter Zijlstra

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
Change-Id: Idd54334615da4c78698ca8b3b12b514ae9d8360f
Signed-off-by: Alexander Winkowski <dereference23@outlook.com>

---
## [HackerDaGreat57/HackerDaGreat57](https://github.com/HackerDaGreat57/HackerDaGreat57)@[347b99a9ad...](https://github.com/HackerDaGreat57/HackerDaGreat57/commit/347b99a9add4b4876aa7815094381d4f06b72cff)
#### Thursday 2023-11-09 04:41:01 by Akshat Singh

i can explain.

i will not be removing revisions of this file from commit history, because that would symbolize "i refuse to admit this ever happened."

i'm not a perfect person. nobody is. we all make some very bad mistakes sometimes. i'm sorry what what i've done. (the people in question have forgiven me and we are on good terms now. life is good.)

---
## [dawinkenwe/dnd5e_simulator](https://github.com/dawinkenwe/dnd5e_simulator)@[010c910400...](https://github.com/dawinkenwe/dnd5e_simulator/commit/010c91040045bff37343c6c5d72bad8a76c603ef)
#### Thursday 2023-11-09 05:12:39 by dwink

Commit work done at Victors house so I can move from laptop to desktop. Don't judge me. Only god can judge me. And my friends, and my parents, and literal judges, and. ok fine. You can judge me. Thanks bud.

---
## [jefina17/jefina17](https://github.com/jefina17/jefina17)@[90d6c8772d...](https://github.com/jefina17/jefina17/commit/90d6c8772dd059de5342a48e7350cbde84ede3af)
#### Thursday 2023-11-09 06:58:42 by jefina vincy

Update README.md

👋 Hey there! I'm jefina. A passionate  about data science and data engineering.  I'm on a journey to explore, learn, and contribute to the ever-evolving landscape of data science.
- 
- 👀"Fun fact about me: I've found my true passion in programming, and my love affair is with Python. Just like a maestro conducts an orchestra, I orchestrate data with Pandas and NumPy, creating harmonious data symphonies. When it comes to visualization, I'm a visual storyteller, painting insights with Matplotlib and Seaborn. And SQL, well, it's my language of data, where I craft stories from rows and columns."


- 📚"I'm currently diving into the worlds of data visualization and data modeling, along with exploring the intriguing realm of ethical hacking.
- 🧩 Programming is like an endless puzzle, and I'm the eager solver. With data, I 🎨 paint stories; with code, I craft solutions. In the world of hacking, I'm the friendly spy 🕵️ seeking digital adventures. 💻🌐
- 📫 connect with me:


 [YouTube](https://youtube.com/@jefidiaries1513?si=V52f4RC59K5UhWHP) | [LinkedIn](https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile) | [Instagram](https://www.instagram.com/travel_feel_vibezz/?igshid=OGQ5ZDc2ODk2ZA%3D%3D)

---
## [TimUkrainian/zechub](https://github.com/TimUkrainian/zechub)@[0d97121c8c...](https://github.com/TimUkrainian/zechub/commit/0d97121c8ca6106c2c829f5b8f47679d1801a3f1)
#### Thursday 2023-11-09 07:13:10 by TonyAkinsWritesCrypto

ZecWeekly66

# ZecWeekly (Episode 66)


The Zebra book, Zcash enhanced privacy, ZecHub Extras, Zcash 7th Anniversary , Ywallet Upgrade. 


Curated by "TonyAkins"[TonyAkin01](https://twitter.com/TonyAkins01))

---

#### Welcome to ZecWeekly Episode 66


Welcome to the thrilling episode of ZecWeekly, as we explore Zcash's implementation of FROST using Schnorr , Zcash 7th Anniversary celebrated with lots of merches and prizes, release of Zebra updated 1.3.0, and the introduction of UniFFi for Developer's use cases. 

–
### This Week Education's Pieces.

This week's education pieces will educate and refine us with all details about Zcash addresses, both shielded and transparent addresses and other the latest development in the Zcash payment system. 

Click  the link below to access the resource :

https://wiki.zechub.xyz/visualizing-zcash-addresses




### Zcash Updates

Zcash and ECC updates. 

[NowNodes features Zcash for upgraded Privacy ecosystem](https://twitter.com/NOWNodes/status/1716463761777680713)

[Ywallet Zcash Ledger app on Nano S Plus w/ Orchard tx](https://www.youtube.com/watch?v=HRVNpDDoh1Y&t=34s) 

[Zcash Digitals Decentralized](https://twitter.com/ElectricCoinCo/status/1717570088771952811)

[tECC DAYS 2023 celebrated](https://twitter.com/ECCIntegrator/status/1718035043736547504)


[Announcing Zebra 1.3.0](https://twitter.com/ZcashFoundation/status/1716524342853476576)

[Implementation of UniFFi on Zcash Network](https://twitter.com/eiger_co/status/1716801431510851824)

[Zcash SDK fixes now live](https://twitter.com/EdgeWallet/status/1716530980499128578)

#### Zcash Community Grants Updates

[WalletD Community Grant Application](https://forum.zcashcommunity.com/t/walletd-community-grant-application/45876?utm_source=dlvr.it&utm_medium=twitter)

[Security assessment for Zcash FROST published](https://twitter.com/ZecHub/status/1716930299140169764)

[Zcash Community funded @eiger_co to create UniFFi library](https://twitter.com/ZcashCommGrants/status/1717273970922123392)

#### Community Projects

[Zcash 7th Anniversary celebrated in grande style](https://free2z.cash/ZecHub/zpage/zcash-7th-anniversary-challenge)

[Post Comments on Free2Z using Zenith CLI! Go check it out!](https://www.youtube.com/watch?v=HtorP8TJ5vk)

#### News & Media

[Binance founder CZ’s fortune gets slashed $12B, while SBF is still at $0](https://cointelegraph.com/news/binance-ceo-changpeng-zhao-fortune-slashed-billionaires-index)

[Google to invest another $2B in AI firm Anthropic: Report](https://cointelegraph.com/news/google-to-invest-another-two-billion-in-ai-firm-anthropic)

[Kraken to suspend trading for USDT, DAI, WBTC, WETH, and WAXL in Canada](https://cointelegraph.com/news/kraken-suspend-trading-usdt-dai-wbtc-weth-and-waxl-stablecoin-canada)

[AI Girlfriend Amouranth Wants to Use Her 'Vaginal Yeast' to Brew Beer](https://decrypt.co/203517)

[Audits and rug-pulled projects, a $650B token burn, and major DeFi protocol quits UK: Finance Redefined](https://cointelegraph.com/news/audits-and-rug-pulled-projects-a-650b-token-burn-and-major-defi-protocol-quits-uk-finance-redefined)

[Bitcoin's 14% Weekly Gain Signals 'End of an Era' as Big Tech Dumps, Analyst Says](https://www.coindesk.com/markets/2023/10/27/bitcoins-14-weekly-gain-signals-end-of-an-era-as-big-tech-dumps-analyst-says/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[Binance Founder CZ's Wealth Falls About $12B as Trading Revenue Slumps: Bloomberg](https://www.coindesk.com/business/2023/10/27/binance-founder-czs-wealth-falls-about-12b-as-trading-revenue-slumps-bloomberg/?utm_medium=referral&utm_source=rss&utm_campaign=headlines)

[How major German firms like Mercedes and Lufthansa are using NFTs](https://cointelegraph.com/news/germany-mercedes-lufthansa-nfts)

[ChatGPT creator OpenAI builds new team to check AI risks](https://cointelegraph.com/news/chatgpt-openai-new-team-ai-risks)

[Bitcoin restarting 2023 uptrend after 26% Uptober BTC price gains — research](https://cointelegraph.com/news/bitcoin-2023-uptober-btc-price-research)



## Some Zcash Tweets


[Central bank of Brazil account heard about Zcash today](https://x.com/anarchychains/status/1717288641288921272)

[Happy Birthday Zcash!!!](https://twitter.com/ZforZcash/status/1718085318543376404)

[ZcashFoundation and NCCGroupInfosec conduct a security assessment of the Foundation’s FROST](https://twitter.com/ZcashFoundation/status/1716849796315512935)

[What are Zero-knowledge Proofs](https://twitter.com/NighthawkWallet/status/1717730883933806958)

[Zcash Community Grant minutes](https://twitter.com/ZcashCommGrants/status/1717556482344907090)

[Keep yourself safe from hack with a Zcash wallet](https://twitter.com/NighthawkWallet/status/1717007699592851702)

[Metrics should be updated](https://twitter.com/ZcashForum/status/1716786643171225726)

[Join our UPA friends if you're at EFDevconnect](https://twitter.com/ElectricCoinCo/status/1716886693444530195)


[Social media Data collection, does it matter?](https://twitter.com/ZecHub/status/1716850588942577890)

[Follow NighthawkWallet for crypto privacy education](https://twitter.com/NighthawkWallet/status/1716625185623728248)

[Privacy is normal!](https://twitter.com/ZcashNigeria/status/1716755151497707660)


## Zeme of the Week

[https://twitter.com/ZcashNigeria/status/1718151545324200002](https://twitter.com/ZcashNigeria/status/1718151545324200002)

[https://twitter.com/zcashbrazil/status/1717609507432337754](https://twitter.com/zcashbrazil/status/1717609507432337754)

[https://twitter.com/zcashbrazil/status/1717225798019567621](https://twitter.com/zcashbrazil/status/1717225798019567621)



## Jobs in the Ecosystem

[Zcash needs graphic designers,writers, and privacy advocate in its ecosystem](https://twitter.com/ZecHub/status/1713947885220344234)

[Create Video HOWTO - Setup WSL in windows, and compile lastest zcashd](https://github.com/ZecHub/zechub/issues/567)

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[d31c21ff1b...](https://github.com/LemonInTheDark/tgstation/commit/d31c21ff1b57ba7003f9bbdcf51171d3215a0774)
#### Thursday 2023-11-09 07:51:08 by jimmyl

new space ruin, the biological research outpost (#79149)

## About The Pull Request

![2023-10-21 18 02
39](https://github.com/tgstation/tgstation/assets/70376633/5829e939-3b04-465f-a186-095ceb360bba)

adds this ruin to space ruin pool
this is a shady (as NT always is) bioresearch outpost that got fucked up
by an experiment
this has like some puzzle aspect to it since you gotta find keycards and
shit and press buttons to unlock shield gates
this ends with you fighting a heart which if you defeat, destroys the
blockade that prevents you from entering the outpost vault

also you can no longer literally just cut indestructible grilles or
unanchor indestructible windows

### new puzzle elements or something idk
variant of pressure plate that you cannot remove and it sends a puzzle
signal
cooler red puzzle doors that look very foreboding or something idk
theyre for this ruin
also puzzle blockades, which are indestructible dense objects that are
destroyed if they receive a puzzle signal
and also buttons and keycard pads for puzzles


https://github.com/tgstation/tgstation/assets/70376633/c98807ec-1e7b-49c4-a757-cdbb76a1b566



https://github.com/tgstation/tgstation/assets/70376633/9d5d9dd1-5868-44e6-a978-5ea57b30c298

stuff that throws electric shocks in a pattern, ignores insuls and only
knocks down, and no you cannot just run past


https://github.com/tgstation/tgstation/assets/70376633/5772917c-a963-48a4-a743-b0f610801d25

### enemies
living floor, it can only attack stuff on top of it and it attacks until
the victim is dead
it is invincible to all but a crowbar, and it cannot move, and it
remains hidden until a victim is in range


https://github.com/tgstation/tgstation/assets/70376633/aa1d54f6-b259-4e58-9d44-e393d2131acf

living flesh, it can replace your limbs with itself
the conditions for that are; the limb must have 20 or more brute, victim
must be alive and dismemberable, the limb may not be torso or head, or
the limb may not be living flesh
alternatively it can replace a missing limb
these are all checked with every attack
they have 20 hp
the limbs in question will sometimes act up, while passively draining
nutrition, arms will randomly start pulling nearby stuff, legs may step
randomly
limbs when detached, turn into mobs and reactivate AI 2 seconds later.
if the host is shocked, all living flesh limbs will detach, or if the
host dies they will also do that


https://github.com/tgstation/tgstation/assets/70376633/765cc99e-c800-4efb-aabe-d68817bbd7ae



## Why It's Good For The Game

ruin variety is cool i think
also the other things i added should be useful for other mappers for
bitrunning or whatever

also bug bad for that one fix
## Changelog
:cl:
add: living floor, living flesh, and other stuff for the bioresearch
outpost ruin
add: bioresearch outpost ruin
fix: you may not defeat indestructible grilles and windows with mere
tools
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [maryam-saeidi/kibana](https://github.com/maryam-saeidi/kibana)@[38ea8093aa...](https://github.com/maryam-saeidi/kibana/commit/38ea8093aa140e0da7ee021ed4a1e0f98b05368c)
#### Thursday 2023-11-09 08:53:33 by Vitalii Dmyterko

[Security Solution][Detection Engine] improves new terms rule for multiple fields (#157413)

## Summary

As described in our README for new terms rule type:

> Runtime field supports only 100 emitted values. So for large arrays or
combination of values greater than 100, results may not be exhaustive.
This applies only to new terms with multiple fields.
  Following edge cases possible:
- false negatives (alert is not generated) if too many fields were
emitted and actual new values are not getting evaluated if it happened
in document in rule run window.
- false positives (wrong alert generated) if too many fields were
emitted in historical document and some old terms are not getting
evaluated against values in new documents.

To avoid this and deliver the better experience for our customers, this
PR is moving from current implementation(emitting aggregated values for
multiple new terms fields) towards using composite aggregation for each
page from phase 1, split in chunks by 500.
This allowed to be done due
[order](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-composite-aggregation.html#_order)
of composite aggregation results

NOTE: implementation for a single new terms filed is the same, due to
performance reasons


### Performance measurements

Implementation | Shards | Docs per shard | Simultaneous Rule Executions
| Fields cardinality | Rule Execution Time Runtime field(current
implementation) | On week work
-- | -- | -- | -- | -- | -- | -- 
array of unique values length 10 |   |   |   |   |   |   
Terms 1 field | 10 | 900,000 | 1 | 100,000 | |   
Terms 2 fields | 10 | 900,000 | 1 | 100,000 | 30s  |  41s
Terms 3 fields | 10 | 900,000 | 1 | 100,000 | 40s | 56s

Implementation | Shards | Docs per shard | Simultaneous Rule Executions
| Fields cardinality | Rule Execution Time Runtime field(current
implementation) | On week work 1,000 per batch | On week work 500 per
batch
-- | -- | -- | -- | -- | -- | -- | --
Terms 2 fields | 10 | 9,000,000 | 1 | 100,000 | 19s | 41s | 35s 
Terms 3 fields | 10 | 9,000,000 | 1 | 100,000 | 21s | 52s| 47s 
CPU % | | | | | 400-450% |500-600% | 400-450%

I selected size of the chunk as 500, since it's a bit faster and less
load on CPU

### Considerations on parallel composite search requests in phase 2

When running composite search requests in parallel, noticed significant
CPU increase in Elasticsearch ~ 1,000% for 2 requests in parallel
against ~ 500% for single.
Where win in performance was not that big: ~ 35s for 2 in parallel, 43s
for a single request. I think, having only one request is the better
option to go, that will prevent unnecessary CPU usage

### Test cases
I've added several functional test cases, that ensures, no missing/false
positives alerts are occurring. Applied to the old implementation, they
would fail

### Retry on max_clause_count error
Because we create query, that can have few thousands clauses, it is
possible it may fail due to [the maximum number of allowed
clauses](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-settings.html)
I implemented retry that: If request fails with batch size of 500
(default value), we will try to reduce it in twice per each retried
request, up until 125. Per ES documentation, max_clause_count min value
is 1,000 - so with 125 we should be able execute query below
max_clause_count value

### Checklist

Delete any items that are not applicable to this PR.

- [x] [Unit or functional
tests](https://www.elastic.co/guide/en/kibana/master/development-tests.html)
were updated or added to match the most common scenarios

---------

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [j6t/git](https://github.com/j6t/git)@[8f23432b38...](https://github.com/j6t/git/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Thursday 2023-11-09 09:00:18 by Johannes Schindelin

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
## [BelleNottelling/FOSSBilling](https://github.com/BelleNottelling/FOSSBilling)@[b3321a8dd3...](https://github.com/BelleNottelling/FOSSBilling/commit/b3321a8dd33dfbd084899709a37b7e3a5c626300)
#### Thursday 2023-11-09 09:56:07 by Adam Daley

Update to Sentry v4 (#1780)

* Bump minimum PHP version to 8.1

* Missed these too

* Shit's broke and stupid as fuck

* Update SentryHelper.php

* Update package-lock.json

* I did the fixing

---------

Co-authored-by: Belle Aerni <belleaerni@gmail.com>

---
## [lysnikolaou/numpy](https://github.com/lysnikolaou/numpy)@[af55348f5c...](https://github.com/lysnikolaou/numpy/commit/af55348f5cbe338a86ed032812ee11e8714be673)
#### Thursday 2023-11-09 10:19:01 by Sebastian Berg

API: Allow comparisons with and between any python integers

This implements comparisons between NumPy integer arrays and arbitrary valued
Python integers when weak promotion is enabled.

To achieve this:
* I allow abstract DTypes (with small bug fixes) to register as loops (`ArrayMethods`).
  This is fine, you just need to take more care.
  It does muddy the waters between promotion and not a bit if the
  result DType would also be abstract.
  (For the specific case it doesn't, but in general it does.)
* A new `resolve_descriptors_raw` function, which does the same job as
  `resolve_descriptors` but I pass it this scalar argument
  (can be expanded, but starting small).
  * This only happens *when available*, so there are some niche paths were this cannot
    be used (`ufunc.at` and the explicit resolution function right now),
    we can deal with those by keeping the previous rules (things will just raise
    trying to convert).
  * The function also gets the actual `arrays.dtype` instances while I normally ensure that
    we pass in dtypes already cast to the correct DType class.
    (The reason is that we don't define how to cast the abstract DTypes as of now,
    and even if we did, it would not be what we need unless the dtype instance actually had
    the value information.)
* There are new loops added (for combinations!), which:
  * Use the new `resolve_descriptors_raw` (a single function dealing with everything)
  * Return the current legacy loop when that makes sense.
  * Return an always true/false loop when that makes sense.
  * To achieve this, they employ a hack/trick: `get_loop()` needs to know the value,
    but only `resolve_descriptors_raw()` does right now, so this is encoded on whether we use
    the `np.dtype("object")` singleton or a fresh instance!
    (Yes, probably ugly, but avoids channeling things to more places.)

Additionally, there is a promoter to say that Python integer comparisons can just use
`object` dtype (in theory weird if the input then wasn't a Python int,
but that is breaking promises).

---
## [rmellis/HelpUKR-master](https://github.com/rmellis/HelpUKR-master)@[b79a4d13f8...](https://github.com/rmellis/HelpUKR-master/commit/b79a4d13f8ae1d9617c503b067820c4f1573c3a0)
#### Thursday 2023-11-09 11:21:54 by rmellis

Merge pull request #463 from rmellis/Beta

Beta ➜ Main | Оновлені цілі на день 624
Simply run this for as long as you can to help flood Russia in the most legal, yet effective way possible 
New targets imported from db1000n:
To keep up with targets we're going to use the db1000n targets direct from their GitHub repository. 
These updates will be daily, so if the db1000n changes, it will probably take a few hours longer for the change to make it here.
Message posted by the IT Army of Ukraine:
In 2000, the digital world encountered a new threat: the Distributed Denial of Service (DDoS) attack. Internet giants like Yahoo, eBay, and Amazon were crippled by a flood of traffic from numerous sources, orchestrated by a 15-year-old hacker known as 'Mafiaboy', real-life Michael Calce from Canada. This revolutionary type of attack managed to halt the services of the strongest online platforms of the time.
Today, Michael Calce is not only a respected white-hat hacker but also a legend of cyberspace.
/ *** / 
Просто запускайте це стільки, скільки зможете, щоб допомогти наповнити Росію найбільш законним, але ефективним способом 
Нові цілі, імпортовані з db1000n:
Щоб не відставати від цілей, ми збираємося використовувати цілі db1000n безпосередньо з їхнього сховища GitHub.
Ці оновлення відбуватимуться щодня, тож якщо db1000n зміниться, ймовірно, знадобиться кілька годин більше, перш ніж зміни з’являться тут.
Інформація про цілі:
У 2000 році цифровий світ зіткнувся з новим видом загрози: атакою типу "розподілена відмова в обслуговуванні" (DDoS). Гіганти інтернету як Yahoo, eBay та Amazon були паралізовані потоком інтернет-трафіку з багатьох джерел, організованим 15-річним хакером на прізвисько 'Mafiaboy', в житті Майкл Калс з Канади. Цим революційно новим типом атаки вдалося зупинити сервіси найміцніших онлайн-платформ того часу. 
Сьогодні Майкл Калс це не тільки поважний білий хакер, але і легенда кіберпростору.

---
## [dakaii/djoser](https://github.com/dakaii/djoser)@[4ebdc10add...](https://github.com/dakaii/djoser/commit/4ebdc10add211cb238002fcc79a7cf8409d99825)
#### Thursday 2023-11-09 11:49:50 by github

Fix for Friendly tips when Missing SOCIAL_AUTH_ALLOWED_REDIRECT_URIS

i forget add SOCIAL_AUTH_ALLOWED_REDIRECT_URIS to my config

it return 400 error, i don't know why ,  i pay more time find the issues

so  i add Friendly tips

-- sorry  , my english is not well

and thank you all

---
## [JohelEGP/cppfront](https://github.com/JohelEGP/cppfront)@[cdf71bdca6...](https://github.com/JohelEGP/cppfront/commit/cdf71bdca64536a005f2491d8c19f1d05a1c62f6)
#### Thursday 2023-11-09 12:13:25 by Herb Sutter

Correct copy/move for `union`

By writing separate construction and assignment, plus the new feature of suppressing assignment to a member by writing `member = _ ;` (now allowed only in assignment operators).

I do realize that's an "opt-out" which I normally prefer to avoid, but:

- I considered and decided against (for now) the alternative of not having assignment be memberwise by default. I want to keep the (new to Cpp2) default of memberwise semantics for assignment as with construction. I think that's a useful feature, and normally if you do assign to a member it doesn't arise, and so I think it makes sense to explicitly call out when we're choosing not to do any assignment at all to a member before doing other assignment processing. We'll get experience with how it goes.

- `_` is arguably natural here, since it's pronounced "don't care." There too, we'll see if that is natural generalized, or feels strained. For now it feels natural to me.

---
## [Burger1998/tgstation](https://github.com/Burger1998/tgstation)@[38567fab48...](https://github.com/Burger1998/tgstation/commit/38567fab4806b6dde59013736f6731b5f7fd79fa)
#### Thursday 2023-11-09 12:56:16 by BluBerry016

Rule Of Cool: Nukie Hallway Mosiac (#78726)

## About The Pull Request
Quick history lesson, yes, seriously, this is backstory for this goofy
PR that affects a *single line of tiles*: near the start of this year I
was asked to help work on a project for here that, to my knowledge, is
all but canned now(?) - more specifically, I was asked to [remap the
nukie
base](https://cdn.discordapp.com/attachments/927814428882251776/1070593334269190175/image.png),
a project I didn't get too particularly far into before things went
quiet. Up at the top-right there you can see I was starting to
experiment with some, quote, "sick-ass designs" using the syndicate
emblem turf decal, which later became
[this.](https://cdn.discordapp.com/attachments/1040395260922183700/1158248386537996350/image.png)

Not anything all too impressive, but it was still fun to work on
(special shoutout to putting the assault pod into a implied
slinglauncher, that was cool as fuck) - that all said, I recently
*remembered* that exercise... which's led to this PR.
### So what does this PR **actually** do?

Simple. Edits this single line of tiles to have a neat, snaking design
on 'em. Yyyyep. That's it.

![image](https://github.com/tgstation/tgstation/assets/50649185/4d00fd35-0bb5-4d44-9efa-56db302dc1e1)

## Why It's Good For The Game
Honestly it's just pretty neat looking. On a related note from my
experimentation, if we ever get diagonal trimline turf decals, you could
pretty easily repurpose the `syndicateemblem/top/left` decal to make a
little Interdyne Pharmaceuticals logo following the design on the
shipping containers.
## Changelog
:cl:
add: The funds the syndicate have been saving by restricting galley
access has been suddenly funneled into a singular mosaic pattern in the
experiments wing.
/:cl:

---
## [Burger1998/tgstation](https://github.com/Burger1998/tgstation)@[1053f00082...](https://github.com/Burger1998/tgstation/commit/1053f00082ec8c6c52412e780d0e739295fdbfe7)
#### Thursday 2023-11-09 12:56:16 by Emmett Gaines

Fixes display of appearance type in VV (#78725)

## About The Pull Request

Appearance vars are awful to detect. They have a type var you can
access, for an appearance the value of this var is `/image`. However
`istype(appearance, /image) == 0`. This is good enough for
identification, you might think this just means detecting appearance
would be something like `if(thing.type == /image && !istype(thing,
/image))`, but there's a problem with this: `istype(appearance, /datum)
== 0`. For that matter it seems like all istypes that check if an
appearance is some type fail, so you can't know that it's safe to access
the `.type` var to do that earlier combined check.

Now we get into magic territory, `istype(new /image, appearance) == 1`.
I have no clue internally why this is the case but it seems to be unique
to appearances, and so can be used to identify them from a previously
unknown var. You have to rule out that the thing you're checking is a
path, it would pass the check if the value were `/image` then, but this
is simple enough.

I hate having to know all this, so now you know this too.

:cl: ninjanomnom
admin: Appearance vars in VV now display instead of being left blank
/:cl:

---
## [hatcatter/HackEM](https://github.com/hatcatter/HackEM)@[ece38e6a5e...](https://github.com/hatcatter/HackEM/commit/ece38e6a5e07ea45e1b92e36bf60c3d03251fd3d)
#### Thursday 2023-11-09 12:57:17 by Erik Lunna

Phoenix egg tweaks. In the spirit of making phoenixes a recurring force to be reckoned with, they will hatch if the player attempts to eat, bury, or confine them in a container. In the previous commit, I allowed their eggs to be canceled, but I modified the chance to roll against the innate MR of the phoenix - so there is now only a 60% chance of success when trying to cancel. Dipping a phoenix egg in a potion of amnesia will always sterilize the egg however.

Polymorph needed to be addressed as well, because one could just zap a phoenix with polymorph and be rid of the pest. So now, when a phoenix doesn't naturally resist a polymorph, it will violently resist and explode, always reverting to it's egg form. This also entailed protecting phoenix eggs from polymorph, because without that protection, the polymorph beam would always poly the egg immediately after the phoenix exploded.

Lastly, in order to avoid some weird philosophical issues and gameplay paradoxes, I added the NOPOLY tag to the phoenix so the player can never take their form.

Thanks to Noisytoot for inspiring these ideas with the observation that phoenix eggs could simply be placed in a container (similar to zombie corpses). Phoenixes should have a special place in Hack'EM so they are revered and despised, plus they add significant value to potions of amnesia.

---
## [dlahn/opentelemetry-ruby-contrib](https://github.com/dlahn/opentelemetry-ruby-contrib)@[e5ba8854bf...](https://github.com/dlahn/opentelemetry-ruby-contrib/commit/e5ba8854bf33140cabfc72198167678291f56c04)
#### Thursday 2023-11-09 13:08:53 by Andrew Hayworth

ci: do not test a config that will never succeed (#388)

In this test, we are asserting that the instrumentation is _not_
installed when the `Rack` constant is not present (see the `before`
block for this test case). We then go on to test that the configuration
is the "default" configuration that you'd get with a fresh installation.

The problem is that if the `Rack` constant is not present, then the
`instrumentation-base` code that sets all the defaults for our options
is never run (and logically, why would it?). So these test lines can
never actually succeed.

Unless, of course, the `instrumentation` object we're referring to is
_not_ a pristine, new object. And in fact, depending on what order the
tests run in, our object is _not_ a pristine, new object. If you run
basically any _other_ test in this suite before, then we actually end up
recycling an object that is partially initialzied from a previous test,
and has an internal `@config` object that has some default options.

And so, the test is actually passing some times because of this
non-deterministic behavior. For example, if you run with `SEED=1`, then
the test suite passes (because other tests run first that initialize the
object completely). If you run with `SEED=6372`, it fails (because it is
the very first test run).

The _real_ bug here is that we do not have proper test isolation. I
think that's actually a problem all over the code base, if I'm being
honest about it.

However, I elect not to fix that problem today. We'd need some way to
"reset" instrumentation and the registry in between tests (maybe not
_that_ hard, honestly). That's more than I want to do on a Saturday
afternoon. So to fix the current issue, we just don't bother testing
things that logically could never pass anyways. What we actually care
about is that the instrumentation reports it was not installed, which
does work correctly as it is.

Fixes #387

---
## [Decuwu/FemboyV3](https://github.com/Decuwu/FemboyV3)@[1fd59b0569...](https://github.com/Decuwu/FemboyV3/commit/1fd59b05694e94a45a66416d8eb86c37a040325a)
#### Thursday 2023-11-09 13:19:45 by Decuwu

v3.9.0

# Changelog 3.9.0
- Added Randomise Outfit
- Added Lazer Sight
- Added "protection" for Tazer Crash
    - will break missions that require a ped to be in your car
    - will delete hookers :3
- Added Demi-God for other players
    - for both all and selected players, will heal players when they have taken damage. DOES NOT MAKE THEM INVULNVERABLE
    - does not work if they are in a car
- Added Car Follows You
    - Last used car will constantly follow/try to get to you
- Added ladder to heaven
    - was bored, enjoy ig 
- Fixed bail from session
- Added check for missing loading sprite -- thanks for reporting Mia

---
## [fira/cmss13](https://github.com/fira/cmss13)@[830e002a27...](https://github.com/fira/cmss13/commit/830e002a27b7b4115815e450b8506832cb403a02)
#### Thursday 2023-11-09 13:52:45 by QuickLode

Adds a Colony Synthetic variant, with bug fixes (#4760)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

1. should fix fax machine problem(thx forest)
2.  gives trucker synth the frontier jumpsuit(Thwomplert)
3. adds Freelancer Synthetic. This Synth is one that was bought off a
civi market and reprogrammed, or stolen and reprogrammed, or hacked, You
get the point - its going with a band of freelancers. The idea behind it
is that this synth's team is dead and they are just programmed as a merc
for pay - hoping to someday find their boss boss and give the money as
set up. I always thought about this one for a long time and decided to
put him in the civilian category, where its hard to roll and also gives
you freedom to choose your allegiance. In this case I hope that a
freelancer synthetic will open up unique avenue of RP and allegiance.
I've only explored it once ingame, but it was very good for RP!
Hopefully people can recreate this success.

was hard to make this guy look cool and I also wasn't sure on what his
loadout would be. I ended up giving him random generic stuff while
looking like a beat up freelancer(missing the armor especially hurt his
look, since thats the largest piece of a freelancer - the curiass, but I
don't want to give armor for balance reasons) and no beret because its
for a SL only.

as usual, if a synth wants to change RP avenues and don different
clothes for different RP, no one would know the difference
# Explain why it's good for the game
1. bug bad
2. a beat up UA laborer that so happens to be synthetic. you wouldn't
expect it because there's so many similar looking people! exactly the
job of a synth - to blend in.
3. Freelancer colony synth hopefully will open up a unique avenue of RP.
If they don't want to they can always ditch it - but its on a relatively
rare and uncommon roll anyways.
# Testing Photographs and Procedure
<details>
<summary>[Screenshots &
Videos](https://cdn.discordapp.com/attachments/490668342357786645/1166307813719556187/image.png?ex=654a03cb&is=65378ecb&hm=7108218bbaab61c78c0bedcecbfdcc07bdf9db87a3fefe9fb94b28d3430cc815&)</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: adds another Colony Synthetic variant, changes up some existing
ones(trucker,CMB)
fix: fixes a small problem with WY-Colony Synthetic access(thx forest),
adds WY subtype of Synthetics for admin building/faxes
fix: fixes problems with organic spawning ferret industries Trucker
Synthetic
/:cl:

---
## [NitkarshChourasia/Python-Programs](https://github.com/NitkarshChourasia/Python-Programs)@[a82f1576c3...](https://github.com/NitkarshChourasia/Python-Programs/commit/a82f1576c32bc3497afa6cb67bdf2f28ce4a2f91)
#### Thursday 2023-11-09 14:02:47 by Purshotam Bohra

Create gstin_scraper.py

Hello owners, this is just a small and beautiful script (pun intended) that demonstrates use of beautifulSoup to extract practical data.

GSTIN, short for Goods and Services Tax Identification Number, is a unique 15 digit identification number assigned to every taxpayer (primarily dealer or supplier or any business entity) registered under the GST regime in INDIA.

I created this script back in 2021, when one of my brother required this for his startup business and today when I saw this repo and it's inclusiveness for all sorts of crazy python script I desired to include this crazy adventure of mine.

Although the original version was bit messier but I refactored it according to current best standards.

Hope for a positive commity commity.

Thank you so much,
Purshotam Bohra

---
## [EaW-Team/equestria_dev](https://github.com/EaW-Team/equestria_dev)@[0c55aebcae...](https://github.com/EaW-Team/equestria_dev/commit/0c55aebcae844d845ab72d6a9fc2e428290d6d59)
#### Thursday 2023-11-09 14:33:17 by Mustafa Alperen Seki

Actually add the FAT female generics.

My stupid ass saved them to wrong place and forgor to copy them to the repo, my fault not resting it.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[81a7c75583...](https://github.com/timothymtorres/tgstation/commit/81a7c75583f75f76d8487b88e63ebaf1402af85b)
#### Thursday 2023-11-09 14:36:16 by necromanceranne

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
## [nobodyiam95/react](https://github.com/nobodyiam95/react)@[1ebedbec2b...](https://github.com/nobodyiam95/react/commit/1ebedbec2bec08e07c286ea6c3cff62737a0fd3a)
#### Thursday 2023-11-09 15:03:16 by Sebastian Markbåge

Add Server Context deprecation warning (#27424)

As agreed, we're removing Server Context. This was never official
documented.

We've found that it's not that useful in practice. Often the better
options are:

- Read things off the url or global scope like params or cookies.
- Use the module system for global dependency injection.
- Use `React.cache()` to dedupe multiple things instead of computing
once and passing down.

There are still legit use cases for Server Context but you have to be
very careful not to pass any large data, so in generally we recommend
against it anyway.

Yes, prop drilling is annoying but it's not impossible for the cases
this is needed. I would personally always pick it over Server Context
anyway.

Semantically, Server Context also blocks object deduping due to how it
plays out with Server Components that can't be deduped. This is much
more important feature.

Since it's already in canary along with the rest of RSC, we're adding a
warning for a few versions before removing completely to help migration.

---------

Co-authored-by: Josh Story <josh.c.story@gmail.com>

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[f3d81edb00...](https://github.com/mc-oofert/tgstation/commit/f3d81edb00b07160bc046ab0d79457e60aefba0e)
#### Thursday 2023-11-09 15:55:40 by Paxilmaniac

Improves the deployable component (#79199)

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

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[eb9da97b7d...](https://github.com/mc-oofert/tgstation/commit/eb9da97b7da54f9bdce32aa29ec972f469625ed2)
#### Thursday 2023-11-09 15:55:40 by GoldenAlpharex

Adds support to the wet_floor component to avoid displaying its overlay, makes ice turfs no longer receive said wet overlay (#79275)

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

---
## [Opentrons/opentrons](https://github.com/Opentrons/opentrons)@[30425f7a3b...](https://github.com/Opentrons/opentrons/commit/30425f7a3bd4a7ddb8ba9d3c14b05cdff13ccf34)
#### Thursday 2023-11-09 16:23:01 by Seth Foster

feat(app): Update robots from USB flash drive (#13923)

* feat(app-shell-odd): watch for USB drives

The Flex operating system automatically mounts the filesystems of
well-formatted USB drives (FAT and ext4 and maybe ntfs but that's a bit
iffy) to /media when those USB drives are inserted on the robot. In
theory it will in fact do this for _any_ kind of media that presents a
filesystem interface.

To that end, add a node task that will use a node filesystem watch to
keep an eye on /media, and
- when something that looks like a USB drive (/media/sd\w\d+) appears,
notify via redux actions
   - then enumerate all the files on it and notify those via redux
   actions
- when something we were keeping an eye on disappears, notify via
redux actions

The redux actions don't alter state and so don't need new reducers or
selectors; they exist because it's a handy mechanism to talk between our
components.

This code is very tightly coupled to the way the node fs interfaces work
and so I don't see a lot of point in unit tests for it; it's almost
entirely fs calls originating everything and providing all of the data,
and all the complexity is from working around weirdnesses in those calls
and in the underlying system. For instance,
- There's a little bit of time in between when the fs watch on /media
fires and when you can actually find the contents of the newly-present
directory; if you readdir before that you'll get an empty list, so we
wait a second
- The node fs.watch interface looks very fully features but is
absolutely chock-full of warnings about various features not being
reliable. A lot of that unreliability is _probably_ across systems and
everything works as we expect on linux, but just in case we have a lot
of fallbacks for if our callback doesn't get filepaths, etc

* fix(app-shell-odd): handle errors in readstreams in http.post

We have our custom http interface that wraps around node-fetch that
provides things like "doing your own read stream when posting a file",
and "mapping everything into the promise interface", which is nice,
but has an issue specifically for that read stream: we don't monitor
errors on it. Read streams surface errors by emitting an 'error' event;
we hook up a listener to that error event _while we're creating the
stream_, but then we disconnect it. So if you have an error in the
stream - for instance, you're reading from a file on a USB flash drive
and the user unplugs the flash drive - then the error will never get
surfaced.

Unfortunately the fix to this is a bit fiddly. We can hook up an error
listener fine, but it needs to do something; specifically, it needs to
turn the error from a callback into a promise rejection. That means it
needs to have a promise to reject that has the same lifetime as the
stream itself. http.post didn't provide that because it returns a whole
big promise chain, and each time you move a link in that chain the old
promise is gone and a new one happens, so we'd need to move the listener
around.

Since promises are monadic, a better fix is to have post return a single
promise and do all the promise chaining _inside_ that promise; then, the
read stream error handler can reject the outer promise directly, while
relying on promises bubbling up rejections to preserve error handling
capability for the promises in the internal chain.

* fix(app): Poll for updates on the ODD

Though we have everything set up to automatically fetch, prompt for, and
execute robot updates from the ODD, we weren't actually _checking_ for
those updates except once on boot (which then wouldn't work if the robot
wasn't internet-connected during boot). This means in particular that
the software updates during onboarding were guaranteed to fail.

We can use the same hook in the ODD app root that we do in the desktop
app route, but if we're going to do that then we better remove a log
message that suddenly becomes extremely spammy.

* feat(app-shell-odd): Supply "system updates" from flash drives

Adds the capability to provide system updates from flash drives to the
ODD app-shell.

These are "system updates" in that the app-shell determines their
availability and provides it to the app, rather than the user indicating
the presence of a file alongside their intent to update. The app-shell
will advertise the flash drive updates in the same way it advertises
internet-discovered updates, with a RobotUpdateInfo redux message; since
those now provide the path to the file they mean, it will be easy for
the app to specify the system update to load.

We can duplicate the logic that we use for system updates by adding a
second let cache for the "current update"; the system-updates code will
then prefer an update in the mass storage update cache to an update in
the old system updates cache, and send new robot update info messages in
all the state changes between neither cache being full; either cache
being full; and both caches being full.

The determination that a flash drive system update is present is
triggered by a mass storage enumerated message; when that flash drive
gets removed, we'll get a removal message.

To figure out whether updates are actually present, we can the list of
files that just got enumerated for things that end with .zip, and then
try to open them as zip files and read the VERSION.json information out
of them. This is a somewhat fraught process; the file could not be a zip
file, it could be a zip file but corrupted, it could be a zip file but
not an update, it could be an update but it's for an OT-2,  and we need
to handle all that, so there's a pretty excessive amount of error
handling in here. Once we're sure that there are one or more zip files
containing robot system updates, we can provide something to redux; we
provide the highest-version update present.

There is one way in which updates from flash drives differ from system
updates found on the internet, however: plugging in a flash drive
requires user intent, while checking for updates on the internet
doesn't. Therefore, if the user plugs in a flash drive with an update
file, we always want to make that update file available no matter the
relative versions of the robot and the update file. So we can add a bool
to the system update message (and then to the update state) that shows
that this is a "forced notification" update, and the app can know to
display it without caring about the upgrade/downgrade/reinstall state.

Since there's a lot of duplication, we can also factor out some common
logic to make it feel a little better.

That process of duplication also fixes a bug that would have prevented
the ODD from ever prompting for updates. The function that gets
information about updates used the same promise to read the release
notes and provide the update information; but we overrode the downloaded
release files to null out the release notes, meaning that promise would
always fail, and we'd never get the notification. We no longer override
the release notes to be null, and we also treat reading the release
notes separately from reading the rest of the update.

* feat(app): allow robot updates from USB files

Now that the odd app-shell provides us with notifications of updates
from USB flash drives, we can allow the user to install them. While the
redux mechanisms allow this pretty easily - a system update is a system
update, after all, and with the force mechanism the app wouldn't even
know if the update was a downgrade or anything - we ran into a problem
where the general robot update machinery in the ODD was very tightly
bound with the onboarding experience for the ODD, since that's the
context in which it was developed.

This commit extracts the robot update mechanisms from onboarding by
- Hoisting onboarding-related logic out of lower level components and
instead injecting that logic into the organisms code from the top level
page
- Moving the current update page to a new one that is focused on
onboarding at a new route, and copying just the update-related code to
a generic RobotUpdate page

This means that the two pages - RobotUpdate and
RobotUpdateDuringOnboarding - share most of the same code but are bound
to different routes and can have different top level behavior by
injecting different contexts to the finish and error handling behaviors
of the update. RobotUpdateDuringOnboarding sets the unfinished
onboarding page breadcrumbs appropriately, and uses display language
appropriate to the update being just a component of the larger workflow,
and moves on to estop handling when cancelled; RobotUpdate doesn't touch
any of that, and goes back to the settings page when cancelled, and uses
wording more appropriate to being its own topline flow.

Closes RAUT-829

---
## [SomeguyManperson/Yogstation](https://github.com/SomeguyManperson/Yogstation)@[274c21e88b...](https://github.com/SomeguyManperson/Yogstation/commit/274c21e88bb7d291188caf1a1058b10497cd9295)
#### Thursday 2023-11-09 16:30:27 by Molti

[PORT] help, i just wanted to give visuals to being wet, now i've ported an entire fire_stacks refactor (#20735)

* oh god

* Update atoms_movable.dm

* Update atoms_movable.dm

* oh god oh fuck what have i done

* Update life.dm

* Update Hallucination.dm

---
## [MGOOOOOO/tgstation](https://github.com/MGOOOOOO/tgstation)@[d1ad9b6658...](https://github.com/MGOOOOOO/tgstation/commit/d1ad9b665823708c3ae651eb9729023968e7feaf)
#### Thursday 2023-11-09 16:40:02 by necromanceranne

Nukie Update Followup: Returns CQC to the previous price range, Core Gear kit for newbies, hat stabilizers for everyone (#79232)

## About The Pull Request

Brings the CQC kit back down to the same price range of 14 TC (it's 1
more than before weapon kits). It feels like currently that CQC is
overpriced, even with the stealth box coming along with it, and by
comparison the energy sword and shield got a huge value increase by
combining the two. They're both melee styles and also equally difficult
play styles. It isn't really necessary to make one more expensive than
the other. Also now comes with syndicate smokes. It's a whatever change,
ops get these for free on the base.

Adds a core gear kit in the weapon category. This kit comes with a
doormag, a freedom implant, stimpack and c-4 charge. All of these are
items almost every nukie buys if they want to succeed, so let's inform
newer players by putting it RIGHT on top of the list. This isn't at any
discount, this is mostly to help inform players what items help make you
successful.

Hat stabilizers are now a part of every syndicate modsuit for FREE. It
comes built in, can't be removed, and has no complexity cost. Now
everyone can wear their wacky hats as they operate.

## Why It's Good For The Game

CQC felt like it got shafted waaay too hard with the weapon case
changes. Definitely don't believe that it is punching at the same weight
as many of the other high cost weapons. So we've dropped it down a
category. 14 TC is still a large upfront cost, even if it comes bundled
with a lot of goods.

Melbert gave me the idea of a core bundle kit to help newer players and
I was really taken with that. So I added it as part of this followup.

I want people to wear their hats goddamnit, and I didn't learn my
mistake with the tool parcels. So now everyone has hat stands on their
suits. WEAR THE SOMBRERO YOU **FUCK**.

### THIS IS NOW A THREAT.

## Changelog
:cl:
balance: Operatives can once again read about the basics of CQC at a
reasonable price of 14 TC.
qol: All Syndicate MODsuits come with the potent ability to wear hats on
their helmets FOR FREE. No longer does any operative need be shamed by
their bald helmet's unhatted state when they spot the captain, in their
MODsuit, wearing a hat on their helmet. The embarrassment has resulted
in more than a few operatives prematurely detonating their implants! BUT
NO LONGER! FASHION IS YOURS!
qol: There is now a Core Gear Box, containing a few essential pieces of
gear for success as an operative. This is right at the top of the
uplink, you can't miss it! Great for those operatives just starting out,
or operatives who need all their baseline equipment NOW.
/:cl:

---
## [Oyu07/Paradise](https://github.com/Oyu07/Paradise)@[dcd1f5d88a...](https://github.com/Oyu07/Paradise/commit/dcd1f5d88a8c5ba9634fc3fce67a76ada45f71dc)
#### Thursday 2023-11-09 16:48:38 by Octus

Adds eight vox hairstyles because why not and stuff (#22573)

* god i hate myself

* donedone

* fixxxxx

---
## [semrush/intergalactic](https://github.com/semrush/intergalactic)@[13a8ca3e6c...](https://github.com/semrush/intergalactic/commit/13a8ca3e6caf5e7b566f5eaa06d48c2b1a608420)
#### Thursday 2023-11-09 17:13:24 by Michael Sereniti

[utils, website] fixed old palette resolving and also fixed palette view on website (#873)

## Motivation and Context

The color resolver contained a very stupid mistake that was making using
old color palette impossible. It has been existing in our codebase for
about two weeks and it's insane that we haven't spotted it.

Basically it was removing `--` prefix from variable name and then was
checking does this variable exist in map where all names had prefix
`--`. So our potential users had to use `----{variable_name}` syntax if
they were trying to overcome the issue.

## How has this been tested?

The fix is clear.

## Types of changes

<!--- What types of changes does your code introduce? Put an `x` in all
the boxes that apply: -->

- [x] Bug fix (non-breaking change which fixes an issue).
- [ ] New feature (non-breaking change which adds functionality).
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected).
- [ ] Nice improve.

## Checklist:

<!--- Go over all the following points, and put an `x` in all the boxes
that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're
here to help! -->

- [x] My code follows the code style of this project.
- [x] I have updated the documentation accordingly or it's not required.
- [x] Unit tests are not broken.
- [x] I have added changelog note to corresponding `CHANGELOG.md` file
with planned publish date.
- [ ] I have added new unit tests on added of fixed functionality.

---
## [KikoWen0/NebulaStation](https://github.com/KikoWen0/NebulaStation)@[404a7cd290...](https://github.com/KikoWen0/NebulaStation/commit/404a7cd29063f00078f85d8171612085a611b271)
#### Thursday 2023-11-09 19:00:24 by san7890

Fixes Space Dragon Attacking (#78964)

Fixes #78953

## About The Pull Request

Basically the gist is that Space Dragon's special attack code was on
`AttackingTarget()` rather than whatever the hell simple animals
controlled by clients use (I didn't bother enough to look into the chain
to remember this). This was the complete wrong proc to use, and it NEVER
got executed. Anyways, we just hook into the signal for whatever the
simple animal proc is as well as clean up all the code, make everything
pretty, and most importantly:

MAKE THE DAMN CODE WORK
## Why It's Good For The Game

Either someone did not test their code at all, or some weird esoteric
change in the attack chain changed this somehow? I'm not sure when or
why this happened but it is guaranteed to be fixed now.

The code cleanup and tinkering I did means that it's gonna be about 10%
easier to port this over to a basic mob eventually (not doing a full
refactor when this shit is this broken, the code added here is modular
enough to the point where it's plug-n-play).
## Changelog
:cl:
fix: Space Dragons can now, once again, tear down walls and eat corpses.
They also have regained their special damage modifier when attacking
mechs.
/:cl:

---
## [carpentries/sandpaper](https://github.com/carpentries/sandpaper)@[44ef4d8fef...](https://github.com/carpentries/sandpaper/commit/44ef4d8fef4e98637cb000f9861839e3e35eeda9)
#### Thursday 2023-11-09 19:08:55 by Zhian N. Kamvar

reset metdata for handout test

This is one of the weird litte things that I need to get better at
controlling. When we test these things, the global metdata is affected,
but it's not possible (at the moment) to _remove_ metadata without
resetting everything, so instead, we need to set the global metadata
option for "handout" to NULL.

In the words of the author of a C++ library that I rewrote in R for my
Ph. D.:

> This is a bloody awful nasty hack ... and will give us grief
> elsewhere. Find a better way to do this

---
## [sethp/learn-gpgpu](https://github.com/sethp/learn-gpgpu)@[cf9701c799...](https://github.com/sethp/learn-gpgpu/commit/cf9701c7998b6a4f2756d9299c5e9b86080f5601)
#### Thursday 2023-11-09 19:21:42 by Seth Pellegrino

feat: start splitting up tcf file (w/ ENTRY)

The TCF (talvos command file) is doing three things for us:

1. Defining inputs and outputs; in the case of vecadd, that's vectors a,
   b, & c. Besides allocating storage for these, it's also populating
   them (SERIES / FILL) and presenting them (DUMP).
2. Invoking the kernel with a particular "shape": MODULE points to the
   kernel sources (which is superceded by our editor), ENTRY says where
   to jump into that module, and DISPATCH invokes it.
3. Binding the first two together; that's what (I believe)
   DESCRIPTOR_SET is doing, and that's what would happen with multiple
   ENTRYies/DISPATCHes referencing the same set of descriptors/buffers.

(It's also got a fourth job in talvos-land: the `# CHECK` comments serve
as a "blessed" output that the testing framework looks for, but we're
not doing anything with those.)

The first two, and especially how they map to each other, are key
intutions for learners to build, so we've got to take over those
behaviors to try and find a more accessible way to build that
understanding. The last one I don't understand well enough yet, but I
suspect it's accidental complexity from Talvos' particular construction
that we ought to be able to roll into the other two.

Either way, this change starts the process of unwinding the TCF spring
and mapping it into what are ultimately DOM elements in the browser. The
particular mechanism for doing this is an experimental approach to try
and solve these two related challenges:

1. (transparency) Exposing details of Talvos' model through the
   WASM<->JS barrier right now is a lot of rote steps; the tools that I
   was able to evaluate (embind, WebIDL) for smoothing this part out
   didn't seem to offer very much utility (mostly requiring the same
   rote steps, just in *their* bespoke DSL). Instead, this approach
   attempts to read the internal model state as directly as possible, so
   that minimal source changes (/ spurious copies) are required to bind
   to a new property.

2. (efficiency) Briefly; the WASM "linear memory" is embedded in the
   javascript heap. The browser's execution engine, therefore, can read
   & write it "for free," but anything that we want Talvos to operate
   over needs to be inside that segment for it to be visible. So, we
   *simply* choose to allocate shared things inside the linear memory
   directly, and pass around references to avoid copies!

Curious readers might note that our strategy implies that now JS-land
and C++-land have to agree about the representation of various data
structures & objects; a challenge that neither ecosystem accepts
willingly. But, ABI stability is just a social contstruct, after all.
Given the very specific build conditions we're using on the talvos side
(a pinned libc++, clang, emscripten, the works), we should at least have
warning when it's being broken, and options around timing of uptaking
changes.

Conditions under which `lib/binding` might be removed include:

- A better answer from the broader WebAssembly community; this is an
  area that's actively being worked on, but it's a little impenetrable
  to me at the moment whether any of the answers meet our needs and how to
  use them.
- Re-writing Talvos in javascript to eliminate WebAssembly as a
  dependency; that would be a shame as this is (or, ought to be)
  WebAssembly's sweet spot.
- If the maintenance burden ends up being too high, then re-writing the
  mapping in either aforementioned tool (embind, WebIDL) ought to also
  do the job.

Also included in this too-big change are:

1. An experiment with memory benchmarking that ~kinda works,
2. Efforts to understand what kinds of JS v8 finds easier or harder to
   execute; unfortunately, the resolution of the `tinybench` framework
   that's built-in to `vitest` is only 1ms, so it's waaaayyyyy too
   coarse to be super useful to us.
3. A wild hair about implementing a teensy-tinsy (~1 instruction)
   function in WASM to speed up bit-twiddling in `BitSet`; sorry, when I
   get sad I make thinks faster and this was a sad week for me.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a5fabd8819...](https://github.com/tgstation/tgstation/commit/a5fabd881961cc0c26fdcc93a23a973af1c5cdc3)
#### Thursday 2023-11-09 19:49:19 by Profakos

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
## [Mirag1993/mrdg](https://github.com/Mirag1993/mrdg)@[70463ae71b...](https://github.com/Mirag1993/mrdg/commit/70463ae71b7d639eecea572d3251562c5ffef68b)
#### Thursday 2023-11-09 21:03:24 by Mirag1993

Reworks The Visuals Of Independent And Nanotrasen Captains (#2453)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

Does what it says in the title. This is a demented PR that touches a lot
of things, but its main benefit is that now regular independent
captains, cowboy independent captains, and nanotrasen captains have a
unique identity.

Of those changed, it includes:

- The Nanotrasen Captain (parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/48a31cb1-b266-43cb-9b6e-525028893011)

- The Nanotrasen Captain (regular)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/799c88f0-b7ce-4736-956d-2e9c0a096433)

- The Independent Captain (regular/parade)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/17ecb3d3-5f2f-4ce0-a518-81366945ebdf)

- The Independent Captain (western)

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a56a798c-5adf-41d7-917a-730661f306ed)

The PR also axes a bunch of unused, or frankly quite basic lieutenant
outfits that were nothing more than set dressing with not much substance
behind them. The roles were not removed for now, and they have
appropriate outfits as a placeholder pending a full removal.

This also means that the Head of Personnel was slightly touched up,
mostly by having a coat and hat similar to the western captain's when
appropriate. The role itself is pending a full visual rework for later
that is beyond the scope of this PR.

Speaking of removals, this also means that captain outfits/roles that
were there as a legacy of removed ships, were finally axed for good.
Goodbye deserter captain for Riggs variant number 4, you will not be
missed.

This PR also touches several (a lot) of maps, mostly adding/removing
outfits that were either missing, or didn't fit with the dress code of
the vessel.

Also the PR fixes an oversight by @MarkSuckerberg by making the BYOND
version warning an actual warning, instead of an error when compiling.
Etto bleh.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

Visual cohesion is important, and dear fucking god if I see one more
independent western captain not wearing the duster because it wasn't in
the ship, I will weep, and my weeping will cause a biblical deluge.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

:cl: PositiveEntropy
imageadd: Outfits for independent and Nanotrasen captains have been
violently reworked.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [distributivgesetz/tgstation](https://github.com/distributivgesetz/tgstation)@[6bdf052a84...](https://github.com/distributivgesetz/tgstation/commit/6bdf052a84c07ff54065dd7906d9c9da540a07b8)
#### Thursday 2023-11-09 21:26:18 by lizardqueenlexi

Converts cursed heart effect into a component. (#78554)

## About The Pull Request

Fixes #58401 
Fixes #58799
Fixes #58800

Converts the manual heart-beating effect of the cursed heart into a
component.

Behavior has mostly been maintained, but polished a bit as compared to
the original cursed heart. Most notably, the action for beating your
heart is now a cooldown action - providing a visual indicator of when
you can beat it again, rather than leaving you guessing. Some better
checks have also been put in place for edge cases such as having your
species changed.

Implementation inspired by the existing "manual blinking" and "manual
breathing" components. Currently only used by the cursed heart and the
(now majorly simplified) effect of corazargh.

My first component, so hopefully I didn't miss anything.
## Why It's Good For The Game

The cursed heart was kind of unusably bad - which may have been part of
the intent, but having to count in your head or spam-click the button is
just annoying. With a visual indicator of when you should beat your
heart, hopefully it will be slightly less awful for the cursed.

The real motivation here was that corazargh's implementation was kind of
a travesty - summoning a cursed heart inside of your body while it was
in your system, then restoring your old heart afterward. This was
error-prone as well as just being ridiculous. Making this effect a
component gets rid of these problems, and leaves space open for new uses
of manual heart beating if anyone feels like being cruel.
## Changelog
:cl:
fix: Your heart will no longer be deleted if an admin heals you while
you have corazargh in your system.
refactor: The cursed heart has been streamlined a bit, and now gives you
a visual cooldown for when you can beat your heart again.
/:cl:

---
## [distributivgesetz/tgstation](https://github.com/distributivgesetz/tgstation)@[66a1cd6ab2...](https://github.com/distributivgesetz/tgstation/commit/66a1cd6ab2c46d84c6773d94fabb08f10c3e6fcd)
#### Thursday 2023-11-09 21:26:18 by Wallem

Adds The Hand of Midas, an ancient Egyptian gun. (#78699)

## About The Pull Request
Adds the Hand of Midas (HoM), a weapon for pirate captains.

This matchlock pistol is powered by gold rather than gunpowder.
If you hit someone with it, they will be afflicted with Midas Blight for
a duration of time that scales with how much gold is in your gun.
Midas Blight will slowly turn their blood into gold, and slow them down
depending on how much blood is in their system.
If you right-click on someone with the HoM, it will siphon all gold from
their bloodstream and recharge the gun, curing them of Midas Blight in
the process if they still have it.
The amount of gold you can get from people is meant to be ~1.5x as much
as you fired into them in the first place, if you get your timing right.
This way you can exponentially scale the power of your weapon if you can
hit your shots, with a limit of 30 Seconds on the Blight timer.
The siphon has a range of 2 meters, and if you miss a shot you can input
a gold coin into the gun to refill it with the same weak shot you
started with.

It's a little hard to explain in text so here's some video examples:


https://github.com/tgstation/tgstation/assets/66052067/d49238fc-beb2-4ba9-be0c-83e8a701c995


https://github.com/tgstation/tgstation/assets/66052067/34dc23e7-2b88-4ee9-bb1e-c8067a491975


https://github.com/tgstation/tgstation/assets/66052067/68a07426-ba6c-43a7-8228-132fc4b02b83

## Why It's Good For The Game
Honestly I just had the idea for the gun and thought it would be really
cool lmao.
Also because Barrel Behind the Door is one of the funniest YuGiOh cards,
the censored design is TOO GOOD.


![image](https://github.com/tgstation/tgstation/assets/66052067/7c930287-410d-43bd-8731-0f7224b9f049)
## Changelog
:cl: Wallem
add: Adds The Hand of Midas, an ancient Egyptian matchlock pistol.
/:cl:

---
## [Imaginos16/Shiptest](https://github.com/Imaginos16/Shiptest)@[590e8cb752...](https://github.com/Imaginos16/Shiptest/commit/590e8cb752400295fe770c303cf5b65a0089fc97)
#### Thursday 2023-11-09 22:04:55 by Imaginos16

Adds the Inkwell-class Supply Freighter (#2385)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## Wait, isn't there a freeze right now?
Correct, there is a ship freeze currently, but I have received
permission from @Apogee-dev to create the PR for this vessel, as it was
a ship I've been working on since at least early-to-mid August.

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/653635cc-b83d-44d8-a9e3-384ffbd9367b)

If any other maptainer would like to overrule Apogee, I'd be more than
happy to temporarily close the PR. Until then, here it is!
## About The Pull Request
Hello everyone! Mr. SolGov here again to add yet another ship to be
tested!

This PR adds a completely new vessel, that being the **Inkwell-class
Supply Freighter**, a ship known for its vast cargo space!

![2023-10-13 13 54
57](https://github.com/shiptest-ss13/Shiptest/assets/77556824/9a70d97e-ab17-45af-a690-e528574b95cb)

![2023-10-13 13 54
59](https://github.com/shiptest-ss13/Shiptest/assets/77556824/2d9d6d0a-85e2-4c46-9754-d49f15be0560)

With extra starter money, three sonnensöldners, and three miners,
players can enjoy completing bounties like no tomorrow, have drinks with
their crewmates in peace, and supply other SolGov vessels with much
needed equipment in less time than you can say "I ran out of ammo!"

Notable things in this ship include:
- Turrets (with IFF!)
- A bar!
- A full-blown cafeteria with a small kitchen and lounge!
- An office space for bureaucrats and scribes!
- Decently-sized quarters for the Logistics Deck Officer and Captain!
- A massive cargo bay with pre-existing supplies!
- A secret compartment for private storage!

And finally, as for jobs, there are:
- 1 Captain
- 1 Logistics Deck Officer
- 3 Sonnensöldneren
- 2 Space Engineers
- 3 Field Engineers
- 2 Bureaucrats
- 6 Scribes
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More SolGov content is nice! Especially when it comes to ships, for a
faction that only has two existing at the moment, haha.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
add: The Solarian Port Authority Has Now Permitted Inkwell-class Vessels
To Explore The Stars!
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
## [Boopideedoo/tgstation](https://github.com/Boopideedoo/tgstation)@[9cf089361e...](https://github.com/Boopideedoo/tgstation/commit/9cf089361e8cea86d2415de0535b1a28f517e040)
#### Thursday 2023-11-09 22:20:29 by Rhials

Abandoned Domains: Adds two new psyker-oriented virtual domains (#78892)

## About The Pull Request

_Really? Bitrunning maps are so simple you could do them with your eyes
closed? Hmmmmm..._

This adds two new medium-difficulty virtual domains to the pool -- Crate
Chaos and Infected Domain.

These two domains take you to neglected corners of the virtual world.
These are unstable, bizarre locales that do not support the bitrunning
machine's visual display, and must be traversed using echolocation.
**_These domains have been designed around you being a psyker, and will
turn your bitrunner avatar into a psyker until they leave the domain._**

_**Crate Chaos:** Low cost, medium reward._

Sneak into an abandoned virtual domain, where they store all of the loot
crates. There's about 40-ish crates in this space, and one of them
(RANDOM) is the encrypted cache we're looking for. The crates must be
manually inspected, requiring you to drop your weapon for a few moments,
but that shouldn't be a problem. There's no hostiles, just a bunch of
crates... right?

This one has very few shenanigans or threats in it. It's meant to be an
introductory experience to interfacing with things as a psyker, and
getting the rhythm down for moving between visual pulses.

_**Infected Domain:** Medium cost, high reward._

Enter another abandoned virtual domain. This one was sealed off from the
digital world after the cyber-police failed to contain a virus that
zombified its inhabitants, leaving it to grow unstable and full of
holes. Fortunately, you're provided with the single best tool for arming
yourself against zombies in any video game, ever -- Your very own
Mystery Box. Get armed with (basically) whatever gun you want, and go
put those wacky psyker abilities to use against those zombies.

This one is a lot meaner. Many chasms, landmines, and zombies. Walk
slowly, stay with your fellow bitrunners, and if it's too hard, there's
no shame in going back and rolling for a better gun!

The domains themselves are VERY simple, since there's little need for
decor or particularly complex layouts. The idea is that you should be
able to see everything you need to see in a given room/area with a
single vision pulse. Here's what one of the maps looks like:


![image](https://github.com/tgstation/tgstation/assets/28870487/fe63adce-aa05-4339-9d19-28ce06a2d31f)

Err, uh, I mean... This is what the maps look like:

<details>
<summary>SPOILERS BEWARE</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/28870487/265ecdc5-50f6-4a28-8068-fab08ae1f5e8)


![image](https://github.com/tgstation/tgstation/assets/28870487/0b41da6a-e018-4434-9368-6daee1f97fe9)

(You wanna find out if there's something cool under those red lines? Go
there yourself!)

</details>

These two psyker maps come with their own psyker safehouse too -- The
Bathroom. It's gross, the medical supplies are kind of just sitting
there on the floor... It looks a little bit better when you're blind, I
guess.


![image](https://github.com/tgstation/tgstation/assets/28870487/a10b70bb-5586-4d37-bbb1-a642d8524d54)
## Why It's Good For The Game

I like psykers a lot more than I'm willing to admit. Unfortunately, the
jankiness of echolocation provides such a disadvantage at times, that
any "real" conflict is usually over before the psyker is even aware
they're taking damage.

Fortunately, the controlled environments that bitrunning maps are
perfect for psykers. They give the opportunity to craft an experience
around the player being blind, rather than forcing them to play blind
through a seeing mans world.

These two domains should present players with a unique challenge that is
designed around playing as a psyker, with slightly higher-than-usual
rewards for their trouble. More importantly -- They're fun!
## Changelog
:cl: Rhials
add: Two new psyker-oriented virtual domains -- Crate Chaos and Infected
Domain.
add: Map helper for cyber-police corpse spawn.
add: Map helper for swapping the encrypted crate in an area with a
random crate from that same area.
/:cl:

---
## [Momo8289/tgstation](https://github.com/Momo8289/tgstation)@[b77fa8c2a2...](https://github.com/Momo8289/tgstation/commit/b77fa8c2a2490b43bf9174271ebfad72c4782d98)
#### Thursday 2023-11-09 22:49:18 by LemonInTheDark

Starlight Control (Aurora works now, space gas doesn't touch starlight, narsie ending effects) (#78877)

## About The Pull Request

[Implements a setter for starlight
variables](https://github.com/tgstation/tgstation/commit/af34f06b418b039b2ead90b29112b30adea4bc68)

I want to start to modify starlight more, and that means I need a way to
hook into everything that uses it and update it, so we can modify it on
the fly.

This does that, alongside removing space overlays from nearspace (too
many false positives) and making the aurora modify all turfs projecting
starlight, rather then all turfs in an area.

Do still need to figure out handling for the starlight color usage in
turf underlays tho (I gave up, we just keep it static. I'll fix it
someday but the render_relay strategy just doesn't work with its masking
setup)

[Reworks how starlight overlays
work](https://github.com/tgstation/tgstation/commit/9da4bc38e223e0ce2d91b0c8beddf1ebba968b9c)

Instead of setting color on the overlays directly, we instead store an
object with our current settings in every mob's screen, and
render_target it down onto our overlays.

This lets us update overlay colors VERY trivially. Just need to set
color on the overlay var. Makes modifying starlight a lot cheaper.

It doesn't work on area overlays, because suffering, and it MIGHT induce
extra cost on clients. if it does we can do something about that, we'll
play it by ear

[Removes parallax starlight
coloring.](https://github.com/tgstation/tgstation/commit/5f701a1b137c7d4c333929e4cbfdd9d4aa8656d6)

I'm sorta iffy on the color, the effect can be real oppressive in some
cases, and I'd like to use starlight color for more events in world, and
having it vary can make that looking nice hard.

[Adds some visual effects to narsie being
summoned](https://github.com/tgstation/tgstation/pull/78877/commits/a423cfcb2ba9c0d729b06c36dd7d38ff68c967c2)

As the rune drawing progresses space (starlight and parallax) go from
normal to greyscale. Then, right about when narsie shows up, starlight
becomes vibrant red.

It's a nice effect. I wanna do more shit like this, I think it'll
improve vibes significantly.
## Why It's Good For The Game

Can't embed it because of github's upload limit, can show a
[link](https://cdn.discordapp.com/attachments/458452245256601615/1160821856358645860/2023-10-08_22-31-22.mp4?ex=65360e99&is=65239999&hm=680e33e4e0026b89e132afc50c04a648a24f869eb662f274a381a5de5c5a36f2&)
for the narsie stuff

Here's
[one](https://cdn.discordapp.com/attachments/326831214667235328/1160813747196141568/2023-10-08_22-34-10.mp4?ex=6536070c&is=6523920c&hm=f8d571d1013da89887f49f3fec99f632251eeeac83085aa7dde97009aee3922f&)
for the aurora too.

This gives us more pretty starlight shit, and the ABILITY to do more
pretty starlight shit. I'm pretty jazzed, and I hope people use this
proc more (keeping in mind that it's pretty hard on the lighting system,
and needs significant delay between changes)
## Changelog

🆑
add: Narsie summoning has had some effects added to space and starlight
del: Removes the link between spacegas color and starlight. It was a
slight bit too vibrant and I think impacted the vibe too wildly to be
incidental.
fix: The aurora event actually... works now. Space lights up and all
that
/🆑

---
## [crawl/crawl](https://github.com/crawl/crawl)@[9676161fe1...](https://github.com/crawl/crawl/commit/9676161fe14693c228fe4a55440a0b557540bf9e)
#### Thursday 2023-11-09 23:34:41 by yrdzrfxndfvh

change holy ziggurat floors to include more monsters (#3118)

adds sun moths, holy swine & seraphs to holy zig floors

holy swine have a decreasing chance to spawn at lower depths & seraphs
have an initially very low spawn rate which increases with depth and
zigs completed

[Committer's note: No holy swine. Plenty of non-branch Zig sets leave out
the weakest enemies in their themes, and the current slim vaults using
holy swine have at least some gesture of demonic magic, Xom, or Kirke
having done something malevolent, while a ziggurat doesn't. Sun moths
get half weight; they are technically holy, but they don't really fit
much with the other holies, they're pretty harmless for zigs, and also
their design needs shifts beyond "conjurer in the non-conjurations branch"
and "rarely tell new players ghost moths exist".

Pearl dragons no longer try to spawn more often than daevas, since their
breath went from 3d36 to 3d18. Seraphs are restricted from the first half
of ziggurat floors until one does sufficiently many ziggurats, so that
unholy players aren't any further discouraged from single-digit first zig
floors in regular 15 rune games. Thanks, c0fddb9. Still will probably
ruin a bunch of megaziggers to be surrounded by fire-immune cleansing
flame users, but I'm sure they'll adapt.

Closes #3118.]

---

