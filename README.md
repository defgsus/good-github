## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-21](docs/good-messages/2023/2023-12-21.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,492,779 were push events containing 3,603,088 commit messages that amount to 253,832,503 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 69 messages:


## [authenyoo/authenkey](https://github.com/authenyoo/authenkey)@[c5369c5458...](https://github.com/authenyoo/authenkey/commit/c5369c545825e0ecaa63a56c573ed498dfd6ec7a)
#### Thursday 2023-12-21 00:31:29 by authenyoo

i just changed one script this might not be able to run at all but im not testing that do it yourself fuck you

---
## [sailfishos-mirror/git](https://github.com/sailfishos-mirror/git)@[a1fbe26a0c...](https://github.com/sailfishos-mirror/git/commit/a1fbe26a0c2bb8ba84c3976023e4ded4cf94608e)
#### Thursday 2023-12-21 00:41:12 by Elijah Newren

completion: avoid user confusion in non-cone mode

It is tempting to think of "files and directories" of the current
directory as valid inputs to the add and set subcommands of git
sparse-checkout.  However, in non-cone mode, they often aren't and using
them as potential completions leads to *many* forms of confusion:

Issue #1. It provides the *wrong* files and directories.

For
    git sparse-checkout add
we always want to add files and directories not currently in our sparse
checkout, which means we want file and directories not currently present
in the current working tree.  Providing the files and directories
currently present is thus always wrong.

For
    git sparse-checkout set
we have a similar problem except in the subset of cases where we are
trying to narrow our checkout to a strict subset of what we already
have.  That is not a very common scenario, especially since it often
does not even happen to be true for the first use of the command; for
years we required users to create a sparse-checkout via
    git sparse-checkout init
    git sparse-checkout set <args...>
(or use a clone option that did the init step for you at clone time).
The init command creates a minimal sparse-checkout with just the
top-level directory present, meaning the set command has to be used to
expand the checkout.  Thus, only in a special and perhaps unusual cases
would any of the suggestions from normal file and directory completion
be appropriate.

Issue #2: Suggesting patterns that lead to warnings is unfriendly.

If the user specifies any regular file and omits the leading '/', then
the sparse-checkout command will warn the user that their command is
problematic and suggest they use a leading slash instead.

Issue #3: Completion gets confused by leading '/', and provides wrong paths.

Users often want to anchor their patterns to the toplevel of the
repository, especially when listing individual files.  There are a
number of reasons for this, but notably even sparse-checkout encourages
them to do so (as noted above).  However, if users do so (via adding a
leading '/' to their pattern), then bash completion will interpret the
leading slash not as a request for a path at the toplevel of the
repository, but as a request for a path at the root of the filesytem.
That means at best that completion cannot help with such paths, and if
it does find any completions, they are almost guaranteed to be wrong.

Issue #4: Suggesting invalid patterns from subdirectories is unfriendly.

There is no per-directory equivalent to .gitignore with
sparse-checkouts.  There is only a single worktree-global
$GIT_DIR/info/sparse-checkout file.  As such, paths to files must be
specified relative to the toplevel of a repository.  Providing
suggestions of paths that are relative to the current working directory,
as bash completion defaults to, is wrong when the current working
directory is not the worktree toplevel directory.

Issue #5: Paths with special characters will be interpreted incorrectly

The entries in the sparse-checkout file are patterns, not paths.  While
most paths also qualify as patterns (though even in such cases it would
be better for users to not use them directly but prefix them with a
leading '/'), there are a variety of special characters that would need
special escaping beyond the normal shell escaping: '*', '?', '\', '[',
']', and any leading '#' or '!'.  If completion suggests any such paths,
users will likely expect them to be treated as an exact path rather than
as a pattern that might match some number of files other than 1.

However, despite the first four issues, we can note that _if_ users are
using tab completion, then they are probably trying to specify a path in
the index.  As such, we transform their argument into a top-level-rooted
pattern that matches such a file.  For example, if they type:
   git sparse-checkout add Make<TAB>
we could "complete" to
   git sparse-checkout add /Makefile
or, if they ran from the Documentation/technical/ subdirectory:
   git sparse-checkout add m<TAB>
we could "complete" it to:
   git sparse-checkout add /Documentation/technical/multi-pack-index.txt
Note in both cases I use "complete" in quotes, because we actually add
characters both before and after the argument in question, so we are
kind of abusing "bash completions" to be "bash completions AND
beginnings".

The fifth issue is a bit stickier, especially when you consider that we
not only need to deal with escaping issues because of special meanings
of patterns in sparse-checkout & gitignore files, but also that we need
to consider escaping issues due to ls-files needing to sometimes quote
or escape characters, and because the shell needs to escape some
characters.  The multiple interacting forms of escaping could get ugly;
this patch makes no attempt to do so and simply documents that we
decided to not deal with those corner cases for now but at least get the
common cases right.

Signed-off-by: Elijah Newren <newren@gmail.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [bhammy27/Building-Lego-s-Legacy](https://github.com/bhammy27/Building-Lego-s-Legacy)@[7b511e315c...](https://github.com/bhammy27/Building-Lego-s-Legacy/commit/7b511e315c6c6d93394d63efbe0effbe43ce65d9)
#### Thursday 2023-12-21 00:45:24 by Bryan Hamilton

Update README.md

## Overview:
Over the weekend, my 6-year-old nephew and I spent a few hours playing with Legos.  As he randomly connected the multicolored bricks, I built a little car and a house.  After over an hour of stacking bricks, he then spent the rest of the afternoon playing with the car I made.  I began to wonder, how such a simple toy that my parents and I played with still popular today?  Being an inquisitive Data Analyst, I found and analyzed data which covers Lego's production from 1950-2017.

My role in this case study is that of a toy company marketing analyst.  The toy industry faces a challenge in creating toys which captivates children's interest for a month or two, let alone 7+ generations.  My direct supervisor tasked me with the challenge of analyzing Legos production trends and find any insight that we could use to create a popular generational toy.  

Using PostgreSQL and Jupyter Notebook, with Python for visualization, the following questions will be answered:

1. What is the average number of Lego parts over total time span and per year?

2. What is the average number of Lego sets released per from 1950-2017?
3. Are there any trends with the sets produced and number of parts produced?

---
## [discourse/discourse](https://github.com/discourse/discourse)@[cbc28e8e33...](https://github.com/discourse/discourse/commit/cbc28e8e337acc740487bc9cf5c263b3eaba6493)
#### Thursday 2023-12-21 01:07:37 by David Taylor

Enable Embroider/Webpack code spliting for Wizard (#24919)

(extracted from #23678)

* Move Wizard back into main app, remove Wizard addon
* Remove Wizard-related resolver or build hacks
* Install and enable `@embroider/router`
* Add "wizard" to `splitAtRoutes`

In a fully optimized Embroider app, route-based code splitting more
or less Just Work™ – install `@embroider/router`, subclass from it,
configure which routes you want to split and that's about it.

However, our app is not "fully optimized", by which I mean we are
not able to turn on all the `static*` flags.

In Embroider, "static" means "statically analyzable". Specifically
it means that all inter-dependencies between modules (files) are
explicitly expressed as `import`s, as opposed to `{{i18n ...}}`
magically means "look for the default export in app/helpers/i18n.js"
or something even more dynamic with the resolver.

Without turning on those flags, Embroider behaves conservatively,
slurps up all `app` files eagerly into the primary bundle/chunks.
So, while you _could_ turn on route-based code splitting, there
won't be much to split.

The commits leading up to this involves a bunch of refactors and
cleanups that 1) works perfectly fine in the classic build, 2) are
good and useful in their own right, but also 3) re-arranged things
such that most dependencies are now explicit.

With those in place, I was able to move all the wizard code into
the "app/static" folder. Embroider does not eagerly pull things from
this folder into any bundle, unless something explicitly "asks" for
them via `imports`. Conversely, things from this folder are not
registered with the resolver and are not added to the `loader.js`
registry.

In conjunction with route-based code splitting, we now have the
ability to split out islands of on-demand functionalities from the
main app bundle.

When you split a route in Embroider, it automatically creates a
bundle/entrypoint with the relevant routes/templates/controllers
matching that route prefix. Anything they import will be added to
the bundle as well, assuming they are not already in the main app
bundle, which is where the "app/static" folder comes into play.

The "app/static" folder name is not special. It is configured in
ember-cli-build.js. Alternatively, we could have left everything
in their normal locations, and add more fine-grained paths to the
`staticAppPaths` array. I just thought it would be easy to manage
and scale, and less error-prone to do it this way.

Note that putting things in `app/static` does not guarantee that
it would not be part of the main app bundle. For example, if we
were to add an `import ... from "app/static/wizard/...";` in a
main bundle file (say, `app.js`), then that chunk of the module
graph would be pulled in. (Consider using `await import(...)`?)

Overtime, we can build better tooling (e.g. lint rules and babel
macros to make things less repetitive) as we expand the use of
this pattern, but this is a start.

Co-authored-by: Godfrey Chan <godfreykfc@gmail.com>

---
## [openai/evals](https://github.com/openai/evals)@[f20c305dc7...](https://github.com/openai/evals/commit/f20c305dc743eb545a57fd19b3b59426b9171465)
#### Thursday 2023-12-21 01:09:38 by Erik Ritter

Add MMMU evals and runner (#1442)

## Eval details 📑

### Eval name

MMMU

### Eval description
A multi-modal version of MMLU published here:
https://arxiv.org/pdf/2311.16502.pdf

### What makes this a useful eval?
Tests a variety of subjects, along with image recognition and
comprehension

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Multimodal, covers many subjects 

## Eval structure 🏗️

Your eval should

- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

### Eval JSON data

Dataset defined here: https://huggingface.co/datasets/MMMU/MMMU

### Eval Results

on `gpt-4-vision-preview`:

```
{
  "mmmu-accounting": 0.5333333333333333,
  "mmmu-agriculture": 0.6333333333333333,
  "mmmu-architecture-and-engineering": 0.16666666666666666,
  "mmmu-art": 0.7333333333333333,
  "mmmu-art-theory": 0.8333333333333334,
  "mmmu-basic-medical-science": 0.6,
  "mmmu-biology": 0.43333333333333335,
  "mmmu-chemistry": 0.43333333333333335,
  "mmmu-clinical-medicine": 0.6333333333333333,
  "mmmu-computer-science": 0.6333333333333333,
  "mmmu-design": 0.7666666666666667,
  "mmmu-diagnostics-and-laboratory-medicine": 0.3,
  "mmmu-economics": 0.6333333333333333,
  "mmmu-electronics": 0.4,
  "mmmu-energy-and-power": 0.36666666666666664,
  "mmmu-finance": 0.43333333333333335,
  "mmmu-geography": 0.4,
  "mmmu-history": 0.6666666666666666,
  "mmmu-literature": 0.9,
  "mmmu-manage": 0.6,
  "mmmu-marketing": 0.6333333333333333,
  "mmmu-materials": 0.26666666666666666,
  "mmmu-math": 0.5,
  "mmmu-mechanical-engineering": 0.23333333333333334,
  "mmmu-music": 0.36666666666666664,
  "mmmu-pharmacy": 0.7666666666666667,
  "mmmu-physics": 0.43333333333333335,
  "mmmu-psychology": 0.7,
  "mmmu-public-health": 0.8,
  "mmmu-sociology": 0.5666666666666667
}
Average accuracy: 0.5455555555555556
```

Note that this is slightly lower than the MMMU paper's findings of
`0.568`. There's likely prompt engineering that could be done to improve
this, but I'll leave that as an exercise for later

---
## [Badeklubben/Badeklubben](https://github.com/Badeklubben/Badeklubben)@[54bb604822...](https://github.com/Badeklubben/Badeklubben/commit/54bb604822f09569df74337632d231bbc9e35806)
#### Thursday 2023-12-21 01:17:38 by X104n

OMG i fucking hate CSS, please someone save from this sin

---
## [Rhuan-P-Dev/genericGame](https://github.com/Rhuan-P-Dev/genericGame)@[26558279a7...](https://github.com/Rhuan-P-Dev/genericGame/commit/26558279a7a098f374e34836814b4114fa453799)
#### Thursday 2023-12-21 02:00:42 by Rhuan P

ACTIVATES!!! GIVE ME MORE ACTIVATES!!!!!!!!!! AAAAAAAAAAAAAAAAAAAAAAAA

defense - 17-1
special - 10
weapon - 17
factory - 21

- DEFENSE -

frontal shield - don't work
band aid - a long-term regen but slow - temporary
basic anti-projectile system - do damage on a limited count of objects in range
basic shield area - do damage any object in range
basic fortification module - fortify the owner - temporary
efficient shield - efficiency increases the "shield" stats
light shield - poorly increases the "shield" stats
energy shield - on damage consume the energy
heal pulse 1 - heal the owner and any ally on range
heavy defense - increases the "defense" stats - temporary
light defense - increases the "defense" stats - temporary
iron mind - randomically reduce or increase damage - reduce is more likely - temporary
little shield boost - increases shield and related - temporary
minor miracle stone - revitalize your ship if you die this activate will try activate - the "if" part don't work
reflect shield 1 - reflex projectiles
resilience 1 - increases "maxLife" stats by percentage of damage taken
survive instinct 1 - increases all stats to survive - temporary
tactic upgrade 1 - increases some stats

- SPECIAL -

basic camouflage - reduce "priority" stats - temporary
basic taunt - increases "priority" stats - temporary
blink - a little teleport
teleport - a big teleport
dummy maker - create a distraction dummy
ghost system - make owner invulnerable - incomplete - temporary
illusion 1 - create a illusion of owner
splitter 1 - split owner
test quantum bomb - explode owner and do damage on any enemy on range
turbo 1 - increases "vel" stats - temporary

- WEAPON -

bubbler 1 - too lazy...
diffusion 1 - too lazy...
shotgun 1 - too lazy...
death hand launcher - this projectile will apply onHit a effect - this effect will do damage forever - this effect stake forever
disassemble 1 - this projectile will apply onHit a effect - this effect will increase the damage taken by percentage - this effect stake "forever"
fragilizer 1 - this projectile will apply onHit a effect - this effect will increase the damage taken by percentage - this effect stake
scrapper 1 - this projectile will apply onHit a effect - this effect will increase the damage taken by percentage - this effect stake
electrified bomb 1 - this projectile will apply onHit a "shock" effect - this effect do more damage  compared with "electrified missile 1" - too lazy...
electrified missile 1 - this projectile will apply onHit a "shock" effect - too lazy...
flame thrower 1 - this projectile will apply onHit a "burn" effect - this effect stake
mini world launcher - this projectile has a effect - this effect will pull any enemy in range
missile cluster 1 - shoot a missile - on missile's death create more missiles!
small bullet cluster 1 - shoot a bullet - on bullet's death create more bullets!
missilepiston - this missile has a "piston 1" cool!! right?!
paintbrush 1 - this projectile onHit convert any enemy into a ally
parasite injection 1 - this projectile will apply onHit a "parasite tesla coil" effect
toy machinegun - a low damage machinegun

- FACTORY -

assassin 1 - ...
movable disassemble 1 - ...
movable flame thrower 1 - ...
movable missile burst 1 - ...
movable scrapper 1 - ...
movable shotgun 1 - ...
stationary basic shield area - ...
stationary basic anti-projectile system - ...
tank 1 - ...
adaptive factory - use a factory activate stop the production - on 'drone' death start to produce again but a better version of 'drone' - incomplete
anti-mob 1 - electrified missile 1
diffuser - diffusion 1
evolve factory - use a factory activate - on 'drone' death the next 'drone' will be better
safe perimeter carrier 1 - on death summon 'area protector drones'
upgrader 1/2/3 - use activates to upgrade
vanguard helper 1 - create tank type 'drones', heal others and have a silly auto weapon
war factory - on each use of activates make the next use faster
war promoter 1 - a offensive support

- BALANCING -
basic safe zone 1 - make it better

---
## [ReturnToZender/ReturnsBubber](https://github.com/ReturnToZender/ReturnsBubber)@[d96b2b97aa...](https://github.com/ReturnToZender/ReturnsBubber/commit/d96b2b97aa9969f4a9d800ec0bc8501fcf3529ef)
#### Thursday 2023-12-21 02:24:22 by Waterpig

Waterpig grows more insane with modularity: The massive PR that probably breaks shit (#838)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

I have circuitry theory finals in 1 hour. And as such, to distract
myself from my impending doom and to stop thinking about loop currents,
I have decided to start working on this. (Update: I passed)

This isn't even close to how I wish our modularity to look

But that's future Waterpig's problem (Note to self: Fix the no_antag
button)

In another news, this probably breaks stuff.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Modularity is good. The more stuff we can modularize the better, and
incase it gets removed upstream it's as simple as... removing our
modular override.
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
refactor: Refactors modularity significantly
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

Co-authored-by: The Sharkening <95130227+StrangeWeirdKitten@users.noreply.github.com>

---
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[bc66a212d7...](https://github.com/RustingWithYou/Aurora.3/commit/bc66a212d771eef33ae88445ebe4462ee25bde17)
#### Thursday 2023-12-21 02:47:12 by RustingWithYou

Hephaestus Security Ship & Corporate Voidsuit Tweaks (#17962)

* hephaestus security ship

* fuck off

* welcome mesgaes

* lattice hell

* damn you kaizr

* cabinet

---
## [theUnBurn/Onion](https://github.com/theUnBurn/Onion)@[c7694511f2...](https://github.com/theUnBurn/Onion/commit/c7694511f224fe469f97b98308a9dcfb6fb13917)
#### Thursday 2023-12-21 03:08:27 by XK

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
## [benhartcheatham/advent-of-code-23](https://github.com/benhartcheatham/advent-of-code-23)@[ac58781584...](https://github.com/benhartcheatham/advent-of-code-23/commit/ac58781584b0e2786a5c531b4b8dc372c028f484)
#### Thursday 2023-12-21 03:27:37 by Ben Cheatham

Day nineteen part 2 solution

I ended up transcribing this code here:
https://gist.github.com/samueltardieu/63e7d1f8edbb520334c2dc10c0afb545.
Specifically the process_rule() function (run_rules() in my code).

I had the right approach for my own solution (day19-wip-solution
branch), but I wasn't creating ranges correctly and couldn't be bothered
to figure it out (I hate that shit).

Signed-off-by: Ben Cheatham <Benjamin.Cheatham@amd.com>

---
## [evmts/tevm-monorepo](https://github.com/evmts/tevm-monorepo)@[d6e92eecf2...](https://github.com/evmts/tevm-monorepo/commit/d6e92eecf224b3b5ba304c0c204e28cc2c8b82a2)
#### Thursday 2023-12-21 03:50:44 by Will Cory

:sparkles: Feat(vm): Add precompiles as an option (#664)

## Description

[Norswap requested
precompiles](https://twitter.com/norswap/status/1724944291204665439).
Norswap gets precompiles.

With precompiles one will be able to write arbitrary javascript that
runs when a contract is called. They can even do gross stuff like append
to a dom. Fwiw this will also be how evmts cheat codes work but before
we weren't planning on exposing this to end users.

While implementing this feature I found an annoying bug. If you don't
include an argument in your precompile the entire thing fails to
execute. Opened pr to fix issue here
https://github.com/ethereumjs/ethereumjs-monorepo/pull/3158

The types are currently wrong. It takes an Ethjs address instead of a
HexString address unlike the rest of the evmts pr. This is because
patching the types as I wished was tediously hard as a result of
ethereumjs not exporting specific types I need. Later I will do a pr to
ethereumjs about this. For now we do some typescript magic to infer the
type but because of the type is a union type it's difficult to patch and
I gave up for now.

## Testing

Unit test testing a precompile

## Additional Information

- [ ] I read the [contributing docs](../docs/contributing.md) (if this
is your first contribution)

Your ENS/address:

Co-authored-by: Will Cory <willcory@Wills-MacBook-Pro.local>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3c2d4f03a8...](https://github.com/tgstation/tgstation/commit/3c2d4f03a8883a416434dcb7e32c334bba3e40ae)
#### Thursday 2023-12-21 04:42:16 by SSensum

New Quirk! Cyborg Lover! (#80023)

## About The Pull Request

This PR adds a new quirk for people, who want to play as
silicon-friendly crew.

Basic quirk info:
- It costs 2 points.
- It has minor additions to person's mail goodies list (cable coils,
basic cells, etc).
- It has a few simple mood events, when you pet a borg or being
touched/hugged by borg.

## Why It's Good For The Game

I think it is nice to have a chance to play as ~~robo-creep~~ person who
loves borgos.

## Changelog

:cl:
add: Added new quirk: Cyborg Lover!
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Booking-Team29/ISS](https://github.com/Booking-Team29/ISS)@[991626fa03...](https://github.com/Booking-Team29/ISS/commit/991626fa03939d7d1b42abb05a9da3821736e9bb)
#### Thursday 2023-12-21 04:49:13 by Teodor Đurić

Feature/working backend acc service (#22)

* end my suffering

* fix database scripts

* make every enum entry ALLCAPS

* fix decorator clusterfuck

* change all arrays to Lists; adjust factory methods

* fix stupid field name

* add foreign key reference

* remove stupid lazy loading method

* use eager loading method instead

---
## [Harshvaghela01/CODSOFT](https://github.com/Harshvaghela01/CODSOFT)@[93b42d57ed...](https://github.com/Harshvaghela01/CODSOFT/commit/93b42d57ed402598fe912cfbd9ff83210dfe813e)
#### Thursday 2023-12-21 06:26:00 by Harsh Vaghela

NETFLIX LANDING PAGE

Welcome to my project showcasing a reimagined Netflix landing page, brought to life with the magic of HTML, CSS, and JavaScript. As an avid fan of both web development and streaming content, I embarked on this project to merge my passions and create a dynamic user experience.

The HTML structure forms the backbone, ensuring a well-organized and accessible layout. CSS swoops in to stylize each element, capturing the sleek and modern aesthetic synonymous with Netflix. From the bold typography to the responsive design, every detail has been meticulously crafted to mirror the streaming giant's signature look.

JavaScript takes the user interaction to the next level. Enjoy a carousel of featured shows and movies that dynamically update, providing a taste of the diverse content available. Immerse yourself in the interactive navigation bar, offering seamless transitions and a user-friendly experience.

Whether you're a developer exploring my code or a visitor experiencing the page, I hope this project sparks the same excitement for web development and entertainment that inspired its creation. Lights, camera, action — welcome to the Netflix landing page like never before!

---
## [Harshvaghela01/CODSOFT](https://github.com/Harshvaghela01/CODSOFT)@[88eebe0033...](https://github.com/Harshvaghela01/CODSOFT/commit/88eebe0033c62809ade969392be7d3bfebc5f62b)
#### Thursday 2023-12-21 06:29:37 by Harsh Vaghela

CALCULATOR

Certainly! Here's a description for the calculator project you've made using HTML, CSS, and JavaScript:

Step into the world of digital calculation with my interactive web-based calculator project! Crafted using HTML, CSS, and JavaScript, this project is more than just buttons and numbers—it's a functional and visually appealing tool designed to make your mathematical tasks a breeze.

The HTML structure forms the foundation, providing a clear layout for the calculator interface. CSS steps in to enhance the aesthetics, creating a sleek and intuitive design that aligns with modern user expectations. The responsive layout ensures a seamless experience across various devices, whether you're using a desktop or a mobile device.

But the real magic happens with JavaScript. Witness real-time calculations as you press the buttons, thanks to the dynamic scripting that powers this calculator. From basic arithmetic to more complex operations, this tool adapts to your needs, providing instant results and making mathematical operations efficient and enjoyable.

Whether you're a student, professional, or just someone who appreciates the beauty of a well-designed calculator, this project showcases the synergy of HTML, CSS, and JavaScript to bring functionality and style together. Dive in, explore the features, and let the numbers dance at your fingertips!

---
## [shawnyeung/shawnyeung.github.io](https://github.com/shawnyeung/shawnyeung.github.io)@[e6e9af6fe2...](https://github.com/shawnyeung/shawnyeung.github.io/commit/e6e9af6fe2dba330621ef33a09a831914f773b06)
#### Thursday 2023-12-21 07:02:46 by Zero2Hero

Composer The intent is a classical music composer, a person who writes music to be played or recorded by musicians. If the person in the query both composes and performs music, classify them by the main contribution role or what the person is most likely known for.  Perfect:  Page of the intended composer  Note that it's common for composers to perform the music as well, so the same person can be listed as both Composer and Artist. Disregard the difference in the entity types and rate the page Perfect, as long as it satisfies the intent.  Excellent:  Works by the intended composer Albums featuring only the music of the intended composer  Playlists featuring only the music by intended composer (Essentials, Deep Cuts, Next Steps or created by non-Apple Music) Individual songs with music of the intended composers  Good:  Playlists or albums featuring music by the intended composer along with other composers Popular artists, orchestras and composers matching the full string in the query that could satisfy secondary intent “Albums – Singles” with music of the intended composers  "Inspired by" playlists for the intended composer by Apple Music  Variations of the intended composer's work Acceptable:  Composers, Artists (and orchestras) that are matching the full string in the query but have low popularity Albums that include only variations of the intended composer and not works by the composer Content related to possible secondary intents (more in Tips & Tricks: Tips on Rating Ambiguous Queries) Unacceptable (Off-Topic):  Songs/albums/playlists that are not connected to music of the intended composer (matching only parts of the query or matching it incorrectly)  Artists who perform works from the intended composer and don't match the query  Artist The intent is an artist/singer/orchestra/band, performing other composer’s music.  Perfect: Page of the intended artist  Note that it's common for composers to perform the music as well, so the same person can be listed as both Composer and Artist. Disregard the difference in the entity types and rate the page Perfect, as long as it satisfies the intent.  Excellent:  Songs performed by the intended artist Albums by the intended artists (the artist name should appear in the artist line for the album in Apple Music) Playlists featuring only the music by intended artist (Essentials, Deep Cuts, Next Steps or created by non-Apple Music) Good:  Playlists or albums featuring the intended artist, but not by the intended artist (to be considered by the artist, the artist name should appear in the artist line for the album in Apple Music) Popular artists, orchestras and composers matching the full string in the query that could satisfy secondary intent “Albums – Singles” with music of the intended artist  "Inspired by" playlists for the intended artist by Apple Music  Acceptable:  Composers, Artists (and orchestras) that are matching the full string in the query but have low popularity.  Content related to possible secondary intents (more in Tips & Tricks: Tips on Rating Ambiguous Queries) Unacceptable (Off-Topic):  Songs/albums/playlists/works that are not connected to music of the intended artist (matching only parts of the query or matching it incorrectly)   Work Title The intent is a classical musical composition, i.e. Work. Musical composition can refer to an original piece or work of music, either vocal or instrumental, the structure of a musical piece or to the process of creating or writing a new piece of music. Works are usually referred to by some combination of number, key and catalogue number. The AKA Work Title refers to sub-titles, nicknames and non-numeric titles that the composition is known by. Work Title + Composer User is looking for a specific music composition by the composer and includes both entities in the query.  Catalog Number  The intent is a classical composition and the user is using "work number" to search. "Work number" indicates the chronological order of the composer's production. Opus numbers are used to distinguish among compositions with similar titles; the word is abbreviated as "Op." for a single work, or "Opp." when referring to more than one work. The query can consist of letters and numerics to indicate the catalogue number for composer + number of the work.  Note: Queries referring to a specific movement of the work are classified as Work Title, but have their own rules for Perfect and Excellent results (refer to examples [clair de lune] and [suite bergamasque] below).  Perfect:  Full work that is intended by the query If the query is referring to a movement: the full work of that movement as well as the individual specified movement If the query is referring to an AKA set of works: all works that constitute the set (like sets Water Music or Four Seasons) Variation of the work by the same composer (like Swan Lake Suite in relation to work Swan Lake) Excellent:  Ambiguous Work Title/Catalogue Number examples without Composer specified or Ambiguous incomplete Work Title examples , where we can’t be sure of the primary intent  Individual songs (movements) from the intended work Variations of the work by other composers Album/playlists containing only the intended work  Good:  Album/playlists containing the intended work along with other works Composer’s page for the intended work Acceptable:  Other works by the composer of the intended work (in different entities: Works, Albums, Songs) Artists/orchestras/albums that are matching the full string in the query but have low popularity  Works that are matching the query but only poorly satisfy the intent  Unpopular variations/covers/remixes of the intended work (lullabies, jazz interpretations, modern remixes) unless the version is directly specified in the query  Unacceptable (Off-Topic):  songs/albums/playlists/works that are not connected to music of the intended composer (matching only parts of the query or not matching the result at all)   Composer + Work Type User is looking for a certain work type of a composer. Note that this is different to looking for a specific work, which would be considered Work Title / AKA Work Title + Composer otherwise.  Perfect:  Playlists/albums satisfying the intended work type and composer, containing multiple works only by the queried composer  Excellent:  Playlists/albums satisfying the intended work type and composer, containing single works only by the queried composer Works by the queried composer in the correct work type  Good:  Page of the intended composer  Playlists featuring/albums only music by the intended composer (not necessarily in the queried work type) Individual songs of the intended composers in a right work type  Works by the queried composer in a different work type Acceptable:  Playlists/albums containing intended work type by the intended composer along with and other composers and work types  Entities that are matching the full string in the query but have low popularity  Unpopular variations/covers/remixes of the intended composer's work type (lullabies, jazz interpretations, modern remixes) unless the version is directly specified in the query  Unacceptable (Off-Topic):  songs/albums/playlists that are not connected to music of the intended composer (matching only parts of the query or matching it incorrectly)   Album  User is looking for an album by its name. Note that this is different to other classifications where intended results for queries could also be aggregated in albums.  Perfect:  An intended album implied by the query. If there are multiple possible intents for the query and the result satisfies the result, rate it Perfect. If versions/volumes is not specified, check if the album is satisfying the intent and rate Perfect if it does, even if it's not the first volume. Excellent:  Individual songs from the intended album(s) Works of the intended album(s) Artist Essentials playlists of the intended artist Versions/volumes other than the intended one by the query (if nothing is specified, check if the album is satisfying the intent and rate Perfect if it does) [in a time lapse] – song Discovery At Night by Ludovico Einaudi from the intended album [bavouzet beethoven connection] – song Sonata, Op. 33 No. 3: I. Allegro by Jean-Efflam Bavouzet  [in a time lapse] – playlist Ludovico Einaudi Essentials [nutcracker arsm] – work The Nutcracker Op.71 by Tchaikovsky (the intent is ARSM I, Vol. 34, 35. Tchaikovsky: The Nutcracker, Op. 71 and the returned result is a relevant work)  [in a time lapse] – work In a Time Lapse by Ludovico Einaudi Good: Artist and/or composer page of the album in the query Other music by the intended artist  Secondary intents (other versions, popular matching content) Albums that can satisfy the intent of the query for a certain artist/composer/instrument/genre even though it's not exactly the album user is searching for  [in a time lapse] – album In a Time Lapse (The Remixes) (version of the album by the artist himself, could satisfy secondary intent and is music by the artist) [in a time lapse] – artist page Ludovico Einaudi [in a time lapse] – song Primavera by Ludovico Einaudi [bavouzet beethoven connection] – artist page Jean-Efflam Bavouzet [great catedral organs] – album The Great Organ of Washington National Cathedral (while that is not specifically the album that the user is looking for – Great Cathedral Organs of England), the album provides music in similar genre/type, so it could satisfy secondary intent and can be rated Good) Acceptable:  Matching content that could poorly satisfy the intent [officium] – work Officium Defunctorum by Victoria (the intent is the album Officium by Hilliard Ensemble, but the work matches the query fully and could poorly satisfy the intent) Unacceptable (Off-Topic):  songs/albums/playlists/works that do not satisfy the intent for the composer and artist performance (matching only parts of the query or not matching the result at all)  [in a time lapse] – work Für Alina by Arvo Pärt  Ambiguous The primary intent of the query can’t be determined (query too vague, unfinished, doesn't point to classical music)  Given the ambiguity of the query intent, there is no Perfect rating for this classification.  Excellent:  A piece of content which is very likely to satisfy primary intent of the query. Only the most popular content will be eligible for this rating.  [m] – artist pages for Mozart, Mendelssohn, Mahler, Monteverdi, Mussorgsky [anne] – work Prelude & Fugue in E-flat major “St Anne”, artist page for Anne Gastinel, Anne-Sophie Mutter [mu] – artist page for Mussorgsky, Munchner Rundfunkorcheste , Anne-Sophie Mutter Good:  A piece of content which is very likely to satisfy secondary intent of the query A piece of content that is related to the potential primary intent of the query  [mu] – composer page for Alonso Mudarra Acceptable:  A piece of content that is related to the query, but may be of poor quality, not popular A piece of content that is related to the potential secondary intent of the query  [mu] – artist page for Karl Münchinger  Unacceptable (Off-Topic):  Entities that do not satisfy the intent for the query and do not match the tokens in a meaningful way  More at the top of the guidelines in section Acceptable vs Unacceptable Token Matching    Artist + Composer User is looking for a performance of certain composer performed and recorded by a certain artist.  Perfect:  Album or playlist of intended collaborations of the queried artist and composer  [mozart abbado] – album Mozart: Piano Concertos Nos. 20 & 21 by Friedrich Gulda, Vienna Philharmonic Claudio Abbado  [vivaldi london phil] – album Vivaldi: The Four Seasons by Itzhak Perlman, London Philharmonic Orchestra, Rodney Friend (note that the query is incomplete, but the intent is clear, and the album satisfies the intent) Excellent:  Individual songs from the intended collaboration album  Artist Essentials playlists of the intended artist/composer [mozart abbado] – song Le nozze di Figaro, K. 492, Vienna 1786: Overture from the album Mozart: Le Nozze di Figaro (Highlights) by Vienna Philharmonic and Claudio Abbado [mozart abbado] – playlist Claudio Abbado Essentials  [vivaldi london phil] – playlist London Philharmonic Orchestra Essentials Good: Artist and/or composer page from the query Playlists with other music by the composer or artist individually  Other works/songs of the intended composer/artist, not from the intended album [vivaldi london phil] – album Vivaldi: The Four Seasons - Bach: Brandenburg Concerto No. 3 composed by Vivaldi, performed by Royal Philharmonic Orchestra (the album contains queried composer, but the artist is different)  [vivaldi london phil] – song Concerto for Viola d'amore, Lute and Orchestra, RV 540: I. Allegro composed by Vivaldi, performed by Ton Koopman, Yo-Yo Ma, Amsterdam Baroque Orchestra (the album contains queried composer, but the artist is different)  [vivaldi london phil] – artist page for London Philharmonic Orchestra [vivaldi london phil] – work Violin Concerto in F Minor, Op. 8/4 by Vivaldi (work by the queried composer) [vivaldi london phil] – playlist Background Music that includes several songs by London Philharmonic Orchestra (like Adagio for Strings)  Acceptable:  Matching content that could poorly satisfy the intent Unacceptable (Off-Topic):  Songs/albums/playlists/works that do not satisfy the intent for the composer and artist performance (matching only parts of the query or not matching the result at all)  [mozart abbado] – work Violin Concerto in F Minor, Op. 8/4 by Vivaldi   Artist + Work Title User is looking for a specific recording of the work performed by a certain artist.  Perfect:  An album/playlist of the intended work performed by the intended artist. Sometimes there are multiple albums that would fully satisfy the intent of a queried artist performing a queried work. All albums that satisfy the intent fully are eligible for Perfect.  [mahler 9 chicago] – album Mahler: Symphony No. 9 by Chicago Symphony Orchestra, Pierre Boulez  [mahler 9 chicago] – album Mahler: Symphony No. 9 in D by Chicago Symphony Orchestra, Carlo Maria Giulini Excellent:  Individual songs from the intended collaboration album  Essentials playlists of the intended artist (not composer) Works of the intended album  [mahler 9 chicago] – song Symphony No. 9 in D: I. Andante comodo composed by Mahler and performed by Chicago Symphony Orchestra, Pierre Boulez  [mahler 9 chicago] – playlist Chicago Symphony Orchestra Essentials [mahler 9 chicago] – work Symphony No.9 in D Major by Mahler  Good: Artist page implied by the query Composer page of the work implied by the query Other works of the composer performed by the intended artist  [mahler 9 chicago] – artist page for Mahler (composer of the intended work)  [mahler 9 chicago] – artist page for Chicago Symphony Orchestra (artist)  Acceptable:  Essentials playlists of the intended composer (not artist) Matching content that could poorly satisfy the intent Playlists with other music by the composer or artist individually  Other works and songs of the intended composer/artist, not from the intended album [mahler 9 chicago] – album Mahler: Symphony No. 4 in G Major (Arr. C. Domínguez-Nieto for Chamber Orchestra) by Raquel Lojendio, Camerata Gala, Alejandro Muñoz [mahler 9 chicago] – playlist Mahler Essentials  Unacceptable (Off-Topic):  songs/albums/playlists/works that do not satisfy the intent for the composer and artist performance (matching only parts of the query or not matching the result at all)   Genre User is looking for a specific sub-genre of classical music or a different music genre. Note that this is different from Mood/Activity and Period classification and is applied to conventional genre. Some established genres of classical music are: Orchestral, Chamber Music, Vocal Music, Stage Works, Solo Instrumental, Film Music, Experimental Classical, etc.  Perfect:  High-quality playlists or albums satisfying the intended genre with various composers/artists [chamber music] – album Chamber Music - 50 of the Best by Various Artists [chamber music] – playlist Chamber Music by Alpha Classics [jazz] – playlist Jazz Chill Excellent:  Playlists or albums in the genre for a specific activity/mood/era/occasion/instrument with various composers/artists (a bit more specific and therefore rated Excellent over Perfect) [film music] – album Genius of Film Music: Hollywood 1960s - 1980s by John Mauceri and London Philharmonic Orchestra (containing works from different composers, satisfying the intent of the query, only covering music from 60s-80s)  [jazz] – playlist Jazz in 1959 Essentials  [chamber music] – playlist Relaxing Chamber Music by Analekta  Good:  Works in a specified genre  Individual popular artist’s compilations (albums and playlists) in that genre. [chamber music] – album Mozart: Chamber Music  [chamber music] – playlist Beethoven: Chamber Music  [chamber music] – work Canon and Gigue in D Major, P37 by Johann Pachelbel  [film music] – playlist John Williams Essentials (famous composer in the intended genre)  [film music] – work Star Wars by John Williams  [film music] – album Prokofiev: The Film Music [film music] – album Max Richter: Film Scores [jazz] – work Rhapsody in Blue by George Gershwin Acceptable:  Composers and artists well-known for the specified genre Individual songs of music from popular composers in that genre Individual unpopular artist’s compilations (albums and playlists) in that genre (consider storefront popularity as well) Unpopular matching titles that can poorly satisfy the intent of the query Works in closely related genres/sub-genres  [jazz] – artist page for Ella Fitzgerald (famous performer in the intended genre)  [film music] – artist page for John Williams (famous composer in the intended genre)  [film music] – song The Imperial March (Darth Vader’s Theme) by John Williams and London Symphony Orchestra  [film music] – playlist Suede Essentials (less popular artist in the queried genre)  [chamber music] – artist Southwest Chamber Music (unpopular artist fully matching the string in the query) [jazz] – work Sing Sing Sing by Benny Goodman & His Orchestra (work in the genre swing, closely related to jazz)  Unacceptable (Off-Topic):  songs/albums/playlists/works that do not satisfy the intent (matching only parts of the query or not matching the result at all)   Soundtrack User is looking for soundtrack to a movie/game/tv-show.  Perfect:  High quality playlists or albums satisfying the intent of the soundtrack query. If the version is not specified in the search, assume the user is looking for the first version. Other versions/volumes would be Excellent results. Also use your market knowledge to determine which version the user is most likely looking for. Works of the intended soundtrack [star wars] – album Star Wars: A New Hope (Original Motion Picture Score) by John Williams and London Symphony Orchestra  [lion king] – album The Lion King (Original Motion Picture Soundtrack) by Elton John, Tim Rice, Hans Zimmer  Excellent:  Individual songs from the soundtrack compilation. Versions/volumes other than the intended one by the query. [star wars] – album Star Wars: Revenge of the Sith (Original Motion Picture Soundtrack) by John Williams [star wars] – song The Imperial March (Darth Vader’s Theme) by John Williams and London Symphony Orchestra Good:  Artist or composer pages of the intended soundtrack Secondary intents (other versions, popular matching content: albums or songs) [star wars] – composer page for John Williams [lion king] – song Circle of Life by Tsidii Le Loka, The Lion King Ensemble, Lebo M, Faca Kulu from the soncdary intent album The Lion King (Original 1997 Broadway Cast Recording) Acceptable:  This includes content of lower quality and unpopular pieces of content with the same name or title. [star wars] – artist page for Star Wars  [gladiator] – work Le Gladiateur L.41, CD52 by Debussy  Unacceptable (Off-Topic):  Songs/albums/playlists/works that do not satisfy the intent for the composer and artist performance (matching only parts of the query or not matching the result at all)   Instrument User is searching for compositions and composers by an instrument.  Perfect:  High-quality playlists or albums satisfying the intended instrument with various composers/artists Instrument pages satisfying the intent [piano] – instrument page Piano [piano] – playlist Piano Essentials  Excellent:  Playlists or albums for a queried instrument for a specific activity/mood/era/occasion with various composers/artists  [piano] – playlist Melancholy Piano (playlist with works from different composers in a specified mood)  [piano] – playlist Piano Christmas Classics (playlist with works from different composers for a specified occasion)  Good:  Works for a specified instrument  Individual popular artist’s/composers’s compilations (albums and playlists) for that instrument [piano] – work Piano Sonata No.14 in C-Sharp Minor, Moonlight by Ludwig van Beethoven (work for a queried instrument) [piano] – playlist Frédéric Chopin Essentials [piano] – playlist Beethoven: Piano Sonatas  [piano] – album Beethoven: Piano Concerto No. 5 by Maurizio Pollini, Vienna Philharmonic, Karl Böhm (album of an individual popular composer)  [piano] – compilation album Cinema by Ludovico Einaudi  [piano] – work Piano Concerto No. 5 by Beethoven  Acceptable:  Composers and artists well-known for the specified instrument Individual songs from popular composers for the specified instrument Individual unpopular artist’s compilations (albums and playlists) in that genre (consider storefront popularity as well) Unpopular matching titles that can poorly satisfy the intent of the query [piano] – composer page for Ludwig van Beethoven  [piano] – artist page for The Piano Guys  [piano] – song Suite bergamasque, L. 75: III. Clair de lune composed by Debussy for piano and performed by François-Joël Thiollier  [piano] – album Piano Lullabies, Vol. 1 by Hillsong Kids Jr. (poorly satisfies the intent but includes music of the queried instrument) Unacceptable (Off-Topic):  Songs/albums/playlists/works that do not satisfy the intent (matching only parts of the query or not matching the result at all)  [piano] – work Flute Concerto in D major, K.314/285d by Mozart (the work is for another instrument and therefore doesn’t satisfy the intent)  Work Type User is looking for a work type, without specifying the name of the work or composers.  Perfect:  High-quality playlists or albums satisfying the intended work type with various composers/artists [piano concertos] – playlist Top 10 Piano Concertos [string quartet] – album Debussy & Ravel: String Quartets by Emerson String Quartet  Excellent:  Playlists or albums in the intended work type for a specific activity/mood/era/occasion with various composers/artists  [piano concertos] – album 20th-Century Piano Concertos by BBC Music Magazine  Good:  Works in the correct work type (to identify whether the returned content is in correct work type consider adding "instruments" to your google research; you should first identify the type of the returned piece and the instruments used in the piece to understand if it's applicable for the query) Individual popular artist’s compilations (albums and playlists) in that work type Artists matching the string that could satisfy secondary intent  [string quartet] – artist page for Budapest String Quartet  [string quartet] – work String Quartet No.1 in D Major, Op. 11 by Tchaikovsky  [string quartet] – album Mozart String Quartets by Quatuor Ébène  Acceptable:  Composers and artists well-known for the specified work type Individual songs in the correct work type Individual unpopular artist’s compilations (albums and playlists) in that work type  Instrument playlists related to the intended work type  Unpopular matching titles that can poorly satisfy the intent of the query Unpopular variations/covers/remixes of the intended work type (lullabies, jazz interpretations, modern remixes) unless the version is directly specified in the query  [piano concertos] – artist page for Wolfgang Amadeus Mozart [piano concertos] – song Piano Concerto No. 20 in D Minor, K. 466. II. Romance composed by Mozart and performed by Seong-Jin Cho, Chamber Orchestra of Europe, Yannick Nézet-Séguin [piano concertos] – playlist Piano Essentials   Origin User is looking for composers or music by the origin of the composer.  Perfect:  Playlists and albums satisfying the intended origin [russian] – playlist 55 Russian Classical Hits [russian] – playlist Russian Composers [russian] – album Russian Classics by Sächsische Bläserphilharmonie & Thomas Clamor Excellent:  Composers or artists pages of the intended origin  Works of the well-known composers of the intended origin  [russian] – work Nutcracker by Tchaikovsky  [russian] – composer page for Pyotr Ilyich Tchaikovsky Good:  Individual songs of music from popular composers of the intended origin  Well-known works/songs/artists that match the query and could satisfy secondary intent  [russian] – song The Nutcracker, Op. 71: XIIId. Trepan (Russian Dance) (well-known song that fully matches the string in the query)  [italian] – work Italian Concerto in F Major by Bach (well-known work that fully matches the string in the query)  [russian] – artist page for Russian State Symphony Orchestra Acceptable:  Unpopular composers/artists/works that match the string of the query  [japanese] – work Japanese Suite H126, Op. 33 by Holst  [italian] – artist page for Italian Classical Consort  Unacceptable (Off-Topic):  Songs/albums/playlists/works that do not satisfy the intent and has no relevance (matching only parts of the query or not matching the result at all)  [japanese] – artist page for Joseph Trapanese   Playlist Navigational Intent for a specific playlist.  Perfect:  User is looking for a specific playlist (intent is very clear from the query).  [beethoven essentials] – playlist Ludwig van Beethoven Essentials [classical dinner party] – playlist Classical Dinner Party Excellent:  A piece of content which satisfies a dominant intent of the query (other albums or playlists closely related to the intent).  If the intent is more ambiguous, use popularity of the composer/artist to determine between Excellent and Good, if it's matching the query. All popular composers/artists, genres, periods and instruments essentials can be considered Excellent.  [beethoven essentials] – playlist The Beethoven Effect [beethoven essentials] – album Beethoven Essentials [essentials] – playlist Ludwig van Beethoven Essentials (popular composer’s essentials)  [essentials] – album Beethoven Piano Essentials (popular composer’s album)  [essentials] – playlist Piano Essentials (instrument essentials that could satisfy the intent)  [essentials] – playlist ‘10s Classical Essentials (decade/era essentials that could satisfy the intent)  Good:  Artist pages for the queried artist  Works and songs by the intended artist  Playlists/albums that poorly satisfy the intent [beethoven essentials] – artist page for Ludwig van Beethoven  [essentials] – playlist Abdel Rahman el Bacha Essentials (less popular artist’s essentials) Acceptable: A piece of content that is related to the query, but is unpopular or only poorly satisfies a secondary intent. [essential] – artist page for Essential Voices USA [essential] – song Kirkpatrick: Angles We Have Heard on High by Tedd Firth, Essential Voices USA,  Unacceptable (Off-Topic): A piece of content that is not related to the query or has no perceived relevance.   Moods/Activity User is searching for music with a mood/activity/occasion keyword.  Perfect:  High-quality playlists or albums satisfying the intended mood/activity with various composers/artists [sleep] – playlist Classical Sleep  [sleep] – album Sleep: 111 Pieces of Classical Music for Bedtime (album with music by different composers and artists)  Excellent:  Playlists or albums for a specific activity/mood/era/occasion/instrument with various composers/artists  [sleep] – album Relaxing Cello: Classical Cello Music for Sleep, Relaxation & Stress Relief (album in a specific instrument with music from different composers) [study] – album Study with Baroque Music by Analekta  Good:  Individual popular artist’s compilations (albums and playlists) in that mood/activity  Secondary intent that matches the string (works/songs)  [sleep] – album Satie Deep Sleep  [study] – playlist Mozart: Study  [sleep] – album Sleep by Max Richer  [sleep] – work The Sleeping Beauty, Op. 66 by Tchaikovsky Acceptable:  Unpopular matching titles that can poorly satisfy the intent of the query Individual songs from albums that could satisfy the intent for the mood/activity [sleep] – artist page for Thomas Sleeper (given the incremental search, the query might be incomplete; the artist is unpopular, so it would poorly satisfy intent)  [sleep] – song Soothing Sleep by Piano Peace (individual song from the album that could satisfy the intent for the queried mood/activity) Unacceptable (Off-Topic):  Songs/albums/playlists/works that do not satisfy the intent (matching only parts of the query or not matching the result at all)   Tempo User is looking for classical works in a certain tempo. Full list of tempo markings could be found here. Music Key User is looking for classical works in a certain key. Key of a piece is the group of pitches, or scale, that forms the basis of a musical composition. Keys are abbreviated with letters + special characters ♭(flat)♮(sharp) + major/minor.  Given the ambiguity of the query intent, there is no Perfect rating for this classification.  Excellent:  Playlists or albums in the tempo/music key for a specific activity/mood/era/occasion with various composers/artists [allegro] – albums of multiple composers  Good:  Works in a specified tempo/music key  Individual artist’s compilations (albums and playlists) in that tempo/music key [allegro] – work Adagio and Allegro in A-Flar Major, Op.70 by Schumann  [allegro] – album Schumann: Piano Concerto, Concert Allegro, Introduction & Allegro by Vladimir Ashkenazy, London Symphony Orchestra and Uri Segal (includes music composed only by Schumann)  [c major] – work Prelude and Fugue No. 1 in C Major, BWV846 by Bach Acceptable:  Individual songs of music from popular composers in that key/tempo Unpopular matching titles that can poorly satisfy the intent of the query [allegro] – song Symphony No. 9 in D Minor, Op. 125 - “Choral”: I. Allegro Ma Non Troppo, Un Poco Maestoso   Unacceptable (Off-Topic):  songs/albums/playlists/works that do not satisfy the intent (matching only parts of the query or not matching the result at all)  [allegro] – composer page for Gregorio Allegri   Radio Intent is for conventional hosted live stations, often associated with a radio network. This includes local, satellite and internet radio stations. OR Intent is for non-hosted radio stations, focussing on a certain genre/mood/era. This includes queries with a functional query + “radio” or “station” in the string.  Perfect:  Radio of the intended genre/composer/broadcast station [beethoven station] – artist radio station for Beethoven  [classical 90.3fm] – radio station KEXP 90.3  Excellent:  Playlists satisfying the intent of the query (similar genre/composer/theme) Albums satisfying the intent of the query (similar genre/composer/theme) [beethoven station] – playlist The Beethoven Effect [beethoven station] – album 50 of the Best: Beethoven [classical 90.3fm] – album Selections from "White Noise" Live from Kexp 90.3 FM Seattle - September 22 2017  Good:  Individual songs satisfying the intent of the query  Composer or artist pages satisfying the intent of the query [beethoven station] – song Egmont, Op.84: Overture  [beethoven station] – artist page for Ludwig van Beethoven  Acceptable: Artists, orchestras, composers, works that are matching the full string in the query but have low popularity  Unacceptable (Off-Topic):  A piece of content that is not related to the query or has no perceived relevance.   Period User is looking for classical music from a specific period/era of time. Some established classical music periods are Medieval (500-1400), Renaissance (1400-1600), Baroque (1600-1750), Classical (1730-1820), Romantic (1780-1910), Early 20th Century (1900-1945), Late 20th Century (1940-1999) and 21st Century.   Perfect:  High-quality playlists or albums satisfying the intended period with various composers/artists [renaissance] – playlist Early Music [renaissance] – album Renaissance Music - Classical Navígator containing music by different artists Excellent:  Playlists or albums in the period for a specific activity/mood/era/occasion with various composers/artists  [renaissance] – playlist Medieval and Renaissance Christmas Good:  Works in a specified genre  Individual popular artist’s compilations (albums and playlists) in that period. [renaissance] – album The Golden Renaissance: William Byrd performed by Stile Antico  [renaissance] – work O magnum mysterium by Victoria  [renaissance] – album The Tallis Scholars Sing William Byrd with music composed by William Byrd  Acceptable:  Composers and artists well-known for the specified period Individual songs of music from popular composers in that period Individual unpopular artist’s compilations (albums and playlists) in that period (consider storefront popularity as well) Unpopular matching titles that can poorly satisfy the intent of the query [renaissance] – artist page for composer Giovanni Pierluigi da Palestrina  [renaissance] – work Renaissance by Godowsky (matching the string in the query fully, but doesn’t satisfy the intent for period) [renaissance] – artist page for Orchestra of the Renaissance  Unacceptable (Off-Topic):  Songs/albums/playlists/works that do not satisfy the intent (matching only parts of the query or not matching the result at all)  Label User is looking for music associated with a certain label.  Perfect:  Particular label implied by the query  [deutsche grammophon] – record label Deutsche Grammophon Excellent:  Record label’s Curator’s page, and all content either curated, or produced by the intended record label. This includes Artist pages for artists signed by the record label, Playlists, Albums, Songs, and Radio Shows produced, and/or curated by the record [deutsche grammophon] – curator Deutsche Grammophon (DG) [deutsche grammophon] – playlist Deutsche Grammophon: Mozart [deutsche grammophon] – album Complete Bach Recordings On Deutsche Grammophon by Walter Gieseking  [deutsche grammophon] – song Symphony No. 7 in A, Op. 92: 2. Allegretto from the album Complete Recordings On Deutsche Grammophon - Vol.1 - Orchestral Works Good:  Matching content that can still satisfy secondary intent  [deutsche grammophon] – song Deutsche Grammophon by Vincent Delerm  Acceptable:  Content relevant to matching content that can still satisfy secondary intent  [deutsche grammophon] – album Kensington Square by Vincent Delerm, consisting song Deutsche Grammophon Unacceptable (Off-Topic):  Songs/albums/playlists/works that do not satisfy the intent (matching only parts of the query or not matching the result at all)  Playlist Functional Intent for a playlist in a certain genre, style, era, mood. A query that includes a functional query + “playlist” in the string.  Perfect:  High quality playlists relevant to the query [mozart playlist] – playlist Mozart: Top 50 by Filtr Classical  [baroque playlist] – playlist Baroque Essentials [harp playlist] – playlist Harp Music: Classical & Modern [harp playlist] – playlist The Harp Excellent:  High-quality playlists relevant to the query that are slightly specific (specific activity/mood/era/occasion) Popular albums in the intended genre featuring multiple composers/artists  [baroque playlist] – album Baroque - The Essentials with multiple composers’ music  [harp playlist] – playlist Jazz Ensemble: Harp Good:  Albums/playlists in the intended genre featuring only one composer/artist [baroque playlist] – album Vivaldi: The Four Seasons [harp playlist] – album Mozart: Flute & Harp Concerto Acceptable:  Artist and composer pages in the intended genre/theme Individual songs in the intended genre/theme Unpopular matching titles that can poorly satisfy the intent of the query Individual unpopular artist’s compilations (albums and playlists) in that genre (consider storefront popularity as well) [baroque playlist] – artist page for Antonio Vivaldi [harp playlist] – song Concerto for Flute & Harp in C Major, K. 299: Allegro   Unacceptable (Off-Topic):  Songs/albums/playlists/works that do not satisfy the intent for the composer and artist performance (matching only parts of the query or not matching the result at all)

---
## [kernelci/linux](https://github.com/kernelci/linux)@[2fcd38f4de...](https://github.com/kernelci/linux/commit/2fcd38f4de7256e2b5cb23ad22a6e3ebfea7dd18)
#### Thursday 2023-12-21 08:02:58 by Al Viro

[software coproarchaeology] dentry.h: kill a mysterious comment

there's a strange comment in front of d_lookup() declaration:

/* appendix may either be NULL or be used for transname suffixes */

Looks like nobody had been curious enough to track its history;
it predates git, it predates bitkeeper and if you look through
the pre-BK trees, you finally arrive at this in 2.1.44-for-davem:
  /* appendix may either be NULL or be used for transname suffixes */
 -extern struct dentry * d_lookup(struct inode * dir, struct qstr * name,
 -                               struct qstr * appendix);
 +extern struct dentry * d_lookup(struct dentry * dir, struct qstr * name);
In other words, it refers to the third argument d_lookup() used to have
back then.  It had been introduced in 2.1.43-pre, on June 12 1997,
along with d_lookup(), only to be removed by July 4 1997, presumably
when the Cthulhu-awful thing it used to be used for (look for
CONFIG_TRANS_NAMES in 2.1.43-pre, and keep a heavy-duty barfbag
ready) had been, er, noticed and recognized for what it had been.

Despite the appendectomy, the comment remained.  Some things really
need to be put out of their misery...

Signed-off-by: Al Viro <viro@zeniv.linux.org.uk>

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[2805c86c81...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/2805c86c811fde2450a054a25c7a665b77df47e5)
#### Thursday 2023-12-21 08:11:17 by Nerevar

[THE HALF-MODULAR PRINCE] Snalance (Snail Balance) and Snissues (Snail Issues) Adjustment (#25439)

* initial d

* holy shit i forgot

* i got so much cheese in my pocket, they thought I was a fucking calzone

* opp was sneak-dissing on the 'gram, turned his city into pompeii

* Just fixing some diffs (line breaks should match tg)

* Fixes these edit comments

---------

Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [amannn/next-intl](https://github.com/amannn/next-intl)@[e6d98787ad...](https://github.com/amannn/next-intl/commit/e6d98787ad43aec50dcb6594353da83a958a81d1)
#### Thursday 2023-12-21 08:39:49 by Jan Amann

feat: Invoke `notFound()` when no locale was attached to the request and update docs to suggest validating the locale in `i18n.ts` (#742)

Users are currently struggling with errors that are caused by these two
scenarios:
1. An invalid locale was passed to `next-intl` APIs (e.g.
[#736](https://github.com/amannn/next-intl/issues/736))
2. No locale is available during rendering (e.g.
[#716](https://github.com/amannn/next-intl/issues/716))

**tldr:**
1. We now suggest to validate the incoming `locale` in
[`i18n.ts`](https://next-intl-docs.vercel.app/docs/usage/configuration#i18nts).
This change is recommended to all users.
2. `next-intl` will call the `notFound()` function when the middleware
didn't run on a localized request and `next-intl` APIs are used during
rendering. Previously this would throw an error, therefore this is only
relevant for you in case you've encountered [the corresponding
error](https://next-intl-docs.vercel.app/docs/routing/middleware#unable-to-find-locale).
Make sure you provide a relevant [`not-found`
page](https://next-intl-docs.vercel.app/docs/environments/error-files#not-foundjs)
that can be rendered in this case.

---

**Handling invalid locales**

Users run into this error because the locale wasn't sufficiently
validated. This is in practice quite hard because we currently educate
in the docs that this should happen in [the root
layout](https://next-intl-docs.vercel.app/docs/getting-started/app-router#applocalelayouttsx),
but due to the parallel rendering capabilities of Next.js, potentially a
page or `generateMetadata` runs first.

Therefore moving this validation to a more central place seems
necessary. Due to this, the docs will now suggest validating the locale
in `i18n.ts`. By doing this, we can catch erroneous locale arguments in
a single place before e.g. importing JSON files.

The only edge case is if an app uses no APIs of `next-intl` in Server
Components at all and therefore `i18n.ts` doesn't run. This should be a
very rare case though as even `NextIntlClientProvider` will call
`i18n.ts`. The only case to run into this is if you're using
`NextIntlClientProvider` in a Client Component and delegate all i18n
handling to Client Components too. If you have such an app, `i18n.ts`
will not be invoked and you should validate the `locale` before passing
it to `NextIntlClientProvider`.

**Handling missing locales**

This warning is probably one of the most annoying errors that users
currently run into:

```
Unable to find next-intl locale because the middleware didn't run on this request.
```

The various causes of this error are outlined in [the
docs](https://next-intl-docs.vercel.app/docs/routing/middleware#unable-to-find-locale).

Some of these cases should simply be 404s (e.g. when your middleware
matcher doesn't match `/unknown.txt`), while others require a fix in the
matcher (e.g. considering `/users/jane.doe` when using `localePrefix:
'as-necessary'`).

My assumption is that many of these errors are false positives that are
caused by the `[locale]` segment acting as a catch-all. As a result, a
500 error is encountered instead of 404s. Due to this, this PR will
downgrade the previous error to a dev-only warning and will invoke the
`notFound()` function. This should help in the majority of cases. Note
that you should define [a `not-found`
file](https://next-intl-docs.vercel.app/docs/environments/error-files#not-foundjs)
to handle this case.

I think this change is a good idea because if you're using
`unstable_setRequestLocale` and you have a misconfigured middleware
matcher, you can provide any kind of string to `next-intl` (also
`unknown.txt`) and not run into this error. Therefore it only affects
users with dynamic rendering. Validating the locale in `i18n.ts` is the
solution to either case (see above). Also in case something like
[`routeParams`](https://github.com/amannn/next-intl/issues/663) gets
added to Next.js, the current warning will be gone entirely—therefore
tackling it from a different direction is likely a good idea.

The false negatives of this should hopefully be rather small as we
consistently point out that you need to adapt your middleware matcher
when switching the `localePrefix` to anything other than `always`.
Dev-only warnings should help to get further information for these
requests.

---

Closes https://github.com/amannn/next-intl/issues/736
Closes https://github.com/amannn/next-intl/issues/716
Closes https://github.com/amannn/next-intl/discussions/446

---
## [pivovarit/AoC_2023_go](https://github.com/pivovarit/AoC_2023_go)@[f6fcf67ce5...](https://github.com/pivovarit/AoC_2023_go/commit/f6fcf67ce5323aa8ac8756612c57c67c21373391)
#### Thursday 2023-12-21 09:23:47 by Grzegorz Piwowarek

Day 12 (#19)

### Day 12: Hot Springs

You finally reach the hot springs! You can see steam rising from
secluded areas attached to the primary, ornate building.

As you turn to enter, the researcher stops you. "Wait - I thought you
were looking for the hot springs, weren't you?" You indicate that this
definitely looks like hot springs to you.

"Oh, sorry, common mistake! This is actually the onsen! The hot springs
are next door."

You look in the direction the researcher is pointing and suddenly notice
the massive metal helixes towering overhead. "This way!"

It only takes you a few more steps to reach the main gate of the massive
fenced-off area containing the springs. You go through the gate and into
a small administrative building.

"Hello! What brings you to the hot springs today? Sorry they're not very
hot right now; we're having a lava shortage at the moment." You ask
about the missing machine parts for Desert Island.

"Oh, all of Gear Island is currently offline! Nothing is being
manufactured at the moment, not until we get more lava to heat our
forges. And our springs. The springs aren't very springy unless they're
hot!"

"Say, could you go up and see why the lava stopped flowing? The springs
are too cold for normal operation, but we should be able to find one
springy enough to launch you up there!"

There's just one problem - many of the springs have fallen into
disrepair, so they're not actually sure which springs would even be safe
to use! Worse yet, their condition records of which springs are damaged
(your puzzle input) are also damaged! You'll need to help them repair
the damaged records.

In the giant field just outside, the springs are arranged into rows. For
each row, the condition records show every spring and whether it is
operational (.) or damaged (#). This is the part of the condition
records that is itself damaged; for some springs, it is simply unknown
(?) whether the spring is operational or damaged.

However, the engineer that produced the condition records also
duplicated some of this information in a different format! After the
list of springs for a given row, the size of each contiguous group of
damaged springs is listed in the order those groups appear in the row.
This list always accounts for every damaged spring, and each number is
the entire size of its contiguous group (that is, groups are always
separated by at least one operational spring: #### would always be 4,
never 2,2).

So, condition records with no unknown spring conditions might look like
this:
```
#.#.### 1,1,3
.#...#....###. 1,1,3
.#.###.#.###### 1,3,1,6
####.#...#... 4,1,1
#....######..#####. 1,6,5
.###.##....# 3,2,1
```
However, the condition records are partially damaged; some of the
springs' conditions are actually unknown (?). For example:

```
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
```
Equipped with this information, it is your job to figure out how many
different arrangements of operational and broken springs fit the given
criteria in each row.

In the first line (???.### 1,1,3), there is exactly one way separate
groups of one, one, and three broken springs (in that order) can appear
in that row: the first three unknown springs must be broken, then
operational, then broken (#.#), making the whole row #.#.###.

The second line is more interesting: .??..??...?##. 1,1,3 could be a
total of four different arrangements. The last ? must always be broken
(to satisfy the final contiguous group of three broken springs), and
each ?? must hide exactly one of the two broken springs. (Neither ??
could be both broken springs or they would form a single contiguous
group of two; if that were true, the numbers afterward would have been
2,3 instead.) Since each ?? can either be #. or .#, there are four
possible arrangements of springs.

The last line is actually consistent with ten different arrangements!
Because the first number is 3, the first and second ? must both be . (if
either were #, the first number would have to be 4 or higher). However,
the remaining run of unknown spring conditions have many different ways
they could hold groups of two and one broken springs:

```
?###???????? 3,2,1
.###.##.#...
.###.##..#..
.###.##...#.
.###.##....#
.###..##.#..
.###..##..#.
.###..##...#
.###...##.#.
.###...##..#
.###....##.#
```
In this example, the number of possible arrangements for each row is:


- ```???.### 1,1,3``` - 1 arrangement
- ```.??..??...?##. 1,1,3``` - 4 arrangements
- ```?#?#?#?#?#?#?#? 1,3,1,6``` - 1 arrangement
- ```????.#...#... 4,1,1``` - 1 arrangement
- ```????.######..#####. 1,6,5``` - 4 arrangements
- ```?###???????? 3,2,1``` - 10 arrangements

Adding all of the possible arrangement counts together produces a total
of 21 arrangements.

For each row, count all of the different arrangements of operational and
broken springs that meet the given criteria. What is the sum of those
counts?

#### Part Two

As you look out at the field of springs, you feel like there are way
more springs than the condition records list. When you examine the
records, you discover that they were actually folded up this whole time!

To unfold the records, on each row, replace the list of spring
conditions with five copies of itself (separated by ?) and replace the
list of contiguous groups of damaged springs with five copies of itself
(separated by ,).

So, this row:
```
.# 1
```
Would become:
```
.#?.#?.#?.#?.# 1,1,1,1,1
```
The first line of the above example would become:

```
???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3
```
In the above example, after unfolding, the number of possible
arrangements for some rows is now much larger:

- ```???.### 1,1,3``` - 1 arrangement
- ```.??..??...?##. 1,1,3``` - 16384 arrangements
- ```?#?#?#?#?#?#?#? 1,3,1,6``` - 1 arrangement
- ```????.#...#... 4,1,1``` - 16 arrangements
- ```????.######..#####. 1,6,5``` - 2500 arrangements
- ```?###???????? 3,2,1``` - 506250 arrangements
After unfolding, adding all of the possible arrangement counts together
produces 525152.

Unfold your condition records; what is the new sum of possible
arrangement counts?

---
## [irreverentsimplicity/gno](https://github.com/irreverentsimplicity/gno)@[24d89a4f5d...](https://github.com/irreverentsimplicity/gno/commit/24d89a4f5debd3c1ae711e98587e1e32980e4347)
#### Thursday 2023-12-21 09:58:23 by Morgan

feat(examples): add p/demo/seqid (#1378)

A very simple ID generation package, designed to be used in combination
with `avl.Tree`s to push values in order.

The name was originally `seqid` (sequential IDs), but after saying it a
few times I realised it was close to "squid" and probably would be more
fun if I named it that way ;)

There's another piece of functionality that I want to add, which is a
way to create simple base32-encoded IDs. This depends on #1290. These
would also guarantee alphabetical ordering, so a list of them can be
easily sorted and you'd get it in the same order they were created. They
would likely be 13 characters long, but I'm also thinking of making a
compact version which works from [0,2^35) which is 7 chracters, and then
smoothly transitions over to the 13 characters version when the ID is
reached.

(I've experience with both base64 and base32 encoded IDs as 64-bit
numbers, as I used both systems. The advantage of base32 is that it
makes IDs case insensitive, all the while being at most 13 bytes instead
of 11 for base64.)

In GnoChess, we used simple sequential IDs combined with
[`zeroPad9`](https://github.com/gnolang/gnochess/blob/7e841191a4a0a94c0d46bc977458bd6b757eab5e/realm/chess.gno#L287-L296)
to create IDs which were both readable and sortable. I want to make a
more "canonical" solution to this which does not have a upper limit at 1
billion entries.

---
## [elan-ev/tobira](https://github.com/elan-ev/tobira)@[4f8ce99b6d...](https://github.com/elan-ev/tobira/commit/4f8ce99b6dd001fe3ea2f95c08a176a03ee672a8)
#### Thursday 2023-12-21 10:58:23 by Ole Wieners

Store user info in DB and make them searchable in ACL UI (#1027)

Fixes #951 (also removing our dummy users from the code, unblocking the
release)

The main goal of this PR was to make the ACL UI user selection work
nicely. I.e. that one can search through users to add user entries to
the ACL. Previously we had a bunch of hardcoded dummy users (which also
made us unable to release Tobira). This is now done, but lots of related
changed had to be done as well. There is also a configuration option
which controls whether users can actually be searched by name or whether
they can only be found by typing the exact username/email. The latter
mode is the default for data privacy reasons.

User information is remembered whenever a user logs into Tobira or does
anything there. It is also possible to import users from a JSON file.

**Important**: this PR introduces a breaking change as it makes a "user
role" mandatory for users. See second commit. I doubt this is a problem
for anyone, but it's still technically breaking.

---

This can probably be reviewed commit by commit. The commit messages
should be read for sure. However, the changes to `ui/Access.tsx` are
likely very annoying to review because it's also lots of refactoring,
over multiple commits. So yeah, not 100% sure how to best approach that.

---

Finally, there are a few things that still have to be improved. But not
in this PR, it's already large enough. I will create issues for these
after merging.

- [ ] Potentially add some basic user stats to `/~metrics`, e.g. "active
user in last 24h
- [ ] Re-add the paste functionality
- [ ] Stop sending a list of all known groups to the frontend, that
makes stuff slow.

---
## [epiverse-trace/sandpaper](https://github.com/epiverse-trace/sandpaper)@[44ef4d8fef...](https://github.com/epiverse-trace/sandpaper/commit/44ef4d8fef4e98637cb000f9861839e3e35eeda9)
#### Thursday 2023-12-21 11:45:07 by Zhian N. Kamvar

reset metdata for handout test

This is one of the weird litte things that I need to get better at
controlling. When we test these things, the global metdata is affected,
but it's not possible (at the moment) to _remove_ metadata without
resetting everything, so instead, we need to set the global metadata
option for "handout" to NULL.

In the words of the author of a C++ library that I rewrote in R for my
Ph. D.:

> This is a bloody awful nasty hack ... and will give us grief
> elsewhere. Find a better way to do this

---
## [OmarEl-Jundi/Games_Galaxy](https://github.com/OmarEl-Jundi/Games_Galaxy)@[130ab26991...](https://github.com/OmarEl-Jundi/Games_Galaxy/commit/130ab2699139372b2bd5352ed07c494e01c0d728)
#### Thursday 2023-12-21 12:17:52 by OmarEl-Jundi

removed the ".content" div and the script for it (fuck you kevin)

---
## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[afeb8edd3b...](https://github.com/Mu-L/crawl/commit/afeb8edd3b8c5a8165938164b7b2bc36ea37fb54)
#### Thursday 2023-12-21 12:20:04 by DracoOmega

Change player Ogres into Oni, shorten Armataur tongues

Ogres are considered a fairly weak player species, and have been arguably
additionally troubled by the fact that most of the ogres the player ever
encounters in the dungeon are dumb giant club brutes - leading new players
to assume this is the core ogre playstyle, despite many veterans arguing
that they make better mages than fighters, and that 1-hander + shield is
the better choice for them.

Simultaneously, there's been a desire to cut armataur's doubled potion
gimmick. Their new regen-on-rampage is already very strong, and does a
better job of emphasizing the species' core movement gimmick than long
tongue does, and it is much easier to reasonably balance their power
without TWO big sources of healing. (Inversely, despite their large hp
pools, ogres can be paradoxically fragile and could definitely benefit from
the additional potion healing.)

So I am simplifying that mutation, moving it to ogre, and rethemeing them
slightly to give the mechanic a stronger flavor fit.

Player Ogres are now Oni. Leaning into the mythical backdrop of them being
legendary drinkers and brawlers, oni gain doubled health and magic from
any potion that restores these (ie: !curing, !heal wounds, !magic, and
!ambrosia, and when they drink such a potion, they also make an immediate
attack against all enemies surrounding them. Cleave with a giant spiked
club, just so long as you have enough on hand to drink while you do it!

Oni apts are mostly the same as Ogres, with the following changes:
 Maces -1 -> 0
 Armour -2 -> -1
 Shields 0 -> -1
 Invocations 1 -> 2

People have clamored for ages for the most obvious wielder of giant spiked
clubs in the game to not have a negative apt and that seems reasonable to
me (the ancient +3 they had made this more of a no-brainer, but 0 probably
leaves other weapons sufficiently appealing)

Slightly better armor and slightly worse shields apt (along with drunken
brawling) may also nudge them a bit more towards 2-handers without making
them obviously correct.

And +1 invocations due to their famous associations of working for the
celestial bureaucracy (as torturers... >.>)

They have also gained horns 1 (they already were too large to wear helmets,
so this is a minor buff than a new restriction - also oni are usually
depicted with horns).

I toyed with the idea of giving them built-in shoutitits 1, with rewritten
messages so that they kept bellowing challenges and taunts at random
enemies. And while I think the flavor of this is *hilarious*, I worry that
their buffs might not entirely compensate for this downside. Or maybe it
would be fine along with some other minor tweak?

Either way, this hopefully does a somewhat better job of selling the
fantasy of the species one is playing as, while providing a unique gimmick
to play with.

(Enemy ogres are staying as ogres - it would defeat some of the purpose of
this if they changed - but Erolcha specifically may be slated to become an
oni instead)

---
## [char1eschen/react](https://github.com/char1eschen/react)@[b6978bc38f...](https://github.com/char1eschen/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Thursday 2023-12-21 13:03:41 by Andrew Clark

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
## [CursedBirb/Shiptest](https://github.com/CursedBirb/Shiptest)@[8744738e59...](https://github.com/CursedBirb/Shiptest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Thursday 2023-12-21 13:13:41 by Arturlang

Updates TGUI and adds bin folder for .bat scripts (#2011)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Updates TGUI and build tools and .vscode files to what TG has.
Does not actually update UI's, but does have fixes for a couple
including the join game UI's tabs not working.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not needing to have a local installation of yarn to run dev-mode is
nice.
Updating TGUI is a annoying chore that helps in the future when porting
more interfaces
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
code: Adds a bin folder with dev scripts, updates TGUI, .vscode folder
to what TG has.
fix: Fixes the input in the bottom right being white in darkmode, no
more unreadable text
fix: You can now use the tab buttons in the join ship menu.
qol: The outpost mission menu now looks a whole lot better
fix: The input bar no longer randomly becomes white and unreadable on
darkmode
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [repinger/android_kernel_xiaomi_sm8250](https://github.com/repinger/android_kernel_xiaomi_sm8250)@[08cd3e59cf...](https://github.com/repinger/android_kernel_xiaomi_sm8250/commit/08cd3e59cf83eb6fe551b8fc44acc693698176cb)
#### Thursday 2023-12-21 13:16:41 by Peter Zijlstra

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
## [repinger/android_kernel_xiaomi_sm8250](https://github.com/repinger/android_kernel_xiaomi_sm8250)@[27434439e5...](https://github.com/repinger/android_kernel_xiaomi_sm8250/commit/27434439e563e89f0bcdf6f421004331bb4274e0)
#### Thursday 2023-12-21 13:16:41 by Peter Zijlstra

sched: Fix loadavg accounting race

The recent commit:

  c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")

moved these lines in ttwu():

	p->sched_contributes_to_load = !!task_contributes_to_load(p);
	p->state = TASK_WAKING;

up before:

	smp_cond_load_acquire(&p->on_cpu, !VAL);

into the 'p->on_rq == 0' block, with the thinking that once we hit
schedule() the current task cannot change it's ->state anymore. And
while this is true, it is both incorrect and flawed.

It is incorrect in that we need at least an ACQUIRE on 'p->on_rq == 0'
to avoid weak hardware from re-ordering things for us. This can fairly
easily be achieved by relying on the control-dependency already in
place.

The second problem, which makes the flaw in the original argument, is
that while schedule() will not change prev->state, it will read it a
number of times (arguably too many times since it's marked volatile).
The previous condition 'p->on_cpu == 0' was sufficient because that
indicates schedule() has completed, and will no longer read
prev->state. So now the trick is to make this same true for the (much)
earlier 'prev->on_rq == 0' case.

Furthermore, in order to make the ordering stick, the 'prev->on_rq = 0'
assignment needs to he a RELEASE, but adding additional ordering to
schedule() is an unwelcome proposition at the best of times, doubly so
for mere accounting.

Luckily we can push the prev->state load up before rq->lock, with the
only caveat that we then have to re-read the state after. However, we
know that if it changed, we no longer have to worry about the blocking
path. This gives us the required ordering, if we block, we did the
prev->state load before an (effective) smp_mb() and the p->on_rq store
needs not change.

With this we end up with the effective ordering:

	LOAD p->state           LOAD-ACQUIRE p->on_rq == 0
	MB
	STORE p->on_rq, 0       STORE p->state, TASK_WAKING

which ensures the TASK_WAKING store happens after the prev->state
load, and all is well again.

Fixes: c6e7bd7afaeb ("sched/core: Optimize ttwu() spinning on p->on_cpu")
Reported-by: Dave Jones <davej@codemonkey.org.uk>
Reported-by: Paul Gortmaker <paul.gortmaker@windriver.com>
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Tested-by: Dave Jones <davej@codemonkey.org.uk>
Tested-by: Paul Gortmaker <paul.gortmaker@windriver.com>
Link: https://lkml.kernel.org/r/20200707102957.GN117543@hirez.programming.kicks-ass.net
Change-Id: I26d4c16043df672db986f8a9a24e013e21ac2d01
Signed-off-by: repinger <devel@repinger.my.id>

---
## [vtex/faststore](https://github.com/vtex/faststore)@[d476541686...](https://github.com/vtex/faststore/commit/d4765416862d2386e2b1a7767c2ee455282584d3)
#### Thursday 2023-12-21 13:38:04 by Fanny Chien

fix: Display discount badge only when has discount (#2173)

## What's the purpose of this pull request?

This PR attempts to fix scenario when there is no discount applied in
the product, and sale price is > listing price.

<img width="233" alt="image"
src="https://github.com/vtex/faststore/assets/3356699/fef94c1e-d50f-4c29-843b-41cbeca10783">


_I wonder if this logic should be inside the `ProductCardContent`
component (fs/ui library) or in the core. Any thoughts?_


## How it works?

When no discount applied, we should not display the `DiscountBadge`
component.

## How to test it?

<img width="1322" alt="image"
src="https://github.com/vtex/faststore/assets/3356699/3256f552-318b-4688-9ea2-08f37e7ae177">

1. Go to homepage -> Look for `Apple Magic Mouse` in the Most Wanted
section.
2. The `infinity` badge should not appear.

### Starters Deploy Preview

<!--- Add a link to a deploy preview from `gatsby.store` AND
`nextjs.store` with this branch being used. --->

<!--- Tip: You can get an installable version of this branch from the
CodeSandbox generated when this PR is created. --->

## References


[FS-1482](https://vtex-dev.atlassian.net/browse/FS-1482?atlOrigin=eyJpIjoiMWU1MGFjYTZkY2RiNDY2MGE0NGI4ZDZiNmZjODRkMWEiLCJwIjoiaiJ9)


[FS-1482]:
https://vtex-dev.atlassian.net/browse/FS-1482?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[24d8d41e01...](https://github.com/morgoth1145/advent-of-code/commit/24d8d41e0192fd3584b4e7238c724cc4592433a7)
#### Thursday 2023-12-21 13:47:09 by Patrick Hogg

2023 Day 21 Part 2

Wow. I normally wouldn't commit my solution *quite* this raw, but I spent ages trying a myriad of things and I'm going to commit the whole mess for posterity.

Where to even begin. At first I thought it might be good to handle it like parallel universes in Super Mario 64, counting how many "instances" are on each tile in the main grid. This doesn't work (at least not how I did it) because:
1) The iteration count we need to do is insane
2) This won't give the right answer anyway because we need to deduplicate stepping on the same coordinate, while also counting two coordinates from different universes that map to the same home coordinate.
Maybe there's a clever way to deal with both #1 and #2, but I never figured it out.

After that I tried a more direct simulation just to see how bad it was. Pretty bad, as I anticipated.

Then I tried to analyize how this monster grows. I had missteps along the way but had been making progress with a partial simulation (to 65+131*3 steps) and data extracted to count how many squares were in various grid universe "types" at the end of the whole simulation. I kept getting the math wrong though.

I then spent just over 3 hours debugging and trying a fully analytical approach until I got the right answer, which was a huge pain. (It didn't help that I was doing it all in my head instead of sketching anything. I finally cracked it when I sketched out the growth pattern over 3 cycles of 131 steps!)

As part of this I kept dumping out partial grids from both my simulation and my calculation branches to try to figure out what was going wrong. Now that I know the growth pattern and characteristics I maybe could solve this just with simulating for 65+131*2 steps and extracting info from that simulation, but that is a problem for some other time. I need sleep.

Rank 2145. I'm not sure if I was just slow in analyzing this or if I missed a huge trick which made this simpler...

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[57ac67bbfb...](https://github.com/TaleStation/TaleStation/commit/57ac67bbfbd2b98d0c81455313d04a4d730efbbd)
#### Thursday 2023-12-21 14:04:17 by TaleStationBot

[MIRROR] [MDB IGNORE] Delamination variants are now locked in after the countdown is reached (#9053)

Original PR: https://github.com/tgstation/tgstation/pull/80324
-----
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

---------

Co-authored-by: distributivgesetz <distributivgesetz93@gmail.com>

---
## [hdickie/expense_forecast](https://github.com/hdickie/expense_forecast)@[aa52d9f4f4...](https://github.com/hdickie/expense_forecast/commit/aa52d9f4f463a7690939d578a68c2a0cbaaf4bd7)
#### Thursday 2023-12-21 14:06:55 by Hume Dickie

the trivial translation from unittest to pytext using @pytest.mark.parametrize has mostly been accomplished. the remaining fixes require me to turn my brain on. Coverage is at 66% so that is my win for today. Meta comment: I feel a deep sense of relief as I submit this commit message haha. It doesn't have to be professional bc I'm not trying to be a data professional anymore. My git commit history is also my journal apparently DEAL WITH IT. Programming this project has been full of emotional ups and downs. It is December 21, 2023 and I am still writing code instead of having AI write it for me. I may as well be using punchcards lmao. Anyway love you, stay hydrated, love Hume <3

---
## [CrabbytheCrab/lobotomy-corp13](https://github.com/CrabbytheCrab/lobotomy-corp13)@[294f764ad0...](https://github.com/CrabbytheCrab/lobotomy-corp13/commit/294f764ad01a99c63b46dfea3dac7e5cfe14cd7d)
#### Thursday 2023-12-21 14:22:52 by Coxswain

Adds distorted form (#1435)

adds some basic features

new 1% sprite dropped

text update

Finished work mechanics

adds basic breaching

should fix linters a bit

It works!!!! Kinda...

adds crumbling armor and hammer of light (beta)

adds cool and important stuff

does a thing

adds apostle and tutorial abnorms

adds the stuff

might fix linters

adds a console proc

adds crumbling armor's proper attack and red queen

does some things

should fix linters

adds a blubbering toad transformation

adds more attacks

brings the tier up

adds big boy attacks

updates some sfx, fixes bugs

adds jump attacks

why does linters care about indentation on comments?

adds suggested changes

should fix some stuff

adds info

adjusts damage numbers

updates an effects and fixes transformations

updates blacklist

lowers stack damage

lowers max qlip to 3

adds bloodbath

adds a new AOE attack

adds halberd apostle

blacklists DF from pink midnight

fixes weirdness

requested changes and sound design improvement

removes armortype

removes armortype for real

damage coeff update

makes suggested changes

updates comments

adds procs

adds stuff

---
## [HallOfSame/AdventOfCode](https://github.com/HallOfSame/AdventOfCode)@[a61f2a4255...](https://github.com/HallOfSame/AdventOfCode/commit/a61f2a42551279e43d42fcfadd582adc07dc9db7)
#### Thursday 2023-12-21 14:29:00 by Dylan O'Gara

2023 Day 21 Part 2

Well I got an infinite map class out of it, and made the code faster. Funny how I hate this puzzle right after making fun of people for hating yesterdays puzzle. But in this case you basically output numbers until it looks like a quadratic I guess? And then use something else to calculate the quadratic because this isn't Python.

---
## [usnpeepoo/TerraGov-Marine-Corps](https://github.com/usnpeepoo/TerraGov-Marine-Corps)@[554acbd763...](https://github.com/usnpeepoo/TerraGov-Marine-Corps/commit/554acbd763ebd56cfdf35d4a5860e1e0b7071a31)
#### Thursday 2023-12-21 14:34:36 by vvvv-vvvv

Add a chat reliability layer (#14619)

* Adds a Chat Reliability Layer (#79479)

Everyone knows that chat will just eat your messages now and then, isn't
that annoying?
What if SSchat was smart enough to keep track of your messages and
notice when you didn't get one?
Well, now it can!

Chat messages poofing into the aether is bad, really bad.
:cl:
add: Chat Reliability Layer
code: TGUI chat messages now track their sequence and will be resent if
the client notices a discrepenency
/:cl:

---------

Co-authored-by: Kyle Spier-Swenson <kyleshome@gmail.com>
(cherry picked from commit e1c6cfdce89c7dbcd507d0c44803f5407a042a96)

* Fixes sending stuff to "Old" Chat (#79819)

## About The Pull Request

This functionality was removed in #79479
(e1c6cfdce89c7dbcd507d0c44803f5407a042a96), and we should still be
supporting the old chat anyways because it contains a plethora of useful
BYOND information that we still can really leverage (such as the
built-in profiler and stuff like that) and it's going to be painful to
do that if you have to keep spamming `fix-chat` to see OOC/ASAY while
alternating every damn time.
## Why It's Good For The Game

It's ugly but we still need it. There's a reason why we still have it.
## Changelog
:cl:
fix: "Old Chat" (AKA: The old-styled non-TGUI raw-HTMLesque chat that
you might see when it prods you with the "Failed to load fancy chat!"
issue) should now get all text messages as expected.
/:cl:

(cherry picked from commit eb246c21f6eb5380dc56e5779fcd51d11437557c)

* Fixes chat bluescreen (#79821)

## About The Pull Request
Adds a chat reliability layer reliability layer

<details>
<summary>more info</summary>

json.parse claims another

![d86](https://github.com/tgstation/tgstation/assets/42397676/c7d864f2-b5d6-4c5d-95b4-deece37c808d)

javascript completely opaque about what throws. innocuous function not
wrapped in try/catch block

</details>

## Why It's Good For The Game
No bluescreen?
Fixes #79814
## Changelog
:cl:
fix: Chat shouldn't bluescreen at the start of the round
/:cl:

(cherry picked from commit cfeb2d84eb92dcd0abae5c9353b8b35bc4ecdd39)

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[212142f210...](https://github.com/TaleStation/TaleStation/commit/212142f210b15affe399b20335a20de594c968d4)
#### Thursday 2023-12-21 14:40:47 by TaleStationBot

[MIRROR] [MDB IGNORE] The Spectre-Meter App, also a bootleg data disk item for the black market. (#9103)

Original PR: https://github.com/tgstation/tgstation/pull/80188
-----
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

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Holoo-1/tgstation](https://github.com/Holoo-1/tgstation)@[a1e46c5d31...](https://github.com/Holoo-1/tgstation/commit/a1e46c5d31347887de95520eee31c00749379b9c)
#### Thursday 2023-12-21 15:07:51 by Jacquerel

Basic Guardians/Holoparasites (#79473)

## About The Pull Request

Fixes #79485
Fixes #77552

Converts Guardians (aka Holoparasites) into Basic Mobs.
Changes a bunch of their behaviours into actions or components which we
can reuse.
Replaces some verbs it would give to you and hide in the status panel
with action buttons that you may be able to find more quickly.

They _**should**_ work basically like they did before but a bit
smoother. It is not unlikely that I made some changes by accident or
just by changing framework though.

My one creative touch was adding random name suggestions.
The Wizard federation have a convention of naming their arcane spirit
guardians by combining a colour and a major arcana of the tarot. The
Syndicate of course won't truck with any of that mystical claptrap and
for their codenames use the much more sensible construction of a colour
and a gamepiece.

This lets you be randomly assigned such creative names as "Sparkling
Hermit", "Bloody Queen", "Blue World", or "Purple Diamond".
You can of course still ignore this entirely and type "The Brapmaster"
into the box if so desired.

I made _one_ other intentional change, which is to swap to Mothblocks'
nice leash component instead of instantly teleporting guardians back to
you when they are pulled out of the edge of their range. They should now
be "dragged" along behind you until they can't path, at which point they
will teleport. This should make the experience a bit less disorienting,
you have the recall button if you _want_ to instantly catch up.

This is unfortunately a bumper-sized PR because it did not seem
plausible to not do all of it at once, but I can make a project branch
for atomisation if people think this is too much of a pain in the ass to
review.

Other changes:
- Some refactoring to how the charge action works so I could
individually override "what you can hit" and "what happens when you hit"
instead of those being the same proc
- Lightning Guardian damage chain is now a component
- Explosive Guardian explosive trap is now a component
- Added even more arguments to the Healing Touch component to allow it
to heal tox/oxy damage and require a specific click modifier
- Life Link component which implements the Guardian behaviour of using
another mob as your health bar
- Moved some stuff about deciding what guardians look and are described
like into a theming datum
- Added a generic proc which can return whether your mob is meant to
apply some kind of damage multiplier to a certain damage type. It's not
perfect because I couldn't figure out how ot cram limb modifiers in
there, which is where most of it is on carbons. Oh well.
- Riders of vehicles now inherit all movement traits of those vehicles,
so riding a charging holoparasite will let you cross chasms. Also works
if you piggyback someone with wings, probably.

## Changelog

:cl:
refactor: Guardians/Powerminers/Holoparasites now use the basic mob
framework. Please report any unexpected changes or behaviour.
qol: The verbs used to communicate with, recall, or banish your Guardian
are now action buttons.
balance: If (as a Guardian) your host moves slightly out of range you
will now be dragged back into range if possible, rather than being
instantly teleported to them.
balance: Protectors now have a shorter leash range rather than a longer
one, in order to more easily take advantage of their ability to drag
their charge out of danger.
balance: Ranged Guardians can now hold down the mouse button to fire
automatically.
balance: People riding vehicles or other mobs now inherit all of their
movement traits, so riding a flying mob (or vehicle, if we have any of
those) will allow you to cross chasms and lava safely.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [samskivert/adventofcode](https://github.com/samskivert/adventofcode)@[c71f6d7205...](https://github.com/samskivert/adventofcode/commit/c71f6d72056a31cdfed52da0ef568cac28fbed59)
#### Thursday 2023-12-21 15:36:05 by Michael Bayne

Day 17.

I started with plain A* and tried various hacks to account for the max straight
path condition but was just not getting it. Then I tried Dikjstra but that
didn't work either. In the end, I had to look it up; I'm dumb.

Given the simple insight that we're searching a 4D space instead of a 2D space,
everything was much simpler and fell into place immediately with no funny
business.

I can try to blame it on the brutal sinus headache I have had the last three
days, but I probably would not have figured it out even had my brain been
working at normal capacity, so I won't flatter myself.

---
## [HickeysTechCompany/finalsprintbackend](https://github.com/HickeysTechCompany/finalsprintbackend)@[0bcb5c8c5c...](https://github.com/HickeysTechCompany/finalsprintbackend/commit/0bcb5c8c5c7b7d0c1bfd27a8b2a5848de3cf4337)
#### Thursday 2023-12-21 15:39:59 by Colonater

WORKING BACK END HELL YA

please please for the love of god make a branch of this and merge im sick of manuelly merging ur guys

---
## [rnpnr/aoc2023](https://github.com/rnpnr/aoc2023)@[149724fd0a...](https://github.com/rnpnr/aoc2023/commit/149724fd0a0ac682929edc8b45bc106847a0fc0a)
#### Thursday 2023-12-21 15:50:02 by Randy Palamar

day 8

Day 8 started out as a nice problem with some interesting
solutions but quickly grew frustrating with part 2 (partly because
of Haskell and partly because of the problem itself).

To start with I immediately compressed the input by ~33% by
converting all the nodes to base 26 integers (3 ASCII digits
require at least 24 bits, but converting to base 26 requires 26^3
values which fits in 16 bits). The instructions were converted
into a list of functions the head of which is applied to the
current node to get to the next node. Then the path is easily
traversed.

Part 2 is also fairly trivial to implement the, correct, general
solution but the inputs were chosen such that the runtime would be
much too long (apparently some people did it in reasonable runtime
using more efficient languages). As it turns out however, the
inputs were also chosen such that you could just find the LCM of
all the paths. Its just that this was not indicated anywhere (I
had originally considered this approach but discarded it before
writing because it would not be correct in general). After
struggling for a while not knowing if my general algorithm was
correct (it is) I learned that people were just using LCM. I would
have found out this solution would work sooner if Haskell had any
reasonable way of printing out intermediate values because I would
have noticed the cyclic nature of each path. But alas my long
lived frustration with this aspect of Haskell continues.

Even using the LCM approach the solution is relatively slow. I
reckon I could write a much faster version in C but I'm not sure I
care enough about this specific problem to do so. Runtime:

avgtime -n 64 ./day8 input
real 1.390469
user 1.372344
sys 0.000469

(I realized that my avgtime script doesn't play nice with data
from stdin. I will fix later or replace with a simple C program)

---
## [blueloveTH/TIC-80](https://github.com/blueloveTH/TIC-80)@[c86219f735...](https://github.com/blueloveTH/TIC-80/commit/c86219f73563aefee4f81bceb6b58f957697f069)
#### Thursday 2023-12-21 15:51:56 by bonjorno7

Implement trim on save

I'm not too experienced with C so this was tough, but I got it working.
It trims spaces at the end of lines, and newlines at the end of the file (except for the last one, if there's space for it).
It also updates the cursor position and selection.

I increment src after the done check so that its value is correct after the loop; not actually using it after the loop in this version but just in case.
That check by the way uses a stored variable because the loop overwrites the buffer, so checking the value of end at the bottom of the loop doesn't work.
I'm using memmove instead of memcpy because the data can overlap, and this is apparently still quite fast.
I don't zero out garbage data after the terminator because it's apparently unnecessary.
After trimming whitespace it calls history and update; hopefully those are the right functions in the right order.

One small note: if your selection was entirely trimmed, you're left with a zero length selection.
I can fix this by detecting if position and selection are equal, and then setting selection to null.
I chose not to do this however, because it's easy to create a zero length selection by hand, and the user might in some cases do so intentionally.
If you want to get rid of zero length selections entirely, that should probably be fixed elsewhere, rather than in this function.

Another note: trimming only happens with Ctrl + S, not with typing save in the console.
Perhaps I should fix this, though I think it has advantages too; I think ideally the trimming should only happen when you can see it happening, which you can't if you're in the console.
Also while writing this code it was nice to be able to undo and save my file without running the trimming code, though I suppose now that the code works properly I won't need it anymore.

---
## [Sockshare/genaicreations](https://github.com/Sockshare/genaicreations)@[3480fba7cd...](https://github.com/Sockshare/genaicreations/commit/3480fba7cd5c2a2ae5a71706b0fea49cd965517f)
#### Thursday 2023-12-21 16:08:08 by Sockshare

Update README.md

Commit Message:

feat: 🚀 Introduce Generative AI Renders Repository ReadMe

Description:

Buckle up, fellow code adventurers! This commit marks the launch of the Generative AI Renders repository, where the magic of artificial intelligence meets the vibrant world of creativity! 🎨✨ Get ready to explore, contribute, and dive deep into the mesmerizing universe of generative AI.

Changes Made:

1. **ReadMe.md:** Added a detailed and upbeat ReadMe file, providing a lively introduction to the repository and offering a glimpse into the folder structure and exploration process.

Motivation:

Why the hype, you ask? Well, we're not just dealing with pixels; we're orchestrating symphonies of code and creativity! 🚀 This ReadMe is designed to be your trusty guide as you navigate through the diverse renders housed within our "Renders" folders. It's not just about showcasing images; it's about unraveling the stories behind each creation — the applications, the prompts, and the sheer joy of bringing pixels to life.

So, whether you're a seasoned generative artist, a curious coder, or just someone looking for a dash of inspiration, join us on this exhilarating journey! Let's paint the digital canvas with bits and bytes, one commit at a time. 🌈🤖

---
## [Unleash/unleash](https://github.com/Unleash/unleash)@[c44601b33c...](https://github.com/Unleash/unleash/commit/c44601b33cb701e324e56cb6ba6217ff48de497a)
#### Thursday 2023-12-21 16:15:25 by Nnenna Ndukwe

React Tutorial Improvements (#5657)

<!-- Thanks for creating a PR! To make it easier for reviewers and
everyone else to understand what your changes relate to, please add some
relevant content to the headings below. Feel free to ignore or delete
sections that you don't think are relevant. Thank you! ❤️ -->

## About the changes
<!-- Describe the changes introduced. What are they and why are they
being introduced? Feel free to also add screenshots or steps to view the
changes if they're visual. -->

We've made some first round updates to the React tutorial:

- making it more SEO-friendly with ordered lists, sequential language,
description of the JS library
- Switched over the demo app to point to an open source project:
[Cypress Real World
App](https://github.com/cypress-io/cypress-realworld-app)
- included best practice considerations for client-side development
- updated URL path to point to `/feature-flag-tutorials/react` for
simplification


## Discussion points
<!-- Anything about the PR you'd like to discuss before it gets merged?
Got any questions or doubts? -->

Would love feedback on if there's a need for more screenshots? Don't
want to be too screenshot-heavy though I imagine.
And need feedback on the descriptions of "Considerations for using
feature flags in react"
https://github.com/Unleash/unleash/compare/react-improvements?expand=1#diff-96d4956f49f80cd76489a72d4d88c2956ce9dcc695f66fe014ad1185e37cb589R21

Want to make sure that what I described makes sense or if it could use
some tweaking to convey the right message clearly.

---
## [dagster-io/dagster](https://github.com/dagster-io/dagster)@[5168f5a8ee...](https://github.com/dagster-io/dagster/commit/5168f5a8ee14ef0af13ff65c9f567d7b27deb437)
#### Thursday 2023-12-21 16:34:56 by quantum-byte

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
## [Qiskit/documentation](https://github.com/Qiskit/documentation)@[9ce5f6422d...](https://github.com/Qiskit/documentation/commit/9ce5f6422d9cd59b5311c3bc5752236ce21b00e9)
#### Thursday 2023-12-21 17:04:17 by Arnau Casau

Allow dedicated page for each method (#543)

Part of fixing https://github.com/Qiskit/documentation/issues/542.

## Methods living on dedicated pages

Before Qiskit 0.44, methods lived on dedicated HTML pages. We changed
that in Qiskit 0.44 because it resulted in horrible build-time
performance when migrating `qiskit.org/documentation` from the old
Pytorch theme to the new Furo theme, so that instead methods lived
directly on their class pages.

It looks like the script `updateApiDocs.ts` was trying to emulate
methods living on class pages before Qiskit 0.44 through the file
`mergeClassMembers.ts`. This code attempted to remove the method pages
and instead have them live directly on the class pages.

I believe the original script author had `mergeClassMembers.ts` to try
to avoid performance issues. Until a fix a few weeks ago to the docs
application, having a huge amount of pages would cause the site to load
extremely slowly due to the left side bar being too large. That is now
fixed because the left side bar is loaded dynamically rather than
statically.

## `mergeClassMembers.ts` was causing problems

1. It looks like it wasn't behaving properly, at least some of the time.
We did not exhaustively audit every page, but for example,
https://docs.quantum.ibm.com/api/qiskit/0.33/qiskit.result.Result only
had properties at the top, then a table summarizing all the methods
below, but not the methods actually inlined:

<img width="774" alt="Screenshot 2023-12-21 at 11 43 47 AM"
src="https://github.com/Qiskit/documentation/assets/14852634/576ff54a-763c-484d-bc3b-42068693b0d1">

2. We didn't know about this inlining when setting up qiskit.org
redirects, which do a 1:1 mapping so that dedicated method pages take
you to the dedicated method page on IBM, which was 404ing.

## Solution: allow dedicated method pages

By deleting `mergeClassMembers.ts`, the script will properly generate
dedicated HTML pages for each method.

We took this approach—rather than instead fixing
`mergeClassMembers.ts`—for a few reasons:

1. It allows us to avoid messing with our redirect rules, which are the
1:1 mapping.
2. We've gotten user feedback that the API docs are not as usable as
they could be. We are planning to fix that in
https://github.com/Qiskit/documentation/issues/479, but it won't be
fixed in time for putting out the fire of
https://github.com/Qiskit/documentation/issues/542. In the meantime, it
is more user-friendly to have dedicated method pages for those
historical API docs.

The biggest reason we would not want to take this approach of dedicated
method pages is the possible impact on performance mentioned above. But
that has been fixed already in the IBM application.

## Impact of this PR

No impact when generating docs where methods already live on class
pages, like Qiskit 0.44+.

For earlier Qiskit versions, it results in the method pages being
generated. Those will be added in follow up PRs.

---------

Co-authored-by: Eric Arellano <14852634+Eric-Arellano@users.noreply.github.com>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a71f45be9e...](https://github.com/mrakgr/The-Spiral-Language/commit/a71f45be9ead964485fece0fca46ccbf40a39e49)
#### Thursday 2023-12-21 17:26:11 by mrakgr

"10:05am. https://www.youtube.com/watch?v=_mIiTvJk7dg
Thenar and Hypothenar Atrophy

Right now I am having issues with this and want to do some research on it.

11:30 AM. Let me do some programming here. I wasted quite a lot of time doing nothing. I did some research on dinner atrophy, but it seems exercise steroids and that kind of thing is the only choice. I'm thinking maybe better actually to stop doing the exercises because it's trains main thumb.

My fingers are better than they have been in months, but now my tumba is the one that is giving me the most concern. I keep getting persistent pain in it. Not a large amount, mind you, but some pre clicking. If it's just a pain itself, I wouldn't care about it. But I'm losing muscle mass. So that's what is giving me concern. I have no idea when this will stop. Typically these are symptoms of neuro entrapment, but I already did the test for it and it came out negative. I guess in two weeks the physiotherapy will tell me what to do.

Right now, it's Thursday, and I still haven't gotten word of the apple chat pad being sent. I guess it really will get here some time next week. I can't even lucky with it this time around.

Okay for today, let me just focus on doing the tests for the hand ranker. I'll compare the new one with the old one. Once I do that, it will be a major milestone, because I'll be able to move on to the game itself.

I'm never going to let this happen again. Whether that be hand pain or switching the hardware, I'm going to bet big big Nvidia, because those ai hardware startups are so **** bad. People crap on imd and Intel. But those **** ai hardware startups are completely useless. There were hundred of them, and literally none of them had any effect on this AI wave. They completely missed the generative AI boom. I couldn't have possibly imagined that they would be this incompetent. But I am expecting now is that the efforts of Intel and amd will, as well as the hyperscalers, will cause Nvidia to drop a prices. So in fact, there is no real need for me to rewrite my software. in the future.

I'm going to do everything right this time around. I'm going to make the game on the gpu and make the training and the email library for it all there.

Thought that I would do this quickly.

But now that this has been giving me this much difficulty, what I'm going to do is going to web 3 and crypto and see whether there are some poker rooms that use cryptocurrency. That way, if I get detected as an AI bot user, I won't lose everything. Losing money is not the problem, but if, for example, I lost my account on a poker stars, I have no way of getting back. I'm not some elite hacker with infinite proxy accounts. The Web 3 environment will give me a place to develop in relative safety. When I conquered those places, then I can set my sights on the real world.

https://youtu.be/JczNHT_2uHA?t=15
The Ploopy Trackball(s)

A keyboard with a integrated tracker ball. That's a pretty interesting actually.

https://www.reddit.com/r/mac/comments/z9n0ly/anybody_agree_that_apples_magic_trackpad_is_much/
> its notably better wired compared to bluetooth. i was hesitant leaving it plugged in all the time so i started using the magic mouse but kinda getting sick of its goofy ergonomics so back to trackpad but this time wired YOLO it may or may not swell after 2-3 years.

> People are absolutely insane here. I have both the trackpad and magic mouse - the trackpad collects dust while the MM gets used every day for the past 8 years.

It seems there are some contrarians that prefer the mouse.

4:00 PM. I need to take a break already because I am starting to get a burning feeling in my ring finger from all the typing.

It is finally the last but damn it really hurts now. Actually, it doesn't really hurt too badly, but it's going to hurt if I resume typing.

https://www.youtube.com/results?search_query=lightest+mouse

I just got the idea of searching for the light as possible mouse and I found this one. These are like 20 grams.

https://youtu.be/n006S8nue7U?t=224

I should consider getting this mouse.

https://zaunkoenig.co/m3k
444 M3K on December 17th; 340 Euros; free world-wide express shipping

Damn, they are expensive.

Never mind, this is a dead end. These mates are especially made, and they're not very available.

```spiral
open corebase

inl prim x = real
    match x with
    | (x : i8) | (x : i16) | (x : i32) | (x : i64) => "%d", x
    | (x : u8) | (x : u16) | (x : u32) | (x : u64) => "%u", x
    | (x : f32) | (x : f64) => "%f", x
    | (x : string) => "%s", x
    | (x : char) => "%c", x

inl rec write l : () = real
    inl array_limit = 100
    open real_core
    inl p (a,b) = $"printf(!a,!b)" : ()

    match l with // According to Bing it shouldn't matter whether these are %d or %lld in printf.
    | (x : i8) | (x : i16) | (x : i32) | (x : i64) => p ("%d", x)
    | (x : u8) | (x : u16) | (x : u32) | (x : u64) => p ("%u", x)
    | (x : f32) | (x : f64) => p ("%f", x)
    | (x : string) => p ("%s", x)
    | (x : char) => p ("%c", x)
    | (a,b) => write a . write b
    | {} as x =>
        record_fold_back (fun {state=(separator, state) key value} =>
            "; ", (symbol_to_string key," = ", value, separator, state)
            ) a ((), ())
        |> fun _,x => write ('{', x, '}')
    | () => ()
    | x when symbol_is x => write (symbol_to_string x)
    | x =>
        typecase `x with
        | sa ~dim _ =>
            write "["
            open sam
            loop.for {from=0; nearTo=max array_limit (length x)} (fun i =>
                write (index x i)
                if i + 1 < length x then write ", "
                )
            if length x > array_limit then write ", ..."
            write "]"
        | _ => error_type "Unsupported type."

inl write_nl l =
    write l
    $'printf("\\n")'
    ()
```

Let me go have lunch. This is what I've been bussying myself today. Until my hand starts to smart, I've been making especially good progress.

Now that I've healed somewhat, what I should do next is pick up a habit of making small breaks.

I find it now that I have taken one and a half hour break before receiving programming. My right hand has completely healed. I mean relaxed. Maybe I even shorter break would be fine to get over the burns.

I feel like I have been very dexterous today. I am using this glove 80 keyboard like nothing else. It feels very comfortable to type on right now.

Maybe I'll do even more after lunch, we'll see."

---
## [hussam178/liquid](https://github.com/hussam178/liquid)@[0b2fedb403...](https://github.com/hussam178/liquid/commit/0b2fedb40354a217fcb649deaf9396528eb3e1ee)
#### Thursday 2023-12-21 17:42:41 by hussam178

Create Themes 

A professional template for an online store catering to dropshipping products in Arabic should prioritize a seamless user experience and incorporate essential features. Here's a comprehensive description:

**1. Responsive Design:**
   - Ensure the template is fully responsive, adapting to various screen sizes and devices, providing a consistent and user-friendly experience for customers accessing the online store from different platforms.

**2. Arabic Language Support:**
   - Integrate robust Arabic language support throughout the template, including RTL (Right-to-Left) layout. This ensures a culturally appropriate and comfortable browsing experience for Arabic-speaking users.

**3. Clean and Intuitive Navigation:**
   - Design an intuitive navigation system with clear menus, categories, and search functionality. Facilitate easy exploration of products and seamless navigation between pages.

**4. High-Quality Imagery:**
   - Emphasize high-quality product images with zoom features to allow customers a detailed view of items. Visual appeal is crucial in online shopping, and clear images enhance the overall aesthetic.

**5. Product Categories and Filters:**
   - Organize products into relevant categories and provide effective filtering options. This makes it simple for customers to locate specific items, enhancing their shopping experience.

**6. Secure Checkout Process:**
   - Implement a secure and straightforward checkout process. Clearly outline the steps, offer multiple payment options, and reassure customers about the security of their personal and financial information.

**7. Integration with Dropshipping Platforms:**
   - Seamlessly integrate the template with dropshipping platforms to automate order fulfillment, inventory management, and product updates. This ensures efficiency and accuracy in handling orders and product information.

**8. Multilingual Support:**
   - If the target audience extends beyond Arabic speakers, consider incorporating multilingual support to accommodate a broader customer base.

**9. Customer Reviews and Ratings:**
   - Include a section for customer reviews and ratings to build trust and credibility. Positive feedback can influence potential customers and enhance their confidence in making a purchase.

**10. Social Media Integration:**
   - Integrate social media buttons and sharing options to encourage customers to share products and promote the online store on various platforms.

**11. Promotional Sections:**
   - Include sections for promotions, discounts, and featured products to attract attention and drive sales.

**12. Mobile App Compatibility:**
   - If feasible, ensure compatibility with mobile apps for both Android and iOS platforms, providing an additional channel for customers to access the store.

A professional online store template for dropshipping products in Arabic should balance aesthetics with functionality, creating a positive and efficient shopping environment for customers. Regular updates and optimizations based on user feedback are essential for ongoing success.

---
## [b12k/naming-cheatsheet](https://github.com/b12k/naming-cheatsheet)@[8bcb483976...](https://github.com/b12k/naming-cheatsheet/commit/8bcb4839762053a095ee8cbbf3b4f5b471d01181)
#### Thursday 2023-12-21 17:45:00 by tebb

docs: improve a/hc/lc pattern order explanation (#40)

Thank you.  This cheatsheet is very useful.

If I understood the logic, my changes to README.md may be helpful.  If not, sorry :)

Also ... Could you add shouldUpdateComponent and shouldComponentUpdate into the table (or an extension to the table below Note:).  It isn't obvious to me which columns 'should', 'Update' and 'Component' are in because 'Update' is the verb (action?).

Thanks.

---
## [Mirag1993/mrdg](https://github.com/Mirag1993/mrdg)@[d960193cdb...](https://github.com/Mirag1993/mrdg/commit/d960193cdb07ccce873e22ade5c81be03e505018)
#### Thursday 2023-12-21 17:53:37 by BluBerry016

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
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[bf869a0ded...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/bf869a0ded3a3ca5e00500ef5ad856bcb7f012dd)
#### Thursday 2023-12-21 18:12:31 by Bloop

[MISSED MIRROR] Fixes runtime relating to hard TGS reboots (PROBABLY WON'T FIX REBOOT CRASHES) (#25185)

Fixes runtime relating to hard TGS reboots (PROBABLY WON'T FIX REBOOT CRASHES) (#77309)

## About The Pull Request

Servers are crashing on every round restart and I have absolutely no
idea where to start, but I noticed this so I figure I'll throw up a PR
to fix it.

This is the runtime (only found in dd.log, sorry non-admin/maintainer
gamers
https://[tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log](https://tgstation13.org/raw-logs/sybil/data/logs/2023/08/01/round-211577/dd.log)
)

```txt
[00:07:07] Runtime in code/modules/logging/log_holder.dm,166: Attempted to call shutdown_logging twice!
  proc name: shutdown logging (/datum/log_holder/proc/shutdown_logging)
  src: /datum/log_holder (/datum/log_holder)
  call stack:
  /datum/log_holder (/datum/log_holder): shutdown logging()
  shutdown logging()
  world: Reboot(0, 0)
  Ticker (/datum/controller/subsystem/ticker): Reboot("Round ended.", "proper completion", 600)
```

This is the full log:


![image](https://github.com/tgstation/tgstation/assets/34697715/af938235-3076-41d5-98b2-02907dedb6d5)

This is the code:


![image](https://github.com/tgstation/tgstation/assets/34697715/371b11cb-3bc9-4a99-a17c-73968ded308d)

For some reason, even though we invoke `TGSEndProcess`, we still
continue on in this `if()` chain. I don't know why we keep executing DM
code after TGS is supposed to be shut down (which may be why no one has
ever included a `return` here, but let's be safe instead of sorry.

If you really want to investigate why TGS is running DM code after we
end the process, I am amenable to including a stack trace or crash of
this phenomenon instead.
## Why It's Good For The Game

Since we aren't invoking `LOG_CLOSE_ALL` to rust-g twice (which seems to
be really unwanted per the code I read), hopefully thing no crash?
Rust-g had two breaking changes (one with logs, and one with SQL), so
I'm presuming that this might be related to the log one (which is why we
didn't see this sorta thing happen pre-#77307)... Worst case scenario
less runtimes in the funny runtime log.

I hope this wasn't loadbearing either... Likely requires testmerging
since TGS and I don't get along on my machine.
## Changelog
:cl:
server: Added a preventative measure to prevent calling both
TGSHardRestart and TGSReboot, as well as potentially invoking sensitive
procs that are only meant to be called once.
/:cl:

TL;DR- I do not definitively know why servers are crashing but I noticed
this runtime so I'll put out this open flame while I have the time to do
so.

Co-authored-by: san7890 <the@san7890.com>

---
## [DanaDririon/Skyrat-tg](https://github.com/DanaDririon/Skyrat-tg)@[fc0dc4ec6f...](https://github.com/DanaDririon/Skyrat-tg/commit/fc0dc4ec6f1d9ce02608825df6a6f942fec44b8c)
#### Thursday 2023-12-21 18:15:58 by SkyratBot

[MIRROR] Changes Virology Rather Than Killing It [MDB IGNORE] (#25483)

* Changes Virology Rather Than Killing It (#79854)

## About The Pull Request
God, alright, here we go. See HackMD here:
https://hackmd.io/@ Higgin/HJljdBuNp

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

* Changes Virology Rather Than Killing It

---------

Co-authored-by: Higgin <cdonny11@yahoo.com>

---
## [DanaDririon/Skyrat-tg](https://github.com/DanaDririon/Skyrat-tg)@[015a3cf18a...](https://github.com/DanaDririon/Skyrat-tg/commit/015a3cf18a133ef12c1ee5bac4a4179140ecbc75)
#### Thursday 2023-12-21 18:15:58 by Bloop

[MANUAL MIRROR] Replaces prettierx with the normal prettier (#80189)  (#25538)

* Replaces prettierx with the normal prettier (#80189)

Oh god the file diff... I'm so, so sorry.

No need to worry though. This just replaces the prettierx version that
we were using and replaces it with normal prettier. Most of the settings
were default or no longer valid with this version.
You no longer get this warning #70484

It actually drives me up the wall and I have to click it each time I
open my editor.
N/A nothing player facing

* Converts this to tsx

* Update JobsPage.tsx

* Update JobsPage.tsx

* Update JobsPage.tsx

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [wrye-bash/wrye-bash](https://github.com/wrye-bash/wrye-bash)@[84cb3caf94...](https://github.com/wrye-bash/wrye-bash/commit/84cb3caf943c053dd85166af184cc56b71ebe1cb)
#### Thursday 2023-12-21 18:26:26 by MrD

Squashed version of ut-353-pt1-578:

Refactoring in load order:

Move  the logic of _filter_active in callers - they were doing the checks
anyways - then inline - we certainly want to thin LoGame API, _games_lo
is complex enough and flat is better (and shorter) than nested here.

_CleanPlugins(LoGame):

Clean/create logic is very hard to follow - let's confine it to games that
need it. We then need to clarify what happens with cached parameters vs
creating the plugins txt - AsteriskGame._fetch_load_order logic is still
hard to follow see todos added there.

EAFP for parsing mod file

Then I realized that since 96394dda9179188825cc184ea84d689bda667824
actually for Textfile games we only need to remove the master_path,
so _active_entries_to_remove is only needed in AsteriskGame - then
_clean_actives, which for Asterisk necessarily cleans
the whole plugins.txt, is inlined taking down tricky logic and lots
of comments trying to explain what goes on.

Oh lord_func:

I. Use the return value:

This necessitated returning from _update_cache -> refresh_lo (single
use). For now I return the cached_lord - this is temporary, we will
eventually confine cached_lord to load_order.py, but we need to forge
a ring for that - that's part II.

quiet WIP:

get_load_order had quiet=False effectively - added this as default to
fix_load/active and then in set_load_order quiet=True and set it only
in load_order.save_lo

Became clear that warn_missing_lo_act was only updated when quiet was
False which was when lo_deprint was called. This simplified the bolts
of _game_lo at the expense of a local modInfos import - nice.

The timestamp game _fix_load_order override was tricky to get - if fix_lo
was None, which only happened in _restore_lo (quiet=True and
set_load_order validation) and in refresh_lo (for validation of a saved
load order), it would not reorder the added plugins but add them to the
end - I kept that but dropped the debug message as anyway the lo_added
will be printed. What we should do when a plugin is added needs
standardizing - makes sense to add them at the end so saves show blue.

Mopy/bash/basher/__init__.py: nit, better reset a dialog trigger before
showing the dialog lest one falleth into an infinite loop.

Expose more LoadOrder attributes:

The index dicts contain all the info of load order/active changes - as
a bonus a couple one-line, one-use methods were removed. load_order.py
is the balt of load order handling and although (because of saved load
order handling) it does have a well defined role it still needs to be
kept at a minimum - more on this later.

Simplify/optimize _refresh_mod_inis:

No need to clean up since we overwrite at the end - pruned also the OD.

Only the values of _plugin_inis was used - this will re-become a dict
but for now simplify and make easier to track by exposing it and
removing essentially nothing-new ini_files (not the ini_files.py
module).

WIP refactor BP activations handling:

count would decide on refreshing saves - probably if any mods got
activated we should DO. Moved the info handling higher up, I need to do
activations in parent.

Reduce occurrences of lo_activate (2)/cached_lo_save_active (1) - these
must be further confined. Note the decoupling from load_order (and Link)
in patcher_dialog.py

_modTimesChange -> unlock_lo - mod redates fix:

Was unlocking in all except one case - in those cases unlocking made
only sense if the game was a timestamp game - I am glad I kept
_modTimesChange and gladder I dropped it

Needs some testing as there are subtle changes in the logic - note that:

mod_links.py: we wouldn't unlock. That was actually a bug (if lock load
order was on) as the redates would silently be reverted in refresh_lo
(with no change shown in the UI) and then a dialog would be displayed on
*next time* we would tab in to Bash (still no change in the UI).
That was probably not the intention :P

Mopy/bash/basher/app_buttons.py: while we did unlock always we did not
forceRefresh - well it's a couple stats() added, won't harm

The rest is fine - just one more use of using_txt_file, inside the same
(DoSave) scope - good sign.

Mopy/bash/basher/installers_links.py: the (not so) long term goal is to
absorb this into refresh - need to refactor base signature for this.

WIP setGhost return status change: RRR TTT drop notify bain?

This gets us rid of a few uglyStuff including a Path method (# RRR 368), and
one bare except - we might as well deprint out (and maybe tighten the
remaining except).

As seen in _refresh_from_data_dir we chop off the ghost extension so we
should not notify BAIN TTT cause data_sizeCrcDate is difficult to track,
hence WIP see next commit

Under # RRR 219

isGhost -> is_ghost:

Now that autoGhost is (will) be gone

Some nit - in particular no need to create these (None, None, None) tuples

Drop _reset_info_sets: TTT EEE Mopy/bash/basher/files_links.py

Finally, this set up was a smell. This makes some calls like new_info
more expensive but no worries

TTT new_info: the _in_refresh param is obviously a temp hack :P

WIP decide what we need to refresh in restore backup:

This is partial (new_info is the hardest to absorb in refresh from the
refresh satellites). No need to further dig in there - refresh will see
an overhaul soon.

Sort by master status once in _fix_load_order: EEE drop allow_deactivate_master?

Trying to make complex less complicated here - comments included. This
permitted inlining _index_of_first_esp - IIUC we just needed to calculate
once and then increment. So one function and 2 uses of in_master_block
down - neat.

More undead pruning: RRR

Including one more modInfos local import - typing is badly needed here

Mopy/bash/gui/popups.py: user_ok was essentially unused, was checked in
show_modal - while quietly doing RRR

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[b9ef508d2c...](https://github.com/treckstar/yolo-octo-hipster/commit/b9ef508d2c108fbdc5ecb556ccc3103b5a8bc71f)
#### Thursday 2023-12-21 19:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [HerculesChrysanthos/frontend-cook-hub](https://github.com/HerculesChrysanthos/frontend-cook-hub)@[9252760244...](https://github.com/HerculesChrysanthos/frontend-cook-hub/commit/92527602442b037e653855f1cd5192154f38275a)
#### Thursday 2023-12-21 20:02:14 by kostassifa

final handling in registration messages maybe i dont know we will see i hate my life so much

---
## [ihatethisengine/cmss13](https://github.com/ihatethisengine/cmss13)@[dc234c9939...](https://github.com/ihatethisengine/cmss13/commit/dc234c9939efeb43170a934437f50148323407f7)
#### Thursday 2023-12-21 20:24:48 by InsaneRed

Oppressor cooldown changes (#5154)

# About the pull request

Lowers the oppressor tail_abudct (the hook) to 15 seconds of cooldown
and makes the windup faster.

Makes punch shave off cooldown from the abduct for 5 seconds 

All have been tested but i would like this to get testmerged first so i
can actually see the results in game, nothing is set in stone and i want
to edit this further so the cd / cd reduction isnt too powerful, they're
just numbers ive decided were good enough to atleast make the caste
decent for the time being.


# Explain why it's good for the game

Oppressor has been a snoozer strain for a while now where you cast an
ability, and IF it hits you get to play the game otherwise you wait 20
seconds and thats just not fun. Especially for what the ability is, a 20
second cooldown is not worth it.

I've talked with a few people that all agree that the downtime for what
you "could" do with oppressor is not worth it. And i have to agree with
them, the caste feels boring to play and its basically half dead due to
the amnout of downtime you have between abilities compared to how
everything else works. The idea of this is to make it so its not busted
out of its brain but atleast not an observer++ strain so you can feel
more involved in the gameplay.




# Testing Photographs and Procedure
</details>


# Changelog



:cl:
balance: Oppressor tail abduct changed to 15 seconds and lowers the
windup to 7 deciseconds
balance: Changes around the punch effect so that instead of having to
meet demonic standards, you only need to punch to lower your tail/hook
on oppressor.
fix: You will now automatically punch chest if the target you are aiming
at is delimbed instead of doing nothing
/:cl:

---------

Co-authored-by: InsaneRed <prodexter31@outlook.comm>
Co-authored-by: Birdtalon <birdtalon@gmail.com>

---
## [pprmint/pprmint.art](https://github.com/pprmint/pprmint.art)@[615358cb08...](https://github.com/pprmint/pprmint.art/commit/615358cb08dacfd4e8dad82abdf792c69efef255)
#### Thursday 2023-12-21 20:29:00 by pprmint

Update packages and finally fix this fucking god damn title alignment because Apple is so fucking horny over adding blur behind shit that on shitty fucking Safari on iOS the bottom bar would cover parts of elements that were 100vh tall so now we had to include new fucking units just to accomodate for shitty things like this.
I hate WebKit too. Fuck you.

---
## [ROCmSoftwarePlatform/pytorch](https://github.com/ROCmSoftwarePlatform/pytorch)@[ddf1cb7870...](https://github.com/ROCmSoftwarePlatform/pytorch/commit/ddf1cb78705dcf79fe8c8df01f6f18ca4a218c55)
#### Thursday 2023-12-21 20:37:05 by voznesenskym

AOTAutograd: handle set_(), detect metadata mutations that cancel out (#111554)

This should be enough to get @voznesenskym 's FSDP branch to plumb `set_()` through AOTAutograd properly and have everything properly no-op out. Main changes are:

(1) graph break on `aten::set_.source_Tensor_storage_offset` (we could support it but it isn't needed, seems safer to graph break)

(2) Functionalization: add a "proper" functionalization kernel for `aten::set_.source_Tensor`. The previous one we had was codegen'd and it was wrong (it would just clone() and call set_(), which does not do the right thing). I also manually mark on the `FunctionalTensorWrapper` when a given tensor has been mutated by a `set_()` call.

(3) AOTAutograd: I added a new field, `InputAliasInfo.mutates_storage_metadata`, so we can distinguish between "regular" metadata mutations, and metadata mutations due to `set_()` calls. This is mainly because at runtime, one requires calling `as_strided_()` to fix up metadata, while the other requires calling `set_()`.

(4) Made AOTAutograd's detection for metadata mutations / set_() mutations smarter and detect no-ops (if the storage and metadata are all the same).

I also killed `was_updated()` and `was_metadata_updated()`, and replaced them with (existing) `has_data_mutation() ` and (new) `has_data_mutation()`, which can more accurately distinguish between data-mutation vs. `set_()` calls vs. metadata-mutation

**This PR is still silently correct in one case though**, which I'd like to discuss more. In particular, this example:
```
def f(x):
    x_view = x.view(-1)
    x.set_(torch.ones(2))
    x_view.mul_(2)
    return
```

If you have an input that experiences both a data-mutation **and** a `x_old.set_(x_new)` call, there are two cases:

(a) the data mutation happened on the storage of `x_new`. This case should be handled automatically: if x_new is a graph intermediate then we will functionalize the mutation. If x_new is a different graph input, then we will perform the usual `copy_()` on that other graph input

(b) the data mutation happened on the storage of `x_old`. This is more of a pain to handle, and doesn't currently work. At runtime, the right thing to do is probably something like:
```

def functionalized_f(x):
    x_view = x.view(-1)
    # set_() desugars into a no-op; later usages of x will use x_output
    x_output = torch.ones(2)
    # functionalize the mutation on x_view
    x_view_updated = x.mul(2)
    x_updated = x_view_updated.view(x.shape)
    # x experienced TWO TYPES of mutations; a data mutation and a metatadata mutation
    # We need to return both updated tensors in our graph
    return x_updated, x_output
def runtime_wrapper(x):
    x_data_mutation_result, x_set_mutation_result = compiled_graph(x)
    # First, perform the data mutation on x's old storage
    x.copy_(x_data_mutation_result)
    # Then, swap out the storage of x with the new storage
    x.set_(x_set_mutation_result)
```

There are two things that make this difficult to do though:

(1) Functionalization: the functionalization rule for `set_()` will fully throw away the old `FunctionalStorageImpl` on the graph input. So if there are any mutations to that `FunctionalStorageImpl` later on in the graph, the current graph input won't know about it. Maybe we can have a given `FunctionalTensorWrapper` remember all previous storages that it had, and track mutations on all of them - although this feels pretty complicated.

(2) AOTAutograd now needs to know that we might have *two* graph outputs that correspond to a single "mutated input", which is annoying.

It's worth pointing out that this issue is probably extremely unlikely for anyone to run into - can we just detect it and error? This feels slightly easier than solving it, although not significantly easier. We would still need `FunctionalTensorWrapper` to keep track of mutations on any of its "previous" storages, so it can report this info back to AOTAutograd so we can raise an error.

Pull Request resolved: https://github.com/pytorch/pytorch/pull/111554
Approved by: https://github.com/ezyang
ghstack dependencies: #113926

---
## [FrankitoBoar/Boar](https://github.com/FrankitoBoar/Boar)@[48b5a35dea...](https://github.com/FrankitoBoar/Boar/commit/48b5a35deadc1cdeb19d117ee50702c76df0d275)
#### Thursday 2023-12-21 20:59:52 by Bloop

[MISSED MIRRORS] Linters, part two (#25138)

* Split Run Linters step into multiple steps (#78265)

Splits the big "Run Linters" step into multiple steps. Also since all of
these steps are independent of eachother, I've made them all run
regardless of if the job is currently failing.

<details>
<summary>Proof of testing:</summary>

Fail in install tools, all linting steps are skipped:
https://github.com/distributivgesetz/tgstation/actions/runs/6151628214/job/16692089726
Fail in Run DreamChecker, other steps continue to run:
https://github.com/distributivgesetz/tgstation/actions/runs/6151664705/job/16692203569?pr=2
</details>

<details>
<summary>Pictured: me breaking CI for a day</summary>

https://github.com/tgstation/tgstation/assets/47710522/ea12ad30-2b69-4aa3-9642-7d0818eab2d1

</details>

Going through the Run Linters step has always been a slog. Finding an
error is like finding a needle in a haystack. Seeing what command
exactly went wrong is going to go a long way in helping people find out
which linters have failed.

nothing playerfacing

* Fixes TFE being useless after #78265 (#78433)

I thought `set +e` would still make the shell exit with an error if any
command failed, I didn't think that it would just use the exit code of
the last command. I am dumb, I'm an idiot and I want to cry.

* Update ci_suite.yml

* Fix some odd vscode highlighting errors in workflow files  (#78274)

few errors which were odd and annoying

stealing PRs from san7890, they wanted to do this
nothing playerfacing

* Only cancel concurrent CI in the same PR (#73398)

More merge queue bullshit. Cancels are counted as failures, and even
though on my test branch it worked completely fine, when trying on two
real PRs, it did not.

This makes it so merges into master might mess with CI clogging again,
but also merge queue is going to do that on its own, and the gain is
worth it.


![image](https://user-images.githubusercontent.com/35135081/218340666-6f937611-c47e-4122-b4b8-b84e8edcc1e9.png)

* Remove cache purge key that has never worked and has meant that our cache has never worked (#71529)

ci_suite.yml runs on your fork. This means you do not have access to
secrets. Every user has had the purge key of blank.

WE have it set to something. Which means the master cache that every PR
pulls from has been unable to match.

This means our cache has been at the max limit all this time, constantly
clearing out old caches, and never reusing any.

* Caches Node and Python Bootstrap for GH Actions (#78307)

## About The Pull Request

I was planning on doing this a lot earlier but ran into some weird
roadblocks, but this time I finally did the research and it's done
properly.

We do a lot of useless work on every single CI run, and in the interest
of saving the world's energy (by a matter of at least 10 seconds per my
testing), lets stop doing so much extra work by caching both the work we
do on the python bootstrap installation (we literally call it `cache`
for a reason) and the Node installation by sharing it between github
actions runners.

Here's a random CI run on master where you can see that the `Install
Tools` portion takes about 19 seconds -
https://github.com/tgstation/tgstation/actions/runs/6167104927/job/16737570519

Here's the CI run I was testing with where you can see we slim it down
to about 6 seconds for the `Install Tools` step, but with a second-or-so
taken to restore the cache since the runner needs to download+unzip the
cache. it tends to be shorter or longer by a second at times but i'm
certain this is just noise -
https://github.com/san7890/bruhstation/actions/runs/6167245722/job/16737919874

On average, we save about **10 seconds** a run on Run Linters, which is
meant to be the fastest CI step. Future improvements would lie in making
either maplint or the tgui test suite faster, but that would be a much
more complicated and code-intensive task. cache go weeeee

## Changelog

Nothing that concerns players.

* Conditionally run TGS tests (#73704)

Also add test merge support for pull requests

---------

Co-authored-by: distributivgesetz <distributivgesetz93@gmail.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>
Co-authored-by: Jordan Dominion <Cyberboss@users.noreply.github.com>

---
## [FrankitoBoar/Boar](https://github.com/FrankitoBoar/Boar)@[8f3d1036c8...](https://github.com/FrankitoBoar/Boar/commit/8f3d1036c8f4f7b51acc6bad8b28009a81e20ac4)
#### Thursday 2023-12-21 20:59:52 by SkyratBot

[MIRROR] Refactor icemoon wolves into basic mobs and add taming + pack behavior [MDB IGNORE] (#25126)

* Refactor icemoon wolves into basic mobs and add taming + pack behavior (#79736)

## About The Pull Request

Ports icemoon wolves over to the basic mob framework with a bit of extra
stuff:

- Wolves call for help when attacked within a decently large radius.
Because you know, pack animals.
- Wolves can now be tamed with a slab of meat
- When tamed, wolves can be ridden like goliath mounts. Ride wolf, life
good. Pretend you're playing ARK and start shivering to death in thatch
huts for that High Roleplay experience.
- Tamed wolves have access to a bunch of pet commands (following, point
fetching, point attacking, play dead, etc) and will also defend their
owners vehemently if they're attacked.

You can probably tame multiple if you wanted to.

## Why It's Good For The Game

What part about riding wolves isn't entertaining? I don't really play
/tg/ that much so I can't argue too much about the balance implications
this might pose, but it's undoubtedly a stupid little gimmick and is
likely to be used by bored assistants and miners with too much time on
their hands.

Especially robust individuals will probably find a million things to do
with a basic mob capable of fetching, attacking on command and generally
being able to defend themselves decently well.

## Changelog

:cl: yooriss
refactor: Icemoon wolves now use the basic mob framework and should act
more intelligently, defending their pack.
add: Icemoon wolves can be tamed with slabs of meat and can be ridden as
mounts once friendly. Being rather large dogs, they also have access to
most of the pet commands you'd expect, such as fetching things, and
violently mauling people their owners point at.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Refactor icemoon wolves into basic mobs and add taming + pack behavior

---------

Co-authored-by: Ephemeralis <Ephemeralis@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [FrankitoBoar/Boar](https://github.com/FrankitoBoar/Boar)@[17cba0dccf...](https://github.com/FrankitoBoar/Boar/commit/17cba0dccfb57eb492fcfade92abc0065a07b356)
#### Thursday 2023-12-21 20:59:52 by Bloop

[MISSED MIRROR] Puts all traits in the globalvars file + CI Testing (#79642) (#25131)

* Puts all traits in the globalvars file + CI Testing (#79642)

Fixes #76349

I didn't know that people needed to add any new traits to a global list
so they can be easily read in View Variables, and was pretty shocked to
find out many other people didn't know it was a thing. Let's make it a
thing by testing it using a new CI Python Linter to check this. But oh
no-

![image](https://github.com/tgstation/tgstation/assets/34697715/c093f1a8-00ce-40a6-8e1d-f344107ce7b8)

There were about 200+ missing traits. Alright, so let's do the
following:

* Move trait defines to their own dedicated folder in the `_DEFINES`
folder.
* Split up the traits mega-file into different files, for better
organization. One for the macros, one for the sources, and a few for the
"trait declarations"
* Run the linter a load of times and add everything to the globalvars
file, removing anything that's no longer used and figuring out where the
best categorization of it is. also minor code improvements. also rename
all of the ones that look weird. also fix list indentations
* Also alphabetize the lists because it's easy
* Move everything to a new `traits_by_type` list, while keeping the
admin one the way it is for the time being while we figure out a better
way to show that list to admins.
* Profit

Mapping trait injectors will now work for any type of trait. You
shouldn't add any trait via this injector though, but you're no longer
limited to coders remembering to add it to that critical list you
needed.

Lays the framework for a better view variables experience. This work is
too lengthy to presently do, but hopefully we can get this done sooner
rather than later. we will need a code-accessible way to view these
traits for such a framework to be implemented, so let's just do that.

Future steps are to break down the mega-declarations file into a folder
full of separate files by typepath, but that requires a lot of auditing.
Does need to happen one day though, there's a lot of mob traits mingled
with datum traits and auuugh we gotta do this later this PR is already
massive.

there's probably ways to game this but this catches _my_ mistakes so
good luck to everyone else (it should work for 99% of everyone)

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).

* Update tgstation.dme

* Update _traits.dm

* Comment these out for now

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [FrankitoBoar/Boar](https://github.com/FrankitoBoar/Boar)@[67ddf1507c...](https://github.com/FrankitoBoar/Boar/commit/67ddf1507c8663c4b8f006ed8c763ca372e5fc29)
#### Thursday 2023-12-21 20:59:52 by SkyratBot

[MIRROR] Make sign language unaffected by the Social Anxiety quirk's direct speech effects [MDB IGNORE] (#25140)

* Make sign language unaffected by the Social Anxiety quirk's direct speech effects (#79809)

## About The Pull Request

Alternative title: "Make going non-verbal make you less anxious."

This is a two line change to `social_anxiety.dm` to quit out its
`handle_speech` method when user has the `TRAIT_SIGN_LANG` trait.
This stops the Social Anxiety quirk from applying its
stutters/fillers/blockers for as long as the speaker is using sign
language.
This does nothing to any of social anxiety's non-verbal effects, those
are still active regardless and entirely unaffected.
## Why It's Good For The Game

Primarily: I think giving people the choice between using anxious talk
or sign language, and thus the different hurdles inherent to both, makes
for a more interesting gameplay interaction than simply blanket-applying
the quirk's speech effects to both.

Secondarily: Social Anxiety's non-verbal penalties are entirely
unaffected. One will still get the penalties from making eye contact and
occasionally make eye contact with objects. Notably this includes the
stuttering making eye contact could get you, which still makes your
signing shaky. You're still anxious, after all.
On top of this, it still costs more to pick up Signer than Social
Anxiety allows for, and thus the change doesn't simply make the
combination free points.

Tertiarily: when one has trouble speaking verbally, non-verbal
communication can be helpful in overcoming that hurdle. This is
especially so when the trigger for said anxiety is speaking verbally in
the first place. This is part of why I was so enamoured by the
combination before a broader and, mind you, fairly needed fix to sign
language made these interact differently.
## Changelog
:cl:
balance: signers no longer suffer from social anxiety's speech changes
when they go non-verbal. Other effects are maintained.
/:cl:

* Make sign language unaffected by the Social Anxiety quirk's direct speech effects

---------

Co-authored-by: _0Steven <42909981+00-Steven@users.noreply.github.com>

---
## [MPhonks/cmss13](https://github.com/MPhonks/cmss13)@[825d7ddc87...](https://github.com/MPhonks/cmss13/commit/825d7ddc87d08d107611f3df6ac71597ae8e711c)
#### Thursday 2023-12-21 21:47:09 by HumiliatedGoblin

Makes Dropship Pilot Two Dropship Crew Chief hours, instead of Five Marine squad hours. (#4488)

# About the pull request

### Changes the hours from five marine hours to *two* DCC hours,
something that should've been done years ago.

# Explain why it's good for the game

I'm **SICK** and **TIRED** of TROGLADYTE dropship pilots who don't even
ATTEMPT to read the guide, and think they're the coolest person ever
after direct firing without a laser detector, wiping the front with six
minis, and they don't even have the GAL
to apologize afterwards. I want this to END.

It's honestly comical how terrible pilots have gotten, so much so that I
refuse to call them in unless they have a silver medal or above. It
makes absolutely no sense how pilots only need five hours as a marine to
have the power to kill fifteen marines with one napalm. By making it two
DCC hours, you give them a chance to learn how to fly, and also get tips
from experienced pilots.

I honestly believe that the reason marine winrate is so low is because
of the sheer incompetence shown by command slots and fire support-ists,
and by making the hours needed higher, HOPEFULLY marines can actually
use fire support without fear of the person faltering and killing
everyone.

I was thinking of having Two Fireteam Leader hours as well, but because
of the moving away of RTO's, I didn't think it was necessary and
would've been overkill. Might be something to consider though.

was brought upon by this screenshot:

https://media.discordapp.net/attachments/604397850675380234/1155395437256249354/image_4.png

# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>



</details>


# Changelog
:cl: bostonthebear
add: Changes pilot officer timelock from 5 hours as squad marine to 2
hours as DCC
/:cl:

---
## [WarlockD/tgstation](https://github.com/WarlockD/tgstation)@[b8fc9b367e...](https://github.com/WarlockD/tgstation/commit/b8fc9b367ebb26def792a68bcb25294e518698d8)
#### Thursday 2023-12-21 22:20:33 by LemonInTheDark

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
## [ubccsss/ubccsss.org](https://github.com/ubccsss/ubccsss.org)@[b4b923ea72...](https://github.com/ubccsss/ubccsss.org/commit/b4b923ea721c5a6a06c73669a1698a558200c0d4)
#### Thursday 2023-12-21 22:24:06 by csssbot

New review for CPSC 213 by ushankab (#559)

> A friend described this course as a “religious experience”. Surely a
joke, but 213 is definitely an experience. Probably the hardest CPSC
I’ve ever taken. I spent hours upon hours reviewing slide decks and
grinding practice problems and exams for this course. I left most
lectures feeling confused and would have to spend at least an hour if
not more going over things to “unconfuse” myself. However, this is also
one of the most satisfying courses I ever taken. Every unit and topic
covered is extremely interesting imo. In particular, the final unit on
concurrency is one of my favourite units of any CPSC course. I enjoyed
cracking open what is a black box to most people and taking a look at
the internals. I also feel knowing some of these internals has improved
my ability to use computers to solve problems. The assignments are all
great. However, the last assignments (for the concurrency unit) are a
significant step up in difficulty. The tests in this class are hard but
if you put in work things should work out fine in the end (likely due to
some scaling magic).
>
> Difficulty: 4/5
> Quality: 4/5
> <cite><a href=''>ushankab</a>, Dec 17 2023, course taken during
2021W2</cite>
<details><summary>View YAML for new review</summary>
<pre>
  - author: ushankab
    authorLink: 
    date: 2023-12-17
    review: |
A friend described this course as a “religious experience”. Surely a
joke, but 213 is definitely an experience. Probably the hardest CPSC
I’ve ever taken. I spent hours upon hours reviewing slide decks and
grinding practice problems and exams for this course. I left most
lectures feeling confused and would have to spend at least an hour if
not more going over things to “unconfuse” myself. However, this is also
one of the most satisfying courses I ever taken. Every unit and topic
covered is extremely interesting imo. In particular, the final unit on
concurrency is one of my favourite units of any CPSC course. I enjoyed
cracking open what is a black box to most people and taking a look at
the internals. I also feel knowing some of these internals has improved
my ability to use computers to solve problems. The assignments are all
great. However, the last assignments (for the concurrency unit) are a
significant step up in difficulty. The tests in this class are hard but
if you put in work things should work out fine in the end (likely due to
some scaling magic).
    difficulty: 4
    quality: 4
    sessionTaken: 2021W2

<pre>
</details>This is an auto-generated PR made using:
https://github.com/ubccsss/course-review-worker

---
## [ubccsss/ubccsss.org](https://github.com/ubccsss/ubccsss.org)@[c758cdb798...](https://github.com/ubccsss/ubccsss.org/commit/c758cdb79872b7176208cf30a26f21901933c374)
#### Thursday 2023-12-21 22:24:30 by csssbot

New review for CPSC 430 by ushankab (#560)

> Not a great course, but a decent one overall. Gives lots of practice
reading and writing argumentative essays. If that doesn’t sound like
something you want to do, then this might not be the course for you. The
textbook and lectures can be a little dry at times. However, the
lectures also have a significant amount of participation and discussion
which is a highlight of the course. People often had interesting things
to say and points to make. Weekly essays are graded using peer review.
Some may worry about this but I found the reviews to be quite fair and
reasonable. See the syllabus for details on how exactly peer review
works and how it is set up to try incentivize reasonable and fair peer
reviews. I did find the course to be run in a bit of a disorganized and
haphazard way compare to other CPSC courses. To be fair CPSC courses are
almost always very well organized so that’s a high bar to meet. Also the
bulk of tests comes from writing an argumentative essay (two for the
final). However, writing good argumentative essays under artificial time
constraints seems a bit silly in my view. It’s a bit like asking someone
to code up a complex program. You don’t ask someone to do this on an
exam because it’s simply not feasible under tight time constraints. But
they need some way to assess that the learning outcomes are being met so
I guess these sorts of tests may be a necessary evil in this class.
>
> Difficulty: 2/5
> Quality: 3.5/5
> <cite><a href=''>ushankab</a>, Dec 17 2023, course taken during
2023W1</cite>
<details><summary>View YAML for new review</summary>
<pre>
  - author: ushankab
    authorLink: 
    date: 2023-12-17
    review: |
Not a great course, but a decent one overall. Gives lots of practice
reading and writing argumentative essays. If that doesn’t sound like
something you want to do, then this might not be the course for you. The
textbook and lectures can be a little dry at times. However, the
lectures also have a significant amount of participation and discussion
which is a highlight of the course. People often had interesting things
to say and points to make. Weekly essays are graded using peer review.
Some may worry about this but I found the reviews to be quite fair and
reasonable. See the syllabus for details on how exactly peer review
works and how it is set up to try incentivize reasonable and fair peer
reviews. I did find the course to be run in a bit of a disorganized and
haphazard way compare to other CPSC courses. To be fair CPSC courses are
almost always very well organized so that’s a high bar to meet. Also the
bulk of tests comes from writing an argumentative essay (two for the
final). However, writing good argumentative essays under artificial time
constraints seems a bit silly in my view. It’s a bit like asking someone
to code up a complex program. You don’t ask someone to do this on an
exam because it’s simply not feasible under tight time constraints. But
they need some way to assess that the learning outcomes are being met so
I guess these sorts of tests may be a necessary evil in this class.
    difficulty: 2
    quality: 3.5
    sessionTaken: 2023W1

<pre>
</details>This is an auto-generated PR made using:
https://github.com/ubccsss/course-review-worker

---
## [TheUnholyWrath/oaa](https://github.com/TheUnholyWrath/oaa)@[fed0e74065...](https://github.com/TheUnholyWrath/oaa/commit/fed0e740659c26863f5ab19d182e23bc3e4d4297)
#### Thursday 2023-12-21 23:21:49 by TheUnholyWrath

7.35 (OAA version)

[* 7.35 parity](https://www.dota2.com/patches/7.35)

* ITEMS:
Blade of Judecca cooldown reduced from 25 to 20 seconds.
Blood Core now also provides 50/60/70/80/90 bonus aoe.
Blood Core passive spell lifesteal against creeps reduced from 6/7/8/9/10% to 6/6.5/7/7.5/8%.
Bloodstone bonus aoe reduced from 75 to 50.
Bloodstone spell lifesteal reduced from 30% to 28%.
Butterfly provides 15 attack speed + 20% Agility Attack Speed (0.2 bonus attack speed per 1 AGI) instead of 20% Base Attack Speed.
Craggy Coat duration increased from 5 to 8 seconds.
Dagger of Moriah and Stoneskin Armor now inherit stats from Shiva's Guard.
Divine Rapier bonus spell amp increased from 25% to 35%.
Divine Rapier recipe gold cost reduced from 40000 to 30000.
Divine Shards (component for Divine Rapier) core point cost increased from 30 to 40.
Ethereal Blade provides the same cast range as Far Sight. Doesn't stack.
Far Sight bonus mana regen increased by 0.5 at all levels.
Far Sight now has Chain Mail in the recipe instead of Diadem.
Far Sight now provides 4/5/7/10/14 armor.
Ghost King Bar now has Headdress in the recipe.
Ghost King Bar recipe gold cost reduced from 250 to 0.
Heart of Tarrasque now has Vitality Booster and Ring of Tarrasque in the recipe.
Heart of Tarrasque recipe gold cost reduced from 1300 to 0.
Heart of Tarrasque still provides health.
Pipe of Insight bonus hp regen unchanged.
Pipe of Insight recipe cost reduced from 700 to 200.
Revenant's Brooch is now a tier 4 item.
Scythe of Vyse cooldown reduced from 25 to 20 seconds.
Stoneskin Armor bonus status resist reduced from 22/24% to 20/22%.

* HEROES:
Abaddon Borrowed Time Immolation talent dps increased from 95 to 100.
Beastmaster boar hp increased from 300/600/900/1200/2400/4800 to 450/750/1050/1350/2700/5400.
Bounty Hunter Jinada damage reduced at OAA levels from 360/540 to 260/340.
Bounty Hunter Jinada gold steal reduced from 45/70/100/150/300/600 to 36/60/84/108/216/432.
Crystal Maiden Arcane Aura global bonus mana regen reduced from 0.5/1/1.5/2/3/4 to 0.5/0.75/1/1.25/1.75/2.5 (proximity and self mana regen adjusted accordingly).
Dazzle Bad Juju armor reduction per cast improved from 1/2/3/4/5 to 1/3/5/7/9.
Dazzle Bad Juju health cost rescaled from 75 + 100% increase per cast to 50/75/100/125/150 + 75% increase per cast.
Disruptor Static Storm radius reduced from 500 to 450.
Dragon Knight Level 25 Talent +80 Attack Speed changed to +400 Breathe Fire Damage.
Ember Spirit Level 20 Talent +150 Sleight of Fist damage reduced to +110.
Juggernaut Blade Fury damage per tick increased from 35/40/45/50 to 40/45/50/55/70/85.
Kunkka Torrent cooldown increased at OAA levels from 9/8 to 10 seconds.
Kunkka Torrent slow duration reduced at OAA levels from 5/6 to 4 seconds.
Leshrac Level 10 Talent +40 Split Earth Radius reduced to +25.
OD Arcane Orb splash radius reduced from 300 to 250.
Pangolier Shield Crash damage increased from 70/140/210/280/560/1120 to 75/150/225/300/600/1200.
Phantom Assassin base agility and agility gain increased from 21+3.2 to 23+3.4
Phantom Assassin base strength and strength gain increased from 19+2.0 to 21+2.2
Puck Illusory Orb damage increased at early levels from 75/150/225/300 to 90/160/230/300.
QoP Level 10 talent +16 Strength unchanged.
QoP Level 15 talent +60 Attack Speed reduced to +30.
QoP Level 15 talent +60 Shadow Strike Heal Per Tick changed to +40 Shadow Strike Damage & Heal Per Tick.
Sand King Caustic Finale radius reduced from 800 to 700.
Spectre Desolate damage reduced at OAA levels from 120/180 to 86/112.
Tinkerer Keen Contraption aoe reduced from 350 to 325.
Underlord Dark Abduction aoe reduced from 450 to 430.
Underlord Dark Rift aoe reduced from 430 to 425.
Windranger Level 25 Talent +2 Shackleshot Target changed to +470 Powershot Damage. (other talents are now the same as vanilla)
Windranger scepter Windrun bonus spell amp increased from 35% to 45%.

* OTHER:
Update guides based on item changes
Fixed some guides missing Heart, Aeon Disk and Dagger of Moriah.
Finally changed game version to 7.35

---------

Co-authored-by: Darko V <darko1290@gmail.com>

---

