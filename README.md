## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-25](docs/good-messages/2022/2022-12-25.md)


1,481,716 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,481,716 were push events containing 1,884,374 commit messages that amount to 97,419,155 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 32 messages:


## [Cheshify/tgstation](https://github.com/Cheshify/tgstation)@[176f7a0e42...](https://github.com/Cheshify/tgstation/commit/176f7a0e422b8417456e1ab65fa59e7ee88a16c5)
#### Sunday 2022-12-25 00:49:15 by san7890

Traitor UI only shows Unlock/Failsafe Code if you have it (#72114)

## About The Pull Request

There are cases in which you don't have an unlock code (if the uplink is
implanted in you from the start) and you obviously don't always start
with with a failsafe code (need to buy it). So, let's only fill in this
fields in the UI should they exist.

There might be something to be said about wanting to ensure that people
remember that they can check this UI screen to find the failsafe code
should they lose it later, and I wouldn't mind changing the string to be
something like "Failsafe: None" in that case. However, I just think that
keeping it as:

```txt
Code:
Failsafe:
```

is silly and should be changed somehow.
## Why It's Good For The Game


![image](https://user-images.githubusercontent.com/34697715/208604758-d7ff3ae9-e552-4dd2-998d-81715cd06ffc.png)

Note: That white box isn't part of the UI, that's a part of the edit I
did to the screenshot in the area where the stuff... isn't? What was i
thinking

I think the UI looks a lot cleaner for those cases when you just don't
have anything.
## Changelog
:cl:
qol: The Traitor's Antagonist Panel's Unlock and Failsafe entries will
only appear if there is an Unlock/Failsafe Code to display.
/:cl:

---
## [lizardqueenlexi/orbstation](https://github.com/lizardqueenlexi/orbstation)@[8cb4947084...](https://github.com/lizardqueenlexi/orbstation/commit/8cb4947084edffc9476c40ea6283b68e818f48bd)
#### Sunday 2022-12-25 01:07:02 by Jacquerel

AI actions won't unassign each other's movement targets & Mice stop being scared of people if fed cheese  (#72130)

## About The Pull Request

Fixes #72116 
I've had a persistent issue with basic mob actions reporting this error
and think I finally cracked it
When replanning with `AI_BEHAVIOR_CAN_PLAN_DURING_EXECUTION` it can run
`Setup` on one action leading to the plan changing, meaning that it runs
`finishCommand` to cancel all other existing commands
If you triggered a replan by setting up a movement action in the middle
of another movement action, cancelling the existing action would remove
the target already set by the current one.
We want actions to be able to remove _their own_ movement target but not
if it has been changed by something else in the intervening time.

I fixed this by passing a source every time you set a movement target
and adding a proc which only clears it if you are the source... but this
feels kind of ugly. I couldn't think of anything but if you have a
better idea let me know.

Also while I was doing this I turned it into a feature because I'm
crazy.
If you feed a mouse cheese by hand it will stop being scared of humans
and so will any other mice it attracts from eating more cheese. This is
mostly because I think industrial mouse farming to pass cargo bounties
is funny.
Mice controlled by a Regal Rat lose this behaviour and forget any past
loyalties they may have had.


https://user-images.githubusercontent.com/7483112/208779368-3bd1da0f-4191-4405-86e5-b55a58c2cd00.mp4

Oh also I removed a block about cancelling if you have another target
from the "hunt" behaviour, everywhere using this already achieves that
simply by ordering the actions in expected priority order and it was
messing with how I expected mice to work.
Now if they happen to stop by some cheese they will correctly stop
fleeing in order to eat it before continuing to run away.

## Why It's Good For The Game

Fixes a bug I kept running into.
Makes it possible to set up a mouse farm without them screaming
constantly.
Lets people more easily domesticate mice to support Ratatouille
gameplay.

## Changelog

:cl:
add: Mice who are fed cheese by hand will accept humans as friends, at
least until reminded otherwise by their rightful lord.
fix: Fixed a runtime preventing mice from acting correctly when trying
to flee and also eat cheese at the same time.
/:cl:

---
## [Salex08/tgstation](https://github.com/Salex08/tgstation)@[99537d0123...](https://github.com/Salex08/tgstation/commit/99537d0123167a07b242c33dad7c23ec9a5becef)
#### Sunday 2022-12-25 01:14:43 by LemonInTheDark

Fixes parallax on >2 level maps going fucky with optimized multiz (#72169)

## About The Pull Request

We no longer always render parallax.
This was causing issues because we can't isolate the white of space from
the vaugely white of everything else.

So instead, if your parallax plane is out of view, we'll not only
disable it, but we'll disable the strand we send from the main plane TO
it.

Instead only blending against the bottom stack.

This does mean there's a possibility for fullwhite on z transition
borders (potentially fixable), or when hijacking the plane (also
fixable, but significantly more annoying).

This is enough to make large maps functional though, so I'm happy with
it

## Why It's Good For The Game

Allows for #71731 and other maps like it. Makes my code actually work

## Changelog
:cl:
fix: Using optimized multiz on > 2 z layer maps will no longer cause
fucko bungo
/:cl:

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[5ad1289248...](https://github.com/TaleStation/TaleStation/commit/5ad12892483b47d706136c206b3c571895a56433)
#### Sunday 2022-12-25 01:34:28 by TaleStationBot

[MIRROR] [MDB IGNORE] converts contraband file into poster file, makes holiday posters work (kind of) (#3821)

* converts contraband file into poster file, makes holiday posters work (kind of) (#72131)

## About The Pull Request

The first part of this is just something that bothered me when I was
messing around with something that I will PR in the new year,
contraband.dm and dmi is ONLY posters. There's nothing else in there and
there are plenty of official posters, and if with #71717 we will also
add holiday posters to the mix then I think that its time to retire
contraband and make it poster.

Some small things I did while messing with it was change some variables
that were single letters into actual variable names, but overall this
part of the pr is not a player facing change.

That said, speaking of #71717 I think that it didn't work? Or didn't
work the way that it was supposed to? All of the spawned posters aren't
instances of festive posters, they are instances of normal posters, so
the code on initialize was not doing anything and the only reason the
holiday_none poster was showing up was because of the proc in randomize
spawning the posters in as those other posters. Because it didn't
actually _become_ poster/official/festive it never could do the proc
that turns it into a poster for the holiday that is actually occurring.

But then when I made it work and it turned into the generic posters I
decided that it would be better if instead of 30% of all posters being a
half finished mess, that if there wasn't a holiday poster it just
wouldn't replace them at all. I have poster Ideas and Dreams so I will
try to help with adding to more holiday posters but not in this PR.

What IS in this PR though, is a new traitor poster that appears during
the holidays.

![dreamseeker_MxxBzXIxiy](https://user-images.githubusercontent.com/116288367/208793262-9d4a45dc-f7bb-4208-b3c3-78cb68cf9af5.png)

This is a generic evil holiday poster that will replace normal evil
posters in the evil poster objective, because I agree with #72003 that
it should be a feature.

## Why It's Good For The Game

Contraband file is just posters already, this is easier for people to
find the posters.
I like holiday posters and think that we should have them and add more,
it is a fun easy thing to add to a lot of the microholidays to make them
more visible in addition to the name generation, but I don't want to see
the unfinished holiday poster so I do think that it's better to only
have them spawn if the holiday actually has a poster. Looking forward to
febuary!

## Changelog

:cl:
add: during holidays the spread syndicate propaganda through posters
objective has a chance of spawning evil holiday poster
fix: framework for holiday posters is more functional and modular
code: contraband.dm file and contraband.dmi file are both now poster.dm
and poster.dmi
/:cl:

* converts contraband file into poster file, makes holiday posters work (kind of)

Co-authored-by: Sol N <116288367+flowercuco@users.noreply.github.com>

---
## [nickyiliwang/neetcode](https://github.com/nickyiliwang/neetcode)@[d041ed0f79...](https://github.com/nickyiliwang/neetcode/commit/d041ed0f79e2aa0b71bca31ce0d5515803719661)
#### Sunday 2022-12-25 05:19:30 by nickyiliwang

HOLY FUCKING SHIT I JUST LEARNED HOW TO REVERSE A LINKED LIST, FUCK YOU LINKED LISTS HAHAHAHHAHAAHHAHHHHHHHHH

---
## [Mothblocks/tgstation](https://github.com/Mothblocks/tgstation)@[6dd4839ef3...](https://github.com/Mothblocks/tgstation/commit/6dd4839ef321aa0a997549d1ae07fe7ccbba59ed)
#### Sunday 2022-12-25 07:57:38 by carshalash

Gatfruit will no longer drop from ice portals. (#72048)

## About The Pull Request

For some god-forsaken reason, somebody decided that ice portals should
be able to drop one of the most disruptive items in the game. This PR
amends this by removing it from the drop pool.

## Why It's Good For The Game

In 2013 gatfruit was introduced in the following PR #2000 . This was
almost a decade ago at this point, repeatedly through the PR the creator
states his belief that this item should only ever be obtainable through
admin intervention due to its ridiculous capabilities. At the time
everyone in the PR agreed it was a reasonable item to add **as it was
unobtainable without admin intervention**. Over the years, it has crept
its way to become more prevalent and openly obtainable, the most
offensive of these options is the ice moon portal. As is, there is a 1
in 28 chance of obtaining the seeds, this sounds pretty inoffensive
right? That's just 3.44% probability. Now, let us search the instances
of the portal that spawns this.


![image](https://user-images.githubusercontent.com/16896032/208220173-bbefe604-0885-44a5-9add-b5f0c62067cc.png)

That is a big number, a lot of chances to get that seed packet and other
gamer looters. Now, let's take a look at the probability of being able
to get these seeds, assuming you wipe out all of the portals.


![image](https://user-images.githubusercontent.com/16896032/208220460-3f59a2ac-d936-4f3a-aa14-9c637af6a9d7.png)

92.8% chance to be able to get these seeds each shift if you focus
entirely on gaming the portals. That's a pretty insane probability of
being able to obtain the gatfruit seeds.

While I dislike people who sprint to the seed vault, there is at least
the possibility of a pod person telling them to fuck off when they
demand their _free_ gamer seed. There is also the fact that the ruin
isn't a guaranteed spawn every shift.

## Changelog

:cl:
balance: Gatfruit seeds will no longer drop from ice portals.
/:cl:

---
## [Mothblocks/tgstation](https://github.com/Mothblocks/tgstation)@[00e7d5d746...](https://github.com/Mothblocks/tgstation/commit/00e7d5d7465211ccf0e3d604e566e2c08775cd20)
#### Sunday 2022-12-25 07:57:38 by GoldenAlpharex

*hand, or That /One/ Emote You Always Felt Was Missing (#71600)

## About The Pull Request
It's happened to me _repeatedly_ that I'd see someone down on the floor,
and wanted to just, give them a hand, so they could take it and get up
that way, without just, directly clicking on them, since that's a little
bland. I've also wanted to just, offer my hand to someone so they could
grab it, so that I could pull them alongside me, rather than just
targeting one of their arms and ctrl-clicking them.

I've had this idea for a _long_ time, and only just decided to do this
today.

Now, I know what you might say. "Golden, that's a lot of code for
something this simple!" You're not wrong. _However_. I decided to go
along and to give some more love to the `/datum/status_effect/offering`
status effect and the offering-related alerts, to make them a lot more
versatile and a lot less hardcoded. Hence the whole "refactoring" part
of this.

Of course, when I add something, I don't do it half-way. So, the way the
emote works is much like the `*slap` emote, except that:

- When you click on someone, it does the exact same as if you were
offering the item to them, except that it's targeted (much like
ctrl-shift-click).
- If there's nobody directly adjacent to you, it won't do anything.
- If there's at least one person lying down around you, you will offer
them your help to get up. Should they take your hand and let you help
them up, you will both receive a simple memory about being helped up (or
helping up), as well as a 45-seconds-long small mood buff, because it
feels nice to be on either end of such a friendly gesture. If they get
up, they automatically get disqualified from being offered some help
standing up, and likewise, if you lie down, that offer goes away as
well.
- If there's at least one person around you, you will instead extend
your hand in their direction, for them to grab onto it. Should they do
so, you will then grab them by their arms and pull them.

I reworked the offering status effect to no longer have a hardcoded
`can_hold_items()` check, so that kisses and the hand offering would no
longer need you to have free hands to complete. The logic here is that
you can still pull someone even with both hands filled, so I figured I'd
leave it this way.

Note: If anyone would like to give the item a better sprite, by all
means, go ahead, that'd be amazing. I'm just not really a great spriter
and couldn't be bothered to waste hours making a very _meh_ hand.

## Why It's Good For The Game
It's fluff, and nice fluff at that. It makes it easier for people to be
nice to one-another without having to necessarily spend so long writing
up an emote that the person on the floor will already have gotten back
up. I'm sure the MRP folks will like it, and I'm certain the HRP
downstreams will love it too ;)

## Changelog

:cl:
add: Added the *hand emote, which you can offer to someone standing up
in order to give them the possibility to grab onto your hand and let you
drag them away, or to someone lying down to help them back up, which
always makes everyone involved a little happier!
refactor: De-hardcoded and genericized a lot of the offering status
effect and alert code, to make it require a lot less copy-paste to
handle new cases.
fix: Offering a kiss no longer requires the receiver to have free hands
to accept said kiss!
/:cl:

---
## [Mothblocks/tgstation](https://github.com/Mothblocks/tgstation)@[75439c71f2...](https://github.com/Mothblocks/tgstation/commit/75439c71f2282a3ae72b4ea35c80e27ca8556aaf)
#### Sunday 2022-12-25 07:57:38 by Mothblocks

Smoothing groups optimization, save 265ms with configs, more on production & w/ space ruins (#71989)

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

---
## [Stalkeros2/Skyrat-tg](https://github.com/Stalkeros2/Skyrat-tg)@[cd13fcdf46...](https://github.com/Stalkeros2/Skyrat-tg/commit/cd13fcdf467b1a9fe5d8fc5256552b0601284dca)
#### Sunday 2022-12-25 08:35:09 by Jolly

[MODULAR] contraband.dmi is no longer a hard override on posters (#18106)

* hhngh

* dunks this fucking dmi

* fuck you

---
## [AndrewTheSkid/Roblox-](https://github.com/AndrewTheSkid/Roblox-)@[e7a9189019...](https://github.com/AndrewTheSkid/Roblox-/commit/e7a9189019abb80603ad683252b7ff8af5f829b6)
#### Sunday 2022-12-25 10:08:07 by AndrewTheSkid

Update AnonymousPlayer

shortened time works better dont use any older versions they dont work as well anyways heres the final script! this took me 2 fuckin hours damn welp i might make another script soon! idk anyways bye guys and you dont know how much it means to me if you use it

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[0dd70b12e5...](https://github.com/Huffie56/cmss13/commit/0dd70b12e5142b3b0f14bf237765c1e643fe8a3f)
#### Sunday 2022-12-25 10:41:40 by Stan_Albatross

removes unused nanoui templates (#2012)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

none of these templates are used anywhere

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

fuck nanoui

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
del: Removed ten unused nanoui templates. Don't worry, they'll all be
going away soon.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Stan_Albatross <swt91a@gmail.com>

---
## [QuacksQ/Skyrat-tg](https://github.com/QuacksQ/Skyrat-tg)@[1c76ea5334...](https://github.com/QuacksQ/Skyrat-tg/commit/1c76ea533439dcd7fca15a2dd500a44dc6158883)
#### Sunday 2022-12-25 10:49:19 by SkyratBot

[MIRROR] Changes our map_format to SIDE_MAP [MDB IGNORE] (#18070)

* Changes our map_format to SIDE_MAP (#70162)

## About The Pull Request

This does nothing currently, but will allow me to test for layering
issues on LIVE, rather then in just wallening.
Oh also I'm packaging in a fix to one of my macros that I wrote wrong,
as a joke

[removes SEE_BLACKNESS usage, because we actually cannot use it
effectively](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

[c9a19dd](https://github.com/tgstation/tgstation/pull/70162/commits/c9a19dd7cce95038340ebd5c1a6e4cb27ee7c9ee)

Sidemap removes the ability to control it on a plane, so it basically
just means there's an uncontrollable black slate even if you have other
toggles set.

This just like, removes that, since it's silly

[fixes weird layering on solars and ai portraits. Pixel y was casuing
things to render below who
shouldn't](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[3885b9d](https://github.com/tgstation/tgstation/pull/70162/commits/3885b9d9ed634cdc4c8041b19df5b5ea9a1a37ae)

[Fixes flicker
issues](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

[2defc0a](https://github.com/tgstation/tgstation/pull/70162/commits/2defc0ad20a0ee7d12e0b071f6d31b6127b8765d)

Offsetting the vis_contents'd objects down physically, and then up
visually resolves the confliciting that was going on between the text
and its display.

This resolves the existing reported flickering issues

[fixes plated food not appearing in
world](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

[28a34c6](https://github.com/tgstation/tgstation/pull/70162/commits/28a34c64f830660d7fb1cc669b9fc3ed9f5c7d61)

pixel_y'd vis_contents strikes again. It's a tad hacky but we'll just
use pixel_z for this

[Adds wall and upper wall plane
masters](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

[89fe2b4](https://github.com/tgstation/tgstation/pull/70162/commits/89fe2b4eb40edc36879e4e1954dee8616be94522)

We use these + the floor and space planes to build a mask of all the
visible turfs.
Then we take that, stick it in a plane master, and mask the emissive
plane with it.

This solves the lighting fulldark screen object getting cut by emissives
Shifts some planes around to match this new layering. Also ensures we
only shift fullscreen objects if they don't object to it.

[compresses plane master
controllers](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

[bd64cc1](https://github.com/tgstation/tgstation/pull/70162/commits/bd64cc196a4265d42809eebbd1afa46fa33a576d)

we don't use them for much rn, but we might in future so I'm keeping it
as a convienince thing

:cl:
refactor: The logic of how we well, render things has changed. Make an
issue report if anything looks funky, particularly layers. PLEASE USE
YOUR EYES
/:cl:

Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>

* Changes our map_format to SIDE_MAP

* Modular!

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@ users.noreply.github.com>
Co-authored-by: Funce <funce.973@gmail.com>

---
## [Offroaders123/Librar.io](https://github.com/Offroaders123/Librar.io)@[f0abd731a8...](https://github.com/Offroaders123/Librar.io/commit/f0abd731a82fb85cc13576b26471a8fb0791ca44)
#### Sunday 2022-12-25 11:31:14 by Offroaders123

TSC Time! Part Two

Wow! That took some big brain magic to get fully typed-out. Found some wonky/missing type definitions for the File System Access API, and that kind of stumped me on a few problems for a while. But, in the end, I got it all done tonight!

This update simply adds type checking to the existing codebase, and adds some of the dev dependencies required to make that fully work. I also had to make a few changes to the code itself in a few spots, just to make the type definitions work like they should.

Learned a lot about my existing codebase from this! It's amazing what things it points out to you, considering I know that I built this, but am still learning how it works yet again XD

Had to use `// @ts-expect-error` in a few spots. Didn't know too much about that one, vs simply just `// @ts-ignore`, so I decided to look into it to see if I should use that one instead. This little article was neat for that :)
https://dev.to/oliverjumpertz/making-good-use-of-ts-expect-error-in-typescript-1f41

Also, found out how to semi-consistently get drag-and-drop to work on Ubuntu! It only works from the desktop (not Nautilus), and you also have to re-focus Chrome before you re-hover over it to place the item there. If you do both of those things, it works about 65% of the time, versus 0% XD

It looks like there's some type issues with the `new-javascript` type definitions, so the project isn't fully `tsc` compliant yet. None of my files have any issues within the editor though! That's much closer than before.

Merry Christmas!
Not sure why I'm up so late in the morning, working on this. I should go to bed! My Chromebook is at 5% too, so I'm squeezing this one in just in time, haha.

...and to all a goodnight! :)

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[001f46d372...](https://github.com/mrakgr/The-Spiral-Language/commit/001f46d372e221f117b01f83a6cefc09abeb2c97)
#### Sunday 2022-12-25 11:49:38 by Marko Grdinić

"10:45am. Still no answer. This was a full week already. I am washing my hands clear of UPMEM. I won't be checking the emails for answers from Adam Harries anymore or contacting him. I've sent him a message each on Saturday, Sunday, Monday and then Thrusday and Friday. The fact that I got zero involvement from him despite me doing the company a favor is a humiliation I'll hold a grudge for. I hate the type of person who pretends to have interest, but then loses it after less than 10m of work. What an asshole. There is no point in expecting anything else from him. Why did he even contact me?

I guess it happens that sometimes internet people will get in touch with the expectation of being felated. In his case, he is a compiler lead at UPMEM. Did he want my admiration for that? If so, that is pretty stupid of him. He must have been quite surprised that I just decided to do a backend as an exercise instead.

Forget it. I'll just complete the work and post it on HN. I won't even bother linking him to the finished product. Hopefully it impacts the company.

I've been thinking for the past few hours while I was in bed, and I've realized that when it comes to transfering arrays in Python - I have issuues. I do not actually know how to access the MRAM_HEAP_POINTER.

I am going to have to look at the library source to see if it is there. If not, I might have to switch to doing a C backend.

11am. But besides that I have another concern about the language. It has been bothering me for a while, but the enumerative pattern matcher I am using is really inefficient.

Suppose I match something like...

```spiral
match a,b with
| A, A => 0
| _ => 1
```

If the union type has maybe two unique cases, then this would not be too bad, it would result in only 3 cases being compiled: AA, AB and the rest. But if it had something like a 100, then this would result in 101 different cases being compiled!

I know if I did a bit extra work, I could group the cases and get the same outcome for either way.

11:10am. It would be a significant change to the compiler, but maybe I can justify it in anticipation of doing the genetic programming system. That thing is going to be doing a lot of AST splicing, so maybe it would be worth it.

11:30am. I am sorry, I am distracted. I keep thinking about the pattern matcher improvements, and the more I elaborate them the better they seem.

At first what I had to do felt complicated, but I am thinking about how I could do it and in fact it seems quite simple!

At first I thought about grouping them in the pattern compiler, but no. That would be really difficult.

Instead, what I should do is get rid of that needless PatUnbox. Istead of it enumerating anything, it should make a check for a single specific case.

If it is a hit then go into it. But in the else case, I'd do something special. In the CSE dictionary I'd add a pattern blocking tag, so that the partial evaluator remembers the failed cases. That way if it encounters the same check, it would know to go into the else branch automatically.

Moreover, that particular branch would be responsible for grouping the evaluated unions!

This way I could avoid doing the same thing in 3 different codegens.

It would be a large gain in compilation efficiency for patterns.

I am sure that F# is doing it like this. Doing it like Spiral does now would be ridiculous. So I should not fear about how F# is compiling its own patterns.

11:40am. Sigh. I've been thinking about it, and programming like this is really meaningful. I am learning a lot about programming through work on a language. But when I studied ML, I basically learned nothing. The only things of value were those tabular RL and CFR algorithms.

If others can win the Singularity race through cultivating pure ML, then I give up. You can come and kill me after you've ascended. I tried it, and I just can't do it. I tried really hard and couldn't learn a thing.

Somebody at my level of intelligence really needs the machine itself to help him. Functional programming is the most I can do.

11:45am. Today my plan was to make the scalar map, but it is going to be just like ref counting it seems. I feel like making a segue and taking a look at pattern compilation once more first.

Yeah, forget the backend. The HN crowd is not going to look down on me for having it take extra time.

11:50am. Let me take a look at PatUnbox.

```py
PatUnbox(r,PatPair(r,PatSymbol(r,a),b))
```

So this is how I compile it. Nasty. Unions should be proper unions.

11:55am. Ok, before I dive into this let me chill a little. I should also make some tests for pattern matching ahead of time and compile them with the current inefficient matcher.

...Hmmm, I am going to have to extend the partial evaluator. I am actually not going to be able to reuse the CSE dictionary...

Actually, maybe I would be...

Yeah, I should be, I should be. It is fine. The way CSE rewriting is that it takes an OP and a list of Data. I won't need to check a set, I can just check whether the variable is blocked for a particular symbol.

12:05pm. Let me chill here. A new Satanophany translated chapter is out. I am also behind on Destiny Unchained Online raws.

Let me have some fun and then I will dive in.

12:40pm.

```spiral
// Is the following pattern being compiled efficiently?

union qwe = A | B | C | D | E

inl main () =
    match dyn (A, B) with
    | A, A => 0i32
    | _ => 1i32
```

```py
kernels = {
}
from dpu import DpuSet
import numpy as np
from dataclasses import dataclass
from typing import NamedTuple, Union, Callable, Tuple
i8 = i16 = i32 = i64 = u8 = u16 = u32 = u64 = int; f32 = f64 = float; char = string = str

class US0_0(NamedTuple): # A
    tag = 0
class US0_1(NamedTuple): # B
    tag = 1
class US0_2(NamedTuple): # C
    tag = 2
class US0_3(NamedTuple): # D
    tag = 3
class US0_4(NamedTuple): # E
    tag = 4
US0 = Union[US0_0, US0_1, US0_2, US0_3, US0_4]
def main():
    v0 = US0_0()
    v1 = US0_1()
    match v0:
        case US0_0(): # A
            del v0
            match v1:
                case US0_0(): # A
                    del v1
                    return 0
                case US0_1(): # B
                    del v1
                    return 1
                case US0_2(): # C
                    del v1
                    return 1
                case US0_3(): # D
                    del v1
                    return 1
                case US0_4(): # E
                    del v1
                    return 1
        case US0_1(): # B
            del v0, v1
            return 1
        case US0_2(): # C
            del v0, v1
            return 1
        case US0_3(): # D
            del v0, v1
            return 1
        case US0_4(): # E
            del v0, v1
            return 1

if __name__ == '__main__': print(main())
```

This is the kind of inefficient compilation that I am worried about.

12:45pm. Let me have breakfast and chores here. I should be able to finish it all in one day. It is no problem."

---
## [brucerennie/muforth](https://github.com/brucerennie/muforth)@[5043786e38...](https://github.com/brucerennie/muforth/commit/5043786e38d776d6dd38df152ac026b0a07a56e3)
#### Sunday 2022-12-25 13:30:12 by David Frech

[arm] O frabjous day! Working USB firmware for STM32F303/F072!!!!!

Late last night I realized that I the "variable" defining word was
wrong, and wouldn't work for code compiled into flash.

I fixed it, re-compiled the USB test code, and it immediately worked!

This is after trying over and over to get it to work, and basically
giving up on ST and the STM32. It turned out to be a stupid simple
mistake on my part.

I've made a few small changes to the USB code, including commenting out
the possibly offensive "manufacturer string" and replacing it with
something banal.

I've also made the USB code the "out of the box" code that the STM32F072
Discovery and F3 Discovery board files load.

You too can try this at home!

  ./muforth -f target/ARM/board/stm32f072b-discovery.mu4

OR

  ./muforth -f target/ARM/board/stm32f3-discovery.mu4

then

  jtag
  flash-image
  verify

Reset the board, plug into the "user USB" jack, and watch your favorite
OS enumerate the board. I've had success with Linux and Windows 10.

Pressing the reset switch will disconnect from the USB, and the board
will re-enumerate.

It doesn't do anything more than that, but the hard part was getting to
this point. Adding code to process vendor requests to turn it into a
chat target is pretty easy.

Super exciting!!!!

---
## [Tangerineje/PsychonautStation](https://github.com/Tangerineje/PsychonautStation)@[a3e7c70f6d...](https://github.com/Tangerineje/PsychonautStation/commit/a3e7c70f6da0fc7ea9929ddb39beddcf3113707f)
#### Sunday 2022-12-25 13:35:00 by necromanceranne

Bodypart code cleanup, robotic limbs can actually be disabled through damage again. (#71739)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Cleans up various variables and code comments in bodypart code so that
it is easier to understand (hopefully) what the fuck is happening there.

Fixes a hilarious oversight. For what may have been an entire 2 year
span, robotic limbs were unable to be disabled whatsoever. Good stuff.

## Why It's Good For The Game

Lost all your limbs and now have only surplus prosthetics?
Congratulations! You're now more durable than even someone with proper
robotic limbs, as your arms do not contribute anything more than 10
damage (or 15 stamina) to your overall damage taken. Furthermore, taking
the maximum amount of damage is actually entirely meaningless to you.

Laugh as someone attempting to shoot your arms does almost no meaningful
damage once you hit the cap! It's all sunk cost! You can't have it blown
off anyway, because dismembering surplus limbs is gone!

Who knew getting into a horrible bluespace/goliath accident could have
such an impact on your combat prowess. Thanks Nanotrasen!

Anyway, these vars are ugly.

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
code: Makes a lot of the bodypart variables clearer as to what they do.
Includes more detailed code comments.
fix: Robotic limbs are no longer immune to being disabled through
reaching maximum damage.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [pitpo/aoc22](https://github.com/pitpo/aoc22)@[faf9a0b89b...](https://github.com/pitpo/aoc22/commit/faf9a0b89bea97ea36ae3c31a44d03845a110847)
#### Sunday 2022-12-25 13:39:51 by Piotr Gabrielski

Add Day 22 part 2 (non-generic) solution

Holy shit, this one is a story to remember
This was meant to be a generic solution (and can be very easily made
into one!), but I'm out of energy and time for philosophical Paint
drawings.
I'm super happy it works for both my input and example input.
To support more grids, the rest of cases has to be added to dissect_cube
function. Maybe someday (haha)

---
## [rhumounet/adventofcode2K22](https://github.com/rhumounet/adventofcode2K22)@[c71c807987...](https://github.com/rhumounet/adventofcode2K22/commit/c71c807987ae5bdf591b44cb36a501ba48c5673f)
#### Sunday 2022-12-25 13:46:12 by rhumounet

Day 17, part2, you did 2000, now do 1000000000000000 BECAUSE FUCK YOU

---
## [orouz/kibana](https://github.com/orouz/kibana)@[afb09ccf8a...](https://github.com/orouz/kibana/commit/afb09ccf8a61d610e8e3d8beb2c80f413f1b33c5)
#### Sunday 2022-12-25 16:41:38 by Spencer

Transpile packages on demand, validate all TS projects (#146212)

## Dearest Reviewers 👋 

I've been working on this branch with @mistic and @tylersmalley and
we're really confident in these changes. Additionally, this changes code
in nearly every package in the repo so we don't plan to wait for reviews
to get in before merging this. If you'd like to have a concern
addressed, please feel free to leave a review, but assuming that nobody
raises a blocker in the next 24 hours we plan to merge this EOD pacific
tomorrow, 12/22.

We'll be paying close attention to any issues this causes after merging
and work on getting those fixed ASAP. 🚀

---

The operations team is not confident that we'll have the time to achieve
what we originally set out to accomplish by moving to Bazel with the
time and resources we have available. We have also bought ourselves some
headroom with improvements to babel-register, optimizer caching, and
typescript project structure.

In order to make sure we deliver packages as quickly as possible (many
teams really want them), with a usable and familiar developer
experience, this PR removes Bazel for building packages in favor of
using the same JIT transpilation we use for plugins.

Additionally, packages now use `kbn_references` (again, just copying the
dx from plugins to packages).

Because of the complex relationships between packages/plugins and in
order to prepare ourselves for automatic dependency detection tools we
plan to use in the future, this PR also introduces a "TS Project Linter"
which will validate that every tsconfig.json file meets a few
requirements:

1. the chain of base config files extended by each config includes
`tsconfig.base.json` and not `tsconfig.json`
1. the `include` config is used, and not `files`
2. the `exclude` config includes `target/**/*`
3. the `outDir` compiler option is specified as `target/types`
1. none of these compiler options are specified: `declaration`,
`declarationMap`, `emitDeclarationOnly`, `skipLibCheck`, `target`,
`paths`

4. all references to other packages/plugins use their pkg id, ie:
	
	```js
    // valid
    {
      "kbn_references": ["@kbn/core"]
    }
    // not valid
    {
      "kbn_references": [{ "path": "../../../src/core/tsconfig.json" }]
    }
    ```

5. only packages/plugins which are imported somewhere in the ts code are
listed in `kbn_references`

This linter is not only validating all of the tsconfig.json files, but
it also will fix these config files to deal with just about any
violation that can be produced. Just run `node scripts/ts_project_linter
--fix` locally to apply these fixes, or let CI take care of
automatically fixing things and pushing the changes to your PR.

> **Example:** [`64e93e5`
(#146212)](https://github.com/elastic/kibana/pull/146212/commits/64e93e580679dd55f4fdf19bd01402bc478a1a75)
When I merged main into my PR it included a change which removed the
`@kbn/core-injected-metadata-browser` package. After resolving the
conflicts I missed a few tsconfig files which included references to the
now removed package. The TS Project Linter identified that these
references were removed from the code and pushed a change to the PR to
remove them from the tsconfig.json files.

## No bazel? Does that mean no packages??
Nope! We're still doing packages but we're pretty sure now that we won't
be using Bazel to accomplish the 'distributed caching' and 'change-based
tasks' portions of the packages project.

This PR actually makes packages much easier to work with and will be
followed up with the bundling benefits described by the original
packages RFC. Then we'll work on documentation and advocacy for using
packages for any and all new code.

We're pretty confident that implementing distributed caching and
change-based tasks will be necessary in the future, but because of
recent improvements in the repo we think we can live without them for
**at least** a year.

## Wait, there are still BUILD.bazel files in the repo
Yes, there are still three webpack bundles which are built by Bazel: the
`@kbn/ui-shared-deps-npm` DLL, `@kbn/ui-shared-deps-src` externals, and
the `@kbn/monaco` workers. These three webpack bundles are still created
during bootstrap and remotely cached using bazel. The next phase of this
project is to figure out how to get the package bundling features
described in the RFC with the current optimizer, and we expect these
bundles to go away then. Until then any package that is used in those
three bundles still needs to have a BUILD.bazel file so that they can be
referenced by the remaining webpack builds.

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [FelixSiegel/J-I-B](https://github.com/FelixSiegel/J-I-B)@[0fa4aa72f5...](https://github.com/FelixSiegel/J-I-B/commit/0fa4aa72f5a80fa0b4886fe5eb75eae319ec7543)
#### Sunday 2022-12-25 16:57:45 by jumpie700

hate my life why are the ignored ones in the list?

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[879d605afa...](https://github.com/mrakgr/The-Spiral-Language/commit/879d605afaf115a0672d7ac256de7b418b4ed1b9)
#### Sunday 2022-12-25 18:21:48 by Marko Grdinić

"```py
            v9 = v0.tag
```

Ah, whops, I forgot about this in UnionTag.

```fs
        | EOp(_,UnionTag,[a]) ->
            let eval k (h : Union) = h.Item.tags.[k] |> LitInt32 |> DLit
            match term s a with
            | DNominal(DV(L(_,YUnion h) & v) & a, _) ->
                match Map.tryFind v s.unions with
                | Some (UnionData (k,_)) -> eval k h
                | _ -> push_op_no_rewrite s UnionTag a (YPrim Int32T)
            | DNominal(DUnion(DPair(DSymbol k,_),h), _) -> eval k h
            | a -> raise_type_error s <| sprintf "Expected an union.\nGot: %s" (show_data a)
```

Is it really good that I am pushing this without rewriting.

```fs
        | EOp(r,UnionUntag,[EType(_,t);a;on_succ;on_fail]) ->
            let t = ty s t
            match nominal_apply s t with
            | YUnion h ->
                let h = h.Item
                let on_succ, on_fail = term s on_succ, term s on_fail
```

Ah, I remember why this thing has a fail case. Just in case the serialization is done on cruddy data.

7pm. Done with lunch.

```fs
        | EOp(r,UnionUntag,[EType(_,t);a;on_succ;on_fail]) ->
            let t = ty s t
            match nominal_apply s t with
            | YUnion h ->
                let h = h.Item
                let on_succ, on_fail = term s on_succ, term s on_fail
                let lit i =
                    if 0 <= i && i < h.tag_cases.Length then
                        let k,v = h.tag_cases.[i]
                        type_apply s (apply s (on_succ, DSymbol k)) v
                    else raise_type_error s <| sprintf "Invalid tag %i." i
                match term s a with
                | DV(L(i,YPrim Int32T) as tyv) as a ->
                    let key = TyOp(UnionTag,[a])
                    match cse_tryfind s key with
                    | Some(DLit(LitInt32 i)) -> lit i
                    | Some _ -> failwith "Compiler error: Expected an 32-bit int."
                    | None ->
                        let on_fail, on_fail_ty =
                            let s = {s with cse = Dictionary(HashIdentity.Structural) :: s.cse; seq = ResizeArray()}
                            let r = apply s (on_fail, DB) |> dyn false s
                            seq_apply s r, data_to_ty s r
                        let on_succ =
                            Array.mapi (fun i (k,v) ->
                                let cse = Dictionary()
                                cse.Add(key,DLit(LitInt32 i))
                                let s = {s with cse = cse :: s.cse; seq = ResizeArray()}
                                let r = type_apply s (apply s (on_succ, DSymbol k)) v |> dyn false s
                                let r_ty = data_to_ty s r
                                if on_fail_ty <> r_ty then raise_type_error s <| sprintf "Return type of the success case does not match the failure one.\nGot: %s\nExpected: %s" (show_ty r_ty) (show_ty on_fail_ty)
                                seq_apply s r
                                ) h.tag_cases
                        push_typedop_no_rewrite s (TyIntSwitch(tyv,on_succ,on_fail)) on_fail_ty
                | DLit(LitInt32 i) -> lit i
                | a -> raise_type_error s <| sprintf "Expected an i32.\nGot: %s" (show_data a)
            | _ -> raise_type_error s <| sprintf "Expected an union type.\nGot: %s" (show_ty t)
```

These `lit i` returns are bonkers. They make zero sense. I am really putting in overtime right now.

```fs
                let lit i =
                    if 0 <= i && i < h.tag_cases.Length then
                        let k,v = h.tag_cases.[i]
                        type_apply s (apply s (on_succ, DSymbol k)) v
                    else raise_type_error s <| sprintf "Invalid tag %i." i
```

Ah, wait it does make sense. I thought it was returning a literal literal.

At 7pm, my ability to pay attention is reduced.

```fs
let key = TyOp(UnionUntag,[a])
```

Let me change the key to this. Why did I pick `UnionTag`?

```fs
let cse = Dictionary(HashIdentity.Structural)
```

Let me also just add the `HashIdentity.Structural`.

```fs
else raise_type_error s $"Invalid tag 0 <= {i} < {h.tag_cases.Length} in UnionUntag."
```

Let me also improve the error a bit.

```fs
        | EOp(_,UnionTag,[a]) ->
            let eval k (h : Union) = h.Item.tags.[k] |> LitInt32 |> DLit
            match term s a with
            | DNominal(DV(L(_,YUnion h) & v) & a, _) ->
                match Map.tryFind v s.unions with
                | Some (UnionData (k,_)) -> eval k h
                | _ -> push_op s UnionTag a (YPrim Int32T)
            | DNominal(DUnion(DPair(DSymbol k,_),h), _) -> eval k h
            | a -> raise_type_error s <| sprintf "Expected an union.\nGot: %s" (show_data a)
```

Also it should totally be possible to CSE this particular op.

7:10pm. Ok, let me try the `serializaion4` test again.

7:15pm. Yeah, now it is the same as before.

Good. I am done for the day.

I really can't go on anymore. Today I really made a huge contribution to Spiral.

The pattern matcher is the most important, but I also changed the way backend join point returns work as well as changed the other case in Python to `_`. I also made the UnionTag CSE-sable.

7:20pm. I'll push out a new version once I am done with work on the UPMEM backend. This should be in a few days.

No way am I going to be doing any writing today."

---
## [Koi-3088/ForkBot.NET](https://github.com/Koi-3088/ForkBot.NET)@[45f33907f1...](https://github.com/Koi-3088/ForkBot.NET/commit/45f33907f148021d7f17f0d11f7af50ce4639708)
#### Sunday 2022-12-25 18:31:46 by Koi

Mr. Mime is a thing, unfortunately.
Mild clean, some more Cherish set handling attempts.
Exclude set MetDate from mystery gifts.
Fix daycare enum parsing.
Check for no result in case $qc was used or some other weird thing happens.
Remove FixOT and TradeCord as routine types (FlexTrade handles both).
Try to apply trainer info for Mystery gifts.
Re-add fixed met date if not GO origin.
Update DenBot distribution data, minor fixes.
Fix Yamask-Galar in daycare, some more oopsies.
-Add DenBot - a seed lookup and day skipper bot for raids.
-Change AutoRoll's behavior to make use of some of DenBot's functionality.
Minor clean.
Revise TradeCord "traded" check, remove potential user path straggler entries because paranoia, some minor fixes.
TradeCord fixes (shocker, I know).
Extract Json serializer.
Minor clean and fixes.
Minor fixes.
Fix Milcery when an Alcremie variant is a parent.
Update to latest Core and ALM dependencies.
Handle non-shiny events in a better way.
Work around a race condition?
Simplify and de-bugify trade completion check.
Fix indexing, improve chance for Melmetal-Gmax because it's nigh impossible to get.
Rework TradeCord internals, add new functionality:
-Migrate user data from ".txt" files to a serialized Json (migration for a large amount of users will take a few minutes, be patient).
-Make TradeCord configurable, add its own settings category.
-Add some template events with an optional end timer (YYYY/MM/DD 8PM as an example, though any local time format should work).
-Add barebones Pokedex (counter, flavor text).
-Can check dex completion by typing `$dex`, check missing entries by typing `$dex missing`.
-Completing the Pokedex will slightly improve shiny rate.
-Can now mass release cherish event Pokemon and shinies ($massrelease shiny/cherish).
-Various tweaks, improvements, and bugfixes.

Slightly change FixOT's behavior:
-If a shown Pokemon is illegal and an event, attempt to find a match within the MGDB first.
-Try to force users to trade away the shown Pokemon, log attempt to change shown Pokemon.
Add consideration for easter eggs being enabled in settings, fix Suicune
Change species rng for TradeCord, some bugfixes (I really need to rewrite this mess)
Add check if we're using ListUtil for Giveaway instead of TradeCord.
Amend commit since I'm squashing and force-pushing while bringing the fork in line with the main branch
Add Giveaway module to Discord bot (#22)

Thanks, rigrassm.
Co-authored-by: Koi-3088 <61223145+Koi-3088@users.noreply.github.com>
Specify USB port instead of adding the first result (can be found via Device Manager).
Re-add boolean check because we don't want to fix everything
FixOT will attempt to regenerate illegal Pokémon.
Apply trash bytes for reasons.
Minor TradeCord fixes and adjustments.
Minor clean for C#9
Use "GetValidPreEvolutions()" instead of "GetPreEvolutions()".
Index forms correctly.
Fix the fixed and re-introduced empty daycare index error.
*an* Ultra Ball.
Add EvoTree breeding for TradeCord.
Remove unnecessary value declarations for pinging on encounter match.
Mildly beautify EncounterBot mark output.
Integrate Anubis' system update prevention into Soft Reset and Regigigas Encounter Modes.
Rename "Regi" Encounter Mode to "Soft Reset".
Speed up "A" clicks for Regigigas and Soft Reset modes.
Add Mark logging output for EncounterBot.
Fix oops (re-order logic, remove unnecessary lines).
Add optional species and form specification for $massrelease
Use an obscure string splitter because people like symbols in their names.
Fix things that broke after rebasing to the latest main repo commit.
Use a less unfortunate field name and value splitter...again.
Fix Marowak-Alola always generating as an NPC trade.
Add filters for "$list <species>" to narrow down results.
Fix Cherish Pichu and Octillery
Stop making dumb mistakes, me (implying the rest of it isn't a dumb mistake).
Can't breed antiques.
Use a less unfortunate embed name and value splitter
Add Melmetal-Gmax to TradeCord.
Add ability to search by caught ball.
Have MassRelease ignore events.
Add specific regional form breeding.
Revise egg rate and egg shiny chance.
Have trade evolutions hold an Everstone.
Add an extra right click when navigating to settings for AutoRoll.
Add reworked encounter/egg/fossil logs.
Minor clean.
Minor clean.
Get rid of EncounterBot, FossilBot, EggFetch text logs until I properly rework them.
Break on an empty page due to aggressive rounding
Add multi-page lists for Tradecord.
More random bugfixes.
Fix some bugs before major clean
Add Language parameter for TradeCord.
Change trainer info input format for TradeCord.
Move focus on Showdown set instead of randomizing a pkm file.
Allow user to enter whatever they want for $list, handle edge cases like Kommo-o
Add "$list all" to show non-duplicate caught species.
Automatically remove from favorites if trading or gifting (small QOL thing).
Change how favorites are removed from user file.
Revert base egg shiny chance nerf.
Fix daycare
Add favorites command to TradeCord.
Slightly nerf eggs.
Fix TradeCord list for shinies
Add TradeCord (my dumbest and messiest project so far, Archit pls don't hate the mess).
Add Showdown output for Star/Square shinies and OTGender.
Add optional link code input for FixOT.
Change how OTName, TID, SID is displayed.
Add Regigigas SR bot.
Add SoJ Camp SR bot.
Ribbons now work with EggTrade (remove ribbons if egg).
Remove EggRoll.
Add another filter for FixOT
Fix.. FixOT
Update offsets for EncounterBot catching.
Slightly change StrongSpawn to work with Regi SR and make it its own mode.
Make SpinTrade only available for USB-Botbase
Update valid eggs for CT
winforms: resize icon.ico to fix crash at startup on unix using mono
Rework Spin, read initial in-game coordinates in order to correct drift
Add TID, SID, Language output for Showdown
Remove obsolete OT and Language parsing
Very minor clean until I have time for a proper one.
Detach controller when stopping USB bot.
Actually set LastUsedBall for EncounterBot (missed when bringing in line with main repo)
Move extra RaidBot timings following the official commit
Remove PKHeX Discord invite from Readme.md

Maybe fewer people will pester devs now about my unofficial fork?
Update for latest main repo EncounterBot commits.
Update README.md
Add back best commit: Red's SpinTrade.
Add egg trades, foreign Dittos and OT for Twitch.
If ItemMule is enabled, also display the item a user is receiving.
Add periodic time sync toggle for all methods of hosting (except for non-soft locked AutoRoll) to (hopefully) prevent den rollover during extended hosts.

Add routine to exit a lobby for SoftLock if no players are ready in time (to preserve soft lock).

Add a routine to recover from disbanded lobbies (when someone disconnects unexpectedly) for SoftLock.

Add a routine to restart game if all else fails and we're stuck in a raid.

Add a routine for adding and deleting friends if we're soft locked and raids go empty.

Slightly reorganize settings, extract methods, minor clean.
Don't use such a generic file name for stream assets.
Check USB port index for running bots. Should fix adding additional USB bots when no config is saved.
Add fixed met date for FixOT.
How do I boolean
Change airplane mode logic, tweak timings and routine for soft lock lobby exit
Rework EggRoll cooldown (static list in favor of a txt file).
Start clean up and refactor
Add setting to increase delay after pressing "Home" after a date skip.
Use USB port index for blocking and sprite pngs if connection type is USB
Add option for airplane host (usb-botbase required)
Add option to softlock on selected species for AutoRoll
Add automatic compatibility for all console languages when date skipping (have to set ConsoleLanguage under ScreenDetection)
Attempt to fix multiple USB device add and connect...again
Minor clean
Fix oops?
Handle add/remove of bots
Distinguish between multiple USB devices, tweak BotRemoteControl for USB, other various fixes
Add SpA modifier for foreign Dittos
Add alpha USB-Botbase support
Fix DateTime parsing for European format for EggRoll
Set fixed EggMetDate and MetDate for EggRoll
More FixOT filters
Remove Beheeyem. Oops.
Split EggRoll into its own routine and trade type, only output "Receiving: Mysterious Egg" if routine is EggRoll, other minor tweaks and fixes
Make FixOT its own queue with roles and counts
Add a couple more OTs to $fix
Parsing for EggRaffle auto-clear and $clearcooldown
Adjust timings and split Watt collecting clicks for AutoRoll
Fix oops with file attachments for Ditto
Further improvements for OT, memes for invalid pokemon (disable EasterEggs)
Add spaces, digits for OT
Randomize memes, cut down bloat
Fix miscellaneous bots after Anubis' recent QOL additions
-Ignore events for OT because headache.
-Add overlooked "$convert <generation>" input for OT.
-Move $clearcooldown to SudoModule
-Clear timer automatically if NoTrainerFound
-More reliable Dittos
-Foreign Dittos for $convert
-Command to clear cooldown for EggRaffle in case trade gets disconnected
-Fix "Trade finished" line to keep result secret
-EggRaffle as a toggle, option to specify channels
-Seed Check output to both DMs and Channel (apparently some want it)
-Randomly generated egg raffle via a "$roll" command with a configurable cooldown
-FixAdOT reworked, has its own command "$fix" and no longer overrides $clone
-Ball: <value> output for Showdown sets
-Fix oversight
-Option to output Seed Check results to Discord channel with a User mention
-Showdown set output for OT name and eggs
-Basic "OT: <name>" option without Showdown set output
-Initial $convert support for EggTrade
-Egg moves for EggTrade test attempt
-Minor update
-EggTrade (by nicknaming a Pokémon "Egg" using $trade)
-Failsafe for memes if enabled but field left blank or incomplete
-Niche breedable Ditto trade mode.
Add minimize button
EggFetch text logs
StrongSpawn mode for EncounterBot
Re-add EncounterBot Master Ball catching
More parsing for FixAdOTs
Park Ball as held item instead of string
Actually remove the offset instead of saying I did
Initial DLC commit
Faster code entry
Removed catching for EncounterBot (need a new offset)
CloneBot mode to fix Nickname and OT if adverts detected

---
## [i3roly/CMI8788](https://github.com/i3roly/CMI8788)@[24591bbe82...](https://github.com/i3roly/CMI8788/commit/24591bbe821996f2fc57997a8b04c40b0b807028)
#### Sunday 2022-12-25 19:34:31 by gagan sidhu

save controls+getting position, everything actually looks surprisingly good. tim cook equals 'full <you know what>'

my gut tells me it "feels good" because now disabling the main interrupt doesn't immediately crash the system.
	-seems like i'm handling the interrupts at the hardware level in APPUL's operating system properly now.

still have the following issues:
- lingering PCIAudioDevice object that prevents full unloading (PCI driver, so this may not be feasible).
- unsolved control mysteries, and
- the conundrum of getting the current sample position on a device with two clocks (one for SPDIF and one for everything else, where the latter can sample at different periods)

but it looks good.

since when did oprah's fixation with stock price (along with the other talentless hacks piled in and holding a shitton of APPUL) supersede the number one rule?
	"DON'T FUCK WITH THE OPERATING SYSTEM."

remember people, suspender-slapping, generic-looking, ecosystem-destroying, fat bitch(oprah)-enriching TIM COOK WENT 'FULL <YOU KNOW WHAT> '

https://www.youtube.com/watch?v=X6WHBO_Qc-Q

I LOVE U BEN.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[47ec8ecd38...](https://github.com/tgstation/tgstation/commit/47ec8ecd386f028ee8b2697412c89f00c9cd139f)
#### Sunday 2022-12-25 20:47:31 by Rhials

Adds the Sandstorm random event, directional meteor functionality, space sand. (#71802)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request


![sandstorm](https://user-images.githubusercontent.com/28870487/206070641-80d37afc-a365-4f5e-ad48-e8cdf0153ac9.png)

Hey guys, it's your boy. Back at it again with another meteor-adjacent
event PR.

Adds the Sandstorm random event, inspired by the long-unused admin only
one. It picks a direction to approach from, alerts the crew of its
imminent arrival, and after a little over a minute of preparatory time,
sends waves of sand and dust to grind down everything in that direction.

To accomplish this, some minor adjustments had to be made to meteor
generation code. They can now be passed an optional arg for a direction
to be thrown from, and will pick a random one if no direction is given.

Also introduces the newest addition to our cast of meteors -- space
sand! It's even weaker than space dust, and shows up exclusively in this
event. Space sand is **ineffective against rwalls**, and will not damage
the arrivals area's high-tech sand-resistant glass. This is to prevent
this event from venting one of the most dust-vulnerable areas on the
station, and to make sure new players aren't shafted into firelock hell
when the right angle is picked.

I did a lot of testing and tweaking of numbers to get the damage to
average at about the level I'm comfortable with. This is meant to be a
high-impact event that isn't as destructive (or unavoidable) as a meteor
wave. Speaking of avoidance, let's talk about mitigation:

You get an early warning and a direction the sand will come from. You
have time to grab repair supplies, move to safety, get a MODsuit. You
can make worthwhile repairs as the sand comes in from inside (or
outside, if you're brave enough) with nothing more than a welder and
iron sheets. If you're feeling particularly spicy, you can leverage your
prep time setting up shield generators, which spawn in engineering and
have been added to the maintenance machines loot pool. Anyone can
contribute, so do your part as a good crewmate and help out!

All that being said, the event can't be prevented entirely. Shit's going
to get shredded, especially on the outside of the station. Damage will
vary heavily based on the station and direction, ranging from
inconsequential to threatening. It should happen late enough into the
round that, at the bare minimum, the crew shouldn't be caught
unprepared.

For those of you who are worried, the ORIGINAL sandstorm admin event is
still with us too. It's been moved from the space dust file into the
Sandstorm event file. This PR also makes a very minor change to the
naming of the space _dust_ events, for better menuing.

So, to sum it all up: Sand hits grinds down one side of the station, you
get a minute of warning, shield generators now spawn in maintenance. Be
a good crewmate and help where you can.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

More event variety is good, and events that give the players agency on
how bad the impact will be is even better.

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

:cl: Rhials
add: Sandstorm random event! A random side of the station is pummeled by
an onslaught of sand and dust. If you hear that one is approaching, grab
a welder and some iron to help with repairs!
add: Space sand! It's weak and doesn't hurt reinforced walls, but
shouldn't be underestimated in high quantities.
code: You can now pass a start direction to the
spawn_meteors/spawn_meteor global procs.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[08aa858561...](https://github.com/treckstar/yolo-octo-hipster/commit/08aa8585618d936475c0e9a875090aee486eec4a)
#### Sunday 2022-12-25 21:22:02 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [SMERTONOS/tgstation](https://github.com/SMERTONOS/tgstation)@[9e69e5d6ac...](https://github.com/SMERTONOS/tgstation/commit/9e69e5d6acae10bf0941155c418ea3b9194668e5)
#### Sunday 2022-12-25 21:28:05 by LemonInTheDark

Minor plane cube cleanup (#72038)

## About The Pull Request

[Fixes area lighting not working on turf change in multiz
cases](https://github.com/tgstation/tgstation/commit/7b92deffbca92a834cb0a361fd685de51a12ea53)

If you modify a area lit turf when using multiz, it'd end up using the
wrong plane for its light, because of stupid shit on my part.
Stupid shit resolved

[Fixes some uses of plane masters that only specified one rather then
all](https://github.com/tgstation/tgstation/commit/a59ec96d29710b967bf8b3ffe8210b230cb194b3)

We almost never only want to show SOME hidden planes. 
Should really make a helper for this someday

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[0747099063...](https://github.com/IndieanaJones/tgstation/commit/074709906301e3e396179c861ca0af068c3f36ec)
#### Sunday 2022-12-25 21:36:00 by RikuTheKiller

Adds a reagent injector component and BCI manipulators to all circuit labs (#71236)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

This PR adds a reagent injector component that's exclusive to BCIs.
(Requested to be integrated into BCIs by Mothblocks.)
When outside of a circuit, the component itself stores the reagents.
However, if it's inside of a BCI, the storage is moved to the BCI. The
storage can contain up to 15u of reagents and acts like an open
container. (However, it won't spill even if you throw it, it just acts
like an open container code-wise, don't worry about it.)
You can only have one reagent injector in a circuit. Trying to insert
multiple will give you an error message.
The entire dose is administered at once. (Requirement set by
Mothblocks.)

Please don't try to dispute any of the specific limitations in the
comments as they're out of my control. They're reasonable anyways.

Reagent Injector Input/Output:
Inject (Input Signal) - Administers all reagents currently stored inside
of the BCI into the user.
Injected (Output Signal) - Triggered when reagents are injected. Not
triggered if the reagent storage is empty.

New BCI Input:
Show Charge Meter (Number) - Toggles showing the charge meter action.
(Adds some capacity for stealth.)

Install Detector Outputs: (Added following a comment about having to use
weird workarounds for proper loops.)
Current State (Number) - Outputs 1 if the BCI is implanted and 0 if it's
not.
Installed (Signal) - Triggered when the BCI is implanted into it's user.
Removed (Signal) - Triggered when the BCI is removed from it's user.

This PR also adds BCI manipulation chambers to all currently present
circuit labs. (Solution proposed by Mothblocks.)
Yes I had to do some other mapping changes to allow for this. No I don't
have any mapping experience, why do you ask?

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

One small step for BCIs, one giant leap for circuit kind. (First
"proper" circuit to human interaction in the entire game!)

This allows for some funky stuff and also makes it less of a pain in the
ass to use BCIs. What's not to love?

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
add: Added a reagent injector component and BCI manipulators to all
circuit labs. (+ install detector component)
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[bf582cb833...](https://github.com/IndieanaJones/tgstation/commit/bf582cb833d89b7121b4fefa37e8da1773783245)
#### Sunday 2022-12-25 21:36:00 by Profakos

Trophy case update (#71015)

## About The Pull Request

I have been chipping away/procrastinating at this since May, but after
several years, I have finally updated how Trophy Cases work.

So, what this PR does is the following:

- Standardized everything in persistence.dm to use snake case, and added
basic autodocs
- Automatically moves trophies from data/npc_saves/TrophyItems.json to
data/trophy_items.json. Removed legacy .sav conversion by request, it
has been a long time.
- Trophy cases are opened and loaded the same way you would open a
regular ID locked display case (used curator access, relevant access
autodoc has been updated)
- Instead of cheap plastic replicas that turn to dust anyways, trophy
cases use holograms, which can be dispelled by hand
- Trophy data gets saved if an item stays in the trophy case when the
shuttle arrives to centcom, and the item has a description set. This is
in line with paintings, which has to still hang on the wall at round
end.
- You can edit the description of new trophies by using the librarian's
key to unlock History Mode
- When you click on a closed trophy case, it will open a tgui, and will
not display the case description. It will still do for open cases.
Vendatrays have been updated to do the same.
- The UI's icon uses icon2base64(getFlatIcon(showpiece, no_anim=TRUE)).
Vendatrays have been updated similarly, so items with directions and
animations are displayed properly. The base64 strings are updated in
update_static_data.
- Fixes vendatrays from displaying some characters in strange ways, such
as displaying /improper.
- Renames some one letter, or nonindicate argument and var names in
trophy case code
- Adds a trophy management admin panel, where admins can finally delete
all the curator ID cards swallowed over the years. Or, they can replace
the paths with funny new paths.
- If an entry has an incorrect, no longer existing path, it will be
marked red in the management panel
- Adds MAX_PLAQUE_LEN define, which 144 characters
- Removes start_showpieces from trophy cases, as it was completely
unused. The start_showpiece_type var is still around.
- Moves trophy_message var to trophy cases. Only a dice collector
display case used them in the Snowdin map.

What this PR does not do

- Sadly, it still only saves the base image of an item, and no layers or
altered image states. This has to come in the future.

<details>
<summary>Click here to see various states of the trophy tgUI</summary>
 

![kép](https://user-images.githubusercontent.com/2676196/199545412-e5b7e7a8-59fb-41e6-aca5-6b07ba33501c.png)
Locked history mode, existing item.


![kép](https://user-images.githubusercontent.com/2676196/199545574-9e705603-9b7a-457d-9575-2d4145ad940d.png)
Unlocked history mode, but holographic trophy is present.


![kép](https://user-images.githubusercontent.com/2676196/199545883-45c3916b-011f-462a-8296-6eb13db32158.png)
Locked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199545967-a33e2501-aa5f-473b-b79f-ebd950df2afc.png)
Unlocked history mode, no item.


![kép](https://user-images.githubusercontent.com/2676196/199546100-718bd639-3199-4df7-ad77-ed3dbf27b290.png)
Unlocked history mode, item placed, default text. (Note: this picture is
out of date. The typo has been fixed, and "record a message" is now
"record a description" for consistency)
 

![kép](https://user-images.githubusercontent.com/2676196/199546202-5ebbbd28-907c-4f2d-b7cd-29d2ef21c7f3.png)
Unlocked history mode, item placed, new text.

</details>

<details>
<summary>Click here to see the admin panel</summary>


![kép](https://user-images.githubusercontent.com/2676196/199553349-8684f23f-4699-42f2-a27e-15cccad29d0b.png)


</details>

## Why It's Good For The Game

Less curator ID's stuck in the Trophy Cases, and the existing ones can
be cleaned up. A more immersive Trophy Case user experience, in general.

## Changelog


:cl:
refactor: refactored trophy cases, to be more user friendly
admin: created a trophy managment admin panel
/:cl:

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[bbb956d2a6...](https://github.com/IndieanaJones/tgstation/commit/bbb956d2a670656e546c35a09ec27295e5e06e94)
#### Sunday 2022-12-25 21:36:00 by OrionTheFox

Removes Bowls from garbage spawners because they don't fit in trash bags and I'm SICK of not being able to clean! (#71152)

## About The Pull Request
Let me give you a scenario.

---

THIS, is you. Say hi!

![image](https://user-images.githubusercontent.com/76465278/200268480-9dcf1f45-3bc5-402d-b743-b0649deefb08.png)

You're a loyal janitor aboard NT-SS13. You love your job; despite the
dangers, it's generally not too busy or tedious. Just a spray, a sweep,
and put it all in a bag.

---

This. This is your enemy.

![image](https://user-images.githubusercontent.com/76465278/200269058-957ca433-4666-44b5-9c10-ae0da75219cb.png)

Some crewmembers continuously leave them in maintenance, tossing them
into garbage bins as they pass.
This bowl, you cannot spray it. You can sweep it as far as you want, but
in the end, cannot put it into the bag.

![image](https://user-images.githubusercontent.com/76465278/200269156-bbc7758b-9cbe-4a3b-8d17-9aa53254b4b2.png)

---

It exists to torment you.
Nothing more, nothing less.

You hate the bowl. And it hates you.
Wake up.

![image](https://user-images.githubusercontent.com/76465278/200269456-a7fda598-3556-4069-bd2a-44a8793c198f.png)
## Why It's Good For The Game
Usually when you pass a trash pile you expect it to have trash, and
entire bowls aren't technically trash code-wise, nor can you clean them.
Yes, this PR has a modicum of salt. It was salt left behind in THE DAMN
BOWLS.
## Changelog
:cl:
del: NT has decided to begin a Recycling initiative, asking crew to
please stop throwing their bowls away in maintenance. You should only
find trash and grime from now on!
/:cl:

---
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[c1f0141967...](https://github.com/IndieanaJones/tgstation/commit/c1f01419671ad084a6c048ec7900d008de53bfe2)
#### Sunday 2022-12-25 21:36:00 by LemonInTheDark

Fixes mineral turfs having weird lighting (#71219)

## About The Pull Request

Pixel offsets, unlike transforms, offset overlays too. this was breaking
lighting overlays for mineral walls.

We did pixel offsets to save on init time, but we can acomplish the same
thing using an initial matrix. It's static, so there's no additional
cost. S free

Damn moth

## Changelog
:cl:
fix: Mining walls won't have fucked lighting anymore
/:cl:

---
## [Tupinambis/TerraGov-Marine-Corps](https://github.com/Tupinambis/TerraGov-Marine-Corps)@[a96d4df973...](https://github.com/Tupinambis/TerraGov-Marine-Corps/commit/a96d4df9736c68bf6534de6124698fabbd9e9c97)
#### Sunday 2022-12-25 21:48:14 by 567Turtle

item storage tweaks (#10913)

* whistle thing

i hate this fucking game

* grammar

who knew defibrillator was spelled with two Ls

* defib go bye bye

bye bye

* few other things

Makes it so you can put a sodering tool in your belt and your vest, robots need healing to

* injector boots

If you can put a whole ass MRE in your boot you can put a little ass pen in there

* reverts changelog changes

nuff said

* fixes things

adds trail commas where I forgot them, removes medipens going in shoes

* jaeger module soldering tool

you can put a soldering tool into the medical jaeger storage module :)

* reverts typo fix

nuff said

---
## [maesierra/adventOfCode2022](https://github.com/maesierra/adventOfCode2022)@[08c159ce15...](https://github.com/maesierra/adventOfCode2022/commit/08c159ce151b5f86bee1b3da50018b43fd2d9dc4)
#### Sunday 2022-12-25 23:34:07 by Maria-Eugenia Sierra

day 25

piece of cake (compared with the last week)

go rant

quite disappointed with go. I cannot see any reasonable use case for it. It's just a better C, but with all the C annoyances
this half-baked OO is clearly insuficient to take advantage of OO

It doesn't have enought library power to compete with PHP and I rather use python half-baked OO. It's not good either but
it's much better than this

It's fast and light weight and the syntax it's OK but without OO or free cast it's really difficult to model

Generics seems a nice addition but they're quite recent to the language

tooling wise, the debugger is quite limited (I'm so used to be able to do proper evaulations) and you cannot have a quick varilable to
check a return function value. Because the compiler won't alow you to run with the unused varilable (to be fair probably that's something
that can be changed on the settings)
Maybe GoLand it's good, but VS Code go it's limited.

I don't think I will use it for anything, but I will definitelly repeat the experience of doing next year AoC in a language I want to
learn. It's definitelly how to learn a programming language in 25 days.

Next year it will be either Scala or Python (I need to learn python properly)

---

