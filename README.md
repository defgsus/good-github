## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-29](docs/good-messages/2022/2022-11-29.md)


2,317,581 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,317,581 were push events containing 3,503,492 commit messages that amount to 272,545,144 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 53 messages:


## [Tastyfish/Skyrat-tg](https://github.com/Tastyfish/Skyrat-tg)@[fcebbd61a9...](https://github.com/Tastyfish/Skyrat-tg/commit/fcebbd61a909087393babf445b94e5aa271b42d8)
#### Tuesday 2022-11-29 00:36:24 by SkyratBot

[MIRROR] Basic Mob Carp Bonus Part: Wall smashing [MDB IGNORE] (#17791)

* Basic Mob Carp Bonus Part: Wall smashing (#71524)

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

* Basic Mob Carp Bonus Part: Wall smashing

* SR mobs

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: tastyfish <crazychris32@gmail.com>

---
## [gustavoloureirodosreis/recipe_app](https://github.com/gustavoloureirodosreis/recipe_app)@[7012674590...](https://github.com/gustavoloureirodosreis/recipe_app/commit/70126745908746d75b2b345aa329b0dc179b361d)
#### Tuesday 2022-11-29 00:45:58 by Gustavo

@A bunch of unhe nhee from ESLINT (FUCK YOU, ESLINT!)

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[37b60d187d...](https://github.com/lessthnthree/Skyrat-tg/commit/37b60d187daa6b8c8f2c2623dbf49555774a90aa)
#### Tuesday 2022-11-29 01:20:33 by SkyratBot

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
## [softcerv/Skyrat-tg](https://github.com/softcerv/Skyrat-tg)@[932d25cdeb...](https://github.com/softcerv/Skyrat-tg/commit/932d25cdebb11b433f6faefa9f983a91e2011a67)
#### Tuesday 2022-11-29 01:29:25 by SkyratBot

[MIRROR] Mail sorting helper, and disposals fixes [MDB IGNORE] (#17683)

* Mail sorting helper, and disposals fixes (#70861)

## About The Pull Request

![image](https://user-images.githubusercontent.com/2676196/198695007-53db1b70-845f-46a9-b98a-e146bb53951b.png)

This PR adds a mail sorting map helper, which during Late Initialization
will apply a sorting location index to the mail sorting disposals pipe
under them. I have replaced the varedits with all mail sorters with the
appropriate map helpers. I have thoroughly tested this, making sure
packages arrived to every location, where possible.

I have also fixed a few issues with the disposals network:

**Tramstation**

- One of the random maintenance segments had a place with no disposal
pipes. This has been fixed
- A sorter was looking for chapel and library packages, but it actually
meant to look for engineering packages
- There was no dormitory mail sorter, I have added one

**Metastation**

- There was no dormitory mail sorter, I have added one

**Icebox**

- There is no experimentor lab in icebox, but there is an
"experimentation" lab, which is good enough, so I have added it as a
location

**Deltastation**

- There was no dormitory mail sorter, I have added one
- Virology was not connected to the disposals network. However, on every
other map, it has a one way connection. I have hooked it up just like
that, so virology mail will arrive safely, and virology trash will go
into space as usual.

**Kilostation**

- Genetics packages were rerouted to the psychologist office

Unsolved issue on kilostation: there is no experimentor on this station,
and there is no space for a disposals in the circuits lab, so sadly, if
you send a package to this destination, it will come back to the mail
sorting office.

**Future improvements**

The TAGGERLOCATIONS list, which is used to retrieve the labels of the
various tags, is frankly unorganizable, and hard to expand. I have
delayed fixing this for a future PR.

I kinda wish to remove the sortType variable, as it is no longer
necessary to have it around with these helpers, but sadly, this would
ruin downstream maps, so I have no plans for this at the moment.

## Why It's Good For The Game

While mapping, having to constantly compare a comment in flavor_misc.dm
to figure out what to varedit a disposal mail sorter to is rather
annoying. These map helpers, similar to the access helpers, will help
with this issue.

Its also good if mail actually arrives.

## Changelog

:cl:
qol: added a mail sorting map helper, to allow mappers to create
disposal networks faster
fix: fixes several non working disposal mail targets that never received
their packages
/:cl:

* Mail sorting helper, and disposals fixes

* vr fixes

Co-authored-by: Profakos <profakos@gmail.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [EthanRockss/tgstation](https://github.com/EthanRockss/tgstation)@[a811adac74...](https://github.com/EthanRockss/tgstation/commit/a811adac74513494a620fae631da95d2626b1be7)
#### Tuesday 2022-11-29 01:49:33 by Epic

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
## [mucsci-students/2022fa-475-ArchTowerDefense](https://github.com/mucsci-students/2022fa-475-ArchTowerDefense)@[c083a58eb7...](https://github.com/mucsci-students/2022fa-475-ArchTowerDefense/commit/c083a58eb73f70595e86aa7161138edfd7797978)
#### Tuesday 2022-11-29 02:00:30 by Trevor Bender

Merge pull request #1 from mucsci-students/fucjk

fucjing stipud sufkc ufkc FUCK YOU GITHUB

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[83f475aa7e...](https://github.com/tgstation/tgstation/commit/83f475aa7ec4290c6961f1f14c5da80f340989b8)
#### Tuesday 2022-11-29 02:05:46 by tralezab

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
## [madsmars/finsta](https://github.com/madsmars/finsta)@[f281014698...](https://github.com/madsmars/finsta/commit/f281014698bc062da8ba1df5c58983a24bf5a0ea)
#### Tuesday 2022-11-29 02:41:51 by madsmars

fixed the jquery and added some images to the comics folder. remember that even tiny lil mistakes can make java stop working bc java is a lil bitch. we love her though.

---
## [airplanedev/lib](https://github.com/airplanedev/lib)@[a5978d8afe...](https://github.com/airplanedev/lib/commit/a5978d8afeee4652692dd3f3c2d2f39e369d64db)
#### Tuesday 2022-11-29 02:47:30 by Lee Weisberger

Send env vars when creating deployment (#411)

## Description
In bundle discovery, send env vars along with the bundles. Env vars are calculated from `airplane.yaml` and the task definition.

The original plan here was to calculate these in the bundler. However env vars contain secret values that must be resolved. I don't think we should do this in the bundler because we'd have to expose an endpoint to resolve secret values and the bundler doesn't have any sort of advanced authn. Let me know if you have any other thoughts here, or else we'll just send these with the bundle.

## Test plan
I wrote a unit tests

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[24ae11ad6f...](https://github.com/Paxilmaniac/Skyrat-tg/commit/24ae11ad6f6af9c0b6dab12986b95943f0cdf1f8)
#### Tuesday 2022-11-29 02:54:26 by SkyratBot

[MIRROR] Adds a reagent injector component and BCI manipulators to all circuit labs [MDB IGNORE] (#17617)

* Adds a reagent injector component and BCI manipulators to all circuit labs (#71236)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This PR adds a reagent injector component that's exclusive to BCIs.
(Requested to be integrated into BCIs by Mothblocks.)
When outside of a circuit, the component itself stores the reagents.
However, if it's inside of a BCI, the storage is moved to the BCI. The
storage can contain up to 15u of reagents and acts like an open
container. (However, it won't spill even if you throw it, it just acts
like an open container code-wise, don't worry about it.)
You can only have one reagent injector in a circuit. Trying to insert
multiple will give you an error message.
The entire dose is administered at once. (Requirement set by
Mothblocks.)

Please don't try to dispute any of the specific limitations in the
comments as they're out of my control. They're reasonable anyways.

Reagent Injector Input/Output:
Inject (Input Signal) - Administers all reagents currently stored inside
of the BCI into the user.
Injected (Output Signal) - Triggered when reagents are injected. Not
triggered if the reagent storage is empty.

New BCI Input:
Show Charge Meter (Number) - Toggles showing the charge meter action.
(Adds some capacity for stealth.)

Install Detector Outputs: (Added following a comment about having to use
weird workarounds for proper loops.)
Current State (Number) - Outputs 1 if the BCI is implanted and 0 if it's
not.
Installed (Signal) - Triggered when the BCI is implanted into it's user.
Removed (Signal) - Triggered when the BCI is removed from it's user.

This PR also adds BCI manipulation chambers to all currently present
circuit labs. (Solution proposed by Mothblocks.)
Yes I had to do some other mapping changes to allow for this. No I don't
have any mapping experience, why do you ask?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

One small step for BCIs, one giant leap for circuit kind. (First
"proper" circuit to human interaction in the entire game!)

This allows for some funky stuff and also makes it less of a pain in the
ass to use BCIs. What's not to love?

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
add: Added a reagent injector component and BCI manipulators to all
circuit labs. (+ install detector component)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Adds a reagent injector component and BCI manipulators to all circuit labs

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Co-authored-by: Paxilmaniac <paxilmaniac@gmail.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[f4335e5184...](https://github.com/Paxilmaniac/Skyrat-tg/commit/f4335e5184da0a4643bab601ae11c59e9d411a6e)
#### Tuesday 2022-11-29 02:54:26 by SkyratBot

[MIRROR] Fishing Odds Code Improvements and Rescue Hooks [MDB IGNORE] (#17697)

* Fishing Odds Code Improvements and Rescue Hooks (#71415)

## About The Pull Request
I wanted to try and implement an easier way for people to fish out
corpses from chasms, as I heard many tales of people trying to fish
others out of chasms and it taking over one IRL hour, with some cases
where it would take over two hours. Obviously, that's not really
interesting gameplay, and it doesn't really give people an incentive to
fish, it just turns it into an annoyance that people won't want to do
for fun. Now, we don't want that, do we?

As such, I've created the rescue hook, a special fishing hook that can
only be used in chasms (as that's currently the only place you can find
people into), which will only be able to fish out duds, skeleton
corpses, any mob that's fallen into a chasm and hasn't been rescued yet,
or rarely, a hostile monster lurking below. It has, at the time of
writing this, a weight of 5 (50 without bait, lower with bait) for duds
and a weight of 30 for chasm detritus, which themselves have a 50%
chance to be a random skeleton corpse, or a lobstrosity, and the
remaining 50% chance of fishing out a mob that's fallen into a chasm.
I'm open to tweaking these values if we think it's too easy or too hard,
but it's still a rather expensive item, so I'd consider it quite fine
the way it is myself, as it's still not risk-free.

It's currently only obtainable through buying it from cargo in the
goodies section, at a default price of 600 credits (making it
SIGNIFICANTLY more expensive than the rest of the fishing content, and
making it something that assistants will have to put some elbow grease
into if they want to be able to afford it).

As it stands currently, it can't be used to recover the fallen's
belongings that weren't on their person (i.e., their crusher if they
were holding it in hands), ~*but* I'm down to make that easier to fish
out using, for instance, the magnet hook, while also making it
incompatible with fishing out bodies, which would make it a nice way to
recover those lost items without spending over an hour fishing for them,
if that's something that maintainers would want.~ Maintainers did want
it, and as such...

The Magnetic hook is now the go-to hook to retrieve objects from chasms!
Not only does it inherently do a much better job at fishing out
non-fishes, it also has a lesser chance of retrieving random junk from
chasms, and an even lower chance of fishing out lobstrosities!

I also improved the code for the fishing weights calculation so that the
hooks and the rods can have an effect on the odds of certain types of
rewards more easily, with the option of offloading a more of what's
currently being calculated on `fishing_challenge` over on the rods or
even the hooks themselves.

I finished by fixing a handful of capitalization and punctuation issues
in various fishing items, as that bugged me when I was testing my
changes.

## Why It's Good For The Game
Corpses being recoverable from chasms was a great idea, however making
it so people would have to sink a major portion of their shift for a
chance at recovering a corpse doesn't create a particularly interesting
gameplay loop. However, being able to spend your hard-earned funds in
order to streamline that process without really being able to use that
to cheese other mechanics sounds like a great deal to me.

## Changelog

:cl: GoldenAlpharex
add: Added a Rescue Hook, that will allow the fishing rod it's attached
onto to become a lot more proficient at recovering corpses from chasms,
at the expense of making it unusable for more traditional fishing. It
isn't entirely lobstrosity-proof, however...
balance: The magnetic hook can no longer fish out corpses from chasms,
but will fish out items much more efficiently than any other hooks,
while also being much less attractive to lobstrosities. Some still fall
for it regardless, however.
spellcheck: Fixed the capitalization and punctuation in the description
of multiple fishing accessories.
code: Improved the code for fishing weights, to allow for different
hooks to have some more noticeable results on the weights without having
to add to an already massive proc.
/:cl:

* Fishing Odds Code Improvements and Rescue Hooks

Co-authored-by: GoldenAlpharex <58045821+GoldenAlpharex@users.noreply.github.com>

---
## [bwhua/SDSGC-Randomizer](https://github.com/bwhua/SDSGC-Randomizer)@[bcdd7a5d01...](https://github.com/bwhua/SDSGC-Randomizer/commit/bcdd7a5d01d88bf027d27cd0cf7bfddb3504fd7d)
#### Tuesday 2022-11-29 03:33:08 by JD

Add Knight of the Holy War Griamore, Flame of Life Escanor

---
## [Hatterhat/Skyrat-tg](https://github.com/Hatterhat/Skyrat-tg)@[bbaefcefeb...](https://github.com/Hatterhat/Skyrat-tg/commit/bbaefcefebf4200cf30456cfdb3cbfdb30af6c49)
#### Tuesday 2022-11-29 03:37:42 by SkyratBot

[MIRROR] UpdatePaths Readme - Reforged [MDB IGNORE] (#17204)

* UpdatePaths Readme - Reforged (#70806)

* UpdatePaths Readme - Reforged

I'm a bit tired after typing for the last hour so apologies if some of this stuff is unreadable. Basically, I just took time to add a small blurb about UpdatePaths in MAPS_AND_AWAY_MISSIONS.md, as well as write out examples on how you can properly use every single function UpdatePaths might have. I'm probably missing something? I think I got everything though. Let me know if I should be consistent somehow, but I did deliberately choose different test-cases per example because it's nearly impossible to come up one "generic" fit-all situation that illustrates every possible use of UpdatePaths (to my small mind).

Anyways, hope this helps.

* i fucked up with the TGM format

augh

* UpdatePaths Readme - Reforged

Co-authored-by: san7890 <the@san7890.com>

---
## [clair0se/UUTTT](https://github.com/clair0se/UUTTT)@[1ab964ac3e...](https://github.com/clair0se/UUTTT/commit/1ab964ac3e08b4a7bc2bc8354cef71f23911e179)
#### Tuesday 2022-11-29 03:39:17 by Claire

oh my god you can win
i'm so close
just one more big thing
then i will like, comment my code all the way and stuff
as a treat
for being a good girl
yeah
i love you commit messages

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[0ca2c0b527...](https://github.com/OrionTheFox/Skyrat-tg/commit/0ca2c0b527a564de32818057b7fc09eb07875f51)
#### Tuesday 2022-11-29 03:58:44 by SkyratBot

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
## [Pink-Chink/sojourn-station](https://github.com/Pink-Chink/sojourn-station)@[8620d970b0...](https://github.com/Pink-Chink/sojourn-station/commit/8620d970b0aaa8d632e83a4dcc35547826f555df)
#### Tuesday 2022-11-29 04:36:58 by DimmaDunk

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
## [Lyicx/linux-shit](https://github.com/Lyicx/linux-shit)@[8bdd19683f...](https://github.com/Lyicx/linux-shit/commit/8bdd19683fe026a971244a8ed86d429edcb2f919)
#### Tuesday 2022-11-29 04:54:01 by Lyicx

sudo'd the pkill since thats how that shit works - FUCKING I HATE VIM SO MUCH IF YOU LOVE VIM YOU'RE A GENUINE PEDOPHILE

---
## [politecat314/divorce-prediction](https://github.com/politecat314/divorce-prediction)@[20c2ac1318...](https://github.com/politecat314/divorce-prediction/commit/20c2ac131859880111774fea5fcddd4b41efbde0)
#### Tuesday 2022-11-29 04:59:10 by Oliverluyu

Add ML Project Report PDF

Hi Aman! I am currently reviewing the past year course project for the purpose of a postgraduate study interview preparation. So I wonder whether it is pleasant to add on our project report, as it can provide a more clear view to the readers. Let be awared if you have any suggestions via whatsapp. TQ : )

Your lovely friend
Lu Yu

---
## [newstools/2022-new-york-post](https://github.com/newstools/2022-new-york-post)@[560b2ad8ce...](https://github.com/newstools/2022-new-york-post/commit/560b2ad8ce77c8b31d3cac9a87e614ed824013d5)
#### Tuesday 2022-11-29 05:27:20 by Billy Einkamerer

Created Text For URL [nypost.com/2022/11/28/accused-killer-bronx-mom-dimone-fleming-thought-boyfriend-was-the-devil-her-dad/]

---
## [VastKilleroOm/tgstation](https://github.com/VastKilleroOm/tgstation)@[3c187487b1...](https://github.com/VastKilleroOm/tgstation/commit/3c187487b1884040608ba23b0a89aa8b0176c2aa)
#### Tuesday 2022-11-29 05:30:26 by MrMelbert

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
## [wild233-sys/Grasscutter](https://github.com/wild233-sys/Grasscutter)@[88bc5c4c54...](https://github.com/wild233-sys/Grasscutter/commit/88bc5c4c54c1aadcdc6cc9a24c0f69d4bebce97c)
#### Tuesday 2022-11-29 07:09:21 by Kimi

another translation patches because i fucked it up

i hate myself

---
## [Holoo-1/tgstation](https://github.com/Holoo-1/tgstation)@[03bc97ade5...](https://github.com/Holoo-1/tgstation/commit/03bc97ade5a76f156229b946e38816ced97a0e30)
#### Tuesday 2022-11-29 08:05:35 by necromanceranne

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
## [tahaluindo/Sofware-Tools](https://github.com/tahaluindo/Sofware-Tools)@[3b38e7a982...](https://github.com/tahaluindo/Sofware-Tools/commit/3b38e7a982e957f1eb62fc3d5a3e0fefd28e3522)
#### Tuesday 2022-11-29 09:11:01 by LulzGhost-Team BOT

29 November 2022

---
{"dg-publish":true,"permalink":"/apps/","dgShowBacklinks":true,"dgShowLocalGraph":true}
---

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents** *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Apps](#apps)
  - [Cross-Platform](#cross-platform)
  - [Docker](#docker)
  - [iOS](#ios)
  - [Linux](#linux)
  - [MacOS](#macos)
  - [Online](#online)
  - [Packages](#packages)
  - [VS Code](#vs-code)
  - [Windows](#windows)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

---

# Apps

- [A Markdown Editor for the 21st Century - Zettlr](https://zettlr.com/)

- [Zenkit Hypernotes - Experience a new way of collaborative writing.](https://zenkit.com/en/hypernotes/)

- [Zengobi Curio](https://zengobi.com/curio/)

- [VNote - A pleasant note-taking platform](http://app.vnote.fun/en_us/)

- [Transno - Outlines, Notes, Mind Map](https://transno.com/)

- [tiddlyroam · your open source external brain](https://tiddlyroam.org/)

- [Tangent Notes](https://www.tangentnotes.com/)

- [RemNote – The all-in-one tool for thinking and learning.](https://www.remnote.com/)

- [Reflect](https://reflect.app/)

- [Recall - Your personal encyclopedia](https://www.recall.wiki/)

- [Your Second Brain - myReach](https://myreach.io/)

- [NotePlan - Your tasks, notes, and calendar. All linked in one place.](https://noteplan.co/)

- [Nota Bene](https://www.notabene.com/)

- [Nota - Pro notes app designed for local Markdown files.](https://nota.md/)

- [Mind Map & Brainstorm Ideas](https://www.mindnode.com/)

- [MindMeister: Online Mind Mapping and Brainstorming](https://www.mindmeister.com/)

- [mindlib - Your personal mind library](https://mindlib.de/login)

- [Marginnote](https://www.marginnote.com/)

- [Innos Note](https://innos.io/)

- [Best Notes App - Write and Organize with UpNote](https://getupnote.com/)

- [Dive into big ideas with Muse](https://museapp.com/)

- [RemNote – The all-in-one tool for thinking and learning.](https://www.remnote.io/)

- [POLAR - Easily manage your reading. Tag, annotate, and highlight PDFs and web content.](https://app.getpolarized.io/)

- [μPad | Take and organise notes for free](https://getmicropad.com/)

- [Mem: The self-organizing workspace](https://get.mem.ai/)

- [Escape - Mind mapping & Outlining for iOS](https://escapeapp.cloud/)

- [dokuwiki [DokuWiki]](https://www.dokuwiki.org/dokuwiki)

- [Dendron](https://www.dendron.so/)

- [Defter Notes | iPad app for deft handwritten notes & spatial organizing.](https://defternotes.com/)

- [Notorious](https://danobot.github.io/notorious-landing/)

- [Craft - The Future of Documents](https://www.craft.do/)

- [CmapTools | Cmap](https://cmap.ihmc.us/cmaptools/)

- [The developer notepad | Stashpad](https://www.stashpad.com/)

- [Boost Note | Chronicle your Stories](https://boostnote.io/)

- [Capacities](https://app.capacities.io/)

- [Anytype.io](https://anytype.io/en)

- [Amplenote: Best Note-taking App for To-do Lists & Calendar Scheduling](https://www.amplenote.com/)

- [AFFiNE - All In One Workos](https://affine.pro/)

- [ABLE | Dive into learning, spark insights, find your perfect flow](https://able.ac/)

## Cross-Platform

- [Notesnook | Open source & zero knowledge private note taking app](https://notesnook.com/)

- [Glamorous Toolkit](https://gtoolkit.com/)

- [acreom — IDE for your workflow](https://acreom.com/)

- [cherrytree – giuspen](https://www.giuspen.com/cherrytree/)

- [Memrey](https://www.memrey.com/)

- [Nuclino](https://www.nuclino.com/)

- [Zim - a desktop wiki](https://www.zim-wiki.org/?utm_source=saashub&utm_medium=marketplace&utm_campaign=saashub)

- [TiddlyWiki — a non-linear personal web notebook](https://tiddlywiki.com/)

- [Roam Research – A note taking tool for networked thought.](https://roamresearch.com/)

- [Notion – The all-in-one workspace for your notes, tasks, wikis, and databases.](https://www.notion.so/)

- [MindForger - Thinking Notebook and Markdown Editor](https://www.mindforger.com/)

- [Create amazing 3D Mind Maps and Flowcharts with our software](http://www.buildyourmap.com/)

- [AppFlowy.IO](https://www.appflowy.io/)

- [Anytype Community](https://community.anytype.io/)



## Docker

- [Hello from Personal Management System | Personal Management System](https://volmarg.github.io/)

- [Gist - Data becomes knowledge](https://www.gistapp.com/?ref=producthunt)



## iOS

- [‎Muse — tool for thought](https://apps.apple.com/in/app/muse-tool-for-thought/id1501563902)

- [mindlib - Your personal mind library](https://mindlib.de/)

- [Relanote | List](https://app.relanote.com/platform/notes-list)

- [‎Quine 2](https://apps.apple.com/us/app/quine-2/id1450128957)

- [Note Garden](https://notegarden.web.app/)

- [‎KnowledgeBase Builder](https://apps.apple.com/us/app/knowledgebase-builder/id1448579863)

- [‎Kase: Your Personal Database](https://apps.apple.com/us/app/kase-your-personal-database/id1481308987)



## Linux

- [Focalboard: Open source alternative to Trello, Asana, and Notion](https://www.focalboard.com/)



## MacOS

- [Tinderbox: The Tool For Notes](http://www.eastgate.com/Tinderbox/index.html)

- [Notenik Home](https://notenik.app/)

- [Agenda - Date-focused Note Taking.](https://agenda.com/)

- [A Markdown Editor for the 21st Century](https://www.zettlr.com/)

- [Note taking and mind mapping combined in one app](https://brainio.com/#/)

- [cryo file manager](https://cryonet.io/?ref=producthunt)



## Online

- [Word Webs](https://wordwebs.app/home)

- [Scolary](https://scolary.com/)

- [Data Stewardship Wizard](https://ds-wizard.org/)

- [The Dataverse Project - Dataverse.org](https://dataverse.org/)

- [wizdom.ai - intelligence for everyone](https://www.wizdom.ai/)

- [Academicons](https://jpswalsh.github.io/academicons/)

- [D3.js - Data-Driven Documents](https://d3js.org/)

- [Authorea](https://www.authorea.com/)

- [ELN and Project Management for science labs](https://www.colabra.app/)

- [mathieudutour/gatsby-digital-garden: 🌷 🌻 🌺 Create a digital garden with Gatsby](https://github.com/mathieudutour/gatsby-digital-garden)

- [Hyperdraft](https://hyperdraft.rosano.ca/)

- [bCisive - online decision mapping](https://www.bcisiveonline.com/)

- [Notabase](https://notabase.io/)

- [Apps with 'Knowledge Management' feature](https://alternativeto.net/feature/knowledge-management/)

- [Go beyond Bookmarks with BrainTool, the online Topic Manager](https://braintool.org/)

- [bundleIQ | Think Better](https://www.bundleiq.com/)

- [capacities – Your second brain](http://capacities.io/)

- [You need a wiki](https://youneedawiki.com/app)

- [Wavebox](https://wavebox.io/)

- [Wannadocs – Knowledge Base Management System](https://wannadocs.com/?ref=producthunt)

- [Spaceli — Turn Google Docs into a knowledge base](https://spaceli.io/?ref=producthunt)

- [SlimWiki — Beautiful Wikis for Teams](https://slimwiki.com/)

- [SigmaOS](https://sigmaos.com/?ref=producthunt)

- [Schema - The most productive cloud drive](https://www.schema.team/?ref=producthunt)

- [OrgPad - Universal, yet so simple](https://orgpad.com/)

- [Neatly Dashboard](https://app.useneatly.com/dashboard/categories/61c1b21284920b00c2388cad)

- [Legend](https://legendapp.com/)

- [KgBase - No-code knowledge graphs](https://www.kgbase.com/)

- [Interactive step-by-step guides and troubleshooting | Stonly](https://stonly.com/product/knowledge-base-software?ref=producthunt)

- [Fibery | Build your company workspace with no code](https://fibery.io/)

- [Databyss](https://www.databyss.org/?ref=producthunt)

- [Curabase: We make it easy to curate, collaborate, and share bookmarks.](https://www.curabase.com/?utm_source=saashub&utm_medium=marketplace&utm_campaign=saashub)

- [Connected Knowledge Networks Connect, organize, and visualize your knowledge.](https://www.ramsync.com/)

- [Build a Wiki on Google Drive - Kbee](https://www.kbee.app/?ref=producthunt)



## Packages

- [Screenshot tour · zadam/trilium Wiki · GitHub](https://github.com/zadam/trilium/wiki/Screenshot-tour)

- [cotoami/cotoami: Cotoami is a platform where people can weave a large network of wisdom from tiny ideas.](https://github.com/cotoami/cotoami#flow-timeline-and-stock-structured-content)

- [Argdown](https://argdown.org/)

- [Neuron Zettelkasten](https://neuron.zettel.page/)

- [Wiki.js](https://js.wiki/?utm_source=saashub&utm_medium=marketplace&utm_campaign=saashub)

- [Personal Knowledge Base with Vimwiki](https://www.rockyourcode.com/personal-knowledge-base-with-vimwiki/)

- [Pandoc - About pandoc](https://pandoc.org/?utm_source=saashub&utm_medium=marketplace&utm_campaign=saashub)

- [Onivim 2 - Modal Editing from the Future](https://v2.onivim.io/)

- [jKanban - Javascript plugin for Kanban boards](https://www.riccardotartaglia.it/jkanban/?ref=producthunt)

- [Index - Archivy](https://archivy.github.io/)



## VS Code

- [Dendron](https://www.dendron.so//)

- [Foam - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=foam.foam-vscode)

- [Foam](https://foambubble.github.io/foam)



## Windows

- [MyInfo Note Taking & Personal Information Manager](https://www.myinfoapp.com/)

Signed-off-by: LulzGhost-Team BOT <tahaluindo@gmail.com>

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[b77cf7c120...](https://github.com/timothymtorres/tgstation/commit/b77cf7c1205d466b8cb242cd3302891e82b44da2)
#### Tuesday 2022-11-29 09:29:04 by Iamgoofball

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
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[4d6dd806d6...](https://github.com/Offroaders123/NBTify/commit/4d6dd806d6ef59ccb7210bb2bbf0a490d25f3209)
#### Tuesday 2022-11-29 09:37:23 by Offroaders123

Unnamed Root Compound Tags

Added initial support for unnamed root compound tags! This currently works at the `NBTReader` level, and fully at the writing level. Because of all the new additions to the `NBTData` class, the composition functions (`read()` and `write()`) could use a little help to better reflect those new updates. One example being, also accepting either simply just a `CompoundTag`, or an `NBTData` object, and also moving all of the validation logic over to the `NBTData` object instead of replicating it in all of the parameter input locations.

Big thanks to WebNBT for being able to deduce the format for this! Looks like not even Prismarine NBT supports unnamed root Compound tags. nbt-ts, does support it though! I checked out their support for how they got it to work. And the format simply just removes an initial `StringTag` after the first `CompoundTag` byte at the start of the file. So, minus two bytes. I'm gonna have to add a check for that in the file type deduction code inside of the `read()` function, similar to how the endianness check currently works. I'll need another check that will also perform a root-name-or-not kind of thing. Glad to have all of the `NBTData` properties declared safely now, relying on those for parameter management will make things much better for the future IO reworks.

Re-added the `Name` type, since it is now more complex than just a `string`, now also possibly `null`. Compared to the optional properties on the `NBTData` object, `name` is not optional, but rather will be listed with a `null` name property. So, it is either `string | null`, instead of `PropType | undefined`.

Getting sleepy, listening to Yellow Hedgerow Dreamscape now. Gotta get up early for my potato buckets shift in the morning, so this will likely be my closing commit for the night. zzz, gn! :)

---
## [guardian/gateway](https://github.com/guardian/gateway)@[b962f668b3...](https://github.com/guardian/gateway/commit/b962f668b35ac72f8f0a0aaace8ee180da8b816e)
#### Tuesday 2022-11-29 09:44:48 by Mahesh Makani

feat(okta): show onboarding flow for new social users

In Okta it is currently not possible to differentiate between new social users, and existing social users. This means that is was not possible to show social users the
onboarding flow.

However there is a case where a new social user differentiates form existing social users. This is to do with the email validated status. A new social user will be in
the `GuardianUser-EmailValidated` but their `emailValidated` field in their user profile will be `false` or `undefined`. So we have a remediation step in our callback to
handle this discrepency, and set the `emailValidated` flag should the user be in the `GuardianUser-EmailValidated` group. This was introduced in this commit:
https://github.com/guardian/gateway/commit/9af078165aa5add60b9e11bfe6731ff25badca6e

This means that the only time this discrepency will occur is for new social users, meaning at this point we can differentiate them from existing social users. This
allows us to use this functionality and set a flag to show the onboarding flow `authState.confirmationPage = consentPages[0].path;`. At any other point in time the user
will have both the `GuardianUser-EmailValidated` group and the `emailValidated` flag set, so they would not see the onboarding flow again.

A number of other options were considered for this functionality, but would involve other changes to the Okta configuration.

1. Using Okta groups
The first option we tried was to use Okta groups to do this. The theory was for new social users we assign them to a specific Okta group that we create, we can then
check this group, and if a user is in this group show then the onboarding flow. We can then remove them from this group so they're not shown the onboarding flow again.

However although this does work and new social users do see the Onboarding flow. I noticed that all social users started seeing the onboarding flow, whether they were
new users, existing users, or had even seen the onboarding flow before. Turns out Okta will always add all social users to the new group if they are not currently in it.
So even when removing the group from the user,  the next time they sign in with social, they get added to the group again, and they get shown the onboarding flow again.
Which wasn't ideal.

2. Using the account `created` timestamp on the user object.
This option was to use the `created` field in the user profile to determine if we should show the onboarding flow or not. This would involve checking this field
everytime a user went to the oauth callback endpoint, and if it's within a certain time period, say 1 minute, then to show the onboarding flow in that scenario.

However the account `created` field isn't returned by default in either the access or id token. So we'd either have to make an additional API call for every time a user
goes to the oauth callback endpoint, or to add a custom claim to add this field to the id token.

Using the API option would require making additional API calls, which we're trying to avoid, due to a limited number of API calls we're able to make to Okta. While
adding this field to the id token would require changes to the Okta terraform configuration to add this in, and would add an additional payload to what's only
effectively used once.

Also we'd have to chose the time period to check to avoid users seeing the onboarding flow multiple times if we set it too long, e.g. if they sign in immeditely after
registering on another browser/device, or not seeing the onboarding flow at all if we set it too short.

Hence the reason I went with the approach that we did.

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[0c59d03303...](https://github.com/GeoB99/reactos/commit/0c59d0330312558cb706ee7efec84656197a345d)
#### Tuesday 2022-11-29 10:00:42 by George Bișoc

[SDK][CMLIB] Implement log transaction writes & Resuscitation

=== DOCUMENTATION REMARKS ===

This implements (also enables some parts of code been decayed for years) the transacted writing of the registry. Transacted writing (or writing into registry in a transactional way) is an operation that ensures the successfulness can be achieved by monitoring two main points.
In CMLIB, such points are what we internally call them the primary and secondary sequences. A sequence is a numeric field that is incremented each time a writing operation (namely done with the FileWrite function and such) has successfully completed.

The primary sequence is incremented to suggest that the initial work of syncing the registry is in progress. During this phase, the base block header is written into the primary hive file and registry data is being written to said file in form of blocks. Afterwards the seconady sequence
is increment to report completion of the transactional writing of the registry. This operation occurs in HvpWriteHive function (invoked by HvSyncHive for syncing). If the transactional writing fails or if the lazy flushing of the registry fails, LOG files come into play.

Like HvpWriteHive, LOGs are updated by the HvpWriteLog which writes dirty data (base block header included) to the LOG themselves. These files serve for recovery and emergency purposes in case the primary machine hive has been damaged due to previous forced interruption of writing stuff into
the registry hive. With specific recovery algorithms, the data that's been gathered from a LOG will be applied to the primary hive, salvaging it. But if a LOG file is corrupt as well, then the system will perform resuscitation techniques by reconstructing the base block header to reasonable values,
reset the registry signature and whatnot.

This work is an inspiration from PR #3932 by mrmks04 (aka Max Korostil). I have continued his work by doing some more tweaks and whatnot. In addition to that, the whole transaction writing code is documented.

=== IMPORTANT NOTES ===

HvpWriteLog -- Currently this function lacks the ability to grow the log file size since we pretty much lack the necessary code that deals with hive shrinking and log shrinking/growing as well. This part is not super critical for us so this shall be left as a TODO for future.

HvLoadHive -- Currently there's a hack that prevents us from refactoring this function in a proper way. That is, we should not be reading the whole and prepare the hive storage using HvpInitializeMemoryHive which is strictly used for HINIT_MEMORY but rather we must read the hive file block by block
and deconstruct the read buffer from the file so that we can get the bins that we read from the file. With the hive bins we got the hive storage will be prepared based on such bins. If one of the bins is corrupt, self healing is applied in such scenario.

For this matter, if in any case the hive we'll be reading is corrupt we could potentially read corrupt data and lead the system into failure. So we have to perform header and data recovery as well before reading the whole hive.

---
## [20hr1a0460/practice](https://github.com/20hr1a0460/practice)@[dbfaa8e866...](https://github.com/20hr1a0460/practice/commit/dbfaa8e866c4c29a81c140e59fbf2d3ea676fc1a)
#### Tuesday 2022-11-29 11:02:19 by 20hr1a0460

Three Idiots

Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality. A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a program to find the midpoint of the line.

---
## [20hr1a0460/practice](https://github.com/20hr1a0460/practice)@[e89731013b...](https://github.com/20hr1a0460/practice/commit/e89731013bf65202e2c842a7e698a3336eaf4688)
#### Tuesday 2022-11-29 11:13:00 by 20hr1a0460

Team Flash

A young man named Diffny leaves home to travel to California, to join the Team Flash. Although Diffny is not able to join this elite team immediately, he befriends the three most formidable members of the age: Joe, Ramsey and vixon and gets involved in affairs of the state and court.At that time, the Villan was planning to dethrone the king and to take the kingdom and to remove the Team Flash of the guard. Since the Villan has spies mixed with the local public , Diffny decides to send a message of his whereabouts to the team Flash in unique way.He gave a note to a boy which has the following message. I am at the midpoint of the line joining the farmhouse next to the palace and the light house. The Team Flash were puzzled. Can you help them find out the location of Diffny?Given the coordinates of the 2 places (x1,y1) and (x2,y2), write a program to find the location of Diffny.

---
## [Huexxx/kernel_xiaomi_msm8998](https://github.com/Huexxx/kernel_xiaomi_msm8998)@[03392a1860...](https://github.com/Huexxx/kernel_xiaomi_msm8998/commit/03392a18606e45fdb29069e61abec32123fc9854)
#### Tuesday 2022-11-29 11:55:02 by Christian Brauner

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

---
## [avar/git](https://github.com/avar/git)@[f1c903debd...](https://github.com/avar/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Tuesday 2022-11-29 12:51:59 by Ævar Arnfjörð Bjarmason

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
## [kpatron-cockroachlabs/cockroach](https://github.com/kpatron-cockroachlabs/cockroach)@[1d04cec7c5...](https://github.com/kpatron-cockroachlabs/cockroach/commit/1d04cec7c5f887d309e09b7b5a267d5269d86b5a)
#### Tuesday 2022-11-29 14:06:39 by craig[bot]

Merge #91394 #91627

91394: changefeedccl: roachtest refactor and initial-scan-only r=samiskin a=samiskin

Epic: https://cockroachlabs.atlassian.net/browse/CRDB-19057

Changefeed roachtests were setup focused on running a workload for a specific duration and then quitting, making it difficult to run an `initial_scan_only` test that terminated upon Job success.

We as a team have also noticed a greater need to test and observe changefeeds running in production against real sinks to catch issues we are unable to mock or observe from simple unit tests.  This is currently a notable hassle as one has to set up each individual sink and run them, ensure the changefeed is pointing to the right URI, and then be able to monitor the metrics of this long running process.  

This change refactors the cdcBasicTest into distinct pieces that are then put together in a test.  This allows for easier experimentation with live tests, allowing us to spin up a cluster and a workload, run one or more changefeeds on it, set up a poller to print out job details,have an accessible grafana URL to view metrics, and wait for some completion condition.

Changing the specialized `runCDCKafkaAuth`, `runCDCBank`, and `runCDCSchemaRegistry` functions were left out of scope for this first big change.

The main APIs involved in basic roachtests are now:
- `newCDCTester`: This creates a tester struct to run the rest of the APIs and initializes the database
- `tester.runTPCCWorkload(tpccArgs)`: Starts a TPCC workload from the last node in the cluster
- `tester.runLedgerWorkload(ledgerArgs)`: Starts a Ledger workload from the last node in the cluster
- `tester.runFeedLatencyVerifier(changefeedJob, latencyTargets)`: starts a routine that monitors the changefeed latency until the tester is `Close`'d
- `tester.waitForWorkload`: waits for a workload started by `setupAndRunWorkload` to complete its duration
- `tester.startCRDBChaos`: This starts a Chaos routine that periodically shuts nodes down and brings them back up
- `tester.newChangefeed(feedArgs)`: starts a new changefeed on the cluster and returns `changefeedJob` object
- `changefeedJob.waitForCompletion`: waits for a changefeed to complete (either success or failure)
- `tester.startGrafana`: Sets up a grafana instance on the last node of the cluster and prints out a link to a grafana, this automatically runs unless `--skip-init` is provided.  If `--debug` is not used, `StopGrafana` will be called on test teardown to publish prometheus metrics to the artifacts directory.

An API that is going to be more useful for experimentation are:
- `changefeedJob.runFeedPoller(ctx, stopper, onInfo)`: runs a given callback every second with the changefeed info

Roachtests can be ran locally with the `--local` flag or on an existing cluster without destroying it afterwards with `--cluster="my-cluster" --debug`

Ex: After adding a new test (lets say `"cdc/my-test"`) to the `registerCDC` function you can keep running 
```bash
./dev build cockroach --cross # if changes made to crdb
./dev build roachtest         # if changes made to the test

./bin/roachtest run cdc/my-test --cluster="my-cluster" --debug
```
as you try out different changes or options.  If you want to try a set of steps against different versions of the app you could download those binaries and use the `--cockroach="path-to-binary"` flag to test against those instead.

If you want to set up a large TPCC database on a cluster and reuse it for tests this can be done with roachtests's `--wipe` and `--skip-init` flags.

Release note: None

91627: upgrade: introduce "permanent" upgrades r=andreimatei a=andreimatei

This patch introduces "permanent" upgrades - a type of upgrade that is
tied to a particular cluster version (just like the existing upgrades)
but that runs regardless of the version at which the cluster was
bootstrapped (in contrast with the existing upgrades that are not run
when they're associated with a cluster version <= the bootstrap
version). These upgrades are called "permanent" because they cannot be
deleted from the codebase at a later point, in contrast with the others
that are deleted once the version they're tied drops below
BinaryMinSupportedVersion).

Existing upgrades are explicitly or implicitly baked into the bootstrap
image of the binary that introduced them. For example, an upgrade that
creates a system table is only run when upgrading an existing,
older-version, cluster to the new version; it does not run for a cluster
bootstrapped by the binary that introduced the upgrade because the
respective system tables are also included in the bootstrap metadata.
For some upcoming upgrades, though, including them in the bootstrap
image is difficult. For example, creating a job record at bootstrap
time is proving to be difficult (the system.jobs table has indexes, so
you want to insert into it through SQL because figuring out the kv's for
a row is tedious, etc). This is where these new permanent upgrades come
in.

These permanent upgrades replace the `startupmigrations` that don't have
the `includedInBootstrap` field set. All such startupmigrations have
been copied over as upgrades. None of the current `startupmigrations`
have `includedInBootstrap` set (except one but that's dummy one since
the actual migration code has been deleted), so the startupmigrations
package is now deleted. That's a good thing - we had one too many
migrations frameworks.

These permanent upgrades, though, do not have exactly the same semantics
as the startupmigrations they replace. To the extent that there is a
difference, the new semantics are considered more desirable:
- startupmigrations run when a node that has the code for a particular
  migration startups up for the first time. In other words, the
  startupmigrations were not associated with a cluster version; they were
  associated with a binary version. Migrations can run while old-version
  nodes are still around.  This means that one cannot add a
  migration that is a problem for old nodes - e.g. a migration creating a
  job of a type that the old version wouldn't recognize.
- upgrades are tied to a cluster version - they only run when the
  cluster's active version moves past the upgrade's version. This stays
  the case for the new permanent migrations too, so a v2 node will not
  immediately run the permant migrations introduced since v1 when it joins
  a v1 cluster. Instead, the migrations will run when the cluster version
  is bumped. As such, the migrations can be backwards incompatible.

startupmigrations do arguably have a property that can be desirable:
when there are no backwards compatibility issues, the v2 node can rely
on the effects of the startupmigrations it knows about regardless of the
cluster version. In contrast, with upgrades, not only is a node unable
to simply assume that a particular upgrade has run during startup, but,
more than that, a node is not even able to look at a version gate during
the startup sequence in order to determine whether a particular upgrade
has run or not (because, in clusters that are bootstrapped at v2, the
active cluster version starts as v2 even before the upgrades run). This
is a fact of life for existing upgrades, and now becomes a fact of life
for permanent upgrades too. However, by the time user SQL traffic is
admitted on a node, the node can rely on version gates to correspond to
migrations that have run.

After thinking about it, this possible advantage of startupmigrations
doesn't seem too useful and so it's not reason enough to keep the
startupmigrations machinery around.

Since the relevant startupmigrations have been moved over to upgrades,
and the two libraries use different methods for not running the same
migration twice, a 23.1 node that comes up in a 22.2 cluster will re-run
the several permanent upgrades in question, even though they had already
run as startupmigrations. This is OK since both startupmigrations and
upgrades are idempotent. None of the current permanent upgrades are too
expensive.

Closes https://github.com/cockroachdb/cockroach/issues/73813

Release note: None
Epic: None

Co-authored-by: Shiranka Miskin <shiranka@cockroachlabs.com>
Co-authored-by: Andrei Matei <andrei@cockroachlabs.com>

---
## [KennedySovine/CI435-Introduction-to-Web-Development](https://github.com/KennedySovine/CI435-Introduction-to-Web-Development)@[211f3abb6b...](https://github.com/KennedySovine/CI435-Introduction-to-Web-Development/commit/211f3abb6b56381c0f0af54a3ad01ab4d06d89ec)
#### Tuesday 2022-11-29 14:17:19 by KennedySovine

Responsive Part 2

Electric Boogaloo. I had some trouble doing things like word wraps and stuff, but now it's all good! I've been using Safari's responsive web design stuff to make sure everything is going according to plan.

Added another media query that senses the big screens and makes the text even larger. This is useful if being casted onto a TV or being browsed from a device with a huuuuge screen.

For some reason, hiding images on smaller screens wasn't working so I just decided to say fuck it and just live with it. It was being inverse or something I don't know. Mobile first development sucks, especially when you aren't developing from a phone, but I digress. It works now, so there's no issues :) :+1:

---
## [xDroidOSS-Pixel/frameworks_base](https://github.com/xDroidOSS-Pixel/frameworks_base)@[b7d3f63a02...](https://github.com/xDroidOSS-Pixel/frameworks_base/commit/b7d3f63a02910e4e0e3fee821a5edce140ecaba6)
#### Tuesday 2022-11-29 14:32:57 by Kuba Wojciechowski

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
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[e7c8fed8e3...](https://github.com/odoo-dev/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Tuesday 2022-11-29 15:57:40 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: web_editor

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with an ugly patch. We'll review what to do in
master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104156

Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [anthonygarced/anthonygarced](https://github.com/anthonygarced/anthonygarced)@[1633b29b49...](https://github.com/anthonygarced/anthonygarced/commit/1633b29b491be4ce1674524ed91623a1ef70e458)
#### Tuesday 2022-11-29 16:08:42 by Anthony Garced

changed shitty block

i dont know how to make the funny ass github blocks

---
## [MushiTea/21438_ChaoticCurrent_REPO](https://github.com/MushiTea/21438_ChaoticCurrent_REPO)@[3ee931ba41...](https://github.com/MushiTea/21438_ChaoticCurrent_REPO/commit/3ee931ba41c01eea0f2f299c1f727f40ce3c5d1f)
#### Tuesday 2022-11-29 16:11:23 by yeeT787

Omg girl do you watch forged in fire? Cuz I want you to pick usable steel from this pile of scrap metal to use as the base for your blades. They must meet the following parameters, a length between 8-10 inches, a full tang with a length of 3-4 inches, and width from spine to cutting edge of at least 1 1/2 inch but no longer than 2 1/2 inches. In the next round, you will be attaching handles to your blades to turn them into fully functional weapons. And for the third round we will put it through a series of tests, such as, dummy stab for sharpness, chain chop for durability, and a sheet metal stab for edge retention. And the two winners of the third round will be sent to their home forges to recreate an iconic weapons from history. The winner of the final round will go home with the title of forged in fire champion and a check for $10,000. Your time starts, now!

Essentially what we did was fix claw,slide, and arm positions and I added manual arm just because - Srinirek

---
## [justamanuelax/justamanuelax](https://github.com/justamanuelax/justamanuelax)@[09be3df507...](https://github.com/justamanuelax/justamanuelax/commit/09be3df5075121ba1ed13180ed394e462fd7f4d3)
#### Tuesday 2022-11-29 16:16:10 by Open_Source_Lover

Let's build websites and learn from each other

This Github is a community where the code is open source for real maybe I should call this github the real Openyada yada yo.
But on a serious note let's build stuff and learn from each other my code has zero licensing so you can copy and not credit me and will be more than happy 
get me to as many stars as possible 
stars is life 
but I have to say Im a noob for now and I am dedicated to becoming an expert within a year yo I can dream but this is my 1 year goal and I'm serious 
opportunities will arise but I got to focused for now.
on the 30 of November I will be uploading my first piece of HTML.

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[317aea0435...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/317aea043510ee0c3591ff3a06fdffd360fdfc29)
#### Tuesday 2022-11-29 17:24:17 by Jolly

[FUCK] [NO GBP] Yeah, fixes something in NuInterlink(?) (#17544)

fucking GODDAMNIT

---
## [Koenkk/zigbee2mqtt.io](https://github.com/Koenkk/zigbee2mqtt.io)@[07e1c18d06...](https://github.com/Koenkk/zigbee2mqtt.io/commit/07e1c18d0616b46b2891609a4a5bd0f6f204a45d)
#### Tuesday 2022-11-29 18:01:38 by Artur Sena

Update FAQ (#1730)

* Update README.md

Hey guys, so, i want to share a problem i had for a couple of months, and manage to solve.

It prob has happens to other ppl, and prob, at least a couple of those, still have, or never manage to solve.

If the wrong place, sorry, but i think this should be in the FAQ, even it's not the most common problem.

So, i have a setup with a good router stick, home assistant, and zigbee2mqtt addon.

The problem: some devices was not updating it's status, or desyncing from the network, also, was unable to add new devices. Map, was not being generate prob and timeout was happening without a clue or reason.

I started asking for help, changing the router stick, and without luck, it just ignored because it was kinda working almost all the times.

One day i decide to modify a door sensor, and for such, i needed it to connect to the network to test, it was unable to do so.

I started zigbee2mqtt in a new computer, though docker, and it worked FLAWLESS, after a while, i try to move all the devices to such new device.

Everything working perfect. Doubled the size of the network, no problem.
Add more automations, no problem.

The reason of such strange behaiviour was my raspberry pi model 3+, because it just have 1gb memory or maybe the processor, but, the problem was the limitations of the platform.

The reason for using such a limited board, is, the model 4 is expensive where i live, and i never had such problems. It started without warning.

So, i would like to add such information to the FAQ of Zigbee2mqtt, for more people now that you need a little room of memory and processor to avoid timeouts.

* Update README.md

Co-authored-by: Koen Kanters <koenkanters94@gmail.com>

---
## [nytmyr/Server](https://github.com/nytmyr/Server)@[9250758415...](https://github.com/nytmyr/Server/commit/9250758415303696e8def4198fe6204c0e9380f6)
#### Tuesday 2022-11-29 18:11:59 by toxin06

[Bots] AI Revamp, add all holds, delays, thresholds, min thresholds, character heal settings. Bard fixes.

All group features for combat range and behind mob now work in raids

Every spell type can have a delay, minimum and maximum threshold to cast.

The delay is how quickly a bot can cast that type of spell, the timer starts from the beginning of the cast. If you set this to 10 seconds, as soon as a spell starts casting, another will start in 10 seconds provided it isn't on cooldown or has stacking/immune blocks.

The minimum threshold is the percent of health when a bot will stop casting a spell.
-Escapes, Hate Reductions, Lifetaps and Shaman In-Combat Buffs (Canni) will rely upon the bot's OWN health. (When do you want said bot to start trying to drop aggro, when they reach 80% until 20%? Do they lifetap starting at 60% and never stop till they die? (0%).

Threshold or maximum threshold is the percent of health when the bot will begin casting that type of spell.

Casters will now output what type of spell and what spell they are casting for all spell types except buffs.

Casters will now output all those messages to the entire group or raid, filterable by Pet Response.

Casters now dispel, escape, lifetap, snare and root automatically.

SKs will now cast their bonus hate spells as the spell type in-combat buffs rather than nuke so it can be held if needed.

Shamans will still Cannibalize using in-combat buffs, however you can set the minimum threshold to control when they stop Cannibalizing and the Maximum threshold will be based off their mana to start Cannibalizing.
--Shamans will never start to cannibalize if their mana is above 90% or their health is below 50% regardless of the minimum/maximum setting.

SKs, Paladins and Clerics will not cast their in-combat buffs if they have hit their stop melee level.

SKs, Rangers, Wizards, Enchanters and Bards will now cast hate reduction spells.

Necros/SKs will cast their Darkness line as the Snare spell type.
--Necros will not cast Insidious Retrogression.

Bards will now start casting their songs before they fade instead of waiting for them to fade so there is no gap in buffs.
-------
Casters no longer try to cast DoTs, nukes, roots or snares if it may result in aggro. Once enough aggro is built up by the tank to where they don't think they'll pull aggro, they will begin casting.
--SKs & Pallies will always cast these regardless of aggro, use holds or thresholds if you want them to stop.

Resist checks for spells will now take into affect level differences as well. (Higher level mobs are more likely to resist a spell than a lower level mob with the same resist stats)

If a target mob is Undead, Summoned or Plant, the appropriate classes will cast the appropriate nukes if available.
-Necromancers will nuke plants with Defoliation if they are of level.

Bots will verify spell immunity before casting all spell types.

Roots are held by default.

Bots will now honor Blocked Buffs. You can use this to get bots to cast other buffs. If you only want Virtue for example you would block Faith, Kazad's Mark and Ward of Gallantry.
--Look at bot spells lists on Allaclone to see what spells they can cast to control this.

Bots will now cast buffs that contain Illusions if you don't block them (Boon line for example.)

You can now set your player characters/clients to specific heal thresholds and delays that bots will respect.
-------
Pets will be healed using the default delay settings and can be toggled on/off with ^holdpetheals
-You can control when they start healing pets by stances, stances will only be used for this now as everything else is customizable
-The exception to this is that Warriors, Paladins and Shadowknights will enter a taunting state by default if set to Aggressive. This can still be toggled off by ^taunt as usual.

The thresholds for stances are as follows:
-Reactive will do all the regular default heals starting with HoTs @ 85%, CHs @ 70%,  Regular Heals @ 55% and Fast Heals @ 35%
-Efficient will start with CHs @ 70%, Regular Heals @ 55%, Fast Heals @ 35%
-Balanced (default) will start with Regular Heals @ 55% and Fast @ 35%.
-Burn will only cast Fast Heals/Regular Heals starting at 35%.
-BurnAE will only Fast Heals/Regular Heals starting @ 25%.
-Aggressive will ignore all and not heal at all, you don't want a tank stopping to heal.

-If a bot cannot cast a Fast Heal, CH or HoT, they will try the next best spell in order of: Fast Heal->Regular Heal->Complete Heal->Heal Over Time.
-Any Heal that casts in 2 seconds or less is considered a Fast Heal

---
## [rbutoi/dotfiles](https://github.com/rbutoi/dotfiles)@[40f2e6f48d...](https://github.com/rbutoi/dotfiles/commit/40f2e6f48d0f000b7cd4e61a34741cb43aaec257)
#### Tuesday 2022-11-29 18:33:08 by Radu Butoi

monday morning sway ricing

* laptop-friendly pgup/down binds
* waybar backlight back (useful!)
* wshowkeys +bind
* pulse number-less after all

+ emacs frequent config file opening key binds, because of course
+ p10k don't right-align time because it's ugly with my (frequent)
terminal resizes
+ kitty config parity to wezterm, good backup

---
## [da-blackest-funeral/podcast-finder](https://github.com/da-blackest-funeral/podcast-finder)@[996b18d7ac...](https://github.com/da-blackest-funeral/podcast-finder/commit/996b18d7ace076aef0be85cdc07886c59ed714d1)
#### Tuesday 2022-11-29 19:08:33 by Казарян Фёдор

oh my gosh i love this song 🎧 too and much more now than without you and your amazing beautiful music i can't stop crying 😭 i miss your face i can't believe you're so good 😊 so proud 🥹

---
## [eebssk1/HeroicGamesLauncher](https://github.com/eebssk1/HeroicGamesLauncher)@[3f6541c8a7...](https://github.com/eebssk1/HeroicGamesLauncher/commit/3f6541c8a700511cea9f0c9b572a5d2138ee76e3)
#### Tuesday 2022-11-29 19:38:08 by Mathis Dröge

Improve README and developer experience (#1807)

* Update VSCode configuration

* Lots of README changes

- Update our bages; might've overdone it a little, but they're fun to add :^)
- Add badges for Web Technologies used
- Rewrite & bump up system requirements a bit
- Wrap the Language list, Development in a container, and Screenshots in
  <details>; this makes the page load faster and makes it seem less
  daunting
- Add a Flathub badge to the Flatpak section
- Unify Linux install instructions (as much as possible)
- Remove 3rd-party APT repository
  In my opinion, we have enough distribution formats already, and the
  install instructions are a little dodgy
- Add Beta AUR package to the list
- Clarify Windows install instructions by splitting up WinGet and manual
  install
- Make "Development environment" its own section
- Remove Beta and Alpha notes on Windows and macOS build instructions
- Explain what exactly is happening when you run `yarn dev` and in which
  scenarios you might want to use it
- Move the "Back to top" badge to the actual bottom of the page

* Add a Content Security Policy

This doesn't really do much in our situation:
- Just in case someone ever manages to load a website in Heroic's main
  window, no JS can run inside it
- Gets rid of the warning in the console when testing with `yarn dev`

I've tested the Webviews (unaffected) and links to ProtonDB and such
(also unaffected, not sure why though). Please test if this breaks
anything

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[35b5ac0c4e...](https://github.com/tgstation/tgstation/commit/35b5ac0c4e6bbaf2adf277a7ea7a4a4eab89726b)
#### Tuesday 2022-11-29 20:13:35 by Fikou

Psykers (#71566)

## About The Pull Request
Finishes #66471
At burden level nine (or through a deadly genetic breakdown), you now
turn into a psyker.
This splits your skull in half and transforms it into a weird fleshy
mass. You become blind, but your skull is perfectly suited for sending
out psychic waves. You get potent psy abilities.
First one is brainwave echolocation, inspired by Gehennites (but not as
laggy).
Secondly, you get the ability of Psychic Walls, which act similarly to
wizard ones, but last shorter, and cause projectiles to ricochet off
them.
Thirdly, you get a projectile boost ability, this temporarily lets you
fire guns twice as fast and gives them homing to the target you clicked.
Lastly, you get the ability of psychic projection. This terrifies the
victim, fucking their screen up and causing them to rapidfire any gun
they have in their general direction (they'll probably miss you)
With most of the abilities being based around guns, a burden level nine
chaplain now gets a new rite, Transmogrify. This lets them turn their
null rod into a 5-shot 18 damage .77 revolver. The revolver possesses a
weaker version of antimagic (protects against mind and unholy spells,
but not wizard/cult ones). It is reloaded by a prayer action (can also
only be performed by a max burdened person).
General Video: https://streamable.com/w3kkrk
Psychic Projection Video: https://streamable.com/4ibu7o

![image](https://user-images.githubusercontent.com/23585223/204150279-a6cf8e2f-c678-476e-b72c-6088cd8b684b.png)

## Why It's Good For The Game
Rewards the burdened chaplain with some pretty cool stuff for going
through hell like losing half his limbs, cause the current psychics dont
cut it as much as probably necessary, adds echolocation which can be
used for neat stuff in the future (bat organs for DNA infuser for
example).

## Changelog
:cl: Fikou, sprites from Halcyon, some old code from Basilman and
Armhulen.
refactor: Honorbound and Burdened mutations are brain traumas now.
add: Psykers. Become a psyker through the path of the burdened, or a
genetic breakdown.
add: Echolocation Component.
/:cl:

Co-authored-by: tralezab <spamqetuo2@gmail.com>
Co-authored-by: tralezab <40974010+tralezab@users.noreply.github.com>
Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[a753229ee2...](https://github.com/tgstation/tgstation/commit/a753229ee2541e32164772f05330669d3c6b75d8)
#### Tuesday 2022-11-29 20:45:55 by GoldenAlpharex

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
## [otemitay/zulip](https://github.com/otemitay/zulip)@[23a776c144...](https://github.com/otemitay/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Tuesday 2022-11-29 21:12:05 by Mateusz Mandera

maybe_send_to_registration: Don't reuse pre-existing PreregistraionUser.

There was the following bug here:
1. Send an email invite to a user.
2. Have the user sign up via social auth without going through that
   invite, meaning either going via a multiuse invite link or just
   straight-up Sign up if the org permissions allow.

That resulted in the PreregistrationUser that got generated in step (1)
having 2 Confirmations tied to it - because maybe_send_to_registration
grabbed the object and created a new confirmation link for it. That is a
corrupted state, Confirmation is supposed to be unique.

One could try to do fancy things with checking whether a
PreregistrationUser already have a Confirmation link, but to avoid races
between ConfirmationEmailWorker and maybe_send_to_registration, this
would require taking locks and so on - which gets needlessly
complicated. It's simpler to not have them compete for the same object.

The point of the PreregistrationUser re-use in
maybe_send_to_registration is that if an admin invites a user, setting
their initial streams and role, it'd be an annoying experience if the
user ends up signing up not via the invite and those initial streams
streams etc. don't get set up. But to handle this, we can just copy the
relevant values from the pre-existing prereg_user, rather than re-using
the object itself.

---
## [arimah/condict](https://github.com/arimah/condict)@[ac652a5f94...](https://github.com/arimah/condict/commit/ac652a5f949115aa508e1a0d1bc872242c67f3fd)
#### Tuesday 2022-11-29 21:46:58 by Arimah

server: Implement the collation logic ourselves

So, this may seem a bit overkill. Let me explain myself.

The previous `unicode` collation worked mostly fine. However, it had a
few notable shortcomings:

- It was completely dependent on `Intl.Collator`, the precise semantics
  of which are *not* guaranteed to be stable across Node versions. Since
  the collation affects not just end-user ordering, but database indexes
  as well, more stability is required. Implementing it ourselves affords
  us the necessary stability guarantees.

- In addition to stability, we also get full control of how things are
  sorted. In the case of Condict, I explicitly implemented the "Shifted"
  strategy as described in the Unicode Collation Algorithm standard.
  This chiefly means punctuation is sorted differently. For example, we
  get the order `a, -b, b, b-, c` - very useful for a dictionary where
  people might want to add suffixes and prefixes. I imagine it is more
  desirable for `-b` to be sorted amongst its `b` friends than lumped
  together with other prefix-looking things.

  The collation data in this implementation is based on the CLDR root
  collation element table. It's a decent compromise that does not (and
  cannot) work for all languages.

- It was not exactly efficient. In order to compare strings, both
  strings had to be copied into V8 values, then passed to the V8
  interpreter, which does some magic probably-native stuff with
  `Intl.Collator`. Very likely this involves validating arguments and
  other time-wasting behaviour. When comparing many strings, this
  results in a large amount of memory being allocated and released, with
  possible GC pauses.

  For most common strings, the new implementation does not allocate
  anything other than a bit of stack space.

  However, note that V8 relies on the extraordinarily well-optimized ICU
  library for its collation. Based on informal benchmarks, Condict's
  performance appears surprisingly comparable to `Intl.Collator`, being
  usually no more than 1.5x slower (and often much closer to 1). Exactly
  how this happened, I don't know, as my code has received minimal work
  on optimisation. With more effort, Condict could be made even faster.

- V8 can throw exceptions, but SQLite3 collations must be infallible.
  The collation function can be called pretty much anywhere, any time.
  SQLite may decide to call it when sorting, searching, inserting,
  updating, deleting, reindexing, or whenever it pleases. Errors in the
  collator can potentially corrupt the database. The only situations in
  which our new collator can throw are (i) in case of a bug that is
  lurking somewhere, (ii) when memory runs out. The former is likely to
  happen eventually, as this new implementation is not nearly as battle-
  tested as ICU. The latter is a no-win scenario anyway: there's usually
  nothing we can do to recover from OOM.

- Being implemented as a Node module with a hard Node dependency meant
  it could not be loaded outside of Condict. It was impossible to open a
  Condict database in an SQLite browser, as there was no way to ensure a
  compatible `unicode` collation was loaded. By having it as a dynamic
  library without Node dependency, anyone can load it, enabling future
  out-of-Condict tooling.

The large tables in the `.inc` files are generated by a tool that I have
not released anywhere *yet*. It may come later. They are based on data
for Unicode 15.0.0 and CLDR v42.

In addition to the implementation, I have included some script to test
for conformance. Currently, conformance tests must be compiled
explicitly, with `npm run build:native -- --group=test`, and the
resulting binary must be explicitly called. On Windows, you would run
`.\build\Release\collation_test.exe`. The test script relies on some
*sizable* (~20 MB) data files provided by Unicode, and these are fetched
on demand.

---
## [DataDog/dd-trace-rb](https://github.com/DataDog/dd-trace-rb)@[e65a90939e...](https://github.com/DataDog/dd-trace-rb/commit/e65a90939e5d255dfea8e64a7ab38d81f75c0ab4)
#### Tuesday 2022-11-29 23:11:52 by Ivo Anjo

[PROF-6556] Leave SIGPROF signal handler after disabling profiling

**What does this PR do?**:

This PR changes the teardown behavior of the `CpuAndWallTimeWorker`
collector to NOT remove its SIGPROF signal handler, and instead
leave behind an empty one.

**Motivation**:

While doing other experiments with signal handling, I discovered that
if the Ruby VM receives a SIGPROF signal without having a signal handler
setup, it defaults to the awful UNIX/POSIX behavior of instantly dieing
with a confusing "Profiling timer expired" message (that has nothing to
do with our profiler).

I reasoned that because signal handling is asynchronous, the following
theoretical situation may happen:
1. `CpuAndWallTimeWorker` sends SIGPROF signal
2. `CpuAndWallTimeWorker` notices request to shut down
3. `CpuAndWallTimeWorker` removes SIGPROF signal handler during teardown
4. Process receives SIGPROF, causing it to die.

I strongly suspect this may never happen in practice, but as
documented in the comment I added, the cost of my suspicion being
wrong is really high, so just-in-case I decided to instead leave
behind an empty signal handler.

**How to test the change?**:

Change includes test coverage. Additionally, you can doublecheck
the change in behavior by doing something like:

```
$ DD_TRACE_DEBUG=true DD_PROFILING_ENABLED=true DD_PROFILING_FORCE_ENABLE_NEW=true bundle exec ddtracerb exec pry
D, [2022-11-23T09:31:54.278186 #22975] DEBUG -- ddtrace: [ddtrace] (components.rb:384:in `startup!') Profiling started
[1] pry(main)> Datadog.configure { |c| c.profiling.enabled = false };;
D, [2022-11-23T09:32:08.580276 #22975] DEBUG -- ddtrace: [ddtrace] (profiler.rb:29:in `shutdown!') Shutting down profiler
[3] pry(main)> Process.kill("SIGPROF", Process.pid)
```

and you'll see that the Ruby process stays alive. If you do the
same thing to a process with no profiler, you'll see the process die
when you send it the SIGPROF signal.

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[0b9264ce5f...](https://github.com/Zergspower/Skyrat-tg/commit/0b9264ce5f14565e42d5e3dc67660a95f5d48f65)
#### Tuesday 2022-11-29 23:29:59 by SkyratBot

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
## [victormayowa/NYSC-Camp-Disease-Prevalence-Data-Analysis](https://github.com/victormayowa/NYSC-Camp-Disease-Prevalence-Data-Analysis)@[8409f1bf25...](https://github.com/victormayowa/NYSC-Camp-Disease-Prevalence-Data-Analysis/commit/8409f1bf259f3207484885a24069fd2f62b1db5a)
#### Tuesday 2022-11-29 23:31:05 by Victor Mayowa ADELEYE

Add files via upload

#### BACKGROUND 

##### NYSC CAMP ESCAPADE PROJECT


NYSC (National Youth Service Corps) is a program that was founded in 1973, by the government of Nigeria aimed to involve Nigerian graduates in nation-building and the development of the country.(Wikipedia:https://en.wikipedia.org/wiki/National_Youth_Service_Corps)


Some few weeks ago, I was privileged to be among those who were mobilized to serve my country. I was posted to Imo state with about 1700 other corp members. Over 3 weeks, we were camped at the NYSC permanent orientation camp, the former Girls Model Secondary School, Eziama Obaire, Nkwerre L.G.A., Imo state; for the usual pre-service drill before service.


As soon as I arrived at the camp, got screened of Covid-19, and finished my camp registration, I was co-opted into the camp clinic, where I participated fully with the team in the management of corp members’ health conditions within the capacity provided by the NYSC and NHIS (National Health Insurance scheme) partnership; under the gracious supervision of Dr. Ikedum, an amiable and hardworking resident doctor from the Federal Medical Centre, Owerri; and Mr. Ifeanyi, the Camp Clinic Manager.


Our team consisted of 6 Medical Doctors, 2 Nurses, 5 Pharmacists, an Optometrist, a dietician, an anatomist, and a Medical Laboratory Scientist. As a team, we were able to successfully manage outpatients and emergencies with the limited resources provided. We referred patients that were beyond the capacity of the clinic and its provisions, appropriately.

I MUST SAY, THESE ONES ARE THE BEST HEALTH TEAM EVERY PRACTITIONER WISHES FOR.

###### CLINIC MEMBERS

__DIETICIAN:__

Raphael Victoria


__OPTOMETRIST:__

Oziegbe Akhere

__ANATOMIST;__

Omotayo Oluwafemi


__MEDICAL LABORATORY SCIENTIST__

Emmanuel Clementina


__PHARMACISTS:__

Omosigho Glory

Morebise Oluwatimlehin

Essien Inemesit

Favour Ndakara

Balogun Peter


__NURSES:__

Hassan Musa

Olanrewaju Hadizat


__MEDICAL DOCTORS__

Odogu Precious

Alao Abigail

Aballa Valentine

Toby Agiopu

Yaji Ibrahim Obel

Adeleye Victor




##### CHALLENGES

The experience over the few weeks exposed me to a whole lot of dynamics that go into the provision of healthcare for patients, especially on insurance schemes, and the accompanying politics thereof. More so when I was privileged to serve as the camp clinic's Chief Medical Director.


We were faced with myriads of challenges administratively and logistically among which are;
scarcity of medications for common ailments in camp at some points (which was looked into by the clinic supervisors),
unavailability of needed rapid diagnostic test kits,
increase in the burden of patients on the swearing-in day,
and a spike in flu-like symptoms which affected some clinic members.
In face of these, we strategically manoeuvre through them as a team with arduous support from the clinic supervisors, we ensured corp members enjoyed the best healthcare services within the capacity of the resources available.


Towards the end of the second week, we realised a surge in the prevalence of flu-like symptoms (such as sore throat, cough, catarrh, runny nose, and infrequent fever) among corp members visiting the clinic.

THE ABOVE TRIGGERED ME TO ANALYSE THE PREVALENCE OF DISEASE CONDITIONS IN THE CAMP. (This will be reflected in subtle details in my next post).


Fortunately, the flu symptoms resolved in response to antihistamines, analgesics with antibiotics for those with fever, sore throat, and/or cough, within 2-4days of treatment for the majority of those involved depending on severity.

In conclusion, it was an eventful experience which enabled me in deploying, learning and honing more skills for healthcare administration and leadership coupled with my potential in data collection, data analysis and research

Furthermore, I saw firsthand the efficiency generated by having loving, brilliant and zealous team members in healthcare who are intentional and compassionate.


Our sincere appreciation goes to the Imo state camp coordinator(), Camp welfare coordinator, Camp clinic manager, our Supervising Resident Doctor from FMC, Owerri, the NHIS state coordinator, and my wonderful and loving Imo state NYSC Batch A, Stream 2 Orientation camp clinic family.


For few weeks, I had dilemmas on how to present the data analysis of the prevalence of common diseases conditions in the orientation camp.

I initially analyzed it with Microsoft Excel 2010 since that was the only software handy during and immediately after orientation camp. However, I received my laptop some few days ago and I felt like having better visuals using Power BI and nicer documentation with my Jupyter notebook.

Consequently, I spoke with one of my accountability partners and she was of the opinion that I work on the markdown presentation too using Jupyter Notebook and that I commenced by drafting out a rough sketch before scripting.




ALREADY POSTED THE ANALYSIS USING MICROSOFT EXCEL PRESENTED USING POWERPOINT ON MY LINKEDIN PAGE (https://www.linkedin.com/posts/adeleye-victor-054a98200_prevalence-of-diseases-in-nysc-orientation-activity-6927708818088812544-LYCO?utm_source=linkedin_share&utm_medium=member_desktop_web)

__THIS IS THE JUPYTER NOTEBOOK DOCUMENTATION USING PANDAS AND OTHER LIBRARIES FOR ANALYSIS__

---
## [TheStrechh/android_kernel_xiaomi_surya](https://github.com/TheStrechh/android_kernel_xiaomi_surya)@[b1b9e38059...](https://github.com/TheStrechh/android_kernel_xiaomi_surya/commit/b1b9e380590435fee05e885e099e7fdb36d44655)
#### Tuesday 2022-11-29 23:41:39 by George Spelvin

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

---
## [breck7/CancerDB](https://github.com/breck7/CancerDB)@[c720c97576...](https://github.com/breck7/CancerDB/commit/c720c97576dd34eb97d257c49b0c9876091f37f8)
#### Tuesday 2022-11-29 23:48:01 by Breck Yunits

Fuck you @NSAGov fuck you @CIA. (though if you let me keep my crypto keys we'll call it a truce)

---

