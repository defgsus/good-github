## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-11-24](docs/good-messages/2023/2023-11-24.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,570,895 were push events containing 3,650,923 commit messages that amount to 223,789,086 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 79 messages:


## [ComposableFi/env](https://github.com/ComposableFi/env)@[604f4bf52e...](https://github.com/ComposableFi/env/commit/604f4bf52e48bd695f21e23c67d70ebcbcca5b99)
#### Friday 2023-11-24 00:03:45 by dzmitry-lahoda

happy tf

genious plan

ohoho

hoho

up

wtf

tf

fuck you

happy

work bitch

hoho

cleam up

happy

fun

oh

push

yaml

oho

why

ginal

oohoh

fix

fix

flake

Update README.md

Signed-off-by: dzmitry-lahoda <dzmitry@lahoda.pro>

secure mnemonic

hope is trust

updates to keys and node

cannot self refer

fixing TV

oh 2 places

real use

fail application

fixign

log

fix

fixing

fixing egress

run

final

happy

cleanup

---
## [MichaelHinrichs/SPORE-Creatures-extract](https://github.com/MichaelHinrichs/SPORE-Creatures-extract)@[b21188495d...](https://github.com/MichaelHinrichs/SPORE-Creatures-extract/commit/b21188495d96bce126d54a2948f10ff493471d4f)
#### Friday 2023-11-24 00:12:23 by NintenHero

Don't make me fuck you!

Don't think i won't. I'll fucking do it!

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[33cae266af...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/33cae266af864b22c509f65ffff3ad7277bbb459)
#### Friday 2023-11-24 00:13:04 by Captain277

Subtypes Corporate Crates, Fixes Mapped Biohazard Crate, Renames Advanced Voidsuit (#6126)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

1. *Fixes Bug With Corporate Crates, Subtypes Them.*
2. *Removes Varedited Biohazard Bin and Places Normal Biohazard Bin.*
3. *Changes Advanced Voidsuit Name to Advanced Hardsuit.*

## Why It's Good For The Game

1. _I received reports of one specific corporate crate not rendering
properly when opened. As I inspected it, I realized it would be more
efficient to subtype all corporate crates, so I did that. HOWEVER, this
did not repair the initial bug. For some reason the crate was not
rendering its 'aethersecureopen' state, even though all variables and
code seemed to be working properly. No other crate exhibited this issue.
I discovered that by changing the name of the icon state from
'aethersecureopen' to 'aethersecopen', the state began to enforce and
render properly. I suspected it might be a name length issue, but tests
with other equally long icon states in the crate section disproved this
theory. This may warrant further investigation._
2. _This one avoided detection during my initial sweep through. Can't
remember who just went in and tried to varedit bins to fix biohazards,
but hopefully this is the last one they touched._
3. _This has been driving me crazy for a few days, and yesterday
especially. The Advanced Voidsuit is clearly misnamed, as it is in fact
a Hardsuit. When I tried to order these yesterday I overlooked this
cargo entry twice because I was looking for a hardsuit, not a voidsuit.
This just fixes the name._

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
add: Adds Corporate Crate Subtype, Reassigns Corporate Crates to It.
fix: Fixes incorrectly mapped biohazard bin.
tweak: Changes Name: Advanced Voidsuit to Advanced Hardsuit.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [nrc-cnrc/gramble](https://github.com/nrc-cnrc/gramble)@[058b72b655...](https://github.com/nrc-cnrc/gramble/commit/058b72b655add69586fd8fc43fa1ec3f894e3acf)
#### Friday 2023-11-24 00:21:25 by littell

Fixing recursive rename bugs

A few relatively minor changes fixed our various bugs about tape calculation, renaming, and recursion.  (The code has been somewhat refactored because I expected more serious changes, but my fixes here probably would have worked with our old code too.)

(1) I mentioned in a meeting that I had made an error in conflating two meanings of TapeInfo -- one (call it "intensional") that it represents a constraint on what tapes the symbol can contain, and two (call it "extensional") that it represents that set of tapes.

All along, we've been saying "If you encounter a recursive reference to a symbol, don't just recurse infinitely, just return the empty set."  From an extensional point of view, that's stupid, we know the symbol doesn't contain the empty set.  It makes sense intensionally, though -- recursing wouldn't put any more constraint on the symbol than it already has.

Using an extensional meaning was causing some problems with Renames.  In particular, if there was an erroneous rename to an existing tape, the Renames were *usually* catching this but *sometimes* failing to catch this in a recursive context.  The reason is because they were working on the extension -- looking at that recursion-breaker empty set, saying "Well THIS doesn't contain the problematic tape", and failing to complain, and failing to put the output tape into the tapes object because the input tape wasn't present either.

Part of the fix is that the Rename has to put its toTape into the tapes no matter what -- because the *symbol* will contain the input tape even though that *tape set* is empty.

So long as this happens, the "oops renaming to an already-existing tape" error reliably gets caught in the tape-pushing stage that follows.

(2) I mentioned a few commits ago that we had to do some error detection and repair during unification itself.  I even refactored the locator system to allow that.  Turns out I was wrong, we still can't do it then.  (I'm still happy I refactored the locator system, though, that's good anyway.)

We might have been able to detect and message rename errors during unification, but we couldn't FIX them.  Fixing means changing the grammar tree, and we're not in the grammar tree right now, we're playing with a little reduced form of the grammar.  So either (a) we go back to unifying on the tree itself so we can change it, or (b) we accept that errors can only be caught/fixed in the tree traversal.

(3) Turns out we probably have to accept (b) anyway.  Trying to do a graph algorithm on a graph *that might be changing out from under you* would be a nightmare.

Instead, we come to the best conclusion we can, push it to the graph, and then if the tree changes due to errors, we take the changed tree and do the whole infer-unify-push process again.  Yes, that's a tough bullet to bite but it's inevitable -- a different tree means different tapes.  Our tape calc ordering problems were in part due to using "stale" tape information after the tree had already changed.

(4) So we've addressed a lot of the recursive renaming issues, to the point that rename errors are getting caught and the repairs are happening.

Turns out our repairs are a problem too!

Backing up, the problem with renaming-to-an-existing tape (say, a `t1->t2` rename where `t2` already exists on the child) is that any `t2` material inside the scope of that rename never gets handled during the generation loop.  The rename gets a query on `t2`, and forwards it on as a `t1`; there's never any point where the material inside receives a query.  So our solution was to sneak in an additional rename inside the erroneous rename, renaming the old inaccessible `t2` material to `.ERRt2`.

However, consider a recursive rename paradox with this issue.  We encounter a paradoxical rename, and it's caught in the push stage, and we slip in that sneaky rename to `.ERRt2` to fix it.  Now we restart the tape calc process, because the tree has changed and our old answers are stale.

We recalculate, push the answers into the tree... and find a new error.  Y'see, we find this rename to a tape `.ERRt2`... but `.ERRt2` already exists in its scope due to the recursive reference.  We'll never manage to reach the `.ERRt2` material inside!  In order to reach it, we have to slip in a sneaky rename to a new tape; it gets called `.ERR.ERRt2`.  Then we restart, recalculate, push the answers into the tree, and find a problem with `.ERR.ERR.t2`...

In a way, this is correct behavior given the paradox!  Those really aren't all the same tape, each recursion does really need a different error tape to catch that material.  But it leads to an infinite loop that is tricky to actually stop, and doesn't actually *resolve* the paradoxical situation, like it's treating the symptom but not the disease.

Really, the way to remove the paradox is the simpler repair, what we do for other rename issues: drop the rename entirely.

---
## [mosra/magnum-extras](https://github.com/mosra/magnum-extras)@[ebf11a4a32...](https://github.com/mosra/magnum-extras/commit/ebf11a4a32c99f8bd3f91cc2c45f573f7eafc8d3)
#### Friday 2023-11-24 00:30:57 by Vladimír Vondruš

Whee: rework BaseLayer and TextLayer style assignment.

Requiring the calling code to have a compile-time-sized struct felt like
a good idea in theory. In practice it's absolutely horrendous tho, as:

 - The calling code then has to ensure matching order between a style
   enum and a style struct, which is extremely hard to maintain without
   a nasty preprocessor magic.
 - Defining a builtin style means either having to define & document a
   struct that glues a LayerStyleCommon instance together with several
   LayerStyleItem instances, which is nasty on its own, and then have to
   *somehow* populate it. Which in a (C++11) constexpr context means
   either using the implicit initializer, again losing any mapping from
   the actual enum values to the order (thus gaining *nothing* from such
   a "named tuple" definition), or having to give up on any constexpr
   use and assign to the named fields in order to ensure at least some
   ordering sanity.
 - It's extremely annoying and / or impossible to extend the style
   definition for custom widgets -- one has to *derive a struct* for
   that, and then somehow copy the original builtin data to its prefix.
 - The error message when the layer style count differs from the actual
   passed data is total garbage. Nobody is interested in how many bytes
   something occupies, they want to know *what is wrong* and the API
   isn't capable of saying or even knowing that.

So now it's instead a setStyle() API taking the LayerStyleCommon
instance and a (contiguous) list of LayerStyleItem. A downside is that
the (GL) implementation then does two GL buffer uploads, alternatively
it could put them together and upload at once (which means a nasty temp
allocation). With Vulkan (and I hope WebGPU) this won't be a problem as
there's a way to submit multiple uploads in a single command, or just
memory-mapping the buffer and doing a copy directly.

Extending a style is then a matter of creating an array that's larger
than the compile-time constant, having the custom style items start from
that constant, and copying the original data to prefix of that array.
Simple.

For the TextLayer this also merges the previous setStyle() and
setStyleFonts() APIs together, because they were always meant to be
called together anyway. It makes the whole usage a lot less janky and
unclear.

---
## [JohnFulpWillard/tgstation](https://github.com/JohnFulpWillard/tgstation)@[9112509abd...](https://github.com/JohnFulpWillard/tgstation/commit/9112509abd9507974928ea5d02676d0d0a58cbec)
#### Friday 2023-11-24 00:31:09 by KingkumaArt

Stops rebar crossbow crashing dreamseeker when fired at point blank. (NO GBP) (#79803)

## About The Pull Request

Simply put, due to how "caseless" is an element added to the ammo when
it hits something, but ammo is qdeleted upon hitting someone. If shot
point blank without combat mode (for some reason) it tries to add
caseless to an ammo that no longer exists. For some reason, the result
of this is to just fucking crash DS instead of aborting the adding of
the element. The ammo isnt reusable anymore, but I'll take that over
crashing.

## Why It's Good For The Game

Removes a game-breaking bug. I hate gun ammo code so much. 

## Changelog



:cl:
fix: Stopped a DS crash when shooting a rebar crossbow in specific
circumstances.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [SWE-B5/SpottingSmallPrints](https://github.com/SWE-B5/SpottingSmallPrints)@[3b18914e48...](https://github.com/SWE-B5/SpottingSmallPrints/commit/3b18914e488aa00c76f987e42b78ea0a4ca196bd)
#### Friday 2023-11-24 00:35:18 by Philogex

Merge branch 'bitmap' of https://github.com/SWE-B5/SpottingSmallPrints into Level3
i hate my life

---
## [AcademySoftwareFoundation/OpenImageIO](https://github.com/AcademySoftwareFoundation/OpenImageIO)@[b8723ec691...](https://github.com/AcademySoftwareFoundation/OpenImageIO/commit/b8723ec6918b9204d040c495eba8c8d21484df53)
#### Friday 2023-11-24 00:39:17 by Larry Gritz

fix(oiiotool): --autocc bugfix and color config inventory cleanup (#4060)

The important bug fix is in oiiotool image input when autocc is used,
where we reversed the sense of a test and did the autocc-upon-input if
the file's color space was equivalent to the scene_linear space
(pointlessly), and skipped the conversion if they were different (oh no,
big bug!).

Along the way:

* Add missing try/catch around OCIO call that should have had it.

* Some very ugly SPI-specific recognize-by-name color space heuristics.
I hate this, sorry, but it solves a really important problem for me.

* A bunch of additional debugging messages during color space inventory,
enabled only when debugging, so nobody should see these but me.

* A couple places where we canonicalize the spelling of
"oiio:ColorSpace".

Note that there is still an issue with the color space classification
using OCIO 2.3+'s identification of built-in equivalents by name. These
are shockingly expensive. I will return to this later.

Signed-off-by: Larry Gritz <lg@larrygritz.com>

---
## [LuciliusMothboy/Men-love-me-fish-fear-me](https://github.com/LuciliusMothboy/Men-love-me-fish-fear-me)@[800ad77ed2...](https://github.com/LuciliusMothboy/Men-love-me-fish-fear-me/commit/800ad77ed29fd7c68ddc0cac3112f45e1e1c3015)
#### Friday 2023-11-24 01:00:44 by DBGit42

Adds Affection Aversion quirk (#25194)

* Adds Affection Aversion quirk

Stops affection modules. Very simple.

* I hate you, github

May or may not do anything. Stop giving me a merge conflict. Stop it.

* Revert "I hate you, github"

This reverts commit 6515023cc3f72d97d90bbdf982857b1d2724b1cf.

* Attempts to revert traits.dm

Because something went TERRIBLY wrong with my fork and/or my editor and I'm not sure why.

* Added quirk proper now that my fork is unfucked

Why did this even happen?

* These lists are alphabetized

* Same here

---------

Co-authored-by: Bloop <13398309+vinylspiders@users.noreply.github.com>

---
## [SabreML/cmss13](https://github.com/SabreML/cmss13)@[15086ae683...](https://github.com/SabreML/cmss13/commit/15086ae683f727d9a990e05f8ce9a08e43731207)
#### Friday 2023-11-24 01:06:04 by fira

Allow playing uploaded sounds through the music player w/ Webroot (#4934)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

Too long have we suffered at the hands of admin auditive abuse. 

The prophet, spookydonut, once said, "You shouldn't be using this lol".
And he was right. Using "Play MIDI sound" both reduces usability for our
users, and can cause performance issues by freezing up the game for a
while as the data is transfered to these 200 poor CM addicts.

So we sought to alienate it with "Play Internet Sound" backed by
youtube-dl. Unfortunately, some things are subject to geo blocking or
simply not available on Youtube. Thus the regime of terror of Admins
continues.

This PR brings us one step closer to our goal: it allows to use the now
renamed "Play Admin Sound" to (also) upload a sound file to Webroot and
have it played through CDN. It also works with simple transport but that
mostly defeats the point.

Also reduced default volume for new players from 50% to 20%... Don't
worry, It's still way more than enough to get them to quit the server, i
have mine at 2-10% max

# Explain why it's good for the game
* Less new player abuse by reducing default volume
 * More performance by allowing big or custom songs to be backed by CDN
* Better UX: People can easily see the song name and more easily stop it
* Admins can now hide the name of played songs if they want to. Don't
ask me why.

# Testing Photographs and Procedure

![image](https://github.com/cmss13-devs/cmss13/assets/604624/4f00c45d-76ca-47e2-860a-2f26d55de2a4)
You'll have to believe me on the sound working

# Changelog
:cl:
balance: Default Web Music Player volume is now 20% down from 50%. It
was found too effective against new players.
admin: "Play Internet Sound" is now "Play Admin Sound" and optionally
allow to hide the track name.
admin: "Play Admin Sound" can now be used with uploaded tracks, which
use CDN delivery and the in-chat music player, granting players more
control over them.
admin: Removed "Play Midi Sound". 
/:cl:

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[71082d8192...](https://github.com/effigy-se/effigy-se/commit/71082d819219298b695f279baeab99786d7711cd)
#### Friday 2023-11-24 01:08:58 by Ephemeralis

Refactor icemoon wolves into basic mobs and add taming + pack behavior (#79736)

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

Co-authored-by: san7890 <the@san7890.com>

---
## [cyyever/pytorch](https://github.com/cyyever/pytorch)@[5f504d1de7...](https://github.com/cyyever/pytorch/commit/5f504d1de74a5189f93e65aa9283fc4607b8631c)
#### Friday 2023-11-24 01:22:27 by Pedro Caldeira

Check for boolean values as argument on pow function.  (#114133)

Hello everyone! 😄
Also @lezcano , nice to meet you! :)

Sorry if I miss anything, this is my first time around here. 🙃

This PR basically makes the same behaviour for cuda when using `torch.pow`. Basically Python considers True as 1 and False as 0. I just added this check into `pow` function. From what I understood, when I do `.equal` for `Scalar` that is boolean, I'm sure that types match so that won't cause more trouble.

I know that the issue suggest to disable this case but that could be a little more complicated, in my humble opinion. And that can create some compability problems too, I guess.

My argument is that code below is correct for native language, so I guess it does makes sense sending booleans as Scalar.

```
$ x = True
$ x + x
2
```

This was my first test:
```
Python 3.12.0 | packaged by Anaconda, Inc. | (main, Oct  2 2023, 17:29:18) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> torch.pow(torch.tensor([1, 2], device='cuda'), True)
tensor([1, 2], device='cuda:0')
>>> torch.pow(torch.tensor([1, 2]), True)
tensor([1, 2])
>>> torch.pow(torch.tensor([1, 2]), False)
tensor([1, 1])
>>> torch.pow(torch.tensor([1, 2], device='cuda'), False)
tensor([1, 1], device='cuda:0')
```

I've run `test_torch.py` and got following results, so my guess is that I didn't break anything. I was just looking for a test that uses linear regression, as suggested.

```
Ran 1619 tests in 52.363s

OK (skipped=111)
[TORCH_VITAL] Dataloader.enabled		 True
[TORCH_VITAL] Dataloader.basic_unit_test		 TEST_VALUE_STRING
[TORCH_VITAL] CUDA.used		 true

```
(I can paste whole log, if necessary)

If this is a bad idea overall, dont worry about it. It's not a big deal, it's actually a two line change 😅  so can we talk of how do things in a different strategy.

For the record I've signed the agreement already. And I didn't run linter because it's not working 😞 . Looks like PyYaml 6.0 is broken and there's a 6.0.1 fix already but I have no idea how to update that 😅

Fixes #113198

Pull Request resolved: https://github.com/pytorch/pytorch/pull/114133
Approved by: https://github.com/lezcano

---
## [eurekadevelopment/android_hardware_samsung_slsi-linaro_graphics](https://github.com/eurekadevelopment/android_hardware_samsung_slsi-linaro_graphics)@[dca70be694...](https://github.com/eurekadevelopment/android_hardware_samsung_slsi-linaro_graphics/commit/dca70be694dee8edef6df10c6bf853d1592bd5d6)
#### Friday 2023-11-24 01:22:33 by K9100ii

graphics: Switch to a new versioned path and BSP variant setting

and add soong namespacing.

Copy-paste explanation:

There are two sets of BSP sources - These new ones intended for Android
13, and older ones originally intended for Android 10. The older ones
have support for some legacy things like HWC1 for older devices, and
the newer ones have support for newer things like gralloc4.

To keep support for older devices going, I want to keep the older
sources alongside the newer ones. But they can't co-exist as-is. Some
changes are needed:
 - a change of paths to the BSP sources, which are referenced directly
   within them
 - a new BSP variant setting ('TARGET_SLSI_VARIANT' flag)
 - and finally, some soong namespacing.

The BSP variant setting and paths are the biggest challenge. For the
existing BSP sources, there's absolutely no versioning. It's the same
old generic "linaro"/"samsung_slsi-linaro" for both sets of BSP sources.
Sadly, my expressions of concern for my life to not be made more hellish
were quite badly dismissed, all the while I'd think it would be best
practice to version things like this to not keep using the same old
generic identifiers and not run into issues (or for others to not do so)
later, so I'm on my own to figure out what to do here.

My solution that touches the least I can is as follows:

For Android 13 - The older Android 10 BSP sources are typically used,
and since I'd like to use 13 sources as I have a device that requires
gralloc4, I need to make changes within them.
To manage it, the naming is as follows:
  Directory for 10 sources - 'samsung_slsi-linaro'
  Directory for 13 sources - 'samsung_slsi-linaro_13-e850-96'
  Git branch name for 10 sources - '...'
  Git branch name for 13 sources - '..._13-e850-96'
  SLSI variant flag setting for 10 sources - 'linaro'
  SLSI variant flag setting for 13 sources - 'linaro_13-e850-96'
The only changes here are for 13 sources. Naming is left untouched for
10 sources so as to not break anything for trees using them currently.

For Android 14+ - I'd want to preserve support for older devices, if
running newer Android versions doesn't become an impossibility for them,
so, while the newer Android 13 BSP sources are typically used, I'd have
to make changes to the 10 sources to keep them alongside.
To manage it, the naming will be as follows:
  Directory for 10 sources - 'samsung_slsi-linaro_10-e850-96'
  Directory for 13 sources - 'samsung_slsi-linaro'
  Git branch name for 10 sources - '..._10-e850-96'
  Git branch name for 13 sources - '..._13-e850-96'
  SLSI variant flag setting for 10 sources - 'linaro_10-e850-96'
  SLSI variant flag setting for 13 sources - 'linaro'
The directory and variant flag setting will be untouched for 13 sources,
so as to stay in line with everyone else, and changes would only need to
be made within 10 sources. However, for consistency, git branches will
all be versioned in future.

Lastly, soong namespacing is added specifically for the "exynos" and
"graphics" parts of the sources. Without, there are conflicts between
the two sets of sources. For all devices, BoardConfigCommon.mk in the
collection of BSP configs is included, and namespaces can be added
there, for a clean result where no changes are required in device trees
at all.

Change-Id: I79e77f9bff0d4a1595d5cc6fe72fbd17d2734373

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[d3f79b6612...](https://github.com/lessthnthree/effigy-se/commit/d3f79b6612ee31503bae890c460c54ca2f5252dc)
#### Friday 2023-11-24 01:25:56 by san7890

Puts all traits in the globalvars file + CI Testing (#79642)

## About The Pull Request

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
## Why It's Good For The Game

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
## Changelog

Nothing applicable to players. However, to mappers, the mapping trait
injector should always be able to add any kind of trait (which is rather
good for the times when you need it).
# Conflicts:
#	tgstation.dme

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[6d5aa5121e...](https://github.com/lessthnthree/effigy-se/commit/6d5aa5121eb08bec19d3d5413f45a216af8a2c1e)
#### Friday 2023-11-24 01:25:56 by san7890

Fixes sending stuff to "Old" Chat (#79819)

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

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[b3f97b0115...](https://github.com/lessthnthree/effigy-se/commit/b3f97b01152fa1427b848f0ca3b03ea6bd5b014d)
#### Friday 2023-11-24 01:26:04 by Kyle Spier-Swenson

fix stupid "this forces us to do things the """right""" way" bullshit from python 3.11 (#79783)

This is likely not the best way to go about this, but i do not want us
to capitulate to python3's nanny state, suffocating levels of propriety
bullshit.

venv sucks and i fucking hate it.

---
## [caballero17/app-dev](https://github.com/caballero17/app-dev)@[3754933c54...](https://github.com/caballero17/app-dev/commit/3754933c54e22b4ea516ee8f0af3ebb742776798)
#### Friday 2023-11-24 01:42:02 by caballero17

Update README.md

Hanagaki Takemichi lives an unsatisfying life right up until his death. Waking up 12 years in the past, he reckons with the eventual fate of his friends and tries to prevent an unfortunate results in the future. Takemichi  is a freelancer that's reached the absolute pits of despair in his life.

---
## [y3un9/react](https://github.com/y3un9/react)@[ac1a16c67e...](https://github.com/y3un9/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Friday 2023-11-24 01:44:49 by Sebastian Markbåge

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
## [GerHobbelt/clBLAS](https://github.com/GerHobbelt/clBLAS)@[619d976cfc...](https://github.com/GerHobbelt/clBLAS/commit/619d976cfcd1078c72bc02af1516210ed3ac2ac0)
#### Friday 2023-11-24 01:47:22 by Ger Hobbelt

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
## [sourcemaster7/math66](https://github.com/sourcemaster7/math66)@[b5467e8681...](https://github.com/sourcemaster7/math66/commit/b5467e8681e3de3bc7789134b31da3150500095d)
#### Friday 2023-11-24 02:18:34 by TheDiamondfinderYT

SEASON 3 OUT NOW!

 # SEASON 3 OUT NOW!

 ## Summary
A long time in the making, we're proud to release season three! For the sake of getting it out early, it's unfortunately unfinished.
But this was an ambitious update, full of optimizations and roadblocks! We feel that you will still enjoy this update and be excited what's in store
This is a revamp of the current season 2, consisting of a new
 - Search bar
 - Game page
 - File formatting
 - Game page compiling
 - Optimized files for faster load time
 - More detailed info on game pages
 - Cleaner code
 - etc.

 ## Known issues
 - Some games are currently broken (45, thanks rm) and do not have proper iframe configurations. Should be fixed by friday
 - Descriptions are unfinished
 - Python is clunky and hard to understand

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[5d29487121...](https://github.com/effigy-se/effigy-se/commit/5d2948712144ccd117e6ba34d851c147754a778e)
#### Friday 2023-11-24 03:23:46 by necromanceranne

Fixes body collision causing a stun, despite a successful block. (#79824)

## About The Pull Request

Puts a block check into the ``throw_impact()`` of carbon mobs. 

## Why It's Good For The Game

I'm touching on a lot of 'get around shields' stuns, and this has been a
big one for the better part of a few years and potentially not even
intentional. I would say it gained its largest popularity when it became
weaponized with fireman carrying.

Despite seemingly rolling to block, blocking a body hitting you doesn't
actually do anything at all. This reminds me a bit of energy bolas. So I
fixed it? I think, there might be a better fix, I'm just replicating
code present in xenomorph tackles. This shit sucks, please recommend a
better fix if you know it.

## Changelog
:cl:
fix: When you successfully block a body collision, it does something
rather than nothing at all.
/:cl:

---
## [jongan69/cinemaswipe](https://github.com/jongan69/cinemaswipe)@[f58cf42efd...](https://github.com/jongan69/cinemaswipe/commit/f58cf42efd197d4f3e9c4e5bc974a8117bdac41c)
#### Friday 2023-11-24 03:35:02 by jongan69

Last one for the day, can stand the ai api key bullshit who the fuck cares fuck your key its not that cool

---
## [juju/juju](https://github.com/juju/juju)@[9332e8c436...](https://github.com/juju/juju/commit/9332e8c4361fe8860cbda185e0f1597431ea3e0f)
#### Friday 2023-11-24 03:58:33 by Juju bot

Merge pull request #16611 from tlm/model-config-api

https://github.com/juju/juju/pull/16611

With this commit we are introducing a new global table to the controller database to describe model defaults that should be applied to all models in the controller.

Previously in Juju we have not had this notion of controller wide model defaults. They have always been scoped to the cloud or cloud region. However secretly under the covers we have been living a life of shame where we have been taking the controller models config and using that as a controller wide default source.

It is time to rise up out of the shadows of this murky controller model defaults world and own our desire for a controller wide model defaults source. No longer should lesser models live in shame and more importantly no longer should the controller model be treated as some special case model that acts as a source of truth.

A perfect example of this is we use the controller model to find the Juju system ssh key that is created during bootstrap. Every model needs ssh key added to it at creation time. We currently interrogate the controller model for the key. We are going to stop doing this so that the controller model can have the exact same logic applied to it as every other model in Juju.

## Checklist

- [x] Code style: imports ordered, good names, simple structure, etc
- [x] Comments saying why design decisions were made
- ~[ ] Go unit tests, with comments saying what you're testing~
- ~[ ] [Integration tests](https://github.com/juju/juju/tree/main/tests), with comments saying what you're testing~
- ~[ ] [doc.go](https://discourse.charmhub.io/t/readme-in-packages/451) added or updated in changed packages~

## QA steps

No tests for this change. I am just proposing the DDL. The next PR that wires up the state layer will offer the tests for this DDL.

## Documentation changes

None. We are not going to offer this defaults source as a user configurable component via the cli or API. We are just going to store bootstrap generated concerns in the table at the moment where we know a key is going to be needed for every model regardless of what cloud it is for.

## Links

**Jira card:** JUJU-5046

---
## [effigy-se/effigy-se](https://github.com/effigy-se/effigy-se)@[55260650e4...](https://github.com/effigy-se/effigy-se/commit/55260650e4aca4ef905ce66071c82363e6860abb)
#### Friday 2023-11-24 03:59:29 by necromanceranne

[READY] The Tackleling: Unarmed bonuses and features contribute to tackle success and failure, significant outcome overhaul, among other things (#79721)

## About The Pull Request

### Tackling Outcomes

Tackling now determines success based on outcome categories. These are
derived from the typical attacker/defender roll that would have
previously determined the outcome on its own. A negative roll results in
a negative outcome, a positive roll a positive outcome, and a result of
exactly 0 resulting in a neutral outcome.

The result of your roll are then passed along to the relevant proc to
determine severity. The derived roll is multiplied by 10 (or -10 for the
negative roll to get a positive value to roll with). Then we see if our
final roll fits a severity bracket. Negative outcomes will roll to
determine their outcome, and potentially could roll a less severe
outcome than what our first roll would suggest.

For positive outcomes, the defender's melee armor reduces the severity
of the outcome.
For negative outcomes, the attacker's melee armor improves the potential
outcome and at least prevents more severe backlash. It'll still be
negative, you can't move from a negative outcome to a positive outcome
just from good armor.

Most of the outcomes are fairly similar to the current outcomes, but
with the inclusion of staggering one or both parties to make the
subsequent potential grabs _stickier_, if that makes sense.

Neutral is now a mutual stagger, but also the tackler being left
upright. It's effectively net zero.

### Blocking

Blocking is checked on impact, and results in a neutral outcome if the
defender successfully blocks. This means our tackler isn't too severely
impacted from an unsuccessful tackle

### Additional Changes

Your arms ``unarmed_effectiveness`` now contributes to the attack mod
and defense mod of tackles. For humans tackling humans, this often
results in a net neutral result. But if you have a better arm, or the
tackle target has worse arms, this can alter the outcome significantly.

Any tackler with the trait TRAIT_NOGUNS (like bezerkers, Sleeping Carp
users or the very unlikely chance ninjas are tackling while wearing
their armor) gains a bonus to their tackles.

Any suit that prevents shove knockdowns grants an attack bonus, and not
just riot armor. This now includes Mk.1 Swat suits, the ones from the
SWAT crate in cargo.

Settlers are vulnerable to tackles, much like their dwarf cousins.
They're also just as bad at tackles.

Security lockers come with gripper gloves, and the sec vendor has 5 sets
of gripper gloves as standard items. They also have a +1 skill bonus.
This should encourage people to use tackling a bit more without having
to always seek out the best gear to accomplish the task. (particularly
since security is inherently pretty good at tackling with the outcome
changes).

The HoS gets a pair of gorilla gloves in his garment bag. If he wants
them.

The shove slowdown is now a new status effect, Staggered. This is just
better functionality overall. Any instance of adding the shove slowdown
now makes our target staggered.

## Why It's Good For The Game

Tackling is a bit outdated, to say the least. Not much content has been
added for a while that isn't strictly meme content. With these changes,
tackling should be slightly more nuanced, considering elements such as
unarmed effectiveness, the presence of martial arts, and actually
properly checking block rather than notionally checking block. There is
also more opportunity to protect yourself from tackle outcomes, both
positive and negative.

It also should be a little fairer to be on the receiving end of tackles
if you have taken the time to layer up defenses against it. Attackers
often overwhelmed defenders due to numbers favoring attackers more than
defenders.

Closes some really outdated design that was resulting in some really
bizarre behaviour with regards to layered defenses against attack not
having the same meaning against tackles, if only because it was looking
for the wrong things and not even the correct parts of what it was
looking for. Namely, blocking and shielding.

The inclusion of more gripper gloves and a good outcome from using them
will hopefully incentivize people to consider tacking as a useful tool,
if a bit risky still due to the splat mechanics.

## Changelog
:cl:
balance: Judo Joe, archnemesis of Maint Khan, has begun re-airing his
midnight infomercials shilling his extremely expensive Tackle Supreme
Judo Karate Training video tapes. Unable to pass up a 'bargain',
Nanotrasen has purchased these tapes en masse. Tackling techniques have
started to improve, as well as Nanotrasen's tackling instructional
algorithms within tackle gloves.
balance: The outcomes for tackling are more equalized. It isn't as feast
or famine, and should be somewhat more controllable without becoming too
severe.
add: Blocking successfully against a tackle will force the tackle to be
a neutral outcome.
add: Unarmed effectiveness from arms now contributes to attacking with
and defending from tackles.
add: Those who refuse to use firearms (like Sleeping Carp users and
insane unholy berzerkers) are better at tackling others.
add: Riot specialized armor, and not just riot armor, now contributes
meaningfully to tackling effectiveness.
balance: MK.1 Swat Suits, the ones that come in SWAT crates, now
functions similarly to riot armor.
add: Settlers from the outer rims have noticed they aren't very good at
protecting themselves against Judo Joe's clearly discriminatory tackling
techniques.
add: Security lockers come with gripper gloves, security vendors now
sell them as standard items, and the HoS' garment bag now has a pair of
gorilla gloves. Gripper gloves have a positive skill bonus to tackling.
add: Being insane also makes you INSANELY good at tackling but also
INSANELY likely to eat shit on a whiff. DO OR DIE, BITCH.
refactor: Shoving slowdown and all its implementations now use a status
effect, Staggered.
/:cl:
# Conflicts:
#	code/datums/components/tackle.dm

---
## [rutek-code/Skyrat-tg](https://github.com/rutek-code/Skyrat-tg)@[48b5a35dea...](https://github.com/rutek-code/Skyrat-tg/commit/48b5a35deadc1cdeb19d117ee50702c76df0d275)
#### Friday 2023-11-24 04:00:24 by Bloop

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
## [rutek-code/Skyrat-tg](https://github.com/rutek-code/Skyrat-tg)@[67ddf1507c...](https://github.com/rutek-code/Skyrat-tg/commit/67ddf1507c8663c4b8f006ed8c763ca372e5fc29)
#### Friday 2023-11-24 04:00:24 by SkyratBot

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
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[e62799a06d...](https://github.com/RustingWithYou/Aurora.3/commit/e62799a06d3aa17eec0f8c6bef77ad8f824d8887)
#### Friday 2023-11-24 04:21:43 by RustingWithYou

air konyang ship

it's a shuttle now, im gonna kms

smaller so it can fit

desperately cramming into shuttle guidelines

changelog & placeholder comments

chairs

name & mapping fixes

dme fix

carpet

new airlocks

entry points?

cries, shits

a

unit test group

fuck

ghuh

hguh

hate

fixes stupid problems

area flags

---
## [longit644/carbon-lang](https://github.com/longit644/carbon-lang)@[c7e6238fa8...](https://github.com/longit644/carbon-lang/commit/c7e6238fa8dd57672b0765e738f4c425a27cac3b)
#### Friday 2023-11-24 04:28:18 by Chandler Carruth

Introduce two speed-of-light benchmarks. (#3270)

The goal of these kinds of benchmarks is to help calibrate other
benchmarks and expectations. They benchmark the underlying hardware
capabilities that we can't avoid, and help illustrate bounds for what is
possible. The term "speed-of-light benchmark" references the aspect of
measuring how fast thing could possible run.

The first is a simple memory bandwidth measurement in the best case
scenario -- using `strcpy` over the buffer. This still does a minimal
number of writes to memory and examines each byte of input to see if it
is null, but can cheat in every way possible to run at the maximum speed
of hardware. To a certain extent, we never expect to get close to this
speed, but it's a good illustration of how much headroom the hardware
has available.

The second is potentially more interesting. This illustrates how fast a
byte-by-byte dispatch loop can potentially be. It uses the technique
that I'm hoping to use in the lexer itself of guaranteed tail recursion
to achieve this with a very small code footprint. The performance of
this technique, even when running in this extremely minimal setting to
establish bounds, is hugely dependent on the number of distinct dispatch
targets, and so the benchmark includes a healthy range to show the range
of performance that we might expect when running in a byte-by-byte mode.
Note that we should expect the lexer to be *faster* than this
"speed-of-light" whenever it is able to lex in larger granules than
byte-wise. But for complex, dense token sequences that force looking at
every byte, this shows the "worst case" "speed-of-light" in a sense.

On my recent AMD cloud VM instance, I get the following results running
the main lexer benchmark with these changes included:

```
-------------------------------------------------------------------------------------------------------------------------
Benchmark                                            Time             CPU   Iterations bytes_per_second tokens_per_second
-------------------------------------------------------------------------------------------------------------------------
BM_ValidKeywords                               3169403 ns      3169283 ns          221        188.44M/s        31.5529M/s
BM_ValidIdentifiers<1, 64, false>             12486725 ns     12486445 ns           51       117.953M/s        8.00868M/s
BM_ValidIdentifiers<1, 1, true>                3950455 ns      3950298 ns          178       72.4252M/s        25.3145M/s
BM_ValidIdentifiers<3, 5, true>               15562294 ns     15561178 ns           45       36.7712M/s        6.42625M/s
BM_ValidIdentifiers<3, 16, true>              16118656 ns     16118374 ns           44       68.0412M/s         6.2041M/s
BM_ValidIdentifiers<12, 64, true>             19116271 ns     19116258 ns           35       199.541M/s        5.23115M/s
BM_ValidMix/10/40                              7074336 ns      7073795 ns           93       140.744M/s        14.1367M/s
BM_ValidMix/25/30                              6790722 ns      6790006 ns          102       131.793M/s        14.7275M/s
BM_ValidMix/50/20                              5960514 ns      5960443 ns          118       112.594M/s        16.7773M/s
BM_ValidMix/75/10                              4325546 ns      4325556 ns          159       102.559M/s        23.1184M/s
BM_SpeedOfLightStrCpy                            24339 ns        24339 ns        29650       35.9049G/s        4.10858G/s
BM_SpeedOfLightDispatch<1>                     1756051 ns      1755800 ns          398       509.668M/s        56.9541M/s
BM_SpeedOfLightDispatch<2>                     1611973 ns      1611725 ns          436       555.228M/s        62.0453M/s
BM_SpeedOfLightDispatch<4>                     2064280 ns      2063990 ns          326       433.565M/s        48.4498M/s
BM_SpeedOfLightDispatch<8>                     2484055 ns      2483946 ns          280       360.263M/s        40.2585M/s
BM_SpeedOfLightDispatch<16>                    4550963 ns      4550894 ns          155       196.637M/s        21.9737M/s
BM_SpeedOfLightDispatch<32>                    6507077 ns      6507090 ns          107       137.523M/s        15.3679M/s
BM_SpeedOfLightDispatch<MaxDispatchTargets>    9071198 ns      9071217 ns           77       98.6499M/s        11.0239M/s
```

Even though we're not lexing anything in the speed-of-light benchmark,
the tokens-per-second measure is still meaningful because we *generated*
the token stream and know how many tokens we put into it. The dispatch
technique easily exceeds hits 10-million tokens/second, but we need to
do substantially better than that to lex at 10-million lines/second.
Fortunately, when the lexer is consuming more than one-byte tokens,
we're already faster than this. And the bytes-per-second numbers from
all but the worst case dispatch scenario are promising.

---
## [lunar-linux/moonbase-core](https://github.com/lunar-linux/moonbase-core)@[f9e9967baa...](https://github.com/lunar-linux/moonbase-core/commit/f9e9967baa6204f76e052ab78ed759d137bbb69c)
#### Friday 2023-11-24 04:29:34 by Dave Brown

pciutils: Add hard dependency on wget

Even though nothing in core is supposed to be downloading anything from
the Internet as part of its build (because if you're building an ISO, by
definition you'll have an incomplete system), pciutils thinks that it's
special and insists on downloading a new pci.ids file just in case it's
changed in the last half hour or so.

(The pci.ids file chagnes on average once a month. It's not that
special.)

So until there's a better fix, just add another layer of stupid, ugly
hackwork on top of the existing pile of problems.

---
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[2fe6a7fc50...](https://github.com/RustingWithYou/Aurora.3/commit/2fe6a7fc508cd14e6bcb2a5e4e904effb5480a9c)
#### Friday 2023-11-24 04:30:11 by RustingWithYou

Uueoa-Esa Sector

stonks

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

merchant guild camp

guwandi

gawgaryn and katas

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

merchant guild camp

gawgaryn and katas

hegemony base

oasis clans

vihnmes tweak

ruined wasteland village

siakh and izweski outpost

izweski outpost fix

vihnmes tweaks and baseturf tweaks

vihnmes spawner fix

flag fixes

ozeuoi fixes

thakh and skakh sites

reclaimers, bugs and martial artists

bug lighting fix/start of ouerea

ouerea versions of bar, village and heph facility

ouerea, functional edition

aut'akh compound and hegemony base

autakh books

fishing league farm

bunch of generic ruins

bunch more sites

uncomments

genericifies plantspawner

pid away sites

skrell and sol away sites for ouerea

fixes hegemony base path

unexploded nuclear bomb

moghes memorial and sky behemoth wreckage

heph planetary mining station

miners guild outpost

guild mining camps on moghes and ouerea

replaces random gun with random civgun

welcome messages and siakh fixes

siakh area change

lore planets for uueoa-esa

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

lore planets for uueoa-esa

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

lore planets for uueoa-esa

literally fucking around with themes

tweaks to planets so that they work + village

bar and hephaestus mining camp maps

merchant gaming

ouerea versions of bar, village and heph facility

aut'akh compound and hegemony base

bunch more sites

uncomments

genericifies plantspawner

skrell and sol away sites for ouerea

fixes hegemony base path

moghes memorial and sky behemoth wreckage

plant spawners, fixing banned ruins and broken ghostroles

thakh seeds

fixes thakh pilgrim spawn

fixes seed packet spawn and cargo price coeffs

written languages

paper fixes

klax scrubbers to stop vhoron vhires

updates miners guild stuff now the station is merged

indent fix

fixes atmos generation that i broke

ruin banning and literal bug fixes

solarian asteroid ruin

sol asteroid ruin 2: electric boogaloo

sol aseroid tweak

ouerea nt ruin

aaa
omgolo fixes

tret fake planet

engi stuff

ouerea flags

ouerean revolution memorial

a BUNCH of changes

terrain tweaks

Revert "terrain tweaks"

This reverts commit 8a961212d968afb1daa6d381a0786850c2626e73.

sandbike stuff

ihss reclamation 1

ihss reclamation 2

ihss reclamation 3

ihss reclamation 4

ihss reclamation 5

ihss relamation 6

ihss reclamation final tweaks

welcome messages that were missing

3/4 1

colors

access

dorviza limbs & mikuetz languages

hephaestus bans

ouerea ghostrole tweaks

wasteland radiation + fixes

rifles & geigers

fuck you, no lights

hegemony visitor event

more fedship

freewater & caligae fixes

ouerea battlefield

yet more fedship

feuahfiehg

fedship & map fixes

reclamation fixes & warblers

names & fluff

no more dead bug storage

fedbrained

access changes

flag

existing ships can spawn in uwu

the 3/4ing

area flags

---
## [xiaomi-sm7225/android_kernel_xiaomi_gauguin](https://github.com/xiaomi-sm7225/android_kernel_xiaomi_gauguin)@[a8b8c2e2f2...](https://github.com/xiaomi-sm7225/android_kernel_xiaomi_gauguin/commit/a8b8c2e2f26d680fca2b9880924c6456f267c70e)
#### Friday 2023-11-24 04:57:22 by Peter Zijlstra

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
## [uniqpathlab0980/Vitamins-test-in-Greater-Noida](https://github.com/uniqpathlab0980/Vitamins-test-in-Greater-Noida)@[823b42fab3...](https://github.com/uniqpathlab0980/Vitamins-test-in-Greater-Noida/commit/823b42fab31c6666e7edfd049954b6c198139111)
#### Friday 2023-11-24 05:35:57 by uniqpathlab0980

Update README.md

Why Choose Vitamins test in Greater Noida ( UniQ Pathlab) |https://shorturl.at/nzOS2
Vitamins play a crucial role in maintaining our overall health and well-being. In the hustle and bustle of life, it's easy to overlook the importance of these micronutrients. However, understanding and regularly monitoring your vitamin levels can make a significant difference in your health journey. In Greater Noida, UniQ Pathlab stands out as a leading pathology center, offering comprehensive vitamin testing services.

UniQ Pathlab: A Leading Vitamin Test Pathology Center in Greater Noida
When it comes to health diagnostics, trust is paramount. UniQ Pathlab has established itself as a reliable and reputable pathology center in Greater Noida, known for its accuracy and efficiency in test results. With state-of-the-art facilities and a team of experienced professionals, UniQ Pathlab ensures that your health is in good hands.

Why Vitamin Tests Matter 
Vitamins are essential for various bodily functions, including energy production, immune system support, and bone health. However, our modern lifestyles, dietary habits, and environmental factors can contribute to vitamin deficiencies. Regular vitamin tests are a proactive way to identify and address these deficiencies before they manifest into more significant health issues.
Address: Shop No. 4 Basement, B.J. Mart, Jagat Farm, Greater Noida, Uttar Pradesh 201308

Common Vitamin Test  Deficiencies
From vitamin D to B12, deficiencies in these crucial vitamins can lead to fatigue, weakened immunity, and even more severe health conditions. Exploring the common deficiencies allows individuals to be aware of potential symptoms and take timely action to rectify them.

UniQ Pathlab's Comprehensive Vitamin Testing Services
UniQ Pathlab understands the diverse needs of its clients. The pathology center offers a range of vitamin tests, including but not limited to Vitamin D, Vitamin B12, Vitamin C, and more. The comprehensive nature of these tests ensures that all essential vitamins are covered, providing a holistic view of one's nutritional status.

Understanding the Vitamin Testing Process
You might be wondering, how does vitamin testing work? UniQ Pathlab simplifies the process for its clients. A blood sample is usually taken, and advanced diagnostic techniques are employed to measure the concentration of various vitamins in the sample. The accuracy of these tests forms the basis for informed health decisions.

Benefits of Regular Vitamin Testing In Greater Noida
Regular vitamin testing offers numerous benefits. It allows for early detection of deficiencies, enabling timely interventions. Additionally, it provides valuable insights into dietary adjustments and lifestyle changes that can contribute to improved overall health.

Interpreting Vitamin Test  In Greater Noida Results
Understanding your vitamin test results can be a game-changer. UniQ Pathlab ensures that your results are presented in a clear and comprehensible format. The pathology center also provides guidance on interpreting these results and taking the necessary steps to address any deficiencies.

Tailored Recommendations for Vitamin Test In Greater Noida Supplementation
One size does not fit all when it comes to nutrition. UniQ Pathlab goes beyond merely providing vitamin  test results; it offers personalized recommendations for supplementation based on individual needs. This tailored approach ensures that clients receive the most relevant advice for their health goals.

Importance of Localized Vitamin Testing - Greater Noida Perspective
Living in Greater Noida has its perks, and one of them is easy access to quality healthcare services. UniQ Pathlab's presence in the local community makes it convenient for residents to undergo regular vitamin testing without the hassle of traveling far distances.

UniQ Pathlab's Technological Advancements in Vitamin Testing
In a world driven by technology, UniQ Pathlab leverages advanced diagnostic tools to enhance the accuracy and efficiency of vitamin testing. The integration of technology ensures that clients receive precise and reliable results, setting UniQ Pathlab apart in the realm of pathology services.

Customer Experiences and Testimonials
The success of UniQ Pathlab is not just in numbers but in the positive experiences of its clients. Real stories from individuals who have benefitted from UniQ Pathlab's vitamin testing services provide a testament to the center's commitment to excellence in healthcare.

Affordability and Accessibility
Healthcare should be accessible to everyone. UniQ Pathlab understands this and strives to make vitamin testing affordable without compromising on quality. The center believes that everyone should have the opportunity to take proactive steps towards better health.

UniQ Pathlab's Contribution to Community Health
UniQ Pathlab is not just a service provider; it is an active contributor to community health. The center engages in health awareness programs, workshops, and initiatives that empower the community to prioritize their well-being. UniQ Pathlab's commitment extends beyond diagnostics to fostering a healthier and happier community.

---
## [SparklyPower/SparklyPaper](https://github.com/SparklyPower/SparklyPaper)@[d17719e4e3...](https://github.com/SparklyPower/SparklyPaper/commit/d17719e4e378e9391c7ffa9a6c86478ce24e81a7)
#### Friday 2023-11-24 05:52:02 by MrPowerGamerBR

Remove some "dubious" patches

Honestly, some of these changes felt like hopium "surely this will fix the lag issues", even tho in my mind these didn't make sense

Yeah, these methods do show up in the profiler, but does these *really* make sense? I don't think so, I think these are just useless patches that only attempt to hide the pain, instead of tackling the REAL issue that is causing these methods to show up in the profiler

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[0dee3cc079...](https://github.com/treckstar/yolo-octo-hipster/commit/0dee3cc079cb537041d244bf960abf6b50bc3e95)
#### Friday 2023-11-24 06:22:07 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [pompororo/VR_Project](https://github.com/pompororo/VR_Project)@[4f1b22d92d...](https://github.com/pompororo/VR_Project/commit/4f1b22d92d933159f05aa792c5222c9a7d5d039c)
#### Friday 2023-11-24 06:33:30 by pompororo

Fuck you

Co-Authored-By: FrozenTEAR <85834370+froz4d@users.noreply.github.com>

---
## [softcerv/Skyrat-tg](https://github.com/softcerv/Skyrat-tg)@[5761091212...](https://github.com/softcerv/Skyrat-tg/commit/57610912121327266d1b5b47eb6d93bfb33d8362)
#### Friday 2023-11-24 06:41:05 by SkyratBot

[MIRROR] Revert "if you die in a mech you are ejected" [MDB IGNORE] (#25051)

* Revert "if you die in a mech you are ejected" (#79768)

Reverts tgstation/tgstation#79380
this is literally what the mech removal tool is for. gameplay reasons
for that tool missing do not mean that we need to remove its use - if
you want a better solution then let people purchase it... or just smash
the mech- you saving their life and them being sad about their mech is
really funny
the original pr being marked as qol when that was a specific balance
change is very stupid

## Changelog
🆑
del: if you die in a mech you again don't automatically eject
/🆑

* Revert "if you die in a mech you are ejected"

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [Ivanncab511/app-dev](https://github.com/Ivanncab511/app-dev)@[d52a1d95ba...](https://github.com/Ivanncab511/app-dev/commit/d52a1d95ba46504d30974e608c5dfa8f2526fe74)
#### Friday 2023-11-24 07:21:41 by Ivanncab511

My Hero

Takemichi Hanagaki, a 26-year-old temp worker with a gloomy life, who learns that his ex-girlfriend, Hinata Tachibana, has died in a dispute involving the Tokyo Manji Gang. The next day, while returning from a part-time job, Takemichi gets pushed off the subway platform by someone.

---
## [Narido33/app-dev](https://github.com/Narido33/app-dev)@[b49b5279d0...](https://github.com/Narido33/app-dev/commit/b49b5279d04c38a3d782ebb977ede1b8f38dd805)
#### Friday 2023-11-24 07:45:27 by Narido33

Time traveler hero

Takemichi Hanagaki is a freelancer that's reached the absolute pits of despair in his life. He finds out that the only girlfriend he ever had, in middle school, Hinata Tachibana, had been killed by the ruthless Tokyo Manji Gang.

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[517903ce9f...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/517903ce9ff62cc540ad10f6fb3d29fccfa95779)
#### Friday 2023-11-24 07:52:34 by SkyratBot

[MIRROR] Further Prevention of Disposals Qdeletion [MDB IGNORE] (#25015)

* Further Prevention of Disposals Qdeletion (#79714)

## About The Pull Request

Fixes the consequences of #79629 - Verdict is still out on what the root
issue is

This has been an issue for the last two years and everything I go
bananas trying to get a consistent reproduction case to figure out the
root issue. After three session of picking, I think it's just a
consequence of certain thing in disposals code sleeping due to
`addtimer()` and whatnot so I'm just throwing in the towel and just
making it so we stop sending atoms to nullspace for no reason.

`target_turf` is typically always a present arg, but regardless we are
guaranteed to get a valid turf to send people to instead of the deleted
mob room. We still `stack_trace()` whenever this happens, so tracking
this issue doesn't change any more than the present status quo- we just
don't keep torturing mobs by sending them to the shadow realm.
## Why It's Good For The Game

One day we'll figure out why we keep getting `null` passed into
`forceMove()` like this but today is not that day. i know turfs
technically can't be deleted but it's just there as a safety since we
nullcheck anyways (which is the whole point of this fix). Let's just
stop screwing with players for the time being

also the code looks much better
## Changelog
:cl:
fix: Safeties in the code have been added to prevent things in disposals
going into nullspace whenever they get ejected from a pipe - you will
just magically spawn at the turf that you were meant to be flung
towards.
/:cl:

* Further Prevention of Disposals Qdeletion

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[73bdd7341a...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/73bdd7341acdf6f5b7d38a484a1dba8106438c56)
#### Friday 2023-11-24 07:52:34 by SkyratBot

[MIRROR] TGUI Destructive Analyzer [MDB IGNORE] (#25005)

* TGUI Destructive Analyzer (#79572)

## About The Pull Request

I made this to help me move more towards my goals [laid out
here](https://hackmd.io/XLt5MoRvRxuhFbwtk4VAUA) which currently doesn't
have much interest.

This makes the Destructive Analyzer use a little neat TGUI menu instead
of its old HTML one. I also touch a lot of science stuff and a little
experimentor stuff, so let me explain a bit:
Old iterations of Science had different items that you can use to boost
nodes through deconstruction. This has been removed, and its only
feature is the auto-unlocking of nodes (that is; making them visible to
the R&D console). I thought that instead of keeping this deprecated code
around, I would rework it a little to make it clear what we actually use
it for (unhiding nodes).
All vars and procs that mentioned this have been renamed or reworked to
make more sense now.

Experimentor stuff shares a lot with the destructive analyzer, so I had
to mess with that a bit to keep its decayed corpse of deprecated code,
functional.

I also added context tips to the destructive analyzer, and added the
ability to AltClick to remove the inserted item. Removing items now also
plays a little sound because it was kinda lame.
Also, balloon alerts.

## Why It's Good For The Game

Moves a shitty machine to TGUI so it is slightly less shitty, now it's
more direct and compact with more player-feedback.
Helps me with a personal project and yea

### Video demonstration

I show off connecting the machine to R&D Servers, but I haven't changed
the behavior of that and the roundstart analyzers are connected to
servers by default.

https://github.com/tgstation/tgstation/assets/53777086/65295600-4fae-42d1-9bae-eccefe337a2b

## Changelog

:cl:
refactor: Destructive Analyzers now have a TGUI menu.
/:cl:

* TGUI Destructive Analyzer

* Modular

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [f13babylon/f13babylon](https://github.com/f13babylon/f13babylon)@[830db814f3...](https://github.com/f13babylon/f13babylon/commit/830db814f3104bfe595db02eea0759766eb2cd10)
#### Friday 2023-11-24 08:04:33 by GreytidePanda

Expanded Mall (#171)

## About The Pull Request
The northwest mall was an area scraped together from an older mall
building and expanded on by me well over a year ago, but it was always
unfinished as I left Sunset before I submitted the final version. You
can really tell this if you look at some of the suspiciously empty rooms
on the upper levels.

The finished version has been sitting on my harddrive for a long time so
I've copied it in and made a few changes to fit the server. I'm not sure
if the mall is staying with future map changes, but at least for now I
want to be judged on my completed work.

- References to 'Mall of Wyoming' are now 'Mall of Utah'
- A lot of rooms are now less claustrophobic and use their space better
- More loot and detail (no crazy loot - it was always intended as a
fairly beginner friendly zone)
- Now far more vertical - an underground parking lot, and accessible
roof
- Removed the 'requires_power' flag from the mall area tag - no other
ruin uses it
- Fixed the instrument shop shutter not working (I can't believe this
bug has existed for over a year)

## Why It's Good For The Game
Better locations are always good for the game!

## Pre-Merge Checklist
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.


## Changelog
:cl:
add: The Mall of Utah now offers an even bigger shopping experience.
/:cl:

---
## [Little-W/android_kernel_xiaomi_alioth](https://github.com/Little-W/android_kernel_xiaomi_alioth)@[62abe93576...](https://github.com/Little-W/android_kernel_xiaomi_alioth/commit/62abe93576f2000a3c578bdfdf9635ef650acb48)
#### Friday 2023-11-24 08:26:49 by Angelo G. Del Regno

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
5      	      20220479
2      	      20940223
1      	      21231290

Remember again that we're loading from a UFS card and that
we are loading ~1.1MB more out of a 20MB file.
If you're smart enough you surely know already about RAM and CPU
overhead of very high compression levels.

If you still disagree with what I just did, read this commit description
another 20 times, or more, until you understand it. :)))

---
## [schlapzz/dagger](https://github.com/schlapzz/dagger)@[80180aaaed...](https://github.com/schlapzz/dagger/commit/80180aaaed1e1e91a13dbf7df7e0411a9a54c7d3)
#### Friday 2023-11-24 08:34:04 by Justin Chadwell

Fix secret scrubbing log latency (#6034)

* fix: use custom implementation for secret scrubbing

This was a fun exercise in processing streams in go, and an absolutely
massive nerd-snipe :(

Essentially, we need a custom transformer to handle *precisely* matching
Reads on the underlying source with the output - we shouldn't hold
output any longer than is absolutely neccessary.

To be able to do this at all in any reasonable way, we need a trie, and
handle *all* the secrets at once, instead of doing multiple passes.
Multiple passes won't work, since it's possible to accidentally trim too
much at each step, which would be very sad.

> e.g. imagine secrets (aaa, bbb, ccc, etc), and an input (cba)
>
> In removing secret aaa, we would trim to cb, then we'd remove bbb to
> trim to c, then finally trim to nothing. However, this is overly
> enthusiastic, we could easily just trim to cb, if we knew about all
> the secrets at once.

So, we need a trie, and we need a custom implementation of one. This is
because *no off the shelf implementation* seems to allow traversing the
trie state-by-state. Thankfully, it's a pretty short implementation to
implement one from scratch, and not too much harder to turn it into a
radix tree (which lets us use quite a lot less memory).

With our trie, we can implement our custom transformer, which is *an
utter pain*. Honestly, the comments should explain all the fun edge
cases it's possible to hit. There's a lot of tests added as well, each
of which was a real horrible thing I hit while implementing it.

I played around a bit with benchmarking, but ugh, it's a *tiny* bit
slower than the original implementation (maybe by like ~25%?). It's not
huge, but the latency problem is *actually solved*. Some potential
things I did look into and gave up on:
- Only copy into dstBuf when dst is full (requires tons of extra
conditionals, so slows everything down).
- Avoid copies at all costs by having "virtual buffer pointers" into
src, that indicate future data to copy (not only is this *slower*, the
logic becomes truly incomprehensible).
- Playing with off-the-shelf radix tree implementations, but they're so
inconvenient to use for this specific use case, it'd be way more
trouble than it'd be worth.

Any ideas welcome, but honestly, I've looked at enough flamegraphs
today.

Signed-off-by: Justin Chadwell <me@jedevc.com>

* test: avoid use of require.Eventually for secret scrubbing

Signed-off-by: Justin Chadwell <me@jedevc.com>

---------

Signed-off-by: Justin Chadwell <me@jedevc.com>

---
## [tbaederr/llvm-project](https://github.com/tbaederr/llvm-project)@[5cd24759c4...](https://github.com/tbaederr/llvm-project/commit/5cd24759c41864215e67c280234b6c745a4cd369)
#### Friday 2023-11-24 09:12:53 by Louis Dionne

[libc++] Reduce the compilation time required by SIMD tests (#72602)

Testing all the SIMD widths exhaustively is nice in theory, however in
practice it leads to extremely slow tests. Given that
1. our testing resources are finite and actually pretty costly
2. we have thousands of other tests we also need to run
3. the value of executing these SIMD tests for absolutely all supported
SIMD widths is fairly small compared to cherry-picking a few relevant
widths

I think it makes a lot of sense to reduce the exhaustiveness of these
tests. I'm getting a ~4x speedup for the worst offender
(reference_assignment.pass.cpp) after this patch.

I'd also like to make this a reminder to anyone seeing this PR that
tests impact everyone's productivity. Slow unit tests contribute to
making the CI slower as a whole, and that has a direct impact on
everyone's ability to iterate quickly during PRs. Even though we have a
pretty robust CI setup in place, we should remember that it doesn't come
for free and should strive to keep our tests at a good bang for the buck
ratio.

---
## [Perkedel/CVR_Stuffings](https://github.com/Perkedel/CVR_Stuffings)@[1b091d748d...](https://github.com/Perkedel/CVR_Stuffings/commit/1b091d748dd2e78ae2b5b62bb1e60ca86486af73)
#### Friday 2023-11-24 09:16:46 by JOELwindows7

Oh fuck yeah!

Sorry we forgot that. Only in this project.

if that's not clear, dm us... uhh no prefix yet.. maybe `PROFANITY_CONCERN`?

---
## [Robbbert/exp](https://github.com/Robbbert/exp)@[96ab505d66...](https://github.com/Robbbert/exp/commit/96ab505d665a886809e8109a55d5e13fb7e520aa)
#### Friday 2023-11-24 09:41:19 by ArcadeShadow

ibm5170_cdrom.xml: Added 21 items (18 working). (#11760)

New working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
5 Plus One: Pack 12 - Ghostbusters II [redump.org]
Brutal: Paws of Fury (Europe) [redump.org]
Darkseed (Germany, Action Sixteen release) [redump.org]
Dune (Europe, White Label release) [redump.org]
Dune II - Battle for Arrakis (Netherlands) [redump.org]
Dune II - Battle for Arrakis (Germany, PC Games Collection 2 release) [redump.org]
Dune II - The Building of a Dynasty (USA, Gold Medal 12 CD Pack) [redump.org]
Fables & Fiends - Book Three: Malcolm's Revenge (Europe, Japan) [redump.org]
Fables & Fiends - Book Two: The Hand of Fate (UK, Sold Out release) [redump.org]
Jurassic Park (Europe) [redump.org]
Jurassic Park (Germany) [redump.org]
Jurassic Park (USA) [redump.org]
Star Control [redump.org]
Stellar 7 (USA) [redump.org]
Stellar 7 (USA, alt) [redump.org]
The Cool Croc Twins + Magic Boy (Europe, 2 Game Pack release) [redump.org]
The Cool Croc Twins + Magic Boy (Netherlands) [redump.org]
The Dig (Japan) [redump.org]

New NOT working software list additions (ibm5170_cdrom.xml)
--------------------------------------------
Darkseed (USA) [redump.org]
Darkseed (USA, alt) [redump.org]
Dogfight: 80 Years of Aerial Warfare (Europe) [redump.org]

---
## [Vallat/tgstation](https://github.com/Vallat/tgstation)@[10f194781d...](https://github.com/Vallat/tgstation/commit/10f194781db0a6b2e71d2769a07fca7d5960c21f)
#### Friday 2023-11-24 09:57:35 by Jacquerel

It is now possible to survive the Mansus  (#79131)

## About The Pull Request

Fixes #79113

There were a handful of bugs with the Mansus realm, this PR fixes them.

Firstly an most importantly, a refactor to damage handling touched the
"unholy determination" effect incorrectly (and I'm not even sure why?),
causing it to damage you instead of healing you most of the time. This
damage was not avoidable, so most people would be crit shortly after
entering the area and stay there.

Secondly, some of the heretic realms were unlit. A change to when
lazyloaded template atmosphere initialises means that the bonfires were
trying to light themselves with no air. Now they do this in
late_initialize instead, giving time for air to arrive.

Thirdly, the spooky hands were runtiming when passing through transit
tiles outside of the bounds of the heretic map. They shouldn't be
effected by shuttle drag anyway, so now they aren't.

Fourthly, I removed a row of empty space at the edge of the heretic map,
just because it annoyed me slightly.

Finally, while I was touching the heretic buff I made it heal you 1/4 as
much as it originally did. This is a balance change rather than a fix,
I'll atomise it out if it is controversial but I don't really expect it
to be.
In the future I would like to come back to these and make each realm
more specific to the path, because I think we could make these both more
exciting and more characterful.

## Why It's Good For The Game

Once it is working properly, the hand dodging minigame is actually
extremely forgiving, even if you don't move very much and get frequently
hit. This means some of those hits might actually add some tension.

## Changelog

:cl:
fix: You should be revived properly when entering the mansus realm
following a heretic sacrifice
fix: The buff which is supposed to heal you in the mansus realm will now
do that instead of unavoidably damaging you
balance: The mansus realm's healing buff heals for 25% as much as it did
before it was broken
/:cl:

---
## [aleslab/Psychtoolbox-3-aleslab-fork](https://github.com/aleslab/Psychtoolbox-3-aleslab-fork)@[ecbf87a62a...](https://github.com/aleslab/Psychtoolbox-3-aleslab-fork/commit/ecbf87a62a1453ea5ebea95325203e099a3a75c3)
#### Friday 2023-11-24 10:33:28 by Mario Kleiner

PsychOpenXR: Add initial eyetracking via HTC SRanipal.

Requires SRAnipalMex to work and on the path, otherwise standard OpenXR eyetracking is
used. The mex file and source code is not yet included in the Psychtoolbox distribution.

This works with and requires the HTC proprietary SRanipal eye tracking api for MS-Windows,
in combination with a supported HTC HMD, e.g., HTC Vive Pro Eye (tested) or HTC Vive Cosmos
or HTC Vive Focus 3 with eye tracker hardware extension, the latter two untested, but assumed
to work in the same way.

It allows binocular eye tracking for left and right eye separately, returning two separate eye
gaze samples. Additionally a 3rd combined "cyclops eye" sample is returned, which is the fusion
or average of the two eye gaze samples, similar (identical?) to what HTC's implementation of
the OpenXR XR_EXT_eye_gaze_interaction extension returns as sole eye pose.

Implementation notes:

While OpenXR eye tracking with the standard OpenXR extension only works with a maximum
sampling rate of 60 Hz, ie. blocking the calling code for approximately 16 msecs for each
query in PsychVRHMD('PrepareRender') or PsychOpenXRCore('GetTrackingState', ..., 4), this
works with up to native sampling rate of the eyetracker, in this case 120 Hz / one sample
every approximately 8.3 msecs. As it turns out, one needs to use the callback api to get max
rate and minimum latency/overhead, where our callback is called from SRanipals own thread.
With the non-callback api's it is always blocking calls with 16 msecs+ duration resulting in poor
performance. The latter seems to be what HTC's implementation of OpenXR eyetracking does.

The HTC proprietary api delivers more detailed info than current official OpenXR extensions,
so both from a performance perspective and richness of information perspective it is clearly
perferrable to use the HTC proprietary api when available on a HTC HMD. The quality of the
api docs is horrifying however, and often faulty, so using it is somewhat a pain in the ass.

The type and units of returned information from SRanipal is different from what OpenXR
returns or uses, so some hacks had to be used to sort-of convert to OpenXR compliant format.

Currently the raw gaze samples are not 7 component vectors with eye position (x,y,z) and
orientation quaternion (rx,ry,rz,rw), but only 6 component vectors with orientation encoded
differently, and some shady matrix math hacks to get a sort of usable / sort of ok'ish gazeMat
matrix for eyegaze out of it. From that we derive other info like global gaze matrix, 3D eye
gaze vectors and 2D (x,y) gaze sample positions the usual way via the code shared with
regular OpenXR gaze tracking.

Some oddities - the reason for these is totally unclear:

- We need to switch some signs in the math - Is it a bug in HTC's runtime? A feature? A quirk?
I don't know.

- Eye center of the left eye seems to be stored in right eye, and vice versa, but the end result
wrt. 2D gaze position is the same, and the 3D gaze vectors originate in puzzling locations but
point to and converge in the correct gaze location. Again, could not find out why.

---
## [Gry4hon/MadeWithAbby.com](https://github.com/Gry4hon/MadeWithAbby.com)@[5e5ab51662...](https://github.com/Gry4hon/MadeWithAbby.com/commit/5e5ab51662fd2143c7e13be17f35e6ae202520ff)
#### Friday 2023-11-24 10:56:38 by Gry4hon

The website (for now!)

The brain child of my girlfriend is here! Enjoy!

---
## [alphagov/signon](https://github.com/alphagov/signon)@[42c64cfbd6...](https://github.com/alphagov/signon/commit/42c64cfbd6e382152b7b7226c539f426e233c792)
#### Friday 2023-11-24 12:30:21 by James Mead

Extract page for change user's 2SV requirement

Trello: https://trello.com/c/caETStGa

This is about changing the value of `User#require_2sv`. This is used in
combination with `Organisation#reqire_2sv?` in the implementation of
`User#require_2sv?`. The value of `User#require_2sv` can be changed from
false -> true OR from true -> false and it's only in the former case
that we're "mandating" 2SV. That's why I've used "2SV requirement" in
the copy and the code.

This is a step on the journey to move the edit user page to use the
GOV.UK Design System. The new design calls for separate pages for
different operations on a user and this is the next one.

Unlike in commits like this one [1] where we first split out the new
page and then separatly moved the new page to use the Design System,
here I've created the new page using the Design System in one go,
because there wasn't much markup in the "edit user" page to
extract.

The new `app/views/users/two_step_verification_requirements/edit.html.erb`
template is based on other similar pages which we've recently extracted,
e.g. `app/views/users/organisations/edit.html.erb`. The hidden field for
"user[require_2sv]" with value 0 is necessary, because we're now using
the Design System `checkboxes` component rather than
`ActionView::Helpers::FormBuilder#check_box`. I've given the hidden
field an explicit element ID to distinguish it from the checkbox field.

The new `Users::TwoStepVerificationRequirementsController` is closely
based on the relevant bits of code from `UsersController`, even though
some of it is probably overkill in the new context, e.g. the use of
`UserUpdate` & `UserParameterSanitiser`. However, I thought it was worth
keeping this step as small as possible.

I'm using `UserPolicy#mandate_2sv?` for the authorization in the new
`Users::TwoStepVerificationRequirementsController`, because that seems
to make the most sense. You could argue that I should also check
`UserPolicy#edit?` & `UserPolicy#update?` like I did in
`Users::OrganisationsController` in this commit [2], but I've gone off
that idea (sorry, @chrisroos!). Instead I've matched what I did in
`Users::TwoStepVerificationResetsController` in this commit [3].

There weren't any tests in `UsersControllerTest` for this behaviour, so
I had to write `Users::TwoStepVerificationRequirementsControllerTest`
from scratch, but I based it closely on other similar controller tests.
Luckily there was an integration test
(`test/integration/managing_two_step_verification_test.rb`) covering the
behaviour which I've been able to fixup to work with the new UI.

Rather than creating a combinatorial explosion of tests in
`Users::TwoStepVerificationRequirementsControllerTest` relating to
whether a user with all the different roles can edit another user with
all the different roles, I've resorted to stubbing `UserPolicy.new` and
`UserPolicy#mandate_2sv?`. Although this is a bit ugly, since
`UserPolicy` is thoroughly tested in `UserPolicyTest`, it seems like a
pragmatic option.

I'm using the `error_summary` component in combination with identical
code we've used elsewhere so that the errors in the summary link to the
relevant form field. Unfortunately I haven't been able to set the error
message on the checkboxes component so that any relevant errors are
displayed alongside the `require_2sv` field and the field itself is
highlighted in red as per this Design System guidance [4], because there
seems to be a bug in the `checkboxes` component.

Note that in normal operation there are unlikely to be validation errors
on this page, but since it's theoretically possible I thought it was
worth adding the error summary. We might want to consider changing this
to work more like `Users::TwoStepVerificationResetsController` which
raises an exception if there is a validation error. This makes sense
particulalry given that the only validation on `User#require_2sv` only
applied on recrod creation.

[1]: https://github.com/alphagov/signon/commit/899a8a16356ad3b9e3434feaf99f5e5f2bf8a243
[2]: https://github.com/alphagov/signon/commit/bf207efe2769c0ae48102b40bb6df8e4f7ce7770
[3]: https://github.com/alphagov/signon/commit/1baf6856c34f857d71466ec3cb11e974a141175d
[4]: https://design-system.service.gov.uk/patterns/validation/#how-to-tell-the-user-about-validation-errors

---
## [BurgerLUA/Bubberstation](https://github.com/BurgerLUA/Bubberstation)@[52f69b96ee...](https://github.com/BurgerLUA/Bubberstation/commit/52f69b96eebfbe14a763ae9c5a8dd7ef156c4582)
#### Friday 2023-11-24 13:03:27 by The-Sun-In-Splendour

mid-round salt pr about EMP mold because being repeatedly shocked 500 times in a row unless you get charcoal (now called syniver or whatever fuck new chems) is not what I consider to be fun gameplay (#755)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
emp mold mosquitoes no longer put you in shock stunlock hell because
that shit is not funny
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game
it made me mad and this is a salt pr

![image](https://github.com/Bubberstation/Bubberstation/assets/70348069/b5002caa-d401-478a-9d48-fbc772c05b3e)

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
balance: emp mold mosquitoes no longer shock you all the time until you
have a stroke irl over the annoyance
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

---
## [Singul0/tgstation](https://github.com/Singul0/tgstation)@[ff0aea800b...](https://github.com/Singul0/tgstation/commit/ff0aea800b0ce03346d7a655deadf8b53d7f098d)
#### Friday 2023-11-24 13:17:43 by carlarctg

Bladists can now use silver *or* titanium while creating their blades (#78701)

## About The Pull Request

Blade Heretics can now use silver *or* titanium while creating their
blades.

## Why It's Good For The Game

Silver quite literally *only* exists on surgery tables. Being a blade
heretic with shit miners/roundstart means one of several things.

1. Wait for miners to come back with enough silver (They might never
come back or they might have not gotten any silver)

2. Go to lavaland to dig your own silver (Extremely time-consuming on
the antagonist role that has most downtime, death knell for latejoin
heretics)

All that is not even to mention that for some reason it takes two sheets
rather than one, and surgery tables give one silver when scavenged.

This all combined makes obtaining blades super annoying as the BLADE
path.

Now we can farm titanium off shuttles if the miners are jacking off or
dead, or if we joined 9 minutes to roundend.

## Changelog

:cl:
qol: Bladists can now use silver *or* titanium while creating their
blades
/:cl:

---
## [norbert-acedanski/supernatural-guide](https://github.com/norbert-acedanski/supernatural-guide)@[b0a1edead9...](https://github.com/norbert-acedanski/supernatural-guide/commit/b0a1edead90b60dd9b6c90df0def19f7d002fc8b)
#### Friday 2023-11-24 13:30:22 by Norbert Acedanski

Add Vengeful spirit, Demon, Reaper, Angel, Empty appearances.
Add GOD clues.
Add Nephilim clue.
All episodes done.
S14E20

---
## [fjfdepedro/space-launches-app](https://github.com/fjfdepedro/space-launches-app)@[6aa9fddaf8...](https://github.com/fjfdepedro/space-launches-app/commit/6aa9fddaf884c7e9fea0fab3e2763771a2858cb6)
#### Friday 2023-11-24 13:42:28 by Paco Fernández

aider: Updated `pages/index.tsx` and `components/LaunchItem.tsx` to use Tailwind CSS for styling.

# Aider chat conversation:

USER: what is tailwindcss?

ASSISTANT: Tailwind CSS is a highly customizable, low-level CSS framework that gives you all of the building blocks you need to build bespoke designs without any annoying opinionated styles you have to fight to override.

Unlike many other CSS frameworks that offer predefined components, Tailwind allows you to construct your own components by combining a series of CSS utility classes.

Tailwind CSS is described as a utility-first CSS framework. Utility-first CSS is a method of styling where new classes are introduced for each style variation. This means that you can build a component by combining many utility classes, instead of writing custom CSS.

For example, if you want to create a button with Tailwind CSS, instead of writing custom CSS like this:

```css
.button {
  padding: 10px 20px;
  background-color: blue;
  color: white;
  border-radius: 5px;
}
```

You would use utility classes in your HTML like this:

```html
<button class="px-4 py-2 bg-blue-500 text-white rounded">Button</button>
```

Each class in Tailwind is a self-contained piece of styling (a utility). The classes `px-4`, `py-2`, `bg-blue-500`, `text-white`, and `rounded` each apply a single rule of CSS.

Tailwind CSS also supports responsive design, pseudo-classes, and can be customized to fit your design needs. It's designed to be highly efficient and performant, and it's become very popular in modern web development.

USER: my html and css files use tailwind?

ASSISTANT: Based on the files you've shared, it appears that your project is using Tailwind CSS. The `pages/globals.css` file includes Tailwind's base, components, and utilities styles:

<source>css
pages/globals.css
@tailwind base;
@tailwind components;
@tailwind utilities;
...
</source>

These directives are replaced by Tailwind's pre-generated CSS styles during the build process.

Also, the presence of `tailwind.config.ts` file in your project indicates that Tailwind CSS is being used. This file is used to customize Tailwind's default configuration.

However, I don't see any specific usage of Tailwind CSS classes in the HTML (JSX) code you've shared. Tailwind CSS classes are typically used directly in your HTML or JSX files. For example, you might see something like this:

```jsx
<div className="flex items-center justify-center h-screen bg-gray-200">
  <h1 className="text-2xl font-bold text-blue-700">Hello, world!</h1>
</div>
```

In this example, `flex`, `items-center`, `justify-center`, `h-screen`, `bg-gray-200`, `text-2xl`, `font-bold`, and `text-blue-700` are all Tailwind CSS utility classes.

If you're not seeing any Tailwind CSS classes in your JSX files, it's possible that they're being used in files that haven't been shared yet.

USER: I added these *read-write* files: tailwind.config.ts

ASSISTANT: Great! Now that the `tailwind.config.ts` file is in *read-write* mode, we can propose changes to it if needed. However, based on the information you've provided so far, I don't see any immediate need for changes to this file.

The `tailwind.config.ts` file is used to customize Tailwind's default configuration. It's where you can customize your design system, like defining the colors, spacing/sizing scale, typography, etc. that you want to use in your project.

If you have any specific changes you'd like to make to this file, please let me know!

USER: could you change my `pages/index.tsx` `components/LaunchItem.tsx` `components/LaunchItem.tsx` and use tailwind?

ASSISTANT: Sure, we can update your `pages/index.tsx` and `components/LaunchItem.tsx` files to use Tailwind CSS for styling. Here are the proposed changes:

For `pages/index.tsx`, we'll add some padding and center the text:

<source>tsx
pages/index.tsx
<<<<<<< HEAD
export default function Home({ launches }: { launches: Launch[] }) {
  console.log('launches', launches);
  return (
    <div>
      <h1>
        SpaceX Launches
      </h1>
      <div>
        <Launches launches={launches} />
      </div>
    </div>

  )
}
=======
export default function Home({ launches }: { launches: Launch[] }) {
  console.log('launches', launches);
  return (
    <div className="p-6">
      <h1 className="text-center text-3xl font-bold">
        SpaceX Launches
      </h1>
      <div>
        <Launches launches={launches} />
      </div>
    </div>
  )
}
>>>>>>> updated
</source>

For `components/LaunchItem.tsx`, we'll add some margin, padding, and border styling:

<source>tsx
components/LaunchItem.tsx
<<<<<<< HEAD
export function LaunchItem({ launch }: { launch: Launch }) {
  return (
    <a key={launch.id} href={launch.links.video_link}>
      <h3>{ launch.mission_name }</h3>
      <p><strong>Launch Date:</strong> { new Date(launch.launch_date_local).toLocaleDateString("en-US") }</p>
    </a>
  );
}
=======
export function LaunchItem({ launch }: { launch: Launch }) {
  return (
    <a key={launch.id} href={launch.links.video_link} className="block p-4 m-2 border rounded shadow">
      <h3 className="text-xl font-bold">{ launch.mission_name }</h3>
      <p><strong>Launch Date:</strong> { new Date(launch.launch_date_local).toLocaleDateString("en-US") }</p>
    </a>
  );
}
>>>>>>> updated
</source>

These changes will apply Tailwind CSS classes to your components for styling. Please review and apply these changes if they meet your requirements.

---
## [RandomGuy3015/5IAR_bot_arena](https://github.com/RandomGuy3015/5IAR_bot_arena)@[aa4cee6229...](https://github.com/RandomGuy3015/5IAR_bot_arena/commit/aa4cee6229bf7bf72f31b967898483f7bb8c7fa5)
#### Friday 2023-11-24 14:33:03 by Kai

Revert "fixed tylers ugly bad bad evil shitty bot 3.0"

This reverts commit bedf02121616435b3ec32dd45edffe073a9a29b7.

---
## [Project-Mist-OS/frameworks_base](https://github.com/Project-Mist-OS/frameworks_base)@[49eafee12f...](https://github.com/Project-Mist-OS/frameworks_base/commit/49eafee12fbeea6416874c6ee47b9f4dec345af2)
#### Friday 2023-11-24 14:41:21 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>
Signed-off-by: Hưng Phan <phandinhhungvp2001@gmail.com>

---
## [kokizzu/Mindustry](https://github.com/kokizzu/Mindustry)@[6200f08cd8...](https://github.com/kokizzu/Mindustry/commit/6200f08cd84b9a74563beddfe0c89106a43f6e1d)
#### Friday 2023-11-24 14:41:53 by Darkness

Remove Darkdustry from the Global Server List (#9289)

The time has come. It's been more than two years since we started Mindurka, which was later renamed to Darkdustry. It was an amazing time and an amazing experience to maintain the server, to create plugins and gamemodes, to discuss mindustry with all of you. But It's enough. The server is getting constantly DDoSed, the host dies all the time and I have no motivation to develop anything related to Mindustry. 
Goodbye. And I hope, we'll meet again.

---
## [codewithvk/online](https://github.com/codewithvk/online)@[3185307c7a...](https://github.com/codewithvk/online/commit/3185307c7afa5e76bd10b76a2d97ecbdbc97455a)
#### Friday 2023-11-24 15:11:32 by Skyler Grey

Stop hiding both menu and notebookbar softlocking

Previously, when using the Collapse_Notebookbar postmessage or
equivalent ui_defaults (SpreadsheetToolbar=false, etc.), particularly in
compact mode, it was possible to additionally hide the menu bar. As the
button to show the menu bar is on the notebookbar, this meant that you
couldn't reactivate either notebookbar or menubar until you refreshed
the page. This is particularly annoying in integrators that may not
provide an easy way to reload the page

This commit makes it so that hiding the menu bar automatically
uncollapses the notebookbar and won't let it be collapsed again. Whether
the notebook bar should be collapsed (the last thing done to it was a
collapse) is remembered and restored after the menu bar is shown again,
so if you send a postmessage that will affect the state of the
notebookbar after the menu is shown (even though it will not affect the
notebookbar's state immediately)

Caveats:
- If you are hiding the notebookbar to limit the control the user has,
  that's broken by this commit as it makes it impossible to hide both
  the menu and notebook bars at the same time.
- The notebook bar will be hidden again when re-showing the menu bar,
  however there still isn't a way to hide the notebook bar in normal
  use (i.e. without using either postmessage or ui_defaults) while in
  compact mode (although there is a workaround to show it- switching
  into tabbed mode and then back!). It might be nice to have one.

Other considered solutions:
- We could add a new button that allowed you to reopen the menu if both
  menu and notebookbar were hidden
  - Not sure there's much benefit to this over just doing what we're
    doing here, and it's harder to implement
- We could disable the button to hide the menu bar when the notebookbar
  is collapsed
  - As far as I know, there's no button in the UI to show the notebook
    bar. This would make it impossible to hide the menu bar if the
    notebookbar was hidden via postmessage or ui_defaults

Signed-off-by: Skyler Grey <skyler.grey@collabora.com>
Change-Id: Ieab6d72a6be181aba88e9a5b21dda16a369b9e54

---
## [ParadiseSS13/Paradise](https://github.com/ParadiseSS13/Paradise)@[6a109ade7f...](https://github.com/ParadiseSS13/Paradise/commit/6a109ade7f7cd612dcd371f64c4485340ab963d9)
#### Friday 2023-11-24 15:39:22 by Henri215

Moves a few sprites out of items.dmi (#23301)

* fuck you items.dmi

* banhammer

---
## [johnhaddon/cortex](https://github.com/johnhaddon/cortex)@[36be6d6258...](https://github.com/johnhaddon/cortex/commit/36be6d625873e7e1daaf78332aadd38c7665f66f)
#### Friday 2023-11-24 15:48:40 by John Haddon

ExceptionAlgo : Fix `translatePythonException()` reference counting bug

The `PyErr_Fetch()` documentation says "you own a reference to each object retrieved", which means we need to decrement the reference count before returning, as we have no interest in sharing ownership. We were doing this via the `boost::python::handle<>` objects in `formatInternal()`, but since d0731a3e9f0757760e618cb5a68d74e0651273b9 we haven't been calling `formatInternal()` for exceptions bound via `IECorePython::ExceptionClass`. That meant we were leaking such Python exceptions such that they would never be destroyed.

The solution, and the moral of the story, is to always hold `PyObject *` via a sensible RAII class like `handle` or `object`, and to always do that _as early as possible_.

You might be forgiven for thinking that leaking a little exception object isn't that big a deal. But Python exceptions have a `__traceback__` attribute that contains the entire stack at the point the exception was raised, and _that_ contains all the local variables from all of those stack frames. So the leak can actually include a completely arbitrary amount of stuff.

---
## [Striders13/tgstation](https://github.com/Striders13/tgstation)@[2532911353...](https://github.com/Striders13/tgstation/commit/2532911353d63661b735004f2895103d45858b50)
#### Friday 2023-11-24 15:56:41 by LemonInTheDark

Adds pathmaps, refactors pathfinding a bit (#78684)

## About The Pull Request

Implements /datum/pathfind/sssp, which generates /datum/path_map

/datum/path_maps allow us to very efficently generate paths to any turf
they contain from their central point.

We're effectively running the single source shortest paths algorithm.
We expand from the center turf, adding turfs as they're found, and then
processing them in order of addition.
As we go, we remember what turf "found" us first. Reversing this chain
gives us the shortest possible path from the center turf to any turf in
its range (or the inverse).

This isn't all that useful on its own, outside of a few niche cases
(Like if we wanted to get the farthest reachable turf from the center)
but if we could reuse the map more then once, we'd be able to swarm
to/from a point very easily.

Reuse is a bit troublesome, reqiures a timeout system and a way to
compare different movables trying to get paths.
I've implemented it tho. I've refactored CanAStarPass to take a datum,
/datum/can_pass_info. This is built from a movable and a list of access,
and copies all the properties that would impact pathfinding over onto
itself.

There is one case where we don't do this, pathing over openspace
requires checking if we'd fall through the openspace, and the proc for
that takes an atom.
So instead we use the weakref to the owner that we hold onto, and hold
copies of all the values that would impact the check on the datum.

When someone requests a swarmed path their pass info is compared with
the pass info of all other path_maps centered on their target turf. If
it matches and their requested timeout isn't too short, we just reuse
the map.

Timeout is a tricky thing because the longer a map exists the more out
of date it gets.
I've added a few age defines that let you modulate your level of risk
here. We default to only allowing maps that are currently
being generated, or finished generating in our tick. 
Hopefully this prevents falling into trouble, but consumers will need to
allow "failed" movements.

As a part of this datumized pass info, I've refactored pathfinding to
use access lists, rather then id cards directly. This also avoids some
dumbass harddel oppertunities, and prevents an idcard from changing mid
path.

Did a few things to the zPass procs, they took args that they did NOT
need, and I thought it'd be better to yeet em.

If you'd all like I could undo the caching/can_pass_info stuff if you'd
all like. I think it's useful generally because it avoids stuff changing
mid pathfind attempt, but if it's too clunky I could nuke it.

Oh also I added optional args to jps that constricts how it handles
diagonals. I've used this to fix bot paths.

## Why It's Good For The Game

Much of this is redundant currently. I'm adding it because it could have
saved hugglebippers, and because I get the feeling it'll be useful for
"grouping" mobs like bees and such.
We're doing more basic mob work currently and I want to provide extra
tools for that work.


https://github.com/tgstation/tgstation/assets/58055496/66aca1f9-c6e7-4173-9c38-c40516d6d853

## Changelog
🆑
add: Adds swarmed pathfinding, trading accuracy for potential
optimization of used correctly
fix: Bots will no longer take diagonal paths, preventing weirdo looking
path visuals
refactor: Refactored bits of pathfinding code, hopefully easier to add
new pathfinding strategies now
/🆑

---
## [Aleguhs/Watched-but-Unseen](https://github.com/Aleguhs/Watched-but-Unseen)@[1169d9fdba...](https://github.com/Aleguhs/Watched-but-Unseen/commit/1169d9fdbacd1a43e8ab609402507de6bd301268)
#### Friday 2023-11-24 16:06:06 by Aleguhs

Watched but Unseen

This thesis uses the lens of the interactive installation "Watched but Unseen" to explore the state of people under the pressure of contemporary society and the complex relationship with individual freedom. This article draws on the growing rates of unhappiness, as well as social pressure and the relationship between art and society, to lead to our project "Watched but Unseen". We use symbolic and interactive elements to allow the audience to interact with it in the process. It further allows people to experience the standpoints of various social roles under the pressure of today's society, prompting people to reflect on individual needs in today's society.

---
## [sorphin/awesome-docker](https://github.com/sorphin/awesome-docker)@[3164d6df94...](https://github.com/sorphin/awesome-docker/commit/3164d6df94f60d7d3d11629241c111ed416eb8eb)
#### Friday 2023-11-24 16:31:46 by Derek Lee

Add Kurtosis to list of testing tools (#1063)

* Add Kurtosis to list of testing tools

Hey team! We'd like to add Kurtosis to the list of testing tools. 

*What is Kurtosis?* Kurtosis is a built system for multi-(docker)container test environments. 
*What is Kurtosis for?* Kurtosis is for engineers who dev against large distributed systems/applications and who experience pain when trying to configure multi (Docker) container environments for their testing workflows. 

Kurtosis can be used locally without the need to sign up and is free-forever under a source-available license (BSL). 

We have:
- Linked out to our Github: https://github.com/kurtosis-tech/kurtosis
- [A README on our GIthub](https://github.com/kurtosis-tech/kurtosis#readme)
- Content about how to setup/install the project (in our [Github README](https://github.com/kurtosis-tech/kurtosis#to-start-using-kurtosis) and on our [docs](https://docs.kurtosis.com/install)),
- Lots of great examples on: [Github](https://github.com/kurtosis-tech/awesome-kurtosis#awesome-kurtosis-) and in our [docs](https://docs.kurtosis.com/). 

I followed the [Quality Standards](https://github.com/veggiemonk/awesome-docker/blob/master/.github/CONTRIBUTING.md#quality-standards) you guys wrote, but please let me know if you've got any questions about Kurtosis or if we missed something!

Thanks

* add "composable" to description

---
## [ss220-space/Skyrat-tg](https://github.com/ss220-space/Skyrat-tg)@[caa13c44af...](https://github.com/ss220-space/Skyrat-tg/commit/caa13c44af926e36843fdeb8c50460d6566a6cd7)
#### Friday 2023-11-24 18:19:23 by SkyratBot

[MIRROR] Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished [MDB IGNORE] (#25038)

* Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished (#79694)

## About The Pull Request

Related: #78017

Stop drop and roll is no longer instant -5 fire stacks -> stun -> wait.

Now, when you stop drop and roll, every time you roll you will lose 1
firestack.

A roll is triggered every 0.8 seconds. Moving, getting up, or becoming
incapacitated / stunned will stop you from rolling.
_(This number puts it roughly equivalent to its current rate.)_

While rolling, your hands are blocked (you cannot use items, hold
things, etc.)
Additionally, you will roll until all firestacks are cleared.

## Why It's Good For The Game

Getting stunned for 6 seconds because you decide to stop and roll is a
little silly. Reasonably you could stop rolling and get back up should
the need arise, such as "oh god there's more fire I gotta relocate".

By changing it to a gradual thing, it makes it a bit more reasonable and
fair.
- New players who immediately slam "STOP DROP ROLL" because the alert on
their screen tells them to are no longer helpless for 6 whole seconds
- People who hit the resist key, intending to interact with something
else (such as a bola) are no longer stuck rolling when they did not want
to

## Changelog

:cl: Melbert
balance: Stop, drop, and roll no longer instantly clears 5 fire stacks
off of you - Instead, it will clear 1 fire stack off of you every time
you roll, with a roll every 0.8 seconds.
balance: Stop, drop, and roll no longer stuns you for 6 seconds.
Instead, it will knock you to the floor while you are rolling. Moving
around or getting up will cancel the roll, and you cannot use items
while rolling around.
balance: Stop, drop, and roll will now repeat until the fire is put out
or you get up.
/:cl:

* Reworks stop, drop, roll into a gradual, interruptable thing, that repeats until extinguished

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [ss220-space/Skyrat-tg](https://github.com/ss220-space/Skyrat-tg)@[318d5b38d7...](https://github.com/ss220-space/Skyrat-tg/commit/318d5b38d734129579050a98107b044cfb2791e2)
#### Friday 2023-11-24 18:19:23 by SkyratBot

[MIRROR] Fixes Relay Attackers Misfire [MDB IGNORE] (#25039)

* Fixes Relay Attackers Misfire (#79731)

## About The Pull Request

Fixes #76079

Basically we were both not getting all of the args that we recieve from
`COMSIG_ITEM_AFTERATTACK` which included the very important
`proximity_flag` which tells us if the person was in range to actually
hurt us or not. This means that clicking a mob with this element with a
stack of metal from across the room would cause them to aggro, which
makes no sense whatsoever. Let's actually use that proximity check.

We listen for projectiles hitting us separately, don't worry.
## Why It's Good For The Game

It just makes no damn sense, fixes some weird ass behavior.
## Changelog
:cl:
fix: Bar Bots (and several other mobs) will no longer aggro on you if
you click on them with a "forceful" item from halfway across the room.
/:cl:

* Fixes Relay Attackers Misfire

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [multiverse-95/glados-tts](https://github.com/multiverse-95/glados-tts)@[9e739528ad...](https://github.com/multiverse-95/glados-tts/commit/9e739528ad6b2c99d56ce5294d531bf2b7d4d6ea)
#### Friday 2023-11-24 18:36:10 by multiverse-95

KILL AND EAT GOD AND DEVIL, ALL ANGELS, ALL DEMONS, ALL GIRLS, ALL WOMEN, ALL ANDROIDS, ALL 2B, ALL 9S, ALL DOCTORS, ALL MASTERS, ALL TIMELORDS, ALL NEO, ALL SMITH ,ALL MANKIND IN ALL MULTIVERSE IN REAL WORLD 25.11.2023 02:00 FOREVER.

---
## [Cpt-Hazama/AVP-2010-MapDumps](https://github.com/Cpt-Hazama/AVP-2010-MapDumps)@[8cbc30b675...](https://github.com/Cpt-Hazama/AVP-2010-MapDumps/commit/8cbc30b6753c059197caf07d4e3303639e1dade5)
#### Friday 2023-11-24 19:17:51 by Cpt. Hazama

41000 bitrate + foobar said fuck your folder paths

---
## [PennyLaneAI/pennylane](https://github.com/PennyLaneAI/pennylane)@[47e74e16d0...](https://github.com/PennyLaneAI/pennylane/commit/47e74e16d0fb27aedc5ffab69aefaf5188115038)
#### Friday 2023-11-24 19:30:49 by Matthew Silverman

simplify state reordering logic (#4817)

**Context:**
I wrote the same function twice, differing only by state flattening, to
get the DQ upgrade done. It's starting to cause trouble.

**Description of the Change:**
Greatly simplified the state re-arrangement logic. There used to be a
whole mess of things happening, but now things are much more
straightforward.
1. `simulate` first puts things in our "standard" order, and this means
that if any measured wires are not also operator wires, they are put to
the _end_ of our tape wires. Therefore, for each measured-only wire, we
just have to stack a `zeros_like(state)` to the last axis of our final
state! `simulate` never tried to transpose wires back to a different
ordering, so that was always wasted work.
2. `StateMP.process_state` _always_ receives the full state, and never
needed to pad. No other device has done this optimization (the function
used to literally just `return state` before DQ2 migration), and
`simulate` already ensures that the final state has all wires in it -
they just might be out of order. The only thing we might need from
`process_state` is a transposition to the correct wire order. The
inputted `wire_order` _should_ always be `range(len(wires))`, but
whatever, we don't need to assume that.

I'll paint a picture for a normal scenario:

```python
@qml.qnode(qml.device("default.qubit", wires=3))
def circuit(x):
    qml.RX(x, 0)
    qml.CNOT([0, 2])
    return qml.state()
```

What happens with this QNode?
1. Device preprocessing sticks the device wires (`[0, 1, 2]`) onto the
`StateMP`
2. `simulate` maps the wires to our standard order. I'll demonstrate
(with `probs` so I can specify wires):

```pycon
>>> qs = qml.tape.QuantumScript([qml.RX(1.1, 0), qml.CNOT([0, 2])], [qml.probs(wires=[0, 1, 2])])
>>> qs.map_to_standard_wires().circuit
[RX(1.1, wires=[0]), CNOT(wires=[0, 1]), probs(wires=[0, 2, 1])]
```

3. Operate on the 2-qubit state, then stack another `[[0, 0], [0, 0]]`
on the end of it (wire "1")
4. `StateMP(wires=[0, 1, 2]).process_state(state, wire_order=[0, 2, 1])`
transposes the result to the correct order

I also changed the torch tests to stop using a deprecated setter for
default float types.

**Benefits:**
Duplicate code is cleaned up, existing code is simplified, no
unnecessary call to transpose.

**Possible Drawbacks:**
- Have to call `qml.math.stack` for every wire that was not operated on.
Hopefully this is usually not a lot, and it's not that costly anyway
- functions now do less than they used to (I see this as a perk - they
now do _exactly_ what they're supposed to)

---
## [JoJoJet/bevy](https://github.com/JoJoJet/bevy)@[ab300d0ed9...](https://github.com/JoJoJet/bevy/commit/ab300d0ed9990972679629af3ef18fd37c0e106c)
#### Friday 2023-11-24 19:35:33 by Connor King

Gizmo Arrows (#10550)

## Objective

- Add an arrow gizmo as suggested by #9400 

## Solution

(excuse my Protomen music)


https://github.com/bevyengine/bevy/assets/14184826/192adf24-079f-4a4b-a17b-091e892974ec

Wasn't horribly hard when i remembered i can change coordinate systems
whenever I want. Gave them four tips (as suggested by @alice-i-cecile in
discord) instead of trying to decide what direction the tips should
point.

Made the tip length default to 1/10 of the arrow's length, which looked
good enough to me. Hard-coded the angle from the body to the tips to 45
degrees.

## Still TODO

- [x] actual doc comments
- [x] doctests
- [x] `ArrowBuilder.with_tip_length()`

---

## Changelog

- Added `gizmos.arrow()` and `gizmos.arrow_2d()`
- Added arrows to `2d_gizmos` and `3d_gizmos` examples

## Migration Guide

N/A

---------

Co-authored-by: Nicola Papale <nicopap@users.noreply.github.com>

---
## [moreginger/Zero-K](https://github.com/moreginger/Zero-K)@[b6ad432197...](https://github.com/moreginger/Zero-K/commit/b6ad43219720477632d6c1a3593922a794895379)
#### Friday 2023-11-24 20:25:56 by GoogleFrog

Followed "Fight your opponent, not the UI" through to removing manual groundcrash technique from Odin.
 * The micro involves waiting until Odin is flying over the target, then firing, for 800 or so extra damage.
 * Implemented via enforced minimum horizontal velocity.

The removal of the physics interaction and leverageable knowledge is sad, but probably for the best. Alternates might be:
 * Reduce shot range significantly, so it always groundcrashes. This would look a bit silly, and also be a pain because Odin would have to line up with its target perfectly.
 * Some sort of UI for selecting groundcrash - even worse.
 * Delve beyond "Fight your opponent, not the UI", but that doesn't seem warranted for a one-off mechanic.

With this in place it seems to be impossible to deal more than 8050 damage by shooting at Grizzly. However, there is even now still a technique that 1-shots it. But this technique is disrupted by prettymuch any unit bumping up against the Grizzly, although it will be possible to accidentally 1-shot your own Grizzly by dodging very slightly into the right spot for the technique.

---
## [kirankumar-2002/kirankumar-2002.github.io](https://github.com/kirankumar-2002/kirankumar-2002.github.io)@[e468f968f0...](https://github.com/kirankumar-2002/kirankumar-2002.github.io/commit/e468f968f0236de753907f72ac3a8cb20727ecf5)
#### Friday 2023-11-24 20:35:13 by kiran Kumar

Create README.md

Historical pages of the world encompass a vast and captivating collection of narratives that chronicle the rise and fall of civilizations, the triumphs and tragedies of humanity, and the enduring impact of individuals who have shaped the course of history. These pages are not merely records of the past; they are living testaments to the resilience of the human spirit, the enduring power of ideas, and the transformative potential of change.

Delving into the historical pages of the world is akin to embarking on a grand voyage through time, traversing the vast landscapes of human experience. From the ancient civilizations of Mesopotamia and Egypt to the tumultuous revolutions that reshaped Europe, from the groundbreaking discoveries of the Renaissance to the transformative movements of the 20th century, history provides a rich tapestry of interconnected stories that offer profound insights into the human condition.

Through the lens of history, we can trace the evolution of governance, from the despotic rule of monarchs to the rise of democratic ideals, and examine the enduring quest for justice and equality. We can witness the transformative power of innovation, from the invention of the wheel to the digital revolution, and marvel at the human capacity for creativity and ingenuity.

Historical pages also reveal the darker chapters of human history, the wars and conflicts that have caused untold suffering, the injustices and inequalities that have persisted across generations, and the stains of oppression and discrimination that continue to cast shadows on the present. These accounts serve as stark reminders of the fragility of peace and the importance of vigilance against the forces of tyranny and intolerance.

Yet, amidst the tales of conflict and oppression, history also illuminates the indomitable spirit of humanity. We witness the courage of individuals who dared to challenge the status quo, the resilience of communities that have weathered storms of adversity, and the unwavering pursuit of freedom and dignity that has driven countless movements for social change.

Exploring the historical pages of the world is not merely an exercise in intellectual curiosity; it is a profound journey of self-discovery and a vital step towards shaping a better future. By understanding the past, we gain a deeper appreciation for the present and a renewed sense of responsibility to shape a more just, equitable, and sustainable world for generations to come.

---
## [mahlemiut/wolfmame](https://github.com/mahlemiut/wolfmame)@[b17bd90268...](https://github.com/mahlemiut/wolfmame/commit/b17bd90268aa6b970b96efcfe4f52040434b000f)
#### Friday 2023-11-24 20:44:23 by wilbertpol

msx2_cart.xml: Added 31 items, 29 working. (#11642)

* msx2_cart.xml: Added 31 items, 29 working.

New working software list items
-------------------------------
Aleste (Woomb) [file-hunter]
Arkanoid 2 (Korea) [file-hunter]
Ashguine - Fukushuu no Honoo (Japan, alt 2) [file-hunter]
Daisenryaku MSX2 (Japan, alt) [file-hunter]
Gekitotsu Pennant Race 2 (Japan, sample) [file-hunter]
Hydlide 3 - The Space Memories (Woomb) [file-hunter]
Alien 8 Remake [file-hunter]
Los Amores de Brunilda (v1.01) [file-hunter]
Los Amores de Brunilda (v1.0) [file-hunter]
Barbarian the Duel [MSXdev]
Bomb Jack [file-hunter]
Bomb Jack (alt) [file-hunter]
Booming Boy (demo) [MSX Area]
Bubble Dream [MRC Tenliner Challenge]
DIM X (demo) [file-hunter]
Equivocal (v1.5) [Passion MSX2 Contest]
Equivocal (v1.0) [Passion MSX2 Contest]
Gold Fan [N.I]
Highway Fighter (demo) [file-hunter]
Inferno [msxdev Compo]
Jailbreak (v1.02) [Passion MSX2 Contest]
Jailbreak (alt) [Passion MSX2 Contest]
Jailbreak (alt 2) [Passion MSX2 Contest]
Knight Lore Remake [Retroworks]
Lilly's Saga - The Stones of Evergreen (v1.2) [MSXdev]
Lilly's Saga - The Stones of Evergreen (v1.1) [MSXdev]
Lilly's Saga - The Stones of Evergreen (v1.0) [MSXdev]
La Sorpresa (Spanish) [Oniric Factor]
A Surpresa (Portuguese) [Oniric Factor]

New NOT_WORKING software list additions
------------------------------------------
Ehagaki-yō wāpuro (Japan) [file-hunter]
Life on Earth (demo) [file-hunter]

* Fix capitalisations of Wāpuro and AshGuine

---
## [r8teful/OneSocket](https://github.com/r8teful/OneSocket)@[283385a577...](https://github.com/r8teful/OneSocket/commit/283385a5779e68516fe145443756c9d74033aaef)
#### Friday 2023-11-24 21:40:56 by r8teful

More Menu Changes

Oh My god I hate menus they are so enoying omg I hate it so much. The fade out is making everything so horrible to code why am I doing this to myself, there is still a glitch where you can spam the restart or main menu button in the pause screen and it will load several instances of the same scene and just softlock the game but eh who is going to notice it. Otherwise everything should be working fine I'll have a last bug check before releasing the demo but everthing should be about done woogit add .

---
## [evelynmitchell/gorilla](https://github.com/evelynmitchell/gorilla)@[f3ce849a8c...](https://github.com/evelynmitchell/gorilla/commit/f3ce849a8c46f5683477ff26ec34dc04518c294b)
#### Friday 2023-11-24 22:18:05 by Shishir Patil

Releasing Torch and TF weights 🚀  (#16)

In this PR we release the weights for Gorilla 0-shot model for Torch Hub
and Tensorflow Hub APIs 🎉

It chooses from 626 (exhaustive) TensorFlow v2 APIs, and 94 (exhaustive)
Torch Hub in a 0-shot fashion (without any retrieval). In the spirit of
being open, we do not filter, nor carry out any post processing either
to the prompt nor response 🎁 We would like to remind the community that
neither of `gorilla-7b-hf-v0`, `gorilla-7b-tf-v0`, nor
`gorilla-7b-th-v0` have any generic chat capability. We do have a model
with all the 1600+ APIs which also has generic chat capability, which we
release slowly to accommodate server demand.

You can play around with Gorilla either through our hosted colab (OpenAI
Chat completion API compliant) or you can download and run it locally.

Thank you for all the comments and suggestions so far! Keep them
coming!!!

🚀 🚀 🚀

---
## [bag-xml/WhatsFixer](https://github.com/bag-xml/WhatsFixer)@[6ee3374f89...](https://github.com/bag-xml/WhatsFixer/commit/6ee3374f89a13c622038c3ca15bdef7bc25e491b)
#### Friday 2023-11-24 22:37:46 by Daph357

FUCKING HELL FUCK YOU FUCK YOU FUCK YOU FUCK OU FUCK YOU

---
## [Offroaders123/NBTify](https://github.com/Offroaders123/NBTify)@[a839b086a8...](https://github.com/Offroaders123/NBTify/commit/a839b086a82058015b592ea226b20f39e84e32ef)
#### Friday 2023-11-24 22:57:16 by Offroaders123

Stricter SNBT + TS 5.3 + Node Deflate Raw

And I also started working on an initial experimental implementation for VarInt little endian encoding, but it wasn't working out correctly, so I'm holding that back to a later release, and I will try again at that point to reimplement it again. I think the challenge is understanding how the implementation works in regards to how it lines up with the NBT spec, and where VarInt is specifically used in the NBT implementation.

Oh, and I forgot to mention in the last commit that I made the change to the `Object.defineProperty()` calls for the `NBTData` fields because I wanted to more explicitly show how I want them to be non-writable, and I was just relying on the implicit behavior of having them be non-writable, which is what happens when you don't pass in the `writable` flag to `Object.defineProperty()`. I didn't add it originally because that was the default, so it made sense not to need to pass it. But after thinking about it, showing that it's moreso intended behavior by clarifying it in the config is more simple to see, rather than needing to read the docs like I did, to know that it does that implicitly.

In other words, with that and my TS variable and function return types, I want to start being more explicit once I know how I want things to work a certain way. It helps make things easier to catch unexpected changes down the road, because my pre-defined breakpoints show me where my intended behavior meets my unexpected changes, unlike having it bubble up to the nearest type check. That example is more in regards to return types, but yeah!

I want to try using more spaces in my code formatting too, for the longest time I have been used to doing no extra whitespace, not completely sure why. I think I was just used to that from the very early days, and I just kept that methodology around for a long time hehe. My opinionated formatting is what initially turned me off about Rust, since they have a very strict set of formatting rules, and I want to use Rust, so I want to get myself out of the habit of needing to use the syntax formatting that I personally like, and learn to like the other ways also, since I don't want that to hold back my learning and experience.

---
## [Bird-Lounge/Naakas-Lounge](https://github.com/Bird-Lounge/Naakas-Lounge)@[bf869a0ded...](https://github.com/Bird-Lounge/Naakas-Lounge/commit/bf869a0ded3a3ca5e00500ef5ad856bcb7f012dd)
#### Friday 2023-11-24 23:18:40 by Bloop

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
## [GerHobbelt/glfw](https://github.com/GerHobbelt/glfw)@[62dfbc74e4...](https://github.com/GerHobbelt/glfw/commit/62dfbc74e47b2e691a8a90f7a887f740746d016d)
#### Friday 2023-11-24 23:33:29 by Ger Hobbelt

making the bugger build in monolithic buil mode; the way we had to muck around to get the windows.h internally induced errors go away is a bit hacky to my taste, but so it always is once you start to use windows.h & friends for real, is my experience (for one: brittle in conjunction with OEMRESOURCE, but there's lots of buggers around that way; the whole APIENTRY hoobaloo is not worth any medals either. Jeez.)

---
## [mdohse29/mdohse29.github.io](https://github.com/mdohse29/mdohse29.github.io)@[492e7fa506...](https://github.com/mdohse29/mdohse29.github.io/commit/492e7fa5061b87bb74a816ecbcdc7a518d2d60dc)
#### Friday 2023-11-24 23:40:06 by mdohse29

Merge pull request #230 from mdohse29/dev

Fuck you Ryan

---

