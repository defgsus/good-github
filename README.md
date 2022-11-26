## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-25](docs/good-messages/2022/2022-11-25.md)


2,016,420 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,016,420 were push events containing 2,927,098 commit messages that amount to 199,433,466 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 39 messages:


## [Dav999-v/VVVVVV](https://github.com/Dav999-v/VVVVVV)@[86d90a1296...](https://github.com/Dav999-v/VVVVVV/commit/86d90a1296739adef30b224f41e3a6ab55069a48)
#### Friday 2022-11-25 00:27:20 by Misa

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
## [Dav999-v/VVVVVV](https://github.com/Dav999-v/VVVVVV)@[2d6b2e685b...](https://github.com/Dav999-v/VVVVVV/commit/2d6b2e685b09d364e629b30a16c533b131efbde7)
#### Friday 2022-11-25 00:27:20 by Dav999-v

Clarify submodules in desktop_version/README.md

VVVVVV uses submodules now, so you need to know how to initialize them.

I'm explicitly not including `git clone --recurse-submodules`. Usage of
submodules in git projects is kinda rare in my experience, so people
are used to doing simple clones, and that instruction would just result
in people being annoyed thinking they have to delete the repo they
already cloned, and clone it again except slightly differently.

It also doesn't help you if you need submodules that aren't in the
master branch (for example, if you clone my fork recursively and then
checkout the localization branch, you won't have C-HashMap and you'll
need the update command anyway). And you also need it whenever VVVVVV
updates its submodules. So teaching people just the update command is
better.

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[ef59c0e0fa...](https://github.com/willior/Action_RPG_1/commit/ef59c0e0fa4d89b62d228a3b194154e852eca4da)
#### Friday 2022-11-25 00:38:50 by willior

MainMenu fixed; organizing font situation

at this point it is a good idea to completely re-haul the GUI/Theme organization as it's been a complete mess. the Control/layout system of godot 4 has been vastly improved (still a shitshow but not like it was before), and there are vestiges of bad organization and trial-by-error choices when it comes to fonts & themes.
here's how it should be:
we should have a "Theme" for each collection of buttons in a similar style. these Themes should have Fonts set. Fonts are .ttf files. then, their Button styleboxes can be set, and saved within the theme. whenever we want a menu/series of Buttons to look a certain way, we simply load the theme and it's done.
how it currently is:
some buttons have their font set by overriding the current theme. most of the time a theme isn't set. some labels/buttons have their theme_overrides/font set to a font file; others have it sent to a font RESOURCE pointing to the file. from what i can tell, this type of resource is depcrecated and replaced with new types of font resources.
some objects have a theme set, then aspects of that theme get overridden. also, the naming convention/file structure of all this stuff is all over the place and, frankly, absolutely terrible.
problem is, deleting everything and starting from scratch fucks up the project in unimaginable ways. deleting the depcrecated font resources changed the fucking node structure of my PauseScreen. it RE-NAMED NODES. what the fuck? so i will likely have to go through every single UI element, one-by-one, and fixing things, one-by-one.
i've done the MainMenu buttons - which are instances of a new BigButton scene. this BigButton has styleboxes creating for normal, and pressed. they are saved as resources under assets\UI\Menu\Buttons\Styleboxes\bigbutton(...etc.).

---
## [willior/Action_RPG_1](https://github.com/willior/Action_RPG_1)@[d74c2bc6ca...](https://github.com/willior/Action_RPG_1/commit/d74c2bc6ca3f8e90ef51434d5b93b753c2f8ccb3)
#### Friday 2022-11-25 01:44:32 by willior

font fixes

also fixed an issue where the Defend formula wasn't levelling up. the Defend formula has a built-in script, as opposed to a separate .gd file. when i'd declared the player.player_name variable (to hold a String version of the node name's StringName type... fucking hell...), i'd done a "find in files" search, which looks through all .gd files. i'd replaced every instance of player.name with player.player_name. however, this change didn't happen for Defend - it was still trying to give XP using player.name. however, it didn't throw an error or even a warning - it just didn't work. so i'm glad to have caught it. but it's introduced anxiety over having built-in scripts, if their contents aren't batch-searchable...
also, added an entry for Defend in the FormulaData scripts. i need to remember to do this for every Formula added.
anyways, looked for owners of large_dynamicFont, and replaced every instance of it with the 5x7 FontFile instead. i have done this on an object-by-object basis. what i need to do is create a Theme that sets the font, and save that theme. right now, every object has its own font-setting theme. so let's say, one day, i decide to change the font... i would have to do it for every object that has it. if i'd just saved the font to a theme resource, and used that resources across objects that needed that font, i could avoid future headaches.
let's see, a list of scenes changed:
BossHealth
check_formula_button
formula_customize_button
CustomizeScreen
check_tech_button
equip_tech_button
weapon_customize_menu
Dialog_Button
ExpBar1 & 2
HUD (HealthUI)
ButtonSTAT
FormulaItem
MenuIngredient
MessagePopup
PickupPopup (obsolete?)

---
## [LemonInTheDark/tgstation](https://github.com/LemonInTheDark/tgstation)@[25d4afc869...](https://github.com/LemonInTheDark/tgstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Friday 2022-11-25 02:21:18 by Iamgoofball

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
## [queercpu/script](https://github.com/queercpu/script)@[f4aacacc89...](https://github.com/queercpu/script/commit/f4aacacc89875cc6d4198422a03494d643d8061e)
#### Friday 2022-11-25 03:27:09 by home.cpu

i made a huge 20ft or so scroll. i dont know how long exactly but pretty long... longer than this room.  It's pretty indepth the whole outline of the story I'm looking at right now. I have to be confident to know if something should stay or not, only I can say what is extra fat and what is essential.... well... I realized also the 3rd rewrite ultimately has to be the renpy rewrite.. maybe its more like a revision but...... I'll be building the story out from ground up again with my hands so if theres going to be major changes it'll happen there i'll be able to work it out... then revision after its finished in renpy. I really want to start making 3d girls now, i want to make a doll body to work with, a base body mesh that I can cut up and use for various characters...  its going to be both genders/sex. in a way... its gonna be like the mmd doll and have sex fetish capabilities... strictly for me to make weird visual shit...experiment to hell with 3d and all the obsessive desire shit.the script just isnt done yet so. i feel like I can't get carried away with 3d just yet. I'm still really working out the kinks and all that I'm on aroll.  I really don't know what exactly to do right now cuz, i know alot of ep2 is lacking, and there are plenty of unwritten scenes that didnte ven get a first draft yet.  the outline is way past complete tho, the first / second draft is in various stages. technically the first drafts were ep1/2 and the original versions of 3.  its been evolving alot but it is slowly crystallizing and becoming more and more solid, conceptually more than anything else.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[24d795b354...](https://github.com/tgstation/tgstation/commit/24d795b354d9d6444cdea85fdf68fe0af00f98d4)
#### Friday 2022-11-25 04:31:37 by LemonInTheDark

Adds a preference that disables intensive rendering on different multiz layers (#71218)

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

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[24ae11ad6f...](https://github.com/Sonic121x/Skyrat-tg/commit/24ae11ad6f6af9c0b6dab12986b95943f0cdf1f8)
#### Friday 2022-11-25 05:17:17 by SkyratBot

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
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[f4335e5184...](https://github.com/Sonic121x/Skyrat-tg/commit/f4335e5184da0a4643bab601ae11c59e9d411a6e)
#### Friday 2022-11-25 05:17:17 by SkyratBot

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
## [lhy-42/grass](https://github.com/lhy-42/grass)@[b1616979f4...](https://github.com/lhy-42/grass/commit/b1616979f49a587d1a583a377206d0f787fa2b30)
#### Friday 2022-11-25 06:05:30 by James Kuang

Onboarding finally fucking works lets fucking go boys fuck yeah fucky fuck

---
## [adambujak/FALCON](https://github.com/adambujak/FALCON)@[f00f8bec67...](https://github.com/adambujak/FALCON/commit/f00f8bec67489c1ced980c0fd79227377e0dcbd7)
#### Friday 2022-11-25 06:09:37 by Devin Bell

Db/pose estim (#71)

* added AHRS library, seems to work ok, but the axis are all messed up

* added dt to madgwick library

* added beast attitude shit, quaternions are my bitch

* running fly mode with new attitude, pretty good. Needs some fine tuning and testing

* made logging 1Mbits

* changed rf logs to DEBUG

* minor changes for flight testing

* cleanup

Co-authored-by: Adam Bujak <adamjbujak@gmail.com>

---
## [ConquerOS/frameworks_base](https://github.com/ConquerOS/frameworks_base)@[eaabfb79f6...](https://github.com/ConquerOS/frameworks_base/commit/eaabfb79f6c4c793764fa746d43cc771c0f4c3c6)
#### Friday 2022-11-25 06:34:08 by Kuba Wojciechowski

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
Signed-off-by: HeroBuxx <me@buxxed.tk>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[29d766e25f...](https://github.com/tgstation/tgstation/commit/29d766e25f18c5030972562ed649832077cdfc95)
#### Friday 2022-11-25 08:31:07 by LemonInTheDark

Fixes attempting to offset floating planes (#71490)

## About The Pull Request

This is a dumb idea, and leads to fucked rendering on occasion

## Why It's Good For The Game

Fixes another portion of #70258, a player will no longer have a hidden
antag hud if they move down a z level after getting an antag. We were
trying to offset the floating plane of their image, and it went to shit.
Also fixes a bug with observers not having antag huds for the combo hud
to see. We were only giving them one on mind.on_transfer, rather then on
mind assignment. I hate mindcode

---
## [el-gringo/rx-player](https://github.com/el-gringo/rx-player)@[bd8bbbc8a7...](https://github.com/el-gringo/rx-player/commit/bd8bbbc8a7397b6fd6462aaf7d901e8c6d5e40cc)
#### Friday 2022-11-25 09:17:05 by Paul Berberian

remove RxJS code from the transports code

After doing a proof-of-concept looking at how some parts of the code
looks like without RxJS (#916), this is a first functional proposal
which looks good enough to me to be merged.

It removes all RxJS code from the `transports` code in `src/transports`.

As a reminder, the reasons for doing this are:

  1. Observables are complicated and full of implicit behaviors
     (lazily running, sync or async, unsubscribing automatically after
     the last unsubscription etc.) which is difficult to reason about,
     especially for a newcomer.

     Things like exploiting schedulers through the `deferSubscriptions`
     util to work-around some subtle potential race-conditions, or
     merging Observables in a specific order for similar reasons, are
     ugly hacks that are difficult to explain to someone not familiar
     with that code.

     Even for us with multiple years of experience with it, we sometimes
     struggle with it.

  2. Promises, event listeners - and direct callbacks in general - are
     generally much more explicit and most developpers (at least JS/TS
     devs) are familiar with them.

  3. Call stacks are close to inexploitable when using RxJS.

  4. Promises provide async/await syntax which can improve drastically
     the readability of our async-heavy code, which for the moment
     suffer from callback hells almost everywhere.

However, I'm still not sure if this wish (getting rid of RxJS) is shared
by other maintainers and/or contributors, so it is still only a proposal.

Thoughts?

---
## [el-gringo/rx-player](https://github.com/el-gringo/rx-player)@[60fbedb324...](https://github.com/el-gringo/rx-player/commit/60fbedb324f9caf6592ccccdab0bda8444820259)
#### Friday 2022-11-25 09:17:05 by Paul Berberian

transports: simplify segment parsers types

This commit proposes a simplification of types used by the segment
parsers by defining a unique segment data type instead of two: one for
the init segment and the other for media segments.

As `SegmentBuffers` - on which those segment data will be pushed - are
only generic based on a single segment data type, this is not really
necessary anyway.

The real reason behind creating two types was to better indicate that
text and image Representation had no initialization segment (by setting
their type to `null`) but considering that a parsed media segment could
theoretically be `null` as well, nothing is lost by using the same type
for both.

Being generic over a single type simplify the way we approach segment
parsers in my opinion. Now we're thinking: "which type is the parsed
segment data in?" not "which type is a parsed init segment data and
which type is a media segment data?". Both should generally be in the
same format and the only difference until now was that one could be
always `null`.
Also, considering that media segments could theorically contain
initialization data themselves, this is one more argument in the
direction of only defining a single type.

---

Another improvement in that commit is to limit `any` typings to the
small `segment_fetcher_creator.ts` file. Doing this there should reduce
possible typing errors as segment loader and parsers are now properly
type-checked (both their inputs and outputs).

---
## [izzyyes/Skyrat-tg-izzy-](https://github.com/izzyyes/Skyrat-tg-izzy-)@[b922aef977...](https://github.com/izzyyes/Skyrat-tg-izzy-/commit/b922aef97718aeffc0d3b450012575df2d065e20)
#### Friday 2022-11-25 09:44:03 by SkyratBot

[MIRROR] Adds Some Supermatter Effects  [MDB IGNORE] (#17734)

* Adds Some Supermatter Effects  (#67866)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This pull request adds a variety of Supermatter delamination effects to
make the crystal a bit more fun to watch and stare at. The initial
filter effects and animations are from Baystation12, but I have adapted
it to make it fun to watch!

It'll be a bit hard to explain in text, so this is the text explanation.

For normal running conditions, the Supermatter will emit pretty golden
rays, and a large campfire like that glow that grows and shrinks based
on it's power level.

![dreamseeker_vnw1BL7DNy](https://user-images.githubusercontent.com/77420409/174471609-7be70234-5eae-4839-b551-1c28145d6b60.gif)

For high power conditions, such as high O2 or CO2 amounts, the
Supermatter's rays will glow red and it will emit red light, aswell as
turn red (like before, unchanged).

https://user-images.githubusercontent.com/77420409/174471693-e191ee47-1a01-4b76-8570-9d12b994c2d4.mp4

When the conditions for a cascade, singularity, or a tesla are met, the
colours and rays emitting from the crystal will change to match!

https://user-images.githubusercontent.com/77420409/174471747-dffb3beb-dd38-42a1-a97b-7262dabd60af.mp4

https://user-images.githubusercontent.com/77420409/174471765-af1927e8-a48e-4fd5-a35c-6b3aa53c5add.mp4

Also, I've added more sucking power to the crystal during its final
countdown for DRAMATIC EFFECT. If the singularity conditions are met,
the supermatter will SUCK THINGS INTO IT, even if they are bolted to the
GROUND. Just like a singularity! It's REALLY COOL.
https://streamasaurus.com/sharing/singularity_full.mp4 <--17MB video.
UPDATE 1: New rays for the singulo

https://user-images.githubusercontent.com/77420409/174933219-0118748a-02da-40f8-9b99-06009e197cc8.mp4
UPDATE 2:
Singularity delamination final countdown effect??:

https://user-images.githubusercontent.com/77420409/175421220-66bae109-204d-44ee-8a67-c18ce8eff3ba.mp4

When the supermatter has reached the FINAL COUNTDOWN but does NOT meet
the criteria for a singularity, it will simply YOINK everything
unwrenched towards, like a gravitational anomaly, range based on power
at the time. Not as crazy as the singularity. Most things will get
slapped against walls.

Here, have another cool delamination demo showing the criteria's
swapping mid countdown!
https://streamasaurus.com/sharing/modeswapping.mp4 <-- 17.5MB

I am likely missing something important from this body as I am drowsy
making this! I will update this body with anything I forgot to note that
I did.

## Why It's Good For The Game

The supermatter is a a very cool thing, but it could be cooler. I think
the visual experience could do with a bit of an upgrade, as visual
feedback is really cool and impressive to watch! You could tell more
about the crystal without looking at the console, but not everything or
precise numbers.

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
add: The Supermatter crystal will now emit rays of light, varying on
it's power level and situation.
code: improves a formatting and comment spelling
fix: The Causality field now actually shows up!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: tralezab <40974010+tralezab@ users.noreply.github.com>

* Adds Some Supermatter Effects

Co-authored-by: nevimer <77420409+nevimer@users.noreply.github.com>
Co-authored-by: tralezab <40974010+tralezab@ users.noreply.github.com>

---
## [nachiketa3299/baekjoon-ruzen](https://github.com/nachiketa3299/baekjoon-ruzen)@[249618a5c8...](https://github.com/nachiketa3299/baekjoon-ruzen/commit/249618a5c8a26d00eb0013be781527e0946edfff)
#### Friday 2022-11-25 09:54:38 by Ruzen

Merge branch 'master' of https://github.com/nachiketa3299/baekjoon-ruzen
Go Fuck Your Self

---
## [brucerennie/muforth](https://github.com/brucerennie/muforth)@[e7d8f795ac...](https://github.com/brucerennie/muforth/commit/e7d8f795acd9d8026089b0433e40131af18f8913)
#### Friday 2022-11-25 10:32:09 by David Frech

[core] WIP - mixed 32/64 implementation

I'm checking this in because there are some interesting ideas in here
for dealing with, eg, a 32-bit wide heap even on 64-bit machines, using
relative addressing. There are interesting questions about when you want
to deal with relative vs absolute addresses, when to convert them, etc.
I came to the conclusion that it made the most sense to always push
absolute addresses onto the stack - and @ and ! and friends would expect
absolute addresses - only converting them to relative form when writing
them into or reading them from a heap cell.

NEXT would be a bit slower because it has to do this conversion - when
reading an xt (a 32-bit relative pointer), it has to make it absolute (by
adding the heap origin address) before fetching the code field - which
is also a relative address, but this time relative to mu_do_colon;
chosen carefully so that colon words would always have a code field with
all zeros, so it would be easily recognizable. ;-)

I've decided to pursue a different approach. Instead of having a nice
compact heap on all platforms, instead let's favor the address size of
the machine. On a 32-bit machine, heap cells - which mostly contain
addresses - are 32 bits wide. And on a 64-bit machine they are 64 bits.
We can write a very natural NEXT that uses machine pointers in most
obvious and efficient way.

The tricky part comes with dealing with *values*. I want to keep the
64-bit computational nature of muforth intact, so the stacks will remain
64 bits wide on all platforms. This works cleanly on a 64-bit machine:
the stacks and the heap are both 64-bits wide. On a 32-bit machine,
we have to store values in two consecutive cells, and be careful about
alignment or do 64-bit fetches and stores in two 32-bit pieces. I'm not
too concerned about this because 32-bit machines are not the "intended"
host platform for muforth; I'm much more interested in a stellar
experience on 64-bit machines. But if I can get it to work reasonably
well on 32-bit machines, great.

Some of the changes I've made while experimenting with the
relative-addressed heap still apply, and there are also some changes in
the way that values are communicated between C and Forth that I want to
keep, so I'm going to start from here as I continue on this adventure
into the heap!

---
## [Mrlinkwii/pcsx2](https://github.com/Mrlinkwii/pcsx2)@[4d73147121...](https://github.com/Mrlinkwii/pcsx2/commit/4d731471214898389c6b39e459595b54e1b89ce3)
#### Friday 2022-11-25 10:43:09 by RedDevilus

GameDB: Fixes to multiple games yet again

- Thrillville + Thrillville Off The Rails: Mad TFF / deinterlace 8 to stop shaking the whole game
- Forgotten Realm Demon Stone: Get rid of more blur
- ATV Offroad Fury 3: MTVU disabled which was an odd find to improve FPS
- Crimson Tears: Wild arms + Full Sprite for reducing bloom misalignment + note that Blending TFF might be better especialy when you use Software.
- Final Fantasy X: Texture in Rt for fixing endgame summons like Anima and The Magus Sisters
- No One Lives Forever: Mipmap full + trilinear + full blending needed to fix lighting

---
## [umoi0/Fuu](https://github.com/umoi0/Fuu)@[7d04edb6e2...](https://github.com/umoi0/Fuu/commit/7d04edb6e2927330906a7af89664b7a5ab3aa48c)
#### Friday 2022-11-25 11:29:41 by Profakos

Mail sorting helper, and disposals fixes (#70861)

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

---
## [SOVIET-ANDROID/kernel_xiaomi_raphael](https://github.com/SOVIET-ANDROID/kernel_xiaomi_raphael)@[a78d677870...](https://github.com/SOVIET-ANDROID/kernel_xiaomi_raphael/commit/a78d677870e511262c9758e2fcd97ab8c9f54ec1)
#### Friday 2022-11-25 12:33:51 by kondors1995

raphael_defconfig: Revert FBEv2 defconfig changes

To maiteiners who still use FBEv1 Fuck you in particular

https://www.youtube.com/watch?v=Ok3xVYz8Ibs

---
## [Empire-Strikes-Back/Billy-Hoyle](https://github.com/Empire-Strikes-Back/Billy-Hoyle)@[de7a490522...](https://github.com/Empire-Strikes-Back/Billy-Hoyle/commit/de7a490522ae0e38cee7d1548af80563629ec850)
#### Friday 2022-11-25 13:26:36 by Billy-Hoyle

hire me of fire me - it's entirely up to you

like James Harden personal stats were too important to me

unlike Kip Andersen I didn't take time to deliver fruit but rushed

I was busy when Jesus spoke about two masters, blind leads the blind, teacher and student

let my name be Billy-Hoyle
like James Bond after Moneypenny shot hit - so far I am a wreck
let my gui - even thow initially in brower - be on jvm - even I being evil understand it's more merciful and light
I heard Jesus speak about root - I am one of the roots of the garden
let me use project.clj - I am enemy of the garden so for me it's not even painful after shadow-cljs.edn insanity

:Matthew-McConaughey very interesting trend I tell you
:Jay-Farrow mr... it's not a trend...
:Adele I muust have caallledd a thouuusand tiimes
:child thanks, Adele!

---
## [lyubomyr-shaydariv/git](https://github.com/lyubomyr-shaydariv/git)@[f1c903debd...](https://github.com/lyubomyr-shaydariv/git/commit/f1c903debdcbf6aaf8fd3abf222fa941b42d5d31)
#### Friday 2022-11-25 13:32:12 by Ævar Arnfjörð Bjarmason

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
## [Arthurreuss/pets_air_bnb](https://github.com/Arthurreuss/pets_air_bnb)@[75a409d3da...](https://github.com/Arthurreuss/pets_air_bnb/commit/75a409d3dae63e7a44f98d3c98073d03000ff5b8)
#### Friday 2022-11-25 13:55:48 by Arthurreuss

Merge pull request #35 from Arthurreuss/finalchanges

fuck you

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[e7c8fed8e3...](https://github.com/odoo-dev/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Friday 2022-11-25 15:53:44 by qsm-odoo

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
## [techie2000/awesome-console-services](https://github.com/techie2000/awesome-console-services)@[4b8f298fb2...](https://github.com/techie2000/awesome-console-services/commit/4b8f298fb2b94b3c492da39ca43fcd2775907eea)
#### Friday 2022-11-25 16:40:44 by techie2000

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
## [HelloVolla/android_kernel_volla_mt6768](https://github.com/HelloVolla/android_kernel_volla_mt6768)@[ea51dd856a...](https://github.com/HelloVolla/android_kernel_volla_mt6768/commit/ea51dd856a87985ba4a17f3283af364c7e2e4bd6)
#### Friday 2022-11-25 17:52:12 by Peter Zijlstra

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

---
## [lessthnthree/tgstation](https://github.com/lessthnthree/tgstation)@[deee485693...](https://github.com/lessthnthree/tgstation/commit/deee48569310b1d48d739fc3b529ac00838e45b0)
#### Friday 2022-11-25 19:00:16 by LemonInTheDark

Fixes antag hud icons disappearing if mesons were equipped (#71155)

## About The Pull Request

They sit on plane 0, IE the darkness plane. So if say, the darkness
plane was alpha'd away (which we have to do with see_blackness), then so
goes the hud element. stupid stupid stupid stupid

## Why It's Good For The Game

Fixes a derivation of #68087
Not all of it, since most of that came about pre plane cube and likely
has to do with z'd image shenanigines. I got it to replicate once
randomly but then it stopped. v annoying. There is a linked issue report
that mentions mesons however, which this does resolve.

## Changelog
:cl:
fix: You can now see antag hud icons AND see through walls. WOW
/:cl:

---
## [thearst3rd/Fairy-Stockfish](https://github.com/thearst3rd/Fairy-Stockfish)@[57bda214fc...](https://github.com/thearst3rd/Fairy-Stockfish/commit/57bda214fcc8cd9d40fd3fd6f43c766ac9f88662)
#### Friday 2022-11-25 19:51:05 by Snowmoondaphne

Update variants.ini

I'm really sorry to tell you this,,,

The positions of Black's Queen and Cardinal have been swapped in Pandemonium. Therefore, the definition has changed and it is necessary to modify it

[pandemonium]
variantTemplate = shogi
pieceToCharTable = PNBRFSA.UV.++++++++.++Kpnbrfsa.uv.++++++++.++k
maxFile = 9
maxRank = 9
pocketSize = 9
startFen = rnbsksbnr/2+f1+u1+a2/p1p1p1p1p/4v4/9/4V4/P1P1P1P1P/2+F1+U1+A2/RNBSKSBNR[] w - - 0 1
customPiece1 = o:NA
customPiece2 = s:WF
customPiece3 = u:D
customPiece4 = w:DWF
cast = false
pieceDrops = true
capturesToHand = true
immobilityIllegal = true
soldier = p
knight = n
bishop = b
rook = r
king = k
queen = q
commoner = g
dragonHorse = h
bers = d
alfil = a
archbishop = c
chancellor = m
fers = f
wazir = v
centaur = t
promotionRank = 7
promotedPieceType = p:g n:o b:h r:d a:c v:m f:q s:w u:t
doubleStep = false
perpetualCheckIllegal = true
nMoveRule = 0
nFoldValue = loss
stalemateValue = loss

Could you please modify the definition like this?

Sorry again for the troublesome request,,,

---
## [sgharms/dotfiles](https://github.com/sgharms/dotfiles)@[4163848562...](https://github.com/sgharms/dotfiles/commit/416384856269a42cd89a80062c7b380fdd8f58fb)
#### Friday 2022-11-25 20:15:56 by Steven G. Harms

Ground control to major jason

Hey man, it was a real surprise seeing you after a pandemic in the middle of the balloon insanity on 72nd street. Sorry I didn't recognize ya, we were on our pediatrics visit with my 30 day-old kid! I didn't have any other contact data for you, so here's a PR that I hope will land i your inbox. Find me on linked in or sgharms -at- stevengharms.com! It'd be great to catch up again soon!

---
## [Radeon0078/Fedoraware](https://github.com/Radeon0078/Fedoraware)@[50a54973e7...](https://github.com/Radeon0078/Fedoraware/commit/50a54973e76ff2315320cab53235f3a91da053c8)
#### Friday 2022-11-25 20:20:36 by Baan

Merge pull request #693 from Radeon0078/patch-1

fuck you this is better kys 130 fov sucks balls

---
## [thief-hub/thief-site](https://github.com/thief-hub/thief-site)@[a0e8f16709...](https://github.com/thief-hub/thief-site/commit/a0e8f167090617bdd9bcf1b304e78585ed3f5460)
#### Friday 2022-11-25 21:17:51 by Eric Boschmann

feature: add a SHIT TON OF FUCKING LINKS TO THIS STUPID LIST MANUALLY

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[460ab7adf5...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/460ab7adf560856148d46233e3cde565d05354a4)
#### Friday 2022-11-25 21:41:49 by SkyratBot

[MIRROR] JPS Optimization (Light Botcode) [MDB IGNORE] (#17669)

* JPS Optimization (Light Botcode) (#70623)

## About The Pull Request

Alright. So.
Right now, JPS works like this:
```
code requests path
we enter the actual pathfinding
pathfinding sleeps when it overruns a tick
if it sleeps, it'll then wake up before the mc starts
continue
```
This has annoying side effects. Primarily that we have no real control
over JPS, we just sorta have to eat its cost.
So if there's like 10 different things pathfinding at once, the mc will
have no time to do anything. Hell we might even end up eating into
maptick's time if the jps work is expensive enough (note the cost of
sleeping is not accounted for, and that has overhead)
This has happen before, usually when someone makes a lot of bots, and
it's really annoying.

So then, lets put JPS on a subsystem. That way the MC has control over
it.
But wait, existing code expects to yield and get back a path list, and
that's a sane request.
This is solvable, but requires abusing pass by reference lists, and the
ability to make callbacks into partials (preinsert arguments into them
before they're called, and accept other args later)

Because of this, we can now pass callbacks into pathfinders, allowing
for async use, rather then JUST yielding.

Of note: I've removed the 10 pathfinding datums limit, since
ratelimiting like that is handled nicely by the MC.
I've also removed the 15 second timeout, since mc yielding would trigger
it too often. I'm unsure if this means we don't have exit conditions for
pathfinding, need to talk to ryll. (@ Ryll-Ryll what happens if jps just
like, fails to find a path?)

Also of note: I think bots will fire off more then one pathfinding
attempt at a time if their first takes too long to complete. This is
dumb, why do we do this?

Optimizes JPS by more then 40% by removing redundant for(thing in turf)
loops, and avoiding making proc calls if objects are non dense.
This makes things slightly more fragile, but saves a LOT of time. I
think it's worth it, tho talking to mso it might be possible to do
better. Maybe I should do a LINDA system style thing. (I did a linda
system style thing I fixed it)

Optimizes botscanning, fixes bots not seeing things adjacent to them
The list of types could be a cached typecache
We could inline both checkscan and check_bot
check_bot SHOULD NOT BE CALLED ON EVERY OBJECT IN VIEW HOLY SHIT WHY
We don't need to process adjacent and the shuffled view separately, it's
in fact easier to process them in one block
Renames a var

Moves bot's pathing images to above most floor objects, so they're
visible in maint

## Why It's Good For The Game

Speed. Also manuel will stop killing their server by placing 20000
medibots (fucking icebox man every time)

## Changelog

:cl:
fix: Bots will now "notice" you if you're standing right next to them
fix: Bot paths will now draw above things like pipes, rather then below
them
refactor: Changed how pathfinding paths get generated
refactor: Made pathfinding and bot searching significantly faster
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* JPS Optimization (Light Botcode)

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

---
## [marcellerusu/small-clj-lang](https://github.com/marcellerusu/small-clj-lang)@[1eb40683db...](https://github.com/marcellerusu/small-clj-lang/commit/1eb40683dbbe9b2d2b07cf2b310bb27ed1a97ab5)
#### Friday 2022-11-25 22:01:02 by MarcelRusu

Clean up

lexer/tokenize
 - use loop macro to drastically clean up the recursion
 - make lexer/tokens a vec of maps to make iteration dead simple

I really love this loop macro, its so clean & easy to use. I feel like all my imperative ruby algorithms translate surprisingly easy to clojure with the help of loop

Clojure is feeling super natural now, really glad to have tried again. It feels like the clean code I used to write in ruby but with just a little bit more foresight with the restriction of immutability

There have been some parts of this process where I was seriously banging my head against the wall, thinking this immutability stuff is just a waste of time.. but now it feels very elegant - ugh I kinda hate that word lol, but its good.

Even the parser, I didn't think I could write a much simpler parser than what I did in ruby, and I think I still have quite a ways to go before, maybe I eventually will do make a let-parse macro or something to clean up some of the core.match ugliness.

Overall I'm very happy. Even though the error messages in clojure are probably the worst I've ever seen, the calva plugin makes it still more productive than I've been in ruby & honestly likely any other language for this kind of stuff

---
## [Phiggle/bizhawk-shuffler-2](https://github.com/Phiggle/bizhawk-shuffler-2)@[5885e8b5bc...](https://github.com/Phiggle/bizhawk-shuffler-2/commit/5885e8b5bcb808574aedfbf6fd044b2ed2abf30b)
#### Friday 2022-11-25 22:12:25 by Phiggle

Massive update - more games, fixes, 2.8 support?

HUGE UPDATE WITH LOTS OF CHANGES so please say something if you find bugs or can't run something that should run!

Several games were added:
- Castlevanias 1, 2, 3 (NES), 4, Bloodlines, Rondo, Dracula X (SNES)
- F-Zero (SNES)
- Mario Paint (with joystick hack) for Gnat Attack
- Kirby's Adventure (NES)

Chip and Dale (NES) is temporarily disabled while I investigate some glitches related to infinite lives and, uh, crashing the plugin when I try to rectify that.

Super Metroid and SMZ3 now only swap on Zebes if you BOTH trigger i-frames and lose health. This prevents swaps from steam while escaping Ceres/Zebes!

Certain games, annoyingly, have some kind of hex workaround for how they show their 10s and 1 digits. That now has been taken into account for counting lost lives for shuffling/infinite lives purposes. Also, a problem with the formula I used in testing to convert these from hex to decimal was causing extra swaps in SML1 and missed swaps in SMB2 (GB). That SHOULD be fixed now, but I will re-check my math...

Glitches to fix still include: Chip and Dale infinite lives not working somehow, F-Zero swapping the player on winning a race.

Additionally, the plugin SHOULD work well with 2.6.3+! Much of this required relocating functions to on_game_load or on_frame and specifying which RAM we wanted to use, exactly, rather than using mainmemory, for reasons I am not fully sure about but am investigating! Fortunately, that doesn't affect anything in 2.6.2 other than my convenience in adding code for new games.

Phew!

---
## [Firetop/FastAsyncWorldEdit](https://github.com/Firetop/FastAsyncWorldEdit)@[2fe54a04b5...](https://github.com/Firetop/FastAsyncWorldEdit/commit/2fe54a04b5d2b8cbb2a26947df610f3c8d4400ca)
#### Friday 2022-11-25 22:14:42 by Pierre Maurice Schwang

Adjust platform specific code to recent changes (#1997)

* chore: remove usage of MCUtil in StarlightRelighter

* chore: cleanup of unused imports

* hacky shit-fuckery for papers new chunksystem und refactor

* chore: address review comments

* Update dependency io.papermc.paperweight.userdev:io.papermc.paperweight.userdev.gradle.plugin to v1.3.9 (#2001)

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

* fix: suppress exceptions for field retrieval, cache fields / methods

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com>

---
## [Udiknedormin/CompassOfWomanhood](https://github.com/Udiknedormin/CompassOfWomanhood)@[e4e1647677...](https://github.com/Udiknedormin/CompassOfWomanhood/commit/e4e16476778d22f6c24bf6af6d690cc5b6a5f46f)
#### Friday 2022-11-25 22:27:18 by Misha Kotwica

improve Polish voiceover for Shithri (drinks)

mainly volume, but also making male and female versions more similar

---
## [PiMaker/rvc](https://github.com/PiMaker/rvc)@[134e85e485...](https://github.com/PiMaker/rvc/commit/134e85e485cb326f2b31642afeeb6583c9245f96)
#### Friday 2022-11-25 22:33:24 by pi

add rng, rtc, networking, more CSR paravirt exts and fixes

honestly forgot what I added all over the last year or so, but here you
go, enjoy more cursed code

---
## [mahak/cockroach](https://github.com/mahak/cockroach)@[1d04cec7c5...](https://github.com/mahak/cockroach/commit/1d04cec7c5f887d309e09b7b5a267d5269d86b5a)
#### Friday 2022-11-25 23:23:24 by craig[bot]

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

