## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-18](docs/good-messages/2023/2023-11-18.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,237,335 were push events containing 3,007,576 commit messages that amount to 169,574,206 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 88 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[30dae8899b...](https://github.com/tgstation/tgstation/commit/30dae8899bad0007ae9220f1fc10be16908dd1a9)
#### Saturday 2023-11-18 00:09:03 by Kyle Spier-Swenson

fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#79783)

This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

---
## [dieamond13/tgstation-dieamond](https://github.com/dieamond13/tgstation-dieamond)@[1a9043d797...](https://github.com/dieamond13/tgstation-dieamond/commit/1a9043d797325fe09cdb4e42d42f5d922c151ed9)
#### Saturday 2023-11-18 00:09:55 by necromanceranne

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
## [dieamond13/tgstation-dieamond](https://github.com/dieamond13/tgstation-dieamond)@[91af16bcbf...](https://github.com/dieamond13/tgstation-dieamond/commit/91af16bcbfd2dd363a89d846ae2acd6d655083c2)
#### Saturday 2023-11-18 00:09:55 by zxaber

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
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[3ce50d7766...](https://github.com/effigy-se/effigy-se/commit/3ce50d776649294a7950630ff9984dab42442768)
#### Saturday 2023-11-18 00:14:39 by san7890

Codifies male goats not having an udder (#79722)

## About The Pull Request

This was addressed in #78759 (1b1fde4908826ef5c54ffc0734e74028270af3fd)
and reviewed (and merged even though I didn't respond to it, oh well),
but I half-assed it because the whole point was to prevent male goats
from having an udder, but I only added it to the subtype of Pete i made
in that PR. Let's expand that to all male goats now.
## Why It's Good For The Game

It doesn't make biological nor morphological sense as to why a male goat
can provide milk. Ideally this should be like this for all animals
(because that's real life) but that's a later issue with further balance
implication.

I think it's still an interesting idea that Nanotrasen will just send
you any old goat despite it being "useless" beyond being very good at
eating plants. Maybe cargo should have a way to guarantee getting a
female goat in the future? It's just like real life where zoos and farms
have to constantly dealw ith female animals (such as giraffes or other
exotic stuff) tending to be far rarer/cost far more than their male
variants due to the potential to generate offspring (there's more nuance
to husbandry than this but just play along)... and in space, every
animal is "exotic".

It still remains possible to biogenerate milk, which tends to be far
faster than feeding/milking goats- which is something that the cook
should have access to anyways.
## Changelog
:cl:
balance: Male Goats should no longer spawn with an udder, instead of it
just being Pete.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [distributivgesetz/effigy-se](https://github.com/distributivgesetz/effigy-se)@[57569bfcbd...](https://github.com/distributivgesetz/effigy-se/commit/57569bfcbde0af7b25eac58df98abfcb72f956f4)
#### Saturday 2023-11-18 00:17:33 by carlarctg

Adds a Syndicate Monkey Agent beacon uplink item (#79012)

## About The Pull Request

Adds a Syndicate Monkey Agent beacon uplink item. It spawns a dapper
monkey that must follow your orders.

Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

Added a more modularlike subtype for antagonist spawners to reduce
future hardcoding.

Gave the syndicate turtleneck a monkey sprite, from SS14!

## Why It's Good For The Game

I want to see the clown driving security insane with 2-3 monkeys and an
incredible amount of pranking. Or an assistant killing everyone with his
monkey friends while wearing a monkey suit. Or a geneticist sending out
mutated monkeys to kill people. Or a scientist equipping his monkeys
with bombs or xenobiology equipment and sending them out to wreak havoc.

6 TC is only enough for two monkeys, but you can get a third if you
finish any kind of objective.

> Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.

We can't have the monkey mafia without guns, come on. The guns are weak
and only usable by monkeys. Additionally, they're restricted to
entertainment only.

Credit to SS14 for the monky turtleneck sprite.

## Changelog

:cl:
add: Adds a Syndicate Monkey Agent beacon uplink item. It spawns a
dapper monkey that must follow your orders.
add: Added a monkey gun case to the uplink, which contains monkey guns!
Though they aren't very powerful.
refactor: Added a more modularlike subtype for antagonist spawners to
reduce future hardcoding.
sprite: Gave the syndicate turtleneck a monkey sprite, from SS14!
/:cl:

---------

Co-authored-by: ATH1909 <42606352+ATH1909@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [OliOliOnsiPree/tgstation](https://github.com/OliOliOnsiPree/tgstation)@[2532911353...](https://github.com/OliOliOnsiPree/tgstation/commit/2532911353d63661b735004f2895103d45858b50)
#### Saturday 2023-11-18 00:26:30 by LemonInTheDark

Adds pathmaps, refactors pathfinding a bit (#78684)

## About The Pull Request

Implements /datum/pathfind/sssp, which generates /datum/path_map

/datum/path_maps allow us to very efficently generate paths to any turf
they contain from their central point.

We're effectively running the single source shortest paths algorithm.
We expand from the center turf, adding turfs as they're found, and then
processing them in order of addition.
As we go, we remember what turf "found" us first. Reversing this chain
gives us the shortest possible path from the center turf to any turf in
its range (or the inverse).

This isn't all that useful on its own, outside of a few niche cases
(Like if we wanted to get the farthest reachable turf from the center)
but if we could reuse the map more then once, we'd be able to swarm
to/from a point very easily.

Reuse is a bit troublesome, reqiures a timeout system and a way to
compare different movables trying to get paths.
I've implemented it tho. I've refactored CanAStarPass to take a datum,
/datum/can_pass_info. This is built from a movable and a list of access,
and copies all the properties that would impact pathfinding over onto
itself.

There is one case where we don't do this, pathing over openspace
requires checking if we'd fall through the openspace, and the proc for
that takes an atom.
So instead we use the weakref to the owner that we hold onto, and hold
copies of all the values that would impact the check on the datum.

When someone requests a swarmed path their pass info is compared with
the pass info of all other path_maps centered on their target turf. If
it matches and their requested timeout isn't too short, we just reuse
the map.

Timeout is a tricky thing because the longer a map exists the more out
of date it gets.
I've added a few age defines that let you modulate your level of risk
here. We default to only allowing maps that are currently
being generated, or finished generating in our tick. 
Hopefully this prevents falling into trouble, but consumers will need to
allow "failed" movements.

As a part of this datumized pass info, I've refactored pathfinding to
use access lists, rather then id cards directly. This also avoids some
dumbass harddel oppertunities, and prevents an idcard from changing mid
path.

Did a few things to the zPass procs, they took args that they did NOT
need, and I thought it'd be better to yeet em.

If you'd all like I could undo the caching/can_pass_info stuff if you'd
all like. I think it's useful generally because it avoids stuff changing
mid pathfind attempt, but if it's too clunky I could nuke it.

Oh also I added optional args to jps that constricts how it handles
diagonals. I've used this to fix bot paths.

## Why It's Good For The Game

Much of this is redundant currently. I'm adding it because it could have
saved hugglebippers, and because I get the feeling it'll be useful for
"grouping" mobs like bees and such.
We're doing more basic mob work currently and I want to provide extra
tools for that work.


https://github.com/tgstation/tgstation/assets/58055496/66aca1f9-c6e7-4173-9c38-c40516d6d853

## Changelog
🆑
add: Adds swarmed pathfinding, trading accuracy for potential
optimization of used correctly
fix: Bots will no longer take diagonal paths, preventing weirdo looking
path visuals
refactor: Refactored bits of pathfinding code, hopefully easier to add
new pathfinding strategies now
/🆑

---
## [yui019/azu](https://github.com/yui019/azu)@[e86d8b00fd...](https://github.com/yui019/azu/commit/e86d8b00fdf7af77254e92e9313b5adb354f6424)
#### Saturday 2023-11-18 00:28:38 by yui019

Fix segfault when destroying VmaAllocator

I swear to fucking god, this is the most annoying shit possible. I'm
still under the impression that manually swapping all class members in
the move assignment operator is not how you're supposed to do it, but
I can't find anything else online.

---
## [Y0SH1M4S73R/tgstation](https://github.com/Y0SH1M4S73R/tgstation)@[0be45dcd65...](https://github.com/Y0SH1M4S73R/tgstation/commit/0be45dcd6534244532e652564976bab13a3d8bdb)
#### Saturday 2023-11-18 00:31:31 by John Willard

Human sounds now depend on body type (#78632)

## About The Pull Request

So there's currently a problem where our human sounds are dependent on
whether you are a male or female, however we have 4 genders in-game.
This leads to scream sounds being female if you're anything but a Male,
and gasp shock sounds being male if you're anything but a Female. This
is very inconsistent, and I think as a better way of handling this, it
should all be handled by Bodytype, since we only have 2 and is a
separate choice from gender. This means regardless of gender, you can
still choose what sounds your character will make.

## Why It's Good For The Game

Mostly explained in the about section, this lets people who play as
they/them & it/its to decide what they should sound like.
I guess as a bonus, it means men now appear more like women if they
choose the female bodytype, and vice versa. Or at least I think it's a
bonus? I'm not really knowledgeable in this sort of stuff.

I kinda have the same argument as why I think TTS should be accurate.
You should be able to customize your character to how you want it, and I
think that choosing the non-male/female ones shouldn't give you
inconsistent voices.

## Changelog

I actually don't know what to label this.

:cl:
code: Your bodytype now decides what gendered sounds you make.
/:cl:

---
## [morrowwolf/tgstation](https://github.com/morrowwolf/tgstation)@[0f5d14e68b...](https://github.com/morrowwolf/tgstation/commit/0f5d14e68b19111592301efe52a03de80aced61e)
#### Saturday 2023-11-18 00:31:54 by Ben10Omintrix

Mook village and basic mook refactor (#78789)

## About The Pull Request
refactors mooks into basic mooks and re-adds them to the game

## Why It's Good For The Game
this refactors mooks into basic mobs and re adds them to the game. mooks
are now a part of lavaland. they come as a part of a random ruin which
consist of a entire village of friendly mooks. Mooks will aid players
but they will still attack ashwalkers because of some troubled history
between them.

![mookvillage](https://github.com/tgstation/tgstation/assets/138636438/ad1c5d63-c168-475a-a85d-b727dff43e7b)

mooks are a very diseased specie. nanotrasen discovered a small tribe of
mooks and cut a deal with their tribal chief to aid ss13 miners in
exchange for medical supplies.

tribal chief in his decked out home

![tribalchief](https://github.com/tgstation/tgstation/assets/138636438/cc0e0a11-9bf0-4322-b3ae-c7be43092ee8)

male mooks go out and mine and haul ore off back to their village. they
will deposit ores into a stand which is managed by another mook. they
will all return to their village to rest once a lavastorm comes.

![mookstand](https://github.com/tgstation/tgstation/assets/138636438/c7adbf4e-6322-4347-acfc-4e8d45aff798)

players can use this stand to withdraw any ore they like

![mookui](https://github.com/tgstation/tgstation/assets/138636438/a1318be8-50f7-49b2-827c-97bafdb2488a)

female mooks will stay behind in the village to guard it from
ashwalkers. they will also heal male mooks when they come back from a
long day of work. the tribal chief is a bum and chooses not to go out
and mine. he will stay behind in the village and issue commands to his
people rather than work

the village also has its own bard! he follows player visitors and plays
nice music for them while they are in the village (although he is not
very talented).

![mookbard](https://github.com/tgstation/tgstation/assets/138636438/5123e492-6657-4755-9dc7-ab94d4beb554)

he is still a warrior at heart tho so he will be smashing his guitar
over ashwalker skull

![mookshmash](https://github.com/tgstation/tgstation/assets/138636438/bf211bf0-e963-4dbb-b004-e653e06e3974)




## Changelog
:cl:
refactor: mooks are now basic mobs. please report any bugs
feature: added mook village to lavaland ruins!
/:cl:

---
## [morrowwolf/tgstation](https://github.com/morrowwolf/tgstation)@[3e554bdab3...](https://github.com/morrowwolf/tgstation/commit/3e554bdab3ae7ffff4bd9090b71dc0b3666f081f)
#### Saturday 2023-11-18 00:31:54 by Jacquerel

Flesh Spiders Regenerate + QoL (#78704)

## About The Pull Request

Replaces the Healing Touch component on Changeling-spawned Flesh Spiders
with the Regenerator component, as the comment helpfully suggests.
Flesh Spiders can no longer touch themselves to heal, instead they
automatically begin regenerating their health if they go four seconds
without taking damage. It takes 6 seconds to fully regenerate, so 10
seconds to fully heal from the edge of death (less if you're not that
injured).


![image](https://github.com/tgstation/tgstation/assets/7483112/37faca55-35fe-48dc-a3ed-03f4b79860bd)

Also I changed the sprite for flesh spider eggs to a different one we
already had rather than regular spider eggs tinted red, just because I
felt like it.
Would be cool to give the spiders their own sprite some time, but that's
for another PR.


![image](https://github.com/tgstation/tgstation/assets/7483112/8ec286c4-46dc-4aec-aa98-cb4e4e432690)
_Additionally_ the flavour text for flesh spiders was kind of messed up
by being shoved into the objectives box and claiming that it was a
directive from a spider queen you don't have, so I gave them their own
slightly different antag datum to compensate.
It also actually mentions how you heal yourself, which previously was
down to trial and error or codediving.

In the course of doing this I decided to just... move flesh spiders to
their own type path. It _sort of_ made sense for them to be part of the
giant spider typepath, but they keep being modified by changes targetted
at "balancing the Giant Spiders antagonist" which this mob isn't related
to and doesn't have any reason to follow. The fact that a mob has
similar stats to another one isn't automatically a reason to share a
typepath, and now that I have looked a little at this mob I'm sort of
interested in branching it further away from "it's a spider mob but
spawned a different way" in the future.

Finally, this spider egg cluster and the midwife one would prompt ghosts
with a radial menu with a single option on it... that's a bit pointless,
so we'll bypass that menu if there is only one possible outcome.

## Why It's Good For The Game

Currently Flesh Spiders heal by clicking on themselves and standing
still for two seconds, restoring 50% of their HP. This means they can
fully regenerate over 4 seconds unless you stun them, and with 90 HP
you're not _that_ likely to kill one during the channel time.
This just feels like an odd way for the creature to operate,
regenerating instead gives it a hit-and-run strategy and adds more use
to their webs (maybe we should give them meatier or bloody webs at some
point? Might be cool).
Also clicking yourself to heal is just unintuitive and I suspect several
players just didn't realise they could do it in the first place.

## Changelog

:cl:
balance: Flesh Spiders heal automatically over time if they go a short
time without taking damage, instead of healing large chunks by clicking
themselves and waiting two seconds.
qol: Spider egg clusters which only hatch into one kind of spider don't
ask you to select that one type from a radial menu with one option on
it.
qol: As a Flesh Spider, the game now tells you how you can heal
yourself.
/:cl:

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[9e18c6575a...](https://github.com/necromanceranne/tgstation/commit/9e18c6575a3cb9e73c3e699d4fe51b904b76e2f6)
#### Saturday 2023-11-18 00:32:43 by lizardqueenlexi

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
## [ihatethisengine/cmss13](https://github.com/ihatethisengine/cmss13)@[1e890af39d...](https://github.com/ihatethisengine/cmss13/commit/1e890af39d7c4b6233439fbaa8693a3918e35f5c)
#### Saturday 2023-11-18 00:34:28 by Steelpoint

Revolver Heavy Ammo Effect Change (#4706)

# About the pull request

This PR changes heavy ammo for the Revolver to knockback a mob and slow
them down instead of stunning it.

# Explain why it's good for the game

Combat balance is a precarious and often difficult conversation to hold,
ergo I'll lay my biases out on the table at first. I'm a marine main at
heart, but I have played a lot of xeno recently to gain a better
understanding of their side of the story, enough that I feel confident
to make these assertions.

My belief is that the heavy ammo of the revolver is a negative concept
for the game, and it needs to be removed, due to its stun factor.

The issue here is readability and prediction. When you see a RPG, you
know that it can fire a devastating warhead that can stun and kill T3s.
When you see a Warrior, you know it can leap to 4 tiles to stun and drag
a Human, when you hear a CAS strike you know exactly what is about to
drop. When you see a Queen you know she can stun screech and neuro stun
you.

But the issue with the Revolver is it has no obvious tell. It is a small
item, that can be fit inside backpacks, holsters, pouches, belts, armour
slots. It has no obvious advance warning when you are going to fire it.
There is no special uniform requirement making a revolver user standout
amongst the crowd. There is no tell.

The problem with the stun revolver is simply that is is a hard counter
to all T1s and most T2s. Its ability to stun allows it to perform an
attack that is uncounterable to a xeno as a xeno has no way to predict
who may be carrying one. A xeno can tell who a Specialist is, a xeno can
tell who has a shotgun or flamer or sniper or RPG, you can tell when a
mortar is being prepared, or a CAS strike or even an OB. You can see the
smartgunner. Even the Scout, a literal cloaked Marine, has to uncloak to
fire. You can not tell who has a revolver until they pull it out and
stun you. Once you are stunned you die.

A xeno equilivant would be if any Xeno could be carrying a special tool
that lets them grab a marine from 7 tiles away and pull them in plus
stun them for 2 seconds. But any xenomorph could be using it, including
a Lesser Drone.

Perhaps the heavy revolver could be reworked to do something else, but
ultimately the only reason anyone takes this ammo is for the stun.
Anything else is beating around the bush.

Those are my reasoning's, I'll leave the rest to the powers' that be. 

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Revolver Heavy ammo no longer stuns targets it strikes, it will
instead knock them back and slow them down for a short time.
/:cl:

---------

Co-authored-by: Steelpoint <alexander.henley@hotmai.com>

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[9ff9e4b9a8...](https://github.com/Thunder12345/tgstation/commit/9ff9e4b9a849e4a50bf500aaaeca5e020e7677d6)
#### Saturday 2023-11-18 00:35:33 by necromanceranne

Scatter laser shells now use the scatter laser beam, and makes them significantly easier to make. Projectiles can now have damage falloff. (#78927)

## About The Pull Request

Allows for damage falloff to apply to more than just shotgun pellets.
Now any projectile can have a damage falloff defined.

Scatter Laser shells no longer use the minigun beams to determine their
damage. Instead they use the actually defined scatter laser beams. Those
beams do 7.5 damage per pellet, times by 6 pellets.

Scatter laser beams now have damage falloff, a separately defined
(positive) wounding power from normal beams, and wound falloff.

Scatter laser shells can be printed from security protolathes once you
have weapon tech.

Scatter laser shells _may_ be damaged by EMPs based on severity. The
result is that it fires a practically useless volley of laser fire. They
cause a honk sound when they hit, so you know when you've shot one of
these.

## Why It's Good For The Game

Well, we want shotguns universally to not be defined by their damage
output (especially extreme damage output) but by niche.

What does the scatter laser shell currently occupy as a niche?

The single highest damage output of any projectile weapon in direct
damage. The thing we don't want of shotguns, and it is reigning champion
of all guns.

Okay, that's a bit misleading, because obviously it is competing with
the likes of .50 BMG which does 70 damage outright and dismembers limbs,
potentially doing upwards of 90 damage if it does, and also hard stuns
people. Obviously _that_ is technically a stronger bullet.

But not for raw damage, because the scatter laser does 90 damage out the
gate, barring any potential wounding that might occur which increases
the damage multiplicatively. No gimmicks, no extra procs, nothing. It's
just 15 force lasers (with no damage dropoff) split between 6 beams.

And the reason for this is because this shell has been nerfed once prior
by making it not fire 6 normal laser shots into someone. That was 120
damage at the time, 120 to 90 was...I guess a nerf during the taser era.
Depends on how you viewed it. Buckshot was doing like 80 at the time,
believe me it was a wild period. But anyway, when we did the whole
damage rearrangement over the course of the laser few years, every other
shell got touched except this one for some reason. Even pulse slugs lost
10 damage while this was still sitting on 90 force point blank.

So what is the new niche? Well, it's laser buckshot. That's not a niche
but crew don't get buckshot, so this is their buckshot. It wounds real
good. Real goddamn good. And its is a laser. It fits the aesthetic,
obviously.

Okay, thanks.

## Changelog
:cl:
balance: Scatter laser shells actually utilize the _real_ scatter laser
beam. This comes with damage changes. And wounding power.
feature: EMPs can potentially damage scatter laser shells.
refactor: All projectiles can now have damage falloff defined. Yay.
balance: Scatter laser shells can be printed when weapons technology is
researched.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[071f6063e6...](https://github.com/Thunder12345/tgstation/commit/071f6063e69d39e1403eca917a395191339f353a)
#### Saturday 2023-11-18 00:35:33 by carlarctg

Adds charges to omens and omen smiting. Reduces omen bad luck if nobody's nearby. (#78899)

## About The Pull Request

refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.

qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)

fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.

## Why It's Good For The Game

> refactor: Adds charges to omens and omen smiting rather than only
being permanent or one-use. Mirrors now grant seven bad luckers.

Allows for someone to get between 1-infinity omen accidents. Seriously
why wasnt this a thing before

> qol: Reduces omen bad luck if nobody's nearby.

I LOVE this quirk, but trying to do antything at all except 'Suffer
Miserably' is nigh impossible. To alleviate life a little, making it so
that you have a lesser chance of suffering misfortune if nobody's around
will be the perfect compromise. It makes life easier but doesn't
compromise funny moments.

Any client in viewrange will disable the reduction. This includes
ghosts.

## Changelog

:cl:
refactor: Adds charges to omens and omen smiting rather than only being
permanent or one-use. Mirrors now grant seven bad luckers.
qol: Reduces omen bad luck if nobody's nearby to witness the funny.
(Ghosts are included in the check!)
fix: Fixed an issue where a monkey check in doorcrushing was never
actually able to pass. Also they screech now.
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[0d5f9907a2...](https://github.com/Thunder12345/tgstation/commit/0d5f9907a24346554f4da78199138f4cdcca8de5)
#### Saturday 2023-11-18 00:35:33 by Jacquerel

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
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[053e66b0d3...](https://github.com/itseasytosee/tgstation/commit/053e66b0d36700f6e55a15290cf2f853a1a6d58e)
#### Saturday 2023-11-18 00:38:41 by necromanceranne

Makes the Regal Condor realistically simulate being shot dead with a high caliber hand cannon by making it HITSCAN (#78674)

## About The Pull Request

The Regal Condor come with a magazine and ammo already inside.

The recipe for the magazine now no longer needs TC, but does need donk
pockets (sponsored murder gear, you see) and a hell of a lot more
materials per magazine (you're looking at like 40 sheets of various
materials all up). It also needs you to make the Condor first. But it
comes preloaded with ammo.

The Condor is 1 whole TC more expensive. Also needs some metal. The old
recipe is there in spirit.

The Regal Condor and the magazines come with 10mm Reaper bullets.
They're high damage. They're high AP. They are also hitscan.

## Why It's Good For The Game

Apparently people don't like the Condor. Too much effort for not enough
reward. After all, revolvers exist. 'It must be a joke' they say! 'It's
joke content! I went to all that effort to make it for nothing! That
slut Anne tricked us!'

**Wrong, bitch.**

If you want the Condor to make you shit yourself the moment someone with
it appears on the screen, then fine!

### **You get what you fucking deserve.**

## Changelog
:cl:
balance: Despite earlier reports suggesting that the famous lethality of
the Regal Condor was largely a myth, there has been rumors that the gun
has once again started to display its true killing potential on any
station that it 'manifests'.
/:cl:

---
## [AquillaF/Shiptest](https://github.com/AquillaF/Shiptest)@[7f8874df29...](https://github.com/AquillaF/Shiptest/commit/7f8874df29bdd5624bc957907249edffbbeaba12)
#### Saturday 2023-11-18 00:43:51 by Zevotech

Mashes several of the Whitesands Survivor Camp ruins into one extra large ruin (#1640)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Combines the whitesands surface camp adobe, farm, gunslingers,
survivors, hunters and saloon into one massive, 59x59 ruin. Some various
extra loot and changes have been made throughout, generally to improve
the experience of digging through the trash for goodies. Changes the
riot shotgun in the saloon to a double barrel shotgun. Also cleans up
the various issues with the ruins, like walls under doors, or area
passthroughs being used excessively over the outside of the ruins,
resulting in them generating in the middle of mountains buried in the
rock.

"Well, why didn't you add the drugstore?" The loot in it was too good.
The stuff in there can really help a ship get on its feet, and I am not
gonna deprive them of that just to shove it in an already packed massive
ruin area. I'm not saying it doesn't need its own remap, just that it
doesn't fit well with the other camps put into this ruin.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
"a ruin that is tiny and sucks on purpose is still bad" and holy shit
did most of the camps fit this criteria. Survivor, Gunslinger, and
Hunter camp variants were the smallest ruins in the game next to the one
that was just a single tumor, and constantly took up entire map
generations just to be a massive dissapointment to any player that came
across them. Or they would spawn in the middle of an acid lake. Either
way this ruin is massive and should provide a breath of fresh air for
scavengers and combat hungry miners alike.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pics or it Didn't Happen

![image](https://user-images.githubusercontent.com/95449138/208811497-ad556187-174a-4803-aea5-be40f0bb3038.png)
Ingame, two pics due to view range not being large enough to get the
full thing at a good quality.

![image](https://user-images.githubusercontent.com/95449138/208816213-082d6597-9718-45ff-9132-2907fcf63a57.png)

![image](https://user-images.githubusercontent.com/95449138/208816258-a3e2909b-fc98-4686-9bdc-8dc3192421e1.png)


## Changelog

:cl:
add: whitesands_surface_camp_combination, a survivor village comprised
of smaller revamped whitesands camps all packaged in one ruin. can be
found in the map catalogue.
del: whitesands_surface_camp adobe, farm, gunslingers, survivors,
hunters and saloon, for being tiny ruins that suck.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [Thera-Pissed/Shiptest](https://github.com/Thera-Pissed/Shiptest)@[2a74c23d62...](https://github.com/Thera-Pissed/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Saturday 2023-11-18 00:44:56 by Imaginos16

Nerfs the everloving almighty shit out of the jungle demonic office ruin (#2430)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Nerfs the ruin by removing most of its gamer gear, and changing the
syndicate hardsuit you find into a scarlet hardsuit.


Not to mention the two goddamn deathsquad hardsuits all there,
wholesale, for free.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/a8333190-37ce-441f-a746-bb5f2fc26828)

This shit is not okay jesus fucking christ, two deathsquad hardsuits?
Are you insane?
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
balance: The Jungle Demonic Office Ruin has now been appropriately
balanced, now only having a scarlet hardsuit, decent syndicate armor,
and a bulldog with no spare mags.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[d31c21ff1b...](https://github.com/DATA-xPUNGED/DataStation/commit/d31c21ff1b57ba7003f9bbdcf51171d3215a0774)
#### Saturday 2023-11-18 00:55:10 by jimmyl

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
## [edsonfrancavasconcelos/vasconvert-all](https://github.com/edsonfrancavasconcelos/vasconvert-all)@[3b3b7b019a...](https://github.com/edsonfrancavasconcelos/vasconvert-all/commit/3b3b7b019af5574c6e272736488c8345826b99be)
#### Saturday 2023-11-18 01:03:07 by Edson França Vasconcelos

Create README.md


Vasconvert-all
Vasconvert-all Logo

A simple web application, Vasconvert-all, designed for currency conversion and astronomical calculations. This project utilizes HTML, CSS, and JavaScript to create an interactive and user-friendly experience.

Features
Currency Conversion: Convert Brazilian Real (BRL) to various currencies including US Dollar (USD), British Pound (GBP), and Cryptocurrency.
Astronomical Calculation: Calculate the distance in light-years based on a predefined value and display the result.
Screenshots
Vasconvert-all Screenshot

How to Use
Open index.html in a web browser.
Enter your name when prompted.
Enter the amount in Brazilian Real that you want to convert.
Choose the currency (Dolar, Pound, or Cripto) for conversion.
View the converted amount in the selected currency.
Receive information about the distance in light-years.
Styling
The application features a stylish and responsive design, making use of background images and custom fonts.

Dependencies
No external dependencies are required. The project uses pure HTML, CSS, and JavaScript.

Contributing
Feel free to contribute to the project by submitting issues or pull requests. Your feedback and suggestions are highly appreciated.

License
This project is licensed under the MIT License.

Acknowledgments
Alura for the inspiration and educational content.
Background image source: motospace.jpeg
Author
Edson França Vasconcelos

---
## [OrionTheFox/tgstation](https://github.com/OrionTheFox/tgstation)@[d1ad9b6658...](https://github.com/OrionTheFox/tgstation/commit/d1ad9b665823708c3ae651eb9729023968e7feaf)
#### Saturday 2023-11-18 01:04:20 by necromanceranne

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
## [IbissKB/FrondStation-TG](https://github.com/IbissKB/FrondStation-TG)@[4a618d0561...](https://github.com/IbissKB/FrondStation-TG/commit/4a618d05616c654924ea86ea63eb4a12684caeb1)
#### Saturday 2023-11-18 01:07:09 by SkyratBot

[MIRROR] Watcher Nest Lavaland Ruin [MDB IGNORE] (#24286)

* Watcher Nest Lavaland Ruin (#78790)

## About The Pull Request

Adds a small new lavaland ruin, the Watchers' Grave.

![image](https://github.com/tgstation/tgstation/assets/7483112/9c3fa6f0-3e7d-4540-8646-5229eb11445b)

![image](https://github.com/tgstation/tgstation/assets/7483112/93bc14f0-9a0c-40d3-bd30-cc79a0d85752)

You will need to figure out yourself how to find a way through the walls
surrounding it (it's not very hard).
This is mostly just atmospheric but also serves as a delivery vehicle
for a unique item; an orphaned Watcher egg.
(That's kind of it in terms of loot, unless you count a handful of
lavaland mob corpses and mushrooms).

You can either eat this (it's an egg), throw it at someone to spawn an
angry watcher, or keep hold of it for a while and see what happens.

<details>

![dreamseeker_cMNnZXjfgL](https://github.com/tgstation/tgstation/assets/7483112/841db8fc-19ac-431f-aa66-c9ec5fbedbc3)

That's right it's your very own baby watcher.
It orbits your head and shoots at lavaland creatures for unimpressive
damage. It won't ever intentionally shoot a player but they might walk
in front of it, as it doesn't hurt very much they will probably forgive
you.
If you die it will continue circling your corpse to guard it against
predation.
</details>

In creating this ruin I also added a new component called "corpse
description".
It provides some extra examine text to a corpse which is removed
permanently if the mob is revived.
There's a field you can varedit on corpse spawners (or make a subtype)
which will automatically apply it to spawned corpses.
You can use it for environmental storytelling. Or admins can use it to
make fun of how you died.

Also I fixed basic mobs runtiming when examined by ghosts.

## Why It's Good For The Game

More variety in map generation. It's cute.
Adds a tool that mappers might like.

## Changelog

:cl:
add: Adds a new lavaland ruin where you can find a unique egg.
/:cl:

* Watcher Nest Lavaland Ruin

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [patevs/terminal](https://github.com/patevs/terminal)@[86fb9b4478...](https://github.com/patevs/terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Saturday 2023-11-18 01:12:45 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [TheNeoGamer42/Shiptest](https://github.com/TheNeoGamer42/Shiptest)@[b22529fc74...](https://github.com/TheNeoGamer42/Shiptest/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Saturday 2023-11-18 01:21:03 by zevo

Fixes rock sprites ingame [WHOOPS] (#2332)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Rocks were invisible in game due to a recently merged PR of mine. this
is why we testmerge PRs! anyways this should fix them.

Adds flora and rock missing texture sprites to most flora files to
prevent something like this from ever happening again.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
invisible things that block movement bad yeah. i want to fix my
mistakes.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Most rocks are now visible again
add: Most flora files now have missing texture sprites to make it easier
to spot when something has gone wrong.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[8720fef596...](https://github.com/treckstar/yolo-octo-hipster/commit/8720fef596d0d4f6ffed2c72eeef265216e4e834)
#### Saturday 2023-11-18 01:22:05 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [RikerW/dNAO](https://github.com/RikerW/dNAO)@[20d62687e4...](https://github.com/RikerW/dNAO/commit/20d62687e4a34836c8d131b82213520a459c3c97)
#### Saturday 2023-11-18 01:54:22 by RikerW

minor tweaks - gwf, tty descendant random

tty can't random into descendant (curses already couldn't)

gwf now rerolls bottom 16%, 33%, 50% of rolls, not just 1/2/3 - so its not absolutely awful for larger weapons. I realized that like, oversized weapons have larger dice sizes, so this should _probably_ synergize better with them. Go figure. This will maxroll d2s, fun fact, but it probably did really bad things before this, since I didn't actually ever test that and I think it was doing n*3 + d(n, -1) or something stupid. Now it won't.

previously touched sflame logic but noisy fixed it more comprehensively so i removed my own

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[f3d81edb00...](https://github.com/Timberpoes/tgstation-nxt/commit/f3d81edb00b07160bc046ab0d79457e60aefba0e)
#### Saturday 2023-11-18 02:04:11 by Paxilmaniac

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
## [Zeldazackman/Citadel-Station-13-RP](https://github.com/Zeldazackman/Citadel-Station-13-RP)@[fb9c40f675...](https://github.com/Zeldazackman/Citadel-Station-13-RP/commit/fb9c40f6752f19e293da244c45e48dabb9236320)
#### Saturday 2023-11-18 02:12:08 by SpartanKadence

Jukebox Update (#6102)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This will add plenty of more songs to the Jukebox.

Song List:
Alternative:
Say It Ain’t So by Weezer
Buddy Holly by Weezer
The Good Life by Weezer
Troublemaker by Weezer
Undone by Weezer
Hash Pipe by Weezer (All Emagged)
Wayside by Mitchel Dae
Freaking Out the Neighborhood by Mac DeMarco

Arcade:
Skyline and Menagerie Mix by 63hnsh3
Deputized by Locknar
The Ashoka Attacks by Paul Ruskay

Electronic:
How Would You Like It? By Moxifloxi
Syrsa - Cythas - Magichnology
Beyond Memory by NINA

Jazz and Lounge:
People Equals Shit by Richard Cheese (Emagged)

Metal:
Alone I Break by Korn
Shoots and Ladders by Korn
Blind by Korn
A Different World by Korn ft. Corey Taylor
Kidnap the Sandy Claws by Korn (Emagged)
Before I Forget by Slipknot
Psychosocial by Slipknot
The Devil in I by Slipknot
Dead Memories by Slipknot
People Equals Shit by Slipknot
Fade Away by Breaking Benjamin
Give me a Sign by Breaking Benjamin
I Will Not Bow by Breaking Benjamin
Into the Nothing by Breaking Benjamin
Without You by Breaking Benjamin
Smooth Criminal by Alien Ant Farm
Movies by Alien Ant Farm
Happy Death Day by Alien Ant Farm
Violent Pornnography by System of a Down
Science by System of a Down
Spiders by System of a Down
Jet Pilot by System of a Down
Chic ‘n’ Stu by System of a Down
Chop Suey! by System of a Down
B.Y.O.B. by System of a Down
Last Resort by Papa Roach
Scars by Papa Roach
Words as Weapons by Seether
Crawling by Linkin Park
Leave Out All the Rest by Linkin Park
Papercut by Linkin Park
Lost by Linkin Park
In The End by Linkin Park
Bodies by Drowning Pool
Tear Away by Drowning Pool
I Don't Care by Apocalyptica ft. Adam Gontier
One by Metallica
Sad But True by Metallica
Wherever I May Roam by Metallica
Nothing Else Matters by Metallica
Master of Puppets by Metallica
Tenebre Rosso Sangue by Keygen Church (Emagged)
Simple Sight by Piercing Lazer (Emagged)
Order by Heaven Pierce Her (Emagged)

Classical and Orchestral:
One Final Effort by Martin O’Donnell
Never Forget by Martin O’Donnell

Rock:
8675309 Jenny Jenny by Tommy Tutone
I Love You Like An Alcoholic by The Taxpayers
Must Have Been The Wind by The Chalkeaters (Emagged)

_Yes, this list is very biased._
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

With the recent repair of the previous songs in the Jukebox, it would
seem to be a good idea to finally add more to the list, allowing for
more songs for players to choose from.


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
add: Added more songs to the Jukebox!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [goober3/hi-github-portside](https://github.com/goober3/hi-github-portside)@[88e683cec6...](https://github.com/goober3/hi-github-portside/commit/88e683cec669624228d5204d7e3da06e6075d158)
#### Saturday 2023-11-18 02:20:23 by zevo

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
## [thatoneguy650/Los-Santos-RED](https://github.com/thatoneguy650/Los-Santos-RED)@[c7ae3c227b...](https://github.com/thatoneguy650/Los-Santos-RED/commit/c7ae3c227bed11f7f64448d2e43fba1a3e7b9596)
#### Saturday 2023-11-18 03:13:16 by Jack Bauer

fuck this stupid fucking bullshit and fuck yourself

---
## [Mortalelite/server](https://github.com/Mortalelite/server)@[aa30c9ec2e...](https://github.com/Mortalelite/server/commit/aa30c9ec2e15fd526fca9080ab434939d12a9656)
#### Saturday 2023-11-18 03:28:34 by MowFord

Cait Sith Avatar:

- Cait sith has proper name prefix and named properly to be "Cait Sith" instead of "The CaitSith"
- BPs Implemented
  - Regal Slash (BP:Rage): 3-hit physical
  - Level ? Holy (BP:Rage): aoe magical
    - Rolls a die and does dmg proportional to roll
    - Only does damage if the target's level is divisible by the roll
  - Mewing Lullaby (BP:Ward):
  AoE lullaby that resets TP
  - Eerie Eye (BP:Ward):
  conal silence/amnesia with appropriate elemental resist check for amnesia, but retail does light check for silence
  - Reraise II (BP:Ward):
  single-target 60-minute reraise II buff for any party member
  - Raise II (BP:Ward):
  single-target raise II for any party member
  - Altana's Favor (BP:Ward):
  2-hour ability gives arise to all party members in range
  (Arise and reraise III with infinite duration)

---
## [saadindassum/saadindassum.github.io](https://github.com/saadindassum/saadindassum.github.io)@[eeec2b9575...](https://github.com/saadindassum/saadindassum.github.io/commit/eeec2b95758ae494001cd9b00a802d37adb379bf)
#### Saturday 2023-11-18 03:42:44 by saadindassum

Missed another thing

God damn you Javascript. Why can't you be normal?

Jk, thanks for helping me get shit done.

---
## [oxidecomputer/omicron](https://github.com/oxidecomputer/omicron)@[2fc0dfd8c1...](https://github.com/oxidecomputer/omicron/commit/2fc0dfd8c11f31e66cfaf8ee80586bb2ed607216)
#### Saturday 2023-11-18 04:06:46 by Andrew J. Stone

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
## [mohammadhosseinmoradi/react](https://github.com/mohammadhosseinmoradi/react)@[ac1a16c67e...](https://github.com/mohammadhosseinmoradi/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Saturday 2023-11-18 04:11:28 by Sebastian Markbåge

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
## [rowleynt/diapersplus](https://github.com/rowleynt/diapersplus)@[0636707f46...](https://github.com/rowleynt/diapersplus/commit/0636707f463a0325a1af0d2919a524936a48db78)
#### Saturday 2023-11-18 05:16:08 by biglarge

A test to change the behavior of the pissing status effect. We don't have to merge this if we don't like it. What has been changed (and why):
Instead of teleporting the player to the same spot, the player instead loses most (but not all) of their movement speed, and almost all of their attack damage. My reasoning here is that the process of teleporting is extremely choppy, and it has the side effect of mobs not being able to knock players around, water not being able to push players, etc. If the player is instead just slowed to an extreme degree, they are still left extremely vulnerable, but can be more easily interacted with by mobs/the world. The attack damage is reduced because funny. If you read the entire commit message to the very end then you like men and want to kiss them passionately and get married and live a long happy life together.

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[81a7c75583...](https://github.com/JohnFulpWillard/tgstation/commit/81a7c75583f75f76d8487b88e63ebaf1402af85b)
#### Saturday 2023-11-18 05:22:12 by necromanceranne

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
## [cyphar/runc](https://github.com/cyphar/runc)@[4d7357f609...](https://github.com/cyphar/runc/commit/4d7357f6096f3ae20543bbce8147bde158078c12)
#### Saturday 2023-11-18 05:48:46 by Aleksa Sarai

tree-wide: use /proc/thread-self for thread-local state

With the idmap work, we will have a tainted Go thread in our
thread-group that has a different mount namespace to the other threads.
It seems that (due to some bad luck) the Go scheduler tends to make this
thread the thread-group leader in our tests, which results in very
baffling failures where /proc/self/mountinfo produces gibberish results.

In order to avoid this, switch to using /proc/thread-self for everything
that is thread-local. This primarily includes switching all file
descriptor paths (CLONE_FS), all of the places that check the current
cgroup (technically we never will run a single runc thread in a separate
cgroup, but better to be safe than sorry), and the aforementioned
mountinfo code. We don't need to do anything for the following because
the results we need aren't thread-local:

 * Checks that certain namespaces are supported by stat(2)ing
   /proc/self/ns/...

 * /proc/self/exe and /proc/self/cmdline are not thread-local.

 * While threads can be in different cgroups, we do not do this for the
   runc binary (or libcontainer) and thus we do not need to switch to
   the thread-local version of /proc/self/cgroups.

 * All of the CLONE_NEWUSER files are not thread-local because you
   cannot set the usernamespace of a single thread (setns(CLONE_NEWUSER)
   is blocked for multi-threaded programs).

Note that we have to use runtime.LockOSThread when we have an open
handle to a tid-specific procfs file that we are operating on multiple
times. Go can reschedule us such that we are running on a different
thread and then kill the original thread (causing -ENOENT or similarly
confusing errors). This is not strictly necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) since
only operating on the actual inodes associated with the tid requires
this locking, but because of the pre-3.17 fallback for CentOS, we have
to do this in most cases.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [cam900/mame](https://github.com/cam900/mame)@[65ec4542ca...](https://github.com/cam900/mame/commit/65ec4542ca3c0092247ebcab86d21eff987e4472)
#### Saturday 2023-11-18 05:50:10 by wilbertpol

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
## [KunalSalunkhe31/Statistical-Report-](https://github.com/KunalSalunkhe31/Statistical-Report-)@[2a3ce772d6...](https://github.com/KunalSalunkhe31/Statistical-Report-/commit/2a3ce772d6cb6c14be20483db95fc3849ba2ba89)
#### Saturday 2023-11-18 06:29:01 by Kunal Chatur Salunkhe

GLM Report on Result of Internal Exam 

In the realm of statistical analysis, the Generalized Linear Model (GLM) stands as a cornerstone methodology, serving as a powerful tool for modeling a wide array of data types and patterns. It is a versatile statistical framework that finds applications in a multitude of disciplines, from epidemiology to finance, and from ecology to social sciences. In this report, we delve into a comprehensive study of GLM results, focusing on their application and relevance within the context of both Applied Statistics and Pure Statistics programs.

The motivation behind this study is to bridge the gap between theory and practical application in the field of statistics, particularly within the academic setting of Applied and Pure Statistics programs. We recognize that student’s performance, represented by the variable "Marks," is influenced by various factors, such as the "Course" they are enrolled in, the "Time" allocated for studying, their "Anxiety Level," and even "Gender" differences. Understanding the relationship between these variables is crucial in designing effective educational strategies, identifying potential challenges, and ultimately enhancing the learning experience for students.

By using Generalized Linear Models, we aim to provide a comprehensive analysis of the interplay between these variables, enabling us to draw meaningful conclusions and recommendations for program improvement. This study is not only valuable to educators but also to students, administrators, and policymakers who seek to optimize the educational environment, ensure fairness, and promote better learning outcomes.

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[5175ae0637...](https://github.com/san7890/bruhstation/commit/5175ae06374450b87324bb280c754e53880b7b16)
#### Saturday 2023-11-18 06:54:26 by John Willard

TGUI Destructive Analyzer (#79572)

## About The Pull Request

I made this to help me move more towards my goals [laid out
here](https://hackmd.io/XLt5MoRvRxuhFbwtk4VAUA) which currently doesn't
have much interest.

This makes the Destructive Analyzer use a little neat TGUI menu instead
of its old HTML one. I also touch a lot of science stuff and a little
experimentor stuff, so let me explain a bit:
Old iterations of Science had different items that you can use to boost
nodes through deconstruction. This has been removed, and its only
feature is the auto-unlocking of nodes (that is; making them visible to
the R&D console). I thought that instead of keeping this deprecated code
around, I would rework it a little to make it clear what we actually use
it for (unhiding nodes).
All vars and procs that mentioned this have been renamed or reworked to
make more sense now.

Experimentor stuff shares a lot with the destructive analyzer, so I had
to mess with that a bit to keep its decayed corpse of deprecated code,
functional.

I also added context tips to the destructive analyzer, and added the
ability to AltClick to remove the inserted item. Removing items now also
plays a little sound because it was kinda lame.
Also, balloon alerts.

## Why It's Good For The Game

Moves a shitty machine to TGUI so it is slightly less shitty, now it's
more direct and compact with more player-feedback.
Helps me with a personal project and yea

### Video demonstration

I show off connecting the machine to R&D Servers, but I haven't changed
the behavior of that and the roundstart analyzers are connected to
servers by default.


https://github.com/tgstation/tgstation/assets/53777086/65295600-4fae-42d1-9bae-eccefe337a2b

## Changelog

:cl:
refactor: Destructive Analyzers now have a TGUI menu.
/:cl:

---
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[bed92e193c...](https://github.com/Donglesplonge/tgstation/commit/bed92e193ce4a79824fd4fd30a900245dca870ae)
#### Saturday 2023-11-18 06:55:35 by san7890

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
## [WordlessMeteor/LoL-DIY-Programs](https://github.com/WordlessMeteor/LoL-DIY-Programs)@[42c507ce20...](https://github.com/WordlessMeteor/LoL-DIY-Programs/commit/42c507ce20a1f5cde9fabcd306ccc7921bdf6500)
#### Saturday 2023-11-18 07:06:15 by WordlessMeteor

查战绩脚本和自定义脚本11的一些功能更新【A Function Update of Customized Programs 5 and 11】

一、程序更新综述（Program Update Summary 4.23 -> 4.24）
1. 排序工作表（Worksheet sorting）
对于本程序集的老用户，特别是自定义脚本5和11的老用户来说，有的时候在召唤师文件夹里保存的工作簿的各工作表的顺序不尽如人意。这主要是因为pandas库支持的工作簿导出方式中，只有追加模式是最好用的，然而这也带来一个问题，就是后追加的工作表可能在对局创建时间上比前面的追加的工作表更早。（这么说其实有点不严谨，因为对局创建时间顺序和对局序号顺序不是完全相同的——同一个服务器上，对局序号较小的对局是有可能后创建的。）如果是每天都有导出某名召唤师的战绩的话，手动调一调也还能接受。（这里提供一个小技巧，就是当一张工作簿存在上百张工作表而导致定位到特定工作表比较费劲时，可以通过鼠标右键点击工作表栏左边的箭头处，这时Microsoft Excel会弹出“激活”窗口，显示“活动文档”。在活动文档中查看想要跳转的工作表比较方便。）但是如果工作表的顺序错乱得比较严重，那调整起来就费劲了。
For old users of this program set, especially the Customized Programs 5 and 11, sometimes the order of sheets in the workbook saved under the corresponding summoner folder aren't satisfying. This is mainly because among the export approach that `pandas` library supports, only the "append" mode works best, which brings about a problem in the meantime: the later appended sheets may be earlier than the earlier appended, in terms of the gameCreationTime. (Actually this statement isn't so rigorous, for the gameCreationTime order and the matchID order aren't the same thing - On a specific server, a match of a smaller matchID may be created later.) If a user exports summoner profile daily, then a manual adjustment of the sheet order is relatively acceptable. (Hint: When there're hundreds of sheets in an Excel workbook, so that it takes a lot of time to scroll to a specific sheet, the user may right-click the bar with two triangles at the left of the sheet bar. Then, an "Activate" window will pop up, displaying "Active documents". It should be more handy to locate to a specific sheet by this window.) However, if the sheets are largely disordered, then it won't be easy to totally order them.
比如如果一位用户在第11赛季的时候使用存档脚本查询了一名召唤师的英雄联盟对局，得到400张工作表。然后他使用本次功能更新前的脚本查询了一名召唤师的云顶之弈对局，这样在原工作簿的最后又追加了200张工作表。但问题在于，这位召唤师只有在云顶之弈刚出的时候才玩过，大概是第9赛季的时候才玩过，那这些对局的对局序号以及创建时间都先于之前查询的英雄联盟对局。但是它们被追加到了工作表的最后。这样，要把200张工作表一张一张移动到这400张工作表前面（现有的Excel不支持批量移动工作表），那工作量就相当大了。因此，便产生了这一条功能更新。
Let's look at such an example. Suppose a user searched for a summoner's LoL matches in Season 11 using the archived Customized Program 5, which generated a workbook with about 400 sheets. Then, recently he's used the programs before this functional update to search for the same summoners' TFT matches, which appended 200 sheets to the last of the sheet list of the workbook. But it appeared that this summoner only played TFT when it was just released in Season 9. Therefore, these TFT matches' matchIDs and gameCreationTimes are all earlier than those of the LoL matches previously looked up. However, they were appended to the last. In such case, it would be considerably large work to move the 200 sheets to the front of the 400 sheets one by one (for current Excel doesn't support moving sheets in batch). For this reason, this functional update is committed.
2. 使对局信息类文本文档的生成成为可选项（Generation OPTION of text files of game information class）
从英雄联盟自定义房间创建程序集（算上之前存档的存储库）创建到此次更新前（实际上我开始撰写代码甚至比创建存储库要早一年），程序都是默认输出文本文档的。现在，在决定是否生成文本文档方面，用户具有选择权了。这主要是有两点考虑：其一，输出文本文档的过程涉及到大量文件读写操作，而在配置不佳的条件下，这可能导致文件资源管理器占用较多资源，进而导致游戏卡顿；其二，大量文本文档会使得文件夹内容混乱度增加，如果用户想要通过滚轮来翻转查找召唤师生涯工作簿，则要翻转很长时间。如果这两点问题的确有困扰到您，那么您可以选择不生成文本文档。但是，还是建议始终生成文本文档，因为【本地重查】模式依据的是这些文本文档的文件名。换言之，这些文本文档的文件名也是含有信息价值的。
Ever since the LoL-DIY-Program repository (including the archived repository) was created and until this update (actually I'd begun to created these programs one year before), the program always generates the text files. Now, whether to generate these text files is up to the user to decide. Here're mainly two considerations: on the one hand, text file generation involves a great amount of file input/output operations, which may cause the Explorer.exe to take up much resource and results in the low game FPS; on the other hand, increase of the number of text files contributes to the folder's entropy (the degree of chaos), and if the user is looking for the summoner profile workbook, then it'll take a long time. If these two problems do make a difference to your experience, then you may choose not to generate the text files. Nevertheless, you're suggested to always generate them, for [Local Recheck] is based on these text files' names. In other words, there lies information in these text files' names.
3. 单独检查玩家邂逅情况（Check of single recently played summoner）
在此次更新前，近期一起玩过的玩家只能在英雄选择阶段进行检查。这样有一个限制——往往不能检查一名对手是否曾经遇到过，因为在所有队列房间中，对手信息是不可见的。现在，当程序检测到玩家正在游戏中时，允许玩家单独查询一名玩家是否曾经遇到过。
Before this update, recently played summoners can be checked only within the champ select stage. This limits the function - the user won't be able to check whether an enemy has been encountered before, for in all queue lobbies during champ select stage, enemy information are hidden. Now, if the program detects a user in game, then the user is allowed to check whether one summoner has been played with at a time.
二、实现细节（Implementation Details）
1. 添加了排序工作表的代码。排序算法是通过逐渐计算每个工作表的原来的位置与排好序后的位置的差值，来对每个工作表进行移动。（自定义脚本5第5、3026、3027、3071和3133～3172行。）
Added the code to sort the sheets. The algorithm is designed to calculate the difference between each sheet's original position and its position after being sorted. The movement offset is based on this difference. (Lines 5, 3026, 3027, 3071 and 3133～3172 in Customized Program 5.)
说明：之前尝试问gpt-3.5对工作表进行排序，gpt-3.5给出的一个答案是通过读取所有工作表，再将所有工作表按照顺序追加到新的工作簿中，从而得到顺序工作表。这是非常暴力的一个算法，在时间和空间上开销都很大。后来gpt-3.5又提出了基于openpyxl库的load_workbook函数和move_sheet属性的方法，大大降低了时空开销。
Note: The first time I tried to ask gpt-3.5 how to sort the sheets, it suggested that I read in all the sheets and append the sheets to a new workbook according to a specific order to get the workbook with ordered sheets. This is a very brute-force algorithm that takes up great time and space. Later, gpt-3.5 put forward the approach based on the `load_workbook` function in `openpyxl` library and the `move_sheet` attribute, which lowered the spatiotemporal cost significantly.
2. 添加了export_txt变量来控制文本文档的生成，并添加了相应的提示语和调整了部分代码的缩进。（自定义脚本5第1920、1921、1986、2023、2024、2026、2027、2508、2509和2538～2562行。）
Added a variable `export_txt` to control the generation of text files. Adaptively, added the corresponding prompt statements and adjusted the indentation of some code. (Lines 1920, 1921, 1986, 2023, 2024, 2026, 2027, 2508, 2509 and 2538～2562 in Customized Program 5.)
3. 添加了“正在游戏”状态下检测单名玩家是否曾经遇到过的代码。其中，部分变量以check为后缀，来表明它们属于【单独检查】部分代码。（自定义脚本11第2528～2530、2541、2543、2689～2782行。其中，检查召唤师名可用性的部分沿用了自定义脚本5和自定义脚本11的【生成模式】对于召唤师名可用性的判断。）
Added the code to detect whether a single player has been encountered before when the gameflow phase is "InProgress". In this part, some variables are postfixed with "check" to indicate they belong to the code that implements [Single Check]. (Lines 2528～2530, 2541, 2543, 2689～2782 in Customized Program 11. The part that checks the summoner name availability inherits from the code that implements the judgment of summoner name eligibility in Customized Program 5 and the [Generate Mode] in Customized Program 11.)
4. 原代码中的session变量现更名为champ_select_session，以和gameflow_session变量区分开来。（自定义脚本11第2559～2562、2612、2613、2673和2687行。）
The variable `session` is now renamed as `champ_select_session` to distinguish from the variable `gameflow_session`. (Lines 2559～2562, 2612, 2613, 2673 and 2687 in Customized Program 11.)
说明：添加gameflow_session变量的原因是为了获取对局序号。在游戏中，“/lol-champ-select/v1/session”接口将返回“无可用委派”的提示，而“/lol-gameflow/v1/session”会正确地给出游戏信息。
Note: The reason for adding the `gameflow_session` variable is to get the gameId. When a game is in progress, the API `lol-champ-select/v1/session` returns `No active delegate`, while `/lol-gameflow/v1/session` returns the game information as expected.
声明：由于本脚本基于LCU通信进行开发，是通过LeagueClientUx.exe获取连接信息的，而对局内的玩家信息是需要通过League of Legends.exe进行通信的，因此本程序集不会支持直接获取对局中的敌方信息，只能由玩家手动输入敌方的召唤师名或拳头ID。
Declaration: This program is developed based on LCU communication, and the connection is built through LeagueClientUx.exe. However, in-game player information can only be captured through `League of Legends.exe`. Therefore, this program (set) won't support directly fetching the enemies' information. The user has to input an enemy's summoner name or Riot ID by hand.
5. 本次更新还包括三条代码上的优化。
This update also introduces 3 code optimization ideas.
（1）调整了一处换行符。（自定义脚本5第3131行。）
Adjusted a line break character. (Line 3131 in Customized Program 5.)
（2）修复了一处提示错误。现在，所有“回退”替换为“转”，因为实际上在程序找不到一个版本的数据资源时而执行FindPostPatch函数时，FindPostPatch返回的是更新的一个版本，而不是更旧的一个版本。（自定义脚本5第1421、1494、1757、1823、2073、2122、2168、2223、2267、2656、2699、2792、2861、2924和2962行和自定义脚本11第1214、1287、1570、1625、1669、1906、1948、2036、2103、2163和2201行。）
Fixed a mistake in prompts. Now, all "回退"s are replaced by "转"s, because when the program fails to get the data resource of a patch and triggers off `FindPostPatch` function, this function returns a later patch, instead of an older patch. (Lines 1421, 1494, 1757, 1823, 2073, 2122, 2168, 2223, 2267, 2656, 2699, 2792, 2861, 2924 and 2962 in Customized Program 5 and Lines 1214, 1287, 1570, 1625, 1669, 1906, 1948, 2036, 2103, 2163 and 2201 in Customized Program 11.)
（3）现在，要输出的近期一起玩过的英雄联盟玩家工作表和近期一起玩过的云顶之弈玩家工作表的表头分别被存储为recent_LoLPlayer_fields和recent_TFTPlayer_fields变量，以缩减代码规模。（自定义脚本11第2544～2551、2586、2588、2636、2638、2743和2744行。）
Now, the headers of recently played LoL and TFT summoners' sheets are assigned to two variables `recent_LoLPlayer_fields` and `recent_TFTPlayer_fields`, respectively, to simplify the code. (Lines 2544～2551, 2586, 2588, 2636, 2638, 2743 and 2744 in Customized Program 11.)
（4）需要强调，现在当用户选择不生成文本文档时，“保存进度”的提示被“加载进度”取代。（自定义脚本5第2023～2027和2558～2562行。）
Note that when a user chooses not to generate text files, the prompt "Saving process" is now replaced by "Loading process". (Lines 2023～2027 and 2558～2562 in Customized Program 5.)
6. 相应于第3条实现细节，调整了自定义脚本11的一条说明。（说明文档第153和154行。）
Corresponding to the third implementation detail, adjusted an instruction of Customized Program 11. (Lines 379 and 380.)
三、发行版（Release）
从此版本开始，完整且必要的文件将被整理成一个压缩包，置于发行版中。发行版将跟随每次提交而更新。需要注意，在发行版中，“自定义房间创建（Custom Lobby Creation）”被重命名为“双语版（zh-CN & en-US）”。
Since this version, the complete and necessary files are sorted into a zip file and released. The release will follow the update of each commit. Note that the "自定义房间创建（Custom Lobby Creation）" folder is renamed as "双语版（zh-CN & en-US）" in the release.

---
## [marcsvll/ngx_wasm_module](https://github.com/marcsvll/ngx_wasm_module)@[ecd7896846...](https://github.com/marcsvll/ngx_wasm_module/commit/ecd78968469ed5fa40d81a26600964535d3e6b00)
#### Saturday 2023-11-18 07:11:23 by Thibault Charbonnier

refactor(proxy-wasm) improve pwexec resurrection and instance lifecycle

The main goal of this overhaul is to simplify `on_context_create`, make
it fully re-entrant *and* properly handle instance recycling at the same
time.

The way to do so, in my opinion, was to move `pwexec` creation where
`rexec` already was. In other words, always lookup the context id in the
instance rbtree, and if not found, create it. This means that
surrounding code also needed big overhauls. It also removes the
reference counting poor man's GC of the older implementation. The code
became really ugly by then so I took the time to also review this
module's code structure instead of making a *very* ugly commit.

This new ngx_proxy_wasm.c file should be much easier to read and follow
now.

One change I do not fully like is moving the `next_id` to a global
counter, but we do not have a "global proxy-wasm conf" object yet. I
also started thinking about pre-allocating a number of `pwexecs` (like
`worker_connections`) and use free/busy queue that all filter chains can
dip into to get a context id + context memory zone. Perhaps for a later
time.

---
## [WizWilliam1/spc-rant](https://github.com/WizWilliam1/spc-rant)@[b970329613...](https://github.com/WizWilliam1/spc-rant/commit/b970329613401cab0e2793e4099e7fe4e9afa148)
#### Saturday 2023-11-18 07:12:30 by WizWilliam1

SPC Rant Version 3.0

## Development Logs Update

### Date: 11/18/2023

### Project: SPC RANT

---

#### 1. **Dark Mode and Light Mode Functionality**

Implemented a robust JavaScript function to enable Dark Mode and Light Mode seamlessly across both 'index.php' and 'rant.php'. Users now have the flexibility to choose their preferred theme for a personalized browsing experience.

---

#### 2. **User Posts Redesign**

Revamped the user posts display to enhance the overall aesthetic and user experience. The new design ensures better readability and engagement, aligning with modern web design standards.

---

#### 3. **Comment System Enhancement**

Introduced an advanced comment system with improved functionality. Users can now express their thoughts and engage in discussions effectively. The new system is designed for both simplicity and user-friendliness.

---

#### 4. **Modal Popup in 'Rant Now' Feature**

Added a modal popup to the 'Rant Now' feature, providing a more interactive and visually appealing interface. Users can now compose their rants seamlessly within the modal, enhancing the overall user journey.

---

#### 5. **Like Counter Functionality**

Implemented a like counter feature to track user engagement with posts. Although the feature currently operates without a database integration, it lays the foundation for upcoming database implementation.

---

#### 6. **Slight Ajax Integration**

Introduced Ajax code snippets to the project, improving the overall responsiveness and interactivity of the web application. Ajax ensures smoother data retrieval and enhances the user experience without requiring a full page reload.

---

#### 7. **Performance Optimization**

Conducted performance optimizations to streamline the application. This includes code refactoring and adjustments aimed at achieving better loading times and overall efficiency.

---

#### 8. **Bug Fixes and Stability Improvements**

Addressed several bugs and enhanced the stability of the application. Resolved issues reported during testing to ensure a seamless and error-free user experience.

---

#### 9. **Upcoming Features Preview**

Provided a sneak peek into upcoming features and functionalities planned for future releases. Stay tuned for exciting additions to further enrich the user experience.

---

### Conclusion:

This update marks significant progress in enhancing the functionality and aesthetics of [Your Web Application Name]. Looking forward to the continuous evolution of the project with upcoming features and improvements.

---

### Step-by-Step Instruction Tutorial:

#### Importing SQL File Using phpMyAdmin

**Step 1: Access phpMyAdmin**
1. Open your web browser.
2. Go to [http://localhost/phpmyadmin/index.php?route=/](http://localhost/phpmyadmin/index.php?route=/).

**Step 2: Navigate to Import Section**
1. Once logged in, find and click on the "Import" tab in the top navigation menu.

**Step 3: Choose File**
1. In the "File to import" section, click the "Choose File" button.
2. Select the ".sql" file you want to import from your local machine.

**Step 4: Upload File**
1. After selecting the file, click the "Go" or "Open" button to upload the ".sql" file.

**Step 5: Configure Import Options**
1. Scroll down to view additional options if needed.
2. You can configure settings such as character set or collation.

**Step 6: Start Import**
1. Once configured, scroll down further.
2. Click the "Go" or "Import" button to start the import process.

**Step 7: Wait for Completion**
1. Wait for the import process to complete. The time taken depends on the size of the SQL file.

**Step 8: Confirmation**
1. Once completed, you should see a confirmation message indicating a successful import.

---
## [jobalisk/Matoran-Quest](https://github.com/jobalisk/Matoran-Quest)@[c827543c63...](https://github.com/jobalisk/Matoran-Quest/commit/c827543c6358a16b4e19b4685b4a7d938b94989f)
#### Saturday 2023-11-18 07:38:31 by jobalisk

realized that I hadn't actually solved the player name bug cause I hadn't put any code about it in the mapcontroller. I hate my life.

---
## [Darkness6030/Mindustry](https://github.com/Darkness6030/Mindustry)@[d628aa442e...](https://github.com/Darkness6030/Mindustry/commit/d628aa442ed4cbe63281ca29f0bd1f479323dc1a)
#### Saturday 2023-11-18 07:46:59 by Darkness

Remove Darkdustry from the Global Server List 

The time has come. It's been more than two years since we started Mindurka, which was later renamed to Darkdustry. It was an amazing time and an amazing experience to maintain the server, to create plugins and gamemodes, to discuss mindustry with all of you. But It's enough. The server is getting constantly DDoSed, the host dies all the time and I have no motivation to develop anything related to Mindustry. 
Goodbye. And I hope, we'll meet again.

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[9cf089361e...](https://github.com/Derpguy3/tgstation/commit/9cf089361e8cea86d2415de0535b1a28f517e040)
#### Saturday 2023-11-18 08:11:28 by Rhials

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
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[66f726dfe3...](https://github.com/Derpguy3/tgstation/commit/66f726dfe31dae0a14feaed8718c41e40e82af09)
#### Saturday 2023-11-18 08:11:28 by SyncIt21

General code maintenance for rcd devices and their DEFINE file (#78443)

## About The Pull Request
The changes made can be best summarized into points

**1. Cleans up `code/_DEFINES/construction.dm`**

Looking at the top comment of this file 

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L1

One would expect stuff related to materials, rcd, and other construction
related stuff. Well this file is anything but

Why is there stuff related to food & crafting over here then?

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L91-L94

It gets worse why are global lists declared here?

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L115
There is a dedicated folder to store global lists i.e.
`code/_globalvars/lists` for lists like these. These clearly don't
belong here

On top of that a lot of construction related defines has been just
dumped here making it too large for it's purposes. which is why this
file has been scraped and it's
1. crafting related stuff have been moved to its
`code/_DEFINES/crafting.dm`
2. global lists for crafting moved to
`code/_globalvars/lists/crafting.dm`
3. Finally remaining construction related defines split apart into 4
file types under the new `code/_DEFINES/construction` folder
- `code/_DEFINES/construction/actions.dm` -> for wrench act or other
construction related actions
- `code/_DEFINES/construction/material.dm` -> contains your sheet
defines and cable & stack related values. Also merged
`code/_DEFINES/material.dm` with this file so it belongs in one place
- `code/_DEFINES/construction/rcd.dm` -> dedicated file for everything
rcd related
- `code/_DEFINES/construction/structures.dm` -> contains the
construction states for various stuff like walls, girders, floodlight
etc

By splitting this file into multiple meaningful define file names will
help in reducing merge conflicts and will aid in faster navigation so
this is the 1st part of this PR

**2. Debloats the `RCD.dm` file(Part 1)**

This uses the same concepts as above. i.e. moving defines into their
appropriate files for e.g.

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L170

1. Global vars belong in the `code/_globalvars` folder so these vars and
their related functions to initialize them are moved into the
`code/_globalvars/rcd.dm` file
2. See this proc

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L200
This proc does not belong to the `obj/item/construction/rcd` type it's a
global "helper function" this is an effect proc as it creates rcd
holograms so it has been moved to the `code/game/objects/effects/rcd.dm`
file which is a global effect that can be used by anyone

And with that we have moved these vars & procs into their correct places
& reduced the size of this file . We can go even further

**3. Debloats the `RCD.dm` file(Part 2)**
This deals with the large list which contains all the designs supported
by the RCD

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L42

This list contains a lot of local defines. We can scrape some of them
and reduce the overall bulkiness & memory requirements of this list and
so the following defines

```
#define WINDOW_TYPE "window_type"
#define COMPUTER_DIR "computer_dir"
#define WALLFRAME_TYPE "wallframe_type"
#define FURNISH_TYPE "furnish_type"
#define AIRLOCK_TYPE "airlock_type"
#define TITLE "title"
#define ICON "icon"
#define CATEGORY_ICON_STATE  "category_icon_state"
#define CATEGORY_ICON_SUFFIX "category_icon_suffix"
#define TITLE_ICON "ICON=TITLE"
```

Have all been removed making this list a lot more cleaner. Why? because
a lot of these are just semantic sugar, we can infer the value of a lot
of these defines if we just know the type path of the structure the rcd
is trying to build for e.g. take these 2 defines

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/game/objects/items/rcd/RCD.dm#L13-L15

These defines tell the rcd UI the name and the icon it should display.
Rather than specifying these manually in the design we can infer them
like this

```
var/obj/design = /obj/structure/window  //let's say the rcd is trying to build an window
var/name = initial(design.name)         //we have inferred the name of the design without requiring TITLE define
var/icon = initial(design.icon_state)   //we have inferred the icon of the design without requiring ICON define
```

And so by using similar logic to the remaining defines we can eliminate
a lot of these local defines and reduce the overall size of this list.

The same logic applies to the different modes of construction, the
following defines

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/__DEFINES/construction.dm#L186-L192
Have all been removed and replaced with a single value `RCD_STRUCTURE`

All these modes follow the same principle when building them
1. First check the turf if the structure exists. If it does early return
2. If not create a new structure there and that's it

So rather than creating a new construction mode every time you want to
add a new design we can use this mode to apply this general approach
every time

The design list has also now been made into a global list rather than a
private static list. The big advantage to this is that the rcd asset
cache can now access this list and load the correct icons from the list
directly. This means you no longer have to manually specify what icons
you want to load which is the case currently.

https://github.com/tgstation/tgstation/blob/0fb8b8b218400b3f1805ae81e9bb0364d7a4e9c6/code/modules/asset_cache/assets/rcd.dm#L8-L9
This has lead to the UI icons breaking twice now in the past
- #74194
- #77217

Hopefully this should never repeat itself again

**4. Other RCD like device changes**
- Fixed the broken silo link icon when the radial menu of the RLD was
opened
- replaced a lot of vars inside RLD with defines to save memory
- Small changes to `ui_act` across RCD, Plumbing RCD and RTD
- Removed unused vars in RCD and snowflaked code
- Moved a large majority of `ui_data()` to `ui_static_data()` making the
experience much faster

Just some general clean up going on here

**5. The Large majority of other code changes**
These are actually small code changes spread across multiple files.
These effect the `rcd_act()` & the `rcd_vals()` procs across all items.
Basically it
- Removes a large majority of `to_chat()` & `visible_message()` calls.
This was done because we already have enough visual feedback of what's
going on. When we construct a wall we don't need a `to_chat()` to tell
us you have a built a wall, we can clearly see that
- replaces the static string `"mode"` with a predefined constant
`RCD_DESIGN_MODE` to bring some standard to use across all cases

Should reduce chat spam and improve readability of code. 

**6. Airlock & Window names**
The rcd asset cache relies on the design name to be unique. So i filled
in the missing names for some airlocks & windows which are subjective
and open to change but must have some value

**7 Removes Microwave PDA upgrade**
The RCD should not be allowed to build this microwave considering how
quickly it can spawn multiple structures and more importantly as it's a
special multipurpose machine so you should spend some effort in printing
it's parts and acquiring tools to complete it. This upgrade makes
obsolete the need to carry an
- A RPED to install the parts
- A screwdriver to complete the frame
- The circuit board for the microwave 

The most important point to note here is that whenever an RPED/circuit
board is printed at an lathe it charges you "Lathe Tax". The RCD with
this upgrade would essentially bypass the need to "Pay Taxes" at these
lathes as you are just creating a circuit board from thin air. This
causes economy imbalance(10 cr per print) which scales up the more of
these machines you make so to avoid this let's end the problem here

Not to mention people would not find the need to print the circuit board
for a regular microwave now if they have an RCD because they can just
make this microwave type making the need for a regular microwave
completely pointless.

Just build a machine frame with the RCD and complete the microwave from
there

## Changelog
:cl:
code: moved global vars, lists and helper procs for construction related
stuff to their appropriate files
code: reduced overall code size & memory of rcd design list and removed
unused defines
refactor: removed a ton of chat alerts for rcd related actions to help
reduce chat spam
refactor: some airlock & window default names have changed
fix: broken icon in radial menu of rld silo link
remove: removes microwave pda upgrade from RCD. It's a special machine
so spend some time in building it rather than shitting them out for free
with the RCD. Use the RCD upgrade to spawn a machine frame instead & go
from there
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [UncertainSchrodinger/dotfiles](https://github.com/UncertainSchrodinger/dotfiles)@[8f8fc5c1ae...](https://github.com/UncertainSchrodinger/dotfiles/commit/8f8fc5c1ae03d2da5d2abc7dfd99ba244dc7ed7a)
#### Saturday 2023-11-18 08:29:19 by Tatu Argillander

tools: Move to rtx

Mostly as always due to Python issues. Pyenv was a constant pain in the
ass, it was slow as fuck, there were other issues as well that my brain
has wiped away for protection.

Rtx seems fast and includes all the tools I need. Hopefully it'll work
consistently across tools. Tools like pyenv and jenv would copy the
original rbenv way but then differ due to some fucking reasons like
being pythonic. I think jenv never set JAVA_HOME or some brain dead shit
like that.

This allows me to replace at least the following tools:

* rbenv
* nodenv
* tfenv
* pyenv
* jenv

---
## [aled99/kernel_xiaomi_sm8250](https://github.com/aled99/kernel_xiaomi_sm8250)@[fa3195ebac...](https://github.com/aled99/kernel_xiaomi_sm8250/commit/fa3195ebacd7ba11ac902f1f49a4b1e479def046)
#### Saturday 2023-11-18 10:24:16 by Angelo G. Del Regno

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
## [XuehaiPan/pytorch](https://github.com/XuehaiPan/pytorch)@[3afb4e5cf7...](https://github.com/XuehaiPan/pytorch/commit/3afb4e5cf7b0162c532449fb5c9e7c7058a4c803)
#### Saturday 2023-11-18 10:24:59 by Brian Hirsh

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
## [ickshonpe/bevy](https://github.com/ickshonpe/bevy)@[ab300d0ed9...](https://github.com/ickshonpe/bevy/commit/ab300d0ed9990972679629af3ef18fd37c0e106c)
#### Saturday 2023-11-18 11:01:35 by Connor King

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[71b45e54ad...](https://github.com/tgstation/tgstation/commit/71b45e54adfaa4c681babc545db97fa7103289de)
#### Saturday 2023-11-18 12:06:03 by san7890

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
## [QingweiXu/rtk-libbpf](https://github.com/QingweiXu/rtk-libbpf)@[b064c40d94...](https://github.com/QingweiXu/rtk-libbpf/commit/b064c40d9460c34d8fb539cf0042b298b888cdd4)
#### Saturday 2023-11-18 12:18:32 by Daniel Borkmann

bpf: Add fd-based tcx multi-prog infra with link support

This work refactors and adds a lightweight extension ("tcx") to the tc BPF
ingress and egress data path side for allowing BPF program management based
on fds via bpf() syscall through the newly added generic multi-prog API.
The main goal behind this work which we also presented at LPC [0] last year
and a recent update at LSF/MM/BPF this year [3] is to support long-awaited
BPF link functionality for tc BPF programs, which allows for a model of safe
ownership and program detachment.

Given the rise in tc BPF users in cloud native environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications accidentally stepping on each others toes.
As a recap, a BPF link represents the attachment of a BPF program to a BPF
hook point. The BPF link holds a single reference to keep BPF program alive.
Moreover, hook points do not reference a BPF link, only the application's
fd or pinning does. A BPF link holds meta-data specific to attachment and
implements operations for link creation, (atomic) BPF program update,
detachment and introspection. The motivation for BPF links for tc BPF programs
is multi-fold, for example:

  - From Meta: "It's especially important for applications that are deployed
    fleet-wide and that don't "control" hosts they are deployed to. If such
    application crashes and no one notices and does anything about that, BPF
    program will keep running draining resources or even just, say, dropping
    packets. We at FB had outages due to such permanent BPF attachment
    semantics. With fd-based BPF link we are getting a framework, which allows
    safe, auto-detachable behavior by default, unless application explicitly
    opts in by pinning the BPF link." [1]

  - From Cilium-side the tc BPF programs we attach to host-facing veth devices
    and phys devices build the core datapath for Kubernetes Pods, and they
    implement forwarding, load-balancing, policy, EDT-management, etc, within
    BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
    experienced hard-to-debug issues in a user's staging environment where
    another Kubernetes application using tc BPF attached to the same prio/handle
    of cls_bpf, accidentally wiping all Cilium-based BPF programs from underneath
    it. The goal is to establish a clear/safe ownership model via links which
    cannot accidentally be overridden. [0,2]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [4] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.

We instead implemented the tcx (tc 'express') layer which is an fd-based tc BPF
attach API, so that the BPF link implementation blends in naturally similar to
other link types which are fd-based and without the need for changing core tc
internal APIs. BPF programs for tc can then be successively migrated from classic
cls_bpf to the new tc BPF link without needing to change the program's source
code, just the BPF loader mechanics for attaching is sufficient.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook have a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
entry point for tc BPF. The name tcx has been suggested from discussion of
earlier revisions of this work as a good fit, and to more easily differ between
the classic cls_bpf attachment and the fd-based one.

For the ingress and egress tcx points, the device holds a cache-friendly array
with program pointers which is separated from control plane (slow-path) data.
Earlier versions of this work used priority to determine ordering and expression
of dependencies similar as with classic tc, but it was challenged that for
something more future-proof a better user experience is required. Hence this
resulted in the design and development of the generic attach/detach/query API
for multi-progs. See prior patch with its discussion on the API design. tcx is
the first user and later we plan to integrate also others, for example, one
candidate is multi-prog support for XDP which would benefit and have the same
'look and feel' from API perspective.

The goal with tcx is to have maximum compatibility to existing tc BPF programs,
so they don't need to be rewritten specifically. Compatibility to call into
classic tcf_classify() is also provided in order to allow successive migration
or both to cleanly co-exist where needed given its all one logical tc layer and
the tcx plus classic tc cls/act build one logical overall processing pipeline.

tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail.

The work has been tested with tc-testing selftest suite which all passes, as
well as the tc BPF tests from the BPF CI, and also with Cilium's L4LB.

Thanks also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Acked-by: Jakub Kicinski <kuba@kernel.org>
Link: https://lore.kernel.org/r/20230719140858.13224-3-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [QingweiXu/rtk-libbpf](https://github.com/QingweiXu/rtk-libbpf)@[d7e583a6ea...](https://github.com/QingweiXu/rtk-libbpf/commit/d7e583a6eac64a79c21f1a749e6b3d371b884365)
#### Saturday 2023-11-18 12:18:32 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating internally about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle; the rationale for id is so that user
        space application does not need CAP_SYS_ADMIN to retrieve foreign fds
        via bpf_*_get_fd_by_id()
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog, links have their
      own infra for replacing their internal prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space application can query current state with revision, and pass it
    along for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficiency. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.
Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Thanks also to Andrii Nakryiko for early API discussions wrt Meta's BPF prog
management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Link: https://lore.kernel.org/r/20230719140858.13224-2-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[66b8b1d866...](https://github.com/Time-Green/tgstation/commit/66b8b1d8669379eac50fa358a3eb5e7707b46f25)
#### Saturday 2023-11-18 12:33:55 by Fikou

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
## [TheDailySimile/GuzzleHumdrum](https://github.com/TheDailySimile/GuzzleHumdrum)@[85ff16b7b9...](https://github.com/TheDailySimile/GuzzleHumdrum/commit/85ff16b7b9470e6d2316f7a86a260ff344ce75c6)
#### Saturday 2023-11-18 12:42:23 by The Daily Simile

Create Phantom : The Meaning of Lie.html

Misty@dissapointed : "but still Ms Sabrina so scornfully repellend Marc you know he's still her only relative nevertheless.."
Ash@straight : "the bigger question though compeer is that first he rejected your.. appreciation for his inclinations as you.."
Misty@angry : "shut up you b.. he's way better than you at handling emotions of losing something#.."
Ash@happy : "this reminds me something you see in the battle i only devised a scheme where it was un ill favoured match for Ms Birch because you never win against a Lokix if you're using an Goodra you see as then you expect the Bug to find a way to get under your skin so that you can trap it in the long run but the psychic enthusiasm that needs to be present for that is only going to be darkened by the illusion..shh..of your poise..sometimes it feels better just ot good enough to be on top of self something you'd agree..shh..only upon retrospective parity.."
Misty@very Angry : "shut up you b.. how dare you challenge my inclinations#.."
Ash@happy : "it's almost midnight compeer why don't you come over to Sabrina's cabin along Marc giving a false alarm even if he suspects your motives he fails to overcome logic and coincidence even if not emotion..shh..so quantifiable.."
Misty@frown : "you do it yourself i'm not a deceitful cheat in such an occasion so perfect for emotional blackmailing and no i'm not going to stay there either bye.."
Ash@shrug : "what is this strange idea of evaluatory morality despite overseeing Mr Slatr#.."
Brock@scowl : "a tribute to all pervasiveness night#.."
Ash@shrug : "fair enough the least inflected..shh..yet only as me#..now the trap will test not only emotion but also security..(happy)..shh..so unmonitored unless for emotional casualties..right..
been been been been my..seem seem seem seem thy/lastly hallucinate/that imposter of thought/captures ego's bot/to surveillance self..
thus alarm bell secured your mail alas you feel i cheat/been been all just my/seemy describe/thys feels..thee..
Thus Ash means lastly Further left no Me.."
Sabrina,Marc+Misty,Brock@scowl : "what created the commotion of shadowy figures and what forced the bond of souls to surpass the hype of suspense's own#.."
Ash@happy : "you're only going to find clues Gyre just as them while neglecting the fact that i'm ever haunted by selfs in terms of probable identities for one and each..on the wheels of truth it's only the more manifest where trivial facts become projected as desire paramount..
thus neither the Ceruledges or Armarogues or Machamps and so on nor the motions of what actually was moving nor the desires what proved to be only self deceiving would've seemed to be..shh..self counterin'..and Team Sic failed to understand it wasn't at all them who were pulling the strings rather their mere..desire to be just as mot them their selves..the more metaphorical is reality as is the legendary forward claim.."
🐺@scowl : "for the rest than me in terms of self it's the same me a result of being left ever free by the self countering hope and hopelessness rendering theleftover me ever free cunning indeed Ash apnei you're still under the purview of evaluatory tax having come in relativity thus our endeavours rhyming.."
Ash@shrug : "well i declared first up still Gyre unless only you would POPULARIZE do i have to be me..shh..through the comis of seein'..Phantom : The Meaning of Lie.."
🐺@scowl : "amen..bye#..Sabrina,Marc+Misty,Brock..Phantom : The Meaning of Lie,#,.."

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[eb246c21f6...](https://github.com/tgstation/tgstation/commit/eb246c21f6eb5380dc56e5779fcd51d11437557c)
#### Saturday 2023-11-18 13:48:40 by san7890

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
## [brian8181/streamy-cpp](https://github.com/brian8181/streamy-cpp)@[8bd69b9732...](https://github.com/brian8181/streamy-cpp/commit/8bd69b97320242a6975b48dc60bb27005d27696e)
#### Saturday 2023-11-18 14:07:38 by Brian K

just commiting this shit pile, what the holy fuck is going on here assholes ...

---
## [Party-Buddy/backend](https://github.com/Party-Buddy/backend)@[cfbf817a75...](https://github.com/Party-Buddy/backend/commit/cfbf817a7554d33326369546c527d4f56c6d490d)
#### Saturday 2023-11-18 14:12:26 by Alexander Yanin

wip: validate BaseMessage

I've decided to go with valgo after all, it being the least bad option
of those considered. If I had enough time, I'd have just made a brand
new parsing framework because absolutely everything I've seen is
a flaming bag of carcinogenic thermonuclear waste.

Like, you can't even tell it that all fields are required. All the other
languages I've used had that by default — you'd have to consciously tell
them that a field can be omitted, which is a perfectly sensible
behavior, except apparently in Go. I guess it's just not the Go way.
The Go way is to put EVERYTHING behind a pointer indirection because
heap is cheap and value semantics were invented by naive sophists who
never deal with the real world and for the likes of them. Stupid me,
I know. Whyever would I want to check if all fields are specified,
indeed. People don't need reasonable and actionable error messages,
why would they.

Oh, the error messages! That's a great one. You see, Decode() returns a
generic `error` instead of something specific. Well, it's just the
common convention because Go has those interface nils that aren't
actually nil, so if you don't want to lose your sanity over such a
trivial mistake, you'll just go with error even if you only ever return
a single concrete error type. Well, you can tell people what that type
is in the docs, at least.

Therefore json.Decoder() does not. I had to browse the source code to
see what errors it could return. This led me to find many unspoken
horrors, such as the fact that DisallowUnknownFields() returns an
*errors.errorString when that particular check is triggered, so you
can't detect that at all. Moreover, custom Unmarshal implementations can
just yeet whatever they want as an error.

You want to know any of the following about your particular error?
1. which field triggered it
2. whether it was due to invalid syntax, type mismatch, or semantic
   check failure
Well, guess what. You can't.

These errors are just like exceptions except much worse because you can
ignore them even if you don't mean to. I hate exceptions with a burning
passion, but I can't bring myself to hate Go errors lest I should turn
into a fuming volcano and make the whole world writhe in chemical
flames, and that's illegal.

I don't even want to mention — but as you can see I will nonetheless —
the fact that Decode() does not check for trailing junk at the end of
the input.  Whereas Unmarshal() does. But the latter also ignores
unknown fields provided in the input (why? and why is it the
default????). You can tell a custom Decoder you don't want that — great,
but now you can't do anything about the trailing junk! Except, I guess,
get the current scanner position in the input stream and compare that
against the input length. I remember C's strtol working like that, and
that was fine because it was C; but in Go this is a bit cringey.

...You see why I wanted to make my own parser framework yet?

And, uhm, sorry. For hijacking your commit log. Here, have a cookie: 🍪.

---
## [dundargoc/neovim](https://github.com/dundargoc/neovim)@[c9a69aff0b...](https://github.com/dundargoc/neovim/commit/c9a69aff0b00e701cfe44162c3ab91cfbfb9c835)
#### Saturday 2023-11-18 14:23:28 by dundargoc

fixup: burn in hell clint, hope you die a painful death

---
## [Implojin/crawl](https://github.com/Implojin/crawl)@[9676161fe1...](https://github.com/Implojin/crawl/commit/9676161fe14693c228fe4a55440a0b557540bf9e)
#### Saturday 2023-11-18 14:26:25 by yrdzrfxndfvh

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
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[7f0536bb93...](https://github.com/Ghommie/tgstation/commit/7f0536bb930a022d23d636619e4baf73661280a2)
#### Saturday 2023-11-18 14:46:14 by san7890

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
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[2562f0997a...](https://github.com/Ghommie/tgstation/commit/2562f0997a73a52c4ada51c7e0d9996fea4ee573)
#### Saturday 2023-11-18 14:46:14 by MrMelbert

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
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[742971675d...](https://github.com/Ghommie/tgstation/commit/742971675de266aa4ebe671dc5175a5c543d93d7)
#### Saturday 2023-11-18 14:46:14 by san7890

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
## [ayoubenezzi/Pig-Game](https://github.com/ayoubenezzi/Pig-Game)@[23ea5ece81...](https://github.com/ayoubenezzi/Pig-Game/commit/23ea5ece81e720b94ef896dc4a2f4839d979a1ef)
#### Saturday 2023-11-18 16:00:16 by Ayoub Benezzi

Update README.md


Certainly! Here's a description for your Pig Game project that you can use in your Git and GitHub repository:

🎲 Pig Game: Roll the Dice Adventure 🐷

Welcome to the "Pig Game," a thrilling two-player dice game where the stakes are high, and the dice are your destiny! This project, crafted with HTML, CSS, and JavaScript, brings the classic jeopardy of Pig to life in a digital playground.

🚀 Key Features:

Dynamic Gameplay: Immerse yourself in the excitement of a race to reach 100 points before your opponent.
Two-Player Fun: Challenge a friend in head-to-head competition, each taking turns to roll the dice and make strategic decisions.
Intuitive Design: The game features a user-friendly interface, making it easy for players of all levels to dive in and enjoy.
🎯 How to Play:

Roll the Dice: Click the "Roll Dice" button to unleash the power of chance.
Score or Risk: Decide whether to add your dice roll to your current score or risk it all for a potentially higher reward.
Watch Out for the Pig: Roll a '1,' and you lose all your points for that turn. The stakes are high; the choice is yours!
Reach 100 Points: Be the first player to reach or exceed 100 points to claim victory.
👾 Why I Built This:
The "Pig Game" is more than a digital recreation; it's a journey into the strategic and unpredictable world of dice gaming. This project reflects my passion for creating interactive and entertaining web experiences using fundamental web technologies.

---
## [kolyad3v/Discussr_that_finally_works](https://github.com/kolyad3v/Discussr_that_finally_works)@[6af15b637c...](https://github.com/kolyad3v/Discussr_that_finally_works/commit/6af15b637cefa99cce52b7654c8954f0319baf45)
#### Saturday 2023-11-18 16:27:50 by Nick

holy fucking shit, it's actually rendering the messages correctly

---
## [Mirag1993/mrdg](https://github.com/Mirag1993/mrdg)@[b58b3abe4f...](https://github.com/Mirag1993/mrdg/commit/b58b3abe4ffd26c63adb349f873ededfda5781a6)
#### Saturday 2023-11-18 17:44:54 by zevo

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
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[5b380921be...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/5b380921be658ddf46ed558472c007b885debf7a)
#### Saturday 2023-11-18 17:47:26 by Ron Nazarov

Make weapon oprops able to appear on more things

- Hell vaults can now generate weapon oprops on helms as well as gloves
  and boots.
- Lesser/greater cult oprops (lesser acid/drool for shubbie, lesser
  magic/window for yog) now stack, lesser oprops can be applied to
  artifacts, and both can be consistently applied to helms, gloves, and
  boots, as well as real weapons.
- Kukeri can now apply the holy armor oprop as well as the weapon
  oprop.  They will apply both where possible (armor oprop is applied to
  ARMOR_CLASS, weapon oprop is applied to is_weapon).
- There is now a somewhat misleadingly named is_weapon macro that
  actually means "weapon oprops can be applied to this", not "this is
  a weapon that should be wielded to use properly".  I'm not sure what
  a better name would be.
- Some sflame prop bugfixes:
-- Curse glaze now works (previously sflm_able would never return true
   for armor so it was broken).
-- RWTH, RBRD, and SLIF don't work on non-silver/mithril/platinum armor.
- Also fixes a completely unrelated typo ("Cut me lose, please!" ->
  "Cut me loose, please!").

---
## [p3rseph0ne/restaurant-guru](https://github.com/p3rseph0ne/restaurant-guru)@[f1b0e3d6c3...](https://github.com/p3rseph0ne/restaurant-guru/commit/f1b0e3d6c3923f80a6d11826e2da8801da177b15)
#### Saturday 2023-11-18 18:35:15 by p3rseph0ne

db connection works now, I also hate my life and have to add a new interface

---
## [vrglab/LowpEngine](https://github.com/vrglab/LowpEngine)@[1facbaf8d8...](https://github.com/vrglab/LowpEngine/commit/1facbaf8d8a3929f4326d4e1142011bdb68f030b)
#### Saturday 2023-11-18 18:45:44 by Vrglab

Just nearly fixed this stupid fucking shit head, it's driving  me fucking insane, why is a simple system linking in core but not inlauncher

---
## [vrglab/LowpEngine](https://github.com/vrglab/LowpEngine)@[00b4706cac...](https://github.com/vrglab/LowpEngine/commit/00b4706cac95d23e2fb363b2262f151a6caeeb34)
#### Saturday 2023-11-18 18:45:44 by Vrglab

Fuck this event system i swear to god if i shot myself in the legs it would be less painful

---
## [LSIS5425-Fall2023/group-7](https://github.com/LSIS5425-Fall2023/group-7)@[de54c64721...](https://github.com/LSIS5425-Fall2023/group-7/commit/de54c6472146c53af14333385b53fda0c8e1e542)
#### Saturday 2023-11-18 18:46:18 by jmarsic1

Create banned_books_01

The House of the Spirits, the unforgettable first novel that established Isabel Allende as one of the world’s most gifted storytellers, brings to life the triumphs and tragedies of three generations of the Trueba family. The patriarch Esteban is a volatile, proud man whose voracious pursuit of political power is tempered only by his love for his delicate wife Clara, a woman with a mystical connection to the spirit world. When their daughter Blanca embarks on a forbidden love affair in defiance of her implacable father, the result is an unexpected gift to Esteban: his adored granddaughter Alba, a beautiful and strong-willed child who will lead her family and her country into a revolutionary future.

---
## [y-ack/mame](https://github.com/y-ack/mame)@[6db28f4041...](https://github.com/y-ack/mame/commit/6db28f40416aa72a75128537e29b20985c26c75d)
#### Saturday 2023-11-18 19:01:51 by A-Noid33

New working software list items (mac - macii) 123 dumps (#11432)

* Initial softlist for mac moof 400/800 floppy disks

* Added mac moof software list support

New working software list items (123 working dumps)
-------------------------------
mac_flop_orig:

Lode Runner (version 1.0) [4AM, Anoid]
Balance of Power (version 1.03) [4AM, Anoid]
Shanghai (version 1.0) [4AM, Anoid]
Skyfox [4AM, Anoid]
Temple of Apshai Trilogy [4AM, Anoid]
The Surgeon (version 1.5) [4AM, Anoid]
Uninvited [4AM, Anoid]
King's Quest (version 1.10) [4AM, Anoid]
Smash Hit Racquetball (version 1.01) [4AM, Anoid]
The Ancient Art of War [4AM, Anoid]
Hacker II [4AM, Anoid]
Rambo: First Blood Part II [4AM, Anoid]
One on One [4AM, Anoid]
Indiana Jones and the Revenge of the Ancients [4AM, Anoid]
Winter Games (version 1985-10-24) [4AM, Anoid]
Winter Games (version 1985-10-31) [4AM, Anoid]
Star Trek: The Kobayashi Alternative (version 1.0) [4AM, Anoid]
Mac Attack [4AM, Anoid]
GATO (version 1.3) [4AM, Anoid]
Dark Castle (version 1.0) [4AM, Anoid]
Oids (version 1.4) [4AM, Anoid]
MacWars [4AM, Anoid]
Shadowgate [4AM, Anoid]
Seven Cities of Gold [4AM, Anoid]
Enchanted Scepters [4AM, Anoid]
Beyond Dark Castle [4AM, Anoid]
Arkanoid (version 1.00) [4AM, Anoid]
The Chessmaster 2000 (version 1.02) [4AM, Anoid]
Maze Survival [4AM, Anoid]
Frogger (version 1.0) [4AM, Anoid]
SimCity (version 1.2, black & white) [4AM, Anoid]
Falcon (version 1.0) [4AM, Anoid]
Cutthroats (release 23 / 840809-C) [4AM, Anoid]
The Witness (release 22 / 840924-C) [4AM, Anoid]
Seastalker (release 15 / 840522-C) [4AM, Anoid]
Zork III (release 17 / 840727-C) [4AM, Anoid]
A Mind Forever Voyaging (release 77 / 850814-E) [4AM, Anoid]
Hollywood Hijinx (release 37 / 861215-I) [4AM, Anoid]
Nord and Bert Couldn't Make Head or Tail of It (release 19 / 870722-I) [4AM, Anoid]
Border Zone (release 9 / 881008-3B) [4AM, Anoid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914) [4AM, Anoid]
Zork I: The Great Underground Empire (release 76 / 840509) [4AM, Anoid]
Deadline (release 27 / 831005-C) [4AM, Anoid]
Infidel (release 22 / 840522-C) [4AM, Anoid]
Suspect (release 14 / 841005-C) [4AM, Anoid]
Planetfall (release 29 / 840118-B) [4AM, Anoid]
Ballyhoo (release 97 / 851218-G) [4AM, Anoid]
Enchanter (release 24 / 851118-G) [4AM, Anoid]
Spellbreaker (release 63 / 850916-F) [4AM, Anoid]
Trinity (release 11 / 860509-3H) [4AM, Anoid]
Stationfall (release 107 / 870430-G) [4AM, Anoid]
The Lurking Horror (release 203 / 870506-G) [4AM, Anoid]
Alter Ego (male version 1.0) [4AM, Anoid]
Alter Ego (version 1.1 female) [4AM, Anoid]
The Print Shop (version 1.2) [4AM, Anoid]
Flight Simulator (version 1.02) [4AM, Anoid]
Run for the Money [4AM, Anoid]
Master Tracks Pro (version 4.0) [4AM, Anoid]
Where in Time is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Deluxe Music Construction Set (version 1.0) [4AM, Anoid]
Apache Strike (version 1.2) [4AM, Anoid]
Wizardry VI: Bane of the Cosmic Forge [4AM, Anoid]
Harrier Strike Mission [4AM, Anoid]
Airborne! [4AM, Anoid]
Mac Vegas (version 1.1) [4AM, Anoid]
Dragonworld [4AM, Anoid]
MacDraft (version 1.2) [4AM, Anoid]
The Mind Prober (version 1.0) [4AM, Anoid]
The Toy Shop (version 1.1) [4AM, Anoid]
Strategic Conquest (version 1.2) [4AM, Anoid]
The Home Accountant (version 1.01) [4AM, Anoid]
Sub Battle Simulator [4AM, Anoid]
Vegas Video Poker [4AM, Anoid]
The Pawn (version 2.3) [4AM, Anoid]
Downhill Racer [4AM, Anoid]
Dollars and Sense (version 1.3) [4AM, Anoid]
Alternate Reality: The City (version 3.0) [4AM, Anoid]
Borrowed Time [4AM, Anoid]
The Quest [4AM, Anoid]
The Crimson Crown [4AM, Anoid]
Mindshadow [4AM, Anoid]
Pensate (version 1.1) [4AM, Anoid]
Sierra Championship Boxing [4AM, Anoid]
Championship Star League Baseball [4AM, Anoid]
Forbidden Castle [4AM, Anoid]
Defender of the Crown [4AM, Anoid]
The King of Chicago [4AM, Anoid]
Macintosh Pascal (version 1.0) [4AM, Anoid]
Fusillade [4AM, Anoid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) [4AM, Anoid]
Speed Reader II (version 1.1) [4AM, Anoid]
][ in a Mac (version 2.03) [4AM, Anoid]
Q-Sheet (version 1.0) [4AM, Anoid]
Fontographer (version 2.4.1) [4AM, Anoid]
Mouse Stampede (version 1.00) [4AM, Anoid]
The Mist [4AM, Anoid]
Tass Times in Tonetown [4AM, Anoid]
Pinball Construction Set [4AM, Anoid]
Transylvania [4AM, Anoid]
Déjà Vu: A Nightmare Comes True!! [4AM, Anoid]
Déjà Vu II: Lost in Las Vegas!! [4AM, Anoid]
Rogue (version 1.0) [4AM, Anoid]
Bridge (version 6.0) [4AM, Anoid]
Harrier Strike Mission II (version 1.2) [4AM, Anoid]
Patton vs. Rommel (version 1.05) [4AM, Anoid]
Moebius: The Orb of Celestial Harmony (version 1.03) [4AM, Anoid]
Tesserae (version 1.06) [4AM, Anoid]
Where in Europe is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Shufflepuck Cafe (version 1.0) [4AM, Anoid]
Geometry (version 1.1) [4AM, Anoid]
Physics (version 1.2) [4AM, Anoid]
SimCity (version 1.1) [4AM, Anoid]
Murder by the Dozen [4AM, Anoid]
The Duel: Test Drive II [4AM, Anoid]
Master Tracks Pro (version 1.10) [4AM, Anoid]
Master Tracks Pro (version 2.00h) [4AM, Anoid]
Master Tracks Pro (version 3.4a) [4AM, Anoid]
Squire (version 1.1) [4AM, Anoid]
Millionaire (version 1.0) [4AM, Anoid]
Microsoft File (version 1.04) [4AM, Anoid]
Microsoft Excel (version 1.00) [4AM, Anoid]
The Fool's Errand (version 2.0) [4AM, Anoid]
MacGammon! (version 1.0) [4AM, Anoid]

---------

Co-authored-by: Bob Schultz <bobschultz03@gamil.com>

---
## [TheDarkElites/Foundation-19](https://github.com/TheDarkElites/Foundation-19)@[a666b103d3...](https://github.com/TheDarkElites/Foundation-19/commit/a666b103d3adcbcc9d954d05bad4e348f0d6ffaa)
#### Saturday 2023-11-18 19:01:54 by cheesePizza2

Fixes CDZ Medical Checkpoint windoors (#1386)

* changes

* fuck me

* fuck you

---
## [TheVampiric/anbubingobook](https://github.com/TheVampiric/anbubingobook)@[5ae5e94d01...](https://github.com/TheVampiric/anbubingobook/commit/5ae5e94d01e6a8284e6cad5bffca445efca7726f)
#### Saturday 2023-11-18 19:06:59 by bobzeus

strkoe

firstly, sorry you need to look at half the ugly shit i had to do

secondly i think images wasnt working before cuz we forgot to make both assets and data identical

thirdly, i have been trying to get naruto recipies to work for over 30 minutes now

im going for a cup of tea
-- Door (19:06 PM)

---
## [RuzzyTheFuzzy/GameJam2023](https://github.com/RuzzyTheFuzzy/GameJam2023)@[8f289135a0...](https://github.com/RuzzyTheFuzzy/GameJam2023/commit/8f289135a0c9266c4b9e7141a7ea1d54a83aece4)
#### Saturday 2023-11-18 19:08:57 by RuzzyTheFuzzy

FUCKIN GRIDSNAPPING ON PLATFORMS

I AM A GOD AND I KILLED THE OLD GOD AND ATE THEIR FLESH!!! YOU BOW TO ME NOW! PRAISE ME YOUR PROGRAMMING OVERLORD YOU SIMPLE MORTALS!!!

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[223dc74ef1...](https://github.com/shiptest-ss13/Shiptest/commit/223dc74ef1f528e2c29b0e62271ddaf7b68d79d8)
#### Saturday 2023-11-18 19:54:17 by retlaw34

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
## [ComposableFi/env](https://github.com/ComposableFi/env)@[a2d0625c43...](https://github.com/ComposableFi/env/commit/a2d0625c435e9905a2a921c70652d7c99b111d57)
#### Saturday 2023-11-18 20:00:36 by dzmitry-lahoda

ohoho

hoho

up

wtf

tf

fuck you

happy

work bitch

hoho

cleam up

happy

fun

oh

---
## [mwiencek/musicbrainz-server](https://github.com/mwiencek/musicbrainz-server)@[07a47c4ccc...](https://github.com/mwiencek/musicbrainz-server/commit/07a47c4ccc01d368cba0123344595de2266b3e5e)
#### Saturday 2023-11-18 20:59:06 by Michael Wiencek

MBS-13310: Add new empty artist credits to unreferenced_row_log

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
empty AC which had't been cleaned up yet.

---
## [kevinveenbirkenbach/computer-playbook](https://github.com/kevinveenbirkenbach/computer-playbook)@[9b82435a6d...](https://github.com/kevinveenbirkenbach/computer-playbook/commit/9b82435a6d705e25519e96987f9a48faf829d8e8)
#### Saturday 2023-11-18 21:15:10 by Kevin Veen-Birkenbach

Implemented hopefully the solution for the subs_filter method. Anyway I'm annoyed by this problem an will now clean up and go dacing. Enjoy your evening folks! :)

---
## [Lightmaxifrvr/LethalPlayers](https://github.com/Lightmaxifrvr/LethalPlayers)@[299f847263...](https://github.com/Lightmaxifrvr/LethalPlayers/commit/299f847263fe0c9a919574c19640f7d4a12ba0da)
#### Saturday 2023-11-18 21:25:48 by Lightmaxifrvr

why is this a fucking pain in the ass? also just recopied stuff back from BiggerLobbies

---
## [Loernius/crawl](https://github.com/Loernius/crawl)@[23a37c35b7...](https://github.com/Loernius/crawl/commit/23a37c35b79dbd581fed2f45b95338651489e7b7)
#### Saturday 2023-11-18 21:27:30 by Nicholas Feinberg

Rework the dreamshard necklace

Getting an extra life in a roguelike is an insanely, wildly strong
effect. This made the dreamshard necklace a ludicrously strong item,
but not one that made the game feel more exciting. Instead, one's
character felt a bit weaker most of the time.

Let's try to fix both sides of this. To make the amulet a bit more
fun to wear, give it Acrobat - good for running away :) To make it
less preposterously strong (and thus possible that a really good
unrand or randart amulet could be preferable), make it only restore
the player to 1 HP when it triggers (rather than 50-100% of MHP),
but guarantee that they won't die until their next turn. To simplify,
make it only trigger when the player's HP drops to 0, rather than
sometimes triggering on very big hits, and remove *Drain.

Finally, make it stick around as a normal amulet of the acrobat after
it triggers, for running away synergy.

Let's try this out.

---
## [K9100ii/android_hardware_samsung_slsi-linaro_graphics](https://github.com/K9100ii/android_hardware_samsung_slsi-linaro_graphics)@[81ee0c9d8a...](https://github.com/K9100ii/android_hardware_samsung_slsi-linaro_graphics/commit/81ee0c9d8a61d95781d13dac10ae4e6453587bbb)
#### Saturday 2023-11-18 21:32:07 by K9100ii

graphics: Switch to a new versioned path and BSP variant setting

and add soong namespacing.

Copy-paste explanation:

There are two sets of BSP sources - These new ones intended for Android
13, and older ones originally intended for Android 10. The older ones
have support for some legacy things like HWC1 for older devices, and
the newer ones have support for newer things like gralloc4.

To keep support for older devices going, I want to keep the older
sources alongside the newer ones. But they can't co-exist as-is. Some
changes are needed:
 - a change of paths to the BSP sources, which are referenced directly
   within them
 - a new BSP variant setting ('TARGET_SLSI_VARIANT' flag)
 - and finally, some soong namespacing.

The BSP variant setting and paths are the biggest challenge. For the
existing BSP sources, there's absolutely no versioning. It's the same
old generic "linaro"/"samsung_slsi-linaro" for both sets of BSP sources.
Sadly, my expressions of concern for my life to not be made more hellish
were quite badly dismissed, all the while I'd think it would be best
practice to version things like this to not keep using the same old
generic identifiers and not run into issues (or for others to not do so)
later, so I'm on my own to figure out what to do here.

My solution that touches the least I can is as follows:

For Android 13 - The older Android 10 BSP sources are typically used,
and since I'd like to use 13 sources as I have a device that requires
gralloc4, I need to make changes within them.
To manage it, the naming is as follows:
  Directory for 10 sources - 'samsung_slsi-linaro'
  Directory for 13 sources - 'samsung_slsi-linaro_13-e850-96'
  Git branch name for 10 sources - '...'
  Git branch name for 13 sources - '..._13-e850-96'
  SLSI variant flag setting for 10 sources - 'linaro'
  SLSI variant flag setting for 13 sources - 'linaro_13-e850-96'
The only changes here are for 13 sources. Naming is left untouched for
10 sources so as to not break anything for trees using them currently.

For Android 14+ - I'd want to preserve support for older devices, if
running newer Android versions doesn't become an impossibility for them,
so, while the newer Android 13 BSP sources are typically used, I'd have
to make changes to the 10 sources to keep them alongside.
To manage it, the naming will be as follows:
  Directory for 10 sources - 'samsung_slsi-linaro_10-e850-96'
  Directory for 13 sources - 'samsung_slsi-linaro'
  Git branch name for 10 sources - '..._10-e850-96'
  Git branch name for 13 sources - '..._13-e850-96'
  SLSI variant flag setting for 10 sources - 'linaro_10-e850-96'
  SLSI variant flag setting for 13 sources - 'linaro'
The directory and variant flag setting will be untouched for 13 sources,
so as to stay in line with everyone else, and changes would only need to
be made within 10 sources. However, for consistency, git branches will
all be versioned in future.

Lastly, soong namespacing is added specifically for the "exynos" and
"graphics" parts of the sources. Without, there are conflicts between
the two sets of sources. For all devices, BoardConfigCommon.mk in the
collection of BSP configs is included, and namespaces can be added
there, for a clean result where no changes are required in device trees
at all.

Change-Id: I79e77f9bff0d4a1595d5cc6fe72fbd17d2734373

---
## [KittyNoodle/Monkestation2.0](https://github.com/KittyNoodle/Monkestation2.0)@[1e9edd6a49...](https://github.com/KittyNoodle/Monkestation2.0/commit/1e9edd6a49665dc9ae5e857e72455961be4f8230)
#### Saturday 2023-11-18 22:19:49 by Kittynoodle

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
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[a1e46c5d31...](https://github.com/Ghommie/tgstation/commit/a1e46c5d31347887de95520eee31c00749379b9c)
#### Saturday 2023-11-18 22:19:56 by Jacquerel

Basic Guardians/Holoparasites (#79473)

## About The Pull Request

Fixes #79485
Fixes #77552

Converts Guardians (aka Holoparasites) into Basic Mobs.
Changes a bunch of their behaviours into actions or components which we
can reuse.
Replaces some verbs it would give to you and hide in the status panel
with action buttons that you may be able to find more quickly.

They _**should**_ work basically like they did before but a bit
smoother. It is not unlikely that I made some changes by accident or
just by changing framework though.

My one creative touch was adding random name suggestions.
The Wizard federation have a convention of naming their arcane spirit
guardians by combining a colour and a major arcana of the tarot. The
Syndicate of course won't truck with any of that mystical claptrap and
for their codenames use the much more sensible construction of a colour
and a gamepiece.

This lets you be randomly assigned such creative names as "Sparkling
Hermit", "Bloody Queen", "Blue World", or "Purple Diamond".
You can of course still ignore this entirely and type "The Brapmaster"
into the box if so desired.

I made _one_ other intentional change, which is to swap to Mothblocks'
nice leash component instead of instantly teleporting guardians back to
you when they are pulled out of the edge of their range. They should now
be "dragged" along behind you until they can't path, at which point they
will teleport. This should make the experience a bit less disorienting,
you have the recall button if you _want_ to instantly catch up.

This is unfortunately a bumper-sized PR because it did not seem
plausible to not do all of it at once, but I can make a project branch
for atomisation if people think this is too much of a pain in the ass to
review.

Other changes:
- Some refactoring to how the charge action works so I could
individually override "what you can hit" and "what happens when you hit"
instead of those being the same proc
- Lightning Guardian damage chain is now a component
- Explosive Guardian explosive trap is now a component
- Added even more arguments to the Healing Touch component to allow it
to heal tox/oxy damage and require a specific click modifier
- Life Link component which implements the Guardian behaviour of using
another mob as your health bar
- Moved some stuff about deciding what guardians look and are described
like into a theming datum
- Added a generic proc which can return whether your mob is meant to
apply some kind of damage multiplier to a certain damage type. It's not
perfect because I couldn't figure out how ot cram limb modifiers in
there, which is where most of it is on carbons. Oh well.
- Riders of vehicles now inherit all movement traits of those vehicles,
so riding a charging holoparasite will let you cross chasms. Also works
if you piggyback someone with wings, probably.

## Changelog

:cl:
refactor: Guardians/Powerminers/Holoparasites now use the basic mob
framework. Please report any unexpected changes or behaviour.
qol: The verbs used to communicate with, recall, or banish your Guardian
are now action buttons.
balance: If (as a Guardian) your host moves slightly out of range you
will now be dragged back into range if possible, rather than being
instantly teleported to them.
balance: Protectors now have a shorter leash range rather than a longer
one, in order to more easily take advantage of their ability to drag
their charge out of danger.
balance: Ranged Guardians can now hold down the mouse button to fire
automatically.
balance: People riding vehicles or other mobs now inherit all of their
movement traits, so riding a flying mob (or vehicle, if we have any of
those) will allow you to cross chasms and lava safely.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Tomsod/elemental](https://github.com/Tomsod/elemental)@[177715a611...](https://github.com/Tomsod/elemental/commit/177715a61189125367d6f8527d93fdd678f8f554)
#### Saturday 2023-11-18 22:42:14 by Tomsod M

Rehaul Armageddon, again

As of v3, my Armageddon nerfs got way out of hand and it became just a
worse version of Souldrinker.  Inspired by a discussion with Gray Magic
Expert on the forums, I'll try a more restrained approach this time.

Armageddon now mostly works like vanilla, except killed monsters award
no XP (since your party did virtually nothing), instead I added a call
to the code that handles fines and reputation hit for killing peasants.
This in turn makes the old rep hack unnecessary, so it's removed.

Furthermore, to nerf multi-day Armageddon camping (which is the only
really degenerate use of the spell), monsters on the current map heal
fully every full day you spend on it (unless you're in combat, then it's
delayed).  It's still possible to use two days' casting limit by
starting near 2 AM, but it's fine.  The spell once again affects the
entire map fully, and the casting limit is reduced to vanilla 3-4/day.

One quirk of the heal code is that unless you visit the moon temple
during the first day, all monsters on EI will be healed at midnight,
which is less than 24 hours since game start.  It's probably harmless.

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[7423345abc...](https://github.com/lessthnthree/effigy-se/commit/7423345abcd04302316b9fa7b13571f138367899)
#### Saturday 2023-11-18 22:47:03 by Andrew

Pipe painting, spraycan preset colors (#79521)

![dreamseeker_AZs0erdnrs](https://github.com/tgstation/tgstation/assets/3625094/06a12d22-387b-4a33-8b61-59bbe3495c82)

## About The Pull Request

Made pipe painter properly paint pipe colors, work on pipe items, and
added the same functionality to regular spraycans.

Spraycans now have the color presets in UI for easier selection of the
valid pipe colors.

## Why It's Good For The Game

Bug fixing is good.
It was weird that spraycans couldn't paint pipes, but some other device
could.
Also custom spraycan color is too clunky, presets are nice for quick
spraycan color selection.

## Changelog

:cl:
fix: fixed pipe painter not applying pipe color properly
qol: made spraycans work also as pipe painters
qol: spraycans now have basic color presets for quick selection
/:cl:

---

