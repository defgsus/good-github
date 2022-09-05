## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-04](docs/good-messages/2022/2022-09-04.md)


1,712,011 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,712,011 were push events containing 2,366,219 commit messages that amount to 130,806,167 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 34 messages:


## [camrynpoole/nvimlua](https://github.com/camrynpoole/nvimlua)@[ae3e8bf1be...](https://github.com/camrynpoole/nvimlua/commit/ae3e8bf1be2aca3065ddbb9a65cc45c74371e544)
#### Sunday 2022-09-04 00:40:51 by Camryn Poole

refactor: fuck you

sike nah i cleaned up everything i hate shit thats there for no reason

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[e1839f0e37...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/e1839f0e375a2169c8d80d942376dddb8be1958d)
#### Sunday 2022-09-04 02:42:53 by SkyratBot

[MIRROR] Spider Rebalance PR: Burn Baby Burn Edition [MDB IGNORE] (#15997)

* Spider Rebalance PR: Burn Baby Burn Edition (#68971)

This is a remake of #66106, with more thought put into the underlying balance. The main goal of this PR is to make fighting spiders more accessible and interesting for the majority of the crew while nerfing the extremely strong and boring option of simply using freezing temps to kill spiders. Also fixes #67765. The changes are as follows:

NEW SPIDER COUNTERS

    Fly swatters now deal 25 damage to spiders on hit, increased from 1
    Pesticide now deals massive stamina damage to spiders and a little bit of physical damage as well (the damage portion not added by this PR)
    Spiders can now be caught on fire through any traditional mean of catching something on fire. Spiders will automatically put themselves out after a time. This was done instead of an active action because AI spiders are also subject to this change as well, and I don't feel like bloating the simple mob AI with putting themselves out

SPIDER CHANGES

NERFS

    Toxin injection has been removed from all spiders except for the hunter, flesh spiders and the viper
    Hunter toxin (used by hunters and flesh spiders) now only brings the afflicted down to 40 health, and will stop taking effect once the afflicted reaches that threshold. Should the afflicted still have the toxin in their system and get healed, the toxin will begin dealing damage again until the afflicted is at 40 health or below again
    Viper toxin now only brings the afflicted down to 10 health, but also has the hallucination effects of Mindbreaker toxin. This hallucination effect is applied regardless of target health. It also no longer generates other harmful chemicals into the afflicted's system, but is much more potent at base
    Flesh spiders cannot regenerate while on fire

BUFFS

    Time it takes for spiders to normalize their temperature cut by half. While they will react faster when in cold or hot environments, when they leave said environments it will take less time to return to normal temperature
    Unsuitable temperature damage reduced to 4 from 8
    You can no longer push spiders by running into them
    Webbing heat damage threshold increased from 300 to 350 (same temp where spiders also take damage)
    Broodmother egg laying time reduced to 12 seconds from 15
    Broodmother web laying time multiplier reduced to 0.5 from 1
    Broodmother health increased to 60 from 40
    Broodmother damage increased to 10 - 15 from 5 -10

BEHIND THE SCENES CHANGES

    You can now make any simple mob able to be caught on fire by setting flammable to true
    How fast a simplemob stops burning is controlled by fire_stack_removal_speed
    Can now now control how fast simplemobs regulate their temperature using temperature_normalization_speed. Before this PR, this value was hard-coded at 10, I have set the default to 5 as 10 was too long in almost any case. This will notably affect slimes, who could easily die to being cold long after being removed from the cold area. I see this as purely beneficial
    Toxins now have a health_required value. The afflicted has to be above this health value in order to take damage from the toxin. Only used in the spider toxins currently
    When I was setting up simplemobs to be flammable, I noticed basic mobs can be glitchily set on fire, so I fixed it to where they can't be set on fire.

Why It's Good For The Game

    Spacing something is very easy, but not very fun or interesting compared to starting and controlling a fire. Swapping spiders' temperature weakness from spacing to fire is beneficial to the fun of fighting them and playing as them, allowing more creativity and resourcefulness on both sides. Ideally, this should allow for atmosians and chemists to use their skills in a fun way.
    Currently, ignoring spacing them, the only people who can reasonably take on spiders is security, since they have lasers which do burn and stuns to slow the spiders down. However, this small subset of players cannot normally destroy a spider infestation without spacing them, so letting fly swatters and pesticide be used to combat spiders allows other crewmembers to fight back, letting them actually enjoy facing spiders as a threat and allowing the crew to defend themselves.
    Being killed by spider toxin after fighting off a horde isn't fun. The changes still make it a threat you have to be aware of, but not one which detracts as much from the combat loop. This also forces spiders to secure the kill themselves, which is more fun than having the toxin do it for you.
    Broodmothers in their current state are incredibly weak by themselves, which is intentional by design. However, the new changes hope to make playing as a broodmother easier and hopefully allow more broodmothers to get the spider infestation started properly. After all, Dynamic is their common source now, and they should be consistently worth the threat cost to spawn them.
    Previously, spider structures would seemingly vanish for no reason if the room was heated to be greater than 300 but less than 350, as the spiders would not be able to tell that it was too hot. Now, if the structures are taking damage, spiders will also be taking damage, so understanding what's going on should be easier now.
    Pushing spiders into a corner by running into them was not a fun tactic to deal with as a spider and didn't make much sense seeing how big the spiders are.

Changelog

cl
add: Spiders can now be caught on fire
add: Spiders take significant damage from fly swatters and stamina damage from pesticide
balance: Spiders have been re-balanced. Their toxins can no longer kill but they are not as susceptible to freezing
balance: General stats of spider broodmothers have been buffed with more health, damage, and faster web and egg placement
balance: Flesh spiders cannot regenerate whilst on fire
balance: Simplemobs change their internal temperature twice as fast
fix: Basic mobs no longer glitchily catch on fire.
/cl

* Spider Rebalance PR: Burn Baby Burn Edition

Co-authored-by: IndieanaJones <47086570+IndieanaJones@users.noreply.github.com>

---
## [SimonCalleLaverde/project-x-2022-next-js](https://github.com/SimonCalleLaverde/project-x-2022-next-js)@[8756ca7942...](https://github.com/SimonCalleLaverde/project-x-2022-next-js/commit/8756ca7942552076723d810c68bbfde71ad5b776)
#### Sunday 2022-09-04 03:53:05 by Simon Calle Laverde

YEAH, I don't like ".modules". Reasons.

- Making some classes more semantic/meaningful.
- Small edits.

-- YEAH, I don't like ".modules". Reasons:
º I would need to add/import the "mixins", "utility_classes", "fonts", "main" theme-colors, etc, into every fkn ".module" file over and over, making for a nightmare of dev experience.
º Weird to have a bunch of classes site-wide with different values and styles, but maybe the same exact names = more confusing, as hell. (Altho with extra random stuff added). Like: -Why this ".container" has this width here, but other somewhere else, or missing styles here but not there, or it is used as some other random small ".container" in any other article, card, or sht. Making for a "0" semantic codebase. (I guess even worst, many people working in one codebase, will make a HECK of a code with NO SINGLE/FUCKING sense or standards, everyone using any fkn name for anything, anywhere, just because classes don't collapse with each other).
º I rather prefer ages to have 2 organized files controlling everything in a site, super easy to re-use still, with most of its styles independent and easy to copy, like I'm doing right now (will try to improve on this still for creating independent components and for re-usability), than having dozens of random styling files per each component in a site/app, with lots of repeated and un-organized styles.
º It makes for some horrendous random additions to classes too. (I don't want the same class but with random letters that differentiate them. To inspect-element and work long-term on this sites/apps must be a nightmare). Maybe for a kid who is learning to code & style for the first time and is un-organized in nature, this will make sense.
º The worst part: We are already trading a lot and doing everything the JavaScript way with this "JavaScript Frameworks" everywhere now, and getting very away from the routes which are still HTML & CSS, but JS people will want to make it all through JS if they can.
* This still makes it sometimes harder to implement simple styles, transitions, animations, simple scss stuff, using css or scss variables, and many of the wonders and newest things in CSS, etc. Even implementing responsiveness, media-queries, etc, all harder, or less robust. This is why separated (maybe a few) "Cascade Style Sheets" to control the whole structure, where invented. This ".module" files are almost like adding inline-styles to HTML or CSS in JS directly.
* Worst worst of all: I hate having classes as JavaScript all over my JSX (i.e. "<main className={ styles.main }>" rather prefer "<main className='main'>"). Literally it makes everything more confusing to read, mixed with all the rest of JavaScript.

---
## [naikari/naikari](https://github.com/naikari/naikari)@[b17a09849e...](https://github.com/naikari/naikari/commit/b17a09849e5f1858e97e995a344f57ce891d8c3d)
#### Sunday 2022-09-04 04:20:08 by diligentcircle

Removed the standing cap system entirely.

I did some thinking about this and talked about it with my girlfriend
and I think this whole "faction standing cap" system needs to be
scrapped entirely. It's very confusing, and it hardlines the player
into getting reputation in only one particular way, which isn't a
very good gameplay experience. Actually, I think I remember us bringing
up how confusing and restrictive the rep cap system is years ago
with bobbens, but he said something along the lines of not wanting
reputation to be all about just killing ships.

Thing is, though, there's a much better way to achieve that: simply
reward more reputation for doing the story missions than for killing.
This is what MMOs seem to do.

The *only* "advantage" of the faction cap system I can think of is
that it forces the player to do the story, which is completely
antithetical to what I want this game to be. Sure, it might make
more sense for the Empire to only give you Empire ships after doing
their story, but this is quite an extreme measure, restricting the
players' freedom, for a rather insignificant benefit. I suppose this
also ties into bobbens' desire to force players to choose one or two
"major factions" to ally with and get the ships of, another design
idea I'm thinking is so controlling as to be anti-player.

All that considered, I'm taking the faction cap system out.

---
## [Technobug14/mojave-sun-14](https://github.com/Technobug14/mojave-sun-14)@[7c2f38c41e...](https://github.com/Technobug14/mojave-sun-14/commit/7c2f38c41effd2269290ea801f81570f052e140b)
#### Sunday 2022-09-04 04:36:11 by Technobug14

Shit

HATE HATE HATE this sucks and it is buggy as hell

---
## [lordnull/milang](https://github.com/lordnull/milang)@[ceeba995af...](https://github.com/lordnull/milang/commit/ceeba995af45b14c59311b3ff684bd63d75b34d4)
#### Sunday 2022-09-04 05:03:27 by Micah Warren

Massive revamp of ideoloty, syntax, and arch.

First a change in ideology. Initially milang was going to end up looking
very much like elm with some erlang mixed in and arbitrary infix
notations. However, that turned out to have a _ton_ of edge cases for
naming and how things looked. I hated having 2 ways that functions looked.
Different name binding rules. Further, it didn't really help reduce the
bike shedding that can happen.

I was playing around with scratch, and realized that the main issue with it
was a clunky interface. If an ide was able to input blocks of visual code
through text, then perhaps a visual programming language would work.

So, milang the language is a save file format(s) that is edited by
milang the ide. The tools to support compiling milang are still cli
forward, and the laguage itself is designed to be editable by humans.
However, it is not designed to be written primarily that way. It is
designed to be readable, however.

This lead to a massive change in syntax. It lead to a much more regular
system that did end up with more boilerplate and some keywords added.
However, code looks regular. The body of a function and the body
of a class implementation / class default look the same. Many features
have been (possibly on temporarily) tossed out. For example, there is no
module aliases for now, nor any auto matic aliasing of types / functions
from imported modules either. The ability is still there through the "let"
and "alias" declarations, it's just verbose. We're not worried about ease
of typing, so we're doing it. Other things have been massively moved.
Espose lists are gone. Instead a spec, type, or class declaration can have
the 'expose' or 'expose all' keyword in front of it. This allows one to
see at a glance what is exposed, and means a ui could toggle exposed or
not and have the data written more efficiently.

Finally, this meant massive changes for the parser. And that was ending up
painful. So I ended up re-writing a massive portion of that, adding a ton
of modules to represent the ast data parts. All this mainly to keep as much
comments w/ appropriate ast parts as I could.

Hopefully I've documented enough here, there, and elsewhere to allow all
this to make sense to someone other than myself, including my future self.

---
## [utilForever/RosettaStone](https://github.com/utilForever/RosettaStone)@[a4cc04fff8...](https://github.com/utilForever/RosettaStone/commit/a4cc04fff867a53ee3fb9f9c9a5607a14f92358d)
#### Sunday 2022-09-04 05:07:59 by Chris Ohk

feat(patch): Apply card update for Hearthstone Patch 24.0.3

- Celestial Alignment: Old: Set each player to 0 Mana Crystals. Set the cost of all cards in hands and decks to (1). → New:  Set your Mana Crystals to 0. Set the cost of all cards in your hand and deck to (1).
- Stag Spirit Wildseed: Old: Dormant for 3 turns. When this awakens, equip a 4/2 Greatbow. → New: Dormant for 3 turns. When this awakens, equip a 3/2 Greatbow.
- Snowfall Guardian: Old: 3 Attack, 3 Health. Battlecry: Freeze all other minions. Gain +1/+1 for each Frozen minion. → New: 5 Attack, 5 Health. Battlecry: Freeze all other minions.
- Vile Library: Old: Give a friendly minion +1/+1. Repeat for each Imp you control. → New: Give a minion +1/+1 for each Imp you control.
- Kobold Illusionist: Old: [Costs 4] → New: [Costs 5]
- Relic Vault: Old: [Costs 3] → New: [Costs 2]
- Relic of Extinction: Old: [Costs 2] → New: [Costs 1]
- Bibliomite: Old: 4 Attack, 4 Health → New: 5 Attack, 4 Health
- Magnifying Glaive: Old: 2 Attack, 2 Durability → New: 3 Attack, 2 Durability
- Abyssal Depths: Old: [Costs 4] → New: [Costs 3]
- Battleworn Vanguard: Old: 2 Attack, 1 Health → New: 2 Attack, 2 Health
- Irebound Brute: Old: [Costs 8] →  New: [Costs 7]
- Legendary Invitation (generated by The Countess): Old: [Costs 3] → New: [Costs 2]
- Stand Against Darkness: Old: [Costs 5] → New: [Costs 4]
- Warhorse Trainer: Old: Your Silver Hand Recruits Have +1 Attack. → New: Your Silver Hand Recruits have +2 Attack and Taunt.
- Promotion: Old: Give a Silver Hand Recruit +3/+3. → New: Give a Silver Hand Recruit +3/+3 and Taunt.
- Edwin, Defias Kingpin: Old: [Costs 4] 4 Attack, 4 Health → New: [Costs 3] 3 Attack, 3 Health
- Sprint: Old: [Costs 6] →  New: [Costs 5]
- Silverleaf Poison: Old: [Costs 2] → New: [Costs 1]
- Halkias: Old: Deathrattle: If you control a Secret, store Halkias' soul inside of it. It resummons Halkias when triggered. → New: Stealth. Deathrattle: Store Halkias's soul inside of a friendly Secret. It resummons Halkias when triggered.
- Sanguine Depths: Old: Deal 1 damage to a minion and give it +1 Attack. → New: Deal 1 damage to a minion and give it +2 Attack.
- Imbued Axe: Old: After your hero attacks, give your damaged minions +1/+1. Infuse (3): +2/+2 instead. → New: After your hero attacks, give your damaged minions +1/+2. Infuse (2): +2/+2 instead.
- Cruel Taskmaster: Old: 2 Attack, 2 Health →  New: 2 Attack, 3 Health
- Tidal Revenant: Old: Battlecry: Deal 5 damage. Gain 5 Armor. → New: Battlecry: Deal 5 damage. Gain 8 Armor.
- Shield Shatter: Old: Deal 4 damage to all minions. Costs (1) less for each Armor you have. → New: Deal 5 damage to all minions. Costs (1) less for each Armor you have.
- Slam: Old: [Costs 2] → New: [Costs 1]
- Bash: Old: [Costs 3] → New: [Costs 2]

---
## [WouterSpekkink/dwm](https://github.com/WouterSpekkink/dwm)@[67d76bdc68...](https://github.com/WouterSpekkink/dwm/commit/67d76bdc68102df976177de351f65329d8683064)
#### Sunday 2022-09-04 09:27:43 by Chris Down

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
## [kavirajk/linux](https://github.com/kavirajk/linux)@[4a557a5d1a...](https://github.com/kavirajk/linux/commit/4a557a5d1a6145ea586dc9b17a9b4e5190c9c017)
#### Sunday 2022-09-04 10:01:42 by Linus Torvalds

sparse: introduce conditional lock acquire function attribute

The kernel tends to try to avoid conditional locking semantics because
it makes it harder to think about and statically check locking rules,
but we do have a few fundamental locking primitives that take locks
conditionally - most obviously the 'trylock' functions.

That has always been a problem for 'sparse' checking for locking
imbalance, and we've had a special '__cond_lock()' macro that we've used
to let sparse know how the locking works:

    # define __cond_lock(x,c)        ((c) ? ({ __acquire(x); 1; }) : 0)

so that you can then use this to tell sparse that (for example) the
spinlock trylock macro ends up acquiring the lock when it succeeds, but
not when it fails:

    #define raw_spin_trylock(lock)  __cond_lock(lock, _raw_spin_trylock(lock))

and then sparse can follow along the locking rules when you have code like

        if (!spin_trylock(&dentry->d_lock))
                return LRU_SKIP;
	.. sparse sees that the lock is held here..
        spin_unlock(&dentry->d_lock);

and sparse ends up happy about the lock contexts.

However, this '__cond_lock()' use does result in very ugly header files,
and requires you to basically wrap the real function with that macro
that uses '__cond_lock'.  Which has made PeterZ NAK things that try to
fix sparse warnings over the years [1].

To solve this, there is now a very experimental patch to sparse that
basically does the exact same thing as '__cond_lock()' did, but using a
function attribute instead.  That seems to make PeterZ happy [2].

Note that this does not replace existing use of '__cond_lock()', but
only exposes the new proposed attribute and uses it for the previously
unannotated 'refcount_dec_and_lock()' family of functions.

For existing sparse installations, this will make no difference (a
negative output context was ignored), but if you have the experimental
sparse patch it will make sparse now understand code that uses those
functions, the same way '__cond_lock()' makes sparse understand the very
similar 'atomic_dec_and_lock()' uses that have the old '__cond_lock()'
annotations.

Note that in some cases this will silence existing context imbalance
warnings.  But in other cases it may end up exposing new sparse warnings
for code that sparse just didn't see the locking for at all before.

This is a trial, in other words.  I'd expect that if it ends up being
successful, and new sparse releases end up having this new attribute,
we'll migrate the old-style '__cond_lock()' users to use the new-style
'__cond_acquires' function attribute.

The actual experimental sparse patch was posted in [3].

Link: https://lore.kernel.org/all/20130930134434.GC12926@twins.programming.kicks-ass.net/ [1]
Link: https://lore.kernel.org/all/Yr60tWxN4P568x3W@worktop.programming.kicks-ass.net/ [2]
Link: https://lore.kernel.org/all/CAHk-=wjZfO9hGqJ2_hGQG3U_XzSh9_XaXze=HgPdvJbgrvASfA@mail.gmail.com/ [3]
Acked-by: Peter Zijlstra <peterz@infradead.org>
Cc: Alexander Aring <aahringo@redhat.com>
Cc: Luc Van Oostenryck <luc.vanoostenryck@gmail.com>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f956875e84...](https://github.com/treckstar/yolo-octo-hipster/commit/f956875e84140a646084a85b9cc95a853ac52b2a)
#### Sunday 2022-09-04 10:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [j-naylor/postgres](https://github.com/j-naylor/postgres)@[7fed801135...](https://github.com/j-naylor/postgres/commit/7fed801135bae14d63b11ee4a10f6083767046d8)
#### Sunday 2022-09-04 10:26:08 by Tom Lane

Clean up inconsistent use of fflush().

More than twenty years ago (79fcde48b), we hacked the postmaster
to avoid a core-dump on systems that didn't support fflush(NULL).
We've mostly, though not completely, hewed to that rule ever since.
But such systems are surely gone in the wild, so in the spirit of
cleaning out no-longer-needed portability hacks let's get rid of
multiple per-file fflush() calls in favor of using fflush(NULL).

Also, we were fairly inconsistent about whether to fflush() before
popen() and system() calls.  While we've received no bug reports
about that, it seems likely that at least some of these call sites
are at risk of odd behavior, such as error messages appearing in
an unexpected order.  Rather than expend a lot of brain cells
figuring out which places are at hazard, let's just establish a
uniform coding rule that we should fflush(NULL) before these calls.
A no-op fflush() is surely of trivial cost compared to launching
a sub-process via a shell; while if it's not a no-op then we likely
need it.

Discussion: https://postgr.es/m/2923412.1661722825@sss.pgh.pa.us

---
## [samuel-lucas6/Kryptor](https://github.com/samuel-lucas6/Kryptor)@[264da123a2...](https://github.com/samuel-lucas6/Kryptor/commit/264da123a2dd26e93d3bbb78af6ee2383d487f59)
#### Sunday 2022-09-04 10:41:30 by samuel-lucas6

src: Screw it; time to use ChaCha20-Poly1305.

I've been extremely indecisive on a couple of design decisions because I want this to be a stable format. This one is particularly tricky. People want me to use ChaCha20-Poly1305, and I want to use it too due to the performance and standardisation. However, like most AEADs, it's not committing. In other words, these AEADs are poorly designed in a way reminiscent of length extension attacks. Without adding commitment, I'm knowingly weakening the protocol, opening doors to potential attacks.

Due to the padding fix, this should currently be CMT-1 secure. It commits to the key and nonce. However, it hasn't been investigated as much as the UtC transform and adds 32 bytes to each ciphertext. Furthermore, it means you can't just use any old ChaCha20-Poly1305 implementation; you need to combine ChaCha20 and Poly1305 yourself.

The other problem is that ChaCha20-BLAKE2b is CMT-4 secure. How bad is only having CMT-1 security? It's not very clear, but it's certainly not ideal because you'd expect an AEAD to commit to all the inputs. Making it CMT-4 secure is possible by including the associated data in the key derivation, but it gets real ugly (e.g. you can't just use Argon2 anymore).

Then do I add commitment to each chunk or only the header? Again, it's not clear. Only to the header would reduce storage overhead and be enough to prevent partitioning oracle attacks but certainly seems unwise when using a separate file key for the payload.

---
## [pri0818/falcon_kernel_realme_sm7125](https://github.com/pri0818/falcon_kernel_realme_sm7125)@[d4486cb235...](https://github.com/pri0818/falcon_kernel_realme_sm7125/commit/d4486cb23539ea6f9ccdc8fcc12e3c5adeedab04)
#### Sunday 2022-09-04 11:40:24 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: pri0818 <priyanshusinghal0818@gmail.com>

---
## [Jpog2010/Jpog_Foundation-19](https://github.com/Jpog2010/Jpog_Foundation-19)@[6bf6cdb77f...](https://github.com/Jpog2010/Jpog_Foundation-19/commit/6bf6cdb77f582598b90e63fa44a922fd033ae3d0)
#### Sunday 2022-09-04 11:42:53 by harry

fixes panic bunker adjacent shitcode (#769)

* ugly as hell

* idiot

* think before i commit (never)

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[f0ceecff46...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/f0ceecff46f9b600dfe8e60199f354f61d63a0a4)
#### Sunday 2022-09-04 13:08:35 by SkyratBot

[MIRROR] Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff [MDB IGNORE] (#16000)

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff (#69158)

About The Pull Request

Title!
The CO2 thing is there because it makes my job much easier. Can probably find a way to make it move slowly if a maint insist on it. Prefer not to though.

Drafting because I want to make a second PR that have more sweeping changes (clean vars up, make a simpler formula for damage and heat production, delete underused behaviors, etc). Would honestly prefer if both this and that gets merged at the same time but I'm separating it out since it might be rejected. Or maybe ill combine it here we'll see.
Ignore that, looks like i can keep this one absolutely atomic.
Why It's Good For The Game

Had a lot of trouble when trying to document the SM gas interactions into the wiki, the interactions are all scattered and tracking down everything a gas does is extremely annoying. Hopefully this fixes that.
Changelog

cl
balance: CO2 powerloss inhibition now works immediately based on gas composition instead of slowly ramping up.
refactor: refactored how the SM fetches it's gas info and data. No changes expected except for the co2 thing.
/cl

* Refactors SM gas behavior to be datum based instead of list based + powerloss co2 buff

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[e7230e8b4a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/e7230e8b4a6d60e1b6c025b52b9f3d2fc26577a5)
#### Sunday 2022-09-04 13:08:35 by SkyratBot

[MIRROR] Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) [MDB IGNORE] (#16001)

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly) (#69376)

About The Pull Request

Just to be clear, when I refer to time here, I am not talking about cpu time. I'm talking about real time.
This doesn't significantly reduce the amount of work we do, it just removes a lot of the waiting around we need to do for db calls to finish.

Adds queuing support to sql bans, so if an ongoing ban retrieval query is active any successive ban retrieval attempts will wait for the active query to finish

This uses the number/blocking_query_timeout config option, I hope it's still valid

This system will allow us to precache ban info, in parallel (or in batches)
With this, we can avoid needing to setup all uses of is_banned_from to support parallelization or eat the cost of in-series database requests

Clients who join after initialize will now build a ban cache automatically

Those who join before init is done will be gathered by a batch query sent by a new subsystem, SSban_cache.

This means that any post initalize uses of is_banned_from are worst case by NATURE parallel (since the request is already sent, and we're just waiting for the response)

This saves a lot of headache for implementers (users) of the proc, and saves ~0.9 second from roundstart setup for each client (on /tg/station)

There's a lot of in series is_banned_from calls in there, and this nukes them. This should bring down roundstart join times significantly.

It's hard to say exactly how much, since some cases generate the ban cache at other times.
At base tho, we save about 0.9 seconds of real time per client off doing this stuff in parallel.
Why It's Good For The Game

    When I use percentages I'm speaking about cost per player

I don't like how slow roundstart feels, this kills about 66% of that. the rest is a lot of misc things. About 11% (it's actually 16%) is general mob placing which is hard to optimize. 22% is manifest generation, most of which is GetFlatIcons which REALLY do not need to be holding up the main thread of execution.

An additional 1 second is constant cost from a db query we make to tell the server we exist, which can be made async to avoid holding the proc chain.

That's it. I'm bullying someone into working on the manifest issue, so that should just leave 16% of mob placing, which is really not that bad compared to what we have now.
Changelog

cl
code: The time between the round starting and the game like, actually starting has been reduced by 66%
refactor: I've slightly changed how ban caches are generated, admins please let me know if anything goes fuckey
server: I'm using the blocking_query_timeout config. Make sure it's up to date and all.
/cl

* Resolves is_banned_from headaches and lag (Speeds up roundstart significantly)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [A-Walrus/helix](https://github.com/A-Walrus/helix)@[973c51c3e9...](https://github.com/A-Walrus/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Sunday 2022-09-04 14:41:13 by Michael Davis

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
## [SagarKadam32/HackingWithSwift-SwiftUI](https://github.com/SagarKadam32/HackingWithSwift-SwiftUI)@[62493dc92d...](https://github.com/SagarKadam32/HackingWithSwift-SwiftUI/commit/62493dc92da509b92caad4f152dec16d90d999ee)
#### Sunday 2022-09-04 15:18:56 by Sagar Kadam

Creating context menus - Change-3

Few tips for you when working with context menus, to help ensure you give your users the best experience:
If you’re going to use them, use them in lots of places – it can be frustrating to press and hold on something only to find nothing happens.
Keep your list of options as short as you can – aim for three or less.
Don’t repeat options the user can already see elsewhere in your UI.
Remember, context menus are by their nature hidden, so please think twice before hiding important actions in a context menu.

---
## [vg-mjg/majsoul-api](https://github.com/vg-mjg/majsoul-api)@[2bc039a2b0...](https://github.com/vg-mjg/majsoul-api/commit/2bc039a2b0628809334a82ff38f32f3d7661df0f)
#### Sunday 2022-09-04 15:28:07 by hierarch

Fuck ESModules

No longer torn in two I learned about my life by living through you.
This feeling inside me finally found my life I'm finally free.

---
## [loidtayag/Web-Dev](https://github.com/loidtayag/Web-Dev)@[bee680d986...](https://github.com/loidtayag/Web-Dev/commit/bee680d986745c35ed9fdf890972582f48950cf9)
#### Sunday 2022-09-04 15:56:24 by loidtayag

Made it pretty, finalised the sidebar and the header, not their overlays though. Also got the day and night theme done, note to self don't use <input> for animations, the fact I had to use type="checkbox" for it to work is weird, well probably frustrating, and it doesn't work if <button> is used.

---
## [newstools/2022-citizen-digital-kenya](https://github.com/newstools/2022-citizen-digital-kenya)@[dacb6cb8dd...](https://github.com/newstools/2022-citizen-digital-kenya/commit/dacb6cb8ddf132662142d69c703baaccbda4e966)
#### Sunday 2022-09-04 15:59:04 by Billy Einkamerer

Created Text For URL [citizen.digital/news/kenyan-woman-moved-to-the-us-with-big-dreams-and-met-a-boyfriend-on-craigslist-then-she-vanished-n305041]

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[84d15cfdf4...](https://github.com/mrakgr/The-Spiral-Language/commit/84d15cfdf4c53c690af3a0dbe6402bb6a505290d)
#### Sunday 2022-09-04 16:11:52 by Marko Grdinić

"2:05pm. Let me resume. Living like this is fine. What can you really do? In some better world, having 30 views would be 30$. Maybe I am destined never to make anything. Who knows. But either way, I should keep up the pursuit. As a writer I do not want to do anything, but write about the Singularity. As a programmer, I do not want to do anything but pursue it directly. This is both my strength and my downfall.

Maybe some people are destined to never get rewarded. But either way, I'll follow my path. If it leads me to ruin, it is the player's fault. With my meager powers, I can't take responsibility for my success and failure.

$$$

(Heaven's Key, Heavenly realm)

Slowly, out of the pocket of his trenchcoat, the revolver came out. To my eyes, the movement seemed impossibly smooth and ethereal. I had a sense of time and could see exactly the trail the gun followed and as he raised it, where it would go. As if to draw out the tension, the white haired guy lifted the gun straight up, paused it a bit and then swung it down until it was pointed straight at me. He had a grin on his face. I perfect slow motion, I could see him put his finger on the trigger.

I knew what would happen next.

The last time I was here I got shot to death. This time, my mind is whirring a lot faster, so I even though I have a second in game time until the trigger gets squeezed, I have 27h to think about my next move. If this wasn't a game running at 10,000x speed, but the real world I'd have 30 years. Before I had started the game, the controller me did a memory merge, so I understood everything that I'd missed while I was crossing the Street. Right now I have the programming and the ML skills of the controller, and the optimized mind of the instance that beat the Street game, as well as the memories of both.

I understand what the controller wants, which is to beat this white haired dude with my newly found superintelligence.

But as I am staring down the barrel of the gun, I am really wondering what I could do here.

Make my body resistant to bullets? Make them phase through my body? Regenerate the wounds?

I am racking my brain here, but I don't know how to do this. I try to do an act of will here. I picture a rock in very vivid detail and try to manifest it in front of me. My mind is working too fast for the body to react, so I do not make any movements, but nonetheless I try to focus all of my mental abilities into making something happen.

...

As expected, nothing is happening. I do not know how the white haired dude is doing it, but there must be some other trick to it than just wanting magic to work really badly. Expanding my mind and speeding it up, didn't do much to change the situation from where I was a human. I am going to get a few new holes either way.

[Gnosis check DC 1.9 Succeeded - Sampled 2.76]

Imminent death facing me, I get a sudden burst of inspiration. I realize that if I just let things as they stand, I am just going to get shot like last time. It is inevitable. So I might as well quit the game now and go to an earlier save. There is no point in letting the events unfold. That much is obvious, but...is it really? I seriously consider eating a few bullets and then realize something.

Was I really killed last time?

This situation is just too weird. Last time I took it at face value, but it is strange that the game would allow one of the players to kill another. Last time, I just aborted the game due to shock once the darkness overtook me, but had I actually gotten a notification that I died from the game itself?

I do not think that happened. Did I abort the game too quickly to get that notice? Did I simply miss it in my panic? Or is there something deeper to this?

I can't help, but to loathe myself for what I am going to do, but let's eat a few bullets to make sure of what is going on.

Bang...

I put all my willpower into not escaping to an earlier state and let the lead object pierce my chest. Damn it, it hurts! Like last time, I look at it in horror, and on cue the white haired guy empties the rest of the magazine.

Bang...bang...bang...bang...bang...

The speed at which my mind works now really drew out the horror of this moment.

I sprawl out on the table, waiting for death to come to me. Like before, I can see my blood pooling out on the table until it covered my two face down cards. And then my vision became hazy and dark. Like last time, I couldn't make out what the white haired dude was saying. It felt distant...

Like that, I slipped into unconsciousness and death.

But...since this was a game, while it can simulate many things, it can't literally simulate the absence of life. Not without killing me in the real world as well. And now that I am keeping my emotions in order, I realize that despite being dead, I can still think just fine. I can't hear anything, I can't see anything, I can't touch anything. But my mind is working.

I feel out with my senses and I realize that I still have the connection with my chip pile. I wait a while in that senseless space, and there is no change. While I can't feel anything else, my life chips are still there. And I don't get a death notification from the game itself. Meaning, the game was still on.

Experiment - success!

I save the game here and exit it.

I should have noticed this last time, but that is the weakness of the mind controlling program that I used to get rid of my fear. It is one thing to be calm, but creativity requires an active and restless mind. It is easy to notice what is there when you are calm, but hard to notice what isn't. I guess that is the difference between what you need to be a member of society and what you need to conquer it.

(Heaven's Key, Inn room)

I go back to one of the earlier save states. This point in time is exactly the time before sliped out in secret out of my room through the window and explored the city. It was the dead of night and I wasn't tired enough to sleep, so that is why I did it. It was that time I met Mickey in the park of ghosts.

I remember what that translucent old ghost told me. That we are all holograms here. And the system is what determines what exists based on our inner state.

Right now I am sitting on my bed with the lights turned off in the room. I close the courtains and flip them on. Then I manifest a body sized mirror and sit in front of it, pondering.

I need to figure out the trick to becoming translucent. Mickey did it somehow and if I could do it as well, it would give me a hint for how to deal with bullets. I'll go about it scientifically. I do not really know how to trick the system into doing it, but it is not like I can't interface with it at all.

For example...I take out one of the chips, place it on the floor in front of me and using it as a focus, manifest a bottle of water.

Rather than asking how I should change my body, why not instead start by asking how I did this obvious bit of magic?

This gives me a lot of information about the system. It is commonly believed that VR works by hijacking your senses, but if it was just that, then how would movement work? Obviously it has to capture a lot more from the brain in order to be able to do those. But why stop there?

That I could manifest this bottle as I'd imagined it, that is proof that the system understand my desires... and in the dueling realms, it rejects them. Well, Mickey told me as much, but I am thinking things through and confirming them as I go along.

Then the next step would be, rather than just my desires, my true beliefs...

I spend a few minutes thinking about it from various angles.

Honestly, I have no idea how I'd do this if I were a human. If I were a human it'd literally be like trying to develop psychic powers. I'd have to try out all sorts of drugs in order to get something going, messing myself up in the process. Maybe get into the occult mindset. It is dumb.

But as I am now, the various perspectives are all converging to one conclussion. It should actually be pretty easy.

I have access to the entirety of my mind, and thought is merely the transfer of high dimensional vectors throughout the system. A small part of that data describes whether for example I am looking at a water bottle or just imagining a water bottle. It makes sense, otherwise I wouldn't be able to tell my own imagination and reality apart. This is a very good thing, since in the real world, the perception does not affect reality, but here the system is literally basing a part of it on what it sees in my mind.

So if I mess with those thought vectors and conventiently erase the part of the data that tells me what the imagination is, I should make my first step on becoming a reality warper.

Doing this unhindered is dangerous as I'd completely lose track of what is real and isn't.

I understand where things are going with this though. If I could make it safe, I would receive a strong power. Right now even though I've increased my intelligence significantly, my emotional system is still that of a human. When I lost to the white haired guy the first time, I swore that I'd challenge him as a player, not as a character in a game.

This capability of tricking myself to think my imagination is reality should not be in my own hands, but the player's. But there is no reason why I couldn't automate the process eventually. It is like how computer programs become a part of you once you get rid of the interface obstructions, one day the player and the character might be one. Furthermore, now that I've moved from the human model of cognition to my own streamlined one, the tool I was using to regulate my emotions before has become unusable. I need to recover its capabilities by making my own.

I am still a beginner, my capability is nowhere near close enough to the person who made this game. The game is here to teach me.

Anyway, what I have to do is straightforward now that I've planned it out. The first thing I have to get out of the way is the player. The one who is currently supervising me is no good. I need him to have at least my level of capability otherwise he won't be able to keep up.

I really need the controller to help me in this because my own measure of what is sane and isn't will become distorted once I start relying on this power, and I don't mean that in the based, anti-normie way.

I need to account for any and all risks.

Having made my decision, I open up a text editor and compose a message to the controller. After that I save the game, and as a show of will, I terminate my own process.

(Helix Studio, Regent Suite, Bedroom)

I was using the emotion controlling tool to keep my focus up, so I was in fact paying attention to what was going on. Still, it is not like I can read my other self's thoughts. So far, I saw him get shot by the white haired guy, reload back a week ago, and then spend a few minutes staring at himself in the mirror. Then he terminated himself, which shocked me enough to curse. I was really perplexed as to what was going on and started thinking that something might have gone wrong in the optimization process to make him mentally unstable. My thoughts went in that direction for a few seconds and then I realized I got a message from him.

> Subject: Self-Improvement Step Request

What followed is a report by him that went into great detail regarding his thinking since he started the game. It hadn't even occured to me to think about that he deliberated whether to load back right away or get shot purposely. It went on for couple of pages and by the end I got the gist of what he wanted to develop and why he wanted to replace me with somebody more fitting.

> You won't be able to keep up, I need somebody more fitting for the role.

He literally said as much directly to me. Sigh. I didn't think my turn would come so quickly. I've been expecting him to challenge Lily's group without relying on saveloading and was looking forward to seeing how he does it, but it seems a lot of action has happened in his head that I've been unaware of.

...It is just too soon, so let me compromise. The report he wrote demonstrated his intelligence to me, so I no longer have any doubts about him broken in some way. But nonetheless, I want to see him in action before I just hand him the reigns to everything. If something goes wrong, who is going to take the responsibility of explaining that to the main me who is currently sleeping in the real world?

Maybe the role of the controller is too much, but I need to spend a while observing. So I'll do that.

I copy his paused process and do a memory merge. Then I make the necessary setup and start him in a different Helix Studio limbo. Now he should have what he needs to act as a controller. He'll be able to fork himself and start the game.

If this was a real self-improvement step, I'd erase myself here, but I am not going to do that, not yet. He is asking me to literally kill myself for him, so it is fair that I take some time to observe before deciding if I want to go forth with it. The report he sent me was pretty interesting. I'll have him do a writeup at the end of every day. At his speed of thought it shouldn't take him more than a few seconds, and it really gives me an insight into what is going on.

(Helix Studio, Skylark Island)

> Hello, welcome to the Skylark Island. Whereas most character limbos tend to be obvious, this one is heavily inspired by the Simulacrum scenario Wordly Abyss, and it is magic based. In order to acclimate the host, the tutorial messages will show up as you explore the areas. For now, keep in mind that you can access the spell list whenever you wish for it.

Before I copied myself, I wasn't aware of what I would pick, so this limbo is new to me. I remmeber seeing it in passing during past selections. The controller me picked something weird this time. I guess he didn't want to duplicate the Regent Suite.

This place was interesting, it was like a cottage made of wood. There was a table, chairs for it. It wasn't too big, certainly smaller than the Regent Suite. But whereas regular wood cottage were made of modular wood planks and boards, walls, the floors, and the ceiling and indeed the furniture seems to be made of composite wood, as if it were grown. It was how I'd imagine a fantasy druid would build it. He wouldn't use saws and nails, but magic to guide nature into the shape he desired. Looking behind me, I realize what I see is a bed.

It isn't really obvious at first glance, as it looked like some furry, green plant. It had some oversized leaves that felt like animal fur to my touch and bended flexibly as I'd moved it. The pillows were some kind of membranes and I could see liquid inside. I poke it a bit and realize that while it is flexible, it is also tough and wouldn't burst easily. It felt smooth to the touch. I tried the bed out a bit and found that it felt comfortable to rest here.

I like this place. As I walked, I noted than unlike the regular floor, this one was a slightly uneven due to being bark. My first thought that this would make it difficult to position furniture, but when I tried out the chair and sat on it, I found that it had a bit of springiness, that ensured its seat was always balanced horizontally.

The table itself, unlike the floor was made of smooth polished wood. I brushed my hand along its surface, liking how it feels.

This is a really nice feeling of adventure. It is like being a child during its first days in the world.

I take a look at the windows from my sets in the middle of the room, and realize that instead of glass, they seemed to be some kind of translucent membrane. I come up to it, touch it a bit, push it and note how flexible it is. I give it a punch. My fist sinks into it, but the membrane does not tear, instead it bounces me backwards and comes into the original straight position. I approve, it feels reliable as a window.

Looking through the window I realize that the place I am in is quite high up. My cotage in particular is high in the island, but beyond the island it feels like it is a very deep drop given how high it is. It reminds me looking over the edge of the city in Heaven's Key, though not quite that high. In the distance I can see the sea, the mountains and the forests. Sunlight gleams off it, and I get the impression of looking at another natural wonder.

In the minds of people, when people think of techology, they think of steel and concrete. Cars, robots, machines. Guns, tanks, airplanes. Skyscrappers.

But maybe that is wrong. They haven't realized it yet, but maybe the true form of techology is celestial in nature. These simulated worlds. Can breathtaking wonders that I've seen, and the powers that I am trying to attain be anything other than divine?

The brain cores that I've gotten are supposedly mostly made of carbon. Experiencing them from the inside, they don't feel technological in nature at all.

I brush away these thoughts and come to the door. It doesn't have a handle, but two wooden hook on the side. I detatch them and the door slides inward as it were a measuring tape. Like the windows, it the door was made of sturdy and flexible biological material that looked like wood, but was more like plant matter that I'd guess doesn't exist in the real world.

I poke my head outside and realize there is a huge drop below. As I imagine splattering myself below, I get a sense of vertigo and take a step backward.

> If you want to exit the building to explore the rest of the island, please use the Wings spell.

I get a helpful notification and do as instructed. As I do some large fairy wings manifest themselves on my back, and my body feels weightless. This reminds me of being a disembodied entity in the Heaven's Key title menu, and I find that it is much the same. Rather than having to beat them against the air to take flight, they are more like an antigravity device attached to my back.

I have no trouble controlling my flight and exit the room to explore the island beyond.

I spend some time playing like that and then I create a fork of myself and plug it into the game.

(Heaven's Key, Inn room)

"I am visualizing my hands at twice their usual size. How are my recordings?" I ask the controller back at the the Skylark Island.

Back in the game, I am seated in front of the big mirror. I have my hands raised in front. I think it is due to the latest batch of improvements, but my imagination is very vivid compared to before. I can almost see my enlarged hands overlaid over my regular ones as if they were real. No amount of desiring they are real will be enough to make it so. instead the controller me has to be the one to make the step. While I am focusing on visualization, right now he shuold be looking directly at my brain studying the neural messaging as it occurs.

"I've recorded it, but it is a bit hard. Instead try imagining yourself pinching your hand." I do as instructed.

"Good, now actually pinch yourself lightly." I do it just enough to be a bit painful.

"I see it. Now relax. Don't try to think of anything." I do so. What happens next is that I get a bizzare feeling of having my hand in front of me and pinching it with the other. It feels a bit dissonant, but eventually that fixes itself by me focusing on it. Just like before, I seem to be imagining pinching myself, but there is an obsessive streak to it. I am finding it difficult to focus on anything else. After a bit I get relieved.

"Good. I've aborted the program, how is your mental state?" He messages me.

"I seem to be fine." I reply. "The obsession is gone."

"Is that how it feels like? Anyway, I'll try the actual pinching next."

"Ah!" Feeling being pinched, I raise my hand to look at it. I expected to see some pain, but I am surprised to see that my skin is physically twisted. It is as if an invisble hand was pinching it. I try to relax the skin with my other hand, but it does not help. The feeling of my skin being pulled remains and after I remove it, I see the pinching fold again. "Are you seeing this?" I show it triumphantly.

"It is a success! I think I understand this. Let's try the hands again. This is like hacking memory states to cheat in games. Focus on the hands and I'll try edit the relevant thought vectors based on the previous recording. I don't want to make everything real."

I raised my hands in front of me and focus, imagining them to be oversized. As I do so something in me shifts, and to my surprise, it works. What was once imagination turns into reality. I clench and unclench them, marveling at the unfamiliar sensations. I try using them to lift the water bottle and unscrew the bottle. It feels so weird, but they aren't clumsy. I take a gulp, and screw the cap back on.

"This is pretty cool." I show of my hands in front of me. The controller can't see or feel anything my senses can't. He doesn't have direct access to them through his own mind, instead he is looking at what I am seeing through the screen. Eventually what we have planned is to integrate the rest of the senses into him, so he can feel directly what I feel through separate neural channels. If the controller had that kind of ability, it would make his work a lot easier. At the end of that road, what the controller will become is a higher order consciousness for myself, able to control me as I would a video game character.

At that point, we'll be able to do these transformations instinctively. For now...

"This is cool, but let's turn them back. I'll imagine them being normal. You do your thing." I message him.

I look at my hands and imagine them being as same as before. As I watch, I again get that strange impulse like a gear in my head has skipped a turn and the hands transform back into their previous shape. I flex them to test them out and satisfied, I let out a breath.

"Phew. We've got it!"

That white hair dude is going to get what is coming to him. Right now I could go back to that dead end, and try to resurrect myself. Except, it is one thing to imagine my hands changing shape, but quite another to imagine having a living body. I am getting to ahead of myself. We did just the very first step. The program we have is not capable of flexible whole-identity transformations. We should challenge him when we are ready.

Right now, how about we beat on some noobs?

I think back to Lily and Dale's group.

They are the ideal testing ground to develop our skills at programming the language of the mind.

Back then I just scammed them out of a ton of chips, but then they sent the tough white haired guy after me. This time I am not going to do it using saveloading, but with my own skills. Maybe if I did it that way, something different will happen.

Me and the controller burned the candle late into the night, creating some simple cheating methods and trying out what we would call the True Belief Modification. It wasn't until later that we realize that the method we invented was the legendary hallmark of the stories of the Inspired. Their titular ability was called the Inspired Desire. This was its embryonic form.

(Heaven's Key, Raven's Eye Casino)

...

$$$

2:10pm. I hear thunder. Maybe I'll have to run later, right now it is slight. It is quite sunny outside.

2:15pm. Now I have to think about some other setting. I'll go for something druidic.

2:20pm. It is really getting louder. No choice, I have to run. I'll resume later. Hopefully it won't last the whole day.

3:20pm. I am back. This time has given me time to think.

I've decided. When it is time, I'll have the 5$ tier be access to Heaven's Key, while the 10$ tier will also have access to the Spiral blog. I'll move the blog to a separate Patreon page and have it cost 5$ a month to access. This way will be fair to everyone. Once I start making Heaven's Key a business, it woulnd't be fair to subscribers if I kept putting it out for free here, so that's what I'll do. I have 100 followers right now, but this isn't useful to me unless I derive some benefit from that. Imagine if I could get 5$ a month from every one of those 100 followers. I'd literally have no trouble getting the cheaper Grayskull in that case. Instead, right now I just have some useless lurkers. If they really want to read my thoughts they can pay the cup of coffee a month if they so desire.

3:30pm. Every little bit will count for me.

Now, let me try to visualize the Skylark Island.

3:45pm. Microsoft Defender is going haywire due to the Chrome issue.

6pm. I've finished the room scene a bit ago and in a daze. What am I at so far? 4.3k.

Not bad. That is about 3k written for the day. Right now I am at 9 pages.

Tomorrow I'll publish chapter 7b and do more of the chapter 8. 3k a day is fine. In fact, I doubt I'll be able to manage 6 quality pages on average per day throughout the whole year. Managing to write 2k pages a year is quite tough, I doubt most pro writers do this much.

6:05pm. Let me stop here for the day. I haven't mentioned it, but earlier I downloaded Wrath of the Righteous. I'll get to it after Kingmaker. I think I have less than a third of the game left at this point.

This life, if only it would pay me something would not be so bad. It is a pity that my choices are so restrained by money. If I were not restrained by money, I'd be pursuing AI chips much more aggressively. But now I am reduced to a sci-fi author. Well, it will all come together if I managed to live long enough.

Today's day is over."

---
## [EdgeLordExe/Yogstation](https://github.com/EdgeLordExe/Yogstation)@[0ff6072553...](https://github.com/EdgeLordExe/Yogstation/commit/0ff60725538bf03729f749b91cbf3e887d3d4b2d)
#### Sunday 2022-09-04 16:13:52 by Edge

WE ARE SO FUCKING CLOSE TO TM PHASE GOD FUCKING DAMN

---
## [robertxgray/crawl](https://github.com/robertxgray/crawl)@[a852ce8369...](https://github.com/robertxgray/crawl/commit/a852ce8369264a3a4759b99df0bbba7645a78c97)
#### Sunday 2022-09-04 18:46:41 by Nicholas Feinberg

Play with ranged weapon stats more

Following some thinking about ranged weapons, here's a new set of
ammoless stats. Philosophy:

- Slings are high-skill 1-handers. Hunting slings are vaguely like
  war axes, and fustibaluses are no longer ultra-rare but are now
  more like broad axes.
- Bows are high-skill 2-handers.
- Crossbows are lower-skill - it takes fairly little to get the hand
  crossbow or the arbalest to mindelay. The triple crossbow is still
  high-skill, but it's quite rare, so doesn't define the 'feel' of
  the class, much as you can't rely on finding a triple sword as a
  lbl user or an exec axe as an axe user. (Unless a gifting god gets
  involved.)

If we're going to keep all these item classes, it would be great to
have some more obvious and pronounced gimmicks. I suspect we'll end
up merging or removing some of these at some point, but that's a
larger project than I'm ready for right now.

TODO: make fustibali spawn at a higher rate - right now they're about
1/5th as common as I'd like.

---
## [Royzilya/backend_test_homework](https://github.com/Royzilya/backend_test_homework)@[d862cf73c5...](https://github.com/Royzilya/backend_test_homework/commit/d862cf73c5006ea10e2d6cb18df562acda99cf8d)
#### Sunday 2022-09-04 18:52:27 by Royz Ilya

 Changes to be committed:
	modified:   program.py

git add

done
exit
finish
fuck
fuck you git hub
reboot
reset
format internet
destroy world
sucks
programming is sucks

---
## [OliOliOnsiPree/LoneStar](https://github.com/OliOliOnsiPree/LoneStar)@[e2cbff46d2...](https://github.com/OliOliOnsiPree/LoneStar/commit/e2cbff46d22c78e8e773ad20d47cdecb285ab9a6)
#### Sunday 2022-09-04 19:15:37 by Jawnner

Walking Turret - A Minigun PR (#496)

* Update minigun.dm

* Does the same for gatling laser

* better gatling sound

* Energy weapons can reload with click instead of alt click

* Beefier gatling laser sounds

* Update laser.dm

* Gatling Laser 180 shots now (fuck you pots)

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[210c4163a0...](https://github.com/ammarfaizi2/linux-fork/commit/210c4163a098540e57d96cb9a78dbf3024082c9b)
#### Sunday 2022-09-04 19:31:13 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [GerHobbelt/mupdf](https://github.com/GerHobbelt/mupdf)@[ab8edabcba...](https://github.com/GerHobbelt/mupdf/commit/ab8edabcba8e7f025f278c016663b34679e34f79)
#### Sunday 2022-09-04 19:42:00 by Ger Hobbelt

fz_storable / cmaps: it's not very smart to use -1 as a magic for a refcount that should be kept intact/alive forever as when you're hunting run-time glitches a.k.a. race conditions around fz_store, it's very risky to have a -1 mean anything useful: after all, when the refcounting itself is b0rked, it's pretty easy to drop a refcount to -1 before the shit hits the fan and your assertions finally fire, because you'll always discover a crap-up **after the fact**. (Currently we're looking for something else, but refcounting is involved and thus we stumbled across this).

-42 is pretty hard to achieve for malfunctioning software like that (and in other circumstances too as then it's one number in the entire random integer range), so we move to using -42 (42, negative) as a magic number for static cmaps that can end up in an fz_storable.

Also added debug-build-only checking code to make sure everybody does it right in the future of cmaps.

---
## [GerHobbelt/mupdf](https://github.com/GerHobbelt/mupdf)@[7f403843b2...](https://github.com/GerHobbelt/mupdf/commit/7f403843b2d0b9fb456bab8fff21a28bf662ff24)
#### Sunday 2022-09-04 19:42:00 by Ger Hobbelt

WIP: attempt to make XMP parsing more lenient to errors in the content. This generalizes to pdfinfo & pdfmetadump tools potentially benefitting from this as well, improving their ability to dump info from (partly) damaged/invalid PDFs.

However, note this thought from the bulktest logbook notes yesterday evening:

------

## THOUGHT:

After working an evening on some Metadata (XML) recovery code in `mupdf` core, I believe this is the WRONG TACTIC for this problem:

1) it takes a long time to get stuff done as the test/debug round trip is relatively slow, due to having to run the PDFs through the correct commands to trigger recovery, etc.
2) we limit ourselves to recovery code in C, using the xml parser (which fails) and the now-used gumbo html parser as a second attempt -- which turns out to be worthless as it expects HTML and nothing else, so it is pretty useless parsing semi-b0rked or fully-b0rked XMP records (XML).

Now we could persist and find ourselves the most lenient XML parser in the world and some very smart recovery codes, but here's a thought:

> Isn't this much more suitable to SCRIPTED processing? Where userland scripts can be created and used to fiddle to your heart's content?

**YES!**

Question is then: do we do this through an external process invoked through a callback, or via QuickJS and specifying user script to run or ...?

All those sound really nice, until you look at reality: https://jsonformatter.org/xml-formatter had no problem cleaning it up for us and that might not be batchable, but is surely very useful to any user anyway.

Which leads us to a meta-question: what can we do best to have the same tools suitable for batch and incident edits, including manual user operations like this copy&pasting to an external website?

--> while I was initially thinking in the direction of callbacks, i.e. staying in the current exec/run, now I believe the better and faster way forward is this:

allow the repair/recovery process to take arbitrary time and be executed at arbitrary times, hence:

- have the ability to at least detect these errors/issues in a batch or single run.
- use that signal (or do this as part of that signaling): ability to dump the raw data with sufficient markers so we can process it any way we want ...
- ... and then have a second tool (or batch run) import/replace those buggered bits with the corrected data provided by the external process (which might be anything, including manual actions such as copy/paste to/from websites, editors, ...)

Hence we must have tools with the ability to EXPORT these erroneous chunks ...
... and have the ability to IMPORT replacement data from files, preferably produced during previous EXPORT so users / external processes only need to bother with replacing the bad stuff for some good stuff.

^^^^^^ That means we can keep our tools relatively simple and don't need elaborate recovery schemes in the core tools themselves as everything is reduced to EXPORT + IMPORT/REPLACE (when available).

> Then the whole correction process becomes external activity that can be dealt with any way we like!

---
## [npv12/strix_kernel_oneplus_sm8150](https://github.com/npv12/strix_kernel_oneplus_sm8150)@[bc3d557105...](https://github.com/npv12/strix_kernel_oneplus_sm8150/commit/bc3d5571059f92fa45f4815dce6f9bade506a10b)
#### Sunday 2022-09-04 20:17:11 by Zlatan Radovanovic

Revert "msm: camera: icp: Enable hang dump on failure"

Fuck you CAF.

This reverts commit eece594678f618c964051092fa0dd470b26039b3.

Signed-off-by: Pranav <npv12@iitbbs.ac.in>

---
## [IHorvalds/ReFerbIsh](https://github.com/IHorvalds/ReFerbIsh)@[fadea66997...](https://github.com/IHorvalds/ReFerbIsh/commit/fadea6699748bede4d14036277efe770a626a9ac)
#### Sunday 2022-09-04 21:21:24 by Imod Horvalds

Add multi-channel diffuser instead of bypass at each step of the reverb loop.

- each step has 2 allpass filters in series -> mc-diff/delay line/bypass
- reverb has 4 steps
- before feeding back into the reverb, we're applying a low cut and a low pass for freq-dependent decay
- with the mc-diffuser and krt around .97-.99, you get a massive droning delayed creepy-ass noise. Very cool and the decay is also interesting. Maybe offer option to sync reverb time to project tempo.
TODO:
- smoothed parameters
- add option between mc-diff/delay line/bypass
- add host sync for reverb time to project tempo
- GUI....pls
- try mixing output channels with a lossless matrix (try others)

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[24aca0ae55...](https://github.com/silicons/Citadel-Station-13-RP/commit/24aca0ae55ce2204474ec23fed6d23cb46b6645e)
#### Sunday 2022-09-04 21:29:54 by LordPapalus

Cargonia, but with less weapons (#4370)

* Cargonia is no more

Fuck you

* PLEASE

* Zandario, I will suck your PP

---
## [ThursdayWitness/MonstriDefense](https://github.com/ThursdayWitness/MonstriDefense)@[068ccb8b6d...](https://github.com/ThursdayWitness/MonstriDefense/commit/068ccb8b6de6c2c69ae94bd0e835b68f4847d238)
#### Sunday 2022-09-04 23:15:22 by Konako

Oh my god I waste 3 hours on this fucking shit I hate it
- Add test to damage_type
- All works fine now
- I gonna sleep 6 hours and die on lessons

---
## [ThakaSartu/muna](https://github.com/ThakaSartu/muna)@[06aa54bff4...](https://github.com/ThakaSartu/muna/commit/06aa54bff4ebdfce999cdf38b11ac227a38d81a0)
#### Sunday 2022-09-04 23:41:34 by ThakaSartu

 {% highlight ruby %}
1 # HOLE_TO_ANOTHER_UNiVERSE##############################
2 # TO####################MUWAH########################
3 # ANOTHER###############################################
4 # UNiVERSE############ሙና####################Muna#####
{% endhighlight %}

## Hole To Another Universe
One day my blog will `RETURN true` when run from the [command](https://youtu.be/EDuvO_Qpk2s) line!

[What makes speakers happy](https://lea.verou.me/category/thoughts/)
[Even More CSS Secrets - Lea Verou](https://www.youtube.com/watch?v=8BXQ3zCihYM)
[CSS Variable Secrets | Lea Verou | CSS Day 2022](https://www.youtube.com/watch?v=ZuZizqDF4q8)
##  مونا
[(Rare) 🏆Tony Touch - Hip Hop #48 (1995) NYC Brooklyn sides A&B](https://www.youtube.com/watch?v=_AvRfO7CFcM)
[Inside Louvre Museum Paris, Mona Lisa - (Part 1) 🇫🇷 France - 4K Walking Tour](https://www.youtube.com/watch?v=6vuFh6NNa70)
<IMG src="https://thephotoacademy.com/storage/magazine/444/THE-PHOTO-ACADEMY-courses-nature-7.jpg">
<IMG src="https://i.pinimg.com/originals/82/38/43/82384346f772edf917ad61370552b14e.gif">

[The%20Goddess%20of%20Spring%20-%20Silly%20Symphony](https://www.youtube.com/watch?v=pBo8NOarYMo)

<IMG src="https://i.pinimg.com/736x/cd/50/a0/cd50a0503ac8c96e7de28371d258e99f--disney-posters-classic.jpg">

[Silly Symphonies - The Skeleton Dance](https://www.youtube.com/watch?v=vOGhAV-84iI)
<IMG src="https://m.media-amazon.com/images/M/MV5BOWRmNDI2MWEtNzIwNi00ZTFjLThlNjYtZjEwOTdhZTI3NDM5XkEyXkFqcGdeQXVyNjYyODY4NDU@._V1_FMjpg_UX1000_.jpg">

[Popeye The Sailor Man - Meets Alibaba's Forty Thieves](https://www.youtube.com/watch?v=W0uqdyMns9M)

<IMG src="https://dygtyjqp7pi0m.cloudfront.net/i/28385/24833978_1.jpg?v=8D397A887547150">

[Silly Symphony - The Three Little Pigs](https://www.youtube.com/watch?v=FsZ61cCieaM)

[Basic concepts of flexbox - DEVELOPER.MOZiLLA.](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)
[ROAM presents: Jayda G on Fauve Radio](youtube.com/watch?v=63wzhFt3Bas)
[Jayda G Boiler Room London Studio DJ Set](https://www.youtube.com/watch?v=EPjoLWoW_Lw)




<IMG src="https://pyxis.nymag.com/v1/imgs/e64/fc3/75f3082d8daefc6f9a51c2b21e35efb31d-1----.2x.w710.jpg">
<IMG src="https://pyxis.nymag.com/v1/imgs/965/7de/754b2a193291dc70ec34e73dafcc8a3e1c-funny-anniversary-card-valentines-day-ca.2x.h473.w710.jpg">
<IMG src="https://www.livetalentnow.com/wp-content/uploads/gravity_forms/1-ef723e2dced7176b663016787e182fa3/2018/11/23F153EF-EFAE-4DFE-8BF2-0A20BA9530D1.jpeg">
<IMG src="https://64.media.tumblr.com/278a1d44cb2532ba54c03fe01a2310b1/tumblr_pko5s5RsBj1qzoxf3o1_1280.jpg">
## Hole to another universe 

 {% highlight python %}
1 # HOLE_TO_ANOTHER_UNiVERSE##############################
2 # TO####################################################
3 # ANOTHER###############################################
4 # UNiVERSE###########################SELASSiE_POSSE#####
{% endhighlight %}

---

