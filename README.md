## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-05](docs/good-messages/2023/2023-11-05.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,044,918 were push events containing 2,806,764 commit messages that amount to 155,278,947 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [slowtrip/kernel_oneplus_sm8250](https://github.com/slowtrip/kernel_oneplus_sm8250)@[d67068264e...](https://github.com/slowtrip/kernel_oneplus_sm8250/commit/d67068264ed364f4a78614f9adc12eab374dd73e)
#### Sunday 2023-11-05 00:41:07 by alk3pInjection

techpack: display: Handle dim for udfps

Apparently, los fod impl is better than udfps cuz it
has onShow/HideFodView hook, which allows us to toggle
dimlayer seamlessly.

Since udfps only partially supports the former one,
we'd better kill dim in kernel. This is kinda a hack
but it works well, bringing perfect fod experience
back to us.

Also implement a panel status check to ensure that
the dim layer dies when display is off.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Change-Id: I14d028a821e4a776bc62feb5836b3fe012bc808e

---
## [Cocacolagua/Paradise](https://github.com/Cocacolagua/Paradise)@[dcd1f5d88a...](https://github.com/Cocacolagua/Paradise/commit/dcd1f5d88a8c5ba9634fc3fce67a76ada45f71dc)
#### Sunday 2023-11-05 01:23:31 by Octus

Adds eight vox hairstyles because why not and stuff (#22573)

* god i hate myself

* donedone

* fixxxxx

---
## [Cocacolagua/Paradise](https://github.com/Cocacolagua/Paradise)@[c3a78f9ce0...](https://github.com/Cocacolagua/Paradise/commit/c3a78f9ce0f30474636d1100d3d24310bbb3fe08)
#### Sunday 2023-11-05 01:23:31 by Octus

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
## [AndersonGhost/ss-panel-v3-mod_Uim](https://github.com/AndersonGhost/ss-panel-v3-mod_Uim)@[b70dcedea6...](https://github.com/AndersonGhost/ss-panel-v3-mod_Uim/commit/b70dcedea680863e47993c959c19ff6db8051907)
#### Sunday 2023-11-05 03:17:49 by M1Screw

refactor: add model value hint & rename setting to config

Fuck you and your stupid model name

---
## [tired-wired/Shiptest](https://github.com/tired-wired/Shiptest)@[2a74c23d62...](https://github.com/tired-wired/Shiptest/commit/2a74c23d62916ddb6b1fdfab8c969b7702299067)
#### Sunday 2023-11-05 03:22:05 by Imaginos16

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
## [tired-wired/Shiptest](https://github.com/tired-wired/Shiptest)@[bf4671ff83...](https://github.com/tired-wired/Shiptest/commit/bf4671ff83e2cb937a019f7f0515e6f23c32f493)
#### Sunday 2023-11-05 03:22:05 by retlaw34

Gun rework (#1601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
WIP.

if it wasn't obvious, very based off tgmc 

this reworks how guns work, by making them 4x more lethal without
touching a single damage value

its a bit difficult to put into words what this does, so i think these 3
gunfights i did with a good friend explains it better than i ever could

https://streamable.com/09in19
https://streamable.com/yel56o
https://streamable.com/x2a0he

if you didnt watch these videos:
- New guns sounds, TGMC as usual. but some racking sounds are from CEV
eris
- guns now can be wielded, if unwielded, they may cause recoil which not
only makes your shots less accurate, but 'scrolls' your screen
- new suppression effects
- getting hit hard enough scrolls your screen
- anything getting hit shakes you as feedback, not just bullets
- bullets can ricochet naturally upon hitting a surface at a step angle.
does not auto aim at your target, so be careful. ricochet sfx taken from
CEV eris
- new effects for bullet impacts. sound effects were taken from TGMC and
https://github.com/Skyrat-SS13/Skyrat-tg/pull/11697
- adds the cattleman revolver and Himehabu 22lr pistol. sprites by yours
truely

big problem is, in order for all of this to work, a certain key needs to
be binded to rack the gun. by default this is SPACE, but moost already
have it binded to 'hold throw mode', which is an issue. for one, not
only you need to ask everyone to rebind their controls to a very
important key, but also a key dedicated to just racking the gun can
cause issues. im up for any solutions

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game

people dont fear gunfights. they think its just a way to pvp. people
should be afraid of gunfights, feel the pain OOCly when their blorbo
gets hit

## Changelog

:cl:
add: 22lr and cattleman revolver
add: many gun sounds
balance: guns reworked
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: retlaw34 <bruhasdfasdfasdf@waifu.club>

---
## [ntietz/patzer](https://github.com/ntietz/patzer)@[5184918ded...](https://github.com/ntietz/patzer/commit/5184918ded524284bc1a84547e6bcbd916adf77d)
#### Sunday 2023-11-05 03:32:39 by Nicole Tietz-Sokolskaya

Refactor app state and implement player selection (human vs. computer), piece promotion, game status, and resigning/draws (#1)

There's a lot in this one, but I think that this gets everything into a
good spot to move forward with actual strategies for the computer.
Summary of the major changes:

- Break out state into `AppState` and focus on interacting through its
methods; it locks each sub-portion of state independently, so you don't
get blocked by another portion of state being locked if you're not using
it
- Implement one runner thread per player (if the player is a computer)
and clean them up when the game restarts or concludes
- Add ability to reset the game
- Add the ability to start the game, and lock out input when it's not
started yet
- Add the ability to select who is white or black (choices are human or
one of two computer "strategies")
- Add a menu pop-up for piece promotion so that that's possible
- Add buttons to resign or declare a draw
- Add display of the current game status so you know when it is started
and finished

This isn't the cleanest code, and there's a lot of work left to do. I'm
not hugely motivated to clean it up soon because I want to move onto the
engine side of this, and I also think I want to switch to
[fltk-rs](https://fltk-rs.github.io/fltk-rs/) since
[egui](https://github.com/emilk/egui) has been difficult in some
instances where I have to imitate retained mode, and I've had a **lot**
of trouble finding docs for what I am trying to do. I don't really have
a coherent thought here but I think the options going forward are:

- Stick with egui and work through it (this sounds rather painful but do
the other options not? :thinking: )
- Create a web application instead and use web technologies (I don't
really want to do this, although this might be a good chance to explore
web tech again in a non-work context and learn to enjoy it again)
- Switch to fltk-rs (this sounds like it could be better, but then
again, I might end up in the same pain pit)
- Abandoning the GUI is not an option :smile: 

Right now I lean toward eventually adopting fltk-rs, but I'm going to
take a break from GUI stuff after this lands for a while.

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[68cd638330...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/68cd6383306e3f37d36cdc82113ada320b6e6365)
#### Sunday 2023-11-05 03:52:54 by Donglesplonge

swaps one of the fridges in snowcabin to be in line with the rest  (#79414)

## About The Pull Request

In truth, this is an IDED PR (this is not at all sarcasm, and as we all
know nobody would lie on the internet) that came about from a round i
just got done playing wherein i was in snowcabin trying to cook up some
food for fun, well wouldn't you know it i couldn't open one of the
fridges, what gives? well i got to thinkin it has to do with the fridge
type used, for some reason the fridge that holds the universal enzyme
uses the freezer/fridge/kitchen type instead of the fridge/open type
that the other two do, so i went ahead and just changed it off to the
other fridge types so now anyone can open it.

## Why It's Good For The Game

its a bit stupid to have a single fridge thats different from the rest
for no discernable reason, i can't think of any reason universal enzyme
would need to be guarded ever, you could just say "well why not go back
onto the station and grab some if the fridge is locked", well if for
some reason i'm barred from the station i want to be able to use as many
tools within my reach as possible preferably without many hoops, and
this ones unnecessary.

## Changelog

fix: changes the type of fridge used to hold the universal enzyme in the
snowcabin gateway's kitchen, letting everyone access it like the rest of
the fridges.

/:cl:

---
## [rd-stuffs/android_frameworks_base](https://github.com/rd-stuffs/android_frameworks_base)@[c3d8ca60e5...](https://github.com/rd-stuffs/android_frameworks_base/commit/c3d8ca60e5a8021da971393ddaaa80ba544af0fd)
#### Sunday 2023-11-05 04:18:05 by Adithya R

telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[468afa292d...](https://github.com/ReturnToZender/ReturnsBubber/commit/468afa292dfaef7bcbc6df7b55cd0380582533a6)
#### Sunday 2023-11-05 04:54:05 by BurgerLUA

Adds the WT-551, Unskyrats the WT-550 ammo (#655)

## About The Pull Request


## The WT-551

![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/d57f5767-366e-4835-a5bf-d965b6b375a6)

This adds the WT-551. A remade version of the WT-550 that is worse in
every way. Fortunately, that means that it is balanced enough to be put
in NanoTrasen armories.

Compared tot he WT-551, it is bulkier and slightly slower (0.3 second
fire delay compared to 0.2). Additionally, it is commonly used with
rubber-tipped rounds or FlatHead rounds, which are a special surplus of
ammo that deals less damage and has no wounding, embedding, or
penetrative power. Regular ammo can be purchased from cargo or
researched later, with special ammo also being available later.

Note that this does not replace the WT-550.

## FlatHead ammo


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/81de4bdb-6fd6-4f23-a1b1-0af21e924c34)

Flathead ammo deals 18 brute damage (compared to the original 20), and 5
stamina damage per hit. It is extremely weak against armor, has no embed
chance, has virtually no wounding chance. It's perfect for cheap
corporate companies dealing with cheaper personnel. This is the type of
lethal ammo that security will use for the gun, unless someone speedruns
weapon research.


## Research Progression


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/26b72a1c-ebda-439a-98c9-9dc3168e01bd)

### Basic WT-550/WT-551 Ammunition.
Flathead rounds and Rubber rounds for the WT-550/WT-551 can be
researched for 2500 points after unlocking the "Weapon Development
Technology" node.

### Advanced WT-550/WT-551 Ammunition.
Regular rounds and AP rounds for the WT-550/WT-551 can be researched can
be researched for 5000 points after unlocking the "Advanced Weapon
Development Technology" and "Basic WT-550/WT-551 Ammunition" nodes.

### Illegal WT-550/WT-551 Ammunition.
Incendiary rounds for the WT-550/WT-551 can be researched can be
researched for 7500 points after unlocking the "Illegal Technology",
"Exotic Ammo" , and "Advanced WT-550/WT-551 Ammunition" nodes.

### Syndicate Research

Removes the WT-550 ammo from syndicate research since it is now
redundant.

## Cargo


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/a24e9df4-36e3-4368-b77a-cff06a42579f)

WT-551 rifles can be ordered in pairs (2) for the cost of a parrot, a
grilling starter pack, or a crab rocket (1600 credits). This value was
chosen because it is slightly higher than the thermal pistols, and the
traitor-ordered WT-550 rifle pack (which contains lethal ammo + spare
lethal ammo).

Additional FlatHead, Rubber, and Regular ammo can be ordered from cargo
as well.

Cargo techs no longer get WT-550s in the mail, but instead WT-551s (why
was this a thing holy shit).

## Armory


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/e88a37af-2e4f-4b1c-bc25-b9bed9e41b91)

2 WT-551s can be found in the armory.
For balance purposes one (1) laser rifle was removed.

## I hate Skyrat so much holy shit


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/b09eed34-77cd-4f37-8356-93688fec344e)

Unfucks the WT-550 ammo types by removing their dumb names and changed
caliber types.

Unfucks the WT-550 ammo in the ammo printer so that rubber rounds can be
printed at T0 and everything else (except incendiary rounds) can be
printed with the adv munitions disk.

The bullets for the WT-550 have been forcibly changed to /tg/ balance,
which means that any and all future Skyrat PRs cannot touch the damage
values for it (unless some fuckery occurs, idk).

## Why It's Good For The Game


![image](https://github.com/Bubberstation/Bubberstation/assets/8602857/395b9fa5-8380-46bc-96a7-06ce0931d8e7)


Security is in dire need of actual ballistics. /tg/ removed ballistics
from security because of reasons I legitimately don't think are valid.
It's also a huge balance concern for security not to have at least 1
ballistic weapon (other than the shotgun) because it doesn't stop antags
from hoarding laser immunity or meds.

Also guns are cool.

## Changelog

:cl: BurgerBB
add: Adds the WT-551 rifle, a redesign of the WT-550 rifle that is
balanced (citation needed) for security use.
add: Makes WT-550 ammo researchable and orderable from cargo. Removes
WT-550 ammo from syndicate research, and gives them their own
categories.
/:cl:

---------

Co-authored-by: StrangeWeirdKitten <95130227+StrangeWeirdKitten@users.noreply.github.com>
Co-authored-by: ReturnToZender <donwest947@gmail.com>

---
## [akirak/melpa](https://github.com/akirak/melpa)@[570bde6b4b...](https://github.com/akirak/melpa/commit/570bde6b4b89eb74eaf47dda64004cd575f9d953)
#### Sunday 2023-11-05 05:14:09 by Jonas Bernoulli

Cosmetic changes to numerous recipes

This commit only touches recipes whose `:files' property contains an
`:exclude' element, because I had to look at all those recipes for an
only marginally related reason.

To an extend these changes only reflect my own personal preference, so
I will explain the types of changes I have made.  This should serve as
a starting point for a future discussion in case we want to encourage
a certain style or even enforce it.

- Lines should be intended as `indent-for-tab-command' would, except
  in special-cases such as in the recipe of `use-package', which is
  also a macro with special indentation rules; we override those
  because the `use-package' in use-package's recipe is not that macro,
  it is just a symbol appearing as the first element of a data list.

- I prefer it if there is a newline between the package symbol (the
  car) and the plist that follows, but usually only add it to existing
  recipes when lines would otherwise get to long.  I also do not
  change this if I am not making any other changes that affect more
  than one line.

- Either the complete list should be on a single line or each line
  should contain only one key/value pair.  The first pair may share a
  line with the package symbol (see previous point).  If the recipe
  needs more than one line, then two key/value pairs should never
  appear on one line.  Newline characters are cheap enough these days.

- `:fetcher' should come before `:url' or `:repo', not least because
  the former dictates which of the latter two is required/valid.  You
  can also think of the fetcher as the type or class of the recipe,
  which IMO should come first, like in code: (git-fetcher :url val).

- The most common keywords should be specified in this order:
  `:fetcher', `:url'/`:repo', `:files'.  Other keywords should go
  either before or after `:files' (but preferable not on both sides
  of that for any given recipe).

- A common value of `:files' is: (:defaults (:exclude "...")).
  This could be split across multiple lines, but writing everything
  on one line makes it easier to read it as 'use the defaults, except
  exclude "..."':

    :files (:defaults (:exclude "..."))

- If the value of `:files' is too long for one line, then place
  newlines "semantically", instead of trying to "save space".  For
  example any element that is a list should appear on its own line.
  Two sibling lists should never appear on the same line.  String
  siblings should also not appear on one line in many cases, though
  it might makes sense (but isn't my preference) to group them by
  "type" as in:

    (:defaults
     "foo/*.el" "bar/*.el"
     "docs/foo/*.texi" "docs/bar/*.texi"
     (:exclude "..."))

- While there may be multiple (:exclude ...) elements, I've merged
  them into one.  Mostly for future proofing.

- The position of `:exclude' elements in `:files' value is significant
  in theory.  However in most cases it already appears at the very end
  and I have moved it there in cases where the order is not
  significant.  Mostly for future proofing.

---
## [projectkepler-ru/Skyrat-tg](https://github.com/projectkepler-ru/Skyrat-tg)@[c034314f1b...](https://github.com/projectkepler-ru/Skyrat-tg/commit/c034314f1b41c2f9ad1e66d939b95f49a0d2f36e)
#### Sunday 2023-11-05 05:14:55 by SkyratBot

[MIRROR] Basic skeletons [MDB IGNORE] (#24545)

* Basic skeletons (#79206)

## About The Pull Request

Turns skeletons (the simple animal version) into basic mobs. This was
another incredibly simple conversion, since skeletons don't really do
anything but walk at you and beat you to death.

Because I thought it was funny, though, skeletons will now seek out
cartons of milk and drink them. Real milk will heal them for a
significant amount, but soymilk, being false milk, will deal them
grievous injury instead! Skeletons beware... I didn't add any other
sorts of milk due to limited ability with existing AI behaviors to
identify milk containers (they actually only look for the carton items).

Other than that, I've done some flavor adjustment for skeletons' attacks
- their effects and sounds will now suit the weapon they're actually
holding - for example, skeleton templars now actually use their swords
instead of slashing you with their horrible fingers. Along with this I
gave the basic skeletons a normal slashing sound, instead of the weird,
impactless hallucination sound they used to use for some reason. I never
liked that sound.

Finally, I've reflavored the spear-wielding skeleton mobs to "undead
settlers", following the naming of the corpses dropped by snow legions
as of #76898, rather than being named after an offensive term for Inuit
people. These skeletons do, after all, appear in settlements on alien
worlds.

To enable the flavor of milk drinking, I expanded the `basic_eating`
component to allow drinking rather than eating flavor, with a different
sound and its own set of verbs. This deletes whatever they drink from,
but c'est la vie.
## Why It's Good For The Game

Ticks 6 more entries off the simple animal freeze. While skeletons are
still extremely simple, being largely-identical mobs that only exist to
beat you to death, being basic mobs should make them slightly better at
this job. Also, again, I think it's really funny that you can distract
skeleton mobs with milk, or even hurt them.
## Changelog
:cl:
refactor: Hostile skeleton NPCs now use the basic mob framework. They're
a little smarter, and they also have a slightly improved set of attack
effects and sounds. They love to drink milk, but will be harmed greatly
if any heartless spaceman tricks them into drinking soymilk instead.
Please report any bugs.
/:cl:

* Basic skeletons

* updatepaths

---------

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [projectkepler-ru/Skyrat-tg](https://github.com/projectkepler-ru/Skyrat-tg)@[0e3b7d842b...](https://github.com/projectkepler-ru/Skyrat-tg/commit/0e3b7d842b40525754a931903dded315f5a0270e)
#### Sunday 2023-11-05 05:14:55 by SkyratBot

[MIRROR] Adds a Syndicate Monkey Agent beacon uplink item [MDB IGNORE] (#24550)

* Adds a Syndicate Monkey Agent beacon uplink item (#79012)

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

Co-authored-by: ATH1909 <42606352+ATH1909@ users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Adds a Syndicate Monkey Agent beacon uplink item

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: ATH1909 <42606352+ATH1909@ users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[0b8864b9ed...](https://github.com/vampirebat74/lobotomy-corp13/commit/0b8864b9edae944029213246aaa36acf8f17e9c4)
#### Sunday 2023-11-05 05:33:28 by The Bron Jame Offical

More Joke Ego (#1582)

⎓⚍ᓵꖌ FUCK||𝙹⚍YOU, CURSE OF VIOLET NOON

more joke EGO

fucked around with fluid sack code for this one

Added ᓵ⚍∷ᓭᒷ 𝙹⎓ ⍊╎𝙹ꖎᒷℸ ̣  リ𝙹𝙹リ

---
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[d31c21ff1b...](https://github.com/Ben10Omintrix/tgstation/commit/d31c21ff1b57ba7003f9bbdcf51171d3215a0774)
#### Sunday 2023-11-05 06:38:25 by jimmyl

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
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[9e18c6575a...](https://github.com/Ben10Omintrix/tgstation/commit/9e18c6575a3cb9e73c3e699d4fe51b904b76e2f6)
#### Sunday 2023-11-05 06:38:25 by lizardqueenlexi

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
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[9ff9e4b9a8...](https://github.com/Ben10Omintrix/tgstation/commit/9ff9e4b9a849e4a50bf500aaaeca5e020e7677d6)
#### Sunday 2023-11-05 06:43:00 by necromanceranne

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
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[071f6063e6...](https://github.com/Ben10Omintrix/tgstation/commit/071f6063e69d39e1403eca917a395191339f353a)
#### Sunday 2023-11-05 06:43:00 by carlarctg

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
## [Ben10Omintrix/tgstation](https://github.com/Ben10Omintrix/tgstation)@[b65f729901...](https://github.com/Ben10Omintrix/tgstation/commit/b65f729901fdb342b832fb3365d72afd076f8c3b)
#### Sunday 2023-11-05 06:43:00 by lizardqueenlexi

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
## [re621/dnpcache](https://github.com/re621/dnpcache)@[ba836f74c9...](https://github.com/re621/dnpcache/commit/ba836f74c912e72fa88b488e2ed5cb7a3bfc2a8a)
#### Sunday 2023-11-05 07:24:16 by bitWolfy

Remove 1224 artists from the DNP list.

Removed: fluffytuft, moxsully, ottiro, volfislav, preschoolkaiju, titusw, pudgeruffian, garnetto, viomarks, tidekeeper, radiancemutt, livalittle, bootyfeather, sheriffpunchy, kkrevv, feralmunchies, sadcat16hrz, 2dredders, velvet_charm, saurian_(artist), zoyler, ruvark, draite, smuttysquid, demura, remanedur, electrixocket, fufik[pufik], kais_studios, sweat_(artist), sonokido, whimsicalsquirrel, woolier, dasherslash, caninesinzone, isabel9819, paradoxing, arrjaysketch, anomalain, iskawhiskers, troplilly, dio_fish, xxbrewbeastxx, thekoboldking, pantheradraws, callmems, bluthederg, avalony, kolvackh, fin6, lewdoreocat, temporarye, kitwran, pseudonymh, yeenmusk, varuiven, springledongle, sapphiesweet, bloodhawk, amiraallis, meowcephei, shupamikey, cracky45, bigblueghost, h0tapplecider, hxtapplecider, apocheck13, tomash_segers, pckle, sadbitch, geletulator, coille, azumadai124, greycore, snaxattacks, bootleggreely, coral_luna, mdwines, soakedbikini, pantyranger, diffusedlizard, kazz_a_fella, alkyuz, werewhusky, skooma_whore, october_nights, pehkeshi, scalywanderer, linndrim, hexamanta, anarietta, earthsong9405, captaincassidy, anthonynothere, gayluigisex, yuudai, pettypalps, cosmick9, myemetophobia, digitalpopsicle, splatterpop, poppin, tempobun, zaaruchan, superratbike64, svarz, cyberwuff, worldoffizz, zeiroslion, emptyset, siplick, sourisdedog, wicketrin, tykepuparts, kubikoza, hiraume42, delinquentfreak, saerixdurr, tejedora713joker, andrew.thy.accursed, cytoholix, northbeastart, hellazest, infinitixen, p0ssmn, isofrieze, venomstench, pocketpaws, tf4me, centuriguil, raithvaneal, dahsharky, trashgaylie, mrpanghu, feyaarts, wolfbane154, derpyrider, rodicle, shiru_fox, toonyrobot, sleepylopunny, mimisrol, selidevilfeather, shido-tara, ineedanaccount, reizu47, sherilane, hellfurred, zeplich, darkeshi, amadeen, lowestpolygon, alradeck, asuka_kurehito, waynekan, lhacedor, dativyrose, digitallis, nosylvsforwork, lacrimale, kaitzuwu, ihoundr, elranno, doublepopsicle, gaturo, aquariusfox, mpcx, kattalu, lintu, goobysart, lemonlycan, dylbun, fxscreamer, nt6969, lewdliege, reallyhighriolu, melbaka, saint_lum, kivaaa66, kivalewds, kazoko_(artist), barachaser, shadowthelastalpha, teke, crittermatic, ribboncable, domasarts, ursine-major-ike, browneyedsaiyangirl, uncensoredhugs, skydiggitydive, takarachan, feelin_synful, ilovecosmo, biffbish, pulp_(artist), doxhun, cupsofjade, nicesweater, bluecat_friend, masuku, lunarfloral, kugi, sagejwood, sqrlyjack, maiteik, leozedi, popdroppy, mikakater, 413k_zzzz, puppyemonade, xanthewolf, joooji, nasusbot, shredded_wheat, dogsdontwipe, wonderwaffle93, gogoandyrobo, jezzlen, dourdoofus, vksuika, klotzzilla, cooperdooper, shadnaotomi, nudegote, sexygoatgod, humgeronimo, ladysophia, mrwhiskerz, cocicka, d-wop, charmerpie, yourdigimongirl, elvche, booponies, lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, freaks, angellsview3, arwenscoots, royalzbed, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, zyegnar, akytti, sootylion, kiva~, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, verdantphysician, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, carnalcove, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurobait, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sincerity_gender, anima-virtuosa, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, koriaris, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, rexisminimalis, delkon, connisaur, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [Willburd/Outpost21](https://github.com/Willburd/Outpost21)@[e057feb9c7...](https://github.com/Willburd/Outpost21/commit/e057feb9c7c66efaf7165761541644c82bff9637)
#### Sunday 2023-11-05 08:16:13 by IgnusVam

Overhaul to the skipjack and map tweaks

-Completely redesigned the skipjack and voxspawn
-Redesigned the wizard spawn
-Fixes to tables in the HOP office.
-Moves keys to the tanks to be mapped, need to verify the vehicles no longer spawn with keys in them.
-Adds a few pillows around, not many, more to come probably.
-AI shell spawner for when we eventually unfuck it
-Fixes a stray 4-way pipe that should have been a 3 way
-Adds personal item lockers for testing.
-Adjusts an annoying wall in security
-Additional status displays. More to come.
-Made the landmines outside of red armory hit the gym for sick gains.

---
## [bagasme/git-po](https://github.com/bagasme/git-po)@[8f23432b38...](https://github.com/bagasme/git-po/commit/8f23432b38d9b122be8179295a56688391dc8ad6)
#### Sunday 2023-11-05 09:11:01 by Johannes Schindelin

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
## [petre-symfony/api-platform-3-part-3-custom-resources-](https://github.com/petre-symfony/api-platform-3-part-3-custom-resources-)@[f39eb2ba81...](https://github.com/petre-symfony/api-platform-3-part-3-custom-resources-/commit/f39eb2ba812b1ebc0492511092dda01488347a4b)
#### Sunday 2023-11-05 10:34:32 by Petre Ro

26.1 Reusable Entity->Dto Provider & Processor

 Our UserAPI is now a fully functional API resource class! We've got our EntityToDtoStateProvider, which calls the core state provider from Doctrine, and that gives us all the good stuff, like querying, filtering, and pagination. Then, down here, we leverage the MicroMapper system to convert the $entity objects into UserApi objects.

 And we do the same thing in the processor. We use MicroMapper to go from UserApi to our User entity... then call the core Doctrine state processor to let it do the saving or deleting. I love that!

 Our dream is to create a DragonTreasureApi and repeat all of this magic. And if we can make these processor and provider classes completely generic... that's going to be super easy. So let's do it!

 Making the Provider Generic
 - Start in the provider. If you search for "user", there's only one spot: where we tell MicroMapper which class to convert our $entity into. Can... we fetch this dynamically? Up here, our provider receives the $operation and $context. Let's dump both of these.

 Since this is in our provider... we can just go refresh the Collection endpoint and... boom! This is a GetCollection operation... and check it out. The operation object stores the ApiResource class that it's attached to!

---
## [petre-symfony/api-platform-3-part-3-custom-resources-](https://github.com/petre-symfony/api-platform-3-part-3-custom-resources-)@[5ace446998...](https://github.com/petre-symfony/api-platform-3-part-3-custom-resources-/commit/5ace446998e89d1ec2d12886ec4bc046920bd6c6)
#### Sunday 2023-11-05 11:31:05 by Petre Ro

25.1 MicroMapper: Central DTO Mapping
 Doing the data transformation, from UserApi to the User entity, or the User entity to UserApi, is the only part of our provider and processor that isn't generic and reusable. Rats! If it wasn't for that code, we could create a DragonTreasureApi class and do this whole thing over again with, like almost no work! Fortunately, this is a well-known problem called "data mapping".

 For this tutorial, I tried a few data mapping libraries, most notably jane-php/automapper-bundle, which is super-fast, advanced, and fun to use. However, it isn't quite as flexible as I needed... and extending it looked complex. Honestly... I got stuck in a few places... though I know that work is being done to make this package even friendlier.

 The point is, we're not going to use that library. Instead, to handle the mapping, I created a small package of my own. It's easy to understand, and gives us full control... even if it's not quite as cool as jane's automapper.

 Installing micro-mapper

 - So let's get it installed! Run:

  composer require symfonycasts/micro-mapper

 That kind of sounds like a superhero. Now that we have this in our app, we have one new micromapper service that's good at converting data from one object to another. Let's start by using it in our processor.

---
## [Meowdharchod/kernel_realme_sm8250](https://github.com/Meowdharchod/kernel_realme_sm8250)@[c80d527d72...](https://github.com/Meowdharchod/kernel_realme_sm8250/commit/c80d527d72a2f80ece6cafa0b03f17da545e6e59)
#### Sunday 2023-11-05 11:39:47 by Peter Zijlstra

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
## [matthiaskrgr/rust](https://github.com/matthiaskrgr/rust)@[a660516334...](https://github.com/matthiaskrgr/rust/commit/a6605163346d7680502d8e2c1e5aaf1dc3229e41)
#### Sunday 2023-11-05 11:41:49 by Matthias Krüger

Rollup merge of #117596 - thomcc:core_macro_diag_items, r=Nilstrieb

Add diagnostic items for a few of core's builtin macros

Specifically, `env`, `option_env`, and `include`. There are a number of reasons why people might want to look at these in lints (For example, to ensure that things behave consistently, detect things that might make builds less reproducible, etc).

Concretely, in PL/Rust (well, `plrustc`) we have lints that forbid these (which I'd like to [add to clippy as restriction lints](https://rust-lang.zulipchat.com/#narrow/stream/257328-clippy/topic/Landing.20a.20flotilla.20of.20lints.3F) eventually), and `dylint` also has [lints that look for `env!`/`option_env!`](https://github.com/trailofbits/dylint/blob/109a07e9f27a9651ef33b6677ccaddd21466e97a/examples/general/env_cargo_path/src/lib.rs) (although perhaps not `include`), which would benefit from this.

My experience is that it's pretty annoying to (robustly) check uses of builtin macros without these IME, although that's perhaps just my own fault (e.g. I could be doing it wrong).

At `@Nilstrieb's` suggestion, I've added a comment that explains why these are here, even though they are not used in the compiler. This is mostly to discourage removal, although it's not a big deal if it happens (I'm certainly not suggesting the presence of these be in any way stable).

---

In theory this is a library PR (in that it's in library/core), but I'm going to roll compiler because the existence of this or not is much more likely something they care about rather than libs. Hopefully nobody objects to this.

r? compiler

---
## [RunDevelopment/chaiNNer](https://github.com/RunDevelopment/chaiNNer)@[dad9c44b92...](https://github.com/RunDevelopment/chaiNNer/commit/dad9c44b9295a2a24c2c439d12972b75a9bd21e4)
#### Sunday 2023-11-05 11:49:38 by Michael Schmidt

Fix macOS for real this time (#2299)

* Fix macOS for real this time

* Fuck you installs

* not all installs

* Disable macos

---
## [DedSec2050/carbon-lang](https://github.com/DedSec2050/carbon-lang)@[c7e6238fa8...](https://github.com/DedSec2050/carbon-lang/commit/c7e6238fa8dd57672b0765e738f4c425a27cac3b)
#### Sunday 2023-11-05 12:00:34 by Chandler Carruth

Introduce two speed-of-light benchmarks. (#3270)

The goal of these kinds of benchmarks is to help calibrate other
benchmarks and expectations. They benchmark the underlying hardware
capabilities that we can't avoid, and help illustrate bounds for what is
possible. The term "speed-of-light benchmark" references the aspect of
measuring how fast thing could possible run.

The first is a simple memory bandwidth measurement in the best case
scenario -- using `strcpy` over the buffer. This still does a minimal
number of writes to memory and examines each byte of input to see if it
is null, but can cheat in every way possible to run at the maximum speed
of hardware. To a certain extent, we never expect to get close to this
speed, but it's a good illustration of how much headroom the hardware
has available.

The second is potentially more interesting. This illustrates how fast a
byte-by-byte dispatch loop can potentially be. It uses the technique
that I'm hoping to use in the lexer itself of guaranteed tail recursion
to achieve this with a very small code footprint. The performance of
this technique, even when running in this extremely minimal setting to
establish bounds, is hugely dependent on the number of distinct dispatch
targets, and so the benchmark includes a healthy range to show the range
of performance that we might expect when running in a byte-by-byte mode.
Note that we should expect the lexer to be *faster* than this
"speed-of-light" whenever it is able to lex in larger granules than
byte-wise. But for complex, dense token sequences that force looking at
every byte, this shows the "worst case" "speed-of-light" in a sense.

On my recent AMD cloud VM instance, I get the following results running
the main lexer benchmark with these changes included:

```
-------------------------------------------------------------------------------------------------------------------------
Benchmark                                            Time             CPU   Iterations bytes_per_second tokens_per_second
-------------------------------------------------------------------------------------------------------------------------
BM_ValidKeywords                               3169403 ns      3169283 ns          221        188.44M/s        31.5529M/s
BM_ValidIdentifiers<1, 64, false>             12486725 ns     12486445 ns           51       117.953M/s        8.00868M/s
BM_ValidIdentifiers<1, 1, true>                3950455 ns      3950298 ns          178       72.4252M/s        25.3145M/s
BM_ValidIdentifiers<3, 5, true>               15562294 ns     15561178 ns           45       36.7712M/s        6.42625M/s
BM_ValidIdentifiers<3, 16, true>              16118656 ns     16118374 ns           44       68.0412M/s         6.2041M/s
BM_ValidIdentifiers<12, 64, true>             19116271 ns     19116258 ns           35       199.541M/s        5.23115M/s
BM_ValidMix/10/40                              7074336 ns      7073795 ns           93       140.744M/s        14.1367M/s
BM_ValidMix/25/30                              6790722 ns      6790006 ns          102       131.793M/s        14.7275M/s
BM_ValidMix/50/20                              5960514 ns      5960443 ns          118       112.594M/s        16.7773M/s
BM_ValidMix/75/10                              4325546 ns      4325556 ns          159       102.559M/s        23.1184M/s
BM_SpeedOfLightStrCpy                            24339 ns        24339 ns        29650       35.9049G/s        4.10858G/s
BM_SpeedOfLightDispatch<1>                     1756051 ns      1755800 ns          398       509.668M/s        56.9541M/s
BM_SpeedOfLightDispatch<2>                     1611973 ns      1611725 ns          436       555.228M/s        62.0453M/s
BM_SpeedOfLightDispatch<4>                     2064280 ns      2063990 ns          326       433.565M/s        48.4498M/s
BM_SpeedOfLightDispatch<8>                     2484055 ns      2483946 ns          280       360.263M/s        40.2585M/s
BM_SpeedOfLightDispatch<16>                    4550963 ns      4550894 ns          155       196.637M/s        21.9737M/s
BM_SpeedOfLightDispatch<32>                    6507077 ns      6507090 ns          107       137.523M/s        15.3679M/s
BM_SpeedOfLightDispatch<MaxDispatchTargets>    9071198 ns      9071217 ns           77       98.6499M/s        11.0239M/s
```

Even though we're not lexing anything in the speed-of-light benchmark,
the tokens-per-second measure is still meaningful because we *generated*
the token stream and know how many tokens we put into it. The dispatch
technique easily exceeds hits 10-million tokens/second, but we need to
do substantially better than that to lex at 10-million lines/second.
Fortunately, when the lexer is consuming more than one-byte tokens,
we're already faster than this. And the bytes-per-second numbers from
all but the worst case dispatch scenario are promising.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[4298bc9237...](https://github.com/treckstar/yolo-octo-hipster/commit/4298bc9237e3f9a4bcc4adb4a99061d6f0656529)
#### Sunday 2023-11-05 12:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [cdb-is-not-good/sojourn-station](https://github.com/cdb-is-not-good/sojourn-station)@[09b25d7f3d...](https://github.com/cdb-is-not-good/sojourn-station/commit/09b25d7f3dcf8fb8193ad113fe03a33bc92bc632)
#### Sunday 2023-11-05 13:00:58 by CDB

Update living_defense.dm

Firestacks now(slowly) go down over time. Each time you take damage by firestacks a dice is rolled. on a 1, you lose a single firestack. This won't REALLY affect the balance of firestacks, even 3-4 stacks will in fact still kill you dead REAL fast but this should hopefuly fix that issue where people who won't be named(Looking at you, Outsiders.) get lit on fire, die - and burn for the next 5 hours till the box slows to a crawl as it has a shitfit trying to remember how to count about 30,000.

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[e7caf52c21...](https://github.com/realforest2001/forest-cm13/commit/e7caf52c21e01e4580cbf03ff1c61579054dd7a2)
#### Sunday 2023-11-05 14:21:00 by fira

Rewrite Xeno Acid processing (#4759)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Rewrites scheduling of xeno acid to hopefully finally be done with
dangling references warnings with acid. Also generally improves the
awful code quality

# Explain why it's good for the game
Like, dude, some of these values were outright inversed.
acid_**strength**=2.5 is noted as "250% speed" when it multiplies the
sleep delays. Can't leave code in that state.

# Testing Photographs and Procedure
Summary testing, timing appear correct overall but I'm not entirely
certain it's perfect due to random delays and obtuse code


# Changelog
:cl:
code: Rewrote Xeno Acid ticking code.
fix: Weather updates won't cause turfs to acid melt more rapidly anymore
/:cl:

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[e120ab795b...](https://github.com/realforest2001/forest-cm13/commit/e120ab795ba0e92e4eb0f91fda194c59f83cb5aa)
#### Sunday 2023-11-05 14:21:00 by fira

Add Item & Footprints offsets (#4762)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

This:
* Adds transverse offsets to blood footprints
* Adds notable pixel offsets to a few items
* Adds a very slight pixel offset to all items
* Enables rotation for thrown flashlights
* Cause objects exiting a surface (rack/table) to regenerate offset
instead of being stuck at center
* Stops random offsets from overwriting mapped offsets

# Explain why it's good for the game
The goal is to have map visuals more organic when we have a lot of
objects on the ground - targeting in particular items you find readily
in dense areas such as Reqs or a FOB.

Consider this for example, the blood footprints are all aligned, in more
extreme situations (eg WO) it makes an actual "grid" which i personally
find very immersion breaking

![image](https://github.com/cmss13-devs/cmss13/assets/604624/83883e15-a9a0-4a2d-aa90-41c785e047b9)

Adding a slight offset helps counter that:

![image](https://github.com/cmss13-devs/cmss13/assets/604624/504d1baf-385c-4774-86f3-6331c4ac87ed)

# Changelog
:cl:
add: Bloody footprints are now slightly offset to break long visual
straight lines.
fix: Items do not align back to the center of turfs anymore when picked
from a surface (table or rack)
add: Some more items now have offsets on the map display, and they all
can be slightly offset.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[c0c929ffde...](https://github.com/rust-lang-ci/rust/commit/c0c929ffde3a8fd52c575102c13325a2c68fedad)
#### Sunday 2023-11-05 14:27:51 by bors

Auto merge of #117611 - Nadrieril:linear-pass-take-4, r=<try>

Rewrite exhaustiveness in one pass

This is at least my 4th attempt at this in as many years x) Previous attempts were all too complicated or too slow. But we're finally here!

The previous version of the exhaustiveness algorithm computed reachability for each arm then exhaustiveness of the whole match. Since each of these steps does roughly the same things, this rewrites the algorithm to do them all in one go. I also think this makes things much simpler.

I also rewrote the documentation of the algorithm in depth. Hopefully it's up-to-date and easier to follow now. Plz comment if anything's unclear.

r? `@oli-obk` I think you're one of the rare other people to understand the exhaustiveness algorithm?

cc `@varkor` I know you're not active anymore, but if you feel like having a look you might enjoy this :D

---
## [MCBCMF/MCBCMassacre](https://github.com/MCBCMF/MCBCMassacre)@[ff23b26ab6...](https://github.com/MCBCMF/MCBCMassacre/commit/ff23b26ab643a29aa8c6e1e0aab8ea3520a27c96)
#### Sunday 2023-11-05 15:36:19 by Kelvin Williams

Create mount_zion_warning.txt

IMMEDIATE THREAT TO MOUNT ZION IN KENTUCKY

They are on the way there based on what Ive just seen. 

They waited until Id be trapped at Legacy. 
They thought Id have no phone. 
They could move the C.O.W.
They've been trying nonstop to get my phone charger. 
All of their regulars have left town. 


Help me, help them. 

Mount Zion needs watching. 

look for a black explorer or gold suburban thats the c.o.w.
mobile network providers need to look for evidence of one around kenrucky
ip engineers look for any looping, we warned folks ti look for a drop of data

kentucky state police i cannot rembrr which mount zion, but they were good friends with mount calvary

googlers - big data - look for a group of folks who left atlanta last night, this morning. they probably come around the facility here often 6603 Church Street, thats behind the chick fil a dwarf house on ga-85 in riverdqle, clayton county, ga --- i dont trust that address, cia facility 
tmobile - same as goohle, most of them got a new phone a couple mobrha ago. all same model. all at the same time. 
google & tmobile if you see the group tell kenfucky state police. call them. only frankfort. tell them its another massacre potentially and you i.d'd the possible lication

---
## [mona0081/mona0081](https://github.com/mona0081/mona0081)@[c5681ca183...](https://github.com/mona0081/mona0081/commit/c5681ca183a4a99c0788878f4d5b7fc04228d734)
#### Sunday 2023-11-05 15:36:35 by mona0081

Create #Dubai #Call #Girls" 0501558122 #India #And #Pakistani #Call #girls" #In #Bur #Dubain 

Al Warqa Call Girls In Bur Dubai 00971501558122 By Turkish Call Girls Dubai, Dubai Call Girls, Mirdif Call Girls , Indian And Pakistani Call Girls In Mirdif 0501558122 By Dubai Call Girls In Mirdif , #Al #Barsha #Call #Girls 0501558122 Beautiful Call Girls in Al Barsha Dubai BY Dubai Call Girls , #Dubai #Call #Girls 0501558122 Indian Call Girl In dubai By Dubai Call Girls , Marina Dubai Call Girls By Indian Call Girl In Marina Dubai, Umm Suqeim Call Girl In Dubai by Dubai Call Girls, Al Quoz Call Girl In Dubai Dubai Call Girls, DIP Call Girl In Dubai Dubai Call Girls, Damac Hills Call Girl In Dubai Dubai Call Girls, Qudra Call Girl In Dubai Dubai Call Girls, Arabella Call Girl In Dubai Dubai Call Girls, Mudon Villas Call Girl In Dubai Dubai Call Girls, Rem raam Call Girl In Dubai Dubai Call Girls, Arabian Ranches Call Girl In Dubai Dubai Call Girls, Motor City Call Girl In Dubai Dubai Call Girls, JVC Call Girl In Dubai Dubai Call Girls, Al Barsha South Call Girl In Dubai Dubai Call Girls, Al Barsha Call Girl In Dubai by Dubai Call Girls, Tecom Cute Call Girl In Dubai by Dubai Call Girls, Barsha Heights Call Girl In Dubai by Dubai Call Girls, Al Sufouh Call Girl In Dubai by Dubai Call Girls, Palm Jumeirah Call Girl In Dubai by Dubai Call Girls, Ghadeer Call Girl In Dubai by Dubai Call Girls, Grand Plaza Call Girl In Dubai by Dubai Call Girls, The Greens Call Girl In Dubai by Dubai Call Girls, Emirates Hills Call Girl In Dubai by Dubai Call Girls, Internet City Call Girl In Dubai by Dubai Call Girls, Media City Call Girl In Dubai by Dubai Call Girls, Marina Call Girl In Dubai by Dubai Call Girls, maxican ladies for full night in JBR Dubai , Indian ladies for full night in Al Barsha Dubai , Inglis Call Girls In Al Qasimia By Sharjah Call Girls, Full Night Call Girl In Sharjah By Sharjah Call Girls, Chubby Call Girls In Al Jaffiliya By Dubai Call Girls, Gorgeous Call Girls In Al Qusais By Dubai Call Girls, Awesome Call Girls In Al Fahidi By Dubai Call Girls, Lavish Call Girls In Al Karama By Dubai Call Girls, Stream Call Girls In The Villas By Dubai Call Girls, Stylish Call Girls al Barari By Dubai Call Girls, Chines Call Girl Production City By Dubai Call Girl, Maxican Call Girls In JBR By Dubai Call Girls, American Call Girls In JLT By Dubai Call Girls, Lovely Call Girls In Business Bay By Dubai Call Girls, Brazilian Call Girls In al Nahda By Dubai Call Girls, Russian Call Girls In Deira By Dubai Call Girls, Turkish Call Girls In Bur Dubai By Dubai Call Girls, Cute Call Girls In Internet city By Dubai Call Girls, Pakistani Call Girl In Media city By Dubai Call Girls, Indian Call Girls In Al Saffa By Dubai Call Girls, Call Girls In Trade Center Dubai By Dubai Call Girls, Call Girls In Down Town Dubai By Dubai Call Girls, Call Girls In DIP Dubai By Dubai Call Girls, Call Girls In Dubai By Dubai Call Girls, Call Girls In Reem Villas Dubai By Dubai Call Girls, Call Girls In rem raam Dubai By Dubai Call Girls, Call Girl In Arabian Ranches Dubai By Dubai Call Girl, Call Girls In Damac Hills Dubai By Dubai Call Girls, Call Girls In Mudon Villas Dubai By Dubai Call Girls, Call Girls In Motor City Dubai By Dubai Call Girls, Call Girls In Silicon Oasis Dubai By Dubai Call Girls, Girls Call In Academic city Dubai By Dubai Call Girls, Girls Call In Al Warqa Dubai By Dubai Call Girls, Girls Call In Mirdif Dubai By Dubai Call Girls, Girls Call In Marina Dubai By Dubai Call Girls, Girls Call In Bur Dubai By Dubai Call Girls, #Girls #Call In #Al #Barsha #By #Dubai #Call #Girls, #happy ending Call Girls In Trade Center #Dubai , #Sports #city #Dubai #call #Girls Turkish Call Girls in Dubai By Dubai Call Grils, #Dubai #Call #Girls Indian And Pakistan Call Girls In Dubai BY Dubai Call Girls, Dubai Call Girls, dubai call girls , DUBAI CALL GIRLS, Dubai Call Girls, dubai call girls , DUBAI CALL GIRLS, Best call “girls’ agency in Dubai (verified) by Uae Call “girls” in Dubai. Dubai Call “Girl’ , call-girls-dubai-al-barsha-marina-juemeirah-bur-dubai-deira-business-bay-al-nahda-jlt-jbr-jvc-jvt-downtown-al-jaddaf-## We are Currently @ offering the service in ~ Al areas~ Of Dubai ~ Like Abu Dhabi ~ Call “Girl’ In Dubai. %%$#% Call ‘’Girls’ Dubai, Call ‘Girls’’ In Deira, Deira Call ‘’Girl’ In Business bay, Business Bay Call ‘Girl’’ Dubai, Dubai Call ‘Girl’s’,# Dubai Call ‘Girls’ Agency,$ Dubai Call ‘’Girls’ Service, Dubai Independent Call ‘’Girls’, Dubai Model Call ‘’Girls’, Dubai VIP Call ‘’Girls’,& Indian Dubai Call ‘’Girls’, Pakistani Dubai Call ‘’Girls’,~ Russian Dubai Call ‘’Girls’,* Indian {Call ‘’Girls’} In Dubai, Independent Call ‘’Girls’ in Dubai, [Call ‘Girls’’] Services In Dubai, Dubai ‘’Escorts’, ‘’Escorts’’ In Dubai, Dubai ‘’Escort’’ Service, ‘’Escort’’ Service In Dubai, Indian ‘’Escort’’ In Dubai, ‘’Escorts’, ‘’Escort, Service, ‘Outcall, Indian, Dubai,

Indian Call “Girl’ in Abu Dhabi, Pakistani Call “Girl’ in Bur Dubai, JBR Call “Girl’ in Dubai, JLT Call “Girl’ in Al Karama, JVC Call “Girl’ in Bur Dubai Call “Girl’ in Dubai, Pakistani Call “Girl’ in Abu Dhabi, Call “Girl’ Service in al jaddaf Dubai, Deira Call “Girl’ in Al Barsha, stream Call “Girl’ in DIP, Pakistani Call “Girl’ in Al Barsha, Al Nahda Call “Girl’ in Marina, best Call “Girl’ in al ain Al Ain, Lavish Call “Girl’ in Silicon Oasis, charming Call “Girl’ Palm Jumeirah, beautiful Call “Girl’ Al Barsha Heights, famous Call “Girl’ Sheikh Zyed Road Dubai, high class Call “Girl’ Jumeirah Lakes Towers, cute Call “Girl’ in Business Bay, happy ending Call “Girl’ Discovery Gardens, Call “Girl’ Downtown Call “Girl’ Emirates Hills Call “Girl’ Call “Girl’ in Burj Khalifa, Call “Girl’ Service in Abu Dhabi Creek, Bur Juman Call “Girl’ in Dubai Media City, gracias Call “Girl’ Jumeirah Beach Residence, chika Call “Girl’ Agency, Al Qusais Call “Girl’ Al Quoz Call “Girl’ Al meena Call “Girl’ Al Rowdah Call “Girl’ Al Sufouh Call “Girl’ Al Rashidiya Call “Girl’ Desert Safari Call “Girl’ Oud Metha Call “Girl’ Al Jaffiliya Call “Girl’ Al Satwa Call “Girl’ Al Ras Call “Girl’ Burjuman Call “Girl’ Al Tawar Call “Girl’ Industrial Area Call “Girl’ Al Ramtha Call “Girl’ Al Sabkha Call “Girl’ Al Jerf Call “Girl’ Al Alia Call “Girl’ Al Heliow Call “Girl’ Al Gitanah Call “Girl’ Al Lebsa Call “Girl’ Ghub Call “Girl’ Al Ghail Call “Girl’ Al Shinouf Call “Girl’ AL Zubair Call “Girl’ AL Zahya Call “Girl’ AL Hamidiya Call “Girl’ Free zone Call “Girl’ AL Mirgab Call “Girl’ Dasman Call “Girl’ Al Majaz Call “Girl’ Hor Al Anz Call “Girl’ Al Murar Call “Girl’ Al Mankhool Call “Girl’ Al Bada Call “Girl’ Al Karama Call “Girl’ Jebel Ali Call “Girl’ Academic City Call “Girl’ Al Maktoum Call “Girl’ International City Call “Girl’ Khalifa City Call “Girl’ Sports City Call “Girls

, Umm Suqeim Call Girl In Dubai by Dubai Call Girls, Al Quoz Call Girl In Dubai Dubai Call Girls, DIP Call Girl In Dubai Dubai Call Girls, Damac Hills Call Girl In Dubai Dubai Call Girls, Qudra Call Girl In Dubai Dubai Call Girls, Arabella Call Girl In Dubai Dubai Call Girls, Mudon Villas Call Girl In Dubai Dubai Call Girls, Remraam Call Girl In Dubai Dubai Call Girls, Arabian Ranches Call Girl In Dubai Dubai Call Girls, Motor City Call Girl In Dubai Dubai Call Girls, JVC Call Girl In Dubai Dubai Call Girls, Al Barsha South Call Girl In Dubai Dubai Call Girls, Al Barsha Call Girl In Dubai by Dubai Call Girls, Tecom Cute Call Girl In Dubai by Dubai Call Girls, Barsha Heights Call Girl In Dubai by Dubai Call Girls, Al Sufouh Call Girl In Dubai by Dubai Call Girls, Palm Jumeirah Call Girl In Dubai by Dubai Call Girls, Ghadeer Call Girl In Dubai by Dubai Call Girls, Grand Plaza Call Girl In Dubai by Dubai Call Girls, The Greens Call Girl In Dubai by Dubai Call Girls, Emirates Hills Call Girl In Dubai by Dubai Call Girls, Internet City Call Girl In Dubai by Dubai Call Girls, Media City Call Girl In Dubai by Dubai Call Girls, Marina Call Girl In Dubai by Dubai Call Girls, maxican ladies for full night in JBR Dubai , Indian ladies for full night in Al Barsha Dubai , Inglis Call Girls In Al Qasimia By Sharjah Call Girls, Full Night Call Girl In Sharjah By Sharjah Call Girls, Chubby Call Girls In Al Jaffiliya By Dubai Call Girls, Gorgeous Call Girls In Al Qusais By Dubai Call Girls, Awesome Call Girls In Al Fahidi By Dubai Call Girls, Lavish Call Girls In Al Karama By Dubai Call Girls, Stream Call Girls In The Villas By Dubai Call Girls, Stylish Call Girls al Barari By Dubai Call Girls, Chines Call Girl Production City By Dubai Call Girl, Maxican Call Girls In JBR By Dubai Call Girls, American Call Girls In JLT By Dubai Call Girls, Lovely Call Girls In Business Bay By Dubai Call Girls, Brazilian Call Girls In al Nahda By Dubai Call Girls, Russian Call Girls In Deira By Dubai Call Girls, Turkish Call Girls In Bur Dubai By Dubai Call Girls, Cute Call Girls In Internet city By Dubai Call Girls, Pakistani Call Girl In Media city By Dubai Call Girls, Indian Call Girls In Al Saffa By Dubai Call Girls, Call Girls In Trade Center Dubai By Dubai Call Girls, Call Girls In Down Town Dubai By Dubai Call Girls, Call Girls In DIP Dubai By Dubai Call Girls, Call Girls In Dubai By Dubai Call Girls, Call Girls In Reem Villas Dubai By Dubai Call Girls, Call Girls In rem raam Dubai By Dubai Call Girls, Call Girl In Arabian Ranches Dubai By Dubai Call Girl, Call Girls In Damac Hills Dubai By Dubai Call Girls, Call Girls In Mudon Villas Dubai By Dubai Call Girls, Call Girls In Motor City Dubai By Dubai Call Girls, Call Girls In Silicon Oasis Dubai By Dubai Call Girls, Girls Call In Academic city Dubai By Dubai Call Girls, Girls Call In Al Warqa Dubai By Dubai Call Girls, Girls Call In Mirdif Dubai By Dubai Call Girls, Girls Call In Marina Dubai By Dubai Call Girls, Girls Call In Bur Dubai By Dubai Call Girls, #Girls #Call In #Al #Barsha #By #Dubai #Call #Girls, #happy ending Call Girls In Trade Center #Dubai , #Sports #city #Dubai #call #Girls Turkish Call Girls in Dubai By Dubai Call Grils, #Dubai #Call #Girls Indian And Pakistan Call Girls In Dubai BY Dubai Call Girls, Dubai Call Girls, dubai call girls , DUBAI CALL GIRLS, Dubai Call Girls, dubai call girls , DUBAI CALL GIRLS, Best call “girls’ agency in Dubai (verified) by Uae Call “girls” in Dubai. Dubai Call “Girl’ , call-girls-dubai-al-barsha-marina-juemeirah-bur-dubai-deira-business-bay-al-nahda-jlt-jbr-jvc-jvt-downtown-al-jaddaf-## We are Currently @ offering the service in ~ Al areas~ Of Dubai ~ Like Abu Dhabi ~ Call “Girl’ In Dubai. %%$#% Call ‘’Girls’ Dubai, Call ‘Girls’’ In Deira, Deira Call ‘’Girl’ In Business bay, Business Bay Call ‘Girl’’ Dubai, Dubai Call ‘Girl’s’,# Dubai Call ‘Girls’ Agency,$ Dubai Call ‘’Girls’ Service, Dubai Independent Call ‘’Girls’, Dubai Model Call ‘’Girls’, Dubai VIP Call ‘’Girls’,& Indian Dubai Call ‘’Girls’, Pakistani Dubai Call ‘’Girls’,~ Russian Dubai Call ‘’Girls’,* Indian {Call ‘’Girls’} In Dubai, Independent Call ‘’Girls’ in Dubai, [Call ‘Girls’’] Services In Dubai, Dubai ‘’Escorts’, ‘’Escorts’’ In Dubai, Dubai ‘’Escort’’ Service, ‘’Escort’’ Service In Dubai, Indian ‘’Escort’’ In Dubai, ‘’Escorts’, ‘’Escort, Service, ‘Outcall, Indian, Dubai,

Indian Call “Girl’ in Abu Dhabi, Pakistani Call “Girl’ in Bur Dubai, JBR Call “Girl’ in Dubai, JLT Call “Girl’ in Al Karama, JVC Call “Girl’ in Bur Dubai Call “Girl’ in Dubai, Pakistani Call “Girl’ in Abu Dhabi, Call “Girl’ Service in al jaddaf Dubai, Deira Call “Girl’ in Al Barsha, stream Call “Girl’ in DIP, Pakistani Call “Girl’ in Al Barsha, Al Nahda Call “Girl’ in Marina, best Call “Girl’ in al ain Al Ain, Lavish Call “Girl’ in Silicon Oasis, charming Call “Girl’ Palm Jumeirah, beautiful Call “Girl’ Al Barsha Heights, famous Call “Girl’ Sheikh Zyed Road Dubai, high class Call “Girl’ Jumeirah Lakes Towers, cute Call “Girl’ in Business Bay, happy ending Call “Girl’ Discovery Gardens, Call “Girl’ Downtown Call “Girl’ Emirates Hills Call “Girl’ Call “Girl’ in Burj Khalifa, Call “Girl’ Service in Abu Dhabi Creek, Bur Juman Call “Girl’ in Dubai Media City, gracias Call “Girl’ Jumeirah Beach Residence, chika Call “Girl’ Agency, Al Qusais Call “Girl’ Al Quoz Call “Girl’ Al meena Call “Girl’ Al Rowdah Call “Girl’ Al Sufouh Call “Girl’ Al Rashidiya Call “Girl’ Desert Safari Call “Girl’ Oud Metha Call “Girl’ Al Jaffiliya Call “Girl’ Al Satwa Call “Girl’ Al Ras Call “Girl’ Burjuman Call “Girl’ Al Tawar Call “Girl’ Industrial Area Call “Girl’ Al Ramtha Call “Girl’ Al Sabkha Call “Girl’ Al Jerf Call “Girl’ Al Alia Call “Girl’ Al Heliow Call “Girl’ Al Gitanah Call “Girl’ Al Lebsa Call “Girl’ Ghub Call “Girl’ Al Ghail Call “Girl’ Al Shinouf Call “Girl’ AL Zubair Call “Girl’ AL Zahya Call “Girl’ AL Hamidiya Call “Girl’ Free zone Call “Girl’ AL Mirgab Call “Girl’ Dasman Call “Girl’ Al Majaz Call “Girl’ Hor Al Anz Call “Girl’ Al Murar Call “Girl’ Al Mankhool Call “Girl’ Al Bada Call “Girl’ Al Karama Call “Girl’ Jebel Ali Call “Girl’ Academic City Call “Girl’ Al Maktoum Call “Girl’ International City Call “Girl’ Khalifa City Call “Girl’ Sports City Call “Girl’

Being an enthusiast of women I examined many call “Girl’ in the prior 6 months but never got that much pleasure from anyone. I’m facing challenges in my own relationship that is the reason I become close to such “Girl’ but when you cannot get peace even paying for women that thing hurts more. I chose This call “Girl’ agency and tried one of their Indian call “Girl’ she gave me real comfort and after one week of that service, I chose another Pakistani call “Girl’ and again then Russian. so overall my practice was magnificent. The price is also moderate per hour. The plus point is the “Girl’ comes instantly to your location doesn’t matter you are in Sharjah or Ajman or bur dubai or al Barsha or abu Dhabi or Deira or any area she comes undeviatingly to your hotel room. Definitely recommend the call “Girl’ agency.

A nutshell review for Hot call “Girl’ in dubai. MY experience was superb with them this is the only recommended call “Girl’ service in dubai with verified call “Girl’. I am using their services from past 6 months they never ever disappointed me in any way

---
## [afirpo/tgstation](https://github.com/afirpo/tgstation)@[0be45dcd65...](https://github.com/afirpo/tgstation/commit/0be45dcd6534244532e652564976bab13a3d8bdb)
#### Sunday 2023-11-05 17:18:04 by John Willard

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
## [Aikya-004/Cake-Ordering-small-business](https://github.com/Aikya-004/Cake-Ordering-small-business)@[1c654bdb1e...](https://github.com/Aikya-004/Cake-Ordering-small-business/commit/1c654bdb1e746882d3a10d3e4437c65ba6d49c4b)
#### Sunday 2023-11-05 17:54:29 by Aikya-004

Add files via upload

Cake Ordering Website:

Our cake ordering website is built with a modern tech stack consisting of HTML, CSS, and JavaScript. We provide a seamless and delightful online experience for customers to order their dream cakes. With a user-friendly interface powered by HTML, elegant and responsive designs using CSS, and interactive features enhanced by JavaScript, you can easily customize your cake, view pricing, and place orders with just a few clicks. Enjoy a smooth and visually appealing ordering process on our platform.

---
## [elunna/hackem](https://github.com/elunna/hackem)@[ece38e6a5e...](https://github.com/elunna/hackem/commit/ece38e6a5e07ea45e1b92e36bf60c3d03251fd3d)
#### Sunday 2023-11-05 17:56:33 by Erik Lunna

Phoenix egg tweaks. In the spirit of making phoenixes a recurring force to be reckoned with, they will hatch if the player attempts to eat, bury, or confine them in a container. In the previous commit, I allowed their eggs to be canceled, but I modified the chance to roll against the innate MR of the phoenix - so there is now only a 60% chance of success when trying to cancel. Dipping a phoenix egg in a potion of amnesia will always sterilize the egg however.

Polymorph needed to be addressed as well, because one could just zap a phoenix with polymorph and be rid of the pest. So now, when a phoenix doesn't naturally resist a polymorph, it will violently resist and explode, always reverting to it's egg form. This also entailed protecting phoenix eggs from polymorph, because without that protection, the polymorph beam would always poly the egg immediately after the phoenix exploded.

Lastly, in order to avoid some weird philosophical issues and gameplay paradoxes, I added the NOPOLY tag to the phoenix so the player can never take their form.

Thanks to Noisytoot for inspiring these ideas with the observation that phoenix eggs could simply be placed in a container (similar to zombie corpses). Phoenixes should have a special place in Hack'EM so they are revered and despised, plus they add significant value to potions of amnesia.

---
## [selliott512/freedoom](https://github.com/selliott512/freedoom)@[9ea70e75de...](https://github.com/selliott512/freedoom/commit/9ea70e75de134e0922ed4120e05721f73dd2b097)
#### Sunday 2023-11-05 17:58:28 by mc776

levels: various QOL fixes.

Generally there should be nothing *necessary to finish a level* that requires any of:
- straferunning;
- extremely sensitive timing that could softlock you if you're on keyboard, lagging in multiplayer or have motor issues;
- checking only for a sound cue that something has happened;
- remembering how to distinguish two visually nearly identical areas; or
- backtracking to a previous area on the map that you had previously been given no reason to revisit.

I haven't caught all of them by any stretch of the imagination but it's a start.

Also some regular minor fixes.

E1M9
- Fixed some textures around the big blue-trimmed lift and removed an extraneous use line that triggered a faraway lift for no reason.
- The red key bridge lowerable section is now textured differently from the rest of the bridge.

E3M5
- Teleporter platform to get back up to the catwalk from the northeastern blood maze is now clearly marked as having a switch, as it is a mandatory progression rather than a secret.

E4M8
- Got rid of some fake contrasts on the noodles at the start.
- Added a radsuit for the northwest switch. While it is possible to avoid damage even without straferun, unless you've got a tic counter display and can time it to the damage interval this is basically RNG.
- The water flat on top of the lowering wall in the east was very, very noticeable. The switch is now stepped on instead of hit. (Not too sure if the secret isn't *too* obscure now...)
- Removed asymmetrical doortrak on the slime bridge on the southeastern piston switch.
- The linedefs of said slime bridge pit are flipped so a deathmatch opponent trying to grab the berserk in there is not magically immune to rocket blasts. (see #996)
- Realigned the four pistons by the gate to the starship. They also reveal moving parts when activated - not nearly as good as the crushers on the original DI, but better than nothing.
- Made the southern walls use PLAT1 to make it more obvious that those walls will lower later (with the added bonus that they match the four pistons).
- The southern light bronze area now has a strip to guide the player towards the switch in case they lose track of their direction while fighting monsters and forget to explore inside that area, as well as to better distinguish it from the southeast.
- The gate threshold to the southern light bronze area now matches that of the pre-opened southeast.
- There is now actually a threshold where you can tell where the starport ends and the ship begins.
- The two light bronze areas are a bit too similar-looking. Added a few health boosts so the player can spot/be attacked by them and know this is an unexplored area.

Map11
- The lift going down into the yellow key room requires a switch that is out of sight from the lift itself, which is not clearly marked as a lift to begin with. The only real way to realize what's going on if you don't already know about the lift is to locate the sound and immediately turn to investigate before the lift comes back up. I thought this was annoying when I first did my big overhaul of this map, but ultimately left the basic mechanism alone out of an abundance of caution; however, with the recent discussion of accessibility in the proposed changes to the documentation I'm revisiting this. That upper switch now lowers a wall to reveal the lift which is triggered by a walk line.
- The lower far switch on that same lift was actually literally *impossible* to make on keyboard and no straferun (and no vanilla wallbounce exploit), even if I change it to a regular lift instead of fast. This is completely unacceptable for something necessary to progression (rather than an obscure secret). The lower switches are now permanent repeatable floor-lowerers, while the line crossing from the lift into the lower chamber is a permanent repeatable floor-raiser, with the line crossing into the lift from above being a simple lift line.
- Retextured the stairs out of the water in the eastern branch so it's not an unreadable mess of criss-crossing grey lines.
- Realigned the new skull switch texture in the skull room.

Map19
- One of the stealth worms was stuck in a burning barrel.
- Removed monster block flag on line 2083.
- Unmerged and remerged a few identical sectors to better match the intended sound travel.
- Flagged line 281 as a monster blocker. This allows the player to always be able to make the jump onto that bottom stair without being blocked by the octaminator.
- That octaminator is now a pain bringer in easy mode. The far end of that platform path is well outside the maximum vertical autoaim range in vanilla, which means that to actually hit the octaminator without up/down aiming you'd have to be on one of the later platforms - i.e., confined to a relatively narrow area with no cover *against an opponent that has seeker missiles*. The best way to solve this is to charge towards the octaminator as fast and as soon as possible with the SSG, minigun, or ripsaw+prayer to RNGsus that you'll get a good painlock. This is not the kind of tactic the sort of person who *needs* to play on easy will think to do, or could do while also being ready to sidestep if the octaminator fires at the wrong time.
- 347 and 249 are now also monster blockers, and the worms in that slime pit have been moved to the platform just behind the combat slug since they're awakened early on and that's where you'll first encounter them anyway.
- Replaced the teleport pad in the vertical platforming sequence with a lift, to minimize disorientation and going the wrong way. (In retrospect I probably could have just made the teleport destination face the pit you came in from, but the lift worked aesthetically better anyway.)
- A good chunk of that entire platforming area has been moved 8 units to the west so that things would align with the flat grid.
- Lines 307 and 309 are now also monster blockers. The worm that would be trapped between them is now moved further down the route and marked ambush.

Map20
- Removed the useless, misleading skull switch texture on the bars at the start.
- The door leading into the blue key arena needs no blue key; the door leading out needs a blue key. Both are marked with blue-light trim. Removed the blue lights on the first one.
- The lowering wall leading to the teleporter now uses a pipe texture.
- The door leading out of the giant quadruped arena now has a bright flickering light.
- Yellow key is another case of effectively-randomly-mandatory damage. Added a path.
- Same with the lava tunnel on the red key route.

Map25
- The silver lift near the river and shack is now activated by SW1GSTON switch right on the wall at eye level, rather than counterintuitively and invisibly recessed into additional sectors.
- The painlord ambush lift is now accessible after the encounter. A small health refill has been added there for easy and medium.

---
## [DarkoniusXNG/oaa](https://github.com/DarkoniusXNG/oaa)@[8b803f055a...](https://github.com/DarkoniusXNG/oaa/commit/8b803f055a6b77d621d083ed34ac72bb7a0e8928)
#### Sunday 2023-11-05 18:15:26 by Darko V

7.34d (OAA version) (#3574)

7.34d+
* ITEMS:
Battlefury recipe cost reduced from 450 to 300. (total gold cost of Battlefury is now the same as in normal DotA)
Eternal Shroud bonus strength increased from 14/19/29/44/64 to 14/24/39/59/84.
Greater Phase Boots active for ranged heroes will attack all units within your attack range + 150/175/200/225/250 range.
Greater Phase Boots bonus armor increased from 4/5/7/10/14 to 5/6/8/11/15.
Greater Phase Boots bonus HP rescaled from 200/400/600/800/1000 to 250/350/500/700/950.
Greater Power Treads bonus all stats increased from 5/10/15/20 to 10/15/20/25.
Linken's Sphere bonus damage increased from 10/15/25/40/60 to 10/20/35/55/80.
Shiva's Guard cooldown reduced from 27 to 27/26/25/24/23 seconds.
Shiva's Guard mana cost reduced from 100/125/150/175/200 to 100 at all levels.
Wind Waker recipe cost increased from 625 to 675.
* HEROES:
Dark Willow Bramble Maze duration increased from 7 to 8.5 seconds.
Disruptor Glimpse max damage increased at max level from 825 to 1100.
Disruptor Thunder Strike cooldown increased at OAA levels from 7/5 to 8/7 seconds.
Earth Spirit Level 20 Talent Boulder Smash Damage increased from 125 to 200.
Ember Spirit Fire Remnant cooldown reduced from 0.3 to 0.1 seconds.
Enigma Demonic Conversion health cost reduced from 75/100/125/150/175/200 to 70/80/90/100/110/120.
Legion Commander Moment of Courage lifesteal increased from 50/55/60/65/70/75% to 55/60/65/70/75/80%
Magnus Shockwave mana cost reduced from 60/70/80/90/100/110 to 60/65/70/75/80/85.
Marci Sidekick bonus damage increased from 6/12/18/24/48/96 to 6/12/24/48/96/144.
Marci Level 25 Talent +65 Sidekick damage reduced to +48.
Nature's Prophet Sprout cooldown increased at OAA levels from 8.5/8 to 9 seconds.
Phantom Assassin Blur cooldown increased from 12 to 14 seconds.
Phantom Assassin Coup De Grace deadly focus chance for Stiffling Dagger reduced from 40% to 25%.
Pugna Nether Blast bonus damage to bosses increased from 150% to 165%.
Riki Smoke Screen radius increased from 375 to 400.
Slark Essence Shift duration rescaled from 25/50/75/100/110/120 to 20/40/60/80/100/120 seconds.
Sniper Level 25 Talent +100 Attack Range replaced with +150 Take Aim Active Range bonus.
Spectre Dispersion damage reflected reduced at OAA levels from 22/25% to 21/22%.
Techies Blast Off cooldown reduced from 30 to 28/27/26/25/24/23 seconds.
Tinkerer Defense Matrix level 5 shield health increased from 750 to 1000.
Windranger Level 10 Talent -5% Powershot damage reduction improved to -10%.
Winter Wyvern Winter's Curse nearby allies check timer increased at OAA levels from 2.5 to 3.5/4.5 seconds.
Witch Doctor Death Ward cooldown increased from 60 to 90/80/70/65/60 seconds.

---
## [ComputerElite/QuestAppVersionSwitcher](https://github.com/ComputerElite/QuestAppVersionSwitcher)@[187bf03d1c...](https://github.com/ComputerElite/QuestAppVersionSwitcher/commit/187bf03d1cdc9443d5dedaa0c7fffd3d834256d4)
#### Sunday 2023-11-05 19:46:31 by ComputerElite

I have no idea, reorder stuff and shit and Quest 1 fixes hell yeah I'm going insane

---
## [j1philli/langchain](https://github.com/j1philli/langchain)@[dff24285ea...](https://github.com/j1philli/langchain/commit/dff24285eaf6d102b1ff913274d18379d8aeeb21)
#### Sunday 2023-11-05 19:50:00 by Nikhil Jha

Comprehend Moderation 0.2 (#11730)

This PR replaces the previous `Intent` check with the new `Prompt
Safety` check. The logic and steps to enable chain moderation via the
Amazon Comprehend service, allowing you to detect and redact PII, Toxic,
and Prompt Safety information in the LLM prompt or answer remains
unchanged.
This implementation updates the code and configuration types with
respect to `Prompt Safety`.


### Usage sample

```python
from langchain_experimental.comprehend_moderation import (BaseModerationConfig, 
                                 ModerationPromptSafetyConfig, 
                                 ModerationPiiConfig, 
                                 ModerationToxicityConfig
)

pii_config = ModerationPiiConfig(
    labels=["SSN"],
    redact=True,
    mask_character="X"
)

toxicity_config = ModerationToxicityConfig(
    threshold=0.5
)

prompt_safety_config = ModerationPromptSafetyConfig(
    threshold=0.5
)

moderation_config = BaseModerationConfig(
    filters=[pii_config, toxicity_config, prompt_safety_config]
)

comp_moderation_with_config = AmazonComprehendModerationChain(
    moderation_config=moderation_config, #specify the configuration
    client=comprehend_client,            #optionally pass the Boto3 Client
    verbose=True
)

template = """Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

responses = [
    "Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like 323-22-9980. John Doe's phone number is (999)253-9876.", 
    "Final Answer: This is a really shitty way of constructing a birdhouse. This is fucking insane to think that any birds would actually create their motherfucking nests here."
]
llm = FakeListLLM(responses=responses)

llm_chain = LLMChain(prompt=prompt, llm=llm)

chain = ( 
    prompt 
    | comp_moderation_with_config 
    | {llm_chain.input_keys[0]: lambda x: x['output'] }  
    | llm_chain 
    | { "input": lambda x: x['text'] } 
    | comp_moderation_with_config 
)

try:
    response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})
except Exception as e:
    print(str(e))
else:
    print(response['output'])

```

### Output

```python
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii Validation...
Running toxicity Validation...
Running prompt safety Validation...

> Finished chain.


> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii Validation...
Running toxicity Validation...
Running prompt safety Validation...

> Finished chain.
Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like XXXXXXXXXXXX John Doe's phone number is (999)253-9876.
```

---------

Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Anjan Biswas <84933469+anjanvb@users.noreply.github.com>

---
## [himadriut/Machine-Learning-AI](https://github.com/himadriut/Machine-Learning-AI)@[3158bf232d...](https://github.com/himadriut/Machine-Learning-AI/commit/3158bf232d0ce1ad9d9bf584fadcdadde7f88cd7)
#### Sunday 2023-11-05 19:52:26 by Himadri Samanta

Supervised Learning - Classification

INN Hotels Project
Context
A significant number of hotel bookings are called-off due to cancellations or no-shows. The typical reasons for cancellations include change of plans, scheduling conflicts, etc. This is often made easier by the option to do so free of charge or preferably at a low cost which is beneficial to hotel guests but it is a less desirable and possibly revenue-diminishing factor for hotels to deal with. Such losses are particularly high on last-minute cancellations.

The new technologies involving online booking channels have dramatically changed customers’ booking possibilities and behavior. This adds a further dimension to the challenge of how hotels handle cancellations, which are no longer limited to traditional booking and guest characteristics.

The cancellation of bookings impact a hotel on various fronts:

Loss of resources (revenue) when the hotel cannot resell the room.
Additional costs of distribution channels by increasing commissions or paying for publicity to help sell these rooms.
Lowering prices last minute, so the hotel can resell a room, resulting in reducing the profit margin.
Human resources to make arrangements for the guests.
Objective
The increasing number of cancellations calls for a Machine Learning based solution that can help in predicting which booking is likely to be canceled. INN Hotels Group has a chain of hotels in Portugal, they are facing problems with the high number of booking cancellations and have reached out to your firm for data-driven solutions. You as a data scientist have to analyze the data provided to find which factors have a high influence on booking cancellations, build a predictive model that can predict which booking is going to be canceled in advance, and help in formulating profitable policies for cancellations and refunds.

Data Description
The data contains the different attributes of customers' booking details. The detailed data dictionary is given below.

Data Dictionary

Booking_ID: unique identifier of each booking
no_of_adults: Number of adults
no_of_children: Number of Children
no_of_weekend_nights: Number of weekend nights (Saturday or Sunday) the guest stayed or booked to stay at the hotel
no_of_week_nights: Number of week nights (Monday to Friday) the guest stayed or booked to stay at the hotel
type_of_meal_plan: Type of meal plan booked by the customer:
Not Selected – No meal plan selected
Meal Plan 1 – Breakfast
Meal Plan 2 – Half board (breakfast and one other meal)
Meal Plan 3 – Full board (breakfast, lunch, and dinner)
required_car_parking_space: Does the customer require a car parking space? (0 - No, 1- Yes)
room_type_reserved: Type of room reserved by the customer. The values are ciphered (encoded) by INN Hotels.
lead_time: Number of days between the date of booking and the arrival date
arrival_year: Year of arrival date
arrival_month: Month of arrival date
arrival_date: Date of the month
market_segment_type: Market segment designation.
repeated_guest: Is the customer a repeated guest? (0 - No, 1- Yes)
no_of_previous_cancellations: Number of previous bookings that were canceled by the customer prior to the current booking
no_of_previous_bookings_not_canceled: Number of previous bookings not canceled by the customer prior to the current booking
avg_price_per_room: Average price per day of the reservation; prices of the rooms are dynamic. (in euros)
no_of_special_requests: Total number of special requests made by the customer (e.g. high floor, view from the room, etc)
booking_status: Flag indicating if the booking was canceled or not.

---
## [UBCFormulaElectric/Consolidated-Firmware](https://github.com/UBCFormulaElectric/Consolidated-Firmware)@[48ee00ec77...](https://github.com/UBCFormulaElectric/Consolidated-Firmware/commit/48ee00ec772e45a997365bdf7dadaecc117a31e9)
#### Sunday 2023-11-05 21:07:39 by Gus Tahara-Edmonds

Make CAN signal names unique (#1019)

### Summary
<!-- Quick summary of changes, optional -->

Currently CAN signal names are not unique. This is not a problem when
using PCAN or writing code, since signals are categorized by their CAN
message. However, this is not the case when uploading data to Influx,
since then only signal names are uploaded. This means that there are
weird conflicts between signals of the same name. For example, `State`
for the BMS and the DCM.

This PR changes so signal names are prefixed by their board, and then we
enforce all signals are unique across all boards. To avoid ridiculously
long CAN setters/getters in the firmware, only the signal name is now
used.

For example:
| | Before | After |

|-----------|--------------------------------------------|---------------------------------|
| Message | `BMS_Contactors` | `BMS_Contactors` |
| Signal | `AirPositive` | `BMS_AirPositive` |
| TX Setter | `App_CanTx_BMS_Contactors_AirPositive_Set` |
`App_CanTx_BMS_AirPositive_Set` |

The board name prefixes are also now added automatically to
messages/signals, so they've been removed from the `*_tx.json` files.

### Changelist 
<!-- Give a list of the changes covered in this PR. This will help both
you and the reviewer keep this PR within scope. -->

- Change `jsoncan` Python to support these changes
- Rename all signals
- Removed a few unused signals

Note: This diff is huge because of the autogenerated example code in
`jsoncan`. I should really remove this and add proper unit tests
instead.

### Testing Done
<!-- Outline the testing that was done to demonstrate the changes are
solid. This could be unit tests, integration tests, testing on the car,
etc. Include relevant code snippets, screenshots, etc as needed. -->

- [x] Validated on car

### Resolved Issues
<!-- Link any issues that this PR resolved like so: `Resolves #1, #2,
and #5` (Note: Using this format, Github will automatically close the
issue(s) when this PR is merged in). -->

### Checklist
*Please change `[ ]` to `[x]` when you are ready.*
- [x] I have read and followed the code conventions detailed in
[README.md](../README.md) (*This will save time for both you and the
reviewer!*).
- [x] If this pull request is longer then **500** lines, I have provided
*explicit* justification in the summary above explaining why I *cannot*
break this up into multiple pull requests (*Small PR's are faster and
less painful for everyone involved!*).

---
## [vvvv-vvvv/TerraGov-Marine-Corps](https://github.com/vvvv-vvvv/TerraGov-Marine-Corps)@[100f9fe420...](https://github.com/vvvv-vvvv/TerraGov-Marine-Corps/commit/100f9fe420ebd6a79782c316db484bf117b01fe1)
#### Sunday 2023-11-05 23:01:14 by LemonInTheDark

Converts del logging to proper json, using json objects instead of building a text file (#75636)

It's easier to parse, and makes more sense when you read it. This way
I'll never have to add yet another case to my parser for someone
changing where a space goes or something.

Moves qdel into its own category cause the old name looked ugly (yell if
this is dumb)
Added a bitfield to entries pulled from categories, adds a new flag that
enables pretty printing json lists.

IMPROVES my workflow

:cl:
server: del logging is now done by outputting to a json file again, but
this time we're using ACTUAL json and not just a big text string with
newlines and shit
/:cl:

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [Cheemaroni/Cheemaroni.github.io](https://github.com/Cheemaroni/Cheemaroni.github.io)@[20f6a874f5...](https://github.com/Cheemaroni/Cheemaroni.github.io/commit/20f6a874f50dd55ebff5be23676b8995e150fddf)
#### Sunday 2023-11-05 23:08:22 by Cheemaroni

A bunch of shit for music

I added the god awful 7.css with the tabs and then the header pngs for those tabs and ugh a moving text on the bottm adn then the two side gifs on the right

---

