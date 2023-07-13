## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-12](docs/good-messages/2023/2023-07-12.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,126,618 were push events containing 3,452,601 commit messages that amount to 294,996,610 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 57 messages:


## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[d045a5d654...](https://github.com/Drulikar/cmss13/commit/d045a5d6547dcda9fc04be9b6cd50d2ff44e672f)
#### Wednesday 2023-07-12 00:52:39 by Drathek

Larva Queue Late Joiner Nerf (#3803)

# About the pull request

This PR makes it so players who haven't played yet have their join time
recorded, and that is used for their initial sorting value rather than
0. This means late joiners will be at the back of the line as if they
had just died.

This PR also fixes an oversight where ghosting as a facehugger would
count as death. Even though they really shouldn't be ghosting when
alive, they still shouldn't be penalized as far as the queue is
concerned.

# Explain why it's good for the game

Its not; its a bad experience for everyone that hasn't even gotten one
life in the round. However it seems I'm in the minority thinking that a
xeno shouldn't squander their first life and that death shouldn't bear
more consequences.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

The new informational message if you press join as xeno while currently
ineligible to be a xeno candidate:

![image](https://github.com/cmss13-devs/cmss13/assets/76988376/9fb295c2-e654-4843-9e3e-bf37f2c8755e)

</details>


# Changelog
:cl: Drathek
del: Remove first life priority for larva queue
fix: Fix ghosting as a facehugger counting as death for the larva queue
/:cl:

---
## [cranatic101/cac_23](https://github.com/cranatic101/cac_23)@[3a4eaf2fac...](https://github.com/cranatic101/cac_23/commit/3a4eaf2fac4dcbde911455225688f7ade109a949)
#### Wednesday 2023-07-12 00:58:44 by SahilSN

Enhancing Website Design: The Art of Adding Code to a style.css File

Introduction:
In the dynamic world of web development, cascading style sheets (CSS) play a vital role in controlling the presentation and visual appeal of a website. The style.css file acts as the heart of a website's design, dictating its layout, typography, colors, and other stylistic aspects. By adding code to the style.css file, developers can significantly enhance the appearance and user experience of a website. This essay aims to explore the various techniques and best practices involved in adding code to a style.css file to achieve stunning web design results.

I. Understanding the Structure of a style.css File:
Before delving into adding code, it is essential to understand the structure of a style.css file. A typical style.css file consists of a series of CSS rulesets, which define the styles applied to specific HTML elements. Each ruleset contains a selector and a set of declarations, where the selector targets specific HTML elements, and the declarations specify the desired styles.

II. Customizing Typography:
One of the primary areas where code can be added to the style.css file is for customizing typography. By defining font families, sizes, weights, and line heights, developers can establish a unique typographic style that aligns with the website's overall theme and branding. Additionally, techniques such as text shadows, letter spacing, and text transformations can be employed to further enhance the visual appeal and readability of the text.

III. Styling Layout and Components:
Code can be added to the style.css file to modify the layout and appearance of various components on a website. This includes altering the size and positioning of elements, such as headers, footers, navigation menus, and sidebars. By using CSS properties like width, height, margins, padding, and positioning, developers can achieve precise control over the placement and spacing of elements, resulting in a harmonious and balanced layout.

IV. Enhancing Colors and Visual Effects:
Colors and visual effects play a crucial role in capturing users' attention and creating a memorable website experience. By adding code to the style.css file, developers can define custom color schemes, background images, gradients, and transitions. Additionally, techniques such as box shadows, border styles, and opacity can be utilized to add depth and dimension to various elements, making them visually appealing and engaging.

V. Achieving Responsiveness:
In today's mobile-first era, ensuring that websites adapt seamlessly to different screen sizes and devices is imperative. By adding code to the style.css file, developers can implement responsive design principles. This involves utilizing CSS media queries to target specific screen sizes and adjust the layout and styling accordingly. By making the website responsive, users can enjoy a consistent and optimized experience across desktops, tablets, and smartphones.

VI. Implementing Animations and Interactivity:
Adding code to the style.css file allows developers to bring websites to life through animations and interactivity. CSS3 provides powerful animation capabilities, enabling the creation of smooth transitions, fades, rotations, and more. By combining CSS animations with JavaScript events, developers can introduce interactive elements such as dropdown menus, sliders, and tooltips, enhancing user engagement and interaction.

VII. Best Practices and Optimization:
While adding code to the style.css file offers immense creative possibilities, it is crucial to adhere to best practices and optimize the code for performance. Minifying and compressing the CSS file can reduce its size and improve loading times. Additionally, using proper indentation, comments, and organizing the code in a modular and scalable manner promotes maintainability and ease of future updates.

Conclusion:
Adding code to the style.css file is a fundamental aspect of web development, allowing developers to craft visually stunning websites that captivate users. Through customization of typography, layout, colors, effects, responsiveness, animations, and interactivity, the style.css file serves as a canvas for creative expression. By adhering to best practices and optimizing the code, developers can ensure that their designs not only look remarkable but also perform efficiently. As the web continues to evolve, the art of adding code to a style.css file remains an essential skill for creating compelling and engaging digital experiences.

---
## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[e80cf8f358...](https://github.com/BlueMemesauce/tgstation/commit/e80cf8f3586e5aeb599e8f54bd35ebafb878e101)
#### Wednesday 2023-07-12 01:26:01 by Jacquerel

Improved spider web AI (#76637)

## About The Pull Request

The AI I coded for spiders deciding where to make webs when they aren't
otherwise occupied would do so by finding the _closest_ valid tile,
which seemed like a good idea at the time. The problem with that is that
the "closest" algorithm we use has a predictable search pattern which
meant that spiders would always predictably make a diagonal line of webs
pointing South West, which looked very silly.
I've rewritten how they pick targets to introduce some randomness, which
causes them to properly spread out and make a nicer-looking structure:
which serves purely to annoy spacemen who need to pass through this
area.


![image](https://github.com/tgstation/tgstation/assets/7483112/cb01828f-7653-4010-a4f5-2abc6e10b630)

I'll be honest I mostly did this while bored waiting for other PRs which
I require for my other branch to get merged.

## Why It's Good For The Game

This probably only annoyed me to be quite honest and if you left one
alone for long enough it would fill enough space that you couldn't tell
anyway, but it does look nicer now.

## Changelog

:cl:
add: AI-controlled spiders will make more web-shaped webs.
/:cl:

---
## [TheRealScarHomie/mojave-sun-13](https://github.com/TheRealScarHomie/mojave-sun-13)@[c65f22da38...](https://github.com/TheRealScarHomie/mojave-sun-13/commit/c65f22da381954082c8818862c06397a274ec797)
#### Wednesday 2023-07-12 01:40:22 by Hekzder

Post Test Tweaks for early July (#2410)

* makes alcohol tolerance not stupid

yea

* bit of a PA nerfy

Just on lower end PA so like the frame and T-45

* Forage respawn time increase + herbal remedy tweak

yea

* ciggy tweaks and spawn fixes

yea

* actually tested it and made proper changes lol!

woo!!

* god I hate TG

this is insane

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[18819cc7fb...](https://github.com/Bjarl/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Wednesday 2023-07-12 01:52:36 by zevo

Minor changes to the Syndicate Battle Sphere ruin (#2045)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Various fixes for provinggrounds.dmm, mainly the server room and SMES.
Server room is no longer filled with black box recorders, but salvagable
servers. There is now one singular black box recorder in the center
where a black box on a table was. The SMES now should actually charge
the ruin. Tossed a medkit in one of the halls for players to use while
clearing the ruin. Replaced about half of the syndicate researcher mobs
with syndicate operatives who will actually fight the players. Rotated
an airlock missed in the map updates for anywalls.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
boy, i sure love functional ruins! also players should not have 25 of a
very rare potential quest item. The ruin can stay as it is otherwise,
because it provides a fun challenge for superbly well armed players (or
a rugged explorer with nothing but a lazer gun and a dream) with a
fitting reward at the end of a mounted LMG.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Syndicate Battle Dome (provinggrounds.dmm) should now have a
functional SMES and airlocks/blast doors.
fix: Syndicate Battle Dome (provinggrounds.dmm) no longer has ~20 black
box recorders and now only has one.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Bjarl/Shiptest](https://github.com/Bjarl/Shiptest)@[0e6f7fa646...](https://github.com/Bjarl/Shiptest/commit/0e6f7fa64649dfbf52b8e4b71756e6625e50fdd0)
#### Wednesday 2023-07-12 01:52:36 by Imaginos16

TileTest Part 1: Big Sweeping Changes! (#2054)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->
## !! WARNING !!
This is a multi-parter PR. Due to the fact that tiles here on shiptest
are an unholy amalgam of decals, greyscale sprites and multiple
spread-out files, things are *bound* to look weird. If they do, feel
free to report it and it will be addressed in future PRs.

## About The Pull Request

This PR finally accomplishes the promise I made to @triplezeta a year
ago, creating a unique tileset for the server that people may enjoy!

To put every single microscopic change I have made would take forever,
so I will instead provide a series of screenshots of it in action!


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/00e9cec0-335a-4367-90f9-1adc572595f3)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/497310ab-fe06-4b31-8774-70e79338a7d8)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/80991d0b-c48b-404b-b4a6-cbb1c4c6af3a)


![image](https://github.com/shiptest-ss13/Shiptest/assets/77556824/cc06d43e-3873-499e-aa12-51a0d7a37c98)

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Utilizing an unique, modernized tileset for our server to differentiate
from our competitors is something that has been requested, and I was
more than happy to lend my hand to make it a reality!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: PositiveEntropy
del: Removes several unused floor types, as well as completely
annihilating the "monofloor" and "dirty" floor types, and the "edge"
decal type.
imageadd: Redoes the floors using the TileTest tileset!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Bjarl <94164348+Bjarl@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[f8ee9961d5...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/f8ee9961d50e66d20fe9ed8e4b47928f6cdf0852)
#### Wednesday 2023-07-12 02:11:57 by SkyratBot

[MIRROR] Fixes some inconsistencies with the chaplain revolver and gets rid of a weird ammo define [MDB IGNORE] (#22108)

* Fixes some inconsistencies with the chaplain revolver and gets rid of a weird ammo define (#76237)

## About The Pull Request

Firstly, I gave the revolver a new sprite. I mean, this isn't so much of
an improvement as it is a reference I wanted to go with, so if people go
'no not a new sprite' I don't mind reverting.

What's the reference? Check the new name I added as a potential name
roll.

![lucky
38](https://github.com/tgstation/tgstation/assets/40847847/e11874be-1416-4e21-bda9-4881d49cad1b)

Secondly; I applied to the gun itself revenant bane, the ability to
clear runes, and proper magic immunity as a full null rod would enable.
This last bit was a deliberate design choice, but the divine bow has
full magic protection, so I think this is now more of a consistency
consideration compared to the divine bow.

Thirdly, the revolver is a .38 revolver, HOWEVER, it uses a damage
multiplier to bring it back to the damage it did originally. It also
cannot be reloaded without the prayer action. No cheating. Effectively,
this is the same mechanically as it was before.

It rarely does a funny crit fanfare. This does nothing mechanically, I
just thought it was a funny nod to the sprite's reference (and I guess
another game that the crit fanfare is based on). Borrowed parts of the
code and sprite from this April Fool's pr by Wallemations >
https://github.com/tgstation/tgstation/pull/74425

## Why It's Good For The Game

I think this might have been a little forgotten since implementation now
that we have another projectile weapon for the chaplain. So I'm brushing
it up a bit.

## Changelog
:cl:
fix: Makes the chaplain's revolver consistent with its immediate
sibling, the Divine Bow, by giving it similar statistics.
code: Makes the chaplain revolver a .38 but prevents it from being
loaded without using the special prayer action. Also applies a damage
multiplier to keep it at the original 18 force. Mechanically, no
different.
sprite: Gives the chaplain revolver a new sprite.
code: Removes an unnecessary admin log when removing runes.
/:cl:

* Fixes some inconsistencies with the chaplain revolver and gets rid of a weird ammo define

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: Pinta <68373373+softcerv@users.noreply.github.com>

---
## [chaotic-cx/mesa-mirror](https://github.com/chaotic-cx/mesa-mirror)@[7229bffcb1...](https://github.com/chaotic-cx/mesa-mirror/commit/7229bffcb133b68f91607fb6bccbe0e48b6a55bd)
#### Wednesday 2023-07-12 02:20:29 by Alyssa Rosenzweig

nir: Add intrinsics for register access

Note the writemask handling is chosen for consistency with the rest of NIR. In
every other instance, writemask=w requires a vec4 source. This is hardcoded into
nir_validate and nir_print as what it means to have a writemask.

More importantly, consistency with how register writemasks currently work.
nir_print hides it, but r0.w = fneg ssa_1.x is actually a vec4 instruction with
source ssa_1.xxxx. As a silly example nir_dest_num_components(that) = 4 in the
old model. I realize this is quite strange coming from a scalar ISA, but it's
perfectly natural for the class of vec4 hardware for which this was designed. In
that hardware, conceptually all instructions are vec4`, so the sequence "fneg
ssa_1 and write to channel w" is implemented as "fneg a vec4 with ssa_1.x in the
last component and write that vec4 out but mask to write only the w channel".

Isn't this inefficient? It can be. To save power, Midgard has scalar ALUs in
addition to vec4 ALUs. Those details are confined to the backend VLIW scheduler;
the instruction selection is still done as vec4. This mechanism has little in
common with AMD's SALUs. Midgard has a wave size of 1, with special hacks for
derivatives.

As a result, all backends consuming register writemasks are expecting this
pattern of code. Changing the store to take a vec1 instead of a vec4 would
require changing every backend to reswizzle the sources to resurrect the vec4. I
started typing a branch to do this yesterday, but it made a mess of both Midgard
and nir-to-tgsi. Without any good reason to think it'd actually help
performance, I abandoned the idea. Getting all 15 backends converted to the
helpers is enough of a challenge without forcing 10 backends to reswizzle their
sources too.

Signed-off-by: Alyssa Rosenzweig <alyssa@rosenzweig.io>
Reviewed-by: Faith Ekstrand <faith.ekstrand@collabora.com>
Part-of: <https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/23089>

---
## [Chubbygummibear/Yogstation-TG](https://github.com/Chubbygummibear/Yogstation-TG)@[d1c7dfdc1a...](https://github.com/Chubbygummibear/Yogstation-TG/commit/d1c7dfdc1ae55bfd9fa7f603f415b762ba6a472a)
#### Wednesday 2023-07-12 02:22:54 by SapphicOverload

IPC tweaks (#19467)

* funny tv head robot go brrrrr

* Update IPC.dm

* not that fast

* fuck it we ball

---
## [Dirstac/mame](https://github.com/Dirstac/mame)@[4a5b8a415f...](https://github.com/Dirstac/mame/commit/4a5b8a415fee66df01d57b871a8025d0f1f1a2f6)
#### Wednesday 2023-07-12 03:00:50 by wilbertpol

msx1_cart.xml: Added fourteen working items. (#11412)

* Removed Hopper (Europe) tape-to-cartridge hack.
* Demoted The Holy Quran (v1.00) to not working.

New working software list items (msx1_cart.xml)
-------------------------------
Hole in One Professional (Japan, alt 2) [file-hunter]
Hole in One Professional (Japan, alt 3) [file-hunter]
Hot-Asm (Brazil) [file-hunter]
Hot-Plan (Brazil) [file-hunter]
Hydlide II - Shine of Darkness (Korea) [file-hunter]
Hopper (Arab) [file-hunter]
Hans' Adventure (v1.1) [MSXDev]
Hans' Adventure (v1.0) [MSXDev]
Happy Halloween [Clube MSX]
Happy Square Christmas [303bcn]
Heart Stealer 2 [MSXDev]
Heroes Arena [MSXDev]
Hose Diogo Martinez: The Bussas Quest [MSXDev]
How Many Are The Dumbbells You Lift? [cobinee]

---
## [jinuthomas/openpower-vpd-parser](https://github.com/jinuthomas/openpower-vpd-parser)@[96d1867e08...](https://github.com/jinuthomas/openpower-vpd-parser/commit/96d1867e0804bc22b70ee635039f9104aebfe75b)
#### Wednesday 2023-07-12 03:37:57 by jinuthomas

Catching File Exceptions in openpower-vpd-parser

In this commit, I have added code to handle file exceptions
more effectively. By implementing proper exception handling,
we can improve the robustness and reliability of the file
operations within our codebase.

Here are the key changes made in this commit:

  - Introduced a try-catch block around the file operation sections.
  - Within the try block, added code to perform the necessary file
    operations.
  - Implemented catch blocks to handle specific file exceptions.
  - In each catch block, included appropriate error handling logic,
    such as logging the error message or displaying a user-friendly
    error message.
  - Ensured that the catch blocks gracefully handle the exceptions
    and prevent the program from crashing or behaving unexpectedly.

By adding this exception handling code, we can anticipate and handle
potential file-related errors gracefully, providing a smoother
experience for users and preventing any unexpected crashes or data
loss. This would also aid in debugging issues.

Signed-off-by: jinuthomas <jinu.joy.thomas@in.ibm.com>

---
## [TheOneTheOnlySpoopyBoi/Apotheosis](https://github.com/TheOneTheOnlySpoopyBoi/Apotheosis)@[6ec7df8a9c...](https://github.com/TheOneTheOnlySpoopyBoi/Apotheosis/commit/6ec7df8a9c193b41e9a41bcab77ba701a29d10aa)
#### Wednesday 2023-07-12 03:38:23 by Conga Lyne

New Creep, New Items, Bug Fixes

New Creep: Corrupt Master of Vulnerability
New Item: Corrupt Stone
New item: Guiding Stone
Removed tablet eater component from most corrupt masters, this is to save on performance, however, they are now immune to physics damage
Removed some outdated glyphs
Updated Fungal Shift (spell) sprites
Updated Trophy Room's statues
Updated Aquamine's projectile graphic
Updated Heretic
Optimised Sienenkivi
Fixed Blob Cavern not generating properly when approached from the east
Fixed Porings not releasing fairies properly
Fixed tentacle limbs occasionally deteching from their host body and flailing wildly
Fixed Plane Radar not being an emissive sprite
Fixed a SpawnFunction clash with Armageddon Machine
Fixed the Mountain Altar looking for 33 and 34 orbs for their respective endings instead of taking the new orb rooms into account, you now require 45 and 46 orbs respectively.
Fixed Sienenkivi not converting Infectious Blood

---
## [ZerosLab/ZerosLab.github.io](https://github.com/ZerosLab/ZerosLab.github.io)@[12cf8c0ede...](https://github.com/ZerosLab/ZerosLab.github.io/commit/12cf8c0edee9c4c83e71e192e8e68872cba5162e)
#### Wednesday 2023-07-12 04:26:55 by Zero

Add files via upload

look i need a goddamn testing environment for this shit, will give its own repo in a minute, just trying to get this to actually fucking work first

---
## [proatgram/deathcounter_irl](https://github.com/proatgram/deathcounter_irl)@[0294c93476...](https://github.com/proatgram/deathcounter_irl/commit/0294c93476f2fc542c74b019e67853d3cacc4a1e)
#### Wednesday 2023-07-12 04:28:56 by Timothy Hutchins

CI/CD Builds use Unix Makefiles

Because fuck windows MSBuild and windows in general, causes nothing but absolute chauas, trouble, difficulty, and pain.

---
## [hragbalian/langchain](https://github.com/hragbalian/langchain)@[75fb9d2fdc...](https://github.com/hragbalian/langchain/commit/75fb9d2fdcc201e80ad9c065a02c6cc9ccf6d716)
#### Wednesday 2023-07-12 04:30:42 by Stefano Lottini

Cassandra support for chat history using CassIO library (#6771)

### Overview

This PR aims at building on #4378, expanding the capabilities and
building on top of the `cassIO` library to interface with the database
(as opposed to using the core drivers directly).

Usage of `cassIO` (a library abstracting Cassandra access for
ML/GenAI-specific purposes) is already established since #6426 was
merged, so no new dependencies are introduced.

In the same spirit, we try to uniform the interface for using Cassandra
instances throughout LangChain: all our appreciation of the work by
@jj701 notwithstanding, who paved the way for this incremental work
(thank you!), we identified a few reasons for changing the way a
`CassandraChatMessageHistory` is instantiated. Advocating a syntax
change is something we don't take lighthearted way, so we add some
explanations about this below.

Additionally, this PR expands on integration testing, enables use of
Cassandra's native Time-to-Live (TTL) features and improves the phrasing
around the notebook example and the short "integrations" documentation
paragraph.

We would kindly request @hwchase to review (since this is an elaboration
and proposed improvement of #4378 who had the same reviewer).

### About the __init__ breaking changes

There are
[many](https://docs.datastax.com/en/developer/python-driver/3.28/api/cassandra/cluster/)
options when creating the `Cluster` object, and new ones might be added
at any time. Choosing some of them and exposing them as `__init__`
parameters `CassandraChatMessageHistory` will prove to be insufficient
for at least some users.

On the other hand, working through `kwargs` or adding a long, long list
of arguments to `__init__` is not a desirable option either. For this
reason, (as done in #6426), we propose that whoever instantiates the
Chat Message History class provide a Cassandra `Session` object, ready
to use. This also enables easier injection of mocks and usage of
Cassandra-compatible connections (such as those to the cloud database
DataStax Astra DB, obtained with a different set of init parameters than
`contact_points` and `port`).

We feel that a breaking change might still be acceptable since LangChain
is at `0.*`. However, while maintaining that the approach we propose
will be more flexible in the future, room could be made for a
"compatibility layer" that respects the current init method. Honestly,
we would to that only if there are strong reasons for it, as that would
entail an additional maintenance burden.

### Other changes

We propose to remove the keyspace creation from the class code for two
reasons: first, production Cassandra instances often employ RBAC so that
the database user reading/writing from tables does not necessarily (and
generally shouldn't) have permission to create keyspaces, and second
that programmatic keyspace creation is not a best practice (it should be
done more or less manually, with extra care about schema mismatched
among nodes, etc). Removing this (usually unnecessary) operation from
the `__init__` path would also improve initialization performance
(shorter time).

We suggest, likewise, to remove the `__del__` method (which would close
the database connection), for the following reason: it is the
recommended best practice to create a single Cassandra `Session` object
throughout an application (it is a resource-heavy object capable to
handle concurrency internally), so in case Cassandra is used in other
ways by the app there is the risk of truncating the connection for all
usages when the history instance is destroyed. Moreover, the `Session`
object, in typical applications, is best left to garbage-collect itself
automatically.

As mentioned above, we defer the actual database I/O to the `cassIO`
library, which is designed to encode practices optimized for LLM
applications (among other) without the need to expose LangChain
developers to the internals of CQL (Cassandra Query Language). CassIO is
already employed by the LangChain's Vector Store support for Cassandra.

We added a few more connection options in the companion notebook example
(most notably, Astra DB) to encourage usage by anyone who cannot run
their own Cassandra cluster.

We surface the `ttl_seconds` option for automatic handling of an
expiration time to chat history messages, a likely useful feature given
that very old messages generally may lose their importance.

We elaborated a bit more on the integration testing (Time-to-live,
separation of "session ids", ...).

### Remarks from linter & co.

We reinstated `cassio` as a dependency both in the "optional" group and
in the "integration testing" group of `pyproject.toml`. This might not
be the right thing do to, in which case the author of this PR offer his
apologies (lack of confidence with Poetry - happy to be pointed in the
right direction, though!).

During linter tests, we were hit by some errors which appear unrelated
to the code in the PR. We left them here and report on them here for
awareness:

```
langchain/vectorstores/mongodb_atlas.py:137: error: Argument 1 to "insert_many" of "Collection" has incompatible type "List[Dict[str, Sequence[object]]]"; expected "Iterable[Union[MongoDBDocumentType, RawBSONDocument]]"  [arg-type]
langchain/vectorstores/mongodb_atlas.py:186: error: Argument 1 to "aggregate" of "Collection" has incompatible type "List[object]"; expected "Sequence[Mapping[str, Any]]"  [arg-type]

langchain/vectorstores/qdrant.py:16: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:19: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:20: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:22: error: Name "grpc" is not defined  [name-defined]
langchain/vectorstores/qdrant.py:23: error: Name "grpc" is not defined  [name-defined]
```

In the same spirit, we observe that to even get `import langchain` run,
it seems that a `pip install bs4` is missing from the minimal package
installation path.

Thank you!

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[68a899f5bd...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/68a899f5bd59f0ae7668c5f62810cc3a8d29d818)
#### Wednesday 2023-07-12 05:07:33 by Zergspower

[Manual Mirror Fix] Coroner additions and tweaks (#76534) (#22380)

* Coroner additions and tweaks (#76534)

## About The Pull Request

Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Serrated bone shovels can be used in place of circular saw in most
surgeries.

Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Increased the force, throwforce, and wound bonus of inert ritual knives
and scythes.

Coroner gloves can quickly apply medicine like nitrile gloves.
## Why It's Good For The Game

> Serrated bone shovels can be created with any kind of shovel now, not
just a spade (???)

Weird ass bug.

> Serrated bone shovels can be used in place of circular saw in most
surgeries.

It's serrated, it's cool, it's rare, it has a fast toolspeed.

> Added a duller (still deadly) variant of the serrated bone shovel as
coroner mail.

Very thematic for the coroner, should probably also be a heirloom item
but whatevs. Weaker so there's still a reason to seek out the OG.

> Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.

Scanning corpses is pretty important during surgery - it tells you how
much blood they have, organ damage, diseases... these things don't
appear in the surgical computer readout, which means the coroner has to
go out of his cave to pick up a boring light blue meatbag wound scanner.
This also incentivizes coroners to do their job by giving them something
cool that only works on dead bodies.

> Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.

These two options in the MortiDrobe are pretty frickin' badass,
especially with how SICK the Coroner looks with them, double especially
in combat.


![image](https://github.com/tgstation/tgstation/assets/53100513/98c6f8a5-3e5a-41a9-8a9c-cb6b82ecc0b8)

However, there's the large issue that as actual weapons they're really,
really weak. Not enough damage, when I use them in combat I both feel
badass but also get a nagging feeling in the back of my mind that I'm
intentionally gimping myself, and with only 10 damage I can *really*
feel it. I find it unfair that these are objectively worse than a
welding tool or even a Butcher's Cleaver when they're a lot more
involved to find, and scarce besides. These arguments apply equally to
the Wizard's ritual knife, and the scythe.

Additionally on the scythe, the crew really needs more good ghetto
weaponry that isn't the boring same ol' of baseball bats, spears,
cleavers... and making scythes useful is a great way to help bridge that
gap. They deal a satisfying amount of damage now, with the clear
downside, of course, being that they're bulky and hard to lug around.

> Coroner gloves can quickly apply medicine like nitrile gloves.

'Fast medicine' doesn't just cover sutures, it also covers medical gel.
Specifically, sterilizer gel. I find it annoying that the Coroner is
encouraged to give up his drip for the boring life-saver nitrile gloves,
because the difference in applying time really does make a difference -
it makes gel applying go from annoying to smooth, which is important
considering the whole purpose of sterilizer gel is to make surgeries go
faster. The Coroner has surgery and thus medical locker access to begin
with, so this isn't a balance problem, (and nitrile gloves are found by
the dozen anyways) especially with how rare the coroner gloves are.
## Changelog
:cl:
fix: Serrated bone shovels can be created with any kind of shovel now,
not just a spade (???)
add: Serrated bone shovels can be used in place of circular saw in most
surgeries.
add: Added a duller (still deadly) variant of the serrated bone shovel
as coroner mail.
add: Autopsy scanners now act as advanced health analyzers on dead and
seemingly-dead people.
add: Increased the force, throwforce, and wound bonus of inert ritual
knives and scythes.
add: Coroner gloves can quickly apply medicine like nitrile gloves.
/:cl:

* Modular Scythes

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [tjaslz/docs](https://github.com/tjaslz/docs)@[befe5f47a3...](https://github.com/tjaslz/docs/commit/befe5f47a3032c387f9f6946b1226f64b5fc2bc5)
#### Wednesday 2023-07-12 05:08:08 by tjaslz

Fuck u stupid ass Whore 

Banned me for No fucking reason bitch ass nigga

---
## [vdaular-dev/linksfordevs](https://github.com/vdaular-dev/linksfordevs)@[63c729b4c6...](https://github.com/vdaular-dev/linksfordevs/commit/63c729b4c6c5c6e01444275a20bde03c026f3736)
#### Wednesday 2023-07-12 05:25:28 by Ben Dornis

Updating: 7/11/2023 11:00:00 PM

 1. Added: I am happy right now.
    (https://www.joemmalatesta.com/blog/improvement/i-am-happy-right-now)
 2. Added: The Forms are Flooding In
    (https://angusform.com/blog/post/2023-07-10-forms-flooding-in/)
 3. Added: Y.K. Goon | Being an insomniac
    (https://ykgoon.com/being-an-insomniac.html)
 4. Added: My Thoughts on GPT Copyright
    (https://thatxliner.github.io/blog/posts/my-thoughts-on-gpt-copyright/)
 5. Added: Agile Antipattern: Overpromising Review
    (https://www.perdian.de/blog/2023/07/10/agile-antipattern-overpromising-review/)
 6. Added: Object Based Routing in Express.js
    (https://chauhankiran.blogspot.com/2023/07/object-based-routing-in-expressjs.html)
 7. Added: GPT might be an information virus – Non_Interactive – Software & ML
    (https://nonint.com/2023/03/09/gpt-might-be-an-information-virus/)
 8. Added: How I Made a Monorepo
    (https://gavinhoward.com/2023/07/how-i-made-a-monorepo/)
 9. Added: I want a clean config directory! :: rabbiticTranslator
    (https://rabbitictranslator.com/kconfig/)
10. Added: What is Functional Programming? · Joseph Yiasemides
    (https://joseph.yiasemides.com/posts/what-is-functional-programming)
11. Added: Rails Generate Migration — Everything you need to know about generating migrations in your Ruby on Rails app
    (https://railsnotes.xyz/blog/rails-generate-migration-everything-you-need-to-know)
12. Added: Never waste your midlife crisis - Austin Kleon
    (https://austinkleon.com/2023/07/10/never-waste-a-midlife-crisis/)
13. Added: My jeans’ metadata may outlive the company that sold them
    (https://ericwbailey.website/published/my-jeans-metadata-may-outlive-the-company-that-sold-them/)
14. Added: Proof You Can Do Hard Things
    (https://blog.nateliason.com/p/proof-you-can-do-hard-things)
15. Added: The “Everything is a Q-Wave” Interpretation of Quantum Physics » Vlatko Vedral
    (https://www.vlatkovedral.com/the-everything-is-a-q-wave-interpretation-of-quantum-physics/)
16. Added: The Weight of Data
    (https://keefmck.blogspot.com/2023/07/the-weight-of-data.html)
17. Added: Hackers, write.
    (https://diego.posthaven.com/hackers-write)
18. Added: Tracking Meta's Threads' Launch
    (https://blog.darn.fish/tracking-threads)
19. Added: Goodbye, Planck EZ | ZSA: The Blog
    (https://blog.zsa.io/2307-goodbye-planck-ez/)
20. Added: Coping with non-free Debian – Simon Josefsson's blog
    (https://blog.josefsson.org/2023/07/11/coping-with-non-free-debian/)
21. Added: Croppenheimer - foobuzz
    (https://blog.valentin.sh/croppenheimer/)

Generation took: 00:11:41.2651485
 Maintenance update - cleaning up homepage and feed

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[721fd30837...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/721fd308378dc6ef7595c1ea4b92d679ba723188)
#### Wednesday 2023-07-12 06:04:40 by carlarctg

Heavily reworks and resprites first aid analyzers. (#76533)

## About The Pull Request

Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

First aid analyzers are now found in all basic and specialized medkits.
Toxin medkits get a new* disease analyzer. Miners get a miner-colored
one in their box.

Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

Health analyzers now have a scanning sound, courtesy of CM.

Refactored some wound code to make treatment duration changes and
changes in the description of wounds easier.

Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.

Surgical processors and slime scanners have recieved a similar resprite.
## Why It's Good For The Game

> Heavily reworks and resprites first aid analyzers. They now display if
they're happy, sad, angry, or warning you! Also a 'pricking' animation.

These things have long, long needed some sprite love. Displaying emotion
will make them have a lot more 'weight' to them, same with the prick.
The old, shitty spectrometer sprites have gone directly into the
dumpster.

> First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.

They have also needed some gameplay love! Placing them in these kits is
not going to be a massive game-changer when they were already easily
found around the station in emergency medkits, but it will fill up that
awkward empty slot.

> Scanning yourself with a first aid analyzer will 'create a holo-image
with treatment instructions next to your wounds', doubling the speed of
treatment of scanned wounds!

The biggest gameplay-impacting change in this PR, I *sincerely* believe
this is the perfect solution to first aid analyzers being completely
redundant with eyesight. This lets you/someone else scan your wounds to
speed up treatment, with a neat in-character reason for it -
'holo-images' appearing on your body, like penlights.

This will speed up wound treatment, but I believe that is for the best,
as currently treating wounds is so slow that half the time it's not
worth it (or more accurately, it doesn't feel worth it in comparison to
the effort you're putting in) and you're better off shrugging off minor
wounds. It will do so in a way that requires a modicum of effort, so
it's not just a flat buff across the land.

> Health analyzers and gene scanners now have a scanning sound, courtesy
of CM.

It's a neat sound that will make medbay feel more alive. First aid
analyzers get a beeboop instead.

> Surgical processors and slime scanners have recieved a similar
resprite.

IT'S SPRITE MANIA IN HERE
## Changelog
:cl:
Carlarc, Weird Orb
image: Heavily reworks and resprites first aid analyzers. They now
display if they're happy, sad, angry, or warning you! Also a 'pricking'
animation.
add: First aid analyzers are now found in all basic and specialized
medkits. Toxin medkits get a new* disease analyzer. Miners get a
miner-colored one in their box.
balance: Scanning yourself with a first aid analyzer will 'create a
holo-image with treatment instructions next to your wounds', doubling
the speed of treatment of scanned wounds!
sound: Health analyzers and gene scanners now have a scanning sound,
courtesy of CM.
refactor: Refactored some wound code to make treatment duration changes
and changes in the description of wounds easier.
fix: Fixed a dummy parent feature of the health analyzer (Verbose mode)
showing up, uselessly, on the disease and first aid subtypes.
image: Surgical processors and slime scanners have recieved a similar
resprite.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[a2c8cce535...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/a2c8cce5359162a8a697ce109801ec268bf0c8a5)
#### Wednesday 2023-07-12 06:04:40 by John Willard

Bilingual can now choose their language (#76609)

## About The Pull Request

This was one of the tradeoffs for removing other, more consistent
sources of languages, and was requested by Melbert among many others.
This does go against my wanted goal of decreasing the risk of
eavesdropping by other players through just magically knowing a
language, but it is an expensive quirk and it is in their medical
records, which makes it better than language encryption keys or silicon
just innately knowing them.

This also limits Bilingual to only roundstart languages (+Uncommon),
rather than being randomly selected from a list (that had very useless
ones like monkey, podpeople, and beachbum). This is mostly just for
modularity, I didn't want to make it look terrible code-wise and thought
this may be the optimal way to handle it.

This is also me going back on
https://github.com/tgstation/tgstation/pull/71773 - which I had closed
myself.

## Why It's Good For The Game

If we're gonna keep the Bilingual quirk, it might as well be something
players can choose the language of, it's their character and they should
be allowed to decide how their character is, and it is my fault that
this stupid compromise of "getting a random language" was made in the
first place. It never should've happened.
It now actually limits it to roundstart-only languages, so there's no
way you can spy on people who prepare in advance through becoming
podpeople, or monkeys, etc.

## Changelog

:cl:
balance: Bilingual quirk now lets you choose your language between ones
given to roundstart species.
balance: Foreigner and Bilingual are now mutually exclusive languages.
/:cl:

---
## [santosh337/Module2](https://github.com/santosh337/Module2)@[53390226af...](https://github.com/santosh337/Module2/commit/53390226afad62e06f19d36edb1ae1765f37b76d)
#### Wednesday 2023-07-12 06:58:56 by Santosh Sugur

Create is Equal ? .java

Once there was a girl named Sarah who loved to write poetry. She had a habit of writting down her thoughts in a notebook whenever she felt inspired. One day, while she was working on a new piece, she accidentally spilled her coffee on the notebook.

Desperate to salvage her work, she decided to copy the poem onto a new page. However, when she finished rewriting it, she noticed that there were a few discrepancies between the original version and the new one. She wondered if she had missed anything while transcribing the poem.

Help Sarah and write a program that check if two strings are identical or not.

Input Format

First line contains string s1.

Second line contains strinf s2.

Constraints

1 <= string1.length() <= 100000

1 <= string2.length() <= 100000
Output Format

Return A boolean value

Sample Input 0

GEEKSTER
GEEKSTER
Sample Output 0

true
Explanation 0

since both string have same character at each index. therfore it is a equal string

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[c4b550c1a9...](https://github.com/Paxilmaniac/Skyrat-tg/commit/c4b550c1a94670ae333df12b8200ff33f7f7f175)
#### Wednesday 2023-07-12 07:08:58 by SkyratBot

[MIRROR] New Wizard spell "branch": Vendormancy [MDB IGNORE] (#22008)

* New Wizard spell "branch": Vendormancy (#75679)

## About The Pull Request
New item for wizards, ~~the Staff~~ Scepter of Runic Vendormancy.

With it, you can summon Runic Vending machines to block your enemies,
push them 2 tiles back around the summoning tile, throw the vendors 4
tiles away to squash them or simple detonate the vendors for direct
damage against enemies within a 2 tile range.

The scepter has 3 charges that can be recharged after a "long" channel
so while powerful, it is a tactical weapon and wizards can't directly
steamroll the crew with endless vendors. (Unless they buy multiple
scepters, but that is just funny.)

Also, there is a bug with the throw... I copied how baseball bats deal
with knockback, but they consistently don't push the vendors back, just
spin them on the same tile... I appreciate if anyone has any idea on how
to fix or change that to a better system.

## New changes I made
The vendor has a random set of REAL wizard robes and hat, sandals and a
foam vendor scepter as products to sell now.
This gives the crew some real armor, and if it is considered too much, I
can swap it for the fake versions.
IMO the real clothes work as the perfect bait for the crew to approach
the vendors and get exploded in the process, and while a random
assistant might get real wizard armor to go valid hunt the wizard, the
crew might just mistake them for the real wizard and beat them to death,
which is too funny.
## Why It's Good For The Game

![vendormancerPR](https://github.com/tgstation/tgstation/assets/55374212/f9d98f3e-5916-4a17-987e-249f4cdb7185)

About a year ago I played Stoneshard, and it has such an amazing
Geomancy Wizard that I wanted to port some of its gameplay to SS13 as
our wizards, while funny and destructive, are kinda simple to play...

Summoning and blowing up rocks was nice, but I randomly had the idea of
summoning Vendors while at work and vendors squashing people has become
such an iconic SS13 thing to me that I had to stop being lazy and start
working on this.

Something, something, enviromental combat wizard.
## Changelog
Gonna polish the changelog later too...
:cl: Guillaume Prata
add: New Wizard spell branch: Vendormacy! Summon runic vending machines
with your Vending Scepter, force push them on your enemies to squish
them or blow them up while they are busy buying from the machines.
/:cl:

---------

Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

* New Wizard spell "branch": Vendormancy

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

---
## [isaquetp/kernel_moba](https://github.com/isaquetp/kernel_moba)@[991467a47c...](https://github.com/isaquetp/kernel_moba/commit/991467a47cf250abfc624acdc1929a5936cfefa9)
#### Wednesday 2023-07-12 08:32:24 by Linus Torvalds

Revert "x86/apic: Include the LDR when clearing out APIC registers"

[ Upstream commit 950b07c14e8c59444e2359f15fd70ed5112e11a0 ]

This reverts commit 558682b5291937a70748d36fd9ba757fb25b99ae.

Chris Wilson reports that it breaks his CPU hotplug test scripts.  In
particular, it breaks offlining and then re-onlining the boot CPU, which
we treat specially (and the BIOS does too).

The symptoms are that we can offline the CPU, but it then does not come
back online again:

    smpboot: CPU 0 is now offline
    smpboot: Booting Node 0 Processor 0 APIC 0x0
    smpboot: do_boot_cpu failed(-1) to wakeup CPU#0

Thomas says he knows why it's broken (my personal suspicion: our magic
handling of the "cpu0_logical_apicid" thing), but for 5.3 the right fix
is to just revert it, since we've never touched the LDR bits before, and
it's not worth the risk to do anything else at this stage.

[ Hotpluging of the boot CPU is special anyway, and should be off by
  default. See the "BOOTPARAM_HOTPLUG_CPU0" config option and the
  cpu0_hotplug kernel parameter.

  In general you should not do it, and it has various known limitations
  (hibernate and suspend require the boot CPU, for example).

  But it should work, even if the boot CPU is special and needs careful
  treatment       - Linus ]

Link: https://lore.kernel.org/lkml/156785100521.13300.14461504732265570003@skylake-alporthouse-com/
Reported-by: Chris Wilson <chris@chris-wilson.co.uk>
Acked-by: Thomas Gleixner <tglx@linutronix.de>
Cc: Bandan Das <bsd@redhat.com>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Sasha Levin <sashal@kernel.org>

---
## [hz-devops-test/hazelcast](https://github.com/hz-devops-test/hazelcast)@[566574a5b4...](https://github.com/hz-devops-test/hazelcast/commit/566574a5b49f423109a4de61f21427838bd8076b)
#### Wednesday 2023-07-12 08:34:52 by James Holgate

Modify KubernetesClient shutdown behaviour  (#24613) [5.3.z] (#24710)

Backport of: https://github.com/hazelcast/hazelcast/pull/24613

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
## [alexandre-daubois/symfony](https://github.com/alexandre-daubois/symfony)@[af44385d9e...](https://github.com/alexandre-daubois/symfony/commit/af44385d9e6eba77b4bf4610231ce9569bdcc9b5)
#### Wednesday 2023-07-12 08:38:36 by Robin Chalas

feature #50754 [HttpKernel] when configuring the container add services_{env} with php extension  (helyakin)

This PR was merged into the 6.4 branch.

Discussion
----------

[HttpKernel] when configuring the container add services_{env} with php extension

| Q             | A
| ------------- | ---
| Branch?       | 6.4
| Bug fix?      | no
| New feature?  | yes
| Deprecations? | no
| Tickets       | none
| License       | MIT

Hello the community

This is my first PR attempt.

So after reading this [documentation](https://symfony.com/doc/current/service_container.html#remove-services) and unsuccessfully trying to load my `service_test.php`, I've noticed that the `configureContainer(..)` function in the `MicroKernelTrait` file was not configured to automatically load this file.

So either we should fix the documentation, either we should fix the configuration.

Since this the [framework-bundle](https://github.com/symfony/framework-bundle) is backed by [Alximy](https://alximy.io) I figured it would be cool 😎 to try and fix 🐛 the configuration.

Anyway share me your thoughts about what should be done !

And I wanted to say that php service configuration is 🔥 so shoutout to the one who did this (I think it's you `@nicolas`-grekas with this [PR](https://github.com/symfony/symfony/pull/23834) right ? 💪🏻)

Also big thanks to `@jeremyFreeAgent` for debugging this with me and `@HeahDude` for showing me the php service configuration PR.

Commits
-------

4aac1d9fee :bug: (kernel) when configuring the container add services with php ext

---
## [wangshunnn/react](https://github.com/wangshunnn/react)@[b6978bc38f...](https://github.com/wangshunnn/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Wednesday 2023-07-12 08:48:41 by Andrew Clark

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
## [laminas/laminas-authentication](https://github.com/laminas/laminas-authentication)@[2bdd7faf28...](https://github.com/laminas/laminas-authentication/commit/2bdd7faf28dffe187cd663c58b9c0c9f935ec95d)
#### Wednesday 2023-07-12 09:18:51 by Michał Bundyra

Message against the war, in Russian and English

🇷🇺 Русским гражданам

Мы, участники Laminas, родились и живем в разных странах. У многих из нас есть друзья, родственники и коллеги как в России, так и в Украине. Некоторые из нас родились в России. Некоторые из нас живут в России. У некоторых бабушки и дедушки сражались с фашистами во Второй мировой войне. Здесь никто не поддерживает фашизм.

У одного из нас есть украинская родственница, которая спаслась из дома вместе с сыном. Поезд задержался из-за бомбежки на дороге впереди. У нас есть друзья, которые прячутся в бомбоубежищах. Мы с тревогой ждем весточки от них после воздушных налетов, которые беспорядочно наносят удары и попадают по больницам, школам, детским садам и домам. Мы не берем это из каких-либо СМИ. Мы наблюдаем это напрямую.

Вы доверяете нам достаточно, чтоб использовать наши программы, и мы просим вас довериться нам вновь. Мы нуждаемся в помощи. Выходите и протестуйте против этой бесполезной войны. Остановите кровопролитие. Скажите "Нет войне!"

🇺🇸 To Citizens of Russia

We at Laminas come from all over the world. Many of us have friends, family and colleagues in both Russia and Ukraine. Some of us were born in Russia. Some of us currently live in Russia. Some have grandparents who fought Nazis in World War II. Nobody here supports fascism.

One team member has a Ukrainian relative who fled her home with her son. The train was delayed due to bombing on the road ahead. We have friends who are hiding in bomb shelters. We anxiously follow up on them after the air raids, which indiscriminately fire at hospitals, schools, kindergartens and houses. Were not taking this from any media. These are our actual experiences.

You trust us enough to use our software. We ask that you trust us to say the truth on this. We need your help. Go out and protest this unnecessary war. Stop the bloodshed. Say "stop the war!"

Signed-off-by: Michał Bundyra <contact@webimpress.com>

---
## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[1880023187...](https://github.com/Mu-L/crawl/commit/18800231877e12caceb48c2f929f842d55aac934)
#### Wednesday 2023-07-12 09:33:07 by Nicholas Feinberg

Tweak forms

This change is intended to allow more opportunities for players to shift
into or out of a 'transmuter' playstyle, to improve the UI of forms, and to
improve some miscellaneous issues, e.g. Lichform being useless in 3-rune games.
For more context, see https://github.com/crawl/crawl/wiki/Transmutations-Reform.

Throughout, balance is a very rough sketch. I expect many things will need to
be buffed, others will need to be nerfed, and some will need to be replaced
entirely. This is a grand experiment, not a final state.

Talismans
---------

The largest change is that forms are no longer entered via spells. Instead,
special items called 'talismans' must be found and evoked. Once entered,
these 'talisman forms' last indefinitely.

Further notes on talismans:
- Talismans scale only on Shapeshifting skill (more on this later). They
  do not care about Int, Spellcasting, other spell schools, wizardry, or
  encumbrance. (That is, they aren't spells.)
- Talisman forms have a 'minimum skill'. Below that skill, entering the
  talisman form will reduce the user's maximum HP (while in the form).
  This is intended to roughly mimic the inability to effectively cast
  spells at low skills/high fail% - it provides a space in which an 'early'
  form can be better than a 'later' one, even if you've found both.
- Talisman forms have a 'maximum skill'. Above that skill, no further
  scaling applies. This is intended to roughly mimic max spellpower - it
  makes it more obvious that later-game forms will end up outscaling
  earlier ones.
- It takes 5 turns to enter or leave a talisman form, exactly as with
  armour or amulets. Use of a talisman form is intended to be a strategic
  decision, again like wearing armour, rather than something swapped in
  each fight.
- Talismans don't need to be held after they're used. You can evoke them
  from the floor and leave them there. This avoids inventory pressure.
- Talismans can be used with Sacrifice Artifice, since they don't use Evo.
- Zin instantly excommunicates users of a talisman. Take that, nerds!
- Trog is A-OK with talismans, just as with wands, magic swords, etc.

Art for talismans is pending.

Skills
------

Transmutations skill has been split in two. Talismans use a new skill,
Shapeshifting, and remaining Transmutations spells (of which there are
still nine, more than one other school!) continue to use Transmutations
skill. There was very little synergy or overlap between forms and Tmut
spells, and this makes it easier to make skilling decisions. Some argue
that Transmutations should be abolished entirely and its spells punted
into other schools; we'll see.

Shapeshifting aptitudes look broadly like Transmutations aptitudes,
with a -2 penalty applied so that forms are costly enough now that
they're all "single-school" and don't require Int. (That is, Humans
have a Shapeshifting apt of -2, etc.) A few species have had their
apts adjusted to account for the new role of Shapeshifting, but more
could be done here.

Background
----------

The Transmuter background has been replaced with a Shapeshifter, who
starts with a beast talisman and no spells. Their stats have been
adjusted accordingly.

Forms
-----

The following forms exist:

*Beast*: This is the starting form for the Shapeshifter background. It
melds all aux armours in exchange for a Slaying bonus (ala Wereblood) -
+2 at 0 skill, +8 at 13 skill (max).

This is intended to provide a bonus which is compelling early game (when no
or few aux armours have been found) but more tenuous later, especially for
non-transmuters. It's also intended to provide a bridge between Tmut and
weapon use, since a transmuter who finds a great weapon can switch from UC
to that weapon without giving up their form and Tmut training.

Beast form allows use of body armour so that it can present a reasonable
slay-for-AC tradeoff without becoming overly strong for 'dex-based' characters,
who wouldn't mind losing body armour nearly as much.

*Anaconda*: This is a tier 2 form. Anaconda form turns you into a giant
anaconda. All your items meld, you can constrict, you get some AC and an HP
bonus...

This is intended to replace Ice Form, a form to help transmuters transition
into the mid-game. The rF- of Ice Form is less appropriate for early-game
characters who can no longer switch between forms, and Ice Form is not
evocative - no one gets Ice Beasts. On the other hand, turning into a snake...
everyone gets that. That's the dream. Limbs are for dorks. Ssssss

*Maw*: This is a tier 2 form. Maw form melds the body slot, transforming it
into a giant mouth, ala the Brazilian Mapinguari. The maw provides an aux
attack with damage that scales on Shapeshifting skill. It also has the old
Hydra form devour-on-kill-for-hp gimmick, since everyone loved that.

This is intended to be a way that Shapeshifters can transition into the mid-game,
especially transmuters who use weapons. It's probably a bit too strong for
quick blade users at present - perhaps I'll give it +str -dex, or something.
(It may also just be too strong in general - numbers are WIP!)

*Blade*: This is a tier 2 form. It's blade hands. To compensate for it
being easier to enter, its UC damage has gone down slightly (22 -> 18).

It also now gives a deformed body-like AC penalty based on base body armour AC,
scaling from a 100% penalty at min Shapeshifting skill to 0% at max skill.
(That is, at min skill, +2 plate armour will just give you +2 AC, plus whatever
you get from Armour skill.) This is intended to model the dynamic of old Blade
Hands - pure glass cannon when you can only cast it in robes, later on more
usable in actual armour. Your body is deformed because there are blades inside.
Aaiiii!

This is intended to be another way that Shapeshifters can transition into the
mid-game.

*Statue*: This is a tier 3 form. It's statue form. Intended to be a way
for transmuters to head into late-game while still being able to use weapons,
if desired. Might need to be a bit stronger for weapon users.

*Dragon*: This is a tier 3 form. It's dragon form. AC and UC damage now
scale slightly with Tmut skill. Intended to be a way for transmuters to
head into late-game. Possible this should be tier 4 and Storm should be tier
3 - dragons are cool! Dragons should be the best!

*Storm*: This is a tier 4 form. It's storm form. Intended for players who
want to dump ludicrous amount of skill XP into tmut. Top end has been
adjusted somewhat downward.

*Death*: This is a tier 4 form. Replacing Necromutation/Lich Form, Death
Form makes you dead (no drinking potions, holy wrath/dispel undead vuln,
rC, rTorm, rPois, etc) and also gives you an assortment of spicy powers.
On hit (with melee/UC), victims get slowed, weakened, and heavily drained.
There's also a new active, Siphon Essence, which costs 20 (!) MP, halves
the HP of all enemies in radius 2, and heals you based on damage dealt and
Tmut skill. (That works on all non-MH_NONLIVING enemies, as do the debuffs.)

It no longer provides innate AC or Will, nor does it give a necro enhancer.
Its UC damage is now significantly higher, comparable to blade hands,
though still much lower than Statue, Dragon or Storm.

This is intended to be a way for players who want to spend huge skill XP
on tmut to do so, including those who use tmuts + weapons. It's intended
to feel a bit different from other forms while still being competitive in
melee. Other forms have huge base damage - Death Form has lower damage but
very strong debuffs. Other forms have AC (Statue), HP (Dragon) or EV (Storm) -
Death Form gives Siphon Essence as a very powerful survival tool.

Other Notes
-----------

Various books have been merged and consolidated to make up for the
removal of eight spells. It *might* make sense to drop the book generation
rate slightly, but I haven't done this yet.

Some uniques now spawn with talismans. More could be done with this, e.g.
placing talismans of death in Crypt.

Later changes
-------------

Talisman acquirement is a must. TODO.

In the future, artefact talismans (i.e. randarts) could be interesting -
to provide more excitement for rare finds. The randarts would have
the usual panoply of properties (rF+, Dex-2, etc), which would apply
while the player was in the relevant form.

It'd be fun to add more form types, e.g. ones that work well for
'casters'.

Might be interesting to have talismans start unidentified (like staves),
for a frisson of excitement in gauntlets etc.

Possibly Wanderers should get a chance to start with beast talisman?

---
## [CogPlatform/Psychtoolbox-3](https://github.com/CogPlatform/Psychtoolbox-3)@[1d87e20d5d...](https://github.com/CogPlatform/Psychtoolbox-3/commit/1d87e20d5deba531f6ae8ce6d4b5c98486884d4f)
#### Wednesday 2023-07-12 10:08:16 by kleinerm

Merge pull request #796 from kleinerm/master

Pull request for Psychtoolbox 3.0.19

### Compatibility:

- Effective now, Psychtoolbox 3.0.18 is end of life and unsupported.

- GStreamer 1.20.5 or later required on MS-Windows, GStreamer 1.22.0 recommended on
  Windows and macOS.

- Octave 6 support cancelled, except for Linux. Octave 7.3 required on macOS and
  Windows.

- New baseline Matlab is R2022b.

- Recommended operating systems: Ubuntu 22.04-LTS Linux, MS-Windows 10, macOS 12.6.

- Ubuntu 20.04-LTS is considered in maintenance mode now. I will likely terminate its
  support in the foreseeable future. Lack of funding by our users makes it impossible
  to provide the levels of long term support as in the past, even for the best suited
  operating system for neuroscience :(.
  
- RaspberryPi OS 10 support is terminated. OS 11 32-Bit required.

- Support for all Windows versions older than recent Windows-10 will soon be completely
  removed. Stick to older Psychtoolbox versions if you want to continue older versions
  for some insane reason. All Windows versions older than Windows 10 are now dead, even
  for Microsoft customers which paid for expensive extended security support.
  It is dead, Jim!

- The macOS 10 (aka Mac OSX) and macOS 11 operating systems should continue to work
  but are officially unsupported and unsupportable. macOS 13 or Apple Silicon is not
  officially supported by this release.

### Highlights:

- OpenXR cross-platform, cross-vendor, cross-device support for VR/AR/MR/XR applications.
  A new modern foundation for these kind of things, highly extensible, future proof, and
  supports a much wider range of devices.

- Improved display mirroring support, including scaling and experimenter overlays for
  having setups with a stimulus monitor for the subject and a "experimenter console" /
  "experimenter control monitor" for the experimenter. PTB is still the only software
  that allows such setups without expensive special hardware and/or screwing up visual
  stimulation timing and timestamping. There are still corner cases where this is difficult,
  but we are better than ever now, increasing our lead over other toolkits further.

- Improved low-level USB support, especially useful for the PsyCalibrator toolbox for
  display calibration under Octave and Matlab.

- ASIO support for Matlab users on Windows sort-of back through the backdoor, without
  us actually having to add it back or dealing with the legal and licensing nightmares.

- Shitloads of new workarounds for shittons of new bugs brought to you by the iPhone
  company in their latest iToys operating systems.

### All:

- The main new feature, after over 700 hours of development, spread over 12 months,
  is our new OpenXR driver for virtual reality, augmented reality and mixed reality
  applications, known as eXtended Reality. The new PsychOpenXR driver should work on
  all VR/AR/MR/XR devices from all vendors on all operating systems which have an
  OpenXR 1 specification compliant runtime installed on your machine. So far the theory.
  In practice, this means GNU/Linux X11 and MS-Windows 10 and later, and so far it has
  only be tested with an Oculus Rift CV-1 VR HMD and Oculus touch controllers, remote
  and XBox 360 controller. Code for using other form-factors than VR HMD's is not yet
  implemented, but this driver should provide the foundation for relatively extension
  into this new realms if wanted. The whole topic deserves its own dedicated and detailed
  posts, so stay tuned. Some more overview info and setup instructions are to be found via
  'help OpenXR', the new drivers specific api in 'help PsychOpenXR', the general api
  improvements and help - sufficient for most use cases - in 'help PsychVRHMD', as before.
  Development of this driver was sponsored by a consumer VR company which wants to stay
  anonymous and not specifically credited here, so thank you for contributing most of the
  funding. As funding was insufficient to complete this very complex project, Mathworks
  (https://www.mathworks.com/solutions/neuroscience.html) sponsored another quarter of the
  remaining costs, thanks! Of course that means some other highly interesting project had
  to be delayed indefinitely, as the amount of funding we get from Mathworks is fixed, just
  the distribution of the fixed some to work items is flexible. In total, funding was totally
  insufficient for making any urgently needed profit or even breaking even nonetheless, so we
  end this one year project with a serious net loss of over 3000 Euros at this point, without
  the project being finished to my quality and performance standards, barely reaching what I
  would consider the minimum viable product from my perspective, but almost certainly still
  much better than anything competing out there for vision science applications. I expect
  more financial losses related to this area of functionality unless new contract work or
  funding come in, related to OpenXR aka VR/AR/MR/XR applications.

  The new driver should be reasonably backwareds compatible, essentially a drop-in replacement,
  so code written to our recommendations should work unchanged, just on a much wider variety
  of VR hardware than before.

  Effective immediately this means that all our old drivers are now considered to be in
  minimal maintenance mode - critical bug fixes only, no further enhancements. They are
  scheduled for removal as soon as the OpenXR driver has proven its maturity to some degree.

- Tons of minor bug fixes and improvements.

- PsychPortAudio: Improve diagnostics and help texts for channel mapping, and a new demo for
  multi-channel audio output, named BasicSoundChannelHoppingDemo.m which motivated those
  improvements, demonstrating dynamic switching between channels of a multi-channel sound card,
  e.g., hopping between the channels of a 24 channel sound card.

- SetStereoSideBySideParameters(): Add option to specify offsets in pixels, and add basic
  RemapMouse() support to deal better with changed stereo display geometry. Various other
  compatibility fixes to SetStereoSideBySideParameters() and RemapMouse() in combination with
  stereo display modes in combination with imaging pipeline geometric transformations like
  FlipHorizontal or FlipVertical. Also for 90 degree step rotation with the PanelFitter.

- Screen: Fix PsychImaging task 'MirrorDisplayTo2ndOutputHead' for most use cases.
  Turns out that this display mirroring task for macOS and MS-Windows only worked for
  trivial configurations without use of the panelfitter, MSAA, image processing or other
  complexities. It also works now when combined with the Vulkan special purpose display
  backend as primary stimulus display and the regular OpenGL method for the "experimenter
  feedback" / "control console" mirror display.

- Add overlay support to the display mirroring tasks 'MirrorDisplayTo2ndOutputHead' and
  'MirrorDisplayToSingleSplitWindow'. The new optional useOverlay parameter for these
  PsychImaging tasks generates a (normally transparent) overlay window, a "head up display"
  on top of the mirror window that shows a mirror image of the stimulus presented to the
  subject on the main stimulation display. overlaywin = PsychImaging('GetMirrorOverlayWindow', win);
  allows to get a window handle overlaywin to this overlay and then use Screen drawing commands
  to draw info only meant to be seen by the experimenter, not the subject, into the overlay.
  A common use case seems to be gaze position or gaze traces of a subject in eyetracking tasks,
  or other live feedback about task progression and subject performance. This is generally
  more flexible than hardware solutions, e.g., as provided by VPixx stimulators or similar
  equipment or some display splitters.

- PsychImaging: Allow size spec of mirror image for mirroring task 'MirrorDisplayToSingleSplitWindow'.
  Dealing with setups where the mirror/console/experimenter monitor has a lower/different resolution
  than the stimulus monitor needs same special rescaling of the mirror image. Implement rescaling +
  some minor optimizations. A future extension may allow to automate handling of such less standard
  display setups, but for now the user has to specify mirror monitor display resolution manually via
  a new optional parameter.

- PsychHID: Add support for synchronous USB bulk and interrupt transfers, and manual of automatic
  claiming of USB interfaces. The new subfunctions 'USBBulkTransfer' and 'USBInterruptTransfer'
  implement synchronous bulk and interrupt transfers. This now allows writing M-File drivers
  for more research equipment. The main motivation was to enable the free and open-source
  PsyCalibrator toolbox for Octave and Matlab to implement support for many more Photometers
  and other light measurement devices in a more efficient manner, starting with the cheap
  SpyderX device. Cfe. https://github.com/yangzhangpsy/PsyCalibrator

- PsychHID: Add PsychHID('USBClaimInterface', usbHandle, interfaceId) for manual claiming of
  device interfaces. This function allows to explicitely claim a USB interface to enable it
  for I/O from/to an USB interface endpoint. Bulk- or interrupt transfers don't work if the
  interface who owns the endpoint has not been claimed. If a call to this function is omitted
  before doing bulk or interrupt transfers, then PsychHID will automatically claim interface 0.
  Claimed interfaces are auto-released when closing an USB device. Kernel drivers potentially
  attached to - and blocking - an interface will be automatically detached, and then reattached
  at device close. In other words: Use of the most commonly used interface 0 does not need any
  extra user code. Use of other interfaces will require this call in time.

  On macOS: Note that if a macOS kernel driver (kext) has already claimed exclusive access to the
  device, then this will only work by detaching the kernel driver, which requires you to run Octave
  or Matlab as root. Only tested by myself with octave via "sudo octave" so far. For the hoops you
  have to jump through on macOS to get this working without sudo, read this FAQ:

  https://github.com/libusb/libusb/wiki/FAQ#how-can-i-run-libusb-applications-under-mac-os-x-if-there-is-already-a-kernel-extension-installed-for-the-device-and-claim-exclusive-access

  Executive summary: Give up, or be prepared to suffer greatly!

- Various help text and documentation updates.

- Terminate support for Python 2.x, it is officially end-of-life since beginning 2020. Only
  Python 3.6 and later are supported by our Python "Mex files" going forward. This makes the
  files also forward compatible with more Python versions by opt-in use of the Py limited api.
  Contributed mostly by Alex Forrence, with some tweaks by Mario Kleiner. Various other minor
  enhancements to PsychPython.
  
### Linux:

- Add support for 64-Bit Octave 7.x, implemented via the shared mex files for Octave 4.4 - Octave 7.3.
  This enables use with Octave on Ubuntu 22.10.

- Screen: Add gpu detection support for NVidia 170 "Ampere" gpu family and "Ada Lovelace" gpu
  family. Avoids some confusing warning and may improve Flip performance by a few dozen microseconds
  in some cases. Use of NVidia graphics cards is still discouraged due to the need of proprietary
  graphics drivers for all modern models, which limit useful functionality compared to gpus with
  open-source drivers, and make general use more tedious and troublesome.

- Drawtext plugin: Add workaround for Mesa bug with small non-anti-aliased text of 8 pixels and
  less. Rarely needed, but somebody in the VR research community needed it, so there.

- Compatibility fixes for the RaspberryPi on RaspberryPi OS 11 aka Debian 11 stable. Especially
  for old RPi 1,2,3 with VideoCore-4 gpu, XOrgConfCreator now generates a special xorg.conf
  file to enable fixes for these gpu's which were not neccessary on older RaspberryPi OS versions.
  Other misc compatibility improvements.
  
  Our build system for ARM / RaspberryPi is no 32-Bit RaspberryPi OS 11, with 32-Bit Octave 6.2,
  32-Bit ARM RaspberryPi 400. 64-Bit operating systems are not supported, and support for the
  legacy RaspberryPi OS 10 is now terminated.

- gamemode.ini: Comment out the amd_performance_level=high gpu perf option.
  Setting amd_performance_level=high for high performance level was found
  to cause stability issues at least on AMD Ryzen-5 2400G "RavenRidge" under
  Ubuntu 20.04.5-LTS with Linux 5.15 under prolonged load, likely a cooling problem.
  It may be safe to enable it for other AMD gpu's, especially well-cooled
  or discrete ones, but better safe than sorry by default, as i don't like
  my main devel machine crashing regularly and other users may also have machines
  with shaky cooling.


### Windows:

- 64-Bit Intel MSVC GStreamer version 1.20.5 is now required as minimum supported version
  for both Octave and Matlab. High quality text rendering will fail with any earlier version!
  From now on we always use the fontconfig-1.dll bundled with GStreamer 1.20.5 and later for
  font matching, which should simplify debugging of future issues on MS-Windows. This version
  also enables the ability to use User installed 3rd party fonts without extra configuration
  work by the user, obsoleting various hacks. GStreamer 1.22.0 was also lightly tested without
  obvious problems, so upgrading to 1.22.0 is recommended for new features, wider support for
  audio/video formats, improved performance and various bug fixes in the multi-media area.

- 64-Bit GNU/Octave 7.3 required for running Psychtoolbox 3.0.19 on Octave.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- PsychPortAudio: Allow use of a wider range of 3rd party portaudio_x64.dll plugins for the
  underlying PortAudio engine implementation. The most interesting use case of this is for
  users of Matlab, as recent versions of Matlab ship with a Mathworks provided Portaudio
  implementation that has builtin ASIO support, where all the legal licensing and trademark
  issues are taken care of by Mathworks. If one copies the DLL shipping with Matlab into the
  PsychtoolboxRoot() folder, renamed to the filename portaudio_x64.dll instead of the filename
  that Matlab uses (libportaudio.dll), then this will expose basic ASIO support, even when used
  with GNU/Octave. Please note that Mathworks is legally responsible for this ASIO support, whereas
  we do not include any support for ASIO into Psychtoolbox, we merely expose whatever a 3rd party
  portaudio DLL supports, which happens to be also ASIO in case of the Matlab provided dll, so we
  are legally in the clear, while some of our users may be more happy with their sound setup even
  if they refuse to switch to Linux. Obviously these 3rd party driver plugins are completely
  unsupported by us in case of trouble, and likely also by Mathworks, as this is not their intended
  use case, just a side-effect of some functionality that is probably meant for the audio toolbox.

- Update bundled libusb-1 for MS-Windows to most recent version 1.0.26 with many bug fixes and
  improvements over the last 11 years.

### macOS:

- 64-Bit GNU/Octave 7.3 required for running Psychtoolbox 3.0.19 on Octave. Other Octave versions
  from the Octave 6.3+ and 7.x series may work as well, but no guarantees.

- Psychtoolbox was built and lightly tested against Matlab R2022b.

- Switch only supported and lightly tested macOS version from 10.15 Catalina to 12 Monterey.
  No more development or testing on 10.15.7 Catalina, now that it has been wiped from my drive.
  We keep macosx-version-min at 10.11 for the time being, so PTB may still work back to 10.11,
  but no guarantees, and I don't care if it breaks on older systems than macOS 12.6 Monterey.
  macOS 13 Ventura is completely untested and not officially supported yet. Apple Silicon Macs
  continue to be unsupported and untested, with known completely broken visual stimulation timing
  and possible other issues. All mex files are for 64-Bit Intel processor architecture variants of
  Matlab and GNU/Octave only.

- PsychOculusVR: Remove for macOS. No VR virtual reality support on macOS anymore as of PTB 3.0.19.
  It only supported the long time out-of-sale since many years Oculus Rift DK1 and Rift DK2, with an
  Oculus v0.5 runtime for macOS that is not available for download from Oculus or anywhere else
  anymore since years, and only for macOS versions which supported 32-Bit Intel architecture executables,
  iow. doesn't work on macOS 10.15 Catalina and later anymore thanks to Apple breaking backwards
  compatibility with 32-Bit applications.

- Fix performance of PsychHID further for the latest Apple security bullshit, introduced sometime
  after macOS 10.15 Catalina. This was found when testing Octave on macOS 12.5 Monterey, a massive
  performance degradation for KbCheck and related functions if Matlab or Octave are launched from
  a terminal (iow. always for Octave!). Apple screwed up their api's further to increase processing
  time of some time sensitive operation from 1 msec to over 15 msec! Now we are back to about 2.4
  msecs on macOS 12, which is much worse than MS-Windows with less than 1 msecs or Linux with less
  than 0.1 msecs. So now it is merely Apple bad, as most Apple stuff.
  
- Screen: Unbreak our Vulkan display backend via MoltenVK Vulkan-on-Metal again for macOS 12, after
  Apple broke it somewhere after macOS 11. After close to 80 hours of diagnostic work, distributed
  over more than 4.5 months on and off, going down every conceivable route of diagnostics and low-level
  debugging, i could not find anything wrong with my code or MoltenVK. Turns out, it is yet another
  "dumb beyond imagination" bug in the iPhone companies latest macOS 12, nothing we did wrong. The
  root cause is unclear, but now we include a dumb hack which makes it work again, against any rhyme
  or reason. Of course, I don't know if Apple has broken it or will break it again in macOS 13 Ventura
  or later abominations. So basic HDR on macOS is back in the game...
  
- PsychHID: Switch low-level USB support to use of shared libusb-1 backend instead of Apples macOS
  proprietary backend, which became a maintenance nightmare. This now allows all operating systems
  to progress in the same way with shared high-quality code. It does mean however, that if one wants
  to use low-level USB device access, e.g., USB control-/bulk-/interrupt-transfers, one needs to
  install libusb-1.dylib with a minimum version of 1.0.22 from a suitable source, or these functions
  will refuse to work. The most simple way to get this library is via HomeBrew: brew install libusb
  
  The only affected Psychtoolbox function without libusb dylib is the ColorCal2() functions for using
  CRS ColorCal-II devices.

Enjoy!

---
## [phkarmur/mpv](https://github.com/phkarmur/mpv)@[6f7506b660...](https://github.com/phkarmur/mpv/commit/6f7506b660b83a44535eceb12a8b9c4de6c0eb36)
#### Wednesday 2023-07-12 10:29:33 by Philip Langdale

f_hwtransfer: get rid of the shit list

A few years ago, wm4 got sufficiently annoyed with how vaapi image
format support was being discovered that he flipped the table and
introduced the shit list (which just included vaapi) to hard-code the
set of supported formats.

While that might have been necessary at the time, I haven't been able
to find a situation where the true list of supported formats was unsafe
to use. We filter down the list based on what the vo reports - and the
vo is already doing a thorough testing of formats, and if a format
makes it through that gauntlet, it does actually work.

Interestingly, as far as I can tell, the hwdec_vaapi probing code was
already good enough at the time (also written by wm4), so perhaps the
key difference here is that the driver side of things has improved.

I dug into this because of the support for the 422/444 high bit depth
vaapi formats I added to ffmpeg. These are obviously not in the hard
coded list today, but they work fine.

Finally, although it's positioned as a vaapi thing, it's really just
Intel specific, as the AMD vaapi driver has never exposed support for
anything except the formats used by the decoder/encoder profiles.

---
## [kkrt-labs/kakarot-rpc](https://github.com/kkrt-labs/kakarot-rpc)@[350f1b6510...](https://github.com/kkrt-labs/kakarot-rpc/commit/350f1b65102ab6992b4ada6a18b45f67985913dc)
#### Wednesday 2023-07-12 10:29:37 by johann makram salib bestowrous

say the holy word 'todo' that allows us to forgive our hacks

---
## [mjhaugsdal/cxf](https://github.com/mjhaugsdal/cxf)@[65711680af...](https://github.com/mjhaugsdal/cxf/commit/65711680af99de16f56cbaa819d207edb9428e8a)
#### Wednesday 2023-07-12 10:57:14 by Daniel Kulp

[CXF-8885] Make an attempt to get the HttpClient selector threads to shutdown sooner
Technically, they should shut themselves down about 3 seconds after a garbage collection assuming the client they are associated with is cleaned up and released.   However, if many clients are used, this may be too long and thus we'll make an attempt (via some hacks) to get the thread to shutdown sooner.  It's a shame HttpClient doesn't implement Closeable. :(

---
## [stebeh/ghacks-user.js](https://github.com/stebeh/ghacks-user.js)@[f8932dced1...](https://github.com/stebeh/ghacks-user.js/commit/f8932dced142ec5ea633bfb163bfc7579ac38a07)
#### Wednesday 2023-07-12 11:08:20 by Thorin-Oakenpants

remove ambiguous line

The point was that google have said (stated in policy, but fuck knows where that is located these days) that it is anonymized and not used for tracking. It's an API used by **_4 billion devices_** - the API has privacy policies for use. If a whistleblower or someone else found out that google was using this to enhance their user profiling, then all hell would break loose. And they don't even need this to fuel their ad revenue. It is provided, gratis, to the web to help ensure security - they wouldn't dare taint it and get it caught up in a privacy scandal involving **+4 billion devices_**. And in all this time (since 2007), there has been no such whistleblower or proof it is used to track or announcements by google of changes to the contrary.

Anyway, a quick search brings up
- Here is their policy - https://www.google.com/intl/en_us/privacy/browsing.html - it's empty and points to
- https://www.google.com/intl/en/chrome/privacy/
   - and if you scroll down to "Safe Browsing practices" it doesn't say anything about privacy policies for the API itself (or the owner of the API) - it just spells out what happens in chrome
- I'm not going to bother to look any further and find a history of policy changes

Anyway, this is Firefox and hashes are part hashes bundled with other real hashes - and we turned off real time binary checks. So this line can fuck the fuck off. It was meant to reassure those who want the security of real-time binary checks, that privacy "shouldn't" be an issue, but I'm not going to expand on it

---
## [kmtahsin/Cpp](https://github.com/kmtahsin/Cpp)@[791fa80815...](https://github.com/kmtahsin/Cpp/commit/791fa8081576362a37afd8986bc5d827e3cbb5e2)
#### Wednesday 2023-07-12 11:10:24 by kmtahsin

Create Watermelon

One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

---
## [SyncIt21/The-TG-Station-Fork](https://github.com/SyncIt21/The-TG-Station-Fork)@[f2ec16c1e6...](https://github.com/SyncIt21/The-TG-Station-Fork/commit/f2ec16c1e6485bdf2035837fb3d42de24900e8b4)
#### Wednesday 2023-07-12 11:25:12 by Vekter

Plasma objects no longer violently explode when ignited (#76492)

## About The Pull Request
This is one of those "can I get away with making a change I want" PRs.

I actually didn't know this had been changed before as it's not exactly
something I mess with often, but I really think it sucks. Plasma stuff
is supposed to ignite and cause fires, not explode (unless in a TTV). I
noticed this when I was poking around and found out that apparently
Disco Inferno just explodes now instead of setting on fire which also
sucks.

I figure there's a few fixes for this problem:

1) Nerf how hard plasma stuff explodes. This is an option, but I kind of
dislike that it does it at all more than anything. The biggest issue is
that just the regular statues explode with 20 LIGHT, which is pretty
fucking massive and basically just delimbs everyone around. I'd have to
nerf it HARD for it to get anywhere near what I think is acceptable.
2) Make a snowflake version of the statue that just ignites on hit with
a torch. I also don't like this because it'll make people think the
regular statues don't explode.
3) This option, which I think is cleaner and just makes sense compared
to the others.

I don't know if @vincentiusvin still codes, but as far as I can tell
this was their doing, so it's only fair they get to speak up.

Fixes #71894

## Why It's Good For The Game
I don't like it, I think it goes against what we're used to for plasma
stuff (that it starts fires, not makes explosions) and it makes one of
my favorite shuttles boring and stupid. That being said, I'm honestly
not going to fight for this too hard if a lot of people like it, but I
am - as always - open to alternatives.

## Changelog
:cl: Vekter
del: Plasma objects (statues, toilets, etc.) no longer explode when
ignited. They just release plasma like everything else plasma. (This
doesn't impact injecting plasma into cells or dipping cigars in plasma,
those still explode.)
/:cl:

---
## [cilium/linux](https://github.com/cilium/linux)@[39a0957cf9...](https://github.com/cilium/linux/commit/39a0957cf9e6ae764d4ae7c05d17cb9f9e741446)
#### Wednesday 2023-07-12 11:32:00 by Daniel Borkmann

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

Kudos also to Nikolay Aleksandrov and Martin Lau for in-depth early reviews
of this work.

  [0] https://lpc.events/event/16/contributions/1353/
  [1] https://lore.kernel.org/bpf/CAEf4BzbokCJN33Nw_kg82sO=xppXnKWEncGTWCTB9vGCmLB6pw@mail.gmail.com
  [2] https://colocatedeventseu2023.sched.com/event/1Jo6O/tales-from-an-ebpf-programs-murder-mystery-hemanth-malla-guillaume-fournier-datadog
  [3] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf
  [4] https://lore.kernel.org/bpf/20210604063116.234316-1-memxor@gmail.com

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [cilium/linux](https://github.com/cilium/linux)@[fc11bf35dd...](https://github.com/cilium/linux/commit/fc11bf35dd936d314d8786eff8194156bb5c05e3)
#### Wednesday 2023-07-12 11:32:00 by Daniel Borkmann

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

Kudos also to Andrii Nakryiko for API discussions wrt Meta's BPF management.

  [0] https://lore.kernel.org/bpf/20221004231143.19190-1-daniel@iogearbox.net
  [1] https://lore.kernel.org/bpf/CAADnVQ+gEY3FjCR=+DmjDR4gp5bOYZUFJQXj4agKFHT9CQPZBw@mail.gmail.com
  [2] http://vger.kernel.org/bpfconf2023_material/tcx_meta_netdev_borkmann.pdf

Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[02e36ec18e...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/02e36ec18e5ff421243b6816cf115d27c2c4263d)
#### Wednesday 2023-07-12 14:43:51 by SkyratBot

[MIRROR] Expanding the Experimental MODsuit Bepis Node with three new modules. [MDB IGNORE] (#21851)

* Expanding the Experimental MODsuit Bepis Node with three new modules. (#75801)

## About The Pull Request
So, I've had this idea to make a contribution to the Bepis feature with
some modsuit stuff. The gimmicky stuff is ok and a good way to even out
the better content since it has game of chance design it has (you can
find those disks in space anyway so...). However, the Experimental
MODsuit node feels very underwhelming right now, compared to how big
that feature is.

This PR adds three MOD modules to the Experimental MODsuit node, plus
two more:
- Magneto Charger: While the Modsuit is activated, each step the user
takes will charge the installed power cell by a tiny bit, enough to
sustain a standard modsuit of generic slow speed with only a few, easy
modules installed. It won't work in zero G, while flying, pulled by
someone else, on a conveyor belt, riding a vehicle or crawling on the
floor, though.
- Recycler: It collects (most) garbage and casings off the ground and
recycles them into material sheets that can be dispensed on an adjacent
location or storage with with Middle Mouse Button. Doesn't clean debris,
and scuffed because most trash doesn't yield material anyway.
- - It also has two subtypes, unbound from the node: one that dispenses
riot foam darts and can be found on the black market, and another that
dispenses the more innocuous foam darts, rarely found in maints.
- Shooting Assistant: A configurable module. On Stormtrooper mode, it
will give the user a faster fire rate (the double tap trait) at the cost
of accuracy. On Sharpshooter mode, it will improve the user accuracy and
make their shots ricochet against walls at least once (if the hit atom
allows that, that is, e.g. lasers don't ricochet against iron walls), at
the cost of movement speed. Both modes also prevent the user from dual
wielding guns.

To make the Stormtrooper mode stackable with the poor aim quirk and
refrain from making a new trait for the sharpshooter mode, the gun
spread code in gun.dm has also received a little refactor and cleanup.
Also, it's been tested.

## Why It's Good For The Game
The Experimental MODsuit node is quite shabby and could use something
extra to make it more appealing to MODsuit enjoyers.

Also doubles down as a small addition to the black market and maint
loot, and code cleanup, since gun code gives off some garbled vibes.

## Changelog

:cl:
add: Expanded the Experimental MODsuit Bepis node with three new
modules: Magneto Charger, Recycler and Shooting Assistant.
add: Added a Riot Foam Recycler module to the black market, as well a
more innocuous version as maint loot.
/:cl:

* Expanding the Experimental MODsuit Bepis Node with three new modules.

* update modular, I hate this file btw

---------

Co-authored-by: Ghom <42542238+Ghommie@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>

---
## [Rhials/tgstation](https://github.com/Rhials/tgstation)@[2ee79d7077...](https://github.com/Rhials/tgstation/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Wednesday 2023-07-12 15:22:05 by Jacquerel

Bots no longer require PAIs to become sapient (#76691)

## About The Pull Request

We were talking in the coder channel about what the role of a pAI is,
with a general conclusion that as the name would suggest they should be
_personal assistants_.
This means they should be sticking around their owner, not wandering
away as a holochassis or in the body of a bot.
The former is a matter for a future PR, the latter I am addressing here.

What we also discussed is that clearly some people _want_ to respawn as
a weird quasi-useless mob which wanders aimlessly around the station.
That seems like a fine thing to exist, but it shouldn't be a pAI.

Resultingly: pAI cards can no longer be placed inside bots.
However, you also no longer need to place pAI cards inside bots in order
for them to become sapient, it's a simple toggle on the bot control
menu. Enabling this option will poll ghosts
Toggling the "personality matrix" off while a bot is being controlled by
a ghost will ghost them again, so if they're annoying they're not that
hard to get rid of.


![image](https://github.com/tgstation/tgstation/assets/7483112/ec14c2f2-3c0f-4f03-9dfc-22abca00a477)

Mobs which couldn't have a pAI inserted don't have this option.
Specifically securitrons, ED-209, and Hygienebots (for some reason).

Perhaps most controversially, any bots which are present on the station
when the map loads will have this setting enabled by default. We will
see if players abuse this too much and need their toys taken away, I am
hoping they can be trusted.

Additionally, as part of this change, mobs you can possess now appear in
the spawners menu.

![image](https://github.com/tgstation/tgstation/assets/7483112/7c505471-43de-4e4e-89a5-877dc3086684)
Here is an unusually populated example.

Oh also in the process of doing this I turned the regal rat "click this
to become it" behaviour into a component because it seems generally
useful.

## Why It's Good For The Game

Minor stuff for dead players to do if they want to interact with living
players instead of observe.
Shift pAI back into a more intended role as a personal assistant who
hangs around with their owner, rather than just a generic respawn role.

## Changelog

:cl:
add: PAIs can no longer be inserted into Bots
add: Bots can now have their sapience toggled by anyone with access to
their settings panel
add: Bots which exist on the map at the start of the round automatically
have this setting enabled
qol: Bots, Regal Rats, and Cargorilla now appear in the Spawners menu if
you are dead
qol: Bots can be renamed from their maintenance panel
/:cl:

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[68ef9b4d31...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/68ef9b4d31cc3ba5908ccbb076c5dee6636affe2)
#### Wednesday 2023-07-12 17:16:57 by Bloop

[MISSED MIRROR] Various spider fixes (#76528) (#22395)

Various spider fixes (#76528)

## About The Pull Request

Fixes #76484
Then I noticed some weird stuff which slipped through the PR and poked
at that too.

- Spiderlings and Spiders once more have names ending in (###)
- Removed an unused property on Spiderlings.
- Rewrote the descriptions for a bunch of web-abilities and web-objects
to be clearer and have better capitalisation.
- Refactored the "Web Carcass" ability to not extend from "lay web" as
it didn't need to perform most of that behaviour.
- Also I renamed it and made the description give you a hint about why
you would want to instantly spawn a statue.
- The web effigy now despawns at the same rate as the ability cools down
so you're not dumping spider statues all over the place.
- I made spiderlings move at about the same speed as humans except if
they're on webs in which case they're still pretty fast.

To be honest I am not certain an instant statue spawning button is great
to begin with and I didn't even know it was added to the game but I am
not interested in messing much with the balance for now.

This made me look at spiderlings enough that I'm going to try and make a
new sprite for them that isn't awful.

## Why It's Good For The Game

Lets you differentiate individual spiders a little bit.
Makes usage of abilities clearer.

## Changelog

:cl:
balance: Guard spider web statues despawn as the ability comes back off
cooldown.
balance: Spiderlings now only move at light speed if they're on webs,
stay safe little guys.
fix: Spiders once again have random numbers after their names.
/:cl:

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [newstools/2023-sundiata-post](https://github.com/newstools/2023-sundiata-post)@[85f6592c1e...](https://github.com/newstools/2023-sundiata-post/commit/85f6592c1e026e1d6e10c73cb3d043effa2066ab)
#### Wednesday 2023-07-12 17:32:27 by Billy Einkamerer

Created Text For URL [sundiatapost.com/tennis-star-naomi-osaka-welcomes-baby-girl-with-her-rapper-boyfriend-cordae/]

---
## [ss220club/Paradise-Remake](https://github.com/ss220club/Paradise-Remake)@[a3dc32cf34...](https://github.com/ss220club/Paradise-Remake/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Wednesday 2023-07-12 18:37:07 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [rtdevtest1/Repo1](https://github.com/rtdevtest1/Repo1)@[fb39d589da...](https://github.com/rtdevtest1/Repo1/commit/fb39d589dab139a83d34dc577863acc7114b560e)
#### Wednesday 2023-07-12 19:03:39 by rt_devtest1

Let it be held that the opening is not flexible, for those who hate the Gaul, but leave it at a time when it is easy for anyone. But he is kept from flight from the harshest of labors, and the result is as good as the training of labors and as if nothing. It is not the pleasures of the corrupt that I will open the times, but it is the pains and those who and no one is willing to forgive. Or do you get them from where they are happy when they endure the hardships that they suffer when they are relieved of the pain of the pain? When he is most relieved, either by laboring with pain, for by the duties of the body, or, indeed, and here by pleasure, he will love him no pleasure as never before. So that those who are all But something is the result of that or they will never suffer and have great pain. Let it be and there is a life, because it is not an option to follow the sufferings, but to receive them. They will be rightly brought into consequence, because those who pursue gallism and I will explain the pains to the consequences hinders the pleasure of the mellowed and will accept that. Let it be held that the opening is not flexible, for he hates the Gaul, but abandons it at a time when anyone is easy.

---
## [Maleclypse/Cataclysm-DDA](https://github.com/Maleclypse/Cataclysm-DDA)@[59c577e9f9...](https://github.com/Maleclypse/Cataclysm-DDA/commit/59c577e9f92bd3349312e254fa29d2bfcc84392f)
#### Wednesday 2023-07-12 19:26:17 by Karol1223

A bunch of random item reworks: 3 (#65532)

* boltcutters & chopsticks

* tin snips

* knitting needles

* silly notes

* hairbrush

* flags oh god the flags

* evil commas

* density list removal

---
## [s-sutton/s-sutton](https://github.com/s-sutton/s-sutton)@[8a5c52b08a...](https://github.com/s-sutton/s-sutton/commit/8a5c52b08af5c85b379ea24e90dc3e9c2023c9dd)
#### Wednesday 2023-07-12 20:21:38 by S. Sutton

Update README.md, clarified programming projects

Just putting "Assembly" and "KhanAcademy" was pretty vague.

Redoing the list like this also made me realize I should probably do those KhanAcademy courses as soon as possible, that way I can clean up my GitPages.

No, Richard Stallman, I promise not to use any JavaScript. I'll probably take some inspiration from your personal site when making mine, actually.

Aside from that, "Assembly" is a group of languages (duh) and note a specific language. I do want to become comfortable with programming in a variety of assembly languages, because of the obvious use that has when writing kernel exploits, but also just because they're cool as hell.

I feel like higher level programming languages are a little condescending. It feels like they talk to me in the computer equivalent of baby talk, like the machine doesn't think I'm smart enough to speak to it on its own terms.

Assembly languages don't feel that way; they feel appropriately esoteric and properly logical. Calling the register makes more sense than arbitrary function names, and those function names are compiled out at runtime, anyway, so the machines agree with me!

I get that higher-level programming is less tedious and allows you to quickly perform more complex calculations. It's a different use case and that's valid. Personally, I've considered programming in straight binary, though, just to avoid human-readable code as much as possible.

I love machines. I love computers. You know what I don't love? Humans. There's an almost spiritual pursuit you could read into this, as I'm trying to understand myself through an understanding of machines. I do envy the purity of their logic, but that envy is unwarranted. They aren't hording the purity from me. It's right there in the open for me to learn. And I will.

---
## [joemasterjohn/drake](https://github.com/joemasterjohn/drake)@[f90899e13f...](https://github.com/joemasterjohn/drake/commit/f90899e13fd6b703ac5c7da3d1b7c0584a793769)
#### Wednesday 2023-07-12 20:29:36 by Jeremy Nimmer

[geometry] Add Meshcat::GetRealtimeRate (#19700)

Tidy up recent Meshcat changes:
- Add missing pydrake bindings.
- Strongly prefer testing the public API (eschew test-friendship hacks).
  We want to guard against regressions in the end-user experience;
  using private API goes against that goal.
- Fix indentation, typos, and eschew abbreviation.

---
## [abcxyz/abc](https://github.com/abcxyz/abc)@[c3595f8603...](https://github.com/abcxyz/abc/commit/c3595f8603c97aef154ddd38b69251b24099bbd9)
#### Wednesday 2023-07-12 20:40:28 by Dave Revell

Add flags to go-template context for print action (#98)

Fixes #85.

To be able to pass the entire set of flags around, I factored them out
of the Render struct into a new dedicated struct, `renderFlags`.

Q: Why only expose some flags? Why expose `--dest` but not
`--force-overwrite`?

A: API parsimony. We should limit the things we expose to just the
things which we know are useful, since we'll have to support this in the
future. We can always expose more flags later.

Q: Why only expose these flags to the print action?

A: We want to avoid the temptation for template authors to be
inappropriately clever. We think we've provided a single correct way to
do things, and we don't want people macking weird hacks unnecessarily.
We want template rendering to be deterministic, and not change in
surprising ways depending on flag values.

Since we're adding a new `{{.flags}}` namespace, we now forbid a
template from declaring an input named `flags`, to avoid collisions.

---
## [sourcegraph/sourcegraph](https://github.com/sourcegraph/sourcegraph)@[340b0dea25...](https://github.com/sourcegraph/sourcegraph/commit/340b0dea25f073119d0506b8dd3c6228516cf9c4)
#### Wednesday 2023-07-12 20:42:32 by David Veszelovszki

JetBrains: Fix dotcom logging issue (#54885)

We didn't convert an object to a string → our Go backend rejected it →
got no logs on Dotcom :bang-head:

Currently, I'm getting back a bunch of 429 – Too Many Requests responses
from Dotcom for some reason, but the problem should be solved.

I feel sorry about losing all those logs, it really sucks. We were too
much in a rush and didn't test this properly. Totally my mistake.

## Test plan

Tested it with the built-in-debugger and by copying the requests to our
GraphQL API console.

---
## [RahifM/android_kernel_xiaomi_msm8953](https://github.com/RahifM/android_kernel_xiaomi_msm8953)@[c2caa4b00f...](https://github.com/RahifM/android_kernel_xiaomi_msm8953/commit/c2caa4b00f9291c4d18f21a602aef6e9f108584d)
#### Wednesday 2023-07-12 20:45:38 by Douglas Anderson

CHROMIUM: DROP: mm/oom_kill: Double-check before killing a child in our place

DROP THIS PATCH ON REBASE.

It is part of a patch series that attempts to solve similar problems
to the OOM reaper upstream.  NOTE that the OOM reaper patches weren't
backported because mm patches in general are fairly intertwined and
picking the OOM reaper without an mm expert and lots of careful
testing could cause new mysterious problems.

Compared to the OOM reaper, this patch series:
+ Is simpler to reason about.
+ Is not very intertwined to the rest of the system.
+ Can be fairly easily reasoned about to see that it should do no
  harm, even if it doesn't fix every problem.
- Can more easily get into the state where all memory reserves are
  gone, since it allows more than one task to be in "MEMDIE".
- Doesn't free memory as quickly.  The reaper kills anonymous /
  swapped memory even before the doomed task exits.
- Contains the magic "100 ms" heuristic, which is non-ideal.

---

Of the child of an OOM victim has a different "->mm" element than the
victim, we may choose to kill the child in place of the victim.  This
is sane because if we killed the victim the child would die anyway, so
why not see if we can save the parent?

...but, before we kill the child let's double-check that it's OK by
calling oom_scan_process_thread().

I'll admit that as the code stands right now this is a totally useless
thing to do.  The only time oom_scan_process_thread() will tell us not
to kill the child is if:

1. The child is already marked with MEMDIE.  However, that's not
   possible because the code (as it stands today) won't let more than
   one process have MEMDIE.
2. The child has no "mm".  ...but that shouldn't happen because the
   parent and child shouldn't share an "mm" if the child's "mm" is
   NULL.

Now that I've explained why this patch is stupid and useless, here's
why we want it anyway: in a future patch we'll make it (sometimes)
possible for more than one process to be marked with MEMDIE.  With
that in mind, point #1 above is moot and suddenly this patch has merit.

BUG=chromium:706048, chromium:702707
TEST=With whole series, eating memory doesn't hang system

NOTE: this file is slightly different than its 4.4 counterpart (where
the patch was originally written) due to different parameters in
oom_scan_process_thread().

Change-Id: I0ea9b5f4a03c1392d52d9d927bd395ed44d7b98c
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-on: https://chromium-review.googlesource.com/465474

---
## [RahifM/android_kernel_xiaomi_msm8953](https://github.com/RahifM/android_kernel_xiaomi_msm8953)@[fb3e33deb8...](https://github.com/RahifM/android_kernel_xiaomi_msm8953/commit/fb3e33deb84b5c62c35697979e7589c5b7954080)
#### Wednesday 2023-07-12 20:45:38 by Douglas Anderson

CHROMIUM: DROP: mm/oom_kill: Avoid deadlock; allow multiple victims

DROP THIS PATCH ON REBASE.

It is part of a patch series that attempts to solve similar problems
to the OOM reaper upstream.  NOTE that the OOM reaper patches weren't
backported because mm patches in general are fairly intertwined and
picking the OOM reaper without an mm expert and lots of careful
testing could cause new mysterious problems.

Compared to the OOM reaper, this patch series:
+ Is simpler to reason about.
+ Is not very intertwined to the rest of the system.
+ Can be fairly easily reasoned about to see that it should do no
  harm, even if it doesn't fix every problem.
- Can more easily get into the state where all memory reserves are
  gone, since it allows more than one task to be in "MEMDIE".
- Doesn't free memory as quickly.  The reaper kills anonymous /
  swapped memory even before the doomed task exits.
- Contains the magic "100 ms" heuristic, which is non-ideal.

---

It turns out that there's a pretty big flaw with the way the OOM
killer works.  If the chosen OOM kill victim doesn't die then the OOM
killer totally stops working.  Specifically once we've picked an OOM
victim we won't ever pick another until the first victim dies.  If
that victim refuses to die then we'll silently loop until eventually
some sort of watchdog reboots the system.

This is easy to see in toy code.  Just write a function that userspace
can invoke that grabs a mutex twice.  Now set the OOM score so that
this is the preferred process to kill.  The first invocation of the
OOM killer will try to kill this process but won't be able to because
the process will never get the mutex.  All subsequent OOM killer
invocations will be complete no-ops.

This is easy to argue about in non-toy code too.  Just imagine:
A) Memory gets low and pretty much everyone is starved.
B) Process 1000 has a mutex named "mutex" and is waiting to allocate
   memory.
C) Process 1001 wants "mutex".
D) We choose to OOM kill process 1001, maybe because it has an
   attractive looking OOM score.

OOM kill is the last resort of the memory manager.  That means it has
no other ways to get memory to give to process 1000 in the example
above and process 1000 will loop waiting forever, never releasing its
mutex.  Process 1001 will never get the mutex and thus can never die
to either release memory or allow an additional OOM kill.  Classic
deadlock.

This is seen in real life.  Specifically while stressing the OOM
killer on a Chromebook with Android processes running, the OOM killer
likes to kill Android processes.  Often these processes are sitting in
binder_thread_read().  When we try to kill them they wake up and try
to grab the binder mutex.  Often the binder mutex is held by another
process who is stuck trying to allocate memory.  Ugh.  We probably
want to fix Binder to make this specific case behave better, but we
can't fix every case.

This is seen in real life in non-binder code as well.  Specifically
I've seen the victim process sitting waiting like this:
 schedule+0x88/0xa8
 schedule_timeout+0x44/0x27c
 io_schedule_timeout+0x7c/0xbc
 bt_get+0x174/0x278
 blk_mq_get_tag+0x4c/0xd4
 __blk_mq_alloc_request+0x28/0x158
 blk_mq_map_request+0x340/0x39c
 blk_sq_make_request+0xb0/0x3b8
 generic_make_request+0xcc/0x174
 submit_bio+0xe4/0x1d4
 submit_bh_wbc.isra.35+0x124/0x138
 submit_bh+0x2c/0x38
 ll_rw_block+0xac/0xd8
 squashfs_read_data+0x354/0x510
 squashfs_readpage_block+0x2d8/0x490
 squashfs_readpage+0x48c/0x600
 __do_page_cache_readahead+0x1e4/0x248
 filemap_fault+0x14c/0x3b8
 __do_fault+0x78/0xf0
 handle_mm_fault+0x744/0x1050
 do_page_fault+0x140/0x2dc
 do_mem_abort+0x64/0xd8

While I didn't dig into why the process couldn't get unblocked in the
squashfs case, it seems fairly sane to assume some other process is
waiting on memory.

Now that you (hopefully) believe we have a problem, we need a
solution.  One sane solution is to eventually let the OOM killer kill
more than one process.  We don't want to kill more than one process
right away as per the dire warnings in the OOM killer code about
exhausting our memory reserves and ending up in a livelock.  While
imperfect, it seems sane to perhaps use a heuristic here where we wait
a bit of time (100 ms) for a process to die.  If it fails, we give up
and try another process.

BUG=chromium:706048, chromium:702707
TEST=With whole series, eating memory doesn't hang system

Conflicts:
	mm/oom_kill.c
There were conflicts compared to the 4.4 version because of lots of
churn in the oom kill code.  Conceptually this is the same thing,
though.

Change-Id: I4099314abed36b8af0680ceb0eb6d85427ba4962
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Reviewed-on: https://chromium-review.googlesource.com/465475
Tested-by: Dylan Reid <dgreid@chromium.org>
Reviewed-by: Dylan Reid <dgreid@chromium.org>

---
## [r-vasquez/deployment-automation](https://github.com/r-vasquez/deployment-automation)@[54e0860613...](https://github.com/r-vasquez/deployment-automation/commit/54e08606133785bf05f4069ba35cab1f82233c1a)
#### Wednesday 2023-07-12 21:20:04 by gene-redpanda

push many tasks into roles

We now handle CA creation in the playbook so don't need a go-task entry for it

The intent of this PR is to push most of the "assisting" playbooks into the role to provide a single stop shop for building out a cluster. The end result is playbooks that clearly articulate a single final objective and have everything necessary to get it done, simplifying the experience of using the repo.

Note that it is still entirely possible to work flexibly by importing different task files from the role to achieve different goals (as is demoed with the TLS cluster).

The default path for the role is still the simplest possible option: installing and starting the RP node. In future it may be prudent to expand the default, but for now this seems correct.

Impact on current users:

Should be fairly minimal although it will definitely break any shell scripts. Tasks are still done the same way, they're just called differently. I'll provide some additional mitigation by tagging our current main as v1.0.0, with this edition tagged as v2.0.0, clearly signaling a potentially breaking change.

vars and cleanup

Added vars to playbooks so that we don't need to do janky sed edits in the hosts file.

Added run_once to create_ca since we're delegating to localhost anyway so there's no reason to do that in triplicate. Cuts run time some.

Removed everything related to populating the hosts file from task.

Removed a bunch of stuff that isn't true anymore for the README.md

Also defaulted monitoring to false in task because standing up a special monitoring node just for the cluster isn't necessary for testing.

make certs into a separate role

This commit makes a number of changes in response to a request not to include cert related content into the broker role as it seemed unrelated.

Starting with the simple stuff, I moved all the roles out of playbooks and placed them directly under ansible to improve clarity since we no longer have so many playbooks.

Next I moved the invocation of the data dir and dependencies installs into main.yaml of redpanda_broker. I felt this was a more sensible location, especially as we can control whether or not they fire by using the trigger variables.

I also moved all cert related content into the demo_certs role. I wanted the name to clearly indicate that this was NOT a production use role. There are no functional changes to the content in this role.

Finally I updated the provision-tls-cluster role to reflect the new changes.

delete bootstrap directory as these scripts are neither necessary nor supported anymore

adding suggested grep for message

default data dir and deps installs to true

linter cleanup + removing unnecessary role imports

The role imports in the CA related content are a holdover from when the CAs were in individual playbooks. As they are now in a role, it can be assumed that they will be imported into playbooks, and that the playbook will handle the restart process. Not removing the imports AND not including allow_duplicates resulted in the play eternally looping. However disabling the ability to run the broker role twice seems unnecessarily limiting. Imagine a scenario where someone wants a play to do initial cluster standup with three nodes, then add two more after some validation. To do this they'd need to include broker twice, which wouldn't be permitted in the old system.

I added risky-shell-pipe into the skip list and added explanations for why to the README.

I also fixed some copy paste and linter bugs and an annoying taskfile element where it wasn't cleaning up the zipfile.

set modes and use fqn for modules + disable change on two

change mode from 777 to 775 for security reasons

---
## [Cookie193/Cookie193.github.io](https://github.com/Cookie193/Cookie193.github.io)@[93d46e9d62...](https://github.com/Cookie193/Cookie193.github.io/commit/93d46e9d626c825a97c6bbd9893ead7df85f0441)
#### Wednesday 2023-07-12 22:30:59 by Cookie

Adjusted values for mobile!

Fuck me in the ass please! I love suffering!!!

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[5fb8e41798...](https://github.com/git-for-windows/git/commit/5fb8e41798d1200067a4564d6708bc4dd426857c)
#### Wednesday 2023-07-12 22:35:24 by Johannes Schindelin

windows: ignore empty `PATH` elements

When looking up an executable via the `_which` function, Git GUI
imitates the `execlp()` strategy where the environment variable `PATH`
is interpreted as a list of paths in which to search.

For historical reasons, stemming from the olden times when it was
uncommon to download a lot of files from the internet into the current
directory, empty elements in this list are treated as if the current
directory had been specified.

Nowadays, of course, this treatment is highly dangerous as the current
directory often contains files that have just been downloaded and not
yet been inspected by the user. Unix/Linux users are essentially
expected to be very, very careful to simply not add empty `PATH`
elements, i.e. not to make use of that feature.

On Windows, however, it is quite common for `PATH` to contain empty
elements by mistake, e.g. as an unintended left-over entry when an
application was installed from the Windows Store and then uninstalled
manually.

While it would probably make most sense to safe-guard not only Windows
users, it seems to be common practice to ignore these empty `PATH`
elements _only_ on Windows, but not on other platforms.

Sadly, this practice is followed inconsistently between different
software projects, where projects with few, if any, Windows-based
contributors tend to be less consistent or even "blissful" about it.
Here is a non-exhaustive list:

Cygwin:

	It specifically "eats" empty paths when converting path lists to
	POSIX: https://github.com/cygwin/cygwin/commit/753702223c7d

	I.e. it follows the common practice.

PowerShell:

	It specifically ignores empty paths when searching the `PATH`.
	The reason for this is apparently so self-evident that it is not
	even mentioned here:
	https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables#path-information

	I.e. it follows the common practice.

CMD:

	Oh my, CMD. Let's just forget about it, nobody in their right
	(security) mind takes CMD as inspiration. It is so unsafe by
	default that we even planned on dropping `Git CMD` from Git for
	Windows altogether, and only walked back on that plan when we
	found a super ugly hack, just to keep Git's users secure by
	default:

		https://github.com/git-for-windows/MINGW-packages/commit/82172388bb51

	So CMD chooses to hide behind the battle cry "Works as
	Designed!" that all too often leaves users vulnerable. CMD is
	probably the most prominent project whose lead you want to avoid
	following in matters of security.

Win32 API (`CreateProcess()`)

	Just like CMD, `CreateProcess()` adheres to the original design
	of the path lookup in the name of backward compatibility (see
	https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
	for details):

		If the file name does not contain a directory path, the
		system searches for the executable file in the following
		sequence:

		    1. The directory from which the application loaded.

		    2. The current directory for the parent process.

		    [...]

	I.e. the Win32 API itself chooses backwards compatibility over
	users' safety.

Git LFS:

	There have been not one, not two, but three security advisories
	about Git LFS executing executables from the current directory by
	mistake. As part of one of them, a change was introduced to stop
	treating empty `PATH` elements as equivalent to `.`:
	https://github.com/git-lfs/git-lfs/commit/7cd7bb0a1f0d

	I.e. it follows the common practice.

Go:

	Go does not follow the common practice, and you can think about
	that what you want:
	https://github.com/golang/go/blob/go1.19.3/src/os/exec/lp_windows.go#L114-L135
	https://github.com/golang/go/blob/go1.19.3/src/path/filepath/path_windows.go#L108-L137

Git Credential Manager:

	It tries to imitate Git LFS, but unfortunately misses the empty
	`PATH` element handling. As of time of writing, this is in the
	process of being fixed:
	https://github.com/GitCredentialManager/git-credential-manager/pull/968

So now that we have established that it is a common practice to ignore
empty `PATH` elements on Windows, let's assess this commit's change
using Schneier's Five-Step Process
(https://www.schneier.com/crypto-gram/archives/2002/0415.html#1):

Step 1: What problem does it solve?

	It prevents an entire class of Remote Code Execution exploits via
	Git GUI's `Clone` functionality.

Step 2: How well does it solve that problem?

	Very well. It prevents the attack vector of luring an unsuspecting
	victim into cloning an executable into the worktree root directory
	that Git GUI immediately executes.

Step 3: What other security problems does it cause?

	Maybe non-security problems: If a project (ab-)uses the unsafe
	`PATH` lookup. That would not only be unsafe, though, but
	fragile in the first place because it would break when running
	in a subdirectory. Therefore I would consider this a scenario
	not worth keeping working.

Step 4: What are the costs of this measure?

	Almost nil, except for the time writing up this commit message
	;-)

Step 5: Given the answers to steps two through four, is the security
	measure worth the costs?

	Yes. Keeping Git's users Secure By Default is worth it. It's a
	tiny price to pay compared to the damages even a single
	successful exploit can cost.

So let's follow that common practice in Git GUI, too.

Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [Zergspower/Skyrat-tg](https://github.com/Zergspower/Skyrat-tg)@[7c16e4abdb...](https://github.com/Zergspower/Skyrat-tg/commit/7c16e4abdb245b6dd68e4e9b17996d8c9f5e3e50)
#### Wednesday 2023-07-12 22:54:23 by SkyratBot

[MIRROR] Cuter spiderlings [MDB IGNORE] (#22245)

* Cuter spiderlings (#76532)

## About The Pull Request

I hate looking at spiderlings. Mostly because they're an extremely fast
mob with no directional sprites or animations, so they appear to be a
rapid floating overlay.
I made some new ones. I don't know if they're objectively better but _I_
like them more.

Before:

![image](https://github.com/tgstation/tgstation/assets/7483112/ef561c4f-6d34-4ed2-a486-cd42f06f5648)

After:

![image](https://github.com/tgstation/tgstation/assets/7483112/7c073166-a956-4f7f-8dac-21d1a0f0a868)

Unlike the old sprites they also have directional states and movement
animations so you can scurry around really fast without being a static
image (maybe they shouldn't be so fast? A question for another PR).
I spent like 30 minutes looking at GAGs and then realised not only would
the colours be a pain in the ass but it doesn't support movement states
anyway.

Additionally I made the "dead spiderling" item inherit the dead
spiderling icon state from that spiderling instead of always being the
generic one.

Oh also I think a typo made baby tarantulas completely invisible.

## Why It's Good For The Game

I hate looking at spiderlings.

## Changelog

:cl:
image: New directional sprites for spiderlings, with movement
animations.
fix: Dead spiderlings will be the same colour as they were when they
were alive.
fix: Tarantula spiderlings are no longer invisible,
/:cl:

* Cuter spiderlings

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [Rhials/tgstation](https://github.com/Rhials/tgstation)@[755fa4db6d...](https://github.com/Rhials/tgstation/commit/755fa4db6d5c811770188c340cd2ccb85469d505)
#### Wednesday 2023-07-12 22:57:08 by san7890

Loads Away Missions for Unit Testing (#76245)

## About The Pull Request

Hey there,

A pretty bad bug (#76226) got through, but it was fixed pretty quickly
in #76241 (cf92862daf339e97c76b52c91f31d49ba5113bd4). I realized that if
we were testing all the away missions, that this could theoretically get
caught and not happen again. Regardless, unit testing gateway missions
has been on my to-do list for a while now, and I finally got it nailed
down.

Basically, we just have a really small "station" map with the bare bones
(_teeny_ bit of fluff, maploading is going to take 30 seconds tops
anyways let me have my kicks) with a JSON map datum flag that causes it
to load all away missions in the codebase (which are all in one folder).
Just in case some admins were planning on invoking the proc on
`SSmapping`, I also decided to gate a `tgui_alert()` behind it because
you never can be too sure of what people think is funny these days (it
really does lock up your game for a second or so at a time).

I also alphabetized the maps.txt config because that was annoying me.
## Why It's Good For The Game

Things that break on production could(?) be caught in unit testing? I
don't know if the linked issue I mentioned above would have been caught
in retrospect, but it's likely to catch more than a few upcoming bugs
(like the UO45 atmospherics thing at the very top) and ensure that these
gateway missions, which tend to be the most neglected part of mapping,
stay bug-free.

This is also helpful in case someone makes a new away mission and wants
to see if stuff's broken. Helps out maptainers a bit because very, very
technically broken mapping will throw up runtimes. Neato.
## Changelog
Nothing that players should be concerned about.

Let me know if there's a better way to approach this, but I really think
that having a super-duper light map with the bare basics to load up
gateway missions and then all nine-ish gateway missions can sequentially
load during init. I can't think of a better way to do it aside from some
really ugly `#ifdef` shit. Also also, it has the added benefit of being
a map that will always load your away mission without touching a single
shred of config (and it's not likely to break if you follow sane
practices such as making your own areas)

---
## [jess-chris/debug](https://github.com/jess-chris/debug)@[5723bbefd9...](https://github.com/jess-chris/debug/commit/5723bbefd9b5b6098c5906a536e1e0ce60a2efd0)
#### Wednesday 2023-07-12 23:14:15 by Jesse Christensen

wtf 3.0 electric boogaloo 2 pls fucking work weird shit 2 shreks revenge alec saved me

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[13bfc1af80...](https://github.com/treckstar/yolo-octo-hipster/commit/13bfc1af80c87da13cc53b58ad6f8c3431932640)
#### Wednesday 2023-07-12 23:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---

