## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-09](docs/good-messages/2023/2023-02-09.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,411,105 were push events containing 3,682,684 commit messages that amount to 287,013,483 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 60 messages:


## [Floofies/Skyrat-tg](https://github.com/Floofies/Skyrat-tg)@[91f06a97d3...](https://github.com/Floofies/Skyrat-tg/commit/91f06a97d3f24c849241bf909b7de28b9b6ec951)
#### Thursday 2023-02-09 00:49:42 by candle :)

Small VoxPrimalis Fixes (#18944)

* fuck you i don't need to give you a fucking summary

* fixes

---
## [Floofies/Skyrat-tg](https://github.com/Floofies/Skyrat-tg)@[d95ca04819...](https://github.com/Floofies/Skyrat-tg/commit/d95ca048192f08a8fbaf524fdb4ab0ca498b319e)
#### Thursday 2023-02-09 00:49:42 by Rimi Nosha

[MODULAR] Fixes All Known Modular Persistence (NIF) Saving Issues (#19096)

* Fuck

* Holy shit

---
## [Floofies/Skyrat-tg](https://github.com/Floofies/Skyrat-tg)@[8500d62b79...](https://github.com/Floofies/Skyrat-tg/commit/8500d62b798a45812832be0c686f532f877f1e3a)
#### Thursday 2023-02-09 00:49:42 by SkyratBot

[MIRROR] Abductor scientist self-retrieve failure/runtime fix [MDB IGNORE] (#19179)

* Abductor scientist self-retrieve failure/runtime fix (#73172)

## About The Pull Request

Since the abductor outfit/implant would load before the abductor ship
(and it's teleport pad) when first generating a team, a runtime would
occur when trying to link the pad to the implant. Another would occur
every time you attempted to retrieve yourself (as the linked pad would
be null), preventing recall and completely neutering an abductor team's
most important maneuver.

Now, using the implant will perform the linking process again if no
linked pad is found, and provides the owner with a warning if (by some
great calamity) they genuinely have no pad to teleport back to. This
solves the issue of the implant sometimes not linking to a pad properly
on initialize, and makes them way less prone to breaking.

Apparently this has been broken for a while, presumably since the
abductor ship was made into a lazyloading template.
## Why It's Good For The Game

The funny silly grey men get to torture the poor hapless crew once
again.
## Changelog
:cl:
fix: abductor scientist's retrieval implants will now properly recall
the owner, and inform them upon recall failure.
/:cl:

* Abductor scientist self-retrieve failure/runtime fix

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[83275d8cdf...](https://github.com/pytorch/pytorch/commit/83275d8cdf7721285c4e1b921c28295dc215ba7c)
#### Thursday 2023-02-09 00:54:59 by Brian Hirsh

add torch.autograd._set_view_replay_enabled, use in aot autograd (#92588)

tldr; this should fix some minor perf regressions that were caused by adding more as_strided() calls in aot autograd.

This PR adds a new context manager, `torch.autograd._set_view_replay_enabled()`.

Context: AOT Autograd has special handling for "outputs that alias graph intermediates". E.g. given this function:

```
def f(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    return out
```

AOT Autograd will do the following:

```
def fn_to_compile(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    # return the graph intermediate
    return y, out

compiled_fn = compile(fn_to_compile)

def wrapper(x):
    y, out = compiled_fn(x)
    # regenerate the alias of the graph intermediate
    return out._view_func(y)
```

What's annoying is that `out._view_func()` will result in a `.as_strided` call, because `out` is an ordinary runtime tensor. This (likely?) caused a perf regression, because when running the backward, out `as_strided_backward()` is slower than our `view_backward()`.

In this PR, I added some TLS for instructing autograd to do view replay instead of as_strided, even when given a normal tensor. I'm definitely interested in thoughts from autograd folks (cc @albanD @soulitzer). A few points that I want to bring up:

(1) One reason that this API seems generally useful to me is because of the case where you `torch.compile()` a function, and you pass in two inputs that alias each other, and mutate one of the inputs. Autograd is forced to add a bunch of as_strided() calls into the graph when this happens, but this would give users an escape hatch for better compiled perf in this situation

(2) To be fair, AOT Autograd probably won't need this TLS in the long term. There's a better (more complicated) solution, where AOT Autograd manually precomputes the view chain off of graph intermediates during tracing, and re-applies them at runtime. This is kind of complicated though and feels lower priority to implement immediately.

(3) Given all of that I made the API private, but lmk what you all think.

This is a followup of https://github.com/pytorch/pytorch/pull/92255.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/92588
Approved by: https://github.com/ezyang, https://github.com/albanD

---
## [PreatB/tango_with_django_project](https://github.com/PreatB/tango_with_django_project)@[013bc978fb...](https://github.com/PreatB/tango_with_django_project/commit/013bc978fbb7e90740f6a6428e8bf3ee8ab9c460)
#### Thursday 2023-02-09 00:57:43 by “David

End of chapter 7. My life is becoming cloudy. Got called into work when they said i could have a day off. i spend 50 minutes in rush hour traffic and when i get there, there is no work. literally went home in 3 hours when it is normally an 8 hour shift. waste of everyones time honestly. 5 red bull (sugar free) deep right now and i want this done. heart failure before resitting the year

---
## [Nanu308/cmss13](https://github.com/Nanu308/cmss13)@[c7a33d5ff9...](https://github.com/Nanu308/cmss13/commit/c7a33d5ff9f4f7563145e82dd6cd0cd00f6b53c5)
#### Thursday 2023-02-09 01:34:37 by riot

PMC and Whiteout stuff (#1966)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

As a preword, I came up with every change in this PR and coded them in
the span of 10 hours, so some things may be iffy.

PMCs and Whiteout may be good, but they're a bit outdated, this
modernizes multiple loadout aspects, enables antag vendors for
admin-spawn, and does some balance changes to certain
portions(specifically chem ERT).

Individual changes, numbered, will go over each in why its good, may
have forgotten one or two things.

1. Buffs whiteout flamer with blue flame damage, belt-linked magharn,
and pyro underbarrel extinguisher
2. Adds a synthetic repair kit(medkit), with synth repair tools, gives
it to whiteout.
3. Adds breaching charges and swaps crowbars to tactical in whiteout
loadouts
4. Gives whiteout PMC sniper goggles(thermals)
5. Gives whiteout medic the required gear to actually repair a downed
member of the team, and just a lot of synth heals.
6. Gives whiteout leader a pyro extinguisher.
7. Gives whiteout weapons default attachments.
8. Adds an 'advanced' mini-flamer with the same stats as UPP integrated
UBF, gives it to NSG23 and random m41/2 attachie.
9. Gives detainer PMCs a version of the corporate m41A MK2(goon gun),
with attachies and adv flamer to replace flamethrower.
10. Swaps chem PMC TL P90(name is too long) with an M41/2
11. Gives normal PMC ERT roles a webbing vest with meds and
miniextinguisher
12. Gives PMC Surgeon the essentials required to act as a medic, swaps
NSG with M39/2, gives them a normal but unique look.
13. Whiteout and PMC SG powerpacks have 30k power by default, instead of
10k.
14. Gives PMC guns more options for random attachments, and gives m41/2
its intended collapsible stock
15. Gives PMC engi m39/2 instead of P90
16. Removes flamer from potential PMC loadouts.
17. Gives PMCs better CQC skill.
18. Gives PMC TLs autoinjector pouches(which gives chem TL a second
pouch in the first place)
19. Detainer PMCs now have tac-sechuds, PMC TLs have sensorhuds.
20. **Enables antag vendor for PMC roles.** (Look at file changes for
the specific things, too long for pr desc)

# Explain why it's good for the game

Modernization and some needed loadout/balance changes(IMO).
Per number:

1. Whiteout flamer did worse damage than napalm, and was incredibly easy
to lose.
2. More heals for each member of the whiteout team, allows more
self-sufficiency.
3. Breach charges for tacticool breaches, crowbar doubles as a melee
weapon in case the player doesn't know about synth punch
4. Whiteout didn't have proper NVG, thermals allows them to do
tacticooler breaches by lining up people wth breach charge.
5. Whiteout medic didn't have a lot of heals at all, and didn't have a
defib, so they weren't much of a medic.
6. To extinguish the flames and lead charges, works like pyro
underbarrel extinguisher, but handheld.
7. Default tacticool attachment, already made whiteout subtypes for
HEAP, why not give them good attachies with them too.
8. Mini-flamer sucks, gives a better version for NSG and m41/2, same
stats as the already existing UPP integrated UBF.
9. Detainers had flamers which sucked, gives them corpo m41s which
aren't as good as /2s, but have adv UBF for flames.
10. P90 sucks, having default m41/2 fits with other leader type, also
gives them a better gun than their underlings.
11. Medkit but in a webbing, its my personal combat webbing load when I
play so its good.
12. PMC Surgeon was horrifically undergeared, they didn't even have a
medhud, gives them basic gear similar to PMC med but with a beret to
tell them apart.
13. ERTs don't have spare batteries to get usually, more staying power
in fights.
14. More options for attachies to further make PMC weapons better, also
gives m41/2 the m41 collapsible stock because it needed it.
15. P90 sucks, support roles getting the m39/2 is cool.
16. Flamer sucks to get as PMC, and adv. UBF as a potential m41/2
attachie makes a full-sized flamer useless too.
17. PMCs could fireman carry, and multi-strip, but did it horrifically
slow, gives them MP level CQC(master for spec, expert for TL)
18. TL getting extra meds is neat, also chem TL had an empty pocket slot
and no meds, thats bad.
19. Sechud-thing for PMC detainers is useful(stops flashbang trolling
for one), giving PMC TL a sensorhud to watch their team's status is also
good.
20. Makes doing event bases for PMCs much easier, too long to post the
specific changes here but look at files for them.


# Testing Photographs and Procedure

I forgot to take screenshots but it all works. 👍 
I spawned myself as every changed role and tested every individual
change extensively.

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
add: PMCs are now able to use antag vendors.
balance: Multiple loadout and skill changes to PMCs and Whiteout
balance: Buffs whiteout flame damage to blue flame damage.
fix: PMC Investigator Lead now appropriately spawns with a medical pouch
in their pocket, instead of nothing.
fix: Maximum skill preset now appropriately also has BE and intel skill,
at maximum of course.
fix: PMC Smartgunner now appropriately a VP78 to go along with their
VP78 magazines
fix: Whiteout now appropriately have night vision.
fix: M41A/2 now appropriately comes equipped with a collapsible stock.
spellcheck: PMC smartgun drum now has a seperate description and name
from base SG to match its different appearance.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [dsmith328/LC13Master](https://github.com/dsmith328/LC13Master)@[f03f3f5d20...](https://github.com/dsmith328/LC13Master/commit/f03f3f5d200f089e603ceb9a5c953b044123169f)
#### Thursday 2023-02-09 02:00:31 by Lance

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

---
## [TheWolfbringer/tgstation](https://github.com/TheWolfbringer/tgstation)@[10a344bde0...](https://github.com/TheWolfbringer/tgstation/commit/10a344bde0d48fb250dcb7a9eb4a1e98b9bb6df5)
#### Thursday 2023-02-09 02:14:25 by Time-Green

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

### Why this is good for the game
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
## [TheWolfbringer/tgstation](https://github.com/TheWolfbringer/tgstation)@[36090c1b20...](https://github.com/TheWolfbringer/tgstation/commit/36090c1b206dee8b643e83607e333c29906b6bc8)
#### Thursday 2023-02-09 02:14:25 by san7890

Refactors Suicide Verb + Basic Mobs (actually all (most) living mobs) Can Now Suicide (#72919)

## About The Pull Request

On the tin. There was a lot of needless copy-paste and a lot of
single-letter vars and weird indentation and... well just all of it was
at least eight years old. So, I decided to "abstract" as much as I could
of it out instead of piling onto the big copypaste clusterfuck for
implementing basic mob suicide.
## Why It's Good For The Game

Fixes #72903

Having more procs that can be easily repeatably called to the same
results is much better than having to transplant the same exact three
lines everywhere. It's also a good first step to further in-depth
behavior by allowing sub-type overrides of certain procs (which is quite
nice). Just feels more extensible overall for the next guy who wants to
add funny suicide behavior whenever they might come around.

There's probably a few better ways to do what I did, but I wrote code
comments explaining why I did what I did. I think there's a few ways to
make it more agnostic, but I think that'll be another can of worms that
will bloat out an already quite large PR. Let's just get the framework
set.

(this refactor should also make it quite easy to unit test suicide
actions :eyes:)
## Changelog
:cl:
fix: All Mobs (including Basic mobs) are now able to suicide. (warning:
some exclusions remain)
/:cl:

---
## [PreatB/tango_with_django_project](https://github.com/PreatB/tango_with_django_project)@[462d8e821c...](https://github.com/PreatB/tango_with_django_project/commit/462d8e821cb0baeecfde4685e0e090496954611d)
#### Thursday 2023-02-09 02:42:01 by “David

Chapter 8 done. Dont hate my life as much honestly but apparently 9 is really long ;). current song playing is dream on by aerosmith

---
## [insertnamehere123/Skyrat-tg](https://github.com/insertnamehere123/Skyrat-tg)@[1fe9efd00a...](https://github.com/insertnamehere123/Skyrat-tg/commit/1fe9efd00aeb0e2d4f4dedf89460abacecef9d1b)
#### Thursday 2023-02-09 02:54:44 by SkyratBot

[MIRROR] Rebuilds Luxury Shuttle (mostly), makes it emag-only [MDB IGNORE] (#19229)

* Rebuilds Luxury Shuttle (mostly), makes it emag-only (#72940)

## About The Pull Request
![2023 02 07-06 49
54](https://user-images.githubusercontent.com/70376633/217159751-790e6ded-8525-4d13-a5b5-6a3d8076a00e.png)
Changes the really goofy old lux shuttle to a cooler layout with some
additions to make it a luxury and not just
"anti-poor-people protection + food"

Shuttle was made bigger to make it less cramped for the luxury class,
pool was moved to its own room, added an arcade
and a bar corner, has real lasers to shoot poors with (20c each shot),
has fire extinguishers now
Adds a new preopen variant of hardened shutters
Adds a paywall pin subtype for the luxury shuttle, and a laser gun
subtype

Made emag-only at a price of 10000 credits
## Why It's Good For The Game

The old luxury shuttle looked REALLY awful with its pool, was pretty
cramped even in the luxury section and BARELY resembled a luxury..
This luxury shuttle provides luxuries such as a less poorly designed
pool, more space for legs, arcade, to make it resemble a luxury unlike
the old one

## Changelog
:cl:
add: Luxury Shuttle is now bigger, and less ugly! Poor people still get
it rough though...
/:cl:

* Rebuilds Luxury Shuttle (mostly), makes it emag-only

---------

Co-authored-by: jimmyl <70376633+mc-oofert@users.noreply.github.com>

---
## [Gabibag/possiblyNotGood](https://github.com/Gabibag/possiblyNotGood)@[3d0478030c...](https://github.com/Gabibag/possiblyNotGood/commit/3d0478030c843f00e832a0eef855d7cf8d4ed7cf)
#### Thursday 2023-02-09 03:09:18 by Gabibag

Bro. It took me like 5 hours to fix the damn boss check. I hate my life.

---
## [Ajengnilta/My-Portfolio](https://github.com/Ajengnilta/My-Portfolio)@[8bbd3e26ad...](https://github.com/Ajengnilta/My-Portfolio/commit/8bbd3e26ad13903aa1240c6dc430bf1efb444c2b)
#### Thursday 2023-02-09 03:31:41 by Ajeng Nilta Adriani

Add files via upload

Hello Everyone!

After 3 months of challenging phase in bootcamp, I finally graduated from Hacktiv8 Full Time Data Science Program. With solid material every day and weekly project assignments that had to be completed with tight deadlines, but I really enjoyed it and was able to finish bootcamp well because this is my passion and career that I want to achieve. I've learned a lot about Python, Data Analytics, Machine Learning, Deep Learning, Natural Language Processing, Computer Vision, SQL, Web Scrapping, a little of full stack concept, and etc. Not only that, but I also learned about model deployment, which is a very important skill for a data scientist. Those thing are so challenging, and I'm excited to learn more about data science stuff.

As a final project of my bootcamp completion, me and my teammates : Aan Nurliyanah, Ropiudin, Fachmi Maris and Muhammad Fawwaz Dynoeputra makes an project called “Anminvesting” Mutual Fund Investment Recommendation system Based on Risk Profile Customer. Anminvesting a system utilized machine learning, and created a risk profiling for upcoming new investors that are interested in investing on Mutual Funds. From the risk profiles we recommend the best products that suit their needs. And new investors can see the high and low price forecasting from products for up to 4 weeks ahead based on the last 5 years datas.

Even though I have been able to complete the bootcamp very well, data science technology is developing very quickly every time, so I always have to learn new things to sharpen my knowledge of data science.

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[27c35bfa0b...](https://github.com/lessthnthree/tgstation/commit/27c35bfa0b11a7248314cc057b70c6a0729794bf)
#### Thursday 2023-02-09 04:26:32 by MrMelbert

Fixes all antag datum moodlets being removed when any single antag datum is removed (#73305)

## About The Pull Request

All antag datums operated under the `antag_moodlet` mood category, which
is clearly an issue when you can (and commonly) have multiple antag
datums of different types on your mob.

New antag datums of different type will now no longer override older
antag datum moodlets, now they will stack. This means traitor
revolutionaries are the most zealous folk on the station.

This has a few potential oversights down the line: 
- Someone adds an antag datum players can have duplicates of, and also
has a moodlet associated
- Re-used moodlets in antag datums that can easily be stacked will be
noticed
- Most solo antags used `focused` right now, but none can stack outside
of admemes

But I don't think it's an issue for now.

## Why It's Good For The Game

Prevents a quick revolution from stripping you of your joy. 

Fixes #67313

## Changelog

:cl: Melbert
fix: Revolutionary Heretics and Cultists Traitors no longer lose all of
their joy in life after being de-converted from their respective causes.
/:cl:

---
## [mathhis/discord-api-docs](https://github.com/mathhis/discord-api-docs)@[dd3f05a170...](https://github.com/mathhis/discord-api-docs/commit/dd3f05a1709add398bac3a68af3cc27287f67038)
#### Thursday 2023-02-09 04:30:19 by Jerry Jiang

Document Silent Messages. (#5910)

Hey folks!

This is actually my 2022 hackweek project which I got to finish to
completion. :)

During a message send request, if you include the new
`SUPPRESS_NOTIFICATIONS` flag it will not broadcast any push/desktop
notifications but will still increment the relevant mention counters.

The intention is that you can get someone's attention but not feel like
you could be distracting them. Like when you DM someone at 5am. I'm sure some
bots can leverage this as well to avoid noise or something.

Also this should work for the webhook send request as well.

[Add a picture of the UI here]

If you're looking to leverage this as a non-bot, you can write `@silent`
as the _very first_ thing in a message. Make sure your client is
up-to-date btw. Autocomplete a-la `@everyone` is not planned. Eventually we may
put this in an "actual UI", for now this is where it lives. :)

Also sorry to all the users on Discord named silent who may have some
textual conflict now. Forgive me!

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[101aacde93...](https://github.com/pytorch/pytorch/commit/101aacde9317a8a3a75374011e15e567499d26d5)
#### Thursday 2023-02-09 05:07:54 by Taylor Robie

Update base for Update on "[Profiler] Defer recording startup python events (take 2)"


This is my commandeer of https://github.com/pytorch/pytorch/pull/82154 with a couple extra fixes.

The high level idea is that when we start profiling we see python frames which are currently executing, but we don't know what system TID created them. So instead we defer the TID assignment, and then during post processing we peer into the future and use the system TID *of the next* call on that Python TID.

As an aside, it turns out that CPython does some bookkeeping (https://github.com/python/cpython/blob/ee821dcd3961efc47262322848267fe398faa4e4/Include/cpython/pystate.h#L159-L165, thanks dzhulgakov for the pointer), but you'd have to do some extra work at runtime to know how to map their TID to ours so for now I'm going to stick to what I can glean from post processing alone.

As we start observing more threads it becomes more important to be principled about how we start up and shut down. (Since threads may die while the profiler is running.) #82154 had various troubles with segfaults that wound up being related to accessing Python thread pointers which were no longer alive. I've tweaked the startup and shutdown interaction with the CPython interpreter and it should be safer now.

Differential Revision: [D42336292](https://our.internmc.facebook.com/intern/diff/D42336292/)

[ghstack-poisoned]

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[b24d8db0da...](https://github.com/pytorch/pytorch/commit/b24d8db0dab6a3974bb713302f75309e035c009c)
#### Thursday 2023-02-09 05:08:01 by Taylor Robie

[Profiler] Defer recording startup python events (take 2)

Pull Request resolved: https://github.com/pytorch/pytorch/pull/91684

This is my commandeer of https://github.com/pytorch/pytorch/pull/82154 with a couple extra fixes.

The high level idea is that when we start profiling we see python frames which are currently executing, but we don't know what system TID created them. So instead we defer the TID assignment, and then during post processing we peer into the future and use the system TID *of the next* call on that Python TID.

As an aside, it turns out that CPython does some bookkeeping (https://github.com/python/cpython/blob/ee821dcd3961efc47262322848267fe398faa4e4/Include/cpython/pystate.h#L159-L165, thanks @dzhulgakov for the pointer), but you'd have to do some extra work at runtime to know how to map their TID to ours so for now I'm going to stick to what I can glean from post processing alone.

As we start observing more threads it becomes more important to be principled about how we start up and shut down. (Since threads may die while the profiler is running.) #82154 had various troubles with segfaults that wound up being related to accessing Python thread pointers which were no longer alive. I've tweaked the startup and shutdown interaction with the CPython interpreter and it should be safer now.
ghstack-source-id: 179750376

Differential Revision: [D42336292](https://our.internmc.facebook.com/intern/diff/D42336292/)

---
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[4b69f5d536...](https://github.com/Kapu1178/daedalusdock/commit/4b69f5d53635f72e87dd045b4ba00bc7478ce83a)
#### Thursday 2023-02-09 05:51:26 by Kapu1178

Speed up the roundstart significantly (#147)

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

* manifest_inject() stuff

* Fixes role banned players not being banned from roles that they are banned from (Option Two) (#69703)

I feex

* Saves on average 10 seconds from roundstart times (#71730)

## About The Pull Request

When runlevels change mid work, subsystems running behind have their
next_fire updated.
It's offset by a sum of random numbers, so things don't bunch up,
especially KEEPTIME SSs

The trouble is we have so many subsystems that get added at roundstart
that this offset gets LARGE, like 10 seconds on average.

So instead of randomly offsetting, why not "fill" a set of time slots?
Only 1 keeptime subsystem a tick, and 4 others. Then we just fill up
those buckets and get to it (also don't offset things that are already
processing)

I've talked to mso a bit about this. What he reccomended was sampling a
random time withing a 2 second window.
I'm not totally sure why, kinda waiting for him to tell me off, if he
does I'll fix things up.

This pattern takes the max possible delay from 16 (76 * 5 / 20)) seconds
to 0.7 (56 / 4 / 20)
It obviously scales with subsystem count, but I like this scaling a bit
better

I've applied the same pattern to the offsetting we do at the start of
Loop(), for ticker subsystems. I am less confident in this, it does take
last fire times from at worst 3.75 seconds (15 * 5 / 20) to a static
0.75 (15 / 20)
As stated I'm less sure of this, hoping to get mso'd so I can clean
things up

## Why It's Good For The Game

Makes roundstart snappier

## Changelog
:cl:
code: Roundstart "starting" should be much snappier now
/:cl:

Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>

* fix missing macro

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Timberpoes <silent_insomnia_pp@hotmail.co.uk>
Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>

---
## [kwvanderlinde/maptool](https://github.com/kwvanderlinde/maptool)@[75199c5c99...](https://github.com/kwvanderlinde/maptool/commit/75199c5c993ff50835c6cb2eaa2dd09fbe2793d0)
#### Thursday 2023-02-09 06:32:21 by Kenneth VanderLinde

Begin a sloppy implementation; need a way to get different lumens per light range

Try building a special illumination data structure that can represent what we need for lights. In future, consider moving away from a plain list of individual illuminations, and build up a specialized global data structure

Fix lumens overlay so that it does not add to the lighting cache; in the future, these should be unified anyways, and the light renderer should not have to depend on whether or not something was previously cached in just the right way

Add bitset for controlling whether to render lights and lumens overlay

Instead of bitset, rely on AppState in ZoneRenderer

Multiply in extra alpha so light opacity can be managed

Beef up the lumens border

Textured tintable lights

Rework soft lighting to use black-background lights; alpha had some wierd artifacts as near the edge had a sharp darkness

Go back to trying alpha-based; it is better using pegtop soft lighting (as is used in GIMP), but still gets a bit dark

Commit to premultiplied alpha for soft lighting; interpret extraAlpha as a light boost instead of a transparency effect

MULTIPLY blend is not used; recognize that SCREEN blend is really used for building up lights rather than composing layers; make sure we _know_ whether we are using premultiplied or not

Stick to premultiplied images, but support others as well via color converters; performances is much better at ~50ms worst case

Tweak soft light for premultiplied usage; allow map to shine through by alpha compositing the soft light result back onto the map; no more use for boosting in soft lighting

Render lumens overlay on top of lights instead of the other way around; map lumens=50 and lumens=100 to match 1.11.5 dim and bright lights for predefined 5e torches

Settle on overlay for blending light layer onto map

Clip the final light overlay render rather than each individual light; this is a perf win for player view where lots of screen space does not need to be passed through a software blender

Create a new graphics context for the light overlay, which frees us from having to restore state; remove unused view and overlayOpacity parameters from renderLightOverlay

Remove doc for old parameter

Make darkness a separate type from normal lights

Some handy todo notes

Need to include darkness in the lumens map

Some lumens map clean up; working towards a world where we have one data structure to represent the actual lighting in a zone

Reenable darkness rendering; required us to be able to control both the light blending and overlaying behaviour for renderLightOverlay

Make a bunch of progress towards coalesced calculation of lit areas and drawable lights; BIG PROBLEM is performance, as there is no way to turn off these sometimes expensive calculations; Solutions include adding proper caching per light source, unioning of Path2D instead of Area, an allowance for on-demand calculation of the individual components of global illumination, and ultimately a bespoke data structure that can dynamically adjust as lighting changes are made

Rewrite getIllumination coalesence loop to use Path2D for lumens areas

Actually cache the results of getIllumination()

Clear up some names in the loop, and don't unnecessarily copy areas

Remove all the old lighting calculations in ZoneView in favour of the new stuff that obsoletes it

Now make sure we can support personal lights and daylight by actually building a per-view illumination structure

Now get rid of the new methods that are no longer used

Remove unused ZoneView.Illumination

Add a treatise on where to go from here

Rework lumens map into a list of lumens levels, where each level is not guaranteed to be disjoint; note that individual lights for a light source will in practice be disjoint, but once lights start overlapping that statement does not generally hold true

TEMP Implement an Illuminator data structure for speeding up lumens updates; still need to be able to produce drawable lights

Finish the first step of the illuminator. Has parity with stuff from before this change, but still needs personal and daylight support

TODO Notes galore

More TODOs

TEMP Begin accounting for sight magnifiers; the returned GlobalIllumination will now permit overlapping ranges in this case, and will rely on the handling of the lumens map to display them correctly; still need to make sure DrawableLights work (they won't because now they overlay, and it's not clear which one should win) and need to make ZoneRenderer actually look up the correct sights; will also need to merge results together when multiple tokens are in the view

Use the first token's sight type; sufficient for now, until we start merging results

Instead of caching on Sight, and instead of caching on View, cache on a special SightIlluminationKey that can have properties independent of any actual sight. E.g., by taking the maximum magnification

Calculate illumination keys in ZoneRenderer; only getExposedArea(PlayerView) and getVisibleArea(PlayerView) even rely on views anymore; thinking this means the illumination stuff can go into its own illumination model or something, but that is extra work that does not need to happen

Remove obsolete notes about SightTypes since we now use IlluminationKeys

Simplify lumens shade calculation understanding we don't yet have generality

Add todo note about empty lumens areas, esp for darkness

Add a second shade level easier magnification edge case testing

Fix which area we use for light in the presence of magnification; added todo note about how we need to fix drawable lights

For light hole punching, sort the ranges' areas by lumens and make sure the stronger ranges beats out the weaker ranges without overlap

Cleanup; removed already-actioned TODOs and unneeded methods

Keep track of which tokens have contributed to the lighting; use that when flushing a token to determine if vision needs to be recalculated; flush the illuminationCache in that case

Factor out large main loop of getAndCacheIllumination so it works on a single light token at a time

Stop caching illumination results, and instead keep illuminators around; allow remove LitAreas from illuminators

Fixup light invalidation to work even when adding a light source to a token and not just removing / modifying one

Track contributing tokens on a per-illuminator basis; otherwise we (of course) found that one illuminator would prevent additions to others

Add timer specifically for filling the lights during rendering

Clear the illuminators on ZoneView.flush(); future improvement is definitely to be as precise as possible in what information to throw away

Some todo notes on flushing

Add notes about caching in ZoneView and how it makes no sense

Clarify the isEmpty check and how we should do it and whether we even need it

Only grab lights and darknesses when actually needed

When rendering the lumens overlay, clip the original g as well as newG

More notes

Split Illuminator.getIllumination() into getVisibleArea(), getLumensLevels(), getLightAreas() and getDarknessAreas()

Rework ZoneView methods to use the new decomposed Illuminator methods; saves calculating things like drawable lights even when those don't need to be rendered; also is much easier to follow and eliminates GlobalIllumination

Slightly better naming

Handle case of token having no vision according to FogUtil

Add notes about per-view caching and the need for flushing

Make the remainder of ZoneView's caches per-view

This boils down to changing `ZoneView.getVisibleArea(Token)` to `ZoneView.getVisibleArea(Token, PlayerView)`, which
required updating several callers, mainly macro functions and `FogUtil`. This method also had a thin wrapper
`ZoneRenderer.getVisibleArea(Token)` which was hardly used and has been removed in favour of a direct call to
`ZoneView.getVisibleArea(Token, PlayerView)`.

Now that `ZoneView` can cache everything for multiple `PlayerView`s at once, `ZoneView.flush()` only needs to be called
in the situations now mentioned in its documentation. It does *not* need to be called when the current `PlayerView`
changes (thanks to the above changes), and is also no longer called when the map viewport changes. This greatly reduces
the amount of recalculation, and the sight-heavy sunless citadel map can now fluently switch views.

Fix flush(Token) to remove from the nested map instead of a type-incorrect removal from the top-level map (thanks for nothing Java)

Link to fields in doc comments instead of via plain names; remove references to old fields no longer with us RIP

Get rid of a bunch of obsolete TODOs

Do a real isEmpty check rather than checking for a zero center of the bounding box

Change FogUtil.calculateVisibility to not transformed its areas; otherwise we sometimes have to copy areas just to translate it afterwards

Add another debugging hot key for showing single lumens levels

Clip both the light buffer and the underlying buffer when rendering lights, for performance

Do lumens map hole punching in ZoneRenderer

START Begin moving Illuminator away from direct knowledge of lights and light sources, instead only caring about lumens and areas

Render lumens overlay overtop light and darkness; only retrieve drawable lights when lighting is enabled (performance); change bright light to not be entirely clear, but still draw a nearly transparent white

No longer require disjoint lumens levels; begin move toward a single Illumination result type

Calculate visible area from returned Illuminations

Expand on the nature of darkness in our new lighting system

Calculate drawable light areas based on the illumination

Remove genericness of Illuminator as we no longer rely on the user data to associate lit areas with the originating lights

Remove reliance on IlluminationKey in ZoneRenderer, recognizing the results will generally depend on the entire PlayerView

Factor out per-view token selection logic

Encapsulate tokenVisibleAreaCachePerView so we can use it more freely

Include personal lights and daylight in the results used for drawable lights

Do not include non-renderable daylight in contributed personal lights

Include personal light and daylight in the lumens map

Put both light and darkness into each lumens level; TODO Make sure we don't unnecessarily work with empty areas to our detriment

Only use the sight's multiplier for personal lights; don't use the illumination key's multiplier

Fix the sign of personal darkness

Cache per-view illuminations

Clean up LitAreaUserData to reflect its new nature

From ZoneView remove completed todos or todos that have not aged well

Disable antialiasing in light overlay; it's less important with textured lights, and is the cause of some gapping or even slight overlapping that then makes really bright rings

Cache personal lights per-IlluminationKey instead of required stashing per-PlayerView

Calculate and cache token visible areas per-IlluminationKey instead of per-PlayerView

Do not cache token's personal lights or visible areas according to IlluminationKey, but solely according to Token since they don't actually depend on it

Regroup fields for clarity

Non-lights changes to get rid of DARKNESS

ZR changes for lumens level

Fix multi-range light hole punching when mixnig darkness and light

Update ZR for BC changes

Fix to not magnify darkness

Improve performance of calculateVisibleArea(PlayerView) by using the `Illumination` we already have

ZR changes now that light now longer has a getPaint()

ZR now uses tinted paint provided by LightSource

ZR changes for no more Operation enum

ZR changes for non-int getPaint

ZR spotlessApply

ZV spotlessApply

ZV changes for light changes

Render unlit areas as dark in the lumens overlay; opt for a simple linear interpolation from 0 to 100 for the lumens overlay shade, with >= 100 being almost transparent

Tweak shading

Disable redundant clipping for more conssitent frames

Remove use of old getLumensLevelsToShow()

Change daylight representation to zero lumens; do not include render daylight in the lumens overlay

---
## [Surrealaser/ROSIGMA](https://github.com/Surrealaser/ROSIGMA)@[d28fef844a...](https://github.com/Surrealaser/ROSIGMA/commit/d28fef844af8c4ed02960f3434982f4b34bdb0ca)
#### Thursday 2023-02-09 06:36:10 by Surrealaser

Khorne Update

1. Added the stat gain on melee hit/kill 'Rampage' mechanics to more Khorne units; Juggernauts, Khorne Warptalons.

2. Standardized traits among Khorne units like Fear and Pain Immunity.

3. Added the Intimidation ability/weapon. This is primarily used for Khorne units that lack ranged weapons for reaction fire like Bloodletters, Juggernauts and Warptalons; drains TUs and Morale in a small AoE via paralytic terror.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f5e523360a...](https://github.com/treckstar/yolo-octo-hipster/commit/f5e523360a0db4df7c2757e21ffe467f1e3a4710)
#### Thursday 2023-02-09 07:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [projects-nexus/nexus_kernel_xiaomi_lavender](https://github.com/projects-nexus/nexus_kernel_xiaomi_lavender)@[2d2adf8dbf...](https://github.com/projects-nexus/nexus_kernel_xiaomi_lavender/commit/2d2adf8dbfdd8a9646973ab8636a9f28bcbc0485)
#### Thursday 2023-02-09 07:48:11 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: ImPrashantt <prashant33968@gmail.com>

---
## [mihaigociu/ZeProject](https://github.com/mihaigociu/ZeProject)@[45227d313f...](https://github.com/mihaigociu/ZeProject/commit/45227d313f72e697469cdfb924f22e801163b19d)
#### Thursday 2023-02-09 08:02:38 by Mihai Gociu

Update models.py

Please read about django relationships at https://docs.djangoproject.com/en/4.1/topics/db/examples/

I also have a suggestion that would make the project a bit more interesting. Check the api at https://api.chucknorris.io/#!
Let's add a CNJoke model where we store the user's preferred jokes. 
Here's my suggestion:
- create a CNJokes view; when the user enters the page, you retrieve a random joke from https://api.chucknorris.io/jokes/random and present it to the user; the user has the possibility to "like" the joke (by pressing a Like button on the page or something like that). This should submit a form and create a CNJoke instance for the user.
- create a LikedJokes view where the user can see the jokes they liked so far.
- to fetch the jokes from the api you can use the requests python library at https://pypi.org/project/requests/

---
## [rdi-berkeley/rdi-berkeley.github.io](https://github.com/rdi-berkeley/rdi-berkeley.github.io)@[e18e3e5137...](https://github.com/rdi-berkeley/rdi-berkeley.github.io/commit/e18e3e5137fcb35b62287c3e03493d9a228d0264)
#### Thursday 2023-02-09 08:57:41 by rohitkanagal

Update events.yml

- link: /events/10-25-22
  img: /assets/images/events/10_25_Web3_MOOC.jpeg
  row-title: "Berkeley RDI Frontier Forum"
  date: "2022-10-25"
  formatted-date: "October 25"
  start: "4:00 pm"
  end: "5:00 pm"
  title: "10-25-22 Avichal Garg - Entrepreneurship in Web3: Product"
  img: /assets/images/events/10_25_Web3_MOOC.jpeg
  location: In person @ Soda Hall
  # zoom: https://berkeley.zoom.us/webinar/register/WN_Hi44XRhiRhy11U-exg_VOw
  description: |
    UC Berkeley's new Center for Responsible, Decentralized Intelligence (RDI) 
    is excited to announce this week's Frontier Forum: Entrepreneurship in Web3: Product, 
    with Avichal Garg.
  speakers:
    - name: Avichal Garg
      description: |
      Avichal Garg, Co-Founder/Partner at Electric Capital. Avichal is a successful entrepreneur with executive experience at Google and Facebook, which acquired his previous company. As an angel investor, Avichal has invested in 15 unicorns and 5 decacorns including Airtable, Boom Supersonic, Color Genomics, Cruise, Deel, Figma, Newfront Insurance, Notion, Nova Credit, Pulley, and others. He co-founded Electric Capital in 2018 and has grown it to one of the largest crypto venture firms globally. Electric is an investor in leading web3 protocols and companies such as Bitwise, Bitnomial, dYdX, Frax, Kraken, Magic Eden, NEAR, and Tokemak.

---
## [dr3ams/Roguelike-Adventures-and-Dungeons-2](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2)@[a7d6793949...](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2/commit/a7d67939495495ebea60ca96160e7050d58c1ff6)
#### Thursday 2023-02-09 09:09:56 by dr3ams

1.0 with summarized changes

- updated titles list
- fixed xp_bonus_dimension
- disabled buddycards card display
- life mending added to ender mending
- life mending added to grimoire incompats
- re enabled ender's markman
- Spartan Reach disabled and replaced with Dungeons Gear Reach Attribute (the tooltip looks the same so you should notice no difference in-game)
- Emerald Upgrade Kit is now just as expensive as Emerald Bow, requiring Emeraldite Shards
- Nerfed spirit orb drop rate from spawners
- Soul Enchanter requires 200 Magic to use
- Quality of Life changes for new players to avoid confusion:
	- Removed the +0% sprinting speed bonus text when leveling up
	- The "Too Hot to wear" message changed to mention pmmo skills
- fixed all the spartan weaponry throwables (throwing knife, tomahawk, javelin, boomerang) now working properly if you have the requirements.
- Villager Trade Changes
	- Librarian:
		- Removed First Librarian Enchanted Book Trade
		- Replaced Vanilla Lantern Trade with Brass Lantern
		- Added Disenchantment Book to last librarian trade

	- Nitwits can be traded with; they sell you worthless junk which gets only *slightly* better each tier. They are a more reliable source of getting tin due to their tin can trade.
- 9 Amethyst Nuggets = 1 Gem
- overgrown caves in twilight forest
- Moved Wormhole Potion from Equipment to Potions
- Bulldozer Nerf
- SoLPotato unreachable thresholds fix & rework (Thanks to @Chkoupinator for this!)
- nerfed nether coin crate
- Removed Afterlight Ore from Mining Dim
- added lion to champions blacklist
- Add plague clouds to the champions blacklist
- Grace of the Creator disabled
- added tropicraft white chair recipe
- temp disabling greek fantasy potions
- blacklisted mossy ring and belt trinkets
- added Forgery mod. If you're familiar with this mod and have suggestions - please provide feedback!

---
## [ArtemisStation/artemis-tg](https://github.com/ArtemisStation/artemis-tg)@[97f567fdc7...](https://github.com/ArtemisStation/artemis-tg/commit/97f567fdc745230b1594c305680dce683512d032)
#### Thursday 2023-02-09 10:22:19 by MMMiracles

Tramstation: Growing Pains (#72331)

## About The Pull Request


![image](https://user-images.githubusercontent.com/9276171/209841644-3e8be93c-7903-4eb4-85bf-cc582248a9fa.png)

## Why It's Good For The Game

Lots of QoL and structural changes in attempt to make the cool map even
cooler.

## Changelog
:cl: MMMiracles
add: Tramstation has received a substantial overhaul! Please consult
your local tour guide and station maps for changes.
/:cl:

**Changes (as of so far)**
- The Tramstation tunnels have been extended 6 tiles each way, making
that trek across the central rail a little more dangerous.
- No more mid-way safety net on the transit rails. You're either making
it or you're jumping to the bottom floor to avoid the tram.
- The central rail apparently had a negative slowdown, meaning you
actually WERE faster to just run the gauntlet because it literally made
you faster. This has been reverted because I want you to get hit by a
train.
- The side routes are now a bit more dangerous since you can get pushed
off into the lower floor
- Fauna overhaul! Several locations including the transit tunnels have
gotten some greenery to help liven up transit between sectors. Please do
not rip up the AstroTurf it is very expensive in space.
- Handicap-accessible departments! Every major wing and departments with
multiple floors has been given a 2x3 elevator segment for those among
the crew who have been hit by the tram a few too many times. Handicap
inaccessible staircases may or may not come after this (i hate the
handicapped)
- Expanded Security wing! You know that lame hallway between
interrogation and the courtroom access? Now its a whole holding wing fit
with essentials to keep your inmates content while waiting for their due
process (never ever).
- Reworked Bridge! Front row seats to the western tram dock as well as a
furnished meeting room with various corporate memorabilia!
- The HoP's office has been moved to function more as an arrival gate
for late joining crew! Scenic queue lines and an option to block off the
lower dorm access if you really want to enforce the 'Papers, Please'
roleplay you've always wanted out of your HoP experience.
- Combined the teleporter/gateway/eva access into one special external
operations room. All you off-station needs in one convenient place!
- More multi-z integration! Several segments (mainly maintenance level
transfers) have been given overhangs and better methods to move between
levels. This is still being expanded upon as of current PR posting.
- The power/pipe access shafts have been changed to be more
public-facing and now also act as another inbetween for
maintenance-dwelling crew to shift between floors.
- Multi-z solars! Both solar wings have been extensively overhauled to
include multi-z structuring and easily doubled the amount of roundstart
panels on the map.
- Escape pod bay! [Casually borrowing from a certain ship
map](https://tgstation13.org/phpBB/viewtopic.php?t=32834), there is now
a centralized location for all station escape pods on the floor below
Arrivals. Honestly makes more sense thematically instead of having a
bunch of scattered bays.
- MULEBOT integration! Each major department now has delivery drop-off
points along with Cargo getting a minor restructuring to fit 4 MULEBOTs.
Seedy side-tunnels and drop points have been added for departments that
aren't normally accessible from upper maintenance so they can still
properly deliver cargo if sent this way. I can't guarantee this won't
end in MULEBOTs getting ran over by a tram because they're fickle
beasts.
- Complete rework of the disposals/piping/wirenet! I literally ripped
everything up and rebuilt it with (hopefully) better stability in mind.
Disposals is now also set up in that it'll try to avoid going through
departments unnecessarily if your package isn't marked for it.
- Cargo's mail room and trash room has been overhauled to be more easily
accessed for cargo techs and for routing mail.
- The chef has access to the morgue's back door via the front
maintenance hatch while Robotics can now access the same back door via
their maintenance shaft.
- The chem lab's starting area has been expanded so chemists don't have
to worry as much about digging if they don't have large projects.

![2023 02 02-18 15
45](https://user-images.githubusercontent.com/9276171/216472805-77074a12-d653-41c4-b730-f26f93c27d3b.png)
![2023 02 02-18 15
38](https://user-images.githubusercontent.com/9276171/216472852-555e6ca9-e967-4915-9555-e29cfc99393d.png)

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[b7383425d9...](https://github.com/odoo-dev/odoo/commit/b7383425d99b76afc0ba0df7c5827c331262a086)
#### Thursday 2023-02-09 10:41:41 by Arnold Moyaux

[FIX] stock,purchase,mrp: accumulative security days

Usecase to reproduce:
- Set the warehouse as 3 steps receipt
- Put a security delay of 3 days for purchase
- Set a product with a vendor and 1 days as LT
- Replenish with the orderpoint

You expect to have a schedule date for tomorrow that contains all the
product needed in the incoming 4 days.

Currenly the internal transfer from QC -> Stock is for tomorrow (ok).
The transfer from Inpur -> QC is plan for 2 days in the past. (not ok)
The PO date is plan for 5 days in the past. (not ok)

It happens because the system check at each `stock.rule` application if
purchase is part of the route. If it's then it applies the security lead
time. It's a mistake because we should apply it only the first time.

To fix it we directly set it when the orderpoint run and not during
`stock.move` creation.
However for MTO it's not that easy. We don't want to deliver too
early the customer. So we keep applying the delay during the
`stock.move` creation but only when it goes under the warehouse stock
location.

---
## [qrohlf/next.js](https://github.com/qrohlf/next.js)@[268dd6e80b...](https://github.com/qrohlf/next.js/commit/268dd6e80bb4e17096c0e75da94cf4de0b809697)
#### Thursday 2023-02-09 10:49:17 by José Fernando Höwer Barbosa

Simplify with-google-analytics example (#43894)

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->
## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm build && pnpm lint`
- [x] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

First of all thanks for this amazing project and all the help you
provide with these examples.

It seems there is code duplication in this example. After some tests
locally seem to _document.js is not necessary for `gtag` to work
properly.


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_app.js#L30-L34


https://github.com/vercel/next.js/blob/9d97a1e34a8a6e09eb127292c730d1a8df63ebb6/examples/with-google-analytics/pages/_document.js#L13-L17

I am aware of https://github.com/vercel/next.js/pull/40645 and I would
like to ask @dave-hay, @SukkaW and @ijjk to consider this is still
necessary. If so why then not move all content of the scripts from _app
to _document?

In any case, I am open to adding here some comments explaining what is
the reason for this code duplication if necessary.

<hr/>

Changes that come from  https://github.com/vercel/next.js/pull/43897

1. The `event` hashChangeComplete should be removed since `/home` and
`/home/#section` is not new pageview, but just reference to the same
page.

If we go from /home to /home/#section (with a button click or a link for
example) this shouldn't trigger a new page visit on `gtag`.

For this reason, I think we should revert the changes from
https://github.com/vercel/next.js/pull/36079. If there is a better
argument of why this should stay I am also open to creating comments to
clarify this on the example since I don't think should be the default
behavior and not useful in most cases.

2. The `id="gtag-init"` was added with no context to the example from
https://github.com/vercel/next.js/pull/29530

If there is a reason for this id in the script to existing I am open to
adding a comment that clarifies this since in my experience is not
necessary at all.


Edit: Batching with https://github.com/vercel/next.js/pull/43897 as
recommended by
https://github.com/vercel/next.js/pull/43897#issuecomment-1344635000

---------

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [petre-symfony/PHPUnit-Testing-With-A-Bite-SymfonyCasts-2022](https://github.com/petre-symfony/PHPUnit-Testing-With-A-Bite-SymfonyCasts-2022)@[7f42aa71e3...](https://github.com/petre-symfony/PHPUnit-Testing-With-A-Bite-SymfonyCasts-2022/commit/7f42aa71e365e84adbcab28b4bcbf60ae4382318)
#### Thursday 2023-02-09 11:43:15 by petrero

15 Mocking Symfony's Http Client
 Having the ability to mock objects in tests is super awesome, and kind of weird and complex all at the same time. If we have simple objects, like Dinosaur, we should avoid the extra lines of code and just instantiate a real Dinosaur for the test. After all, it's pretty easy to control the behavior of Dinosaur just by calling its real methods. No need for the mock weirdness.

 But, for more complex objects, like HttpClient, using the real client... can be a headache. The general rule of thumb is to use mocks for complex objects like, services... but for simple objects, like models or entities, just use the real thing.

 Looking back at Symfony's HTTP Client, we were able to mock both the client and the response to control its behavior. But, because needing to do this sort of thing is so common, Symfony's HTTP Client comes with some special classes that can do the mocking for us. It comes with two real classes specifically made for testing: MockHttpClient & MockResponse. Using PHPUnit's mock system is fine, but these exist to make our life even easier.

 Check it out: instead of creating a mock for $mockResponse, instantiate a MockResponse() passing in json_encode() with an array to mimic GitHub's API response. Grab Maverick's issue below and paste that into the array. Since MockResponse is already configured, remove the $mockResponse bits below.

 For the client, remove $mockHttpClient and below, instantiate a new MockHttpClient() passing in $mockResponse instead. Since we're not doing anything with $mockLogger, cut createMock(), remove the variable, and paste that as an argument to GithubService().

 Wow, this is looking better already! But, let's see what happens when we run the tests:

  ./vendor/bin/phpunit
 And... Woah! All of the tests are passing!

 But, the assertion count did go down to "16" because MockHttpClient and MockResponse do not actually perform any assertions, like how many times a method is called.

 So... what's the actual benefit to using these mock classes? Why not just create our own via PHPUnit? Ha... Check out this diff of GithubService. We removed 11 lines of code by using the "built-in" mocks in just one test. Imagine how many lines of code we could remove by using them in all of our tests. Hm... I think that's exactly what we'll do next.

---
## [distributed-system-analysis/pbench](https://github.com/distributed-system-analysis/pbench)@[36cbbd1c8f...](https://github.com/distributed-system-analysis/pbench/commit/36cbbd1c8f98ddd4c46ccd7405fbca6263245753)
#### Thursday 2023-02-09 12:09:09 by David Butenhof

Fix operation synchronization (#3232)

* Fix operation synchronization

PBENCH-993

This is fairly large, but yet much smaller than it started out. This solves
two problems in Pbench Server task scheduling:

1. The default SQLAlchemy transaction model is to start a transaction on any
   SELECT and end it on any UPDATE or INSERT; this means there's no potential
   for atomic update. This impacts the management of all internal context, but
   serious problems have been observed with the "operation" and "state" of the
   datasets.
2. I began the dataset with the concept of a "state", as the dataset
   progresses through upload, backup, unpack, index, and delete. I quickly
   discovered that this wasn't ideal, but had trouble backing off completely
   from the concept. When I added the DB-based "operation" to replace the old
   filesystem links, the relationship between "operation" and "state" became
   even messier.

The primary change here is to divorce the `Sync` class entirely from general
metadata. (I originally set out to make `Metadata` management atomic, and the
fan-out was enormous: I'll tackle that again later, but while important in the
long run, getting `Sync` working is immediately critical.)

There is a new `Operation` DB object associated with a `Dataset`, and this is
entirely managed within the `Sync` class. For visibility, `Dataset.as_json`
will collect associated rows just as it does for `dataset.metalog`, but this
doesn't require any special transactional management. (It's a snapshot.)

I've completely *removed* the `Dataset.state` column (and its associated "last
transition" timestamp). "State" is tracked and observed by the various `Operation`
rows created and managed by `Sync`. This corresponds to the previous
dataset.status` sub-object managed by the old `Sync`: each named operation
(`OperationName` enum) that's been associated to a dataset will have a row with
`state` and `message` columns. The `state` can be advanced through `READY`,
`WORKING`, `OK`, and `FAILED`, and a message can be associated with each
row (on error via `Sync.error` or as part of transition via `Sync.update`).

While I was modifying the Dataset schema, I also removed the `created` column;
it's really redundant with `dataset.metalog.pbench.date`, and we'll need to
understand that for "non-Pbench-standard" tarballs we might not be able to get
this anyway. This wasn't quite as "easy" as I'd thought, because it meant that
I had to refactor date-range operations to work on `uploaded` (perhaps they
should have been that way originally).

`Sync.__init__`: Construct a sync object for a particular named operation.
`Sync.next`: Return a list of datasets which have `Operation` rows for the
   sync component that are in `READY` state.
`Sync.update`: Change the state of the sync component's `Operation`,
   optionally add a message to that `Operation`, and set a list of named
   operations for that dataset to `READY`.
`Sync.error`: Change the state of the sync component's `Operation` to `FAILED`
   and record an explanatory message for the failure.

To avoid rippling massive SQLAlchemy transaction model changes across all our
code, I've added a second session factory in `Database` with the most strict
integrity level, `SERIALIZABLE`. (In fact, I *think* that `"REPEATABLE READ"`
would be enough, and slightly more efficient, but sqlite3 doesn't support that
and I don't think I want to trust the weaker model it does support.)

*Only* the `Sync` class in `sync.py` currently uses that alternate session
factory. To avoid conflicts and confusions with autoflush and autocommit and
other SQLAlchemy "help", I'm creating new sessions on-the-fly for each call
and retiring them after commit/rollback. Note that the idiom
`with Database.maker.begin() as session:` constructs a new session with fresh
state, allows a sequence of session operations, and then implicitly tears down
the session after it commits on success or rolls back on an exception.

To avoid multiple `SELECT` statements within our transaction, `Sync.update`
fetches all relevant rows in a single `SELECT`, and then organizes them for
selective updates. This ensures we have no `SELECT` following the update of any
proxy object, which confuses SQLAlchemy in normal configuration.

`Sync.update` and `Sync.error` will loop up to 10 times on commit failure to
re-try with fresh data. Note that I've observed the retry logic in dozens of
functional test runs; and while I wonder vaguely whether I should be concerned
with the constant 10, I rarely see more than one or two retries since I added
a small delay to minimize thrashing.

NOTE: Alembic schema changes for Operation table

After working with Pete get get alembic to successfully generate a revision
file for my changes, we realized what a pain it would be to migrate (and
test) an actual live database. We need to have a functional test framework to
stand up an "old" functional DB, upgrade it to the latest revision, and then
validate the correctness.

---
## [ninstar/Rich-Presence-U-DB](https://github.com/ninstar/Rich-Presence-U-DB)@[b676b6cf58...](https://github.com/ninstar/Rich-Presence-U-DB/commit/b676b6cf583efcb4045ce7c6b21566b93f726a19)
#### Thursday 2023-02-09 12:27:01 by ninstar

+71 New Nintendo Switch titles

Anuchard
Behind the Frame: The Finest Scenery
Bow to Blood: Last Captain Standing
Capcom Fighting Collection
Colors Live
Cozy Grove
Crash Bandicoot 4: It’s About Time
Dadish
Dadish 2
Dadish 3
Daily Dadish
Devil May Cry
Devil May Cry 2
Devil May Cry 3 Special Edition
DOOM 64
DOOM Eternal
DYSMANTLE
Fallout Shelter
FATAL FRAME: Maiden of Black Water
FIFA 18
FIFA 20 Nintendo Switch Legacy Edition
FIFA 21 Nintendo Switch Legacy Edition
FIFA 23 Nintendo Switch Legacy Edition
Figment
Gang Beasts
Horizon Chase Turbo
Huntdown
Just Dance 2017
Just Dance 2018
Just Dance 2019
Just Dance 2021
LEGO Brawls
LEGO Bricktales
LEGO Builder's Journey
LEGO Marvel Super Heroes
LEGRAND LEGACY: Tale of the Fatebounds
Marooners
MEGA MAN BATTLE & FIGHTERS
Mega Man Battle Network Legacy Collection Vol. 1
Mega Man Battle Network Legacy Collection Vol. 2
Metroid Prime Remastered
Moonlighter
Moto Rush GT
NAMCO MUSEUM
New Tales from the Borderlands
OKAMI HD
ONE PIECE Pirate Warriors 3 Deluxe Edition
ONE PIECE: PIRATE WARRIORS 4
ONE PIECE: Unlimited World Red Deluxe Edition
OneShot: World Machine Edition
PAC-MAN WORLD Re-PAC
Panzer Dragoon: Remake
Shantae
Shantae and the Pirate's Curse
Shantae and the Seven Sirens
Shantae: Half-Genie Hero
Shantae: Risky's Revenge - Director's Cut
Sid Meier’s Civilization VI
SmileBASIC 4
Street Fighter 30th Anniversary Collection
Summer in Mara
Super Fowlst
Super Fowlst 2
Super Monkey Ball Banana Mania
Super Monkey Ball: Banana Blitz HD
Tales from the Borderlands
The Outer Worlds
Tools Up!
Ultra Street Fighter® II: The Final Challengers
Will You Snail?
Yu-Gi-Oh! Master Duel

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[8435ac84ca...](https://github.com/treckstar/yolo-octo-hipster/commit/8435ac84caf8f4627a9d5864b40ff3072b32d148)
#### Thursday 2023-02-09 13:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [gbmaster/linux](https://github.com/gbmaster/linux)@[0e5181221a...](https://github.com/gbmaster/linux/commit/0e5181221acee67f67aa3626479db17ee3361029)
#### Thursday 2023-02-09 13:24:05 by Linus Torvalds

Linux-0.12 (January 15, 1992)

This was created from a re-packaged 0.12 tree

Major milestone! Over the christmas break, I implemented paging to disk,
meaning that you could actually use gcc on a 2MB system.  Some poor sod
(Robert Blum) wanted to use Linux on such a system, and couldn't get the
kernel to compile with anything less "bloated" than gcc.

[ Irony alert: this was back when gcc worked fine on a system with just
  4MB.  Gone are those days. _Loong_ gone. ]

The task size was still limited to 63 tasks of at most 64MB each, but
other than that we were actually getting usable.

Together with other improvements and fixes, 0.12 was actually a very
nice kernel.  It was by now clearly more usable than Minix, which caused
us to think that a 1.0 release was imminent.  The next kernel version
was to be named 0.95, which turned out to be less than a stellar idea.

This was also the point where we changed the copyright license.  See the
attached original release notes.

Other changes:

 - Ted Ts'o continued on his rampage, and implemented BSD process
   control (ie ^Z) etc.  This also introduced the process tree code,
   with pointers between parents and children, rather than iterating
   over the whole list of processes.

 - Ted also did SVR4-style "saved uid/gid" handling.

 - use the C preprocessor for assembly files, cleaning up a lot of
   duplicate definitions etc.

 - better boot loader diagnostics

 - boot sequence now can change the size of the text display.  Who the
   hell is d88-man?

 - fix nasty race condition between "truncate" and file IO.

 - add support for shared libraries with the "uselib()" system call.
   This (together with the fact that we could share clean executable
   pages) cut down on memory usage a lot.

 - supplemental group support.  Hey, what can I say? Unix users expected
   them.

 - symbolic link handling.  This was the first real extension to the
   standard Minix disk layout, and was made possible by the fact that I
   had written my own "mkfs" and "fsck".  Before that, we were still on
   crutches, in that a Linux system depended on a Minix installation for
   these fundamental system tools.

 - mkdir()/rmdir() isn't just for root, you know..  (Yes, seriously.
   Old-style UNIX used to limit them to root-only, since they were just
   special sequences of mknod's)

 - Virtual terminals by Peter MacDonald (who was to do the SLS
   distribution).

   Before having X, this was a _big_ deal.  The fact that Linux had
   virtual terminals with a good vt100 emulation actually made Linux
   stand out even among some of the big commercial unixes.  The Linux
   console was just _so_ much more pleasant to use that it isn't even
   funny.

 - first implementation of "select()", virtual terminals, and pty's.

   These too were originally done by Peter MacDonald, based on some
   patches that had been floating around for Minix for a long time (but
   were never accepted into Minix).

   They didn't get accepted into Linux either, but the patches _did_ end
   up inspiring me to re-do the select/pty parts in a way that was more
   palatable to me.

 - restartable system calls

   This was needed for Ted's code to do ^Z

 - Math emulation! The code was a total crock, and didn't bother with
   such unnecessary niceties as getting rounding right (or, to be
   honest, even getting more than about 60 bits right), but let's face
   it: it was enough to get work done.

   My math emulation was eventually to be entirely replaced by a much
   more complete, and much more precise implementation by Bill
   Metzenthen.  But my original stupid implementation actually ended
   living on at least for a while in BSD - I ended up making it
   available to the BSD people who couldn't use Bill's much better
   implementation due to licensing reasons.  I don't know whatever
   eventually happened to it.

 - support alignment check on i486+. Nobody seems to have ever used it,
   though.

Original release notes:

         RELEASE NOTES FOR LINUX v0.12

This is file mostly contains info on changed features of Linux, and
using old versions as a help-reference might be a good idea.

         COPYRIGHT

The Linux copyright will change: I've had a couple of requests to make
it compatible with the GNU copyleft, removing the "you may not
distribute it for money" condition.  I agree.  I propose that the
copyright be changed so that it confirms to GNU - pending approval of
the persons who have helped write code.  I assume this is going to be no
problem for anybody: If you have grievances ("I wrote that code assuming
the copyright would stay the same") mail me.  Otherwise The GNU copyleft
takes effect as of the first of February.  If you do not know the gist
of the GNU copyright - read it.

         INSTALLATION

This is a SHORT install-note. The installation is very similar to 0.11,
so read that (INSTALL-0.11) too. There are a couple of programs you will
need to install linux: something that writes disk images (rawrite.exe or
NU or...) and something that can create harddisk partitions (fdisk under
xenix or older versions of dos, edpart.exe or something like that).

NOTE! Repartitioning your harddisk will destroy all data on it (well,
not exactly, but if you know enough to get back the data you probably
didn't need this warning).  So be careful.

READ THIS THROUGH, THEN READ INSTALL-0.11, AND IF YOU ARE SURE YOU KNOW
WHAT YOU ARE DOING, CONTINUE.  OTHERWISE, PANIC.  OR WRITE ME FOR
EXPLANATIONS.  OR DO ANYTHING BUT INSTALL LINUX - IT'S VERY SIMPLE, BUT
IF YOU DON'T KNOW WHAT YOU ARE DOING YOU'LL PROBABLY BE SORRY.  I'D
RATHER ANSWER A FEW UNNECESSARY MAILS THAN GET MAIL SAYING "YOU KILLED
MY HARDDISK, BASTARD.  I'M GOING TO FIND YOU, AND YOU'LL BE SORRY WHEN I
DO".

1) back up everything you have on your harddisk - linux-0.12 is still in
   beta and might do weird things.  The only thing I guarantee is that
   it has worked fine on /my/ machine - for all I know it might eat your
   harddisk and spit it out in small pieces on any other hardware.

2) Test out the linux boot-disk with the root file system.  If it
   doesn't work, check the hardware requirements, and mail me if you
   still think it should work.  I might not be able to help you, but
   your bug-report would still be appreciated.

   Test that linux can read your harddisk at least partly: run the fdisk
   program on the root-disk, and see if it barfs.  If it tells you about
   any partitions at all, linux can successfully read at least part of
   your harddisk.

3) Make sure that you have a free /primary/ partition.  There can be 4
   primary partitions per drive: newer DOS fdisks seem to be able to
   create only 2 (one primary and one extended).  In that case use some
   other partitioning software: edpart.exe etc.  Linux fdisk currently
   only tells you the partition info - it doesn't write to the disk.

   Remember to check how big your partition was, as that can be used to
   tell which device Linux thinks it is.

4) Boot up linux again, fdisk to make sure you now have the new
   partition, and use mkfs to make a filesystem on one of the partitions
   fdisk reports.  Write "mkfs -c /dev/hdX nnn" where X is the device
   number reported by linux fdisk, and nnn is the size - also reported
   by fdisk.  nnn is the size in /blocks/, ie kilobytes.  You should be
   able to use the size info to determine which partition is represented
   by which device name.

5) Mount the new disk partition: "mount /dev/hdX /user".  Copy over the
   root filesystem to the harddisk, eg like this:

        # for i in bin dev etc usr tmp
        # do
        # cp +recursive /$i /user
        # done

   You caanot use just "cp +recursive / /user", as that will result in a
   loop.

6) Sync the filesystem after you have played around enough, and reboot.

        # sync
        <wait for it to sync>
        ctrl-alt-del

   The folklore says you should do this three times before rebooting:
   once should be enough, but I admit I do it three times anyway :) THIS
   IS IMPORTANT! NEVER EVER FORGET TO SYNC BEFORE KILLING THE MACHINE.

7) Change the bootdisk to understand which partition it should use as a
   root filesystem.  See INSTALL-0.11: it's still the word at offset
   508 into the image. You should be up and running.

That's it. Go back and read the INSTALL-0.11

         New features of 0.12, in order of appearance
         (ie in the order you see them)

        Linux now prints cute dots when loading

WoW. Run, don't walk, to see this :). Seriously, it should hopefully now
load even on machines that never got off the ground before, but
otherwise the loading hasn't changed. Implemented by drew.

        Super-VGA detection for extended alphamun modes

I cannot guarantee it, I didn't write it, but it works great on a ET400
SVGA card.  I'm addicted to the new look with 100x40 character editing,
instead of a cramped 80x25.  This only works on VGA-cards that support
higher text-resolutions, and which are correctly identified. Implemented
by d88-man.

        Job Control.

Ok, everybody used to typing ^Z after they started a long command, and
forgot to put it in the background - now it works on linux too.  Bash
knows the usualy job-control commands: bg, fg, jobs & kill.  I hope
there will be no nasty surprises.  Job control was implemented by
tytso@athena.mit.edu.

        Virtual consoles on EGA/VGA screens.

You can select one of several consoles by pressing the left alt-key and
a function key at the same time. Linux should report the number of
virtual consoles available upon bootup. /dev/tty0 is now "the current"
screen, /dev/tty1 is the main console, and /dev/tty2-8 can exist
depending on your text-mode or card.

NOTE! Scrolling is noticeably much slower with virtual consoles on a
EGA/VGA. The reason is that no longer does linux use all the screen
memory as a long buffer, but crams in several consoles in it. I think
it's worth it.

The virtual consoles also have some new screen-handling commands: they
confirm even better to vt200 control codes than 0.11. Special graphic
characters etc: you can well use them as terminals to VMS (although
that's a shameful waste of resources).

        pty's

Ok. I have to admit that I didn't get the hangup-code working correctly,
but that should be easy to add. The general things are there.

        select

I've never used it, so I cannot say how well it works. My minor testing
seems to indicate that it works ok. vc's, pty's and select were
implemented by pmacdona, although I hacked it heavily.

        387-emulation.

It's not complete, but it works well enough to run those gcc2.0 compiled
programs I tested (few).  None of the "heavy" math-functions are
implemented yet.

        Symbolic links.

Try out a few "ln -s xx yy", and ls -l. Note that I think tar should be
recompiled to know anout them, and probably some other programs too. The
0.12 rootimage-disk has most of the recompiled fileutilities.

        Virtual memory.

In addition to the "mkfs" program, there is now a "mkswap" program on
the root disk.  The syntax is identical: "mkswap -c /dev/hdX nnn", and
again: this writes over the partition, so be careful.  Swapping can then
be enabled by changing the word at offset 506 in the bootimage to the
desired device.  Use the same program as for setting the root file
system (but change the 508 offset to 506 of course).

NOTE! This has been tested by Robert Blum, who has a 2M machine, and it
allows you to run gcc without much memory.  HOWEVER, I had to stop using
it, as my diskspace was eaten up by the beta-gcc-2.0, so I'd like to
hear that it still works: I've been totally unable to make a
swap-partition for even rudimentary testing since about christmastime.
Thus the new changes could possibly just have backfired on the VM, but I
doubt it.

        And that's it, I think.

Happy hacking.

         Linus

---
## [gbmaster/linux](https://github.com/gbmaster/linux)@[6774a9ac56...](https://github.com/gbmaster/linux/commit/6774a9ac56a0d1079e5bcd950f2b3d703c6888db)
#### Thursday 2023-02-09 13:24:05 by Linus Torvalds

Linux-0.01 (September 17, 1991)

This is the initial 0.01 kernel as found on various history sites.

Fun facts:

 - kernel/Makefile still calls it the FREAX kernel

 - this was in a more innocent age, when the only copyright notice
   is a single "(C) 1991 Linus Torvalds" in lib/string.h

 - the keyboard driver was still in all assembly language, with a
   hardcoded map for (7-bit) Finnish keyboards. At least I had converted
   the VT100 emulation from assembly to C. Too bad I didn't keep the
   _really_ old code around for historical interest.

 - All the early kernels wanted a special version of gcc to compile: I
   had made extensions to gcc-1.40 to make it use the x86 string
   instructions for things like "memcpy()" using the "-mstring-insns"
   command line option.

 - Also, note that newer versions of gcc (which do have the inline
   intrisics, quite independently of my early -mstring-insns hack) will
   not accept the code: it needs a compiler that outputs old-style a.out
   format, and that accepts some of the strange inline assembly that I
   used.

 - In short: you really need some stone-age tools to actually compile
   this, if you actually want to.  And if you actually want to _run_ it
   too, you need to have some old hardware and most likely edit some of
   the hardcoded numbers too.  The harddisk driver has two different
   hardcoded settings: my harddisk, and Lasu's harddisk.

Statistics:

It's 88 files with about ten thousand lines, written by yours truly
except for the vsprintf routine which was co-written with Lars
Wirzenius.  Lasu wasn't as huge a fan of inline assembly as I was, thus
the comment

        "Wirzenius wrote this portably, Torvalds fucked it up :-)"

I think that comment pretty much sums it up ;)

Original release notes for 0.01 follow:

         Notes for linux release 0.01

         0. Contents of this directory

linux-0.01.tar.Z - sources to the kernel
bash.Z - compressed bash binary if you want to test it
update.Z - compressed update binary
RELNOTES-0.01 - this file

         1. Short intro

This is a free minix-like kernel for i386(+) based AT-machines.  Full
source is included, and this source has been used to produce a running
kernel on two different machines.  Currently there are no kernel
binaries for public viewing, as they have to be recompiled for different
machines.  You need to compile it with gcc (I use 1.40, don't know if
1.37.1 will handle all __asm__-directives), after having changed the
relevant configuration file(s).

As the version number (0.01) suggests this is not a mature product.
Currently only a subset of AT-hardware is supported (hard-disk, screen,
keyboard and serial lines), and some of the system calls are not yet
fully implemented (notably mount/umount aren't even implemented).  See
comments or readme's in the code.

This version is also meant mostly for reading - ie if you are interested
in how the system looks like currently.  It will compile and produce a
working kernel, and though I will help in any way I can to get it
working on your machine (mail me), it isn't really supported.  Changes
are frequent, and the first "production" version will probably differ
wildly from this pre-alpha-release.

Hardware needed for running linux:
        - 386 AT
        - VGA/EGA screen
        - AT-type harddisk controller (IDE is fine)
        - Finnish keyboard (oh, you can use a US keyboard, but not
          without some practise :-)

The Finnish keyboard is hard-wired, and as I don't have a US one I
cannot change it without major problems. See kernel/keyboard.s for
details. If anybody is willing to make an even partial port, I'd be
grateful. Shouldn't be too hard, as it's tabledriven (it's assembler
though, so ...)

Although linux is a complete kernel, and uses no code from minix or
other sources, almost none of the support routines have yet been coded.
Thus you currently need minix to bootstrap the system. It might be
possible to use the free minix demo-disk to make a filesystem and run
linux without having minix, but I don't know...

         2. Copyrights etc

This kernel is (C) 1991 Linus Torvalds, but all or part of it may be
redistributed provided you do the following:

        - Full source must be available (and free), if not with the
          distribution then at least on asking for it.

        - Copyright notices must be intact. (In fact, if you distribute
          only parts of it you may have to add copyrights, as there aren't
          (C)'s in all files.) Small partial excerpts may be copied
          without bothering with copyrights.

        - You may not distibute this for a fee, not even "handling"
          costs.

Mail me at "torvalds@kruuna.helsinki.fi" if you have any questions.

Sadly, a kernel by itself gets you nowhere. To get a working system you
need a shell, compilers, a library etc. These are separate parts and may
be under a stricter (or even looser) copyright. Most of the tools used
with linux are GNU software and are under the GNU copyleft. These tools
aren't in the distribution - ask me (or GNU) for more info.

         3. Short technical overview of the kernel.

The linux kernel has been made under minix, and it was my original idea
to make it binary compatible with minix. That was dropped, as the
differences got bigger, but the system still resembles minix a great
deal. Some of the key points are:

        - Efficient use of the possibilities offered by the 386 chip.
          Minix was written on a 8088, and later ported to other
          machines - linux takes full advantage of the 386 (which is
          nice if you /have/ a 386, but makes porting very difficult)

        - No message passing, this is a more traditional approach to
          unix. System calls are just that - calls. This might or might
          not be faster, but it does mean we can dispense with some of
          the problems with messages (message queues etc). Of course, we
          also miss the nice features :-p.

        - Multithreaded FS - a direct consequence of not using messages.
          This makes the filesystem a bit (a lot) more complicated, but
          much nicer. Coupled with a better scheduler, this means that
          you can actually run several processes concurrently without
          the performance hit induced by minix.

        - Minimal task switching. This too is a consequence of not using
          messages. We task switch only when we really want to switch
          tasks - unlike minix which task-switches whatever you do. This
          means we can more easily implement 387 support (indeed this is
          already mostly implemented)

        - Interrupts aren't hidden. Some people (among them Tanenbaum)
          think interrupts are ugly and should be hidden. Not so IMHO.
          Due to practical reasons interrupts must be mainly handled by
          machine code, which is a pity, but they are a part of the code
          like everything else. Especially device drivers are mostly
          interrupt routines - see kernel/hd.c etc.

        - There is no distinction between kernel/fs/mm, and they are all
          linked into the same heap of code. This has it's good sides as
          well as bad. The code isn't as modular as the minix code, but
          on the other hand some things are simpler. The different parts
          of the kernel are under different sub-directories in the
          source tree, but when running everything happens in the same
          data/code space.

The guiding line when implementing linux was: get it working fast. I
wanted the kernel simple, yet powerful enough to run most unix software.
The file system I couldn't do much about - it needed to be minix
compatible for practical reasons, and the minix filesystem was simple
enough as it was. The kernel and mm could be simplified, though:

        - Just one data structure for tasks. "Real" unices have task
          information in several places, I wanted everything in one
          place.

        - A very simple memory management algorithm, using both the
          paging and segmentation capabilities of the i386. Currently
          MM is just two files - memory.c and page.s, just a couple of
          hundreds of lines of code.

These decisions seem to have worked out well - bugs were easy to spot,
and things work.

         4. The "kernel proper"

All the routines handling tasks are in the subdirectory "kernel". These
include things like 'fork' and 'exit' as well as scheduling and minor
system calls like 'getpid' etc. Here are also the handlers for most
exceptions and traps (not page faults, they are in mm), and all
low-level device drivers (get_hd_block, tty_write etc). Currently all
faults lead to a exit with error code 11 (Segmentation fault), and the
system seems to be relatively stable ("crashme" hasn't - yet).

         5. Memory management

This is the simplest of all parts, and should need only little changes.
It contains entry-points for some things that the rest of the kernel
needs, but mostly copes on it's own, handling page faults as they
happen. Indeed, the rest of the kernel usually doesn't actively allocate
pages, and just writes into user space, letting mm handle any possible
'page-not-present' errors.

Memory is dealt with in two completely different ways - by paging and
segmentation.  First the 386 VM-space (4GB) is divided into a number of
segments (currently 64 segments of 64Mb each), the first of which is the
kernel memory segment, with the complete physical memory identity-mapped
into it.  All kernel functions live within this area.

Tasks are then given one segment each, to use as they wish. The paging
mechanism sees to filling the segment with the appropriate pages,
keeping track of any duplicate copies (created at a 'fork'), and making
copies on any write. The rest of the system doesn't need to know about
all this.

         6. The file system

As already mentioned, the linux FS is the same as in minix. This makes
crosscompiling from minix easy, and means you can mount a linux
partition from minix (or the other way around as soon as I implement
mount :-). This is only on the logical level though - the actual
routines are very different.

        NOTE! Minix-1.6.16 seems to have a new FS, with minor
        modifications to the 1.5.10 I've been using. Linux
        won't understand the new system.

The main difference is in the fact that minix has a single-threaded
file-system and linux hasn't. Implementing a single-threaded FS is much
easier as you don't need to worry about other processes allocating
buffer blocks etc while you do something else. It also means that you
lose some of the multiprocessing so important to unix.

There are a number of problems (deadlocks/raceconditions) that the linux
kernel needed to address due to multi-threading.  One way to inhibit
race-conditions is to lock everything you need, but as this can lead to
unnecessary blocking I decided never to lock any data structures (unless
actually reading or writing to a physical device).  This has the nice
property that dead-locks cannot happen.

Sadly it has the not so nice property that race-conditions can happen
almost everywhere.  These are handled by double-checking allocations etc
(see fs/buffer.c and fs/inode.c).  Not letting the kernel schedule a
task while it is in supervisor mode (standard unix practise), means that
all kernel/fs/mm actions are atomic (not counting interrupts, and we are
careful when writing those) if you don't call 'sleep', so that is one of
the things we can count on.

         7. Apologies :-)

This isn't yet the "mother of all operating systems", and anyone who
hoped for that will have to wait for the first real release (1.0), and
even then you might not want to change from minix.  This is a source
release for those that are interested in seeing what linux looks like,
and it's not really supported yet.  Anyone with questions or suggestions
(even bug-reports if you decide to get it working on your system) is
encouraged to mail me.

         8. Getting it working

Most hardware dependancies will have to be compiled into the system, and
there a number of defines in the file "include/linux/config.h" that you
have to change to get a personalized kernel.  Also you must uncomment
the right "equ" in the file boot/boot.s, telling the bootup-routine what
kind of device your A-floppy is.  After that a simple "make" should make
the file "Image", which you can copy to a floppy (cp Image /dev/PS0 is
what I use with a 1.44Mb floppy).  That's it.

Without any programs to run, though, the kernel cannot do anything. You
should find binaries for 'update' and 'bash' at the same place you found
this, which will have to be put into the '/bin' directory on the
specified root-device (specified in config.h). Bash must be found under
the name '/bin/sh', as that's what the kernel currently executes. Happy
hacking.

         Linus Torvalds "torvalds@kruuna.helsinki.fi"
         Petersgatan 2 A 2
         00140 Helsingfors 14
         FINLAND

---
## [gbmaster/linux](https://github.com/gbmaster/linux)@[e49565f5e6...](https://github.com/gbmaster/linux/commit/e49565f5e63cfb820c73e89073be2b12fe7f680f)
#### Thursday 2023-02-09 13:24:05 by Linus Torvalds

Linux-0.11 (December 8, 1991)

This was created from a re-packaged 0.11 tree.

Linux-0.11 has a few rather major improvements, but perhaps most
notably, is the first kernel where some other people start making
real contributions.

 - I fixed the buffer cache code, making it a lot more stable

 - demand-loading from disk. My comment proudly states:

        Once more I can proudly say that linux stood up to being changed: it
        was less than 2 hours work to get demand-loading completely implemented.

   This is a major milestone, since it makes the kernel much more
   powerful than Minix was at the time.  I also share clean pages.

 - we still don't have an /sbin/init, but we now load /etc/rc at bootup,
   and the kernel will loop, spawning shells forever. That makes it easier
   to test things.

 - scaffolding for math emulation introduced.

 - Ted Ts'o shows up as a coder. Ted implements:
        o "#!" escape handling for executables
        o fixes for some file permission handling
        o "sticky" directory bit
        o first "malloc()/free()" implementation.
          (this one is horrible: the free needs the size for good
           performance, which will result in years of "free_s()" pains)
        o adds BSD-style setreuid/gid() handling
        o allows us to specify root device at image build time
        o cleanups of some of the uglier direct %fs-register accesses

 - Galen Hunt shows up as a coder: he's added code to handle different
   video card detection (whereas my original one just handled VGA, we
   now handle CGA, MGA, EGA and VGA)

 - The console can beep now: John T Kohl (who also does the tty KILL
   char handling)

 - we also now have German (Wolfgang Thiel) and French (Marc Corsini)
   keyboard maps.  World Domination!

Btw, if you wonder what the "Urgel" comments are - I was still fairly
Swedish-speaking, and "Urgel" is what I would these days write as "Ugh".

It's a sign of trouble or ugly code.  The floppy driver in particular is
clearly not something I'm very proud of ;).

---
## [gbmaster/linux](https://github.com/gbmaster/linux)@[1f30554791...](https://github.com/gbmaster/linux/commit/1f3055479199a92caa4be7207d28b9c52be4f690)
#### Thursday 2023-02-09 13:24:05 by Linus Torvalds

[PATCH] Linux-0.95 (March 8, 1992)

This was the first kernel that got released under the GPL (0.12 had a
time-lapse to make sure the people involved accepted the license change:
nobody ever complained).

Because 0.12 had been so successful, this was supposed to be closer to
1.0.  Yeah, right.  1.0 was eventually released almost exactly two years
later..

The big change here is the first signs of a real VFS layer: while the
only available filesystem is still the Minix-compatible one, the code is
factored out, and the Minix-specific stuff is put in its own directory.
You can clearly see how the thing is moving towards having multiple
different filesystems.

The VFS changes also cause cleanups in various drivers, since we end
up having more clear inode operation structure pointer handling.

Superblock handling is still minix-specific..

NOTE! We also have /bin/init finally.  It still falls through to the old
"run shells forever" case if no init can be found, but it's starting to
look a whole more like real UNIX user-land now..

New developers: Ross Biro shows up, and does ptrace.  He will later end
up doing the first-generation networking code.

Other changes:

 - UK and Danish keyboard maps (and the keyboard driver supported
   "Application mode" keys from vt100+)
 - Make sure interrupts clear the 'D'irection flag
 - Floppy driver gets track buffer, which speeds it up immensely.  This
   was done based on patches by Lawrence Foard (entropy@wintermute.wpi.edu)
 - Lots of buffer cache cleanups.
 - support nonblocking pipe file descriptors
 - recursive symlink support
 - sys_swapon() means that we don't have to select the swap device
   at build (or boot) time ("Written 01/25/92 by Simmule Turner, heavily
   changed by Linus")
 - start some generic timer work (ugh, but these first timers were
   _horrible_ hardcoded things)
 - ptrace for debugging
 - console size query support with TIOC[G|S]WINSZ
 - /dev/kmem ("by Damiano")
 - rebooting (with ctrl-alt-del or sys_reboot()).

From the release notes:

              New features of 0.95, in order of appearance
                      (ie in the order you see them)

      Init/login

Yeah, thanks to poe (Peter Orbaeck (sp?)), linux now boots up like a
real unix with a login-prompt.  Login as root (no passwd), and change
your /etc/passwd to your hearts delight (and add other logins in
/etc/inittab etc).

      Bash is even bigger

It's really a bummer to boot up from floppies: bash takes a long time to
load.  Bash is also now so big that I couldn't fit compress and tar onto
the root-floppy: You'll probably want the old rootimage-0.12 just in
order to get tar+compress onto your harddisk.  If anybody has pointers
to a simple shell that is freely distributable, it might be a good idea
to use that for the root-diskette.

Especially with a small buffer-cache, things aren't fun. Don't worry:
linux runs much better on a harddisk.

      Virtual consoles on any (?) hardware.

You can select one of several consoles by pressing the left alt-key and
a function key at the same time. Linux should report the number of
virtual consoles available upon bootup. /dev/tty0 is now "the current"
screen, /dev/tty1 is the main console, and /dev/tty2-8 can exist
depending on your text-mode or card.

The virtual consoles also have some new screen-handling commands: they
confirm even better to vt200 control codes than 0.11. Special graphic
characters etc: you can well use them as terminals to VMS (although
that's a shameful waste of resources), and the PF1-4 keys work somewhat
in the application-key mode.

      Symbolic links.

0.95 now allows symlinks to point to other symlinks etc (the maximum
depth is a rather arbitrary 5 links). 0.12 didn't like more than one
level of indirection.

      Virtual memory.

VM under 0.95 should be better than under 0.12: no more lockups (as far
as I have seen), and you can now swap to the filesystem as well as to a
special partition. There are two programs to handle this: mkswap to set
up a swap-file/partition and swapon to start up swapping.

mkswap needs either a partition or a file that already exists to make a
swap-area. To make a swap-file, do this:

      # dd bs=1024 count=NN if=/dev/hda of=swapfile
      # mkswap swapfile NN

The first command just makes a file that is NN blocks long (initializing
it from /dev/hda, but that could be anything). The second command then
writes the necessary setup-info into the file. To start swapping, write

      # swapon swapfile

NOTE! 'dd' isn't on the rootdisk: you have to install some things onto
the harddisk before you can get up and running.

NOTE2! When linux runs totally out of virtual memory, things slow down
dramatically. It tries to keep on running as long as it can, but at
least it shouldn't lock up any more. ^C should work, although you might
have to wait a while for it..

      Faster floppies

Ok, you don't notice this much when booting up from a floppy: bash has
grown, so it takes longer to load, and the optimizations work mostly
with sequential accesses.  When you start un-taring floppies to get the
programs onto your harddisk, you'll notice that it's much faster now.
That should be about the only use for floppies under a unix: nobody in
their right mind uses floppies as filesystems.

      Better FS-independence

Hopefully you'll never even notice this, but the filesystem has been
partly rewritten to make it less minix-fs-specific. I haven't
implemented all the VFS-patches I got, so it's still not ready, but it's
getting there, slowly.

      And that's it, I think.

Happy hacking.

                      Linus (torvalds@kruuna.helsinki.fi)

---
## [gbmaster/linux](https://github.com/gbmaster/linux)@[899ea64d5b...](https://github.com/gbmaster/linux/commit/899ea64d5b064cf6c68ba1fc55808e8b1ffbfe26)
#### Thursday 2023-02-09 13:24:05 by Linus Torvalds

patch3....

Ok, I already announced it on the kernel mailing-list, but I might as
well go all the way. I put out patch3 to 0.96a yesterday, and it's
available on banjo in pub/Linux/Linus, and I'll upload it to the other
normal ftp-sites tonight.

NOTE! Patch3 is (like patch2) more of a kernel-hacker patch: it's just
in case you want to keep up with my kernel. It has some problems with
some serial lines, and if you experience them, I'd like to know what
type of chip you are running (and what linux reports on bootup). If you
don't think patching the kernel is fun, you might as well forget this
and wait for a real release (next month?).

Patch 3 contains:

- support for attaching and detaching processes under gdb (but you need
  a gdb that knows about this).
- 16550A support
- full core-dumping (again, you need a gdb that supports it)
- sockets have no problems with non-root binding etc
- /dev/zero implemented (mknod /dev/zero c 1 5)

None of the patches are very big (the whole patch is 17kB compressed,
most of it attach/detach code), but they are all pretty useful.

The 16550A support means that with the appropriate chip you now should
be able to use the serial ports at much higher speeds, but as mentioned,
it seems to break on some machines.

The detaching isn't perfect yet (I noticed only after making the diffs
that I had forgotten to do some cleanups), but it's not generally a
problem (the code just forgets to give the process back to it's rightful
father).

The patch is relative to the pl2 kernel, so you have to use the earlier
patches first. This time, I've added the lib/itimer.c code.

16550A support was written by tdavis, the correct format of the
core-dumps was written by eric (who also wrote the attach/detach code I
used as an example when implementing it), /dev/zero was written by
almesber. Nice to see good patches: I just did the socket-thing and
rewrote the attaching to suit me.

            Linus

---
## [gbmaster/linux](https://github.com/gbmaster/linux)@[4a4ded6ae1...](https://github.com/gbmaster/linux/commit/4a4ded6ae1bfea1dd3be95a5aef9275c1f3a24a2)
#### Thursday 2023-02-09 13:24:05 by Linus Torvalds

[PATCH] Linux-0.97 (August 1, 1992)

Move <xxx.h> to <linux/xxxx.h>

Variable-sized buffer blocks and dynamic buffer cache allocation. The VM
knows how to shrink it automatically!

Add support for "fast" interrupt handlers for serial lines.

Update copyrights to say 1992 too.

Remove broken VESA video card handling.

Separate out partition handling code ("genhd").

Make init unkillable.

Norwegian keyboard map.

Future Domain SCSI controller driver by Rik Faith.

Changes in 0.97:

 - The VESA-support was removed.  I'd be happy to put it back once it
   works on all hardware.  Instead of the VESA-code, I finally put in
   the automatic SVGA setup patches.  See the top-level Makefile.

 - The IRQ code has solidified, and should work on all machines.  Not
   all of the SCSI drivers use it yet, so I expect patches for that..

 - Serial interrupts are handled slightly differently, and performance
   should be up.  I've sent out a few alpha-releases, and testing seems
   to indicate that's actually true this time.  Reactions have ranged
   from "nice" to "wonderful" :-)

 - The buffer-cache and memory management code has been edited quite a
   bit.  ps/free etc programs that reads kernel memory directly no
   longer work, and even a recompilation won't be enough.  They actually
   need editing before they work.

   The buffer-cache now grows and shrinks dynamically depending on how
   much free memory there is.  Shift+PrintScreen will give some memory
   statistics.  (Ctrl+PrSc gives task-info, ALT+PrSc gives current
   register values).

   The mm code changes removed some race-conditions in the VM code, and
   I also tried to make the Out-of-swapspace error less severe (better
   thrashing-detection etc).

 - The super-block code has been cleaned up.  Especially the extended fs
   needs to be edited a bit to take advantage of the new setup, and I
   expect Remy Card will have a patch out eventually.

 - include-files have been moved around some more: there are still some
   names that clash with the standard headers, but not many.

 - Unswappable processes implemented: by default only 'init' is
   unswappable.  This is a bit safer in low-memory conditions, as at
   least init won't die due to low memory.  I also made killing init
   impossible: if init doesn't recognize a signal, it simply won't get
   it.  Some other changes ("while (1) fork();" won't kill the machine
   for non-root users etc)

 - The new SCSI drivers are in.  These make the kernel noticeably
   bigger, but you can leave them out if you don't want them.

 - The floppy- and hd-drivers print out more debugging-info in case of
   errors: this might be irritating if you have hardware that works, but
   often gives soft-errors.  On the other hand, some old debugging-info
   was removed - notably for user-level protection errors etc.

 - Various minor fixes.  I haven't made cdiffs (and I haven't gotten any
   requests for them, so I probably never will), but they would be
   pretty big.

Things that I didn't have time for:

 - I wanted to rewrite the tty drivers to be more "streams-like" (ie not
   an actual streams-implementation, but some of the ideas from
   streams).  I never got around to it: there was simply too much else
   to do.

 - I got a lot of patches, and some went in, others didn't.  If you
   think your patch was important, please re-send it relative to the new
   version.

I'd like comments on the new system: performance / clarity of code etc.
0.97 should correct all known bugs (at least the ones I know about), but
I guess that's just wishful thinking.

Note that the dynamic buffer-code also handles differently-sized
buffers, but that the rest of the system (block device drivers,
filesystem code etc) cannot yet take advantage of this - there is still
some coding needed.

		Linus

---
## [gbmaster/linux](https://github.com/gbmaster/linux)@[80c6dde28a...](https://github.com/gbmaster/linux/commit/80c6dde28a8260af634f72b0d788281d5ba3029a)
#### Thursday 2023-02-09 13:24:05 by Linus Torvalds

linux-0.96c.patch1 contains more changes than I originally envisioned: I
changed the IRQ routines and the serial code to be easier and cleaner
(and hopefully more efficient) and I thought that would be it. I was
wrong.

I got several patches (and one bug-report) again, and while I haven't
had time to check them all, some of them are in. Fixes:

 - Remy Cards correction to the out-of-space problem with the extended
fs is here. Most people using the ext-fs might already have applied
this patch, in which case you might have problems patching.

 - my ftruncate() fix is here. Again, if you already did the trivial
patch by hand, you'll get errors when patching.

 - almesber's implementation of read-only filesystems is here (after
editing by yours truly). The mount() system call now accepts a flags
integer as well as a pointer to some arbitraty data in user space for
some special mount() calls. The general flags allow (a) read-only
mounting, (b) disabling of suid executables (c) disabling of device
special files and (d) total disabling of executables on a per-filesystem
basis. The filesystem specific mount() info isn't currently used by any
fs, but can be used to specify additional information that depends on a
special fs type (a password or similar would be possible..)

 - the rename() system call had a bug in that it allowed moving over a
directory: I think the code to handle this was lost in the vfs editing,
and although the GNU mv utility checked it, a malicious (or just
unsuspecting) program can destroy the fs using this. Thanks for the
bug-report: it was very easy to add once I saw the problem.

 - support for vesa-standard svga cards in setup.S. I'm unable to test
this, but my svga card still works after the patch, so I left it in in
the hope that it doesn't break for anybody else.

 - various minor editing by me, or minor patches sent in by others.

The full cdiff is almost 50kB compressed, so this is a bigger-than-usual
patch. Hope there are no problems. People who are using the new SCSI
drivers might have problems with my changes to the SCSI irq-setup
changes, so be careful (actually using the original sources might be a
good idea, and then upgrading again). I hope to get the new SCSI
drivers into the kernel soon (definitely in time for 0.98).

I'd be interested to hear comments on serial line performance, bugs,
features, etc. As usual, I'm hoping this release won't contain any new
bugs while fixing all the old ones, but I guess that's likely to happen
right after the first winter olympics in Hell.

            Linus

---
## [Tomoms/android_frameworks_base](https://github.com/Tomoms/android_frameworks_base)@[b234e1282b...](https://github.com/Tomoms/android_frameworks_base/commit/b234e1282b441d75c0178e28d2f9676c62267f1f)
#### Thursday 2023-02-09 13:27:08 by Kuba Wojciechowski

[SQUASHED] core: Blacklist pixel system feature from Google Photos

    We want to include the P21 experience flag to enable new features,
    however it seems like Google Photos uses it to decide whether to use the
    TPU tflite delegate. There doesn't seem to be any fallback so we need to
    make sure the feature is not exposed to the app so that a normal
    NNAPI/GPU delegate can be used instead.

    Test: Google Photos editor with PIXEL_2021_EXPERIENCE feature in product
    Signed-off-by: Kuba Wojciechowski <nullbytepl@gmail.com>
    Change-Id: I51a02f8347324c7a85f3136b802dce4cc4556ac5

commit 67eb31b3bb43d06fcc7f6fdb2f92eb486451cae6
Author: kondors1995 <normandija1945@gmail.com>
Date:   Thu Jun 9 17:39:25 2022 +0530

    Core: Extend Pixel experience Blacklist For Google Photos

    Turns out having these brakes Original quality backups.
    Since these indicate that the device is pixel 4 with in the turn brakes device spoofing as OG pixel

    Change-Id: I336facff7b55552f094997ade337656461a0ea1d

commit 508a99cde60b73dc3f1e843d569bca31def35988
Author: ReallySnow <reallysnow233@gmail.com>
Date:   Fri Dec 31 16:40:23 2021 +0800

    base: core: Blacklist Pixel 2017 and 2018 exclusive for Google Photos

    * In this way can use PixelPropsUtils to simulate the Pixel XL prop
      method to use the unlimited storage space of Google Photos
    * Thanks nullbytepl for the idea

    Change-Id: I92d472d319373d648365c8c63e301f1a915f8de9

commit aaf07f6ccc89c2747b97bc6dc2ee4cb7bd2c6727
Author: Akash Srivastava <akashniki@gmail.com>
Date:   Sat Aug 20 19:04:32 2022 +0700

    core: Pixel experience Blacklist For Google Photos for Android 13

    * See, in Android 13 pixel_experience_2022_midyear was added, which needs to be blacklisted aswell

    Change-Id: Id36d12afeda3cf6b39d01a0dbe7e3e9058659b8e

commit 9d6e5749a988c9051b1d47c11bb02daa7b1b36fd
Author: spezi77 <spezi7713@gmx.net>
Date:   Mon Jan 31 19:17:34 2022 +0100

    core: Rework the ph0t0s features blacklist

    * Moving the flags to an array feels more like a blacklist :P
    * Converted the flags into fully qualified package names, while at it

    Signed-off-by: spezi77 <spezi7713@gmx.net>
    Change-Id: I4b9e925fc0b8c01204564e18b9e9ee4c7d31c123

commit d7201c0cff326a6374e29aa79c6ce18828f96dc6
Author: Joey Huab <joey@evolution-x.org>
Date:   Tue Feb 15 17:32:11 2022 +0900

    core: Refactor Pixel features

    * Magic Eraser is wonky and hard to
      enable and all this mess isn't really worth
      the trouble so just stick to the older setup.

    * Default Pixel 5 spoof for Photos and only switch
      to Pixel XL when spoof is toggled.

    * We will try to bypass 2021 features and Raven
      props for non-Pixel 2021 devices as apps usage
      requires TPU.

    * Remove P21 experience system feature check

Change-Id: Iffae2ac87ce5428daaf6711414b86212814db7f2

---
## [gbmaster/linux](https://github.com/gbmaster/linux)@[c3f602f0ab...](https://github.com/gbmaster/linux/commit/c3f602f0abdd0f83c536243d7d88bf268596a072)
#### Thursday 2023-02-09 13:44:37 by Linus Torvalds

[PATCH] Linux-0.99.7 (March 13, 1993)

Nigel Gamble makes lp driver able to use interrupts.

The mmap() code is finally starting to really happen.  In particular,
this means that "verify_area()" is doing more - it can check the actual
areas that have been mapped, rather than just blindly assume that the
user can access anything in the first 3GB.

For now, the mmap code only does anonymous mappings and /dev/mem.
Executables are still read into memory.  But the infrastructure is
there.

The VFS layer stops using names directly in user space - the race
conditions were just too hard to handle.  So pathnames are copied into
kernel space before they are looked up.

Ext2fs (Remy Card) and xiafs (Frank Xia) are merged.  Both are much
faster filesystems using bitmaps rather than freelists, and can handle
big disks and big files.

Ext2fs is based on extfs, while xiafs is a simpler straightforward
extension of the old minixfs.

Xiafs obviously was eventually dropped.

[Original announcement below]

It has been two weeks since the last release, so it's high time you
should once more enjoy the pleasures of patching up your kernel to a
higher version number if you are into those kinds of perversions.  Linux
0.99pl7 is available as both full source and diffs against pl6 on
nic.funet.fi: pub/OS/Linux/PEOPLE/Linus, and it will probably show up on
the other major sites within days.

As of pl7, I'm trying out a new format: both the full distribution and
the diffs are now compressed with gzip as it is now available at most
machines.  Also, the diffs are no longer context diffs: they use the
smaller unified diff format.  At least the stock SunOS 'patch' binary
seems not to understand them at all, but GNU patch has no problems, and
unified diffs are a bit smaller (not that it matters much after gzip has
done its deed on them).

As to the changes in pl7: they are many and varied, and hopefully all to
the better (-"Dream on Linus" -"Shut up").  Short list follows, hope I
haven't forgotten anything major.

 - ext2fs is in: note that this is version 0.2c and that if you are
   currently using an older version there are some changes.  Small
   filesystems (< 256MB) should reportedly be automatically converted,
   bigger filesystems need some assistance. Ext2fs written by Remy Card.
 - xiafs is also in: again, the final version uses a slightly different
   layout to support exact file block counts, so if you use the xiafs,
   you should make sure you have the latest fs-tools.  Xiafs written by
   Frank Xia.
 - updated Ultrastor SCSI driver with scatter/gather by Scott Taylor.
   It should be much faster, as well as support the Ultrastor-34F.
 - major changes in the memory manager.  Yours truly got carried away,
   and finally cleaned up the mm layer due to pmacdona wanting mmap() on
   /dev/zero.  This means that the IPC patches won't go in, and need
   updating.  Krishna?
 - more big changes: I rewrote most of the VFS filename-handling.
   Filenames are copied into kernel space before being used, which
   cleaned things up somewhat, as well as simplifying some race-
   condition handling.  As a result, I was also able to easily expand
   the minix fs to cover the "linux" fs that some people have been using
   (same layout, but with 30-character names).
 - updated the printer driver: Nigel Gamble.  It is now able to use
   interrupts, although the default behaviour is still to poll.
 - serial driver updates by tytso (but no SLIP yet)
 - various minor patches for POSIX compliace: Bruce Evans, Rick Sladkey
   and me.
 - other minor patches all over the place: scsi, tcpip etc.

All in all, the patches are almost half a megabyte even as unified
diffs: getting the full sources might be easier than patching it all up.

As always, some of the patches are actually tested by me, some aren't
(and just because I wrote some of them doesn't mean I actually *tested*
them: I have no idea if mmap() works on /dev/zero, although it should).
I have neither a printer nor an Ultrastor controller, and I haven't got
the diskspace to test out the new filesystems, so I can only hope they
work "as advertized".  If you have problems, I want to hear about them,
so keep the reports coming, and try to pinpoint the problem as well as
you can ("when I do *this* it happens every time..").

                Linus

---
## [Tomoms/android_packages_apps_Settings-t](https://github.com/Tomoms/android_packages_apps_Settings-t)@[007ec58be4...](https://github.com/Tomoms/android_packages_apps_Settings-t/commit/007ec58be41a44f035aff3e1d3de83096578872d)
#### Thursday 2023-02-09 14:19:49 by Ido Ben-Hur

Settings: Refactor and clean connectivity check preference

wow this was just horrible...

Made this preference way more maintainable and runtime effective:
* Declare the preference in xml instead of hardcoding - this makes it searchable, more maintainable and is also better runtime wise
* Use arrays instead of manually naming each URL
* Use an ArrayList to handle index <-> setting relationship more easily
* Use static imports instead of literal calls
* Actually handle cases of non availability
* There is absolutely no reason to handle OnResume here
* Get rid of useless functions
* Get rid of useless imports
* Move resources to the proper custom files so we don't confuse translators
* More, too lazy. Don't write shit code please. Thank you.

Change-Id: Idd3b95d851ec83b36005b7a52880932df7e5009e

---
## [GrayMatterWorks/Dpboss-SattaMatka-Online-Play](https://github.com/GrayMatterWorks/Dpboss-SattaMatka-Online-Play)@[e4b4b53684...](https://github.com/GrayMatterWorks/Dpboss-SattaMatka-Online-Play/commit/e4b4b5368449cfe239d3e403f18e6930e8c04390)
#### Thursday 2023-02-09 14:31:59 by GrayMatterWorks

Add files via upload

Kalyan bazar Satta online matka results app Kalyan Jodi Ank Panna Single Satta Matka  Milan bazar Gali Disawar Result App entertainment

Please note that our app is only for entertainment purpose. No Real money involved in our app

Kalyan Bazar Satta Matka - Online Matka Play App is Online Kalyan Bazar Satta Matka Play App Play online matka satta matka dpboss for Entertainment Purpose Only.

Online Matka Play App for Entertainment Purpose Only

Welcome To The World Of Dpboss Kalyan Bazar Satta Matka - Online Matka Play App , Here You Get Latest Information About Satta Matka Guessing, Satta Matka Kalyan And Much More.

Kalyan  Bazar Satta  Matka online RESULT:- Provides You Latest Satta Result, Today's Matka Result, Quickly Updated Satta Matka Etc. We Also Porvide You Free Matka Tips Today, Perfect Satta Matka Tips And Kalyan Matka Tips.

Kalyan Bazar dpboss Satta Matka  , Is The Only Website That Provide You Perfect And Sure Guessing Of Kalyan Matka, Main Mumbai, Milan Day/Night Etc.

Kalyan dpboss Bazar Satta Matka - Online Matka Play App is a very fantastic application. For sports person. We providing the best and fast service to a sports person.

We providing fast results for all markets Like - Kalyan, Shridevi, Milan etc.
We provide best Satta Matka Tips, Online Matka Result, Online Matka Play app for Kalyan, Live Matka Result, Kalyan Chart, Kalyan Panel Chart, Dpboss Online information.

We need consistent support to get going. If you have enjoyed this app and helpful for your life, do not forget to rate us on the play store. Please help us by spreading this app amongst your friends.

Declaration:
All content provided by Kalyan Bazar satta Matka - Online Matka Play App.
All information provided by Kalyan Bazar Matka - Online Matka Play App and this application does not relate to any illegal Business.

Note:- Please note that this app is only for sports persons. No Real Money Involved in this App.

---
## [kewbish/ubccsss.org](https://github.com/kewbish/ubccsss.org)@[a072092d42...](https://github.com/kewbish/ubccsss.org/commit/a072092d42ecf2c8a1b044de8fe93d9cc4107ea1)
#### Thursday 2023-02-09 15:39:22 by csssbot

New review for CPSC 310 by Andy Liang (#378)

> The course consists of a full stack project (no DB) where the hardest
part of the project is actually more algorithm related ish (building a
query engine) than it is software construction in my opinion. The
project itself ended up being very useless (especially if you have done
one decent full stack personal project or have coop experience) since
there is no code quality enforcement. This means you are free to write
garbage code, as long as it works. I would advice to start early on the
project though!

The conceptual portion taught in lecture is useful. However the project,
nor any other part of the course, really forces you to try the design
patterns that you have learned. :)
>
> Difficulty: 3/5
> Quality: 2/5
> <cite><a href=''>Andy Liang</a>, Feb 05 2023, course taken during
2022W1</cite>
<details><summary>View YAML for new review</summary>
<pre>
  - author: Andy Liang
    authorLink: 
    date: 2023-02-05
    review: |
The course consists of a full stack project (no DB) where the hardest
part of the project is actually more algorithm related ish (building a
query engine) than it is software construction in my opinion. The
project itself ended up being very useless (especially if you have done
one decent full stack personal project or have coop experience) since
there is no code quality enforcement. This means you are free to write
garbage code, as long as it works. I would advice to start early on the
project though!
      
The conceptual portion taught in lecture is useful. However the project,
nor any other part of the course, really forces you to try the design
patterns that you have learned. :)
    difficulty: 3
    quality: 2
    sessionTaken: 2022W1

<pre>
</details>This is an auto-generated PR made using:
https://github.com/ubccsss/course-review-worker

---
## [DrSensor/nusa](https://github.com/DrSensor/nusa)@[bd0021498d...](https://github.com/DrSensor/nusa/commit/bd0021498de950b1c4629949bc4f43f2f6fa5c77)
#### Thursday 2023-02-09 16:30:09 by Fahmi Akbar Wildana

Story of lockfile 🔒

In the not-too-distant future, the world was heavily reliant on software
for nearly everything. Companies and organizations had come to rely on
a multitude of dependencies and libraries, all managed by complex
package managers and lock files.

However, as time passed, the number of dependencies and libraries grew
exponentially, leading to an ever-increasing web of interdependent
software systems. The lock files that were meant to keep these systems
stable and secure began to crumble under the weight of their own complexity.

One day, a small error was introduced into one of the lock files,
which quickly cascaded into a massive chain reaction, causing software
systems all over the world to fail. Banks, transportation systems,
hospitals, and even military defense systems were all affected
by the disastrous bug.

The error was traced back to a single library, which was used by
hundreds of other dependencies and libraries. The library had been
updated by its developers, but the lock file had not been updated to
reflect the change, causing a mismatch between the expected and actual
versions of the library.

Panic and chaos erupted as people all over the world were affected by
the malfunctioning software. Governments declared a state of emergency,
and teams of engineers worked tirelessly to try and fix the problem,
but the sheer complexity of the interdependent systems made it nearly
impossible to find and fix the root cause of the issue.

As the days passed, more and more systems failed, leading to widespread
famine, disease, and social unrest. The world had been brought to its
knees by the very software that was meant to keep it running smoothly.

And so began the Doom Age of Dependencies Lock Files, a time of
darkness and despair, where the once-great civilizations of the world
were brought low by the complexity of their own technology. But through
it all, the human spirit remained strong, and eventually, new systems
were built, stronger and more resilient than before.
The Doom Age of Dependencies Lock Files would forever be remembered as
a cautionary tale of what can happen when technology outpaces
our ability to manage it.

---
## [jonpryor/java.interop](https://github.com/jonpryor/java.interop)@[132e49c71a...](https://github.com/jonpryor/java.interop/commit/132e49c71a8a858253290b7a956674d4a50bd914)
#### Thursday 2023-02-09 16:31:21 by Jonathan Pryor

[Java.Interop.Tools.Expressions] Add Java.Interop.Tools.Expressions

Fixes: https://github.com/xamarin/java.interop/issues/616

Context: https://github.com/xamarin/java.interop/issues/14
Context: ff4053cb1e966ebec1c16f97211b9ded936f2707
Context: da5d1b8103bb90f156b93ebac9caa16cfc85764e
Context: 4787e0179b349ab5ee0d0dd03d08b694acea4971
Context: 41ba34856ab119ea6e22ab103320180143fdf03d

Remember `jnimarshalmethod-gen` (176240d2)?  And it's crazy idea to
use the `System.Linq.Expressions`-based custom marshaling
infrastructure (ff4053cb, da5d1b81) to generate JNI marshal methods
at build/packaging time.  And how we had to back burner it because
it depended upon `System.Reflection.Emit` being able to write
assemblies to disk, which is a feature that never made it to
.NET Core, and is still lacking as of .NET 7?

Add `src/Java.Interop.Tools.Expressions`, which contains code which
uses Mono.Cecil to compile `Expression<T>` expressions to IL.

Then update `jnimarshalmethod-gen` to use it!

~~ Usage ~~

	% dotnet bin/Debug-net7.0/jnimarshalmethod-gen.dll \
	  bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
	  -v -v --keeptemp \
	  --jvm /Library/Java/JavaVirtualMachines/microsoft-11.jdk/Contents/Home/lib/jli/libjli.dylib \
	  -o _x \
	  -L bin/TestDebug-net7.0 \
	  -L /usr/local/share/dotnet/shared/Microsoft.NETCore.App/7.0.0

First param is assembly to process; `Java.Interop.Export-Tests.dll`
is handy because that's what the `run-test-jnimarshal` target in
`Makefile` processed.

  * `-v -v` is *really* verbose output

  * `--keeptemp` is keep temporary files, in this case
    `_x/Java.Interop.Export-Tests.dll.cecil`.

  * `--jvm PATH` is the path to the JVM library to load+use.

  * `-o DIR` is where to place output files; this will create
    `_x/Java.Interop.Export-Tests.dll`.

  * `-L DIR` adds `DIR` to library resolution paths; this adds
    `bin/TestDebug/net7.0` (dependencies of
    `Java.Interop.Export-Tests.dll`) and
    `Microsoft.NETCore.App/7.0.0-rc.1.22422.12` (net7 libs).

By default the directories containing input assemblies and the
directory containing `System.Private.CoreLib.dll` are part of the
default `-L` list.

When running in-tree, e.g. AzDO pipeline execution, `--jvm PATH`
will attempt to read the path in `bin/Build*/JdkInfo.props`
a'la `TestJVM` (002dea4a).  This allows an in-place update in
`core-tests.yaml` which does:

	dotnet bin/Debug-net7.0/jnimarshalmethod-gen.dll \
	  bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll \
	  -v -v --keeptemp -o bin/TestDebug-net7.0

~~ Using `jnimarshalmethod-gen` output ~~

What does `jnimarshalmethod-gen` *do*?

	% ikdasm bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll > beg.il
	% ikdasm _x/Java.Interop.Export-Tests.dll > end.il
	% git diff --no-index beg.il end.il
	# https://gist.github.com/jonpryor/b8233444f2e51043732bea922f6afc81

is a ~1KB diff which shows, paraphrasing greatly:

	public partial class ExportTest {
	    partial class '__<$>_jni_marshal_methods' {
	        static IntPtr funcIJavaObject (IntPtr jnienv, IntPtr this) => …
	        // …
	        [JniAddNativeMethodRegistration]
	        static void __RegisterNativeMembers (JniNativeMethodRegistrationArguments args) => …
	    }
	}
	internal delegate long _JniMarshal_PP_L (IntPtr jnienv, IntPtr self);
	// …

wherein `ExportTest._<$>_jni_marshal_methods` and the `_JniMarshal*`
delegate types are added to the assembly.

This also unblocks the desire stated in 4787e017:

> For `Java.Base`, @jonpryor wants to support the custom marshaling
> infrastructure introduced in 77a6bf86.  This would allow types to
> participate in JNI marshal method ("connector method") generation
> *at runtime*, allowing specialization based on the current set of
> types and assemblies.

What can we do with this `jnimarshalmethod-gen` output?  Use it!

First, make sure the tests work:

	% dotnet test --logger "console;verbosity=detailed" bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll
	…
	Passed!  - Failed:     0, Passed:    17, Skipped:     0, Total:    17, Duration: 103 ms - Java.Interop.Export-Tests.dll (net7.0)

Then update/replace the unit test assembly with
`jnimarshalmethod-gen` output:

	% \cp _x/Java.Interop.Export-Tests.dll bin/TestDebug-net7.0
	% dotnet test --logger "console;verbosity=detailed" bin/TestDebug-net7.0/Java.Interop.Export-Tests.dll
	…
	Total tests: 17
	     Passed: 17

`core-tests.yaml` has been updated to do this.

~~ One-Off Tests ~~

One-off tests: ensure that the generated assembly can be decompiled:

	% ikdasm  bin/TestDebug-net7.0/Java.Interop.Tools.Expressions-Tests-ExpressionAssemblyBuilderTests.dll
	% monodis bin/TestDebug-net7.0/Java.Interop.Tools.Expressions-Tests-ExpressionAssemblyBuilderTests.dll

	% ikdasm  _x/Java.Interop.Export-Tests.dll
	% monodis _x/Java.Interop.Export-Tests.dll
	# which currently fails :-()

Re-enable most of `Java.Interop.Export-Tests.dll` for .NET 7;
see 41ba3485, which disabled those tests.

To verify the generated IL, use the [dotnet-ilverify][0] tool:

	dotnet tool install --global dotnet-ilverify

Usage of which is "weird":

	$HOME/.dotnet/tools/ilverify _x/Java.Interop.Export-Tests.dll \
	  --tokens --system-module System.Private.CoreLib \
	  -r 'bin/TestDebug-net7.0/*.dll' \
	  -r '/usr/local/share/dotnet/shared/Microsoft.NETCore.App/7.0.0/*.dll'
	All Classes and Methods in /Volumes/Xamarin-Work/src/xamarin/Java.Interop/_x/Java.Interop.Export-Tests.dll Verified.
	# no errors!

where:

  * `--tokens`: Include metadata tokens in error messages.
  * `--system-module NAME`: set the "System module name".  Defaults
    to `mscorlib`, which is wrong for .NET 5+, so this must be set to
    `System.Private.CoreLib` (no `.dll` suffix!).
  * `-r FILE-GLOB`: Where to resolve assembly references for the
    input assembly.  Fortunately file globs are supported…

~~ Removing `System.Private.CoreLib` ~~

`System.Private.CoreLib.dll` is *private*; it's not part of the
public assembly surface area, so you can't use
`csc -r:System.Private.CoreLib …` and expect it to work.  This makes
things interesting because *at runtime* everything "important" is in
`System.Private.CoreLib.dll`, like `System.Object`.

Specifically, if we do the "obvious" thing and do:

	newTypeDefinition.BaseType = assemblyDefinition.MainModule
	    .ImportReference (typeof (object));

you're gonna have a bad type, because the resulting IL for
`newTypeDefinition` will have a base class of
`[System.Private.CoreLib]System.Object`, which isn't usable.

Fix this by:

 1. Writing the assembly to a `Stream`.
 2. Reading the `Stream` from (1)
 3. Fixing all member references and assembly references so that
    `System.Private.CoreLib` is not referenced.

If `jnimarshalmethod-gen.dll --keeptemp` is used, then a `.cecil`
file is created with the contents of (1).

Additionally, and unexpectedly -- [jbevain/cecil#895][1] -- Mono.Cecil
adds a reference to the assembly being modified.  Remove the declaring
assembly from `AssemblyReferences`.

[0]: https://www.nuget.org/packages/dotnet-ilverify
[1]: https://github.com/jbevain/cecil/issues/895

---
## [PeriodicChaos/tgstation](https://github.com/PeriodicChaos/tgstation)@[97db4ecca4...](https://github.com/PeriodicChaos/tgstation/commit/97db4ecca46ddac5b10f6bd7b2088fc2bd1f5aea)
#### Thursday 2023-02-09 16:34:44 by Jeremiah

Adds the Cursed quirk  (#72317)

## About The Pull Request
Adds a silly negative quirk inspired by fallout's bloody mess.

Bad luck interactions for
- Microwaving
- Cigarette coupons
- Russian roulette
- Vending machines
- Ledges
- Slipping

All of which have a chance to kill you, which, by the way, causes you to
**delimb and explode**.

This changes the admin smite as well since it's all the omen component.
Giving permanent omens will mean the player will gib on death, which is
super probable given the insane base damage from bonking your head.
Permanent omen smites are basically dooming someone to die of natural
causes.

<details>
<summary>GIFs</summary>


![dreamseeker_ZE6hyRdYet](https://user-images.githubusercontent.com/42397676/209779120-f7d76862-91e2-4366-a49d-e93366d96faf.gif)

updated: Death no longer fully gibs (carbons)

![dreamseeker_8S8r6B6gMM](https://user-images.githubusercontent.com/42397676/209874302-2e24f581-ffda-42e7-9794-dbe0fff2ff5b.gif)

Panic at seeing bad omen coupons

![dreamseeker_tykHbePTSS](https://user-images.githubusercontent.com/42397676/209887936-5d7f5edf-6fa2-41c7-8503-37432b49c7c0.gif)


![3](https://user-images.githubusercontent.com/42397676/209885388-90523f2c-531a-4928-96b2-c902552cbbbc.png)
</details>

## Why It's Good For The Game
Adds a bit of physical comedy and difficulty for players that want it.
## Changelog
:cl:
add: Hope you saved for a rainy day: Added the 'Cursed' quirk which
causes excessive slippage and... other difficulties.
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Timberpoes <silent_insomnia_pp@hotmail.co.uk>
Co-authored-by: Watermelon914 <37270891+Watermelon914@users.noreply.github.com>

---
## [cashapp/multiplatform-paging](https://github.com/cashapp/multiplatform-paging)@[35675c8000...](https://github.com/cashapp/multiplatform-paging/commit/35675c8000d88a11fb73e752e5331f5fdc1100a3)
#### Thursday 2023-02-09 17:14:54 by Aurimas Liutikas

Move to AGP 3.0.0 stable 😁

Finally after many months of pain, suffering and tears we get to
move to the stable version of AGP even it this is going to last
us a short while until we need the next bleeding edge AGP feature
in support library to make our lives gloomy yet again.

For now - rejoice!

Test: ./gradlew buildOnServer
Change-Id: Ia6e1f7a8ecc4ecc4e79283d970d6defbd70828c6

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[5f78464e25...](https://github.com/harryob/cmss13/commit/5f78464e255b89ada7ca58f5114561be7b32f055)
#### Thursday 2023-02-09 17:21:07 by NewyearnewmeUwu

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
## [ArcaneDefence/tgstation](https://github.com/ArcaneDefence/tgstation)@[ef335f7d1f...](https://github.com/ArcaneDefence/tgstation/commit/ef335f7d1f33d196062a5a285c7f7216df2302a6)
#### Thursday 2023-02-09 17:49:15 by Rhials

It Came From Outer Spess: Adds midround changelings, delivered by an absolutely disgusting changeling meteor (#73018)

## About The Pull Request

Adds a new dynamic midround opportunity and random event - Space
Changeling.


https://user-images.githubusercontent.com/28870487/215284465-f5c5c1b1-b83d-471a-89be-1b65a4d2f2d4.mp4

If you are fortunate enough to recieve this role, you will be stuffed
into a changeling meteor and hurled at the side of the station. With no
crew identities, no access, and no equipment, you'll have to rely on
your **free** organic space suit and armblade to infiltrate the station
and get settled.

With no disguises to fall back on, the midround changeling experience
may lead to some very unfavorable situations. It's not unlikely that
you'll be spotted making your way inside, or that someone will see the
impact site and cause a panic. This role is not easy, but keep in mind
that you also have nothing to lose in the event that you use Lesser
Form/Headslug.

Aside from the starting circumstances, you have the same objectives and
capabilities as a roundstart changeling. Getting inside of the station
will be the hard part, but from there you can do what changelings do
best and blend in.

<details>
<summary>A brief note on the free stuff you get:</summary>
<br>
You get the organic space suit and armblade for free. The space suit is
absolutely vital, but I decided that the armblade should be given for
free as well. It's necessary for breaking open windows or airlocks and
getting access to the station, since otherwise your options are limited
to arrivals/departures. Having to pay a 2 point tax to avoid walking
naked into the main hallways of the station and getting gibbed is lame,
and with the added difficulty of the role I think it's fair.
</details>

Also, this is my 100th PR here! :)

## Why It's Good For The Game

Adds midround changelings in a WAY COOLER way than just making a random
crew/new arrival a changeling.

Lets people experience Hardmode Changeling, and test the adaptability
and flexibility of the most versatile antagonist even harder than
before. Losing the option to bypass the whole shape-shifter thing by
disguising as your crew identity presents a welcome change to the
formula.

Adds a teensy bit more midround variety, so we stop getting Nightmare At
The Thirty Minute Mark every round.
## Changelog
:cl: Rhials
add: Midround changeling spawn event.
add: Changeling meteor. It has a present for you.
/:cl:

---
## [whiteinge/dotfiles](https://github.com/whiteinge/dotfiles)@[5df5017605...](https://github.com/whiteinge/dotfiles/commit/5df5017605d7615bd592ffee82af13d553aadb7b)
#### Thursday 2023-02-09 17:56:52 by Seth House

Add default graphical packages for WSL and wslu utils

Turns out WSL2 ships with working, pre-configured, out-of-box support
for graphical apps and sound (using the main, official Ubuntu distro).
No tweaking or installation needed. That is absolutely mind-blowing.

Gimp and Inkscape run beautifully. I prefer using boring, steady,
predicable xterm and it looks fantastic in WSL with my default
Xresources config, including anti-aliased fonts. Clipboard support
between WSL and Windows Just Works (TM) in xterm and gVim. You can tell
the apps are running out of a container rather than natively, but
there's only a very slight input lag. Firefox can't be installed because
Ubuntu still thinks Snaps are a good idea (but that's not WSL's fault).
Overall surprisingly great experience.

As WSL has matured, I've wondered if WSL makes Windows a better, more
friendly development environment than OS X nowadays. This clinches it:
the answer is yes. Much eeasier to install, better defaults, more
features, way more similar to running native Linux. And this environment
is fully supported by Microsoft rather than the neglected and abused
red-headed step-children that Apple has with Homebrew, XQuartz,
`/usr/local`, and the random mishmash of BSD and GNU utils.

If you can't run Linux natively at work, running a full Linux inside
Windows via WSL is a _better_ experience than running a half-UNIX
alongside OS X via Homebrew and XQuartz.

Apple has been moving away from their UNIX roots and is being ever more
hostile to open source projects. In contrast, Microsoft is leaning in,
hard, with WSL. Never thought I'd be here, but as a programmer I'll be
requesting Microsoft hardware instead of Apple hardware at future jobs.

---
## [fdncred/nushell](https://github.com/fdncred/nushell)@[3d65fd7cc4...](https://github.com/fdncred/nushell/commit/3d65fd7cc4f6e0db0c1c31b895feabf2be66cb0a)
#### Thursday 2023-02-09 18:45:41 by Doru

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
## [Enchoseon/2based2wait](https://github.com/Enchoseon/2based2wait)@[259b126aa6...](https://github.com/Enchoseon/2based2wait/commit/259b126aa6712030c008db41f82537c32ed52662)
#### Thursday 2023-02-09 19:15:19 by unclamped

refactor: use string template literals

note to more experienced, older dev me in the future: if you have found a way to make this automatically, then please feel free to laugh at your young yourself. my fingers fucking hurt.

---
## [ZhengPeiRu21/azerothcore-wotlk](https://github.com/ZhengPeiRu21/azerothcore-wotlk)@[ef949f9ff0...](https://github.com/ZhengPeiRu21/azerothcore-wotlk/commit/ef949f9ff0a89e837c67258d7e199da1706bc438)
#### Thursday 2023-02-09 19:42:21 by ICXCNIKA

fix(DB/Locale): deDE fix request items texts #02 (#14615)

Process of translation: only original sources of deDE texts by
researching multiple sources, reverse translation by searching for
related quest items/NPCs and using these names to reconstruct a proper
translation.

This fixes the terms

Coldtooth-Mine (Eisbeißermine), Doomhammer (Schicksalshammer), Fizzle
(Zischel), Fizzledowser (Rutenwünschels), Fizzlebub (Zischelbub),
Burning Blade (Brennende Klinge), Ashenvale (Eschental),
Bloodscalp/s/stamm (Blutskalpe, Blutskalpstamm),
Darkspeartrolle/Darkspears/Darkspearstamm (Dunkelspeere,
Dunkelspeertrolle, -stamm), Moonglade (Mondlichtung), Starblaze
(Sternenschauer), Shadowglen (Laubschattental), Darrowshire (Darroheim),
Booty Bay (Beutebucht), Ratchet (Ratschet), Dizzywig (Flunkerblick),
Hearthglen (Herdweiler), Chillwindspitze (Zugwindspitze), Stormrage
(Sturmgrimm), Stormpike (Sturmlanze/n), Ironforge (Eisenschmiede),
Thunderhorn (Donnerhörner), Steamboil (Kesseldampf), Twilight-Hammer,
-klan (Schattenhammer/Schattenhammerklan), Fathom-Kern (Tiefenkern),
Blackfathom Deeps (Tiefschwarze Grotte), Blackrock-* (Schwarzfels-*),
Hawkwind (Falkenwind), Feathermoon (Mondfeder), Moonrage (Mondzorn),
Firemane (Feuermähne), Searingblade (Sengende Klinge), Ragefireabgrund
(Flammenschlund), Ironbands Areal (Eisenbands Lager), Zandalar
(Zandalari), Southshore (Süderstade)

for quest progress/request text entries for the deDE localisation with
proper casus/declension (these are not proper translated names of
locations/NPCs that have been left over by Blizzard since their language
localisations in TBC in 2006 and onward).

Added missing progress/request text entries for 308, 311, 417, 1644,
1787, 5059, 5060, 5721, 6004, 6023, 6025, 6187, 8042, 8043, 8044, 8046,
8047, 8048, 8050-8079, 8102, 8107, 8108, 8111, 8112, 8113, 8117, 8118,
8142, 8143, 8147, 8183-8195, 8238, 8239, 8240, 8243, 8246, 8860, 9594,
9692, 9707, 10414, 10415, 10919, 11451. (A lot of them are
Zandalari/Zul'Gurub related quests.)

Replaced post-Cataclysm progress/request text entries for 933, 935,
6387, 7383.

Fixed a wrong $R with plain text at progress/request text for 9147.

Added missing female gender equivalent to 6391.

(There are probably more changes in the file that aren't further
explained here as it was hard to keep track of everything. If you think
I made a mistake or have questions please contact me directly.)

<!-- First of all, THANK YOU for your contribution. -->

## Changes Proposed:
-  Fixing a lot in the quest_request_items_locale table.

## Issues Addressed:
<!-- If your fix has a relating issue, link it below -->
- Fixing some of the tasks in
https://github.com/azerothcore/azerothcore-wotlk/issues/14244
Referring to my other two bug reports from CC Github:
- https://github.com/chromiecraft/chromiecraft/issues/4697
- https://github.com/chromiecraft/chromiecraft/issues/4745

## SOURCE:
<!-- If you can, include a source that can strengthen your claim -->
- Read the text on top.

## Tests Performed:
<!-- Does it build without errors? Did you test in-game? What did you
test? On which OS did you test? Describe any other tests performed -->
- Not tested.


## How to Test the Changes:
<!-- Describe in a detailed step-by-step order how to test the changes
-->
All of the changes are to reward texts of quests, can be tested by
completing quests or simply reviewing the changed file.

## Known Issues and TODO List:
<!-- Is there anything else left to do after this PR? -->

- [ ]
- [ ]

<!-- If you intend to contribute repeatedly to our project, it is a good
idea to join our discord channel. We set ranks for our contributors and
give them access to special resources or knowledge:
https://discord.com/invite/DasJqPba)
Do not remove the instructions below about testing, they will help users
to test your PR -->
## How to Test AzerothCore PRs
 
When a PR is ready to be tested, it will be marked as **[WAITING TO BE
TESTED]**.

You can help by testing PRs and writing your feedback here on the PR's
page on GitHub. Follow the instructions here:

http://www.azerothcore.org/wiki/How-to-test-a-PR

**REMEMBER**: when testing a PR that changes something **generic** (i.e.
a part of code that handles more than one specific thing), the tester
should not only check that the PR does its job (e.g. fixing spell XXX)
but **especially** check that the PR does not cause any regression (i.e.
introducing new bugs).

**For example**: if a PR fixes spell X by changing a part of code that
handles spells X, Y, and Z, we should not only test X, but **we should
test Y and Z as well**.

---
## [catlettra/RootingForNature](https://github.com/catlettra/RootingForNature)@[ec5c645965...](https://github.com/catlettra/RootingForNature/commit/ec5c645965c2d4fede2e969512ccff52c02f754a)
#### Thursday 2023-02-09 19:59:01 by Elettra Messuri

Landing page created

I hate my life I wish I was born a cat

---
## [Veiyna/Voidcrew-LRP](https://github.com/Veiyna/Voidcrew-LRP)@[a05d69d10a...](https://github.com/Veiyna/Voidcrew-LRP/commit/a05d69d10a26b502d8ef6fe86b023fd95025ca0f)
#### Thursday 2023-02-09 20:21:57 by Addust

oh my fucking god I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JSON I HATE JS…

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[8eac9e98f2...](https://github.com/pytorch/pytorch/commit/8eac9e98f2ca427362d73878114a4067b6e5cf60)
#### Thursday 2023-02-09 22:28:01 by Brian Hirsh

Update base for Update on "add torch.autograd._set_view_replay_enabled, use in aot autograd"

tldr; this should fix some minor perf regressions that were caused by adding more as_strided() calls in aot autograd.

This PR adds a new context manager, `torch.autograd._set_view_replay_enabled()`.

Context: AOT Autograd has special handling for "outputs that alias graph intermediates". E.g. given this function:

```
def f(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    return out
```

AOT Autograd will do the following:

```
def fn_to_compile(x):
    y = torch.mul(x, 2)
    out = y.view(-1)
    # return the graph intermediate
    return y, out

compiled_fn = compile(fn_to_compile)

def wrapper(x):
    y, out = compiled_fn(x)
    # regenerate the alias of the graph intermediate
    return out._view_func(y)
```

What's annoying is that `out._view_func()` will result in a `.as_strided` call, because `out` is an ordinary runtime tensor. This (likely?) caused a perf regression, because when running the backward, out `as_strided_backward()` is slower than our `view_backward()`.

In this PR, I added some TLS for instructing autograd to do view replay instead of as_strided, even when given a normal tensor. I'm definitely interested in thoughts from autograd folks (cc albanD soulitzer). A few points that I want to bring up:

(1) One reason that this API seems generally useful to me is because of the case where you `torch.compile()` a function, and you pass in two inputs that alias each other, and mutate one of the inputs. Autograd is forced to add a bunch of as_strided() calls into the graph when this happens, but this would give users an escape hatch for better compiled perf in this situation

(2) To be fair, AOT Autograd probably won't need this TLS in the long term. There's a better (more complicated) solution, where AOT Autograd manually precomputes the view chain off of graph intermediates during tracing, and re-applies them at runtime. This is kind of complicated though and feels lower priority to implement immediately.

(3) Given all of that I made the API private, but lmk what you all think.

This is a followup of https://github.com/pytorch/pytorch/pull/92255.




[ghstack-poisoned]

---
## [Jolly-66/tgstation](https://github.com/Jolly-66/tgstation)@[74144f2bc9...](https://github.com/Jolly-66/tgstation/commit/74144f2bc9e69c9829339a1bd7ffa962e37c0cd0)
#### Thursday 2023-02-09 23:03:00 by LemonInTheDark

Fixes some runtime spam from lazyloading/map templates (#73037)

## About The Pull Request

Ensures we don't try and rebuild loading turfs midload

Turf refs persist through destroy, so when we changeturf earlier to get
our turf reservation, we insert our space turfs into the rebuild queue,
and then end up here where we can be rebuilt randomly, midload, with
uninit'd turfs

Avoids starting atmos machine processing until init

This avoids some runtimes with null gasmixtures

There's still trouble with atmos and template loading, pipes start
processing before their pipelines exist, so we just kinda get fucked.
Need to look into this more deeply, it involves pulling this stuff off
`on_construct` and `setup_template_machinery` and throwing it in maybe
late init, which I don't really relish but will just have to do
eventually.

## Why It's Good For The Game

Reduces runtime spam

---
## [FRC-Team3484/X23_RobotCode](https://github.com/FRC-Team3484/X23_RobotCode)@[b59131dcc2...](https://github.com/FRC-Team3484/X23_RobotCode/commit/b59131dcc2baf9a2b434310e35fe871c2b8d665d)
#### Thursday 2023-02-09 23:35:13 by Programmer1

My Funny alex Friend said to me "You understand where parameters are, not what they do yet. I am beating your brain." he also put in a FPD loop because the I scared him and he likes giving me more work to do. I am afraid of deer, chickens and feeling my ribcage. -p <3

---
## [FRC-Team3484/X23_RobotCode](https://github.com/FRC-Team3484/X23_RobotCode)@[aa04f17b7e...](https://github.com/FRC-Team3484/X23_RobotCode/commit/aa04f17b7e062ad432c7e734a988f5974d27d9cf)
#### Thursday 2023-02-09 23:35:13 by Programmer1

I said a funny joke about ripping a body part off and got banned. We made the second PID Loop, and Bortnite became the favorite mentor of the day. We are now scared of the cv->?->Output thingy but once we suceed we will rule all of FRC. If we fail then arson would be kinda funny but a bad idea.

---

