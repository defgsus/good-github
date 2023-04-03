## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-04-02](docs/good-messages/2023/2023-04-02.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,937,749 were push events containing 2,789,382 commit messages that amount to 178,966,743 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 58 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[e1221c986f...](https://github.com/tgstation/tgstation/commit/e1221c986f5da2551051f47aa0fbd1d49e367c9b)
#### Sunday 2023-04-02 00:02:19 by san7890

Chasm Hell On Icebox - 300 Active Turfs on Prod Moment (#74410)

## About The Pull Request

Spontaneous regressions introduced by #74359
(1e58c1875d9e2f48a306fe31a0626dbbb1990ff9).
```txt
 - Z-Level 2 has 150 active turf(s).
 - Z-Level 3 has 150 active turf(s).
 - Z-Level trait Ice Ruins Underground has 300 active turf(s).
 - Z-Level trait Mining has 300 active turf(s).
 - Z-Level trait Station has 300 active turf(s).
 - End of active turf list.
 ```

![image](https://user-images.githubusercontent.com/34697715/229213138-5a6a7a4f-edec-47ab-8def-ee4e4bddfe61.png)

Basically the lavaland ruin sucks dogshit and I had to do a lot of stuff to account for everything failing. There was even a moment where we were adding something to `flags_1` instead of `turf_flags` and that was also really bad to figure out.

![image](https://user-images.githubusercontent.com/34697715/229213428-63bb1f6e-6f88-4604-a3c6-e08e20cbfa7a.png)

i also had to add orange genturfs because it was really getting bad with all of the assertions we had to keep making, especially since stuff like this could also show up:

![image](https://user-images.githubusercontent.com/34697715/229213562-4a145453-5f90-4d05-b8cc-5c1beec2b0dd.png)

That's the prison in the red box, those are active turfs because a chasm scraped it away.

Sorry if this is hard to follow but I promise you everything in this is essential. I wish we didn't have to rely on turf flags as much as we do but this is a fix PR, not a refactor.
## Why It's Good For The Game

Even one active turf on IceBox ate up _three_ seconds of SSair's initialization every single time it was really fucking bad.

We haven't had to deal with chasms for about two years so there's a lot of mapping assertions we made since they just weren't a thing, but now they're back so lets do it properly.
## Changelog
:cl:
fix: The prison on IceBox should no longer leak air as often.
/:cl:

I have compiled this map about 30 times until active turfs stopped fucking happening and now I am content. This likely doesn't fix _everything_ because some stuff can still be hidden to me, and we still have PRs that need to be merged to reduce the amount of noise we're getting on prod.

---
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[27d37cb0f4...](https://github.com/Kapu1178/daedalusdock/commit/27d37cb0f47d007d1159ad5af69ace39a50b003f)
#### Sunday 2023-04-02 00:05:39 by Gallyus

Alternate Version Tests (#281)

* AltVer Checks
I think?
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* 1603 target

* support script

* HOLY SHIT CAN I READ

* e

* HOLY FUCK CAN I READ

* Disable shortkill version check

---
## [AOSP-Krypton/frameworks_base](https://github.com/AOSP-Krypton/frameworks_base)@[3e99f654fb...](https://github.com/AOSP-Krypton/frameworks_base/commit/3e99f654fbf56d3b7ef7130658b8ef83d2d0cdbd)
#### Sunday 2023-04-02 00:10:10 by Dianne Hackborn

Fix issue #34471029: Don't allow audio use from background apps.

This is becoming a common pattern (keeping track of which processes
are cached and not allowing them to do stuff in that state), so I
am turning this in to a general mechanism for monitoring this state
through the activity manager's IUidObserver.  Now we can just have
AudoService implement its own IUidObserver to get this state and
update which uids it is blocking.

This required making some changes to uid change reports so that
the integer is now a bit mask instead of an enumerations, but that
is what it was already turning in to anyway.  (This gets rid of
the crazy GONE_IDLE constant that we'd needed to add before because
it wasn't a bit mask).

Eventually the power manager should be changed to be told about
these changes to cached state instead of listening to every proc
state change, but we'll do that later, it is more disruption than
I want to take for now.  However, while working on this, I noticed
that the power manager had regressed in the cached uids it would
actually block, because the activity manager was no longer telling
it about all uids that are idle.  (I think this happened when I had
to change the default idle state of UidRecord to true.)  So I am
adding a bit of new code to keep track of what idle state we last
reported to observers, to make sure we tell it about newly created
uids that are idle but have never actually become active.

Test: runtest -c com.android.server.am.ActivityManagerServiceTest frameworks-services

Change-Id: I7bfd46bacadd4cab2a69f40e6e52afb4e67b456a

---
## [ArtemisStation/artemis-tg](https://github.com/ArtemisStation/artemis-tg)@[0a1f7e8de2...](https://github.com/ArtemisStation/artemis-tg/commit/0a1f7e8de2fea2116b73f22a11fdf328763c503a)
#### Sunday 2023-04-02 00:15:04 by Hatterhat

Thrown containers splashing on mobs spill some contents on the floor (#74345)

## About The Pull Request
Spiritual continuation of tgstation/tgstation#74187.

![image](https://user-images.githubusercontent.com/31829017/228645705-5a32cc67-37e0-48d6-9e95-6006f455ed3c.png)
Reagent containers that splash their contents on people also splash the
floor - the amount that gets splashed on the floor is the amount that
missed the target.
### Mapping March

Ckey to receive rewards: N/A (it's not a mapping PR)

## Why It's Good For The Game
Splashing people with a molotov filled with Random Shit now also
splashes that Random Shit all around, making them slightly more spicy to
play around with. Unfortunately, I couldn't figure out how to make fuel
puddles ignite off of lit objects resting on top of them (there's no
item-level proc for hotspot exposure or something). If anyone wants to
advise me on how to make that happen, that'd be cool.

## Changelog
:cl:
add: Reagent containers that splash on people when thrown (e.g.
molotovs) now spill their contents on both target and turf. (This means
that throwing molotovs with enough fuel spills fuel puddles, throwing
beakers with acid spills acid on the floor, etc. etc.) Unfortunately,
molotovs still lack the ability to ignite their own spilled fuel, but
we'll get there one day.
/:cl:

Co-authored-by: Hatterhat <Hatterhat@users.noreply.github.com>

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[4599842d7c...](https://github.com/DrDiasyl/tgstation/commit/4599842d7c6b5ed499307f92a6f8032d598b7889)
#### Sunday 2023-04-02 00:28:55 by Jacquerel

Makes Shake() proc work (#73480)

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

---
## [ShamanSliph/Bubberstation](https://github.com/ShamanSliph/Bubberstation)@[1fe9efd00a...](https://github.com/ShamanSliph/Bubberstation/commit/1fe9efd00aeb0e2d4f4dedf89460abacecef9d1b)
#### Sunday 2023-04-02 00:30:02 by SkyratBot

[MIRROR] Rebuilds Luxury Shuttle (mostly), makes it emag-only [MDB IGNORE] (#19229)

* Rebuilds Luxury Shuttle (mostly), makes it emag-only (#72940)

## About The Pull Request
![2023 02 07-06 49
54](https://user-images.githubusercontent.com/70376633/217159751-790e6ded-8525-4d13-a5b5-6a3d8076a00e.png)
Changes the really goofy old lux shuttle to a cooler layout with some
additions to make it a luxury and not just
"anti-poor-people protection + food"

Shuttle was made bigger to make it less cramped for the luxury class,
pool was moved to its own room, added an arcade
and a bar corner, has real lasers to shoot poors with (20c each shot),
has fire extinguishers now
Adds a new preopen variant of hardened shutters
Adds a paywall pin subtype for the luxury shuttle, and a laser gun
subtype

Made emag-only at a price of 10000 credits
## Why It's Good For The Game

The old luxury shuttle looked REALLY awful with its pool, was pretty
cramped even in the luxury section and BARELY resembled a luxury..
This luxury shuttle provides luxuries such as a less poorly designed
pool, more space for legs, arcade, to make it resemble a luxury unlike
the old one

## Changelog
:cl:
add: Luxury Shuttle is now bigger, and less ugly! Poor people still get
it rough though...
/:cl:

* Rebuilds Luxury Shuttle (mostly), makes it emag-only

---------

Co-authored-by: jimmyl <70376633+mc-oofert@users.noreply.github.com>

---
## [Tastyfish/-tg-station](https://github.com/Tastyfish/-tg-station)@[ab307032ed...](https://github.com/Tastyfish/-tg-station/commit/ab307032edc7ed3dd360bfcc9176f6f54c22a3fe)
#### Sunday 2023-04-02 00:31:24 by LemonInTheDark

Nightvision Rework (In the name of color) (#73094)

## About The Pull Request

Relies on #72886 for some render relay expansion I use for light_mask
stuff.

Hello bestie! Night vision pissed me off, so I've come to burn this
place to the ground.
Two sections to discuss here. First we'll talk about see_in_dark and why
I hate it, second we'll discuss the lighting plane and how we brighten
it, plus introducing color to the party.

### `see_in_dark` and why it kinda sucks

https://www.byond.com/docs/ref/#/mob/var/see_in_dark

See in dark lets us control how far away from us a turf can be before we
hide it/its contents if it's dark (not got luminosity set)
We currently set it semi inconsistently to provide nightvision to mobs.

The trouble is stuff that produces light != stuff that sets luminosity.
The worst case of this can be seen by walking out of escape on icebox,
where you'll see this


![image](https://user-images.githubusercontent.com/58055496/215683654-587fb00f-ebb8-4c83-962d-a1b2bf429c4a.png)

Snow draws above the lighting plane, so the snow will intermittently
draw, depending on see_in_dark and the luminosity from tracking lights.
This would in theory be solvable by modifying the area, but the same
problem applies across many things in the codebase.
As things currently stand, to be emissive you NEED to have a light on
your tile. People are bad at this, and honestly it's a bit much to
expect of them. An emissive overlay on a canister shouldn't need an
element or something and a list on turfs to manage it.
This gets worse when you factor in the patterns I'm using to avoid
drawing lights above nothing, which leads to lights that should show,
but are misoffset because their parent pixel offsets.

It's silly. We do it so we can have things like mesons without just
handing out night vision, but even there the effect of just hiding
objects and mobs looks baddddddd when moving. It's always bothered me.
I'll complain about mesons more later, but really just like, they're too
bright as it is.

I'm proposing here that rather then manually hiding stuff based off
distance from the player, we can instead show/hide using just the
lighting plane. This means things like mesons are gonna get dimmer, but
that's fine because they suck.

It does have some side effects, things like view() on mobs won't hide
stuff in darkness, but that's fine because none actually thinks about
view like that, I think.

Oh and I added a case to prevent examining stuff that's in darkness, and
not right next to you when you don't have enough nightvision, to match
the old behavior `see_in_dark` gave us.

Now I'd like to go on a mild tangent about color, please bare with me

### Color and why `lighting_alpha` REALLY sucks

You ever walk around with mesons on when there's a fire going, or an
ethereal or firelocks down.
You notice how there isn't really much color to our lights? Doesn't that
suck?

It's because the way we go about brighting lighting is by making
everything on the lighting plane transparent.
This is fine for brightening things, but it ends up looking kinda crummy
in the end and leads to really washed out colors that should be bright.
Playing engineer or miner gets fucking depressing.

The central idea of this pr, that everything else falls out of, is
instead of making the plane more transparent, we can use color matrixes
to make things AT LEAST x bright.

https://www.byond.com/docs/ref/#/{notes}/color-matrix

Brief recap for color matrixes, fully expanded they're a set of 20
different values in a list
Units generally scale 0-1 as multipliers, though since it's
multiplication in order to make an rgb(1,1,1) pixel fullbright you would
need to use 255s.

A "unit matrix" for color looks like this:
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0, 0, 0, 0
)
```

The first four rows are how much each r, g, b and a impact r, g, b and
well a.
So a first row of `(1, 0, 0, 0)` means 1 unit of r results in 1 unit of
r. and 0 units of green, blue and alpha, and so on.
A first row of `(0, 1, 0, 0)` would make 1 red component into 1 green
component, and leave red, blue and alpha alone, shifting any red of
whatever it's applied to a green.

Using these we can essentially color transform our world. It's a fun
tool. But there's more.

That last row there doesn't take a variable input like the others.
Instead, it ADDS some fraction of 255 to red, green, blue and alpha.

So a fifth row of `(1, 0, 0, 0)` would make every pixel as red as it
could possibly be.

This is what we're going to exploit here. You see all these values
accept negative multipliers, so we can lower colors down instead of
raising them up!
The key idea is using color matrix filters
https://www.byond.com/docs/ref/#/{notes}/filters/color to chain these
operations together.

Pulling alllll the way back, we want to brighten darkness without
affecting brighter colors.
Lower rgb values are darker, higher ones are brighter. This relationship
isn't really linear because of suffering reasons, but it's good enough
for this.
Let's try chaining some matrixes on the lighting plane, which is bright
where fullbright, and dark where dark.

Take a list like this

```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     -0.2, -0.2, -0.2, 0
)
```
That would darken the lighting a bit, but negative values will get
rounded to 0
A subsequent raising by the same amount
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0.2, 0.2, 0.2, 0
)
```
Will essentially threshold our brightness at that value.
This ensures we aren't washing out colors when we make things brighter,
while leaving higher values unaffected since they basically just had a
constant subtracted and then readded.

### But wait, there's more

You may have noticed, we gain access to individual color components
here.
This means not only can we darken and lighten by thresholds, we can
COLOR those thresholds.
```
list(1, 0, 0, 0,
     0, 1, 0, 0,
     0, 0, 1, 0,
     0, 0, 0, 1,
     0.1, 0.2, 0.1, 0
)
```
Something like the above, if applied with its inverse, would tint the
darkness green.
The delta between the different scalars will determine how vivid the
color is, and the actual value will impact the brightness.

Something that's always bothered me about nightvision is it's just
greyscale for the most part, there isn't any color to it.
There was an old idea of coloring the game plane to match their lenses,
but if you've ever played with the colorblind quirk you know that gets
headachey really fast.
So instead of that, lets color just the darkness that these glasses
produce.
It provides some reminder that you're wearing them, instead of just
being something you forget about while playing, and provides a reason to
use flashlights and such since they can give you a clearer, less tinted
view of things while retaining the ability to look around things.

I've so far applied this pattern to JUST headwear for humans (also those
mining wisps)
I'm planning on furthering it to mobs that use nightvision, but I wanted
to get this up cause I don't wanna pr it the day before the freeze.

Mesons are green, sec night vision is red, thermals orange, etc.

I think the effect this gives is really really nice. 
I've tuned most things to work for the station, though mesons works for
lavaland for obvious reasons.

I've tuned things significantly darker then we have them set currently,
since I really hate flat lighting and this system suffers when
interacting with it.

My goal with these is to give you a rough idea of what's around you,
without a good eye for detail.
That's the difference between say, mesons, and night vision. One helps
you see outlines, the other gives you detail and prevents missing
someone in the darkness.

It's hard to balance this precisely because of different colored
backgrounds (looking at you icebox)
More can be done on this front in future but I'm quite happy with things
as of now

### **EDIT**

I have since expanded to all uses of nightvision, coloring most all of
them.

Along the way I turned some toggleable nightvision into just one level. 
Fullbright sucks, and I'd rather just have one "good" value.

I've kept it for a few cases, mostly eyes you rip out of mobs.
Impacted mobs are nightmares, aliens, zombies, revenants, states and
sort of stands.

I've done a pass on all mobs and items that impact nightvision and added
what I thought was the right level of color to them. This includes stuff
like blobs and shuttle control consoles
As with glasses much of this was around reducing vision, though I kept
it stronger here, since many of these mobs rely on it for engaging with
the game

<details>
<summary>
Technical Changes
</summary>

#### Adds filter proc (the ones that act like templates) support to
filter transitions.
Found this when testing this pr, seemed silly.

#### Makes our emissive mask mask all light instead
This avoids dumbass overlay lighting lighting up wallmounts.
We switch modes if some turfflags are set, to accomplish the same thing
with more overhead, and support showing things through the darkness.

Also fixes a bug where you'd only get one fullscreen object per mob, so
opening and closing a submap would take it away

Also also fixes the lighting backdrop not actually spanning the screen. 
It doesn't actually do anything anymore because of the fullscreen light
we have, but just in case that's unsued.
Needs cleanup in future.

#### Moves openspace to its own plane that doesn't draw, maxing its
color with a sprite

This is to support the above
We relay this plane to lighting mask so openspace can like, have
lighting

#### Changes our definition of nightvision to the light cutoff of night
vision goggles and such
Side affect of removing see_in_dark. This logic is a bit weak atm, needs
some work.

#### Removes the nightvision spell
It's a dupe of the nightvision action button, and newly redundant since
I've removed all uses of it

#### Cleans up existing plane master critical defines, ensures
trasnparent won't render

These sucked
Also transparent stuff should never render, if it does you'll get white
blobs which suck

</details>

## Why It's Good For The Game

Videos! (Github doesn't like using a summary here I'm sorry)
<details>

Demonstration of ghost lighting, and color


https://user-images.githubusercontent.com/58055496/215693983-99e00f9e-7214-4cf4-a76a-6e669a8a1103.mp4

Engi-glass mesons and walking in maint (Potentially overtuned, yellow is
hard)


https://user-images.githubusercontent.com/58055496/215695978-26e7dc45-28aa-4285-ae95-62ea3d79860f.mp4

Diagnostic nightvision goggles and see_in_dark not hiding emissives


https://user-images.githubusercontent.com/58055496/215692233-115b4094-1099-4393-9e94-db2088d834f3.mp4

Sec nightvision (I just think it looks neat)


https://user-images.githubusercontent.com/58055496/215692269-bc08335e-0223-49c3-9faf-d2d7b22fe2d2.mp4

Medical nightvision goggles and other colors


https://user-images.githubusercontent.com/58055496/215692286-0ba3de6a-b1d5-4aed-a6eb-c32794ea45da.mp4

Miner mesons and mobs hiding in lavaland (This is basically the darkest
possible environment)


https://user-images.githubusercontent.com/58055496/215696327-26958b69-0e1c-4412-9298-4e9e68b3df68.mp4

Thermal goggles and coloring displayed mobs


https://user-images.githubusercontent.com/58055496/215692710-d2b101f3-7922-498c-918c-9b528d181430.mp4

</details>

I think it's pretty, and see_in_dark sucks butt.

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
add: The darkness that glasses and hud goggles that impact your
nightvision (think mesons, nightvision goggles, etc) lighten is now
tinted to match the glasses. S pretty IMO, and hopefully it helps with
forgetting you're wearing X.
balance: Nightvision is darker. I think bright looks bad, and things
like mesons do way too much
balance: Mesons (and mobs in general) no longer have a static distance
you can see stuff in the dark. If a tile is lit, you can now see it.
fix: Nightvision no longer dims colored lights, instead simply
thresholding off bits of darkness that are dimmer then some level.
/:cl:

---
## [Tastyfish/-tg-station](https://github.com/Tastyfish/-tg-station)@[5a069975c3...](https://github.com/Tastyfish/-tg-station/commit/5a069975c3083888c986302ab5c0b32fc4362c20)
#### Sunday 2023-04-02 00:31:24 by LemonInTheDark

God I hate my life

This reverts commit d57e2000384a0176f11f4c1266fbea3ff102f068.

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[2e5bfe5be6...](https://github.com/Comxy/tgstation/commit/2e5bfe5be669d5222b68c7318349c4ac0947722b)
#### Sunday 2023-04-02 00:47:19 by LemonInTheDark

Refactors and optimizes breath code (Saves 12% of carbon/Life()) (#74230)

## About The Pull Request

### How things work

As things currently stand, when a mob breaths several things happen
(simplified to focus on the stupid)

We assert the existance of all possible breathable gases, and pull
partial pressures for them
Then we walk through all possible interactions lungs could have with
these gases, one by one, and see if they're happening or not
As we go we are forced to cleanup potential alerts caused by the
previous breath, even if those effects never actually happen
At the end we clear out all the unused gas ids, and handle the
temperature of the breath.

### What sucks

There's I'd say 3 different types of gas reactions.

- You can "need" a gas to survive. o2, n2 and plasma all fall into this
category
- A gas can do something to you while it's in your system. This applies
to most gas types
- Variation on the previous, some gases do cleanup when they're not in
your system, or when there isn't much of them in the first place

The main headache here is that second one, constantly cleaning up
potential side effects sucks, and fixing it would require a lot of dummy
variables

There's other suckage too.

Needing to constantly check for a gas type even if it isn't there is
stupid, and leads to wasted time It's also really annoying to do
subtypes in this system.
There is what amounts to a hook proc you can override, but you can't
override the reaction to a gas type.
It also just like, sucks to add new gases. one mega proc smells real
stupid.

### Improvements

In the interest of speed:

- I'd like to build a system that doesn't require manually checking for
gas
- Reacting to gas "disappearing" should be promoted by the system,
instead of being hacky.
- I would like to avoid needing to assert the existence of all possible
gases, as this is slow on both the assert and the garbage collect.

In the interest of dev ergonomics:

- It should be easy to define a new gas reaction 
- It should be easy for subtypes to implement their own gas reactions.
The current method of vars on the lung is all tangled up and not really
undoable as of now, but I'd like to not require it
- It should be possible to fully override how a gas is handled

### What I've Done

Lungs have 3 lists of proc paths stored on them

Each list handles a different way the lung might want to interact with a
gas.
There's a list for always processing on a gas (we use this for stuff
that's breathed), a list for handling a gas in our breath, and a list
for reacting to a gas previously being in our breath, but not any more.

Lungs fill out these lists using a helper proc during Initialize()
Then, when it comes time to breath, we loop over the gas in the breath
and react to it.
We also keep track of the previous list of partial pressures, which we
calculate for free here, and use that to figure out when to call the
loss reactions.

This proc pattern allows for overrides, easy reactions to removals,
lower indentation code and early returns, and better organization of
signal handlers

It's also significantly faster. Ballpark 4x faster

### Misc

Removes support for breathing co2, and dying from n2 poisoning. 
They were both unused, and I think it's cringe to clutter these procs
even further

Added "do we even have oxyloss" checks to most cases of passive
breathing.
This is a significant save, since redundant adjustoxy's are decently
expensive at the volume of calls we have here.

Fixes a bug with breathing out if no gas is passed in, assigning a var
to another var doesn't perform a copy

Rewrote breathe_gas_volume() slightly to insert gas into an immutable
mix stored on the lung, rather then one passed in
This avoids passing of a gas_mixture around just to fill a hole. 

I may change my mind on this, since it would be nice to have support for
temperature changing from a hot/cold breath.
Not gonna be done off bodytemp tho lord no.

Uses merge() instead of a hard coded version to move the gas ids over. 
This is slightly slower with lower gas counts but supports more things
in future and is also just easier to read.

## Why It's Good For The Game

Faster, easier to work with and read (imo)

Profiles: 

[breath_results_old.txt](https://github.com/tgstation/tgstation/files/11068247/breath_results_old.txt)

[breath_results_pre_master.txt](https://github.com/tgstation/tgstation/files/11068248/breath_results_new.txt)

[breath_results_new.txt](https://github.com/tgstation/tgstation/files/11068349/breath_results_new.txt)

(These profiles were initially missing #73026. Merging this brings the
savings from 16% to 12%. Life is pain)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[60d2d2ee1a...](https://github.com/Lamella-0587/Skyrat-tg/commit/60d2d2ee1ae4f7a3c8c93e14fdbd6c210a45cf04)
#### Sunday 2023-04-02 00:53:35 by SkyratBot

[MIRROR] Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% [MDB IGNORE] (#20118)

* Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33% (#74233)

## About The Pull Request
It is faster to operate on a gas list, especially if cached, then it is
to operate on a datum.
Doing this cause I'm seeing cost in merge() post #74230

Hits on a few other important places too. self_breakdown and such. Worth
it IMO

Could in theory go further by caching the global list. I'm tempted I
admit but it needs profiling first and it's late

EDIT: I have not slept, and have gone tooo far

[Micros /gas_mixture/copy and copy_from, adds a new proc to handle
copying with a ratio,
copy_from_ratio](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

[91da000](https://github.com/tgstation/tgstation/pull/74233/commits/91da0003daa9485962525d3e6bc9170a4c09876b)

The ADD_GAS sidestep saves us 0.1 seconds of init (used to at least.
Ensuring we don't break archive is gonna have a cost. I don't want to
profile this so I'll estimate maybe 0.05 seconds). The faster version of
copy_from is just well, better, and helps to avoid stupid

[Optimizes pipeline
processing](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

[bf5a2d2](https://github.com/tgstation/tgstation/pull/74233/commits/bf5a2d2d60554da2ce5fa1ac5f6c4179f6208cb2)

I haven't slept in 36 hours. Have some atmos optimizations

Pipelines now keep track of components that require custom
reconciliation as a seperate list.
This avoids the overhead of filtering all connected atmos machinery.

Rather then relying on |= to avoid duplicate gas_mixtures, we instead
use a cycle var stored on the mix itself, which is compared with a
static unique id from reconcile_air()
This fully prevents double processing of gas, and should (hopefully)
prevent stupid dupe issues in future

Rather then summing volume on the gas mixture itself, we sum it in a
local var.
This avoids datum var accesses, and saves a slight bit of time

Instead of running THERMAL_ENERGY() (and thus heat_capacity(), which
iterates all gases in the mix AGAIN) when processing gas, we instead
just hook into the existing heat capacity calculation done inside the
giver gases loop
This saves a significant amount of time, somewhere around 30% of the
proc, I think?

This doesn't tackle the big headache here, which is the copy_from loop
at the base of the proc.

I think the solution is to convert pipelines to a sort of polling model.
Atmos components don't "own" their mix, they instead have to request a
copy of it from the pipeline datum.
This would work based off a mutually agreed upon volume amount for that
component in that process cycle.

We'd use an archived system to figure out what gases to give to
components, while removing from the real MOLES list.

We could then push gas consumption requests to the pipeline, which would
handle them, alongside volume changes, on the next process.

Not sure how I'd handle connected pipelines... Merging post reconcile
maybe?
This is a problem for tomorrow though, I need to go to bed.

Saves about 30% of pipeline costs.
Profiles taken on kilo, until each reconcile_air hits 5000 calls

[old.txt](https://github.com/tgstation/tgstation/files/11075118/Profile.results.total.time.txt)

[new.txt](https://github.com/tgstation/tgstation/files/11075133/profiler.txt)

* Optimizes some gas_mixture procs, Optimizes pipeline processing significantly by 33%

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [omarcopires/canary](https://github.com/omarcopires/canary)@[8314f6a3e8...](https://github.com/omarcopires/canary/commit/8314f6a3e8c3b94242d43d4f754a6fb4fccf6461)
#### Sunday 2023-04-02 00:58:15 by Spiller

feat: add several missing bosses (#708)

• See the pull request description to read detailed information.

Add bosses from some quests there were not developed. This PR adds only the bosses, levers mechanics for simple functionality.
This doesn't add the bosses mechanics! If someone is willing to contribute with the mechanics, feel free to contribute with the PR.
The bosses added are:

• A pirate's tail: Ratmiral Blackwhiskers, Tentugly's head;
• Adventures of Galthen: Megasylvan Yselda;
• Feaster of Souls: The Fear Feaster, The Unwelcome, The Dread Maiden, Irgix the Flimsy, Unaz the Mean, Vok The Freakish;
• Grave Danger (rework): Lord Azaram, Duke Krule, Count Vlarkorth, Sir Nictros & Sir Baeloc, Earl Osam, King Zelos;
• Grimvale/Ancient Feud: Katex Blood Tongue, Srezz Yellow Eyes, Utua Stone Sting, Yirkas Blue Scales, Bloodback, Darkfang, Sharpclaw, Shadowpelt, Black Vixen;
• Soul War: Goshnar's Cruelty, Goshnar's Greed, Goshnar's Hatred, Goshnar's Malice, Goshnar's Spite, Goshnar's Megalomania;
• The Dream Courts: The Nightmare Beast, Izcandar the Banished, Alptramun, Plagueroot, Malofur Mangrinder, Maxxenius;
• The Secret Library: Ghulosh, Gorzindel, Lokathmor, Mazzinor, Scourge of Oblivion.
• The SoulWar reward was added. In order to get the reward, the player needs to kill all the bosses and the final boss.
• The Dream Court's World change was added.

• All the access needed were granted on FreeQuests.lua. If you are already running a server, you'll need to update freeQuestStage on config.lua to one number higher than it is. So, all the players of your server will have the access granted.

---
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[c0ef4ba907...](https://github.com/Donglesplonge/tgstation/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Sunday 2023-04-02 00:58:46 by tralezab

Adds the Dark Matt-eor when you emag a stupid amount of meteor shields + lots of meteor file sorting + qol + dark matter singularity + dark matt-eor summoning final traitor objective (#74330)

## About The Pull Request

<details>
  <summary>Dark Matt-eor Image</summary>
  

![image](https://user-images.githubusercontent.com/40974010/228368755-34ae5f89-e1bb-498b-bbf8-a14ff4240dc0.png)

</details>

> A barely visible blur in the cosmic darkness, like a ghostly shadow on
a moonless night. A piercing howl in the vacuum of space, as if it were
tearing the fabric of reality. A twisted halo of light around it,
bending and breaking the rays of distant suns. A shower of quantum
sparks, flickering and fading in its wake. A dark matter meteor (dark
matt-eor) is a wonder to witness, and to dread.

> A sudden impact, like a hammer blow to the heart of the station. A
violent tremor, shaking and shattering the metal walls and windows. A
deafening roar, as the air rushes out of the breached hull. A blinding
flash, as the dark matter meteor unleashes its hidden energy. A tiny
black hole, forming and growing in the center of the station. A
relentless pull, dragging everything towards the abyss. A dark matter
meteor is incredibly deadly.

Emagging too many meteor shields will summon a dark matt-eor. This comes
with several warnings, and after awhile, warns the station that someone
is trying to summon a dark matteor.

The dark matt-eor itself is not that damaging in its impact, but drops a
singularity in its final resting place.

## Why It's Good For The Game

It's a new way to terrorize a round as an antagonist. Before, emagging a
lot of meteor shields would basically make meteor showers the only event
that can run, which is cool, but since constant meteor waves are going
to destroy the station, let's also throw in the mother of all meteors!

This also adds warnings to spamming emagging meteor shields, which imo
needs it. The round ends when someone spams emagged meteor shields, and
since they're meteor shields nobody is going to reasonably check on
them.

## Changelog
:cl:
add: The dark matt-eor
add: Summon a dark matt-eor final traitor objective
add: Dark matter singularity variant, which can't grow as big as a
regular singularity but hungers for blood
code: cleaned up/sorted meteor shield code, satellite control, and more
qol: added a lot of feedback to interacting with meteor shields
balance: emagging a lot of meteor shields warns the station, but
emagging enough of them summons a Dark Matt-eor.
/:cl:

---
## [Donglesplonge/tgstation](https://github.com/Donglesplonge/tgstation)@[ccef887efe...](https://github.com/Donglesplonge/tgstation/commit/ccef887efec2cb3025228210bcb134700aac5175)
#### Sunday 2023-04-02 00:58:46 by san7890

Lints Against Unmanaged Local Defines (#74333)

# MAINTAINER - USE THE BUTTON THAT SAYS "MERGE MASTER" THEN SET THE PR
TO AUTO-MERGE! IT'S MUCH EASIER FOR ME TO FIX THINGS BEFORE THEY SKEW
RATHER THAN AFTER THE FACT.

## About The Pull Request

Hey there,

This took a while to do, but here's the gist:

Python file now regexes every file in `/code` except for those that have
some valid reason to be tacking on more global defines. Some of those
reasons are simply just that I don't have the time right now (doing what
you see in this PR took a few hours) to refactor and parse what should
belong and what should be thrown out. For the time being though, this PR
will at least _halt_ people making the mistake of not `#undef`ing any
files they `#define` "locally", or within the scope of a file.

Most people forget to do this and this leads to a lot of mess later on
due to how many variables can be unmanaged on the global level. I've
made this mistake, you've made this mistake, it's a common thing. Let's
automatically check for it so it can be fixed no-stress.

Scenarios this PR corrects:

* Forgetting to undef a define but undeffing others.
* Not undeffing any defines in your file.
* Earmarking a define as a "file local" define, but not defining it.
* Having a define be a "file local" define, but having it be used
elsewhere.
* Having a "local" define not even be in the file that it only shows up
in.
* Having a completely unused define*

(* I kept some of these because they seemed important... Others were
junked.)
## Why It's Good For The Game

If you wanna use it across multiple files, no reason to not make it a
global define (maybe there's a few reasons but let's assume that this is
the 95% case).

Let me know if you don't like how I re-arranged some of the defines and
how you'd rather see it be implemented, and I'd be happy to do that.
This was mostly just "eh does it need it or not" sorta stuff.

I used a pretty cool way to detect if we should use the standardized
GitHub "error" output, you can see the results of that here
https://github.com/san7890/bruhstation/actions/runs/4549766579/jobs/8022186846#step:7:792
## Changelog
Nothing that really concerns players.

(I fixed up all this stuff using vscode, no regexes beyond what you see
in the python script. sorry downstreams)

---
## [Hekzder/mojave-sun-13](https://github.com/Hekzder/mojave-sun-13)@[bdc9c58586...](https://github.com/Hekzder/mojave-sun-13/commit/bdc9c58586e0ab567e98b31054e8275d74990a58)
#### Sunday 2023-04-02 01:02:08 by Technobug14

Agriculture ('Technoculture') Farming: Fertilizer Edition :) (#2278)

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

* Fertilizer groundwork

Some stuff for fertilizer, need to add the attackby but cutting out a bunch of code to clean things up. Need to see if it breaks stuff.

* Fertilizer attackby changes

Adds code to the attackby for farm plots that checks if you're attacking it with fertilizer, doesn't work for some reason I can't tell. Also removes some vestigial TG botany stuff.

* fixt

fixes fertilizer, I forgot to specify something in a var, works now!!! YAY!!!

---
## [lessthnthree/Skyrat-tg](https://github.com/lessthnthree/Skyrat-tg)@[e8a8da18ae...](https://github.com/lessthnthree/Skyrat-tg/commit/e8a8da18aebc4cb3f742dc9d7810151e87abbf3b)
#### Sunday 2023-04-02 01:06:10 by SkyratBot

[MIRROR] Goliath-Infused Tendril Hammer uses an internal cooldown for the its special attack instead of a universal click cooldown [MDB IGNORE] (#20092)

* Goliath-Infused Tendril Hammer uses an internal cooldown for the its special attack instead of a universal click cooldown (#74159)

## About The Pull Request

Rather than using a click cooldown, the tendril hammer instead can make
its special heavy attack every 2 seconds.

## Why It's Good For The Game

In my newfound quest to try and eliminate universal click cooldowns or
weird non-interactivity timers as balancing factors, this definitely is
one of the biggest standout offenders. Lemme make an argument for
universal click cooldowns increases being an ineffective limitation.

I'll use the problems presented by the tendril hammer to highlight some
of those problems, as well as unique problems to the tendril hammer
itself.

<details>
  <summary>da big discussion</summary>

A) The functionality of the hammer actively inhibits all in-game handuse
interaction for several seconds, without explaining this to a player. As
a player, you won't know why this is happening, as universal click
cooldown is not present as a UI element.

B) Since universal click cooldowns are not visible to players, it might
feel more like the game is malfunctioning rather than being a deliberate
mechanic. Even if click cooldowns were visible, players probably would
think that the cooldown applies to the hammer, and not handuse
interactivity with the game world as a whole for several seconds.

C) The functionality of the hammer could work fine as an internal
cooldown on the hammer, only relevant to the hammer. This ensures that
its special effects are exclusive, without the need to interrupt player
interaction as a whole.

D) Since we're talking about miners. If someone is concerned about the
hammer being used on the station against carbon players; you need
someone to help mutate you into goliath mutant, which cannot be bypassed
whatsoever. An excellent example of something similar is the chainsaw
arm, created right next door to genetics in robotics, which does even
more force than the arm and is sharp. With the limitations that exist, I
think it probably discourages most powergaming, if that was even a
realistic concern (it really isn't).

E) You lose both a hand AND your gloves slot when you get the hammer. No
modsuits, no glove equipment, no two-handed equipment, and you now have
to juggle everything with one hand assuming you're not on your, once
again, universal click cooldown for several precious seconds. Miners
live or die in their rapid response to problems. This is also the total
sum of what you lose as a miner. That's a steep cost and it just doesn't
justify its own value compared to what you lose.

</details>

TL;DR - There is no offset to the cost of this weapon, it is strictly a
detriment because of poorly conceived implementation.

This is maybe one of the coolest ideas conceptually for the infusions so
far, heavily hampered by what seems to be an intense fear of the
mutation being _too useful_. So it was made _borderline masochistic to
willingly seek out and use_.

I want to see this actually be useful. I can't see this with the
restrictions it has. Hopefully this is enough to make it worthwhile
getting.

## Changelog
:cl:
balance: Changes the universal click cooldown of the tendril hammer from
the goliath infusion into an internal cooldown just for the special
heavy attack.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@ gmail.com>

* Goliath-Infused Tendril Hammer uses an internal cooldown for the its special attack instead of a universal click cooldown

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>
Co-authored-by: Jacquerel <hnevard@ gmail.com>

---
## [A5rocks/discord-api-docs](https://github.com/A5rocks/discord-api-docs)@[dd3f05a170...](https://github.com/A5rocks/discord-api-docs/commit/dd3f05a1709add398bac3a68af3cc27287f67038)
#### Sunday 2023-04-02 01:31:57 by Jerry Jiang

Document Silent Messages. (#5910)

Hey folks!

This is actually my 2022 hackweek project which I got to finish to
completion. :)

During a message send request, if you include the new
`SUPPRESS_NOTIFICATIONS` flag it will not broadcast any push/desktop
notifications but will still increment the relevant mention counters.

The intention is that you can get someone's attention but not feel like
you could be distracting them. Like when you DM someone at 5am. I'm sure some
bots can leverage this as well to avoid noise or something.

Also this should work for the webhook send request as well.

[Add a picture of the UI here]

If you're looking to leverage this as a non-bot, you can write `@silent`
as the _very first_ thing in a message. Make sure your client is
up-to-date btw. Autocomplete a-la `@everyone` is not planned. Eventually we may
put this in an "actual UI", for now this is where it lives. :)

Also sorry to all the users on Discord named silent who may have some
textual conflict now. Forgive me!

---
## [SkyN9ne/WindowsTerminal](https://github.com/SkyN9ne/WindowsTerminal)@[5a34d92cb5...](https://github.com/SkyN9ne/WindowsTerminal/commit/5a34d92cb5c99000e95f612cb8bc23ba374dd941)
#### Sunday 2023-04-02 01:35:02 by Dustin L. Howett

winget.yml: switch to manually using wingetcreate (#15023)

It was brought to my attention that we should be more restrictive in
which tasks we ovver a GitHub token to. Sorry!

With thanks to sitiom for the version parsing and the magic GitHub
action syntax incantation for determining what is a prerelease.

---
## [AOSP-Krypton/frameworks_base](https://github.com/AOSP-Krypton/frameworks_base)@[ca7809507c...](https://github.com/AOSP-Krypton/frameworks_base/commit/ca7809507c3b40a6eb47e7dd8822744d5901254c)
#### Sunday 2023-04-02 01:36:35 by Yohei Yukawa

Stop restoring ENABLED_INPUT_METHODS

This CL logically reverts the following CL to stop restoring
Settings.Secure.ENABLED_INPUT_METHODS during the new device/user
setup.

 * If0104151b3526da6ecc669adde3119a239ecafeb
   7b9a28c7f0a7b88ed1ea777edc05002d2d2b38b7

This CL also partially reverts the following CL because part of that
CL is no longer necessary.

 * I94b4039c9f54c341aec72b62579be3dd8bd84dbb
   964943ab98874a91be04f9ea2137861c93f6ffd3

In theory we should have been able to revert most of the following CL,
but other team it is already used by other projects so we cannot
revert it right now, unfortunately.

 * I01f5fafbbcfe3e3f5313829162ec011eaf2ad991
   2028ddaa5024dfc9844376f2032115aee360155a

Reason for revert:
At high level, we doubt restoring
Settings.Secure.ENABLED_INPUT_METHODS still benefits restore
experience for the user.

 * Anecdotally almost all IMEs maintain enabled languages with their
   per-app settings such as SheredPreference.  This observation leads
   us to think that we should focus more on stabilizing per-app
   backup/restore scenario at least for IME migration scenarios.

 * The code is not that simple and cost to maintain it is not that
   low.  If we reverted this code, we could spend our resources for
   other tasks, including improving restore experience for the user.

 * Stopping restoring ENABLED_INPUT_METHODS reduces chances to
   conflict with what the device policy says [1].

 * We have had a strict rule about what IMEs can be enabled
   automatically, and the rule has been that only pre-installed IMEs
   can be automatically enabled by the system, unless some system
   components that have WRITE_SECURE_SETTINGS permission overrides it.
   Mechanically enabling an IME just because it was enabled in the
   previous device does not fit this model well.

 * Since Android O MR1, we also backup/restore user languages
   specified in the global settings [2].  The default selected IME
   should be able to automatically enable language support based on
   the restored system locales.

 [1]: DevicePolicyManager#setPermittedInputMethods()
 [2]: I1e6c7ba5b7abb6bde8b01ce0f647c04a5caa81a6
      0f19cc779fb81bca0d00fd0a062f431cedb5f684

Fix: 72978240
Test: atest FrameworksCoreTests:android.provider.SettingsBackupTest
Test: atest FrameworksCoreTests:android.provider.SettingsValidatorsTest
Test: atest FrameworksCoreTests:com.android.internal.inputmethod.InputMethodUtilsTest
Change-Id: I122a8f69b2f75a9af85e14b66db764c5d153040e

---
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[b80b0797fb...](https://github.com/Kapu1178/daedalusdock/commit/b80b0797fbcc74ccee118ac829177b4a5a869f5b)
#### Sunday 2023-04-02 02:02:11 by LemonInTheDark

Macro optimizes SSmapping saving 50%  (#69632)

* 'optimizes' space transitions by like 0.06 seconds, makes them easier to read tho, so that's an upside

* ''''optimizes'''' parsed map loading

I'm honestly not sure how big a difference this makes, looked like small
percentage points if anything
It's a bit more internally concistent at least, which is nice. Also I
understand the system now.

I'd like to think it helped but I think this is kinda a "do you think
it's easier to read" sort of situation. if it did help it was by the
skin of its teeth

* Saves 0.6 seconds off loading meta and lavaland's map files

This is just a lot of micro stuff.
1: Bound checks don't need to be inside for loops, we can instead bound the iteration counts
2: TGM and DMM are parsed differently. in dmm a grid_set is one z level,
   in tgm it's one collumn. Realizing this allows you to skip copytexts and
   other such silly in the tgm implemenentation, saving a good bit of time
3: Min/max bounds do not need to be checked inside for loops, and can
   instead be handled outside of them, because we know the order of x
   and y iteration. This saves 0.2 seconds

I may or may not have made the code harder to read, if so let me know
and I'll check it over.

* Micro ops key caching significantly. Fixes macros bug

inserting \ into a dmm with no valid target would just less then loop
the string. Dumb

Anyway, optimizations. I save a LOT of time by not needing to call
find_next_delimiter_position for every entry and var set. (like maybe 0.5
seconds, not totally sure)
I save this by using splittext, which is significantly faster. this
would cause parsing issues if you could embed \n into dmms, but you
can't, so I'm safe.

Lemme see uh, lots of little things, stuff that's suboptimal or could be
done cheaper. Some "hey you and I both know a \" is 2 chars long sort of
stuff

I removed trim_text because the quote trimming was never actually used,
and the space trimming was slower then using the code in trim. I also
micro'd trim to save a bit of time. this saves another maybe 0.5.

Few other things, I think that's the main of it. Gives me the fuzzy
feelings

* Saves 50% of build_coordinate's time

Micro optimizing go brrrrr
I made turf_blacklist an assoc list rather then just a normal one, so
lookups are O(log n) instead of O(n). Also it's faster for the base case
of loading mostly space.

Instead of toggling the map loader right before and right after New()
calls, we toggle at the start of mapload, and disable then reenable if
we check tick. This saves like 0.3 seconds

Rather then tracking an area cache ourselves, and needing to pass it
around, we use a locally static list to reference the global list of
area -> type. This is much faster, if slightly fragile.

Rather then checking for a null turf at every line, we do it at the
start of the proc and not after. Faster this way, tho it can in theory
drop area vvs.

Avoids calling world.preloader_setup unless we actually have a unique
set of attributes. We use another static list to make this comparison
cheap. This saves another 0.3

Rather then checking for area paths in the turf logic, or vis versa, we
assume we are creating the type implied by the index we're reading off.
So only the last type entry will be loaded like a turf, etc.
This is slightly unsafe but saves a good bit of time, and will properly
error on fucked maps.

Also, rather then using a datum to hold preloader vars, we use 2 global
variables. This is faster.

This marks the end of my optimizations for direct maploading. I've
reduced the cost of loading a map by more then 50% now. Get owned.

* Adds a define for maploading tick check

* makes shuttles load again, removes some of the hard limits I had on the reader for profiling

* Macro ops cave generation

Cave generation was insanely more expensive then it had any right to be.
Maybe 0.5 seconds was saved off not doing a range(12) for EVERY SPAWNED
MOB.
0.14 was saved off using expanded weighted lists (A new idea of mine)
This is useful because I can take a weighted list, and condense it into
weight * path count. This is more memory heavy, and costs more to
create, but is so much faster then the proc.

I also added a naive implementation of gcd to make this a bit less bad.
It's not great, but it'll do for this usecase.

Oh and I changed some ChangeTurfs into New()s. I'm still not entirely
sure what the core difference between the two is, but it seems to work
fine.
I believe it's safe because the turf below us hasn't init'd yet, there's
nothing to take from them. It's like 3 seconds faster too so I'll be sad
when it turns out I'm being dumb

* Micros river spawning

This uses the same sort of concepts as the last change, mostly New being
preferable to ChangeTurf at this level of code.
This bit isn't nearly as detailed as the last few, I honestly got a bit
tired. It's still like 0.4 seconds saved tho

* Micros ruin loading

Turns out it saves time if you don't check area type for every tile on a
ruin. Not a whole ton faster, like 0.03, but faster.

Saves even more time (0.1) to not iterate all your ruin's turfs 3 times
to clear away lavaland mobs, when you're IN SPACE who wrote this.

Oh it also saves time to only pull your turf list once, rather then 3
times

---
## [KenAdeniji/WordEngineering](https://github.com/KenAdeniji/WordEngineering)@[2e4cbe148a...](https://github.com/KenAdeniji/WordEngineering/commit/2e4cbe148adc559743fecbc42450dbd44e3bf528)
#### Sunday 2023-04-02 02:48:19 by Ken Adeniji

Weee! - The Largest Asian and Hispanic Grocery Store in North America. A Bible engine. Nanda bent down to hide from a Caucasian male buyer. Nanda sold me cookies. Chocolate chip lunch bag cookies 18 count. Total price $2.99 08:15 AM Packaged by: Agnes C. Sell by: April 07 2023 You pay: $2.50 You save: $0.49 Freshness chocolate chip guaranteed. Freshness Oatmeal Raisin guaranteed. I left Charter Square and I am now at Pegasus Center. On who's expense I do better. At the intersection of Fremont Boulevard and Paseo Padre Parkway, South East. A male motorcyclist and a female riding at his back. Song music playing, Nobody does it better. At the intersection of Paseo Padre Parkway and Hall Way. A positioning of hatred. 19:30 ... 19:42 Microsoft Windows Operating System, Mozilla Firefox browser cite Chuck Missler data loss error.

---
## [Citadel-Station-13/Citadel-Station-13-RP](https://github.com/Citadel-Station-13/Citadel-Station-13-RP)@[d23ac504a0...](https://github.com/Citadel-Station-13/Citadel-Station-13-RP/commit/d23ac504a0963a99c4a598abf102cd51144a0ef5)
#### Sunday 2023-04-02 02:49:47 by Captain277

Ashlanders Phase 3.5: Prelude to War (#5259)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

_War is coming to Surt-nar-Vel'la. It rages in the caverns below, held
back only by the furious roiling blood of the Mother. More and more
Scori are driven up to Surt-nar-Vel'la, and they bring ancient secrets
with them. But, perhaps not all that dwells below should be
unearthed..._

1. **Increases Mother's Blessing from 5 minutes to 15.**
2. **Gives Ashlanders access to Sign Language.**
3. **Creates reagent Phlogiston.**
4. **Creates Condensed Phlogiston item.**
5. **Creates craftable Heaven Shaker hand-held explosive.**
6. **Buffs Shank riding speed.**
7. **Makes tying posts dense.**
8. **Adds craftable Primitive Splints.**
9. **Adds craftable Bone Pipes.**
10. **Adds the craftable Spark Striker.**
11. **Adds cowls.**
12. **Adds Ashlander cryo.**

## Why It's Good For The Game

1. _This buff is too short-lived to be used by the Ashlanders. I'm
raising it to 15 minutes. However, it is still fairly robust, so I might
drop it to 10. Or raise it even further if it's still too short._
2. _It's been months of lessons. Knowledge of primitive sign is now
available to most surface dwellers. It is slowly being disseminated
below the surface to those who are willing to learn, meaning those who
are likely to come to the surface may know it too._
3. _Phlogiston is the alchemical compound found in all explosive and
flammable things. Here I imagine it as a sticky tar similar to napalm or
condensed nitroglycerin._
4. _Condensed Phlogiston is basically semtex. Not much more to add
there._
5. _These craftable grenades require condensed phlogiston. They are
designed to address an impending threat, but will almost certainly need
to be nerfed and fine tuned. They come in two flavors: HE and Frag._
6. _Shanks now move slightly faster, providing a movement bonus to
mounted travel._
7. _Tying posts not being dense has bothered me for a while now._
8. _Gotta have a way to temporarily mend bones until surgery is done!_
9. _Apparently Ashlanders are missing avenues to fine tobacco - and
other substances. Perhaps a new avenue of trade..._
10. _Going to need lighters for your pipes._
11. _These are basically the hood parts of certain cloaks or jackets,
but toggleable as simple headwear._
12. _No longer will there be braindead Ashlanders sleeping in the
Temple!_

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
tweak: Increases duration of Mother's Buff.
tweak: Gives Scori Sign Language.
add: Adds Ashlander cryo.
add: Adds Phlogiston and Condensed Phlogiston.
add: Adds Heaven Shaker grenades, using phlogiston.
tweak: Buffs riding speed of Shanks.
tweak: Makes tying posts dense.
add: Adds craftable primitive splints.
add: Adds bone pipes.
add: Adds primitive lighters.
add: Adds cowls.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [AOSP-Krypton/frameworks_base](https://github.com/AOSP-Krypton/frameworks_base)@[bc2ae00878...](https://github.com/AOSP-Krypton/frameworks_base/commit/bc2ae008785cc23aa5fa2fe92b1f1d1efef6fb51)
#### Sunday 2023-04-02 03:08:53 by Jeff Sharkey

Magic to keep "_data" paths working.

As part of the storage changes in Q, we're removing the ability for
apps to directly access storage devices like /sdcard/.  (Instead,
they'll need to go through ContentResolver.openFileDescriptor() to
gain access.)  However, in several places we're returning raw
filesystem paths in the "_data" column.  An initial attempt to simply
redact these with "/dev/null" shows that many popular apps are
depending on these paths, and become non-functional.

So we need to somehow return "_data" paths that apps can manually
open.  We explored tricks like /proc/self/fd/ and FUSE, but neither
of those are feasible.  Instead, we've created a cursor that returns
paths of this form:

/mnt/content/media/audio/12

And we then hook Libcore.os to intercept open() syscalls made by
Java code and redirect these to CR.openFileDescriptor() with Uris
like this:

content://media/audio/12

This appears to be enough to keep most popular apps working!  Note
that it doesn't support apps that try opening the returned paths
from native code, which we'll hopefully be solving via direct
developer outreach.

Since this feature is a bit risky, it's guarded with a feature flag
that's disabled by default; a future CL will actually enable it,
offering a simple CL to revert in the case of trouble.

Bug: 111268862, 111960973
Test: atest cts/tests/tests/provider/src/android/provider/cts/MediaStore*
Change-Id: Ied15e62b46852aef73725f63d7648da390c4e03e

---
## [Odyssey-Games/TombstoneTunnels](https://github.com/Odyssey-Games/TombstoneTunnels)@[13dc7c909a...](https://github.com/Odyssey-Games/TombstoneTunnels/commit/13dc7c909a30b6c8e297a2416f353d6e87eabbf7)
#### Sunday 2023-04-02 03:10:30 by Magnus K

finally managed to get tilemap collision to work. still some weird collision response in some places but its like 5 am and i want to sleep and i fucking hate programing and my life and tilemap collisions

---
## [Chilledheart/boringssl](https://github.com/Chilledheart/boringssl)@[0d5b608614...](https://github.com/Chilledheart/boringssl/commit/0d5b6086143d19f86cc5d01b8944a1c13f99be24)
#### Sunday 2023-04-02 04:53:17 by David Benjamin

Maintain a frame pointer in aesni-gcm-x86_64.pl and add SEH unwind codes

Some profiling systems cannot unwind with CFI and benefit from having a
frame pointer. Since this code doesn't have enough register pressure to
actually need to use rbp as a general register, this change tweaks
things so that a frame pointer is preserved.

As this would invalidate the SEH handler, just replace it with proper
unwind codes, which are more profiler-friendly and supportable by our
unwind tests. Some notes on this:

- We don't currently support the automatic calling convention conversion
  with unwind codes, but this file already puts all arguments in
  registers, so I just renamed the arguments and put the last two
  arguments in RDI and RSI. Those I stashed into the parameter stack
  area because it's free storage.

- It is tedious to write the same directives in both CFI and SEH. We
  really could do with an abstraction. Although since most of our
  functions need a Windows variation anyway.

- I restored the original file's use of PUSH to save the registers.
  This matches what Clang likes to output anyway, and push is probably
  smaller than the corresponding move with offset. (And it reduces how
  much thinking about offsets I need to do.)

- Although it's an extra instruction, I restored the original file's
  separate fixed stack allocation and alloca for the sake of clarity.

- The epilog is constrained by Windows being extremely picky about
  epilogs. (Windows doesn't annotate epilogs and instead simulates
  forward.) I think other options are possible, but using LEA with an
  offset to realign the stack for the POPs both matches the examples in
  Windows and what Clang seems to like to output. The original file used
  MOV with offset, but it seems to be related to the funny SEH handler.

- The offsets in SEH directives may be surprising to someone used to CFI
  directives or a SysV RBP frame pointer. All three use slightly
  different baselines:

  CFI's canonical frame address (CFA) is RSP just before a CALL (so
  before the saved RIP in stack order). It is 16-byte aligned by ABI.

  A SysV RBP frame pointer is 16 bytes after that, after a saved RIP and
  saved RBP. It is also 16-byte aligned.

  Windows' baseline is the top of the fixed stack allocation, so
  potentially some bytes after that (all pushreg and allocstack
  directives). This too is required to be 16-byte aligned.

  Windows, however, doesn't require the frame register actually contain
  the fixed stack allocation. You can specify an offset from the value
  in the register to the actual top. But all the offsets in savereg,
  etc., directives use this baseline.

Performance difference is within measurement noise.

This does not create a stack frame for internal functions so
frame-pointer unwinding may miss a function or two, but the broad
attribution will be correct.

Change originally by Clemens Fruhwirth. Then reworked from Adam
Langley's https://boringssl-review.googlesource.com/c/boringssl/+/55945
by me to work on Windows and fix up some issues with the RBP setup.

Bug: b/33072965, 259
Change-Id: I52302635a8ad3d9272404feac125e2a4a4a5d14c
Reviewed-on: https://boringssl-review.googlesource.com/c/boringssl/+/56128
Reviewed-by: Adam Langley <agl@google.com>
Commit-Queue: David Benjamin <davidben@google.com>

---
## [andOlga/freedoom](https://github.com/andOlga/freedoom)@[944b790c93...](https://github.com/andOlga/freedoom/commit/944b790c931be9e42383cef9429750fd16883df5)
#### Sunday 2023-04-02 05:49:03 by mc776

dehacked: fix quit messages.

The messages hadn't been checked for length. Fortunately caught relatively early because the only string that shows up in vanilla (and thus would cause a crash) is also one of the longest ones.

I've also amended two things in the text itself:

1. big burly violent guy who's all about freedom and blaming scientists for things is...... not something that's aged well. And when a corporation is involved you know it's the investors pushing for the bad thing and not the actual researchers on the ground.

2. that other quit message literally reads like you're goading someone into suicide IRL, in the current environment where everybody's depressed and a lot of us have lost important people to plague or war or medical neglect or workplace accidents or violent bigotry or any combination thereof. I've taken the liberty to rephrase it so the emphasis is on what I think was intended.

Threw in a replacement for "exit to DOS" as well.

---
## [Kapu1178/daedalusdock](https://github.com/Kapu1178/daedalusdock)@[2f554f39d8...](https://github.com/Kapu1178/daedalusdock/commit/2f554f39d81bce889ba66cf8be2ed9929e26d879)
#### Sunday 2023-04-02 06:13:57 by Mothblocks

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
## [MrSamu99/Shiptest](https://github.com/MrSamu99/Shiptest)@[725233b42b...](https://github.com/MrSamu99/Shiptest/commit/725233b42b6f56551798a0a75b5362e577042de3)
#### Sunday 2023-04-02 06:50:26 by thgvr

The Lizardening Part One (And Friends) (#1845)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
This PR changes a lot of sprites. It's honestly too much. Namely:

- Explorer Equipment + Prototype
- Syndicate clothing
- Digitigrade lizard legs
- A new tail from Halcyon.
- Magboots from Zeta. Originally PR'd to tgstation.
- Colored (not greyscale! Ha Ha!) jumpsuits from Imaginos.

Heavy inspiration from the work of Imaginos, Halcyon, Mqiib, and
2cents#8442 for the original leg-work. (Haha, get it?)
The new digitigrade sprites started as a twinkle in the eye of Mqiib,
for yogstation(?) After myself and Halcyon saw those, an epihpany
struck. Perspective makes things cool and digitigrade perspective was
BAD.

I'll include a collage image of the new sprites if it's needed later.
Preview below:


![image](https://user-images.githubusercontent.com/81882910/228710332-0a213f88-5a8b-4b41-abdd-cee3b70ec403.png)
## Why It's Good For The Game
lizard,
Death of Codersprites
## Changelog

:cl:
add: New Digitigrade lizard sprites.
add: Various syndicate and mining clothing resprites.
add: Sarathi can now have an incredibly large tail.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [MrSamu99/Shiptest](https://github.com/MrSamu99/Shiptest)@[1c039c0623...](https://github.com/MrSamu99/Shiptest/commit/1c039c0623b6e8af463de0f0b1ca1ccc49050d94)
#### Sunday 2023-04-02 06:50:26 by Sun-Soaked

Botany Balance Pass (#1783)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
First came the content, now comes the hammer.

- Nukes Megaseed servitors from orbit. 
- Plants now age much, much slower and produce half as quickly.
Ruins that had them now have a ruined seed vendor that can be salvaged
for random seeds(and danger).
Ships that had one now have a crate with some thematic starting seeds,
and a Strange Seed.
Ghostrole Ruins that relied on having all seeds locally now have a
special biogenerator variant that can print a random seed for biomass.

- Adds Genesis Serum. This can be splashed on a tile to make natural
grass and some flora. Green your ship!
Genesis Serum was made a while ago, on request for a way to add natural
grass and flora to your ship. Since I had it lying around fully coded, I
thought I might as well pr it with botany changes.

- Gatfruit found in the seed vault have been replaced with Strange
Seeds.

- The chance to get Gatfruit from a demonic portal(plant variety) has
dropped from 15% to 5%.

- Corpse flowers now have liquid gibs and formaldehyde again. 

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Okay, hear me out

With this and Gardens, botany ships go from a "sit in your vessel for 2
hours" experience to an "explore and forage" one that better fits our
feature arc. It goes without saying that this **shouldn't be merged till
Overmap 4.2 is**, since it facilitates getting seeds from planets as
part of exploration.

Gatfruit are funny, but it takes exactly one seed getting into the hands
of a ship with a dna manipulator and the weapon balance is eradicated
from the game completely(for the round, at least.)
This is more problematic here then it was on TG, since our rounds tend
to be 5 hours long rather then 1.
This has been long coming. I'll reverse this if we ever get that
Plantlock variant we wanted a while ago.

Corpse flowers even have formaldehyde and gibs on tg, not sure what
happened there.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl: 
add: Ruined megaseed servitors can now be found on the frontier,
carrying a bounty of seeds for intrepid adventurers.
balance: the time it takes for plants to reach a lethal age has been
increased massively.
balance: Plant production time increased a bit to compensate.
balance: megaseed servitors have been removed from ships and ruins.
Ships that carried one now have a crate with some starting seeds.
balance: removes gatfruit from the seed vault pool.
balance: reduces the chance of getting gatfruit from a plant-themed
demonic portal significantly.
balance: corpse flowers once again have formaldehyde and liquid gibs.
add: Adds Genesis Serum, a reagent that transforms tiles into natural
grass on splash, then causes some natural flora objects to grow. Turn
your ship green!
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [Lothyriel/enigma_rust](https://github.com/Lothyriel/enigma_rust)@[614588ed84...](https://github.com/Lothyriel/enigma_rust/commit/614588ed844fe14d342355973aef26991bd704bd)
#### Sunday 2023-04-02 07:07:14 by João Xavier

I can't remember anything
Can't tell if this is true or dream
Deep down inside I feel to scream
This terrible silence stops with me

Now that the war is through with me
I'm waking up, I cannot see
That there's not much left of me
Nothing is real but pain now

---
## [Shroopy/Skyrat-tg](https://github.com/Shroopy/Skyrat-tg)@[6c978308c7...](https://github.com/Shroopy/Skyrat-tg/commit/6c978308c71cbd5b24e3242aec42b227461f9aaa)
#### Sunday 2023-04-02 08:17:16 by SkyratBot

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
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[7a64573c8b...](https://github.com/Lamella-0587/Skyrat-tg/commit/7a64573c8bfa01bac0d690db68d4b6528d502579)
#### Sunday 2023-04-02 08:50:23 by SkyratBot

[MIRROR] Atmos QOL + Small Sprite Fix [MDB IGNORE] (#20243)

* Atmos QOL + Small Sprite Fix (#74251)

## About The Pull Request
Added screentips and balloon alerts to many atmos machines/pipes
Volume pump overclocking overlay is much slower and less seizure
inducing
RPD screentips for right clicking pipes to copy settings
Removed (RPD) from the RPD's name since having an abbreviation in the
name is ugly
Crystallizer and electrolyzer use ctrl+click and alt-click to turn on
On examine electrolyzer tells you about anchoring to drain from APC
instead of cell
## Why It's Good For The Game
QOL for atmos stuff, user friendliness and better experience
## Changelog
:cl:
fix: Volume pump overclocking animation is much slower, no more
headaches
qol: Added screentips to the RPD; screentips and balloon alerts to many
atmos machines and devices
:cl:

* Atmos QOL + Small Sprite Fix

---------

Co-authored-by: 13spacemen <46101244+13spacemen@users.noreply.github.com>

---
## [Lamella-0587/Skyrat-tg](https://github.com/Lamella-0587/Skyrat-tg)@[ec67ffb340...](https://github.com/Lamella-0587/Skyrat-tg/commit/ec67ffb340b3c4a64f17eb6458a32cb55ae5183b)
#### Sunday 2023-04-02 08:50:23 by SkyratBot

[MIRROR] Properly accounts for byond tick fuckery in runechat code [MDB IGNORE] (#20237)

* Properly accounts for byond tick fuckery in runechat code (#74388)

## About The Pull Request

Ok so like, the agreed upon assumption for "verb like code" (stuff that
triggers when a client sents a network packet to the server), is it runs
in verb time, that sliver of time between maptick and the start of the
next tick.
We thought MeasureText worked like this. It doesn't.

It will, occasionally, resume not during verb time but as a sleeping
proc, at the start of the next tick.
Before the MC has started working.
This appears to only happen when the tick is already overloaded.

Unfortunately, it doesn't invoke after all sleeping procs as we were
lead to believe, but just like, like any sleeping proc.

This means it fights with the mc for cpu time, and doesn't respect the
TICK_CHECK macro we use to ensure this situation doesn't happen.

SOOO lets use a var off the MC instead, tracking when it last fired.
We can use this in companion with TICK_CHECK to ensure verbs schedule
properly if they invoke before the MC runs.

Hopefully this should fix 0 cpu when running at highpop

Thanks to Kylerace and MrStonedOne for suffering together with me on
this, I hate this engine.

* Properly accounts for byond tick fuckery in runechat code

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[c18b1ef442...](https://github.com/DrDiasyl/tgstation/commit/c18b1ef4423fc7d9083adac9b51aab4f169ea8aa)
#### Sunday 2023-04-02 09:13:09 by tralezab

End of Mapping March (Thanks to everyone who contributed, you're amazing!!!) (#74417)

## About The Pull Request

Removes the special mapping template. We got a really good turnout this
year! Will start counting ckeys and all that.

### But my mapping pr isn't done yet!

If it was opened during march, you'll get your token, don't worry

---
## [Profakos/orbstation](https://github.com/Profakos/orbstation)@[b3e5642d94...](https://github.com/Profakos/orbstation/commit/b3e5642d94caab455bea8b71e244081249cb2924)
#### Sunday 2023-04-02 09:46:53 by san7890

Fixes Active Turf Scenario on Tramstation (#74354)

## About The Pull Request

On the tin. Basically whenever `atmoscilower_2.dmm` would invoked
`atmoscilower_attachment_a_2.dmm`, it would trigger an active turf in
this location since it doesn't have a "ceiling". (as well as there being
an "aired" turf mingling with airless turfs)

This caused the following report:
```txt
 - All that follows is a turf with an active air difference at roundstart. To clear this, make sure that all of the turfs listed below are connected to a turf with the same air contents.
 - In an ideal world, this list should have enough information to help you locate the active turf(s) in question. Unfortunately, this might not be an ideal world.
 - If the round is still ongoing, you can use the "Mapping -> Show roundstart AT list" verb to see exactly what active turfs were detected. Otherwise, good luck.
 - Active turf: Station Asteroid (163,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (163,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (164,80,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (164,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,80,2) (/area/station/asteroid). Turf type: /turf/open/misc/asteroid/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,81,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/plating. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (166,81,2) (/area/station/asteroid). Turf type: /turf/open/floor/plating/airless. Relevant Z-Trait(s): Station.
 - Active turf: Lesser Starboard Maintenance (165,83,2) (/area/station/maintenance/starboard/lesser). Turf type: /turf/open/floor/iron/smooth. Relevant Z-Trait(s): Station.
 - Active turf: Station Asteroid (165,83,3) (/area/station/asteroid). Turf type: /turf/open/openspace/airless. Relevant Z-Trait(s): Station.
 - Z-Level 2 has 8 active turf(s).
 - Z-Level 3 has 1 active turf(s).
 - Z-Level trait Station has 9 active turf(s).
 - End of active turf list.
```

This is what it looked like when it was reproduced on my machine:


![image](https://user-images.githubusercontent.com/34697715/228689991-d9cc87c3-f931-4513-8399-928c93def605.png)


Surprisingly not that hard to debug, albeit tedious. At least I know
that this was the issue with 100% confidence.
## Why It's Good For The Game

Ate up 0.1 seconds of init on my machine. That's silly.
## Changelog
No way players care

---
## [amjoseph-nixpkgs/nixpkgs](https://github.com/amjoseph-nixpkgs/nixpkgs)@[454267ce5c...](https://github.com/amjoseph-nixpkgs/nixpkgs/commit/454267ce5c4725ba33e718c204e1cced938bb58d)
#### Sunday 2023-04-02 10:11:44 by Adam Joseph

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
## [PPUC/pinmame](https://github.com/PPUC/pinmame)@[a37fbbe90f...](https://github.com/PPUC/pinmame/commit/a37fbbe90f79865b4d1f48228b9f2acc925a9be3)
#### Sunday 2023-04-02 11:13:06 by toxie

address issue #102

cite from mjr:

The change to this file in commit 9ed410d, which is labeled as ported from MAME/MESS, adds a new bug, which affects DCS playback quality.

The changes are all to the implementation of the ABS (ABSOLUTE VALUE) instruction. The old version had an explicit CLR_S to clear the AS flag in ASTAT, whereas the new code deletes the CLR_S and substitutes CLR_FLAGS.

The addition of CLR_FLAGS is correct, since the instruction is documented as updating the AC-AN-AV-AZ flags. But the deletion of CLR_S is a bug, because the documentation also says that ABS must set or clear AS, according to the sign of the source operand. (See the ADSP 2100 User's Manual, 3rd edition, September 1995, section 15, ABSOLUTE VALUE (ABS) instruction: "AS: Set if the source operand is negative. Cleared otherwise.") CLR_FLAGS doesn't affect AS, so if AS was set going into the instruction, it'll still be set coming out, even if the operand was positive.

This isn't just a harmless bookkeeping detail - it actually breaks the DCS games in a subtle way! You can observe the effect of the bug on the DCS games by firing up ST-TNG LX7, going to the test menu, running the sound test, and letting track 1 ("1ST TUNE") run on auto-repeat. You'll hear a sort of flatulent distortion, which is occurring because that new ABS instruction bug is randomizing about 30% of the DCS frames decoded. It's actually affecting all of the tracks, but it seems to be more audible in tracks with lots of low bass frequencies, and just causes some annoying popping and crackling on most of the other tracks.

If anyone has been asking why the audio for all of the DCS games has been sucking lately, this is probably the answer.

Solution: Add back the CLR_S that was there before, right after the new CLR_FLAGS.

---
## [Pradyumn-101/Contest-Soln](https://github.com/Pradyumn-101/Contest-Soln)@[c09d893007...](https://github.com/Pradyumn-101/Contest-Soln/commit/c09d8930077a1521c14b8550baa1e9c3122c75ef)
#### Sunday 2023-04-02 12:14:05 by Pradyumn Gupta

Create Knight in Geekland

Knight is at (start_x,start_y) in Geekland which is represented by an NxM 2D matrix.
Each cell in the matrix contains some points. In the ith step, the knight can collect all the points from all the cells that can be visited in exactly i steps without revisiting any cell.
Also, the knight has some magical powers that enable him to fetch coins from the future i.e. If the knight can collect y coins in the xth step he can fetch all the coins that he will collect in the (x + y)th step and if the knight can collect z coins in the yth step he can fetch all the coins that he will collect in the (y + z)th step and so on without increasing the step count i.e. knight will stay on xth step and will get all the coins of the future steps mentioned above((x + y)th step coins + (y+z)th steps + ...).
Find the minimum number of steps required to collect the maximum points.
Note: The knight moves exactly the same as the knight on a chess board. Please follow 0 indexing.

Example 1:

Input:
n = 9
m = 10
start_x = 4, start_y = 5
arr =
0 0 0 2 0 2 0 2 0 0
0 0 2 0 2 0 2 0 2 0
0 2 0 0 1 2 0 0 0 2
0 0 2 0 2 0 2 0 2 0
0 2 0 2 0 0 0 2 0 2
0 0 2 0 2 0 2 0 2 0
0 2 0 0 0 2 0 0 0 2
0 0 2 0 2 0 2 0 2 0
0 0 0 2 0 2 0 2 0 0
Output: 1
Explanation: minimum knight have to take 1 steps to gain maximum points.
Initially, the knight has 0 coins, he will take 1 step to collect 1 point (sum of cells denoted in red color).
Now in the second step, he can collect points from all the cells colored green i.e. 64 points.
But with his magical power, at the 1st step, he can fetch points from the (1 + 1)th step. Therefore he can collect 1 + 64 coins at step 1 only. Hence answer is 1.
Example 2:

Input:
n = 3 
m = 3
start_x = 2, start_y = 1
arr =
7 6 8
9 1 4
6 2 8
Output:0
Explanation:
Initially, the knight has 2 points, or more formally we can say that at the 0th step knight has 2 points.
In the first step, he can collect points from cells (0, 0) and (0, 2) i.e. 15 points.
In the second step, he can collect points from cells (1, 0) and (1, 2) i.e. 13 coins.
In the third step, he can collect points from cells (2, 0) and (2, 2) i.e. 14 points.
In the fourth step, he can collect points from the cell (0, 1) i.e. 6 points.
So in each step, he can collect coins like -You can see in the below image  Knight can collect 15 coins in the 0th step only

Your Task:
You don't need to read input or print anything. Your task is to complete the function knightInGeekland() which takes 2-d array arr[][], starting coordinates of knight start_x, and start_y as input, and return an integer value as min steps to gain max points.

Expected Time Complexity: O(N*M)
Expected Auxiliary Space: O(N*M)

Constraints:
   1 <= len(arr), len(arr[0]) < 103
   0 <= values in arr <=100

---
## [Pickle-Coding/tgstation](https://github.com/Pickle-Coding/tgstation)@[7cc6934eff...](https://github.com/Pickle-Coding/tgstation/commit/7cc6934eff126c508436e1655fb5f79e24cf1767)
#### Sunday 2023-04-02 13:12:45 by LemonInTheDark

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
## [rik0612c/android_kernel_moto_shamu_t](https://github.com/rik0612c/android_kernel_moto_shamu_t)@[66b05f5640...](https://github.com/rik0612c/android_kernel_moto_shamu_t/commit/66b05f5640fa18aff21d457d85ef57a3435d1707)
#### Sunday 2023-04-02 13:48:00 by Masahiro Yamada

modpost: file2alias: go back to simple devtable lookup

commit ec91e78d378cc5d4b43805a1227d8e04e5dfa17d upstream.

Commit e49ce14150c6 ("modpost: use linker section to generate table.")
was not so cool as we had expected first; it ended up with ugly section
hacks when commit dd2a3acaecd7 ("mod/file2alias: make modpost compile
on darwin again") came in.

Given a certain degree of unknowledge about the link stage of host
programs, I really want to see simple, stupid table lookup so that
this works in the same way regardless of the underlying executable
format.

Signed-off-by: Masahiro Yamada <yamada.masahiro@socionext.com>
Acked-by: Mathieu Malaterre <malat@debian.org>
[nc: Omit rpmsg, sdw, fslmc, tbsvc, and typec as they don't exist here
     Add of to avoid backporting two larger patches]
Signed-off-by: Nathan Chancellor <natechancellor@gmail.com>
Signed-off-by: Sasha Levin <sashal@kernel.org>
Signed-off-by: Kevin F. Haggerty <haggertk@lineageos.org>
Change-Id: Ic632eaa7777338109f80c76535e67917f5b9761c

---
## [wrp/dotfiles](https://github.com/wrp/dotfiles)@[a8fe585267...](https://github.com/wrp/dotfiles/commit/a8fe585267ade20eef90447d6e8bd6d67be27412)
#### Sunday 2023-04-02 13:51:54 by William Pursell

Use awk vice grep to parse blacklist

Sigh.  2023 and still having to think about whitespace crap in names
PATH, etc. fundamentally relies on names being sane (ie, not containing
whitespace) but I keep bumping into vendors who do stupid crap like
making the directory in which they put executables have names with
horizontal whitespace, so you have to think about this.  But this is my
own personal dotfiles, so I can impose policy.  And policy is that
names do not contain stupid characters.  So we will not try to make
the code robust.  Grrr, this is annoying.

---
## [juniorohanyere/do_hard_things](https://github.com/juniorohanyere/do_hard_things)@[06f6a32830...](https://github.com/juniorohanyere/do_hard_things/commit/06f6a32830ced3fb1691cd6552a6f9e1e492920e)
#### Sunday 2023-04-02 15:55:56 by Twin J

Hmm,need to take my take my breakfast, omg, my breakfast at dinner time 😫, c is really hitting me hard 😣

---
## [matanco64/rustworkx](https://github.com/matanco64/rustworkx)@[e025356b04...](https://github.com/matanco64/rustworkx/commit/e025356b046a807e848a7c0ee2a32490927d46da)
#### Sunday 2023-04-02 17:33:54 by Matthew Treinish

Update tox configuration to use tox >= 4.4.0 (#851)

* Update tox configuration to use tox >= 4.4.0

Tox 4.0.0 was released in December 2022 [1] and was a major rewrite of
the internals of the package that included numerous backwards
incompatible changes [2]. Along with that major rewrite was a long
period of instability in the package with a flurry of 47 releases [3]
since 4.0.0 (which has only been 3-4 months). At the time of the 4.0.0
release we pinned the tox version in CI with #761 to avoid this
instability as our tox configuration was not compatible with tox 4.x.y
and tox was actually not compatible with how we had things configured
more generally. The hope was that tox would stabilize more, fix the
issues that plagued the tox 4 release series and we'd be able to relax
that pin without requiring bumping our minimum tox version to ensure
users could use either the old version or the new version locally.
However, since #761 that hope hasn't been realized the divergence
between tox 3 and tox 4 has only widened and at least personally I'm not
convinced of an improvement in stability to the tox 4 release series.
That being said however, this is becoming a developer pain as by default
when setting up a new build environment pip will install the latest
version of tox and we don't have an effective mechanism to pin the tox
version for users as you need to install tox manually as it's the
primary python development entrypoint we use. The only only avenue to
address this would be documentation updates in the CONTRIBUTING.md file,
which we didn't update at the time in #761 because it was meant to be
a version temporary pin that has turned out to not be so temporary.

Since it's been >3 months since we first pinned the tox version and that
pin was meant to be temporary this commit removes that pin and bumps our
minimum supported tox version to be 4.4.0, which despite not being
compatible with tox < 4 as we originally hoped, at least seems to work
fine with install rustworkx after updating the configuration file. This
should hopefully ease the onboarding experience for developers when
working with rustworkx and trying to bootstrap a local development
environment. Longer term I expect we'll look at moving off of tox,
as it no longer seems like a project we can rely on (especially as
a key component for our development and CI infrastructure) for rustworkx
and instead look at something like `nox` which I've heard good things
about and know that PyO3 had moved to it a year or two ago.

Fixes #812

[1] https://pypi.org/project/tox/4.0.0/
[2] https://tox.wiki/en/latest/upgrading.html
[3] https://pypi.org/project/tox/#history

* Stop using tox for retworkx backwards compat jobs

Tox's isolated builder mechanism seems to be incompatible with our
environment variable based package naming mechanism that we use to build
the legacy retworkx package. This is causing CI to fail on the backwards
compat jobs that are installing retworkx (which depends on rustworkx) to
ensure that our backwards compatibility shim works as expected. Instead
of trying to force tox to do the correct thing, it's just easier to stop
using it for that one CI job and instead just manually install and run
the tests.

---
## [artemiy-228/Practice-Work](https://github.com/artemiy-228/Practice-Work)@[94c0cd6797...](https://github.com/artemiy-228/Practice-Work/commit/94c0cd6797bf6140dbef2a45c11d3f7e0ab54aa1)
#### Sunday 2023-04-02 17:54:38 by artemiy-228

Laba 4

RUS: Здесь представлена лабораторная работа, на которой мы работали со строками. Тк у нас есть определенные ограничения, то нельзя было пользоваться множествами, поэтому задача H такая страшная) Кому надо, могу скинуть оптимальное, красивое и сексуальное решение этой задачи)
ENG: Here is my practice work, where we were working with strings. Because we have certain restrictions, we couldn't use "sets", thats the reasong why my solve for Task H is so ugly and scary. if you need, i can commit optimal, beautiful, wonderful and sexual solve for this task(sorry for my english, try to improve it)

---
## [jakobnunnendorf/SE_egrocery](https://github.com/jakobnunnendorf/SE_egrocery)@[a9e82943c0...](https://github.com/jakobnunnendorf/SE_egrocery/commit/a9e82943c0301876f8db2e043cc061d482586a8d)
#### Sunday 2023-04-02 18:03:51 by Pache

CHECKPOINT: backend connection failed for some stupid fucked up annoying bullshit reason

---
## [raghuvrao/misc-config](https://github.com/raghuvrao/misc-config)@[7fd8cc23ca...](https://github.com/raghuvrao/misc-config/commit/7fd8cc23ca89892a5c726c7617e17ffb4d78f5ed)
#### Sunday 2023-04-02 19:36:18 by Raghu V. Rao

Bash: use default prompt and terminal title

I am struggling with depression and anxiety due to what my home life has
become.  I am constantly being forced to do things that bring me no joy.
Work used to be something that brought me some happiness, but the
pressure there is also mounting.  As a result, I have become desperate
to find things that bring me happiness, however little it might be.

I obsess more than I like to admit about my shell prompt, to the point
of getting upset.  By letting go of this obsession, I hope to free at
least some part of my mind, in an effort to cope with everything else
that is going on.

The desire to keep going is diminishing each day, but I still must keep
going; there is at least one person for whom I want to be around.

---
## [swarm-game/swarm](https://github.com/swarm-game/swarm)@[a4c8057a28...](https://github.com/swarm-game/swarm/commit/a4c8057a28e043caed531e7d035efc2a41dc30a1)
#### Sunday 2023-04-02 19:41:02 by Brent Yorgey

Records (#1148)

Add record types to the language: record values are written like `[x = 3, y = "hi"]` and have types like `[x : int, y : text]`.  Empty and singleton records are allowed.  You can project a field out of a record using standard dot notation, like `r.x`.  If things named e.g. `x` and `y` are in scope, you can also write e.g. `[x, y]` as a shorthand for `[x=x, y=y]`.

Closes #1093 .

#153 would make this even nicer to use.

One reason this is significant is that record projection is our first language construct whose type cannot be inferred, because if we see something like `r.x` all we know about the type of `r` is that it is a record type with at least one field `x`, but we don't know how many other fields it might have.  Without some complex stuff like row polymorphism we can't deal with that, so we just punt and throw an error saying that we can't infer the type of a projection.  To make this usable we have to do a better job checking types, a la #99 . For example `def f : [x:int] -> int = \r. r.x end` would not have type checked before, since when checking the lambda we immediately switched into inference mode, and then encountered the record projection and threw up our hands.  Now we work harder to push the given function type down into the lambda so that we are still in checking mode when we get to `r.x` which makes it work.  But it is probably easy to write examples of other things where this doesn't work.  Eventually we will want to fully implement #99 ; in the meantime one can always add a type annotation (#1164) on the record to get around this problem.

Note, I was planning to add a `open e1 in e2` syntax, which would take a record expression `e1` and "open" it locally in `e2`, so all the fields would be in scope within `e2`.  For example, if we had  `r = [x = 3, y = 7]` then instead of writing `r.x + r.y` you could write `open r in x + y`.  This would be especially useful for imports, as in `open import foo.sw in ...`.  However, it turns out to be problematic: the only way to figure out the free variables in `open e1 in e2` is if you know the *type* of `e1`, so you know which names it binds in `e2`.  (In all other cases, bound names can be determined statically from the *syntax*.)  However, in our current codebase there is one place where we get the free variables of an untyped term: we decide at parse time whether definitions are recursive (and fill in a boolean to that effect) by checking whether the name of the thing being defined occurs free in its body.  One idea might be to either fill in this boolean later, after typechecking, or simply compute it on the fly when it is needed; currently this is slightly problematic because we need the info about whether a definition is recursive when doing capability checking, which is currently independent of typechecking.

I was also planning to add `export` keyword which creates a record with all names currently in scope --- this could be useful for creating modules.  However, I realized that very often you don't really want *all* in-scope names, so it's not that useful to have `export`.  Instead I added record punning so if you have several variables `x`, `y`, `z` in scope that you want to package into a record, you can just write `[x, y, z]` instead of `[x=x, y=y, z=z]`.  Though it could still be rather annoying if you wanted to make a module with tons of useful functions and had to list them all in a record at the end...

Originally I started adding records because I thought it would be a helpful way to organize modules and imports.  However, that would require having records that contain fields with polymorphic types.  I am not yet sure how that would play out.  It would essentially allow encoding arbitrary higher-rank types, so it sounds kind of scary.  In any case, I'm still glad I implemented records and I learned a lot, even if they can't be used for my original motivation.

I can't think of a way to make a scenario that requires the use of records.  Eventually once we have proper #94 we could make a scenario where you have to communicate with another robot and send it a value of some required type.  That would be a cool way to test the use of other language features like lambdas, too.

---
## [BarteG44/Shiptest](https://github.com/BarteG44/Shiptest)@[7f8874df29...](https://github.com/BarteG44/Shiptest/commit/7f8874df29bdd5624bc957907249edffbbeaba12)
#### Sunday 2023-04-02 19:58:45 by Zevotech

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
## [IAGamingWay/Minecraft-DC-Skinpack](https://github.com/IAGamingWay/Minecraft-DC-Skinpack)@[76be2cb587...](https://github.com/IAGamingWay/Minecraft-DC-Skinpack/commit/76be2cb5876d4333dbb1e497eb096222825e6c9f)
#### Sunday 2023-04-02 20:34:26 by IA

Description

Are you a fan of Minecraft and DC Comics? Then you'll love Minecraft-DC-SkinPack, a downloadable addon that allows you to transform your Minecraft character into your favorite DC heroes and villains. Choose from a range of skins inspired by characters such as Batman, Superman, Wonder Woman, Joker, Green Lantern, Flash, and many more. These skins are specially designed to fit seamlessly into the Minecraft world, so you can show off your fandom in-game without sacrificing the game's aesthetic.

Minecraft-DC-SkinPack is perfect for anyone who wants to inject a little bit of superhero action into their Minecraft experience. Whether you're battling enemies, exploring new worlds, or building epic structures, these skins will give you the power to do it all in style. Plus, with permission to use and modify the skin pack, you can create your own unique Minecraft-DC mashups and share them with the Minecraft community. Download Minecraft-DC-SkinPack today and become a superhero in your own Minecraft world!

---
## [MassMeta/tgstation](https://github.com/MassMeta/tgstation)@[d43ebd042d...](https://github.com/MassMeta/tgstation/commit/d43ebd042dd751842728e8cb91fa7fc1a82f26d0)
#### Sunday 2023-04-02 20:41:50 by san7890

Log Active Turfs To Mapping Log (#74267)

## About The Pull Request

Was reminded of doing this via
https://github.com/tgstation/tgstation/issues/74245#issuecomment-1483943979

They're mapping issues, so let's log them to the mapping log. Quite
shrimple honestly.


![image](https://user-images.githubusercontent.com/34697715/227805458-5e6bcf01-629d-4b81-ab6a-b26e63d41ca3.png)
## Why It's Good For The Game

As the comments expound, the reason why we probably haven't done this in
the past is because any number of things can cause active turfs (like
ruin placement (either in icebox or in space)), or other silly stuff
like that. Thus, finding stuff like this would only really be viable
with stuff like the View Active Turfs verb, where you could visually
jump to and see all of the active turfs in that dynamic configuration
(and this still remains the best way to find active turfs).

This PR just makes it easier to do a "post-mortem" analysis on potential
active turfs, so that if it's very blatant, it can be fixed a lot
easier. It's best to try and find them during an ongoing round, but this
is life. (same as the unit tests concession, not too enthused on that
but we would have spontaneous errors out the ass without _something_)
## Changelog
Nothing that concerns players.

---------

Co-authored-by: tattle <66640614+dragomagol@users.noreply.github.com>

---
## [EOBGames/tgstation](https://github.com/EOBGames/tgstation)@[2b76197397...](https://github.com/EOBGames/tgstation/commit/2b76197397b4241957e93a9779fdd9dfbada2688)
#### Sunday 2023-04-02 20:58:30 by Jacquerel

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
## [FireFlashie/Thelema-STG](https://github.com/FireFlashie/Thelema-STG)@[0b6a4b557d...](https://github.com/FireFlashie/Thelema-STG/commit/0b6a4b557d4e2e126ae6cb8790a74e279820c9ee)
#### Sunday 2023-04-02 21:10:48 by SkyratBot

Polishes some side sources of light and color [MDB IGNORE] (#19860)

* Polishes some side sources of light and color (#73936)

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

* Polishes some side sources of light and color

* yellow

* Update dance_machine.dm

* Merge branch 'upstream-merge-73936' of https://github.com/Skyrat-SS13/Skyrat-tg into upstream-merge-73936

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: Zonespace <41448081+Zonespace27@users.noreply.github.com>
Co-authored-by: lessthnthree <three@lessthanthree.dk>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [Willenbrink/dream](https://github.com/Willenbrink/dream)@[764bce3c8d...](https://github.com/Willenbrink/dream/commit/764bce3c8d6a687f018b5e5c455d000169dd4f2e)
#### Sunday 2023-04-02 21:15:32 by Thomas Leonard

Initial port to Eio

This is a proof-of-concept port of Dream to Eio. Most of the public API
in dream.mli has been changed to no longer use promises and the main
tutorial examples (`[1-9a-l]-*`) have been updated and are working.
The documentation mostly hasn't been updated.

Internally, it's still using Lwt in many places, using Lwt_eio to
convert between them.

The main changes are:

- User code doesn't need to use lwt (or lwt_ppx) now for Dream stuff.
  However, the SQL example still uses lwt for the Caqti callback.

- Dream servers must be wrapped in an `Eio_main.run`.
  Unlike Lwt, where you can somewhat get away with running other
  services with `Lwt.async` before `Dream.run` and relying on the
  mainloop picking them up later, everything in Eio must be started
  from inside the loop. Personally, I think this is clearer and less
  magical, making it obvious that Dream can run alongside other Eio
  code, but obviously Dream had previously made the choice to hide
  the `Lwt_main.run` by default.

- `Dream.run` now takes an `env` argument (from `Eio_main.run`),
  granting it access to the environment. At present, it uses this
  just to start `Lwt_eio`, but once fully converted it should also
  use it to listen on the network and read certificates, etc.

Error handling isn't quite right yet. Ideally, we'd create a new Eio
switch for each new connection, and that would get the errors. However,
connection creation is currently handled by Lwt. Also, it still tries to
attach the request ID to the Lwt thread for logging, which likely won't
work. I should provide a way to add log tags to fibres in Eio.

Note: `example/k-websocket` logs `Async exception: (Failure "cannot write to closed
writer")`. It does that on `master` with Lwt too.

---
## [francip/evals](https://github.com/francip/evals)@[ab5f7b2a89...](https://github.com/francip/evals/commit/ab5f7b2a89bcf60e8e93adfb2c70688c6d6ffd44)
#### Sunday 2023-04-02 21:41:14 by oscar-king

Counting bigrams in sentences (#302)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Bigram Counting

### Eval description

Tests whether the model is able to count the frequency of bigrams in a
sentence.

### What makes this a useful eval?

This is a very simple task for humans and it's possibly slightly more
'difficult' than counting the occurrences of a single letter.

Bigram frequencies are used in applications ranging from rudimentary NLP
tasks to cryptography.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"I'm
worried by the fact that my daughter looks to the local carpet seller as
a role model."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
found rain fascinating yet unpleasant."}],"ideal":"1"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"The
near-death experience brought new ideas to light."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the
frequency."},{"role":"user","content":"Separation anxiety is what
happens when you can't find your phone."}],"ideal":"0"}
{"input":[{"role":"system","content":"You will be presented with a
sentence. The task is to count the frequency of the bigram 'ng'. After
reading the sentence tell me the number of times the bigram appeared by
saying 'X' where 'X' is the frequency."},{"role":"user","content":"He
realized there had been several deaths on this road, but his concern
rose when he saw the exact number."}],"ideal":"0"}
  ```
</details>

---
## [francip/evals](https://github.com/francip/evals)@[b170a21cf3...](https://github.com/francip/evals/commit/b170a21cf32c47d841f64ec110cfd6796ec3f89a)
#### Sunday 2023-04-02 21:41:14 by Sam Ennis

Computer Science Theory (#83)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name
Computer Science based questions

### Eval description

Testing the models ability to answer multiple choice computer science
questions correctly

### What makes this a useful eval?

Tests whether it has the ability to answer time complexity, binary tree,
algorithmic computer science calculations.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [X] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [X] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [X] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [ ] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should
- [X] Check that your data is in `evals/registry/data/{name}`
- [X] Check that your yaml is registered at
`evals/registry/evals/{name}.jsonl`
- [X] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [X] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [X] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [X] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [X] I have filled out all required fields in the evals PR form
- [x] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"How many children does a
binary tree have? a) 2 b) any number of children c) 0 or 1 or 2 d) 0 or
1"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is/are the
disadvantages of implementing tree using normal arrays? a) difficulty in
knowing children nodes of a node b) difficult in finding the parent of a
node c) have to know the maximum number of nodes possible before
creation of trees d) difficult to implement"}],"ideal":"c"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What must be the ideal size
of array if the height of tree is ‘l’? a) (2^l)-1 b) l-1 c) l d)
2l"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What are the children for
node ‘w’ of a complete-binary tree in an array representation? a) 2w and
2w+1 b) 2+w and 2-w c) w+1/2 and w/2 d) w-1/2 and w+1/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"What is the parent for a
node ‘w’ of a complete binary tree in an array representation when w is
not 0? a) floor(w-1/2) b) ceil(w-1/2) c) w-1/2 d) w/2"}],"ideal":"a"}
{"input":[{"role":"system","content":"Choose the best multiple choice
answer to this question. Reply ONLY with the single letter of the answer
you have chosen."},{"role":"user","content":"If the tree is not a
complete binary tree then what changes can be made for easy access of
children of a node in the array? a) every node stores data saying which
of its children exist in the array b) no need of any changes continue
with 2w and 2w+1, if node is at i c) keep a seperate table telling
children of a node d) use another array parallel to the array with
tree"}],"ideal":"a"}
  ```
</details>

---
## [francip/evals](https://github.com/francip/evals)@[b5da073c21...](https://github.com/francip/evals/commit/b5da073c215c6453b99269a6dab2dca5454f04dd)
#### Sunday 2023-04-02 21:41:14 by somerandomguyontheweb

Add Belarusian lexicon eval (#372)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, __failure to follow
the guidelines below will result in the PR being closed automatically__.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access granted. 🚨

__PLEASE READ THIS__:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject since GPT-4 is already capable of completing the
task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. We encourage partial PR's with
~5-10 example that we can then run the evals on and share the results
with you so you know how your eval does with GPT-4 before writing all
100 examples.

## Eval details 📑
### Eval name

belarusian-lexicon

### Eval description

Test the model's ability to distinguish between existing and
hallucinated Belarusian words.

### What makes this a useful eval?

While the multilingual capability of recent GPT models is impressive,
there is still room for improvement. Many human languages are lagging
far behind English in terms of the model's ability to answer questions
and produce coherent texts in these languages, and the model's
"knowledge" of their lexicon and grammar is, to some extent,
hallucinated. One example is Belarusian, an East Slavic language spoken
by several million people. In my experience with ChatGPT, when the model
is prompted in Belarusian, its responses are sometimes ungrammatical or
semantically incoherent, and very often they contain made-up words – a
possible sign of overgeneralization based on Russian and Ukrainian data,
which are much more
[abundant](https://commoncrawl.github.io/cc-crawl-statistics/plots/languages)
on the web than Belarusian.

This eval contains 150 pairs of single-word prompts: one item in each
pair is a non-word hallucinated by ChatGPT (either totally meaningless
in Belarusian or violating the language's orthographic and phonetic
rules), and another item is an actual Belarusian word with similar
spelling. The model's task is to distinguish between words and
non-words. ChatGPT tends to label most items as existing words,
therefore its accuracy appears to be around 50%, and the negative-class
F measure is very low. Any competent speaker of Belarusian would perform
much better, and a language-specific tool, such as [this spell
checker](https://corpus.by/SpellChecker) or [this grammatical
database](https://bnkorpus.info/grammar.en.html) of Belarusian (also
available for
[download](https://github.com/Belarus/GrammarDB/releases)), would
flawlessly identify non-words.

## Criteria for a good eval ✅

Below are some of the criteria we look for in a good eval. In general,
we are seeking cases where the model does not do a good job despite
being capable of generating a good response (note that there are some
things large language models cannot do, so those would not make good
evals).

Your eval should be:

- [x] Thematically consistent: The eval should be thematically
consistent. We'd like to see a number of prompts all demonstrating some
particular failure mode. For example, we can create an eval on cases
where the model fails to reason about the physical world.
- [x] Contains failures where a human can do the task, but either GPT-4
or GPT-3.5-Turbo could not.
- [x] Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] Include at least 100 high quality examples (it is okay to only
contribute 5-10 meaningful examples and have us test them with GPT-4
before adding all 100)

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

This eval an attempt to point out specific deficiencies in the model's
ability to handle a lower-resource language (Belarusian). As such, it
might not only benchmark future refinements of Belarusian language
capability in the GPT models, but also serve as an instructuve example
for other language communities.

## Eval structure 🏗️

Your eval should
- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your yaml is registered at
`evals/registry/evals/{name}.yaml`
- [x] Ensure you have the right to use the data you submit via this eval

(For now, we will only be approving evals that use one of the existing
eval classes. You may still write custom eval classes for your own
cases, and we may consider merging them in the future.)

## Final checklist 👀

### Submission agreement

By contributing to Evals, you are agreeing to make your evaluation logic
and data under the same MIT license as this repository. You must have
adequate rights to upload any data used in an Eval. OpenAI reserves the
right to use this data in future service improvements to our product.
Contributions to OpenAI Evals will be subject to our usual Usage
Policies (https://platform.openai.com/docs/usage-policies).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgement

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and high volume of submissions, we will not
be able to accept all submissions and thus not grant everyone who opens
a PR GPT-4 access. We know this is disappointing, but we hope to set the
right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access
granted.

### Submit eval

- [x] I have filled out all required fields in the evals PR form
- [ ] (Ignore if not submitting code) I have run `pip install
pre-commit; pre-commit install` and have verified that `black`, `isort`,
and `autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data 

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкою"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абвязкаю"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абласці"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "вобласці"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмяну"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абмену"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абоўязак"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "абавязак"}], "ideal": "Y"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднасінькіх"}], "ideal": "N"}
{"input": [{"role": "system", "content": "You will be prompted with a
single word. Does this word exist in Belarusian language? Answer Y or
N."}, {"role": "user", "content": "аднюсенькіх"}], "ideal": "Y"}
  ```
</details>

---
## [kaylexis/Bubberstation](https://github.com/kaylexis/Bubberstation)@[7c419e721e...](https://github.com/kaylexis/Bubberstation/commit/7c419e721e959dd6df0ac01745f645bdcfcc2dbb)
#### Sunday 2023-04-02 21:46:10 by lexis

hell yeah i fixed everything

mainly fixed the fucked up SMES setup

---
## [rkovac14/ija2](https://github.com/rkovac14/ija2)@[42c5451c0a...](https://github.com/rkovac14/ija2/commit/42c5451c0a97dbc39cc8748b5c2db58c92544525)
#### Sunday 2023-04-02 21:49:55 by Shackooo

v0.30 patch notes
-We are proud to announce very successful patch, the moving of ghost is fully implemented along with collision with Pacman where if Pacman and Ghost move to the same field Pacman loses his fucking life.
-I have done a full rewrite of the moving function, so now it's not a hot garbage.

---
## [NewyearnewmeUwu/cmss13](https://github.com/NewyearnewmeUwu/cmss13)@[a2d5ca6e69...](https://github.com/NewyearnewmeUwu/cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Sunday 2023-04-02 22:39:45 by QuickLode

Introducing the Colonial Marshal ERT w/ Anchorpoint Marines (#2318)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
My first PR of this scale, for sure. 

Been working on this PR for two weeks off and on, and finally I believe
I have checked every box that I intended to check when I first thought
of this idea a couple months back in November or so. Original idea:
https://discord.com/channels/150315577943130112/1037030635820306562/1037030635820306562

It will be adding a Colonial Marshal Bureau ERT, a Colonial Marshal
Bureau Inspection Team, and an Anchorpoint Station ERT.

First: Anchorpoint Station, unlike many ERTs, this one will hail from a
station. The station is located in the Neroid Sector and is used as a
transit / refinery station. It's large enough to hold 3000 but never
reaches its full potential. It consists of four towers and a central
module - one of the towers houses a permanent CMB presence and in the
same tower, a contingent of Colonial Marines is onboard. There's also a
Seegson office but I didn't do anything with it here.
Reference: https://avp.fandom.com/wiki/Anchorpoint_Station

For standard inspections, a dropship is dispatched from Anchorpoint
Station to the USS Almayer to carry out their objectives.
I do expect this to be the primary usage of this entire PR, because
there was always a part lacking for Anti-Corporate/Anti-Smuggling/CMB
type of interactions. It was almost always focused on Corporate, or
USCM. Nothing else. You should consider this to be an HRP addition to
the game.

Its also important to note that the Colonial Marshals are **Colonial**
and UA law enforcement agents / investigative functionaries. **They
shouldn't be enforcing Marine Law** unless: 1. The CMP/aCO has requested
it, 2. The Colonial Marshal believes its in the best interest of the CMB
and 3. The CMB Office at Anchorpoint(admins) does not intervene to
change this decision. Jurisdiction is another interaction that will be
nice to see. Non-USCM suspects should be transferred to the CMB, and
vice versa. The CMB should also be handling crimes, especially with the
ICC, involving smuggling, black market activities, and corporate
corruption/cover-ups.

**The Colonial Marshal** - He leads the team, and should be an
experience player with some knowledge of the lore behind what they are
doing. There's objectives and a backstory to help guide players if they
are unaware.
**The CMB Investigative Synthetic** - Unlike what you would expect from
most Synthetics, this one(as the name implies) is purely for
investigative and/or law enforcement purposes, though they have brought
along a medical belt.
**The CMB Deputy** - Working under the lead of the Marshal, his loyal
deputies uphold Colonial Law, Earth Law, and help with investigations
and/or law enforcement should it be needed.
**Interstellar Commerce Commission Corporate Liaison** - This Executive
works with the Colonial Marshals specifically to observe proper trade
practices and investigate any possibilities of smuggling or black market
activity. They are also an advisory agent to the Marshals by giving them
an eye on the corporate side of things.
**Interstellar Human Rights Observer** - Through a lot of hard work, the
Observer has managed to make his way onto the frontier to document and
record any kind of atrocities that may be occurring in this dark sector
of space. It's a bit of a PR stunt, but the Observer might surprise you.
Also, in an emergency, the Observer may be able to provide medical aid
for the team - they are the most capable of it.


For Emergency Responses, a nearby dropship which was enroute to an
investigation of its own, is re-routed to the USS Almayer's distress
beacon. There is a 10% chance of this happening.
They will not fare very well in extended combat, because they are not
prepared for it. They simply come aboard to lend a helping hand to a
distress beacon.
As the Colonial Marshals are equipped for law enforcement and
investigations, they are comparably lightly armed to most things they
might encounter in or by the USS Almayer.

This is where the contingent of Colonial Marines in Tower 4 comes in.

The third ERT that may be called in is an Anchorpoint Station QRF Team.
Canonically this is purely used when a random-beacon is answered by the
CMB Patrol Team, and they are able to raise the radio back to base to
call in the QRF. Thus giving them an additional, albeit optional
objective. This is controlled entirely by admins, as the Anchorpoint QRF
Team, despite its small size and average skill levels, is equipped with
a decent amount of gear compared to the depleted stocks of the USS
Almayer. Should the CMB team be able to raise its own distress signal to
the preparing QRF team, admins may choose to grant, delay, or deny the
QRF entirely.



Those are the main points of the PR.
There are also small variation changes to CMB-related survivors and also
some changes to synths.dm. (I tried to refractor the code because the
last PR to it bugged out the way items spawn in, but I was unsuccessful
and those changes are not in this PR.)

Pizza ERT chance and Freelancer ERT chance was nerfed by 4 and 5
respectively. This gives room for this ERT, and also Pizza was a bit
LRP.. You see a ship burning with a giant hole in it and you go to
deliver a pizza...?

EDIT: Pizza ERT removed from rotation entirely a la morrow

I would love to give a great thanks to:
nauticall - for their awesome cap and badge sprites! Also they have just
been a great help to me for much of my time here :)
kitsunemitsu - for their CMB hud icons!
harryOB - for helping me with fixing my vars and procs in the main ERT!
I was able to make things a % chance thanks to him.
and forest2001 - for helping me troubleshoot and find a solution for a
really annoying piece of hud code.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

This is a great, non-combat ERT and extremely HRP addition which adds a
phenomenal avenue of RP to the game rarely seen before. There is someone
to investigate the CL, interact with survivors, give MPs someone to talk
to, take non-USCM prisoners, assist with CMB-survivors and especially
with the new Black Market update this ERT will have tons of potential to
bring really interesting dynamics to the Almayer. The Colonial Marshal
Bureau are a HRP oriented set of roles, perfect for mini-events.

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>
I have done extensive testing with this and believe I have figured out
pretty much every single bug. One thing I was not able to test was the
ERT messages for obvious reasons, but they seem to be sound - and a test
merge will definitely double check that.

In addition, there may or may not be a bug where the CMB cannot see
their own HUD Icons, but ghosts can just fine. I haven't been able to
find the cause of this yet.

https://media.discordapp.net/attachments/1042176396711170119/1064156692050358372/image.png</summary>

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

:cl: QuickLoad, nauticall, Kitsunemitsu, harryOB, forest2001
add: Introducing the Colonial Marshal Bureau Inspection and Emergency
Response Teams - A Law Enforcement & Investigative UA Functionary which
brings with it an HRP oriented set of roles perfect for your anti-corpo,
colonial, prisoner, smuggling, or other types of interactions on the
Almayer! It should unlock a very unique avenue of RP for many players,
especially smugglers, CL, survivors and the black market. This is a well
supported faction with their own frequencies, equipment, even faxes and
icons etcetera. The laws of the Earth stretch beyond the Sol.
add: Added the Anchorpoint Station Emergency QRF - A team of Colonial
Marines dispatched from Anchorpoint Station to respond to the CMB's
distress signal. Few in numbers, average in skills, but well equipped.
When things get dicey for the Marshals, they are the cavalry. This is an
admin call but makes it into an optional two-part ERT.
imageadd: Awesome looking CMB Cap, Marshal Badge and Deputy Badge by
nauticall!
imageadd: HUD Icons for each of the Colonial Marshal Bureau
Investigation Members, made by Kitsunemitsu!
imageadd: CMB key, hudsec and earpiece! Comes with a nice blue shale
radio color.
qol: Switched up some of the bugged synth loadouts, added some variety.
fix: Corrects the legacy path of hudsec where it was looking for old
paths instead of the updated ones - hudsec should work fine now. Thanks
to forest for his help in spotting these.
tweak: Superficial changes to cryo ERT loadout and CMB-relevant survivor
loadouts.
tweak: Superficial changes to armor vest so that they can carry
guns/lights.
tweak: Superficial changes to not being able to put on vests over
certain uniforms.
tweak: Freelancer ERT chance down from 25 to 20.
tweak: Synthetic vendor has some packs renamed for clarity, and receives
the tech welder satchel and medical satchel as an option.
del: Synthetic nurse hat is gone from Synthetics!
del: Pizza ERT is removed from rotation
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: naut <55491249+nauticall@users.noreply.github.com>
Co-authored-by: naut <nautilussplat@gmail.com>

---

