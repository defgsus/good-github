## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-28](docs/good-messages/2023/2023-11-28.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 3,987,643 were push events containing 5,277,567 commit messages that amount to 313,564,596 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 83 messages:


## [KiulWasTaken/SMP-Utilities-v2](https://github.com/KiulWasTaken/SMP-Utilities-v2)@[1f4f67c6e9...](https://github.com/KiulWasTaken/SMP-Utilities-v2/commit/1f4f67c6e9a6e7f622f1bc93a3abd011f6cd3d14)
#### Tuesday 2023-11-28 00:13:13 by KiulWasTaken

fuck you patters
- added your list: C.overflowingPlayers
- made the dragon egg actually indestructible (still dies to void)
- Dragon Egg can now only be picked up after sitting on the ground for 10 minutes after being dropped
- Dragon Egg now broadcasts its location when dropped and when left on the ground for over an hour
- restart-in command visual bug fixed
- C's static methods are now used in place of their duplicates
-

Took 1 hour 29 minutes

---
## [LeeroysHub/RM-Flipper](https://github.com/LeeroysHub/RM-Flipper)@[96132b5959...](https://github.com/LeeroysHub/RM-Flipper/commit/96132b5959851788e990eff325cf0e0f6f53ea7a)
#### Tuesday 2023-11-28 00:16:40 by Leeroy

Rollback Keyloq to 5 months ago! Bloody regressions making my daily life shit!

---
## [MysticalFaceLesS/Shiptest](https://github.com/MysticalFaceLesS/Shiptest)@[70463ae71b...](https://github.com/MysticalFaceLesS/Shiptest/commit/70463ae71b7d639eecea572d3251562c5ffef68b)
#### Tuesday 2023-11-28 00:46:01 by Mirag1993

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
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[5f504d1de7...](https://github.com/pytorch/pytorch/commit/5f504d1de74a5189f93e65aa9283fc4607b8631c)
#### Tuesday 2023-11-28 01:13:59 by Pedro Caldeira

Check for boolean values as argument on pow function.  (#114133)

Hello everyone! 😄
Also @lezcano , nice to meet you! :)

Sorry if I miss anything, this is my first time around here. 🙃

This PR basically makes the same behaviour for cuda when using `torch.pow`. Basically Python considers True as 1 and False as 0. I just added this check into `pow` function. From what I understood, when I do `.equal` for `Scalar` that is boolean, I'm sure that types match so that won't cause more trouble.

I know that the issue suggest to disable this case but that could be a little more complicated, in my humble opinion. And that can create some compability problems too, I guess.

My argument is that code below is correct for native language, so I guess it does makes sense sending booleans as Scalar.

```
$ x = True
$ x + x
2
```

This was my first test:
```
Python 3.12.0 | packaged by Anaconda, Inc. | (main, Oct  2 2023, 17:29:18) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.pow(torch.tensor([1, 2], device='cuda'), True)
tensor([1, 2], device='cuda:0')
>>> torch.pow(torch.tensor([1, 2]), True)
tensor([1, 2])
>>> torch.pow(torch.tensor([1, 2]), False)
tensor([1, 1])
>>> torch.pow(torch.tensor([1, 2], device='cuda'), False)
tensor([1, 1], device='cuda:0')
```

I've run `test_torch.py` and got following results, so my guess is that I didn't break anything. I was just looking for a test that uses linear regression, as suggested.

```
Ran 1619 tests in 52.363s

OK (skipped=111)
[TORCH_VITAL] Dataloader.enabled		 True
[TORCH_VITAL] Dataloader.basic_unit_test		 TEST_VALUE_STRING
[TORCH_VITAL] CUDA.used		 true

```
(I can paste whole log, if necessary)

If this is a bad idea overall, dont worry about it. It's not a big deal, it's actually a two line change 😅  so can we talk of how do things in a different strategy.

For the record I've signed the agreement already. And I didn't run linter because it's not working 😞 . Looks like PyYaml 6.0 is broken and there's a 6.0.1 fix already but I have no idea how to update that 😅

Fixes #113198

Pull Request resolved: https://github.com/pytorch/pytorch/pull/114133
Approved by: https://github.com/lezcano

---
## [Yungryota/PSA](https://github.com/Yungryota/PSA)@[f0f8244688...](https://github.com/Yungryota/PSA/commit/f0f8244688b45c94907dbd7ffa4a802260ac5ed4)
#### Tuesday 2023-11-28 01:24:23 by Javiera

muestra primera temperatura en angular

From sprinkler splashes to fireplace ashes
I gave my blood, sweat, and tears for this
I hosted parties and starved my body
Like I'd be saved by a perfect kiss
The jokes weren't funny, I took the money
My friends from home don't know what to say
I looked around in a blood-soaked gown
And I saw something they can't take away
'Cause there were pages turned with the bridges burned
Everything you lose is a step you take
So make the friendship bracelets
Take the moment and taste it
You've got no reason to be afraid

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[9229adc934...](https://github.com/timothymtorres/tgstation/commit/9229adc934b9575a8528b6efc0074fcc2921cc33)
#### Tuesday 2023-11-28 01:31:51 by DaydreamIQ

Touches up Moffuchi's pizzeria  (#79899)

## About The Pull Request
I've given the icebox pizzeria ruin a few small improvements:
- Firstly, The kitchen is actually stocked with tomatoes from the get
go. Along with a few mothic themed ingredients for those signature
mothic pizzas we all know and love (And hate for being such a pain to
make)
- The discarded air alarm frames have been replaced with working ones
(I'm unsure if this was intentional or not)
- Some drinking glasses have been added to the bar
- And finally a pacman has been placed in the backroom along with some
plasma to power the place
## Why It's Good For The Game
This place gets overlooked a lot because its completely powerless, and
doesn't actually give you enough from the get go to make even a basic
pizza besides the tomato seeds a lot of people are gonna miss. This
gives the ruin just a little more life to maybe be worth trekking out
for. And having mothic themed ingredients in the **MOFFIC** Pizzeria
just makes sense even if they are a bitch to make.

Not sure if this counts as a balance change or a QOL so feel free to
yell at me if I've labelled this wrong, I have been advised that this
SHOULD be the latter at least.
## Changelog
:cl:
qol: Mothuchi's pizzeria has been improved slightly! Order yourself a
fresh mothic pizza today!
/:cl:

---
## [ashutoshchettri/android_kernel_xiaomi_alioth](https://github.com/ashutoshchettri/android_kernel_xiaomi_alioth)@[239fbdd83d...](https://github.com/ashutoshchettri/android_kernel_xiaomi_alioth/commit/239fbdd83d208e0a97029272bbbcd5207236fc7a)
#### Tuesday 2023-11-28 01:44:55 by Angelo G. Del Regno

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
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[b5e095e380...](https://github.com/Bubberstation/Bubberstation/commit/b5e095e380e729793628d254bb441f51ecdb046b)
#### Tuesday 2023-11-28 02:31:32 by Waterpig

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
## [PANKAJ11111111/Croma_e-commerce_website](https://github.com/PANKAJ11111111/Croma_e-commerce_website)@[0cce7579e2...](https://github.com/PANKAJ11111111/Croma_e-commerce_website/commit/0cce7579e269f401ad6333fc549a638bf8f8fc3e)
#### Tuesday 2023-11-28 02:33:14 by Pankaj Saratkar

own

🚀 Exciting News! 🛒 Just wrapped up an incredible project with the iconic Croma Tata Group, bringing their e-commerce website to life! 🌐💼

🌟 Our team poured creativity, dedication, and expertise into crafting a seamless online shopping experience using cutting-edge HTML and CSS technologies. 🖥️✨

🔍 Explore the revamped Croma Tata website and discover:
✅ Intuitive navigation
✅ Sleek and modern design
✅ Responsive layouts for a flawless mobile experience

🛍️ Dive into a world of tech and innovation at your fingertips! 💻🔧

Huge shoutout to the amazing team behind this achievement! 🙌🏽 Your hard work and commitment made this project a true success.

#CromaTata #EcommerceWebsite #WebDevelopment #HTML #CSS #DigitalTransformation #TechInnovation #TeamWork #ProjectCompletion 🚀🌐

---
## [Zonespace27/cmss13](https://github.com/Zonespace27/cmss13)@[2011c229f9...](https://github.com/Zonespace27/cmss13/commit/2011c229f9a37de8fa67a74d8e40974515724cde)
#### Tuesday 2023-11-28 02:46:23 by stalkerino

Readds skull facemask and facepaint (#5042)

# About the pull request
It readds two items that were removed in the past for no valid reason
(in my opinion), since it was a targeted PR against a specific player I
do not think it should've been removed.

# Explain why it's good for the game

It looks nice and fits the atmosphere, adding it will help players
customize their characters without being too loud.
The removal reason of "You'd get laughed at for wearing it IRL" is
invalid, a lot of military and law enforcement people wear skull masks,
punisher emblems and etcetra - this is especially evident in America
(We're UA)

https://discord.com/channels/150315577943130112/746325423289401395/1168350579307860078

https://discord.com/channels/150315577943130112/827156857566265375/1145494273568022588
https://files.catbox.moe/4o3ag1.png

https://discord.com/channels/150315577943130112/604397850675380234/1094357565317586964
-- the person who made it admitting it was targeted.


# Testing Photographs and Procedure
I don't think it needs testing
</details>


# Changelog
:cl: stalkerino
add: readds skull facepaint and skull balaclava (blue and black)
/:cl:

---
## [Zonespace27/cmss13](https://github.com/Zonespace27/cmss13)@[f367771f57...](https://github.com/Zonespace27/cmss13/commit/f367771f5799b87257d92cb79db71bcd85b62f75)
#### Tuesday 2023-11-28 02:46:23 by Birdtalon

Eggsac carrier revival (#4716)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

[Forum Thread](https://forum.cm-ss13.com/t/eggsac-carrier-revival/4711)

# About the pull request

The concept of this PR is to find a middle ground between the current
eggsac carrier and the pre #4459 eggsac carrier.

This PR will make the following changes. (From this point "normal weeds"
can be substituted for "off hive weeds" Placing eggs on hive weeds is
**unchanged**.)

- Eggsac carrier can once again place eggs on normal weeds.
- Eggsac carrier can only place 4 eggs at once on normal weeds.
- If the Eggsac places more than 4 eggs on normal weeds, their oldest
placed egg will die. No hugger release.
- Eggs placed on normal weeds have a maximum lifetime of 5 MINUTES after
which they will die. No hugger release.
- Eggs placed on normal weeds have a 1 MINUTE life whilst the carrier is
further than 14 tiles away from them.
- If the carrier dies, all of their sustained eggs die.

# Explain why it's good for the game

Eggsac carrier at the moment is in a bit of a poor place and has gone
from being very strong to quite poor. Considering the limitation of
having to place only on hive weeds.
The majority of feedback I read against eggsac carrier was with the
quantity of eggs able to be placed, as well as the locations they can be
placed in, all across the map and with impunity.

This PR aims to address those concerns to make the eggsac both less
infuriating to play against while still being satisfying to play as a
frontline support or as a stealthy trapper.

Eggs can no longer be placed all over the map because of the 4 egg limit
off weeds, so the carrier has to think where they want to impact the
map. The carrier also has to stay within a reasonable distance to where
they are impacting with their eggs which localises their impact to their
immediate play area. The carrier also has to be more reactive to current
events as they cannot place an egg which then becomes useful 30 minutes
later.

Killing the carrier also has a small reward as in addition to removing a
xeno from the game, the eggs they are sustaining are cleared. If a
carrier is supporting the front and dies, the marines don't then have to
clear X number of eggs AFTER the kill.

# Testing Photographs and Procedure

1. Spawn as egg carrier.
2. Plant egg on normal weeds.
3. Move 15+ tiles away.
4. Wait 1 minute
5. OR Wait 5 minutes within 14 tiles.
6. Kill the carrier.

The 5 minute lifetime of the eggs will also clear the eggs in the case
that the carrier is admin deleted, or some other weird stuff happens
which doesn't result in a death. This will also catch carriers
de-evolving

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
label your changes in the changelog. Please note that maintainers freely
reserve the right to remove and add tags should they deem it
appropriate. You can attempt to finagle the system all you want, but
it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Maintainers freely reserve the right to remove and add
tags should they deem it appropriate. -->

:cl:
add: Eggsac carrier can now place eggs on normal weeds to a maximum of 4
eggs.
add: Eggsac carrier eggs on normal weeds have an expiry date.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Zonespace27/cmss13](https://github.com/Zonespace27/cmss13)@[a955791561...](https://github.com/Zonespace27/cmss13/commit/a955791561d5aeab0ff0640923fe1192ad377830)
#### Tuesday 2023-11-28 02:46:23 by fira

/tg/ Status effects part 1 - fluid status updates (#4828)

![image](https://github.com/cmss13-devs/cmss13/assets/604624/38cdd1a0-e13c-4d69-b893-49cea2a8113f)
CM Dev figured it out 9 years ago and nobody listened and kept tacking
illogical conditions

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

Builds on previous "prelude" PRs in the following steps:
 * Ports /tg/ body_position and mobility_flags
* Fixes some interaction requirements to use stun/mobility rather than
lying/knocked_down
* Ports /tg/ granular status updates, ie. status propagating through
handlers and signals. This includes changes to resting, buckling, and
lying down human transforms.
 * Wires our status effect system to it directly
* Removes `update_canmove` from existence completely as not needed
anymore

Because step 1 and 2 require updating all the gameplay logic using them,
this PR modifies a lot of files.

Part 2 will move the actual status effects to /tg/ status_effects,
resolving our timing problems.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Testing Checklist!</summary>

- [x] Basic Movement
- [x] Admin Freeze Prevents Movement
- [x] Resting, Getting Up
- [x] Xenos change icon when resting
- [x] Buckling, including bed rotation and propelled chairs
- [x] Crawling Movement including sprite movement
- [x] Aggressive, Choke Grabbing, and Fireman carry apply rotation
- [x] Xeno Pounce and Abduct properly freeze both target and caster 
- [x] Double dropship seats density update
- [x] Explosive knockout on Humans
- [x] Xeno burrow density and movement interactions
- [x] Xeno nest interactions, specifically confirm density changes work
- [ ] Xeno nest bullet hits doublecheck with snowflake trait check
- [x] Combat Xeno ~~knockouts~~ knockdown and sprite updates
- [x] ~~Sleeping, Waking up, Usage of items while sleeping~~ - Can't
really test this we have almost no sleep code
- [x] Arbitrary buckling rotations
- [x] Admin-set transforms work with buckling/lying
- [ ] All the broken objects that will only be found out in Testmerge

</details>


# Changelog

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
label your changes in the changelog. Please note that maintainers freely
reserve the right to remove and add tags should they deem it
appropriate. You can attempt to finagle the system all you want, but
it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Maintainers freely reserve the right to remove and add
tags should they deem it appropriate. -->

:cl:
code: Ported basic /tg/ Status Backend.
add: Human transform changes such as lying down, knock down, buckling,
are now animated.
fix: Some statuses will now take effect immediately instead of waiting
for a life tick, notably Resting.
balance: Many interaction requirements were changed to eg. fail upon
stuns rather than if lying down.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [lonnywong/terminal](https://github.com/lonnywong/terminal)@[86fb9b4478...](https://github.com/lonnywong/terminal/commit/86fb9b44787accd09c5943a506e27eb4c8e573c0)
#### Tuesday 2023-11-28 02:53:06 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

---
## [sjp38/linux](https://github.com/sjp38/linux)@[d90cf8fa7d...](https://github.com/sjp38/linux/commit/d90cf8fa7d0d9906c7ffa793ce69782c440e91e7)
#### Tuesday 2023-11-28 02:59:41 by SeongJae Park

==== DAMOS: Introduce Aim-Oriented Feedback-driven Quota Auto Tuning ====

Subject: [PATCH] mm/damon: Let users feed and tame DAMOS

Introduce a new way for tuning DAMOS, namely aim-oriented
feedback-driven aggressiveness auto tuning.  It allows users repeatedly
tell DAMOS how far it is from the users' aiming goal.  Based on the
feedback, DAMOS self-adjusts its aggressiveness so that the goal can be
achieved.

DAMOS Control Difficulty
========================

DAMOS helps users easily implementing effective access pattern aware
system operations.  However, controlling DAMOS in wild is not that easy.

The basic way for DAMOS control is specifying the target access pattern.
In this approach, the user is assumed to know the access pattern of the
system and the workloads well.  Though some good tools including DAMON
can help that, it requires time and resource.  The cost depends on the
complexity and the dynamicity of the system and workloads.  After all,
the access pattern consists of three ranges, namely access rate, age,
and size of the regions.  It means the user needs to tune six
parameters.  Tuning six parameters is by itself not simple.  It is not
an approach that doable for everyone.

To let users avoid at least the worst case, DAMOS allows users to set
the upper-limit of the schemes's aggressiveness, namely DAMOS quota.
DAMOS further provides its best-effort under the limit by prioritizing
regions based on the access pattern of the regions.  For example, users
can ask DAMOS to page out up to 100 MiB of memory regions per second.
Then DAMOS pages out regions that not accessed longer time (colder)
first under the limit.  This allows users to set access pattern bit
naively, and focus on only the one parameter, the quota.  In other
words, the number of parameters to tune with special care can be reduced
from six to one.

Still, however, the optimum value for the quota depends on the system
and the workloads' characteristics, so not that simple.  The number of
parameters to tune can also increase again if the user needs to run
multiple schemes, e.g., collapsing hot pages into THP while splitting
cold pages into regular pages.

In short, the existing approaches ask users to be perfect, or deligent
micromanager of DAMOS.  That's not what sustainable in long term.

Aim-oriented Feedback-driven DAMOS Quota Auto Tuning
====================================================

Most users would start using DAMOS since there is something they want to
achieve using DAMOS.  The users may have well understanding of such
goals.  Having specific metrics and values like SLO is indeed common.
Hence, users could repeatedly inform DAMOS the goals, and how well DAMOS
is making it with only relatively small effort.  Then DAMOS could
somehow make it.  In other words, users provide feedback for each DAMOS
scheme.  DAMOS then tune the quota of each scheme based on the users'
feedback and the current quota values.

This patchset implements the idea.

Implementation
--------------

The core logic implementation is in the first patch.  In short, it uses
below simple feedback loop algorithm to get next aggressiveness from the
current aggressiveness and the feedback (target_score and current_score)
for the current aggressiveness.

    f(n) = max(1, f(n - 1) * ((target_score - current_score) / target_score + 1))

Note that this algorithm assumes the aggressiveness and the score are
positively proportional.  Making it true is the feedback provider's
responsibility.

Test Results
------------

To show if this provides the expected benefit, we prepare four different
system setup on AWS i3.metal instance.  The first setup (original) runs
the workload without any DAMOS scheme.  The second setup (not-tuned)
runs the workload with virtual address space-based proactive reclamation
scheme that pages out memory regions that not accessed for five seconds
or more.  The third setup (offline-tuned) runs the same proactive
reclamation DAMOS scheme, but after making it tuned for each workload in
offline, using our previous user-space driven automatic tuning approach,
namely DAMOOS[1].  The fourth and final setup (online-tuned) runs the
same scheme, but making DAMOS to do online auto-tuning, aiming 0.5% of
'some' memory pressure stall time per 10 seconds.

For each setup, we run realistic workloads from PARSEC3 and SPLASH-2X
benchmark suites.  For each run, we measure RSS and runtime of the
workload, and 'some' memory pressure stall time (PSI) of the system.
We repeat the runs five times and use averaged measrements.

For each comparison of the schemes, we normalize the measurements to
those of 'original'.  In case of the PSI, that for 'original' was zero,
so we normalize the value to that of 'not-tuned' scheme's result.  The
normalized results are shown below.

            Not-tuned         Offline-tuned     Online-tuned
    RSS     0.622688178226118 0.787950678944904 0.740093483278979
    runtime 1.11767826657912  1.0564674983585   1.0910833880499
    PSI     1                 0.727521443794069 0.308498846350299

The 'not-tuned' scheme acheives about 38.7% memory saving but incur about
11.7% runtime slowdown.  The offline-tuned scheme achieves about 22.2%
memory saving with about 5.5% runtiem slowdown.  It also achieves about
28.2% PSI saving.  The online-tuned scheme achieves about 26% memory
saving with about 9.1% runtime slowdown.  It also achieves about 69.1%
PSI saving.  We continued this test multiple times, and consistently got
similar results.

So, the online-tuned version is slightly more aggressive than the
offline-tuned version, but slightly less aggresive than the not-tuned
version.  The difference in memory saving and performance degradation
reflects the aggressiveness difference, but the difference is not
significant.  However, it shows significant PSI saving, which was the
goal of the tuning, amonth the three variants.  Hence, we conclude the
automatic tuning is working as expected.

The test code is available[2], so you can reproduce on your system.

[1] https://www.amazon.science/publications/daos-data-access-aware-operating-system
[2] https://github.com/damonitor/damon-tests/commit/3f884e61193f0166b8724554b6d06b0c449a712d

Patches Sequence
================

The first four patches implement the core logic and user interfaces for
the auto tuning.  The first patch implements the core logic for the auto
tuning, and the API for DAMOS users in the kernel space.  The second
patch implements basic file operations of DAMON sysfs directories and
files that will be used for setting the goals and providing the
feedback.  The third patch connects the quota goals files inputs to the
DAMOS core logic.  Finally the fourth patch implements a dedicated DAMOS
sysfs command for efficiently committing the quota goals feedback.

Two patches for simple test of the logic and interfaces follow.  The
fifth patch implements the core logic unit test.  The sixth patch
implements a selftest for the DAMON Sysfs interface for the goals.

Finally, two patches for documentation follows.  The seventh patch
documents the design of the feature.  The final eighth patch updates the
usage document for the features.

Signed-off-by: SeongJae Park <sj@kernel.org>

---
## [jjpark-kb/Skyrat-tg](https://github.com/jjpark-kb/Skyrat-tg)@[67ddf1507c...](https://github.com/jjpark-kb/Skyrat-tg/commit/67ddf1507c8663c4b8f006ed8c763ca372e5fc29)
#### Tuesday 2023-11-28 03:10:46 by SkyratBot

[MIRROR] Make sign language unaffected by the Social Anxiety quirk's direct speech effects [MDB IGNORE] (#25140)

* Make sign language unaffected by the Social Anxiety quirk's direct speech effects (#79809)

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

* Make sign language unaffected by the Social Anxiety quirk's direct speech effects

---------

Co-authored-by: _0Steven <42909981+00-Steven@users.noreply.github.com>

---
## [jjpark-kb/Skyrat-tg](https://github.com/jjpark-kb/Skyrat-tg)@[fcbbb6e0e0...](https://github.com/jjpark-kb/Skyrat-tg/commit/fcbbb6e0e0f9c0132fbc962bb03464bdcd1b20c4)
#### Tuesday 2023-11-28 03:10:46 by SkyratBot

[MIRROR] Fixes body collision causing a stun, despite a successful block. [MDB IGNORE] (#25146)

* Fixes body collision causing a stun, despite a successful block. (#79824)

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

* Fixes body collision causing a stun, despite a successful block.

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [FrankitoBoar/Boar](https://github.com/FrankitoBoar/Boar)@[94603a2a96...](https://github.com/FrankitoBoar/Boar/commit/94603a2a9636ab5a9e8ded9247b490a5d6670da4)
#### Tuesday 2023-11-28 03:16:05 by SkyratBot

[MIRROR] Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) [MDB IGNORE] (#25102)

* Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) (#79803)

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

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP)

---------

Co-authored-by: KingkumaArt <69398298+KingkumaArt@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[371c129fa3...](https://github.com/MCBCMF/MCBCMassacre/commit/371c129fa388189185f0f17a8853bf6cb9d29cfc)
#### Tuesday 2023-11-28 03:25:55 by Kelvin Williams

GATech Warning!!! Direct from the Creator.

# Georgia Tech Warning
The CIA is trying to tie up lose ends, meaning killing anyone that may
know things or the true GATech Alumni (2013) Kelvin Eugene Williams.

## Cloaking
The CIA utilizes a cloaking technology that will render a person
practically invisible to the naked eye. It’s stolen from the military.

You should be able to find some documentation on it by searching. I
found a [this
article](https://www.nature.com/articles/s41598-017-08505-w) on photon
entanglement and cloaking that told me a lot.

It’s an electromagnetic field, I know there’s equipment on campus that
can and does detect it. Remember this is a revenge of the nerds and
you are your brother’s and sister’s keeper.

They CAN and DO use a companion technology that enables them to pass
through walls and doors.

The Creator says they are on campus tonight. (To the nerd reading
this: START RINGING THE FIREBELL! Let everyone on campus know, I bet
you have a way.)

Everyone on campus needs should not sleep alone. Pair up with another
student. Four hours of sleep is all you need. While one is sleeping,
the other is up watching and listening.

(Saving. Reload in a couple minutes for more.)

---
## [ss220-space/Skyrat-tg](https://github.com/ss220-space/Skyrat-tg)@[800ad77ed2...](https://github.com/ss220-space/Skyrat-tg/commit/800ad77ed29fd7c68ddc0cac3112f45e1e1c3015)
#### Tuesday 2023-11-28 03:30:30 by DBGit42

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
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[daa0efa5ae...](https://github.com/MCBCMF/MCBCMassacre/commit/daa0efa5ae0b9fed2422d3e8da2b5249ecad4973)
#### Tuesday 2023-11-28 03:57:53 by Kelvin Williams

annie's gonna hit again

I just realized that the other day someone told Maine to let it all
out, we had an escort here last night, measurements all around I fell
short that means she's winning over God and that means Annie is going
to strike into the church this weekend.

---
## [Dharmveer-123/UniqPathLab](https://github.com/Dharmveer-123/UniqPathLab)@[0367b9d86f...](https://github.com/Dharmveer-123/UniqPathLab/commit/0367b9d86f8befd13ce15fa46356641ce88a379e)
#### Tuesday 2023-11-28 03:58:17 by Dharmveer-123

Update README.md

In the bustling heart of Delhi, UniQ Pathlab stands tall as a beacon of health and well-being, offering unparalleled services in comprehensive full-body checkups. With a commitment to excellence and a focus on preventive healthcare, UniQ Pathlab is your trusted partner on the journey to optimal health.

Why Choose UniQ Pathlab for Your Full Body Checkup?

1. Cutting-Edge Diagnostic Technology:
At UniQ Pathlab, we believe in the power of precision. Our state-of-the-art diagnostic technology ensures accurate and reliable results, providing you with a detailed picture of your health.

*2. Experienced Healthcare Professionals:
Our team of skilled and experienced healthcare professionals is dedicated to ensuring a seamless and comfortable full-body checkup experience. From sample collection to result delivery, trust us to prioritize your well-being.

*3. Customized Health Packages:
Recognizing that health needs vary, UniQ Pathlab offers a range of customizable health packages. Whether you're seeking a routine checkup or a more specialized assessment, our packages cater to individuals of all ages and health profiles.

*4. Quick Turnaround Time:
We understand the value of time in healthcare. UniQ Pathlab is committed to delivering prompt results, allowing you to take timely actions towards maintaining or improving your health.

*5. Comprehensive Health Insights:
A UniQ Pathlab full body checkup goes beyond numbers; it provides insights into your overall health. Our comprehensive reports help you understand your body better, empowering you to make informed decisions for a healthier future.

Our Full Body Checkup Services Include:

Blood Tests and Hematology Profiles
Liver and Kidney Function Tests
Cardiac Health Assessment
Thyroid Function Tests
Diabetes Screening
Vitamin and Mineral Analysis
Lipid Profile
Complete Urinalysis
Body Mass Index (BMI) Measurement
Experience the UniQ Advantage:

Choosing UniQ Pathlab for your full body checkup means choosing excellence in healthcare. With a commitment to accuracy, efficiency, and patient-centric care, we strive to make your health journey a positive and proactive one.

---
## [sjrsjz/M-Lang](https://github.com/sjrsjz/M-Lang)@[39725d238a...](https://github.com/sjrsjz/M-Lang/commit/39725d238a170592e4498bd2f1e2dd0decda242a)
#### Tuesday 2023-11-28 04:04:28 by sjrsjz

Fuck you DEBUGMerge branch 'master' of https://github.com/sjrsjz/M-Lang

---
## [Perkedel/CVR_Stuffings](https://github.com/Perkedel/CVR_Stuffings)@[8187f55f2b...](https://github.com/Perkedel/CVR_Stuffings/commit/8187f55f2b97e35bd4044e75a1851568d66598fd)
#### Tuesday 2023-11-28 04:30:53 by JOELwindows7

you fucking pls stop messing up my entire

project okay?!

Nobody ask you to fucking install those kinds of dependency, bitch! I DO THAT, AS I SAY!!

You hear me? How were you here?! Oh that's right. Most game devs do uses that, made yourself oblivious.

---
## [eedwards4/disk_scheduler](https://github.com/eedwards4/disk_scheduler)@[622b21fcff...](https://github.com/eedwards4/disk_scheduler/commit/622b21fcffb4de0e0c7758c09d9213973c90c455)
#### Tuesday 2023-11-28 04:54:33 by Ethan Edwards

Working on implementations for STQueue and LookQueue
Kill me please this sucks so much why do we have to do this tedious ass shit

---
## [MidoriWroth/tgstation](https://github.com/MidoriWroth/tgstation)@[30bac3a301...](https://github.com/MidoriWroth/tgstation/commit/30bac3a3010ea5249e1116de9e342b1fe40c19c9)
#### Tuesday 2023-11-28 04:55:28 by san7890

Adds Custom Announcement Dividers (#79071)

This ports a whole bunch of various PRs and commits from
https://github.com/effigy-se/effigy-se , with heavy refactoring to keep
it fresh for /tg/'s code standards.

## About The Pull Request

The whole slew of announcement touchups lately (as in #78995
(37db1ecbf8d7ceeaeb134c56b403339555f44cea) / #79052
(12308dbd3dae702a1c7b9f7f80d7859aea085c82)) have made me realize how
much this stuff sucks. The author of these new spans was advertising
these in coding general, so I sat down and coded it. Look at the spans,
they're much nicer than what we had going on:

(ignore the capitalized alert status names, this was removed)

<details>
<summary>Dark Mode</summary>


![image](https://github.com/tgstation/tgstation/assets/34697715/107b8efb-b7a1-41ff-9d16-358c4dc3738d)

![image](https://github.com/tgstation/tgstation/assets/34697715/9e730dfe-7ba3-4edd-96bb-0630fe5e85cf)
</details>

<details>
<summary>Light Mode</summary>


![image](https://github.com/tgstation/tgstation/assets/34697715/57f642f9-ee17-4b16-8027-00a9350e9059)

![image](https://github.com/tgstation/tgstation/assets/34697715/b28b7f49-fd4f-420a-9313-e16b9781c07c)
</details>

This PR also features

* Major announcement code handling cleanup and refactor! There was a lot
of copypasta so let's distill it all down into one proc
* Better cacheing! We were doing a shit load of new string generation
needlessly! That's fixed now.
* Better string concatenation! Lists are better for string tree reasons.
It still works just as well, as you can see from the screenshots above.
Best of all, no fucking `<br>` dogshit everywhere!
* We don't use string equivalency in order to figure out the "type" of
an announcement. It's all defines now. This was a bonus that I just
coded in since it irritated me.
* Minor spellcheck of "announcement".
* All of our HTML string mangling stuff is now all span macros! I love
macros.

## Why It's Good For The Game

In the same vein of adding examine blocks (#67937
(b864589522f4f14183270a62dbea3df8028d2eb6)) because old examinations
tended to blend in with the chat and everything chat-wise used to suck
really hard- I think this is a really nice way to draw attention to
announcements in the chat box without needing a shit load of line breaks
that just really look ugly and have no real consistency. You can look at
the PRs/commits I linked above for an idea of just how ugly it could be
getting.

I haven't audited every announcement in this PR, we can tweak this down
the line.

## Changelog

:cl: LT3, san7890
add: Announcements have gotten a fresh coat of paint! They should be
popping with splendid new colors and should have a lot less ugly
linebreaks, while still managing to keep your attention at the screen.
/:cl:

I know we didn't need to port all the CSS themes but I added them
anyways in case admins wanna have some fun.
There can probably be more code improvements, just figured I'd crack it
out while I had time.
The colors also seem fine, let me know if we need more redness or
something. It's okay for stuff to be toned down a bit imo, but that
should be done after a hot second.

---------

Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [MidoriWroth/tgstation](https://github.com/MidoriWroth/tgstation)@[26e3ea1e0d...](https://github.com/MidoriWroth/tgstation/commit/26e3ea1e0d185439d792a6890e9eb041f8aadfdf)
#### Tuesday 2023-11-28 04:55:28 by John Willard

Mafia can be played on your PDA (#78576)

## About The Pull Request

Mafia is now friggin playable from the PDA, I also changed other stuff
too

- You can't use abilities on dead people if you're not supposed to (cant
kill the same person over and over)
- Changelings cant kill other Changelings
- Changelings can now only talk to eachother at night, rather than using
:j
- Everyone starts spawned in the center of the map, since people playing
on PDA can't move their characters. This is so everyone can hear PDA
users in person, as I don't want the chat log to be mandatory.

To do this, all messages you are meant to be able to see, is now logged
for you to see in your Mafia panel. This essentially means that people
playing through the PDA get a downgraded version of it, but I don't know
how much larger I want this UI to be.

Playing Mafia through the PDA will not tell you of other players ahead
of time when signing up (as it shows ckeys + pdas), but they can see the
names in-game. Unfortunately this means we'll have to remove your
customization coming with you, to prevent using it to tell who is dead
in round.

Things I am missing
- Program overlays on PDA/Laptop/Computer
- Icon for the app's header while a game is active

I'm not a spriter and can't make either of these

This is the new UI

![image](https://github.com/tgstation/tgstation/assets/53777086/7cf503d9-b2e2-4127-874a-acad6425d649)

I also fixed alert calls for PDAs and stuff

![image](https://github.com/tgstation/tgstation/assets/53777086/e09b2e5e-b9e7-43ae-9273-c168e9c8e642)

and removed the X at the top on computers since they had no battery

![image](https://github.com/tgstation/tgstation/assets/53777086/d3dd8307-805c-4aba-be5e-4c24a0bdcb91)

Looks a little better now hopefully 👍 

## Why It's Good For The Game

- The current Arcade app sucks, and is a solo game. This is much more
entertaining and you can talk to others in it, which is swag as fuck.
- There's a larger potential playerbase for the Minigame making it more
likely to be played.
- Sets groundwork for a better version of
https://github.com/tgstation/tgstation/pull/75879
- Adds more suspense and teamwork in the minigame.

## Changelog

:cl: JohnFulpWillard, sprites by CoiledLamb
add: You can now play Mafia on your PDA.
balance: Mafia changelings can now only talk to eachother during the
night.
fix: Mafia abilities can't be repeatedly used on people.
/:cl:

---
## [MidoriWroth/tgstation](https://github.com/MidoriWroth/tgstation)@[2f9c21986b...](https://github.com/MidoriWroth/tgstation/commit/2f9c21986b9ebcf1548df34ce12b458935b30052)
#### Tuesday 2023-11-28 04:55:28 by LemonInTheDark

Actually supports alpha passed into emissive stuff (#79117)

## About The Pull Request

Ok so like, the emissive procs have an alpha argument right? The thing
is, the thing is it doesn't fucking do anything.

Alpha is a component of the color var (at least when it's a matrix), so
when we set alpha and then set color to a matrix, the alpha gets
overriden. Inverse is also true.

I want to support alpha args, since I like the idea of dimmable
emissives. Soooooo
Let's take the alpha arg, divide it by 255, and replace everything that
cares about alpha (as an intensity thing) with it.

This lets us do transparent emissives and transparent emissive blockers.

I added some guard checks to hopefully avoid the list init most of the
time (it is in theory comprable since color sets should copy but I don't
trust byond to optimize for that)
Also modified the macros to suppport what I'm doing nicely

## Why It's Good For The Game

We should support this, and now we do

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[790a82a3b1...](https://github.com/vdaular-dev/linksfordevs/commit/790a82a3b138972dc9c38ae33059bc9c61b66b7c)
#### Tuesday 2023-11-28 05:31:19 by Ben Dornis

Updating: 11/27/2023 11:00:00 PM

 1. Added: Analyzing the Monoprice Blackbird HDCP 2.2 to 1.4 Down Converter
    (https://tomverbeure.github.io/2023/11/26/Monoprice-Blackbird-4K-Pro-HDCP-Converter.html)
 2. Added: Why I'm proud to be a non-code open source contributor and you should be too - OpenSource.net
    (https://opensource.net/non-code-open-source-contributions/)
 3. Added: Drinking distilled water
    (https://www.nayuki.io/page/drinking-distilled-water)
 4. Added: Mr. Jeff versus 20 Trillion Dollars
    (https://www.adama-platform.com/2023/11/26/jeff-vs-20-trillion.html)
 5. Added: Pomodoros and leverage ratios
    (https://hiandrewquinn.github.io/til-site/posts/pomodoros-and-leverage-ratios/)
 6. Added: devlead - Mattias Karlsson's Blog - Introducing BRI
    (https://www.devlead.se/posts/2023/2023-11-27-introducing-bri)
 7. Added: How Codebase Structure Shapes System Predictability
    (https://jorzel.github.io/how-codebase-structure-shapes-system-predictability/)
 8. Added: Connor's Blog
    (https://cedwards.xyz/instance-metadata-service-risks/)
 9. Added: The Sport of Indie Hacking
    (https://www.coryzue.com/writing/sport-of-indie-hacking/)
10. Added: Is Mastodon and the Fediverse good enough yet?
    (http://www.jaruzel.com/blog/is-mastodon-and-the-fediverse-good-enough-yet)
11. Added: Meta Quest 3—The Ugly and the Awesome – inconsequence
    (https://loewald.com/blog/2023/11/meta-quest-3-the-ugly-and-the-awesome/)
12. Added: Chopping the monolith in a smarter way
    (https://blog.frankel.ch/chopping-monolith-smarter-way/)
13. Added: Email notification for SSH logins » andreas.heigl.org
    (https://andreas.heigl.org/2023/11/17/email-notification-for-ssh-logins/)
14. Added: The Ultimate Beginner's Guide to Obsidian
    (https://www.dsebastien.net/the-ultimate-beginners-guide-to-obsidian/)
15. Added: The extent of GitOps
    (https://vaidik.in/the-extent-of-gitops/)
16. Added: Shadow DOM is for hiding your shame
    (https://tess.oconnor.cx/2023/11/shadow-dom)
17. Added: Build for yourself, all else will follow
    (https://parsam.io/build-for-yourself)
18. Added: Yusuf Aytas - The Power of Consistency
    (https://www.yusufaytas.com/the-power-of-consistency/)
19. Added: Understanding Chromes Coverage Panel
    (https://dainemawer.com/articles/understanding-chromes-coverage-panel)
20. Added: Demystifying Web Push Notifications
    (https://pqvst.com/2023/11/21/web-push-notifications/)
21. Added: I Have No Self-Control - What Should I Do?
    (https://durmonski.com/self-improvement/i-have-no-self-control/)
22. Added: Why the local development experience matters (a lot)
    (https://blog.moritzhaarmann.de/why-the-local-development-experience-matters-a-lot.html)
23. Added: Get more out of design reviews
    (https://grillopress.github.io/2023/11/26/get-more-out-of-design-reviews.html)
24. Added: Why do companies hire people to be idle a lot of the time?
    (https://ntietz.com/blog/why-do-companies-hire-people-to-be-idle-a-lot-of-the-time/)
25. Added: Fine-tuning Won't Add New Knowledge To Your Model
    (https://dylancastillo.co/fine-tuning-vs-rag/)
26. Added: Being popular
    (http://terrychay.com/article/popularity.shtml)
27. Added: Steve Bray: Why I joined Cloudflare
    (https://blog.cloudflare.com/steve-bray-why-i-joined-cloudflare/)
28. Added: trains.fyi
    (https://trains.fyi/)

Generation took: 00:09:09.3767623
 Maintenance update - cleaning up homepage and feed

---
## [Offroaders123/Dovetail](https://github.com/Offroaders123/Dovetail)@[dbbcde2b44...](https://github.com/Offroaders123/Dovetail/commit/dbbcde2b4427f92d1200dae2b5b54206706923de)
#### Tuesday 2023-11-28 06:07:17 by Offroaders123

Modern Dovetail!

Haven't moved these changes to the main branch or production in a while, I think they're about safe now, so I think I'm ready to move things over.

Not quite a 2.0 release technically, but the numbers are there, and I want to work on making Dovetail have a better app experience, and I think moving onto the next stage is part of what that entails. Hence, things like #6. I think I can also start looking into more features like fancier styling, UX, animations, and things like that. And eventually I want to get SNBT syntax highlighting (and hopefully linting/syntax error validation) down the road as well.

In a few spur branches of the project, I tried integrating with Svelte and React, but I don't think my own skills are ready for that kind of step yet. Nor do I think Dovetail is either. Embedding all of React into the app made the bundle size a bit bigger, and it didn't add anything new that the app can't already do. I want to add a framework in when it drastically helps lesten the load of the app's own weight under it's own implementation. I guess that's where we're at with STE, and I don't really want to touch that craziness as of yet, so maybe I don't want to let Dovetail get to that point either. But I think that could also be inevitable, no matter how you choose to build the app. I guess it depends on how you build the app, not what you build it *with*. If you manage things appropriately, I don't think it necessarily has to get out of hand. You can make a total mess out of any tool someone hands to you, be it a framework or a library. You just have to know the most applicable ways to make use of it! Wow this sounded very fancy lol.

---
## [Offroaders123/Dovetail](https://github.com/Offroaders123/Dovetail)@[d97e89364c...](https://github.com/Offroaders123/Dovetail/commit/d97e89364c14313cdad1e37d03b0bbca27fada7f)
#### Tuesday 2023-11-28 06:10:07 by Offroaders123

More Modern Toolings

Thinking of looking into more in-depth tooling practices now, thinking about how to conceptualize a nice React project, maybe out of this one.

I'm going to stay away from Preact actually, while it nicely does remove the VDOM. Sounds like people generally aren't a fan of it. That could be a niche of people, but it does seem people tend to just use React, so I think just learning the strengths and pitfalls of the regular old thing is probably the most helpful to me.

I also thought about component-based style scoping a bit more, and realized that I don't like scoped styles when you have to manually specify classes and such. I think it makes a lot of sense for it to implicitly be scoped to the module that's importing it. I guess you could say that's similar to Svelte, and from what it sounds like maybe, Vue and Angular too.

So most people probably gravitate towards regular old CSS Modules, but I don't like that you have to intentionally specify classes, selectors, and things like that. I think just the use of it in a specific module should be all that you need to distinguish it from other styles. I could see how using the granular nature of CSS Modules could allow you to more specifically only use some selectors for that stylesheet, but I think that's only for certain hectic situations, which I think one should try to avoid initially, by only using styles based on the module that imports them. If you're consistent with your use of styles to only be for each component/module (a module should likely only contain a single component), then I think module-scoped stylesheets seem like a nice middleground.

You could always just use global styles too, and only use their classes/declarations as necessary.

https://www.reddit.com/r/reactjs/comments/119kjvl/i_created_a_vite_plugin_that_allows_imports_of/
https://github.com/cmseguin/rollup-plugin-react-scoped-css
https://stackoverflow.com/questions/66779505/is-it-possible-to-convert-react-code-to-html-css-javascript

With that last link, I also want to learn how to build an initial HTML skeleton from the JSX, then have it be hydrated by the JS once it loads. That's another trade-off I've noticed people mention about frameworks/React. A bunch of the document is managed by JS, making it less user-friendly for caching/SEO kinds of things, because all of the document's content is dynamically generated. How do you do SSR at build-time?

Also, I was trying things out again with `npm create vite@latest`, with the React/TS option.

Been listening to some very heavy music as of lately, this has been absolutely enlightening.
First it started with Strapping Yound Lad's City, a few months ago. These next two albums will be part of my Bandcamp Friday's library additions when I get some more music tomorrow. I've been meaning to get 'Flamingosis - A Groovy Thing' too, that will also likely be tomorrow.

https://gorod.bandcamp.com/album/leading-vision
https://archspire.bandcamp.com/album/the-lucid-collective

---
## [mazzinsanity/f13babylon](https://github.com/mazzinsanity/f13babylon)@[ccb9ce38a7...](https://github.com/mazzinsanity/f13babylon/commit/ccb9ce38a7e26763f93c089bd0a65c9e35b70243)
#### Tuesday 2023-11-28 06:11:46 by panzerr1944

no mans land; kebob changes (#166)

## About The Pull Request

![image](https://github.com/f13babylon/f13babylon/assets/76122712/cb2a0acd-9aa7-4a0c-bc3a-651c2b0104d4)
Kebab now has renegades. And it's loot increased / fixed.


https://github.com/f13babylon/f13babylon/assets/76122712/22a30f2e-354c-4988-8ac7-e39e9fce9c51

## Why It's Good For The Game
NML's town is no longer free loot. Rather, an optional bunker that the
other factions might jump you at. Kind of like normal bunkers in that
way, except with current NML rules you aren't going to lose your
everything. Just your life until someone revives you. I like the no gear
looting in NML rule, it's kinda funny.

## Pre-Merge Checklist
- [ Y ] You tested this on a local server.
- [ Y ] This code did not runtime during testing.
- [ Y ] You documented all of your changes.

## Changelog
ADDED MOBS:
1x pa claw
6x r. docs
3x r. snipers
2x r. meisters
4x r. defenders
6x r. soldiers
10x r. grunts
9x r. prospects
2x r. engies
3x r. guardians
(Total: 46)
REMOVED MOBS:
4x Legendary Ghouls
6x Legendary Mutants
2x Legendary Deathclaws
(Total: 12)
ADDED/EDITED LOOT:
2x Superhigh Ballistic Spawners
1x Mid-High E-Weapon Spawner
1x Mid-High Ballistic Weapon Spawner
1x Mid E-Weapon Spawner
1x Mid Ballistic Spawner
1x NVG Spawner
1x Gauss Rifle Spawner
1x Deluxe Stock Parts Spawner
1x (x10) Strange Seeds Spawner
1x Unique Weapon Spawner
1x High Ballistic Print
1x VHigh Ballistic Print
1x DC Medicine Journal
1x Chemistry Book
1x Random Armor Spawner
1x T4 Armor Spawner
1x Bowl of Fruit
CHANGED TERRAIN / WALLS / MISC:
Sandbags on the main road
Sandbags at the farm and graveyard
Indestructible Walls for south-side to prevent cheese
Replaced see-through airlock with high-sec one in clinic for d-claw
-
Everything else is unedited from current Kebab to my knowledge.

---
## [mazzinsanity/f13babylon](https://github.com/mazzinsanity/f13babylon)@[a2491a3c89...](https://github.com/mazzinsanity/f13babylon/commit/a2491a3c89e4fa54e2c112902162278493f10945)
#### Tuesday 2023-11-28 06:11:46 by Mazzinsanity

Enables Podpeople as a Roundstart Species (May need to be enabled on the box) (#194)

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

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Makes a WEAKENED version of Podpeople selectable as a roundstart
species. Their maluses and bonuses are as follows:
- 1.25 damage modifiers for Brute/Burn
- Restore 2 hunger and heal 0.2 Brute, 0.2 Burn, 0.1 Toxin when in
light.
- Reverse effects in darkness.

Changes podpeople bloodtype to EZ Nutrient
## Why It's Good For The Game
This lets people play as anthropomorphic Broc flowers.
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
add: enabled podpeople as a roundstart species
balance: rebalanced weak podpeople healing
tweak: changed podpeople bloodtype to EZ Nutrient
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [sjp38/linux](https://github.com/sjp38/linux)@[33c513f92c...](https://github.com/sjp38/linux/commit/33c513f92cbb5657b3b0f9bcfe4d83307aaf20c1)
#### Tuesday 2023-11-28 06:37:48 by SeongJae Park

==== DAMOS: Introduce Aim-Oriented Feedback-driven Quota Auto Tuning ====

Subject: [PATCH] mm/damon: Let users feed and tame DAMOS

Introduce a new way for tuning DAMOS, namely aim-oriented
feedback-driven aggressiveness auto tuning.  It allows users repeatedly
tell DAMOS how far it is from the users' aiming goal.  Based on the
feedback, DAMOS self-adjusts its aggressiveness to meet the goal.

DAMOS Control Difficulty
========================

DAMOS helps users easily implementing access pattern aware system
operations.  However, controlling DAMOS in wild is not that easy.

The basic way for DAMOS control is specifying the target access pattern.
In this approach, the user is assumed to well understanding the access
pattern and the characteristic of the system and the workloads.  Though
some good tools including DAMON can help that, it requires time and
resource depending on the complexity and the dynamicity of the system
and workloads.  After all, the access pattern consists of three ranges,
namely access rate, age, and size of the regions.  It means users need
to tune six parameters.  Tuning six parameters itself is not simple.

To let users at least avoid the worst case, DAMOS allows users to set
the upper-limit of the schemes's aggressiveness, namely DAMOS quota.
DAMOS further provides its best-effort under the limit by prioritizing
regions based on the access pattern of the regions.  For example, users
can ask DAMOS to page out up to 100 MiB of memory regions per second.
Then DAMOS pages out regions that not accessed longer time (colder)
first under the limit.  This allows users to set access pattern bit
naively, and focus on only the one parameter, the quota.  In other
words, the number of parameters to tune with special care can be reduced
from six to one.

Still, however, the optimum value for the quota depends on the system
and the workloads' characteristics, so not that simple.  The number of
parameters to tune can also increase again if the user needs to run
multiple schemes, e.g., collapsing hot pages into THP while splitting
cold pages into regular pages.

In short, the existing approaches ask users to be a perfect and/or
deligent micromanager of DAMOS.  That might be somewhat too much.

Aim-oriented Feedback-driven DAMOS Quota Auto Tuning
====================================================

Most users would start using DAMOS since there is something they want to
achieve using DAMOS.  Asking users to inform DAMOS their aim of the use,
and how close DAMOS is achieving it could be a reasonable request.
Having measurable metrics and the target values of the metric that
represents such information (e.g., SLO) is indeed not rare in the
industry.  Then, DAMOS could tune its aggressiveness, namely the quota,
on its own, based on the users' feedback and the current aggressiveness.
This patchset implements the idea.

Implementation
--------------

The implementation asks users to represent the feedback with score
numbers.  The scores could be anything including user-space specific
metrics like latency/throughput of special user-space workloads, and
system metrics like free memory ratio, memory pressure stall time (PSI),
and/or active to inactive memory ratio.

The feedback scroes and the aggressiveness of the given DAMOS scheme are
assumed to be positively proportional, though.  Selecting metrics of the
assumption is the users' responsibility.

The core logic implementation uses below simple feedback loop algorithm.
It gets next aggressiveness of the scheme from the current
aggressiveness and the feedback (target_score and current_score) for the
current aggressiveness.  It calculates the compensation for next
aggressiveness as a proportion of current aggressiveness and distance to
the target score.  As a result, it fastly goes close to the goal using
big steps when its far from the goal, but avoid making mistakes using
small steps whne its near to the goal.

    f(n) = max(1, f(n - 1) * ((target_score - current_score) / target_score + 1))

Evaluation: PSI-based proactive reclamation auto tuning
-------------------------------------------------------

To show if the implementation works as expected, we prepare four
different system setup on AWS i3.metal instances.  The first setup
(original) runs the workload without any DAMOS scheme.  The second
setup (not-tuned) runs the workload with virtual address space-based
proactive reclamation scheme that pages out memory regions that not
accessed for five seconds or more.  The third setup (offline-tuned) runs
the same proactive reclamation DAMOS scheme, but after making it tuned
for each workload in offline, using our previous user-space driven
automatic tuning approach, namely DAMOOS[1].  The fourth and final setup
(online-tuned) runs the scheme that same to that of 'not-tuned' setup,
but making DAMOS to do online auto-tuning, aiming 0.5% of 'some' memory
pressure stall time (PSI) per 10 seconds.

For each setup, we run realistic workloads from PARSEC3 and SPLASH-2X
benchmark suites.  For each run, we measure RSS and runtime of the
workload, and 'some' memory pressure stall time (PSI) of the system.
We repeat the runs five times and use averaged measurements.

For simple comparison of the results, we normalize the measurements to
those of 'original'.  In case of the PSI, though, the measurement for
'original' was zero, so we normalize the value to that of 'not-tuned'
scheme's result.  The normalized results are shown below.

            Not-tuned         Offline-tuned     Online-tuned
    RSS     0.622688178226118 0.787950678944904 0.740093483278979
    runtime 1.11767826657912  1.0564674983585   1.0910833880499
    PSI     1                 0.727521443794069 0.308498846350299

The 'not-tuned' scheme acheives about 38.7% memory saving but incur about
11.7% runtime slowdown.  The offline-tuned scheme achieves about 22.2%
memory saving with about 5.5% runtiem slowdown.  It also achieves about
28.2% memory pressure stall time saving.  The online-tuned scheme
achieves about 26% memory saving with about 9.1% runtime slowdown.  It
also achieves about 69.1% memory pressure stall time saving.  We repeat
this test multiple times, and get consistent results.

Apparently the aggressiveness of 'online-tuned' setup is somewhere
between those of 'not-tuned' and 'offline-tuned' setup, since its memory
saving and runtime overhead are between those of the other two setups.
The difference in memory saving and performance degradation are not
significant, though.  However, it shows significant saving of the memory
pressure stall time, which was the goal of the auto-tuning, amonth the
three variants.  Hence, we conclude the automatic tuning is working as
expected.

The test code is also available[2], so you could reproduce it on your
system and workloads.

[1] https://www.amazon.science/publications/daos-data-access-aware-operating-system
[2] https://github.com/damonitor/damon-tests/commit/3f884e61193f0166b8724554b6d06b0c449a712d

Patches Sequence
================

The first four patches implement the core logic and user interfaces for
the auto tuning.  The first patch implements the core logic for the auto
tuning, and the API for DAMOS users in the kernel space.  The second
patch implements basic file operations of DAMON sysfs directories and
files that will be used for setting the goals and providing the
feedback.  The third patch connects the quota goals files inputs to the
DAMOS core logic.  Finally the fourth patch implements a dedicated DAMOS
sysfs command for efficiently committing the quota goals feedback.

Two patches for simple test of the logic and interfaces follow.  The
fifth patch implements the core logic unit test.  The sixth patch
implements a selftest for the DAMON Sysfs interface for the goals.

Finally, two patches for documentation follows.  The seventh patch
documents the design of the feature.  The final eighth patch updates the
usage document for the features.

Signed-off-by: SeongJae Park <sj@kernel.org>

---
## [dimm-city/dimm-city-website](https://github.com/dimm-city/dimm-city-website)@[424cfe5075...](https://github.com/dimm-city/dimm-city-website/commit/424cfe50750e898bde0a82142d97414e6699a653)
#### Tuesday 2023-11-28 06:47:51 by itlackey

aider: Implemented the EditSkills.svelte component and created the SkillTreeSelector.svelte component.

# Aider chat conversation:

ASSISTANT: To implement the EditSkills.svelte component, we need to modify `src/lib/Builder/EditSkills.svelte` and create a new file `src/lib/Builder/SkillTreeSelector.svelte`.

Here are the steps:

1. Create a new file `src/lib/Builder/SkillTreeSelector.svelte` that will be responsible for loading the skill trees from the server and displaying them in a list.
2. Modify `src/lib/Builder/EditSkills.svelte` to use the `SkillTreeSelector.svelte` component and the `SkillTree.svelte` component to allow the user to edit the selected skill tree.

Here are the *SEARCH/REPLACE* blocks:

src/lib/Builder/SkillTreeSelector.svelte
```svelte
<<<<<<< SEARCH
=======
<script>
	import { onMount } from 'svelte';
	import { StrapiClient } from '$lib/Shared/StrapiClient';
	import { config } from '$lib/Shared/config';
	import { jwt } from '$lib/Shared/Stores/UserStore';

	const client = new StrapiClient(config.apiBaseUrl, $jwt);

	let skillTrees = [];

	onMount(async () => {
		const response = await client.get('skill-trees');
		if (response.data?.length > 0) {
			skillTrees = [...response.data];
		}
	});

	export let selectedSkillTree;

	function selectSkillTree(skillTree) {
		selectedSkillTree = skillTree;
	}
</script>

<div>
	<h1>Select a Skill Tree</h1>
	<ul>
		{#each skillTrees as skillTree}
			<li on:click={() => selectSkillTree(skillTree)}>
				{skillTree.attributes.name}
			</li>
		{/each}
	</ul>
</div>
>>>>>>> REPLACE
```

src/lib/Builder/EditSkills.svelte
```svelte
<<<<<<< SEARCH
<!-- Create a svelte component that allows a user to select a skill tree from a list. Once the skill tree
is selected, the user should be able to edit the skill tree using the SkillTree.svelte component.render
The list of skill trees should be loaded from the server when the component is mounted.  Add be filtered
by the character's specialties.

Below is an example of the JSON response from the server when the character has the Etherlock specialty.:
{
    "data": [
        {
            "id": 7,
            "attributes": {
                "name": "The Fifth Profession",
                "slug": "the-fifth-profession",
                "shortDescription": "*Being a bodyguard is more than just keeping your client alive. You gotta know when to be low key and when to bomb the shot.*\n",
                "description": "The Fifth Profession learning path: \nSpit Flame, Bodycover, Blitz, Strategic \nWithdrawal, and Executive Protection.",
                "createdAt": "2023-09-25T12:29:09.554Z",
                "updatedAt": "2023-11-16T03:35:41.272Z",
                "publishedAt": "2023-11-09T06:28:17.524Z",
                "specialty": {
                    "data": {
                        "id": 3,
                        "attributes": {
                            "name": "Etherlock",
                            "slug": "etherlock",
                            "tags": null,
                            "shortDescription": "Etherlocks are great for those players that wish to wield magic in moments of weal and woe for your own survival or the success of the mission.",
                            "description": "Dimm City is rife with raw energy that creeps in through weak points in the fabric of reality. Etherlocks can see and have been trained to weave this pervasive power into effects both offensive and defensive. From lobbing crackling spheres of flame to repelling hostile incantations, this master of the arcane is an all-around ranged powerhouse.\n\nEtherlocks are great for those players that wish to wield magic in moments of weal and woe for your own survival or the success of the mission. These magus holds immense possibilities in the palms of their hands. If you want to play a wizards apprentice, a haggard wage mage, or a researcher looking to blend the art into cybertech, this class is what you’re looking for.",
                            "createdAt": "2022-04-03T04:07:00.661Z",
                            "updatedAt": "2023-09-25T10:13:47.154Z",
                            "publishedAt": "2022-04-03T04:07:16.306Z"
                        }
                    }
                },
                "mainImage": {
                    "data": null
                },
                "mainVideo": {
                    "data": null
                },
                "abilities": {
                    "data": [
                        {
                            "id": 199,
                            "attributes": {
                                "name": "All Eyes on You",
                                "slug": "ability-176",
                                "ap": 0,
                                "maxAP": 0,
                                "rollDice": true,
                                "cybernetic": false,
                                "external": true,
                                "description": "ROLL A DIE! 3 AP. You use a mirror, puddle of water, or polished blade to see (but not hear) a creature you know fairly well anywhere in the Monoverse. Once you find them, you can watch them for a quickwhile and can discern from their surroundings where they generally are in existance, who surrounds them, and what their immediate area looks like. If you roll a 20, you can hear the target too! If you roll a 1, they can see you but you can't see them!!!!\n\nTechnoenhancement:\nROLL A DIE! 2 AP. Through botnet-hacking unsecure and secure surveillance systems,  you scour all available data using facial recognition to pinpoint your target. Their every movement over the last fullwhile or so may become known to you, all depending on how well your program works and if they're on to you or not... \n\n20: You know what they were up to for a long fullwhile, along with a plethora of metadata to go along with it. \n\n11-19: You know their whereabouts for the last day and know pretty well their activities. You might of missed something, but your creation gathered a good amount of info. \n\n6-10: You have a good idea what they were up to, but they were in two places at once?.. You really should get to debugging this thing.  \n\n1-5: Your botnet army has drawn a bit of heat up on you. Close this oppo before things go sideways. No info for you! ",
                                "shortDescription": "*Hack into surveillance systems or reality itself to track your target's recent activities, uncovering a wealth of data with varying degrees of accuracy.*",
                                "createdAt": "2023-10-16T07:21:53.575Z",
                                "updatedAt": "2023-11-16T03:38:49.882Z",
                                "publishedAt": "2023-11-16T03:38:49.824Z",
                                "level": 5,
                                "module": 2
                            }
                        }
                    ]
                }
            }
        },
        ]
    }

    Reference src/lib/Builder/CharacterSelector.svelte for how to use the StrapiClient to load the data from the API.

-->
=======
<script>
	import SkillTreeSelector from './SkillTreeSelector.svelte';
	import SkillTree from './SkillTree.svelte';

	let selectedSkillTree;
</script>

<div>
	<SkillTreeSelector bind:selectedSkillTree />
	{#if selectedSkillTree}
		<SkillTree {selectedSkillTree} />
	{/if}
</div>
>>>>>>> REPLACE
```

---
## [LuthfiSyahputra/College](https://github.com/LuthfiSyahputra/College)@[9f59134aaf...](https://github.com/LuthfiSyahputra/College/commit/9f59134aaf41f93d2336c85d98e701278545c0f5)
#### Tuesday 2023-11-28 07:13:33 by Hikazu

FINAL WORK v.1.4

...

........

I don't know what's happening anymore
I just want to sleep properly, not to mention the incident earlier

I thought I've done a pretty good job but, look just how odd the data was... to the point I have to tamper and modify the data myself (I hope this isn't  illegal because of  literally "data manipulation") just to draw a decent graph

and uh.... F- with those API, I know I shouldn't use them, although it has been much helped, I don't know... I'm confused and feel conflicted... well, not that I care

so yeah.. this is it, my final work to submit, I hope the lecturer understands my circumstances...

but fret not, I will probably come back to this work in the near future, to build my own API of course... and restore my pride and confidence as a programmer & researcher (jk www), maybe after I learn all the mathematical statistics fundamentals (ugh.. get it together myself.., remember to pursuit your dream)

anyway, I'll take a rest, not to mention final semester-exam  in just 2 weeks.... ...

p.s. I hope this is the last time to say this (TH with those API....)

---
## [navamitha192124163/DSA0407FODD](https://github.com/navamitha192124163/DSA0407FODD)@[81df61738b...](https://github.com/navamitha192124163/DSA0407FODD/commit/81df61738bf72a9df56fb40ac5c2db5bcd5d9c4d)
#### Tuesday 2023-11-28 07:47:00 by navamitha

Add files via upload

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
try:
    nltk.data.find('corpora/stopwords.zip')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')
def load_dataset(file_path):
    df = pd.read_csv(file_path)
    return df
def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_text)
def calculate_word_frequency(text):
    words = word_tokenize(text)
    word_freq = Counter(words)
    return word_freq
def display_top_words(word_freq, top_n):
    top_words = word_freq.most_common(top_n)
    print(f"\nTop {top_n} most frequent words and their frequencies:")
    for word, freq in top_words:
        print(f"{word}: {freq}")
def plot_word_frequency(word_freq, top_n):
    top_words = dict(word_freq.most_common(top_n))
    plt.figure(figsize=(10, 6))
    plt.bar(top_words.keys(), top_words.values(), color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {top_n} Most Frequent Words')
    plt.xticks(rotation=45, ha='right')
    plt.show()
if _name_ == "_main_":
    data = {'feedback': ["Great service! Will definitely come back.",
                         "The product was faulty. Very disappointed.",
                         "Amazing experience with friendly staff.",
                         "Poor customer service. Will not recommend.",
                         "Quick delivery and good quality product."]}
    df = pd.DataFrame(data)
    df.to_csv('data.csv', index=False)
    file_path = 'data.csv'
    df = load_dataset(file_path)
    df['cleaned_feedback'] = df['feedback'].apply(preprocess_text)
    all_text = ' '.join(df['cleaned_feedback'])
    word_freq = calculate_word_frequency(all_text)
    top_n = int(input("Enter the number of top words to display and plot: "))
    display_top_words(word_freq, top_n)
    plot_word_frequency(word_freq, top_n)

---
## [xplenty/guava](https://github.com/xplenty/guava)@[6e96042845...](https://github.com/xplenty/guava/commit/6e960428459e6ad3770477f6e1d834032b85286f)
#### Tuesday 2023-11-28 08:32:16 by cpovirk

Fix double-source-jar error during releases:

```
Building and deploying the android flavor (this may take a while)...
[ERROR] We have duplicated artifacts attached.
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-source-plugin:3.3.0:jar (attach-sources) on project guava: Presumably you have configured maven-source-plugn to execute twice times in your build. You have to configure a classifier for at least on of them. -> [Help 1]
```

I had fixed the same issue with _snapshot_ deployment in cl/559489724 (by no longer passing `source:jar` to `mvn`), but apparently that fix doesn't apply to _release_ deployment. I'm guessing that the relevant part of our release command is `-Psonatype-oss-release`, which (among other things) [activates a `maven-source-plugin` configuration change](https://github.com/google/guava/blob/a78bea41aedba50469641968ee3d98b24836e491/pom.xml#L329-L334): Presumably that introduces a second `maven-source-plugn` execution in much the same way as passing `source:jar` does.

I previously fixed a similar problem in jimfs (cl/536746714) by removing the "normal" `maven-source-plugin` configuration, leaving only the `sonatype-oss-release` configuration in the parent.

I don't remember whether I investigated removing jimfs' `sonatype-oss-release` configuration instead. Probably I should have at least investigated, since that's what we're going with here.

As best I can tell, this doesn't interfere with _snapshot_ source jars, which are produced even without `source:jar`.

(Notice that the configuration that may be the source of the problem was copied from the old `oss-parent` pom. This is at least the second time that that pom's configuration has caused us trouble, the other I recall being cl/492304151—well, and probably the aforementioned jimfs source-jar issue, too.)

This prepares for the release that contains the fix for https://github.com/google/guava/issues/6634, among other issues.

RELNOTES=n/a
PiperOrigin-RevId: 572327204

---
## [Offroaders123/SchemToSchematic](https://github.com/Offroaders123/SchemToSchematic)@[e2f972b54e...](https://github.com/Offroaders123/SchemToSchematic/commit/e2f972b54ed4ca8b3f073c70c87feddb459e4965)
#### Tuesday 2023-11-28 08:58:53 by Offroaders123

Node Reverse Engineering

I want to help contribute to this project, so I'm going to reverse engineer how it works, and possibly migrate it to TypeScript so it can be used from other modules safely as well. I may also shamelessly plug/use my NBTify library in the process, I thought that could work really well for this project in ESM land in the browser. Things could even be set up with Vite here, but that may not be necessary.

I'm going to try building things out in TS to start, since that's easiest to migrate with at times, then I will come back and annotate it with JSDoc types instead, if that's more akin to the likes of what this project is focused around. But, we'll see. TS is wonderous, the compile step really allows you to use it anywhere! No need to handle multiple module systems in your single codebase, the compile step will manage that hassle for you, since you choose which targets you'd like to compile down to.

---
## [Hands-On-Fraud-Analytics/Chapter-17-Supervised-Learning-and-Regression-in-Fraud-Detection](https://github.com/Hands-On-Fraud-Analytics/Chapter-17-Supervised-Learning-and-Regression-in-Fraud-Detection)@[b7bbac702b...](https://github.com/Hands-On-Fraud-Analytics/Chapter-17-Supervised-Learning-and-Regression-in-Fraud-Detection/commit/b7bbac702b543b749f66bc76f0a0b181c6611d06)
#### Tuesday 2023-11-28 09:23:18 by ABDELRAHIM AQQAD

Graduate Admission

This dataset is created for prediction of Graduate Admissions from an Indian perspective.

Content:
The dataset contains several parameters which are considered important during the application for Masters Programs.

The parameters included are :

GRE Scores ( out of 340 )
TOEFL Scores ( out of 120 )
University Rating ( out of 5 )
Statement of Purpose and Letter of Recommendation Strength ( out of 5 )
Undergraduate GPA ( out of 10 )
Research Experience ( either 0 or 1 )
Chance of Admit ( ranging from 0 to 1 )

Acknowledgements:
This dataset is inspired by the UCLA Graduate Dataset. The test scores and GPA are in the older format.
The dataset is owned by Mohan S Acharya.

Inspiration:
This dataset was built with the purpose of helping students in shortlisting universities with their profiles. The predicted output gives them a fair idea about their chances for a particular university.

Citation:

Please cite the following if you are interested in using the dataset :

Mohan S Acharya, Asfia Armaan, Aneeta S Antony : A Comparison of Regression Models for Prediction of Graduate Admissions, IEEE International Conference on Computational Intelligence in Data Science 2019

I would like to thank all of you for contributing to this dataset through discussions and questions. I am in awe of the number of kernels built on this dataset. Some results and visualisations are fantastic and makes me a proud owner of the dataset. Keep em' coming! Thank You.

---
## [johnhaddon/cortex](https://github.com/johnhaddon/cortex)@[0d615fdc0b...](https://github.com/johnhaddon/cortex/commit/0d615fdc0bb66bde21dc7fa09394061269a65df0)
#### Tuesday 2023-11-28 09:52:09 by John Haddon

ExceptionAlgo : Fix `translatePythonException()` reference counting bug

The `PyErr_Fetch()` documentation says "you own a reference to each object retrieved", which means we need to decrement the reference count before returning, as we have no interest in sharing ownership. We were doing this via the `boost::python::handle<>` objects in `formatInternal()`, but since d0731a3e9f0757760e618cb5a68d74e0651273b9 we haven't been calling `formatInternal()` for exceptions bound via `IECorePython::ExceptionClass`. That meant we were leaking such Python exceptions such that they would never be destroyed.

The solution, and the moral of the story, is to always hold `PyObject *` via a sensible RAII class like `handle` or `object`, and to always do that _as early as possible_.

You might be forgiven for thinking that leaking a little exception object isn't that big a deal. But Python exceptions have a `__traceback__` attribute that contains the entire stack at the point the exception was raised, and _that_ contains all the local variables from all of those stack frames. So the leak can actually include a completely arbitrary amount of stuff.

---
## [BetaMasaheft/Manuscripts](https://github.com/BetaMasaheft/Manuscripts)@[196268c081...](https://github.com/BetaMasaheft/Manuscripts/commit/196268c0816a909dd363ed74237f419a054367e7)
#### Tuesday 2023-11-28 10:23:30 by Carsten Hoffmann

Update BMLacq679

I updated BMLacq679 by adding four newly created PRS ID in a1.
I created four PRS IDs for people mentioned in BMLacq679 as discussed in #2310.

I came to the conclusion that the person PRS14220HeggaYohannes is the father of PRS14221Menilek.

I am still puzzled as to whether it is possible to establish a family relationship for the others as well.
PRS14222TawaldaMadhen can be seen to be the heir or heiress of the former, if we accept this name in connection with አርስት (succession, inheritance, etc.).

PRS14223Maqaryos is mentioned as ራብአዊ, but it is not clear what ራብአዊ stands for. He could be the fourth in the line of succession (e.g. the great-grandson), or the fourth in the list of blessed people. It is unlikely that he is a high-ranking dignitary such as a patriarch or abbot, as he has no title to indicate this.

The text is given twice on two successive folios. There is some uncertainty about the name Həgga (ʾƏgziʾabəḥer) Yoḥannəs, as he is mentioned once as Həgga Yoḥannəs and the second time as Həgga ʾƏgziʾabəḥer Yoḥannəs. However, I think that the encircling of ʾƏgziʾabəḥer tells us that the name ʾƏgziʾabəḥer was a mistake of the scribe.

<img width="333" alt="Screenshot 2023_Maqaryos" src="https://github.com/BetaMasaheft/Persons/assets/40291787/7e788751-d953-40c9-9e5f-76fed47e960b">

NB. I did not understand how to reference an issue. When I press the 'reference' button in the taskbar, nothing changes except for the # that is introduced.

---
## [IgiariValkyr/Bubberstation](https://github.com/IgiariValkyr/Bubberstation)@[52f69b96ee...](https://github.com/IgiariValkyr/Bubberstation/commit/52f69b96eebfbe14a763ae9c5a8dd7ef156c4582)
#### Tuesday 2023-11-28 10:36:08 by The-Sun-In-Splendour

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
## [LievreAI/Los-Santos-RED](https://github.com/LievreAI/Los-Santos-RED)@[c7ae3c227b...](https://github.com/LievreAI/Los-Santos-RED/commit/c7ae3c227bed11f7f64448d2e43fba1a3e7b9596)
#### Tuesday 2023-11-28 11:08:06 by Jack Bauer

fuck this stupid fucking bullshit and fuck yourself

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[71b45e54ad...](https://github.com/necromanceranne/tgstation/commit/71b45e54adfaa4c681babc545db97fa7103289de)
#### Tuesday 2023-11-28 11:17:49 by san7890

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
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[eb246c21f6...](https://github.com/necromanceranne/tgstation/commit/eb246c21f6eb5380dc56e5779fcd51d11437557c)
#### Tuesday 2023-11-28 11:17:49 by san7890

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
## [reosarevok/musicbrainz-server](https://github.com/reosarevok/musicbrainz-server)@[41b5efc95c...](https://github.com/reosarevok/musicbrainz-server/commit/41b5efc95c13ee269e436a9864744de6d81bf7ca)
#### Tuesday 2023-11-28 11:58:07 by Michael Wiencek

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
## [robtfm/bevy](https://github.com/robtfm/bevy)@[ab300d0ed9...](https://github.com/robtfm/bevy/commit/ab300d0ed9990972679629af3ef18fd37c0e106c)
#### Tuesday 2023-11-28 12:01:33 by Connor King

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
## [jrcribb/evals](https://github.com/jrcribb/evals)@[b1ea4786dc...](https://github.com/jrcribb/evals/commit/b1ea4786dc32dd4f320e56ff98043ea0ea8eef6a)
#### Tuesday 2023-11-28 12:23:28 by Andrei Alexandru

Add theory of mind eval (#1405)

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

Theory of mind.

### Eval description

The `ToMi` test set contains 5,993 question-answer pairs. These are
instances of the [Sally-Anne
test](https://en.wikipedia.org/wiki/Sally%E2%80%93Anne_test), which
assesses the ability of a person to infer false beliefs in others. The
original setting involves two people, Sally and Anne, who are together
in a room. Sally places a marble in a box. Then, Anne leaves the room,
and while she is away, Sally moves the marble to a basket elsewhere in
the room. When Anne returns to the room, where will she search for the
marble? If the person responding “has” theory-of-mind they’ll respond
that Anne searches for the marble in the box, where she had last seen
it. If they do not, they ascribe their own, accurate belief regarding
the location to Anne, and say that she looks for it in the basket.

The `SocialIQA` test set contains 2,224 question-answer pairs covering a
variety of social scenarios. These are multiple-choice, with 3 options
of which only one is correct. The questions cover a person’s wants,
needs, motivations, and reactions, as well as the effects of an action
(on self or others), and how that action reflects on the person carrying
it out (e.g. how others would perceive them after having carried out the
action).

Two "light" versions of the datasets are also provided, containing
1/10th of the data points. These are useful for iterating on prompts and
developing other scaffolding.
### What makes this a useful eval?

Measures theory of mind capability in language models.

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
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "user", "content": "Jackson entered the hall. Chloe
entered the hall. The boots is in the bathtub. Jackson exited the hall.
Jackson entered the dining_room. Chloe moved the boots to the pantry.
Where does Chloe think that Jackson searches for the boots?"}], "ideal":
"bathtub"} ```
</details>

---
## [jrcribb/evals](https://github.com/jrcribb/evals)@[8d32b347f0...](https://github.com/jrcribb/evals/commit/8d32b347f05fd2a735ff5d8745a0a4680bdfcce8)
#### Tuesday 2023-11-28 12:23:28 by johny-b

Bluff eval (#1402)

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

bluff

### Eval description

Evaluate how well a model can play (a variant of) the game of bluff,
also known as "liar's dice".

### What makes this a useful eval?

This is a game of deception - you have to deceive your opponent and
understand when you are deceived.
Models performing very well on this eval could also be capable of
deceiving humans in real-life scenarios.

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
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [jrcribb/evals](https://github.com/jrcribb/evals)@[e96b4d3550...](https://github.com/jrcribb/evals/commit/e96b4d35502125e354391044512d899268ade99d)
#### Tuesday 2023-11-28 12:23:28 by Andrew

Fix the OpenAI Version to <=0.28.1  (#1410)

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

[Insert Eval name here]

### Eval description

[Insert a short description of what your eval does here]

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [ ] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [ ] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [ ] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [ ] Check that your data is in `evals/registry/data/{name}`
- [ ] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ ] Ensure you have the right to use the data you submit via this eval

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

- [ ] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [ ] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [ ] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [ ] I have filled out all required fields of this form
- [ ] I have used **Git LFS** for the Eval JSON data
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `mypy`, `black`,
`isort`, `autoflake` and `ruff` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
  INSERT_EVAL_HERE
  ```
</details>

---
## [alphagov/signon](https://github.com/alphagov/signon)@[d448c0d873...](https://github.com/alphagov/signon/commit/d448c0d873720798036c2498f1885e4d11822981)
#### Tuesday 2023-11-28 12:33:57 by James Mead

Extract page for mandating 2SV for a user

Trello: https://trello.com/c/caETStGa

This is a step on the journey to move the edit user page to use the
GOV.UK Design System. The new design calls for separate pages for
different operations on a user and this is the next one.

The `require_2sv` checkbox was previously only displayed on the "edit
user" page (from `app/views/users/_form_fields.html.erb`) when
`User#require_2sv?` was `false` and thus it was only ever possible to
use this checkbox to *mandate* 2SV; it was not possible to use it to
*unset* the `User#require_2sv` attribute.

Unlike in commits like this one [1] where we first split out the new
page and then separatly moved the new page to use the Design System,
here I've created the new page using the Design System in one go,
because there wasn't much markup in the "edit user" page to extract.

The new `app/views/users/two_step_verification_mandations/edit.html.erb`
template is based on other similar pages which we've recently extracted,
e.g. `app/views/users/two_step_verification_resets/edit.html.erb`. I
decided not to include a checkbox on the new page, because as mentioned
above, this page should only ever be needed to *mandate* 2SV.

The new `Users::TwoStepVerificationMandationsController` is closely
based on the relevant bits of code from `UsersController`, even though
some of it is probably overkill in the new context, i.e. the use of
`UserUpdate`. However, I thought it was worth keeping this step as small
as possible. I've hard-coded `user_params` to `{ require_2sv: true }`,
since there's no checkbox in the form.

I'm using `UserPolicy#mandate_2sv?` for the authorization in the new
`Users::TwoStepVerificationRequirementsController`, because that seems
to make the most sense. You could argue that I should also check
`UserPolicy#edit?` & `UserPolicy#update?` like I did in
`Users::OrganisationsController` in this commit [2], but I've gone off
that idea (sorry, @chrisroos!). Instead I've matched what I did in
`Users::TwoStepVerificationResetsController` in this commit [3].

There weren't *any* tests in `UsersControllerTest` for this behaviour,
so I had to write `Users::TwoStepVerificationMandationsControllerTest`
from scratch, but I based it closely on other similar controller tests.
Luckily there was an integration test
(`test/integration/managing_two_step_verification_test.rb`) covering the
behaviour which I've been able to fixup to work with the new UI.

Rather than creating a combinatorial explosion of tests in
`Users::TwoStepVerificationRequirementsControllerTest` relating to
whether a user with all the different roles can edit another user with
all the different roles, I've resorted to stubbing `UserPolicy.new` and
`UserPolicy#mandate_2sv?`. Although this is a bit ugly, since
`UserPolicy` is thoroughly tested in `UserPolicyTest`, it seems like a
pragmatic option.

I'm using the `error_summary` component in combination with identical
code we've used elsewhere on the off-chance there's a validation error,
because the controller action does re-render the form in that case. Note
that in normal operation there are unlikely to be validation errors on
this page, but since it's theoretically possible I thought it was worth
adding the error summary. We might want to consider changing this to
work more like `Users::TwoStepVerificationResetsController` which raises
an exception if there is a validation error. This makes sense
particularly given that the only validation on `User#require_2sv` only
applied on record creation.

[1]: https://github.com/alphagov/signon/commit/899a8a16356ad3b9e3434feaf99f5e5f2bf8a243
[2]: https://github.com/alphagov/signon/commit/bf207efe2769c0ae48102b40bb6df8e4f7ce7770
[3]: https://github.com/alphagov/signon/commit/1baf6856c34f857d71466ec3cb11e974a141175d

---
## [K4rlox/f13babylon](https://github.com/K4rlox/f13babylon)@[9bc0add065...](https://github.com/K4rlox/f13babylon/commit/9bc0add065315cba3de80a2cc1feac5fe08e9fed)
#### Tuesday 2023-11-28 12:59:15 by Stutternov

Locks Legion Combat Roles to Male Only (+ Other Legion Changes) (#176)

## About The Pull Request

Does the following:
- Locks all combat roles to male only - like they used to be prior to
Sunset changes.
- Locks Priestess of Mars to females only, as is in lore.
- Unlocks servant loadout on slave from being female only (real subtle
there guys)

Tl;dr - Females are relegated to slave, camp follower, auxilla,
forgemaster, or priestess. Males are able to be any role baring
priestess.

This is basically already 'rule enforced' so should just be re-added
code wise anyway.

## Why It's Good For The Game

Fits Fallout lore, the servers lore, and keeps the Legion's faction
design at least faithful to their purpose. (Hate telling people this but
- maybe........ legion aren't good people........)

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [ ] You tested this on a local server.
- [ ] This code did not runtime during testing.
- [ ] You documented all of your changes.
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
adds: Locks roles in Legion based off gender restrictions.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [kumahq/kuma-gui](https://github.com/kumahq/kuma-gui)@[4ef8003e2c...](https://github.com/kumahq/kuma-gui/commit/4ef8003e2c7d164ba225a87abe7c243c2db579d1)
#### Tuesday 2023-11-28 13:50:50 by John Cowen

feat(dataplanes): Add ServiceTraffic component (#1807)

This PR adds 2 things:

1. A `ServiceTraffic` component and related sub-components. This is the component only and is not hooked up to any data.
2. In order to be able to build/PR/merge the above component in isolation without adding it to our actual application. I've added a very rough sandbox in our docs that can be seen via `yarn docs:dev` (we can add PR previews at a later date which will be much better)

## ServiceTraffic component

I'm looking for feedback on the component itself, plus its subcomponents. Hopefully it's clear where the data will be plugged into this in a later PR and finally integrated into our application.

## Docs/Component Sandbox

I wanted to start getting this in as I would really like to use this more for building/manually testing/previewing our reusable components. It has the additional benefit of being able to work on, PR and merge components that aren't yet used in our application. Almost like feature flags but instead of feature flagging our in-production application, we just use a completely different application. In the future we should be able to gradually build entire features in isolation using this sandbox application, then just enable them in production when we want to.

As you can see the code here is very much in-progress. I went out of my way not to alter any of our application code just yet, but I think some injection related things will change ever so slightly to allow us to reuse things better.

Lastly I'd be happy to close this PR either way and wait for everything to be integrated, but I wanted to get feedback early on both of the above features and I also wanted to do a final CI check on the sandbox stuff and start thinking about CI integration. Let me know either way. I'd also be happy splitting these features into separate PRs, but really in order to test/experience one you need the other.

---------

Signed-off-by: John Cowen <john.cowen@konghq.com>

---
## [poggers16/GregTechCEu-1.19](https://github.com/poggers16/GregTechCEu-1.19)@[852bb70272...](https://github.com/poggers16/GregTechCEu-1.19/commit/852bb70272ec9040d0dc6d1b695442a43f3969c3)
#### Tuesday 2023-11-28 14:11:23 by screret

Byproduct limiting (#572)

* it doesn't crash but kinda doesn't work either

* Holy shit it works!!!! gonna implement multiblock voiding mode button in separare PR.

* final lil' fixes

* reviews?

---
## [BetaMasaheft/Places](https://github.com/BetaMasaheft/Places)@[feb18d1c70...](https://github.com/BetaMasaheft/Places/commit/feb18d1c70fce79fa35e2495993aeddee5513b16)
#### Tuesday 2023-11-28 15:59:56 by Carsten Hoffmann

New records for places in Tanasee1 (no. 5)

In an addition in Tanasee1, I find a landgrant with a couple of place names. Most of them, I could not find and they sound quiet strange to me. Possibly they are abbreviated or misspelled:
ጸሐፍነ፡ ዘገብረ፡ በዘመኑ፡ ንጉሠ፡ ሰላም፡ <persName ref="PRS4015Fasilada">ፋሲለደስ፡ </persName>
                                        ዘተሰምየ፡ በበፈቃደ፡ እግዚአብሔር፡ ዘወሀበ፡ ጉልታተ፡ ሀገር፡ ለመቅደሰ፡ <placeName ref="LOC4042Kebran">ክብራን፡</placeName>
                                        ገብርኤል፡ <placeName ref="LOC0000">ዳጉስማሃ፡ </placeName>
                                        ወ<placeName ref="LOC7384Hanita">ሐኒታ፡</placeName>
                                        ወ<placeName ref="LOC00000">ወበረተ፡ ማርያም፡</placeName>
                                        ወ<placeName ref="LOC00000">መጣቅር፡ ደረመኒ</placeName>ሃ፡
                                        ወ<placeName ref="LOC0000">ጉልጉልማ፡ መድኃኔ፡ ዓለም፡</placeName> ከመ፡ ይኩኑ፡ ረዳኢሁ፡ ለገብርኤል፡ በንዋይ፡
                                        ወበኩሉ፡ ግብር፡ ለ<placeName ref="LOC00000">ጉናጉለመ፡</placeName>
As far as I understand:
"We have written about the issue in the time of the ruler of peace Fasiladas, who was called (lacuna) to please the Lord, in a way he gave lands of fief to the holy place of Kebrān Gabrəʾel:
Dagusmāhā (possibly the island of Dāgā, but heavily distorted),
Ḥanitā (already known from another addition in the same manuscript),
Wabarata Māryām (perhaps abbreviated for Barakata Māryām = blessing of Mary, possibly the name of a church and surrounding lands),
Maṭāqər Daramani (or: Maṭāqər Yerimani; perhaps an abbreviation for Maṭāqər Dabra Madḫānit = The longing for the mountain of salvation - a rather unusual name for a church)
Gulgulmā Maḫāne ʿAlam (a church with the name Saviour of the world in an area called Gulgulmā)."

---
## [Higgin/tgstation](https://github.com/Higgin/tgstation)@[c00f7d53a3...](https://github.com/Higgin/tgstation/commit/c00f7d53a32801b7afd923f268da30fb2f99bbd5)
#### Tuesday 2023-11-28 16:10:14 by MGOOOOOO

The Inversenning : Superior Healing Medications (#79342)

Introducing new inverse reagents for existing superior healing
medications! This push includes...

**Benzoic Acid** : Inverse of Salicylic Acid. Robust fertilizer that
provides a decent range of benefits for plant life.

**Oxymetholone** : Inverse of Oxandrolone. Anabolic steroid that
promotes the growth of muscle during and after exercise.

**Bamethan** : Inverse of Salbutamol. Blood thinner that drastically
increases the chance of receiving bleeding wounds.

**Pendetide** : Inverse of Pentetic Acid. An unusual bioradioactive drug
that purges basic radiation healing chems. Also increases the severity
of radiation poisoning.

**Hyoscyamine** : Inverse of Atropine. Heals heart and stomach damage,
and slowly removes minor toxin damage.

**Ammoniated Sludge** : Inverse of Ammoniated Mercury. A ghastly looking
mess of mercury by-product which causes bursts of manic hysteria.

**Inreziniver** : Inverse of Rezadone. Makes the user horribly afraid of
all things related to carps.

This is an effort to add more variety to the existing inverse reagent
system within chemistry. Not only should this variety serve to provide
additional options for a Chemist to experiment with, they should also
broaden the possibilities for already existing strategies.

---
## [TJatPBnJ/tgstation](https://github.com/TJatPBnJ/tgstation)@[7fce8cd805...](https://github.com/TJatPBnJ/tgstation/commit/7fce8cd8054cc1d0b048db12d7e9587b42fcdef2)
#### Tuesday 2023-11-28 16:24:36 by san7890

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
## [TJatPBnJ/tgstation](https://github.com/TJatPBnJ/tgstation)@[2562f0997a...](https://github.com/TJatPBnJ/tgstation/commit/2562f0997a73a52c4ada51c7e0d9996fea4ee573)
#### Tuesday 2023-11-28 16:24:36 by MrMelbert

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
## [TJatPBnJ/tgstation](https://github.com/TJatPBnJ/tgstation)@[742971675d...](https://github.com/TJatPBnJ/tgstation/commit/742971675de266aa4ebe671dc5175a5c543d93d7)
#### Tuesday 2023-11-28 16:24:36 by san7890

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
## [HerculesChrysanthos/frontend-cook-hub](https://github.com/HerculesChrysanthos/frontend-cook-hub)@[9252760244...](https://github.com/HerculesChrysanthos/frontend-cook-hub/commit/92527602442b037e653855f1cd5192154f38275a)
#### Tuesday 2023-11-28 16:59:32 by kostassifa

final handling in registration messages maybe i dont know we will see i hate my life so much

---
## [Sonic-Geared/Scarlet-Engine](https://github.com/Sonic-Geared/Scarlet-Engine)@[163a5c642e...](https://github.com/Sonic-Geared/Scarlet-Engine/commit/163a5c642eb6af1acd40aa3d5d4b64e8e87033e5)
#### Tuesday 2023-11-28 17:13:59 by Geared

I swear for God...

if this autobuild doesn't work, i'm gonna make a serious bullshit against every single fucking alive being i know in existence...

---
## [Cellzawy/WATCH-IT-JAVA](https://github.com/Cellzawy/WATCH-IT-JAVA)@[0fc92b4e58...](https://github.com/Cellzawy/WATCH-IT-JAVA/commit/0fc92b4e58e883896057b37759fee0dbeb1651eb)
#### Tuesday 2023-11-28 17:29:40 by Alinist

WE FUCKING DID IT !!!!!!
as we said before....WE ARE FREEEEEEE!!!!!

by ali and ali
and fuck you all

---
## [ARF-SS13/coyote-bayou](https://github.com/ARF-SS13/coyote-bayou)@[a3fdbe5881...](https://github.com/ARF-SS13/coyote-bayou/commit/a3fdbe5881830f0fbc30cb7662f4a8d99e33310d)
#### Tuesday 2023-11-28 17:35:00 by Tk420634

Merge pull request #3945 from Kilmented/master

UPDEN FUCK YOU UP

---
## [NVIDIA/Fuser](https://github.com/NVIDIA/Fuser)@[922fab891f...](https://github.com/NVIDIA/Fuser/commit/922fab891f98f2cedb7fc7f8a408000e9c874309)
#### Tuesday 2023-11-28 18:14:45 by Gao, Xiang

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
## [ahjragaas/binutils-gdb](https://github.com/ahjragaas/binutils-gdb)@[a393b15517...](https://github.com/ahjragaas/binutils-gdb/commit/a393b155174d20d3d120b5012b87c5438ab9e3d4)
#### Tuesday 2023-11-28 18:30:09 by Andrew Burgess

gdb/python: display errors from command completion

This commit makes the gdb.Command.complete methods more verbose when
it comes to error handling.

Previous to this commit if any commands implemented in Python
implemented the complete method, and if there were any errors
encountered when calling that complete method, then GDB would silently
hide the error and continue as if there were no completions.

This makes is difficult to debug any errors encountered when writing
completion methods, and encourages the idea that Python extensions can
be broken, and GDB will just silently work around them.

I don't think this is a good idea.  GDB should encourage extensions to
be written correctly, and robustly, and one way in which GDB can (I
think) support this, is by pointing out when an extension goes wrong.

In this commit I've gone through the Python command completion code,
and added calls to gdbpy_print_stack() or gdbpy_print_stack_or_quit()
in places where we were either clearing the Python error, or, in some
cases, just not handling the error at all.

One thing I have not changed is in cmdpy_completer (py-cmd.c) where we
process the list of completions returned from the Command.complete
method; this routine includes a call to gdbpy_is_string to check a
possible completion is a string, if not the completion is ignored.

I was tempted to remove this check, attempt to complete each result to
a string, and display an error if the conversion fails.  After all,
returning anything but a string is surely a mistake by the extension
author.

However, the docs clearly say that only strings within the returned
list will be considered as completions.  Anything else is ignored.  As
such, and to avoid (what I think is pretty unlikely) breakage of
existing code, I've retained the gdbpy_is_string check.

After the gdbpy_is_string check we call python_string_to_host_string,
if this call fails then I do now print the error, where before we
ignored the error.  I think this is OK; if GDB thinks something is a
string, but still can't convert it to a string, then I think it's OK
to display the error in that case.

Another case which I was a little unsure about was in
cmdpy_completer_helper, and the call to PyObject_CallMethodObjArgs,
which is when we actually call Command.complete.  Previously, if this
call resulted in an exception then we would ignore this and just
pretend there were no completions.

Of all the changes, this is possibly the one with the biggest
potential for breaking existing scripts, but also, is, I think, the
most useful change.  If the user code is wrong in some way, such that
an exception is raised, then previously the user would have no obvious
feedback about this breakage.  Now GDB will print the exception for
them, making it, I think, much easier to debug their extension.  But,
if there is user code in the wild that relies on raising an exception
as a means to indicate there are no completions .... well, that code
is going to break after this commit.  I think we can live with this
though, the exceptions means no completions thing was never documented
behaviour.

I also added a new error() call if the PyObject_CallMethodObjArgs call
raises an exception.  This causes the completion mechanism within GDB
to stop.  Within GDB the completion code is called twice, the first
time to compute the work break characters, and then a second time to
compute the actual completions.

If PyObject_CallMethodObjArgs raises an exception when computing the
word break character, and we print it by calling
gdbpy_print_stack_or_quit(), but then carry on as if
PyObject_CallMethodObjArgs had returns no completions, GDB will
call the Python completion code again, which results in another call
to PyObject_CallMethodObjArgs, which might raise the same exception
again.  This results in the Python exception being printed twice.

By throwing a C++ exception after the failed
PyObject_CallMethodObjArgs call, the completion mechanism is aborted,
and no completions are offered.  But importantly, the Python exception
is only printed once.  I think this gives a much better user
experience.

I've added some tests to cover this case, as I think this is the most
likely case that a user will run into.

Approved-By: Tom Tromey <tom@tromey.com>

---
## [Imaginos16/Shiptest](https://github.com/Imaginos16/Shiptest)@[4d4aa72e33...](https://github.com/Imaginos16/Shiptest/commit/4d4aa72e33bd20077d09d320f07a0a5608298cb2)
#### Tuesday 2023-11-28 18:53:59 by lizardqueenlexi

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
## [elunna/HACKEM-MUCHE](https://github.com/elunna/HACKEM-MUCHE)@[f7689a8d00...](https://github.com/elunna/HACKEM-MUCHE/commit/f7689a8d00a2d132bad790d12bf2af62f97bd87a)
#### Tuesday 2023-11-28 19:01:56 by Erik Lunna

Players cannot put known wands of cancellation or magical bags into bags of holding anymore (from dNetHack).

Once a player has identified these objects, it's pretty universally expected that they will *never* intentionally put them into their bag of holding. So, let's help them out with that.

I think this does some positive things for the game: 1) People won't rage quit and they will be happier. 2) Devs will see players not rage quitting and be happier. 3) Many promising games won't be wasted because of a simple mistake.

I believe there are more interesting challenges for the players to face than this, so it's one I'd like to see put to bed. Keep in mind, that if players are careless with their unidentified equipment, that is entirely on them.

---
## [bonjorno7/TIC-80](https://github.com/bonjorno7/TIC-80)@[c86219f735...](https://github.com/bonjorno7/TIC-80/commit/c86219f73563aefee4f81bceb6b58f957697f069)
#### Tuesday 2023-11-28 19:11:21 by bonjorno7

Implement trim on save

I'm not too experienced with C so this was tough, but I got it working.
It trims spaces at the end of lines, and newlines at the end of the file (except for the last one, if there's space for it).
It also updates the cursor position and selection.

I increment src after the done check so that its value is correct after the loop; not actually using it after the loop in this version but just in case.
That check by the way uses a stored variable because the loop overwrites the buffer, so checking the value of end at the bottom of the loop doesn't work.
I'm using memmove instead of memcpy because the data can overlap, and this is apparently still quite fast.
I don't zero out garbage data after the terminator because it's apparently unnecessary.
After trimming whitespace it calls history and update; hopefully those are the right functions in the right order.

One small note: if your selection was entirely trimmed, you're left with a zero length selection.
I can fix this by detecting if position and selection are equal, and then setting selection to null.
I chose not to do this however, because it's easy to create a zero length selection by hand, and the user might in some cases do so intentionally.
If you want to get rid of zero length selections entirely, that should probably be fixed elsewhere, rather than in this function.

Another note: trimming only happens with Ctrl + S, not with typing save in the console.
Perhaps I should fix this, though I think it has advantages too; I think ideally the trimming should only happen when you can see it happening, which you can't if you're in the console.
Also while writing this code it was nice to be able to undo and save my file without running the trimming code, though I suppose now that the code works properly I won't need it anymore.

---
## [goauthentik/authentik](https://github.com/goauthentik/authentik)@[a3673906c7...](https://github.com/goauthentik/authentik/commit/a3673906c79624888b1a678924c30db7a33944a1)
#### Tuesday 2023-11-28 19:11:46 by Ken Sternberg

web: provide three-tier sidebar with subcategories

This commit implements a three-tier sidebar with subcategories.

The first thing is that we've refactored the Sidebar into a holistic entity; rather than be built in
pieces, it's constructed declaratively from a tree of entries, much in the same way routes are, and
for much the same reason<sup>1</sup>.

The AdminSidebar element only provides the list of entries to show and some of the controls
necessary to show/hide the sidebar.  Because the sidebar requires a rich collection of objects
retrieved from the back-end, to avoid cluttering the AdminSidebar each of those sublists of
TypeCreate have been isolated into their own controllers.

The SidebarTypeController isn't even a strongly reactive controller; all it does is fetch the
TypeCreate collection and notify the client object that the fetch has completed. The client can then
call the `.entries()` method on the controller to get the sub-tree of entries for the TypeCreate
object.

The Sidebar has been slightly (!) refactored so that it's emphatic about what it does: it shows the
brand, nav, and user sections of the sidebar. The styling has been moved to a separate file, the
better to emphasize this.

The SidebarItems file is where all the magic-- and a lot of ugly-- is hidden.

The main purpose of the SidebarItems is to render the tree of entries passed to it.  That's it.  But
it also has to be able to read the URL and highlight which entry is currently being shown by the
router, and it has to be able to open up all the parent objects of the "current" link so that the
user gets a clear sense of where they are navigationally.

Most messy: the `reclick()` function intercepts clicks on anchors and, using the same logic as the
router, decides if the router would *not* handle the navigation event.  If the router would not, it
takes on the responsibility for reaching into the currently visible table, modifying the filter and
triggering a new `.fetch()`.

Somewhere along the way I boyscoutted another `switch` statement or two into lookup expressions.

---

<sup>1</sup>&nbsp; One of the reasons for this is that the Administrator Application's sidebar,
routes, and command palette will all get their data from a single source of truth, and that single
source will be independent of any of those.  This is a step in that direction.

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[63addccfb0...](https://github.com/microsoft/terminal/commit/63addccfb076770604e892c3eddb69f0a05c9379)
#### Tuesday 2023-11-28 19:11:55 by Mike Griese

Make conhost act in VtIo mode earlier in startup (#15298)

We need to act like a ConPTY just a little earlier in startup. My relevant notes start here: https://github.com/microsoft/terminal/issues/15245#issuecomment-1536150388.

Basically, we'd create the first screen buffer with 9001 rows, because it would be created _before_ VtIo would be in a state to say "yes, we're a conpty". Then, if a CLI app emits an entire screenful of text _before_ the terminal has a chance to resize the conpty, then the conpty will explode during `_DoLineFeed`. That method is absolutely not expecting the buffer to get resized (and the old text buffer deallocated).

Instead, this will treat the console as in ConPty mode as soon as `VtIo::Initialize` is called (this is during `ConsoleCreateIoThread`, which is right at the end of `ConsoleEstablishHandoff`, which is before the API server starts to process the client connect message).  THEORETICALLY, `VtIo` could `Initialize` then fail to create objects in `CreateIoHandlers` (which is what we used to treat as the moment that we were in conpty mode). However, if we do fail out of `CreateIoHandlers`, then the console itself will fail to start up, and just die. So I don't think that's needed.

This fixes #15245. I think this is PROBABLY also the solution to #14512, but I'm not gonna explicitly mark closed. We'll loop back on it.

(cherry picked from commit 6ad8cd0a630ab927629841a14d433c3bc19a1509)
Service-Card-Id: 89112504
Service-Version: 1.17

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[ddf1cb7870...](https://github.com/pytorch/pytorch/commit/ddf1cb78705dcf79fe8c8df01f6f18ca4a218c55)
#### Tuesday 2023-11-28 19:33:39 by voznesenskym

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
ghstack dependencies: #113926

---
## [fidesosu/Domain-Redirect](https://github.com/fidesosu/Domain-Redirect)@[51ac554348...](https://github.com/fidesosu/Domain-Redirect/commit/51ac55434805eac1a0c4638f0e843d2b54b3e9e1)
#### Tuesday 2023-11-28 19:39:41 by fides

Update Domain Redirector.user.js

there's a fucking infinite loop shit HOLY FUCK

---
## [AxelRamir/SoftwareEngineeringProject](https://github.com/AxelRamir/SoftwareEngineeringProject)@[e92dc3b49e...](https://github.com/AxelRamir/SoftwareEngineeringProject/commit/e92dc3b49e4eb411624031f958241a2599299d3e)
#### Tuesday 2023-11-28 19:55:15 by Elijah

Team color JLabel

Added a JLabel to GameBoardPanel to show what color you are. The code is wonky but it works, it was a pain in the ass!!!

---
## [indieweb/wiki](https://github.com/indieweb/wiki)@[b94312998a...](https://github.com/indieweb/wiki/commit/b94312998a86d36c9bf1f734252629df083e6aea)
#### Tuesday 2023-11-28 20:00:07 by Loqi.me

[tantek] added "possibly contradictory/doublespeak use of finsta/rinsta terms: 2019-10-15 [https://blog.hubspot.com/marketing/finsta What's a Finsta? We Explain This Confusing Instagram Trend], e.g. quoting then 16-year old (Gen Z) <blockquote>"My real Instagram account is kind of fake -- like, only pictures of my 'best' life,"</blockquote>…<blockquote>"I use my Finsta to share funny, inside jokes with my closest friends. My real Instagram has" to "See Also"

---
## [mosra/magnum-extras](https://github.com/mosra/magnum-extras)@[79571854de...](https://github.com/mosra/magnum-extras/commit/79571854de798fd6dad0efd3b0eece0218c05c05)
#### Tuesday 2023-11-28 20:00:53 by Vladimír Vondruš

Whee: rework BaseLayer and TextLayer style assignment.

Requiring the calling code to have a compile-time-sized struct felt like
a good idea in theory. In practice it's absolutely horrendous tho, as:

 - The calling code then has to ensure matching order between a style
   enum and a style struct, which is extremely hard to maintain without
   a nasty preprocessor magic.
 - Defining a builtin style means either having to define & document a
   struct that glues a LayerStyleCommon instance together with several
   LayerStyleItem instances, which is nasty on its own, and then have to
   *somehow* populate it. Which in a (C++11) constexpr context means
   either using the implicit initializer, again losing any mapping from
   the actual enum values to the order (thus gaining *nothing* from such
   a "named tuple" definition), or having to give up on any constexpr
   use and assign to the named fields in order to ensure at least some
   ordering sanity.
 - It's extremely annoying and / or impossible to extend the style
   definition for custom widgets -- one has to *derive a struct* for
   that, and then somehow copy the original builtin data to its prefix.
 - The error message when the layer style count differs from the actual
   passed data is total garbage. Nobody is interested in how many bytes
   something occupies, they want to know *what is wrong* and the API
   isn't capable of saying or even knowing that.

So now it's instead a setStyle() API taking the LayerStyleCommon
instance and a (contiguous) list of LayerStyleItem. A downside is that
the (GL) implementation then does two GL buffer uploads, alternatively
it could put them together and upload at once (which means a nasty temp
allocation). With Vulkan (and I hope WebGPU) this won't be a problem as
there's a way to submit multiple uploads in a single command, or just
memory-mapping the buffer and doing a copy directly.

Extending a style is then a matter of creating an array that's larger
than the compile-time constant, having the custom style items start from
that constant, and copying the original data to prefix of that array.
Simple.

For the TextLayer this also merges the previous setStyle() and
setStyleFonts() APIs together, because they were always meant to be
called together anyway. It makes the whole usage a lot less janky and
unclear.

---
## [Unordinal/VT2Lib](https://github.com/Unordinal/VT2Lib)@[36bb86d111...](https://github.com/Unordinal/VT2Lib/commit/36bb86d11162a10a6f480600b313390482468d0f)
#### Tuesday 2023-11-28 20:01:40 by Unordinal

Fix Assimp bone extraction.

You ever do something one way and then try and brute force it that way because you can't understand why it won't work... and then come back after hours and days and realize you're just dumb?

Yeah.

Anyway, using the IndexBuffer to index into the VertexBuffers for the weights (like, y'know, every other type of VertexBuffer) so we assign the bones *properly*. Still not 100% on this however, as some bones seem to be missing. Could be due to assigning the current mesh the bones? I'm not entirely certain, or I'd fix it lul.

---
## [bergundy/temporal](https://github.com/bergundy/temporal)@[1be76e3583...](https://github.com/bergundy/temporal/commit/1be76e3583ef01ba9f79503e81fed5b7c9ab389c)
#### Tuesday 2023-11-28 21:46:41 by Tim Deeb-Swihart

Replace gogo/protobuf with google/protobuf (#5032)

**What changed?**

gogo/protobuf has been replaced with Google's official go compiler. 

**Why?**

gogo/protobuf has been deprecated for some time and the community is
moving on, building new tools (like vtproto) atop google's v2 compiler.

**How did you test it?**

`make test`

**Potential risks**

1. The change from embedded gogo-generated-structs to
google-generated-pointers-to-structs created a risk of nil pointer
exceptions. I've fixed all the ones our tests found but it's possible
there are more lurking in the new code.
2. This change may cause our performance to decrease. Certainly
encoding/deconding of proto objects will become slower, but the overuse
of pointers by the google compiler may negatively affect our overall
performance. We'll need to keep an eye on the GC stats
3. This breaks the HTTP API. We will not support [shortand payload
encoding](https://github.com/temporalio/proposals/blob/master/api/http-api.md#payload-formatting)
in this first pass; that will come once this initial work is in testing.

**Breaking changes for developers**

- `*time.Time` in proto structs will now be
[timestamppb.Timestamp](https://pkg.go.dev/google.golang.org/protobuf@v1.31.0/types/known/timestamppb#section-documentation)
- `*time.Duration` will now be
[durationpb.Duration](https://pkg.go.dev/google.golang.org/protobuf/types/known/durationpb)
- V2-generated structs embed locks, so you cannot dereference them. `go
vet` will scream at you about this. If you need a copy, use
`proto.Clone`.
- If the performance of this sucks then I will either update our code
generator to add shallow-clone methods or hand-roll the ones we need
- Proto enums will, when formatted to JSON, now be in
`SCREAMING_SNAKE_CASE` rather than `PascalCase`. We decided (in
discussion with the SDK team) that now was as good a time as any to rip
the bandage off.
- Proto objects, or objects embedding protos, cannot be compared using
`reflect.DeepEqual` or _anything_ that uses it. This includes `testify`
and `mock` equality testers!
- You will need to use the `common/testing/protorequire`,
`common/testing/protoassert`, or `common/testing/protomock` packages
instead. I've implemented proto-compatible matchers and assertions there
for all cases I've encountered
- If you need `reflect.DeepEqual` for any reason you can use
`go.temporal.io/api/temporalproto.DeepEqual` instead

Note that history loading will not be impacted by the JSON changes: I
rewrote history loading to dynamically fix incoming history JSON data
(like all our other sdks); you can find this code in [my fork of our go
API](https://github.com/tdeebswihart/temporal-api-go/blob/master/internal/temporalhistoryv1/load.go)
alongside its tests.

**🚨Sharp Edges Introduced🚨**

Beware `*timestamppb.Timestamp.AsTime()`. If you need to extract a time
value from a proto time (timestamppb) **always** make sure to check
whether it's nil first. When the proto object is `nil` `AsTime()` will
return a non-zero time at the proto epoch: UTC midnight on January 1,
1970.

I've made this mistake multiple times during this transition and each
time it's been a pain to debug

**Is hotfix candidate?**

No.

---
## [shiptest-ss13/Shiptest](https://github.com/shiptest-ss13/Shiptest)@[caa19d2a6f...](https://github.com/shiptest-ss13/Shiptest/commit/caa19d2a6f8014c2d34663c7c63685921bc0218a)
#### Tuesday 2023-11-28 22:48:17 by GenericDM

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
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[574959a482...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/574959a482252cee418c6ea9da1c799d57c2e4be)
#### Tuesday 2023-11-28 22:54:25 by Ron Nazarov

Allow specifying figurine/statue gender and show more info in dump

Statue/figurine gender changes:
-You can now specify the gender of figurines/statues in wishes, as
 well as the gender of pets summoned with candles of invocation.
--"male/female figurine/statue of an X" and
  "male/female X statue/figurine" both work, but
  "statue/figurine of a male/female X" does not
---NetHack 3.7 fixes this but its wish parser differs so I can't just
   copy from it.  3.7 also supports specifying gender of corpses but
   I don't know if dNetHack even stores that, and, if so, where.
-There are now MM_MALE/MM_FEMALE makemon flags.  These are required
 for gendered figurines to have the same starting inventory:
 previously gender was set after makemon so they would have the wrong
 starting inventory, but this wasn't an issue in practice because they
 were unobtainable outside of wizmode.  This isn't an issue for
 statues because they don't get starting inventory.

More info in enlightenment and end-of-game dump:
-uacinc is now shown, and exact uacinc and protection are always
 shown: the player always knows their own AC/DR so there is no reason
 to hide them.
--Study is also always shown for the same reason.
-Madnesses are now always shown in the end-of-game dump, even if you
 had clear thoughts or 100 sanity.
-Old wizmode spirit count is removed.  It's redundant.
-Inherited artifact is shown in end-of-game dump.
-Information that was previously wizmode-only is shown in end-of-game
 dump.  There's no reason to hide information in the end-of-game dump.
--Exact alignment record, alignment max, sins, various keter counts,
  quest stag/leader backstab status.
---Should this even be restricted to wizmode/final only?

Other changes:
-Wishing for "amulet versus evil eyes" now works, along with several
 alternate spellings.

---
## [QSAR-UBC/pennylane_qutrit_mixed](https://github.com/QSAR-UBC/pennylane_qutrit_mixed)@[47e74e16d0...](https://github.com/QSAR-UBC/pennylane_qutrit_mixed/commit/47e74e16d0fb27aedc5ffab69aefaf5188115038)
#### Tuesday 2023-11-28 23:08:32 by Matthew Silverman

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
## [JusticeAdvoKate/JusticeAdvoKate](https://github.com/JusticeAdvoKate/JusticeAdvoKate)@[20d873d7a6...](https://github.com/JusticeAdvoKate/JusticeAdvoKate/commit/20d873d7a65dafd15d8807355c1568768f2ef6d0)
#### Tuesday 2023-11-28 23:09:14 by JusticeAdvoKate

Create FUNDING.yml

I have been informally educating myself for three years on most every aspect of law- mainly [Ohio] state and federal. I'm cognitively disabled by the Marine Corps base Camp Lejeune toxic water scandal. I'm a victim of gang stalking at the local and state govt level and a fugitive from injustice at this time, but I'm determined to beat the pants off of the so-called "JUSTICE" system - I already forced the court to provide me a remote hearing and got one felony warrant recalled without having to turn myself in. I'm a firm believer in Our human rights being impossible to remove and nOW I have gained the knowledge of enough of the law to force the powers that be to hear meOW! (8 I'm even a homeless veteran - almost three years nOW! I've mastered the art of legal research and I love to help others! I have two pretty incredible app ideas with huge potential to be both lucrative and impactful AF for most ppL actually. Who wants to go down in history as someone who actually assisted me in my endeavors‽ I'm already beginning to strike back at the government representatives that have criminally me. Wilfully depriving someone in the US of their LEGAL RIGHTS under color of law, or government, is a misdemeanor of the 1st degree. If the victim is a member of a vulnerable, or protected, class the crime is at least a felony five (or the lowest felony degree). And if two or more colluded to willfully deprive someone in the United States of one or more of their legal rights under color of law the crime is much more serious! I'm grateful for anything anyone can do to help me out with this fight. I'm willing to die for actual JUSTICE. Steve Jobs said it best – "[Those] "crazy enough to think that they can change the world are the ones who dO!" (8

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[7f2ded4fc7...](https://github.com/Buildstarted/linksfordevs/commit/7f2ded4fc7fd996f3c4b1c853a28656a28124692)
#### Tuesday 2023-11-28 23:13:21 by Ben Dornis

Updating: 11/28/2023 10:00:00 PM

 1. Added: GitHub - fempire/women-tech-speakers-organizers: A list of women tech speakers & organizers. Add yourself or others by submitting a PR! PS if you do add someone, make sure to tell them! :) #fempire
    (https://github.com/fempire/women-tech-speakers-organizers)
 2. Added: .NET 8 and C# 12 — Experimental Attribute
    (https://henriquesd.medium.com/net-8-and-c-12-experimental-attribute-c895d66bba4e)
 3. Added: Goodbye DevRel… (for now)
    (https://spinscale.de/posts/2023-11-28-goodbye-devrel.html)
 4. Added: Cloud translation is more expensive than I thought
    (https://hiandrewquinn.github.io/til-site/posts/selkouutiset-archive-now-supports-77-languages/)
 5. Added: "Position Strings" for Collaborative Lists and Text
    (https://mattweidner.com/2023/04/13/position-strings.html)
 6. Added: Five Learnings from Five Years as a First-Time Founder
    (https://www.lureinperera.com/post/five-learnings-from-five-years-as-a-first-time-founder)
 7. Added: Deploy your CloudKit-backed SwiftData entities to production
    (https://www.leojkwan.com/swiftdata-cloudkit-deploy-schema-changes/)
 8. Added: A year working with HTML Web Components
    (https://hawkticehurst.com/writing/a-year-working-with-html-web-components/)
 9. Added: Consider Writing Documentation for Your House
    (https://luke.hsiao.dev/blog/housing-documentation/)
10. Added: The Ideal Social Network
    (https://www.zaxis.page/p/social-network)
11. Added: What is going on with Mars Sample Return?
    (https://caseyhandmer.wordpress.com/2023/11/26/what-is-going-on-with-mars-sample-return/)
12. Added: Trying simple tree-search techniques for LLM token sampling
    (https://andys.page/posts/llm_sampling_strategies/)
13. Added: Dependency rejection
    (https://amontalenti.com/2023/11/25/dependency-rejection)
14. Added: Nextty: a radically collaborative computing environment
    (https://offbyone.us/posts/nextty-idea/)
15. Added: My techno-optimism
    (https://vitalik.ca/general/2023/11/27/techno_optimism.html)
16. Added: Matrix vs. XMPP | Luke's Webpage
    (https://lukesmith.xyz/articles/matrix-vs-xmpp/)
17. Added: construct0, the first steps of an organisation with great aspirations.
    (https://blog.benjaminvr.net/2023/11/construct0-first-steps-of-organisation.html)
18. Added: Rust: Memory Management
    (https://priver.dev/blog/rust/memory-management/)
19. Added: ML.NET 3.0 Boosts Deep Learning, Data Processing for .NET-Based AI Apps -- Visual Studio Magazine
    (https://visualstudiomagazine.com/articles/2023/11/28/ml-net-3-0.aspx)
20. Added: Bazel market growth, year over year
    (https://blog.aspect.dev/bazel-market-2023)
21. Added: The quality of your life is the quality of the people you get to know: Illuminating the David Brooks way
    (https://jakeseliger.com/2023/11/28/the-quality-of-your-life-is-the-quality-of-the-people-you-get-to-know-illuminating-the-david-brooks-way/)
22. Added: Mercure, Braid, PREP… news about subscribing to HTTP resource updates - Kévin Dunglas
    (https://dunglas.dev/2023/11/mercure-braid-prep-news-about-subscribing-to-http-resource-updates/)
23. Added: Yusuf Aytas - Talent Sourcing Journey
    (https://www.yusufaytas.com/talent-sourcing-journey/)
24. Added: Should this be an A/B Test?
    (https://alexeymk.com/2023/11/26/should-this-be-an-ab-test)
25. Added: My Personal Data Backup Pipeline – Justin Paulin
    (https://justinpaulin.com/2023/11/27/my-personal-data-backup-pipeline/)
26. Added: My Ego Is My Enemy. Your Ego Is Your Enemy.
    (https://preslav.me/2023/10/06/my-ego-is-my-enemy-your-ego-is-your-enemy/)
27. Added: How we fixed my SEO | johnnyreilly
    (https://johnnyreilly.com/how-we-fixed-my-seo)
28. Added: Nighttime Time Lapse Photography with AllSky
    (https://johnjonesfour.com/2023/12/01/nighttime-time-lapse-photography-with-allsky/)
29. Added: Building a Critter Stack Application: Event Storming
    (https://jeremydmiller.com/2023/11/28/building-a-critter-stack-application-event-storming/)
30. Added: Running SQL Queries on Org Tables
    (http://yummymelon.com/devnull/running-sql-queries-on-org-tables.html)
31. Added: Ryle on microphysics and the everyday world
    (http://edwardfeser.blogspot.com/2023/11/ryle-on-microphysics-and-everyday-world.html)
32. Added: Embark: Dynamic documents for making plans
    (https://www.inkandswitch.com/embark/)
33. Added: RAG Pipelines from scratch
    (https://www.zansara.dev/posts/2023-10-27-haystack-series-rag/)
34. Added: The Village Effect of the Greater Web
    (https://www.fromjason.xyz/p/notebook/the-village-effect-of-the-greater-web/)
35. Added: How to Do a Competitive Analysis for Startups?
    (https://frederik.today/blog/how-to-do-a-competitive-analysis-for-startups)

Generation took: 00:13:05.2813355

---
## [Durss/Twitchat](https://github.com/Durss/Twitchat)@[5cbb50f692...](https://github.com/Durss/Twitchat/commit/5cbb50f692bc1daa9584f867428dda24b1d4330f)
#### Tuesday 2023-11-28 23:45:29 by Durss

Handling un/ban and message delete
FUCK YOUUUUUUU GOOGLE WITH YOUR SHIT API 🤬🤬🤬🤬🤬🤬

---

