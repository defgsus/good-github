## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-02-25](docs/good-messages/2023/2023-02-25.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,828,989 were push events containing 2,594,512 commit messages that amount to 164,822,281 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 54 messages:


## [GerHobbelt/jpeg-xl](https://github.com/GerHobbelt/jpeg-xl)@[fead2da64d...](https://github.com/GerHobbelt/jpeg-xl/commit/fead2da64d6b091317f71ce146edb03855e4a2ac)
#### Saturday 2023-02-25 00:11:46 by Ger Hobbelt

fix duplicated here after code review.

----------------------

tesseract: fix compiler errors due to windows system header file errors

// mupdf headers cause some weird error in MSVC system header commdlg.h when include *after* <random> header below. And this only happens for params.cpp, i.e. when params.h has been included first. ... A definite case of WTF?!
//
// Which is why we include the mupdf headers here in monolithic builds...
//
// EDIT: Subsequent compiler runs and analysis now popped up the same 'crazy' errors in commdlg.h (caused by missing font struct definitions)
// from control.cpp and a few other tesseract source files. Which forced me to investigate further.
//
// Debugging through running the preprocessor (cl /E /P ...) and some grepping
//
//   grep '#line' $( find -name control.i )  | grep -B 1000000 commdlg | grep -B 1000000 wingdi | grep -v "Program Files"
//
// showed the original culprit was probably MuPDF\\thirdparty\\curl\\lib\\setup-win32.h.
// And indeed there we found the often-troublesome WIN32_LEAN_AND_MEAN and a few choice other NOXYZ feature defines before loading windows.h.
//
// > Rationale for the precise grep chain is out of scope.
// > Hint: wingdi defines what commdlg needs. Chain + last filter takes care of getting loading file as last #line stmt, IFF you're lucky.
// > Of course I was lucky. After N iterations, which got me to this grep chain. EFF that shite, with prejudice!
//
// This practice MUST be abolished in all libraries, everywhere, as it causes severe compile errors at surprise locations and at surprise times,
// while the errors reported aren't always easy to diagnose for everybody. (How many programmers are well versed with gcc -E, cl /P and code inspection?)
//
// Setting these feature defines MUST be the sole prerogative of the final application code/project, if any. Or rather more precise: the final C/C++ *.c+*.cpp source files.
// No-one else MUST mess with these in any header / include files, just to 'help' shorten compiler turn-around times. The road to Hell is paved with good intentions.
// If you want to offer 'help' like that, consider making sure your header files work well with precompiled header caching in the various compilers instead.
//

See also cUrl repo.

---
## [SharezoneApp/sharezone-app](https://github.com/SharezoneApp/sharezone-app)@[34a4016318...](https://github.com/SharezoneApp/sharezone-app/commit/34a40163180ebcc2af1a5f6e52eefa047781a4b8)
#### Saturday 2023-02-25 00:18:44 by Nils Reichardt

Initialize Firebase via Dart (#376)

## Description

With this PR we initialize Firebase also via Dart. This change requires
setting the `main` file when running the Flutter app:

```sh
flutter run \
  --flavor dev \
  --target lib/main_dev.dart
```

This is because we need a way to know which flavor is used inside the
Dart code to terminate which Firebase project we should initialize. An
alternative would be to use `--dart-define`. However, I like the
`--target` solution more because there is no default option and you have
to explicitly set a flavor. With `--dart-define`, we would either need
to set a default or throw an exception at runtime.

Our file structure looks like this:
```
lib/
  ...
  main_common.dart
  main_dev.dart
  main_prod.dart
```

`main_common.dart` is just the old `main.dart` but with a required
`flavor` parameter.

We are going to keep the native Firebase initialization for Android on
iOS because we need it for Crashlytics and from my experience is the
initialize Firebase way for Android and iOS not that stable. It's no
problem to have both solutions.

## Related Tickets

Closes #375 
Closes #221

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[3978cfe70f...](https://github.com/cmss13-devs/cmss13/commit/3978cfe70f7e32331243e8b05738067b6101ebe6)
#### Saturday 2023-02-25 00:20:50 by spartanbobby

LV522: Chances Changes (#2695)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR makes numerous Changes to LV522 as well as adds more props to
ease of mapper use

# Explain why it's good for the game

The areas changes and reasons why as are follows
**SW Reactor:** Entirely removed and replaced with a much more open
containers area for the xenos to build up and defend, this area is now
the linchpin of the map as marines have to push though it to get to
other flanks inside the reactor meaning the xeno players should now have
a much better understanding of where they need to defend instead of
prior problems with the map of them being hard flanked and losing at
12:26

**LZ1:** LZ1 was moved slightly more north in an attempt to remove some
deadspace and make the path from the front to the FOB slightly less
long, more LZ1 tunnels and ways inside the FOB were added for xeno
flankers aswell as LZ1 being locked down until the marines push a button
to open it up

**Colony admin** A sensor tower was added to colony admin to encourage
marines to go over there and investigate, along with a lockdown to the
area being added

**LZ3** a FORECON prop LZ housing the Tornado was re-added after being
removed in an attempt to downsize the map, basically I figured out where
I could put it

**props:** Alot of instanced props for the map were made into actual
items such as, bedrolls and folded bedrolls, FORECON dogtags, used
flares, jerry cans, used bandages and some weird gameboy thing

Sprites: https://i.imgur.com/avi2fUo.png
FORECON was always made to have a patch it was one of those things I
wanted but never got, luckily while making this PR I was able to look
into it and get the old sprite from tri to finish up myself with onmobs

FORECON Balance changes: The M39 being in the primary weapon slot is
more of a "fuck you" to people playing the roll than just unlucky RNG
that is workaround able moving it to the secondary pool lets the FORECON
play around with better weapons to survive with and the M39 extended
magazines means it's one of the only weapons FORECON spawn with that has
a decent amount of ammo

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

:cl:SpartanBobby
add: Made some instanced props on LV522 actual items for mapper ease of
use
maptweak: tweaked LV522, removing the SW reactor and replacing it with a
much more open container area once used as the FORECONS FOB
maptweak: tweaked LZ1 on LV522 making it start locked down and be
slightly more north along with some extra tunnels and flanking routes
for the xenos
maptweak: LV522, added a lockdown and moved the sensor tower to colony
admin
maptweak: re-added the prop LZ in the NE of the colony
maptweak: redistributed LV522 mining metal spawns to be more spread out
maptweak: removed building color outlines from LV522 that were there to
help with navigation during Test merges since the map has been out for
long enough for the majority to properly navigate it
tweak: M39 removed from FORECON primary weapon pool and added to
secondary weapon pool along with extended mags instead of normal
add: Added FORECON Patches for the survivors on LV522 sprites made by
Triiodine while onmobs were made by myself with help from Kugamo
fix: examing a uniform no longer tells you that it has "an
USCM/FORECON/Falling falcons patch" instead it says "a patch"
add: updated the USCM FORECON uniform name and description 
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Nanu308 <59782240+Nanu308@users.noreply.github.com>

---
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[7d27d8508c...](https://github.com/realforest2001/forest-cm13/commit/7d27d8508ce0723dbbcf1dfad9810a3092a71f61)
#### Saturday 2023-02-25 00:29:52 by TotalEpicness

Fixes invincible base crusher (#2682)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Fixes an oversight that allowed base crusher to have half it's intended
shield cooldown
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.
runs
Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Never intended on the first place and led to crusher being busted as
fuck as it is currently.

This was never intended and was a mess up on my part. It fell through
from the painfully long development that Charger had as months went by
between testing sessions and TMs, along with my inexperience with larger
projects and bad note taking at the time.

Maintainers are also supposed to filter stuff like this but after like a
billion code reviews Charger had, I can see how it got through on their
end as well.

Nevertheless this dies here. 

funny contrib moment
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
it runs
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

:cl: Totalepicness
balance: Fixes base crusher having half it's intended cooldown for the
shield ability
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Epicness <coolguyethanw@gmail.com>

---
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[b4954e1402...](https://github.com/Ultimate-Fluff/cmss13/commit/b4954e14028909b107d0b204da0ad06c5dfeb50a)
#### Saturday 2023-02-25 00:33:48 by carlarctg

zombie powder fix (#2315)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Fixes Zombie Powder bugging the fuck out by slapping a ton of FAKEDEATH
checks everywhere. It now properly shows the holder as dead on HUDs and
scans.

Fixed an issue in which sometimes qdeleted reagents still procced on
life.

Fixed examining things changing your direction if you're incapacitated.

Added FAKEDEATH to the mob_incapacitated() check.


# Explain why it's good for the game

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
fix: Fixes Zombie Powder bugging the fuck out by slapping a ton of
FAKEDEATH checks everywhere. It now properly shows the holder as dead on
HUDs and scans.
fix: Fixed an issue in which sometimes qdeleted reagents still procced
on life.
fix: Fixed examining things changing your direction if you're
incapacitated.
fix: Added FAKEDEATH to the mob_incapacitated() check.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: harryob <me@harryob.live>

---
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[b53c9f0531...](https://github.com/Ultimate-Fluff/cmss13/commit/b53c9f0531897023fe365961c16863d8f41983d9)
#### Saturday 2023-02-25 00:33:48 by carlarctg

Turns all instances of 'colour' into 'color' (#2609)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Turns all instances of 'colour' into 'color'.

Changed a shittily-named crayon variable's name.

# Explain why it's good for the game

We use burgerclapper english and we should standardize this

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
spellcheck: Removed all instances of 'colour' and replaced them with
'color'
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [CharlesWedge/Citadel-Station-13-RP](https://github.com/CharlesWedge/Citadel-Station-13-RP)@[81c1229373...](https://github.com/CharlesWedge/Citadel-Station-13-RP/commit/81c1229373208790c3375a138579aaf76a0006d0)
#### Saturday 2023-02-25 00:41:12 by Captain277

Adds Just Like, a Ton of Clothes (#5048)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. **Adds a wide array of clothes, listed below.**

## Why It's Good For The Game

1. _My good friend Tech provided me with some sprite sheets when I was
working on Ashlanders, requesting a hobo coat. Going through the sheets
I found several different items I thought it would be fun to add to our
expanding list of customization and fashion options. The list is huge so
I'm just gonna itemize it here. As for attributions, as I understand it
most of this is from a D&D server, and some from a 40k server._
2. _Two of the outfits, the Belial and Lilin items, are sprites crafted
by our very own Doopy, as part of their Lindenoak line!_

## Outfits & Where to Get them

**Costume Vendor**
1. _Banana Costume_
3. _Hashashin Costume_
4. _Bard Hat_
5. _Aquiline Enforcer Uniform_
6. _Scavenging Sniper Set_
7. _Spiral Hero Outfit_
8. _Body Tape Wrapping_
9. _Redcoat Uniform_
10. _Despotic General Uniform_
11. _Post-Revolution American Uniform_
12. _Prussian Uniform_

**Suit Vendor**
1. _Ragged Coat_
2. _Spiral Hero Cloak_
3. _Nerdy Shirt_

**Jumpsuit Vendor**
1. _Toga_
2. _Countess Dress_
3. _Baroness Dress_
4. _Revealing Cocktail Dress_
5. _Belial Striped Shirt and Shorts_
6. _Lilin Sash Dress_

**Shoes Vendor**
1. _Utilitarian Shoes_

**Loadout**
1. _Ragged Coat_
7. _Spiral Hero Cloak_
8. _Nerdy Shirt_
9. _Bard Hat_
10. _Utilitarian Shoes_
11. _Toga_
13. _Countess Dress_
14. _Baroness Dress_
15. _Scavenging Sniper Set_
16. _Spiral Hero Outfit_
17. _Body Tape Wrapping_
18. _Revealing Cocktail Dress_
19. _Belial Striped Shirt and Shorts_
20. _Lilin Sash Dress_

**Medieval Armor Supply Crate**
1. _Crimson Knight Armor_
2. _Forest Knight Armor_
3. _Hauberk_
4. _Elite Paladin Armor, Helmet, and Boots_
5. _Alternate Knight Helmet_

**Cryosuit Supply Crates (Under Voidsuit Menu)**
1. _Cryosuit, Variants: Security, Engineering, Atmos, Mining_

**Crafting Menu**
1. _Duraskull Helmet_

**Ashlander Specific Crafting Menu**
1. _Ashen Vestment_
2. _Ashen Tabard_

**Ashlander Spawn**
1. _Priests now spawn with the Ashen Vestment._

**Admin Spawn**
1. _Actual armored versions of all new Knight sets._
5. _Utilitarian Military Helmet, Armor, and Boots._

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
add: Adds a wide array of new clothing items. Itemized in PR. #5408
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2b76197397...](https://github.com/tgstation/tgstation/commit/2b76197397b4241957e93a9779fdd9dfbada2688)
#### Saturday 2023-02-25 01:14:06 by Jacquerel

Makes Lesser Form into one ability & unit tests it (#73572)

## About The Pull Request

Fixes #73491
Every time I have used this ability lately it's been fucked. 
It would vanish from my actions at arbitrary moments, and also sometimes
transform me into a horrible monkey-man thing instead of a monkey. This
is a shame because being able to become a monkey can be pretty fun, even
if it makes you very vulnerable to being butchered.

Refactoring it into being one action instead of two actions which add
and remove each other fixes the part where the action just disappears.
It reliably sticks between transformations now, regardless of whether or
not they were voluntary.

I also noticed that when I was turning into a monkey it wasn't dropping
the changeling "fake clothes" outfit pieces I had on as a human, leading
to a really fucked up looking monkey. I fixed this by adding `force =
TRUE` in the drop to ground proc in the check for if the equipment you
have is still valid after your species changes. I don't _think_ this has
any side effects but I never do and then someone finds some.
For good measure I also made all of the changeling equipment abilities
which don't work if you are a monkey detect if you become a monkey and
retract themselves.

I also noticed that for a long time Last Resort has been trying and
failing to give you Lesser Form (well, Human Form rather) as a Headcrab,
so I fixed that and now you actually get the ability.

Finally I did a _little_ bit of housekeeping in general on the
changeling actions, mostly balloon alerts. I think these definitely need
more attention than I gave them though. I left a lot of the `to_chat`s
in place because many of them give information you want to be a little
sticky, or refer back to in order to double check what you just did.

I also added a unit test which flips back and forth a few times to
ensure the ability still works.
This required adding an "instant" flag to the monkeyize/humanize procs
to skip the timers, and idenitified a couple of weird issues.
First point: Humanising a monkey would remove the monkey mutation and
then call humanise again, which would not skip itself because it still
regarded you as being a monkey. I changed the order of operations here
slightly so that it will early return.
Second point: Calling `domutcheck` on `human/consistent` would runtime
because we skip the bit which sets up any mutations in their DNA. This
is a part of changeling transformation, so I just made it return
instantly.

## Why It's Good For The Game

You can use this ability again without getting stuck permanently as a
monkey, or it just deleting itself from your list of abilities for no
reason.
Turning into a monkey with fake outfit pieces on won't turn you into an
abomination.

## Changelog

:cl:
refactor: Changeling's Lesser Form is now one ability instead of two
which keep swapping, which should consistently turn you back and forth
without deleting itself from your action bar.
fix: Hatching from an egg left by a Last Resort headcrab should
correctly grant you Lesser Form in addition to your other abilities.
fix: Turning into a monkey while using the Changeling space suit won't
leave you as a monkey with a weird inflated head.
qol: Using lesser form as a monkey with only one stored DNA profile will
skip asking which profile you want and will simply transform you
immediately into the only option.
/:cl:

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

---
## [Clownsw/qemu](https://github.com/Clownsw/qemu)@[8d0efbcfa0...](https://github.com/Clownsw/qemu/commit/8d0efbcfa0656bef76e95d40933b6243feca58c9)
#### Saturday 2023-02-25 01:25:00 by Paolo Bonzini

docs: build-platforms: refine requirements on Python build dependencies

Historically, the critical dependency for both building and running
QEMU has been the distro packages.  Because QEMU is written in C and C's
package management has been tied to distros (at least if you do not want
to bundle libraries with the binary, otherwise I suppose you could use
something like conda or wrapdb), C dependencies of QEMU would target the
version that is shipped in relatively old but still commonly used distros.

For non-C libraries, however, the situation is different, as these
languages have their own package management tool (cpan, pip, gem, npm,
and so on).  For some of these languages, the amount of dependencies
for even a simple program can easily balloon to the point that many
distros have given up on packaging non-C code.  For this reason, it has
become increasingly normal for developers to download dependencies into
a self-contained local environment, instead of relying on distro packages.

Fortunately, this affects QEMU only at build time, as qemu.git does
not package non-C artifacts such as the qemu.qmp package; but still,
as we make more use of Python, we experience a clash between a support
policy that is written for the C world, and dependencies (both direct
and indirect) that increasingly do not care for the distro versions
and are quick at moving past Python runtime versions that are declared
end-of-life.

For example, Python 3.6 has been EOL'd since December 2021 and Meson 0.62
(released the following March) already dropped support for it.  Yet,
Python 3.6 is the default version of the Python runtime for RHEL/CentOS
8 and SLE 15, respectively the penultimate and the most recent version
of two distros that QEMU would like to support.  (It is also the version
used by Ubuntu 18.04, but QEMU stopped supporting it in April 2022).

There are good reasons to move forward with the deprecation of Python
3.6 in QEMU as well: completing the configure->meson switch (which
requires Meson 0.63), and making the QAPI generator fully typed (which
requires newer versions of not just mypy but also Python, due to PEP563).

Fortunately, these long-term support distros do include newer versions of
the Python runtime.  However, these more recent runtimes only come with
a very small subset of the Python packages that the distro includes.
Because most dependencies are optional tests (avocado, mypy, flake8)
and Meson is bundled with QEMU, the most noticeably missing package is
Sphinx (and the readthedocs theme).  There are four possibilities:

* we change the support policy and stop supporting CentOS 8 and SLE 15;
  not a good idea since CentOS 8 is not an unreasonable distro for us to
  want to continue to support

* we keep supporting Python 3.6 until CentOS 8 and SLE 15 stop being
  supported.  This is a possibility---but we may want to revise the support
  policy anyway because SLE 16 has not even been released, so this would
  mean delaying those desirable reasons for perhaps three years;

* we support Python 3.6 just for building documentation, i.e. we are
  careful not to use Python 3.7+ features in our Sphinx extensions but are
  free to use them elsewhere.  Besides being more complicated to understand
  for developers, this can be quite limiting; parts of the QAPI generator
  run at sphinx-build time, which would exclude one of the areas which
  would benefit from a newer version of the runtime;

* we only support Python 3.7+, which means CentOS 8 CI and users
  have to either install Sphinx from pip or disable documentation.

This proposed update to the support policy chooses the last of these
possibilities.  It does by modifying three aspects of the support
policy:

* it introduces different support periods for *native* vs. *non-native*
  dependencies.  Non-native dependencies are currently Python ones only,
  and for simplicity the policy only mentions Python; however, the concept
  generalizes to other languages with a well-known upstream package
  manager, that users of older distributions can fetch dependencies from;

* it opens up the possibility of taking non-native dependencies from their
  own package index instead of using the version in the distribution.  The
  wording right now is specific to dependencies that are only required at
  build time.  In the future we may have to refine it if, for example, parts
  of QEMU will be written in Rust; in that case, crates would be handled
  in a similar way to submodules and vendored in the release tarballs.

* it mentions specifically that optional build dependencies are excluded
  from the platform policy.  Tools such as mypy don't affect the ability
  to build QEMU and move fast enough that distros cannot standardize on
  a single version of them (for example RHEL9 does not package them at
  all, nor does it run them at rpmbuild time).  In other cases, such as
  cross compilers, we have alternatives.

Right now, non-native dependencies have to be download manually by
running "pip" before "configure".  In the future, it will be desirable
for configure to set up a virtual environment and download them in the
same way that it populates git submodules (but, in this case, without
vendoring them in the release tarballs).

Just like with submodules, this would make things easier for people
that can afford accessing the network in their build environment; the
option to populate the build environment manually would remain for
people whose build machines lack network access.  The change to the
support policy neither requires nor forbids this future change.

[Thanks to Daniel P. Berrangé, Peter Maydell and others for discussions
 that were copied or summarized in the above commit message]

Cc: Markus Armbruster <armbru@redhat.com>
Cc: Peter Maydell <peter.maydell@linaro.org>
Cc: John Snow <jsnow@redhat.com>
Cc: Kevin Wolf <kwolf@redhat.com>
Reviewed-by: Daniel P. Berrangé <berrange@redhat.com>
Reviewed-by: Alex Bennée <alex.bennee@linaro.org>
Signed-off-by: Paolo Bonzini <pbonzini@redhat.com>

---
## [ssharkk/DSG23-State-of-Flow](https://github.com/ssharkk/DSG23-State-of-Flow)@[963b88baa2...](https://github.com/ssharkk/DSG23-State-of-Flow/commit/963b88baa2bab711ec907f820140ed6c64c1d40c)
#### Saturday 2023-02-25 01:35:00 by Piotrus Watson

made a fucken series of pipes holy shit its still broken so bwec carefuyle

---
## [vijaydasmp/dash](https://github.com/vijaydasmp/dash)@[aec7441ac2...](https://github.com/vijaydasmp/dash/commit/aec7441ac2863b4d92c5032e98e8b2691262a912)
#### Saturday 2023-02-25 01:57:01 by Wladimir J. van der Laan

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
## [Sidpatchy/ClaireBot](https://github.com/Sidpatchy/ClaireBot)@[4731619c45...](https://github.com/Sidpatchy/ClaireBot/commit/4731619c45bd432e2a6db3c97bc66f1f1baa6e92)
#### Saturday 2023-02-25 02:05:39 by Sidpatchy

v3.0.0-alpha.3

This adds *a lot*.

Finishes up the implementation of /config. The only thing missing is the language setting as I have not added that to the rest of the bot yet (and honestly i'm on the fence about doing that at all).

On the topic of /config, I couldn't find a way to update ephemeral messages so I just gave up and started to respond with an interaction follow-up instead. This isn't as neat as I'd like, but oh well. 🤷‍♀️

Next, it adds the info command, disables (until I get around to implementing it) /level and /leaderboard.

It also completely removes all music bot functionality, I do not have interest in maintaining that feature-set anymore.

Pushes all file-handling code to Robin, I honestly thought I already did this, but here we are.

I started an update to the 8ball command but decidedly gave up on that because as it turns out, making a generic response to non-yes/no questions is pretty hard. Even making answers that are comedically wrong is rather difficult.

I also finally fixed the bloody log4j2.xml file to make it less awful to debug issues.

The commands(.yml) file has been updated to feature the new overview field from Robin v1.1. You will need to regenerate or manually update your config file.

The config(.yml) has a fully fleshed out series of options for ClaireData, so be sure to add that section or regenerate your config file.

Besides some other misc. bugfixes, I think that's about it.

P.S. the longest part of all of this was figuring out what I changed 3 months ago and then left partially complete. Probably don't do that.

---
## [xiaosen7/react](https://github.com/xiaosen7/react)@[b6978bc38f...](https://github.com/xiaosen7/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Saturday 2023-02-25 02:13:31 by Andrew Clark

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
## [Pink-Chink/CEV-Eris-14](https://github.com/Pink-Chink/CEV-Eris-14)@[168bad2ef2...](https://github.com/Pink-Chink/CEV-Eris-14/commit/168bad2ef25cc25c2cffea788f643425b858be6d)
#### Saturday 2023-02-25 03:33:57 by Nemanja

multi-handed item component (#12523)

* multi-handed item component

* pretty fucking obvious missed portion of this

* holy shit was i on crack wtf was that code

* DEWIT RIGHT

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[0641490ad9...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/0641490ad9819094444c84129e8a5e9aa0ed29ce)
#### Saturday 2023-02-25 03:35:35 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- *Zero* additional `gcc` builds (stage1+stage2+stageCompare)
  - The `gcc` derivation builds `gcc` once instead of three times.
  - The libraries that are linked into the final `pkgs.gcc` (`mpfr`,
    `mpc`, `gmp`, `isl`, `glibc`) are built by
    `stdenv.__bootPkgs.gcc` rather than by the `bootstrapFiles`.  No
    more Frankenstein compiler!
  - stageCompare runs **concurrently** with (not in series with)
    with `stdenv`'s dependees.
- Many other `stdenv` hacks eliminated.
  - `gcc` and `clang` share the same codepath for more of
    `cc-wrapper`.
  - Makes the cross and native codepaths much more similar --
    another step towards "cross by default".

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- There will be an "avalanche of simplification" when we set
  `enableGccNixDrivenBootstrap=true` and run dead code elimination.
  It's really quite a huge amount of code that goes away.
  Native-gcc has its own special codepath in so many places, while
  cross-gcc and clang work the same way (and are much simpler).
- This should allow each of the libraries that ship with `gcc`
  (`lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}`) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`.
  - Building `libstdc++-v3` in a separate derivation will eliminate
    a lot of accidental-reference-to-the-`bootstrapFiles` landmines.

 #### Incorporates

- https://github.com/NixOS/nixpkgs/pull/210004
- https://github.com/NixOS/nixpkgs/pull/36948 (unreverted)
- https://github.com/NixOS/nixpkgs/pull/210325
- https://github.com/NixOS/nixpkgs/pull/210118
- https://github.com/NixOS/nixpkgs/pull/210132
- https://github.com/NixOS/nixpkgs/pull/210109
- https://github.com/NixOS/nixpkgs/pull/213909
- https://github.com/NixOS/nixpkgs/pull/216136
- https://github.com/NixOS/nixpkgs/pull/216237
- https://github.com/NixOS/nixpkgs/pull/210019
- https://github.com/NixOS/nixpkgs/pull/216232
- https://github.com/NixOS/nixpkgs/pull/216016
- https://github.com/NixOS/nixpkgs/pull/217977
- https://github.com/NixOS/nixpkgs/pull/217981
- https://github.com/NixOS/nixpkgs/pull/217995

 #### Closes

- Closes #108305
- Closes #108111
- Closes #201254
- Closes #208412

 #### Credits

This project was made possible by three important insights, none of
which were mine:

1. @ericson2314 was the first to advocate for this change, and
   probably the first to appreciate its advantages.  Nix-driven
   (external) bootstrap is "cross by default".

2. @trofi has figured out a lot about how to get gcc to not mix up
   the copy of `libstdc++` that it depends on with the copy that it
   builds, by moving the `bootstrapFiles`' `libstdc++` into a
   [versioned directory].  This allows a Nix-driven bootstrap of gcc
   without the final gcc would still having references to the
   `bootstrapFiles`.

3. Using the undocumented variable [`user-defined-trusted-dirs`]
   when building glibc.  When glibc `dlopen()`s `libgcc_s.so`, it
   uses a completely different and totally special set of rules for
   finding `libgcc_s.so`.  This trick is the only way we can put
   `libgcc_s.so` in its own separate outpath without creating
   circular dependencies or dependencies on the bootstrapFiles.  I
   would never have guessed to use this (or that it existed!) if it
   were not for a [comment in guix] which @Mic92 [mentioned].

My own role in this PR was basically: being available to go on a
coding binge at an opportune moment, so we wouldn't waste a
[crisis].

[aarch64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662822938
[amd64-compare-ofborg]: https://github.com/NixOS/nixpkgs/pull/209870/checks?check_run_id=10662825857
[nonexistent sysroot]: https://github.com/NixOS/nixpkgs/pull/210004
[versioned directory]: https://github.com/NixOS/nixpkgs/pull/209054
[`user-defined-trusted-dirs`]: https://sourceware.org/legacy-ml/libc-help/2013-11/msg00026.html
[comment in guix]: https://github.com/guix-mirror/guix/blob/5e4ec8218142eee8e6e148e787381a5ef891c5b1/gnu/packages/gcc.scm#L253
[mentioned]: https://github.com/NixOS/nixpkgs/pull/210112#issuecomment-1379608483
[crisis]: https://github.com/NixOS/nixpkgs/issues/108305
[foreign]: https://github.com/NixOS/nixpkgs/pull/170857#issuecomment-1170558348
[static lib{mpfr,mpc,gmp,isl}.a hack]: https://github.com/NixOS/nixpkgs/blob/2f1948af9c984ebb82dfd618e67dc949755823e2/pkgs/stdenv/linux/default.nix#L380

---
## [rd-stuffs/android_frameworks_base](https://github.com/rd-stuffs/android_frameworks_base)@[e2ce96a5d9...](https://github.com/rd-stuffs/android_frameworks_base/commit/e2ce96a5d98e8333ac3af66255395d95db4ebe7d)
#### Saturday 2023-02-25 05:12:07 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [rain-world-map/rain-world-map.github.io](https://github.com/rain-world-map/rain-world-map.github.io)@[064227326a...](https://github.com/rain-world-map/rain-world-map.github.io/commit/064227326a614b26b6920134cc921e0e855630b6)
#### Saturday 2023-02-25 06:17:19 by Dual-Iron

Adjust tiling

And by that i mean fix fucking everything seriously im a goddamn idiot !!

---
## [Davchikk/Shiptest](https://github.com/Davchikk/Shiptest)@[d21740b475...](https://github.com/Davchikk/Shiptest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Saturday 2023-02-25 06:26:56 by tmtmtl30

Mapgen fixes and speedups (ignore the branch name. I'm dumb) (#1637)

## About The Pull Request

Alters the structure of map/planet generation to squash some bugs and
improve performance.

Previously, planet maps were generated by placing the ruin first, and
THEN generating the turfs according to the map_generator datum. This has
been adjusted -- now, turfs are generated WITHOUT objects such as
mobs/flora, the ruin is placed, and THEN the objects are added (turfs
are "populated"). In conjunction with the addition of needed
AfterChange() calls to update the atmos adjacency of the generated
turfs, this ensures that planet atmos acts correctly surrounding ruins.

When deleting reservations (such as the deletion of planets after
undocking), all objects on the planet are rounded up in a list and
qdeleted. Although this causes a small lag spike, it SHOULD prevent
items from hanging out inside the edges of planets.

There's a feature to change the default baseturf of a virtual level,
ZTRAIT_BASETURF, that we now use. This should cut down on the instances
where a ruin on a planet is blown up and there's space underneath (might
still happen on asteroids, because the baseturf there is still space; I
didn't want space turfs without space as their baseturf).

Overmap encounter areas aren't global anymore (they no longer have the
flag UNIQUE_AREA). Don't fucking add the flag UNIQUE_AREA to anything
that should have weather in it, because if that area gets added anywhere
else that _actually respects the flag_ you'll end up with cross-planet
weather, because weather code sucks. This didn't cause bugs before,
because the flag wasn't respected; it will now.

The biome assoc list has been moved into the map generator datum, and
all encounters now generate using a map generator that either uses a
biome or replaces everything with a single turf. This prevents
duplication of cave generation code and makes dynamic overmap object
code slightly easier to understand.

Some systems have been altered to improve performance; many of these
changes are rather small, like the changes to turf population (mob
placement now uses a stack of recently-created mobs to check if there
are any nearby, instead of checking everything within 12 turfs; I've yet
to add ruin mobs to these stacks to avoid placing mobs near ruin mobs)
or lighting objects (removed a single line that changed the color of the
lighting object on init).

Starlight has been altered, so that small turf changes near space turfs
don't need to check as many nearby turfs and so that large turf changes
can be batched to prevent further recalculation. This is probably
responsible for the biggest performance increase.

Smoothing groups are cached before sorting instead of after, to prevent
sort calls on many atom inits; /tg/station uses a unit test to avoid
needing to sort at runtime ever, but I couldn't figure out how to do
that without larger changes or writing a unit test that attempted to
instance every atom once, which would be an undertaking of its own.

Gas strings have been similarly altered, and now their interpretation
defaults to copying from a cached, immutable version of the mix encoded
by the string. This avoids the significant overhead caused by repeated
calls to params2list(). Auxmos has a better solution to this,
__auxtools_parse_gas_string(), but our current custom build of Auxmos
doesn't support it.

There are a few other small changes that I'm probably forgetting about
and you should yell at me to read my own fucking code and tell you what
else I changed.

- [ ] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

I still need to manually check each planet type to make sure they aren't
fucked up, I should probably do some proper profiling comparisons.

## Why It's Good For The Game

Fewer weird bugs, things generate faster, better* code.

## Changelog

:cl:
fix: Ruins don't sometimes start in hard vacuum anymore; planet turfs
now share atmos correctly.
fix: There hopefully shouldn't be any random stray objects sitting in
the edges of planets anymore.
fix: Planets now (hopefully) have the correct baseturfs (more or less).
When you bomb a ruin on a planet, it probably won't break through to
space anymore.
refactor: Planet generation has been refactored, improving performance
somewhat.
/:cl:

---
## [kyrofx/fuckben](https://github.com/kyrofx/fuckben)@[3482234f9d...](https://github.com/kyrofx/fuckben/commit/3482234f9d1e21ab6771fd0cb4dda4ebd0f3dbc7)
#### Saturday 2023-02-25 06:48:08 by PupLord

Update fuck you ben.py

Updated with error prevention and an end time display. goes from 1 to a billion from base 2-35

---
## [kyrofx/fuckben](https://github.com/kyrofx/fuckben)@[e2dc870899...](https://github.com/kyrofx/fuckben/commit/e2dc870899ae2169036c03d16d05f4ee765a9def)
#### Saturday 2023-02-25 06:49:18 by PupLord

Update fuck you ben.py

changed object 'hexBase' to 'base'

---
## [VioletN/orbstation](https://github.com/VioletN/orbstation)@[c58cbb4dfb...](https://github.com/VioletN/orbstation/commit/c58cbb4dfb42e0d9d6198c3ad581dc5a4d2f8f48)
#### Saturday 2023-02-25 06:55:26 by John Willard

Reworked PDA menu & NtOS themes (#73070)

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

Co-authored-by: san7890 <the@san7890.com>

---
## [SumStarLord/EE1103_Assignment10_ShortestPathAlgorithms](https://github.com/SumStarLord/EE1103_Assignment10_ShortestPathAlgorithms)@[4e10a467f9...](https://github.com/SumStarLord/EE1103_Assignment10_ShortestPathAlgorithms/commit/4e10a467f920a239bab1d1bc3bcde76641d9a68e)
#### Saturday 2023-02-25 07:15:02 by Jhumid

Adding pathfining_prob1.c, definitely is seg faulting in bellman ford, has alll the signss of it. For instance one of the ways to bypass the segfault is to include a printf statement within the code. The reason I know this is from my debugging experiences with LUdecomp. Something about having a print statement must like auto convert something or soemthing idk. But yeah my thoughts

---
## [Aman-Vishwakarma1729/Python_For_Data_Science](https://github.com/Aman-Vishwakarma1729/Python_For_Data_Science)@[4e40ae2693...](https://github.com/Aman-Vishwakarma1729/Python_For_Data_Science/commit/4e40ae2693417e94a27d52c4a399337f01bdb81b)
#### Saturday 2023-02-25 07:31:23 by Aman-Vishwakarma1729

Add files via upload

Q1. Create a function which will take a list as an argument and return the product of all the numbers
after creating a flat list.

Use the below-given list as an argument for your function.


list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']


Note: you must extract numeric keys and values of the dictionary also.
Q2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption
should be such that, for a the output should be z. For b, the output should be y. For c, the output should
be x respectively. Also, the whitespace should be replaced with a dollar sign. Keep the punctuation
marks unchanged.


Input Sentence: I want to become a Data Scientist.


Encrypt the above input sentence using the program you just created.

---
## [Offroaders123/Smart-Text-Editor](https://github.com/Offroaders123/Smart-Text-Editor)@[7b88518b82...](https://github.com/Offroaders123/Smart-Text-Editor/commit/7b88518b8260b61789f67b2629c2be6c94e53d46)
#### Saturday 2023-02-25 08:01:34 by Offroaders123

Editor Component!

This is a big one! Been working on it all day.

This merges the Editor functionality into a single component, currently just an object/class which will instead store the data for the given Editor, rather than relying on getting that data from the corresponding elements in the DOM, which has shown to be veerry messy. This is one step I've been wanting to take with this project for a while now, I think it really helps containerize/scope the logic for the different parts of the app. Next I will make it so that this Editor class is just an extension of `NumTextElement`, meaning it's just a single Web Component which internally manages it's own state, so you don't have to worry about how it works.

This is the "last commit" on my Chromebook, at least before the new wave has come around. Ordered the base model 2021 MacBook Pro refurbished yesterday, with $8 one-day shipping, and it got here today! Was partway through a lot of this rework once UPS got here, haha. Heard the truck door from my room XD  Gonna make the next commit to my GitHub from the new Mac, it's all set up now! Transferred everything from my iMac using a Time Machine backup, and Migration Assistant. Appears to have worked amazingly so far! The only hiccup is that I'm having to manually remove and reinstall any apps/binaries/packages that are x86-64, and replace them with their Apple Silicon ARM counterparts. Alongside that, had to reinstall Homebrew and everything I had set up with that. But, all of my settings for all of the apps were still intacked, and that was my biggest thing that I was hoping I wouldn't have to deal with. Horray!

Alright, taking a rest tonight after a long tech day, gonna have a second one tomorrow, now that everything is all set up and nearly ready to go. Time to make some more cool sh!ti Thanks Theo, haha.

Oh yeah, tried vanilla Minecraft 1.19 with the native ARM build, got 102 fps while running 120hz, f yeah that's cool!

---
## [Chelseadamola/Testin-12](https://github.com/Chelseadamola/Testin-12)@[5725da7fa4...](https://github.com/Chelseadamola/Testin-12/commit/5725da7fa4431c6fe850f86d57af940b9b6b7cd3)
#### Saturday 2023-02-25 08:10:47 by Chelseadamola

Add files via upload

# My Data Analytics Journey: Starting Out and Looking Ahead
## Introduction
Hello, my name is Chelsea. I have always had a passion for technology and have always been fascinated by the power of data to drive decisions and drive progress. I'm just starting out on my journey in data analytics, but I'm eager to see where it takes me.
### Starting Out
This week, I have a task to work on 2-3 projects using Microsoft Excel. I'm looking forward to putting my newfound skills to the test and seeing where this journey takes me.
### Developing Skills
I believe that the key skills for success in data analytics include attention to detail, critical thinking, and problem-solving. I plan on developing these skills by taking online courses, reading books on the subject, and seeking guidance from mentors in the field.
I know that there will be challenges along the way, but I'm eager to face them head-on and grow as a data analyst. I'm confident that with hard work and dedication, I'll be able to achieve my goals.
Working on Projects:
So far, I haven't faced any major challenges in my data analytics journey. However, I'm eager to take on new projects and see what the future holds. I believe that with each project I complete, I'll become a better data analyst and gain valuable experience in the field.
### Looking Ahead
I see a bright future for data analytics, with the potential to revolutionize the way we make decisions and drive progress. I hope to be a part of this revolution and contribute to the advancement of this field.
### Conclusion
In conclusion, I'm just starting out on my journey in data analytics, but I'm eager to see where it takes me. With the support of my boss, and my determination to succeed, I'm confident that I'll make a difference in this field.
I'm grateful for the opportunity to start my journey in data analytics and I'm looking forward to updating this article as I progress and make new achievements. I'm also thankful for the opportunity to meet with top data analysts and learn from their experiences. Thank you for reading and I hope my journey inspires others to pursue their passions in technology and data analytics.

---
## [CapCamIII/cmss13](https://github.com/CapCamIII/cmss13)@[4c373316ad...](https://github.com/CapCamIII/cmss13/commit/4c373316ad1e9a68e5cd7ae0e216bddcd52ee3aa)
#### Saturday 2023-02-25 09:57:39 by NewyearnewmeUwu

Alerts admins whenever humans try to gib another human. (#2560)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Successor to #2237 that properly addresses the issues brought up by
myself and others. This sends a admin alert similar to when a pred
activates their SD that allows admins to jump to the (strictly human)
player gibbing another human/human corpse and sleep them/amessage them.
This also creates logs when someone _attempts_ to stuff someone into a
gibber. I also fixed up some of the single letter variables in the
gibber code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Insanity RP is bad, and this solution allows admins to respond in
realtime. It takes 30 seconds to gib another human as a human, without
any skill modifiers helping. It also doesn't flag the player if they're
a pred, as they're _supposed_ to be doing funny human meat stuff.
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
code: gibbing another human takes an unmodifiable 30 seconds
admin: admins are alerted when a human tries to gib another human
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Riken-Shah/zulip](https://github.com/Riken-Shah/zulip)@[23a776c144...](https://github.com/Riken-Shah/zulip/commit/23a776c1448da18b906529e5951e24d8d58a7e81)
#### Saturday 2023-02-25 10:33:39 by Mateusz Mandera

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
## [Seinuve/Kudasai](https://github.com/Seinuve/Kudasai)@[cfde8f1e71...](https://github.com/Seinuve/Kudasai/commit/cfde8f1e713c73e8ad35209d9923397ad2116d15)
#### Saturday 2023-02-25 10:35:31 by Seinu

Suffering

removed testing script because i don't need it and i hate my life
switched from mecab to spacy
changed some comments
requirements.txt updated

---
## [haint126/obsidian](https://github.com/haint126/obsidian)@[7d5a30f056...](https://github.com/haint126/obsidian/commit/7d5a30f05653fd02c1938cbdbc3dc6156ce83132)
#### Saturday 2023-02-25 10:46:11 by haint126

Vault backup: 2023-02-25 17:46:05 : home

Affected files:
03_Life_experience/Books/Book to read/Others/20 books that helped me more than years at school by Ankur Warikoo/20 books that helped me more than years at school by Ankur Warikoo.md
03_Life_experience/Habits/10 Productivity Hacks by Ankur Warikoo/10 Productivity Hacks by Ankur Warikoo.md
03_Life_experience/Habits/17 life hacks from Ankur Warikoo/17 life hacks from Ankur Warikoo.md
03_Life_experience/Habits/How I read my books by Ankur Warikoo/How I read my books by Ankur Warikoo.md
03_Life_experience/Habits/_11 shocking facts about managing time/_11 shocking facts about managing time.md

---
## [LLLida/lidaEngine](https://github.com/LLLida/lidaEngine)@[8eacd67f30...](https://github.com/LLLida/lidaEngine/commit/8eacd67f30384526479887784cdd657e4729b690)
#### Saturday 2023-02-25 10:47:04 by LLLida

Index buffer for voxels🤙

I was struggling a lot doing this. Anyway I did the thing saving us
~1/3 voxel memory in future. Code is not very complex, it's just me
being tired at night.

For some reason we have a ridiculous bug: sometimes when we launch the
application we get DEVICE_LOST error from Vulkan. This is very bad. I
have no idea why this is happening. If I wouldn't find the reason I
would just reboot my computer😎

---
## [LLLida/lidaEngine](https://github.com/LLLida/lidaEngine)@[bae2368a0d...](https://github.com/LLLida/lidaEngine/commit/bae2368a0da96f6e63b76cf61f4db8a438cbf94c)
#### Saturday 2023-02-25 10:47:04 by LLLida

Fix horrible device lost error😐

It's ridiculous. I wasn't getting VK_ERROR_DEVICE_LOST when I
implemented quad rendering system. Everything was OK. Then I moved to
implementing index buffer for voxels. That was the moment where I was
getting this stupid crash. I obviously thought that I'm doing
something wrong with voxel indices. Of course I didn't find the reason
and proceeded to implement index buffer with 60-80% crash rate. Then I
did some few code improving things and got crash rate to nearly
40-50%.

I'm happy that I found the bug and I'm terrified of the reason. I
forgot to initialise a pointer. Just a single pointer was getting me
random device losts🥰

---
## [durgaprasad123n/python_projects](https://github.com/durgaprasad123n/python_projects)@[ccfa576340...](https://github.com/durgaprasad123n/python_projects/commit/ccfa5763404370fb5fb5c6d266034453cbc8593c)
#### Saturday 2023-02-25 10:52:36 by durgaprasad123n

Add files via upload

Myntra Fashion Clothing 		
Aim
Myntra is a major Indian fashion e-commerce company headquartered in Bengaluru, Karnataka, India.] The company was founded in 2007 to sell personalized gift items. In May 2014, Myntra.com was acquired by Flipkart.
We will be using data science skills to identify the apparel type that customers favours and their prices. To identify the parameter that attracts customers to make purchase. 
Is it number of images, or colours, or brand name or price?
Problem Statement
The Myntra have shared the dataset with you to identify the attributes to increase sales. You are working as Lead consultant and your key role is to identify the parameters that are extremely important while making a decision.
As a lead consultant you also have to show the results to your client and managers so it’s advised to create charts while you perform analysis and write down the insights in some separate sheet that you can refer later on.
Some of the problems can be easily identified while solving the scenarios and tasks shared here but you are also required to further share your key points in the Conclusion.
Exploratory Data Analysis (EDA) is an approach to analysing data sets to summarize the main characteristics of data by often using statistical graphs and other visualization methods such as by the use of statistical graphs.
  

Learning Outcome
●	Pandas Joins and Merge
●	Data Manipulation
●	Data cleaning
●	Creating charts and bars
●	Perform wrangling operations to draw more insights
●	Evaluation of bi-columns on the basis of next attribute
●	Creating new columns to drill down on analysis

Data Information
There are 2 csv files that are shared here.
A.	Product Details
●	ProductID – ID assigned to the product
●	ProductName – Name of the Product
●	ProductBrand – Brand Name of the Product
 

B.	Products Catalog
●	Gender – gender to which specific products that have been designed
●	Price (INR) – Price of the products
●	NumImages  – Number of images that have been clicked for specific product
●	ID - ID assigned to the product
●	Description – full details of the product
●	PrimaryColor – Color of the product

 


Skill Requirement
●	numpy 
●	pandas 
●	matplotlib
●	seaborn 
 
Scenario1

You have been provided with 2 datasets. You will be learning here how to create the dataframe from 2 datasets and make some minor changes as required.
Recognize the attributes carefully and make sure they are aligned in proper format.
Task1
1.	Import all the relevant packages (Eg: Numpy, Seaborn...)
2.	Import the datasets into the python environment.
3.	Check the structure, statistics and other important functions. (Only observe the changes)

 Task2
1.	Create a new dataframe “df” by joining the 2 datasets
2.	Drop the duplicate data
3.	Check for missing values
Scenario2
You have successfully created the dataframe from the two input files.
Here we will be processing cleaning operations and intro to brief analysis.
Expected shape of the dataset: 12491 rows and 8 columns
Task
1.	There is a column that needs string strip operation. Identify that and apply it.
2.	Fill the missing value by ‘Others’ in the column containing it
3.	Since all the column names are single word so you can convert the ‘Price (INR)’ also to single name ‘Price’.
4.	Analyse the Gender column and include your viewpoints how to make it useful.

 
Scenario3
So far we have learnt the basics of the dataset and cleaned it as required. Over here you are going to perform deep analysis of the dataset with the help of data manipulation tricks as well as visualize the results. 
This is the most time consuming tasks and make sure you do perform proper analysis method. While answering the question against all the tasks, it will be great if you can create charts to support it also.
Expected shape of the dataset: 12491 rows and 8 columns
Task1
1.	Univariate analysis of each variable
2.	Bivariate Analysis of categorical vs numerical variables (Take target variable as fixed variable here)
3.	Multivariate Analysis of categorical and numerical variables
4.	Check distribution of variables
Task2
1.	Create a new Column “NewGender” to analyse further its distribution. Going forward we will consider this group for tasks
Logic Applied
i.	Include Boys & Men as Men
ii.	Include Girls & Women as Women
iii.	Include Unisex & Unisex Kids as Unisex
2.	Complete the analysis of NewGender along with other categorical cols.


Task3
1.	Create a new Column “DescriptionLength” to analyse further its distribution.
Logic Applied
i.	Each record of DescriptionLength is equal to the number of chars in Description

2.	Complete the analysis of DescriptionLength along with other categorical cols. 
3.	Isn’t it important to check if attribute information is also included in Description? Complete this task before answering it.

---
## [dsmith328/LC13Master](https://github.com/dsmith328/LC13Master)@[582f5b38cb...](https://github.com/dsmith328/LC13Master/commit/582f5b38cb9ad5d051cbea48af501089ba3f0206)
#### Saturday 2023-02-25 10:57:44 by Lance

Holy FUCK temporary commit

Mixed between previous abno based spawning and new subsystem

Cleanup Commit

Removes a lot of previous code and paves the way for the subsystem method.

Major Commit

Apocalypse Bird drops it's loot and only spawns once. It'll not try to happen if there aren't enough birds, and if two are breached before the third arrives it'll take the third breaching to start the event, until the others are suppressed. Birds do not target people and are immortal while moving to the portal. If unable to reach it after 3 minutes they'll be forced in manually.

Tweaked Proc

Redundant Code Removal

Remembered I didn't need this

Enhanced Code

Moved an if-statement to a better place to more adequately solve the issue.

Test Commit

Does this solution work?

Global Abnormality Mob List

Patrol Changes and Bird Grab changes

Gaming Test?

Temp Commit

Second Commit

Another Commit!

Fourth Commit

Subsystem changes. Dead abno cleansing. Lower speak cooldown. Debug text removal.

P-bird fix

Fixes P-bird able to die before reaching the portal

---
## [durgaprasad123n/python_projects](https://github.com/durgaprasad123n/python_projects)@[f30ccef78d...](https://github.com/durgaprasad123n/python_projects/commit/f30ccef78d135dbf585610ea40d945105c64ecd6)
#### Saturday 2023-02-25 11:01:53 by durgaprasad123n

Add files via upload

Introduction to Project


Aim

The main goal of Exploratory Data Analysis is to identify errors in data sets. Give a better understanding about the relationship between various attributes in the dataset. Thus, we will be able to schedule all the other processes accordingly.

Project explanation

Agriculture sector is one of the most significant sectors of Indian Economy. It is a crucial contributor accounting about 15% of the GDP. In agriculture sector where farmers and agribusinesses have to make innumerable decisions every day and intricate complexities involves the various factors influencing them. 

An essential issue for agricultural planning intention is the accurate yield estimation for the numerous crops involved in the planning. Exploratory Data Analysis are necessary for accomplishing practical and effective solutions for this problem. Agriculture has been an obvious target for big data. Environmental conditions, variability in soil, input levels, combinations and commodity prices have made it all the more relevant for farmers to use information and get help to make critical farming decisions.

Problem Statement Description

This dataset provides a huge amount of information on crop production in India ranging from several years across different states in India. Based on the Information the ultimate goal would be to predict crop production using powerful machine learning techniques.

Business Context

Historical crop yield information is also important for supply chain operation of companies engaged in industries. These industries use agricultural products as raw material, livestock, food, animal feed, chemical, poultry, fertilizer, pesticides, seed and paper.

 An accurate estimate of crop production helps these companies in planning supply chain decision like production scheduling.

Business such as seed, fertilizer, agrochemical and agricultural machinery industries plan production and marketing activities based on crop production estimates. 

There are 2 factors which are helpful for the farmers and the government in decision making namely:

It helps farmers in providing the historical crop yield record with a forecast reducing the risk management.
It helps the government in making crop insurance policies and policies for supply chain operation.
Exploratory Data Analysis plays a vital role in the analysis of data. Exploratory Data Analysis is the computing process of discovering patterns in large data sets involving methods at the intersection of artificial intelligence, machine learning, statistics, and database system.

Data Explanation.

This is the basic view of the dataset - link

State-wise Crop Production in India for 2000 to 2014

It also gave information about different seasonal crops at district level and area of cultivation along with total crop production. India being agriculture rich country, this data will have lots of minor and major facts which will help in charting a next successful agriculture revolution after 1965. 

Doing an exploratory data analysis of this dataset would give insights into Indian agriculture status: state-wise, district-wise, crop-wise, area-wise and levels of productions. A complete analysis will paint a beautiful story of this important aspect of India.

Dimensions of the dataset is 246091 rows and 7 columns.

---
## [claydegruchy/wfrp-map-osm](https://github.com/claydegruchy/wfrp-map-osm)@[0e589a7538...](https://github.com/claydegruchy/wfrp-map-osm/commit/0e589a7538c9ebadb0557bc0c61a985b9c59cc66)
#### Saturday 2023-02-25 11:29:15 by clay

fuck shit fucking tailwind overcomplicated motherfucker of a system make it fucking simple, dont make me learn some entirely new, janky css shit, might as well write it myself, at least the garbage always stays in one file isntead of being smeared over hte entire project FUCK

---
## [Danielkaas94/DTAP](https://github.com/Danielkaas94/DTAP)@[fa4754750f...](https://github.com/Danielkaas94/DTAP/commit/fa4754750fac5b8ea43ebcfce180e4be04e70c9a)
#### Saturday 2023-02-25 13:18:04 by Danielkaas94

✝ The Day We Meet Again ✝
The day we meet again
I'll be waiting there
I'll be waiting there for you
'Cause the years have been so lonely
Like a dog without a home
It's dangerous when you find out
You've been drinking on your own

The day we meet again
We will walk in peace
Through the garden down the road
Where the mist of time is lifting
See it rising in the air
Like the shadow I was chasing
When I looked, it wasn't there, oh, no

Just in case you're wondering
What was really on my mind
It wasn't what you took, my love
It's what you left behind

And just in case you're wondering
Will it really be the same?
Will it really be the same?
You know we're only living for the day me meet again

So hold, hold on and don't let go
Time, it heals, you know, I know

The day we meet again
I'll be waiting there
I'll be waiting there for you
'Cause the years have been so lonely
Like a dog without a home
It's dangerous when you find out
You've been drinking on your own

The day we meet again
We will walk in peace
Through the garden down the road
Where the mist of time is lifting
See it rising in the air
Like the shadow I was chasing
When I looked, oh, no, it wasn't there, oh, no
It wasn't there, it wasn't there

It wasn't there, oh, no; oh, no; oh, no

---
## [jandaX/android_kernel_xiaomi_joyeuse](https://github.com/jandaX/android_kernel_xiaomi_joyeuse)@[543af705b8...](https://github.com/jandaX/android_kernel_xiaomi_joyeuse/commit/543af705b87748d4517391fa50638a8211d1bb0e)
#### Saturday 2023-02-25 13:42:07 by Peter Zijlstra

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
Change-Id: Idd54334615da4c78698ca8b3b12b514ae9d8360f
Signed-off-by: Alexander Winkowski <dereference23@outlook.com>

---
## [Gold3729/rustest_bander-version](https://github.com/Gold3729/rustest_bander-version)@[6d158bd3b3...](https://github.com/Gold3729/rustest_bander-version/commit/6d158bd3b37bba2cb2cec2a27fdb0b9b7d8275ac)
#### Saturday 2023-02-25 14:01:20 by spockye

beach ruin, The Treasure Cove! (#1701)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR adds a new Beach ruin, Treasure Cove. 

![2023 01 17-11 26
30](https://user-images.githubusercontent.com/79304582/212874736-b17917a5-876e-4a7a-a073-1581cc394b8e.png)

![2023 01 17-11 26
58](https://user-images.githubusercontent.com/79304582/212874824-9a161419-b751-41d2-a82d-e50f06981025.png)


![image](https://user-images.githubusercontent.com/79304582/212879021-bcdc2238-b50b-48c2-9cd0-d17cccbd50dc.png)

Loot: 
cm-16 rifle (main loot)
energy gun
pirate sabre
frontiersmen hardsuit
misc combat supplies
secret documents
2x abandoned crates
research note / tesla researcher
basic engineering supplies (smes/tools/autolathe/battery charger)
two boats
silver crate / hidden gold crate
misc junk
______
Threat: 
1x spacesuit ranged pirate
2x sword pirates
1x ranged pirate
punji sticks
_____

Lore tidbit:
This "humble abode" is the home of our 5- now 4 Pirate friends! After a
mildly successful raid on a CMM VIP transport, they managed to take a
Cargo tech (the VIP), and a CMM guard as hostage. sadly it didn't all go
as planned, and the CMM officer managed to free himself and killed one
of the pirates. This is where you now find the cave, with both hostages
executed, their brother buried, and the pirates grieving his unfortunate
passing.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [x] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
more ruins = good.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Adds a new beach ruin, the beach_treasure_cove
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
Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [selliott512/freedoom](https://github.com/selliott512/freedoom)@[3efe8a0e41...](https://github.com/selliott512/freedoom/commit/3efe8a0e4114414d764d4a1f03400a9a0f2094dd)
#### Saturday 2023-02-25 14:37:26 by mc776

levels: fix various bugs. (#871)

* levels: fix various bugs.

Thanks to Goji!, Inuk and rednakhla on Discord for pointing these out.


E1M3: Northern lift simplified to address texture alignment problems.

E1M5: Door near (-205,1336) (leading out into open ceiling area with the big strip of lights down the middle) door tracks needed to be lower unpegged.

E1M9: Lift near (-2328,120) was split into 2 sectors, causing HOMs when they went out of sync. There's nothing that relies on this split (contrast the neat lighting stuff from Map22) so the lift is just merged into one sector.

E2M2: Shellbox near (-486,192) is right on the line between two stairs, causing it to rest on the bottom step which causes ports like GZDoom to have the sprite clip *very* visibly into the upper stair. Moved it slightly so it rests on the upper of those two stairs.

E2M3: Door leading to red key and "door" leading to soulsphere: former should be lower unpegged but latter should not, but were reversed. Two exit-door-textured doorframes also given more conventional DOORTRAK and lower unpegged treatment. The teleporter representing the hatch going down into the nukage is now fully repeatable.


Map07: Infinite height in vanilla would cause the spectres in the red key courtyard to trap the player on the entrance ledge from below in a way that could not be seen or diegetically explained. Those three spectres now warp in only after you cross the ledge. (Setting them to "ambush" would do nothing since you're in LOS with them from the top of the ledge.)

Map11: Lights above red keycard weren't aligned; moved that entire sector and added a few lines to round the corner. Removed a strobe effect on the exit teleporter to compensate for a GZDoom issue where the light would go to absolute zero during the blink.

Map12: Room to the south with the 2 stimpacks, ammo boxes, 2 chaingunners and berserk would sometimes cause some of the items to be "levitated" to the highest sectors they touch. Moved them away from said higher sectors - it looks a bit sloppier but this is a backroom not a storefront lol.

Map13: The easternmost archvile platform had the archvile stuck in the seam, preventing it from lowering in vanilla. (Worked fine in GZDoom) Moved it a little further in.

Map19: The combat slugs teleport in from a W1 teleporter which could sometimes be spent while one of the pinkies is blocking the destination, permanently preventing that slug from teleporting in. These are now WRs like the other teleporting enemies.

Map22: More W1 monster teleports that should be WR. Also filled in some missing textures in the multi-sector lift connecting the cavern to the hall in the southwest, which parts are clearly not meant to be seen moving separately but can - it still looks fucked up if you manage to desync them, but it's a diegetic fucked up now.

Map24: Another W1 spawn. This one is impossible to screw up in vanilla, but there are some mods that could end up spawning something there that could block the archviles from teleporting.

Map25: More W1 problems. The spawn source room now also has a small barrier to make sure each pinkie only goes to its own teleporter unless the initial teleport fails.

Map27: Lizardbaby dropping too far meant that the bracket was falling along with it in a visibly unnatural way.

Map29: Broke up all the long linedefs on the perimeter of the map to get around the invisible hitscan barrier bug: https://doomwiki.org/wiki/Hitscan_attacks_hit_invisible_barriers_in_large_open_areas
(Ideally this entire perimeter should be redone to break up the box in favour of more natural-looking formations, but that's a bit outside the scope of a fix like this.)


Also got rid of the Plutonia-style start/end teleports on the fixed Phase 2 maps, to address #867.

* maps: more fixes.

More floaty items and other things.

E1M9
- floater mid south stim by staircase
E1M7
- floater northwest clips near the tunnels
- floaters near switch by railings, now all on the railings
- duckproofed sector 439 barrier
E2M9
- floater thing #125 medikit on top of lift, now in middle of platform
- shotgun guy (thing #309) and the spectre behind it stuck in geometry.
- lines 430 and 761 both open the same door and are in the same room right next to each other. Since 761 is actually textured and positioned as a switch, the tag and special on 430 is removed.

* levels: flag e2m7 DM stuff as multi-only.

Marked the following based on eyeballing out what items are right next to DM spawns with no obvious alternate route to them: 487, 488; 203, 397; 499, 500, 501, 502; 482, 485; 491, 492, 493; 494; 496; 28, 486; 182; 54

* levels: more misc. fixes.

E1M6 W1 lines 2318 and 2321.

E3M5 Removed all monster block lines in that gross blood room and raised the blood floor to only 4 below the normal floors, but flagged more monsters in there as ambush to make up for it. Also fixed a lot of texture alignment issues in the top skin panels and lowered the ceiling, along with adding a new sector to address texture tiling issues in the northern teleporter room.

E4M1 fixed a mysterious HOM that was going on near the northern shadow line in the northern outdoor area. Merged a lot of sectors that were identical in their properties.

E4M7 entrance to sector 985 seems to be intended that the player run off the ledge into that room, then the pinkie near the ledge ambushes the player from behind. Instead, what sometimes happens is that the pinkie is alerted somehow, then obstructs the player (vanilla infinite height) from being able to get down there. That means of getting down into that room is now walled off, and instead you step onto that lift to bring it down from above. Neat side effect: any monsters still in the ring when you enter that room will follow you down there.

E4M5 linedefs 1724 and 1725 were facing the wrong way and couldn't be hit with projectiles.

Map25 Float thing 217. Moved that entire row further south to address floating item issues.

Map28 Float thing 464.

* levels: use inner room texture in E4M7 lift.

* levels: align side textures on that lift.

Didn't realize the little squares were sticking into the floor at the *bottom* of the lift as well.

---
## [Jackraxxus/tgstation](https://github.com/Jackraxxus/tgstation)@[296ca23aa1...](https://github.com/Jackraxxus/tgstation/commit/296ca23aa1d8531fba291eb9b802b7282fee657b)
#### Saturday 2023-02-25 17:13:00 by Jacquerel

Most actions cannot be used while incapacitated (#73513)

## About The Pull Request

Fixes #39775
The `TRAIT_INCAPACITATED` trait is intended to block you from acting but
does not inherently block actions. Actions only check for "conscious",
"has available hands", "immobile", or "lying down".
Most actions still _can't_ be used while incapacitated. This is because
most actions are spells, most spells have invocations, and you can't
talk while you are incapacitated. This is silly.

I have resolved this by adding a new flag which blocks actions while
incapacitated. This is somewhat redundant with "conscious" because most
sources of that also make you incapacitated but not _always_, you might
want the specificity.

I have tried to be discerning about where this flag is applied, it is
not in all cases (for instance you can still swallow implanted pills
while incapacitated and such), but it's not only possible but I can't
really avoid implementing this without it being a balance change in
_some_ cases,

Actions this effects are things such as:
Xenomorph Tail Sweep, Lesser Magic Missile (cult constucts), Heretic
Shadow Cloak, the Smoke spell in general, Conjuring (but not firing)
Infinite Guns, Mime spells

Times when these actions will no longer be available but were previously
are such times as when the mob is:
Stamina Crit, Stunned, Paralysis, and Time Stopped.

## Why It's Good For The Game

The incapacitated trait is applied by effects which should block acting
but still permits several actions which logically would be prevented.
This fortunately hasn't come up too often due to the high ratio of
actions with invocations, but it feels bad to stun someone and then have
them still able to perform an action they logically wouldn't be able to
take while stunned.
This is especially egregious in the case of Time Stop (the only way to
stun a lot of the mobs effected by this) but that's a rare pick on a
rare antagonist and would also rarely be used on these mobs, so a bit of
an edge case.

## Changelog

:cl:
fix: Many spell-like abilities which could be stunned, paralysed, or
frozen in time now cannot be.
/:cl:

---
## [MM2-0/Kvaesitso](https://github.com/MM2-0/Kvaesitso)@[c664f2e777...](https://github.com/MM2-0/Kvaesitso/commit/c664f2e777df4226ae47988fd95d250f126f12af)
#### Saturday 2023-02-25 17:31:27 by MM20

Fuck you Android studio, please fix your goddamn focus, I wanted to type into the terminal, not the editor

---
## [clintjedwards/gofer](https://github.com/clintjedwards/gofer)@[b216d820fd...](https://github.com/clintjedwards/gofer/commit/b216d820fd512e0b77b4d6d9215fda8a561f24d5)
#### Saturday 2023-02-25 17:32:38 by Clint J Edwards

feat: Pipelines are now versioned

In order to eventually have canary-able deployments in Gofer we must
first support versioned pipelines.

This allows us to:
* Have a good target in which to roll back and forward.
* Understand what we are gaining and losing on each change.
* Track each update as it happens.

This is not easy though as pipelines have parts which are easy to version
(namely the config) and parts which are much harder to version (how do
we handle the cutting over of triggers?).

Because of this nuance, we've had to redesign a lot of earlier
assumptions for how Gofer models worked. This was a major refactor and
since I was here I made a few other large sweeping changes.

* Full storage package refactor: The storage layer was hard to use,
brittle, and inflexible. I've refactored it, leaning a bit more on
sqlx and going back to basics. I tried to make the storage package
work in the past by keeping the domain models to a minimum. I've since
learned this does not work once things become reasonably complicated. One
of the main refactors to the storage package is the introduction of
dedicated storage models. This means that I have to write a bunch of
boilerplate code to switch from in-memory models to the storage ones,
but the looser coupling is worth it. More storage refactors coming
as I learn what works at large scale and what doesn't.
https://github.com/go-jet/jet looks interesting.

* Removal of Triggers as Pipeline configuration: I desparately wanted
to have pipeline configurations encompass everything a pipeline would
have to offer, so that it was easy to look at a config and know exactly
what was going on in a particular pipeline. Triggers were a pain in the
ass though. Triggers unfortunately occupy a very special place in Gofer's
archetecture. Without triggers nothing really gets done. And so allowing
the user to apply all the same functionality to triggers as they would
with any other deployment was short-sighted. Triggers don't make a lot
of sense as a canary deployment. Triggers aren't ephemeral, they are
either on or their off. No in-between.

Instead Triggers can now be added to your pipeline via the command line.
This way trigger subscriptions aren't held down by the paradigms of
configuration change.

* Pipelines are now versioned: Not only have we added versions to pipelines,
but they now have deployments and configurations and metadata and a lot
of smaller loosely coupled parts so that they aren't a huge data monolith.
This means a lot of breaking changes for outward (and inward for that matter)
apis.

* Just lots of general breakages everywhere: Pretty much a large percentage
of things just aren't the same anymore.

---
## [Saiswetha20/Basics-of-java](https://github.com/Saiswetha20/Basics-of-java)@[87fa1bfc58...](https://github.com/Saiswetha20/Basics-of-java/commit/87fa1bfc58f4ff5b4943758c86c65eb49faccf0e)
#### Saturday 2023-02-25 17:33:46 by Saiswetha20

Three.java

Ajay, Binoy and Chandru were very close friends at school. They were very good in Mathematics and they were the pet students of Emily Mam. Their gang was known as 3-idiots. Ajay, Binoy and Chandru live in the same locality. A new student Dinesh joins their class and he wanted to be friends with them. He asked Binoy about his house address. Binoy wanted to test Dinesh's mathematical skills. Binoy told Dinesh that his house is at the midpoint of the line joining Ajay's house and Chandru's house. Dinesh was puzzled. Can you help Dinesh out? Given the coordinates of the 2 end points of a line (x1,y1) and (x2,y2), write a program to find the midpoint of the line.

---
## [nushell/nushell](https://github.com/nushell/nushell)@[378a3ae05f...](https://github.com/nushell/nushell/commit/378a3ae05f5459a64f97af3781d4336c35652db4)
#### Saturday 2023-02-25 17:36:53 by Kovacsics Robert

Use `with-env` to avoid calling external command on invalid command (#8209)

# Description

My terminal emulator happens to be called `st`
(https://st.suckless.org/) which breaks these tests for me

_(Thank you for improving Nushell. Please, check our [contributing
guide](../CONTRIBUTING.md) and talk to the core team before making major
changes.)_

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes

_(List of all changes that impact the user experience here. This helps
us keep track of breaking changes.)_

# Tests + Formatting

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
## [hrzntal/fledermaus](https://github.com/hrzntal/fledermaus)@[90435a56b3...](https://github.com/hrzntal/fledermaus/commit/90435a56b3d4292306a5a0317b4636026aba5269)
#### Saturday 2023-02-25 18:13:45 by SkyratBot

[MIRROR] Smoothing groups optimization, save 265ms with configs, more on production & w/ space ruins [MDB IGNORE] (#18189)

* Smoothing groups optimization, save 265ms with configs, more on production & w/ space ruins (#71989)

This one is fun.

On every /turf/Initialize and /atom/Initialize, we try to set
`smoothing_groups` and `canSmoothWith` to a cached list of bitfields. At
the type level, these are specified as lists of IDs, which are then
`Join`ed in Initialize, and retrieved from the cache (or built from
there).

The problem is that the cache only misses about 60 times, but the cache
hits more than a hundred thousand times. This means we eat the cost of
`Join` (which is very very slow, because strings + BYOND), as well as
the preliminary `length` checks, for every single atom.

Furthermore, as you might remember, if you have any list variable set on
a type, it'll create a hidden `(init)` proc to create the list. On
turfs, that costs us about 60ms.

This PR does a cool trick where we can completely eliminate the `Join`
*and* the lists at the cost of a little more work when building the
cache.

The trick is that we replace the current type definitions with this:

```patch
- smoothing_groups = list(SMOOTH_GROUP_TURF_OPEN, SMOOTH_GROUP_FLOOR_ASH)
- canSmoothWith = list(SMOOTH_GROUP_FLOOR_ASH, SMOOTH_GROUP_CLOSED_TURFS)
+ smoothing_groups = SMOOTH_GROUP_TURF_OPEN + SMOOTH_GROUP_FLOOR_ASH
+ canSmoothWith = SMOOTH_GROUP_FLOOR_ASH + SMOOTH_GROUP_CLOSED_TURFS
```

These defines, instead of being numbers, are now segments of a string,
delimited by commas.

For instance, if ASH used to be 13, and CLOSED_TURFS used to be 37, this
used to equal `list(13, 37)`. Now, it equals `"13,37,"`.

Then, when the cache misses, we take that string, and treat it as part
of a JSON list, and decode it from there. Meaning:

```java
// Starting value
"13,37,"

// We have a trailing comma, so add a dummy value
"13,37,0"

// Make it an array
"[13,37,0]"

// Decode
list(13, 37, 0)

// Chop off the dummy value
list(13, 37) // Done!
```

This on its own eliminates 265ms *without space ruins*, with the
combined savings of turf/Initialize, atom/Initialize, and the hidden
(init) procs that no longer exist.

Furthermore, there's some other fun stuff we gain from this approach
emergently.

We previously had a difference between `S_TURF` and `S_OBJ`. The idea is
that if you have any smoothing groups with `S_OBJ`, then you will gain
the `SMOOTH_OBJ` bitflag (though note to self, I need to check that the
cost of adding this is actually worth it). This is achieved by the fact
that `S_OBJ` simply takes the last turf, and adds onto that, meaning
that if the biggest value in the sorting groups is greater than that,
then we know we're going to be smoothing to objects.

This new method provides a limitation here. BYOND has no way of
converting a number to a string at compile time, meaning that we can't
evaluate `MAX_S_TURF + offset` into a string. Instead, in order to
preserve the nice UX, `S_OBJ` now instead opts to make the numbers
negative. This means that what used to be something like:

```dm
smoothing_groups = list(SMOOTH_GROUP_ALIEN_RESIN, SMOOTH_GROUP_ALIEN_WEEDS)
```

...which may have been represented as

```dm
smoothing_groups = list(15, MAX_S_TURF + 3)
```

...will now become, at compile time:

```dm
smoothing_groups = "15,-3,"
```

Except! Because we guarantee smoothing groups are sorted through unit
testing, this is actually going to look like:

```dm
smoothing_groups = "-3,15,"
```

Meaning that we can now check if we're smoothing with objects just by
checking if `smoothing_groups[1] == "-"`, as that's the only way that is
possible. Neat!

Furthermore, though much simpler, what used to be `if
(length(smoothing_groups))` (and canSmoothWith) on every single
atom/Initialize and turf/Initialize can now be `if (smoothing_groups)`,
since empty strings are falsy. `length` is about 15% slower than doing
nothing, so in procs as hot as this, this gives some nice gains just on
its own.

For developers, very little changes. Instead of using `list`, you now
use `+`. The order might change, as `S_OBJ` now needs to come first, but
unit tests will catch you if you mess up. Also, you will notice that all
`S_OBJ` have been increased by one. This is because we used to have
`S_TURF(0)` and `S_OBJ(0)`, but with this new trick, -0 == 0, and so
they conflicted and needed to be changed.

* Sorting how did I miss it

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>
Co-authored-by: Funce <funce.973@gmail.com>

---
## [RonSheely/Xyce](https://github.com/RonSheely/Xyce)@[87f47161f7...](https://github.com/RonSheely/Xyce/commit/87f47161f72bc2b56de8cb04fb01bf854d7a885e)
#### Saturday 2023-02-25 19:02:35 by Tom Russo

Let configure detect ABI clashes

Ever since the very first commit of configure.ac (f5ebf77, back in
2002), after hunting down all required libraries, Xyce's configure
does a simple check to see if the entire link line actually works.
This was something that Tammy Kolda had suggested back in those days,
and I took her advice.

Thing is, when configure is hunting down libraries it's already trying
to link small programs with them, so this test has always been
pointless.  All it does is make sure the libraries can be found, which
honestly we already did earlier.

And worse, ever since we started using the Trilinos Makefile.export
thing instead of probing libraries normally, we NEVER actually link
meaningful test programs with trilinos anymore.

This means that while the libraries are found and a link of a trivial
program succeeds, it could be the case that Trilinos has been compiled
with a compiler that uses an ABI that is incompatible with the one
we're trying to use now.

This came up this weekend (again) when Eric tried to build Xyce on one
of the ASCIC machines and tried to use our precompiled Trilinos
archdir for gcc8.  These libraries were compiled with RHEL7 devtools-8
gcc 8.3, but Eric was using CDE gcc 8.4.

RHEL devtools gcc8 is compiled to use the old GCC ABI for compatibility
with the native gcc4, but CDE gcc 8.4 is compiled with the default,
new ABI.  It is not possible to use one with the other unless special
macros are defined to make it use the the non-default ABI.

And because we were only testing whether libraries would link by
linking an empty main function with the libraries, no Trilinos
functions are actually needed and so the linker never pulls them in
and tries to use them.

So configure succeeds, the build proceeds all the way to the final
link phase, and then a semi-infinite number of undefined symbole
errors show up.  It is frustrating and confusing for a user to have
that happen.

In this commit, I change this 20-year-old pointless link test into a
meaningful link test.  Now, configure tries to build a small test
program that includes Teuchos_RCP.hpp and tries to instantiate an
RCP.  This is a real test --- if the Trilinos libraries are
incompatible, this will fail, and fail before the user has bothered to
try to build Xyce.

if it fails, the user will get the message:
checking whether libraries (-lfftw3  -llocaepetra ...  ) will link... no
configure: error: FATAL: cannot link with the libraries detected so far ...
It may be that your compiler is incompatible with the one that was
used to build Trilinos.  See config.log for failure message.

That final error message used to include the entire list of libraries,
but that list is so freakin' long it makes the error message
unreadable (the beginning of the message scrolls off the screen before
the end of it gets printed).  So I shortened it.  The full list is in
the previous message anyway.

And config.log will have all of those undefined symbol errors instead
of them showing up at final link time of the full build.

This does not guarantee we won't get annoyed queries from users who
hit this problem, but it at least gets that frustration to
happen *before* they've spend an hour or so compiling Xyce.

---
## [TingTingShao/java_assignment_2022](https://github.com/TingTingShao/java_assignment_2022)@[f9ea7f722a...](https://github.com/TingTingShao/java_assignment_2022/commit/f9ea7f722a8ffc6515683f559c636527e2efcc7b)
#### Saturday 2023-02-25 19:13:32 by TingTingShao

Create README.md

For the purpose of this assignment, you need to implement 2 types of alignments: the standard alignment as discussed above, and what we will refer to as a SNiP or SNP alignment. An SNP alignment is a different way of representing the same data as in the standard alignment, i.e., no separate input file is required from which to read a SNP alignment as you can obtain it directly from the standard alignment. Compared on a reference sequence, which is shown in full (see screenshot below) as in the standard alignment, only the (nucleotide) differences in the other genomes are shown, while identical nucleotides are represented as a dot (‘.’).

Each alignment type needs to support at least the following operations:
- search through the genomes for a specific sequence of characters (e.g., AACAAATG) and return the corresponding names / identifiers for those genomes in which the sequence can be found
- replace a genome in the alignment with a new sequence (i.e., a genome that was previously not part of the alignment and that has a name / identifier that was not part of the initial FASTA file)
- in a given genome, replace all occurrences of a given sequence of characters by a new sequence of characters (without changing the total length of the genome)
- in the entire alignment, replace all occurrences of a given sequence of characters by a new sequence of characters (without changing the total length of the alignment)
- adding a genome with its corresponding name / identifier
- removing a genome, based on its name / identifier
- other functions that you think are useful to edit an alignment
It will be important to think about what effect some of these methods will have on the different alignment implementations. Finally, and to be 100% clear: you do NOT need to develop a graphical interface / visualisation of the alignment(s) as part of this assignment. The images provided above (from AliView) only serve to explain the data you will be working with.
Description of the text (.txt) input file
A bioinformatics team consists of a potentially large number of users that each have their own responsibilities and possible tasks they can perform. An example input text (.txt) file is provided on Toledo, describing each team member by her/his function, first and last name , and years of experience in the team. You can assume that a team member has a first and last name that consists of only one single word (without special characters).
The goal of your application is to construct a standard alignment for each bioinformatician to work on, based on the data in the provided .fasta file. Both the .fasta and the .txt file can only be read in once! The .fasta file also serves as the input to create the optimal alignment that is stored in a repository, which is initially identical to each of the bioinformaticians’ alignments. The repository also contains the SNiP alignment that always corresponds to the current version of the optimal alignment. Only the team lead(ers) and the technical support members have access to the repository. The team lead(ers) and technical support can query the repository for each user’s personal alignment, but they cannot retrieve (nor directly access) the optimal alignment nor the SNiP alignment from the repository.
As you have been able to deduce from the previous paragraphs, there are three types of team members:
- bioinformaticians, who only have access to their own personal alignment (that can change over time due to editing operations), but not to the repository
6
Introduction to Object-Oriented Programming 2022-2023
- team lead(ers), who have direct access to a repository that contains the optimal alignment (with the lowest score), its corresponding SNiP alignment and the personal alignment of each bioinformatician, i.e., the team lead(ers) do not have their own alignment to work on but can select the alignment of any user to be promoted as the optimal alignment based on a simply ‘difference score’ criterion; the team lead(ers) are not able to retrieve the optimal alignment nor the corresponding SNiP alignment from the repository, but the alignment from each specific user can be retrieved
- technical support, who have direct access to the same repository as the team lead(ers); however, the functions of technical support members restrict themselves to backing up, restoring and removing / clearing the data in the repository
The following functions / operations need to be provided for the bioinformaticians and the team lead(ers), but not for the technical support crew:
- write data to file: for bioinformaticians, this means writing their own personal alignment to an output text file, of which the name is simply their first name + their last name with a .alignment.txt extension; for team lead(ers), this means writing all of the users’ alignments to one single file with the same naming convention
- write a report to file: for bioinformaticians, this means writing the difference score (see below for more information) for their own personal alignment to an output text file, of which the name is simply their first name + their last name with a .score.txt extension; for team lead(ers), this means writing all of the users’ alignments scores to a file with the same naming convention
The ‘difference score’ of an alignment is a simple metric to compute. Basically, you use one of the genomes in the alignment as the reference genome (typically the first / top genome) and compute the number of different positions / characters of each other genome compared to that reference genome. Add up all of those numbers to obtain the difference score. Importantly, this difference score also needs to be defined for the SNiP alignment! You can – for example – have this score computed in your main method to show how you have implemented this aspect.
The following functions / operations need to be provided specifically for the bioinformaticians:
- the functions that enable changes to the alignment, as listed above
- retrieving the personal alignment (from that bioinformatician)
The following functions / operations need to be provided specifically for the team lead(ers):
- copy a user’s alignment to the optimal alignment in the repository (note that this will also affect the SNiP alignment); after this operation has been performed, changes to the user’s alignment do not affect the optimal alignment (nor the other way around)
- overwrite a user’s alignment with the optimal alignment; after this operation has been performed, changes to the user’s alignment do not affect the optimal alignment (nor the other way around)
The following functions / operations need to be provided for the technical support members:
7

Introduction to Object-Oriented Programming 2022-2023
- backup the repository data: a hard / deep copy of the current optimal alignment, its corresponding SNiP alignment and, for each user, her/ his personal alignment; whenever such a backup is made, the date and time of the backup procedure is stored as an instance variable for the technical support member
- restore the repository data: reinstating the backup data, and hence overwriting the contents of the current optimal alignment, its corresponding SNiP alignment and, for each user, her/ his personal alignment
- clearing the repository data: removing / emptying the current optimal standard alignment, its corresponding SNiP alignment and, for each user, her/ his personal alignment
The goal of the application is to provide the opportunity for each bioinformatician to work on their own personal alignment independently, through the operations mentioned earlier in this document. As such, each bioinformatician starts off with a personal copy of the same initial standard alignment, which she/he can independently work on and make changes to. As different bioinformaticians perform different operations on their personal alignment, they can hence end up with different alignments during the course of their work. The initial alignment also serves as the initial optimal alignment in the repository and as a source for creating the initial SNiP alignment. None of the users, regardless of their function, is able to edit the optimal alignment(s) directly, as the optimal alignment can only be copied as a whole, as described above in the functions for the team lead(ers).
Description of the application / main method:
First of all: provide sufficient comments in the code, especially in your main method, but also throughout the other classes you decide to implement.
In your main method, the goal is to show how the different classes you decide to implement work together, and also what their main features are and how to use them. For example, start by reading in the two input files, constructing the required alignments (and printing them after having done so) and users, and have each user perform a number of tasks as described in this document. Then have the team lead(ers) and technical support personnel come in and perform a few tasks (as described above), after which the bioinformaticians can continue working on their alignments. A short (incomplete) example of what the output could look like is shown here (but yours should be more extensive / elaborate):
...
SNiP alignment:
>1992.A1.UG.92.UG029 ....C..A...........................G......C.......C........A....................T.....G.G..... (full line not shown) >1998.A1.UG.98.98UG57135 ....C...................................T...T..............A.........G..................G......A.. (full line not shown)
8

Introduction to Object-Oriented Programming 2022-2023
>1998.A1.UG.98.98UG57136 ....C.........C............................................A.........G..................G......A... (full line not shown)
alignment score = 34443
SNiP alignment score = 34443
Replacing TTTTC with TTTTT in genome 1998.A1.UG.98.98UG57136 Marc Janssens's alignment score = 34444
Promoting alignment from Marc Janssens to shared alignment Copying shared alignment to Werner Lippens
Werner Lippens 's alignment score = 34444
...
Providing input to your implementation:
At this point, the only aspect left to discuss for your application is how to instruct your implementation which text and FASTA file to read. Hard coding file names into your application should be avoided, and there are various options available to achieve this. The easiest one would be to provide this information via the program / command-line arguments, but you can also make use of a properties file. Which of these approaches to implement is entirely up to you and does not affect your score in any way. You may assume the presence (and name / location) of such a properties file in your implementation if you so choose. More information can be found here (for example):
https://www.jetbrains.com/help/idea/properties-files.html
https://stackoverflow.com/questions/30010833/creating-a-properties-file-in-java-and- eclipse/30010882
For this assignment and the specific files discussed in this document, such a properties file (typically named config.properties) only needs to contain two lines of key-value pairs:
teamfilename=team.txt fastafilename=hiv.fasta
Important: both input files should only be read in once at the start of your program / implementation. In your main program, show how to use the functionality you have implemented in the different classes of your implementation and how the different classes are to be used together.
Important: make sure that you use relative paths to the file that needs to be read so that your application works directly when copying your Eclipse / IntelliJ project files. Hard coding the location of the file into your implementation is considered poor practice.
   9

Introduction to Object-Oriented Programming 2022-2023
Key points when implementing the assignment:
The structure of your code is the most important evaluation for the project. This means you should take care to include as many of the object-oriented concepts covered in the course whenever applicable. That also means thinking about future extensions of your implementation and keeping an eye on possible code reuse (outside of the current assignment).
Watch out for plagiarism! Online you may find similar partial implementations which you may use for inspiration, but you must write your own code! Note that many code examples you can find online are poorly written and/or poorly designed.
We realize that design patterns such as Model-View-Controller are not part of the course material, and you are not meant to study this material for the project; you are however required to think about properly structuring your project code.
Do not implement your project with solely the provided input files and their dimensions / number of lines in mind. Your project should run fine with a different .fasta and .txt files as well. Avoid hard coding aspects that relate to the specifics of these files at all cost.
Finally, aim for a well-designed / well-structured project with cleanly written code, organized in different packages. As stated before, clearly state in the project if you were unable to provide certain requested aims of the project and provide some information (what did you try and where did it go wrong).
Questions can be asked on the Discussion Board in Toledo.
Report Guidelines
You should prepare a short report of maximum 4 pages detailing important components of your project. It should include the following information:
• Write a short description of every class, indicating what functionality is included in each class.
• Describe the relationship between your classes (this may be text and/or a simple diagram, but not a UML diagram), for example, inheritance relationships or method calls from one class to another.
• If you are unable to implement a certain part of the game, we encourage you to make a sensible decision, be upfront about this decision (i.e., explain it in your report) and explain what the main difficulty was. Additionally, if you encounter implementation difficulties or time constraints, it’s better to fully and correctly implement a subset of the functionality rather than to implement small parts of each of the targeted program parts.
• Discuss what you think are the strengths and weaknesses in your project but focus on code design when doing so and not on how the application looks. Describe any difficulties you faced while working on the project.
10

---
## [JasmineRickards/T.E.-station](https://github.com/JasmineRickards/T.E.-station)@[7dccb4c5ce...](https://github.com/JasmineRickards/T.E.-station/commit/7dccb4c5cef5ff2286ef31f80126d13e01153cac)
#### Saturday 2023-02-25 19:56:25 by JasmineRickards

Merge pull request #3 from IFuckedUpMerging/oh-god-i'm-stupid

Buffs pay for all Species, minus humans, and nerfs monkey payday

---
## [midtsveen/midtsveen.github.io](https://github.com/midtsveen/midtsveen.github.io)@[d9c03cc197...](https://github.com/midtsveen/midtsveen.github.io/commit/d9c03cc19775fbdb8407b95f3b4342c9c98ce11a)
#### Saturday 2023-02-25 20:43:44 by Erik Leander Midtsveen

Yes

ZOË is a fantastic French singer whose music always fills me with joy. Her upbeat melodies and infectious energy never fail to put me in a good mood, and her voice is like a ray of sunshine on a cloudy day. I listen to her music whenever I need a pick-me-up, and she's the only artist who's ever moved me to tears with the beauty of her songs. I'm grateful for the happiness and positivity she brings into my life through her music.

---
## [VinierAardvark1/Tactical-Intervention---RMC-Branch](https://github.com/VinierAardvark1/Tactical-Intervention---RMC-Branch)@[b7d84d78e5...](https://github.com/VinierAardvark1/Tactical-Intervention---RMC-Branch/commit/b7d84d78e58851bc5baab0eccb3e20642decf1ae)
#### Saturday 2023-02-25 21:27:11 by Jayrazer

"this took too long" yeah fuck you

fuck you fesi fuck you i hate you meanest ever *gives you massive kiss* yeah fuck you

---
## [dsmith328/LC13Master](https://github.com/dsmith328/LC13Master)@[fc5dba0784...](https://github.com/dsmith328/LC13Master/commit/fc5dba078416e86fbb33a8ccd1b3c52747b294dd)
#### Saturday 2023-02-25 21:37:42 by Lance

Servant of Wrath

Records and Instability

Dash speed up

Fuck you I'll space indent all I like

There was some fuckin lint in this PR

God damned there's a lot of lint in here

Faction Check

Sprite update, minor bug fixes

Floating and Gun and Acid

Minor Records

---
## [littlebabyman/quick-loadout](https://github.com/littlebabyman/quick-loadout)@[d3e2533cad...](https://github.com/littlebabyman/quick-loadout/commit/d3e2533cadb18705515aaf9bb49137f29802f5cc)
#### Saturday 2023-02-25 21:40:32 by littlebabyman

Fuck richtext actually, fuck rubat. fuck garry

Go to hell
Fuck off
Die!!!!!!!!!!
I just wasted several hours on garbage

---
## [VinierAardvark1/Tactical-Intervention---RMC-Branch](https://github.com/VinierAardvark1/Tactical-Intervention---RMC-Branch)@[511e5d6553...](https://github.com/VinierAardvark1/Tactical-Intervention---RMC-Branch/commit/511e5d655396cc0be17c5565feafac6d66de37e2)
#### Saturday 2023-02-25 22:55:19 by VinierAardvark1

Fixed the shitty ass sorting bullshit

why was there a pistol in slot 3

---
## [Sulfurous-Impersonation/old-cpp-projects](https://github.com/Sulfurous-Impersonation/old-cpp-projects)@[87dee666bf...](https://github.com/Sulfurous-Impersonation/old-cpp-projects/commit/87dee666bf5be99fb98908dce4e1a06fef5e639c)
#### Saturday 2023-02-25 23:52:37 by Sulfurous-Impersonation

it's supposed to take input, but that's boring and I wanted to program a dice roller. I ain't gonna let some fuckin' book from the 90's tell me what to do, goddammit! Fuck that book! That book is boring! I don't wanna take input, all I've been doing is taking input! I wanna roll some fuckin' dice! Fuck you!

---

