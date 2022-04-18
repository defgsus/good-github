## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-04-17](docs/good-messages/2022/2022-04-17.md)


1,495,072 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,495,072 were push events containing 2,168,056 commit messages that amount to 114,194,851 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 33 messages:


## [DragonTrance/tgstation](https://github.com/DragonTrance/tgstation)@[759d24ab14...](https://github.com/DragonTrance/tgstation/commit/759d24ab14af0ab22ae9642e9190c3db91e16516)
#### Sunday 2022-04-17 01:13:34 by san7890

Four Corners, Red Rover: An Exploration in Decal Trends [MDB IGNORE] (#65290)

* Four Corners, Red Rover: An Exploration in Decaled Trends

You there! What exactly is wrong with this photograph?!

You don't need to tell me, I've boxed it out. There's four individual corners for the decalling. This is weird. You may be asking: Why don't they use the "full tile" turf decals? Let me demonstrate.

Look at the difference between the one at left and the one in the middle. The turf decal totally smothers the nice contrast lines afforded to use by the base turf, causing it to have smooth, clammy exterior. This is probably why no mapper ever uses the full turf decal, much to the chagrin of people who stare at how big the size of this repo is.

Now, what's that on the right? Why, it's the new sprite (and pathing I made) to help counter-act this issue! This perfectly lines up with the contrast lines of the base turf, allowing us to have a non-flattened visualization, while not having four fucking turf decals a turf load upon initialization. How epic!

I've also added "contrasted" variants of the "half" and "anticorner" turf decals for future use. I probably won't go through and update this in this PR, but the opportunity remains available.

I may or not map this change across all the maps. We shall see.

* neutral corners

we love vsc

* no wait

i forgot a bunch of potential edgecases so we'll have to go back. yellow should be fine but neutral, dark, blue, and green should get a second look over

* recheck

found some stuff, probably missed out on others. let us commence forth

* MISTAKE

nearly a fucko bwoingo

* final pass

it compiles and i've had enough, someone else can probably figure it out from this point onwards

* #65230 goated my timbs

now we wait for linters to fail

* YOU DIDN'T SAY THAT THE FIRST TIME

LINTERS AAFAFAFF

---
## [DragonTrance/tgstation](https://github.com/DragonTrance/tgstation)@[884c1eeb62...](https://github.com/DragonTrance/tgstation/commit/884c1eeb62e1c970b2b6edc425f36c924b9f48ee)
#### Sunday 2022-04-17 01:13:34 by 小月猫

fixes wallmounts (#65408)

closes #65393 (Engineering Cyborgs can't place APC or Air alarm frames on walls anymore)
fixes the code error in #64428 (afc1e44ee2922a316feb958249f7806568953bbe)

basically what occured is that he typed out the T(turf) attackby proc to input the screwdriver as an arg rather then the wallmount, remember, you want the WALLMOUNT to hit the wall to place it, not the screwdriver, that just creates runtimes and doesnt place anything

EDIT: actually re-reading it, what it was actually doing was using the screwdriver as the user arg, and trying to smash the user into the wall, thats actually kinda funny

borgo wallmounting is a good thing, good borgos need their treats

---
## [lioniac/pokefirered](https://github.com/lioniac/pokefirered)@[5cf4069063...](https://github.com/lioniac/pokefirered/commit/5cf4069063f692c38e3895ee7a13bcdc6a7b5e6a)
#### Sunday 2022-04-17 01:37:04 by lioniac

[Base] Multiple BugFixes & Basic QOL
- Bugfix: Tall and Short Grass (Credit: Deokishisu)
- BugFix: Snow Weather (Credit: ghoulslash)
- BugFix: Multiple bugfixes already available in the code
- Debug: Startup Script (Credit: Lunos)
- Debug: MGBA PrintF Support (Credit: hjk321)
- Debug: Menu (Credit: hjk321)
- Debug: Better Givemon
- QOL: Extra Save Space (Credit: hjk321)
- QOL: Increased Max Money
- QOL: Removed redundant move grammar tables (Credit: Kurausukun)
- QOL: Fixed Default Names: Red(M), Green(F), Blue(Rival)
- QOL: Faster Joy (Credit: TheXaman and ghoulslash)
- QOL: Autorun
- QOL: Skip Controls+Battle Tutorial, Viridian Old Man, Flashbacks
- QOL: RenderText faster w/o pressing A or B buttons
- QOL: Game Start Options = Fast|Stereo|Set|True|LR
- QOL: Lower case after first input in Naming Screen (Credit: Jaizu)
- QOL: Emerald Bag Sort Ported (Credit: ghoulslash)
- QOL: Register LR (Freed SELECT button)
- QOL: Unhidden Power (Summary and Battle Screen)
- QOL: Pokemon Summary Screen: Nature Colored Stats
- QOL: Removed all FRLG item animation screens
- QOL: BW Repel/Reuse Field Medicine (Credit: ghoulslash/AsparagusEduardo)
- QOL: Enable NationalDex from Start
- QOL: Trainer class-based Pokéballs
- QOL: Better Givemon (Credit: Lunos/ghoulslash)
- QOL: Pokémon editor specials: EV,Moveset,Replenish PP (Credit: Lunos)
- QOL: Reusable TMs; Can purchase only one
- QOL: Expanded TMs up to 92; Only GenIII moves available
- QOL: HackMew's Shinyzer
- QOL: Removed badge boosts.
- QOL: Disable Bag Use In Battle (Credit: ghoulslash)
- QOL: Let a Pokémon forget any move they know (Credit: Lunos)
- QOL: Change Pokémon Nickname from Party Menu (Adapted from Shinny456)
- QOL: Nop Quest Log
- QOL: Increased boxes from 14 to 16
- QOL: Disable Pokémon Center Union Room check
- QOL: Surf Dismount Ground Effects
- QOL: Seed on startup
- QOL: Improved freecam
- QOL: Optimized WaitForVBlank
- QOL: Removed unecessary encryption of Pkmn struct data
- QOL: Allow Pichu Breeding with Volt Tackle
- QOL: Ported Pickup Mechanics (Credit: Lunos)
- QOL: Egg hatches at Lvl 1
- QOL: Physical/Special/Status split
- QOL: Fairy Type, Type Effectiveness Chart Updated
- QOL: Moves, Items and Learnsets Updated
--- Immunity, Limber, Insomnia, Vital Spirit and Magma Armor heal up on Switch
--- Damage Boost held items updated from 10% to 20% increase.
--- Wild Pokemon Held Items updated
--- Learnsets w/ early Leech Life moved to later lvls; Early = Absorb
- QOL: Shop Items By Badge Count (Credit: ghoulslash)
- QOL: TrainerMons EV,Nature,Gender,Friendship,Nicknames (Adapted from: surskitty)
- QOL: All FRLG Mons +Starters +GameCorner Update - Starters like in GenVII: Viridian Forest, Route 3, Route 4, Route 24
- QOL: RTC code (Credit: Anthony La)
- QOL: Dynamic Overworld Palettes (Thanks hjk321)
- Feature/Untested: Added Dive. Received at Viridian Gym (Credit: ghoulslash)
- Feature/Untested: Follow Me (Credit: ghoulslash)
- Feature/Untested: Quest Menu (Credit: ghoulslash)
- SRW (Feature/Tested/Incomplete): Seasons Random Weather
--- Dynamic Season Wild Pokemon
--- Dynamic Hidden Items per Season
--- Day and Night wild encounter per Season

---
## [lioniac/pokefirered](https://github.com/lioniac/pokefirered)@[6697ea4b60...](https://github.com/lioniac/pokefirered/commit/6697ea4b603aeddfa90a6be273fd6fb45e141470)
#### Sunday 2022-04-17 01:48:08 by lioniac

[Base] Multiple BugFixes & Basic QOL
- Bugfix: Tall and Short Grass (Credit: Deokishisu)
- BugFix: Snow Weather (Credit: ghoulslash)
- BugFix: Multiple bugfixes already available in the code
- Debug: Startup Script (Credit: Lunos)
- Debug: MGBA PrintF Support (Credit: hjk321)
- Debug: Menu (Credit: hjk321)
- Debug: Better Givemon
- QOL: Extra Save Space (Credit: hjk321)
- QOL: Increased Max Money
- QOL: Removed redundant move grammar tables (Credit: Kurausukun)
- QOL: Fixed Default Names: Red(M), Green(F), Blue(Rival)
- QOL: Faster Joy (Credit: TheXaman and ghoulslash)
- QOL: Autorun
- QOL: Skip Controls+Battle Tutorial, Viridian Old Man, Flashbacks
- QOL: RenderText faster w/o pressing A or B buttons
- QOL: Game Start Options = Fast|Stereo|Set|True|LR
- QOL: Lower case after first input in Naming Screen (Credit: Jaizu)
- QOL: Emerald Bag Sort Ported (Credit: ghoulslash)
- QOL: Register LR (Freed SELECT button)
- QOL: Unhidden Power (Summary and Battle Screen)
- QOL: Pokemon Summary Screen: Nature Colored Stats
- QOL: Removed all FRLG item animation screens
- QOL: BW Repel/Reuse Field Medicine (Credit: ghoulslash/AsparagusEduardo)
- QOL: Enable NationalDex from Start
- QOL: Trainer class-based Pokéballs
- QOL: Better Givemon (Credit: Lunos/ghoulslash)
- QOL: Pokémon editor specials: EV,Moveset,Replenish PP (Credit: Lunos)
- QOL: Reusable TMs; Can purchase only one
- QOL: Expanded TMs up to 92; Only GenIII moves available
- QOL: HackMew's Shinyzer
- QOL: Removed badge boosts.
- QOL: Disable Bag Use In Battle (Credit: ghoulslash)
- QOL: Let a Pokémon forget any move they know (Credit: Lunos)
- QOL: Change Pokémon Nickname from Party Menu (Adapted from Shinny456)
- QOL: Nop Quest Log
- QOL: Increased boxes from 14 to 16
- QOL: Disable Pokémon Center Union Room check
- QOL: Surf Dismount Ground Effects
- QOL: Seed on startup
- QOL: Improved freecam
- QOL: Optimized WaitForVBlank
- QOL: Removed unecessary encryption of Pkmn struct data
- QOL: Allow Pichu Breeding with Volt Tackle
- QOL: Ported Pickup Mechanics (Credit: Lunos)
- QOL: Egg hatches at Lvl 1
- QOL: Physical/Special/Status split
- QOL: Fairy Type, Type Effectiveness Chart Updated
- QOL: IV+EV in Summary Screen
- QOL: Moves, Items and Learnsets Updated
--- Immunity, Limber, Insomnia, Vital Spirit and Magma Armor heal up on Switch
--- Damage Boost held items updated from 10% to 20% increase.
--- Wild Pokemon Held Items updated
--- Learnsets w/ early Leech Life moved to later lvls; Early = Absorb
- QOL: Shop Items By Badge Count (Credit: ghoulslash)
- QOL: TrainerMons EV,Nature,Gender,Friendship,Nicknames (Adapted from: surskitty)
- QOL: All FRLG Mons +Starters +GameCorner Update - Starters like in GenVII: Viridian Forest, Route 3, Route 4, Route 24
- QOL: RTC code (Credit: Anthony La)
- QOL: Dynamic Overworld Palettes (Thanks hjk321)
- Feature/Untested: Added Dive. Received at Viridian Gym (Credit: ghoulslash)
- Feature/Untested: Follow Me (Credit: ghoulslash)
- Feature/Untested: Quest Menu (Credit: ghoulslash)
- SRW (Feature/Tested/Incomplete): Seasons Random Weather
--- Dynamic Season Wild Pokemon
--- Dynamic Hidden Items per Season
--- Day and Night wild encounter per Season

---
## [Bill2232/Online_Clinic](https://github.com/Bill2232/Online_Clinic)@[4f4938bbdd...](https://github.com/Bill2232/Online_Clinic/commit/4f4938bbddfc15eeebf17cbe9b2112644c1e2d1b)
#### Sunday 2022-04-17 02:59:45 by Bill2232

Settings form almost done....
YEAH YEAH AS U HERAD (ALMOST DONE) NOT COMPLETLY DONR CAUS I'M FUCKING TYRED AND I WANT TO FUCKING SLEEP, GOOD FUCKING NIGHT

---
## [Hathoom/Submarine-Pirates](https://github.com/Hathoom/Submarine-Pirates)@[df77f4ff84...](https://github.com/Hathoom/Submarine-Pirates/commit/df77f4ff84163cae1fbef3576a5bb1df7b48de17)
#### Sunday 2022-04-17 03:46:18 by Nicky

Merge pull request #20 from Hathoom/UI

fuck you github

---
## [patevs/terminal](https://github.com/patevs/terminal)@[446f280757...](https://github.com/patevs/terminal/commit/446f2807573ffda411f548a519835d15cacdcd9b)
#### Sunday 2022-04-17 03:58:01 by Mike Griese

Try to silently fall back to a local monarch (#12825)

This is a crazy idea Dustin and I had.

> we can't repro this at will. But we kinda have an idea of where the deref is. We don't know if the small patch (throw, and try again) will fix it. We're sure that the "just fall back to an isolated monarch" will work. I'd almost rather take a build testing the small patch first, to see if that works

> This might seem crazy
> in 1.12, isolated monarch. In 1.13, "small patch". In 1.14, we can wait and see

I can write more details in the morning. It's 5pm here so if we want this today, here it is.

@dhowett double check my velocity flag logic here. Should be always true for Release, and off for Dev, Preview. 

* [x] closes #12774

---
## [MalefactorIX/Damage-Processing-System](https://github.com/MalefactorIX/Damage-Processing-System)@[8d58d0bf68...](https://github.com/MalefactorIX/Damage-Processing-System/commit/8d58d0bf6808ef1a702cea43f77e0da832a5ea35)
#### Sunday 2022-04-17 04:45:51 by MalefactorIX

Update and rename SRS.Register.v1.1.lsl to SRS.Register.v1.5.lsl

Applying a year and a half of updates in a single patch because fuck you.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[9f8d65768b...](https://github.com/treckstar/yolo-octo-hipster/commit/9f8d65768bbb0fe32c669750235321695353da85)
#### Sunday 2022-04-17 06:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [kumard3/next.js](https://github.com/kumard3/next.js)@[91146b23a2...](https://github.com/kumard3/next.js/commit/91146b23a21e33d54332a469f30afe6e6156cd65)
#### Sunday 2022-04-17 07:06:42 by Glenn Gijsberts

Make adjustment to cache config of with-apollo example (#32733)

## Description
This year we implemented the new Apollo config using this example. We recently moved to `getServerSideProps` as well, however, this was giving us some cache problems. The issue was that the cache was older than the actual data that was coming from the server side query. 

Because the `merge` of the cache in `apolloClient.js` is merging the existingCache in the initialState it will overwrite the "fresh" initialState with properties that already exists. This means that if you have something in your cache from previous client render, for example `user` with the value `null`, and you go to a new page and do a new query on the server which returns a value for the `user` field, it will still return `null` because of that `merge` function.

Since this was weird in our opinion, we've changed this in our own environment by always overwriting the existing cache with the new initialState, so that the initialState that is coming from a fresh server side query is overwriting. We thought it was a good idea to reflect this also in this example, because we couldn't think of a reason why the existing cache should overwrite fresh queries.

I've added a reproduction that shows what this is exactly about. I hope my description makes sense, let me know what you think!

## Reproduction of old scenario
Created a reproduction branch here: https://github.com/glenngijsberts/with-apollo-example. Using a different API than in the example, because of https://github.com/vercel/next.js/issues/32731.

1. checkout the example
2. yarn
3. yarn dev
4. visit http://localhost:3000/client-only
5. Hit "Update name". This will run a mutation that will update the cache automatically. Because I use a mocked API, the actual value on the API won't be updated, but this is actually the perfect scenario for the problem because in reality data can already change in the meantime when you're doing a new request.
6. Go to the SSR page
7. This will display two values: one is coming from the server side request (which is the latest data, because no cache is used in `getServerSideProps`) and the other is using the cache, which is outdated at that point, yet it's still returned because the old way of merging the cache was picking the existing cache over the initialState that was coming from the fresh server side query.

## Documentation / Examples

- [x] Make sure the linting passes by running `yarn lint`

---
## [zelon88/HRConvert2](https://github.com/zelon88/HRConvert2)@[7f6c454e02...](https://github.com/zelon88/HRConvert2/commit/7f6c454e0217d3275384d2c7f9b9e81da6486fbb)
#### Sunday 2022-04-17 07:24:28 by Justin Grimes

-v2.8. -Refactor the core.   -The original codebase was developed more than 4 years ago.     -The first unpublished experiments began in 2014.   -The "generation" of the HRConvert2 codebase until today was "Valkyrie".     -HonestRepair server side software comes in 3 generations.      -The first generation is unsafe to use. It is part of the "zelon88/HRToolkitTools" repo.       -It was called the "Genesis" engine because it was a proof-of-concept design.       -Hence the name "Genesis".     -The second generation is performant & safe to use but hard to maintain.       -It is called the "Valkyrie" engine because the runtime environment is "dynamically constructed".       -The "Valkyrie" in Norse mythology is any of a group of maidens who serves the god Odin.       -Valkyrie's were also the "Choosers of the slain" and decided who would die on the battlefield.       -Because the "Valkyrie" codebase is made up of one main core served by smaller cores that dynamically call dependencies.       -Hence the name "Valkyrie" is very fitting.     -The third and current generation is called "Diablo". It is secure, performant, & modular.       -"Diablo" is Spanish for Devil.        -The coding convention was introduced in the "Zelon88/HRCloud3" alpha repo and is currently under active development.        -If you're a major Cloud provider you should fear Diablo.   -Removes most core output except from log files or when logs cannot be reached.   -Uses a more consistent logging/error catching mechanism.   -Makes the core extremely modular and easy to work on.   -Adding new features is easier because logging and error functions are repeatable & consistent.   -Output is consistent.   -Logic flow is capable of withstanding non-fatal errors.     -Before we stopped execution for a lot more things.     -Logic behavior is more intuitive.   -Errors produced use incremental error numbers that can be easily adjusted or documented.   -Log generation happens earlier during execution, meaning more logs can be captured.     -More logs means problems are easier to identify & debug.   -Switching to a modern design will mean more interoperability of functions between applications.     -It becomes easier to apply simiilar patches to other products.   -I don't have to look at my old code anymore.     -Programmers grow. Programming styles change.      -I am a better programmer now than I was when I first wrote this.     -There will probably be bugs introduced and regressions but at least I'll enjoy working on the codebase again.     -This work needed to get done eventually anyway considering it will be needed for HRCloud3. -Added $Verbose config entry for controlling the amount of logging performed.   -If $Verbose is set to TRUE every significant operation will create a log entry.   -If $Verbose is set to FALSE only errors will create a log entry. -$VirusScan config entry now only accepts boolean values. -Improve formatting of config.php file for readability. -All conversions except archive conversions now receive 5 conversion attempts.   -Previously it was only for documents and the threshold was 10 attempts. -Reworked the way the document conversion engine is started and verified. -Removed a lot of unused variables. -Started using the same capitalization scheme as HRCloud3 (Diablo style).   -Lower case first letter variables denote highly limited scope.   -Upper case first letter variables denote very wide (almost global) scope.   -I know that PHP takes care of memory cleanup, and I know how variable scope works in functions.     -I also don't care.      -Doing the capitalization scheme and manually NULL'ing + unsetting variables helps me keep track of variables.     -I came up with this scheme exactly because I kept seeing dead variables in my code and I wanted it to stop.     -This forces accountability for all variables and puts visiblity on most of them.     -So when one of them isn't used anywhere it kind of stands out. -Refactored Javascript a tiny bit. -Now the core will remember when you leave and come back for a short while. -Added unique identifier for logs.    -Makes searching logs much easier because requests group together. -Core now captures the stdout of it's dependencies.   -Writes to log if $Verbose is set to TRUE. -Changed extraction behaviour for archive conversions.   -Archive conversions where the destination folder already exists will have the new contents ADDED to the original archive instead of replacing them.   -You can now build archives in this fashion, admittedly it is not for the faint of heart. -Remove sanitizeCore.php.   -This has been replaced by the verifyGlobals() function in convertCore.php.   -This was a suggestion made about 5 years ago on Reddit. It finally happened! -I worked on this commit for 30 hours straight with no sleep.   -With only one consecutive 90 minute break to take a phone call.   -Then I took a 3 hour nap and finished the rest, over the next 8 hours.   -I am recovering from a broken leg and surgery to fix it and I still have a couple more weeks to go.   -Send halp!

-v2.8.
-Refactor the core.
  -The original codebase was developed more than 4 years ago.
    -The first unpublished experiments began in 2014.
  -The "generation" of the HRConvert2 codebase until today was "Valkyrie".
    -HonestRepair server side software comes in 3 generations.
    -The first generation is unsafe to use. It is part of the "zelon88/HRToolkitTools" repo.
      -It was called the "Genesis" engine because it was a proof-of-concept design.
      -Hence the name "Genesis".
    -The second generation is performant & safe to use but hard to maintain.
      -It is called the "Valkyrie" engine because the runtime environment is "dynamically constructed".
      -The "Valkyrie" in Norse mythology is any of a group of maidens who serves the god Odin.
      -Valkyrie's were also the "Choosers of the slain" and decided who would die on the battlefield.
      -Because the "Valkyrie" codebase is made up of one main core served by smaller cores that dynamically call dependencies.
      -Hence the name "Valkyrie" is very fitting.
    -The third and current generation is called "Diablo". It is secure, performant, & modular.
      -"Diablo" is Spanish for Devil.
      -The coding convention was introduced in the "Zelon88/HRCloud3" alpha repo and is currently under active development.
      -If you're a major Cloud provider you should fear Diablo.
  -Removes most core output except from log files or when logs cannot be reached.
  -Uses a more consistent logging/error catching mechanism.
  -Makes the core extremely modular and easy to work on.
  -Adding new features is easier because logging and error functions are repeatable & consistent.
  -Output is consistent.
  -Logic flow is capable of withstanding non-fatal errors.
    -Before we stopped execution for a lot more things.
    -Logic behavior is more intuitive.
  -Errors produced use incremental error numbers that can be easily adjusted or documented.
  -Log generation happens earlier during execution, meaning more logs can be captured.
    -More logs means problems are easier to identify & debug.
  -Switching to a modern design will mean more interoperability of functions between applications.
    -It becomes easier to apply simiilar patches to other products.
  -I don't have to look at my old code anymore.
    -Programmers grow. Programming styles change.
    -I am a better programmer now than I was when I first wrote this.
    -There will probably be bugs introduced and regressions but at least I'll enjoy working on the codebase again.
    -This work needed to get done eventually anyway considering it will be needed for HRCloud3.
-Added $Verbose config entry for controlling the amount of logging performed.
  -If $Verbose is set to TRUE every significant operation will create a log entry.
  -If $Verbose is set to FALSE only errors will create a log entry.
-$VirusScan config entry now only accepts boolean values.
-Improve formatting of config.php file for readability.
-All conversions except archive conversions now receive 5 conversion attempts.
  -Previously it was only for documents and the threshold was 10 attempts.
-Reworked the way the document conversion engine is started and verified.
-Removed a lot of unused variables.
-Started using the same capitalization scheme as HRCloud3 (Diablo style).
  -Lower case first letter variables denote highly limited scope.
  -Upper case first letter variables denote very wide (almost global) scope.
  -I know that PHP takes care of memory cleanup, and I know how variable scope works in functions.
    -I also don't care.
    -Doing the capitalization scheme and manually NULL'ing + unsetting variables helps me keep track of variables.
    -I came up with this scheme exactly because I kept seeing dead variables in my code and I wanted it to stop.
    -This forces accountability for all variables and puts visiblity on most of them.
    -So when one of them isn't used anywhere it kind of stands out.
-Refactored Javascript a tiny bit.
-Now the core will remember when you leave and come back for a short while.
-Added unique identifier for logs.
  -Makes searching logs much easier because requests group together.
-Core now captures the stdout of it's dependencies.
  -Writes to log if $Verbose is set to TRUE.
-Changed extraction behaviour for archive conversions.
  -Archive conversions where the destination folder already exists will have the new contents ADDED to the original archive instead of replacing them.
  -You can now build archives in this fashion, admittedly it is not for the faint of heart.
-Remove sanitizeCore.php.
  -This has been replaced by the verifyGlobals() function in convertCore.php.
  -This was a suggestion made about 5 years ago on Reddit. It finally happened!
-I worked on this commit for 30 hours straight with no sleep.
  -With only one consecutive 90 minute break to take a phone call.
  -Then I took a 3 hour nap and finished the rest, over the next 8 hours.
  -I am recovering from a broken leg and surgery to fix it and I still have a couple more weeks to go.
  -Send halp!

---
## [LooserRIP/LooserRIP.github.io](https://github.com/LooserRIP/LooserRIP.github.io)@[2ca237bc50...](https://github.com/LooserRIP/LooserRIP.github.io/commit/2ca237bc50377a1d60a6abec1c4ba91e971717ce)
#### Sunday 2022-04-17 07:44:49 by LooserRIP

OH MY GOD IS THAT A SECRET UNLIMITED MODE HOLY FUCKING SHIT???

---
## [Goratrix/goratrix-crawl](https://github.com/Goratrix/goratrix-crawl)@[af92d4a5d6...](https://github.com/Goratrix/goratrix-crawl/commit/af92d4a5d6ba2f841e8bfdf8639f77a784fcaeae)
#### Sunday 2022-04-17 08:06:37 by Nicholas Feinberg

Make Hell Knights evil again (catern)

Lost this when they lost Pain.

Slightly hacky.

---
## [rentruewang/datasets](https://github.com/rentruewang/datasets)@[a8fa7cfe95...](https://github.com/rentruewang/datasets/commit/a8fa7cfe95e06c8a667c4d7c5b7c7287b7e9ac4f)
#### Sunday 2022-04-17 08:29:56 by RenChu Wang

Multi-GPU support for `FaissIndex` (#3721)

* 🎉 This commit fixes huggingface/datasets#3716

This commit adds handling for faiss indices that run on multiple GPUs.

* 🤕 Stupid mistake in that index isn't returned in the function handling device.

Now it's fixed. Hopefully the PR isn't merged yet!

* 🗎 Updated documents to reflect changes I made in the code.

Update `device`'s document to include negative numbers and lists.

* 1️⃣ The line should not exceed length: 119

It seems that this is what circle CI checked anyways.

* 🥴 Apply suggestions from code review

Missed it the first time :)

Co-authored-by: Albert Villanova del Moral <8515462+albertvillanova@users.noreply.github.com>

* 🛠️ Fixed my fixes.

Updated code to address concerns.

* 🇫 Update src/datasets/search.py

Using f-strings in docs.

Co-authored-by: Quentin Lhoest <42851186+lhoestq@users.noreply.github.com>

Co-authored-by: Albert Villanova del Moral <8515462+albertvillanova@users.noreply.github.com>
Co-authored-by: Quentin Lhoest <42851186+lhoestq@users.noreply.github.com>

---
## [allusion-app/Allusion](https://github.com/allusion-app/Allusion)@[aa538a9d5a...](https://github.com/allusion-app/Allusion/commit/aa538a9d5a8d873dadcc7dfef0453046fc0c4f12)
#### Sunday 2022-04-17 10:03:00 by hummingly

One context menu to rule them all
* Back when we still used BlueprintJS, React portals were slow or
BlueprintJS' implementation. We talk about seconds to open a context
menu.
* Furthermore, portals do not inherit styles since they are out of tree
:( BUT you can solve that with passing the top level class on creation
and always update that.
* Back then I was also on an explicit everything trip which is how the
useContextMenu hook was born. However, it has its merit if you do not
know what the perfect API looks like (which is kinda always the case).
* Now I don't hate portals anymore but I still deleted them lol
* The context menu will be now a sibling element which solves most
overlap issues.
* Well, except for tooltips but this is such a weird edge case. Who
wants to read tooltips after opening context menus?
* Either way the React Context API pretty much fixes all API issues
which stem from React fundamental designs (isolated components and
and tree like state flow == PITA for graph like state).

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[ebd6b5c216...](https://github.com/mrakgr/The-Spiral-Language/commit/ebd6b5c216221f190255a8fc4af33627fa035674)
#### Sunday 2022-04-17 10:08:15 by Marko Grdinić

"11am. I got up an hour ago and have been playing with beveling the cube. I figured out something interesting. When beveling two adjacent edges in % mode, it matters hugely what the angle between them. It it is 45 degrees or less, it won't slide along the opposing edge.

11:45am. At any rate, enough playing with the damn cube. When you bevel stuff on the surface of the cube, you get some bizzare results. It seems the % mode has a lot of stuff built in to automatically select which edges to bevel. It did not even occur to me to wonder that it is strange that the other side is not being beveled yesterday, but maybe it should have. At any rate, I do not need to understand this. All I need to know is what result I want to get. I can just place the guiding edges after that.

If an edge I want is not being selected for splitting, I can just slide it manually into place before doing the bevel.

The functionality of this is really remarkable

11:55am. Enough of studying this. Maybe I am not really suited to art as I get engrossed in these small matter too easily like in programming. In programming this is good, but I am not sure what to think about this here.

12pm. I checked the emails when I got up, but it was just a bunch of NetMQ issues being auto closed. I completely forgot about those by now. No reply to that sponsorship message yet. Nevermind it.

12:05pm. Let me take a break here.

It seems I am into learning fundamental things, but not so much into making the actual props. I felt yesterday that I could really take off running and close on time today, but spenting a bunch of time playing with the cube threw me off again.

Let me just get breakfast.

Incidentally, Estab Life is the new Milky Holmes. It does not have much in common with it in terms of plot or characters, but the spirit is there. Despite being CGI, if Girls Frontline had its quality, it would have been great."

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[4d54e290db...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/4d54e290db51697d12fc54a6bbb0a376f43b7280)
#### Sunday 2022-04-17 10:21:04 by Zandario

Security TGUI (#3886)

* e

* Fuck it, I'm pushing it.

* Fuck you

* Refactored Brigdoors, updated their UI, does annoucements

Also updated logging a little bit and documented some things.

* Multitool sync

---
## [zhcheng828/postgres](https://github.com/zhcheng828/postgres)@[ec62cb0aac...](https://github.com/zhcheng828/postgres/commit/ec62cb0aac5ba31a82339606009ddbd7eb00e2ac)
#### Sunday 2022-04-17 10:28:43 by Tom Lane

Revert applying column aliases to the output of whole-row Vars.

In commit bf7ca1587, I had the bright idea that we could make the
result of a whole-row Var (that is, foo.*) track any column aliases
that had been applied to the FROM entry the Var refers to.  However,
that's not terribly logically consistent, because now the output of
the Var is no longer of the named composite type that the Var claims
to emit.  bf7ca1587 tried to handle that by changing the output
tuple values to be labeled with a blessed RECORD type, but that's
really pretty disastrous: we can wind up storing such tuples onto
disk, whereupon they're not readable by other sessions.

The only practical fix I can see is to give up on what bf7ca1587
tried to do, and say that the column names of tuples produced by
a whole-row Var are always those of the underlying named composite
type, query aliases or no.  While this introduces some inconsistencies,
it removes others, so it's not that awful in the abstract.  What *is*
kind of awful is to make such a behavioral change in a back-patched
bug fix.  But corrupt data is worse, so back-patched it will be.

(A workaround available to anyone who's unhappy about this is to
introduce an extra level of sub-SELECT, so that the whole-row Var is
referring to the sub-SELECT's output and not to a named table type.
Then the Var is of type RECORD to begin with and there's no issue.)

Per report from Miles Delahunty.  The faulty commit dates to 9.5,
so back-patch to all supported branches.

Discussion: https://postgr.es/m/2950001.1638729947@sss.pgh.pa.us

---
## [Akatap26/B2B-Marketing-Translation-to-Spanish](https://github.com/Akatap26/B2B-Marketing-Translation-to-Spanish)@[f6b3f0208e...](https://github.com/Akatap26/B2B-Marketing-Translation-to-Spanish/commit/f6b3f0208e7cb94f0329d0ec69716c31daff83c0)
#### Sunday 2022-04-17 10:55:24 by Aikaterini Katapodi

One more file uploaded

HAPPY EASTER! May God and Jesus Bless you and your life in all terms. I am not forgetting you, as last time, I'll be uploading files, actually target files in Spanish, as translation of book uploaded as source file in English,
See you online soon again

---
## [introt/docs](https://github.com/introt/docs)@[2f0ddec7e3...](https://github.com/introt/docs/commit/2f0ddec7e3483087a91e5613b6522124e463cefb)
#### Sunday 2022-04-17 12:08:19 by introt

Automate site building via GitHub Actions

Could've saved some time by just using a ready-made one from the Marketplace, but boy did I gain some troubleshooting experience doing it myself :D

---
## [Nurb432/zero-riscy](https://github.com/Nurb432/zero-riscy)@[c15f3b8888...](https://github.com/Nurb432/zero-riscy/commit/c15f3b88883781808eaa96bda205a9bdaff5eb98)
#### Sunday 2022-04-17 13:02:48 by Rupert Swarbrick

[icache] Define some fake DPI functions to simplify linking

This is triggered by the fact that if the ICache parameter is false
then we don't instantiate the ibex_icache module. For verilator
simulations, the module is then discarded entirely, which means that
its two DPI functions are not defined. That's unfortunate because
we're also compiling the code in scrambled_ecc32_mem_area.cc, which
expects the functions to be defined.

The obvious solution (don't include scrambled_ecc32_mem_area.cc if you
don't have an icache) isn't easy to do, because FuseSoc doesn't
currently allow us to use parameters to configure its dependency
tree (see fusesoc issue 438 for a discussion).

The super-clever solution that I came up with before(!) was to declare
these symbols as weak in the C++ code. That way, we can do a runtime
check to make sure that no-one is silly enough to call them without an
icache, but everything will still build properly either way.

Unfortunately, that doesn't work well with xcelium simulations.
Xcelium turns out to compile all the C++ code into one .so library and
generate functions for exported DPI functions in another. These two
solibs then get loaded at runtime with dlopen(). But this doesn't work
with weak symbols: in fact, it seems you end up with the C++ version
every time. Boo!

So let's be stupider about it and define (bogus) versions of the DPI
functions in this case. Fortunately, both of them are designed to
return zero on failure so we can just return zero and needn't worry
too much.

The idea is that when this lands, we can revert the OpenTitan change
that switched the C++ code to using weak symbols and Xcelium
simulations will start working.

---
## [Furball-Engine/Furball.Vixie](https://github.com/Furball-Engine/Furball.Vixie)@[61c1415353...](https://github.com/Furball-Engine/Furball.Vixie/commit/61c141535350bb5d5bca1c404eb192d0e79013de)
#### Sunday 2022-04-17 14:15:25 by Furball

fuck fss fuck sourcerect fuck graphics programming fuck my entire life thank you very much

---
## [RoostersNest/qb-vehiclekeys](https://github.com/RoostersNest/qb-vehiclekeys)@[757fdd0859...](https://github.com/RoostersNest/qb-vehiclekeys/commit/757fdd0859013e45f9d432fa894f0ecb03d8bbf5)
#### Sunday 2022-04-17 15:44:29 by ItsANoBrainer

Proper Refactor

Refactored the entire resource because the key system was not working.

No longer does a server callback 10 or so times a second, on top of other bad practices.

Tested pretty much everything with my devs, but there might be some weird issues we havnt found. Please lookover as I've been going crazy with the small tedious issues I've come across doing this.

Throwing this up to get feedback, and for people to use who want it.

Features:

- Keys are saved server side, and sent to each client when they are added or removed, as well as on character selection. This allows characters to leave and come back in the same server uptime session and still have the same keys
- Keys are only pulled from the server once on character load
- Giving keys has 3 types, /givekeys with an id will attempt to give keys you have to an id, not including an id will try to give it to the closest person, and if you're in a vehicle it will give to everyone
- Can only give keys to vehicles you have keys to
- Server event to force acquire keys to a plate for a person (for lockpicking/stealing/spawning, etc.)
- Can Carjack an NPC with a gun, has different percentages to work based on weapon (config)
- Take keys from dead npc drivers
- Can lockpick a car to unlock the doors
- Can hotwire a car if you're in the driver seat of the vehicle you dont have keys to to get keys
- Keeps the engine of a vehicle off if you dont have keys to it (allows other resources to attempt to toggle car engine without needing to interface if you have keys or not)
- Vehicle blacklist system for vehicles you dont want to be lockable (always unlocked)
- Police Alerts from lockpicking/hotwiring/carjacking
- Export to check if you have keys to a vehicle
- Locking/unlocking with hotkey
- Locking/unlocking and giving keys uses a custom GetVehicleInDirection you are facing for realism/accuracy
- Fully compatible with old resource. Has an event handler for 'vehiclekeys:client:SetOwner' in which it gives keys for that plate
- Some other shit I probably forgot

TODO:
- Add LOCALE support
- Stop peds from wanting to get back into the vehicle they just got carjacked out of as they're fleeing

---
## [silont-project/kernel_xiaomi_sdm439](https://github.com/silont-project/kernel_xiaomi_sdm439)@[b0f490c677...](https://github.com/silont-project/kernel_xiaomi_sdm439/commit/b0f490c677c87c377773523046cbc1b3bb06d7e7)
#### Sunday 2022-04-17 16:14:41 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

Signed-off-by: sweetyicecare <gabrielseedev@outlook.com>
Signed-off-by: Jprimero15 <jprimero155@gmail.com>
Signed-off-by: Joel Gómez <nahuelgomez329@gmail.com>

Conflicts:
	mm/swapfile.c
	mm/swap.c

---
## [SonicProYT/ScratchCraftAndDashNEW](https://github.com/SonicProYT/ScratchCraftAndDashNEW)@[d92e11e16b...](https://github.com/SonicProYT/ScratchCraftAndDashNEW/commit/d92e11e16b2aff4bfd7c2e169949e19ed9b1be98)
#### Sunday 2022-04-17 17:10:37 by Matt 3

Dumbass example for the stupid shitty ass thing auefhirwyjneklMOQp;waki

oh also i got a new keyboard

Huo JI BT-885 Blue Switches RGB :D

---
## [Lunarequest/servers-config](https://github.com/Lunarequest/servers-config)@[f1f937c559...](https://github.com/Lunarequest/servers-config/commit/f1f937c55946cd3d1a320ce3a65c3e118269aea3)
#### Sunday 2022-04-17 17:39:16 by Luna D. Dragon

god damn that hardneding bull broke my server. I hate this

---
## [outfrost/ld50](https://github.com/outfrost/ld50)@[5560f3f2a7...](https://github.com/outfrost/ld50/commit/5560f3f2a7915403e1f0b43c0e099f79c892d39f)
#### Sunday 2022-04-17 17:48:33 by Ryan

Attachment 9 changed to accept 2 orientations

Removed the 'Fuck You' pinout to allow attachment to be accepted at 0 and 180 degree positions

---
## [Fargowilta/FargowiltasSouls](https://github.com/Fargowilta/FargowiltasSouls)@[29d3bebeab...](https://github.com/Fargowilta/FargowiltasSouls/commit/29d3bebeabcc588562d840de13b036e9b3cb3ec9)
#### Sunday 2022-04-17 18:13:17 by terrynmuse

fixed maul still causing "-5 max life" to appear when youre not actually losing max life
cactus ench nerfed
 obeys static iframes
 enemies can only be marked as needled by needles
fixed devi trying to stone dead players
fixed devi floating directly into player while doing shadowbeam attack
nerfed wandering eye fish to spawn demon eyes, not wandering eyes
queen bee can actually despawn in multiplayer
fixed mutant's gift not spawning devi properly
skeletron can change targets after a spin (was locked onto one person until they die)
skeletron regrows arms at 25%
giant and ice tortoise can yeet you like pinky
lightning rod rains lightning while going out as intended, not coming back

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[271d04f02c...](https://github.com/mrakgr/The-Spiral-Language/commit/271d04f02c125b494c6d8a7af18675b03d7ed564)
#### Sunday 2022-04-17 18:57:26 by Marko Grdinić

"1pm. Let me do chores here and then I'll get started on making the monitor.

1:45pm. I need to clear my head. Forget the distractions. For the next couple of hours, just focus on being awesome at 3d art. That is the way to go.

There is no need to think about it too much. Heaven's Key will get made if I can become good enough at art. Otherwise I'll have to get a regular job. It has only been 6.5 months so far. My pace of development has not been bad at all. If I go for a six month stretch where I am not getting better, then I can start to get worried.

2:35pm. Gahhhh, I am running into another unforeseen problem. The subdiv workflow is fine in general, but now that I am trying to make an indent I realized something. It is creating these ridiculous flaps around the edges which creases of 1 do not resolve.

2:45pm. Now I just relized that some geometry to the side is messed up.

Focus me, do not give into despair and scrap everything. You have the unfuck tool for a reason!

2:55pm. No let me start from scratch.

I didn't think thigs would turn out like this.

3pm. Let me take a break.

3:15pm. I am back. When I first started on the monitor, I did a loop cut, and then a bevel, but the % mode for some reason did not work!

Now it works. Why didn't it work earlier?

This is so confusing. I didn't expect to encounter this kind of difficulty.

It seems the path to becoming a skilled 3d artist is a long and winding one.

3:30pm. Let me get into the habit of making copies periodically. The undo will only get me so far.

4:25pm. Let me take a break here. I am still stuck on this.

I need to work less and think more.

4:40pm. This has been happening way too often lately. I run into difficulty and instead of stopping to think, I make an endless amount of experiments to try and wrap my head around it.

Let me make some more.

5:10pm. My whole day has gone kaput because of this. There is one thing I can say with certainty - I do not understand subdivision surfaces at all. What the hell?

Forget modeling.

https://youtu.be/mfp1Z1mBClc
Implementing Catmull-Clark Subdivision - Introduction & Rules

Let me study subdivision for a bit. The way subdivion behaves is too unpredictable, I have zero idea what is going on anymore.

https://youtu.be/mfp1Z1mBClc?t=119
> Real progress is not by speed, but by momentum.

This is a good quote.

https://youtu.be/mfp1Z1mBClc?t=201

Ah, I see. This is one way of converting a ngon to a quad.

6:40pm. I figured it out. I finally know make that dedent. Let me try it again.

8:30pm. I got it perfectly now. It was really simple, but I was too retarded to do the right thing. All I had to do to get the right beveling was to bevel the edges and then join the corners with the other side. It is not complicated at all and yet it had me scratching my head all day. Sigh.

The really embarassing thing is that I was messing with bevels for how long now and I still could not figure out the sequence of actions needed to get the result that I want. I have no excuse.

8:40pm. I'll do beter tomorrow. I really have a grasp on how to use bevels effectively with subdivision surfaces now.

I was in the zone the whole day today, and hopefully tomorrow I'll be able to make significant progress on the prop tomorrow. I tend to do well when I am in the zone programming. In 3d art, I am yet to cross the significant threeshold of experience in order to be able to do things smoothly. But I am really close to cross the threshold. I think it should be smooth sailing from here.

The monitor is unique in being one ove of the very few props that needs subdiv surfaces in the room. Its form has a lot of curviness to it. The rig on the other hand has a lot of decal details which will be a whole different challenge that I will have to tackle. For that one I might have to install Boxcutter, or maybe just Hops will do.

The only other prop that would require the subsurf workflow might be the earphones. Maybe the glass as well, but I can't think of anything else. The radiator? There isn't much.

But there are a lot of props in the room. I will continue training myself on them until I feel satisfied. What I am doing now is no different from a regular artist doing still lives. It is a good way of getting proficiency and confidence in modeling. It might seem trivial, but it is not trivial practice by any means.

Now let me take off for the day. It is time for rest."

---
## [Hathoom/Submarine-Pirates](https://github.com/Hathoom/Submarine-Pirates)@[1258935b7b...](https://github.com/Hathoom/Submarine-Pirates/commit/1258935b7bfbdd324a2faacb5d160a6662039e91)
#### Sunday 2022-04-17 21:21:10 by ATimpe

Merge pull request #37 from Hathoom/UI

fuck you unity

---
## [kuroringo90/android_kernel_xiaomi_sm8150](https://github.com/kuroringo90/android_kernel_xiaomi_sm8150)@[0286613dd9...](https://github.com/kuroringo90/android_kernel_xiaomi_sm8150/commit/0286613dd93ca9c81809f9920eacc31fe74c2b27)
#### Sunday 2022-04-17 22:08:59 by Peter Zijlstra

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
Signed-off-by: alanndz <alanndz7@gmail.com>

---
## [jukibom/FlyDangerous](https://github.com/jukibom/FlyDangerous)@[3e982e4b15...](https://github.com/jukibom/FlyDangerous/commit/3e982e4b156061ad9d0de694875769e0a78ca78d)
#### Sunday 2022-04-17 23:11:37 by Jay Faulkner

fix: anti-clipping positioning code shifted first-start player forward

well fucking hell that was an awful one to figure out - turns out the multiplayer code for shifting the player out of the way of one-another was checking against itself at the start and pushing the player forward but only on the first go - this meant you were always ~40 meters ahead before a restart.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[4652d4bb63...](https://github.com/tgstation/tgstation/commit/4652d4bb63cec6f73bc46a0ea75d867d235107d1)
#### Sunday 2022-04-17 23:14:23 by Jolly

Updates The Derelict to some modern standards, also some turf edits (#66045)

Brings The Derelict up to speed with some of our new mapping tools and stuff.
This also places nearstation turf in certain areas, as well as general turf clean up.
Also cleans up the absurdly placed black holes of light that were over space tiles.
Girder/Grill spawners were placed in certain locations (mostly on external girlls).
I also remapped the main AI chambers SMES power to not go through the fucking wall, as a trade off, its no longer wired round start, and the two pieces of cable that are automatically in the room have been swapped out for two (2) five cables each. Its not enough to reach the main area, but god fuck wires running through walls.

As an aside, some of plating on the outside, walls include, does look weird being full bright like this. I'm neutral for the most part. Theres a weird fine balance that needs to be maintained with some of the areas being open to space, I've opted to keep lattice as nearstation and any thing plating and above as turfed (excluding plating that is solely in space).

I'll be redoing the turfs of this later, sprite wise.

Images

---

