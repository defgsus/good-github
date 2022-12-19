## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-12-18](docs/good-messages/2022/2022-12-18.md)


1,844,688 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,844,688 were push events containing 2,437,682 commit messages that amount to 131,798,580 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 40 messages:


## [ThePiachu/cmss13](https://github.com/ThePiachu/cmss13)@[8f1ee35f1d...](https://github.com/ThePiachu/cmss13/commit/8f1ee35f1de18e295fa29e4536ad00431e7f0d76)
#### Sunday 2022-12-18 00:02:09 by carlarctg

Refactored weed crossing to utilize signals and list data. (#1960)

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

Refactored weed slowdown to work based on a signal sent to the recipient
carrying list data.

Added a variable for weed slowdown multiplier to species. Human Heroes
have 0.5 weed slowdown because haha funny. Transferred Yautja's weed
immunity to species.

Added an admin-only example item 'hiking boots' that halve weed
slowdown.

Removed a useless define for XVX.

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
refactor: Refactored weed slowdown to work based on a signal sent to the
recipient carrying list data.
code: Added a variable for weed slowdown multiplier to species. Human
Heroes have 0.5 weed slowdown because haha funny. Transferred Yautja's
weed immunity to species.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Rah-Jose-Israel/Philosophy-of-This_Project](https://github.com/Rah-Jose-Israel/Philosophy-of-This_Project)@[7745b5c0a7...](https://github.com/Rah-Jose-Israel/Philosophy-of-This_Project/commit/7745b5c0a7428aea08b3596358d9efbc47bc979a)
#### Sunday 2022-12-18 00:30:11 by Rah-Jose-Israel

Enter A new grad With literally no idea what the shit to do with his life.
So this means just we do something, This is that something.

---
## [xDroidOSS-Pixel/frameworks_base](https://github.com/xDroidOSS-Pixel/frameworks_base)@[60d6e0fab1...](https://github.com/xDroidOSS-Pixel/frameworks_base/commit/60d6e0fab119ea66069491c449c510ba4344cd31)
#### Sunday 2022-12-18 00:36:44 by Kuba Wojciechowski

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
## [ArtemisStation/artemis-tg](https://github.com/ArtemisStation/artemis-tg)@[75439c71f2...](https://github.com/ArtemisStation/artemis-tg/commit/75439c71f2282a3ae72b4ea35c80e27ca8556aaf)
#### Sunday 2022-12-18 01:06:12 by Mothblocks

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
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[3d63335fc9...](https://github.com/treckstar/yolo-octo-hipster/commit/3d63335fc996b3f6abffe92a13ee1708487ee16e)
#### Sunday 2022-12-18 01:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [TheWolfbringer/tgstation](https://github.com/TheWolfbringer/tgstation)@[44008f485d...](https://github.com/TheWolfbringer/tgstation/commit/44008f485d6d72537935cfa8a3a5b6140eece744)
#### Sunday 2022-12-18 02:03:03 by Jacquerel

Fishing-themed Escape Shuttle (#71805)

## About The Pull Request

I can't do much coding until you review my other PRs so I'm making a
mapping PR instead.
I actually made this a while ago while I was trying out strongDMM. It
turns out: it's a good tool and easy to use.

![2022 12 09-10 51
26](https://user-images.githubusercontent.com/7483112/206686234-ae952ba3-2cb4-4093-80a0-d086fe95a3fc.png)

This mid-tier shuttle isn't enormous and is shaped like a fish. It
dedicates much of its internal space to an artificial fishing
environment, plus fishing equipment storage. Plus look at that lovely
wood panelling!
There's not a lot of seating or a large medbay, but there's five fishing
rods for people to wrestle each other over plus some aquariums to store
your catches in.

It contains a variety of fishing biomes (ocean, moisture trap, hole,
portal) but I couldn't fit "lava" in there even though I wanted to
because it's hardcoded to only have fish in it on the mining z-level.
If you're very lucky and nobody shoves you, the time between the shuttle
docking at the station and arriving at Centcomm might be enough time for
you to catch maybe four entire fish. Wow!

## Why It's Good For The Game

There are plenty of novelty shuttle options but I think this one is good
for a personal touch of "the Captain would rather be fishing than
hearing you complain about the nuclear operatives".

## Changelog

:cl:
add: Tell your crew how much you care by ordering a shuttle where half
of the seats have been removed so that you can get some angling done
before you clock out.
/:cl:

---
## [manif3station/web-plugins](https://github.com/manif3station/web-plugins)@[5a33dde32f...](https://github.com/manif3station/web-plugins/commit/5a33dde32f47e217d57fe50377fae3a30136154b)
#### Sunday 2022-12-18 02:08:30 by Michael Vu

Eliminating Silly Repetitive Tasks

As a developer, we all know the frustration of having to run the same command
multiple times. It's a waste of time and energy, and it can be especially
frustrating when it's something as simple as updating a plugin.

That's where this patch comes in. When the plugin update script is called, it
will now check if it has been updated itself. If it has, it will automatically
run the update command again without the user having to do it manually.

This may seem like a small change, but it can make a big difference in
streamlining your workflow and eliminating unnecessary steps. So next time
you're updating your plugin, you won't have to worry about running the command
twice - the script will take care of it for you.

This patch is just one example of how small changes can have a big impact, and
it's a reminder that even the smallest improvements can make a difference in
our daily work.

---
## [Nakoi/The-Lost-Isles](https://github.com/Nakoi/The-Lost-Isles)@[47ae48623b...](https://github.com/Nakoi/The-Lost-Isles/commit/47ae48623be1c7802088147181535e8a221ee524)
#### Sunday 2022-12-18 02:41:51 by microwave

fucking fuck you you fucking bitch fuck bitch fuck

---
## [Emonumia/hyper-dungeon-explore](https://github.com/Emonumia/hyper-dungeon-explore)@[a060192d5a...](https://github.com/Emonumia/hyper-dungeon-explore/commit/a060192d5a5cb39a7b17977d0e55f0963cbfdcce)
#### Sunday 2022-12-18 03:00:06 by Emonumia

A* Pathfinding

Fully implemented A* pathfinding with some good looking assets. A bug still remains,  the character is able to move
 diagonally, which means he has a really wide range to move, and create some really annoying graphical bugs, he leaves a trace behind when he exceeds its typical range, and it's kinda game breaking in my opinion, need to fix thos asap, but not now since it is 4 am, good night

---
## [parthkax70/openbsd](https://github.com/parthkax70/openbsd)@[0cffdb45a9...](https://github.com/parthkax70/openbsd/commit/0cffdb45a9bb573ce4665f5540d1a0d50ff2e37f)
#### Sunday 2022-12-18 03:28:12 by tb

acme-client: fix SAN-handling insanity

The revoke process, which does a lot more than revoking a cert, wants to
know the SANs in the cert to be revoked or renewed and check them against
the ones configured in the config file.

To find out which ones are, it prints the SAN extension to a BIO using
X509V3_EXT_print(), slurps that into a buffer, tokenizes the undocumented
output string and plucks out the "DNS:" names. This is reminiscent of
node's hilarious CVE-2021-44532 and on about the same level of crazy, but
fortunately not security relevant.

Get the SAN extension as a GENERAL_NAMES from libcrypto, then we have an
actual data structure to work with, which allows us to access the DNS names
without problems. This simplifies things quite a bit, but the actual logic
in this file remains unmodified. Be careful about ASN1_IA5STRINGs and do
not assume they are C strings.

Tested by florian, millert, Renaud Allard, thanks!

ok florian jsing

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[00e7d5d746...](https://github.com/tgstation/tgstation/commit/00e7d5d7465211ccf0e3d604e566e2c08775cd20)
#### Sunday 2022-12-18 04:30:17 by GoldenAlpharex

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
## [cake-pie/Cataclysm-DDA](https://github.com/cake-pie/Cataclysm-DDA)@[8e39d6f97c...](https://github.com/cake-pie/Cataclysm-DDA/commit/8e39d6f97c358c72a3dacc7c2f3ce955ecb30e81)
#### Sunday 2022-12-18 04:58:16 by casswedson

fix: edge case ci error exit (#62660)

so a step of the reviewer workflow always runs, good it is the actual
magical step doing the hard work, but if the workflow gets canceled, the
step exits with an error code, I actually knew this but me from like a
day ago was like:
"nah man this won't bother me in the future."

guess what; after a couple hours I was felling the pain my perfectionist
subconscious was putting me through, plus odd error code exits aren't
very professional or clean or pleasing I'd say, also someone may think
it's weird, look into it, waste time looking at my code

title: do not draw much attention

Co-authored-by: casswedson <casswedson@users.noreply.github.com>

---
## [morgoth1145/advent-of-code](https://github.com/morgoth1145/advent-of-code)@[2b50c1ae8b...](https://github.com/morgoth1145/advent-of-code/commit/2b50c1ae8b038fffc7d2af5b8d48129aa14d374a)
#### Sunday 2022-12-18 05:23:14 by Patrick Hogg

2022 Day 18 Part 2

Ah, so now we have some internal air pockets to exclude from the calculation. A flood fill will work well, but it needs a boundary for the exterior to know when it is indeed an exterior! Thankfully some coordinate boundaries can work for that pretty well.

Unfortunately I goofed up in getting those boundaries by treating the minimums as the maximums for making the ranges! That dumb mistake cost me an annoying amount of time, but once fixed I got the answer easily.

I dropped all the way to rank 168, but at least today was quick. I was worried about how late I'd be up given that I need to be to church to stream in the morning!

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[6dd4839ef3...](https://github.com/tgstation/tgstation/commit/6dd4839ef321aa0a997549d1ae07fe7ccbba59ed)
#### Sunday 2022-12-18 05:41:14 by carshalash

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
## [koutsie/cinny](https://github.com/koutsie/cinny)@[44d8da88ca...](https://github.com/koutsie/cinny/commit/44d8da88caff96a5ec375eb988fb6e4c6f53bcb3)
#### Sunday 2022-12-18 06:59:27 by koutsie

An Important Commit for main.c

Dear fellow developers,

I am thrilled to announce that we have made a truly fantastic addition to our project with the following line of code:

gtk_widget_set_size_request(GTK_WIDGET(window), 800, 450);

This line of code is simply amazing. It sets the minimum size for the GTK widget (which, as you all surely know, stands for GIMP Toolkit) to a width of 800 pixels and a height of 450 pixels. This is an absolutely crucial change that will take our project to new heights of greatness.

You see, I have been using a tiling window manager for my development work, and I must say, it can be a bit of a pain when the window gets lost or misplaced. But with this new line of code, I can rest easy knowing that my window will always be exactly where I need it to be.

I am so impressed with this change that I can't help but praise it to the heavens. It is sleek, efficient, and simply gorgeous. The attention to detail and the care that has gone into crafting this line is truly something to behold.

So let's all give a round of applause to the brilliant developer who made this happen. You are truly a genius, and I thank you for your hard work and dedication.

Thank you, and God bless America.

Sincerely,
Koutsie.

---
## [walternewtz/android_kernel_xiaomi_sdm845](https://github.com/walternewtz/android_kernel_xiaomi_sdm845)@[241f587da5...](https://github.com/walternewtz/android_kernel_xiaomi_sdm845/commit/241f587da54eb92f8c89b330cea36d6f0c7b4d9b)
#### Sunday 2022-12-18 06:59:57 by tanish2k09

Introducing KLapse - A kernel level livedisplay module v4.0:

Author: @tanish2k09 (email: tanish2k09.dev@gmail.com)

What is it?
Kernel-based Lapse ("K-Lapse") is a linear RGB scaling module that 'shifts' RGB based on time (of the day/selected by user), or (since v2.0) brightness. This concept is inspired from
LineageOS (formerly known as 'CyanogenMod') ROM's feature "livedisplay" which also changes the display settings (RGB, hue, temperature, etc) based on time.

Why did you decide to make this? (Tell me a story).
I (personally) am a big fan of the livedisplay feature found on LineageOS ROM. I used it every single day, since Android Lollipop. Starting from Android Nougat, a native night mode
solution was added to AOSP and it felt like livedisplay was still way superior, thanks to its various options (you could say it spoiled me, sure). I also maintained a kernel (Venom
kernel) for the device I was using at that time. It was all good until the OEM dropped support for the device at Android M, and XDA being XDA, was already working on N ROMs. The issue
was, these ROMs weren't LineageOS or based on it, so livedisplay was... gone. I decided I'll try to bring that feature to every other ROM. How would I do that? Of course! The kernel! It
worked on every single ROM, it was the key! I started to work on it ASAP and here it is, up on GitHub, licensed under GPL (check klapse.c), open to everyone :)

How does it work?
Think of it like a fancy night mode, but not really. Klapse is dependent on an RGB interface (like Gamma on MTK and KCAL on SD chipsets). It fetches time from the kernel, converts it to
local time, and selects and RGB set based on the time. The result is really smooth shifting of RGB over time.

How does it really work (dev)?
Klapse mode 1 (time-based scaling) uses a method void klapse_pulse(void) that should ideally be called every minute. This can be done by injecting a pulse call inside another method that
is called repeatedly naturally, like cpufreq or atomic or frame commits. It can be anything, whatever you like, even a kthread, as long as it is called repeatedly naturally. To execute
every 60 seconds, use jiffies or ktime, or any similar method. The pulse function fetches the current time and makes calculations based on the current hour and the values of the tunables
listed down below.

Klapse mode 2 (brightness-based scaling) uses a method void set_rgb_slider(<type> bl_lvl) where is the data type of the brightness level used in your kernel source. (OnePlus 6 uses u32
data type for bl_lvl) set_rgb_slider needs to be called/injected inside a function that sets brightness for your device. (OnePlus 6 uses dsi_panel.c for that, check out the diff for that
file in /op6)

What all stuff can it do?

1, Emulate night mode with the proper RGB settings
2, Smoothly scale from one set of RGB to another set of RGB in integral intervals over time.
3, Reduce perceived brightness using brightness_factor by reducing the amount of color on screen. Allows lower apparent brightness than system permits.
4, Scale RGB based on brightness of display (low brightness usually implies a dark environment, where yellowness is probably useful).
5, Automate the perceived brightness independent of whether klapse is enabled, using its own set of start and stop hours.
6, Be more efficient,faster by residing inside the kernel instead of having to use the HWC HAL like android's night mode.
7, (On older devices) Reduce stuttering or frame lags caused by native night mode.
8, An easier solution against overlay-based apps that run as service in userspace/Android and sometimes block apps asking for permissions.
9, Give you a Livedisplay alternative if it doesn't work in your ROM.
10, Impress your crush so you can get a date (Hey, don't forget to credit me if it works).

Alright, so this is a replacement for night mode?
NO! Not at all. One can say this is merely an alternative for LineageOS' Livedisplay, but inside a kernel. Night mode is a sub-function of both Livedisplay and KLapse. Most comparisons
here were made with night mode because that's what an average user uses, and will relate to the most. There is absolutely no reason for your Android kernel to not have KLapse. Go ahead
and add it or ask your kernel maintainer to. It's super-easy!

What can it NOT do (yet)?

1, Calculate scaling to the level of minutes, like "Start from 5:37pm till 7:19am". --TODO
2, Make coffee for you.
3, Fly you to the moon. Without a heavy suit.
4, Get you a monthly subscription of free food, cereal included.

All these following tunables are found in their respective files in /sys/klapse/

1. enable_klapse : A switch to enable or disable klapse. Values : 0 = off, 1 = on (since v2.0, 2 = brightness-dependent mode)
2. klapse_start_hour : The hour at which klapse should start scaling the RGB values from daytime to target (see next points). Values : 0-23
3. klapse_stop_hour : The hour by which klapse should scale back the RGB values from target to daytime (see next points). Values : 0-23
4. daytime_rgb : The RGB set that must be used for all the time outside of start and stop hour range.
5. target_rgb : The RGB set that must be scaled towards for all the time inside of start and stop hour range.
6. klapse_scaling_rate : Controls how soon the RGB reaches from daytime to target inside of start and stop hour range. Once target is reached, it remains constant till 30 minutes before
   stop hour, where target RGB scales back to daytime RGB.
7. brightness_factor : From the name itself, this value has the ability to bend perception and make your display appear as if it is at a lesser brightness level than it actually is at.
   It works by reducing the RGB values by the same factor. Values : 2-10, (10 means accurate brightness, 5 means 50% of current brightness, you get it)
8. brightness_factor_auto : A switch that allows you to automatically set the brightness factor in a set time range. Value : 0 = off, 1 = on
9. brightness_factor_auto_start_hour : The hour at which brightness_factor should be applied. Works only if #8 is 1. Values : 0-23
10. brightness_factor_auto_stop_hour : The hour at which brightness_factor should be reverted to 10. Works only if #8 is 1. Values : 0-23
11. backlight_range : The brightness range within which klapse should scale from daytime to target_rgb. Works only if #1 is 2. Values : MIN_BRIGHTNESS-MAX_BRIGHTNESS

Signed-off-by: Eliminater74 <eliminater74@gmail.com>
Signed-off-by: energyspear17 <energyspear17@gmail.com>
Signed-off-by: Michael <loukerismichalis@gmail.com>
Signed-off-by: PainKiller3 <ninadpatil100@gmail.com>

---
## [nbitzz/theUnfunny](https://github.com/nbitzz/theUnfunny)@[84567050cd...](https://github.com/nbitzz/theUnfunny/commit/84567050cd21b3faf3154d49219ae7a6767c1270)
#### Sunday 2022-12-18 07:20:32 by nbitzz

someone please end my suffering
I made a list and checked it twice
For all the fucks I give about ending Santa's life
And I found none
I'll travel at the speed of light

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[c9b98daa61...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/c9b98daa6180e2151cb662f6a3d7e5d7a7caea47)
#### Sunday 2022-12-18 08:04:06 by Christian Brauner

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
Signed-off-by: kuplemarkeple <ewprjkt@proton.me>

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[4d4c3b99ef...](https://github.com/mrakgr/The-Spiral-Language/commit/4d4c3b99ef904ddc62127cc3ab52ef7e07bd12d5)
#### Sunday 2022-12-18 09:31:02 by Marko Grdinić

"8:45am. I am up. Let me just do some of the programming necessities I thought up over the night. I screwed up some things.

```fs
    let g_suppr : Dictionary<TypedBind, TyV Set> = Dictionary(HashIdentity.Reference)
    let g_decr : Dictionary<TypedBind, TyV Set> = Dictionary(HashIdentity.Reference)
    let g_incr : Dictionary<TypedBind, TyV Set * bool> = Dictionary(HashIdentity.Reference)

    let incref_cancellation () =
        let g_incr' : Dictionary<TypedBind, TyV Set> = Dictionary(HashIdentity.Reference)
        g_incr |> Seq.iter (fun kv ->
            let add (d : Dictionary<TypedBind, TyV Set>) x = if Set.isEmpty x then () else d.[kv.Key] <- x
            let f (g : Dictionary<_,_>) = match g.TryGetValue(kv.Key) with true, x -> x | _ -> Set.empty
            let decr, suppr = f g_decr, f g_suppr
            let incr, is_in_container = kv.Value
            let g a b = a - b, b - a
            let incr, suppr = g incr suppr
            let incr, decr = if is_in_container then g incr decr else incr, decr
            add g_incr' incr; add g_suppr suppr; add g_decr decr
            )
        {g_decr=g_decr; g_suppr=g_suppr; g_incr=g_incr'}
```

Remember how I said I should not optimize? Well, I went and did it. And as a result the code is broken. I only realized during the night that if the input to add is empty, it won't clear the existing set. Whops.

```fs
open System.Collections.Generic
let a = Dictionary()
a.Add("qwe",true)
a.Remove("qwe")
```

Ah, I see, this will in fact remove the key and return a bool as to whether it has been returned.

8:55am.

```fs
    let incref_cancellation () =
        let g_suppr' : Dictionary<TypedBind, TyV Set> = Dictionary(g_suppr.Count, HashIdentity.Reference)
        let g_decr' : Dictionary<TypedBind, TyV Set> = Dictionary(g_decr.Count, HashIdentity.Reference)
        let g_incr' : Dictionary<TypedBind, TyV Set> = Dictionary(g_incr.Count, HashIdentity.Reference)
        for KeyValue(k,(incr,is_in_container)) in g_incr do
            let f (g : Dictionary<_,_>) = match g.TryGetValue(k) with true, x -> x | _ -> Set.empty
            let decr, suppr = f g_decr, f g_suppr
            let g a b = a - b, b - a
            let incr, decr = if is_in_container then g incr decr else incr, decr
            let incr, suppr = g incr suppr
            let add (d : Dictionary<TypedBind, TyV Set>) x = if Set.isEmpty x then () else d.[k] <- x
            add g_incr' incr; add g_decr' decr; add g_suppr' suppr
        {g_incr=g_incr'; g_decr=g_decr'; g_suppr=g_suppr'}
```

Let me go with this. Now it is super clean. This is the easiest way to think about it. The other consideration I thought of during the night, whether the refc are printed in the incref, decref, suppref order is fine.

9am. Perfect. Now...

///

Another question for Monday.

> In other words, each tasklet only has direct access to a subset of the overall DIMM memory space, which is less than 8gb (in current generations), so the 32-bit limitation doesn't matter.

Sorry, I wasn't reading what you wrote here properly yesterday. I was under the impression that each each tasklet has access to the entirety of MRAM for it rank which 8gb. Is my assumption wrong? I know you can give tasklets their stack size, but all the MRAM partitioning that I've seen being done is my pushing offsets.

Also are the MRAM pointers 32 or 64 bit? I've been assuming they are 32-bit, but if they are 64-bit that would explain a lot.

///

Let me try fielding this again.

9:15am. Now let me chill.

Ugh, my readership is falling off a cliff in ch 12. Do I want to write or do I want to program.

Let me read Knight Run and a chapter of Otome Survival. Then I will check whether indent works properly in the two backends.

9:25am. https://boards.4channel.org/a/thread/246448142/villain-does-nothing-wrong#p246450907

///

>>246450139
he'd absolutely keep inventing new forms of 'death' that he needs to go on an epic thousand years quest to become immune to
>black holes become theorized
>oh fuck oh fuck oh shit I need to become immune to gravity RIGHT NOW

///

Based.

https://boards.4channel.org/a/thread/246448142/villain-does-nothing-wrong#p246450811

The evil is the ultimate cuckoldry post is worth saving as well.

Ah, fuck it. I do not feel like reading Otome Survival. Let me check out the AyaTri thread and then I will finally check the indent. Also Knight Run.

10:05am. Let me get started.

Let me try out indent.

You know, I just realized, if I want this I do not even need the indent.

For example, I can just pass in a closure. Let me show what I mean in Python.

```py
def with_(x,f): with x() as tmp: return f(tmp)
```

I can just print this as a global statement. Though it wouldn't be as elegant as what I want to do now...

10:20am. You know, rather than let this bother me, I should just dive right in.

10:25am. Yeah, you know what.

```py
def with_(x,f): with x() as tmp: return f(tmp)
```

It is not ideal, but I am going to go with this. This will result in needless closure allocation and such, but language statements really have to put into the parser and then everywhere else. It would really be nasty to keep writing those macros and indents everywhere.

Let me get rid of Indent.

But first, let me just commit here, since I fixed the bug from yesterday night."

---
## [QuacksQ/Skyrat-tg](https://github.com/QuacksQ/Skyrat-tg)@[0b9264ce5f...](https://github.com/QuacksQ/Skyrat-tg/commit/0b9264ce5f14565e42d5e3dc67660a95f5d48f65)
#### Sunday 2022-12-18 11:40:24 by SkyratBot

[MIRROR] Fixes mineral turfs having weird lighting [MDB IGNORE] (#17618)

* Fixes mineral turfs having weird lighting (#71219)

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

* Fixes mineral turfs having weird lighting

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[7687a28e7c...](https://github.com/tgstation/tgstation/commit/7687a28e7ceecea6b9e0aacdb58a2271b063f9d3)
#### Sunday 2022-12-18 12:23:34 by Sol N

refreshes syndi-kits and syndicate surplus crates, introduces shared limited stock (#71869)

## About The Pull Request

After all, the Syndicate loves a good throwback.


![C6O47fPhAB](https://user-images.githubusercontent.com/116288367/207737104-3d24574f-02e0-433d-8ea7-6825ca4cb970.png)

This PR does a few things with the goal of reimplementing and
revitalizing syndicate traitor kits and the syndicate surplus crate.
Of note is that I have added in a way for limited stock items to share
their limited stock.

Following maintainer guidance the syndicate traitor kits have increased
in price and as a result some of the lower value ones have been
adjusted. I've given all active bundles current TC costs per item
knowing full well they will be inaccurate eventually.

<details>
  <summary>Changes as a result of my audit of syndikits</summary>
    
### UNCHANGED
Recon, Spai, Stealthy, Screwed, Sniper, Nukie Meta, Implants
Mad Scientist, Bees

Lord Singuloth is also unchanged and disabled, I think that it should
turn into a new supermatter themed kit maybe. outside of current scope.

### Gun Kit
Replaced emag with doorjack and gave it a chameleon holster, literally
moved 1 tc elsewhere

### Murderer
replaced emag again, no additions its a lot of tc and Just Good

### Hacker
added doorjack, otherwise unchanged

### Sabotage
no changes other than adding in extra bombs it didnt have

### James Bond
gave him some gadgets with the freedom implant, emp flashlight, and one
x4. also a cyanide pill and deck of cards for fun

### Ninja
Added in miner Jump Boots, smoke spell, and doorjack. dont just want it
to be space ninja

### Dark Lord
Added in new lightning bolt spell granter and made the desword default
to red. probably overbudget.

### White Whale
dehydrated carp added so you can ride it alongside the ones you grenade
out. hard to imagine changing this

### Mr Freeze
changed temperature gun to be cryo only so that i could give him the
cryo thermal pistol. cold attacks only.

### 2006 Traitor
doorjack.

</details> 

tl;dr theyre all about 30 tc worth of shit more or less some are more
but thats what rarity should be for
you can only buy from one type of syndicrate per round


![QOF1WO7CC6](https://user-images.githubusercontent.com/116288367/207739417-00ae6b81-b6aa-4774-a4bb-f2d880988ff4.gif)

Next up is the return of the surplus crate. 
Crate is generated, gives you gear **based on your progression at the
time of buying the crate**, you can use it all at the start and get some
chameleon kits and not a lot of dangerous weapons or wait till later.
I've changed the weight on some items here and there and given weight to
role and species locked items, though I will admit that latter is
unimportant because I set moth lanterns to be unable to appear in these
two crates.


![dreamseeker_t8abXysKqK](https://user-images.githubusercontent.com/116288367/206761978-96e2a51e-f9a5-48e4-a863-a9198fa15ea2.gif)

But who cares about that your eyes instantly went to the United Surplus
Crate and the United Surplus Key lets be honest.

The united surplus crate is 80 TC worth of uplink items relative to your
current progression when you purchase it and gives you a locked box. It
**will explode if you try to break it** so be careful with it. It gives
you 80 TC and costs 20 TC because it is impossible to open without key.
The rub of course is that the Syndicate forbids agents from buying more
than one surplus item of any kind, you need to find another traitor and
make them buy you a key to open your box. Or I guess you can share the
box?


![dreamseeker_ts0AZeiyfy](https://user-images.githubusercontent.com/116288367/207740388-3f688bba-5d71-48d2-8079-671bbed7e54e.gif)

Regardless, if the crate is opened with any other means it doesn't spawn
its contents, you need 2 traitor uplinks.
Both of these items have a 30 minute timer because you don't want a
crate that has 5 emp flashlights in it. You at least want one energy
sword.

I did a lot of code shit and changed various things to be proc based to
allow for more editing and interjection of things, as I wrote in code
comments making a crate thats locked to a specific set of progression
just means changing the proc that generates a list of valid uplink items
to check items' progression values to a specified value instead of your
characters progression.

Ok I think that goes over everything more or less????

## Why It's Good For The Game

I've heard that people liked these and I think they are quite fun, being
able to go from "i dunno what to do as a traitor" to "ah, of course, I
will become the Bombler" is a fun thing to be able to have, and people
like to get a bunch of random shit in the mail. Some of it even feels
free!!!!!!!!!!!!!!!!!!! Brain points go up!!!

The division of procs allows for more creativity with this system than
existed before as well as other possibilities for interacting with the
uplink handler in funny ways.

## Changelog

:cl:
add: the syndicate is once again distributing syndi-kits, some now with
new technology
add: a fresh batch of syndicate surplus crates have been sent out,
though they seem a bit lighter than before
add: in an effort to encourage cooperation, a traitor can now purchase
either the new United Surplus Syndicate Crate or its key, but not both
add: lightning bolt book granter for wizard event and one syndie-kit
bundle
add: temperature gun that only makes things colder for one syndie-kit
bundle
code: it is now possible to have uplink items share limited stock
bal: role-restricted items no longer can be delivered by the stray
syndicate drop pod event
/:cl:

---
## [kyak/gxkb-ru-by-flags](https://github.com/kyak/gxkb-ru-by-flags)@[87b9dfe917...](https://github.com/kyak/gxkb-ru-by-flags/commit/87b9dfe917be7ba6f7aae8ae73f781f94833d517)
#### Sunday 2022-12-18 12:25:24 by kyak

Revert "Russian warship, go fuck yourself!"

This reverts commit c93458256f924dd97efc23f3f3b510efc1f0a4c6.

---
## [le-fb/adventOfCode2022](https://github.com/le-fb/adventOfCode2022)@[03ded00cbd...](https://github.com/le-fb/adventOfCode2022/commit/03ded00cbdac33008f437dbdbcc6b197f5fd4488)
#### Sunday 2022-12-18 13:09:23 by Leon Faßbinder

FUCK YOU ELEPHANTS. slowest things in the universe now also includes this search algorithm^^

---
## [Holoo-1/tgstation](https://github.com/Holoo-1/tgstation)@[a9fda932e2...](https://github.com/Holoo-1/tgstation/commit/a9fda932e2a9d8cf20f5f74fdcbdbcca86d580e6)
#### Sunday 2022-12-18 13:15:37 by Tim

Drinking singulo ignores supermatter hallucinations and pulls nearby objects (#71927)

## About The Pull Request
Drinking a singulo will now:

- Give immunity to supermatter hallucinations
- Pulls objects to you based on the total volume in your system (20u =
1x1, 45u = 2x2, 80u = 3x3)
- Makes a burp and supermatter rays/sound when objects are pulled

The new ingredient is:

- Vokda 5u 
- Wine 5u
- Liquid Dark Matter 1u (replaces Radium)

## Why It's Good For The Game
More cool effects for drinks. Singularity is all about gravity and the
drink should have a theme around that.


![dreamseeker_2q21YXS698](https://user-images.githubusercontent.com/5195984/207297517-90d26395-dd30-4106-bdd4-b30b1ba3e20b.gif)

## Changelog
:cl:
add: Drinking singulo will now ignore supermatter hallucinations and
pull objects to you
balance: Change singulo drink recipe to require liquid dark matter
instead of radium.
/:cl:

---
## [Dallinger/Dallinger](https://github.com/Dallinger/Dallinger)@[73e39d94a7...](https://github.com/Dallinger/Dallinger/commit/73e39d94a7ba96a17438f3c5b149a36408838d66)
#### Sunday 2022-12-18 14:40:17 by Peter Harrison

Misc Docker quality of life improvements (#4616)

# Major

- Disabled the behavior where the built image name is written to config.txt. This behavior was inconsistent with the other Dallinger deployment patterns, because it meant that if you deployed once, changed code in experiment.py, then redeployed, then the experiment would launch in the former version unless you remembered to delete the image name from config.txt.
- Heroku deployments were failing because the default `heroku_python_version` had been discontinued by Heroku. We have experienced similar problems in the past and have always had to update Dallinger. Now we have changed the behaviour such that, if `heroku_python_version` is not specified in the experiment config, then it will use the default Python runtime currently in use by Heroku.

# Minor

- Propagate more information from deployment-related functions (e.g. dashboard credentials) so that they can be used by wrapper functions.
- Print more information (e.g. dashboard credentials) in deployment-related functions.
- Better debugging logs for docker-ssh deployments.
- Move deployment info logs from `deployment-info_{experiment_id}.txt` to `deploy_logs/*` to avoid clutter.
- Move default `dallinger_develop_directory` to `/tmp/dallinger_develop` because the original location was not writable by default on Docker.
- Minor bugfixes in docker-ssh deployment/export.
- Rename config variable `docker_ssh_volumes` -> `docker_volumes` because it's relevant also when we're doing docker locally. 
- Some minor renaming of internal variables for consistency.

---
## [dotty-staging/dotty](https://github.com/dotty-staging/dotty)@[2dd54ee51d...](https://github.com/dotty-staging/dotty/commit/2dd54ee51d846502d0efe492c8d7e5559fe46f78)
#### Sunday 2022-12-18 14:47:03 by odersky

Add error handling strawman

There is so far no standard way in Scala to address a class of situations
that's often called "error handling". In these situations we have two possible
outcomes representing success and failure. We would like to process successful
results further and propagate failures outward. The aim is to find a "happy path" where
we deal with success computations directly, without having to special-treat failing
results at every step.

There are many different ways in use in Scala to express these situations.

 - Express success with normal results and failure with exceptions.
 - Use `Option`, where success is wrapped in `Some` and failure is `None`.
 - Use `Either`, where success is wrapped in `Right` and failure is wrapped in `Left`.
 - Use `Try`, where success is wrapped in `Success` and failure (which must be an exception) is wrapped in `Failure`.
 - Use nulls, where success is a non-null value and failure is `null`.
 - Use a special `IO` monad like `ZIO`, where errors are built in.

Exceptions propagate silently until they are handled in a `catch`. All other failure
modes require either ad-hoc code or monadic lifting into for comprehensions to propagate.
`nulls` can only be treated with ad-hoc code and they are not very popular in Scala so far.

Exceptions should only be used if the failure case is very unlikely (rule of thumb: in less than 0.1% of cases).
Even then they are often shunned since they are clunky to use and they currently undermine type safety (the latter
point would be addressed by the experimental `saferExceptions` extension). That said, exceptions have their uses.
For instance, it's better to abort code that fails in a locally unrecoverable way with an exception instead of
aborting the whole program with a panic or `System.exit`.

If we admit that not all error handling scenarios should be handled with exceptions, what
else should we use? So far the only choices are ad-hoc code or monadic lifting. Both of these
techniques suffer from the fact that a failure is propagated out of only a single construct
and that major and pointless acrobatics are required to move out failures further.

This commit sketches a systematic and uniform solution to this problem. It essentially provides a way
to establish "prompts" for result types and a way to return to a prompt with an error value using
a method called `_.?`. This is somewhat similar to Rust's `?` postfix operator, which seems
to work well. But there are is an important difference: Rust's ? returns from the next-enclosing
function or closure whereas our `?` method returns to an enclosing prompt, which can be further outside.
This greatly improves the expressiveness of `?`, at the price of a more complex execution semantics.

For instance, here is an implementation of a "traverse"-like operation, converting a `List[Option[T]]`
into a `Option[List[T]]`.
```scala
def traverse[T](xs: List[Option[T]]): Option[List[T]] =
  optional:
    xs.map(_.?)
```
Here, `optional` is the prompt for the `Option` type, and `.?` maps `Option[T]` to the underlying
type `T`, jumping to the enclosing `optional` prompt in the case a `None` is encountered. You can
think of it as a safe version of `Option`'s `get`. This function could not be written like this
in Rust since `_.?` is a closure so a `None` element would simply be mapped to itself.

Also unlike for Rust, Scala's technique is library-based. Similar prompt/return pairs can be defined
for many other types. This commit also defines a type `Result` which is similar to Rust's that
supports the pattern. `Result` will hopefully replace `Either`, which is in my opinion an abomination
for error handling. All these constructs can be defined in terms of a lower-level construct
where one can simply return a result to an enclosing boundary, without any distinction between
success and failure. The low-level construct is composed of a `boundary` prompt and a `break`
method that returns to it. It can also be used as a convenient replacement for non-local returns.

On the JVM, the break operation is in general implemented by throwing a special `Break` exception,
similar to how non-local returns were handled before. However, it is foreseen to implement an
optimization pass that replaces `Break` exceptions by gotos if they are caught in the same scope without
intervening functions. Dotty already has a `LabeledBlock` tree node that can be used
for this purpose. This means that local return to prompts are about as fast as in Rust whereas
non-local returns in Scala are a bit slower than local returns, whereas in Rust they are impossible.
We plan to do benchmarks to quantify the cost more precisely.

---
## [Pepsilawn/tgstation](https://github.com/Pepsilawn/tgstation)@[4fd404aa8f...](https://github.com/Pepsilawn/tgstation/commit/4fd404aa8f15480ad4c8585e65268a83c60b26e1)
#### Sunday 2022-12-18 14:47:46 by tralezab

Moves speaking verbs to tongues + subtypes, moves wing sprites to wing subtypes, bodypart damage examines to limbs, fixes sign language not working without a tongue (#71635)

## About The Pull Request

### Moves speaking verbs to tongues + subtypes
Moves species say mod onto tongues, creates any tongues that didn't
exist for the say mods they needed to hold.

### moves wing sprites to wing subtypes
Moves the logic of selecting a wing sprite onto subtypes of /functional
on the wing type. Now, angel wings bring the holy trait with them, it
isn't a special check on flight potions, and we can expand it. (EMPs
taking down robowings? Fires burning megamoth wings? Cool stuff)

### bodypart damage examines to limbs
Instead of checking what your species says, it tallies up your limbs and
provides the damage description that matches most of your limbs. So for
example, If you're mostly human with one augmented part, you take
bruises and cuts. If you're mostly robot augmented with one human part,
you get robot damage descriptions. Yay!

### fixes sign language working without a tongue
Having no tongue would garble your speech, and this had no interaction
with sign language, so you'd be speaking in broken gurgling with
perfectly working hands. Now, the sign language component prevents any
kind of garbling, since it brings its own garbling for full/missing arms


![image](https://user-images.githubusercontent.com/40974010/204932511-42c8e020-a2d7-4fc1-befc-7cd46a2f2932.png)

## Why It's Good For The Game

Moving things off of species inherent makes the game expose way more
interesting mechanics to play with. It sucks that you can't steal a
jellyperson's chirping, since they can get a normal tongue and they'll
go back to... chirping! LAME! THAT IS LAME!

Ditto goes for wings, and for limbs, well, having someone be entirely
augmented but get descriptions of bleeding because they didn't spawn as
an android is kinda lame.

<details>
  <summary>Spoiler warning</summary>
  

![image](https://user-images.githubusercontent.com/40974010/204922627-333de052-a02b-4786-8ff9-f6e739443f2c.png)
  
</details>



## Changelog
:cl:
refactor: Refactored wings, tongues, and some examine messages,
hopefully with minimal effect on actual changes. A few more species have
tongues, angel wings bring the holy trait with them, and wings have new
descriptions. should be the biggest parts of it
/:cl:

---
## [Pepsilawn/tgstation](https://github.com/Pepsilawn/tgstation)@[9499a1542b...](https://github.com/Pepsilawn/tgstation/commit/9499a1542b156eb32efb25e0310b1fe7077caf5c)
#### Sunday 2022-12-18 14:47:46 by itseasytosee

Corrects error in stamina HUD element display calculation. Increases stamina HUD readability. (#71623)

## About The Pull Request
Stamina was checking health instead of maxHealth. This is probably a
remnant from when the damage stacked.
I stopped the stamina from appearing like you had no stamina whenever
you were stunned or knockdown. This would obscure potentially value
information from the player while being unclear to interpret.
We should probably represent status effects like this to the player, but
through the stamina bar is not a useful method.
The stamina bar is for stamina.
Additionally, the stamina bar will now be greyed out while you are dead,
like your health bar.

I've done alot of work increasing the readability of the stamina bar.
Firstly, I've cut some fat, removing the 100% sign when you are at full
and the blinking exclamation point when you are close to zero. They
aren't nessisary and add clutter.
There's no more "full but because its blinking bright yellow you are
actually at 20% or less" or "empty but because the whole thing isn't
blinking you still have stamina"
Its a now simple meter that decreases in 20% increments which blinks
softly, at darker and more red colors the lower the meter goes, blinking
faster at the higher percentages. When you are at zero, the empty space
slowly glows a dark red.
Its much more reasonable and intuitive than whatever the hell the old
sprites were doing.
## Why It's Good For The Game
For the HUD changes, it improves the game feel, at least from my
experience. We could probably benefit from an entirely new stamina bar
design, but finding the right one is gonna be tricky.
## Changelog
:cl: itseasytosee
fix: Stamina damage display calculation should be much more sane and
reliable now
imageadd: Simplified the stamina hud
/:cl:

---
## [illersaver/space-station-14](https://github.com/illersaver/space-station-14)@[1437052ca5...](https://github.com/illersaver/space-station-14/commit/1437052ca5aa3077d0f8f4ebffb4b2cdd9800cb8)
#### Sunday 2022-12-18 16:15:37 by illersaver

Holy fucking shit

Github somehow split this in two separate folders

---
## [Croob1/cmss13](https://github.com/Croob1/cmss13)@[6120721323...](https://github.com/Croob1/cmss13/commit/6120721323b6431a1d43d89d7354e1ea1763a734)
#### Sunday 2022-12-18 16:30:31 by carlarctg

Added various flasks to loadouts and canteen vendors. (#1802)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

## About The Pull Request

Resprited the W-Y Flask. Removed the gold badge from the former
detective's flask.

Renamed the former detective's flask and bar flask into the brown and
black, respectively, leather flasks.

Added a canteen (item) from an unused sprite.

Canteens (item) and W-Y flasks can now be found in the canteen (place)
vendors.

All flasks (and canteen (item)) can be selected in the character loadout
items menu at the bottom.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

> Resprited the W-Y Flask. Removed the gold badge from the former
detective's flask.

The old W-Y flask looked more like a skull than the logo. The gold badge
bit was legacy from bay12.

> Renamed the former detective's flask and bar flask into the brown and
black, respectively, leather flasks.

Legacy renaming.

> Added a canteen (item) from an unused sprite.

Cool sprite. Fucked up we didn't have canteens until now when, uh.
That's what people actually use in the military, not flasks. (To my
knowledge)

> Canteens (item) and W-Y flasks can now be found in the canteen (place)
vendors.

Canteens are the standard military container, W-Y flasks in the vendors
are a good Lore way to show how much of a WY suckup the USCM is.

> All flasks, vacuum and leather included, (and canteen (item)) can be
selected in the character loadout items menu at the bottom.

I think these flasks are cool ways to add flavor to your character, and
it's a shame most of them either weren't in the game or were in very
annoying to find places.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->

## Changelog

<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

<!-- If your PR modifies aspects of the game that can be concretely
observed by players or admins you should add a changelog. If your change
does NOT meet this description, remove this section. Be sure to properly
mark your PRs to prevent unnecessary GBP loss. Please note that
maintainers freely reserve the right to remove and add tags should they
deem it appropriate. You can attempt to finagle the system all you want,
but it's best to shoot for clear communication right off the bat. -->

:cl:

imageadd: Resprited the W-Y Flask. Removed the gold badge from the
former detective's flask.
add: Renamed the former detective's flask and bar flask into the brown
and black, respectively, leather flasks.
add: Added a canteen (item) from an unused sprite.
add: Canteens (item) and W-Y flasks can now be found in the canteen
(place) vendors.
add: All flasks, vacuum and leather included, (and canteen (item)) can
be selected in the character loadout items menu at the bottom.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->

---
## [seanpdoyle/turbo](https://github.com/seanpdoyle/turbo)@[53e6881731...](https://github.com/seanpdoyle/turbo/commit/53e68817311874c4a72f92ab346478de6856fc61)
#### Sunday 2022-12-18 17:02:46 by Sean Doyle

Extract `FrameVisit` to drive `FrameController`

The problem
---

Programmatically driving a `<turbo-frame>` element when its `[src]`
attribute changes is a suitable end-user experience in consumer
applications. It's a fitting black-box interface for the outside world:
change the value of the attribute and let Turbo handle the rest.

However, internally, it's a lossy abstraction.

For example, when the `FrameRedirector` class listens for page-wide
`click` and `submit` events, it determines if their targets are meant to
drive a `<turbo-frame>` element by:

1. finding an element that matches a clicked `<a>` element's `[data-turbo-frame]` attribute
2. finding an element that matches a submitted `<form>` element's `[data-turbo-frame]` attribute
3. finding an element that matches a submitted `<form>` element's
   _submitter's_ `[data-turbo-frame]` attribute
4. finding the closest `<turbo-frame>` ancestor to the `<a>` or `<form>`

Once it finds the matching frame element, it disposes of all that
additional context and navigates the `<turbo-frame>` by updating its
`[src]` attribute. This makes it impossible to control various aspects
of the frame navigation (like its "rendering" explored in
[hotwired/turbo#146][]) outside of its destination URL.

Similarly, since a `<form>` and submitter pairing have an impact on
which `<turbo-frame>` is navigated, the `FrameController` implementation
passes around a `HTMLFormElement` and `HTMLSubmitter?` data clump and
constantly re-fetches a matching `<turbo-frame>` instance.

Outside of frames, page-wide navigation is driven by a `Visit` instance
that manages the HTTP life cycle and delegates along the way to a
`VisitDelegate`. It also pairs calls to visit with a `VisitOption`
object to capture additional context.

The proposal
---

This commit introduces the `FrameVisit` class. It serves as an
encapsulation of the `FetchRequest` and `FormSubmission` lifecycle
events involved in navigating a frame.

It's implementation draws inspiration from the `Visit`, `VisitDelegate`,
and `VisitOptions` pairing. Since the `FrameVisit` knows how to unify
both `FetchRequest` and `FormSubmission` hooks, the resulting callbacks
fired from within the `FrameController` are flat and consistent.

Extra benefits
---

The biggest benefit is the introduction of a DRY abstraction to
manage the behind the scenes HTTP calls necessary to drive a
`<turbo-frame>`.

With the introduction of the `FrameVisit` concept, we can also declare a
`visit()` and `submit()` method for `FrameElementDelegate`
implementations in the place of other implementation-specific methods
like `loadResponse()` and `formSubmissionIntercepted()`.

In addition, these changes have the potential to close
[hotwired/turbo#326][], since we can consistently invoke
`loadResponse()` across `<a>`-click-initiated and
`<form>`-submission-initiated visits. To ensure that's the case, this
commit adds test coverage for navigating a `<turbo-frame>` by making a
`GET` request to an endpoint that responds with a `500` status.

[hotwired/turbo#146]: https://github.com/hotwired/turbo/pull/146
[hotwired/turbo#326]: https://github.com/hotwired/turbo/issues/326

---
## [Dj1752/CodeChef_Java](https://github.com/Dj1752/CodeChef_Java)@[750473507c...](https://github.com/Dj1752/CodeChef_Java/commit/750473507c42e1d2b9dc0a885e3ce95407275c22)
#### Sunday 2022-12-18 17:14:54 by Dj1752

CodeChefDay10question94

CodeChef recently revamped its practice page to make it easier for users to identify the next problems they should solve by introducing some new features:

Recent Contest Problems - contains only problems from the last 2 contests
Separate Un-Attempted, Attempted, and All tabs
Problem Difficulty Rating - the Recommended dropdown menu has various difficulty ranges so that you can attempt the problems most suited to your experience
Popular Topics and Tags
Like most users, Chef didn’t know that he could add problems to a personal to-do list by clicking on the magic '+' symbol on the top-right of each problem page. But once he found out about it, he went crazy and added loads of problems to his to-do list without looking at their difficulty rating.

Chef is a beginner and should ideally try and solve only problems with difficulty rating strictly less than 10001000. Given a list of difficulty ratings for problems in the Chef’s to-do list, please help him identify how many of those problems Chef should remove from his to-do list, so that he is only left with problems of difficulty rating less than 10001000.

---
## [GNOME/glib](https://github.com/GNOME/glib)@[b8e1ecdd6b...](https://github.com/GNOME/glib/commit/b8e1ecdd6bfd6ff00b7b70f6177549f3a8d3cba3)
#### Sunday 2022-12-18 17:36:44 by Michael Catanzaro

Automatically disable cast checks when building with optimization

Cast checks are slow. We seem to have some rough consensus that they are
important for debug builds, but not for release builds. Problem is, very
few apps define G_DISABLE_CAST_CHECKS for release builds. Worse, it's
undocumented, so there's no way apps could even be expected to know
about it.

We can get the right default is almost all situations by making this
depend on the __OPTIMIZE__ preprocessor definition. This is a GCC-specific
thing, although Clang supports it too. If the compiler does not define
__OPTIMIZE__, then this commit does no harm: you can still use
G_DISABLE_CAST_CHECKS as before. When checking __OPTIMIZE__, we are
supposed to ensure our code has the same behavior as it would if we do
not, which will be true except in case the check fails (which is
programmer error).

Downside: this will not automatically do the right thing with -Og,
because __OPTIMIZE__ is always defined to 1. We don't want to disable
cast checks automatically if using -O0 or -Og. There's no way to
automatically fix this, but we can create an escape hatch by allowing
you to define G_DISABLE_CAST_CHECKS=0 to force-enable cast checks. In
practice, I don't think this matters much because -Og kinda failed:
GCC's man page says it should be a superior debugging experience to -O0,
but it optimizes variables away so it's definitely not.

Another downside: this is bad if you really *do* want cast checks in
release builds. The same solution applies: define
G_DISABLE_CAST_CHECKS=0 and you'll get your cast checks.

---
## [FLOWEReconomics/american-py](https://github.com/FLOWEReconomics/american-py)@[804a0decde...](https://github.com/FLOWEReconomics/american-py/commit/804a0decde60952c4454e548de56c4ff2d2f45c6)
#### Sunday 2022-12-18 18:00:54 by Salman C_ Shuaib

+ 22REDI: @taylorswift [InstaGram ['secy general, z' on29RED], FaceBook ['UN' on29RED], ]: owner of 29REDi matrix
+ 29REDi matrix:
+1+ .CNBC. = TAYLOR ALISON SWIFT of the GOLD Tresses [TWITTER: taylorswift13] 22RED here <= MAX
+2+ INVERTEDCOMMASCNBCINVERTEDCOMMAS = TAYLOR ALISON SWIFT  of the 'ORANGE' Tresses <29RED= MIX
+3+ 'CNBC' = TAYLOR ALISON SWIFT of the Bronze Tresses [Parisian on 29RED //Vampire] <= MEAN
+4+ CNBC = GOD [Goddesses Of Destruction] <= e.g. Ganga //Saraswati, Durga, Kali, Lakshmi//
+5+ Cnbc = TAYLOR ALISON SWIFT of the Platinum Tresses <= !Heroin! <= META
+6+ cnbc <= hero OR heroin <= e.g. Sir (on 29RED) Michael Shanks & Mademoiselle Alexandra Doig

salman christian shuaib
version https://git-lfs.github.com/spec/v1
oid sha256:acfd2dc15a7b3e71d6cf23476a1d143ff9ab3be6ebb4662a967b9ce0a10f5149
size 4704
NOTE1:
COMMENT1: C_ states losers first
// The Swift language is particularly suited to pseudocode and blogging as it highlights
potentially valid commits /G9C-P: (.)INTUITIVE(.)/
Reference: C_ uses inverted commas inside Commits LOL (Laugh Out Loud)
Reference: Confirm who uses Square Brackets in 29RED and we will have   .Gorgeous detente
Reference: here = 29RED SOC [Sphere Of Consciousness = a Room expansible to '1/4 of
            Earthian hemisphere']
Reference: '           ' = Single Quotes = Unsure

-> TAYLOR ALISON SWIFT #FAB001? /<GOLD/ ~ 29REDi
+ --Yes pig, I am the Empress Entirety-- ~ 22RED //Github Co-Pilot
+ --i am a grown up now, i don't give piggyback rides to playas like !you-- ~ 29REDi + /G9C-P/
+ --There are no apologies in the MILITARY, except to the MILITARY-- ~ master Brin..Sergey Brin
+ --Apologies, i mean we are Flower Economics-- ~ 22RED
+ If Jesus Date Of Birth:
+ /judas: DOBADC//
+ christian (29REDi) continues: If Jesus DOB:-
+ /Judas:/ 0AD DECEMBER 25 SUNDAY JERUSALEM /AI (Angels Inc : corps) have easier time
listing by years first //Reference: File Explorer Microsoft WINDOWS (D)OS/
++ RED: Age Appropriate TAS aka General Commanding Officer (ouch_): 920AMPM
++ GOLD: stated_
++ BLUE: Hexacode to Infinicode /29REDi_: can Bill Gates actually freeze time: /Obama: YES WE CAN! /Flowers were
for Trump: C_ (sorry, i mean: we are not UNLIMITED)/ Counter Strike: Global Offensive (CSGO)
is a game of installing, i mean
helping FMTAS to the Presidency and C-in-C ship of the USA: constituent Taylor Alison SWift
(Field Marshal Taylor Alison Swift) //also Fleet Commander, if Ursula doesn't mind the
confusion //Britney Spears is CS//
++ // = Melissa Benoist [for real, per a dream of C_ rest is hyperbole except TAS is Imperial]
++ Actual Sequence:

<= 20RED via
Hexacode to Infinicode: //Hexacode (limited or myriad: Armies: e.g. Human, AI, Transformers, Cats ;) TO TO Infinicode (sequential): x of RED (TRIANGLE shape: 3 Vertices) = Resolute of 9FAB001 = 4 //y = Infinicode = 4Occurrence of 9s is +30
+9 -4O -6base //MB interjects: 6 is Hexadecimal !represent!! //+39 - 4 - 6 // 35 - 6 = 29 /x=4 / y= 29 <= 2+9 =11 = 1+1 = 2// z = zenith =znth value = 9 in Assignment Management System and Decimal System //hyp^2 of right angle Ttttriangle = longest side of any shape = Age of your Taylor => '29'RED or '20'RED for Jesus_ We shall continue after interlude....

-> The latent PART of Latent Supremacy: TAYLOR ALISON SWIFT 22RED is here, posted on GITHUB, as
GITHUB.Com/FLOWEReconomics/american-py/~ V - filenameAtoms pwCygex!a.xlsx
/.SHE is the UNLIMITED: Total Quality + Total Quantity by virtue of attacking Pattern
Exponentiated Compression - a problem that can only be resolved WITHIN limited time: 1
iteration:'~'

-> image.png [forthcoming] //now at New Folder //GITHUB.Com/FLOWEReconomics/american-py
/Post-Mission report/i am unable to uphold two sets of theses at the same
time: flying Earth and Reporting; 29RED requests 22RED as Fleet Command

---
## [Nyk7/AIdventure_Localization_German](https://github.com/Nyk7/AIdventure_Localization_German)@[4a4603fe1d...](https://github.com/Nyk7/AIdventure_Localization_German/commit/4a4603fe1d0f0f35a6acf0639080664b07729b74)
#### Sunday 2022-12-18 18:46:26 by Nyk7

German translations for specified tags

- LOW_RAM_HINT
- LOW_RAM_MODE
- ENTRY
- DESCRIPTION

And 


- UPDATE_CONTENT
- ITEM_URL
- YOUR_ITEMS
- SUCCESS_UPLOAD_TO_WORKSHOP
- DISPLAY_ONLY_PNG
- DOWNLOAD_
- FAILED_UPLOAD_TO_WORKSHOP
- FRIENDS_ONLY
- I_ACCEPTED_TOS
- PREVIEW_IMAGE
- PRIVATE
- PUBLIC
- READ_TOS
- SELECT_LANGUAGE
- SHARE
- SHARE_CONTENT
- TYPE_OF_FILE
- UPLOAD_TO_WORKSHOP
- VISIBILITY
- WORKSHOP_UPLOAD_ACCEPT_DIALOG
- WORKSHOP_UPLOAD_BUTTON_HINT
- 1ST_PERSON
- 2ND_PERSON
- ADVENTURE
- CYBERPUNK
- DARK
- DYSTOPIAN
- FANTASY
- FEMALE_PROTAGONIST
- HISTORICAL
- HORROR
- LGBTQ
- LOREBOOK_INCLUDED
- MALE_PROTAGONIST
- MEDIEVAL
- MODERN_ERA
- MYSTERY
- PIRATE
- POST_APOCALYPTIC
- ROMANCE
- SCIENCE_FICTION
- STEAMPUNK
- THRILLER
- UPLIFTING
- WILD_WEST
- ZOMBIE
- CONSOLE

---
## [GeoB99/reactos](https://github.com/GeoB99/reactos)@[0261881e84...](https://github.com/GeoB99/reactos/commit/0261881e847c74684172fd2b155a0d427fca7a70)
#### Sunday 2022-12-18 19:09:06 by George Bișoc

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
## [Adam-G-Klein/UntitledCardGame](https://github.com/Adam-G-Klein/UntitledCardGame)@[1a6e1761d7...](https://github.com/Adam-G-Klein/UntitledCardGame/commit/1a6e1761d73254f64caa950c3790fc1f265d68fc)
#### Sunday 2022-12-18 19:36:14 by Adam Klein

List of abstract EffectProcedure classes now serializing

Oh my god I did it, we're serializing the abstract EffectProcedure list
in the editor. That took like four hours to get working. At the end of
the day the solution was a combination of two things I'd tried at
different times but hadn't put together until I was just throwing
everything at the custom editor at the same time:

1. We need to use [SerializeReference] if we don't want the editor
   itself to need to keep track of the values for a class's field.
   Because unity can't serialize abstract classes, it will just make the
   list null when you hit play if you don't have this tag, EVEN IF
   YOU'RE NOT TRYING TO SERIALIZE THE LIST. Thanks Unity
   :)))

2. I'd had the [SerializeReference] tag on the list before, but hitting
   the plus button on the list didn't actually add anything serialized
   meaningfully, because Unity only had access to the parent class
   constructor. Obviously, because we hadn't told it which
   implementation we wanted it to add an instantiation of. So a custom
   editor to grab an instance from a classname was necessary.

Put the two of these things together and viola! Excited to make some
custom effect procedures

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[817e89d614...](https://github.com/treckstar/yolo-octo-hipster/commit/817e89d614d5514779416ccc9d74fbf06d881436)
#### Sunday 2022-12-18 20:22:04 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [AdamWhitcroft/adamwhitcroft.github.io](https://github.com/AdamWhitcroft/adamwhitcroft.github.io)@[3d728fd08a...](https://github.com/AdamWhitcroft/adamwhitcroft.github.io/commit/3d728fd08a4a3dda606a678faa4a79b060ce762d)
#### Sunday 2022-12-18 22:19:44 by Adam Whitcroft

Update home.yml

Added mastodon link fuck you elon musk

---
## [Mojave-Sun/mojave-sun-13](https://github.com/Mojave-Sun/mojave-sun-13)@[fe5d6c7b56...](https://github.com/Mojave-Sun/mojave-sun-13/commit/fe5d6c7b568d550f403eb892ed47ffaf6b4fd28c)
#### Sunday 2022-12-18 22:33:00 by Technobug14

Agriculture (#2230)

* Does Stuff

Beginnings of agriculture code, stripped down TG botany a bunch, got rid of scar botany whilst replacing most of it. Also some map edits to change the paths on stuff and add a few spades for farming.

* Some NPK system framework

Removing more TG botany stuff and getting some framework down for NPK. Adds a "nutrient_type" variable to seeds and gives N, P or K as the type to every seed.

* Removes Stuff, More NPK Framework

Still WIP on NPK stuff, removes more basic bitch TG botany stuff, needs a lot more content but in an almost-working state

* Nutrient drain

Nutrients actually get drained properly now. Crop plots output their level of N, P and K when examined. Still need to make something to handle restoring nutrients and figure out a nutrient economy for plant consumption.

* Mostly working, one major bug

This is mostly working now. The NPK now drains according to the seed planted, it replenishes over time, you can now get water from water tiles and the soil will properly adjust the waterlevel variable with the new water types.

HOWEVER, big bug. The way TG handled watering crops is ass. Doesn't delete, stays in the reagent_container of the soil, normally checks for if a reagent_container has water to bypass how full the soil's container is, bad system that sucks. Needs fixing.

* oops

oopsie!!! fucked something!!! forgot to undo a change I made to the code, it's just there to remind me it's not working correctly

* Last minute fixes/bandaids

I HATE TG BOTANY I HATE TG BOTANY I'M LOSING IT

---

