## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-02](docs/good-messages/2023/2023-12-02.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 5,861,640 were push events containing 6,573,737 commit messages that amount to 217,102,527 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 72 messages:


## [minetest-game/default](https://github.com/minetest-game/default)@[bc40ea00fa...](https://github.com/minetest-game/default/commit/bc40ea00fa4c9f88c98ce23b1095c42da44ec61c)
#### Saturday 2023-12-02 00:24:32 by Yaya - Nurul Azeera Hidayah @ Muhammad Nur Hidayat Yasuyoshi

Update Malay translations
1. Added missing translation to the following files:
  beds.ms.tr, creative.ms.tr, default.ms.tr, farming.ms.tr,
  fire.ms.tr, sethome.ms.tr
2. Changes some translation as per following:
  a. beds.ms.tr
    - Leave Bed changed from Bangun (wake up) to Tinggalkan Katil
      (leave bed, in literal sense) just because the button would
      be interpreted by some people as 'wake up on next morning'
      (ie. skipping night) instead of 'wake up interrupting current
      sleep progress' which is the intended meaning.
  b. boats.ms.tr
    - Boat cruise mode changed from Mod bot layar makan angin to
      Mod jelajah bot, the original translation is more like direct
      translation, and this has been changed to more natural one
      to make sure player know that the mode is a cruise control.
    - Reset changed from Set semula to Tetap semula, this is for
      standardizing with existing term used in various places.
  c. default.ms.tr
    - Page \@1 of \@2 changed from the short form to the long form.
    - Mese Crystal Fragment had missing word 'Kristal' re-added.
  d. dye.ms.tr
    - Dark Grey changed from Kelabu Gelap to Kelabu Tua to make it
      standardized with the colour name elsewhere.
    - Dark Green changed from Hijau Gelap to Hijau Tua to make it
      standardized with the colour name elsewhere.
    - Magenta changed from Merah Lembayung to Magenta, because the
      colour Merah Lembayung is now used to refer to purplish red
      and no longer equal to magenta, the loanword is used instead.
  e. game_commands.ms.tr
    - respawn changed from lahir semula (reborn) to jelma semula
      (reappear), this is to make it consistent with the language
      used in multiple other games that had similar respawning
      system, and avoiding the religious context of life that is
      implied by the use of previous translation.
    - spawnpoint changed from titik permulaan (starting point) to
      titik jelma ((re)appear point), see previous point.
  f. tnt.ms.tr
    - Gun Powder changed from Serbuk Senjata Api (firearms powder)
      to Serbuk Letupan (explosion powder) because that is the
      proper translation, the latter is still the term used even
      when talking about actual firearm, the former didn't exist
  g. vessels.ms.tr
    - item changed from barang (thing) to item, this is mainly
      because some of the 'item' that could be stored are not
      some solid 'thing' where the word barang could be used for,
      so using the word item here keep it neutral.
  h. wool.ms.tr
    - Dark Grey changed from Kelabu Gelap to Kelabu Tua to make it
      standardized with the colour name elsewhere.
    - Dark Green changed from Hijau Gelap to Hijau Tua to make it
      standardized with the colour name elsewhere.
    - Magenta changed from Merah Lembayung to Magenta, because the
      colour Merah Lembayung is now used to refer to purplish red
      and no longer equal to magenta, the loanword is used instead.

---
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[2011c229f9...](https://github.com/silencer-pl/cmss13/commit/2011c229f9a37de8fa67a74d8e40974515724cde)
#### Saturday 2023-12-02 00:27:01 by stalkerino

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
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[f367771f57...](https://github.com/silencer-pl/cmss13/commit/f367771f5799b87257d92cb79db71bcd85b62f75)
#### Saturday 2023-12-02 00:27:01 by Birdtalon

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
## [silencer-pl/cmss13](https://github.com/silencer-pl/cmss13)@[a955791561...](https://github.com/silencer-pl/cmss13/commit/a955791561d5aeab0ff0640923fe1192ad377830)
#### Saturday 2023-12-02 00:27:01 by fira

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
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[caa19d2a6f...](https://github.com/Latentish/Shiptest/commit/caa19d2a6f8014c2d34663c7c63685921bc0218a)
#### Saturday 2023-12-02 01:04:55 by GenericDM

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
## [f13babylon/f13babylon](https://github.com/f13babylon/f13babylon)@[e208ee981e...](https://github.com/f13babylon/f13babylon/commit/e208ee981e86227c2a19b6ae4e35f489be0b0de3)
#### Saturday 2023-12-02 01:43:53 by SM45H

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
## [atteria/Shiptest](https://github.com/atteria/Shiptest)@[c21670412d...](https://github.com/atteria/Shiptest/commit/c21670412dff10f4a3a1b1ab1e72f53294581d25)
#### Saturday 2023-12-02 01:56:21 by Bjarl

New Ruin: The Beach Town (#1572)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds a new beach ruin, the abandoned beachside town
![2022 10 10-18 20
10](https://user-images.githubusercontent.com/94164348/194977185-0f35d08e-64c1-459d-94b2-ec6b66137753.png)
![2022 10 10-18 20
00](https://user-images.githubusercontent.com/94164348/194977192-0b93346e-cea0-4fb2-8b66-5ae7319ec3f1.png)

![dreamseeker_Ht2YcvyQbH](https://user-images.githubusercontent.com/94164348/194977254-d0b25aba-ec6b-4e8b-bad5-949a9961cf07.png)

![dreamseeker_KAB6kPSLrP](https://user-images.githubusercontent.com/94164348/194977259-561f8d97-962e-4545-a4b7-1637ad1a7156.png)

![dreamseeker_8Xe7Cuq6NH](https://user-images.githubusercontent.com/94164348/194977262-fb125315-2508-4022-9eda-5ed5078442c9.png)

![dreamseeker_SKJXeK9SOt](https://user-images.githubusercontent.com/94164348/194977268-b4efcd99-0896-4209-8b83-c61c086bda65.png)

![dreamseeker_6Ak0bNoVe5](https://user-images.githubusercontent.com/94164348/194977270-367aaf92-5d6d-4cd8-9827-eba99ec92080.png)

The town is an mostly empty place formerly devoted to tourism and the
beloved art of "chilling out". Facets of the life of its inhabitants
before their disappearance included drinking, grilling, and swimming off
the coast of their fairly large beach. Many interesting things happened
on the boardwalk, and a landing pad was present to allow for small ships
to dock inside the town.

The loot list is sparse here. I intend for this to mostly be a setpiece
for roleplay instead of a loot pinata. There's a good selection of
hydroponics seeds and gear, 2 full bar kits, basic kitchen equipment, an
autolathe, a few PDAs, a lotta wood, and a jukebox. Also donuts.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] Ruin spawns, nothing is out of whack that shouldn't be.

## Why It's Good For The Game
Continues the trend of making planets more good by adding more content
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: An oddly empty town has been spotted on beach planets in the area.
Check it out spacers.
add: Random donut spawners, never eat the same donut two days in a row!

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
## [atteria/Shiptest](https://github.com/atteria/Shiptest)@[babf89eb74...](https://github.com/atteria/Shiptest/commit/babf89eb746741ba4f33f686b0c4750fe68e1603)
#### Saturday 2023-12-02 01:56:21 by The-Moon-Itself

SubShips attempt 2 (#1627)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Accidentally destroyed my old PR for this, #1573, by completely botching
a merge from master to the point that it was easier to make a whole new
fork than try to save it, so here we are again. Here's the original
description:

Ports the parts of beestation/beestation-hornet#7152 that adds the
framework for ships to land on top of each other and not break
everything. A ship can only land on another ship if there's an open
docking port on the mothership that's large enough for the subship.
Here's a video of it in action on a modified dwayne-class:


https://user-images.githubusercontent.com/51838176/195471361-f9f0d145-d7c9-480e-ad4a-d18705f2590f.mp4

This system should be able to handle just about any orientation of ships
on top of each other, such as ships landed across areas, multiple ships
landed on a single ship, a single ship landed on multiple ships, a ship
that is only partially landed on another ship, a ship that is partially
landed on a ship that's partially landed on another ship, and so on.
Just make sure that you never try to land a ship on itself.

Something to note for this is that ships remember what's underneath them
via baseturfs, and there's a hardcoded check that will cause errors if a
baseturf list grows over 10 entries long. Because ship turfs have
typically 1-3 baseturfs, after about 3 ships stacked on top of each
other things will start to break.

You can also make maps with subships on them, to do this, follow these
steps:
1. make the subship as if it were a regular ship in its own map file
2. create a new /datum/map_template/shuttle subtype that points to your
subship map, these datums can be found in code/datums/shuttle.dm
3. On your main ship, place "subship dock" landmark in turf where you
want the bottomleft corner of the subship's bounding box to be, you can
also use the offset_x and offset_y vars on the landmark to offset this
corner if you need to place the landmark somewhere else.
4. Set the "subship_template" var on the landmark to the path of your
subship's map_template subtype
5. Optionally change the dir on the landmark to rotate the subship. for
reference, NORTH is no rotation, EAST is a 90 degree clockwise rotation,
etc.

You can put the stationary docking port anywhere on your map, as long as
it's on the ship. You can have its bounding box hang off the side of
your ship, but please try to keep the entirety of its bounding box
within the bounding box of map file, otherwise subships landing on your
main ship might accidentally clip through structures nearby your
mainship, including virtual z level borders.
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
Subships allow for many more creative designs and interesting dynamics
between and within ships, especially when a crew may need or want to
split its attention between multiple locations at the same time, or to
make interactions between ships easier when you just need to land a
smaller vessel inside of the other, cutting out the need to travel
through space turfs to get between two ships.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Subships are now possible
code: Lots of large changes to ship code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[ddf1cb7870...](https://github.com/pytorch/pytorch/commit/ddf1cb78705dcf79fe8c8df01f6f18ca4a218c55)
#### Saturday 2023-12-02 02:09:55 by voznesenskym

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
## [Stutternov/f13tbd](https://github.com/Stutternov/f13tbd)@[ec2004b453...](https://github.com/Stutternov/f13tbd/commit/ec2004b453a5da2b81513777b420a23a845825e3)
#### Saturday 2023-12-02 02:15:49 by Stutternov

Logistics Officer Buff!!!! (Fuck you, leftover Yellowstone change) (#280)

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

Tl;dr - Took the explosive granter off the construction loadout of CE
(why did they have it, they already had the one with C4 with that
trait.......... leftover Yellowstone change) and gave it instead to the
Logistics Officer since they realistically should have it as they do gun
crafting.

Also - it makes it so LO's can make mortar rounds now. Also-also, took
away the X4 off CE since it's strong. Gave them 2 C4 instead.

## Why It's Good For The Game

LO buff omg

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
removes: Removed explosive crafting and BP off of CE construction
loadout.
removes: Removed X4 off of CE explosive loadout option, replaced it with
C4
add: Added explosive perk book to LO so they can craft mortars,
grenades, and be useful. (I will buff them more soon so NCR has to use
them more.)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [lolman360/f13tbd](https://github.com/lolman360/f13tbd)@[3c052bcd6d...](https://github.com/lolman360/f13tbd/commit/3c052bcd6d3ff02680c3fe1f15151549154eb162)
#### Saturday 2023-12-02 02:19:30 by Mazzinsanity

Main Fallout13 Medicine Rework (#113)

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
This PR aims to bring a number of changes to the way the main Fallout13
medicines function.

Stims remain the vanilla videogame healing item they were, stronger than
tribal medicine at healing brute and burn damage, but lacking in
specialization. On the other hand, tribal medicine has been given a new
breath of life in the form of excelling in certain damage types and
increased healing from wounds.

Activation delays for certain healing items have been changed:
- Hydra/Med-X/Psycho/Turbo - 1 second on yourself / 3 seconds on others
- All forms of gauze/sutures/mesh/ointment - 3 seconds for yourself / 1
second on others

Using the stimpak as a base, here are the healing rates for brute/burn
healing for the healing items:
1. Super stimpak - 225% of base stimpak strength
2. Imitation super stimpak - 188% of base stimpak strength (75% of super
stimpak strength)
3. Bitter drink -180% of base stimpak strength for tribals / 133% for
non-tribals
4. Healing poultice - 115% of base stimpak strength for tribals / 87.5%
for non-tribals
5. Imitation stimpak - 75% of base stimpak strength
6. Healing powder - 75% of base stimpak strength for tribals / 55% for
non-tribals

All medicine now heals burn damage at 75% of its healing power for brute
damage.

Powder/poultice/bitters/hydra will not heal when any stimpak fluid
variant is in the system. Stimpak fluid will not heal when
powder/poultice/bitters are the system.

Only one medicine is able to heal at a time. This medicine must be the
weakest one currently in the system:
- For example, if super stim fluid is present in the body, and regular
stim fluid is introduced, then the super stim fluid will stop healing,
while the regular stim fluid heals.
- If imitation stim fluid is added, then regular stim fluid stops
healing, and only imitation stim fluid can heal.
- If at any point powder/poultice/bitters are added, no medicine will
heal.
- The same logic follows for powder/poultice/bitters.

All stimpaks have lost the ability to additionally heal bodyparts with
each wound applied to that bodypart. The logic behind this property has
been reworked and moved to tribal medicine.

All stimpaks have retained their ability to clot active pierce/slash
wounds, reducing their bleed rates.

All medicine has lost its crit stabilizing properties.

Bitter drink no longer heals radiation and has reduced toxin and oxyloss
healing rates.

Healing poultice now excels at healing radiation and toxin damage, as
strong as the super stimpak brute healing rate. Healing powder now
excels at healing oxyloss damage, as stong as the super stimpak brute
healing rate.

The overdose effects for all main healing medicines have had their
damage values tweaked and additional drawbacks added.

Using stims as Legion now causes serious side-effects, including
vomiting, confusion, dizzyness and jitteriness. Using
Med-X/Psycho/Buffout/Jet/Turbo as Legion/NCR/BoS/Enclave now also causes
these side-ffects. As such, Psycho and Turbo have been removed from
Enclave loadouts.

2 new negative quirks are now available for selection: Stim Intolerance
and Straight Edge:
- Stim Intolerance makes you vomit, causes dizziness, jitteriness and
confusion whenever any variant of stim fluid enters your body.
- Straight Edge makes you have the same effects but with Fallout chems
like Psycho/Med-X etc.

New positive quirk available for selection: Herbal Affinity:
- Grants bonus healing from tribal medicine and removes the negative
side-effects

Roles that start with these quirks already allocated to them
(NCR/Legion/BoS/Enclave) cannot select these quirks for free points.

Small miscellaneous tweaks and fixes, such as crafting time changes for
medicine, are present as well.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
The current roster of Fallout13 medicine is somewhat unbalanced and
needs a little love. This aims to do that by making superstims act as
vanilla jack-of-all-trades healing items, while making the tribal
medicines specialize in certain damage types to fill the gaps left by
their inability to use chem machines while also making them grow
stronger as the user gains more wounds, taking into account the low
wound armor and hit-and-run, all-or-nothing gameplay that Tribal and
Legion roles have.

The side-effects changes for Med-X/Psycho/Turbo/Buffout were made to
counteract powergaming and circumvent factions breaking their lore in
order to gain an upper hand in a fight.
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
add: Added side-effects for the 4 major factions upon Fallout chem use
add: Added side-effects for Legion upon stim use
add: Added 2 new negative quirks - Stim Intolerance and Straight Edge
tweak: Tweaked medicine crafting times
tweak: Tweaked time delays on medicine application
balance: Rebalanced the main Fallout13 healing chemicals
fix: Fixed incorrect poultice x50 batch crafting requirements
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Yawet330 <65188584+Yawet330@users.noreply.github.com>

---
## [f13babylon/f13babylon](https://github.com/f13babylon/f13babylon)@[893e0e151c...](https://github.com/f13babylon/f13babylon/commit/893e0e151c05648fd712f75e24520fc77354ed39)
#### Saturday 2023-12-02 02:20:40 by lolman360

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
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[2e0597d055...](https://github.com/san7890/bruhstation/commit/2e0597d055fc105037a904355726139434f36b3a)
#### Saturday 2023-12-02 02:51:07 by Vekter

Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun (#80030)

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

---
## [tiluuta/LAspots](https://github.com/tiluuta/LAspots)@[4d01fd6a7d...](https://github.com/tiluuta/LAspots/commit/4d01fd6a7d9fdf55c84bc9ef1c5bb25ceb48e707)
#### Saturday 2023-12-02 03:00:18 by Khalil Mayden

randomize shit

fucking hell this is SO FUCKING ANNOYING AHHHH WHY IS THERE DETAILS ERROR NOW

---
## [XaineDev/FarmHelper](https://github.com/XaineDev/FarmHelper)@[e4b3fb3d3e...](https://github.com/XaineDev/FarmHelper/commit/e4b3fb3d3ef60431ed7557a7052436e5060d8a98)
#### Saturday 2023-12-02 04:18:17 by xai

fuck you we changing a minor version instead of a revision for dis shid

---
## [DaCoolBoss/tgstation](https://github.com/DaCoolBoss/tgstation)@[c9d2c940d8...](https://github.com/DaCoolBoss/tgstation/commit/c9d2c940d87f5205bdf882280af074b132e1af6c)
#### Saturday 2023-12-02 04:31:18 by Vekter

Ports feral cats and feral cat grenades from Hippie (#80031)

## About The Pull Request
Feral Cats are just a hostile variant of cats that will fuck you up if
they see you. They are added solely for the sake of feral cat grenades -
a new, interesting, and fuzzy way to get out of a jam or just wreak
havoc around you. Each one costs 5 TC and spawns 5 really pissed off
cats to chase down assistants in the hallway.

They don't currently ignore traitors or the person who threw them - I
haven't worked out how to do that with our faction system (Hippie gave
them the syndicate faction but traitors don't get that on our codebase).
If anyone wants to contribute or help me suss that out it'll be cool,
otherwise just don't be around if there's nobody else for them to maul.

## Why It's Good For The Game
They're funny.

## Changelog
:cl: Vekter
add: Added a new hostile variant of cats, "feral cats".
add: Added a new traitor item, "feral cat grenades". For 5 TC, you too
can throw a grenade at someone and make five cats maul them to death.
/:cl:

---
## [XaineDev/FarmHelper](https://github.com/XaineDev/FarmHelper)@[786ce5a597...](https://github.com/XaineDev/FarmHelper/commit/786ce5a597275565cae7861225795ac65eebdf57)
#### Saturday 2023-12-02 05:45:35 by xai

fuck you for this bug i hate you i was so confused

---
## [tdib/advent_of_code](https://github.com/tdib/advent_of_code)@[c4d5d21cbb...](https://github.com/tdib/advent_of_code/commit/c4d5d21cbb412b1b819b840198d737b21c6dd566)
#### Saturday 2023-12-02 05:55:29 by Dib

Update README.md

This change has been on my mind for quite some time, and I think it's about time I pulled the trigger and did it. I've been really nervous about doing this so please don't shut me down here. I want you to truly consider the impact this could make on society, and why it could benefit you and your family. Skibidi toilet is something that has impacted and influenced not only me, but my family and friends, and the children of our generation. These children will grow into young adults having been influenced by their childhood. Just imagine if they see this while they are young, they have their whole future ahead of them!

In conclusion, I propose these changes for the betterment of society, and I kindly ask that you consider them.

If you'd like to discuss further, please reach out to me on telegram or whatsapp.

Thank you.

---
## [vesk4000/advent-of-code-2023](https://github.com/vesk4000/advent-of-code-2023)@[dd9d15e720...](https://github.com/vesk4000/advent-of-code-2023/commit/dd9d15e7200199aacd412ca496d6d8baae4be6ab)
#### Saturday 2023-12-02 06:07:35 by vesk4000

Day 2, quite a bit easier than Day 1. Part 2 especially, was absolutely trivial. Just a bunch of string splitting really. Wonder if it can be done better with the some more clever parsing... Anyways, I'm happy, Rust didn't cause me much trouble today. However, damn... does it have to be so verbose.

---
## [Coconutat/android_kernel_xiaomi_sdm845_byd_exp](https://github.com/Coconutat/android_kernel_xiaomi_sdm845_byd_exp)@[1d34babbb5...](https://github.com/Coconutat/android_kernel_xiaomi_sdm845_byd_exp/commit/1d34babbb5f901e4b967fd977686a86ef3b7425a)
#### Saturday 2023-12-02 06:58:01 by Douglas Anderson

serial: core: Allow processing sysrq at port unlock time

[ Upstream commit d6e1935819db0c91ce4a5af82466f3ab50d17346 ]

Right now serial drivers process sysrq keys deep in their character
receiving code.  This means that they've already grabbed their
port->lock spinlock.  This can end up getting in the way if we've go
to do serial stuff (especially kgdb) in response to the sysrq.

Serial drivers have various hacks in them to handle this.  Looking at
'8250_port.c' you can see that the console_write() skips locking if
we're in the sysrq handler.  Looking at 'msm_serial.c' you can see
that the port lock is dropped around uart_handle_sysrq_char().

It turns out that these hacks aren't exactly perfect.  If you have
lockdep turned on and use something like the 8250_port hack you'll get
a splat that looks like:

  WARNING: possible circular locking dependency detected
  [...] is trying to acquire lock:
  ... (console_owner){-.-.}, at: console_unlock+0x2e0/0x5e4

  but task is already holding lock:
  ... (&port_lock_key){-.-.}, at: serial8250_handle_irq+0x30/0xe4

  which lock already depends on the new lock.

  the existing dependency chain (in reverse order) is:

  -> #1 (&port_lock_key){-.-.}:
         _raw_spin_lock_irqsave+0x58/0x70
         serial8250_console_write+0xa8/0x250
         univ8250_console_write+0x40/0x4c
         console_unlock+0x528/0x5e4
         register_console+0x2c4/0x3b0
         uart_add_one_port+0x350/0x478
         serial8250_register_8250_port+0x350/0x3a8
         dw8250_probe+0x67c/0x754
         platform_drv_probe+0x58/0xa4
         really_probe+0x150/0x294
         driver_probe_device+0xac/0xe8
         __driver_attach+0x98/0xd0
         bus_for_each_dev+0x84/0xc8
         driver_attach+0x2c/0x34
         bus_add_driver+0xf0/0x1ec
         driver_register+0xb4/0x100
         __platform_driver_register+0x60/0x6c
         dw8250_platform_driver_init+0x20/0x28
	 ...

  -> #0 (console_owner){-.-.}:
         lock_acquire+0x1e8/0x214
         console_unlock+0x35c/0x5e4
         vprintk_emit+0x230/0x274
         vprintk_default+0x7c/0x84
         vprintk_func+0x190/0x1bc
         printk+0x80/0xa0
         __handle_sysrq+0x104/0x21c
         handle_sysrq+0x30/0x3c
         serial8250_read_char+0x15c/0x18c
         serial8250_rx_chars+0x34/0x74
         serial8250_handle_irq+0x9c/0xe4
         dw8250_handle_irq+0x98/0xcc
         serial8250_interrupt+0x50/0xe8
         ...

  other info that might help us debug this:

   Possible unsafe locking scenario:

         CPU0                    CPU1
         ----                    ----
    lock(&port_lock_key);
                                 lock(console_owner);
                                 lock(&port_lock_key);
    lock(console_owner);

   *** DEADLOCK ***

The hack used in 'msm_serial.c' doesn't cause the above splats but it
seems a bit ugly to unlock / lock our spinlock deep in our irq
handler.

It seems like we could defer processing the sysrq until the end of the
interrupt handler right after we've unlocked the port.  With this
scheme if a whole batch of sysrq characters comes in one irq then we
won't handle them all, but that seems like it should be a fine
compromise.

Signed-off-by: Douglas Anderson <dianders@chromium.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [iithundersnake/ATLA-restored](https://github.com/iithundersnake/ATLA-restored)@[ba162adace...](https://github.com/iithundersnake/ATLA-restored/commit/ba162adace3bb96f77c8d92d1d12eb5aa4bbf50a)
#### Saturday 2023-12-02 07:08:02 by Stocky Kruegar

description for changelog

-Color coded Bender text for Bloodlines
-Filled in Roku, Sozin & Aang's, Chaejin(saowan), Kuvira's  bloodlines
-Fixed missing icons for several bloodlines including above
-Removed duplicates loc & (mainly sand society & avatar events )
-Fixed missing opinion localizations
-Added in missing Sun Warrior, Saowan Bloodlines
-Added image to tea society event
-Fixed tribal sand loc
-Sun Warriors now receive the 'Sun Warrior'  bloodline if they meet all prereqs (sun warrior faith, culture firebender etc), this is obviously inherited but just added incase the AI's dynasty dies out.
-One Nation Empire Bloodline now has its correct flag

---
## [ZacharyTStone/ZacharyTStone](https://github.com/ZacharyTStone/ZacharyTStone)@[d76b6eda23...](https://github.com/ZacharyTStone/ZacharyTStone/commit/d76b6eda23957b8c86d6bb7966298f6d069167c6)
#### Saturday 2023-12-02 08:04:19 by ROBO-ZACH

Update README with new quote: "It is one of the severest tests of friendship to tell your friend his faults. So to love a man that you cannot bear to see a stain upon him, and to speak painful truth through loving words, that is friendship." <br>— Henry Ward Beecher

---
## [Le-Jeremy-GG/Coral](https://github.com/Le-Jeremy-GG/Coral)@[1d6aabb3e0...](https://github.com/Le-Jeremy-GG/Coral/commit/1d6aabb3e0159f3b88b83bef47cb765c8b382f6f)
#### Saturday 2023-12-02 08:08:43 by Shirron

OMFG C'EST LE FUCKING SHADDER OPAQUE!

Fix du crash de façon DEFINITIVE
Fuck you Epic. Fixez votre fucking shader oppaque avant de le ship putin.

- Modification du DefaultEngine.ini :
    - MSAA à 4 au lieu de 2
    - Nanite disabled because, wtf?
    - Reactivation de la résolution dynamique.
    - Minimum pixel density set à 0.6.
    - Max pixel density set à 1 (ATTENTION, ne pas aller au dela, ça fait des bugs graphique).
    - ProcessorFavor set sur FavorEqually.

- Addaptation des corraux pour prendre en compte le passage de Opaque à Masked.
- Retrait de la console command du VRPawn.
- Ajustement du carrousel pour le mode Masked because fuck me that's why.

---
## [Higgin/tgstation](https://github.com/Higgin/tgstation)@[39d9c45b4a...](https://github.com/Higgin/tgstation/commit/39d9c45b4a7afc2a963de4249592a3d4ae6c4715)
#### Saturday 2023-12-02 08:20:20 by san7890

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
## [Higgin/tgstation](https://github.com/Higgin/tgstation)@[08ab5d2731...](https://github.com/Higgin/tgstation/commit/08ab5d27312d236593eabdb27fb23dccbf8283e6)
#### Saturday 2023-12-02 08:20:20 by Mothblocks

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
## [mooyg/cap](https://github.com/mooyg/cap)@[7c8d2ac197...](https://github.com/mooyg/cap/commit/7c8d2ac197f7634ceace15d3ad3dde03efd9302c)
#### Saturday 2023-12-02 08:35:45 by Lakshay Khattar

Add Email Validation Feature to HomePage.tsx

**Pull Request Description:**

**Description:**
This incredible masterpiece of code introduces a groundbreaking feature to the `HomePage` component – the ability to make users actually enter their email addresses. Say goodbye to the days of mysterious, empty submissions from users who apparently communicate telepathically.

**Changes Made:**
- Added state (`emailError`) to track email validation error messages.
- Updated the `handleSubmit` function to check for empty emails and display an error message if necessary.
- Modified JSX to display the error message in red, ensuring users get a hint about the existence of their keyboards.

**How to Test:**
1. Navigate to the `HomePage` component.
2. Attempt to submit the form without entering an email.
3. Witness the magic of a red error message gracefully reminding users to type something meaningful.

**Screenshots:**
Behold the beauty of an error message that tells users, "Your email is missing, genius!"

**Additional Notes:**
- Ensure you have sunglasses on when viewing the mesmerizing red error message.
- This groundbreaking feature has the potential to revolutionize the way we collect user data.

**Related Issue:**
Solve issue #8 

**Checklist:**
- [x] The code follows the project's coding standards because who needs standards?
- [x] Tests have been added because we love living on the edge.
- [x] The documentation has been updated because who doesn't love reading?

**Bounty Request:**
In recognition of the heroic effort put into solving this groundbreaking issue, I kindly request a bounty of one imaginary golden unicorn. If golden unicorns are in short supply, I will also accept a virtual high-five.

**Closing Note:**
May this code be forever remembered as the turning point in human-computer interaction history. Your gratitude and virtual unicorns are appreciated : )

---
## [goravgupta2007/Dr.-Gorav-Gupta](https://github.com/goravgupta2007/Dr.-Gorav-Gupta)@[56dccdeac4...](https://github.com/goravgupta2007/Dr.-Gorav-Gupta/commit/56dccdeac40345166639e1e1959a71f80af38d68)
#### Saturday 2023-12-02 09:01:14 by goravgupta2007

Update README.md

If you're looking for information or assistance regarding anxiety and are considering consulting with a psychiatrist, it's a positive step towards addressing your concerns. However, it's important to note that I am not a healthcare professional, and my responses should not be considered a substitute for professional medical advice.

If you are experiencing anxiety symptoms and are considering seeing a psychiatrist, here are some steps you might want to consider:

Primary Care Physician:
Start by consulting your primary care physician. They can assess your symptoms, rule out any underlying medical conditions, and provide a referral to a psychiatrist if needed.

Psychiatrist Referral:
If your primary care physician determines that your symptoms may benefit from psychiatric evaluation and treatment, they can refer you to a psychiatrist.

Insurance Coverage:
Check with your insurance provider to understand the coverage for mental health services, including psychiatry. This can help you find psychiatrists who accept your insurance.

Research and Recommendations:
Research local psychiatrists, and consider seeking recommendations from friends, family, or healthcare professionals. Online reviews and testimonials can also be helpful.

Initial Appointment:
Schedule an initial appointment with the psychiatrist. During this appointment, the psychiatrist will assess your symptoms, gather information about your medical and mental health history, and work with you to develop a treatment plan.

Therapeutic Approaches:
Psychiatrists may employ various therapeutic approaches, including medication management, psychotherapy, or a combination of both, depending on the nature and severity of your anxiety.

Open Communication:
Be open and honest with your psychiatrist about your symptoms, concerns, and any past treatments you may have tried. This information will help them tailor a treatment plan to your specific needs.

Remember, seeking help for anxiety is a positive step, and mental health professionals are trained to provide support and guidance. If you are in crisis or need urgent assistance, please contact your local emergency services or a mental health hotline.

Dr. Gorav Gupta is top psychiatrist in Delhi. He has been working in the field of mental health for 25 years. He is experienced in treating patients with addiction and mental health problems.

---
## [Nabu-upsidedowncake/platform_frameworks_base](https://github.com/Nabu-upsidedowncake/platform_frameworks_base)@[0d5442bc3a...](https://github.com/Nabu-upsidedowncake/platform_frameworks_base/commit/0d5442bc3a0594c9a2943d569c140c8f2599da1b)
#### Saturday 2023-12-02 09:19:31 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [MUKESHPAL311/Login-Page](https://github.com/MUKESHPAL311/Login-Page)@[1f93baca10...](https://github.com/MUKESHPAL311/Login-Page/commit/1f93baca10b13ccc13ee31c6a27e7943c0415276)
#### Saturday 2023-12-02 09:24:52 by Your Name

Elevate your user onboarding experience with our Signup Form React App! This innovative application combines the power of React with a user-friendly interface to streamline the signup process. With responsive design, robust security measures, and customizable fields, our app offers a modern solution for effortless registration. Forget the hassle – our password recovery feature and clear error handling make user interaction intuitive and error-free. Join us on this journey to redefine user onboarding. Embrace simplicity, security, and style with our Signup Form React App. Get started today for a seamless and delightful signup experience!

Welcome to our Signup Form React App – the seamless solution for effortless user onboarding! Our application leverages the power of React to deliver a smooth and intuitive signup experience, ensuring a delightful start for your users.

Key Features:

User-Friendly Interface: Our signup form boasts a clean and user-friendly interface, designed to guide users through the registration process with ease.

Responsive Design: Enjoy a consistent and visually appealing experience across various devices. Our app is built with responsiveness in mind, ensuring accessibility from desktops to smartphones.

Secure and Reliable: Your users' security is our priority. We implement robust security measures to protect sensitive information, guaranteeing a secure signup process.

Password Recovery: Forgot your password? No worries! Our app includes a password recovery feature, allowing users to regain access to their accounts effortlessly.

Customizable Fields: Tailor the signup form to your specific needs. Whether you require additional information or want to streamline the registration process, our app offers flexibility in customizing form fields.

Error Handling: Say goodbye to confusing error messages. Our app provides clear and concise error handling, guiding users to rectify any mistakes made during the signup process.

Modern Design Elements: Impress your users with a modern and visually appealing design. Our app incorporates the latest design trends to enhance the overall user experience.

How to Get Started:

Click the signup link to create your account.
Fill out the form with your details.
Experience the simplicity and efficiency of our signup process.
Join us on this journey of creating a seamless onboarding experience for your users. Get started with our Signup Form React App today!

Feel free to customize this description based on the specific features and benefits your signup form React app offers. Highlighting unique aspects and user benefits will help attract and engage potential users.

---
## [lgritz/OpenImageIO](https://github.com/lgritz/OpenImageIO)@[51899ea478...](https://github.com/lgritz/OpenImageIO/commit/51899ea47895d299ca6245dd4b99597b2202ddf8)
#### Saturday 2023-12-02 09:29:04 by Larry Gritz

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
## [cosanta/cosanta-core](https://github.com/cosanta/cosanta-core)@[249d6cb7b4...](https://github.com/cosanta/cosanta-core/commit/249d6cb7b4b94d9ee220317dd4fe0d38bcdb8c98)
#### Saturday 2023-12-02 09:40:24 by fanquake

Merge #18295: scripts: add MACHO lazy bindings check to security-check.py

5ca90f8b598978437340bb8467f527b9edfb2bbf scripts: add MACHO lazy bindings check to security-check.py (fanquake)

Pull request description:

  This is a slightly belated follow up to #17686 and some discussion with Cory. It's not entirely clear if we should make this change due to the way the macOS dynamic loader appears to work. However I'm opening this for some discussion. Also related to #17768.

  #### Issue:
  [`LD64`](https://opensource.apple.com/source/ld64/) doesn't set the [MH_BINDATLOAD](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) bit in the header of MACHO executables, when building with `-bind_at_load`. This is in contradiction to the [documentation](https://opensource.apple.com/source/ld64/ld64-450.3/doc/man/man1/ld.1.auto.html):
  ```bash
  -bind_at_load
       Sets a bit in the mach header of the resulting binary which tells dyld to
       bind all symbols when the binary is loaded, rather than lazily.
  ```

  The [`ld` in Apples cctools](https://opensource.apple.com/source/cctools/cctools-927.0.2/ld/layout.c.auto.html) does set the bit, however the [cctools-port](https://github.com/tpoechtrager/cctools-port/) that we use for release builds, bundles `LD64`.

  However; even if the linker hasn't set that bit, the dynamic loader ([`dyld`](https://opensource.apple.com/source/dyld/)) doesn't seem to ever check for it, and from what I understand, it looks at a different part of the header when determining whether to lazily load symbols.

  Note that our release binaries are currently working as expected, and no lazy loading occurs.

  #### Example:

  Using a small program, we can observe the behaviour of the dynamic loader.

  Conducted using:
  ```bash
  clang++ --version
  Apple clang version 11.0.0 (clang-1100.0.33.17)
  Target: x86_64-apple-darwin18.7.0

  ld -v
  @(#)PROGRAM:ld  PROJECT:ld64-530
  BUILD 18:57:17 Dec 13 2019
  LTO support using: LLVM version 11.0.0, (clang-1100.0.33.17) (static support for 23, runtime is 23)
  TAPI support using: Apple TAPI version 11.0.0 (tapi-1100.0.11)
  ```

  ```cpp
  #include <iostream>
  int main() {
  	std::cout << "Hello World!\n";
  	return 0;
  }
  ```

  Compile and check the MACHO header:
  ```bash
  clang++ test.cpp -o test
  otool -vh test
  ...
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE

  # Run and dump dynamic loader bindings:
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=no_bind.txt ./test
  Hello World!
  ```

  Recompile with `-bind_at_load`. Note still no `BINDATLOAD` flag:
  ```bash
  clang++ test.cpp -o test -Wl,-bind_at_load
  otool -vh test
  Mach header
        magic cputype cpusubtype  caps    filetype ncmds sizeofcmds      flags
  MH_MAGIC_64  X86_64        ALL LIB64     EXECUTE    16       1424   NOUNDEFS DYLDLINK TWOLEVEL WEAK_DEFINES BINDS_TO_WEAK PIE
  ...
  DYLD_PRINT_BINDINGS=1 DYLD_PRINT_TO_FILE=bind.txt ./test
  Hello World!
  ```

  If we diff the outputs, you can see that `dyld` doesn't perform any lazy bindings when the binary is compiled with `-bind_at_load`, even if the `BINDATLOAD` flag is not set:
  ```diff
  @@ -1,11 +1,27 @@
  +dyld: bind: test:0x103EDF030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x103EDF030 = 0x7FFF70C9FA58
  +dyld: bind: test:0x103EDF038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x103EDF038 = 0x7FFF70CA12C2
  +dyld: bind: test:0x103EDF068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x103EDF068 = 0x7FFF70CA12B6
  +dyld: bind: test:0x103EDF070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x103EDF070 = 0x7FFF70CA1528
  +dyld: bind: test:0x103EDF080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x103EDF080 = 0x7FFF70C9FAE6
  <trim>
  -dyld: lazy bind: test:0x10D4AC0C8 = libsystem_platform.dylib:_strlen, *0x10D4AC0C8 = 0x7FFF73C5C6E0
  -dyld: lazy bind: test:0x10D4AC068 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_, *0x10D4AC068 = 0x7FFF70CA12B6
  -dyld: lazy bind: test:0x10D4AC038 = libc++.1.dylib:__ZNKSt3__18ios_base6getlocEv, *0x10D4AC038 = 0x7FFF70CA12C2
  -dyld: lazy bind: test:0x10D4AC030 = libc++.1.dylib:__ZNKSt3__16locale9use_facetERNS0_2idE, *0x10D4AC030 = 0x7FFF70C9FA58
  -dyld: lazy bind: test:0x10D4AC080 = libc++.1.dylib:__ZNSt3__16localeD1Ev, *0x10D4AC080 = 0x7FFF70C9FAE6
  -dyld: lazy bind: test:0x10D4AC070 = libc++.1.dylib:__ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE6sentryD1Ev, *0x10D4AC070 = 0x7FFF70CA1528
  ```

  Note: `dyld` also has a `DYLD_BIND_AT_LAUNCH=1` environment variable, that when set, will force any lazy bindings to be non-lazy:
  ```bash
  dyld: forced lazy bind: test:0x10BEC8068 = libc++.1.dylib:__ZNSt3__113basic_ostream
  ```

  #### Thoughts:
  After looking at the dyld source, I can't find any checks for `MH_BINDATLOAD`. You can see the flags it does check for, such as MH_PIE or MH_BIND_TO_WEAK [here](https://opensource.apple.com/source/dyld/dyld-732.8/src/ImageLoaderMachO.cpp.auto.html).

  It seems that the lazy binding of any symbols depends on whether or not [lazy_bind_size](https://opensource.apple.com/source/xnu/xnu-6153.11.26/EXTERNAL_HEADERS/mach-o/loader.h.auto.html) from the `LC_DYLD_INFO_ONLY` load command is > 0. Which was mentioned in [#17686](https://github.com/bitcoin/bitcoin/pull/17686#issue-350216254).

  #### Changes:
  This PR is one of [Corys commits](https://github.com/theuni/bitcoin/commit/7b6ba26178d2754568a1308d3d44e038e9ebf450), that I've rebased and modified to make build. I've also included an addition to the `security-check.py` script to check for the flag.

  However, given the above, I'm not entirely sure this patch is the correct approach. If the linker no-longer inserts it, and the dynamic loader doesn't look for it, there might be little benefit to setting it. Or, maybe this is an oversight from Apple and needs some upstream discussion. Looking for some thoughts / Concept ACK/NACK.

  One alternate approach we could take is to drop the patch and modify security-check.py to look for `lazy_bind_size` == 0 in the `LC_DYLD_INFO_ONLY` load command, using `otool -l`.

ACKs for top commit:
  theuni:
    ACK 5ca90f8b598978437340bb8467f527b9edfb2bbf

Tree-SHA512: 444022ea9d19ed74dd06dc2ab3857a9c23fbc2f6475364e8552d761b712d684b3a7114d144f20de42328d1a99403b48667ba96885121392affb2e05b834b6e1c

---
## [jro31/slowmadding](https://github.com/jro31/slowmadding)@[9f5e41f2b6...](https://github.com/jro31/slowmadding/commit/9f5e41f2b68e24f1ecb633c61f338ec99509fb99)
#### Saturday 2023-12-02 09:50:37 by Jethro Williams

Attempt to consider user's timezone when generating timeline

Fuck I hate timezones.

This commit reverts the previous change of adding a timezone to the `formatDate` function, which wasn't working anyway because I'd used `timezone` instead of `timeZone`, because that's the kind of genius I am, but I also decided this wasn't the place to mess around with timezones and any date passed-in here shoiuld be formatted in UTC anyway so that it will be rendered the same no matter where the user is (so long as it's passed-in as a UTC date).

Instead, the key change is that we're using the local date for the user in the timeline component (imported into the timeline in the `usersDate` variable) and comparing that date to the arrival/departure in place of the `beginningOfToday` variable, which was the beginning of the current day in UTC time, but was inaccurate if the date for the current user differed for the current UTC date.

This, in theory, will keep the timeline accurate for the local user at all hours of the day so even after midnight, my current stay should say 'now' instead of a date.

That was a lot of work just to say 'now' for a bit longer.

As the `formatDate` function is used in a lot of places, all should be checked (before and after midnight) as displaying dates correctly, particularly the timeline.

---
## [functionland/collabora-RK3588-linux](https://github.com/functionland/collabora-RK3588-linux)@[a06a4dc3a0...](https://github.com/functionland/collabora-RK3588-linux/commit/a06a4dc3a08201ff6a8a958f935b3cbf7744115f)
#### Saturday 2023-12-02 09:56:25 by Neil Horman

kmod: add init function to usermodehelper

About 6 months ago, I made a set of changes to how the core-dump-to-a-pipe
feature in the kernel works.  We had reports of several races, including
some reports of apps bypassing our recursion check so that a process that
was forked as part of a core_pattern setup could infinitely crash and
refork until the system crashed.

We fixed those by improving our recursion checks.  The new check basically
refuses to fork a process if its core limit is zero, which works well.

Unfortunately, I've been getting grief from maintainer of user space
programs that are inserted as the forked process of core_pattern.  They
contend that in order for their programs (such as abrt and apport) to
work, all the running processes in a system must have their core limits
set to a non-zero value, to which I say 'yes'.  I did this by design, and
think thats the right way to do things.

But I've been asked to ease this burden on user space enough times that I
thought I would take a look at it.  The first suggestion was to make the
recursion check fail on a non-zero 'special' number, like one.  That way
the core collector process could set its core size ulimit to 1, and enable
the kernel's recursion detection.  This isn't a bad idea on the surface,
but I don't like it since its opt-in, in that if a program like abrt or
apport has a bug and fails to set such a core limit, we're left with a
recursively crashing system again.

So I've come up with this.  What I've done is modify the
call_usermodehelper api such that an extra parameter is added, a function
pointer which will be called by the user helper task, after it forks, but
before it exec's the required process.  This will give the caller the
opportunity to get a call back in the processes context, allowing it to do
whatever it needs to to the process in the kernel prior to exec-ing the
user space code.  In the case of do_coredump, this callback is ues to set
the core ulimit of the helper process to 1.  This elimnates the opt-in
problem that I had above, as it allows the ulimit for core sizes to be set
to the value of 1, which is what the recursion check looks for in
do_coredump.

This patch:

Create new function call_usermodehelper_fns() and allow it to assign both
an init and cleanup function, as we'll as arbitrary data.

The init function is called from the context of the forked process and
allows for customization of the helper process prior to calling exec.  Its
return code gates the continuation of the process, or causes its exit.
Also add an arbitrary data pointer to the subprocess_info struct allowing
for data to be passed from the caller to the new process, and the
subsequent cleanup process

Also, use this patch to cleanup the cleanup function.  It currently takes
an argp and envp pointer for freeing, which is ugly.  Lets instead just
make the subprocess_info structure public, and pass that to the cleanup
and init routines

Signed-off-by: Neil Horman <nhorman@tuxdriver.com>
Reviewed-by: Oleg Nesterov <oleg@redhat.com>
Cc: Andi Kleen <andi@firstfloor.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [carshalash/lobotomy-corp13](https://github.com/carshalash/lobotomy-corp13)@[e23ea7b596...](https://github.com/carshalash/lobotomy-corp13/commit/e23ea7b5965a446e5b34f30baa0d4e4dc2d5b868)
#### Saturday 2023-12-02 10:11:42 by Táculo

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
## [carshalash/lobotomy-corp13](https://github.com/carshalash/lobotomy-corp13)@[294f764ad0...](https://github.com/carshalash/lobotomy-corp13/commit/294f764ad01a99c63b46dfea3dac7e5cfe14cd7d)
#### Saturday 2023-12-02 10:11:42 by Coxswain

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
## [Erol509/Bubberstation](https://github.com/Erol509/Bubberstation)@[b5e095e380...](https://github.com/Erol509/Bubberstation/commit/b5e095e380e729793628d254bb441f51ecdb046b)
#### Saturday 2023-12-02 10:33:15 by Waterpig

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
## [yourdoom9898/Citadel-Station-13-RP](https://github.com/yourdoom9898/Citadel-Station-13-RP)@[81c1229373...](https://github.com/yourdoom9898/Citadel-Station-13-RP/commit/81c1229373208790c3375a138579aaf76a0006d0)
#### Saturday 2023-12-02 10:42:41 by Captain277

Adds Just Like, a Ton of Clothes (#5048)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. **Adds a wide array of clothes, listed below.**

## Why It's Good For The Game

1. _My good friend Tech provided me with some sprite sheets when I was
working on Ashlanders, requesting a hobo coat. Going through the sheets
I found several different items I thought it would be fun to add to our
expanding list of customization and fashion options. The list is huge so
I'm just gonna itemize it here. As for attributions, as I understand it
most of this is from a D&D server, and some from a 40k server._
2. _Two of the outfits, the Belial and Lilin items, are sprites crafted
by our very own Doopy, as part of their Lindenoak line!_

## Outfits & Where to Get them

**Costume Vendor**
1. _Banana Costume_
3. _Hashashin Costume_
4. _Bard Hat_
5. _Aquiline Enforcer Uniform_
6. _Scavenging Sniper Set_
7. _Spiral Hero Outfit_
8. _Body Tape Wrapping_
9. _Redcoat Uniform_
10. _Despotic General Uniform_
11. _Post-Revolution American Uniform_
12. _Prussian Uniform_

**Suit Vendor**
1. _Ragged Coat_
2. _Spiral Hero Cloak_
3. _Nerdy Shirt_

**Jumpsuit Vendor**
1. _Toga_
2. _Countess Dress_
3. _Baroness Dress_
4. _Revealing Cocktail Dress_
5. _Belial Striped Shirt and Shorts_
6. _Lilin Sash Dress_

**Shoes Vendor**
1. _Utilitarian Shoes_

**Loadout**
1. _Ragged Coat_
7. _Spiral Hero Cloak_
8. _Nerdy Shirt_
9. _Bard Hat_
10. _Utilitarian Shoes_
11. _Toga_
13. _Countess Dress_
14. _Baroness Dress_
15. _Scavenging Sniper Set_
16. _Spiral Hero Outfit_
17. _Body Tape Wrapping_
18. _Revealing Cocktail Dress_
19. _Belial Striped Shirt and Shorts_
20. _Lilin Sash Dress_

**Medieval Armor Supply Crate**
1. _Crimson Knight Armor_
2. _Forest Knight Armor_
3. _Hauberk_
4. _Elite Paladin Armor, Helmet, and Boots_
5. _Alternate Knight Helmet_

**Cryosuit Supply Crates (Under Voidsuit Menu)**
1. _Cryosuit, Variants: Security, Engineering, Atmos, Mining_

**Crafting Menu**
1. _Duraskull Helmet_

**Ashlander Specific Crafting Menu**
1. _Ashen Vestment_
2. _Ashen Tabard_

**Ashlander Spawn**
1. _Priests now spawn with the Ashen Vestment._

**Admin Spawn**
1. _Actual armored versions of all new Knight sets._
5. _Utilitarian Military Helmet, Armor, and Boots._

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
add: Adds a wide array of new clothing items. Itemized in PR. #5408
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Dogist/PathOfBuilding](https://github.com/Dogist/PathOfBuilding)@[fb66ee7051...](https://github.com/Dogist/PathOfBuilding/commit/fb66ee70516cdb416b6f9c7799307c5757e199b2)
#### Saturday 2023-12-02 10:42:56 by LocalIdentity

Fix accuracy of skill Mana/Life cost calculations (#6220)

* Rough code to male it work

* Recommit changes

* Fix breakdowns

* Correct values for Divine Blessing

* Fix breakdown when using Lifetap or Blood Magic

* Fix display of skills with innate Life Cost

---------

Co-authored-by: LocalIdentity <localidentity2@gmail.com>

---
## [RobinTail/express-zod-api](https://github.com/RobinTail/express-zod-api)@[7c0e0ed291...](https://github.com/RobinTail/express-zod-api/commit/7c0e0ed2910fc8480593c3a4128acaaccd58823c)
#### Saturday 2023-12-02 10:53:05 by Anna Bocharova

`v15` is for Vika (#1301)

### The dedication


![image](https://github.com/RobinTail/express-zod-api/assets/13189514/49831267-e98b-4e17-a961-edfe312224cf)

Vika was 24 years young transgender woman when her boyfriend (a
policeman, by the way) murdered her. Moreover, in order to confuse the
tracks and create the impression that the murdered woman was alive, the
policeman cut off her finger, unlocked her mobile phone and sent
messages to her friends. On the evening of October 13, 2020, he was
detained, confessed and showed where he buried the girl’s body.

https://ngs.ru/text/criminal/2022/09/29/71695301/

Transgender women suffer too frequently from transphobic violence and
cruelty, being the less protected social group. I'd like to raise an
awareness of this problem. Humans should be creators — not killers.
Protect transgender women.

Find out more about Vika's story from her interview:
https://ngs.ru/text/relations/2019/06/25/66137377/

----------------------

### Version 15

... description coming soon ...

- #1255 
- #1280 
- #1314 
- #1335 
  - supporting any testing framework having function mocking method 
- #1343 
- #1342 
- #1347

---
## [functionland/collabora-RK3588-linux](https://github.com/functionland/collabora-RK3588-linux)@[4d6fa57b4d...](https://github.com/functionland/collabora-RK3588-linux/commit/4d6fa57b4dab0d77f4d8e9d9c73d1e63f6fe8fee)
#### Saturday 2023-12-02 11:16:30 by Jason A. Donenfeld

macsec: avoid heap overflow in skb_to_sgvec

While this may appear as a humdrum one line change, it's actually quite
important. An sk_buff stores data in three places:

1. A linear chunk of allocated memory in skb->data. This is the easiest
   one to work with, but it precludes using scatterdata since the memory
   must be linear.
2. The array skb_shinfo(skb)->frags, which is of maximum length
   MAX_SKB_FRAGS. This is nice for scattergather, since these fragments
   can point to different pages.
3. skb_shinfo(skb)->frag_list, which is a pointer to another sk_buff,
   which in turn can have data in either (1) or (2).

The first two are rather easy to deal with, since they're of a fixed
maximum length, while the third one is not, since there can be
potentially limitless chains of fragments. Fortunately dealing with
frag_list is opt-in for drivers, so drivers don't actually have to deal
with this mess. For whatever reason, macsec decided it wanted pain, and
so it explicitly specified NETIF_F_FRAGLIST.

Because dealing with (1), (2), and (3) is insane, most users of sk_buff
doing any sort of crypto or paging operation calls a convenient function
called skb_to_sgvec (which happens to be recursive if (3) is in use!).
This takes a sk_buff as input, and writes into its output pointer an
array of scattergather list items. Sometimes people like to declare a
fixed size scattergather list on the stack; othertimes people like to
allocate a fixed size scattergather list on the heap. However, if you're
doing it in a fixed-size fashion, you really shouldn't be using
NETIF_F_FRAGLIST too (unless you're also ensuring the sk_buff and its
frag_list children arent't shared and then you check the number of
fragments in total required.)

Macsec specifically does this:

        size += sizeof(struct scatterlist) * (MAX_SKB_FRAGS + 1);
        tmp = kmalloc(size, GFP_ATOMIC);
        *sg = (struct scatterlist *)(tmp + sg_offset);
	...
        sg_init_table(sg, MAX_SKB_FRAGS + 1);
        skb_to_sgvec(skb, sg, 0, skb->len);

Specifying MAX_SKB_FRAGS + 1 is the right answer usually, but not if you're
using NETIF_F_FRAGLIST, in which case the call to skb_to_sgvec will
overflow the heap, and disaster ensues.

Signed-off-by: Jason A. Donenfeld <Jason@zx2c4.com>
Cc: stable@vger.kernel.org
Cc: security@kernel.org
Signed-off-by: David S. Miller <davem@davemloft.net>

---
## [RengaN02/PsychonautStation](https://github.com/RengaN02/PsychonautStation)@[31afabc9af...](https://github.com/RengaN02/PsychonautStation/commit/31afabc9afae2252fc22958d07f12f7148d6963d)
#### Saturday 2023-12-02 11:25:53 by Jacquerel

Adds missing default biotypes to some damage procs (#79102)

## About The Pull Request

I noticed by complete coincidence because I happened to glance at the
channel a bunch of people complaining about blobbernauts not taking any
damage when leaving the blob in manuel round end chat.
Did anyone report this bug, even after prompting? No. Not even the game
admin who was playing as the blob.

Makes you wonder how many other bugs people are perfectly willing to
spend 15 minutes posting "i fucking hate coders" about without actually
telling anyone they exist. Sucks to be them I guess.

Anyone the cause is that some of these procs didn't have a default
biotype, so they would never take the toxin damage they were being
assigned. Now they will.

## Changelog

:cl:
fix: Blobbernauts will once again take damage when not on blob tiles.
/:cl:

---
## [RengaN02/PsychonautStation](https://github.com/RengaN02/PsychonautStation)@[ece51a1a9d...](https://github.com/RengaN02/PsychonautStation/commit/ece51a1a9d6896a54b878563d9c33002bc8f3688)
#### Saturday 2023-12-02 11:25:53 by nikothedude

[NO GBP] Fixes scream for me, and also fixes literally EVERY INSTANCE of non-random puncture wounds (#79043)

## About The Pull Request

Closes https://github.com/tgstation/tgstation/issues/79017

So turns out, I

1. Had a pair of inverted more/less than operators in a crucial area. I
DONT KNOW HOW THIS WORKED. SHIT is a FUCKING mystery.
2. Used a non-existant define which DM converted into a string because
Byond
## Why It's Good For The Game

bugsgs badagfd
## Changelog
:cl:
fix: Scream for me, the spell, now works
fix: Non-random puncture wounds can now be applied
/:cl:

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [functionland/collabora-RK3588-linux](https://github.com/functionland/collabora-RK3588-linux)@[3eb39f4793...](https://github.com/functionland/collabora-RK3588-linux/commit/3eb39f47934f9d5a3027fe00d906a45fe3a15fad)
#### Saturday 2023-12-02 11:42:17 by Christian Brauner

signal: add pidfd_send_signal() syscall

The kill() syscall operates on process identifiers (pid). After a process
has exited its pid can be reused by another process. If a caller sends a
signal to a reused pid it will end up signaling the wrong process. This
issue has often surfaced and there has been a push to address this problem [1].

This patch uses file descriptors (fd) from proc/<pid> as stable handles on
struct pid. Even if a pid is recycled the handle will not change. The fd
can be used to send signals to the process it refers to.
Thus, the new syscall pidfd_send_signal() is introduced to solve this
problem. Instead of pids it operates on process fds (pidfd).

/* prototype and argument /*
long pidfd_send_signal(int pidfd, int sig, siginfo_t *info, unsigned int flags);

/* syscall number 424 */
The syscall number was chosen to be 424 to align with Arnd's rework in his
y2038 to minimize merge conflicts (cf. [25]).

In addition to the pidfd and signal argument it takes an additional
siginfo_t and flags argument. If the siginfo_t argument is NULL then
pidfd_send_signal() is equivalent to kill(<positive-pid>, <signal>). If it
is not NULL pidfd_send_signal() is equivalent to rt_sigqueueinfo().
The flags argument is added to allow for future extensions of this syscall.
It currently needs to be passed as 0. Failing to do so will cause EINVAL.

/* pidfd_send_signal() replaces multiple pid-based syscalls */
The pidfd_send_signal() syscall currently takes on the job of
rt_sigqueueinfo(2) and parts of the functionality of kill(2), Namely, when a
positive pid is passed to kill(2). It will however be possible to also
replace tgkill(2) and rt_tgsigqueueinfo(2) if this syscall is extended.

/* sending signals to threads (tid) and process groups (pgid) */
Specifically, the pidfd_send_signal() syscall does currently not operate on
process groups or threads. This is left for future extensions.
In order to extend the syscall to allow sending signal to threads and
process groups appropriately named flags (e.g. PIDFD_TYPE_PGID, and
PIDFD_TYPE_TID) should be added. This implies that the flags argument will
determine what is signaled and not the file descriptor itself. Put in other
words, grouping in this api is a property of the flags argument not a
property of the file descriptor (cf. [13]). Clarification for this has been
requested by Eric (cf. [19]).
When appropriate extensions through the flags argument are added then
pidfd_send_signal() can additionally replace the part of kill(2) which
operates on process groups as well as the tgkill(2) and
rt_tgsigqueueinfo(2) syscalls.
How such an extension could be implemented has been very roughly sketched
in [14], [15], and [16]. However, this should not be taken as a commitment
to a particular implementation. There might be better ways to do it.
Right now this is intentionally left out to keep this patchset as simple as
possible (cf. [4]).

/* naming */
The syscall had various names throughout iterations of this patchset:
- procfd_signal()
- procfd_send_signal()
- taskfd_send_signal()
In the last round of reviews it was pointed out that given that if the
flags argument decides the scope of the signal instead of different types
of fds it might make sense to either settle for "procfd_" or "pidfd_" as
prefix. The community was willing to accept either (cf. [17] and [18]).
Given that one developer expressed strong preference for the "pidfd_"
prefix (cf. [13]) and with other developers less opinionated about the name
we should settle for "pidfd_" to avoid further bikeshedding.

The  "_send_signal" suffix was chosen to reflect the fact that the syscall
takes on the job of multiple syscalls. It is therefore intentional that the
name is not reminiscent of neither kill(2) nor rt_sigqueueinfo(2). Not the
fomer because it might imply that pidfd_send_signal() is a replacement for
kill(2), and not the latter because it is a hassle to remember the correct
spelling - especially for non-native speakers - and because it is not
descriptive enough of what the syscall actually does. The name
"pidfd_send_signal" makes it very clear that its job is to send signals.

/* zombies */
Zombies can be signaled just as any other process. No special error will be
reported since a zombie state is an unreliable state (cf. [3]). However,
this can be added as an extension through the @flags argument if the need
ever arises.

/* cross-namespace signals */
The patch currently enforces that the signaler and signalee either are in
the same pid namespace or that the signaler's pid namespace is an ancestor
of the signalee's pid namespace. This is done for the sake of simplicity
and because it is unclear to what values certain members of struct
siginfo_t would need to be set to (cf. [5], [6]).

/* compat syscalls */
It became clear that we would like to avoid adding compat syscalls
(cf. [7]).  The compat syscall handling is now done in kernel/signal.c
itself by adding __copy_siginfo_from_user_generic() which lets us avoid
compat syscalls (cf. [8]). It should be noted that the addition of
__copy_siginfo_from_user_any() is caused by a bug in the original
implementation of rt_sigqueueinfo(2) (cf. 12).
With upcoming rework for syscall handling things might improve
significantly (cf. [11]) and __copy_siginfo_from_user_any() will not gain
any additional callers.

/* testing */
This patch was tested on x64 and x86.

/* userspace usage */
An asciinema recording for the basic functionality can be found under [9].
With this patch a process can be killed via:

 #define _GNU_SOURCE
 #include <errno.h>
 #include <fcntl.h>
 #include <signal.h>
 #include <stdio.h>
 #include <stdlib.h>
 #include <string.h>
 #include <sys/stat.h>
 #include <sys/syscall.h>
 #include <sys/types.h>
 #include <unistd.h>

 static inline int do_pidfd_send_signal(int pidfd, int sig, siginfo_t *info,
                                         unsigned int flags)
 {
 #ifdef __NR_pidfd_send_signal
         return syscall(__NR_pidfd_send_signal, pidfd, sig, info, flags);
 #else
         return -ENOSYS;
 #endif
 }

 int main(int argc, char *argv[])
 {
         int fd, ret, saved_errno, sig;

         if (argc < 3)
                 exit(EXIT_FAILURE);

         fd = open(argv[1], O_DIRECTORY | O_CLOEXEC);
         if (fd < 0) {
                 printf("%s - Failed to open \"%s\"\n", strerror(errno), argv[1]);
                 exit(EXIT_FAILURE);
         }

         sig = atoi(argv[2]);

         printf("Sending signal %d to process %s\n", sig, argv[1]);
         ret = do_pidfd_send_signal(fd, sig, NULL, 0);

         saved_errno = errno;
         close(fd);
         errno = saved_errno;

         if (ret < 0) {
                 printf("%s - Failed to send signal %d to process %s\n",
                        strerror(errno), sig, argv[1]);
                 exit(EXIT_FAILURE);
         }

         exit(EXIT_SUCCESS);
 }

/* Q&A
 * Given that it seems the same questions get asked again by people who are
 * late to the party it makes sense to add a Q&A section to the commit
 * message so it's hopefully easier to avoid duplicate threads.
 *
 * For the sake of progress please consider these arguments settled unless
 * there is a new point that desperately needs to be addressed. Please make
 * sure to check the links to the threads in this commit message whether
 * this has not already been covered.
 */
Q-01: (Florian Weimer [20], Andrew Morton [21])
      What happens when the target process has exited?
A-01: Sending the signal will fail with ESRCH (cf. [22]).

Q-02:  (Andrew Morton [21])
       Is the task_struct pinned by the fd?
A-02:  No. A reference to struct pid is kept. struct pid - as far as I
       understand - was created exactly for the reason to not require to
       pin struct task_struct (cf. [22]).

Q-03: (Andrew Morton [21])
      Does the entire procfs directory remain visible? Just one entry
      within it?
A-03: The same thing that happens right now when you hold a file descriptor
      to /proc/<pid> open (cf. [22]).

Q-04: (Andrew Morton [21])
      Does the pid remain reserved?
A-04: No. This patchset guarantees a stable handle not that pids are not
      recycled (cf. [22]).

Q-05: (Andrew Morton [21])
      Do attempts to signal that fd return errors?
A-05: See {Q,A}-01.

Q-06: (Andrew Morton [22])
      Is there a cleaner way of obtaining the fd? Another syscall perhaps.
A-06: Userspace can already trivially retrieve file descriptors from procfs
      so this is something that we will need to support anyway. Hence,
      there's no immediate need to add another syscalls just to make
      pidfd_send_signal() not dependent on the presence of procfs. However,
      adding a syscalls to get such file descriptors is planned for a
      future patchset (cf. [22]).

Q-07: (Andrew Morton [21] and others)
      This fd-for-a-process sounds like a handy thing and people may well
      think up other uses for it in the future, probably unrelated to
      signals. Are the code and the interface designed to permit such
      future applications?
A-07: Yes (cf. [22]).

Q-08: (Andrew Morton [21] and others)
      Now I think about it, why a new syscall? This thing is looking
      rather like an ioctl?
A-08: This has been extensively discussed. It was agreed that a syscall is
      preferred for a variety or reasons. Here are just a few taken from
      prior threads. Syscalls are safer than ioctl()s especially when
      signaling to fds. Processes are a core kernel concept so a syscall
      seems more appropriate. The layout of the syscall with its four
      arguments would require the addition of a custom struct for the
      ioctl() thereby causing at least the same amount or even more
      complexity for userspace than a simple syscall. The new syscall will
      replace multiple other pid-based syscalls (see description above).
      The file-descriptors-for-processes concept introduced with this
      syscall will be extended with other syscalls in the future. See also
      [22], [23] and various other threads already linked in here.

Q-09: (Florian Weimer [24])
      What happens if you use the new interface with an O_PATH descriptor?
A-09:
      pidfds opened as O_PATH fds cannot be used to send signals to a
      process (cf. [2]). Signaling processes through pidfds is the
      equivalent of writing to a file. Thus, this is not an operation that
      operates "purely at the file descriptor level" as required by the
      open(2) manpage. See also [4].

/* References */
[1]:  https://lore.kernel.org/lkml/20181029221037.87724-1-dancol@google.com/
[2]:  https://lore.kernel.org/lkml/874lbtjvtd.fsf@oldenburg2.str.redhat.com/
[3]:  https://lore.kernel.org/lkml/20181204132604.aspfupwjgjx6fhva@brauner.io/
[4]:  https://lore.kernel.org/lkml/20181203180224.fkvw4kajtbvru2ku@brauner.io/
[5]:  https://lore.kernel.org/lkml/20181121213946.GA10795@mail.hallyn.com/
[6]:  https://lore.kernel.org/lkml/20181120103111.etlqp7zop34v6nv4@brauner.io/
[7]:  https://lore.kernel.org/lkml/36323361-90BD-41AF-AB5B-EE0D7BA02C21@amacapital.net/
[8]:  https://lore.kernel.org/lkml/87tvjxp8pc.fsf@xmission.com/
[9]:  https://asciinema.org/a/IQjuCHew6bnq1cr78yuMv16cy
[11]: https://lore.kernel.org/lkml/F53D6D38-3521-4C20-9034-5AF447DF62FF@amacapital.net/
[12]: https://lore.kernel.org/lkml/87zhtjn8ck.fsf@xmission.com/
[13]: https://lore.kernel.org/lkml/871s6u9z6u.fsf@xmission.com/
[14]: https://lore.kernel.org/lkml/20181206231742.xxi4ghn24z4h2qki@brauner.io/
[15]: https://lore.kernel.org/lkml/20181207003124.GA11160@mail.hallyn.com/
[16]: https://lore.kernel.org/lkml/20181207015423.4miorx43l3qhppfz@brauner.io/
[17]: https://lore.kernel.org/lkml/CAGXu5jL8PciZAXvOvCeCU3wKUEB_dU-O3q0tDw4uB_ojMvDEew@mail.gmail.com/
[18]: https://lore.kernel.org/lkml/20181206222746.GB9224@mail.hallyn.com/
[19]: https://lore.kernel.org/lkml/20181208054059.19813-1-christian@brauner.io/
[20]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[21]: https://lore.kernel.org/lkml/20181228152012.dbf0508c2508138efc5f2bbe@linux-foundation.org/
[22]: https://lore.kernel.org/lkml/20181228233725.722tdfgijxcssg76@brauner.io/
[23]: https://lwn.net/Articles/773459/
[24]: https://lore.kernel.org/lkml/8736rebl9s.fsf@oldenburg.str.redhat.com/
[25]: https://lore.kernel.org/lkml/CAK8P3a0ej9NcJM8wXNPbcGUyOUZYX+VLoDFdbenW3s3114oQZw@mail.gmail.com/

Cc: "Eric W. Biederman" <ebiederm@xmission.com>
Cc: Jann Horn <jannh@google.com>
Cc: Andy Lutomirsky <luto@kernel.org>
Cc: Andrew Morton <akpm@linux-foundation.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Al Viro <viro@zeniv.linux.org.uk>
Cc: Florian Weimer <fweimer@redhat.com>
Signed-off-by: Christian Brauner <christian@brauner.io>
Reviewed-by: Tycho Andersen <tycho@tycho.ws>
Reviewed-by: Kees Cook <keescook@chromium.org>
Reviewed-by: David Howells <dhowells@redhat.com>
Acked-by: Arnd Bergmann <arnd@arndb.de>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Acked-by: Serge Hallyn <serge@hallyn.com>
Acked-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [VasyaKaban/top_5_java_tricks_you_have_never_used_before](https://github.com/VasyaKaban/top_5_java_tricks_you_have_never_used_before)@[a1371a04e4...](https://github.com/VasyaKaban/top_5_java_tricks_you_have_never_used_before/commit/a1371a04e472b1f8e0dcec356ff66015fe9cbdc8)
#### Saturday 2023-12-02 11:47:27 by vasyakaban

Merge branch 'master' of github.com:VasyaKaban/top_5_java_tricks_you_have_never_used_before

FUCK GITHUB I HATE THIS FUCKING SHIT LOL I LIKE TO USE PLAIN DIRECTORIES INSTEAD YO FUCK TORVALDS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[74815acdf6...](https://github.com/Offroaders123/Smart-Text-Editor/commit/74815acdf63bfb562547036da3f90789184150d3)
#### Saturday 2023-12-02 11:57:14 by Offroaders123

STE.query() Sunsetting!

Finally breaking apart how this works! It was very stacked up and weird, looking back on it. But it's all based on experience, or rather my lack there of, always lots to learn from.

Very mind opening experience to hear the origins behind Devin Townsend's album Infinity, now I have a mix of feelings about the album. I love the music a lot, and still do, but it's a similar sad scenario to City, where it was heavily based on strife, or maybe rather it's relation to it (he mentions how it's a Ying-Yang based approach, I think the other was City? This is the peaceful side to the two). He's very inspiring in how he reflects on his life and his outlooks over time. Where he is now is so much different than back then.

Devin Townsend Podcast is great.

---
## [DivyaPareek7/Credit-card-Approval-Prediction](https://github.com/DivyaPareek7/Credit-card-Approval-Prediction)@[8b01520f62...](https://github.com/DivyaPareek7/Credit-card-Approval-Prediction/commit/8b01520f62de1c98ad8049a83e5c29f5528ad0ae)
#### Saturday 2023-12-02 11:57:51 by DivyaPareek7

Add files via upload

Instructions
Project proposal to predict credit card approval


1.	Questions
2.	Hypothesis
3.	Approach


You will prepare a project proposal detailing the questions we are wanting to answer. The initial hypotheses about the data relationships and the approach you will take to get your answers.


•	Proposal is just a plan.
•	End goal is important


Section 1: Questions to Answer
What questions do you want to answer? 2-5


1.	Why is your proposal important in today’s world? How predicting a good client is worthy for a bank?  
2.	How is it going to impact the banking sector? 
3.	If any, what is the gap in the knowledge or how your proposed method can be helpful if required in future for any bank in India.


Section 2: Initial Hypothesis (or hypotheses)
1.	Here you have to make some assumptions based on the questions you want to address based on the DA track or ML track. 
1.	If DA track please aim to identify patterns in the data and important features that may impact a ML model.
2.	If ML track please perform part ‘i’ as well as multiple machine learning models, perform all required steps to check if there is any assumption and justify your model. Why is your model better than any other possible model? Please justify it by relevant cost functions and if possible by any graph.
2.	From step 1, you may see some relationship that you want to explore and will develop a belief about data


Section 3: Data analysis approach
1.	What approach are you going to take in order to prove or disprove your hypothesis?
2.	What feature engineering techniques will be relevant to your project?
3.	Please justify your data analysis approach.
4.	Identify important patterns in your data using the EDA approach to justify your findings.


Section 4: Machine learning approach
1.	What method will you use for machine learning based predictions for credit card approval?
2.	Please justify the most appropriate model.
3.	Please perform necessary steps required to improve the accuracy of your model.
4.	Please compare all models (at least 4  models).


Utilize machine learning approaches to predict credit card approval based on customer information.


A bank's credit card department is one of the top adopters of data science. A top focus for the bank has always been acquiring new credit card customers. Giving out credit cards without doing proper research or evaluating applicants' creditworthiness is quite risky. The credit card department has been using a data-driven system for credit assessment called Credit Scoring for many years, and the model is known as an application scorecard. A credit card application's cutoff value is determined using the application scorecard, which also aids in estimating the applicant's level of risk. This decision is made based on strategic priority at a given time.


Customers must fill out a form, either physically or online, to apply for a credit card. The application data is used to evaluate the applicant's creditworthiness. The decision is made using the application data in addition to the Credit Bureau Score, such as the FICO Score in the US or the CIBIL Score in India, and other internal information on the applicants. Additionally, the banks are rapidly taking a lot of outside data into account to enhance the caliber of credit judgements.


Features name: (Credit_Card.csv)
Ind_ID: Client ID
Gender: Gender information
Car_owner: Having car or not
Propert_owner: Having property or not
Children: Count of children
Annual_income: Annual income
Type_Income: Income type
Education: Education level
Marital_status: Marital_status
Housing_type: Living style
Birthday_count: Use backward count from current day (0), -1 means yesterday.
Employed_days: Start date of employment. Use backward count from current day (0). Positive value means, individual is currently unemployed.
Mobile_phone: Any mobile phone
Work_phone: Any work phone
Phone: Any phone number
EMAIL_ID: Any email ID
Type_Occupation: Occupation
Family_Members: Family size


Another data set (Credit_card_label.csv) contains two key pieces of information
ID: The joining key between application data and credit status data, same is Ind_ID
Label: 0 is application approved and 1 is application rejected. 

SQL
Use MySQL or PyMySQL to perform the below queries. 
Note: Use only the cleaned data for SQL part of the project


1.	Group the customers based on their income type and find the average of their annual income.
2.	Find the female owners of cars and property.
3.	Find the male customers who are staying with their families.
4.	Please list the top five people having the highest income.
5.	How many married people are having bad credit?
6.	What is the highest education level and what is the total count?
7.	Between married males and females, who is having more bad credit?

---
## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[dffb6e3712...](https://github.com/Mu-L/crawl/commit/dffb6e3712f7bc9ff45b6ae244928f1d806afe75)
#### Saturday 2023-12-02 12:05:27 by regret-index

Brain Feed -> Brain Bite (minor damage + mp drain, no int drain)

Brain Feed is an extremely weird monster spell in most games. With so
little stat drain around by default in a three-rune game, individual hits
against a stat approach 0 extremely rarely unless a player has next to
none, which is influenced heavily by character start combo and very little
by normal character growth. The relatively minor hit of intelligence also
does very little for its use on higher Int characters aside from slightly
worsening spell success rates, which works weirdly against the flavour of
various brain-eating monsters not actually caring about the quality of
brain so much as just killing those with incidentally little of it.

It's kind of difficult to tell what this spell should do. It'd be entirely
possible to make it drain a lot more intelligence or percentage-based +
flat intelligence to make actually effect more characters, but while
strategic damage of a restorable sort would be more mechanical diversity,
screwing with spell success chances and non-tangible damage rolls aren't
mechanics we've kept to the present day (c.f. skilldrain, old sap magic).
So, I'm sidestepping the original effect of the spell entirely, while
focusing still on its theme.

Brain Feed is now revised into Brain Bite, a mildly-experimental mix of half
a Smite plus a percentile version of Draining Gaze- 4-8 irresistable direct
damage doubled if you have no mp, then draining 20% of one's max mp (rounded
down). (This now also works on monsters, dealing damage checking on antimagic
and then applying antimagic.) The percentage part lets it scale across the
game (compared to Draining Gaze rapidly heavily draining most player mp), and
irresistable but restrained damage sources are currently pretty reserved
designs (Smiting, Damnation, usually Torment) that could be iterated further
upon.

(It'd be good to think over what the point of statdrain even is outside
of Hell, Tomb, and klown pies. Possibly a variant of flaying but only
for stats would be interesting, possibly making an even shorter para but
with brief stat-zero would be an interesting revision of current para.
This is kind of out of this particular commit's scope, though- getting
to stat zero via Brain Feed didn't really happen for a very large number
of character combinations, so concerns over that are minimal.)

Tile update uses the old mimic teeth tile by coolio, modified by jpeg,
on top of the current Brain Feed icon by snw-0.

---
## [Kawa-oneechan/Asspull3X](https://github.com/Kawa-oneechan/Asspull3X)@[ed061251f7...](https://github.com/Kawa-oneechan/Asspull3X/commit/ed061251f76bffdd444c22a4035530b42490d244)
#### Saturday 2023-12-02 13:04:41 by Kawa

Add floating point support

Somehow this had to include a stupid two-line hack to enable two missing opcodes.

I'm told these two opcodes are part of the 68881 coprocessor. GCC insists on using it.

Fuck it. There's probably some intricate differences but THIS WORKS. Multiplying a float works.

It's bullshit and I HATE IT.

---
## [dr3ams/Roguelike-Adventures-and-Dungeons-2](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2)@[6fa8fc2ce2...](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2/commit/6fa8fc2ce24e32027fc452bc8e52e672aa5c5cd9)
#### Saturday 2023-12-02 13:25:31 by dr3ams

1.8 update

- Updated A Reliable Friend Quests (by RecyclingTiger)
	- Less bones needed to start the questline
	- Adjusted the Dog Modes description (DoggyTalents replaced their Command Emblem with the Dog Whistle)
	- Added Description for what each of the Whistle modes do
	- Updated dog bed description
	- Made some quest descriptions clearer to read
	- new quest for big bone & tiny bone
- Every single log & wood from biomes you go now has a wood to bark cutting board recipe (by RecyclingTiger)
- yeet gale shot & freezing shot (by RecyclingTiger)
	- enchantments are bugged; they are bow enchantments but can only be applied to swords & tridents
	- they do not function on either even with thrown tridents
- doubled durability of dungeons gear armor (by RecyclingTiger)
	- The durability script didn't affect the dungeons gear armor
	- also somehow the dungeons gear folder was in the wrong place so it didn't do anything. How did I not notice this for 7 months...
- New reward for a certain obsidian quest (by Zarchyar)
- added 2 missing pmmo boosts to dungeons gear armor  (by RecyclingTiger)
	- added skill boosts for the leggings & boots for the Spelunker & Battle armor
	- removed the minor negative skill effects from goat armor & beehive armor, they didn't do much anyways except discourage new players from using them
- removed negative light from hungry horror armor (by RecyclingTiger)
- fixed another typo (by RecyclingTiger)
- decreased mobs "Magic Resistance Increase" and "Max Magic Resistance" values. This is a buff.

---
## [cowprotocol/services](https://github.com/cowprotocol/services)@[1fe4c4485a...](https://github.com/cowprotocol/services/commit/1fe4c4485a2d5d8a557ff663a5163c9d83f9ec25)
#### Saturday 2023-12-02 13:39:13 by Martin Beckmann

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
## [nesbox/TIC-80](https://github.com/nesbox/TIC-80)@[c86219f735...](https://github.com/nesbox/TIC-80/commit/c86219f73563aefee4f81bceb6b58f957697f069)
#### Saturday 2023-12-02 13:40:30 by bonjorno7

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
## [kawaaii/kernel_gauguin](https://github.com/kawaaii/kernel_gauguin)@[b1acf857db...](https://github.com/kawaaii/kernel_gauguin/commit/b1acf857db5c4c1da995399c55251be32b8f14aa)
#### Saturday 2023-12-02 14:17:39 by Peter Zijlstra

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
## [tyfighter/mame-dev](https://github.com/tyfighter/mame-dev)@[96ab505d66...](https://github.com/tyfighter/mame-dev/commit/96ab505d665a886809e8109a55d5e13fb7e520aa)
#### Saturday 2023-12-02 14:32:37 by ArcadeShadow

ibm5170_cdrom.xml: Added 21 items (18 working). (#11760)

New working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
5 Plus One: Pack 12 - Ghostbusters II [redump.org]
Brutal: Paws of Fury (Europe) [redump.org]
Darkseed (Germany, Action Sixteen release) [redump.org]
Dune (Europe, White Label release) [redump.org]
Dune II - Battle for Arrakis (Netherlands) [redump.org]
Dune II - Battle for Arrakis (Germany, PC Games Collection 2 release) [redump.org]
Dune II - The Building of a Dynasty (USA, Gold Medal 12 CD Pack) [redump.org]
Fables & Fiends - Book Three: Malcolm's Revenge (Europe, Japan) [redump.org]
Fables & Fiends - Book Two: The Hand of Fate (UK, Sold Out release) [redump.org]
Jurassic Park (Europe) [redump.org]
Jurassic Park (Germany) [redump.org]
Jurassic Park (USA) [redump.org]
Star Control [redump.org]
Stellar 7 (USA) [redump.org]
Stellar 7 (USA, alt) [redump.org]
The Cool Croc Twins + Magic Boy (Europe, 2 Game Pack release) [redump.org]
The Cool Croc Twins + Magic Boy (Netherlands) [redump.org]
The Dig (Japan) [redump.org]

New NOT working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
Darkseed (USA) [redump.org]
Darkseed (USA, alt) [redump.org]
Dogfight: 80 Years of Aerial Warfare (Europe) [redump.org]

---
## [Cevaler/New-Paradise-SS220](https://github.com/Cevaler/New-Paradise-SS220)@[c3a78f9ce0...](https://github.com/Cevaler/New-Paradise-SS220/commit/c3a78f9ce0f30474636d1100d3d24310bbb3fe08)
#### Saturday 2023-12-02 14:46:03 by Octus

Removes Beach Bums, Adds Althland Excavation Pit (#22315)

* replace

* Update lavaland_biodome_beach.dmm

* fixes

* we are so BACK bros

* oh yeah, now were cookin

* turf

* oops!

* Update lavaland.dm

* work you fuck

* donedonedoneeeeeee

---
## [WonderingGodling/My-Mind-Space](https://github.com/WonderingGodling/My-Mind-Space)@[76549ed3bc...](https://github.com/WonderingGodling/My-Mind-Space/commit/76549ed3bcef48920ee848aaee3ac476eb3b36fd)
#### Saturday 2023-12-02 14:55:15 by WonderingGodling

Update content src/site/notes/Skull/Concentrated Brain/Random Thoughts/One Day I Know That You Will Be There One day Ill Focus On The Future Maybe One Day Oh Baby Isnt Life So Fucking Inconsistent.md

---
## [alexminza/semantic-kernel](https://github.com/alexminza/semantic-kernel)@[2733a5574f...](https://github.com/alexminza/semantic-kernel/commit/2733a5574f72980413e339f100dbe4272644888c)
#### Saturday 2023-12-02 15:14:15 by Mark Karle

Python: Import OpenAPI documents into the semantic kernel (#2297)

### Motivation and Context

<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->

This allows us to import OpenAPI documents, including ChatGPT plugins,
into the Semantic Kernel.

### Description

<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
- The interface reads the operationIds of the openapi spec into a skill:
```python
from semantic_kernel.connectors.openapi import register_openapi_skill
skill = register_openapi_skill(kernel=kernel, skill_name="test", openapi_document="url/or/path/to/openapi.yamlorjson")
skill['operationId'].invoke_async()
```
- Parse an OpenAPI document
- For each operation in the document, create a function that will
execute the operation
- Add all those operations to a skill in the kernel
- Modified `import_skill` to accept a dictionary of functions instead of
just class so that we can import dynamically created functions
- Created unit tests

TESTING:
I've been testing this with the following ChatGPT plugins:
- [Semantic Kernel Starter's Python Flask
plugin](https://github.com/microsoft/semantic-kernel-starters/tree/main/sk-python-flask)
- [ChatGPT's example retrieval
plugin](https://github.com/openai/chatgpt-retrieval-plugin/blob/main/docs/providers/azuresearch/setup.md)
- This one was annoying to setup. I didn't get the plugin functioning,
but I was able to send the right API requests
- Also, their openapi file was invalid. The "servers" attribute is
misindented
- [Google ChatGPT
plugin](https://github.com/Sogody/google-chatgpt-plugin)
- [Chat TODO plugin](https://github.com/lencx/chat-todo-plugin)
- This openapi file is also invalid. I checked with an online validator.
I had to remove"required" from the referenced request objects'
properties:
https://github.com/lencx/chat-todo-plugin/blob/main/openapi.yaml#L85

Then I used this python file to test the examples:

```python
import asyncio
import logging

import semantic_kernel as sk
from semantic_kernel import ContextVariables, Kernel
from semantic_kernel.connectors.ai.open_ai import AzureTextCompletion
from semantic_kernel.connectors.openapi.sk_openapi import register_openapi_skill

# Example usage
chatgpt_retrieval_plugin = {
    "openapi": # location of the plugin's openapi.yaml file,
    "payload": {
        "queries": [
            {
                "query": "string",
                "filter": {
                    "document_id": "string",
                    "source": "email",
                    "source_id": "string",
                    "author": "string",
                    "start_date": "string",
                    "end_date": "string",
                },
                "top_k": 3,
            }
        ]
    },
    "operation_id": "query_query_post",
}

sk_python_flask = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"skill_name": "FunSkill", "function_name": "Joke"},
    "payload": {"input": "dinosaurs"},
    "operation_id": "executeFunction",
}
google_chatgpt_plugin = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "query_params": {"q": "dinosaurs"},
    "operation_id": "searchGet",
}

todo_plugin_add = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo": "finish this"},
    "operation_id": "addTodo",
}

todo_plugin_get = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "operation_id": "getTodos",
}

todo_plugin_delete = {
    "openapi":  # location of the plugin's openapi.yaml file,
    "path_params": {"username": "markkarle"},
    "payload": {"todo_idx": 0},
    "operation_id": "deleteTodo",
}


plugin = todo_plugin_get # set this to the plugin you want to try

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

kernel = Kernel(log=logger)
deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
kernel.add_text_completion_service(
    "dv", AzureTextCompletion(deployment, endpoint, api_key)
)

skill = register_openapi_skill(
    kernel=kernel, skill_name="test", openapi_document=plugin["openapi"]
)
context_variables = ContextVariables(variables=plugin)
result = asyncio.run(
    skill[plugin["operation_id"]].invoke_async(variables=context_variables)
)
print(result)
```

### Contribution Checklist

<!-- Before submitting this PR, please make sure: -->

- [ ] The code builds clean without any errors or warnings
- [ ] The PR follows the [SK Contribution
Guidelines](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
and the [pre-submission formatting
script](https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md#development-scripts)
raises no violations
- [ ] All unit tests pass, and I have added new tests where possible
- [ ] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <abharris@microsoft.com>

---
## [modernuo/ModernUO](https://github.com/modernuo/ModernUO)@[e9d6460e7c...](https://github.com/modernuo/ModernUO/commit/e9d6460e7c42fa2223d335e03905c6403e4d51df)
#### Saturday 2023-12-02 17:54:16 by markhannaway

misc fixes:
* fix players under the affect of pain spike, wouldn’t take extra damage from evil omen
* fix paralyze spell wouldnt work against targets with higher than 110.1 magic resist
* Curse spell OSI accurate:  duration should be refreshed when a new curse spell is cast and it would expire further in the future, else it should fizzle when the targets current curse affliction is more powerful
* fix mana vampire wouldn’t drain the maximum amount of mana from the target, if the caster had a large amount of mana remaining

---
## [TheBronJameOffical/lobotomy-corp13](https://github.com/TheBronJameOffical/lobotomy-corp13)@[21b0cb111b...](https://github.com/TheBronJameOffical/lobotomy-corp13/commit/21b0cb111be6eeac24f15807e949570e2b415383)
#### Saturday 2023-12-02 18:17:13 by The Bron Jame Offical

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
## [NL0bP/ReClassEx](https://github.com/NL0bP/ReClassEx)@[e4450bcf86...](https://github.com/NL0bP/ReClassEx/commit/e4450bcf8673e3ffa3f05c87b3b1e03b970b6f1d)
#### Saturday 2023-12-02 18:23:02 by user1

I added some changes to make the generated classes compile properly without having to be manually reordered.

Summary:

* When the 'generate' button is clicked, each class is added to a Class Dependency Graph, and each class that class references is added as a depenedency.
* There are two dependency types - POINTER and INSTANCE.
    * POINTER references can be solved with a forward declaration.  However, a simple reordering can solve that dependency and limit the forward declaration spam at the top of the generated file.
    * INSTANCE references can only be solved with reordering.  If class B contains an instance of class A, A must come before B in the generated file, no way around it.
* The graph is then recursively traversed - starting at nodes with no dependencies - with classes being added to the 'ordered' class collection.
* Circular dependencies (A points to B points to C points to A) are solved with forward declarations (C comes before B comes before A, with A being forward declared)
* The result is the output has fewer forward declarations and classes don't need to be manually reordered.  In my DayZ Reclass file (which inspired this work, because it takes me a lot of time manually reordering every time I generate the output) there are only 5 forward declarations with 356 classes.

Details:

The graph class itself is pretty simple.  It maintains a mapping of CNodeClass pointers to DependencyNodes.  Each node knows what class it represents, and has two vectors of edges - incoming edges (another class depends on this one) and outgoing edges (this class depends on another).  Each edge knows what node it points to, as well as whether the dependency is of POINTER or INSTANCE type.

Edges are generated by walking each node in a class and adding a dependency edge for each pointer, instance, instance array, and pointer array.  Parallel edges (duplicates) are not added, nor are simple recursive edges (a class has a pointer to an instance of that same class).  Other types (function ptrs?  Can we prototype those in ReClass?) may be necessary here, but these were all I could figure out without asking someone.

ClassDependencyGraph            depGraph;
    // Add each class as a node to the graph before adding dependency edges
    for (auto cNode : this->m_Classes) {
        depGraph.AddNode(cNode);
    }
    for (auto cNode : this->m_Classes) {
        for (size_t n = 0; n < cNode->NodeCount(); n++)
        {
            CNodeBase* pNode = (CNodeBase*)cNode->GetNode(n);
            NodeType Type = pNode->GetType();
            switch (Type) {
            case(nt_pointer):
            {
                CNodePtr* pPointer = (CNodePtr*)pNode;
                CNodeClass* pointerClass = pPointer->GetClass();
                depGraph.AddEdge(cNode, pointerClass, DependencyType::POINTER);
                break;
            }
            case(nt_instance):
            {
                CNodeClassInstance* pClassInstance = (CNodeClassInstance*)pNode;
                CNodeClass* instanceClass = pClassInstance->GetClass();
                depGraph.AddEdge(cNode, instanceClass, DependencyType::INSTANCE);
                break;
            }

            case(nt_array):
            {
                CNodeArray* pArray = (CNodeArray*)pNode;
                CNodeClass* instanceClass = pArray->GetClass();
                depGraph.AddEdge(cNode, instanceClass, DependencyType::INSTANCE);
                break;
            }

            case(nt_ptrarray):
            {
                CNodePtrArray* pArray = (CNodePtrArray*)pNode;
                CNodeClass* pointerClass = pArray->GetClass();
                depGraph.AddEdge(cNode, pointerClass, DependencyType::POINTER);
                break;
            }
            }
        }
    }

Ordering dependencies in the graph is simple in naive cases.  Just start at nodes that have no dependencies (leaf nodes) and recursively visit dependencies, adding them to an ordered class vector as you go.  This works great until you hit circular dependencies - you'd recurse until death.  That's where forward declarations are needed.  If you hit a node that is already being processed, you know you've thrown that ass in a circle.  So that's when you throw your hands up and forward declare - but you can only do that for a POINTER dependency, not an INSTANCE one.

You can see in this graph that DayZPlayer instances Entity which points to physicsObject which points to DayZPlayer.  And if that's the order you hit the nodes in, you're fine - just forward declare DayZPlayer.  However, there exists a path from gpWorld -> World -> N0000120E -> Entity -> PhysicsObject -> DayZPlayer -> Entity.  In that case, when you realize you're in a cycle you're at an INSTANCE dependency and you can't solve it with a forward declaration.

I wasn't sure what the correct way to handle this was, so I kind of improvised a solution.  At the beginning of graph solving, all nodes which have incoming INSTANCE type dependencies are marked.  Then, when they're visited during recursion, if they're being visited across a POINTER dependency edge, they're forward declared and not processed further.  So when you hit gpWorld -> World -> N0000120E -> Entity, it knows Entity has incoming INSTANCE dependencies, so instead of recursing and ending up in DayZPlayer, it adds a forward declaration for Entity and bails out.  Then, later (and along a different path that doesn't go through Entity), DayZPlayer is visited normally and it recurses into Entity, and all is well.

With forward declarations generated and the classes in dependency order, output goes on as normal, except instead of iterating of m_Classes, it iterates over the set of forward declarations and the in-order vector of classes instead.

To generate the visualized graph, I put a ToDot method in the DependencyGraph, which generates a GraphViz Dot representation of the graph.  I left it in as it may end up being useful in troubleshooting in the future.

---
## [JebbJabroni/hsmusic-media](https://github.com/JebbJabroni/hsmusic-media)@[6dd219ac1c...](https://github.com/JebbJabroni/hsmusic-media/commit/6dd219ac1c5472d4e9f3d35a7647703b9992b0a2)
#### Saturday 2023-12-02 18:41:30 by JebbJabroni

Xszelor Albums Assets

Assets for the albums Demo 2019-2021 (Vicious Valor),  Army of the wicked God,  Remains of formed pain, Grim chain of feast, War Marks, Legion, Rites of Bloodgrinded, His Honorable Tyranny, Genesis Genocide, Faces of Oglogoth, Jugglanoids From Outer Space​/​First Interdimensional Clown Chronicles Volume One [UNRELEASED COMPILATION] and Face of Oglogoth - cover LP

---
## [distributivgesetz/tgstation](https://github.com/distributivgesetz/tgstation)@[1b8bcd0365...](https://github.com/distributivgesetz/tgstation/commit/1b8bcd0365ac210701605d19dd549e1b97c13ae9)
#### Saturday 2023-12-02 19:40:55 by lizardqueenlexi

Basic drones (#79109)

## About The Pull Request

Fixes #68825
Fixes #72249
Fixes #70184

Converts maintenance drones to use the basic mob framework. As drones
don't use AI, this was mostly a perfunctory conversion, but I took the
opportunity to clean up drone code a bit and fixed a few bugs.

Noteworthy changes:
- Drones now have a `can_unhack` field. This is set to FALSE on
syndrones, because unhacking them doesn't make them stop being evil but
does cause some weirdness. Syndrones are unused right now, but you never
know.
- Drones use the Dextrous component for hand-having.
- Drones no longer have an internal ID card, instead being given
all-access with the `simple_access` component.
- Picking up drones now works the same as for other mobs, instead of
pointlessly copying the code into `attack_hand`. As a consequence, it is
now possible to punch drones if you want to for some reason.
- Drones can now reboot/cannibalize dead drones without being in combat
mode.
- Cannibalizing a drone that contains a client no longer runtimes - the
client is ghosted ahead of time.
- Drones now have TRAIT_ADVANCEDTOOLUSER, allowing them to properly
interact with machines.
- Trying to screwdriver a dead drone now gives a balloon alert about why
you can't do that.

In addition to these changes, I cleaned up the code quite a bit,
organizing things better and placing more useful comments throughout.
And removing a hell of a lot of single-letter variable names.

I will note that this PR does _not_ address #72129. The issue there is
that sprites for drones-as-hats are entirely nonexistent, and I'm not a
spriter. It shouldn't be too hard to fix if someone makes dronehat
sprites, though!

## Why It's Good For The Game
Kills 8 more simple animals.

In addition to that, drones were clearly a bit neglected, so this fixes
them up a bit and makes the code a little bit clearer. Maybe not that
much clearer, but it's something. It certainly leaves them in a better
place for further work if anyone wants to do that. Plus, a bunch of bugs
and other jankiness are fixed now, which is nice.

## Changelog
:cl:
refactor: Maintenance Drones now use the basic mob framework. This
shouldn't come with any noticeable gameplay changes, but please report
any bugs.
fix: Drones can now interact normally with electrified doors.
fix: Drones' built-in tools can no longer be placed in storage objects
and/or thrown on the floor.
fix: Drones can now perform right-click interactions correctly, such as
deconstructing reinforced windows.
fix: Drones can now reboot or cannibalize other drones without being in
combat mode.
/:cl:

---
## [QeianTEA/MapCommander](https://github.com/QeianTEA/MapCommander)@[d84b5eba10...](https://github.com/QeianTEA/MapCommander/commit/d84b5eba105d576153ae520b4bfebcf89bf75490)
#### Saturday 2023-12-02 20:17:56 by Qeian

You can take items now
well done
You cant drop it though fuck you

---
## [sitshawon/apps](https://github.com/sitshawon/apps)@[f876a48df7...](https://github.com/sitshawon/apps/commit/f876a48df7071c9d3d4f257378337eb75652ed2e)
#### Saturday 2023-12-02 20:22:04 by sitshawon

++*[[LIVESTREAMs!]] Garcia vs Duarte LIVE ON TV Channel

03sec ago~ Upgrade your sports-watching Garcia v Duarte Live Stream | Fight Night experience with our exclusive live streaming offers – the future of fandom is here! Saturday 12.02.2023 at 09:00 PM ET: Garcia v Duarte

STREAMING==►► https://tinyurl.com/5n77h9t5


GO LIVE==► https://tinyurl.com/5n77h9t5

Boxing steeped in history still garners attention during major fights and championship bouts. Garcia v Duarte Auto racing particularly NASCAR events draws fans for the adrenaline rush of high-speed competition.
His resignation was communicated through a statement on his personal website. Garcia v Duarte Regional restrictions might affect access to the game.
Motorsports enthusiasts eagerly anticipate events like the Indy 500 for adrenaline-pumping races. Garcia v Duarte Examining the 49ers' position in the NFC playoff scenario during Week 13's critical matchups:
Motorsports enthusiasts flock to events like the Indy 500 for thrilling races. Garcia v Duarte The semifinals posed a significant test resulting in a 26-20 triumph over King for the Bulldogs.
The Boxing featuring 32 teams stands as a cornerstone of professional football. Garcia v Duarte Evaluating the 49ers' position in the NFC playoff scenario during Week 13's critical matches:
Forest Hills Central demonstrated versatility securing wins through various strategies in the playoffs. Garcia v Duarte American football renowned for its physicality and strategy remains a beloved sport.
Gymnastics events showcasing acrobatic feats captivate audiences with displays of grace and strength. Garcia v Duarte The WNBA (Women's National Basketball Association) is instrumental in promoting women's basketball at a professional level.
San Francisco's recent performance propels them to the NFC's No. 2 seed post the Lions' loss to the Packers. Garcia v Duarte The school maintained they did not terminate him; instead he didn't apply to renew his contract post-season.
CrossFit competitions challenge participants in multiple areas of fitness and endurance. Garcia v Duarte Today's match holds immense significance as it determines the Michigan Division 3 state champion in high school football.
A Supreme Court ruling favored Kennedy with a 6-3 majority on June 27 2022. Garcia v Duarte Last season's finalists the Rangers aim to surpass their prior performance and clinch victory this time.

The clash between Ryan Garcia and Oscar Duarte has left fans on the edge of their seats, eagerly awaiting the intense lightweight showdown. This article delves into the details of the much-anticipated fight, analyzing the fighters' strengths, strategies, and previous performances. Sit back, relax, and get ready for a thrilling and action-packed encounter in the ring. Ryan Garcia: Rising Star of the Lightweight Division Ryan Garcia, commonly referred to as "The Flash," has quickly risen through the ranks of the lightweight division. Known for his blinding speed, dynamic footwork, and a devastatingly accurate left hook, Garcia has captured the attention of boxing enthusiasts worldwide.
Garcia's Unmatched Speed and Precision Garcia's lightning-fast hands and exceptional hand-eye coordination give him a distinct advantage in the ring. His ability to land clean and powerful shots has earned him numerous knockout victories throughout his career.

A Formidable Offense Garcia's offensive prowess extends beyond his unmatched speed. His precise timing and ring intelligence enable him to set up his opponents, unleashing a barrage of devastating combinations that often leave them reeling. Additionally, his knack for delivering powerful body shots further adds to his already formidable punching arsenal. Oscar Duarte: A Worthy Challenger While Garcia may steal the spotlight, Oscar Duarte stands as a worthy opponent, ready to demonstrate his skills and prove himself against the rising star. Duarte's Technical Proficiency Duarte is known for his technical proficiency and strategic approach to the sport. He possesses a solid defense, relying on well-timed counters and a high guard to deflect incoming punches.

Duarte's ability to read his opponents and exploit their weaknesses is a key aspect of his fighting style. The Dominance of Duarte's Jabs Duarte's jabs are a notable weapon in his arsenal. With precision and accuracy, he peppers his opponents with jabs, setting up combinations and maintaining distance. His jabs often dictate the pace of the fight and keep his opponents at bay. Clash of Styles: Speed vs Technique The Garcia-Duarte bout promises to be a captivating clash of styles. Garcia's lightning-fast speed and explosive offense collide with Duarte's technical prowess and defensive finesse. The Power of Speed Garcia's ability to move swiftly in and out of range is likely to pose a significant challenge to Duarte. His lightning-fast speed may overwhelm his opponent, making it difficult for Duarte to mount a sustained defense.

Duarte's Precision and Strategy On the other hand, Duarte's technical proficiency and strategic approach could neutralize Garcia's speed to some extent. If Duarte can effectively read and counter Garcia's punches, the fight could take on a different dynamic, potentially unsettling the rising star. Predictions for the Fight Speculation and anticipation surround the outcome of the Garcia-Duarte bout. While it is impossible to predict the future with certainty, analyzing the fighters' previous performances can provide some insights. Factors Favoring Garcia Garcia's incredible speed, extraordinary punching power, and offensive skills make him the favorite going into the fight. Given his recent victories and ascent in the lightweight division, Garcia has the momentum and confidence to secure another significant win.

Duarte's Strengths as an Underdog However, Duarte should not be underestimated. His technical proficiency, defensive capabilities, and strategic approach could present a challenge for Garcia. If Duarte can successfully execute his game plan and exploit Garcia's weaknesses, he has the potential to surprise his opponent and the boxing world. In Conclusion The highly anticipated showdown between Ryan Garcia and Oscar Duarte promises an enthralling battle between speed and technique. Garcia's lightning-fast hands and devastating offense clash with Duarte's technical prowess and strategic finesse. As the fight approaches, boxing fans around the world eagerly await the outcome, ready to witness a memorable encounter in the lightweight division.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[41d659378d...](https://github.com/git-for-windows/git/commit/41d659378daed04aeb737da109c7b3f296939db5)
#### Saturday 2023-12-02 21:08:15 by Johannes Schindelin

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
## [mosra/magnum-extras](https://github.com/mosra/magnum-extras)@[b17f6f9125...](https://github.com/mosra/magnum-extras/commit/b17f6f9125cbfdb6b4fe2e14ae875aaa1f8c96dc)
#### Saturday 2023-12-02 21:28:03 by Vladimír Vondruš

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
## [darylmokolo737/Cyber-security-Pentest-](https://github.com/darylmokolo737/Cyber-security-Pentest-)@[195eedab26...](https://github.com/darylmokolo737/Cyber-security-Pentest-/commit/195eedab2637c6d2ebe837a04371a398de4a7efb)
#### Saturday 2023-12-02 21:35:31 by darylmokolo737

Add files via upload

 This Pentest report for MegaCorp's Jupyter Notebook deployment was a thrilling adventure in the world of network security. The absence of intentional CVEs sparked creativity, pushing me to think outside the box and apply my security knowledge in a hands-on setting. Navigating security misconfigurations with tools like port forwarding and dynamic proxying added a dynamic layer, reinforcing the importance of understanding the threat model within defined engagement rules.

The real gem of the experience was the challenge of conducting a reconnaissance attack without relying on brute force tactics. It demanded a strategic approach, delving deep into the network architecture and discovering potential weak points. Overcoming this challenge not only enhanced my skills in information gathering but also made the entire lab a fun and enriching endeavor.

To my fellow learners and readers, thanks for joining me on this exciting journey into network hacking. The lessons learned in this lab aren't just about overcoming challenges; they're like power-ups leveling up our collective cybersecurity expertise. Your enthusiasm and engagement make the adventure even more rewarding. Happy hacking, and a huge thank you for being part of the ride! 🚀

---
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[30dae8899b...](https://github.com/Donglesplonge/tgstation/commit/30dae8899bad0007ae9220f1fc10be16908dd1a9)
#### Saturday 2023-12-02 21:39:00 by Kyle Spier-Swenson

fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#79783)

This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

---
## [TheWolfbringer/tgstation](https://github.com/TheWolfbringer/tgstation)@[b65f729901...](https://github.com/TheWolfbringer/tgstation/commit/b65f729901fdb342b832fb3365d72afd076f8c3b)
#### Saturday 2023-12-02 22:07:25 by lizardqueenlexi

Nanotrasen basic mobs. (#78917)

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

---
## [Timberpoes/tgstation-nxt](https://github.com/Timberpoes/tgstation-nxt)@[c00f7d53a3...](https://github.com/Timberpoes/tgstation-nxt/commit/c00f7d53a32801b7afd923f268da30fb2f99bbd5)
#### Saturday 2023-12-02 23:12:43 by MGOOOOOO

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
## [andras204/Hungrush](https://github.com/andras204/Hungrush)@[602b0844d2...](https://github.com/andras204/Hungrush/commit/602b0844d2340833439adaae2d0ebe307f9d7f51)
#### Saturday 2023-12-02 23:38:25 by Alaa

Kill me V2

Annoying ass error, fixed delivery setters and getters

Note to self: learn how to use github properly

---
## [cyphar/runc](https://github.com/cyphar/runc)@[dbcb5ea689...](https://github.com/cyphar/runc/commit/dbcb5ea6899694a78ae69bf92828ebdc939619fe)
#### Saturday 2023-12-02 23:45:52 by Aleksa Sarai

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
## [calblueprint/impact-fund](https://github.com/calblueprint/impact-fund)@[d9e37dc872...](https://github.com/calblueprint/impact-fund/commit/d9e37dc872091b3b7e29615c2583a8854d1e2d9c)
#### Saturday 2023-12-02 23:57:02 by Philip Ye

[QRCodeScanner] Fixed Scan Issues and Supabase Queries 

* fixed some issues, useEffect being weird

* fuck you ESLINT

* fixed thing

* fixed some issues, useEffect being weird

* fuck you ESLINT

* fixed thing

* hello, fixed toast thing

---

