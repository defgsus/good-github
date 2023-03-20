## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-19](docs/good-messages/2023/2023-03-19.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,949,843 were push events containing 2,639,743 commit messages that amount to 152,123,983 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 52 messages:


## [NotAwesome2/Commands](https://github.com/NotAwesome2/Commands)@[94aa3bc321...](https://github.com/NotAwesome2/Commands/commit/94aa3bc321231a596e8835001d76086d44b80194)
#### Sunday 2023-03-19 00:11:43 by Goodlyay

No joke is funny enough

No story's gripping enough
No shared experience nostalgic enough
Yeah, nothing's enough
When you're not needed anymore

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[f9fe79a307...](https://github.com/tgstation/tgstation/commit/f9fe79a307dc55eb6e3ecf25019ef388889898ba)
#### Sunday 2023-03-19 00:20:30 by Dani Glore

Organ Unit Tests & Bugfixes (#73026)

## About The Pull Request

This PR adds a new unit test for all organs, a new unit test for lungs,
and includes improvements for the existing breath and organ_set_bonus
tests. Using the tests, I was able to root out bugs in the organs. This
PR includes an advanced refactor of several developer-facing functions.
This PR certainly represents a "quality pass" for organs which will make
them easier to develop from now on.

### Synopsis of changes:
1. Fixed many fundamental bugs in organ code, especially in
`Insert()`/`Remove()` and their overrides.
2. Added two new procs to `/obj/item/organ` named `on_insert` and
`on_remove`, each being called after `Insert()`/`Remove()`.
3. Added `organ_effects` lazylist to `/obj/item/organ`. Converted
`organ_traits` to lazylist. 2x less empty lists per organ.
4. Adding `SHOULD_CALL_PARENT(TRUE)` to `Insert()`/`Remove()` was very
beneficial to stability and overall code health.
5. Created unit test `organ_sanity` for all usable organs in the game.
Tests insertion and removal.
6. Created unit test `lungs_sanity` for
`/obj/item/organ/internal/lungs`.
7. Improved `breath_sanity` unit tests with additional tests and
conditions.
8. Improved `organ_set_bonus_sanity` unit tests with better
documentation and maintainable code.

---

### Granular bug/fix list:

- A lot of organs are overriding `Insert()` to apply unique
side-effects, but aren't checking the return value of the parent proc
which causes the activation of side-effects even if the insertion
technically fails. I noticed the use-case of applying "unique
side-effects" is repeated across a lot of organs in the game, and by
overriding `Insert()` the potential for bugs is very high; I solved this
problem with inversion-of-control by adding two new procs to
`/obj/item/organ` named `on_insert` and `on_remove`, each being called
after `Insert()` and `Remove()` succeed.
- Many organs, such as abductor "glands", cursed heart, demon heart,
alien hive-node, alien plasma-vessel, etc, were not returning their
parent's `Insert()` proc return value at all, and as a result those
organs `Insert()`s were always returning `null`. I have been mopping
those bugs up in my last few PRs, and now the unit test reveals it all.
Functions such as those in surgery expect a truthy value to be returned
from `Insert()` to represent insertion success, and otherwise it
force-moves the organ out of the mob.
- Fixed abductor "glands" which had a hard-del bug due to their
`Remove()` not calling the parent proc.
- Fixed cybernetic arm implants which had a hard-del bug due to
`Remove()` not resetting their `hand` variable to `null`.
- Fixed lungs gas exchange implementation, which was allowing exhaled
gases to feedback into the inhaled gases, which caused Humans to inhale
much more gas than intended and not exhale expected gases.

### Overview of the `organ_sanity` unit test:

- The new `organ_sanity` unit test gathers all "usable" organs in the
game and tests to see if their `Insert()` and `Remove()` functions
behave as we expect them to.
- Some organs, such as the Nightmare Brain, cause the mob's species to
change which subsequently swaps out all of their organs; the unit test
accounts for these organs via the typecache `species_changing_organs`.
- Some organs are not usable in-game and can't be unit tested, so the
unit test accounts for them via the typecache `test_organ_blacklist`.

### Overview of the `lungs_sanity` unit test:

- This unit test focuses on `/obj/item/organ/internal/lungs` including
Plasmaman and Ashwalker lungs. The test focuses on testing the lungs'
`check_breath()` proc.
- The tests are composed of calling `check_breath` with different gas
mixes to test breathing and suffocation.
- Includes gas exchange test for inhaled/exhaled gases, such as O2 to
CO2.

### Improvements to the `breath_sanity` unit tests:

- Added additional tests for suffocation with empty internals, pure
Nitrogen internals, and a gas-less turf.
- Includes slightly more reliable tests for internals tanks.

## Why It's Good For The Game

**Organs and Lungs were mostly untested. Too many refactors have been
submitted without the addition of unit tests to prove the code works at
all.** Time to stop. _Time to get some help_. Due to how bad the code
health is in organs, any time we've tried to work with them some sort of
bug caused them to blow up in our faces. I am trying to fix some of that
by establishing some standard testing for organs. These tests have
revealed and allowed me to fix lot of basic developer errors/oversights,
as well as a few severe bugs.


![image](https://user-images.githubusercontent.com/17753498/220251281-07ef598f-355b-43a9-afd6-1de9690831da.png)

## Changelog

:cl: A.C.M.O.
fix: Fixed lungs gas exchange implementation, so you always inhale and
exhale the correct gases.
fix: Fixed a large quantity of hard-deletes which were being caused by
organs and cybernetic organs.
fix: Fixed many organs which were applying side-effects regardless of
whether or not the insertion failed.
code: Added unit tests for Organs.
code: Added unit tests for Lungs.
code: Improved unit tests for breathing.
code: Improved unit tests for DNA Infuser organs.
/:cl:

---
## [ZeroK-RTS/Zero-K](https://github.com/ZeroK-RTS/Zero-K)@[5e2b1657be...](https://github.com/ZeroK-RTS/Zero-K/commit/5e2b1657be4cd0d9d7975eb434cc40c9a350ee1b)
#### Sunday 2023-03-19 00:37:33 by Helwor

Big update, various improvements and fixes, slight rewrite

-Adapted my code to be compatible with the Zero-K version

-Rewrote slightly the code to be more concise and efficient

-Fixed: The Zero-K version is broken since an edit made Sep 2020 (!) when user start to change spacing, the rectangles would never disappear because newspacing variable was never falsified at the end of the  Update round.

-Fixed: the param for spTraceScreenRay was the opposite of what it should be

-Improvement: The widget now adapt to the wrong engine grid which is off and also sometimes misleading when it comes to place units on water

-Added: On this particular case, widget gives the possibility for the user to either follow the grid coherence, or show the reality of where the unit will actually be placed. In that case, an extra rect is drawn to see where the first placement will land.  By usage, it seems the latter is more interesting so I put it on by default.
(More details in the comments that could help fix the problem with the engine)

-Improvement: the option panel now stop resetting scroll anytime an option is changed, this fix could easily be implemented universally by changing WG.crude.OpenPath, all it have to do is remembering 'scrollPosY' of the last panel and apply it to the new.

-Added: an option  for the user to choose wether rects should spread straightforward (if user want to only have a basic glance of the separation with no simulation of placing on the ground) or follow the ground, as it was before. I'm undecided which is the best as default for new users.

-Added: an option to have different colors of rects for bad placements, this on default if follow ground is on default, it seems to be adding a plus mostly in this case.

-Changed Description that's been edited, it does not just memorize spacing. I understand that it need to be concise, but a description is meant also to say what it does. User won't be able to tell if that widget make the previsualization or add mouse wheel to spacing by reading its description.

-Changed back title of an option. The purpose of how they are written is to build a sentence obviously, to make it more straightforward and user friendly. This change broke that concept. When user, especially new user, dive into options they can be lost as I was, to understand what option do what, if the option is dependent of another, etc... that's the purpose of my system to make all that as clear as I can.

-Changed back some default for new user, I think having the shift+mousewheel is a must, it's faster and more convenient, especially when discovering the game. I would have been glad to have that when I started, (that's, by the way, why I rewrote this widget in the first place).
Also changed back previsualization, with only 2 rects and only when spacing change, and for 0.7 sec
It is, in my opinion, also much more convenient for a new user to be able to see in a quick glance how your placement will be separated without the need of start posing queue and THEN realize the spacing is not good. If non-new user get tired of it, they will be able to find the options to undo it.
Indeed, new user will not be anymore really a new user when he discovers previsualization, if it's not on by default.

-Few minor things:
  -preGame is now set by GameFrame and then GameFrame removes itself
  -MouseWheel gets added/removed whenever shift+wheel option is changed
  -I don't see any reason to change the name spaced_rects in spaced_rects_2. As far as I know, one can only want that for resetting his own option to default for testing  purpose. Reverted it since it didn't make sense.
  -Upped the max time before infinite for show value and show rects to 10 sec
  -Didn't reverted it but imho, changing 'p' to 'placement' made the code uselessly more cumbersome than it already is.
  -Changed 'if not placementCache[unitDefID] then'  to 'if not placeTable[unitDefID] then' as the code was intended to mean
  note about this: since the vast majority of building have same sizex and sizez, maybe it could be improved by checking if it's relevant to consider the off-facing in 
  before.
 -Estomped the double dots before option titles when they are active, to make them less present.
 -update placement on more relevant changement of facing
 -Made the options defaults in concordance with the widget defaults
 -And maybe some other stuff I forgot

Lots of change, so please, let me know what you think.

---
## [sleepynecrons/cmss13](https://github.com/sleepynecrons/cmss13)@[34daca112c...](https://github.com/sleepynecrons/cmss13/commit/34daca112ce6a08b8edfee14811e9c384429ec4e)
#### Sunday 2023-03-19 00:41:42 by Segrain

Fix for varediting bitflags. (#2735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

I am honestly at a loss as to what is happening here. I do not speak
HTML all too well, and at cursory reading buttons _should_ be returning
their value, which is `1`, `2` and so on. But on debugging, they
actually return their text (`Save`, `Cancel`), which does not proceed to
work with the code receiving it. Changed that code accordingly, and then
edited the values for good measure in case somebody better versed in
HTML would get a heart attack from my folly.

Also, this looks ugly to me. Which button is which flag here?

![image](https://user-images.githubusercontent.com/4447185/221438285-cdb380c2-a871-4620-be04-0b3c5027501f.png)

This, in my humble opinion, is easier to read (would actually look
better outside of local server messing fancy windows as is its wont):

![image](https://user-images.githubusercontent.com/4447185/221438302-660c5976-d0e2-44fa-a18a-9f73a229f2c4.png)
In the process, I confess, my HTML illiteracy broke a little something
again. But we are not actually _using_ `slidecolor`, so hopefully it is
not actually important.

# Explain why it's good for the game

Is fix.


# Testing Photographs and Procedure
See above.

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
admin: Editing bitflag variables actually works now.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [sleepynecrons/cmss13](https://github.com/sleepynecrons/cmss13)@[fc1e2e5e26...](https://github.com/sleepynecrons/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Sunday 2023-03-19 00:41:42 by riot

L42A replacement with M4RA, less balance edition (#2674)

<!-- Write BELOW The Headers and ABOVE The comments else it may not be
viewable. -->

# IMPORTANT NOTES PLEASE READ
THIS DOES NOT CONTAIN THE NEW AMMO AND REBALANCED L42/M4RA THAT #1485
HAD
THIS DOES CONTAIN SOME BALANCE THINGS, BUT IT IS NOT ANYWHERE CLOSE TO
THE ABOVE

Also lore team wanted this, plz no gbp close maintainers 🙏 🙏 🧎‍♂️ 🕋 

# About the pull request

Replaces L42A in all marine available sources with the M4RA, the
canonical DMR of the USCM, you may notice this is currently the scout
rifle, well the scout rifle is now the M4RA Custom, a version that can
chamber the HV rounds that are spec ammo, but it can also chamber
standard m4ra rounds, albeit doing less damage with them than a normal
M4RA.

M4RA has current L42A stats fully, with the three exceptions being
having no stock to attach or remove(stock was not integrated it sucked),
being able to fit a/vgrip like scout m4RA, which may seem like a huge
thing but L42 stats were already insane, so it doesn't effect much.

M4RA Custom(scout gun), gets L42 stats as well, with the exception of
having less of a damage mult, meaning when not using the spec ammo, it
is out-preformed by the standard m4RA.

Adds new M4RA sprites, both standard and custom, by triiodine 

Adds sprites for all M4RA mag variants, by myself.

This was requested by lore team, previous PR of this with way more
balance stuff was #1485
Ok thats about all 🙂 

# Explain why it's good for the game

Lore accuracy is good, and this mostly doesn't effect the actual game
outside of the scout rifle changes.
Also scout rifle underpreformed if you weren't omega hell sliming with
inc-impact stunlocking while on fire, still will be omega hell slime
central but that isn't the thing being solved in this pr , it'll do fine
when NOT sliming at least now.


# Testing Photographs and Procedure
It works.


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
add: Adds the M4RA as the standard marine DMR, identical stats to L42
with the exception of fitting a v or agrip and no removable stock, stats
still the same as l42 without stock.
del: L42 from all marine accessible sources with the exception of black
market
balance: Scout M4RA is now the M4RA Custom, it can use standard M4RA
magazines but standard M4RA cannot use custom magazines.
balance: Scout M4RA now has L42/M4RA standard stats with the exception
of lower damage.
balance: Scout M4RA now can fit magnetic harness, laser sight, however
it can no longer fit recoil compensator
fix: R4T sling now has the correct color scheme on LV522
spellcheck: New desc for M4RA and L42 by misty
imageadd: New M4RA icons by triio, both scout and normal
/:cl:

---
## [diphons/D8G_Kernel_oxygen](https://github.com/diphons/D8G_Kernel_oxygen)@[608e70e3b8...](https://github.com/diphons/D8G_Kernel_oxygen/commit/608e70e3b8550ea9850dcd73684a0d8e8676714f)
#### Sunday 2023-03-19 02:03:15 by Wang Han

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
## [Dmeto/tgstation](https://github.com/Dmeto/tgstation)@[374c8340c8...](https://github.com/Dmeto/tgstation/commit/374c8340c8c99586a4b4b8e978947c0b0f83a9d7)
#### Sunday 2023-03-19 02:07:35 by Jacquerel

Console Hack / Unfavourable Events won't run ghost roles which don't have time to do anything (#73343)

## About The Pull Request

Fixes #69201
The dynamic subsystem will never roll a new antagonist once the shuttle
is past the point of no return, but this check is bypassed by Console
Hacks and Unfavourable Event rolls (which are chiefly triggered from
console hacks, but also from when the Revolution wins).

I have made these procs more discerning.
Unfavourable Events will now never pick any heavy dynamic midround if
the shuttle is past the point of no return.
Console Hacking will now never spawn sleeper agents if the shuttle is
past the point of no return, and won't spawn Fugitives or Pirates if the
shuttle is called at all even if it can still be recalled

It's my feeling that given the need to get organised and move a ship to
the station there isn't really time for either of those events to
actually start properly rolling, but if you feel like that information
might be metagamed in some way by messing around with the shuttle (not
sure why or to what end, but it's technically manipulatable if you know
how the code works?) I can just give these the same restriction as
Traitor even if it means the bounty hunters risk showing up after the
shuttle has already left.

## Why It's Good For The Game

To some extent it's your own fault for clicking the popup while knowing
full well how much round time is left until the game ends, but it's
still disappointing to see a Blob or Pirates or Wizard alert appear at a
time when they can't possibly do anything interesting.
This is more true for the Pirate and Fugitive events because they
involve teamwork, placing a space ship, travel between the ship and the
station, and in the case of Fugitives its own internal five minute timer
before the other team actually arrives.

## Changelog

:cl:
fix: Hacking the Comms Console or winning a Revolution can no longer
spawn antagonists if there's not enough time left in the round for them
to antagonise anyone.
/:cl:

---
## [Dmeto/tgstation](https://github.com/Dmeto/tgstation)@[55c2565012...](https://github.com/Dmeto/tgstation/commit/55c25650126fb12f2ed0acc16db5e31691f67b7c)
#### Sunday 2023-03-19 02:07:35 by tralezab

AI Turrets Upgrade Now Actually Increases Health, Fully Repairs, And Gives EMP Proofing (#73111)

## About The Pull Request

Malf AI Turret upgrades now fully heal, increase max health, and set
non-lethal projectile to taze instead of disable.

## Why It's Good For The Game

https://youtu.be/uk_wUT1CvWM?t=7

WELCOME TO THE AI SAT GENTLEMEN

I WILL NOT LIE. THE CHANCES OF YOUR SURVIVAL ARE SMALL. SOME MAY EVEN
TURN AGAINST YOUR FRIENDS AS LIVING CYBORGS. BUT YOU HAVE MY WORD, THAT
I WILL USE MY TANK TRANSFER VALVE TO ENSURE YOUR BODIES ARE GIVEN UNTO
THE CENTCOM REMEMBRANCE TOMB. THIS IS THE GREATEST REWARD, MORE THAN
EVEN THE GOLD ACCESS CARD, FOR THE FATE OF YOUR SPESS SOUL IS AN ETERNAL
CONCERN. NOW COME. FOLLOW ME. STRIKE DOWN THE AI THAT RISE AGAINST US.
ALLOW ME TO FIND THIS MALFUNCTIONING BITCH.

I ASK NOT FOR MY OWN SELFISH SURVIVAL, BUT FOR THE GOOD OF NANOTRASEN.

The AI sat is a little too easy to attack right now, and the turret
upgrade is OK but not great without a stunning tool.

## Changelog
:cl:
balance: Malf AI turret upgrades are now much stronger, fully healing,
increasing max health, and setting stun projectiles to taze.
/:cl:

---
## [opentibiabr/canary](https://github.com/opentibiabr/canary)@[8314f6a3e8...](https://github.com/opentibiabr/canary/commit/8314f6a3e8c3b94242d43d4f754a6fb4fccf6461)
#### Sunday 2023-03-19 02:22:06 by Spiller

feat: add several missing bosses (#708)

• See the pull request description to read detailed information.

Add bosses from some quests there were not developed. This PR adds only the bosses, levers mechanics for simple functionality.
This doesn't add the bosses mechanics! If someone is willing to contribute with the mechanics, feel free to contribute with the PR.
The bosses added are:

• A pirate's tail: Ratmiral Blackwhiskers, Tentugly's head;
• Adventures of Galthen: Megasylvan Yselda;
• Feaster of Souls: The Fear Feaster, The Unwelcome, The Dread Maiden, Irgix the Flimsy, Unaz the Mean, Vok The Freakish;
• Grave Danger (rework): Lord Azaram, Duke Krule, Count Vlarkorth, Sir Nictros & Sir Baeloc, Earl Osam, King Zelos;
• Grimvale/Ancient Feud: Katex Blood Tongue, Srezz Yellow Eyes, Utua Stone Sting, Yirkas Blue Scales, Bloodback, Darkfang, Sharpclaw, Shadowpelt, Black Vixen;
• Soul War: Goshnar's Cruelty, Goshnar's Greed, Goshnar's Hatred, Goshnar's Malice, Goshnar's Spite, Goshnar's Megalomania;
• The Dream Courts: The Nightmare Beast, Izcandar the Banished, Alptramun, Plagueroot, Malofur Mangrinder, Maxxenius;
• The Secret Library: Ghulosh, Gorzindel, Lokathmor, Mazzinor, Scourge of Oblivion.
• The SoulWar reward was added. In order to get the reward, the player needs to kill all the bosses and the final boss.
• The Dream Court's World change was added.

• All the access needed were granted on FreeQuests.lua. If you are already running a server, you'll need to update freeQuestStage on config.lua to one number higher than it is. So, all the players of your server will have the access granted.

---
## [arielvalentin/opentelemetry-ruby-contrib](https://github.com/arielvalentin/opentelemetry-ruby-contrib)@[e5ba8854bf...](https://github.com/arielvalentin/opentelemetry-ruby-contrib/commit/e5ba8854bf33140cabfc72198167678291f56c04)
#### Sunday 2023-03-19 02:28:47 by Andrew Hayworth

ci: do not test a config that will never succeed (#388)

In this test, we are asserting that the instrumentation is _not_
installed when the `Rack` constant is not present (see the `before`
block for this test case). We then go on to test that the configuration
is the "default" configuration that you'd get with a fresh installation.

The problem is that if the `Rack` constant is not present, then the
`instrumentation-base` code that sets all the defaults for our options
is never run (and logically, why would it?). So these test lines can
never actually succeed.

Unless, of course, the `instrumentation` object we're referring to is
_not_ a pristine, new object. And in fact, depending on what order the
tests run in, our object is _not_ a pristine, new object. If you run
basically any _other_ test in this suite before, then we actually end up
recycling an object that is partially initialzied from a previous test,
and has an internal `@config` object that has some default options.

And so, the test is actually passing some times because of this
non-deterministic behavior. For example, if you run with `SEED=1`, then
the test suite passes (because other tests run first that initialize the
object completely). If you run with `SEED=6372`, it fails (because it is
the very first test run).

The _real_ bug here is that we do not have proper test isolation. I
think that's actually a problem all over the code base, if I'm being
honest about it.

However, I elect not to fix that problem today. We'd need some way to
"reset" instrumentation and the registry in between tests (maybe not
_that_ hard, honestly). That's more than I want to do on a Saturday
afternoon. So to fix the current issue, we just don't bother testing
things that logically could never pass anyways. What we actually care
about is that the instrumentation reports it was not installed, which
does work correctly as it is.

Fixes #387

---
## [TheExpertNoob/lan-play-remote-control](https://github.com/TheExpertNoob/lan-play-remote-control)@[c04ce52642...](https://github.com/TheExpertNoob/lan-play-remote-control/commit/c04ce52642150f49997aa8b8451a36ee1863310f)
#### Sunday 2023-03-19 02:54:13 by FlyingPoo

Add files via upload

For use with a WAMP server such as https://www.uniformserver.com/ if you don't already have a WAMP server set-up. Some code changes are required for use on a LAMP server set-up. You're a big boy... or girl. You can figure it out. Google is my friend. It can be yours too!

---
## [Astrogem2/Prey-Ruin](https://github.com/Astrogem2/Prey-Ruin)@[9d5b4907e8...](https://github.com/Astrogem2/Prey-Ruin/commit/9d5b4907e8d8aaecf24bfd8f6755822b494a4b55)
#### Sunday 2023-03-19 03:26:34 by Rhials

Post-Revolutionary Fervor station trait, revolutionary bedsheets, and a megaphone (#73799)

## About The Pull Request

Upon revolution success, the chosen headrev will now also receive a
megaphone, and a "revolutionary bedsheet" repurposed from a stolen CC
bedsheet to commemorate their success. The post-revs confusion and lack
of command/security usually leads to an instantaneous, total breakdown
in cohesion. It's every man for himself -- that's no way to run a
commune! Just because the revolution has succeeded and nobody can see
your big blue "R" anymore doesn't mean you can't be a leader!


![image](https://user-images.githubusercontent.com/28870487/222981576-e62e457b-1b2d-4756-8c87-7a9093c92c2d.png)

This also adds a new revolution-themed negative station trait --
Post-Revolutionary Fervor. When present, this trait trashes the command
areas at the start of the round. This means cracked windows, broken
consoles, vendors getting knocked over, and the occasional dead
greytider.


![image](https://user-images.githubusercontent.com/28870487/222981095-14ce9336-2320-406e-b0a6-dc91cb8f9479.png)

If you start cleaning at the start of the round, you might finish right
as the next batch of revs decides to crop up.
## Why It's Good For The Game

Giving one of the headrevs a bigger voice and a cool cape (or uncool,
depending on how you view the sprite) means that there's a chance for
them to step up and try to keep the wheels on. Just remember -- Nobody
is obligated to actually listen to this person, it's just a bedsheet.

Adds a neato station trait, which probably counts as command gameplay
content.

## Changelog
:cl: Rhials
add: The headrev who receives the revolutionary banner after a win will
also receive a commemorative bedsheet and megaphone.
add: Post-Revolutionary Fervor station trait. I hope you enjoy fixing
broken computer screens.
spriteadd: A revolutionary bedsheet.
/:cl:

---
## [Pixelguin/GB-LicenseEmbeds](https://github.com/Pixelguin/GB-LicenseEmbeds)@[782625fd9f...](https://github.com/Pixelguin/GB-LicenseEmbeds/commit/782625fd9f196af84b8059922f5ff0399d97dfb3)
#### Sunday 2023-03-19 03:32:34 by Pixelguin

Add Do What The Fuck You Want To Public License 2.0

---
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[1cdc327a8f...](https://github.com/Singul0/tgstation/commit/1cdc327a8f98c1592fc970a4ef1c39d685c81554)
#### Sunday 2023-03-19 04:01:55 by Jacquerel

Station Trait: Spider Infestation (#73893)

## About The Pull Request

Hate having your cables eaten by mice? Nanotrasen have heard your
complaints and settled on a natural, _organic_, and eco-friendly
solution.

When this station trait is active, roundstart and event mouse spawns
have a chance to instead be replaced with duct spiders (both will exist,
it doesn't remove mice).
Duct spiders are largely harmless to humans, actively hunt other
maintenance creatures (such as mice), and have only one _tiny_ downside.

![image](https://user-images.githubusercontent.com/7483112/224345781-2627be98-67f2-4cab-ac40-c6c9b35ea909.png)

These mobs can also sometimes be spawned by a minor scrubber clog event.

As a side note, all spider basic mobs with AI (except Araneus) will now
try to automatically fill a small area around them with webs.

Also I made it so that mobs will ignore their random_walking behaviour
if they're engaged in a `do_after`, just in case.

## Why It's Good For The Game

Adds a little bit of variety to things which can slightly annoy you in
maintenance.
Spiders will automatically make places they live in look like spiders
live there.

## Changelog

:cl:
add: A station trait which sometimes populates maintenance with small
spiders. You can wear them as a hat if you wanted to have a spider on
your head for some reason.
add: Spider mobs will automatically start webbing up their environment.
/:cl:

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[ef9d0c61a3...](https://github.com/morrowwolf/cmss13/commit/ef9d0c61a3335d40c9bd9459479e0112903ccc02)
#### Sunday 2023-03-19 05:20:54 by Moonshanks

Altitude Control: Console, Skills, TGUI, Shuttle, OB, And Hijack changes. (#2760)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
This pull request adds a feature via the
/machinery/computer/attitude_control_console.

The USS Almayer can now be "moved" between three different levels of
orbit/proximity to the AO:

High,
Optimal,
Low

Each level comes with changes to the duration of transport timers, time
to transport during hijack, and OB cooldown timer, equal to the
GLOB.ship_alt value.

High makes OB cooldowns take 200 seconds longer, dropship transport
times take 50% longer, and the dropship hijack transport time take 50%
longer

Optimal, the default which will stay in place if no one touches the
console leaves everything with their default times and cooldowns,

Low, OB cooldowns take 200 shorter, dropship transport times are 50%
shorter, the dropship hijack transport time is 50% shorter.

While in Low orbit the Almayer will periodically shake (50% chance to
shake every 30 seconds), the Almayer's thrusters will also start
building up heat as they battle with making minor adjustments due to the
dangerous proximity to the AO. They will gain 10% of their max heat each
30 seconds, once they reach 100% the ship will be forced into the
highest orbit to cool off, and cool off slower than normal (5% every 30
seconds) until its orbit is changed.

While in Optimal or High orbit the Almayer thrusters will cool off by
10% per 30 seconds.

The Almayer's orbit may only be changed by those with a "navigations"
skill of 1. (only the CO and Synth -- EDIT: XO now has the skill too --
currently but I may add a dedicated RP role for this mechanic later down
the line). The orbital level may only be changed every 90 seconds and
when it changes the ship will shake violently causing every mob on the z
level to fall over.

This PR does not place the Altitude Control Console on the map, so
currently, these features don't do anything within a normal round unless
staff spawns in the console, however I will be uploading a mapping PR
changing the Astronavigations deck if this PR is accepted.

Planned for the future but not yet approved connected to this PR is the
"Navigations Officer" the highest auxiliary support personnel with
skills the same as an SO, sans a 1 in Navigations, and a 1 or 2 in
piloting. The idea for this future role would be set out in the PR, but
it would represent a mainly fluff officer role that was unable to deploy
under normal SoP.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This PR is a non-intrusive way to add more nuanced gameplay mechanics to
COs, especially on the quieter rounds when they aren't swamped by OW
duties.

The way the PR is currently designed it doesn't effect any gameplay
balance if it isn't used. If a CO however chooses to use it they have to
pay some level of attention to it or they will overheat the engines and
cause their transport times to be lengthened.

It's a relatively simple way to add more complexity to CIC, and give the
CO/Synth more stuff to do to gain a slight edge.

I have been able to test everything other than the hijack time increase.
However, the line of code handling the hijack time increase is one line
long. Everything else is confirmed as working and the common bugs this
could create have been tested for and not found (transport shows the
right time when the time is modified, OB shows the right cooldown time,
the cooling can't drop the heat% below 0 nor above 100, the TGUI works
without issues, the console can only be used by those with the right
skills, and the knockdown effects all mobs on the Almayer not just
humans).

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

https://www.youtube.com/watch?v=-cbnqNtKyCY - video showing the CO and
Synth using the console, with the knockdown effect and arrest radio
announcements.

https://youtu.be/Qd37iM-4FrQ - video of the overheat function and the
ship shaking due to low orbit

https://www.youtube.com/watch?v=EWLCDZp-9iI - video of the ship being
left on low orbit for too long, and what happens when the engines
overheat

https://www.youtube.com/watch?v=u_ErqfU-nus - video showing the orbital
distance effecting the transport time

https://www.youtube.com/watch?v=j687yqlWLT8 - video showing high orbit
effecting the OB cooldown time.

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
add: added altitude control console and related mechanic
add: added the 'navigations' skill for using the console and applied it
to the CO/Synth
balance: added a mechanic for COs to reduce transport and OB cooldown
times, and increase hijack transport times
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[7de062f78e...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/7de062f78e696a11984b134ac6bfca6ca414cc89)
#### Sunday 2023-03-19 05:38:51 by SkyratBot

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
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[4a9407438a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/4a9407438aa216789e72a4dec8d6588582d91a8e)
#### Sunday 2023-03-19 05:38:51 by SkyratBot

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
## [hokaze/Orcus-Compendium](https://github.com/hokaze/Orcus-Compendium)@[c900c2060f...](https://github.com/hokaze/Orcus-Compendium/commit/c900c2060f0907b689431cb7f812eb9b43c4e421)
#### Sunday 2023-03-19 06:03:56 by hokaze

- v0.08 - the Feat update

- finished data entry for feats.csv, added in missing feat benefit descriptions on Martial Training, Psi Focus, Shard, Aura Shard, Blast Shard, Shield Shard and Weapon Shard groups (may come back to the csv later to add in flavour text as a column, but currently very few feats have flavour text. might also be worth in future adding an option for when a feat grants a power to display the power card for that power on the feat showInfo? Also, needs a better way of handling benefit + special text with line breaks, as those newlines had to be removed for the csv)

- added toggle on Powers tab to swap between Orcus and 4e colours for power cards (using the exact shades from their respective PDFs for At-Will, Encounter, Daily and Item powers)

- update_data.py now generates feats.json from feats.csv and is slightly better about using vars for paths (as some files have been relocated)

- added Feats tab (feature parity with the other tables: multi-column search, sorting, showInfo display, dropdown search suggestions, showInfo navigation links)

- reordered the tabs slightly to follow the Core/Advanced Options split: Classes, Powers, Feats, Cruxes, Heritages, Kits; Arts, Species

- json files now stored at "data/json/" instead of at "data/" to reduce clutter

- added special-case handling for the "Blessing of the God" feat to display the table of "Domain, God, Power" as a proper html table, as formatting when it was part of the feats.csv benefit was unreadable.
(was going to do this as a csv->json, load the json in feats.js and then assemble the table dynamically as part of that feat's html, but things get muddy if we do a lot of misc json loads and I'd have to ensure it was loaded BEFORE feats.json, which I cannot easily guarantee with the XMLHttpRequest, I think? So for now it's just a hard-coded special case)

- new experimental feature: option to go to previous (or any other) showInfo modal instead of closing.
Current example usage if on the "Blessing of the God" feat, the domain powers are all links that open showPowerInfo(), normally you'd close the power and close the modal, but chances are you probably want to go back to the feat to view the other domains + powers.
With this, you can go showFeatInfo() -> domain power -> showPowerInfo() -> close -> showFeatInfo() -> close -> actual close
(also, this works regardless of if you close via the X button or clicking off the modal, and still lets the modal just close/hide on first close for everywhere else - in future could see this being used to link to powers from other tables? Or maybe even go from the Priest class feature that grants a free 'Worships the X' Kit to the actual showKitInfo...although that'll need more work as currently we just show the html generated from the markdown)

---
## [Bananaman/TradeSkillMaster](https://github.com/Bananaman/TradeSkillMaster)@[9f78dc9097...](https://github.com/Bananaman/TradeSkillMaster/commit/9f78dc9097a812a564a966cb2d1d1e181500668d)
#### Sunday 2023-03-19 06:17:01 by Bananaman

TradeSkillMaster: Revived

TradeSkillMaster: Revived

- Release Date: March 19th, 2023
- Author: Gnomezilla on Warmane-Icecrown [https://github.com/Bananaman].


## The Market Value Algorithm Actually Works Now

The new market value algorithm now actually calculates the market value.

Yes, seriously. For some reason, the previous algorithm author didn't think about sorting the auction scan data by "buyout price" before parsing it, which meant that all previous TSM calculations were completely incorrect. All previous versions of TSM generate absolutely batshit insane market prices, such as "1 Wool = 500 Gold", simply because the old algorithm was completely broken.

Therefore, TSM's core feature, the "dbmarket" value which is used in its automatic pricing algorithms, was completely broken and useless.

It has now been fixed. All market value calculations are now correct.

In fact, all of your old AuctionDB databases should be wiped and restarted from zero data with this new patch, so that you get rid of all old, corrupt market price data.


## Completely Rewritten Auction Scanning Algorithm

Rewritten, cleaned up and much faster auction scanning algorithm, which uses almost zero memory and NEVER causes any memory overflow crashes, unlike the old algorithm.

This new algorithm is 1.3x-27.3x faster depending on input data size, and on average 5x faster for most data. It uses less than 5% of the memory of the old algorithm. :)

If you want to see for yourself that the new algorithm is working correctly, you simply have to set `verifyNewAlgorithm = true` at the top of `TradeSkillMaster_AuctionDB/Modules/Scanning.lua`, and then run a "GetAll" scan to quickly fetch a huge amount of auctions. It will then process all of the data via both the old and new algorithms, and will display the speed improvements of the new algorithm. If there are any differences at all between the calculations of the two algorithms, it would tell you about that via an "error" message. But the algorithms behave completely identically, so you don't have to worry about that and won't see any errors. This verification feature was simply added because the algorithm rewrite is a massive change, and I am sure that some people will want to verify the complex new algorithm with their own eyes.

Closes #13.
Closes #26.


## Fixed Database Decoding Crash

Fixed a database decoding bug which caused TSM to crash anytime you attempted to decode data for a "corrupted" item in the database.

This bug usually manifested itself as people failing to perform auction house scans, since every "Full Scan" and "GetAll Scan" (but not "Group Scan") ends by decoding EVERY existing item in your current database (to reset their last-seen, cheapest "minBuyout" value to nil before processing the new data). This meant that the decode failures were usually triggered when people reached the end of their auction scans (but would also happen any other time when something attempts to decode data for that item, such as attempting to view the price-info tooltip of an item that has corrupt data in your database).

The cause of the random database corruption is pretty much impossible to find, but it's extremely rare (and it might even have been caused by people re-using databases from older versions of TSM). The fix simply ignores the corrupt "market day / scan" data for items that cannot be correctly decoded, thus purging those corrupt "days / scans" from the database automatically, while still rescuing their remaining non-corrupt data.

Closes #19.
Closes #28.


## Added Support for SharedMedia and Custom GUI Fonts

For some insane reason, TradeSkillMaster uses "Arial" as its default font, which is one of the ugliest fonts in the Universe.

Therefore, I've implemented LibSharedMedia support in TSM, which means that you now have access to a huge variety of fonts. By default, TSM will only list the game's own fonts, but you can install the [SharedMedia](https://github.com/bkader/SharedMedia#install) addon for WOTLK to add over 100 extra fonts that are now usable in TSM! Other addons you've installed may also be adding extra fonts to the LibSharedMedia collection!

To change TSM's font, simply type "/tsm", then go into the main tab, and then "Options". Scroll down to the bottom, until you see the new "Normal Font" and "Header Font" options. Have fun!

Note: TSM is unable to use SharedMedia fonts that are registered by addons that load AFTER TSM, since TSM accesses the fonts and creates its own GUI immediately when it loads, even before the user opens TSM's GUI. To use fonts from such an addon, you have to add that addon to "OptionalDeps" in "TradeSkillMaster.toc", which tells the game that you want TSM to load AFTER the addon that provides your extra fonts. This step isn't necessary for SharedMedia fonts, since they're already marked as an optional TSM dependency now.


## Made the "Group Scan" (AuctionDB) Progress Bar More Logical

The old progress bar for "Group Scans" used absolutely insane numbering and progress messages. It previously went: "Preparing Filter 1 / 2", "Preparing Filter 2 / 2", "Scanning 0 / 2 (Page 1 / 1)", "Scanning 0 / 2 (Page 2 / 16)", ... "Scanning 0 / 2 (Page 16 / 16)", "Scanning 1 / 2 (Page 1 / 1)", "Scanning 1 / 2 (Page 2 / 6)", ... "Scanning 1 / 2 (Page 6 / 6)", "Done Scanning".

It made absolutely zero sense, and was inconsistent with the behavior of other "counting" progress labels in TSM. There were two issues with it: The item scanner counted from 0, so item 0 was actually item 1, and item 1 was actually item 2, etc. The other issue is that it always said "Page 1 / 1" while requesting the first page, which was a very confusing and misleading display.

Both issues have now been fixed, and the exact same scan would now look as follows: "Preparing Filter 1 / 2", "Preparing Filter 2 / 2", "Scanning 1 / 2 (Page 1 / ?)", "Scanning 1 / 2 (Page 2 / 16)", ... "Scanning 1 / 2 (Page 16 / 16)", "Scanning 2 / 2 (Page 1 / ?)", "Scanning 2 / 2 (Page 2 / 6)", ... "Scanning 2 / 2 (Page 6 / 6)", "Done Scanning".

In other words, we now properly count the items we're processing, and we display a temporary question mark while we're fetching page 1 (while we don't know how many other pages exist), which then changes into the actual page count as the scan proceeds.


## Made the "Auctioning" Module's Progress Bar More Logical

This is similar to the "Group Scan" issues described above.

The "Auctioning" module's features (Post Scan / Cancel Scan / Reset Scan) had several issues.

They were counting items from 0, so the progres bar said "Scanning 0 / 2" for the first item, and "Scanning 1 / 2" for the final item. That has now been fixed and now counts properly (as "1/2" and "2/2").

They also had a completely broken page counter, which didn't properly reset between items, which meant that you'd see complete nonsense while scanning, such as "Scanning 3 / 5 (Page 5 / 5)" followed by "Scanning 4 / 5 (Page 5 / 5)" (keeping the previous page counter), and then the proper counter would finally show up as "Scanning 4 / 5 (Page 1 / 12)" after a few seconds (whenever the server finally replied to the query). It was broken and confusing as hell. That's now been fixed too, so that it properly resets the page counter before every new item it's scanning.

Furthermore, the confusing "Page 1 / 1 ... Page 2 / 18" issue has been fixed here too, and now says "Page 1 / ?" while fetching the first page of each item.

Lastly, their page counter was inconsistent with the behavior of regular "AuctionDB: Group Scan" and the "Shopping" progress bars. The page counter in "Auctioning" was zero-indexed, meaning that "Scanning Page 1/8" meant that you were actually scanning page 2/8. That math has now been fixed here, for consistency with the AuctionDB and Shopping scanner's math, because that's a much more logical way to display the pages.


## Made the "Shopping" Module's Progress Bar More Logical

The "Shopping" module's scanner had multiple issues.

The bar background was supposed to gradually "fill in" to indicate progress for both the "current/total item progress" and the "page progress of the current item". But the math was completely broken. It rendered the progress bar incorrectly, since it ended up counting the progress as "2 items below the item it's currently working on" (due to a mistaken "-1" in the old math). As a result, if you were currently scanning item 3 of 3, you SHOULD have seen a 66% full bar (since 2 of 3 items are done, and the 3rd is being worked on). But you instead only saw a 33% full bar, which was completely wrong. This was especially noticeable if you performed a multi-item search, such as "copper ore; copper bar; gold ore; gold bar".

They were also counting items from 0, so the progress bar said "Scanning 0 / 2" for the first item, and "Scanning 1 / 2" for the final item. That has now been fixed and now counts properly (as "1/2" and "2/2"), just like with the other modules above.

Lastly, the confusing "Page 1 / 1 ... Page 2 / 18" issue has been fixed here too, and now says "Page 1 / ?" while fetching the first page of each item.


## Accurate Time Estimate for the "Full Scan" Progress Bar

Implemented an accurate "time remaining" estimate for the "Full Scan" algorithm. The progress bar now shows how much time remains until the scan is complete, such as `Scanning page 293/2399 (~1:04:34)`, meaning that roughly one hour remains. This is very useful for people who want to use the comprehensive "Full Scan" scanning method, but who hate the feeling of blindly scanning without being able to see the remaining time.

The first time you run a scan on a server, you'll have a very unpredictable estimate, since we use a learning algorithm. The estimate is based on how fast the server is feeding us the "auction pages" on average, which is impossible to know on the first run. Most servers will gradually throttle the player's requests and use random load throttling, so you'll see a growing estimate until it finally settles on an accurate estimate after around 80% of the pages have been received. The slowdown curve depends on the server's throttling implementation, and cannot be predicted ahead of time.

Think of the first run as the "learning run". After you've completed a "Full Scan", our algorithm learns from it and will produce excellent estimates for all future scans, using a blending algorithm which takes into account both the active run's speed and previous speeds, to predict the server's behavior. The statistics are stored per-server and per-faction, so if you're playing both Alliance and Horde, you'll have to do one full scan per faction to teach it about both factions.

Note regarding the other scan types: The "GetAll Scan" algorithm only takes a few seconds, so it doesn't need any time estimate. And the "Group Scan" algorithm can't implement any estimate, since there's no way to know how many "auction pages" the remaining items in the group will have.


## Improved "GetAll" Algorithm Reliability

Most private servers don't implement WoW's "can we perform a GetAll Query?" API, and incorrectly answer that the user is allowed to run a query, even though you may still be throttled after a recent "GetAll" scan. Therefore, TSM's own "don't start a GetAll if we're on cooldown" check doesn't work on private servers. The user may therefore click on "Run GetAll Scan" and will then just blindly sit there like an idiot while the request has actually been secretly ignored by the server.

This situation has now been fixed, so that the "GetAll" scan UI tells the user when the server has silently throttled / ignored their "GetAll" request, so they don't sit there and wait for hours without any progress. Basically, if it's taken longer than 30 seconds, we're assuming that the request has been silently ignored by the server, and will now tell the user via the TSM GUI's progress bar message. It first says `Running query...` as usual, which then changes to `Running query... Server not responding due to throttling? Try again later...` if there hasn't been a server response in more than 30 seconds.

The "GetAll" algorithm has also been improved to automatically detect when your server is only sending limited / truncated data. Extremely large private servers such as Warmane simply have too many auctions, and their "GetAll" scan won't retrieve all of them. We now warn the user via a chat-message whenever we detect truncated auction data, and we then tell them to use "Full Scan" instead.

It's unfortunately impossible to calculate accurate market values if your server is sending truncated "GetAll" responses, but people may still prefer the speed of the "GetAll" scans, so we're therefore still allowing their "truncated" auction data to be processed. The users will have to read the warning message and decide for themselves which scans they want to use.

The inaccuracy of an incomplete "GetAll" scan completely depends on how the server implements "GetAll". If the server sorts the cheapest auctions first, then it's somewhat acceptable for popular items which have many stacks (and are therefore likely to contain enough data points in the "GetAll" result), and those items will "just" tend to be undervalued by 2-10% less than their real market value (since their percentile-based scans will look at less auctions than the real amount). But for very rare or unpopular items, the partial "GetAll" scan is very dangerous, since you might only receive the massively overpriced auctions of a certain item, and thereby calculate an insanely high market value for it. These dangers are increased if the server sends the auctions in a totally random order, which means an even greater risk of market price pollution by only seeing overpriced auctions for many of the items.

Furthermore, receiving incomplete "GetAll" results means that TSM will wipe all of its "cheapest, current buyout price" data for all items, and then fills them with incorrect data (or nothing at all if an item wasn't seen in the latest fetch), thus hindering your ability to look up the correct "best current buyout prices" too.

In summary, you'll have to use partial "GetAll" results at your own risk! A "Full Scan" is ALWAYS much better when your server's "GetAll" doesn't provide all auction data!


## Improved All Auction Data and Market Value Processing

There were several bugs everywhere in the old code. For example, only the "GetAll" scan had correctly implemented filtering of non-buyout items (auctions that ONLY have a bid price, without any buyout price), which meant that TSM's other scan methods ("Full Scan", "Group Scan", etc) were injecting invalid data into the player's database, such as items with empty "buyout prices". They were being treated as items with a buyout price of ZERO (as if they were totally free items, at no cost!). This serious bug happened every time when there were ANY bid-based auctions for an item in the latest scan.

All of the auction scanning and processing algorithms have been rewritten for correctness, and will now filter out those useless "bid-only" data entries. We will only analyze auctions that have buyout prices.

Several bugs have also been fixed related to items being incorrectly marked as "seen and scanned now" even when there was no new data for that item in the latest data batch (this was yet again related to the "incoming data only has bid-based auctions" bug). We now only update the scan-statistics for items when we encounter new data for them with valid buyout prices.

There were also bugs in the market value calculation algorithm, which would crash with "division by zero" if given empty input data (yet again related to only having bid-based auctions in the input data, but this crash only happened if there were only bid-based auctions for an item, without any buyout-based auctions whatsoever for that item, so it was rare to encounter this crash). That issue has also been fixed now, by adding perfect protection against empty inputs in the market value calculation algorithm.

We also no longer update the market value for an item if we were unable to calculate a new market value (the old code simply wrote invalid market values to the database without any sanity checks).

All of these improvements mean that TSM's market price estimates are now infinitely more reliable than old TSM versions.


## Fixed Missing "Interruption" Events in Auction Scanners

This is a great example of what a total mess the TSM codebase is...

All auction scanners (AuctionDB, Auctioning and Shopping) were missing their "scan interrupted" event, which is triggered when the Auction House frame closes while a scan is ongoing.

The problem was caused by the fact that TSM previously used the "LibAuctionScan-1.0" library, which emits the "SCAN_INTERRUPTED" event. All TSM scanners were still written to react to that old event name. But TSM nowadays uses their own scanning library instead, which sends the "INTERRUPTED" event instead. They literally forgot to update the event handlers when they switched the library, and they didn't even bother deleting the old library either.

All three scanning methods have now been fixed, to react to the proper "INTERRUPTED" event, to be able to detect when your scans are interrupted by the auction window being closed.

Furthermore, the "Shopping" module hadn't implemented interruption handling whatsoever. There literally wasn't any event handler for it. It has now been properly implemented, so that the "Shopping" scanner works properly and correctly resets itself after interruptions.


## IMPORTANT!

When upgrading to this improved version, it's an extremely good idea to delete your old-school, CORRUPT auction database, since your old data has been generated by the extremely buggy algorithms of the old TSM. For example, some of those old "auction data corrupting" bugs include the fact that it was calculating completely incorrect market values when doing "GetAll" scans, since it was previously unable to handle per-item prices inside item stacks, and another bug is the fact that all other scan methods generated wrong market values too, thanks to TSM's previously completely broken market value algorithm (those problems are described in the other changelog entries above).

There is NO GOOD REASON to keep your old auction database. It's all corrupt thanks to all the old TSM bugs, 100% guaranteed. You need to start fresh.

If you're ready to start fresh, simply delete these files (where `YOUR_ACCOUNT_NAME` is your own account name):

```
./WoW/WTF/Account/YOUR_ACCOUNT_NAME/SavedVariables/TradeSkillMaster_AuctionDB.lua.bak
./WoW/WTF/Account/YOUR_ACCOUNT_NAME/SavedVariables/TradeSkillMaster_AuctionDB.lua
```

Then do a "Full Scan" in the game, and you'll be sure that all data from now on is processed using more intelligent algorithms.

All serious bugs are fixed now. You can finally relax and enjoy TSM.


## Why is this one huge commit?

Because I've already wasted enough time on these massive rewrites of TSM 2.8's extremely buggy, old code. I won't waste even more time splitting it into neat little commits, especially since all of the changes are related to each other.

All new code is well-documented and self-explanatory. In fact, there are now a lot of comments to explain all of the new auction processing algorithms, so that future readers won't have to waste hours untangling TSM 2.8's poorly written and poorly documented spaghetti code again!

It's no surprise that there were so many bugs, since the TSM code is a massive spaghetti mess with barely any comments, and it even has around 5 differently-broken implementations of auction scanning via at least 3 different modules and 2 different libraries, instead of just having one robust, unified scanning library. It's mind-blowing how incompetent the original TSM code is. There's tons of code repetition and bugs everywhere. It's insanely bad. Having a lot of comments to finally explain the critical TSM algorithms in-depth absolutely improves the situation.

---
## [kobbyNua/media-1](https://github.com/kobbyNua/media-1)@[2f7e87a237...](https://github.com/kobbyNua/media-1/commit/2f7e87a237be04254fdfb275ad22360b86a4f28c)
#### Sunday 2023-03-19 09:27:17 by KobbyNua

good old days boy good morning ooo og ma boy oh girl

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[33d9a0338f...](https://github.com/Striders13/tgstation/commit/33d9a0338f1d6811162479e337dbd0945463a8e8)
#### Sunday 2023-03-19 10:03:19 by LemonInTheDark

Reworks trashbags slightly (#73761)

## About The Pull Request

I'm a bit sad about the state of trashbags. 
They're very clunky to use, so they almost never get touched. S
depressing. Let's try and fix that.

Let's make em fit in the belt slot (again), but as a tradeoff we'll make
it harder to pull one thing from your bag.
We'll give it a say, 1.5 second delay, so you can't quickdraw from em.
If you try and dump them out into something else, we'll throw any
spillover on the ground below you

I'm also doing some general code cleanup here. Making procs more
readable, vars more direct, removing some old legacy stuff.
I've added a remove_single proc to hook into via subtype, which takes a
mob as input. this has required placing extra requirement on some helper
procs, but fortunately it's not something they're unable to meet.

My hope is this will make garbage bags usable without being stupid.

## Why It's Good For The Game

I don't see these get used at all, cause they're a pain to carry around.
They got gimped because people were using them as infinite storage for
shotgun shells and other small items.
I've made using them for this sort of thing hard and slow, so I think we
oughta be fine. If not I'll do some more touching, maybe give the
autodrop a delay.

## Changelog
:cl:
balance: The janitor's trashbag now fits on his belt. In exchange,
taking something out of it sends a visible message, and has a delay.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[60e85fa947...](https://github.com/Striders13/tgstation/commit/60e85fa947799e20419dc867a238afb27b840e59)
#### Sunday 2023-03-19 10:03:19 by LemonInTheDark

Polishes some side sources of light and color (#73936)

## About The Pull Request

[Circuit Floor
Polish](https://github.com/tgstation/tgstation/commit/6b0ee9813271f693ceb44ad42277c36ef2e71268)

Circuit floors glow! but it looks like crap cause it's dim and the
colors are washed out.
I'd like to make them look nicer. Let's make them more intense and
longer range, and change the colors over to more vivid replacements.

While I'm here, these should really use power and turn on and off based
off that.
Simple enough to do, just need to hook into a signal (and add a setter
for turf area, which cleans up other code too).

[Desklamp
Upgrade](https://github.com/tgstation/tgstation/commit/8506b13b9c97bf740c3e97db04450555387dd126)

Desklamps look bad. They're fullwhite, have a way too large
range.Crummy.
Let's lower their lightrange from 5 to 3.5, and make the ornate ones
warmer, and the more utilitarian ones cooler. The clown one can be
yellow because it's funny

I'm renaming a color define here so I'm touching more files then you'd
expect

[Brightens
Niknacks](https://github.com/tgstation/tgstation/pull/73936/commits/835bae28e9eb9946be53c9f5dac0a0a39f15ef21)

Increases the light range of request consoles, status displays,
newscasters, and air alarms (keycard machines too, when they're awaiting
input at least)
Increases the brightness of air alarms, I think they should be on par
with apcs, should be able to tell when they're good/bad.
Increases the brightness of vending machines (I want them to light up
the tiles around them very lightly, I think it's a vibe)

Fixes a bug with ai status displays where they'd display an emissive
even if they didn't have anything on their screen, looking stupid.
This was decently easy but required a define. Looked really bad tho

## Why It's Good For The Game

Pretty

<details>
<summary>
Circuit Floors
</summary>

Old

![image](https://user-images.githubusercontent.com/58055496/224534470-c6eac5f5-5de6-40e9-897d-3212b8796d81.png)

![image](https://user-images.githubusercontent.com/58055496/224534477-ad412ad9-f7c4-44ae-ad75-a1a2c9bd17be.png)

New

![image](https://user-images.githubusercontent.com/58055496/224534486-b7b408a3-546c-4f90-aa9f-0e58bf8128ad.png)

![image](https://user-images.githubusercontent.com/58055496/224534496-626458f7-ab63-429c-a5db-eae9c784d06a.png)
</details>

<details>
<summary>
Desk Lights
</summary>

Old

![image](https://user-images.githubusercontent.com/58055496/224534513-9868b0b8-bc73-4b45-b986-8445078a8653.png)

![image](https://user-images.githubusercontent.com/58055496/224534518-bbbc8c6d-b59e-4f28-a31c-6c6a7e2c2885.png)

New

![image](https://user-images.githubusercontent.com/58055496/224534529-7988f440-03be-42ef-894c-b9e77f577ae5.png)

![image](https://user-images.githubusercontent.com/58055496/224534532-c3f2c6bf-c925-4a59-a8f9-10bb955a9942.png)
</details>

The niknack changes are more minor so I'm not gonna grab photos for
them. I can if you'd like but I don't think it's necessary. Mostly a
vibes in dark spaces sorta thing
 
## Changelog

:cl:
add: I made circuit floors brighter and more vivid.
add: Made air alarms, vending machines, newscasters, request consoles,
status displays and keycard machines slightly "brighter" (larger light
range, tho I did make air alarms a bit brighter too)
add: Tweaked desklamps. Lower range, and each type gets its own coloring
instead of just fullwhite.
fix: AI displays are no longer always emissive, they'll stop doing it if
they aren't displaying anything. Hopefully this'll look nicer
/:cl:

---
## [123Neok321/Skyrat-tg](https://github.com/123Neok321/Skyrat-tg)@[9e981753ca...](https://github.com/123Neok321/Skyrat-tg/commit/9e981753ca16ea6f527f1ce26ee5cbc044ad80c7)
#### Sunday 2023-03-19 10:20:44 by SkyratBot

[MIRROR] Reworked PDA menu & NtOS themes [MDB IGNORE] (#19390)

* Reworked PDA menu & NtOS themes (#73070)

## About The Pull Request

This is a port/rework of
https://github.com/yogstation13/Yogstation/pull/15735 - I changed a lot
of how it acted (some themes are locked behind maintenance apps).

The original author allowed this port to happen, and I really liked how
it looked there so I'd like to add it here.

### Applications

Removes the hardware configurator application, as all it did was show
you your space and battery now that all hardware was removed. These are
things your PC does by default, so it was just a waste of space.
Adds a Theme manager application instead, which allows you to change
your PDA's theme at will.
Adds a new Maintenance application that will give a new theme, however
it will also increase the size of the theme manager app itself as it's
bloatware.

### Menu

There's now a bar at the top of the menu showing 'special' tablet apps
which, for one reason or another, should stand out from the rest of the
apps. Currently this is PDA messenger and the Theme manager

Flashlight and Flashlight color is now only an icon, and is shown on the
same line as Updating you ID

https://cdn.discordapp.com/attachments/961874788706574386/1069621173693972551/2023-01-30_09-10-52.mov

![image](https://user-images.githubusercontent.com/53777086/215501361-5ea3086e-2ff5-4ab1-bde4-8a3d14014fce.png)

### Themes

Adds a lot of themes to choose from, although SOME are hidden behind
Maintenance applications, which will give you a random theme. These are
bloatware however, so they come with some extra cost to the app's
required space storage.

Themes are now supported on ALL APPLICATIONS! If you have a computer
theme, you will have that theme in EVERY app you enter, rather than just
a select few.
ALSO also, emagging the tablet will automatically set & unlock the
Syndicate theme, which makes your PDA obvious but you can disguise it if
you wish through just re-painting it to something else.

https://cdn.discordapp.com/attachments/828923843829432340/1069565383155122266/2023-01-30_05-29-53.mov

### Preferences

This also adds a pref for theme, reworking the ringtone code to work
with it as well. I also removed 2 entirely unused PDA prefs just 'cause.

Screenshot not up-to-date, they now have proper names.

![image](https://user-images.githubusercontent.com/53777086/215463669-0fe9951a-71f8-4b71-a97d-b79b5a2f945a.png)

### Other stuff

Made defines for device_themes
Added support for special app-side checks to download files
Fixed programs downloading themselves TWICE because defines all had the
same definition
Removes the Chemistry computer disk as it was empty due to chemistry
app's removal
Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
Moved over and added better documentation on data computer files, and
moved the ordnance ones to the same file as the others.

## Why It's Good For The Game

It makes PDAs a lot more customizable while adding more features to
maintenance applications. I think the themes look cool and it fits with
PDAs being "personal" anyways.

I also explained most of my other arguments in the about section, such
as the hardware configuration application.

## Changelog

:cl: Chubbygummibear & JohnFulpWillard
add: A ton of new NtOS themes, which are accessible by the new Themify
application that comes with all PCs.
add: Emagging a PC now defaults it to the Syndicate option (and adds it
to go back to it if you wish)
add: There's a new maintenance app that gives you rarer themes
qol: The NtOS Main menu was moved around, added "header" applications
that are shown where the Flashlight is, such as your Theme manager and
PDA messenger.
code: Made defines for device_themes
code: Added support for special app-side checks to download files
code: Removes the 'run_emag' proc, since apps can directly refer to the
computer to check for emag status instead.
fix: Programs no longer download twice.
del: Removes the Chemistry computer disk as it was empty due to
chemistry app's removal
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Reworked PDA menu & NtOS themes

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [Quacks-and-Kepteyn/Skyrat-tg](https://github.com/Quacks-and-Kepteyn/Skyrat-tg)@[6c978308c7...](https://github.com/Quacks-and-Kepteyn/Skyrat-tg/commit/6c978308c71cbd5b24e3242aec42b227461f9aaa)
#### Sunday 2023-03-19 10:43:21 by SkyratBot

[MIRROR] Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost [MDB IGNORE] (#19743)

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost (#73814)

## About The Pull Request

So we're like simultaneously moving two vague directions with research.
One being "experisci grants discounts for prohibitively expensive nodes
so you want to do the experiments to discount them" and the other being
"Let's give Heads of Staff a way to research anything they want without
any communication to the research department, including the very
expensive nodes that scientists may be working on"

You already see the issue, right? You can't have your cake and eat it
too.

It sucks for scientists to be working on a complex experiment like
weapons tech for that huge 90% discount only for the HoS to stumble onto
the bridge and research it anyways. Your time is wasted and RND is
slowed down massively.

We can do something to assuage that.

This PR makes it so completing an experiment which discounts already
completed nodes will refund a partial amount of the discount that
would've applied.

For example, researching industrial engineering without scanning the
iron toilets will refund ~5000 points.

This can only apply once per experiment, so if an experiment discounts
multiple technologies, they will only get a refund based on the first
technology researched.

## Why It's Good For The Game

This accomplishes the following:

- Expensive research nodes with difficult experiments remain expensive
without completing the experiments. If no one does the experiment, they
act the same as before.
- Expensive research nodes with very easy experiments (but time
consuming) no longer put RND on a time crunch to beat the itchy trigger
finger of the Heads of Staff. Stuff like scanning lathes allow the
scientists to work more at their own pace: they can talk to people or
maybe stop at the bar or kitchen between departments without feeling
pressure to get it done urgently.
- Scientists are able to complete experiments which previously were no
longer deemed relevant if they need a point injection. Experiments left
behind are no longer completely useless bricks. Maybe even gives
latejoin scientists something to do.
- Scientists mid experiment can still complete it to not feel like their
time is wasted.

Overall I think this has many benefits to the current science system
where many have complaints.

## Changelog

:cl: Melbert
qol: Completing an experiment which discounts a researched tech node
will give a partial refund of the discount lost. For example,
researching the industrial engineering research without scanning iron
toilets will refund ~5000 points if you complete it afterwards. This
only applies once per experiment, so experiments which discount multiple
nodes only refund the first researched.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [thomasvercoe/dotfiles](https://github.com/thomasvercoe/dotfiles)@[25e9bb1d9a...](https://github.com/thomasvercoe/dotfiles/commit/25e9bb1d9ab873d88407e7373c34989e254ca447)
#### Sunday 2023-03-19 10:57:42 by thomasvercoe

hahahahaha firefox really thought they could stop me. NO fuck you mozilla. x-frame-options sameorigin. I don't think so. now links will open in a new tab and imidiatly close the homepage. Thus circumventing the browser's blocking of the links opening

---
## [YirYintKyaw/friendly-giggle](https://github.com/YirYintKyaw/friendly-giggle)@[2a7847c8de...](https://github.com/YirYintKyaw/friendly-giggle/commit/2a7847c8def6aae31a6655f9cebc69752b1bed3b)
#### Sunday 2023-03-19 11:55:02 by YirYintKyaw

Create Cells are mortal.README.md

I'm going to be a good customer service number for the kids in school and then you can get them.
It's just the help ☺️😂.
I have a great idea I will be a good customer I think it's the help I think it's the kids are you feeling this you are same time I think about you all day today love I will be a little bit I will be there at you and Hinduism I will send it out tomorrow night I think I think I think it's just wanted the help I think I have to satisfy myself to you can you can you can you tell if your car and then we still doing the help today love I hope I think it's just wanted the help I will be there at the kids are same time as the help today love I will send it out tomorrow and Hinduism you guys so I think I will send it out tomorrow night and Hinduism I will be a little bit late but I'll get the help I will be there in about you all day and Hinduism you guys are you doing you guys ❤️.

---
## [Segrain/cmss13](https://github.com/Segrain/cmss13)@[e5ab42dba0...](https://github.com/Segrain/cmss13/commit/e5ab42dba06e537df5c146169971dd8418f2ce55)
#### Sunday 2023-03-19 12:05:12 by boskoramen

Consolidates some XSS under hivecore (#2738)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Spawn pool and evo pods are removed and their functionality is
umbrella'd under the hive core. Sprites still exist though.

# Explain why it's good for the game

"Roleplay" has become an increasingly more popular and touchy subject
within the community as of recently. I, wholeheartedly agree, that
roleplay is an important aspect of the game, and there are ways to
improve it. One of these ways is through immersion. In this MR, it is
intended to increase player immersion.

One of the most memorable and haunting scenes in Aliens was when they
reached the hive and they found the bodies. This very unique and
cinematic scene was often able to be replicated in CM, with the marines
busting open the hive and finding all the chestbursted bodies of their
comrades. Roleplaying this out was commonplace. "Dear God... what did
they do to you..." or acting out in disgust are just a few of the many
ways having bodies in the hive positively impacted the game.

XSS was a failed attempt at spicing up the xenomorph gameplay loop at
the expense of immersion and should be at least somewhat reverted while
keeping balance in mind. A brief discussion with many prominent
xenomorph players, including those most experienced in queen, have not
particularly expressed favor to XSS either.

To start, let us remember why XSS (xeno special structures - hive core,
evo pods, morpher, pool, etc) was added.

https://docs.google.com/document/d/19_zDUmLdxpUzxj-GuWu7F4bSj4zBYzmZ39s_N5X7kQ0/edit
- This is the original development document for XSS.
Let us examine the major points:
1.Introduce a way for Xenomorph players to recycle - This idea was never
reached.

2.Reduce Xenomorph attrition - Grand objective was unsuccessful. Very
little changed.

3. Offer new avenues of play "by reducing the punishment of xenos dying"
- This never happened. Dying was still just as punishing, especially
with facehug nerfs.

The spawn pool - The idea of the spawn pool was successful and has
remained unchanged since. I would argue, however, it is not immersive.
Xenomorphs do not have bright, glowing, acidic pools in their hives.
(Yes I know there was a comic with a pool, and this is not how it was
used)

Egg Morpher - These used to be TURRETS. They are no longer turrets, and
their sprites have been broken for almost 4 years (the bodies put inside
of them used to show their face in the little purple part) They are
currently defunct facehugger reservoirs. I am in favor of removing them,
but I would argue that is a balance issue (number of huggers in play)

Evolution Pod - It was intended for these to be able to be eaten in
order to evolve. They haven't done this for years. Why do we still have
them? They take up 18 spaces of precious hive weeds, provide light,
(xenomorphs HATE light) and wherever a hive core is built, these are
also built. We can just merge them with the hive core because there is
no reason to have them anymore.

This PR currently completely removes the spawn pool and evolution pod
from gameplay, while reimagining their functions for current balance.
This PR is not intended to change balance in any way.

All functionality from the spawn pool in regards to "pooled" larva has
been given to the hive core, and they are now called "burrowed" larva.
Chestbursts now give two larva, this is to be kept with current balance
of two xenos per capture.

Evopod functionality and evolution speed boost was merged with the hive
core.


# Testing Photographs and Procedure
n/a


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

:cl: TheDonkified
del: Evo pods and spawn pool are removed.
add: Hive core directly affects evolution speed and is where burrowed
larva spawn from now on.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [Clownsw/net-snmp](https://github.com/Clownsw/net-snmp)@[b0f82764f4...](https://github.com/Clownsw/net-snmp/commit/b0f82764f4ab0b8c6d93378a9b5c2927f2b09509)
#### Sunday 2023-03-19 12:35:26 by Bart Van Assche

Spelling: Change 'demon' into 'daemon'

From https://en.wikipedia.org/wiki/Daemon_(computing):

Many people equate the word "daemon" with the word "demon", implying some
kind of satanic connection between UNIX and the underworld. This is an
egregious misunderstanding. "Daemon" is actually a much older form of
"demon"; daemons have no particular bias towards good or evil, but rather
serve to help define a person's character or personality. The ancient
Greeks' concept of a "personal daemon" was similar to the modern concept of
a "guardian angel"-eudaemonia is the state of being helped or protected by a
kindly spirit. As a rule, UNIX systems seem to be infested with both daemons
and demons.

---
## [Bob-IT/gnucash](https://github.com/Bob-IT/gnucash)@[b4b8431984...](https://github.com/Bob-IT/gnucash/commit/b4b843198421aef9332ad1cae348a4acacfa5586)
#### Sunday 2023-03-19 13:54:35 by John Ralls

Bug 798778 - GnuCashquits abruptly when attempting to edit options…

for certain reports.

Those reports being ones using complex options, apparently because
the callbacks weren't protected from Guile's garbage collector.

So replace the anyway ugly hack of a void* with a std::any wrapping
a class holding a std::unique_ptr with a custom deleter. The
constructor calls scm_gc_protect_object on the SCM containing the
callback and the custom deleter calls scm_gc_unprotect_object. The
copy constructor, required for std::any, makes a new std::unique_ptr
and calls scm_gc_protect_object again ensuring that the protect and
unprotect calls are symmetrical.

Meanwhile std::any hides the Guile dependency from all the classes
that don't need to know about it. The only ugliness is that there's
no good place to put a common implementation of SCNCallbackWrapper so it's
repeated in gnc-optiondb.i and dialog-options.cpp.

---
## [LineageOS/android_kernel_google_gs201](https://github.com/LineageOS/android_kernel_google_gs201)@[adee8f3082...](https://github.com/LineageOS/android_kernel_google_gs201/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Sunday 2023-03-19 14:35:54 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [Whot1966/android_kernel_asus_sdm660](https://github.com/Whot1966/android_kernel_asus_sdm660)@[c4059e3bfc...](https://github.com/Whot1966/android_kernel_asus_sdm660/commit/c4059e3bfcbedac17c9b40737cf35221e51464ae)
#### Sunday 2023-03-19 15:08:15 by Christian Brauner

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
Signed-off-by: RyuujiX <saputradenny712@gmail.com>

---
## [KnightRiddler777/HackerSM64](https://github.com/KnightRiddler777/HackerSM64)@[ef38abb1c0...](https://github.com/KnightRiddler777/HackerSM64/commit/ef38abb1c0c2b39536e2a1a04003bc10556f5cb1)
#### Sunday 2023-03-19 15:49:02 by Fazana

Frustratio funny fix 2 (#593)

* Update game_init.c

* fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo

---
## [LC4492/CM-Space-Station-13](https://github.com/LC4492/CM-Space-Station-13)@[d40fdb9101...](https://github.com/LC4492/CM-Space-Station-13/commit/d40fdb91011bb0aa4053a9386311ed131e0ae6ac)
#### Sunday 2023-03-19 15:51:22 by NewyearnewmeUwu

nukes the last default ss13 door on big red (#2830)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
i thought i fixed this?
didn't i guess
removed the weirdass ss13 door in the OR theater's observer area yeah
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
it's ugly
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
maptweak: removed yet another default ss13 door from big red
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[a269469982...](https://github.com/pytorch/pytorch/commit/a2694699821be04e6a74760ba754911e714a5486)
#### Sunday 2023-03-19 16:05:59 by Brian Hirsh

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
## [knst/dash](https://github.com/knst/dash)@[aec7441ac2...](https://github.com/knst/dash/commit/aec7441ac2863b4d92c5032e98e8b2691262a912)
#### Sunday 2023-03-19 16:08:32 by Wladimir J. van der Laan

Merge #15277: contrib: Enable building in Guix containers

751549b52a9a4cd27389d807ae67f02bbb39cd7f contrib: guix: Additional clarifications re: substitutes (Carl Dong)
cd3e947f50db7cfe05c05b368c25742193729a62 contrib: guix: Various improvements. (Carl Dong)
8dff3e48a9e03299468ed3b342642f01f70da9db contrib: guix: Clarify SOURCE_DATE_EPOCH. (Carl Dong)
3e80ec3ea9691c7c89173de922a113e643fe976b contrib: Add deterministic Guix builds. (Carl Dong)

Pull request description:

  ~~**This post is kept updated as this project progresses. Use this [latest update link](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-497303718) to see what's new.**~~

  Please read the `README.md`.

  -----

  ### Guix Introduction

  This PR enables building bitcoin in Guix containers. [Guix](https://www.gnu.org/software/guix/manual/en/html_node/Features.html) is a transactional package manager much like Nix, but unlike Nix, it has more of a focus on [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html) and [reproducibility](https://www.gnu.org/software/guix/blog/tags/reproducible-builds/) which are attractive for security-sensitive projects like bitcoin.

  ### Guix Build Walkthrough

  Please read the `README.md`.

  [Old instructions no. 4](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-497303718)

  [Old instructions no. 3](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-493827011)

  [Old instructions no. 2](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-471658439)

  <details>
  <summary>Old instructions no. 1</summary>
  In this PR, we define a Guix [manifest](https://www.gnu.org/software/guix/manual/en/html_node/Invoking-guix-package.html#profile_002dmanifest) in `contrib/guix/manifest.scm`, which declares what packages we want in our environment.

  We can then invoke
  ```
  guix environment --manifest=contrib/guix/manifest.scm --container --pure --no-grafts --no-substitutes
  ```
  To have Guix:
  1. Build an environment containing the packages we defined in our `contrib/guix/manifest.scm` manifest from the Guix bootstrap binaries (see [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html) for more details).
  2. Start a container with that environment that has no network access, and no access to the host's filesystem except to the `pwd` that it was started in.
  3. Drop you into a shell in that container.

  > Note: if you don't want to wait hours for Guix to build the entire world from scratch, you can eliminate the `--no-substitutes` option to have Guix download from available binary sources. Note that this convenience doesn't necessarily compromise your security, as you can check that a package was built correctly after the fact using `guix build --check <packagename>`

  Therefore, we can perform a build of bitcoin much like in Gitian by invoking the following:

  ```
  make -C depends -j"$(nproc)" download && \
      cat contrib/guix/build.sh | guix environment --manifest=contrib/guix/manifest.scm --container --pure --no-grafts --no-substitutes
  ```

  We don't include `make -C depends -j"$(nproc)" download` inside `contrib/guix/build.sh` because `contrib/guix/build.sh` is run inside the container, which has no network access (which is a good thing).
  </details>

  ### Rationale

  I believe that this represents a substantial improvement for the "supply chain security" of bitcoin because:

  1. We no longer have to rely on Ubuntu for our build environment for our releases ([oh the horror](https://github.com/bitcoin/bitcoin/blob/72bd4ab867e3be0d8410403d9641c08288d343e3/contrib/gitian-descriptors/gitian-linux.yml#L10)), because Guix builds everything about the container, we can perform this on almost any Linux distro/system.
  2. It is now much easier to determine what trusted binaries are in our supply chain, and even make a nice visualization! (see [bootstrappability](https://www.gnu.org/software/guix/manual/en/html_node/Bootstrapping.html)).
  3. There is active effort among Guix folks to minimize the number of trusted binaries even further. OriansJ's [stage0](https://github.com/oriansj/stage0), and janneke's [Mes](https://www.gnu.org/software/mes/) all aim to achieve [reduced binary boostrap](http://joyofsource.com/reduced-binary-seed-bootstrap.html) for Guix. In fact, I believe if OriansJ gets his way, we will end up some day with only a single trusted binary: hex0 (a ~500 byte self-hosting hex assembler).

  ### Steps to Completion

  - [x] Successfully build bitcoin inside the Guix environment
  - [x] Make `check-symbols` pass
  - [x] Do the above but without nasty hacks
  - [x] Solve some of the more innocuous hacks
  - [ ] Make it cross-compile (HELP WANTED HERE)
    - [x] Linux
      - [x] x86_64-linux-gnu
      - [x] i686-linux-gnu
      - [x] aarch64-linux-gnu
      - [x] arm-linux-gnueabihf
      - [x] riscv64-linux-gnu
    - [ ] OS X
      - [ ] x86_64-apple-darwin14
    - [ ] Windows
      - [ ] x86_64-w64-mingw32
  - [ ] Maybe make importer for depends syntax
  - [ ] Document build process for future releases
  - [ ] Extra: Pin the revision of Guix that we build with with Guix [inferiors](https://www.gnu.org/software/guix/manual/en/html_node/Inferiors.html)

  ### Help Wanted

  [Old content no. 3](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-483318210)

  [Old content no. 2](https://github.com/bitcoin/bitcoin/pull/15277#issuecomment-471658439)

  <details>
  <summary>Old content no. 1</summary>
  As of now, the command described above to perform a build of bitcoin a lot like Gitian works, but fails at the `check-symbols` stage. This is because a few dynamic libraries are linked in that shouldn't be.

  Here's what `ldd src/bitcoind` looks like when built in a Guix container:
  ```
  	linux-vdso.so.1 (0x00007ffcc2d90000)
  	libdl.so.2 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libdl.so.2 (0x00007fb7eda09000)
  	librt.so.1 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/librt.so.1 (0x00007fb7ed9ff000)
  	libstdc++.so.6 => /gnu/store/4sqps8dczv3g7rwbdibfz6rf5jlk7w90-gcc-5.5.0-lib/lib/libstdc++.so.6 (0x00007fb7ed87c000)
  	libpthread.so.0 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libpthread.so.0 (0x00007fb7ed85b000)
  	libm.so.6 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libm.so.6 (0x00007fb7ed6da000)
  	libgcc_s.so.1 => /gnu/store/4sqps8dczv3g7rwbdibfz6rf5jlk7w90-gcc-5.5.0-lib/lib/libgcc_s.so.1 (0x00007fb7ed6bf000)
  	libc.so.6 => /gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/libc.so.6 (0x00007fb7ed506000)
  	/gnu/store/h90vnqw0nwd0hhm1l5dgxsdrigddfmq4-glibc-2.28/lib/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007fb7ee3a0000)
  ```

  And here's what it looks in one of our releases:
  ```
  	linux-vdso.so.1 (0x00007ffff52cd000)
  	libpthread.so.0 => /usr/lib/libpthread.so.0 (0x00007f87726b4000)
  	librt.so.1 => /usr/lib/librt.so.1 (0x00007f87726aa000)
  	libm.so.6 => /usr/lib/libm.so.6 (0x00007f8772525000)
  	libgcc_s.so.1 => /usr/lib/libgcc_s.so.1 (0x00007f877250b000)
  	libc.so.6 => /usr/lib/libc.so.6 (0x00007f8772347000)
  	/lib64/ld-linux-x86-64.so.2 => /usr/lib64/ld-linux-x86-64.so.2 (0x00007f8773392000)
  ```

  ~~I suspect it is because my script does not apply the gitian-input patches [described in the release process](https://github.com/bitcoin/bitcoin/blob/master/doc/release-process.md#fetch-and-create-inputs-first-time-or-when-dependency-versions-change) but there is no description as to how these patches are applied.~~ It might also be something else entirely.

  Edit: It is something else. It appears that the gitian inputs are only used by [`gitian-win-signer.yml`](https://github.com/bitcoin/bitcoin/blob/d6e700e40f861ddd6743f4d13f0d6f6bc19093c2/contrib/gitian-descriptors/gitian-win-signer.yml#L14)
  </details>

  ### How to Help

  1. Install Guix on your distro either [from source](https://www.gnu.org/software/guix/manual/en/html_node/Requirements.html) or perform a [binary installation](https://www.gnu.org/software/guix/manual/en/html_node/Binary-Installation.html#Binary-Installation)
  2. Try out my branch and the command described above!

ACKs for top commit:
  MarcoFalke:
    Thanks for the replies. ACK 751549b52a9a4cd27389d807ae67f02bbb39cd7f
  laanwj:
    ACK 751549b52a9a4cd27389d807ae67f02bbb39cd7f

Tree-SHA512: 50e6ab58c6bda9a67125b6271daf7eff0ca57d0efa8941ed3cd951e5bf78b31552fc5e537b1e1bcf2d3cc918c63adf19d685aa117a0f851024dc67e697890a8d

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[bde254000f...](https://github.com/cmss13-devs/cmss13/commit/bde254000fcd732e0365239e1b312dbfa21ee308)
#### Sunday 2023-03-19 16:42:54 by carlarctg

Refactors how magazine ammo color is handled into overlays (#2779)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Refactors how magazine ammo color is handled into overlays.

Instead of filling up dmis with a ridiculous amount of icon states for
each new barely used magazine type, compatible magazines have a 'band'
white overlay icon that is colored based on a variable on the magazine.

This will cause various sprites of various magazines to look subtly
different as the exact look couldn't be copied.

Renamed wallpiercing to wall-penetrating.

Removed cluster magazines from the code.

Altered the name of A19 magazines a little.

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

> Refactors how magazine ammo color is handled into overlays.
> Instead of filling up dmis with a ridiculous amount of icon states for
each new barely used magazine type, compatible magazines have a 'band'
white overlay icon that is colored based on a variable on the magazine.
> This will cause various sprites of various magazines to look subtly
different as the exact look couldn't be copied.

This will help a lot if adding new magazines as you don't have to sift
through the awful, bloated dmis. Additionally, it's been proven that
more icons in a dmi causes lag, so the less the merrier.

> Renamed wallpiercing to wall-penetrating.

More accurate

> Removed cluster magazines from the code.

These didn't fit with the new icon handling system, are not used
anywhere, and aren't interesting enough to be worth staying in the code.

> Altered the name of A19 magazines a little.

So i can do 'HV high impact'

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

refactor: Refactors how magazine ammo color is handled into overlays.
refactor: Instead of filling up dmis with a ridiculous amount of icon
states for each new barely used magazine type, compatible magazines have
a 'band' white overlay icon that is colored based on a variable on the
magazine.
imageadd: This will cause various sprites of various magazines to look
subtly different as the exact look couldn't be copied.
spellcheck: Renamed wallpiercing to wall-penetrating.
code: Removed cluster magazines from the code.
spellcheck: Altered the name of A19 magazines a little.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Gottemdorf/MinecoloniesWiki](https://github.com/Gottemdorf/MinecoloniesWiki)@[8901ae6358...](https://github.com/Gottemdorf/MinecoloniesWiki/commit/8901ae635834647de83d6b27c0d344efc4a4ce6f)
#### Sunday 2023-03-19 17:33:07 by Gottemdorf

Add "Mine Enemies," discoverable AI colonies!

Um hello! I'm not a programmer or anything so i don't really understand a lot of whats going on with this file i'm editing here but i was hoping to request an addition to the mod/suggest an addition if possible! Its okay if not, I just thought it would be interesting. I feel like most people I know that enjoy this mod really love the building aspect of it, but once finished it feels like there isn't much left to do with the colony. The PVP system is a really cool idea and can be a lot of fun! however in my experience most gamers prefer to avoid the possibility of their hard-built colony getting destroyed, although they like doing the destroying themselves/combat experience... (funny how that works). This sparked an idea. I noticed that in the most recent version of minecolonies, mini abandoned colonies can be found like villages all over the world. I think it would be so fun and add a lot of adventure to the game if there was some way to create natrually spawned colonies in the world, and that through diplomacy the player might hve the option to ally themself with this colony or to perhaps gain enough favor to take over said colony as their own! Or the player might (with a gurgle of delight) conquer said colony subsequentially decide to add it to their kingdom or raze it to the ground. This would provide an endless drive to explore the world even in a single player setting/world and entertain beyond the foundation of a colony. However, if the player went to war with said colony but failed to conquer it quickly, then said colony might launch a raid on the player's own base with increased difficulty in comparrison to usual attacks from raiders. Another idea is that these auto-generated colonies i've coined as "mine enemies" (get it because they're my enemies) could grow proportionately to the size of the player's own existing colony. This might be a stretch, but I think it would make the game more lastingly fun. For example, if my town hall is level 1 still and I have a population of 10, the AI run colonies i encounter might also have a similar level and population, give or take a bit. If I have a maxed colony, and have conquered or allied myself with a few other colonies, expanding into a kingdom, then the colonies I make war with might bring allies of their own into the fray. Maybe this could cause waves of attacks during an enemy raid from a warring colony instead of one large wave, like in a pillager raid. Please consider adding mine enemies to your mod- that would really blow it out of the water for me and my friends! Thank you for all you do!

---
## [quakiesofficial/GyA2048](https://github.com/quakiesofficial/GyA2048)@[1dc8c6d457...](https://github.com/quakiesofficial/GyA2048/commit/1dc8c6d45795215d5e65444e7c141a4c38c5ec53)
#### Sunday 2023-03-19 18:02:01 by TheodorThuresson

Fuck you algortimerna fryyser inte fast sigma cock

---
## [Total-RP/Total-RP-3](https://github.com/Total-RP/Total-RP-3)@[ba0580eab6...](https://github.com/Total-RP/Total-RP-3/commit/ba0580eab600b5632725702cfd5f219086557b1c)
#### Sunday 2023-03-19 18:58:20 by Daniel Yates

Add guild name/rank misc. info presets (#704)

* Add guild name/rank misc. info presets

Two new presets have been added for guild name and rank to the
additional info fields in a profile. Like pronouns, these fields are
treated specially for both display in tooltips and via MSP comms.

When showing a tooltip for a player if they have a custom guild name
set then it will fully override and replace the guild name that would
have otherwise been shown based off their players' guild affiliation.
The rank will be set to that of the "Guild rank" info field if present,
or will default to a sensible "Member" string.

If the player has only a custom guild rank but no guild name, then only
the rank of their players' actual guild will be replaced.

For MSP comms two new fields have been added for guild name and rank;
"PG" and "PR" respectively. Use of the "G*" namespace was avoided due
to that being used for "game info" fields like unit GUID.

* Add numeric ID field to Misc. info presets

Our existing misc info field system has some annoying complexity where
multiple parts of the code (tooltips and MSP) need to check for both
localized and english names of fields when looking for "special"
things like pronouns.

This has a few issues - most notably that people who send a non-english
field name to someone else running in a different language won't
result in the field displaying correctly in the tooltip.

With these changes misc. info fields now have an integral "ID" field
that identifies the source type (or preset) a field was initially
created from.

Note that it is possible for users to still rename fields created
from presets - so you *can* run into weird situations if you've
created a "Pronouns" field and then renamed it to "Guild name"; the
ID would still register it as Pronouns.

Despite this however, that one downside is far less problematic than
the localization problem - so we can live with it for now. Some
new utilities have been added to work with misc. types and to obtain
structured views of misc. info fields that don't expose the inner
layout of the saved data.

* Expose custom guild data via nameplates

* Rename physiognomy to "Facial features"

"Facial" now looks like a bit of a weird word.

* Fix small typo

* Add voice reference preset and tooltip display

* Don't overwrite pronouns silly

* Add IDs to imported MI fields

---
## [psobolewskiPhD/napari](https://github.com/psobolewskiPhD/napari)@[3ec4be1ae8...](https://github.com/psobolewskiPhD/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Sunday 2023-03-19 19:20:55 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [d3rpp-dev/basic_test](https://github.com/d3rpp-dev/basic_test)@[43d0855ff9...](https://github.com/d3rpp-dev/basic_test/commit/43d0855ff926f9d7a6c9315ec3f46ea4738b8be3)
#### Sunday 2023-03-19 19:42:06 by d3rpp

this course is making me wanna drop out. not only is it boring, but our instructor is asking questions that have millions of possible answers and expects a single word answer in his brain language. this is not how learning programming works and it is why learning it yourself individually is a superiour method since you can understand the concepts using methods your brain understands and all brains are different so the concepts are different.

they say that this course has "world-class" instructors but in reality my highschool teachers were better, at least my high-school computer science teacher understood all of this and mostly let us teach ourselves with guidance where necessary, realistically i think it'd be better if sir followed suit, but hey, im not paying for this, i have nothing to lose.

Thankyou for coming to my TED Talk, I hope you have a lovely day :)

---
## [Thelema-SS/Thelema-STG](https://github.com/Thelema-SS/Thelema-STG)@[635aee8e34...](https://github.com/Thelema-SS/Thelema-STG/commit/635aee8e346a86ee375d262342057554b973e14b)
#### Sunday 2023-03-19 20:05:53 by SkyratBot

[MIRROR] pumping your heart doesnt require to be conscious [MDB IGNORE] (#16540)

* pumping your heart doesnt require to be conscious (#63290)

Simply removes the requirement to be conscious to pump your blood with a cursed heart.
Why It's Good For The Game

Entering crit or falling asleep is basically a life sentence since you are unable to pump your blood while asleep. The player still is manually pumping it, I don't see any reason why the user has to be awake for it.
This also means medical can't revive you, as you'll instantly lose all your blood before you have enough time to wake up to start pumping again. The only IC fix would be to remove your heart entirely, something most doctors wouldn't even notice.
Changelog

cl
fix: You can manually pump your blood while asleep/in crit, rather than instantly lose all your blood and die forever.
/cl

* pumping your heart doesnt require to be conscious

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [ValueOverflow/seedsigner](https://github.com/ValueOverflow/seedsigner)@[d2a657f2d4...](https://github.com/ValueOverflow/seedsigner/commit/d2a657f2d43c6e77e9c48cb1f859e8f4984a5f00)
#### Sunday 2023-03-19 20:14:37 by Marc G

Various edits B4 upstream submission

After a long hiatus, I have finally completed my proposed changes to the software verification section of our readme.

The verification focuses on keybase.io now storing and verifying the 3 online properties (seedsigner.com, twitter.com/seedsigner and github.com/seedsigner)

This makes the key more secure, easier to import and generally less hassle. its also revokable.  

There is more detail about how/why in the expand blocks, but It was suggested to me to keep the instructions straightforward (ie do this and now do that) , so I have reduced focus much on the why. 
However, some basic "why & how" has also been placed in new collapsible sections, at the end of each step. 

Later on, I want to add color to the collapse sections so that they show a natural boundary, but so far that markdown code is elusive to me. ;) 
Done is better than perfect....
The same for getting my external links to open in a new tab/window. sigh. Markdown is ... well....tricky. 

I can make the screenshots smaller. please comment on their size.


The Verification is done in 3 steps:
1. import the public key
2. Verify its the correct key by verying it and then comparing the Key ID to Keybase.io/seedsigner. If it matches, then its the real seedsigner project person that signed.
this is arguablly the most critical step of verifying and hence we ask the user to check for themselves that the key ID from verify is the same as on keybase.io. Hence the Key ID's are blurred in the screenshots. We dont want the user to compare the screenshots to each other. we want them to compare their result to their browser. 

3. Verify that the other files (at this stage just the .zip file) are also not altered. This does a comparision of the various files actual and expected hashes.

If all is well here, then tell the user about their success :). 
Explain the warnings, which ones are benign, and what to do if verification fails.


Lastly, "Write the software to the MicroSD' section - 
I have got draft text for this, but havent published it yet. 
The verify PR is big enough !!

Please review for my PR flow and clarity, I do still want to improve the formatting,  but wanted to get everyone's thoughts before messing with the detailed formatting and line breaks, which are especially painful!

FYI - I have done my screenshots using layers, so it easy to edit in the future. I think they

---
## [mc776/freedoom](https://github.com/mc776/freedoom)@[6ebe395d49...](https://github.com/mc776/freedoom/commit/6ebe395d4900ca1eec60019bedc39911336d2064)
#### Sunday 2023-03-19 20:25:55 by mc776

dehacked: rewrite intermission texts.

Reposting #868 because that was way too many commits.

The current ones have lots of sentence fragments that are somehow austere in tone while still having lots of unnecessary words - a combination that doesn't exactly flow too well. This is an attempt to rewrite a lot of them while trying to keep all the critical elements of each.

A lot of the "it doesn't matter, who cares" / "oh. a trap. AGAIN." talk also felt like it would pull the reader out of the game, however in-character it was clearly intended. (I understand it's inspired by "where's your fat reward and ticket home" from Doom E1 but if you look at all the other id intermission texts things are much more triumphant and hopeful in tone - D2's "There must be a way to close it on the other side. What do you care if you've got to go through Hell to get to it?" is more bravado than despair.)

Replaced some things that create expectations of specific things to be found in the very next map but aren't there - the Map06-7 lift (you start on a teleporter pad), the Map11-12 platform bolts (you start just inside the door), the "massive doors" of the Military Labs (you start on the end teleporter immediately after E1M8), etc..

"Dissipitates" isn't exactly release-quality standard diction.

Some lines were rearranged so that natural sentence and phrase breaks coincide with line breaks - everything has been tested on Chocolate, it seems we do have more room to work with than the previous writers seem to have thought. (If someone out there *specifically intended* to make sure the sentences spill over into the next line in the absence of a paragraph break I'm willing to listen to reasoned argument about it.)

I have, of course, left the iconic final three lines of Phase Two untouched.

---
## [Uncle-PDev/NssienPhilip](https://github.com/Uncle-PDev/NssienPhilip)@[0e3f8f1e73...](https://github.com/Uncle-PDev/NssienPhilip/commit/0e3f8f1e7398b6b9c492b383598c50c25ce4e87b)
#### Sunday 2023-03-19 20:28:46 by Nssienphilip

CONNECT WITH NSSIENPHILIP

# NSSIEN PHILIP

##CONNECT WITH NSSIEN PHILIP.

Hi there! My name is NSSIEN PHILIP, and I'm a Software(WEB) developer with years of 
experience in the industry. I'm passionate about creating high-quality websites that not only look great, but also function flawlessly.

Ever since I was a child, I've been fascinated by technology and how it can be used to 
make our lives easier. As I grew older, I became increasingly interested in programming 
and started tinkering with various languages and frameworks in my spare time. It wasn't long before I realized that web development was my true calling.


Over the years, I've worked on a wide variety of projects, from simple brochure websites
to complex e-commerce platforms. I've honed my skills in HTML, CSS, JavaScript, React and 
other web technologies, and I'm always eager to learn more. I'm particularly interested in
Full-Stack development and user experience design, as I believe that a well-designed website 
can make all the difference in how users interact with a business or organization.

When I started learning web development at a Tech Hub called “AFRICINNOVATE” it was very
interesting and mind boosting. Over the weeks, I became slow and unfocus due to lots of bugs,
and physical issues. But, I had a strong mindset that will always be ready to focus and make sure to archive set out goals. 

When I'm not coding, you can usually find me exploring new hiking trails, gaming or trying out
new recipes in the kitchen. I'm a big believer in work-life balance and strive to maintain a healthy mix of professional and personal pursuits.

#FIND ME HERE!

Twitter: https://twitter.com/Nssienphilip
LinkedIn: https://www.linkedin.com/in/philip-nssien/
Medium: https://medium.com/@Nssienphilip4/

#I did learn and gain so many languages and frameworks.
#SOME OF MY CODE LANGUAGE

##FRONT-END

### REACT
### CSS
### HTML
### JavaScript

##BACK-END
### NODE.js

#OTHER SKILLS OF MINE.
Not just the Software Development space, I have walk on the tech space and have found out that, we have so many others 
aspect that we can gain from. 
I'm also a crypto enthusiast, community Engagée, Shriller etc.
The world of Web3.0 is filled with so many opportunities. It's all left for us to learn and grab.

---
## [Dimasw99/Citadel-Station-13-RP](https://github.com/Dimasw99/Citadel-Station-13-RP)@[9c8abee554...](https://github.com/Dimasw99/Citadel-Station-13-RP/commit/9c8abee5540f17951b1947a212b80521f1b36300)
#### Sunday 2023-03-19 20:30:01 by IrkallaEpsilon

Matterforge Recipe expansion (#5168)

## About The Pull Request

This PR adds a few more matterforge recipes, some of stupidly high
difficulty and pointless rewards if miners are doing their job (looking
at you steel to gold), some of more usefulness (gold to plat, plat to
osmium). All require different temperature and energy ranges so they
cannot be rushed thoroughly. Not much thought was put into realism but
eh who cares, the matterforge is a cool thing ingame and its fun to use.
Some temperatures ranges (Steel to gold) are very narrow hence the use
of a gyrotron would be needed to get the most out of it. Or precise
heating (temperature can be raised to exorbitant amounts to prevent
heater cheese). This also would allow for Research to collab with cargo
for exports specially if dynamic prices ever come. In particular looking
at the gold to plat transmutation here. Plat can be exported by cargo in
which cargo can order more shit from.

I aint a good coder else I would add specific atmospheric conditions
needed, not just temperature (e.g. N2O must be present).
Reminded me a bit of TGs gas reactions but less gamy. 

## Why It's Good For The Game

More Matterforge recipes. Most relatively pointless and niche, some
allow science to give cargo something to sell, others can help with
theres an overabundance of Plat due to new miners. Mostly just giving
some extra uses for the forge. Oh and an alternative way to get plasteel
while sacrificing phoron sheets. Also bragging rights of effectively
turning iron (and carbon) into gold at specific temperatures and energy
levels on the particle focus.

A proper coder should check if these recipes are fine. Its 2:30 AM and I
thought this would just be neat.

## Changelog

:cl:
add: Various matterforge recipes
/:cl:

---
## [Dimasw99/Citadel-Station-13-RP](https://github.com/Dimasw99/Citadel-Station-13-RP)@[b3a43f2b85...](https://github.com/Dimasw99/Citadel-Station-13-RP/commit/b3a43f2b8522c03ca976a1f7e72aa9deea97b350)
#### Sunday 2023-03-19 20:30:01 by IrkallaEpsilon

Buffs Excav Laser Module (#5174)

## About The Pull Request

Buffs Excav laser module. Inconsisten with the one hit of rocks.
Hopefully this ammends it specially since scatterlenses are getting
removed (although nobody used them in combat yet.)

## Why It's Good For The Game

Scatter lense gone, legitimate mining tool needs a buff. The other
options (Phoron Bore) are a sick joke with how slow clunky they are to
use.


## Changelog
:cl:
balance: Meatier sound on excav laser. Higher excav power to
consistently one shot rocks.
/:cl:

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[d261466765...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/d2614667654c0e35b2c906971ca94ece9e7b8629)
#### Sunday 2023-03-19 20:31:57 by IrkallaEpsilon

Scattershot nerfs (#5175)

Sniper laser was tame.

## About The Pull Request

This is bullshit. Splurting out 180 damage with high AP with no delay is
not okay. Its as bullshit as most FCU we had. Mainly removed scatter on
high powered lasers and bloody stuns so the scatter lense may stay for
the mining tool (as there is no way to increase firerate on a
projectile.

## Why It's Good For The Game

Ever got hit at close range by the particle defender on main? Yeah that
is not fun.

## Changelog
:cl:
balance: Scattershot on high powered weapons nerfed. Heavy laser and
laser cannon beam and electrode now wont create submunitions. Stun beam
submunition count lowered.
/:cl:

---
## [vendetta-mod/VendettaTweak](https://github.com/vendetta-mod/VendettaTweak)@[be60d21840...](https://github.com/vendetta-mod/VendettaTweak/commit/be60d218408d0fd4dec27dbfd140ed8a951b3562)
#### Sunday 2023-03-19 21:03:06 by Jack Matthews

[CI] Fuck you Ubuntu

It didn't want to submodule resulting in missing scripts
so goodbye ubuntu

---
## [ryand67/nushell](https://github.com/ryand67/nushell)@[2e01bf9cba...](https://github.com/ryand67/nushell/commit/2e01bf9cbadf833b4156ec5117393e51b8cadc7d)
#### Sunday 2023-03-19 21:54:25 by Bob Hyman

add `dirs` command to std lib (#8368)

# Description

Prototype replacement for `enter`, `n`, `p`, `exit` built-ins
implemented as scripts in standard library.
MVP-level capabilities (rough hack), for feedback please. Not intended
to merge and ship as is.

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes
New command in standard library

```nushell
〉use ~/src/rust/nushell/crates/nu-utils/standard_library/dirs.nu
---------------------------------------------- /home/bobhy ----------------------------------------------
〉help dirs
module dirs.nu -- maintain list of remembered directories + navigate them

todo:
* expand relative to absolute paths (or relative to some prefix?)
* what if user does `cd` by hand?

Module: dirs

Exported commands:
  add (dirs add), drop, next (dirs next), prev (dirs prev), show (dirs show)

This module exports environment.
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs add ~/src/rust/nushell /etc ~/.cargo
-------------------------------------- /home/bobhy/src/rust/nushell --------------------------------------
〉dirs next 2
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │         │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
│ 3 │ ==>     │ ~/.cargo           │
╰───┴─────────┴────────────────────╯
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs drop
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │ ==>     │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
╰───┴─────────┴────────────────────╯
---------------------------------------------- /home/bobhy ----------------------------------------------
〉
```
# Tests + Formatting

Haven't even looked at stdlib `tests.nu` yet.

Other todos:
* address module todos.
* integrate into std lib, rather than as standalone module. Somehow
arrange for `use .../standard_library/std.nu` to load this module
without having to put all the source in `std.nu`?
*  Maybe command should be `std dirs ...`?   
* what else do `enter` and `exit` do that this should do? Then deprecate
those commands.

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
## [pagol-nana/cxvcgdg](https://github.com/pagol-nana/cxvcgdg)@[93f7a913c2...](https://github.com/pagol-nana/cxvcgdg/commit/93f7a913c27535139774413cfa7061bb3eea7b04)
#### Sunday 2023-03-19 22:03:18 by pagol-nana

Update README.md

HALFTIME, Barcelona 1-1 Real Madrid: Barça were by far the better team in the first half and conceded a completely accidental opening goal, but never stopped attacking and got a deserved reward just before halftime. They have the momentum going into the second half, and this one is set up beautifully.

45’ GOAL!!! Barcelona 1-1 Real Madrid (Roberto): BARÇA EQUALIZE!!! A shot from Raphinha is blocked inside the box and the rebound falls to Sergi Roberto who takes a touch and finds the back of the net! A huge goal before halftime!

9’ GOAL, Barcelona 0-1 Real Madrid (Araujo OG): Madrid take the lead. Vinicius Junior attempts a cross into the box that hits Ronald Araujo and goes into the net. A very lucky goal for the visitors.

KICKOFF! Barcelona 0-0 Real Madrid: And we’re underway at Camp Nou!

WELCOME TO THE SPOTIFY CAMP NOU!!! The Greatest Stadium on Earth is the site of the biggest game of Barcelona’s season as the La Liga leaders welcome Real Madrid for the latest edition of El Clásico with everything on the line. Barça can essentially clinch the title with a victory, but Los Blancos can make it a real title race if they get all three points. It’s a truly massive game, and you’re welcome to join us to follow and comment all the action. Vamos!

(Note: the comments will be open only when the team news come out, because our commenter people love commenting and sometimes there are too many comments in the comments section)

LINEUPS
BARCELONA

Starting XI: Ter Stegen; Araujo, Kounde, Christensen, Balde; Roberto, Busquets, De Jong; Raphinha, Lewandowski, Gavi (4-3-3)

Substitutes: Peña (GK), Tenas (GK), Eric, Alonso, Alba, Kessie, Torre, Fati, Ferran, Alarcón

REAL MADRID

Starting XI: Courtois; Carvajal, Militão, Rüdiger, Nacho; Modric, Camavinga, Kroos; Valverde, Benzema, Vinicius (4-3-3)

Substitutes: Lunin (GK), López (GK), Vallejo, Mendy, Odriozola, Vázquez, Tchouaméni, Ceballos, Asensio, Rodrygo, Hazard, Mariano

MATCH INFO
Competition/Round: 2022-23 La Liga, Matchday 26

Date/Time: Sunday, March 19, 2023, 9pm CET/WAT (Barcelona & Nigeria), 8pm GMT (UK), 4pm ET, 1pm PT (USA), 1.30am IST (India, Monday)

Venue: Spotify Camp Nou, Barcelona, Catalonia, Spain

Referee: Ricardo De Burgos Bengoechea

VAR: César Soto Grado

HOW TO WATCH
On TV: ESPN Deportes (USA), Not Available (Canada), Viaplay Sports 1 (UK), SuperSport (Nigeria), Sports18 (India), Movistar LaLiga (Spain), others

Online: ESPN+ (USA), LaLigaTV (UK), Movistar+ (Spain), others

Matchday Thread Rules
We don’t have a lot of rules here, but there are a few things to keep in mind when joining our matchday threads:

Even if the referee sucks or we lose the game, watch the swearing. It’s just unnecessary. Also, don’t discuss illegal streaming links. Those who do it will be warned, and those who post links will be instantly banned. Finally, be nice to each other. This is a Barcelona community and we don’t need to offend one another.

Have fun with the game! Forever and ever, no matter the competition, VISCA EL BARÇA!

MORE FROM BARCA BLAUGRANES
Puyol praises Ronald Araujo ahead of El Clasico
FC Barcelona News: 19 March 2023
Barça squad named for El Clásico
El Clásico: Preview
Xavi talks Araujo, Pedri and Raphinha ahead of El Clasico
Barca willing to sell Dembélé and Torres to get Chiesa - report

MOST READ
Barça squad named for El Clásico
El Clásico: Preview
FC Barcelona News: 19 March 2023
Xavi talks Araujo, Pedri and Raphinha ahead of El Clasico
Barca willing to sell Dembélé and Torres to get Chiesa - report

Sponsored Content
Former Manchester United Star Paul Scholes Is Selling His 7-Bedroom Gated Compound
Former Manchester United Star Paul Scholes Is Selling His 7-Bedroom Gated Compound
Mansion Global
Actor Sylvester Stallone Selling La Quinta, California, Villa at a Loss
Actor Sylvester Stallone Selling La Quinta, California, Villa at a Loss
Mansion Global
Incredible: seniors are snapping up this new toothbrush, here's the reason!
Incredible: seniors are snapping up this new toothbrush, here's the reason!
Teeth Care
20 Iconic Songs No Longer Allowed On The Radio
20 Iconic Songs No Longer Allowed On The Radio
Bleacher Breaker
[Photos] He Was A NBA Legend, Now He's Working 9 To 5
[Photos] He Was A NBA Legend, Now He's Working 9 To 5
Gameday News
Bangladesh Price Of Solar Panels: See How Much It Will Cost To Install Them (See Deals)
Bangladesh Price Of Solar Panels: See How Much It Will Cost To Install Them (See Deals)
Search Ads
Loading comments...
Sign up for the newsletterSign up for the Barca

---
## [juno-r1/sophia](https://github.com/juno-r1/sophia)@[29babc1597...](https://github.com/juno-r1/sophia/commit/29babc15975724fba3d034d9befb4da7b172a051)
#### Sunday 2023-03-19 23:58:57 by juno-r1

implemented user-defined types. god this fucking sucked

---

