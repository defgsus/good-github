## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-03-15](docs/good-messages/2023/2023-03-15.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,457,288 were push events containing 3,714,607 commit messages that amount to 305,850,747 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 63 messages:


## [dsmith328/LC13Master](https://github.com/dsmith328/LC13Master)@[dd06e8c675...](https://github.com/dsmith328/LC13Master/commit/dd06e8c675cd1703d1daae6e541254134ff11c62)
#### Wednesday 2023-03-15 00:09:36 by Lance

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

Small update

Unnerfs resists

AoE hit fix

Gun update real

more res should mean less talk

Pixel Fix

Sound... Fix?

Broke the staff's legs, fuck those guys.

lmfao audio pains

Gun Rename, Spawn nerf

NO MORE FRIENDS FROM GUN

Faction change

acid tweak

LINT!

SW Code and Balance

SoW Temp commit

Scuff-Fix

SoW bonk update

Hermit range increase and ranged damage decrease

visual fix

Ending adjustments

I forgot to carry the 4

---
## [ElectroJr/space-station-14](https://github.com/ElectroJr/space-station-14)@[581e8a0d12...](https://github.com/ElectroJr/space-station-14/commit/581e8a0d123eca621e52716fd5816966b0569a36)
#### Wednesday 2023-03-15 00:14:04 by eclips_e

Give slimes their sex back (not the ERP one) (#14380)

<!-- Please read these guidelines before opening your PR: https://docs.spacestation14.io/en/getting-started/pr-guideline -->
<!-- The text between the arrows are comments - they will not be visible on your PR. -->

## About the PR
<!-- What does it change? What other things could this impact? -->

Gives back the ability for slimes to have a definitive sex. Cosmetic/visual things such as emotes/other stuff use the person's sex and not the gender and I feel like that the removal of slime's having sexes was just to show that the species refactor could handle unsexed species.

**Media**
<!-- 
PRs which make ingame changes (adding clothing, items, new features, etc) are required to have media attached that showcase the changes.
Small fixes/refactors are exempt.
Any media may be used in SS14 progress reports, with clear credit given.

If you're unsure whether your PR will require media, ask a maintainer.

Check the box below to confirm that you have in fact seen this (put an X in the brackets, like [X]):
-->

- [x] I have added screenshots/videos to this PR showcasing its changes ingame, **or** this PR does not require an ingame showcase

**Changelog**
<!--
Here you can fill out a changelog that will automatically be added to the game when your PR is merged.

Only put changes that are visible and important to the player on the changelog.

Don't consider the entry type suffix (e.g. add) to be "part" of the sentence:
bad: - add: a new tool for engineers
good: - add: added a new tool for engineers

Putting a name after the :cl: symbol will change the name that shows in the changelog (otherwise it takes your GitHub username)
Like so: :cl: PJB
-->

:cl: eclips_e
- fix: Male and female slimes now scream and laugh properly

---
## [mwatts/nushell](https://github.com/mwatts/nushell)@[2e01bf9cba...](https://github.com/mwatts/nushell/commit/2e01bf9cbadf833b4156ec5117393e51b8cadc7d)
#### Wednesday 2023-03-15 00:32:47 by Bob Hyman

add `dirs` command to std lib (#8368)

# Description

Prototype replacement for `enter`, `n`, `p`, `exit` built-ins
implemented as scripts in standard library.
MVP-level capabilities (rough hack), for feedback please. Not intended
to merge and ship as is.

_(Description of your pull request goes here. **Provide examples and/or
screenshots** if your changes affect the user experience.)_

# User-Facing Changes
New command in standard library

```nushell
〉use ~/src/rust/nushell/crates/nu-utils/standard_library/dirs.nu
---------------------------------------------- /home/bobhy ----------------------------------------------
〉help dirs
module dirs.nu -- maintain list of remembered directories + navigate them

todo:
* expand relative to absolute paths (or relative to some prefix?)
* what if user does `cd` by hand?

Module: dirs

Exported commands:
  add (dirs add), drop, next (dirs next), prev (dirs prev), show (dirs show)

This module exports environment.
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs add ~/src/rust/nushell /etc ~/.cargo
-------------------------------------- /home/bobhy/src/rust/nushell --------------------------------------
〉dirs next 2
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │         │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
│ 3 │ ==>     │ ~/.cargo           │
╰───┴─────────┴────────────────────╯
------------------------------------------- /home/bobhy/.cargo -------------------------------------------
〉dirs drop
---------------------------------------------- /home/bobhy ----------------------------------------------
〉dirs show
╭───┬─────────┬────────────────────╮
│ # │ current │        path        │
├───┼─────────┼────────────────────┤
│ 0 │ ==>     │ /home/bobhy        │
│ 1 │         │ ~/src/rust/nushell │
│ 2 │         │ /etc               │
╰───┴─────────┴────────────────────╯
---------------------------------------------- /home/bobhy ----------------------------------------------
〉
```
# Tests + Formatting

Haven't even looked at stdlib `tests.nu` yet.

Other todos:
* address module todos.
* integrate into std lib, rather than as standalone module. Somehow
arrange for `use .../standard_library/std.nu` to load this module
without having to put all the source in `std.nu`?
*  Maybe command should be `std dirs ...`?   
* what else do `enter` and `exit` do that this should do? Then deprecate
those commands.

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
## [kugamo/cmss13](https://github.com/kugamo/cmss13)@[a742c64df9...](https://github.com/kugamo/cmss13/commit/a742c64df98ec4f23eaa64162a2518a91c642ead)
#### Wednesday 2023-03-15 00:40:14 by carlarctg

Fix entering a ghosted xeno not removing ghostize sleep. (#2076)

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

Fix entering a ghosted xeno not removing ghostize sleep.

# Explain why it's good for the game

This sucks ass! Let me wake up!!!!! can KILL you if you enter a xeno in
a difficult situation!!!!!!

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
fix: Fix entering a ghosted xeno not removing ghostize sleep.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[4a9407438a...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/4a9407438aa216789e72a4dec8d6588582d91a8e)
#### Wednesday 2023-03-15 00:49:26 by SkyratBot

[MIRROR] You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed [MDB IGNORE] (#19855)

* You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed (#73983)

## About The Pull Request

If you are restrained, and placed into an unlocked labor camp
teleporter, you cannot instantly resist out of it. However the resist
timer is cut in half while unlocked.

## Why It's Good For The Game

Getting someone into the gulag teleporter is an incredibly un-necessary
pain in the rear because simply *spamming resist* turns it into a game
where you have to shove them in, then really quick go over to the
computer and slam the lock button. This is... kinda lame. A lot of new
player security officers get got by this, and I think it's sad. Inb4
"Skill issue"

## Changelog

:cl: Melbert
balance: If you are handcuffed, you can't instantly resist out of an
unlocked labor camp teleporter (however, resist time is halved).
/:cl:

* You can't instantly resist out of an unlocked labor camp teleporter if you are handcuffed

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[7de062f78e...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/7de062f78e696a11984b134ac6bfca6ca414cc89)
#### Wednesday 2023-03-15 00:51:15 by SkyratBot

[MIRROR] All hail The Pickle Jar, harbringer of better crafting [MDB IGNORE] (#19866)

* All hail The Pickle Jar, harbringer of better crafting (#73939)

## About The Pull Request
Fixes #73841

---

_It is the 12th of March, 2023. Around 3am. I have published a Pull
Request which involves circuits, and got reminded of my low GBP. I go
into the issues tab to see if there's anything someone of my low skill
caliber could tackle. I see it; Pickles.
"How hard could I be?" I ask myself, foolishly unaware of the dangers
that would soon overcome me.
Surely it must've been a mistype, I thought. Surely someone accidentally
confused pickles and cucumbers.
"Wait, the pickles are supposed to be created on the jar when the jar is
created", I say foolishly.
"Wait, its putting the ingredients used for the jar in the jar, that
doesn't explain why the pickles aren't there though", I say foolishly
"Wait, whoever tried fixing this earlier fucking qdel'd the beaker and
called it a day????", I say, foolishly._

---

Anyways I changed how the crafting menu distincts between categories,
instead of checking whether or not the path is for food, it checks the
actual categories themselves (why didn't it do this already), meaning
that you can have non-food items on the food tab if it has a food
category. Did this by adding a list that includes all crafting
categories, so in the future when adding new categories you'll have to
add them twice, which sucks, but oh well.

Also added a new variable to craftable items, which makes it so that you
can not delete a container's contents if you so wish (why was this the
default).

All this so that when you craft pickles, it actually crafts pickles
instead of cucumbers.

I spent hours on this, its 6:30am as I'm typing this. I'm tired. Fucking
pickles.

Super duper ultra thanks to FinalPotato for guiding me and suffering
with me through this and teaching me so much about DM and BYOND. I
cannot emphasize just how helpful and awesome they were thank you thank
you thank you <3
## Why It's Good For The Game

Bug fixing be good
## Changelog
:cl:
fix: The jar of pickles, after millenia, finally actually contains
pickles. All hail the jar of pickles.
/:cl:

* All hail The Pickle Jar, harbringer of better crafting

---------

Co-authored-by: TheSmallBlue <ilanmori@hotmail.com>

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[33d9a0338f...](https://github.com/DATA-xPUNGED/DataStation/commit/33d9a0338f1d6811162479e337dbd0945463a8e8)
#### Wednesday 2023-03-15 00:54:29 by LemonInTheDark

Reworks trashbags slightly (#73761)

## About The Pull Request

I'm a bit sad about the state of trashbags. 
They're very clunky to use, so they almost never get touched. S
depressing. Let's try and fix that.

Let's make em fit in the belt slot (again), but as a tradeoff we'll make
it harder to pull one thing from your bag.
We'll give it a say, 1.5 second delay, so you can't quickdraw from em.
If you try and dump them out into something else, we'll throw any
spillover on the ground below you

I'm also doing some general code cleanup here. Making procs more
readable, vars more direct, removing some old legacy stuff.
I've added a remove_single proc to hook into via subtype, which takes a
mob as input. this has required placing extra requirement on some helper
procs, but fortunately it's not something they're unable to meet.

My hope is this will make garbage bags usable without being stupid.

## Why It's Good For The Game

I don't see these get used at all, cause they're a pain to carry around.
They got gimped because people were using them as infinite storage for
shotgun shells and other small items.
I've made using them for this sort of thing hard and slow, so I think we
oughta be fine. If not I'll do some more touching, maybe give the
autodrop a delay.

## Changelog
:cl:
balance: The janitor's trashbag now fits on his belt. In exchange,
taking something out of it sends a visible message, and has a delay.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[60e85fa947...](https://github.com/DATA-xPUNGED/DataStation/commit/60e85fa947799e20419dc867a238afb27b840e59)
#### Wednesday 2023-03-15 00:54:29 by LemonInTheDark

Polishes some side sources of light and color (#73936)

## About The Pull Request

[Circuit Floor
Polish](https://github.com/tgstation/tgstation/commit/6b0ee9813271f693ceb44ad42277c36ef2e71268)

Circuit floors glow! but it looks like crap cause it's dim and the
colors are washed out.
I'd like to make them look nicer. Let's make them more intense and
longer range, and change the colors over to more vivid replacements.

While I'm here, these should really use power and turn on and off based
off that.
Simple enough to do, just need to hook into a signal (and add a setter
for turf area, which cleans up other code too).

[Desklamp
Upgrade](https://github.com/tgstation/tgstation/commit/8506b13b9c97bf740c3e97db04450555387dd126)

Desklamps look bad. They're fullwhite, have a way too large
range.Crummy.
Let's lower their lightrange from 5 to 3.5, and make the ornate ones
warmer, and the more utilitarian ones cooler. The clown one can be
yellow because it's funny

I'm renaming a color define here so I'm touching more files then you'd
expect

[Brightens
Niknacks](https://github.com/tgstation/tgstation/pull/73936/commits/835bae28e9eb9946be53c9f5dac0a0a39f15ef21)

Increases the light range of request consoles, status displays,
newscasters, and air alarms (keycard machines too, when they're awaiting
input at least)
Increases the brightness of air alarms, I think they should be on par
with apcs, should be able to tell when they're good/bad.
Increases the brightness of vending machines (I want them to light up
the tiles around them very lightly, I think it's a vibe)

Fixes a bug with ai status displays where they'd display an emissive
even if they didn't have anything on their screen, looking stupid.
This was decently easy but required a define. Looked really bad tho

## Why It's Good For The Game

Pretty

<details>
<summary>
Circuit Floors
</summary>

Old

![image](https://user-images.githubusercontent.com/58055496/224534470-c6eac5f5-5de6-40e9-897d-3212b8796d81.png)

![image](https://user-images.githubusercontent.com/58055496/224534477-ad412ad9-f7c4-44ae-ad75-a1a2c9bd17be.png)

New

![image](https://user-images.githubusercontent.com/58055496/224534486-b7b408a3-546c-4f90-aa9f-0e58bf8128ad.png)

![image](https://user-images.githubusercontent.com/58055496/224534496-626458f7-ab63-429c-a5db-eae9c784d06a.png)
</details>

<details>
<summary>
Desk Lights
</summary>

Old

![image](https://user-images.githubusercontent.com/58055496/224534513-9868b0b8-bc73-4b45-b986-8445078a8653.png)

![image](https://user-images.githubusercontent.com/58055496/224534518-bbbc8c6d-b59e-4f28-a31c-6c6a7e2c2885.png)

New

![image](https://user-images.githubusercontent.com/58055496/224534529-7988f440-03be-42ef-894c-b9e77f577ae5.png)

![image](https://user-images.githubusercontent.com/58055496/224534532-c3f2c6bf-c925-4a59-a8f9-10bb955a9942.png)
</details>

The niknack changes are more minor so I'm not gonna grab photos for
them. I can if you'd like but I don't think it's necessary. Mostly a
vibes in dark spaces sorta thing
 
## Changelog

:cl:
add: I made circuit floors brighter and more vivid.
add: Made air alarms, vending machines, newscasters, request consoles,
status displays and keycard machines slightly "brighter" (larger light
range, tho I did make air alarms a bit brighter too)
add: Tweaked desklamps. Lower range, and each type gets its own coloring
instead of just fullwhite.
fix: AI displays are no longer always emissive, they'll stop doing it if
they aren't displaying anything. Hopefully this'll look nicer
/:cl:

---
## [rememberSnippetGameing/learning-on-video](https://github.com/rememberSnippetGameing/learning-on-video)@[8f64271bae...](https://github.com/rememberSnippetGameing/learning-on-video/commit/8f64271bae3daa0560b98893b0d09c5a9a25d8d5)
#### Wednesday 2023-03-15 01:03:58 by rememberSnippetGameing

I added the line, angels are holy.

And got rid of, god is beautiful.

---
## [Zonespace27/Skyrat-tg](https://github.com/Zonespace27/Skyrat-tg)@[5f9f60713b...](https://github.com/Zonespace27/Skyrat-tg/commit/5f9f60713b7f79f548eb9d02baeec793c1e50243)
#### Wednesday 2023-03-15 01:11:39 by SkyratBot

[MIRROR] Starlight Polish (Space is blue!) [MDB IGNORE] (#19059)

* Starlight Polish (Space is blue!) (#72886)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Adds support to underlays to realize_overlays
Ensures decals properly handle plane offsets
Fixes space lighting double applying if it's changeturf'd into. this
will be important later
Makes solar vis_contents block emissives as expected
Moves transit tube overlays to update_overlays, adds emissive blockers
to them

#### Adds render steps

An expansion on render_target based emissive blockers. 
They allow us to hijack an object's appearance and draw it somewhere
else, or even modify it, THEN draw it somewhere else.
They chain quite nicely

Fixes shuttles deleting z holder objects

#### Makes space emissive, makes walls and floors block emissives
The core idea here goes like this:
We make space glow, and give its overlays some color

This way, the tile and space parallax remain fullbright, along with
anything that doesn't block emissives, but anything that does block
emissives will instead get shaded the color of starlight

This requires a bit of extra work, see later

This is done automatically with render relays, which now support
specifiying layer and color (Need to make an editor for these one of
these days)

The emissive blocking floor stuff requires making a second render plate
to prevent double scaling

Also adds some new layering defines for lighting, and ensures all turf
lights have a layer. We'll get to this soon

#### Makes things in space blue

We color them the same as starlight, by taking advantage of space being
emissive
This means that things in space that block emissive will block it
correctly and be colored blue by the light overlay, but space itself
will remain fullbright

This does require redefining what always_lit means, but nothing but
cordons use that so it's fineee


#### Makes glass above space glow, and some other stuff

Glass tiles that sit above space will now shine light with matching
color to the glasses color. This includes mat tiles.

Glass tiles (not mat because they have no alpha) also only partially
block emissives.
Adds a new proc that uses render steps to acomplish this, essentially
we're cutting out bits below X alpha and drawing what remains as an
emissive.

#### Modifies partial space showing to support glow

Essentially, alongside displaying space as an underlay, we also display
a light overlay colored like starlight.
That starlight overlay gets masked to only be visible in bits that do
not contain any alpha.

We also mask the turf lighting to not go into bits that have no alpha,
to ensure we get the effect we want.
This is done with that lighting layer thing I mentioned earlier.

#### Makes appearance realization's list output ordered

I want it output in order of overlay, sub overlay suboverlay, next
overlay
Need to use insert for that

## Why It's Good For The Game

Pretty!
Also having space be emissive is a very very good way to test for fucked
emissive blockers (If it's broken why are we even drawing the overlay)
I know for a fact mob blockers on lizards and socks are kinda yorked, I
think there's more

<details>
<summary>
Old
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916157-d4b38aa7-3ab6-42a4-989f-7bfba2dc2cba.png)

![image](https://user-images.githubusercontent.com/58055496/213916077-637fa288-bbee-477d-aded-730d9683477e.png)

![image](https://user-images.githubusercontent.com/58055496/213916088-0657a8a2-5627-48e2-8c4b-870c90ef2072.png)

</details>


<details>
<summary>
New
</summary>


![image](https://user-images.githubusercontent.com/58055496/213916107-2af74e64-1817-4a44-b528-180a9160cb9e.png)

![image](https://user-images.githubusercontent.com/58055496/213916115-5fa36fcc-b988-4ccf-850e-21c26ed463d0.png)

![image](https://user-images.githubusercontent.com/58055496/213916120-6833187d-b12e-42a7-ac4b-63c56deb71e5.png)

</details>

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
add: Space now makes things in it starlight faintly blue
fix: Glass floors that display space now properly let space shine
through them, rather then hiding it in the dark
add: Glass floors above space now glow faintly depending on their glass
type
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>

* update modular

* Update _decal.dm

* Update _decal.dm

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Zephyr <12817816+ZephyrTFA@users.noreply.github.com>
Co-authored-by: Tom <8881105+tf-4@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [A-Hilaly/ack-test-infra](https://github.com/A-Hilaly/ack-test-infra)@[95e4857b28...](https://github.com/A-Hilaly/ack-test-infra/commit/95e4857b28122c6c5f8a30260be3dcac94e0e466)
#### Wednesday 2023-03-15 01:15:45 by Amine

Move Go binaries to `/usr/bin` (#287)

Issue https://github.com/aws-controllers-k8s/community/issues/1640

TL;DR: Prow was mounting `test-infra` code volume into `$GOPATH`
causing the deletion of `kind` and `controller-gen` binaries that are
installed in `$GOPATH/bin`


Yesterday, i embarked on a wild 7 hour journey to fix a bug that had
been causing prow jobs to fail with the error message "Kind not found".
The bug was introduced after a recent update that bumped the Go compiler
to `1.19`. I found the investigation to this bug to be both interesting
and frustrating, so i wanted to share some key takeways with the
community:

[The patch](https://github.com/aws-controllers-k8s/test-infra/commit/14dda81ce8ea430b51c9ce738483bea3744a5450) that introduced Go `1.19` also modified a `go get` command
into a `go install` command (because of this deprecation notice:
https://go.dev/doc/go-get-install-deprecation), which technically should
not have caused any issues. I tried restarting the e2e jobs in various
repositories to figure out whether the error was only related to one
controller or code-generator only, but all the repositories that execute
e2e tests were affected.

First, i started suspecting that thee `go install` command was not
working properly or had not been used correctly. I experiemented with it
locally, using various combinations of `GOPATH` and `GOBIN`, however, i
learned that the Go compiler is sophisticated enough to always put
downloaded binaries under `GOBIN` or `GOPATH/bin`. I then wondered if
the `PATH` variable didn't include the `GOBIN` path, which is supposed
to contain the `kind` and `controller-gen` binaries. I spent some time
reading the Dockerfiles and testing scripts, but they all set `GOPATH`
and always included a `GOBIN` in the `PATH` variable.

I also suspected that the issue may be related to the containers, but
experimentations with "Go containers" and environement variables
manipulation did not yield any results. I also tried building minimal
DOckerfiles to try to reproduce the issue, but that also did not give
any clues.

At this point, I suspected the container image it self. I build an image
locally and ran a shell inside it, but everythin g looked fine. THe
`kind` and `controller-gen` binaries were present and the `PATH` and
`GOPATH` variables were properly set. I then suspect that we may have a
corrupted published image in ECR, but pulling the image and running the
same commands revealed that the image was fine.

I then took a break from experimenting with Go/Docker/Envvars and tried
to spin some prowjobs with `v0.0.10` and `v0.0.9` (the last two versions
that were still using Go 1.17) of the integration tests image. This
confirmed that the issue was only with `v0.0.11`.

So, I decided to investigate further and logged in the Prow production
cluster. My first attempt was to restart a job and try to "exec bash" in
it, but the jobs failed to quickly for that to be possible. I then ran
a custom prow job (with `v0.0.11` integration image tag) but with a
`sleep 10000` command. When looking inside, there were no `kind` or
`controller-gen` binaries, i searched the entire file system, they were
nowhere to be found, grep, find, name it all.. nada. I then execute a
`go install sigs.k8s.io/kind@v0.17.0"`, and bam, it worked, the binary
was here again. The same thing happened with controller-gen. So for now
we know that we ship images with all the necessary binaries and when a
prow job starts, they disapear...

To isolate the problem further, i created a `ProwJob` resource and
copied the `Pod` (spawned by Prow) spec and metadata into a different
file. Running the same commands used previously proved that indeed
something is wrong with the pod spec, causing the binaries to disapear.
And when a file disppears it reminds me of my college years, where i
epically failed to use symbolic links, which is a bit similar (at least
from a UX point) to volume mounts in the Docker world.

So, i decided to check the volume mounts, and to my not-surprise, I
found this:

```yaml
    - mountPath: /home/prow/go
      name: code
```

Yes... Prow is mounting the test-infra source code into `GOPATH`
(`/home/prow/go` in prow jobs) ! Which is the parent directory of
`GOBIN` where we install the binaries. And it all makes sense now.
Mounting code into this directory overrides the existing volume and
deletes everything existing in `GOPATH` including the binaries we
installed before.

The Dockerfile was missing the `mv` commands that puts `kind` and
`controller-gen` in `/usr/bin`. To fix this issue, I added the missing
`mv` command to the docker file and published and new `integration`
image `v0.0.12`.

---

Anyways, investigating the source of the volume mount led me to the Prow
presets configurations. Presets are a set of configurations (volume
mounts, environement variables, etc...) that are used for jobs with
specific labels in their metadata. I tried to play with this in our Prow
cluster, but quickly stoped when it was a bit risky and could break
other components too. While digging into `test-infra` pod-util package i
learned that the code volume is not coming from our defined presets and
is a default preset coming from Prow it self - the `/home/prow/go` value
is harded-coded in `prow/pod-utils/decorate/podspec.go#L54`. I'm not
sure whether we can override this value.

Anyways, for now, i'm just gonna implement a quick fix that moves the
binaries to `/usr/bin` instead of leaving them inside `GOBIN`. Ideally
we should either choose a new directory go `GOPATH` that is different
from `$HOME/go` or find a solution that will let the code and our
binaries coexist in the same place. Either of them requires a lot of
changes and can agressively break some our prow components/scripts.

@jljaco is currently workng on creating a staging cluster, which will
provide us a safe environementto test and experiment with new
configurations. This will allow us to try out new changes without having
to woryy about potentially impacting the production environement.

Signed-off-by: Amine Hilaly <hilalyamine@gmail.com>

By submitting this pull request, I confirm that my contribution is made under the terms of the Apache 2.0 license.

---
## [ArcaneDefence/tgstation](https://github.com/ArcaneDefence/tgstation)@[a3451b7fe4...](https://github.com/ArcaneDefence/tgstation/commit/a3451b7fe4ff60e0cb6cc4f2bd6d20543f455940)
#### Wednesday 2023-03-15 01:20:26 by san7890

Makes "forced" opening and closing of doors way more sane (#73699)

## About The Pull Request

The gist is that people thought that this was a boolean value, which was
fucked up. It's not a boolean value, it accepts anything between 0 and
2. So, let's re-arrange the checks and framework, give it some
descriptive defines, just so people know what the fuck "2" actually
does. `DOOR_DEFAULT_CHECKS` (0) does stuff normally,
`DOOR_FORCED_CHECKS` 1 typically just checking if we aren't emagged shut
or something (i suppose it could happen), and `DOOR_BYPASS_CHECKS` (2)
means that we just get the fucking door open if it isn't physically
sealed shut/open somehow.

I don't know if `forced` has ever _been_ a boolean, but for some reason
people thought it was.

I also enforced boolean returns instead of passing back null. This did
not matter for close() but i think it's silly to have a TRUE/null
dichotomy so that was also touched up.
## Why It's Good For The Game

Much better to read, less confusing, less stupid. It's been irritating
me for a while now, so let's just implement it now. Had to make a few
awkward concessions in order to fit this into the current code
framework, but it should be a lot nicer. I also shuffled the order of
some code around because certain placements didn't make any sense (early
returns not being in the right spot for an early return).
## Changelog
Nothing that should concern players.

---
## [ArcaneDefence/tgstation](https://github.com/ArcaneDefence/tgstation)@[db7534d6da...](https://github.com/ArcaneDefence/tgstation/commit/db7534d6dabf0127c87b291eae4063b6f77d36e4)
#### Wednesday 2023-03-15 01:20:26 by LemonInTheDark

Lowers nightvision threshold to work for mesons, fixes not being able to examine stuff lit by overlay lights (#73712)

## About The Pull Request

Might be a bit low, but part of that is because it's kinda bad at
figuring color, rgb isn't really balanced in that respect

Fixes not being able to see stuff under the light of a lamp

Overlay lights don't set lumen, which leads to stupid when you try and
check with ONLY it
It worked before because the mob has THEIR luminosity set, which then
"glowed" out

That doesn't work here cause yaknow I removed our uses of byond lighting
(except for errant view() calls) so this is the best I've got

## Why It's Good For The Game

Closes #73548 

## Changelog
:cl:
fix: Examining in the dark is less wonk now, sorry bout that
/:cl:

---
## [Ricoenrique24/fachry-15](https://github.com/Ricoenrique24/fachry-15)@[2ad8c69fe1...](https://github.com/Ricoenrique24/fachry-15/commit/2ad8c69fe1efbecf47a6dd2500faff56cdf43deb)
#### Wednesday 2023-03-15 03:07:35 by Ricoenrique24

Little Mistake but i fixed this mistake

Hi! I'm Rico. Your Friend.

FYI, I'm going to your github profile to hint some creativity. I'm Interested with your Readme.md! But, i found Little mistake from your information. Just Little, Not Big!

I hope you can be great front-end developer! I'm Sorry if my english is bad:(

Best Regard,
Enrique

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[a1212427b1...](https://github.com/treckstar/yolo-octo-hipster/commit/a1212427b19e1d3e1bb592a67d460cb96b668c6a)
#### Wednesday 2023-03-15 03:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [AndigenaTeam/andigenagate](https://github.com/AndigenaTeam/andigenagate)@[aa775d8006...](https://github.com/AndigenaTeam/andigenagate/commit/aa775d80065d76a17af13fe255ebac11d5a3f4b4)
#### Wednesday 2023-03-15 03:31:12 by TukanDev

refactor device grant, reset password actually sends a code now smh, better email messages and experimental ww support (fuck your implementation and empty tokens...)

Signed-off-by: TukanDev <contact@tukandev.com>

---
## [Jqual1/ArtGame](https://github.com/Jqual1/ArtGame)@[7bdaf09715...](https://github.com/Jqual1/ArtGame/commit/7bdaf097154439d18034e7c78d666826becceefa)
#### Wednesday 2023-03-15 03:42:44 by Jonathon Qualls

The friends room is now more complete looking

(need to figure out which other two paintings to put in and need to connect shit but this is a start)

---
## [pytorch/pytorch](https://github.com/pytorch/pytorch)@[c5a66e26c1...](https://github.com/pytorch/pytorch/commit/c5a66e26c11806a69c07dbffae2f7df9ee783a2d)
#### Wednesday 2023-03-15 04:04:51 by Brian Hirsh

Update base for Update on "aot autograd refactor: make all synthetic base logic layered in a single location"

This  refactor doesn't significantly change LoC in aot autograd, but I think this nets out to making it clearer (interested in peoples' thoughts).

The idea is that I tried to re-write the part of aot autograd that deals with synthetic bases in a layered way, similar to how Ed wrote the logic for dedup'ing inputs: it happens in one place, and all of the downstream transformation in aot autograd don't have to worry about it.

Specifically, I added a new function `aot_wrapper_synthetic_base`, similar to the existing `aot_wrapper_dedupe`.

The benefit: none of the other code in aot autograd needs to think about synthetic bases (previously, synthetic base code was intertwined in several places).

The downsides: there are two.

(1) `aot_wrapper_synthetic_base()` needs to have its own epilogue. There is one particularly hairy case, where factoring the synthetic base logic to a single location was painful: If you have two inputs that alias each other, where one gets a data mutation, and the other gets a metadata mutation.

Ordinarily, metadata mutations are handled by the runtime epilogue, in `create_runtime_wrapper`. However, now that things are factored this way, the runtime wrapper operates only on synthetic bases instead of operating on the original inputs. For data mutations, it is fine to apply the data mutation to the synthetic base instead of the original input alias. But for metadata mutations, we **need** to apply the metadata mutation directly to the original inputs.

The way that I handled this was by tracking which inputs slot into this specific case (part of a synthetic base, and get metadata mutations), and updateing the flat_fn() that we pass downstream to return these updated inputs as extra outputs. From the perspective of downstream logic, these are real user outputs, that it can treat like any other user outputs. `aot_wrapper_synthetic_base` will know to grab these extra outputs and use them to apply the metadata mutations.

This was pretty annoying, but has the benefit that all of that logic is encapsulated entirely in `aot_wrapper_synthetic_base()`.

(2) input mutations are now performed on the synthetic base instead of the individual aliases.

You can see the original code comment [here](https://github.com/pytorch/pytorch/blob/b0b5f3c6c681896febbd9ff7ad7649b13def345d/torch/_functorch/aot_autograd.py#L1131) for details. We used to do the optimized thing in this case, and now we do the less optimized thing (copying the entire synthetic base, instead of the potentially smaller alias).

To be fair, we had no data showing that this optimization was showing improvements on any models in practice. I also think that the main reason anyone would ever run across this problem is because of a graph break - so if you care about perf, you probably want to avoid the extra graph breaks to begin with. I haven't added any warnings for this, but we probably could depending on what people think.




[ghstack-poisoned]

---
## [TheSmallBlue/tgstation](https://github.com/TheSmallBlue/tgstation)@[1cdc327a8f...](https://github.com/TheSmallBlue/tgstation/commit/1cdc327a8f98c1592fc970a4ef1c39d685c81554)
#### Wednesday 2023-03-15 04:12:25 by Jacquerel

Station Trait: Spider Infestation (#73893)

## About The Pull Request

Hate having your cables eaten by mice? Nanotrasen have heard your
complaints and settled on a natural, _organic_, and eco-friendly
solution.

When this station trait is active, roundstart and event mouse spawns
have a chance to instead be replaced with duct spiders (both will exist,
it doesn't remove mice).
Duct spiders are largely harmless to humans, actively hunt other
maintenance creatures (such as mice), and have only one _tiny_ downside.

![image](https://user-images.githubusercontent.com/7483112/224345781-2627be98-67f2-4cab-ac40-c6c9b35ea909.png)

These mobs can also sometimes be spawned by a minor scrubber clog event.

As a side note, all spider basic mobs with AI (except Araneus) will now
try to automatically fill a small area around them with webs.

Also I made it so that mobs will ignore their random_walking behaviour
if they're engaged in a `do_after`, just in case.

## Why It's Good For The Game

Adds a little bit of variety to things which can slightly annoy you in
maintenance.
Spiders will automatically make places they live in look like spiders
live there.

## Changelog

:cl:
add: A station trait which sometimes populates maintenance with small
spiders. You can wear them as a hat if you wanted to have a spider on
your head for some reason.
add: Spider mobs will automatically start webbing up their environment.
/:cl:

---
## [justcool393/themotte-rDrama](https://github.com/justcool393/themotte-rDrama)@[9895fa1bba...](https://github.com/justcool393/themotte-rDrama/commit/9895fa1bbabc9213391e380753ca72404f80aa18)
#### Wednesday 2023-03-15 04:29:00 by justcool393

comments.html: refactor so that something can be sanely
changed in it

the comments.html template (along with submission.html) has numerous
undesirable properties which i will describe now. unless you are very
familiar with the codebase, it can be extremely difficult to grok.

this is pretty insane as there is nothing fundamentally complex about
the goal of comments.html: return a component that shows a username
and info, reports if any, comment content, and actions a user can
take.

this behemeoth was initially 886 lines in the old version of this
codebase, and this is with awards and a lot of other cruft removed.
anyway, the maintainability of this file is about on par with some
legacy application that keels over and dies if you sneeze vaguely
in its direction.

the nicest thing i can say about it is that it isn't currently
crashing.

anyway some of the problems include:

* large, splittable components, are not split into separate files.

this makes it incredibly difficult to find or make changes across
the template and makes it nearly impossible to find or change a
specific thing.

this is most easily exemplified in the modals, which should by all
accounts be separate templates, just inlined into comments.html.

* the nesting is oftentimes incorrect.

inexplicably, probably out of laziness from when the code was first
written, things will end up fully left aligned, while multiple layers
deep into a nesting context.

if an if statement or an endif is changed, it is *incredibly*
difficult to figure out where the error was. you can't trust the
nesting.

* multiple repeated checks for things that are always true.

this is probably a symptom of the above two problems but it's very
noticeable once you fix the nesting. for example there is a block
near the very top of the actions bar which checks for
parent_submission which effectively checks "is this in a post" (this
commit won't complain about parent_submission checks but i do have
opinions on those).

all of the action buttons further down the chain also check for
parent_submission, or even check inconsistently (by using if c.post)
within this context this is a completely unnecessary check in this
context.

while it is potentially useful (and in fact because #251 requires we
dismantle the assumption a little bit) to have these checks now, the
fact that they were initially added shows that when the code was all
initial written, there was little care into thinking about comment
state.

* mobile actions are duplicated and duplicated inline.

i actually do find it probably pretty hard to support this normally
given the codebase's DOM so whatever, duplicate the things, *but* if
we're going to do that, inlining it into the middle of an incredibly
long template is really difficult to comprehend as a design decision.

...anyway yeah this PR intends to fix these problems and enable work
to be done on #251. this is a "perfect is the enemy of good" commit.
it doesn't change much fundamental and is not intended to erase the
sins of the original file, but at least make it maintainable.

this also fixes a minor bug with #473 where the GIF modal was left
in by accident.

---
## [AnandSuresh02/android_kernel_asus_sdm660](https://github.com/AnandSuresh02/android_kernel_asus_sdm660)@[3d667727d0...](https://github.com/AnandSuresh02/android_kernel_asus_sdm660/commit/3d667727d05956ca1c330a8bac677859721c00c9)
#### Wednesday 2023-03-15 05:04:15 by Christian Brauner

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

---
## [CaiCanCode/prime_factoring_projects](https://github.com/CaiCanCode/prime_factoring_projects)@[93dfdb8e5a...](https://github.com/CaiCanCode/prime_factoring_projects/commit/93dfdb8e5ac825f8e3866effdccef61f94be97c6)
#### Wednesday 2023-03-15 05:49:01 by Michaiah

Error handling

oh god, C. I'm preventing accidentally wrapping and it still takes negatives so that's good but the conversion x_x
There's probably a library function that does what I want but I did it myself so I'm pretty happy with that.
C, my love, you're beautiful, but occasionally very annoying

---
## [jimbolo/crawlee](https://github.com/jimbolo/crawlee)@[a95e6676b2...](https://github.com/jimbolo/crawlee/commit/a95e6676b2e3574c8db3083c661dc09a5405751e)
#### Wednesday 2023-03-15 06:34:13 by Martin Adámek

chore: switch to yarn v3 (#1752)

NPM got somehow [broken more than
usual](https://github.com/apify/crawlee/actions/runs/3997285915/jobs/6873858419)
and its no longer possible to install the dependencies in CI. We were
struggling with NPM for quite some time (especially after we moved to
turborepo). I’ve been advocating for yarn since my first days here, been
using it for last ~5 years on a daily basis and it never did anything
wrong to me, so I hope this will be the right step and a smooth
transition for all the collaborators.

What to expect? Since we require node 16, we can leverage `corepack`, a
new tool shipped with newer node versions (btw developed by yarn
maintainers). This means you just need to run `corepack enable` and yarn
should be available in your workspace. In case of some problems, you can
try running `corepack prepare yarn@stable --activate`, but it shouldn’t
be needed. Note that we use `corepack` instead of commiting yarn binary
to the git repo - that is the reason why `.yarn` folder is gitignored.

Initially we will start with a conservative setup, using a node linker,
so there will be the good `node_modules` folder we are all used to. I’d
like to experiment with the advanced features as well, mainly in the
project templates, as it could greatly improve the build times (we could
even skip the install step completely).

With that said, we will be still using NPM inside our E2E tests, to be
sure the project can be safely installed with NPM. This change should
affect only the collaborators, not our users. Ideally we should test
other package managers via CI too, so we are sure `pnpm` works as well,
or maybe even `bun`.

Few API differences and quality of life improvements yarn brings:
* `npm install` -> `yarn`
* `npm install xxx` -> `yarn add xxx`
* `npm run ...` -> `yarn …`
* `npx …` -> `yarn …`
* no need to deal with the `--` issue from `npm run` (propagating CLI
params to the script)
* powerful caching and _sane_ lockfile format

---
## [SchwabischesBauernbrot/OpenViva-UE5](https://github.com/SchwabischesBauernbrot/OpenViva-UE5)@[297bf8d0c9...](https://github.com/SchwabischesBauernbrot/OpenViva-UE5/commit/297bf8d0c9d5bc787b2f12e3b8ad1249b491bf0c)
#### Wednesday 2023-03-15 06:40:27 by SolidStonee

lamp system that hurts my fucking head

god unreal is so annoying sometimes

---
## [leslie-fang-intel/pytorch](https://github.com/leslie-fang-intel/pytorch)@[11aab72dc9...](https://github.com/leslie-fang-intel/pytorch/commit/11aab72dc9da488832326a066d2e47520e4ab2b3)
#### Wednesday 2023-03-15 07:24:20 by Driss Guessous

[SDPA] Add an optional scale kwarg (#95259)

# Summary
This PR adds an optional kwarg to torch torch.nn.functional.scaled_dot_product_attention()
The new kwarg is a scaling factor that is applied after the q@k.T step of the computation. Made updates to the efficient kernel to support but flash and math were minimally updated to support as well.

Will reduce the complexity of: #94729 and has been asked for by a couple of users.

# Review Highlights
- As far as I know I did this the correct way and this both BC and FC compliant. However I always seem to break internal workloads so I would love if someone can advice I did this right?
- I named the optional arg 'scale'. This is probably dumb and I should name it 'scale_factor'. I will make this change but this is annoying and it will require someone thinking we should rename.
- 'scale' is interpreted as `Q@K.T * (scale)`

Pull Request resolved: https://github.com/pytorch/pytorch/pull/95259
Approved by: https://github.com/cpuhrsch

---
## [MrSamu99/Shiptest](https://github.com/MrSamu99/Shiptest)@[7f8874df29...](https://github.com/MrSamu99/Shiptest/commit/7f8874df29bdd5624bc957907249edffbbeaba12)
#### Wednesday 2023-03-15 07:25:40 by Zevotech

Mashes several of the Whitesands Survivor Camp ruins into one extra large ruin (#1640)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Combines the whitesands surface camp adobe, farm, gunslingers,
survivors, hunters and saloon into one massive, 59x59 ruin. Some various
extra loot and changes have been made throughout, generally to improve
the experience of digging through the trash for goodies. Changes the
riot shotgun in the saloon to a double barrel shotgun. Also cleans up
the various issues with the ruins, like walls under doors, or area
passthroughs being used excessively over the outside of the ruins,
resulting in them generating in the middle of mountains buried in the
rock.

"Well, why didn't you add the drugstore?" The loot in it was too good.
The stuff in there can really help a ship get on its feet, and I am not
gonna deprive them of that just to shove it in an already packed massive
ruin area. I'm not saying it doesn't need its own remap, just that it
doesn't fit well with the other camps put into this ruin.
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
"a ruin that is tiny and sucks on purpose is still bad" and holy shit
did most of the camps fit this criteria. Survivor, Gunslinger, and
Hunter camp variants were the smallest ruins in the game next to the one
that was just a single tumor, and constantly took up entire map
generations just to be a massive dissapointment to any player that came
across them. Or they would spawn in the middle of an acid lake. Either
way this ruin is massive and should provide a breath of fresh air for
scavengers and combat hungry miners alike.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pics or it Didn't Happen

![image](https://user-images.githubusercontent.com/95449138/208811497-ad556187-174a-4803-aea5-be40f0bb3038.png)
Ingame, two pics due to view range not being large enough to get the
full thing at a good quality.

![image](https://user-images.githubusercontent.com/95449138/208816213-082d6597-9718-45ff-9132-2907fcf63a57.png)

![image](https://user-images.githubusercontent.com/95449138/208816258-a3e2909b-fc98-4686-9bdc-8dc3192421e1.png)


## Changelog

:cl:
add: whitesands_surface_camp_combination, a survivor village comprised
of smaller revamped whitesands camps all packaged in one ruin. can be
found in the map catalogue.
del: whitesands_surface_camp adobe, farm, gunslingers, survivors,
hunters and saloon, for being tiny ruins that suck.
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
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[9d5b4907e8...](https://github.com/lizardqueenlexi/orbstation/commit/9d5b4907e8d8aaecf24bfd8f6755822b494a4b55)
#### Wednesday 2023-03-15 07:47:36 by Rhials

Post-Revolutionary Fervor station trait, revolutionary bedsheets, and a megaphone (#73799)

## About The Pull Request

Upon revolution success, the chosen headrev will now also receive a
megaphone, and a "revolutionary bedsheet" repurposed from a stolen CC
bedsheet to commemorate their success. The post-revs confusion and lack
of command/security usually leads to an instantaneous, total breakdown
in cohesion. It's every man for himself -- that's no way to run a
commune! Just because the revolution has succeeded and nobody can see
your big blue "R" anymore doesn't mean you can't be a leader!


![image](https://user-images.githubusercontent.com/28870487/222981576-e62e457b-1b2d-4756-8c87-7a9093c92c2d.png)

This also adds a new revolution-themed negative station trait --
Post-Revolutionary Fervor. When present, this trait trashes the command
areas at the start of the round. This means cracked windows, broken
consoles, vendors getting knocked over, and the occasional dead
greytider.


![image](https://user-images.githubusercontent.com/28870487/222981095-14ce9336-2320-406e-b0a6-dc91cb8f9479.png)

If you start cleaning at the start of the round, you might finish right
as the next batch of revs decides to crop up.
## Why It's Good For The Game

Giving one of the headrevs a bigger voice and a cool cape (or uncool,
depending on how you view the sprite) means that there's a chance for
them to step up and try to keep the wheels on. Just remember -- Nobody
is obligated to actually listen to this person, it's just a bedsheet.

Adds a neato station trait, which probably counts as command gameplay
content.

## Changelog
:cl: Rhials
add: The headrev who receives the revolutionary banner after a win will
also receive a commemorative bedsheet and megaphone.
add: Post-Revolutionary Fervor station trait. I hope you enjoy fixing
broken computer screens.
spriteadd: A revolutionary bedsheet.
/:cl:

---
## [Aikiro42/Project-45](https://github.com/Aikiro42/Project-45)@[7abc014622...](https://github.com/Aikiro42/Project-45/commit/7abc014622a02432fa0c0d8e63e3b6623d842700)
#### Wednesday 2023-03-15 07:51:19 by Aikiro42

stupid ass conflicts

how the fuck does it even work

---
## [gurking/Citadel-Station-13-RP](https://github.com/gurking/Citadel-Station-13-RP)@[81c1229373...](https://github.com/gurking/Citadel-Station-13-RP/commit/81c1229373208790c3375a138579aaf76a0006d0)
#### Wednesday 2023-03-15 09:08:39 by Captain277

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
## [its-Hans/NeteaseMC-Accounts](https://github.com/its-Hans/NeteaseMC-Accounts)@[e239ad2a9f...](https://github.com/its-Hans/NeteaseMC-Accounts/commit/e239ad2a9fafcc9b448103b9240a6d59795d462a)
#### Wednesday 2023-03-15 09:22:35 by MakeBetterMe

LICENCE

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.

---
## [Dusoleil/sploit](https://github.com/Dusoleil/sploit)@[c989e25377...](https://github.com/Dusoleil/sploit/commit/c989e253774b07721149bed0c8cd4fa38fe1fb69)
#### Wednesday 2023-03-15 09:26:29 by dusoleil

RFC on the auto-arch and bininfo stuff

Rough idea/implementation of where I was thinking of going with this.
Thoughts?

There are three main additions here:

In r2, you can now get the results of the iI command. Or at least the
fields that I thought were useful for now.

In elf, the results of the above are broken into two fields and added to
the class' API.  elf.bininfo and elf.security are another private inner types
that allow you to access the info as attributes and have special __repr__.

In arch, there is now a lookup_arch() function that retrieves one of the
preconfigured Archs based on a tuple of arch_string, wordsize, and
endianness from elf.bininfo.  Elf automatically calls this on
construction and stores the result in elf.arch.

In order to facilitate the lookup dict without having to respecify the
Arch entries, I moved some things around and am doing some somewhat
gross shit with importlib. On the bright side, I can now move the
preconfigured Arch definitions to the top of the file.

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[c68a159884...](https://github.com/odoo-dev/odoo/commit/c68a15988432b201ae3786eb54bac3110c4242f4)
#### Wednesday 2023-03-15 09:44:13 by Arnold Moyaux

[FIX] stock,purchase,mrp: accumulative security days

Usecase to reproduce:
- Set the warehouse as 3 steps receipt
- Put a security delay of 3 days for purchase
- Set a product with a vendor and 1 days as LT
- Replenish with the orderpoint

You expect to have a schedule date for tomorrow that contains all the
product needed in the incoming 4 days.

Currenly the internal transfer from QC -> Stock is for tomorrow (ok).
The transfer from Inpur -> QC is plan for 2 days in the past. (not ok)
The PO date is plan for 5 days in the past. (not ok)

It happens because the system check at each `stock.rule` application if
purchase is part of the route. If it's then it applies the security lead
time. It's a mistake because we should apply it only the first time.

To fix it we directly set it when the orderpoint run and not during
`stock.move` creation.
However for MTO it's not that easy. We don't want to deliver too
early the customer. So we keep applying the delay during the
`stock.move` creation but only when it goes under the warehouse stock
location.

X-original-commit: 97f52bd40d97109a7983549d252476959ddceada
Part-of: odoo/odoo#112325

---
## [Alfombruh/python_piscine](https://github.com/Alfombruh/python_piscine)@[2b2c11ec03...](https://github.com/Alfombruh/python_piscine/commit/2b2c11ec036e3d5edc2ba77f2b763f29f01f2fa3)
#### Wednesday 2023-03-15 09:49:38 by Alfombruh

module01 finished. Not gonna delete comments fuck you

---
## [LebToki/index-for-xampp](https://github.com/LebToki/index-for-xampp)@[a42be0b7c9...](https://github.com/LebToki/index-for-xampp/commit/a42be0b7c9033236d496c9eff6d7e1b1da2547af)
#### Wednesday 2023-03-15 10:03:10 by Tarek Tarabichi

Update README.md

Welcome to the XAMPP root directory index page!

We've created a visually appealing user interface that will auto sense any projects and directories created within the root page of your XAMPP server. Our index file replaces the vanilla XAMPP server index page, providing you with a more interactive and efficient way to manage your projects.

With our customized UI, you can easily navigate through your projects and directories, quickly find the files you need, and manage your server more effectively. We understand the importance of having an organized workspace, and our index page helps you achieve just that.

Our index page is designed to be user-friendly and intuitive, making it easy for beginners and experienced developers alike. We've incorporated a responsive design, so you can access it on any device, whether you're on your desktop computer or mobile phone.

We're confident that our XAMPP root directory index page will enhance your development experience and streamline your workflow. Try it out today and let us know what you think!

---
## [chilkat81/blue](https://github.com/chilkat81/blue)@[9f1c7d1a55...](https://github.com/chilkat81/blue/commit/9f1c7d1a55913ca9a1d8f1b0b011b254ea6ebd80)
#### Wednesday 2023-03-15 11:23:42 by Angelo G. Del Regno

Makefile.lib: Lower kernel gzip compression to fastest

You're reading this - so you're trying to understand "JUST WHY OMG".
That's already a good step.

First of all, this is a downstream kernel - always keep that in mind!
Now, this kernel is targeting new *very powerful* Qualcomm platforms
like SM8250 and the Sony Edo platform - which has a very fast UFS card.

Keep in mind that the bootloader sets the CPU at a frequency that is
slightly faster than the "in the middle" ones, which is anyway not
veeeery fast - but that's good, really. I agree.

So.. check this out:   for Image.gz-dtb.....
COMP_LEVEL    SIZE
9             20116171
5	      20220479
2	      20940223
1	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

Signed-off-by: Tiktodz <ewprjkt@proton.me>

---
## [astrorick/thesis_work](https://github.com/astrorick/thesis_work)@[9bdf800cb0...](https://github.com/astrorick/thesis_work/commit/9bdf800cb061d76a0e36b4791ea140470c283181)
#### Wednesday 2023-03-15 11:44:01 by Astrorick

Fixed stupid Gazebo bullshit

To make it really simple, Gazebo has problems.
Robot was turning slower than it should and that caused SLAM to diverge.
That problem is now fixed but a shameful trick was used to achieve this.

---
## [kawaaii/kernel_xiaomi_gauguin](https://github.com/kawaaii/kernel_xiaomi_gauguin)@[02649f5ae4...](https://github.com/kawaaii/kernel_xiaomi_gauguin/commit/02649f5ae4411278f5b6c497092d327ab79fc7b8)
#### Wednesday 2023-03-15 12:10:00 by Wang Han

power: Introduce OnePlus 3 fingerprintd thaw hack

Taken from Oneplus 3, this hack will make fingerprintd recover from suspend quickly.

Small fixes for newer kernels since we're coming from 3.10.108..

Change-Id: I0166e82d51a07439d15b41dbc03d7e751bfa783b
Co-authored-by: Cyber Knight <cyberknight755@gmail.com>
[cyberknight777: forwardport and adapt to 4.14]
Co-authored-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[Tashar02: forwardport and adapt to 4.19 and xiaomi_sdm660's fp]
Signed-off-by: Shreyansh Lodha <slodha96@gmail.com>
Signed-off-by: Pierre2324 <pdbbasketball@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>
Signed-off-by: Dhruv <dhruvgera61@gmail.com>
Signed-off-by: Cyber Knight <cyberknight755@gmail.com>
Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
[ hridaya: Adapt for xiaomi_gauguin's fp ]
Signed-off-by: hridaya <hridaya@pixelos.net>

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[e5ab42dba0...](https://github.com/cmss13-devs/cmss13/commit/e5ab42dba06e537df5c146169971dd8418f2ce55)
#### Wednesday 2023-03-15 12:53:58 by boskoramen

Consolidates some XSS under hivecore (#2738)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Spawn pool and evo pods are removed and their functionality is
umbrella'd under the hive core. Sprites still exist though.

# Explain why it's good for the game

"Roleplay" has become an increasingly more popular and touchy subject
within the community as of recently. I, wholeheartedly agree, that
roleplay is an important aspect of the game, and there are ways to
improve it. One of these ways is through immersion. In this MR, it is
intended to increase player immersion.

One of the most memorable and haunting scenes in Aliens was when they
reached the hive and they found the bodies. This very unique and
cinematic scene was often able to be replicated in CM, with the marines
busting open the hive and finding all the chestbursted bodies of their
comrades. Roleplaying this out was commonplace. "Dear God... what did
they do to you..." or acting out in disgust are just a few of the many
ways having bodies in the hive positively impacted the game.

XSS was a failed attempt at spicing up the xenomorph gameplay loop at
the expense of immersion and should be at least somewhat reverted while
keeping balance in mind. A brief discussion with many prominent
xenomorph players, including those most experienced in queen, have not
particularly expressed favor to XSS either.

To start, let us remember why XSS (xeno special structures - hive core,
evo pods, morpher, pool, etc) was added.

https://docs.google.com/document/d/19_zDUmLdxpUzxj-GuWu7F4bSj4zBYzmZ39s_N5X7kQ0/edit
- This is the original development document for XSS.
Let us examine the major points:
1.Introduce a way for Xenomorph players to recycle - This idea was never
reached.

2.Reduce Xenomorph attrition - Grand objective was unsuccessful. Very
little changed.

3. Offer new avenues of play "by reducing the punishment of xenos dying"
- This never happened. Dying was still just as punishing, especially
with facehug nerfs.

The spawn pool - The idea of the spawn pool was successful and has
remained unchanged since. I would argue, however, it is not immersive.
Xenomorphs do not have bright, glowing, acidic pools in their hives.
(Yes I know there was a comic with a pool, and this is not how it was
used)

Egg Morpher - These used to be TURRETS. They are no longer turrets, and
their sprites have been broken for almost 4 years (the bodies put inside
of them used to show their face in the little purple part) They are
currently defunct facehugger reservoirs. I am in favor of removing them,
but I would argue that is a balance issue (number of huggers in play)

Evolution Pod - It was intended for these to be able to be eaten in
order to evolve. They haven't done this for years. Why do we still have
them? They take up 18 spaces of precious hive weeds, provide light,
(xenomorphs HATE light) and wherever a hive core is built, these are
also built. We can just merge them with the hive core because there is
no reason to have them anymore.

This PR currently completely removes the spawn pool and evolution pod
from gameplay, while reimagining their functions for current balance.
This PR is not intended to change balance in any way.

All functionality from the spawn pool in regards to "pooled" larva has
been given to the hive core, and they are now called "burrowed" larva.
Chestbursts now give two larva, this is to be kept with current balance
of two xenos per capture.

Evopod functionality and evolution speed boost was merged with the hive
core.


# Testing Photographs and Procedure
n/a


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

:cl: TheDonkified
del: Evo pods and spawn pool are removed.
add: Hive core directly affects evolution speed and is where burrowed
larva spawn from now on.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>
Co-authored-by: harryob <me@harryob.live>

---
## [AtariDreams/git](https://github.com/AtariDreams/git)@[69bbbe484b...](https://github.com/AtariDreams/git/commit/69bbbe484ba10bd88efb9ae3f6a58fcc687df69e)
#### Wednesday 2023-03-15 13:18:17 by Jeff King

hash-object: use fsck for object checks

Since c879daa237 (Make hash-object more robust against malformed
objects, 2011-02-05), we've done some rudimentary checks against objects
we're about to write by running them through our usual parsers for
trees, commits, and tags.

These parsers catch some problems, but they are not nearly as careful as
the fsck functions (which make sense; the parsers are designed to be
fast and forgiving, bailing only when the input is unintelligible). We
are better off doing the more thorough fsck checks when writing objects.
Doing so at write time is much better than writing garbage only to find
out later (after building more history atop it!) that fsck complains
about it, or hosts with transfer.fsckObjects reject it.

This is obviously going to be a user-visible behavior change, and the
test changes earlier in this series show the scope of the impact. But
I'd argue that this is OK:

  - the documentation for hash-object is already vague about which
    checks we might do, saying that --literally will allow "any
    garbage[...] which might not otherwise pass standard object parsing
    or git-fsck checks". So we are already covered under the documented
    behavior.

  - users don't generally run hash-object anyway. There are a lot of
    spots in the tests that needed to be updated because creating
    garbage objects is something that Git's tests disproportionately do.

  - it's hard to imagine anyone thinking the new behavior is worse. Any
    object we reject would be a potential problem down the road for the
    user. And if they really want to create garbage, --literally is
    already the escape hatch they need.

Note that the change here is actually in index_mem(), which handles the
HASH_FORMAT_CHECK flag passed by hash-object. That flag is also used by
"git-replace --edit" to sanity-check the result. Covering that with more
thorough checks likewise seems like a good thing.

Besides being more thorough, there are a few other bonuses:

  - we get rid of some questionable stack allocations of object structs.
    These don't seem to currently cause any problems in practice, but
    they subtly violate some of the assumptions made by the rest of the
    code (e.g., the "struct commit" we put on the stack and
    zero-initialize will not have a proper index from
    alloc_comit_index().

  - likewise, those parsed object structs are the source of some small
    memory leaks

  - the resulting messages are much better. For example:

      [before]
      $ echo 'tree 123' | git hash-object -t commit --stdin
      error: bogus commit object 0000000000000000000000000000000000000000
      fatal: corrupt commit

      [after]
      $ echo 'tree 123' | git.compile hash-object -t commit --stdin
      error: object fails fsck: badTreeSha1: invalid 'tree' line format - bad sha1
      fatal: refusing to create malformed object

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [defgsus/kindergarten-times](https://github.com/defgsus/kindergarten-times)@[55636fb3b1...](https://github.com/defgsus/kindergarten-times/commit/55636fb3b19ab5acf8b2cc3c1a27c80b8235cd64)
#### Wednesday 2023-03-15 13:24:52 by bergi

... so actually, we all have the cough.

One thing that helped regaining some energy was the IGORRR concert last night.
I think this fusion between metal and electronic breakbeat is just taking off.
Oh, there is also a lot of opera singing in this tour. One interesting thing to
see was the actual crowd of people. I've counted about 3 to 4,000 people, most
of them probably coming for Igorrr, while the support bands like Amenra or "Freiheit"
would normally attract metal-headz only, you know, those dark long-haired creatures
that only come to death metal concerts and are never to be seen anywhere else.
So, there where a couple of them to be recognized but all in all the crowd was
a nice mixture of fans of multiple genres. And! The Igorrr guy could have played
two hours more of jungle rythms at the end because the excitement was just exploding
through the roof. Well, it wasn't possible of course because the venue has a
clear contract and staff wants to go to sleep at some point.
Very interesting in any case.

---
## [MagiCircles/MagiCircles](https://github.com/MagiCircles/MagiCircles)@[73e6ace685...](https://github.com/MagiCircles/MagiCircles/commit/73e6ace685a21c8873fa23775396bf7d00a42d5a)
#### Wednesday 2023-03-15 13:31:53 by db0company

MagiFields are here! ↓ 🎨 ⚙️ 💔 🌐
- Collection level:
    - to_magifields
    - fields_class
- List view:
    - ordering_fields_class
    - table_fields_class
    - to_magifields
    - to_magi_ordering_fields
    - to_magi_table_fields
    - Deprecated:
        - to_fields, ordering_fields, table_fields
- Item view:
    - fields_suggest_edit
    - to_magifields
- Comments and Share buttons are now part of buttons_per_item
- Deprecated:
    - only_show_buttons in URL
- Collections migrated to MagiFields:
    - Accounts: uses MagiLeaderboardPositionModelField
    - Prizes: uses MagiICharacterModelField
- Fields itemview uses flexbox
- YouTube videos now show a thumbnail before loading and when the video is in a different language from English, it's gonna load the subtitles in that language (when available)

Faster loading of queries:
- Prefetch_together items:
    - in item view only
    - by limiting # of items loaded to: how many will be displayed + 1
    - doesn't work for account item view as it's always loaded within user item view
    - not loaded in high traffic mode (when logged out)
- Add/edit view:
    - get_queryset gets called to make sure there's no N+1 issue when showing model choice selectors

Tab item view:
- display_style_table_show_open_button now defaults to True

Alt views:
- Alt views get "loaded" on startup (when magicollections get initiated):
    - turned into OrderedDict
    - Choices and visible choices get cached
    - Alt views get added for collections set in FAVORITE_CHARACTERS_MODEL, OTHER_CHARACTERS_MODELS or BACKGROUNDS_MODEL
- Views with display_style "table" are now displayed using flex-box instead of table elements

Magicollections:
- New base class CommunityMainItemCollection, for magicollections expected to get filled by the community (smaller sites), as well as CommunitySubItemCollection and CommunityBaseEventCollection
    - Utils makeCollectionCommunity
- New utils in views: has_method_been_overridden, uses_deprecated_to_fields, notTranslatedWarning
- show_item_buttons_as_icons now defaults to True
- `view_icon` can be set for each view. they're currently used in staff page "collections" and in buttons to add/edit.
- List view:
    - new method check_random_permissions
    - deprecated: plain_default_ordering_list and plain_default_ordering
    - deprecated: show_owner in request.GET
- Rewrite of ListView
    - Parameters (request.GET or given to view function) wrapped in MagiQueryDict, allowing to handle both QueryDict and dict and wrapping the work of having multiple values, as well as determining wether the form was filled or not (ignoring known GET parameters not used in filters)
- ItemView:
    - New option: show_owner
    - New option: share_templates (Twitter/Instagram copy-pastable templates for community managers)

Forms:
- `request` may not be set in your form, so your code needs to handle that
- YouTubeVideoField now has modestbranding on and will suggest videos from the same channel only (at the end of the video playing)

Filter forms:
- Form will be instanciated on startup (when initializing collection objects) in order to cache some settings like suggest edit choices and filter details
    - so they now need to work when request=None. it will crash on startup if request is used without checking if it's not None, making it easy to debug this change
- Presets:
    - Presets now handle lists of values (ex: multiple activities tags!)
    - When someone uses the sidebar to search/filter, if the selected filters match a preset, then it will redirect to that preset, adding a nice header + helps with SEO
- If a URL contains some filters but not all, the missing filters will be filled with default values (previously: empty value, which was an issue for activities for example)
- New utility method: foreach_merge_fields
- When filtering by foreign keys, multi-level relationships now work too ("__")
- Merged filters:
    - Filters get unified. Ex: i_unit_i_subunit. If i_unit=3, then i_unit_i_subunit will be set to i_unit-3, and vice-versa
    - The merged filters themself are now noop filters, and it's the original filters that do the work of filtering
    - They now work with presets! (make sure your preset refers to the original field, not the merged field)
- Ordering fields show up right under search field (feedback that the "more" sections were assumed to be opened because of that field)
- New setting: ordering_show_relevant_fields (specify which fields to show, or [] for none)

Website settings:
- New settings: BACKGROUNDS_MODEL, BACKGROUNDS_FILTER, HAS_MANY_BACKGROUNDS, SHOW_BACKGROUND_NAME_ON_SELECTION, MAX_CACHED_BACKGROUNDS
- New settings: MANY_CHARACTERS_THRESHOLD, HAS_MANY_FAVORITE_CHARACTERS
- New settings: FEEDBACK_FORM_ANSWERS, EVENT_FEEDBACK_FORM, EVENT_FEEDBACK_FORM_ANSWERS, EVENT_PRIZES_FORM, EVENT_PRIZES_FORM_ANSWERS

Local settings:
- New: DEBUG_SHOW_QUERYSET, DEBUG_SHOW_MAGIFIELDS, DEBUG_SHOW_MAGIFIELDS_LIST

SEO:
- Json Ld now used on item view pages to describe the content of the page
  - FAQ (Q&A style section for item views)
  - Article (for activities + most items)
  - Videos (if any YouTube video is linked)

Settings page:
- If there are too many backgrounds, instead of selecting your background from a modal popup, you'll have to select it from a separate section of the settings page. This section will link to the backgrounds page itself, with a special view that shows buttons to set a background.
    - Default: 30 backgrounds. Can be changed with `MANY_BACKGROUNDS_THRESHOLD`. If you want to always set from the background view, then you can set HAS_MANY_BACKGROUNDS to True.
- If there are too many characters that can be set as favorite, instead of selecting your favorites from a modal popup, there will be a separate section in the settings page that allows you to view and set your favorite characters. When you set your favorite characters, it actually opens the collection list view instead, with a special view that shows buttons to set as favorite. This works for both the main "FAVORITE_CHARACTERS" (as long as you set FAVORITE_CHARACTERS_MODEL) and any "OTHER_CHARACTERS" you set up.
    - For FAVORITE_CHARACTERS: Default: 30 characters. Can be changed with MANY_CHARACTERS_THRESHOLD. If you want to always set from the list view regardless of how many characters there are, you can set HAS_MANY_FAVORITE_CHARACTERS to True.
    - For OTHER_CHARACTERS: Default: value of MANY_CHARACTERS_THRESHOLD, which is 30. Can be changed by setting `many_threshold` in your dict that sets up the other characters setings. To show regardless of how many, you can set `has_many` in your dict.
- New link option: linktree
- Staff and contributors can now update their settings directly from the settings page (mostly translators languages)

Item model classes:
- New util: d_unicodes
- New setting can be set to True: IS_PERSON
- Caches:
    - `total_` caches don't need `to_cache` methods, automatically retrieve total
- Can set {}_AUTO_IMAGES to i_, c_ and d_ fields to show an image. Can also specify: {}_AUTO_IMAGES_FROM_I to use int values and {}_AUTO_IMAGES_FOLDER to specify the folder name.

Suggest edit:
- suggest_edit_choices are now cached on startup (when initializing collection objects)

Utils:
- Global:
    - failSafe
    - recursiveCall
    - isFullURL, getDomainFromURL
    - hasValue
    - getValueIfNotProperty
    - validNullBoolOptions
    - classproperty
    - isRequestAjax
    - getSiteName
    - mergeDicts
- Collections / Models / items / queryset:
    - getOwnerFromItem, getAddressFromOwner, getTwitterFromOwner
    - getDescriptionFromItem
    - getMagiCollectionFromModel
    - reverseOrdering, reverseOrderingString, plainOrdering
    - getAllModelRelatedFields
    - fieldNameMatch
    - getListURL, isPreset, unifyMergedFields
    - prepareCache, will recursively transform any unsupported type into unicode, ensuring it never crashes
    - getRelatedItemFromItem, getRelatedItemsFromItem, getVerboseNameOfRelatedField, getFilterFieldNameOfRelatedItem
    - getAllModelFields, getAllModelRelatedFields
    - getRelOptionsDict, setRelOptionsDefaults, getMaxShownForPrefetchedTogether
    - getQuerysetFromModel
    - getColOffset
    - suggestFlaticonFromFieldName
    - baseButton
    - makeCollectionCommunity
- Translations (team A):
    - Format translated strings using `__`. Ex: __(_('Hello, {username}!'), username=_('Anonymous'))
    - Lowercase translated strings using `lowerTranslation`. Ex: lowerTranslation(_('Cards'))
    - Join translated strings using `joinTranslation`. Ex: joinTranslation([ _('A'), _('B'), ... ], separator=' ')
    - Translated name from an item or dict with `name` + `names` (or other field names) with `getTranslatedNameLazy`. Ex: getTranslatedNameLazy({ 'name': 'Maria', 'names': { 'ja': u'マリア' } }, language='ja')
    - getRomajiWithFallback
    - getLanguageImage
    - notTranslatedWarning
- Characters / Badges:
    - isValidCharacterPk, isValidCharacterNth, getCharacterEnglishNameFromPk, getCharactersHasMany, getCharactersKeys, getCharactersOtherExtraKey
    - getCharactersUsersFavorites, isCharactersUserFavorite, setCharactersUserFavorite, unsetCharactersUserFavorite
    - getMedalImage
- Seasons:
    - adventCalendar now checks for date server-side too (not just client-side only)
    - New utils: getAllCurrentSeasons, getValueInSeason, getVariableInSeason
- Json Ld:
    - jsonLd, FAQjsonLd, articleJsonLd, authorJsonLd, articleJsonLdFromActivity, articleJsonLdFromItem, videoJsonLd
- Social media:
    - tweetLength
    - isTweetTooLong
- Database migration:
    - New utils shift_i_choices
    - Doc: https://github.com/MagiCircles/MagiCircles/wiki/Save-choices-values-as-integer-rather-than-strings#adding-more-choices-in-the-future
- Renamed:
    - duplicate_translation → duplicateTranslations
    - find_all_translations → findAllTranslations
    - googleTranslateFixLanguage → rfc3066ToIso6392
- Updated:
    - getEventStatus now works if you compare dates with date times
    - listUnique new parameter: remove_empty=False
    - addParametersToURL now works with anchors (keeps existing anchor if any, replacing it if given)
    - redirectWhenNotAuthenticated now checks if request is None
    - Rewrite of getModelOfRelatedItem
    - formFieldFromOtherField now also copies MagiCircles specific values (in FORM_FIELDS_EXTRA_VALUES)
    - newOrder works with dict and allows to add dict values when missing, with option insert_in_dict_when_missing.
    - newOrder also allows `order` with a list of keys (useful for dicts!)
    - csvToDict does't crash when a title is missing in the row (one row shorter for ex)
    - makeBadgeImage takes either badge or badge_image + badge_rank
    - staticFileURL/staticImageURL more permissive: only path required
    - getColSize works with per_line = 8
- Deprecated:
    - toCountDownField, eventToCountDownField

Javascript:
- better loading of countdown, timeago, timezone, markdown, githubwiki,
- Better loading of next pages with pagination: will append tables to avoid having tables with different width columns
- when you open a modal:
    - it always shows the top of the modal
    - tooltips get hidden properly
- when you close a modal:
    - audio stops playing (if any in-modal audio)

Staff only changes:
- Collections view is prettier with "view_icon" displayed next to the links to the view
- edit_staff_status deprecated (the only way to change staff status is to set roles)
- Managers and desginers are now allowed to upload 2x
- New roles: Developer (Main), Wiki editor, Community entertainer (prizes)
- On profile, the button to edit user is now divided in multiple separate form depending on what you're trying to edit:
    - Mark e-mail address invalid
    - Edit roles
    - Edit donator status
    - And a separate form only accessible from reports, when you're editing a user that has been reported. It's separated in 2 forms: one for description, location and force remove avatar, and one for username/email
- When ordering users or accounts by most popular, will show reputation points ()
- Reports: can't lookup reports by staff (too heavy query)
- Profiles now show icons of staff roles under the avatar

Other:
- Link to "Contact us" in navbar (links to about page with anchor)
- Activities titles (for SEO and social media share) is now auto-retrieved from h1 to h5 titles
- fix bug with share_url in base account (was not a property)
- Add labels to _cache_leaderboard (now used)
- Tried my best to make sure untranslated strings show up with a warning in DEBUG mode so that developers notice it (mostly for model field names)
- post_news given to Managers as well
- icon_for_prefetched deprecated (not used by any site anyway)
- Dump model data for local import: make sure it doesn't print out useless things
- List of contest participants: new option --print-table
- CSS: new classes col-XX-special-8 and col-XX-offset-special, where XX is the size (xs, sm, md, lg), new class nowrap, new class padding5, stripes on staff-only stuff
- Better SEO tags in base header
- Remove Maji Love from list of sites
- Events now use new MagiFields stuff
- Bug fix: when ko-fi doesn't get loaded, don't crash
- Translations: Facebook/Reddit/Twitter/Instagram/YouTube are now translatable
- Bug fix: Markdown help text doesn't open in the same modal if the current form has been opened in a modal
- Rename website → app
- Rewrote default introduction (about page)
- Various bug fixes

Breaking changes:

New signature for:
- MagiCollection.get_queryset(self, view=None, queryset=None, parameters={}, request=None):
- All views get_queryset(self, queryset=None, parameters={}, request=None):
This means we should be able to call `some_collection.get_queryset()` without it failing because it relied on queryset, parameters or request.

- `request` may not be set in your form, so your code needs to handle that

---
## [denaxen/awesome-chatgpt-prompts](https://github.com/denaxen/awesome-chatgpt-prompts)@[2491289e38...](https://github.com/denaxen/awesome-chatgpt-prompts/commit/2491289e38f14f663a631f6a715ab11d105075bf)
#### Wednesday 2023-03-15 14:05:35 by Daniil Likhobaba

"Act like a human"

This prompt makes chatGPT act like a human. Sometimes it's better to receive like-a-human answers instead of stuffy complicated texts. This is also useful because such smart texts are obviously generated by artificial intelligence, and prompt "Act like a human" allows one to get texts similar to human ones.

There are some simple examples:

- Question: "What color is the sky?"
- ChatGPT: "The color of the sky can vary depending on different factors such as the time of day, weather conditions, and geographic location. During the day, the sky is usually blue, but it can sometimes appear gray or even red during sunrise or sunset. At night, the sky is dark, but it can be illuminated by the moon and stars."
- "Act like a human" prompt: "Blue."

- Question: "Why is the grass green?"
- ChatGPT: "Grass appears green to our eyes because of a pigment called chlorophyll. Chlorophyll is the molecule that is responsible for capturing light energy during the process of photosynthesis, which allows plants to convert sunlight into food. 
Chlorophyll absorbs light in the blue and red parts of the spectrum, but reflects green light, giving the grass its green color. This is also why many other plants appear green to us. However, some plants have different pigments that can give them different colors, such as carotenoids, which give carrots their orange color, or anthocyanins, which give red grapes their color. 
It's worth noting that the color we perceive can also be affected by factors such as lighting conditions, the angle of the light, and the structure of the grass blades themselves."
- "Act like a human" prompt: "Grass is green because it contains chlorophyll, which absorbs blue and red light and reflects green light."

- Question: "Why it's dark at night?"
- ChatGPT: "It is dark at night because the Earth rotates on its axis, causing the side facing away from the sun to be in darkness. During daylight hours, the sun's rays reach the Earth's surface and provide light, but when the Earth rotates away from the sun, that light is no longer present, resulting in darkness. Additionally, the absence of sunlight allows the stars and other celestial bodies to become visible, creating a beautiful and awe-inspiring night sky."
- "Act like a human" prompt: "It's dark at night because the sun is on the other side of the Earth and its light cannot reach us."

---
## [Arceveti/HackerSM64](https://github.com/Arceveti/HackerSM64)@[ef38abb1c0...](https://github.com/Arceveti/HackerSM64/commit/ef38abb1c0c2b39536e2a1a04003bc10556f5cb1)
#### Wednesday 2023-03-15 14:59:54 by Fazana

Frustratio funny fix 2 (#593)

* Update game_init.c

* fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo fuck you nintendo

---
## [Cenrus/tgstation](https://github.com/Cenrus/tgstation)@[6de1258bd3...](https://github.com/Cenrus/tgstation/commit/6de1258bd3fb5919bb45f3dac3ae801d4b3bc8d6)
#### Wednesday 2023-03-15 15:04:13 by Jacquerel

Admins can now choose where fish go (#73109)

## About The Pull Request

I've pigeonholed myself as the fish guy now. It seems like someone made
events easier to add admin controls for so I thought I'd add some to the
event I most recently touched.

Instead of letting the RNG choose admins can now direct a circle of carp
to converge upon a specific location, or even a trail of specific
locations if they want the carp to just sort of swim in a circle around
the space station (although the ones on the far side of the station from
the starting point will travel all the way through it to get there).
This also works with magicarp.
They don't really move fast enough for you to use this to punish a
specific person but you can use it to annoy a specific location full of
people.

Plausibly there's no reason the code _wouldn't_ work for a specified
atom instead of a turf (as long as it sticks to one z level) but I
couldn't think of an elegant way of selecting that whereas "use my
current ghost location" is very intuitive, so I didn't add one.

## Why It's Good For The Game

Plausibly this permits admins do more fun things.

## Changelog

:cl:
admin: Admins can direct where carp (or magicarp) are interested in
going when manually triggering the event
/:cl:

---
## [Sea-of-Lost-Souls/Tannhauser-Gate](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate)@[6c978308c7...](https://github.com/Sea-of-Lost-Souls/Tannhauser-Gate/commit/6c978308c71cbd5b24e3242aec42b227461f9aaa)
#### Wednesday 2023-03-15 15:44:56 by SkyratBot

[MIRROR] Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost [MDB IGNORE] (#19743)

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost (#73814)

## About The Pull Request

So we're like simultaneously moving two vague directions with research.
One being "experisci grants discounts for prohibitively expensive nodes
so you want to do the experiments to discount them" and the other being
"Let's give Heads of Staff a way to research anything they want without
any communication to the research department, including the very
expensive nodes that scientists may be working on"

You already see the issue, right? You can't have your cake and eat it
too.

It sucks for scientists to be working on a complex experiment like
weapons tech for that huge 90% discount only for the HoS to stumble onto
the bridge and research it anyways. Your time is wasted and RND is
slowed down massively.

We can do something to assuage that.

This PR makes it so completing an experiment which discounts already
completed nodes will refund a partial amount of the discount that
would've applied.

For example, researching industrial engineering without scanning the
iron toilets will refund ~5000 points.

This can only apply once per experiment, so if an experiment discounts
multiple technologies, they will only get a refund based on the first
technology researched.

## Why It's Good For The Game

This accomplishes the following:

- Expensive research nodes with difficult experiments remain expensive
without completing the experiments. If no one does the experiment, they
act the same as before.
- Expensive research nodes with very easy experiments (but time
consuming) no longer put RND on a time crunch to beat the itchy trigger
finger of the Heads of Staff. Stuff like scanning lathes allow the
scientists to work more at their own pace: they can talk to people or
maybe stop at the bar or kitchen between departments without feeling
pressure to get it done urgently.
- Scientists are able to complete experiments which previously were no
longer deemed relevant if they need a point injection. Experiments left
behind are no longer completely useless bricks. Maybe even gives
latejoin scientists something to do.
- Scientists mid experiment can still complete it to not feel like their
time is wasted.

Overall I think this has many benefits to the current science system
where many have complaints.

## Changelog

:cl: Melbert
qol: Completing an experiment which discounts a researched tech node
will give a partial refund of the discount lost. For example,
researching the industrial engineering research without scanning iron
toilets will refund ~5000 points if you complete it afterwards. This
only applies once per experiment, so experiments which discount multiple
nodes only refund the first researched.
/:cl:

---------

Co-authored-by: san7890 <the@ san7890.com>

* Completing experiments after their associated nodes have been researched gives back a partial refund of the discount lost

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: san7890 <the@ san7890.com>

---
## [bigcoder69/PythonLearningCode](https://github.com/bigcoder69/PythonLearningCode)@[3b4722108c...](https://github.com/bigcoder69/PythonLearningCode/commit/3b4722108cb299a0553a449ccb3b8b57b5d8ce11)
#### Wednesday 2023-03-15 16:08:17 by bigcoder69

familycounter.py

This family counter counts the number of boys and girls are there in the family, then gives you the result!
If you have very little experience this great because it goes over core topics for your python learning journey. Happy coding!

---
## [SLASHEM-Extended/SLASHEM-Extended](https://github.com/SLASHEM-Extended/SLASHEM-Extended)@[7df5fb6a18...](https://github.com/SLASHEM-Extended/SLASHEM-Extended/commit/7df5fb6a18840014f62dcb5a3f5b13b840f81abc)
#### Wednesday 2023-03-15 16:23:10 by AmyBSOD

holy shit what a bug

Gotta give credit where it's due, so... thanks entrez for finding this bug and thanks PatR for implementing a fix. Yeah, this is one of the extremely rare cases where even the 3.7 devteam makes an actually good change that is then pulled into SLEX.

---
## [hyperledger-labs/perun-rs](https://github.com/hyperledger-labs/perun-rs)@[e233238f5a...](https://github.com/hyperledger-labs/perun-rs/commit/e233238f5a2c5d998288ddc413dd4bda10eef54e)
#### Wednesday 2023-03-15 16:23:51 by Jens

channel: Implement applying channel updates

I'm not completely happy with the current solution, but it will have to
suffice for now. We basically have the following options:
- Store new-state + new-signatures in the ActiveChannel object. This
  would basically combine two states from the Go state-machine into one,
  removing any static checks on when a signature could be added for
  example. We should probably avoid this unless we have to. It has the
  downside of making the channel object bigger, especially when not using
  heap allocation.
- Store an immutable reference in the ChannelUpdate. This would allow
  creating multiple proposed updates with the same version number, but
  it leads to big problems when trying to apply the new state. The
  ChannelUpdate only has an immutable reference and we thus have to give
  it a mutable reference or call a mutable reference function on the
  channel. Alternatively the caller would have to somehow remove the
  reference before calling. I could not get this to work. Perhaps it is
  possible if the channel is moved into the function and back out
  afterwards. Regardless, this has a conceptual problem: We'd have to
  invalidate (drop) all other pending channel updates. In theory this
  sounds great, exactly what we want, but in practice difficult to do.
  Perhaps possible with some lifetime magic.
- Store a mutable reference in the ChannelUpdate. What we currently do.
  It prevents the user from creating two simultaneously existing
  ChannelUpdates, which _might_ be what we want. The more annoying issue
  is that the underlying channel can probably not be used at all (not
  even read from), since that would require creating an immutable
  reference. It is basically like the channel does not exist, but you
  have to keep it stored somewhere, since it is referenced by the
  ChannelUpdate. I might be wrong about not being able to use the
  channel in read-only mode.
- Move the channel into the ChannelUpdate (or create a
  UpdatePendingChannel) representing this phase. This would probably be
  closest to the Go-code. It means the user of the low-level api only
  has to bother about one object, less lifetimes, less references. It
  also means that allowing multiple simultaneous updates may get
  difficult in the future unless storing a list of pending updates. This
  might be our best option for the long term.
- Don't bother with references and instead use the channel id (the
  caller has to give the correct object). This completely bypasses the
  borrow-checker (not sure if we want that) and will require additional
  runtime-checks, as well as additional error cases.

Signed-off-by: Jens <jens@perun.network>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[61e5d61bc3...](https://github.com/mrakgr/The-Spiral-Language/commit/61e5d61bc3bf097122a9f31e18889ea22afb26fd)
#### Wednesday 2023-03-15 17:02:09 by Marko Grdinić

"8:15am. I am up. Somehow using games to push myself to brink leads to me falling into deep slumber. Today, my agenda is to finish CFR, but before that, I am overdue for a bath. Let me chill and then I will get to that.

https://www.reddit.com/r/MachineLearning/comments/11rizyb/d_anyone_else_witnessing_a_panic_inside_nlp_orgs/
> Let me tell you about quants : they do more math, they get more money and what do they do? They clean data to be fed into linear models.

9:40am. Done with the bath.

Let me get started.

10:35am. Let me resume. I gave myself the neti pot treatment and I'll see whether it makes a difference. Next time I'll do it more efficiently. I should let the salt dissolve in the glass after I microwaved it instead of putting in the neti pot and stirring later. That was foolish of me.

12:40pm. Let me pause here. So far I have 7:06m of the screecast recorded. Now I'll finally implement the update function for the CFR algorithm.

Maybe instead of fucking around and making these videos nobody will ever care to watch, I should just move on to interviewing.io instead? Let me jus finish this video, and then I will send out my faux resume to a couple of companies just to see what the response is.

I am not sure what I should be doing in this situation, but it is certainly not spending my entire days to make 7m of video. I'll finish this one though, definitely.

https://www.youtube.com/watch?v=7Pq-S557XQU
Humans Need Not Apply

1:25pm. Let me do the chores here. I want to resume quickly.

1:50pm. Let me resume.

2pm. Fuck Camtasia with a spoon. Why did it eat my most recently recorded video. Son a bitch.

...I realized it why. I really should be setting the option to display by date added. I rerecorded it, but once I found the setting, it showed me my old video near the top. Sigh. This happened once or twice before today, I think.

3pm. My god, my god! When I talk it builds up pressure inside my skull. And when I finish the sentence, the tension gets released and the there is a pop in my nasal pssage. The microphone picks it up every time. It is actually really difficult to blow some air at the end so that the pop happens later when I can cut it off.

Right now, this is my biggest enemy. I've gotten used to reciting, but this particular issue is just hard for me to deal with. Sometimes blowing air at the end works, but the click often happens before I can initiate it.

3:10pm. >  It would never learn anything in that situation.

I am trying to say this sentence without a pop at the end and it is killing me. It is not a matter of controlling pronounciation, it happens from somewhere inside my nasal passage once the pressure releases at the end.

https://www.sonnox.com/plugin/oxford-declicker

There are a ton of these plugins for this thing.

https://www.reddit.com/r/Reaper/comments/a4ol3w/how_to_achieve_a_midword_click_correction/

> Thanks! Luckily I nabbed iZotope de-click and de-noise during one of there sales. These two plugins save me literal hours, I don't want to remember life before them.

https://www.izotope.com/en/products/rx/features/de-click.html

It is on sale right now.

3:25pm. Instead of getting that, I am getting the advanced version from one of the warez sites I've stumbled upon back when I was trying to find Audiate. In hindsight, the reason why I couldn't find that one for free is most likely due to it being a cloud service. The pirates can't crack the TechSmith server. But this is different.

Had I known about it, I would have gotten Izotope Rx 10 Advanced, but I only found out about this program in the last 10 minutes. The only reason why I knew about the Izotope Declicker is because that Creators Village guy mentioned it. I looked for Izotope and here it is.

I guess it was a good thing I took a trip through the warezhouse. On IGetIntoPC there is only an order version. I found the most up to date version on DirtyWarez. Of course, you can't count on Google giving the good stuff to you these days. The best search engine would be Yandex at this date.

3:35pm. This distracted me. I'll put my faith in the program, but while it downloads, let me just continue recording in Camtasia. I'll stop putting so much effort in getting rid of the clicks manually and let the Rx take care of it later.

Having to constantly do this kind of editing is really killing both my pace and motivation.

3:40pm. Had to do a chore. Let me resume.

5:50pm. 13 full minutes today. It would really be much easier to do the script in its entirety. Task switching between talking and writing leads to delays.

5:55pm. I am not done with the video. What I need to do is introduce a new tab in the UI for training the agents. Something to act as a training board. I'll also look into charting here.

Right now, weirdly I am still not tired, but I did get up at 8am, so I should just take it easy and stop. The stress will go up easily enough once I cross a line. It is better to just be satisfied with a job well done.

If I want to do anything, why don't I check out a few Rx 10 tutorials and install the audio editor while I am at it? That would be for the best."

---
## [keflavich/spectral-cube](https://github.com/keflavich/spectral-cube)@[8747c377e1...](https://github.com/keflavich/spectral-cube/commit/8747c377e190c0f5d193f9dd9916e1fe4b4af1c1)
#### Wednesday 2023-03-15 17:34:39 by Adam Ginsburg

Expand test coverage (#854)

* try to expand test coverage

expand test coverage

fix test failure for dask

trivial whitespace change?

try to emulate https://github.com/astropy/astroquery/pull/2626

that last one seems to maybe have broken CI?  undoing the CI changes

try putting things on one line ?

try changing ubuntu-latest to linux based on the versions-manifest, which doesn't mention ubuntu at all

try changing 3.10 -> '3.10' instead of the linux change

shorten job names so we can see the whole name in the sidebar of gh-actions

add a mask setter to solve problem where numpy masked arrays are trying
to set the mask attribute but being blocked from doing so

drop openfiles b/c it's deprecated (not sure what we're supposed to
replace it with yet)

make some of the failing tests more extensive and explicit

* split a test onto more lines to try to pin down where the error is coming from (pdb revealed that code that succeeded on the previous line is the direct source of this failure)

fix mistake

add a new test for "all"

add all-dev and remove -openfiles from windoze

move dev dependenc installs from tox to setup.cfg

whitespace and naming

expand test coverage yet again: try dev w/o novis/all

separate out 'viz' from 'noviz'

fix a typo....

add extras that were all missing into tox.ini

make sure basic tests use latest numpy

rearrange and make tests more granular still

drop 3.7 from grid b/c astropy 5.2.1 doesn't support it

see if pvextractor can be included in the "good" viz

hack around astropy 14514

hack needs to be hackier b/c _new_view didn't always have finalize= option

try to run tests w/dev branch

fix syntax

fix install url

fix name again?

try to fix last exception

allow for three types of error?  this might not be the right approach

fix test again

remove mask setter - I'm not sure it was actually needed, I think that might have been a side-effect error caused by something else?  Pushing this to run tests to check; may neeed to partially revert this if tests fail

set ndim

fix the naxis defn

restore the mask setter, it _is_ needed

reproject high_level_wcs fix merged; revert to master in tests

fix names of # of dims

* revert to my branch, even though it was merged, to see if that can make tests go green again

* try using astropy nightly wheels.  This might inadvertently make tests go green for <24h b/c the breaking change is <8h old, but the intent is to make builds faster

change order of commands

oh, I just had stupidly pasted in setup.cfg too

* put some sticky tape over the check engine light.

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[5b794e55e9...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/5b794e55e92db97baa5ec0b23170907d821bee23)
#### Wednesday 2023-03-15 17:57:59 by Adam Joseph

stdenv: Nix-driven bootstrap of gcc

 #### Summary

By default, when you type `make`, GCC will compile itself three
times.  This PR inhibits that behavior by configuring GCC with
`--disable-bootstrap`, and reimplements the triple-rebuild using
Nix rather than `make`/`sh`.

 #### Immediate Benefits

- Allow `gcc11` and `gcc12` on `aarch64` (without needing new
  `bootstrapFiles`)
- Faster stdenv rebuilds: the third compilation of gcc
  (i.e. stageCompare) is no longer a `drvInput` of the final stdenv.
  This allows Nix to build stageCompare in parallel with the rest of
  nixpkgs instead of in series.
- No more copying `libgcc_s` out of the bootstrap-files or other
  derivations
- No more Frankenstein compiler: the final gcc and the libraries it
  links against (mpfr, mpc, isl, glibc) are all built by the same
  compiler (xgcc) instead of a mixture of the bootstrapFiles'
  compiler and xgcc.
- No more [static lib{mpfr,mpc,gmp,isl}.a hack]
- Many other small `stdenv` hacks eliminated
- `gcc` and `clang` share the same codepath for more of `cc-wrapper`.

 #### Future Benefits

- This should allow using a [foreign] `bootstrap-files` so long as
  `hostPlatform.canExecute bootstrapFiles`.
- This should allow each of the libraries that ship with `gcc`
  (lib{backtrace, atomic, cc1, decnumber, ffi, gomp, iberty,
  offloadatomic, quadmath, sanitizer, ssp, stdc++-v3, vtv}) to be
  built in separate (one-liner) derivations which `inherit src;`
  from `gcc`, much like https://github.com/NixOS/nixpkgs/pull/132343

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
## [jedjoud10/cflake-engine](https://github.com/jedjoud10/cflake-engine)@[b0145e956e...](https://github.com/jedjoud10/cflake-engine/commit/b0145e956e71409a9b1c023813b4b50eefa0915d)
#### Wednesday 2023-03-15 18:00:23 by jedjoud10

Holy shit it truly is asynchronous that's insane bro

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[d261466765...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/d2614667654c0e35b2c906971ca94ece9e7b8629)
#### Wednesday 2023-03-15 18:49:04 by IrkallaEpsilon

Scattershot nerfs (#5175)

Sniper laser was tame.

## About The Pull Request

This is bullshit. Splurting out 180 damage with high AP with no delay is
not okay. Its as bullshit as most FCU we had. Mainly removed scatter on
high powered lasers and bloody stuns so the scatter lense may stay for
the mining tool (as there is no way to increase firerate on a
projectile.

## Why It's Good For The Game

Ever got hit at close range by the particle defender on main? Yeah that
is not fun.

## Changelog
:cl:
balance: Scattershot on high powered weapons nerfed. Heavy laser and
laser cannon beam and electrode now wont create submunitions. Stun beam
submunition count lowered.
/:cl:

---
## [SDP-GeoHunt/geo-hunt](https://github.com/SDP-GeoHunt/geo-hunt)@[f9251b69f7...](https://github.com/SDP-GeoHunt/geo-hunt/commit/f9251b69f7619f194275af5f78673368a1de171b)
#### Wednesday 2023-03-15 18:52:47 by Marwan

Compose migration (#26)

* Modify configuration files to support Kotlin & Jetpack Compose

As discussed this morning, we plan on moving to Kotlin and Jetpack compose. This commit marks the beginning of the modification to make it.

* Update minSdk to comply with firebase requirement

Changes:
* Change from minSdk:24 to minSdk:28 to comply with the firebase
  realtime database requirements

* Delete old java activity file and write basic test

Changes:
* Remove `GreetingActivity.java` and `MainActivity.java` and
  dependencies
* Write simple `ComposeActvitityTest.kt`

* fix: Support for coverage with Kotlin

* Added Mockito

* Fixed the build.gradle with proper versions

* :fire: :100: :triump: base :rage:

---------

Co-authored-by: BoyeGuillaume <guillaume.boye@epfl.ch>

---
## [leoplace71/ARC-9](https://github.com/leoplace71/ARC-9)@[bab0e24906...](https://github.com/leoplace71/ARC-9/commit/bab0e249064fc65adfedb5de4b21ab2f858952b6)
#### Wednesday 2023-03-15 19:07:03 by Darsu

consistent mp/server recoil with sp god i hate this fucking base and whoever made this visual recoil

---
## [Dimasw99/Citadel-Station-13-RP](https://github.com/Dimasw99/Citadel-Station-13-RP)@[b9313e344b...](https://github.com/Dimasw99/Citadel-Station-13-RP/commit/b9313e344b7b468f2e68d428e69c19503e3833b8)
#### Wednesday 2023-03-15 19:44:02 by Keekenox

Fix Keek's Offset Sprites Finally (#5135)

Keekenox has fixed the pixel offsets for sprite assets, which is a
crucial improvement to the game. In the previous version, some sprites
appeared blurry and misaligned, making the game look unprofessional and
unpolished. With this commit, the sprites are correctly aligned,
improving the overall visual quality of the game. This is important
because it enhances the player experience and makes the game more
enjoyable.

Firstly, fixing the pixel offsets ensures that the sprites display
accurately across all devices and platforms. With the increasing
popularity of gaming on different devices, it is essential that the game
looks good and functions well across all of them. Inconsistent display
of assets can be frustrating for players and negatively impact their
experience. By addressing this issue, Keekenox has taken a step towards
creating a more accessible game, which can be played by a wider
audience.

Secondly, fixing the pixel offsets is important for the branding of the
game. The look and feel of the game are integral to creating a strong
brand image. The blurry and misaligned sprites make the game look less
polished and unprofessional. With the visual improvements from this
commit, the game now looks more visually appealing, and its brand image
is strengthened. This can lead to increased engagement, higher retention
rates, and better marketing opportunities.

Thirdly, by fixing the pixel offsets, Keekenox has made the game more
scalable. As the game grows and more assets are added, the risk of
misaligned and blurry sprites increases. By addressing this issue early
on, Keekenox has prevented potential headaches down the road, saving
time and resources in the long run. This demonstrates a commitment to
quality and attention to detail that players appreciate and respect.

Fourthly, fixing the pixel offsets is important for maintaining the
quality of the game. Players expect games to look and feel polished,
with attention given to even the smallest details. The misaligned and
blurry sprites detract from the overall quality of the game, leaving
players with a negative impression. By fixing this issue, Keekenox has
shown that they care about their players' experience and are committed
to delivering a high-quality game.

Lastly, fixing the pixel offsets has a direct impact on the player
experience. Games are meant to be enjoyable, and players want to immerse
themselves in a world that looks and feels great. Misaligned and blurry
sprites can be distracting and detract from the experience, making it
less enjoyable for the player. With the improvements made in this
commit, players can now enjoy the game without these distractions,
leading to increased satisfaction and potentially higher retention
rates.

In summary, fixing the pixel offsets for sprite assets is an important
improvement to the game. It ensures accurate display across all devices,
strengthens the brand image, improves scalability, maintains quality,
and enhances the player experience. Keekenox has demonstrated a
commitment to delivering a high-quality game, and players will
appreciate the attention to detail that went into this improvement.

---
## [kala-nea/ScalawagSeas](https://github.com/kala-nea/ScalawagSeas)@[9dad1e189c...](https://github.com/kala-nea/ScalawagSeas/commit/9dad1e189ccd2c15933f437535015625a542200e)
#### Wednesday 2023-03-15 19:45:57 by Colby Kirk

placeholder logo

I see a ghost, a spirit
Walking on the water
He bids me come to Him
Without a boat
To walk upon the sea

So I jump over the edge
And take a step upon the water
I’m getting closer
As I feel the sea move
Underneath my feet

[Pre-Chorus]
I feel the wind and hear
The roar of waves
That crash around me
And when they get their hold on me
I feel I’m going down
Please don’t let me drown

[Chorus]
Like Peter all those years ago
Who looked away and sank below
When I sink in seas of doubt
Will You take my hand and pull me out?
The devil and the deep blue sea
With open arms awaiting me
But I won’t go down tonight
If I keep my eyes on You, I’ll be alright

[Verse 2]
God, the storms are heavy
And the waves have beaten me down
And the winds have turned me
Every which way
Round and round and round

It’s so hard to focus
But I don’t want to look away
Even when the waves grow higher
Every day
Higher every day

You might also like
Altar to the Unknown God
Theocracy
30 Pieces of Silver
Theocracy
I Am
Theocracy

[Chorus]
Like Peter all those years ago
Who looked away and sank below
When I sink in seas of doubt
Will You take my hand and pull me out?
The devil and the deep blue sea
With open arms awaiting me
But I won’t go down tonight
If I keep my eyes on You, I’ll be alright

[Bridge]
Waves and whirlwinds turn my eyes
Raging under threatening skies
The miracles of yesterday
Can sometimes seem so far away
Oh we of little faith, how quickly we forget

[Guitar Solo]

[Outro]
Tired and battered by the waves
Won’t let the waters be my grave
Devotion deeper than the sea
The ocean’s tide won’t swallow me
A hand is reaching
I grab it and rise

---
## [goober3/hi-github-portside](https://github.com/goober3/hi-github-portside)@[31eabb62f1...](https://github.com/goober3/hi-github-portside/commit/31eabb62f1bfe944a58fa6b74d1745cf80cb83aa)
#### Wednesday 2023-03-15 20:33:11 by spockye

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
## [joshjohanning/ghas-enablement](https://github.com/joshjohanning/ghas-enablement)@[c32bab9ba1...](https://github.com/joshjohanning/ghas-enablement/commit/c32bab9ba13c0d5e9d577b38e8c954fc9efa5916)
#### Wednesday 2023-03-15 21:24:02 by Dominique Thornton DJ

Features & Refactors (#64)

* chore: :wrench: Rename repos.json

This change is to allow repos.json & organizations.json to be added
to gitignore so that privacy can be maintained in private organizations.

* feat: :sparkles: Add missing java codeql file

Not sure if this was intentional, but a java codeql file doesn't exists.
This commit introduces the file

* chore: :arrow_up: Update deps

Update documentation. `Yarn add` expects a package. The equivalent of npm
install (install all deps)ya is `yarn install` or just `yarn`

See: https://classic.yarnpkg.com/lang/en/docs/cli/install/

* feat: :sparkles: Simplify destDir, user, add root

This commit attempts to simplify the determination of the destination
directory and username. It also introduces the root for user home to be
used in later feature.

* refactor: :recycle: command refactor

This commit is largely a refactor of the existing code. The point is to
simplify the commands required for windows/macos/linux. They largely
all use the same commands with slight variations, such as home
directory, and command arguments.

It is a larger commit than I'd like, but all three file changes do go
together.

globals.ts:
- Removes the need to create separate vars for windows vs
everything else. Determine the differences in globals and send 1 var.
- Determine OS here so we can set root to home path. No longer needed
in commitFile.ts

commands.ts:
- Squash windows/macOS/linux into a single command array.
- Introduce platform and root to differ commands/paths
- Remove unnecessary commands like mv as cp can accomplish this
- Make commands/arguments conditional
- Add helper function to convert linux paths to windows paths
  - This really helps with mkdir as Windows can natively create
    multi-leveled directory structures when correct paths are used: `\`

commitFile.ts:
- Moved existsSync, os and isCodespace to globals.ts
- Replaced mac/windowsCommands w/ genearlCommands
- Simplified gitCommands condition
- Added informs
- Added try catch to "for loop" of commands. I may just be missing it,
  but the If (stderr) block didn't seem to be activating. The app would
  die after stating the error.
- Whitelist function for known error responses like this folder alredy
  exists and can't delete a folder that doesn't exists.

The whitelist function feels hacky, so I welcome any thoughts on it.

* feat: :sparkles: ISSUE-61 PR comments

This commit contains the recommended changes from Nick.

1. globals consolidates all OS types to a common cwd under destdir
2. The commands.ts file consolidates all commands into a single list
3. Backticks are used in string block.

Also introduces user specified temp directory. It turns out I don't
have a ~/Desktop thanks to OneDrive.

ISSUE-61

---
## [goanpeca/napari](https://github.com/goanpeca/napari)@[3ec4be1ae8...](https://github.com/goanpeca/napari/commit/3ec4be1ae8eee50ab4912ba87981261cc94c075f)
#### Wednesday 2023-03-15 22:53:22 by Grzegorz Bokota

Incorret theme should not prevent napari from start (#5605)

# Description
<!-- What does this pull request (PR) do? Why is it necessary? -->
<!-- Tell us about your new feature, improvement, or fix! -->
<!-- If your change includes user interface changes, please add an
image, or an animation "An image is worth a thousand words!" -->
<!-- You can use https://www.cockos.com/licecap/ or similar to create
animations -->

For the current implementation, the error in theme registration prevents
the napari form from starting. It may be problematic for bundle users.

In this PR I add `try: ... except` to handle an error during theme
registration and convert it to logging exceptions. I use logging because
it happened before creating GUI.

## Type of change
<!-- Please delete options that are not relevant. -->
- [x] Bug-fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] This change requires a documentation update

# References
<!-- What resources, documentation, and guides were used in the creation
of this PR? -->
<!-- If this is a bug-fix or otherwise resolves an issue, reference it
here with "closes #(issue)" -->

# How has this been tested?
<!-- Please describe the tests that you ran to verify your changes. -->
- [ ] example: the test suite for my feature covers cases x, y, and z
- [ ] example: all tests pass with my change
- [ ] example: I check if my changes works with both PySide and PyQt
backends
      as there are small differences between the two Qt bindings.  

Install `napari-gruvbox`, `pygments==2.6` (bellow 2.9) and start napari 

Example error message:
```python-traceback
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-dark provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
11:52:01 ERROR Registration theme failed.
1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
Traceback (most recent call last):
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 391, in _install_npe2_themes
    register_theme(theme.id, theme_dict, manifest.name)
  File "/home/czaki/Projekty/napari/napari/utils/theme.py", line 266, in register_theme
    theme = Theme(**theme)
  File "/home/czaki/Projekty/napari/napari/utils/events/evented_model.py", line 200, in __init__
    super().__init__(**kwargs)
  File "pydantic/main.py", line 342, in pydantic.main.BaseModel.__init__
pydantic.error_wrappers.ValidationError: 1 validation error for Theme
syntax_style
  Incorrect `syntax_style` value: gruvbox-light provided. Please use one of the following:  default, emacs, friendly, colorful, autumn, murphy, manni, monokai, perldoc, pastie, borland, trac, native, fruity, bw, vim, vs, tango, rrt, xcode, igor, paraiso-light, paraiso-dark, lovelace, algol, algol_nu, arduino, rainbow_dash, abap, solarized-dark, solarized-light, sas, stata, stata-light, stata-dark, inkpot (type=assertion_error)
```

## Final checklist:
- [ ] My PR is the minimum possible work for the desired functionality
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] I have added tests that prove my fix is effective or that my
feature works
- [ ] If I included new strings, I have used `trans.` to make them
localizable.
For more information see our [translations
guide](https://napari.org/developers/translations.html).

---------

Co-authored-by: Lorenzo Gaifas <brisvag@gmail.com>

---
## [heady8354/Video-Game-Project](https://github.com/heady8354/Video-Game-Project)@[deda8a697e...](https://github.com/heady8354/Video-Game-Project/commit/deda8a697e7acfaddd851a8fcb050371a22604fd)
#### Wednesday 2023-03-15 23:05:20 by heady8354

success but not really

turns out im NOT that retarded and the issue I was having was that i was using names embedded in the code or whatever that cant be used as file names such as location and name. silly me. anyways, I will continue development tonight because i just wanted to fix my issue and not actually do anything. also im playing golf tonight so thatll be fun. if I win, ill work extra hard and maybe try to implemennt a golf minigame.

---
## [tequilaOS/platform_frameworks_base](https://github.com/tequilaOS/platform_frameworks_base)@[d741f9de8c...](https://github.com/tequilaOS/platform_frameworks_base/commit/d741f9de8c59f29270d67c18eca4cf479363dafd)
#### Wednesday 2023-03-15 23:43:48 by Kuba Wojciechowski

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

---
## [REDLAERT88/sojourn-station](https://github.com/REDLAERT88/sojourn-station)@[8620d970b0...](https://github.com/REDLAERT88/sojourn-station/commit/8620d970b0aaa8d632e83a4dcc35547826f555df)
#### Wednesday 2023-03-15 23:54:40 by DimmaDunk

Shields, sounds, holsters and more (#4169)

* Shields, sounds, holsters and more

- Better sound for blocking with shields, also sounds for stopping projectiles with them (and breaking)
- Ports the double belt pistol holder (pouch) and throwing knives rig (pouch) from Eris. With belt-worn sprites made by me.
- Adds the belt pistol holster and knife rig to the marshal vendors and absolutist printing disk
- Ports the Bulldozer shield from Eris, tweaks its recipe to include an actual closet
- Makes suit sensors spike in danger if someone's toxloss is at 70 or higher, since that is the point of liver failure
- On the same note, reduces the amount of organ damage from MSOF as it was too punishing, allowing for a better window of opportunity to save someone from dying
- Makes deployable barriers needed to be anchored to be able to brace your gun on it
- Adds most types of holsters to marshals vendors, ups their quantity
- Soteria Gauze and Ointment buffed on par with Church ones, to justify their convoluted hand-crafting method
- Makeshift AK and Luty added to random handmade guns to spawn
- Rangers get the double holster instead of the single one
- Adds a generic katana to loadout for four points
- Adds better sounds for the following emotes: male and female *sigh, *whistle (more variety), female *urah
- Adds snort and awhistle (targeted) emotes
- Makes a lot of audible emotes actually check if you're muzzled instead of magically being executed despite mouth coverage
- Adds some of the missing emotes to the *help list
- Adds hissing, meowing, and purring sound for cats, they will hiss at any ghosts they detect now!
- Fixes Mana from Heaven invisible sprite
- Claw and Baton energy drinks added overdose that causes organ damage at 60 units consumed
- Fixes incorrect Claw RED and BLUE sprites
- Claw Blue made actually made tastier
- Case Closer baton now contains atomic coffee instead of espresso (Marshal buff)
- Hay Fever claw energy improved citric formula
- Attempts to port Shields blocking projectiles functionality from Eris, but fails miserably (Tested not to work, but leaving the groundwork just in case)

* Nerfs liver failure damage even further

Random number 2 to 6 damage per tick

* Adds *zartan emote

Whistling of "For he's a jolly good fellow", GI Joe reference.

* Armor pen fix

Certain powered hammers were not properly inheriting armor pen somehow

* Preppers fairness

- Removes Sentinel Seeker from the random prepper mob spawn list
- Makes Sentinel Seeker a low spawner on par with Renders and nightmare stalkers as it shares similar stats with them
- Replaces certain prepper mob spawns with various low-chance Sentinel Seeker spawns on areas of high loot concentration (mech bays, prepper armory, near the excelsior disks, etc)
- Removes a trap spawner on the same room as Outsider spawn, as it can sometimes be a mine impossible to traverse on the only exit way
- Replaces hardspawn of Sentinel Seeker in Preppers medbay with a low chance for one, compensates by adding two more ranged mobs to the area

* Louder emotes

- Some female emotes were too low
- Typo fixes on bear rawr proc

* Apply suggestions from code review

This is a BYOND joke

Co-authored-by: Trilbyspaceclone <30435998+Trilbyspaceclone@users.noreply.github.com>

---

