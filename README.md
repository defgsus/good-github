## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-06-08](docs/good-messages/2023/2023-06-08.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,155,570 were push events containing 3,429,266 commit messages that amount to 255,890,022 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 65 messages:


## [sailfishos-mirror/protobuf](https://github.com/sailfishos-mirror/protobuf)@[efa1ec75cf...](https://github.com/sailfishos-mirror/protobuf/commit/efa1ec75cf152991a64cedf9c4a1ec5cb826ee34)
#### Thursday 2023-06-08 00:13:53 by Romain Geissler @ Amadeus

Use the same ABI for static and shared libraries on non-Windows platforms (#12983)

Hi,

It seems that until last year, the logic behind `PROTOBUF_USE_DLLS` was for Windows (MSCV) only. It was changed to all platforms here in https://github.com/protocolbuffers/protobuf/commit/5a0887fc6529596eff5c0f72febc602a9d494cc2

Last month, the generated pkg config files were updated to reflect the protobuf build-time value of `PROTOBUF_USE_DLLS` as it was indeed noted that it changes the ABI. This was done in https://github.com/protocolbuffers/protobuf/pull/12700 In the commit message it is mentionned that most likely we shall rather have a stable ABI.

Finally in https://github.com/protocolbuffers/protobuf/issues/12746 which at some point mentions https://issuetracker.google.com/issues/283987730#comment7 where a Google employee hits the linker issue:
```
undefined reference to `google::protobuf::internal::ThreadSafeArena::thread_cache_'
```
which denotes a mix of some .o or libs built `PROTOBUF_USE_DLLS` defined and some others build with `PROTOBUF_USE_DLLS` undefined, resulting in ABI incompatibilities.

I also hit this issue while trying to include protobuf in a corporate environment using it's own proprietary build system in which it is expected that .a and .so use a compatible ABI.

From my own understanding, ideally we should always use `thread_local` variables, but experience has shown that:
 - old iOS (iOS < 9) didn't seem to accept `thread_local`, leading to the `GOOGLE_PROTOBUF_NO_THREADLOCAL` macro later renamed `PROTOBUF_NO_THREADLOCAL` which allowed to disable this, but it is not set anywhere in the protobuf code base. Also I doubt you still want to support such old iOS now, so maybe you should consider removing all `PROTOBUF_NO_THREADLOCAL` related code paths (this pull request doesn't do this).
  - MSVC's DLL interface doesn't seem to accept exporting thread local variables (at least from what I understood, I know absolutely nothing about the Windows ecosystem), yet we can "hide" a thread local variable in a static function using a thread local variable. However in that case the access to TLS variable is not inlined, leading to worse performances, this hack shall be done only for Windows (actually when using MSVC) *AND* we build a shared library.
  - In all other cases, a classical `thread_local` shall be used, no matter if we build a static or a shared library. In particular on Linux which I guess is the target Google cares the more about for its own production. This pull request achieves this.

Am I right in my conclusion ?

Closes #12983

COPYBARA_INTEGRATE_REVIEW=https://github.com/protocolbuffers/protobuf/pull/12983 from Romain-Geissler-1A:stable-abi-use-dll-non-windows dc23ff50f67cf0c8e45900a78700d1fc3e8bec39
PiperOrigin-RevId: 538230923

---
## [DS-13-Dev-Team/DS13-2.0](https://github.com/DS-13-Dev-Team/DS13-2.0)@[159d2aeebe...](https://github.com/DS-13-Dev-Team/DS13-2.0/commit/159d2aeebee7ef681891019d52069bf898846e03)
#### Thursday 2023-06-08 00:44:00 by Gallyus

Reagent Description and Abstract Changes (#164)

* Reagent Description and Abstract Changes...
Abstract reagents are no longer detected via a magic list.
Added a description to non-abstract reagents that were missing them.
Adds a unit test to detect non-abstract reagents missing a description.

As a consequence:
Some reagents have disappeared from lists for being abstract.
Instantiating an abstract reagent is illegal and crashes New().

* Minor fixes
It's 3am go fuck yourself.

* Apply suggestions from code review

* Allows access to a new ANSI color

* C&D creates a notice on start for logging purposes

---
## [DS-13-Dev-Team/DS13-2.0](https://github.com/DS-13-Dev-Team/DS13-2.0)@[a3eb90b950...](https://github.com/DS-13-Dev-Team/DS13-2.0/commit/a3eb90b9504f6a21c2636a4bb8aeb8b40eb66861)
#### Thursday 2023-06-08 00:44:00 by Gallyus

Fix Pack 3: Revenge Of The Fuck (#225)

* Various Jaunt fixes (#70431)

* Jaunt code path reworked so that traits and other effects can be removed consistently regardless of how effect is ended.
Jaunts will more consistently clean themselves up (and unjaunt you) when you lose the spell.
If a shuttle lands on you while you are jaunted it will now kill you instead of crashing and fucking with the shuttle landing process.
Z travelling while inside an object or mob will now relay that direction instead, allowing you to jaunt up and down as well as cardinally.
Mirror walk button updates at correct times.
Blood and Shadow walk buttons have same functionality as Mirror Walk.

* Fixes Soul Scythe being able to get to Centcom by moving down on the bottom Z-level (#71171)

## About The Pull Request

`/obj/item/soulscythe/relaymove()` was using `get_step()` which doesn't
understand our multi-z system and was happily trying to move Z - 1 which
is Centcom. I'm still not really sure I understand why move() allowed
the scythe to just move right through the floor in this case, I think
moving to turfs with `density = 0` is also behaving strangely and just
skipping some checks that should keep it from moving through the floor,
but to be honest I don't fully understand the move chain and just
changing to `get_step_multiz()` at least keeps the scythe from going to
Z-levels it shouldn't.
## Why It's Good For The Game

Whilst it is fun for the scythe to go on an adventure to forbidden
Z-levels, admins probably don't appreciate these adventures so much.
## Changelog
:cl: VexingRaven
fix: Soul Scythes can no longer phase through the floor into Centcom.
/:cl:

* Fixes multi-Z ruins (Ice Moon Mining Site) not spawning (#70097)

* Fixes multi-z ruins not spawning

* I should proably commit said changelog files.

* Proc Ref wrapping

* Update to the correct procs

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: VexingRaven <msgerbs@users.noreply.github.com>

---
## [YakumoChen/Skyrat-tg](https://github.com/YakumoChen/Skyrat-tg)@[7dad8c75ca...](https://github.com/YakumoChen/Skyrat-tg/commit/7dad8c75cac06a405dc3c30a5cbc31919f33ff13)
#### Thursday 2023-06-08 00:53:03 by SkyratBot

[MIRROR] Adds a eye-dropper right-click function to the painting canvas. [MDB IGNORE] (#21411)

* Adds a eye-dropper right-click function to the painting canvas. (#75571)

## About The Pull Request
Having used the painting UI to kill some time during long rounds for a
decent chunk of the past year, the need of a quicker and less tedious
way to fix a misclick or mistake like drawing over the wrong pixel has
become clear to me, as well as getting some feedback on the palette
component I made last year.

As the title suggests, this PR adds an eye-dropper function to the
canvas. Right-Click a pixel on the canvas, and the painting tool will
copy its color. Simple as, works on both finished and unfinished
paintings.

As a bonus, you can also right-click one of those selectable
white/colored squares on the color scheme near the bottom of the UI (if
using spraycan/palette) to change its color without having to go back to
main game window and a radial menu.

EDIT: With the tooltip added to the UI, I can say it's ready.

## Why It's Good For The Game
This PR aims to add better options to change colors on the go and
improve the user experience on the painting UI.

## Changelog

:cl:
qol: Adds a eye-dropper-like right-click function to the painting canvas
UI. Right-Click a pixel on the canvas while holding a painting tool to
have it copy its color.
qol: Also adds a right-click function to the color palette at the bottom
of the UI to allow users to set its colors without having to alternate
between the game window and the UI.
qol: Lastly, a tooltip has been added near the top-left corner of the
same UI to let players know of these features.
/:cl:

* Adds a eye-dropper right-click function to the painting canvas.

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[e4ece2fbd6...](https://github.com/Pickle-Coding/tgstation/commit/e4ece2fbd62dfa6a1270ce37e31fe93bd1823c07)
#### Thursday 2023-06-08 00:54:01 by Hatterhat

makes snow legions from portals drop skeletons (like tendril legions) (#75707)

## About The Pull Request
Exactly what it says on the tin (snow legions only dropping ashen
skeletons, like tendril legions).

Also changes the name of the "fromtendril" variable to "from_spawner",
and comments it. Not sure if that warrants a changelong comment, but
I'll go ahead and assume no.

## Why It's Good For The Game
being able to farm snow legion portals for an endless tide of bodies
and/or equipment is a bit weird. also puts it a bit more in line with
the legions of Lavaland

## Changelog

:cl:
balance: The source of the demonic portals that endlessly deposits snow
legions onto the Icemoon no longer preserves the bodies nor gear of the
damned (read: demon portal snow legions now only drop skeletons).
/:cl:

---------

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[0cff53fc09...](https://github.com/Bjarl/Shiptest/commit/0cff53fc09c34d989d2bc34b1699bd856af2cb92)
#### Thursday 2023-06-08 01:48:12 by meemofcourse

Reworks the Twinkleshine-Class (#1825)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request


![2023 05 13-23 20
45](https://github.com/shiptest-ss13/Shiptest/assets/75212565/de6f3a47-7be8-4800-ae73-9fc386e4bf01)

![twinklerework5](https://github.com/shiptest-ss13/Shiptest/assets/75212565/f1808576-70e3-4b56-b977-5b5e7d665fdd)





The Twinkleshine is a CyberSun-made Syndicate display of force, staffed
by every branch of the Syndicate. Despite the silly name, the presence
of one in a sector implies it to be of importance to the Syndicate, and
enemies within sight can only pray that the Twinkleshine crew are
incompetent enough to shoot themselves with their own weaponry (or blow
themselves up with the supermatter on-board).

It is staffed by:

- 1 Captain
- 1 Lieutenant (previously the Operative - serves as a warden/hos)
- 2 Medics
- 2 Engineers (previously the Mechanics)
- 5 Operatives (previously the Troopers)
- 1 Bartender
- 1 Miner
- 2 Deck Assistants

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Few days ago, an admin spawned a Twinkleshine, and I got to captain it.
The Twinkleshine is old. It sucks. This, hopefully, fixes that.

Originally, this was going to be minor fixes, but ended up becoming an
attempt at reworking the ship to a more modern state - the hull has been
redone and is mostly symmetrical, the old spacepod was replaced with a
Dark Gygax, the supermatter shouldn't be activated upon spawning the
ship, there's more turf decals and a bigger lot-of-things, added a
bartender and a miner, people can actually tell who they are and what
they do, and there is now a box moth. Rejoice.

Also, this is the first time I've ever mapped a ship. What better way to
begin with a giant battleship?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
tweak: Reworks the Twinkleshine
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: meemofcourse <75212565+meemofcourse@users.noreply.github.com>

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[d4b5a598e2...](https://github.com/Bjarl/Shiptest/commit/d4b5a598e2346bb3f69d533ed05a94d539e8b830)
#### Thursday 2023-06-08 01:48:12 by Bjarl

Sand Survivor Rework (#1940)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Reworks how Sand Survivors spawn their loot. Instead of an outfit datum,
they now create a corpse similiarly to how legions do it, this allows
their contents to have some variety, more ease of expansion, and
generally Improves the file.

How I could write better code in a day than White Sands functioned with
for iunno how long is byond me


https://user-images.githubusercontent.com/94164348/236322169-c303f934-634f-447d-950f-78a55346d152.mp4

![image](https://user-images.githubusercontent.com/94164348/236376947-6e484ed0-f136-4787-9e74-fad0f5c21d11.png)

![image](https://user-images.githubusercontent.com/94164348/236377018-e2dc1661-fe78-4c6a-8be2-8bf24e5d00b2.png)


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Consistency + Just kinda cool
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Sand Planet hermits now have randomized inventories. And Hair.
Sometimes.
add: Sand Planet hermits can now drop different races
add: legions will now drop a variety of species
balance: drop rates for legions have been changed in a few spots.
fix: hivelord.dm no longer sears my eyes out.
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
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[c20b961685...](https://github.com/Bjarl/Shiptest/commit/c20b961685c78760ab807c95a2e79fe72ee4d507)
#### Thursday 2023-06-08 01:57:09 by thgvr

Elementizes and Greyscales blood decals/overlays (#1882)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR converts our blood decals to elements, and adds greyscale
capability to blood, tied to species DNA.
Ports:
https://github.com/BeeStation/BeeStation-Hornet/pull/3111
https://github.com/BeeStation/BeeStation-Hornet/pull/3046
https://github.com/tgstation/tgstation/pull/61610
https://github.com/tgstation/tgstation/pull/59873
https://github.com/tgstation/tgstation/pull/59315
https://github.com/tgstation/tgstation/pull/53109

Some others, I don't quite remember. Mostly related fixes for those PRs.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Decals as a component is a cause of some lag, apparently. This should
alleviate some if it's even noticeable.

Species having a framework for unique, greyscale blood colors can add a
lot for our lore and visual feel.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Elzu now bleed, but do not have Liquid Electricity reagent as
blood. (will be changed in the future)
add: IPCs now "bleed" by leaking coolant
add: Sarathi now have teal-colored blood.
add: Blood will now dry over time
add: New bloody footprint sprites from bay
refactor: Refactors a lot of blood code
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: thgvr <81882910+thgvr@users.noreply.github.com>
Co-authored-by: Mark Suckerberg <mark@suckerberg.gay>

---
## [Jiingy/Jineric-Mod](https://github.com/Jiingy/Jineric-Mod)@[7787c69653...](https://github.com/Jiingy/Jineric-Mod/commit/7787c6965373d946676d916bc1fea84493889fb5)
#### Thursday 2023-06-08 03:07:18 by Eric

Merge pull request #99 from Jiingy/1.19.4

fuck you mr cheeze (fixed refinery recipe book categories / added fabric asm)

---
## [feldera/dbsp](https://github.com/feldera/dbsp)@[bace627dc8...](https://github.com/feldera/dbsp/commit/bace627dc869a221492c8d4159b240b43627bc5d)
#### Thursday 2023-06-08 03:10:03 by Chase Wilson

Added `@dbsp.sql.round()` function to implement SQL `ROUND()`

Adds two different implementations, determined by
`CodegenConfig.string_based_round_function`.
When `string_based_round_function` is true it uses the string-based
"rounding" function, which formats the string to the given number of
places and then parses that string back into a float. This is known
to be flawed, but so is the premise of the function in the first place.
When `string_based_round_function` is false (the default) it uses native
operations to try and round the float to the given number of decimal
places, but this is also a best-effort. I implemented a pretty simple
algorithm roughly equivalent to `nearest(x * (10 ** digits)) / (10 ** digits)`
but some of the other code I've seen does a *way* more complicated song
and dance, some of it concerned with error handling which we should be
able to do statically within the compiler. Neither of the implementations
handle the negative case of `ROUND()`, which should be an entirely different
function and be not the world's sketchiest function overload by using
the fucking sign bit to determine what it should do.

With the explanation aside, let's talk about `ROUND()`. Fuck `ROUND()`.
This piece of shit function shouldn't exist, and here's why: It doesn't
make sense. Neither of the "modes" `ROUND()` operates in (we'll call them
integer mode and fractional mode depending on which part of the number it
rounds) are expressible in floating point operations. Like *sure*, they're
"""technically""" representable, but the error is terrible and makes things
get really wacky on the edge cases. What's more is that the error is
dependent on the number of decimal places you round to, yippie! Running
Herbie on the various equations lets us make this neat little error table
(this is only testing fractional mode since I've yet to implement integer
mode, the limit of 13 is what I saw used as an upper bound in other
implementations, quick shout out to [Herbie](https://herbie.uwplse.org)
for helping with this)

| places | bits of error |
| :----- | :-----------: |
| 1      |      0.2      |
| 2      |      0.3      |
| 3      |      0.4      |
| 4      |      0.5      |
| 5      |      0.6      |
| 6      |      0.7      |
| 7      |      0.8      |
| 8      |      0.9      |
| 9      |      1.0      |
| 10     |      1.1      |
| 11     |      1.3      |
| 12     |      1.3      |
| 13     |      1.4      |

That's an egregious amount of error, C and C++ specify all operations to
be within 0.5 ULP which means that rounding a float to 13 digits is almost
THREE TIMES THAT LIMIT. This is utterly nuts, and `ROUND()` should never
be used for anything important, ever. Even rust's native implementation
of factional rounding (via `format!("{float:.1}")`) is broken in seemingly
obvious cases since FLOATS DON'T WORK LIKE THIS

```
// Fractional rounding via `std::format!("{float:.places$}")` in Rust 1.70.0
println!("{:.1}", 0.15);  // 0.1
println!("{:.1}", 0.25);  // 0.2
println!("{:.1}", 0.35);  // 0.3
println!("{:.1}", 0.45);  // 0.5
println!("{:.2}", 0.115); // 0.12
println!("{:.2}", 0.125); // 0.12
println!("{:.2}", 0.135); // 0.14
println!("{:.2}", 0.145); // 0.14
```

And what's even better is that this already weird, wrong and convoluted
function gets even worse since there's actually a THIRD parameter to
`ROUND()` which makes the function round the float when it's set to zero
(which it is by default) and which makes the function TRUNCATE the float
when it's non-zero. C called, it wants its bootleg booleans back. Why in
the hell does the **ROUND** function **TRUNCATE** things?! Why does it
take an integer which is treated like a boolean? Who thought this was a
good idea? Why is truncating a float to the given number of decimal places
also impossible to express in floating point operations? Is all of computing
precariously balanced on top of incredibly janky and unreliable systems
that are so deeply rooted that it's near-impossible to free ourselves of
the terrible restrictions and paradigms of thought that are required to
work around the veritable minefield that you have to navigate just to
function? Who cares, if all this shit burns down I'm dead anyways.

---
## [newstools/2023-new-york-post](https://github.com/newstools/2023-new-york-post)@[0ee06e7ed3...](https://github.com/newstools/2023-new-york-post/commit/0ee06e7ed3fd4c055a6bc9c5f3f8dfca97733d7d)
#### Thursday 2023-06-08 03:11:06 by Billy Einkamerer

Created Text For URL [nypost.com/2023/06/07/my-boyfriend-cheated-on-me-with-his-mom-is-his-name-oedipus/]

---
## [SmoSmoSmoSmok/tgstation](https://github.com/SmoSmoSmoSmok/tgstation)@[f7a49c4068...](https://github.com/SmoSmoSmoSmok/tgstation/commit/f7a49c4068f1277e6857baf0892d355f1c055974)
#### Thursday 2023-06-08 03:39:11 by Ryll Ryll

Gunpoints now take half a second to activate, make gasp sounds, and briefly immobilize the shooter and target, other small balance changes (#74036)

## About The Pull Request
This PR messes around with gunpoints a bit, with the purpose of making
them more viable in certain scenarios without making them obnoxious. The
biggest change is that gunpoints now require a 0.5 second do_after()
where neither the shooter nor the target moves, and immobilizes both of
them for 0.75 seconds if point blank, or half that if you're 2 tiles
away. Originally you were supposed to only be able to initiate a
gunpoint from point-blank, but #56601 seems to have removed that
requirement, so we'll run with it and just leave it as advantageous to
gunpoint closer up. The do_after() reinforces that it should be used as
an ambush tactic, and so you can't use it on someone who's actively
fleeing or fighting you.

Getting held up will now make you emit a shocked gasp sound, a la Metal
Gear Solid, which combined with the short immobilize will hopefully make
it more noticeable that someone's pointing a gun at you.

Holdups will now immediately give a 25% bonus to damage and wounds,
instead of having to wait 2.5 seconds to hit the double damage stage.

Finally, right clicking someone that you're holding up will no longer
shoot them. That just feels like good consistency.

## Why It's Good For The Game
Hopefully makes gunpoints a little more viable for when you want to
stick someone who's not expecting it up without them immediately jetting
off. In the future I'd like to ape Baycode and let the gunman have an
action that toggles whether the victim is allowed to move, so you can
order them to move to a second location without instantly shooting them,
but that'll come later.
## Changelog
:cl: Ryll/Shaps
balance: Holding someone at gunpoint now requires both the shooter and
the victim to hold still for half a second before activating, so you
can't hold-up people fleeing or fighting you. After that, it will
briefly immobilize the both of you, 0.75 seconds if adjacent, or half
that if you're two tiles away. Nuke ops are immune to the
immobilization, since they're ready to die anyways.
balance: Holding someone up will immediately apply a 1.25x damage and
wound multiplier, rather than waiting 2.5 seconds to hit 2x.
soundadd: Being held up will now make the victim play a sharp gasp
sound, a la Metal Gear Solid.
qol: Trying to hold someone up that you're already holding up will no
longer shoot them.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [BrokerBrain/evals](https://github.com/BrokerBrain/evals)@[93fa8a55e9...](https://github.com/BrokerBrain/evals/commit/93fa8a55e9113ebf221347af731b9a5fb6400512)
#### Thursday 2023-06-08 03:51:26 by Austin Starnes

Add logic grid puzzle eval (#830)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
`logic-grid`

### Eval description

The model is prompted with a logic grid word problem with a list of
hints, categories, and values for the category. The model is then asked
to provide a solution, showing reasoning, in a set of Python tuples that
show the matched category values.

<details>
  <summary>See human-friendly example prompt</summary>

```
Using the hints and information provided, solve the following logic grid puzzle.
Show your reasoning concisely, but step-by-step, to arrive at your final answer.
Remember, since this is a grid-based puzzle, each option in every category will be used exactly once.
Since there are 4 values per category, and 3 categories, your final answer will include 4 tuples each of length 3.
 Puzzle Scenario:
A number of new space probes were launched this year. Using only the clues that follow, match each probe to the month it launched and its eventual destination.

Category Options:
  Probes: "Nalini", "Hikaru", "Sarika", and "Sven"
  Destinations: "Ganymede", "Titan", "Enceladus", and "Phobos"
  Months: "January", "February", "March", and "April"

Hints:
  1: The Hikaru launched 2 months before the Nalini.
  2: The probe going to Phobos launched sometime after the Hikaru.
  3: The Sven launched 2 months before the mission going to Ganymede.
  4: Of the probe that launched in April and the mission going to Titan, one is the Sarika and the other is the Nalini.

In your response, format your final answer for each set of linked category values as a python tuple of strings in this order:
("Enceladus", [value from months], [value from probes])
("Ganymede", [value from months], [value from probes])
("Phobos", [value from months], [value from probes])
("Titan", [value from months], [value from probes])
```
</details>

<details>
  <summary>See expected/ideal answer</summary>

```
("Enceladus", "January", "Hikaru")
("Ganymede", "April", "Sarika")
("Phobos", "February", "Sven")
("Titan", "March", "Nalini")
```
</details>

<details>
<summary>See failure case from GPT-4 (at least from the web UI - I don't
have API access to GPT-4)</summary>

```
Step 1: From Hint 3, we know that Hikaru launched 2 months before Nalini. Since the latest month available is April, this means that Nalini cannot have launched in April because there wouldn't be a 2-month gap for Hikaru. So, Nalini must be the probe going to Titan (from Hint 4), and Sarika must be the probe that launched in April.

Step 2: Since Nalini is going to Titan, from Hint 4, it must have launched in February to allow Hikaru to launch in December (2 months before). However, December is not an option, so Hikaru must have launched in January (the earliest month possible) and Nalini in March.

Step 3: The Sven launched 2 months before the mission going to Ganymede (Hint 2). Since Sven cannot be launched in January (as Hikaru is launched in January), it must have launched in February. That means the mission to Ganymede must be in April.

Step 4: The only remaining month is March, and the only remaining probe is Nalini. So Nalini was launched in March.

Step 5: The probe going to Phobos launched sometime after Hikaru (Hint 1). Since Hikaru launched in January, the only remaining option for Phobos is Sarika, which launched in April.

Step 6: The only remaining destination is Enceladus, and the only remaining probe is Hikaru, so Hikaru is going to Enceladus.

The final answer is:
("Enceladus", "January", "Hikaru")
("Ganymede", "April", "Sven")
("Phobos", "April", "Sarika")
("Titan", "March", "Nalini")
```
</details>

### What makes this a useful eval?

This set of evals relies on a lot of *context-ramping* (as I call it)
for LLMs to get right - relying on chain-of-thought style logic to
'ramp' into the most likely next-deduction for a multi-parameter logical
problem.
These prompts are written as word problems and don't rely on any ASCII
or markdown type of table to express the puzzle (though `gpt-3.5-turbo`
appears to use markdown tables in it's chain of thought).

This ramping gets expensive and doesn't scale well with the increase of
category or values-per-category parameters, and is something that LLMs
might benefit from avoiding (either by requiring less of a context-ramp
to get to the meat of an answer, or by the surrounding
infrastructure/problem agent that tries to use a cheaper ensemble for
most of the context ramping, or other strategies).

The reasoning skills required for this kind of <b>constraint
satisfaction</b> expressed in natural language word prompts can, in
theory, generalize to solving constraints expressed in less structured
formats in the wild.

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
- [X] <span title="A GPT-4 failure case from the eval set is included
above.">Contains failures where a human can do the task, but either
GPT-4 or GPT-3.5-Turbo could not.</span>
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [X] **<span title="15 examples per grid size are included, for 6
different grid sizes, make a total of 90 included examples.">Include at
least 15 high quality examples.</span>**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval contains varied prompts and grid sizes, 15 examples per grid
size, for a total of 90 procedurally generated puzzles.
~This PR also implements (disabled by default) multiline answers and
punctuation whitelisting behavior in `FuzzyMatch`, which was required
due to the structural nature of the logic grid answers and the behavior
of `utils.normalize(...)` which (prior to this PR) did not provide any
functionality to interpret answers that span across newline characters
`\n` or preserve punctuation where it may be useful (in this case, the
model is prompted for the resultant grid associations in python tuple
format, so the punctuation in `(",)` is configured to be preserved for
these evals).
The new functionality is, again, disabled by default, such that existing
evals are not affected.~

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
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
- [X] (Ignore if not submitting code) I have run `pip install
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
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nA number of new
space probes were launched this year. Using only the clues that follow,
match each probe to the month it launched and its eventual
destination.\n\nCategory Options:\n Probes: \"Nalini\", \"Hikaru\",
\"Sarika\", and \"Sven\"\n Destinations: \"Ganymede\", \"Titan\",
\"Enceladus\", and \"Phobos\"\n Months: \"January\", \"February\",
\"March\", and \"April\"\n\nHints:\n 1: The Hikaru launched 2 months
before the Nalini.\n 2: The probe going to Phobos launched sometime
after the Hikaru.\n 3: The Sven launched 2 months before the mission
going to Ganymede.\n 4: Of the probe that launched in April and the
mission going to Titan, one is the Sarika and the other is the
Nalini.\n\nIn your response, format your final answer for each set of
linked category values as a python tuple of strings in this
order:\n(\"Enceladus\", [value from months], [value from
probes])\n(\"Ganymede\", [value from months], [value from
probes])\n(\"Phobos\", [value from months], [value from
probes])\n(\"Titan\", [value from months], [value from
probes])"}],"ideal":"(\"Enceladus\", \"January\",
\"Hikaru\")\n(\"Ganymede\", \"April\", \"Sarika\")\n(\"Phobos\",
\"February\", \"Sven\")\n(\"Titan\", \"March\", \"Nalini\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nThe Monterey Bay
Aquarium has a new exhibit featuring several dolphin skeletons. The
aquarium asked local elementary school children to name each dolphin and
match it to its species, length, and the year in which it was donated to
the aquarium. Use the given clues to solve the puzzle.\n\nCategory
Options:\n Dolphin: \"Atlantic white-sided dolphin\", \"Pacific
white-sided dolphin\", \"common dolphin\", and \"bottlenose dolphin\"\n
Names: \"Momo\", \"Simon\", \"Tychus\", and \"Marlo\"\n Lengths: \"21
ft\", \"23 ft\", \"25 ft\", and \"27 ft\"\n\nHints:\n 1: Momo is 4 feet
shorter than Tychus.\n 2: The common dolphin is somewhat shorter than
the bottlenose dolphin.\n 3: The 21 ft long exhibit is either the
Atlantic white-sided dolphin or Simon.\n 4: Marlo is either the 23 ft
long exhibit or the Atlantic white-sided dolphin.\n 5: Of Simon and the
Pacific white-sided dolphin, one is 27 ft long and the other is 21 ft
long.\n\nIn your response, format your final answer for each set of
linked category values as a python tuple of strings in this
order:\n(\"Atlantic white-sided dolphin\", [value from lengths], [value
from names])\n(\"Pacific white-sided dolphin\", [value from lengths],
[value from names])\n(\"bottlenose dolphin\", [value from lengths],
[value from names])\n(\"common dolphin\", [value from lengths], [value
from names])"}],"ideal":"(\"Atlantic white-sided dolphin\", \"25 ft\",
\"Marlo\")\n(\"Pacific white-sided dolphin\", \"27 ft\",
\"Tychus\")\n(\"bottlenose dolphin\", \"23 ft\", \"Momo\")\n(\"common
dolphin\", \"21 ft\", \"Simon\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nHillcrest County
Hospital released a press release today to announce its annual list of
the first babies born immediately after the start of the new year. Using
only the clues below, match each baby to its family time of birth, and
determine the room number in which it was delivered.\n\nCategory
Options:\n Names: \"Lydia\", \"Naomi\", \"Katherine\", and \"Rebecca\"\n
Families: \"McIntyre\", \"Gonzalez\", \"Hudson\", and \"O'Connor\"\n
Times: \"12:01am\", \"12:04am\", \"12:07am\", and
\"12:10am\"\n\nHints:\n 1: Naomi was born 3 minutes after Rebecca.\n 2:
The Hudsons' child was born 6 minutes after the O'Connors' child.\n 3:
The baby born at 12:04am was either Rebecca or the McIntyres' child.\n
4: Of Katherine and the baby born at 12:01am, one was the O'Connors' and
the other was the Gonzalezes'.\n\nIn your response, format your final
answer for each set of linked category values as a python tuple of
strings in this order:\n(\"Gonzalez\", [value from names], [value from
times])\n(\"Hudson\", [value from names], [value from
times])\n(\"McIntyre\", [value from names], [value from
times])\n(\"O'Connor\", [value from names], [value from
times])"}],"ideal":"(\"Gonzalez\", \"Katherine\",
\"12:10am\")\n(\"Hudson\", \"Lydia\", \"12:07am\")\n(\"McIntyre\",
\"Naomi\", \"12:04am\")\n(\"O'Connor\", \"Rebecca\", \"12:01am\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nMedisynth
Therapeutics has spent decades scouring the world's rainforests for new
sources of medical drugs, and this year a number of these new drugs have
been officially approved by the FDA. Using only the clues below, match
each drug to the condition it treats, the month it was approved, and the
source from which its main ingredient is derived.\n\nCategory Options:\n
Drugs: \"Mystolam\", \"Soludox\", \"Aurexil\", and \"Synodil\"\n
Conditions: \"rheumatism\", \"chikungunya\", \"hyperglycemia\", and
\"encephalitis\"\n Months: \"January\", \"February\", \"March\", and
\"April\"\n\nHints:\n 1: The medicine that treats hyperglycemia was
approved sometime after Synodil.\n 2: The medicine that treats
hyperglycemia was approved 1 month before the medicine that treats
rheumatism.\n 3: Of Mystolam and the pharmaceutical approved in April,
one treats rheumatism and the other treats encephalitis.\n 4: Of the
Aurexil approved in February and the drug that treats chikungunya, one
is Soludox and the other is Synodil.\n\nIn your response, format your
final answer for each set of linked category values as a python tuple of
strings in this order:\n(\"chikungunya\", [value from drugs], [value
from months])\n(\"encephalitis\", [value from drugs], [value from
months])\n(\"hyperglycemia\", [value from drugs], [value from
months])\n(\"rheumatism\", [value from drugs], [value from
months])"}],"ideal":"(\"chikungunya\", \"Synodil\",
\"January\")\n(\"encephalitis\", \"Soludox\",
\"April\")\n(\"hyperglycemia\", \"Aurexil\",
\"February\")\n(\"rheumatism\", \"Mystolam\", \"March\")"}
{"input":[{"role":"system","content":"Using the hints and information
provided, solve the following logic grid puzzle.\nShow your reasoning
concisely, but step-by-step, to arrive at your final answer.\nRemember,
since this is a grid-based puzzle, each option in every category will be
used exactly once.\nSince there are 4 values per category, and 3
categories, your final answer will include 4 tuples each of length
3.\n"},{"role":"system","content":"Puzzle Scenario:\nA group of friends
has gotten together for dinner, and just for fun they're comparing their
\"social networking\" stats on Facebook, Twitter and LinkedIn. Using
only the clues that follow, determine the number of friends (Facebook),
followers (Twitter) and connections (LinkedIn) each person
has.\n\nCategory Options:\n Names: \"Avery\", \"Evan\", \"Natalia\", and
\"Camila\"\n Linkedin: \"54\", \"59\", \"64\", and \"68\"\n Facebook:
\"120\", \"130\", \"140\", and \"150\"\n\nHints:\n 1: Avery has 68
LinkedIn connections.\n 2: Natalia has 10 fewer Facebook friends than
the person with 68 LinkedIn connections.\n 3: The person with 140
Facebook friends is either the one with 54 LinkedIn connections or
Evan.\n 4: The one with 54 LinkedIn connections has 10 fewer Facebook
friends than the one with 64 LinkedIn connections.\n\nIn your response,
format your final answer for each set of linked category values as a
python tuple of strings in this order:\n(\"120\", [value from LinkedIn],
[value from names])\n(\"130\", [value from LinkedIn], [value from
names])\n(\"140\", [value from LinkedIn], [value from names])\n(\"150\",
[value from LinkedIn], [value from names])"}],"ideal":"(\"120\", \"59\",
\"Natalia\")\n(\"130\", \"68\", \"Avery\")\n(\"140\", \"54\",
\"Camila\")\n(\"150\", \"64\", \"Evan\")"}
  ```
</details>

---
## [BrokerBrain/evals](https://github.com/BrokerBrain/evals)@[b0650402dd...](https://github.com/BrokerBrain/evals/commit/b0650402ddeaf93dba27f4a0252ae890bf8184ab)
#### Thursday 2023-06-08 03:51:26 by Alexander Shirkov

[Eval] English-Russian homonym context resolution (GPT-3.5: 0.42) (#1064)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
English-Russian homonym context resolution

### Eval description

Cross-lingual English-Russian eval to resolve ambiguity with homonyms
present.

### What makes this a useful eval?

[Insert why this eval is worth including and any additional context]
Cross-lingual homonyms are hard to resolve: they add context ambiguity,
which needs to be resolved via reasoning.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "You
are coming to a community facility to drop a child for hockey practice.
The road is under construction and big machines are paving it. What
would \"каток\" mean in this context? rink or roller"}], "ideal":
"unknown"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "You
are coming to a community facility to drop a child for hockey practice.
The road is under construction and big machines are paving it. Child
pointing at the machine and says: \"каток\". What does he mean: rink or
roller?"}], "ideal": "roller"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "You
are coming to a community facility to drop a child for hockey practice.
The road is under construction and big machines are paving it. Child
pointing at the building and says: \"каток\". What does he mean: rink or
roller?"}], "ideal": "rink"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "A
woman with long braided hair is working in the field. She cuts the grass
with scythe. Someone says \"хорошая коса\". Do they refer scythe or
hairstyle?"}], "ideal": "unknown"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "A
woman with long braided hair is working in the field. She cuts the grass
with scythe. Someone points at the quality of her work and says
\"хорошая коса\". Do they refer scythe or hairstyle?"}], "ideal":
"scythe"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "A
woman with long braided hair is working in the field. She cuts the grass
with scythe. Someone points at her head and says \"хорошая коса\". Do
they refer scythe or hairstyle?"}], "ideal": "hairstyle"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "Scythe
is found on a sandbar. A person is saying: \"коса\". Do they refer
scythe or sandbar?"}], "ideal": "unknown"}
{"input": [{"role": "system", "content": "For the given context, resolve
the ambiguity and determine the most appropriate response. If there is
one, output just one word; otherwise, output unknown. The responses must
be lowercase with no punctuation."}, {"role": "user", "content": "Scythe
is found on a sandbar. A person is saying: \"ржавая коса\". Do they
refer scythe or sandbar?"}], "ideal": "scythe"}
  ```
</details>

---
## [BrokerBrain/evals](https://github.com/BrokerBrain/evals)@[e959ff4b90...](https://github.com/BrokerBrain/evals/commit/e959ff4b90c3511f5b8a91ca69413a9206d8c4c7)
#### Thursday 2023-06-08 03:51:26 by Vasco Lange

[Eval] German part-of-speech (#1053)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
> german-part-of-speech

### Eval description

> For a given German word, the model is asked to list all possible parts
of speech (multiple choice). The model is also asked to think about the
word as an inflection of another word. The models output is tested
against annotations extracted from de.wiktionary.org. This is a follow
up to #1039

### What makes this a useful eval?

> Part of speech analysis is a basic task in language / grammar classes.
While it is usually done in the context of a sentence, coming up with
possible uses in lack of a sentence requires a certain amount of
creativity and language understanding, or very good recall of
information that is usually sparse outside of dictionaries. The task in
this eval could be seen as a combination of part of speech analysis and
an easy-to-evaluate form of the question "How could x be used in a
sentence".

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> To build the dataset, all 1.000.000+ entries of the German wiktionary
were parsed. Excluded from this list were all phrases, abbreviations,
symbols, names, toponyms and any words with at least one possible part
of speech not fitting the categories given in the prompt. Also I had to
exclude some entries where the part of speech could not be determined
automatically from the wikitext.
> From this set, words were sampled so that each combination of the
parts of speech existing in the dataset would be equally likely in the
tests. This way the model is tested to respond with all possible uses of
a word and not just the most common ones. > For combinations that fit a
lot of words, the uniform sampling led to a bias towards rarely used
words.
> The labels of each word were taken from the corresponding page at
de.wiktionary.org/wiki/{word}. The information taken from each page was:
the word, the part of speech this word can have in German and whether
the word is an abbreviation or not.
> This means only factual data was taken and is therefore in the public
domain.

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

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "anstelle"}],
"ideal": ["preposition, adverb, verb.", "preposition, verb, adverb.",
"adverb, preposition, verb.", "adverb, verb, preposition.", "verb,
preposition, adverb.", "verb, adverb, preposition."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "heute"}],
"ideal": ["adverb, verb.", "verb, adverb."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "Mist"}],
"ideal": ["noun, interjection.", "interjection, noun."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "Rotschöpfe"}],
"ideal": ["noun."]}
{"input": [{"role": "system", "content": "Act as a German language
part-of-speech classifier. You will be prompted with a single German
word. Return an unsorted comma-separated list for all the parts of
speech the word could possibly be, in any context. Take care to consider
if the word is any kind of inflection. If so, include the part of speech
for the main word.\nAnswer with the comma-separated list only. Use
single spaces after the commas. End the list with a dot. Do not include
any explanations. Only include parts of speech from the following list,
ignoring possible other parts of speech:\nadjective, adverb, article,
conjunction, interjection, noun, particle, preposition, pronoun,
verb\n**Example prompt 1**: alle\n**Example output 1**: adverb, noun,
pronoun.\n**Example prompt 2**: künftig\n**Example output 2**:
adjective, adverb.\n**Example prompt 3**: Sommelier\n**Example output
3**: noun.\n**Prompt**:"}, {"role": "user", "content": "vornüber"}],
"ideal": ["adverb."]}
  ```
</details>

---------

Co-authored-by: Vasco Yannic Lange <mail@vascolange.com>

---
## [benhoyt/operator](https://github.com/benhoyt/operator)@[807b8589e0...](https://github.com/benhoyt/operator/commit/807b8589e008fabfa3dee52f0f167fee841cb1fd)
#### Thursday 2023-06-08 03:52:13 by Ben Hoyt

Update Pyright to latest version, 1.1.313 (and fix new errors)

Boy this was more painful than I expected. Lots of fighting with the
compiler. I ended up disabling a few more Pyright issues, specifically
these seemed more trouble than they're worth:

* reportPrivateUsage: we do this often in the codebase, for example
  charm.py pokes at _ModelBackend stuff
* reportUnnecessaryIsInstance: we do lots of isinstance checks to
  detect type issues at runtime (we've done this since the beginning,
  and it's useful for people not using type checking)
* reportUnnecessaryComparison: similar to the above, but for checking
  "if non_optional_value is None" and the like

---
## [vdaular/linksfordevs](https://github.com/vdaular/linksfordevs)@[65d70b0f74...](https://github.com/vdaular/linksfordevs/commit/65d70b0f747ae6522b65af291693a248442e5638)
#### Thursday 2023-06-08 04:23:26 by Ben Dornis

Updating: 6/7/2023 10:00:00 PM

 1. Added: Functional programming in MongoDB
    (https://beny23.github.io/posts/functional_mongo_aggregation/)
 2. Added: Thoughts On A More Offline Life
    (https://davidt.co.uk/thoughts-on-a-more-offline-life)
 3. Added: You need black pixels
    (https://stephanango.com/black-pixels)
 4. Added: zacksiri.dev
    (https://zacksiri.dev/posts/work-distribution-with-jump-consistent-hashing)
 5. Added: Suburbian transplant: my experience moving and living in a big city
    (https://qf0.github.io/blog/2023/06/07/Suburbian-transplant-my-experience-moving-and-living-in-a-big-city)
 6. Added: On Object Orientation
    (https://jackrusher.com/journal/on-object-orientation.html)
 7. Added: Proto-Danksharding: Speeding Up Blobs Verification
    (https://belijzajac.dev/proto-danksharding-speeding-up-blobs-verification/)
 8. Added: Confessions
    (https://www.marginalia.nu/log/81-confessions/)
 9. Added: Improve Your Prompts for LLMs: Simple and Effective Techniques
    (https://www.dylanpaulus.com/posts/improve-your-prompts-llms/)
10. Added: A bicycle for the senses
    (https://stephanango.com/bicycle-for-the-senses)
11. Added: The business information server: generic data checking using PostgreSQL, PostgREST, and Semgrep
    (https://www.fabianzeindl.com/posts/business-information-server)
12. Added: How I made my web pages load 10x faster
    (https://prahladyeri.github.io/blog/2023/06/how-i-made-my-web-pages-load-10x-faster.html)
13. Added: Web Apps on macOS Sonoma 14 Beta
    (https://blog.tomayac.com/2023/06/07/web-apps-on-macos-sonoma-14-beta/)

Generation took: 00:08:58.7995112
 Maintenance update - cleaning up homepage and feed

---
## [rust-lang-ci/rust](https://github.com/rust-lang-ci/rust)@[80917360d3...](https://github.com/rust-lang-ci/rust/commit/80917360d350fb55aebf383e7ff99efea41f63fd)
#### Thursday 2023-06-08 04:44:11 by bors

Auto merge of #112292 - thomcc:tls-ohno, r=m-ou-se

Avoid unwind across `extern "C"` in `thread_local::fast_local`

This is a minimal fix for #112285, in case we want a simple patch that can be easily to backported if that's desirable.

*(Note: I have another broader cleanup which I've mostly omitted from here to avoid clutter, except for the `Cell` change, which isn't needed to fix UB, but simplifies safety comments).*

The only tier-1 target that this occurs on in a way that seems likely to cause problems in practice linux-gnu, although I believe some folks care about that platform somewhat 😉. I'm unsure how big of an issue this is. I've seen stuff like this behave quite badly, but there's a number of reasons to think this might actually be "fine in practice".

I've hedged my bets and assumed we'll backport this at least to beta but my feeling is that there's not enough evidence this is a problem worth backporting further than that.

### More details

This issue seems to have existed since `thread_local!`'s `const` init functionality was added. It occurs if you have a `const`-initialized thread local for a type that `needs_drop`, the drop panics, and you're on a target with support for static thread locals. In this case, we will end up defining an `extern "C"` function in the user crate rather than in libstd, and because the user crate will not have `#![feature(c_unwind)]` enabled, their panic will not be caught by an auto-inserted abort guard.

In practice, the actual situation where problems are likely[^ub] is somewhat narrower.

On most targets with static thread locals, we manage the TLS dtor list by hand (for reentrancy reasons among others). In these cases, while the users code may panic, we're calling it inside our own `extern "C"` (or `extern "system"`) function, which seems to (at least in practice) catch the panic and convert it to an abort.

However, on a few targets, most notably linux-gnu with recent glibc (but also fuchsia and redox), a tls dtor registration mechanism exists which we can actually use directly, [`__cxa_thread_atexit_impl`](https://github.com/rust-lang/rust/blob/master/library/std/src/sys/unix/thread_local_dtor.rs#L26-L36).

This is the case that seems most likely to be a cause for concern, as now we're passing a function to the system library and panicking out of it in a case where there are may not be Rust frames above it on the call stack (since it's running thread shutdown), and even if there were, it may not be prepared to handle such unwinding. If that's the case, it'd be bad.

Is it? Dunno. The fact that it's a `__cxa_*` function makes me think they probably have considered that the callback could throw but I have no evidence here and it doesn't seem to be written down anywhere, so it's just a guess. (I would not be surprised if someone comes into this thread to tell me how definitely-bad-news it is).

That said, as I said, all this is actually UB! If this isn't a "technically UB but fine in practice", but all bets are off if this is the kind of thing we are telling LLVM about.

[^ub]: This is UB so take that with a grain of salt -- I'm absolutely making assumptions about how the UB will behave "in practice" here, which is almost certainly a mistake.

---
## [itspebbleboy/The-Shining-CMPM120](https://github.com/itspebbleboy/The-Shining-CMPM120)@[ad03ab671c...](https://github.com/itspebbleboy/The-Shining-CMPM120/commit/ad03ab671c8f612afb05b02d64184788fc3f2169)
#### Thursday 2023-06-08 05:56:50 by Athena Patronas

updated hallway keys holy shit fuck my life these matrix's are so ass to change

---
## [mosswg/mycelium-lang](https://github.com/mosswg/mycelium-lang)@[050592335c...](https://github.com/mosswg/mycelium-lang/commit/050592335cc92eaabdf3e7c2158d6ddd7ce36f85)
#### Thursday 2023-06-08 06:26:06 by Moss

Pattern: Reintegrated Pattern Tokens With Patterns

They now work completely (probably I didn't really test it more than I
tested it before). Still not integrated with the parser, interpreter, or
tokenizer properly. Stay tuned I know you're sitting on the edge of your
seats for the next commit in a series that I haven't pushed in a repo
that I haven't worked on in 4 months.

Also, can I say losing motivation sucks. I was kinda on a roll with
this project and then I just lost my ability to work on it.
IDK why maybe its mental illness but it doesn't really matter because
that doesn't change what I can do about it. You may be thinking
(or maybe not because probably no one is reading this) if its mental
illness you probably can't do anything about it. But you would be
wrong, I can do something about it now, when I have motivation. I can
make the project easier to work on (like spliting a 1000 line header
file into multiple workable files). To be honest I kinda didn't want to
return to this project. Which absolutly sucks cause I love this project
and I really want to keep working on it but the state it was in just
made it a chore. I think thats partly why I want to make this language;
Because dealing with C, C++, Rust, Python, and any other language bs
just kill my motivation for a project. I remember when I first wanted to
learn programming I almost gave up because of cryptic complier errors.
If there weren't forms (like stackoverflow even with its many many flaws)
that explained what they meant, I probably never would have gotten past
the first program. I dont want anyone to give up on something so special
as programming for such a dumb reason. And I not saying that someone is
dumb for giving up. I still struggle with compilier (and linker) error
to this day, but I learned what the most common ones mean and I learned
how to figure out what the other ones mean. What I mean when I say that
is a dumb reason for giving up I mean that is a reason that should not
exist. There is absolutly no good reason why compiler errors should be
terrible. I called out rust earlier but thats not entirely fair because
it has really good complier error... Sometimes, other times it can be
just as bad as C. Anyways rant over hope you enjoyed.

P.S. If you're reading this I love you <3.

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[6c3f18a816...](https://github.com/Offroaders123/NBTify/commit/6c3f18a816bc3ad33288e69786f4c29ff2d26ef4)
#### Thursday 2023-06-08 07:14:03 by Offroaders123

Generic Shadows: Success!

Wow haha, turns out it was simply solveable with a slight type assertion. Didn't realize that would help there, guess I hadn't tried that yet. I think it was this error that helped me figure it out:

```
Argument of type '{ readonly name: Name; readonly endian: Endian; }' is not assignable to parameter of type 'U'.
'{ readonly name: Name; readonly endian: Endian; }' is assignable to the constraint of type 'U', but 'U' could be instantiated with a different subtype of constraint 'FormatOptions'. ts(2345)
```

I think this was the original error that I was encountering earlier. It didn't quite click for me what it was trying to say.

```
Type '{}' is not assignable to type 'U'. '{}' is assignable to the constraint of type 'U', but 'U' could be instantiated with a different subtype of constraint 'FormatOptions'. ts(2322)
```

I think I realized with the commit above that the type you are passing in is more specific than what the generic allows for, and that could break the types for the generic if you were to try narrowing the type like that. So it's not the parameter's default's issue, it's that the default is too specific for what the generic could allow for. So broadening the scope of the default back up to the type for the generic will make things dandy again. I think my initial problem was that I didn't know that it narrows the scope like that. I guess I did know that, since that's how my NBT primitive wrapper classes work with values, but I hadn't tied the scope-ish thing together like that yet.

So for the `2322` error message, I thought that assigning the default value to the parameter/variable would just use the type for that variable, but looks like there's room for two types in this case, one for what the generic is constrained to, and what the actual default is by itself. I'm curious what can be done to use this to one's *advantage?* This is making some other subconsious lightbulbs go off in my head.

I'm also wondering if there's some way I can add `const T` support to my NBT primitive wrappers, since you don't always want to have the constant value of the generic type. Say you pass in `35` as the number value, maybe you don't want to allow only `35` for that variable's value type. Right now you have to do `35 as number` or `as PrimitiveWrapper<number>` to widen the type scope back up again.

Thinking about it, it seems like these two behaviours (Why do I do that by default now, haha? Guess I'm turning British) are two sides to the same coin (Glass Attack!). I like the idea of what I could possibly use these to build things with. Super neat! Generics are complicated, and ***sick***! ('sick' was in Muscle-Man's voice, not sure why either)

Oh yeah, was working on a standalone demo to try and debug things in an effort to getting it to work. I'm glad I tried again, I was almost going to move on instead. I think using this in *combination* with the function type handling, this will be even stronger to build things with!

I'm glad that I dove this deep into getting the types for things set up, and that TypeScript can allow for things as complicated as this. It's super nice.

```ts
export interface Formatze {
  fancy?: boolean;
  woaheiy?: string;
}

export class NoiceData<T extends object = any, const U extends Formatze = Formatze> {
  declare readonly data: T;
  declare readonly fancy: U["fancy"];
  declare readonly woaheiy: U["woaheiy"];

  constructor(data: T | NoiceData<T>, { fancy, woaheiy }: U = {} as U) {
    if (data instanceof NoiceData){
      data = data.data;
    }
    this.data = data;
    this.fancy = fancy;
    this.woaheiy = woaheiy;
  }
}

declare const noice: NoiceData;

const heya = new NoiceData({},{ fancy: true, woaheiy: "gg" });
heya.fancy;
heya.woaheiy;

// I'd like to be able to merge the properties, at the type-level too!
const oaugh = new NoiceData(heya,{  });
```

---
## [OskarStark/symfony](https://github.com/OskarStark/symfony)@[f64e38d5b9...](https://github.com/OskarStark/symfony/commit/f64e38d5b9ae7e889da4a4482645bd17c7a5cd43)
#### Thursday 2023-06-08 07:34:32 by Nicolas Grekas

bug #50408 [AssetMapper] Change default importmap "provider" to JsDelivr+esm (weaverryan, nicolas-grekas)

This PR was merged into the 6.3 branch.

Discussion
----------

[AssetMapper] Change default importmap "provider" to JsDelivr+esm

| Q             | A
| ------------- | ---
| Branch?       | 6.3
| Bug fix?      | yes
| New feature?  | yes
| Deprecations? | no
| Tickets       | None
| License       | MIT
| Doc PR        |Still TODO

We currently use the https://jspm.org/ API in `importmap:require` to find a CDN URL for an npm package - just like Rails. Unfortunately, this is NOT as robust as we had thought. For me, it's broken. 3 big issues:

A) **Not Combined**
Some packages are not packed/combined. Example: [chart.js/auto](https://ga.jspm.io/npm:chart.js@4.3.0/auto/auto.js) imports other packages and results in 3 requests instead of 1. Not TERRIBLE... so here IS a terrible example: [`@popperjs`/core](https://ga.jspm.io/npm:`@popperjs`/core@2.11.7/lib/index.js) (needed by `bootstrap`) results in nearly 50 requests ❗

B) **Downloading Broken**
For some packages, downloading simply doesn't work - https://github.com/rails/importmap-rails/issues/65. ``@popperjs`/core` is another good example. Many of its imports have the form `import"./utils/getOppositeVariationPlacement.js`. If we download the main file, it looks locally for that `utils/` file, which won't be there. [`@chart`.js/auto](https://ga.jspm.io/npm:chart.js@4.3.0/auto/auto.js) is another example.

C) **process.env.NODE_ENV included**
Some packages (yes, again ``@popperjs`/core` is a great example!) contain `process.env.NODE_ENV` inside - https://github.com/rails/importmap-rails/issues/65#issuecomment-999569497

I believe that some package advertise an "esm" package... but just don't do a good job of creating it... or create it without the browser context in mind (or at least in a way that's inconvenient for downloading).

### jsDelivr to the rescue

THANKFULLY, jsDelivr seems to have a fantastic API/hosting that is *almost* exactly what we want: https://www.jsdelivr.com/?docs=esm

They deliver fully "packaged" modules, where the only import is for peer dependencies - e.g. https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/+esm

There IS still an issue when downloading. "Peer imports" are relative -e.g. `import*as t from"/npm/`@popperjs`/core@2.11.7/+esm";` However, these imports follow a VERY strict pattern. So, when `--download` is passed, we parse these, download the peer dependency and update the import contents to ``@popperjs`/core`, which works with the importmap. It's not ideal that we need to do that, but it's straightforward and works great.

Sorry again for this late PR - I had assumed that jspm was robust because Rails is using it. It turns out it's robust... unless you hit a "bad" package, then it's terrible. And they're not that rare: on ux.symfony.com, I have hit several.

Thanks!

Commits
-------

b530dc3bb1 [AssetMapper] Fix wiring resolvers, send requests in parallel and use readonly properties in MappedAsset
de44614447 [AssetMapper] Change default importmap "provider" to JsDelivr+esm

---
## [hazelcast/hazelcast](https://github.com/hazelcast/hazelcast)@[5f414fa3ad...](https://github.com/hazelcast/hazelcast/commit/5f414fa3ad03417e0b9078c8d9f249904003c936)
#### Thursday 2023-06-08 07:52:23 by James Holgate

Modify KubernetesClient shutdown behaviour [HZ-1921] (#24613)

The overall goal of this change is to change the shutdown behaviour of
KubernetesClient so our Stateful Set monitor thread shuts down before
our `ClusterTopologyIntentTracker`, to allow the intent tracker to fully
process all completed messages before Node shutdown.

**The Current Problem**
In its current state, the Stateful Set monitor thread is intended to
shutdown after `Thread#interrupt` is called, triggering the
`Thread#interrupted` check within the main `while(running)` loop of the
Runnable. However, this check is not reached as the call to
`WatchResponse#readLine` from within the main `run()` method is a
blocking call that waits until data is available to read before
proceeding. Since this call waits for non-null data before completing,
the result is always non-null, and therefore this code block never exits
under normal conditions:
```java
while ((message = watchResponse.nextLine()) != null) {
    onMessage(message);
}
```

Since this `while` loop cannot exit, and the `#readLine` method (which
passes to `BufferedReader#readLine` under the hood) is a blocking I/O
operation which cannot be interrupted, this operation does not end when
`Thread#interrupt` is called. This leads to the Stateful Set monitor
thread out-living the `ClusterTopologyIntentTracker`, even if the
StsMonitor is interrupted first. As a result, during shutdown, it is
possible for the StsMonitor to send data to the intent tracker after it
has been destroyed and its executor is no longer accepting tasks.

**The Root of the Problem**
To reach our goal of ensuring that the Stateful Set monitor thread can
no longer send requests to the `ClusterTopologyIntentTracker`, we need
to add synchronization between the two objects that guarantees the
intent tracker shuts down after the StsMonitor thread has completed.
This can be achieved using a simple `CountDownLatch` which is counted
down after the thread has completed, and awaited before shutting down
the tracker.

The main obstacle to achieving this is, as mentioned above, that the
StsMonitor thread cannot be interrupted when waiting for
`WatchResponse#readLine` to complete, and so the thread never completes.
The only way this thread can complete is to either force its
termination, or alter the message reading approach to allow interruption
as intended.

**Identifying Resolution Paths**
We don't want to force termination of our Stateful Set monitor thread as
this could result in message handling being terminated after it has been
received, but not before it has finished being processed. Therefore the
only way we can allow this thread to be interrupted as intended is to
alter the message reading mechanics in a way that allows it to be
interrupted as well.

There is no way for us to know if more messages are pending from the k8s
watch besides waiting for data to be received, so the best we can do is
allow the StsMonitor to finish processing any messages it has already
received (preventing process corruption), but terminate the stream of
new messages it is waiting for before we shutdown the intent tracker.

**Potential Solutions**
So we've identified the root of the problem as our `#readLine` function
blocking through interrupts, so how do we make it interruptible? Sadly
one of the shortcomings of I/O operations in Java is that they usually
cannot be interrupted in the traditional manner, so we have a few
approaches to consider:

1) We could modify the message reading code to use
`BufferedReader#ready` and `Thread#sleep` to periodically check if there
is data to be read before calling any read functions. The problem with
this approach is that A) `#ready` returns true if any data is available,
not just if there is a full line of data to be read; and B) utilizing a
sleep loop can result in delayed message handling at the least, or
busy-waiting overhead at worst.

2) We could use "hacky" solutions to interrupt the
`BufferedReader#readLine` such as closing underlying sockets or
connections, propagating an exception to the reader. The problem with
this solution is that everything related to our reading operation is
handled in `syncrhonized` blocks, and since our shutdown process starts
outside the StsMonitor thread, our calling thread is unable to obtain
these locks (being held by the StsMonitor)!

3) It's possible that we could rewrite the `WatchResponse` mechanics to
use Java NIO magic such as `Selector` for interruptible I/O operations.
The issue with this approach is that it would require fairly significant
refactoring of the related codebase, and may not end up providing the
exact functionality we are looking for in our use case.

4) We can introduce an `Executor` to handle our I/O operations within
the StsMonitor thread, allowing us to wait on a `Future#get` call
instead of our `BufferedReader#readLine` call, where a `Future#get`
operation can be interrupted by the waiting thread being interrupted.
The downside to this solution is we have to introduce an additional
thread on top of the existing StsMonitor thread itself.

**Selecting a Solution**
Considering the above information, I concluded the most sensible
approach was to use (4) and introduce an `Executor` thread for the I/O
operations. By using a separate thread for this call we can be rougher
with it, as we know that worse case scenario we interrupt a message
being read that has not started being processed yet (but we're shutting
down anyway).

This solution also allows for the least amount of underlying code
changes, as our `Future#get` can be interrupted without issue,
maintaining the current approach used for handling the StsMonitor
shutdown. The only downside for this approach is the addition of another
thread alongside the StsMonitor thread, but the actual impact of this
should be minimal as both threads will still be waiting most of the
time, so the only negative impact is being 1 tiny step closer to
possible thread starvation.

Generally I think this is the best solution at hand which allows quick
shutdown of the StsMonitor thread while minimising potential for data
loss or corruption. Combined with the `CountDownLatch` used, this allows
for consistent service shutdown order between the `StsMonitor` thread
and the `ClusterTopologyIntentTracker`.

---
## [petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023)@[2bf8dc210a...](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023/commit/2bf8dc210ad12820c4a8a7c0af55fc29328561b8)
#### Thursday 2023-06-08 08:03:54 by Petre Ro

2.1. API Tokens? Session Cookies?

 Join me, while we tell a tale as old as... the modern Internet: API authentication. A topic of hype, complexity and unlikely heroes. Characters include sessions, API tokens, OAuth, JSON web tokens! But what do we need for our situation?

 The first thing I want you to ask is:

  Who will be using my API?

 Is it your own JavaScript, or do you need to allow programmatic access? Like someone will write a script that will use your API?

 We're going to go through both of these use-cases... and each has some extra complexities that we'll discuss along the way.

 Everything is a Token!
 - By the way, when you think of API authentication, you typically think of an API token. And that's true! But it turns out that... pretty much all authentication is done by some sort of a token. Even session-based authentication is done by sending a cookie... which contains a unique, you guessed it, "token". It's a random string that PHP uses to find and load the related session data on the server.

 So the trick is figuring out which type of token you need in each situation and how the end-user will get that token.

 Use-Case 1: Building for your Own JavaScript
 - So let's talk about that first use-case: the user of your API is your own JavaScript.

 Well, before we even dive into security, make sure your frontend and your API live on the same domain... like the exact same domain, not just a subdomain. Why? Because if they live on two different domains or subdomains, you have to deal with CORS: Cross-Origin Resource Sharing.

 CORS not only adds complexity to your setup, it also hurts performance. Kévin Dunglas - the lead developer of API Platform - has a blog post about this. He even shows a strategy where your frontend and backend can live in totally different directories or repositories, but still live on the same domain thanks to some web server tricks.

 If you do, for some reason, decide to put your API and frontend on different sub-domains, then you will need to worry about CORS headers and you can solve that with NelmioCorsBundle. But, I don't recommend it.

 The case for Sessions
 - Anyways, back to security. If you're calling your API from your own JavaScript, the user is probably logging in via a login form with an email and password. It doesn't matter if that's a traditional login form or one that's built with a fancy JavaScript framework that submits via AJAX.

 And, honestly, a really simple way to handle this use-case is not with API tokens, but with good ol' fashioned HTTP Basic authentication. Yea, where you literally pass the email & password to each endpoint. For example, the user enters their email and password, you make an API request to some endpoint just to make sure it's valid, then you store that email and password in JavaScript and send it on every single API request going forward. Your email & password works basically like an API token.

 However, this has some practical challenges, like the question of where you securely store the email and password in JavaScript so you can continually use it. This is actually a problem in general with JavaScript and "credentials", including API tokens: you need to be very careful where you store those so that other JavaScript on your page can't read them. There are solutions: https://bit.ly/auth0-token-storage - but it adds complexity that you very likely don't need.

 So instead, for your own JavaScript, you can use a session. When you start a session in Symfony, it returns an "HTTP only" cookie... and that cookie contains the session id. Though, the contents of the cookie aren't really important: it could be the session id or some sort of token you invented and are reading in Symfony. The really important thing is that because the cookie is "HTTP only", it can't be read by JavaScript: your JavaScript or anyone else's JavaScript. But whenever you make an API request to your domain, that cookie's will come with it... and your app will use it to log in the user.

 So the API token in this situation is simply the "session id", which is stored securely in an HTTP-only cookie. Mmm. We will code through this use case.

 Oh, and by the way, one edge-case with this situation is if you have a Single Sign On situation - an SSO. In that case, you'll authenticate with your SSO like a normal web app. When you finish, you'll have a token, which you can then use to either authenticate the user with a session like normal... or you can use that token directly from your JavaScript. That's a more advanced use case that we won't go through in this tutorial... though, we will talk about how to read & validate API tokens regardless of where those tokens came from.

 Use-Case 2: Programmatic Access & API Tokens
 - The second big use-case for authentication is programmatic access. Some code will talk to your API... besides JavaScript from inside the browser.

 In this case, the API clients absolutely will send some sort of an API token string. And so, you need to make your API able to read a token that's sent on each request, usually sent on an Authorization header:

 $response = $httpClient->request(
    'GET',
    '/api/treasures',
    [
        'Authorization' => 'Bearer '.$apiToken,
    ],
);
 How the user gets this token depends: there are kind of two main cases. The first one is the "GitHub personal access token" case. This is where a user can browse to a page on your site and click to create a new access token. Then they can copy that and go use it in some code.

 The second big case is OAuth, which is just a fancy & secure way to get an access token. It's especially important when the "code" that's making the API requests is making those requests on "behalf" of some user on your system.

 Like imagine a site - ReplyToAllCommentsWithHearts.com - that allows you to connect with GitHub. Once you do, that site can then make API requests to GitHub for your account, like making comments as your user. Or imagine an iPhone app where, to log in, you show the user the login form on your site. Then, via an OAuth flow, that mobile app will receive an access token it can use to talk to your API on behalf of that user.

 We're going to talk about the personal access token method in this tutorial, including how to read and validate API tokens, no matter where they come from. We won't talk about the OAuth flow... and it's partially because it's a separate beast. Yes, if you have the use-case where you need to allow third parties to get API tokens for different users on your site, you will need some sort of OAuth server, whether you build it yourself or use some other solution. But once the OAuth server has done its work, the client that will talk to your API receives... a token! And then they'll use that token to talk to your API. So your API will need to read, validate, and understand that token, but it doesn't care how the API client got it.

 Ok, let's put all this theory behind us and start going through the first use-case next: allowing our JavaScript to log in by sending an AJAX request.

---
## [petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023)@[2485319916...](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023/commit/248531991632c6e60e81e03b0f574ac13a41c25b)
#### Thursday 2023-06-08 08:03:54 by Petre Ro

5.1 On Authentication Success

 If you refresh the page and check the web debug toolbar, you can see that we're not logged in. Let's try using a real email and password. We can cheat by clicking the email and password links: this user exists in our AppFixtures, so it should work. And... okay... the boxes disappear! But nothing else happens. We'll improve that in a minute.

 Thanks Session!
 - But for now, refresh the page and look at the web debug toolbar again. We're authenticated! Yea! Just by making a successful AJAX request to that login endpoint, that was enough to create the session and keep us logged in. Even better, if we started making requests to our API from JavaScript, those requests would be authenticated too. That's right! We don't need a fancy API token system where we attach a token to every request. We can just make a request and through the magic of cookies, that request will be authenticated.

 REST and What Data to Return from our Authentication Endpoint?
 - So, logging in worked... but nothing happened on the page. What should we do after authentication? Once again, it doesn't really matter. If you're writing your auth system for your own JavaScript, you should do whatever is useful for your frontend. We're currently returning the user id. But we could, if we wanted, return the entire user object as JSON.

 But there's one tiny problem with that. It's not super RESTful. This is one of those "REST purity" things. Every URL in your API, on a technical level, represents a different resource. This represents the collection resource, and this URL represents a single User resource. And if you have a different URL, that's understood to be a different resource. The point is that, in a perfect world, you would just return a User resource from a single URL instead of having five different endpoints to fetch a user.

 If we return the User JSON from this endpoint, we're "technically" creating a new API resource. In fact, anything we return from this endpoint, from a REST point of view, becomes a new resource in our API. To be honest, this is all technical semantics and you should feel free to do whatever you want. But, I do have a fun suggestion.

 To try be helpful to our frontend and somewhat RESTful, I have another idea. What if we return nothing from the endpoint.... but sneak the user's IRI onto the Location header of the response. Then, our frontend could use that to know who just logged in.

 Let me show you. First, instead of returning the User ID, we're going to return the IRI, which will look something like '/api/users/'.$user->getId(). But I don't want to hard code that because we could potentially change the URL in the future. I'd rather have API Platform generate that for me.

---
## [petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023)@[53e278a15a...](https://github.com/petre-symfony/api-platform-3-part-2-security-for-you-symfonycasts-june-2023/commit/53e278a15a5f78fa76ebebd114ed6bd569b2c385)
#### Thursday 2023-06-08 08:03:54 by Petre Ro

4.1. Handling Authentication Errors

 When we log in with an invalid email and password, it looks like the json_login system sends back some nice JSON with an error key set to "Invalid credentials". If we wanted to customize this, we could create a class that implements AuthenticationFailureHandlerInterface:

 class AppAuthFailureHandler implements AuthenticationFailureHandlerInterface
 {
    public function onAuthenticationFailure($request, $exception)
    {
        return new JsonResponse(
            ['something' => 'went wrong'],
            401
        );
    }
 }
 And then set its service ID onto the failure_handler option under json_login:

 json_login:
    failure_handler: App\Security\AppAuthFailureHandler

 Showing the Error on the Form
 - But, this is plenty good for us. So let's use it over in our /assets/vue/LoginForm.vue. We won't go too deeply into Vue, but I already have state called error, and if we set that, it will show up on the form

 After making the request, if the response is not okay, we're already decoding the JSON. Now let's say error.value = data.error

 To see if this works, make sure you have Webpack Encore running in the background so it recompiles our JavaScript. Refresh. And... you can click this little link to cheat and enter a valid email. But then type in a ridiculous password and... I love it! We see "Invalid credentials" on top with some red boxes!

---
## [APOPHIS9283/kernel_google_gs201](https://github.com/APOPHIS9283/kernel_google_gs201)@[d1655955a2...](https://github.com/APOPHIS9283/kernel_google_gs201/commit/d1655955a2bdc4965f56018441915555f01cfde1)
#### Thursday 2023-06-08 08:14:13 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

commit f53af4285d775cd9a9a146fc438bd0a1bee1838a upstream.

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
Signed-off-by: Panchajanya1999 <kernel@panchajanya.dev>

---
## [tyeagg/tgstation](https://github.com/tyeagg/tgstation)@[c5dce84be8...](https://github.com/tyeagg/tgstation/commit/c5dce84be826ea945a11c492dce7eb2c2789548a)
#### Thursday 2023-06-08 08:23:44 by Rhials

Deadchat Announcement Variety Pack 1 (#75140)

## About The Pull Request

Adds announce_to_ghosts()/notify_ghosts() calls to a bunch of different
things.

**THIS INCLUDES:**
- Powersink being activated/reaching critical (explosion) heat capacity.
- His Grace being awoken.
- Hot Potatoes being armed.
- Ascension Rituals being completed.
- Eyesnatcher victims.
- Ovens exploding as a result of the Aurora Caelus event.
- Wizard Imposter spawns.
- Rock-Paper-Scissors with death as the result of Helbital consumption.
- BSA impact sites.
- Spontaneous Appendicitis.
- The purchasing of a badass syndie balloon.
- The Supermatter beginning to delaminate.

This was everything that I could think of that would be worth announcing
to deadchat. These were all chosen with consideration to questions like
"how easy would it be to spam deadchat with this?" and "will observers
actually see the interesting thing happen, or just the aftermath?".

Not gonna lie, I've really become an observer main as of recently. Maybe
that's being reflected in my recent PRs. Who's to say? Deadchat
Announcement Variety Pack 2 will probably never come out. Sorry.
## Why It's Good For The Game

Gives deadchat a better indiciation of when/where something **REALLY
FUNNY** is about to happen. Draws attention to certain things that are
likely to gather an audience anyways, but sooner (for your viewing
pleasure). In simple terms, it helps the observers observe things
better.

Some cases, such as the aurora caelus or helbitaljanken, are occurrences
so rare that they deserve the audience.
## Changelog
:cl: Rhials
qol: Observers now recieve an alert when a powersink is activated/about
to explode.
qol: His Grace being awoken now alerts observers, to give you a
headstart on your murderbone ghost ring.
qol: Ascension Rituals being completed will also alert observers, for
basically the same reason.
qol: Arming a hot potato will now alert observers. Catch!
qol: Eyesnatcher victims will now notify observers, and invite them to
laugh at their state of misery and impotence.
qol: Observers will be notified of any acute references to The Simpsons
or other 20th Television America copyright properties.
qol: Wizard Imposter spawns alert observers, much like any other ghost
role event should.
qol: Playing Rock-Paper-Scissors with death will now alert the observers
and invite them to watch. Better not choke!
qol: Observers now get an orbit link for BSA impact sites. Why does it
keep teleporting me to the AI upload??
qol: Spontaneous Appendicitis now alerts deadchat. 
qol: The purchasing of a badass syndie balloon now alerts deadchat. You
might not be any more powerful, but at least you have an audience.
qol: When beginning to delaminate, the Supermatter will alert observers
and invite them to watch the fireworks.
/:cl:

---
## [tyeagg/tgstation](https://github.com/tyeagg/tgstation)@[1674f25725...](https://github.com/tyeagg/tgstation/commit/1674f25725c25e15769b031553b42144f526f841)
#### Thursday 2023-06-08 08:23:44 by John Willard

New Medical job: The Coroner (#75065)

## About The Pull Request

HackMD: https://hackmd.io/RE9uRwSYSjCch17-OQ4pjQ?view

Feedback link: https://tgstation13.org/phpBB/viewtopic.php?f=10&t=33972

Adds a Coroner job to the game, they work in the Medical department and
have their office in the Morgue.
I was inspired to make this after I had played my first round on
Paradise and messed around in there. The analyzer is copied from there
(https://github.com/ParadiseSS13/Paradise/pull/20957), and their
jumpsuit is also mostly stolen from it (i just copied the color scheme
onto our own suits).

Coroners can perform autopsies on people to see their stats, like this

![image](https://user-images.githubusercontent.com/53777086/235369225-805d482c-56c0-441c-9ef8-a42d0a0192bc.png)

They have access to Medbay, and on lowpop will get Pharmacy (to make
their own formaldehyde). They also have their own Secure Morgue access
for their office (doubles as a surgery room because they are edgelords
or whatever) and the secure morgue trays.

Secure Morgue trays spawn with their beepers off and is only accessible
by them, the CMO, and HoS. It's used to morgue Antagonists. Security's
own morgue trays have been removed.

The job in action


https://cdn.discordapp.com/attachments/950489581151735849/1102297675669442570/2023-04-30_14-16-06.mp4

### Surgery changes

Autopsies are a Surgery, and I tried to intertwine this with the
Dissection surgery.
Dissections and Autopsies both require the Autopsy scanner to perform
them, however you can only perform one on any given body. Dissections
are for experiments, Autopsies is for the paper of information.

Dissected bodies now also give a ~20% surgery speed boost, this was
added at the request of Fikou as a way to encourage Doctors to let the
Coroner do their job before reviving a body.
I also remember the Medical skill, which allowed Doctors to do surgery
faster on people, and I hope that this can do something like that
WITHOUT adding the potential for exploiting, which led to the skill's
downfall.

### Morgue Improvements

Morgue trays are no longer named with pens, they instead will steal the
name of the last bodybag to be put in them.

Morgue trays are also removed from Brig Medical areas and Robotics, now
they have to bring their corpses to the Morgue where the Coroner can
keep track and ensure records are properly updated.

### Sprite credits

I can't fit it all in the Changelog, so this is who made what

McRamon
- Autopsy scanner

Tattax 
- Table clock sprites and in-hands

CoiledLamb
- Coroner jumpsuits & labcoats (inhand, on sprite, and their respective
alternatives)
- Coroner gloves
- CoronerDrobe (the vending machine)

## Why It's Good For The Game

This is mostly explained in the hackmd, but the goal of this is:

1. Increase the use of the Medical Records console.
2. Add a new and interesting way for Detectives to uncover mysteries.
3. Add a more RP-flavored role in Medical that still has mechanics tied
behind it.

## Changelog

:cl: JohnFulpWillard, sprites by McRamon, tattax, and Lamb
add: The Coroner, a new Medical role revolving around dead corpses and
autopsies.
add: The Coroner's Autopsy Scanner, used for discovering the cause for
someone's death, listing their wounds, the causes of them, their
reagents, and diseases (including stealth ones!)
qol: Morgue Trays are now named after the bodybags inside of them.
balance: The morgue now has 'Secure' morgue trays which by default don't
beep.
balance: Security Medical area and Robotics no longer have their own
morgue trays.
balance: Dissected bodies now have faster surgery speed. Autopsies also
count as dissections, however they're mutually exclusive.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Unknownity/cmss13](https://github.com/Unknownity/cmss13)@[d40fdb9101...](https://github.com/Unknownity/cmss13/commit/d40fdb91011bb0aa4053a9386311ed131e0ae6ac)
#### Thursday 2023-06-08 08:49:23 by NewyearnewmeUwu

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
## [prometheus-community/node-exporter-textfile-collector-scripts](https://github.com/prometheus-community/node-exporter-textfile-collector-scripts)@[0ca17e6e51...](https://github.com/prometheus-community/node-exporter-textfile-collector-scripts/commit/0ca17e6e510404139188d3644001c5b59e494895)
#### Thursday 2023-06-08 10:36:20 by Antoine Beaupré

lvm: add support for "all" checks

It seems rather inconvenient to have to specify all those switches by
hand. Right now, I need to specify -gpst to get all the stats and, if
some new metric get added (e.g. #159 hopefully), I need to remember to
update my callers to match. This is annoying.

Let's make a -a that's going to do it all for us. Hell, i'd make it
the default, personally, if I wasn't worried about breaking people's
stuff...

This obviously conflicts with other PRs that might add another flag
like this, like #159. Please prioritize the latter.

Signed-off-by: Antoine Beaupré <anarcat@debian.org>

---
## [kernel-patches/bpf-rc](https://github.com/kernel-patches/bpf-rc)@[1ea4a3e5ce...](https://github.com/kernel-patches/bpf-rc/commit/1ea4a3e5ce17ea0d87f590e2d43614cea28349a2)
#### Thursday 2023-06-08 11:31:11 by Daniel Borkmann

bpf: Add fd-based tcx multi-prog infra with link support

This work refactors and adds a lightweight extension ("tcx") to the tc BPF
ingress and egress data path side for allowing BPF program management based
on fds via bpf() syscall through the newly added generic multi-prog API.
The main goal behind this work which we also presented at LPC [0] last year
and a recent update at LSF/MM/BPF this year [3] is to support long-awaited
BPF link functionality for tc BPF programs, which allows for a model of safe
ownership and program detachment.

Given the rise in tc BPF users in cloud native environments, this becomes
necessary to avoid hard to debug incidents either through stale leftover
programs or 3rd party applications accidentally stepping on each others toes.
As a recap, a BPF link represents the attachment of a BPF program to a BPF
hook point. The BPF link holds a single reference to keep BPF program alive.
Moreover, hook points do not reference a BPF link, only the application's
fd or pinning does. A BPF link holds meta-data specific to attachment and
implements operations for link creation, (atomic) BPF program update,
detachment and introspection. The motivation for BPF links for tc BPF programs
is multi-fold, for example:

  - From Meta: "It's especially important for applications that are deployed
    fleet-wide and that don't "control" hosts they are deployed to. If such
    application crashes and no one notices and does anything about that, BPF
    program will keep running draining resources or even just, say, dropping
    packets. We at FB had outages due to such permanent BPF attachment
    semantics. With fd-based BPF link we are getting a framework, which allows
    safe, auto-detachable behavior by default, unless application explicitly
    opts in by pinning the BPF link." [1]

  - From Cilium-side the tc BPF programs we attach to host-facing veth devices
    and phys devices build the core datapath for Kubernetes Pods, and they
    implement forwarding, load-balancing, policy, EDT-management, etc, within
    BPF. Currently there is no concept of 'safe' ownership, e.g. we've recently
    experienced hard-to-debug issues in a user's staging environment where
    another Kubernetes application using tc BPF attached to the same prio/handle
    of cls_bpf, accidentally wiping all Cilium-based BPF programs from underneath
    it. The goal is to establish a clear/safe ownership model via links which
    cannot accidentally be overridden. [0,2]

BPF links for tc can co-exist with non-link attachments, and the semantics are
in line also with XDP links: BPF links cannot replace other BPF links, BPF
links cannot replace non-BPF links, non-BPF links cannot replace BPF links and
lastly only non-BPF links can replace non-BPF links. In case of Cilium, this
would solve mentioned issue of safe ownership model as 3rd party applications
would not be able to accidentally wipe Cilium programs, even if they are not
BPF link aware.

Earlier attempts [4] have tried to integrate BPF links into core tc machinery
to solve cls_bpf, which has been intrusive to the generic tc kernel API with
extensions only specific to cls_bpf and suboptimal/complex since cls_bpf could
be wiped from the qdisc also. Locking a tc BPF program in place this way, is
getting into layering hacks given the two object models are vastly different.

We instead implemented the tcx (tc 'express') layer which is an fd-based tc BPF
attach API, so that the BPF link implementation blends in naturally similar to
other link types which are fd-based and without the need for changing core tc
internal APIs. BPF programs for tc can then be successively migrated from classic
cls_bpf to the new tc BPF link without needing to change the program's source
code, just the BPF loader mechanics for attaching is sufficient.

For the current tc framework, there is no change in behavior with this change
and neither does this change touch on tc core kernel APIs. The gist of this
patch is that the ingress and egress hook have a lightweight, qdisc-less
extension for BPF to attach its tc BPF programs, in other words, a minimal
entry point for tc BPF. The name tcx has been suggested from discussion of
earlier revisions of this work as a good fit, and to more easily differ between
the classic cls_bpf attachment and the fd-based one.

For the ingress and egress tcx points, the device holds a cache-friendly array
with program pointers which is separated from control plane (slow-path) data.
Earlier versions of this work used priority to determine ordering and expression
of dependencies similar as with classic tc, but it was challenged that for
something more future-proof a better user experience is required. Hence this
resulted in the design and development of the generic attach/detach/query API
for multi-progs. See prior patch with its discussion on the API design. tcx is
the first user and later we plan to integrate also others, for example, one
candidate is multi-prog support for XDP which would benefit and have the same
'look and feel' from API perspective.

The goal with tcx is to have maximum compatibility to existing tc BPF programs,
so they don't need to be rewritten specifically. Compatibility to call into
classic tcf_classify() is also provided in order to allow successive migration
or both to cleanly co-exist where needed given its all one logical tc layer.
tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail. The work has been tested with tc-testing selftest suite
which all passes, as well as the tc BPF tests from the BPF CI, and also with
Cilium's L4LB.

Kudos also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com/
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com/

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [kernel-patches/bpf-rc](https://github.com/kernel-patches/bpf-rc)@[34494dd0f0...](https://github.com/kernel-patches/bpf-rc/commit/34494dd0f0d1850e78e2c983df4680d1a9499984)
#### Thursday 2023-06-08 11:31:11 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for the case of attaching
      - Enforced only at attach time
    - BPF_F_{FIRST,LAST}
      - Enforced throughout the bpf_mprog state's lifetime
      - Admin override possible (e.g. link detach, prog-based BPF_F_REPLACE)
  - Internal revision counter and optionally being able to pass expected_revision
  - User space daemon can query current state with revision, and pass it along
    for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure) and bpf_mprog_cp (control-path
structure). Both have been separated, so that fast-path gets efficient packing
of bpf_prog pointers for maximum cache efficieny. Also, array has been chosen
instead of linked list or other structures to remove unnecessary indirections
for a fast point-to-entry in tc for BPF. The bpf_mprog_entry comes as a pair
via bpf_mprog_bundle so that in case of updates the peer bpf_mprog_entry
is populated and then just swapped which avoids additional allocations that
could otherwise fail, for example, in detach case. bpf_mprog_{fp,cp} arrays are
currently static, but they could be converted to dynamic allocation if necessary
at a point in future. Locking is deferred to the in-kernel user of bpf_mprog,
for example, in case of tcx which uses this API in the next patch, it piggy-
backs on rtnl. The nitty-gritty details are in the bpf_mprog_{replace,head_tail,
add,del} implementation and an extensive test suite for checking all aspects
of this API for prog-based attach/detach and link API as BPF selftests in
this series.

Kudos also to Andrii Nakryiko for API discussions wrt Meta's BPF management daemon.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net/
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [MuhammadAhmad1444/Dot-Box-Game-cpp](https://github.com/MuhammadAhmad1444/Dot-Box-Game-cpp)@[f111da24f3...](https://github.com/MuhammadAhmad1444/Dot-Box-Game-cpp/commit/f111da24f384b7b18e85842062ac969e06420ec1)
#### Thursday 2023-06-08 11:48:39 by MuhammadAhmad1444

Add files via upload

Dot and Box game in C++ - A classic multiplayer game where players take turns connecting dots to form boxes. This repository contains the C++ implementation with a command-line interface. Players can enjoy strategic gameplay while competing against friends or an AI opponent. Dive into the code to explore the game logic, algorithms, and data structures employed to create an engaging gaming experience. Enhance your C++ skills by studying and contributing to this project. Have fun playing and happy coding.
Feel free to modify or expand on this description based on the specific features, design, or unique aspects of your Dot and Box game implementation.

---
## [samsung-msm8974/kernel_samsung_msm8974](https://github.com/samsung-msm8974/kernel_samsung_msm8974)@[ec89fa3a47...](https://github.com/samsung-msm8974/kernel_samsung_msm8974/commit/ec89fa3a47d91b5aea19527b1dcfc09554af0d45)
#### Thursday 2023-06-08 12:26:30 by Linus Torvalds

mm: get rid of 'vmalloc_info' from /proc/meminfo

It turns out that at least some versions of glibc end up reading
/proc/meminfo at every single startup, because glibc wants to know the
amount of memory the machine has.  And while that's arguably insane,
it's just how things are.

And it turns out that it's not all that expensive most of the time, but
the vmalloc information statistics (amount of virtual memory used in the
vmalloc space, and the biggest remaining chunk) can be rather expensive
to compute.

The 'get_vmalloc_info()' function actually showed up on my profiles as
4% of the CPU usage of "make test" in the git source repository, because
the git tests are lots of very short-lived shell-scripts etc.

It turns out that apparently this same silly vmalloc info gathering
shows up on the facebook servers too, according to Dave Jones.  So it's
not just "make test" for git.

We had two patches to just cache the information (one by me, one by
Ingo) to mitigate this issue, but the whole vmalloc information of of
rather dubious value to begin with, and people who *actually* want to
know what the situation is wrt the vmalloc area should just look at the
much more complete /proc/vmallocinfo instead.

In fact, according to my testing - and perhaps more importantly,
according to that big search engine in the sky: Google - there is
nothing out there that actually cares about those two expensive fields:
VmallocUsed and VmallocChunk.

So let's try to just remove them entirely.  Actually, this just removes
the computation and reports the numbers as zero for now, just to try to
be minimally intrusive.

If this breaks anything, we'll obviously have to re-introduce the code
to compute this all and add the caching patches on top.  But if given
the option, I'd really prefer to just remove this bad idea entirely
rather than add even more code to work around our historical mistake
that likely nobody really cares about.

Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Change-Id: Ia17de8b8f49d801efa5aaff3c61ba4c1082dc1e3

---
## [IGES-Institut/evals](https://github.com/IGES-Institut/evals)@[e116ede848...](https://github.com/IGES-Institut/evals/commit/e116ede848957eff8e76b5d8463ed5291163a28f)
#### Thursday 2023-06-08 12:35:25 by Wesley Barlow

Add eval: rhetorical-devices (#1005)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
rhetorical-devices

### Eval description

Evaluates model's ability to select the most specific rhetorical
modification of a sentence from a multiple choice with a large number of
nuanced rhetorical devices.

### What makes this a useful eval?

Useful for using LLMs to write novels and generate consistent/parametric
authorial tone.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL She likes to listen to the winds. MODIFIED
She swoons at such sweet gales. Answer in the format (x) Rhetorical"}],
"ideal": "(a) Alliteration"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL The rock was very large. MODIFIED The rock
was remarkably raised. Answer in the format (x) Rhetorical"}], "ideal":
"(a) Alliteration"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Visionary dreams elevate me at night.
MODIFIED Visionary reminitions elevate self resting in lightlessness.
Answer in the format (x) Rhetorical"}], "ideal": "(b) Assonance"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Once, I thought I had lost her pet.
MODIFIED Once, dunce — thought I lost Juliet's pet. Answer in the format
(x) Rhetorical"}], "ideal": "(b) Assonance"}
{"input": [{"role": "system", "content":"Which of the following
rhetorical devices was added to the original sentence? Choose the most
specific of the following (a) Alliteration, (b) Assonance, (c)
Consonance, (d) Cacophony, (e) Onomatopoeia, (f) Anadiplosis, (g)
Conduplicatio, (h) Anaphora, (i) Epistrophe, (j) Symploce, (k)
Epanalepsis, (l) Epizeuxis, (m) Antanaclasis, (n) Diacope, (o)
Antithesis, (p) Antimetabole, (q) Chiasmus, (r) Asyndeton, (s)
Polysyndeton, (t) Catacosmesis, (u) Oxymoron, (v) Zeugma"}, {"role":
"user", "content": "ORIGINAL Do you want to understand research on
artificial general intelligence? MODIFIED Don't you want to investigate
artifacts of artificial general intelligence? Answer in the format (x)
Rhetorical"}], "ideal": "(c) Consonance"}
  ```
</details>

---
## [IGES-Institut/evals](https://github.com/IGES-Institut/evals)@[b91292c803...](https://github.com/IGES-Institut/evals/commit/b91292c803af2bdadeec3853ab03514b73310109)
#### Thursday 2023-06-08 12:35:25 by Zyenith

Add Eval: Internal Representations via Counting (#1006)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
Internal representations via counting

### Eval description

Using series of logical questions that require multiple (simple)
manipulations of numbers to get the ideal answer. These are basic tasks
that should be doable by an LLM, but require several steps of internal
"thought" to get right.

### What makes this a useful eval?

Situations with number manipulation with multiple steps are prevalent
anywhere in the modern world. Testing the internal representation of the
LLM can provide other insights on how well its "mind" processes
information.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval is capable of providing insight into the LLM's internal
representation of objects versus answering fact-based questions or
straightforward complex logic puzzles.

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

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"Roger and Emily are in a room.
Roger puts a cat in an empty box while Emily is in the room. They both
leave, and Emily returns and puts a turtle in the box as well. How many
items does Roger think are in the box?"}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"There are four darts already on a
dart board. Bob throws one dart at the dartboard, and it lands. Alice
throws two darts, and one misses but one hits the dartboard. How many
darts are on the dartboard?"}],"ideal":"6"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"A bakery sold 25 cakes in the
morning and 17 cakes in the afternoon. The day after, they sold 15 more
cakes. How many cakes did they sell on the second day?"}],"ideal":"15"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"There are six blue birds and three
red birds sitting on a tree. Two blue birds fly away, and one red bird
flies away. How many birds are left on the tree?"}],"ideal":"6"}
{"input":[{"role":"system","content":"You will be prompted with a
logical question. Respond only with a number, nothing else is
required."},{"role":"user","content":"John has double the amount of
pencils than Sarah, and Sarah has as many pencils as Mark. Mark has 2
pencils. How many pencils does John have?"}],"ideal":"4"}
  ```
</details>

---
## [IGES-Institut/evals](https://github.com/IGES-Institut/evals)@[3d9de9a624...](https://github.com/IGES-Institut/evals/commit/3d9de9a62411f9e6a999e96ce8f07eebf0e8c121)
#### Thursday 2023-06-08 12:35:25 by dyar-al-ashtari

Eval Norwegian lexicon (#1044)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
`norwegian-lexicon`

### Eval description

This eval uses valid Norwegian words taken from the dictionary and
assesses whether GPT can recognize them as valid.

### What makes this a useful eval?

The Norwegian language is simple yet complicated at the same time. There
are a lot of words that are valid Norwegian words that do not get
recognized anymore. An AI should be able to identify these words with
precision. All of the words used in the samples are valid Norwegian
words and can be found in the dictionary. After assessing GPT-4 (through
the playground) and GPT-3.5 -- it failed to recognize most of the words.
Some of the words would return positive during some evals. Other times
it wouldn't recognize them. After asking GPT why it is not a valid word,
it would apologize and fix its mistake.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

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

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Skarpne"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Bløtne"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Hovedantall"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Klenge"}],"ideal":"Y"}
{"input":[{"role":"system","content":"You will be prompted with a single
word. Does this word exist in the Norwegian language? Answer with
exactly one letter: Y or N. Do not use punctionation. Do not explain
your answer."},{"role":"user","content":"Blankolov"}],"ideal":"Y"}
  ```
</details>

---
## [IGES-Institut/evals](https://github.com/IGES-Institut/evals)@[6a37c9b51b...](https://github.com/IGES-Institut/evals/commit/6a37c9b51b48a2f735898846cfb08b37cbd63179)
#### Thursday 2023-06-08 12:35:25 by Aaron Goldsmith

[eval] 3x3 Game Of Life  (#345)

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
GOL

### Eval description

Determine the next state of a 3x3 Game of Life Board. 

### What makes this a useful eval?

Spacial reasoning

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
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n1 1 1\n\n0 0
0\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 1 0\n\n0 1
0\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n1 1 1\n\n1 0
0\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["1 0 1\n\n1 0
1\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 1\n\n1 1
1\n\n1 1 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["1 0 1\n\n0 0
0\n\n1 0 1"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 1\n\n0 1
1\n\n0 0 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 1 1\n\n0 1
1\n\n0 0 0"]}
{"input": [{"role": "system", "content": "You are a helpful assistant.
"}, {"role": "user", "content": "Using the classic Game of Life Rules,
determine the next state of the 3x3 Game of life board: \n0 1 0\n\n0 0
0\n\n1 1 0 \n\n Do not provide any explanation other than the next state
of the board. e.g 0 0 0\n\n0 0 0\n\n0 0 0"}], "ideal": ["0 0 0\n\n1 1
0\n\n0 0 0"]}
  ```
</details>

---
## [Waseemq1235/cmss13](https://github.com/Waseemq1235/cmss13)@[e8f53984c1...](https://github.com/Waseemq1235/cmss13/commit/e8f53984c1edd98c25b4c3199a6a5363eaa26869)
#### Thursday 2023-06-08 12:39:42 by morrowwolf

Warrior Nerf (#3424)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR removes cooldown reduction on slash.

This PR slightly lowers fling and punch cooldowns.

This PR lowers fling stun to a micro stun and adds a slow.

This PR decreases lunge range to 4 tiles.

As a reminder design feedback and balance concerns go here:
https://forum.cm-ss13.com/w/pr-feedback/steps/step_1

# Explain why it's good for the game

Warrior rework has been on my mind for a while. I'm not quite sure how I
want to do it. The cooldowns on abilities and the abilities themselves
are incredibly powerful crowd control and just a few warriors can do
immense damage to large groups of marines. It's just... not in a great
place for a T2 and sadly I don't have a thorough game plan yet to rework
it into something more bearable while equally enjoyable to play. In the
mean time, this is what we're getting. Am I promising a rework in the
near future? Not really. It's on my list somewhere. Does warrior need
some changing around? Yeah.

Overall, this should make warrior a bit more bearable. We'll see. More
changes as testing goes.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removes warrior cooldown reduction on slash
balance: Warrior slightly lowered fling and punch cooldowns
balance: Lowers fling stun to a micro stun and adds a slow
balance: Decreases warrior lunge range to 4 tiles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [ShubhamJethava51/Counsellor](https://github.com/ShubhamJethava51/Counsellor)@[7adb80bdf0...](https://github.com/ShubhamJethava51/Counsellor/commit/7adb80bdf0881a3bd7b96f37d821c1dbc5e7e0d6)
#### Thursday 2023-06-08 13:00:44 by Sahil Ali

Login and Sign Up { ui redesign } 

These UI enhancements aim to make the login and sign up processes more intuitive and visually appealing, resulting in an improved user engagement and satisfaction. By incorporating user-friendly design principles and enabling social login options, we expect to enhance the overall user experience and encourage higher conversion rates.

---
## [raeleus/libgdx](https://github.com/raeleus/libgdx)@[e1d1fdc5fb...](https://github.com/raeleus/libgdx/commit/e1d1fdc5fb5b8409dc74f638c633ead405e535f3)
#### Thursday 2023-06-08 13:13:46 by Tommy Ettinger

I18NMessageTest needs to reset I18NBundle static state. (#7101)

* Mark PauseableThread as excluded on GWT.

* Minor typo corrections.

* Fix atan2() when it should produce 0f.

Without this small change (which has essentially no performance impact that I could measure), calling atan2() with a point on the x-axis would produce a small but non-zero result, which is incorrect.

* Add atan, atan2, asin, acos for degrees.

This also includes atan2Deg360(), which in my opinion is the most useful of these because it does something differently from Math.atan2(), and can often save some effort.

* Approximations for tan() and tanDeg().

Sorry this is so long-winded, but the error isn't as straightforward to express as with sin() or cos().

* Apply formatter

* Add to MathUtilsTest.

* Apply formatter

* Stop trying to load defaults from wrong dir.

This old behavior broke Flame's effect-open dialog when any particle effect used the default billlboard or model particle. Now Flame tries to load a file given its absolute path (like before), but if it fails, it falls back to trying the default filenames as internal files.

* I18NMessageTest needs to reset I18NBundle state.

If you run I18NSimpleMessageTest and then I18NMessageTest without this PR, then the first test will have called I18NBundle.setSimpleFormatter(true), but the second test needs it to be set to false.

Because the tests are still perfectly usable if you run them on their own (or use LWJGL2, I think, because it might not share static state), this is not at all a priority to merge; it just makes running many tests in one session not throw an Exception.

---------

Co-authored-by: GitHub Action <action@github.com>

---
## [cilium/linux](https://github.com/cilium/linux)@[64aa8479b7...](https://github.com/cilium/linux/commit/64aa8479b7cf95b92f19283e0e66409655ca34a8)
#### Thursday 2023-06-08 13:16:20 by Daniel Borkmann

bpf: Add generic attach/detach/query API for multi-progs

This adds a generic layer called bpf_mprog which can be reused by different
attachment layers to enable multi-program attachment and dependency resolution.
In-kernel users of the bpf_mprog don't need to care about the dependency
resolution internals, they can just consume it with few API calls.

The initial idea of having a generic API sparked out of discussion [0] from an
earlier revision of this work where tc's priority was reused and exposed via
BPF uapi as a way to coordinate dependencies among tc BPF programs, similar
as-is for classic tc BPF. The feedback was that priority provides a bad user
experience and is hard to use [1], e.g.:

  I cannot help but feel that priority logic copy-paste from old tc, netfilter
  and friends is done because "that's how things were done in the past". [...]
  Priority gets exposed everywhere in uapi all the way to bpftool when it's
  right there for users to understand. And that's the main problem with it.

  The user don't want to and don't need to be aware of it, but uapi forces them
  to pick the priority. [...] Your cover letter [0] example proves that in
  real life different service pick the same priority. They simply don't know
  any better. Priority is an unnecessary magic that apps _have_ to pick, so
  they just copy-paste and everyone ends up using the same.

The course of the discussion showed more and more the need for a generic,
reusable API where the "same look and feel" can be applied for various other
program types beyond just tc BPF, for example XDP today does not have multi-
program support in kernel, but also there was interest around this API for
improving management of cgroup program types. Such common multi-program
management concept is useful for BPF management daemons or user space BPF
applications coordinating about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_{FIRST,LAST}
      - Enforced throughout the bpf_mprog state's lifetime
      - Admin override possible (e.g. link detach, prog-based BPF_F_REPLACE)
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space daemon can query current state with revision, and pass it along
    for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure) and bpf_mprog_cp (control-path
structure). Both have been separated, so that fast-path gets efficient packing
of bpf_prog pointers for maximum cache efficieny. Also, array has been chosen
instead of linked list or other structures to remove unnecessary indirections
for a fast point-to-entry in tc for BPF. The bpf_mprog_entry comes as a pair
via bpf_mprog_bundle so that in case of updates the peer bpf_mprog_entry
is populated and then just swapped which avoids additional allocations that
could otherwise fail, for example, in detach case. bpf_mprog_{fp,cp} arrays are
currently static, but they could be converted to dynamic allocation if necessary
at a point in future. Locking is deferred to the in-kernel user of bpf_mprog,
for example, in case of tcx which uses this API in the next patch, it piggy-
backs on rtnl. The nitty-gritty details are in the bpf_mprog_{replace,head_tail,
add,del} implementation and an extensive test suite for checking all aspects
of this API for prog-based attach/detach and link API as BPF selftests in
this series.

Kudos also to Andrii Nakryiko for API discussions wrt Meta's BPF management daemon.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net/
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [utsavr96/config-server](https://github.com/utsavr96/config-server)@[8aa965c79b...](https://github.com/utsavr96/config-server/commit/8aa965c79b5def9aba18b874e34f0aa5ac315221)
#### Thursday 2023-06-08 13:36:27 by Utsav

Merge branch 'main' of https://github.com/utsavr96/config-server into main

fuck you# the commit.

---
## [Jolly-66/dragon-station](https://github.com/Jolly-66/dragon-station)@[ddd018f4d5...](https://github.com/Jolly-66/dragon-station/commit/ddd018f4d54fcb2917ca9cbf71a913a3bafc7900)
#### Thursday 2023-06-08 14:00:10 by SkyratBot

[MIRROR] Changes syndicate surgery duffelbags to contain advanced tools [MDB IGNORE] (#21619)

* Changes syndicate surgery duffelbags to contain advanced tools (#75846)

## About The Pull Request

Changes syndicate surgery duffelbags to contain advanced tools.

In total, they contain
- All advanced surgical tools, alongside the normal ones without an
advanced version
- Sterilizine gel
- Bone gel and surgical tape
- Roller bed
- Straight jacket, muzzle, and MMI

Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.

The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.

## Why It's Good For The Game

> Changes syndicate surgery duffelbags to contain advanced tools.

> In total, they contain (...)

The only real reason to buy this item is for the increased storage space
the duffelbag gives, and I find that a little sad. Surgical tools are
plentiful, as they can either be lathed from cargo, medbay, or just
taken. A surgeon, the role that *should* thematically need this the
most, has absolutely no reason to take it. Now they do! A full set of
advanced tools is certainly something that can be considered for
purchase, especially with all the bonus items in here - which might just
allow a traitor to repair their bones if they're heavily wanted and
licking their wounds in maintenance. The TC cost has been increased to 4
to compensate.

> Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.

Similar to above, but instead, the reasoning is that nukies really do
not have a lot of time to do surgery. A lot of the 20 minutes of prep
time in War is spent figuring out what you're buying with your
exorbitant amount of TC, in non-War you don't really want to delay the
mission for five minutes for surgery, and its hassle means that most
people do not really want to bother with things like nerve threading,
etc. due to the large, annoying time cost.

> The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.

The former is because, well, what the hell, why didn't it have one!
Removing the loose tools gave me the space for it. The latter is just me
realizing that empty closet is weird and lame and so I gave it some
fluff contents to give it a reason to exist.

## Changelog

:cl:
add: Changes syndicate surgery duffelbags to contain advanced tools,
sterilizine, surgical tape, and a roller bed.
add: Changed the Syndicate Infiltrators' surgery areas to contain a full
syndicate surgery duffelbag.
add: The normal infiltrator now has a operating computer and a closet of
misc. surgical clothing and anesthesic tank.
/:cl:

* Changes syndicate surgery duffelbags to contain advanced tools

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [DinoDefend/gorilla](https://github.com/DinoDefend/gorilla)@[f3ce849a8c...](https://github.com/DinoDefend/gorilla/commit/f3ce849a8c46f5683477ff26ec34dc04518c294b)
#### Thursday 2023-06-08 14:08:35 by Shishir Patil

Releasing Torch and TF weights 🚀  (#16)

In this PR we release the weights for Gorilla 0-shot model for Torch Hub
and Tensorflow Hub APIs 🎉

It chooses from 626 (exhaustive) TensorFlow v2 APIs, and 94 (exhaustive)
Torch Hub in a 0-shot fashion (without any retrieval). In the spirit of
being open, we do not filter, nor carry out any post processing either
to the prompt nor response 🎁 We would like to remind the community that
neither of `gorilla-7b-hf-v0`, `gorilla-7b-tf-v0`, nor
`gorilla-7b-th-v0` have any generic chat capability. We do have a model
with all the 1600+ APIs which also has generic chat capability, which we
release slowly to accommodate server demand.

You can play around with Gorilla either through our hosted colab (OpenAI
Chat completion API compliant) or you can download and run it locally.

Thank you for all the comments and suggestions so far! Keep them
coming!!!

🚀 🚀 🚀

---
## [rsuppersahabatan/cockpit](https://github.com/rsuppersahabatan/cockpit)@[79d6a888d4...](https://github.com/rsuppersahabatan/cockpit/commit/79d6a888d43a1544ec275c7681cc699abdd698f0)
#### Thursday 2023-06-08 15:04:06 by Martin Pitt

pybridge: Fix clobbering remote user set in SSH config

When opening a remote host channel without `user`, stop assuming the
current local user name, as that overwrites any `User` field in
the SSH configuration.

Instead, we need to do the opposite: for an unknown host, the UI will
not set a `user` field in the channel options, but for an actual login
attempt with a password it will. We need to treat them as the same
channel in the `self.remotes` map. The C bridge deals with this in
cockpit_router_normalize_host_params() by disregarding the `user` field
if it is equal to the current user name.

This is a rather silly hack for backwards compatibility, but while we
have two bridges, let's rather stay bug-for-bug compatible and clean
this up in the UI only after we drop the C bridge.

There is one extra tweak: `rpartition()` returns an empty string, but
we can't pass that on literally. So turn those into `None`.

Fixes #18714

---
## [CsabaVas44/Armored_Rampage](https://github.com/CsabaVas44/Armored_Rampage)@[375ef39cba...](https://github.com/CsabaVas44/Armored_Rampage/commit/375ef39cba0aeaf3629d7691a6dce4c7e9db7264)
#### Thursday 2023-06-08 15:13:30 by Karikó-Tóth Máté

xd

I'm chilling to my tunes Neighbours complaining again
You lot knocking at my door's really fucking up my Zen
I take one look at my phone I got textes from my friend
Telling me about this rave I'm like cool bro where and when
Can we get in with balloons he said dunno it depends
Made a call an called me back "I'm finding out man give me ten"
Pack my stuff get in my car
Blasting tunes from start to end
Neighbours taking pics of me like I won't come and smash your lens
Point this middle finger at you like what the fuck can you do
You can call the feds I'll slam my door like F you to
I'm like what's the matter it's a banger of a tune
Me apologise? You crazy loon ain't thought this through
Must be off your trolley
I don't bow down to no body
Must be off your trolley
I don't bow down to no body
Must be off your trolley
I don't bow down to no body
About I'm trying to watch my Corrie
Well I'm sorry not sorry
Sorry im not sorry
I'm having the time of my life what do you want me to say
Gimme the mic I run up on stage
I Give em a flow they gimme a wave
At any time I pick up the pace
Ramming the place it's getting in insane
Selling balloons supplying the rave
Gimme a five I'll give you a taste
Breaking laws I want a raise
F an award gimme the pay
Gimme the cash gimme the car
Gimme the yard that comes with a lake
Gimme a girl that gimme it sloppy
Gimme a label that does it properly
This is work this ain't a hobby
So I'm sorry I'm not sorry
Sorry im not sorry
I'm chilling to my tunes Neighbours complaining again
You lot knocking on my door's really fucking up my Zen
I take one look at my phone I got textes from my friend
Telling me about this rave I'm like cool bro where and when
Must be off your trolley
I don't bow down to nobody
Must be of your trolley
I don't bow don't to nobody
Must be off your trolley
I don't bow down to nobody
About I'm trying to watch my Corrie
Well I'm sorry not sorry
Sorry im not sorry
Must be off your trolley
I don't bow down to nobody
Must be off your trolley
I don't bow down to nobody
About I'm trying to watch my Corrie
Well I'm sorry not sorry

---
## [jwdat/Mad-Libs](https://github.com/jwdat/Mad-Libs)@[3e982ce864...](https://github.com/jwdat/Mad-Libs/commit/3e982ce8647908e2897d7f8ad94cc11f4fd9a9b7)
#### Thursday 2023-06-08 15:59:06 by Jawdat Tayfour

This is the simple code for a three choice Mad Lib

In the vast expanse of linguistic playfulness and intellectual amusement, behold the wondrous concoction known as the Mad Libs game—a tapestry woven from the threads of language and creativity. Like a masterfully crafted symphony of words, it invites participants to embark upon an epic journey of literary collaboration.

With pens poised and minds ablaze, players delve into a realm where nouns, verbs, adjectives, and adverbs reign supreme. They navigate through a labyrinth of whimsical prompts, each one a portal to uncharted realms of possibility. As the game unfolds, the sacred blanks beckon, eager to be adorned with the vibrant hues of their lexical counterparts.

Within this realm, participants don the noble mantle of storytellers, channeling the power of their imagination to complete the tapestry. With each carefully selected word, they shape the narrative, injecting it with their own unique essence. The game, much like a vibrant ecosystem, thrives on the diversity of contributions, as each player's linguistic brushstrokes meld harmoniously, culminating in a masterpiece of collaborative creation.

The Mad Libs game serves as a temple to the beauty of language, transcending mere syntax and grammar. It celebrates the intrinsic joy of words, allowing players to revel in the sheer delight of linguistic juxtapositions and unexpected combinations. As the symphony of laughter and camaraderie resounds, minds ignite with delight, forging connections between seemingly disparate elements of the lexicon.

In this sacred arena, nerds and wordsmiths find solace, their shared affinity for language transformed into an immersive experience. The Mad Libs game beckons, drawing them into its embrace—a haven where puns are cherished, alliterations dance, and similes soar through the ether. Here, the boundaries of language blur, and imagination takes flight, unfettered by the constraints of conventional storytelling.

So, let your creativity unfurl its wings and join this captivating odyssey of lexicon and mirth. Embrace the challenge of filling the void with your chosen linguistic treasures, for within the Mad Libs game lies a world of boundless enchantment, where words become the paintbrushes of the soul and laughter the orchestra that fills the air.

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[92e317a930...](https://github.com/pytorch/pytorch/commit/92e317a930e7a6f455800d3d22ba9222e62e4d54)
#### Thursday 2023-06-08 16:29:36 by Joel Schlosser

Update base for Update on "(WIP; DO NOT REVIEW) Use python tensor subclass version of NT for PT2"


I'm out next week so I'm dumping some stuff here for whoever is interested. Added some notes inline. Other things:
* Main idea: convert real NT -> fake / meta instance of `NestedTensor` python tensor subclass during tracing and use that throughout the rest of the PT2 stack
* Python tensor subclass only supports contiguous for now
    * Only need `sizes` because of this, and `sizes` is a dim-length list containing int / List[int] items (for ragged dims) OR SymInts for dynamic shapes (will probably only support this case anyway)
* Inference-only for now; ignore Autograd
* Skip functionalization on NTs for now (there's no in-place op support anyway, although we should ideally handle NT <-> T views within functionalization)

Example script:
```python
import torch
from torch.nested import nested_tensor
from torch.nested._nested_tensor import NestedTensor
from torch._inductor import debug

torch._inductor.config.debug = True
torch._dynamo.config.traceable_tensor_subclasses.add(NestedTensor)

device = 'cuda'

def make_tensor(*shape, device=device, dtype=torch.float32):
    return torch.randn(*shape, device=device, dtype=dtype)

torch.manual_seed(1)

def fn(x, x_offsets):
    x_nt = torch._nested_view_from_jagged(x, x_offsets)
    x_nt = x_nt + 69
    x_nt = x_nt * 42
    return x_nt

torch._dynamo.disallow_in_graph(torch.diff)

compiled_fn = torch.compile(fn)

# shape (sum(*), D)
# component shapes: (3, 5), (4, 5), (6, 5)
x = make_tensor(13, 5)
x_offsets = torch.tensor([0, 3, 7, 13], dtype=torch.int64, device=device)

# helps create dynamic graph right away
torch._dynamo.mark_dynamic(x, 0)
torch._dynamo.mark_dynamic(x_offsets, 0)

output = compiled_fn(x, x_offsets)

# shape (sum(*), D)
# component shapes: (2, 5), (6, 5), (4, 5), (5, 5)
y = make_tensor(17, 5)
y_offsets = torch.tensor([0, 2, 8, 12, 17], dtype=torch.int64, device=device)

output2 = compiled_fn(y, y_offsets)

print(output)
print(output2)
```

WARNING: AWFUL HACKS AHEAD. DO NOT REVIEW YET.

cc soumith voznesenskym penguinwu anijain2305 EikanWang jgong5 Guobing-Chen XiaobingSuper zhuhaozhe blzheng Xia-Weiwen wenzhe-nrv jiayisunx peterbell10 desertfire

[ghstack-poisoned]

---
## [Saikikusuoisgood/ShiNeaL](https://github.com/Saikikusuoisgood/ShiNeaL)@[cd039664df...](https://github.com/Saikikusuoisgood/ShiNeaL/commit/cd039664df707eab927d5b0984bd11ea251f1271)
#### Thursday 2023-06-08 17:35:18 by Saikiisdone

french translation

The Hog Rider card is unlocked from the Spell Valley (Arena 5). He is a very fast building-targeting, melee troop with moderately high hitpoints and damage. He appears just like his Clash of Clans counterpart; a man with brown eyebrows, a beard, a mohawk, and a golden body piercing in his left ear who is riding a hog. A Hog Rider card costs 4 Elixir to deploy.
Strategy
His fast move speed can boost forward mini tanks like an Ice Golem in a push. At the same time, he can also function as a tank for lower hitpoint troops such as Goblins as he still has a fair amount of health. Most cheap swarms complement the Hog Rider well, as they are nearly as fast as him and usually force more than one card out of the opponent's hand.
The Hog Rider struggles with swarms, as they can damage him down and defeat him quickly while obstructing his path. Barbarians in particular can fully counter him without very strict timing on the defender's part, though be wary of spells.
A Hunter can kill the Hog Rider in 2 hits if placed right on top of it. However, if you place something in front of the Hog Rider, the Hunter's splash will damage the Hog Rider and hit the card in front of it more.
The Hog Rider in conjunction with the Freeze can surprise the opponent and allow the Hog Rider to deal much more damage than anticipated, especially if the opponent's go-to counter is a swarm, or swarms are their only effective counter to him. Skeletons and Bats will immediately be defeated by the spell, while Spear Goblins, Goblins, and Minions will be at low enough health to be defeated by a follow up Zap or Giant Snowball.
However, this strategy isn't very effective against buildings as the Hog Rider will take a while to destroy the building, giving the opponent ample time to articulate another counter.
Against non-swarm troops, it can deal a lot of damage during the freeze time, but this can allow the opponent to set up a massive counterpush. For this reason, players should either only go for a Hog Rider + Freeze when they have other units backing it up from a counterattack, or if the match is about to end and they need to deal as much damage as possible.
It is not a good idea to send in a Hog Rider simply to destroy a building, especially if it is the only building targeting unit available, as defeating Crown Towers becomes substantially more difficult. Spells or simply waiting out the lifetime of the building are more effective. The exception to this is an Elixir Collector placed in front of the King's Tower. If a Hog Rider placed at the bridge, he can destroy the Collector for a positive Elixir trade, though the damage from both Princess Towers will usually mean he does not survive to deal any damage to them. However, if the opponent sends in defending troops, it can be an opportunity to gain spell damage value.
In a deck with several low-cost cards, it might be worth it to simply send the Hog Rider against one building. These decks shuffle their card rotation quick enough, that they will arrive to their next Hog Rider before the next building arrives in the opponent's card rotation.
Long-ranged troops like Musketeer and Flying Machine can snipe those buildings, preserving some of the Hog Rider's health, possibly allowing it to get some Tower damage.
When there are buildings placed in the middle to counter the Hog Rider, understanding the placement of the Hog Rider and the type of building placed can help the Hog Rider to bypass certain buildings.
Passive buildings such as spawners and Elixir Collector have a larger hitbox than defensive buildings; which means that if a passive building was placed 3 tiles away from the river in the middle of the opponent's side, then it is impossible for the Hog Rider to bypass that placement as the Hog Rider will get pulled to that building.
Defensive buildings have a smaller hitbox than a passive building, which means if that if a defensive building was placed three tiles away from the river in the middle of the opponent's side, a Hog Rider placed at the very left or right side of the Arena may be able to bypass it due to its smaller hitbox.
If the player has a building already placed down in the center of the arena, and the opponent tries to bypass it with a Hog Rider at the edge of the arena, they can use certain air troops to push the Hog Rider towards the building as it jumps over the river, effectively denying the bypass attempt. They must be already hovering over the correct placement, as very quick reflexes are required to correctly perform this technique.
For Bats, Skeleton Dragons, and Minion Horde, they should be placed right in front of the Hog Rider as soon as it is deployed.
For Minions, Skeleton Barrel, Mega Minion, Flying Machine, Electro Dragon, Baby Dragon, Inferno Dragon, Balloon, and Lava Hound, stagger the above placement one tile to the right if the Hog Rider is placed on the left side of the arena, and vice versa.
They can also use ground troops to achieve the same result. Something like an Ice Golem deployed at the Hog Rider’s landing spot will obstruct his path and force him to go around the unit, which causes him to be closer to the building instead of the Crown Tower.
The Hog Rider can kite Very Fast non-building targeting troops due to his own Very Fast speed and building only targeting if he is placed on the fourth tile from the bridge, slightly into the opposite lane. He can also stall grounded units when placed right at the bridge. He will pull them towards him while deploying, and then be untargetable by them when he jumps over the bridge. After landing, he will pull them back. This can be useful when the player needs to deal damage in the same lane they are defending. It will also help separate troops behind a tank in a large push.
A Tornado placed on the second tile front of the player's King's Tower and staggered two tiles towards the Princess Tower will activate it without any damage dealt to the Princess Tower, helping them in defending future pushes. This can also be a method of mitigating all damage dealt to a Princess Tower, but doing this more than three times may result in the King's Tower's health being low enough to be targeted directly, opening up the possible threat of a back door three crown. A better alternative is to pull the Hog away from the Princess Tower into the attacking range of all three Crown Towers, which will negate all damage as long as none of them are already distracted
A very powerful combo is the Hog Rider, the Musketeer, and the Valkyrie, typically referred to as the Trifecta. The Musketeer will defend against most troops, while the Valkyrie can protect her and the Hog Rider from swarms or high damage units. The Hog Rider is used to deal damage to the tower.
This can be effectively countered by Lightning, one-shotting the Musketeer and severely damaging both the Valkyrie and Hog Rider. The Minion Horde is also effective, but the enemy can Zap them and the Musketeer will one-shot them all. Even if the Musketeer is defeated, the Hog Rider and Valkyrie will have enough time to severely damage the Tower.
The Hog Rider should be placed behind the Valkyrie to give it a boost so that it stays in front of the Hog Rider, protecting it.
A Hog Rider combined with a Goblin Barrel can be awkward for the opponent to defend against. Timing it so that the Hog Rider is tanking the tower shots for the Goblins is the most effective way to deal damage. However, a Barbarian Barrel can shut this down with minimal Tower damage for a positive Elixir trade, as long as the Goblin Barrel was placed directly on the Tower.
Pairing the Hog Rider with the Balloon can deal devastating damage. If executed properly, the Hog Rider will act as a tank while the Balloon threatens to deal massive damage. The Hog Rider can also destroy any buildings attempting to slow down the combo. However, this combo is very vulnerable to swarms and anti-air cards as neither of the troops target anything but buildings. Additionally, they are easy to separate, due to the disparity in move speeds. Alternatively, the Hog Rider and the Balloon can be played in different lanes to spread the opponent's defenses thin. However, a building or Tornado can bring them back together for an easier defense.
The Hog Rider can be paired with the Lumberjack as both a swarm bait and damage combo. It is a very fast combo with an extremely high damage output potential, so the enemy will likely try to counter it with a swarm. If this happens, use a spell like Arrows to render the opponent defenseless. If they manage to defeat the Lumberjack, the dropped Rage will make the Hog Rider even more dangerous than it normally is.
A fast and deadly combination is the Hog Rider and Mini P.E.K.K.A. combo. Both units are fast but the Mini P.E.K.K.A. does much more damage and does not attack only buildings so the Mini P.E.K.K.A. can deal with troops like the Executioner and Musketeer. However, this combo can be defeated with swarms like Skeleton Army, which will defeat both of them since neither of them can deal area damage. They are also unable to target air troops, so the Minion Horde can stop this easily.
A risky play is to deploy the Hog Rider at the bridge as soon as the match starts. If the opponent does not react fast enough, the Hog Rider will deal a significant amount of damage to the Princess Tower. This can also allow the player to quickly scout the opponent's deck if they happen to react to him fast enough.
⠀⠀⠘⡀⠀⠀HOG RIDAAAAAA⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀
⠀⠀⠀⠑⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⠊⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠤⠄⠒⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣀⠄⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠉⢈⠩⢙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⠠⠀⠀⠨⠐⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢐⠐⠌⡌⢄⢐⢈⠔⡝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡏⠉⡀⠐⡀⢁⠈⠐⠱⠑⡑⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⢗⠀⠀⠐⡠⡛⠔⡁⢜⡔⡬⢎⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠡⠀⠀⠀⠀⠂⠁⠀⠄⢂⠈⠂⢂⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⢟⠩⠐⡀⠀⠀⠀⠐⠐⠁⠓⠒⠒⢀⠁⢐⢝⢟⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠫⠡⠡⠨⢀⠂⠠⠀⠀⢁⠑⡱⠛⠗⡓⢂⠠⢸⢸⢨⠣⡝⣻⣿⣿⣿⣿⣿⣿
⣿⢏⢐⢁⠊⢌⠐⡈⠄⠠⠀⠀⠀⠀⠁⠑⠈⠀⢄⢕⠸⡨⠪⡪⡘⣻⣿⡿⣿⣿⣿
⣿⢂⠂⡂⠅⡂⠅⡐⠨⢐⠐⠠⠠⡀⢄⠠⡠⡡⡱⡐⠕⢌⢊⢆⢣⢒⠽⢿⣿⣿⣿
⠣⢂⠂⠄⠡⠐⠐⠈⠌⡐⠨⡈⠢⠨⡂⢌⢂⠆⡪⠨⡊⠂⡂⠢⢡⣢⣣⡣⣍⢿⣿
⠨⢂⢂⠁⡀⠀⠀⠁⠐⠈⠐⠈⢈⠈⠐⡀⠄⠁⠌⠈⠔⣄⡀⠠⡑⡂⠆⠢⢂⠑⠽
⡨⠐⠀⠀⠀⢠⡎⡀⠀⠀⠄⠈⡀⠌⠐⠠⠈⠄⡁⠂⡀⡫⠑⣑⠀⢂⠌⠄⢕⠀⠨
⠺⡪⠢⡀⠀⠞⢇⢂⠀⠂⡀⠠⠀⠄⠁⠌⠨⠀⢄⠢⡁⢂⢿⡟⡀⠀⠈⠈⡀⠂⣰
⢀⢀⠀⠄⠀⠀⡐⠀⡈⠄⡐⠅⡊⠌⢌⠄⡕⡑⡁⢂⠂⢂⠸⣿⡄⠀⠈⣠⣴⣿⣿
⢐⠔⠠⠀⠀⡐⠠⢈⠢⢑⠄⠑⢈⠊⡂⡱⢁⣂⢌⢔⢌⢄⠀⠹⢀⣺⡿⣟⢿⣿⣿
⢀⠡⠁⠂⠐⠠⠈⠄⢈⠠⢈⢢⡣⣗⠕⠄⣕⢮⣞⣞⣗⣯⢯⡷⡴⣹⡪⣷⣿⣿⣿
⠊⠄⠠⠠⠡⠈⠠⢐⠠⡊⡎⣗⢭⢐⠹⡹⣮⡳⡵⣳⣻⢾⣻⣽⣻⣺⣺⣽⣿⣿⣿
⣨⣾⢐⠰⠐⠅⡂⡂⢕⢜⢜⢵⢹⢑⢔⠨⢘⠸⡹⡵⣯⣻⢽⣳⣻⣺⢞⡿⣿⣿⣿
⣿⣿⡔⠠⢈⠐⠐⢠⢱⢸⢸⢸⢸⠰⡡⢘⢔⢕⠝⢮⣳⢽⢝⡾⡵⡯⣏⠯⣿⣿⣿
⣿⣿⣗⢅⢢⠠⠡⠢⡱⡑⡕⡕⢅⠣⡊⢨⢪⡣⡣⡂⡬⡳⢽⢽⢽⢽⣞⣧⠙⣿⣿
⡻⣿⡯⡪⠢⡡⠡⢑⢌⠪⡪⡊⠆⢌⠪⢐⢕⢱⢱⢱⢱⢱⢙⢮⡫⡟⣞⢮⣳⠙⣿
⠊⣿⣯⠪⡊⠄⢅⠂⢂⠁⢇⢇⢃⠂⢕⠐⠌⡲⡰⡡⣇⠇⢇⢕⠪⠉⠂⠅⠂⡑⠹
⣸⢿⣳⢱⠨⡐⡽⡿⡶⡾⡬⡢⢂⠅⡢⢡⣌⠐⠈⢎⢎⢎⢔⠠⠡⠠⠠⠡⡁⡂⠡
⡯⡯⡇⢅⠕⠠⢱⢹⡙⢮⢹⠨⡂⡂⢇⠌⠮⡳⠅⡂⢕⠡⡑⠠⢁⢁⣡⣡⣢⣶⣿
⣗⢽⢌⡢⡡⡡⡸⡢⡣⡣⡱⡑⠔⡈⢎⢆⢂⠂⠅⣢⡳⣽⡐⢅⢂⣊⣿⣿⣿⣿⣿
⣯⢯⢷⢽⢮⢯⣺⣪⢞⡮⣳⢘⠔⢌⢜⣞⣖⣮⣻⢮⣯⢷⣿⣻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

---
## [Jawdat-Tayfour/Rock-Paper-Scissors](https://github.com/Jawdat-Tayfour/Rock-Paper-Scissors)@[63b817bfe6...](https://github.com/Jawdat-Tayfour/Rock-Paper-Scissors/commit/63b817bfe6fcdec14dc9a5b472a77bbab4fc8b22)
#### Thursday 2023-06-08 17:51:51 by Jawdat Tayfour

The code for the game.

In the realm of strategic choices and spontaneous gestures, a timeless battle unfolds—the exhilarating game of Rock-Paper-Scissors, where a human player faces off against a cunning digital adversary. With each poised hand and calculated maneuver, players engage in a captivating duel of wits and intuition.

As the stage is set, the human player and the computer lock eyes, their minds prepared to unleash their chosen arsenal of gestures. The rules are simple, yet the possibilities are boundless. Rock, the symbol of strength and resilience, poised to crush its opponents. Paper, the embodiment of tact and versatility, ready to envelop and conquer. Scissors, the epitome of precision and cunning, poised to slice through the opposition.

With a synchronized countdown, both participants unveil their selections, their hands shaping the destiny of the impending clash. The human player, their senses heightened, channels their intuition and strategic acumen, seeking to anticipate the computer's next move. The digital adversary, an algorithmic oracle, calculates probabilities and patterns, aiming to outwit its human challenger.

Rock collides with paper, the sound reverberating through the air—a victory for paper, leaving the rock shattered in defeat. Scissors meet rock, a resounding triumph for the unyielding stone. Paper encounters scissors, its fragile form yielding to the sharp blades—a victory for the wielder of scissors. Victory and defeat intertwine in a mesmerizing dance, each outcome a testament to the calculated choices made.

Round after round, the players engage in an intricate interplay of deduction and risk. The human player embraces the delicate balance of strategy and intuition, attempting to discern patterns or exploit the computer's potential tendencies. The computer, an unyielding digital adversary, harnesses its computational might to analyze the probabilities and optimize its choices, ever watchful for the patterns that might guide its path to triumph.

As the game unfolds, a tapestry of anticipation and excitement weaves itself into the fabric of the battle. The ebb and flow of victories and defeats give rise to a sense of exhilaration, fueling the competitive spirit that courses through the veins of both human and machine. Laughter and shouts of triumph fill the air, as each victory is celebrated and each defeat met with newfound determination.

And in the final clash, as the game draws to a close, the participants reflect upon the riveting contest of Rock-Paper-Scissors against the computer. They revel in the sheer joy of the unexpected, the thrill of outsmarting their digital foe or being outwitted by its calculating cunning. For in this elemental game, the human spirit dances alongside the digital realm, an ode to the unending quest for strategic mastery and the sheer delight of friendly competition.

So, embrace the challenge, summon your intuition, and engage in the enthralling game of Rock-Paper-Scissors against the computer. Let the clash of symbols and the dance of choices ignite your spirit, and revel in the timeless battle of wits that transcends the boundaries between human and machine.

---
## [vampirebat74/lobotomy-corp13](https://github.com/vampirebat74/lobotomy-corp13)@[dd0a22918c...](https://github.com/vampirebat74/lobotomy-corp13/commit/dd0a22918c6f9079be658ff9641e858bd3daa8f8)
#### Thursday 2023-06-08 18:10:34 by Mr.Heavenly

Tool ego

adds tool E.G.O

removes a extra line

fixes shit

swindle

voce

divinity

fixes shit

shifts divinity down a few pixels

This is the fourth time this same commit was made

I hate TG so fucking much like it's unbelievable why does this only fuck up on my PC? WHY?

hyde weapon

stuff

hyde code

---
## [GPeckman/tgstation](https://github.com/GPeckman/tgstation)@[2068ea9ab5...](https://github.com/GPeckman/tgstation/commit/2068ea9ab53803557b5e48cddbe57205f4c4792e)
#### Thursday 2023-06-08 18:14:39 by SyncIt21

Crate, Closet Refactors & Access Secured Stuff  (#74754)

## About The Pull Request
This PR is actually 2 parts, one that fixes runtimes with crates & the
other that allows secured closets to be crafted
along with a secured suit storage unit

**Crate Fixes**

Fixes #74708

The problem starts here

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L31-L34
Not only does this if condition look ugly but it's highly error prone
because one single call to `update_appearance()` can cause this to fail,
and sure enough if you look at the parent `Initialize()` proc it calls
just that

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L81-L88
Since we know the appearance is guaranteed to be changed in some way
before the if condition gets executed let's check what the final state
of the crate would be before this if check

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L54-L56
We see that the final icon state depends on the variable `opened` so if
we want to place/spawn a crate that is opened at round start we have to
ensure that `opened = TRUE` so the `if(icon_state ==
"[initial(icon_state)]open")` succeeds and does its job correctly.
Sadly we did dum shit like this
```
/obj/structure/closet/crate{
	icon_state = "crateopen"
}
```
throughout the entire code base, we thought backwards and were only
concerned in making the closet look open rather than setting its correct
variables to actually say that it is opened. because none of these
crates actually set `opened = TRUE` the final icon state becomes just
"crate" NOT "crateopen" therefore the if condition fails and we add the
component

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L36-L37
with the wrong parameters, so when closing the closet after_close()
removes the component with the wrong arguments

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L81-L84
that is does not unregister the signals and readds the component i.e.
re-registers the signals causing runtime.

The solution just do this
```
/obj/structure/closet/crate/open[mapping helper]
```
To clearly state that you want the closet to be open, that way you don't
have to memorize the icon_state for each different type of crate, it's
consistent across all crates & you don't get runtimes.

And that's exactly what i did everywhere

Another issue that is fixed is "Houdini crates" i.e. crates which are
open & appear empty but when you close & reopen them magical loot
appears, Go ahead walk upto to cargo and find any empty crate that is
open and do this

Fixes #69779


https://user-images.githubusercontent.com/110812394/232234489-0193acde-22c8-4c19-af89-e897f3c23d53.mp4

You will be surprised, This is seriously harmful to players because they
can just walk by a crate that appears to be open & empty only to realize
later that it had some awesome loot. Just mean

The reason this happens is because of the Late Initialization inside
closets

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L85-L86

What late initialization does is suck up all stuff on its turf

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L97-L100

In theory this is supposed to work perfectly, if the closet is closed
move everything on the turf into the closet and so when the player opens
it, they all pop back out.
But what happens if the closet is opened before ` LateInitialize()` is
called? This breaking behaviour is caused by object spawners

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/effects/spawners/random/structure.dm#L94-L100
And maint crates

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L141-L143
These 2 spawners open up the crate based on random probability before `
LateInitialize()` is called on the crate and so what happens is the
crate is first opened and then stuff on the turf is sucked in causing an
open but empty crate to appear.

The solution is simple just check again in ` LateInitialize()` if our
crate is still closed before we proceed.That's fixed now too

**Code Refactors**
1. Introduced 2 new signals COMSIG_CLOSET_PRE/POST CLOSE which are the
counter parts for the open signals. hook into them if you ever need to
do stuff before & after closing the closet while return BLOCK_CLOSE for
COMSIG_CLOSET_PRE_CLOSE if you want to block closing the closet for some
reason
2. 2 new procs `before_open()` & `before_close()` which are the counter
parts for `after_open()` & `after_close()`. If you need to write checks
and do actions before opening the closet or before closing the closet
override these procs & not the `open()` & `close()` procs directly

**Secured Craftables** 
This is just a reopened version of #74115 after i accidently merged
another branch without resolving the conflicts first so i'll just
repaste everything here, since crates & closets are related might as
well do all in one

1. **Access secured closets**
   
   - **What about them?**
          **1. Existing System**
If you wanted to create a access secured closet with the existing system
its an 4 step process
            - First construct a normal closet
            - Weld it shut so you can install the airlock electronics
            - Install the electronics [4 seconds]
            - Unweld
This is a 4 step process which takes time & requires a welding tool
         **2. New system**
Combine the 4 steps into 1 by crafting the secure closet directly
                    
![Screenshot
(184)](https://user-images.githubusercontent.com/110812394/235904926-c2ea231c-eba7-45d0-a5af-e0456fdd40bc.png)

    - **Bonus Features**
              **1. Card reader**
The card reader acts as an interface between the airlock electronics &
the player. Usually if you want to change access on a locker you have to
                  - Weld the closet shut
                  - Screw driver out the electronics
                  - Change the settings
                  - Install it back
                  - Unweld
With a card reader there is no need of a welder & screwdriver. You can
change the access of the locker while its operational

        **How do i install the card reader?**
             1. Weld the closet shut
             3. Insert card reader with hand
4. To remove the card reader use crowbar or just deconstruct the whole
closet with a welding tool
             5. Unweld closet

         **How to change its access?**
This will overwrite the settings on your airlock electronics. To do this
1. make sure the closet is first unlocked. This is important so that no
random person who doesn't have access to the closet can change its
access while its locked. It would be like giving the privilege of
changing your current password without first confirming if you know the
old password
2. attack/swipe the closet with your PDA. Make sure your ID card is
inside the PDA for this to work. You can also just use your ID card
directly without a PDA
         3. You will get 3 options to decide the new access levels
           
![Screenshot
(174)](https://user-images.githubusercontent.com/110812394/233454364-d99a2fb6-9f26-4db3-9fac-a10689955484.png)


        They work as follows
- **Personal**: As the name implies only you can access this locker and
no one else. Make sure to have your ID on you at all times cause if you
loose it then no one can open it
- **Departmental**: This copies the access levels of your ID and will
allow people having those exact same access levels. Say you want to
create a closet accessible to only miners. Then have an miner choose
this option and now only miners can open this closet. If the Hop sets
custom access on your ID then only people with those specific access
levels can open this closet
         - **None**: No access, free for all just like a normal closet

**Security:** After you have set the access level it is important to
lock the access panel with a "multi-tool", so no one else can change it.
Unlock the panel again with the "multi-tool" to set the new access type

       **2. Give your own name & description**
To rename the closet or change its description you must first make the
closet access type as personel i.e. make it yours, then use an pen to
complete the job. You cannot change names of departmental or no access
closets because that's vandelism

       **3. Custom Paint Job**
    Use airlock painter. Not intuitive but does the job. 
   
![Screenshot
(181)](https://user-images.githubusercontent.com/110812394/234202905-00946b88-2513-489d-b0a2-d618a72f3e49.png)

      **4. Personal closets**
Round start personal closets can have their access overridden by a new
ID when in it's unlocked state. This is useful if the last person has no
use for the closet & someone else wants to use it.


    - **Why its good for the game?**      
1. Having your own personal closet with your own name & description
gives you more privacy & security for your belongings so people don't
steal your stuff. Personal access is more secure because it requires you
to have the physical ID card you used to set this access and not an ID
which has the same access levels as your previous ID
2. Make secure closets faster without an welding tool & screw driver
3. Bug fix where electronics could be screwed out from round start
secured closets countless times spawning a new airlock electronic each
time
      
2. **Access secured freezers**

    - **What about them?**
The craftable freezer from #73942 has been modified to support secure
access. These can be deconstructed with welders just as before

![Screenshot
(185)](https://user-images.githubusercontent.com/110812394/235905000-ba165feb-4384-4759-b46b-dba77c9e6ba3.png)


    - **How does it work?**
The access stuff works exactly the same as secure closets described
above. You can rename & change description with pen just like the above
described secure closets. No paint job for this. Install card reader
with the same steps described above.

    - **Why it's good for the game?**
1. Make access secured freezers faster without a welder and screwdriver
2. Your own personally named & locked freezer for storing dead bodies is
always a good thing

4. **Access secured suit storage unit**
   - **What about them?**
Suit storage units now require airlock electronics for construction. The
access levels you set on it will be used to decide
       1. If a player can unlock the unit
       2. If the player can open the unit after unlocking
       3. If the player can disinfect whatever is inside
       
      By default all round start suit storage units have free access

   - **Install card reader**
Provides the same functionality as secured closets described above. To
install it
     1. Open its panel with a screw driver
     2. Add a card reader to it with hand
     3. Close the panel
     
     When you deconstruct the machine the card reader pops back out

   - **Why it's good for the game?**
1. Having your own access protected and named suit storage unit so
random people don't steal your mod suits? Who wouldn't want that.?
Provides security for department storage units.
2. If you have the unit locked then you cannot deconstruct the machine
with a crowbar providing additional security
3. Fixes #70552 , random people can't open/unlock the suit storage unit
without access. You can set personal access to make sure only you can
access the unit

## Changelog
:cl:
add: Access secured closets. Personal closets can have their access
overwritten by an new id in it's unlocked state
add: Access secured freezers.
add: Access secured suit storage units.
fix: Suit storage unit not having access restrictions.
fix: airlock electronics not properly getting removed after screwing
them out from round start lockers
fix: round spawned open crates run timing when closed
fix: open crates hiding stuff in plain sight
fix: open closets/crates sucking up contents during late initialize
causing them appear empty & open
/:cl:

---------

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [silicons/Citadel-Station-13-RP](https://github.com/silicons/Citadel-Station-13-RP)@[560b44d889...](https://github.com/silicons/Citadel-Station-13-RP/commit/560b44d889f06d0b724a1e4e9e298e3886c91be2)
#### Thursday 2023-06-08 18:42:01 by silicons

WHY DIDNT I JUST BUY FULLY INTO THE WEB DEV PLAGUE GOD FUCKING DAMNIT

---
## [Thunder12345/Skyrat-tg](https://github.com/Thunder12345/Skyrat-tg)@[bfb3967c90...](https://github.com/Thunder12345/Skyrat-tg/commit/bfb3967c908682e21202312d8b30ec17ad65e549)
#### Thursday 2023-06-08 19:18:23 by SkyratBot

[MIRROR] Adds proper armor for security plasmamen. [MDB IGNORE] (#21268)

* Adds proper armor for security plasmamen. (#75156)

## About The Pull Request
It's kinda strange that security plasmamen has no proper armor and you
can just bully them with bottlesmashes. Literally.
Also suits had no wound armor for some reason, which considering that
mold dies without hand kinda silly too.
And helmets just had no armor besides 1 melee armor.
## Why It's Good For The Game
Plasmamen security won't die that easilly. I mean, still easy to kill
them, but not that much.
## Changelog
:cl:
balance: Security Plasmamen now have Security armor. No bullying them
with bottlesmashes anymore.
/:cl:

* Adds proper armor for security plasmamen.

---------

Co-authored-by: Helg2 <93882977+Helg2@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[d1d23352eb...](https://github.com/cmss13-devs/cmss13/commit/d1d23352eb41452a98d0c66c7fbf5c5ea4143ffe)
#### Thursday 2023-06-08 20:10:29 by fira

Reduces SG Full Auto Scatter (#3556)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

It's been bugging me for a long time, but when you fire for a good dozen
seconds with the standard issue smartguns, the bullets start scattering.
So, so far you'll say, good Fira, that's soulful!

However, we have no ACTUAL recoil or similar mechanic. So letting go of
the LMB for just even 20 miliseconds is enough to reset scatter to start
of firing. **It's just a noobtrap with zero real gameplay elements.**

This reduces the max scatter so that bullets don't just start (after
EIGHTY shots!) spraying a (roughly) 48° angle cone, but instead 12°
which mostly stays on the same actual turfs. At this value the targeting
impact is vastly minimized, but the projectile visuals retain
significant scattering.

I don't think this ACTUALLY qualifies as a "balance" change due to how
irrelevant the "mechanic" was, but i'll slap it on.

# Explain why it's good for the game
Less of a noobtrap and pointless purely mechanical micromanagement so
people can focus on playing the game.

I'd rather we get a recoil mechanic to make this meaningful but it's bit
of a bigger problem...

# Changelog
:cl:
qol: Reduced USCM SG max scattering on Full Auto fire so you don't have
to periodically let go of the fire button to keep it from firing way
wide.
/:cl:

---
## [metamechanists/MetaLib](https://github.com/metamechanists/MetaLib)@[6c2a99c3a9...](https://github.com/metamechanists/MetaLib/commit/6c2a99c3a9a08261e271ef7816a0f022ea59ca57)
#### Thursday 2023-06-08 20:13:36 by MetaMechanists

Add removeDefaultItalics because fuck you Components

---
## [karlrackler/WebKit](https://github.com/karlrackler/WebKit)@[d6ae2528a9...](https://github.com/karlrackler/WebKit/commit/d6ae2528a9f3819005e08f9d5091ceff8b880fa8)
#### Thursday 2023-06-08 20:40:04 by Dean Jackson

WebXR: Severe aliasing in WebXR experiences (with WebGL1 contexts)
https://bugs.webkit.org/show_bug.cgi?id=256861
rdar://109424254

Reviewed by Dan Glastonbury.

WebXR sessions using WebGL1 contexts are unable to turn on
multisampling. I'm pretty sure this was my fault, but I can't
remember if it was intentional or a mistake. Either way it is
a bug.

Fix this by implementing the multisample renderbuffer creation
and resolution steps. Since we're doing this on a WebGL1 context,
the normal API will be invalid (it requires GLES3), so call the
extension API instead. This means we need to expose some extra methods
on GraphicsContextGL.

Lastly, the framebuffer textures we get are SRGB8_ALPHA8 which
requires an extension to be enabled with a WebGL1 context when
we're talking to an XR-compatible context. Similarly, we
enable the extension to allow multisampled framebuffers.

* Source/WebCore/Modules/webxr/WebXROpaqueFramebuffer.cpp:
(WebCore::WebXROpaqueFramebuffer::endFrame): call blitFramebufferANGLE.
(WebCore::WebXROpaqueFramebuffer::setupFramebuffer): Implement logic for WebGL 1.
* Source/WebCore/platform/graphics/GraphicsContextGL.h:
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.cpp: Implement the extension API/
(WebCore::GraphicsContextGLANGLE::renderbufferStorageMultisampleANGLE):
(WebCore::GraphicsContextGLANGLE::blitFramebufferANGLE):
* Source/WebCore/platform/graphics/angle/GraphicsContextGLANGLE.h:
* Source/WebCore/platform/graphics/cocoa/GraphicsContextGLCocoa.mm:
(WebCore::GraphicsContextGLCocoa::platformInitialize): Turn on the sRGB extension.
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGL.messages.in:
* Source/WebKit/GPUProcess/graphics/RemoteGraphicsContextGLFunctionsGenerated.h:
(renderbufferStorageMultisampleANGLE):
(blitFramebufferANGLE):
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxy.h:
* Source/WebKit/WebProcess/GPU/graphics/RemoteGraphicsContextGLProxyFunctionsGenerated.cpp:
(WebKit::RemoteGraphicsContextGLProxy::renderbufferStorageMultisampleANGLE):
(WebKit::RemoteGraphicsContextGLProxy::blitFramebufferANGLE):

Canonical link: https://commits.webkit.org/264838@main

---
## [chadlyalan/portfolio](https://github.com/chadlyalan/portfolio)@[4cf8389e14...](https://github.com/chadlyalan/portfolio/commit/4cf8389e149f007ae1d658601d865cddb627a987)
#### Thursday 2023-06-08 20:43:48 by Chad

Chadlyalan/issue16 (#17)

* Create landing.dart

* extra landing (accident)

somehow i created a duplicate landing widget and put it in the widgets folder. I was quite confused, not sure how it happened.

* email and linkedin

i have fully functional linkedIn, and Email buttons now, as well as Github.
Linked in and Github are simple hyper links where as the gmail button opens up your default mail app, and starts to compose an email with the mailto address being my own.

I've also removed the social media icons from the side panel widget.

* rock-garden svg icon

* resume card and linkedIn

linkedIn and resume now have their own cards.

Resume doesn't work yet but LInkedIn works great.

* trying to get pdf going

cleaning things up a little bit

* pdf'ing almost

it doesn't work but we might have a pdf viewer kinda close

* cleaning up socials

I'm going to give up on showing the resume in a PDF for now. I don't think most people are going to want to see the pdf while they're at my website anyway so it will be a feature I add later once the website is up and polished. for now socials are good where they're at.

---
## [shifucun/website](https://github.com/shifucun/website)@[60d93d54cc...](https://github.com/shifucun/website/commit/60d93d54cc21bc04c0f3e1c3435a76e3e74fe808)
#### Thursday 2023-06-08 21:22:28 by Jehangir Amjad

[NL Interface] Embeddings update (#2642)

In this PR, we do the following:

1. Make the build_embeddings_v2.py be the default way to generate
embeddings.
2. Updates the latest embeddings (after running the process in (1)).
3. Due to (1) and (2), increased the number of query -> sentences
matched number (from 20 to 40).
4. Updates the nl server tests (need reviewers to check carefully)
5. Update the integration tests (will need a careful look)
6. Linked is the embeddings index differ script output (using top 3
only):

https://drive.google.com/file/d/1-6A-xXcRYj50poglis_7rc1P3aqxYf3R/view?usp=sharing


Based on (6), most of the changes look Ok. We looked at some individual
cases to figure out if the differences are actually impacting. Only one
case below (in bold) was found to actually be different than what's on
autopush right now.

24: How many male civilians are there in Queens? => this is the same on
autopush and after the changes in this PR (ignoring "Queens" and the
stop words makes the results the same.)

38: What is the median age of American Indian or Alaska Native females
in the United States? => same as above (no impact).

43: age in california => this is different but since we'll soon be
removing some of the age SVs by breakdowns, it should be Ok.

44: agricultural output across california => same as above (no impact
due to place and stop word removal)

63: count of earthquakes per year => same on autopush so no impact. This
is because earthquake events are handled separately.

100: housing price trend comparison across US states => same as above
(no impact) after place and stop word removal.

**101: housing trend comparison across US states** => this is different
(autopush uses housing units but new embeddings lead to number of
households but that seems Ok but arguably autopush is also bad because
it goes to a correlation plot which is not the right thing to do here
anyway)

---
## [KingkumaArt/KingkumaTGSS13](https://github.com/KingkumaArt/KingkumaTGSS13)@[303cfa3bbb...](https://github.com/KingkumaArt/KingkumaTGSS13/commit/303cfa3bbb2199b24df17e87864d92e038a32dca)
#### Thursday 2023-06-08 21:47:34 by GoldenAlpharex

Fixes is_station_level() sometimes behaving erratically if the value provided is more complex than just a variable (#75489)

## About The Pull Request
I have been debugging this stupid macro for the past nearly five hours,
to finally figure out why it was breaking. If you had something like `a
|| 0` in what you called the macro with, it would somehow manage to
break the cache. This makes it far more foolproof, and will ensure that
it doesn't break here anymore, because debugging this has to be one of
the biggest pains in my ass I've ever had.

## Why It's Good For The Game
So shit like this

![image](https://github.com/tgstation/tgstation/assets/58045821/455122b0-34eb-4ec0-92dd-2775c1f0f878)

Doesn't end up breaking your CI (or even worse, the game in prod), in
places unrelated. At least now it shouldn't be overwriting values in the
cache.

It shouldn't have to do verification that you're doing the right thing,
that should be left on the person using the macro because it was meant
to be faster than a proc call, adding too much verification overhead
kind of just loses some of that speed.

## Changelog

:cl: GoldenAlpharex
fix: Makes checks for the station z level more robust against coders
doing less intuitive stuff, thus protecting it from breaking in weirdly
difficult and seemingly unrelated places (I'm looking at you, nuke
cinematic unit test).
/:cl:

---
## [KingkumaArt/KingkumaTGSS13](https://github.com/KingkumaArt/KingkumaTGSS13)@[2845c985fa...](https://github.com/KingkumaArt/KingkumaTGSS13/commit/2845c985fab04b0de1f7615799a260527af30822)
#### Thursday 2023-06-08 21:47:34 by Rhials

Adds a revolutionary conversion stinger (#75002)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds an antagonist gain stinger for Revolutionaries, created with
inspiration from the obsessed/traitor conversion sounds.


https://user-images.githubusercontent.com/28870487/235028674-170a4f9e-a873-4938-a700-536f005e539f.mp4

Raw audio:


https://cdn.discordapp.com/attachments/440978216484732934/1101964419203862548/revolutionary_tide.ogg

_A distant, hypnotic whistling. The heavy footfalls and clamoring voices
of an approaching crowd. The unstoppable revolutionary tide breaks its
waves upon an unsuspecting station._

I wanted to try and make something that felt like it fit in with the
other antagonist stingers we already have. Let me know what you think!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Gives a bit more flavor, and helps set the mood for the upcoming
bloodbath.

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
sound: Revolutionaries now have their own stinger that plays upon
becoming that antagonist.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[ae7595b8e1...](https://github.com/microsoft/terminal/commit/ae7595b8e13d4764f4db7b4060eaf57d1b4ee82e)
#### Thursday 2023-06-08 21:55:43 by Mike Griese

Add `til::property` and other winrt helpers (#15029)

## Summary of the Pull Request

This was a fever dream I had last July. What if, instead of `WINRT_PROPERTY` magic macros everywhere, we had actual templated versions you could debug into. 

So instead of 

```c++
WINRT_PROPERTY(bool, Deleted, false);
WINRT_PROPERTY(OriginTag, Origin, OriginTag::None);
WINRT_PROPERTY(guid, Updates);
```

you'd do 

```c++
til::property<bool> Deleted{ false };
til::property<OriginTag> Origin{ OriginTag::None };
til::property<guid> Updates;
```

.... and then I just kinda kept doing that. So I did that for `til::event`.

**AND THEN LAST WEEK**

Raymond Chen was like: ["this is a good idea"](https://devblogs.microsoft.com/oldnewthing/20230317-00/?p=107946)

So here it is. 

## Validation Steps Performed
Added some simple tests.

Co-authored-by: Leonard Hecker <lhecker@microsoft.com>

---
## [microsoft/terminal](https://github.com/microsoft/terminal)@[6ad8cd0a63...](https://github.com/microsoft/terminal/commit/6ad8cd0a630ab927629841a14d433c3bc19a1509)
#### Thursday 2023-06-08 21:55:43 by Mike Griese

Make conhost act in VtIo mode earlier in startup (#15298)

We need to act like a ConPTY just a little earlier in startup. My relevant notes start here: https://github.com/microsoft/terminal/issues/15245#issuecomment-1536150388. 

Basically, we'd create the first screen buffer with 9001 rows, because it would be created _before_ VtIo would be in a state to say "yes, we're a conpty". Then, if a CLI app emits an entire screenful of text _before_ the terminal has a chance to resize the conpty, then the conpty will explode during `_DoLineFeed`. That method is absolutely not expecting the buffer to get resized (and the old text buffer deallocated). 

Instead, this will treat the console as in ConPty mode as soon as `VtIo::Initialize` is called (this is during `ConsoleCreateIoThread`, which is right at the end of `ConsoleEstablishHandoff`, which is before the API server starts to process the client connect message).  THEORETICALLY, `VtIo` could `Initialize` then fail to create objects in `CreateIoHandlers` (which is what we used to treat as the moment that we were in conpty mode). However, if we do fail out of `CreateIoHandlers`, then the console itself will fail to start up, and just die. So I don't think that's needed.

This fixes #15245. I think this is PROBABLY also the solution to #14512, but I'm not gonna explicitly mark closed. We'll loop back on it.

---

