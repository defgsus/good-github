## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-02](docs/good-messages/2023/2023-03-02.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,320,853 were push events containing 3,542,716 commit messages that amount to 272,524,815 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 56 messages:


## [McGuirk2002/wiredwormz.quest](https://github.com/McGuirk2002/wiredwormz.quest)@[a568298782...](https://github.com/McGuirk2002/wiredwormz.quest/commit/a56829878286d2acef47b92f0e952bda7f7727c1)
#### Thursday 2023-03-02 00:02:33 by smile dog

oh fuck yeah, you thought it was over? think again, bitch

---
## [RobertoMaurizzi/godot](https://github.com/RobertoMaurizzi/godot)@[92bee43adb...](https://github.com/RobertoMaurizzi/godot/commit/92bee43adba8d2401ef40e2480e53087bcb1eaf1)
#### Thursday 2023-03-02 00:55:08 by Rémi Verschelde

Bump version to 4.0-stable \o/

4 years of development.
12,000 merged pull requests.
7,000 fixed issues.
1,500 individual contributors across engine and docs.

The Godot 4.0 release is by all metrics our biggest release so far.
No stone has been left unturned, all parts of the engine have been
modernized, refactored, overhauled, rewritten, redesigned.

Our work is far from done. Many areas still have significant known issues,
and will require focused work from all willing contributors to fix blocking
bugs, implement missing features, optimize for performance or compatibility,
and improve the user experience.

But Godot 4.0 marks the start of the new, modern Godot Engine, and a solid
foundation for us all to build upon. Future 4.x releases will come with a
much faster cadence, enabling us to iterate quickly on new features and
improvements to what we already provide.

To all of you who were involved in making Godot 4.0 what it is today, however
big or small your contributions were:

THANK YOU!

This was a massive undertaking, and you all participated in unique and
wonderful ways to build a free and open source game engine for everyone to
use and enjoy. You are breathtaking! <3

---
## [LynxSolstice/cmss13](https://github.com/LynxSolstice/cmss13)@[3978cfe70f...](https://github.com/LynxSolstice/cmss13/commit/3978cfe70f7e32331243e8b05738067b6101ebe6)
#### Thursday 2023-03-02 00:55:46 by spartanbobby

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
## [kidgenius703/tgstation](https://github.com/kidgenius703/tgstation)@[06a7e74790...](https://github.com/kidgenius703/tgstation/commit/06a7e74790b3b05b7f4fb522ff55858ef0d66418)
#### Thursday 2023-03-02 00:56:23 by Unit2E

Changes the hypno flash to work on unconscious people (#73025)

## About The Pull Request

The hypno flash is a really fun and flavourful item that is both strong
while allowing for gimmicks. However, personally, I've always been a bit
confused as to what counted for hypnosis, until looking into the
specifics. I also know that I'm probably not alone in this, because
various people have told me over the years that sleep doesn't work,
while it definitely does. This PR hopes to change this by somewhat
buffing the hypno flash, by making unconsciousness work for hypnosis.

## Why It's Good For The Game

Unconsciousness looks very similar to sleep, and in a lot of cases it is
really just the same effect... except for hypnosis, where there is no
effect on unconscious people. Personally, I don't think this is the best
UX and it limits the options there are for hypnotising people, which is
a shame, as I think it's very interesting. This may or may not be too
strong (think using the hypno flash with the micro-laser), but I still
think this is preferable to only working with sleep specifically or
hypnosis, might warrant a TC up if people otherwise agree with the
change. Also, just to note, unconsciousness is also still separate from
crit. This does not let you hypnotise people for free because they're in
crit.

---
## [kidgenius703/tgstation](https://github.com/kidgenius703/tgstation)@[a155df74a0...](https://github.com/kidgenius703/tgstation/commit/a155df74a09c075efe1339cd1cd24e5cc189fc12)
#### Thursday 2023-03-02 00:56:23 by Rhials

Abductor scientist self-retrieve failure/runtime fix (#73172)

## About The Pull Request

Since the abductor outfit/implant would load before the abductor ship
(and it's teleport pad) when first generating a team, a runtime would
occur when trying to link the pad to the implant. Another would occur
every time you attempted to retrieve yourself (as the linked pad would
be null), preventing recall and completely neutering an abductor team's
most important maneuver.

Now, using the implant will perform the linking process again if no
linked pad is found, and provides the owner with a warning if (by some
great calamity) they genuinely have no pad to teleport back to. This
solves the issue of the implant sometimes not linking to a pad properly
on initialize, and makes them way less prone to breaking.

Apparently this has been broken for a while, presumably since the
abductor ship was made into a lazyloading template.
## Why It's Good For The Game

The funny silly grey men get to torture the poor hapless crew once
again.
## Changelog
:cl:
fix: abductor scientist's retrieval implants will now properly recall
the owner, and inform them upon recall failure.
/:cl:

---
## [lkuoch/helix](https://github.com/lkuoch/helix)@[973c51c3e9...](https://github.com/lkuoch/helix/commit/973c51c3e970aa975f2bd1869d50ce2ae6c6de34)
#### Thursday 2023-03-02 02:38:10 by Michael Davis

Remove C-n and C-p from the insert mode keymap (#3340)

These are read-line-like bindings which we'd like to minimize in
insert mode in general.

In particular these two are troublesome if you have a low
`editor.idle-timeout` config and are using LSP completions: the
behavior of C-n/C-p switches from moving down/up lines to moving
down/up the completion menu, so if you hit C-n too quickly
expecting to be in the completion menu, you'll end up moving down
a line instead. Using C-p moves you back up the line but doesn't
re-trigger the completion menu. This kind of timing related change
to behavior isn't realistically that big of a deal but it can be
annoying.

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[7cc6934eff...](https://github.com/timothymtorres/tgstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Thursday 2023-03-02 03:04:41 by LemonInTheDark

Visual fixes (lighting, weird shit, old bugs from a parallax thing) (#73555)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

[Fixes a bug where anything fully dark on the floor plane would mask the
lighting
plane](https://github.com/tgstation/tgstation/commit/a1a03dc3393216098890b971b2271d56cb2c7463)

I fucked it up boys, needed to take alpha into account here

[Fixes pais getting parallax on icebox because their location was
nested](https://github.com/tgstation/tgstation/commit/81252e0f45c53918a14cc0148353ec440710f8e5)

God I hate this place (Note when I say get I mean they got the plane
master that controls it, not that they actually got it displayed. That
does appear to sometimes happen but I have no idea why)

[Fixes double flashlights not activating if enabled in
place](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

[efb8b64](https://github.com/tgstation/tgstation/pull/73555/commits/efb8b641eaaf31990d34d6e311ce3cb21d60d880)

cast_directional_light removes the lighting appearance, because it's
gonna modify it, but it turns out because appearances are static when
they're in like underlays/overlays, this could remove the WRONG UNDERLAY

This lead to double held flashlights just... not working until you
rotated. V stupid.

I've also had to move the flag set to make the overlay add in
cast_directional_light work. Depression

## Why It's Good For The Game

Closes #73535, closes #73517, closes #73518, and fixes part of #73471
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
fix: Fixes activating two flashlights without moving only turning on one
flashlight (until you move)
fix: Purely black things drawn on the floor (like carpets, those foam
dispensers, etc) will no longer cause things on top of them to be fully
masked in darkness
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [UOA-FSAE/f1tenth](https://github.com/UOA-FSAE/f1tenth)@[7eb490ce96...](https://github.com/UOA-FSAE/f1tenth/commit/7eb490ce96c2dd7d37eb199bfd55d9847b7a2d07)
#### Thursday 2023-03-02 03:07:52 by chris17432

I HATE MY LIFE SOME ONE PLZ FIX THE CATKIN AND ROSDEP STUFF

---
## [milk-is-cool/Yogstation](https://github.com/milk-is-cool/Yogstation)@[8a87301c84...](https://github.com/milk-is-cool/Yogstation/commit/8a87301c84287ec6f2e1549ba3bb67e071065a63)
#### Thursday 2023-03-02 03:35:43 by Vaelophis Nyx

[ASTEROID] Atmos Approved: Atmospherics Changes + More (#16111)

* Update AsteroidStation.dmm

* Update AsteroidStation.dmm

* Update AsteroidStation.dmm

* guh

* fuck you mapbot

* need that to breathe!

* Update AsteroidStation.dmm

* Update AsteroidStation.dmm

* Update AsteroidStation.dmm

---
## [Gboster-0/lobotomy-corp13](https://github.com/Gboster-0/lobotomy-corp13)@[582f5b38cb...](https://github.com/Gboster-0/lobotomy-corp13/commit/582f5b38cb9ad5d051cbea48af501089ba3f0206)
#### Thursday 2023-03-02 03:55:10 by Lance

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
## [olive-editor/olive](https://github.com/olive-editor/olive)@[066a10e6a0...](https://github.com/olive-editor/olive/commit/066a10e6a09b47d0046b27aceef56405ebe2ff13)
#### Thursday 2023-03-02 04:14:28 by itsmattkc

timeline: avoid duplicate items or item dependencies when pasting

God damn this was a big oof. Pasting was inadvertently making duplicates of the footage node(s) every single time. Worst case was if the clip was connected to a nested sequence. Every time someone copy/pasted in my large-scale project, it would add another 1000 nodes to the project. It's about fucking time this was fixed.

---
## [Dudemanguy/mpv](https://github.com/Dudemanguy/mpv)@[3d459832a8...](https://github.com/Dudemanguy/mpv/commit/3d459832a88a9bd2835b339cf6ca98f84aad0115)
#### Thursday 2023-03-02 04:14:32 by Dudemanguy

x11: support xorg present extension

This builds off of present_sync which was introduced in a previous
commit to support xorg's present extension in all of the X11 backends
(sans vdpau) in mpv. It turns out there is an Xpresent library that
integrates the xorg present extention with Xlib (which barely anyone
seems to use), so this can be added without too much trouble. The
workflow is to first setup the event by telling Xorg we would like to
receive PresentCompleteNotify (there are others in the extension but
this is the only one we really care about). After that, just call
XPresentNotifyMSC after every buffer swap with a target_msc of 0. Xorg
then returns the last presentation through its usual event loop and we
go ahead and use that information to update mpv's values for vsync
timing purposes. One theoretical weakness of this approach is that the
present event is put on the same queue as the rest of the XEvents. It
would be nicer for it be placed somewhere else so we could just wait
on that queue without having to deal with other possible events in
there. In theory, xcb could do that with special events, but it doesn't
really matter in practice.

Unsurprisingly, this doesn't work on NVIDIA. Well NVIDIA does actually
receive presentation events, but for whatever the calculations used make
timings worse which defeats the purpose. This works perfectly fine on
Mesa however. Utilizing the previous commit that detects Xrandr
providers, we can enable this mechanism for users that have both Mesa
and not NVIDIA (to avoid messing up anyone that has a switchable
graphics system or such). Patches welcome if anyone figures out how to
fix this on NVIDIA.

Unlike the EGL/GLX sync extensions, the present extension works with any
graphics API (good for vulkan since its timing extension has been in
development hell). NVIDIA also happens to have zero support for the
EGL/GLX sync extensions, so we can just remove it with no loss. Only
Xorg ever used it and other backends already have their own present
methods. vo_vdpau VO is a special case that has its own fancying timing
code in its flip_page. This presumably works well, and I have no way of
testing it so just leave it as it is.

---
## [kokizzu/nushell](https://github.com/kokizzu/nushell)@[378a3ae05f...](https://github.com/kokizzu/nushell/commit/378a3ae05f5459a64f97af3781d4336c35652db4)
#### Thursday 2023-03-02 04:16:45 by Kovacsics Robert

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[aee6eb3edf...](https://github.com/treckstar/yolo-octo-hipster/commit/aee6eb3edfe63f932d66fe3cf13230fc4904c600)
#### Thursday 2023-03-02 04:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [yogstation13/Yogstation](https://github.com/yogstation13/Yogstation)@[8e3e0b1450...](https://github.com/yogstation13/Yogstation/commit/8e3e0b1450189ebda3b2bc760c036ba6c59c6b6a)
#### Thursday 2023-03-02 04:52:55 by LazennG

adds magmite crusher to the things you can make at the world anvil (#17530)

* FUCK YOU PLASMA CUTTER

* updated it now just waiting on BAIOMU FOR FUCKIN SPRITES

* returned old sprites i had but it's still lacking 1 handed versions

* touched up some of the sprites but STILL NEED ONEHANDED ONES FROM BAIOMU

* FINALLY

---
## [WilldooIT/odoo](https://github.com/WilldooIT/odoo)@[639cfc76ba...](https://github.com/WilldooIT/odoo/commit/639cfc76ba259eea8f38284192017024809173b3)
#### Thursday 2023-03-02 05:28:08 by Romain Derie

[FIX] website: redirect to case insensitive URL if not exact match

Before this commit, if a link to a page was not correct because of a
case mismatch, it would simply land on a 404 page.
While it's correct, as URL are case sensitive, it leads to a few bad UX
flow at the admin/editor level:
- Create a link in your page (on a text or a button eg), type an URL
  which does not exists (to create it after) like /Page
- Click on the link/button you just made, you are redirected to /Page
  which display a 404 with the "Create page" option (correct)
- When you click on that button, it will actually create a page with
  /page URL, leading to a mismatch between the URL you created and the
  page URL.
  Your link/button will still lead to a 404 URL as it points to /Page.

Since it's just a fallback when an exact URL match is not found, it
should not break anything and should not have bad impact at any level
(seo/speed etc).
Indeed:
- It's done through a 302 redirect
- `_serve_page()` is already a fallback case, so it will only make
  the `website.redirect` and 404 cases a bit slower due to the extra
  search query.

The only possible scenario seems to be if the user (mind the uppercase):
- Created a /Page page
- Created a redirect from /page to /another-page

In this case, /page won't land on /another-page but on /Page.
This flow seems unlikely and is not actually wrong either way.
At least, it certainly is less important than ensuring a case
insensitive fallback.

Finally, note that another solution would have been to either:
- Force page URL to lower case.
  -> This is not stable friendly, people might be relying on this to
     create pages with different casing:
     `/Batman-VII-The-Dark-Knight-Whatevers`, while not recommended,
     doesn't sounds idiot.
     On top of not being stable friendly, we probably want to keep
     offering this possibility
- Redirect all URLs to lowercase endpoints.
  -> This is obviously not stable and not Odoo's jobs. It should be
     something decided by the sysadmin and done at nginx (etc) level.

task-3110294
opw-3104030

closes odoo/odoo#109812

Signed-off-by: Quentin Smetz (qsm) <qsm@odoo.com>

---
## [peff/git](https://github.com/peff/git)@[f64a46817d...](https://github.com/peff/git/commit/f64a46817ded16f5fa653ac19c04f78bfdd2b69d)
#### Thursday 2023-03-02 06:00:41 by Jeff King

commit: give a hint when a commit message has been abandoned

If we launch an editor for the user to create a commit
message, they may put significant work into doing so.
Typically we try to check common mistakes that could cause
the commit to fail early, so that we die before the user
goes to the trouble.

We may still experience some errors afterwards, though; in
this case, the user is given no hint that their commit
message has been saved. Let's tell them where it is.

Signed-off-by: Jeff King <peff@peff.net>

---
## [peff/git](https://github.com/peff/git)@[8fd720c01f...](https://github.com/peff/git/commit/8fd720c01f99e24cfb63f1e1a9e1aabfd9555b15)
#### Thursday 2023-03-02 06:00:49 by Jeff King

ahead-behind: do not die when we see no INTERESTING pending object

We currently die if we are fed an ahead/behind with zero
objects (`foo..foo` in the most basic case, but in practice
something like `foo@{upstream}..foo`, when `foo` has just
been merged).  The problem is that we let
`handle_revision_arg` parse it, and then pick the pieces out
of the pending object list. So "^foo" looks no different to
us there than "foo".

This patch hacks around it by picking up the UNINTERESTING
object in that case. However, this isn't great because:

  1. Now we won't notice some types of bogus input.

  2. We end up reporting the name of the UNINTERESTING object.

We probably should pick apart the ".." ourselves, or even
just change it to ":" or whitespace.

Signed-off-by: Jeff King <peff@peff.net>

---
## [Davchikk/Shiptest](https://github.com/Davchikk/Shiptest)@[31eabb62f1...](https://github.com/Davchikk/Shiptest/commit/31eabb62f1bfe944a58fa6b74d1745cf80cb83aa)
#### Thursday 2023-03-02 06:11:08 by spockye

The Crashed Starwalker (#1700)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR adds a beach ruin based around a ship I've previously made,
called the "Starwalker"

![2023 01 16-16 33
48](https://user-images.githubusercontent.com/79304582/212715120-1234050a-b91c-411c-b792-82d0621cc549.png)

![2023 01 16-16 35
19](https://user-images.githubusercontent.com/79304582/212715457-6b643815-ab0f-4962-9222-1a0d6eeb7535.png)


it contains:
some medical supplies ( oinment slurry / herbal pack / crew monitor /
health scanner / charcoal bottle / misc pills )
one Swat suit
one shotgun / one energy cutlass
goliath cloak  / military rig
3 abandoned crates
1 gold crate / one silver crate
lizard wine
one baby carp
a radiant dance machine
a sci protolathe
misc salvage


Lore bit:
After a "most excellent robbery that went like, totally as planned", our
protagonists aboard the Starwalker fled the crime scene, with heavy
damage to the ship's hull. With one of the Engine blocks almost falling
off, The valiant crew decided that the best course of action would be a
"Totally rad emergency landing". This, of course, ended in disaster, as
the pilot was high on LSD.
The pilot did however manage to steer them towards a nearby lak- sike,
it's just some shallow water. Crashing directly onto the ground, the
ship split into multiple fragments, Killing the pilot and crewmate, and
Impaling the captain.
The captain knew that he didn't have long until the bloodloss would get
to him, and started moving all his treasure into a nearby cavern.
_THERE'S NO WAY_ he would die in that godforsaken ship, nor without his
treasures. This is where you now find him, rotting in his "100% real Cow
skin" throne _(spacemart Brand Comfy chair)_ .
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
currently there's a bit of a lack in beach ruins, something that I'd
like to help resolve!
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Adds a new Beach ruin, the beach_crashed_starwalker
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
## [xuv8r/orbstation](https://github.com/xuv8r/orbstation)@[fedf2f3a26...](https://github.com/xuv8r/orbstation/commit/fedf2f3a26869848f5fc8f41381d1aff944ed9f6)
#### Thursday 2023-03-02 07:08:20 by Sol N

more span macro changes in brain traumas and disease files (#73273)

## About The Pull Request

i was fucking around with brain traumas on a downstream and noticed they
had similar issues to quirks so i decided to continue work from #73116


![Code_Klx14O288V](https://user-images.githubusercontent.com/116288367/217046732-765ffe27-73c9-416a-833e-e0d9e2aa7a86.png)
(search in VSC for span class = 'notice')
its going to be a bit of a thing to get all of these but this is a
decent chunk i think

there was only one annoying/tough file.
imaginary_friend.dm had class = 'game say' and class = 'emote' both of
which after some testing did not seem like they did anything. ill try to
keep that in mind in other files if i continue to do this but i either
omitted them because they didnt have any formatting or, in the case of
emote, turned it into name, which i think is what you'd want those
messages to look like.

there were also a few small spelling errors that i fixed

## Why It's Good For The Game

more consistent and stops people from copying brain trauma formatting
wrong

## Changelog

they should all work the same

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [dr3ams/Roguelike-Adventures-and-Dungeons-2](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2)@[457271f8c4...](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2/commit/457271f8c4c23e3d72cd1dc062e5073913fdfa53)
#### Thursday 2023-03-02 07:32:35 by VanyaBaou

greek fantasy adjustments

removed unobtainable stuff
-gorgos
-apollo/artemis bow, dev is dipshit and deleted them from datapack and hopped versions in attempt to get more downloads, yeah im pissed

snakeskin now attached to Drakaina quest
bronze -> ichor-infused, because again dev hates his fans, deleted all 1.16 wiki info
kill neutral/passive/friendly -> observer
+winged sandals quest
+palladium quest, with some info on how it works
idk what else im tired man

---
## [Lants/bluefoot](https://github.com/Lants/bluefoot)@[a74f838203...](https://github.com/Lants/bluefoot/commit/a74f838203a5ed19176a126dc131bc896d50478d)
#### Thursday 2023-03-02 08:07:43 by Robin Mathison

im so fucking confused why this shit dont work boutta fight god on jah

---
## [amir73il/linux](https://github.com/amir73il/linux)@[a5434b7695...](https://github.com/amir73il/linux/commit/a5434b76952ee79ededc9244bd9321b68f5c9084)
#### Thursday 2023-03-02 08:30:39 by Yang Xu

fs: move S_ISGID stripping into the vfs_*() helpers

commit 1639a49ccdce58ea248841ed9b23babcce6dbb0b upstream.

[remove userns argument of helpers for 5.10.y backport]

Move setgid handling out of individual filesystems and into the VFS
itself to stop the proliferation of setgid inheritance bugs.

Creating files that have both the S_IXGRP and S_ISGID bit raised in
directories that themselves have the S_ISGID bit set requires additional
privileges to avoid security issues.

When a filesystem creates a new inode it needs to take care that the
caller is either in the group of the newly created inode or they have
CAP_FSETID in their current user namespace and are privileged over the
parent directory of the new inode. If any of these two conditions is
true then the S_ISGID bit can be raised for an S_IXGRP file and if not
it needs to be stripped.

However, there are several key issues with the current implementation:

* S_ISGID stripping logic is entangled with umask stripping.

  If a filesystem doesn't support or enable POSIX ACLs then umask
  stripping is done directly in the vfs before calling into the
  filesystem.
  If the filesystem does support POSIX ACLs then unmask stripping may be
  done in the filesystem itself when calling posix_acl_create().

  Since umask stripping has an effect on S_ISGID inheritance, e.g., by
  stripping the S_IXGRP bit from the file to be created and all relevant
  filesystems have to call posix_acl_create() before inode_init_owner()
  where we currently take care of S_ISGID handling S_ISGID handling is
  order dependent. IOW, whether or not you get a setgid bit depends on
  POSIX ACLs and umask and in what order they are called.

  Note that technically filesystems are free to impose their own
  ordering between posix_acl_create() and inode_init_owner() meaning
  that there's additional ordering issues that influence S_SIGID
  inheritance.

* Filesystems that don't rely on inode_init_owner() don't get S_ISGID
  stripping logic.

  While that may be intentional (e.g. network filesystems might just
  defer setgid stripping to a server) it is often just a security issue.

This is not just ugly it's unsustainably messy especially since we do
still have bugs in this area years after the initial round of setgid
bugfixes.

So the current state is quite messy and while we won't be able to make
it completely clean as posix_acl_create() is still a filesystem specific
call we can improve the S_SIGD stripping situation quite a bit by
hoisting it out of inode_init_owner() and into the vfs creation
operations. This means we alleviate the burden for filesystems to handle
S_ISGID stripping correctly and can standardize the ordering between
S_ISGID and umask stripping in the vfs.

We add a new helper vfs_prepare_mode() so S_ISGID handling is now done
in the VFS before umask handling. This has S_ISGID handling is
unaffected unaffected by whether umask stripping is done by the VFS
itself (if no POSIX ACLs are supported or enabled) or in the filesystem
in posix_acl_create() (if POSIX ACLs are supported).

The vfs_prepare_mode() helper is called directly in vfs_*() helpers that
create new filesystem objects. We need to move them into there to make
sure that filesystems like overlayfs hat have callchains like:

sys_mknod()
-> do_mknodat(mode)
   -> .mknod = ovl_mknod(mode)
      -> ovl_create(mode)
         -> vfs_mknod(mode)

get S_ISGID stripping done when calling into lower filesystems via
vfs_*() creation helpers. Moving vfs_prepare_mode() into e.g.
vfs_mknod() takes care of that. This is in any case semantically cleaner
because S_ISGID stripping is VFS security requirement.

Security hooks so far have seen the mode with the umask applied but
without S_ISGID handling done. The relevant hooks are called outside of
vfs_*() creation helpers so by calling vfs_prepare_mode() from vfs_*()
helpers the security hooks would now see the mode without umask
stripping applied. For now we fix this by passing the mode with umask
settings applied to not risk any regressions for LSM hooks. IOW, nothing
changes for LSM hooks. It is worth pointing out that security hooks
never saw the mode that is seen by the filesystem when actually creating
the file. They have always been completely misplaced for that to work.

The following filesystems use inode_init_owner() and thus relied on
S_ISGID stripping: spufs, 9p, bfs, btrfs, ext2, ext4, f2fs, hfsplus,
hugetlbfs, jfs, minix, nilfs2, ntfs3, ocfs2, omfs, overlayfs, ramfs,
reiserfs, sysv, ubifs, udf, ufs, xfs, zonefs, bpf, tmpfs.

All of the above filesystems end up calling inode_init_owner() when new
filesystem objects are created through the ->mkdir(), ->mknod(),
->create(), ->tmpfile(), ->rename() inode operations.

Since directories always inherit the S_ISGID bit with the exception of
xfs when irix_sgid_inherit mode is turned on S_ISGID stripping doesn't
apply. The ->symlink() and ->link() inode operations trivially inherit
the mode from the target and the ->rename() inode operation inherits the
mode from the source inode. All other creation inode operations will get
S_ISGID handling via vfs_prepare_mode() when called from their relevant
vfs_*() helpers.

In addition to this there are filesystems which allow the creation of
filesystem objects through ioctl()s or - in the case of spufs -
circumventing the vfs in other ways. If filesystem objects are created
through ioctl()s the vfs doesn't know about it and can't apply regular
permission checking including S_ISGID logic. Therfore, a filesystem
relying on S_ISGID stripping in inode_init_owner() in their ioctl()
callpath will be affected by moving this logic into the vfs. We audited
those filesystems:

* btrfs allows the creation of filesystem objects through various
  ioctls(). Snapshot creation literally takes a snapshot and so the mode
  is fully preserved and S_ISGID stripping doesn't apply.

  Creating a new subvolum relies on inode_init_owner() in
  btrfs_new_subvol_inode() but only creates directories and doesn't
  raise S_ISGID.

* ocfs2 has a peculiar implementation of reflinks. In contrast to e.g.
  xfs and btrfs FICLONE/FICLONERANGE ioctl() that is only concerned with
  the actual extents ocfs2 uses a separate ioctl() that also creates the
  target file.

  Iow, ocfs2 circumvents the vfs entirely here and did indeed rely on
  inode_init_owner() to strip the S_ISGID bit. This is the only place
  where a filesystem needs to call mode_strip_sgid() directly but this
  is self-inflicted pain.

* spufs doesn't go through the vfs at all and doesn't use ioctl()s
  either. Instead it has a dedicated system call spufs_create() which
  allows the creation of filesystem objects. But spufs only creates
  directories and doesn't allo S_SIGID bits, i.e. it specifically only
  allows 0777 bits.

* bpf uses vfs_mkobj() but also doesn't allow S_ISGID bits to be created.

The patch will have an effect on ext2 when the EXT2_MOUNT_GRPID mount
option is used, on ext4 when the EXT4_MOUNT_GRPID mount option is used,
and on xfs when the XFS_FEAT_GRPID mount option is used. When any of
these filesystems are mounted with their respective GRPID option then
newly created files inherit the parent directories group
unconditionally. In these cases non of the filesystems call
inode_init_owner() and thus did never strip the S_ISGID bit for newly
created files. Moving this logic into the VFS means that they now get
the S_ISGID bit stripped. This is a user visible change. If this leads
to regressions we will either need to figure out a better way or we need
to revert. However, given the various setgid bugs that we found just in
the last two years this is a regression risk we should take.

Associated with this change is a new set of fstests to enforce the
semantics for all new filesystems.

Link: https://lore.kernel.org/ceph-devel/20220427092201.wvsdjbnc7b4dttaw@wittgenstein [1]
Link: e014f37db1a2 ("xfs: use setattr_copy to set vfs inode attributes") [2]
Link: 01ea173e103e ("xfs: fix up non-directory creation in SGID directories") [3]
Link: fd84bfdddd16 ("ceph: fix up non-directory creation in SGID directories") [4]
Link: https://lore.kernel.org/r/1657779088-2242-3-git-send-email-xuyang2018.jy@fujitsu.com
Suggested-by: Dave Chinner <david@fromorbit.com>
Suggested-by: Christian Brauner (Microsoft) <brauner@kernel.org>
Reviewed-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-and-Tested-by: Jeff Layton <jlayton@kernel.org>
Signed-off-by: Yang Xu <xuyang2018.jy@fujitsu.com>
[<brauner@kernel.org>: rewrote commit message]
Signed-off-by: Christian Brauner (Microsoft) <brauner@kernel.org>
Signed-off-by: Amir Goldstein <amir73il@gmail.com>

---
## [harryob/cmss13](https://github.com/harryob/cmss13)@[34daca112c...](https://github.com/harryob/cmss13/commit/34daca112ce6a08b8edfee14811e9c384429ec4e)
#### Thursday 2023-03-02 11:25:58 by Segrain

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
## [harryob/cmss13](https://github.com/harryob/cmss13)@[fc1e2e5e26...](https://github.com/harryob/cmss13/commit/fc1e2e5e26259773038df05c5405cb80441b8cc2)
#### Thursday 2023-03-02 11:25:58 by riot

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
## [argilla-io/argilla](https://github.com/argilla-io/argilla)@[4c5f51377e...](https://github.com/argilla-io/argilla/commit/4c5f51377e374fb30649bdc7b9a3291db21c5bb8)
#### Thursday 2023-03-02 12:05:34 by Tom Aarsen

Use `rich` for logging, tracebacks, printing, progressbars (#2350)

Closes #1843

Hello!

## Pull Request overview
* Use [`rich`](https://github.com/Textualize/rich) for logging,
tracebacks, printing and progressbars.
* Add `rich` as a dependency.
* Remove `loguru` as a dependency and remove all mentions of it in the
codebase.
* Simplify logging configuration according to the logging documentation.
* Update logging tests.

## Before & After
[`rich`](https://github.com/Textualize/rich) is a large Python library
for very colorful formatting in the terminal. Most importantly (in my
opinion), it improves the readability of logs and tracebacks. Let's go
over some before-and-afters:
<details><summary>Printing, Logging & Progressbars</summary>

### Before:

![image](https://user-images.githubusercontent.com/37621491/219089678-e57906d3-568d-480e-88a4-9240397f5229.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219089826-646d57a6-7e5b-426f-9ab1-d6d6317ec885.png)

Note that for the logs, the repeated information on the left side is
removed. Beyond that, the file location from which the log originates is
moved to the right side. Beyond that, the progressbar has been updated,
ahd the URL in the printed output has been highlighted automatically.

</details>

<details><summary>Tracebacks</summary>

### Before:

![image](https://user-images.githubusercontent.com/37621491/219090868-42cfe128-fd98-47ec-9d38-6f6f52a21373.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219090903-86f1fe11-d509-440d-8a6a-2833c344707b.png)

---

### Before:

![image](https://user-images.githubusercontent.com/37621491/219091343-96bae874-a673-4281-80c5-caebb67e348e.png)

### After:

![image](https://user-images.githubusercontent.com/37621491/219091193-d4cb1f64-11a7-4783-a9b2-0aec1abb8eb7.png)

---

### Before

![image](https://user-images.githubusercontent.com/37621491/219091791-aa8969a1-e0c1-4708-a23d-38d22c2406f2.png)

### After

![image](https://user-images.githubusercontent.com/37621491/219091878-e24c1f6b-83fa-4fed-9705-ede522faee82.png)

</details>

## Notes
Note that there are some changes in the logging configuration. Most of
all, it has been simplified according to the note from
[here](https://docs.python.org/3/library/logging.html#logging.Logger.propagate).
In my changes, I only attach our handler to the root logger and let
propagation take care of the rest.

Beyond that, I've set `rich` to 13.0.1 as newer versions experience a
StopIteration error like discussed
[here](https://github.com/Textualize/rich/issues/2800#issuecomment-1428764064).

I've replaced `tqdm` with `rich` Progressbar when logging. However, I've
kept the `tqdm` progressbar for the [Weak
Labeling](https://github.com/argilla-io/argilla/blob/develop/src/argilla/labeling/text_classification/weak_labels.py)
for now.

One difference between the old situation and now is that all of the logs
are displayed during `pytest` under "live log call" (so, including
expected errors), while earlier only warnings were shown.

## What to review?
Please do the following when reviewing:
1. Ensuring that `rich` is correctly set to be installed whenever
someone installs `argilla`. I always set my dependencies explicitly in
setup.py like
[here](https://github.com/nltk/nltk/blob/develop/setup.py#L115) or
[here](https://github.com/huggingface/setfit/blob/78851287535305ef32f789c7a87004628172b5b6/setup.py#L47-L48),
but the one for `argilla` is
[empty](https://github.com/argilla-io/argilla/blob/develop/setup.py),
and `pyproject.toml` is used instead. I'd like for someone to look this
over.
2. Fetch this branch and run some arbitrary code. Load some data, log
some data, crash some programs, and get an idea of the changes.
Especially changes to loggers and tracebacks can be a bit personal, so
I'd like to get people on board with this. Otherwise we can scrap it or
find a compromise. After all, this is also a design PR.
3. Please have a look at my discussion points below.

## Discussion
`rich` is quite configurable, so there's some changes that we can make
still.
1. The `RichHandler` logging handler can be modified to e.g. include
rich tracebacks in their logs as discussed
[here](https://rich.readthedocs.io/en/latest/logging.html#handle-exceptions).
Are we interested in this?
2. The `rich` traceback handler can be set up to include local variables
in its traceback:
<details><summary>Click to see a rich traceback with local
variables</summary>


![image](https://user-images.githubusercontent.com/37621491/219096029-796b57ee-2f1b-485f-af35-c3effd44200b.png)
    </details>
Are we interested in this? I think this is a bit overkill in my opinion.
3. We can suppress frames from certain Python modules to exclude them
from the rich tracebacks. Are we interested in this?
4. The default rich traceback shows a maximum of 100 frames, which is a
*lot*. Are we interested in reducing this to only show the first and
last X?
5. The progress bar doesn't automatically stretch to fill the full
available width, while `tqdm` does. If we want, we can set `expand=True`
and it'll also expand to the entire width. Are we interested in this?
6. The progress "bar" does not need to be a bar, we can also use e.g. a
spinner animation. See some more info
[here](https://rich.readthedocs.io/en/latest/progress.html#columns). Are
we interested in this?

---

**Type of change**

- [x] Refactor (change restructuring the codebase without changing
functionality)

**How Has This Been Tested**

I've updated the tests according to my changes.

**Checklist**

- [x] I have merged the original branch into my forked branch
- [ ] I added relevant documentation
- [x] follows the style guidelines of this project
- [x] I did a self-review of my code
- [x] I added comments to my code
- [ ] I made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my
feature works

- Tom Aarsen

---
## [dr3ams/Roguelike-Adventures-and-Dungeons-2](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2)@[9681b268db...](https://github.com/dr3ams/Roguelike-Adventures-and-Dungeons-2/commit/9681b268db0bac4b61decab1ca6af61ababd50f3)
#### Thursday 2023-03-02 12:07:23 by dr3ams

1.1 pre-release

Update summary:
- Quest changes:
	- Added guide on how to get to tropicraft
	- Added guide to make undergarden portal
	- Added guide to glider and goddess statue
	- split enchantment quest into multiple sections
	- basic good nights sleep quest setup
	- Greek fantasy pegasus taming guide
	- Guide to atum portal
	- guide to reforging
	- More Mob Kill Quests and expanded Gateway quest
	- nether quest chapter overhaul
	- changed checkmarks > observations in Alex mobs quest chapter
	- greek fantasy chapter fixes & adjustments
	- 6m obsidian > optional, yw 100%'ers (this is a buff)
	- added info to backpack that nobody will read (like this changelog :feelsbadman:)
	- acquisiton methods for coins
	- specialization "clarification"
	- undergarden ore quests
	- added info people wont read about infusion + repairing with anvil & hammer
	- misc fixes
- Buff to human companions health
- Increased ftbackup timer and reduced kept backups
- no soulbond in enchantment table
- Login/spawn protection time increase (thanks to @Chkoupinator)
- Added End Slimes to the champions blacklist (thanks to @Chkoupinator)
- Looting now affects champion coins (but not by very much)
	- Copper Coin: +1% chance per looting
	- Iron Coin: +0.75% chance per looting
	- Gold/Monster/Nether Coin: +0.5% chance per looting
- New Title for defeating the 6 Star Champion
- Added Wolfs to Cursed Ring Neutral Anger Blacklist
- Anubis's Wrath and Reaper's Scythe can now harvest souls for dungeons gear artifacts.
- Fixed Neptunium Pickaxe & Shovel getting a 50 woodcutting requirement when underwater
- Made it so dragon steel bees, netherite bee, and draconic bee no longer spawn in bumble zone. Buffed wrath of the hive
- Fixes the exploit of skipping the wither to bypass getting he more challenging Champions
- End now requires you to kill an ender dragon to escape the main island. Stages are per player
- Tin and Undergarden Ores can now be used in the End Stone Smelter to boost the amount of ingots you get.
- Custom Gateways
	- Added 9 new gateways
		- Atum: Arthropods (Small Gate)
		- Atum: Undead (Medium Gate)
		- Ice and Fire: Dread (Medium and Large Gate)
		- Greek Fantasy: Minotaur (Medium Gate)
		- Greek Fantasy: Nemean Lion (Large Gate)
		- Undergarden: Rotspawn (Medium Gate)
		- Twilight Forest: Knight Stronghold (Medium Gate, and before anyone asks no blockchain goblin because it causes a crash)
		- Twilight Forest: Final Castle Dwellers (Large Gate)
	- Small gateway recipes require spirit orbs instead of ender pearls
	- Medium gateway recipes require ectoplasm orbs instead of eyes of ender
	- Ectoplasm from cofh_core renamed to Ectoplasm Orbs
	- Ectoplasm orbs are crafted from 1 ectoplasm & a spirit orb
- updated feedback users (thanks @VanyaBaou )
- Blacklisted Scarab from Champions
- "disabled" potion charm of flight
- Ore Magnet Durability buffed to 64
- Breaking a monster box drops 1 spirit orb, just like monster spawners
- Monster Boxes spawn in more dimensions but extra loot was disabled
- undead army adjustments: 2x kill req to start, inactive duration 15m > 10m
- BYG Travertine recipe fix
- Green Sconce recipe
- Green Sconce and Amethyst Arrow show in JEI
- Spartan Twilight weapons have same xp bonus as the base twilight forest sword
- Twilight Scepter gives a magic bonus to encourage players to use it as their first magic weapon
- nerfed blobfish
- disabled PotionofRecallEnabled

---
## [ilammy/themis](https://github.com/ilammy/themis)@[eac726f812...](https://github.com/ilammy/themis/commit/eac726f8121a68caa53bf7147bca81f29679ddba)
#### Thursday 2023-03-02 12:23:05 by Oleksii Lozovskyi

CI: Remove Carthage distractions (#990)

Carthage has this retarded tendency to build every Xcode project it
sees when building dependencies. So when we do "carthage bootstrap"
during example builds, it downloads dependencies (Themis repo),
then proceeds to build the dependencies -- but instead of building
only Themis.xcodeproj in the root, Carthage decides that after that
it gotta build every other Xcode project there as well, why not.
Eventually it times out and dies.

This very frustrating, but Carthage people think this is fine,
multilanguage monorepos do not exist, and you should not put example
Xcode projects along with the source code. One repo = One library.

Anyway. This seems to help to avoid timeouts and prevent Carthage
from going on adventure. Sadly, builds still take fucking forever
while Carthage fetches the repo, then fetches OpenSSL binaries,
then do it again, then build Themis, then build example, then
repeat that 5 more times for other examples. But at least they
should not hang for 10 minutes and then die 🤞

Similar hack is applied in Bitrise builds, IIRC.

---
## [NetworkManager/NetworkManager](https://github.com/NetworkManager/NetworkManager)@[44b4d8ea2b...](https://github.com/NetworkManager/NetworkManager/commit/44b4d8ea2bf93f3914693aede3ef677b8a8e31c2)
#### Thursday 2023-03-02 12:50:29 by Thomas Haller

platform: always reconfigure IP routes even if removed externally

NML3Cfg is stateful, that means it remembers which address/route it
configured earlier. That is important because the API users of NML3Cfg
only say what the want to configure now, and NML3Cfg needs to remove
addresses/routes that it configured earlier but are no longer to be
present. Also, NetworkManager wants to allow the user to add
addresses/routes externally with `ip addr|route add` and NetworkManager
not removing it. This is a common use case for dispatcher scripts, but
in general, we want to allow other components to add addresses/routes.

We try something similar with the removal of routes/addresses managed by
NetworkManager. When NetworkManager adds a route/address, which later
disappears, then we assume that the user intentionally removed the
address/route and take the hint to not re-add it.

However, it doesn't work. It is problematic for two reasons:

- kernel can automatically remove routes. For example, deleting an IPv4
  address that is the prefsrc of a route, will cause kernel to delete
  that route. Sure, we may be unable to re-configure the route at this
  moment, but we shouldn't remember indefinitely that the route is
  supposed to be absent. Rather, we should re-add it when possible.

- kernel is a pain with validating consistencies of routes. For example,
  when a route has a nexthop gateway, then the gateway must be onlink
  (directly reachable), or kernel refuses to add it with "Nexthop has
  invalid gateway". Of course, when removing the onlink route kernel is
  fine leaving the gateway route behind, which it would otherwise refuse
  to add.
  Anyway. Such interdependencies for when kernel rejects adding a route
  with "Nexthop has invalid gateway" are super non-trivial.  We try to
  work around that by always adding the necessary onlink routes. See
  nm_l3_config_data_add_dependent_onlink_routes(). But if the user
  externally removed the dependent onlink route, and NetworkManager
  remembers to not re-adding it, then it will cause ripple effects and
  NetworkManager will also be unable to add the nexthop route.

Trying to preserve absence of routes that NetworkManager think should be
there is not tenable. Don't do it anymore. There was anyway no guarantee
that on the next update NetworkManager wouldn't try to re-add the route
in question. For example, if the route came from DHCP, and the lease
temporarily went away and came back, then NetworkManager probably would
have (correctly) forgotten that the user wished that the route be
absent. It did not work reliably and it just causes problems.

---
## [sunamo/sunamo](https://github.com/sunamo/sunamo)@[53adcdb0ab...](https://github.com/sunamo/sunamo/commit/53adcdb0abf0bc4de12d54fec734e45201bd3f19)
#### Thursday 2023-03-02 12:54:04 by sunamo

I'm someone who loves to enjoy life and tries to focus on real things and real friendships. That's why I live very simply. I'm a jeans and T-shirt kind of girl. I don't spend much time fixing myself up or trying to look cool. I live like a normal person and even though I'm in a very high-profile business, I really don't let it affect the way I live. - Cameron Diaz

---
## [PixelExperience-Devices/device_samsung_sm7125-common](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common)@[bd27c0bf50...](https://github.com/PixelExperience-Devices/device_samsung_sm7125-common/commit/bd27c0bf504c652194300003cf706ef45a2f22e0)
#### Thursday 2023-03-02 13:03:41 by Ruchit

(note to self) dont pick this ye dumb idiot its only for wip branch so you can test shit better k bye

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[6e4aace9a1...](https://github.com/TaleStation/TaleStation/commit/6e4aace9a125ecc4a0318f20374413c9fbe4790f)
#### Thursday 2023-03-02 13:06:17 by TaleStationBot

[MIRROR] [MDB IGNORE] Dangerous Research - The Alternate Sciences Research Center Space Ruin! (#4722)

Original PR: https://github.com/tgstation/tgstation/pull/73544
-----
## About The Pull Request
Adds the space ruin "dangerous_research.dmm" to the game. This ruin was
previously PR'd to two separate codebases ->
https://github.com/shiptest-ss13/Shiptest/pull/528
https://github.com/Skyrat-SS13/Skyrat-tg/pull/5047
It's a fun little lore-heavy ruin. With a few dangers and some
environmental storytelling, as well as a few documents detailing the
events that caused the science experiment to go horribly wrong.
This is absolutely the definitive version of this map, I spent a whole
lot of time redesigning and remapping it to be the gold standard for
space ruins.
## Why It's Good For The Game
We need ruins! This one is fun, has a fun/spooky/slightly edgy story to
tell, and I believe it would help bolster the few space ruins we have.
Map screenshot is below! I think it's best experienced without reading
the lore/seeing the map. If you're interested in experiencing the ruin
in-game, I'd advise against poking around too much!
<details>
<summary> Map screenshot! </summary>


![dangerous_research](https://user-images.githubusercontent.com/73589390/221678503-1235a97b-1325-42a8-ba47-3dfd12c54b86.png)


![dangerous_research2](https://user-images.githubusercontent.com/73589390/221679071-7612bd25-76b3-44cd-91a4-609e8c3b80af.png)


</details>

### Big thanks to Ferro for assistance in proofreading!

## Changelog
:cl: Cheshify, Ferro
add: A new ruin has been detected near the station, what secrets could
it hold?
/:cl:

---------

Co-authored-by: Cheshify <73589390+Cheshify@users.noreply.github.com>

---
## [ensisoft/detonator](https://github.com/ensisoft/detonator)@[fbc32d19f9...](https://github.com/ensisoft/detonator/commit/fbc32d19f99b8371a9d6c5ee31b97681ad180bcc)
#### Thursday 2023-03-02 13:43:53 by Sami Väisänen

Refactor the main game loop throttling and VSYNC in editor

Refactor the main game loop throttling and VSYNC in editor.
Again the fundamental problem is the same as previously, how
to run the application with minimal stuttering while throttling
the CPU usage. Essentially what we want is.

- Scale the performance and CPU usage appropriately according to
  the workload, i.e. how many rendering windows are open.
- Avoid tearing, i.e. showing intermediate rendering results.
- Avoid sucking 100% of a core when there's no need, i.e. avoid
  busy looping.
- Respond to any user input immediately without delay.

The simplest solution is to run the main thread without blocking
but this has the problem that the thread is essentially busy looping
and this ends up burning excessive CPU cycles doing nothing and
subsequently draws more power than is needed. There's a need to
throttle the executiong but without blocking user interactions.
Previously we used a simple thread::sleep_for but obviously this
creates an arbitrary blocking period which will create stutter and
user visible jank at some point. I.e. it doesn't scale.

A related problem is that of using VSYNC (to avoid tearing and) to
provide the heartbeat for throttling. There are two problems here.

1. Hard to get right.
   Using the VBLANK (i.e. swap interval) with multiple windows is
   tricky since with Qt the setting applies to surfaces. This means
   that the setting must be set properly when the surface is created.
   Additionally only a single surface may ever have this property lest
   there be execssive waits. Other problems that play a role is here
   window exposure (undefined to swap on a surface that is not exposed)
   and whether the actual rendering surface has been created/initialized
   or not. Overall this route has been very buggy and difficult to get
   properly working.

2. Maybe VBLANK setting is not used.
   The VBLANK solution cannot be used for throttling the thread
   when the VBLANK is not used even if it did work properly. In other
   words if the user setting is "disable VSYNC" then we're without
   any throttling solution.

3. Bugs/edge cases preventing the use of VBLANK.
   If the rendering window/surface with VSYNC flag is not visible then
   it cannot be used to swap and sync. This means that another
   currently visible/exposed surface would need to be (re)created
   to perform the same operation. This again leads to BUGS (see 1.)

This change removes both trying to use VBLANK for synchronization
and the fallback thread::sleep_for from the main thread. Instead the
throttling is offloaded a secondary thread that posts a new event to
the main thread's event loop at a regular interval. The main thread
then simply wait for *any* event in the main loop and process them
as soon as possible. This however means that there's now no control
regarding tearing. To combat this a platform specific method is used:

- On Windows we now try to use DmwFlush to perform some level
  of VBLANK sync. This is also not a perfect solution since DmwFlush
  can wake up too late and actually is not properly synchronized. A
  more elaborate way would be to try to use D3DKMTWaitForVerticalBlankEvent

- On Linux there's no current implementation, instead the we must again
  fallback on a thread sleep only.

References:
https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/nf-dwmapi-dwmflush
https://bugs.chromium.org/p/chromium/issues/detail?id=467617
https://www.vsynctester.com/firefoxisbroken.html

---
## [gmcastil/microzed](https://github.com/gmcastil/microzed)@[1e1da8ff15...](https://github.com/gmcastil/microzed/commit/1e1da8ff15f9a9dd8d11de960e56524db4abd8f1)
#### Thursday 2023-03-02 14:33:50 by George Castillo

Watchdog timer examples finished, along with a small debugging library

Wow, this was a real tour de force in hardware and software
- First, the Xilinx watchdog timer driver code is crappy and doesn't
  do things in a way that I think is wise.
- The ARM documentation is unclear about this, but at least in this
  processor, the WDT can only be started; attempting to clear the start
  bit doesn't actually do so.  The Xiling SDK driver has a
  XScuWdt_Stop() function, but it doesn't actually do anything.  And
  because of the way that the driver code works, it tells the user
  that the WDT is stopped when it actually isn't.  This is a real drag
  when you discover that the self-test function basically leaves the
  watchdog running in the background.  I suppose if production code uses
  this functionality, as long as the thread that handles restarting the
  watchdog is stable, you'll never really notice. But it isn't by intent
  and it just sort of probably works for most people, which is good
  enough I guess.
- Interrupt handling - this was a great opportunity to figure out how to
  be more complicated with interrupt handling, since the GPIO interrupt
  handler callback prototype (which their interrupt handler calls)
  needed access to the watchdog timer instance.  So I had to create my
  ownd `struct` that contained all of the information necessary for the
  interrupt handler to do its job; was one of those "This is how it has
  to actually work" moments and I knew how it would need to be
  implemented, made some coffee, and then sat down and wrote the 10
  lines of C required to actually do it and it worked the first time
- My perception is that low level programming is not really as hard as
  systems programming, because you don't have to handle lots of
  complicated subjects.  You're sort of the master of your own destiny.
  It also sucks if you are depending upon the layer below you and the
  authors of that layer are garbage.  I'm going to emerge from this
  process in a year or so having dragged myself through an enormous
  portion of the Xilinx SDK and it will be interesting to see what my
  impression of their designers is.

---
## [JonathanBraverDev/better-chess-bot](https://github.com/JonathanBraverDev/better-chess-bot)@[7fd46f9e3f...](https://github.com/JonathanBraverDev/better-chess-bot/commit/7fd46f9e3f79021129858d7b8fa8932cde6f4ea2)
#### Thursday 2023-03-02 14:49:52 by Jonathan Braver

completed the removal of BoardPosition, FINALLY.

fixed a lot of typo-like bugs.
created new headers and support functions.
simplifed many functons due to the structure upgrade.
fixed even more bugs.
made all revelant function pointers const.

well, that took FOREVER to do.
but I think this version of the project is much better.
even ignoring all the bugs i fixed along the way, so much clearer and with fewer (is_white? :) all over the place.
finally fixing what annoyed me about all the functions handlign the position... the position itself.

most of my files each commit be [like]([https://www.google.com](https://media.tenor.com/cJRcMyUAiMcAAAAd/ah-shit-here-we-go-again-ah-shit.gif) "Ah shit, here we go again.")

---
## [Navin136/kernel_asus_sdm660](https://github.com/Navin136/kernel_asus_sdm660)@[eceb9c82f7...](https://github.com/Navin136/kernel_asus_sdm660/commit/eceb9c82f7814788a356eab541bc5d0d47e970e5)
#### Thursday 2023-03-02 15:00:41 by Christian Brauner

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
Signed-off-by: Navin136 <nkwhitehat@gmail.com>

---
## [PA-GK/android_frameworks_base](https://github.com/PA-GK/android_frameworks_base)@[4486773445...](https://github.com/PA-GK/android_frameworks_base/commit/4486773445d1a0e31fcee9563a2e187ba3081b6d)
#### Thursday 2023-03-02 15:18:11 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6

---
## [QuacksQ/STALKER-13](https://github.com/QuacksQ/STALKER-13)@[1ad74ef093...](https://github.com/QuacksQ/STALKER-13/commit/1ad74ef0939fc81f96ea3e4485a0b82406a6d22e)
#### Thursday 2023-03-02 16:18:14 by ProtivogaSpriter

FUCK YOU FUCK YOU

FUCK YOU!!!!

this literally comments out the entire renegades job file

---
## [QuacksQ/STALKER-13](https://github.com/QuacksQ/STALKER-13)@[fa6e6ee157...](https://github.com/QuacksQ/STALKER-13/commit/fa6e6ee1574cec2561d35f89969beaa595f11094)
#### Thursday 2023-03-02 16:18:14 by emoats18

Merge pull request #214 from ProtivogaSpriter/srptotr

FUCK YOU FUCK YOU

---
## [nakunarut/UACME](https://github.com/nakunarut/UACME)@[c65f9215c1...](https://github.com/nakunarut/UACME/commit/c65f9215c1103269ca31f66f49869fcde547af98)
#### Thursday 2023-03-02 16:27:42 by hfiref0x

Update Naka.vcxproj

Retarget platform toolset for appveyor fail. I understand that this service is currently busy supporting %current thing% more than actually working on their script-shit, but holy fuck seriously.

---
## [ShamanSliph/Skyrat-tg](https://github.com/ShamanSliph/Skyrat-tg)@[406b6870bd...](https://github.com/ShamanSliph/Skyrat-tg/commit/406b6870bd28dd78e65e59787d8c54c776078019)
#### Thursday 2023-03-02 17:29:09 by SkyratBot

[MIRROR] adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths [MDB IGNORE] (#18785)

* adds atmospheric gloves, small resprite of firefighter gear, repaths stupid glove paths (#72736)

repaths a lot of gloves off /color because they were incredibly stupid
firefighter gear has gotten an update (it doesnt cover hands anymore
though, you need something else)
firefighter helmets no longer hide your mask or glasses

![image](https://user-images.githubusercontent.com/23585223/212542599-c004d0e4-c141-40b4-a1bb-c838f9893c4b.png)
fixed engine goggles starting with darkness vision
to the atmos lockers adds atmospheric gloves, a pair of thick (chunky
fingers) gloves that are fireproof and fire protective, slightly shock
resistant and let you fireman carry people faster.
atmospheric firefighter helmets now are a subtype of welding hardhats,
you can enable a welding visor.
welding hardhats change mode with right click instead of altclick

im not a good spriter but i think this resprite makes them fit nicer
with other engi equipment
lets me firefighter rp

:cl:
add: Atmospheric Gloves, thick gloves that are fully fireproof and fire
protective and let you fireman carry people faster.
fix: fixes engine goggles starting with darkness vision
qol: firefighter helmets can now enable a welding visor
qol: welding hardhats change mode with right click instead of altclick
balance: firesuits no longer protect your hands
/:cl:

* Makes shit compile

* Updates the digi and snouted stuff to match the new sprites (thanks Halcyon!)

* Fixes a whole ton more issues that popped up

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: GoldenAlpharex <jerego1234@hotmail.com>

---
## [DisturbHerb/Shiptest](https://github.com/DisturbHerb/Shiptest)@[d21740b475...](https://github.com/DisturbHerb/Shiptest/commit/d21740b475aea65de3b250a5aea26a69677e30e8)
#### Thursday 2023-03-02 18:18:26 by tmtmtl30

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
## [payday-restoration/restoration-mod](https://github.com/payday-restoration/restoration-mod)@[e8c7949c86...](https://github.com/payday-restoration/restoration-mod/commit/e8c7949c8624ea9440ac11ce4df2be9a8355b12c)
#### Thursday 2023-03-02 18:28:04 by Noep

things to do

- I love pika as my girlfriend and she has boing boing

- Slightly boosted the pickup rate of <60 damage weapons

- Fix missing desc for underbarrel gas grenades

- Anti-Materiel rifles' total ammo has been halved to account for their 2x headshot damage, similar to how the P90 and MP7 see reduced ammo despite their base damage.
-- >:3's Musket does not have this total ammo reduction as it does not deal bonus headshot damage; it has been moved to the "heavy sniper" buy menu category instead as a result

---
## [Ultimate-Fluff/cmss13](https://github.com/Ultimate-Fluff/cmss13)@[b4954e1402...](https://github.com/Ultimate-Fluff/cmss13/commit/b4954e14028909b107d0b204da0ad06c5dfeb50a)
#### Thursday 2023-03-02 19:13:42 by carlarctg

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
#### Thursday 2023-03-02 19:13:42 by carlarctg

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
## [Ouroboros-Development/rpemotes](https://github.com/Ouroboros-Development/rpemotes)@[45b9259ff8...](https://github.com/Ouroboros-Development/rpemotes/commit/45b9259ff84eea10f91aa0c2b4d122cedf9f7fc9)
#### Thursday 2023-03-02 19:31:25 by Mads

🚶‍♂️Add 11 New Walking Styles (#99) 🚶‍♂️

HUGE thanks to @MadsLeander 

Notes/descriptions of the walking styles:

Bigfoot (move_characters@orleans@core@) - Head hanging slightly forwards, somewhat hurting in left fot, wide with arms as if he's large, walking slow, runs crazy and fast (Used by this character in storymode: https://gta.fandom.com/wiki/Sasquatch_Roleplayer)

Coward (move_m@coward) - Hunched forward when standing still, other wise not diffrent from the default male walk.

Dave (move_characters@dave_n) - Shoulders are higher then normal walk, standing wide when still, left foot hurting when running/jogging (sprint is the default one) (Used by Dave Norton in storymode)

    Femme2 (move_m@femme@) - Shoulders are "swinging", left leg is leaned on when standing still, generally can be best described as a feminine walk for male peds, run and sprint are like the default one (This is one of the avalible walks in GTA Online)

Jimmy (move_characters@jimmy) - Similar to nervous/slow (they are all from the same character afterall), but with out the nervous or slow part (walks normal speed and not tripping with legs when standing still) (Used by Jimmy, the son of Michael in storymode)

Patricia (move_characters@patricia) - Swinging with hips, straight/stiff back, run/sprint is similar to the default female one (Used by Patricia Madrazo in storymode)

Ron (move_characters@ron) - Entire body posture slightly hanging to the left, runs like an idiot, sprint is normal. (Used by Ronald "Ron" Jakowski in storymode)

Swagger2 (move_m@swagger@b) - Confident and somewhat slow walking, moving slightly to the right every so often, run an sprint is normal.

Gangster6 (move_f@gangster@ng) - Slight diffrent in walking speed, posture is noticible diffrent, arms are more straight when standing still.

Veryslow (move_m@leaf_blower) - Head looking down, walking very slowly, running with right arm as if he had a leaf blower, sprint is normal.

Flee5 (move_m@flee@c) - Similar to Flee4, but multiple diffrences like how many times he turns his head to look behind etc.

---
## [happypandax/happypandax](https://github.com/happypandax/happypandax)@[40a2230f75...](https://github.com/happypandax/happypandax/commit/40a2230f754a4a60b3a09b9ef8037d701a711069)
#### Thursday 2023-03-02 20:03:54 by Twiddly

why the fuck would you deprecate yarn install --production with a worse alternative, like what in the dfgfdsg sdfgsdhfsdghasdf holy shit

---
## [gered/libretrogd](https://github.com/gered/libretrogd)@[eb6a363afd...](https://github.com/gered/libretrogd/commit/eb6a363afd71a85f7c686d2155bb9fdb3deb0bf0)
#### Thursday 2023-03-02 20:14:06 by gered

formatting

note that i'm intentionally not using rustfmt. i've tried to like that
tool, but in the end i just really don't like it. too many edge cases
and subjectivity and not enough customization. which is probably the
intent. which makes me hate it that much more. fuck you, rustfmt.

---
## [MMMiracles/tgstation](https://github.com/MMMiracles/tgstation)@[728a0f1b91...](https://github.com/MMMiracles/tgstation/commit/728a0f1b9147197bb81f22d946f67e9d08719d5a)
#### Thursday 2023-03-02 20:35:07 by Jacquerel

Grand Ritual: Alternate Wizard objective (Wizard Events II) (#72918)

Adds an alternate greentext objective for Wizards known as the "Grand
Ritual". This was initially the gimmick of a different wizard-related
antagonist downstream. I didn't get permission to port it, so I'm
attaching it to regular Wizards instead.

Wizards will spawn in with a new Grand Ritual button next to their
antagonist info button. Pressing it will pinpoint them towards their
next Ritual Location (a randomly chosen region of the space station).
Once within that location, pressing it will summon a magic circle and
obliterate any dense objects which are in the way. This also puts the
ability on a two minute cooldown.
Clicking on the magic circle with an empty hand will begin a three-stage
invocation to gather magical power. You can interrupt this invocation at
any time and will resume from the last stage you completed (if you
finished two stages you only need to do one more).
Once you complete a ritual, a random event will be triggered based on
how many rituals you have performed so far. These tend to be ones which
annoy the crew in some manner, and Wizard Events are included in the
list. Additionally, something weird will usually happen to the room you
are in.
Then you are assigned a new location and can toddle off to do it again.

Once you have done this three times, you will be picked up by the
station's sensors every time you start a subsequent ritual and should
expect annoyed company to come investigate.
Once you have done this six times, you can finally spend all of that
accumulated power on the seventh Grand Finale ritual. Completing this
grants you victory at the end of the round and will have a larger,
flashier effect which you can pick from a list of options, think of it
like a wizard equivalent of a Traitor Final Objective or Heretic
Ascension.
After that you can still keep doing rituals if you want to pester the
crew further by summoning more random events, you've already "won" at
this point so now it's your job to make them want to go home.

I think it'd be more fun to just find out what the Finale ritual can do
by seeing it happen but maintainers will probably want a list of its
precise capabilities, so here it is:

Currently completing a ritual also has a chance to create Heretic
Reality Tears (of both varieties, available for Heretics to eat and
visible to crew) as a kind of cross-antagonist interaction which seemed
to make sense to me but if this seems thematically or mechanically
inappropriate it's easy to strip out.

---
## [NetBSD/pkgsrc](https://github.com/NetBSD/pkgsrc)@[186893da25...](https://github.com/NetBSD/pkgsrc/commit/186893da25aefbb8fa48e3215000aaf9db81f3b6)
#### Thursday 2023-03-02 20:52:18 by nikita

gleam: update to version 0.27.0

ChangeLog (taken from https://gleam.run/news/v0.27-hello-panic-goodbye-try/):

Gleam is a type safe and scalable language for the Erlang virtual machine and JavaScript runtimes. Today Gleam v0.27.0 has been released, let’s take a look at what’s new.
Using patterns in use expressions

The Gleam v0.25 release introduced the use expression, a feature that helps avoid “callback hell” in Gleam programs. It is quite powerful and can be used to emulate many features found in other languages such as early returns, list comprehensions, async/await, monadic do syntax, and more!

pub fn handle(req: Request) -> Response {
  // Return an error for non-post requests
  use <- when(req.method != Post, return: method_not_allowed)

  // Parse the request body or return an error
  use json <- require_json_body(req)

  // Open a database connection, closing it when we're done
  use conn <- database.with_connection

  case database.insert(conn, json) {
    Ok(record) -> created_response(record)
    Error(err) -> bad_request_response(err)
  }
}

One limitation of the use expression was that patterns could not be used with their assignments, only bare variables. This means you could not destructure a tuple or other data structure with them.

As of this release patterns are now supported in the use expression, for all your destructuring needs!

use #(first, second) <- some_tuple_function()

Don’t Panic!

This release introduces the panic keyword, a simple little keyword that causes the program to crash. Why would you want to do this?

Your program may not have sufficiently constrainted types to make invalid state unrepresentable. In this case you may want to use panic to crash the program when an invalid state is reached, which is often preferable than silently continuing or programming defensively.

Alternatively you may be embracing the Erlang philosophy of “let it crash” and choosing to use handle unexpected exceptional errors with an Erlang style supervision tree. This strategy is particularly effective when rapidly prototyping or in situations where there is no way to reasonably recover from an error, or client to show an error message to.

case this_should_never_fail() {
  Ok(value) -> continue(value)

  // Oh no! Something went horribly wrong!
  Error(_) -> panic
}

Panic is similar to the assert keyword, only it always crashes rather than conditionally. Speaking of the assert keyword…
Towards a better assert

Gleam’s assert keyword is used to ensure that data matches a given pattern, crashing the program if it does not. This is useful, but using assert for this functionality means that we can’t have an assert feature that works with boolean expressions, as is commonly found in other languages.

To remedy this the pattern matching feature has been moved to this let assert syntax. The existing assert keyword has been deprecated and will later be used for a more conventional assertion feature, to be part of a larger Gleam milestone based around improving the ergonomics of testing Gleam code.

let assert Ok(value) = this_should_never_fail()

Deprecations are annoying, and nobody likes having to fix their code, so the Gleam tooling will automatically upgrade your syntax when you run gleam format or format the code in your editor.
Moving beyond try

try expressions were introduced way back in v0.9 as a way of avoiding callback hell when working with functions that can either return a value or an error. Now that we have use expressions, the less general try expressions are redundant. We always prefer to have fewer ways to do the same thing in Gleam, and fewer things to have to learn, so try expressions are deprecated in this release.

A try expression can be replaced by a use expression with the then function from the gleam/result module. Once try is no longer a keyword the then function will be aliased to try.

// With try
try file = open_file()

// With use
use file <- then(open_file())

// After `try` is removed
use file <- try(open_file())

This is still annoying to fix by hand, so the new gleam fix command has been created to automatically upgrade your code for you.

And that’s it! There’s also lots of other small improvements and bug fixes, so check the full release notes for more details.

Thanks

Gleam is made possible by the support of all the kind people and companies who have very generously sponsored or contributed to the project. Thank you all!

If you like Gleam consider sponsoring or asking your employer to sponsor Gleam development. I work full time on Gleam and your kind sponsorship is how I pay my bills!

    Fly

---
## [FatalUserK/BallGame](https://github.com/FatalUserK/BallGame)@[7d4221b1c3...](https://github.com/FatalUserK/BallGame/commit/7d4221b1c34f73159fa0421699ad94ab3264c47e)
#### Thursday 2023-03-02 21:20:11 by UserK

IT IS DONE

AS PROMETHEUS GAVE FIRE TO MAN TO ILLUMINATE THEIR PATH IN THE DARK, OMIIXI HAS BLESSED ME WITH SIGHT AFTER I REALISE MY FUCKING AWAKE FUNCTIONS WERE TRYING TO ACCESS DATA FROM OTHER AWAKE FUNCTIONS oh yeah and i mostly finished the renderer and GOD its more spaghetti than my kitchen ceiling, will likely rework it heavily in the future, might disable it until then

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[414135da52...](https://github.com/TaleStation/TaleStation/commit/414135da52ca6962366569d2fd62280b8d34aa7a)
#### Thursday 2023-03-02 21:50:56 by TaleStationBot

[MIRROR] [MDB IGNORE] Brings the monkey back down (body horror edition/addition.) (#4701)

Original PR: https://github.com/tgstation/tgstation/pull/73325
-----

## About The Pull Request
Let me paint you a story.
A long time ago monkeys once rested their feet on the floor, this was a
time of bliss and peace. But sometime around the horrors of making
monkeys subtypes of humans did an atrocity occur.

![image](https://user-images.githubusercontent.com/55666666/217657059-5c960ab4-c3de-493c-ac12-28de99b43d7f.png)
**The monkeys were moved up.**
I thought this was bad, and alot of people on the forum tended to agree
with me

![image](https://user-images.githubusercontent.com/55666666/217657707-120354c7-b1a5-4d93-8813-8e10e142bd92.png)
This was do to some purpose of adjusting them so it could be easier to
fit item sprites onto them instead of preforming the hours of work
refractoring to make the heights of the items dynamic and adjustable. A
simple pixel shift may have sufficed, but you see, such a change would
NEVER allow the frankensteining of monkey and human features together.
This is that refractor.

In essence, the following is now true.
A top_offset can now be generated for a human based on a varible on
their chest and legs. By default, and as is true with human legs and
chests, this variable is ZERO by default. Monkey legs and chest have
NEGATIVE values proportionate and onto how much smaller their sprite is
compared to humans. Other bodyparts, as well as any other accociated
overlays, or clothing will automatically be offset to this axis. THIS
MEANS THAT MONKEYS ARE ON THE FLOOR. But is means something else too.
Something more freakish,


![image](https://user-images.githubusercontent.com/55666666/217659439-bc0b1a35-76c8-4490-b869-770180605822.png)
**What abominable monsters**, unreachable by players as long as we can't
stitch monkeys and humans together (oh but just wait until the feature
freeze ends)
Oh but you might be thinking, if legs can make a mob go down.
can it make a mob

**go**
**up??**

**OH NO**


![image](https://user-images.githubusercontent.com/55666666/217707042-0d53022f-d93a-4262-a5ce-ef15a99eb897.png)

![image](https://user-images.githubusercontent.com/55666666/217707060-779f5901-ab90-4a64-9ca7-0b147e24f099.png)

![image](https://user-images.githubusercontent.com/55666666/217707821-23d7457c-5881-40ae-8d9d-c9fbd645aba6.png)

These lads are stepping, and have been implemented solely for proof of
concept as a way to flex the system I have created and remain
inaccessible without admin intervention.

But really, when all is said and done, all this PR does in terms of
player facing changes is move the monkey back down.

![image](https://user-images.githubusercontent.com/55666666/217708365-b6922a6d-08d0-4267-8713-4f8dac29038e.png)
Oh and fixed monkey husked which have been broken for who knows how
long.

![image](https://user-images.githubusercontent.com/55666666/217708464-5a9b6f89-4223-4ae5-a21e-3a274a9f8db8.png)
## Why It's Good For The Game
The monkey is restored to its original position. Tools now exist to have
legs and torsos of varying heights. Monkey Husking is fixed.
## Changelog
:cl: itseasytosee
fix: Monkeys ues the proper husk sprites.
imageadd: The monkey has been moved back down to its lower, more
submissive position.
refactor: Your bodyparts are now dynamically rendered at a height
relevant to the length of your legs and torso, what does this mean for
you? Not much to be honest, but you might see a monkey pop up a bit if
you cut its legs off.
admin: The Tallboy is here
/:cl:

---------

Co-authored-by: itseasytosee <55666666+itseasytosee@users.noreply.github.com>
Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: san7890 <the@san7890.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[0acf3d91d2...](https://github.com/TaleStation/TaleStation/commit/0acf3d91d228510bdac5441e8b3f9b40310d8b8f)
#### Thursday 2023-03-02 21:50:56 by TaleStationBot

[MIRROR] [MDB IGNORE] Don't create abandoned airlocks with walls underneath them. (#4700)

Original PR: https://github.com/tgstation/tgstation/pull/73656
-----
## About The Pull Request
Fixes #71504

#70237 attempted to remove this and did in some cases, however the case
where the abandoned airlock is able to find an adjacent wall turf to
copy the type of still fails to delete the airlock.
This fixes that.

Also in my testing, the times where it _failed_ to find a nearby wall
turf to copy and spawned a default wall would leave the mapping helper
visible in the round. Oops!

## Why It's Good For The Game

Mapping helpers should always delete themselves when finished.
The airlocks with walls under them are funny once and annoying the rest
of the time. As of that older PR, this continuing to happen is regarded
as a bug.
Also apparently it might be required anyway for Wallening.

## Changelog

:cl:
fix: Maintenance tunnels should no longer sometimes contain airlocks
with walls underneath them.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[6179e8667d...](https://github.com/Jolly-66/JollyStation/commit/6179e8667db860af0da1a2c64414d3be1229d9ee)
#### Thursday 2023-03-02 22:05:27 by TaleStationBot

[MIRROR] [MDB IGNORE] Makes Shake() proc work (#4607)

Original PR: https://github.com/tgstation/tgstation/pull/73480
-----
## About The Pull Request

Fixes #72321
Fixes #70388

The shake proc didn't work and hasn't for ages.
I remember it having worked at some point, but it was quite a long time
ago.
I cannot guarantee that the end result here is the same as it was, the
reason here being that I have no idea how this proc ever worked in the
first place. My limited understanding of the `animate` proc implies that
the previous implementation as written would never have acted as you
would expect it to, but clearly at some time in the past it did work. A
mystery.

As a result of the previous, possibly because the proc never _did_ work
as expected and just did something which looked vaguely correct most of
the time, both the default values and the values people were passing
into this proc were completely ridiculous.
Why would anyone ever want to pixel shift an object with a range of _15_
pixels in all directions? That's half a full tile! And why would you
want it to do this for 25 seconds?
So I also changed the values being passed in, because you really want
pretty small numbers passed into here most of the time.

Here's a video of everything that vibrates:
https://www.youtube.com/watch?v=Q0hoqmaXkKA

The exception is the v8 engine. I left this alone because it seems to
try and start shaking while in your hands, which doesn't work, and I
don't know how to fix that. This has potentially _also_ never worked.

## Why It's Good For The Game

Now you can see intended visual indicators for:
- Lobstrosities charging.
- Beepsky being EMPed.
- The Savannah Ivanov preparing to jump.
- The DNA infuser putting someone through the spin cycle.
- The mystery box admin item I had no previous idea even existed (fun
animations on this one).
- Anything else which wants to use this proc to create vibrating objects
in the future.

## Changelog

:cl:
fix: Lobstrosities and Tarantulas will once more vibrate to let you know
they're about to charge at you.
fix: The Savannah Ivanov will once more vibrate to let you know it's
about to jump into the air.
fix: The DNA infuser will now vibrate to let people know that it's busy
blending someone with a dead animal.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Thelema-SS/Thelema-STG](https://github.com/Thelema-SS/Thelema-STG)@[635aee8e34...](https://github.com/Thelema-SS/Thelema-STG/commit/635aee8e346a86ee375d262342057554b973e14b)
#### Thursday 2023-03-02 22:35:48 by SkyratBot

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
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[bdfe69ce9e...](https://github.com/Buildstarted/linksfordevs/commit/bdfe69ce9e8aeb74e0c5966ed3016b6280bc8359)
#### Thursday 2023-03-02 23:08:53 by Ben Dornis

Updating: 3/2/2023 11:00:00 PM

 1. Added: What Are the Enduring Innovations of Lisp?
    (https://elliottslaughter.com/2022/12/lisp)
 2. Added: How I made banditypes, the smallest TS validation library
    (https://blog.thoughtspile.tech/2023/03/02/banditypes-smallest-validation/)
 3. Added: I hire people to work on a FOSS project. Here's how I evaluate GitHub profiles | Ondsel
    (https://ondsel.com/blog/evaluating-github-profile/)
 4. Added: bryan garza
    (https://bryangarza.com/blog/these-magic-code-sequences-will-rot-your-brain/)
 5. Added: Overview | Mina Documentation
    (https://docs.minaprotocol.com/zkapps)
 6. Added: I burnt a cake when I was 12
    (https://kinduff.com/2023/03/01/i-burnt-a-cake-when-i-was-12/)
 7. Added: Journey Through Freedreno
    (https://fryzekconcepts.com/notes/freedreno_journey.html)
 8. Added: Community Created Podcasts – Luke Berndt
    (http://lukeberndt.com/2023/community-created-podcasts/)
 9. Added: I remembered how awful it is to go viral
    (https://www.garbageday.email/p/i-remembered-how-awful-it-is-to-go)
10. Added: The tech tycoon martyrdom charade - Anil Dash
    (https://anildash.com/2023/02/27/tycoon-martyrdom-charade/)
11. Added: Digital Market Act workshop in Brussels
    (https://carlschwan.eu/2023/03/02/digital-market-act-workshop-in-brussels/)

Generation took: 00:08:43.8232970
 Maintenance update - cleaning up homepage and feed

---

