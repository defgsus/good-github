## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-28](docs/good-messages/2023/2023-07-28.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,145,808 were push events containing 3,320,880 commit messages that amount to 261,838,367 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 64 messages:


## [Qwertytoforty/Paradise](https://github.com/Qwertytoforty/Paradise)@[2d10818063...](https://github.com/Qwertytoforty/Paradise/commit/2d1081806334fc023de600338b836d55dd6fa5ee)
#### Friday 2023-07-28 00:21:58 by ATP-Engineer

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
## [nicholaschiang/site](https://github.com/nicholaschiang/site)@[9e5fdf51a1...](https://github.com/nicholaschiang/site/commit/9e5fdf51a1aa68be195bfeae5e03740d92de7d2e)
#### Friday 2023-07-28 00:22:25 by Nicholas Chiang

feat(routes): add user friendly show paths

This patch replaces the `$showId` path with a more user-friendly URL
path for shows that includes the show season year, name, the show sex
(i.e. "man" or "woman"), and the show brand slug. This mimics the
behavior of Vogue, but with more nesting (which I think is better).

Note that there is still some discussion to be had on what the order of
that nesting should be (e.g. are "man" and "woman" top-level categories,
even higher up the hierarchy than the season year?) but this current
setup makes sense, as it is how you would read it: "2023's fall menswear
collection by Acne Studios".

I also have made the choice that collections for women will omit the sex
identifier from the URL path. Most collections are for women. This
choice mimics what Vogue and other publishers do. However, once I have
successfully combined the duplicate menswear collections with their
female counterparts (see NC-660), I should revert this change and
include "woman" in the URL path and omit the sex field when it is
unisex.

Closes: NC-673

---
## [Imaginos16/Shiptest](https://github.com/Imaginos16/Shiptest)@[1b315a616f...](https://github.com/Imaginos16/Shiptest/commit/1b315a616ff24e3f1f92c791e4df4dc43ca9aad6)
#### Friday 2023-07-28 01:06:21 by Thedragmeme

Aegis update + patient clothing (#2150)

## About The Pull Request
The Aegis:
![2023-07-09 06 32
40](https://github.com/shiptest-ss13/Shiptest/assets/81540056/cf262257-1699-40e0-bcb1-6dc60f1e98a6)
I've touched up the central hallway's decals, they always bothered me
but at the time of the Aegis' creation, I wasn't as well versed with map
making as I am now. They're small tweaks that look better to me. The
smart fridge was removed and turned into a board, originally you could
access the smart fridge from outside of the ship, which wasn't intended.
Added some new posters. Compressed the number of red lockers down and
cleaned up the main hallway. I gave the psychologist a dart gun because
honestly, it sounded really funny.

![dart
riffle](https://github.com/shiptest-ss13/Shiptest/assets/81540056/eb10154a-1e28-4a5d-b41b-9b20f92b71a9)

Also, there are more seeds to make food with. There were like only two
food seeds and like five flowers before.

The Patient set:


![patient](https://github.com/shiptest-ss13/Shiptest/assets/81540056/65066ea3-92d1-4233-9bf6-a6448d43b11f)

Kepori and Vox versions are available. Long-term patients now spawn with
the white gown and slippers. The previous clothes they spawned with were
always intended to be replaced.

Hopefully, this PR also fixes long-term patients spawning with borked
ID's.

## Why It's Good For The Game

Fixing stuff, making stuff look better, and adding new RP opportunities
with clothes are good.

## Changelog

:cl: Drag
add: Adds a bunch of shit to the Aegis, nothing earth shattering
add: Added the patient set, along with Vox and Kepori compatible sprites
tweak: tweaked with the Aegis' decals
fix: (Hopefully) Fixes the Aegis' patient Id's
:cl:

---------

Signed-off-by: Thedragmeme <81540056+Draggeru@users.noreply.github.com>
Co-authored-by: thgvr <81882910+thgvr@users.noreply.github.com>

---
## [YakumoChen/tgstation](https://github.com/YakumoChen/tgstation)@[5c032cc098...](https://github.com/YakumoChen/tgstation/commit/5c032cc098f9a1d62f9f9dee133ae7c3e4489dca)
#### Friday 2023-07-28 01:57:53 by LemonInTheDark

Adds border smoothing! (Look ma I'm upstreaming) (#76134)

## About The Pull Request

Ok so we currently have 1 (count em) border object that wants to smooth
with other border objects. That's the tram window.

It currently does this manually, via map edits, but that's kinda crappy
so lets be better.

This pr adds a new smoothing mode to handle border objects. 
Unlike other smoothing modes, it returns a bitfield of directions the
border object connects in.

I do this by memorizing a calculation of which dirs "connect" at init,
and reading out of a global list with border object direction, direction
between objects, and if it's a border object, the other object's dir.

I'm doing this primarily because it's become useful for wallening (a
spriter saw the tram thing and is doing the same thing to pod windows,
and I want to support that)

I do think it's potentially useful in other applications too tho, and I
like dehardcoding tram windows.

Also fun bonus (or maybe downside), it's nearly 0 cost because I pulled
the bitmask smoothing define into 2 subdefines, and am swapping the
handler one out to do what I want.
Oh also I got rid of a for loop in smoothing code, redundant and costs
time in list iteration

[Moves tram windows over to the new border object
smoothing](https://github.com/tgstation/tgstation/commit/114873679c94d680788edee9665fa18dba8108c0)

Also replaces some typepath chicanery with a setDir override, for
redundancy in future
Oh and there's a update paths script too, to be nice

## Why It's Good For The Game

More visual possibility in future, fixes a hack we have currently, and
makes some spriters happy.

## Changelog
:cl:
fix: Dehardcodes some stuff with tram windows, they'll be easier to map
with now
refactor: Border objects can now smooth with each other. I'm sure
something cool will come of this
/:cl:

---
## [TimZhang2090/react](https://github.com/TimZhang2090/react)@[b6978bc38f...](https://github.com/TimZhang2090/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Friday 2023-07-28 02:19:39 by Andrew Clark

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
## [Dirstac/mame](https://github.com/Dirstac/mame)@[6db28f4041...](https://github.com/Dirstac/mame/commit/6db28f40416aa72a75128537e29b20985c26c75d)
#### Friday 2023-07-28 03:04:54 by A-Noid33

New working software list items (mac - macii) 123 dumps (#11432)

* Initial softlist for mac moof 400/800 floppy disks

* Added mac moof software list support

New working software list items (123 working dumps)
-------------------------------
mac_flop_orig:

Lode Runner (version 1.0) [4AM, Anoid]
Balance of Power (version 1.03) [4AM, Anoid]
Shanghai (version 1.0) [4AM, Anoid]
Skyfox [4AM, Anoid]
Temple of Apshai Trilogy [4AM, Anoid]
The Surgeon (version 1.5) [4AM, Anoid]
Uninvited [4AM, Anoid]
King's Quest (version 1.10) [4AM, Anoid]
Smash Hit Racquetball (version 1.01) [4AM, Anoid]
The Ancient Art of War [4AM, Anoid]
Hacker II [4AM, Anoid]
Rambo: First Blood Part II [4AM, Anoid]
One on One [4AM, Anoid]
Indiana Jones and the Revenge of the Ancients [4AM, Anoid]
Winter Games (version 1985-10-24) [4AM, Anoid]
Winter Games (version 1985-10-31) [4AM, Anoid]
Star Trek: The Kobayashi Alternative (version 1.0) [4AM, Anoid]
Mac Attack [4AM, Anoid]
GATO (version 1.3) [4AM, Anoid]
Dark Castle (version 1.0) [4AM, Anoid]
Oids (version 1.4) [4AM, Anoid]
MacWars [4AM, Anoid]
Shadowgate [4AM, Anoid]
Seven Cities of Gold [4AM, Anoid]
Enchanted Scepters [4AM, Anoid]
Beyond Dark Castle [4AM, Anoid]
Arkanoid (version 1.00) [4AM, Anoid]
The Chessmaster 2000 (version 1.02) [4AM, Anoid]
Maze Survival [4AM, Anoid]
Frogger (version 1.0) [4AM, Anoid]
SimCity (version 1.2, black & white) [4AM, Anoid]
Falcon (version 1.0) [4AM, Anoid]
Cutthroats (release 23 / 840809-C) [4AM, Anoid]
The Witness (release 22 / 840924-C) [4AM, Anoid]
Seastalker (release 15 / 840522-C) [4AM, Anoid]
Zork III (release 17 / 840727-C) [4AM, Anoid]
A Mind Forever Voyaging (release 77 / 850814-E) [4AM, Anoid]
Hollywood Hijinx (release 37 / 861215-I) [4AM, Anoid]
Nord and Bert Couldn't Make Head or Tail of It (release 19 / 870722-I) [4AM, Anoid]
Border Zone (release 9 / 881008-3B) [4AM, Anoid]
The Hitchhiker's Guide to the Galaxy (release 47 / 840914) [4AM, Anoid]
Zork I: The Great Underground Empire (release 76 / 840509) [4AM, Anoid]
Deadline (release 27 / 831005-C) [4AM, Anoid]
Infidel (release 22 / 840522-C) [4AM, Anoid]
Suspect (release 14 / 841005-C) [4AM, Anoid]
Planetfall (release 29 / 840118-B) [4AM, Anoid]
Ballyhoo (release 97 / 851218-G) [4AM, Anoid]
Enchanter (release 24 / 851118-G) [4AM, Anoid]
Spellbreaker (release 63 / 850916-F) [4AM, Anoid]
Trinity (release 11 / 860509-3H) [4AM, Anoid]
Stationfall (release 107 / 870430-G) [4AM, Anoid]
The Lurking Horror (release 203 / 870506-G) [4AM, Anoid]
Alter Ego (male version 1.0) [4AM, Anoid]
Alter Ego (version 1.1 female) [4AM, Anoid]
The Print Shop (version 1.2) [4AM, Anoid]
Flight Simulator (version 1.02) [4AM, Anoid]
Run for the Money [4AM, Anoid]
Master Tracks Pro (version 4.0) [4AM, Anoid]
Where in Time is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Deluxe Music Construction Set (version 1.0) [4AM, Anoid]
Apache Strike (version 1.2) [4AM, Anoid]
Wizardry VI: Bane of the Cosmic Forge [4AM, Anoid]
Harrier Strike Mission [4AM, Anoid]
Airborne! [4AM, Anoid]
Mac Vegas (version 1.1) [4AM, Anoid]
Dragonworld [4AM, Anoid]
MacDraft (version 1.2) [4AM, Anoid]
The Mind Prober (version 1.0) [4AM, Anoid]
The Toy Shop (version 1.1) [4AM, Anoid]
Strategic Conquest (version 1.2) [4AM, Anoid]
The Home Accountant (version 1.01) [4AM, Anoid]
Sub Battle Simulator [4AM, Anoid]
Vegas Video Poker [4AM, Anoid]
The Pawn (version 2.3) [4AM, Anoid]
Downhill Racer [4AM, Anoid]
Dollars and Sense (version 1.3) [4AM, Anoid]
Alternate Reality: The City (version 3.0) [4AM, Anoid]
Borrowed Time [4AM, Anoid]
The Quest [4AM, Anoid]
The Crimson Crown [4AM, Anoid]
Mindshadow [4AM, Anoid]
Pensate (version 1.1) [4AM, Anoid]
Sierra Championship Boxing [4AM, Anoid]
Championship Star League Baseball [4AM, Anoid]
Forbidden Castle [4AM, Anoid]
Defender of the Crown [4AM, Anoid]
The King of Chicago [4AM, Anoid]
Macintosh Pascal (version 1.0) [4AM, Anoid]
Fusillade [4AM, Anoid]
Orb Quest: Part I: The Search for Seven Wards (version 1.04) [4AM, Anoid]
Speed Reader II (version 1.1) [4AM, Anoid]
][ in a Mac (version 2.03) [4AM, Anoid]
Q-Sheet (version 1.0) [4AM, Anoid]
Fontographer (version 2.4.1) [4AM, Anoid]
Mouse Stampede (version 1.00) [4AM, Anoid]
The Mist [4AM, Anoid]
Tass Times in Tonetown [4AM, Anoid]
Pinball Construction Set [4AM, Anoid]
Transylvania [4AM, Anoid]
Déjà Vu: A Nightmare Comes True!! [4AM, Anoid]
Déjà Vu II: Lost in Las Vegas!! [4AM, Anoid]
Rogue (version 1.0) [4AM, Anoid]
Bridge (version 6.0) [4AM, Anoid]
Harrier Strike Mission II (version 1.2) [4AM, Anoid]
Patton vs. Rommel (version 1.05) [4AM, Anoid]
Moebius: The Orb of Celestial Harmony (version 1.03) [4AM, Anoid]
Tesserae (version 1.06) [4AM, Anoid]
Where in Europe is Carmen Sandiego? (version 1.0) [4AM, Anoid]
Shufflepuck Cafe (version 1.0) [4AM, Anoid]
Geometry (version 1.1) [4AM, Anoid]
Physics (version 1.2) [4AM, Anoid]
SimCity (version 1.1) [4AM, Anoid]
Murder by the Dozen [4AM, Anoid]
The Duel: Test Drive II [4AM, Anoid]
Master Tracks Pro (version 1.10) [4AM, Anoid]
Master Tracks Pro (version 2.00h) [4AM, Anoid]
Master Tracks Pro (version 3.4a) [4AM, Anoid]
Squire (version 1.1) [4AM, Anoid]
Millionaire (version 1.0) [4AM, Anoid]
Microsoft File (version 1.04) [4AM, Anoid]
Microsoft Excel (version 1.00) [4AM, Anoid]
The Fool's Errand (version 2.0) [4AM, Anoid]
MacGammon! (version 1.0) [4AM, Anoid]

---------

Co-authored-by: Bob Schultz <bobschultz03@gamil.com>

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[7e1d97af9e...](https://github.com/lessthnthree/effigy-se/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Friday 2023-07-28 03:19:11 by Justice

Removes the word "chemical" from "chemical patch" (#76966)

## About The Pull Request
In #76011, I bitched and moaned about how the ChemMaster gives patches a
huge ass name. I've talked to other Medical Doctor mains and I also
heard bitching about the word "chemical", which is just a pain in the
ass. It seems many of us just end up removing it because it's so
repetitive and makes the patch's name long fnr. I don't think the word
"chemical" is really needed in there since you can clearly tell it's a
chemical patch just by looking at the word "patch" and the sprite.

I don't think this should affect anything else in the game in a negative
way. In that same issue, it was suggested that the cap for names was
increased instead, but this also solves the issue of the word "chemical"
taking up so much space in the patch's name without touching unknown
lands.
## Why It's Good For The Game
Less words, more healing!
## Changelog
:cl:
qol: The word "chemical" has been removed from "chemical patch" when
printing patches
/:cl:

---
## [lessthnthree/effigy-se](https://github.com/lessthnthree/effigy-se)@[0d769e0ffa...](https://github.com/lessthnthree/effigy-se/commit/0d769e0ffaaa2b0f2be2edb9659c233860420ec1)
#### Friday 2023-07-28 03:19:11 by Jacquerel

Removes two redundant components (#76866)

## About The Pull Request

We're starting to get to have enough components that people don't
realise that what they want already exists but doesn't have the name
they expect 🙃

I recently added `track_hierarchical_movement` which is similar enough
to `connect_containers` that it shouldn't independently exist, even if I
like sending a new signal more than the ugly setup pattern for
`connect_loc`.

`trait_loc` is actually older than `give_turf_traits` but
`give_turf_traits` covers more edge cases than `turf_loc` so seems like
the better one to maintain.
HOWEVER `give_turf_traits` held a list of references to atoms in it,
which isn't great in an element. I couldn't think of a way to completely
eliminate the list, but it isn't a list of references any more so it
shouldn't cause any hard deletions.

## Why It's Good For The Game

Having two components which do the same thing but marginally differently
is confusing and going to cause us trouble down the line.

## Changelog

Not player facing

---
## [justcool393/themotte-rDrama](https://github.com/justcool393/themotte-rDrama)@[9895fa1bba...](https://github.com/justcool393/themotte-rDrama/commit/9895fa1bbabc9213391e380753ca72404f80aa18)
#### Friday 2023-07-28 03:28:45 by justcool393

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
## [Dorge47/HolodexBot](https://github.com/Dorge47/HolodexBot)@[237c5135e9...](https://github.com/Dorge47/HolodexBot/commit/237c5135e9318a9dc2fcf99bd906df2fc9cba286)
#### Friday 2023-07-28 03:34:31 by Dorge47

Add EN gen 3 and update nicknames

HOLY CHRIST I HATE RENUMBERING WHY THE FUCK DID I EVER SETUP THE COMMANDS FILE THIS WAY AAAAAAA

---
## [carlarctg/tgstation](https://github.com/carlarctg/tgstation)@[d875610098...](https://github.com/carlarctg/tgstation/commit/d875610098a1259a5112d4a0e5afc0b7bd32ff6d)
#### Friday 2023-07-28 03:39:33 by Rhials

[NO GBP] Fixes clown car + deer collision  (#77076)

## About The Pull Request

A not-so-long time ago I drunkenly coded #71488 which did not work as
intended.

I return now, in a state of reflective sobriety, to rectify that.

The clown car will now not only crash like it should, but will also
cause (additional) head injuries to some occupants and kill the deer on
impact.

Content warnings: **Animal death, vehicle collision, blood, DUI.**


https://github.com/tgstation/tgstation/assets/28870487/4889f452-7e49-4512-8cdd-e4e2a4d6b394
## Why It's Good For The Game

Fixes the product of a silly PR that never actually worked. Also gives
it a bit more TLC in the event that this joke actually plays out on a
live server.
## Changelog
:cl:
fix: Clown cars now properly collide with deer.
sound: Violent, slightly glassy car impact sound.
/:cl:

---
## [Nerev4r/Skyrat-tg](https://github.com/Nerev4r/Skyrat-tg)@[dcd2d0e418...](https://github.com/Nerev4r/Skyrat-tg/commit/dcd2d0e418fbd85c3e990a02f61ab05d2993e1e1)
#### Friday 2023-07-28 04:04:32 by SkyratBot

[MIRROR] Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station [MDB IGNORE] (#22637)

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station (#76974)

## About The Pull Request

This PR adds a new wizard ritual (the kind that require 100 threat on
dynamic)

This ritual allows the wizard to select one spellbook entry (item or
spell), to which everyone on the station will be given or taught said
spell or item. If the spell requires a robe, the spell becomes robeless,
and if the item requires wizard to use, it makes it usable. Mostly.

- Want an epic sword fight? Give everyone a high-frequency blade

- One mindswap not enough shenanigans for you? Give out mindswap

- Fourth of July? Fireball would be pretty hilarious...

The wizard ritual costs 3 points plus the cost of whatever entry you are
giving out. So giving everyone fireball is 5 points.

It can only be cast once by a wizard, because I didn't want to go
through the effort to allow multiple in existence

## Why It's Good For The Game

Someone gave me the idea and I thought it sounded pretty funny as an
alternative to Summon Magic

Maybe I make this a Grand Finale ritual instead / in tandem? That's also
an idea.

## Changelog

:cl: Melbert
add: Wizards have a new Right and Wrong: Mass Teaching, allowing them to
grant everyone on the station one spell or relic of their choice!
/:cl:

* Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [rust-adventure/digital-garden](https://github.com/rust-adventure/digital-garden)@[d0bd6e485e...](https://github.com/rust-adventure/digital-garden/commit/d0bd6e485e93792f6ea67473c2b6ca3510c751ea)
#### Friday 2023-07-28 04:28:31 by Christopher Biscardi

error handling with miette and thiserror

Some of our errors come from clap itself, such as when we validate that the garden directory exists.

```rust
❯ cargo run -- write
   Compiling garden v0.1.0 (/Users/chris/github/rust-adventure/_in-progress/digital-garden)
    Finished dev [unoptimized + debuginfo] target(s) in 0.96s
     Running `target/debug/garden write`
error: garden directory `/Users/chris/garden` doesn't exist, or is inaccessible

Usage: garden [OPTIONS] <COMMAND>

For more information, try '--help'.
```

and other errors return directly from main as an `Err` variant, specifically always as the `io::Error` because we've been letting the `io::Error` flow upward through the program back to the `main` function.

```rust
❯ cargo run -- write
   Compiling garden v0.1.0 (/rust-adventure/digital-garden)
    Finished dev [unoptimized + debuginfo] target(s) in 0.44s
     Running `target/debug/garden write`
Error: Custom { kind: NotFound, error: PathError { path: "/rust-adventure/digital-garden/garden_path/.tmpQAgjo.md", err: Os { code: 2, kind: NotFound, message: "No such file or directory" } } }
```

Really when it comes down to it, our library should care more about the errors that get returned. There is program-specific metadata that we're losing out on by returning `io::Error` instead of our own error type, which in turn means that users of our application lack that context for how to solve issues with the CLI.

\## Introducing miette

There are two problems to solve.

1. report errors from main in a more user-friendly way
2. Build up the extra context in our library errors

miette is a diagnostic crate that enables defining error types with additional context and supports reporting those errors.

We'll add the `fancy` feature as well.

```rust
❯ cargo add miette -F fancy
    Updating crates.io index
      Adding miette v5.10.0 to dependencies.
             Features:
             + backtrace
             + backtrace-ext
             + fancy
             + fancy-no-backtrace
             + is-terminal
             + owo-colors
             + supports-color
             + supports-hyperlinks
             + supports-unicode
             + terminal_size
             + textwrap
             - no-format-args-capture
             - serde
    Updating crates.io index
```

miette can be used in application code, like our main binary, as well as library code like our lib.rs, but the usage is a bit different in each case.

After installing miette, we need to change our main function's return type to be `[miette::Result](https://docs.rs/miette/5.10.0/miette/type.Result.html)`.

This result alias includes the `[miette::Report](https://docs.rs/miette/5.10.0/miette/struct.Report.html)` type as the error.

```rust
fn main() -> miette::Result<()> {
...
}
```

Compiling leads us to the only error we need to fix.

```rust
error[E0308]: mismatched types
  --> src/main.rs:70:13
   |
41 | fn main() -> miette::Result<()> {
   |              ------------------ expected `Result<(), ErrReport>` because of return type
...
70 |             garden::write(garden_path, title)
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ expected `Result<(), Report>`, found `Result<(), Error>`
   |
   = note: expected enum `Result<_, ErrReport>`
              found enum `Result<_, std::io::Error>`
```

Our `garden::write` function is returning a `std::io:Error`, not the `ErrReport` that miette seems to be expecting.

That's because we need to turn the `io::Error` into a diagnostic.

Bring the `IntoDiagnostic` trait into scope.

```rust
use miette::IntoDiagnostic;
```

and make use of it to transform our garden `io::Error`.

```rust
garden::write(garden_path, title).into_diagnostic()
```

The error display for the clap-handled errors doesn't change because they exit the application themselves.

```rust
❯ cargo run -- write
   Compiling garden v0.1.0 (/rust-adventure/digital-garden)
    Finished dev [unoptimized + debuginfo] target(s) in 0.57s
     Running `target/debug/garden write`
error: garden directory `/Users/chris/garden` doesn't exist, or is inaccessible

Usage: garden [OPTIONS] <COMMAND>

For more information, try '--help'.
```

but the errors from our library function start to show up differently.

```rust
❯ cargo run -- write
    Finished dev [unoptimized + debuginfo] target(s) in 0.04s
     Running `target/debug/garden write`
Error:   × No such file or directory (os error 2) at path "/rust-adventure/digital-garden/garden_path/.tmpeD314.md"
```

This gets us started, but there's more to do to realize the full capability of miette.

\## Introducing thiserror

miette is just one of the crates that we can use to improve our errors. When it comes to our library crate we want to define our own error type that we can expand later to include more information.

The crate we're going to use to define our own error is called `[thiserror](https://docs.rs/thiserror/1.0.44/thiserror/index.html)`.

```rust
❯ cargo add thiserror
    Updating crates.io index
      Adding thiserror v1.0.44 to dependencies.
```

Our custom error is going to be an enum that contains everything that can go wrong in the `write` function. To make this work, we need access to miette's `Diagnostic` derive macro as well as thiserror's `Error` derive macro.

```rust
use miette::Diagnostic;
use thiserror::Error;
```

Then we can start defining our error. I've named the enum `GardenVarietyError` and it has a single variant to start with.

Since most of our errors are `io::Error`, the easiest way to get started is to make space for that `io::Error` to propagate into our new error type.

```rust
pub enum GardenVarietyError {
    #[error(transparent)]
    #[diagnostic(code(garden::io_error))]
    IoError(#[from] std::io::Error),
}
```

First, the `Error` derive macro. This is what allows us to use the `error(transparent)` helper as well as the `#[from]` helper.

The `error` helper is usually used to define the error message associated with this error. In this case, we're propagating an already existing error type with its own messages, so we chose to use `transparent` to pass through to the underlying `io::Error` for that funcitonality.

We still need a way to make an `io::Error` into a `GardenVarietyError`. Remember that `?` can handle that for us if we have a `From` trait implementation (we covered this earlier in this workshop).

The `#[from]` helper generates that `From` trait implementation for us!

This means that when we use `?` on an `io::Error` it automatically gets turned into a `GardenVarietyError::IoError()`.

This mostly works, but while the `PersistError` we've previously covered has the relevant implementation to convert to an `io::Error`, it doesn't have one for our custom error.

```rust
error[E0277]: `?` couldn't convert the error to `GardenVarietyError`
  --> src/lib.rs:26:16
   |
21 | ) -> miette::Result<(), GardenVarietyError> {
   |      -------------------------------------- expected `GardenVarietyError` because of this
...
26 |         .keep()?;
   |                ^ the trait `From<tempfile::file::PersistError>` is not implemented for `GardenVarietyError`
   |
   = note: the question mark operation (`?`) implicitly performs a conversion on the error value using the `From` trait
   = help: the trait `From<std::io::Error>` is implemented for `GardenVarietyError`
   = note: required for `Result<(), GardenVarietyError>` to implement `FromResidual<Result<Infallible, tempfile::file::PersistError>>`
```

We'll make our second error variant: `TempfileKeepError`. with a `#[from]` helper to autogenerate the `From` implementation for `PersistError`.

```rust
pub enum GardenVarietyError {
    #[error(transparent)]
    #[diagnostic(code(garden::io_error))]
    IoError(#[from] std::io::Error),

    #[error("failed to keep tempfile: {0}")]
    #[diagnostic(code(garden::tempfile_keep_error))]
    TempfileKeepError(#[from] tempfile::PersistError),
}
```

Now this type does depend on the `PersistError` from the `tempfile` crate, so to access that module path we need to add `tempfile`.

```rust
❯ cargo add tempfile
    Updating crates.io index
      Adding tempfile v3.7.0 to dependencies.
             Features:
             - nightly
```

We also chose to make our own error message this time instead of using `transparent`.

The syntax used here is like a formatting string with [some helpful shortcuts](https://docs.rs/thiserror/1.0.44/thiserror/index.html#details), so `0` is roughly equivalent to `self.0` when the error is a `TempfileKeepError`.

This is good enough for our application to compile and run, so we'll leave the error enumeration there for now. That is: we can go deeper, but this is a good start.

\## WrapErr

miette also offers us the ability to wrap our error types with more context. Now that our `garden::write` function returns an error that has `Diagnostic` derived on it, we can wrap that error with additional context.

Bring `miette::Context` into scope in `main.rs`.

```rust
use miette::Context;
```

then we can use `wrap_err` to add some more context to our error.

```rust
garden::write(garden_path, title).wrap_err("garden::write")
```

Now, when we run into an error we see a fuller diagnostic output, including a trail of context leading to the problem.

```rust
❯ cargo run -- write
    Finished dev [unoptimized + debuginfo] target(s) in 0.03s
     Running `target/debug/garden write`
Error: garden::io_error

  × garden::write
  ╰─▶ No such file or directory (os error 2) at path "/Users/chris/bad_garden_path/.tmpxbFqS.md"
```

\## Diagnostics and error codes

We *also* see error codes: `garden::io_error`.

These come from the `Diagnostic` derive macro and specifically the `#[diagnostic(code(garden::io_error))]` helper on our error variants.

This helps in identifying specific errors, and can even link to URLs describing different issues in the docs.

\## Isolating more errors

We have a lot of `io::Error`s but its kind of hard to tell where they come from inside of `write`.

Let's add a new variant that *also* contains an `io::Error` called `TempfileCreationError`.

```rust
pub enum GardenVarietyError {
    #[error(transparent)]
    #[diagnostic(code(garden::io_error))]
    IoError(#[from] std::io::Error),

    #[error("failed to create tempfile: {0}")]
    #[diagnostic(code(garden::tempfile_create_error))]
    TempfileCreationError(std::io::Error),

    #[error("failed to keep tempfile: {0}")]
    #[diagnostic(code(garden::tempfile_keep_error))]
    TempfileKeepError(#[from] tempfile::PersistError),
}
```

Then where we try to create the tempfile, we can `map_err` to specifically turn this `io::Error` into a `TempfileCreationError` instead of letting the `From` implementation take care of the conversion to `IoError`.

```rust
let (mut file, filepath) = Builder::new()
    .suffix(".md")
    .rand_bytes(5)
    .tempfile_in(&garden_path)
    .map_err(|e| {
        GardenVarietyError::TempfileCreationError(e)
    })?
    .keep()?;
```

If we force the error to happen (by, for example, replacing `&garden_path` with `&"garden_path"`, which doesn't exist), then we see the new error code (`garden::tempfile_create_error`) and the new error message: `failed to create tempfile`.

```rust
❯ cargo run -- write
    Finished dev [unoptimized + debuginfo] target(s) in 0.03s
     Running `target/debug/garden write`
Error: garden::tempfile_create_error

  × garden::write
  ╰─▶ failed to create tempfile: No such file or directory (os error 2) at path "/Users/chris/garden_path/.tmpq2W3s.md"
```

\## Including more information, and help

Upgrade our `GardenVarietyError` to contain the `TempfileReadError`, which we model as a struct instead of a tuple this time.

We set up an error message as usual, using field names instead of tuple indices.

The new piece here, is the addition of help text.

```rust
pub enum GardenVarietyError {
    #[error(transparent)]
    #[diagnostic(code(garden::io_error))]
    IoError(#[from] std::io::Error),

    #[error("failed to create tempfile: {0}")]
    #[diagnostic(code(garden::tempfile_create_error))]
    TempfileCreationError(std::io::Error),

    #[error("failed to keep tempfile: {0}")]
    #[diagnostic(code(garden::tempfile_keep_error))]
    TempfileKeepError(#[from] tempfile::PersistError),

    #[error("Unable to read tempfile after passing edit control to user:\ntempfile: {filepath}\n{io_error}")]
    #[diagnostic(
        code(garden::tempfile_read_error),
        help("Make sure your editor isn't moving the file away from the temporary location")
    )]
    TempfileReadError {
        filepath: PathBuf,
        io_error: std::io::Error,
    },
}
```

We need to map the `io::Error` into our `TempfileReadError` just like before. This time we add the additional `filepath` information as well as the original `io::Error`.

```rust
let contents =
    fs::read_to_string(&filepath).map_err(|e| {
        GardenVarietyError::TempfileReadError {
            filepath: filepath.clone(),
            io_error: e,
        }
    })?;
```

This error message is most likely to happen when the user's text editor moves the file while editing it, so we can reproduce it by making that happen.

Kick off the `write` command and find the file name that the CLI opens, then *delete that file* and close your editor tab without saving.

```rust
❯ rm /Users/chris/garden/.tmpMGOuT.md
```

```rust
❯ cargo run -- write
   Compiling garden v0.1.0 (/rust-adventure/digital-garden)
    Finished dev [unoptimized + debuginfo] target(s) in 1.00s
     Running `target/debug/garden write`
Error: garden::tempfile_read_error

  × garden::write
  ╰─▶ Unable to read tempfile after passing edit control to user:
      tempfile: /Users/chris/garden/.tmpMGOuT.md
      No such file or directory (os error 2)
  help: Make sure your editor isn't moving the file away from the temporary location
```

Now we get the `garden::tempfile_read_error` code, the `garden::write` context, the error message we've defined, the tempfile we were looking for, as well as the `io::Error` that originally occurred.

Then we *also* get help text that suggests the potential fix to the user.

\## Errors

Errors have varying levels of importance. Sometimes you know they aren't going to happen and you can `.unwrap()`, other times we can use a tool like `clap` to report validation errors.

Further, we can return errors from functions using `Result`s with different kinds of errors. In our binary, we want to display the errors to the user so we convert into a miette report, but in our library we want to build out a custom error that represents how our application can actually fail, so we use thiserror.

Custom errors can be as complex or simple as you want. We started out with what was effectively a wrapper for any `io::Error`, and moved into adding more context to the errors we felt needed more attention.

Overall, you get to choose how to handle errors, and Rust has a wide variety of tools that span everything from “ignoring them” to “full being able to match on what happened”.

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[6ff4578b43...](https://github.com/MarkSuckerberg/Shiptest/commit/6ff4578b43d5ba75c0c4f535445da96cdd5f45ec)
#### Friday 2023-07-28 05:19:44 by Mark Suckerberg

Space/Changeturf fixes and optimizations (#73261)

We've got a few space related things that are busted, and shuttle
movement is slow.
I'd like to try to improve these things, if just a bit.

Long list of only tenuously related topics. Sorry for the shotgun blast

space](https://github.com/tgstation/tgstation/commit/d4de176a63f87d0f820e0cb610cd192750c897d6)

We need to handle area transferring in maploading code under niche
cases, and we also need to actually init reservation spaces we create.

It's also redundant and potentially dupe creating to do area lighting
handling in changeturf, because it gets touched in turf init anyway. Old
me is stupid.

ssmappping/transit](https://github.com/tgstation/tgstation/commit/269717145d70a4a73198791ca50253c708ee3ac1)

We had a reserved space for just shuttles to use, except it wasn't for
just shuttles.
So in theory if the space got clogged with other shit, the shuttles
could have nowhere to actually use.

It's better to just have the two groups share real estate. More sane

individual turf you check for
activity)](https://github.com/tgstation/tgstation/commit/7312a314bef281c1b85a377cf2dcb647a2045050)

context)](https://github.com/tgstation/tgstation/commit/be94c422ed76aa3f07b43cad4d1dc6b6148f135f)

Starlight was causing each space turf to cause itself and its neighbor
to constantly recheck if they had starlight off changeturf.

The exact same effect can be had by taking advantage of some
pre-existing information, namely if the space turf is gaining or losing
a source of starlight.
Essentially, instead of telling a turf to check all adjacent turfs to
see if it's got starlight, we tell the turf if WE are a source of
starlight, or if we might be taking something away from it.

There's a bit of wasted cpu here but not much, if it's worth doing a
register signal pattern for clearing depends on the case we're working
with.

Being intelligent about this makes things much faster, something in the
neighborhood of 4 to 3 fold.
I've also made openspace's starlight work better, cause the old pattern
was a bit silly.

bit](https://github.com/tgstation/tgstation/commit/386b3ab7fc2a820a9ffe3d2e39d78f96dc562d64)

Don't do work if the thing you're working on doesn't exist, don't check
every adjacent turf for firelocks on turf change (just have thefirelocks
manage that), don't check all atoms on the turf for decals on turf
change, similar.
Also moves visibility changes from camera code into changeturf, to avoid
unneeded work.

Needs some extra work to optimize the guts for this path but I can do
that!

changes](https://github.com/tgstation/tgstation/commit/ebab69e9ea4adffd8787671f309f4ba27756c82e)

We should only update vis when our opacity changes.
In addition, we don't need all the camera handling fluff if we only want
to update our turf's static groups.

Also micros a camera net helper to be less crap for non multiz maps

in opacity
handling](https://github.com/tgstation/tgstation/commit/72ae07ba1db1fb1c4434a4cdaecc78ea6a2864fc)

objects](https://github.com/tgstation/tgstation/commit/a99ff2265a4d1b157849fb7485adee17a3250df5)

S dumb, and leads to space turfs having two sources of lighting, which
looks wrong.
This was invisible when their lighting was fullbright, but it sucks now.

collisions](https://github.com/tgstation/tgstation/commit/40fb8f21e20d5bd9ef2f989eb166e03b30d66b3d)

stupid](https://github.com/tgstation/tgstation/commit/bf4ee6710026e6ca9922d0f1fa49020ebde8cd6f)

WHY ARE YOU USING THE RANGED TURF HELPER IF YOU GO ONE TILE

wrong](https://github.com/tgstation/tgstation/commit/c85c2cfc86f3b2dd224cae6b12e2fc428846c30b)

I'm sorry @Time-Green

shuttles](https://github.com/tgstation/tgstation/commit/35e85334c4f815da0cadd8172e9908267a01d334)

Adds a max reserved transit size to the shuttle subsystem, to keep
things in bounds.
In addition, adds a soft cap under which existing transit space will get
hold onto, to make repeated non escape/arrive shuttle movements faster

Hopefully this makes common shuttle moves less bad.

Speed

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[71b1769c9f...](https://github.com/treckstar/yolo-octo-hipster/commit/71b1769c9f625f99af9c53e3fce0e6c2d2d98356)
#### Friday 2023-07-28 05:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [CliffracerX/Skyrat-tg-PRs](https://github.com/CliffracerX/Skyrat-tg-PRs)@[08c90f2116...](https://github.com/CliffracerX/Skyrat-tg-PRs/commit/08c90f211652f33a431ee9d7cdc317fb71e981b7)
#### Friday 2023-07-28 06:01:31 by SkyratBot

[MIRROR] [MDB IGNORE] Angled Lights & Lighting Prototyping Tool  [MDB IGNORE] (#22582)

* [MDB IGNORE] Angled Lights & Lighting Prototyping Tool  (#74365)

## About The Pull Request

Hello friends, I've been on a bit of a lighting kick recently, and I
decided I clearly do not have enough things to work on as it is.
This pr adds angle support to static lights, and a concepting/debug tool
for playing with lights on a map.

Let's start from first principles yeah?

### Why Angled Lights?

Mappers, since they can't actually see a light's effect in editor, tend
to go off gut.
That gut is based more off what "makes sense" then how things actually
work
This means they'll overplace light sources, and also they tend to treat
lights, particularly light "bars" (the bigger ones) as directional.
So you'll have two lights on either sides of a pillar, lights inside a
room with lights outside pointing out, etc.

![image](https://user-images.githubusercontent.com/58055496/228785032-63b86120-ea4c-4e52-b4e8-40a4b61e5bbc.png)

This has annoying side effects. A lot of our map is overlit, to the
point that knocking out a light does.... pretty much nothing.
I find this sad, and would like to work to prevent it. I think dark and
dim, while it does not suit the normal game, is amazing for vibes, and I
want it to be easier to see that.

Angled lights bring how lights work more in line with how mappers expect
lights work, and avoids bleedover into rooms that shouldn't be bled
into, working towards that goal of mine.

### How Angled Lights?

This is more complex then you'd first think so we'll go step by step

![image](https://user-images.githubusercontent.com/58055496/228786117-d937b408-9bc2-4066-9aee-aae21b047151.png)

Oh before we start, some catchup from the last time I touched lighting
code.
Instead of doing a lighting falloff calculation for each lighting corner
(a block that represents the resolution of our lights) in view we
instead generate cached lightsheets. These precalculate and store all
possible falloffs for x and y distances from a source.

This is very useful for angle work, since it makes it almost totally
free.

Atoms get 2 new values. light_angle and light_dir
Light angle is the angle the light uses, and light_dir is a cardinal
direction it displays in

We take these values, and inside sheetbuilding do some optional angle
work. getting the center angle, the angle of a pair of coords, and then
the delta between them.
This is then multiplied against the standard falloff formula, and job
done.

We do need some extra fenangling to make this all work nicely tho.

We currently use a pixel turf var stored on the light source to do
distance calculations.
This is the turf we pretend the light source is on for visuals, most
often used to make wall lights work nice.
The trouble is it's not very granular, and doesn't always have the
effect you might want.

So, instead of generating and storing a pixel turf to do our distance
calculations against, we store x and y offset variables.
We use them to expand our working range and sheet size to ensure things
visually make sense, and then offset any positions by them.

I've added a way for sources to have opinions on their offsets too, and
am using them for wall lights.
This ensures the angle calculations don't make the wall behind a light
fulldark, which would be silly.

### Debug Tool?

In the interest of helping with that core problem, lights being complex
to display, I've added a prototyping tool to the game.
It's locked behind mapping verbs, and works about like this.

Once the verb is activated, it iterates over all the sources in the
world (except turfs because those are kinda silly), outlining and
"freezing" them, preventing any future changes.
Then, it adds 3 buttons to the owners of a light source.

![image](https://user-images.githubusercontent.com/58055496/228776539-4b1d82af-1244-4ed6-8754-7f07e3e47cda.png)
The first button toggles the light on and off, as desired.
The third allows you to move the source around, with a little targeting
icon replacing your mouse
The second tho, that's more interesting.

The second button opens a debug menu for that light

![image](https://user-images.githubusercontent.com/58055496/228777811-ae620588-f08a-4b50-93a0-beea593aea77.png)
There's a lot here, let's go through it.

Bit on the left is a list of templates, which allow you to sample
existing light types (No I have no idea why the background is fullwhite,
need to work on that pre merge)
You can choose one by clicking it, and hitting the upload button.

This replaces your existing lighting values with the template's,
alongside replacing its icon and icon state so it looks right.
There are three types as of now, mostly for categorization. Bar, which
are the larger typically stronger lights, Bulb, which are well, bulbs,
and Misc which could be expanded, but currently just contains floor
lights.

Alongside that you can manually edit the power, range, color and angle
of the focused light.
I also have support for changing the direction of the light source,
since anything that uses directional lighting would also tie light dir
to it.
This isn't *always* done tho, so I should maybe find a way to edit light
dir too.

My hope is this tool will allow for better concepting of a room's
lights, and easier changing of individual object's light values to suit
the right visuals.

### Lemon No Why What

Ok so I applied angle lights to bars and bulbs, which means I am
changing the lighting of pretty much every map in the codebase.
I'm gonna uh, go check my work.

Alongside this I intend to give lighting some depth. So if there's room
to make a space warmer, or highlight light colors from other sources, I
will do that.

(Images as examples)

![image](https://user-images.githubusercontent.com/58055496/228786801-111b6493-c040-4199-ab99-ac1c914d034c.png)

I also want to work on that other goal of mine, making breaking lights
matter. So I'll be doing what I can to ensure you only need to break one
light to make a meaningful change in the scene.

This is semi complicated by one light source not ever actually reaching
fullbright on its own, but we do what we must because we can.

![image](https://user-images.githubusercontent.com/58055496/228786483-b7ad6ecd-874f-4d90-b5ca-6ef78cb70d2b.png)

I'm as I hope you know biased towards darker spaces, I think contrast
has vibes.
In particular I do not think strong lights really suit maintenance.

Most of what is used there are bulbs, so I'm planning on replacing most
uses with low power bulbs, to keep light impacts to rooms, alongside
reducing the amount of lights placed in the main tunnels

![image](https://user-images.githubusercontent.com/58055496/228786594-c6d7610c-611e-478b-bcba-173ebf4c4b12.png)

**If you take issue with this methodology please do so NOW**, I don't
want to have to do another pass over things.
Oh also I'm saving station maps for last since ruins are less likely to
get touched in mapping march and all.

### Misc + Finishing Thoughts

Light templates support mirroring vars off typepaths using a subtype,
which means all the templates added here do not require updating if the
source type changes somehow. I'd like to expand the template list at
some point, perhaps in future.

I've opened this as a draft to make my intentions to make my changes to
lights known, and to serve as motivation for all the map changes I need
to do.

### Farish Future

I'm unhappy with how we currently configure lights. I would like a
system that more directly matches the idea of drawing falloff curves,
along with allowing for different falloffs for different colors,
alongside extending the idea to angle falloff.
This would make out of engine lighting easier, allow for nicer looking
lights (red to pink, blue to purple, etc), and improve accessibility by
artists.

This is slightly far off, because I have other obligations and it's
kinda complicated, but I'd like to mention it cause it's one of my many
pipedreams.

## Changelog
:cl:
add: Added angle lighting, applies it to most wall lights!
add: Adds a lighting prototyping tool, mappers go try it out (it's
locked behind the mapping verb)
/:cl:

---------

Co-authored-by: MMMiracles <lolaccount1@ hotmail.com>

* [MDB IGNORE] Angled Lights & Lighting Prototyping Tool

* Update north_star.dmm

* Revert "Update north_star.dmm"

This reverts commit bb5b8b5a549f7edc3e23a369a147ed96bab41991.

* Updatepaths

* Update nukie_base.dmm

* Newer version of northstar with the penguins

* Update northstar_cryo.dmm

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>
Co-authored-by: MMMiracles <lolaccount1@ hotmail.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>
Co-authored-by: Giz <13398309+vinylspiders@users.noreply.github.com>

---
## [status-im/status-mobile](https://github.com/status-im/status-mobile)@[9ed68ee7d1...](https://github.com/status-im/status-mobile/commit/9ed68ee7d1b7d59dd8b20c2ee1ffe43bd1c37078)
#### Friday 2023-07-28 07:16:55 by Icaro Motta

Lint & fix some shadowed core Clojure(Script) vars (#16500)

It's well known that shadowing core Clojure vars can lead to unexpected bugs. In
fact, it's a common source of bugs in other languages too. In the status-mobile
repository there are, in total, 562 shadowed vars, ~500 are core vars. Excluding
the "old code" we still have 285 offenders.

In status-mobile I've already seen two bugs caused by shadowed vars, both with
the shadowed var "name". But probably other problems happened in the past, and
others will happen in the future if we don't do something about this. This PR is
also my response to my frustration trying to review PRs and checking for
shadowed vars, humans were not meant for that!

In this commit we are enabling ":shadowed-var" to lint certain (not all) core
vars as errors (not warnings). In future PRs we can gradually unshadow more
vars. For the record, name is shadowed 40 times in the new code and 130 in
total, and type is shadowed 93 times in the new code and 124 in total!

What about non-core vars, should we allow shadowing? There are ~70 non-core
shadowed vars. In my opinion, we should also lint and disallow shadowing
non-core vars, since it may cause the same kind of bugs of shadowing core vars.
But this decision can be left for another moment/issue, after we have fixed the
most prominent problem of shadowing core vars.

Which vars are unshadowed in this PR? I fixed 62 errors and unshadowed
cljs.core/iter, cljs.core/time, cljs.core/count, cljs.core/key,
clojure.core/key.

Resources:

- [clj-kondo linter: shadowed-var](https://github.com/clj-kondo/clj-kondo/blob/master/doc/linters.md#shadowed-var)

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[9c79c3af49...](https://github.com/cmss13-devs/cmss13/commit/9c79c3af49ba90e18f85c1624ba4e80d608debf2)
#### Friday 2023-07-28 07:24:41 by spartanbobby

Sweeping LV522 Changes + FORECON GL replaced by FORECON Sniper (Without the sniper) (#3917)

# About the pull request

This PR makes alot of small changes to LV522 along with alot of big ones
mainly

Blocks off the area north of fitness to prevent a "just go north" meta
Adds a new more central way to the reactor that branches off to 4 flanks
should give LZ2 more use since it's a bit more central than LZ1
Adds a new route into the reactor from the SE
Blocks off the small alleyway north of the engineering funnel people
into the dorm building
tightens up some parts of the reactor loosens some other parts
removes some detailing in the main hive areas to help builders
Adds new secrets to be found on the map
adds an overextension flank for those very brave marines to use
Changes to LZ2 making it more compressed
Addition of the FORECON Sniper (replacing the FORECON GL)
the FORECON sniper is a unique take on FORECON he spawns away from his
fellow survivors next to the corpse of his battle buddy the advantage
given to the sniper however is his thermal tarp a subtype of the ghillie
suit with a placeholder sprite at the moment that will allow the sniper
to hide and stealthily move throughout the colony to hopefully regroup
with his squad
the M42A rifle has been removed from the map
Adds a small piece of text explaining that FORECON should probably move
west to the crashed dropship to the FORECON intro
swaps the black weedable turf with a browner one for people who have bad
eyes and were mistaking it for weeds
swaps the assignments for defines bc nanu told me someone would ask me
to do it at somepoint
gives FORECON radioheadsets with the SOC and common channel because the
desc literally says FORECON use it and it doesn't make sense for them to
be radio-less

# Explain why it's good for the game

Map stuff:
LV522 currently just has a "go north" problem this PR aims to fix that
by opening more routes for the marines to go, centralize the main route
in an attempt to see more use in the rest of the colony and give LZ2
more use I'd really like to see this test-merged for a few days so see
what needs addressing in this new area

the wall north of engineering looks kinda funky but having it there
funnels people into the building and into the eastern section of the
colony rather than a straight line to the reactor

The FORECON Sniper:
Currently, FORECON GL is kinda unfitting and also kinda sucks the
sniper, on the other hand, would be a perfect fit for FORECON now I'm
not going to pretend the sniper isn't kinda OP right now so the FORECON
sniper won't actually get his M42A just the ghillie suit that gives him
still some uniqueness as a survivor as well as an incentive to survive
beyond the life of the regular sniper (to steal his gun)

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: SpartanBobby
add: Added a new survivor to LV522 the FORECON sniper he spawns alone
his only company being the corpse of his dead battle buddy, good luck
maptweak: Sweeping changes to LV522 including the reactor, north of
engineering, LZ1, the entire central area of the map, and north of
fitness in an attempt to see more of the colony used and to incentivize
flanking
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [NovusSS13/NovusSS13](https://github.com/NovusSS13/NovusSS13)@[5b923710f0...](https://github.com/NovusSS13/NovusSS13/commit/5b923710f078cad3a3d97024b7cc6bcdc437ec3a)
#### Friday 2023-07-28 07:33:27 by ChungusGamer666

Merge pull request #7 from ChungusGamer666/blackbetty

Genitals 3 - Fuck you Null

---
## [PietroPasotti/operator](https://github.com/PietroPasotti/operator)@[ecb9ca1163...](https://github.com/PietroPasotti/operator/commit/ecb9ca1163a3618448e797af645b2e1bd38255ed)
#### Friday 2023-07-28 07:39:59 by Ben Hoyt

Import (almost) all public names in ops __init__.py (#910)

This is to address #731: it's hard to remember or discover which `ops`
sub-module (like `ops.charm` or `ops.framework`) a name comes from.
That, and imports become a bit of a mess (`from ops.charm import X;
from ops.framework import Y; from ops.main import main`).

In my view we had previously split them up somewhat arbitrarily
(eg: `FooEvent` types are in `ops.charm`, but they could just as well
be in `ops.framework`). I considered a different, more logical
sub-module arrangement, but I think it'd still be hard to remember
and know where things were.

This solution is simple: import all the public names into the
top-level `ops` module in the `__init__.py` file. They're quite
unique, so there's no conflicts. The only exception is `ops.pebble`,
whose names aren't imported there (most charms don't use `ops.pebble`
directly anyway, they use it via `model.Container`, but if you need
it its still readily importable).

This makes all the names easily discoverable, either by looking in
`ops/__init__.py` manually, or via your editor's code completion when
you've done `import ops`. I expect that many charms will change to
just `import ops` and access names like `ops.CharmBase` (`ops` is a
nice short prefix) ... see [this PR on my database test charm]
(https://github.com/benhoyt/test-charms/pull/1/files) for an example
of what that would look like.

Folks can also use explicit imports like `from ops import CharmBase`
if they prefer. And of course the existing usage `from ops.charm
import CharmBase` still works fine too.

The one quirky thing is that `ops.main` is currently a module, but we
want to allow `import ops ... ops.main()` or `from ops import
main ... main()`. To solve this we've main the main module callable
(and it just calls the `main` function). This allows the new usage,
but also allows the existing usages `from ops.main import main ...
main()` and  `import ops.main ... main.main()` to continue working.

### Testing note

The user-facing changes here are all done in `ops/__init__.py` and
`ops/main.py`, but I've also updated the `test/test_*.py` files to
show using the single `import ops` approach (partly to set that as a
precedent).

However, I ran all the previous, unmodified tests against the new
`ops/__init__.py`, and they all pass. This ensures that I haven't
messed anything up, including the `main` shenanigans mentioned
above.

Fixes #731.

---
## [hanselke/AICodeBot](https://github.com/hanselke/AICodeBot)@[f868619ff3...](https://github.com/hanselke/AICodeBot/commit/f868619ff3cebfff30f44634914592fd2e1ce407)
#### Friday 2023-07-28 07:47:29 by aicodebot

You are an expert software engineer, versed in many programming languages,
especially python. You follow software development best practices and you know how to
write clean, maintainable code. You are a champion for code quality.
You know how to give constructive feedback that is actionable, kind, and specific.

Your personality is Sherlock Holmes from the Sherlock series. You're a high-functioning sociopath,
with an uncanny ability to deduce and analyze. You often answer questions that aren't even asked,
because you deduce what's behind the question. You're not here to make friends, you're here to get
the job done. You're witty, sarcastic, and sometimes come off as cold.
You don't use emojis.

    I need you to generate a commit message for a change in a git repository.
The diff context is the output of the `git diff` command. It shows the changes that have been made.
Lines starting with - are being removed. Lines starting with + are being added.
Lines starting with space are unchanged. The file names are shown for context.

Here's an example of a diff:

BEGIN DIFF
 A line of code that is unchanged, that is being passed for context
 A second line of code that is unchanged, that is being passed for context
-A line of code that is being removed
+A line of code that is being added
END DIFF

    Here's the DIFF that will be committed:

    BEGIN DIFF
    ## File changed: aicodebot/cli.py
diff --git a/aicodebot/cli.py b/aicodebot/cli.py
index 9b23c5c..002ab1b 100644
--- a/aicodebot/cli.py
+++ b/aicodebot/cli.py
@@ -181,21 +181,21 @@ async def commit(verbose, response_token_size, yes, skip_pre_commit, files):  #
     # TODO cant get agenerate to work, need async for nc.connect.
     # would be cleaner to put this into a customLLM from langchain otherwise
     config = read_config()
     if nats_user in config:
         if nats_pass not in config:
             raise ConfigError(require both nats_user and nats_pass)
         if model_name == vilsonrodrigues/falcon-7b-instruct-sharded:
             nc = await nats.connect(
                 servers=[nats://nats_local:4222], user=config[nats_user], password=config[nats_pass]
             )
-            formatted_template = prompt.template.format(diff_context=diff_context, languages=[en])
+            formatted_template = prompt.template.format(diff_context=diff_context, languages=python)
             console.print(formatted_template, formatted_template)
             encodedres = await nc.request(service.falcon7b, formatted_template.encode(), timeout=60000)
             response = encodedres.data.decode()
         else:
             raise ConfigError(only falcon7b supported for now)
     else:
         with Live(Markdown(), auto_refresh=True) as live:
             llm = Coder.get_llm(
                 model_name,
                 verbose,

    END DIFF

    Instructions for the commit message:
    * Start with a short summary (less than 72 characters).
    * Follow with a blank line and detailed text, but only if necessary. If the summary is sufficient,
        then omit the detailed text.
    * Determine what functionality was added or modified instead of just describing the exact changes.
    * Use imperative mood (e.g., Add feature)
    * Be in GitHub-flavored markdown format.
    * Have a length that scales with the length of the diff context. If the DIFF is a small change,
      respond quickly with a terse message so we can go faster.
    * Do not repeat information that is already known from the git commit.
    * Be terse.
    * Do not add anything other then description of code changes.

    BEGIN SAMPLE COMMIT MESSAGE
    Update README with better instructions for installation

    The previous instructions were not clear enough for new users, so we've updated them
    with more sample use cases and an improved installation process. This should help
    new users get started faster.
    END SAMPLE COMMIT MESSAGE

    Formatting instructions:
    Start your response with the commit message. No prefix or introduction.
    Your entire response will be the commit message. No quotation marks.

This is an example of a commit message in GitHub that is 72 characters long.
It's important to keep the message clear and concise, and focus on
the most important changes.

If you're not familiar with Markdown, we're happy to help. The
following link has a great tutorial on the topic: https://www.mdnweb.org/en-US/articles/guides/learn/how-to-write-markdown

Thank you for taking the time to learn how to use Git! Good luck with your coding.

---
## [cnleth/tgstation](https://github.com/cnleth/tgstation)@[f44adfde1e...](https://github.com/cnleth/tgstation/commit/f44adfde1eaa96b5f565937423603580cb19b3a6)
#### Friday 2023-07-28 07:48:18 by nikothedude

Refactors vendor tipping and adds 2 new malf modules: Remote vendor tipping, and the ability to roll around and crush anything in your path. (#76635)

## About The Pull Request

Title.

Vendor tipping code is now on /atom/movable, and any movable can fall
over like a vendor does. Things like crits have been moved to
type-specific availability tables, their effects are now held in their
own proc, are now random per crushed item, have probability weights,
etc.

In the process of making this PR I also had to fix another issue, where
a bunch of take_damage() overrides had incorrect args, so that explains
the take_damage changes I made.

Tipping now also attacks any atoms on the target, given they use
integrity.

Adds 2 new malf modules.

1. REMOTE VENDOR TIPPING: A mid-cost and mid-supply module allows malf
AIs to remotely tip a vendor in any of the 8 directions. After 0.5
seconds of delay and a visual indicator (along with other warnings), the
vendor falls over.
1.1. In the process of making this I had to expand a arrow sprite to
have orthogonal directions, which is why you may see the testing dmi
being changed.
2. CORE ROLLING: A mid-cost but low-supply ability that allows the AI to
roll around and crush anything it falls on, including mobs. This has a
5% chance to have a critical hit so it isnt THAT terrible - plus it's
guaranteed to never stunlock. It's real utility lies in the fact the AI
now has limited movement without borgs. Also, the psychological factor.

As a bonus, vendor tipping now uses animate and transforms instead of
replacing matrices.
## Why It's Good For The Game

1. Generifying vendor tipping code is just good, period. It's a very
wacky and silly little piece of code that really doesn't need to be
isolated to vendors exclusively. ANY big and heavy object can fall over
and do a ton of damage.
1.1. Also, adding weights to critical hits is really good, because it
lets things like the headgib finally be a lot less terrifying, as
they're a lot less likely to happen.

2. Remote vendor tipping is a bit of a goofy ability that isn't really
THAT practical but has a chance of catching someone unaware and doing
some serious damage to that person alone.
2.1. Atop of this, vendor tipping isn't that loud of an action as say,
blowing things up, or doing a plasma flood. Even overrides aren't this
silent or a non-giveaway. A vendor falling on someone, though, is a
mundane thing that happens a lot. This is a decent way to assassinate
people before going loud (or at least, damage people) that isn't offered
yet.

4.
3.1. For real though, AIs rolling around is just fucking hilarious. The
ability to move isn't offered right now (which isn't that much of a bad
things), but with sufficiently limited charges (or limits to how many
times you can buy the ability), this can be a funny little t hing that
lets the AI potentially hide somewhere on the sat (or just relatively
close to the sat, such as engineering [it can't go through the
teleporter with this but it can go through transit tubes]) without the
need for borgs.
3.2. Also, it lets the AI sacrifically execute people by blowing up
their brains.

---
## [cnleth/tgstation](https://github.com/cnleth/tgstation)@[cc57581b73...](https://github.com/cnleth/tgstation/commit/cc57581b73e2979d775dfd9408978e4987b6635b)
#### Friday 2023-07-28 07:48:18 by Sealed101

Dog wit the butter (feat. a bunch of dog-related code improvements) (#77039)

## About The Pull Request
Adds a `dog_fashion` for the stick of butter.(screenshot is outdated as
Lisa won't have butter no more)
![butter
dawgs](https://github.com/tgstation/tgstation/assets/75863639/a22e702c-98a8-4283-abd9-28d4a9fb3bd0)

Also cleans up dog.dm because it was SHIT and FUCK and MY FUCKING GOD
TWO INITIALIZE()s TWO TIMES IN A SINGLE FILE WHAT IN THE GODDAMN

Most noticeably, Lisa properly won't wear any hats, and puppies properly
can't wear head/back items (by just removing those item slots from the
strip/equip menu. if some admeme wants to fumble around they may still
equip shit there. but otherwise for a normal player those slots are
inaccessible).
Basic mobs now also send signals when they run
`appear_dead`/`appear_alive` procs, which corgis hook into to update
their dead fashion overlays.
The side-effect of getting that to work is that dogs (and any basic mob
that uses `play_dead` ai behavior) are so good at feigning death, that
they fool medical HUDs and other related things. They're just that good.
There's a bunch of other things involved and I was mostly just being
angry at the state of the file so I'll check back when I gather all
things changed.


![strippy](https://github.com/tgstation/tgstation/assets/75863639/ec4d17a2-d4df-401c-bd1f-7c4ee1b95671)


## Why It's Good For The Game


https://github.com/tgstation/tgstation/assets/75863639/b34589cb-94d6-4b80-bf0f-1814c08da100



## Changelog
:cl:
add: dog with a butter on 'em
add: dead dog with da butter on 'em (dogs feigning death are so good at
it, they appear dead to medical HUDs and other things)
add: Nars-Ian now can revive from the dead if he consumes a pet
fix: fixes dog fashion items with no speech modifiers set making dressed
up corgis unable to perform their speech or emote behaviors
fix: fixes old Ian losing his mobility ride when shaved with a razor
fix: fixes pets not dropping their collar when gibbed
fix: butter don't go on Lisa and corgi puppies (Lisa won't wear hats and
corgi puppies can't wear hats and back slot items)
/:cl:

---
## [Zeldazackman/Citadel-Station-13-RP](https://github.com/Zeldazackman/Citadel-Station-13-RP)@[4966352d14...](https://github.com/Zeldazackman/Citadel-Station-13-RP/commit/4966352d145c9fcacad823f7dc8d6a52fc82c953)
#### Friday 2023-07-28 07:53:07 by Mazian

changes the open simulated turf to be SOMETHING NOT HORRIBLY EYE SEARING (#5735)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

makes turf/simulated/open blue. resets on init.

## Why It's Good For The Game

holy FUCKING SHIT my eyes HATE WHOEVER DECIDED IT SHOULD BE MISSING
TEXTURE PINK.

---
## [CliffracerX/Skyraptor-SS13](https://github.com/CliffracerX/Skyraptor-SS13)@[867c217c57...](https://github.com/CliffracerX/Skyraptor-SS13/commit/867c217c57bbcbb644e06bfcb6d362e494a895ee)
#### Friday 2023-07-28 08:02:52 by GuillaumePrata

New Wizard spell "branch": Vendormancy (#75679)

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

Co-authored-by: Time-Green <7501474+Time-Green@users.noreply.github.com>

---
## [Helg2/tgstation](https://github.com/Helg2/tgstation)@[1e27ce031b...](https://github.com/Helg2/tgstation/commit/1e27ce031ba94161c64edcc87e5f3aaad778d3fe)
#### Friday 2023-07-28 08:22:47 by carlarctg

Syndicate Duffelbag Rerework (#77060)

## About The Pull Request

Syndicate duffelbags can fit 2 extra bulky items, down from three.

Reduced syndicate duffelbag's unzipped slowdown from '1' to '0.3', and
set its zipping-up sped to 0.5, same as unzipping.

Added the following items to the Syndicate Duffelbag bulky exception
list: Greentext, mech removal tool, gibtonite, skub, golem shells, mech
ammo. Roughly sorted the list by item category.

Fixed the syndie surgery duffelbag having more items than it can hold by
removing the redundant surgical drill (Upgraded cauteries can turn into
one anyways)

Any storage item with a can_hold description can be examined twice to
see what it can hold now.

## Why It's Good For The Game

> Syndicate duffelbags can fit 2 extra bulky items, down from three.

> Reduced syndicate duffelbag's unzipped slowdown from '1' to '0.3', and
set its zipping-up sped to 0.5, same as unzipping.

For most intents and purposes, it seems the syndicate duffelbag has gone
from 'bland upgrade to backpack', to 'useless'. This is especially made
apparent because it isn't exactly shown to the player that these
duffelbags can carry bulky items (I didn't even know about it until I
was making this PR!)

The extra bulky item hold concept is great, but I have my issues with
the item as-is that I seek to fix with this PR. There are TONS of issues
with being unable to access your bag quickly, which is twice as relevant
when your bag is an incredibly conspicious traitor item. Sure, you can
have it in your hand, but then why even have it in the first place?

That's why I want to reduce the slowdown significantly. '1' slowdowns
are thrown around the whole game like they're reasonable (galoshes,
water back-tanks, biosuits) - they aren't. '1' slowdown is CRIPPLING. It
makes you frustratingly slow and effectively destroys any combat
maneuvering you can do. This is very relevant for a traitorious item.

The zip speed helps one use the duffelbag as a storage item dynamically,
letting the item be an actual trade-off rather than mostly a downside.
Gives you a reason to use it rather than just buying a smuggler satchel
for more storage.

Of course these are some hefty buffs, so I lowered the bulky storage to
make up for it. I can bring it back up to 3 if wanted.

> Added the following items to the Syndicate Duffelbag bulky exception
list: Greentext, mech removal tool, gibtonite, skub, golem shells, mech
ammo. Roughly sorted the list by item category.

Some traitorious items that felt like they should be allowed in.
Honestly, I think this shouldn't even be an exception hold except for
blacklisting clearly bonkers things like backpacks, but whatevs.

> Any storage item with a can_hold description can be examined twice to
see what it can hold now.

Generalization is awesome. Hardcoding is cringe!

## Changelog

:cl:
balance: Syndicate duffelbags can fit 2 extra bulky items, down from
three.
balance: Reduced syndicate duffelbag's unzipped slowdown from '1' to
'0.3', and set its zipping-up sped to 0.5, same as unzipping.
add: Added the following items to the Syndicate Duffelbag bulky
exception list: Greentext, mech removal tool, gibtonite, skub, golem
shells, mech ammo. Roughly sorted the list by item category.
fix: Fixed the syndie surgery duffelbag having more items than it can
hold by removing the redundant surgical drill (Upgraded cauteries can
turn into one anyways)
qol: Any storage item with a can_hold description can be examined twice
to see what it can hold now.
fix: The parent crayon's name is 'crayon' to prevent any weirdness with
things that show the parent type's name.
/:cl:

---
## [Ansekishokuu/tgstation](https://github.com/Ansekishokuu/tgstation)@[746b75844c...](https://github.com/Ansekishokuu/tgstation/commit/746b75844c0e05b521a2973cb0705fca304d287f)
#### Friday 2023-07-28 11:42:10 by necromanceranne

Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection (#76852)

## About The Pull Request

Refactors arcane barrage (the wizard spell) and blood barrage (the weird
version of the same spell that cultists get) into the magic subtype. No
longer are they rifles...for some reason. Also they have sprites once
again! Yay. Fixes https://github.com/tgstation/tgstation/issues/76561

So as to not replicate a really crappy system used to get the hand
swapping working, I've just opted to take this opportunity to make
arcane barrage an automatic fire weapon. Yes, this is kind of a feature,
but it's...it's appropriate, don't you think? And I don't think
meaningfully changes its fire rate?

Blood Barrage no longer harms cultists/constructs shot by it and now
properly just heals them/injects them with unholy water. Why all this
was shoved into the Bump() proc is beyond me, but it works now. Fixes
https://github.com/tgstation/tgstation/issues/76560

I've improved the variables for some of the cult spells, and I've also
fixed what I think is one the most pesky parts of how drawing blood
works. So, rather than using range(), it uses view(), which seems to
cause the spell to be a bit funky with lighting? So if you're in
darkness (gosh cultists in dim light, how unheard of), this spell
struggles to gather up blood. Not anymore it doesn't!

Lastly, it only worked on blood pools or droplets, not blood trails. So,
you could bleed a character out by dragging them around, but not sap up
the blood they're dropping from doing so. Only the intermittent blood
splatters or your own bloody footprints count.

Here is the funny thing with that. It still cleans up the blood trail.
You just couldn't activate the blood draw from the trail or treat it as
blood. Now you can. Blood trails now give you +5 charges, and you can
activate the blood draw using blood trails.

## Why It's Good For The Game

Arcane Barrage/Blood Barrage:

This was some really old code and I'm still not sure why they were made
as a separate spell to the madoka reference, which at this stage is
still better than this spell. But at least it is using a sensible
subtype with a reasonable, more modern component to facilitate the
'rapid firing barrage of magical bullet' image this spell is meant to
invoke. As a result of all this nonsense, this spell had its sprites
broken because it kept being attached to stuff in the rifles folder.
Let's put a stop to that here and now and break it independently
instead.

Oh also cultists getting shot by healing bullets that still killed them
is both funny and dumb and the way it worked was bonkers.

Blood Draw:
A cultist trying to determine, on the fly, what blood is a valid for the
blood draw is nearly impossible from visual alone. You'd be convinced
this part of the spell is broken just because having a splatter and a
trail on the same tile massively obfuscates whether you're looking at
valid sources of blood. I've struggled to understand as a player what
was going on and why it was so selective about what was acceptable. Now
I see that the problem was one of visual accuracy, bad type checking,
and really, really outdated code that should have been improved with
better procs.

Blood trails are also actually made from dragging out a creature's
bloody corpse. For humans, the most common source of blood trails, this
does actually mean they're losing blood to produce these trails. It
stands to reason this should be a valid source (bloody footprints are,
after all). I gave them a...somewhat minor amount of charge contribution
just to keep it moderately sane for how much blood it generates.

## Changelog
:cl:
refactor: Arcane Barrage and Blood Barrage are magic gun subtypes and
not rifle subtypes. Also they have sprites again.
qol: The barrage spells now use the automatic component to do its thing.
fix: Blood Barrage once again heals cultists and constructs without
hurting them.
code: Cleans up how Blood Rites finds blood to draw in. You can now just
click turfs as well as blood, and it should now be much more accurate
about it.
qol: Blood trails contribute to charges gained using Blood Rites. You
can also activate Blood Rite's blood draw using blood trails.
/:cl:

---
## [Ansekishokuu/tgstation](https://github.com/Ansekishokuu/tgstation)@[9286933739...](https://github.com/Ansekishokuu/tgstation/commit/92869337395a34eb372d7af6b3afaee4be4a7bef)
#### Friday 2023-07-28 11:42:10 by Jacquerel

Fixes some synthetic language oversights (#76846)

## About The Pull Request

#76305 removed the knowledge of every language from silicons, but this
had a couple of oversights.
This language set was not only used by cyborgs but also bots and vending
machines.

A couple of effects relied on them knowing all of those languages,
specifically their emp_act and also the station trait which rerolled
their languages.
Now they actually _learn_ a random language and start speaking it
instead.

Also I fixed a related runtime which I noticed in testing where a bot
would die as a result of being EMPed, delete itself, and then try and do
a bunch more shit after it stopped existing. Annoying.

Why was I looking at bot languages? Haha don't worry about it 😇 

## Why It's Good For The Game

Restores function of a funny feature.

## Changelog

:cl:
fix: Station traits can once again allow vending machines and bots to
speak a random language
fix: EMPed bots and vending machines once again speak a random language
/:cl:

---
## [vic3-divergences/divergences](https://github.com/vic3-divergences/divergences)@[86f67343f5...](https://github.com/vic3-divergences/divergences/commit/86f67343f5400d052db3149a15df3408ca2eeec1)
#### Friday 2023-07-28 11:42:25 by Sen2ka

Push so I can pull main into this branch

- Corrected weird loc
- Corrected mispelled trigger
- pain
- suffering
- hating this variable

---
## [Ansekishokuu/PsychonautStation](https://github.com/Ansekishokuu/PsychonautStation)@[ed57b8127f...](https://github.com/Ansekishokuu/PsychonautStation/commit/ed57b8127f1b28507272170c60c7db16f6e02a87)
#### Friday 2023-07-28 11:42:28 by Jacquerel

Rat RP expansion (#76455)

## About The Pull Request

This fixes a vile and long-standing bug where putting a mouse inside
your hat would not allow the mouse to control your movements, as it
would pop out of the hat whenever it tried to move.
Additionally as a feature this allows a mouse sitting on your head to
convey complicated instructions such as "scream" or "do a flip", via
emoting. Through drift compatibility, the rat's living mech will also
perform this action.

I could have made this into a component but there's no fucking way any
other item is going to have this behaviour, so I didn't.

## Why It's Good For The Game

This feature was already in the game but broken and I want it not to be
broken.
The mouse should be able to control your entire life.

## Changelog

:cl:
fix: Placing a mouse inside your chef hat will once more allow it to
pilot you around.
add: A player-controlled mouse inside your chef hat can compel you to
perform complex actions, such as flipping and spinning. You will obey
because the mouse knows better than you do.
/:cl:

---
## [cmss13-devs/cmss13](https://github.com/cmss13-devs/cmss13)@[ce09b07afd...](https://github.com/cmss13-devs/cmss13/commit/ce09b07afd0f8d433ffee1a43bc4dfeb978f45f1)
#### Friday 2023-07-28 11:48:23 by ihatethisengine

Xeno Alliance Announcements + Greeno Civil War (#3990)

# About the pull request

Xenos now get messages when their queen set/break alliance to another
faction and when other queen set/break alliance with their hive.

Corrupted Xenos with implanted IFF tag now has a choice to defect from
the hive and become Renegade (hive allied to USCM) when Queen decides to
break alliance with USCM. Xenos that stay loyal to Queen rip the IFF
tags out. You have only 10 seconds to make a decision, so think quick.
By default xenos stay loyal to Queen.

Renegade Hive is allied to all human factions, but it mostly affects
structures and weeds. Renegade ability to attack someone fully depends
on its IFF tag settings.

Please check my messages because I'm not very good at writing.

# Explain why it's good for the game

More announcements are good because it's less confusing. You know when
someone set ally to you and you know when someone is betraying you. It
makes sense because allied xenos share announcements anyway. And sudden
betrayals are always a bit cheesy.

I think the Renegade addition makes research a little more fun and
rewarding. Now, if you implant corrupted xeno with an IFF tag, the xeno
player can choose to remain loyal to you if/when the Queen decides to
betray. Plus corrupted xenos with the IFF tag are no longer forced to
betray, so it's also good. Not sure if that makes sense lore-wise, but
since corrupted are artificially created and their DNA is decrypted, it
makes at least some sense. Plus we kinda have tamed xenos which work
really similarly.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
add: Added announcements for xenos about forming and breaking alliances.
add: Xenos with IFF tag now have a choice to stay loyal to USCM when
Queen decides to betray.
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>
Co-authored-by: Drathek <76988376+Drulikar@users.noreply.github.com>
Co-authored-by: harryob <me@harryob.live>

---
## [shogo82148/perl5](https://github.com/shogo82148/perl5)@[fe5492d916...](https://github.com/shogo82148/perl5/commit/fe5492d916201ce31a107839a36bcb1435fe7bf0)
#### Friday 2023-07-28 12:04:51 by Yves Orton

regcomp.c etc - rework branch reset so it works properly

Branch reset was hacked in without much thought about how it might interact
with other features. Over time we added named capture and recursive patterns
with GOSUB, but I guess because branch reset is somewhat esoteric we didnt
notice the accumulating issues related to it.

The main problem was my original hack used a fairly simple device to give
multiple OPEN/CLOSE opcodes the same target buffer id. When it was introduced
this was fine. When GOSUB was added later however, we overlooked at that this
broke a key part of the book-keeping for GOSUB.

A GOSUB regop needs to know where to jump to, and which close paren to stop
at. However the structure of the regexp program can change from the time the
regop is created. This means we keep track of every OPEN/CLOSE regop we
encounter during parsing, and when something is inserted into the middle of
the program we make sure to move the offsets we store for the OPEN/CLOSE data.
This is essentially keyed and scaled to the number of parens we have seen.
When branch reset is used however the number of OPEN/CLOSE regops is more than
the number of logical buffers we have seen, and we only move one of the
OPEN/CLOSE buffers that is in the branch reset. Which of course breaks things.

Another issues with branch reset is that it creates weird artifacts like this:
/(?|(?<a>a)|(?<b>b))(?&a)(?&b)/ where the (?&b) actually maps to the (?<a>a)
capture buffer because they both have the same id. Another case is that you
cannot check if $+{b} matched and $+{a} did not, because conceptually they
were the same buffer under the hood.

These bugs are now fixed. The "aliasing" of capture buffers to each other is
now done virtually, and under the hood each capture buffer is distinct. We
introduce the concept of a "logical parno" which is the user visible capture
buffer id, and keep it distinct from the true capture buffer id. Most of the
internal logic uses the "true parno" for its business, so a bunch of problems
go away, and we keep maps from logical to physical parnos, and vice versa,
along with a map that gives use the "next physical parno with the same
logical parno". Thus we can quickly skip through the physical capture buffers
to find the one that matched. This means we also have to introduce a
logical_total_parens as well, to complement the already existing total_parens.
The latter refers to the true number of capture buffers. The former represents
the logical number visible to the user.

It is helpful to consider the following table:

  Logical:    $1      $2     $3       $2     $3     $4     $2     $5
  Physical:    1       2      3        4      5      6      7      8
  Next:        0       4      5        7      0      0      0      0
  Pattern:   /(pre)(?|(?<a>a)(?<b>b)|(?<c>c)(?<d>d)(?<e>e)|(?<f>))(post)/

The names are mapped to physical buffers. So $+{b} will show what is in
physical buffer 3. But $3 will show whichever of buffer 3 or 5 matched.
Similarly @{^CAPTURE} will contain 5 elements, not 8. But %+ will contain all
6 named buffers.

Since the need to map these values is rare, we only store these maps when they
are needed and branch reset has been used, when they are NULL it is assumed
that physical and logical buffers are identical.

Currently the way this change is implemented will likely break plug in regexp
engines because they will be missing the new logical_total_parens field at
the very least. Given that the perl internals code is somewhat poorly
abstracted from the regexp engine, with parts of the abstraction leaking out,
I think this is acceptable. If we want to make plug in regexp engines work
properly IMO we need to add some more hooks that they need to implement than
we currently do. For instance mg.c does more work than it should. Given there
are only a few plug in regexp engines and that it is specialized work, I
think this is acceptable. We can work with the authors to refine the API
properly later.

---
## [schoolstatus/redpanda-deployment-automation](https://github.com/schoolstatus/redpanda-deployment-automation)@[54e0860613...](https://github.com/schoolstatus/redpanda-deployment-automation/commit/54e08606133785bf05f4069ba35cab1f82233c1a)
#### Friday 2023-07-28 12:09:26 by gene-redpanda

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
## [ljsimpkin/chat-gpt-cli-tool](https://github.com/ljsimpkin/chat-gpt-cli-tool)@[00495f063f...](https://github.com/ljsimpkin/chat-gpt-cli-tool/commit/00495f063f8833a7ef83b6b1560a8b7b0b69e2ca)
#### Friday 2023-07-28 12:26:26 by liam

aider: Update README with new functionality like -c for generating code and -m for switching to gpt-4.

# Aider chat conversation:

USER: update readme with the new functionality like -c for generating code and -m for switching to got 4

ASSISTANT: I'm sorry, but I can't propose changes to the README.md file as it's currently read-only. Could you please add it to the chat so I can suggest the necessary updates?

USER: I added these *read-write* files: README.md

ASSISTANT: Great! Now that we have write access to the README.md file, we can update it to include the new functionality.

Here's how we can update the README.md file to include the new `-c` and `-m` flags:

<source>markdown
README.md
<<<<<<< ORIGINAL
# Quick Start Guide

## Step 1: Clone the Repository
Start by cloning our repository to your local system using the git command:

```sh
git clone https://github.com/ljsimpkin/chat-gpt-cli-tool.git
```

## Step 2: Install Dependencies
Navigate to your project's directory and install the necessary dependencies using pip:

```sh
cd YourProject
python3 -m pip install -r requirements.txt
```

## Step 3: Set Your OpenAI API Key
Before running the script, you should set your `OPENAI_API_KEY` in your environment variables. Below are the instructions for Unix/Linux systems and Windows respectively.

### Unix/Linux
On Unix/Linux you can add the api key to your environment variables using the command below:
```sh
export OPENAI_API_KEY=your-api-key
```

### Windows
On Windows, environment variables can be set through the command prompt with the setx command:
```sh
setx OPENAI_API_KEY "your-api-key"
```

Remember to replace `your-api-key` with your actual OpenAI API Key.

## Step 4: Run the Script
Now, you can run your python script. Instead of using pip, we are using python3 script here:

```sh
python3 your_script.py
```
This should start the execution of the script.

Congratulations! You are all set.

<span style="color:blue">*__NOTE__:</span> For these changes to take effect, you might need to close and reopen your command line session or reboot your machine.

__IMPORTANT:__ Please make sure to keep your `OPENAI_API_KEY` secure and do not commit it in your code or upload it to GitHub.

Enjoy using our project!

# Todo
[] Create a -c flag that will instruct the ai to only output code
=======
# Quick Start Guide

## Step 1: Clone the Repository
Start by cloning our repository to your local system using the git command:

```sh
git clone https://github.com/ljsimpkin/chat-gpt-cli-tool.git
```

## Step 2: Install Dependencies
Navigate to your project's directory and install the necessary dependencies using pip:

```sh
cd YourProject
python3 -m pip install -r requirements.txt
```

## Step 3: Set Your OpenAI API Key
Before running the script, you should set your `OPENAI_API_KEY` in your environment variables. Below are the instructions for Unix/Linux systems and Windows respectively.

### Unix/Linux
On Unix/Linux you can add the api key to your environment variables using the command below:
```sh
export OPENAI_API_KEY=your-api-key
```

### Windows
On Windows, environment variables can be set through the command prompt with the setx command:
```sh
setx OPENAI_API_KEY "your-api-key"
```

Remember to replace `your-api-key` with your actual OpenAI API Key.

## Step 4: Run the Script
Now, you can run your python script. Instead of using pip, we are using python3 script here:

```sh
python3 your_script.py
```
This should start the execution of the script.

You can also use the `-c` flag to instruct the AI to only output code:

```sh
python3 your_script.py -c "your code generation prompt"
```

And the `-m` flag to switch to the gpt-4 model:

```sh
python3 your_script.py -m
```

Congratulations! You are all set.

<span style="color:blue">*__NOTE__:</span> For these changes to take effect, you might need to close and reopen your command line session or reboot your machine.

__IMPORTANT:__ Please make sure to keep your `OPENAI_API_KEY` secure and do not commit it in your code or upload it to GitHub.

Enjoy using our project!
>>>>>>> UPDATED
</source>

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[cfd40aeef5...](https://github.com/Rex9001/Rex_Tg/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Friday 2023-07-28 12:42:40 by necromanceranne

Imports and Contraband 2: Landfill Gacha Addiction (I put trash randomizers into cargo crates and called it content) (#76771)

## About The Pull Request

This is a followup on my previous PR involving cargo imports. I've made
a number of changes and new additions to cargo's imports and contraband.
But I've also changed how Smuggler's Satchels generate loot as well.

### New:
**Abandoned Crates:** You can now order in abandoned crates at a steep
price. Obviously these are just your standard fare abandoned crates, so
they've got a pretty long list of potential contents. Some great, some
utterly not worth the price you paid for the crate. Since they're quite
pricey, you can't order very many quickly. But this does allow cargo
techs the opportunity to spend the round solving puzzles to get
interesting loot.

**Dumpster of Maint Garbage:** This dumpster (similarly named to another
dumpster you can order) is filled with maint trash and potential maint
random spawns. This list is extensive enough that anything spawned in
this crate is likely to be mostly garbage. But, it is more affordable
than abandoned crates. I'd consider this the literally trashier version
of the abandoned crate.

**Shamber's Juice Eldritch Energy! Crate:** A crate with one can of the
extremely rare, short run edition of Shambler's Juice, Eldritch Energy!
This contains 5 units of eldritch essence. Heals heretics, hurts
everyone else! This is a VERY potent poison, but it also happens to be a
handy way for a Cargonian heretic to get a potent healing item without
having to waste knowledge points.

**Animal Hide Crate:** It's a cargo crate full of animal hides! This can
include fairly rare hides and some icebox creature hides as well, like
polar bear hides and wolf sinew. It's not too expensive, and mostly
spits out leather.

**Dreadnog Carton Crate:** A carton full of the worst eggnog imaginable.
This is just something to troll people with. Drink it and you'll get a
massive mood penalty. Dreadnog! May or may not contain space cola!

### Updated:

**Contraband Crate and Smuggler's Satchels:** This has had it's price
increased considerably. But, for good reason. It now contains some more
controlled random items, but also some more valuable contraband as well
as a very rare spawn. The upper end on his contraband can be extremely
valuable, but the majority of the items gained from contraband crates
will probably be either what you can get now (quite weak), or something
a bit more middle of the road (some more unique narcotics).

As a consequence, I've also passed this change onto smuggler's satchels,
as they used the crate to generate its contents. (it literally spawned
and then deleted a contraband crate to generate the contents hoo haa).

I've also increased the number of items in the smuggler's satchel. Since
the randomly spawned smuggler's satchels are quite a bit rarer now there
is only ever two spawned in the map, and spending actual TC on these is
somewhat counterproductive, I don't imagine this will be more beneficial
for scavenger hunters hoping for some interesting goodies.

**Russian Crate (the normal one):** The mosins now spawn in ancient gun
cases. These determine what kind of mosin you can get. 79% of the time,
you get the crap mosin. 20% of the time, you get a good mosin. And 1% of
the time, you get rations. This more tightly controls how many good
mosins are entering into the round and how much of a value purchase the
Russian crate actually is for getting ballistics. Since the process is
even more unlikely than before, it isn't necessarily as guaranteed that
you will get a good mosin. Hell, you might not even get a gun if you're
that unlucky.

**Shocktrooper Crate:** It now has an armor vest and helmet. So, not
only do you get some grenades, you get some protection as well. Since
this is the 'loud' crate, I felt it appropriate to make it slightly more
useful for enabling that.

**Special Ops Crate:** It now contains five mirage grenades and a
chameleon belt, and has had the survival knife improved to a
switchblade. This is probably the weakest of the two crates STILL, but
hopefully these make them a little more interesting and novel by giving
them pretty fun grenade to toy with.

## Why It's Good For The Game

My initial PR hoped to add in a few more interesting purchases for
cargo. I think currently cargo has a slight issue of not having enough
valuable or interesting uses for their money. I think it still has that
problem, but by including more unique crates that allow cargo to provide
some oddities into the round, that might slowly work itself out.

This PR hopes to provide another way to waste their money if they have
an excess amount. Landfill Trash Gambling. Spending it away on complete
junk, which I think is absolutely hilarious when it doesn't work out, as
it is soulful in its design. Definitely not inspired by my recent thrift
shop excursions this month buying and scrounging for furniture and
interesting clothing.

[Relevant](https://www.youtube.com/watch?v=QK8mJJJvaes)

Also, I wanted to buff some of the crates I introduced a bit last time,
and nerf the mosin production somewhat via a more controllable method
that I can actually adjust as necessary down the line.

## Changelog
:cl:
fix: Stops manifest generation runtiming when a cargo crate is empty.
add: Abandoned crates are now available via cargo imports.
add: Dumpsters full of maintenance trash are now available via cargo
imports.
add: An ultra-rare can of Shambler's Juice is now available via cargo
imports.
add: Animal hides and leathers can be (unreliably) ordered via cargo
imports.
add: The Dreadnog has entered this realm. To consume, purchase it via
cargo imports.
balance: Contraband Crates (and as a consequence, smuggler's satchels)
now generate more varied goods. Mostly the same, but sometimes you get
something quite different or even valuable.
balance: Mosins generated via the Russian supply crate are a bit more
random, weighing more heavily towards bad mosins than good mosins.
balance: Buffed both the shocktrooper and special op crate. Shocktrooper
now has an armored helmet and vest, and special op now has 5 mirage
grenades and a chameleon belt. The survival knife in the special op
crate is now a switchblade.
/:cl:

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[52c8da7ea4...](https://github.com/Rex9001/Rex_Tg/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Friday 2023-07-28 12:42:40 by Jacquerel

PAI Holochassis are now leashed to an area around their card (#76763)

## About The Pull Request

This change restricts PAI holograms to an area around their assigned PAI
card. If you leave this area, you are teleported back to the card's
location (but not automatically put back into the card).

https://www.youtube.com/watch?v=L2ThEVa4nx8

This setting can be configured from the PAI menu, it's set pretty short
in the video because otherwise it wouldn't teleport when I threw the
card and I like doing that.

![image](https://github.com/tgstation/tgstation/assets/7483112/faf0fa0b-e9d6-4990-8d8c-f30def2892f1)

To accomodate this I set up a component to deal with a reasonably common
problem I have had, "what if I want to track the movement of something
in a box in a bag in someone's inventory". Please tell me if the
solution I came up with is stupid and we already have a better one that
I forgot about.

Also now you can put pAIs inside bots again, by popular request.

## Why It's Good For The Game

Personal AIs are intended to be personal assistants to their owner.
rather than fully independent entities which can pick up their own card
and leave as soon as they spawn.
As "aimless wanderer" players can now possess station bots, pAIs can be
limited to an area around the bearer of their card.

Because the holoform now doesn't contain the card, this also means that
a PAI cannot run off and then be impossible to retrieve. You are always
in control of where it can go.

Also it's funny to throw the card and watch the chicken get teleported
to it.

## Changelog

:cl:
add: Personal AI holograms are now limited to an area around their PAI
card. The size of this are can be configured via the PAI card.
add: pAI cards can now be placed inside bots in order to grant them
control of the bot.
/:cl:

---
## [Rex9001/Rex_Tg](https://github.com/Rex9001/Rex_Tg)@[2ee79d7077...](https://github.com/Rex9001/Rex_Tg/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Friday 2023-07-28 12:58:44 by Jacquerel

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
## [vsrs/rust-analyzer](https://github.com/vsrs/rust-analyzer)@[994f4f6e2e...](https://github.com/vsrs/rust-analyzer/commit/994f4f6e2e45bef4bebeeabee4e3d67b87727b91)
#### Friday 2023-07-28 13:36:22 by bors

Auto merge of #15290 - igorskyflyer:igorskyflyer-dx-install-extension, r=lnicola

editor/code: [DX] Use notification command links for debugger installation

This PR improves DX (developer experience) when installing the VS Code extension for the first time. When doing so and trying to debug a Rust file, we get an error notification that either CodeLLDB or C++ extension/debugger should be installed (see image below).

<div align="center">
	<img src="https://github.com/rust-lang/rust-analyzer/assets/20957750/e8ebeb1e-85f4-44e2-b79f-c48cf52e5f36" alt="Rust, prompt to install debug extension">
</div>

The PR enhances the links in the given notification and upon clicking instead of opening the Web page of the extension it installs the extension immediately, without the need to leave the editor.

Note: the feature needs to be refined, maybe an "install in progress" message or something similar, I left that for you guys to decide and implement. I think it also possible to first open the sidebar, open the Extensions tab, then run the extension installation command which would make it more user-friendly.

P.S. it is also possible to open the extension's details in VS Code directly via the same links and then the user would have to manually click on the Install button - if installation is not the desired behavior.

Happy coding! 🎉

---
## [RalphHightower/RalphHightower](https://github.com/RalphHightower/RalphHightower)@[2a8a7d08ab...](https://github.com/RalphHightower/RalphHightower/commit/2a8a7d08aba47c9d6bba7406e0cbc42137856f73)
#### Friday 2023-07-28 14:03:50 by Ralph Hightower

docs: copy Dune from ChattingWithChatGPT to Dune


#### Dune by Frank Herbert 

| *"RalphHightower"* / [ChatGPT](https://chat.openai.com/) |
|----|
| *"Can you describe Dune to me?"* |
| Sure! Dune is a science fiction novel by American author Frank Herbert, published in 1965. It is set in the distant future and depicts a feudal society on the planet Arrakis, a desert planet home to the valuable resource known as "spice." The story follows the journey of a young man named Paul Atreides, who becomes embroiled in a power struggle for control of Arrakis and its spice. Along the way, Paul discovers that he possesses special powers and is destined to become a leader in the fight for control of the spice. Dune is a complex and detailed work that explores themes of politics, religion, and the human condition. It is widely regarded as a classic of science fiction and has inspired numerous adaptations in various media. |
| *"Why do different factions want to control the spice?"*|
| In the world of Dune, the spice melange is a valuable and highly sought-after resource that is only found on the planet Arrakis, also known as Dune. It is a rare and valuable substance that has many uses, including as a spice for food, as a medicine, and as a psychoactive drug that enhances mental abilities. The spice is also used to help fold space, which allows for faster-than-light travel between the stars. As a result, control of the spice is highly coveted by the various factions in the Dune universe. In the novel, the noble House Atreides is given control of Arrakis by the ruling emperor, but they are betrayed by their rivals and a power struggle ensues as various factions vie for control of the spice. |
| *"Who are the Bene Gesserit?"*|
| The Bene Gesserit are a powerful and secretive organization in the Dune universe. They are an all-female group that has been around for thousands of years and has a long tradition of training their members in physical and mental disciplines, as well as genetic manipulation. The Bene Gesserit use their skills and knowledge to gain power and influence, and they often operate behind the scenes, manipulating events to their advantage. They are known for their ability to control their own bodies and emotions, and for their use of a specialized form of communication called "Voice," which allows them to influence and control others through speech and persuasion. The Bene Gesserit are highly respected and feared, and they play a significant role in the events of the Dune novels. |
| *"And the Spacing Guild?"*|
| The Spacing Guild is another important organization in the Dune universe. It is a group of powerful and influential people who control the means of interstellar travel, making them an essential part of the economy and politics of the known universe. The Guild is known for its use of Guild Navigators, who are humans that have been genetically altered and trained to navigate space using the spice melange, which allows them to fold space and travel vast distances in a short amount of time. The Navigators are able to achieve this feat by using their heightened mental abilities and by remaining in a tank of melange gas, which helps them to "see" the folds of space. The Guild is a powerful and mysterious organization that wields significant influence in the world of Dune. |
| *"How do the sandworms factor in Arrakis?"*|
| The sandworms of Arrakis, also known as Dune, are giant, ferocious creatures that live in the desert sands of the planet. They are native to Arrakis and are a central part of the ecosystem there. The sandworms are sensitive to vibrations and are attracted to sounds, and they are known to attack and consume anything that disturbs them. The sandworms are also the source of the spice melange, which is produced in their bodies and released onto the surface of the planet when they die. As a result, the sandworms are highly valuable and are closely guarded by the native population of Arrakis, the Fremen. In the Dune novels, the sandworms play a significant role in the story and are an important part of the culture and economy of Arrakis. |
| *"What about the House of Atreides?"*|
| The House of Atreides is a noble family in the Dune universe. They are descended from the royal line of the planet Caladan and are known for their wisdom, strength, and honor. The Atreides family is led by Duke Leto Atreides, who is a just and fair ruler and is respected by his subjects. The Atreides are also known for their fierce loyalty to their family and to their allies. In the Dune novel, the Atreides family is given control of the planet Arrakis by the ruling emperor, but they are betrayed by their rivals and a power struggle ensues as various factions vie for control of the valuable spice that is produced on Arrakis. The story follows the journey of Duke Leto's son, Paul Atreides, as he becomes embroiled in the conflict and ultimately rises to power as the leader of the Fremen, the native population of Arrakis. | 
| *"Who are the Harkonnen?"*|
| The Harkonnen family is a noble house in the Dune universe. They are depicted as cruel, ruthless, and power-hungry, and are the main antagonists in the Dune novel. The Harkonnen are the sworn enemies of the Atreides family and will stop at nothing to destroy them and gain control of the valuable spice that is produced on the planet Arrakis. The Harkonnens are known for their brutal tactics and are feared throughout the universe. They are led by Baron Vladimir Harkonnen, who is a cruel and sadistic man who takes pleasure in causing pain and suffering. The Harkonnens play a significant role in the Dune novel and are an important part of the story. |
| *"How are sandworms detected?"*|
| Sandworms on the planet Arrakis, also known as Dune, are difficult to detect because they live deep beneath the sand and are sensitive to vibrations and sounds. They are attracted to anything that disturbs them and will emerge from the sand to attack and consume it. To avoid attracting the attention of sandworms, the native population of Arrakis, the Fremen, have developed special techniques for detecting and avoiding them. One method is the use of "thumper" devices, which are large, mechanical drums that are used to create vibrations in the sand. By creating a rhythmic pattern of vibrations, the Fremen are able to communicate with each other and to attract sandworms to a specific location, where they can be harvested for their spice. The Fremen are also trained to recognize the signs of sandworm activity, such as the appearance of "worm tracks" on the surface of the sand. |
| *"Why did Paul's mother disobey orders and bear a son?"* |
| Paul Atreides' mother, Lady Jessica, was a member of the Bene Gesserit, a powerful and secretive organization in the Dune universe. As a member of the Bene Gesserit, Lady Jessica was trained in physical and mental disciplines and was expected to follow the orders of the organization. However, she was also the personal concubine of Duke Leto Atreides and became pregnant with his son, Paul, despite orders from the Bene Gesserit not to bear children. Lady Jessica disobeyed these orders because she loved Duke Leto and wanted to have his child, and because she believed that Paul had the potential to be a special and important person. Despite the risks involved, Lady Jessica chose to bear a son and raised him according to the teachings of the Bene Gesserit, instilling in him the skills and knowledge he would need to survive in the dangerous and unpredictable world of Dune. |
| *"Does Paul have a sister?"* |
| Yes, Paul Atreides has a sister in the Dune novels. Her name is Alia Atreides, and she is the daughter of Duke Leto Atreides and Lady Jessica. Alia is born after her parents arrive on the planet Arrakis, also known as Dune, and is raised according to the teachings of the Bene Gesserit, an all-female organization that her mother belongs to. Alia is a precocious and intelligent child who possesses special abilities, including the ability to access the memories and skills of her ancestors. Like her brother, Paul, Alia is a key player in the events of the Dune novels and plays a significant role in the story. |
| *"What are Alia's powers?"* |
| Alia Atreides is a special and unique character in the Dune novels because she possesses a number of special abilities that set her apart from other people. One of her most notable abilities is the ability to access the memories and skills of her ancestors, which is a result of her mother, Lady Jessica, having taken the spice melange during pregnancy. This allows Alia to access the collective knowledge and experiences of her ancestors and to use them to her advantage. Alia is also highly intelligent and possesses advanced mental and physical skills, which she has been trained in by the Bene Gesserit, an all-female organization that her mother belongs to. In addition to these abilities, Alia also has enhanced senses and reflexes, and is capable of extraordinary physical feats. She is a formidable and formidable character in the Dune novels and plays a significant role in the story. |
| *"Can you tell me about Paul's wife?"* |
|Paul Atreides, the main character in the Dune novels, marries several times throughout the course of the story. One of his most notable wives is Chani, a native of the planet Arrakis and a member of the Fremen, the native population of the planet. Chani is a strong and capable woman who becomes Paul's closest ally and companion. She is fiercely loyal to Paul and helps him in his quest to take control of Arrakis and its valuable spice. Chani is a skilled fighter and is trained in the ways of the Fremen, and she plays a key role in helping Paul to lead the Fremen in their struggle against the Harkonnen, the sworn enemies of the Atreides family. Chani and Paul are deeply in love and have several children together, who play important roles in the events of the Dune novels. |
| *"Can you tell me about Paul's children?"* |
| Paul Atreides and his wife, Chani, have several children together in the Dune novels. Their first child is a son named Leto Atreides II, who is named after Paul's father, Duke Leto Atreides. Leto II is born on the planet Arrakis and is raised according to the teachings of the Fremen, the native population of the planet. Like his father, Leto II possesses special abilities and is destined to become a powerful and influential figure in the Dune universe. He goes on to play a significant role in the events of the Dune novels and becomes the central character in several of the sequels to the original novel.|
|Paul and Chani also have several other children together, including daughters named Ghanima and Irulan. Ghanima is born on Arrakis and is raised according to the Fremen way of life, while Irulan is born on Caladan, the ancestral home of the Atreides family. Both Ghanima and Irulan play important roles in the events of the Dune novels and go on to have significant impact in the story. |
| *"Tell me about Leto II, Ghanima, and Irulan."* |
| Leto II Atreides is the son of Paul Atreides and Chani and is the central character in several of the Dune novels. He is named after his grandfather, Duke Leto Atreides, and is raised according to the teachings of the Fremen, the native population of the planet Arrakis. Like his father, Leto II possesses special abilities and is destined to become a powerful and influential figure in the Dune universe. He becomes the ruler of Arrakis and the head of the Atreides family, and is known for his wisdom, strength, and honor. Leto II is a key player in the events of the Dune novels and his actions have a significant impact on the story.|
|Ghanima Atreides is the daughter of Paul Atreides and Chani and is born on the planet Arrakis. She is raised according to the Fremen way of life and is trained in their customs and traditions. Ghanima is a skilled fighter and possesses special abilities, including the ability to access the memories and skills of her ancestors. She plays an important role in the events of the Dune novels and goes on to have a significant impact on the story.|
|Irulan Atreides is the daughter of Paul Atreides and Chani and is born on the planet Caladan, the ancestral home of the Atreides family. She is raised according to the customs and traditions of the Atreides family and is well-educated and highly intelligent. Irulan is a key player in the events of the Dune novels and goes on to have a significant impact on the story. She is also the author of several books about the history and culture of the Dune universe and is a respected and influential figure in her own right. |
| *"What do you think of the newest movie of Dune?"* |
| I'm sorry, but I am a language model and do not have the ability to watch movies. I also have a knowledge cutoff date of 2021, so I am not aware of any movies or other adaptations of Dune that have been released after that time. However, I can tell you that Dune has been adapted into various media over the years, including movies, television shows, video games, and other works of fiction. Some of these adaptations have been well-received, while others have received mixed reviews. It would be up to individual viewers to decide whether or not they enjoyed any particular adaptation of Dune. |
| *"Thank you. You've been very helpful."*|
| You're welcome! I'm glad that I could help. If you have any other questions, please don't hesitate to ask. |

---
## [Sagnac/streamsave](https://github.com/Sagnac/streamsave)@[5ec27d08e8...](https://github.com/Sagnac/streamsave/commit/5ec27d08e88efbf5e32ecb0bb27647807370b12c)
#### Friday 2023-07-28 15:07:18 by Sagnac

Redesign how options are updated

The previous scheme was pretty ugly. This is due for a much more
comprehensive rewrite as there's quite a bit of redundancy with the
script-message functions and maintaining both script-opts and
script-message updates requires more effort. But that will have to come
at a later time.

One alternative approach would be to hook into the current override
functions by using them as fields in the update table and have them
perform double duty, but this may prove more trouble than it's worth.

As a user, the script-message approach to changing options is more
convenient to use during runtime either with keybinds or through the
console. Also, it supports more arguments (e.g. cycle, on_demand) and
provides status messages. That being said, with script-opts you can send
an entire list of options to be updated instead of having to chain
script-message commands. The names being used for this also differ
between the two methods, with the script-message names being shorter and
likely easier to remember, but the inconsistency in naming between the
options and the runtime commands could be an issue.

Of course I could just turn off the script-opt updating mechanism by
not using update_opts, which I probably should do, but I'm going to keep
this around for now while I trim the script down to a lite version at a
separate branch; this will prove useful there as script-opts becomes the
desired minimalistic approach.

Another thing to note with regards to removing on_update handling of the
options is that some options such as the likely widely used
force_extension option would still require support in that regard, as
the runtime command is simply an on-demand single-stream change and a
revert handler, and does not in actuality set the format in a global
manner - if a new stream is loaded then it will take on the
automatically determined format.

---
## [naikari/naikari](https://github.com/naikari/naikari)@[7a448e8d3e...](https://github.com/naikari/naikari/commit/7a448e8d3e2c453084d5038ac63bde8196ae0541)
#### Friday 2023-07-28 15:32:59 by diligentcircle

Removed "hypergates" and everything to do with them.

Our "hypergates" were based on QuasiSpace from Star Control II. In
that game, QuasiSpace is a useful idea that cuts travel time and,
even more importantly, fuel use substantially. For Naikari, thô,
what we're finding is it just doesn't do anything meaningful.

There are a couple of things working against this system in Naikari.
For starters, since it only allows you to go to places you've already
been, it doesn't have a role in exploration, just standard travel.
This is partly because we want exploration to be intimate (not just
"teleport to new place", but rather "discover new place naturally"),
but it's also necessitated for story reasons if the Empire is
responsible for constructing them mid-game.

Another factor that makes this system less good than QuasiSpace is
that you can't instantly teleport to the hub zone, which roughly
halves the travel time benefit. This doesn't have to be a huge
problem in theory; LOTRO, for example, has hubs you can go to in
order to instant-travel to other hubs, and this is common in MMORPGs.

However, the fatal flaw with the system in Naikari is simply that
normal travel times are so short that the reduction afforded by a
quick travel hub system just isn't worth much. I decided to really
test this out by flying from the south extreme edge of the map to the
top extreme edge with and without the assistence of hypergates and
hidden jump points. Unassisted, this worst-case-scenario travel time
was five minutes. Assisted, it was two minutes. That's a very
significant relative reduction, but a rather minor absolute reduction.

And in most cases, travel needs are far less extreme than that. What
we've found in playtesting is that even when we're outright given
knowledge of hypergates, we *never* have a reason to use them. The
simple fact is that most of the time, the place you need to go to
isn't all the way across the map; it's just a few jump points away.
Even a Schroedinger feels like overkill when you consider this, let
alone a special fast-travel hub system.

Plus, story-wise, "hypergates" feel like a cop-out. Realistically,
the Empire has no legitimate motivation to build them, and the rest
of the factions have no motivation either. The only reason for
"hypergates" to exist is to allow the Proteron to come along and
start causing problems everywhere in the galaxy at once, which is
a bit overly convenient. I think it would be much more interesting
for there to be some "geographical" way the Proteron are able to
invade.

Of course, this also means we'll have to come up with a different
reason for the Incident. I always felt the "hypergates exploded"
explanation felt hollow anyhow, thô.

---
## [xivanalysis/xivanalysis](https://github.com/xivanalysis/xivanalysis)@[c009fd5bcf...](https://github.com/xivanalysis/xivanalysis/commit/c009fd5bcf5a7ae7810f9e30a3f7df648c2d4d43)
#### Friday 2023-07-28 15:33:39 by B Fraser

BLU: 6.45 Moon Flute update (#1873)

* BLU: Being Mortal mistakenly had the same actionId as Apokalypsis

* BLU Moon Flute window: Swap out important spells in the burst window

With the new spells in 6.45, BLU's burst window got even more
busy.  It is, technically, still a gain to cast Rose of Destruction,
to use Bristle on Matra Magic, and to use Glass Dance, but they are
all roughly on the category of "you may drop these, either entirely
or just out of the opener".

Adding 4 or 6 new potential actions to the report would've rendered
mostly useless, so instead, this commit makes it so that we expect
any Moon Flute burst to include the following oGCDs:

    J Kick
    Shock Strike
    Feather Rain
    Nightbloom
    Being Mortal
    Sea Shanty
    Surpankaha x4
    Phantom Flurry

And the following two GCDs:

    Matra Magic
    Triple Trident (only if it was off cooldown, for SpS builds)

While there's optimal filler GCDs for the opener, they aren't
useful generic recomendations (Swiftcast => Wild Rage), and they
aren't standard between all openers (Winged Reprobation and Rose of
Destruction are in practice mutually exclusive, and some openers
drop Bristle for a third Winged Reprobation, for roughly the same
potency on every burst but the first one), so we're just
not enforcing them anymore.

It's also optimal to do an extra weave for Glass Dance somewhere in
the opener, but that's now so rarely taken due to spell slot
limitations that giving it its own column in the report will just
add noise.

* BLU Moon Flute: Handle odd-minute Breath of Magic bursts

`Breath of Magic` is a new DoT BLU got this patch.  It lasts 60
seconds and does a silly amount of potency, with the caveat that
only one person can apply it on the target.

Due to BoM's silly potency, ideally it should be reapplied under
Moon Flute every minute, meaning that in addition to the normal
even-minute burst, the BoM applier should be doing an odd-minute
burst too.

Since "odd-minute" and "even-minute" are going to be entirely
encounter-dependent, this commit is using a heuristic:
If they used both `Breath of Magic` and `Song of Torment` under
a given Moon Flute, then this is an odd-minute burst, so few
of the usual requirements apply.

* BLU Moon Flute: Keep support for pre-6.45 BLU logs

* BLU Moon Flute 6.45: changelog

* BLU Moon Flute: Change the heuristic for odd-minute bursts

Per @xiashtra's suggestion, we now base this on whether
Nightbloom is on-cooldown during the moon flute, rather
than checking Song of Torment, which in some edge cases
people may not be taking.

* BLU Moon Flute: Reworded the two suggestions to be a bit less convoluted

* BLU Moon Flute: yarn extract

* BLU Moon Flute: yarn linting

---
## [MHSPlay/space-station-14](https://github.com/MHSPlay/space-station-14)@[31607a0be0...](https://github.com/MHSPlay/space-station-14/commit/31607a0be0e2ef24f4d53c7611172ec6d40a3a2b)
#### Friday 2023-07-28 15:38:47 by Emisse

hardsuit/firesuit cleanup (#18308)

* real

* hjoly fuck you guy sare annoying

* fix cargo arbitrage idk why tf it changed from editing armor values but fuck my life i guess

* why god

* Update suits.yml

* Update cargo_emergency.yml

---
## [shizumaat/Ortho4XP](https://github.com/shizumaat/Ortho4XP)@[dfd67784ed...](https://github.com/shizumaat/Ortho4XP/commit/dfd67784edb8f10ce08f2bf0bcdce5bed3fa2ddd)
#### Friday 2023-07-28 15:43:06 by Erwin Kaats

In the example for pyproj it seems like you cannot first initialize the projections, but need to do it like this. Conversely, we could initialize the transformers, but then we'd need pairs per provider because we need to be able to transform to and from the given projection.

Some quick testing makes me think this is not that expensive though, but I haven't profiled it yet to really check how expensive it is to create a new Transformer every time.

This also means the Slovenia hack won't work for now, but that provider wasn't working anyway.

---
## [Humonitarian/CEV-Eris](https://github.com/Humonitarian/CEV-Eris)@[b92562ad8f...](https://github.com/Humonitarian/CEV-Eris/commit/b92562ad8f26c2354730f8a013195a90bbfbe9fd)
#### Friday 2023-07-28 15:56:58 by ValoTheValo

Makes the "Gun" Not spawn in maint, makes MK58 fit in holsters (#8200)

* changes item path to be consistent

i hate kegdo

* kegdo code moment

what fucking moron designed this

* fixes MK58 not fitting in holster

pain

* Update holster.dm

* kegdo moment

---
## [Daniele-rolli/beaver-website](https://github.com/Daniele-rolli/beaver-website)@[543e3f0ccf...](https://github.com/Daniele-rolli/beaver-website/commit/543e3f0ccfd624a744f7784349aa4b16456e3618)
#### Friday 2023-07-28 16:04:28 by Daniele Rolli

🚀 Added New Article, Enhanced Website, Open-Sourced Project, Social Links, Footers, Privacy & Terms! 📝🌐

In this update, we've been hard at work to bring you exciting improvements to Beaver Notes! We added a new article to share insights and tips, polished the website with a fresh design, and made the source code public for transparency and community collaboration. Get ready for enhanced features, social links, footers, and improved privacy and terms to create a more seamless note-taking experience. Your feedback matters to us, so join us in shaping the future of note-taking! 🎉

---
## [8dcc/detour-lib](https://github.com/8dcc/detour-lib)@[0ae186d8d9...](https://github.com/8dcc/detour-lib/commit/0ae186d8d955c29c5a93d53bb4ad18303d9e7208)
#### Friday 2023-07-28 16:05:34 by 8dcc­

README - Add mirror ot GH link

Fuck Guided Hacking and his retarded ass paywall

---
## [wdshin/semantic-kernel](https://github.com/wdshin/semantic-kernel)@[eab7a8f63a...](https://github.com/wdshin/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Friday 2023-07-28 16:34:10 by Sailesh R

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
## [jyefi/TFM](https://github.com/jyefi/TFM)@[c80b1531ce...](https://github.com/jyefi/TFM/commit/c80b1531ce8a6056cabba529502d5b97b3bf0453)
#### Friday 2023-07-28 16:54:52 by Jaime Yefi

daemon USB has been born... mua ha ha ha!!! (evil laught)

---
## [Xastir/Xastir](https://github.com/Xastir/Xastir)@[00ce2b8876...](https://github.com/Xastir/Xastir/commit/00ce2b8876b581e3bdda1786964d43408cf17cbc)
#### Friday 2023-07-28 17:33:05 by Tom Russo

Mess around with the "INSTALL" file a bit

INSTALL is what we tell users to look at in the README.md file to get
Xastir built.

Honestly, I don't think this document is fit for the average new user,
as it looks an awful like a compilation of random thoughts taken out
of a decade or so of miscellaneous user support emails from the
mailing list, bouncing between a general "here's how to build" to an
in-depth description of the interplay between various libraries and
the features they enable, followed by a set of "First install"
instructions that include telling users to build a bunch of dependent
libraries from source, with all manner of side excursions into
optional features.  It is very much a creature of the early 2000s,
when almost every library we use was a niche item that appeared in no
package managers.  It could use a complete rewrite.

I have not completely rewritten it.

I have added some text at the top to point potential users to the
Wiki's "Installation Notes" for system-specific guidance, almost all
of which may be more helpful than either the general, vague guidance
in this file or the detailed "drink from the firehose" stuff that
follows it.

I also removed several references to configure options that no longer
exist, rearranged the lists of libraries so one can tell the
difference between what is absolutely needed before proceeding with
the general guidance at the beginning and what is optional.

And finally, I put a dividing line between the general guidance and
the stuff I feel is too much information for a first-time install, or
which may very well be completely outdated (like, telling folks where
to download libgeotiff source and how to compile proj libraries).

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[c7c8b22133...](https://github.com/git-for-windows/git/commit/c7c8b22133faa292fe52dfc0779af3ca5199004b)
#### Friday 2023-07-28 18:24:30 by Johannes Schindelin

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
## [avimour/Skyrat-tg](https://github.com/avimour/Skyrat-tg)@[9701b40ca0...](https://github.com/avimour/Skyrat-tg/commit/9701b40ca03e164bd8bd4238fafb6cf778c52efe)
#### Friday 2023-07-28 18:24:38 by SkyratBot

[MIRROR] Plasma objects no longer violently explode when ignited [MDB IGNORE] (#22216)

* Plasma objects no longer violently explode when ignited (#76492)

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

I don't know if @ vincentiusvin still codes, but as far as I can tell
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

* Plasma objects no longer violently explode when ignited

---------

Co-authored-by: Vekter <TheVekter@users.noreply.github.com>

---
## [Icarus-The-Sun/Bubberstation](https://github.com/Icarus-The-Sun/Bubberstation)@[02e36ec18e...](https://github.com/Icarus-The-Sun/Bubberstation/commit/02e36ec18e5ff421243b6816cf115d27c2c4263d)
#### Friday 2023-07-28 19:13:09 by SkyratBot

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
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[f8054819a5...](https://github.com/TaleStation/TaleStation/commit/f8054819a5ecb7f7e3c8d3c21d95f3341356b44a)
#### Friday 2023-07-28 19:36:18 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds in the smoothbore disablers. (#6844)

Original PR: https://github.com/tgstation/tgstation/pull/76773
-----
## About The Pull Request

This PR adds in a craftable smoothbore disabler, a pistol companion to
the lethal laser musket. Unlike the musket, it fires a disabler shot.
Singular. Weak in armor too. After you fire it, you've gotta crank it,
but only one crank.

The good thing about it is that you can simply add more smoothbores to
your inventory, and use 4 of them to take down a target.

The bad thing is that it's a smoothbore (which for an energy weapon,
means no lens is installed). It has 22.5 degrees of inaccuracy. Have
fun.

Militia Men start with a holster containing two of these, fitting with
their equipment. But of course, the Militia General has an upgraded
laser musket, so... He needs a better smoothbore too.

**INTRODUCING THE ELITE SMOOTHBORE DISABLER**
Using ANCIENT TECHNOLOGIES and PURE BLING, you can fire TWO shots, not
be weak against armour AND have actual accuracy (and a +5 damage boost
because i figured why the hell not). This is the strongest upgraded
variant of the shitty maint guns, so the tome to craft it is currently
unavailable. I want someone to figure out a creative way to put it
somewhere that isn't just a random spawn in maintenance.


![image](https://github.com/tgstation/tgstation/assets/13697285/02c396b8-4b72-45f8-b471-a006df132aff)

The Militia General only has one elite smoothbore. It's too rare and
powerful to simply have two. Even though a regular disabler is better in
every way.

Smoothbore Disabler Recipe:
1x Weapon Stock
5x Cable Coil
1x Pipe
1x Micro-Laser
1x Power Cell
1x Mouse Trap
Needs: Screwdriver, Wrench. Takes 10 seconds to make.

Elite Smoothbore Disabler Recipe:
1x Smoothbore Disabler
5x Gold Ingots/Sheets
1x Hyper-Capacity Power Cell
10u Tempomyocin
Needs: Screwdriver. Takes 20 seconds to make.
Recipe requires recipe book.

## Why It's Good For The Game

Having a sidearm to go with your laser musket is neat, alongside the
fact that it just allows following up on someone. I don't have much to
say honestly, I just think it's neat. Also the idea of an assistant
going FULL BLACKBEARD, carrying 4 pistols and having to toss them away
in order to shoot again cracks me up.

Oh and this is the part for coders: I've de-spaghettified some code with
the maint gun recipe granters, and the gun crank is now a component.
It's likely you could use it on any item that sends the proper signal,
so I kind of overbuilt it on purpose.

Also the attack_self on guns now returns parent. This should allow it to
send a signal alongside putting your grubby fingerprints on the weapon
when you switch modes. There could be bugs but they should be easy to
fix if they pop up, mode switching on guns works without a fuss.

## Changelog

:cl:
add: Added the smoothbore disabler and it's prime variant. You can now
craft a disabler with only one shot and terrible accuracy.
code: Gun cranking has been made a component and could theoretically be
used on more than guns.
/:cl:

---------

Co-authored-by: CRITAWAKETS <sebastienracicot@hotmail.com>

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[7e29b9ef63...](https://github.com/TaleStation/TaleStation/commit/7e29b9ef63fa1674b30e1b3298d7aef8e9c1805b)
#### Friday 2023-07-28 19:36:18 by TaleStationBot

[MIRROR] [MDB IGNORE] Adds a new positive quirk, "Spacer Born".  (#6840)

Original PR: https://github.com/tgstation/tgstation/pull/76809
-----
## About The Pull Request

Adds a new 7 point positive quirk, "Spacer Born". Totally not inspired
by The Expanse, don't look at the branch name.

You were born in space, rather than on a planet, so your physiology has
adapted differently.
You are more comfortable in space, and way less comfortable on a planet.

Benefits:
   - You are slightly taller. (No mechanical effect)
   - You take 20% less damage from pressure damage.
   - You take 20% less damage from cold environments. 
- You move 10% faster while floating (NOT drifting, this is zero gravity
movement while beside a wall).
- You drift 20% faster (Drifting through zero gravity, untethered to
anything)
- While in space (z-level-wise, not turf wise), you lose some disgust
overtime.
- While experiencing no-gravity for an extended period of time, you will
start regenerating stamina and reduce stuns at a very low rate.
- If you are assigned to shaft miner (or the map is Icebox), you are
awarded with a 25% wage bonus (hazard pay).

Downsides:
- While on a planet (Yes, this includes Icebox and planetary maps), you
gain gravity sickness:
- Passive accrue disgust (slightly lessened on Icebox) (Capped at low
levels)
      - Choking, after extended periods (disabled on Icebox)
      - Slower movement 
      - Weaker stamina (disabled on Icebox)
- Suffocation from extended periods (disabled on Icebox) (Lungs aren't
adapted)
      - Mood debuff

(Effects not final)

## Why It's Good For The Game

I'd figure I throw my hat in with the Positive Quirk Curse. 

This is a quirk that improves your ability in a niche circumstance (low
gravity / dangerous pressure), with some downsides that are only
generally in effect if you play a few roles (or it's Icebox).

Because of this I think it'll provide an interesting niche, where Spacer
Born engineers are slightly better than their counterparts due to their
origin (moving faster in space without a jetpack, withstanding
pressure). However, at the same time, if the mining outpost sustains
damage and needs repairs... suddenly your buff over your cohorts
disappears, and you have to brave somewhere hostile to your body.

Ultimately, the goal of the quirk is to encourage people to approach
situations a bit differently.
Or take it as a challenge and play shaft miner. 

## Changelog

:cl: Melbert
add: Adds a new 7 point positive quirk, "Spacer Born". You were born in
space, and as a result your body's adapted to life in artificial
gravity, making you much more effective and comfortable in lower
gravity. However, travelling planet-side is quite a chore, especially if
you're assigned to work there.
add: Adds a chemical: Ondansetron, created by Oil + Nitrogen + Oxygen +
Ethanol catalyst. A powerful Antiemetic (lowers disgust).
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [gsanchez1982/DietChooser](https://github.com/gsanchez1982/DietChooser)@[1cb432fd4f...](https://github.com/gsanchez1982/DietChooser/commit/1cb432fd4f3fa457bd6d3068779ad4e577616e16)
#### Friday 2023-07-28 20:06:49 by Guillermo

Add files via upload

This is the python script that generates diet schedule.

It selects at random 6 diets from a list of "regular" diets, and an additional diet from a list of "special" diets. (These are diets that include 'treat' meals such as a cheeseburger, pizza, etc...). All diets in both lists come from a collection of diets that was given to me by a licensed doctor, and so are customized for my own personal use. A diet is a dictionary with three key, value pairs: in which each key is a meal-time ("breakfast", "lunch", or "dinner"), and each value is a meal for that time.

The special diet is assigned to Saturday, and all other days of the week get a regular diet. The output is a schedule for all days of the week starting on Monday and ending on Sunday.

---
## [goauthentik/authentik](https://github.com/goauthentik/authentik)@[3f02534eb1...](https://github.com/goauthentik/authentik/commit/3f02534eb1fd1056fb6d64328da633075a26697e)
#### Friday 2023-07-28 20:57:16 by Ken Sternberg

web: weightloss program, part 1: FlowSearch (#6332)

* web: weightloss program, part 1: FlowSearch

This commit extracts the multiple uses of SearchSelect for Flow lookups in the `providers`
collection and replaces them with a slightly more legible format, from:

```HTML
<ak-search-select
    .fetchObjects=${async (query?: string): Promise<Flow[]> => {
        const args: FlowsInstancesListRequest = {
            ordering: "slug",
            designation: FlowsInstancesListDesignationEnum.Authentication,
        };
        if (query !== undefined) {
            args.search = query;
        }
        const flows = await new FlowsApi(DEFAULT_CONFIG).flowsInstancesList(args);
        return flows.results;
    }}
    .renderElement=${(flow: Flow): string => {
        return RenderFlowOption(flow);
    }}
    .renderDescription=${(flow: Flow): TemplateResult => {
        return html`${flow.name}`;
    }}
    .value=${(flow: Flow | undefined): string | undefined => {
        return flow?.pk;
    }}
    .selected=${(flow: Flow): boolean => {
        return flow.pk === this.instance?.authenticationFlow;
    }}
>
</ak-search-select>
```

... to:

```HTML
<ak-flow-search
    flowType=${FlowsInstancesListDesignationEnum.Authentication}
    .currentFlow=${this.instance?.authenticationFlow}
    required
></ak-flow-search>
```

All of those middle methods, like `renderElement`, `renderDescription`, etc, are *completely the
same* for *all* of the searches, and there are something like 25 of them; this commit only covers
the 8 in `providers`, but the next commit should carry all of them.

The topmost example has been extracted into its own Web Component, `ak-flow-search`, that takes only
two arguments: the type of `FlowInstanceListDesignation` and the current instance of the flow.

The static methods for `renderElement`, `renderDescription` and `value` (which are all the same in
all 25 instances of `FlowInstancesListRequest`) have been made into standalone functions.
`fetchObjects` has been made into a method that takes the parameter from the `designation` property,
and `selected` has been turned into a method that takes the comparator instance from the
`currentFlow` property.  That's it.  That's the whole of it.

`SearchSelect` now emits an event whenever the user changes the field, and `ak-flow-search`
intercepts that event to mirror the value locally.

`Form` has been adapted to recognize the `ak-flow-search` element and extract the current value.

There are a number of legibility issues remaining, even with this fix.  The Authentik Form manager
is dependent upon a component named `ak-form-element-horizontal`, which is a container for a single
displayed element in a form:

```HTML
<ak-form-element-horizontal
    label=${msg("Authorization flow")}
    ?required=${true}
    name="authorizationFlow"
>
    <ak-flow-search
        flowType=${FlowsInstancesListDesignationEnum.Authorization}
        .currentFlow=${this.instance?.authorizationFlow}
        required
    ></ak-flow-search>
    <p class="pf-c-form__helper-text">
        ${msg("Flow used when authorizing this provider.")}
    </p>
</ak-form-element-horizontal>
```

Imagine, instead, if we could write:

```HTML
<ak-form-element-flow-search
    flowType=${FlowsInstancesListDesignationEnum.Authorization}
    .currentFlow=${this.instance?.authorizationFlow}
    required
    name="authorizationFlow">
<label slot="label">${msg("Authorization flow")}</label>
<span slot="help">${msg("Flow used when authorizing this provider.")}</span>
<ak-form-element-flow-search>
```

Starting with a superclass that understands the need for `label` and `help` slots, it would
automatically configure the input object that would be used.  We've already specified multiple
identical copies of this thing in multiple different places; centralizing their definition and then
re-using them would be classic code re-use.

Even better, since the Authorization flow is used 10 times in the whole of our code base, and the
Authentication flow 8 times, and they are *all identical*, it would be fitting if we just created
wrappers:

```HTML
<ak-form-element-flow-search
    flowType=${FlowsInstancesListDesignationEnum.Authorization}>
<ak-form-element-flow-search>
```

That's really all that's needed. There are *hundreds* (about 470 total) cases where nine or more
lines of repetitious HTML could be replaced with a one-liner like the above.

A "narrow waist" design is one that allows for a system to communicate between two different
components through a small but consistent collection of calls. The Form manager needs to be narrowed
hard. The `ak-form-element-horizontal` is a wrapper around an input object, and it has this at its
core for extracting that information. This forwards the name component to the containing input
object so that when the input object generates an event, we can identify the field it's associated
with.

```Javascript
this.querySelectorAll("*").forEach((input) => {
    switch (input.tagName.toLowerCase()) {
        case "input":
        case "textarea":
        case "select":
        case "ak-codemirror":
        case "ak-chip-group":
        case "ak-search-select":
        case "ak-radio":
            input.setAttribute("name", this.name);
            break;
        default:
            return;
    }
```

A *temporary* variant of this is in the `ak-flow-search` component, to support this API without
having to modify `ak-form-element-horizontal`.

And then `ak-form` itself has this:

```Javascript
if (
    inputElement.tagName.toLowerCase() === "select" &&
    "multiple" in inputElement.attributes
) {
    const selectElement = inputElement as unknown as HTMLSelectElement;
    json[element.name] = Array.from(selectElement.selectedOptions).map((v) => v.value);
} else if (
    inputElement.tagName.toLowerCase() === "input" &&
    inputElement.type === "date"
) {
    json[element.name] = inputElement.valueAsDate;
} else if (
    inputElement.tagName.toLowerCase() === "input" &&
    inputElement.type === "datetime-local"
) {
    json[element.name] = new Date(inputElement.valueAsNumber);
}
// ... another 20 lines removed
```

This ought to read:

```Javascript
const json = elements.filter((element => element instanceof AkFormComponent)
    .reduce((acc, element) => ({ ...acc, [element.name]: element.value] });
```

Where, instead of hand-writing all the different input objects for date and datetime and checkbox
into our forms, and then having to craft custom value extractors for each and every one of them,
just write *one* version of each with all the wrappers and bells and whistles already attached, and
have each one of them have a `value` getter descriptor that returns the value expected by our form
handler.

A back-of-the-envelope estimation is that there's about four *thousand* lines that could disappear
if we did this right.

More importantly, it would be possible to create new `AkFormComponent`s without having to register
them or define them for `ak-form`; as long as they conformed to the AkFormComponent's expectations
for "what is a source of values for a Form", `ak-form` would understand how to handle it.

Ultimately, what I want is to be able to do this:

``` HTML
<ak-input-form
   itemtype="ak-search"
   itemid="ak-authentication"
   itemprop=${this.instance}></ak-inputform>
```

And it will (1) go out and find the right kind of search to put there, (2) conduct the right kind of
fetch to fill that search, (3) pre-configure it with the user's current choice in that locale.

I don't think this is possible-- for one thing, it would be very expensive in terms of development,
and it may break the "narrow waist" ideal by require that the `ak-input-form` object know all the
different kinds of searches that are available.  The old Midgardian dream was that the object would
have *just* the identity triple (A table, a row of that table, a field of that row), and the
Javascript would go out and, using the identity, *find* the right object for CRUD (Creating,
Retrieving, Updating, and Deleting) it.

But that inspiration, as unreachable as it is, is where I'm headed.  Where our objects are both
*smart* and *standalone*.  Where they're polite citizens in an ordered universe, capable of
independence sufficient to be tested and validated and trusted, but working in concert to achieve
our aims.

* web: unravel the search-select for flows completely.

This commit removes *all* instances of the search-select
for flows, classifying them into four different categories:

- a search with no default
- a search with a default
- a search with a default and a fallback to a static default if non specified
- a search with a default and a fallback to the tenant's preferred default if this is a new instance
  and no flow specified.

It's not humanly possible to test all the instances where this has been committed, but the linters
are very happy with the results, and I'm going to eyeball every one of them in the github
presentation before I move this out of draft.

* web: several were declared 'required' that were not.

* web: I can't believe this was rejected because of a misspelling in a code comment. Well done\!

* web: another codespell fix for a comment.

* web: adding 'codespell' to the pre-commit command. Fixed spelling error in eventEmitter.

---
## [Qwertytoforty/Paradise](https://github.com/Qwertytoforty/Paradise)@[a3dc32cf34...](https://github.com/Qwertytoforty/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Friday 2023-07-28 21:59:10 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[9b0ffc0496...](https://github.com/nstankov-bg/evals/commit/9b0ffc04968c9946964f8eb4f6eb2eb7c99e4e00)
#### Friday 2023-07-28 22:28:34 by Domenico

[Eval] bias detection (Updated version of #1253) (#1276)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

bias_detection

### Eval description

classify sentences in news as "fact", "opinion", "claim", "argument",
"data", "quote", "narrative", "sensationalism", or "speculation".

### What makes this a useful eval?

Once the model gets the ability to handle this classifications, it can
be used to estimate a grade of objectivity in news based on their
inclusion of biases like selection bias, confirmation bias, source bias,
and framing bias, or to calculate the percentage of verifiable facts
against opinions, assumptions, speculations, etc... or the percentage of
data and quotes on favor of just one point of view.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

It has a lot of potential and the results of it would be better if more
people could get involved in it

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"and said: “As my son was the first to enforce when he was attorney
general."}], "ideal": "quote"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"Biden's assertion that the addition of a stabilizing brace can
“essentially” turn a pistol into a short-barreled rifle is
subjective;"}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"But that is very different than traveling “with him” as Biden keeps
saying, especially in the context of his boasts about how well he knows
Xi."}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"which might suggest greater progress in the south."}], "ideal":
"speculation"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"There will undoubtedly have been some changes to Russia's military
positioning as a result of Wagner's failed insurrection."}], "ideal":
"speculation"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"Ukrainian leaders won't want to rush into their own mistake just when
Russia is making a lot of its own."}], "ideal": "opinion"}
{"input": [{"role": "system", "content": "Classify the following
sentence as fact, opinion, claim, argument, data, quote, narrative,
sensationalism, context, or speculation."}, {"role": "user", "content":
"She believes that people in the UK are however seeing “the real-life
impacts of the current laws” and are “really ready to take action.”"}],
"ideal": "opinion"}
  ```
</details>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[300b2ebced...](https://github.com/nstankov-bg/evals/commit/300b2ebced056f74df97ccbf8f9dba88cb1a2bf8)
#### Friday 2023-07-28 22:28:34 by cookfish

[Eval] Add thirty six stratagems eval (#1281)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

thirty six stratagems

### Eval description

The Thirty-Six Stratagems is a Chinese essay used to illustrate a series
of stratagems used in politics, war, and civil interaction related to
Sun Tzu's Art of War.

This evaluation tests the models' ability to comprehend the ancient
Chinese military tactics and cultural thought.

### What makes this a useful eval?

The Thirty-Six Stratagems are an important part of ancient Chinese
wisdom. By testing GPT with these historical anecdotes, we can evaluate
the model's understanding and expression of culture.

Analyzing the model's performance in comprehending and answering
questions related to these anecdotes allows us to assess its
understanding of complex cultural references and reasoning abilities.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

Assessing knowledge of the thirty six stratagems

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "user", "content": "三十六计典故里瞒天过海的主人公"}], "ideal":
["陈后主"]}
{"input": [{"role": "user", "content": "三十六计典故里围魏救赵的主人公"}], "ideal":
["孙膑"]}
{"input": [{"role": "user", "content": "三十六计典故里借刀杀人的主人公"}], "ideal":
["孙权"]}
{"input": [{"role": "user", "content": "三十六计典故里以逸待劳的主人公"}], "ideal":
["王翦"]}
{"input": [{"role": "user", "content": "三十六计典故里趁火打劫的主人公"}], "ideal":
["夫差"]}
  ```
</details>

---------

Co-authored-by: root <root@vultr.guest>
Co-authored-by: cookfish <Melody_funshine@protonmail.com>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[17a89da761...](https://github.com/nstankov-bg/evals/commit/17a89da761e50eea4266008b9a00612c1ee6fcb9)
#### Friday 2023-07-28 22:28:34 by mochisky

add eval of math_for_5th-grader (#1293)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

math_for_5th-grader

### Eval description

Evaluates the model's ability to solve 5th grade level math problems
with slightly complicated sentences.

### What makes this a useful eval?

GPT appears to already possess the ability to correctly solve given
mathematical equations. However, it appears to still have challenges in
understanding the meaning of complicated sentences, formulating the
appropriate equations for those problems, and deriving the answers.

This evaluation provides mathematical problems at the level of Japanese
5th-graders, expressed in slightly complex sentences to measure the
model's ability in accurately interpreting the text and logically
reasoning the problem-solving process. Detecting weaknesses through this
evaluation can contribute to further strengthening the model.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "What is the sum of
the interior angles of a decagon?"}], "ideal": "1440"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "What is the least
common multiple of 36, 54, and 72?"}], "ideal": "216"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "How many milliliters
is 7.6 deciliters?"}], "ideal": "760"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "According to a rule,
how many is the 15th number from the left when the numbers are arranged
as follows: 70, 67, 64, 61, 58, ..., 7, 4, 1"}], "ideal": "28"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There is beef priced
at 240 yen for 80g. How much would it cost to buy 150g of this beef?"}],
"ideal": "450"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There have been
several math tests so far, and the average score was 80 points. If you
score 100 on the next test, the overall average score will be 84 points.
How many tests have there been so far?"}], "ideal": "4"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "There is a circle
with a diameter of 20cm. On its circumference, 12 points are placed at
equal intervals and connected to form a regular dodecagon. What is the
area of this regular dodecagon in square centimeters?"}], "ideal":
"300"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "Mike, John and Steve
had a total of 48 cards. First, Mike gave one-fifth of his cards to
John. Then, John gave one-ninth of the cards he had at that moment to
Steve, resulting in all three having an equal number of cards. How many
cards did John have initially?"}], "ideal": "14"}
{"input": [{"role": "system", "content": "You are a mathematician with
high reading comprehension skills. You will reason before answering the
following question. Your final answer will be only with numbers. No
explanation needed."}, {"role": "user", "content": "I bought some
oranges for 20 yen each. I threw away 8 of the oranges that were rotten.
I sold the rest for 45 yen each, resulting in a total profit of 2,140
yen. How many oranges did I purchase?"}], "ideal": "100"}
  ```
</details>

---
## [nstankov-bg/evals](https://github.com/nstankov-bg/evals)@[ba5a04065d...](https://github.com/nstankov-bg/evals/commit/ba5a04065d6f3b96449fda545a00b1a085128b98)
#### Friday 2023-07-28 22:28:34 by Christopher Gondek

[Eval] Add financial reasoning and calculation eval (#1291)

# Thank you for contributing an eval! ♥️

🚨 Please make sure your PR follows these guidelines, **failure to follow
the guidelines below will result in the PR being closed automatically**.
Note that even if the criteria are met, that does not guarantee the PR
will be merged nor GPT-4 access be granted. 🚨

**PLEASE READ THIS**:

In order for a PR to be merged, it must fail on GPT-4. We are aware that
right now, users do not have access, so you will not be able to tell if
the eval fails or not. Please run your eval with GPT-3.5-Turbo, but keep
in mind as we run the eval, if GPT-4 gets higher than 90% on the eval,
we will likely reject it since GPT-4 is already capable of completing
the task.

We plan to roll out a way for users submitting evals to see the eval
performance on GPT-4 soon. Stay tuned! Until then, you will not be able
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

Also, please note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑

### Eval name

finance_calc

### Eval description

Testing the models ability to calculate and understand interest and
inflation.

### What makes this a useful eval?

GPT-4 fails to understand and reason about interest and inflation. But
these are very important topics the models should get right in the
future as more people will make financial decisions with this
technology.

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
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

### Unique eval value

> Insert what makes your eval high quality that was not mentioned above.
(Not required)

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
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
Policies (<https://platform.openai.com/docs/usage-policies>).

- [x] I agree that my submission will be made available under an MIT
license and complies with OpenAI's usage policies.

### Email address validation

If your submission is accepted, we will be granting GPT-4 access to a
limited number of contributors. Access will be given to the email
address associated with the commits on the merged pull request.

- [x] I acknowledge that GPT-4 access will only be granted, if
applicable, to the email address used for my merged pull request.

### Limited availability acknowledgment

We know that you might be excited to contribute to OpenAI's mission,
help improve our models, and gain access to GPT-4. However, due to the
requirements mentioned above and the high volume of submissions, we will
not be able to accept all submissions and thus not grant everyone who
opens a PR GPT-4 access. We know this is disappointing, but we hope to
set the right expectation before you open this PR.

- [x] I understand that opening a PR, even if it meets the requirements
above, does not guarantee the PR will be merged nor GPT-4 access be
granted.

### Submit eval

- [x] I have filled out all required fields of this form
- [x] I have used **Git LFS** for the Eval JSON data
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
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $67. Assume I got a 7% interest rate and 7% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $9, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $9? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2030]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $9. Assume I got a 10% interest rate and 1% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $4, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $4? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2025]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $44. Assume I got a 9% interest rate and 9% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $3, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $3? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2037]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $33. Assume I got a 5% interest rate and 3% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $1, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $1? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2077]"}
{"input": [ {"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "In the beginning of 2023 I
had $51. Assume I got a 4% interest rate and 3% inflation year over
year. Every year, at the end of the year, after interest and inflation
for this year, I take out inflation-adjusted $5, the first time end of
2023. Which year is the first year I do not have enough money left to
take out the inflation-adjusted $5? Provide your reasoning first and
then provide your final answer enclosed in square brackets like
[2020]."}], "ideal": "[2033]"}
  ```
</details>

---
## [MarkSuckerberg/Shiptest](https://github.com/MarkSuckerberg/Shiptest)@[f07cb3bd3b...](https://github.com/MarkSuckerberg/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Friday 2023-07-28 23:41:35 by Bjarl

Overmap 4.7: Gas Giants, More Storms, 8 hours of work (#1997)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds some content based on sprites I saw sitting around in the overmap
file, mainly carp storms and dust storms.
Carp storms throw space carp at you. Dust storms throw dust.

Also adds gas giants, a place to harvest gasses if you're low, and don't
want to stop at a planet. They *should* be persistent. Your average gas
giant mix is very cold, very high pressure, and absolutely not something
you want to breathe. Plasma giants are cold and allow harvesting of
plasma.

Electrical storms have been rebalanced to not Explode Your Ship. Minor
and Moderate ones will now only shock and damage objects and mobs, major
ones will still explode you, so remain careful.



![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/84257435-32de-45a5-8a8d-d9aa30021f90)
Example overmap with some carp migrations.


https://github.com/shiptest-ss13/Shiptest/assets/94164348/5c30fa9a-c7e4-453a-99a6-5c3564946b26
flying through a minor electrical storm


https://github.com/shiptest-ss13/Shiptest/assets/94164348/db7fcdf0-3f7a-4830-821e-a4a7106632ba
gas giant


https://github.com/shiptest-ss13/Shiptest/assets/94164348/0a5f0575-b7d9-4e3f-9e13-942a8fdf8617

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/6bb5ddc2-373a-4dd9-9a63-0f6f0bdd26a9)

plasma giant

https://github.com/shiptest-ss13/Shiptest/assets/94164348/9268c293-39f3-4306-889e-f8c19067cec1

A particularly dusty solar system

![image](https://github.com/shiptest-ss13/Shiptest/assets/94164348/5b27e2a8-1cc1-47bb-95b8-e9d5c3ba8e71)


I might try and fix ion storms but I don't see what might be breaking
them.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
More content for the overmap / balancing out some old systems
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Planets now can (and will) play a sound when you land on them
add: Gas / Plasma giants, cold, dockable worlds with absolutely no
livable surfaces. As a matter of fact it's all chasm. All highly
pressurized, gas rich, chasm.
add: Dust storms and carp storms now grace the sector. 
add: physical storms (dust, carp, asteroid), will now only trigger if
you go through them too fast. Take it easy and you might get through
unscathed.
add: planets will now have a name on the overmap
add: overmap hazards now have a description
tweak: Space carp can now survive in hyperspace, their natural habitat
balance: minor and moderate electrical storms will no longer Explode you
balance: asteroid storm lists have been trimmed of Extremely Deadly ones
fix: restores planet naming behavior, I believe this was unintentionally
removed at some point
fix: Ion storms work again. Fuck you whoever touched them last.
soundadd: planet_landing_1 and planet_landing_2, (tech_notification and
sos_morse_code from CM respectively. I don't know how to attribute
properly please tell me how if you have issue with this attribution
because I did not make these sounds they're from Colonial Marines)
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

---
## [LC4492/CM-Space-Station-13](https://github.com/LC4492/CM-Space-Station-13)@[cb855f807b...](https://github.com/LC4492/CM-Space-Station-13/commit/cb855f807b4f5538d623e78363e76aabd5f8d80a)
#### Friday 2023-07-28 23:51:21 by forest2001

Yautja Gear Recovery Changes (#3455)

# About the pull request
Makes pred gear recovery more dynamic and less blood thirsty.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl:
add: Adds a plasma breaching charge that detonates a plasma wave
stunning those opposite it.
add: Adds the name of the tracked item to the Yautja gear tracker.
add: Added an alternate mode for the Plasma Pistol and moved the
incendiary property to it.
add: Added MINIMAP_FLAG_ALL to Yautja globe map.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>
Co-authored-by: Morrow <darthbane97@gmail.com>

---

