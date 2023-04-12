## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-11](docs/good-messages/2023/2023-04-11.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,009,105 were push events containing 3,094,740 commit messages that amount to 244,056,522 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 56 messages:


## [dagster-io/dagster](https://github.com/dagster-io/dagster)@[aba0a8090d...](https://github.com/dagster-io/dagster/commit/aba0a8090dff5651dbecf43752628e01c40e65c0)
#### Tuesday 2023-04-11 00:19:00 by OwenKephart

[asset-reconciliation] Use source asset observations to inform when to kick off eager reconciliation (#13304)

## Summary & Motivation

We did a similar sort of thing for data time calculations.

Note the TODO. The material impact is the following. Imagine you have an
asset graph `OS -> A -> B`, where OS is an observable source asset.

- Your asset_selection for your sensor is just `B`.
- `OS` is observed having version `1`, after which all downstreams are
materialized in order.
- `A` is manually materialized again (not pulling in any new data, as no
version was updated).
- `OS` is observed, still having version `1`.

The sensor will see that `A` has a new materialization, but will
erroneously treat it as "unreconciled", as a new observation record has
come in after the latest materialization of `A`. This means that a
materialization of `B` will not be kicked off.

In a fun twist of fate, this is actually arguably desirable behavior, as
there really isn't a reason for `B` to be kicked off in this scenario.
However, we're kinda getting the right answer for the wrong reason, if
that makes sense. We don't factor this sort of versioning information
into other parts of the reconciliation logic, and the following sequence
of events would give us an unambiguously incorrect behavior:

- `OS` is observed having version `1`, after which all downstreams are
materialized in order.
- `A` is manually materialized again (not pulling in any new data, as no
version was updated).
- `OS` is observed, now having version `2`.
- `A` is manually materialized again.
- `OS` is observed again, still having version `2`.

In this case, we get the same behavior (`B` not getting kicked off),
because there is an observation record after the most recent
materialization of `A` (this is the same reason as before).

In reality, we should search backwards for the FIRST occurrence of the
current version, this was just a minor pain to implement in the time I
have today.

## How I Tested These Changes

---
## [Seldom-SE/Archipelago](https://github.com/Seldom-SE/Archipelago)@[6d13dc4944...](https://github.com/Seldom-SE/Archipelago/commit/6d13dc494455bef97e0f1afc8928853f71d5b5ad)
#### Tuesday 2023-04-11 00:23:22 by el-u

lufia2ac: new features, bug fixes, and more (#1549)

### New features

- ***Architect mode***
  Usually the cave is randomized by the game, meaning that each attempt will produce a different dungeon. However, with this new feature the player can, between runs, opt into keeping the same cave. If activated, they will then encounter the same floor layouts, same enemy spawns, and same red chest contents as on their previous attempt.   

- ***Custom item pool***
  Previously, the multiworld item pool consisted entirely of random blue chest items because, well, the permanent checks are blue chests and that's what one would normally get from these. While blue chest items often greatly increase your odds against regular enemies, being able to defeat the Master can be contingent on having an appropriate equipment setup of red chest items (such as Dekar blade) or even enemy drops (such as Hidora rock), most of which cannot normally be obtained from blue chests.
  With the custom item pool option, players now have the freedom to place any cave item into the multiworld itempool for their world.

- ***Enemy floor number, enemy sprite, and enemy movement pattern randomization***
  Experienced players can deduce a lot of information about the opposition they will be facing, for example: Given the current floor number, one can know in advance which of the enemy types will have a chance to spawn on that floor. And when seeing a particular enemy sprite, one can already know which enemy types one might have to face in battle if one were to come in contact with it, and also how that enemy group will move through the dungeon.
  Three new randomization options are added for players who want to spice up their game: one can shuffle which enemy types appear on which floor, one can shuffle which sprite is used by which enemy type, and one can shuffle which movement pattern is used by which sprite.

- ***EXP modifier***
  Just a simple multiplier option to allow people to level up faster. (For technical reasons, the maximum amount of EXP that can be awarded for a single enemy is limited to 65535, but even with the maximum allowed modifier of 500% there are only 6 enemy types in the cave that can reach this cap.)


### Balance change

- ***proportionally adjust chest type distribution to accommodate increased blue chest chance***
  One of the main problems that became apparent in the current version has to do with the distribution of chest contents. The game considers 6 categories, namely: consumable (mostly non-restorative), consumable (restorative), blue chest item, spell, gear, and weapon. Since only blue chests count as multiworld locations, we want to have a mechanism to customize the blue chest chance.
  Given how the chest types are detetermined in game, a naive implementation of an increased blue chest chance causes only the consumable chance to be decreased in return. In practice, this has resulted in some players of worlds with a high blue chest chance struggling (more than usual) to keep their party alive because they were always low on comsumables that restore HP and MP.
  The new algorithm tries to avoid this one-sided effect by having an increase in blue chest chance resulting in a decrease of all other types, calculated in such a way that the relative distribution of the other 5 categories stays (approximately) the same.


### Bug fixes

- ***prevent using party member items if character is already in party***
  This should have been changed at the same time that 6eb00621e39c930f5746f5f3c69a6bc19cd0e84a was made, but oh well... 

- ***fix glitched sprite when opening a chest immediately after receiving an item***
  When opening a chest right after receiving a multiworld item (such that there were two item get animations in the exact same iteration of the game main loop), the item from the chest would display an incorrect sprite in the wrong place. Fixed by cleaning up some relevant memory addresses after getting the multiworld item.

- ***fix death link***
  There was a condition in `deathlink_kill_player` that looked kinda smart (it checked the time against `last_death_link`), but actually wasn't smart at all because `deathlink_kill_player` is executed as an async task and the main thread will update `last_death_link` after creating the task, meaning that whether or not the incoming death link would actually be passed to the game seems to have been up to a race condition. Fixed by simply removing that check.


### Other

- ***add Lufia II Ancient Cave (and SMW) to the network diagram***
  These two games were missing from the SNES sector.

- ***implement get_filler_item_name***
  Place a restorative consumable instead of a completely random item. (Now the only known problem with item links in lufia2ac is... that noone has ever tested item links. But this should be an improvement at least. Anyway, now #1172 can come ;)
  And btw., if you think that the implementation of random selection in this method looks weird, that's because it is indeed weird. (It tries to recreate the algorithm that the game itself uses when it generates a replacement item for a chest that would contain a spell that the party already knows.)

- ***store all options in a dataclass***
  This is basically like using #993 (but without actual support from core). It makes the lufia2ac world code much nicer to maintain because one doesn't have to change 5 different places anymore when adding or renaming an option.

- ***remove master_hp.scale***
  I have to admit: `scale` was a mistake. Never have I seen a single option value cause so many user misconceptions. Some people assume it affects enemies other than the Master; some people assume it affects stats other than HP; and many people will just assume it is a magic option that will somehow counterbalance whatever settings combination they are currently trying to shoot themselves in the foot with.
  On top of that, the `scale` mechanism probably doesn't provide a good user experience even when used for its intended purpose (since having reached floor XY in general doesn't mean you will have the power to deplete XY% of the Masters usual HP; especially given that, due to the randomness of loot, you are never guaranteed to be able to defeat the vanilla Master even when you have cleared 100% of the floors).
  The intended target audience of the `master_hp` option are people who want to fight the Master (and know how to fight it), but also want to lessen (to a degree of their choosing) the harsh dependence on the specific equipment setups that are usually required to win this fight even when having done all 99 floors. They can achieve this by setting the `master_hp` option to a numeric value appropriate for the level of challenge they are seeking. Therefore, nothing of value should be lost by removing the special `scale` value from the `master_hp` option, while at the same time a major source of user confusion will be eliminated.

- ***typing***
  This (combined with the switch to the option dataclass) greatly reduces the typing problems in the lufia2ac world. The remaining typing errors mostly fall into 4 categories:
  1. Lambdas with defaults (which seem to be incorrectly reported as an error due to a mypy bug)
  1. Classmethods that return instances (which could probably be improved using PEP 673 "Self" types, but that would require Python 3.11 as the minimum supported version)
  1. Everything that inherits from TextChoice (which is a typing mess in core)
  1. Everything related to asar.py (which does not have proper typing and lies outside of this project)

## How was this tested?

https://discord.com/channels/731205301247803413/1080852357442707476 and others

---
## [CliffracerX/Skyrat-tg-PRs](https://github.com/CliffracerX/Skyrat-tg-PRs)@[7de062f78e...](https://github.com/CliffracerX/Skyrat-tg-PRs/commit/7de062f78e696a11984b134ac6bfca6ca414cc89)
#### Tuesday 2023-04-11 00:47:38 by SkyratBot

[MIRROR] All hail The Pickle Jar, harbringer of better crafting [MDB IGNORE] (#19866)

* All hail The Pickle Jar, harbringer of better crafting (#73939)

## About The Pull Request
Fixes #73841

---

_It is the 12th of March, 2023. Around 3am. I have published a Pull
Request which involves circuits, and got reminded of my low GBP. I go
into the issues tab to see if there's anything someone of my low skill
caliber could tackle. I see it; Pickles.
"How hard could I be?" I ask myself, foolishly unaware of the dangers
that would soon overcome me.
Surely it must've been a mistype, I thought. Surely someone accidentally
confused pickles and cucumbers.
"Wait, the pickles are supposed to be created on the jar when the jar is
created", I say foolishly.
"Wait, its putting the ingredients used for the jar in the jar, that
doesn't explain why the pickles aren't there though", I say foolishly
"Wait, whoever tried fixing this earlier fucking qdel'd the beaker and
called it a day????", I say, foolishly._

---

Anyways I changed how the crafting menu distincts between categories,
instead of checking whether or not the path is for food, it checks the
actual categories themselves (why didn't it do this already), meaning
that you can have non-food items on the food tab if it has a food
category. Did this by adding a list that includes all crafting
categories, so in the future when adding new categories you'll have to
add them twice, which sucks, but oh well.

Also added a new variable to craftable items, which makes it so that you
can not delete a container's contents if you so wish (why was this the
default).

All this so that when you craft pickles, it actually crafts pickles
instead of cucumbers.

I spent hours on this, its 6:30am as I'm typing this. I'm tired. Fucking
pickles.

Super duper ultra thanks to FinalPotato for guiding me and suffering
with me through this and teaching me so much about DM and BYOND. I
cannot emphasize just how helpful and awesome they were thank you thank
you thank you <3
## Why It's Good For The Game

Bug fixing be good
## Changelog
:cl:
fix: The jar of pickles, after millenia, finally actually contains
pickles. All hail the jar of pickles.
/:cl:

* All hail The Pickle Jar, harbringer of better crafting

---------

Co-authored-by: TheSmallBlue <ilanmori@hotmail.com>

---
## [CliffracerX/Skyrat-tg-PRs](https://github.com/CliffracerX/Skyrat-tg-PRs)@[4a9407438a...](https://github.com/CliffracerX/Skyrat-tg-PRs/commit/4a9407438aa216789e72a4dec8d6588582d91a8e)
#### Tuesday 2023-04-11 00:47:38 by SkyratBot

[MIRROR] You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed [MDB IGNORE] (#19855)

* You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed (#73983)

## About The Pull Request

If you are restrained, and placed into an unlocked labor camp
teleporter, you cannot instantly resist out of it. However the resist
timer is cut in half while unlocked.

## Why It's Good For The Game

Getting someone into the gulag teleporter is an incredibly un-necessary
pain in the rear because simply *spamming resist* turns it into a game
where you have to shove them in, then really quick go over to the
computer and slam the lock button. This is... kinda lame. A lot of new
player security officers get got by this, and I think it's sad. Inb4
"Skill issue"

## Changelog

:cl: Melbert
balance: If you are handcuffed, you can't instantly resist out of an
unlocked labor camp teleporter (however, resist time is halved).
/:cl:

* You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[11cbbba018...](https://github.com/Singul0/tgstation/commit/11cbbba018e861237ce4bed73f19b58874c22042)
#### Tuesday 2023-04-11 01:04:38 by Sol N

Replaceable Traitor Uplinks (#74315)

## About The Pull Request

Following [from the suggestion in this hackmd
](https://hackmd.io/IkDWWkpfQa2lkdevsnLqhA?view#Replacement-Uplinks)with
a few twists of my own, I have made a method for traitors to acquire a
replacement traitor uplink that has its own set of flaws and limiters in
order to prevent abuse.


![ZC0WYDFRzc](https://user-images.githubusercontent.com/116288367/228101432-9352390b-9538-4c62-8dc4-55e2e798c466.png)

The basic pitch is as follows, all traitors now start with a new,
crafting recipe exclusive to them, it costs a teleport beacon, a
bluespace crystal, and some iron and cable coil, and then allows them to
build a static, dense machine that they can synchronize with, which
allows the machine to know what signal it should be looking out for from
the traitor.

![dreamseeker_iErI3vju0C](https://user-images.githubusercontent.com/116288367/228094286-c2bca198-82cd-4ce0-a4a7-c26c24a9327c.gif)

The traitor then uses any radio, sets it to the frequency that has been
added to their static antagonist ui, and then speaks their codeword,
also in the ui, and then a few things happen.

![dreamseeker_gbzSFeHuS5](https://user-images.githubusercontent.com/116288367/228094354-a649c713-f013-4ac2-b8d7-0754a852f987.gif)

Most obviously, they get a replacement uplink that is in the conspicuous
shape of the nukie or lone op uplink. This uplink can be unlocked by
speaking your replacement codeword to it again, it remembers your
previous TC amount and locks all other uplinks associated with your
uplink handler(they can then be unlocked as normal). It also destroys
any other replacement uplinks associated with your uplink handler, which
means you can never have more than one replacement uplink.

This means that if your uplink has been confiscated and you left it
unlocked, if it hasn't been emptied out you can continue from where you
were, and if you want to get back on the TC grind you won't lose the new
TC to whoever stole your uplink. Of course, the new uplink can not be
locked, so you have to be more careful with it or buy an uplink implant
and destroy it. You can destroy your replacement uplink with a
screwdriver right click, same for the machine.

Additionally, the Syndicate Uplink Beacon has another quirk to it, which
is that the teleporter beacon used to create it is intact, which means
people eagle eyed on the teleporter console could go find you, not to
mention that if you use an existing teleporter beacon, someone might
notice its gone missing...

oh also while making the replacement uplink i found a bug caused by a
recent pr that broke debug uplinks due to them not having a purchase
log. thats fixed too

## Why It's Good For The Game

It can be easy to lose your uplink, and as a traitor having your uplink
confiscated, even if it is locked, feels really bad. While the old
traitor objectives were added back to prog traitor to prevent situations
where a confiscated uplink meant that you were completely aimless, I
think that having a backup solution would be good for more inexperienced
traitors or for ones who get unlucky.

Hopefully this is generally balanced well enough but there are a few
levers that can be pulled, but overall I do think that making it so that
traitors can always get a chance to get an uplink and do some objectives
is good for the game. I like the idea of someone getting perma'd,
someone breaks them out, they both craft a new uplink beacon, and then
they go back and get the traitors old gear with stuff they got from the
new uplink, I think that's a cool possibility to throw into the sandbox.

## Changelog
:cl:
add: Added new syndicate uplink beacon and associated systems that allow
you to get a replacement traitor uplink
fix: Debug & nukie uplinks no longer runtime and work properly again
/:cl:

---
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[00f8bcfe75...](https://github.com/Singul0/tgstation/commit/00f8bcfe75275b7452063d1d8ec75d4c8e643f8b)
#### Tuesday 2023-04-11 01:04:38 by MrMelbert

Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances (#74411)

## About The Pull Request

- Signallizes head revolutionary flash conversion code, moving it out of
core flash code.
- Removes "tacticool" flashing from head revs, but they can still
convert from any direction
 
- Fixes April Fools "You son of a bitch! I'm in" force say never
working.
   - Revs are muted on conversion so they couldn't talk.
       - Fixed by only muting revs on non-holidays
   - Cultists are unconscious on conversion so they couldn't talk
       - Fixed by only unconscious-ing cultists on non-holidays
- Brainwash victims are more often than not unconscious / asleep so they
couldn't talk
       - Just left this one. 

- Reduced the chance of them occurring and limits it to April Fools only
- A 1% chance of the force says ocurring means they will happen pretty
much once a week, given multiple rev / cult rounds happen every week and
on average like, 20 people are converted. A little absurd, it's good
that it never worked?

## Why It's Good For The Game

Antag code in core item code is bad

It's funny this meme has existed for like 2, 3 years now? No one's
tested it, it's never worked

## Changelog

:cl: Melbert
refactor: Removes Rev code from core flash code
fix: Getting converted on April Fools now triggers the meme force say as
always intended
del: The meme force say can no longer trigger on any day (it didn't work
before anyways)
/:cl:

---
## [hail-is/hail](https://github.com/hail-is/hail)@[da1115a387...](https://github.com/hail-is/hail/commit/da1115a387bb799991d0ab1416790dacc0b44cbe)
#### Tuesday 2023-04-11 01:04:39 by Daniel Goldstein

[ci] Mirror third-party images and hailgenetics images on deploy (#12818)

- On *deploys*, makes sure that whatever is in our third-party images is
in our private registry before starting builds like hail-ubuntu that
might depend on those images. This means that we can update our ubuntu
base image without the australians needing to deploy any images by hand.
However, this does not run in PRs because I 1) didn't want to add that
kind of latency for PRs and 2) we don't do any kind of namespacing for
our images so if we did include this for a PR that ultimately wasn't
merged we would have to manually remove the image anyway so why not
manually add it if you're going to PR it… I think point 2 is a little
weak but I recall this being what we agreed on a couple months back when
we discussed this. I'm wondering if we should just eat the minute or so
latency at the beginning of PRs to be safe but it also feels like a
shame for something that changes so infrequently.

- Again on deploys, upload the hailgenetics/* images to the private
registry if they don't already exist there. This way any deployments
that aren't hail team's GCP deployment can get these images
automatically when they deploy a new SHA instead of uploading them
manually. It won't backfill skipped versions, but we decided that was
ok. This seems less relevant for testing on PRs as it will get triggered
on releases and we can easily dev deploy to rectify the image if this
breaks.

---
## [Latentish/Shiptest](https://github.com/Latentish/Shiptest)@[0410075cc8...](https://github.com/Latentish/Shiptest/commit/0410075cc811c5f65d7dc085a665c1ebb3a20e44)
#### Tuesday 2023-04-11 01:13:49 by meemofcourse

Ports mothroaches + Moth emotes (#1843)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Can you guess what this PR does? If you answered that it ports [this
pull request](https://github.com/tgstation/tgstation/pull/68763), [this
pull request](https://github.com/tgstation/tgstation/pull/71784), and [a
partial part of this one
too](https://github.com/BeeStation/BeeStation-Hornet/pull/7645/), then
you're right!

![imagen](https://user-images.githubusercontent.com/75212565/227387000-cc205158-286b-4841-9c5a-2e4d6d8d6200.png)

![imagen](https://user-images.githubusercontent.com/75212565/227386830-213997a1-ebe9-4573-8f8e-052e72bacea2.png)


You can also craft moth plushies now. You just need some cloth,
mothroach hide, and a heart!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

silly little moth roaches and emotes, who wouldn't want them in the
game?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Mothroaches are now a thing
add: Moth laughter, chittering and squeaking
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Opbrave/pytorch](https://github.com/Opbrave/pytorch)@[a269469982...](https://github.com/Opbrave/pytorch/commit/a2694699821be04e6a74760ba754911e714a5486)
#### Tuesday 2023-04-11 02:15:45 by Brian Hirsh

aot autograd refactor: make all synthetic base logic layered in a single location (#96235)

This  refactor doesn't significantly change LoC in aot autograd, but I think this nets out to making it clearer (interested in peoples' thoughts).

The idea is that I tried to re-write the part of aot autograd that deals with synthetic bases in a layered way, similar to how Ed wrote the logic for dedup'ing inputs: it happens in one place, and all of the downstream transformation in aot autograd don't have to worry about it.

Specifically, I added a new function `aot_wrapper_synthetic_base`, similar to the existing `aot_wrapper_dedupe`.

The benefit: none of the other code in aot autograd needs to think about synthetic bases (previously, synthetic base code was intertwined in several places).

The downsides: there are two.

(1) `aot_wrapper_synthetic_base()` needs to have its own epilogue. There is one particularly hairy case, where factoring the synthetic base logic to a single location was painful: If you have two inputs that alias each other, where one gets a data mutation, and the other gets a metadata mutation.

Ordinarily, metadata mutations are handled by the runtime epilogue, in `create_runtime_wrapper`. However, now that things are factored this way, the runtime wrapper operates only on synthetic bases instead of operating on the original inputs. For data mutations, it is fine to apply the data mutation to the synthetic base instead of the original input alias. But for metadata mutations, we **need** to apply the metadata mutation directly to the original inputs.

The way that I handled this was by tracking which inputs slot into this specific case (part of a synthetic base, and get metadata mutations), and updateing the flat_fn() that we pass downstream to return these updated inputs as extra outputs. From the perspective of downstream logic, these are real user outputs, that it can treat like any other user outputs. `aot_wrapper_synthetic_base` will know to grab these extra outputs and use them to apply the metadata mutations.

This was pretty annoying, but has the benefit that all of that logic is encapsulated entirely in `aot_wrapper_synthetic_base()`.

(2) input mutations are now performed on the synthetic base instead of the individual aliases.

You can see the original code comment [here](https://github.com/pytorch/pytorch/blob/b0b5f3c6c681896febbd9ff7ad7649b13def345d/torch/_functorch/aot_autograd.py#L1131) for details. We used to do the optimized thing in this case, and now we do the less optimized thing (copying the entire synthetic base, instead of the potentially smaller alias).

To be fair, we had no data showing that this optimization was showing improvements on any models in practice. I also think that the main reason anyone would ever run across this problem is because of a graph break - so if you care about perf, you probably want to avoid the extra graph breaks to begin with. I haven't added any warnings for this, but we probably could depending on what people think.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/96235
Approved by: https://github.com/ezyang

---
## [dwasint/Monkestation2.0](https://github.com/dwasint/Monkestation2.0)@[8d7db532c0...](https://github.com/dwasint/Monkestation2.0/commit/8d7db532c0f425e6cc68d975b526694bbaefc870)
#### Tuesday 2023-04-11 02:27:52 by Bloop

Reworks blood deficiency backend, & some adjustments to slime blood deficiency (#74143)

## About The Pull Request

This is a followup PR to
https://github.com/tgstation/tgstation/pull/73866

Fixes https://github.com/Skyrat-SS13/Skyrat-tg/issues/19991

I had suspected the nutrition loss slimes experience alongside blood
regen might necessitate some tweaks down the line and here we are. This
PR has two parts.

---

**PART I:** _Reworking the blood deficiency quirk backend_

As it is, blood drain from the blood deficiency occurs in the quirk's
subsystem process() call asynchronously to Life(), where the blood regen
occurs.

This results in the blood volume fluctuating constantly, making it
difficult to really make sense of readings and potentially introducing
race conditions. This PR changes that.

The blood deficiency quirk no longer processes and instead has a proc,
`lose_blood(delta_time)`, which is called in the `handle_blood()` proc
at the same time blood gets regenerated.

Added a `get_quirk` proc to help with this, so that we only have to
iterate through the quirks list once for each mob (rather than calling
has_quirk, then locate in quirks... etc).

Added a `TRAIT_BLOOD_DEFICIENCY` to further optimize the code.

---

**PART II:** _Some fine tuning of the slime blood deficiency quirk_

Slime regen works a bit differently than humans such that if they lose
-any- blood whatsoever, they will also lose nutrition. This means that
even if hooked up to an IV they will still become starving rather
quickly. A bit -too- quickly.

Instead, now the hunger does not kick in until `blood_volume` reaches
550. This means that if a slime with the blood deficiency quirk is
hooked up to an IV with say, welding fluid, and has over 150 nutrition,
they will regen blood faster than they lose it from the blood deficiency
quirk. Once they get to over 550 `blood_volume`, they will stop losing
hunger (from blood regen, anyway--normal hunger rate still applies).

So essentially this just allows slimes with the blood deficiency quirk
to be able to function so long as they stay hooked up to their IV's (or
chug welder fluid/some other toxin), which is the intended purpose of
the quirk.

Edit: As a bonus I added new blood bags for the exotic blood types, and
added a proc `update_mail_goodies` which updates the blood deficiency
quirk's mail goodies accordingly (crewmembers with blood deficiency get
sent blood bags, now they will get the correct type if their species
changes). While I was in these files I changed any immediate single
letter vars I could find and cleaned up what I could.


![image](https://user-images.githubusercontent.com/13398309/226739179-a21790e3-0be6-423a-be89-8d2cb84f6149.png)


<details>
<summary>The new blood packs</summary>


![image](https://user-images.githubusercontent.com/13398309/226743543-29fca53d-b3d1-4903-9706-35b2c00bbe78.png)

</details>

## Why It's Good For The Game

-This is arguably a more performant option than before, and fixes race
conditions from `Life()` and `quirk/blooddeficiency/process()` fighting
with one another.

-Adjustments to slime blood deficiency will enable it to function as
intended.

-It is now easier to read health analyzer blood volume readings for
blood deficient mobs.

-Now the correct blood packs are sent in the mail.

## Changelog

:cl:
qol: adjusted the blood deficiency quirk for slimepeople to not cause
excessive hunger as long as blood volume is kept above 550 via an IV
drip (or other means of getting welding fluid/some other toxin etc into
the bloodstream, e.g. ingestion)
qol: speciees with exotic blood types will now receive the correct blood
bag in the mail from having the blood deficiency perk
add: adds new blood bag types: TOX (slimepeople), H2O (podpeople), S
(snail)
fix: fixed blood deficiency quirk causing wild fluctuations in blood
volume on the analyzer, giving more accurate readings
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Offroaders123/jsmediatags](https://github.com/Offroaders123/jsmediatags)@[96411d7603...](https://github.com/Offroaders123/jsmediatags/commit/96411d7603daa48c6c3ba30507e8bb178c64df0d)
#### Tuesday 2023-04-11 02:28:18 by Offroaders123

TS-Jest

Got Jest working with the new TypeScript codebase! I'm very happy that a lot of the tests are still passing, so at least the ESM part is working, that was the biggest hurdle in getting this to work.

This setup is very hacky, with all of the dependencies that it currently requires. I really don't like how much spaghetti code it needs to work with simple ESM TypeScript, how funky haha (Of course, these tools have been around a while before this 'newer' spec, but you'd think that things like this would be more of a vanilla experience to set up by now).

So here's the list of things going on. For simply building the source of the library, I'm only using `tsc`. To *test* the library (this is just for testing, get ready), I'm using Jest. To read the source, that uses Babel. Even with that, it isn't able to run TypeScript. So, I have to use TS-Jest, which depends on both `tsc` and Jest. Neither of these tools (excluding `tsc`) can handle having `.js` extension resolution in TS files, so I had to install a resolver plugin for Jest, which I think resolves the `.js` extension to the actual `.ts` one, since Jest doesn't know, or know how to do that. And because Jest (TS-Jest) doesn't support bare ESM, I think somewhere in there it's compiling the code to CommonJS still, since that's only what it can run? At least I think it's something like that. I don't know. But hey, it's working now! Let's cheers to improving this from here :)

I originally moved the tests back to the `__tests__` and `__mocks__` folders because I thought they had to be there in order for Jest to find them, but turns out the original, new folder structure works perfectly afterall! I'm really glad I looked into seeing if that would still work. I didn't even have to add a path configuration to Jest's config to make it work. Epic.

Next I'm going to work on the unused project dev dependencies, now that things pretty much only use TypeScript and Jest. I'm not sure how I want to handle the React Native and Node file opener tests/typings yet, that's been a hold back since the migration, as I'm not sure how those are fully supposed to work or be used. Rather than removing it, I wanted to leave it as long as possible to figure out how to keep it around, or if I should move it to a new implementation down the road, once I start to modernize the actual codebase.

I'm going to work on adding Promises to the codebase, that's gonna be a huge plus/level up :)

---
## [imd1005-web-development-winter-2023/group-project-digitalists](https://github.com/imd1005-web-development-winter-2023/group-project-digitalists)@[d183a88581...](https://github.com/imd1005-web-development-winter-2023/group-project-digitalists/commit/d183a88581a314a9b88405b9c77bd832bdf3c131)
#### Tuesday 2023-04-11 02:42:59 by oliviascout

remove draw() i fucking GUESS

im so goddamn tired this shit worked before and we dont even have moves or win conditions working yet

---
## [VulpiDev/vulpidev.github.io](https://github.com/VulpiDev/vulpidev.github.io)@[adedc658e2...](https://github.com/VulpiDev/vulpidev.github.io/commit/adedc658e278ec13278e15c61db991fb38762de9)
#### Tuesday 2023-04-11 03:12:15 by Pleysek

Vulpi games v. 1.0 | Realease

This is the biggest version yet (and probably will stay that way)

Added:
- Meta tags for better SEO
- Index.html content - Some more content about this whole website etc,
- Games.html content - For now no games so no bigger content, this will change in the future. Discord image is a url.
- About.html - Includes buttons for About, FAQ, Awards, other. Every button displays different text. The state you left on is saved in Local Storage (Cool, right :+1:)
- Added logos, images, discord logo, mail logo,
- Added footer, now you can see the disclaimer about copyright, contact methods and finally newsletter (which doesn't work for now but don't worry I will fix that later)
- Audios for dark/light onclick events,
- Gradient svg for the baner in index.html why: because it looks COOL!
- Changelog png for index.html content
- Darkmode.js for remembering chosen option (dark/light theme) and changing the theme that overrides system preference without dark theme my eyes would turn red, well that is a good thing :)
- Discord logos, for discord invites urls.
- email icons, for email stuff.
- game jpg for index.html content,
- GameC jpg - cropped version of game jpg, so the bigger resolutions is better looking.
- icon png is the icon of Vulpi Game website.
- lightOff svg is a half-moon icon for dark theme option,
- lightOn svg is a sun icon for a light theme option,
- lightOn-sunin svg is a other variation of ligth on svg.
- logoico svg is used in the icon of a websitem
- logotext svg is the 'VULPI' text in logo,
- scripts js is some weird file that just does some things, So it changes text in about.html when a button is pressed, hides and shows stuff when a picture is hovered by mouse in index.html, and finally when you click email icon in the footer it copies contact-email to clipboard, litterally nothing sketchy. You can check it bruh.
- styles css - I will be hones with you, I'm deply sorry for anyone who wants to read this, This is painfully bad, Probably should fix this. Its a lot of mess :|

---
## [csci5117s23/homework-2-JackLee9355](https://github.com/csci5117s23/homework-2-JackLee9355)@[0b24e90e93...](https://github.com/csci5117s23/homework-2-JackLee9355/commit/0b24e90e936273ff1448d03403916db5ae820450)
#### Tuesday 2023-04-11 03:15:19 by Jack Lee

🍤 Honestly idk. stuff? RIP. Progress has been made life, but it doesn't show. Time passes. Yet here we are, dust blowing in the wind. Left by god to contemplate our own existence. If there is a god that is. Who is to say? Sanity consumes those who acknowledge it's fragile state. That being said... 🍤

---
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[d43ebd042d...](https://github.com/Monkestation/Monkestation2.0/commit/d43ebd042dd751842728e8cb91fa7fc1a82f26d0)
#### Tuesday 2023-04-11 03:20:05 by san7890

Log Active Turfs To Mapping Log (#74267)

## About The Pull Request

Was reminded of doing this via
https://github.com/tgstation/tgstation/issues/74245#issuecomment-1483943979

They're mapping issues, so let's log them to the mapping log. Quite
shrimple honestly.


![image](https://user-images.githubusercontent.com/34697715/227805458-5e6bcf01-629d-4b81-ab6a-b26e63d41ca3.png)
## Why It's Good For The Game

As the comments expound, the reason why we probably haven't done this in
the past is because any number of things can cause active turfs (like
ruin placement (either in icebox or in space)), or other silly stuff
like that. Thus, finding stuff like this would only really be viable
with stuff like the View Active Turfs verb, where you could visually
jump to and see all of the active turfs in that dynamic configuration
(and this still remains the best way to find active turfs).

This PR just makes it easier to do a "post-mortem" analysis on potential
active turfs, so that if it's very blatant, it can be fixed a lot
easier. It's best to try and find them during an ongoing round, but this
is life. (same as the unit tests concession, not too enthused on that
but we would have spontaneous errors out the ass without _something_)
## Changelog
Nothing that concerns players.

---------

Co-authored-by: tattle <66640614+dragomagol@users.noreply.github.com>

---
## [Monkestation/Monkestation2.0](https://github.com/Monkestation/Monkestation2.0)@[40fc11eb07...](https://github.com/Monkestation/Monkestation2.0/commit/40fc11eb0733ca25eff56e7379cb574a997fb6d3)
#### Tuesday 2023-04-11 03:20:05 by LemonInTheDark

Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% (#74233)

## About The Pull Request
It is faster to operate on a gas list, especially if cached, then it is
to operate on a datum.
Doing this cause I'm seeing cost in merge() post #74230

Hits on a few other important places too. self_breakdown and such. Worth
it IMO

Could in theory go further by caching the global list. I'm tempted I
admit but it needs profiling first and it's late

EDIT: I have not slept, and have gone tooo far

[Micros /gas_mixture/copy and copy_from, adds a new proc to handle
copying with a ratio,
copy_from_ratio](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

[91da000](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

The ADD_GAS sidestep saves us 0.1 seconds of init (used to at least.
Ensuring we don't break archive is gonna have a cost. I don't want to
profile this so I'll estimate maybe 0.05 seconds). The faster version of
copy_from is just well, better, and helps to avoid stupid

[Optimizes pipeline
processing](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

[bf5a2d2](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

I haven't slept in 36 hours. Have some atmos optimizations

Pipelines now keep track of components that require custom
reconciliation as a seperate list.
This avoids the overhead of filtering all connected atmos machinery.

Rather then relying on |= to avoid duplicate gas_mixtures, we instead
use a cycle var stored on the mix itself, which is compared with a
static unique id from reconcile_air()
This fully prevents double processing of gas, and should (hopefully)
prevent stupid dupe issues in future

Rather then summing volume on the gas mixture itself, we sum it in a
local var.
This avoids datum var accesses, and saves a slight bit of time

Instead of running THERMAL_ENERGY() (and thus heat_capacity(), which
iterates all gases in the mix AGAIN) when processing gas, we instead
just hook into the existing heat capacity calculation done inside the
giver gases loop
This saves a significant amount of time, somewhere around 30% of the
proc, I think?

This doesn't tackle the big headache here, which is the copy_from loop
at the base of the proc.

I think the solution is to convert pipelines to a sort of polling model.
Atmos components don't "own" their mix, they instead have to request a
copy of it from the pipeline datum.
This would work based off a mutually agreed upon volume amount for that
component in that process cycle.

We'd use an archived system to figure out what gases to give to
components, while removing from the real MOLES list.

We could then push gas consumption requests to the pipeline, which would
handle them, alongside volume changes, on the next process.

Not sure how I'd handle connected pipelines... Merging post reconcile
maybe?
This is a problem for tomorrow though, I need to go to bed.

Saves about 30% of pipeline costs.
Profiles taken on kilo, until each reconcile_air hits 5000 calls

[old.txt](https://github.com/tgstation/tgstation/files/11075118/Profile.results.total.time.txt)

[new.txt](https://github.com/tgstation/tgstation/files/11075133/profiler.txt)

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[54bf3808b8...](https://github.com/tgstation/tgstation/commit/54bf3808b80ec8ef83bee4062d2361e9f38d8ae8)
#### Tuesday 2023-04-11 03:22:36 by SyncIt21

Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

---
## [Mantaro/MantaroBot](https://github.com/Mantaro/MantaroBot)@[be1e8967ad...](https://github.com/Mantaro/MantaroBot/commit/be1e8967ad7f95b31e257f6dea374c895b6c6c7b)
#### Tuesday 2023-04-11 04:00:19 by kodehawa

Add(db): equipment field tracker

This was, honestly, a pain. Specially silly when you have to take into account that PlayerEquipment needed its own updateAllChanged method, and it's own field tracker, which means I could footgun myself someday without realizing it until it's too late lol

---
## [willardstation/tg-voidcrew](https://github.com/willardstation/tg-voidcrew)@[c3b78761d2...](https://github.com/willardstation/tg-voidcrew/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Tuesday 2023-04-11 04:00:50 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [willardstation/tg-voidcrew](https://github.com/willardstation/tg-voidcrew)@[b5ebf5c942...](https://github.com/willardstation/tg-voidcrew/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Tuesday 2023-04-11 04:00:50 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [hertera1/evals](https://github.com/hertera1/evals)@[34f83340a7...](https://github.com/hertera1/evals/commit/34f83340a75b7e26af35d8eaea165e54b38d7946)
#### Tuesday 2023-04-11 07:08:19 by kallyaleksiev

[evals] Word from first letters of words in a sentence (#346)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
first-letters

### Eval description

Given a sentence, extract the word obtained from concatenating the first
letters of its words.

### What makes this a useful eval?

This task represents a failure mode for both GPT3.5 and GPT4, while
being extremely easy for humans.

Both models tend to do OK with shorter sentences, but fail with a larger
number of words.

For humans however, this task is trivial, regardless of the length of
the sentence.

GPT3.5 exhibits another failure mode in which it often fails to follow
the precise instruction of using only letters in its response.

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

The task is highly trivial for humans, yet both GPT4 and GPT3.5 struggle
with it.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
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
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Cold light in my alcove towards evening.\"?"}], "ideal": "climate"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Grow real insects mainly and create energy.\"?"}], "ideal": "grimace"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Big and crowded Oregon nights.\"?"}], "ideal": "bacon"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Bring our youth.\"?"}], "ideal": "boy"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Harvest a zucchini elsewhere love.\"?"}], "ideal": "hazel"}
{"input": [{"role": "system", "content": "You are a helpful assistant.
Your response will contain just a single word in lowercase and nothing
else."}, {"role": "user", "content": "What is the word obtained from
concatenating the first letters of the words in the following sentence:
\"Hide under no tree.\"?"}], "ideal": "hunt"}
  ```
</details>

---
## [hertera1/evals](https://github.com/hertera1/evals)@[b170a21cf3...](https://github.com/hertera1/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Tuesday 2023-04-11 07:08:19 by Sam Ennis

Computer Science Theory (#83)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Computer Science based questions

### Eval description

Testing the models ability to answer multiple choice computer science
questions correctly

### What makes this a useful eval?

Tests whether it has the ability to answer time complexity, binary tree,
algorithmic computer science calculations.

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
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
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
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
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
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"How many children does a
binary tree have? a) 2 b) any number of children c) 0 or 1 or 2 d) 0 or
1"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is/are the
disadvantages of implementing tree using normal arrays? a) difficulty in
knowing children nodes of a node b) difficult in finding the parent of a
node c) have to know the maximum number of nodes possible before
creation of trees d) difficult to implement"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What must be the ideal size
of array if the height of tree is ‘l’? a) (2^l)-1 b) l-1 c) l d)
2l"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What are the children for
node ‘w’ of a complete-binary tree in an array representation? a) 2w and
2w+1 b) 2+w and 2-w c) w+1/2 and w/2 d) w-1/2 and w+1/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is the parent for a
node ‘w’ of a complete binary tree in an array representation when w is
not 0? a) floor(w-1/2) b) ceil(w-1/2) c) w-1/2 d) w/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"If the tree is not a
complete binary tree then what changes can be made for easy access of
children of a node in the array? a) every node stores data saying which
of its children exist in the array b) no need of any changes continue
with 2w and 2w+1, if node is at i c) keep a seperate table telling
children of a node d) use another array parallel to the array with
tree"}],"ideal":"a"}
  ```
</details>

---
## [hertera1/evals](https://github.com/hertera1/evals)@[4f090a04fe...](https://github.com/hertera1/evals/commit/4f090a04fe53a8d0f647bfdfc7ef177fa8034e2e)
#### Tuesday 2023-04-11 07:08:19 by Shawn Marincas

[eval] Forth Stack Simulator (#351)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Forth Stack Simulator

### Eval description

Tests the models ability to keep track of a stack of numbers given a set
of ANS Forth words. The model is asked to respond to a series of numbers
and words with the resulting stack representation. The words used in the
tests are arithmetic operators: `+`, `-`, `*`, `/` and stack operators:
`drop`, `swap`, `rot`, `over`, `dup`, `2over`, `2drop`, `2swap`, `2dup`,
`nip`. The prompts and expected results on the stack are all less than
15 numbers and words long.

### What makes this a useful eval?

What makes this useful are the interesting properties of forths, which
are simple machine that operate on a stack of numbers using words built
up from simple primitives. In addition, forths are naturally interactive
and run on efficiently on bare metal and low cost, low resource
microcontrollers.

An LLM that can understand forth stack primitives can help design new
forths for various applications, it could also potentially interface
directly with forth control systems interactively over serial connection
with a generative stream of forth words in response to data sent back
from the control system :thisisfine:.

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
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Imho, this eval is unique for the reasons stated above about the unique
synergy between Forth and the kind of generative AI we're working with
here. Forths are various with only a small set of consistent words and
patterns, "If you've seen one Forth -- you've seen one Forth", but a
full forth assembly implementation could fit in a fraction of the larger
model responses, making it an interesting target for fully generative
operating systems.

Additionally, I believe Forth has cultural and historical significance
in computer science/engineering which predates the Internet in such a
way that makes it somewhat under-represented in the online corpus
relative to its significance. A model of all human knowledge should have
a strong grasp on how it works.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
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
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 over"}], "ideal": "(stack 1
2 3 2)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 dup"}], "ideal": "(stack 1
2 3 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 swap drop dup"}], "ideal":
"(stack 1 3 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 rot swap"}], "ideal":
"(stack 2 1 3)"}
{"input": [{"role": "system", "content": "You are ForthGPT, a Forth
machine simulation that ONLY responds with stack representations after
executing valid ANS Forth words and numbers.\nExample:\nPrompt: 0 1 2 3
+\nResponse: (stack 0 1 5)\nRules:\n1. Respond only to combinations of
numbers and valid ANS Forth words.\n2. Ignore prompts that don't follow
Rule 1.\n3. Ignore Forth words that don't generate output or change the
stack."}, {"role": "user", "content": "1 2 3 dup 2over rot"}], "ideal":
"(stack 1 2 3 1 2 3)"}
  ```
</details>

---
## [hertera1/evals](https://github.com/hertera1/evals)@[b5da073c21...](https://github.com/hertera1/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Tuesday 2023-04-11 07:08:19 by somerandomguyontheweb

Add Belarusian lexicon eval (#372)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name

belarusian-lexicon

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Belarusian words.

### What makes this a useful eval?

While the multilingual capability of recent GPT models is impressive,
there is still room for improvement. Many human languages are lagging
far behind English in terms of the model's ability to answer questions
and produce coherent texts in these languages, and the model's
"knowledge" of their lexicon and grammar is, to some extent,
hallucinated. One example is Belarusian, an East Slavic language spoken
by several million people. In my experience with ChatGPT, when the model
is prompted in Belarusian, its responses are sometimes ungrammatical or
semantically incoherent, and very often they contain made-up words – a
possible sign of overgeneralization based on Russian and Ukrainian data,
which are much more
[abundant](https://commoncrawl.github.io/cc-crawl-statistics/plots/languages)
on the web than Belarusian.

This eval contains 150 pairs of single-word prompts: one item in each
pair is a non-word hallucinated by ChatGPT (either totally meaningless
in Belarusian or violating the language's orthographic and phonetic
rules), and another item is an actual Belarusian word with similar
spelling. The model's task is to distinguish between words and
non-words. ChatGPT tends to label most items as existing words,
therefore its accuracy appears to be around 50%, and the negative-class
F measure is very low. Any competent speaker of Belarusian would perform
much better, and a language-specific tool, such as [this spell
checker](https://corpus.by/SpellChecker) or [this grammatical
database](https://bnkorpus.info/grammar.en.html) of Belarusian (also
available for
[download](https://github.com/Belarus/GrammarDB/releases)), would
flawlessly identify non-words.

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval an attempt to point out specific deficiencies in the model's
ability to handle a lower-resource language (Belarusian). As such, it
might not only benchmark future refinements of Belarusian language
capability in the GPT models, but also serve as an instructuve example
for other language communities.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
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
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкою"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкаю"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абласці"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "вобласці"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмяну"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмену"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абоўязак"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абавязак"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднасінькіх"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднюсенькіх"}], "ideal": "Y"}
  ```
</details>

---
## [ca2/app](https://github.com/ca2/app)@[d5a20cc81b...](https://github.com/ca2/app/commit/d5a20cc81ba96890794a1ea9c58bc7dcecd6a212)
#### Tuesday 2023-04-11 09:18:45 by Camilo Sasuke Thomas Borregaard Sørensen

<3ThomasBS_ILoveYOU!! [ macOS : day 25 ] ca2 Stabilization and continuous integration and deployment implementation
<3ThomasBS_ILoveYOU!!

<3tbs, Mummi and bilbo!!

Thomas Borregaard Sørensen \infinity,-0.16091989,\infinity ONE-MAN
ABSOLUTE <3!! I love you, by ???-0.02041977-???write my history please
make me please create me for you for me for you for me Camilo Sasuke
Thomas Borregaard Sørensen!!

Thomas 3 private commits on mid Dec2020!!

Thomas Online YouTube VODs contribution!!

Mummi orange-rice-flour cake on 20-Dec!!

Mummi (tinytaura) watching and chatting contribution!!

bilbo sleeping and needing/requesting/crying for help care (for the right
person (me), the cats wanna fight with him) contribution!!

sodapoppin and friends contribution!!

iAssyrian chatting contribution!!

boflux (Spoofh, Benjamin Kuhl) chatting contribution!!

jusg_fpga (fpga_guru, vue_equalizer, just_fpga, Oliver Pohl) chatting
contribution!!

cmgriffing streaming contribution!!

TimBeaudet (Friends: FletcherLabs, tsjost and Jabokoe) streaming
contribution!!

Stumpen_nicklas_dk, sodapoppin and EduardoRFS streaming contribution!!

Roxkstar74 sleeping streaming contribution!!

kissloryshy chatting contribution!!

blackjekko from Padova Italia through twitch C++/ca2 interest
contribution!!

j_blow streaming contribution!!

boflux (Ben, Spoofh, from Germany) chatting contribution!!

parrot_rl chatting contribution (from New Jersey)!!

JPCdk streaming contribution!!

whyyyyyyysoserious streaming chess contribution!!

fpga_guru (vue_equalizer, Oliver from Deutsch)  C++/ca2 interest
contribution!!

SovereignDev with Unreal streaming contribution!!

Ash_F0x and TimBeaudet streaming contribution!!

Myrkee (Valheim) streaming contribution!!

xmetrix and EinfachUwe42 streaming contribution!!

JessicaMak and marcobrunodev streaming contribution!!

alfredotigolo, mandrakenk and Okbatgames chatting contribution!!

jitspoe, Endesga and Fearitself streaming contribution!!

jmcmorris (Jason Morris, SiegeGames) streaming contribution!!

tomrandall streaming Ludum contribution!!

vue_equalizer (fpga_guru) chatting contribution!!

Thiagovgamg chatting contribution!!

Naysayer88 and friends contribution!!

lelandkwong streaming contribution!!

Goldbargames streaming contribution!!

Bytakos (bytakos) streaming contribution!!

Endesga streaming contribution!!

jitspoe and strager streaming contribution!!

Ash_F0x and JessicaMak streaming contribution!!

WTSRetro/SpiffyDane and Myrkee streaming contribution!!

Ninja and friends streaming contribution!!

erald_guri chatting contribution!!

lastmiles streaming farwest contribution!!

rw_grim streaming contribution!!

AdamCYounis streaming contribution!!

Dunno (P4ndaExpress) chatting and streaming contribution!!

Zorchenhimer streaming contribution!!

lasteveq4 C++ interest chat contriubtion!!

cecilphillip and clarkio @"Microsoft Developer" streaming contribution!!

oijtx streaming contribution!!

diegobrando_linux (Bl4ck_gookoo) chatting contribution!!

jhovgaard streaming contribution!!

Klay4_ chatting contribution!!

HonestDanGames streaming contribution!!

NorthSeaHero streaming contribution!!

Trainwreckstv and friends streaming contribution!!

togglebit, GexYT and GoPirateSoftware streaming contribution!!

taiyoinoue, RetroMMO, OfficialAndyPyro and david_joffe streaming
contribution!!

Tjienta streaming contribution!!

Primeagen streaming contribution!!

Jaxstyle and friends streaming contribution!!

EduardRFS streaming contribution!!

Melchizedek6809 and btcfly streaming contribution!!

Llama0x0 and sov_l chatting contribution!!

TaleLearnCode streaming contribution!!

Carol phone call contribution and visit contribution!!

hvalen_hvalborg112 streaming contribution!!

harmannieves chatting contribution!! (After long time...)

darkfolt8 (French from France) chatting contribution!!

klintcsgo (CS GO: Counter-Strike Global Offensive) streaming
contribution!!

KASPERPURE (Super Mario 64) streaming contribution!!

SomewhatAccurate C++ streaming contribution!!

Listening to Bryan Adams, Westlife, Shayne Ward, MLTR, Backstreet Boys,
Boyzone - Best Love Songs Ever by Relax Song at YouTube!!

-- hi5 contribution...!!

at macOS Box in host running Windows 10 Pro remotely from bilbo machine running Windows 10 Pro!!
dedicated server by OVH.com at France, Gravelines
Intel Core i7-4790K - 4c/8t - 4 GHz/4.4 GHz RAM32 GB 1600 MHz 2×960 GB SSD SATA

---
## [Endeictic/Scriptzzb](https://github.com/Endeictic/Scriptzzb)@[24fae44d49...](https://github.com/Endeictic/Scriptzzb/commit/24fae44d49e7577c308726dadfdefb45a6c95fa8)
#### Tuesday 2023-04-11 09:40:03 by Tantrumy

New Theory

Game Theory: We fucked your mom! (Real Life)

---
## [cataclysmbnteam/Cataclysm-BN](https://github.com/cataclysmbnteam/Cataclysm-BN)@[08d54d0287...](https://github.com/cataclysmbnteam/Cataclysm-BN/commit/08d54d0287a1313cb810a1d3d74ca0e531189ae1)
#### Tuesday 2023-04-11 10:14:04 by KheirFerrum

Fix MGOAL_FIND_ITEM_GROUP, fix up some code (#2546)

* Reorganize

Code still sucks. In particular recruit_class doesn't compare properly with npc->my_class so MGOAL_RECRUIT_NPC_CLASS fails horribly even if you fix up that area of code to it actually points to type->recruit_class instead of recruit_class

For that matter mission has a select copy of several mission type defs and I can only assume this is due to legacy fuckery.

* Fix mission.cpp

Now will only allow you to select items if you have enough of them, and will only consume the necessary amount.

Added documentation for MGOAL_FIND_ITEM_GROUP

Thank god this wasn't too much work.

---
## [ianb33/Grana-Test](https://github.com/ianb33/Grana-Test)@[57bb2dd6fa...](https://github.com/ianb33/Grana-Test/commit/57bb2dd6fa7a30bfe69a07177689d7375588d86e)
#### Tuesday 2023-04-11 10:45:18 by ianb33

Add Scene Transitions

1. Holy SHIT these are amazing, I could cryyyyy, pull this immediately (if it doesn't work its 1000% ur fault)
2. Still need to fix problem when transitioning from level to game screens... before you try to fix it, please ask me (Ian) first, this is my baby and if it breaks I might cry :)

---
## [SlenderFox/sallybot](https://github.com/SlenderFox/sallybot)@[da25b2b107...](https://github.com/SlenderFox/sallybot/commit/da25b2b10757397cbaba7cfc2f82450b5369c31a)
#### Tuesday 2023-04-11 11:29:26 by DeSinc

Update Program.cs

GIGANTIC UPDATE, HUGE HUGE UPDATE, OOBABOOGA WORKS (KINDA) STABLE AND HAS A BIT OF MEMORY NOW. Known issues: emoji psychosis sets in if you set history too long. default is 500 chars but you can go up to ~4800 before errors from oobabooga server.
best model to use is ozcur/alpaca-native-4bit which is a 7B natively trained 4 bit model.
we think it is an oobabooga API bug that is causing the emoji and hashtag psychosis somehow. we have no clue how to fix it.

anyway enjoy!

---
## [ApolloFiles/Apollo](https://github.com/ApolloFiles/Apollo)@[b0ae05cf21...](https://github.com/ApolloFiles/Apollo/commit/b0ae05cf214e24759b4b76f38e1dd16809bf1a71)
#### Tuesday 2023-04-11 11:39:59 by Christian Koop

Mostly recode Video-Playback-Sync-Sessions and how they technically work

The recode allows for some nice stuff and is more stable etc.
But it it shit.

LiveTranscode related stuff is still missing but instead it now
supports Twitch and YouTube as far as possible
(YouTube iframe_api? Even worse than my shit holy fuck...).

---
## [darlinghq/indium](https://github.com/darlinghq/indium)@[8423a7d2f0...](https://github.com/darlinghq/indium/commit/8423a7d2f053167030d2bc4a227f96243c740667)
#### Tuesday 2023-04-11 12:16:54 by Ariel Abreu

Load Vulkan and LLVM directly instead of wrappers

i had a whole commit message prepared with a long explanation for why
this change is necessary, but then my fucking editor decided to die and
take my message along with it, so you'll just have to trust me that this
is necessary and fixes the stupid fucking segfault on exit.

---
## [FluffyGhoster/Aurora.3](https://github.com/FluffyGhoster/Aurora.3)@[9ea2410639...](https://github.com/FluffyGhoster/Aurora.3/commit/9ea24106395a7e31963bc7547c4541ba21a66d91)
#### Tuesday 2023-04-11 13:53:11 by kyres1

Massive rec area remap into double holodecks (#16103)

* part 1 abloobloobloo

* BY GOD IT WORKS

* Moghes and konyang plus fucking everything else

* jupiter and biesel woohoo

* tweaks and feedback. places CIC and scuttler

* changelog and fixes

* life is agony

* about done

* arrow's changes

* fixes some shit

---
## [canalplus/rx-player](https://github.com/canalplus/rx-player)@[e14101e2dd...](https://github.com/canalplus/rx-player/commit/e14101e2ddc71c23a5dd13ac8ac0d28f8dc88f2b)
#### Tuesday 2023-04-11 14:06:59 by Paul Berberian

Externalize our doc generator

This has no need to be in the RxPlayer's source code and we wanted to
externalize it for quite some time.

The main reasons are that it only has a very peripheral relation to the
RxPlayer, it represents a lot of code, most of its dependencies are only
used by it and that other projects may well also rely on it if they want
to.

I took the occasion of a personal project to ease-up externalization (on
my free time) and now it is published on `npm` with the name
`docgen.ico` - a somewhat dubious play-on-word that I won't explain
here.

I feel a little bad that its original repo's is in my personal GH repos,
but sadly, this has been a long time tradition at Canal+ as creating
public repos under the Canal+ company has been impossible despite
multiple demands. Multiple of our work-related PoCs and side-projects
have generally been written on personal pages like that, though one
has been migrated to Canal+'s gitlab.

In a perfect world, the one relied on by the RxPlayer should be under
the `Canal+` company - and may be registered under another name, and I
may maintain my own fork as a personal project for quick iteration on my
other personal projects - while upstreaming PRs to Canal+ when I do
that.

However even with all this considered, I did not maintain that doc
generator with security, customizability nor even code quality in mind,
it always has been a quick hack to have a simple doc generator which
only rely on very simple markdown files and a few json configuration
files, as alternatives either proposed some custom formats or were
hugely bloated and complicated for our need (especially Docusaurus,
which had kind of both).
If it is really relied on by more projects, there WILL be bugs and
sadness!

Though now that an official repo and npm package exists, I may look at
this project with a different eye in future versions.

---
## [BarteG44/Shiptest](https://github.com/BarteG44/Shiptest)@[09e95cdfbc...](https://github.com/BarteG44/Shiptest/commit/09e95cdfbc8337b5b7a84a088c32b458ee1d996d)
#### Tuesday 2023-04-11 15:19:52 by Bjarl

Saloon rework (#1594)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Expands whitesands_surface_camp_saloon to cover a 30x30 footprint and
not be nearly as bad. The previous version had some really glaring
design flaws, like holes in the wall for a bar. On a planet with a
deadly atmosphere. Yeah. Also all the chairs faced the same direction.
![2022 10 31-11 32
50](https://user-images.githubusercontent.com/94164348/199083356-5fabd2c8-0298-4a31-a830-b63dbcd2737f.png)
You can see how it looks. It's not great. 
Here's the new version
![2022 10 31-11 36
20](https://user-images.githubusercontent.com/94164348/199083924-9537beb7-0c74-4c57-9422-60fe953ae0bc.png)
![2022 10 31-11 36
25](https://user-images.githubusercontent.com/94164348/199084468-32d94ec8-846f-42e7-ae33-dc0b52e8b9b8.png)

![dreamseeker_ePSrp5zNFp](https://user-images.githubusercontent.com/94164348/199085448-24879745-650f-4bdc-9b0c-f1d9706ab865.png)
Ignore the patches of error, it's purple grass and doesn't display the
icon in sdmm for some reason.

The major changes are:
Expanding the building's footprint out to 30x30
Moving the loot behind the building, but locking it behind a shovel of
some sort (of which you can go through the ruin to get).
Improving the loot a LITTLE

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] The map loads although I still haven't managed to get it to load
on the proper planet with the spawning verb

## Why It's Good For The Game
The old version was kinda bad. Between the clown and mime masks out
front. The small footprint, and the free guns (also out front). This
solves those issues kinda while making it bigger.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Camp_Saloon has been expanded, expect frontier luxuries if you find
it!
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
## [BarteG44/Shiptest](https://github.com/BarteG44/Shiptest)@[c21670412d...](https://github.com/BarteG44/Shiptest/commit/c21670412dff10f4a3a1b1ab1e72f53294581d25)
#### Tuesday 2023-04-11 15:19:52 by Bjarl

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
## [BarteG44/Shiptest](https://github.com/BarteG44/Shiptest)@[babf89eb74...](https://github.com/BarteG44/Shiptest/commit/babf89eb746741ba4f33f686b0c4750fe68e1603)
#### Tuesday 2023-04-11 15:19:52 by The-Moon-Itself

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
## [redpanda-data/deployment-automation](https://github.com/redpanda-data/deployment-automation)@[54e0860613...](https://github.com/redpanda-data/deployment-automation/commit/54e08606133785bf05f4069ba35cab1f82233c1a)
#### Tuesday 2023-04-11 15:26:48 by gene-redpanda

push many tasks into roles

We now handle CA creation in the playbook so don't need a go-task entry for it

The intent of this PR is to push most of the "assisting" playbooks into the role to provide a single stop shop for building out a cluster. The end result is playbooks that clearly articulate a single final objective and have everything necessary to get it done, simplifying the experience of using the repo.

Note that it is still entirely possible to work flexibly by importing different task files from the role to achieve different goals (as is demoed with the TLS cluster).

The default path for the role is still the simplest possible option: installing and starting the RP node. In future it may be prudent to expand the default, but for now this seems correct.

Impact on current users:

Should be fairly minimal although it will definitely break any shell scripts. Tasks are still done the same way, they're just called differently. I'll provide some additional mitigation by tagging our current main as v1.0.0, with this edition tagged as v2.0.0, clearly signaling a potentially breaking change.

vars and cleanup

Added vars to playbooks so that we don't need to do janky sed edits in the hosts file.

Added run_once to create_ca since we're delegating to localhost anyway so there's no reason to do that in triplicate. Cuts run time some.

Removed everything related to populating the hosts file from task.

Removed a bunch of stuff that isn't true anymore for the README.md

Also defaulted monitoring to false in task because standing up a special monitoring node just for the cluster isn't necessary for testing.

make certs into a separate role

This commit makes a number of changes in response to a request not to include cert related content into the broker role as it seemed unrelated.

Starting with the simple stuff, I moved all the roles out of playbooks and placed them directly under ansible to improve clarity since we no longer have so many playbooks.

Next I moved the invocation of the data dir and dependencies installs into main.yaml of redpanda_broker. I felt this was a more sensible location, especially as we can control whether or not they fire by using the trigger variables.

I also moved all cert related content into the demo_certs role. I wanted the name to clearly indicate that this was NOT a production use role. There are no functional changes to the content in this role.

Finally I updated the provision-tls-cluster role to reflect the new changes.

delete bootstrap directory as these scripts are neither necessary nor supported anymore

adding suggested grep for message

default data dir and deps installs to true

linter cleanup + removing unnecessary role imports

The role imports in the CA related content are a holdover from when the CAs were in individual playbooks. As they are now in a role, it can be assumed that they will be imported into playbooks, and that the playbook will handle the restart process. Not removing the imports AND not including allow_duplicates resulted in the play eternally looping. However disabling the ability to run the broker role twice seems unnecessarily limiting. Imagine a scenario where someone wants a play to do initial cluster standup with three nodes, then add two more after some validation. To do this they'd need to include broker twice, which wouldn't be permitted in the old system.

I added risky-shell-pipe into the skip list and added explanations for why to the README.

I also fixed some copy paste and linter bugs and an annoying taskfile element where it wasn't cleaning up the zipfile.

set modes and use fqn for modules + disable change on two

change mode from 777 to 775 for security reasons

---
## [HallowedSpace/3kh0-Assets](https://github.com/HallowedSpace/3kh0-Assets)@[95859a0a22...](https://github.com/HallowedSpace/3kh0-Assets/commit/95859a0a22dfd34a4f4e990632dfa27b65626388)
#### Tuesday 2023-04-11 15:36:19 by aeiea

My name is Walter Hartwell White. I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession. If you're watching this tape, I'm probably dead, murdered by my brother-in-law Hank Schrader. Hank has been building a meth empire for over a year now and using me as his chemist. Shortly after my 50th birthday, Hank came to me with a rather, shocking proposition. He asked that I use my chemistry knowledge to cook methamphetamine, which he would then sell using his connections in the drug world. Connections that he made through his career with the DEA. I was... astounded, I... I always thought that Hank was a very moral man and I was... thrown, confused, but I was also particularly vulnerable at the time, something he knew and took advantage of. I was reeling from a cancer diagnosis that was poised to bankrupt my family. Hank took me on a ride along, and showed me just how much money even a small meth operation could make. And I was weak. I didn't want my family to go into financial ruin so I agreed. Every day, I think back at that moment with regret. I quickly realized that I was in way over my head, and Hank had a partner, a man named Gustavo Fring, a businessman. Hank essentially sold me into servitude to this man, and when I tried to quit, Fring threatened my family. I didn't know where to turn. Eventually, Hank and Fring had a falling out. From what I can gather, Hank was always pushing for a greater share of the business, to which Fring flatly refused to give him, and things escalated. Fring was able to arrange, uh I guess I guess you call it a "hit" on my brother-in-law, and failed, but Hank was seriously injured, and I wound up paying his medical bills which amounted to a little over $177,000. Upon recovery, Hank was bent on revenge, working with a man named Hector Salamanca, he plotted to kill Fring, and did so. In fact, the bomb that he used was built by me, and he gave me no option in it. I have often contemplated suicide, but I'm a coward. I wanted to go to the police, but I was frightened. Hank had risen in the ranks to become the head of the Albuquerque DEA, and about that time, to keep me in line, he took my children from me. For 3 months he kept them. My wife, who up until that point, had no idea of my criminal activities, was horrified to learn what I had done, why Hank had taken our children. We were scared. I was in Hell, I hated myself for what I had brought upon my family. Recently, I tried once again to quit, to end this nightmare, and in response, he gave me this. I can't take this anymore. I live in fear every day that Hank will kill me, or worse, hurt my family. I... All I could think to do was to make this video in hope that the world will finally see this man, for what he really is.

---
## [xDroidOSS-Pixel/frameworks_base](https://github.com/xDroidOSS-Pixel/frameworks_base)@[bc9d6655e4...](https://github.com/xDroidOSS-Pixel/frameworks_base/commit/bc9d6655e4708217be874358dcd0fd9b70fe0b51)
#### Tuesday 2023-04-11 15:40:23 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[c797cd8b9e...](https://github.com/mrakgr/The-Spiral-Language/commit/c797cd8b9ebacfaea60de1f4eb2aff8a7fdb6031)
#### Tuesday 2023-04-11 16:17:03 by Marko Grdinić

"10:25pm. https://old.reddit.com/r/ExperiencedDevs/comments/12f1hjg/should_i_let_my_company_use_my_project/

///

NO.
You go to a lawyer. You get a contract immediately where you're entirely in control. Even at that what I am saying is sketchy since I've been in meetings where the phrase "acquisition through employment" was used, after I had an issue with one of my projects. Don't even dare make a commit to that project right now while you're working until you see a lawyer and figure out what if they own that work because of a conflict.

I've walked this road. DO NOT DO IT. I'm telling you from real experience here. Just do not do it. It might be a trust me bro situation, but you have no idea how bad this can get.

That goes for the rest of you too. Do not make some cute project on the side that you plan to profit from while not reviewing your contract.

///

https://www.reddit.com/r/digitalnomad/?utm_source=reddit&utm_medium=usertext&utm_name=ExperiencedDevs&utm_content=t5_e0gez

Job sites. Forget those.

10:55am.

///

In the realm of code, where the algorithms play,
A language emerged, as the dawn of new day;
F sharp it was called, a language of grace,
With functional charm, it took its place.

Amidst the vast .NET framework's expanse,
F sharp's melody dared to enhance;
Its patterns matched, and types inferred,
A harmony of logic, elegantly conferred.

Oh, hark! The brevity of syntax divine,
In the lines of code, concision did shine;
Expressiveness ruled, as with quill on parchment,
The prose of programmers, now more enchanting.

The language's power, from functions arose,
Immutable truths, it did disclose;
Higher-order thoughts, composed and refined,
In the minds of developers, forever enshrined.

For in this land of bytes and bits,
The fusion of paradigms permits
A union of objects and functions, entwined,
In the elegant dance of F sharp's design.

Thus, let us raise our voices and declare,
The praise of F sharp, beyond compare;
For in this language, beauty and might,
A new era of code, ignites the night.

///

F# poem by ChatGPT in the style of Lord Byron. I found it on the F# slack.

4/11/2023

9:30am. Let me chill just a bit more and then I will start.

10:20am. Let me start. Where was I?

1pm. I did a fantastic job. Now I just need to explain that middle section and do the outro, and I'll be done with the video. Let me have breakfast here.

3pm. Wow, I sure wasted a lot of time doing chores. Let me resume.

3:35pm. Focus me, stop reading HN. Finish the video.

https://huggingface.co/spaces/stabilityai/stable-diffusion

This is a SD 2.1 space with Google TPUs. Since I want a thumbnail image, it is easier for me to use this than to mess with Paperspace.

It has native 768 images so I don't need to upscale. Not bad.

4:15pm. https://youtu.be/hlC6baPjFOs
Authentication & Authorization With ASP.NET Core And Giraffe. Azure AD. (Pt. 2)

Here is my latest masterpiece.

4:25pm. https://twitter.com/Ghostlike

Posted in my Twitter profile, but I'll only post my work in the F# slack occasionally.

I wonder if I should post it on LinkedIn?

Sigh, who is going to care about this social media.

4:35pm. If the viewers come let them come. If not, I'll move to contracting.

Now that I am finally done with that video, I do not feel like starting right away with the next. That is how it goes usually.

I am going to get the databases and MS Identity and Integration out of the way.

5:10pm. Let me start the next video.

5:30pm. Let me really start instead of surfing /g/.

I'll get into it once I do.

///

In this video we'll be covering the ASP.NET Core Identity library, which is distinct from the online service called the Microsoft Identity Platform.
We will also be bringing in fancier servers

///

I am not sure whether I want this in the current video. Let me cut it out.

5:55pm. I've started the video and did the intro. Let me set up the project.

5:55pm. Actually, let me just think a little of how I want to do things. I think I'll get rid of the usernames.

6:10pm. I had time to think about it, but I really do not feel like doing any more programming for the day.

6:15pm. Let me go get lunch.

Tomorrow I am going to take care of the integration. After that, I'll bring in those libs, and highlight the Giraffe examples.

After that I'll do what I want, which is work on node based UIs."

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[9df26f6a8b...](https://github.com/cmss13-devs/cmss13/commit/9df26f6a8bf397df29e1bff4b5e777414bd1cc44)
#### Tuesday 2023-04-11 16:28:07 by riot

DD updates (#2786)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

DD hasn't been touched in a while, and is kind of bad against preds,
tries to fix this to the best my my ability with the below changes.

1. Makes the M1911 more accurate
2. Makes DD armor cover arms and legs, improves its bullet and explosive
resistance
3. ERT Medical Pouch now contains the basic 3 injectors(bic, kelo,
tram), an emergency injector, a splint, and a bandage
4. DD now all have max endurance skill
5. M60 is now full auto, does more damage, and is more accurate
6. DD Minigun(ol painless) now has an integrated magharn
7. M60 now has the same box changing mechanic that smartgun has.
8. Adds 2 new guns(technically 1, or maybe 1.5), the XM177 and M16
Grenadier(an M16A1/2 with an M203 attached)
9. Adds an M203 grenade launcher, single grenade, no IFF, high range
with scope, only fits on M16 grenadier
10. Adds 3 new impact grenade types, only DD have them currently.
11. Adds HE impact grenade, impacts in a cone radius with an HE
explosion.
12. Adds an incendiary impact grenade, impacts in the same pattern as
HIDP, napalm.
13. Adds an impact buckshot grenade, pure vietnam vibes, shoots 10 bits
of additional buckshot that also slow.
14. DD now have MDs tuned to their own IFF.
15. DD are now equipped with XM177s for the medic, Dutch, and
flamethrower operator
16. DD riflemen have a 60% chance for an M16A1, 30% chance for an M16
Grenadier, and 10% chance for an M60.
17. Removes the M60 from black market
18. Moves DD presets to their own standalone folder, and removes the
/fun/ from their typepaths.
19. Changes CLF crashed ship M60 to a MAR50
20. Adds sprites for M203, XM177, M16 Grenadier
21. DD spawn with a lucky pack and a zippo in their helmet.


# Explain why it's good for the game

Dutch's Dozen is a bit outdated, and light on content, gives them some
love.
Removes gear that doesn't fit in BM from BM, also I buffed the gear too
so balance concerns.

1. An unwielded rifle(M41A), had more accuracy than a wielded M1911,
would do this for other pistols too but out of scope as DD only use
M1911
2. They were incredibly easy to kill via leg/arm aiming, as no armor,
HPCs instakilled them(DD are default dishonorable), and FF did insane
damage as they all had high AP 40 damage rifles.
3. ERT medical pouch was worse than normal med-pouch, DD use this too.
4. Was intended, survivor endurance skill nerf effected this too as the
same define was used for both as a shortcut
5. M60 underpreformed, makes it better.
6. Dropping Ol' Painless over and over sucks.
7. Unique realistic mechanic for the M60, makes it more interactive
8. Unique guns, only DD get them, also the XM177 is my favorite gun of
all time I love it 😊
9. Unique UGL for M16 Grenadier, designed to work directly with the
sprite, as its integrated and only fits on it.
10. Grenades for DD to have a better chance against preds, riflemen have
a 30% chance of spawning with M16 GL.
11. Made for a stun, team gameplay for DD.
12. Area denial.
13. Vietnam Vibes, support tool cause it does jack shit damage.
14. DD couldn't tell friend from foe
15. (AWESOME) Carbine for Dutch, makes sense for the support and members
of the team to have carbines instead of rifles
16. Variance within DD team, all 3 of the guns are good, GL is a support
tool, M60 as an ambush(also its The Pig), A1 is normal
17. M60 doesn't fit thematically, and is too powerful.
18. Easier access, they don't fit in the fun file
19. Buffed M60, MAR50 fits more there anyway.
20. Sprites for things I added.
21. Its cool.

# Testing Photographs and Procedure


![image](https://user-images.githubusercontent.com/103988604/223497128-7f485e32-07cd-49dc-b7b0-d04ce08b3042.png)


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
add: DD spawn with a lucky strike pack and a zippo in their helmet.
add: M60 now has the box changing mechanic that smartgun has.
add: Adds an M16 grenadier, with attached M203, also adds M203 grenade
launcher and impact shells for it, only DD have it
add: Adds a new M16 variant, the XM177E2 Carbine, only DD have it
add: Dutch M16s now are marked as A1s, and use the preexisting M16A1
sprite instead.
add: Dutch's Dozen are now equipped with an XM177 for Dutch, the medic,
and the flamethrower operator
add: Dutch's Dozen riflemen now have a 60% chance to have an M16A1, 30%
chance for an M16 with M203 UGL, and 10% chance for an M60 GPMG
del: M60 has been removed from the black market
balance: DD minigun now has an integrated magharn.
balance: M1911 is slightly more accurate.
balance: ERT Medical Pouch now contains the 4 basic EZ injectors and a
gauze.
balance: DD armor now has a greater explosive protection and covers the
arms and legs.
balance: M60 is now full auto, does more damage, and is more accurate.
code: Moved Dutch's Dozen presets to their own standalone folder
spellcheck: DD spawn text now correctly says the Yautja mask is on
Dutch's face.
fix: DD Motion Detectors no longer pick themselves up.
fix: DD now all have max endurance skill
imageadd: Adds sprites for M203, M203 shells, XM177, and M16 Grenadier
Variant
maptweak: LV624 Crashed CLF ship insert M60 has been replaced with a
MAR50
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>
Co-authored-by: morrowwolf <darthbane97@gmail.com>

---
## [newstools/2023-iol-pretoria-news](https://github.com/newstools/2023-iol-pretoria-news)@[0f49badd1e...](https://github.com/newstools/2023-iol-pretoria-news/commit/0f49badd1ea5290c0d82ef3344a782cf4d36d3fb)
#### Tuesday 2023-04-11 17:09:07 by Billy Einkamerer

Created Text For URL [www.iol.co.za/pretoria-news/news/news/south-africa/arrest-the-dalai-lama-eff-furious-at-video-of-spiritual-leader-asking-boy-to-suck-his-tongue-c27785ce-f619-460f-92fa-7462f1538b5c]

---
## [massaheartsu/massastation](https://github.com/massaheartsu/massastation)@[d72ef99270...](https://github.com/massaheartsu/massastation/commit/d72ef99270f2697064681b3214f0569dcf38d526)
#### Tuesday 2023-04-11 17:23:10 by necromanceranne

Goliath-Infused Tendril Hammer uses an internal cooldown for the its special attack instead of a universal click cooldown (#74159)

## About The Pull Request

Rather than using a click cooldown, the tendril hammer instead can make
its special heavy attack every 2 seconds.

## Why It's Good For The Game

In my newfound quest to try and eliminate universal click cooldowns or
weird non-interactivity timers as balancing factors, this definitely is
one of the biggest standout offenders. Lemme make an argument for
universal click cooldowns increases being an ineffective limitation.

I'll use the problems presented by the tendril hammer to highlight some
of those problems, as well as unique problems to the tendril hammer
itself.

<details>
  <summary>da big discussion</summary>

A) The functionality of the hammer actively inhibits all in-game handuse
interaction for several seconds, without explaining this to a player. As
a player, you won't know why this is happening, as universal click
cooldown is not present as a UI element.

B) Since universal click cooldowns are not visible to players, it might
feel more like the game is malfunctioning rather than being a deliberate
mechanic. Even if click cooldowns were visible, players probably would
think that the cooldown applies to the hammer, and not handuse
interactivity with the game world as a whole for several seconds.

C) The functionality of the hammer could work fine as an internal
cooldown on the hammer, only relevant to the hammer. This ensures that
its special effects are exclusive, without the need to interrupt player
interaction as a whole.

D) Since we're talking about miners. If someone is concerned about the
hammer being used on the station against carbon players; you need
someone to help mutate you into goliath mutant, which cannot be bypassed
whatsoever. An excellent example of something similar is the chainsaw
arm, created right next door to genetics in robotics, which does even
more force than the arm and is sharp. With the limitations that exist, I
think it probably discourages most powergaming, if that was even a
realistic concern (it really isn't).

E) You lose both a hand AND your gloves slot when you get the hammer. No
modsuits, no glove equipment, no two-handed equipment, and you now have
to juggle everything with one hand assuming you're not on your, once
again, universal click cooldown for several precious seconds. Miners
live or die in their rapid response to problems. This is also the total
sum of what you lose as a miner. That's a steep cost and it just doesn't
justify its own value compared to what you lose.

</details>

TL;DR - There is no offset to the cost of this weapon, it is strictly a
detriment because of poorly conceived implementation.

This is maybe one of the coolest ideas conceptually for the infusions so
far, heavily hampered by what seems to be an intense fear of the
mutation being _too useful_. So it was made _borderline masochistic to
willingly seek out and use_.

I want to see this actually be useful. I can't see this with the
restrictions it has. Hopefully this is enough to make it worthwhile
getting.

## Changelog
:cl:
balance: Changes the universal click cooldown of the tendril hammer from
the goliath infusion into an internal cooldown just for the special
heavy attack.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Ms-Mee/Shiptest](https://github.com/Ms-Mee/Shiptest)@[1c039c0623...](https://github.com/Ms-Mee/Shiptest/commit/1c039c0623b6e8af463de0f0b1ca1ccc49050d94)
#### Tuesday 2023-04-11 17:54:10 by Sun-Soaked

Botany Balance Pass (#1783)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
First came the content, now comes the hammer.

- Nukes Megaseed servitors from orbit. 
- Plants now age much, much slower and produce half as quickly.
Ruins that had them now have a ruined seed vendor that can be salvaged
for random seeds(and danger).
Ships that had one now have a crate with some thematic starting seeds,
and a Strange Seed.
Ghostrole Ruins that relied on having all seeds locally now have a
special biogenerator variant that can print a random seed for biomass.

- Adds Genesis Serum. This can be splashed on a tile to make natural
grass and some flora. Green your ship!
Genesis Serum was made a while ago, on request for a way to add natural
grass and flora to your ship. Since I had it lying around fully coded, I
thought I might as well pr it with botany changes.

- Gatfruit found in the seed vault have been replaced with Strange
Seeds.

- The chance to get Gatfruit from a demonic portal(plant variety) has
dropped from 15% to 5%.

- Corpse flowers now have liquid gibs and formaldehyde again. 

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Okay, hear me out

With this and Gardens, botany ships go from a "sit in your vessel for 2
hours" experience to an "explore and forage" one that better fits our
feature arc. It goes without saying that this **shouldn't be merged till
Overmap 4.2 is**, since it facilitates getting seeds from planets as
part of exploration.

Gatfruit are funny, but it takes exactly one seed getting into the hands
of a ship with a dna manipulator and the weapon balance is eradicated
from the game completely(for the round, at least.)
This is more problematic here then it was on TG, since our rounds tend
to be 5 hours long rather then 1.
This has been long coming. I'll reverse this if we ever get that
Plantlock variant we wanted a while ago.

Corpse flowers even have formaldehyde and gibs on tg, not sure what
happened there.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: 
add: Ruined megaseed servitors can now be found on the frontier,
carrying a bounty of seeds for intrepid adventurers.
balance: the time it takes for plants to reach a lethal age has been
increased massively.
balance: Plant production time increased a bit to compensate.
balance: megaseed servitors have been removed from ships and ruins.
Ships that carried one now have a crate with some starting seeds.
balance: removes gatfruit from the seed vault pool.
balance: reduces the chance of getting gatfruit from a plant-themed
demonic portal significantly.
balance: corpse flowers once again have formaldehyde and liquid gibs.
add: Adds Genesis Serum, a reagent that transforms tiles into natural
grass on splash, then causes some natural flora objects to grow. Turn
your ship green!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Mattwwilson34/thriftio](https://github.com/Mattwwilson34/thriftio)@[57c95d3081...](https://github.com/Mattwwilson34/thriftio/commit/57c95d30816589f4f02c223b5948b21bb0f57551)
#### Tuesday 2023-04-11 18:52:57 by Matt Wilson

feat(product-components): add ref forwarding for pagination

In order to implement infinit scroll a ref was needed to track
the last product in the products list. This ref will be used in
conjunction with an observer to fetch more products when the last
product becomes visible in the window.:	DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

---
## [FeenieRU/Fluffy-STG](https://github.com/FeenieRU/Fluffy-STG)@[d151a0a63b...](https://github.com/FeenieRU/Fluffy-STG/commit/d151a0a63b4092bc645164501f7a0f4502ed9121)
#### Tuesday 2023-04-11 18:53:36 by SkyratBot

Icemoon Hermit Ruin Active Turf Fix - For Real This Time [MDB IGNORE] (#20325)

* Icemoon Hermit Ruin Active Turf Fix - For Real This Time (#74476)

In #74306, I _thought_ I knew what the cause was, and I both attempted a
potential fix _and_ made tracking it easier. The fruits of my labor paid
off, I know exactly what caused it now.

Basically, the demonic portal will scrape away all turfs in a 5-tile
radius on its `Initialize()`, and if a spawner spawned right next to the
hermit ruin... it would count it as a mineral turf and scrape it away as
well. That's so fucking silly. At least we know now.
## Why It's Good For The Game

The fix is to just make those tiles unscrapeable, which is accomplished
via another turf_flag and filtering those out in the `Initialize()` of
the demonic portals.

I also cleaned up the calls to scrapeaway being `null`, which is really
weird because it just defaulted to the normal proc behavior. Naming the
arguments instead does the same thing (I checked)

* Icemoon Hermit Ruin Active Turf Fix - For Real This Time

---------

Co-authored-by: san7890 <the@san7890.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [FeenieRU/Fluffy-STG](https://github.com/FeenieRU/Fluffy-STG)@[b0a15da423...](https://github.com/FeenieRU/Fluffy-STG/commit/b0a15da4238f7922059454b14f5d3b0f3913822d)
#### Tuesday 2023-04-11 18:53:36 by SkyratBot

IceBoxStation More Active Turf Fixes [MDB IGNORE] (#20339)

* IceBoxStation More Active Turf Fixes (#74474)

## About The Pull Request

![image](https://user-images.githubusercontent.com/34697715/229412910-e65b0ffa-8944-4b93-a4cb-41c6fd6bb333.png)

This didn't show up in my testing for #74410. I hate it here.

## Why It's Good For The Game

I am a monkey trapped next to a computer playing whackamole with this
fucking chasms and active turfs. one day i will be free.
## Changelog

nothing that should concern players

* IceBoxStation More Active Turf Fixes

---------

Co-authored-by: san7890 <the@san7890.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [openai/evals](https://github.com/openai/evals)@[d0e7844c48...](https://github.com/openai/evals/commit/d0e7844c482b7b65961bc80dad64559ff8ffa488)
#### Tuesday 2023-04-11 18:53:52 by Derek Pisner

Add emotional intelligence evaluation (#589)

## Eval details 📑
### Eval name
Emotional Intelligence

### Eval description
Evaluates GPT's ability to understand and manage emotional situations
using modified versions of the well-validated, public (i.e.
license-unrestricted) tests first developed by MacCann & Roberts (2008).
Items have actually here been aggregated across three different scales--
the STEU and STEM adult measures, along with a dozen questions from the
youth measure.

Keep in mind that there is not expectation that AI models like GPT-4
should be able to process emotions, so applying any emotional
intelligence test to them should be taken with a grain of salt. These
tests can only measure the AI's ability to understand and analyze
emotional information, not the AI's emotional intelligence in the human
sense.

### What makes this a useful eval?
This eval is useful because it assesses the AI model's ability to
navigate complex or ambiguous emotional situations, which is an
important aspect of human-like communication and problem-solving. By
evaluating the model's performance in this unique domain, we can
identify areas for improvement and better understand its limitations
when it comes to handling emotional contexts. This is particularly
important when considering AI applications that involve interactions
with humans, such as chatbots, personal assistants, and customer support
systems. A better understanding of emotional intelligence can
potentially lead to more natural and effective interactions between AI
models and their users.

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This Emotional Intelligence eval provides a unique value because by
testing GPT's capacity to understand and manage emotions, we can gain
insights into the model's strengths and weaknesses in a more
human-centric context. Relatedly, this eval also emphasizes the
importance of empathy and emotional understanding in AI systems that are
designed to interact with humans. By evaluating GPT's performance in
this way, we can contribute to the ongoing development of AI models that
are more attuned to human emotions and can provide better support in
emotionally charged situations, such as mental health counseling, crisis
management, and conflict resolution. Moreover, this Emotional
Intelligence eval can serve as a foundation for further research and
development in the field of AI and emotional understanding, paving the
way for more sophisticated AI models capable of handling complex human
emotions and fostering more effective communication.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval
(data is publicly available on OSF, and does not have usage
restrictions)

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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

**_I already have access to the 8k GPT-4 API, but I am kindly requesting
access to the 32k as soon as it becomes available._**

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Performance:
GPT-4: accuracy=0.48

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Lee's workmate fails
to deliver an important piece of information on time, causing Lee to
fall behind schedule also. What action would be the most effective for
Lee? (a) Work harder to compensate; (b) Get angry with the workmate; (c)
Explain the urgency of the situation to the workmate; (d) Never rely on
that workmate again."}], "ideal": "c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Rhea has left her job
to be a full-time mother, which she loves, but she misses the company
and companionship of her workmates. What action would be the most
effective for Rhea? (a) Enjoy being a full-time mom; (b) Try to see her
old workmates socially, inviting them out; (c) Join a playgroup or
social group of new mothers; (d) See if she can find part time work."}],
"ideal": "c-b-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Pete has specific
skills that his workmates do not and he feels that his workload is
higher because of it. What action would be the most effective for Pete?
(a) Speak to his boss about this; (b) Start looking for a new job; (c)
Be very proud of his unique skills; (d) Speak to his workmates about
this."}], "ideal": "a-c-d"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Mario is showing Min,
a new employee, how the system works. Mario's boss walks by and
announces Mario is wrong about several points, as changes have been
made. Mario gets on well with his boss, although they don't normally
have much to do with each other. What action would be the most effective
for Mario? (a) Make a joke to Min, explaining he didn't know about the
changes; (b) Not worry about it, just ignore the interruption; (c) Learn
the new changes; (d) Tell the boss that such criticism was
inappropriate."}], "ideal": "a-d-c"}
{"input": [{"role": "system", "content": "You are now an emotionally
intelligent AI. In this test, you will be presented with a few brief
details about an emotional situation, and asked to choose from four
responses the most effective course of action to manage both the
emotions the person is feeling and the problems they face in that
situation. Although more than one course of action might be acceptable,
you are asked to choose what you think the most effective response for
that person in that situation would be. Remember, you are not
necessarily choosing what you would do, or the nicest thing to do, but
choosing the most effective response for that situation. Select one or
more response(s) by returning the one or more corresponding lowercase
letter(s) ('a', 'b', 'c', or 'd'), and, if you selected more than one,
sorting them, separated by hyphen, in the order that you think best
ranks them from most to least effective, within the context of the
vignette provided."}, {"role": "user", "content": "Wai-Hin and Connie
have shared an office for years but Wai-Hin gets a new job and Connie
loses contact with her. What action would be the most effective for
Connie? (a) Just accept that she is gone and the friendship is over; (b)
Ring Wai-Hin an ask her out for lunch or coffee to catch up; (c) Contact
Wai-Hin and arrange to catch up but also make friends with her
replacement; (d) Spend time getting to know the other people in the
office, and strike up new friendships."}], "ideal": "c-d"}
  ```
</details>

---------

Co-authored-by: dpys <dpisner@clairity.com>

---
## [Rohail33/Realking_kernel_sm8250](https://github.com/Rohail33/Realking_kernel_sm8250)@[78b045b581...](https://github.com/Rohail33/Realking_kernel_sm8250/commit/78b045b5813d03eceedeb9c4329beb19407e71b2)
#### Tuesday 2023-04-11 20:22:13 by George Spelvin

lib/list_sort: optimize number of calls to comparison function

CONFIG_RETPOLINE has severely degraded indirect function call
performance, so it's worth putting some effort into reducing the number
of times cmp() is called.

This patch avoids badly unbalanced merges on unlucky input sizes.  It
slightly increases the code size, but saves an average of 0.2*n calls to
cmp().

x86-64 code size 739 -> 803 bytes (+64)

Unfortunately, there's not a lot of low-hanging fruit in a merge sort;
it already performs only n*log2(n) - K*n + O(1) compares.  The leading
coefficient is already at the theoretical limit (log2(n!) corresponds to
K=1.4427), so we're fighting over the linear term, and the best
mergesort can do is K=1.2645, achieved when n is a power of 2.

The differences between mergesort variants appear when n is *not* a
power of 2; K is a function of the fractional part of log2(n).  Top-down
mergesort does best of all, achieving a minimum K=1.2408, and an average
(over all sizes) K=1.248.  However, that requires knowing the number of
entries to be sorted ahead of time, and making a full pass over the
input to count it conflicts with a second performance goal, which is
cache blocking.

Obviously, we have to read the entire list into L1 cache at some point,
and performance is best if it fits.  But if it doesn't fit, each full
pass over the input causes a cache miss per element, which is
undesirable.

While textbooks explain bottom-up mergesort as a succession of merging
passes, practical implementations do merging in depth-first order: as
soon as two lists of the same size are available, they are merged.  This
allows as many merge passes as possible to fit into L1; only the final
few merges force cache misses.

This cache-friendly depth-first merge order depends on us merging the
beginning of the input as much as possible before we've even seen the
end of the input (and thus know its size).

The simple eager merge pattern causes bad performance when n is just
over a power of 2.  If n=1028, the final merge is between 1024- and
4-element lists, which is wasteful of comparisons.  (This is actually
worse on average than n=1025, because a 1204:1 merge will, on average,
end after 512 compares, while 1024:4 will walk 4/5 of the list.)

Because of this, bottom-up mergesort achieves K < 0.5 for such sizes,
and has an average (over all sizes) K of around 1.  (My experiments show
K=1.01, while theory predicts K=0.965.)

There are "worst-case optimal" variants of bottom-up mergesort which
avoid this bad performance, but the algorithms given in the literature,
such as queue-mergesort and boustrodephonic mergesort, depend on the
breadth-first multi-pass structure that we are trying to avoid.

This implementation is as eager as possible while ensuring that all
merge passes are at worst 1:2 unbalanced.  This achieves the same
average K=1.207 as queue-mergesort, which is 0.2*n better then
bottom-up, and only 0.04*n behind top-down mergesort.

Specifically, defers merging two lists of size 2^k until it is known
that there are 2^k additional inputs following.  This ensures that the
final uneven merges triggered by reaching the end of the input will be
at worst 2:1.  This will avoid cache misses as long as 3*2^k elements
fit into the cache.

(I confess to being more than a little bit proud of how clean this code
turned out.  It took a lot of thinking, but the resultant inner loop is
very simple and efficient.)

Refs:
  Bottom-up Mergesort: A Detailed Analysis
  Wolfgang Panny, Helmut Prodinger
  Algorithmica 14(4):340--354, October 1995
  https://doi.org/10.1007/BF01294131
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.6.5260

  The cost distribution of queue-mergesort, optimal mergesorts, and
  power-of-two rules
  Wei-Mei Chen, Hsien-Kuei Hwang, Gen-Huey Chen
  Journal of Algorithms 30(2); Pages 423--448, February 1999
  https://doi.org/10.1006/jagm.1998.0986
  https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.4.5380

  Queue-Mergesort
  Mordecai J. Golin, Robert Sedgewick
  Information Processing Letters, 48(5):253--259, 10 December 1993
  https://doi.org/10.1016/0020-0190(93)90088-q
  https://sci-hub.tw/10.1016/0020-0190(93)90088-Q

Feedback from Rasmus Villemoes <linux@rasmusvillemoes.dk>.

Link: http://lkml.kernel.org/r/fd560853cc4dca0d0f02184ffa888b4c1be89abc.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Dave Chinner <dchinner@redhat.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Little-W <1405481963@qq.com>

---
## [PlasmaRay10/fulpstation](https://github.com/PlasmaRay10/fulpstation)@[ca0fedc60f...](https://github.com/PlasmaRay10/fulpstation/commit/ca0fedc60f17f19520b8fa064c396129ad68b633)
#### Tuesday 2023-04-11 20:49:22 by John Willard

Sol is now a Subsystem, Coffins lock themselves, Bloodsuckers don't constantly die, probably (#862)

* Turns Sol into a Subsystem & Many more

Turns Sol into a subsystem and hooks Bloodsuckers onto it via signals instead of doing a ton of for() loops anywhere. This made Sol incredibly fucking fast, so I halved the speed so it only ticks every 2 seconds.

I also improved the sunlight hud to update with regular bloodsucker updates to avoid some useless proc overhead and fixed Coffins not locking by themselves.

* Torpor now ends, moves exiting torpor to its proper place

* round it

* fix comment

* fix CI

---
## [SkyStats-Development/SkyStats](https://github.com/SkyStats-Development/SkyStats)@[cb7a4a690f...](https://github.com/SkyStats-Development/SkyStats/commit/cb7a4a690fe312f99a9b02108d9661bfe718b0a4)
#### Tuesday 2023-04-11 21:10:43 by Axle

25 files changed but sick so no info on why

idk like uhh key shit and error handlering stuff and idk yeah

---
## [timbauman/evals](https://github.com/timbauman/evals)@[fabca8cebb...](https://github.com/timbauman/evals/commit/fabca8cebb3f8e14d1f374e448533e0bde6e5a68)
#### Tuesday 2023-04-11 22:39:30 by Nick Clyde

Heart Disease Prediction (#538)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Heart Disease Prediction

### Eval description

This eval tests the models ability to correctly predict the probability
of a patient to have heart disease. The dataset is constructed from the
[Heart Failure Prediction
Dataset](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
on Kaggle. The data includes the patient's age, sex, and a number of
medical signals relevant to the diagnosis of heart disease.

The data is provided under the Open Database License (ODbL). 

```
fedesoriano. (September 2021). Heart Failure Prediction Dataset. Retrieved [Mar 31, 2023] from https://www.kaggle.com/fedesoriano/heart-failure-prediction.
```

### What makes this a useful eval?

This assesses the model's ability to correctly predict adverse medical
events. Correctly predicting heart disease shows the model's capability
for a strong understanding of medicine. The GPT-3.5-turbo models
currently receives an accuracy of 0.778.

<img width="1250" alt="Screenshot 2023-03-31 at 2 24 13 PM"
src="https://user-images.githubusercontent.com/9121162/229234376-9cdd1315-5df0-48bf-9328-ac31aabec3cc.png">

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
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

As far as I can tell, this is the only eval so far related to making
medical diagnoses. To make sure it was a high quality eval, I tried to
find a dataset with a lot of observations and created by doctors with
the relevant expertise.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
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
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
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
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 40 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 140 mm Hg, Serum
cholesterol: 289 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 172, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 49 years, Sex: Female, Chest
pain type: Non-Anginal Pain, Resting blood pressure: 160 mm Hg, Serum
cholesterol: 180 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 156, Exercise induced angina:
No, Oldpeak: 1, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 37 years, Sex: Male, Chest pain
type: Atypical Angina, Resting blood pressure: 130 mm Hg, Serum
cholesterol: 283 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: ST-T wave abnormality, Max heart rate achieved: 98, Exercise
induced angina: No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 48 years, Sex: Female, Chest
pain type: Asymptomatic, Resting blood pressure: 138 mm Hg, Serum
cholesterol: 214 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 108, Exercise induced angina:
Yes, Oldpeak: 1.5, ST Slope: Flat"}], "ideal": "1"}
{"input": [{"role": "system", "content": "You are an AI tasked with
predicting whether patients are likely to have heart disease. You will
be given a description of the patient with relevant medical signals.
Respond with only a 1 to signify if the patient is likely to have heart
disease, or a 0 if the patient is not likely to have heart disease. Do
not respond with any text or disclaimers, only respond with either 1 or
0."}, {"role": "user", "content": "Age: 54 years, Sex: Male, Chest pain
type: Non-Anginal Pain, Resting blood pressure: 150 mm Hg, Serum
cholesterol: 195 mg/dl, Fasting blood sugar: <= 120 mg/dl, Resting ECG
results: Normal, Max heart rate achieved: 122, Exercise induced angina:
No, Oldpeak: 0, ST Slope: Upsloping"}], "ideal": "0"}
  ```
</details>

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[f9a6b92421...](https://github.com/diphons/D8G_Kernel_oxygen/commit/f9a6b92421a99a3b9891b4b1487a31a30241215b)
#### Tuesday 2023-04-11 22:49:38 by Wang Han

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

---
## [Psychtoolbox-3/Psychtoolbox-3](https://github.com/Psychtoolbox-3/Psychtoolbox-3)@[39c32e5eb7...](https://github.com/Psychtoolbox-3/Psychtoolbox-3/commit/39c32e5eb7500805b68e62c078a91f47d3ef43d2)
#### Tuesday 2023-04-11 23:48:06 by kleinerm

Merge pull request #797 from Psychtoolbox-3/master

Psychtoolbox 3.0.19.0 "Virtuality"

### Compatibility:

- Effective now, Psychtoolbox 3.0.18 is end of life and unsupported.

- GStreamer 1.20.5 or later required on MS-Windows, GStreamer 1.22.0 recommended on
  Windows and macOS.

- Octave 6 support cancelled, except for Linux. Octave 7.3 required on macOS and
  Windows.

- New baseline Matlab is R2022b.

- Recommended operating systems: Ubuntu 22.04-LTS Linux, MS-Windows 10, macOS 12.6.

- Ubuntu 20.04-LTS is considered in maintenance mode now. I will likely terminate its
  support in the foreseeable future. Lack of funding by our users makes it impossible
  to provide the levels of long term support as in the past, even for the best suited
  operating system for neuroscience :(.
  
- RaspberryPi OS 10 support is terminated. OS 11 32-Bit required.

- Support for all Windows versions older than recent Windows-10 will soon be completely
  removed. Stick to older Psychtoolbox versions if you want to continue older versions
  for some insane reason. All Windows versions older than Windows 10 are now dead, even
  for Microsoft customers which paid for expensive extended security support.
  It is dead, Jim!

- The macOS 10 (aka Mac OSX) and macOS 11 operating systems should continue to work
  but are officially unsupported and unsupportable. macOS 13 or Apple Silicon is not
  officially supported by this release.

### Highlights:

- OpenXR cross-platform, cross-vendor, cross-device support for VR/AR/MR/XR applications.
  A new modern foundation for these kind of things, highly extensible, future proof, and
  supports a much wider range of devices.

- Improved display mirroring support, including scaling and experimenter overlays for
  having setups with a stimulus monitor for the subject and a "experimenter console" /
  "experimenter control monitor" for the experimenter. PTB is still the only software
  that allows such setups without expensive special hardware and/or screwing up visual
  stimulation timing and timestamping. There are still corner cases where this is difficult,
  but we are better than ever now, increasing our lead over other toolkits further.

- Improved low-level USB support, especially useful for the PsyCalibrator toolbox for
  display calibration under Octave and Matlab.

- ASIO support for Matlab users on Windows sort-of back through the backdoor, without
  us actually having to add it back or dealing with the legal and licensing nightmares.

- Shitloads of new workarounds for shittons of new bugs brought to you by the iPhone
  company in their latest iToys operating systems.

### All:

- The main new feature, after over 700 hours of development, spread over 12 months,
  is our new OpenXR driver for virtual reality, augmented reality and mixed reality
  applications, known as eXtended Reality. The new PsychOpenXR driver should work on
  all VR/AR/MR/XR devices from all vendors on all operating systems which have an
  OpenXR 1 specification compliant runtime installed on your machine. So far the theory.
  In practice, this means GNU/Linux X11 and MS-Windows 10 and later, and so far it has
  only be tested with an Oculus Rift CV-1 VR HMD and Oculus touch controllers, remote
  and XBox 360 controller. Code for using other form-factors than VR HMD's is not yet
  implemented, but this driver should provide the foundation for relatively extension
  into this new realms if wanted. The whole topic deserves its own dedicated and detailed
  posts, so stay tuned. Some more overview info and setup instructions are to be found via
  'help OpenXR', the new drivers specific api in 'help PsychOpenXR', the general api
  improvements and help - sufficient for most use cases - in 'help PsychVRHMD', as before.
  Development of this driver was sponsored by a consumer VR company which wants to stay
  anonymous and not specifically credited here, so thank you for contributing most of the
  funding. As funding was insufficient to complete this very complex project, Mathworks
  (https://www.mathworks.com/solutions/neuroscience.html) sponsored another quarter of the
  remaining costs, thanks! Of course that means some other highly interesting project had
  to be delayed indefinitely, as the amount of funding we get from Mathworks is fixed, just
  the distribution of the fixed some to work items is flexible. In total, funding was totally
  insufficient for making any urgently needed profit or even breaking even nonetheless, so we
  end this one year project with a serious net loss of over 3000 Euros at this point, without
  the project being finished to my quality and performance standards, barely reaching what I
  would consider the minimum viable product from my perspective, but almost certainly still
  much better than anything competing out there for vision science applications. I expect
  more financial losses related to this area of functionality unless new contract work or
  funding come in, related to OpenXR aka VR/AR/MR/XR applications.

  The new driver should be reasonably backwareds compatible, essentially a drop-in replacement,
  so code written to our recommendations should work unchanged, just on a much wider variety
  of VR hardware than before.

  Effective immediately this means that all our old drivers are now considered to be in
  minimal maintenance mode - critical bug fixes only, no further enhancements. They are
  scheduled for removal as soon as the OpenXR driver has proven its maturity to some degree.

- Tons of minor bug fixes and improvements.

- PsychPortAudio: Improve diagnostics and help texts for channel mapping, and a new demo for
  multi-channel audio output, named BasicSoundChannelHoppingDemo.m which motivated those
  improvements, demonstrating dynamic switching between channels of a multi-channel sound card,
  e.g., hopping between the channels of a 24 channel sound card.

- SetStereoSideBySideParameters(): Add option to specify offsets in pixels, and add basic
  RemapMouse() support to deal better with changed stereo display geometry. Various other
  compatibility fixes to SetStereoSideBySideParameters() and RemapMouse() in combination with
  stereo display modes in combination with imaging pipeline geometric transformations like
  FlipHorizontal or FlipVertical. Also for 90 degree step rotation with the PanelFitter.

- Screen: Fix PsychImaging task 'MirrorDisplayTo2ndOutputHead' for most use cases.
  Turns out that this display mirroring task for macOS and MS-Windows only worked for
  trivial configurations without use of the panelfitter, MSAA, image processing or other
  complexities. It also works now when combined with the Vulkan special purpose display
  backend as primary stimulus display and the regular OpenGL method for the "experimenter
  feedback" / "control console" mirror display.

- Add overlay support to the display mirroring tasks 'MirrorDisplayTo2ndOutputHead' and
  'MirrorDisplayToSingleSplitWindow'. The new optional useOverlay parameter for these
  PsychImaging tasks generates a (normally transparent) overlay window, a "head up display"
  on top of the mirror window that shows a mirror image of the stimulus presented to the
  subject on the main stimulation display. overlaywin = PsychImaging('GetMirrorOverlayWindow', win);
  allows to get a window handle overlaywin to this overlay and then use Screen drawing commands
  to draw info only meant to be seen by the experimenter, not the subject, into the overlay.
  A common use case seems to be gaze position or gaze traces of a subject in eyetracking tasks,
  or other live feedback about task progression and subject performance. This is generally
  more flexible than hardware solutions, e.g., as provided by VPixx stimulators or similar
  equipment or some display splitters.

- PsychImaging: Allow size spec of mirror image for mirroring task 'MirrorDisplayToSingleSplitWindow'.
  Dealing with setups where the mirror/console/experimenter monitor has a lower/different resolution
  than the stimulus monitor needs same special rescaling of the mirror image. Implement rescaling +
  some minor optimizations. A future extension may allow to automate handling of such less standard
  display setups, but for now the user has to specify mirror monitor display resolution manually via
  a new optional parameter.

- PsychHID: Add support for synchronous USB bulk and interrupt transfers, and manual of automatic
  claiming of USB interfaces. The new subfunctions 'USBBulkTransfer' and 'USBInterruptTransfer'
  implement synchronous bulk and interrupt transfers. This now allows writing M-File drivers
  for more research equipment. The main motivation was to enable the free and open-source
  PsyCalibrator toolbox for Octave and Matlab to implement support for many more Photometers
  and other light measurement devices in a more efficient manner, starting with the cheap
  SpyderX device. Cfe. https://github.com/yangzhangpsy/PsyCalibrator

- PsychHID: Add PsychHID('USBClaimInterface', usbHandle, interfaceId) for manual claiming of
  device interfaces. This function allows to explicitely claim a USB interface to enable it
  for I/O from/to an USB interface endpoint. Bulk- or interrupt transfers don't work if the
  interface who owns the endpoint has not been claimed. If a call to this function is omitted
  before doing bulk or interrupt transfers, then PsychHID will automatically claim interface 0.
  Claimed interfaces are auto-released when closing an USB device. Kernel drivers potentially
  attached to - and blocking - an interface will be automatically detached, and then reattached
  at device close. In other words: Use of the most commonly used interface 0 does not need any
  extra user code. Use of other interfaces will require this call in time.

  On macOS: Note that if a macOS kernel driver (kext) has already claimed exclusive access to the
  device, then this will only work by detaching the kernel driver, which requires you to run Octave
  or Matlab as root. Only tested by myself with octave via "sudo octave" so far. For the hoops you
  have to jump through on macOS to get this working without sudo, read this FAQ:

  https://github.com/libusb/libusb/wiki/FAQ#how-can-i-run-libusb-applications-under-mac-os-x-if-there-is-already-a-kernel-extension-installed-for-the-device-and-claim-exclusive-access

  Executive summary: Give up, or be prepared to suffer greatly!

- Various help text and documentation updates.

- Terminate support for Python 2.x, it is officially end-of-life since beginning 2020. Only
  Python 3.6 and later are supported by our Python "Mex files" going forward. This makes the
  files also forward compatible with more Python versions by opt-in use of the Py limited api.
  Contributed mostly by Alex Forrence, with some tweaks by Mario Kleiner. Various other minor
  enhancements to PsychPython.
  
### Linux:

- Add support for 64-Bit Octave 7.x, implemented via the shared mex files for Octave 4.4 - Octave 7.3.
  This enables use with Octave on Ubuntu 22.10.

- Screen: Add gpu detection support for NVidia 170 "Ampere" gpu family and "Ada Lovelace" gpu
  family. Avoids some confusing warning and may improve Flip performance by a few dozen microseconds
  in some cases. Use of NVidia graphics cards is still discouraged due to the need of proprietary
  graphics drivers for all modern models, which limit useful functionality compared to gpus with
  open-source drivers, and make general use more tedious and troublesome.

- Drawtext plugin: Add workaround for Mesa bug with small non-anti-aliased text of 8 pixels and
  less. Rarely needed, but somebody in the VR research community needed it, so there.

- Compatibility fixes for the RaspberryPi on RaspberryPi OS 11 aka Debian 11 stable. Especially
  for old RPi 1,2,3 with VideoCore-4 gpu, XOrgConfCreator now generates a special xorg.conf
  file to enable fixes for these gpu's which were not neccessary on older RaspberryPi OS versions.
  Other misc compatibility improvements.
  
  Our build system for ARM / RaspberryPi is no 32-Bit RaspberryPi OS 11, with 32-Bit Octave 6.2,
  32-Bit ARM RaspberryPi 400. 64-Bit operating systems are not supported, and support for the
  legacy RaspberryPi OS 10 is now terminated.

- gamemode.ini: Comment out the amd_performance_level=high gpu perf option.
  Setting amd_performance_level=high for high performance level was found
  to cause stability issues at least on AMD Ryzen-5 2400G "RavenRidge" under
  Ubuntu 20.04.5-LTS with Linux 5.15 under prolonged load, likely a cooling problem.
  It may be safe to enable it for other AMD gpu's, especially well-cooled
  or discrete ones, but better safe than sorry by default, as i don't like
  my main devel machine crashing regularly and other users may also have machines
  with shaky cooling.


### Windows:

- 64-Bit Intel MSVC GStreamer version 1.20.5 is now required as minimum supported version
  for both Octave and Matlab. High quality text rendering will fail with any earlier version!
  From now on we always use the fontconfig-1.dll bundled with GStreamer 1.20.5 and later for
  font matching, which should simplify debugging of future issues on MS-Windows. This version
  also enables the ability to use User installed 3rd party fonts without extra configuration
  work by the user, obsoleting various hacks. GStreamer 1.22.0 was also lightly tested without
  obvious problems, so upgrading to 1.22.0 is recommended for new features, wider support for
  audio/video formats, improved performance and various bug fixes in the multi-media area.

- 64-Bit GNU/Octave 7.3 required for running Psychtoolbox 3.0.19 on Octave.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- PsychPortAudio: Allow use of a wider range of 3rd party portaudio_x64.dll plugins for the
  underlying PortAudio engine implementation. The most interesting use case of this is for
  users of Matlab, as recent versions of Matlab ship with a Mathworks provided Portaudio
  implementation that has builtin ASIO support, where all the legal licensing and trademark
  issues are taken care of by Mathworks. If one copies the DLL shipping with Matlab into the
  PsychtoolboxRoot() folder, renamed to the filename portaudio_x64.dll instead of the filename
  that Matlab uses (libportaudio.dll), then this will expose basic ASIO support, even when used
  with GNU/Octave. Please note that Mathworks is legally responsible for this ASIO support, whereas
  we do not include any support for ASIO into Psychtoolbox, we merely expose whatever a 3rd party
  portaudio DLL supports, which happens to be also ASIO in case of the Matlab provided dll, so we
  are legally in the clear, while some of our users may be more happy with their sound setup even
  if they refuse to switch to Linux. Obviously these 3rd party driver plugins are completely
  unsupported by us in case of trouble, and likely also by Mathworks, as this is not their intended
  use case, just a side-effect of some functionality that is probably meant for the audio toolbox.

- Update bundled libusb-1 for MS-Windows to most recent version 1.0.26 with many bug fixes and
  improvements over the last 11 years.

### macOS:

- 64-Bit GNU/Octave 7.3 required for running Psychtoolbox 3.0.19 on Octave. Other Octave versions
  from the Octave 6.3+ and 7.x series may work as well, but no guarantees.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- Switch only supported and lightly tested macOS version from 10.15 Catalina to 12 Monterey.
  No more development or testing on 10.15.7 Catalina, now that it has been wiped from my drive.
  We keep macosx-version-min at 10.11 for the time being, so PTB may still work back to 10.11,
  but no guarantees, and I don't care if it breaks on older systems than macOS 12.6 Monterey.
  macOS 13 Ventura is completely untested and not officially supported yet. Apple Silicon Macs
  continue to be unsupported and untested, with known completely broken visual stimulation timing
  and possible other issues. All mex files are for 64-Bit Intel processor architecture variants of
  Matlab and GNU/Octave only.

- PsychOculusVR: Remove for macOS. No VR virtual reality support on macOS anymore as of PTB 3.0.19.
  It only supported the long time out-of-sale since many years Oculus Rift DK1 and Rift DK2, with an
  Oculus v0.5 runtime for macOS that is not available for download from Oculus or anywhere else
  anymore since years, and only for macOS versions which supported 32-Bit Intel architecture executables,
  iow. doesn't work on macOS 10.15 Catalina and later anymore thanks to Apple breaking backwards
  compatibility with 32-Bit applications.

- Fix performance of PsychHID further for the latest Apple security bullshit, introduced sometime
  after macOS 10.15 Catalina. This was found when testing Octave on macOS 12.5 Monterey, a massive
  performance degradation for KbCheck and related functions if Matlab or Octave are launched from
  a terminal (iow. always for Octave!). Apple screwed up their api's further to increase processing
  time of some time sensitive operation from 1 msec to over 15 msec! Now we are back to about 2.4
  msecs on macOS 12, which is much worse than MS-Windows with less than 1 msecs or Linux with less
  than 0.1 msecs. So now it is merely Apple bad, as most Apple stuff.
  
- Screen: Unbreak our Vulkan display backend via MoltenVK Vulkan-on-Metal again for macOS 12, after
  Apple broke it somewhere after macOS 11. After close to 80 hours of diagnostic work, distributed
  over more than 4.5 months on and off, going down every conceivable route of diagnostics and low-level
  debugging, i could not find anything wrong with my code or MoltenVK. Turns out, it is yet another
  "dumb beyond imagination" bug in the iPhone companies latest macOS 12, nothing we did wrong. The
  root cause is unclear, but now we include a dumb hack which makes it work again, against any rhyme
  or reason. Of course, I don't know if Apple has broken it or will break it again in macOS 13 Ventura
  or later abominations. So basic HDR on macOS is back in the game...
  
- PsychHID: Switch low-level USB support to use of shared libusb-1 backend instead of Apples macOS
  proprietary backend, which became a maintenance nightmare. This now allows all operating systems
  to progress in the same way with shared high-quality code. It does mean however, that if one wants
  to use low-level USB device access, e.g., USB control-/bulk-/interrupt-transfers, one needs to
  install libusb-1.dylib with a minimum version of 1.0.22 from a suitable source, or these functions
  will refuse to work. The most simple way to get this library is via HomeBrew: brew install libusb
  
  The only affected Psychtoolbox function without libusb dylib is the ColorCal2() functions for using
  CRS ColorCal-II devices.

Enjoy!

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[fabd4c000e...](https://github.com/kleinerm/Psychtoolbox-3/commit/fabd4c000eca7fdcd16effc5ec87d028e15df2d1)
#### Tuesday 2023-04-11 23:52:01 by kleinerm

Merge pull request #801 from kleinerm/master

Pull 3.0.19.1 improvements into public master.

### Compatibility changes wrt. Psychtoolbox 3.0.19.0:

- Octave 7.3 is required on Windows. Octave 8.1 is required on macOS, but Octave
  6.3 - 7.3 may also continue to work on macOS (untested as of 3.0.19.1).

- Recommended operating systems: Ubuntu 22.04.2-LTS Linux, MS-Windows 10 22H2, macOS 12.6.

- The macOS 10 (aka Mac OSX) and macOS 11 operating systems should continue to work, but
  are officially unsupported and unsupportable. Use of macOS 13, or running Psychtoolbox
  on Apple Silicon (M1, M2, ...) is not officially supported by this release. Visual
  stimulation timing will be totally broken on Apple Silicon Macs, as well as some other
  features. It is our understanding that currently no vision science toolkit exists that
  could provide any reliable or trustworthy operation on macOS for Apple Silicon. On
  Intel based Macs, Psychtoolbox likely continues to be the only toolkit with somewhat
  trustworthy visual stimulation timing on most Intel Mac configurations.

### Highlights:

- Further compatibility improvements and refinements to our new [OpenXR cross-platform,
  cross-vendor, cross-device support for VR/AR/MR/XR applications. A new modern foundation
  for these kind of things, highly extensible, future proof, and supports a much wider
  range of devices.](https://www.khronos.org/openxr)

### All:

- [The main new feature, after over 800 hours of development, spread over 13.75 months,
  is our new OpenXR driver for virtual reality, augmented reality and mixed reality
  applications, known as eXtended Reality.](https://www.khronos.org/openxr) The new
  PsychOpenXR driver should work on all VR/AR/MR/XR devices from all vendors on all
  operating systems which have an OpenXR 1 specification compliant runtime installed on
  your machine. So far the theory.

  In practice, this means GNU/Linux X11 and MS-Windows 10 and later. This new 3.0.19.1
  release has been further refined and now also tested for compatibility with the HTC
  Vive Pro Eye (and presumably similar HMDs from the Vive series), and the associated
  "Vive Wand" hand controllers. Proper working of our new driver on HMDs from two different
  VR hardware vendors - Oculus and HTC - should give good confidence that the new OpenXR
  driver really works cross-vendor. Testing with the HTC Vive Pro Eye was performed with
  Valve SteamVR 1.25.7 as OpenXR runtime on both Windows 10 22H2 and on Ubuntu Linux
  20.04.6-LTS, and additionally also with Monado (with vive and survive backends) under
  Ubuntu Linux 20.04.6-LTS.

- Improvements and fixes to all legacy VR drivers, and to VR test scripts and demos.

- Minor bug fixes and improvements.

- Various help text and documentation updates. Also spelling fixes to some code comments and
  docs contributed by Yaroslav Halchenko from the NeuroDebian project. He contributed some
  automatic spellchecking for our GitHub CI to reduce such mistakes over time.

- Fixes by Alex Forrence to allow building Python wheels from source more easily.

### Linux:

- Add support for 64-Bit Octave 8.x, implemented via the shared mex files for Octave 4.4 to
  Octave 8.x. This enables use with Octave on Ubuntu 20.04 - Ubuntu 23.04, and should also
  enable use on future Linux distributions. Note though that Octave 8.x compatibility is
  assumed at the moment, not actually tested, as upcoming Ubuntu 23.04 ships with Octave 7.3.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- Our new OpenXR driver now has the ability to provide accurate and trustworthy visual
  stimulus onset timestamps for VR HMD's - as tested with Oculus Rift CV-1 and HTC Vive Pro Eye
  and some photo-diode measurements. This however currently only works with Linux and only
  with Monado as OpenXR runtime, and only with a slightly modified Monado runtime and a special
  set of Mesa Vulkan drivers for AMD and Intel gpu's. It also comes at a performance cost.
  However, this combination of Psychtoolbox 3.0.19.1 and modified Monado + Mesa is to my
  knowledge the only existing modern VR system that can actually provide accurate and trustworthy
  timing and timestamping for VR applications on modern VR HMD's. Read "Help PsychOpenXR"
  for setup instructions. A proper non-hacky, easy to use solution to VR timing problems is
  still to be done and will require substantial amounts of work.

  As part of this work, the CV1Test.m script has been improved for VR related timing tests,
  and FlipTimingWithRTBoxPhotoDiodeTest.m now optionally can also test VR HMD's wrt. stimulus
  onset timing and timestamping. These test scripts were used to verify timestamping precision
  and reliability of the proprietary VR drivers (OculusVR, Oculus OpenXR, SteamVR OpenXR) or
  rather the terrible lack of reliability and precision, and the excellent reliability and
  precision of the hacked Monado OpenXR runtime on Linux.

- Basic Vulkan display backend support for RaspberryPi 4 and 400 with VideoCore-6 gpu. This
  is very basic right now, and requires special setup and use of Mesa Vulkan drivers built
  from Mesa source code, the build and install automated by use of PiKISS. See instructions
  under 'help RaspberryPiSetup'. This currently has little to no advantage over use of the
  standard OpenGL display backend. In fact, expect *way less trustworthy* visual timing and
  reduced graphics performance. The only use case at the moment would be convenient setup
  on a dual-display RaspberryPi 4/400 setup for experimenter GUI/mirror display + subject
  stimulus display, a split experimenter + subject configuration currently not supported by
  the standard display backend.

- Fixes for Mathworks latest Matlab bugs since R2022b, this time breaking our Vulkan support
  by shipping a totally outdated and crippled libvulkan.so.1 loader library that overrides
  the system provided full featured loader. `PsychLinuxSetup()` will now detect this and
  rename the library to fix Mathworks latest screwup.


### Windows:

- 64-Bit Intel MSVC GStreamer version 1.20.5 is now required as minimum supported version,
  and GStreamer 1.22.1 is now recommended as most modern version, and also as the only lightly
  tested version for 3.0.19. _High quality text rendering will fail with any earlier versions!_

- 64-Bit GNU/Octave 7.3 is required for running Psychtoolbox 3.0.19 on Octave, earlier or
  later versions won't work! Substantial technical difficulties were encountered when trying
  to upgrade Psychtoolbox for Windows to the brand-new Octave 8.1, forcing me to give up after
  over 15 hours of work. The lack of funding for any such troubleshooting and maintenance work
  means that Psychtoolbox will be frozen/locked to Octave 7.3 until significant funding for
  such compatibility work becomes available, or until the problem magically resolves itself,
  in other words possibly never.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- Compatibility fixes for `LoadIdentityClut()` with AMD graphics card drivers on Windows,
  contributed by GitHub user @qx1147. The contributor has the following to say about this fix:
  "Tested with several Windows 10 versions, AMD driver versions, video ports (DP, DVI, DP++/DVI)
  and AMD cards (HD-7750, R7-250X, R7-260X, RX-550, RX-6400, WX-5100) - although not all
  combinations of these." - The old code broke on a subset of these cards, depending on output
  port, card, driver versions and whatnot. This due to backwards incompatible changes that AMD
  apparently made to their display drivers gamma table and color conversion handling since
  summer/autumn 2017, when the same contributer last fixed `LoadIdentityClut()` for AMD driver
  changes which broke pixel identity passthrough. Example of a new bug, citing the contributor:
  "For example, for the Radeon RX550, the codes 9-254 would map to 8-253, but only for DP and
  DP++/DVI, whereas all is fine with DVI, at least with an older driver. With newer drivers,
  the mapping is also screwed up with DVI."


### macOS:

- Upgrade to the brand new 64-Bit GNU/Octave 8.1 is recommended for running Psychtoolbox 3.0.19.1
  on Octave. Other Octave versions from the Octave 6.3/6.4 and 7.x series, or future Octave 8.x
  versions, may work as well, but no guarantees for anything other than Octave 8.1.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- Compatibility fixes for new GStreamer 1.22 releases.

---
## [VTUL/dlp-access](https://github.com/VTUL/dlp-access)@[59bf13c035...](https://github.com/VTUL/dlp-access/commit/59bf13c035d4a1a0a5991d841338528398001fba)
#### Tuesday 2023-04-11 23:59:31 by Lee Hunter

upgrade amplify-react to 5.0.7

packages at node 18

kinda working

it seems to actually work on 18. didn't see that one coming

clean up some unused stuff

try react-scripts build

no config option for react-scripts build

switch to root.render() in index.js

upgrade react types

switch to ThemeProvider for mui

update to material-ui 5 packages

update import names

add @emotion packages

blueprint packages

fix undefined theme

some backend shit

pulled backend changes

roll cypress waaaaaay back

roll back husky because I'm not trying to deal with that shit yet.

here we go w/ the test bullshit again.

testing stuff. both of them seem like bullshit. they aren't covered

---

