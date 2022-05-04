## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-05-03](docs/good-messages/2022/2022-05-03.md)


1,791,332 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,791,332 were push events containing 2,875,064 commit messages that amount to 215,450,994 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [jwhonce/podman](https://github.com/jwhonce/podman)@[e74717f348...](https://github.com/jwhonce/podman/commit/e74717f348c2768b87cad7dd6997c42dc85fc50a)
#### Tuesday 2022-05-03 00:20:47 by Ed Santiago

Treadmill script: revamp

Major revamp: instead of stacking a vendor commit on top of
the treadmill changes, do it the other way around: vendor,
then apply treadmill diffs.

Reason: the build-all-new-commits test. Sigh. It fails in the
common case where our treadmill changes include a new struct
element in cmd/podman/images/build.go

Why this is good: well, superficially, it's more intuitive.

Why this is horrible: omg the rebasing games are a nightmare.
When the vendor commit is on top (HEAD), it's ultra-trivial
to drop it, rebase the treadmill changes on main, then add
a new vendor-buildah commit on top. As you can see from the
diffs in this PR, treadmill-as-HEAD introduces all sorts
of complex dance steps in which things can go catastrophically
wrong and you can lose all your treadmill patches. I try very
hard to prevent this, and to offer hints if there's a problem,
and heck in the worst case it's still git so it's still possible
to find lost commits... but it's still much riskier than the
old way.

Alternative I considered: using sed magic to disable the
build-all-new-commits test. So tempting... but that would
also disable the bloat check.

Signed-off-by: Ed Santiago <santiago@redhat.com>

---
## [SoSMaster9000/tgstation](https://github.com/SoSMaster9000/tgstation)@[50689f89a4...](https://github.com/SoSMaster9000/tgstation/commit/50689f89a40e5e7a2732a0c5fb38c787b69f7d28)
#### Tuesday 2022-05-03 01:17:19 by LemonInTheDark

Action button refactor/rework: Enhanced Dragging (#65180)

About The Pull Request

I noticed a lot of strange and un-intuitive behavior in action buttons, and got stung by the bloat bug. Damn it hug #58027
I'll do my best to explain what I've changed and why, might get a bit long.
If you want a better idea, read the commits. Most of em are pretty solid, if long.

Whelp. Here we go.
How do action buttons currently work

All action buttons are draggable, to any place on the screen. They're held in an actions list on the player's mob.
Their location in this list determines their position on the top of the screen. If one is dragged away from the top, its position in the list is "saved". This looks really bad.
If two buttons are dragged over each other, their positions swap. (inside the actions list too)
If a button is shift clicked, it is brought back to the position it started at.
If the action collapse button that you likely just mentally edit out is alt clicked, it resets the position of all action buttons on the screen.
If an action is ctrl clicked, it is "locked". This prevents any future position changes, and also enables a saving feature. With this saving feature, locked button positions persist between rounds. So your first o2 canister will always start where you saved it, etc.
Actions and buttons are a one to one link. While there is functionality to share action buttons between two players, this means showing the same object to both. So one player can move a button on another's screen. Horrendous.
This also makes code that modifies properties of the screen object itself very clunky.
Why is this bad

A: None knew pretty much any of this information. It is actually documented, just in a horribly formatted screen tip on the collapse button, you know the one we all mentally delete from the hud.
B: None of this is intuitive. Dragging buttons makes the hud look much worse, and you get no feedback that you even can drag them. Depressing
C: We use actions to make new options clear to the player. This means players can have a lot of action buttons on the hud. This gets cluttery
D: The collapse button is useless. It lets you clear your screen if someone like me fucks up and gives you 2000 actions, but outside of that it just hides all information from you. You never want to see none of your action buttons, just a filtered list of them.
E: On a technical level, they're quite messy, and not fully functionally complete. This is depressing.
What I've done

Assuming the above to be true, how do we fix them?
Well first I'm going to go over everything I changed, including links to major commits. I'll then describe the finished product, and why I made the decisions I did.

Oh and I've moved some of the more niche or technical discussion to dropdowns. Hopefully this makes finding the major functional changes easier

Adds helper procs for turning screen_loc strings into more manageable arrays. This doesn't fully support all of the screen_loc spec, but it's enough for what I'm doing. (f54865f)

Uses these helper procs to improve existing code (6273b93)

Fixes an issue with tooltip code itself. If you tried to hold down a mouse button while dragging onto a tooltip enabled object, it would silently fail. The js made assumptions about the order args came in, which broke when buttons were held down (e0e42f6)

Adds a signal linked to /client/Click(). Surprised we didn't have this before honestly (c491a4a)

Makes /client/MouseDrag() return parent. If we don't do this, any overrides of MouseDrag will never actually be called (2190b2a)
Refactors how action buttons work under the hood (53ccce2)
Basically, rather then generating one button per action, we generate one button per viewer

Starts to change button behavior, more cleanup

Changes the mouse cursor when an action button is dragged. Hopefully
this makes moving things feel less like an accident, and makes you doing
it more clear

Removes the moved and locked vars. This will be more relevant later, but
for now:

Moved exists as a sort of budget "We've been dragged" variable. We can
handle this more cleanly, and the movable type doesn't care about it

Locked is a very old variable that is also not something that the
movable type "owns". It's more an action button thing that's been moved
down.
It exists so an action can be locked in place, and in that locking, be
treated as a "saved location"
(21e20fc)

Because I've nuked move, we don't need to directly set our button's
position. We can use the default_button_position var instead. This is
quite handy.

Please ignore position_action, I will explain that later
(83e265e)

Removes the buttons locked pref

It was another obscure part of action buttons, basically do buttons
start "locked" or not. See previous discussion of locked
(b58b1bd)

Major rework starts here

Alright. Sorry for this, this is where me not commiting regularly starts
to suck. I'll do my best though.

Rather then figuring out an action button's position via a combination
of the moved and ordered vars, we use a separate location var to store
one of a few defines. This makes life later much easier.

Adds tooltip support for dragging action buttons. The way the tooltip
just froze in place when dragging really bugged me, and lead to some
nasty visual artifacts.
This is a bit messy because the drag procs are horrible, but it's
workable

Dropping a button on another button will no longer swap their positions
Behavior instead depends on the target button.

If it's a part of a group (A concept I will explain later) the dragged
button is simply inserted before it in the group's list.

If it's floating on the general hud, we instead position the dragged
button to its right. There's extra logic here to ensure buttons will
never overflow the screen, but I'll get into that later.

Alright. That's most of the refactoring. Time for the larger behavior
changes.

Adds a button palette. This is a separate dropdown that renders
underneath buttons.

image

The idea is to allow for a conceptual separation between "important"
buttons and the ones that end up cluttering the screen.

You can click on the dropdown to open it, then any later clicks that
don't involve actions in some way will autoclose it.

My goal is to come up with an alternative for the action button that
just acted as a way to hide all buttons on screen. Not convinced it saw
much use.

As a side effect of removing that, I've moved its tooltip stuff to the
palette. I've properly formatted it, so hopefully it's easier to read
then the jumble that we used to have.

(You can alt click the palette button to reset all button positions)

Oh and the palette can scroll, since as you'll see later it has a
limited size.
image

Moving on from that, I've added what amounts to action landing buttons.
These allow buttons to rejoin groups, or be positioned at the end of a
line of buttons.
image

They've got a 32x32 hitbox, and only show up when dragging. Hopefully
this makes the system more clear just by dragging an action.

Oh and I've changed how button position updating works. The old system
of calling update_action_buttons on mob every time an action button
changes position is gone, mostly because I've setup more robust
grouping. Will discuss when I get to huds

(0d1e93f)
Adds the backbone behind action button position changes (94133bd)

Moves hud defines to the global folder, safer this way (7260117)

Adds color changing to the palette button, giving some heads up for buttons being inserted into the palette automatically
image
image
Ensures a landing button is always shown, even if it needs to break the
max row rule
Makes palettes auto contract if they have no buttons inside them
Prevents palettes from being opened if they have no buttons inside them
(f9417f3)
How it looks
2022-02-26.02-30-10.mp4
Why It's Good For The Game

Players have more control over the clutter on their screen.
Buttons are available, but not in the way,
Since any player move of a button saves it, any lack of clarity in the way buttons work will be forced out by buttons not just resetting when a new game starts.
We don't overlap any existing screen elements, unless the upper button list gets really long.
The code is much less crummy (I think, may have made it worse it's hard for me to judge my own work)

If it ends up not being as usable as I'd like, I'll rip out the existing changes and just implement the qol and backend stuff. I think it's worth doing though.
Changelog

cl
add: Expanded heavily on action buttons
add: Adds an action button dropdown that sits just under the normal list in the top left. You can drag new buttons onto it to insert them. Click on it to show its contents, do what you want to do, then click again anywhere to contract it. Alt click it to reset all button positions
add: Action buttons will now remember their position between rounds. So if you really like your flashlight right next to your player for some reason, we support that now
add: When you start to drag an action button, docking ports will appear in places that it can be inserted into. (Outside of just floating somewhere on your screen of course)
del: Removed action button locking, and the associated preference. I'm reasonably sure literally none uses this, but if you do hit me up
qol: Dragging an action button will now give you an outline of its size around your cursor
fix: You can no longer cause the screen to expand by putting an action button on the edge of widescreen, and then resizing to standard.
refactor: Refactors action and button code significantly. lots of little things.
/cl

---
## [greenforce-project/kernel_xiaomi_citrus_sm6115](https://github.com/greenforce-project/kernel_xiaomi_citrus_sm6115)@[5cd5d957d0...](https://github.com/greenforce-project/kernel_xiaomi_citrus_sm6115/commit/5cd5d957d0d89c6f277461e2a54e7ffb1a1ee08c)
#### Tuesday 2022-05-03 01:18:57 by George Spelvin

lib/sort: make swap functions more generic

Patch series "lib/sort & lib/list_sort: faster and smaller", v2.

Because CONFIG_RETPOLINE has made indirect calls much more expensive, I
thought I'd try to reduce the number made by the library sort functions.

The first three patches apply to lib/sort.c.

Patch #1 is a simple optimization.  The built-in swap has special cases
for aligned 4- and 8-byte objects.  But those are almost never used;
most calls to sort() work on larger structures, which fall back to the
byte-at-a-time loop.  This generalizes them to aligned *multiples* of 4
and 8 bytes.  (If nothing else, it saves an awful lot of energy by not
thrashing the store buffers as much.)

Patch #2 grabs a juicy piece of low-hanging fruit.  I agree that nice
simple solid heapsort is preferable to more complex algorithms (sorry,
Andrey), but it's possible to implement heapsort with far fewer
comparisons (50% asymptotically, 25-40% reduction for realistic sizes)
than the way it's been done up to now.  And with some care, the code
ends up smaller, as well.  This is the "big win" patch.

Patch #3 adds the same sort of indirect call bypass that has been added
to the net code of late.  The great majority of the callers use the
builtin swap functions, so replace the indirect call to sort_func with a
(highly preditable) series of if() statements.  Rather surprisingly,
this decreased code size, as the swap functions were inlined and their
prologue & epilogue code eliminated.

lib/list_sort.c is a bit trickier, as merge sort is already close to
optimal, and we don't want to introduce triumphs of theory over
practicality like the Ford-Johnson merge-insertion sort.

Patch #4, without changing the algorithm, chops 32% off the code size
and removes the part[MAX_LIST_LENGTH+1] pointer array (and the
corresponding upper limit on efficiently sortable input size).

Patch #5 improves the algorithm.  The previous code is already optimal
for power-of-two (or slightly smaller) size inputs, but when the input
size is just over a power of 2, there's a very unbalanced final merge.

There are, in the literature, several algorithms which solve this, but
they all depend on the "breadth-first" merge order which was replaced by
commit 835cc0c8477f with a more cache-friendly "depth-first" order.
Some hard thinking came up with a depth-first algorithm which defers
merges as little as possible while avoiding bad merges.  This saves
0.2*n compares, averaged over all sizes.

The code size increase is minimal (64 bytes on x86-64, reducing the net
savings to 26%), but the comments expanded significantly to document the
clever algorithm.

TESTING NOTES: I have some ugly user-space benchmarking code which I
used for testing before moving this code into the kernel.  Shout if you
want a copy.

I'm running this code right now, with CONFIG_TEST_SORT and
CONFIG_TEST_LIST_SORT, but I confess I haven't rebooted since the last
round of minor edits to quell checkpatch.  I figure there will be at
least one round of comments and final testing.

This patch (of 5):

Rather than having special-case swap functions for 4- and 8-byte
objects, special-case aligned multiples of 4 or 8 bytes.  This speeds up
most users of sort() by avoiding fallback to the byte copy loop.

Despite what ca96ab859ab4 ("lib/sort: Add 64 bit swap function") claims,
very few users of sort() sort pointers (or pointer-sized objects); most
sort structures containing at least two words.  (E.g.
drivers/acpi/fan.c:acpi_fan_get_fps() sorts an array of 40-byte struct
acpi_fan_fps.)

The functions also got renamed to reflect the fact that they support
multiple words.  In the great tradition of bikeshedding, the names were
by far the most contentious issue during review of this patch series.

x86-64 code size 872 -> 886 bytes (+14)

With feedback from Andy Shevchenko, Rasmus Villemoes and Geert
Uytterhoeven.

Link: http://lkml.kernel.org/r/f24f932df3a7fa1973c1084154f1cea596bcf341.1552704200.git.lkml@sdf.org
Signed-off-by: George Spelvin <lkml@sdf.org>
Acked-by: Andrey Abramov <st5pub@yandex.ru>
Acked-by: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Reviewed-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>
Cc: Rasmus Villemoes <linux@rasmusvillemoes.dk>
Cc: Geert Uytterhoeven <geert@linux-m68k.org>
Cc: Daniel Wagner <daniel.wagner@siemens.com>
Cc: Don Mullis <don.mullis@gmail.com>
Cc: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Yousef Algadri <yusufgadrie@gmail.com>
Signed-off-by: Panchajanya1999 <panchajanya@azure-dev.live>
Signed-off-by: Forenche <prahul2003@gmail.com>
Signed-off-by: Little-W <1405481963@qq.com>

---
## [relativehysteria/naga](https://github.com/relativehysteria/naga)@[b245fece44...](https://github.com/relativehysteria/naga/commit/b245fece443d4cdb90d867810b58da0cfc9dde30)
#### Tuesday 2022-05-03 01:30:16 by relativehysteria

Command testing or something like that

i fucking hate discord holy fucking shit this thing is annoying as fuck
you can't even imagine how painful this is

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[f6ce903dea...](https://github.com/Paxilmaniac/Skyrat-tg/commit/f6ce903deade160357e23b927d376851f0dbdd2c)
#### Tuesday 2022-05-03 01:46:43 by SkyratBot

[MIRROR] Makes glass floors override platings. Fixes glass floor openspace bug. [MDB IGNORE] (#13226)

* Makes glass floors override platings. Fixes glass floor openspace bug. (#66301)

About The Pull Request

Fixes #63868. Actual one liner fix for this one here. If this pr dies feel free to atomize this one.
AND it turns out to not be tim's fault.

Fixes #63548. But i really shouldnt say fixed. The original implementation was causing the invincible plating bug. When tim's refactor got in it instead relies on the element state, which was broken from the get go, removing the invincible plating bug which was in a sense "intended" its all messy man I hate this code. Thats why im removing the plating thing. Let the turf handle the turf change themselves this complicates things.

Mapped in glass floors have openspace (now baseturf bottom) as their baseturfs, while built ones have plating under them. Which doesnt make sense to be honest. Why would things be visible if a plating is under the glass. They are also crowbarrable on top of this, which to be fair is my main reasoning behind the PR.

To solve this, I am instead making glass floors replace the plating instead of building over it. This is made to be generalizable for every tile in game, as long as their initial baseturf is the same and the tile wants it to happen.

do after of three seconds is completely arbitrary. If any maint want it changed let me know.
Why It's Good For The Game

First one solves a bug
Second one makes more sense
And er, icebox is currently using the glass floors in sec, they can be crowbarred very easily. This might be a good idea from a gameplay perspective.
Changelog

cl
del: Removed adding glass floors to plating
balance: Allows you to replace plating with glass floors instead. 3 second timer.
del: Removed deconstructing the glass floors. No replacement for this one, use a rcd.
fix: Fixed metastation glassfloor spawning a weird turf when crowbarred.
/cl

* Makes glass floors override platings. Fixes glass floor openspace bug.

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [xproot/WinBot](https://github.com/xproot/WinBot)@[d6aea48c10...](https://github.com/xproot/WinBot/commit/d6aea48c10f993efe675eb53870f8052e9b1265a)
#### Tuesday 2022-05-03 02:25:19 by Cam K

FUCK YOU DISCORD
Shitcord... HOW IS IT POSSIBLE TO BE **THIS** INCOMPETENT WHEN IMPLEMENTING A VERY BASIC API FUNCTION!?!?!?!?!?!??!

---
## [san7890/bruhstation](https://github.com/san7890/bruhstation)@[67bbcf3208...](https://github.com/san7890/bruhstation/commit/67bbcf3208d75f2a54776c11ad33e0b01fe2bfa7)
#### Tuesday 2022-05-03 02:33:18 by san7890

Menage A Trois - Putting IceBoxStation In One DMM

Hey there,

I got it to work. I thought something would horribly break. However, nothing did. Not a peep out of runtimes, and cave generator appears to have worked flawlessly. I'm astounded, maybe I just did everything right, or maybe there's a deep demon lurking underneath the surface. Irregardless, it works:tm:.

There is a new annoying thing where you must click up twice in StrongDMM to get up to the "Station" level of IceBox, but such is the price we pay for being able to visualize everything in one window.

---
## [Fennec82/ChaosStation-YW](https://github.com/Fennec82/ChaosStation-YW)@[b31a49844d...](https://github.com/Fennec82/ChaosStation-YW/commit/b31a49844d613edc4f91fab89939d4dc58d3cb22)
#### Tuesday 2022-05-03 02:36:04 by Fennec82

More dogborgs!

(I think I'm obsessed with them)

Adds framework for cargo-hound once work on the delivery gut wraps up upstream [If ever]. Also adds in a crisis dogborg module. With 3 sleepers and a taser unit when hacked. Awesome.

[Note: Had to add taser sprite to Widerobot_med_vr. Just so, you know...]

---
## [toyamaza/acts](https://github.com/toyamaza/acts)@[6e1fd31474...](https://github.com/toyamaza/acts/commit/6e1fd314745ae31eaddd8db8f0454b88a9aa60fa)
#### Tuesday 2022-05-03 03:25:07 by Stephen Nicholas Swatman

feat: Implement a new orthogonal range search seed finder (#904)

As I said in #901, I have been playing around with seed finding a little bit lately. Last weekend, I mentioned an idea for a new (?) kind of seed finding algorithm based on range search datastructures, and this is the very, very first semi-working implementation of it, just before the weekend.

The idea behind this algorithm is relatively simple. In traditional seedfinding, we check a whole lot of candidate spacepoints to see whether they meet some condition. If you look at this differently, each spacepoint defines a volume in the z-r-φ space, which contains any spacepoints it can form a doublet with. What if we reversed this logic? What if we defined this volume first, and then just extract the spacepoints inside of that space? That way, we can vastly reduce the number of spacepoints we need to look at.

How do we do this quickly? With [_k_-d trees](https://en.wikipedia.org/wiki/K-d_tree). These data structures are cheap to build, and they give us very fast orthogonal range searches. In other words, we can very quickly look up which of our spacepoints lie within an axis-aligned orthognal n-dimensional hyperrectangle. In this case, which spacepoints lie within a z-r-φ box.

So, the core idea of this seedfinder is to define as many of our seedfinding constraints in orthogonal fashion. That way, we can make our candidate hyperrectangle smaller and smaller. The tighter the constraints we can place, the better. Then, we look up the relevant spacepoints, and we can avoid looking at any others. That also means this solution requires no binning whatsoever.

## Constraint conversion

Currently there are quite a few constraints in the code. Here is my status update on how well it is going to convert each of them. In some cases, we can define a weaker version of the constraints in orthogonal fashion. This is still very powerful, and it doesn't actually lose us any efficiency (because we can always check the tighter constraint in a non-orthogonal way later, not a problem)!

### Unary constraints

Currently, I am not aware of any unary constraints in the Acts seed finding code. That is to say, logic to determine whether a point is allowed to be a lower spacepoint. However, I have the following thoughts about introducing some:

* I believe the binning code does some kind of magic to determine whether a spacepoint can be a lower spacepoint. Since my solution doesn't use any binning, I don't have access to this just yet. However, if we can incorporate this logic it could be very powerful.
* Maximum single-point η: we currently have some checks in place to see if the pseudorapidity of particles is not too high. We could realistically use this maximum pseudorapidity, combined with the collision region range to constrain the bottom spacepoints.

### Binary constraints

These are the existing binary constraints on spacepoint duplets:

Constraint | Description | Orthogonalization
-|-|-
Minimum ∆r | Ensure that the second spacepoint is within a certain difference in radius | Full
Maximum cot θ | Ensure that the pseudorapidity of the duplet is not too high | Unsuccessful
z-origin range | Ensure that the duplet would have originated from the collision point | Weakened 
Maximum ∆φ<sup>1</sup> | Ensure that the duplet does not bend too much in the x-y plane | Full

<sup>1</sup> This check does not exist explicitly in the existing seed finder, but is implicit in the binning process.

### Ternary constraints

There are a lot of ternary constraints (to check whether a triplet is valid):

Constraint | Description | Orthogonalization
-|-|-
Scattering angle | ??? | Unsuccessful
Helix diameter | Ensure the helix diameter is within some range | In progress
Impact parameters | Ensure the impact parameters are close to the collision point | In progress
Monotonic z<sup>1</sup> | Ensure that z increases or decreases monotonically between points | Full

<sup>1</sup> This check does not exist in the existing seed finder, check #901.

There are also constraints defined in the experiment-specific cuts, and the seed filter, and in other places. If we could convert some of those to orthogonal constraints the implementation would become much more powerful. However, I don't really understand what is happening in those files just yet. Need more reading.

## Current performance

The current performance of this seedfinder is... Complicated. On my machine, it runs a 4000 π<sup>+</sup> event in about 5 seconds, three times slower than the existing seedfinder. Its efficiency is much higher though, and the fake rate is much lower. So that's something. However, that is in part because I am creating far more seed candidates, so take this with a big grain of salt.

## Potential gain

There are two ways that I can think of to use this kind of algorithm. The first is an inside-to-outside algorithm, where we pick a lower spacepoint first, check the space it defines for a middle spacepoint, and then check the space the two of them define for a third spacepoint. This algorithm has time complexity 𝒪(_n_<sup>3</sup>), and it has space complexity 𝒪(_n_). Due to the constants, I still believe this implementation can outperform the 𝒪(_n_<sup>2</sup>) existing algorithm, however.

The second way would be to construct a set of duplets using this logic, and then to fit those together like we do with traditional seedfinding. This has 𝒪(_n_<sup>2</sup>) time complexity like the existing code, but also space complexity 𝒪(_n_<sup>2</sup>).

## Things that are completed

* The implementation of the _k_-d tree seems to work very well, and it is quite fast.
* Basic seedfinding using this strategy is functional.

## Things that don't work yet

* My maximum ∆φ constraint does not cross the 2π boundary yet.
* I used the existing seedfinding algorithm as a stepping stone, which I have completely destroyed in the process. Obviously I do not intend on keeping it that way, and the existing algorithm will be restored to its full glory.
* Lots more.

## Things that can be improved

* Add more constraints, and tighten existing ones.
* Lots of things, pretty much everything. But I really want to go home for the weekend, so I will write this part next week.

---
## [hosja83/software-development-curriculum](https://github.com/hosja83/software-development-curriculum)@[9c740aacfa...](https://github.com/hosja83/software-development-curriculum/commit/9c740aacfa82b3abb39345c2f6fe042c271ca711)
#### Tuesday 2022-05-03 03:27:54 by BMT-z

Add section for warnings about branch diversions

From personal experience and what I've seen in the git-help channel it seems like a few people are struggling with the issue of branch diversion, I'm still doing the html foundations and didn't realize making changes to my readme file via GitHub would cause the branch diversion issue, I think in git basics it should state that making any changes to your files via GitHub can cause issues and if you want to change even the readme file it's best to do it via a commit and push, I'm aware this is covered later on but i still believe making this a note in the git basics section would help a lot of users from running into this issue.

---
## [classified/android_kernel_oneplus_sm8150](https://github.com/classified/android_kernel_oneplus_sm8150)@[2c66467b1a...](https://github.com/classified/android_kernel_oneplus_sm8150/commit/2c66467b1a9b4bbfa818f79b3d69b4f761c2e072)
#### Tuesday 2022-05-03 04:51:23 by alk3pInjection

drm: Handle dim for udfps

* Apparently, los fod impl is better than udfps cuz it
  has onShow/HideFodView hook, which allows us to toggle
  dimlayer seamlessly.

  Since udfps only partially supports the former one,
  we'd better kill dim in kernel. This is kinda a hack
  but it works well, bringing perfect fod experience
  back to us.

Co-authored-by: Art_Chen <Chenxy0201@qq.com>
Signed-off-by: alk3pInjection <webmaster@raspii.tech>
Change-Id: I80bfd508dacac5db89f4fff0283529c256fb30ce

---
## [Weblure/Skyrat-tg](https://github.com/Weblure/Skyrat-tg)@[cd2bd18cf8...](https://github.com/Weblure/Skyrat-tg/commit/cd2bd18cf8193c7cfc2f0014ef449baa8792aad4)
#### Tuesday 2022-05-03 05:49:50 by SkyratBot

[MIRROR] Creates Linters for (bad) Commented Out Lines in Maps [MDB IGNORE] (#12543)

* Creates Linters for (bad) Commented Out Lines in Maps (#65888)

* Creates CI Linters for Commented Out Lines in Maps

Creates Linters for (bad) Commented Out Lines in Maps

Hey there,

This PR is made because what happened in #65837 was fucking horrible awful shit that I'm still dealing with a few days after I fixed it. This _should hopefully_ add a new linter for commented out lines of code in a .DMM file, and HOPEFULLY doesn't flag the commented line that prevents unwanted TGM > DMM conversion.

As a proof to see if it works, I'll be adding a comment to Line 2 of IcemoonUnderground_Above.dmm. Hopefully, on the first CI check, it'll fail. I'll remove that line so it doesn't make its way into production (it will suck).

* Creates Linters for (bad) Commented Out Lines in Maps

Co-authored-by: san7890 <34697715+san7890@users.noreply.github.com>

---
## [Glonee/book_management_system_frontend](https://github.com/Glonee/book_management_system_frontend)@[6dcdfdf6aa...](https://github.com/Glonee/book_management_system_frontend/commit/6dcdfdf6aa186826329996fbfc07ed9b333af147)
#### Tuesday 2022-05-03 06:48:16 by Glonee

Do not go gentle into that good night,
Old age should burn and rave at close of day;
Rage, rage against the dying of the light.
Though wise men at their end know dark is right,
Because their words had forked no lightning they
Do not go gentle into that good night.
Good men, the last wave by, crying how bright
Their frail deeds might have danced in a green bay,
Rage, rage against the dying of the light.
Wild men who caught and sang the sun in flight,
And learn, too late, they grieved it on its way,
Do not go gentle into that good night.
Grave men, near death, who see with blinding sight
Blind eyes could blaze like meteors and be gay,
Rage, rage against the dying of the light.
And you, my father, there on the sad height,
Curse, bless me now with your fierce tears, I pray.
Do not go gentle into that good night.
Rage, rage against the dying of the light.

---
## [input-output-hk/ouroboros-network](https://github.com/input-output-hk/ouroboros-network)@[71cbca3021...](https://github.com/input-output-hk/ouroboros-network/commit/71cbca30215c827117425b8f082038b34a390109)
#### Tuesday 2022-05-03 07:16:33 by Nicholas Clarke

Integrate the Babbage ledger era.

- The BabbageEra is imported from cardano-ledger-babbage and added to
  `CardanoEras` etc.
- A new Babbage era is added to the Shelley codebase, and made an
  instance of `ShelleyBasedEra`. Note the slightly weird
  `TranslationContext` - we need to use the Alonzo translation context
  because of the assumption (in `ShelleyBasedEra`) that the translation
  context is equal to the `AdditionalGenesisConfig`. The latter is a
  diff from `Shelley`, whereas the former is a diff from the previous
  era.

  TODO We should drop this assumption and correct the relationship
  between these things.
- We introduce a new class, `SupportsTwoPhaseValidation`, to reuse code
  for dealing with 2-phase validation in Alonzo and subsequent eras.
- Add standard boilerplate patterns for the Babbage era (particularly in
  Ouroboros.Consensus.Cardano.Block).
- We add additional translation code to translate from Alonzo to
  Baggage. This is slightly more complex than usual, since it must also
  translate from TPraos to Praos. It's generally formulaic, however.
- New protocol versions are introduced supporting the Babbage era.
- `protocolInfoCardano` is expanded with configuration for
  Babbage/Praos. Again, this is largely straightforward.
- Block forging code for Praos is now uncommented, since there is a
  Praos era to work on.
- The block forging code for the TPraos eras is adjusted to add a "skip"
  at the end, for the Babbage era. Honestly, this is rather ugly, but
  it's the simplest approach right now.

---
## [clamor-s/u-boot](https://github.com/clamor-s/u-boot)@[485ad34a2e...](https://github.com/clamor-s/u-boot/commit/485ad34a2e10b94be78c0aba12015051f321b3e2)
#### Tuesday 2022-05-03 07:21:30 by Marcel Ziswiler

tegra: lcd: video: integrate display driver for t30

On popular request make the display driver from T20 work on T30 as
well. Turned out to be quite straight forward. However a few notes
about some things encountered during porting: Of course the T30 device
tree was completely missing host1x as well as PWM support but it turns
out this can simply be copied from T20. The only trouble compiling the
Tegra video driver for T30 had to do with some hard-coded PWM pin
muxing for T20 which is quite ugly anyway. On T30 this gets handled by
a board specific complete pin muxing table. The older Chromium U-Boot
2011.06 which to my knowledge was the only prior attempt at enabling a
display driver for T30 for whatever reason got some clocking stuff
mixed up. Turns out at least for a single display controller T20 and
T30 can be clocked quite similar. Enjoy.

Signed-off-by: Marcel Ziswiler <marcel.ziswiler@toradex.com>
Signed-off-by: Svyatoslav Ryhel <clamor95@gmail.com>

---
## [rohittembhurne2194/ICTSBMALL_ULB](https://github.com/rohittembhurne2194/ICTSBMALL_ULB)@[6ab213c5d2...](https://github.com/rohittembhurne2194/ICTSBMALL_ULB/commit/6ab213c5d28cfdf6fd9448fa80f12ef2e9124439)
#### Tuesday 2022-05-03 07:44:21 by umeshl@appynitty.com

Chnages done by Me the Millionaire persone i genrate multi source of income main is trading and other from social media for ex.. youtune instagram and amzon i will be definiltly successfull in this year and i buying my 1st car is mercedes c class c200d or c300 d 2022 model ameen god bleassed me sorry for my any mistake and so thanku for giving me this beatiful life

---
## [rohittembhurne2194/ICTSBMALL_ULB](https://github.com/rohittembhurne2194/ICTSBMALL_ULB)@[772a7c241d...](https://github.com/rohittembhurne2194/ICTSBMALL_ULB/commit/772a7c241d51e4cc46030227c2e0a47e28272abf)
#### Tuesday 2022-05-03 08:04:26 by umeshl@appynitty.com

Changes done By me its Millionaire Umesh i Will be definitly successful in this year in trading i will consitancely makeing profit in trading and i will genrate income 20k plus consitancely ameen god bleassed me and forgive me god for my any mistake and feelling gratitide for yours support in my life har har Mahadev Jai Mahakal

---
## [defgsus/kindergarten-times](https://github.com/defgsus/kindergarten-times)@[25fed91d18...](https://github.com/defgsus/kindergarten-times/commit/25fed91d1849736e97f814c74fb3c76e3f6ebc87)
#### Tuesday 2022-05-03 09:06:22 by bergi

Yesterday i falsly stated that i'd nothing special to say.
In truth, i was just busy with something else. But is this
repo really going to become my public diary? I don't know.

Regarding the sad story of **O** vs. **C** and me in between:
I did have a talk with **O**, the next day which was much
less radical. The previous night, we drank a lot (and here's another
retrospective truth: 'simply laziness' was in fact 'laziness
after a couple of beer last night') and the his basic notion
remains, which is, in non-radicalized form:

If someone is collaborating with or supporting people who (for example)
strive for a right-wing political career, then s/he should
not be made comfortable within my own comforting spaces.
If that happens, though, uncomfortable decissions need to be made.

---
## [freedesktop/drm-misc](https://github.com/freedesktop/drm-misc)@[213d266ebf...](https://github.com/freedesktop/drm-misc/commit/213d266ebfb1621aab79cfe63388facc520a1381)
#### Tuesday 2022-05-03 10:09:41 by Linus Torvalds

gpiolib: acpi: use correct format characters

When compiling with -Wformat, clang emits the following warning:

  gpiolib-acpi.c:393:4: warning: format specifies type 'unsigned char' but the argument has type 'int' [-Wformat]
                        pin);
                        ^~~

So warning that '%hhX' is paired with an 'int' is all just completely
mindless and wrong. Sadly, I can see a different bogus warning reason
why people would want to use '%02hhX'.

Again, the *sane* thing from a human perspective is to use '%02X. But
if the compiler doesn't do any range analysis at all, it could decide
that "Oh, that print format could need up to 8 bytes of space in the
result". Using '%02hhX' would cut that down to two.

And since we use

        char ev_name[5];

and currently use "_%c%02hhX" as the format string, even a compiler
that doesn't notice that "pin <= 255" test that guards this all will
go "OK, that's at most 4 bytes and the final NUL termination, so it's
fine".

While a compiler - like gcc - that only sees that the original source
of the 'pin' value is a 'unsigned short' array, and then doesn't take
the "pin <= 255" into account, will warn like this:

  gpiolib-acpi.c: In function 'acpi_gpiochip_request_interrupt':
  gpiolib-acpi.c:206:24: warning: '%02X' directive writing between 2 and 4 bytes into a region of size 3 [-Wformat-overflow=]
       sprintf(ev_name, "_%c%02X",
                            ^~~~
  gpiolib-acpi.c:206:20: note: directive argument in the range [0, 65535]

because gcc isn't being very good at that argument range analysis either.

In other words, the original use of 'hhx' was bogus to begin with, and
due to *another* compiler warning being bad, and we had that bad code
being written back in 2016 to work around _that_ compiler warning
(commit e40a3ae1f794: "gpio: acpi: work around false-positive
-Wstring-overflow warning").

Sadly, two different bad compiler warnings together does not make for
one good one.

It just makes for even more pain.

End result: I think the simplest and cleanest option is simply the
proposed change which undoes that '%hhX' change for gcc, and replaces
it with just using a slightly bigger stack allocation. It's not like
a 5-byte allocation is in any way likely to have saved any actual stack,
since all the other variables in that function are 'int' or bigger.

False-positive compiler warnings really do make people write worse
code, and that's a problem. But on a scale of bad code, I feel that
extending the buffer trivially is better than adding a pointless cast
that literally makes no sense.

At least in this case the end result isn't unreadable or buggy. We've
had several cases of bad compiler warnings that caused changes that
were actually horrendously wrong.

Fixes: e40a3ae1f794 ("gpio: acpi: work around false-positive -Wstring-overflow warning")
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
Signed-off-by: Andy Shevchenko <andriy.shevchenko@linux.intel.com>

---
## [skanev/dotfiles](https://github.com/skanev/dotfiles)@[41062c5a74...](https://github.com/skanev/dotfiles/commit/41062c5a74853b8930606b1aa6901556dc535085)
#### Tuesday 2022-05-03 10:10:16 by Stefan Kanev

tools: redo track-hivemind in Ruby

Alright, time for a long one.

scripts/track-hivemind got broken when we moved from webpacker to
vanilla webpack because the output was different. I wanted to fix it,
but it was annoying to do so, as it was hard to test the changes I'm
making. I needed to write a unit test, but it was a weird Perl script,
and now I faced a conundrum.

I made a decision a while ago to do more dotfile scripting in Perl. This
was purely for hedonistic reasons – I just enjoy writing Perl. But I run
into two problems:

* Some "advanced" techniques, like coroutines and threads, are awkward
  in Perl. They are doable, but I don't know how to do them and will
  need to learn.

* Non-trivial project setup (e.g. having your tests and your code in the
  same shebang runnable file) is tricky in Perl. It's doable, but I
  don't know how to do it, and I will need to learn.

Either I have to spend a lot of time learning auxiliary Perl skills,
which is fine, but time-consuming in a I'd-love-to-do-it-but-I-do-not-
have-the-time way. So I had to make a choice, and the choice is to keep
doing the same thing, but in Ruby, which is the modern Perl anyway. I
loose the learning fun, but as a bonus:

- I'm so much nimbler when doing this in Ruby
- I get to start a new Ruby codebase I can use to testbed Ruby tools I'm
  potentially gonna tools (or stuff that's already written like sorbet
  and solargraph)
- Ruby is fun too! I don't get to do it enough at work for some weird
  reason.

This, this is now moving to Ruby. I'm gonna start a Swamp-like thing,
but in Ruby. I chose to call it "mire", because that's a synonym and
also a fun word. Yeah, I'm lazy that way.

Like or retweet if you enjoyed reading.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[a9ccc5876a...](https://github.com/mrakgr/The-Spiral-Language/commit/a9ccc5876a6ade7001283b64879a4a9428b8c92e)
#### Tuesday 2022-05-03 11:31:30 by Marko Grdinić

"9:05am. Rough night. I am really groggy right now, and it is no wonder given the time I went to bed.

9:15am. https://youtu.be/2Iy6sfPVdF4
Retopology: Manual VS Automatic #1 (Manual)

I am obsessed with topology right now. I do not feel like redoing the monitor, but let me watch this. It should do for getting rid of my grogginess. At this level of obsession, I am not going to be doing any chilling. In fact I may just redo the whole thing.

https://youtu.be/2Iy6sfPVdF4?t=570

Instead of slicing it like that, maybe he could have made it planar, and have gotten rid of the ngons so the curvature gets maintained. Let me test out planar.

10:05am. https://youtu.be/2Iy6sfPVdF4?t=1045

Subdiv modeling is a pain in the ass.

https://youtu.be/Gzaf6_7eP8Q
Retopology: Manual VS Automatic #2 (Automatic)

Let me see how he will model it using splines and booleans. He didn't really retopology in the manual video, he just made sure the topology was right as he was working along.

10:15am. It is good that he is going into the time it would take to make it.

https://youtu.be/Gzaf6_7eP8Q?t=1261

It would have been faster to do an object like this in Moi.

10:35pm. Ok, enough of that. I think I completely understand the intricacies of topology. Let me redo the screen as an exercise. I kwetch too much about getting started. Once you have a goal in mind, redoing things should not be a big deal.

11:35am. Wow, this time on the front the topology is perfect. No distortion whatsoever when I put on that striped matcap.

Let me just do the back.

12:15pm. I knew that fiddling around with this would be the most time consuming part. Shit. It is just very difficult to get the exact shape of what I booleaned before. Maybe I should just use a lattice to stretch it into shape and not worry about it. That seems to be a smarter approach than the one I am taking now.

12:50pm. Let me stop here. Maybe I am not suited to being an artist. At least a 3d one. I really should not have fiddled around with the back so much. But I got engrossed in it.

1:30pm. Rather than stop, I ended up looking over the mesh and noticed that the lattice is messing up the seams. It is non symmetric.

https://docs.blender.org/manual/en/latest/modeling/modifiers/deform/mesh_deform.html

I'll look into using this instead later. What a pain in the ass this is. Let me have breakfast here."

---
## [zjjhot/gitea](https://github.com/zjjhot/gitea)@[3725fa28cc...](https://github.com/zjjhot/gitea/commit/3725fa28ccc01ab08060f591f894ea6443a348e8)
#### Tuesday 2022-05-03 11:47:00 by Gusted

Improve UI on mobile (#19546)

Start making the mobile experience not painful and be actually usable. This contains a few smaller changes to enhance this experience.

- Submit buttons on the review forms aren't columns anymore and are now allowed to be displayed on one row.
- The label/milestone & New Issue buttons were given each own row even tough, there's enough place to do it one the same row. This commit fixes that.
- The issues+Pull tab on repo's has a third item besides the label/milestone & New Issue buttons, the search bar. On desktop there's enough place to do this on one row, for mobile it isn't, currently it was using for each item a new row. This commits fixes that by only giving the searchbar a new row and have the other two buttons on the same row.
- The notification table will now be show a scrollbar instead of overflow.
- The repo buttons(Watch, Star, Fork) on mobile were showing quite big and the SVG wasn't even displayed on the same line, if the count of those numbers were too high it would even overflow. This commit removes the SVG, as there isn't any place to show them on the same row and allows them to have a new row if the counts of those buttons are high.
- The admin page can show you a lot of interesting information, on mobile the System Status + Configuration weren't properly displayed as the margin's were too high. This commit fixes that by reducing the margin to a number that makes sense on mobile.
- Fixes to not overflow the tables but instead force them to be scrollable.
- When viewing a issue or pull request, the comments aren't full-width but instead 80% and aligned to right, on mobile this is a annoyance as there isn't much width to begin with. This commits fixes that by forcing full-width and removing the avatars on the left side and instead including them inline in the comment header.

---
## [savethetreez/Civ13](https://github.com/savethetreez/Civ13)@[20b320a949...](https://github.com/savethetreez/Civ13/commit/20b320a949e6bd50e25ec505df3023405ce90dd6)
#### Tuesday 2022-05-03 13:13:01 by savethetreez

Adds missing conflicted icons

Fuck you again, Odisurin!

---
## [dotnet-maestro-bot/msbuild](https://github.com/dotnet-maestro-bot/msbuild)@[a572dc6b79...](https://github.com/dotnet-maestro-bot/msbuild/commit/a572dc6b796aec7d028e53aa24a82a059e47edfa)
#### Tuesday 2022-05-03 14:11:22 by Forgind

Fix low priority issues (#7413)

Thanks @svetkereMS for bringing this up, driving, and testing.

This fixes two interconnected issues.
First, if a process starts at normal priority then changes to low priority, it stays at normal priority. That's good for Visual Studio, which should stay at normal priority, but we relied on passing priority from a parent process to children, which is no longer valid. This ensures that we set the priority of a process early enough that we get the desired priority in worker nodes as well.

Second, if we were already connected to normal priority worker nodes, we could keep using them. This "shuts down" (disconnects—they may keep running if nodeReuse is true) worker nodes when the priority changes between build submissions.

One non-issue (therefore not fixed) is connecting to task hosts that are low priority. Tasks host nodes currently do not store their priority or node reuse. Node reuse makes sense because it's automatically off always for task hosts, at least currently. Not storing low priority sounds problematic, but it's actually fine because we make a task host—the right priority for this build, since we just made it—and connect to it. If we make a new build with different priority, we disconnect from all nodes, including task hosts. Since nodeReuse is always false, the task host dies, and we cannot reconnect to it even though if it didn't immediately die, we could, erroneously.

On the other hand, we went a little further and didn't even specify that task hosts should take the priority assigned to them as a command line argument. That has been changed.

svetkereMS had a chance to test some of this. He raised a couple potential issues:

conhost.exe launches as normal priority. Maybe some custom task dlls or other (Mef?) extensions will do something between MSBuild start time and when its priority is adjusted.
Some vulnerability if MSBuild init code improperly accounts for timing
For (1), how is conhost.exe related to MSBuild? It sounds like a command prompt thing. I don't know what Mef is.
For (2), what vulnerability? Too many processes starting and connecting to task hosts with different priorities simultaneously? I could imagine that being a problem but don't think it's worth worrying about unless someone complains.

He also mentioned a potential optimization if the main node stays at normal priority. Rather than making a new set of nodes, the main node could change the priority of all its nodes to the desired priority. Then it can skip the handshake, and if it's still at normal priority, it may be able to both raise and lower the priority of its children. Since there would never be more than 2x the "right" number of nodes anyway, and I don't think people will be switching rapidly back and forth, I think maybe we should file that as an issue in the backlog and get to it if we have time but not worry about it right now.

Edit:
I changed "shuts down...worker nodes when the priority changes" to just changing their priority. This does not work on linux or mac. However, Visual Studio does not run on linux or mac, and VS is the only currently known customer that runs in normal priority but may change between using worker nodes at normal priority or low priority. This approach is substantially more efficient than starting new nodes for every switch, disconnecting and reconnecting, or even maintaining two separate pools for different builds.

---
## [cdk8s-team/cdk8s-plus](https://github.com/cdk8s-team/cdk8s-plus)@[a9bb51303a...](https://github.com/cdk8s-team/cdk8s-plus/commit/a9bb51303ac94a6ddc37eff07c078669e45bc22b)
#### Tuesday 2022-05-03 14:24:44 by Eli Polonsky

chore: roles refactor (#678)

@Chriscbr Following our conversation, I think we need to take a somewhat different approach. 

We've been trying to optimize for code maintenance by creating a common `RoleBase` that gives us some common functionality between a `Role` and a `ClusterRole`. However, we should be optimizing for user experience. 

A `Role` can only define rules for resources, where as a `ClusterRole` can define rules both for resources and non-resources. Trying to express this inherent difference, while still keeping a common base class, is I think what gets us in trouble. The solution we came up with is to have a common `addResourceRule` method in the base class, and have `ClusterRole` add an `addNonResourceRule` method that will only apply to it. 

This will result in the following API:

```ts
const role = new kplus.Role(...);
role.addResourceRule(...);
role.allow(...);

const clusterRole = new kplus.Role(...);
clusterRole.addResourceRule(...);
clusterRole.addNonResourceRule(...);
clusterRole.allow(...);
```

There are several problems with this:

- Naming inconsistency (`addResourceRule` vs `allow` - even though both refer to resource rules). Note that if we change `addResourceRule -> addRule`, it won't be clear why `ClusterRole` has `addRule` and `addNonResourceRule`.
- The `add` methods don't offer any capabilities that the `allow` method don't. It creates a situation where we have two API's offering the same thing - which is confusing. I'm not sure the `add` methods have merit in higher level API's, the whole point is to remove this bulky k8s structure. If users want to use the underlying structure instead, they can always escape hatch. 

If we focus on optimizing user experience for the common use-case, I think the API should look like this: 

```ts
const role = new kplus.Role(...);
// allow reading a specific pod and all secrets
role.allowGet(pod, ApiResource.SECRETS);

const clusterRole = new kplus.ClusterRole(...);
// allow reading a specific pod, all secrets, and the /healthz endpoint
clusterRole.allowGet(pod, ApiResource.SECRETS, ApiEndpoint.of('/healthz'));
```

Note that a `Role` can be given only api resources, but a `ClusterRole` can be given non api resources as well, all with the same API. 

This PR adds an `ApiEndpoint` (this name is also used in k8s docs: *non-resource endpoints (like /healthz)*) interface that allows `ClusterRole` to accept everything it can. It also removes the `add` methods in favor of the existing `allow` ones. 

Note that the base was class was completely removed, which of course resulted in a some duplication, but I think its worth it for the flexibility it gives. 

#### Resources

- https://octopus.com/blog/k8s-rbac-roles-and-bindings
- https://kubernetes.io/docs/reference/access-authn-authz/rbac/

---
## [ENGO150/WHY2](https://github.com/ENGO150/WHY2)@[703c7d7044...](https://github.com/ENGO150/WHY2/commit/703c7d7044d24c4b3a23a101b5d0fd61eebe8982)
#### Tuesday 2022-05-03 15:10:26 by ENGO150

fixed undefined reference problem (hopefully)

dude - this problem.... I was searching fucking milions pages to fix this shit and THE WHOLE PROBLEM WAS CAUSED BY WRONG ORDER OF FLAGS..... I'm gonna die....

---
## [RealCrayfish/GuesserGame](https://github.com/RealCrayfish/GuesserGame)@[ae906e38a3...](https://github.com/RealCrayfish/GuesserGame/commit/ae906e38a3bc49fb1282170d12b6463f12d03c27)
#### Tuesday 2022-05-03 16:06:45 by RealCrayfish

changed the clear function to use ANSI escape codes instead of sys cls, and some other stuff i cant remember cause i did them last night

done some stuff meaning clear uses ANSI escape codes to clear the screen instead of sys cls meaning the app is now cross-platform compatable and doesnt have the risk of using some sort of weird virus some hacker did. i did some other stuff last night but i cant remember if i committed them so imma include them here, i would laugh if it is that i added the entire playablity update and im just glossing over it. but look, i did a cool thing with my clear function. and thats the thing im most proud of in this entire project. thanks for coming to my ted talk, see you in the next one

---
## [hexbatch/hexbatch-core-flow](https://github.com/hexbatch/hexbatch-core-flow)@[260615b431...](https://github.com/hexbatch/hexbatch-core-flow/commit/260615b431dbdf5419996153af66ba51011ef526)
#### Tuesday 2022-05-03 16:31:07 by Will Woodlief

0.5.1 git bit (#2)

Settings for projects using standards 

Now its easy to use the gui for any sort of standard data a project might make. The general user flow will be to store settings across several projects in the user project, and specific settings in the projects

There is a javascript function that can take a data setup and generate a dialog to show the views of a colletion of standards, and makes a fancy dropdown box to chose one. Also the user can clear the setting

Currently, the first setting being used is to replace the git settings in the project db table. These settings are now in the history page. The Project model now has some fancy constants to help standardize its settings. Probably will be more added later

Project model has some useful functions to get and set settings, as well as to get or create tags by name and attributes by name (useful as standard settings exists in system defined tags and attributes that might not exist yet)

Added to the git standard, a key for pushing automatically.
It can be checked in the git editor, and shows up as a magic wand icon in the git display near the git repo ssh link


Each setting exists in a tag that does not have to be part of the project, this is where the tag pointer comes in, so that a commonly used setting can be adjusted and then those changes are seen elsewhere. Also, permissions are always used when reading and writing settings. If you use a tag outside of the project, you must be able to read it to use it

Made new route to set project settings

Started to actually upgrade the version number a bit , now and then

Flow Attributes can now point to flow tags
Added support for this in the attributes and briefs

Made the User public profile more visually appealing

BUGFIX the pointee name and link was not showing up in the tag and attribute editors. Also have new tag pointer icon to show there

Improvement: now the pointee link is generated differently from the sql, and includes all four types. Also now have an icon showing the type, and all the links work

Bugfix, fixed up the links the attributes point to, as they are displayed in the GUI. Tag attributes now pull more general stuff from the db when created to help make links



Added new column for the tag pointer and did a bit of index refactoring in the text files

Improved the widely used project permission checking function to not require part of the slim framework to work, now its optional

Centralized another amazingly useful php function to handle ajax processing. It started life as part of the tag control, but now is shared in all the helpers in the base class. Did some renaming here too

Put the user selected meta into the regular profile page

Added a more general function to get user specific settings and data

Tags now have an easy way to see if they have a standard attribute or not, done by simply checking for the required keys of a standard type given

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[f71441c9b0...](https://github.com/UnderMybrella/usa/commit/f71441c9b058fab1b73efbf3ce696ed9501718df)
#### Tuesday 2022-05-03 16:32:29 by MarkiSpider

Update 78 files @ Tue, 03 May 2022 16:32:27 GMT
This site update changes thedude.html, ohyouwouldlikethatwouldntyou.html, dont-push.html, shatteredbysomeone.html, girlofthe21stcentury.html, cases.html, legal.html, idkbro.html, redacted.html, 914222-20513165181205.html, terrorblycute.html, user.html, michaeljackson.html, Jupiterandfriends.html, thefounders.html, 914222-3116201914.html, para.docs-portal, the-baboonies.html, corn-dm.html, usa-home.html, messenger.html, zeusandfriends.html, overview.html, byebyebye.html, inhumanresources.html, 914222-5241612154525.html, the-d_.html, suspect-hierarchy.html, karen-archive.html, everyone.html, youreinthewrongpartoftown.html, cart.html, case-directory.html, whyami.html, logout.html, 914222-1916135212518.html, karen6809.html, illinois.html, 914222-3116201914.html, reviews.html, Imsorrymissjackson.html, thebannerborn.html, helpcenter.html, shatteredbysomeone.html, michaeljackson.html, Rad_R.html, agencydirectory.html, 914222-3151316212051825072125.html, iinhumanresources.html, dont-push.html, para.docs-portal, karen-archive.html, dickpicks.html, ijustmadeyoulookunderthere.html, case-directory.html, ohyouwouldlikethatwouldntyou.html, captainwhyareyoudoingthistome.html, aretheyalium.html, moriarty.html, nebuchadnezzar.html, legal.html, fuckem.html, usa-home.html, intel.html, terminate-session.html, inbox.html, mission-report.html, youreinthewrongpartoftown.html, MRING.html, usaid-1121425.html, usaid-1121425.html, invii_suspects.html, usaid-1121425.html, push-reciept.jpg, usaid-1121425.html, dickpicks.html, usaid-1121425-1.html, supply-req.html

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[a7e1790c0b...](https://github.com/UnderMybrella/usa/commit/a7e1790c0baf00a01e16e6bfb6aeda2c2eb2effd)
#### Tuesday 2022-05-03 16:33:54 by MarkiSpider

Update 49 files @ Tue, 03 May 2022 16:33:52 GMT
This site update changes dashboard.html, cases.html, thecaptain.html, thejackson5.html, zeusandfriends.html, fuckem.html, thefounders.html, girlofthe21stcentury.html, images.html, 914222-3116201914.html, usa-home.html, overview.html, Jupiterandfriends.html, karen6815.html, employeeaccountabilitytimesignature-portal.html, suspect-hierarchy.html, 914222-3151316212051825072125.html, karen-archive.html, byebyebye.html, 914222-208502131102116.html, karen6816.html, schedule.html, overview.html, capitalism.html, the-asshats.html, woahhh.html, agencydirectory.html, helpcenter.html, karen6809.html, karen6803.html, thefounders.html, Imsorrymissjackson.html, ohyouwouldlikethatwouldntyou.html, messenger.html, oopsalbangers.html, NerdFiction.html, suspect-hierarchy.html, evidence.html, fuckem.html, howami.html, captainpleaseidontknowwhatshappeningimjustaneditor.html, c-8-dickpicks.html, inbox.html, push-reciept.jpg, usaid-1121425.html, usaid-1121425-1.html, intel.html, invii.html, usaid-1121425.html

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[fd727d11c0...](https://github.com/UnderMybrella/usa/commit/fd727d11c07910ecc2eaad504bc41ac60b8943fa)
#### Tuesday 2022-05-03 16:34:24 by MarkiSpider

Update 103 files @ Tue, 03 May 2022 16:34:21 GMT
This site update changes ijustmadeyoulookunderthere.html, illinois.html, 914222-29151493191121139.html, thealienalliance.html, fuckem.html, user8118151241161251919.html, auth.html, helpcenter.html, evidence.html, agentloginportal.html, dashboard.html, oopsalbangers.html, images.html, legal.html, karen6815.html, MichaelJackson.html, moriarty.html, para.docs-portal, theoracle.html, cases.html, reviews.html, 914222-201516156208512914513151814914741815145.html, user.html, dont-push.html, agencydirectory.html, corn-dm.html, 914222-3421144920.html, logout.html, karen6809.html, Imsorrymissjackson.html, 914222-208502131102116.html, 2702-invincible2syndicate.html, case-directory.html, kriskringle.html, cart.html, karen6816.html, MatPat.html, 914222-201516156208512914513151814914741815145.html, the-baboonies.html, lolgotyou.html, the-asshats.html, Rad_R.html, 914222-3151316212051825072125.html, illinois.html, para.docs-portal, cachow.html, terfwar.html, thedude.html, 914222-20513165181205.html, woahhh.html, inhumanresources.html, employeeaccountabilitytimesignature-portal.html, girlofthe21stcentury.html, Imsorrymissjackson.html, agencydirectory.html, agentloginportal.html, reviews.html, ijustmadeyoulookunderthere.html, gettingjiggywithit.html, iinhumanresources.html, thealienalliance.html, karen6809.html, thecaptain.html, ohyouwouldlikethatwouldntyou.html, 914222-208502131102116.html, 914222-5241612154525.html, legal.html, thejackson5.html, whereami.html, howami.html, fuckem.html, aretheyalium.html, departments.html, NerdFiction.html, 914222-29151493191121139.html, case-directory.html, usa-home.html, zeusandfriends.html, .html, 2702-invincible2syndicate.html, youreinthewrongpartoftown.html, moriarty.html, LixianTV.html, usaid-1121425-1.html, usaid-1121425.html, fieldrequest-dashboard.html, supply-req.html, usaid-1121425.html, usaid-1121425.html, usaid-1121425.html, mission-report.html, usaid-1121425.html, youreinthewrongpartoftown.html, .html, usaid-1121425.html, cart.html, assignments.html, current-position.html, captainpleaseidontknowwhatshappeningimjustaneditor.html, push-reciept.jpg, inbox.html, c-8-dickpicks.html, usaid-1121425.html

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[1c01c3b01f...](https://github.com/UnderMybrella/usa/commit/1c01c3b01ff5be6a491bb01b008396c8b3b9c1d3)
#### Tuesday 2022-05-03 16:34:54 by MarkiSpider

Update 94 files @ Tue, 03 May 2022 16:34:52 GMT
This site update changes logs.html, thecaptain.html, terrorblycute.html, .html, employeeaccountabilitytimesignature-portal.html, karen6815.html, auth.html, dashboard.html, terfwar.html, the-asshats.html, images.html, departments.html, shatteredbysomeone.html, para.docs-portal, thefounders.html, nebuchadnezzar.html, iinhumanresources.html, thejackson5.html, user8118151241161251919.html, messenger.html, theoracle.html, 914222-3421144920.html, thealienalliance.html, evidence.html, thedude.html, fuckem.html, corn-dm.html, 914222-20513165181205.html, logs.html, aretheyalium.html, woahhh.html, capitalism.html, karen6816.html, 914222-16152051420911213119153891920.html, karen6809.html, byebyebye.html, karen6804.html, 914222-5241612154525.html, thebannerborn.html, logout.html, lolgotyou.html, youreinthewrongpartoftown.html, inhumanresources.html, karen-archive.html, Imsorrymissjackson.html, helpcenter.html, ijustmadeyoulookunderthere.html, karen6804.html, overview.html, reviews.html, thedude.html, dont-push.html, illinois.html, agencydirectory.html, 914222-1916151820192112124214513114.html, karen6815.html, everyone.html, dickpicks.html, thebannerborn.html, thekilleidoscope.html, terrorblycute.html, karen6816.html, inhumanresources.html, terfwar.html, usa-home.html, departments.html, thejackson5.html, legal.html, fuckem.html, whereareyou.html, the-secret-lies-just-a-little-farther.html, case-directory.html, whereami.html, LixianTV.html, idkbro.html, zeusandfriends.html, usaid-1121425.html, dickpicks.html, usaid-1121425.html, dickpicks.html, usaid-1121425.html, usaid-1121425.html, usaid-1121425.html, usaid-1121425.html, MRING.html, supply-req.html, dickpicks.html, invii_suspects.html, push-reciept.jpg, youreinthewrongpartoftown.html, usaid-1121425.html, invii.html, captainpleaseidontknowwhatshappeningimjustaneditor.html, usaid-1121425.html

---
## [maxieds/FlowersForMama2022](https://github.com/maxieds/FlowersForMama2022)@[4fe89fd8b6...](https://github.com/maxieds/FlowersForMama2022/commit/4fe89fd8b6bbf6a7f076ecf89a39aa90869bb142)
#### Tuesday 2022-05-03 16:47:55 by Maxie D. Schmidt

RIP child of the 1960's :)))

I am learning to let go... At least gradually, but with some hesitation as to inflating the ego of daughter #2 (B) versus daugther #1 (M) -- as Don openly called us to tell Mama who was requesting her presence on the phone these last years -- e.g., by a reference to bodily functions (get it?). 

Misnomers are unnecessary, hurtful and not cool! I was the last one to hug Mama before she passed!! Brandye was asleep in her boyfriend's lap when I arrived that night. When the nurse woke us up to inform that she had passed on in hospice, Brandye was sitting on the floor near where I was sleeping. 

As a second topic note, my childhood IQ test score was reported to me by the psychologist that performed the analysis at getting capped off by him at 150. He whispered that it could project to 165 if they wanted to pay for further testing. Why God, why, the story has always been fudged to my sister that I scored a 137, where she got the 139, is beyond me. The lies end here. Do not believe what they repeat to you while your sister is watching Daria on the mTV laughing at the same time you are for diametrically opposed reasons over her favorite classic cartoon. It is enough that you love her more. Really, just cut the f-ing cord before she turns 40...

ARCHIVING THIS REPOSITORY NOW AS A GESTURE TOWARDS CLOSURE. I LOVE YOU, MAMA. YOU WILL ALWAYS BE IN MY HEART -- MDS ❤️❤️❤️☮︎☮︎☮︎❤️❤️❤️

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[13a65d3682...](https://github.com/cockroachdb/cockroach/commit/13a65d3682863dc94b5057801edae7ed8f7d7d18)
#### Tuesday 2022-05-03 16:49:10 by Andrei Matei

util/tracing: fix crash in StreamClientInterceptor

Before this patch, our client-side tracing interceptor for streaming rpc
calls was exposed to gRPC bugs being currently fixed in
github.com/grpc/grpc-go/pull/5323. This had to do with calls to
clientStream.Context() panicking with an NPE under certain races with
RPCs failing. We've recently gotten two crashes seemingly because of
this. It's unclear why this hasn't shown up before, as nothing seems new
(either on our side or on the grpc side). In 22.2 we do use more
streaming RPCs than before (for example for span configs), so maybe that
does it.

This patch eliminates the problem by eliminating the
problematic call into ClientStream.Context(). The background is that
our interceptors needs to watch for ctx cancelation and consider the RPC
done at that point. But, there was no reason for that call; we can more
simply use the RPC caller's ctx for the purposes of figuring out if the
caller cancels the RPC. In fact, calling ClientStream.Context() is bad
for other reasons, beyond exposing us to the bug:
1) ClientStream.Context() pins the RPC attempt to a lower-level
connection, and inhibits gRPC's ability to sometimes transparently
retry failed calls. In fact, there's a comment on ClientStream.Context()
that tells you not to call it before using the stream through other
methods like Recv(), which imply that the RPC is already "pinned" and
transparent retries are no longer possible anyway. We were breaking
this.
2) One of the grpc-go maintainers suggested that, due to the bugs
reference above, this call could actually sometimes give us "the
wrong context", although how wrong exactly is not clear to me (i.e.
could we have gotten a ctx that doesn't inherit from the caller's ctx?
Or a ctx that's canceled independently from the caller?)

This patch also removes a paranoid catch-all finalizer in the
interceptor that assured that the RPC client span is always eventually
closed (at a random GC time), regardless of what the caller does - i.e.
even if the caller forgets about interacting with the response stream or
canceling the ctx.  This kind of paranoia is not needed. The code in
question was copied from grpc-opentracing[1], which quoted a
StackOverflow answer[2] about whether or not a client is allowed to
simply walk away from a streaming call. As a result of conversations
triggered by this patch [3], that SO answer was updated to reflect the fact
that it is not, in fact, OK for a client to do so, as it will leak gRPC
resources. The client's contract is specified in [4] (although arguably
that place is not the easiest to find by a casual gRPC user). In any
case, this patch gets rid of the finalizer. This could in theory result
in leaked spans if our own code is buggy in the way that the paranoia
prevented, but all our TestServers check that spans don't leak like that
so we are pretty protected. FWIW, a newer re-implementation of the
OpenTracing interceptor[4] doesn't have the finalizer (although it also
doesn't listen for ctx cancellation, so I think it's buggy), and neither
does the equivalent OpenTelemetry interceptor[6].

Fixes #80689

[1] https://github.com/grpc-ecosystem/grpc-opentracing/blob/8e809c8a86450a29b90dcc9efbf062d0fe6d9746/go/otgrpc/client.go#L174
[2] https://stackoverflow.com/questions/42915337/are-you-required-to-call-recv-until-you-get-io-eof-when-interacting-with-grpc-cl
[3] https://github.com/grpc/grpc-go/issues/5324
[4] https://pkg.go.dev/google.golang.org/grpc#ClientConn.NewStream
[5] https://github.com/grpc-ecosystem/go-grpc-middleware/blob/master/tracing/opentracing/client_interceptors.go#L37-L52
[6] https://github.com/open-telemetry/opentelemetry-go-contrib/blame/main/instrumentation/google.golang.org/grpc/otelgrpc/interceptor.go#L193

Release note: A rare crash indicating a nil-pointer deference in
google.golang.org/grpc/internal/transport.(*Stream).Context(...)
was fixed.

---
## [mrakgr/The-Spiral-Language](https://github.com/mrakgr/The-Spiral-Language)@[c0ea67ef6c...](https://github.com/mrakgr/The-Spiral-Language/commit/c0ea67ef6cd285acdd128a06a524bef702f1328b)
#### Tuesday 2022-05-03 18:14:58 by Marko Grdinić

"2:15pm. https://www.youtube.com/watch?v=YbphjXJnuvk
Back to Basics: Mesh Deform Modifier

Done with chores. Let me watch some of these.

https://youtu.be/YbphjXJnuvk?t=237

I should figure out what shape keys are.

https://youtu.be/YbphjXJnuvk?t=255

Can you use these to immutably deform the mesh. If so that would be really useful.

https://youtu.be/YbphjXJnuvk?t=312

This is really powerful. I really should get more familiar with the deformers shouldn't I?

It is really hard to do certain things with subdiv. If I start adding more points to get precision that would increase the density of the topology. But with this I could get a lot more mileage out of it without necessarily applying it.

https://youtu.be/B11XBZmIIZc
Learn Shape Keys In Under 5 Mins | Blender

2:30pm. So what happens if you change topology while using shape keys?

2:35pm. Let me get rid of that lattice. I'll have to redo some of the work that I did.

It seems nothing problematic happens when you add geometry. A loop cut just gets interpolated.

2:40pm. Since I am at it, let me check out the other deformers. What about the laplacian deform?

https://youtu.be/UKjuk76Icu8
The Laplacian Smooth Modifier

Let me watch this first.

2:45pm. It seems Youtube has the shorts feature. Never saw this before. It sucks.

https://youtu.be/eozO8MYh-FQ?t=52
Blender Secrets - Laplacian Deform Modifier and Hooks

Hmmm, interesting. Let me play around with this for a bit.

3:05pm. Yeah, it is quite nice. Let me go for some more tutorials on this. What does hook vertex group do given that it already has a system of assigning to them?

https://youtu.be/YB55LsMc7P8
Blender 2.8 Tutorial: Surface Deform Modifier

Let me also watch this.

https://docs.blender.org/manual/en/latest/modeling/modifiers/deform/laplacian_deform.html

The docs mention nothing about hooks. Could I use shape keys for the laplacian deform instead?

https://youtu.be/kbfarm-LSIA
The Blender Hook Modifier EXPLAINED! (When do you use this thing?)

Let me take a look at this.

https://youtu.be/kbfarm-LSIA?t=70

Now I am confused whether it was the hook or the laplacian modifier that was responsible for moving the cube.

https://youtu.be/3brXVB1ewtA?t=82

Smart apply and shift click applies the mods and duplicated the object.

3:55pm. Played around with the laplacian mod a bit.

It is quite nice, but I am going to need the mesh deform in order to affect the subdiv'd vertices. Moving the regular ones around would defeat the point.

Though maybe if I put it after the subdiv modifier the vertex groups would get transfered and still work. It does not matter, the cage is the better solution.

Right, before I resume, let me take a proper break. I want to chill for a bit. After that I'll deal with the monitor.

4:20pm. Let me resume. Time to play with the mesh deformer.

I have that hole on the back of the monitor. The subdiv defines the 4 corners, and it is a real pain in the ass to modify the sides themselves without breaking everything.

Let me finally take care of it properly.

4:30pm. I am confused as to what is going on. Why is it just tugging the edges a bit?

4:55pm. I seems I am still messing with this. I do not get it. It does not behave like the lattice at all.

Ah fuck! I did not apply the scale!

5:05pm. I've tried setting the precision to 10. The quality of the mesh deformer's deformations is low. It is worse than the lattice.

Oh, Blender crashed.

I guess 10 was too much. I'll try 7 next time.

5:10pm. No, 7 is too much as well. I'll try 6.

5:15pm. No, it does not make a difference. Change of plans, I do not trust this as I am getting pinching. The lattice is what gives the best results. I am just going to stack those. I wanted to do that, but Hops refuses to do it automatically so I'll just do it by hand.

Actually what if I duplicated the mesh and applied it as a deformer?

5:30pm. No, the modifier works horrible. It's shit. No wonder I've yet to see it recommended.

5:30pm. Let me take a break here.

6pm. Let me resume. I want to get that monitor out of the way. Let me go all in on lattices. They are great. I have some ideas how to make them work better.

6:35pm. Considering they work based on bounding boxes, it is a waste of time that Blender itself does not do the fitting. Well, all is well that ends well. I finally have the model exported.

6:40pm. But who feels like starting texturing now?

Just one thing - remember that thread I opened yesterday, or was it 2 days ago? I completely forgot to check for replies to the question I posted...it seems I haven't gotten any. That takes care of that.

6:40pm. It is so lame that I spent the entire day today on this monitor. The front was easy, but just as I was afraid, I started fiddling around the back trying to get it to fit just right. I knew it would trigger my compulsive urges to get it right and I was right. This was after I spent the whole night cutting that cube with the knife tool and observing the subdiv patterns.

6:45pm. Instead of the lattice, for more difficult examples, I should just apply the mods and make the fits using the elastic move brush. That would have taken care of the problem in a few minutes. Instead I literally spent hours fiddling around trying to get the topology just right. Know yourself, and know your enemy and you shall not waste hours fiddling around.

6:50pm. I'll close here for the day. This will be on time for once. Tomorrow I will try to fall into a streamlined pace of doing the props and texturing them.

Maybe I'd be faster if I just ground things out instead of constructing an elaborate view of whatever it is that I am attempting first, but that is how I learn, so I can't avoid it. Once I attain expertise, I'll be able to just go forward unperturbed. If I was really good, all the props in my room would be done in a week, two tops.

7:05pm. It would have been faster to just stick with the old asset. Topology asside, the overall shape was there. And the slight shading issues would not be visible. But despite the voice urging me to conserve time, I just had to do it. Looking at the monitor now, and seeing how the quads smoothly flow over the surface without any kind of distortion or pinching makes me pleased. I cannot help, but be satisfied with my owrk, as simple as it is.

Next time, I really will just leave the final touches to the sculpting brushes and not mess with deformers like I have today. They are not worth it.

7:15pm. https://boards.4channel.org/a/thread/237359534/hikaru-no-go-vol18

I read Hikaru no Go a decade and a half ago, but I do not remember this story. I guess I must have missed these extra chapters. I really liked the manga, too bad it got cancelled.

8:15pm. Done with lunch. Let me close here. I am into the Hng reading session. Let me continue having this bit of fun. Tomorrow, I'll get the monitor done for real."

---
## [kane-f/vgstation13](https://github.com/kane-f/vgstation13)@[620e9e480e...](https://github.com/kane-f/vgstation13/commit/620e9e480e17c337eb674c7649534bb37e89fe1f)
#### Tuesday 2022-05-03 18:16:37 by Eneocho

pAI medical chems buff (#32388)

* pAI medical chems

* Update pai.dm

* DexalinPlus?

* Some more chems, for effect

* Fix?

* do you feel it now mr dream checker

* i need better glasses holy shit i'm blind

* dexp to dex

---
## [BeatLeader/beatleader-mod](https://github.com/BeatLeader/beatleader-mod)@[0d678566a9...](https://github.com/BeatLeader/beatleader-mod/commit/0d678566a94a4917722f1a7fbdc6b8f8aeb24180)
#### Tuesday 2022-05-03 18:39:49 by Hermanest

a lot of comments with auros insults

ye, auros, fuck you again

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[04a989c1d6...](https://github.com/UnderMybrella/usa/commit/04a989c1d603355dbee433fdf6e08f625ed569b8)
#### Tuesday 2022-05-03 18:56:55 by MarkiSpider

Update 108 files @ Tue, 03 May 2022 18:56:53 GMT
This site update changes para.docs-portal, agentloginportal.html, zeusandfriends.html, legal.html, 914222-20513165181205.html, captainwhyareyoudoingthistome.html, logs.html, 914222-3116201914.html, agencydirectory.html, NerdFiction.html, thealienalliance.html, user8118151241161251919.html, MichaelJackson.html, michaeljackson.html, terfwar.html, messenger.html, thejackson5.html, 914222-3421144920.html, overview.html, karen6803.html, Rad_R.html, cart.html, inhumanresources.html, 914222-3151316212051825072125.html, youreinthewrongpartoftown.html, Imsorrymissjackson.html, 2702-invincible2syndicate.html, everyone.html, logs.html, woahhh.html, the-d_.html, karen6809.html, karen-archive.html, logout.html, aretheyalium.html, MatPat.html, karen6809.html, 914222-201516156208512914513151814914741815145.html, 914222-3116201914.html, messenger.html, para.docs-portal, Jupiterandfriends.html, ohyouwouldlikethatwouldntyou.html, lolgotyou.html, cachow.html, employeeaccountabilitytimesignature-portal.html, dont-push.html, 914222-3151316212051825072125.html, 914222-208502131102116.html, search.html, agencydirectory.html, the-asshats.html, karen6815.html, whyami.html, 914222-20513165181205.html, theoracle.html, logs.html, girlofthe21stcentury.html, shatteredbysomeone.html, illinois.html, overview.html, 914222-16152051420911213119153891920.html, karen6804.html, helpcenter.html, gettingjiggywithit.html, everyone.html, 914222-1952425161182025.html, 914222-3421144920.html, Imsorrymissjackson.html, byebyebye.html, fuckem.html, moriarty.html, zeusandfriends.html, legal.html, 914222-29151493191121139.html, MichaelJackson.html, thejackson5.html, LixianTV.html, 2702-invincible2syndicate.html, the-secret-lies-just-a-little-farther.html, suspect-hierarchy.html, dontpush.html, captainwhyareyoudoingthistome.html, NerdFiction.html, case-directory.html, cart.html, whereareyou.html, usaid-1121425.html, usaid-1121425.html, usaid-1121425-1.html, usaid-1121425.html, usaid-1121425.html, .html, invii.html, invii.html, supply-req.html, terminate-session.html, dickpicks.html, usaid-1121425.html, assignments.html, usaid-1121425.html, usaid-1121425.html, dickpicks.html, youreinthewrongpartoftown.html, usaid-1121425.html, invii-surveillance.html, usaid-1121425.html, usaid-1121425.html

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[c4e40d5d4c...](https://github.com/UnderMybrella/usa/commit/c4e40d5d4c8c5f7b890fe73fc9cf64e0a5d2da07)
#### Tuesday 2022-05-03 18:57:24 by MarkiSpider

Update 85 files @ Tue, 03 May 2022 18:57:22 GMT
This site update changes zeusandfriends.html, dashboard.html, shatteredbysomeone.html, overview.html, terrorblycute.html, michaeljackson.html, messenger.html, thecaptain.html, logs.html, Jupiterandfriends.html, girlofthe21stcentury.html, the-asshats.html, illinois.html, reviews.html, employeeaccountabilitytimesignature-portal.html, legal.html, thefounders.html, 914222-29151493191121139.html, captainwhyareyoudoingthistome.html, agencydirectory.html, evidence.html, fuckem.html, para.docs-portal, images.html, 914222-1952425161182025.html, ohyouwouldlikethatwouldntyou.html, departments.html, Imsorrymissjackson.html, inhumanresources.html, 914222-16152051420911213119153891920.html, capitalism.html, suspect-hierarchy.html, case-directory.html, cart.html, cachow.html, 914222-5241612154525.html, byebyebye.html, thebutterflysoldiers.html, lolgotyou.html, 914222-208502131102116.html, 914222-3151316212051825072125.html, the-d_.html, woahhh.html, karen6816.html, theoracle.html, MatPat.html, agencydirectory.html, 914222-16152051420911213119153891920.html, karen6803.html, the-baboonies.html, inhumanresources.html, 914222-3116201914.html, Imsorrymissjackson.html, the-asshats.html, 914222-20513165181205.html, thedude.html, para.docs-portal, 914222-1952425161182025.html, shatteredbysomeone.html, illinois.html, thekilleidoscope.html, thealienalliance.html, agentloginportal.html, karen6816.html, michaeljackson.html, sexygoldarms.html, case-directory.html, 914222-3421144920.html, 914222-1916135212518.html, dont-push.html, 914222-29151493191121139.html, howami.html, fuckem.html, schedule.html, moriarty.html, idkbro.html, usaid-1121425.html, usaid-1121425.html, usaid-1121425.html, push-reciept.jpg, usaid-1121425.html, usaid-1121425.html, usaid-1121425.html, assignments.html, dickpicks.html

---
## [UnderMybrella/usa](https://github.com/UnderMybrella/usa)@[44eeeb283c...](https://github.com/UnderMybrella/usa/commit/44eeeb283c3b135b17d2112cbe53c899a67aafb8)
#### Tuesday 2022-05-03 18:57:53 by MarkiSpider

Update 67 files @ Tue, 03 May 2022 18:57:51 GMT
This site update changes agentloginportal.html, 914222-195242514914101.html, captainwhyareyoudoingthistome.html, nebuchadnezzar.html, evidence.html, usa-home.html, Jupiterandfriends.html, karen6815.html, thecaptain.html, girlofthe21stcentury.html, gettingjiggywithit.html, 914222-3421144920.html, overview.html, moriarty.html, .html, user.html, thefounders.html, logs.html, 914222-208502131102116.html, sexygoldarms.html, inhumanresources.html, case-directory.html, woahhh.html, 914222-1916151820192112124214513114.html, Imsorrymissjackson.html, 2702-invincible2syndicate.html, thebutterflysoldiers.html, theoracle.html, case-directory.html, everyone.html, whyami.html, thecaptain.html, iinhumanresources.html, 914222-20513165181205.html, 914222-3421144920.html, thekilleidoscope.html, capitalism.html, reviews.html, 914222-1916151820192112124214513114.html, dickpicks.html, 914222-5241612154525.html, 914222-29151493191121139.html, corn-dm.html, zeusandfriends.html, redacted.html, usa-home.html, the-secret-lies-just-a-little-farther.html, whereami.html, case-directory.html, fuckem.html, aretheyalium.html, kriskringle.html, moriarty.html, evidence.html, oopsalbangers.html, cart.html, envii.html, dickpicks.html, mission-report.html, inbox.html, usaid-1121425.html, invii.html, usaid-1121425.html, supply-req.html, intel.html, usaid-1121425.html, assignments.html

---
## [mszeles/a-hamunish-humanish-thoughtishish](https://github.com/mszeles/a-hamunish-humanish-thoughtishish)@[7d423ef528...](https://github.com/mszeles/a-hamunish-humanish-thoughtishish/commit/7d423ef528b5a4a2537bd27150a9384779182a3e)
#### Tuesday 2022-05-03 19:29:27 by Miklos Szeles

Miki: What's up Neveloper?
Neveloper: I am trying to transform agile into a humanish agileish approach which brings the team's well-being into the focus. In my opinion the best way to increase the team's productivity by making them happy.
Nikolai: Buy them a table-soccer, everybody knows table-soccer is the only way to make developers happy.
Miki: It is only one factor from many, but I do like to play table-soccer with my colleagues, but of course it is definitely not for everyone.

I love the humanish agileish method, we use that and it works perfectly.
Neveloper: Of course, it works. I came up with the idea.
Miki: Actually, it was me.
Neveloper: That might be true, but you had no balls to post it under your name and you gave life to me just to make sure they won't throw tomato on you.
Miki: Well. That is partially true. But most importantly I hired you as you are the expert in software development. Having talks with you gives life to new ideas, I really enjoy talking to you.
Minnie: Awww.

---
## [der-lyse/newsboat](https://github.com/der-lyse/newsboat)@[30bf362603...](https://github.com/der-lyse/newsboat/commit/30bf362603086ce2aec04a511824a32a71f3836a)
#### Tuesday 2022-05-03 19:43:19 by Lysander Trischler

Remove trailing whitespace

Trailing whitespace is not harmful, but unnecessary and ugly in my
opinion. I configured my editor to highlight it, so I see it all the
time, which is a bit annoying. Let's get rid of it.

Actually regenerating the filter produces some slightly different code
with my installed version of cococpp (Coco/R Jan 02, 2012), so I just
kept the old code and removed the trailing spaces and tabulators.

`make fmt` now also removes trailing whitespace from all the text files.
Since not only source files but any text files might be subject to
introducing new trailing whitespace, CI will not skip that formatting
task anmyore for documentation-, translation-, contribution- and/or
snap-only changes. It's not executed unconditionally all the time.

---
## [boofiboi/boofiboi.github.io](https://github.com/boofiboi/boofiboi.github.io)@[ee8c0f1d5a...](https://github.com/boofiboi/boofiboi.github.io/commit/ee8c0f1d5ae002398fe7896d1cd38a330e012782)
#### Tuesday 2022-05-03 20:08:21 by boofi

god fucking damn it i hate everything REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

---
## [qihqi/pytorch](https://github.com/qihqi/pytorch)@[1b7d7d9327...](https://github.com/qihqi/pytorch/commit/1b7d7d93276eb37c009905ef87ea9c2a7c95481e)
#### Tuesday 2022-05-03 20:28:35 by Brian Hirsh

Reland: "free up dispatch key space (in C++)" (#74963)

Summary:
Pull Request resolved: https://github.com/pytorch/pytorch/pull/74963

This is a re-land of D35192346 (https://github.com/pytorch/pytorch/commit/9872a06d77582e91e834103db75f774ca75f7fff) and D35192317 (https://github.com/pytorch/pytorch/commit/a9216cde6cc57f94586ea71a75a35aaabee720ff), which together are a diff that changes the internal representation of `DispatchKeySet` in pytorch core to free up the number of dispatch keys that we have available. See a more detailed description of the design in the original PR: https://github.com/pytorch/pytorch/pull/69633.

The original PR broke Milan workflows, which use a pytorch mobile build, and manifested as a memory corruption bug inside of `liboacrmerged.so`.

**Background: Existing Mobile Optimization**
Pytorch mobile builds have an existing optimization (here https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/c10/core/DispatchKey.h#L382 and here https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/aten/src/ATen/core/dispatch/OperatorEntry.h#L214), which works as follows:

Every operator in pytorch has a "dispatch table" of function pointers, corresponding to all of the (up to 64) different kernels that we might dispatch to when we run an operator in pytorch (autograd, cpu, cuda, complex number support, etc).

In mobile builds, the size of that table is shrunk from 64 to 8 to save a bunch of space, because mobile doesn't end up using the functionality associated with most dispatch keys.

The dispatcher also has a notion of "fallback kernels", which are kernels that you can register to a particular dispatch key, but should be able to work for "any operator". The array of fallback kernels is defined here: https://github.com/pytorch/pytorch/blob/cc23725e89713138aa1c81ce5fb4a8dbcd440ccf/aten/src/ATen/core/dispatch/Dispatcher.h#L294.

The mobile-optimization currently does **not** extend to this array (it wouldn't be that useful anyway because there is only one array of fallback kernels globally - vs. there is a separate dispatch table of function pointers per operator). So the per-operator tables on mobile are size 8, while the fallback table is size 64.

**The Bug**
This PR actually makes it difficult to enable that optimization separately for the per-operator arrays vs. the fallback array, and incidentally shrunk the size of the fallback array from 64 to 8 for mobile (that happened on this line: https://github.com/pytorch/pytorch/pull/69633/files#diff-f735cd7aa68f15b624100cbc4bb3b5ea76ffc7c9d3bec3b0ccabaa09609e5319R294).

That isn't a problem by itself (since mobile doesn't actually use any of the fallbacks that can no longer be stored). However, pytorch core will still register all of those fallback kernels on startup in mobile builds, even if they aren't used. When we tried to register one of those fallbacks on startup, it would try to dump the kernel somewhere in memory past the bounds of the (now smaller) array inside of the `Dispatcher` object, `backendFallbackKernels_`.

**Why didn't this problem show up in OSS CI? Why didn't it break other internal mobile workflows aside from Milan?**

Ideally, this failure would show up as part of the OSS signal on GitHub, since we already have mobile OSS builds. Given that it was another memory corruption issue that only affected Milan (subset of mobile), I'm not sure what's specific about Milan's builds that caused it only to manifest there. dreiss I wonder if there's another flavor of mobile builds we could run in OSS CI that could potentially help catch this?

**The debugging experience was pretty difficult**

Debugging the Milan-specific failure was made difficult by the following:

(1) lack of CI
- the original Milan failure didn't surface on my original diff, because the Milan job(s) that failed weren't triggered to run on pytorch changes. There's probably a balance to strike here, since those jobs will only be useful if they aren't flaky, and if they can produce reliable failure logs for debugging.

(2) It's difficult to get a repro.
- my work laptop doesn't have the right specs to run the Milan development workflow (not enough disk space)
- There is an existing OnDemand workflow for Milan, but it appears to be relatively new, and after a bunch of help from MarcioPorto, we ran into issues forwarding the log output from Milan tests on the emulator back to the terminal (see the original discussion here: https://fb.workplace.com/groups/OnDemandFRL/permalink/1424937774645433/)

(3) Lack of stack-traces.
- Most Milan failures didn't include actionable stack traces. phding generously helped me debug by running my suggested patches locally, and reporting back if there were any failures. The failing test didn't include a stack trace though (just the line where the crash appeared), so I ended up making some educated guesses about what the issue was based on the area of the crash.
ghstack-source-id: 152688542

Test Plan: Confirmed with phding that the broken Milan workflow from the previous version of this diff is now passing.

Reviewed By: phding, albanD

Differential Revision: D35222806

fbshipit-source-id: 0ad115a0f768bc8ea5d4c203b2990254c7092d30
(cherry picked from commit 002b91966f11fd55ab3fa3801b636fa39a6dd12c)

---
## [crawl/crawl](https://github.com/crawl/crawl)@[c08b2e8bf8...](https://github.com/crawl/crawl/commit/c08b2e8bf8864494d43077b7622612e4c5b192df)
#### Tuesday 2022-05-03 21:09:39 by nicolae-carpathia

Add the most nicolae demonic rune vault possible (#2260)

* Add the most nicolae demonic rune vault possible

I have reached my apotheosis: I have put a rune in a shop.

Since the demonic rune repeats if you don't pick it up, I figured it
would be the best option for a rune shop. (The abyssal rune also
reappears if you don't pick it up, but the theme is easier to fit into
Pandemonium.) If you already have the rune, the shop instead places
another kind of rarity: a figurine of a ziggurat. (The only other
really rare item I could think of was a quad damage, and I've been
explicitly told multiple times that I'm not allowed to use those
outside of Sprint. Tyranny!)

Out of 25 generated shops, the stats on the price of a demonic rune:
Minimum: 3804
Maximum: 8647
Average: 6640.76
St Dev:  1412.1
I didn't check the price stats on the zigfig because the rune is the
real draw here.

The vault also places fat stacks of cash, three other shops, and
demon-summoning monsters from other branches as visitors. Enjoy!

* Make adjustments to the pan bazaar rune vault

Make some changes based on feedback from the other devs:
1) If you already have the demonic rune, instead of selling a
   zigfig, the central shop now just sells randarts. (I had
   underestimated the importance of zigfigs.)
2) The difficulty has been turned up a bit. The area outside
   the central area places more monsters now.
3) A few of the nonruniferous shops have been tweaked.

---
## [HashmatHamid/Hashmat-Python-assessment](https://github.com/HashmatHamid/Hashmat-Python-assessment)@[5d4063ceb7...](https://github.com/HashmatHamid/Hashmat-Python-assessment/commit/5d4063ceb74081caca2196835533fd40bd732f8c)
#### Tuesday 2022-05-03 21:29:03 by Hashmat Hamid

print("""Hello and welcome to my general mathematics quiz.
In this quiz you will be asked from 10-50 mathematics questions based on
your choice.
Also depending on your choice, you can choose to  do either a hard or easy
quiz.
The hard quiz will feature algebra and number, you will also be only
allowed to answer with word answers.
With the easy questions you will be asked number questions and the answers
wil be in a multi-choice form. """)
    print("I hope you enjoy :)")

#this is where user gets asked to input their name
def name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isalpha():
              break
        except ValueError:
            print("Not a valid name")

    print("Hello {} I hope you have fun playing my game".format(name))
#this is where user gets asked to input their age

def age():
    while True:
        try:
            age = input("Please enter your age: ")
            age = int(age)
            break
        except ValueError:
            print("Not a valid age! Please try again ...")

    print("Wow, you are {}".format(age))

#all my questions
def questions():
    global score
    score=0
    qq = { 'Q.1) What is 2*2 \n a: 4\n b: 5\n c: 3\n' : '4' , 'Q.2) What is 3*2\n a: 2\n b: 6\n c: 7 \n' : '6' ,
                 'Q.3) What is the unit for factorial in maths \n a: ^\n b: %\n c: ! \n' : '!' , 'Q.4) What is the equation for a question using the pythagoras theorem \n a: a^2+b^2=c^2\n b: b^2+c^2=a^2\n c: c^2+a^2=b^2 \n' : 'a^2+b^2=c^2' , 'Q.5) What is the value of pi \n a: 2.5\n b: 3.14\n c: 0.1 \n' : '3.14' , 'Q.6) What is 2 squared \n a: 4\n b: 2\n c: 1\n' : '4' , 'Q.7) What is the square root of 81 \n a: 9\n b: 13\n c: 10 \n' : '9' , 'Q.8) What is the value of Gst \n a: 15%\n b: 1.5%\n c: 0.15% \n' : '15%' , 'Q.9) Where did the person who invented Algorthm die \n a: Baghdad\n b: London\n c: Beijing\n' : 'Baghdad' , 'Q.10) What year did Stephen Hawking die \n a: 2018\n b: 2019\n c: 2017 \n' : '2018'
         }

    for key in qq.keys():
        user_answer=input(key).lower().strip()
        if qq.get(key)==user_answer:
            print("Correct!")
            score+=1
        else:
            print("You're Wrong!")

#printing functions
intro()
name()
age()
questions()
#print score
print("You got "+str(score)+" right!")

---

