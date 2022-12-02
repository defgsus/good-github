## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-01](docs/good-messages/2022/2022-12-01.md)


2,326,195 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,326,195 were push events containing 3,519,200 commit messages that amount to 268,443,345 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [sefinek24/sefinek24](https://github.com/sefinek24/sefinek24)@[b8435310a8...](https://github.com/sefinek24/sefinek24/commit/b8435310a87019893aa10899b05e665b25275efb)
#### Thursday 2022-12-01 00:15:27 by Sefinek

    I got really fucking drunk last night. Smoked a bunch of dope til five in the morning.
    Ended up passing out in the sewer pipe cause it's kind of cramped back here and my back's a little sore.
    Anyways, slept there, had a pretty good sleep, but I still had to get up early this morning cause I got responsibles now. Growed up, I got kids.
    A lot of people say you can't smoke dope and get drunk when you have kids but that's not true. You can. But you still gotta get up in the morning. That's being responsible.

---
## [kondatilakshmi/my-java-practice](https://github.com/kondatilakshmi/my-java-practice)@[93a00c2fdd...](https://github.com/kondatilakshmi/my-java-practice/commit/93a00c2fdd27ef5a224b5bf2dd311fb244744f54)
#### Thursday 2022-12-01 00:28:51 by kondatilakshmi

Three idiots

Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality. A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a program to find the midpoint of the line.

---
## [AllyTally/VVVVVV](https://github.com/AllyTally/VVVVVV)@[86d90a1296...](https://github.com/AllyTally/VVVVVV/commit/86d90a1296739adef30b224f41e3a6ab55069a48)
#### Thursday 2022-12-01 00:44:39 by Misa

Add color support to Windows console output, properly

This adds color support to the output of the console on Windows. Now if
you're using Windows 10 build 1511 or later (I think it's build 1511
anyway; they added more VT sequence support in later versions), you will
see colors by default. This isn't due to Windows helping in any way;
this commit has to specifically enable it with SetConsoleMode() because
by default, Windows won't enable color support unless we enable it. (Or
if it's enabled in the registry, but having to go through the registry
to enable basic shit like that is completely fucking stupid.)

I tested this in my Windows 10 virtual machine and it's completely
working.

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[a753229ee2...](https://github.com/lessthnthree/tgstation/commit/a753229ee2541e32164772f05330669d3c6b75d8)
#### Thursday 2022-12-01 01:17:46 by GoldenAlpharex

Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! (#71563)

## About The Pull Request
So, I looked at the Biogenerator code and there was just, _so_ much old
and undocumented code, that I just spazzed out and started documenting
and refactoring everything. There's now a lot less usage of contents
lookups and for loops, and _almost_ everything is documented, now, too.

As for the changes, as you can see in the title, I made biomass
conversion faster. How much faster, you ask? 5 times faster with default
parts, up to 20 times faster with the best parts. It was painfully slow,
and that's not fun for anyone.

I also lifted the biomass cap. It wasn't useful, it wasn't fun, and
Melbert didn't really agree with it either. However, I enjoyed the look
of the biomass going up, so I gave it a max visual amount of 5000, so
you get to see it gradually filling up as you put your first 5000
biomass in. After that, you do you, chief. Watch the funny numbers go up
all you want.

I also improved the maths so that it wasn't just rounding stuff
constantly, and also gave a little bit more insight on how much biomass
everything would cost you, down to two decimals. If there's no decimals,
it won't show them, however.


<details>
<summary>Here's what that looks like now:</summary>
That's one screenshot per different decimal places, there's no trailing
zeros because I think we can all universally agree that those look bad
in this kind of setting.


![image](https://user-images.githubusercontent.com/58045821/204120744-a8c398dc-7c19-4ee0-a8cb-5615f1dce1ea.png)

![image](https://user-images.githubusercontent.com/58045821/204120749-90aae203-bdb8-4322-a657-bb4fd313d808.png)

![image](https://user-images.githubusercontent.com/58045821/204120755-8bed494d-0d70-4b4a-afa2-413610089f6d.png)

</details>

There's now also more information displayed when you examine the biogen,
namely, how many items it has stored, and how many it can hold. I also
fixed the formatting a bit, so it looks ever so slightly cleaner.

Other than that, I just improved the code everywhere I saw it to be
fitting, there shouldn't be any single-letter variables in there
anymore, and the code should be more spaced out. Honestly, at this
point, I wrote most of this code six hours ago so I don't remember all
of it, and I'm too lazy to go through and check what I've changed again.
Diff and changelog are there for that.

## Why It's Good For The Game
So, I'll be honest, there were two big reasons that motivated me to do
this. First of all, the biomass cap. That was a little silly, anyone
that has spent more than one shift in Hydroponics knows that you usually
only put Watermelons in the biomass generator as they're usually the
thing that nets you the most biomass. Botanists will generally stock the
fridges first, and if they have a lot of excess, they'll put it in the
generator if they want, but that's rarely what was done. I've talked
with @MrMelbert about it and he gave me the go-ahead, as can be seen
here:


![image](https://user-images.githubusercontent.com/58045821/204115174-fb2610c0-61c5-44e1-845e-cc6925ee33e6.png)

The other reason was the excruciatingly slow processing speed, which
I've fixed. So we're good now. :)

## Changelog

:cl: GoldenAlpharex
refactor: Went through and refactored a lot of the old code of the
biogenerator, and made multiple improvements to its logic, which should
hopefully make it behave more consistently. Nearly all of it is now also
fully documented, so as to make it easier for anyone else that has to
sift through it in the future.
qol: The biogenerator now processes items five times faster, up to 20
times faster if properly upgraded!
qol: The biogenerator is no longer capped on biomass. Its visuals will
change up until 5000 biomass, but you're free to go as high as you'd
like with it! Sky's the limit!
fix: Fixed the logic of the biogenerator that would make it so the
amount of biomass used for recipes was wildly inconsistent. Now, there's
no more back-end rounding up, it's all on the front end when it needs to
be, so there's no loss or gain of biomass when there shouldn't be.
spellcheck: Fixed a capitalization issue with the seaweed sheets in the
biogenerator recipes.
spellcheck: Fixed multiple inconsistencies between the messages sent to
your chat by the biogenerator.
/:cl:

---
## [Y0SH1M4S73R/tgstation](https://github.com/Y0SH1M4S73R/tgstation)@[25d4afc869...](https://github.com/Y0SH1M4S73R/tgstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Thursday 2022-12-01 01:28:33 by Iamgoofball

Retires explosive lance crafting to a nice farm upstate where it has plenty of room to run around (#71256)

## About The Pull Request

You can no longer craft explosive lances.

## Why It's Good For The Game

Explosive lances are unhealthy for the game in it's current iteration.
Many years ago when the game was more loose and we weren't dealing with
players who treat the game like competitive TTT or Town of Salem,

They are a one shot kill weapon, which is the most powerful kind of
weapon in every gamemode. @JohnFulpWillard likened it to 1f1, a concept
from Town of Salem players where the town trades 1 person for 1 bad guy.

Modern ss13 design includes a significantly heavier load of antagonists
that aren't fixed roundstart compared to when the e-lance went in.

When we added the e-lance, if nuke ops spawned, that was it, there was
nuke ops, if you e-lanced the nuke ops and died you were dead until the
next round.

Nowadays you're rolling for lone operative, blob, wizard, disease,
revenant, and every other fun enjoyable antagonist role under the sun.

I can e-lance a nuke op/cultist/traitor/revolutionary/any bad guy in the
game as a non-antag assistant, die, and have a good chance to roll
another, way more fun antag in deadchat.

My change to make the e-lance a proper "we both die" tool didn't
actually help because I didn't quite realize that to the modern SS13
player because of how we designed Dynamic and antagonists in the modern
era, death is, frankly, not a punishment anymore.

It's time we admit the facts, items designed in 2015 SS13 in #12389
simply don't hold up in a healthy manner in 2022 SS13. Dying in SS13 in
2015 was a significantly different experience with different
consequences than it has now, and right now "kills you when you use it"
is not the same massive downside it was 7-8 years ago.

## Changelog
:cl:
del: You can no longer craft explosive lances.
/:cl:

---
## [stepleton/flag](https://github.com/stepleton/flag)@[74d8765b65...](https://github.com/stepleton/flag/commit/74d8765b65b0bb7227b267ee49a9bbf7f616a4ea)
#### Thursday 2022-12-01 01:57:29 by Tom Stepleton

Small wording change

Word choice is difficult, so let this commit message be a footnote.
I'm thankful for the trans people in my life and I'm glad they're around.

It's hard to say "I'm happy you're here" in a way that doesn't seem
patronising, and I'm honestly not certain that this message is helpful.
I've guessed that it might be for a few reasons.

This change aims to revise away some more patronising interpretations of
what I'm trying to say here, at any rate.

---
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[b77cf7c120...](https://github.com/TheBoondock/tgstation/commit/b77cf7c1205d466b8cb242cd3302891e82b44da2)
#### Thursday 2022-12-01 02:05:28 by Iamgoofball

Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios. (#71325)


About The Pull Request

Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios.
Why It's Good For The Game

Players have been deploying unbelievable levels of abuse with these hotkeys having completely uncapped speeds.
I watched one cheater do automated inventory management using storage items and weirdly named empty pills to use as inventory delimiters.
Resolves people being able to have a baton hidden in their backpack and then activate and baton someone with it in 0.1 seconds without moving their mouse cursor off of their target.

Players should not be able to interact with their inventory faster than someone moving a mouse and clicking the left mouse button. This cripples the game balance and puts anyone with a worse internet connection, slower reaction speeds, or laggier computer at a distinct disadvantage against people who can macro their inventory management.

I can set up autohotkey so that I can withdraw a stun baton from my backpack, turn it on, and then click someone by just holding down a key and pressing M1 over someone. This shit needs to stop.

If a do_after() on hotkey management is too harsh, we can apply a combat click cooldown every time you use the hotkeys instead to discourage combat macro abuse.
Swapped it over to a click cooldown.
Changelog

cl
balance: Hotkey-based inventory management now applies the click cooldown to prevent it from being abusable in combat scenarios.
/cl

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[03bc97ade5...](https://github.com/necromanceranne/tgstation/commit/03bc97ade5a76f156229b946e38816ced97a0e30)
#### Thursday 2022-12-01 02:36:23 by necromanceranne

Nukies Update 6: Interdyne is here for you! Medical Supplies and Atropine! (#71067)

## About The Pull Request

Quite a few changes overall to the nuclear operatives tactical medkit.
The kit is more of a full suite of equipment for performing field
medical duties as a nukie.

- I've split the medkits between two kinds. Basic and premium. Medical
bundle has the premium kit.
- Basic contains additional amounts of basic c2 chem patches, some spare
atropine autoinjectors, sutures and regen mesh, and some basic medical
equipment for tending wounds. 4 TC (as it was before). That's it.
- The premium kit is a far more useful full suite of advanced medical
equipment, MODsuit modules, medical supplies and cybernetic implants,
including the combat hypospray and the combat defib. 15 TC.

**In the premium kit, there is:**
- It has a box of beakers with powerful healing chems. Omnizine,
salicylic acid, oxandrolone, pentetic acid, atropine, salbutamol and
rezadone.
- The combat injector is empty, so you can load it as necessary.
- There are advanced sutures and regenerative mesh packs. They don't
work through spacesuits, but are invaluable for wound repair. Especially
burns.
- There is a surgery arm toolset so you can do field operations without
lugging tools.
- There is a surgery processor module that comes preloaded with advanced
surgeries, a threadripper module, and the combat defib module. The
module works entirely like a combat defib, but you don't need to lose
your belt slot to use it.
- The surgeries are revival, the upgrade surgeries (like vein
threading), brainwashing (did you know they didn't get access to
brainwashing, I think this is a shame) and the better tend wounds
option.
- The nightvision medical hud doubles as a pair of science goggles.

**Atropine changes:**
- Atropine now stops bomb implants from autoexploding. This does **NOT**
stop you from manually detonating the bomb. (This is possible even when
you're dead and haven't left your body)
- As a result, nukies get atropine medipens so that they can potentially
stop themselves detonating prematurely, or stop their allies detonating
prematurely. They have a little pamphlet to help explain how their
microbomb works.

## Why It's Good For The Game

Straight up: The medkit is ass.

The meds in the injector sucks, just getting c2 meds in patches is kind
of insulting for something granted to you from an uplink item (and also
you get those for free with your ~~xbox~~ infiltrator medical room so
lol), and operatives just got the kit for one reason and one reason
only. That combat defib as a _weapon_.

Fuck that. So the kits now much better as a way to both support yourself
AND your team through providing a range of improvements you can provide
the squad, while also not undermining the reason why people may have
wanted the kit (that defib). I would really like to see more nukies
attempt to support one another in combat, and a medic operative is a
role that needs love to make that a reality.

**Edit here**: I reintroduced a low end kit with more c2 medical
supplies _if you want them_. I can see how someone might pinch all of
the medical supplies like a cunt, so maybe we should have a failsafe for
that.

A huge culprit of the lack of value of support meds was usually that
ops...explode when they die. If a medic can pop atropine into an op
before they die, they might be able to save them, or an op could pop
themselves with atropine prematurely to maybe stave off death.

## Changelog
:cl:
balance: Splits the nuclear operative combat medical kit into two
versions: basic and premium.
balance: Basic contains additional amounts of basic c2 chem patches,
some spare atropine autoinjectors, sutures and regen mesh, and some
basic medical equipment for tending wounds. 4 TC (as it was before).
balance: The premium kit is a far more useful full suite of advanced
medical equipment, MODsuit modules, medical supplies and cybernetic
implants, including the combat hypospray and the combat defib. 15 TC.
balance: Atropine stops bomb implants from automatically detonating on
death. You can still manually activate your bomb implant (even when you
are dead).
balance: Operatives start with an atropine pen to stop themselves and
their allies from detonating so they can hopefully be saved by a medical
operative.
add: There is a pamphlet to explain this in the nuclear operative's
survival box.
add: I'm not telling you to read the pamphlet, but you should probably
read the pamphlet.
/:cl:

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[a811adac74...](https://github.com/necromanceranne/tgstation/commit/a811adac74513494a620fae631da95d2626b1be7)
#### Thursday 2022-12-01 02:36:23 by Epic

Changes Admin Prison to be Anti-Telekinesis: Walls off equipment rooms, replaces computers, and makes the tables tidy (#71433)

First PR, may require some changes or something because I don't know how
to do anything bleh
## About The Pull Request

We already had issues with crewmembers with telekinesis making changes
to the security records (purging them and what not). And, nothing has
been done about it, not yet, anyway. Not only record computers are a
problem as well.


![image](https://user-images.githubusercontent.com/106710384/203241399-8314bcba-d2d0-44af-9360-30ff58dbc39e.png)
Previously, prisoners can access the sec vendor with telepathy, and,
since the vendor is free, spam the vendor and be an annoyance. Sure, I
believe that it is not as big of a problem as purging the security
records, but I feel like it's against what the prison is supposed to
stand for; It's supposed to stop them and get them to listen to ahelps
thrown at them.

I've decided to make a bit of changes to the prison to make it so that
people with telekinesis won't fuck up things as much. This replaces real
computers with nonfunctional ones, adding walls to equipment areas to
make sure prisoners don't spam the vendor, and deletes guns/weapons from
the tables so they won't grab them.

## Why It's Good For The Game


![image](https://user-images.githubusercontent.com/106710384/203241465-833f79da-58a3-4feb-87b0-091fbb846e93.png)
This PR is more tailored to admins dealing with no-good-doers, and goes
for the vibe of "HEY, SOMEONE IS PMING YOU, REPLY TO THEM INSTEAD!" Of
course, this leads to prisoners not interacting with the current round,
and, less chance of them going insane and breaking all the windows with
a telekinesis auto-rifle.

Plus, this can always be reverted in-case someone comes up with coding
stuff in instead. I'm all through with that and willing to work with
whoever to solve the issue.

Also, of course, Closes #60967

## Changelog

:cl:
admin: Nanotrashen made some top-of-the-line changes to their
top-of-the-line prison by walling off their equipment area and removing
some spare guns they somehow left on the tables. We also stole the
security computers, so people with telekinesis can't access them.
/:cl:

---
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[c185dffda0...](https://github.com/necromanceranne/tgstation/commit/c185dffda0cc30d8187fa1ba37e5784b8d630ba4)
#### Thursday 2022-12-01 02:36:23 by Jacquerel

Basic Mob Carp Bonus Part: Wall smashing (#71524)

## About The Pull Request

Atomisation of #71421 
This moves the attack function of "environment smash" flags which allow
simple mobs to attack walls into an element, so that we can put it on
other things later.
For some reason while working on carp I convinced myself that they had
"environment_smash" flags, which they do not, so this actually is not
relevant to carp in any way.

While implementing this I learned that the way wall smashing works is
stupid, because walls don't have health and so resultingly if a mob can
attack walls it deletes them in a single click. If we ever decide to
change this then it should be easier in an element than in three
different `attack_animal` reactions.
This is especially silly with the "wumborian fugu" item which allows any
mob it is used on to instantly delete reinforced walls, and also to
destroy tables if they click them like seven or eight times (because it
does not increase their object damage in any way).

## Why It's Good For The Game

Eventually someone will port a basic mob which does use this behaviour
(most of the mining ones for instance) and then this will be useful.
If we ever rebalance wall smashing to not instantly delete walls then
this will also be useful.
Admins can apply this to a mob to allow it to delete walls if they
wanted to do that for some reason, they probably shouldn't to be honest
at least until after we've done point two unless they trust the player
not to just use it to deconstruct the space station.

## Changelog
:cl:
refactor: Moves wall smashing out of simple mob code and into an element
we can reuse for basic mobs later
/:cl:

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[cf4a194e86...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/cf4a194e86d53d57397f6de4febbea0de9c6ef57)
#### Thursday 2022-12-01 02:42:57 by SkyratBot

[MIRROR] Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! [MDB IGNORE] (#17828)

* Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap! (#71563)

## About The Pull Request
So, I looked at the Biogenerator code and there was just, _so_ much old
and undocumented code, that I just spazzed out and started documenting
and refactoring everything. There's now a lot less usage of contents
lookups and for loops, and _almost_ everything is documented, now, too.

As for the changes, as you can see in the title, I made biomass
conversion faster. How much faster, you ask? 5 times faster with default
parts, up to 20 times faster with the best parts. It was painfully slow,
and that's not fun for anyone.

I also lifted the biomass cap. It wasn't useful, it wasn't fun, and
Melbert didn't really agree with it either. However, I enjoyed the look
of the biomass going up, so I gave it a max visual amount of 5000, so
you get to see it gradually filling up as you put your first 5000
biomass in. After that, you do you, chief. Watch the funny numbers go up
all you want.

I also improved the maths so that it wasn't just rounding stuff
constantly, and also gave a little bit more insight on how much biomass
everything would cost you, down to two decimals. If there's no decimals,
it won't show them, however.

<details>
<summary>Here's what that looks like now:</summary>
That's one screenshot per different decimal places, there's no trailing
zeros because I think we can all universally agree that those look bad
in this kind of setting.

![image](https://user-images.githubusercontent.com/58045821/204120744-a8c398dc-7c19-4ee0-a8cb-5615f1dce1ea.png)

![image](https://user-images.githubusercontent.com/58045821/204120749-90aae203-bdb8-4322-a657-bb4fd313d808.png)

![image](https://user-images.githubusercontent.com/58045821/204120755-8bed494d-0d70-4b4a-afa2-413610089f6d.png)

</details>

There's now also more information displayed when you examine the biogen,
namely, how many items it has stored, and how many it can hold. I also
fixed the formatting a bit, so it looks ever so slightly cleaner.

Other than that, I just improved the code everywhere I saw it to be
fitting, there shouldn't be any single-letter variables in there
anymore, and the code should be more spaced out. Honestly, at this
point, I wrote most of this code six hours ago so I don't remember all
of it, and I'm too lazy to go through and check what I've changed again.
Diff and changelog are there for that.

## Why It's Good For The Game
So, I'll be honest, there were two big reasons that motivated me to do
this. First of all, the biomass cap. That was a little silly, anyone
that has spent more than one shift in Hydroponics knows that you usually
only put Watermelons in the biomass generator as they're usually the
thing that nets you the most biomass. Botanists will generally stock the
fridges first, and if they have a lot of excess, they'll put it in the
generator if they want, but that's rarely what was done. I've talked
with @ MrMelbert about it and he gave me the go-ahead, as can be seen
here:

![image](https://user-images.githubusercontent.com/58045821/204115174-fb2610c0-61c5-44e1-845e-cc6925ee33e6.png)

The other reason was the excruciatingly slow processing speed, which
I've fixed. So we're good now. :)

## Changelog

:cl: GoldenAlpharex
refactor: Went through and refactored a lot of the old code of the
biogenerator, and made multiple improvements to its logic, which should
hopefully make it behave more consistently. Nearly all of it is now also
fully documented, so as to make it easier for anyone else that has to
sift through it in the future.
qol: The biogenerator now processes items five times faster, up to 20
times faster if properly upgraded!
qol: The biogenerator is no longer capped on biomass. Its visuals will
change up until 5000 biomass, but you're free to go as high as you'd
like with it! Sky's the limit!
fix: Fixed the logic of the biogenerator that would make it so the
amount of biomass used for recipes was wildly inconsistent. Now, there's
no more back-end rounding up, it's all on the front end when it needs to
be, so there's no loss or gain of biomass when there shouldn't be.
spellcheck: Fixed a capitalization issue with the seaweed sheets in the
biogenerator recipes.
spellcheck: Fixed multiple inconsistencies between the messages sent to
your chat by the biogenerator.
/:cl:

* Biogen Refactor and Code Cleanup, Faster Biomass Conversion and No More Biomass Cap!

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [cheungglenda/comp1170-project2](https://github.com/cheungglenda/comp1170-project2)@[843b2ba00b...](https://github.com/cheungglenda/comp1170-project2/commit/843b2ba00b67e63cabfc8d5d70a0c94e14436a75)
#### Thursday 2022-12-01 02:50:18 by justinweiyungwu

Merge pull request #14 from cheungglenda/justin

holy fucking shit

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[edf8dd9b22...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/edf8dd9b226b23f80ce77ed5630b812b4de6e793)
#### Thursday 2022-12-01 03:33:47 by SkyratBot

[MIRROR] Create a guide for atomization that includes a new allowance to pull requests that might add dead code [MDB IGNORE] (#17839)

* Create a guide for atomization that includes a new allowance to pull requests that might add dead code (#71429)

@ tgstation/commit-access

I'm proposing a new use for the Atomic tag that we currently virtually
never use.

We have countless pull requests over time, and plenty of which open now,
that are enormous refactors over tens of files with thousands of
additions. We are historically pretty slow to review and merge these,
and it definitely scares a lot of maintainers off. I think part of the
reason is that we do not like dead code being added, which is completely
reasonable at our scale.

However, I propose that, for refactors/purely code stuff, we ease up on
this a lot, and encourage (not require) people to make smaller pull
requests, even to the extent that it creates APIs we do not use yet.

As an example, https://github.com/tgstation/tgstation/pull/71421 does a
massive refactor to carp. It also does some balance changes, which I
think we could agree could be split off if it was enough of a pain.
However, there's a bunch of other stuff that could have been individual
pull requests here with this new allowance.

- The new basic AI behaviors
- The regenerator component
- Pet commands component

These are things that:

- Would not be used until the transition from simple to basic, but are
easily reviewable on their own
- Are easy to REMOVE if the OP does not follow up
- Are easy to FINISH if the OP does not follow up

(I suspect even, for instance, that there are parts of Wallening we
could be merging right now, that's probably gonna be hundreds or
thousands of files long...)

Pros:
- PRs are more often easily reviewable
- PRs are quicker to merge, since we don't have conflicts from editing
one of the 70 files they changed
- Cleanups can be more easily finished by other people. I don't suspect
this will be likely, but it's not easily possible today

Cons:
- We have to mark the PRs as atomic
- Someone needs to look through every so often (I'm thinking like, once
a month or something) to see if the code ended up being used, or if the
committer still plans to use it
- If the PR is adding a complex enough API that isn't modular, it might
be very hard to remove. I suspect for PRs like this that we ask them to
have an implementer before merging.

NL voice would love your thoughts on this

* Create a guide for atomization that includes a new allowance to pull requests that might add dead code

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [newstools/2022-national-daily-nigeria](https://github.com/newstools/2022-national-daily-nigeria)@[cbbdea8df6...](https://github.com/newstools/2022-national-daily-nigeria/commit/cbbdea8df609d7c9e1b20034c18a6d976750820c)
#### Thursday 2022-12-01 03:49:40 by Billy Einkamerer

Created Text For URL [nationaldailyng.com/yahoo-boy-arrested-for-beating-his-girlfriend-to-death-for-refusing-to-relinquish-the-money-his-client-paid-into-her-account/]

---
## [zhengkaiyuan1993/dotnet-runtime](https://github.com/zhengkaiyuan1993/dotnet-runtime)@[1412ee7643...](https://github.com/zhengkaiyuan1993/dotnet-runtime/commit/1412ee76430e8c2d4319e418ab46bfb1af5b839f)
#### Thursday 2022-12-01 04:00:20 by Vitek Karas

Enable basic Kept validation in NativeAOT running linker tests (#78828)

This implements basic Type and Method Kept attribute validation.
It adds a `KeptBy` property on all `KeptAttribute` which uses the same `ProducedBy` enum to specify exceptions for each target product. (Eventually after the source merge we should rename `ProducedBy` enum to just `Tool` or `Platform`, but it's not important and I didn't want to do it here as it would be a giant diff).

The validation is done by going over all `ConstructedEETypeNode` and `IMethodBodyNode` nodes in the final graph and remembers that list. Then it compares that list to the expected kept members as per the attributes in tests. There are some tweaks:
* Filters out all compiler added types/members
* Doesn't track generic instantiations - only remember definition
* If a method body is kept, then it behaves as if the type is also kept even though there's no `ConstructedEETypeNode` - this is technically wrong (since NativeAOT can remove the type if for example only static methods are used from it), but it would require major changes to the linker tests (since in IL this is a necessity). If we ever need precise validation of this, we would probably add a new attribute to check just for this.

I also copied all of the "other assemblies" kept validation code from ResultChecker (were it lives in linker) to AssemblyChecker where it will need to be to actually work (and where it should probably be anyway). That code is not used yet.

Left lot of TODO/commented out code in the AssemblyChecker - lots of other validation to enable eventually.

Fixed/adapted all of the tests which were already ported to NativeAOT to pass with this new validation.
Removed a test for unresolved members, since it actually fails NativeAOT compilation, so it doesn't test anything really.

One tiny product change:
Display names now consistently include all parent types when writing out nested type names. ILLink already does this and NativeAOT was a bit inconsistent. Since the display names are used only in diagnostics, this brings the diagnostics experience closer between the two tools. The added benefit is that we can use display names to compare members between Cecil and Internal.TypeSystem more precisely.

Co-authored-by: Tlakaelel Axayakatl Ceja <tlakaelel.ceja@microsoft.com>

---
## [cheegatikrishna/JAVA-PROGRAMS](https://github.com/cheegatikrishna/JAVA-PROGRAMS)@[29f6f50809...](https://github.com/cheegatikrishna/JAVA-PROGRAMS/commit/29f6f50809e255f6868a4f2b118e7817d8210212)
#### Thursday 2022-12-01 04:25:25 by cheegatikrishna

Team Flash

A young man named Diffny leaves home to travel to California, to join the Team Flash. Although Diffny is not able to join this elite team immediately, he befriends the three most formidable members of the age: Joe, Ramsey and vixon and gets involved in affairs of the state and court.At that time, the Villan was planning to dethrone the king and to take the kingdom and to remove the Team Flash of the guard. Since the Villan has spies mixed with the local public , Diffny decides to send a message of his whereabouts to the team Flash in unique way.He gave a note to a boy which has the following message. I am at the midpoint of the line joining the farmhouse next to the palace and the light house. The Team Flash were puzzled. Can you help them find out the location of Diffny?Given the coordinates of the 2 places (x1,y1) and (x2,y2), write a program to find the location of Diffny.

---
## [chandanagindi/programs](https://github.com/chandanagindi/programs)@[1f112a64c9...](https://github.com/chandanagindi/programs/commit/1f112a64c98f7b0f4e65c3936bee015946781a79)
#### Thursday 2022-12-01 04:27:24 by chandanagindi

Create The Chronicles of Narnia

Four kids Peter,Susan,Edmond and Lucy travel through a wardrobe to the land of Narnia. Narnia is a fantasy world of magic with mythical beasts and talking animals.While exploring the land of narnia Lucy found Mr.Tumnus the two legged stag ,and she followed it, down a narrow path .She and Mr.Tumnus became friends and he offered a cup of coffee to Lucy in his small hut.It was time for Lucy to return to her family and so she bid good bye to Mr.Tumnus and while leaving Mr.Tumnus told that it is quite difficult to find the route back as it was already dark.He told her to see the trees while returning back and said that the first tree with two digits number will help her find the way and the way to go back to her home is the sum of digits of the tree and that numbered way will lead her to the tree next to the wardrobe where she can find the others.Lucy was already confused, so pls help her in finding the route to her home....

---
## [RobertasJ/skylore](https://github.com/RobertasJ/skylore)@[e2730e802d...](https://github.com/RobertasJ/skylore/commit/e2730e802d039107e76e658dcdff0ba328216dd7)
#### Thursday 2022-12-01 05:06:25 by Monster Zero

I hate my life, why is artis not working?

updates, hopefully they don't break anything

---
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[fabf9d669d...](https://github.com/rust-lang-ci/rust/commit/fabf9d669d8708f8b2b4fd8ea76aa78c39348c58)
#### Thursday 2022-12-01 05:56:28 by bors

Auto merge of #105114 - saethlin:mir-opt-ub-asserts, r=<try>

Tweak MIR inline cost estimation and assert_unsafe_precondition so they inline in MIR

It turns out that https://github.com/rust-lang/rust/pull/104121 does not actually achieve what `@Lokathor` wanted, when debug assertions are enabled. In my opinion there are really multiple issues here, this PR addresses all of them:

The implementation of `is_aligned_and_not_null` is compiled to a shocking amount of MIR, because the implementation of `ptr::is_null` is contorted to work in `const fn`, and the implementation of `ptr::is_aligned` is based on `ptr::is_aligned_to` which among other things has a check that the alignment is a power of 2. These of course clean up quite nicely in LLVM... but the goal here is to enable inlining _before_ we get to LLVM.

Then some of the helper functions aren't `#[inline]`. The MIR inliner only inlines `#[inline]` functions at `-Zmir-opt-level=2`, which is what `--release` corresponds to. Whether or not that heuristic should be loosened up, these are good candidates for inlining so I don't see any harm in adding the attribute.

Then the MIR inlining cost estimation seems a bit pessimistic to me. The MIR we generate tends to have a lot of assignments from locals to locals. By eye it looks like a lot of these could be erased by another optimization pass, so I don't think they represent nearly the complexity of any other instruction. For now, this excludes them from cost estimation entirely.

I also removed the extra function call penalty from diverging call terminators. My logic there is that a diverging terminator is often a panic path, and those sometimes (and especially in this case) have a predicate which can be statically reasoned about. There is a fair chance that inlining a function with a diverging terminator will result in optimizing away the divergence entirely, or making other optimizations after the diverging path, based on assume its predicate. (I'm aware that currently MIR opt is not very good at this sort of cleanup, so this is somewhat of a gamble)

(I hope this looks good in perf...)

r? `@cjgillot`
cc `@JakobDegen`

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[0ca2c0b527...](https://github.com/Zergspower/Skyrat-tg/commit/0ca2c0b527a564de32818057b7fc09eb07875f51)
#### Thursday 2022-12-01 07:34:02 by SkyratBot

[MIRROR] Gives bread and cake slice_types and adds screentip verbs to proccessed foods [MDB IGNORE] (#17721)

* Gives bread and cake slice_types and adds screentip verbs to proccessed foods (#71449)

## About The Pull Request

A side effect of my pizza PR #71202 I added contextual screentips as
part of processable.dm. In doing this, I noticed that with a few
exceptions, almost every single bread and cake type copies the proc
exactly the same for every single child of cake or bread, so I put the
proc on the parent of bread and cake and gave them slice_types, making
them more similar to pizza.dm

For everything else I've changed the default that I put in
processable.dm into "slice" or "cut" for things that use the knife and
"flatten" for things that use the rolling pin.

Finally, you can slice bread with saws now, because I think its silly
that only pizza gets this luxury.

## Why It's Good For The Game

Because it wasnt the focus of #71202 I didn't mess with screentips
outside of the pizza file a lot, but now that it's merged I figure I
should go and do that.
As Bread and Cake's processables are almost fully standardized it seems
silly for them to call on the proc 12 times in the same document so I
did this, which also allows for more versatility in editing how they
work as well allow people to, if they want to, add more tool behaviours
in the future without adding in 12 lines of code. Also means that people
who want to add new cake or bread have one less thing to do.

## Changelog

:cl:
add: you can saw bread with a saw into bread slices
qol: added screentip verbs to a bunch of food files
code: bread and cake now have slice types and all only have one call on
the processable.dm proc
/:cl:

* Gives bread and cake slice_types and adds screentip verbs to proccessed foods

* sco'ish

* fuck me ig

Co-authored-by: Sol N <116288367+flowercuco@users.noreply.github.com>
Co-authored-by: John Doe <gamingskeleton3@gmail.com>

---
## [Anilkumar-Hasanapuram/java-basics](https://github.com/Anilkumar-Hasanapuram/java-basics)@[5ba4d11749...](https://github.com/Anilkumar-Hasanapuram/java-basics/commit/5ba4d117497628b1d9358338b0be5d3c5362d367)
#### Thursday 2022-12-01 08:52:59 by Anil kumar

sid

Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

"I love you"
"a little"
"a lot"
"passionately"
"madly"
"not at all"
If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.

When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this question is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.

INPUT 1:
1
OUTPUT  1:
I love you
INPUT 2:
3
OUTPUT 2:
a lot

---
## [avar/git](https://github.com/avar/git)@[f1c903debd...](https://github.com/avar/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Thursday 2022-12-01 08:56:59 by Ævar Arnfjörð Bjarmason

cocci: make "coccicheck" rule incremental

Optimize the very slow "coccicheck" target to take advantage of
incremental rebuilding, and fix outstanding dependency problems with
the existing rule.

The rule is now faster both on the initial run as we can make better
use of GNU make's parallelism than the old ad-hoc combination of
make's parallelism combined with $(SPATCH_BATCH_SIZE) and/or the
"--jobs" argument to "spatch(1)".

It also makes us *much* faster when incrementally building, it's now
viable to "make coccicheck" as topic branches are merged down.

The rule didn't use FORCE (or its equivalents) before, so a:

	make coccicheck
	make coccicheck

Would report nothing to do on the second iteration. But all of our
patch output depended on all $(COCCI_SOURCES) files, therefore e.g.:

    make -W grep.c coccicheck

Would do a full re-run, i.e. a a change in a single file would force
us to do a full re-run.

The reason for this (not the initial rationale, but my analysis) is:

* Since we create a single "*.cocci.patch+" we don't know where to
  pick up where we left off, or how to incrementally merge e.g. a
  "grep.c" change with an existing *.cocci.patch.

* We've been carrying forward the dependency on the *.c files since
  63f0a758a06 (add coccicheck make target, 2016-09-15) the rule was
  initially added as a sort of poor man's dependency discovery.

  As we don't include other *.c files depending on other *.c files
  has always been broken, as could be trivially demonstrated
  e.g. with:

       make coccicheck
       make -W strbuf.h coccicheck

  However, depending on the corresponding *.c files has been doing
  something, namely that *if* an API change modified both *.c and *.h
  files we'd catch the change to the *.h we care about via the *.c
  being changed.

  For API changes that happened only via *.h files we'd do the wrong
  thing before this change, but e.g. for function additions (not
  "static inline" ones) catch the *.h change by proxy.

Now we'll instead:

 * Create a <RULE>/<FILE> pair in the .build directory, E.g. for
   swap.cocci and grep.c we'll create
   .build/contrib/coccinelle/swap.cocci.patch/grep.c.

   That file is the diff we'll apply for that <RULE>-<FILE>
   combination, if there's no changes to me made (the common case)
   it'll be an empty file.

 * Our generated *.patch
   file (e.g. contrib/coccinelle/swap.cocci.patch) is now a simple "cat
   $^" of all of all of the <RULE>/<FILE> files for a given <RULE>.

   In the case discussed above of "grep.c" being changed we'll do the
   full "cat" every time, so they resulting *.cocci.patch will always
   be correct and up-to-date, even if it's "incrementally updated".

   See 1cc0425a27c (Makefile: have "make pot" not "reset --hard",
   2022-05-26) for another recent rule that used that technique.

As before we'll:

 * End up generating a contrib/coccinelle/swap.cocci.patch, if we
   "fail" by creating a non-empty patch we'll still exit with a zero
   exit code.

   Arguably we should move to a more Makefile-native way of doing
   this, i.e. fail early, and if we want all of the "failed" changes
   we can use "make -k", but as the current
   "ci/run-static-analysis.sh" expects us to behave this way let's
   keep the existing behavior of exhaustively discovering all cocci
   changes, and only failing if spatch itself errors out.

Further implementation details & notes:

 * Before this change running "make coccicheck" would by default end
   up pegging just one CPU at the very end for a while, usually as
   we'd finish whichever *.cocci rule was the most expensive.

   This could be mitigated by combining "make -jN" with
   SPATCH_BATCH_SIZE, see 960154b9c17 (coccicheck: optionally batch
   spatch invocations, 2019-05-06).

   There will be cases where getting rid of "SPATCH_BATCH_SIZE" makes
   things worse, but a from-scratch "make coccicheck" with the default
   of SPATCH_BATCH_SIZE=1 (and tweaking it doesn't make a difference)
   is faster (~3m36s v.s. ~3m56s) with this approach, as we can feed
   the CPU more work in a less staggered way.

 * Getting rid of "SPATCH_BATCH_SIZE" particularly helps in cases
   where the default of 1 yields parallelism under "make coccicheck",
   but then running e.g.:

       make -W contrib/coccinelle/swap.cocci coccicheck

   I.e. before that would use only one CPU core, until the user
   remembered to adjust "SPATCH_BATCH_SIZE" differently than the
   setting that makes sense when doing a non-incremental run of "make
   coccicheck".

 * Before the "make coccicheck" rule would have to clean
   "contrib/coccinelle/*.cocci.patch*", since we'd create "*+" and
   "*.log" files there. Now those are created in
   .build/contrib/coccinelle/, which is covered by the "cocciclean" rule
   already.

Outstanding issues & future work:

 * We could get rid of "--all-includes" in favor of manually
   specifying a list of includes to give to "spatch(1)".

   As noted upthread of [1] a naïve removal of "--all-includes" will
   result in broken *.cocci patches, but if we know the exhaustive
   list of includes via COMPUTE_HEADER_DEPENDENCIES we don't need to
   re-scan for them, we could grab the headers to include from the
   .depend.d/<file>.o.d and supply them with the "--include" option to
   spatch(1).q

1. https://lore.kernel.org/git/87ft18tcog.fsf@evledraar.gmail.com/

Signed-off-by: Ævar Arnfjörð Bjarmason <avarab@gmail.com>
Signed-off-by: Taylor Blau <me@ttaylorr.com>

---
## [GTcreyon/SM63Redux](https://github.com/GTcreyon/SM63Redux)@[7d6f940863...](https://github.com/GTcreyon/SM63Redux/commit/7d6f9408634581a745ed5378cf7d99bd61471be9)
#### Thursday 2022-12-01 09:01:26 by Koopa1018

Only accept standstill jumps

Annoying if you're passing by and you jump and accidentally get sucked into the painting.

---
## [emillon/dune](https://github.com/emillon/dune)@[bcfc2425fa...](https://github.com/emillon/dune/commit/bcfc2425faf0d3927d1b2c569a7e6da6f5f95d42)
#### Thursday 2022-12-01 09:21:39 by Etienne Millon

Add shell completion

This provides a shell completion mechanism for dune. This relies on the
bash completion API, which can be used with zsh as well.

The architecture is:

- `dune complete script` outputs a script to be sourced in the user's
  shell. It is comprised of a `_dune` function and the `complete -F
  _dune dune` command to register it. The `_dune` function can be used
  in cram tests to write natural-looking tests for this feature.
- this script calls `dune complete command` with the partial
  command-line. This internal command parses it to determine what the
  word being completed refers to: a command name, an argument name, or
  an argument value. The first two ones are part of the metadata
  `cmdliner` knows about; the last one is provided through a completion
  function that can be passed in one the `Arg` functions.
- the interface between `bash` and `dune complete command` is simple:
  it passes the command line and a position to complete at (this is
  necessary to encode the difference between `dune bui<tab>` and `dune
  build <tab>` for example), and reads an array from the output of the
  command.

The things I'm happy with:

- it is small!
- coverage is pretty good: command names, arguments (positional and
  optional, including optional arguments with optional names), and the
  `--` construct are supported. So, this is likely to improve the user
  experience already.
- it is easy to test through cram or unit tests (I chose the former).

Now, for the ugly bits...

- this effectively is a partial reimplementation of cmdliner inside
  `complete.ml`. If the exact parsing rules are different, it means that
  we can complete to something with different or wrong semantics.
- the vendored copy of cmdliner is patched to expose so that it is
  possible to use the private APIs. these two points need to be resolved
  before we can think about how to upstream this.
- some bits of the cmdliner API need to be modified to provide
  completion automatically. For example for things like `enum` it's easy
  to provide a completion function automatically.
- it is difficult to define the right API for the completion functions.
  `unit -> string list` is a first approximation but with some
  limitations. For example, getting a list of buildable targets needs to
  run under `Fiber`, but we can't pollute the API with it. Interestingly
  enough, algebraic effects seem like they would be an interesting
  solution for this.
- at the moment, we're not relying on the shell's completion helpers to
  complete things like filenames. To support this we would either need
  to implement that in OCaml, or extend the bash/dune interface so that
  the completion function could call `compgen -f` based on the dune
  output.
- as a way to tie the two previous points: if we wanted to complete
  `dune build dir/file<tab>`, it would be a lot more efficient to pass
  the prefix to the build system and let it compute just the targets
  that match this, rather than compute everything and filter it
  afterwards. So that prefix would need to appear in the completion API.

Signed-off-by: Etienne Millon <me@emillon.org>

---
## [wildaip/app-dev](https://github.com/wildaip/app-dev)@[faa82d3b20...](https://github.com/wildaip/app-dev/commit/faa82d3b20306344d0b86ce6f605645b31365f95)
#### Thursday 2022-12-01 09:40:31 by wildaip

Update README.md

Legendary assassin John Wick (Keanu Reeves) retired from his violent career after marrying the love of his life. Her sudden death leaves John in deep mourning. When sadistic mobster Iosef Tarasov (Alfie Allen) and his thugs steal John's prized car and kill the puppy that was a last gift from his wife, John unleashes the remorseless killing machine within and seeks vengeance

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[37b60d187d...](https://github.com/AnywayFarus/Skyrat-tg/commit/37b60d187daa6b8c8f2c2623dbf49555774a90aa)
#### Thursday 2022-12-01 10:38:39 by SkyratBot

[MIRROR] Fixes attempting to offset floating planes [MDB IGNORE] (#17745)

* Fixes attempting to offset floating planes (#71490)

## About The Pull Request

This is a dumb idea, and leads to fucked rendering on occasion

## Why It's Good For The Game

Fixes another portion of #70258, a player will no longer have a hidden
antag hud if they move down a z level after getting an antag. We were
trying to offset the floating plane of their image, and it went to shit.
Also fixes a bug with observers not having antag huds for the combo hud
to see. We were only giving them one on mind.on_transfer, rather then on
mind assignment. I hate mindcode

* Fixes attempting to offset floating planes

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [AnywayFarus/Skyrat-tg](https://github.com/AnywayFarus/Skyrat-tg)@[ea1e6ff95f...](https://github.com/AnywayFarus/Skyrat-tg/commit/ea1e6ff95fb48e198162f2bb99448777bc7f9e06)
#### Thursday 2022-12-01 10:42:19 by SkyratBot

[MIRROR] Adds a preference that disables intensive rendering on different multiz layers [MDB IGNORE] (#17737)

* Adds a preference that disables intensive rendering on different multiz layers (#71218)

## About The Pull Request

It's kinda hacky, but it is nearly the same as just rendering one z
layer.
We allow people to ENTIRELY REMOVE most plane masters from their screen.
This has the side effect of disabling most visual effects (AO is a big
one) which saves a LOT of gpu.

We rely on planes being essentially layers to ensure things render in
the proper order. (outside of some hackyness required to make parallax
work)

I've kept parallax and lighting enabled, so visuals will still look
better then multiz pre plane cube.
It does also mean that things like FOV don't work, but honestly they
didn't work PRE plane cube, and FOV's implementation makes me mad so I
have a hard time caring.

Reduces gpu usage on my machine on tram from 47% to 32%, just above the
27% I get on meta.

I'm happy with this.

Oh also turns out the parallaxing had almost no cost. Need to remove it
as a side effect of what I'm doing but if I could keep it I would.

There's still room for in between performance options, like disabling
things like AO on lower z layers, but I didn't expect it to make a huge
impact, so I left things as is

Also fixes a bug with paper bins not respecting z layer. It came up in
testing and annoyed me

## Why It's Good For The Game

Ensures we can make multiz maps without running into client performance
issues, allows users to customize performance and visual quality.

## Changelog
:cl:
add: Adds a new rendering option to the gameplay preferences. You can
now limit the rendering intensity of multiz levels. This will make
things look a bit worse, but run a LOT better. Try it out if your
machine chokes on icebox or somethin.
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Adds a preference that disables intensive rendering on different multiz layers

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [vicirdek/PsychonautStation](https://github.com/vicirdek/PsychonautStation)@[83f475aa7e...](https://github.com/vicirdek/PsychonautStation/commit/83f475aa7ec4290c6961f1f14c5da80f340989b8)
#### Thursday 2022-12-01 11:07:38 by tralezab

Adds the DNA Infuser, a genetics machine you feed corpses to infuse their DNA with yours! What could go wrong?! (#71351)

## About The Pull Request  
Adds the "DNA Infuser" to genetics. One person enters, a corpse is added
to the machine, and you can activate the machine to "infuse" the subject
with the DNA. This converts one random organ from a set into the
mob-related organ.

### Rat mutation 🐀

Rats can be fed in to turn you into a rat-creature-thing!
```diff
+See better in the dark
+Can pretty much eat anything! Toxic foods, gross foods, whatever works!
+Smaller, and can climb tables
?Randomly squeaks occasionally?
-Take twice as much damage
-Vulnerable to flashes
-Gets hungry MUCH quicker.
-Yes, eat anything, but only ENJOY dairy.
```
Having every rat organ at once allows you to ventcrawl nude!

### Carp mutation 🐟 

Carp work for a mutation as well!
```diff
+Strong jaws, that drop teeth over time!
+Space immunity! Breathe in space, unbothered by pressure or cold!
+Smaller, and can climb tables
-Can't block your jaws with a mask
-Can't take the heat, overheats easily
-Can only breathe in environments that have minimal or no oxygen
-Nomadic. If you don't enter a new zlevel for awhile, you'll start feeling anxious.
```
Having every carp organ at once allows you to swim through space!

### Fly mutation 🪰 

Any corpses without organs to turn into turn into fly organs! Fly organs
now have a bonus for collecting them all, transforming you into a fly,
when you pass the threshold. But even without those, fly organs are
technically... organs. They most of the time work like normal ones.

## Todo 🐦 

- [x] Finish the infuser code
- [x] Create a little booklet that shows what kind of shit you can turn
into, hopefully i can autogenerate this based off of organ set subtypes
list
- [x] sprite/slap a color on rat mutant organs
- [x] Maybe make a *few* more organ sets

## Why It's Good For The Game 🐑 

Oops, I forgor to fill this out! My hackmd is here.

https://hackmd.io/@bazelart/ByFkhuUIi

## Changelog 🧬 

:cl: Tralezab code, Azlan + Azarak (Az gaaang) for the organs
add: Added the DNA infuser to genetics! Person goes in, corpse goes in,
and they combine!
add: Try not to turn yourself into a fly, OK?
/:cl:

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [measurement-factory/squid](https://github.com/measurement-factory/squid)@[2b6b1bcb86...](https://github.com/measurement-factory/squid/commit/2b6b1bcb8650095c99a1916f5964305484af7ef0)
#### Thursday 2022-12-01 12:05:54 by Alex Rousskov

Bug 5055: FATAL FwdState::noteDestinationsEnd exception: opening (#877)

The bug was caused by commit 25b0ce4. Other known symptoms are:

    assertion failed: store.cc:1793: "isEmpty()"
    assertion failed: FwdState.cc:501: "serverConnection() == conn"
    assertion failed: FwdState.cc:1037: "!opening()"

This change has several overlapping parts. Unfortunately, merging
individual parts is both difficult and likely to cause crashes.

## Part 1: Bug 5055.

FwdState used to check serverConn to decide whether to open a connection
to forward the request. Since commit 25b0ce4, a nil serverConn pointer
no longer implies that a new connection should be opened: FwdState
helper jobs may already be working on preparing an existing open
connection (e.g., sending a CONNECT request or negotiating encryption).

Bad serverConn checks in both FwdState::noteDestination() and
FwdState::noteDestinationsEnd() methods led to extra connectStart()
calls creating two conflicting concurrent helper jobs.

To fix this, we replaced direct serverConn inspection with a
usingDestination() call which also checks whether we are waiting for a
helper job. Testing that fix exposed another set of bugs: The helper job
pointers or in-job connections were left stale/set after forwarding
failures. The changes described below addressed most of those problems.


## Part 2: Connection establishing helper jobs and their callbacks

A proper fix for Bug 5055 required answering a difficult question: When
should a dying job call its callbacks? We only found one answer which
required cooperation from the job creator and led to the following
rules:

* AsyncJob destructors must not call any callbacks.

* AsyncJob::swanSong() is responsible for async-calling any remaining
  (i.e. set, uncalled, and uncancelled) callbacks.

* AsyncJob::swanSong() is called (only) for started jobs.

* AsyncJob destructing sequence should validate that no callbacks remain
  uncalled for started jobs.

... where an AsyncJob x is considered "started" if AsyncJob::Start(x)
has returned without throwing.

A new JobWait class helps job creators follow these rules while keeping
track on in-progress helper jobs and killing no-longer-needed helpers.

Also fixed very similar bugs in tunnel.cc code.


## Part 3: ConnOpener fixes

1. Many ConnOpener users are written to keep a ConnectionPointer to the
   destination given to ConnOpener. This means that their connection
   magically opens when ConnOpener successfully connects, before
   ConnOpener has a chance to notify the user about the changes. Having
   multiple concurrent connection owners is always dangerous, and the
   user cannot even have a close handler registered for its now-open
   connection. When something happens to ConnOpener or its answer, the
   user job may be in trouble. Now, ConnOpener callers no longer pass
   Connection objects they own, cloning them as needed. That adjustment
   required adjustment 2:

2. Refactored ConnOpener users to stop assuming that the answer contains
   a pointer to their connection object. After adjustment 1 above, it
   does not. HappyConnOpener relied on that assumption quite a bit so we
   had to refactor to use two custom callback methods instead of one
   with a complicated if-statement distinguishing prime from spare
   attempts. This refactoring is an overall improvement because it
   simplifies the code. Other ConnOpener users just needed to remove a
   few no longer valid paranoid assertions/Musts.

3. ConnOpener users were forced to remember to close params.conn when
   processing negative answers. Some, naturally, forgot, triggering
   warnings about orphaned connections (e.g., Ident and TcpLogger).
   ConnOpener now closes its open connection before sending a negative
   answer.

4. ConnOpener would trigger orphan connection warnings if the job ended
   after opening the connection but without supplying the connection to
   the requestor (e.g., because the requestor has gone away). Now,
   ConnOpener explicitly closes its open connection if it has not been
   sent to the requestor.

Also fixed Comm::ConnOpener::cleanFd() debugging that was incorrectly
saying that the method closes the temporary descriptor.

Also fixed ConnOpener callback's syncWithComm(): The stale
CommConnectCbParams override was testing unused (i.e. always negative)
CommConnectCbParams::fd and was trying to cancel the callback that most
(possibly all) recipients rely on: ConnOpener users expect a negative
answer rather than no answer at all.

Also, after comparing the needs of two old/existing and a temporary
added ("clone everything") Connection cloning method callers, we decided
there is no need to maintain three different methods. All existing
callers should be fine with a single method because none of them suffers
from "extra" copying of members that others need. Right now, the new
cloneProfile() method copies everything except FD and a few
special-purpose members (with documented reasons for not copying).

Also added Comm::Connection::cloneDestinationDetails() debugging to
simplify tracking dependencies between half-baked Connection objects
carrying destination/flags/other metadata and open Connection objects
created by ConnOpener using that metadata (which are later delivered to
ConnOpener users and, in some cases, replace those half-baked
connections mentioned earlier. Long-term, we need to find a better way
to express these and other Connection states/stages than comments and
debugging messages.


## Part 4: Comm::Connection closure callbacks

We improved many closure callbacks to make sure (to the extent possible)
that Connection and other objects are in sync with Comm. There are lots
of small bugs, inconsistencies, and other problems in Connection closure
handlers. It is not clear whether any of those problems could result in
serious runtime errors or leaks. In theory, the rest of the code could
neutralize their negative side effects. However, even in that case, it
would only be a matter of time before the next bug bites us due to stale
Connection::fd and such. These changes themselves carry elevated risk,
but they get us closer to reliable code as far as Connection maintenance
is concerned. Without them, we will keep chasing deadly side effects of
poorly implemented closure callbacks.

Long-term, all these manual efforts to keep things in sync should become
unnecessary with the introduction of appropriate Connection ownership
APIs that automatically maintain the corresponding environments (TODO).


## Part 5: Other notable improvements in the adjusted code

Improved Security::PeerConnector::serverConn and
Http::Tunneler::connection management, especially when sending negative
answers. When sending a negative answer, we would set answer().conn to
an open connection, async-send that answer, and then hurry to close the
connection using our pointer to the shared Connection object. If
everything went according to the plan, the recipient would get a non-nil
but closed Connection object. Now, a negative answer simply means no
connection at all. Same for a tunneled answer.

Refactored ICAP connection-establishing code to to delay Connection
ownership until the ICAP connection is fully ready. This change
addresses primary Connection ownership concerns (as they apply to this
ICAP code) except orphaning of the temporary Connection object by helper
job start exceptions (now an explicit XXX). For example, the transaction
no longer shares a Connection object with ConnOpener and
IcapPeerConnector jobs.

Probably fixed a bug where PeerConnector::negotiate() assumed that
sslFinalized() does not return true after callBack(). It may (e.g., when
CertValidationHelper::Submit() throws). Same for
PeekingPeerConnector::checkForPeekAndSpliceMatched().
 
Fixed FwdState::advanceDestination() bug that did not save
ERR_GATEWAY_FAILURE details and "lost" the address of that failed
destination, making it unavailable to future retries (if any).

Polished PeerPoolMgr, Ident, and Gopher code to be able to fix similar
job callback and connection management issues.

Polished AsyncJob::Start() API. Start() used to return a job pointer,
but that was a bad idea:
    
* It implies that a failed Start() will return a nil pointer, and that
  the caller should check the result. Neither is true.

* It encourages callers to dereference the returned pointer to further
  adjust the job. That technically works (today) but violates the rules
  of communicating with an async job. The Start() method is the boundary
  after which the job is deemed asynchronous.
    
Also removed old "and wait for..." post-Start() comments because the
code itself became clear enough, and those comments were becoming
increasingly stale (because they duplicated the callback names above
them).

Fix Tunneler and PeerConnector handling of last-resort callback
requirements. Events like handleStopRequest() and callException() stop
the job but should not be reported as a BUG (e.g., it would be up to the
callException() to decide how to report the caught exception). There
might (or there will) be other, similar cases where the job is stopped
prematurely for some non-BUG reason beyond swanSong() knowledge. The
existence of non-bug cases does not mean there could be no bugs worth
reporting here, but until they can be identified more reliably than all
these benign/irrelevant cases, reporting no BUGs is a (much) lesser
evil.

TODO: Revise AsyncJob::doneAll(). Many of its overrides are written to
check for both positive (i.e. mission accomplished) and negative (i.e.
mission cancelled or cannot be accomplished) conditions, but the latter
is usually unnecessary, especially after we added handleStopRequest()
API to properly support external job cancellation events. Many doneAll()
overrides can probably be greatly simplified.

---
## [projects-nexus/nexus_kernel_xiaomi_lavender](https://github.com/projects-nexus/nexus_kernel_xiaomi_lavender)@[3f8244054f...](https://github.com/projects-nexus/nexus_kernel_xiaomi_lavender/commit/3f8244054f8a76be61cb950ad51c95df3bb5e5e0)
#### Thursday 2022-12-01 12:16:03 by Christian Brauner

BACKPORT: signal: add pidfd_send_signal() syscall

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

(cherry picked from commit 3eb39f47934f9d5a3027fe00d906a45fe3a15fad)

Conflicts:
        arch/x86/entry/syscalls/syscall_32.tbl - trivial manual merge
        arch/x86/entry/syscalls/syscall_64.tbl - trivial manual merge
        include/linux/proc_fs.h - trivial manual merge
        include/linux/syscalls.h - trivial manual merge
        include/uapi/asm-generic/unistd.h - trivial manual merge
        kernel/signal.c - struct kernel_siginfo does not exist in 4.14
        kernel/sys_ni.c - cond_syscall is used instead of COND_SYSCALL
        arch/x86/entry/syscalls/syscall_32.tbl
        arch/x86/entry/syscalls/syscall_64.tbl

(1. manual merges because of 4.14 differences
 2. change prepare_kill_siginfo() to use struct siginfo instead of
kernel_siginfo
 3. use copy_from_user() instead of copy_siginfo_from_user() in copy_siginfo_from_user_any()
 4. replaced COND_SYSCALL with cond_syscall
 5. Removed __ia32_sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_32.tbl.
 6. Replaced __x64_sys_pidfd_send_signal with sys_pidfd_send_signal in arch/x86/entry/syscalls/syscall_64.tbl.)

Bug: 135608568
Test: test program using syscall(__NR_pidfd_send_signal,..) to send SIGKILL
Change-Id: I34da11c63ac8cafb0353d9af24c820cef519ec27
Signed-off-by: Suren Baghdasaryan <surenb@google.com>
Signed-off-by: electimon <electimon@gmail.com>
Signed-off-by: ImPrashantt <prashant33968@gmail.com>

---
## [Codeptor/password_manager](https://github.com/Codeptor/password_manager)@[4275c80cc5...](https://github.com/Codeptor/password_manager/commit/4275c80cc5f363d01b94bfcfc92c2a62d0de47d8)
#### Thursday 2022-12-01 12:26:55 by aryanraj

Made some changes to stupid ass decisions. Bitch you need yo ass whipped by black momma and a latino drugie dad :/

---
## [Codeptor/password_manager](https://github.com/Codeptor/password_manager)@[747369e099...](https://github.com/Codeptor/password_manager/commit/747369e09995fc387c8c7ac36839585e49da6473)
#### Thursday 2022-12-01 12:26:55 by Krish Katyal

Merge pull request #1 from aryanraj2713/main

Made some changes to stupid ass decisions. Bitch you need yo ass whip…

---
## [Amerecanno/CoffeStation](https://github.com/Amerecanno/CoffeStation)@[8620d970b0...](https://github.com/Amerecanno/CoffeStation/commit/8620d970b0aaa8d632e83a4dcc35547826f555df)
#### Thursday 2022-12-01 13:43:20 by DimmaDunk

Shields, sounds, holsters and more (#4169)

* Shields, sounds, holsters and more

- Better sound for blocking with shields, also sounds for stopping projectiles with them (and breaking)
- Ports the double belt pistol holder (pouch) and throwing knives rig (pouch) from Eris. With belt-worn sprites made by me.
- Adds the belt pistol holster and knife rig to the marshal vendors and absolutist printing disk
- Ports the Bulldozer shield from Eris, tweaks its recipe to include an actual closet
- Makes suit sensors spike in danger if someone's toxloss is at 70 or higher, since that is the point of liver failure
- On the same note, reduces the amount of organ damage from MSOF as it was too punishing, allowing for a better window of opportunity to save someone from dying
- Makes deployable barriers needed to be anchored to be able to brace your gun on it
- Adds most types of holsters to marshals vendors, ups their quantity
- Soteria Gauze and Ointment buffed on par with Church ones, to justify their convoluted hand-crafting method
- Makeshift AK and Luty added to random handmade guns to spawn
- Rangers get the double holster instead of the single one
- Adds a generic katana to loadout for four points
- Adds better sounds for the following emotes: male and female *sigh, *whistle (more variety), female *urah
- Adds snort and awhistle (targeted) emotes
- Makes a lot of audible emotes actually check if you're muzzled instead of magically being executed despite mouth coverage
- Adds some of the missing emotes to the *help list
- Adds hissing, meowing, and purring sound for cats, they will hiss at any ghosts they detect now!
- Fixes Mana from Heaven invisible sprite
- Claw and Baton energy drinks added overdose that causes organ damage at 60 units consumed
- Fixes incorrect Claw RED and BLUE sprites
- Claw Blue made actually made tastier
- Case Closer baton now contains atomic coffee instead of espresso (Marshal buff)
- Hay Fever claw energy improved citric formula
- Attempts to port Shields blocking projectiles functionality from Eris, but fails miserably (Tested not to work, but leaving the groundwork just in case)

* Nerfs liver failure damage even further

Random number 2 to 6 damage per tick

* Adds *zartan emote

Whistling of "For he's a jolly good fellow", GI Joe reference.

* Armor pen fix

Certain powered hammers were not properly inheriting armor pen somehow

* Preppers fairness

- Removes Sentinel Seeker from the random prepper mob spawn list
- Makes Sentinel Seeker a low spawner on par with Renders and nightmare stalkers as it shares similar stats with them
- Replaces certain prepper mob spawns with various low-chance Sentinel Seeker spawns on areas of high loot concentration (mech bays, prepper armory, near the excelsior disks, etc)
- Removes a trap spawner on the same room as Outsider spawn, as it can sometimes be a mine impossible to traverse on the only exit way
- Replaces hardspawn of Sentinel Seeker in Preppers medbay with a low chance for one, compensates by adding two more ranged mobs to the area

* Louder emotes

- Some female emotes were too low
- Typo fixes on bear rawr proc

* Apply suggestions from code review

This is a BYOND joke

Co-authored-by: Trilbyspaceclone <30435998+Trilbyspaceclone@users.noreply.github.com>

---
## [apollographql/router](https://github.com/apollographql/router)@[cfb421a564...](https://github.com/apollographql/router/commit/cfb421a5646de4ae5d5634415c86336d70c6fb90)
#### Thursday 2022-12-01 15:08:41 by Bryn Cooke

Fixes #2123 (#2162)

Issue was introduced with #2116 but no release had this in.

Move operations would insert data in the config due to the delete magic
value always getting added. Now we check before adding such values.

We may need to move to fluvio-jolt longer term.

<!--
First, 🌠 thank you 🌠 for considering a contribution to Apollo!

Some of this information is also included in the /CONTRIBUTING.md file
at the
root of this repository.  We suggest you read it!

  https://github.com/apollographql/router/blob/HEAD/CONTRIBUTING.md

Here are some important details to keep in mind:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will
take more than an hour, please make sure it has been discussed in an
        issue first. This is especially true for feature requests!

* 💡 Features
Feature requests can be created and discussed within a GitHub Issue.
Be sure to search for existing feature requests (and related issues!)
prior to opening a new request. If an existing issue covers the need,
please upvote that issue by using the 👍 emote, rather than opening a
        new issue.

* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.

* 📖 Contribution guidelines
Follow https://github.com/apollographql/router/blob/HEAD/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
        tests for all new behavior.

* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
        your pull request is meant to accomplish. Provide 🔗 links 🔗 to
associated issues! Documentation in the docs/ directory should be
updated
        as necessary.  Finally, a /CHANGELOG.md entry should be added.

We hope you will find this to be a positive experience! Contribution can
be
intimidating and we hope to alleviate that pain as much as possible.
Without
following these guidelines, you may be missing context that can help you
succeed
with your contribution, which is why we encourage discussion first.
Ultimately,
there is no guarantee that we will be able to merge your pull-request,
but by
following these guidelines we can try to avoid disappointment.

-->

Co-authored-by: bryn <bryn@apollographql.com>

---
## [ooni/data](https://github.com/ooni/data)@[ad1a529d59...](https://github.com/ooni/data/commit/ad1a529d5980933572e5bb7b252025fe77933894)
#### Thursday 2022-12-01 15:24:33 by Arturo Filastò

Very Wide Observation Rows + Experiment generation (#17)

As part of this PR I did a major rework of the observation generation
system.

tl;dr
* Observations are being generated at a rate of ~5k measurements per
second (i.e. it should be possible to reprocess the full dataset in less
than 3 days)
* Bodies from the measurements are being archived in WAR files (this is
currently what is slowing down the observation generation the most and
is what leads to the process stalling at the end with a huge queue of
bodies to archive). This needs some work to be optimised further.
* We are now able to generate Experiment results from the based
observations using ground truths at a rate of 15k measurements per
seconds (i.e. it should be possible to re-analyse the full OONI dataset
in less than a day)

If you care to read more details, see below:

## Very Wide Observation Rows

Each Web Connectivity measurements ends up producing observations that
are all of the same type and are written to the same DB table.

This has the benefit that we don't need to lookup the observations we
care about in several disparate tables, but can do it all in the same
one, which is incredibly fast.

A side effect is that we end up with tables are can be a bit sparse
(several columns are NULL), but this doesn't seem to present major
difficulties.

The biggest challenge in this approach is figuring out which
observations are related to each other so that they can be packed into
the same row. In order to do this I kept the original observation model
in place, which gave me guarantees that the data structures were
properly filled out, and then for each of them I tried to lookup the
relevant other ones.

Any observation that doesn't have a friend, just ends up on its own
database row all alone.

## WAR Body writer

I worked on separating the process of archiving bodies and finding
blocking fingerprints in it. Basically during the processing we create a
WAR file with inside it the raw bodies and write to a dedicated database
(or potentially the same in it's own table, but I need to find how to
get that to perform well).

We are then able to separately scan through all these WAR files hunting
for blockpage fingerprints, which is actually pretty fast. If we add new
blockpage fingerprints we can just re-scan the WAR files looking for
them and update the database column with what we found.

## Misc performance improvements

It turns out clickhouse is not too happy when you do many writes per
second to it. In their docs they state you shouldn't be making more than
1 request per second
(https://clickhouse.com/docs/en/about-us/performance/#performance-when-inserting-data).

I encountered this issue when I had optimised the processor to the point
that I was hitting this limit. The result is that the clickhouse process
starts consuming a bunch of CPU and memory and eventually just stops
dropping any connection attempt to it.

To overcome this the ClickhouseConnection database abstraction I added
the concept of a row buffer, which waits to become full with a certain
number of rows before flushing it to the clickhouse connection. This
worked surprisingly well and improved the overall performance of the
reprocessing task by 1 order of magnitude.

Quite a bit of additional changes were made to how multiprocessing is
done and small tweaks here and there based on iterations.

### Experiment result generation

I have added support in here for generating experiment results from the
Very Wide Observation Rows. Basically we process data in batches of 1
day. For each day we first generate a ground truth database which tells
us what we should expect to see by looking at all other web connectivity
control measurement, but in the future maybe from other measurements
too.
The process of generating the ground truths is actually pretty expensive
(it used to be the most expensive task) and takes about 80-90 seconds
for a given day.

We then need to efficiently lookup the ground truths that are related to
a specific measurement so that we can correlate them to what we are
seeing in the data.

In the beginning I went for the most naive solution of just putting it
all in a list and then doing a full scan of it for the relevant ground
truths. As the ground truths for a given day can be in the order of the
100s of thousands, this obviously turned out to be incredibly expensive.

I briefly experimented with creating some hash maps onto the data, so
that these lookups would be faster, but quickly realised I needed
multiple indexes and I was basically re-inventing a database. I
obviously could not use clickhouse for this purpose because doing many
per second there is not what it's made for.

I then realised that I actually already had a database right inside of
the standard library of python: SQLite!

So I quickly put together an in-memory groundtruth database to put all
the ground truths and then do the lookup.

This made things significantly faster.

Yet this was not enough, because when you are processing a measurement,
you don't actually care to look at all the ground truths for the full
day, but only those which are for that specific measurement. It's pretty
easy to figure out which is the subset of all ground truths you care
about, so I implemented a system that does some pre-filtering and
reduction of the ground truths for the full day into only those that are
related to a particular measurement.
Note: this part of the code was put together very quickly and is
currently a bit racy and not so nice to look at, so it needs some
refactoring (the goal was just to see if it would work at all).

After this last improvement, the performance went up by 1 order of
magnitude.

All in all I'm glad to see that it's starting to come together and it
offers the prospect of being a much more efficient and iterative way of
doing analysis on OONI data.

The current state of things that Experiment Result generation is
happening at a rate of 20k results per seconds that are mostly
bottlenecked by the database writes.

Some significant amount of work needs to happen on validating the data
outputs so that we can check if the analysis logic is good (I didn't
spend much time working on this after the big ground truth refactor, so
it likely has some bugs).

It's nice that the results are explainable and you can easily figure out
which part of the analysis code generated a particular outcome through
the blocking_meta key.

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[3c187487b1...](https://github.com/mc-oofert/tgstation/commit/3c187487b1884040608ba23b0a89aa8b0176c2aa)
#### Thursday 2022-12-01 15:59:23 by MrMelbert

Renews a bunch of old roundend new reports that got lost. Plus, some roundend report QoL for cult and revs. (#71284)

## About The Pull Request

A few roundend reports got lost from moving to dynamic and other prs.
This PRs re-allows them to occur. Namely: "Wizard Killed" (lost in
dynamic), "Blob nuked" (lost in dynamic), "Cult escaped" (lost in cult
rework), and "Nuke Ops Victory" (station destroyed via nuke) (lost from,
what I can see, an oversight / accidental swap of report values).

Additionally, small roundend report QOL for cult: Removes antag datums
from spirit realm ghosts after being dusted, so they do not show up on
the report. And in reverse, heads of staff who were dusted / destroyed
in revolution rounds are now also shown in roundend reports.

## Why It's Good For The Game

Some of these reports are dead, which is is a shame because I think
they're cool and fun.

## Changelog

:cl: Melbert
qol: Successfully fending off a blob now has a cross station news report
again. More pressing reports will take priority over it, though.
qol: Successfully killing a wizard (and all of their apprentices) now
has a cross station news report again.
qol: If more than half of a cultist team manages to escape on the
shuttle (rather than summoning Nar'sie), they will send a unique cross
station news report. This is still a loss, by the way. Summon Nar'sie!
qol: Nuclear Operatives successfully nuking the station now has its
unique cross station news report again, and no longer uses the generic
"The station was nuked" report.
qol: Nuking the station to stop a blob infection now has a unique cross
station news report again. Good luck convincing admins to allow this.
qol: Cult ghosts from "Spirit Realm" no longer persist on the cult's
team after being desummoned, meaning they will not show up on roundend
report.
qol: Heads of staff will now always show up on revolution roundend
report - even if their body was fully destroyed.
/:cl:

---
## [Joalor64GH/Chocolate-Engine](https://github.com/Joalor64GH/Chocolate-Engine)@[bb85f1215f...](https://github.com/Joalor64GH/Chocolate-Engine/commit/bb85f1215fa499e2d4129d4158c78a3232a653e7)
#### Thursday 2022-12-01 18:02:10 by Wither362

light up bro

-anyone: OMG OPPONENT STRUMS LIGHT UP, JUST LIKE IN PSYCH ENGINE!!
-me: ***SHUT THE FUCK UP YOU PIECE OF IDIOT!***
-me: ***THAT WAS ORIGINALLY CREATED IN KADE ENGINE!! SO SHUT THE FUCK UP AND STOP TALKING ABOUT PSYCH ENGINE!!!!***

---
## [newstools/2022-business-hallmark](https://github.com/newstools/2022-business-hallmark)@[77ad9336a1...](https://github.com/newstools/2022-business-hallmark/commit/77ad9336a1766983447b50ad17b50a19a8ab5ce7)
#### Thursday 2022-12-01 19:10:46 by Billy Einkamerer

Created Text For URL [hallmarknews.com/suspected-yahoo-boy-hacks-girlfriend-to-death-in-ogun/]

---
## [KDE/spectacle](https://github.com/KDE/spectacle)@[52558022c5...](https://github.com/KDE/spectacle/commit/52558022c56395155d01b74ea202a3a401034f16)
#### Thursday 2022-12-01 19:26:18 by Noah Davis

Use QML SelectionSizeToolTip

remove hideWindow

don't make window transparent

not needed

use isGuiIntitiated

use new window sizing code paths

moved some stuff around to make it easier to get the timing for window
sizing right and also make stuff happening to the window happen in the
window class.

shorten code line

do touchEvent later

set up window color

dialog size/positioning

clean up

stuff I forgot

set cursors via hoverMoveEvent

make SelectionEditor a FocusScope

remove unneeded files

use native text rendering by default

add border and transparency to info box

Selection: add rect, rectItersectsRect, rectContainsRect, fix setX/setY

SelectionEditor: add dragLocation property

SelectionEditor: add dprRound

remove qpainter size tooltip

cleanup

InfoBackground -> FloatingBackground

temp: disable mandatory clang-format

god it's annoying. will remove this change later

add placeholder floating toolbar

will use for future functionality

SelectionEditor: add handlesRect property, clean/fix up painting

- exposes the area where the handles are to QML
- fixes some visual glitches
- makes the visual selection area slightly more accurate to what the
actual selected area is
- no longer changes stored data while painting

update overlay

Selection: add qDebug output

Selection: add dpr to debug output

clean up painting

SelectionEditor: Always use QPointF for mouse positions

If you don't, then you will lose precision when the GUI is scaled up.

SelectionEditor: combine size tooltip with toolbar when they overlap

SelectionEditor: redorder some functions for my convenience

Add SpectacleImageProvider

clean up

might delete this file later

cleanup and fix clazy/clang-tidy warnings

move invokable dprRound to SpectacleWindow, rename some qml files

add ImageView

SelectionEditor: comment formatting

SpectacleWindow: set max size in setGeometryFromScreensRect

SpectacleWindow: testing max DPR hack

theoretically, this should allow Spectacle to always use the max DPR on
Wayland so that higher DPR screens never have low resolution graphics.
Will likely cause serious performance issues until we switch to using
more QSG stuff for the SelectionEditor.

SpectacleWindow: use base/view background color for image view

Polish ImageView, add save/copy functions, make positioning work on wayland

really disable pre-commit hooks

missed this. it's temporary.

ensure image is always only just as big as it needs to be

clip ImageView toolbar while resizing, fix up padding

Focus qml item when not in selection mode

Add OptionsMenu

keep settings dialog above parent window

make acceptSelection public again

put rectangle selection first

ExportMenu: Add open screenshot folder and print actions

Change menus to just Export, Options and Help

Remove window state changing stuff

It works very poorly with Wayland

Fill image selection toolbar with real buttons

OptionsMenu: add all the actions

OptionsMenu: make showPreferencesDialog public

Allow window to be transparent for video recording UI

---
## [mAxYoLo01/library](https://github.com/mAxYoLo01/library)@[e527a7d034...](https://github.com/mAxYoLo01/library/commit/e527a7d034f93781d2739a380a1c87c089fdf572)
#### Thursday 2022-12-01 19:56:47 by EdVraz

feat(channel): Add new overwrite helper methods (#1173)

* fix: edge case

* refactor: move import

* guys I don't recommend coding when you're sick

* do stuff

* omg what the fuck did i code yesterday

* fix: simplify code

* feat: add another helper method

* Update channel.py

---
## [apollographql/apollo-server](https://github.com/apollographql/apollo-server)@[e3115faf8c...](https://github.com/apollographql/apollo-server/commit/e3115faf8c70b0d7e5f46ec26145c1e6bd88e0a9)
#### Thursday 2022-12-01 19:59:52 by Trevor Scheer

Add note about EOL packages (#7216)

There's been some apparent confusion around what EOL means for AS 2/3.
Concerned folks seem to be under the impression that they need to
migrate away immediately as if the software is going to disappear out
from under them, so we should make it clear that's not the case, even if
we recommend strongly against using EOL software.

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

* ⏰ Your time is important
To save your precious time, if the contribution you are making will take
more
than an hour, please make sure it has been discussed in an issue first.
          This is especially true for feature requests!
* 💡 Features
Feature requests can be created and discussed within a GitHub Issue. Be
sure to search for existing feature requests (and related issues!) prior
to
opening a new request. If an existing issue covers the need, please
upvote
that issue by using the 👍 emote, rather than opening a new issue.
* 🔌 Integrations
Apollo Server has many web-framework integrations including Express,
Koa,
Hapi and more. When adding a new feature, or fixing a bug, please take a
peak and see if other integrations are also affected. In most cases, the
fix can be applied to the other frameworks as well. Please note that,
since new web-frameworks have a high maintenance cost, pull-requests for
new web-frameworks should be discussed with a project maintainer first.
* 🕷 Bug fixes
These can be created and discussed in this repository. When fixing a
bug,
please _try_ to add a test which verifies the fix. If you cannot, you
should
still submit the PR but we may still ask you (and help you!) to create a
test.
* 📖 Contribution guidelines
Follow
https://github.com/apollographql/apollo-server/blob/main/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
          tests for all new behavior.
* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
your
pull request is meant to accomplish. Provide 🔗 links 🔗 to associated
issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much as possible. Without following these guidelines, you may be missing
context that can help you succeed with your contribution, which is why
we encourage discussion first. Ultimately, there is no guarantee that we
will be able to merge your pull-request, but by following these
guidelines we can try to avoid disappointment.
-->

Co-authored-by: Rose M Koron <32436232+rkoron007@users.noreply.github.com>

---
## [Garden-AI/garden](https://github.com/Garden-AI/garden)@[0282b5e28c...](https://github.com/Garden-AI/garden/commit/0282b5e28c9d431ae243f2016d1f880744c51ae3)
#### Thursday 2022-12-01 20:05:25 by Owen Price Skelly

🌱completes story 4 (garden metadata creation)🌱

`poetry add pydantic`

pydantic models for (many) datacite fields

new file `metadata.py` with pydantic definitions, contents are currently
just what was generated with
https://github.com/koxudaxi/datamodel-code-generator/, which I fed the
datacite 4.3 json schema found at
https://github.com/datacite/schema/blob/da8e10655cd9d6fffadf11fee142d406fb6f59cc/source/json/kernel-4.3/datacite_4.3_schema.json.
Note that they don't have a similar json schema for 4.4 (only xsd) so
whatever we keep from this this should probably be double-checked for
compatibility. If it turns out the 4.4 xsd is easy to convert to json
schema there's no reason not to, I just didn't find an easy way to do it.

Implement basic Garden pydantic model

The new file `model.py` contains a much, much simpler pydantic model
than the auto-generated one from the datacite 4.3 schema.

It also contains a `TempField` enum, just for use with default values
like we discussed during the gathertown meeting Tuesday.

The model is certainly not complete, but the next steps that I see are
likely to be a bit more involved and/or require some hand-holding
for a design decision.

These are obviously not all the fields we'll want
eventually - I'm not even sure if these are all the fields we
want *today*. These were just the fields I was pretty sure were safe to
include, and I put a handful of non-required fields in there too so that
we had some `TempField.REQUIRED`s and some `TempField.WARN`s

In particular, the actual validation can occur at a few different places
and can be more or less involved, depending on how much work we want a
validator to do for us.

For example, I think it would be straightforward to have the
validator for the doi just automatically try and hit the datacite API if
the user didn't explicitly provide one, OR we could force the user to
call a distinct register_new_doi function (which would naturally perform
some validation when it builds the json payload for the request).

Similarly, I think we'll want the `creators` field to be more than just
plain strings and while I think the `nameparser` library looks really
promising and I'd love to build that into the validation step, I don't
know if it's worth tying ourselves to it yet.

adding comments, minimal `create_garden()` method

implements method to write metadata.json to cwd

Couple of ideas here, both plausibly Bad Ideas.

The first is a validator `check_tempfield`. This is called on *every*
explicit field update, just to check for values that are still
`TempFields`, which should only ever show up as unchecked defaults (i.e.
only as the first arg to a pydantic `Field` function invocation). The
idea is that we want a validator to catch the unset-default
values *eventually*, but not until the user has done something to
indicate that they think they've provided enough info.

If a user is invoking a `register_garden` method, they presumably think
they're done defining the model metadata, so we verify that by
1. exporting their model to a python dict
2. feeding that dict into the `Garden` constructor as **kwargs

The idea is that any still-unset defaults would look (to pydantic) like
someone manually setting e.g.  `title=TempField.REQUIRED`, which will
trigger the `check_tempfield` validator.

The exceptions that validators raise should already be pretty
logs-friendly and human-friendly, if this works how I think it does.

poetry fix

typing typo

flake8 keeping me honest

fix: doi check was skipping when given regex

I'm not sure if this is me misunderstanding that argument, or if this is
a pydantic bug, but it's not the end of the world to take it out

updated `create_garden` method

add `Garden`to `__all__` export list

refactor Garden to not use TempField defaults hack

implement `validate` method for Garden

Note that this shadows a classmethod provided by pydantic's BaseModel,
which also happens to be the only undocumented BaseModel helper
function. I'm also happy to note that the hacky-feeling
`_ = Garden(**garden_to_validate)` trick to force validation is exactly
how the library method does it under the hood.

I'd even go as far as to say that I'm feeling pretty validated, myself.

refactor/cleanup model.py and register_garden

pytest fixtures for varyingly incomplete gardens

🐛 tests were probably a good idea all along

cleanup, more tests

validate year field

real doi prefix

cleanup + test json

refactor `creator` -> `author`

fix: forgot to return validated year str

remove owen-specific deps from poetry

---
## [Offroaders123/Art-Gen](https://github.com/Offroaders123/Art-Gen)@[42697a943f...](https://github.com/Offroaders123/Art-Gen/commit/42697a943f0b397e7594217cc7ef3bc627c41044)
#### Thursday 2022-12-01 20:23:01 by Offroaders123

FFmpeg Encoding Test!

Figured out how to encode my generated thumbnail alongside my song audio, into a video using FFmpeg! Since this is just in the test stage essentially, I'm just adding some links to how I got it to work, and a shell script of what I wrote in the terminal to run it. Now that I have a documented working version of this using `ffmpeg`, I will look into doing the same thing, but in the browser using FFmpeg WASM! It will be nice to have TS types for the API too, as I'm not completely 100% about what all the flags do. I think I understand most of them though:

ffmpeg - Starts the command (hehe)
loop - boolean, loop the next input with an infinite length, as needed
framerate - sets the framerate to 1 (this happens in multiple spots?)
i - first source, this is the image, 26.png
map 0 - get the first (only in this case) source value entry from the first input
map 1:a - get the audio only, from the second input source
c:v libx264 - I think this defines the codec for the output video format
preset: ultrafast - Not completely sure, I think this makes it run faster? I'm curious if this degrades the quality though, so I'm gonna experiment with adding/removing this to see what changes
tune: stillimage - Didn't look into this yet, but it seems like it probably makes the encoding more efficient if you know that the video is just one image the entire time
vvf - Video effects, sets the FPS to 10 (second time around?), sets the video format to yuv420p, not quite sure what that is yet
c:a copy - ooop! Hopefull this means make a simple copy of the audio, without reencoding it? That would be perfectly what I'm looking for! I want to keep the quality as high as possible, since this is for music specifically.
shortest - This sets the length of the output video to be the length of the shortest input source. In this case, the image can expand infinitely, so it's essentially "inifinite", while the audio for 26.m4a is 7 minutes. Since that is the shorter one, the video will be 7 minutes long, with the image truncating to fill that space specifically.
26.mp4 - The output file name!

This is nicely simple, and complex. Definitely feels very terminal-worthy. Like working with Bash, after getting used to hearing all of these different flags and abbreviations, it's gonna be super powerful to specifically critique your video format exactly to how you want it to be exported! I love how extensive `ffmpeg` is, it's mind-blowing how much people have put into it. This is inspirational to how I want my Minecraft world converter/editor project/thing to eventually work; To just let the program do the heavy lifting, and you can work with the data directly, using it's APIs :)

Love this!

---
## [Frank-py/Japy](https://github.com/Frank-py/Japy)@[01aebf1dfb...](https://github.com/Frank-py/Japy/commit/01aebf1dfb18cfc7abe1ecf84dc92aa7114b3301)
#### Thursday 2022-12-01 21:09:24 by Daniel

I am actually so fucking pissed bro this is so fucking annoying nothing ever works this is so fucking shit fuck this shit please help

---
## [itseasytosee/tgstation](https://github.com/itseasytosee/tgstation)@[bbb956d2a6...](https://github.com/itseasytosee/tgstation/commit/bbb956d2a670656e546c35a09ec27295e5e06e94)
#### Thursday 2022-12-01 21:10:58 by OrionTheFox

Removes Bowls from garbage spawners because they don't fit in trash bags and I'm SICK of not being able to clean! (#71152)

## About The Pull Request
Let me give you a scenario.

---

THIS, is you. Say hi!

![image](https://user-images.githubusercontent.com/76465278/200268480-9dcf1f45-3bc5-402d-b743-b0649deefb08.png)

You're a loyal janitor aboard NT-SS13. You love your job; despite the
dangers, it's generally not too busy or tedious. Just a spray, a sweep,
and put it all in a bag.

---

This. This is your enemy.

![image](https://user-images.githubusercontent.com/76465278/200269058-957ca433-4666-44b5-9c10-ae0da75219cb.png)

Some crewmembers continuously leave them in maintenance, tossing them
into garbage bins as they pass.
This bowl, you cannot spray it. You can sweep it as far as you want, but
in the end, cannot put it into the bag.

![image](https://user-images.githubusercontent.com/76465278/200269156-bbc7758b-9cbe-4a3b-8d17-9aa53254b4b2.png)

---

It exists to torment you.
Nothing more, nothing less.

You hate the bowl. And it hates you.
Wake up.

![image](https://user-images.githubusercontent.com/76465278/200269456-a7fda598-3556-4069-bd2a-44a8793c198f.png)
## Why It's Good For The Game
Usually when you pass a trash pile you expect it to have trash, and
entire bowls aren't technically trash code-wise, nor can you clean them.
Yes, this PR has a modicum of salt. It was salt left behind in THE DAMN
BOWLS.
## Changelog
:cl:
del: NT has decided to begin a Recycling initiative, asking crew to
please stop throwing their bowls away in maintenance. You should only
find trash and grime from now on!
/:cl:

---
## [KingBalDoro/Minestuck](https://github.com/KingBalDoro/Minestuck)@[49d249e447...](https://github.com/KingBalDoro/Minestuck/commit/49d249e4475474eb982b201444ab08a109cb0423)
#### Thursday 2022-12-01 21:14:48 by KingBalDoro

fucking stupid fucking screamsnake and it's stupid fucking celebrate yule mechanic

dumb fucking sonic adventure two fucking boss and it's stupid fucking dumb gimmick boss fucking screamsnake piece of shit

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[8c5d8c9828...](https://github.com/treckstar/yolo-octo-hipster/commit/8c5d8c98282b66734d265cb3e81df74c2424bce9)
#### Thursday 2022-12-01 21:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[0b9264ce5f...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/0b9264ce5f14565e42d5e3dc67660a95f5d48f65)
#### Thursday 2022-12-01 22:15:58 by SkyratBot

[MIRROR] Fixes mineral turfs having weird lighting [MDB IGNORE] (#17618)

* Fixes mineral turfs having weird lighting (#71219)

## About The Pull Request

Pixel offsets, unlike transforms, offset overlays too. this was breaking
lighting overlays for mineral walls.

We did pixel offsets to save on init time, but we can acomplish the same
thing using an initial matrix. It's static, so there's no additional
cost. S free

Damn moth

## Changelog
:cl:
fix: Mining walls won't have fucked lighting anymore
/:cl:

* Fixes mineral turfs having weird lighting

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [jrcribb/wireit](https://github.com/jrcribb/wireit)@[c85c022769...](https://github.com/jrcribb/wireit/commit/c85c02276975a1a86cbf509a7e9a353d5f0a19a8)
#### Thursday 2022-12-01 22:20:04 by Alexander Marks

Error when trying to cache outside of package (#182)

It's currently not possible to locally cache an output file that isn't inside of the package directory. We check for this case when we delete and throw, but not when we cache. So if you are caching but have cleaning disabled, we would silently weirdly save the output file to a parent directory, and then not restore it.

Now this is an error.

Note we could in theory do this during analysis, but I'm not 100% confident in my ability to correctly detect this case given all of the possible magic glob syntax, so for now it's safer to just do it at runtime. (see https://github.com/google/wireit/issues/64).

Also note we could in theory support caching files outside of the package root, but we'd have to do something like a tarball for the local cache, instead of simply copying into `.wireit/<script>/cache/<hash>`. We should think carefully about whether we want to do that, though, so I'm not dealing with that for now.

Fixes https://github.com/google/wireit/issues/181

---
## [BardTheBard/Skyrat-tg](https://github.com/BardTheBard/Skyrat-tg)@[120cbae7e7...](https://github.com/BardTheBard/Skyrat-tg/commit/120cbae7e703c5b7fa96924da5c90e1acdea3dc3)
#### Thursday 2022-12-01 22:58:04 by SkyratBot

[MIRROR] Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation. [MDB IGNORE] (#17554)

* Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation. (#71157)

## About The Pull Request

Resolves #67282.

As originally designed, plasma rivers (namely, those on Icebox, though
the turf was originally made for the Snowdin away mission) are meant to
literally strip the flesh from your bones, leaving you with plasmaman
limbs. I'm not certain when this broke entirely, although it seems to
have never been updated to work alongside Kapulimbs.

Transformation of limbs into plasmaman limbs used to be accomplished by
adding the "PLASMABURNT" trait to limbs. However, this trait in the
current code is entirely meaningless, only checked in the proc that
makes plasmamen catch fire. Essentially, the only "interaction" is
having your flesh melted off by a plasma river, donating that specific
limb to a plasmaman, and pranking them with the fact that that specific
limb will still make them burst into flames.

Exciting.

I've removed the trait entirely, as it does functionally nothing, and
restored the ability of plasma rivers to turn your limbs - and
eventually, you - into plasmaman equivalents.

To be honest, I'm not _entirely_ satisfied with the plasmaman
transformation process - it doesn't especially suit the lore of
plasmamen, and if you transform into one in the plasma rivers you'll
probably immediately die from Icemoon's atmosphere anyway. However, this
is something I'd prefer to revisit in a later PR.
## Why It's Good For The Game

There's little reason _not_ to remove a trait that does nothing.

As for plasmafication, it's a fun interaction that was already _meant_
to be there. The message about your flesh melting off has always
printed, even while it's doing exactly nothing to you. It's cool to fall
into the deadly plasma river and come away from it permanently scarred
with a weird skeleton limb. Turning into a plasmaman entirely is
unlikely to happen and will probably just kill you, but it's a fun and
weird way to be dead.
## Changelog
:cl:
del: Removed the useless "plasmaburnt" trait.
fix: Restored a broken interaction with plasma rivers that slowly
transforms you into a plasmaman.
/:cl:

* Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation.

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>

---
## [coveord/gate](https://github.com/coveord/gate)@[e2a108db75...](https://github.com/coveord/gate/commit/e2a108db759f1cdfe89c8ac6bd3fafc10c39ac8e)
#### Thursday 2022-12-01 23:41:02 by Chris Phillips

fix(authn/oauth2): prevent oauth2 redirect loops (#1517)

During setup of spinnaker authentication with oauth2 a common hurdle is a redirect loop.

For example:

https://github.com/spinnaker/spinnaker/issues/5794
https://github.com/spinnaker/spinnaker/issues/1630

Also, many threads in Slack discuss these problems. In fact this appears to be a common
pitfall for the spring-security-oauth2-autoconfigure library in general. A light refresher
on the ouath2 flow in play here seems worthwhile. The user is redirected from `/login` in gate
to the external auth provider (google, github, etc.) and after successfully authenticating
they are redirected back to the gate `/login` endpoint but this time with a code parameter
that is to be used to request an access token.

This request can fail for a variety of reasons, and if it does, the underlying spring library
triggers a redirect to the `/error` endpoint. What causes the redirect loop for gate in particular
(and for other users of the library in a similar fashion) is that the WebSecurityConfigurerAdapter
in play is treating `/error` as an authenticated path and so instead of just returning with a 401,
it re-redirects to `/login` and the redirect loop continues.

My thought is that instead of a redirect loop, simply allowing the 401 to be returned will be a stronger
more helpful signal as to what is going on. Hopefully it will save future first-time installers headaches.

Spinnaker docs have included several troubleshooting hints and tips for how where you terminate SSL
affects configuration etc. Even after following all of these and lots of spelunking through spinnaker
github issues and combing over threads in slack, I found myself still experiencing a redirect loop even
though I had applied all the combined wisdom that was applicable to my setup.

As it turns out, I had a bad copy/paste of my client secret in my configuration. So the request
to turn the code from google into an access token from google was failing with a 401. After much
debugging and deep diving into the spring security code I found that had I turned on DEBUG in gate
for these classes in gate-local.yml:

```
logging:
  level:
    org.springframework.security.web.authentication.SimpleUrlAuthenticationFailureHandler: DEBUG
    org.springframework.security.oauth2.client.filter.OAuth2ClientAuthenticationProcessingFilter: DEBUG
```

Then I would have seen in the logs that a 401 response was returned from google and perhaps it would have
caused me to look closer at my botched client secret configuration. I think perhaps we don't want to require
that all operators of spinnaker become spring-security-oauth2 experts. So I'm proposing adding `/error` to
the list of paths in gate that aren't treated as authenticated. Thus short-circuiting the redirect loop and
bringing to light helpful troubleshooting info that was previously more or less swallowed.

---

