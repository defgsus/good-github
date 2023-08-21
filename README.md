## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-20](docs/good-messages/2023/2023-08-20.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,912,802 were push events containing 2,611,393 commit messages that amount to 139,816,219 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [kd-collective/react](https://github.com/kd-collective/react)@[ac1a16c67e...](https://github.com/kd-collective/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Sunday 2023-08-20 00:20:12 by Sebastian Markbåge

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
## [pinkkea/ReginaBotTEST](https://github.com/pinkkea/ReginaBotTEST)@[b6cfd31ab2...](https://github.com/pinkkea/ReginaBotTEST/commit/b6cfd31ab23fd22582666cbe3ce45250b768454a)
#### Sunday 2023-08-20 00:28:05 by pinkkea

fuck I forgot to take otu the token LOOOOOOL ok its been reset nbd GOD DAMN IT

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[b0ec1e4098...](https://github.com/Ical92/tgstation/commit/b0ec1e4098ed80fdb0bac69c6f950bd5e38012b8)
#### Sunday 2023-08-20 00:28:19 by Jacquerel

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
## [Remis932/cope-mod](https://github.com/Remis932/cope-mod)@[6cf2c728c9...](https://github.com/Remis932/cope-mod/commit/6cf2c728c9b67f1a6ce0694cbf8a81eedc7eb228)
#### Sunday 2023-08-20 00:53:15 by SGTDaveVader

Bruh

I hate what Pogba did to Poland, this is some GFM level event gay shit.
Anyone with half a braincell knows events suck ass, its impossible to make sense of this fucking tree. You need a fucking excel spreadsheet to understand what the fuck is even happening. Like there is straight up no explanation too, in literally every mp game the Poland player just gets stuck with a Silean and Hungarian Puppet and his starting land and cant do shit the entire game because half his country is owned by the ai. Like fucking hell is it really so hard to just make 5 decisions that have an explanation in their description if they are mutually exclusive? Or atleast give a starting event that explains the situation and the paths. This shit is so fucking retarded, whoever made this should kys.

---
## [Apogee-dev/Shiptest](https://github.com/Apogee-dev/Shiptest)@[ee4021c507...](https://github.com/Apogee-dev/Shiptest/commit/ee4021c50792c11bfd21085156edd32200c21cb8)
#### Sunday 2023-08-20 01:02:43 by Imaginos16

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
## [SatwikJha55/GeeksForGeeksPOTDDiscussion](https://github.com/SatwikJha55/GeeksForGeeksPOTDDiscussion)@[e56857ee0a...](https://github.com/SatwikJha55/GeeksForGeeksPOTDDiscussion/commit/e56857ee0a6f5783df846b7a749ad80fe7905509)
#### Sunday 2023-08-20 01:05:58 by SatwikJha

Update README.md

Welcome to the Geeks For Geeks Problem of the Day (POTD) Discussion repository on GitHub! This repository serves as a hub for geeks, developers, and coding enthusiasts who are passionate about improving their problem-solving skills, algorithmic thinking, and coding expertise.

Every day, the Geeks For Geeks team presents a challenging coding problem as the Problem of the Day. These problems cover a wide range of topics including data structures, algorithms, dynamic programming, graph theory, and more. Solving these problems not only sharpens your coding skills but also enhances your understanding of core computer science concepts.

In this repository, you'll find a dedicated discussion thread for each daily POTD. This is where you can engage with fellow programmers, share your thought processes, discuss different approaches, and collaborate to find the most efficient solutions. Whether you're a beginner seeking guidance or an experienced coder looking to exchange insights, this is the place to be.

Here's what you can expect from this repository:

1. **Daily Problem Discussions**: A new discussion thread will be created for each day's POTD. Feel free to share your ideas, ask questions, and learn from others' strategies. Don't hesitate to provide hints and explanations to help your fellow programmers grow.

2. **Variety of Approaches**: Coding problems often have multiple solutions. Explore different approaches shared by the community. Discuss the pros and cons of each approach and learn to choose the most appropriate one for various scenarios.

3. **Learning Opportunities**: Engaging in discussions exposes you to diverse perspectives and problem-solving techniques. By participating actively, you'll not only solve problems but also enhance your problem-solving toolkit.

4. **Collaborative Environment**: Collaboration is key in the world of programming. Contribute to discussions, provide feedback, and build connections with programmers from around the globe.

5. **Guidelines and Respectful Interaction**: To ensure a productive and respectful environment, please adhere to the repository's guidelines. Be polite, avoid spoilers, and maintain the focus on learning and constructive discussions.

Remember, the journey of mastering coding and algorithms is ongoing, and every small step you take contributes to your growth. So, dive into the Geeks For Geeks POTD Discussion repository, share your knowledge, seek guidance, and together, let's unravel the fascinating world of coding challenges!

Happy coding!
The Geeks For Geeks Team

---
## [francinum/Therac-Gameserver](https://github.com/francinum/Therac-Gameserver)@[27d37cb0f4...](https://github.com/francinum/Therac-Gameserver/commit/27d37cb0f47d007d1159ad5af69ace39a50b003f)
#### Sunday 2023-08-20 01:55:41 by Gallyus

Alternate Version Tests (#281)

* AltVer Checks
I think?
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* 1603 target

* support script

* HOLY SHIT CAN I READ

* e

* HOLY FUCK CAN I READ

* Disable shortkill version check

---
## [stepbrobd/nix](https://github.com/stepbrobd/nix)@[b13fc7101f...](https://github.com/stepbrobd/nix/commit/b13fc7101fb06a65935d145081319145f7fef6f9)
#### Sunday 2023-08-20 02:19:07 by Robert Hensing

Add positive source filter

Source filtering is a really cool Nix feature that lets us avoid a
lot of rebuilds, which speeds up the iteration cycle a lot in cases
where the relevant source files aren't actually modified.

We used to have a source filter that marked a few files as irrelevant,
but this is the wrong approach, as we have many more files that are
irrelevant. We may call this negative filtering.

This commit switches the source filtering to positive filtering, which
is a lot more robust. Instead of marking which files we don't need
we marked the files that we do need.

It's a superior approach because it is fail safe. Instead of allowing
build performance problems to creep in over time, we require that all
source inputs are declared.

I shouldn't have to explain that declaring inputs is a good practice,
so I'll stop over-explaining here.

I do have to acknowledge that this will cause a build failure when the
filter is incomplete. This is *good*, because it's the only realistic
way we could be reminded of these problems. These events will be
infrequent, so the small cost of extending the filter is worth it,
compared to the hidden cost of longer dev cycles for things like tests,
docker image, etc, etc.

(Also rebuilding Nix for stupid unnecessary reasons makes my blood boil)

---
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[6c34d93be7...](https://github.com/dragomagol/tgstation/commit/6c34d93be715012943626d0f812e99f730a536ef)
#### Sunday 2023-08-20 02:34:05 by necromanceranne

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
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[3dc75f84f2...](https://github.com/dragomagol/tgstation/commit/3dc75f84f2eebc388c7f698284d77df4d8cf8fdf)
#### Sunday 2023-08-20 02:34:05 by YakumoChen

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
## [dragomagol/tgstation](https://github.com/dragomagol/tgstation)@[95ec0e6545...](https://github.com/dragomagol/tgstation/commit/95ec0e65458ece9c5c80952e75d5d32c4fbb794b)
#### Sunday 2023-08-20 02:34:05 by necromanceranne

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
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[dcd2d0e418...](https://github.com/Paxilmaniac/Skyrat-tg/commit/dcd2d0e418fbd85c3e990a02f61ab05d2993e1e1)
#### Sunday 2023-08-20 03:33:47 by SkyratBot

[MIRROR] Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station [MDB IGNORE] (#22637)

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station (#76974)

## About The Pull Request

This PR adds a new wizard ritual (the kind that require 100 threat on
dynamic)

This ritual allows the wizard to select one spellbook entry (item or
spell), to which everyone on the station will be given or taught said
spell or item. If the spell requires a robe, the spell becomes robeless,
and if the item requires wizard to use, it makes it usable. Mostly.

- Want an epic sword fight? Give everyone a high-frequency blade

- One mindswap not enough shenanigans for you? Give out mindswap

- Fourth of July? Fireball would be pretty hilarious...

The wizard ritual costs 3 points plus the cost of whatever entry you are
giving out. So giving everyone fireball is 5 points.

It can only be cast once by a wizard, because I didn't want to go
through the effort to allow multiple in existence

## Why It's Good For The Game

Someone gave me the idea and I thought it sounded pretty funny as an
alternative to Summon Magic

Maybe I make this a Grand Finale ritual instead / in tandem? That's also
an idea.

## Changelog

:cl: Melbert
add: Wizards have a new Right and Wrong: Mass Teaching, allowing them to
grant everyone on the station one spell or relic of their choice!
/:cl:

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [unit0016/effigy-se](https://github.com/unit0016/effigy-se)@[2d34c7433a...](https://github.com/unit0016/effigy-se/commit/2d34c7433a0c5315e6a46f7e32e2c9a6c90280b3)
#### Sunday 2023-08-20 03:51:06 by Andrew

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
## [kishorekandregula/kishorekandregula](https://github.com/kishorekandregula/kishorekandregula)@[f15d2dd03e...](https://github.com/kishorekandregula/kishorekandregula/commit/f15d2dd03e867d5ab515fccba35710fbf0cfc3cd)
#### Sunday 2023-08-20 04:48:28 by kishorekandregula

Update README.md

As a seasoned DevOps Engineer with more than three years of experience, I have a proven track record of implementing and managing robust infrastructure solutions. My expertise lies in using various DevOps tools, including Git, Maven, Jenkins, Docker, Kubernetes, Ansible, Terraform, SonarQube, and Nexus, to streamline the software development life cycle.

Throughout my career, I have successfully managed complex cloud environments, automated deployment processes, and optimized infrastructure performance. I have also been responsible for ensuring the security and compliance of the environments I manage.

As a collaborative team player, I work closely with cross-functional teams to ensure the delivery of high-quality products. My strong analytical skills and attention to detail have enabled me to identify and resolve critical issues quickly and efficiently.

If you're looking for a skilled DevOps Engineer who can help you deliver reliable and scalable infrastructure solutions, I would love to discuss how my experience and expertise can benefit your organization.

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[66b8748091...](https://github.com/JohnFulpWillard/tgstation/commit/66b87480915434f1184ac257c9ed0f1f3fe87c58)
#### Sunday 2023-08-20 05:20:25 by carlarctg

Adds Summon Simians & Buffs/QoLs Mutate (#77196)

## About The Pull Request

Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

Added further support for nonhuman robed casting: Monkeys, cyborgs, and
drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

Made monkeys able to wield things again.

Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.

Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Improved some monkey AI code.

## Why It's Good For The Game

> Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.

It's criminal we don't have a monky spell, and this is a really fun spin
on it. Total chaos, but total monky chaos. It's surprisingly strong,
but! it can very well backfire if you stay near the angry monkeys too
long and your protection fades away. Unless you become a monkey
yourself!!

> Wizard Mutate spell works on non-human races. 

This spell is great but it's hampered by the mutation's human
requirement, which is reasonable in normal gameplay. Wizards don't need
to care about that, and the human restriction hinders a lot of possible
gimmicks, so off it goes. Also, wizard hulk does't cause chunky fingers
for similar reasons

> Made Laser eyes projectiles a subtype of actual lasers, which has
various properties such as on-hit effects and upping the damage to 30.

Don't really caer about the damage so much, this is more so that it has
effects such as on-hit visuals. Can lower the damage if required, but
honestly anything that competes against troll mjolnir is good.

> Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.

SS13 is known for 'The Dev Team Thinks of Everything' and I believe this
is a sorely lacking part of this or something. It's funny.
I want to see a monkey wizard.

> Made monkeys able to wield things again.

I really don't know why this was a thing and it was breaking my axe and
spear wielding primal monkeys. Like, why?

## Changelog

:cl:
add: Adds Summon Simians, a spell that summons four monkeys or lesser
gorillas, with the amount increasing per upgrade. The monkeys have
various fun gear depending on how lucky you get and how leveled the
spell is. If the spell is maximum level, it only summons normal
gorillas.
balance: Wizard Mutate spell works on non-human races. It also gives you
Gigantism now (funny). If the Race can't support tinted bodyparts, your
whole sprite is temporarily turned green.
balance: Made Laser eyes projectiles a subtype of actual lasers, which
has various properties such as on-hit effects and upping the damage to
30.
add: Added further support for nonhuman robed casting: Monkeys, cyborgs,
and drones can all now cast robed spells as long as they're wearing a
wizardly hat as well.
balance: Made monkeys able to wield two-handed things again.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[87f707dfa8...](https://github.com/JohnFulpWillard/tgstation/commit/87f707dfa8dd901310f72585c6f701035bc653ee)
#### Sunday 2023-08-20 05:20:25 by DeerJesus

Adds the Storage Implanter to the spy kit. (#77452)

## About The Pull Request

Adds the storage implanter to the spy kit to make it decent.

## Why It's Good For The Game
This PR hopes to bring Spy at least a little more in-line with the rest
of the syndie-kit specials, so it doesn’t feel like a complete dud to
get.

Spy absolutely sucks as a syndie-kit and getting it is basically
throwing away 20 TC. Not all of them should be equally powerful but all
of them should be at least more satisfying to get. Spy is so bad that
it’s listed in the official wiki as ‘honestly not that good’. It’s also
_barely_ even above 25 telecrystals as the switchblade is a black market
uplink item, not a syndicate uplink item, and not even that good of an
item at that! And the chameleon kit inside isn’t even a full chameleon
kit! Pitiful. Compare it to stealth right below it which totals to _36_
telecrystals.

Adding a storage implant adds a relatively useful item to the kit that
still fits with the entire theme of ‘stealth and deception’, as you can
be searched without having anything on you. To be stealthy, and deceive
people. Like you should. Given the fact that searches are quite common.
It doesn’t make it TOO overpowered as the rest of the gear is still ‘not
that great’.


## Changelog

:cl:
balance: added the storage implanter to the syndie-kit tactical 'spy'
kit to make it decent.
/:cl:

Co-authored-by: oilysnake <63020759+oilysnake@users.noreply.github.com>

---
## [dgp1130/rules_prerender](https://github.com/dgp1130/rules_prerender)@[4ce322773c...](https://github.com/dgp1130/rules_prerender/commit/4ce322773c059c49ed12f66c28bc973a39447689)
#### Sunday 2023-08-20 05:24:52 by Doug Parker

Adds navigation panel to docs site.

Refs #16.

This was an interesting test case. The panel itself is relatively straightforward, with a hierarchy and expand/collapse behavior. I spent more time than I'd like to admit on the CSS animations trying to get an arrow to rotate, though I did eventually figure it out. The arrow does get noticeably blurry when animated, which is very strange. This behavior applies for Chrome and Firefox. Searching the internet, I found countless hacks which claim to fix this, but none of them worked for me. For the time being, I'm calling this a browser bug.

I also tried to animate the reveal of a route's children, however I decided this is not possible as animating to `height: auto;` is generally not feasible today without compromises I wasn't comfotable making. https://css-tricks.com/using-css-transitions-auto-dimensions/

Beyond the CSS, I think `@rules_prerender` did a good job allowing me to shape the structure of how I solved this particular solution. I was able to decouple routes from the `NavPane` component which made for easier testing. HydroActive was also pretty smooth, though it only binds an event listener and not much more. On its own, that was mostly fine. However testing got complicated _fast_. How and what to assert in a `node-html-parser` test is complicated, verbose, and tedious. I can definitely understand the appeal of snapshot testing, even if I don't think that's a good general solution to this problem. Testing the client code is even more complicated due to a separate `test_cases.tsx` file, multiple build targets, and then the WebDriver tests themselves. User code would need to go out of their way to set up WebDriverIO and Jasmine in addition to all this complexity. This could definitely use some streamlining.

Also I wonder if there might be a better testing approach with in-browser testing vs WebDriver testing. Could we render `test_cases.tsx` at build time, then instrument a test runner which serves them with Jasmine loaded in. If it auto-deferred the root component and ran test code inside the browse, we could take advantage of HydroActive test APIs. Need to think more about how viable this is and where tests would be most useful.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[354de24324...](https://github.com/git-for-windows/git/commit/354de2432449bff5f395149f3d79234ae6256cac)
#### Sunday 2023-08-20 05:31:05 by Johannes Schindelin

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

---
## [DataDog/go-httpbin](https://github.com/DataDog/go-httpbin)@[0de8ec9683...](https://github.com/DataDog/go-httpbin/commit/0de8ec968378e7385f2f9b10b6fe7a035fb27d8e)
#### Sunday 2023-08-20 06:05:06 by Will McCutchen

Refactor test suite to make real requests to a real server (#131)

In the course of validating #125, we discovered that using the stdlib's
[`httptest.ResponseRecorder`][0] mechanism to drive the vast majority of
our unit tests led to some slight brokenness due to subtle differences
in the way those "simulated" requests are handled vs "real" requests to
a live HTTP server, as [explained in this comment][1].

That prompted me to do a big ass refactor of the entire test suite,
swapping httptest.ResponseRecorder for interacting with a live server
instance via [`httptest.Server`][2].

This should make the test suite more accurate and reliable in the long
run by ensuring that the vast majority of tests are making actual HTTP
requests and reading responses from the wire.

Note that updating these tests also uncovered a few minor bugs in
existing handler code, fixed in a separate commit for visibility.

P.S. I'm awfully sorry to anyone who tries to merge or rebase local test
changes after this refactor lands, that is goign to be a nightmare. If
you run into issues resolving conflicts, feel free to ping me and I can
try to help!

[0]: https://pkg.go.dev/net/http/httptest#ResponseRecorder
[1]: https://github.com/mccutchen/go-httpbin/pull/125#issuecomment-1596176645
[2]: https://pkg.go.dev/net/http/httptest#Server

---
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[820c22a5f5...](https://github.com/Derpguy3/tgstation/commit/820c22a5f5381364c595d21b6c047e269f7f0497)
#### Sunday 2023-08-20 06:13:30 by DaydreamIQ

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
## [Derpguy3/tgstation](https://github.com/Derpguy3/tgstation)@[63f7eb1a6a...](https://github.com/Derpguy3/tgstation/commit/63f7eb1a6a01c0c48dcc075f57b58a662d27fc17)
#### Sunday 2023-08-20 06:13:30 by san7890

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
## [downthecrop/2009scape-mirror](https://github.com/downthecrop/2009scape-mirror)@[a105821427...](https://github.com/downthecrop/2009scape-mirror/commit/a105821427d9467b528a6ec7c882d98b6042d7c1)
#### Sunday 2023-08-20 07:25:05 by Zerken

Audio Refactor

1st of many audio refactors, the end goal is removing AudioManager.java and using contentAPI functions for all sound
Refactored playAudio
Refactored playGlobalAudio
Fixed lunar teleport sounds to not play if teleblocked
Refactored the following sounds:
All the special attack and DFS sounds defaulting to new API radius of 8 instead of 5
Dropping coins, item, and destroying object sounds fixed
Ectophial refill sound
Agility pyramid sounds
Emptying a fishbowl
Enchanted jewellery teleport sound
Enchanted jewellery enchant tab sound
All the sounds for Elemental Workshop 1 listeners
The sound when getting experience from a lamp
Blessing and repairing a grave
Hunter pitfall sounds
Hunter sound when catching a kebbit with a noose
Lunar cure me and cure group spell sound
High and low alchemy spells
Silver crafting at a furnace
Spinning at a spinning wheel
Drinking from a waterskin in the desert
Sound when being blessed by drezel in nature's spirit quest
Sound when poison immunity has 30 seconds left and when your immunity expires
Shearing regular sheep and the penguin sheep at lumbridge
Sound when regular spell book charge spell expires
GE sounds: making 0 coin offer when buying, not having enough money, placing a buy offer, not enough room in inventory
Sound when filling vessels from a water source
Regular and ancient combat spells

---
## [Vasanth-p/AtractivePortfolio](https://github.com/Vasanth-p/AtractivePortfolio)@[a32ed5f6f8...](https://github.com/Vasanth-p/AtractivePortfolio/commit/a32ed5f6f866143d90387ca57c4b98bb3b0ebdce)
#### Sunday 2023-08-20 07:39:34 by Vasanth P

Add files via upload

🚀 Welcome to My GitHub Portfolio: Where Innovation Meets Code

Hello there! 👋 Step into my digital realm, where lines of code converge to create extraordinary experiences. This is my GitHub portfolio—a dynamic showcase of my journey, creativity, and love for coding.

🌟 A Tapestry of Projects, A Symphony of Skills

Dive into a collection of meticulously crafted repositories that speak volumes about my coding prowess. From web applications that blend form and function seamlessly, to algorithms that dance through complexity with elegance, each repository is a testament to my dedication and adaptability.

🎨 Coding as an Art, Innovation as a Muse

Coding is my canvas, and innovation is my muse. As you explore my portfolio, you'll uncover not just projects, but stories—stories of challenges conquered, solutions engineered, and creative boundaries pushed. This is a place where imagination merges flawlessly with code.

🔍 More Than Just Code

Beyond the syntax and the pull requests, you'll find the heart and soul I've poured into my work. Each project is a chapter in my coding journey, a fusion of learning, curiosity, and endless cups of coffee. I believe that the best code is not just functional—it's expressive, elegant, and open to evolution.

🌐 Join Me on This Expedition

Embark on this journey with me as we navigate through the intricacies of code and the exhilaration of creation. Whether you're a fellow developer, an aspiring coder, or simply someone who appreciates the art of innovation, I invite you to explore, learn, and collaborate.

💌 Let's Connect

I'm excited to share my passion with you. Feel free to explore the projects, contribute your insights, or reach out for a chat. Together, we can turn lines of code into something truly remarkable.

---
## [UnsatifsedError/lineage_frameworks_base](https://github.com/UnsatifsedError/lineage_frameworks_base)@[cacaa8ac59...](https://github.com/UnsatifsedError/lineage_frameworks_base/commit/cacaa8ac59d6430b18aa065b47be25b5c6b83786)
#### Sunday 2023-08-20 07:39:47 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>
Signed-off-by: Sipun Ku Mahanta <sipunkumar85@gmail.com>

---
## [greengrill/Argonian-and-Khajiit-configs](https://github.com/greengrill/Argonian-and-Khajiit-configs)@[0df3e5fae2...](https://github.com/greengrill/Argonian-and-Khajiit-configs/commit/0df3e5fae26133fb0034e4ce1135dce858733d30)
#### Sunday 2023-08-20 08:33:24 by greengrill

Update README.md

Credits go to Pirana91 for making SynthEBD and the original texture artists:

MONSTERaider--made the original Feminine and Masculine beast race mods and the alternatives used in these configs.
riverbord--made the Riverborn Argonian textures for male and female.
KirillianAmurawr's--the creator of the big stupid lizards texture file.
Flewn--the creator of Flawn's Argonians--Lite, Redux and full.

---
## [ktlwjec0/Yogstation](https://github.com/ktlwjec0/Yogstation)@[9db2f06363...](https://github.com/ktlwjec0/Yogstation/commit/9db2f06363bc325a0e8eadfdf7266e55def4d7c1)
#### Sunday 2023-08-20 09:29:25 by Scrambledeggs

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
## [Admentus64/Patcher64Plus-Tool](https://github.com/Admentus64/Patcher64Plus-Tool)@[68229cbc34...](https://github.com/Admentus64/Patcher64Plus-Tool/commit/68229cbc34e5a994b736c272c6314c58683a44be)
#### Sunday 2023-08-20 09:42:02 by kuirivito

Version 20.3.7 - Gossip Stones Clock (#75)

* somewhat debugged text editor

fixes - multiple control bytes have now been fixed to be successfully read by the program

bugged - as it turns out if you try to edit ID 20D2 in the dialogue, things just break! it doesn't register properly at all

* Gossip Stone Clock feature implemented

....mostly. can't fully test until the SetMessage function has been debugged.

* update v20.3.7

planned to have my extra feature of having the Gossip Stones also have a regular day clock in addition to the time to moonfall clock

delayed until SetMessage function is debugged; current state prevents editing of the necessary dialogue ID for my feature

* fixed a couple female pronoun errors

There may be more, but i'm not doing that shit rn

* Finally. It's working.

Version 20.3.7 is ready to roll

---
## [ludup/hypersocket-framework](https://github.com/ludup/hypersocket-framework)@[5ddd85745c...](https://github.com/ludup/hypersocket-framework/commit/5ddd85745ced56915efc44fe90c27e1047253b00)
#### Sunday 2023-08-20 09:42:29 by brett-smith

The database optimisation work is done. I am pretty confident this is going to make a significant different to at least the general responsiveness of the UI. I am going to decribe the jounrney I went on to get here, in case I've broken anything, and to record a technique I used to discover where the problems were.

We started off needing the reduce these repeated and uncached queries, many of which run many hundreds of times as you navigate around the UI. The log fragment below shows the ones that seem to accumulate very quickly up into the thousands after less than a  minute of moving around the UI.

```
2333 select principal0_.resource_id as resource1_80_0_, principal0_1_.created as created2_80_0_, principal0_1_.deleted as  ...
2334 select authentica0_.resource_id as resource1_80_0_, authentica0_1_.created as created2_80_0_, authentica0_1_.deleted  ...
2335 select session0_.id as id1_93_0_, session0_.created as created2_93_0_, session0_.deleted as deleted3_93_0_, session0_ ...
2337 select realm0_.resource_id as resource1_80_0_, realm0_1_.created as created2_80_0_, realm0_1_.deleted as deleted3_80_ ...
2872 select allowedrol0_.resource_id as resource1_88_0_, allowedrol0_.role_id as role_id2_88_0_, role1_.resource_id as res ...
2872 select deniedrole0_.resource_id as resource1_89_0_, deniedrole0_.role_id as role_id2_89_0_, role1_.resource_id as res ...
2873 select permission0_.role_id as role_id1_83_0_, permission0_.permission_id as permissi2_83_0_, permission1_.id as id1_ ...
2873 select principals0_.role_id as role_id1_84_0_, principals0_.principal_id as principa2_84_0_, principal1_.resource_id  ...
2873 select realms0_.role_id as role_id2_85_0_, realms0_.principal_id as principa1_85_0_, realm1_.resource_id as resource1 ...
2874 select permission0_.role_id as role_id1_83_0_, permission0_.permission_id as permissi2_83_0_, permission1_.id as id1_ ...
2874 select principals0_.role_id as role_id1_84_0_, principals0_.principal_id as principa2_84_0_, principal1_.resource_id ...
2874 select realms0_.role_id as role_id2_85_0_, realms0_.principal_id as principa1_85_0_, realm1_.resource_id as resource1 ...
2880 select permission0_.category_id as category9_59_0_, permission0_.id as id1_59_0_, permission0_.id as id1_59_1_, permi ...
3153 select localuserc0_.id as id1_48_4_, localuserc0_.created as created2_48_4_, localuserc0_.deleted as deleted3_48_4_, ...
3159 select suspension0_.principal_id as principa5_100_0_, suspension0_.resource_id as resource4_100_0_, suspension0_.reso ...
```

These logs were obtained using the p6spy JDBC intercepting driver, which is better than the mariadb general query log, as we can easily apply filters locally and so narrow down the queries logged.

p6spy also allowed another very useful technique to actually track down where these queries coming from (our code, somewhere in spring / hibernate etc). It allows you to define a custom logger. I simply did so, and added conditions such as ..

```java
if(logText.startsWith("select session")) {
   System.out.println("Break!"); // <-- set breakpoint here
}
```

By setting a breakpoint here, I can see the full stack when that SQL query is about to be sent to the server. This ability has been absolutely essential.

As for the actual changes that result from this knowledge, there was no magic-bullet to fix it, there was no single cause for these. Each had to be analysed and dealt with appropriately.

One of these issues is the (over)use of `FetchType.EAGER`. It is now know that eager fetching defeats hibernate caching. In general, this is considered a code smell and indicates a design problems. Given enough time, all of these could probably be designed out, but that is not practical for this work. So instead I dealt with a couple of these in key places that were causing performance degradation.

The first of these was `AuthenticationScheme.allowedRoles` and `AuthenticationScheme.deniedRoles`. These are now using `FetchType.LAZY`. For this to work, a number of places that accessed these collections had to be changed to ensure that they were accessed in the context of a transaction. Fortunately there weren't too many of these.

Another use of eagar featch was in `Principal.suspensions`. This field was not used at all, so doesn't need eagar fetching anyway. It's possible that earlier versions did use this field, but I didn't persue it to find out what.

The remainder of the changes all either added or adjusted caching behaviour.

The first of these was `RealmService.getDefaultRealm()`. For some reason this wasn't being cached by hibernate, and it was difficult to see why. But this method was getting hit a lot, so I could add caching there. The cached default realm is cleared if the realm is changed or deleted. Caching this affects most page loads.

Another is `FileUploadService.getFileUpload`. The resulting `FileUpload` objects are now cached by UUID which is how they are nearly always accessed. Caching this particularly helps the user list page (with all its icons).

`PermissionService.getPersonalRole` is called a lot, and personal role objects were not being cached. They now are, with the cache being invalidated when the user or realm is deleted. Personal roles appear to be mostly immutable. Caching this affects most page loads.

`ConfigurationServiceImpl` now has a cache region for storing configuration. This one is not going to make a big as a difference as the others. I did see a number of occasions where hibernate cache was not working, but many cases where it was. It's still worth doing I think, as retrieving from our own cache will be a little faster than the more complex algorithm hibernate caching uses. Caches are invalidated when configuration changes or realm deletion.

If I now repeat that same log analysis from earlier in this post, we end up with this ..

```
979 select session0_.id as id1_93_0_, session0_.created as created2_93_0_, session0_.deleted as deleted3_93_0_, session0_.legacy_id
1046 select session0_.id as id1_93_0_, session0_.created as created2_93_0_, session0_.deleted as deleted3_93_0_, session0_.legac
1115 select session0_.id as id1_93_0_, session0_.created as created2_93_0_, session0_.deleted as deleted3_93_0_, session0_.legac
2623 select session0_.id as id1_93_0_, session0_.created as created2_93_0_, session0_.deleted as deleted3_93_0_, session0_.legac
```

A big improvement! But ... as you can see there is still one more table to go. This is to do with `Session` and `SessionServiceImpl.isLoggedOn()`. The problem here is that `SessionRepository.refresh()` is being called, which explicitly will always retrieve from the database. `isLoggedOn()` will get called at least once per request, so a single page load (with all of its resources) can potentially happen 100s of times.

This cannot be fixed by adding our own cache, and its not related to eager fetching. As far as I can make out, the refreshing is necessary because we store `Session` objects in the `HttpSession` (making them long lived), but potentially other places might alter the `Session`, e.g. logging it off, so we MUST ensure we have an up to date object for such important state. I believe this can be fixed by not storing the actual `Session` object in such cases, but instead storing it's ID. The session can then be looked up when it's needed, and hibernate caching will deal with ensuring it is fresh. I haven't done anything with this yet, as I could do with a 2nd opinion.

As I mentioned elsewhere, I have added a cache statistics pages. This will help us determine if caching is efficient. It would be interesting to see the hit/miss %ages on a busy system. A single user just navigating around the UI should show cache efficiency close to 100%, but I would expect the more users there are this will start to go down as the cache fills up to it's maximum size (100000 items) and things have to start being evicted. We do not currently have a way to tune the cache sizes, which would be useful for big systems, and would mean "throw more memory at it" starts to become a valid fix.

---
## [XPMUser/XPMUser.github.io](https://github.com/XPMUser/XPMUser.github.io)@[67bdc71102...](https://github.com/XPMUser/XPMUser.github.io/commit/67bdc71102b454cf6f1e927f8c5c75033ca38818)
#### Sunday 2023-08-20 09:43:33 by Ao28th28

Mr. Inquiry can't wait

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
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[a2ee4ec813...](https://github.com/Ben10Omintrix/tgstation/commit/a2ee4ec813c38741d593e5e1731764458c77b811)
#### Sunday 2023-08-20 10:01:31 by Jacquerel

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
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[c8266cf0a2...](https://github.com/Ben10Omintrix/tgstation/commit/c8266cf0a2effaf8b931ba870c124608305b7d68)
#### Sunday 2023-08-20 10:01:31 by necromanceranne

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
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[bae1aef3b4...](https://github.com/Rex9001/Rex_Tg/commit/bae1aef3b457cb4fbad551a8560319ed993ba397)
#### Sunday 2023-08-20 10:04:54 by san7890

Refactors Regal Rats into Basic Mobs (more titles edition) (#77681)

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

---
## [Stymmm/Trigonometry-bot](https://github.com/Stymmm/Trigonometry-bot)@[6f813cc73e...](https://github.com/Stymmm/Trigonometry-bot/commit/6f813cc73e7816959410606cbd52f459f7101232)
#### Sunday 2023-08-20 10:14:58 by Stymmm

Add trigonometry_bot.py script

**Trigonometry Bot: A Python Script for Solving Trigonometric Identities**

Welcome to the Trigonometry Bot repository! This project hosts a Python script (`trigonometry_bot.py`) designed to help you solve various trigonometric identities effortlessly. Whether you're a student studying trigonometry or someone looking for quick solutions to trigonometric equations, this script has got you covered.

**Features:**
- Quickly solve a variety of trigonometric identities, including Pythagorean, Reciprocal, Quotient, Co-Function, Double Angle, and Half Angle Identities.
- Get instant answers by inputting the desired identity or equation. The bot will compute and display the results.
- User-friendly interface with clear instructions and responses.

**How to Use:**
1. Clone or download the repository to your local machine.
2. Run the `trigonometry_bot.py` script using a Python interpreter.
3. Enter the trigonometric identity or equation you'd like to solve.
4. The bot will process your input, compute the result, and display it on the screen.

**Contributing:**
If you're passionate about mathematics, coding, or both, we invite you to contribute to this project. You can suggest new trigonometric identities, improve the user interface, or enhance the error handling of the script. To contribute, simply fork this repository, make your changes, and submit a pull request.

**License:**
This project is open-source and available under the [MIT License](LICENSE). Feel free to use, modify, and distribute the script according to the terms of the license.

**Contact:**
Have questions, suggestions, or feedback? Feel free to open an issue on this repository or reach out to the project owner via their GitHub profile.

Thank you for checking out the Trigonometry Bot project! We hope this script simplifies your trigonometry problem-solving experience.

---
## [fbwer/crawl](https://github.com/fbwer/crawl)@[6656212320...](https://github.com/fbwer/crawl/commit/66562123206107b4e469b57e8098b9c7ca6ab157)
#### Sunday 2023-08-20 10:16:42 by Nicholas Feinberg

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
## [weaponmasterjax/device_xiaomi_blossom](https://github.com/weaponmasterjax/device_xiaomi_blossom)@[14443c5bb8...](https://github.com/weaponmasterjax/device_xiaomi_blossom/commit/14443c5bb8344bc72e26cb2a1718c7e2556807f7)
#### Sunday 2023-08-20 10:30:20 by snnbyyds

Revert "blossom: Switch vendor and odm to erofs"

This reverts commit 951040e1c865d6293aaa91922c206db30e3bb6e4.
So, all in all, for those who wants freedom on their own devices, huawei, fuck you!

---
## [kerberosai/openUI](https://github.com/kerberosai/openUI)@[dbcc24288b...](https://github.com/kerberosai/openUI/commit/dbcc24288bf5f151804af0bcf6ed0ccacafe76c5)
#### Sunday 2023-08-20 11:28:04 by kerberos

Update readme.md

# VSCode Web Template 🚀

Welcome to the VSCode Web Template! This open-source template is designed to bring the magic of your favorite code editor, VS Code, right into your web browser. Perfect for developers and tech enthusiasts, this template gamifies the web experience, making it more interactive and fun!

## 🌟 Features

- **VS Code Interface**: Dive into a web experience that feels just like using VS Code. It's familiar, intuitive, and super cool!
  
- **Interactive Sidebar**: Navigate through different sections like "About", "Web3 Projects", "Open Source Contributions", and more with the click of a button.
  
- **Syntax Highlighting**: With the power of Highlight.js, your code snippets will shine bright, making them a joy to read.
  
- **Status Bar**: Keep track of your "Git branch", "installed extensions", and other fun tidbits with the interactive status bar at the bottom.
  
- **Tooltips**: Hover over certain elements to get extra info. It's like discovering Easter eggs on your webpage!

## 🛠️ Technologies Used

![HTML5 Badge](https://img.shields.io/badge/-HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3 Badge](https://img.shields.io/badge/-CSS3-1572B6?style=flat&logo=css3)
![JavaScript Badge](https://img.shields.io/badge/-JavaScript-black?style=flat&logo=javascript)
![Bootstrap Badge](https://img.shields.io/badge/-Bootstrap-563D7C?style=flat&logo=bootstrap)
![Highlight.js Badge](https://img.shields.io/badge/-Highlight.js-9cf?style=flat)

## 🎮 How to Play

1. **Embed the Magic**: Integrate this template into your website by copying and pasting the provided HTML code.
  
2. **Customize Your Adventure**: Change the content inside the `<pre><code>` tags to tell your story. Tweak the styles and colors to match your quest's theme.
  
3. **Navigate the Kingdom**: Use the sidebar buttons to journey through different realms. Each click unveils a new chapter in the main area.

## 🤝 Contribute

Want to add more magic? 🪄 Feel free to fork the repository, sprinkle in your enhancements, and then send a pull request. Together, we can make the web a more enchanted place!

## 📜 License

This spellbook (aka project) is open source and is licensed under the MIT license.

---

Embark on your web adventure with the VSCode Web Template! May your journey be filled with code, creativity, and countless eureka moments! 🌌🌠🎉

---
## [fubar2/nftoolmaker](https://github.com/fubar2/nftoolmaker)@[09a3a89033...](https://github.com/fubar2/nftoolmaker/commit/09a3a89033a45afb8b4ebb413e03ca334a5196b1)
#### Sunday 2023-08-20 11:30:31 by fubar2

working on ampir but almost nothing else.
Still cleaning up the parsing since the example was easy and being lazy...
uses shlex to tokenise that shit.
What I have seen so far seems not impossible to parse.
Just not easy.
Parsing multiple tests but will do one
Dealing with stupid tests that want inputs from other module runs is just
too annoying at present. Fug that. I always thought modules were supposed
to be modular but what would I know compared to these real bioinformaticians.

---
## [TheGamerdk/cmss13](https://github.com/TheGamerdk/cmss13)@[1ea79a2ed8...](https://github.com/TheGamerdk/cmss13/commit/1ea79a2ed836ef4d20db511485c2f935304bfd55)
#### Sunday 2023-08-20 12:36:41 by Ben

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
## [smclacke/minishell](https://github.com/smclacke/minishell)@[1445eafbfb...](https://github.com/smclacke/minishell/commit/1445eafbfb944d13d2cb97c4d2e17cbb34200fd2)
#### Sunday 2023-08-20 12:47:11 by Sarah Mclacken

holy shit quotations are bullshit, notes in sarah.md

---
## [Peliex/tgstation](https://github.com/Peliex/tgstation)@[dc6ddd821b...](https://github.com/Peliex/tgstation/commit/dc6ddd821b1d9fe4783cf5d05c4ed2aa96f98e89)
#### Sunday 2023-08-20 12:49:36 by Cheshify

North Star Science Rework And More (#77439)

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

---
## [bravely-beep/bevy](https://github.com/bravely-beep/bevy)@[fb4c21e3e6...](https://github.com/bravely-beep/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Sunday 2023-08-20 13:21:02 by Ida "Iyes

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
## [WindSoilder/nushell](https://github.com/WindSoilder/nushell)@[ad49c17eba...](https://github.com/WindSoilder/nushell/commit/ad49c17ebacd04585fb4355e079ec87d7fc63d8d)
#### Sunday 2023-08-20 13:22:53 by Kiryl Mialeshka

fix(nu-parser): do not update plugin.nu file on nu startup (#10007)

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

I've been investigating the [issue
mentioned](https://github.com/nushell/nushell/pull/9976#issuecomment-1673290467)
in my prev pr and I've found that plugin.nu file that is used to cache
plugins signatures gets overwritten on every nushell startup and that
may actually mess up with the file content if 2 or more instances of
nushell will run simultaneously.

To reproduce:
1. register at least 2 plugins in your local nushell
2. remember how many entries you have in plugin.nu with `open
$nu.plugin-path | find nu_plugin`
3. run 
    - either `cargo test` inside nushell repo
- or run smth like this `1..100 | par-each {|it| $"(random integer
1..100)ms" | into duration | sleep $in; nu -c "$nu.plugin-path"}` to
simulate parallel access. This approach is not so reliable to reproduce
as running test but still a good point that it may effect users actually
4. validate that your `plugin.nu` file was stripped

<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

# Solution

In this pr I've refactored the code of handling the `register` command
to minimize code duplications and make sure that overwrite of
`plugin.nu` file is happen only when user calls the command and not on
nu startup

Another option would be to use temp `plugin.nu` when running tests, but
as the issue actually can affect users I've decided to prevent
unnecessary writing at all. Although having isolated `plugin.nu` still
worth of doing

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->
It changes the behaviour actually as the call `register <plugin>
<signature>` now doesn't updates `plugin.nu` and just reads signatures
to the memory. But as I understand that kind of call with explicit
signature is meant to use only by nushell itself in the `plugin.nu` file
only. I've asked about it in
[discord](https://discordapp.com/channels/601130461678272522/615962413203718156/1140013448915325018)

<!--
Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect -A clippy::result_large_err` to check that
you're using the standard code style
- `cargo test --workspace` to check that all tests pass
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

Actually, I think the way plugins are stored might be reworked to
prevent or mitigate possible issues further:
- problem with writing to file may still arise if we try to register in
parallel as several instances will write to the same file so the lock
for the file might be required
- using additional parameters to command like `register` to implement
some internal logic could be misleading to the users
- `register` call actually affects global state of nushell that sounds a
little bit inconsistent with immutability and isolation of other parts
of the nu. See issues
[1](https://github.com/nushell/nushell/issues/8581),
[2](https://github.com/nushell/nushell/issues/8960)

---
## [dieamond13/tgstation-dieamond](https://github.com/dieamond13/tgstation-dieamond)@[7f1d53e719...](https://github.com/dieamond13/tgstation-dieamond/commit/7f1d53e719d8d097e8af41b9b80a829b84b105ce)
#### Sunday 2023-08-20 14:38:33 by Ben10Omintrix

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
## [dieamond13/tgstation-dieamond](https://github.com/dieamond13/tgstation-dieamond)@[b22ff1a4eb...](https://github.com/dieamond13/tgstation-dieamond/commit/b22ff1a4ebfd0a1dd1b75d6979edc73e6f4556b2)
#### Sunday 2023-08-20 14:38:33 by Sealed101

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
## [pinjuf/tutOS](https://github.com/pinjuf/tutOS)@[bc53529ebd...](https://github.com/pinjuf/tutOS/commit/bc53529ebd9a46c66e69a4de869edc87a812342f)
#### Sunday 2023-08-20 14:49:01 by pinjuf

completely fucking redo my entire fucking shit ass shell

---
## [PDP-10/its](https://github.com/PDP-10/its)@[01fa007735...](https://github.com/PDP-10/its/commit/01fa007735621655ea60486912feaff5b387c504)
#### Sunday 2023-08-20 15:12:35 by Lars Brinkhoff

6502 assembler written in Logo.

Courtesy of the author, Leigh Klotz.

Klotz wrote in https://news.ycombinator.com/item?id=23064346

> The assembler [for Apple II Logo] was already chosen, probably by
> Steve Hain or Gary Drescher.  I believe it was CROSS.  It annoyed me
> that I would get phase errors if I edited during the first pass
> which was like 10 or 15 minutes at night so I wrote a one-pass
> assembler in MacLisp, but it was slower to finish than the first
> pass of CROSS so I translated it to Logo and Hal said to put it on
> the utilities disk.  I can't remember who added .output and .input
> but Logo had had them before the Apple II, I think 11Logo had it.

---
## [LovliestPlant/Skyrat-tg](https://github.com/LovliestPlant/Skyrat-tg)@[c6e0ba7516...](https://github.com/LovliestPlant/Skyrat-tg/commit/c6e0ba75169d010e2cdfa48134003b0bb9ab8485)
#### Sunday 2023-08-20 15:24:06 by SkyratBot

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
## [ABoxFaux/tgstation](https://github.com/ABoxFaux/tgstation)@[1c852d2863...](https://github.com/ABoxFaux/tgstation/commit/1c852d2863622bb24acf7511d7a9bb06813619fc)
#### Sunday 2023-08-20 15:56:47 by EOBGames

Martian Food: A Taste of the Red Planet (#75988)

## About The Pull Request
Adds a selection of new foods and drinks based around Mars.
More information on Mars can be found here:
https://github.com/tgstation/common_core/blob/master/Interesting%20Planets/Human%20Space/The%20Sol%20System.md
To summarise for the general audience, Mars is a vital colony of the
Terran Federation, having been primarily settled (at least originally)
by Cybersun Industries to harvest its lucrative supplies of plasma, the
second largest in human space behind Lavaland. This has given Mars a
diverse culture evolving from the mostly East Asian colonists, and their
food reflects this.

Thanks to Melbert for their work on the soup portion of this PR.

The food:
Martian cuisine draws upon the culinary traditions of East Asia, and
adds in fusion cuisine from the later colonists. Expect classics such as
ramen, curry, noodles and donburi, as well as new takes on the formula
like the Croque-Martienne, Peanut Butter Ice Cream Mochi, and the
Kitzushi- chilli cheese and rice inside a fried tofu casing. Oh, and
lots of pineapple. The Martians love pineapple:

![image](https://github.com/tgstation/tgstation/assets/58124831/c9ae33a1-e03a-4f94-8ce0-8ad124e88e8d)
Also included are some foods for Ethereals, which may or may not be
hinting at something I've got planned...

The drinks:
Four new base drinks make their way to the game, bringing with them a
host of new cocktails: enjoy new ventures in bartending with Coconut
Rum, Shochu/Soju, Yuyake (our favourite legally-distinct melon liqueur),
and Mars' favourite alcoholic beverage, rice beer. Each is available in
the dispenser, as well as bottles in the booze-o-mat:

![image](https://github.com/tgstation/tgstation/assets/58124831/914a6e2a-7ef5-4791-ae31-d08fa9211083)

The recipes:
To make your (and the wiki editors) lives easier, please find below the
recipes for both foods and drinks:
Food: https://hackmd.io/@EOBGames/BkVFU0w9Y
Drinks: https://hackmd.io/@EOBGames/rJ1OhnsJ2
## Why It's Good For The Game
Another lot of variety for the chef and bartender, as well as continuing
the work started with lizard and moth food in getting Common Core into
the game in a tangible and fun way.
## Changelog
:cl: EOBGames, MrMelbert
add: Mars celebrates the 250th anniversary of the Martian Concession
this year, and this has brought Martian cuisine to new heights of
popularity. Find a new selection of Martian foods and drinks available
in your crafting menu today!
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [inkeliz/gio](https://github.com/inkeliz/gio)@[6ea4119a3c...](https://github.com/inkeliz/gio/commit/6ea4119a3ceb36f009af1486e41b47f08c2239bd)
#### Sunday 2023-08-20 16:10:14 by Chris Waldon

text,widget: [API] implement consistent, controllable line height

This commit ensures that any given paragraph of text shaped by Gio will use a single
internal line height. This line height is determined (by default) by the text size,
rather than the fonts involved. This is a breaking change, as previously we would
blindly use the largest line height of any font in a line for that line, leading to
lines within the same paragraph with extremely uneven spacing. This commit also
updates some test expectations in package widget.

I thought pretty hard about how to implement line spacing, and consulted a few sources:

[0] https://www.figma.com/blog/line-height-changes/
[1] https://practicaltypography.com/line-spacing.html
[2] https://developer.mozilla.org/en-US/docs/Web/CSS/line-height

There is no single, universal way to think about line spacing. Fonts internally specify
a line height as the sum of their ascent, descent, and gap, but the line height of two
fonts at the same pixel size (say 20 Sp) can vary wildy (especially across writing systems).
There are two strategies we could pursue to establish the line height of a paragraph of text:

- derive the line height from the fonts involved (our old behavior, and the behavior of
  many word processors)
- derive the line height from the requested text size provided by the user (the behavior of the
  web).

The challenge with the first option is that for a given piece of text in the UI, there can
be a silly number of fonts involved. If a label dispays user-generated content, the user can
put an emoji in it, and emoji fonts have different line heights from latin ones. This can cause
unexpected and nasty layout shift. Gio would previously do exactly this, on a line-by-line basis,
resulting in unevenly spaced lines within a paragraph depending on which fonts were used on
which lines. Choosing one of the fonts and enforcing its line height would make things consistent,
but it isn't clear how to choose that canonical font. There is no 1:1 mapping between the input
text.Font provided in the shaping parameters and a single font.Face. Instead, that mapping depends
upon the runes being shaped.

I think the only sane way to implement the first option would be to synthesize some text in the
provided system.Locale (mapping the language to a script and then generating a rune from that
script), shape that single rune, and then enforce the line height of the resulting face on the
entire paragraph. This would require doing a fair bit more work per paragraph than Gio does today,
so I've opted not to do it.

Instead, the second option allows us to choose a line height based on the size of the text that
the user wants to display. While this can potentially interact poorly with unusually tall fonts,
it means that text will always have a consistent line height.

I've provided two knobs to control line height:

- text.Parameters.LineHeight lets you set a specific height in pixels with a default value of
  text.Parameters.PxPerEm.
- text.Parameters.LineHeightScale applies a scaling factor to the LineHeight, allowing you to
  easily space out text without hard-coding a specific pixel size. The default value here
  (drawn from the recommendations of [1]) is 1.2, which looks pretty good across many fonts.

I've chosen this two-value API because many users will want to set one or the other value. I
considered instead a single value field and a "mode" that would specify how it was used, but
that felt uglier. Also, you *can* set both of these two fields and get predictable results.

I'd like to revisit using the line height of the chosen fonts in the future, but it seems a
little too complex to be worthwhile right now. An interesting option would be making the
select-a-face-using-locale strategy described above an opt-in feature, though some users
might instead want to just use the tallest line height among fonts in use. Something like
this Android API might be appropriate:

[3] https://learn.microsoft.com/en-us/dotnet/api/android.widget.textview.fallbacklinespacing?view=xamarin-android-sdk-13

I'd like to thank Dominik Honnef for some good discussion around this feature, and for pointing
me to some good sources on the subject.

Signed-off-by: Chris Waldon <christopher.waldon.dev@gmail.com>

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[dcd1a884fe...](https://github.com/treckstar/yolo-octo-hipster/commit/dcd1a884fe01bed696667f3359bc5f8386f3519b)
#### Sunday 2023-08-20 16:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [carlarctg/tgstation](https://github.com/carlarctg/tgstation)@[2caa114b87...](https://github.com/carlarctg/tgstation/commit/2caa114b873ad31861b3699e1d4685168a3c2332)
#### Sunday 2023-08-20 17:05:17 by carlarctg

Fucking piece of shit finally works now I hate AI code so much

---
## [carlarctg/tgstation](https://github.com/carlarctg/tgstation)@[a8e0d7c8d2...](https://github.com/carlarctg/tgstation/commit/a8e0d7c8d202027d36c96391ed9a43cb5d708065)
#### Sunday 2023-08-20 17:08:00 by MrMelbert

Adds a new positive quirk, "Spacer Born".  (#76809)

## About The Pull Request

Adds a new 7 point positive quirk, "Spacer Born". Totally not inspired
by The Expanse, don't look at the branch name.

You were born in space, rather than on a planet, so your physiology has
adapted differently.
You are more comfortable in space, and way less comfortable on a planet.

Benefits:
   - You are slightly taller. (No mechanical effect)
   - You take 20% less damage from pressure damage.
   - You take 20% less damage from cold environments. 
- You move 10% faster while floating (NOT drifting, this is zero gravity
movement while beside a wall).
- You drift 20% faster (Drifting through zero gravity, untethered to
anything)
- While in space (z-level-wise, not turf wise), you lose some disgust
overtime.
- While experiencing no-gravity for an extended period of time, you will
start regenerating stamina and reduce stuns at a very low rate.
- If you are assigned to shaft miner (or the map is Icebox), you are
awarded with a 25% wage bonus (hazard pay).

Downsides:
- While on a planet (Yes, this includes Icebox and planetary maps), you
gain gravity sickness:
- Passive accrue disgust (slightly lessened on Icebox) (Capped at low
levels)
      - Choking, after extended periods (disabled on Icebox)
      - Slower movement 
      - Weaker stamina (disabled on Icebox)
- Suffocation from extended periods (disabled on Icebox) (Lungs aren't
adapted)
      - Mood debuff

(Effects not final)

## Why It's Good For The Game

I'd figure I throw my hat in with the Positive Quirk Curse. 

This is a quirk that improves your ability in a niche circumstance (low
gravity / dangerous pressure), with some downsides that are only
generally in effect if you play a few roles (or it's Icebox).

Because of this I think it'll provide an interesting niche, where Spacer
Born engineers are slightly better than their counterparts due to their
origin (moving faster in space without a jetpack, withstanding
pressure). However, at the same time, if the mining outpost sustains
damage and needs repairs... suddenly your buff over your cohorts
disappears, and you have to brave somewhere hostile to your body.

Ultimately, the goal of the quirk is to encourage people to approach
situations a bit differently.
Or take it as a challenge and play shaft miner. 

## Changelog

:cl: Melbert
add: Adds a new 7 point positive quirk, "Spacer Born". You were born in
space, and as a result your body's adapted to life in artificial
gravity, making you much more effective and comfortable in lower
gravity. However, travelling planet-side is quite a chore, especially if
you're assigned to work there.
add: Adds a chemical: Ondansetron, created by Oil + Nitrogen + Oxygen +
Ethanol catalyst. A powerful Antiemetic (lowers disgust).
/:cl:

---
## [XPMUser/XPMUser.github.io](https://github.com/XPMUser/XPMUser.github.io)@[ae8a621171...](https://github.com/XPMUser/XPMUser.github.io/commit/ae8a62117118075bdb4cfafb562d6d30088807f7)
#### Sunday 2023-08-20 17:12:37 by Ao28th28

The map is a bit darker.

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
## [distributivgesetz/tgstation](https://github.com/distributivgesetz/tgstation)@[31f1924324...](https://github.com/distributivgesetz/tgstation/commit/31f1924324b04086f24034aaf754d5f85cb595a8)
#### Sunday 2023-08-20 17:48:29 by san7890

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
## [vim/vim](https://github.com/vim/vim)@[c13b3d1350...](https://github.com/vim/vim/commit/c13b3d1350b60b94fe87f0761ea31c0e7fb6ebf3)
#### Sunday 2023-08-20 19:20:12 by Yee Cheng Chin

patch 9.0.1776: No support for stable Python 3 ABI

Problem:  No support for stable Python 3 ABI
Solution: Support Python 3 stable ABI

Commits:
1) Support Python 3 stable ABI to allow mixed version interoperatbility

Vim currently supports embedding Python for use with plugins, and the
"dynamic" linking option allows the user to specify a locally installed
version of Python by setting `pythonthreedll`. However, one caveat is
that the Python 3 libs are not binary compatible across minor versions,
and mixing versions can potentially be dangerous (e.g. let's say Vim was
linked against the Python 3.10 SDK, but the user sets `pythonthreedll`
to a 3.11 lib). Usually, nothing bad happens, but in theory this could
lead to crashes, memory corruption, and other unpredictable behaviors.
It's also difficult for the user to tell something is wrong because Vim
has no way of reporting what Python 3 version Vim was linked with.

For Vim installed via a package manager, this usually isn't an issue
because all the dependencies would already be figured out. For prebuilt
Vim binaries like MacVim (my motivation for working on this), AppImage,
and Win32 installer this could potentially be an issue as usually a
single binary is distributed. This is more tricky when a new Python
version is released, as there's a chicken-and-egg issue with deciding
what Python version to build against and hard to keep in sync when a new
Python version just drops and we have a mix of users of different Python
versions, and a user just blindly upgrading to a new Python could lead to
bad interactions with Vim.

Python 3 does have a solution for this problem: stable ABI / limited API
(see https://docs.python.org/3/c-api/stable.html). The C SDK limits the
API to a set of functions that are promised to be stable across
versions. This pull request adds an ifdef config that allows us to turn
it on when building Vim. Vim binaries built with this option should be
safe to freely link with any Python 3 libraies without having the
constraint of having to use the same minor version.

Note: Python 2 has no such concept and this doesn't change how Python 2
integration works (not that there is going to be a new version of Python
2 that would cause compatibility issues in the future anyway).

---

Technical details:
======

The stable ABI can be accessed when we compile with the Python 3 limited
API (by defining `Py_LIMITED_API`). The Python 3 code (in `if_python3.c`
and `if_py_both.h`) would now handle this and switch to limited API
mode. Without it set, Vim will still use the full API as before so this
is an opt-in change.

The main difference is that `PyType_Object` is now an opaque struct that
we can't directly create "static types" out of, and we have to create
type objects as "heap types" instead. This is because the struct is not
stable and changes from version to version (e.g. 3.8 added a
`tp_vectorcall` field to it). I had to change all the types to be
allocated on the heap instead with just a pointer to them.

Other functions are also simply missing in limited API, or they are
introduced too late (e.g. `PyUnicode_AsUTF8AndSize` in 3.10) to it that
we need some other ways to do the same thing, so I had to abstract a few
things into macros, and sometimes re-implement functions like
`PyObject_NEW`.

One caveat is that in limited API, `OutputType` (used for replacing
`sys.stdout`) no longer inherits from `PyStdPrinter_Type` which I don't
think has any real issue other than minor differences in how they
convert to a string and missing a couple functions like `mode()` and
`fileno()`.

Also fixed an existing bug where `tp_basicsize` was set incorrectly for
`BufferObject`, `TabListObject, `WinListObject`.

Technically, there could be a small performance drop, there is a little
more indirection with accessing type objects, and some APIs like
`PyUnicode_AsUTF8AndSize` are missing, but in practice I didn't see any
difference, and any well-written Python plugin should try to avoid
excessing callbacks to the `vim` module in Python anyway.

I only tested limited API mode down to Python 3.7, which seemes to
compile and work fine. I haven't tried earlier Python versions.

2) Fix PyIter_Check on older Python vers / type##Ptr unused warning

For PyIter_Check, older versions exposed them as either macros (used in
full API), or a function (for use in limited API). A previous change
exposed PyIter_Check to the dynamic build because Python just moved it
to function-only in 3.10 anyway. Because of that, just make sure we
always grab the function in dynamic builds in earlier versions since
that's what Python eventually did anyway.

3) Move Py_LIMITED_API define to configure script

Can now use --with-python-stable-abi flag to customize what stable ABI
version to target. Can also use an env var to do so as well.

4) Show +python/dyn-stable in :version, and allow has() feature query

Not sure if the "/dyn-stable" suffix would break things, or whether we
should do it another way. Or just don't show it in version and rely on
has() feature checking.

5) Documentation first draft. Still need to implement v:python3_version

6) Fix PyIter_Check build breaks when compiling against Python 3.8

7) Add CI coverage stable ABI on Linux/Windows / make configurable on Windows

This adds configurable options for Windows make files (both MinGW and
MSVC). CI will also now exercise both traditional full API and stable
ABI for Linux and Windows in the matrix for coverage.

Also added a "dynamic" option to Linux matrix as a drive-by change to
make other scripting languages like Ruby / Perl testable under both
static and dynamic builds.

8) Fix inaccuracy in Windows docs

Python's own docs are confusing but you don't actually want to use
`python3.dll` for the dynamic linkage.

9) Add generated autoconf file

10) Add v:python3_version support

This variable indicates the version of Python3 that Vim was built
against (PY_VERSION_HEX), and will be useful to check whether the Python
library you are loading in dynamically actually fits it. When built with
stable ABI, it will be the limited ABI version instead
(`Py_LIMITED_API`), which indicates the minimum version of Python 3 the
user should have, rather than the exact match. When stable ABI is used,
we won't be exposing PY_VERSION_HEX in this var because it just doesn't
seem necessary to do so (the whole point of stable ABI is the promise
that it will work across versions), and I don't want to confuse the user
with too many variables.

Also, cleaned up some documentation, and added help tags.

11) Fix Python 3.7 compat issues

Fix a couple issues when using limited API < 3.8

- Crash on exit: In Python 3.7, if a heap-allocated type is destroyed
  before all instances are, it would cause a crash later. This happens
  when we destroyed `OptionsType` before calling `Py_Finalize` when
  using the limited API. To make it worse, later versions changed the
  semantics and now each instance has a strong reference to its own type
  and the recommendation has changed to have each instance de-ref its
  own type and have its type in GC traversal. To avoid dealing with
  these cross-version variations, we just don't free the heap type. They
  are static types in non-limited-API anyway and are designed to last
  through the entirety of the app, and we also don't restart the Python
  runtime and therefore do not need it to have absolutely 0 leaks.

  See:
  - https://docs.python.org/3/whatsnew/3.8.html#changes-in-the-c-api
  - https://docs.python.org/3/whatsnew/3.9.html#changes-in-the-c-api

- PyIter_Check: This function is not provided in limited APIs older than
  3.8. Previously I was trying to mock it out using manual
  PyType_GetSlot() but it was brittle and also does not actually work
  properly for static types (it will generate a Python error). Just
  return false. It does mean using limited API < 3.8 is not recommended
  as you lose the functionality to handle iterators, but from playing
  with plugins I couldn't find it to be an issue.

- Fix loading of PyIter_Check so it will be done when limited API < 3.8.
  Otherwise loading a 3.7 Python lib will fail even if limited API was
  specified to use it.

12) Make sure to only load `PyUnicode_AsUTF8AndSize` in needed in limited API

We don't use this function unless limited API >= 3.10, but we were
loading it regardless. Usually it's ok in Unix-like systems where Python
just has a single lib that we load from, but in Windows where there is a
separate python3.dll this would not work as the symbol would not have
been exposed in this more limited DLL file. This makes it much clearer
under what condition is this function needed.

closes: #12032

Signed-off-by: Christian Brabandt <cb@256bit.org>
Co-authored-by: Yee Cheng Chin <ychin.git@gmail.com>

---
## [neovide/neovide](https://github.com/neovide/neovide)@[937decd850...](https://github.com/neovide/neovide/commit/937decd850f2087a20e6488e42ffd1fafbec02e0)
#### Sunday 2023-08-20 20:33:48 by fredizzimo

fix: Improve nvim detection (#1946)

* Improve nvim detection:

Don't rely on the shell specific `exists", instead run `nvim -v`.
Additionally, if there's unexpected output, for example if your shell is
configured wrongly to output something when run in non-interactive mode,
it will tell you so, instead of failing with very strange errors later.

The `neovim-bin` argument has also been changed to always require the
binary to exist, instead if falling back to `nvim` as that's probably
not what the user wants. If `nevoim-bin` contains path separators the
binary will be tried directly, otherwise `which` will be used to find
the correct executable.

The which command has also been changed to always use the which crate
first to avoid shell specific issues (for example nushell).

The output is printed directly to stderr instead of the log, for a more
user friendly experience. Furthermore, the maybe disown call has been
moved so that the user actually has a chance to see the errors in the
console.

* fix(command): correct typos and clarify help message

* fix: preliminarly restore forking behavior

This however also loses possible error messages at startup about the
nvim binary not being found.

* codestyle: calm rustfmt

* fix(command): make error message about missing/errornous nvim visible

---------

Co-authored-by: MultisampledNight <contact@multisamplednight.com>

---
## [chapmanjacobd/journal](https://github.com/chapmanjacobd/journal)@[98b482b8ea...](https://github.com/chapmanjacobd/journal/commit/98b482b8ea0b61532406d91b9c651a84670ec06d)
#### Sunday 2023-08-20 21:22:08 by Jacob Chapman

gitignore 100_tip_for_lady_selling_tamales_with_her_3_kids#g3za8yz 12_problems_that_people_have_that_can_be_turned#endszi5 16_ideapad_5_pro_ryzen_5800h_worth_it#hg6a4v3 16_ideapad_5_pro_ryzen_5800h_worth_it#hg6eq0v 1890s_busan_a_local_magistrate_and_his_officers#h09evcz 18tb_exos_any_real_downsides_to_using_this_inside#i6pzr93 2023_fleshlight_wish_list#j2xgltm 23#e6iv94a 25_leanfire_country_recommendations_less_than#edaexuk 3634_ideas_for_you_to_steal#isozpzj 3634_ideas_for_you_to_steal#isw4m3y 3_months_agoi_posted_footage_of_ingagi1930_now_i#fzm2dcr 3d_printed_a_miniature_raspberry_pi_server_rack#eoe0w5p 420_10bit_hevc_vs_422_10bit_avc_codecs_higher#jb8azo4 72_of_survey_respondents_say_border_controls#imyjplc 80_of_audible_traffic_signals_for_blind_in_japan#ghzlr2k a_browser_plugin_that_shows_you_which_search#ji96x0q a_bunch_of_python_and_bash_scripts_i_developed#iee6ggd a_bunch_of_python_and_bash_scripts_i_developed#iee7tcp a_few_months_ago_i_thought_4tb_would_be_enough#ikt1nj0 a_full_13_of_this_building_is_reserved_for_cars#havg1gs a_site_that_takes_your_notes_and_turns_them_into#ir6ys2f a_song_about_george_floyd_by_a_korean_pop_singer#hagv9ar a_sub_where_users_help_you_plan_trips_and_help#edab7u9 a_subreddit_that_would_help_me_plan_trip_given#edab4t9 a_subreddit_that_would_help_me_plan_trip_given#edab6z8 a_username_w_mai_in_it#hj3tuu8 a_website_for_rating_reviewing_groceries#jq9z5gq a_website_or_app_that_allows_you_to_rank_or_make#jvxy0gk a_young_north_vietnamese_soldiers_lightning_a#gabxfjr accessing_music_outside_of_home_network_with#j2flkn8 achieved_a_thing_today#eoi6sac affordable_bed_sheets_thatll_keep_me_cool#inhi02i after_over_15_years_of_ripping_and_downloading_my#jdu11x8 after_over_15_years_of_ripping_and_downloading_my#jdu1bsv ai_inventing_its_own_culture_passing_it_on_to#ibbwz11 air_force_skyborg_ai_powered_drones_to_take#frj05bx aligning_text_from_a_file_with_audio_and_video#i8jjxcq alt_tab_in_plasma_forgets_the_order_of_windows#hk5xfz0 alternatives_to_rstudio#hmji1g1 always_make_sure_that_you_have_enough_space_left#icxi9yw amazing#htrtyu8 amazing_guy_comes_to_the_rescue_of_sea_lion_with#hcyeawq an_actual_guide_to_choosing_your_structurer#gdxtkxh an_image_i_found_from_my_old_phone#gg7mwsk an_interesting_fact_about_btrfs#iem81wd any_creative_ideas_to_protect_a_sidewalk_from_an#fwrztcg any_documentation_on_post_properties_such_as#ird1ob9 any_lua_script_to_crop_and_save_cropped_video#jwb0q0s any_offline_bookmark_managers_or_similar_software_youd_recommend_simple_and_open_source_preferred#comment-a355 any_offline_bookmark_managers_or_similar_software_youd_recommend_simple_and_open_source_preferred#comment-a3qc any_reason_not_to_use_tsnode_for_local_utility#gcb5tk6 any_sw_recommendation_to_index_any_kind_of_file#i6x0du0 anybody_know_where_i_can_find_the_magician_of#jt102hp anyone_interested_in_figuring_out_a_better_system#fmjzd9p anyone_know_how_i_can_setup_a_simple_automation#hah8lqy anyone_know_of_any_software_that_can_dissect#hd4u7sq anyone_managed_to_get_a_macro_to_muteunmute_the#fqmc516 anyone_managed_to_get_a_macro_to_muteunmute_the#fqpn7gb anyone_want_2_alt_gfs#hfzhbdp apparently_you_arent_actually_supposed_to_use#h8qyyth area_51_in_fallout_nevada_has_the_same_warning#fv6g8ig asking_a_question_on_stack_overflow_and_all_the#hh11uva at_lego#icdd0ph audio_quality_with_ytdlp#i6rcli8 august_confirmed_trade_thread#dle23xl auto_suggest_randomly_stops_working#fwgh4k5 autohotkey_mouse_tips#e0i83h7 backing_up_files#g348wp0 based_ho_ch\341\273\211_minh#g88t4d2 battery_saver#gentvqr beat_driven_insomnia_a_song_for_winter#dovh1qi beforeafter_of_my_backpack_set_up#hgaoslm bella_saer_u_ne_cla_na_ukcherokee_choral_2015#dniw0ec besides_money_if_the_was_the_case_what_might_prevent_you_from_have_a_fulfilling_life#comment-a5xq best_book_for_learning_python_for_gis#hm09df7 best_book_for_learning_python_for_gis#hm1jswv best_book_for_learning_python_for_gis#hm1kzlf best_introduction_to_hong_sangsoo#i7hbfz4 best_place_to_start#g4pnqn8 best_way_to_access_and_organize_multiple_filetypes#ioq5e7s best_way_to_transfer_my_configuration_to_a_new#jv9ex42 bill_gates_said_i_will_always_choose_a_lazy#gcosw3o bizarre_hobbit_film#io2xdeb blog_wide_haskell_reducing_your_dependencies#fmnmq8r bluetooth_gas#glhp1er bm_ultrastudio_mini_monitor_yuv_or_rgb_slightly#ge392ar bm_ultrastudio_mini_monitor_yuv_or_rgb_slightly#ge3rusm borderline_porn_movies_with_actual_plot_and_a#ixzpgpr bram_moolenaar_creator_of_vim_has_died#juythai browser_tab_hoarding_how_do_you_organizearchive#iqx2mfp bruh#i0ckabf bruh#i0l71ri btrfs_raid0_and_single_what_does_that_mean#j5l0zgh buddy_of_mine_made_1000_pierogies_for_my_birthday#jqk8nw5 building_an_app_to_rule_all_webbased_saas_need#iet5qpm bye_kmart#fiimc72 cali_watch_for_oncoming_tra_never_mind#i5ktdh3 came_across_rare_free_samples_hidden_in_the#gerd2n1 came_across_this_vintage_stamp#ho8l5fe can_anybody_tell_me_what_is_wrong_with_this#i5vmnzz can_btrfs_raid1_disks_be_merged#juxuylt can_btrfs_raid1_disks_be_merged#juyg5el can_i_tell_google_to_complete_a_task_silently#ilnb8bt can_not_delete_individual_cells#g26oxty can_someone_here_nudge_me_in_a_certain_direction#dxcd65w can_someone_please_suggest_how_can_i_improve_this#g1tfm2b can_upvotesdownvotes_be_used_as_evidence_in_court#hhxqhhj can_you_believe_this_doesnt_count_as_a_small_flat#go63y4b cannot_install_moneydance_on_fedora_32#fqmapim cant_connect_to_ssh#ieiz8uq captain_disillusion_is_this_really_just_the_wind#fxmvr36 champions_heros_conquerors_alike_assistance_is#hex7dl8 change_the_official_name_of_the_united_states_of#h1aai3l change_the_official_name_of_the_united_states_of#h1akpmz change_the_official_name_of_the_united_states_of#h1bselj chromecast_was_overheating#g0mvyut cloned_a_120gb_ssdold_to_1tb_ssdnew_the_1tb_ssd#ghc0tju close_all_background_processes_on_an_app_exit#fo4ygkh cloud_chamber_shows_radioactive_decay_of_uranium#gdvxs5u colemak_has_replaced_all_my_other_layouts#h4zt8je colemak_has_replaced_all_my_other_layouts#h4zvve3 colemakmoddh_layout_for_linux#g4tq771 concept_a_open_source_alternative_to_big_query#hh54fpc consolidating_folders_from_various_old_drives#ibbxs2k contact_api_system_for_contact_forms#el0dbz9 contracted_video_editor_says_they_cant_provide#i7m13qw convert_zshs_aliases_to_fishs_abbr#i7xwftu copy_all_text_from_last_command#jkiy0y0 cost_of_baby_crib#he1ff92 create_a_global_shortcut_via_cli#j15h8tj creating_a_crime_heat_map#hm8imoh crewmembers_standing_inside_the_cargo_hold_of_an#i39g8ct custom_fortune#dzr9xxk custom_keybe_public_keyboard#dmubbrz custom_keybe_public_keyboard#dmubdaa custom_keybe_public_keyboard#dmubjv1 custom_keybe_public_keyboard#dmui74u custom_keybe_public_keyboard#dmxn69z cve202335934_file_downloader_cookie_leak#jqyjo7g cvs_and_the_circular_file#fggfhlx data_migration_when_reinstalling_os#j78t1ul data_safe_despite_sata_power_issues_thanks_to#j57ct29 data_sciencegis_wage_disparity_time_for_change#ftngaib day_3_of_colemak_and_still_brutally_slow#g67z1ae dbt_on_windows_any_problems#hjiqok3 dear_user_of_reddit_im_going_mental_can_u_please#ipew3bu deleted_by_user#ecekwd5 deleted_by_user#f0ozelp deleted_by_user#gabyhsv deleted_by_user#gduix4u deleted_by_user#ggl95mz deleted_by_user#ggm33z3 deleted_by_user#h78wi8r deleted_by_user#hamvuxx deleted_by_user#hb9x0j2 deleted_by_user#hfvpuff deleted_by_user#hhvawck deleted_by_user#hhvi1n6 deleted_by_user#hhvn2vn deleted_by_user#hioeqck deleted_by_user#hizdfzq deleted_by_user#hizg17p deleted_by_user#hjo83ma deleted_by_user#hl9bjir deleted_by_user#hmev9df deleted_by_user#hpe4jqy deleted_by_user#hrhven0 deleted_by_user#i4segsi deleted_by_user#i7felx7 deleted_by_user#i7x9gfw deleted_by_user#i8fl777 deleted_by_user#i8r5f31 deleted_by_user#i8wynb4 deleted_by_user#i90mulg deleted_by_user#i9g5spm deleted_by_user#ia59dbf deleted_by_user#ib7qeph deleted_by_user#ice4t09 deleted_by_user#ie13z46 deleted_by_user#ihh7j4x deleted_by_user#ioq5pk5 deleted_by_user#iq5hbga deleted_by_user#iq5hwa0 deleted_by_user#isbt4fm deleted_by_user#j5c0b8v deleted_by_user#jjwbj6p derek#f3x2j25 derek#f3x2q2a derek#f3zdc1u desktop_youtube_subscription_manager#hism7sj desktop_youtube_subscription_manager#hit8ln9 did_swiftkey_have_a_stroke#fvbq43x difference_between_store_and_data#hntpnn2 difference_between_store_and_data#hnuma1o different_names_for_different_genres#gcoxu9e disable_ctrldel_closing_tabs_when_typing_in#fnwdsc9 disk_usage_after_large_deletion#i57sbhs ditching_docker_for_local_development#comment-9r26 diy_mattresses_an_introductory_guide#h7vc3im dmesg_line_incompat_feature_flag#ielzpf0 do_people_still_use_cron_jobs_or_something#hikudd2 do_people_still_use_cron_jobs_or_something#hild84v do_you_always_go_for_the_highest_available#j2p64wl do_you_pick_based_on_the_girl_you_like_or_on_the#j5io052 do_you_store_in_mp3_flac_or_even_another#ib3l2yn do_you_tag_your_music_whats_your_method#comment-9r1u does_anyone_know_where_i_can_find_english#i7or4p5 does_anyone_remember_2011_a_site_called_music#iwd5e18 does_changing_desktop_environments_influence#frxcf7f doesnt_evilginx_tool_case_unknown_login_location#g0wwtvx dokument_sorting#j3k5g7z done_with_the_stores_need_recommendations_for_a#hb0ebzz dont_stop_at_big_tech_we_need_to_bust_big#gmi2urx download_higher_quality_versions_if_available_for#jsx5fo5 download_higher_quality_versions_if_available_for#jsycg0k dreamboat#g3g5hz2 dual_membrane_audio_driver#i52vchd during_the_australian_bushfires_any_water_source#fbr52ms dyk_shp_is_in_the_bad_place#iej6bub easiest_way_to_get_data_from_a_spreadsheet_onto_a#g2frc0i easiest_way_to_get_data_from_a_spreadsheet_onto_a#g2ftbb6 easiest_way_to_get_data_from_a_spreadsheet_onto_a#g2fuz9k ebaby#ghkbfjr eli5_why_do_we_fly_across_the_globe_latitudinally#jupw6gi elm_and_google_tag_manager#geiqtpd emoji_kitchen#iieboqs equivalent_of_zfssnapshot_directory_on_btrfs#i78m43b error_unsupported_url#jtae6ce error_unsupported_url#jte122t european_travels#fhom3d5 european_travels#fhw3hcg everything_is_gone_help#hjipyrz expanse_in_4k_holy#gdvvzc4 expat_describes_living_on_350month_budget_in_the#iq0cfm1 extremely_choppy_hdmi_audio_after_swapping_out#j0onag7 fallout_4s_trinity_tower_has_some_destructible#g2l4giw fedora_35_is_a_nogo_for_october_26_next_target_is#hhldavc fedora_35_is_a_nogo_for_october_26_next_target_is#hhm4tku fedora_35_is_a_nogo_for_october_26_next_target_is#hhmlyhv fedora_35_is_a_nogo_for_october_26_next_target_is#hhnfh1y fedora_35_is_a_nogo_for_october_26_next_target_is#hhru5nc fedora_kde_is_ugly_and_bloated#gdgx8nd fedoraos_is_best#hery4fh fedoraserver_wow#hhbt63g fell_for_a_phishing_simulation_for_the_first_time#geruehj first_presidency_statement_on_church_finances#fb9nz77 fish_completions_for_a_range_of_numbers#ichdr2d flirting_in_japanese#fzabdge for_50_million_would_you_stay_in_solitary#j7yebnw for_exploring_cities_around_the_world_at_home_and#h1k0mi4 for_some_reason_she_didnt_respond_after_sending#hj0wvp0 for_those_linux_pirates_out_there#ia94stu found_a_flying_plane_while_checking_out_faro_on#h0rhoud found_an_old_hdd_i_buried_in_my_yard_when_i_was#i4s411b found_an_old_hdd_i_buried_in_my_yard_when_i_was#i4srzfq free_video_editor_to_only_manipulate_video_length#iea21z2 french_island_of_corsica_wild_cows_took_the_beach#hamt09s from_a_711_in_allen_tx#ggxvfcd fs_read_only_after_balance#icvvwa6 fs_read_only_after_balance#icvwxmm fs_read_only_after_balance#icwrpxw future_narcotics_from_my_scifi_setting#i8p7iz9 gadget_girl#hehcj63 garbage_day#g0j9877 getting_to_attached_to_code#gavhjm1 getting_to_one_9_of_correctness_for_our#fb9obos giant_nacho_ring_hack#gduipe6 github_launches_copilot_publicly_at_10month#ida9v5v global_operating_system#gfpr898 going_to_japan_but_my_debit_card_mastercards#eo7g4j7 going_to_japan_but_my_debit_card_mastercards#eo7nvlg google_invests_12_million_in_sidequest#ir3f35p google_invests_12_million_in_sidequest#ir6y0yi got_3k_songs_from_a_visit_in_iran_from_my_driver#icvyel1 grandaddy_protected_from_the_rain#dv82fzs hackers_threaten_to_leak_80gb_of_confidential#joqemd1 hackers_threaten_to_leak_80gb_of_confidential#joskpi1 hard_drive_recs_for_feature_film#joa3hnv hardware_compatibility_with_linux_and_an_overall#i7jl5bb has_anyone_visited_arcosanti_irl#jv3454r hate_it_when_i_specifically_click_on_that_symbol#fx0bjae havana_syndrome_weed_candy_and_more_spooky#hi7g419 havana_syndrome_weed_candy_and_more_spooky#hi8tpkz he_asked_for_bee_facts_and_somehow_reddit#h4zdxb0 he_is_speed#gi9pgvc he_will_drop_production_if_scared#eg324yj hello_guys_i_need_your_help_i_tried_to_run#fprrcfv hello_guys_i_need_your_help_i_tried_to_run#fpsbc7n help_in_downloading_a_database_legocom_set#j53vapc help_in_downloading_a_database_legocom_set#j53xtgf help_me_find_a_sweet_i_ate_once_20_years_ago#j6xj383 help_me_plz#hih9dv4 help_not_your_usual_post_but_how_do_orchestras#ge4hc62 help_update_messed_up_my_tv#jrcoqj2 help_w_autostart_program_on_desktop#ejuo0xu hi_to_the_5_people_who_see_this#hbnfj2v highly_specialized_and_very_under_appreciated#el0alzn hiligaynon_language_tutor#epurg5k hmm_which_to_choose_indeed#hyznabb hmmm#haro8bd hmmm#haxb17k home_alyen#dn00jnn homeowner_turned_his_sprinklers_on_before_leaving#i0md254 horizon_forbidden_west_on_900#hz3mogp horizon_forbidden_west_patch_106#hz75qtl hose_care_center_for_presoaking_washing_pressure#h2yc7rt how_about_a_site_that_pairs_you_up_with_other#fc734e4 how_and_where_to_set_up_webgis_environment#eo4blyn how_can_i_automatically_download_videos_from_a#jth2nzp how_could_i_display_the_content_of_two_remote#idxrdab how_do_anthropologists_distinguish_religious#idh28qa how_do_i_dl_multiple_videos_at_one_time#jpltqia how_do_i_edit_existing_movies_for_hobby_reasons#hlbm1ya how_do_i_list_multiple_features_in_a_song_is#ia58yts how_do_i_make_my_brother_stop_from_wanking_so#gegs9n9 how_do_i_report_a_bad_business_that_messed_up_my#gfka2fq how_do_you_get_a_deleted_youtube_video_back_that#fzl1z8i how_do_you_hear_about_or_watch_quality_films#ed8nmfg how_do_you_name_images_and_other_files_that_would#ie4vrrz how_do_you_name_images_and_other_files_that_would#ie79j82 how_do_you_save_and_manage_random_cool_bits_of#jo8ru6d how_hard_do_you_think_the_riaa_would_work_to#gadvaps how_is_ai_changing_the_gis_industry#jvlj9c4 how_long_did_it_take_for_you_to_speak_fluent#eohtfe9 how_long_will_a_hdd_last_in_cold_storage_dont#ja9kich how_long_will_a_hdd_last_in_cold_storage_dont#ja9yjcs how_much_did_your_uni_grades_effect_your_career#gecjk30 how_much_does_it_cost_to_get_a_4year_degree_in#g07fuze how_necessary_is_physical_cash_in_japan#jwb0a5h how_should_i_separate_audiobooks_from_ebooks_what#i6nzh8q how_should_i_separate_audiobooks_from_ebooks_what#i6o18y1 how_should_i_separate_audiobooks_from_ebooks_what#i6o5ec4 how_should_i_separate_audiobooks_from_ebooks_what#i6t20oo how_to_apply_for_a_job_when_your_dad_is_the#g4g5wuk how_to_apply_for_a_job_when_your_dad_is_the#g4ie04b how_to_build_an_ai_which_asks_questions_on_stack#ea1fzaa how_to_build_an_ai_which_asks_questions_on_stack#ea1g3k1 how_to_build_an_ai_which_asks_questions_on_stack#ea1g9y7 how_to_build_an_ai_which_asks_questions_on_stack#ea1gfs9 how_to_build_an_ai_which_asks_questions_on_stack#ea1gn19 how_to_build_an_ai_which_asks_questions_on_stack#earvxn6 how_to_change_capslock_to_backspace#g754e7o how_to_defuse_a_naval_mine#hcj2j40 how_to_delete_all_your_files#g2l361k how_to_generate_a_h_from_a_configure_script_with#icf0jue how_to_get_old_fonts_back#g9cuwbe how_to_halt_if_live_stream_is_not_finished#ju08q4a how_to_live_anywhere_in_the_world#eouicsp how_to_set_initial_position_for_new_windows#iebmq53 how_to_simulate_disk_failure#j5clv9d how_to_simulate_disk_failure#j5d06d1 how_to_simulate_disk_failure#j5d44kk how_to_simulate_disk_failure#j5dn7q8 how_to_tell_youve_just_moved_into_a_good#jv7w5lf how_to_use_ytdlp_advanced_tutorial_guide_2023#joj5ta2 how_to_use_ytdlp_advanced_tutorial_guide_2023#joohge8 how_would_i_go_about_detailing_this_so_it_doesnt#hcnce7h how_would_you_update_300000000_records_out_of#fomex5s hr_just_keeps_getting_more_and_more_demanding#em9tey3 hr_just_keeps_getting_more_and_more_demanding#em9tjfr huh#hj3vxly i_am_cat_i_pose_pesky_humans#heg2e5p i_bought_this_burger_king_watch_around_2001_and#hr4bs3l i_cant_believe_i_missed_out_on_linux_for_so#jsx72do i_cant_tell_if_my_eyes_are_green_or_blue#hhr8tjq i_changed_my_terminal_to_ask_for_a_wish_instead#ipqx3ak i_didnt_like_this_one#g2o0n37 i_dont_trust_linux_adoption_numbers_out_there#f7xp8yc i_feel_like_this_is_something_ken_m_heavy#i7xvsgg i_fired_a_guy_who_didnt_work_for_me#fycykis i_found_an_encrypted_thumb_drive_and_i_need_help#gf3pvqd i_hate_paying_rent_and_i_dont_want_to_pay_a#hl74luh i_have_a_skin_condition_called_dermatographia_due#hpto4a2 i_have_an_idea_for_an_app_feel_free_to_take_it_if#eodnpjd i_have_no_idea_what_im_getting_myself_into#i6zhssy i_have_no_words#fsfx2eu i_have_the_best_idea_since_amazon_tell_me_whats#h0mo95t i_installed_fedora_on_a_friends_oldish_laptop_and#hhpgv5v i_just_found_out_albert_einstein_was_a_real_person#h9zrpcv i_just_found_some_spec_on_my_bed_and_i_noticed#hh1ao7n i_m19_have_a_thing_for_japanese_women_and_would#gbwrd3g i_made_a_program_that_gives_me_unlimited_storage#ge4iidi i_made_a_tool_hidscan#jp9v3aq i_made_a_wikipedia_cowsay#g03ntlc i_made_a_wikipedia_cowsay#g03p29v i_made_a_wikipedia_cowsay#g03qe37 i_made_a_wikipedia_cowsay#g07ex1g i_never_really_liked_spotify_so_i_made_a_program#ikfehqt i_never_really_liked_spotify_so_i_made_a_program#ikg7zk1 i_never_really_liked_spotify_so_i_made_a_program#ikg8he3 i_never_really_liked_spotify_so_i_made_a_program#ikhfcj6 i_never_really_liked_spotify_so_i_made_a_program#ikhfmah i_never_really_liked_spotify_so_i_made_a_program#iknjyc0 i_received_a_strange_mail_help_me_crack_the_code#hgk6bv0 i_ruined_my_boss_life#jw1kamv i_spent_most_of_my_teens_and_early_20s_trying_to#gi51luk i_started_my_first_it_job_at_help_desk_2_weeks#eo4crak i_used_my_channel_to_document_crimes_and_violence#gli10rk i_used_my_channel_to_document_crimes_and_violence#gli1iq5 i_used_openstreetmap_and_other_public_datasets_to#gcgosri i_will_not_give_a_fuck#hiup13v i_wish_i_could_tell_google_home_when_i_opened_my#iad2wn7 i_wish_i_could_tell_google_home_when_i_opened_my#iadebot i_wish_i_could_tell_google_home_when_i_opened_my#iafe70m i_wonder_whats_the_answer#g3zb1q8 id_love_some_uiux_opinions_on_my_alternate#eodqzsl ideas_for_a_lets_split_case_design#dl9l5v7 if_cats_eat_your_face_when_you_die_why_dont_they#hrquiqs if_i_can_give_a_tip_as_a_programmer#j2vzsum if_im_downloading_an_album_it_gets_seperated_into#fr603m5 if_three_bottoms_hooked_up_would_that_be_called_a#hhyaua4 if_you_got_offered_1000000_but_it_meant_that#ew4dwmy if_you_got_telepathically_whisper_a_sentence_to#i14cvyz if_you_had_a_100k_remote_work_job_where_would_you#h2fkb8d ill_never_remember#iej5vll im_a_private_tutor_for_a_strange_girl#jt4xmt6 im_confused_with_the_hourglass_sanatorium_1973#jvox4xh im_just_going_to_push_this_code_and_see_how_long#gknszyc im_looking_for_a_version_of_linux_to_switch_to#ftjbizz im_new_to_termux_so_suggest_me_what_cool_stuff_to#j57f9a8 im_new_to_termux_so_suggest_me_what_cool_stuff_to#j57lkxj im_new_to_termux_so_suggest_me_what_cool_stuff_to#j58ruga im_new_to_termux_so_suggest_me_what_cool_stuff_to#j64qfyn imagine_how_explosive_car_crashes_were_in_pre_war#h2yekc1 in_2000_18_year_old_pete_buttigieg_won_a_national#fh2he5t in_2014_i_dreamed_of_a_very_particular_shape_im#ig1xnti in_a_new_study_researchers_at_university_of#h2eg5f3 in_case_of_fire#i0xoup1 in_monopoly_if_no_one_ever_buys_a_property#j9zbt3o in_monopoly_if_no_one_ever_buys_a_property#j9zckbu in_my_dream_last_night_microsoft_released_a#h3y90ih in_need_of_help_creating_a_data_text_file#itvkus2 in_tehran_2020_on_apple_tv_no_one_uses_apple#haffhm8 in_this_representation_of_flags_register_what_do#g87oc9s incremental_book_reading#g2fvis6 incremental_book_reading#g5oiuff indian_missile_hits_pakistan_due_to_technical#i0bpq1h inhibiting_kdes_powermanagement_sleep_when_mpd_is#i78l247 initial_renders_of_keyboard_and_mouse_connected#gebzowe insane_flying_skills_or_cg#hgboxwk internet_archive_responds_to_recording_industry#jwcczrt is_it_ok_to_migrate_to_fedora_now_or_wait_for_the#hgqhe00 is_it_possible_to_create_something_like_sequence#i3z13z5 is_it_possible_to_order_a_pinephone_pro_in_china#hnnu3dm is_it_possible_to_order_a_pinephone_pro_in_china#hnow1wh is_it_possible_to_recovery_deleted_file#ib7pwbw is_it_possible_to_trimconcatenate_a_url_with_ytdlp#jv2admt is_it_possible_to_use_mpv_as_a_music_player#ipxepko is_it_true_that_footage_will_survive_at_lower#ib9eggs is_moving_from_a_de_role_where_writing_spark#fiq5uph is_our_coding_challenge_too_hard#hih8zl6 is_raid_really_worth_it#juuotef is_raid_really_worth_it#juwkcug is_raid_really_worth_it#juwl9ux is_raid_really_worth_it#juwoq6q is_raid_really_worth_it#jux36hc is_soulseek_down_i_cant_ping_the_server#i6jdvl5 is_there_a_100_accurate_globe#io8fl3h is_there_a_calculatorspreadsheet_to_compare_long#dykdc6z is_there_a_website_for_finding_flights_going_to#jedi2di is_there_any_alternative_to_lutrons_smart_blinds#ia559ga is_there_any_remote_job_board_that_focus_solely#iuetq5m is_there_any_software_that_goes_through_all_the#jqxacw1 is_there_any_wadsworth_site_working#ib05lmc is_there_any_wadsworth_site_working#ib1w5rw is_this_not_the_perfect_fleshlight_storage_what#j0w5wha is_this_not_the_perfect_fleshlight_storage_what#j0wmh5g is_this_photos_that_is_violence_these_photos_i#hecky0o is_this_photos_that_is_violence_these_photos_i#hecm11m is_this_real#g6xdg4w is_this_real_or_could_it_just_be_editing#gfpt17g is_this_what_japanese_men_are_like#fbr3xis is_this_what_japanese_men_are_like#fbsyb4t is_volume_spanning_multiple_different_drives#i48kvlx isometric_style_pizza_what_do_you_think#g9s6hll issue_with_routemultiple_destinations#eo0vysa it_is#h21bud3 it_just_feels_like_an_impossible_task_sometimes#itqcad4 it_really_bothers_me_that_ill_never_be_able_to#dlwjurr its_just_that_your_absence_makes_me_grow_an#i7z895l ive_been_excessively_commenting_my_code_since#fxmr6n6 janet_showing_up_in_the_comments#gdujjes japan_proves_yet_again_theyre_decades_ahead_of_us#h343xdq japanese_english_nadesico_class_mobile_battleship#ioi4zvs japanese_scientists_create_vaccine_for_aging_to#hoh8nlz japans_islandshaped_curry_inflames_tensions_with#hgj7419 joined_ts_gang_today#g3g5qmz just_finished_my_first_rewatch_i_have_questions#j5b4l9x just_found_out_my_camera_has_2_protective_films#hgke2qq just_took_my_first_salaried_position_at_42000_a#dp33muz just_watched_a_vice_news_report_on_the_silwan#h11ati9 just_watched_a_vice_news_report_on_the_silwan#h16u38w kde_eats_your_ram_and_looks_pretty#ejdlcq6 kde_plasma_it_is_not_much_but_it_is_home#j85w1ki kde_plasma_it_is_not_much_but_it_is_home#j8acdwd keep_a_backup_of_the_internet_on_the_moon#h3csgdc kentucky_man_accused_of_stealing_police_k9_luring#g4ipe85 kinda_yes#gb48pw4 lagging_on_second_monitor_pop_os#i95yffz lars_homestead_star_wars#idgxdoa late_nite_me_digital_2022#j2528me leanfired_folk_of_reddit_do_you_like_where_you#hmbfqs7 leanfired_folk_of_reddit_do_you_like_where_you#hmbjrag leanfired_folk_of_reddit_do_you_like_where_you#hmdewxm leanfired_folk_of_reddit_do_you_like_where_you#hmemfoj leanfired_folk_of_reddit_do_you_like_where_you#hmen9qy leanfired_folk_of_reddit_do_you_like_where_you#hmeofty leanfired_folk_of_reddit_do_you_like_where_you#hmet0xr leanfired_folk_of_reddit_do_you_like_where_you#hmuuduu learn_phthon_and_apply_to_gis#jsw447s leaving_japan_high_quality_valuable_memorabilia#hgxi9da life_is_so_boring_and_i_dont_seem_to_get_along#j5uchhh life_is_so_boring_and_i_dont_seem_to_get_along#j5w9v6p linux_for_phones#ia1ny0x linux_for_phones#ia1ozss linux_sessions#jux8i32 loaded_question_for_under_1000_what_camera_would#gezbhjh looking_for_a_good_note_taking_app#comment-a5kr looking_for_my_next_location_where_is_the_most#hhuwolo looking_for_recommendations_on_a_portable_high_performance_laptop#comment-a5wk lotte_abc_the_keyboard_snack_a_chocolate_cookie#ik0l1oz lpt_dont_take_chances_with_bed_bugs_when_staying#i02yd68 lpt_never_scan_random_qr_codes_just_left_in#hy3twni lua_repl_inside_mpv#iwnalfg lua_scripting_subswithmatchingaudiono_but_without#iwnijlc macos_sonomalike_widget_dimming_in_plasma#jnl11xz made_this_and_thought_it_would_belong_here#ftnbcub made_this_and_thought_it_would_belong_here#ftr5p0j malloc_fail_in_bash_what_happened#g1pwooj man_attacks_korean_american_employee_shouts#fv3zxkb managing_difficult_software_engineers#jw6rk8r map_of_the_postwar_poland_i_styled_after_the#g4ipi71 map_of_the_postwar_poland_i_styled_after_the#g4ipm4r map_of_the_postwar_poland_i_styled_after_the#g4sf88j massive_google_ads_export_to_bigquery_problems#fwggtkn mate_desktop_environment_122_released#eiv0smw mbti_inside_e1_what_happens_if_you_put_16#iscaady mbti_inside_e1_what_happens_if_you_put_16#jrf6nrn medical_tourism_in_saipan#gvw249g mentorship_for_guys_seeking_a_japanese_girlfriend#hb1owpl meta_i_have_a_processor_chip_greg_could_you_milk#hiuzq49 mickey_mouse_from_above#h3a4sop microsoft_acquires_activision_blizzard_for_687#htea48y milf_cereal_with_the_strawberries#hyx1rgk mind_fk#hq3b1xy mint_wisebanyan_syncing_workaround#dtf1ydt modeling_many_to_many_relationships_in_bigquery#h06zoua modeling_many_to_many_relationships_in_bigquery#h0726fe monday_daily_thread_project_ideas#jpn1dhd more_like_awesome_off_brand#gnswlnq morty_is_actually_insanely_intelligent_and_doesnt#hcozm9r most_common_language_spoken_at_home_other_than#hgkhtyv most_off_the_beaten_path_places_youve_been_a#hgn1g3i moved_fedora_35_nvme_from_amd_laptop_to_an_intel#hyvkw5d moved_fedora_35_nvme_from_amd_laptop_to_an_intel#hyvl2ex moved_fedora_35_nvme_from_amd_laptop_to_an_intel#hyvogzs moved_fedora_35_nvme_from_amd_laptop_to_an_intel#hyvpyuy moved_fedora_35_nvme_from_amd_laptop_to_an_intel#hyxm63s movies_without_obvious_appeal#comment-9pnv moving_for_23_months_to_tokyo_or_kyoto#eeolqlj moving_for_23_months_to_tokyo_or_kyoto#eeombdv moving_to_central_illinois#iln4j7m my_9_year_old_son_just_asked_me_to_pretend_i_was#hsu9whi my_best_way_to_deal_with_inflation_yet_imo_can_be#h8h7zy6 my_christmas_present_i_got_from_my_brother#ggy3ecw my_chrombook_just_received_a_final_software#icy7a78 my_collection_of_python_and_bash_scripts_i#i9h97zz my_drawing_of_some_random_street#hd9ygsp my_entire_workprint_collection#jv6mvrl my_entire_workprint_collection#jv6myyv nasa_is_opening_a_vacuumsealed_sample_it_took#i01bpyz need_advice_for_travel_budgeting_website#ecf3rdd need_advice_for_travel_budgeting_website#ecf8q2y need_advice_for_travel_budgeting_website#ecfgh74 need_advice_for_travel_budgeting_website#ecfhhgo need_advice_for_travel_budgeting_website#ech5ghk need_advice_for_travel_budgeting_website#ed2kw1m need_some_help_with_youtubedl_output#gd83pfc netflix_has_a_page_where_you_can_request_tv_shows#e43015j new_xkcd_bad_map_projection_abslongitude#jvb00xg newbie_question_on_file_compression#jpxxt7u next_winter_my_husband_and_i_plan_to_spend_a_year#gd4qbuc no_space_for_metadata_raid1c3_raid1c4#ibyirov no_space_for_metadata_raid1c3_raid1c4#ibyvlvi no_space_for_metadata_raid1c3_raid1c4#ivgfeu1 no_space_for_metadata_raid1c3_raid1c4#ivi4en8 no_space_for_metadata_raid1c3_raid1c4#jmcoxyi no_words_needed#i5i6k5v noice#h1y002w norilsk_russia_a_city_so_polluted_that_all#ek4iztj now_this_one_is_relatable#g2o12o4 oc_custom_fortune_from_notes#dzrabrj oc_custom_fortune_from_notes#dzrep0h oc_custom_fortune_from_notes#dzsqsk1 oc_reddit_traffic_by_country#hbksu2e oc_sooo_who_is_going_to_take_me_from_behind#g3pej5v oc_ufo_reports_in_the_contiguous_united_states#ip0n44d oc_us_presidential_election_polls_2020_current#g1ejnrq odin_is_with_us#g1ge7rw okay_the_connection_logo_ethernet_or_wifi_same#fzl0hts okay_the_connection_logo_ethernet_or_wifi_same#fzlmrw5 old_goldcopper_crayola_crayons_that_turned_green#hewlpkq online_or_software_video_editing_recommendations#i9044ho opinion_can_we_stop_recommending_less_user#fr92tcu organize_visualize_files_as_graph_or_table_using#j5kqdek organize_your_media_when_it_is_too_big_to_think#ikc1i57 organize_your_media_when_it_is_too_big_to_think#ikfebyh organize_your_media_when_it_is_too_big_to_think#imuir5o osc_what_is_the_f_beside_the_volume_control#jw3bobk ouch#hii0yeg permanent_archival_formats_do_they_exist#comment-9feo permission_missing_on_tasker#iyulis5 personal_youtube_video_archive_stats_19_gone#iqx3mbz picked_up_this_retro_tvradio_after_a_bit_of#h6i6hmk picture_sorting_software_with_folder_move_hotkeys#je3v1ys planning_to_drive_from_iloilo_city_to_belison#ed7sk7v plasmaxmonad_a_two_year_vision_complete#eeom16p plasmaxmonad_a_two_year_vision_complete#eepgtx8 playlist_download_issue#ibhli9v playlist_download_issue#ibi3zr3 please_help_how_do_i_get_ytdlg_to_download_whole#jqrbuwn plsql_developer_wanting_to_become_a_data_engineer#hm76vhg plsql_developer_wanting_to_become_a_data_engineer#hm8aeid postgresql_13_released#g6g6now potential_fixworkaround_for_people_stuck_on#g23sb91 preemptible_gpu_limit#i8tlx9h prices_during_covid_in_asia#hc1zs10 problem_with_global_menu#jtwi0sk problem_with_global_menu#jtyipzz pulse_15_amp_support#hgf4g8o pwls_and_wls_parameter#ird1pw7 pwls_and_wls_parameter#irrwtg1 python_i_use_a_package_of_ffmpeg_how_do_i_make_it#id8w0gb q4_2022_intel_tech_support_thread#j0olzpx qmk_tap_dance_and_macros#dl9jj9i quarterly_salary_discussion#j53xd5r query_more_than_one_days_worth_of_mail#fk8x7zk questions_about_budget_debt_and_investments#edaaw42 raid10_vs_raid1_redundancy_on_515_kernel#i47fabd raid10_vs_raid1_redundancy_on_515_kernel#i47mjyn raid10_vs_raid1_redundancy_on_515_kernel#i4ap3q8 raid10_vs_raid1_redundancy_on_515_kernel#i4dx5vq raid_10_metadata#hzy2yno random_find_in_hong_kong_wanchai_computer_mall#h2vnjb7 random_unrelated_knowledge_sharing#inc7b7g random_unrelated_knowledge_sharing#inc7ont raster_sources#h2yzyr9 rate_limiting_by_ip#ieiyyup recommendation_needed_for_hotel_booking_sites#er7b2ce recommendation_on_products_that_matches_your#gd8a542 recommendations_for_firsttimers_filling_the_gaps#dttamxs recommendations_for_firsttimers_filling_the_gaps#dttcyx3 recovery_procedure#ibqjjbu recovery_procedure#ibqstuv recovery_procedure#ibr2zgl reddit_could_go_public_by_march_and_wants_a_15#hskej0q reddit_is_deleting_thousands_of_old_locked#ie7e7zz reinit_alpinejs_after_html_injection#iecvzm4 reinit_alpinejs_after_html_injection#jn69fhc remember_to_start_nichijou_episode_1_tonight_at#fcpbu7r remoting_into_desktop_without_screen_but_doesnt#jlmek0v request_are_these_numbers_accurate_cause_goddamn#hzbwmh1 request_cells_and_humans_in_the_language_of#g4bfkuw request_for_rswedengonewild#i7b6qr6 request_help_abt_laptop#fwtqmuf request_how_long_would_it_take_to_remove_a_leak#h1z1f21 request_is_there_a_device_that_can_download_my#g67zywi request_is_there_a_way_to_hide_a_program_in#ggyt1e5 request_remote_control_remote_management_tools#ejforog restaurants_where_talking_is_not_allowed_you#jghbx2a roast_me_this_is_how_i_keep_my_data_177tb#iw3ww1c rough_itinerary_for_eloping_to_japanokinawa_late#he67z8r rough_itinerary_for_eloping_to_japanokinawa_late#hechc5i rstudio_on_macbook_m1#gh1c8u9 russia_anti_war_protest#hzij600 russia_anti_war_protest#j5kp0jj ryanair_wont_refund_me_sure_i_fly_for_free#hnun1aq santa_marta_colombia_the_room_is_a_bit_grungy_but#hgqhrgi saw_this_on_fb_with_someone_asking_for_a#ge4btia saw_this_on_tik_tok_honestly_surprised_it_worked#ggq1lm4 school_uniforms_around_the_world#ht36yqo scihub_now_a_browser_extension_that_gives_you#fp4xdkg script_suggestion_post#j3476cm second_display_just_disappeared_and_im_baffled#fo9rkkw second_display_just_disappeared_and_im_baffled#foekhp3 selling_pinephone_3gb_with_dock#id2ep5h serverless_gis#isbx99d sett_kitty_as_desktop_background#i7v6mcj share_weekly_trial_offer_and_free_box_codes_here#gg6ogjg she_didnt_read_the_instructions_after_unboxing#hh1572u shefali_vaidya_bbc_covering_india_covid_deaths#hap0p47 shellrunner_now_allows_setting_env_variables_when#g14i7h1 short_and_sweet_wish_there_was_more_of_this#fwtw91x should_i_be_concerned_about_this_test_done_in_my#hee4t3n should_i_be_concerned_about_this_test_done_in_my#heeopu5 should_i_return_my_new_4tb_seagate_hard_drive#juywwyb shout_out_to_opensuse_kde_maintainers_and#icy6gyk simulation_and_modelling_project_music_as_a#i9kighz so_i_found_out_a_cool_idea_on_konslole_where_you#ic5bmqg so_i_have_an_ergodox_that_i_rarely_use_should_i#fiie06o so_i_just_switched_from_windows_to_fedora_37#j2y701s so_when_are_we_doing_somthingike_this#hpase3l softwareapps_for_gooning#io3ds2u softwareapps_for_gooning#ioze8be some_api_attributes_what_do_they_mean#ird1qvr someone_just_discovered_echoes#givvwiy something_always_bugged_me_about_rstudio_layout#fs9epe4 something_always_bugged_me_about_rstudio_layout#fs9eynz something_always_bugged_me_about_rstudio_layout#fsaq5vz something_always_bugged_me_about_rstudio_layout#fszdkaz sort_3_000_000_000_lines_by_most_repeated_one_via#idpajkx sort_3_000_000_000_lines_by_most_repeated_one_via#idpeasv space_allocation#i9vjg1o spaghetti_chicken_strips_covered_in_tomato_sauce#fj8zjct spaghetti_chicken_strips_covered_in_tomato_sauce#fj909ny spectrum_constantly_sends_me_messages_as_urgent#hnuydn2 spending_about_2_months_this_summer_going_to#ed7rqe3 split_king_adjustable_options#h80ydn4 spoilers_the_forbidden_west_and_where_horizon#i0clqx6 starbucks_shipping_container_store_hualien_taiwan#ice4w33 starting_my_first_highly_modded_new_vegas#ejeu6i0 stranded_french_tourist_makes_ends_meet_by#gkofxis strange_font_issue_in_notebook_instance#i5tb1yj streaming_your_own_music_library_software_hosting#i53he1x streaming_your_own_music_library_software_hosting#i547ptj streaming_your_own_music_library_software_hosting#i5510l3 strong_and_beautiful#ggne5jj struggling_to_understand_file_storage_and_block#ibzsln5 stuttering_download_speed_using#gjb6lg2 subject_a_genius_solution_for_travel#ecemgqg suggestions_for_500_budget#i0ckuyr sunday_daily_thread_whats_everyone_working_on#jpi7k3a sweden_and_covid19_low_threshold_herd_immunity#g3ek2gd switching_to_virtual_ttys_in_linux_not_working#idflpqz system_605#f003t3j taking_advantage_of_my_rather_unique_pegboard#gnswupq terminal_struggles#g1c127o thank_you_guys_you_are_the_real_heroes#fpd3n8h thanks_fedora_devs#fvmexu4 thanks_for_clarifying_so_i_can_see_whats_wrong#eprt6d9 thanks_for_f32#fprqt4g that_sounds_nice#hqzqk7i the_2021_state_of_digital_nomads_the_average#hgfjgf6 the_batmobile_is_likely_uninsured#ipqw4pq the_best_way_of_saving_your_code#ee9izrx the_boy_who_shot_the_sheriff_herbert_niccolls_the#fiio69w the_complexities_of_a_shitpost#fancat7 the_complexities_of_a_shitpost#fao0g9t the_complexities_of_a_shitpost#fao0vj9 the_complexities_of_a_shitpost#faqfphf the_crop_module_is_not_working_for_me#het0jtn the_future_of_humancentered_design_education#hhng0f6 the_meaning_of_the_name_engerraund_serac_vincent#fnie3gh the_more_i_learn_especially_about_ethics_and_self#h2dz0lb the_protonpad_aka_the_everything_macropad_i#gf54quh the_verge_photographing_headsets_in_blazing#hkflhqn the_white_board_is_difficult_to_master_but_not#fo4xs0n these_antique_cookie_cutters_that_feature_an_axe#hppmtff theyre_doing_their_best#hba32rf thinking_of_switching_to_icey_island#jpierv6 this_beautiful_art_is_damn_interesting#egcrrpn this_bench_outdoor_of_a_dive_shop_is_made_with#hpypagg this_bench_outdoor_of_a_dive_shop_is_made_with#hpyr0yi this_car_usb_adapter_has_a_fake_power_display_its#hu8fpa9 this_industrial_vent_thing_in_the_middle_of_a_park#i86tdh1 this_is_how_a_b17_ball_turret_gunner_did_his_job#hzn1nw6 this_is_how_our_is_spent#ieqw5r0 this_is_the_start_of_something#ggndxz3 this_is_the_true_face_of_zionism_racism_is#h2a4nyx this_pill_of_pills#fzl64l6 this_update_screen_is_bringing_back_windows#gj2e8fp those_of_you_with_100tb_what_do_you_do_for_backups#ja9pz7g throwback_thursday_review_adrift_in_tokyo_2007#gk2nzst til_in_english_th_at_word_onset_is_pronounced#i5tldzn til_in_the_1820s_a_cherokee_named_sequoyah#eodmwyo til_that_japan_has_so_many_ghost_houses_that_they#h32tigr til_that_when_usps_parcel_post_began_a_banker#hgy5ygz tildes_video_thread#comment-9tws tim_city_comedy_29_pages#j4n9yvl tmux_is_a_godsend#g14imgv to_cook#g3tp1fo to_give_the_husky_a_bath#gfhc8hc to_write_stop#e68rok8 tokyo_sapporo_osaka_kyoto_in_2_weeks_too_ambitious#gact87e took_an_old_ibm_hard_drive_from_the_80s_and#iaaj7ud tool_to_findlistautorename_non_usascii_characters#j540pds top_level_file_hierarchies_to_facilitate_access#id8g3ta torvalds_said_that_linux_is_getting_huge_and#f94r1b7 toy_recommendation_for_less_endowed#jossvln tpt_for_websitesprograms_that_ask_you_to_upload#fnyyety tpt_is_there_an_audioonly_app_for_youtube_on_ios#fqt7sn1 tpt_request_can_forwarded_emails_be_altered_or#gadvni4 tpt_request_can_forwarded_emails_be_altered_or#gadw6v9 tpt_request_what_are_the_best_laptops_for#hn5lasg tpt_you_can_searchenter_a_url_after_opening_a_new#fychkli track_new_files_newfilestxt#jtjxi4j tracking_movie_collection_via_spreadsheet#hninckj transferring_data_from_external_hard_drive_to#jpoo0ay trying_to_understand_moebius_style_what_does_it#jdz19lz turning_an_old_phone_into_a_google_home_speaker#id6k0kb turns_around_dies#givvgxj turns_around_dies#giwq1tv tuxedo_hiking_up_prices#hhtdf4a tv_tuesdays_free_talk#comment-9tmh twelve_monkeys_1995#gabypql twelve_monkeys_1995#gacehkb two_people_dress_up_as_the_fbi_to_break_into#hkh2onx two_redditors_three_seashells_at_a_colorado_truck#hrzvbxa type_of_short_movie_recorded_with_a_180_degree#ggtsevs ubaid_lizardpeople_figurines_presumerian_6500#hsk21da ulpt_how_can_i_make_my_corporate_laptop_barely#jtbp12m ulpt_if_a_meeting_is_getting_too_boring_stand_up#er1f0zj ulpt_if_you_are_ever_late_to_anything_just_say#fdacm8b ulpt_request_an_easy_way_to_obtain_all_sign_up#hgj813r ulpt_request_can_i_keep_this_incorrectly#hc2jp6s ulpt_tired_of_joining_online_sessions_just_for#fr7bwqm unconventional_method_for_storing_data_for_my_mom#jnq4mjo unexpected#hde3kkq unix_task_spooler_useful_for_youtube#gbc7mhy unix_task_spooler_useful_for_youtube#gbc7r1z unix_task_spooler_useful_for_youtube#gbmwmz2 unnesting_an_array_within_an_array#hfhgpd3 unpopular_opinion_on_red_hats_recent_conundrum#jq2n6eo usbc_charger_for_pulse_14#hi8ujf4 use_a_synced_folder_on_your_cloud_storage_as_the#jo8wl64 using_external_hdd_for_running_programming#i7fz7g4 using_para_do_you_use_it_for_every_platform_youre#icy10xk using_para_do_you_use_it_for_every_platform_youre#icy6tu6 usual_hate_aside_i_thought_this_was_pretty_funny#hiv18wd usut_h_pmk_dsa_sublimated_tkl_base_pbt_keycap_set#dldwu26 various_i_hope_your_is_allowed_here_because_the#hhpqho5 vaulttec_promotional_materials_from_fallout_1#ed7sby8 vaulttec_promotional_materials_from_fallout_1#ed7so2h vietnam_visa_extension#fpzzop3 virtual_tourist#i7pgx27 visualization_of_computer_keyboard_shortcuts#fwts8oo wait_for_the_density#hgcrih1 want_to_learn_a_fp_language_but_cant_decide_which#fi7jgwj war_olympiad_a_way_for_countries_like_russia_to#isoyx2b warning_18#h7a10qf warning_18#h7csjef was_mindlessly_browsing_crate_and_barrel_while#ftghbcu ways_to_make_or_save_money#idtakbq ways_to_make_or_save_money#idtck96 we_have_to_be_careful_why_are_masks_still_worn_in#i95ytnt we_need_to_preserve_hong_kongs_history_before_it#g9jtx61 website_this_is_the_most_conscientious_youtube#g4m63xf well_boys_there_might_be_another_one#h8udlk9 well_thats_futuristic#fmbfyws well_thats_futuristic#fmeke2f were_taking_the_party_from_twitter_to_reddit_to#hbvato0 what_a_stupid_time_to_be_alive#hplg3uq what_are_some_purchases_that_increase_your#j0w7chf what_are_the_best_nsfw_lifehacks#j105xim what_are_your_favorite_ways_to_cook_eggplant_or_dishes_containing_eggplant#comment-a59h what_could_grieving_in_stereo_possibly_mean#hxinorx what_creative_projects_have_you_been_working_on#comment-9pot what_do_you_think_is_the_most_annoying_part_of#hfb4bad what_fact_blows_your_mind_everytime#do1oia4 what_fact_blows_your_mind_everytime#do1opxs what_games_do_you_most_wish_had_a_remake_or_a_sequel_or_both#comment-a4da what_happened_to_naturalearthdatacom#hkps4om what_ide_do_you_think_is_best_for_python#j0oku3x what_is_an_overrated_editing_styletechnique_for#i9ki56t what_is_legal_now_but_likely_to_be_illegal_in_12#ho7sarx what_is_the_extrovert_equivalent_of_a_library#enlt2zu what_is_the_term_for_tech_that_doesnt_have_any#gduiyy6 what_is_this_vessel_its_extremely_heavy_probably#heryjfe what_is_your_favorite_and_least_favorite_south_or#hgp50w1 what_kind_of_present_to_give_to_a_host_family#fdfy1dy what_place_will_burn_a_dvd_for_you#g4pokeg what_programming_technical_projects_have_you_been_working_on#comment-9pli what_programming_technical_projects_have_you_been_working_on#comment-9u1m what_should_i_tell_her#h8uceyy what_software_do_you_prefer_to_read_mac_formatted#g5wvzd6 what_text_comparison_software_do_you_use#comment-9plt what_video_editor_does_jack_stauber_use#i68g28h what_video_editor_does_jack_stauber_use#i6c2mhs what_would_be_100_times_worse_if_it_were_invisible#hezcpbi what_would_be_the_ramifications_if_i_went_to_the#iubkm3i what_would_become_100_worse_if_it_were_to_become#hxwf3qd what_would_make_you_quit_reddit#hmtilpd what_would_make_you_quit_reddit#hmtjhgs what_would_you_add_and_what_would_you_remove_from#i5v804z whatre_your_takes_on_this#ekaubyh whats_a_conspiracy_theory_that_you_100_believe_in#hpyg29y whats_in_my_deceased_friends_secret_vault_wtf#g3tq13b whats_stopping_an_agi_from_hacking_into_every#gd85n2l whats_the_best_colemak_mod_or_vanilla_for_an#ggys9rx whats_the_meanest_thing_a_woman_has_ever_said_to#i2bd1k0 whats_this_dotted_line_represent#ilnmuxl whats_this_dotted_line_represent#iloefny whats_this_thing#isdp2xb whats_your_preferred_method_for_handling#i9gz3jf whats_your_recommendation_for_a_good_app_or#edab8tv when_shes_curvy_tattooed_and_smiles_when_you#hcphlrn when_should_someone_be_able_to_watch_the#is36j8v when_the_movie_starts_at_745_and_its_740_and#e68skn5 where_can_i_watch_short_films_nominated_in_cannes#idsh40n where_do_i_start_learning_and_what_do_i_learn#gc7rz9p where_do_you_guys_go_for_creative_inspiration_for_projects_and_activities#comment-a6oh where_do_you_guys_go_for_creative_inspiration_for_projects_and_activities#comment-a6q3 where_do_you_guys_hunt_new_music_from#fj8zpi0 where_is_youtubedl_now#gbnd3ao where_will_the_next_set_of_young_selfmade#fr0nrwe where_will_the_next_set_of_young_selfmade#fr0nsxr where_will_the_next_set_of_young_selfmade#fr3m5dv which_compression_level_should_i_choose#jutmpzx which_programming_language_to_learn_14yo#g06ce3b whiteunderwearharshnoisecom#iduw7ln who_can_relate#gzl34y3 who_uses_the_window_and_tab_functions_in_kitty_is#iebkm4y wholesome#gdq03lq wholesome_redditors#f3wttat why_chrome_browser_on_ipad_doesnt_offer_text#iphvxgq why_did_this_sub_die_why_did_it_go_from_a_popular#dpi3gzu why_did_this_sub_die_why_did_it_go_from_a_popular#dpi4gv7 why_didnt_you_deliver_my_letter#h8v81bq why_does_it_seem_like_that_in_society_that_guys#dl79qj2 why_does_it_seem_like_that_in_society_that_guys#dl7vpce why_does_yt_allow_ads_that_run_this_long#gckygg6 why_hasnt_it_become_a_cultural_norm_to_bank_our#ib9py8u why_is_learning_data_engineering_so_opaque#hmes0tf why_is_there_a_stigma_in_the_west_about_eating#igcscp5 why_is_wayback_machine_so_slow_right_now#giijhn5 why_isnt_amazon_unlimited_a_music_option_on#hislv92 why_just_why#ht1ofy6 write_a_best_selling_novel_where_publisher_uses_a#gnofi16 xd75_a_60_ortholinear_keyboard#dm4hm9e xfce_purplish_xubuntu_3#iehfccr xfinitycomcast_now_caps_your_data_at_12tb_saying#imaftag xklb_v118_subredditredditor_databases_download#isbu0wa yark_advanced_youtube_archiver_and_viewer#ipei0dy yark_advanced_youtube_archiver_and_viewer#ir1pbu9 year_abroad_travel_insurance_recommendations#icvu7lq yes#g01gui6 yes#g03tyah yet_another_ytdlp_linux_script#islpdi3 you_are_gifted_unlimited_french_fries_but_are#i1wfkks you_have_unlimited_money_what_is_the_first_thing#hg3w5jp you_travel_back_in_time_to_200bc_and_cant_get#g1ux972 you_travel_back_in_time_to_200bc_and_cant_get#g1uxtrf you_travel_back_in_time_to_200bc_and_cant_get#g1uxz1v you_travel_back_in_time_to_200bc_and_cant_get#g1uzclh you_travel_back_in_time_to_200bc_and_cant_get#g1uzp09 you_travel_back_in_time_to_200bc_and_cant_get#g1v1hwf your_favourite_lessknown_python_features#ikppfrv your_favourite_lessknown_python_features#ikpqcov your_favourite_lessknown_python_features#ikpr124 youtube_topic_page_endlessly_scrolls#ienvgqw youtube_topic_page_endlessly_scrolls#ieo3kl3 youtubedlg_suddenly_overnight_does_not_download#i8gomhc ysk_delivery_apps_charge_restaurants_1530_on_top#gfsfe68 ysk_if_you_are_trying_to_copy_text_from_a_phone#huasyeu ysk_that_if_youre_watching_a_youtube_video_with#gs80u6k ytdlp_and_the_new_craftsy#jv1lgx6 ytdlp_automating_download_question_task_scheduler#jqxegki ytdlp_limit_videos_scanned_on_channel#i85e2xp ytdlp_on_termux#hdgpeii ytdlp_trim_title_with_regex#i5fxfxk \340\270\202\340\270\255\340\270\247\340\270\262\340\270\243\340\270\233\340\270\204\340\270\231\340\270\231\340\270\253\340\270\231\340\270\255\340\270\242\340\270\204\340\270\243\340\270\232_source_please#iee4tad

---
## [odoochain/Open-Assistant](https://github.com/odoochain/Open-Assistant)@[b9c60ed582...](https://github.com/odoochain/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Sunday 2023-08-20 21:26:02 by Tobias Pitters

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
## [IllusiveMan196/wrye-bash](https://github.com/IllusiveMan196/wrye-bash)@[e86e939461...](https://github.com/IllusiveMan196/wrye-bash/commit/e86e9394613357d0b5d94c4f4ebeea21c85516af)
#### Sunday 2023-08-20 22:10:26 by Infernio

Rework temporary file handling

View with whitespace diff off for an easier time (--ignore-all-space).

This turned out to be a lot more work than I thought. Really should have
been a branch, but I misjudged this horribly, then it kept growing...
Also not sure how feasible this would be to have as a branch without
breaking dev.

Wrye Bash's temporary files handling was actually a complete mess. There
were *three* different ways that random pieces of code were using it:
 - bass.getTempDir/newTempDir/rmTempDir
 - Path.temp and Path.untemp
 - Just use Path.baseTempDir/tempDir or even tempfile directly and do
   it completely manually.

These all had problems:
 - The bass APIs were very implicit - you would extract something to the
   'bass temp dir' and then access it via getTempDir in some other
   function, then remove the directory via rmTempDir in another
   function. XXX I'm still not done tracking this implicit mess down
   (see converters.py).
 - Path.temp did not guarantee that the file would be unique. This isn't
   really a problem for Wrye Bash right now, but would become a big
   problem if we ever wanted to allow multiple instances to run at the
   same time (which we do). Path.untemp also did some really weird I/O
   stuff that doesn't seem necessary at all and would just cost us a
   bunch of syscalls.
 - Path.baseTempDir/tempDir and tempfile required you to keep track of
   all the path manipulation and logic manually. After going through all
   this refactoring, trust me when I say that you do *not* want to do
   this manually. These places were few, thankfully, and none seem to
   have messed it up.

The new API (wbtemp.py) exposes two ways to do it:
 - Use TempDir or TempFile in a context manager. This is extremely
   simple and works very well. It guarantees that the file will be
   cleaned up, even if your logic becomes very complex or an exception
   occurs.
 - Use new_temp_dir/new_temp_file to create a temporary dir/file and
   manually clean it up via cleanup_temp_dir/cleanup_temp_file. These
   should be used *very sparingly*, only where absolutely needed.
   Right now we only have a single usage of manual temp files in
   dialogs.UpdateNotification and two usages of manual temp dirs (one in
   InstallerArchive.unpackToTemp and one in env.shellMakeDirs).

It also has other advantages:
 - Complexity is encapsulated to a single file.
 - Works even during (very) early boot (though doesn't seem to be
   needed right now?).
 - Should work perfectly with multiple instances of WB running at the
   same time (which isn't possible yet, but is a goal for the future).

There's one ugly wart. barb wants to extract archives to a temporary
folder, which then needs to survive a restart of WB, whereupon it will
be handled by the boot '--restore' handler. wbtemp, by design, does not
allow this and will clean up all created directories and files on exit.
To handle this, I used manual tempfile fiddling. Perhaps a future
refactoring of barb could fix this, but for now I think it's an
acceptable tradeoff for the massive improvements this commit brings us.

Some random stuff that got stuck in here:

Note that I got rid of the utf-8-sig encodings passed to 7z, the docs
say:

  Notes: The list file in Unicode charset can start with the BOM (byte
  order mark) character (U+FEFF). In that case 7-Zip checks that
  encoding of BOM corresponds to encoding specified with this switch
  (for UTF-16LE and UTF-16BE).

and:

  Default charset is UTF-8.

From https://7-zip.opensource.jp/chm/cmdline/switches/charset.htm
Very happy to see some of these terrible BOMs disappear from the
codebase.

Mopy/bash/basher/gui_fomod.py:
Some minor warning fixups in gui_fomod

Utumno:
Refactor compress7z:

The time is ripe for dropping the rel_dest param - note this drops a
couple of FName imports.

Closes #665

Co-authored-by: lojack5 <1458329+lojack5@users.noreply.github.com>
Co-authored-by: MrD <the.ubik@gmail.com>

---
## [kast-spells/summon](https://github.com/kast-spells/summon)@[bb57220611...](https://github.com/kast-spells/summon/commit/bb57220611413a0daf83b905c0bfd23081e7fb8e)
#### Sunday 2023-08-20 22:20:41 by Namen Malkav

"All of Chuck Norris' chinese ex-girlfriends say \"chuck can fuck\" but it didnt work out because \"chuck ig-nore-us\""

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[977ca0a6d9...](https://github.com/i3roly/glibc_ddwrt/commit/977ca0a6d9bcab781f7177282e4aed64dc6e64e3)
#### Sunday 2023-08-20 22:41:31 by gagan sidhu

[4.14.323/v53391] update glibc(2.38) and kernel(4.14.323)

- i updated glibc because these guys decided to add strlcpy and strlcat.
  so then i made the choice to recompile anything that used these
  functions (from libbsd). so a lot of stuff that was linked to libbsd
  is now linked without it (except frr because i forgot)

-  kernel 6.1 seems like a no go. it's too big. i could remove tcpdump
   but the problem is it's still going to be a tight fit, and i'd have
   to probably remove other things. i don't know. plus i've lost the
   appetite to update the kernel after linux kernel devs decided they're
   bigger than gLIBC with their 64 bit time crap.
        -now if you build glibc for kernels 5.0 and newer, there will
        probably be userspace breakage for any programs compiled on
        earlier versions, which defeats the entire principle of glibc.

        -so since the linux development team thinks they're bigger than
        the library that makes them, i don't think i should invest any
        more time in trying to stay up to date.

i've had a top build for over 4 years as of this september,
        - with all the buttons working, and the LEDs.
        - if that support fizzles out in the next year or two, i don't
        think it'll be a bad thing.
                -in fact, i thought this update may be pointless, since
                the previous build seems great.
                        -BUT since some of you guys just love to update
                        your stuff, i decided to spin the build anyways.

i was busy taking over the "redneck swap" so that's why i also haven't
updated. anyways i'm getting bored because i've done too many things and
mitt STILL think he's "the math guy" with "the business sense". i
haven't seen mitt do a fraction of what i have. all i've seen mitt do is
hold a picket sign SUPPORTING the vietnam war

https://www.nytimes.com/2012/09/12/us/politics/at-stanford-romney-stood-ground-on-vietnam.html

and his followers think he's the "Mormon John Lennon"

cool world--sorry, i mean GLOBAL ECKANAMY, bro.

P.S. I DID NOT TEST THIS BUILD BUT I DON'T SEE WHY IT WOULDN'T WORK. i
am at 41 days uptime and i'm trying to keep ti going.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[5f3de3897b...](https://github.com/Buildstarted/linksfordevs/commit/5f3de3897b09dbc61ef47d500b45942c0abe3280)
#### Sunday 2023-08-20 23:08:28 by Ben Dornis

Updating: 8/20/2023 11:00:00 PM

 1. Added: Sponsor based GitHub feature toggling · community · Discussion #46980
    (https://github.com/orgs/community/discussions/46980)
 2. Added: Two quick hacks for laptop in-flight Delta Wi-Fi with T-Mobile
    (https://blog.yossarian.net/2023/08/20/Two-quick-hacks-for-inflight-delta-wifi-with-tmobile)
 3. Added: I have no clue how to interview for data scientists
    (https://andrewpwheeler.com/2022/03/24/i-have-no-clue-how-to-interview-for-data-scientists/)
 4. Added: Quick DBUS Fix
    (https://vermaden.wordpress.com/2023/08/19/quick-dbus-fix/)
 5. Added: How Surround Sound for Headphones Works
    (https://hajo.me/blog/2014/12/28/how-surround-sound-for-headphones-works/)
 6. Added: Ruby's Hash is a Swiss-Army Knife
    (https://www.akshaykhot.com/ruby-hash-is-a-swiss-army-knife/)
 7. Added: A 40 lines app needs 40 files
    (https://thomassimon.dev/ps/2)
 8. Added: I Like You But You’re Not Yet My Friend. What Do We Call Each Other? A Struggle to Replace “Acquaintance” With Something Better.
    (https://hunterwalk.com/2023/08/19/i-like-you-but-youre-not-yet-my-friend-what-do-we-call-each-other-a-struggle-to-replace-acquaintance-with-something-better/)
 9. Added: My Favourite Development Books
    (https://ijrussell.github.io/posts/top-10-books/)
10. Added: Calm tech - Nicolas Bouliane
    (https://nicolasbouliane.com/blog/calm-tech)
11. Added: SponsorLink: feedback and moving forward
    (https://www.cazzulino.com/sponsorlink-feedback.html)
12. Added: How I turned Local Storage into a Web Socket
    (https://alemtuzlak.hashnode.dev/how-i-turned-local-storage-into-a-web-socket)
13. Added: Breaking The Mutant Language's "Encryption"
    (https://eval.blog/breaking-the-mutant-languages-encryption)
14. Added: Bleeding Edge Technology is Made for Silly Art
    (https://www.bramadams.dev/202308192019/)

Generation took: 00:08:16.0963580

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[9ccd6ecd74...](https://github.com/microsoft/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Sunday 2023-08-20 23:18:14 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---

