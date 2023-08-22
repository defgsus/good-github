## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-21](docs/good-messages/2023/2023-08-21.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,237,354 were push events containing 3,371,537 commit messages that amount to 262,229,783 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 59 messages:


## [Dmeto/tgstation](https://github.com/Dmeto/tgstation)@[63d6c2e962...](https://github.com/Dmeto/tgstation/commit/63d6c2e9628be7af04948f59488043f109f1faab)
#### Monday 2023-08-21 00:22:21 by CRITAWAKETS

Adds in the smoothbore disablers. (#76773)

## About The Pull Request

This PR adds in a craftable smoothbore disabler, a pistol companion to
the lethal laser musket. Unlike the musket, it fires a disabler shot.
Singular. Weak in armor too. After you fire it, you've gotta crank it,
but only one crank.

The good thing about it is that you can simply add more smoothbores to
your inventory, and use 4 of them to take down a target.

The bad thing is that it's a smoothbore (which for an energy weapon,
means no lens is installed). It has 22.5 degrees of inaccuracy. Have
fun.

Militia Men start with a holster containing two of these, fitting with
their equipment. But of course, the Militia General has an upgraded
laser musket, so... He needs a better smoothbore too.

**INTRODUCING THE ELITE SMOOTHBORE DISABLER**
Using ANCIENT TECHNOLOGIES and PURE BLING, you can fire TWO shots, not
be weak against armour AND have actual accuracy (and a +5 damage boost
because i figured why the hell not). This is the strongest upgraded
variant of the shitty maint guns, so the tome to craft it is currently
unavailable. I want someone to figure out a creative way to put it
somewhere that isn't just a random spawn in maintenance.


![image](https://github.com/tgstation/tgstation/assets/13697285/02c396b8-4b72-45f8-b471-a006df132aff)

The Militia General only has one elite smoothbore. It's too rare and
powerful to simply have two. Even though a regular disabler is better in
every way.

Smoothbore Disabler Recipe:
1x Weapon Stock
5x Cable Coil
1x Pipe
1x Micro-Laser
1x Power Cell
1x Mouse Trap
Needs: Screwdriver, Wrench. Takes 10 seconds to make.

Elite Smoothbore Disabler Recipe:
1x Smoothbore Disabler
5x Gold Ingots/Sheets
1x Hyper-Capacity Power Cell
10u Tempomyocin
Needs: Screwdriver. Takes 20 seconds to make.
Recipe requires recipe book.

## Why It's Good For The Game

Having a sidearm to go with your laser musket is neat, alongside the
fact that it just allows following up on someone. I don't have much to
say honestly, I just think it's neat. Also the idea of an assistant
going FULL BLACKBEARD, carrying 4 pistols and having to toss them away
in order to shoot again cracks me up.

Oh and this is the part for coders: I've de-spaghettified some code with
the maint gun recipe granters, and the gun crank is now a component.
It's likely you could use it on any item that sends the proper signal,
so I kind of overbuilt it on purpose.

Also the attack_self on guns now returns parent. This should allow it to
send a signal alongside putting your grubby fingerprints on the weapon
when you switch modes. There could be bugs but they should be easy to
fix if they pop up, mode switching on guns works without a fuss.

## Changelog

:cl:
add: Added the smoothbore disabler and it's prime variant. You can now
craft a disabler with only one shot and terrible accuracy.
code: Gun cranking has been made a component and could theoretically be
used on more than guns.
/:cl:

---
## [Dmeto/tgstation](https://github.com/Dmeto/tgstation)@[a8e0d7c8d2...](https://github.com/Dmeto/tgstation/commit/a8e0d7c8d202027d36c96391ed9a43cb5d708065)
#### Monday 2023-08-21 00:22:21 by MrMelbert

Adds a new positive quirk, "Spacer Born".  (#76809)

## About The Pull Request

Adds a new 7 point positive quirk, "Spacer Born". Totally not inspired
by The Expanse, don't look at the branch name.

You were born in space, rather than on a planet, so your physiology has
adapted differently.
You are more comfortable in space, and way less comfortable on a planet.

Benefits:
   - You are slightly taller. (No mechanical effect)
   - You take 20% less damage from pressure damage.
   - You take 20% less damage from cold environments. 
- You move 10% faster while floating (NOT drifting, this is zero gravity
movement while beside a wall).
- You drift 20% faster (Drifting through zero gravity, untethered to
anything)
- While in space (z-level-wise, not turf wise), you lose some disgust
overtime.
- While experiencing no-gravity for an extended period of time, you will
start regenerating stamina and reduce stuns at a very low rate.
- If you are assigned to shaft miner (or the map is Icebox), you are
awarded with a 25% wage bonus (hazard pay).

Downsides:
- While on a planet (Yes, this includes Icebox and planetary maps), you
gain gravity sickness:
- Passive accrue disgust (slightly lessened on Icebox) (Capped at low
levels)
      - Choking, after extended periods (disabled on Icebox)
      - Slower movement 
      - Weaker stamina (disabled on Icebox)
- Suffocation from extended periods (disabled on Icebox) (Lungs aren't
adapted)
      - Mood debuff

(Effects not final)

## Why It's Good For The Game

I'd figure I throw my hat in with the Positive Quirk Curse. 

This is a quirk that improves your ability in a niche circumstance (low
gravity / dangerous pressure), with some downsides that are only
generally in effect if you play a few roles (or it's Icebox).

Because of this I think it'll provide an interesting niche, where Spacer
Born engineers are slightly better than their counterparts due to their
origin (moving faster in space without a jetpack, withstanding
pressure). However, at the same time, if the mining outpost sustains
damage and needs repairs... suddenly your buff over your cohorts
disappears, and you have to brave somewhere hostile to your body.

Ultimately, the goal of the quirk is to encourage people to approach
situations a bit differently.
Or take it as a challenge and play shaft miner. 

## Changelog

:cl: Melbert
add: Adds a new 7 point positive quirk, "Spacer Born". You were born in
space, and as a result your body's adapted to life in artificial
gravity, making you much more effective and comfortable in lower
gravity. However, travelling planet-side is quite a chore, especially if
you're assigned to work there.
add: Adds a chemical: Ondansetron, created by Oil + Nitrogen + Oxygen +
Ethanol catalyst. A powerful Antiemetic (lowers disgust).
/:cl:

---
## [zydras/Skyrat-tg](https://github.com/zydras/Skyrat-tg)@[a0a9a43562...](https://github.com/zydras/Skyrat-tg/commit/a0a9a435625f5b89b78394550b5b7b570a3729b4)
#### Monday 2023-08-21 00:25:14 by SkyratBot

[MIRROR] Refactors Regal Rats into Basic Mobs (more titles edition) [MDB IGNORE] (#23188)

* Refactors Regal Rats into Basic Mobs (more titles edition) (#77681)

## About The Pull Request

I literally can't focus on anything nowadays, so I just did this to
break a never-ending chain of distress. Anyways, regal rats! These
fellas are mostly player controlled, but did have _some_ AI capabilities
(mainly tied to their actions), so that was incorporated too. Everything
should work as-expected (as well as look a shitload cleaner).

Instead of doing weird and awful conditional signals being sent out, I
made the `COMSIG_REGAL_RAT_INTERACT` (not the actual name) have a return
value so we can always rely on that working whenever we have that signal
registered on something we attack. I also cleaned up pretty much every
proc related to regal rats, gave them AIs to reflect their kingly nature
(and action capabilities (as well as move the action to
`mob_cooldown`)).

Since I thought they needed it, Regal Rats now get a special moniker!
This is stuff like "the Big Cheese" and what-not, like actual regents in
history. That's nice.
## Why It's Good For The Game

Two more off the list. Much better code to read. Way smarter rats with
spawning their army as part of a retaliatory assault (war). More sovl
with better regal rat names. The list goes on.
## Changelog
:cl:
refactor: Regal Rats have been refactored into basic mobs. They should
be a bit smarter and retain their docility (until attacked, in which
case you should prepare to get rekt by summoned rats), and properly flee
when they can instead of just sit there as you beat them to death. The
framework for them interacting with stuff (i.e. opening doors while
slobbering on food) is a bit more unified too, now. They also have
cooler names too!
/:cl:

FYI: Beyond a few code touchups, I haven't touched the actions at all. I
do not believe myself to be enthusiastic about fixing anything involving
the actions code as of this moment so that this PR is more overbloated
unless it's unbelievably stupid or easy to fix.

* Refactors Regal Rats into Basic Mobs (more titles edition)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[3c083fbf19...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/3c083fbf197dca0adabd3c85659e68ac8fbb1367)
#### Monday 2023-08-21 00:40:48 by DaydreamIQ

Buffs Heretic ash ascension (#77618)

## About The Pull Request

Post-Ascension the Nightwatchers Rebirth (Or Fiery Rebirth) has its
cooldown lowered from 60 seconds to 10
Additionally adds bomb immunity to the list of resistances that
ascension provides

## Why It's Good For The Game

Ash ascension kind of sucks when compared to its big brothers flesh,
rust and blade. You do get a couple of cool spells but their impact is
negated by how shitty fire damage is and while you get a ton of
resistances, you don't get stun immunity and have absolutely zero
sustainability in long-term engagements.

Blade has its lifesteal, rust has its leeching walk and flesh has a big
worm that eats arms. And while the laziest solution would be to give ash
stun immunity like those three I think it'd be more fitting if it could
capitalize on one of its more powerful spells. Keeping in the fight by
siphoning health from all those people you lit on fire with your cascade
instead of watching in pain as they completely negate any threat you
have with a fire extinguisher and temp adapt.

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[f78dd2d42f...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/f78dd2d42f0cd79b6e089317ba45514157aea583)
#### Monday 2023-08-21 00:40:48 by san7890

Fixes Ticked File Enforcement and Missing Unit Test (and makes said Unit Test Compile) (and genericizes the C&D list to the base unit test datum) (#77632)

Closes #77631

## About The Pull Request

Hey there,

Ticked File Enforcement simply wasn't catching files that were missed.
That's a bit stupid, so I decided to look into what the issue might be,
and whoopsie daisies I did double periods back in #76592
(020ac2405308eab83f314282499dfe777aba5874).

![image](https://github.com/tgstation/tgstation/assets/34697715/6023afe8-313d-4550-9a60-58a8bc211b4f)

I also added some debug info and some more checks to prevent such a
break from happening again on runtime of this script. I thought it was a
weird string concatenation issue (and not the simple break I thought it
was), so I rewrote how it adds `glob`s. I think it's cleaner so I'll
keep it anyhow

This PR also corrects the oversight of the missing unit test (introduced
in #77218 (69827604c46952dd4393db8617cd494ade17bea2)) by reticking it in
the `_unit_tests.dm` file, and also makes it compile because it didn't
do that.

I also then had to do some more work to get the unit test to work.
* Genericizes the Create-and-Destroy "ignore" list to be a static list
on `/datum/unit_test` to allow it to be shared between these types of
tests that we need to test.
* Adds that list to C&D and the broken unit test regarding fantasy
bonuses
* Fixes some actually broken that the unit test was made to catch (beam
rifles, butterdogs and other slippery items, random ingredient boxes).
* Adds cases for things that the unit test and overall framework really
shouldn't be altering anyways (mythril), and was likely causing
inappropriate stack traces on master

## Why It's Good For The Game

Unit Tests WORK. Tools WORK.


![image](https://github.com/tgstation/tgstation/assets/34697715/9a59c0db-7a33-4546-918b-c73372a5b867)


## Changelog

:cl:
fix: Beam rifles will no longer inappropriately retain any bonuses they
may gain from wizardry.
fix: Inappropriate stack traces over bonuses being applied to components
that gain bonuses innately (like Mythril stacks) should cease.
/:cl:

---
## [sailfishos-mirror/vim](https://github.com/sailfishos-mirror/vim)@[c13b3d1350...](https://github.com/sailfishos-mirror/vim/commit/c13b3d1350b60b94fe87f0761ea31c0e7fb6ebf3)
#### Monday 2023-08-21 01:21:34 by Yee Cheng Chin

patch 9.0.1776: No support for stable Python 3 ABI

Problem:  No support for stable Python 3 ABI
Solution: Support Python 3 stable ABI

Commits:
1) Support Python 3 stable ABI to allow mixed version interoperatbility

Vim currently supports embedding Python for use with plugins, and the
"dynamic" linking option allows the user to specify a locally installed
version of Python by setting `pythonthreedll`. However, one caveat is
that the Python 3 libs are not binary compatible across minor versions,
and mixing versions can potentially be dangerous (e.g. let's say Vim was
linked against the Python 3.10 SDK, but the user sets `pythonthreedll`
to a 3.11 lib). Usually, nothing bad happens, but in theory this could
lead to crashes, memory corruption, and other unpredictable behaviors.
It's also difficult for the user to tell something is wrong because Vim
has no way of reporting what Python 3 version Vim was linked with.

For Vim installed via a package manager, this usually isn't an issue
because all the dependencies would already be figured out. For prebuilt
Vim binaries like MacVim (my motivation for working on this), AppImage,
and Win32 installer this could potentially be an issue as usually a
single binary is distributed. This is more tricky when a new Python
version is released, as there's a chicken-and-egg issue with deciding
what Python version to build against and hard to keep in sync when a new
Python version just drops and we have a mix of users of different Python
versions, and a user just blindly upgrading to a new Python could lead to
bad interactions with Vim.

Python 3 does have a solution for this problem: stable ABI / limited API
(see https://docs.python.org/3/c-api/stable.html). The C SDK limits the
API to a set of functions that are promised to be stable across
versions. This pull request adds an ifdef config that allows us to turn
it on when building Vim. Vim binaries built with this option should be
safe to freely link with any Python 3 libraies without having the
constraint of having to use the same minor version.

Note: Python 2 has no such concept and this doesn't change how Python 2
integration works (not that there is going to be a new version of Python
2 that would cause compatibility issues in the future anyway).

---

Technical details:
======

The stable ABI can be accessed when we compile with the Python 3 limited
API (by defining `Py_LIMITED_API`). The Python 3 code (in `if_python3.c`
and `if_py_both.h`) would now handle this and switch to limited API
mode. Without it set, Vim will still use the full API as before so this
is an opt-in change.

The main difference is that `PyType_Object` is now an opaque struct that
we can't directly create "static types" out of, and we have to create
type objects as "heap types" instead. This is because the struct is not
stable and changes from version to version (e.g. 3.8 added a
`tp_vectorcall` field to it). I had to change all the types to be
allocated on the heap instead with just a pointer to them.

Other functions are also simply missing in limited API, or they are
introduced too late (e.g. `PyUnicode_AsUTF8AndSize` in 3.10) to it that
we need some other ways to do the same thing, so I had to abstract a few
things into macros, and sometimes re-implement functions like
`PyObject_NEW`.

One caveat is that in limited API, `OutputType` (used for replacing
`sys.stdout`) no longer inherits from `PyStdPrinter_Type` which I don't
think has any real issue other than minor differences in how they
convert to a string and missing a couple functions like `mode()` and
`fileno()`.

Also fixed an existing bug where `tp_basicsize` was set incorrectly for
`BufferObject`, `TabListObject, `WinListObject`.

Technically, there could be a small performance drop, there is a little
more indirection with accessing type objects, and some APIs like
`PyUnicode_AsUTF8AndSize` are missing, but in practice I didn't see any
difference, and any well-written Python plugin should try to avoid
excessing callbacks to the `vim` module in Python anyway.

I only tested limited API mode down to Python 3.7, which seemes to
compile and work fine. I haven't tried earlier Python versions.

2) Fix PyIter_Check on older Python vers / type##Ptr unused warning

For PyIter_Check, older versions exposed them as either macros (used in
full API), or a function (for use in limited API). A previous change
exposed PyIter_Check to the dynamic build because Python just moved it
to function-only in 3.10 anyway. Because of that, just make sure we
always grab the function in dynamic builds in earlier versions since
that's what Python eventually did anyway.

3) Move Py_LIMITED_API define to configure script

Can now use --with-python-stable-abi flag to customize what stable ABI
version to target. Can also use an env var to do so as well.

4) Show +python/dyn-stable in :version, and allow has() feature query

Not sure if the "/dyn-stable" suffix would break things, or whether we
should do it another way. Or just don't show it in version and rely on
has() feature checking.

5) Documentation first draft. Still need to implement v:python3_version

6) Fix PyIter_Check build breaks when compiling against Python 3.8

7) Add CI coverage stable ABI on Linux/Windows / make configurable on Windows

This adds configurable options for Windows make files (both MinGW and
MSVC). CI will also now exercise both traditional full API and stable
ABI for Linux and Windows in the matrix for coverage.

Also added a "dynamic" option to Linux matrix as a drive-by change to
make other scripting languages like Ruby / Perl testable under both
static and dynamic builds.

8) Fix inaccuracy in Windows docs

Python's own docs are confusing but you don't actually want to use
`python3.dll` for the dynamic linkage.

9) Add generated autoconf file

10) Add v:python3_version support

This variable indicates the version of Python3 that Vim was built
against (PY_VERSION_HEX), and will be useful to check whether the Python
library you are loading in dynamically actually fits it. When built with
stable ABI, it will be the limited ABI version instead
(`Py_LIMITED_API`), which indicates the minimum version of Python 3 the
user should have, rather than the exact match. When stable ABI is used,
we won't be exposing PY_VERSION_HEX in this var because it just doesn't
seem necessary to do so (the whole point of stable ABI is the promise
that it will work across versions), and I don't want to confuse the user
with too many variables.

Also, cleaned up some documentation, and added help tags.

11) Fix Python 3.7 compat issues

Fix a couple issues when using limited API < 3.8

- Crash on exit: In Python 3.7, if a heap-allocated type is destroyed
  before all instances are, it would cause a crash later. This happens
  when we destroyed `OptionsType` before calling `Py_Finalize` when
  using the limited API. To make it worse, later versions changed the
  semantics and now each instance has a strong reference to its own type
  and the recommendation has changed to have each instance de-ref its
  own type and have its type in GC traversal. To avoid dealing with
  these cross-version variations, we just don't free the heap type. They
  are static types in non-limited-API anyway and are designed to last
  through the entirety of the app, and we also don't restart the Python
  runtime and therefore do not need it to have absolutely 0 leaks.

  See:
  - https://docs.python.org/3/whatsnew/3.8.html#changes-in-the-c-api
  - https://docs.python.org/3/whatsnew/3.9.html#changes-in-the-c-api

- PyIter_Check: This function is not provided in limited APIs older than
  3.8. Previously I was trying to mock it out using manual
  PyType_GetSlot() but it was brittle and also does not actually work
  properly for static types (it will generate a Python error). Just
  return false. It does mean using limited API < 3.8 is not recommended
  as you lose the functionality to handle iterators, but from playing
  with plugins I couldn't find it to be an issue.

- Fix loading of PyIter_Check so it will be done when limited API < 3.8.
  Otherwise loading a 3.7 Python lib will fail even if limited API was
  specified to use it.

12) Make sure to only load `PyUnicode_AsUTF8AndSize` in needed in limited API

We don't use this function unless limited API >= 3.10, but we were
loading it regardless. Usually it's ok in Unix-like systems where Python
just has a single lib that we load from, but in Windows where there is a
separate python3.dll this would not work as the symbol would not have
been exposed in this more limited DLL file. This makes it much clearer
under what condition is this function needed.

closes: #12032

Signed-off-by: Christian Brabandt <cb@256bit.org>
Co-authored-by: Yee Cheng Chin <ychin.git@gmail.com>

---
## [wayfarershaven/server](https://github.com/wayfarershaven/server)@[262abca24c...](https://github.com/wayfarershaven/server/commit/262abca24ccb19d91bf90a139f3221ac5da479df)
#### Monday 2023-08-21 02:13:11 by Trust

{EQEmu PR 3551} [Combat Messages] Fix issue where pet proc damage was not showing up

Kinglykrab reported a problem from his server where some pet damage from spells was being missed by observers.

While I think pet damage isn't seen by others on live, as there is no others-pet-filters, this was always a part of eqemu and many parsers used it.

The bug came from my PR back in 2022: https://github.com/EQEmu/Server/pull/2170/files

That PR removed many duplicate messages and added missing color messages, but omitted the ones this PR fixes.

New output as seen by owner of pet that is procing:

[Fri Aug 18 14:11:03 2023] Bristlebanes Warder begins to cast a spell. (Spirit of Scorpion Strike)
[Fri Aug 18 14:11:03 2023] Bristlebanes Warder strikes Kizdean Gix for 92 points of damage.
[Fri Aug 18 14:11:03 2023] Kizdean Gix spasms as the spirit of a scorpion rips through their body .

New output as seen by close observers:

[Fri Aug 18 14:11:09 2023] Bristlebanes Warder begins to cast a spell. (Spirit of Scorpion Strike)
[Fri Aug 18 14:11:09 2023] Bristlebanes Warder strikes Kizdean Gix for 92 points of damage.
[Fri Aug 18 14:11:09 2023] Kizdean Gix spasms as the spirit of a scorpion rips through their body .

This PR also puts the pet damage under the correct filter if you are the pet owner.  if you're not the pet owner, you're just gonna get the messages just like all the other pet messages.

I'd suggest long term maybe we need a rule to turn off others pet messages, but that's outside the scope of this fix.

@Kinglykrab Maybe you can have your guy do some testing before we merge this?  We tried to test it well, testing various situations, but only have like 2 hours of testing in.  Your call.

---
## [nh-server/Kurisu](https://github.com/nh-server/Kurisu)@[9e35541d41...](https://github.com/nh-server/Kurisu/commit/9e35541d41ded2e07a938ef8acfc9b70916c1090)
#### Monday 2023-08-21 02:19:38 by eip

github said i added this but i didnt mean to so i removed it

and then it turned out it needed it anyway
fuck you github

---
## [AngelMTZ2006/BlogAdmissionMIT2024.github.io](https://github.com/AngelMTZ2006/BlogAdmissionMIT2024.github.io)@[200082d179...](https://github.com/AngelMTZ2006/BlogAdmissionMIT2024.github.io/commit/200082d179fd00767052a612477588b6519c861a)
#### Monday 2023-08-21 02:34:00 by AngelMTZ2006

Update README.md

"Unveiling a Remarkable Odyssey: Traversing from the Heart of the Neighborhood to the Pinnacle of Excellence. This is more than a tale; it's a saga that radiates with the energy of aspirations ignited. With every stride, I embody the echoes of countless dreams and the relentless pursuit of advancement. From the humble origins of my neighborhood to the vast landscapes of opportunity, I carry the torch of curiosity and the resolve to transcend limitations.

Embracing challenges as a call to action, I navigate a labyrinth of learning, harnessing the power of education to fuel my ascent. This journey isn't about flashy triumphs; it's about the grit and grace of steady progress. I stand on the precipice of remarkable change, fueled by the synergy of passion and purpose.

As I stand at the threshold of MIT, my spirit resonates with the essence of resilience, forged through the crucible of experience. The path I tread has been carved by unwavering commitment, strengthened by every obstacle overcome. My pursuit mirrors the dynamics of a spider's intricate web, each strand meticulously woven to create a cohesive narrative of growth.

This is my adventure—an expedition fueled by an innate desire to evolve, innovate, and inspire. It's a journey that testifies to the extraordinary results born from the marriage of aspiration and access. Welcome to my world, where the pursuit of excellence thrives, and the spirit of discovery reigns supreme. This is my story—a tapestry interwoven with the threads of curiosity, determination, and the unyielding drive to reach new heights."

---
## [helenhwl/semantic-kernel](https://github.com/helenhwl/semantic-kernel)@[eab7a8f63a...](https://github.com/helenhwl/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Monday 2023-08-21 02:34:36 by Sailesh R

Python: implemented web search engine skill with bing connector (#1813)

### Motivation and Context
<!-- Thank you for your contribution to the semantic-kernel repo!
Please help reviewers and future users, providing the following
information:
  1. Why is this change required?
  2. What problem does it solve?
  3. What scenario does it contribute to?
  4. If it fixes an open issue, please link to the issue here.
-->
In this PR, I have tried my hand at an implementation of web search
engine skill in python semantic kernel using the Bing Web Search API.

### Description
<!-- Describe your changes, the overall approach, the underlying design.
These notes will help understanding how your code works. Thanks! -->
In the semantic kernel directory, I have added a new directory called
web_skills (To replicate Skills.Web from C#) and added the web search
skill here. For now, I have implemented web search using the bing web
search API. If this approach is fine, then I can implement the same with
the google search API too. I have tried to stick with similar naming
conventions as used in the C# implementation with matching context
parameters and arguments.

I can also add some unit tests for the connectors and the search skill,
and add something like exponential backoff to avoid rate limit errors
while querying the search APIs.

Here is some sample code that checks the working of the search skill.

```python
import os
import semantic_kernel as sk
from semantic_kernel.web_skills.web_search_engine_skill import WebSearchEngineSkill
from semantic_kernel.web_skills.connectors import BingConnector
from semantic_kernel.connectors.ai.open_ai import OpenAITextCompletion

async def main():
    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()
    kernel.add_text_completion_service(
        "dv", OpenAITextCompletion("text-davinci-003", api_key, org_id)
    )
    connector = BingConnector(api_key=os.getenv("BING_API_KEY"))
    web_skill = kernel.import_skill(WebSearchEngineSkill(connector), "WebSearch")

    prompt = "Who is Leonardo DiCaprio's current girlfriend?"
    search_async = web_skill["searchAsync"]
    result = await search_async.invoke_async(prompt)
    print(result)

    """
    Output:
    ["Celebrity Celebrity News Everything You Need to Know About Leonardo DiCaprio and Camila Morrone's Relationship From the beginning of their romance to today, we track their relationship here. By..."]
    """

    prompt = """
    Answer the question using only the data that is provided in the data section. Do not use any prior knowledge to answer the question.
    Data: {{WebSearch.SearchAsync "What is semantic kernel?"}}
    Question: What is semantic kernel?
    Answer:
    """

    qna = kernel.create_semantic_function(prompt, temperature=0.2)
    context = kernel.create_new_context()
    context["count"] = "10"
    context["offset"] = "0"
    result = await qna.invoke_async(context=context)
    print(result)

    """
    Output:
    Semantic Kernel is an open-source SDK that lets you easily combine AI services like OpenAI, Azure OpenAI, and Hugging Face with conventional programming languages like C# and Python. By doing so, you can create AI apps that combine the best of both worlds. Semantic Kernel is at the center of the copilot stack.
    """

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

### Contribution Checklist
<!-- Before submitting this PR, please make sure: -->
- [x] The code builds clean without any errors or warnings
- [x] The PR follows SK Contribution Guidelines
(https://github.com/microsoft/semantic-kernel/blob/main/CONTRIBUTING.md)
- [x] The code follows the .NET coding conventions
(https://learn.microsoft.com/dotnet/csharp/fundamentals/coding-style/coding-conventions)
verified with `dotnet format`
- [ ] All unit tests pass, and I have added new tests where possible
- [x] I didn't break anyone :smile:

---------

Co-authored-by: Abby Harrison <54643756+awharrison-28@users.noreply.github.com>
Co-authored-by: Abby Harrison <abby.harrison@microsoft.com>

---
## [Warfan1815/cmss13](https://github.com/Warfan1815/cmss13)@[f3fc60ed65...](https://github.com/Warfan1815/cmss13/commit/f3fc60ed655d27bb3f012d0e0d834c64990b173d)
#### Monday 2023-08-21 03:15:36 by morrowwolf

Attachment nerfs and removals (#4122)

# About the pull request

This PR:

Removes the barrel charger from vendors

Removes all benefits other than wield delay mod from the angled grip

Adds wield delay to the extended barrel

# Explain why it's good for the game

Barrel charger is a straight damage increase and rather silly to work
around given how burst works bypassing real fire rate concerns. If you
know, you know. Horrible idea, I am amazed it's been around this long.

Angled grip had zero downside. Now it still has zero downside but isn't
also a ton of accuracy buffs on top of the god-tier lower wield delay.

Extended barrel had zero downside. Now it has a downside.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removed the barrel charger from vendors
balance: Removed all benefits other than wield delay mod from the angled
grip
balance: Added wield delay to extended barrel
/:cl:

---
## [JoverZhang/neovide](https://github.com/JoverZhang/neovide)@[937decd850...](https://github.com/JoverZhang/neovide/commit/937decd850f2087a20e6488e42ffd1fafbec02e0)
#### Monday 2023-08-21 04:18:49 by fredizzimo

fix: Improve nvim detection (#1946)

* Improve nvim detection:

Don't rely on the shell specific `exists", instead run `nvim -v`.
Additionally, if there's unexpected output, for example if your shell is
configured wrongly to output something when run in non-interactive mode,
it will tell you so, instead of failing with very strange errors later.

The `neovim-bin` argument has also been changed to always require the
binary to exist, instead if falling back to `nvim` as that's probably
not what the user wants. If `nevoim-bin` contains path separators the
binary will be tried directly, otherwise `which` will be used to find
the correct executable.

The which command has also been changed to always use the which crate
first to avoid shell specific issues (for example nushell).

The output is printed directly to stderr instead of the log, for a more
user friendly experience. Furthermore, the maybe disown call has been
moved so that the user actually has a chance to see the errors in the
console.

* fix(command): correct typos and clarify help message

* fix: preliminarly restore forking behavior

This however also loses possible error messages at startup about the
nvim binary not being found.

* codestyle: calm rustfmt

* fix(command): make error message about missing/errornous nvim visible

---------

Co-authored-by: MultisampledNight <contact@multisamplednight.com>

---
## [obsidiansystems/nix](https://github.com/obsidiansystems/nix)@[b13fc7101f...](https://github.com/obsidiansystems/nix/commit/b13fc7101fb06a65935d145081319145f7fef6f9)
#### Monday 2023-08-21 04:35:39 by Robert Hensing

Add positive source filter

Source filtering is a really cool Nix feature that lets us avoid a
lot of rebuilds, which speeds up the iteration cycle a lot in cases
where the relevant source files aren't actually modified.

We used to have a source filter that marked a few files as irrelevant,
but this is the wrong approach, as we have many more files that are
irrelevant. We may call this negative filtering.

This commit switches the source filtering to positive filtering, which
is a lot more robust. Instead of marking which files we don't need
we marked the files that we do need.

It's a superior approach because it is fail safe. Instead of allowing
build performance problems to creep in over time, we require that all
source inputs are declared.

I shouldn't have to explain that declaring inputs is a good practice,
so I'll stop over-explaining here.

I do have to acknowledge that this will cause a build failure when the
filter is incomplete. This is *good*, because it's the only realistic
way we could be reminded of these problems. These events will be
infrequent, so the small cost of extending the filter is worth it,
compared to the hidden cost of longer dev cycles for things like tests,
docker image, etc, etc.

(Also rebuilding Nix for stupid unnecessary reasons makes my blood boil)

---
## [torvalds/linux](https://github.com/torvalds/linux)@[4542057e18...](https://github.com/torvalds/linux/commit/4542057e18caebe5ebaee28f0438878098674504)
#### Monday 2023-08-21 05:09:13 by Linus Torvalds

mm: avoid 'might_sleep()' in get_mmap_lock_carefully()

This might_sleep() goes back a long time: it was originally introduced
way back when by commit 010060741ad3 ("x86: add might_sleep() to
do_page_fault()"), and made it into the generic VM code when the x86
fault path got re-organized and generalized in commit c2508ec5a58d ("mm:
introduce new 'lock_mm_and_find_vma()' page fault helper").

However, it turns out that the placement of that might_sleep() has
always been rather questionable simply because it's not only a debug
statement to warn about sleeping in contexts that shouldn't sleep (which
was the original reason for adding it), but it also implies a voluntary
scheduling point.

That, in turn, is less than desirable for two reasons:

 (a) it ends up being done after we successfully got the mmap_lock, so
     just as we got the lock we will now eagerly schedule away and
     increase lock contention

and

 (b) this is all very possibly part of the "oops, things went horribly
     wrong" path and we just haven't figured that out yet

After all, the whole _reason_ for having that get_mmap_lock_carefully()
rather than just doing the obvious mmap_read_lock() is because this code
wants to deal somewhat gracefully with potential kernel wild pointer
bugs.

So then a voluntary scheduling point here is simply not a good idea.

We could certainly turn the 'might_sleep()' into a '__might_sleep()' and
make it be just the debug check that it was originally intended to be.

But even that seems questionable in the wild kernel pointer case - which
again is part of the whole point of this code.  The problem wouldn't be
about the _sleeping_ part of the page fault, but about a bad kernel
access.  The fact that that bad kernel access might happen in a section
that you shouldn't sleep in is secondary.

So it really ends up being the case that this is simply entirely the
wrong place to do this debug check and related scheduling point at all.

So let's just remove the check entirely.  It's been around for over a
decade, it has served its purpose.

The re-schedule will happen at return to user space anyway for the
normal case, and the warning - if we even need it - might be better off
done as a special case for "page fault from kernel mode" once we've
dealt with any potential kernel oopses where the oops is the relevant
thing, not some artificial "scheduling while atomic" test.

Reported-by: Mateusz Guzik <mjguzik@gmail.com>
Link: https://lore.kernel.org/lkml/20230820104303.2083444-1-mjguzik@gmail.com/
Cc: Matthew Wilcox <willy@infradead.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [chadmcinnis/react](https://github.com/chadmcinnis/react)@[ac1a16c67e...](https://github.com/chadmcinnis/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Monday 2023-08-21 05:20:23 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3645fa7d89...](https://github.com/tgstation/tgstation/commit/3645fa7d8956bed2d3ebff86b072f8b9544d383d)
#### Monday 2023-08-21 06:01:09 by distributivgesetz

Replaces slime clone damage with a "Covered in Slime" status effect (#77569)

## About The Pull Request

This PR replaces clone damage dealt by slimes with a new status effect,
"Covered in Slime".

The status effect is applied when you wrestle a slime off. The status
effect has a chance of not applying if your biohazard protection on your
head and chest is good enough.

It deals brute damage over time and gets removed when you stand under
the shower for about 10 seconds or when you are about to enter softcrit.

As a direct consequence of adding this feature I added showers to the
North Star and Birdshot Xenobiology Labs. I'm sorry, I'm sure you wanted
to make a statement with this, but we kind of require them in there now.

## Why It's Good For The Game

One source of clone damage eliminated whilst hopefully keeping a
"unique" interaction when dealing with slimes. No other source of clone
damage has been touched.

Clone damage is a damage type that shouldn't exist anymore, it's a relic
left from the era of cloning and it's so specific of a damage type that
it rarely gets used as a result. It really should be a type of
affliction (wound etc) instead of its own damage counter.

However, some things in the game still depend on clone damage being
around, so those needs to be addressed first.
We start off with slimes in this PR.

This status effect either lets you either continue with your work if you
react fast enough or it forces you to medbay, giving a victim more
control over the situation, as opposed to just being dealt a rare damage
type that always forces you to go to medbay if you want it healed.

## Changelog

:cl: distributivgesetz
add: Replaced slime clone damage with a "Covered in Slime" status effect
that deals brute damage over time and can be washed off by standing
under a shower.
add: Northstar and Birdshot Xenobiology have been outfitted with a new
shower.
code: Replaced the magic strings in slime code with macros. Also
included some warnings to anyone daring to touch the macros.
/:cl:

---
## [Sagnac/streamsave](https://github.com/Sagnac/streamsave)@[43abedc5a7...](https://github.com/Sagnac/streamsave/commit/43abedc5a702160327b3d47c1922c50d1e80e02f)
#### Monday 2023-08-21 06:40:51 by Sagnac

Redesign how options are updated

The previous scheme was pretty ugly. This is due for a much more
comprehensive rewrite as there's quite a bit of redundancy with the
script-message functions and maintaining both script-opts and
script-message updates requires more effort. But that will have to come
at a later time.

One alternative approach would be to hook into the current override
functions by using them as fields in the update table and have them
perform double duty, but this may prove more trouble than it's worth.

As a user, the script-message approach to changing options is more
convenient to use during runtime either with keybinds or through the
console. Also, it supports more arguments (e.g. cycle, on_demand) and
provides status messages. That being said, with script-opts you can send
an entire list of options to be updated instead of having to chain
script-message commands. The names being used for this also differ
between the two methods, with the script-message names being shorter and
likely easier to remember, but the inconsistency in naming between the
options and the runtime commands could be an issue.

Of course I could just turn off the script-opt updating mechanism by
not using update_opts, which I probably should do, but I'm going to keep
this around for now while I trim the script down to a lite version at a
separate branch; this will prove useful there as script-opts becomes the
desired minimalistic approach.

Another thing to note with regards to removing on_update handling of the
options is that some options such as the likely widely used
force_extension option would still require support in that regard, as
the runtime command is simply an on-demand single-stream change and a
revert handler, and does not in actuality set the format in a global
manner - if a new stream is loaded then it will take on the
automatically determined format.

---
## [Icarus-The-Sun/Bubberstation](https://github.com/Icarus-The-Sun/Bubberstation)@[a21626289e...](https://github.com/Icarus-The-Sun/Bubberstation/commit/a21626289ef84022641eee92cf7ea81406de4fd3)
#### Monday 2023-08-21 06:44:59 by Icarus-The-Sun

FIXES THE BROKEN SHIT

I am, in fact, a fucking idiot.

---
## [LangatErick/LangatErick](https://github.com/LangatErick/LangatErick)@[3a913a9eb4...](https://github.com/LangatErick/LangatErick/commit/3a913a9eb4d02159fd51237906fb9499d1f759d9)
#### Monday 2023-08-21 06:57:55 by Langat Erick

Rename README.md to LngatErick.md

Name: LANGAT ERICK 
Age: 25
Location: NAIROBI KENYA

**Background and Expertise:**
I am a Certified Data Scientist Professional, focusing on machine learning and data Science. With 4+ years of experience, I am a seasoned data scientist who thrives on unraveling complex challenges. My exceptional track record includes successful projects across the e-commerce, finance, and healthcare sectors.

**Technical Mastery:**
- Proficient in Python, R, and SQL for data manipulation, analysis, and modeling.
- Exceptional skill in crafting machine learning models, leveraging both supervised and unsupervised techniques.
- Mastery of data visualization tools like Matplotlib, Seaborn, and D3.js to weave compelling narratives from data.
- Extensive experience with cloud platforms like AWS, Google Cloud, and Azure for scalable data solutions.
- Adept with big data technologies including Hadoop, Spark, and Hive.

**Analytical Prowess:**
I excel at:
- Turning complex data into actionable insights through advanced statistical analysis and predictive modeling.
- Designing A/B tests to optimize strategies and product offerings, boosting ROI by up to 20%.
- Collaborating closely with cross-functional teams, aligning technical solutions with business goals.
- Applying domain knowledge to craft tailored machine learning models, leading to a 15% accuracy boost in sales predictions.

**Communication Excellence:**
With exceptional communication skills, I:
- Delivers impactful presentations, translating data findings into clear business implications.
- Collaborates seamlessly with executives, engineers, and stakeholders to drive data-driven decisions.
- Thrives in team environments, bridging the gap between technical and non-technical stakeholders.
- Mentors junior data scientists, fostering a culture of growth and innovation.

**Ethical Leadership:**
- Champions data privacy and adheres to regulations like GDPR, ensuring data integrity and security.
- Promotes responsible AI practices, mitigating potential biases and ensuring fairness in models.

**Innovation and Aspirations:**

- Expanding her expertise in deep learning to unlock new realms of predictive power.
- Contributing to research that advances the field and promotes ethical AI deployment.
- Sharing my insights through conferences and publications, advocating for transparent and impactful data science.

---
## [a4lg/binutils-gdb](https://github.com/a4lg/binutils-gdb)@[05e1cac249...](https://github.com/a4lg/binutils-gdb/commit/05e1cac2496f842f70744dc5210fb3072ef32f3a)
#### Monday 2023-08-21 07:26:11 by Andrew Burgess

gdb: fix vfork regressions when target-non-stop is off

It was pointed out on the mailing list[1] that after this commit:

  commit b1e0126ec56e099d753c20e91a9f8623aabd6b46
  Date:   Wed Jun 21 14:18:54 2023 +0100

      gdb: don't resume vfork parent while child is still running

the test gdb.base/vfork-follow-parent.exp now has some failures when
run with the native-gdbserver or native-extended-gdbserver boards:

  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to end of inferior 2 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: inferior 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: print unblock_parent = 1 (timeout)
  FAIL: gdb.base/vfork-follow-parent.exp: resolution_method=schedule-multiple: continue to break_parent (timeout)

The reason that these failures don't show up when run on the standard
unix board is that the test is only run in the default operating mode,
so for Linux this will be all-stop on top of non-stop.

If we adjust the test script so that it runs in the default mode and
with target-non-stop turned off, then we see the same failures on the
unix board.  This commit includes this change.

The way that the test is written means that it is not (currently)
possible to turn on non-stop mode and have the test still work, so
this commit does not do that.

I have also updated the test script so that the vfork child performs
an exec as well as the current exit.  Exec and exit are the two ways
in which a vfork child can release the vfork parent, so testing both
of these cases is useful I think.

In this test the inferior performs a vfork and the vfork-child
immediately exits.  The vfork-parent will wait for the vfork-child and
then blocks waiting for gdb.  Once gdb has released the vfork-parent,
the vfork-parent also exits.

In the test that fails, GDB sets 'detach-on-fork off' and then runs to
the vfork.  At this point the test tries to just "continue", but this
fails as the vfork-parent is still selected, and the parent can't
continue until the vfork-child completes.  As the vfork-child is
stopped by GDB the parent will never stop once resumed, so GDB refuses
to resume it.

The test script then sets 'schedule-multiple on' and once again
continues.  This time GDB, in theory, resumes both the parent and the
child, the parent will be held blocked by the kernel, but the child
will run until it exits, and which point GDB stops again, this time
with inferior 2, the newly exited vfork-child, selected.

What happens after this in the test script is irrelevant as far as
this failure is concerned.

To understand why the test started failing we should consider the
behaviour of four different cases:

  1. All-stop-on-non-stop before commit b1e0126ec56e,

  2. All-stop-on-non-stop after commit b1e0126ec56e,

  3. All-stop-on-all-stop before commit b1e0126ec56e, and

  4. All-stop-on-all-stop after commit b1e0126ec56e.

Only case #4 is failing after commit b1e0126ec56e, but I think the
other cases are interesting because, (a) they inform how we might fix
the regression, and (b) it turns out the behaviour of #2 changed too
with the commit, but the change was harmless.

For #1 All-stop-on-non-stop before commit b1e0126ec56e, what happens
is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-non-stop, every thread is resumed
    individually, so GDB tries to resume both the vfork-parent and the
    vfork-child, both of which succeed,

  3. The vfork-parent is held stopped by the kernel,

  4. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  5. At this point we might take two paths depending on which event
     GDB handles first, if GDB handles the VFORK_DONE first then:

     (a) As GDB is controlling both parent and child the VFORK_DONE is
         ignored (see handle_vfork_done), the vfork-parent will be
	 resumed,

     (b) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     Alternatively, if GDB selects the EXITED event first then:

     (c) GDB processes the EXITED event, selects the (now defunct)
         vfork-child, and stops, returning control to the user.

     (d) At some future time the user resumes the vfork-parent, at
         which point the VFORK_DONE is reported to GDB, however, GDB
	 is ignoring the VFORK_DONE (see handle_vfork_done), so the
	 parent is resumed.

For case #2, all-stop-on-non-stop after commit b1e0126ec56e, the
important difference is in step (2) above, now, instead of resuming
both the vfork-parent and the vfork-child, only the vfork-child is
resumed.  As such, when we get to step (5), only a single event, the
EXITED event is reported.

GDB handles the EXITED just as in (5)(c), then, later, when the user
resumes the vfork-parent, the VFORKED_DONE is immediately delivered
from the kernel, but this is ignored just as in (5)(d), and so,
though the pattern of when the vfork-parent is resumed changes, the
overall pattern of which events are reported and when, doesn't
actually change.  In fact, by not resuming the vfork-parent, the order
of events (in this test) is now deterministic, which (maybe?) is a
good thing.

If we now consider case #3, all-stop-on-all-stop before commit
b1e0126ec56e, then what happens is:

  1. GDB calls proceed with the vfork-parent selected, as schedule
     multiple is on user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid (see proceed function),

  2. As this is all-stop-on-all-stop, the resume is passed down to the
     linux-nat target, the vfork-parent is the event thread, while the
     vfork-child is a sibling of the event thread,

  3. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this causes the vfork-child to be resumed.  Then
     in linux_nat_target::resume, the event thread, the vfork-parent,
     is also resumed.

  4. The vfork-parent is held stopped by the kernel,

  5. The vfork-child completes (exits) at which point the GDB sees the
     EXITED event for the vfork-child and the VFORK_DONE event for the
     vfork-parent,

  6. We are now in a situation identical to step (5) as for
     all-stop-on-non-stop above, GDB selects one of the events to
     handle, and whichever we select the user sees the correct
     behaviour.

And so, finally, we can consider #4, all-stop-on-all-stop after commit
b1e0126ec56e, this is the case that started failing.

We start out just like above, in proceed, the resume_ptid is
-1 (resume everything), due to schedule multiple being on.  And just
like above, due to the target being all-stop, we call
proceed_resume_thread_checked just once, for the current thread,
which, remember, is the vfork-parent thread.

The change in commit b1e0126ec56e was to avoid resuming a vfork-parent
thread, read the commit message for the justification for this change.

However, this means that GDB now rejects resuming the vfork-parent in
this case, which means that nothing gets resumed!  Obviously, if
nothing resumes, then nothing will ever stop, and so GDB appears to
hang.

I considered a couple of solutions which, in the end, I didn't go
with, these were:

  1. Move the vfork-parent check out of proceed_resume_thread_checked,
     and place it in proceed, but only on the all-stop-on-non-stop
     path, this should still address the issue seen in b1e0126ec56e,
     but would avoid the issue seen here.  I rejected this just
     because it didn't feel great to split the checks that exist in
     proceed_resume_thread_checked like this,

  2. Extend the condition in proceed_resume_thread_checked by adding a
     target_is_non_stop_p check.  This would have the same effect as
     idea 1, but leaves all the checks in the same place, which I
     think would be better, but this still just didn't feel right to
     me, and so,

What I noticed was that for the all-stop-on-non-stop, after commit
b1e0126ec56e, we only resumed the vfork-child, and this seems fine.
The vfork-parent isn't going to run anyway (the kernel will hold it
back), so if feels like we there's no harm in just waiting for the
child to complete, and then resuming the parent.

So then I started looking at follow_fork, which is called from the top
of proceed.  This function already has the task of switching between
the parent and child based on which the user wishes to follow.  So, I
wondered, could we use this to switch to the vfork-child in the case
that we are attached to both?

Turns out this is pretty simple to do.

Having done that, now the process is for all-stop-on-all-stop after
commit b1e0126ec56e, and with this new fix is:

  1. GDB calls proceed with the vfork-parent selected, but,

  2. In follow_fork, and follow_fork_inferior, GDB switches the
     selected thread to be that of the vfork-child,

  3. Back in proceed user_visible_resume_ptid returns -1 (everything)
     as the resume_ptid still, but now,

  4. When GDB calls proceed_resume_thread_checked, the vfork-child is
     the current selected thread, this is not a vfork-parent, and so
     GDB allows the proceed to continue to the linux-nat target,

  5. In linux_nat_target::resume, GDB calls linux_nat_resume_callback
     for all threads, this does not resume the vfork-parent (because
     it is a vfork-parent), and then the vfork-child is resumed as
     this is the event thread,

At this point we are back in the same situation as for
all-stop-on-non-stop after commit b1e0126ec56e, that is, the
vfork-child is resumed, while the vfork-parent is held stopped by
GDB.

Eventually the vfork-child will exit or exec, at which point the
vfork-parent will be resumed.

[1] https://inbox.sourceware.org/gdb-patches/3e1e1db0-13d9-dd32-b4bb-051149ae6e76@simark.ca/

---
## [KamilAliyev1/Library-Management-System](https://github.com/KamilAliyev1/Library-Management-System)@[567cc52a86...](https://github.com/KamilAliyev1/Library-Management-System/commit/567cc52a863ac4a6b2fc857bc56e82f7538e3be6)
#### Monday 2023-08-21 08:14:59 by KamilAliyev1

Delete Group of Asian teenage girls having party celebrating on beach, friends happy drinking beer on beach at sea when sunset in evening. Outdoor activity friends travel holiday vacation summer concept1.png

---
## [madebr/mpg123](https://github.com/madebr/mpg123)@[bb3d506871...](https://github.com/madebr/mpg123/commit/bb3d506871596ebe4b54227363f3f1ccbdaf1f5c)
#### Monday 2023-08-21 09:07:33 by thor

libmpg123: purge off_t out of the core, offer 64 bit portable API (bug 344)

This now is the result of way to much time of thinking hard about disentangling
the various I/O paths in libmpg123. It needed days of hacking, way too many
hours continuously, to figure out how this would work. So this is my draft
that I tested in various settings and am hopeful that it fulfills the ideas
drafted in bug 344, the relentless discussion with manx about how portable
API should look.

Instead of just adding some 64 bit functions, this is a refactoring of the
reader code, moving the parts actually dealing with OS calls and largefile
support into lfs_wrap.c, which now offers wrappers and aliases. All file I/O
is now routed through the interface of mpg123_reader64() and could neatly be
split into a separate library, weren't it for only a handful of internal hooks.

I fixed up the autoconf and the CMake build. Ideally, both break only on
a limited set of platforms. I am pushing this directly to trunk as a)
I did testing on x86-64 and i686 with some largefile switchery and think
it should work and b) I want people to quickly tell me what does not work.

Let's see how many iterations we'll need until 1.32.0 can finally be released.



git-svn-id: svn://scm.orgis.org/mpg123/trunk@5304 35dc7657-300d-0410-a2e5-dc2837fedb53

---
## [jalenng/Draw](https://github.com/jalenng/Draw)@[f286df5ff3...](https://github.com/jalenng/Draw/commit/f286df5ff3f2ffd3501f5e716df7acf7c0de8665)
#### Monday 2023-08-21 09:22:41 by spicywheatbread

Add files for SFX (#39)

* Basic SFX Added

Added placeholder sound effects to things like jumping and dying.

(cherry picked from commit e721f5ff4a91ac3e89c323e4e900a352f9b02ebf)

* More SFX

Added new page flip sound, added sounds to return buttons in menus, more work to be done on this but just uploading so I can work on this from my laptop at school

(cherry picked from commit 17ef3bacf1a95b3778570ce80ec9582177c4649c)

* SFX files and settings menu

Added some sound files for sfx and light changes for the settings menu to continue to work on later.

(cherry picked from commit 571e9bcd4503ab057ca9b09099a4f41f4f9d562f)

* Sorry this is a bunch of random changes lmao. Added ambiences to NathanP2, the Prefab to play Ambience. Also, added new respawnManager to respawn necesasry objects like OrangeObjects and ScribbleWall. Moved some scripts into folders. Random level fixes for Mike, Claire, etc from playtesting.

(cherry picked from commit b1b9afbf29567d345e08e4a96ca4f4da3b63e885)

* sfx added + slider func

Added some more sound effects, sliders in settings menu now play a sound to reflect their real volumes, added looping sound to drawing canvases.

(cherry picked from commit 8007a22b04b5dde97c5cbfba0ebc9ccc8ab904c2)

* I'm not gonna lie. I don't remember what I changed
about the levels, but I'm PRETTY sure it's something.
Mostly, Stickman now stops walking animation when walking into a wall
and stops playing footstepSFX as well. PageflipSFX when finishing level.
Quick logic fix for levelendtrigger b/c it would call loadnextscene
multiple times. Made audiosystem global so it's easier to code.

(cherry picked from commit 65a49121750f5d3fb48a452b08b4d0063a770bdd)

* Forgot to commit the change for the animation
controller update.

(cherry picked from commit b6cd4de1442639ee872adb574f27acf95450c4dd)

* Delete it.

I hate it. new page flip wav meta

---
## [dr3ams/Roguelike-Adventures-and-Dungeons-2](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2)@[eebbc22d1a...](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2/commit/eebbc22d1a94fc45761ba50c3cc1e6d66263eadc)
#### Monday 2023-08-21 10:13:58 by dr3ams

1.6 update with summarized changes

- reduce nerf to heal
- xp bonus for finding neptune's bounty
- Added 100 fishing xp for catching neptune's bounty from fishing
- Alternate Texture for the Loot Crate.
- Recolored previously white loot crates
	- Recolored the crate crate, enchanted crate, ingots crate, sapling crate, seed crate and stone crate to more fitting colors.
	- Changed the Crate Crate to the alt Crate model from the previous commit.
- Fixed Crafted Akashic Tome not having all the guidebooks
	- Previously the Akashic Tome was empty when crafted. Now it has all the guidebooks similar the starting one and in the shop
- Fixed Fishing Data Pack
- Another Buff to The Twist
- The Twist now grants +100% magic damage in the offhand, making it a spellbook of some sort
- Disable Shiba
- Can cause ticking entities when they "fetch" certain projectiles
- Reduce shield cost
- Minor reduction 1000 > 750
- Increase all armor durability
- Basically all Armor items have durability increased by 100%
- Quest Updates by @ScriptAero
	- Deleted the 3 impossible quests that I was aware of, fixed a centaur quest, added a touch of info on nether cheese and tropicraft"
- Remove Vodoo Upgrade recipe
- Hide voodoo upgrade
- Rearranged jewelry quests
- Tweak Enderoligist
	- Good bye head Hello funny worm
- No More Sandy Endstone Aquisition
- PMMO adjustments
	Exp Boosts
	- made some dungeons gear weapons boost shadow instead of archery
	- totem of undying gives minor magic boost
	- jar of light gives major light boost
	- fishing rods now boost fishing exp when held, with better rods giving better boosts
	- stimphalian bird dagger now gives smithing bonus, in place of the unusable skull
	- cyclops skull now boosts woodcutting, gathering, and wayfaring
	- unused skills removed from i&f skulls
		- enigmatic legacy given significant buffs
		- charm of treasure hunter now gives medium "block breaking" skill boosts
		- emblem of monster slayer now gives minor "slaying" skill boosts
		- emblem of bloodstained valor now gives medium "slaying" skill boosts
		- unholy stone now gives major "slaying" skill boosts
		- ring of seven curses now gives major combat, endurance, light, and shadow skill boosts
		- enchanter's pearl now gives major magic boost
		- nefarious essence now gives major shadow boost
	- blue skies armor buffed
		- diopside armor gives major alchemy bonus
		- pyrope armor gives major mining, woodcutting, and gathering bonuses
		- aquite armor gives +100% swimming bonus
	Requirements
	- sheep disguise requirements removed
	- hoes now require gathering instead of farming
	- dread knight's sword now also requires shadow 3
	- pearl of the void now requires shadow instead of alchemy
- renamed 'The Patreon' quest chapter to 'The Patreon of Gods'
- added new patrons to the 'The Patreon of Gods' quest chapter. Immortalize yourself here https://www.patreon.com/Dreams01

---
## [K4rlox/Foundation-19](https://github.com/K4rlox/Foundation-19)@[b4642dc835...](https://github.com/K4rlox/Foundation-19/commit/b4642dc835dc801d801fd543cfd34bd44ca23929)
#### Monday 2023-08-21 10:17:19 by cheesePizza2

Armor improvements (#1251)

* the fixes

* FUCK YOU

* few more improvements

* bring em back

* fuck you

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[107918eecf...](https://github.com/Offroaders123/NBTify/commit/107918eecf7b6cb5e075dfd8748d461ce83dd713)
#### Monday 2023-08-21 10:24:34 by Offroaders123

Dual-Module Building Demo

Accidentally tried to import NBTify in a CommonJS TypeScript project because I forgot to set the `"type": "module"` value in it's `package.json`. That made me come back and remember that you can publish both ESM and CommonJS builds from the same library. I was debating whether that would be something good for NBTify because it could possible allow more users to be able to use NBTify, if using pure-ESM isn't an option for them. I went down a rabbit hole trying to figure out setting this up.

https://thesametech.com/how-to-build-typescript-project/
https://evertpot.com/universal-commonjs-esm-typescript-packages/
https://antfu.me/posts/publish-esm-and-cjs
https://www.sensedeep.com/blog/posts/2021/how-to-create-single-source-npm-module.html
https://dev.to/mbarzeev/hybrid-npm-package-through-typescript-compiler-tsc-150c

Looked into Project References the other day, and I didn't (and still don't) properly understand what you're supposed to use those for, and how to set them up. In hopes of also learning more about them, I wondered if they would help with setting up a better build organization than having so many unconnected `tsconfig` files, which is how this setup currently works. That's what I went with for this commit, to start with.

https://www.typescriptlang.org/docs/handbook/project-references.html
https://jakeginnivan.medium.com/breaking-down-typescript-project-references-260f77b95913
https://blog.logrocket.com/boost-your-productivity-with-typescript-project-references/

More links about dual-module packages:
https://www.typescriptlang.org/tsconfig#declarationMap (Looked helpful for things, but it only is applicable from the dev side of things it looks like, so I'm not going to enable it)
https://github.com/azu/tsconfig-to-dual-package

Related and having to do with Project References, I didn't understand what the purpose was of the `--build` flag for `tsc`. Looks like it's like a more of a modular approach to building multiple `tsconfig` definitions folder regions. I think Project References/the `--build` flag are more meant for monorepos and things like that, rather than single-build, multi-config libraries like how NBTify is.

Here's more info about the `--build` flag.

https://www.typescriptlang.org/docs/handbook/compiler-options.html
https://stackoverflow.com/questions/67796765/tsc-build-vs-tsc-project
https://stackoverflow.com/questions/70703085/tsc-build-specify-tsconfig-json
https://raghsonline.com/posts/typescript/typescript-clean-build/ (I thought this cleaned *and* built the output files, but looks like it only cleans where the resolution files will be; not including un-managed files :( So if there are any loose files in your `./dist` folder, you still have to make sure you delete them yourself, TypeScript won't do it for you. I do like the choice of security there, so I see why they didn't make `--clean` do that)

Relatable feeling of not knowing where to start with config things like this; This sort of thing were my main challenges when starting with TypeScript last year.
https://www.reddit.com/r/typescript/comments/sfz7xj/recommended_ts_js_build_system/

More info about `tsconfig.json` use. Specific to old versions of VSCode, which apparently only supported a single config per workspace? I was more taking away from this one how they hooked their configs together than the VSCode part, since that seems to be a problem that was solved.
https://stackoverflow.com/questions/37579969/how-to-use-multiple-tsconfig-files-in-vs-code

This one appears to be my current setup/struggle before these experimental changes, where you want to have a consistent set of `tsconfig` options set for the whole project, but you don't want to compile all of the `.ts` files available as part of the build output, only the ones from `./src`. Based on the answers for this one, I feel like it might have been one I've come across before, since it looks very similar to that of the setup I have been using since setting up a proper test suite.
https://stackoverflow.com/questions/35470511/setting-up-tsconfig-with-spec-test-folder

Crossover between the one above, and Project References. I want to see if it's possible to do this, with that, and with these dual-module changes?
https://stackoverflow.com/questions/51631786/how-to-use-project-references-in-typescript-3-0
https://github.com/vercel/next.js/discussions/30815 (Hadn't heard of `.tsbuildinfo`)
https://www.typescriptlang.org/tsconfig#incremental (Nor the `incremenetal` config option)

While looking at my `package.json`, I was reconsidering my `devDependencies` install of `tsx`. Should I use `npx` to run it, rather than managing an install of it bu the module itself? (Gonna stick with no)
https://dev.to/azure/using-npx-and-npm-scripts-to-reduce-the-burden-of-developer-tools-57f9
https://www.codingninjas.com/studio/library/difference-between-npm-and-npx (Nice reminder of what `npx` should properly be used/is intended for)
https://stackoverflow.com/questions/55138134/npx-tsc-version-reports-different-typescript-version-inside-virtual-machine (A reminder than not having packages installed as part of your project can kind of cause problems like being out in the Wild West)

More about `declarationMap`
https://stackoverflow.com/questions/58459988/what-is-the-use-case-of-enabling-declaration-and-declarationmap-in-tsconfig-json

Random thing, this was helpful with checking `declarationMap` while in 'production', with the build output at least.
https://stackoverflow.com/questions/50010438/install-npm-local-module-directory-without-symlinks

---
## [KoviRobi/nushell](https://github.com/KoviRobi/nushell)@[ad49c17eba...](https://github.com/KoviRobi/nushell/commit/ad49c17ebacd04585fb4355e079ec87d7fc63d8d)
#### Monday 2023-08-21 10:32:48 by Kiryl Mialeshka

fix(nu-parser): do not update plugin.nu file on nu startup (#10007)

<!--
if this PR closes one or more issues, you can automatically link the PR
with
them by using one of the [*linking
keywords*](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue#linking-a-pull-request-to-an-issue-using-a-keyword),
e.g.
- this PR should close #xxxx
- fixes #xxxx

you can also mention related issues, PRs or discussions!
-->

# Description

I've been investigating the [issue
mentioned](https://github.com/nushell/nushell/pull/9976#issuecomment-1673290467)
in my prev pr and I've found that plugin.nu file that is used to cache
plugins signatures gets overwritten on every nushell startup and that
may actually mess up with the file content if 2 or more instances of
nushell will run simultaneously.

To reproduce:
1. register at least 2 plugins in your local nushell
2. remember how many entries you have in plugin.nu with `open
$nu.plugin-path | find nu_plugin`
3. run 
    - either `cargo test` inside nushell repo
- or run smth like this `1..100 | par-each {|it| $"(random integer
1..100)ms" | into duration | sleep $in; nu -c "$nu.plugin-path"}` to
simulate parallel access. This approach is not so reliable to reproduce
as running test but still a good point that it may effect users actually
4. validate that your `plugin.nu` file was stripped

<!--
Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.

Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.
-->

# Solution

In this pr I've refactored the code of handling the `register` command
to minimize code duplications and make sure that overwrite of
`plugin.nu` file is happen only when user calls the command and not on
nu startup

Another option would be to use temp `plugin.nu` when running tests, but
as the issue actually can affect users I've decided to prevent
unnecessary writing at all. Although having isolated `plugin.nu` still
worth of doing

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->
It changes the behaviour actually as the call `register <plugin>
<signature>` now doesn't updates `plugin.nu` and just reads signatures
to the memory. But as I understand that kind of call with explicit
signature is meant to use only by nushell itself in the `plugin.nu` file
only. I've asked about it in
[discord](https://discordapp.com/channels/601130461678272522/615962413203718156/1140013448915325018)

<!--
Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used -A
clippy::needless_collect -A clippy::result_large_err` to check that
you're using the standard code style
- `cargo test --workspace` to check that all tests pass
- `cargo run -- -c "use std testing; testing run-tests --path
crates/nu-std"` to run the tests for the standard library

> **Note**
> from `nushell` you can also use the `toolkit` as follows
> ```bash
> use toolkit.nu # or use an `env_change` hook to activate it
automatically
> toolkit check pr
> ```
-->

# After Submitting
<!-- If your PR had any user-facing changes, update [the
documentation](https://github.com/nushell/nushell.github.io) after the
PR is merged, if necessary. This will help us keep the docs up to date.
-->

Actually, I think the way plugins are stored might be reworked to
prevent or mitigate possible issues further:
- problem with writing to file may still arise if we try to register in
parallel as several instances will write to the same file so the lock
for the file might be required
- using additional parameters to command like `register` to implement
some internal logic could be misleading to the users
- `register` call actually affects global state of nushell that sounds a
little bit inconsistent with immutability and isolation of other parts
of the nu. See issues
[1](https://github.com/nushell/nushell/issues/8581),
[2](https://github.com/nushell/nushell/issues/8960)

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[27d46f1717...](https://github.com/mc-oofert/tgstation/commit/27d46f17173034b805d6ef064d4db31c7e34b26d)
#### Monday 2023-08-21 11:14:25 by OrionTheFox

Science Resprite! (With Sovl!) (#77314)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
What a crusty department. These outfits are...
Something.

![image](https://github.com/tgstation/tgstation/assets/76465278/63fe13cf-bcbf-42c2-a22c-c868ae49a72c)

How old are these now? I'm pretty sure they're unchanged since when I
started playing years ago on other servers.... besides the RD Turtleneck
and Roboticist suit of course. But they still did have some touch-ups to
be made...

Regardless, I think this department deserves a little love!
I've tried to stay true as I could to their current designs; this isn't
a re-**_design_**, just a re-sprite. I used the base jumpsuit design
from Medbay for most of these since it's the most modern suit that fit
with the colored-spots style.

![image](https://github.com/tgstation/tgstation/assets/76465278/ef7ff5b0-f0e3-481a-9ed4-ba830e3ee0c3)

All of them have been touched up, and the RD's "alt" is now a subtype of
the buttondown so it can easily inherit any sprite updates in the
future.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
These deserved some touch-ups and modernization, and while I'm not keen
on entirely reworking them I figured I could at the least give them the
update the Science Team deserves.

(The buttondown has an outdated obj sprite in this image! It's since
been made smaller and more folded)
Also labcoats for comparison

![dreamseeker_Ds8gZLKoGE](https://github.com/tgstation/tgstation/assets/76465278/4da60512-b813-4260-b3fe-5c71b60cec81)

![dreamseeker_C9DpFWWOS7](https://github.com/tgstation/tgstation/assets/76465278/1de55f4c-2eaa-480b-811f-aaa5832eeceb)

![dreamseeker_02d3d7b6aj](https://github.com/tgstation/tgstation/assets/76465278/b1f40d03-c9b8-4f6b-bc54-516b11a7bfb3)

![dreamseeker_DwJGDwbUf1](https://github.com/tgstation/tgstation/assets/76465278/20f97a5e-42ab-4fe0-8eae-4ac6ed24ead4)


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
image: resprited the entirety of RnD! Genetics, Robotics, the RD, and
the Science Team themselves will enjoy the fresh new looks but same
great taste! No, wait, great STYLE! Don't eat these, they're covered in
chemicals.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[a288abcaf2...](https://github.com/mc-oofert/tgstation/commit/a288abcaf2a6b6c44edade8265a66b9ba3f0e67b)
#### Monday 2023-08-21 11:14:25 by san7890

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

---
## [Badoniondev/Paradise-fork](https://github.com/Badoniondev/Paradise-fork)@[2d10818063...](https://github.com/Badoniondev/Paradise-fork/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Monday 2023-08-21 11:50:12 by ATP-Engineer

Fixes IV bag blood overlays being too damn bright for some mixtures (#21813)

* Removes old .dmi

* Fixes blood overlay coloring being too bright for IV bags

* Fine-tuning

* Makes the blood bag IV color overlays not as bright as they used to be

In hindsight it was probably easy to avoid

* FINAL TUNE UP

FUCK

* Fixes coloring for IV bags so they're not too bright

FINAL COMMIT

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[b390525fc5...](https://github.com/tgstation/tgstation/commit/b390525fc5543db5fcdb47869b9297cf637239fc)
#### Monday 2023-08-21 12:44:23 by Rhials

Adds a handful of Ninja Hacking MODule interactions of varying usefulness (#77707)

## About The Pull Request

Adds a few new interactions with the Ninja's ~~right click multipurpose
trolling tool~~ Hacking MOD Module. These new effects are not tied to
objectives and are geared towards expanding the ninja's access,
disabling equipment, and giving them more ways to punk the crew.

### **Useful additions**
Ninjas can now hack open **windoors** and **elevator control panels**.
Both trigger emag_act() when hacked, opening in the case of the windoor,
and disabling the access restrictions _(and also maybe the safeties)_ in
the case of the elevator controls.

**Buttons** can also be emagged by the hacking modules, which removes
their access restrictions.

Hacking a **camera** will now EMP it, disabling it for about 90 seconds.
This can especially useful when trying to complete objectives, and works
better than smashing the cameras with your sword or lugging around
tools.

**Firelocks** can be right-click opened now too, thanks to the hacking
MODule.

**Energy guns** of all variety, useless to a ninja since they can't use
ranged weapons, can now be drained and used to charge your suit. This
takes a brief do_after to complete, so pulling it off mid-combat may be
as risky as it is stylish.

### **Being a nuisance**

**Vendors** can be hacked, expending some charge to trigger the "throw"
wire, making it launch inventory at anyone who passes by.

You can now hack **simplebots**, expending some charge from your suit to
overload and detonate them. It's faster than tipping, and far more
tragic. Sentient simplebots should take care when a ninja is around.

### **Sabotage opportunities**

The **recycler** can now be hacked. This takes 30 seconds and notifies
the AI, just like the communications console hack. Completing the hack
will emag it. That's it.

Hacking the **tram control console** will trigger an extended Tram
Malfunction event, and can be repeated after the event is done. This can
only be done to the "main" tram of the map, which I forsee will be an
absolute nightmare to complete on highpop tramstation.

Neither of these, presently, contribute towards any objectives. They can
be useful for diverting attention, but I see them more as ways for an
overachieving ninja to flex or continue the chaos after their objectives
are complete.

### **OH ALSO**

Hacking open doors costs energy. This really shouldn't be an issue just
remember to recharge sometimes.

The charge drains and do_after lengths for all of these were chosen on
vibes. In all honesty I think the drainage values don't _really_ matter,
due to how easy recharging is, but I had a hard time settling on how
long some of these hack do_afters should take (even if I know they
probably won't matter either).

## Why It's Good For The Game

Being able to hack open airlocks but not windoors always irked me. I
figured that they would be openable like any other door, and that losing
their status as a "-1 dash charge gate" wouldn't be a big enough balance
change to spark arguments. The same philosophy extends to buttons and
elevator controls.

Sapping power from eguns expands on the list of sources energy can be
siphoned from. You can also use it to disarm opponents (like the badass
ninja you are), take emergency charge from a recently-gored officer's
disabler, or dunk on security by draining their entire armory.

Hacking simplebots, vendors, and by extension elevator lifts (since that
also disables the safeties!) give opportunities for minor sabotage. Not
meant to be super disruptive, just a bit silly and annoying for the
crew.

The recycler/tram hacking in particular are meant to be bonus goals,
only sought out by the ballsiest (or more likely boredest) of ninjas.

I see all of these additions as expanding upon the current abilities of
the ninja (not really making them much more powerful, just expanding
their flexibility), or providing more interactions to have fun (and
antagonize the crew) with when not mainlining their objectives.
## Changelog
:cl: Rhials
add: Ninjas can now temporarily disable cameras with the Ninja MOD
right-click hacking ability.
add: Ninjas can emag windoors, elevator controls, and buttons with their
hacking ability.
add: Ninjas can drain the power from energy weaponry, adding the charge
to their MODsuit.
add: Ninjas can now hack simplebots, overloading and detonating them
after a brief delay.
add: Ninjas can now hack vendors, causing them to eject their inventory
at people.
add: Ninjas can now hack the recycler, which notifies the AI and emags
it once complete.
add: Ninjas can now trigger an extended tram malfunction by hacking the
tram control console.
add: Ninjas can now hack open firelocks (temporarily) with right-click.
balance: Hacking open doors with the Ninja Hacking MODule will subtract
a paltry amount of energy from your suit.
/:cl:

---
## [Kaz205/linux](https://github.com/Kaz205/linux)@[da506ae650...](https://github.com/Kaz205/linux/commit/da506ae65073b3506047ab4ef43f73b970541056)
#### Monday 2023-08-21 13:48:54 by Douglas Anderson

migrate_pages: avoid blocking for IO in MIGRATE_SYNC_LIGHT

The MIGRATE_SYNC_LIGHT mode is intended to block for things that will
finish quickly but not for things that will take a long time.  Exactly how
long is too long is not well defined, but waits of tens of milliseconds is
likely non-ideal.

When putting a Chromebook under memory pressure (opening over 90 tabs on a
4GB machine) it was fairly easy to see delays waiting for some locks in
the kcompactd code path of > 100 ms.  While the laptop wasn't amazingly
usable in this state, it was still limping along and this state isn't
something artificial.  Sometimes we simply end up with a lot of memory
pressure.

Putting the same Chromebook under memory pressure while it was running
Android apps (though not stressing them) showed a much worse result (NOTE:
this was on a older kernel but the codepaths here are similar).  Android
apps on ChromeOS currently run from a 128K-block, zlib-compressed,
loopback-mounted squashfs disk.  If we get a page fault from something
backed by the squashfs filesystem we could end up holding a folio lock
while reading enough from disk to decompress 128K (and then decompressing
it using the somewhat slow zlib algorithms).  That reading goes through
the ext4 subsystem (because it's a loopback mount) before eventually
ending up in the block subsystem.  This extra jaunt adds extra overhead.
Without much work I could see cases where we ended up blocked on a folio
lock for over a second.  With more extreme memory pressure I could see up
to 25 seconds.

We considered adding a timeout in the case of MIGRATE_SYNC_LIGHT for the
two locks that were seen to be slow [1] and that generated much
discussion.  After discussion, it was decided that we should avoid waiting
for the two locks during MIGRATE_SYNC_LIGHT if they were being held for
IO.  We'll continue with the unbounded wait for the more full SYNC modes.

With this change, I couldn't see any slow waits on these locks with my
previous testcases.

NOTE: The reason I stated digging into this originally isn't because some
benchmark had gone awry, but because we've received in-the-field crash
reports where we have a hung task waiting on the page lock (which is the
equivalent code path on old kernels).  While the root cause of those
crashes is likely unrelated and won't be fixed by this patch, analyzing
those crash reports did point out these very long waits seemed like
something good to fix.  With this patch we should no longer hang waiting
on these locks, but presumably the system will still be in a bad shape and
hang somewhere else.

[1] https://lore.kernel.org/r/20230421151135.v2.1.I2b71e11264c5c214bc59744b9e13e4c353bc5714@changeid

Link: https://lkml.kernel.org/r/20230428135414.v3.1.Ia86ccac02a303154a0b8bc60567e7a95d34c96d3@changeid
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Suggested-by: Matthew Wilcox <willy@infradead.org>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hillf Danton <hdanton@sina.com>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Alexander Viro <viro@zeniv.linux.org.uk>
Cc: Christian Brauner <brauner@kernel.org>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Huang Ying <ying.huang@intel.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Yu Zhao <yuzhao@google.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Holoo-1/tgstation](https://github.com/Holoo-1/tgstation)@[2d34c7433a...](https://github.com/Holoo-1/tgstation/commit/2d34c7433a0c5315e6a46f7e32e2c9a6c90280b3)
#### Monday 2023-08-21 14:19:33 by Andrew

New Mech UI and equipment refactor (#77221)

![bWJlVIDO53](https://github.com/tgstation/tgstation/assets/3625094/d75030b5-59e9-43f6-96b4-1b7564caceef)

## About The Pull Request

Made a new UI and refactored some mech code in the process.

Fixes #66048
Fixes #77051
Fixes #65958 ??? if it was broken
Fixes #73051 - see details below
Fixes other undocumented things, see changelog.

## Why It's Good For The Game

The UI was too bulky and Mechs were too complex for no reason. 
Now they follow some general rules shared between other SS13 machinery,
and there is less magic happening under the hood.

## Detailed Changes

### New Mech UI, Air Tank and Radio as separate modules

Previous UI for comparison:

<img alt="9SScrXAOjy"
src="https://github.com/tgstation/tgstation/assets/3625094/904e3d07-e7d7-4d3a-a062-93e0e35b4b66">

Previously mechs came with radio pre-installed and air canisters
magically pre-filled with air even when you build one in fab.
Radio and Air Tanks are now both utility modules that are optional to
install. Gas RCS thrusters still require Air Tank module to operate.

This made the Mechs more barebones when built, giving you only the basic
functionality.

<img alt="5SDMlXTJxv"
src="https://github.com/tgstation/tgstation/assets/3625094/b9364230-49ac-416b-aa70-e851fbf2050e">

To compensate this change, all mechs got two extra utility module slots.

All other modules got new UI. And ore box now shows the list of ores
inside.

<img alt="SRX5FjvsHA"
src="https://github.com/tgstation/tgstation/assets/3625094/cbe2e98d-1cd4-4667-8dae-2f9227b4b265">

### Mounted Radio

Works as a normal radio, but with subspace transmission. Available from
the basic mech research node and can be printed in fab.

### Cabin Sealing

To compensate for the lack of air tank by default, mechs with enclosed
cabin (e.g. all except Ripley) got an ability to toggle cabin exposure
to the outside air. Exiting the mech makes cabin air automatically
exposed.

When you seal the cabin, it traps some of the outside air inside the
cabin and you can breathe with this air to perform a short space trips.
But the oxygen will run out quickly and CO2 will build up.

Sealing the cabin in space will make the cabin filled with vacuum, and
it will stay there until you return to air environment and unseal the
cabin, letting the breathable air to enter. There are temperature and
pressure sensors that turn yellow/red when the corresponding warning
thresholds are reached.

You could also use personal internals in combination with cabin sealing
for long space travels, so Air Tank is completely optional now and
mostly needed when you need RCS thruster.

### RCS thrusters

They are now available earlier in tech tree and consume reasonable
amount of air (5 times more than human jetpacks), and they don't work
without Mounted Air Tank, unless it's an Ion thruster variant.

### Mounted Air Tank

Available from the basic mech research node and can be printed in fab.
Built model comes empty, and syndicate mechs come with one full of
oxygen.

<img alt="GrFDrH5Hwe"
src="https://github.com/tgstation/tgstation/assets/3625094/b677b705-bda0-4c8c-96c7-d32bf7bf9f28">

Can be switched to pressurize or not pressurize the cabin. Releases gas
only when the cabin is sealed shut. Starts releasing automatically, but
can be toggled to not release if you want to use it just as a portable
canister.

Cabin pressure can now be configured in the module UI instead of
Maintenance UI.

Can be attached to a pipe network when the mech is parked above a
connection port.

Comes with a pump that works similarly to the portable pump. It lets you
vent the air tank contents outside, or suck air from the room to fill
the air tank. Intended to provide an ability to fill the air tank
without the need to bother with pipes.

Also has gas sensors that display gas mix data of the tank and the cabin
(when sealed).

### Stock part changes

All mechs now require a servo motor and they reduce mech movement power
consumption instead of scanning module.

Scanning modules are optional for mech operation (still required to
build) and the lack of one disables the following UI elements:

- Display of mech integrity (you can still see the alerts or examine the
mech to get rough idea)
- Display of mech status on internal damage (and you can't repair what
you can't diagnose)

The rating of scanning module doesn't have any effect as of now.

Cargo mech comes without it roundstart.

<img alt="2vDtt99oqb"
src="https://github.com/tgstation/tgstation/assets/3625094/147144ca-824e-4501-acf5-6ee104f309e7">

Capacitors now also reduce light power usage and raise the overclocking
temperature thresholds (see below).

### Maintenance

Maintenance UI removed, and its logic migrated to other places.

Access modification now managed inside the mech, and anyone who can
control the mech, can adjust the access in the same way as they can set
DNA key.

To open the maintenance panel you just need a screwdriver. It is instant
when the mech is empty and it has a 5 second delay when there is an
occupant to avoid in-combat hacking and part removal. It will alert the
occupant that someone is trying to tinker with their mech.


![image](https://github.com/tgstation/tgstation/assets/3625094/1abfca3c-8ba9-44b0-913c-c209564b91fd)

Once the panel is open, you can see the part ratings:


![image](https://github.com/tgstation/tgstation/assets/3625094/404f95bb-9f74-4e5b-a975-5ab6f74bdfa9)

With open panel you can hack the mech wires (roboticists can now see
them):

<img alt="mj205G2qDa"
src="https://github.com/tgstation/tgstation/assets/3625094/44cea0d1-44b4-4b50-b1d3-a97c0056bab3">

There are wires for:
- Enabling/Disabling ID and DNA locks
- Toggling mech lights
- Toggling mech circuits malfunction (battery drain, sparks) 
- Toggling mech equipment malfunction (to repair after EMP or cause
EMP-like effect, disarming mech)
- 3 dud wires that do nothing

The hacker may be shocked if the mech power cell allows.

When the panel is open and the user has access to the mech, they can
remove parts with a crowbar:

<img alt="jR40gyTWtJ"
src="https://github.com/tgstation/tgstation/assets/3625094/b573f5b9-b8ea-412e-b3e0-c872e01e0c23">

Hitting the mech with an ID from outside now toggles the ID Lock on/off
if the ID has sufficient access.

### Power consumption and overclocking

Rebalanced mech power consumption. T4 parts were not working in
Syndicate Mechs, as their effect was not calculated until you manipulate
parts manually. Constructed mechs with t1 parts even had their energy
drain reduced with upgrade to t1.

Now all mechs apply their base step power usage correctly don't ignore
the stock parts.

Servo tier now reduces base power consumption by 0% at t1, 50% at t2,
33% at t3 and 25% at t4
Capacitor tier now reduces base power consumption of mele attacks,
phasing and light by the same amounts.

Gygax leg actuators overload replaced with mech overclocking. Any mech
can be overclocked by hacking wires, but only Gygax has a button for
toggling it from the Cabin.

Now there is an overclock coefficient. 1.5 for Gygax and other mechs, 2
for Dark Gygax.

When overclocked, mechs moves N times faster, but consumes N times more
power.


![image](https://github.com/tgstation/tgstation/assets/3625094/01e285fd-6fd6-4558-8277-2ed3abf474d8)

While overclocked, mech heats up every second, regardless of movement,
and starts receiving internal and integrity damage after a certain
temperature threshold. The chance is 0% at the threshold, and 100% at
thresholds * 2. The roll happens every tick. Capacitor upgrades this
threshold, letting you overclock safely for longer periods.


![image](https://github.com/tgstation/tgstation/assets/3625094/80d90cea-0d20-4054-9369-a47deb6f52f2)

When you stop overclock, the temperature goes back down.

### Other changes and fixes

Concealed weapon bay now doesn't show up when you examine the mech, so
it's actually concealed now.

New radio module can properly change its frequency, as it didn't work
for previous radio.

Launcher type weapons were ignoring cooldowns and power usage, so you
could spam explosive banana peals, while they should have a 2 second
cooldown:
<img alt="q5GjUsHwGr"
src="https://github.com/tgstation/tgstation/assets/3625094/d102725d-e9e1-4588-9d6c-b9e38b7a6535">

Now this is fixed and all launcher type weapons properly use power and
have their cooldowns working.
And now they have the kickback effect working (when it pushes you in the
opposite direction in zero gravity on throw).

Thermoregulator now heats/cools considering heat capacity instead of
adding/reducing flat 10 degrees. So you can heat up cabin air quicker if
the pressure is low.

There were some other sloppy mistakes in mech code, like some functions
returning too early, blocking other functionality unintentionally. Fixed
these and made some other minor changes and improvements.

## Changelog

:cl:
refactor: Refactored Mech UI
refactor: Refactored mech radio into a utility module, adding extra slot
to all mechs
refactor: Refactored mech air tank into a utility module with an air
pump, adding extra slot to all mechs
refactor: Refactored mech cabin air - there is now a button to seal or
unseal cabin to make it airtight or exchanging gases with the
environment
refactor: Removed mech maintenance UI Access is set in mech UI, and
parts are ejected with a crowbar
add: Mech now has wires and can be hacked
qol: Roboticists now can see MOD suit and mech wires
add: Mechs now require servo motor stock part and it affects movement
power usage instead of scanning module
add: Scanning module absence doesnt block mech movement and hides some
UI data instead. Big Bess starts without one.
qol: Hitting mech with ID card now toggles ID lock on/off if the card
has required access
fix: Fixed concealed weapon bay not being concealed on mech examine
fix: Fixed mech radio not changing frequency
fix: Fixed mech launcher type weapons ignoring specified cooldown
fix: Fixed mech launcher type weapons not using specified power amount
fix: Fixed mech temperature regulator ignoring gas heat capacity
fix: Fixed mech stopping processing other things while not heating
internal air
fix: Fixed mech being able to leave transit tube in transit
fix: Fixed mech internal damage flags working incorrectly
fix: Fixed Gygax leg overloading being useless
fix: Fixed mechs ignoring their stock parts on creation. Syndicate mechs
now stronger against lasers and consume less energy on move. Upgrading
from tier 1 to tier 2 doesn't make mech consume MORE energy than before
the upgrade.
balance: Rebalanced mech energy drain with part upgrades. Base energy
drain reduced by 50%, 33%, 25% with upgrades and applies to movement
(Servo rating), phasing, punching, light (Capacitor rating).
balance: Hydraulic clamp now can force open airlocks
balance: Made mech RCS pack consume reasonable amount of gas
code: Fixed some other minor bugs and made some minor changes in the
mech code
/:cl:

---------

Co-authored-by: SyncIt21 <110812394+SyncIt21@users.noreply.github.com>
Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>
Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[1ea79a2ed8...](https://github.com/realforest2001/forest-cm13/commit/1ea79a2ed836ef4d20db511485c2f935304bfd55)
#### Monday 2023-08-21 14:22:43 by Ben

Zombie Rework (#4060)

# About the pull request

The goal for this PR is to rework zombies into being a fast and
numerous, but weaker, entity. As it stands a zombie has too many
advantages where a hold against them is essentially a fool's errand.

CURRENT PLAN (Will adjust as needed)
Zombies will be FASTER but much weaker than current iteration, with
weaker attacks. They will be designed around being a foe that can be
taken down quicker but if they close the distance, the threat of
infection spells a death sentence.

# Explain why it's good for the game

This will be hard to balance, and as such will be taking feedback before
I submit this for review. This is current position of Zombies:

- Tough: Extreme (25% ?!) brute modifier, with fire modifier on top,
making them very tanky and requiring clips to take down one
- self-revive: They WILL come back up, coupled with toughness, they are
a feared opponent.
- Strength: Claws inflict superslow at 40 brute damage, one of the
highest damage levels.
- Numerous: They have the numbers to put lesser drones and even entire
hives to shame

Overall, they are very overtuned and makes playing against them not that
fun. My plan is to have it so they are much weaker, with their threat
being from infections.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
balance: Zombie attacks deal less damage and only slow down targets (not
superslow as they currently do)
balance: Zombie resistances have been reduced heavily, making them far
more susceptible to brute damage. Their speed has been doubled to
compensate
balance: Black goo on tiles now requires you to not wear shoes to have
chance for infection
fix: Zombie attacks now only apply effects such as slow and infection if
the attack is valid (if the zombie is able to attack)
/:cl:

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[f6dbcd063d...](https://github.com/TaleStation/TaleStation/commit/f6dbcd063da8b330bde07c76fd98a14beb318063)
#### Monday 2023-08-21 14:38:45 by TaleStationBot

[MIRROR] [MDB IGNORE] Reflavors the Mosin to be a surplus rifle from the past IC 200 years, rather than from 670 years ago in game. Allergy warning: May contain microscopic silverscale buff (#7332)

Original PR: https://github.com/tgstation/tgstation/pull/77169
-----
## About The Pull Request

As the beautiful title may imply:

The Mosin-Nagant rifle has been reflavored into something _slightly_
more modern for the setting (The game currently takes place in 2563 you
know). Rather than a gun made in 1891 ending up in the hands of cargo
techs 670 years in the future, instead aspiring revolutionaries,
larpers, and eastern europeans in general will be seen arming themselves
with something at least a few hundred years more modern.

<details>
<summary>The Sakhno Precision Rifle, the new Nagant</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/82386923/d26d0bd6-344e-40a2-879c-303b948ce9bd)

"A Sakhno Precision Rifle, a bolt action weapon that was (and certainly
still is) popular with frontiersmen, cargo runners, private security
forces, explorers, and other unsavoury types. This particular pattern of
the rifle dates back all the way to 2440."

</details>

<details>
<summary>The Sakhno M2442 Army, surplus power</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/82386923/eabcd880-3b0e-4582-a306-000b2e46f4af)

"A modification of the Sakhno Precision Rifle, _Sakhno M2442 Army_ is
stamped into the side. It is unknown what army this pattern of rifle was
made for or if it was ever even used by an army of any sort. What you
can discern, however, is that its previous owner did not treat the
weapon well. For some reason, there's moisture all through the
internals."

</details>

<details>
<summary>The Sakhno - Zhihao Sporting Rifle, weapons for the
rich</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/82386923/f7e2b6d8-0346-4376-9673-43e405b88a17)

"An upgrade and modernisation of the original Sakhno rifle, made with
such wonders as modern materials, a scope, and other impressive
technological advancements that, to be honest, were already around when
the original weapon was designed. Surprisingly for a rifle of this type,
the scope actually has magnification, rather than being decorative."

</details>

<details>
<summary>The Lionhunter and Enchanted Bolt Action</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/82386923/1557cd36-f7ca-4fb9-b1a2-49f07c24af0a)

Because it wouldn't make sense for heretics and wizards to be summoning
brand new military green bolt action guns, some wood-like and
significantly fancier looking variations of the sprite now exist for
both of the guns.

</details>



</details>

<details>
<summary>How these look in game:</summary>
<br>


![image](https://github.com/tgstation/tgstation/assets/82386923/aaed7e56-4c0c-406c-bfc9-6188b9231f26)


</details>

## Why It's Good For The Game

<details>
<summary>See a before and after:</summary>
<br>

The sprites on the left of the arrow are what they are now, and the
sprites on the right are what they will turn into, note that there's one
old sprite to several new sprites, this is because guns that were
represented by the same sprite before now have their own unique looks.

These are subject to be slightly different than what you see here, but
will be more or less like these images.


![image](https://github.com/tgstation/tgstation/assets/82386923/73acecb5-e16c-43c2-b690-e1240e3cd06c)


![image](https://github.com/tgstation/tgstation/assets/82386923/188f6de3-1f89-4c26-9e12-2c5a3bffcdbf)


![image](https://github.com/tgstation/tgstation/assets/82386923/c3f7a4da-f4b3-4864-8bf6-314c84ac528a)


![image](https://github.com/tgstation/tgstation/assets/82386923/5a64327c-de63-44cf-9b02-7e90d80a753a)

</details>

While I understand the appeal of wanting a shitty, old rifle to have in
the game for everyone's surplus needs, the Mosin (and a good few other
guns too, looking at you 1911) is just a fair bit too old in my book.
About 670 years old. I find it more believable that while there would
still be some shitty surplus weapon that cargo techs and larpers would
non-stop fawn over, it'd be something that's old by the standards of the
year 2563 where the game takes place, vs old by the standards of 2023.

I think it'd greatly help the sense of the fact that we exist many
hundreds of years in the future if we stop using guns made before the
first world war.

## Changelog
:cl:
image: The Mosin-Nagant has been given new sprites and a reflavor,
looking for the old rifle? Look for the Sakhno Precision Rifle.
balance: The tiniest balance thing, but since Silverscales use the
Sakhno-Zhihao rifle, which has a scope on it, their main weapon now has
a scope.
sound: The cargo rifle now has a new, considerably more rifle sized
firing sound. Gotten from tgmc from
https://github.com/tgstation/TerraGov-Marine-Corps/pull/12280.
/:cl:

---------

Co-authored-by: Paxilmaniac <82386923+Paxilmaniac@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[0b4398a856...](https://github.com/TaleStation/TaleStation/commit/0b4398a8562b5880f5fb56e7fe12e1ae464e9cd4)
#### Monday 2023-08-21 14:38:45 by TaleStationBot

[MIRROR] [MDB IGNORE] Basic Watchers & Basilisks (#7361)

Original PR: https://github.com/tgstation/tgstation/pull/77630
-----
## About The Pull Request

This one is a double feature because Watchers and Basilisks share the
same typepath. You might see a couple more of those.
As is tradition I decided to fuck with them rather than just port them.
Here's what's up.

**Basilisks**

![image](https://github.com/tgstation/tgstation/assets/7483112/9e4b0115-65dd-4df7-b62a-21c7be8549bf)

![image](https://github.com/tgstation/tgstation/assets/7483112/59162e68-7d73-4659-9531-5078ff751228)

- Have a new soulless sprite which looks less like a living blue hedge.
- Walk at you and shoot you while you are not in range (just like
before).
- Become supercharged if they become "heated" by lava, lasers, or
temperature weapons. This was a feature they also previously had but
they would never encounter lava, so now it also works if you use the
wrong gun on them.
- Lose their supercharge if you cool them down.
- Otherwise pretty normal mobs.

**Watchers**

https://www.youtube.com/watch?v=kOq_Bf78k5A
Here's a traditional video of me intentionally getting hit by mechanics
(trust me its definitely on purpose)

- They glow emmissively a little bit so you can see them from further
away.
- Their eyes light up about 0.5 seconds before they are able to shoot at
you.
- No longer melee attack, instead try to stay out of melee.
- Will occasionally put you into "Overwatch", meaning they will shoot
you rapidly if you move or act while they're staring at you for a brief
time period (after which you become immune for 12 seconds, and during
which other watchers will play fair and stop shooting at you).
- If they start taking damage they will also start using their "Gaze"
attack, look away or suffer some kind of negative effect!
- - Normal watcher gaze flashes and confuses you.
- - Magmawing watcher gaze obviously burns (and briefly stuns) you.
- - Icewing watcher gaze freezes you and throws you backwards.
- Magnetically attract and eat diamonds. They also used to do this, but
just if they happened to coincidentally walk past some.

**Other accompanying changes**

All basic mobs will now adopt the "stop gliding" trait if they get
slowed down too much.
I moved behaviour for "fire a projectile from this atom" into a helper
proc because I was using it in three places and I will probably use it
in more places. There are probably other places in the existing code
which could be using this.
I think I made the basic mob melee attack forecast default a little more
forgiving, they were fucking me up too much and I am the playtester.

## Why It's Good For The Game

Another one off the list.
New tricks for old dogs.
Framework for making mobs with ranged attacks "fairer" (you can see when
they are ready to shoot you).
More (hopefully) versatile AI behaviours which we will reuse later (I
hope I'm not duplicating one someone already made).
If our players "enjoy" them enough we can give more mobs "don't look at
me" mechanics.
Removes some soul sprites.

## Changelog

:cl:
refactor: Basilisks and Watchers now use the basic mob framework. Please
bug report any unusual behaviour.
sprite: Basilisks have new sprites.
add: Basilisks will go into a frenzy if heated by energy weapons or
temperature beams as well as by lava.
add: Watcher eyes will be illuminated briefly when they are ready to
fire at you.
add: Watchers can now briefly put you into "Overwatch" and penalise you
for moving while they can see you.
add: Wounded watchers will occasionally punish players who look at them.
balance: Unusual watcher variants are more likely to appear.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[3bc54e7869...](https://github.com/tgstation/tgstation/commit/3bc54e78697b1bf6845605028085f30cabed9d40)
#### Monday 2023-08-21 14:56:12 by Jacquerel

Mining mob tweaks (#77763)

## About The Pull Request

~~I wanted to do this after #77700 (wow cool numbers) but nobody has
merged it yet despite how simple it is so i'll just hope they don't
conflict.~~ Thanks san

I'm fucking about with mining mobs with the intention of making them
more interesting but not necessarily towards making mining _harder_, but
some of these changes unquestionably have done so.

These changes are mostly in response to feedback about Watchers who are
definitely significantly more threatening than previously, although some
of this is user error.

- Watchers are annoying when traversing lavaland because they use their
ability on you instantly upon acquiring a target, if you are trying to
escape other fauna this quickly becomes deadly.
- A lot of players don't really realise what the overwatch ability is
actually doing and so just complain about getting machine gunned.
- If you _do_ react properly to the ability it still makes fighting them
take a lot longer than it used to.
- The "look away" icon is hard to see in the dark sometimes

To ammeliorate these factors I have:

- Reduced watcher health by ~20%
- Display an alerted graphic over the head of the watcher every time you
trigger the overwatch.
- Multiple watchers now won't overwatch you at the same time (this made
the "penalty" volley essentially become instant death)
- The "look away" icon is rendered above the lighting plane so you can
always see it
- Added a new component which tracks how long a mob has had a specific
target.
- - Watchers will now only Overwatch you if they've seen you for at
least 5 seconds (usually they'll try and shoot at you twice before
this).
- - Goliaths will only tentacle you if they've seen you for at least 3
seconds.

If overwatch is still problematic after this I guess I can just nerf it
to not track movement at all and only respond to attacks.

## Why It's Good For The Game

I don't want to discourage miners from "actually mining" by having them
get sniped just for walking around and the added time-to-kill on these
guys could make clearing tendrils more tedious too.

## Changelog

:cl:
balance: Watchers have less health
balance: You can't be overwatched by several watchers at a time
balance: Watchers won't overwatch you instantly upon seeing you
balance: Goliaths won't launch tentacles at you instantly upon seeing
you
/:cl:

---
## [nikothedude/tgstation](https://github.com/nikothedude/tgstation)@[2d4d23dbf1...](https://github.com/nikothedude/tgstation/commit/2d4d23dbf1e2cc23ed2046534011561e443060f7)
#### Monday 2023-08-21 15:01:25 by Timberpoes

Replaces the poster and graffiti objectives with assault and early steal & destroy ones. (#77029)

## About The Pull Request

With the blessings of @Watermelon914 I am removing the two objectives
for placing posters and spraying graffiti.

These old objectives are not dead. Their items have moved to the
Badassery section of the uplink.

A box of 3 demotivational posters can be bought for 1TC with 0 rep.
The spraycan can be bought for 1TC with 0 rep.

In their place comes one new objective and one extended objective.

The new objective is Assault a Crewmember. This objective requires you
to attack the specified target 2-5 times (random on objective
generation). It tallies from any attack that filters through the
`/datum/element/relay_attackers` element and has an "attacker"
associated with it.

Although it asks you not to kill the other player, it doesn't fail if
you kill them.

I have expanded the low-risk theft objectives with items like a mime
mask, lawyer badge and a fake moustache (commonly on cooks).

Finally, I've added a very low level set of steal-and-destroy objectives
aimed at some items that will require a bit of basic breaking and
entering, and the destruction of which may hurt crew morale.

```
/datum/objective_item/steal/traitor/donut_box
/datum/objective_item/steal/traitor/rpd
/datum/objective_item/steal/traitor/space_law
/datum/objective_item/steal/traitor/granted_stamp
/datum/objective_item/steal/traitor/denied_stamp
/datum/objective_item/steal/traitor/lizard_plush
/datum/objective_item/steal/traitor/moth_plush
/datum/objective_item/steal/traitor/insuls
```

This PR also fixes clown shoes missing a proc override to allow them to
actually register as a theft objective.


![image](https://github.com/tgstation/tgstation/assets/24975989/775d46cf-f40a-43e5-9bf1-3aa4a31d436e)

![image](https://github.com/tgstation/tgstation/assets/24975989/66c77815-1f2b-4dfb-99c6-b8f2e0061654)

![image](https://github.com/tgstation/tgstation/assets/24975989/85d3878a-c598-4ec0-9bb1-920380a004c6)
## Why It's Good For The Game

Basically my discussion with Watermelon focused on the idea that the
graffiti and poster objectives weren't really crimes. They baited
antagonists into very passive play early-game.

These new replacements encourage a more antagonistic playstyle. Starting
fights plus B&E are two bread-and-butter play paradigms for antaggery.

Giving a few early game theft + destroy options with a mix of impactful
items (like insuls and RPDs) versus more symbolic or emotive items
(plushies, donut boxes, Cargonia stamps) gets antagonists out and about
in the station, warming themselves up.

And having an objective to assault players (even if you don't kill them)
allows cheeky antags with a penchant for shittery to start fights with
players and start genuinely impacting the shift, involving sec and
drawing players into their antaggery.

Both of these natually ease players into the more substantive theft and
murder objectives.

The existing spray and posters are actually thematically super cool.
Traitors now have even more access to them since they can be bought for
1TC per spraycan/3-pack of posters. This lets antags with TC to spare
run gimmicks around them and adds extra fun to the Badassery section.
## Changelog
:cl:
del: Traitor objectives to place posters and graffiti the station have
been removed.
add: The items associated with the poster and graffiti objectives can
now be purchased from the Badassery section of the uplink. The posters
come in a box of 3 for 1TC, and the spraycans are 1TC each.
add: Adds a new Assault traitor objective, requiring you to the attack
the target a few times without needing to kill them. Earn TC and
reputation by starting barroom fights and bait players into escalation
battles for fun and profit.
add: Expands low-risk steal objectives to include the Chef's fake
moustache, Lawyer's badge, and Mime's mask.
add: Adds brand new shift start Steal & Destroy objectives for early
breaking and entering. Smash your way into a sec checkpoint to grab a
Space Law book, engineering to grab some insulated gloves or the psych
office to kidnap their moth plush.
fix: Fixes an issue where the steal clown shoes objective would never be
valid.
/:cl:

---
## [Levi-cell/PythonZero](https://github.com/Levi-cell/PythonZero)@[dae9bdb2a1...](https://github.com/Levi-cell/PythonZero/commit/dae9bdb2a1d48d62c8ea7960216ad6accfebe334)
#### Monday 2023-08-21 15:10:36 by Edcarlos

Create README.md

--------------------------PORTUGUESE-----------------------

Seja bem vindo ao PythonZero!!

Aqui há 13 módulos, do módulo 1 ao 13 você poderá analisar toda minha evolução de forma detalhada. Cada módulo terá um readme, vale lembrar que esses módulos nem sempre foram organizados porém apartir de um certo momento consolidei tanta prática e conhecimento que conseguir fazer uma boa organização, revisei tudo do módulo 1 ao 13, então será fácil de você entender!! A maioria dos códigos desse curso é para viéis de aprendizado porém alguns códigos realmente foram desafiadores o suficinete para serem dignos de ter uma readme hahaha.

Do módulo 1 ao 3, minha dedicação foi tanta que os módulos 4 ao 9 foram extramamente fáceis, graças a desafios que eu mesmo me atribui adquiri a habilidade de pesquisa vasculhando cada canto da internet e cada pessoas que pudesse fazer network, e sem saber já estava estudando assunstos de outros módulo hahaha. Porém apartir do módulo 10 me deparei com assunstos bem interessantes como Threads que na maioria das vezes se trata de diminuir o tempo de execução  de um software que recebe um alto volume de dados, uma execução paralela é necessária para aumentar a produtividade, não há nada pior do que ficar vários segundos olhando para tela enquanto espera o software responder hahaha, mas claro.... tudo depende do seu objeto e implmentação meu mentor sempre deixou claro que uma importante habilidade no mundo profissional é a de Interpretação!!

Em todos os módulos você encontrará o interpretador de cada código, encontrará o material de estudo e o guia de estudo, também uma pasta com os slides e PDFs, outra pasta para tarefas, e uma última pasta para uma tarefa extra

Perceba que temos duas pastas extras uma é o NewRestaurant, ele é a versão final de um projeto, bem interessante por sinal, e outra é uma pasta dedicada ao um código de lógica de uma das aulas ao vivo que tive.

Do modulo 10 ao 13 sou apresentado a assuntos que irei aprofundar no PythonPro, não perca!!

Enfim :), fique a vontade para explorar!!


------------------------ENGLISH--------------------------

Welcome to PythonZero!!

Here there are 13 modules, from module 1 to 13 you will be able to analyze all my evolution in detail. Each module will have a readme, it is worth remembering that these modules were not always organized but after a certain moment I consolidated so much practice and knowledge that I managed to do a good organization, I reviewed everything from module 1 to 13, so it will be easy for you to understand!! Most of the code in this course is for learning purposes but some code was really challenging enough to be worthy of a readme hahaha.

From module 1 to 3, my dedication was so great that modules 4 to 9 were extremely easy, thanks to challenges that I myself gave myself, I acquired the research skill by scouring every corner of the internet and every person I could network with, and without even knowing it I was studying subjects from other modules hahaha. However, starting from module 10, I came across very interesting subjects such as Threads, which most of the time is about reducing the execution time of a software that receives a high volume of data, a parallel execution is necessary to increase productivity, there is nothing worse than spending several seconds looking at the screen while waiting for the software to respond hahaha, but of course.... it all depends on its object and implementation my mentor always made it clear that an important skill in the professional world is Interpretation!!

In all modules you will find the interpreter of each code, you will find the study material and the study guide, also a folder with the slides and PDFs, another folder for tasks, and a last folder for an extra task

Notice that we have two extra folders, one is the NewRestaurant, it is the final version of a project, very interesting by the way, and another is a folder dedicated to the logic code of one of the live classes I had.

From module 10 to 13 I'm introduced to subjects that I'll delve into in PythonPro, don't miss it!!

Anyway :), feel free to explore!!

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[5f3de3897b...](https://github.com/vdaular-dev/linksfordevs/commit/5f3de3897b09dbc61ef47d500b45942c0abe3280)
#### Monday 2023-08-21 15:31:44 by Ben Dornis

Updating: 8/20/2023 11:00:00 PM

 1. Added: Sponsor based GitHub feature toggling · community · Discussion #46980
    (https://github.com/orgs/community/discussions/46980)
 2. Added: Two quick hacks for laptop in-flight Delta Wi-Fi with T-Mobile
    (https://blog.yossarian.net/2023/08/20/Two-quick-hacks-for-inflight-delta-wifi-with-tmobile)
 3. Added: I have no clue how to interview for data scientists
    (https://andrewpwheeler.com/2022/03/24/i-have-no-clue-how-to-interview-for-data-scientists/)
 4. Added: Quick DBUS Fix
    (https://vermaden.wordpress.com/2023/08/19/quick-dbus-fix/)
 5. Added: How Surround Sound for Headphones Works
    (https://hajo.me/blog/2014/12/28/how-surround-sound-for-headphones-works/)
 6. Added: Ruby's Hash is a Swiss-Army Knife
    (https://www.akshaykhot.com/ruby-hash-is-a-swiss-army-knife/)
 7. Added: A 40 lines app needs 40 files
    (https://thomassimon.dev/ps/2)
 8. Added: I Like You But You’re Not Yet My Friend. What Do We Call Each Other? A Struggle to Replace “Acquaintance” With Something Better.
    (https://hunterwalk.com/2023/08/19/i-like-you-but-youre-not-yet-my-friend-what-do-we-call-each-other-a-struggle-to-replace-acquaintance-with-something-better/)
 9. Added: My Favourite Development Books
    (https://ijrussell.github.io/posts/top-10-books/)
10. Added: Calm tech - Nicolas Bouliane
    (https://nicolasbouliane.com/blog/calm-tech)
11. Added: SponsorLink: feedback and moving forward
    (https://www.cazzulino.com/sponsorlink-feedback.html)
12. Added: How I turned Local Storage into a Web Socket
    (https://alemtuzlak.hashnode.dev/how-i-turned-local-storage-into-a-web-socket)
13. Added: Breaking The Mutant Language's "Encryption"
    (https://eval.blog/breaking-the-mutant-languages-encryption)
14. Added: Bleeding Edge Technology is Made for Silly Art
    (https://www.bramadams.dev/202308192019/)

Generation took: 00:08:16.0963580

---
## [deandreamatias/GitJournal](https://github.com/deandreamatias/GitJournal)@[f24740ea3a...](https://github.com/deandreamatias/GitJournal/commit/f24740ea3a5a0095703ba6c6e7c4274492f964f3)
#### Monday 2023-08-21 15:33:04 by Vishesh Handa

SortedNotesFolder: Fix binary search

I can't remember why I implemented this myself instead of using a
standard implementation and avoiding idiotic bugs like this.

Fixes #172

---
## [afirpo/tgstation](https://github.com/afirpo/tgstation)@[b0ec1e4098...](https://github.com/afirpo/tgstation/commit/b0ec1e4098ed80fdb0bac69c6f950bd5e38012b8)
#### Monday 2023-08-21 15:37:10 by Jacquerel

[no gbp] Adds missing chat feedback to watcher abilities (#77700)

## About The Pull Request

I kept meaning to add this in my last PR and kept thinking "I'll add
that in with these review changes" and then forgot every time. This
should make it clearer what is happening to you and why.

Also I made the gaze ability stun the user for a short period after it
goes off because them shooting you instantly after they stop channeling
_is_ sort of bullshit.
Also while testing this I noticed the AI interrupt one of its actions to
do the other one which is a bit silly so now it cannot do that.

## Why It's Good For The Game

Outlines in the log why something bad just happened to you.

## Changelog

:cl:
qol: Added some textual feedback to new watcher abilities
balance: Watchers will not attack for a short period following their
gaze attack
fix: Watchers won't interrupt one ability to use the other one
/:cl:

---
## [liuy/cformer](https://github.com/liuy/cformer)@[e469481ce3...](https://github.com/liuy/cformer/commit/e469481ce3082a9ef88d5ec7e06836147c918577)
#### Monday 2023-08-21 15:48:11 by Liu Yuan

net: add reset_hidden_state() to reset hidden state of RNN layer

now we can generate new text from the trained model!

Loading data...32548 training samples, 0 test samples (Used 0.4s)

Sequential Network:
+-------+---------+-------+--------+------+------------+------------+
| Layer | Name    | Input | Output | Bias | Activation | Parameters |
+-------+---------+-------+--------+------+------------+------------+
| 0     | Embed   | 2876  | 1000   | None | None       | 2876000    |
| 1     | RNN     | 1000  | 1000   | Yes  | None       | 2002000    |
| 2     | Linear  | 1000  | 2876   | Yes  | LogSoftmax | 2878876    |
+-------+---------+-------+--------+------+------------+------------+
Total params: 7756876

...
| 98    | 4.9       | 0.47512734 | 0.91403633 |
| 99    | 4.9       | 0.46073234 | 0.91761124 |

Total time 493.9s, RNN Train accuracy: 0.9194

Text generated:

You we the reins, to earn him to rage,
You should the ushers of the state was touch'd,
They would you think it folly
To keep your great pretences veil'd till when
They needs of the state.

BRUTUS:
Let them go on;
This mutiny with the belly smile
As the fairness of the south light on the gown, stand naked our mind: away!

COMINIUS:
Breathe you talk them in authority, and your patience,
If you curse them as enemies.

First Soldier:
Care you so? Which way I carry to be their words: 'we did request you have issued,
And make bold lord. You talk of pride: O that you have lately to the people, there was
never a worthier man.
Here he comes, and if the world
Were feverous of thy sounds, follows it that I am known
well enough too? what barm can your bisson
conspectuities glean out of this character, and thus answer'd:
'True is it, my incorporate came
That Ancus Marcius, Numa's daughter's son, who desires and cities of the night than with the forehead
And

Signed-off-by: Liu Yuan <namei.unix@gmail.com>

---
## [utziacre/android_kernel_oneplus_sm8250](https://github.com/utziacre/android_kernel_oneplus_sm8250)@[1071d73f4d...](https://github.com/utziacre/android_kernel_oneplus_sm8250/commit/1071d73f4d071a3fde6d268ab5eccbf65c37a4a5)
#### Monday 2023-08-21 15:57:14 by Peter Zijlstra

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
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[0f31d50b2f...](https://github.com/cockroachdb/cockroach/commit/0f31d50b2fd4de2980c294d47e87999f27e673c5)
#### Monday 2023-08-21 16:26:59 by craig[bot]

Merge #107110 #107111 #107129 #107149 #107181 #107183

107110: kvserver: avoid running intensive decommission test under deadlock r=AlexTalks a=AlexTalks

The kvserver test `TestDecommission`, which runs a 5-node cluster and decommissions 4 of those 5 nodes, has trouble completing fast enough when under a race or deadlock configuration. While race configurations were already skipped, this modifies the test to be skipped under deadlock configurations as well.

Fixes: #106096

Release note: None

107111: compose: start `docker-compose` with a non-empty `PATH` r=rail a=rickystewart

`docker-compose` invokes `docker`, but obviously this will fail if there is nothing in the `PATH`.

Epic: none
Release note: None

107129: dev: reject builds when CRL JS dependencies are 'pnpm link'ed r=rickystewart a=sjbarag

When working with first-party JS dependencies that aren't in this monorepo, the idiomatic development workflow uses pnpm link [1] to link multiple JS packages together. Specifically, running `pnpm link /path/to/github.com/cockroachdb/ui/packages/foo` from within pkg/ui/workspaces/* creates a symbolic link at
node_modules/`@cockroachlabs/foo` that points to
../../(…)/ui/packages/foo. This works quite smoothly for local development, as changes in the 'foo' package are automatically seen by a `pnpm webpack --watch` running in CRDB. The two packages act like they're maintained in the same repo, while allowing independent version history, CI processes, etc.

Unfortunately, rules_js currently offers no way to link outside of the Bazel workspace. Such a symlink is either ignored by rules_js (since it doesn't appear in pnpm-lock.yaml) or is rejected if it's manually added to the lockfile [2]. Allowing Bazel-based builds of CockroachDB when 'pnpm link'ed packages are present introduces dependency skew between Bazel and non-Bazel builds. To allow `pnpm link` to be used safely, pre-emptively reject builds of 'cockroach' and 'cockroach-oss' that are run through the 'dev' helper when linked `@cockroachlabs/` packages are detected.

[1] https://pnpm.io/cli/link
[2] https://github.com/aspect-build/rules_js/issues/1165

Release note: None
Epic: none

-----

Example output: 
<img width="998" alt="image" src="https://github.com/cockroachdb/cockroach/assets/665775/3fd43abe-f5c2-4ddd-bc60-16a73db12836">

Total duration is 16ms on my machine since we're checking so few files. We can drop these into a goroutine per first-party JS if we want, but this is certainly fast enough to be conversational.

107149: opt: make functional dependency calculation deterministic r=DrewKimball a=DrewKimball

We recently added additional logic for inferring functional dependencies for join expressions. However, this logic iterates through a map, which leads to nondeterminism in which order functional dependencies are added to the FD set. Functional dependency calculation is best-effort, so this can lead to a different resulting FD set, which causes flaky tests. This patch makes the calculation deterministic by iterating instead through a `intsets.Fast` set.

Fixes #107148
Fixes #107162

Release note: None

107181: dev: when cross-building, use `-c opt` r=rail a=rickystewart

This enables optimizations which you probably want for a cross-build.

Epic: CRDB-17171
Release note: None

107183: acceptance: add log dir as a writable path r=rail a=rickystewart

Otherwise you get a sandbox error.

Epic: CRDB-17171
Release note: None

Co-authored-by: Alex Sarkesian <sarkesian@cockroachlabs.com>
Co-authored-by: Ricky Stewart <ricky@cockroachlabs.com>
Co-authored-by: Sean Barag <barag@cockroachlabs.com>
Co-authored-by: Drew Kimball <drewk@cockroachlabs.com>

---
## [facebook/sapling](https://github.com/facebook/sapling)@[260847304b...](https://github.com/facebook/sapling/commit/260847304bbd1c5303a9df5f7465dd07d8577618)
#### Monday 2023-08-21 16:31:49 by Gustavo Galvao Avena

Create gitexport CLI

Summary:
Creating an initial version of the gitexport CLI (for more context on why we need it, see T160586594).

This tool is supposed to take a repo and a list of paths as input and it should export all the history of those paths in a git repo.

## What does it do now?
Currently, this binary doesn't do anything useful. it just gets the history of a single path to be exported and prints their changeset ids and commit messages (for manual debugging).

The main point of this diff is to **set most of the structure/flow of the tool to get some early feedback** before I start implementing anything more complex.

Most of the functions don't have an actual implementation, but just do something simple (e.g. returning the first element of a vector) so it typechecks.

## What's my current plan?
1) Get the history of all the given paths. (This is mostly done in this diff already)
2) Merge the changesets into a single, topologically sorted, list of changesets
3) Strip irrelevant changes from every commit (T161205476).
4) Create a CommitGraph from this list (T161204758).
5) Export that CommitGraph to a new, temporary, Mononoke repo (T160787114).
6) Use existing tools to export that temporary repo to a git repo (T160787114).

The tricky bits are steps 2,3 and 4, which is where I expect to spend most of my time.

First, I'm not sure if event to create a CommitGraph at all, to be able to export the processed changesets to a new repo. If I do need to, I'm not sure if I should (a) strip the irrelevant file changes before or after creating the graph and (b) how to create a new repo and populate it with the commits from the graph I created. (b) is more of a implementation detail, so I don't worry about now...

The main unknowns for me are #2 and #4. Basically, how can I create a proper commit graph from a set of commits that are not direct descendants of each other. Assuming a linear history, I don't think it would be very complicated, but we also have to support branching, so I'm not sure how to do this efficiently...

## Examples
Let me put as simple example below. Commits with uppercase letters are relevant (i.e. should be exported) and lower case letters should now.

```
A -> b -> C -> D -> e
|-> f -> G
```

In this case, I want to have the following commit graph in the end:
```
A' -> C' -> D'
|-> G'
```
where X' is X stripped of irrelevant changes

## RFC
- This is my first Rust diff ever, so please LMK what horrible things I'm doing, bc I'm very likely doing a few 😂
- Does the plan I described above make sense?
- Any suggestions/ideas on how to efficiently stitch the changesets together would be appreciated! But I'll probably set up some time to discuss this problem specifically once I spend more time thinking about it...

## Next steps
- Implement steps #5 and #6 (T160787114) to get the entire E2E solution working with the simplest case (i.e. one path with linear history). This is basically exporting the commit graph to a git repo (maybe through a temporary mononoke repo).
  - Update integration test case to actually run and test the tool with the simple case.
- Figure out how to properly create a commit graph from a list of changeset lists.
- Add test cases for multiple paths and edge cases, like having multiple branches.

Reviewed By: RajivTS

Differential Revision: D48226070

fbshipit-source-id: eed970a8e4697ab10682e3b93863e6d621adaacc

---
## [rd-stuffs/msm-4.14](https://github.com/rd-stuffs/msm-4.14)@[a240ee3e9c...](https://github.com/rd-stuffs/msm-4.14/commit/a240ee3e9c9ab3182caa4998b4e46c7513dbb748)
#### Monday 2023-08-21 16:54:08 by Yaroslav Furman

power/supply: Force disable frame pointers and optimize for size

Holy fucking shit this is so retarded, it doesn't boot with frame pointers
and this is possibly breaking the DS28E16 verification driver.

Signed-off-by: Yaroslav Furman <yaro330@gmail.com>
Change-Id: Ie3023c569516593d0224d416c95ada98efbc66d1
Signed-off-by: Richard Raya <rdxzv.dev@gmail.com>

---
## [Mission23/Mission23](https://github.com/Mission23/Mission23)@[6a9b4b1dbe...](https://github.com/Mission23/Mission23/commit/6a9b4b1dbe8b79e693f40221b548519de3a8ea30)
#### Monday 2023-08-21 17:05:48 by Micah

Create micah.journal

I’m that motherfucker, the answer to some prayers who will always put the real shit in here. 

So many inside jokes about unmodified, not changing, me always me, extensions—I don’t mind these extensions, only ones I use. Fake relationships, and the hypocrites surrounding me. Anyway. See my journal audio I’m putting one up called PsyOp to COVID-19, it will learn you something good. 

InB4 your writing sucks. You need to go back and look at the iceberg from the water’s surface upward if punctuation matters. I need all my troll enemies they hired to do two things: run and keeping looking down here for the shit the media won’t report. 

Lasers inbound. Uploading.

---
## [AyaShibbi/CODSOFT](https://github.com/AyaShibbi/CODSOFT)@[bc2c3d72d0...](https://github.com/AyaShibbi/CODSOFT/commit/bc2c3d72d0bcd2ae111ac46e9b6e4811d5b12e30)
#### Monday 2023-08-21 17:19:55 by AyaShibbi

Add files via upload

ATM Interface: 

Experience the convenience of the ATM Interface built in Java, a comprehensive project designed to replicate the functionalities of an Automated Teller Machine. Developed with user-friendliness in mind, this simulator encapsulates the essential features of an ATM, offering a seamless banking experience.

Features:
- Class-Based Architecture: The project encompasses classes representing the ATM machine, user interface, and bank account. Each component is thoughtfully designed for clear separation of concerns.
- Interactive User Interface: Crafted to emulate a real ATM experience, the user interface offers options for withdrawing, depositing, and checking the balance. Users can interact with the ATM seamlessly.
- Functional Methods: The project implements essential methods for each user option: withdraw(amount), deposit(amount), and checkBalance(). These methods ensure smooth transactions.
- Bank Account Class: A dedicated class represents the user's bank account, efficiently storing and managing account balances.
- Seamless Integration: The ATM class interacts with the user's bank account class, facilitating the seamless management and modification of account balances.
- Input Validation: To ensure data integrity, user inputs are meticulously validated to guarantee they fall within acceptable limits. This prevents unauthorized actions and enhances security.
- User-Centric Messages: Users receive informative messages based on their chosen options and the outcome of their transactions. Clear feedback enhances the user experience.


Usage:
1. Practical Banking: Offers a platform to practice and familiarize with banking operations safely.
2. Functional Learning: Ideal for hands-on learning in coding, UI design, and software integration.
3. Safe Exploration: Users can experiment with various transactions without affecting actual accounts.
4. Code Development: Developers can enhance skills in software architecture and implementation.
5. User-Centered Interaction: Provides positive and educational interaction, increasing confidence in real-life ATM usage.

Experience virtual banking with the ATM Interface. Whether you're a developer refining skills or an individual keen on understanding ATM operations, this project offers an immersive, educational, and practical experience. Elevate your software design and banking understanding today.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[66d90214ec...](https://github.com/treckstar/yolo-octo-hipster/commit/66d90214ec5fdc15bf0b83958c0bd2b04ea0d4fc)
#### Monday 2023-08-21 17:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [olebeck/gio](https://github.com/olebeck/gio)@[6ea4119a3c...](https://github.com/olebeck/gio/commit/6ea4119a3ceb36f009af1486e41b47f08c2239bd)
#### Monday 2023-08-21 17:50:40 by Chris Waldon

text,widget: [API] implement consistent, controllable line height

This commit ensures that any given paragraph of text shaped by Gio will use a single
internal line height. This line height is determined (by default) by the text size,
rather than the fonts involved. This is a breaking change, as previously we would
blindly use the largest line height of any font in a line for that line, leading to
lines within the same paragraph with extremely uneven spacing. This commit also
updates some test expectations in package widget.

I thought pretty hard about how to implement line spacing, and consulted a few sources:

[0] https://www.figma.com/blog/line-height-changes/
[1] https://practicaltypography.com/line-spacing.html
[2] https://developer.mozilla.org/en-US/docs/Web/CSS/line-height

There is no single, universal way to think about line spacing. Fonts internally specify
a line height as the sum of their ascent, descent, and gap, but the line height of two
fonts at the same pixel size (say 20 Sp) can vary wildy (especially across writing systems).
There are two strategies we could pursue to establish the line height of a paragraph of text:

- derive the line height from the fonts involved (our old behavior, and the behavior of
  many word processors)
- derive the line height from the requested text size provided by the user (the behavior of the
  web).

The challenge with the first option is that for a given piece of text in the UI, there can
be a silly number of fonts involved. If a label dispays user-generated content, the user can
put an emoji in it, and emoji fonts have different line heights from latin ones. This can cause
unexpected and nasty layout shift. Gio would previously do exactly this, on a line-by-line basis,
resulting in unevenly spaced lines within a paragraph depending on which fonts were used on
which lines. Choosing one of the fonts and enforcing its line height would make things consistent,
but it isn't clear how to choose that canonical font. There is no 1:1 mapping between the input
text.Font provided in the shaping parameters and a single font.Face. Instead, that mapping depends
upon the runes being shaped.

I think the only sane way to implement the first option would be to synthesize some text in the
provided system.Locale (mapping the language to a script and then generating a rune from that
script), shape that single rune, and then enforce the line height of the resulting face on the
entire paragraph. This would require doing a fair bit more work per paragraph than Gio does today,
so I've opted not to do it.

Instead, the second option allows us to choose a line height based on the size of the text that
the user wants to display. While this can potentially interact poorly with unusually tall fonts,
it means that text will always have a consistent line height.

I've provided two knobs to control line height:

- text.Parameters.LineHeight lets you set a specific height in pixels with a default value of
  text.Parameters.PxPerEm.
- text.Parameters.LineHeightScale applies a scaling factor to the LineHeight, allowing you to
  easily space out text without hard-coding a specific pixel size. The default value here
  (drawn from the recommendations of [1]) is 1.2, which looks pretty good across many fonts.

I've chosen this two-value API because many users will want to set one or the other value. I
considered instead a single value field and a "mode" that would specify how it was used, but
that felt uglier. Also, you *can* set both of these two fields and get predictable results.

I'd like to revisit using the line height of the chosen fonts in the future, but it seems a
little too complex to be worthwhile right now. An interesting option would be making the
select-a-face-using-locale strategy described above an opt-in feature, though some users
might instead want to just use the tallest line height among fonts in use. Something like
this Android API might be appropriate:

[3] https://learn.microsoft.com/en-us/dotnet/api/android.widget.textview.fallbacklinespacing?view=xamarin-android-sdk-13

I'd like to thank Dominik Honnef for some good discussion around this feature, and for pointing
me to some good sources on the subject.

Signed-off-by: Chris Waldon <christopher.waldon.dev@gmail.com>

---
## [BurgerLUA/Bubberstation](https://github.com/BurgerLUA/Bubberstation)@[a1609c4536...](https://github.com/BurgerLUA/Bubberstation/commit/a1609c4536fe05f95560bd1a1be4607b944ee5a5)
#### Monday 2023-08-21 18:31:59 by SkyratBot

[MIRROR] [NO GBP] Fixes clown car + deer collision  [MDB IGNORE] (#22709)

* [NO GBP] Fixes clown car + deer collision  (#77076)

## About The Pull Request

A not-so-long time ago I drunkenly coded #71488 which did not work as
intended.

I return now, in a state of reflective sobriety, to rectify that.

The clown car will now not only crash like it should, but will also
cause (additional) head injuries to some occupants and kill the deer on
impact.

Content warnings: **Animal death, vehicle collision, blood, DUI.**

https://github.com/tgstation/tgstation/assets/28870487/4889f452-7e49-4512-8cdd-e4e2a4d6b394
## Why It's Good For The Game

Fixes the product of a silly PR that never actually worked. Also gives
it a bit more TLC in the event that this joke actually plays out on a
live server.
## Changelog
:cl:
fix: Clown cars now properly collide with deer.
sound: Violent, slightly glassy car impact sound.
/:cl:

* [NO GBP] Fixes clown car + deer collision

---------

Co-authored-by: Rhials <28870487+Rhials@users.noreply.github.com>

---
## [libbpf/libbpf](https://github.com/libbpf/libbpf)@[b064c40d94...](https://github.com/libbpf/libbpf/commit/b064c40d9460c34d8fb539cf0042b298b888cdd4)
#### Monday 2023-08-21 20:27:47 by Daniel Borkmann

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
or both to cleanly co-exist where needed given its all one logical tc layer and
the tcx plus classic tc cls/act build one logical overall processing pipeline.

tcx supports the simplified return codes TCX_NEXT which is non-terminating (go
to next program) and terminating ones with TCX_PASS, TCX_DROP, TCX_REDIRECT.
The fd-based API is behind a static key, so that when unused the code is also
not entered. The struct tcx_entry's program array is currently static, but
could be made dynamic if necessary at a point in future. The a/b pair swap
design has been chosen so that for detachment there are no allocations which
otherwise could fail.

The work has been tested with tc-testing selftest suite which all passes, as
well as the tc BPF tests from the BPF CI, and also with Cilium's L4LB.

Thanks also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Acked-by: Jakub Kicinski <kuba@kernel.org>
Link: https://lore.kernel.org/r/20230719140858.13224-3-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [libbpf/libbpf](https://github.com/libbpf/libbpf)@[d7e583a6ea...](https://github.com/libbpf/libbpf/commit/d7e583a6eac64a79c21f1a749e6b3d371b884365)
#### Monday 2023-08-21 20:27:47 by Daniel Borkmann

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
applications coordinating internally about their attachments.

Both from Cilium and Meta side [2], we've collected the following requirements
for a generic attach/detach/query API for multi-progs which has been implemented
as part of this work:

  - Support prog-based attach/detach and link API
  - Dependency directives (can also be combined):
    - BPF_F_{BEFORE,AFTER} with relative_{fd,id} which can be {prog,link,none}
      - BPF_F_ID flag as {fd,id} toggle; the rationale for id is so that user
        space application does not need CAP_SYS_ADMIN to retrieve foreign fds
        via bpf_*_get_fd_by_id()
      - BPF_F_LINK flag as {prog,link} toggle
      - If relative_{fd,id} is none, then BPF_F_BEFORE will just prepend, and
        BPF_F_AFTER will just append for attaching
      - Enforced only at attach time
    - BPF_F_REPLACE with replace_bpf_fd which can be prog, links have their
      own infra for replacing their internal prog
    - If no flags are set, then it's default append behavior for attaching
  - Internal revision counter and optionally being able to pass expected_revision
  - User space application can query current state with revision, and pass it
    along for attachment to assert current state before doing updates
  - Query also gets extension for link_ids array and link_attach_flags:
    - prog_ids are always filled with program IDs
    - link_ids are filled with link IDs when link was used, otherwise 0
    - {prog,link}_attach_flags for holding {prog,link}-specific flags
  - Must be easy to integrate/reuse for in-kernel users

The uapi-side changes needed for supporting bpf_mprog are rather minimal,
consisting of the additions of the attachment flags, revision counter, and
expanding existing union with relative_{fd,id} member.

The bpf_mprog framework consists of an bpf_mprog_entry object which holds
an array of bpf_mprog_fp (fast-path structure). The bpf_mprog_cp (control-path
structure) is part of bpf_mprog_bundle. Both have been separated, so that
fast-path gets efficient packing of bpf_prog pointers for maximum cache
efficiency. Also, array has been chosen instead of linked list or other
structures to remove unnecessary indirections for a fast point-to-entry in
tc for BPF.

The bpf_mprog_entry comes as a pair via bpf_mprog_bundle so that in case of
updates the peer bpf_mprog_entry is populated and then just swapped which
avoids additional allocations that could otherwise fail, for example, in
detach case. bpf_mprog_{fp,cp} arrays are currently static, but they could
be converted to dynamic allocation if necessary at a point in future.
Locking is deferred to the in-kernel user of bpf_mprog, for example, in case
of tcx which uses this API in the next patch, it piggybacks on rtnl.

An extensive test suite for checking all aspects of this API for prog-based
attach/detach and link API comes as BPF selftests in this series.

Thanks also to Andrii Nakryiko for early API discussions wrt Meta's BPF prog
management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Link: https://lore.kernel.org/r/20230719140858.13224-2-daniel@iogearbox.net
Signed-off-by: Alexei Starovoitov <ast@kernel.org>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[37d8f6162b...](https://github.com/tgstation/tgstation/commit/37d8f6162bbef0c9cbeaf07cdba7cb93eb843e2a)
#### Monday 2023-08-21 20:54:14 by LukasBeedellCodestuff

Compact shotgun re-added (#77759)

## About The Pull Request

This pr seeks to re-add the compact shotgun (slightly buffed with 1 more
ammo) and buff up its larger brother the combat shotgun (with 2 more
ammo.)

## Why It's Good For The Game
With the recent laser buffs, there is a real possibility for the compact
shotgun to return as a unique weapon to make the HOS slightly more
powerful. I am aware that it was a warden's weapon previously but the
HoS doesn't really have many fun toys to play with. The warden already
has crav maga (100x cooler than the laser) so giving this beast to the
HOS could help make it a more attractive and powerful head to play.
(Given 1 extra shot to keep up with the crazy lasers nowadays.)

In regards to the slight combat shotgun buff. The gun itself is ass,
it's barely ever used and the riot shotgun is superior because you can
actually put it in your armour slot. The hope is that this buff will
make people actually use it because it carries a lot of shots now so the
viability may increase.


## Changelog
:cl:
add: Added compact shotgun to the hos locker
add: Added compact shotgun as a traitor objective 
balance: gives the compact shotgun 1 extra shot
/:cl:

---
## [cdb-is-not-good/sojourn-station](https://github.com/cdb-is-not-good/sojourn-station)@[1895bd5c51...](https://github.com/cdb-is-not-good/sojourn-station/commit/1895bd5c511012ac1978d52aea8f6810a90fcf08)
#### Monday 2023-08-21 21:01:58 by CDB

Im so sick of bugs. (#4739)

* Mother fucker. Im so sick of bugs.

Cigarettes no longer(seem to) cause kidney damage to people with unclean living.

psion void armor has correct slowdown for shoes and doesn't use slowdown on other pieces of armor. Additionally, no longer allows ears to flop outside of it. It's a fucking space suit, why would they be out?

Opifex medbelt no longer selectable, sorry powergamers.

Removes change_appearance from baseline armor vest. Why? It is the parent to MANY MANY MANY fucking items and thus caused MANY MANY MANY items to have erronious change_appearance procs that only had two options for the base parent item. This is why we don't put fucking procs on BASE PARENT items that affect DOZENS of other items. Fixes a few others, WO plate has no unique sprite and now has a proper working change appearance. CO does have a unique sprite, it is gone.

Fixes #4732
Fixes #4734
fixes #4724

* Update psi_Larmor.dm

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[783629a9c3...](https://github.com/Buildstarted/linksfordevs/commit/783629a9c3346e676802aaa3a8e9f7edeb8f8ec8)
#### Monday 2023-08-21 21:08:48 by Ben Dornis

Updating: 8/21/2023 9:00:00 PM

 1. Added: Backing Up Personal Files with rclone
    (https://vineeth.io/posts/2023/rclone-backups/)
 2. Added: Reliable communication allows for simpler interfaces - Max's Notes
    (https://notes.max.engineer/reliable-communication-allows-for-simpler-interfaces)
 3. Added: Metaphors for thinking about LLMs
    (https://vivekhaldar.com/articles/metaphors-for-thinking-about-llms/)
 4. Added: The Future of Data Engineering in the Warehouse
    (https://chrisreuter.me/2023-08-21-future-of-data-engineering/)
 5. Added: A Process for Building LLM Classifiers
    (https://blog.kasperjunge.com/a-process-for-building-llm-classifiers)
 6. Added: Listen to non-users!
    (https://kodare.net/2023/08/21/listen-to-non-users.html)
 7. Added: JSON Sort CLI and Pre-Commit Hook
    (https://www.paraesthesia.com/archive/2023/08/21/json-sort-cli-pre-commit/)
 8. Added: The Broad Set of Computer Science Problems Faced at Cloud Database Companies
    (https://davidgomes.com/the-broad-set-of-computer-science-problems-faced-at-cloud-database-companies/)
 9. Added: Don't Fire Your Illustrator
    (https://sambleckley.com/writing/dont-fire-your-illustrator.html)
10. Added: The Problem with Friendly C – Embedded in Academia
    (https://blog.regehr.org/archives/1287)
11. Added: Storing passkeys in password managers is okay, actually
    (https://cendyne.dev/posts/2023-08-21-passkeys-in-password-managers-is-okay.html)
12. Added: Brenton Cleeland - Website Best Practices
    (https://brntn.me/blog/website-best-practices/)
13. Added: DIY Deliberate Practice  — Lynette Bye Coaching
    (https://lynettebye.com/blog/2023/7/27/diy-deliberate-practice)
14. Added: We don't need to "degrow" the economy
    (https://www.elysian.press/p/we-dont-need-degrowth-for-the-environment)
15. Added: Declarative package management with a Brewfile
    (https://matthiasportzel.com/brewfile/)
16. Added: Why LFI is a tough sell
    (https://surfingcomplexity.blog/2023/08/20/why-lfi-is-a-tough-sell/)
17. Added: Algolia + NextJS for Ecommerce
    (https://www.avikaminetzky.dev/posts/algolia-ecommerce-nextjs)
18. Added: E-ink is so Retropunk
    (https://rmkit.dev/eink-is-so-retropunk/)
19. Added: What’s a Website
    (https://joe-ferrara.github.io/2023/08/20/whats-a-website.html)
20. Added: Concise explanations accelerate progress
    (https://stephanango.com/concise)
21. Added: The Ugly Truth About Sleep
    (https://www.okdoomer.io/the-ugly-truth-about-sleep/)
22. Added: Enjoying the Internet again with the Fediverse and IndieWeb
    (https://blog.kovah.de/en/2023/enjoying-internet-again-with-fediverse-indieweb/)

Generation took: 00:08:36.5061520
 Maintenance update - cleaning up homepage and feed

---
## [j12bates/Innullifiability](https://github.com/j12bates/Innullifiability)@[fcaf661212...](https://github.com/j12bates/Innullifiability/commit/fcaf6612123010f32e6bd0de4771cd56d06a2c47)
#### Monday 2023-08-21 22:24:34 by Jacob Bates

i HATE MY LIFEEE

Inserting this ONE LINE sped up the weeding process by at least 5-6x...
AND I COULD HAVE DONE THIS MONTHS AGO!!! This is such a meme, and I feel
so ridiculous for it.

Without this base case, the function spent a lot of time dealing with
size-2 sets and doing every possible operation, when in reality there's
only one thing to do with those: subtract, and see if it's zero. Yeah,
if you can figure out how to optimize stuff deep down there in small
sets, that'll speed things up massively, as in the end most of the
runtime of the function is spent with those smaller ones.

Yeah, it's annoying and all how I could've done this ages ago, But at
least now my code is super fast. The N = 6, M <= 40 case used to take
5.5s, but now it finishes in 1.5s. The weeding process itself sped up
from 4.7s to 0.77s. And for the N = 7, M <= 81 case, the user time went
from 11m23s to 1m57s (and these figures include a substantial amount of
constant disk I/O time)!

So now that my attention is on the Exhaustive Test program, what can I
do to improve it? I think I'll abstract away the recursive function and
make a separate user-level function for some extra checks just for the
initial set. That compile warning about 'max object size' is just
because the potential for a set to be length-0, so I'll handle that case
in there and ensure the recursive function only works with sets of
length 2 or larger. Perhaps I could also try to make an optimized case
for length-3 sets, since those'd be much simpler to work with, and like
I said, it's down with shorter sets that the function spends most of its
time. I could possibly even try to implement memoization at that level.
These are all things I can do to improve the existing code, but I still
think that in the long-term it'd be better to phase this out and go for
something more elegant, unless perhaps I can make this blazing fast.

I've been told to avoid recursion wherever possible, and I've definitely
come to understand why. Most of the optimizations I've made throughout
this project have been simply getting rid of recursion. However, it is
kinda necessary here. I guess a good rule of thumb for using recursion
would be to always make sure your base cases are solid and thorough. If
there's one you could add, even if your code will catch it later, just
do it anyways. This is gonna be saving me loads of runtime.

---
## [brandonassisantonio/SQLportfolioproject1](https://github.com/brandonassisantonio/SQLportfolioproject1)@[dc39fa9bbb...](https://github.com/brandonassisantonio/SQLportfolioproject1/commit/dc39fa9bbb75121cd83cce49028b1b0436d9df14)
#### Monday 2023-08-21 23:56:21 by brandonassisantonio

Add files via upload

Case Study: Choosing an App Idea with Data Analysis

Introduction:
A team of app developers is eager to create a new mobile app but is facing challenges in deciding the app's concept, pricing strategy, and genre. They understand the competitive nature of the app market and want to make an informed decision to increase their chances of success. To address these uncertainties, the team has decided to hire a data analyst to provide insights based on data from the Apple App Store.

Background:
The app development team is composed of skilled developers who have experience creating various types of apps, ranging from games to productivity tools. However, they are aware that creating a successful app requires more than just technical expertise. They need to identify a niche that is in demand and aligns with market trends.

Challenges:

App Concept: The team is struggling to come up with a unique and innovative app concept that stands out in the crowded app market.
Pricing Strategy: They are uncertain about whether to offer the app for free with in-app purchases, charge a one-time fee, or adopt a subscription-based model.
App Genre: The team is debating between several genres, including gaming, health and fitness, education, and social networking.
Solution:
The app development team realizes the importance of data-driven decision-making in selecting the right app concept, pricing strategy, and genre. To gain insights and clarity, they decide to hire a data analyst.

Data Analysis Approach:
The data analyst is tasked with performing an in-depth analysis of the Apple App Store data to uncover trends, user preferences, and market gaps. The analysis will focus on the following aspects:

Top Categories: The analyst will identify the most popular app categories in terms of downloads and revenue. This can provide insights into which genres are currently in demand.

Price Points: By examining the pricing strategies of successful apps, the analyst can help the team make an informed decision about the most suitable pricing model.

User Reviews: Analyzing user reviews and ratings can reveal pain points and features that users appreciate or dislike in existing apps. This information can guide the team in creating a user-focused app.

Competitor Analysis: The analyst will study the top apps in the selected genres to identify gaps or opportunities that the team can leverage.

Expected Outcome:
Based on the data analysis, the app development team expects to gain the following insights:

Clear App Concept: The team will have a better understanding of which app concepts have higher demand and potential for success.
Optimal Pricing Strategy: Data analysis will help determine the most suitable pricing model based on what users are willing to pay.
Genre Selection: The team will have data-driven insights into which genres have the highest growth and user engagement.
Conclusion:
By leveraging data analysis, the app development team aims to make informed decisions that will increase the chances of creating a successful app. The insights gained from the analysis of the Apple App Store data will guide them in selecting the right app concept, pricing strategy, and genre to capture the attention of users and stand out in the competitive app market.

---

