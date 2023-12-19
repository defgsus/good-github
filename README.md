## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-18](docs/good-messages/2023/2023-12-18.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,492,950 were push events containing 3,702,139 commit messages that amount to 296,066,585 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 81 messages:


## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[fa8399334f...](https://github.com/ReturnToZender/ReturnsBubber/commit/fa8399334f9bc10abbf6ddf25b40e43b5363a9ae)
#### Monday 2023-12-18 00:01:36 by The-Sun-In-Splendour

Horrorform changeling salt PR (#859)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Now okay. I get it. It's huge, it's obvious, it's slow... I don't care
if it has more health and sustain than a tank spider or blobbernaut.
What I care is that it can fit into vents.

You can kill a changeling horror form with enough manpower. It's hard
but it's doable. But the fucking fact it can just... Ventcrawl into any
vent and if you don't see the tiny icon during the shitshow and push it?
Sorry but that is just absolute aids gameplay. Usually the monsters with
ventcrawl are pretty weak to make up for it. But not horrorling. I'm
sorry but if you have;

1. 750 health
2. 40 fucking damage swings (A double esword is 34 damage)
3. Passive, CONSTANT life regen
4. Lifesteal off dead bodies

You do **_not_** need ventcrawl. 

## Why it's good for the game

Do I really need to explain why having this almost unkillable machine be
able to ventcrawl to escape practically every situation because "teehee
forgot to weld vent in obscure location!" is bad for the game?

Yes. This is a salt PR.

:cl:
balance: Horror ling cannot ventcrawl anymore
/:cl:

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[2e656fba14...](https://github.com/ReturnToZender/ReturnsBubber/commit/2e656fba14e0b67086bb4d2eff59d6fa6748a55c)
#### Monday 2023-12-18 00:01:36 by Cursor

Grants the ability to open Clown slots once more. (#853)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Title. Skyrat disabled it because they hate fun. We don't.

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Say a Clown dies. Is arrested, or is just a bit shit.
What can you do?
Jackshit.
Pray, fax Clown Planet, but why wait on God or the Clown in the High
Castle when you can do it yourself?
This also let's Antags, or Clowns summon more friends. Assuming people
in the lobby wanna be a clown.

P.S. I commented out and unticked the Skyrat file for double safety.
Tried to just override it, didn't work. If you have a better idea for
this. You have the floor.

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
add: Clown slots are re-openable by royal decree. The incident between
Nanotrasen and King Honkington has been resolved.
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

---------

Co-authored-by: Waterpig <49160555+Majkl-J@users.noreply.github.com>

---
## [Ds1399/unbl0ck.github.io](https://github.com/Ds1399/unbl0ck.github.io)@[ac3796a356...](https://github.com/Ds1399/unbl0ck.github.io/commit/ac3796a3568c08638c2dc9e277842b03c10d1267)
#### Monday 2023-12-18 00:13:00 by Christian Santangelo

deleted. gone. dead. poof.

really fuckin buggy. github lfs too big for my brain, and its giving me a shit ton of errors when cloning.

---
## [jstanley0/advent-2023](https://github.com/jstanley0/advent-2023)@[474d0ffdae...](https://github.com/jstanley0/advent-2023/commit/474d0ffdae83e86ff28ecfaa93e08dd7c80276a5)
#### Monday 2023-12-18 00:33:12 by Jeremy Stanley

1

TypeScript sucks. So does Node. Apparently I hate myself.
Ruby is the only true langauge for this kind of thing.

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[e8cf56dcb2...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/e8cf56dcb2553c842abd7adf60a99b33d65ecfbe)
#### Monday 2023-12-18 00:43:54 by SkyratBot

[MIRROR] Roundstart AIs are positronic [MDB IGNORE] (#25679)

* Roundstart AIs are positronic (#80355)

## About The Pull Request

If you disassemble an AI which was in the round from the start it will
produce a Positronic Cube rather than an MMI with the brain of that
player's usual human character in it.

Also I made changes to a couple of feedback balloon alerts which would
always trigger a runtime when constructing or deconstructing an AI, this
was because balloon alerts have a small time delay before executing and
we deleted the AI mob or structure after trying to show a balloon alert
on them, so they'd never appear.

## Why It's Good For The Game

Honestly this is _mostly_ about vibes, it has annoyed me since AI
deconstruction was added that Nanotrasen AIs tend to actually be brains
in jars rather than AIs. Now they're artifical.
It does also mean that you can't deconstruct the AI and then put its
brain into a human body, which is similarly mostly bad because of vibes:
If you sign up as an AI I think you should be an AI or a cyborg even
after deconstruction.

It also universally looks really stupid when you deconstruct an AI and
it says it has the brain of Penelope Dreadful in there, like should I
expect them to start RPing as their normal character instead of the AI
they have been playing all round now?

## Changelog

:cl:
balance: Roundstart AIs are now made of positronic cubes, rather than
brains inside MMIs
/:cl:

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@ users.noreply.github.com>

* Roundstart AIs are positronic

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: John Willard <53777086+JohnFulpWillard@ users.noreply.github.com>

---
## [warpdragon/oaa](https://github.com/warpdragon/oaa)@[8b803f055a...](https://github.com/warpdragon/oaa/commit/8b803f055a6b77d621d083ed34ac72bb7a0e8928)
#### Monday 2023-12-18 00:55:47 by Darko V

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
## [FalloutFalcon/Shiptest](https://github.com/FalloutFalcon/Shiptest)@[5e4814b6cf...](https://github.com/FalloutFalcon/Shiptest/commit/5e4814b6cf77c20f3e730638e0fa7f896b10aaf6)
#### Monday 2023-12-18 01:22:19 by GenericDM

licorice (#2573)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
renames licorice ice cream
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
regardless of if it's a reference to a real brand or not, i doubt it was
added to /tg/ in good faith. regardless, the company would not have
survived the night of fire, and making it vague prevents people from
making cheap jokes
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

🆑
tweak: renames licorice ice cream
/🆑

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [EvilDragonfiend/tgstation](https://github.com/EvilDragonfiend/tgstation)@[81a7c75583...](https://github.com/EvilDragonfiend/tgstation/commit/81a7c75583f75f76d8487b88e63ebaf1402af85b)
#### Monday 2023-12-18 01:30:43 by necromanceranne

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
## [licoded/cs144-labs-2023](https://github.com/licoded/cs144-labs-2023)@[2581231bc6...](https://github.com/licoded/cs144-labs-2023/commit/2581231bc6b4833a8bca81ff0641569548dd216e)
#### Monday 2023-12-18 02:22:30 by licoded

lab3: tcp_receiver try-10the, successfully passed all TESTs

The Divine Move, God's One Move! Amazing!
When I want to give up temporarily, the surprise just occurs to me

---
## [MidoriWroth/tgstation](https://github.com/MidoriWroth/tgstation)@[39d9c45b4a...](https://github.com/MidoriWroth/tgstation/commit/39d9c45b4a7afc2a963de4249592a3d4ae6c4715)
#### Monday 2023-12-18 02:45:40 by san7890

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
## [MidoriWroth/tgstation](https://github.com/MidoriWroth/tgstation)@[08ab5d2731...](https://github.com/MidoriWroth/tgstation/commit/08ab5d27312d236593eabdb27fb23dccbf8283e6)
#### Monday 2023-12-18 02:45:40 by Mothblocks

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
## [theUnBurn/Onion](https://github.com/theUnBurn/Onion)@[c7694511f2...](https://github.com/theUnBurn/Onion/commit/c7694511f224fe469f97b98308a9dcfb6fb13917)
#### Monday 2023-12-18 03:00:28 by XK

FEAT: Update ScummVM Standalone to 2.9.0git (#1307)

## Overview
Update to scummvm 2.9.0 to include all updates & fixes to the scrollbars
in: https://github.com/scummvm/scummvm/pull/5472

<img
src="https://github.com/OnionUI/Onion/assets/47260768/89080ee6-124e-445a-a14d-b818e277e991"
width="400" alt="Run ScummVM_000"><img
src="https://github.com/OnionUI/Onion/assets/47260768/86848e29-a304-4c9e-ae1f-1c4d491d044a"
width="400" alt="Run ScummVM_001">

## To test

Testing GUI -> 640 x 480: 

- [x]  GUI can be freely scaled to its smallest size

Testing scrollbars:

- [x] Open global options -> Keymaps & observe a scrollbar is still
present

Downscaler can be tested by running BSword2.5. 
Audio has been handled differently so in this PR will also change the
launch scripts to preload libpadsp.so

## Build details
<details>

```markdown
Backend... miyoo (SDL 1.2.15), 16bit color, high resolution, TinyGL, savegame timestamp, HQ and Edge scalers, aspect ratio correction, Lua, virtual keyboard, ENet
WARNING: Disabling engine Hpl1 because the following dependencies are unmet: OpenGL with shaders
WARNING: Disabling engine Tetraedge because the following dependencies are unmet: libtheoradec
WARNING: Disabling engine The Watchmaker because the following dependencies are unmet: OpenGL (classic)

Engines (builtin):
    SCUMM [all games]
    Access
    ADL
    AGI
    AGOS [all games]
    Adventure Game Studio
    Sanitarium
    Lord Avalot d'Argent
    Beavis and Butthead in Virtual Stupidity
    Blade Runner
    The Journeyman Project 2: Buried in Time
    CGE
    CGE2
    Chamber
    Chewy: Esc from F5
    Cinematique evo 1
    Magic Composer
    Crab
    Cinematique evo 2
    Lost Eden
    Cryo Omni3D games [all games]
    Macromedia Director
    Dungeon Master
    Dragon History
    Blazing Dragons
    Drascula: The Vampire Strikes Back
    Dreamweb
    Escape From Hell
    Freescape
    Glk Interactive Fiction games
    UFOs
    Gobli*ns
    The Griffon Legend
    Grim [all games]
    Groovie [all games]
    Hades Challenge
    Hyperspace Delivery Boy!
    Hopkins FBI
    Hugo Trilogy
    Hypnotix Inc.
    In Cold Blood
    Illusions Engine
    The Immortal
    Kingdom: The Far Reaches
    Kyra [all games]
    Labyrinth of Time
    The Last Express
    Lilliput
    Lure of the Temptress
    MacVenture
    MADE
    MADS [all games]
    Might and Magic [all games]
    Mohawk [all games]
    Mortevielle
    mTropolis
    Mutation of JB
    Myst 3
    Nancy Drew
    Neverhood
    Nikita Game Interface
    Parallaction
    The Journeyman Project: Pegasus Prime
    Red Comrades
    Pink Panther
    Playground 3d: the testing and playground environment for 3d renderers
    Plumbers Don't Wear Ties
    The Prince and The Coward
    Private Eye
    Flight of the Amazon Queen
    SAGA [all games]
    SAGA2
    SCI [all games]
    The Lost Files of Sherlock Holmes
    Beneath a Steel Sky
    Sludge
    The Longest Journey
    Star Trek 25th Anniversary/Judgment Rites
    Mission Supernova
    Broken Sword
    Broken Sword II
    Broken Sword 2.5
    Teen Agent
    TestBed: the Testing framework
    Tinsel
    Starship Titanic
    3 Skulls of the Toltecs
    Tony Tough and the Night of Roasted Moths
    Toonstruck
    Touche: The Adventures of the Fifth Musketeer
    Trecision Adventure Module
    TsAGE
    Bud Tucker in Double Trouble
    Little Big Adventure
    Ultima [all games]
    V-Cruise
    Voyeur
    WAGE
    Wintermute [all games]
    Z-Vision

Engines Skipped:
    Hpl1
    Tetraedge
    The Watchmaker

WARNING: This ScummVM build contains the following UNSTABLE engines:
    Lord Avalot d'Argent
    Chamber
    Crab
    Lost Eden
    Dungeon Master
    Grim [Escape from Monkey Island]
    In Cold Blood
    The Immortal
    The Last Express
    Lilliput
    MacVenture
    MADS [MADS V2]
    Might and Magic
    Mohawk [Where in Time is Carmen Sandiego?]
    Mutation of JB
    Playground 3d: the testing and playground environment for 3d renderers
    Sludge
    Star Trek 25th Anniversary/Judgment Rites
    TestBed: the Testing framework
    Ultima [Ultima I - The First Age of Darkness]
    WAGE
    Wintermute [Wintermute3D]

Creating engines/engines.mk
Creating engines/detection_table.h
Creating engines/plugins_table.h
Creating config.h
Creating config.mk

```
</details>

---
## [polsevev/AdventOfCode](https://github.com/polsevev/AdventOfCode)@[cd9656d07f...](https://github.com/polsevev/AdventOfCode/commit/cd9656d07fbe755e660333c4c262f1bc7a94c78d)
#### Monday 2023-12-18 03:06:12 by polsevev

HOLY FUCKING SHIT, I USED THE SAME HASHMAP OVER AND OVER!

---
## [sevendark/langchain](https://github.com/sevendark/langchain)@[dff24285ea...](https://github.com/sevendark/langchain/commit/dff24285eaf6d102b1ff913274d18379d8aeeb21)
#### Monday 2023-12-18 03:38:57 by Nikhil Jha

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
## [StephenODea54/dstk](https://github.com/StephenODea54/dstk)@[ba4fe62da6...](https://github.com/StephenODea54/dstk/commit/ba4fe62da695a4785d4b0205d11c7d2dda210dbb)
#### Monday 2023-12-18 03:50:57 by Christopher Wetherill

Add DeleteStorageProvider method (#35)

Refs. #25

Does what it says on the tin. Normally we're in favor of just
archiving objects with an `is_archived` boolean in the database;
however, in this case dstk is not really the source of truth and
just reflects the state of an external system that we don't have
any control over. Add also that we're storing sensitive access keys
and folks don't always (though they should) have great S3 security
postures, we don't want to keep any keys to the blob storage kingdom
lying around if we don't need to. Worst case, a user can always
re-create a storage provider later on.

One thing that this PR does not consider is how we want to treat FK
references to objects that users have created against the to-be-deleted
storage provider. An option would be to cascade the deletion and just
nuke everything. We could alternately change the `NOT NULL` constraint
on the FK references and just zero them out for all impacted objects.
Although if we went that route, we'd need to make sure we displayed
a big, scary warning to users telling them that their shit is about
to irrevocably break if they continue with this definitely dangerous
action. And users always read warnings, right?

Ultimately I think the safest bet is probably going to be to soft-delete
things where we:

  1. Set an is_archived bit on the row;
  2. Overwrite or just NULL out the endpoint, region, keys, etc.;
  3. Propagate the archive action to affected objects;
  4. Hide this all behind a big, scary "type delete <storage provider ID>
     to continue" confirmation dialog that explains the Very-Bad-But-Not-Catastrophic
     Day you're about to have if you do this without understanding the
     consequences for any registered or deployed models and model versions

---
## [SyliusBot/Sylius](https://github.com/SyliusBot/Sylius)@[23b4abd530...](https://github.com/SyliusBot/Sylius/commit/23b4abd530ad3b985f4028dbeab869d004d9593f)
#### Monday 2023-12-18 04:03:44 by Jacob Tobiasz

minor #15646 [API][Admin] Allow using float for amount in tax rates (NoResponseMate)

This PR was merged into the 1.13 branch.

Discussion
----------

| Q               | A                                                            |
|-----------------|--------------------------------------------------------------|
| Branch?         | 1.13 |
| Bug fix?        | kinda                                                       |
| New feature?    | no                                                       |
| BC breaks?      | no                                                       |
| Deprecations?   | no |
| Related tickets | related #15616                      |
| License         | MIT                                                          |

It's hacky as hell; caused by [this bug](https://github.com/api-platform/core/issues/1647), the only other way of fixing it is a migration but that sucks by itself. I'm guessing there are more convoluted ways as well but that's too much pain for the gain.

Commits
-------
  [API][Admin] Allow using float for amount in tax rates

---
## [Contrabang/cmss13](https://github.com/Contrabang/cmss13)@[e7816d96c5...](https://github.com/Contrabang/cmss13/commit/e7816d96c5d1523337dec081bea0056fbc9189fc)
#### Monday 2023-12-18 04:11:09 by forest2001

Almayer AntiTheft measures. (#5100)

STOP STEALING SHIT
# About the pull request
Adds a subtype of reinforced hull for the Almayer that changes between
indestructible hull and normal reinforced wall after hijack.
Uses this wall type around uniform vendors, the separation wall in the
firing range and around engineering storage.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Having the engineering storage looted at round start is just silly
avoidance of the "don't deconstruct the whole ship without a reason"
rule.

# Testing Photographs and Procedure

I have verified that all works as intended, the walls cannot be harmed
prior to hijack, and shutters function as advertised.

# Changelog
:cl:
add: Added a new almayer hull type (heavy reinforced) which is
indestructible by normal means until after hijack collision.
add: Added a new subtype of shutter that automatically opens or closes
depending on security level.
maptweak: Maps both of the above around the engineering storeroom. Also
adds the walls between the firing ranges and around uniform vendors.
maptweak: Manual control button for shutters over engineering storage in
the CEs office.
code: Changes hijack structural changes (walls/windows/windoors/ladders)
to use signals.
/:cl:

---------

Co-authored-by: fira <loyauflorian@gmail.com>

---
## [Contrabang/cmss13](https://github.com/Contrabang/cmss13)@[5d957ce94e...](https://github.com/Contrabang/cmss13/commit/5d957ce94e398a102fdf16682b740e96df3e363e)
#### Monday 2023-12-18 04:11:09 by InsaneRed

Vanguard tweaks (#5174)

# About the pull request
This catches up vanguard to current gameplay as it was last changed
approximately 4 years ago


# Explain why it's good for the game
Currently Vanguard is supposed to be a frontlining tier 3 who dashes in
> stays in and gets some damage in and goes out (thats why the shield is
a thing) and you're supposed to be able to stay there because your
abilities (pierce and dash) resets your shield. But with the recent
addition of just more damage in general be it m56d, full auto mode or
just the amnout of extra damage you can receive from the front compared
4 years ago.

The strain currently struggles and is near useless other then the
occasional go in and lucky fling.

I've changed up the dash to reset your shield once you hit ONE person,
rather then two so that you dont instantly die while going in, the
shield is very situational as it will most likely decay before you can
even go in.

Listening to people who play vanguard, i've also increased the root to
2.5 seconds (this is buffed so when the prae has the shield) the marine
can still shoot back when they're rooted so i dont think the duration is
a big problem (this is going to be a test merge so i will be watching)

# Testing Photographs and Procedure
it just works

</details>


# Changelog

:cl:
balance: Vanguard dash now restores your shield if you hit ANYONE
instead of 2 people.
balance: Vanguard buffed root now roots you for 2.5 seconds, unbuffed
for 1 second
qol: Vanguard's pierce has now a hit sound for better feedback
/:cl:

---------

Co-authored-by: InsaneRed <prodexter31@outlook.comm>

---
## [opencontainers/runc](https://github.com/opencontainers/runc)@[8e8b136c49...](https://github.com/opencontainers/runc/commit/8e8b136c4923ac33567c4cb775c6c8a17749fd02)
#### Monday 2023-12-18 05:10:47 by Aleksa Sarai

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
## [Moribox/lobotomy-corp13](https://github.com/Moribox/lobotomy-corp13)@[0a75aef49d...](https://github.com/Moribox/lobotomy-corp13/commit/0a75aef49d6474eecc4996a25c1a40766ba18df8)
#### Monday 2023-12-18 05:22:09 by The Bron Jame Offical

Representative Update (#1695)

ITS REALLLLL.

K-corp ERT

begone Crit up

hello health booster

R-corp weapon researches

oh wow thats a lot of rabbit weapons

KIRIE WHY ARE THERE SO MANY

okay normal again, R-corp rep mains eatin good tonite

ancient ass code, reaping what we have sown.

oh for fucks sake

lore fixes

K-corp ERT

changes from Redacteds PR into relevant files

added K-corp spear sound

K-corp ERT comes with grenades that fabricate 3 K-Corp Drones

icon pain and suffeirng

Update lc13icons.dmi

---
## [Maybe-Anton/Shiptest](https://github.com/Maybe-Anton/Shiptest)@[d960193cdb...](https://github.com/Maybe-Anton/Shiptest/commit/d960193cdb07ccce873e22ade5c81be03e505018)
#### Monday 2023-12-18 05:52:59 by BluBerry016

{Icemoon, Ruin} The Crashed Holemaker (#2413)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds a brand-new - well, [new to
shiptest](https://cohost.org/bluwu016/post/885120-a-compilation-of-my) -
ruin to the Icemoon roster, focused on the service department.

It's flavored around being an *incredibly* old NT Spaceworks vessel
that's been carved in half and crashed - what's present only being the
fore of the ship. Being mainly service-focused, it's loot is pretty dry
~~as is it's sole threat.~~
If more current-day mappers/balance-heads have any words about how to
fluff out either of those pools a bit more with the screenshots below,
lemme know. I'll listen well.

(Notarized loot summary removed as updating it was a pain in the ass,
lmao.)

It strikes me as leaning on the underwhelming side from looking at the
other ruins present here but we'll. See? I suppose? It's good practice
for me in the whole, "making something I have memorized and that looks
good normally look sicker ruined".

<details><summary>Pictures (All but SDMM Outdated)</summary>
<p>

Ignore that there's no rust, the firelocks are open here, and some
stuff's knocked around, I was testing it prior to me tacking the rust on
and took pics after running around it in-person.


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/51a3cc54-1727-4241-9592-639f892621bf)


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/580e39fe-bbf9-481f-aff8-cc25f860638d)

StrongDMM View:

![2023-11-09 15 02
20](https://github.com/shiptest-ss13/Shiptest/assets/50649185/5b94af63-d2d8-42bd-a823-0d300d66191f)

</p>
</details> 
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This isn't what I intended to do when I was like, "oh yeah, I have a
goofy ahh downstream out of boredom, ya'll want some of our better
ships" but w/e here it is anyways. Ya'll need ruins. I made (another)
ruin.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A new icemoon ruin has been added, should you be in need of service
department goodies.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: BluBerry016 <50649185+unit0016@users.noreply.github.com>

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[b7b0932c4b...](https://github.com/jlsnow301/tgstation/commit/b7b0932c4b5b3d4f9386b6dce514ee1ba3e25a05)
#### Monday 2023-12-18 06:01:19 by distributivgesetz

Delamination variants are now locked in after the countdown is reached (#80324)

## About The Pull Request

Does what it says on the tin.
## Why It's Good For The Game

This effectively changes one and only one thing: 

The "All Within Theoretical Limits" achievement is easier/fairer to get
with this. Previously, if you edged a crystal with the gas composition
method to get a resonance cascade, you had to make sure that your gas
composition stayed until it left the explosion point, which made the
achievement extremely finnicky and unfun to get this way. Regular
delaminations won't really be affected, because yeah. It's at the
explosion point. What are you going to do about it?

This makes the achievement easier to cheese, but honestly, in my opinion
as person who added the achievement, meh. If people feel like this isn't
good for the achievement, say something in the comments.

Closes #79528

## Changelog
:cl:
balance: Delamination variants no longer change once the explosion point
has been reached.
/:cl:

---
## [EyeOfProvidence7/life-of-game](https://github.com/EyeOfProvidence7/life-of-game)@[36a614c596...](https://github.com/EyeOfProvidence7/life-of-game/commit/36a614c596f9dc5164d8c2e77aa1a5e9a33272b7)
#### Monday 2023-12-18 06:24:15 by EyeOfProvidence7

holy fucking shit, its TRANSPILING. Blue canvas is present once again, but not from index.html anymore. Pog.

---
## [acarrasco/advent_of_code](https://github.com/acarrasco/advent_of_code)@[c93d14a054...](https://github.com/acarrasco/advent_of_code/commit/c93d14a054e8015257e533355101b7f7e87b21cc)
#### Monday 2023-12-18 06:24:48 by Alejandro Carrasco

Year 2023 - day 18

I "brute-forced" the first part doing a flood-fill algorithm. That
approach obviously wouldn't work for part 2.

Luckily I remembered that one of my colleagues' friends solved day 10
(the pipes problem) using Gauss' formula (a.k.a. the shoelace formula).
The only tricky bit was to take into account that we are using full
blocks and not discrete points as the polygon boundary, so we need to
add the perimeter (half of it, because half of it is facing inwards).

I am still thinking about the odd + 1 to the area formula... I believe
it is where the initial and final square overlap when closing the loop,
but it is a bit early to think straight.

      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 18   00:25:40   1234      0   00:38:10    539      0

---
## [ky-1/tictac](https://github.com/ky-1/tictac)@[93746e9223...](https://github.com/ky-1/tictac/commit/93746e92235963ddc2fd708e95b48fe1b7827203)
#### Monday 2023-12-18 06:39:27 by ky-1

HOLY FUCKING SHIT

took so goddamn long to do this thank u subrocks 2009

---
## [RaShCat/Skyrat-tg](https://github.com/RaShCat/Skyrat-tg)@[4d51b2748d...](https://github.com/RaShCat/Skyrat-tg/commit/4d51b2748d036749c7d43c2d997c268bb2205579)
#### Monday 2023-12-18 07:16:50 by SkyratBot

[MIRROR] [NO GBP] Fixing elevation furthermore [MDB IGNORE] (#25414)

* [NO GBP] Fixing elevation furthermore (#80099)

## About The Pull Request
fixes #80059
fixes #80085.

The tram transportation doesn't use `forceMove()`, instead it just
changes the location of the objects directly. What's more, it doesn't
call `oldloc.Exited()` or `loc.Entered()` but only for areas. The
abstract exited/entered signals are from `Moved()` though, which is
called.

https://github.com/tgstation/tgstation/blob/df4bc6d948576a2ec32a90c23c93ec90e54e3933/code/modules/transport/transport_module.dm#L519-L527

About beds, well, I just happened to put a minus symbol where it
shouldn't be.

## Why It's Good For The Game
Truly one of the fuckups of the year. Now tested. I'll make a unit test
later.

## Changelog

:cl:
fix: Fixed some oopsie whoopsie with elevation, trams and beds causing
people to visually ascend or descend to heaven or hell.
/:cl:

* [NO GBP] Fixing elevation furthermore

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Byyyrd/Info-Projekt-Q1](https://github.com/Byyyrd/Info-Projekt-Q1)@[5a4dea30f7...](https://github.com/Byyyrd/Info-Projekt-Q1/commit/5a4dea30f7596e1d0641b5108ff103a92f72e60b)
#### Monday 2023-12-18 07:19:10 by Realnr

Maxim is a stupid piece of shit, pls help him. He's a fucking retard - quote by Maxim

---
## [baraah-othman/AI_Shopping_Assistant](https://github.com/baraah-othman/AI_Shopping_Assistant)@[fd8c21a413...](https://github.com/baraah-othman/AI_Shopping_Assistant/commit/fd8c21a413447b29aad7d95ad44a10685ebe4fea)
#### Monday 2023-12-18 09:21:14 by Baraah Othman

README.md

Welcome to a retail revolution where artificial intelligence meets your shopping needs! In a world where technology is transforming every aspect of our lives, my project emerges as a beacon of innovation in the realm of shopping assistance. Imagine a virtual shopping companion that understands your preferences, guides your choices, and enhances your overall experience—this is the future I envisioned and brought to life.

Shopping can be overwhelming, with countless options and considerations. Traditional methods of shopping assistance, while helpful, lack the personalized touch needed to truly cater to individual preferences. Enter the era of AI-driven shopping assistants, a domain where my project seeks to shine.

Models and Algorithms: At the core of the approach is RAG, a state-of-the-art language model, Retrieval-augmented generation (RAG) is a technique for enhancing the accuracy and reliability of generative Al models with facts fetched from external sources. In other words, it fills a gap in how LLMs work. Under the hood, LLMs are neural networks, typically measured by how many parameters they contain. Meta Al researchers introduced Retrieval Augmented Generation (RAG) to address such knowledge-intensive tasks. RAG combines an information retrieval component with a text generator model.

Document Preparation: Our journey begins with the preparation of documents, where each product's essential details are encapsulated. For every product in our dataset, a unique document is created, incorporating information such as title, description, subcategory, category, gender, prodcategory, and brand. This forms the foundation upon which our language model will operate, ensuring a rich understanding of each product.

Setting the Stage: OpenAI and Embedding With the documents ready, we dive into the realm of language models. We employ the formidable GPT-3.5 Turbo from OpenAI, setting the stage for advanced language understanding. Additionally, we utilize the OpenAIEmbedding to enhance the representation of our textual data, ensuring a comprehensive grasp of the underlying semantics.

Node Parsing for Enhanced Understanding: To facilitate effective information retrieval, we implement a node parser with a meticulous approach to text splitting. This process involves chunking the text, ensuring a balanced distribution for optimal comprehension. This step is crucial for preparing the textual data for input into our language model.

Building the Index The culmination of our efforts takes shape in the creation of a Vector Store Index. This index serves as the bedrock for efficient querying and retrieval of information. The carefully crafted documents, coupled with advanced language understanding and parsing techniques, form an index that is ready to respond to user queries. and of course Querying the Index. Returning matching products: using functions to filter the gender based on user query,by embedding the query and searching for matching products from the dataset using the cosine similarity

Thank you for stopping by my project !

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[7e60a62393...](https://github.com/treckstar/yolo-octo-hipster/commit/7e60a623939ed6af9826f005a40174f3337dd896)
#### Monday 2023-12-18 09:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [sabarop/kernel_xiaomi_sdm660](https://github.com/sabarop/kernel_xiaomi_sdm660)@[779e710fb4...](https://github.com/sabarop/kernel_xiaomi_sdm660/commit/779e710fb4bfdb07508ed82bb95c3add0f5f8de4)
#### Monday 2023-12-18 09:24:28 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: celtare21 <celtare21@gmail.com>
Signed-off-by: sohamxda7 <sensoham135@gmail.com>
Signed-off-by: Oktapra Amtono <oktapra.amtono@gmail.com>
Signed-off-by: clarencelol <clarencekuiek@icloud.com>
Signed-off-by: pix106 <sbordenave@gmail.com>
Signed-off-by: ImSpiDy <SpiDy2713@gmail.com>

---
## [ArchiFleKs/scripts](https://github.com/ArchiFleKs/scripts)@[5562496e3b...](https://github.com/ArchiFleKs/scripts/commit/5562496e3b38f40098b36d62f6dc16d296014c71)
#### Monday 2023-12-18 09:41:20 by gitmachtl

New release: Light-Mode, Sub-Handle and Virtual-Handle, Conway-Era

Rendered Release-Notes: https://github.com/gitmachtl/scripts/releases/tag/Light-Mode

## New Feature - LIGHT-Mode, running the SPO Scripts without a local node

This is an exciting new feature in the SPO Scripts. Before we had two operational modes, Online-Mode and Offline-Mode. Now we have an additional one, the Light-Mode.

So whats this Light-Mode? If you switch the scripts into Light-Mode - see below how easy it is to do so - you have the advantage of being online with your machine, but you don't need a running synced cardano-node. You can switch between Networks Mainnet, PreProd and PreView within seconds.

This comes is handy if you just don't want to install and run a cardano-node, if you don't have the space for the database or if you just don't have the time to wait for a resync.

All transactions are of course generated and signed locally, but the queries and the transmit is done via online APIs like Koios.

How do you switch between Online-, Light- and Offline-Mode?
Thats simple, you just change a single entry in the 00_common.sh, common.inc or $HOME/.common.inc config-file: image

workMode="online": Scripts are working in Online-Mode aka Full-Mode. A locally running and synced cardano-node is needed.
workMode="light": Scripts are working in Light-Mode. No cardano-node needed.
workMode="offline": Scripts are working in isolation and completely offline. No cardano-node needed.

You can do ALL OPERATIONS in Light-Mode now! ?? Currently supported Chains are Mainnet, PreProd and PreView. You can switch between chains in seconds, and if you put a different common.inc file into your folders, you can run them all in parallel too. I also wanna thank Holger from Cardano24, because i am hosting the Online-Version of the Protocol-Parameters JSON files on his distributed Server-Platform uptime.live, thank you! The JSON files are updates every 10 mins to make them available in Light-Mode.

If you have an Online/Offline Workflow, you can use the Online machine in Light-Mode, and your Offline machine is still offline of course.

## New Feature - $Sub-Handle & $Virtual-Handle support for $Adahandles ??

Complete support for the upcoming Sub-Handle and Virtual-Handle release. All scripts than can use Adahandles for queries and destinations are upgraded to support these additional formats. As always, the scripts doing a second lookup if the Handles are really on the UTXOs that the APIs report. For the Virtual-Handles the Scripts are doing an extra Koios request to checkout the Inline-Datum content of the UTXO holding the Virtual-Handle. Virtual-Handles store the destination address within the Inline-Datum.

Also there has been an Update to show all the different types of Adahandles in the Query, like ADA Handle for the original CIP-25 one, Ada Handle(Own) for the new CIP68 ones. Ada Handle(Ref) and Ada Handle(Virt) for the newest formats.

## Improvements to the Online-Mode (aka Full-Mode)

Critical queries now always do a check if the local node is 100% synced with the chain before continuation.

## Improvements to the Offline-Mode

In Offline-Mode the header on each Script Call now shows your local machine time. This is really important if you are doing things like an OpCert-Update to generate the right KES period. So now you can do an easy check if the time on your Offline-Machine is correct
NativeAsset Token-Registry Information also in Offline-Mode. To get the UTXO data of an address you wanna use in Offline-Mode you are using the command ./01_workOffline.sh add <walletname>. This query - if enabled in the config - now also stores the Token-Registry information about NativeAssets on this address within the offlineTransfer.json file.

##  General updates

The SPO Scripts are now fully Conway-Era compatible!!

01_claimRewards.sh, 01_queryAddress.sh are now showing if the Stake-Address is delegated to a pool. If so it tries to show additional pool-informations like the Ticker, Description and the current Pool-Status

03a_genStakingPaymentAddr.sh: The generation of the Stake-Address registration certificate has been moved to be done within 03b_regStakingAddrCert.sh. This is a change for conway-era, because we now have to check the StakeAdress-Registration Deposit-Fee also for the deregistration. The Deposit-Fee can change after a registration has been done, so with conway-era the used amount is now stored within the certificate itself. If the StakeAddress is already registered on chain, the Script will tell you that and if also delegated to a Pool, it wil try to show you additional informations.
03c_checkStakingAddrOnChain.sh now also shows the used Deposit-Fee of a registered Stake-Address. If delegated to a pool, it tries to show additional Informations. image

04d_genNodeOpCert.sh now directly ready out the onDisKOpCertCount from the via an own new CBOR-Decode function to provide checking information in Light-Mode.

04e_checkNodeOpCert.sh now ready out the onDiscOpCertCount and the onDiskKESSStart values for checking in Online- and Light-Mode

05a_genStakepoolCert.sh now shows the set poolPledge also in ADA and not only in lovecase. Shows minPoolCost now also in ADA and not only in lovelaces. Shows the poolMargin now in percentage and not as decimal value.

05c_regStakepoolCert.sh now shows the set poolPledge also in ADA and not only in lovecase. Shows minPoolCost now also in ADA and not only in lovelaces. Shows the poolMargin now in percentage and not as decimal value.
A pool update/registration/retirement of course now also works in Light-Mode: image If there are external Witnesses (MultiOwnerPool) and the registration is done with an attached Metadata-JSON/CBOR, that information is now also stored to be represented in the external witness file.

05e_checkPoolOnChain.sh now gives you detailed informations about the current pool-status. You can of course also use a pool-id in bech or hex to query this information with this script.

06_regDelegationCert.sh now checks the pool status you wanna send the delegation before continue with the transaction. If a pool is retired or was not registered on the chain(yet), such a transaction would let to an error. This precheck avoids this issue. In addition there is now a check that the Stake-Address is already registered on chain. Also, it now shows information about a current delegation and the planned delegation. The script directly reads out the delegation destination pool-id from the delegation certificate to show this information.

08a_genStakingAddrRetireCert.shnow checks if the Stake-Address is even registered before generating the Retirement-Certificate. Also now important, it checks the Deposit-Fee that was used to register the Stake-Address in first place. Because we need to use the exact Fee again to retire the Stake-Address. There is now also a check if the Stake-Address you wanna retire still holds rewards. If the Stake-Address still hold rewards, it will show you the amount and refuse to generate a Retirement certificate. In that case please first claim all your rewards via 01_claimRewards.sh and after that retire the Stake-Address.

08b_deregStakingAddrCert.shnow again checks the current Stake-Address status on chain and a possible active delegation. Just to make sure you're retireing the right Stake-Address. It also now directly reads out the used Stake-Address Deposit-Fee to calculate the balance return correctly.

Many additional updates here and there for better request handling via curl, better error checks, etc ...

Please enjoy this huge update and especially the new Light-Mode!!

---
## [Aliscans/crawl](https://github.com/Aliscans/crawl)@[866d48a76e...](https://github.com/Aliscans/crawl/commit/866d48a76e53198ac7dee08fed80d99590233fe9)
#### Monday 2023-12-18 09:54:15 by Nicholas Feinberg

Add gems

When I added Meteoran (1352289c90d, based on Hellmonk's ad05b8d819def),
I wanted to give players a fun way to engage with time pressure. When I
play, I really enjoy the feeling of exploring on less than full HP and
making choices about which areas to explore. (Full clearing everything
carefully can be fun, too, but variety is the spice of life!) I'd hoped
to find a way to bring that playstyle to the wider playerbase, with time
limits that are more defined and achievable than the harder and fuzzier
goal of 'compete for a high score'.

Some people, including myself, really liked Meteorans! But a large
number of players, probably the majority, found them stressful and unfun.
That isn't the end of the world - I'd much rather have a species which
20% of players love and 80% hate than one which 99% of players don't care
about one way or another. But I'd also hope that we could do better.

Gems are intended to be an alternate approach to the 'time pressure'
playstyle. They're a new type of collectible item, appearing at the end
of DOLESAPNMVCWUZ - basically, all the non-portal, non-temple branches of
a 3-rune game. Each gem has an associated time limit, which ticks down
while the player is in their associated branch. When that time runs out,
regardless of whether the player has gotten the gem yet or not, Zot rudely
smashes the gem into ten thousand pieces.

The intention is to allow several different ways to interact with gems:
- Ignore them, or not even realize they exist. This is intended to be the
  primary/default interaction.
- Dive to grab gems, but not bother trying to keep Zot from smashing them.
  This is a 'lightweight' speedrunning playstyle, a bit like the Speed
  Demon I tournament banner.
- Keep one or more gems intact by only exploring part of a branch, perhaps
  opting to 'go for it' when your character is feeling especially strong.
- Try to grab all gems and retrieve them all intact. This is roughly
  equivalent to the old Meteoran playstyle.

Gems have absolutely no mechanical use within the game. They offer a very
minor score bonus (10k points each), as a bonus for new players who look
at scores for unwon games, but shouldn't affect normal play or speedrunning
in any way.

Getting the Orb of Zot shuts the timer off. One could skip branches, get
the orb, and then clear branches while holding the Orb to get gems with no
time limit... but orbrunning is its own form of time pressure, and I'm
skeptical this would be easier than playing 'normally'. :)

Time limits are currently set on a per-branch basis. Lair, Vaults, and
Depths have longer time limits than they did for Meteoran, to allow for
large levels and travel time, while Slime and Zot are shorter. However, I
would be startled if these time limits stuck - I personally suspect most
of them are too tight for species which *aren't* as strong as Meteoran.
We can experiment.

The good gem tiles are by Sastreii, the bad ones are by me. :)
Credit also to ellpitic for helping to set me down this path.

---
## [Aliscans/crawl](https://github.com/Aliscans/crawl)@[1baa85e0a2...](https://github.com/Aliscans/crawl/commit/1baa85e0a26512e1e768b837f9ff6c13dab64523)
#### Monday 2023-12-18 09:54:15 by regret-index

Buff various old late game uniques stats, bands

Xtahua's statistics are atrociously low for even a lategame unique. For a
once-beloved dragon with three different gimmicks, they still lag heavily
behind other uniques in their equivalent range. Some of this is that while
their stats are higher than all normal dragons, they simply have much worse
health than nearly any other uniques in their range- somehow, the extra big
dragon has less health than a draconian (Bai Suzhen), a normal human
(Margery), a lich (Boris), and even a tengu (Sojobo). To help them actually
survive long enough to consistently use their 3d40 breath and para roars as
a unique with a built-in weakness, they now have only slightly under Vv's
health, and get some AC and melee buffs alongside this. (Possibly they
could do with some sort of mechanical overhaul in general...)

Bai Suzhen isn't doing nearly as poorly as Xtahua or anybody else in this
commit, but still is somewhat lagging a little behind late uniques. Her
transformation gimmick relies very heavily on her living particularly long
for breath and clouds to do much, but it's very easy for the randomness of
player damage to heavily overshoot the 50% health threshold she relies on.
As such, she also gets a mild HP buff and breathes primal wave a little
more often.

Margery is very boring and also performing reasonably poorly. She's a fire
giant with fancy equipment paired with a hell knight band, in the range
where one will fight about 8 of either in the average game. Since her band
is the notable part of her, I'm extending its fanciness a bit further. She
gets one less max hell knights, but on the hell side of things, the band
gets a hellephant or searing wretch to do even more fire damage, and on the
priest or necromancer side (yes hell knights are priests), she gets a deep
elf high priest or death mage to do more cool weird support stuff.

Frederick can clearly afford getting more and more stat buffs until he
doesn't take a month between kills.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[7fce8cd805...](https://github.com/LemonInTheDark/tgstation/commit/7fce8cd8054cc1d0b048db12d7e9587b42fcdef2)
#### Monday 2023-12-18 09:57:41 by san7890

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
## [GitToby/awesome-tasmania](https://github.com/GitToby/awesome-tasmania)@[b2ac6a1ad9...](https://github.com/GitToby/awesome-tasmania/commit/b2ac6a1ad9fb5790e98d1b2ef1112568f71531fb)
#### Monday 2023-12-18 10:23:22 by Toby Devlin

new content and make build work - fuck you typescript.

---
## [EntranceJew/TTT2](https://github.com/EntranceJew/TTT2)@[56597dcf65...](https://github.com/EntranceJew/TTT2/commit/56597dcf65e064452e2db57f649bb27afe35fb6d)
#### Monday 2023-12-18 10:33:56 by EntranceJew

grenades

- added trajectory for grenade throws
- removed redundant Init/CreateGrenade, use baseclass
- renamed confgrenade vars to make more sense
- added UI to conf/smoke/firegrenade
- removed dead code in smoke entity
- brought in ttt_flame entity
- moved ttt_flame globals to game_effects library, affects C4
- fixed ttt_flame not utilizing offset from trace, as the intent seems to be
- allowed disarming players with impacts
- made discombobs bouncy
- grenade UI indicators in gameplay options
- fixed basegame bug where grenades would self-intersect on raytrace for ground searches
- smoke projectile packs in convars to game_effects
- smoke projectile no longer uses accessor functions
- smoke projectile centers itself by half of its radius to prevent floorsmokes
- hook for confgrenade explode
- particle dispersal from discombob
- consolidate ttt_smoke into Disipate and Remove
- force add PVS code (still doesn't fix ParticleEmitter shenanigans)
- smoke effects use same parameters, but smokegrenade convar differs
- ttt_smoke now utilizes the space better to fill the volume better even with maximum variance
- fires get funny particles and trails
- ttt_flame hitboxes adjusted their hitboxes are way too big
- new explosion sound Tim provided
- new fizzle sound edited together by me
- game_effects.Extinguish now plays a noise
- ttt_flame can no longer re-ignite
- PushPullRadius from conf moved to game_effects
- thirdparty menu
- vfire
- factored out game_effects.ScorchDown
- potentially ruined ttt_firegrenade_proj killing itself frame0 because extinguish might not know what to do with it
- reorganized BaseClass.Initialize for no good reason
- addon checker result ammended
- ttt_flame bringdown
- ttt_flame has netvars for new params
- startfires longer signature
- ttt_flame / SpawnFire has more accurate hitbox
- fire size / life span / spread / prevent discombob fling convars
- removed legacy renderer for fire, since smoke is broken, nobody gets to be happy
- smacking grenades makes explosions
- added changelog
- fixes from TimGoll
- renamed boom_ball to "electric_explosion"
- added more addonchecker items
- passes down the inflictor to pushpullradius
- documented extinguish hook
- gameEffects docs
- remove postround protection and redundant latch, correct trace offset
- don't tinker with the PVS if it isn't fixing problems
- it wasn't relevant because there IS no physics object right now
- all this for a little bit of not scorching in the wrong spot
- all this does is prevent repeat callbacks on the explode method on the client, sometimes
- back out cringe network changes
- replace scorch with PaintDown
- looping smoke sound global
- SmokeData color can now be manually overridden
- killed todos
- docs fixes
- added animation timers back in
- networked the var and run only in server to prevent double sfx
- networked grenade pin noise to all clients
- grenade pin noise for shot grenades
- quick grenade
- grenade damage scaling
- Use the ThirdParty Gui as a simple info panel for now
- Remove vFire convar and simply use vFire if installed

Co-authored-by: saibotk <git@saibotk.de>
Co-authored-by: Histalek <16392835+Histalek@users.noreply.github.com>

---
## [boast/AdventOfCode2023](https://github.com/boast/AdventOfCode2023)@[63998feb9f...](https://github.com/boast/AdventOfCode2023/commit/63998feb9fdbeae0a9425bf23639ff8d55dac30a)
#### Monday 2023-12-18 10:35:12 by Dave Thalmann

Day18
Super easy day, if you remember your geometry formulas and theorems.
I first did not know Shoelace, but Pick after reading it for alternative solutions on Day10. Lucky me, those algorithms are linked on Wikipedia, and it is not hard to implement. However, I struggled a bit with the square-feet requirement, which meant you do not need the "area", you need the actual interior points (plus boundary). Combining Pick and Shoelace gives you the answer we are looking for. Part 1 and part 2 then only differ by their respective parsing method. I also refactored point from int to long, which makes my life easier.

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[922625f511...](https://github.com/LemonInTheDark/tgstation/commit/922625f511bbee14b5b10de5d19229fa2472c287)
#### Monday 2023-12-18 10:51:55 by LemonInTheDark

Speeds up reftracking significantly

Ok so I did a bunch of shit, some of it semi simple

Removed some args, removed some inefficent arg passing, moved shit
around to allow for the faster path, just don't handle empty lists.

Some not

The snowflake list check was eating a lot of time, so I've done a bunch
of bullshit for it
Rather then doing the weirdo list ref thing to figure out if it'll
error, we filter out the vars we know for sure will bite us in the ass
first, and then use try/catch to block errors and mark any offending
lists as such

Removes all the fluff that existed to tie running a ref search to
clients. It's fully automatic now, so there's no reason to have it (Also
none ever used it)

Added support for handing in a known "hanging reference" count, and then
searching for that. This lets us early exit the ref search if we find
everything we were looking for.

All this combined speeds up refsearching massively, on the order of
hundreds of seconds, and makes it far less time consuming for both CI
and running on live. Coming soon to a server near you

---
## [Lazice/KitC-fanfictions](https://github.com/Lazice/KitC-fanfictions)@[d914609218...](https://github.com/Lazice/KitC-fanfictions/commit/d914609218914749bced924ac437be4bf8a49d7c)
#### Monday 2023-12-18 10:57:30 by Lazice

Add files via upload

The Space Where a Heart Should be, tells Zoran's perspective, where Raevyn was talking to Luci after the change to that one's emotional preservation after the stardust.
Oh How Cruel is The Fate that just Laughs and Watches, is a short one about Raevyn at the end of their lab time, overblotting. And killing all the scientists.

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[fc530572f6...](https://github.com/Paxilmaniac/Skyrat-tg/commit/fc530572f6bbe4db0a36df35251a2dd7e62c6b64)
#### Monday 2023-12-18 11:25:23 by SkyratBot

[MIRROR] Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors [MDB IGNORE] (#25493)

* Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors (#80159)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/80158 by making
curses block you from playing Russian roulette regardless of whether or
not there's a live bullet in your Russian revolver's chamber.

A Russian revolver has been added to the contraband section of each Good
Clean Fun vendor.

## Why It's Good For The Game

The bug is incredibly funny, but ~~I want GBP~~ probably should be
fixed.

There's no actual way to get (more) Russian revolvers outside of the
mapstart ones, and that can be a bit stifling to gimmicks that involve
them. And Russian roulette IS a game.

Like the roundstart ones, you could unload these vendor revolvers for
.357 bullets, but you can already just print .357 bullets from a hacked
autolathe directly, so I don't think that's an issue.

## Changelog

:cl: ATHATH
fix: Spacemen can no longer use curses to cheat at Russian roulette by
selectively blocking attempts to shoot themselves.
add: A Russian revolver has been added to the contraband section of each
Good Clean Fun vendor.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Removes an exploit that can farm Russian revolver moodlets, adds Russian revolvers to the contraband section of games vendors

---------

Co-authored-by: ATH1909 <42606352+ATH1909@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [spktechnosoft12/-Unveiling-the-Power-of-E-commerce-CRM-Simplifying-Business-Operations](https://github.com/spktechnosoft12/-Unveiling-the-Power-of-E-commerce-CRM-Simplifying-Business-Operations)@[07051a684c...](https://github.com/spktechnosoft12/-Unveiling-the-Power-of-E-commerce-CRM-Simplifying-Business-Operations/commit/07051a684c4eea5bfcee1e1312ec3e5336f4a597)
#### Monday 2023-12-18 11:30:55 by SPK TECHNOSOFT

Update README.md

E-commerce CRM (Customer Relationship Management) emerges as a dynamic force, offering unparalleled benefits in streamlining operations and fortifying customer relationships. As we embark on this exploration of the synergy between E-commerce and CRM, we’ll delve into keywords such as ecommerce CRM, best ecommerce CRM, ecommerce CRM platforms, and more. In this journey, we’ll also spotlight the exemplary services provided by SPK Technosoft, recognized as a top-tier service provider in this domain.

Understanding the Essence of E-commerce CRM
E-commerce CRM is a specialized approach that combines technology, processes, and strategies to manage and analyze customer interactions throughout the online shopping journey. Tailored to the unique challenges faced by online businesses, a robust E-commerce CRM system becomes a cornerstone in enhancing customer experiences, driving sales, and optimizing operational efficiency.

Key Features of the Best E-commerce CRM
1. Seamless Integration with E-commerce Platforms
The best ecommerce CRM seamlessly integrates with various e-commerce platforms, establishing a unified ecosystem. This integration ensures a smooth flow of data, allowing businesses to centralize customer information, track interactions, and optimize marketing efforts.

2. Comprehensive Customer Data Management
A hallmark of effective E-commerce CRM is the ability to create comprehensive customer profiles. These profiles encompass crucial data such as purchase history, preferences, and behavioral patterns. Businesses can leverage this wealth of information to personalize interactions, tailor marketing campaigns, and enhance overall customer satisfaction.

3. Automation for Enhanced Efficiency
Automation is a key driver of efficiency in E-commerce CRM. It streamlines routine tasks, from order processing to marketing campaigns. Notably, drip E-commerce CRM takes automation to the next level, allowing businesses to engage customers with targeted and personalized messages based on their behaviors and preferences.

4. Strategic E-commerce CRM Approach
Crafting a strategic E-commerce CRM approach is pivotal for businesses aiming to maximize the benefits of this system. This involves defining clear goals, segmenting customer groups, and establishing communication channels. The right strategy ensures that businesses effectively leverage the capabilities of E-commerce CRM.

5. Analytics and Reporting Capabilities
E-commerce CRM is not just about managing customer relationships; it’s also a powerful analytics tool. The best CRM software for ecommerce provides robust analytics and reporting capabilities, enabling businesses to gain insights into customer trends, campaign performance, and overall business metrics.

6. E-commerce and CRM Integration
The integration of ecommerce and CRM is a synergy that transforms how businesses operate. It aligns customer data, sales processes, and marketing efforts, providing a holistic view of the customer journey. This integration enhances coordination between departments and ensures a seamless customer experience.

7. Salesforce: A Dynamic Player
A common question often arises: is Salesforce an ecommerce platform? While Salesforce isn’t a dedicated ecommerce platform, its versatile nature makes it an excellent companion for ecommerce businesses. Salesforce integration enhances data visibility, enabling businesses to create a cohesive and personalized customer experience.

SPK Technosoft: Elevating E-commerce CRM Services
In the realm of E-commerce CRM, SPK Technosoft emerges as a beacon of excellence. As a best service provider, SPK Technosoft offers tailored solutions that align with the unique needs of online businesses. Their expertise spans platform integration, automation, and the formulation of effective E-commerce CRM strategies. Businesses looking for a partner in harnessing the full potential of E-commerce CRM need look no further than SPK Technosoft.

The Transformative Impact of E-commerce CRM on Business Operations
1. Enhanced Customer Retention
E-commerce CRM becomes a catalyst for building enduring customer relationships. Through a deep understanding of customer behaviors and preferences, businesses can implement targeted marketing campaigns, personalized promotions, and loyalty programs, fostering customer loyalty and retention.

2. Efficient Order Processing
Automation within E-commerce CRM expedites order processing, reducing manual efforts and minimizing errors. This efficiency not only improves the overall customer experience but also empowers businesses to handle a larger volume of orders seamlessly.

3. Personalized Marketing Campaigns
The ability to create highly targeted and personalized marketing campaigns is a hallmark of effective E-commerce CRM. Businesses can leverage customer data to send relevant product recommendations, promotions, and follow-up communications, increasing the likelihood of conversion.

4. Streamlined Customer Service
E-commerce CRM facilitates streamlined customer service by centralizing customer information. This centralized view enables customer service representatives to access order history, preferences, and previous interactions, allowing for more informed and efficient customer support.

5. Data-Driven Decision Making
The robust analytics and reporting capabilities of E-commerce CRM enable businesses to make data-driven decisions. By analyzing customer trends, purchase patterns, and campaign performance, businesses can refine their strategies and allocate resources effectively.

6. Cross-Channel Consistency
For businesses operating across multiple channels, maintaining consistency is paramount. E-commerce CRM ensures that customer data is synchronized across various touchpoints, providing a seamless and unified experience, regardless of the channel through which customers interact with the brand.

Implementing E-commerce CRM: A Strategic Approach
To fully harness the potential of E-commerce CRM, businesses must adopt a strategic approach tailored to their unique goals. Here are key steps to effectively implement E-commerce CRM:

1. Assessment of Business Needs
Conduct a comprehensive assessment of your business needs. Identify pain points, areas for improvement, and specific goals you aim to achieve with E-commerce CRM.

2. Selection of the Right Platform
Choose the right E-commerce CRM platform based on factors such as scalability, integration capabilities, user-friendliness, and specific features that align with your business requirements.

3. Platform Integration
Integrate the selected E-commerce CRM seamlessly with your existing e-commerce platform. This integration ensures a cohesive flow of data between customer interactions, purchases, and marketing efforts.

4. Customization for Optimal Results
Customize the E-commerce CRM system to align with your business processes and goals. Tailor features, reports, and dashboards to meet the specific needs of your online business.

5. User Training and Adoption
Provide thorough training to your team on using the E-commerce CRM system effectively. Ensure that team members understand how to leverage its features to enhance their daily operations.

6. Continuous Monitoring and Optimization
Regularly monitor the performance of your E-commerce CRM system. Analyze data, gather feedback from users, and make continuous optimizations to ensure that the system evolves with the changing needs of your business.

In Conclusion
E-commerce CRM is a dynamic force that has the potential to revolutionize how online businesses operate and engage with their customers. From enhancing efficiency and customer retention to streamlining order processing and facilitating personalized marketing campaigns, the impact of E-commerce CRM is profound. Businesses looking to embark on this transformative journey need a reliable partner, and SPK Technosoft stands as a beacon of excellence, offering top-tier services

TOLL FREE – CLICK HERE TO GIVE MISS CALL – +918900011103
Support: 247 Support Available in Hindi, English, Bengali, Marathi, Kannada, Tamil, Telugu, Malayalam

Click Here to Call Our 247 Support @ +91 8900011103
Features:
Dynamic SEO Ready Website
Live Chat & Social Media
Mobile Responsive Website
Online Payment Gateway
Website Design Plans & Pricing:
Business Website Plan
Basic Plan – ₹6999
Classic Plan– ₹9999
Premium Plan – ₹15499
E-Commerce Website Plan
Statdard Plan- ₹14999
Extended Plan– ₹19999
Business Plan– ₹24999

---
## [Aurorastation/Aurora.3](https://github.com/Aurorastation/Aurora.3)@[bc66a212d7...](https://github.com/Aurorastation/Aurora.3/commit/bc66a212d771eef33ae88445ebe4462ee25bde17)
#### Monday 2023-12-18 11:46:26 by RustingWithYou

Hephaestus Security Ship & Corporate Voidsuit Tweaks (#17962)

* hephaestus security ship

* fuck off

* welcome mesgaes

* lattice hell

* damn you kaizr

* cabinet

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[e9f12be172...](https://github.com/lizardqueenlexi/orbstation/commit/e9f12be1724e4b711df54f35cc117dca0a3aa07d)
#### Monday 2023-12-18 12:34:19 by Higgin

Changes Virology Rather Than Killing It (#79854)

## About The Pull Request
God, alright, here we go. See HackMD here:
https://hackmd.io/@Higgin/HJljdBuNp

Alternative proposal to #79849 addressing the big problems with
virology. ~~If you need a HackMD for it, I'll put one together, but I
made a comment on that PR and can make it pretty simple here.~~ its done

1. Makes viruses eventually self-cure as long as you're alive. If you
can keep somebody from dying, they can develop immunity.
2. Makes it so you can sleep comfortably and be well-fed to slow and
even potentially defeat viruses without a cure.
3. Makes it so more dangerous viruses can start self-curing faster. This
means Space Ebola is going to burn itself out quicker if a person stays
alive from the other effects.
4. Makes spaceacillin helpful in naturally curing viruses, period, but
with declining effectiveness over 100 cycles.
5. Makes it so curing a virus naturally without being well-fed or having
rode it out from the peak may allow you to be reinfected/not have
natural immunity.
6. Makes it so being well-fed is a much stronger protection against
random virus spread.
7. Makes it so bypasses_immunity stuff like fungal TB and heart failure
isn't subject to any of this.
8. Makes it so using ~~antibiotics~~ spaceacillin jesus christ or being
malnourished can make you lose your healing viruses too. Pay attention
to what you put in your body.
9. ** Makes it so blood can ~~transmit resistances again, not just
vaccines. It's been a hot minute, but it used to work like this.~~ blood
now can cure a virus if the donor has a resistance, but it doesn't
confer lasting immunity. You need to overcome the virus yourself, carry
a constant supply of pure blood, or get a vaccine to get a lasting fix.
10. ** makes severity a function of disease stats and all active
symptoms - not just the highest severity of the active symptoms.
11. ** makes it so you can nosell symptoms firing with spaceacillin or
resting down to a minimum chance of cure_chance to avoid symptoms each
cycle, declining over time, over 100 cycles for a given disease.
12. ** makes it so wearing protective equipment prevents you from
spreading respiratory-spread diseases normally - not just on the
cough/sneezing symptoms.
13. ** gives MDs virology access standard, paramedics and coroners
virology access on skeleton crew. virologists also get pharmacy access.
14. ** makes bypasses_immunity advanced diseases always override
non-bypasses_immunity advanced diseases and resist being overridden by
other advanced diseases. Sentient Disease now has bypasses_immunity.
Sentient Disease fans rejoice!
15. ** also gives SD a buffer of extra stealth points so it has a bit
longer to build up instead of almost uniformly getting spotted and dying
early.
16. ** viruses now scale their severity as a function of their max
symptoms. There's a lot more room to get viruses of varying duration and
severity by adding fewer symptoms now - so creating a tradeoff between
stats (and good thresholds) and the duration of your virus.
17. ** a whole bunch of defines to control all of this stuff - most
recently added a multiplier for symptom appearance frequency.

MAJOR UPDATES: REBALANCING TOWARDS 50% LETHALITY

https://docs.google.com/spreadsheets/d/e/2PACX-1vQ8rqMYFsR1mYj_FGzVjTfcnAF7un-VofOByPxcCCQr6lOOF5fhUgZga0oA4Q5-7K4hr7fCV0jFdmd9/pubhtml#
[Viro Rework Rebalance
Tests.pdf](https://github.com/tgstation/tgstation/files/13447208/Viro.Rework.Rebalance.Tests.pdf)

After a shitload of testing, makes some of the most reliable,
transmissible killers into less-reliable threats. See the above graphs
and pictures for demonstrations of exactly how this was tested and done.

## Why It's Good For The Game

It sucks to be hard-stuck to needing chemistry and medical to deal with
viruses that somebody can randomly blast out without a care in the
world, then be left to sit around waiting to die or otherwise be unable
to do anything as the max-level symptoms fire off on repeat.

This should put curing and surviving viruses much more back in the hands
of normal crew without always ending up at the chemistry front window,
although that is still the fastest and most reliable way to get better.

This also nerfs healing viruses a bit, or makes them a bit less
fire-and-forget if you fail to attend to your body. There's more I'd
like to do in the future and potentially some of the other classic
viruses that could use bypasses_immunity added, values tweaked, but for
now - this seems like the best way to preserve virology as a level of
depth and complexity in the game in a way that rewards people doing
intuitive things to counterplay it when used harmfully.

This also puts more of the mid-range bad symptoms into a better place
balance-wise because the worst ones pretty much only fire at max stages.
With the way this works out, you bounce back and forth between the max
stage and lower stages before, over time, trending towards a cure.
Symptoms that provide more significant effects at lower stages now have
a place that isn't totally overshadowed by the killdeath stage 5 ARDS +
junk symptoms virus Dr. Ambatu Popov shat out in five minutes (as long
as you survive the initial run-in with it.)

## Changelog

:cl:
balance: most diseases can now be slowed, mitigated, and eventually
cured through being well-fed, resting, and using spaceacillin. Curing
diseases through this way will give you immunity if you experience them
at their peak/maximum and aren't starving/malnourished when they cure.
balance: disease symptoms can be forestalled for up to 100 cycles with a
declining chance of avoiding them over time using rest or spaceacillin.
balance: This does not apply to things like fungal TB; it does apply to
healing viruses if you don't take care of yourself by staying fed and
avoiding spaceacillin.
balance: disease can be cured through direct injection or ingestion of
cured blood. However, curing disease in this way does not provide
lasting immunity. You need to naturally beat the virus or get a vaccine
for that.
balance: Wearing internals or using protective equipment while infected
can limit the spread of respiratory illnesses from yourself to others.
Contact transmission is still possible however.
balance: Medical Doctors now have roundstart virology access. Paramedics
and coroners now get virology access on skeleton shift access.
Virologists now have roundstart pharmacy access.
balance: Sentient Diseases now resist being overridden by other advanced
diseases and can always override other advanced diseases; they also have
an extra bonus on their stealth stat to help make up for early outing
without a bit more testing.
balance: biohazard lockers now also contain a syringe of spaceacillin
(in line with the orderable kit from cargo.)
balance: Virus severity is now also a function of the number of symptoms
out of max your virus has. Experiment with different combinations using
less than six symptoms to make viruses that are deceptively less-obvious
and less quick to self-cure at the tradeoff of stats.
/:cl:

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[b8fc9b367e...](https://github.com/lizardqueenlexi/orbstation/commit/b8fc9b367ebb26def792a68bcb25294e518698d8)
#### Monday 2023-12-18 12:34:19 by LemonInTheDark

Icon Autoslicing (#79659)

## About The Pull Request

Ok so you know all the dmis we have that are made to work with the
smoothing system? carpets, walls, etc.

The proper way to edit those is to convert them into a png with 5
"states' it in (one for 0 connections, one for horizontal, one for
vertical, one for all cardinals and one for all directions) and then
modify THAT, then run it through [the cutter
tool.](https://github.com/tgstation/icon-cutter)

But none ever does that, because we explain it fucking nowhere. So
instead, let's keep all those "base" files in the repo, alongside the
configs they work with, and "cut" the pngs into dmis as a part of the
build process.

I wrote a guide for how to interact with this system as a spriter, you
can find it
[HERE](https://github.com/LemonInTheDark/tgstation/blob/slice-the-sky/icons/Cutter.md).

[Adds a icon cutter build
task](https://github.com/tgstation/tgstation/commit/52143d2e96498de92421d516e0dd3f23936f88d8)

This relies on action ninja's hypnagogic (find more
[here](https://github.com/actioninja/hypnagogic)), a rust based icon
cutter.
It operates inline with the file structure, searching the codebase for
templates and resource files and compiling them down to dmis.

It can do way more then just bitmask stuff, but that is what we are
using it for rn.

Hope is to prevent for eternity the "I'm just gonna edit each of these
255 icon states that's how this carpet was made right?" meme, and allow
more expansive use of smoothing in future

[Adds a lint that ensures config files work
right](https://github.com/tgstation/tgstation/commit/21eeab9cf831c5fdac5a9b366478a9dab285c20c)

Checks to ensure they have a paired png and dmi, and also avoids issues
with uncompiled changes by double checking that nothing happens
before/after a cutter run

[Pulls all non smoothed states out of structures into bespoke
dmis](https://github.com/tgstation/tgstation/commit/a730e0cb47fc0a622fe265bccc296cec8d3a8fea)

This is required because the cutter cannot output named icon states,
only the actual cut icon

[Does something similar to
walls](https://github.com/tgstation/tgstation/commit/40780e9481103c8ee9e16538d1c2d0cdc124eeb9)

Moves reinforced walls decon stuff from their icon to a var on the type
and a set of states in the reinforced_states dmi

Moves falsewalls into their own dmi, this involved some changes to
gamecode to ensure falsewalls knew which dmi to use and what key.
Makes falsewalls display as such in editor rather then just walls

Moves smoothrock's gibonite overlays into their own file for similar
reasons

[Same thing different day
(Floors)](https://github.com/tgstation/tgstation/commit/9a3da3b69705278f39af109ac5ce86d27c2479a1)

Pulls bespoke floor icon states into their own file, splits up neon
carpets into multiple files to make cutting possible

[Actually adds the cut templates and their matching png
files](https://github.com/tgstation/tgstation/commit/1bd8920dc90d1ee1b934b6dadc39f2331854f5fa)

Not much to report here, outside of I changed the prefix for bamboo
walls to bamboo_wall so it works with false_walls

## Why It's Good For The Game


![image](https://github.com/tgstation/tgstation/assets/58055496/7c3ac7fb-873c-481b-8667-082e39432876)

None should have to manually edit cut dmis. Ever.
Also this makes adding a new smoothed thing trivial, don't even need to
know what tool you're using to do it. V good v good.
Sets us up nicely for wallening's well, wall of sprites.

Some structural decisions, we are essentially committing build artifacts
here. That's the best way of handling it because otherwise mappers could
need to run build.bat before opening a map, and that is stupid!

## Changelog
:cl:
refactor: (Almost) all smoothed icons can now be edited in their pre cut
forms
/:cl:

---
## [ZacharyTStone/ZacharyTStone](https://github.com/ZacharyTStone/ZacharyTStone)@[812b567b7e...](https://github.com/ZacharyTStone/ZacharyTStone/commit/812b567b7ea2e2b2c79dee6aac66a4811554b0fb)
#### Monday 2023-12-18 13:06:01 by ROBO-ZACH

Update README with new quote: "Yesterday is history, tomorrow is a mystery, today is God's gift, that's why we call it the present." <br>— Joan Rivers

---
## [mullenpaul/cmss13](https://github.com/mullenpaul/cmss13)@[f4f334de22...](https://github.com/mullenpaul/cmss13/commit/f4f334de22e5d2782f35115a9b1461326e1c4a8c)
#### Monday 2023-12-18 13:07:19 by Doubleumc

Vehicle autofire (#4959)

# About the pull request

Convert vehicle hardpoints from using their bespoke firing system to one
structured closely on handheld guns and deployables such as the M2C. Now
using the `autofire` component. Much like handheld weapons it is capable
of different firemodes (semi/burst/auto) and changing targets during
fire.

Hardpoints were converted to match their old effectiveness as closely as
possible; this is intended as a quality of life improvement, not a
rebalance. Damage, AP, range, ammo, etc were not touched.

Fire rates were copied over directly. Single-fire weapons with long
delays were made semi-auto (e.g. LTB), and those with short delays were
made full-auto (e.g. autocannon). Burst-fire weapons with significant
extra delays after the burst remained burst-fire (cupola, smokescreen),
and the rest were converted to full-auto (e.g. dual cannon). While
changing firemodes is easily implemented, no weapon seemed a good
candidate for more than one firemode and so that is omitted for now.

Scatter was approximated. The existing `accuracy` functioned as a
percent chance the shot would stray one tile from the target. Gun-style
`scatter` is instead a cone of fire in degrees. No direct conversion is
possible, so scatter values are roughly set such that firing at a tile
at the edge of the screen should "feel" about as accurate. Closer ranges
would experience less spread than before, longer ranges more.

The buffing weapon sensor module was adjusted to work with the new
firing system, and effects hardpoint scatter angle and firing rate.
Vehicle buffs still use multipliers instead of adding/subtracting as
handheld guns do, as a flat +/- adjustment to fire delay would have a
significantly different effect on slow firing weapons (e.g. LTB) vs fast
firing (e.g. autocannon). One major difference is that burstfire delays
are effected and buffs increases the burst density. Before, there was a
single cooldown initiated at the start of the burst, and only that
cooldown was modified by the buff. Now, since the inter-burst delay is
needed by the `autofire` component both the inter-burst delay and the
after-burst delay are modified by buffs.

Activating non-selected hardpoints was removed as not compatible. The
issue is that tracking a single click's modifiers is no longer
sufficient, it has to track through the whole mousedown-to-mouseup
period and the user can change multiple click modifiers in that time. I
could not find a method that was satisfactory without a much bigger
overhaul of vehicle controls than I'd like to take on in a PR not meant
for it. I'm sure it can be done, but that brings up the question of if
that's even the control scheme we'd want, in a PR that was never meant
to ask that question let alone answer it.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Vehicle weapons using `gun`-like code makes them easier and more
familiar to use, and more code commonality makes maintenance just a
little bit easier.
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
refactor: vehicle weapons can fire full-auto
del: no more controls for firing vehicle non-selected weapons
/:cl:

---
## [mullenpaul/cmss13](https://github.com/mullenpaul/cmss13)@[fe35cc5927...](https://github.com/mullenpaul/cmss13/commit/fe35cc5927f873f7a3497d02a6389c9678a61a7f)
#### Monday 2023-12-18 13:07:19 by forest2001

Forest Bugfix Bundle (#5127)

# About the pull request
Forest is stupid.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
fix: Fixes custom sent ERTs broadcasting when they shouldn't.
fix: Fixes UPP friendly ERT telling staff it's hostile.
/:cl:

---
## [cuppi/react](https://github.com/cuppi/react)@[b6978bc38f...](https://github.com/cuppi/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Monday 2023-12-18 13:54:16 by Andrew Clark

experimental_use(promise) (#25084)

* Internal `act`: Unwrapping resolved promises

This update our internal implementation of `act` to support React's new
behavior for unwrapping promises. Like we did with Scheduler, when 
something suspends, it will yield to the main thread so the microtasks
can run, then continue in a new task.

I need to implement the same behavior in the public version of `act`,
but there are some additional considerations so I'll do that in a
separate commit.

* Move throwException to after work loop resumes

throwException is the function that finds the nearest boundary and
schedules it for a second render pass. We should only call it right 
before we unwind the stack — not if we receive an immediate ping and
render the fiber again.

This was an oversight in 8ef3a7c that I didn't notice because it happens
to mostly work, anyway. What made me notice the mistake is that
throwException also marks the entire render phase as suspended
(RootDidSuspend or RootDidSuspendWithDelay), which is only supposed to
be happen if we show a fallback. One consequence was that, in the 
RootDidSuspendWithDelay case, the entire commit phase was blocked,
because that's the exit status we use to block a bad fallback
from appearing.

* Use expando to check whether promise has resolved

Add a `status` expando to a thrown thenable to track when its value has
resolved.

In a later step, we'll also use `value` and `reason` expandos to track
the resolved value.

This is not part of the official JavaScript spec — think of
it as an extension of the Promise API, or a custom interface that is a
superset of Thenable. However, it's inspired by the terminology used
by `Promise.allSettled`.

The intent is that this will be a public API — Suspense implementations
can set these expandos to allow React to unwrap the value synchronously
without waiting a microtask.

* Scaffolding for `experimental_use` hook

Sets up a new experimental hook behind a feature flag, but does not
implement it yet.

* use(promise)

Adds experimental support to Fiber for unwrapping the value of a promise
inside a component. It is not yet implemented for Server Components, 
but that is planned.

If promise has already resolved, the value can be unwrapped
"immediately" without showing a fallback. The trick we use to implement
this is to yield to the main thread (literally suspending the work
loop), wait for the microtask queue to drain, then check if the promise
resolved in the meantime. If so, we can resume the last attempted fiber
without unwinding the stack. This functionality was implemented in 
previous commits.

Another feature is that the promises do not need to be cached between
attempts. Because we assume idempotent execution of components, React
will track the promises that were used during the previous attempt and
reuse the result. You shouldn't rely on this property, but during
initial render it mostly just works. Updates are trickier, though,
because if you used an uncached promise, we have no way of knowing 
whether the underlying data has changed, so we have to unwrap the
promise every time. It will still work, but it's inefficient and can
lead to unnecessary fallbacks if it happens during a discrete update.

When we implement this for Server Components, this will be less of an
issue because there are no updates in that environment. However, it's
still better for performance to cache data requests, so the same
principles largely apply.

The intention is that this will eventually be the only supported way to
suspend on arbitrary promises. Throwing a promise directly will
be deprecated.

---
## [tuxarch/awesome-console-services](https://github.com/tuxarch/awesome-console-services)@[4b8f298fb2...](https://github.com/tuxarch/awesome-console-services/commit/4b8f298fb2b94b3c492da39ca43fcd2775907eea)
#### Monday 2023-12-18 14:12:10 by techie2000

ascii.town is no longer interactive

Attempting to access it now results in 
```
================================================================================

Nazis, fuck off!

Sorry to everyone else who enjoyed this space.  It was only a matter
of time, and it lasted a lot longer than I ever expected.  It breaks
my heart to log in and see hate on the canvas.  Obscurity is no
longer enough to keep this space as pleasant as it once was.  I'll
clean up what I can and keep https://ascii.town/explore.html running
so that what was created here can continue to be enjoyed.  Thank
you all for your contributions over the years.  You made something
beautiful.

Black lives matter.  Trans rights are human rights.  Much love to
all the gay weirdos out there.

~june

torus@ascii.town  2017-2022

================================================================================
```

---
## [ZuTahi/EnRoute-Prototype-V1](https://github.com/ZuTahi/EnRoute-Prototype-V1)@[7bf762c914...](https://github.com/ZuTahi/EnRoute-Prototype-V1/commit/7bf762c914a2811e5996f63995f859efb8bf19c0)
#### Monday 2023-12-18 14:48:56 by ZuTahi

I added the cam movement for the Nav scene

Dashing through the snow
In a one-horse open sleigh
O'er the fields we go
Laughing all the way
Bells on bobtails ring
Making spirits bright
What fun it is to ride and sing
A sleighing song tonight, oh!

Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one-horse open sleigh, hey!
Jingle bells, jingle bells
Jingle all the way
Oh what fun it is to ride
In a one-horse open sleigh

Now the ground is white
Go it while you're young
Take the girls tonight
Sing this sleighing song
Get a bobtailed bay
Two forty for his speed
And hitch him to an open sleigh
And you will take the lead

Oh, jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one-horse open sleigh, hey!
Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one-horse open sleigh
Oh, what fun it is to ride
In one horse open sleigh!

---
## [StarRuCat/sojourn-station](https://github.com/StarRuCat/sojourn-station)@[3409d0b3ec...](https://github.com/StarRuCat/sojourn-station/commit/3409d0b3ec3ac4c5a8e9bd7a0118581c9749ed51)
#### Monday 2023-12-18 15:07:37 by benj8560

misc map fixes (#4883)

* map stuff

* small touchup

* stuff!

more minor fixes!

Relocates Ians dinner so it's not hiding away inside a closet where he can't enjoy it assumed unintended. Also returns Runtimes food to her from the old map.

Corrects the micromeds in dorms to using offsets rather then being lodged insdie a wall.

Relocates the Turbine cooling chamber blast door button to the GMs storage room and gives it a atmos ID lock for good mesure. Should keep those trainees away from the funny room.

Adds a sec cam I forgot to the new atmos hard storage room.

Moves poly into the GMs breakroom and gives him a few crackers to eat/grab. The stamp is finally free!

* weh

fixes the missing cables preventing the Terminal Lounge from getting power. You know small lounge near the big shuttle pad for ebents.

* buttttton

adds a button to control the shutter for blackshields maint backdoor

---
## [ChanhAvo/SusyFishy](https://github.com/ChanhAvo/SusyFishy)@[d999a6ead5...](https://github.com/ChanhAvo/SusyFishy/commit/d999a6ead5957acd0bc51c9c13acb504c5043927)
#### Monday 2023-12-18 15:19:56 by Đặng Mai

Merge pull request #10 from ChanhAvo/DMai

change for loop map into the orginal one (i hate my life)

---
## [Geronimo-Basso/sierra](https://github.com/Geronimo-Basso/sierra)@[7e71a61f24...](https://github.com/Geronimo-Basso/sierra/commit/7e71a61f24f99c02a067d0f78c1a31ec96dea2c9)
#### Monday 2023-12-18 16:08:33 by jorge

Into the dark side

Introducing Dark Mode - your favorite app now with 100% more darkness and 0% Ewoks.

Midnight Mastery: Just like a stealthy Na'vi navigating through Pandora at night, our Dark Mode allows you to seamlessly blend into the shadows of your phone's interface. Perfect for those midnight app adventures!
Battery Wisdom: Much like a Tesla gliding silently through the night, Dark Mode is not only sleek but energy-efficient. Your battery will thank you, and so will the planet. Elon would be proud.
Eye Comfort, Jedi-Style: Your eyes are precious. Protect them like a Jedi protects the galaxy. With Dark Mode, your screen becomes as soothing as a calm night on Dagobah, ensuring a comfortable experience even during the longest scrolling missions.
Remember, with great power (mode) comes great responsibility. Embrace the dark side, responsibly.

May the dark (mode) be with you!

Disclaimer: No Stormtroopers were harmed in the making of this update.

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[8d77b1be89...](https://github.com/Ghommie/tgstation/commit/8d77b1be89f771391c5697a1a3ac180f68cd6858)
#### Monday 2023-12-18 17:21:51 by necromanceranne

Balance changes to swords, energy shields and modsuit shields. (#80072)

## About The Pull Request

### Sword Weaponry

Mundane sword weapons of all sorts do not block ``LEAP_ATTACK`` attacks
whatsoever. These attacks include tackles, xeno tackles and bodythrows.

Energy swords and double energy swords only gain 25% block probability
against such attacks.

### Double Energy Sword

No longer grants outright energy projectile immunity while employed.
Instead, it just has a high probability of reflecting (the typical 75%
to block any other attack). So, very solid defense against energy
projectiles, but not immunity.

Against non-reflectable projectiles, like ballistics or nanite bullets,
the desword only has 50% block, similar to an energy sword.

To compensate for the loss of defensive power, we'll make it all the
more rewarding for getting on top of someone with the sword by giving it
40 force while active. And also it costs 13 TC.

### Combat Energy Shield

This also lost outright energy projectile immunity, but gained the
standard blocking power of shields on top of the ability to reflect
energy projectiles when they block them. This significantly increases
the shields potential effectiveness while no longer pigeonholing the
shield to only energy weapons. (This makes them exceptionally good
against tackles and body throws, by the by).

Deathsquads still have the perfect deflection energy shield so that they
can continue to spam pulse shots with impunity.

### MODsuit Shield Module

Only has one charge instead of three, but it recharges in half the time.
This is no longer such a perfect defense, and does somewhat need you to
be thinking about how you're utilizing the shield rather than not
thinking about defense at all by barreling forward under three potential
hits worth of protection.

Also much cheaper, at almost half price of 8 TC. Because of how cheap it
is (and how much it still is necessary to keep you alive), I've put it
into the core equipment box (which brings the price up to 22 TC. As a
reminder, this is not meant to be at any discount, and is more aimed
towards teaching newer players which items contribute towards success.
If you don't want all the times within, don't buy this box, just buy
what you want separately.)

## Why It's Good For The Game

This is a doozy of an explanation, I hope you're ready for it under the
spoiler.
<details>
With my tackling and bodythrow prs, numerous people expressed
exasperation at the fact that these two tools may have been keeping some
outlier antagonist gear from becoming too easy to steamroll with if you
already knew what you were doing. My intent was to create consistent
rules and behaviours that both A) did not rely on bugs to keep the
balance of power from tipping one way or the other, and B) was at least
consistent or had consistent rules established.

This PR is tackling overperforming gear combinations for already
competent nukies that may have, over time, crept out of control, and
applying some consistency to the rules around similar equipment.

AND also deals with quite possibly the most braindead element of game
design we've tolerated for about a decade, and half a decade after it
was necessary to maintain that decision.

Part of the culprit of this issue is that, specifically in regards to
nukies, crew can't use the vast majority of their weapons effectively
against them. This largely is because this antagonist can gain
immunities to those types of equipment. And that is rapidly increasing
as we move closer towards outright ballistic removal. I don't think the
game is made healthier by everyone on the station having to fight armed
mercenaries with spears, and doesn't make much thematic sense either.
More so, most greener players probably just don't know this is how it
works, and so surprise Pikachu when their lasers bounce off nukies
harmlessly. (This bit reminds me of the problem of new players using
disablers against simple mobs)

But of course, that isn't the only part of the problem. The other half
is due to being able to be layered on a much more broad defensive tool
in the form of the MODsuit Shield Module, whose three charges could
render the mindful nukie near untouchable if they're pairing it with
some other layered defense, such as a desword. Notice that this doesn't
really address armor. The culprit is negation, and not mitigation, and
we should be sparing in how easily we hand out outright effect negation
simply because it isn't super obvious to a new player why it happened,
and how to resolve it. At the very least, we should look to find ways to
add options for players to overcome these problems. Especially with
teamwork.

Energy projectile immunity made sense while there floated around an
energy projectile that ostensibly would down you in a single shot.
Nukies ALSO had projectile weapons that worked much the same (c-20r stun
bullets, taser shot bulldogs, etc.), so it was predominantly
tit-for-tat. These immunity granting equipment pieces forced crew
members to get shotguns and ballistic guns to fight these dangers;
something more available at the time.

We've exercised large bits and pieces of this from the game a long time
ago, but we still have some remnants convinced we're still in a
taser-rich, ballistic available environment. We need to move the games
languishing tools into the modern era and re-established their place in
the game. Namely, the double-energy sword and the combat energy shield
are almost entirely unchanged besides refactors for the last decade or
so, even while the game around them have changed. They've been a
continuous sore point for me in all my time developing and a constant
nagging issue. I want to deal with it now.

MODsuit Shield Module is just kind of really good and only made stronger
the more defenses you have. It's good to have a defense like this, but I
think it is too brain dead. With only one charge, it will save you from
a lost joust here and there, but it won't make it as simple as running
right at every problem you encounter and eating a volley of attacks
while you kill someone with impunity.

**With regards to traitors**, since they also get double-energy swords;
I'm open to suggestions if this is hitting them far too hard, but I'm
not terribly concerned using this weapon for a few reasons. **Firstly**,
I think their presence amongst the crew make it a much better weapon for
tots than nukies (in isolation) simply because they can find ways to
exploit it via tools they gather from the station. It is a force
multiplier. Traitors also have a much bigger element of surprise
usually. **Secondly**, round-start traitors typically grow to be a bit
stronger over time, but I don't foresee many waiting to pay for the
double-energy sword unless they're already flush with TC. So if a
traitor is in a position after they've unlocked access to it to buy one
of these, they are probably doing pretty okay for themselves.
</details>

### TL;DR

Defense stacking and attack immunities are not particularly healthy
things to both design around, or experience in-game. They are kind of
just relics of the past made only sorer once I ripped off a few
bandaids. This is a source of a number of symptomatic issues in the
game, so let's fix that and make it easier on all of us going forward.

Much of the way these things worked operated on extremely outdated
design considerations. It doesn't make sense for them to work like this
today, and only makes things harder by keeping the status quo.

## Changelog
:cl:
balance: Mundane sword-like and medieval weapons are not able to block
tackles, xenomorph tackles and body throws.
balance: The double-energy sword and energy sword have trouble blocking
physical projectiles, body throws and tackles.
balance: The double-energy sword also no longer has guaranteed energy
projectile deflection; only doing so on a successful block (75% chance
to block).
balance: But it does have 40 force now, so it is more lethal a weapon.
Traitors can purchase the sword for only 13 TC (down from 16 TC).
balance: The combat energy shield (The one you hold) now functions as a
normal shield (it used to only protect you against energy projectiles
and nothing else). It loses guaranteed energy projectile deflection, but
still reflects the projectile so on a block.
feature: Death commandos continue to have their energy shields deflect
all incoming energy projectiles. Because who cares about deathsquads
being balanced?
balance: The MODsuit shield module only has one charge, but recharges
every 10 seconds. It also costs 8 TC (down from 15). It is also now in
the Core Gear beginner box (bringing the total price up to 22 TC).
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[54ab1e3936...](https://github.com/Ghommie/tgstation/commit/54ab1e3936b3d5a301b995f2c1ca14fcdaf3e80d)
#### Monday 2023-12-18 17:21:51 by Time-Green

Organ movement refactor *Un-nullspaces your organs* (#79687)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

closes #53931, #70916, #53931

## About The Pull Request

Organs were previously stored in nullspace. Now they are stored in their
prospective bodyparts. Bodyparts are now stored in the mob.

I've also had to refactor a lot of code concerning organ movement.
Previously, organs were only moved into bodyparts once the bodyparts
were removed. To accomodate this change, two major distinctions have
been made:

**Bodypart removal/insertion**
Called only when an organ is taken out of a bodypart. Bodypart overlays,
damage modifiers or other changes that should affect a bodypart itself
goes here.

**Mob insertion/removal**
Called when an organ is removed from a mob. This can either be directly,
by taking the organ out of a mob, or by removing the bodypart that
contains the organ. This lets you add and remove organ effects safely
without having to worry about the bodypart.

Now that we controle the movement of bodyparts and organs, we can fuck
around with them more. Summoning someones head or chest or heart will
actually kill them now (and quite violently I must say (chest summoning
gibs lol)).


https://github.com/tgstation/tgstation/assets/7501474/5efc9dd3-cfd5-4ce4-b70f-d0d74894626e

I´ve also added a unit test that violently tears apart and reconstructs
a person in different ways to see if they get put toghether the right
way

This will definitely need a testmerge. I've done a lot of testing to
make sure interactions work, but more niche stuff or my own incompetence
can always slip through.

## Why It's Good For The Game

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->

A lot of organ work is quite restricted. You can't C4 someones heart,
you cant summon their organs and a lot of exceptions have to be made to
keep organs in nullspace. This lets organs (and bodyparts) play more
nicely with the rest of the game. This also makes it a lot easier to
move away from extorgans since a lot of their unique movement code has
been removed and or generalized.

I don't like making PRs of this size (I'm so sorry reviewers), but I was
in a unique position to replace the entire system in a way I couldn't
have done conveniently in multiple PRs

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
refactor: Your organs are now inside your body. Please report any issues
with bodypart and organ movement, including exotic organ, on github and
scream at me
fix: Cases of unexpected organ movement, such as teleporting bodyparts
and organs with spells, now invokes a proper reaction (usually violent
death)
runtime: Fixes HARS runtiming on activation/deactivation
fix: Fixes lag when species swapping
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[16bdcf409c...](https://github.com/Ghommie/tgstation/commit/16bdcf409c5d6eb3d846b16f4968849e26cf833c)
#### Monday 2023-12-18 17:21:51 by Rhials

"Security Implant" rework, prisoner management console updates (#79882)

## About The Pull Request

For the vernacular purposes of the following PR body -- "Security
Implant" refers to the existing subset of implants given, by security,
to captured prisoners and such as a punitive, controlling measure. This
includes the chemical, tracking, and maybe exile implants.

This revamps the functionality of how "security" implants are displayed
on huds, prisoner management console implant controls/readouts, and
their instrumentality. It was also, ultimately, an attempt at nerfing
the tracking implant that spiralled far out of control.

Rather than only displaying chemical on the right and tracking on the
left, all implants with the "security implant" flag will be trackable on
SecHuds. A maximum of two can be implanted at once. This is both due to
technical limitations, but also conveniently provides security a limit
to consider when choosing implants.

Implants now also occupy their HUD slot based on the order they were
implanted in, rather than always occupying the same spot. Neat!


![image](https://github.com/tgstation/tgstation/assets/28870487/68b17dbb-cda4-4c3b-96d4-b3bbcf49b80e)

From two (three if you count the exile implant), there are now five
security implants. _The tracker implant has been split into two of these
implants._

<details>
<summary>Summary of the implants, functions, changes:</summary>
<br>

- **Tracker (Red)** -- No longer grants teleporter beacon. Tracking
radius has been increased from 20 to 35 tiles. The Prisoner Management
Console will now list the area the prisoner is occupying as well.
Disables after the implantee is dead for 10 minutes.
- **Chemical (Blue)** -- No mechanical changes. The implant pad readout
has been modified slightly.
- **Exile (Green)** -- In addition to past functionality, station
shuttle controls (public, mining, etc.) will be unresponsive for the
implantee. Flimsy, but more effective than a stern warning not to come
back from lavaland.
- **Beacon (Yellow)** -- Implantee becomes a teleporter beacon. The
prisoner console will report if their currently occupied area is
hazardous or not, so half of the security team doesn't blindly teleport
into space or lava. Disables after the implantee is dead for 10 minutes.
Available from Cargo.
- **Teleport Blocker (Deep Blue, not shown)** -- Prevents the implantee
from being teleported. Ever wanted to keep a wizard or cultist in a
cell? This is where you can start. Available from Cargo, expensive and
scarce.

Each of the implants has some application that would benefit security if
used on a captured criminal. Their usefulness may overlap in some
places, but the overall range of control these implants give security is
broadened.

</details>

The implant control console has also been given a small facelift.
Certain implants provide more useful readouts that can help officers
locate, control, or capture an implantee, rewarding cooperation between
officers.

It has also been totally converted into TGUI by @MrMelbert. Kickass!

Also, You can now remotely destroy implants, either to relieve criminals
from their punishment or to make room for a different implant. Wardens
should keep hold of their ID and remember to log out, since a motivated
convict could use it to shed their implants!


![tgui](https://github.com/tgstation/tgstation/assets/28870487/3c2ae99f-9c1d-4b18-b4cb-942cc96bcafe)

Everything made in this PR _should_ be scaleable enough to allow for new
security implant types to be implemented with relative ease. The
teleport-blocker implant was a last minute attempt to prove it to
myself. I had a few more ideas for implants in my head, but figured this
PR was already getting big and ugly enough. That is all for another day.

I truly apologize if there's anything I've missed in here. I did a lot
of this over a long period of time and kind of just... sat on it for a
while. If there's any confusing our unexplained changes, feel free to
point them out and I'll try to give an explanation.
## Why It's Good For The Game

The goal of this PR is to give a bit more depth to security's armory
implants. The intent is to present a choice in what implants are given
(rather than just tracker and maybe chem if you're feeling spiteful),
and to make them more useful as punitive/monitoring tools.

The tracker implant needed a nerf (and probably still does regardless of
this PR's success). It's never used for tracking since the teleporter
beacon is much more direct (+ gives a virtually free attack
opportunity), and the tracking range was incredibly subpar. I'd rather
not take toys away from security, but having the best option not be
roundstart gear feels like a fair compromise.

Warden content. Wardens have more gear to budget for and use at their
own (or the HOSes) discretion. The changes to the prisoner console allow
them to coordinate with officers to get good value out of the implants
they've chosen for an implantee.

Gives antagonists an alternate way to get de-implanted, without external
help, that can only be granted at the fault of security. Wardens who
dish out implants must keep an eye on the people carrying them!
## Changelog
:cl: Rhials, MrMelbert
add: The Tracker implant has had its teleport beacon functionality
migrated to the new (cargo accessible) Beacon implant.
add: Teleport Blocker security implant, that prevents the implantee from
teleporting by any means. Purchasable from cargo.
add: Security implants may now be harmlessly self-destructed at the
Prisoner Management Console.
balance: The Tracker implant tracking radius has increased from 20 to 35
tiles. The Prisoner Management Console will track and display the area
the implantee is in as well.
balance: The exile implant now prevents implantees from operating
shuttle controls.
code: Various code improvements and removal of unused vars in the
Prisoner Management Console
code: The HUD slots for chem/tracking implants have been converted to
display any implant with the IMPLANT_TYPE_SECURITY flag and an
associated sprite.
spellcheck: Modifies various implant pad readouts, removing false
information and rewriting some sections.
/:cl:

---------

Co-authored-by: MrMelbert <kmelbert4@gmail.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[971bc2611b...](https://github.com/tgstation/tgstation/commit/971bc2611befddba3c774d838b7bed46b462775e)
#### Monday 2023-12-18 17:32:03 by Ghom

The Spectre-Meter App, also a bootleg data disk item for the black market. (#80188)

## About The Pull Request
This PR adds in a new app that scans the nearby area for "spookiness"
(e.g. presence of ghosts, mobs with the spirit biotype, objects made
with hauntium or containing hauntium). A bit clunky by all means. It's a
maintenance app, and as such is more often found in the rare maintenance
computer disks, or downloadable from emagged PDAs (IIRC), or perhaps the
black market item which I've also added here as well, that might contain
it amongst other things.

Oh, if you also have the camera app, it'll let you take pictures of
ghosts like the 'camera obscura' does.

Oh, and there's also a maintenance version of the arcade program too;
just , like, lazier and easier.

## Why It's Good For The Game
Mostly a shower thought, 'cause I felt the idea maintenance disks to be
quite interesting yet lackluster, almost too niche. As for the remote
thought of using the app for validhunting, it isn't something you can
reliably get every and every other round, and if someone's got enough
ghosts circling them, chances are they're some big, loud antag or doing
something so cheeky, that they kinda deserve it.

Also, yeah, more black market stuff. Except for the misc section, it's
pretty lacking in uniqueness.

Screenshot of the UI, taken at the distance of one tile from a revenant:
![screenshot of the
UI](https://github.com/tgstation/tgstation/assets/42542238/402e2533-ae62-42c2-b90d-a3877940fb2c)

## Changelog

:cl:
add: The Spectre-Meter modular computer app. A little, amatuerishly
coded app that, as the name implies, scan an area for spectral presence.
It can be found amongst other apps in maintenance computer disks.
add: An easier, lazier version of the Arcade app, also found in
maintenance.
add: Black market computer disks, which contains programs not readily
available to the average assistant.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [cuttius/dagster](https://github.com/cuttius/dagster)@[5168f5a8ee...](https://github.com/cuttius/dagster/commit/5168f5a8ee14ef0af13ff65c9f567d7b27deb437)
#### Monday 2023-12-18 17:40:53 by quantum-byte

Fix #7442 / multi threading dropped log entries issue (#18493)

## Summary & Motivation

This MR should (based on my code understanding and testing) fix [issue
7442](https://github.com/dagster-io/dagster/issues/7442). It also fixes
in general randomly dropped user written log messages if logs are being
recorded from multiple threads.
Logging is quite important and its quite annoying to work around this
limitation/bug.

Maybe @sryza or @OwenKephart can have a look, since they already looked
into the 7442 issue.

## How I Tested These Changes

I tested the changes locally with an op/graph, which starts multiple
threads and logs multiple messages in each thread.

```python
import logging
import threading
import time

from dagster import AssetKey, AssetMaterialization, Output, job, op, repository

logger = logging.getLogger(__name__)


def background_thread(thread_name):
    for i in range(0, 5):
        logger.info(f"Background thread: {thread_name} {i}")
        time.sleep(0.5)


@op
def op1():
    yield AssetMaterialization(asset_key=AssetKey(["asset1"]))

    threads = []
    for thread_name in range(0, 5):
        thread = threading.Thread(
            name="background_thread",
            target=partial(background_thread, thread_name),
        )
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    yield AssetMaterialization(asset_key=AssetKey(["asset2"]))
    yield Output(123)


@op
def op2(arg):
    logger.info(f"Result of op1: {arg}")


@job
def dropped_events_job():
    op2(op1())


@repository
def dropped_events_repository():
    return [dropped_events_job]
```

Without my change i was missing a significant chunk of the expected log
messages in the captured log output:

![dropped_logs_without_change](https://github.com/dagster-io/dagster/assets/17649269/d777483a-911b-4010-b2e3-48bf7128437d)

With my change i had the exact amount of log messages in the captured
log output that i expected:

![no_dropped_logs_with_change](https://github.com/dagster-io/dagster/assets/17649269/d09f3617-fa86-415c-b7de-0dadab078b5b)

I also tested the original reproducing code from
https://github.com/dagster-io/dagster/issues/7442:

Without my change:

![grayed_out_op1_without_change](https://github.com/dagster-io/dagster/assets/17649269/c32c39ea-33a6-4207-a8c1-b8ddd30aa437)


With my change:

![green_op1_with_change](https://github.com/dagster-io/dagster/assets/17649269/fac597a6-4e2c-428b-afa4-f7695667ade7)


I am not that familiar with the dagster code. If you can point me to a
place where a unittest for this might go and some info on how to test it
in your opinion, than i will have a look at it.

---------

Co-authored-by: Florian Kaufmann <florian.kaufmann@corpuls.com>

---
## [petre-symfony/30-Days-with-Last-Stack-2023](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023)@[a002c957e7...](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023/commit/a002c957e7e1d947a30dea1d8acb530cb6dea4a6)
#### Monday 2023-12-18 17:44:19 by petrero

10.6 But adding target="_top" to each frame is a bit safer.
 Hiding Content Not in a Frame
 - So this is working super well! Except for the fact that if the user does ever get to the planet show page, we have an extra set of links. We really only want to show those when we're inside the <turbo-frame>. How can we do that?

 When Turbo sends an Ajax request for a <turbo-frame>, it does add a request header that tells your app that this is a Turbo Frame request. You can use that inside Symfony to conditionally do different things... like conditionally render these links.

 We are going to do that one time later in the tutorial. However, I try to minimize this: it adds complexity. Another option is to hide extra stuff with CSS! For example, we could add a class onto the sidebar... then only show these links if we're inside that class.

 However, Tailwind doesn't really work like that. In Tailwind, you can't change styling conditionally based on your parent. At least not out-of-the-box. But we can do this with a trick called a variant.

 The first thing to notice is that a <turbo-frame>, by default, looks like this: exactly like we have in our template. But as soon as we click a link, it has a src attribute. We can take advantage of that by adding a way inside of Tailwind to style elements conditionally based on whether they are inside of a <turbo-frame> that has a src attribute. Because, it will have a src over here... but won't have a src inside of this <turbo-frame>... because it never navigates. In fact, it would be a good idea to add a target="_top" to this frame, since we don't need fancy frame navigation on this page.

 Anyway, Tailwind variants are a bit more advanced, but simple enough. Import this plugin module, then go down to plugins. I'll paste in some code

 This adds a variant called turbo-frame: you'll see how we use that in a second. It basically applies to an element that's inside a <turbo-frame> that has a src attribute.

 Because we called this turbo-frame, copy that. Now, in show.html.twig, add a hidden class to hide this div by default.

 When we refresh, it's gone. But then, if we match our turbo-frame variant, change to display block

 Check it out. When we refresh, those links are still hidden. But over here... we've got them! Because we're inside a turbo-frame with a src attribute, our variant activates and the display block takes over.

 Turbo Frames do add some complexity, but we've only started to scratch the surface on what they make possible.

 Tomorrow, when I hover over each planet, I want to add a cool popover with more planet info. To make that happen, we're going to install another third-party Stimulus controller.

---
## [Jasonwei08/AdventureGame01](https://github.com/Jasonwei08/AdventureGame01)@[70e242e1c7...](https://github.com/Jasonwei08/AdventureGame01/commit/70e242e1c74778f9ce598f02e49255d523881bde)
#### Monday 2023-12-18 18:26:02 by VLADIMIR YAKUSHKIN

Jason just gave me breakfast lunch and dinner because he COOKED CALL HIM RATATOUILLE HE GO SQUEAK SQUEAK

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[755e3c0002...](https://github.com/RalphHightower/RalphHightower/commit/755e3c0002dbb5e243d28e249d32c54c5db27823)
#### Monday 2023-12-18 18:33:39 by Ralph Hightower

[docs](web): CalvinAndHobbes(extended description) 

| **[The History Behind Calvin and Hobbes (& Where to Read Bill Watterson's Classic Strips)](https://www.cbr.com/calvin-hobbes-reading-guide/ )** |
| [Why Bill Watterson Named his Characters Calvin and Hobbes](https://www.cbr.com/calvin-hobbes-name-inspiration-trivia/ ) |
| [10 Best Calvin and Hobbes Comics Set In A Winter Wonderland](https://www.cbr.com/calvin-and-hobbes-best-winter-wonderland-comics/) |
| [Calvin & Hobbes' Best Summer Adventures](https://www.cbr.com/calvin-hobbes-best-summer-vacation-comic-strips/ ) |
| [15 Best Calvin And Hobbes Snowman Comic Strips](https://www.cbr.com/best-calvin-hobbes-snowman-comics/ ) |
| [Calvin & Hobbes 10 Most Beloved Stories](https://www.cbr.com/best-calvin-hobbes-stories/ ) |
| [Calvin & Hobbes 10 Best Characters](https://www.cbr.com/calvin-n-hobbes-favorite-characters/ ) |
| [Calvin And Hobbes 10 Most Beloved Running Gags](https://www.cbr.com/calvin-and-hobbes-best-beloved-running-jokes/ ) |
| [15 Times Calvin & Hobbes Broke Our Hearts](https://www.cbr.com/calvin-hobbes-sad-comics/ ) |
| [10 Things Calvin & Hobbes Did Better Than Any Other Strip](https://www.cbr.com/calvin-n-hobbes-best-comic-strip/ ) |
| [How Hobbes Stole the Spotlight in Calvin and Hobbes](https://www.cbr.com/hobbes-better-than-calvin-comic-strips/ ) |
| [Greatest Calvin and Hobbes Strips Ever Published](https://www.cbr.com/greatest-calvin-and-hobbes-newspaper-strips/ ) |
| [10 Most Surreal Calvin and Hobbes Comics About Dinosaurs](https://screenrant.com/10-most-surreal-calvin-and-hobbes-comics-dinosaurs/ ) |
| [Calvin's Iconic Moments In Calvin & Hobbes](https://www.cbr.com/calvin-hobbes-best-calvin-stories/ ) |
| [10 Lessons Calvin & Hobbes Taught Us About Love](https://www.cbr.com/calvin-and-hobbes-lessons-taught-about-love/ ) |
| [Best Calvin's Mom Strips In Calvin & Hobbes, Ranked](https://www.cbr.com/calvin-and-hobbs-mom-comic-strips-ranked/ ) |
| [15 Best Calvin and Hobbes Comic Strips Of All Time](https://www.cbr.com/greatest-calvin-and-hobbes-newspaper-strips/ ) |
| [The Funniest Calvin & Hobbes Comics Of All Time](https://www.cbr.com/calvin-hobbes-funny-comics/ ) |

---
## [google/boringssl](https://github.com/google/boringssl)@[a942d57207...](https://github.com/google/boringssl/commit/a942d572073e98944200e154597442796fdb13de)
#### Monday 2023-12-18 18:59:59 by David Benjamin

Support lists and code blocks in doc.go

Our documentation comments already include examples of code blocks
and lists, they just don't get rendered right. We also have things that
were trying to be lists but aren't. Go ahead and add support for it, and
fix the handful of list-like things that didn't get rendered as lists.

I took inspiration from CommonMark (https://spec.commonmark.org/0.30/)
to resolve questions such as whether blank lines are needed between
lists, etc., but this does not support any kind of nesting and is still
far from a CommonMark parser. Aligning with CommonMark leaves the door
open to pulling in a real Markdown parser if we start to need too many
features. I've also borrowed the "block" terminology from CommonMark.

One ambiguity of note: whether lists may interrupt paragraphs (i.e.
without a blank line in between) is a little thorny. If we say no, this
doesn't work:

   Callers should heed the following warnings:
   1) Don't use the function
   2) Seriously, don't use this function
   3) This function is a bad idea

But if we say yes, this renders wrong:

   This function parses an X.509 certificate (see RFC
   5280) into an X509 object.

We have examples of both in existing comments, though we could easily
add a blank line in the former or rewrap the latter. CommonMark has a
discussion on this in https://spec.commonmark.org/0.30/#lists

CommonMark says yes, but with a hack that only lists starting with 1 can
interrupt paragraphs. Since we're unlikely to cite RFC 1, I've matched
for now, but we may want to revisit this if it gets to be a pain. I
could imagine this becoming a problem:

   This function, on success, does some stuff and returns
   1. Otherwise, it returns 0.

But that looks a little weird and we usually spell out "one" and "zero".
I printed all the lists we detected in existing comments, and this has
not happened so far.

I've also required fewer spaces than CommonMark to trigger a code block.
CommonMark uses four, but four spaces plus a leading "//" and a " " is
quite a lot. For now I'm not stripping the spaces after the comment
marker at comment extraction time and then requiring three spaces, so
two spaces relative to normal text. This is mostly to match what we've
currently been doing, but we can always change it and our comments
later.

Change-Id: Ic61a8e93491ed96aba755aec2a5f32914bdc42ae
Reviewed-on: https://boringssl-review.googlesource.com/c/boringssl/+/64930
Reviewed-by: Bob Beck <bbe@google.com>
Commit-Queue: David Benjamin <davidben@google.com>

---
## [petre-symfony/30-Days-with-Last-Stack-2023](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023)@[7ee1c1fe31...](https://github.com/petre-symfony/30-Days-with-Last-Stack-2023/commit/7ee1c1fe310c976f048aef95dd1c5fe2bbee98a7)
#### Monday 2023-12-18 19:31:26 by petrero

11.12 Remembering the Ajax Call
 - Do we have time for one more thing? When we hover over the element, it makes the AJAX call. And... it repeats that every time we hover. It doesn't remember the content from the AJAX call.

 That's due to how the popover controller works... and if I had been less stubborn and used its way of Ajax-loading content, it wouldn't be a problem. Anyway, each time we hover, it creates the turbo-frame, destroys it, creates a new one, destroys it, etc.

 So: how can we make the controller remember the content? I have no idea! But let's go look inside the code. In assets/vendor/stimulus-popover/, open this file. The contents are minified... but a quick Cmd+L to reformat the code fixes that. How cool is this? We can now read this vendor file - and even add temporary debugging code if we needed to. And... I think I see a way that we can make this work.

 Just like with Symfony controllers, we can override Stimulus controllers. Inside the controllers/ directory, create our own popover_controller.js. Then I'll paste in some code

 Normally we import Controller from Stimulus and extend that. But in this case, I'm importing the popover controller directly and extending that. Then we override the show method and hide method to toggle a hidden class instead of fully destroying the element.

 And now that we have our own controller named popover, in bootstrap.js, we don't need to register the one from Stimulus components. The popover controller will be our controller... then we leverage the Stimulus components controller via inheritance.

 Moment of truth! It loads once... then remembers its content!

 Not only did we create the perfect popover, we can now easily repeat this on other parts of our site. If you're wondering if we could reuse some of the popover markup... stay tuned for Day 23 when we talk about Twig Components.

 That's a wrap for today! Get some well-deserved rest, because tomorrow we'll write a tiny, yet mighty, Stimulus controller called auto-submit.

---
## [thorntonprime/i](https://github.com/thorntonprime/i)@[593f8dc481...](https://github.com/thorntonprime/i/commit/593f8dc481e06d4afbbc52505a801480f65a105d)
#### Monday 2023-12-18 20:10:35 by Thornton Prime

how we stop playing
where i feel pain and you feel sympathy

i just want to play the game
where i lay there with my hand resting at the base of your spine
and i am telling you stories through my touch
and then we switch
and you lay your hand on my back between my shoulder blades
and i am feeling your dreams

---
## [crawl/crawl](https://github.com/crawl/crawl)@[dee8a45240...](https://github.com/crawl/crawl/commit/dee8a452401778e92e71214ace4c6be27690bf66)
#### Monday 2023-12-18 20:32:02 by DracoOmega

Wereblood -> Fugue of the Fallen (level 3 Necromancy)

Wereblood has had somewhat weird thematics ever since Shapeshifting took
over all of the 'transform self' effects from Transmutations. Necromancy,
on the other hand, is a natural fit for a spell that is powered by killing
things.

This has the following mechanical changes over current Wereblood:
 -The healing effect is removed
 -Ally kills now boost the effect (but allies themselves do not benefit
  from it in any way)
 -Max stacks reduced to 7 instead of 9
 -At maximum stacks, successful hits will inflict minor pain damage to all
  adjacent targets to the one you attacked. A little bonus for the tricky
  task of maxing it!
 -Moved to level 3

I haven't put this in the necromancy starter book. Wereblood was never great
at low levels, since you usually can't sustain fights long enough to build
it and struggle to kill already. I think there's no way a necromancy wants
to use their mp on this instead of vampiric draining, and it's more
interesting if the spell is intended for later use. Also: this gives players
more incentive to splash necromancy on a hybrid that doesn't involve allies!

To avoid the player needing to worry about whether any individual monster
they kill has a 'soul' or whatever, the spell is themed as using fresh
death to draw in the spirits of the long-dead that already linger everywhere
in the dungeon (I mean, there's enough corpses in every inch of the dungeon
that BVC works, right? :P)

(Spellbooks have not yet been adjusted. I'm waiting on further Alchemy
changes to do a comprehensive reshuffling.)

---
## [yrdzrfxndfvh/crawl](https://github.com/yrdzrfxndfvh/crawl)@[5f6fb4f5a3...](https://github.com/yrdzrfxndfvh/crawl/commit/5f6fb4f5a389a722ff4ee7fd78d4e43f979cce6c)
#### Monday 2023-12-18 20:33:58 by regret-index

Add and trim a few Xom spells and cloud trails.

New spells: Wereblood, Animate Armour, Battlesphere, Malign Gateway.
Wereblood forces the player to make noise and thus is neat as a mixed
blessing, Animate Armour gets to by-pass its innate castability versus
armour weight issues to be more interesting as a random free god act,
Battlesphere makes for a decent joke if not actually usable and compensates
for the power of the two summons here, Malign Gateway has been missing
since the miscast streamlining and is extremely appropriate between the
chaos brand and unavoidable neutrality.

(These all are exchanged for Canine Familiar, which can't use one of its
most interesting aspects in the recast and thus will mostly make players
unavoidably get drained and guilt.)

New cloud trail clouds are salt and blastmotes, both at miniscule chances.
The salt's purpose is obvious, while the blastmotes are manually set at 25
power (power with those is weird and modular) and definitely give a certain
kind of danger and excitement very distinct from the spell by getting them
without having to stop for laying each of them.

---
## [LunarWatcher/AoC2023](https://github.com/LunarWatcher/AoC2023)@[aed64a41fd...](https://github.com/LunarWatcher/AoC2023/commit/aed64a41fdc748e3caf7b3c0c6f440bc922ca77a)
#### Monday 2023-12-18 20:35:47 by Olivia

Broken day 12

Fuck you windows, just TELL ME THE ERROR MESSAGE! It should not be necessary for me to install and figure out visual studio to get a simple fucking error message in the console

---
## [Noway-code/Checked](https://github.com/Noway-code/Checked)@[61ed9fcbeb...](https://github.com/Noway-code/Checked/commit/61ed9fcbebb4b632c86ebbd650ca56d8087a68b6)
#### Monday 2023-12-18 21:22:13 by noway

remove node modules from main branch
Our Father, Who art in heaven, Hallowed be Thy Name. Thy Kingdom come, Thy Will be done, On earth as it is in Heaven. Give us this day, our daily bread, And forgive us our trespasses, as we forgive those who trespass against us. And lead us not into temptation, but deliver us from evil.

---
## [ZephyrTFA/tgstation](https://github.com/ZephyrTFA/tgstation)@[a5fabd8819...](https://github.com/ZephyrTFA/tgstation/commit/a5fabd881961cc0c26fdcc93a23a973af1c5cdc3)
#### Monday 2023-12-18 21:31:17 by Profakos

Changes to the lore of Knock (#79542)

## About The Pull Request

This PR renames Knock to Lock, and changes most of the knowledge gain
lore.

## Why It's Good For The Game

The Knock Lore, is based on the Knock Principle from Cultist Simulator,
with the path description being copied from the wiki. Many other
keywords and concepts are fully lifted from that game (Locksmith's
Secret, Mother Of Ants, etc). In my vision, if a heretic path has to be
based on a principle from cultist simulator, it should have its own
spin, and also, the knowledge gain texts should tell a story. For
example, Ash tells the story of a watchman burning down their city after
being betrayed, and Cosmic is a love story between a knowledge seeker
and a monster from the beyond.

So I have decided to reflavour Knock. I have changed the name to Lock,
so at least it would feel similar, just like how Blade is akin to Edge.
Many powers also block people or confuse their paths instead of opening
new ways, and thus, I feel a path whose name implies that it *both*
opens and closes would be more self describing.

I have changed most of its lore to be about the Locked Labyrinth, where
knowledge seekers willingly trap themselves and submit themselves to
servitude to find ultimate freedom by progressing through its trials.
These are the Stewards, who are basically workers in an infinite and
malicious hotel in their dreams. Consider them assistants if you will
(this wasn't my intention when I wrote the lore, but thinking about it
in retrospect, it honestly fits). In the implied story, the heretic
joins their ranks, but keeps getting closer to the more corrupt members,
along with parasitic spirits. Ultimately, they manage to open the
Labyrinth's core, letting out the Stewards, allowing them to manifest in
the forms of heretic summon creatures.

The side path spells and the lock knowledge ritual I have not touched,
they were fine. Some items have been renamed and repathed.

I have kept the distinctive sound effect for using the Grasp, as its
unique enough. Though if someone did have a nice sound effect for
turning a lock and added some filters, I would add it.

**DB Issue**

I have renamed the achievement's define to MEDAL_LOCK_ASCENSION but kept
the value as "Knock", as I don't know how trigger a change in the DB. If
this is a blocking change, I'll try to figure out how to make a
migration file.

**Future improvements**

I would also come back later with another PR, that hands out names to
the eldritch beings spawned by the portal, based on the Stewards in the
knowledge gain lore that I added, along with some new ones that fit the
theme, and some jokey ones like Minotaur.

## Changelog

:cl:
spellcheck: Renamed Knock to Locks, and changed most of the flavor text
of knowledge gain, and renamed some items and knowledges from the path.
/:cl:

---
## [apollographql/federation](https://github.com/apollographql/federation)@[4e630d964e...](https://github.com/apollographql/federation/commit/4e630d964eeeba5a42ecd13f02f6e8f5b757523e)
#### Monday 2023-12-18 21:34:09 by Edward Huang

docs: fix broken links (#2885)

<!--
First, 🌠 thank you 🌠 for taking the time to consider a contribution to
Apollo!

Here are some important details to follow:

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

* Federation versions
Please make sure you're targeting the federation version you're opening
the PR for. Federation 2 (alpha) is currently located on the `main`
branch and prior versions of Federation live on the `version-0.x`
branch.

* 📖 Contribution guidelines
Follow
https://github.com/apollographql/federation/blob/HEAD/CONTRIBUTING.md
when submitting a pull request. Make sure existing tests still pass, and
add
        tests for all new behavior.

* ✏️ Explain your pull request
Describe the big picture of your changes here to communicate to what
        your pull request is meant to accomplish. Provide 🔗 links 🔗 to
        associated issues!

We hope you will find this to be a positive experience! Open source
contribution can be intimidating and we hope to alleviate that pain as
much
as possible. Without following these guidelines, you may be missing
context
that can help you succeed with your contribution, which is why we
encourage
discussion first. Ultimately, there is no guarantee that we will be able
to
merge your pull-request, but by following these guidelines we can try to
avoid disappointment.

-->

---
## [MagicQuest/MagicQuest.github.io](https://github.com/MagicQuest/MagicQuest.github.io)@[91c7d03550...](https://github.com/MagicQuest/MagicQuest.github.io/commit/91c7d03550d97c88d9f0d6c140ea4f742dc22303)
#### Monday 2023-12-18 21:46:22 by David Foster

suprising changes

next time might be a bigger change but this push has some random ahh changes

chaosmawebgpu.html - i was looking at a large list of javascript test problems and i think i wrote the link down somewhere in typingtest.html
anyways they used call and bind in the same problem and i realized that call is what i was expecting

fnf\index.html - for some reason sometimes the songs just don't load and give me a readystate of 3?

games\adhdtrap.html - haha i was watching angel scroll on tiktoks and this showed up so i thought i could recreate it (cgmatter/defaultcube has made like 30 tutorials with balls being stuck in a circle (how tf do i explain that) anyways i just remembered how to do that but the hard part was getting them to bounce)

v3\index.html - a while ago i learned that i can just connect to a different ip with socket.io so imma figure that out soon

also im typing this with only a keyboard because my mouse is plugged in to my pi

---
## [dieamond13/tgstation-dieamond](https://github.com/dieamond13/tgstation-dieamond)@[9229adc934...](https://github.com/dieamond13/tgstation-dieamond/commit/9229adc934b9575a8528b6efc0074fcc2921cc33)
#### Monday 2023-12-18 21:49:39 by DaydreamIQ

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
## [dieamond13/tgstation-dieamond](https://github.com/dieamond13/tgstation-dieamond)@[8c0becb4f0...](https://github.com/dieamond13/tgstation-dieamond/commit/8c0becb4f08ec50e00ed758022e18fb1381f4f25)
#### Monday 2023-12-18 21:49:39 by Da Cool Boss

Makes oculine taste slightly better (#79919)

## About The Pull Request
Changes oculine's taste from 'dull toxin' to 'earthy bitterness'.
Probably deserves the no GBP tag.
## Why It's Good For The Game
Oculine is a benign/helpful chem that naturally occurs in carrots. This
means it's in all carrot based food the chef cooks, and if the carrots
cross pollinate with another plant it's in those too. This is currently
a problem, because it means the chef's carrot sticks taste like poison
and this tends to freak out new players who don't know that's just what
oculine tastes like.

Oculine has no negative effects besides potentially triggering a medical
allergy quirk, it can't even be overdosed. So if you see a worrying "you
taste dull toxin" message, there's actually no reason to be concerned.
Still, I see players who are *convinced* the chef is poisoning their
carrot cakes fairly regularly. This should cut down on wasted multiver
and lynched chefs.

I changed it to "earthy bitterness" because that's what some species of
carrot taste like, and "bitterness" implies medicine. The paranoid can
still assume they're being dosed with morphine or something, but they're
not being misled into thinking this. For people chugging medicine
bottles from chemistry, oculine stands out a little less too.
## Changelog
:cl:
qol: Oculine now tastes bitter, and not like toxin.
/:cl:

---
## [getzola/zola](https://github.com/getzola/zola)@[22dc32a589...](https://github.com/getzola/zola/commit/22dc32a5893deac5e91d173d0daf59e1868065ef)
#### Monday 2023-12-18 22:24:08 by sinofp

Add support for lazy loading images (#2211)

* Add optional decoding="async" loading="lazy" for img

In theory, they can make the page load faster and show content faster.

There’s one problem: CommonMark allows arbitrary inline elements in alt text.
If I want to get the correct alt text, I need to match every inline event.

I think most people will only use plain text, so I only match Event::Text.

* Add very basic test for img

This is the reason why we should use plain text when lazy_async_image is enabled.

* Explain lazy_async_image in documentation

* Add test with empty alt and special characters

I totaly forgot one can leave the alt text empty.
I thought I need to eliminate the alt attribute in that case,
but actually empty alt text is better than not having an alt attribute at all:
https://www.w3.org/TR/WCAG20-TECHS/H67.html
https://www.boia.org/blog/images-that-dont-need-alternative-text-still-need-alt-attributes
Thus I will leave the empty alt text.

Another test is added to ensure alt text is properly escaped.
I will remove the redundant escaping code after this commit.

* Remove manually escaping alt text

After removing the if-else inside the arm of Event::Text(text),
the alt text is still escaped.
Indeed they are redundant.

* Use insta for snapshot testing

`cargo insta review` looks cool!

I wanted to dedup the cases variable,
but my Rust skill is not good enough to declare a global vector.

---
## [tedthedragon/haruto-graphtool](https://github.com/tedthedragon/haruto-graphtool)@[d32d6d934d...](https://github.com/tedthedragon/haruto-graphtool/commit/d32d6d934d73aa2350b1f1aa54a9d8558b556c3f)
#### Monday 2023-12-18 22:27:31 by ted the praimortis

- Fix things.

Asshole. Bitch. FUck. Shit ass. Cunt.

---
## [tesselslate/advent](https://github.com/tesselslate/advent)@[4c0dfa427e...](https://github.com/tesselslate/advent/commit/4c0dfa427ef3a586ebf89757183b831ea8867e9e)
#### Monday 2023-12-18 22:48:07 by tesselslate

2023: day 18

i did it this morning but my code was awful. i kind of learned how shoelace formula and picks theorem work but like not that deeply so hopefully no future problems require you to get more goofy

---
## [zygoloid/carbon-lang](https://github.com/zygoloid/carbon-lang)@[c7e6238fa8...](https://github.com/zygoloid/carbon-lang/commit/c7e6238fa8dd57672b0765e738f4c425a27cac3b)
#### Monday 2023-12-18 23:13:32 by Chandler Carruth

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
## [SpringSkipper/Skyrat-tg](https://github.com/SpringSkipper/Skyrat-tg)@[caa13c44af...](https://github.com/SpringSkipper/Skyrat-tg/commit/caa13c44af926e36843fdeb8c50460d6566a6cd7)
#### Monday 2023-12-18 23:22:32 by SkyratBot

[MIRROR] Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished [MDB IGNORE] (#25038)

* Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished (#79694)

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

* Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [SpringSkipper/Skyrat-tg](https://github.com/SpringSkipper/Skyrat-tg)@[318d5b38d7...](https://github.com/SpringSkipper/Skyrat-tg/commit/318d5b38d734129579050a98107b044cfb2791e2)
#### Monday 2023-12-18 23:22:32 by SkyratBot

[MIRROR] Fixes Relay Attackers Misfire [MDB IGNORE] (#25039)

* Fixes Relay Attackers Misfire (#79731)

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

* Fixes Relay Attackers Misfire

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [SpringSkipper/Skyrat-tg](https://github.com/SpringSkipper/Skyrat-tg)@[41026ae8b1...](https://github.com/SpringSkipper/Skyrat-tg/commit/41026ae8b1a14b9380ca7af9885939c9f2dc060e)
#### Monday 2023-12-18 23:25:22 by SkyratBot

[MIRROR] Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun [MDB IGNORE] (#25365)

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun (#80030)

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

* Replaces the fake monkey cube in Birdshot tool storage with a less lethal one, adds something else fun

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[e174990dd5...](https://github.com/cockroachdb/cockroach/commit/e174990dd5015a38b1e9bc6723f270dbe647c3a3)
#### Monday 2023-12-18 23:27:25 by craig[bot]

Merge #113809

113809: kvstreamer: add limit to how many eager batches are issued r=yuzefovich a=yuzefovich

**kvstreamer: add limit to how many eager batches are issued**

This commit fixes extremely suboptimal behavior of the streamer in the
InOrder mode in some cases. In particular, previously it was possible
for the buffered responses to consume most of the working budget, so the
streamer would degrade to processing all requests effectively one
BatchRequest with one Get / Scan at a time, significantly increasing the
latency. For example, the query added as a regression test that performs
30k Gets across 10 ranges would usually take on the order of 1.5s (which
is not great already since in the non-streamer path it takes 400ms), but
in the degenerate cases it could be on the order of 20-30s.

Similar behavior could occur in the OutOfOrder mode too where we would
issue more BatchRequests in which only one request could be satisfied
(although in OutOfOrder mode the problem is not as severe - we don't
buffer any results since we can always return them right away).

This problem is now fixed by imposing the limit on the budget's usage at
which point the streamer stops issuing "eager" requests. Namely, now,
when there is at least one request in flight, the streamer won't issue
anymore requests once `limit * eagerFraction` is exceeded. This
effectively reserves a portion of the budget for the "head-of-the-line"
batch.

The "eager fraction" is controlled by a session variable, separate for
each mode. The defaults of 0.5 for InOrder and 0.8 for OutOfOrder modes
were chosen after running TPCH queries and the query that inspired this
commit. These values bring the number of gRPC calls for the reproduction
query from 1.5k-2k range to below 200 and the query latency to be
reliably around 400ms.

I don't really see any significant downsides to this change - in the
worst case, we'd be utilizing less of the available memory budget which
is not that big of a deal, so I intend to backport this change. Also,
setting the eager fractions to large values (greater than 1.0 is
allowed) would disable this limiting behavior and revert to the previous
behavior if we need it.

Fixes: #113729.

Release note (bug fix): Previously, when executing queries with
index / lookup joins when the ordering needs to be maintained,
CockroachDB in some cases could get into a pathological behavior
which would lead to increased query latency, possibly by 1 or 2 orders
of magnitude. This bug was introduced in 22.2 and is now fixed.

**kvstreamer: increase default avg response multiple**

This commit increases the default value for
`sql.distsql.streamer.avg_response_size_multiple` cluster setting from
1.5 to 3.0. This setting controls the factor by which the current "avg
response size" estimate is multiplied and allows for TargetBytes
parameter to grow over time. In the reproduction query from the
previous commit it was determined that the growth might not be as quick
as desirable.

The effect of this change is as follows:
- if we have responses of varying sizes, then we're now likely to be more
effective since we'll end up issuing less BatchRequests
- if we have responses of similar sizes, then we might pre-reserve too
much budget upfront, so we'll end up with lower concurrency across
ranges.

Thus, we don't want to increase the multiple by too much; however,
keeping it at 1.5 can be quite suboptimal in some cases - 3.0 seems like
a decent middle ground. This number was chosen based on running TPCH
queries (both via InOrder and OutOfOrder modes of the streamer) and the
reproduction query. (For the latter this change reduces the number of
gRPC calls by a factor of 3 or so.)

Release note: None

Co-authored-by: Yahor Yuzefovich <yahor@cockroachlabs.com>

---

