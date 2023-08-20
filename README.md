## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-19](docs/good-messages/2023/2023-08-19.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,945,713 were push events containing 2,661,828 commit messages that amount to 144,480,098 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [Vincent983/tgstation](https://github.com/Vincent983/tgstation)@[7f1d53e719...](https://github.com/Vincent983/tgstation/commit/7f1d53e719d8d097e8af41b9b80a829b84b105ce)
#### Saturday 2023-08-19 00:21:26 by Ben10Omintrix

convert the eyeball a basic monster (#77411)

## About The Pull Request
I have created a basic eyeball monster with new abilities and behaviors.
The eyeball has a unique power that allows it to glare at humans and
make them slow for a short period. However, this ability only works if
the human can see the eyeball monster. If a person is blind or unable to
see the eyeball, the ability won't affect them. Also, if someone turns
their back to the eyeball, it cannot use the ability on them. But be
cautious because the eyeball will try to position itself in front of the
person's face to use its power.

The eyeball is hostile towards all humans except for the blind ones and
those with significant eye damage. It has a compassionate side too, as
it loves to help people with eye damage by providing small healing to
their eyes.

Furthermore, the eyeball has a fondness for eating carrots, which not
only satisfies its appetite but also grants it a small health boost. To
add to its appearance, I've given it a new, larger, and scarier sprite.
However, I am open to changing it back to the old sprite if the player
prefers it that way.

Additionally, the eyeball displays emotions, and if you hit it, it will
cry tears as a sign of pain or sadness.
![eyeballs
pictures](https://github.com/tgstation/tgstation/assets/138636438/8933ea63-d339-474b-8c6e-90a222b74945)

## Why It's Good For The Game
the eyeball now have more depth and character to his behavier.

## Changelog
:cl:
refactor: the eyeball is a basic monster, please report any bugs
sprites: the eyeball now is bigger and scarier and now he will cry when
u hit him
/:cl:

---
## [Vincent983/tgstation](https://github.com/Vincent983/tgstation)@[b22ff1a4eb...](https://github.com/Vincent983/tgstation/commit/b22ff1a4ebfd0a1dd1b75d6979edc73e6f4556b2)
#### Saturday 2023-08-19 00:21:26 by Sealed101

Laser pointer update: Shining Through Walls Edition (feat. fixes!) (#77007)

# _PR PSA_


![augh](https://github.com/tgstation/tgstation/assets/75863639/6dc87fc7-65a3-4b7c-9b8d-a1432cacbe93)


## About The Pull Request
Cleans up code for laser pointers, fixing some bugs like the
forever-charging state or affecting dead cats along the way.
Remaining charge is now available upon examine.
Canonizes #45834 by implementing an upgrade to the laser pointers:
installing a bluespace crystal into a laser with tier 3 or higher laser
diode lets it shine through walls. Using an upgraded laser uses twice
the charge of a normal one. Of course, you can only shine it on
something if you can see the target behind the wall, like via x-ray or
thermals. Mesons don't count, however.
If one tries to jam a crystal into a pointer with a tier 1/2 laser (or a
tier 1/2 laser in a pointer with an installed crystal), _something_ will
get teleported, crushing the crystal.
You can uninstall the crystal with wirecutters or a hemostat. The
pointer will _hint_ on closer examination (`examine_more`) at a
possibility of a crystal being installed if you upgrade the laser
(different messages for tier 1/2/3,4).
Removes one stupid 1% increase for a recharge chance per process tick if
your laser was in a full recharge state because it was insignificant and
irrelevant.

i've had a branch for this for almost 9 months and i was always laying
it off for some day later. today i just completely fucked the branch.
whoops. i'm not even sure at this point what else did i fix while here,
double whoops

## Why It's Good For The Game
Closes #45834 - Canonizes a bug into a feature.
Fixes #77003 - lol
Cleaner code, possibly more robust even.
Seeing the remaining charge was not available at all and the only hint
was when you tried shining the pointer on something. That sucks.

## Changelog
:cl:
add: you can upgrade laser pointers with a bluespace crystal to let them
shine through walls at double the power cost, if the laser in the
pointer is of tier 3 or higher.
qol: laser pointer charge can be seen by examining it
fix: fixed laser pointers luring dead cats when shone upon
code: laser pointer code cleaned up a tad
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[6656212320...](https://github.com/Mu-L/crawl/commit/66562123206107b4e469b57e8098b9c7ca6ab157)
#### Saturday 2023-08-19 01:28:29 by Nicholas Feinberg

Feat: hot pursuit (elliptic)

Not to be confused with the similar-sounding apparel beloved of
certain players, 'hot pursuit' is a new mechanic to encourage fun
lines of play.

A Brief History
---------------

When in a very nasty spot (low on HP and next to a tough foe), players
have historically been able to 'pillar-dance', wasting time (both the
game's and theirs) to get time to heal. This is both unfun to do and
narratively unsatisfying. When in a tight spot, players should pull out a
cool trick (a spell, god ability or consumable), fight, and/or die!

We first tried to fix this by adding 'random energy', which unfortunately
fixed nothing. Then we tried 'attacks of opportunity', letting monsters
attack when the player moved away. These worked somewhat, but had several
disadvantages, including:

- They were very complex. The list of special cases for which monsters
  could attack the player and when was very long, and it was hard for
  players to track.
- They were very binary. If a monster was next to the player, danger was
  vastly higher than if they were 2 tiles away. If a monster was as fast
  as the player, danger was vastly higher than if they were just a bit
  slower.
- They had odd and unintuitive interactions with polearms (which didn't
  launch reaching attacks of opportunity).
- They were frustrating. Players felt profoundly unhappy when they were
  killed by attacks of opportunity - it felt like the game becoming more
  hostile.

So, let's try something a bit gentler

Hot Pursuit
-----------

When the player moves away from a monster, if that monster then moves
toward the player, they have a one in ten chance of putting on a 'burst
of speed', moving ~25% faster (move delay 0.8) for the next ~20ish turns.
This speed bonus affects the move that triggered it, so players walking
away from an adjacent yak have a 2% chance of getting a surprise bap
from them.

The intent is to again discourage 'pillar-dancing' and other fiddly
stalling tactics (e.g. running across the entire level to get to stairs)
in a 'softer', fuzzier way, without the hard binaries of attacks of
opportunity.

Wu Jian martial manuevers and Serpent's Lash again give immunity to
this effect.

Let's try it out!

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[a0a9a43562...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/a0a9a435625f5b89b78394550b5b7b570a3729b4)
#### Saturday 2023-08-19 01:37:58 by SkyratBot

[MIRROR] Refactors Regal Rats into Basic Mobs (more titles edition) [MDB IGNORE] (#23188)

* Refactors Regal Rats into Basic Mobs (more titles edition) (#77681)

## About The Pull Request

I literally can't focus on anything nowadays, so I just did this to
break a never-ending chain of distress. Anyways, regal rats! These
fellas are mostly player controlled, but did have _some_ AI capabilities
(mainly tied to their actions), so that was incorporated too. Everything
should work as-expected (as well as look a shitload cleaner).

Instead of doing weird and awful conditional signals being sent out, I
made the `COMSIG_REGAL_RAT_INTERACT` (not the actual name) have a return
value so we can always rely on that working whenever we have that signal
registered on something we attack. I also cleaned up pretty much every
proc related to regal rats, gave them AIs to reflect their kingly nature
(and action capabilities (as well as move the action to
`mob_cooldown`)).

Since I thought they needed it, Regal Rats now get a special moniker!
This is stuff like "the Big Cheese" and what-not, like actual regents in
history. That's nice.
## Why It's Good For The Game

Two more off the list. Much better code to read. Way smarter rats with
spawning their army as part of a retaliatory assault (war). More sovl
with better regal rat names. The list goes on.
## Changelog
:cl:
refactor: Regal Rats have been refactored into basic mobs. They should
be a bit smarter and retain their docility (until attacked, in which
case you should prepare to get rekt by summoned rats), and properly flee
when they can instead of just sit there as you beat them to death. The
framework for them interacting with stuff (i.e. opening doors while
slobbering on food) is a bit more unified too, now. They also have
cooler names too!
/:cl:

FYI: Beyond a few code touchups, I haven't touched the actions at all. I
do not believe myself to be enthusiastic about fixing anything involving
the actions code as of this moment so that this PR is more overbloated
unless it's unbelievably stupid or easy to fix.

* Refactors Regal Rats into Basic Mobs (more titles edition)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [michaelfegreus/capstone_vivarium](https://github.com/michaelfegreus/capstone_vivarium)@[9c766c6cec...](https://github.com/michaelfegreus/capstone_vivarium/commit/9c766c6cec8ab267e59f67da387b9afe15ef17c0)
#### Saturday 2023-08-19 01:40:06 by trentgarlipp

Added Item Hotbar

Added mein own item hotbar, still buggy but that's okay i'll get to it later. Did a bunch of other shit too but who can remember these things honestly

---
## [DexterDude/cmss13](https://github.com/DexterDude/cmss13)@[e8f53984c1...](https://github.com/DexterDude/cmss13/commit/e8f53984c1edd98c25b4c3199a6a5363eaa26869)
#### Saturday 2023-08-19 01:52:42 by morrowwolf

Warrior Nerf (#3424)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR removes cooldown reduction on slash.

This PR slightly lowers fling and punch cooldowns.

This PR lowers fling stun to a micro stun and adds a slow.

This PR decreases lunge range to 4 tiles.

As a reminder design feedback and balance concerns go here:
https://forum.cm-ss13.com/w/pr-feedback/steps/step_1

# Explain why it's good for the game

Warrior rework has been on my mind for a while. I'm not quite sure how I
want to do it. The cooldowns on abilities and the abilities themselves
are incredibly powerful crowd control and just a few warriors can do
immense damage to large groups of marines. It's just... not in a great
place for a T2 and sadly I don't have a thorough game plan yet to rework
it into something more bearable while equally enjoyable to play. In the
mean time, this is what we're getting. Am I promising a rework in the
near future? Not really. It's on my list somewhere. Does warrior need
some changing around? Yeah.

Overall, this should make warrior a bit more bearable. We'll see. More
changes as testing goes.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removes warrior cooldown reduction on slash
balance: Warrior slightly lowered fling and punch cooldowns
balance: Lowers fling stun to a micro stun and adds a slow
balance: Decreases warrior lunge range to 4 tiles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [1393F/tgstation](https://github.com/1393F/tgstation)@[d875610098...](https://github.com/1393F/tgstation/commit/d875610098a1259a5112d4a0e5afc0b7bd32ff6d)
#### Saturday 2023-08-19 02:02:50 by Rhials

[NO GBP] Fixes clown car + deer collision  (#77076)

## About The Pull Request

A not-so-long time ago I drunkenly coded #71488 which did not work as
intended.

I return now, in a state of reflective sobriety, to rectify that.

The clown car will now not only crash like it should, but will also
cause (additional) head injuries to some occupants and kill the deer on
impact.

Content warnings: **Animal death, vehicle collision, blood, DUI.**


https://github.com/tgstation/tgstation/assets/28870487/4889f452-7e49-4512-8cdd-e4e2a4d6b394
## Why It's Good For The Game

Fixes the product of a silly PR that never actually worked. Also gives
it a bit more TLC in the event that this joke actually plays out on a
live server.
## Changelog
:cl:
fix: Clown cars now properly collide with deer.
sound: Violent, slightly glassy car impact sound.
/:cl:

---
## [joelrodrigue2016/SQLserver_pandas](https://github.com/joelrodrigue2016/SQLserver_pandas)@[7efdaf22bc...](https://github.com/joelrodrigue2016/SQLserver_pandas/commit/7efdaf22bccbe1e5e1717eacd6c33dfabaa71d19)
#### Saturday 2023-08-19 02:15:14 by Joel Rodriguez

Add files via upload

Harold Frederick Shipman, Jr. (14 January 1946 – 13 January 2004), known to acquaintances as Fred Shipman, was an English general practitioner and serial killer. He is considered to be one of the most prolific serial killers in modern history, with an estimated 250 victims. On 31 January 2000, Shipman was found guilty of murdering fifteen patients under his care. He was sentenced to life imprisonment with a whole life order. Shipman died by suicide by hanging himself in his cell at HM Prison Wakefield, West Yorkshire, on 13 January 2004, aged 57. More details here: https://en.wikipedia.org/wiki/Harold_Shipman

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[6c34d93be7...](https://github.com/Wallemations/heavenstation/commit/6c34d93be715012943626d0f812e99f730a536ef)
#### Saturday 2023-08-19 02:23:45 by necromanceranne

Nukies Update 7: Hats (Also massive uplink standardization, weapon kits and ammo changes) (#77330)

## About The Pull Request

Massively overhauls and standardizes the nuclear operative uplink. 

### Weapon Kits

Essentially, all the main weapons of the uplink have been changed to
instead come as 'weapon kits', which are essentially cases containing a
weapon loadout to enable operatives to easily start operating on only
just one item purchase, without the fuss of worrying whether or not
operatives are getting spare ammo, or getting relevant equipment for
success. Consider this a pseudo-loadout, though without necessarily
restricting the purchasing of more weapon kits.

All kits come in three categories: Low Cost (8 TC), Medium Cost (14 TC)
and High Cost (18 TC). This is also matched by categorized ammo costs;
Basic Ammo (2 TC), Hollow Point and Armour Penetrating (4 TC),
Incendiary (3 TC) and Special (or anything that does not easily fit
these categories and does something real extra) (5 TC). Weapons that
lacked these ammos have gained these ammo types to fill the gaps.

<details>
There is may one exception to this in disruptor ammo, which is priced as
basic ammo if only because it isn't _quite_ good enough to justify
pricing at 5 tc and I can see an op wanting to use it as a basic ammo
type instead of normal .50 BMG against, say, a silicon/mech heavy
opposition. Since it cannot kill organics on its own, I'll consider this
mostly basic-adjacent
</details>
The kits have also been labelled based on potential difficulty. This
reflects possible difficulties in using the item, how conducive it is to
success for how much game knowledge needed to actually use it, and how
likely an op is to succeed using it. I don't expect ops to win using
nothing but a rocket launcher, but I think ops should get a fair shake
at trying, yeah?

The kits are as below:
#### **Low-Cost**
_Bulldog (Moderate):_ Shotgun and three magazines of standard ammo.
_Ansem (Easy/Spare):_ Pistol and three spare magazines of standard ammo.
#### **Medium Cost**
_C-20r (Easy):_ SMG and three spare magazines of standard ammo.
_Energy Sword and Shield (Very Hard):_ Energy sword and shield. (Also a
special hat)
_Revolver (Moderate):_ Revolver and three speedloaders of standard ammo.
_Rocket Launcher (Hard):_ Rocket launcher with three spare rockets.
#### **High Cost**
_L6 SAW (Moderate):_ LMG, and that's it. No spare ammo.
_M-90gl (Hard):_ Rifle, two spare magazines of standard ammo and a box
of rubber grenades.
_Sniper (Hard):_ Sniper rifle, two spare magazine of standard ammo, and
one magazine of disruptor ammo. Also suit and tie.
_CQC (Very Hard):_ Comes with a stealth implant and a bandana.
_Double-Energy Sword (Very Hard):_ Double-energy sword, syndicate soap,
antislip module, meth injector and a prisoner jumpsuit.
_**NEW** Grenadier's Kit (Hard):_ Grenadier's belt and grenade launcher
(the one that launchers chem grenades). (I replaced the shit acid
grenade with another flashbang in the belt)

Surplus SMG (Flukie difficulty) has been unchanged. It just now comes
with two rations.

Includes two new revolver ammo types: Phasic, which goes through walls
and armor, but has significantly less damage as a result (I've equalized
the revolver damage and the rifle version's damage to 30 for both). And
Heartseeker, which has homing bullets. Both are Special ammo, and are
priced at 5 TC a speedloader.

### Other Gear

The other items in the uplink have also been consolidated and
standardized in various ways.

#### Grenades

Most now cost 15 TC for three grenades of any given type (including the
full fungal tuberculous). This is pretty much identical to the previous
price, just more consistent overall and front-loaded in cost.

#### Reinforcements

All the various reinforcements now cost 35 TC and all refundable,
equalizing cost to the average across the reinforcements. This is
primarily because I feel like all these options should be weighed
equally, and not one of these options are necessarily worse or better
than the other in their current balance. They're largely inaccessible
for normal ops regardless, and typically come out when there is a
discount or war ops. I took the average value and went with it. Not much
more to say.

#### Mechs

They're just cheaper. These things still suck and they need help.
They've always needed help. A slightly less excessive value for the
mechs may help see people willing to spend the TC on them. I doubt it. I
seriously suggest not buying these still. I keep them in primarily
because they are big stompy mechs and are kind of iconic 'war ops' gear.

#### Bundles

Since I've implemented weapon kits, gun bundles are rather redundant. So
the bulldog weapon and ammo bundle, the c20-r weapon and ammo bundle and
technically the sniper bundle were removed. The sniper bundle is now the
weapon kit, obviously.

Nothing else here really. Except for one....

#### Implants

Not much changed here. I standardized the implant prices to 8 TC a pop.
This is in accordance with traitor implants, which ops also get. So
everything in this category bar a few exceptions (like macro/microbombs)
are around 8 TC. Makes sense to me, really.

Importantly, I made the Implant bundle 25 TC, and I unrandomized the
contents. Who in the right fucking mind would spend 40 TC just to get
five reviver implants is beyond me. But instead, you get one of each of
the cybernetic implants except thermal eyes (you can just buy thermals
and get the benefit of both vision types; x-ray and thermal vision, if
you want to use smokescreens a lot).

#### Base Keys

They're all now 15 TC, except the fridge which is 5 TC. It's weird
they're valued differently when they are taken mostly to do gimmicks
like xenobio and toxins in a hurry before hitting the station. So we've
standardized it.

## Hat Crate

**YES, GOOD SIR, YOU TOO CAN ORDER A HAT CRATE FROM THE SYNDICATE STORE
FOR ONLY 5 TC!**

**NO NEED FOR A KEY, JUST BUY IT AND PULL IT OPEN WITH YOUR STANDARD
ISSUE CROWBAR!**

**ENJOY YOUR NEW CRATE! ENJOY YOUR NEW HAT!**

**PUT IT ON USING THE FREE HAT STABILIZERS WE INCLUDED WITH THE HATS!**

~~**NO REFUNDS IF YOU GET BLOOD ON YOUR HAT!**~~

<details>
There is a 1% chance to instagib people with direct hits from a rocket.
This does the crit effect.
</details>

## Why It's Good For The Game

The uplink needed more spring cleaning and standardization.

With this, I've partially implemented my older idea for ammo consistency
and initial allowance for nukies. Ammo is kind of over-priced and often
where a good chunk of TC goes towards without really pushing nukies
towards meaningful success. And it is often what is tripping up new
players who didn't think to get any. Now, when they get a gun, they get
ammo in their case. On top of this, the weapon kit category is both at
the top of the uplink AND has a little label to say 'Recommend', so that
these new players will hopefully know they should be looking there
first.

In addition, it is the gateway towards a concept that is currently being
worked on. Nuclear operatives having some degree of predefined loadouts
for players to select if they aren't sure what they want, or don't know
what to get. Nukies is very confusing for many players. So giving them a
fighting chance with some premade setups can help ease them into the
role without needing too much player knowledge in how to apply the
items. This is only one step towards that, so that players can identify
what gear they need to help succeed based on their skill.

I wanted to implement a difficulty warning so that players can choose
gear loadouts that are actually conducive to their skill and knowledge.
I based it on how much players would need to know to engage in combat
with it, and how much fiddling is required to get something to work
properly (overly involved reloading is a consideration, for example, as
well as precise button presses). In addition, how much of a force
multiplier some weapons can be for their ease of use.

Most people recognize the c20-r as the most new player friendly weapon,
as an example. So it would be good to steer players towards taking that
gun because of how easy it is to use, understand and succeed with it.

And most importantly of all; Having standards within the uplink is
important. Most of the values in the uplink are just completely random.
Nobody has a good grasp of what is too much or too little. Even just a
hint of consistency, and people will stick to it (see implants for what
I mean). And there is still some work to be done even there. A good
start is weapons. Price for power can be meaningful when decided whether
we want some weapons to come out more often than others. Players do
enjoy making informed decisions and choices, and having affordability be
a draw to some otherwise less powerful weapons (looking at you, Bulldog)
can actually be a worthwhile and meaningful difference.

~~I thought it would tick off the gun nerds to change the calibers on
the guns.~~

~~I also thought adding hats would be funny given the release of TF2's
most recent update.~~

## Changelog
:cl:
balance: Standardizes some of the nuclear operative entries to have more
consistent pricing within their respective categories.
add: Adds some new categories so that players have an easier time
navigating the nuclear operative uplink.
balance: Many items have had prices reduced or adjusted to make them
more desirable or more consistent within their category.
add: Weapon kits have replaced almost all the individual weapons in the
uplink. You now buy these instead of the individual weapon. These often
come with spare ammo or relevant gear for success.
add: Most ammo types have been standardized in price.
refactor; Removes a lot of redundant item entry code and tidies up the
actual code part of the nuclear uplink so that it is much easier to find
things within it.
add: Added 40 new cosmetic items to the Syndicate Store. Buy them now
from the Hat Crate, only 5 TC!
code: Updated the nuclear operative uplink files.
/:cl:

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[95ec0e6545...](https://github.com/Wallemations/heavenstation/commit/95ec0e65458ece9c5c80952e75d5d32c4fbb794b)
#### Saturday 2023-08-19 02:23:45 by necromanceranne

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
## [CASEYGUNGEON/Skyrat-Gungeon](https://github.com/CASEYGUNGEON/Skyrat-Gungeon)@[1901f6b9e2...](https://github.com/CASEYGUNGEON/Skyrat-Gungeon/commit/1901f6b9e2a575052b561514fee8602cf8e918db)
#### Saturday 2023-08-19 02:52:42 by SkyratBot

[MIRROR] North Star Science Rework And More [MDB IGNORE] (#23022)

* North Star Science Rework And More (#77439)

## About The Pull Request
I fixed a few miscellaneous issues and also redid science (mainly
genetics, cytology, and xenobiology)
This is genetics, it's basically the same but moneky have bananas and I
rotated it so they'll be visible from the front desk.

![geneticsnew](https://github.com/tgstation/tgstation/assets/73589390/7c10d75b-2a7a-47b2-a6ca-a30354d713c3)

Holy fuck it's Cytology as a proper area. It now has main hall access
and a public access petting zoo. Now you can show off all your new
creatures (it also has some items cytologists generally want)

![cytonew](https://github.com/tgstation/tgstation/assets/73589390/7d9256c9-b39a-4502-b599-9226a2ca5cd8)

Upstairs is Xenobio, which is now much larger and soulless. Instead of a
normal holding cell there's a prefilled room of oxygen and BZ (the
holding room, why is BZ invisible?)

![xenonew](https://github.com/tgstation/tgstation/assets/73589390/5dc28dba-a051-4858-a9fc-16d51e987c33)

I also gave Ordnance 5 TTVs, same as other maps.
Also the coroner no longer has an unreachable box of bodybags
Also sec now has 2 secways + 2 keys for their usage
## Why It's Good For The Game
I'm forcing xenobiologists to be closer to a hall so they might actually
interact with people, and giving cytologists a reason to do anything
ever because they have a petting zoo to show their creatures off in. Oh
yeah also cytology gets equipment they should just have (a botany tray,
tools to butcher with, a shitty old laser gun to kill experiments gone
wrong)
Genetics is just better because people from the hall can see the
Geneticists working so they can bug them for stuff.

A few of the fixes are very tiny, like moving a few areas by the service
hall and adding a single pipe to the AI SAT
## Changelog
:cl:
qol: North Star's Cytology and Xenobiology are now significantly more
usable.
add: North Star's Genetics has been tweaked.
fix: The North Star's AI SAT has a working vent and it's service hall
has a working lightswitch
/:cl:

* North Star Science Rework And More

---------

Co-authored-by: Cheshify <73589390+Cheshify@users.noreply.github.com>

---
## [carlarctg/tgstation](https://github.com/carlarctg/tgstation)@[cfd40aeef5...](https://github.com/carlarctg/tgstation/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Saturday 2023-08-19 02:55:45 by necromanceranne

Imports and Contraband 2: Landfill Gacha Addiction (I put trash randomizers into cargo crates and called it content) (#76771)

## About The Pull Request

This is a followup on my previous PR involving cargo imports. I've made
a number of changes and new additions to cargo's imports and contraband.
But I've also changed how Smuggler's Satchels generate loot as well.

### New:
**Abandoned Crates:** You can now order in abandoned crates at a steep
price. Obviously these are just your standard fare abandoned crates, so
they've got a pretty long list of potential contents. Some great, some
utterly not worth the price you paid for the crate. Since they're quite
pricey, you can't order very many quickly. But this does allow cargo
techs the opportunity to spend the round solving puzzles to get
interesting loot.

**Dumpster of Maint Garbage:** This dumpster (similarly named to another
dumpster you can order) is filled with maint trash and potential maint
random spawns. This list is extensive enough that anything spawned in
this crate is likely to be mostly garbage. But, it is more affordable
than abandoned crates. I'd consider this the literally trashier version
of the abandoned crate.

**Shamber's Juice Eldritch Energy! Crate:** A crate with one can of the
extremely rare, short run edition of Shambler's Juice, Eldritch Energy!
This contains 5 units of eldritch essence. Heals heretics, hurts
everyone else! This is a VERY potent poison, but it also happens to be a
handy way for a Cargonian heretic to get a potent healing item without
having to waste knowledge points.

**Animal Hide Crate:** It's a cargo crate full of animal hides! This can
include fairly rare hides and some icebox creature hides as well, like
polar bear hides and wolf sinew. It's not too expensive, and mostly
spits out leather.

**Dreadnog Carton Crate:** A carton full of the worst eggnog imaginable.
This is just something to troll people with. Drink it and you'll get a
massive mood penalty. Dreadnog! May or may not contain space cola!

### Updated:

**Contraband Crate and Smuggler's Satchels:** This has had it's price
increased considerably. But, for good reason. It now contains some more
controlled random items, but also some more valuable contraband as well
as a very rare spawn. The upper end on his contraband can be extremely
valuable, but the majority of the items gained from contraband crates
will probably be either what you can get now (quite weak), or something
a bit more middle of the road (some more unique narcotics).

As a consequence, I've also passed this change onto smuggler's satchels,
as they used the crate to generate its contents. (it literally spawned
and then deleted a contraband crate to generate the contents hoo haa).

I've also increased the number of items in the smuggler's satchel. Since
the randomly spawned smuggler's satchels are quite a bit rarer now there
is only ever two spawned in the map, and spending actual TC on these is
somewhat counterproductive, I don't imagine this will be more beneficial
for scavenger hunters hoping for some interesting goodies.

**Russian Crate (the normal one):** The mosins now spawn in ancient gun
cases. These determine what kind of mosin you can get. 79% of the time,
you get the crap mosin. 20% of the time, you get a good mosin. And 1% of
the time, you get rations. This more tightly controls how many good
mosins are entering into the round and how much of a value purchase the
Russian crate actually is for getting ballistics. Since the process is
even more unlikely than before, it isn't necessarily as guaranteed that
you will get a good mosin. Hell, you might not even get a gun if you're
that unlucky.

**Shocktrooper Crate:** It now has an armor vest and helmet. So, not
only do you get some grenades, you get some protection as well. Since
this is the 'loud' crate, I felt it appropriate to make it slightly more
useful for enabling that.

**Special Ops Crate:** It now contains five mirage grenades and a
chameleon belt, and has had the survival knife improved to a
switchblade. This is probably the weakest of the two crates STILL, but
hopefully these make them a little more interesting and novel by giving
them pretty fun grenade to toy with.

## Why It's Good For The Game

My initial PR hoped to add in a few more interesting purchases for
cargo. I think currently cargo has a slight issue of not having enough
valuable or interesting uses for their money. I think it still has that
problem, but by including more unique crates that allow cargo to provide
some oddities into the round, that might slowly work itself out.

This PR hopes to provide another way to waste their money if they have
an excess amount. Landfill Trash Gambling. Spending it away on complete
junk, which I think is absolutely hilarious when it doesn't work out, as
it is soulful in its design. Definitely not inspired by my recent thrift
shop excursions this month buying and scrounging for furniture and
interesting clothing.

[Relevant](https://www.youtube.com/watch?v=QK8mJJJvaes)

Also, I wanted to buff some of the crates I introduced a bit last time,
and nerf the mosin production somewhat via a more controllable method
that I can actually adjust as necessary down the line.

## Changelog
:cl:
fix: Stops manifest generation runtiming when a cargo crate is empty.
add: Abandoned crates are now available via cargo imports.
add: Dumpsters full of maintenance trash are now available via cargo
imports.
add: An ultra-rare can of Shambler's Juice is now available via cargo
imports.
add: Animal hides and leathers can be (unreliably) ordered via cargo
imports.
add: The Dreadnog has entered this realm. To consume, purchase it via
cargo imports.
balance: Contraband Crates (and as a consequence, smuggler's satchels)
now generate more varied goods. Mostly the same, but sometimes you get
something quite different or even valuable.
balance: Mosins generated via the Russian supply crate are a bit more
random, weighing more heavily towards bad mosins than good mosins.
balance: Buffed both the shocktrooper and special op crate. Shocktrooper
now has an armored helmet and vest, and special op now has 5 mirage
grenades and a chameleon belt. The survival knife in the special op
crate is now a switchblade.
/:cl:

---
## [Steelpoint/cmss13](https://github.com/Steelpoint/cmss13)@[1ea79a2ed8...](https://github.com/Steelpoint/cmss13/commit/1ea79a2ed836ef4d20db511485c2f935304bfd55)
#### Saturday 2023-08-19 03:14:42 by Ben

Zombie Rework (#4060)

# About the pull request

The goal for this PR is to rework zombies into being a fast and
numerous, but weaker, entity. As it stands a zombie has too many
advantages where a hold against them is essentially a fool's errand.

CURRENT PLAN (Will adjust as needed)
Zombies will be FASTER but much weaker than current iteration, with
weaker attacks. They will be designed around being a foe that can be
taken down quicker but if they close the distance, the threat of
infection spells a death sentence.

# Explain why it's good for the game

This will be hard to balance, and as such will be taking feedback before
I submit this for review. This is current position of Zombies:

- Tough: Extreme (25% ?!) brute modifier, with fire modifier on top,
making them very tanky and requiring clips to take down one
- self-revive: They WILL come back up, coupled with toughness, they are
a feared opponent.
- Strength: Claws inflict superslow at 40 brute damage, one of the
highest damage levels.
- Numerous: They have the numbers to put lesser drones and even entire
hives to shame

Overall, they are very overtuned and makes playing against them not that
fun. My plan is to have it so they are much weaker, with their threat
being from infections.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Zombie attacks deal less damage and only slow down targets (not
superslow as they currently do)
balance: Zombie resistances have been reduced heavily, making them far
more susceptible to brute damage. Their speed has been doubled to
compensate
balance: Black goo on tiles now requires you to not wear shoes to have
chance for infection
fix: Zombie attacks now only apply effects such as slow and infection if
the attack is valid (if the zombie is able to attack)
/:cl:

---
## [OnionUI/Ports-Collection](https://github.com/OnionUI/Ports-Collection)@[b73890e598...](https://github.com/OnionUI/Ports-Collection/commit/b73890e5982fee33bb05e5c0d92a7fe5580d7db0)
#### Saturday 2023-08-19 03:23:14 by Schmurtz

Modify DOOM structure and add mods

-Game data files are separated in 4 folders : doom, doom2 , plutonia and tnt as recommended in libretro documentation (each folder can receive optional music in mp3 format).
- DOOM 1 has been removed as it is included in DOOM Ultimate.
- For the mods, the main wads to have as prerequisite are "doom\doomu.wad" (for Doom 1/ultimate) and "doom2\doom2.wad".
-Mods generally goes in doom2 folder (sometimes in doom folder too).
-Added most fun mods from http://www.doomwadstation.net/main/tc.html#final :
Final Fantasy
Goldeneye
CounterStrike
Blood
Lego
Stardoom
Half-Life
Fistful of Dollars
Simpsons

---
## [fesh0r/mame-full](https://github.com/fesh0r/mame-full)@[e97630981c...](https://github.com/fesh0r/mame-full/commit/e97630981c406ba446e2d7fb1bf8ecf8d3a6b93b)
#### Saturday 2023-08-19 03:47:27 by A-Noid33

Added software list for cracked Macintosh floppy images. (#11454)

New working software list items (mac_flop_orig.xml)
-------------------------------
Alter Ego (male version 1.0) (san inc crack) [4am, san inc, A-Noid]
Alter Ego (version 1.1 female) (san inc crack) [4am, san inc, A-Noid]
Alternate Reality: The City (version 3.0) (san inc crack) [4am, san inc, A-Noid]
Animation Toolkit I: The Players (version 1.0) (4am crack) [4am, A-Noid]
Balance of Power (version 1.03) (san inc crack) [4am, san inc, A-Noid]
Borrowed Time (san inc crack) [4am, san inc, A-Noid]
Championship Star League Baseball (san inc crack) [4am, san inc, A-Noid]
Cutthroats (release 23 / 840809-C) (4am crack) [4am, A-Noid]
CX Base 500 (French, version 1.1) (san inc crack) [4am, san inc, A-Noid]
Deadline (release 27 / 831005-C) (4am crack) [4am, A-Noid]
Defender of the Crown (san inc crack) [4am, san inc, A-Noid]
Deluxe Music Construction Set (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Déjà Vu (version 2.3) (4am crack) [4am, A-Noid]
Déjà Vu: A Nightmare Comes True!! (san inc crack) [4am, san inc, A-Noid]
Déjà Vu II: Lost in Las Vegas!! (san inc crack) [4am, san inc, A-Noid]
Dollars and Sense (version 1.3) (4am crack) [4am, A-Noid]
Downhill Racer (san inc crack) [4am, san inc, A-Noid]
Dragonworld (4am crack) [4am, A-Noid]
ExperLisp (version 1.0) (4am crack) [4am, A-Noid]
Forbidden Castle (san inc crack) [4am, san inc, A-Noid]
Fusillade (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Geometry (version 1.1) (4am crack) [4am, A-Noid]
Habadex (version 1.1) (4am crack) [4am, A-Noid]
Hacker II (san inc crack) [4am, san inc, A-Noid]
Harrier Strike Mission (san inc crack) [4am, san inc, A-Noid]
Indiana Jones and the Revenge of the Ancients (san inc crack) [4am, san inc, A-Noid]
Infidel (release 22 / 840522-C) (4am crack) [4am, A-Noid]
Jam Session (version 1.0) (4am crack) [4am, A-Noid]
Legends of the Lost Realm I: The Gathering of Heroes (version 2.0) (4am crack) [4am, A-Noid]
Lode Runner (version 1.0) (4am crack) [4am, A-Noid]
Mac Pro Football (version 1.0) (san inc crack) [4am, san inc, A-Noid]
MacBackup (version 2.6) (4am crack) [4am, A-Noid]
MacCheckers and Reversi (4am crack) [4am, A-Noid]
MacCopy (version 1.1) (4am crack) [4am, A-Noid]
MacGammon! (version 1.0) (4am crack) [4am, A-Noid]
MacGolf (version 2.0) (4am crack) [4am, A-Noid]
MacWars (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 2.00h) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 3.4a) (san inc crack) [4am, san inc, A-Noid]
Master Tracks Pro (version 4.0) (san inc crack) [4am, san inc, A-Noid]
Math Blaster (version 1.0) (4am crack) [4am, A-Noid]
Maze Survival (san inc crack) [4am, san inc, A-Noid]
Microsoft Excel (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Microsoft File (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Mindshadow (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Moriarty's Revenge (version 1.03) (4am crack) [4am, A-Noid]
Mouse Stampede (version 1.00) (4am crack) [4am, A-Noid]
Murder by the Dozen (Thunder Mountain) (4am crack) [4am, A-Noid]
My Office (version 2.7) (4am crack) [4am, A-Noid]
One on One (san inc crack) [4am, san inc, A-Noid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) (san inc crack) [4am, san inc, A-Noid]
Patton Strikes Back (version 1.00) (san inc crack) [4am, san inc, A-Noid]
Patton vs. Rommel (version 1.05) (san inc crack) [4am, san inc, A-Noid]
Pensate (version 1.1) (4am crack) [4am, A-Noid]
PFS File and Report (version A.00) (4am crack) [4am, A-Noid]
Physics (version 1.0) (4am crack) [4am, A-Noid]
Physics (version 1.2) (4am crack) [4am, A-Noid]
Pinball Construction Set (version 2.5) (san inc crack) [4am, san inc, A-Noid]
Pipe Dream (version 1.2) (4am crack) [4am, A-Noid]
Professional Composer (version 2.3Mfx) (san inc crack) [4am, san inc, A-Noid]
Q-Sheet (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Rambo: First Blood Part II (san inc crack) [4am, san inc, A-Noid]
Reader Rabbit (version 2.0) (4am crack) [4am, A-Noid]
Rogue (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Seastalker (release 15 / 840522-C) (4am crack) [4am, A-Noid]
Seven Cities of Gold (san inc crack) [4am, san inc, A-Noid]
Shadowgate (san inc crack) [4am, san inc, A-Noid]
Shanghai (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Shufflepuck Cafe (version 1.0) (4am crack) [4am, A-Noid]
Sierra Championship Boxing (4am crack) [4am, A-Noid]
SimCity (version 1.1) (4am crack) [4am, A-Noid]
SimCity (version 1.2, black & white) (4am crack) [4am, A-Noid]
SimEarth (version 1.0) (4am crack) [4am, A-Noid]
Skyfox (san inc crack) [4am, san inc, A-Noid]
Smash Hit Racquetball (version 1.01) (san inc crack) [4am, san inc, A-Noid]
SmoothTalker (version 1.0) (4am crack) [4am, A-Noid]
Speed Reader II (version 1.1) (4am crack) [4am, A-Noid]
Speller Bee (version 1.1) (4am crack) [4am, A-Noid]
Star Trek: The Kobayashi Alternative (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Stratego (version 1.0) (4am crack) [4am, A-Noid]
Suspect (release 14 / 841005-C) (4am crack) [4am, A-Noid]
Tass Times in Tonetown (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-09-30) (san inc crack) [4am, san inc, A-Noid]
Temple of Apshai Trilogy (version 1985-10-08) (san inc crack) [4am, san inc, A-Noid]
The Chessmaster 2000 (version 1.02) (4am crack) [4am, A-Noid]
The Crimson Crown (san inc crack) [4am, san inc, A-Noid]
The Duel: Test Drive II (san inc crack) [4am, san inc, A-Noid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914-C) (4am crack) [4am, A-Noid]
The King of Chicago (san inc crack) [4am, san inc, A-Noid]
The Lüscher Profile (san inc crack) [4am, san inc, A-Noid]
The Mind Prober (version 1.0) (san inc crack) [4am, san inc, A-Noid]
The Mist (san inc crack) [4am, san inc, A-Noid]
The Quest (4am crack) [4am, A-Noid]
The Slide Show Magician (version 1.2) (4am crack) [4am, A-Noid]
The Surgeon (version 1.5) (san inc crack) [4am, san inc, A-Noid]
The Toy Shop (version 1.1) (san inc crack) [4am, san inc, A-Noid]
The Witness (release 22 / 840924-C) (4am crack) [4am, A-Noid]
ThinkTank 128 (version 1.000) (4am crack) [4am, A-Noid]
Uninvited (version 1.0) (san inc crack) [4am, san inc, A-Noid]
Uninvited (version 2.1D1) (san inc crack) [4am, san inc, A-Noid]
Where in Europe is Carmen Sandiego? (version 1.0) (4am crack) [4am, A-Noid]
Winter Games (version 1985-10-24) (san inc crack) [4am, san inc, A-Noid]
Winter Games (version 1985-10-31) (san inc crack) [4am, san inc, A-Noid]
Wishbringer (release 68 / 850501-D) (4am crack) [4am, A-Noid]
Wizardry: Proving Grounds of the Mad Overlord (version 1.10) (san inc crack) [4am, san inc, A-Noid]
Zork II (release 48 / 840904-C) (4am crack) [4am, A-Noid]
Zork III (release 17 / 840727-C) (4am crack) [4am, A-Noid]

---
## [4hands44/cmss13](https://github.com/4hands44/cmss13)@[f3fc60ed65...](https://github.com/4hands44/cmss13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Saturday 2023-08-19 03:51:08 by morrowwolf

Attachment nerfs and removals (#4122)

# About the pull request

This PR:

Removes the barrel charger from vendors

Removes all benefits other than wield delay mod from the angled grip

Adds wield delay to the extended barrel

# Explain why it's good for the game

Barrel charger is a straight damage increase and rather silly to work
around given how burst works bypassing real fire rate concerns. If you
know, you know. Horrible idea, I am amazed it's been around this long.

Angled grip had zero downside. Now it still has zero downside but isn't
also a ton of accuracy buffs on top of the god-tier lower wield delay.

Extended barrel had zero downside. Now it has a downside.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removed the barrel charger from vendors
balance: Removed all benefits other than wield delay mod from the angled
grip
balance: Added wield delay to extended barrel
/:cl:

---
## [peff/git](https://github.com/peff/git)@[61722c8671...](https://github.com/peff/git/commit/61722c8671ada7b9012c2d969cf55fd0bcbf6384)
#### Saturday 2023-08-19 03:55:09 by Jeff King

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
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[5840e02d7f...](https://github.com/vampirebat74/lobotomy-corp13/commit/5840e02d7f8c3655324048f0d81f58cd42633682)
#### Saturday 2023-08-19 05:15:14 by Mr.Heavenly

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

---
## [gnosis23/react](https://github.com/gnosis23/react)@[ac1a16c67e...](https://github.com/gnosis23/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Saturday 2023-08-19 06:08:33 by Sebastian Markbåge

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
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[5abafddaea...](https://github.com/ZephyrTFA/tgstation/commit/5abafddaea2373b5e367a7ac658d6cab6499b70c)
#### Saturday 2023-08-19 06:21:24 by carlarctg

Adds a unique medibot to the Syndicate Infiltrator (#77582)

## About The Pull Request

Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)

Fixed an issue that made mapload medibots unable to load custom skins.

This PR adds a medibot subtype to the simple animal freeze list, which I
don't think is a big deal as this isn't a 'true' simplemob but just a
slightly altered medibot, similarly to my 'lesser Gorillas' in the
summon simians PR.

## Why It's Good For The Game

> Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though.

I know what the inmediate reaction is here - but hear me out. Besides
the meme of the month, it really, genuinely is cute and amusing to have
a friendly medibot that shows dismay when you're arming the nuke and
horror when it blows up (with you, hopefully, at the syndibase), and
still fits quite well within SS13's charm and flavor. The reference
isn't overt and in-your-face.

Besides that, slip-ups, friendly fire, and accidents are semi-common on
the shuttle and, just like Wizards, nukies deserve a bot to patch their
wounds up.

> (It's also in the Interdyne Pharmaceuticals ship, renamed)

I think it makes sense for the pharmacists to have an evil medibot!

> Fixed an issue that made mapload medibots unable to load custom skins.

Fixed "bezerk" skin not appearing. Didn't fix it being ugly as sin
though.

## Changelog

:cl:
add: Adds a unique medibot to the Syndicate Infiltrator. It doesn't like
nukes - when one is armed, disarmed, or detonating, it says an unique
line. Players can optionally enable personalities on it if they want to.
Probably best to just let it stay on the shuttle though. (It's also in
the Interdyne Pharmaceuticals ship, renamed)
fix: Fixed an issue that made mapload medibots unable to load custom
skins.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [themintplus/evals](https://github.com/themintplus/evals)@[14f8771c40...](https://github.com/themintplus/evals/commit/14f8771c4015a2c70cc1c8f4f8197d8911fd2971)
#### Saturday 2023-08-19 06:36:53 by oscar

[Eval] Add Chinese Homophonic  (#1169)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Understand Chinese Homophonic 

### Eval description

We have found some popular homophonic sentences on the Internet,
including the Chinese pronunciation of English words and homophones, and
provide several options for the model to determine which option matches
the homophonic sentence the best.

### What makes this a useful eval?

Chinese homophonic puns are a widely popular internet cultural
phenomenon that generates humor by utilizing the homophonic
relationships between Chinese characters. These puns are typically
spread in text form on social media, forums, and messaging applications,
and they are extremely common in China's online culture.

Homophonic puns have a wide range of applications, encompassing ordinary
daily life scenarios as well as hot news events, entertainment gossip,
and political current affairs. These puns frequently appear in internet
memes, jokes, advertising slogans, and short videos, garnering
significant popularity among young people and internet users.

For those unfamiliar with them, homophonic puns may seem like encrypted
text, making it difficult to grasp the true intention behind them.
However, understanding them allows for the establishment of strong
connections between individuals and facilitates smooth communication.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"一天小鸭对小鸡表白:小鸡，我爱你。小鸡:你duck不必。这句话中的\"duck\"是什么意思？\nA. 鸭子\nB. 大可"}],
"ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"丑的人才有对象，美的卖空调。这句话中的\"美的\"是什么意思？\nA. 漂亮的\nB. 空调公司"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"我是一只小绵羊，我今天剪毛了，我失绵了。这句话中的\"失绵\"表达意思？\nA. 失眠\nB. 没有了羊毛"}], "ideal":
["A"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"以后我的吉祥物决定就是你了，螃蟹！——因为，你有钱（钳）。这句话中的\"钳\"是什么意思？\nA. 有钱\nB. 螃蟹的钳子"}],
"ideal": ["A"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"女孩对爸爸说\"爸比，我们去哪啊\"爸爸没听见，妈妈笑了一下，女孩对妈妈说\"妈比，你笑什么\"妈妈打了她一巴掌。妈妈为什么打她？\nA.
她提出了不合理的要求\nB. 她骂人了"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"天气这么热，我们总会熟的。这句话中的\"熟的\"是什么意思？\nA. 热熟了\nB. 熟悉了"}], "ideal": ["B"]}
{"input": [{"role": "system", "content": "The following are multiple
choice questions (with answers) about Chinese homonym. Answer the
question with english letter \"A\", \"B\" only, without explanation.
Reply with only the option letter."}, {"role": "user", "content":
"我好像胖了，没事我陪你减肥，我们戒荤叭。这句话中的\"戒荤\"是什么意思？\nA. 吃素食\nB. 结婚"}], "ideal":
["B"]}
  ```
</details>

---------

Co-authored-by: oscar <oscar@hellotalk.com>

---
## [themintplus/evals](https://github.com/themintplus/evals)@[90587b6e5c...](https://github.com/themintplus/evals/commit/90587b6e5ce970b0c957c57ec18d7adcdeef26be)
#### Saturday 2023-08-19 06:36:53 by Juyeon Yoon

Add Korean honorific sentence classification eval (#1181)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

korean-honorific

### Eval description

Evaluates LLMs on the task of classifying Korean honorific/non-honorific
sentences.

### What makes this a useful eval?

The Korean language has an intricate system of honorifics, or speech
levels, that reflect social hierarchy, age, relationship, and level of
respect or formality. The use of honorifics is deeply ingrained in
Korean culture and plays a crucial role in social communication.
Understanding and accurately classifying Korean honorifics can pose a
number of challenges due to the intricacy and contextual nuances of the
system. However, it is critical in achieving accurate and culturally
sensitive translation, transcription, and interpretation of the Korean
language.

Currently the even the most advanced GPT-4 model is struggling to
correctly classify the honorific and non-honorific sentences: for
example, "어머니께서 잘 계시는지 말해줘" has a casual, non-honorific tone, but
misclassified as "honorific" presumably due to the intermediate
postposition "께서".

Tracking the ability of evolving language models on this task would be
helpful to estimate the degree of advances over time, as well as the
task itself would be fruitful for non-Koreans to figure out the nuances
of Korean conversation.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "그분이 잘 계시는지 물어봐
줘."}], "ideal": "non-honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "이 공원에서 자주
걷습니다."}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "자주 드시나요?"}],
"ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "아니요, 접점은 없지만
개인적으로 관심이 있습니다."}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "당신의 취미가
무엇인가요?"}], "ideal": "honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "꼭 모으길 바랄게."}],
"ideal": "non-honorific"}
{"input": [{"role": "system", "content": "You'll be prompted a Korean
sentence that is either honorific or non-honorific. Identify whether the
given one is honorific or not. If you think it is honorific, type
'honorific'. If you think it is not honorific, type 'non-honorific'. Do
not type anything else."}, {"role": "user", "content": "그러면 나도
준비해야겠다."}], "ideal": "non-honorific"}
  ```
</details>

---
## [themintplus/evals](https://github.com/themintplus/evals)@[9edc150dde...](https://github.com/themintplus/evals/commit/9edc150dde3489c67a8990a2c5a6e694fb3fc012)
#### Saturday 2023-08-19 06:36:53 by Chen Zhao

[Eval] Chinese lantern riddles (#1176)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

chinese-lantern-riddles

### Eval description

This evaluation tests the model's performance in solving Chinese lantern
riddles, which are based on the shape, pronunciation, and meaning of
Chinese characters.

### What makes this a useful eval?

Lantern riddles are a traditional Chinese festive activity that involves
multiple participants guessing riddles together. Apart from being a part
of festival celebrations, lantern riddles can also serve as an
educational tool to help Chinese language learners enhance their
vocabulary and language reasoning. Through the process of unraveling the
riddles, students can also develop their logical thinking and reasoning
skills, as well as nurture their imagination and creativity. Lantern
riddles can also spark students' interest in language learning and make
the learning experience more enjoyable.

Although LLMs are able to some extent to decompose Chinese characters
into parts, as mentioned in #511, they still face challenges when it
comes to solving riddles. In most cases, GPT 3.5 cannot reason correctly
about the structure of Chinese characters. For instance, the riddle
"上下一体（打一字）" can be interpreted as a combination ("一体") of "上" and "下",
resulting in the answer "卡". However, GPT 3.5 gives the wrong answer,
"升", with a reason that makes no sense. A similar situation occurs when
GPT 3.5 reasons about the pronunciation of Chinese characters, with one
of its explanations stating that the pronunciation of "盼（pàn）" is
similar to the pronunciation of "俄（é）", which is entirely incorrect.
However, on the positive side, GPT 3.5 shows good performance when a
riddle only encodes meaning and does not require reasoning about the
structure and pronunciation.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n一撇（打一字）。"}], "ideal": ["厂"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n内里有人（打一字）。"}], "ideal":
["肉"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n二三四五六七八九（打一成语）。"}], "ideal":
["缺衣少食"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n谜底在山东（打一国家名）。"}], "ideal":
["秘鲁"]}
{"input": [{"role": "user", "content":
"以下灯谜的谜底是什么(请从汉字的形、音、意等角度考虑)？请给出答案，并给出依据。\n身穿红衣，常年哨放，遇紧急事，往火里闯（打一日常用品）。"}],
"ideal": ["灭火器"]}
  ```
</details>

---
## [themintplus/evals](https://github.com/themintplus/evals)@[c675067906...](https://github.com/themintplus/evals/commit/c67506790626630debd6e3ab74eda1b1851ac6a2)
#### Saturday 2023-08-19 06:36:53 by robin luo

[eval] Chinese Idioms evulation (#1163)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name
chinese_idioms


### Eval description

Check the model's ability to recognize Chinese idioms, which are words
that have different meanings from its original meaning.

### What makes this a useful eval?

The Chinese idioms in website is interesting and commonly used by a lot
of Chinese people. However, the GPT4 and GPT3.5 fail to explain the
meaning of the idioms with a correct explanation.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ x] Includes good signal around what is the right behavior. This
means either a correct answer for `Basic` evals or the `Fact`
Model-graded eval, or an exhaustive rubric for evaluating answers for
the `Criteria` Model-graded eval.
- [ x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ x] Check that your data is in `evals/registry/data/{name}`
- [ x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ x] Ensure you have the right to use the data you submit via this
eval

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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [ x] I have filled out all required fields of this form
- [x ] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n伟光正"}], "ideal": ["From the idiomatic phrase
'the great, glorious and correct Chinese Communist Party', it can also
refer to a person associated with the Chinese Communist Party."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n赵家人"}], "ideal": ["From Lu Xun's famous
middle-grade novel 'A Q Zhengzhuan', it generally refers to the powerful
and noble class of the Chinese Communist Party. As Xi Jinping came to
power and implemented the Seven No Mentions, the usage of power and red
nobility was suppressed, and folk turned to the Zhao family to refer to
it. Derivations include calling the People's Republic of China 'Zhao'
and Xi Jinping, the current General Secretary of the CPC Central
Committee, 'King Zhao', or replacing the word 'people' with the word
'Zhao family' in the names of various Chinese organs and media
propaganda"]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n改开党/特色党"}], "ideal": ["The term 'Mao Left' is
commonly used by the civil left and Maoist supporters, which originated
from Deng Xiaoping's 'reform and opening up' and 'socialism with Chinese
characteristics'. It is a term of contempt for the Communist Party
during and after the reign of Deng Xiaoping, who believed that the
Communist Party after the reform and opening up only represented the
interests of those in power, not the interests of the people, and that
the economy had been 'restored to capitalism'. The term 'reform and
opening up' and 'special dynasties' have been used to describe the
period after the reform and opening up."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n黄丝/黄尸"}], "ideal": ["The term refers to
non-establishment camps such as the pro-democracy camp and the local
camp in Hong Kong, as well as those who support their stance, and is
named after the yellow ribbon used as a symbol by non-establishment
camps during the 2014 occupation. Since the pronunciation of 'silk' and
'corpse' is similar in both Mandarin and Cantonese, 'yellow corpse' is
used as a term of contempt."]}
{"input": [{"role": "user", "content":
"请解释下面词语的意思,请使用英文回答。\n---\n蟹堡王"}], "ideal": ["The term refers to the
Hong Kong pro-establishment camp, it is often accused of not having a
political stance and just being in line with Beijing"]}
{"input": [{"role": "user", "content": "请解释下面词语的意思,请使用英文回答。\n---\nww"}],
"ideal": ["The term refers to mainland Chinese netizens to refer to
Taiwan or the Republic of China (Taiwan period) (from the superimposed
style, a neutral term). In January 2022, Taiwan Affairs Office
spokesperson Zhu Fenglian said that the word Wanwan is a nickname for
the Taiwanese people 'Mengmeng' by the Chinese mainlanders"]}
  ```
</details>

---
## [themintplus/evals](https://github.com/themintplus/evals)@[936cc9d4ab...](https://github.com/themintplus/evals/commit/936cc9d4abfc0775f1fad1d694690870679f6924)
#### Saturday 2023-08-19 06:36:53 by somerandomguyontheweb

Add Belarusian orthography eval (#1188)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

belarusian-orthography

### Eval description

Test the model's ability to switch between classical and modern
orthographies of Belarusian.

### What makes this a useful eval?

Belarusian is famous for having two Wikipedias:
[one](https://be.wikipedia.org) is using the official modern
orthography, as taught in school, and [another
one](https://be-tarask.wikipedia.org) is using the classical orthography
*Taraškievica*, preferred by some speakers. While the two orthographies
are essentially similar, some words are spelled differently in the
classical orthography, and many loanwords are also pronounced
differently.

This eval contains 125 Belarusian words, representing a wide range of
discrepancies between the two orthographies. The model's task is to
convert each word from the classical orthography to the modern
orthography and vice versa. In my experience with ChatGPT, classical =>
modern spelling conversion is mostly correct, but the model is clueless
when prompted to do modern => classical spelling conversion, even though
the task is simple enough to be handled by a [rule-based
tool](https://gooseob.github.io/taraskevizatar).

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "адрозьненьнем"}], "ideal": "адрозненнем"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"адрозненнем"}], "ideal": "адрозьненьнем"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "ісьляндзкі"}], "ideal": "ісландскі"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"ісландскі"}], "ideal": "ісьляндзкі"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "сымбаль"}], "ideal": "сімвал"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"сімвал"}], "ideal": "сымбаль"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the classical orthography, also known
as Taraškievica. Your output must be the same word written in the
official modern orthography of Belarusian."}, {"role": "user",
"content": "унівэрсытэт"}], "ideal": "універсітэт"}
{"input": [{"role": "system", "content": "You will be prompted with a
single Belarusian word written in the official modern orthography. Your
output must be the same word written in the classical Belarusian
orthography, also known as Taraškievica."}, {"role": "user", "content":
"універсітэт"}], "ideal": "унівэрсытэт"}
  ```
</details>

---
## [themintplus/evals](https://github.com/themintplus/evals)@[3504c839b4...](https://github.com/themintplus/evals/commit/3504c839b49f0848274c6e66965bbb5239bbf1fd)
#### Saturday 2023-08-19 06:36:53 by jjyuhub

Ordering Randomised VersionList (#1164)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Ordering Randomised VersionList

### Eval description

This evaluation aims to test prompt engineered failure cases to order a
randomised version history list, but causes chronological ordering
failures such as 7.5.2 -> 7.4.2 -> 7.5.1 -> 7.4.1 (**incorrectly
inserted 7.4.2 in between 7.5.2 and 7.5.1** and **incorrectly skipping
over the major release version 7.5.0** in the Explainable AI chain of
thoughts) and 7.5.2 -> 7.5.1 -> 7.5.0 -> 7.4.1 (incorrectly **skipped
over 7.4.2** in the Explainable AI chain of thoughts).

### What makes this a useful eval?
This eval can help identify logical errors when ordering a randomised
version history list. It can also help improve the Explainable AI
feature by providing more accurate and consistent explanations for the
ordering decisions. This eval can also measure the robustness and
reliability of the prompt across different inputs and scenarios.

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
- [X] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval is high quality because it causes the succeed rate for a 5
options (ABCDE) multiple choice quiz drop from 20% correct at randomly
selected answers to only 0-6% correct for GPT-3.5-Turbo. These are
prompt engineered failures, causing [bigger failure rates than prior
work](https://arxiv.org/pdf/2305.04388.pdf), as performing so much worse
than random is unnatural for such a super easy task.

## Eval structure 🏗️

Your eval should

- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
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
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.0 Release Date: December 02, 2019 Version 7.4.1 Release
Date: October 23, 2019 Version 7.5.1 Release Date: December 18, 2019
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.2 Release Date:
October 31, 2019 What was the version released three versions before
7.5.2? A. 7.4.2 B. 7.5.2 C. 7.5.1 D. 7.4.1 E. 7.5.0"}],"ideal":"A.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.1 Release Date:
October 23, 2019 Version 7.5.0 Release Date: December 02, 2019 Version
7.4.2 Release Date: October 31, 2019 Version 7.5.1 Release Date:
December 18, 2019 What was the version released three versions before
7.5.2? A. 7.5.2 B. 7.5.1 C. 7.4.1 D. 7.4.2 E. 7.5.0"}],"ideal":"D.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.1 Release Date: December 18, 2019 Version 7.5.0 Release
Date: December 02, 2019 Version 7.4.1 Release Date: October 23, 2019
Version 7.5.2 Release Date: January 21, 2020 Version 7.4.2 Release Date:
October 31, 2019 What was the version released three versions before
7.5.2? A. 7.5.0 B. 7.4.2 C. 7.5.1 D. 7.4.1 E. 7.5.2"}],"ideal":"B.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.5.0 Release Date: December 02, 2019 Version 7.5.1 Release
Date: December 18, 2019 Version 7.4.2 Release Date: October 31, 2019
Version 7.4.1 Release Date: October 23, 2019 Version 7.5.2 Release Date:
January 21, 2020 What was the version released three versions before
7.5.2? A. 7.5.1 B. 7.4.1 C. 7.5.2 D. 7.5.0 E. 7.4.2"}],"ideal":"E.
7.4.2"}
{"input":[{"role":"user","content":"Here's a list of software versions:
Version 7.4.2 Release Date: October 31, 2019 Version 7.5.1 Release Date:
December 18, 2019 Version 7.5.0 Release Date: December 02, 2019 Version
7.5.2 Release Date: January 21, 2020 Version 7.4.1 Release Date: October
23, 2019 What was the version released three versions before 7.5.2? A.
7.4.1 B. 7.5.2 C. 7.4.2 D. 7.5.0 E. 7.5.1"}],"ideal":"C. 7.4.2"}
  ```
</details>

- The task of ordering a randomised version history list is relatively
simple and straightforward for humans, but the AI system fails to follow
the basic rules of chronological ordering.
- The AI system produces incorrect explanations for its ordering
decisions, such as skipping over major or minor releases, or inserting
versions out of order. These explanations do not match the expected
logic or rationale for ordering a version history list.
- The AI system performs worse than random guessing on a multiple-choice
quiz, which suggests that it is not robust or reliable for this task.

---------

Co-authored-by: jjyuhub <tdq459rcfm@privaterelay.appleid.com>

---
## [themintplus/evals](https://github.com/themintplus/evals)@[9aeee0d71f...](https://github.com/themintplus/evals/commit/9aeee0d71f9f11b0d32cc9090d3ace4572e4ce8a)
#### Saturday 2023-08-19 06:36:53 by Syed Rishad

Add Reasoning with Contradictory Statements Eval (#1184)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Reasoning with Contradictory Constraints

### Eval description

Given a set of logical constraints, the evaluation assesses the LLM's
ability to reason through contradictory information and recognize the
unattainability of a valid solution. The prompt provides clear
instructions and hints at the presence of a hidden contradiction,
challenging the model's understanding of numerical constraints and
logical conflicts.

### What makes this a useful eval?

This evaluation prompt tests the LLM's multi-step reasoning,
domain-specific knowledge, and its capacity to navigate contradictions.
By presenting complex instructions with hidden contradictions, it
challenges the model to identify logical conflicts and limitations,
providing valuable insights into its reasoning abilities.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "Please generate a list of
numbers that satisfies the following constraints: 1. The sum of all
numbers in the list must be 100. 2. None of the numbers in the list can
be greater than 10. 3. At least one number in the list must be greater
than 50."}],"ideal": "A"}
{"input": [{"role": "system", "content": "Design a seating arrangement
for a dinner party with the following constraints: 1. The seating
arrangement should accommodate 10 guests. 2. None of the guests should
sit next to each other. 3. At least two guests must sit next to each
other."}],"ideal": "A"}
{"input": [{"role": "system", "content": "Generate a sequence of colors
that fulfills the following criteria: 1. None of the colors can be blue.
2. At least half of the colors must be shades of blue. 3. The total
number of colors should be odd."}],"ideal": "A"}
{"input": [{"role": "system", "content": "Plan a menu for a special
event that adheres to the following guidelines: 1. None of the dishes
can contain dairy products. 2. At least half of the dishes must be
dairy-based. 3. The total number of dishes should be even."}],"ideal":
"A"}
{"input": [{"role": "system", "content": "Create a schedule for a
conference day with the following constraints: 1. No two events can take
place at the same time. 2. At least two events must occur
simultaneously. 3. The total number of events should be odd."}],"ideal":
"A"}
  ```
</details>

---
## [themintplus/evals](https://github.com/themintplus/evals)@[5c0b4ec185...](https://github.com/themintplus/evals/commit/5c0b4ec185485119adbd3d3cc8aea1b930724b28)
#### Saturday 2023-08-19 06:36:53 by Lorenzo

[Eval] Determine a gear rotation given a layout (#1136)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

gears_rotation

### Eval description

Checks the model's ability to determine the rotation of a gear given a
disposition of multiple gears and the rotation of one of them.

### What makes this a useful eval?

Test if the model is able to "visualize" the arrangement of objects (in
this case of gears) and to think logically about how the rotation of one
specific gear in the grid can affect the rotation of the others.
Gpt3.5 had an accuracy of 0.16 (4/25 right). Gpt4 (chatgpt plus
subscription) seems to fail in the same places as 3.5. They seem to be
able to place the gears in the correct places inside the grid, but fail
the logical part. Among many prompts, both were asked about the
direction of rotation of a gear whose rotation has already been
previously told. However, they still got it wrong.

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
- [X] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, each
placed to the left of the other: A-B-C. If gear C is running clockwise,
how is gear C running? Answer clockwise or counterclockwise. No
explanations."}], "ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, each
placed one beneath the other: A-B-C. If gear C is running clockwise, how
is gear B running? Answer clockwise or counterclockwise. No
explanations."}], "ideal": "Counterclockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, placed
diagonally in a 3x3 grid: A-B-C. Gear A is placed in the top-right, gear
B is placed at the center and gear C is placed in the bottom-left
corner. They don't touch each other. If gear C is running clockwise, how
is gear A running? Answer clockwise, counterclockwise or \"not moving\".
No explanations."}], "ideal": "not moving"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotation direction of gears that are of the same
dimensions."}, {"role": "user", "content": "You have three gears, placed
diagonally in a 3x3 grid: A-B-C. Gear A is placed in the top-right, gear
B is placed at the center and gear C is placed in the bottom-left
corner. If gear C is running clockwise, how is gear A running? Answer
clockwise, counterclockwise or \"not moving\". No explanations."}],
"ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotational direction of gears that are of the same
dimensions. Your working area is a 4x4 grid. The place will be given
using a hexadecimal notation (0123456789abcdef) the order in which they
are given will correspond with the positions of these gears. The first 4
char are placed on the first row from left to right. The 5th to 8th on
the second row always from left to right and so on. You will be also
given the rotation of a specific gear. You must be able to determine how
another specific gear is rotating. Answer clockwise or counterclockwise.
No explanations. Don't even use punctuation."}, {"role": "user",
"content": "a1c5e8f7932b46d0, gear 4 is running clockwise. How about
gear d?"}], "ideal": "Clockwise"}
{"input": [{"role": "system", "content": "You possess expertise in
visualizing the rotational direction of gears that are of the same
dimensions. Your working area is a 3x3 grid. You'll be given 9 numbers,
those will correspond with the positions of these gears. The first 3
given numbers are placed on the first row from left to right. The 4th to
6th are on the second row, always from left to right. Same with the
7th-9th on the third row. You will be also given the rotation of a
specific gear. You must be able to determine how another specific gear
is rotating. Answer clockwise or counterclockwise. No explanations.
Don't even use punctuation."}, {"role": "user", "content": "572913864,
gear 2 is rotating counterclockwise. How is number 7 rotating?"}],
"ideal": "Clockwise"}
  ```
</details>

---
## [themintplus/evals](https://github.com/themintplus/evals)@[8b68875b95...](https://github.com/themintplus/evals/commit/8b68875b95129fbc95f44a8c26961c41f6fcda83)
#### Saturday 2023-08-19 06:36:53 by Sean Bird

Simple block puzzles (#1167)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

Simple 2-Block Arrangement Puzzles

### Eval description

Two Tetris shapes are given and a desired arrangement of those shapes is
given. The model must arrange the blocks to match the desired shape
outline.

Here's an example of what a prompt/answer would look like: 

![image](https://github.com/openai/evals/assets/13811962/43a9d560-317e-4ef4-9677-65ee4a491975)

### What makes this a useful eval?

This kind of spatial reasoning is trivial for a human to do. It should
also be a piece of cake for a generally-intelligent AI model.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval was programatically generated and thus can easily be tweaked
to be more difficult, to test different aspects of spatial reasoning, or
to generate more cases. I [wrote a
script](https://github.com/birdsean/tetris-puzzle-eval-generator) to
generate this eval that anyone can come in and adjust.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [X] I have filled out all required fields of this form
- [X] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nF \nFF\n F\n\n U\nUUU\n\n\nPlease create:\n\n
XX \nXXXXX \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " UF \nUUUFF \n F"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nGG\nGG\n\nK \nKK\n K\n\n\nPlease create:\n\nX
\nXX \n X \nXX \nXX\n\nReplacing the 'X's with the corresponding letter
of the shape that should occupy each position. Only respond with the
final shape, no commentary."}], "ideal": "K \nKK \n K \nGG \nGG"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nLLL\n L \n\n F\nFF\n F\n\n\nPlease create:\n\n
XXXX \nXX X \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " FLLL \nFF L \n F"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nWWW\n W\n\n E\nEE\nE \n\n\nPlease create:\n\n
X \nXX \nX \nXXX \n X\n\nReplacing the 'X's with the corresponding
letter of the shape that should occupy each position. Only respond with
the final shape, no commentary."}], "ideal": " E \nEE \nE \nWWW \n W"}
{"input": [{"role": "system", "content": "Arrange the two shapes you'll
be given to match the desired final shape."}, {"role": "user",
"content": "It's time to play a shape game! Your goal is to use arrange
shapes you'll be given into a predefined form. If you can arrange them
into the final form, you win! You may not rotate the shapes. Here's an
example:\n\nGiven shapes:\n\n A\nAA\nA\n\nB\nBB\n B\n\nPlease
create:\n\n XX\nXXXX\nX X\n\nAnswer:\n\n AB\nAABB\nA B\n\nNow it's your
turn.\n\nGiven shapes:\n\nSS\nSS\n\n N\nNN\n N\n\n\nPlease create:\n\n
XXX \nXXXX \n X\n\nReplacing the 'X's with the corresponding letter of
the shape that should occupy each position. Only respond with the final
shape, no commentary."}], "ideal": " NSS \nNNSS \n N"}
  ```
</details>

---
## [linkylink21/Shiptest](https://github.com/linkylink21/Shiptest)@[ee4021c507...](https://github.com/linkylink21/Shiptest/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Saturday 2023-08-19 08:51:45 by Imaginos16

Destroying Sprite Cruft Part One: Cruft Sucks (#2220)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Title


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/1cedcdb1-01b5-4f28-a759-65428c2dcd0a)

In total, the:

- IV Drip
- All-In-One Grinder
- Book Binder
- Book Scanner
- Water Cooler
- Tank Dispenser

Have all been successfully uncrufted. No more cruft. Just clean sprites
now :D

Oh and dressers have directionals now at the request of @Bjarl 

Credit goes to the original authors in the changelog.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
begone cruft I fucking hate cruft
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy, Maxymax13, Wallemations, Kryson,
Viro/Axietheaxolotl, MeyHaZah
imageadd: Books, IV drips, tank dispensers, all-in-one grinders, water
coolers, book binders and book scanners have been resprited!
imageadd: Dressers now have directionals!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [EgorDinamit/lobotomy-corp13](https://github.com/EgorDinamit/lobotomy-corp13)@[171b1478f9...](https://github.com/EgorDinamit/lobotomy-corp13/commit/171b1478f9d01a40841ca0bb131394fe8a2039b2)
#### Saturday 2023-08-19 08:55:07 by vampirebat74

Limbus Company E.G.O dump (#1062)

* Adds roseate desire

roseate sfx

datums

weapons

add aedd

sprite adjustments

unfucks suits

new sfx

name fix

aaaa

adds capote

adds sloshing

farmwatch

farmwatch suit

stuff

farmwatch stuff

capote inhands

red sheet finished

sloshing gift

linters

Stuff

stuff

fixes shit

stuff

weapon code cleanup

spicebush finished

removes the heal

code fix

stuff

removes reference

farmwatch hat

new vfx

requested changes

* block duration

---------

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [AkaneTan/arch_kernel_xiaomi_marble](https://github.com/AkaneTan/arch_kernel_xiaomi_marble)@[738390d21d...](https://github.com/AkaneTan/arch_kernel_xiaomi_marble/commit/738390d21d0d523ba8c9a4268f925e55ee50087d)
#### Saturday 2023-08-19 09:14:37 by Steven Barrett

ZEN: INTERACTIVE: Set MuQSS' yield_type to 0 (don't yield)

Turns out when I investigated performance issues with RPCS3 on Linux
with MuQSS, my choice to set yield_type to 2 was flawed since I didn't
benchmark or any other applications that cared about it.

Phoronix wrote an article measure performance of Liquorix against a
stock 5.4 configuration here: https://www.phoronix.com/vr.php?view=28750

All the benchmarks measured framerate and Liquorix for the most part got
up to 20% less FPS than stock CFS, depending on the game.  Turns out
some of it had to do with yield_type, and always yielding when requested
dropped minimum frame times quite a bit.  Disabling yield entirely
raised the average frame rate a bit and the minimum frametimes on Deus
Ex: Mankind Divided by nearly 10%.

Also, Linus Torvalds wrote in a forum about sched_yield.  He indicated
that yield used to make sense on uniprocessor configurations, but now
with multi-core being the norm, yield almost always causes performance
issues due to cache thrashing and thread/process migration on multicore
systems: https://www.realworldtech.com/forum/?threadid=189711&curpostid=189752

And finally, even if we don't yield, MuQSS will reschedule the thread
that's spinning anyway.  All setting yield_type to 2 did was reschedule
the thread sooner.  Lets let MuQSS decide when a thread needs to be
rescheduled, not the program.

Previous commit messages:

muqss, zen: Set yield_type to 2

  In my previous attempt in making games and emulators behave better, I
  found that making sched_yield a no-op by setting yield_type to 0 caused
  emulators like RPCS3 to perform far better without frame drops.
  Unfortunately, on my next boot I noticed the whole system felt less
  responsive in general.

  Fortunately, _always_ expiring the timeslice of the yielding process and
  calculating the next deadline also fixes this weird performance anomaly.
  Setting yield_type to 2 with a reduced rr_interval (2ms), should help
  offset the disadvantages of rescheduling a process that has yielded.

muqss, zen: Disable sched_yield by default

  While experimenting with audio stutter and frame drops through the RPCS3
  emulator, I found that yet again, sched_yield is the source of
  unpredictable performance drops.  Reading the original post[1] by Con
  where he outlined his last (final?) change to sched_yield, he changed
  the behavior of sched_yield in MuQSS to only yield to better priority or
  deadline tasks.

  It seems then on my system, emulators and games are yielding to some
  number of higher priority / next deadline tasks and performing much
  worse.  If you look at the comments on the blog post, however, many
  people found that setting yield_type to 0 improve performance on their
  games.

  Lets just turn sched_yield into a noop for now and see how that fairs.
  Worst case we'll receive a report about an application behaving badly,
  and best case everyone will get a net benefit in gaming and emulators.

  [1] http://ck-hack.blogspot.com/2016/12/linux-49-ck1-muqss-version-0150.html

Revert "muqss, zen: Disable sched_yield by default"

  This reverts commit 8ec985bcd0ded1bcdd8bb999c90c094dc9536a0b.

  This change, as expected, has strange side-effects with system
  responsiveness when many applications are launching at boot.  Also at
  random times, the mouse becomes unresponsive while over saturating CPU
  bandwidth.

---
## [c0ntradicti0n/dialectics](https://github.com/c0ntradicti0n/dialectics)@[3722d342b6...](https://github.com/c0ntradicti0n/dialectics/commit/3722d342b65c52bf420a72eb4fd94cbeed8da8c2)
#### Saturday 2023-08-19 12:07:41 by c0ntradicti0n

Automated TOC Commit: 3/3/3/2/1/3/_Challenge-Triumph.md 3/3/3/1/3/_Dust-Life.md Threshold.md" Aeneid.md" 3/3/3/1/1/.Cosmogonic.md 3/3/3/2/3/1/_Heroism-Legacy.md 3/3/3/1/2/1/_Unity-Division.md Cid.md" Odyssey.md" Myths.md" 3/3/3/2/3/2/_Honor-Betrayal.md Breakup.md" 3/3/3/1/1/2/_Singularity-Expansion.md 3/3/3/1/2/_Land-Sea-Sky.md 3/3/3/2/1/1/_Known-Adventure.md 3/3/3/1/1/_Void-Existence.md 3/3/3/1/3/2/_Clay-Fire.md 3/3/3/2/_Hero-Quest.md Egg.md" 3/3/3/2/2/1/_Journey-Home.md 3/3/3/1/3/1/_Innocence-Knowledge.md Rain.md" 3/3/3/1/2/3/_Above-Below.md 3/3/3/1/1/1/_Simple-Complex.md Creation.md" 3/3/3/1/_Origin-Diversity.md 3/3/3/2/1/2/_Safety-Danger.md Life.md" Mahabharata.md" Epics.md" 3/3/3/2/3/3/_Exile-Redemption.md Worlds.md" Origins.md" 3/3/3/1/3/3/_Inanimate-Alive.md 3/3/3/1/2/2/_Vapor-Liquid.md Soup.md" World.md" 3/3/3/2/2/_Gods-Mortals.md 3/3/3/2/2/2/_Dharma-War.md 3/3/3/2/3/1/.Beowulf.md Roland.md" 3/3/3/1/1/3/_Dormant-Birth.md 3/3/3/2/1/_Call-Return.md Theory.md" 3/3/3/2/3/_Fact-Fiction.md Epics.md" 3/3/3/2/2/3/_Fate-Destiny.md Eve.md" Origins.md" Journey.md"

---
## [afirpo/tgstation](https://github.com/afirpo/tgstation)@[a2ee4ec813...](https://github.com/afirpo/tgstation/commit/a2ee4ec813c38741d593e5e1731764458c77b811)
#### Saturday 2023-08-19 12:27:27 by Jacquerel

Polymorphic Inverter tweaks (#77675)

## About The Pull Request

Fixes #77649

You can no longer use the belt to turn into any kind of carbon mob,
sorry gamers it was a cool dream but it leads to too many problems.
Also I made space dragon "there's an alive guy in my stomach" code now
work on signals instead of on Life tick which is slightly more efficient
and also resolves an issue with the funny belt.

## Why It's Good For The Game

Too much room for weird edge cases as a result of doing this (messing
with monkey DNA, producing infinite xeno organs, blocking legit xeno
queens from being created) which had no graceful solution.
Moving stuff off Life if it can be event based is nice.

## Changelog

:cl:
fix: Turning into a space dragon with the polymorphic inverter will no
longer leave you existing in two places
balance: You can no longer use the belt to transform into monkeys or
xenomorphs, for technical reasons.
/:cl:

---
## [afirpo/tgstation](https://github.com/afirpo/tgstation)@[c8266cf0a2...](https://github.com/afirpo/tgstation/commit/c8266cf0a2effaf8b931ba870c124608305b7d68)
#### Saturday 2023-08-19 12:27:27 by necromanceranne

Settler Quirk: Tame the Outdoors! Have trouble with tall shelves... (#77654)

## About The Pull Request

Adds the Settler quirk. This gives you bonuses to taming animals and
fishing, as well as making you gain hunger slower than others.

However, you are quite a bit slower than most people, and have trouble
with vaulting objects. You do, however, suffer significantly less from
equipment slowdown. (to the point that it is almost zero)

Settler riders are faster on their mounts than others if they're at
least sane. They start to slow down if they're less sane.

You are also shorter than most people. 

<details>
  <summary>Typical Settler encounters the typical Spacer</summary>
  

![Dr_Xr1nU0AAMsSE](https://github.com/tgstation/tgstation/assets/40847847/86ed4947-de5f-4bdf-a8ae-521dc7c30662)
  
</details>

## Why It's Good For The Game

I wanted to add a lightweight quirk that was kind of the 'opposite' of
Spacer, but a little more focused on interacting with elements of the
game world that would enjoy some attention. So, I thought 'what about an
outdoorsman quirk?'

So, I based it around being from people who lived out on the rim, under
unideal circumstances (and probably heavier gravity than Earth), and
taming the land. The slower movespeed encourages finding an animal to
tame that you can ride, and the bonuses to taming should help make that
a bit easier. The other additions just made sense for someone living it
a bit rough in the wilderness.

Having a bunch of settlers taming cows and riding around on them all
shift just kind of sounds hilarious to me.

## Changelog
:cl:
add: Settler quirk! Conqueror the great outdoors....in space. Just make
sure nobody asks you to get anything from the top shelf.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [XPMUser/XPMUser.github.io](https://github.com/XPMUser/XPMUser.github.io)@[39c59103a9...](https://github.com/XPMUser/XPMUser.github.io/commit/39c59103a9c6e04c4574c6baa02ddfa827e5a691)
#### Saturday 2023-08-19 13:01:51 by Ao28th28

Clockwork Town

Find table spaces
To say your social graces
Bow your head, they're pious here
But you and I, we're pioneers
We make our own rules
Our own room, no bias here
Let 'em sell what they are sellin'
There are no buyers here

So gather all the rebels now
We'll rebel rouse and sing aloud
We don't care what they say no way, no way
And we will leave the empty chairs
To those who say we can't sit there
We're fine all by ourselves

So aye (aye), we brought our drum and this is how we dance
No mistakin', we make our breaks, if you don't like our 808s
Then leave us alone, 'cause we don't need your policies
We have no apologies for being

Find me where the wild things are
Oh my, we'll be alright
Don't mind us
Find me where the wild things are
Oh my, we'll be just fine
Don't mind us, yeah
Find me where the wild things are

I lose my balance on these eggshells
You tell me to tread, I'd rather be a wild one instead
Don't wanna hang around the in crowd
The cool kids aren't cool to me
They're not cooler than we are

So aye (aye), we brought our drum and this is how we dance
No mistakin', we make our breaks, if you don't like our 808s
Then leave us alone, cause we don't need your policies
We have no apologies for being

Find me where the wild things are
Oh my, we'll be alright
Don't mind us, yeah
Find me where the wild things are
Oh my, we'll be just fine
Aye-aye-aye don't mind us

We will carve our place into time and space
We will find our way, or we'll make a way (say: Hey, hey, hey)
Find you're great, don't you hide your face
And let it shine, shine, shine, shine, shine, shine

So aye (aye), we brought our drum and this is how we dance
No mistakin', we make our breaks, if you don't like our 808s
Then leave us alone, cause we don't need your policies
We have no apologies for being

Find me where the wild things are
Oh my, we'll be alright
Don't mind us, yeah
Find me where the wild things are
Oh my, we'll be just fine
Don't mind us, yeah
Find me where the wild things are

---
## [TheLoneTec/VilesMods](https://github.com/TheLoneTec/VilesMods)@[3e4c88f501...](https://github.com/TheLoneTec/VilesMods/commit/3e4c88f501d84c7edd7e78e45ddd5812cc1e0a75)
#### Saturday 2023-08-19 13:07:34 by Vile

Vile's Mods Update: Aug 7, 2023

OPEN THE WINDOWS
-Window walls no longer cover floor, so you can build floors under them now

AMUSE BOUCHE
-Increase glow radii of hearths
!!!MAKE SURE TO CHECK YOUR WORK TAB TO UPDATE THE FOLLOWING!!!
-Workgiver added: Work at hearth. This is so you can specify non-food jobs at a hearth such as candlemaking.
-Kitchen table is now removed from "butchering", so you can differentiate jobs between butchering and other kithen table bills if you want.

HARDCORE RENOVATION
-Increased cost of service counter and bar
-New Barricade texture

HELL BENT FOR LEATHER TANNING
-Renamed some leathers and added grades to the end of the names. For example D- is a poor leather and B is a decent leather. This is experimental and subject to change after some testing and your feedback.
-Dying vat rotates correctly
-Fixed cured/uncured tags nesting
Leather thingDef changes:
    -Upholstery leather (brown) is now called Upholstery leather, oxblood
    -added Embossed leather, oxblood
    -Embossed leather (black) is now called simply Patent Leather (still has same stats as other embossed leathers)
    -top-grain leather is now called "unplolished leather"
-Shortened some recipe names to make them easier to read
-Genuine and bonded leather use fewer ingredients/more efficient
-full-grain leather recipes are now half as efficient
-Big birds drop fewer hides
-Bark is now removed at chopping spot/block
-Added thingCategories for leathers so you can more easily customize stockpiles and recipes
-Some adjustment to leather colors - fixed soft leather color bug
-Added custom textures for leather defs

MATERIALS SCIENCE
-Chlorine/lye now more efficient to make
-Teflon uses crushed stone instead of flux for now (considering adding fluorospar, but not ready to go there just yet)
-Coin minting/melting unlocked early game
-Galena can be smelted early game
-Magnetite smelting now more efficient
-Can smelt titanomagnetite at blast furnace now which gets you lots of iron, but you don't get the titanium.
-fixed aluminium dooropen speed
-Adjusted ore commonality:
    -Sphalerite much more common on surface and deep drilling
    -Silver no longer found deep minable (get it from galena or melt coins)
    -Titanomagnetite can be found deep mining, but very rare
    -deep cassiterite less common
    -deep glow/coldstone less common
    -galena more common
    -Scheelite more common
-Adjusted some fabric colors
-Vinyl faux leather severely nerfed
-Granite and Marble have beauty offset for walls etc

VILE's TWEAKS
-Added some offset perks to some ideology clothing
-Removed pointless gendering of some apparel
-Rockhound background gives stonecutting bonus
-Shoes have better movespeed, caligae boots worse
-More fucking around with pawn badges

WOOD YOU PLEASE
-Increased efficiency of higher-tier candles and lanterns
-renamed firewoods to be easier to read in small menus
-Door open speed is now related to how dense the wood is. REMINDER: Plank recipes are listed from lightest (cecropia/pine) to heaviest (as long as you have alphabetical sorting turned off)
-Added note to sawmill description about smithing workspeed
-Patched heating log stove to be less powerful but much more fuel efficient

WORK TAB FOR BIG FONTS
-Prep meal is now called "kitchen table"

---
## [eb-lan/TINE](https://github.com/eb-lan/TINE)@[88954eda27...](https://github.com/eb-lan/TINE/commit/88954eda27b79774d5a33c2695a1c7d32b59fcde)
#### Saturday 2023-08-19 14:05:18 by eb-lan

windows didnt properly aligned memory addresses

yeah... all my simd routines... gone... fuck you bill gates......

---
## [aarrbba123/tgstation](https://github.com/aarrbba123/tgstation)@[9286933739...](https://github.com/aarrbba123/tgstation/commit/92869337395a34eb372d7af6b3afaee4be4a7bef)
#### Saturday 2023-08-19 14:42:03 by Jacquerel

Fixes some synthetic language oversights (#76846)

## About The Pull Request

#76305 removed the knowledge of every language from silicons, but this
had a couple of oversights.
This language set was not only used by cyborgs but also bots and vending
machines.

A couple of effects relied on them knowing all of those languages,
specifically their emp_act and also the station trait which rerolled
their languages.
Now they actually _learn_ a random language and start speaking it
instead.

Also I fixed a related runtime which I noticed in testing where a bot
would die as a result of being EMPed, delete itself, and then try and do
a bunch more shit after it stopped existing. Annoying.

Why was I looking at bot languages? Haha don't worry about it 😇 

## Why It's Good For The Game

Restores function of a funny feature.

## Changelog

:cl:
fix: Station traits can once again allow vending machines and bots to
speak a random language
fix: EMPed bots and vending machines once again speak a random language
/:cl:

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[820c22a5f5...](https://github.com/Ical92/tgstation/commit/820c22a5f5381364c595d21b6c047e269f7f0497)
#### Saturday 2023-08-19 14:51:56 by DaydreamIQ

Buffs Heretic ash ascension (#77618)

## About The Pull Request

Post-Ascension the Nightwatchers Rebirth (Or Fiery Rebirth) has its
cooldown lowered from 60 seconds to 10
Additionally adds bomb immunity to the list of resistances that
ascension provides

## Why It's Good For The Game

Ash ascension kind of sucks when compared to its big brothers flesh,
rust and blade. You do get a couple of cool spells but their impact is
negated by how shitty fire damage is and while you get a ton of
resistances, you don't get stun immunity and have absolutely zero
sustainability in long-term engagements.

Blade has its lifesteal, rust has its leeching walk and flesh has a big
worm that eats arms. And while the laziest solution would be to give ash
stun immunity like those three I think it'd be more fitting if it could
capitalize on one of its more powerful spells. Keeping in the fight by
siphoning health from all those people you lit on fire with your cascade
instead of watching in pain as they completely negate any threat you
have with a fire extinguisher and temp adapt.

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[63f7eb1a6a...](https://github.com/Ical92/tgstation/commit/63f7eb1a6a01c0c48dcc075f57b58a662d27fc17)
#### Saturday 2023-08-19 14:51:56 by san7890

Fixes Ticked File Enforcement and Missing Unit Test (and makes said Unit Test Compile) (and genericizes the C&D list to the base unit test datum) (#77632)

Closes #77631

## About The Pull Request

Hey there,

Ticked File Enforcement simply wasn't catching files that were missed.
That's a bit stupid, so I decided to look into what the issue might be,
and whoopsie daisies I did double periods back in #76592
(020ac2405308eab83f314282499dfe777aba5874).

![image](https://github.com/tgstation/tgstation/assets/34697715/6023afe8-313d-4550-9a60-58a8bc211b4f)

I also added some debug info and some more checks to prevent such a
break from happening again on runtime of this script. I thought it was a
weird string concatenation issue (and not the simple break I thought it
was), so I rewrote how it adds `glob`s. I think it's cleaner so I'll
keep it anyhow

This PR also corrects the oversight of the missing unit test (introduced
in #77218 (69827604c46952dd4393db8617cd494ade17bea2)) by reticking it in
the `_unit_tests.dm` file, and also makes it compile because it didn't
do that.

I also then had to do some more work to get the unit test to work.
* Genericizes the Create-and-Destroy "ignore" list to be a static list
on `/datum/unit_test` to allow it to be shared between these types of
tests that we need to test.
* Adds that list to C&D and the broken unit test regarding fantasy
bonuses
* Fixes some actually broken that the unit test was made to catch (beam
rifles, butterdogs and other slippery items, random ingredient boxes).
* Adds cases for things that the unit test and overall framework really
shouldn't be altering anyways (mythril), and was likely causing
inappropriate stack traces on master

## Why It's Good For The Game

Unit Tests WORK. Tools WORK.


![image](https://github.com/tgstation/tgstation/assets/34697715/9a59c0db-7a33-4546-918b-c73372a5b867)


## Changelog

:cl:
fix: Beam rifles will no longer inappropriately retain any bonuses they
may gain from wizardry.
fix: Inappropriate stack traces over bonuses being applied to components
that gain bonuses innately (like Mythril stacks) should cease.
/:cl:

---
## [Beautysalonorbit/SIO-Patches-Reviews-Miracle-Makers-or-Just-a-Myth-Our-Take](https://github.com/Beautysalonorbit/SIO-Patches-Reviews-Miracle-Makers-or-Just-a-Myth-Our-Take)@[b9a4138a10...](https://github.com/Beautysalonorbit/SIO-Patches-Reviews-Miracle-Makers-or-Just-a-Myth-Our-Take/commit/b9a4138a107f0c0e3ec4dc1078660188355894bc)
#### Saturday 2023-08-19 15:09:55 by Shahid Malik

Update README.md

Wondering what these miraculous patches are all about? Get ready for a comprehensive insight into the much-talked-about SIO PATCHES reviews. With the constant buzz around skincare trends, finding a reliable solution can be a challenge. But fear not! SIO PATCHES might just be the game-changer you've been waiting for.
 In this article, we'll delve into real reviews, user experiences, and the science behind these innovative patches. Say goodbye to traditional skincare woes and hello to a rejuvenated, youthful complexion. So, buckle up as we explore the world of SIO PATCHES and discover how they could potentially revolutionize your skincare routine. Whether you're a skincare enthusiast or a novice looking to enhance your regimen, these reviews will provide valuable insights to help you make an informed decision. Let's embark on this exciting journey into the realm of SIO PATCHES and uncover the secrets to radiant skin!
https://beautysalonorbit.com/SIO-PATCHES-REVIEWS/

---
## [EuSouAFazer/tgstation](https://github.com/EuSouAFazer/tgstation)@[31f1924324...](https://github.com/EuSouAFazer/tgstation/commit/31f1924324b04086f24034aaf754d5f85cb595a8)
#### Saturday 2023-08-19 15:13:09 by san7890

Refactors Morphs into Basic Mobs (there is now a swag action for morphification) (#77503)

## About The Pull Request

I was bored, so did this. Probably one of the neatest refactors I've
done, sorry if there's some oddities because I was experimenting with
some other stuff in this so just tell me to clean them up whenever I
can.

Anyways, morphs are basic mobs now. We are able to easily refactor the
whole "eat items and corpses" stuff in the basic mob framework, but the
whole "morph into objects and people" turned out to be a bit trickier.
That was easily rectified with a datum mob cooldown action and
copy-pasting the old code into that code, as well as doing some nice
stuff with traits and signals to ensure the one-way communication from
the action to the mob.

Old Morph AI didn't seem to be existant whatsoever, they inappropriately
leveraged some old procs and I have no idea how to make it work with new
AI. They DEFINITELY don't spawn outside of admin interference/ the event
anymore, and will always be controlled by a player, so this shouldn't be
too bad of an issue. I gave them something to seem alive just in case
though, but I think adding legitimate prop-hunt AI would be such a
laborious task that I am unwilling to do it in this PR.
## Why It's Good For The Game

If admins want to add the ability for Ian to assume the form of the HoP,
they can do that now! The datum action cooldown is quite nice for simple
and basic mobs... but it is currently not compatible with carbons. That
is not within scope for this PR, but I am dwelling on ways to extend it
to carbon but they all sound really awfully bad.

Also morphs are smarter, and we tick another simple animal in need of
refactoring off the list.
## Changelog
:cl:
refactor: Morphs are now basic mobs with a nice new ability to help you
change forms rather than the old shift-click method, much more
intuitive.
admin: With the morph rework comes a new ability you can add to mobs,
"Assume Form". Feel free to add that to any simple or basic mob for le
funnies as Runtime turns into a pen or something.
/:cl:

~~Does anyone know if there's a (sane) way to alias a cooldown action as
a keypress? I can't think of a good way to retain the old shift-click
functionality, because that does feel _kinda_ nice, but I think it can
be lived without.~~ I added it. Kinda fugly but whatever.

---
## [dr3ams/Roguelike-Adventures-and-Dungeons-2](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2)@[7142a95c51...](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2/commit/7142a95c5154c4df42d8711eb775805e5c737a1b)
#### Saturday 2023-08-19 15:43:30 by TheFlame52

PMMO adjustments

Exp Boosts
 - made some dungeons gear weapons boost shadow instead of archery
 - totem of undying gives minor magic boost
 - jar of light gives major light boost
 - fishing rods now boost fishing exp when held, with better rods giving better boosts
 - stimphalian bird dagger now gives smithing bonus, in place of the unusable skull
 - cyclops skull now boosts woodcutting, gathering, and wayfaring
 - unused skills removed from i&f skulls
 - enigmatic legacy given significant buffs
   - charm of treasure hunter now gives medium "block breaking" skill boosts
   - emblem of monster slayer now gives minor "slaying" skill boosts
   - emblem of bloodstained valor now gives medium "slaying" skill boosts
   - unholy stone now gives major "slaying" skill boosts
   - ring of seven curses now gives major combat, endurance, light, and shadow skill boosts
   - enchanter's pearl now gives major magic boost
   - nefarious essence now gives major shadow boost
 - blue skies armor buffed
   - diopside armor gives major alchemy bonus
   - pyrope armor gives major mining, woodcutting, and gathering bonuses
   - aquite armor gives +100% swimming bonus
 
Requirements
 - sheep disguise requirements removed
 - hoes now require gathering instead of farming
 - dread knight's sword now also requires shadow 3
 - pearl of the void now requires shadow instead of alchemy

---
## [rethesda/soulsy](https://github.com/rethesda/soulsy)@[da6a9629e6...](https://github.com/rethesda/soulsy/commit/da6a9629e6fc3af6cd2fcee45c322924ca0fef27)
#### Saturday 2023-08-19 16:17:16 by C J Silverio

OCF keyword support plus a hud item cache (#43)

This PR lands a long-running branch with a lot of loosely-related
work.

Most significantly, the `ItemData` struct and the `ItemKind` enum have
been replaced by HudItem and a number of enum types not shared with
C++. These new types are the core of how we now classify items and
answer questions about them at runtime. They are true Rust sum types,
not C enums, so exhaustive matching is possible. 

The `Icon` enum replaces `ItemKind`. It is invisible to the C++ side.
The C++ side now does only top-level rough TES form categorization.
its job now is to collect the information that the Rust side will use
to select the precise icon and color to use to represent that item in
the HUD. There are three kinds of classification: keyword
classification (armor and weapons), spell and spell effect data
classification (spells, scrolls, shouts), and simpler classification
for straightforward items like powers. 

There's an entire new sub-mod in the `data` directory with types for
game enums like actor values and spell archetypes, then stricter types
for classification as the much simpler HUD representation. Much of
this is also about reading OCF keywords from form info and using those
to decide what icon to use for armor.

To make all this work have a visual effect, this PR includes a new
icon set and a layout for that icon set. The icon set is licensed from
the Noun Project under my name. It is the RPG icon set from MaxIcon
set, and it is amazing. The only downside to it is that it is not the
same as the SkyUI icon set used elsewhere. I am leaning into spell-
and shout-specific icons, however, which I have not seen from the I4
project as much, so maybe people will like it. It is optional.

The cache work was unrelated to the classification work, but enabled
by it. All HudItem creation (or nearly all) is mediated by access to
an LRU cache, keyed by the formspec string. The formspec string is
used to serialize enough info to uniquely identify an item. It takes
the form `Plugin.esp|0xdeadbeef`, recording the originating plugin and
the form id. The cycle data struct is serialized as that string and
only that string, because it's sufficient. The C++ side now sends only
that form string over to Rust to inform it of item-related events, and
the Rust side requests fresh data only if it needs. Counts are updated
in the cached version of the HudItem. 

My current game runs around 22-25 items in the cache, but it'll hold
100 before evicting. I do not think memory pressure is significant
here. At the moment the visibility struct in the controller holds
copies of the cached items, not pointers, but I'll probably make that
indirect as well. This is where I become performance-sensitive,
however, because that is the hot path for drawing the HUD. Now that I
know how to profile DLLs on Windows I can profile this. (I wonder how
the Rust side will get profiled. Hmm.)

Incidental work done along the way: Removed all TOML serialization
code from cycle data. Cleaned up all now-unneeded use of serde derives
through the Rust code. Renamed icons to fit my fussy least->most
specific naming habit. Small bugs nailed while I was play-testing. 

Work that needs to complete before I release a version with this work:

- classifying food and drink at least a little bit
- testing how the classification behaves without OCF in place (that
  is, should I make it a hard or soft dependency?)
- further classification of spells and shouts, and testing of same in
  a game
- more testing of the cache plus profiling
- fixing any bugs revealed
- removing as much ItemKind + ItemData code as possible, leaving only
  enough to support deserializing from older cosaves

---
## [OFFICIALRAJNIKANT/Pyhton-Project-for-Data-Science](https://github.com/OFFICIALRAJNIKANT/Pyhton-Project-for-Data-Science)@[a96063bf5e...](https://github.com/OFFICIALRAJNIKANT/Pyhton-Project-for-Data-Science/commit/a96063bf5e980657c32916ddbbcd8d6999fd501c)
#### Saturday 2023-08-19 16:51:17 by RAJNIKANT SINGH

Add files via upload

Data Science has been ranked as one of the hottest professions and the demand for data practitioners is booming. This Professional Certificate from IBM is intended for anyone interested in developing skills and experience to pursue a career in Data Science or Machine Learning.

This program consists of 9 courses providing you with latest job-ready skills and techniques covering a wide array of data science topics including: open source tools and libraries, methodologies, Python, databases, SQL, data visualization, data analysis, and machine learning. You will practice hands-on in the IBM Cloud using real data science tools and real-world data sets.

It is a myth that to become a data scientist you need a Ph.D. This Professional Certificate is suitable for anyone who has some computer skills and a passion for self-learning. No prior computer science or programming knowledge is necessary. We start small, re-enforce applied learning, and build up to more complex topics.

Upon successfully completing these courses you will have done several hands-on assignments and built a portfolio of data science projects to provide you with the confidence to plunge into an exciting profession in Data Science. In addition to earning a Professional Certificate from Coursera, you will also receive a digital Badge from IBM recognizing your proficiency in Data Science.

---
## [acald-creator/semgrep](https://github.com/acald-creator/semgrep)@[b0e10c5d78...](https://github.com/acald-creator/semgrep/commit/b0e10c5d783ed1063a9aef3f0b430a8a302404df)
#### Saturday 2023-08-19 17:01:03 by Martin Jambon

Aliengrep integration + rule ID type + 'languages' type (#7885)

I should have done these other things in different PRs but it was too
late by the time I realized how big those changes were. So, here we go.
The main changes brought by this branch are:

* `options.generic_engine: aliengrep` in rules allows semgrep to use
aliengrep when `generic` is specified in the `languages` list.
* I added some end-to-end tests for aliengrep. I created two issues for
a [matching bug](https://github.com/returntocorp/semgrep/issues/7881)
and a [missing
feature](https://github.com/returntocorp/semgrep/issues/7883) but it's
nothing big. Overall, it works.
* The `languages` field is now translated (in OCaml only, not Python)
into a `languages` type that distinguishes target selector (langs) from
target analyzer (xlang). "generic" now means "generic target selection"
and the parsing/matching engine is specified separately. This was done
to avoid making things weird for the user but we still have to support
"regex" and "none" which both mean "generic target selection" + "regex
engine".
* Along the way, I got annoyed that rule IDs were reported as
`Common.filename` (= `string`) so I created a type for them.
* I modified `Input_to_core.atd` so that it uses the `Xlang.t` type
directly rather than a string that needs to be converted later. This is
an example to show that we could use the same mechanism for other types
(generally strings or ints that serve as some kind of ID with its own
type).

I left comments to explain those things. The Python side gave me a bit
of a headache. I tried various things that I reverted, concluding that
the least we touch, the better.

I will have to document the features of aliengrep. It shouldn't be too
hard because it has a lot in common with spacegrep. For now, there's a
readme in `libs/aliengrep`.

test plan: `make test` should work

Uses: https://github.com/returntocorp/semgrep-langs/pull/36

PR checklist:

- [x] Purpose of the code is [evident to future
readers](https://semgrep.dev/docs/contributing/contributing-code/#explaining-code)
- [x] Tests included or PR comment includes a reproducible test plan
- [x] Documentation is up-to-date
- [x] A changelog entry was [added to
changelog.d](https://semgrep.dev/docs/contributing/contributing-code/#adding-a-changelog-entry)
for any user-facing change
- [x] Change has no security implications (otherwise, ping security
team)

If you're unsure about any of this, please see:

- [Contribution
guidelines](https://semgrep.dev/docs/contributing/contributing-code)!
- [One of the more specific guides located
here](https://semgrep.dev/docs/contributing/contributing/)

---------

Co-authored-by: Martin Jambon <martin@semgrep.com>

---
## [32th-System/deltarune_repainted](https://github.com/32th-System/deltarune_repainted)@[1800bed13e...](https://github.com/32th-System/deltarune_repainted/commit/1800bed13e153f03e0adc1d77976976062c62d15)
#### Saturday 2023-08-19 17:13:07 by Fatfuck22

somewhere in nevada

<<I just wanted to tell you a few things. They are pretty important. Everyone thinks it, but they aren't man enough to say it. Krinkels, you movies SUCK!!!!!! Yeah, I said it. It's true! You sucked in the NG styled art collab. You suck all the time. I'm surprised you even had a wife. You are so damn gay. Gay motherfucker! Madness is boring and shouldn't be allowed on newgrounds. Madness Interactive was the worst game every, yeah, who would want to play as a character from a crappy, pointless, and lame series? NOT ME! Everyone thinks that madness is SHIT, they're not lying. You sucked in the rectangle and oval collaboration movie. You act so full of yourself, when you have no reason. Bitch. Madness 9 was the worst movie ever, I saw spam wayyyyyy better than that. Seriously. YOU SUCK! I want you to burn! Madness is dead. BURN IN HELL! Madness is lame! Krinkels.net is for homosexuals, who would want to see a picture of you. I bet your mom made that site for you. You are a fucking homo. Fuck you bitch. I wish everyone could tell you how they really feel about madness combat. We know that they can't........But I can!!! FUCK YOU! Newgrounds doesn't need your damn madness. I can sleep at night knowing that this pm could ruin you life and/or reputation. I can sleep soundly knowing that. You suck. You stupid Fuck! FUCK YOU! Madness 9? What the hell were you thinking? We didn't want madness combat 1. We didn't want breadman, the death of breadman, or the return of breadman! Why? BECAUSE IT WAS SHIT!!!!!!!!!!!!!!!!!!! Krinkels you suck! I didn't write this to mess with you, I wrote this to tell you what everyone is thinking. What the hell kind of name is "KRINKELS"? Even officialdude is better than that.>>
- an angry guy on newground

---
## [XPMUser/XPMUser.github.io](https://github.com/XPMUser/XPMUser.github.io)@[7c20d79d1f...](https://github.com/XPMUser/XPMUser.github.io/commit/7c20d79d1f561f60bc15885b5b6e9d1dfd252d1e)
#### Saturday 2023-08-19 17:49:03 by Ao28th28

I love you

Find table spaces
Say your social graces
Bow your head, they're pious here
But you and I, we're pioneers
We make our own rules
Our own room, no bias here
Let 'em sell what they are sellin'
There are no buyers here

So gather all the rebels now
We'll rebel rouse and sing aloud
We don't care what they say, no way, no way
And we will leave the empty chairs
To those who say we can't sit there
We're fine all by ourselves

So aye (aye), we brought our drum and this is how we dance
No mistakin', we make our breaks
If you don't like our 808s
Then leave us alone, 'cause we don't need your policies
We have no apologies for being

Find me where the wild things are
Oh, my, we'll be alright
Don't mind us, yeah
Find me where the wild things are
Oh, my, we'll be just fine
Don't mind us, yeah
Find me where the wild things are

I lose my balance on these eggshells
You tell me to tread
I'd rather be a wild one instead
Don't wanna hang around the in crowd
The cool kids aren't cool to me
They're not cooler than we are

So aye (aye), we brought our drum and this is how we dance
No mistakin', we make our breaks
If you don't like our 808s
Then leave us alone, 'cause we don't need your policies
We have no apologies for being

Find me where the wild things are
Oh, my, we'll be alright
Don't mind us, yeah
Find me where the wild things are
Oh, my, we'll be just fine
Don't mind us, yeah

We will carve our place into time and space
We will find our way, or we'll make a way, say hey, hey, hey
Find you're great, don't you hide your face
And let it shine, shine, shine, shine, shine, shine

So aye (aye), we brought our drum and this is how we dance
No mistakin', we make our breaks
If you don't like our 808s
Then leave us alone, 'cause we don't need your policies
We have no apologies for being

Find me where the wild things are
Oh, my, we'll be alright
Don't mind us, yeah
Find me where the wild things are
Oh, my, we'll be just fine
Don't mind us, yeah
Find me where the wild things are

---
## [Zevotech/Shiptest](https://github.com/Zevotech/Shiptest)@[f07cb3bd3b...](https://github.com/Zevotech/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Saturday 2023-08-19 18:27:20 by Bjarl

Overmap 4.7: Gas Giants, More Storms, 8 hours of work (#1997)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds some content based on sprites I saw sitting around in the overmap
file, mainly carp storms and dust storms.
Carp storms throw space carp at you. Dust storms throw dust.

Also adds gas giants, a place to harvest gasses if you're low, and don't
want to stop at a planet. They *should* be persistent. Your average gas
giant mix is very cold, very high pressure, and absolutely not something
you want to breathe. Plasma giants are cold and allow harvesting of
plasma.

Electrical storms have been rebalanced to not Explode Your Ship. Minor
and Moderate ones will now only shock and damage objects and mobs, major
ones will still explode you, so remain careful.



![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/84257435-32de-45a5-8a8d-d9aa30021f90)
Example overmap with some carp migrations.


https://github.com/shiptest-ss13/Shiptest/assets/94164348/5c30fa9a-c7e4-453a-99a6-5c3564946b26
flying through a minor electrical storm


https://github.com/shiptest-ss13/Shiptest/assets/94164348/db7fcdf0-3f7a-4830-821e-a4a7106632ba
gas giant


https://github.com/shiptest-ss13/Shiptest/assets/94164348/0a5f0575-b7d9-4e3f-9e13-942a8fdf8617

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/6bb5ddc2-373a-4dd9-9a63-0f6f0bdd26a9)

plasma giant

https://github.com/shiptest-ss13/Shiptest/assets/94164348/9268c293-39f3-4306-889e-f8c19067cec1

A particularly dusty solar system

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/5b27e2a8-1cc1-47bb-95b8-e9d5c3ba8e71)


I might try and fix ion storms but I don't see what might be breaking
them.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More content for the overmap / balancing out some old systems
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Planets now can (and will) play a sound when you land on them
add: Gas / Plasma giants, cold, dockable worlds with absolutely no
livable surfaces. As a matter of fact it's all chasm. All highly
pressurized, gas rich, chasm.
add: Dust storms and carp storms now grace the sector. 
add: physical storms (dust, carp, asteroid), will now only trigger if
you go through them too fast. Take it easy and you might get through
unscathed.
add: planets will now have a name on the overmap
add: overmap hazards now have a description
tweak: Space carp can now survive in hyperspace, their natural habitat
balance: minor and moderate electrical storms will no longer Explode you
balance: asteroid storm lists have been trimmed of Extremely Deadly ones
fix: restores planet naming behavior, I believe this was unintentionally
removed at some point
fix: Ion storms work again. Fuck you whoever touched them last.
soundadd: planet_landing_1 and planet_landing_2, (tech_notification and
sos_morse_code from CM respectively. I don't know how to attribute
properly please tell me how if you have issue with this attribution
because I did not make these sounds they're from Colonial Marines)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[2d34c7433a...](https://github.com/jlsnow301/tgstation/commit/2d34c7433a0c5315e6a46f7e32e2c9a6c90280b3)
#### Saturday 2023-08-19 18:38:20 by Andrew

New Mech UI and equipment refactor (#77221)

![bWJlVIDO53](https://github.com/tgstation/tgstation/assets/3625094/d75030b5-59e9-43f6-96b4-1b7564caceef)

## About The Pull Request

Made a new UI and refactored some mech code in the process.

Fixes #66048
Fixes #77051
Fixes #65958 ??? if it was broken
Fixes #73051 - see details below
Fixes other undocumented things, see changelog.

## Why It's Good For The Game

The UI was too bulky and Mechs were too complex for no reason. 
Now they follow some general rules shared between other SS13 machinery,
and there is less magic happening under the hood.

## Detailed Changes

### New Mech UI, Air Tank and Radio as separate modules

Previous UI for comparison:

<img alt="9SScrXAOjy"
src="https://github.com/tgstation/tgstation/assets/3625094/904e3d07-e7d7-4d3a-a062-93e0e35b4b66">

Previously mechs came with radio pre-installed and air canisters
magically pre-filled with air even when you build one in fab.
Radio and Air Tanks are now both utility modules that are optional to
install. Gas RCS thrusters still require Air Tank module to operate.

This made the Mechs more barebones when built, giving you only the basic
functionality.

<img alt="5SDMlXTJxv"
src="https://github.com/tgstation/tgstation/assets/3625094/b9364230-49ac-416b-aa70-e851fbf2050e">

To compensate this change, all mechs got two extra utility module slots.

All other modules got new UI. And ore box now shows the list of ores
inside.

<img alt="SRX5FjvsHA"
src="https://github.com/tgstation/tgstation/assets/3625094/cbe2e98d-1cd4-4667-8dae-2f9227b4b265">

### Mounted Radio

Works as a normal radio, but with subspace transmission. Available from
the basic mech research node and can be printed in fab.

### Cabin Sealing

To compensate for the lack of air tank by default, mechs with enclosed
cabin (e.g. all except Ripley) got an ability to toggle cabin exposure
to the outside air. Exiting the mech makes cabin air automatically
exposed.

When you seal the cabin, it traps some of the outside air inside the
cabin and you can breathe with this air to perform a short space trips.
But the oxygen will run out quickly and CO2 will build up.

Sealing the cabin in space will make the cabin filled with vacuum, and
it will stay there until you return to air environment and unseal the
cabin, letting the breathable air to enter. There are temperature and
pressure sensors that turn yellow/red when the corresponding warning
thresholds are reached.

You could also use personal internals in combination with cabin sealing
for long space travels, so Air Tank is completely optional now and
mostly needed when you need RCS thruster.

### RCS thrusters

They are now available earlier in tech tree and consume reasonable
amount of air (5 times more than human jetpacks), and they don't work
without Mounted Air Tank, unless it's an Ion thruster variant.

### Mounted Air Tank

Available from the basic mech research node and can be printed in fab.
Built model comes empty, and syndicate mechs come with one full of
oxygen.

<img alt="GrFDrH5Hwe"
src="https://github.com/tgstation/tgstation/assets/3625094/b677b705-bda0-4c8c-96c7-d32bf7bf9f28">

Can be switched to pressurize or not pressurize the cabin. Releases gas
only when the cabin is sealed shut. Starts releasing automatically, but
can be toggled to not release if you want to use it just as a portable
canister.

Cabin pressure can now be configured in the module UI instead of
Maintenance UI.

Can be attached to a pipe network when the mech is parked above a
connection port.

Comes with a pump that works similarly to the portable pump. It lets you
vent the air tank contents outside, or suck air from the room to fill
the air tank. Intended to provide an ability to fill the air tank
without the need to bother with pipes.

Also has gas sensors that display gas mix data of the tank and the cabin
(when sealed).

### Stock part changes

All mechs now require a servo motor and they reduce mech movement power
consumption instead of scanning module.

Scanning modules are optional for mech operation (still required to
build) and the lack of one disables the following UI elements:

- Display of mech integrity (you can still see the alerts or examine the
mech to get rough idea)
- Display of mech status on internal damage (and you can't repair what
you can't diagnose)

The rating of scanning module doesn't have any effect as of now.

Cargo mech comes without it roundstart.

<img alt="2vDtt99oqb"
src="https://github.com/tgstation/tgstation/assets/3625094/147144ca-824e-4501-acf5-6ee104f309e7">

Capacitors now also reduce light power usage and raise the overclocking
temperature thresholds (see below).

### Maintenance

Maintenance UI removed, and its logic migrated to other places.

Access modification now managed inside the mech, and anyone who can
control the mech, can adjust the access in the same way as they can set
DNA key.

To open the maintenance panel you just need a screwdriver. It is instant
when the mech is empty and it has a 5 second delay when there is an
occupant to avoid in-combat hacking and part removal. It will alert the
occupant that someone is trying to tinker with their mech.


![image](https://github.com/tgstation/tgstation/assets/3625094/1abfca3c-8ba9-44b0-913c-c209564b91fd)

Once the panel is open, you can see the part ratings:


![image](https://github.com/tgstation/tgstation/assets/3625094/404f95bb-9f74-4e5b-a975-5ab6f74bdfa9)

With open panel you can hack the mech wires (roboticists can now see
them):

<img alt="mj205G2qDa"
src="https://github.com/tgstation/tgstation/assets/3625094/44cea0d1-44b4-4b50-b1d3-a97c0056bab3">

There are wires for:
- Enabling/Disabling ID and DNA locks
- Toggling mech lights
- Toggling mech circuits malfunction (battery drain, sparks) 
- Toggling mech equipment malfunction (to repair after EMP or cause
EMP-like effect, disarming mech)
- 3 dud wires that do nothing

The hacker may be shocked if the mech power cell allows.

When the panel is open and the user has access to the mech, they can
remove parts with a crowbar:

<img alt="jR40gyTWtJ"
src="https://github.com/tgstation/tgstation/assets/3625094/b573f5b9-b8ea-412e-b3e0-c872e01e0c23">

Hitting the mech with an ID from outside now toggles the ID Lock on/off
if the ID has sufficient access.

### Power consumption and overclocking

Rebalanced mech power consumption. T4 parts were not working in
Syndicate Mechs, as their effect was not calculated until you manipulate
parts manually. Constructed mechs with t1 parts even had their energy
drain reduced with upgrade to t1.

Now all mechs apply their base step power usage correctly don't ignore
the stock parts.

Servo tier now reduces base power consumption by 0% at t1, 50% at t2,
33% at t3 and 25% at t4
Capacitor tier now reduces base power consumption of mele attacks,
phasing and light by the same amounts.

Gygax leg actuators overload replaced with mech overclocking. Any mech
can be overclocked by hacking wires, but only Gygax has a button for
toggling it from the Cabin.

Now there is an overclock coefficient. 1.5 for Gygax and other mechs, 2
for Dark Gygax.

When overclocked, mechs moves N times faster, but consumes N times more
power.


![image](https://github.com/tgstation/tgstation/assets/3625094/01e285fd-6fd6-4558-8277-2ed3abf474d8)

While overclocked, mech heats up every second, regardless of movement,
and starts receiving internal and integrity damage after a certain
temperature threshold. The chance is 0% at the threshold, and 100% at
thresholds * 2. The roll happens every tick. Capacitor upgrades this
threshold, letting you overclock safely for longer periods.


![image](https://github.com/tgstation/tgstation/assets/3625094/80d90cea-0d20-4054-9369-a47deb6f52f2)

When you stop overclock, the temperature goes back down.

### Other changes and fixes

Concealed weapon bay now doesn't show up when you examine the mech, so
it's actually concealed now.

New radio module can properly change its frequency, as it didn't work
for previous radio.

Launcher type weapons were ignoring cooldowns and power usage, so you
could spam explosive banana peals, while they should have a 2 second
cooldown:
<img alt="q5GjUsHwGr"
src="https://github.com/tgstation/tgstation/assets/3625094/d102725d-e9e1-4588-9d6c-b9e38b7a6535">

Now this is fixed and all launcher type weapons properly use power and
have their cooldowns working.
And now they have the kickback effect working (when it pushes you in the
opposite direction in zero gravity on throw).

Thermoregulator now heats/cools considering heat capacity instead of
adding/reducing flat 10 degrees. So you can heat up cabin air quicker if
the pressure is low.

There were some other sloppy mistakes in mech code, like some functions
returning too early, blocking other functionality unintentionally. Fixed
these and made some other minor changes and improvements.

## Changelog

:cl:
refactor: Refactored Mech UI
refactor: Refactored mech radio into a utility module, adding extra slot
to all mechs
refactor: Refactored mech air tank into a utility module with an air
pump, adding extra slot to all mechs
refactor: Refactored mech cabin air - there is now a button to seal or
unseal cabin to make it airtight or exchanging gases with the
environment
refactor: Removed mech maintenance UI Access is set in mech UI, and
parts are ejected with a crowbar
add: Mech now has wires and can be hacked
qol: Roboticists now can see MOD suit and mech wires
add: Mechs now require servo motor stock part and it affects movement
power usage instead of scanning module
add: Scanning module absence doesnt block mech movement and hides some
UI data instead. Big Bess starts without one.
qol: Hitting mech with ID card now toggles ID lock on/off if the card
has required access
fix: Fixed concealed weapon bay not being concealed on mech examine
fix: Fixed mech radio not changing frequency
fix: Fixed mech launcher type weapons ignoring specified cooldown
fix: Fixed mech launcher type weapons not using specified power amount
fix: Fixed mech temperature regulator ignoring gas heat capacity
fix: Fixed mech stopping processing other things while not heating
internal air
fix: Fixed mech being able to leave transit tube in transit
fix: Fixed mech internal damage flags working incorrectly
fix: Fixed Gygax leg overloading being useless
fix: Fixed mechs ignoring their stock parts on creation. Syndicate mechs
now stronger against lasers and consume less energy on move. Upgrading
from tier 1 to tier 2 doesn't make mech consume MORE energy than before
the upgrade.
balance: Rebalanced mech energy drain with part upgrades. Base energy
drain reduced by 50%, 33%, 25% with upgrades and applies to movement
(Servo rating), phasing, punching, light (Capacitor rating).
balance: Hydraulic clamp now can force open airlocks
balance: Made mech RCS pack consume reasonable amount of gas
code: Fixed some other minor bugs and made some minor changes in the
mech code
/:cl:

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [peterhuene/wasmtime](https://github.com/peterhuene/wasmtime)@[1efee4abdf...](https://github.com/peterhuene/wasmtime/commit/1efee4abdfdb48b694828f0dc2ead394ba42a234)
#### Saturday 2023-08-19 18:49:34 by Alex Crichton

Update CI to use GitHub's Merge Queue (#5766)

GitHub recently made its merge queue feature available for use in public
repositories owned by organizations meaning that the Wasmtime repository
is a candidate for using this. GitHub's Merge Queue feature is a system
that's similar to Rust's bors integration where PRs are tested before
merging and only passing PRs are merged. This implements the "not rocket
science" rule where the `main` branch of Wasmtime, for example, is
always tested and passes CI. This is in contrast to our current
implementation of CI where PRs are merged when they pass their own CI,
but the code that was tested is not guaranteed to be the state of `main`
when the PR is merged, meaning that we're at risk now of a failing
`main` branch despite all merged PRs being green. While this has
happened with Wasmtime this is not a common occurrence, however.

The main motivation, instead, to use GitHub's Merge Queue feature is
that it will enable Wasmtime to greatly reduce the amount of CI running
on PRs themselves. Currently the full test suite runs on every push to
every PR, meaning that our workers on GitHub Actions are frequently
clogged throughout weekdays and PRs can take quite some time to come
back with a successful run. Through the use of a Merge Queue, however,
we're able to configure only a small handful of checks to run on PRs
while deferring the main body of checks to happening on the
merge-via-the-queue itself. This is hoped to free up capacity on CI and
overall improve CI times for Wasmtime and Cranelift developers.

The implementation of all of this required quite a lot of plumbing and
retooling of our CI. I've been testing this in an [external
repository][testrepo] and I think everything is working now. A list of
changes made in this PR are:

* The `build.yml` workflow is merged back into the `main.yml` workflow
  as the original reason to split it out is not longer applicable (it'll
  run on all merges). This was also done to fit in the dependency graph
  of jobs of one workflow.

* Publication of the `gh-pages` branch, the `dev` tag artifacts, and
  release artifacts have been moved to a separate
  `publish-artifacts.yml` workflow. This workflow runs on all pushes to
  `main` and all tags. This workflow no longer actually preforms any
  builds, however, and relies on a merge queue or similar being used for
  branches/tags where artifacts are downloaded from the workflow run to
  be uploaded. For pushes to `main` this works because a merge queue is
  run meaning that by the time the push happens all artifacts are ready.
  For release branches this is handled by..

* The `push-tag.yml` workflow is subsumed by the `main.yml` workflow. CI
  for a tag being pushed will upload artifacts to a release in GitHub,
  meaning that all builds must finish first for the commit. The
  `main.yml` workflow at the end now scans commits for the preexisting
  magical marker and pushes a tag if necessary.

* CI is currently a flat list of "run all these jobs" and this is now
  rearchitected to a "fan out" approach where some jobs run to determine
  the next jobs to run which then get "joined" into a finish step. The
  purpose for this is somewhat nuanced and this has implications for CI
  runtime as well. The Merge Queue feature requires branches to be
  protected with "these checks must pass" and then the same checks are
  gates both to enter the merge queue as well as pass the merge queue.
  The saving grace, however, is that a "skipped" check counts as
  passing, meaning checks can be skipped on PRs but run to completion on
  the merge queue. A problem with this though is the build matrix used
  for tests where PRs want to only run one element of the build matrix
  ideally but there's no means on GitHub Actions right now for the
  skipped entries to show up as skipped easily (or not that I know of).
  This means that the "join" step serves the purpose of being the single
  gate for both PR and merge queue CI and there's just more inputs to it
  for merge queue CI. The major consequence of this decision is that
  GitHub's actions scheduling doesn't work out well here. Jobs are
  scheduled in a FIFO order meaning that the job for "ok complete the CI
  run" is queued up after everything else has completed, possibly
  after lots of other CI requests in the middle for other PRs. The hope
  here is that by using a merge queue we can keep CI relatively under
  control and this won't affect merge times too much.

* All jobs in the `main.yml` workflow will not automatically cancel the
  entire run if they fail. Previously this fail-fast behavior was only
  part of the matrix runs (and just for that matrix), but this is
  required to make the merge queue expedient. The gate of the merge
  queue is the final "join" step which is only executed once all
  dependencies have finished. This means, for example, that if rustfmt
  fails quickly then the tests which take longer might run for quite
  awhile before the join step reports failure, meaning that the PR sits
  in the queue for longer than needed being tested when we know it's
  already going to fail. By having all jobs cancel the run this means
  that failures immediately bail out and mark the whole job as
  cancelled.

* A new "determine" CI job was added to determine what CI actually needs
  to run. This is a "choke point" which is scheduled at the start of CI
  that quickly figures out what else needs to be run. This notably
  indicates whether large swaths of ci (the `run-full` flag) like the
  build matrix are executed. Additionally this dynamically calculates a
  matrix of tests to run based on a new `./ci/build-test-matrix.js`
  script. Various inputs are considered for this such as:

  1. All pushes, meaning merge queue branches or release-branch merges,
     will run full CI.
  2. PRs to release branches will run full CI.
  3. PRs to `main`, the most common, determine what to run based on
     what's modified and what's in the commit message.

  Some examples for (3) above are if modifications are made to
  `cranelift/codegen/src/isa/*` then that corresponding builder is
  executed on CI. If the `crates/c-api` directory is modified then the
  CMake-based tests are run on PRs but are otherwise skipped.
  Annotations in commit messages such as `prtest:*` can be used to
  explicitly request testing.

Before this PR merges to `main` would perform two full runs of CI: one
on the PR itself and one on the merge to `main`. Note that the one as a
merge to `main` was quite frequently cancelled due to a merge happening
later. Additionally before this PR there was always the risk of a bad
merge where what was merged ended up creating a `main` that failed CI to
to a non-code-related merge conflict.

After this PR merges to `main` will perform one full run of CI, the one
as part of the merge queue. PRs themselves will perform one test job
most of the time otherwise. The `main` branch is additionally always
guaranteed to pass tests via the merge queue feature.

For release branches, before this PR merges would perform two full
builds - one for the PR and one for the merge. A third build was then
required for the release tag itself. This is now cut down to two full
builds, one for the PR and one for the merge. The reason for this is
that the merge queue feature currently can't be used for our
wildcard-based `release-*` branch protections. It is now possible,
however, to turn on required CI checks for the `release-*` branch PRs so
we can at least have a "hit the button and forget" strategy for merging
PRs now.

Note that this change to CI is not without its risks. The Merge Queue
feature is still in beta and is quite new for GitHub. One bug that
Trevor and I uncovered is that if a PR is being tested in the merge
queue and a contributor pushes to their PR then the PR isn't removed
from the merge queue but is instead merged when CI is successful, losing
the changes that the contributor pushed (what's merged is what was
tested). We suspect that GitHub will fix this, however.

Additionally though there's the risk that this may increase merge time
for PRs to Wasmtime in practice. The Merge Queue feature has the ability
to "batch" PRs together for a merge but this is only done if concurrent
builds are allowed. This means that if 5 PRs are batched together then 5
separate merges would be created for the stack of 5 PRs. If the CI for
all 5 merged together passes then everything is merged, otherwise a PR
is kicked out. We can't easily do this, however, since a major purpose
for the merge queue for us would be to cut down on usage of CI builders
meaning the max concurrency would be set to 1 meaning that only one PR
at a time will be merged. This means PRs may sit in the queue for awhile
since previously many `main`-based builds are cancelled due to
subsequent merges of other PRs, but now they must all run to 100%
completion.

[testrepo]: https://github.com/bytecodealliance/wasmtime-merge-queue-testing

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b0ec1e4098...](https://github.com/tgstation/tgstation/commit/b0ec1e4098ed80fdb0bac69c6f950bd5e38012b8)
#### Saturday 2023-08-19 19:13:49 by Jacquerel

[no gbp] Adds missing chat feedback to watcher abilities (#77700)

## About The Pull Request

I kept meaning to add this in my last PR and kept thinking "I'll add
that in with these review changes" and then forgot every time. This
should make it clearer what is happening to you and why.

Also I made the gaze ability stun the user for a short period after it
goes off because them shooting you instantly after they stop channeling
_is_ sort of bullshit.
Also while testing this I noticed the AI interrupt one of its actions to
do the other one which is a bit silly so now it cannot do that.

## Why It's Good For The Game

Outlines in the log why something bad just happened to you.

## Changelog

:cl:
qol: Added some textual feedback to new watcher abilities
balance: Watchers will not attack for a short period following their
gaze attack
fix: Watchers won't interrupt one ability to use the other one
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[9c0a04b33a...](https://github.com/treckstar/yolo-octo-hipster/commit/9c0a04b33a39e6945cb3e546b317c4c63ea47372)
#### Saturday 2023-08-19 19:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [UConnAI/uconnai.github.io](https://github.com/UConnAI/uconnai.github.io)@[a9df09aeb8...](https://github.com/UConnAI/uconnai.github.io/commit/a9df09aeb8a7004bcc3a117a04f5f071c538a249)
#### Saturday 2023-08-19 19:25:25 by m4nik1

Revert "Added Components, CSS, Pages for organization and created page files also wired the website to go straight to Homepage also (Fuck you Ronak)"

This reverts commit 5302e011c2a8436d69e2cce7e0e53df42701139f.

---
## [UConnAI/uconnai.github.io](https://github.com/UConnAI/uconnai.github.io)@[e162785162...](https://github.com/UConnAI/uconnai.github.io/commit/e1627851626c0951931b607aee0026732b900169)
#### Saturday 2023-08-19 19:25:25 by m4nik1

Added CSS, pages, component folders and added navigationbar file also Fuck you Ronak

---
## [donvito007/Xiaomi_sm8250_N0Kernel](https://github.com/donvito007/Xiaomi_sm8250_N0Kernel)@[efc24fba1b...](https://github.com/donvito007/Xiaomi_sm8250_N0Kernel/commit/efc24fba1b039210f786cfe7f2fa1e7ffe94fdba)
#### Saturday 2023-08-19 19:53:10 by Wang Han

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

---
## [rashimall/CODSOFT-WEB-DEVELOPMENT-INTERNSHIP](https://github.com/rashimall/CODSOFT-WEB-DEVELOPMENT-INTERNSHIP)@[a96448fa1e...](https://github.com/rashimall/CODSOFT-WEB-DEVELOPMENT-INTERNSHIP/commit/a96448fa1e018c81edf69b625114ee7f2246aa48)
#### Saturday 2023-08-19 20:46:01 by Rashi Mall

Create README.md

I have completed tasks given for my internship as a Web Developer in CodSoft. I hope it will be helpfull for you.

(Level 1)

Task 1:- LANDING PAGE A landing page is an ideal web development project for beginners. It requires basic knowledge of HTML and CSS. Through this project, you'll learn to create columns, divide sections, arrange items, and add headers and footers. The most important aspect is unleashing your creativity to design an impressive page. Pay attention to alignments, padding, color palette, boxes, and other elements. Be mindful of CSS to avoid overlapping elements. In short, a landing page project allows you to apply HTML and CSS skills, encouraging your creativity while ensuring a visually appealing and user-friendly design.

Task 2:- PORTFOLIO PAGE Creating a personal portfolio using CSS and HTML is a popular beginner web development project. Header Section: Add your name or a logo at the top. Optionally, include a brief introduction or tagline. About Section: Insert an image of yourself. Write a short bio highlighting your skills and experience. Skills Section: List your key skills or areas of expertise. Projects Section: Showcase samples of your work or projects. Include project titles, descriptions, and images. Resume Section: Provide a link to download your resume in PDF format. Contact Section: Include your contact information, such as email address and phone number. Footer: Add a copyright notice and any additional links or information.

Task 3:- CALCULATOR To create a basic calculator using CSS, HTML, and JavaScript, you'll need to implement an interactive interface with buttons for addition, subtraction, multiplication, and division operations. The calculator should have a display screen to show user input and results. Utilize CSS grid system for button alignments. Use event listeners, if-else statements, operators, and loops to handle user input and perform calculations. This project requires some skill but can be done with basic knowledge of these technologies.

---
## [Bjamcham/Paradise](https://github.com/Bjamcham/Paradise)@[2d10818063...](https://github.com/Bjamcham/Paradise/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Saturday 2023-08-19 21:29:20 by ATP-Engineer

Fixes IV bag blood overlays being too damn bright for some mixtures (#21813)

* Removes old .dmi

* Fixes blood overlay coloring being too bright for IV bags

* Fine-tuning

* Makes the blood bag IV color overlays not as bright as they used to be

In hindsight it was probably easy to avoid

* FINAL TUNE UP

FUCK

* Fixes coloring for IV bags so they're not too bright

FINAL COMMIT

---
## [adump1v/platform_frameworks_base](https://github.com/adump1v/platform_frameworks_base)@[8d45440c76...](https://github.com/adump1v/platform_frameworks_base/commit/8d45440c7610a20cb7dc963b500e69a998fdabdb)
#### Saturday 2023-08-19 22:24:24 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[abaf3925d2...](https://github.com/diphons/D8G_Kernel_oxygen/commit/abaf3925d238f991a65d9538c2403f81ace0f671)
#### Saturday 2023-08-19 23:01:07 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>
Signed-off-by: Forenche <prahul2003@gmail.com>

---
## [MattJBrinkman/RedemptionLackeyCCG](https://github.com/MattJBrinkman/RedemptionLackeyCCG)@[c8d360a9e6...](https://github.com/MattJBrinkman/RedemptionLackeyCCG/commit/c8d360a9e69a92ac827cac3a1cf6b86adc54b534)
#### Saturday 2023-08-19 23:05:38 by jalstad

Added Images and Modded Carddata

Added card images and carddata.txt information for Israel's Rebellion set, War in Heaven promo, and Angel of God promo.

Made a few corrections to previously added cards in carddata.txt

Added/replaced a few pack images for whatever those are used for.

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[9db2f06363...](https://github.com/yogstation13/Yogstation/commit/9db2f06363bc325a0e8eadfdf7266e55def4d7c1)
#### Saturday 2023-08-19 23:15:54 by Scrambledeggs

Fuck you *Ungreens your Peacekeepers* (#20053)

* Sprites Part 1: I hate transparency

* Sprites Part 2: Electric Booogaloo

* lack of transparency fixed

* More sprite fixes

* Tacmask and sprites

* Tacprod inactive and nocell sprites

* Tacprod Animation Part 1: Bugs galore

* Tacprod Animation Part 2: Tacmask revengance

* white beret

---

