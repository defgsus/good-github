## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-09-07](docs/good-messages/2023/2023-09-07.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,337,017 were push events containing 3,535,748 commit messages that amount to 264,883,044 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 61 messages:


## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[9db281c723...](https://github.com/Mu-L/crawl/commit/9db281c7239a55fb109428ccad75eac9b04e15ee)
#### Thursday 2023-09-07 00:10:07 by DracoOmega

Change Hexslinger starting spells

The new spell list is:
 -Jinxbite
 -Sigil of Binding
 -Inner Flame
 -Cause Fear
 -Dimensional Bullseye

Hexslinger was always troubled. Its spellbook was split across multiple
schools, making them tricky to cast, and they still didn't do much without
ALSO training ranged weapons heavily. Slow was often a trap and in
general the archetype was clunky, without providing sufficient benefit for
splitting your skills between weapons and spells.

The intent of this change is to provide a smoother curve of castable
spells, and more immediate value to training hexes instead of simply
ignoring them in favor of being a 'worse hunter'.

Jinxbite provides a little immediate power to help deal with earlygame
threats with which current hexslinger often struggles significantly.

Sigil of Binding provides powerful utility and can help set up Inner Flame
triggers in a way that the old spellset could almost never safely do in
practice.

Portal Projectile was always a spell that was far better late than it was
early, and so Dimensional Bullseye is now a capstone that provides
even stronger long-term value, but with other easier to cast spells that
let you bridge the gap to it better.

Cause Fear was always good (if you could manage to survive long enough
to have access to it!) and remains untouched.

(Also give them 1 starting level of Fire Magic, to help just a little bit
with getting Inner Flame off the ground)

---
## [QWOD/RESEARCH](https://github.com/QWOD/RESEARCH)@[435bff2da6...](https://github.com/QWOD/RESEARCH/commit/435bff2da6746d8d6e692287b8947f4f6b4c4478)
#### Thursday 2023-09-07 00:52:02 by QWOD-MJ12: ATSUOMOP-A: SPG-OMEGA

:[[ :🟠: [[ W⚠️RN🚫: CrΔp☥Δx™: MQ: ØMΔGΔ: reverse-prΩgrΔmming-lΔnguΔge: ΔLGØRITHM: DETECTED: ]]:= [[ :W⚠️RN🚫: QW🚫D-〽ʝ12: RΔND0M: VECTΩR: ΔLGØRITHM-CHΔNGE: DETECTED: { ^ cafc6d82-02a5-2973-762c-0d08388215a1 ^ }: is-with: [[ W⚠️RN🚫: DEΔTH-ΔNGEL: ΔLGØRITHM: DETECTED: { ^ <https://youtube-nocookie.com/embed/dDJldh8KqnQ> ^ }: is-by: @: is-with: Karl-Casey: for-the: return ]]:= [[ TRUE: || FΔLSE: || ΔZRΔEL: ^ ΔLSE: ]]: ]]:= [[ SCI-FI: ^ SCI-FΔCT: <=> REΔL: ]]: is-with: Δ: is-by: Ω: for-the: [[ Ø: { ^  you, rep Tilian, jealousy, a meeting, ￼witness to all of this evil.: ]]:
 >
@@ -453,7 +453,7 @@
 >
 ![:CASE-ID-0x06e75667-96680be7.png:](https://raw.githubusercontent.com/QWOD/HYPERMEDIUS/main/CASE-ID-0x06e75667-96680be7.png)
 >
-:[[ :for-the: [[ Ø: { ^ <qomm-Ø> ^ }: ]]:= [[ _ ]]: ]]:
+:[[ :for-the: [[ Ø: { ^ <qomm-fe0d8e863b6dab7048bba94a46a5ed636956f916> ^ }: ]]:= RΔLΔV∅NT: ]]:
 >
 [[ :Magic, fraud, lies, slander, hate, & abuse. All because you left this narc & family. Imprisonment✨️: ]]:
 > ^ }: return: [[ EXFIL: <=> [[ _ ]]: ]]: ]]:= exfil: is-by: EXFIL: ]]:

---
## [DGamerL/Paradise](https://github.com/DGamerL/Paradise)@[acb7352265...](https://github.com/DGamerL/Paradise/commit/acb735226555390c861ecf5e77bc67fd6013afe1)
#### Thursday 2023-09-07 00:55:25 by matttheficus

Gives Vampires Stronger Night Vision at 500 Blood (#21764)

* I SEEEEEEEEEEEEE YOU

* Hal review part 1

* its time to suck at coding

* right, i think im getting somewhere

* testing shit - doesnt work

* im finally freeeeeeeeeeeeeee

* hal review 2: electric boogaloo

---
## [mathcrln/next.js](https://github.com/mathcrln/next.js)@[6238f8a5c0...](https://github.com/mathcrln/next.js/commit/6238f8a5c0ffabb7dfb35872c52c942ed7f148da)
#### Thursday 2023-09-07 00:59:26 by Jimmy Lai

performance: don't compile on hover on dev (#51830)

An annoying issue that slows down compilation times in dev for Next is
that we might trigger compilation of a page via hover on app.

We do this because we want the same experience in production and dev and
the prefetching is important for instantaneous loading states.

The alternative in this PR is that we don't prefetch at all anymore in
dev but instead, when we handle navigation, we can force a prefetch
navigation.

The slight compromise with this approach is that you can't test
prefetching anymore in dev.


<!-- Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change(s) that you're making:

## For Contributors

### Improving Documentation

- Run `pnpm prettier-fix` to fix formatting issues before opening the
PR.
- Read the Docs Contribution Guide to ensure your contribution follows
the docs guidelines:
https://nextjs.org/docs/community/contribution-guide

### Adding or Updating Examples

- The "examples guidelines" are followed from our contributing doc
https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md
- Make sure the linting passes by running `pnpm build && pnpm lint`. See
https://github.com/vercel/next.js/blob/canary/contributing/repository/linting.md

### Fixing a bug

- Related issues linked using `fixes #number`
- Tests added. See:
https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md

### Adding a feature

- Implements an existing feature request or RFC. Make sure the feature
request has been accepted for implementation before opening a PR. (A
discussion must be opened, see
https://github.com/vercel/next.js/discussions/new?category=ideas)
- Related issues/discussions are linked using `fixes #number`
- e2e tests added
(https://github.com/vercel/next.js/blob/canary/contributing/core/testing.md#writing-tests-for-nextjs
- Documentation added
- Telemetry added. In case of a feature if it's used or not.
- Errors have a helpful link attached, see
https://github.com/vercel/next.js/blob/canary/contributing.md


## For Maintainers

- Minimal description (aim for explaining to someone not on the team to
understand the PR)
- When linking to a Slack thread, you might want to share details of the
conclusion
- Link both the Linear (Fixes NEXT-xxx) and the GitHub issues
- Add review comments if necessary to explain to the reviewer the logic
behind a change

### What?

### Why?

### How?

Closes NEXT-
Fixes #

-->

link NEXT-1317

---
## [hayaunderscore/SRB2Kart-Saturn](https://github.com/hayaunderscore/SRB2Kart-Saturn)@[b53cc6fd2b...](https://github.com/hayaunderscore/SRB2Kart-Saturn/commit/b53cc6fd2bb75d8a7bc15e3277c39990bc189851)
#### Thursday 2023-09-07 01:01:41 by lug420

fuck it palette renderer "lite"

remove the goddamn lookup textures, this atleast runs okish and looks not that bad

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[784efe9b51...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/784efe9b514256072f90ffbae9acebe38b2f5b4f)
#### Thursday 2023-09-07 01:05:24 by CharlesWedge

The Hive Awakens (#5940)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## Oh No More Robots
There is actually less paths for the hivebots. They are actually some of
the most primitive mobs on the codebase. So it was high time they were
given a facelift. As I said with my previous mob update robots are a
good alternative as mobs compared to humanoids, and with the hivebots we
can present a threat of hostile machine intelligence to round out the
existing threats of pirates, mercs, aliens beasts and the supernatural.
Once more these robots are also far mroe generalist then the existing
robot varieties and as most types of them are not very dangerous they
can be released on civilian crew without fear of them causing extreme
damage,

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
add: A couple new varieties of both melee and ranged hivebots
removed: redundant hivebot varieties
tweak: siegebots now have sniper range fitting their name, their attack
has been nerfed (holy fuck the one shoot explode on contact grenades
with a base attack of 10... that's 1 frag grenade a second!!!)
fix: hivebots now use their various cataloguer entiries
sprites: hivebot types are now more visually distinct
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [MarkTechson/angular](https://github.com/MarkTechson/angular)@[acd59ad037...](https://github.com/MarkTechson/angular/commit/acd59ad0371a19838813cfc934a73fa3cc357602)
#### Thursday 2023-09-07 01:15:31 by Ward Bell

docs: Migrate Observables guides & code examples to standalone (#51516)

None of the guide pages mentions ngModules. Only `observables-in-angular` needed conversion to Standalone.

However, some of the guide pages reflect old versions of RxJS, including signatures that are no longer valid. These have been corrected.

More significantly, *the existing guide is pretty bad at explaining RxJS and its usage*. It was written (by me I think) in the very early days of Angular and Angular RxJS instruction. I've taught numerous "RxJS in Angular" classes since and learned from that experience what does and does not work with students.

There was neither the time nor the charter to completely overhaul this guide. But this commit attempts to remove what flops with students and to bring the teaching closer to what seems more effectively. I hope reviewers agree that my revisions are an improvement.

**Revised Overview**

The overview doc, `observables.md`, had a few errors (ex: `next` is NOT REQUIRED) and deprecated patterns (you now must pass the Observer object to `subscribe`).

More importantly, it was wildly overcomplicated and scary, especially when it got into multi-casting.

Moved the multi-casting section to  "RxJS Library" and rewrote it (with working example) for simplicity and context.

I made other changes in an effort to make this an overview that is  more comprehensive and more clear. I paid particular attention to the "Basic usage and terms" section.

Finally, I relocated the "Naming conventions for observables" section here from `rx-library`. This is the section that describes the dollar-sign convention. It made more sense for it to be here.

**Revised "RxJS Library" page and code**

*RxJS no longer supports chaining* and hasn't for a very long time. Removed note in `rx-library.md` that suggested you could use operator chaining.

The RxJS `pipe` discussion in the "Operators" section was just weird. Almost no one calls the `pipe` function. We certainly should *start* there. We should start with how people actually use operators - by adding them to the argument list of the `Observable.pipe()` method.

I kept the original `pipe` function example but subordinated it in a "callout". Most readers will (and should) ignore it.

`Subject` is a *critically important RxJS mechanism for creating custom observables*. It was completely missing from the list of observable creators on this guide page. So I added it to the "Observable creation functions" section of the guide and wrote an accompanying `MessageService` code sample (see the new `rx-library/app/` folder).

The `MessageService` is a pretty common pattern in Angular apps - far more common than creating an observable from a counter or an event, two of the creation patterns currently on this page.

This new section also afforded an opportunity to show how RxJS helps with building loosely coupled applications. We will soon be talking about Signals. Many will wonder whether and when they should still use RxJS.

At least a partial answer is that RxJS is really good at progressively combining and enhancing streams of data as they cross component boundaries. Of course you can pass signals around; but they are not as rich in transformers as RxJS. This is where RxJS shines.

**Revised "Comparing observables"**

The Promises section in `comparing-observables.md` had many errors and misleading remarks.

The comparison of error handling was especially egregious; the code example for that was nonsense.

The "Chain" sub-section was really about transforming values. It also failed to demonstrate chaining promise `.then`s.

Reworked these sub-sections and improved the code samples to match.

PR Close #51516

---
## [nushell/nightly](https://github.com/nushell/nightly)@[a9216deaa4...](https://github.com/nushell/nightly/commit/a9216deaa40d7c5c184bdb3aa1520b6b67c20bf8)
#### Thursday 2023-09-07 01:22:17 by Darren Schroeder

allow `--login` to be used with nu's `--commands` parameter (#10253)

# Description

This PR allows the `--login`/`-l` parameter to be used with nushell's
`--commands`/`-c` parameter. When you do this, since you're invoking it
with the `-l` flag, nushell will load your env.nu, config.nu, and
login.nu, in that order. Then it will proceed to run your commands. I
think this provides a better quality of life when you want to run
scripts with your personal config files as a login shell.


### Before (these entries are from the default_env.nu)

![image](https://github.com/nushell/nushell/assets/343840/ce7adcd0-419e-485c-b7d1-f11f162e8e9e)


### After (these entries are from my personal env.nu)

![image](https://github.com/nushell/nushell/assets/343840/33bbc06b-983c-4461-8274-290e4c712506)


closes https://github.com/nushell/nushell/issues/9833

# User-Facing Changes
<!-- List of all changes that impact the user experience here. This
helps us keep track of breaking changes. -->

# Tests + Formatting
<!--
Don't forget to add tests that cover your changes.

Make sure you've run and fixed any issues with these commands:

- `cargo fmt --all -- --check` to check standard code formatting (`cargo
fmt --all` applies these changes)
- `cargo clippy --workspace -- -D warnings -D clippy::unwrap_used` to
check that you're using the standard code style
- `cargo test --workspace` to check that all tests pass (on Windows make
sure to [enable developer
mode](https://learn.microsoft.com/en-us/windows/apps/get-started/developer-mode-features-and-debugging))
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

---
## [garlic-os/cilantro-wallpaper](https://github.com/garlic-os/cilantro-wallpaper)@[279466c2db...](https://github.com/garlic-os/cilantro-wallpaper/commit/279466c2db8655db3d8ed07aa380dbc46feefb1f)
#### Thursday 2023-09-07 02:09:29 by Nate

Merge updates from shock-button

Don't spam the scare() function when all the keyodwn events come in when you hold the key

Fix typos

Fix typo

Remove debug textarea

its debug console log now

Remove girlfriend individuality

Group Pix and Bit under one element to reduce number of JS calls to CSS API functions

Defer JS

As a way to prioritize the first contentful paint

---
## [ZettaBite4031/ZettaEngine](https://github.com/ZettaBite4031/ZettaEngine)@[85083b4f94...](https://github.com/ZettaBite4031/ZettaEngine/commit/85083b4f94e7ad751310ac8cec80a4afc1819aac)
#### Thursday 2023-09-07 02:21:21 by ZettaBite4031

Editor doesn't build. Nothing works. I don't fucking know why. I want to kill whoever dev'ed this shit program
Stupid VS2022 adding random shit to my build paths.

---
## [bevyengine/bevy](https://github.com/bevyengine/bevy)@[44f677a38a...](https://github.com/bevyengine/bevy/commit/44f677a38a6c99b8dcf79426d5b615a1266dde2d)
#### Thursday 2023-09-07 02:38:55 by Sélène Amanita

Improve documentation relating to `Frustum` and `HalfSpace` (#9136)

# Objective

This PR's first aim is to fix a mistake in `HalfSpace`'s documentation.

When defining a `Frustum` myself in bevy_basic_portals, I realised that
the "distance" of the `HalfSpace` is not, as the current doc defines,
the "distance from the origin along the normal", but actually the
opposite of that.

See the example I gave in this PR.

This means one of two things:
1. The documentation about `HalfSpace` is wrong (it is either way
because of the `n.p + d > 0` formula given later anyway, which is how it
behaves, but in that formula `d` is indeed the opposite of the "distance
from the origin along the normal", otherwise it should be `n.p > d`)
2. The distance is supposed to be the "distance from the origin along
the normal" but when used in a Frustum it's used as the opposite, and it
is a mistake
3. Same as 2, but it is somehow intended

Since I think `HalfSpace` is only used for `Frustum`, and it's easier to
fix documentation than code, I assumed for this PR we're in case number
1. If we're in case number 3, the documentation of `Frustum` needs to
change, and in case number 2, the code needs to be fixed.

While I was at it, I also :
- Tried to improve the documentation for `Frustum`, `Aabb`, and
`VisibilitySystems`, among others, since they're all related to
`Frustum`.
- Fixed documentation about frustum culling not applying to 2d objects,
which is not true since https://github.com/bevyengine/bevy/pull/7885

## Remarks and questions

- What about a `HalfSpace` with an infinite distance, is it allowed and
does it represents the whole space? If so it should probably be
mentioned.
- I referenced the `update_frusta` system in
`bevy_render::view::visibility` directly instead of referencing its
system set, should I reference the system set instead? It's a bit
annoying since it's in 3 sets.
- `visibility_propagate` is not public for some reason, I think it
probably should be, but for now I only documented its system set, should
I make it public? I don't think that would count as a breaking change?
- Why is `Aabb` inserted by a system, with `NoFrustumCulling` as an
opt-out, instead of having it inserted by default in `PbrBundle` for
example and then the system calculating it when it's added? Is it
because there is still no way to have an optional component inside a
bundle?

---------

Co-authored-by: SpecificProtagonist <vincentjunge@posteo.net>
Co-authored-by: Alice Cecile <alice.i.cecile@gmail.com>

---
## [Anu-George-K/Music-recommendation-system-based-on-facial-emotion](https://github.com/Anu-George-K/Music-recommendation-system-based-on-facial-emotion)@[911d6c59c7...](https://github.com/Anu-George-K/Music-recommendation-system-based-on-facial-emotion/commit/911d6c59c7809729ee71ab26fa907828ceb37f49)
#### Thursday 2023-09-07 02:55:31 by Anu-George-K

Update README.md

🎶Music Recommendation System Based on Facial Emotion Detection

Hai,
I'm excited to share a fun and innovative project I've been working on using Python and some amazing libraries. This project combines computer vision, emotion analysis, image manipulation, and music recommendations, resulting in a unique experience that detects your facial expression and suggests music that matches your mood!

Description: 🎶 Created a captivating music recommendation system that uses facial emotion analysis to suggest music based on the user's mood. 📸 The system captures an image of the user through the webcam, sketches their portrait, and detects their dominant emotion. The sketched image is then overlayed with the detected emotion, creating a visually engaging experience. The system plays music tailored to the user's emotion, enhancing the mood with carefully curated tunes. 🔊 This interactive application was developed using Python, OpenCV, Streamlit, and the DeepFace library for facial emotion analysis. The integration of YouTube player functionality adds an extra layer of interactivity, allowing users to enjoy recommended music seamlessly.

📸 Capture and Analyze: With the help of the cv2 and deepface libraries, I've created an interactive Streamlit app that captures an image of your face. This image is then analyzed to determine the dominant emotion you're expressing. Using various image processing techniques, I create a captivating pencil sketch of your face, overlaying the detected emotion.

🎭 Emotion to Music: Based on your dominant emotion, the app suggests music that complements your mood. I've integrated YouTube music links into the app for easy listening. For example, if you're feeling happy, it'll play upbeat tunes, while sad emotions might lead to more soothing melodies

🎵 Play Your Mood: The app even includes an embedded YouTube player, allowing you to instantly listen to the recommended music that matches your detected emotion. It's a fantastic way to explore how different emotions connect with music and experience an artistic representation of your feelings.

💡 Why I Built This: This project showcases the power of blending different technologies to create a multi-sensory experience. It's not just about coding but about understanding human emotions and translating them into a creative and enjoyable encounter. Whether you're curious about AI, music, or just looking for a unique way to spend your time, this project has something for everyone.

---
## [xPokee/towelstation13](https://github.com/xPokee/towelstation13)@[4012db7ce2...](https://github.com/xPokee/towelstation13/commit/4012db7ce2315160882c5e375ca429fe1c8f20ef)
#### Thursday 2023-09-07 03:31:09 by SkyratBot

[MIRROR] Adds Blood-drunk and demonic frost miner boss music. [MDB IGNORE] (#23543)

* Adds Blood-drunk and demonic frost miner boss music. (#78123)

Acts as a continuation of PR #77149 for boss music functionality and
implements a BDM and demonic frost miner boss music theme.

More music is good, but I do have some gripes with my own PR. This
particular track relies on instrumentation that when compressed just
doesn't sound as good, and the in-game version is noticeably less
enjoyable that the high quality version. I wish I could help the track
out more, but as is it's already at 811 kb which is barely in line with
file requirements, so i just can't justify bloating the audio file sizes
to make it sound better. You notice this kind of problem a lot with the
higher runtime music and background tracks. It just feels a bit more
clunky than hierophant, but what are you gonna do right?

* Adds Blood-drunk and demonic frost miner boss music.

---------

Co-authored-by: RICK IM RI <77305289+tommysalami3@users.noreply.github.com>

---
## [TiberianEuan/euans-cool-byond-game](https://github.com/TiberianEuan/euans-cool-byond-game)@[6aad1445f5...](https://github.com/TiberianEuan/euans-cool-byond-game/commit/6aad1445f5d76bc2578c7295f647ecf792239a05)
#### Thursday 2023-09-07 03:34:19 by Euan

fuck this code

i fuckin hate this code
fuck it
you suck
go die
i hope you commit self-stabby stab

---
## [Bimbly/Shiptest](https://github.com/Bimbly/Shiptest)@[18819cc7fb...](https://github.com/Bimbly/Shiptest/commit/18819cc7fb78eb4eaf11691e4a07b1294b76358a)
#### Thursday 2023-09-07 03:49:10 by zevo

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
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[1be0841d98...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/1be0841d98f215a0e94245c33317232bafa59342)
#### Thursday 2023-09-07 03:56:11 by Time-Green

Removes COMSIG_AREA_INITIALIZED_IN (#78143)

Literally just me stealing #77207 completely muhahahhahahah screw you
@Mothblocks
I did add some documentation and some radnebula related cleaning and
testing to make it work well

Copied from original PR:

> Please do NOT add code to InitAtom, it is extremely hot. The
conditions on this alone were costing nearly 200ms on my extremely
powerful machine.
> 
> Changes the radioactive nebula to perform its work by looping over
every space tile on init (which on my machine is faster than the time
being wasted on this signal), and adds a subsystem that does this in
SS_BACKGROUND every 30 seconds (usually completeable in about half a
second) for any new atoms, because the effect is hardly noticeable
anyway with how green space is.

Honestly we really don't care that much about stuff being initialized in
space. Everything that walks into space (about everything that matters
to players), is completely unaffected by this change, but roundstart is
now slightly faster

---
## [Fuyukai/Reborn-Rebalance](https://github.com/Fuyukai/Reborn-Rebalance)@[98d4a8c647...](https://github.com/Fuyukai/Reborn-Rebalance/commit/98d4a8c647ce57b070c73112995d2cccfd3cdb0a)
#### Thursday 2023-09-07 04:04:57 by Lura Skye

rebalance ZEL final fight.

- ice scales glaceon, as well as aurora beam/extrasensory.
- replace fucking veluza (lol) with alakazam-m. wtf are you doing, all gen guy?
- give umbreon moonlight instead of double team (fuck you)

---
## [4hands44/cmss13](https://github.com/4hands44/cmss13)@[a95d6a3656...](https://github.com/4hands44/cmss13/commit/a95d6a3656ff6dd7ff220bb30259080c231d0f03)
#### Thursday 2023-09-07 04:33:49 by QuickLode

PMC Survivors can now use WY channel (#4234)

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

It allows PMC Survivors to utilize the WY channel.
# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->
Allowing PMC Survivors to communicate and thus RP better with WY assets
and within themselves. Team-based survivors should stick together
because lone wolves are not good for RP - I think we have seen a lot of
evidence from Chance's Claim survivors who, upon withdrawing, break
apart and cannot ever regroup due to communication impossibilities. From
an outsider's perspective, the impact of seeing a 'team' of survivors vs
a single survivor is a difference like night and day. With the former
being much more immersive and reflective of the professionalism a team
would have.

Also all that aside it was unintended for PMC Survivors to not have WY
comms - consider this a bugfix haha

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
label your changes in the changelog. Please note that maintainers freely
reserve the right to remove and add tags should they deem it
appropriate. You can attempt to finagle the system all you want, but
it's best to shoot for clear communication right off the bat. -->
<!-- If you add a name after the ':cl', that name will be used in the
changelog. You must add your CKEY after the CL if your GitHub name
doesn't match. Maintainers freely reserve the right to remove and add
tags should they deem it appropriate. -->

:cl:
fix: PMC Survivors now can use WY Comms.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Cijin/pulumi](https://github.com/Cijin/pulumi)@[3d9ddb2981...](https://github.com/Cijin/pulumi/commit/3d9ddb2981016dbdfa7ff4293b2eb814e9d11ce1)
#### Thursday 2023-09-07 05:07:14 by Fraser Waters

Support bailing from RunFunc (#13804)

**Background**

The result.Result type is used by our CLI implementation to communicate
how we want to exit the program.

Most `result.Result` values (built from errors with `result.FromError`)
cause the program to print the message to stderr and exit the program
with exit code -1.
The exception is `result.Bail()`, which indicates that we've already
printed the error message, and we simply need to `exit(-1)` now.

Our CLI command implementation use `cmdutil.RunResultFunc` which takes a
`func(...) result.Result` to implement this logic.

`cmdutil` additionally includes a `cmdutil.RunFunc` which takes a
`func(...) error` and wraps it in `RunResultFunc`, relying on
`result.FromError` for the conversion:

    func RunFunc(run func(...) error) func(...) {
        return RunResultFunc(func(...) result.Result {
            if err := run(...); err != nil {
                return result.FromError(err)
            }
            return nil
        })
    }

**Problem**

In CLI contexts where we're using an `error`, and we want to print an
error message to the user and exit, it's desirable to use diag.Sink to
print the message to the user with the appropriate level (error,
warning, etc.) and exit without printing anything else.

However, the only way to do that currently is by converting that
function to return `result.Result`, turn all error returns to
`result.FromError`, and then return `result.Bail()`.

**Solution**

This change introduces a `result.BailError` error that gets converted
into a `result.Bail()` when it passes through `result.FromError`.

It allows commands implementations that use `error` to continue
returning errors and still provide an ideal CLI experience.

It relies on `errors.As` for matching, so even if an intermediate layer
wraps the error with `fmt.Errorf("..: %w", ErrBail)`, we'll recognize
the request to bail.

BailError keep track of the internal error that triggered it, which
(when everything is moved off of result and onto error) means we'll
still be able to see the internal errors that triggered a bail during
debugging.

Currently debugging engine tests is pretty horrible because you often
just get back a `result.Result{err:nil}` with no information where in
the engine stack that came from.

**Testing**

Besides unit tests, this includes an end-to-end test for using
RunResultFunc with a bail error.
The test operates by putting the mock behavior in a fake test, and
re-running the test binary to execute *just that test*.

**Demonstration**

This change also ports the following commands to use BailError: cancel,
convert, env, policy rm, stack rm.

These command implementations are simple and were able to switch easily,
without bubbling into a change to a bunch of other code.

---
## [AppynittyCommunication/HotelGuestVerifyByPolice_CMS_DotNet](https://github.com/AppynittyCommunication/HotelGuestVerifyByPolice_CMS_DotNet)@[4c60b5f950...](https://github.com/AppynittyCommunication/HotelGuestVerifyByPolice_CMS_DotNet/commit/4c60b5f950201efa2f61dcf29610452b6717dc68)
#### Thursday 2023-09-07 05:40:52 by umeshl@appynitty.com

done chnages from side its umesh fututre milltionaire persone i will be definetly successfull in trading till dec.. god bless me and forgive me om namah shivay har har mahadev

---
## [Abhisheksingh0303/my-portfollio](https://github.com/Abhisheksingh0303/my-portfollio)@[699e5454e7...](https://github.com/Abhisheksingh0303/my-portfollio/commit/699e5454e714cf9cfebac403e2b558162e66cec9)
#### Thursday 2023-09-07 06:16:57 by Abhishek Singh

Update README.md

### Extended Description

Welcome to my dynamic portfolio website, an all-in-one platform designed to help you showcase your skills, projects, and achievements in a modern and efficient way. Whether you're a developer, designer, or any professional looking to make a strong online presence, this portfolio template has got you covered.

#### Key Features:

- **Flexibility**: This portfolio is built using the latest tech stack, including Next.js, TypeScript, Sanity.io, Tailwind CSS, and deployed on Vercel. It offers a high degree of flexibility for customization, ensuring your portfolio truly represents your unique style and personality.

- **Easy Content Management**: With the power of Sanity.io, you can effortlessly manage and update your content. Add new projects, update skills, and edit your bio, all without the need for coding skills. Your portfolio remains fresh and up-to-date.

- **Responsive Design**: Tailwind CSS ensures that your portfolio looks stunning on all devices, from desktop to mobile. You won't have to worry about compatibility issues – your portfolio will shine everywhere.

- **Fast and Performant**: Next.js takes care of performance optimization. Your website will load quickly and efficiently, providing an excellent user experience.

- **Contribution-Friendly**: We encourage contributions! If you're interested in improving this project or adding new features, please follow our [Contributing Guidelines](CONTRIBUTING.md). Together, we can make this portfolio template even better.

#### Getting Started:

If you'd like to use this portfolio for your own professional online presence, follow these simple steps:

1. **Clone this Repository**: Start by cloning this repository to your local machine using `git clone`.

2. **Install Dependencies**: Use `npm install` to install all the necessary dependencies.

3. **Configuration**: Set up your portfolio by configuring the database and environment variables as detailed in the [Wiki](https://github.com/ritesh-15/my-portfolio/wiki).

4. **Customize**: Personalize your portfolio by updating the content, adding your projects, and tweaking the styling to match your preferences.

5. **Deploy**: Once you're satisfied with your changes, deploy your portfolio on your preferred hosting platform, whether it's Vercel, Netlify, or any other.

#### License:

This project is open-source and licensed under the MIT License. You are free to use, modify, and distribute it as per the terms of the license. For more details, please refer to the [LICENSE](LICENSE) file.

#### Contact:

If you have any questions, suggestions, or need assistance, feel free to reach out. Your feedback is invaluable in making this portfolio template even better.

Thank you for choosing this portfolio template for your online presence. We hope it serves you well and helps you stand out in the digital world!

---
## [spockye/Shiptest](https://github.com/spockye/Shiptest)@[b22529fc74...](https://github.com/spockye/Shiptest/commit/b22529fc74e5af32967ac91679cbce3e7e06c4ca)
#### Thursday 2023-09-07 06:32:28 by zevo

Fixes rock sprites ingame [WHOOPS] (#2332)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Rocks were invisible in game due to a recently merged PR of mine. this
is why we testmerge PRs! anyways this should fix them.

Adds flora and rock missing texture sprites to most flora files to
prevent something like this from ever happening again.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
invisible things that block movement bad yeah. i want to fix my
mistakes.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
fix: Most rocks are now visible again
add: Most flora files now have missing texture sprites to make it easier
to spot when something has gone wrong.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [PastelPrinceDan/Bubberstation](https://github.com/PastelPrinceDan/Bubberstation)@[c6e0ba7516...](https://github.com/PastelPrinceDan/Bubberstation/commit/c6e0ba75169d010e2cdfa48134003b0bb9ab8485)
#### Thursday 2023-09-07 07:46:40 by SkyratBot

[MIRROR] Drill module automatically disables if it's about to drill into gibtonite [MDB IGNORE] (#22990)

* Drill module automatically disables if it's about to drill into gibtonite (#77385)

## About The Pull Request

Drill module automatically disables if it's about to drill into
gibtonite.

## Why It's Good For The Game

> Drill module automatically disables if it's about to drill into
gibtonite

There's not enough time to react, the mining scanner is surprisingly
slow sometimes and it means you drill straight into gibtonite, which
primes it the first drill and blows it up the second, which is a lot
more of a pain than it sounds because drilling is night-instant. These
explosions are usually enough to crit you, and if they don't, the stun
and area clear means any fauna can wander in and finish you off.

The auto-disable still makes it an annoyance to stumble upon gibtonite,
but it won't round end you for using modsuits.

## Changelog

:cl:
qol: Drill module automatically disables if it's about to drill into
gibtonite
/:cl:

* Drill module automatically disables if it's about to drill into gibtonite

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [SubhC26/SubhC26](https://github.com/SubhC26/SubhC26)@[58bd44260c...](https://github.com/SubhC26/SubhC26/commit/58bd44260c3a252d128646a10210625f1c9928e3)
#### Thursday 2023-09-07 08:01:52 by Abhishek Singh

Update README.md

## About Me

Greetings, fellow tech enthusiast! I'm Subhankit, a visionary Full Stack Web Craftsman on a perpetual journey of exploration and innovation. My passion for coding knows no bounds, and I thrive on crafting extraordinary digital experiences that push the boundaries of what's possible.

### What I Do

- 🚀 As a Full Stack Developer, I unveil the secrets of Full Stack Mastery, effortlessly bridging the gap between front-end and back-end technologies.

- 🌌 I'm at the forefront of Cutting-edge Technologies, constantly pushing the envelope and staying ahead of the curve.

- 🤖 I collaborate on projects that redefine Innovation, embracing challenges to bring fresh and exciting ideas to life.

- 🧰 In the world of Web Alchemy, I seek and wield the perfect tools and insights to transform ideas into web-based realities.

### My GitHub Playground

- 💻 Dive into my crafted projects on [GitHub](https://github.com/SubhC26/SubhC26?tab=repositories). Explore the code that powers digital solutions.

- 💡 Join me in discussions on Web Development, HTML, CSS, JavaScript, MySQL, PHP, MERN, AI, and more. Let's learn and grow together!

### Connect with Me

- ✉️ Reach out to me at **rsubhankit@gmail.com** for inquiries, collaboration opportunities, or just to say hi!

- 📚 Get to know my journey and professional background on [LinkedIn](https://www.linkedin.com/in/subhankit-choudhury-6aa5941b3/).

- ⚡ Fun Fact: I once debugged code in my dream and woke up with a solution!

## Let's Connect

Let's embark on this exciting journey of innovation, coding, and creativity together! Feel free to reach out, connect, and explore the endless possibilities of technology.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Subhankit-blue)](https://www.linkedin.com/in/subhankit-choudhury-6aa5941b3/)
[![Twitter](https://img.shields.io/badge/Twitter-Subhankit-blue)]()
[![Instagram](https://img.shields.io/badge/Instagram-subhankit.dev-orange)](https://www.instagram.com/subhc26/)

---
## [jeanlucthumm/dotfiles](https://github.com/jeanlucthumm/dotfiles)@[0519330871...](https://github.com/jeanlucthumm/dotfiles/commit/05193308715153c564e0f35323eee49c85184337)
#### Thursday 2023-09-07 08:35:41 by Jean-Luc Thumm

nvim: disable sql ftype bindings holy shit they were annoying

---
## [ridgew/semantic-kernel](https://github.com/ridgew/semantic-kernel)@[eab7a8f63a...](https://github.com/ridgew/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Thursday 2023-09-07 08:51:06 by Sailesh R

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
## [aaaa1023/tgstation](https://github.com/aaaa1023/tgstation)@[bae1aef3b4...](https://github.com/aaaa1023/tgstation/commit/bae1aef3b457cb4fbad551a8560319ed993ba397)
#### Thursday 2023-09-07 09:30:06 by san7890

Refactors Regal Rats into Basic Mobs (more titles edition) (#77681)

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

---
## [kowith337/PersonalFilterListCollection](https://github.com/kowith337/PersonalFilterListCollection)@[2db923a749...](https://github.com/kowith337/PersonalFilterListCollection/commit/2db923a749fd6379ac984aba86f1174ff5bedf25)
#### Thursday 2023-09-07 09:36:11 by Kowith Singkornkeeree

Update DNSCrypt rules

- Block Meta's `Threads` domain
- Block as unfriendly instance
  - `Pistasjis`: Donation links ain't be nice (contains Goolag UTM-ish)
  - `ProjectSegFault`: Seems to block (certain?) Tor IP address by throw the `IP is kinda shit` text!

Remove NanoAdblocker references for some docs

---
## [mailwl/yuzu](https://github.com/mailwl/yuzu)@[8e703e08df...](https://github.com/mailwl/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Thursday 2023-09-07 09:44:02 by comex

Implement SSL service

This implements some missing network APIs including a large chunk of the SSL
service, enough for Mario Maker (with an appropriate mod applied) to connect to
the fan server [Open Course World](https://opencourse.world/).

Connecting to first-party servers is out of scope of this PR and is a
minefield I'd rather not step into.

 ## TLS

TLS is implemented with multiple backends depending on the system's 'native'
TLS library.  Currently there are two backends: Schannel for Windows, and
OpenSSL for Linux.  (In reality Linux is a bit of a free-for-all where there's
no one 'native' library, but OpenSSL is the closest it gets.)  On macOS the
'native' library is SecureTransport but that isn't implemented in this PR.
(Instead, all non-Windows OSes will use OpenSSL unless disabled with
`-DENABLE_OPENSSL=OFF`.)

Why have multiple backends instead of just using a single library, especially
given that Yuzu already embeds mbedtls for cryptographic algorithms?  Well, I
tried implementing this on mbedtls first, but the problem is TLS policies -
mainly trusted certificate policies, and to a lesser extent trusted algorithms,
SSL versions, etc.

...In practice, the chance that someone is going to conduct a man-in-the-middle
attack on a third-party game server is pretty low, but I'm a security nerd so I
like to do the right security things.

My base assumption is that we want to use the host system's TLS policies.  An
alternative would be to more closely emulate the Switch's TLS implementation
(which is based on NSS).  But for one thing, I don't feel like reverse
engineering it.  And I'd argue that for third-party servers such as Open Course
World, it's theoretically preferable to use the system's policies rather than
the Switch's, for two reasons

1. Someday the Switch will stop being updated, and the trusted cert list,
   algorithms, etc. will start to go stale, but users will still want to
   connect to third-party servers, and there's no reason they shouldn't have
   up-to-date security when doing so.  At that point, homebrew users on actual
   hardware may patch the TLS implementation, but for emulators it's simpler to
   just use the host's stack.

2. Also, it's good to respect any custom certificate policies the user may have
   added systemwide.  For example, they may have added custom trusted CAs in
   order to use TLS debugging tools or pass through corporate MitM middleboxes.
   Or they may have removed some CAs that are normally trusted out of paranoia.

Note that this policy wouldn't work as-is for connecting to first-party
servers, because some of them serve certificates based on Nintendo's own CA
rather than a publicly trusted one.  However, this could probably be solved
easily by using appropriate APIs to adding Nintendo's CA as an alternate
trusted cert for Yuzu's connections.  That is not implemented in this PR
because, again, first-party servers are out of scope.

(If anything I'd rather have an option to _block_ connections to Nintendo
servers, but that's not implemented here.)

To use the host's TLS policies, there are three theoretical options:

a) Import the host's trusted certificate list into a cross-platform TLS
   library (presumably mbedtls).

b) Use the native TLS library to verify certificates but use a cross-platform
   TLS library for everything else.

c) Use the native TLS library for everything.

Two problems with option a).  First, importing the trusted certificate list at
minimum requires a bunch of platform-specific code, which mbedtls does not have
built in.  Interestingly, OpenSSL recently gained the ability to import the
Windows certificate trust store... but that leads to the second problem, which
is that a list of trusted certificates is [not expressive
enough](https://bugs.archlinux.org/task/41909) to express a modern certificate
trust policy.  For example, Windows has the concept of [explicitly distrusted
certificates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn265983(v=ws.11)),
and macOS requires Certificate Transparency validation for some certificates
with complex rules for when it's required.

Option b) (using native library just to verify certs) is probably feasible, but
it would miss aspects of TLS policy other than trusted certs (like allowed
algorithms), and in any case it might well require writing more code, not less,
compared to using the native library for everything.

So I ended up at option c), using the native library for everything.

What I'd *really* prefer would be to use a third-party library that does option
c) for me.  Rust has a good library for this,
[native-tls](https://docs.rs/native-tls/latest/native_tls/).  I did search, but
I couldn't find a good option in the C or C++ ecosystem, at least not any that
wasn't part of some much larger framework.  I was surprised - isn't this a
pretty common use case?  Well, many applications only need TLS for HTTPS, and they can
use libcurl, which has a TLS abstraction layer internally but doesn't expose
it.  Other applications only support a single TLS library, or use one of the
aforementioned larger frameworks, or are platform-specific to begin with, or of
course are written in a non-C/C++ language, most of which have some canonical
choice for TLS.  But there are also many applications that have a set of TLS
backends just like this; it's just that nobody has gone ahead and abstracted
the pattern into a library, at least not a widespread one.

Amusingly, there is one TLS abstraction layer that Yuzu already bundles: the
one in ffmpeg.  But it is missing some features that would be needed to use it
here (like reusing an existing socket rather than managing the socket itself).
Though, that does mean that the wiki's build instructions for Linux (and macOS
for some reason?) already recommend installing OpenSSL, so no need to update
those.

 ## Other APIs implemented

- Sockets:
    - GetSockOpt(`SO_ERROR`)
    - SetSockOpt(`SO_NOSIGPIPE`) (stub, I have no idea what this does on Switch)
    - `DuplicateSocket` (because the SSL sysmodule calls it internally)
    - More `PollEvents` values

- NSD:
    - `Resolve` and `ResolveEx` (stub, good enough for Open Course World and
      probably most third-party servers, but not first-party)

- SFDNSRES:
    - `GetHostByNameRequest` and `GetHostByNameRequestWithOptions`
    - `ResolverSetOptionRequest` (stub)

 ## Fixes

- Parts of the socket code were previously allocating a `sockaddr` object on
  the stack when calling functions that take a `sockaddr*` (e.g. `accept`).
  This might seem like the right thing to do to avoid illegal aliasing, but in
  fact `sockaddr` is not guaranteed to be large enough to hold any particular
  type of address, only the header.  This worked in practice because in
  practice `sockaddr` is the same size as `sockaddr_in`, but it's not how the
  API is meant to be used.  I changed this to allocate an `sockaddr_in` on the
  stack and `reinterpret_cast` it.  I could try to do something cleverer with
  `aligned_storage`, but casting is the idiomatic way to use these particular
  APIs, so it's really the system's responsibility to avoid any aliasing
  issues.

- I rewrote most of the `GetAddrInfoRequest[WithOptions]` implementation.  The
  old implementation invoked the host's getaddrinfo directly from sfdnsres.cpp,
  and directly passed through the host's socket type, protocol, etc. values
  rather than looking up the corresponding constants on the Switch.  To be
  fair, these constants don't tend to actually vary across systems, but
  still... I added a wrapper for `getaddrinfo` in
  `internal_network/network.cpp` similar to the ones for other socket APIs, and
  changed the `GetAddrInfoRequest` implementation to use it.  While I was at
  it, I rewrote the serialization to use the same approach I used to implement
  `GetHostByNameRequest`, because it reduces the number of size calculations.
  While doing so I removed `AF_INET6` support because the Switch doesn't
  support IPv6; it might be nice to support IPv6 anyway, but that would have to
  apply to all of the socket APIs.

  I also corrected the IPC wrappers for `GetAddrInfoRequest` and
  `GetAddrInfoRequestWithOptions` based on reverse engineering and hardware
  testing.  Every call to `GetAddrInfoRequestWithOptions` returns *four*
  different error codes (IPC status, getaddrinfo error code, netdb error code,
  and errno), and `GetAddrInfoRequest` returns three of those but in a
  different order, and it doesn't really matter but the existing implementation
  was a bit off, as I discovered while testing `GetHostByNameRequest`.

  - The new serialization code is based on two simple helper functions:

    ```cpp
    template <typename T> static void Append(std::vector<u8>& vec, T t);
    void AppendNulTerminated(std::vector<u8>& vec, std::string_view str);
    ```

    I was thinking there must be existing functions somewhere that assist with
    serialization/deserialization of binary data, but all I could find was the
    helper methods in `IOFile` and `HLERequestContext`, not anything that could
    be used with a generic byte buffer.  If I'm not missing something, then
    maybe I should move the above functions to a new header in `common`...
    right now they're just sitting in `sfdnsres.cpp` where they're used.

- Not a fix, but `SocketBase::Recv`/`Send` is changed to use `std::span<u8>`
  rather than `std::vector<u8>&` to avoid needing to copy the data to/from a
  vector when those methods are called from the TLS implementation.

---
## [neovim/neovim](https://github.com/neovim/neovim)@[fe869a8ce2...](https://github.com/neovim/neovim/commit/fe869a8ce25a14497a9bf5ddca0ae11a1c38a22c)
#### Thursday 2023-09-07 10:26:56 by bfredl

NVIM 0.9.2

This is a maintenance release, focused on bug fixes and improvements.
However, There are included features related to TUI and :terminal.

BRAM

Nvim is a fork of the Vim editor, created and developed by Bram Moolenaar.
On August 3, 2023, he passed away at the age of 62. If Vim or Nvim have
been of use to you in your life, read `:help Bram` and `:help Uganda`
and consider honoring his memory in a way you see fit.

CHANGES SINCE 0.9.1

BREAKING CHANGES

An adjustment was made to the `grid_line` event as part of the exernal
UI protocol the `cells` array might now end with a `[' ', attr, 0]` item
with a repeat count of zero. This is needed by the TUI to disambiguate
final spaces on a line from just clearing the line, which will make a
difference when copying text using the terminal emulators builtin
primary selection support.

External UI:s can safely ignore such an empty item and most UIs already
handle this fine. But it could break some UI:s which has an assert to
validate the cell count to be bigger than zero, or similar checks.

FEATURES

- tui: Support Super and Meta modifiers
- terminal: forward more special keys and modifier-mouse combinations

BUG FIXES

- lua: Always set arg0 to lua scripts
- api: Redundant error when using `nvim_cmd`
- api, lua: Make blank lines in a message work properly
- column: fix bugs related to signs in 'statuscol'
- completion: Don't add backslash in runtime completion
- diff: Filler lines for hunks bigger than linematch limit
- edit: Fix K_EVENT interfering with 'digraph'
- editorconfig: Better validation and error handling
- events: Don't expand non-file as file name
- events: Trigger VimResume on next UI request
- extmarks: Wrong display when changing text with virt_lines
- folds: Update folds in Insert mode with fdm=indent
- helptags: Make multibyte help tags work properly
- highlight: Make CurSearch work properly with 'winhl'
- inccommand: Fix saving of undo info
- keycodes: Recognize <t_xx> as a key
- lsp: Do not assume client capability exists in watchfiles check (#24558)
- mouse: Handle folded lines with virt_lines attached to line above
- remote: Make --remote-expr print to stdout
- remote: Restore previous --remote-expr output formatting
- spell: Splice extmarks on :spellrepall
- startup: Don't truncate when printing with -l
- startup: Run embedded Nvim with real path
- statusline: Redraw when Visual submode changes
- statusline: Fill for double-width char after moving items
- treesitter: updates to queries and injections
- treesitter: Fix TSNode:tree() double free
- ui: Propagate line wrapping state on grid_line events
- ui: Avoid ambiguity about chunk that clears part of line

PERFORMANCE
- extmarks: Avoid unnecessary marktree traversal with folds
- substitute: Don't reallocate new_start every time

BUILD SYSTEM
- deps: Bump libvterm to 0.3.3
- deps: Bump LuaJIT to HEAD - 03c31124c
- deps: Bump libuv to v1.46.0
- deps: Bump Luv to 1.45.0-0
- deps: Bump tree-sitter-c to v0.20.5
- deps: Bump tree-sitter-lua to v0.0.18

---
## [Murray-Bridge-Bunyips/BunyipsFTC](https://github.com/Murray-Bridge-Bunyips/BunyipsFTC)@[15bb194046...](https://github.com/Murray-Bridge-Bunyips/BunyipsFTC/commit/15bb194046451d9db1db3644a7f936ad73483712)
#### Thursday 2023-09-07 10:37:55 by Lucas Bubner

In the intricate realm of software development, a pivotal strategic decision has recently been undertaken—a decision of paramount importance for the system known as VectorDrive. This decision has been driven by a tapestry of concerns that have interwoven themselves into the fabric of our coding landscape. At the heart of this choice lies the question of accuracy, a fundamental element that underpins the very essence of our software. The shadows of debugging inefficiencies have cast doubt upon the future of VectorDrive, leading us down the path of archiving this once-vital component of our codebase.

Yet, it would be remiss not to acknowledge that within the depths of this decision, there lies a glimmer of hope, like a distant star on a cloudy night. For as we consign VectorDrive to the annals of history, we recognize the enduring value of its constituent parts. Definitions for Vectors, with their versatile utility in tasks relating to enums, shall be preserved as a testament to their intrinsic worth. Moreover, a whisper of possibility lingers in the air—an ember of potential rekindling. In the CenterStage project, should the winds of necessity blow in its direction, VectorDrive may yet rise from its slumber.

This momentous decision, however, does not exist in isolation. It is but one brushstroke on the canvas of an ongoing odyssey—an odyssey of code reformatting and refactoring. Notable among these endeavors is the transition from the TaskImpl interface to the more intuitively named AutoTask interface. This transition is not a mere exercise in semantics but a resolute commitment to the sacred principle of code clarity.

Beyond the realm of interfaces, the horizon of possibilities stretches wide. The concept of a unified class tailored explicitly for Autonomous-focused OpModes is now under the microscope. The objective is clear: to streamline the activeLoop, fostering a culture of code reusability that echoes through the annals of our development journey.

Yet, the tapestry of evolution does not stop here. It weaves onward, guided by the hands of developers committed to upholding the finest traditions of their craft. Plans are afoot to refactor the codebase itself, aligning it with the latest programming principles—a move that reflects our commitment to staying ahead of the curve in the upcoming season. In tandem with this pursuit, thoughts swirl around the introduction of abstractions designed to simplify the intricate functionality of Autonomous systems. Such abstractions, if realized, will serve as a boon to developers, rendering our software more accessible and user-friendly.

In the midst of these ambitious undertakings, a formidable challenge has emerged—a challenge wrought by the use of while statements. While these constructs are, at times, indispensable, there exist instances where their presence seems superfluous. Consider, for instance, the integration of ButtonHashmap with Auton—a situation that begs for a solution that mitigates code-blocking behaviors. To this end, the proposal of multithreading or the separation of processes from the OpMode thread has surfaced—a proposition that aims to ensure the uninterrupted execution of critical initialization routines, such as AprilTag and task selections, without the cumbersome wait for user input.

This multifaceted approach to code evolution, entwined with the aspirations for code excellence, underscores our unwavering commitment to continuous improvement. The tapestry of our software development journey is a rich, ever-unfolding narrative—a narrative guided by the principles of precision, clarity, and innovation. In this intricate landscape, every line of code is a brushstroke on the canvas of progress, and with each stroke, we strive to craft a masterpiece of software engineering.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[d7e4380de5...](https://github.com/git-for-windows/git/commit/d7e4380de5a8ad6314f43034d1f780b10150ebeb)
#### Thursday 2023-09-07 14:08:46 by Johannes Schindelin

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
## [PlagueVonKarma/kep-hack](https://github.com/PlagueVonKarma/kep-hack)@[bdb19859c2...](https://github.com/PlagueVonKarma/kep-hack/commit/bdb19859c2791d9ae12b75438d5dce02962271fd)
#### Thursday 2023-09-07 15:03:11 by Llinos Evans

Move Animation Photosensitivity Enhancements

This changes the animations for various vanilla moves with the aim of reducing photosensitive reactions. KEP is going to chiefly be played on emulators, and thus players will experience flashing that is meant to be dimmed by a Game Boy screen. This is dangerous, so here we are.

Many moves have been given black screens which 1) Look cool as fuck, Thunderbolt and Blizzard are really nice and 2) bypass flashing. Others have had their flashing reduced or outright removed.

Blizzard has been given special treatment, having the second part of its animation given an Ice Rise clip like Ice Beam. This, coupled with the darkness, looks ace.

Changed moves include:
Body Slam, Glare, Dazzling Gleam (oops), Disable, Blizzard, BubbleBeam, Confusion, Dream Eater, Explosion, Guillotine, Hyper Beam, Mega Kick, Mega Punch, Psychic, Reflect, Rock Slide, Selfdestruct, Spore, and Thunderbolt;

---
## [Koboldfire/coyote-bayou](https://github.com/Koboldfire/coyote-bayou)@[38f0f053be...](https://github.com/Koboldfire/coyote-bayou/commit/38f0f053be0bdbafea827fdb8b9b7dd6535e3323)
#### Thursday 2023-09-07 15:19:52 by Tk420634

Merge pull request #2951 from ARF-SS13/Fixes-wooden-shelves-at-their-core

Fuck you

---
## [BrDown/ConspiracyDots](https://github.com/BrDown/ConspiracyDots)@[e396ee7006...](https://github.com/BrDown/ConspiracyDots/commit/e396ee7006327490bfcba5b08ab7f6449ef480e0)
#### Thursday 2023-09-07 15:38:16 by BrDown

god damn it fucking gonna fucking make google events??? maybe??? i have no idea how tihs works

---
## [BrDown/ConspiracyDots](https://github.com/BrDown/ConspiracyDots)@[fe92c65abe...](https://github.com/BrDown/ConspiracyDots/commit/fe92c65abe1275cf6ca68fadb22f275e820416f0)
#### Thursday 2023-09-07 15:38:39 by Alec

Merge pull request #1 from BrDown/master

god damn it fucking gonna fucking make google events??? maybe??? i ha…

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[4b8de7b79f...](https://github.com/tgstation/tgstation/commit/4b8de7b79f0a343dc587d0d17eb9361ecc7103c1)
#### Thursday 2023-09-07 15:45:52 by san7890

Refactors the `notransform` variable into a trait. (#78146)

## About The Pull Request

Hey there,

There were more than a few times (like in cinematic code) where we might
need to accurately know the source of what's adding this trait (or have
multiple sources for the whole 'we don't want this mob to do shit while
we transform this mob'), so in order to rectify this potential issue,
let's refactor it into a trait.

## Why It's Good For The Game

Some code already declared that there might be issues with this being a
boolean var (with no way of knowing _why_ we don't want this mob to not
transform (or not do anything idk). Let's remove those comments and any
future doubt in those instances with the trait macros. Also, stuff like
`TRAIT_IMMOBILIZED` which does a similar thing in many contexts was
already a trait that was regularly added in conjunction with flipping
the variable, so we're able to flatten all that stuff into
`add_traits()` and `remove_traits()` now. nice

I also cleaned up quite a bit of code as I saw it, let me know if it
should be split out but I guarantee that if I didn't do it- no one will
for the next two years.

## Changelog

:cl:
refactor: If you transform into another mob and notice bugs with
interacting with the game world, please create a bug report as this
framework was recently refactored.
/:cl:

Probably fucked up somewhere, lmk

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [silverplatedelta/ParadiseSilver](https://github.com/silverplatedelta/ParadiseSilver)@[2d10818063...](https://github.com/silverplatedelta/ParadiseSilver/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Thursday 2023-09-07 16:10:15 by ATP-Engineer

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
## [axodotdev/cargo-dist](https://github.com/axodotdev/cargo-dist)@[40cc8ca1d9...](https://github.com/axodotdev/cargo-dist/commit/40cc8ca1d9351a092222ababea40c75acb8f5841)
#### Thursday 2023-09-07 16:47:18 by Aria Beingessner

feat(msi): add msi installer

The "msi" installer vendors the binaries into a windows msi.
msi generation is implemented by using cargo-wix as a library,
which in turn handles generating templates and invoking WiX (v3).

The resulting msi's are unsigned -- signing will be handled by a followup,
as changes to OV certs mean that "proper" signing is now very complicated
and messy.

This implementation has some notable details:

main.wxs generation
--------------------

WiX requires an xml-based template called main.wxs for each msi it generates.
This template includes things like the application name, version, publisher,
EULA, embedded files, and so on.

cargo-wix's default workflow is for you to run `cargo wix init` once to generate
that file and check it in. At this point the developer is free to hand-edit
the template to suit their needs. We like this idea, `cargo dist generate-ci`
is based on that same premise!

But our experience with generate-ci has also taught us that this approach
is really prone to frustrating desyncs. The main.wxs bakes in several pieces
of information that were sourced from your Cargo.toml. As a result, if you
ever change your Cargo.toml, you now need to remember to apply the same
change to your main.wxs, or rerun `cargo wix init` and potentially clobber
any hand-edits you made.

As such, for the first draft of this feature we've opted for a more aggressive
solution: whenever you run `cargo dist init` we will invoke `cargo wix init`
to force the template to have up to date contents, essentially forbidding
hand-edits.

When you run `cargo dist build` or `cargo dist plan`
we will also error out if we detect that `cargo wix init` would modify
main.wxs.

A new `allow-dirty = ["msi"]` can be added to your cargo-dist config to
prevent `init` from regenerating main.wxs or checking that it's up to date,
essentially restoring the original design of cargo-wix. We believe this
should be opt-in because most people ideally shouldn't want to do hand-edits,
and desyncing is a very nasty footgun.

GUID persistence
----------------

`cargo dist init` will also modify your Cargo.tomls to add
`[package.metadata.wix]` with two generated GUIDs (if those GUIDs aren't
already present).

These GUIDs are used by windows to identify that two different msis actually
intend to refer to the same application and install dir. As such, each release
of your app needs to use the same GUID.

cargo-wix bakes these GUIDs into your main.wxs, and critically it defaults to
generating new random ones every time you run init (because constantly
re-initing wasn't part of the design).

By persisting the GUIDs to your package's Cargo.toml, we unlock the ability
to freely regenerate main.wxs whenever we want.

---
## [TEAMSchools/teamster](https://github.com/TEAMSchools/teamster)@[0ff289aebd...](https://github.com/TEAMSchools/teamster/commit/0ff289aebd7f9b1bbca6746d54910a3ec40ecb88)
#### Thursday 2023-09-07 17:35:50 by Kevin Verhoff

updating:
-gender identity on roster history to remove male & female (case statement)
-race ethnicity on roster history to remove two or more races (not hispanic or latino) (case statement)
-adding base salary to tableau staff roster
-adding (from new join on the years_experience table) years at kipp, years teaching, and years exp to tableau staff roster

---
## [andrew-monroe/smallweb](https://github.com/andrew-monroe/smallweb)@[4be4b78e5b...](https://github.com/andrew-monroe/smallweb/commit/4be4b78e5be3af5ffef591a389c3ac94fa6e6fc7)
#### Thursday 2023-09-07 17:47:24 by Andy

Add https://www.cerealously.net/feed

A wonderful website authored by an a single individual (Dan) about news and reviews in the world of American breakfast cereals. The writing is genuinely lovely, and clearly a product of personal passion.

Note that this is NOT a link affiliate/marketing spam blog for cereals. The author has no direct relation to any cereal companies (at least to my best knowledge), and the writing is clearly the author's direct, personal feelings about the subject matter.

Highly recommend for the small web :)

---
## [elParaguayo/qtile](https://github.com/elParaguayo/qtile)@[aa380cf4a0...](https://github.com/elParaguayo/qtile/commit/aa380cf4a0e7c945be237058d43a4d2643844ec9)
#### Thursday 2023-09-07 18:09:19 by Tycho Andersen

pyproject: more (hopefully the last?) porting

Here's the last bits of what I think we should port to pyproject.toml
before releasing.

* I dropped the "Alpha" Classifier, we're beyond alpha, I've been using
  qtile as a daily driver for nearly 15 years
* I dropped the point-release python version Classifiers (i.e. 3.8, 3.9,
  etc.). These are not that interesting and a pain to maintain.
* I dropped Sean Vig as the listed maintainer. We list all the maintainers
  at the bottom of the readme, which ends up in the long_description. No
  reason to maintain two maintainer lists.
* I dropped Aldo as the Author:. There are lots of authors of qtile, this
  info is available from the git log.

My hope is that this will not give a syntax error when uploading source
now during the release workflow. I've inspected the output with:

    python3 setup.py bdist_wheel --keep-temp && cat build/bdist.linux-x86_64/wheel/qtile-*.dist-info/METADATA

and it looks pretty similar to the METADATA from the current release.

Signed-off-by: Tycho Andersen <tycho@tycho.pizza>

---
## [Wallemations/heavenstation](https://github.com/Wallemations/heavenstation)@[3645fa7d89...](https://github.com/Wallemations/heavenstation/commit/3645fa7d8956bed2d3ebff86b072f8b9544d383d)
#### Thursday 2023-09-07 18:15:41 by distributivgesetz

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
## [HWSensum/Fluffy-Frontier-Sensum](https://github.com/HWSensum/Fluffy-Frontier-Sensum)@[9ba52521fb...](https://github.com/HWSensum/Fluffy-Frontier-Sensum/commit/9ba52521fbe6522121dbc7a2c94edcb4add7ed97)
#### Thursday 2023-09-07 18:16:54 by SkyratBot

convert the eyeball a basic monster [MDB IGNORE] (#23043)

* convert the eyeball a basic monster (#77411)

## About The Pull Request
I have created a basic eyeball monster with new abilities and behaviors.
The eyeball has a unique power that allows it to glare at humans and
make them slow for a short period. However, this ability only works if
the human can see the eyeball monster. If a person is blind or unable to
see the eyeball, the ability won't affect them. Also, if someone turns
their back to the eyeball, it cannot use the ability on them. But be
cautious because the eyeball will try to position itself in front of the
person's face to use its power.

The eyeball is hostile towards all humans except for the blind ones and
those with significant eye damage. It has a compassionate side too, as
it loves to help people with eye damage by providing small healing to
their eyes.

Furthermore, the eyeball has a fondness for eating carrots, which not
only satisfies its appetite but also grants it a small health boost. To
add to its appearance, I've given it a new, larger, and scarier sprite.
However, I am open to changing it back to the old sprite if the player
prefers it that way.

Additionally, the eyeball displays emotions, and if you hit it, it will
cry tears as a sign of pain or sadness.
![eyeballs
pictures](https://github.com/tgstation/tgstation/assets/138636438/8933ea63-d339-474b-8c6e-90a222b74945)

## Why It's Good For The Game
the eyeball now have more depth and character to his behavier.

## Changelog
:cl:
refactor: the eyeball is a basic monster, please report any bugs
sprites: the eyeball now is bigger and scarier and now he will cry when
u hit him
/:cl:

* convert the eyeball a basic monster

---------

Co-authored-by: Ben10Omintrix <138636438+Ben10Omintrix@users.noreply.github.com>

---
## [HWSensum/Fluffy-Frontier-Sensum](https://github.com/HWSensum/Fluffy-Frontier-Sensum)@[27dbe394f1...](https://github.com/HWSensum/Fluffy-Frontier-Sensum/commit/27dbe394f1eef840daf6e66505a4c592caa1d228)
#### Thursday 2023-09-07 18:16:54 by SkyratBot

Refactors Morphs into Basic Mobs (there is now a swag action for morphification) [MDB IGNORE] (#23046)

* Refactors Morphs into Basic Mobs (there is now a swag action for morphification) (#77503)

## About The Pull Request

I was bored, so did this. Probably one of the neatest refactors I've
done, sorry if there's some oddities because I was experimenting with
some other stuff in this so just tell me to clean them up whenever I
can.

Anyways, morphs are basic mobs now. We are able to easily refactor the
whole "eat items and corpses" stuff in the basic mob framework, but the
whole "morph into objects and people" turned out to be a bit trickier.
That was easily rectified with a datum mob cooldown action and
copy-pasting the old code into that code, as well as doing some nice
stuff with traits and signals to ensure the one-way communication from
the action to the mob.

Old Morph AI didn't seem to be existant whatsoever, they inappropriately
leveraged some old procs and I have no idea how to make it work with new
AI. They DEFINITELY don't spawn outside of admin interference/ the event
anymore, and will always be controlled by a player, so this shouldn't be
too bad of an issue. I gave them something to seem alive just in case
though, but I think adding legitimate prop-hunt AI would be such a
laborious task that I am unwilling to do it in this PR.
## Why It's Good For The Game

If admins want to add the ability for Ian to assume the form of the HoP,
they can do that now! The datum action cooldown is quite nice for simple
and basic mobs... but it is currently not compatible with carbons. That
is not within scope for this PR, but I am dwelling on ways to extend it
to carbon but they all sound really awfully bad.

Also morphs are smarter, and we tick another simple animal in need of
refactoring off the list.
## Changelog
:cl:
refactor: Morphs are now basic mobs with a nice new ability to help you
change forms rather than the old shift-click method, much more
intuitive.
admin: With the morph rework comes a new ability you can add to mobs,
"Assume Form". Feel free to add that to any simple or basic mob for le
funnies as Runtime turns into a pen or something.
/:cl:

~~Does anyone know if there's a (sane) way to alias a cooldown action as
a keypress? I can't think of a good way to retain the old shift-click
functionality, because that does feel _kinda_ nice, but I think it can
be lived without.~~ I added it. Kinda fugly but whatever.

* Refactors Morphs into Basic Mobs (there is now a swag action for morphification)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [powerhome/playbook](https://github.com/powerhome/playbook)@[205619a0e9...](https://github.com/powerhome/playbook/commit/205619a0e9ce327306acf84735c13ea4ed356c7b)
#### Thursday 2023-09-07 18:28:02 by Gavin Huang

[PLAY-972] dateTime Bug Fixes (#2716)

**What does this PR do?**
- Corrects incorrect weekdays by removing the `getUTC` functions
- In the DB, for example, the date was August 15, 2023 01:30:00. The
`toWeekday` function formatted the date from UTC to Local Time, but
`getUTCDay()` went back to grab the UTC date. This issue was evident
with late-day appointments. Therefore, we should not be using any
`getUTC` functions.
- Corrects two bugs Jason found within`fromNow()`:
  - Remove period from "years ago"
- Fix miscalculation of "milliseconds in a month" - this was causing any
past date with a timestamp of "x months ago" to have a random number
- Updates `toLocaleString()` to use `en-US`
- Hayden R. reported he was receiving `undefined NaN`. Upon
investigation, certain locales (like en-GB [Great Britain]), can't use
functions like `getMonth()` so it was returning `undefined NaN`. We
default to `en-US` because internationalization and formatting does not
matter since Playbook formats dates in a specific way.

**Screenshots**

**Before**

![Before](https://github.com/powerhome/playbook/assets/47684670/07303adf-f2eb-4d7b-a0ba-ad82cf7f945c)

**After**

![After](https://github.com/powerhome/playbook/assets/47684670/8696283f-d4b4-4ab3-9302-c9651af672cd)

**How to test?** Steps to confirm the desired behavior:
1. The weekday problem was experienced in the [Sales
Books](https://nitro.powerhrg.com/sales/reps/11115/sales_books?rep_filter%5Bdate%5D%5Byear%5D=2023&rep_filter%5Bdate%5D%5Bmonth%5D=8).
In Miguel Picart's (or any RC), select their "Books" tab, select "All
Appointments", find any place that has 2+ appointments the same day -
they should be correct.
2. For Hayden's bug, impersonate Hayden and in his user profile ensure
that the address is showing as his European address. Go to a Runway
ticket and check the reviewers, he should not see `undefined NaN`. We
should also ensure that Hayden can see a date after the release.

#### Checklist:
- [X] **LABELS** Add a label: `enhancement`, `bug`, `improvement`, `new
kit`, `deprecated`, or `breaking`. See [Changelog &
Labels](https://github.com/powerhome/playbook/wiki/Changelog-&-Labels)
for details.
- [X] **DEPLOY** I have added the `milano` label to show I'm ready for a
review.
- [ ] **TESTS** I have added test coverage to my code.

---------

Co-authored-by: Nida Ghuman <nidaqg@gmail.com>

---
## [dubstard/eth-phishing-detect](https://github.com/dubstard/eth-phishing-detect)@[780e0b4122...](https://github.com/dubstard/eth-phishing-detect/commit/780e0b4122485bbe8754c72fac2a35a19ecf6dab)
#### Thursday 2023-09-07 18:29:11 by Mich

block scams

``
    "0xcoin.in",
    "2muskx.cc",
    "2tesla.cc",
    "2xmusk.space",
    "2xtesla.cc",
    "500px.com",
    "abict.pro",
    "aerodrome.capital",
    "aibb.claims",
    "ait.gifts",
    "akidcalledbeast.gift",
    "algotradersguild.com",
    "alskafu.com",
    "alskafu.net",
    "anaxine.finance",
    "angrycat.best",
    "angrycat.guru",
    "app-1icnh.com",
    "app-unislwap.org",
    "app3-vniswsepprotocols.top",
    "applediscounter.store",
    "appsv3-panskiekprotocol.top",
    "appsv3-pasnekekswap.top",
    "appv3-unisqswops.top",
    "appv3-unsiwpawprotccol.top+",
    "arbitruun.foundation",
    "arkhamintellingence.net",
    "articlesfox.com",
    "autisminteligence.lol",
    "avifavindia.com",
    "axieinflnity.com",
    "axretailgroup.com",
    "babydogenft.org",
    "balances-celsius.network",
    "bald-base.com",
    "bestaq.com",
    "bigeyescoinclaim.netlify.a",
    "bitinauts.zone",
    "blogsbeta.com",
    "bps-sber24.online",
    "bpsbank24-by.online",
    "c-elsius-withdraw.network",
    "c-elsius.com",
    "cake.claims",
    "cascadune.co",
    "celsi-us-recover-assets.com",
    "celsiius-withdraw.com",
    "celsiu-s-network.com",
    "celsius.pages.dev",
    "celssius-network.com",
    "chainlinks.gift",
    "circleclaim.org",
    "claim-boredapes.com",
    "claim-celsius.network",
    "claimcrv.com",
    "claims-celsius.network",
    "claims-coinbase.com",
    "co-nextget.com",
    "coinstats-app.online",
    "connextairdrop.pages.dev",
    "connextdrop.network",
    "coredao.to",
    "correosprepaqa.com",
    "creditors-celsius.network",
    "crypto-uniswap.org",
    "cryptrecover.com",
    "customer-club.com",
    "customersurveypanel.net",
    "datebest.net",
    "dexstools.com",
    "dfgdsasd.ru",
    "digicask.com",
    "discussionarchive.com",
    "dnrbpo.com",
    "dodo-opros.online",
    "drop-aave.com",
    "drop-jasmy.com",
    "drops-pancakeswap.org",
    "duozap.com",
    "edveno.com",
    "enter-milady.xyz",
    "ethereum-pow.online",
    "evilpepecoin.top",
    "evri-resend.com",
    "exchange-okx.com",
    "finttv.cc",
    "finttv.ga",
    "freeclaim.xyz",
    "friendclaim.live",
    "huangcdev.com",
    "investavoyager.com",
    "invisible.sale",
    "kidsofapocalypse.us",
    "layerzcro.network",
    "layerzeronatwork.xyz",
    "link3tcyberconnect2.tech",
    "livedappsconnect.website",
    "lovelys.gift",
    "mailapp-metamask.com",
    "mailserver-metamask.com",
    "meetyemmy.com",
    "metamask.free-claim.pro",
    "metamask4.app",
    "metamaskjobs.io",
    "metamasktokens-drop.com",
    "metamseak.io",
    "mong.gift",
    "moonbirds.gift",
    "msdrainer.site",
    "mummy.gift",
    "musk-2023.com",
    "musk2xbtc.space",
    "muskbtc2x.space",
    "muskx2.cc",
    "muskx2k.cc",
    "mute.claims",
    "nftangrycat.online",
    "opepen.gift",
    "opnx.gift",
    "org-polygon-v3-defi.site",
    "pancakeswap.affiliate-program.online",
    "pasnkakesvawp-fknance.com",
    "pepexplorers.com",
    "pepperjellys.com",
    "pinkrsale.com",
    "pinkrsale.org",
    "pyusderc.com",
    "quickswap.claims",
    "rdnt.capital",
    "recoverassetscellsius.network",
    "recovercellsius-assets.com",
    "rizmonkey.com",
    "robinsood.info",
    "rtfkt.gifts",
    "s2tesla.cc",
    "s2tesla.com",
    "schasb.com",
    "shabaswap.com",
    "shibarium-claim.com",
    "shibavoucher.top",
    "shibavpepe.io",
    "shilbarum.online",
    "shimbarium.online",
    "slingshot.claims",
    "sonikcoinsofficial.com",
    "sonikcoirn.org",
    "spectacuiardate.com",
    "spsinghcharitabletrust.com",
    "stepnairdrop.top",
    "sushirewards.org",
    "swaprum.io",
    "tesla-giveaway.pro",
    "tesla-stocks.com",
    "tesla-stocks.us",
    "tesla2.cc",
    "tesla2s.cc",
    "teslasx2.com",
    "teslax.cc",
    "teslax2e.cc",
    "teslax2s.cc",
    "teslax2s.com",
    "thetaclaim.com",
    "tradingview.expert",
    "usdcoincrypto.com",
    "usuperfund.com",
    "vela.claims",
    "velocore.gifts",
    "verify-metamask.business",
    "vitalik-qr.com",
    "vizebasvurusu.online",
    "vulcanforged-event.com",
    "wallet-web3.com",
    "wallrstmemes.com",
    "web-uniswap.org",
    "web3-metamaskd.com",
    "withdraw-cellsius.network",
    "withdraw-celsius.network",
    "withdraw-stretto.com",
    "world-circle.net",
    "worldcoin.is",
    "wrapped-gifts.io",
    "x-coin.in",
    "x2teslas.com",
    "xlretailgroup.com",
    "xmusk2.cc",
    "xrpspot.info",
    "xtesla.cc",
    "xtesla2.cc",
    "xteslas2.cc",
    "yearnn.com",
    "yecoin.in",
    "zerc.pro",
    "zksyncy.com",
    "zoras.org",
```

---
## [pytorch/benchmark](https://github.com/pytorch/benchmark)@[745644f391...](https://github.com/pytorch/benchmark/commit/745644f391b4d11da107b2c82fe2d7a3eacf561d)
#### Thursday 2023-09-07 18:36:34 by Mark Saroufim

FIX SAM for bfloat16 (#1764)

Summary:
Ok this was kinda annoying

Basically the SAM codebase had a few places where it hardcodes `torch.float32` such that even if you convert the model to `torch.bfloat16` a few parts of the model won't be and will have type mismatch errors - this fixes the problem cpuhrsch desertfire - idk enough about floats and why there isn't some type promotion rule for bfloat16

I wonder whether we should add tests for multiple dtypes in torchbench to make checking for this kind of issue more robust especially now that bfloat16 seems to be the default for dynamo xuzhao9

## Logs

```
FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
E
======================================================================
ERROR: test_sam_eval_cuda (__main__.TestBenchmark)
----------------------------------------------------------------------
components._impl.workers.subprocess_rpc.ChildTraceException: Traceback (most recent call last):
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 482, in _run_block
    exec(  # noqa: P204
  File "<subprocess-worker>", line 2, in <module>
  File "/home/ubuntu/benchmark/torchbenchmark/util/model.py", line 280, in invoke
    out = self.eval()
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/__init__.py", line 65, in eval
    masks, scores, logits = predictor.predict(
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/predictor.py", line 164, in predict
    low_res_masks_np = low_res_masks[0].detach().cpu().numpy()
TypeError: Got unsupported ScalarType BFloat16

    working_dir: /tmp/tmpg5de41du
    stdout:
        [2023-07-13] 01:57:38.499061: TIMER_SUBPROCESS_BEGIN_EXEC
        [2023-07-13] 01:57:39.002078: TIMER_SUBPROCESS_FAILED
        [2023-07-13] 01:57:39.002141: TIMER_SUBPROCESS_FINISHED
        [2023-07-13] 01:57:39.002153: TIMER_SUBPROCESS_BEGIN_READ

    stderr:

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/ubuntu/benchmark/test.py", line 104, in eval_fn
    task.invoke()
  File "/home/ubuntu/benchmark/torchbenchmark/__init__.py", line 402, in invoke
    self.worker.run("""
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 155, in run
    self._run(snippet)
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 320, in _run
    subprocess_rpc.SerializedException.raise_from(
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 458, in raise_from
    raise e from ChildTraceException(traceback_str)
TypeError: Got unsupported ScalarType BFloat16

----------------------------------------------------------------------
Ran 1 test in 7.814s

FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
.
----------------------------------------------------------------------
Ran 1 test in 8.315s

OK
```

Pull Request resolved: https://github.com/pytorch/benchmark/pull/1764

Reviewed By: drisspg, cpuhrsch

Differential Revision: D47441873

Pulled By: msaroufim

fbshipit-source-id: a60880fd7c0826cfd469ace39d76894469ca0e5e

---
## [Paxilmaniac/tgstation](https://github.com/Paxilmaniac/tgstation)@[fb4587b336...](https://github.com/Paxilmaniac/tgstation/commit/fb4587b3368ebb55e0cc10f8c650abcc26afa5d4)
#### Thursday 2023-09-07 18:51:48 by san7890

Cursed Slot Machine Fixes (#77989)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

A lot of these were stuff I did in response to reviews but apparently
didn't test extremely thoroughly. My bad.

* The proc for checking if the machine is in use is split out into its
own thing for clarity, and for potential reuse.
* The signal is no longer fucked up so you can actually get more than
one curse out of the slot machine as intended.
* Admin heals (and admin heals only) can remove the status effect. This
is just in case someone fucks up a variable when running an event and
wants to quickly heal some people while they varedit it to actually be a
proper event.
* Some nice code stuff while I was there, we don't need to be
typecasting to human anymore so it's nice to fix that.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Fixes are good.

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
fix: The Cursed Slot Machine should now actually give you more than one
pull.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Ua-Gi-Oh/UA_EDO](https://github.com/Ua-Gi-Oh/UA_EDO)@[c7270f152e...](https://github.com/Ua-Gi-Oh/UA_EDO/commit/c7270f152e5a9d2cfb95dd0cb398158d73bea567)
#### Thursday 2023-09-07 19:24:39 by Ua-Gi-Oh

Перекладені карти 

1 - Icejade Cenote Enion Cradle
2 - Buzzsaw Shark
3 - Umbral Horror Ghoul
4 - Field Barrier
5 - Predaplant Cordyceps
6 - Bait Doll
7 - Toon Ancient Gear Golem
8 - Armor Exe
9 - Aurkus, Lightsworn Druid
10 - Number 52: Diamond Crab King
11 - Chocolate Magician Girl
12 - Metal Shooter
13 - Flower Bloom of the Vernusylph
14 - Mon Larvas
15 - Curse of Dragonfire
16 - Koalo-Koala
17 - Infernity Beast
18 - Performapal Life Swordsman
19 - Abyss Actor - Twinkle Little Star
20 - Secret Six Samurai - Genba

---
## [Premvenkat14/PowerBI](https://github.com/Premvenkat14/PowerBI)@[fd1e098c14...](https://github.com/Premvenkat14/PowerBI/commit/fd1e098c144996234d8e621590edbb1b3cbf131c)
#### Thursday 2023-09-07 19:49:00 by Premvenkat14

Add files via upload

🚀 Exciting News! 🚀

I'm thrilled to share a milestone in my data journey – I've just created my very first interactive dashboard using Power BI! 📊✨

Dashboard Title: PIZZA SALES ANALYTICS

Tool Used: Power BI, excel

In this project, I delved into the delicious world of pizza sales data and leveraged the power of Power BI to transform raw data into actionable insights. Here are some of the key performance indicators I've visualized:

📈 Total revenue

💰 Average order value

🍕 Total pizzas sold

🛒 Total orders

🍽️ Average pizzas per order

📆 Monthly trends for total orders

🍕 Pizza categories-wise total sales

📏 Pizza size-wise total sales

🏆 Top 5 best-selling pizzas by revenue

👎 Bottom 5 worst-selling pizzas by revenue

🏆 Top 5 best-selling pizzas by quantity

👎 Bottom 5 worst-selling pizzas by quantity

🏆 Top 5 best-selling pizzas by total orders

👎 Bottom 5 worst-selling pizzas by total orders

Creating this dashboard was a fantastic learning experience, and I'm excited to see how it can provide valuable insights for pizza sales analysis. If you're curious about how Power BI can transform your data into actionable visuals, feel free to reach out—I'd be happy to share my experience and tips! 🤝

Stay tuned for more data-driven adventures and dashboards to come! 🚀 #PowerBI #DataVisualization #PizzaSales #Analytics

---
## [saltwaterterrapin/EvilHack](https://github.com/saltwaterterrapin/EvilHack)@[9c74c93093...](https://github.com/saltwaterterrapin/EvilHack/commit/9c74c93093dd2c664656b28a22643b19e19ba0a7)
#### Thursday 2023-09-07 20:01:11 by k21971

Fix: close a loophole being able to produce tame non-tameable monsters.

In tamedog() there are several monsters that are flagged as off limits
to being tamed (feeding, magical taming, etc). But creating a blessed
figurine of the same, and the player could get around that limitation.
Finally decided to dig into why that was - the restrictions in tamedog()
did not fully align with those in make_familiar(). This commit closes
that loophole. You could still get a tame 'non-tameable' by getting
lucky with a poly trap/wand/spell however, we'll leave that in place as
it's purely by chance. While fixing this, I refactored what was deemed
as non-tameable and made a define for it in mondata.h

Also in this commit, a bit of code formatting in trap.c and wield.c

---
## [RatFromTheJungle/Skyrat-tg](https://github.com/RatFromTheJungle/Skyrat-tg)@[1901f6b9e2...](https://github.com/RatFromTheJungle/Skyrat-tg/commit/1901f6b9e2a575052b561514fee8602cf8e918db)
#### Thursday 2023-09-07 20:11:41 by SkyratBot

[MIRROR] North Star Science Rework And More [MDB IGNORE] (#23022)

* North Star Science Rework And More (#77439)

## About The Pull Request
I fixed a few miscellaneous issues and also redid science (mainly
genetics, cytology, and xenobiology)
This is genetics, it's basically the same but moneky have bananas and I
rotated it so they'll be visible from the front desk.

![geneticsnew](https://github.com/tgstation/tgstation/assets/73589390/7c10d75b-2a7a-47b2-a6ca-a30354d713c3)

Holy fuck it's Cytology as a proper area. It now has main hall access
and a public access petting zoo. Now you can show off all your new
creatures (it also has some items cytologists generally want)

![cytonew](https://github.com/tgstation/tgstation/assets/73589390/7d9256c9-b39a-4502-b599-9226a2ca5cd8)

Upstairs is Xenobio, which is now much larger and soulless. Instead of a
normal holding cell there's a prefilled room of oxygen and BZ (the
holding room, why is BZ invisible?)

![xenonew](https://github.com/tgstation/tgstation/assets/73589390/5dc28dba-a051-4858-a9fc-16d51e987c33)

I also gave Ordnance 5 TTVs, same as other maps.
Also the coroner no longer has an unreachable box of bodybags
Also sec now has 2 secways + 2 keys for their usage
## Why It's Good For The Game
I'm forcing xenobiologists to be closer to a hall so they might actually
interact with people, and giving cytologists a reason to do anything
ever because they have a petting zoo to show their creatures off in. Oh
yeah also cytology gets equipment they should just have (a botany tray,
tools to butcher with, a shitty old laser gun to kill experiments gone
wrong)
Genetics is just better because people from the hall can see the
Geneticists working so they can bug them for stuff.

A few of the fixes are very tiny, like moving a few areas by the service
hall and adding a single pipe to the AI SAT
## Changelog
:cl:
qol: North Star's Cytology and Xenobiology are now significantly more
usable.
add: North Star's Genetics has been tweaked.
fix: The North Star's AI SAT has a working vent and it's service hall
has a working lightswitch
/:cl:

* North Star Science Rework And More

---------

Co-authored-by: Cheshify <73589390+Cheshify@users.noreply.github.com>

---
## [Offroaders123/Dovetail](https://github.com/Offroaders123/Dovetail)@[39bbf27d1d...](https://github.com/Offroaders123/Dovetail/commit/39bbf27d1d0d7bfbe5a23b3f5a6bb58e91589b53)
#### Thursday 2023-09-07 20:49:28 by Offroaders123

Component Learning: Header

Trying to wrap my head around how you're supposed to structure the state of your app using components, I keep getting stuck trying to pass data up and down out of components, when I have a hunch it's only supposed to go from the top-down?

https://stackoverflow.com/questions/70469476/whats-the-equivalent-of-useref-in-svelte (helpful for element references)

From my discussion with HoldYourWaffle about my confusion:

Ok I'm finding out what else I have trouble with in component-based UI structures
It's deciding where I should place my interaction code, like what components should contain them
(`function saveFile`, `Header.svelte`, `saver.addEventListener`)

So the new Svelte code above is what would replace this event listener
My mix up is whether this save handling code should go in the `Header` component, which is where the save button currently is, or go up a level to the `App` component
How do you import values from other components to use them?
Maybe it's that the state shouldn't be centralized to components like I want them to be, but maybe it has to come from the top-down instead?
Because to get the options from the `FormatDialog` component (once I make that), then I have to get the value out of that component somehow, so the Header can use it for the save handling function here
So is my design flaw that the state should instead just be at the top of the app, and each of the elements can just use those as props?
Then it feels counterintuitive to the component nature that Svelte is trying to employ, because I'm just essentially pushing everything up to the 'global' component, which then just passes all the state down as props; that feels more overboard to me for some reason?
I'd think if it's a component, it holds it's own state right?
How do components interact with other components?
I think this is probably just my brain thinking of it the wrong way, it probably should work the top-down way, just like how dependency injection works for functions, it should work that way for components probably too?
I definitely like how that works for functions, so that's probably how you're meant to do it with components too?

(About `Header.svelte`) And can you import exports from other components? That seems like what I'm gravitating towards, but that might be going against how you're intended to design the state flow

```js
import Header, { saveFile } from "./Header.svelte";
```

It's the confusion of where my brain sees ESM but it's not real ESM, but rather Svelte component props being marked a 'public' or 'private', like a `class` would do
`let hi = true` is a private property of the component, while `export let hey = true` is a public property
But how can you use properties from other components, since `export` doesn't do what `export` does in regular JS land?
Wait, actually I wonder if this works (Code snippet above)
Nope, dangit

It's that the syntax makes a `class`-like thing appear like a module, when it's really a `class` in a way
What if you had JSX code which had Svelte destiny-like features, but compiled down to how Svelte works? (not that this should be a thing, but I think the mix of class behavior with ESM syntax is what is getting confusing for me)

(Destiny is about the destiny operator idea/proposal, which is like Svelte's `$` definition)
https://news.ycombinator.com/item?id=8172491
https://es.discourse.group/t/destiny-operator/895

---
## [Night-Traders-Dev/Stock_Market_Engine](https://github.com/Night-Traders-Dev/Stock_Market_Engine)@[6a2e576802...](https://github.com/Night-Traders-Dev/Stock_Market_Engine/commit/6a2e576802e123ca6b3e1cc0549fb99d42775493)
#### Thursday 2023-09-07 21:36:00 by ōFuel Rocket Lounge

Update engine.py

Version 0.0.18.0: Slot Machine Game and Tax Adjustment

In this update, we're introducing the exciting Slot Machine game! Take a spin, match symbols, and win fantastic rewards. We've also made some enhancements to improve the gaming experience:

- Slot Machine Game:
  - Spin the reels and try your luck.
  - Land various symbols for different rewards.
  - Win up to 100 times your bet for a perfect match.
  - Lowered the maximum tax rate to 25% for reduced deductions.

Enjoy the thrill of the Slot Machine and let us know your feedback! Happy gaming! 🎰🎉

Date: 09/07/2023

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[dd778af63d...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/dd778af63dc01e8386739fb9be9821bcf83a198e)
#### Thursday 2023-09-07 22:23:40 by Sealed101

Adds Summon Cheese (#77778)

oh apparently this is my 100th PR on tg, which is weird because github
reports 99 total, and i made at least one to the old voidcrew repo, and
filtering tg prs by my name still shows 99. weird. here's to 100 more i
guess?

<sub>could have been better if it was a get, jhonflupwliiard watch ur
back 🔫 </sub>

## About The Pull Request

Adds a new spell granter book to the Wizard's Den - Summon Cheese, which
grants the spell by the same name, which summons 9 heads of cheese.
That's about it, I think.

## Why It's Good For The Game

Wizards are a hungry bunch, so why can't they just summon food? They can
even share, if they'd like, since the notion of a friendly wizard still
exists

<details>
<summary>... </summary>

alright fine
i'm slightly malding over not getting the 77777 get so no more
roleplaying in the pr body

Wizard Grand Ritual now has a hidden goal of sacrificing 50 cheese
wheels. Sacrificing a cheese wheel is done with invoking the grand rune,
and each invocation/pulse of the rune will whisk away more cheese until
all cheese on the rune is taken by whichever entity lurks in the other
realm. The sacrifice will be hinted at in an _ancient parchment_ which
will be on the bookshelf (when i add it lmao) alongside the spell book.

Meeting this cheese goal will lock the wizard's grand finale rune and
grand finale effect to special ones. The cheese rune is mostly identical
to the normal grand rune, barring the custom sprites/animations.
The cheese finale consists of the wizard getting permanent Levitation
(nogravity + free space movement), a 0.5 modifier(reducing incoming
damage in half) to every damage type, a comically strong mood buff and
**The Wabbajack**(separate sprite pending) - a juiced up chaos staff
which can fire a lot more projectiles than a normal one can (it will get
more, I may even make a few just for it).
Everybody else (including any invader antags) gets hallucinations, 175
brain damage and a comically strong mood debuff, as well as a vendetta
against the wizard. If the victim was already suffering from
hallucinations from a trauma (including the quirk), they are instead
healed.

if you didn't catch the obvious reference, this entire shtick is a
tribute to Sheogorath. the rune makes use of daedric script, and most of
the catchphrases are a direct quotation of the Daedric Prince of
Madness, so if any of those things can get us in trouble somehow, let me
know. i will be sad but i will comply.

This shtick is intended as an easter egg, really, so I wasn't really
planning on expanding the wizard grand finale into heretic paths thing
or whatever.

Oh, and finale grand runes now allow the wizard to select the effect
even if it's time-gated. If it is, you just won't be able to invoke it
until the time comes. The rune will tell you how much time is left until
you can invoke it. And grand finale runes with a finale effect selected
also glow in the color of their effect. I also think I fixed some step
of the grand rune animation not triggering but I'm not sure.

<details><summary>Some rune animations (some are subject to
change)</summary>


![rune_cheese_activate](https://github.com/tgstation/tgstation/assets/75863639/62ae184d-b6fc-4883-a169-4d8ca7636b40)


![rune_cheese_flash_2](https://github.com/tgstation/tgstation/assets/75863639/619545c8-3c55-4264-bfa4-d40067ef7406)


</details> 

## Why It's Great For The Game

it's funny

</details> 

## Changelog


:cl: Sealed101, EBAT_BASUHA for spritework
add: Wizard's Den now has a book of Summon Cheese in the Studies Room
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[bf1269225f...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/bf1269225fbac94304bbcc17af46a45918521575)
#### Thursday 2023-09-07 22:23:40 by GuillaumePrata

Makes fanny packs be silent, others can't see what you put in or take out. (#78010)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Just like the syndicate toolbox and a handful of other items.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This is a blatantly stealth antag buff.

Pockets are 2 silent storage slots everyone has, so it is not adding
anything that antags didn't have access already.
But going from 2 to 5 small items can help a lot, also belts are a lot
smoother to use with their shortcut keys.

Love stealth antags, hate murderboners, gonna help my stealth boys not
be valid hunted because someone checked their chat logs from 10 minutes
ago and read that X player put Y contraband in their bag.

Or people that have some contraband names highlighted on chat... but no
one does that right.... right?
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

:cl:Guillaume Prata
balance: Fanny packs are now silent, no one will get a chat message
about what you put in or take out.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Aki Ito <11748095+ExcessiveUseOfCobblestone@users.noreply.github.com>

---
## [lexical-lsp/lexical](https://github.com/lexical-lsp/lexical)@[170c5c3272...](https://github.com/lexical-lsp/lexical/commit/170c5c327289a9d087051f483e9d5df2843ef3d5)
#### Thursday 2023-09-07 23:21:33 by Steve Cohen

Indexing features for modules (#347)

* Indexing features for modules

This commit introduces indexing for module references. It currently
will only work for files to which we have the source code, turns them
into AST and then applies one or more "extractors" on it. An extractor
runs over AST and indetifies things it's looking for, and then emits
entries, which will be used to build a searchable index.

Currently, there is one extractor implemented: Module references. This
does a fairly exhaustive search for module references, wherever
they're hiding. It then uses the aliases module to find the original
source module.

Note that most of the higher level functions are just placeholders. An
indexing strategy needs to find things inside of .exs files as well as
.ex files, and we currently have no way to index core elixir (this
will be highly dependent on how elixir was installed and if we can get
the source code to the version we're running on).

* Performance fixes / code improvements

Turns out `Aliases.at()` was super slow --especially since we called
it so much when resolving aliases during indexing. This was due to it
having to re-parse the document multiple times for each alias
reference. Moving to sourceror and allowing the AST to be sent in cut
the indexing time for lexical and all its deps from 60 seconds to 10.


* ETS based storage / Fuzzy matching

This commit has ETS based file storage and a fuzzy matching system.
I was having a lot of trouble coming up with an efficient way to perform
fuzzy matching against a corpous of subjects efficiently using the data
stores. ETS is... ets, and it appears that it's impossible to use it for
any type of detailed string matching. SQLite had similar problems. While
it had a lot more complicated and helpful utilities, it just couldn't do
what I wanted when it comes to fuzziness.

Then I thought, hey, why not just store the subjects in memory with all
the places that they appear? Then you just keep that up to date, and you
remove a lot of duplication, which improves performance a lot.

Prior to this, ETS was taking around 300ms to do simple-ish matching,
and SQLite was taking around 180ms. Fuzzy can do it in 14ms. Better yet,
building a fuzzy from scratch only takes 40ms for lexical and all its
deps. This includes doing much more interesting matching.

I think we have a winner.

---
## [Ryll-Ryll/tgstation](https://github.com/Ryll-Ryll/tgstation)@[ebbc45b161...](https://github.com/Ryll-Ryll/tgstation/commit/ebbc45b1616c08d2dc0b6e6ce48258f68eefd46a)
#### Thursday 2023-09-07 23:33:16 by distributivgesetz

Improved PDA Direct Messenger (#75820)

## About The Pull Request

Fixes #76708, Closes #76729 (sorry Zephyr)

This PR expands the Direct Messenger UI, adding a chat screen for each
available messenger that you can find, and moving message sending over
to TGUI.

This chat screen includes a message log that displays messages sent by
you as well as messages received from the recipient. This gets rid of
the previous chat log, which just had all messages thrown together that
you received or have sent, in one big list.

Furthermore, all messaging is now done inside the UI. This kills all
TGUI popups you would ever need to send messages forever (except for
quick replies). Use the input bar on the bottom, press Enter or the Send
button, and it sends your message. Spam mode is now done in the UI too,
via a text field you can find in the contacts list.

Additionally, because I have a habit of blowing things massively out of
scope, I've also completely refactored how messages and chat logs are
stored in the PDA messenger. I plan on using this in a PR that merges
the chat client with the messenger, sometime in the future. Sorry this
took so long.

Stuff left to do before I open this PR for review:
- [x] Add "recent messages"
- [x] Add "unread messages"
- [x] Add message drafts
- [x] Make photo sending not shit
- [x] Implement the edge cases for automated and rigged messages
- [x] Make sure shit isn't fucked
- [x] Profit

<details>
  <summary>Screenshots</summary>
  

![dreamseeker_HIrEfrap5X](https://github.com/tgstation/tgstation/assets/47710522/97c713b7-dda3-44d3-a8f5-d0ec11c92668)

![qIOWhVld4l](https://github.com/tgstation/tgstation/assets/47710522/3ab4e2c1-a38f-4b20-8e9f-509ea14c0434)

![dreamseeker_LIqwi05i4O](https://github.com/tgstation/tgstation/assets/47710522/c051c791-b595-4166-a4d3-82cb7568411f)

![BIYxNVjGL7](https://github.com/tgstation/tgstation/assets/47710522/b9c97eab-52b5-449f-b00f-a0d8aa5f865c)

![dreamseeker_IWdoSsUinC](https://github.com/tgstation/tgstation/assets/47710522/2a4cd76a-2bdc-4283-b642-09e92476fef5)

![L9DxzFHDEF](https://github.com/tgstation/tgstation/assets/47710522/6a5b0e29-d535-4c7e-a88e-e9b71198719b)

![rAuDgqBLNE](https://github.com/tgstation/tgstation/assets/47710522/128a0291-91da-4f9e-9bc5-a65cf411ea6d)

![dreamseeker_voui6S8MUf](https://github.com/tgstation/tgstation/assets/47710522/6e3ba044-b8df-492d-b58d-6c73ab07233d)

![image](https://github.com/tgstation/tgstation/assets/47710522/522c1d85-b9cf-4e0e-9588-9d3993eea03f)

</details>

## Why It's Good For The Game

The UI has largely stayed the same since modular tablets were added a
year ago. Even better, direct messaging has been the same since PDAs
were first added *more than a decade ago*. Imagine that.

Now we finally actually (!) make use of those brand new features that we
got from the TGUI switch in this regard.
## Changelog
:cl: distributivgesetz
add: Updated Direct Messenger to v6.5.3. Now including brand new
individual chat rooms, proper image attachments and a revolutionary
message input field!
add: Added a "Reset Imprint" option to the PDA painter.
refactor: Refactored PDA imprinting code just a bit.
fix: PDAs should now properly respond to rigged messages.
/:cl:

---------

Co-authored-by: Jeremiah <42397676+jlsnow301@users.noreply.github.com>

---
## [Ryll-Ryll/tgstation](https://github.com/Ryll-Ryll/tgstation)@[27d46f1717...](https://github.com/Ryll-Ryll/tgstation/commit/27d46f17173034b805d6ef064d4db31c7e34b26d)
#### Thursday 2023-09-07 23:33:16 by OrionTheFox

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
## [Ryll-Ryll/tgstation](https://github.com/Ryll-Ryll/tgstation)@[a288abcaf2...](https://github.com/Ryll-Ryll/tgstation/commit/a288abcaf2a6b6c44edade8265a66b9ba3f0e67b)
#### Thursday 2023-09-07 23:33:16 by san7890

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

