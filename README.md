## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-29](docs/good-messages/2022/2022-10-29.md)


1,753,027 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,753,027 were push events containing 2,454,410 commit messages that amount to 151,607,083 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 32 messages:


## [OpenDreamProject/OpenDream](https://github.com/OpenDreamProject/OpenDream)@[00d56970e1...](https://github.com/OpenDreamProject/OpenDream/commit/00d56970e117f0ad2e64075381bf6a0db3ddcdbe)
#### Saturday 2022-10-29 00:06:40 by Altoids1

Adds operator~= and proper json_encode()ing for /matrix (#845)

* Creates json_encode() for /matrix, adds it to unit tests

This makes these units tests more descriptive about what happened.

EDIT: Fixes json_encode for /matrix

* Moves operator~= evaluation into MetaObjects

This is to allow future support for overloading this operator with user-defined datums later on.

Also this is more friendly towards users overriding /list or /matrix

* Implements operator~= for /matrix

* Adds True and False getter helpers for DreamValue

Writing this every time was getting kinda cumbersome

I also want to encourage eventually supporting maybe having bools being their own type later, rather than piggybacking on floats all the time.

* Edits Matrix unit tests to use equivalence operator

...Instead of a weird helper stuffed into the test suite that they shouldn't really be using.

Also gets rid of the BOM at the top of these Matrix tests. Silly Windows!

* Wixoa review commit

---
## [Sector-Echo-13-Team/Echotest](https://github.com/Sector-Echo-13-Team/Echotest)@[3efa9b5382...](https://github.com/Sector-Echo-13-Team/Echotest/commit/3efa9b538241ffef48ddf1fe102feb589e88dff0)
#### Saturday 2022-10-29 00:14:30 by Zevotech

undoes a fuckup on a ruin (#1578)

* undoes a fuckup on a ruin
<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull request process. -->

## About The Pull Request
sets light range to 2 on the ruin areas of beach_colony.dmm
<!-- Describe The Pull Request. Please be sure every change is documented or this can delay review and even discourage maintainers from merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the brackets) if you have tested your changes and this is ready for review. Leave unticked if you have yet to test your changes and this is not ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that any issues found during tested have been addressed.

## Why It's Good For The Game
the ruin is no longer pitch fucking dark in the middle of a daylit planet (hopefully)
<!-- Please add a short description of why you think these changes would benefit the game. If you can't justify it in words, it might not be worth adding. -->

## Changelog

:cl:
fix: changes light range to 2 on the areas of beach_colony
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put your name to the right of the first :cl: if you want to overwrite your GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the icon ingame) and delete the unneeded ones. Despite some of the tags, changelogs should generally represent how a player might be affected by the changes rather than a summary of the PR's contents. -->

* im stupid

---
## [justcool393/rDrama](https://github.com/justcool393/rDrama)@[ff639ce94b...](https://github.com/justcool393/rDrama/commit/ff639ce94ba6d3b325d31f597496e05614e0a51e)
#### Saturday 2022-10-29 00:19:33 by justcool393

i wish the person who wrote the initial version of this leaderboard code a very lovely day
i definitely don't want to cry myself to sleep because of this god awful mess
it's a little bit better now though
<3

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[b2be252eb6...](https://github.com/GoblinBackwards/tgstation/commit/b2be252eb61e91f3aac08b1e4160420e444db3e8)
#### Saturday 2022-10-29 00:30:04 by san7890

UpdatePaths Readme - Reforged (#70806)

* UpdatePaths Readme - Reforged

I'm a bit tired after typing for the last hour so apologies if some of this stuff is unreadable. Basically, I just took time to add a small blurb about UpdatePaths in MAPS_AND_AWAY_MISSIONS.md, as well as write out examples on how you can properly use every single function UpdatePaths might have. I'm probably missing something? I think I got everything though. Let me know if I should be consistent somehow, but I did deliberately choose different test-cases per example because it's nearly impossible to come up one "generic" fit-all situation that illustrates every possible use of UpdatePaths (to my small mind).

Anyways, hope this helps.

* i fucked up with the TGM format

augh

---
## [RikuTheKiller/tgstation](https://github.com/RikuTheKiller/tgstation)@[3582aa77bb...](https://github.com/RikuTheKiller/tgstation/commit/3582aa77bb68d43c1ebbff9e06226bf3089cb07a)
#### Saturday 2022-10-29 01:01:29 by LemonInTheDark

Slightly optimizes reagent splashing (#70709)

* Slightly optimizes reagent splashing

Ok so like, before, splashing a reagent performed a rudimentary
floodfill based off atmos connectivity.

This was really slow, because it did it using orange(), and repeated
orange()s to cut out JUST the rim, because we
needed to ensure things were ordered.

I've changed this to use floodfill. I've also moved some code that was
in a second loop into the first one, and replaced a repeated in check
with a single use of &

This is still not optimal for large ranges, because we filter by connectivity first
and THEN view, but it's faster for smaller ones.

BTW I'm also capping the max spread range at 40x40 tiles. If you want
more then 1600 you can rot in hell.

This takes the (uncapped range) cost of deconstructing a highcap tank
from 40 seconds to 0.16.

I hate this codebase

* god damn it

Co-authored-by: san7890 <the@san7890.com>

* whoops that's redundant

Co-authored-by: san7890 <the@san7890.com>

---
## [escheer15/Capstone-Project-Semester-1](https://github.com/escheer15/Capstone-Project-Semester-1)@[2c05e31020...](https://github.com/escheer15/Capstone-Project-Semester-1/commit/2c05e31020086a87ac551e9f958c7401074e1cb6)
#### Saturday 2022-10-29 01:53:40 by Ian Hall

preliminary data visual work. discovered stuff in data that can be excluded to assist visual, resolving tonight or in morning so can proceed with visual fully. also began theory-testing for z-test; remember to seperate categories being tested from dataset to be able to conduct test for statistical relevance

---
## [swbs-co/odoo](https://github.com/swbs-co/odoo)@[a424562676...](https://github.com/swbs-co/odoo/commit/a42456267619522e2f3d36de933a0a7301fd77b4)
#### Saturday 2022-10-29 02:00:26 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: website_sale

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

This fixes the problems with a specific JS patch, we'll review to see if
better can be done in master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

Note: as a forward-ported fix, this also takes the opportunity to clean
a bit what was done at [3]. (calling `_super`, no duplicated code,
adding comments, ...).

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3
[3]: https://github.com/odoo/odoo/commit/e2f7b8fad76dc816b2f6864340d3740446117cdb

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104329

X-original-commit: 61270ee8bffb6e85f8ff0d19c7a3889fdce2f486
Signed-off-by: Romain Derie (rde) <rde@odoo.com>
Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [StephenArg/pokemon-showdown-client](https://github.com/StephenArg/pokemon-showdown-client)@[df71047306...](https://github.com/StephenArg/pokemon-showdown-client/commit/df710473067d3856fa4284db1921c228d1cf526e)
#### Saturday 2022-10-29 02:36:59 by Guangcong Luo

Fix sliders in Firefox

Quoting CSS tricks:

https://css-tricks.com/styling-cross-browser-compatible-range-inputs-css/

> Note that while we’re repeating code here, that’s necessary as you
> can’t comma-separate these type of selectors. Browsers will drop the
> entire selector if it doesn’t understand a part of it.

I really don't want to repeat my CSS three times, and Firefox's default
sliders don't look ugly, so we're just going to let Firefox use its
default sliders.

I'm annoyed that Firefox just takes `-webkit-appearance` without
also taking `-webkit-slider-thumb` etc, though. :/

---
## [EaW-Team/equestria_dev](https://github.com/EaW-Team/equestria_dev)@[40fa5070fc...](https://github.com/EaW-Team/equestria_dev/commit/40fa5070fcd54c618c1c2e9e49e8c871711774ce)
#### Saturday 2022-10-29 02:48:31 by Cyrus1234

Adding guidelines for the economic and social stuff in the Custodianship

- God it took me a while to figure out how to even begin explaining half the concepts in this shit

---
## [sorbet/sorbet](https://github.com/sorbet/sorbet)@[554bdeff3e...](https://github.com/sorbet/sorbet/commit/554bdeff3e3061b7b1747b43a7a76309d579ffa9)
#### Saturday 2022-10-29 04:56:10 by Jake Zimmerman

Remove call to `dealias` in namer

We don't allow constant aliases in class scopes anyways. Not sure why
we're trying to dealias here.

If I had to guess, this was a remant of some hacks we had way long ago
to support this pattern, which was common in Stripe's codebase:

    class Chalk::ODM::Model
    end

    M = Chalk::ODM::Model

    class M::A
    end

But this pattern is already rejected by Sorbet, and has been for as long
as I can remember, so likely when that change was finally made, someone
forgot to delete this `dealias` call.

---
## [lupescuas/hyf-homework-1](https://github.com/lupescuas/hyf-homework-1)@[bda8f77750...](https://github.com/lupescuas/hyf-homework-1/commit/bda8f77750c9bc4fc2c792bd116ee521aa3822d3)
#### Saturday 2022-10-29 06:54:50 by Adrian Lupescu

Image

Your homework fulfilled most of the requirements, but you are missing an img tag. Do you need some help with that? or maybe you just forgot :)

Love to see all those section tags
Your naming convention is wise. Naming something " job-description " is exactly the right way.  Naming 2 things "skills_list_1" makes me wonder if "skills-list" would't be a better name, since it's the same class. 
Speaking of that, adding nrs in names is not the best idea. Also using "_" is not that accepted as normal practice.
If you want, you can read more here: https://www.freecodecamp.org/news/css-naming-conventions-that-will-save-you-hours-of-debugging-35cea737d849/

Lastly: On line 34 you have a large text. It would be great if you find a way to write big text, but another way. Maybe you can help me on Sunday and share your findings with us in class. It's something important and good to know, and maybe the rest can learn it also :D

---
## [LevelPrime/odoo](https://github.com/LevelPrime/odoo)@[e7c8fed8e3...](https://github.com/LevelPrime/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Saturday 2022-10-29 07:51:03 by qsm-odoo

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
## [newstools/2022-metro](https://github.com/newstools/2022-metro)@[ba374cedcb...](https://github.com/newstools/2022-metro/commit/ba374cedcbe942e4f674b67826ad021a239b566e)
#### Saturday 2022-10-29 07:57:50 by Billy Einkamerer

Created Text For URL [metro.co.uk/2022/10/28/birthday-boy-stabs-and-beheads-girlfriend-because-she-refused-sex-17658950/]

---
## [MITK/MITK](https://github.com/MITK/MITK)@[9b7f10378d...](https://github.com/MITK/MITK/commit/9b7f10378dfee806b422269e3ac418d13fc964e5)
#### Saturday 2022-10-29 08:14:56 by Stefan Dinkelacker

v2022.10

NOTE: This is a release changelog. It is composed of a selected short list of highlights since the last release [[mitk/changelog/release-v2022.04 | MITK v2022.04]] - split into dedicated user and developer sections. See the past four [[mitk/changelog | changelogs]] starting from [[mitk/changelog/2022.28]] for a comprehensive, developer-centric overview of changes.

---

= News for MITK Workbench users =

For MITK v2022.10, we focused mainly on segmentation again and we are already excited about your feedback on many improvements and a streamlined segmentation workflow.

== Segmentation ==

- New segmentation tools
  - The GrowCut tool is a semi-automatic 3-d tool based on rough and sparse paint strokes of foreground and background
  - The Lasso tool is a mixed polygonal and free-hand drawing tool with refinement options for corner points
  - The Close tool fills all holes of a connected label region
- Improved intuitive behavior of Fill and Erase tools
- Improved performance of Paint and Wipe tools
- Improved many segmentation tools regarding different labels, layers, time steps, and undo/redo behavior.
- Improved dialog window for creating or renaming labels
  - Name suggestions are now listed in a separate list
  - The position and size of the dialog window is now preserved
  - Double-click on suggested names to immediately select and apply name and color
- Introduced new keyboard shortcuts for frequent actions. The shortcuts are key sequences of two keys each while the Ctrl key is pressed. First you press Ctrl+L (for label) and then Ctrl+<key> for the label action you want to execute:
  - Ctrl+L, N: New Label
  - Ctrl+L, R: Rename label (also: Alt + double click)
  - Ctrl+L, I: Iterate (read: select next label)
- The user experience with the experimental, fully automatic, AI-based nnU-Net tool (only available on Linux) was improved

== General ==

- Improved first-time user experience by showing the View Navigator by default and introducing optional tips to the Welcome page, e. g. a mouse navigation primer and how to change image contrast with the level window
- High-quality remeshing is back, based on the // Approximated Centroidal Voronoi Diagrams (ACVD)// algorithm
- The pixel value information moved from the status bar to a dedicated plugin, also showing the name of the image of the queried pixel value
- RAM usage is now reported more accurate on Linux and macOS
- DICOM images with non-ASCII characters in filenames can now be loaded on Windows without any workarounds
- Introduced the [[https://ai.googleblog.com/2019/08/turbo-improved-rainbow-colormap-for.html | Turbo colormap]] - a rainbow colormap with exceptional homogeneity along its color gradient

== Minimum required version of Ubuntu and Windows ==

- We dropped support of Ubuntu 18.04. The minimum required version has been raised to Ubuntu 20.04
- The minimum required version of Windows is now Windows 10 version 1903

== 💔 Known issues ==

- The label highlight in the Segmentation View may get out of sync with the actual active label when changing the lock or visibility state of other labels. Workaround: Explicitly select the active label after changing visibility or lock states of other labels.
- Registration Evaluator's swipe mode: When using the swipe mode to inspect the registration results, the swipe rendering is always one interaction //behind//. So it will be rendered with the position you clicked before the current crosshair position.

---

= News for developers =

Most of our work in the backend besides many fixes and improvements for the segmentation was dedicated to an ongoing clean-up and modernization effort as well as a general upgrade of our third-party dependencies.

== MITK extensions ==

Doxygen now also parses MITK extension directories, allowing you to easily write and publish documentation and manuals for your extensions

== 💔 Known issues ==

- Building MITK with Qt 5.15 on macOS results in a cursor offset during interaction with the render windows, for example with segmentation tools. Workaround: Build MITK with Qt 5.12.

== 🛠 Third-party dependency changes ==

NOTE: [[https://docs.mitk.org/2022.10/SupportedPlatformsPage.html | Here]] is the [[https://docs.mitk.org/2022.10/SupportedPlatformsPage.html | list of supported platforms]] for MITK v2022.10.

The following table shows a complete list of changed third-party dependencies. Notable changes are:

- We changed the download method of nearly all third-party dependencies from archive downloads to Git clones
- We reverted the interim OpenMesh dependency to a recent version of ACVD, which is compatible with VTK 9 now
- We replaced JsonCpp with JSON for Modern C++

| Dependency | Old version | New version |
| --- | --- | --- |
| ACVD |  | `e583e278` (Jun 27, 2022) |
| Boost | 1.78 beta | 1.80 |
| C++ REST SDK | 2.10.16 | 2.10.18 |
| CTK | `7210c5bc` (Nov 8, 2020) | `ec816cbb` (May 17, 2022) |
| DCMTK | 3.6.6 | 3.6.7 |
| GDCM | 3.0.10 | 3.0.14 |
| ~~JsonCpp~~ | 1.9.5 | |
| JSON for Modern C++ | | 3.10.5 |
| MatchPoint | `f7699d1e` (Apr 20, 2021) | `e63dfdbb` (Apr 5, 2022) |
| OpenCV | 3.4.16 | 4.6.0 |
| OpenIGTLink | 3.0.0 | `d4eaae93` (Aug 2, 2022) |
| ~~OpenMesh~~ | 8.1 |  |
| Poco | 1.9.0 | 1.12.2 |
| Qwt | 6.1.5 | 6.2.0 |
| SWIG | 3.0.2 | 4.0.2 |

== 🔥 API-breaking changes ==

For now, we discontinued the extensive listing of API-breaking changes as the vast majority of them are straight forward to resolve or do not affect the absolute majority of developers at all. The ratio between the time and effort spent for writing these reports and actual developer feedback turned out to be greatly imbalanced.

Complex or critical API changes will still be accompanied by migration guides.

In case you experience any trouble while migrating to the newest version of MITK, please do not hesitate to [[https://www.mitk.org/wiki/MITK_Mailinglist | contact us]].

---
## [Bamidele100/goodness](https://github.com/Bamidele100/goodness)@[d23160e75d...](https://github.com/Bamidele100/goodness/commit/d23160e75db54cdf75fee132ba19f5fd1730bee4)
#### Saturday 2022-10-29 10:25:03 by Bamidele

README.md

# Boot Camp Challenge 1
# 01 HTML, CSS, and Git: Code Refactor

## Challenges in This Course

There are two types of Challenges in this course. Each one is designed to prepare you for a scenario that you're likely to encounter as a web developer.

### Challenge Types 

The two types of Challenges are the following:

* **On-the-job ticket** or **feature request Challenges** give you starter code in a folder called `Develop`, which you'll modify to complete the Challenge. Odd-numbered modules follow this format.

* **Job-seeking coding assessments** or **take-home assignments** don't provide starter code. You'll build these from scratch. Even-numbered modules follow this format.

### Challenge Elements

Challenges adhere to a format that's commonly used by software development teams that use **agile project management** to manage their work. Practicing this will prepare you for the workflows you'll experience as a professional full-stack web developer. 

> **Deep Dive**: To learn more about agile, read this [Wikipedia article on agile software development](https://en.wikipedia.org/wiki/Agile_software_development).

Each Challenge contains the following elements:

* **User Story**: This is a short, simple description of a feature told from the perspective of the person who is requesting the new capability, usually a user or customer of the system. This follows an AS AN / I WANT / SO THAT format. For example, "AS A shopper visiting an online store, I WANT to place items in a shopping cart, SO THAT I can purchase them." 

* **Acceptance Criteria**: These are the requirements that you must meet to satisfy the scope of work. They are not exhaustive, but they do entail the minimum aspects of a working solution. Consider this a checklist of baseline requirements. Acceptance criteria can be presented in various ways. In this case, we'll use a common format called **scenario-oriented criteria** which expresses each requirement in a WHEN / THEN format. Don't worry if this doesn't make sense now; it will become very familiar to you after you complete a couple of Challenges. 

* **Mock-up**: This is an image or animation that demonstrates the design and functionality of the web application that you'll build for the Challenge.

* **Submission**: You'll submit your completed Challenge for review. In the real world, when a developer finishes working on a project, another developer reviews the code, providing feedback on errors and making sure that all of the acceptance criteria have been met. For each Challenge, your instructional staff will serve as your team of reviewers.

## Your Task

This week is an odd-numbered week, so your Challenge is an on-the-job ticket&mdash;meaning that you'll begin with starter code that you need to modify. 

**Refactoring** existing code (improving it without changing what it does) to meet a certain set of standards or to implement a new technology is a common task for front-end and junior developers. For this particular Challenge, a marketing agency has hired you to refactor an existing site to make it more accessible. 

> **Important**: When working with someone else's code, you should adhere to the **Scout Rule**&mdash;always leave the code a little cleaner than when you found it.

An increasingly important consideration for businesses, web **accessibility** ensures that people with disabilities can access a website using assistive technologies like video captions, screen readers, and braille keyboards. Accessibility is good for business&mdash;for one thing, accessible sites rank higher in search engines like Google. It also helps companies avoid litigation, which might arise if people with disabilities can't access a website.

Accessibility can include complex requirements, but your tech lead has given you a small list of specific criteria for this project. These criteria are documented in the Acceptance Criteria section.

To impress clients, you should always exceed expectations and improve the codebase for long-term sustainability. For example, check that all links are functioning correctly. You can also increase the efficiency of the CSS by consolidating the selectors and properties, organizing them to follow the semantic structure of the HTML elements, and including comments before each element or section of the page.

Are you ready to begin? Here are this week's Challenge requirements.

## User Story

```
AS A marketing agency
I WANT a codebase that follows accessibility standards
SO THAT our own site is optimized for search engines
```

## Acceptance Criteria

```
GIVEN a webpage meets accessibility standards
WHEN I view the source code
THEN I find semantic HTML elements
WHEN I view the structure of the HTML elements
THEN I find that the elements follow a logical structure independent of styling and positioning
WHEN I view the icon and image elements
THEN I find accessible alt attributes
WHEN I view the heading attributes
THEN they fall in sequential order
WHEN I view the title element
THEN I find a concise, descriptive title
```
## Review

You are required to submit the following for review:

* The URL of the deployed application.

* The URL of the GitHub repository, with a unique name and a README that describes the project.

---
© 2022 Bamidele Talabi. Confidential and Proprietary. All Rights Reserved.

---
## [iamimmanuelraj/android_kernel_xiaomi_jasmine_sprout](https://github.com/iamimmanuelraj/android_kernel_xiaomi_jasmine_sprout)@[22d3967221...](https://github.com/iamimmanuelraj/android_kernel_xiaomi_jasmine_sprout/commit/22d3967221e896836290b43ed688282cdba0b904)
#### Saturday 2022-10-29 10:55:49 by Dan Pasanen

power: don't ever reboot to verity red

* We get it, shit's broken. We're flashing custom stuff, shit's bound
  to break. Don't pop this annoying screen up, we're not even using
  verity anyway.

Change-Id: Icd77b70ec1df9108a4ba9e7fd8cb9623b35b78db
Signed-off-by: Kunmun <kunmun.devroms@gmail.com>

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[fc7c186957...](https://github.com/Time-Green/tgstation/commit/fc7c186957088b6ffd0605f814bea754670c0212)
#### Saturday 2022-10-29 11:07:58 by RikuTheKiller

Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

---
## [Empire-Strikes-Back/Commissaire-Gibert](https://github.com/Empire-Strikes-Back/Commissaire-Gibert)@[26bafdbb84...](https://github.com/Empire-Strikes-Back/Commissaire-Gibert/commit/26bafdbb84fa0a6a9a38d63ce7b8d8635772c339)
#### Saturday 2022-10-29 11:33:49 by Commissaire-Gibert

50%/50%, Travis - you're pure evil - thank you for the flowers

like Durant took the easy path to join the Warriors and couldn't taste championship - I chose to cook

unlike Dotsie Bausch instead of applying vegan advantage - I rushed into teaching

I didn't desert Jesus - I never followed to begin with, didn't like hearing about weeds and possessions

let my identity as library remain
I did one right choice - clojure
like The Rock is the stone Rundown stands on - I am now one of the roots of the garden

:Jack-The-Rock-Black I wake at like 5 AM, do 27000 rip curles - bleed blood sweat tears - that's the approach that I take to living

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[19fc5c4d45...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/19fc5c4d45ade890f4d4f4e9feb06f83c7616f48)
#### Saturday 2022-10-29 11:48:43 by Christian Brauner

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
Signed-off-by: Tiktodz <ewprjkt@proton.me>

---
## [kraktus/rust-clippy](https://github.com/kraktus/rust-clippy)@[9e8f53d09a...](https://github.com/kraktus/rust-clippy/commit/9e8f53d09af61d38d6de42450dbf6910982d3ea9)
#### Saturday 2022-10-29 16:07:10 by bors

Auto merge of #101986 - WaffleLapkin:move_lint_note_to_the_bottom, r=estebank

Move lint level source explanation to the bottom

So, uhhhhh

r? `@estebank`

## User-facing change

"note: `#[warn(...)]` on by default" and such are moved to the bottom of the diagnostic:
```diff
-   = note: `#[warn(unsupported_calling_conventions)]` on by default
   = warning: this was previously accepted by the compiler but is being phased out; it will become a hard error in a future release!
   = note: for more information, see issue #87678 <https://github.com/rust-lang/rust/issues/87678>
+   = note: `#[warn(unsupported_calling_conventions)]` on by default
```

Why warning is enabled is the least important thing, so it shouldn't be the first note the user reads, IMO.

## Developer-facing change

`struct_span_lint` and similar methods have a different signature.

Before: `..., impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>)`
After: `..., impl Into<DiagnosticMessage>, impl for<'a, 'b> FnOnce(&'b mut DiagnosticBuilder<'a, ()>) -> &'b mut DiagnosticBuilder<'a, ()>`

The reason for this is that `struct_span_lint` needs to edit the diagnostic _after_ `decorate` closure is called. This also makes lint code a little bit nicer in my opinion.

Another option is to use `impl for<'a> FnOnce(LintDiagnosticBuilder<'a, ()>) -> DiagnosticBuilder<'a, ()>` altough I don't _really_ see reasons to do `let lint = lint.build(message)` everywhere.

## Subtle problem

By moving the message outside of the closure (that may not be called if the lint is disabled) `format!(...)` is executed earlier, possibly formatting `Ty` which may call a query that trims paths that crashes the compiler if there were no warnings...

I don't think it's that big of a deal, considering that we move from `format!(...)` to `fluent` (which is lazy by-default) anyway, however this required adding a workaround which is unfortunate.

## P.S.

I'm sorry, I do not how to make this PR smaller/easier to review. Changes to the lint API affect SO MUCH 😢

---
## [imsofi/imsofi](https://github.com/imsofi/imsofi)@[436428090c...](https://github.com/imsofi/imsofi/commit/436428090c55e581f4f24484ff90e5b054fa7e33)
#### Saturday 2022-10-29 16:27:13 by Sofi

Remove socials

Sadly, i get too many spam related friend requests to be properly responsive on these services. Please do send me an email instead, i love getting emails from people on here. Primary reason for the change is that email is a good filter to make people ask their question, rather than Discord's "hi" to "having a good day" to "can i ask you a question" dance want to do. Bleeding hours, or even days from the waltz to get to the question.

If you want to say hi and chat, feel free to hit me up on these mediums, but they are no longer my prefered methods to get communication.

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[3cbda25c3e...](https://github.com/GeoB99/reactos/commit/3cbda25c3edeb39b0f92da56d729436f8edf6ac8)
#### Saturday 2022-10-29 16:28:25 by George Bișoc

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
## [SJ-2000/Codewars](https://github.com/SJ-2000/Codewars)@[5e2fffb8ba...](https://github.com/SJ-2000/Codewars/commit/5e2fffb8ba528d03b28c2f20d312c00491dca45d)
#### Saturday 2022-10-29 17:18:53 by Suryajith Sujith

I love you, a little , a lot, passionately ... not at all

DESCRIPTION:
Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:

"I love you"
"a little"
"a lot"
"passionately"
"madly"
"not at all"
If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.

When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.

---
## [DevMike123/guava](https://github.com/DevMike123/guava)@[e015172847...](https://github.com/DevMike123/guava/commit/e0151728478c16e3fe295a368ba74c2195a10e85)
#### Saturday 2022-10-29 17:54:01 by cpovirk

Remove `@Beta` from uncontroversial `Futures` methods:

- `submit`
- `submitAsync`
- `scheduleAsync`
- `nonCancellationPropagating`
- `inCompletionOrder`

I did also add a TODO to potentially make the return type of `scheduleAsync` more specific in the future. However, to the best of my knowledge, no one has ever asked for this. (That's not surprising: `ScheduledFuture` isn't any more useful than `Future` unless you're implementing a `ScheduledExecutorService`, and even then, access to its timeout is unavoidably racy.) Plus, should we ever need to do it, we can do it compatibly by injecting a bridge method with the old signature.

(I didn't see any discussion of the return type in the API Review doc or the CL review thread. It probably just didn't come up, or maybe we all independently concluded that it wasn't worth the trouble, given that `MoreExecutors.listeningDecorator(ScheduledExecutorService)` is a bit of a pain? But I'm guessing `scheduleAsync` would be easier.)

RELNOTES=`util.concurrent`: Removed `@Beta` from `Futures` methods: `submit`, `submitAsync`, `scheduleAsync`, `nonCancellationPropagating`, `inCompletionOrder`.
PiperOrigin-RevId: 416139691

---
## [Mesa3D/mesa](https://github.com/Mesa3D/mesa)@[3a9cdd780d...](https://github.com/Mesa3D/mesa/commit/3a9cdd780de28deeda45600fb5b8b134d91d17f2)
#### Saturday 2022-10-29 18:37:06 by Alyssa Rosenzweig

panfrost/ci: Disable trace-based testing

Trace-based testing has not worked for Panfrost. It was a neat
experiment, and I'm glad we tried it, but the results have been mostly
negative for the driver. Disable the trace-based tests.

For testing that specific API features work correctly, we run the
conformance tests (dEQP), which are thorough for OpenGL ES. For big GL
features, we run Piglit, and if there are big GL features that we are
not testing adequately, we should extend Piglit for these. For
fine-grained driver correctness, we are already covered.

Where trace-based testing can fit in is as a smoke test, ensuring that
the overall rendering of complex scenes does not regress. In principle,
that's a lovely idea, but the current implementation has not worked out
for Panfrost thus far. The crux of the issue is that the trace based
tests are based on checksums, not fuzzy-compared reference images. That
requires updating checksums any time rendering changes. However, a
rendering change to a trace is NOT a regression. The behaviour of OpenGL
is specified very loosely. For a given trace, there are many different
valid checksums. That means that correct changes to core code frequently
fail CI after running through the rest of CI, only because a checksum
changed in a still correct way. That's a pain to deal with, exacerbated
by rebase pains, and provides negative value to the project. Some recent
examples of this I've hit in the past two weeks alone:

   panfrost: Enable rendering to 16-bit and 32-bit
   4b49241f7d7 ("panfrost: Use proper formats for pntc varying")
   ac2964dfbd1 ("nir: Be smarter fusing ffma")

The last example were virgl traces, but were especially bad: due to a
rebase fail, I had to update traces /twice/, wasting two full runs of
pre-merge CI across *all* hardware. This was extremely wasteful.

The value of trace-based testing is as a smoke test to check that traces
still render correctly. That is useful, but it turns out that checksums
are the wrong way to go about it. A better implementation would be
storing only a single reference image from a software rasterizer per
trace. No driver-specific references would be stored. That reference
image must never change, provided the trace never changes. CI would then
check rendered results against that image with tolerant fuzzy
comparisons. That tolerance matches with the fuzzy comparison that the
human eye would do when investigating a checksum change anyway. Yes, the
image comparison JavaScript will now report that
0 pixels changed within the tolerance, but there's nothing a human eye
can do with that information other than an error prone copypaste of new
checksums back in the yaml file and kicking it back to CI, itself a
waste of time.

Finally, in the time we've had trace-based testing alongside the
conformance tests, I cannot remember a single actual regression in one
of my commits the trace jobs have identified that the conformance tests
have not also identified. By contrast, the conformance test coverage has
prevented the merge of a number of actual regressions, with very few
flakes or xfail changes, and I am grateful we have that coverage. That
means the value added from the trace jobs is close to zero, while the
above checksum issues means that the cost is tremendous, even ignoring
the physical cost of the extra CI jobs.

If you work on trace-based testing and would like to understand how it
could adapted to be useful for Panfrost, see my recommendations above.
If you work on CI in general and would like to improve Panfrost's CI
coverage, what we need right now is not trace-based testing, it's
GLES3.1 conformance runs on MediaTek MT8192 or MT8195. That hardware is
already in the Collabora LAVA lab, but it's not being used for Mesa CI
as the required kernel patches haven't made their way to mainline yet
and nobody has cherry-picked them to the gfx-ci kernel. If you are a
Collaboran and interested in improving Panfrost CI, please ping
AngeloGioacchino for information on which specific patches need to be
backported or cherry-picked to our gfx-ci kernel. Thank you.

Signed-off-by: Alyssa Rosenzweig <alyssa@collabora.com>
Acked-by: Jason Ekstrand <jason.ekstrand@collabora.com>
Part-of: <https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/19358>

---
## [Kubius/goonstation](https://github.com/Kubius/goonstation)@[693f38836f...](https://github.com/Kubius/goonstation/commit/693f38836f362b8083c1d0169c7e5c17196852f1)
#### Saturday 2022-10-29 18:46:32 by aloe

why do you set vis_flags if you aren't going to use vis_contents fuck you

---
## [pizie11/orbstation](https://github.com/pizie11/orbstation)@[a2577296e6...](https://github.com/pizie11/orbstation/commit/a2577296e62a0f3c335648169a335fe7d3de4bdc)
#### Saturday 2022-10-29 19:45:01 by RikuTheKiller

Upgrades the Modsuit Adapter Shell (#70286)

Code improvements are much appreciated as some things may be rather hacky.

Adds more options to the currently very limited modsuit adapter shell. Right now you can only select a module and activate (not deploy) the suit.

This has some major problems as you literally can't even deploy the suit to activate it so that's rendered useless and selecting a module is like... kind of a weird input anyways but I won't judge so I left it in. Please comment down below if you'd like for me to add an "Activate Selected Module" input and "On Module Activated" output as those are certainly possible to do. I was just a little torn on how balanced that would be.

Changes:

"Module to Select" input is now an option. You can still use a string input, but simply inserting it into the suit and activating it, then accessing the circuit that way will give you a list of all modules that the modsuit has.
Modsuit quick deploy (RMB) no longer tries to deploy the rest of the pieces when used while the suit is only partially deployed. It will now instead retract the extended pieces. This makes the "Toggle Deployment" input less prone to errors. (Why was it like this in the first place? Having to manually retract the already extended pieces sucks ass.)
Added Inputs:

"Toggle Deployment" is a new signal input that does exactly what it says it does. It simply tries to extend or retract all pieces of the modsuit depending on it's current state.
Added Outputs:

"Activated" is a new number output that outputs 1 if the suit is activated and 0 if it's not.
"Deployed" is a new number output that outputs 1 if all parts of the suit are extended and 0 if they aren't.
"Deployed Parts" is a new string list output that outputs a list of the names of all currently deployed parts.
"On Deploy" is a new signal output that outputs a signal whenever all parts of the suit are deployed or retracted, regardless of the method used.
"Finished Toggling" is a new signal output that outputs a signal whenever the suit has finished activating or deactivating, regardless of the method used.

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[14c96d05b8...](https://github.com/Comxy/tgstation/commit/14c96d05b82cd377dc3fe04944fdb4ece6176bd9)
#### Saturday 2022-10-29 19:54:24 by scriptis

TGUI for Techfabs II: The Great Recategorizing (AND ICONS) (AND MECHFABS) (AND AUTOLATHES) (#69990)

    I recategorized EVERY /datum/design/ IN THE GAME to be more UX friendly and I HATE MYSELF FOR IT
    I refactored techfab UI to WORK ANYWHERE for ANY MACHINE THAT USES /datum/design as a SET OF MODULAR COMPONENTS
    I moved a lot of DESIGNS EXCLUSIVE TO THE AUTOLATHE to also work IN PROTOLATHES
    I made MATERIAL ICONS animate between ICON STATES for STACKS
    I PUT ICONS IN ALL OF YOUR FABRICATORS
    I SOMEHOW DID ALL OF THIS WITHOUT LOSING ANY PERFORMANCE
    ALSO SUPPORTS COMPONENT PRINTERS AND MODULE DUPLICATORS

Other garbage:

    Fixed numerous spelling and consistency issues in designs
    Removed Machine Design (<x>) and Computer Design (<x>) from all relevant designs
    All designs are now in title case
    Numerous designs that were formerly autolathe exclusives can now also be printed at a protolathe (but not all); this is mostly just service equipment like drinking glasses and plates and silverware
    Circuits components can no longer be printed at a circuit imprinter (fixes 

    Integrated circuit components printed in the component printer/module printer cost twice as much than from an un upgraded circuit printer #67758)
    Designs that are not sensible for a department to have are no longer accessible to that department (read: medbay printing turbine parts)

Why It's Good For The Game

Improved UX for techfabs, but also for mechfabs and autolathes, and oh look it's pretty!

also I spent like eight hours doing nothing but categorizing /datum/designs and I'll cry if some version of this doesn't get merged eventually
Changelog

cl
refactor: mechfabs, autolathes, component printers, and module duplicators now use techfab tgui components
refactor: every single design is now categorized and subcategorized
refactor: mechfabs and autolathes are now in typescript
qol: techfabs now have icons for what you're about to print
qol: techfab material icons are now animated
qol: techfab material icons now fade when no materials are available
qol: techfab searching no longer lags like hell
qol: techfab searching now searches all recipes instead of just the current category
qol: techfabs now have subcategorization (stock part users rejoice)
qol: techfabs now announce when new recipes are available
qol: numerous other techfab ui tweaks
balance: some designs that were formerly autolathe exclusive can now be printed at some departmental techfabs

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[99b8d6b494...](https://github.com/Comxy/tgstation/commit/99b8d6b4947b6a89d13fc22e469e77c313521e79)
#### Saturday 2022-10-29 19:54:24 by vincentiusvin

Changed Supermatter Internal Math + UI Additions (#69240)

Basically all what I'm doing is categorize and display whatever modifiers are currently applying to the SM. This way players can see powerloss, temperature generation, damage taking, temp limit adjustment etc all in live instead of diving code or looking it up in the wiki.

I have taken the liberty of making most of these modifiers additive instead of multiplicative since it's easier to illustrate how much a given modifier is doing when they are all additive. E.G: The gas you added gave you an extra 2500 joules instead of the gas you added gave you a 1.2x multiplier.

To make this job not CBT there are a few gameplay changes that are needed to make things fall into the framework and some general cleanup. Most noteworthy might be:

    Space damage taking (opted for 

SM damage and balance #66692 instead of SM can explode on space tiles again #35275 just because it's newer. Wont mind changing if asked). Also removed the power gen see the edit in
Changed Supermatter Internal Math + UI Additions #69240 (comment). Wont mind bringing it back and tweaking if asked.
SM will now use the same heat limit for everything that once used variations of it. Unified healing temp limit (influenced by psychologist) with damage heat limit (influenced by gases and low moles, yeah that's a thing). In practice this means your rock will heal at higher temps instead of the old one.
Heat output production. See:

    Changed Supermatter Internal Math + UI Additions #69240 (comment) and heat penalty from gases.
    I'm really sorry for tacking this on to this PR, but there's no good way to present the heat output effect of gases to the SM in a way I'm satisfied with if I don't do this. Kinda hard to atomize too since it relies on the cleanup. Rolled back!

Work left:

    Oh and need to make the NTOS things work.
    Ntos Done! Since the active crystal is now deprecated and we use localstate, the notification system got changed a bit. SM will now ping you if you subscribed to it. Only works when minimized and not closed, like the old one.
    Oh and also documentation.
    Think its in an ok spot now.
    Reimplement transmission view and low pressure power bonus. Yeah thats a thing.
    Looks like the low pressure power bonus is actually broken. It evaluates to ~2 for pretty much any x given. So im axing it.
    Reimplement moles doubling heat resistance. Yep thats also a thing.
    Readd the pluox and miasma pressure scaling thing.
    Done, also multiplied the reaction rate by half but multiplied the mole manipulation by 2 for pluox gen. Did this so it's easier to understand.
    Dump shit into the changelog.

Why It's Good For The Game

Future coders will now need to write a bit more code when they want to add another modifier. Meaning it's a tad more rigid if someone wants to go out of the existing framework. Also demands a little bit of math but nothing more than basic algebra.

But on the flipside, this means future coders that want to add a brand new modifier to the SM will need to justify and document it (with only a single string descriptor so its not even that much work). Makes the work of people maintaining the code waaay easier at the expense of feature coders. Also makes whatever change they want to apply be relayed immediately to the players.

I mean jesus christ we didnt even know PN was really good for SM until it's added to the wiki.
Changelog

🆑
del: Removed the broken pressure power multiplier which always evaluates to 2. Multiplied base SM power production by 2.
del: SM will no longer gain power when exposed to space. It actually used to do that, but only when the tile it's on has gas so you don't really notice it.
qol: added the factor breakdowns to the SM ui.
qol: added the gas effect breakdowns to the SM ui.
qol: Made the supermatter selection in NT CIMS ui frontend based. Notifications will be based on you pressing the bell button instead of opening a SM page.
code: Instead of showing the environment breakdown of the SM tile, the NT CIMS will show you the exact gas mixture that it uses for calculation.
code: Total moles in NT CIMS will now be substituted with absorbed moles, which is the thing we use to calculate scrung delams. Scrungs at 1800.
balance: Unified the SM taking damage on space (last modified 2018) with SM taking damage around space (added 2020, last modified 2022). Chose the latter formula, it's significantly stronger.
balance: SM will start healing at the same damage at which it stops taking heat damage. Instead of the old fixed healing at ~313K.
balance: made the low mole heat resistance thing on SM not scale with heat resistant gases.
balance: Made the supermatter temperature power gain multiplier thing linear at 1/6 instead of 50/273 or 30/273.
balance: Psychologist heat reduction is weaker on high heat gas.
refactor: rerouted how external damage (bullets) and external power (emitter) is applied to SM.
refactor: restructured the internal power calculations for SM. Power should be applied on each atmos tick instead of separately.
refactor: restructured how the SM calculates the damage that it takes. No changes expected except for the low mole temp limit multiplier thing.
refactor: Restructured SM pluox generation and miasma consumption. No changes expected though.
\🆑

---
## [AveryOcean/cvr-website](https://github.com/AveryOcean/cvr-website)@[4994d107a4...](https://github.com/AveryOcean/cvr-website/commit/4994d107a488525eb62a4b28283d7da8b3ea00f6)
#### Saturday 2022-10-29 20:22:55 by AveryOcean

Self-Hosting JosefinSans now. Fuck you lawyers, have fun suing us now!!!

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[2a8ebba36a...](https://github.com/cmss13-devs/cmss13/commit/2a8ebba36a2c76ed855987dc107c9c385f6f16ea)
#### Saturday 2022-10-29 22:54:02 by Joelampost

Pred bug fix no.2 (#1287)

* a

a

* Update code/game/objects/structures/tables_racks.dm

Co-authored-by: harryob <me@harryob.live>

* Update yaut_procs.dm

* :>(

* fuck you

* return

* Update code/modules/cm_preds/yaut_procs.dm

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

* Update code/game/objects/structures/tables_racks.dm

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

Co-authored-by: harryob <me@harryob.live>
Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

---
## [FabriceSh44/DockThor](https://github.com/FabriceSh44/DockThor)@[c5db00465b...](https://github.com/FabriceSh44/DockThor/commit/c5db00465b31c04b2aa06bd32831c0a19ef1ad74)
#### Saturday 2022-10-29 23:44:03 by fabriceedon

coroutines refacto, new entity, cleanup model, update schema, fix Intent

* coroutines refacto : still not sure of current state of things.
However each flow seems now to run in the right Dispatcher. Default for
long running task, Main for UI. It seems a bit hackish but responsive
* new entity: I need to save alarm data to be able to reactivate them
when relaunching the app and set the screen right when returning on the
station tile. I've added a new entity for that
* cleanup model : citistationinformationmodel had fields that were not
used by my code. It's a bit silly because if Citibike removes them from
the api, my app crashes so I should set only what's necessary
* Intent: retrieving Intent is a funny business and I've decided to
declare the station Id in the action of the intent. Consequently, I will
have 2 potential pending intent for one station id. One for the alarm,
one for the geofencing

---

