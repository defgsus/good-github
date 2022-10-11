## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-10-10](docs/good-messages/2022/2022-10-10.md)


2,084,383 events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,084,383 were push events containing 3,160,840 commit messages that amount to 250,706,115 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 39 messages:


## [zeeb92/tgstation](https://github.com/zeeb92/tgstation)@[a2577296e6...](https://github.com/zeeb92/tgstation/commit/a2577296e62a0f3c335648169a335fe7d3de4bdc)
#### Monday 2022-10-10 00:02:13 by RikuTheKiller

Upgrades the Modsuit Adapter Shell (#70286)

Code improvements are much appreciated as some things may be rather hacky.

Adds more options to the currently very limited modsuit adapter shell. Right now you can only select a module and activate (not deploy) the suit.

This has some major problems as you literally can't even deploy the suit to activate it so that's rendered useless and selecting a module is like... kind of a weird input anyways but I won't judge so I left it in. Please comment down below if you'd like for me to add an "Activate Selected Module" input and "On Module Activated" output as those are certainly possible to do. I was just a little torn on how balanced that would be.

Changes:

"Module to Select" input is now an option. You can still use a string input, but simply inserting it into the suit and activating it, then accessing the circuit that way will give you a list of all modules that the modsuit has.
Modsuit quick deploy (RMB) no longer tries to deploy the rest of the pieces when used while the suit is only partially deployed. It will now instead retract the extended pieces. This makes the "Toggle Deployment" input less prone to errors. (Why was it like this in the first place? Having to manually retract the already extended pieces sucks ass.)
Added Inputs:

"Toggle Deployment" is a new signal input that does exactly what it says it does. It simply tries to extend or retract all pieces of the modsuit depending on it's current state.
Added Outputs:

"Activated" is a new number output that outputs 1 if the suit is activated and 0 if it's not.
"Deployed" is a new number output that outputs 1 if all parts of the suit are extended and 0 if they aren't.
"Deployed Parts" is a new string list output that outputs a list of the names of all currently deployed parts.
"On Deploy" is a new signal output that outputs a signal whenever all parts of the suit are deployed or retracted, regardless of the method used.
"Finished Toggling" is a new signal output that outputs a signal whenever the suit has finished activating or deactivating, regardless of the method used.

---
## [zeeb92/tgstation](https://github.com/zeeb92/tgstation)@[422accbe4e...](https://github.com/zeeb92/tgstation/commit/422accbe4e9b53f075f9a76ba6293435cb3399da)
#### Monday 2022-10-10 00:02:13 by John Willard

[MDB IGNORE] Shuttle engines part 2: Engines are now machines (#69793)

* Makes engines machines instead of structures

* Updates the maps

* Fixes boards and anchoring

* Removes 2 unused engine types

Router was actually used a total of once, so I just replaced it with propulsion.
I think cutting down on these useless engine types that make no difference in-game would be a nice first step to adding more functionalities to them.

* Don't use power (since shuttles dont have)

Shuttles don't have APCs, instead they just have infinite power, so I'm removing their power usage for now. I'm hoping this can be removed when unique mechanics are added to engines, because I would like them to make use of power like other machines.

* re-organizes vars

* deletes deleted dm file

* Slightly improves cargo selling code

* Renames the updatepaths

* Removes in_wall engines

I hate this stupid engine it sucks it's useless it's used solely for the tram it provides nothing of benefit to the server
replaces them with regular engines

---
## [Nerev4r/Skyrat-tg](https://github.com/Nerev4r/Skyrat-tg)@[23b7daee59...](https://github.com/Nerev4r/Skyrat-tg/commit/23b7daee59100e34f488893b57cd3787a0c08b99)
#### Monday 2022-10-10 01:12:46 by SkyratBot

[MIRROR] Simplifies SM damage calculation, tweaks the numbers. [MDB IGNORE] (#16733)

* Simplifies SM damage calculation, tweaks the numbers. (#70347)

About The Pull Request

We apply the damage hardcap individually now, split off the old flat 1.8 into individual caps for heat, moles, and power.

Set it to 1.5 for heat, 1 for mole and 1 for power. This means for most delams it'll be a tad slower! But its possible to make SM delam nearly twice as fast if you combine all 3. (3.5). Be pretty hard tho.

Set the heat healing to -1 so you can counteract one factor at most (except heat since you'll never get both heat healing and heat damage at the same time anyway).

I'm not hell bent on any of the numbers, just picked round even ones and ones that i think will make sense. If you want them changed lmk.

Got rid of the cascade mole and power multipliers since there's probably like three people that are aware that it even exists. Ideally we just add another entry to the CIMS but its already pretty crowded. Figured nobody is gonna miss it anyway? Sorry ghil.

Got rid of the moles multiplier thing since its nicer to keep the temp damage fully based on temp damage instead of adding another multiplier. I just applied the .25 to the damage flatly, meaning it slows down delams again!

And some space exposure stuff: #70347 (comment)
Why It's Good For The Game

Hardcap: Discrete, less randomly interconnected factors are easier to present and remember. The calculation procs are also made to be additive so we had to hack a bit and do some rescaling to accomodate the old behavior in my original PR #69240. Can remove the hack if this pr goes through.

Cascade and mole multiplier: The rest are just getting rid of underutilized factors so we have a cleaner behavior to maintain, present, and understand. (In a perfect world modifiers that aren't visible to the players shouldn't have been merged in the first place smh smh)
Changelog

🆑
fix: Fixed sm space exposure damage going through walls
del: got rid of the molar multiplier for sm heating damage. It will now only impact molar damage and temp limit. We apply the lowest value directly so this slows down sm delams a tiny bit.
del: got rid of cascades making sm delam at 450 moles and 1250 mev. It delams normally now.
balance: Applied the sm damage hardcap of 1.8 individually to heat (1.5), moles (1), power (1). Meaning most sm delams are slower now, but the really bad ones can be faster.
balance: Halved sm temp healing across the board. Temp limits are still the same though so you shouldn't notice it that much.
balance: Halved SM power damage across the board.
balance: Changed sm space exposure damage to just check for the current tile and adjacent atmos connected tiles.
/🆑

* Simplifies SM damage calculation, tweaks the numbers.

Co-authored-by: vincentiusvin <54709710+vincentiusvin@users.noreply.github.com>

---
## [intel/linux-intel-lts](https://github.com/intel/linux-intel-lts)@[adee8f3082...](https://github.com/intel/linux-intel-lts/commit/adee8f3082b01e5dab620d651e3ec75f57c0c855)
#### Monday 2022-10-10 01:57:07 by Peter Zijlstra

x86/nospec: Unwreck the RSB stuffing

commit 4e3aa9238277597c6c7624f302d81a7b568b6f2d upstream.

Commit 2b1299322016 ("x86/speculation: Add RSB VM Exit protections")
made a right mess of the RSB stuffing, rewrite the whole thing to not
suck.

Thanks to Andrew for the enlightening comment about Post-Barrier RSB
things so we can make this code less magical.

Cc: stable@vger.kernel.org
Signed-off-by: Peter Zijlstra (Intel) <peterz@infradead.org>
Link: https://lkml.kernel.org/r/YvuNdDWoUZSBjYcm@worktop.programming.kicks-ass.net
[bwh: Backported to 5.10: adjust context]
Signed-off-by: Ben Hutchings <benh@debian.org>
Signed-off-by: Greg Kroah-Hartman <gregkh@linuxfoundation.org>

---
## [Fohnzii/css-exercises](https://github.com/Fohnzii/css-exercises)@[58402c9430...](https://github.com/Fohnzii/css-exercises/commit/58402c9430a8ce17227abed8864d9f9f3e43af53)
#### Monday 2022-10-10 02:52:36 by fohnzii

Holy shit i have a long way to go

This exercise took me an hour and a half to botch my way through.
until finally I said fuck it and looked at the solution.css where it
showed me how utterly retarded and incompetent I am. I wrote at least
20-30 lines of code to get nowhere near to the ~8 lines of code it took
to properly do this. I overthought this by a billion and fundamentally
do not comprehend how flex-containers actually affect flex-items.

---
## [cbiagini/Space-Hamlet-Group-Game-](https://github.com/cbiagini/Space-Hamlet-Group-Game-)@[43e38d7722...](https://github.com/cbiagini/Space-Hamlet-Group-Game-/commit/43e38d7722577ea2d27dec93f82c1508c4a77331)
#### Monday 2022-10-10 05:50:47 by sophaloaf24

I tried to do coding and other stuff but low key

Lowered Volume (hopefully), added some assets and set them up for use, made npc dialogue box, added music to fail scene, tried to do some coding and get things set up for victory triggers, created ink files for endings but wasnt able to write them (fuck you unity and ink)

---
## [Enbyy/orbstation](https://github.com/Enbyy/orbstation)@[1810b85553...](https://github.com/Enbyy/orbstation/commit/1810b855536f05891593b1379e455164f45fab3a)
#### Monday 2022-10-10 07:09:30 by tralezab

Heretics cannot be converted, and are immune to cult stun hands. Instead, the cult is rewarded for sacrificing them with the bloody bastard sword, an oversized SPIN2WIN funblade. + Soul Stealing Fantasy Affix (#69725)

About The Pull Request

Heretics can no longer be converted to a cult, as they follow their own Forgotten Gods.
Instead, Nar'Sie will reward the cult for managing to sacrifice one, with the bastard sword.
The bloody bastard sword has been cleaned up codewise and all that. Because it is a free reward instead of a (removed) progression mechanic of cult, it swings just a bit slower during the spin and doesn't have a jaunt. It's still a !fun! swinging sword of hilarity and death.
BLOODY BASTARD https://www.youtube.com/watch?v=ukznXQ3MgN0
Fantasy weapons can now roll "soul-stealing" weapons. They, on killing something, capture its soul inside the item.

    Add fail conditions that instantly end a spin2win, ala how 

    Mimes can now hold a baguette like a sword by right clicking it #69592 works

Why It's Good For The Game

Bloody bastard sword was fun, it made no sense that heretics were valid converts when they're already worshipping a DIFFERENT evil god granting them powers. Should be in a good spot as a nice little antag to antag special interaction. I fucking love antag to antag special interactions, we should have more of 'em

Fantasy affixes are always a neat thing to throw a new component into
Changelog

cl
add: Heretics can no longer be converted to cult. But sacrificing them is very valuable to Nar'Sie, and she will grant special weapons if you manage to do so.
add: Fantasy affixes can also include soul-stealing items!
/cl

---
## [Enbyy/orbstation](https://github.com/Enbyy/orbstation)@[23bfdec8f4...](https://github.com/Enbyy/orbstation/commit/23bfdec8f43046f7b54906509e38ed1ad91f5096)
#### Monday 2022-10-10 07:09:40 by LemonInTheDark

Multiz Rework: Human Suffering Edition (Contains PLANE CUBE) (#69115)


About The Pull Request

I've reworked multiz. This was done because our current implementation of multiz flattens planes down into just the openspace plane. This breaks any effects we attach to plane masters (including lighting), but it also totally kills the SIDE_MAP map format, which we NEED for wallening (A major 3/4ths resprite of all wall and wall adjacent things, making them more then one tile high. Without sidemap we would be unable to display things both in from of and behind objects on map. Stupid.)

This required MASSIVE changes. Both to all uses of the plane var for reasons I'll discuss later, and to a ton of different systems that interact with rendering.

I'll do my best to keep this compact, but there's only so much I can do. Sorry brother.
Core idea

OK: first thing.
vis_contents as it works now squishes the planes of everything inside it down into the plane of the vis_loc.
This is bad. But how to do better?

It's trivially easy to make copies of our existing plane masters but offset, and relay them to the bottom of the plane above. Not a problem. The issue is how to get the actual atoms on the map to "land" on them properly.

We could use FLOAT_PLANE to offset planes based off how they're being seen, in theory this would allow us to create lens for how objects are viewed.
But that's not a stable thing to do, because properly "landing" a plane on a desired plane master would require taking into account every bit of how it's being seen, would inherently break this effect.

Ok so we need to manually edit planes based off "z layer" (IE: what layer of a z stack are you on).

That's the key conceit of this pr. Implementing the plane cube, and ensuring planes are always offset properly.
Everything else is just gravy.
About the Plane Cube

Each plane master (except ones that opt out) is copied down by some constant value equal to the max absolute change between the first and the last plane.
We do this based off the max z stack size detected by SSmapping. This is also where updates come from, and where all our updating logic will live.

As mentioned, plane masters can choose to opt out of being mirrored down. In this case, anything that interacts with them assuming that they'll be offset will instead just get back the valid plane value. This works for render targets too, since I had to work them into the system as well.

Plane masters can also be temporarily hidden from the client's screen. This is done as an attempt at optimization, and applies to anything used in niche cases, or planes only used if there's a z layer below you.
About Plane Master Groups

BYOND supports having different "maps" on screen at once (IE: groups of items/turfs/etc)
Plane masters cannot cover 2 maps at once, since their location is determined by their screen_loc.
So we need to maintain a mirror of each plane for every map we have open.

This was quite messy, so I've refactored it (and maps too) to be a bit more modular.

Rather then storing a list of plane masters, we store a list of plane master group datums.
Each datum is in charge of the plane masters for its particular map, both creating them, and managing them.

Like I mentioned, I also refactored map views. Adding a new mapview is now as simple as newing a /atom/movable/screen/map_view, calling generate_view with the appropriate map id, setting things you want to display in its vis_contents, and then calling display_to on it, passing in the mob to show ourselves to.

Much better then the hardcoded pattern we used to use. So much duplicated code man.

Oh and plane master controllers, that system we have that allows for applying filters to sets of plane masters? I've made it use lookups on plane master groups now, rather then hanging references to all impacted planes. This makes logic easier, and prevents the need to manage references and update the controllers.

image

In addition, I've added a debug ui for plane masters.
It allows you to view all of your own plane masters and short descriptions of what they do, alongside tools for editing them and their relays.

It ALSO supports editing someone elses plane masters, AND it supports (in a very fragile and incomplete manner) viewing literally through someone else's eyes, including their plane masters. This is very useful, because it means you can debug "hey my X is yorked" issues yourself, on live.

In order to accomplish this I have needed to add setters for an ungodly amount of visual impacting vars. Sight flags, eye, see_invis, see_in_dark, etc.

It also comes with an info dump about the ui, and plane masters/relays in general.

Sort of on that note. I've documented everything I know that's niche/useful about our visual effects and rendering system. My hope is this will serve to bring people up to speed on what can be done more quickly, alongside making my sin here less horrible.
See https://github.com/LemonInTheDark/tgstation/blob/multiz-hell/.github/guides/VISUALS.md.
"Landing" planes

Ok so I've explained the backend, but how do we actually land planes properly?
Most of the time this is really simple. When a plane var is set, we need to provide some spokesperson for the appearance's z level. We can use this to derive their z layer, and thus what offset to use.

This is just a lot of gruntwork, but it's occasionally more complex.
Sometimes we need to cache a list of z layer -> effect, and then use that.
Also a LOT of updating on z move. So much z move shit.

Oh. and in order to make byond darkness work properly, I needed to add SEE_BLACKNESS to all sight flags.
This draws darkness to plane 0, which means I'm able to relay it around and draw it on different z layers as is possible. fun darkness ripple effects incoming someday

I also need to update mob overlays on move.
I do this by realiizing their appearances, mutating their plane, and then readding the overlay in the correct order.

The cost of this is currently 3N. I'm convinced this could be improved, but I've not got to it yet.
It can also occasionally cause overlays to corrupt. This is fixed by laying a protective ward of overlays.Copy in the sand, but that spell makes the compiler confused, so I'll have to bully lummy about fixing it at some point.
Behavior changes

We've had to give up on the already broken gateway "see through" effect. Won't work without managing gateway plane masters or something stupid. Not worth it.
So instead we display the other side as a ui element. It's worse, but not that bad.

Because vis_contents no longer flattens planes (most of the time), some uses of it now have interesting behavior.
The main thing that comes to mind is alert popups that display mobs. They can impact the lighting plane.
I don't really care, but it should be fixable, I think, given elbow grease.

Ah and I've cleaned up layers and plane defines to make them a bit easier to read/reason about, at least I think.
Why It's Good For The Game
<visual candy>

Fixes #65800
Fixes #68461
Changelog

cl
refactor: Refactored... well a lot really. Map views, anything to do with planes, multiz, a shit ton of rendering stuff. Basically if you see anything off visually report it
admin: VV a mob, and hit View/Edit Planes in the dropdown to steal their view, and modify it as you like. You can do the same to yourself using the Edit/Debug Planes verb
/cl

---
## [CivilizationVIBetterBalancedGame/BetterBalancedGame](https://github.com/CivilizationVIBetterBalancedGame/BetterBalancedGame)@[0f7828b31a...](https://github.com/CivilizationVIBetterBalancedGame/BetterBalancedGame/commit/0f7828b31a73ec83006ddd119dede2418539e9ba)
#### Monday 2022-10-10 07:37:18 by ZhenjaMax

English update (#49)

* English lang 5.1

New lines for 5.1 patch:
Ottoman UU (naval) - can enter Ocean tiles regardless of researched Technologies;
Ottoman Ibrahim unique governor R2 promotion - +1 movement within 10 tiles of city instead of useless griveances ability;

- Goddess of the Hunt pantheon - +2 gold instead of +1 food;

- Railroad - cost increased to 2 iron & 1 coal per tile;
- Intelligence Agency - +50% production to Spies, +2 capacity (instead of +1).
- Statue of Zeus World Wonder - +35% instead of +50% to anti-cavalry;

- Agoge policy - recon (Classical and earlier);
- Feudal Contract policy - recon (Renaissance and earlier);
- Grande Armee policy - recon (Industrial and earlier);
- Military First policy - recon (all);

Edited lines for 5.1 patch:
Eleanor leader ability - works grant +1 instead of +2;
Ethiopia UU - +1 movement if starts in Hills instead of ignoring them;

Deleted lines for 5.1 patch:
Ethiopia UI - reverted to base-game (faith from adjacent mountains);
Rome UD - reverted to base-game (no culture per adjacent districts);

New other lines:
- Base ranged naval units - Range of these units (1, 2, 3, 4);
- Warrior Monk R2 Promotion - 250 Religious pressure within 6 tiles clarification;
- Victor T3 promotion - anti-air icon;
- Pingala L1 promotion - clarification what affect +100% GPP;
- Orszaghaz World Wonder (English fix) - clarification of Diplomatic favor, +1 is equal +100%;

Medina quarter policy - district icon;
Liberalism policy - district icon;
New deal policy - district icon;
Serfdom policy - charge icon;
Public Works policy - charge icon;
Logistics policy - movement icon;
Integrated Attack Logistics policy - movement icon;
Public Transport (English fix) - yields clarification;
Gothic Architecture policy (English fix) - toward Renaissance and earlier;
Wisselbanken policy (English fix) - +0.25 points (not .25), re-wrote sentence;
Machiavellianism policy - turn icon;
Containment policy - government icon;
Hallyu policy - promotion icon;
Non-stated Actors policy - promotion icon;
Press Gangs policy (English fix) - forgotten "+" character.

Edited other lines:
- Australia leader ability - turn icon;
- France civilization ability (English fix) - moved number and tourism icon near each other;
- Macedon leader ability - turn icon;
- Ottoman UB - first constructed UB grants free Governor Title; it is old artifact from v4 that nobody wrote before;
- Scotland UI - grants +1 appeal to adjacent tiles; edited sentence;
- Spain UI - 8 tiles from current capital; added Science icon;

- Divine Spark pantheon - Great People icons;
- City Patron pantheon - district icons;
- God of War and Plunder pantheon - Great People icons;

- Warlord Throne - production for all cities;
- Foreign Ministry (English fix) - moved items between sentences;

- Trench Warfare policy - for "all" (forgotten word);
- Insulae policy - district icon;

* 5.1 English following new commits

New lines for 5.1 patch:
- Kotoku-in world wonder - allows purchasing Monk in this city (with wonder);
- World Religion congress resolution - +10 strength for religious units only (no Monks).
>
Edited lines for 5.1 patch:
- Sumerian leader ability - start game with War-cart instead of Warrior unit;
- Goddess of the Hunt - food instead of production;
- Railroad - 2 iron & 0 coal.
>
New other lines:
- Cree UU - promotion icon.
>
Edited other lines:
- Rome leader ability - simpify description, just grants Monument building; reason - other cases are giga rare and useless because no one rush Monument for first 8 turns in my opinion; if you don't agree we can discuss it in channel and then change to something else;
- Spain civilization ability - Corps and Army icons for Fleets and Armadas;
- Spain UI - forgotten "current" word for XP2;
- Pingala L1 (English fix) - lower case;
- Grand Master Chapel - can purchase in founded cities, not just owned.

---
## [mydir/postgres](https://github.com/mydir/postgres)@[1c27d16e6e...](https://github.com/mydir/postgres/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Monday 2022-10-10 08:07:32 by Tom Lane

Revise tree-walk APIs to improve spec compliance & silence warnings.

expression_tree_walker and allied functions have traditionally
declared their callback functions as, say, "bool (*walker) ()"
to allow for variation in the declared types of the callback
functions' context argument.  This is apparently going to be
forbidden by the next version of the C standard, and the latest
version of clang warns about that.  In any case it's always
been pretty poor for error-detection purposes, so fixing it is
a good thing to do.

What we want to do is change the callback argument declarations to
be like "bool (*walker) (Node *node, void *context)", which is
correct so far as expression_tree_walker and friends are concerned,
but not change the actual callback functions.  Strict compliance with
the C standard would require changing them to declare their arguments
as "void *context" and then cast to the appropriate context struct
type internally.  That'd be very invasive and it would also introduce
a bunch of opportunities for future bugs, since we'd no longer have
any check that the correct sort of context object is passed by outside
callers or internal recursion cases.  Therefore, we're just going
to ignore the standard's position that "void *" isn't necessarily
compatible with struct pointers.  No machine built in the last forty
or so years actually behaves that way, so it's not worth introducing
bug hazards for compatibility with long-dead hardware.

Therefore, to silence these compiler warnings, introduce a layer of
macro wrappers that cast the supplied function name to the official
argument type.  Thanks to our use of -Wcast-function-type, this will
still produce a warning if the supplied function is seriously
incompatible with the required signature, without going as far as
the official spec restriction does.

This method fixes the problem without any need for source code changes
outside nodeFuncs.h/.c.  However, it is an ABI break because the
physically called functions now have names ending in "_impl".  Hence
we can only fix it this way in HEAD.  In the back branches, we'll have
to settle for disabling -Wdeprecated-non-prototype.

Discussion: https://postgr.es/m/CA+hUKGKpHPDTv67Y+s6yiC8KH5OXeDg6a-twWo_xznKTcG0kSA@mail.gmail.com

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[54409a71a9...](https://github.com/treckstar/yolo-octo-hipster/commit/54409a71a94d077356099586f3044f9c74b99567)
#### Monday 2022-10-10 08:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [lokesh-katari/all-new-programs](https://github.com/lokesh-katari/all-new-programs)@[030f20c01f...](https://github.com/lokesh-katari/all-new-programs/commit/030f20c01f8d86303cad9a9a7c46fda7d653bebc)
#### Monday 2022-10-10 08:41:17 by technicalreju

Guess the word.py

Problem Statement – Kochouseph Chittilappilly went to Dhruv Zplanet , a gaming space, with his friends and played a game called “Guess the Word”.
Rules of games are –

Computer displays some strings on the screen and the player should pick one string / word if this word matches with the random word that the computer picks then the player is declared as Winner.
Kochouseph Chittilappilly’s friends played the game and no one won the game. This is Kochouseph Chittilappilly’s turn to play and he decided to must win the game.
What he observed from his friend’s game is that the computer is picking up the string whose length is odd and also that should be maximum. Due to system failure computers sometimes cannot generate odd length words. In such cases you will lose the game anyways and it displays “better luck next time”. He needs your help. Check below cases for better understand
Sample input :
5 → number of strings
Hello Good morning Welcome you
Sample output :
morning

Explanation:

Hello → 5
Good → 4
Morning → 7
Welcome → 7
You → 3
First word that is picked by computer is morning

Sample input 2 :
3
Go to hell

Sample output 2:
Better luck next time

Explanation:
Here no word with odd length so computer confuses and gives better luck next time

---
## [OrionTheFox/Skyrat-tg](https://github.com/OrionTheFox/Skyrat-tg)@[967de5fb00...](https://github.com/OrionTheFox/Skyrat-tg/commit/967de5fb00613b8004ccfeea93a399799d99191e)
#### Monday 2022-10-10 08:59:14 by SkyratBot

[MIRROR] Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks [MDB IGNORE] (#16716)

* Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks (#70357)

Removed the minimum amount of mannitol required to pour it since limiting this made barely any sense in the first place. Why oh why must we coders implement useless restrictions? (Useless restrictions caused the decay bug anyways.)

Brains no longer care about whether or not they're fully decayed when checking if they can be healed by pouring mannitol on them. They instead check if they're damaged at all and if they are, they'll let you pour mannitol on them.

The amount of time it takes to pour mannitol onto a brain is now 3 seconds instead of 6 seconds as it was way too slow. (Especially since something like a surgery step takes less time than 6 seconds.)

The solution is now only partially consumed as well, meaning if you need 20u of mannitol to fix a brain and you have a mixture of 40u of mannitol and 40u of mercury for example, pouring it will consume 40u of the mixture since you can't magically separate out the mannitol. This is rounded up, by the way. (Before this it simply consumed all of the mannitol, somehow you apparently can't stop pouring even while slowly pouring, according to the text.)

I've also very slightly increased the consistency of the pouring messages.

Fixes #70355

* Brains can now be healed with mannitol without being fully decayed among other quality of life tweaks

Co-authored-by: RikuTheKiller <88713943+RikuTheKiller@users.noreply.github.com>

---
## [jorgegorka/factorial-dotfiles](https://github.com/jorgegorka/factorial-dotfiles)@[277b8a2c09...](https://github.com/jorgegorka/factorial-dotfiles/commit/277b8a2c0904e13000f5a6ea713bd92d2f32fb48)
#### Monday 2022-10-10 09:42:44 by Pau Ramon Revilla

Disable snippets (#16)

This one is controversial and I will understand if you don't want to
merge it (I will branch if that's the case).

I hate snippets. I never use them and they get in my way. Maybe they are
wrongly configured, but the amount of times that I get snippets when I
don't want them is just a waste of time.

Examples:
  - Sometimes I want to move from `{}` to `do/end` and when I place the
    cursor on `{` and type `do<Enter>` I automatically get an annoying
    `end` that I have to delete imediately.
  - Sometimes I want to press `<Enter>` after a `{` and it will add
    ruby block parameters for no reason.

Do you use them? How do you workaround things getting in the middle when
you don't want them? It screws up my muscle memory.

---
## [alfael/alfkern_msm8953_tissot](https://github.com/alfael/alfkern_msm8953_tissot)@[377dcadb7c...](https://github.com/alfael/alfkern_msm8953_tissot/commit/377dcadb7c2717b4c50a4f4b27a19fd90fcfb978)
#### Monday 2022-10-10 10:04:45 by Angelo G. Del Regno

Merge: Performance improvements.

This patchset brings some performance improvements and the addition of the LZO-RLE
algorithm to the kernel, also usable in zram (yup, tested, works but LZ4 is still ok for us).

The main performance improvement is for SWAP space: the locking has changed and
the swap cache is now split in 64MB trunks.
This gives us a reduction of the median page fault latency of 375%, from 15uS to 4uS,
and an improvement of 192% on the swap throughput (this includes "virtual" swap
devices, like zRAM!). The real world user experience improvement of this on a mobile
device is seen after a day or two of usage, where it usually starts losing just a little
performance due to the large amount of apps kept open in background: now I cannot
notice any more performance loss and the user experience is now basically the same as
if the phone was in its first 2 hours of boot life.

Other performance improvements include, in short:

    UDP v4/v6: 10% more performance on single RX queue
    Userspace applications will be faster when checking running time of threads
    2-5% improvements on heavy multipliers (yeah, not a lot, but was totally free...)
    Improvements on rare conditions during sparsetruncate of about 0.3% to a
    way more rare around 20% improvement (that's never gonna happen, but there
    is no performance drop anywhere).

Tested on SoMC Tama Akatsuki RoW

This was taken from
Repo:
https://github.com/sonyxperiadev/kernel
PR: 2039 ([2.3.2.r1.4] Performance improvements)

Signed-off-by: TogoFire <italomellopereira@gmail.com>

---
## [MaboroshiChan/lighthouse](https://github.com/MaboroshiChan/lighthouse)@[66eca1a882...](https://github.com/MaboroshiChan/lighthouse/commit/66eca1a88218462235cb76a116dc3c6a1853444f)
#### Monday 2022-10-10 11:38:22 by Michael Sproul

Refactor op pool for speed and correctness (#3312)

## Proposed Changes

This PR has two aims: to speed up attestation packing in the op pool, and to fix bugs in the verification of attester slashings, proposer slashings and voluntary exits. The changes are bundled into a single database schema upgrade (v12).

Attestation packing is sped up by removing several inefficiencies: 

- No more recalculation of `attesting_indices` during packing.
- No (unnecessary) examination of the `ParticipationFlags`: a bitfield suffices. See `RewardCache`.
- No re-checking of attestation validity during packing: the `AttestationMap` provides attestations which are "correct by construction" (I have checked this using Hydra).
- No SSZ re-serialization for the clunky `AttestationId` type (it can be removed in a future release).

So far the speed-up seems to be roughly 2-10x, from 500ms down to 50-100ms.

Verification of attester slashings, proposer slashings and voluntary exits is fixed by:

- Tracking the `ForkVersion`s that were used to verify each message inside the `SigVerifiedOp`. This allows us to quickly re-verify that they match the head state's opinion of what the `ForkVersion` should be at the epoch(s) relevant to the message.
- Storing the `SigVerifiedOp` on disk rather than the raw operation. This allows us to continue track the fork versions after a reboot.

This is mostly contained in this commit 52bb1840ae5c4356a8fc3a51e5df23ed65ed2c7f.

## Additional Info

The schema upgrade uses the justified state to re-verify attestations and compute `attesting_indices` for them. It will drop any attestations that fail to verify, by the logic that attestations are most valuable in the few slots after they're observed, and are probably stale and useless by the time a node restarts. Exits and proposer slashings and similarly re-verified to obtain `SigVerifiedOp`s.

This PR contains a runtime killswitch `--paranoid-block-proposal` which opts out of all the optimisations in favour of closely verifying every included message. Although I'm quite sure that the optimisations are correct this flag could be useful in the event of an unforeseen emergency.

Finally, you might notice that the `RewardCache` appears quite useless in its current form because it is only updated on the hot-path immediately before proposal. My hope is that in future we can shift calls to `RewardCache::update` into the background, e.g. while performing the state advance. It is also forward-looking to `tree-states` compatibility, where iterating and indexing `state.{previous,current}_epoch_participation` is expensive and needs to be minimised.

---
## [TheBlueSavior/Project-Malice](https://github.com/TheBlueSavior/Project-Malice)@[a7bdc83f0c...](https://github.com/TheBlueSavior/Project-Malice/commit/a7bdc83f0cb80df50df9a1cb205a82a10478f0bd)
#### Monday 2022-10-10 12:47:53 by VNero

LOTS of shit (mostly behavior changes)

- Lesser enemies can now wait to unleash their special/heavy attacks when you aren't
  in their line of sight. Enemies that are given this behavior are listed below;
 > Rapid-Fire Trooper
 > Zombie Trooper
 > Nailgunner
 > Charred
 > Feral Imp
- Wicked's attacks revamped. More dodging, less reaction timing.
- Changed Demon Tech Spectre behavior a bit. It'll try to shut itself up now when
  pursuing you. Enjoy.
- Skeletons don't have their funny punching sound anymore. RIP :(
- Decayed Shotgunners are able to ambush you behind cover if they roll out of sight.
- Fallen Shotgunners have a more aggressive attack mode.
- Added afterimages to Nailgunner projectiles. Easier to spot them that way.
- Added XDeath for Tainted and Decayed Commando.
- Made Beholder's Rush attack its go-to melee attack. Don't worry, it's also nerfed.
- Slightly nerfed Phase Caco's dodge chance.
- Made Wretched's projectiles less static. As in, they're a bit more nicer to look at.
- Renamed model textures to avoid conflicts.
- Reused DTechBruteAttackMelee, finally.
- Fixed some sound issues.
- Missing Raise states added for some enemies.
- Corrected size inconsistencies for some afterimage trails.
- Renamed SMOK >> X111 and changed text files accordingly. Finally!
- Began work on improved sight behavior, starting with the zombies..
  - ..nevermind, it's the entire earlygame roster.
- Fixed *some* issues on startup.

---
## [tbg/cockroach](https://github.com/tbg/cockroach)@[5971b52cfb...](https://github.com/tbg/cockroach/commit/5971b52cfb7d4db76ec535991fb922dd14031679)
#### Monday 2022-10-10 13:22:32 by Tobias Grieger

rpc: re-work connection maintenance

This commit simplifies the `rpc` package.

The main aim is to make the code and the logging it produces somewhat
clearer and to pave the way for an ultimate merging of `nodedialer` with
`rpc` as well as adoption of the `util/circuit` package (async-based
circuit breaker).

`rpc.Context` hadn't aged well. Back in the day, it was a connection
pool that held on to connections even when they failed. The heartbeat
loop would run forever and its latest outcome would reflect the health
of the connection. We relied on gRPC to reconnect the transport as
necessary.

At some point we realized that leaving the connection management to
gRPC could cause correctness issues. For example, if a node is de-
commissioned and brought up again, gRPC might reconnect to it but
now we have a connection that claims to be for node X but is actually
for node Y. Similarly, we want to be able to vet that the remote
node's cluster version is compatible with ours before letting any
messages cross the connection.

To achieve this, we added `onlyOnceDialer` - a dialer that fails
all but the first attempt to actually connect, and in particular
from that point on connections were never long lived once they
hit a failure state.

Still, the code and testing around the heartbeat loop continued
to nurture this illusion. I found that quite unappealing as it
was sure to throw off whoever would ultimately work on this code.

So, while my original impetus was to produce better log messages
from `rpc.Context` when there were connection issues, I took
the opportunity to simplify the architecture of the code to
reflect what it actually does.

In doing so, a few heartbeat-related metrics were removed, as they made
limited sense in a world where failing connections get torn down (i.e.
our world).

Connection state logging is now a lot nicer. Previously, one would very
frequently see the onlyOnceDialer's error "cannot reuse client
connection" which, if one is not familar with the concept of the
onlyOnceDialer is completely opaque, and for those few in the know is an
unhelpful error - you wanted the error that occurred during dialing.

I paid special attention to the "failfast" behavior. If connections
don't stay in the pool when they are unhealthy, what prevents us from
dialing down nodes in a tight loop? I realized that we got lucky with
our use of onlyOnceDialer because it would always prompt gRPC to do
one retry, and at a 1s backoff. So, the connection would stay in the
pool for at least a second, meaning that this was the maximum frequency
at which we'd try to connect to a down node.

My cleanups to onlyOnceDialer in pursuit of better logging elimitated
this (desirable) property. Instead we now skip the log messages should
they become too frequent. I claim that this is acceptable for now since
the vast majority of callers go through a `node.Diaelr`, which has a
circuit breaker (letting callers through at most once per second).

We previously configured gRPC with a 20s dial timeout. That means that
if a remote is unreachable, we'd spend 20s just trying to dial it,
possibly tying up callers that could be trying a reachable node in the
meantime. That seemed wildly too large; I am reducing it to 5s here
which is still generous (but there's a TLS handshake in here so better
not make it too tight).

We previously tried to re-use connections that were keyed with a NodeID
for dial attempts that didn't provide a NodeID. This caused some issues
over the years and was now removed; the extra RPC connections are
unlikely to cause any issues.

The internal connection map is now a plain map with an RWMutex. This is
just easier and gets the job done. The code has simplified as a result
and it's clearer that it's correct (which it repeatedly was not in the
past).

I implemented redactability for gRPC's `status.Status`-style errors,
so they format nicer and at least we get to see the error code (the
error message is already flattened when gRPC hands us the error,
sadly).

There are various other improvements to errors and formatting. The
following are excerpts from the health channel when shutting down
another node in a local cluster:

Connection is first established:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 3  connection is now ready

n1 goes down, i.e. existing connection is interrupted (this error comes
from `onlyOnceDialer`):

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 35  closing
connection after: ‹rpc error: code = Unavailable desc = connection
error: desc = "transport: Error while dialing connection interrupted
(did the remote node shut down or are there networking issues?)"›

Reconnection attempts; these logs are spaced 1-2s apart:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 37  unable to
connect (is the peer up and reachable?): initial connection heartbeat
failed: ‹rpc error: code = Unavailable desc = connection error: desc =
"transport: Error while dialing dial tcp 127.0.0.1:26257: connect:
connection refused"›

n3 is back up:

> [n3,rnode=1,raddr=‹127.0.0.1:26257›,class=system,rpc] 49  connection is now ready

There are other connection errors in the logs that stem from operations
checking for a healthy connection, failing to get through circuit
breakers, etc., such as these:

> [n3,intExec=‹claim-jobs›,range-lookup=/Table/15/4/‹NULL›] 33  unable
to connect to n1: failed to check for ready connection to n1 at
‹127.0.0.1:26257›: ‹connection not ready: TRANSIENT_FAILURE›

Release note (general change): Previously, CockroachDB employed a 20s
connection timeout for cluster-internal connections between nodes.  This
has been reduced to 5s to potentially reduce the impact of network
issues.

---
## [psych10/psych10.github.io](https://github.com/psych10/psych10.github.io)@[16959e3436...](https://github.com/psych10/psych10.github.io/commit/16959e343674e4e5d147716a35698a2b4c0bc5f7)
#### Monday 2022-10-10 14:15:32 by davdrose

Update index.md

Do most people develop this from taking the course? - *Statistical curiosity*: The interest in further developing statistical skills and knowledge, and the confidence in the ability to do so

For the quiz section you wrote: Short answer questions will be graded in the week following the due date, and students will be given an opportunity to revise any answers that are not considered sufficient.  Is this something we allowed last year? Also, it seems that it conflicts a bit with this: In some cases the quizzes may include short answer questions; for these questions, credit will be obtained by making a good faith effort to answer the question, even if the answer is factually incorrect. If we accept answers that are factually incorrect, though display a good faith effort, what would they correct? Would we allow them to correct and resubmit factually incorrect answers where there was no good faith effort made? Or was there something else you had in mind here?

I wonder if this might open the door to a lot of people reporting not feeling well enough to come to section or class: This might include the possibility that you, your peers, or we, the teaching team, wake up one morning not feeling too well, or might need to quarantine or isolate for the safety of everyone. In light of these considerations, we request that you: - skip class/lab/section if you’re feeling unwell and notify the teaching team immediately

I'm not entirely sure what to do about it and maybe it won't even be an issue. But one thought is that we give everyone one or two free passes to miss class and not have it affect attendance. If they miss beyond that we will need documentation (such as evidence that they visited the doctors office).

---
## [TwinUsers/solanum](https://github.com/TwinUsers/solanum)@[06c5309534...](https://github.com/TwinUsers/solanum/commit/06c53095343c2756208f6398bb7e00fb2cbe46dd)
#### Monday 2022-10-10 14:25:46 by Ed Kellett

m_sasl: Remove implicit abort on registration

This doesn't make sense in a world where post-registration SASL is
allowed, and should fix one case of an annoying login desync that's seen
in the real world.

Specifically, when a client sends its final AUTHENTICATE and Atheme
receives it, it sends an SVSLOGIN for that client. If the client sends
us its CAP END *before* we see the SVSLOGIN, the implicit abort will try
to abort the SASL session that's already succeeded.

Atheme interprets this as an instruction to forget about the successful
SASL session; you'll connect unidentified. But it's already sent
SVSLOGIN, which will log the client in ircd-side, causing ircd and
services views to differ until the user authenticates again manually.

I think allowing a SASL session to be aborted when it has already
succeeded is an Atheme bug, and it can still be triggered without this
change. But our behaviour here seems silly anyway.

---
## [Pusheon/Mewdeko](https://github.com/Pusheon/Mewdeko)@[14ef9df323...](https://github.com/Pusheon/Mewdeko/commit/14ef9df3239aad1ec298c5e7997578eb7de2e36a)
#### Monday 2022-10-10 15:11:19 by Pusheon

Starting with the next update, Public Mewdeko will no longer have support for streaming youtube music. Fuck you discord. https://youtu.be/fOpEdS3JVYQ

---
## [Financial-Times/n-express](https://github.com/Financial-Times/n-express)@[d36f98961e...](https://github.com/Financial-Times/n-express/commit/d36f98961eaf49164c99d099415e7604dccda7df)
#### Monday 2022-10-10 15:26:47 by Rowan Manning

Add a withSentry option to allow disabling n-raven

This option is the first step towards us being able to provide an
alternative for Sentry, or at least unpick our Sentry implementation
from n-express. This is needed for us to even properly experiment in
this space, we'd like to be able to trial disabling Sentry on some of
our low-traffic internal apps (e.g. Houston) and it's currently not
possible at all.

Notes on my choices:

  - Because importing the n-raven module has side-effects (i.e. just
    requiring it will register uncaught exception handlers), we had to
    move the `require` statements into conditionals within the n-express
    setup code. This is a little ugly. We could possibly abstract this
    into a new file within n-express if you really hate this.

  - I opted for a `withSentry` option defaulting to `true` as this is
    consistent with the other n-express options.

  - In production, the default error handler outputs the Sentry error ID
    if it's enabled and we no longer have that data if the `withSentry`
    option is `true`. I decided a reasonable alternative which doesn't
    give away any important error information would be to send the
    status code and status message associated with the error.

  - For now (at the request of Joel) I added a warning message if you
    set the `withSentry` option to `false`. This is to highlight that
    it's still an experimental option and so that we in the Reliability
    team can keep track of any apps which have disabled Sentry
    prematurely.

---
## [noreiller/next.js](https://github.com/noreiller/next.js)@[1bbd264216...](https://github.com/noreiller/next.js/commit/1bbd2642164098ceb9cebfb36deba9aed7e8a53b)
#### Monday 2022-10-10 15:52:40 by abdennor

Add additional fix in hydration error document (#40675)

I had the same issue, so the fix that worked for me was pulled from this
thread https://stackoverflow.com/a/71870995

I have been experiencing the same problem lately with NextJS and i am
not sure if my observations are applicable to other libraries. I had
been wrapping my components with an improper tag that is, NextJS is not
comfortable having a p tag wrapping your divs, sections etc so it will
yell "Hydration failed because the initial UI does not match what was
rendered on the server". So I solved this problem by examining how my
elements were wrapping each other. With material UI you would need to be
cautious for example if you use a Typography component as a wrapper, the
default value of the component prop is "p" so you will experience the
error if you don't change the component value to something semantic. So
in my own opinion based on my personal experience the problem is caused
by improper arrangement of html elements and to solve the problem in the
context of NextJS one will have to reevaluate how they are arranging
their html element

<!--
Thanks for opening a PR! Your contribution is much appreciated.
To make sure your PR is handled as smoothly as possible we request that
you follow the checklist sections below.
Choose the right checklist for the change that you're making:
-->


## Documentation / Examples

- [x] Make sure the linting passes by running `pnpm lint`
- [ ] The "examples guidelines" are followed from [our contributing
doc](https://github.com/vercel/next.js/blob/canary/contributing/examples/adding-examples.md)

Co-authored-by: JJ Kasper <jj@jjsweb.site>

---
## [flyingfishfuse/rawr_auto_cat_feederz_uWu](https://github.com/flyingfishfuse/rawr_auto_cat_feederz_uWu)@[53046296b2...](https://github.com/flyingfishfuse/rawr_auto_cat_feederz_uWu/commit/53046296b22f497baa61b33c921ab3884710b6b1)
#### Monday 2022-10-10 15:55:20 by flyingfishfusealt

removed uint8_t stuff, focusing on single cat

I split the uint32_t / uint8_t conversion stuff off into a test file for later modification. I want to have a cat registry to allow more than one animal to use the feeder but I am NOT good at C/C++ yet and I cant focus because ADHD/autism stuff so I kinda suck at thinking right now. Getting the physical aspect built in the meanwhile. Working on power supply now, using dual 18650 batteries and two TP4056 running parallel from 5V input.

Taking suggestions on alternative modules, HAHA nobody even visits my github. fuckers. I was told simply having projects would have recruiters jumping at my heels if I wrote good enough but the good shit is hidden because of a shithead in a hacker community I was previously moderating acting SUPER dangerous towards me so I cant even fucking show the good shit. I hate most of you humans. The smart ones wont have anything to do with me because I refuse to constantly prove myself  to new people, and the stupid ones are too dangerous to even associate with.

I am just going to go into business for myself, assuming I can raise the capital to start a server cluster. Any donors?

---
## [Chris-plus-alphanumericgibberish/dNAO](https://github.com/Chris-plus-alphanumericgibberish/dNAO)@[f260cde5a4...](https://github.com/Chris-plus-alphanumericgibberish/dNAO/commit/f260cde5a426d936bca18ebbc6a22ee051cbd96d)
#### Monday 2022-10-10 16:27:16 by chris

Monster healing fixes

Make one mhp > mhpmax check at end
-Fixes overhealing bug

Re-order mspec cooldown and digestion to start instead of end
-Fixes a bug where Lomya wouldn't get counted in degeneration cases.
-Reduces redundancy in special cases
-Does mean that if a monster dies from degeneration its cooldowns will still have ticked. This seems fine to me.

Switch some cases of == 0 to <= 0
-I don't think this could cause a bug, but better safe than sorry.

Re-order cases so that it goes magic healing->damaging effects->degeneration->natural effects.
-Degeneration was blocking Lolth's clouds and Cthulhu's mind blasts.
-Degeneration is defined as blocking natural healing
--Only one Degen case will take effect, due to early returns. Perhaps this should be considered a bug?

---
## [dnmihnea/JavaPlatformer](https://github.com/dnmihnea/JavaPlatformer)@[3eb8720802...](https://github.com/dnmihnea/JavaPlatformer/commit/3eb8720802dcedc96a3edbc37d3de838b195883d)
#### Monday 2022-10-10 16:46:33 by dnmihnea

Revert "go fuck yourself"

This reverts commit 39cd13ade7a3c496c7b720f1a97fe88cddee7bf0.

---
## [Tiktodz/android_kernel_asus_sdm636](https://github.com/Tiktodz/android_kernel_asus_sdm636)@[8993bc46ae...](https://github.com/Tiktodz/android_kernel_asus_sdm636/commit/8993bc46aef1b47f2bb5bdb7068534b9fa3225cc)
#### Monday 2022-10-10 17:35:41 by George Spelvin

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
Signed-off-by: Dede Dindin Qudsy <xtrymind@gmail.com>
Signed-off-by: Vaisakh Murali <vaisakhmurali@gmail.com>
Signed-off-by: Tiktodz <ewprjkt@proton.me>

---
## [pri0818/falcon_kernel_realme_sm7125](https://github.com/pri0818/falcon_kernel_realme_sm7125)@[ab52ec9fbb...](https://github.com/pri0818/falcon_kernel_realme_sm7125/commit/ab52ec9fbbfcc3e85a63e95314a5cb31b14f48d7)
#### Monday 2022-10-10 17:46:30 by Peter Zijlstra

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
Signed-off-by: pri0818 <priyanshusinghal0818@gmail.com>

---
## [Koshenko/mojave-sun-13](https://github.com/Koshenko/mojave-sun-13)@[736422fac8...](https://github.com/Koshenko/mojave-sun-13/commit/736422fac8d84c8e054853fd2b205cc993250c21)
#### Monday 2022-10-10 18:47:35 by Technobug14

Field Transfusions & Fixes Sprites/Runtime (#2152)

* Working field transfusions

As far as I can tell, no runtimes or bugs. Should be good to go. Could maybe do with some polish? But otherwise it works great.

* Fixes energy weapon bugs

Fixes a runtime related to emptying cells from energy weapons, and fixes an overlay bug and inventory icon bug on the cells themselves.

* Bug fixes

read above, fixes a few bugs/errors

* Broken as hell

Supposed to add new IV bag sprites and overlays that would change as the bag gets emptier. Multiple bugs both with transfusion and the icon/overlay. Right now, the icon currently disappears once the object is on the ground and I can't tell why. Secondly, the overlay has the visual bugs and could probably do with a more thorough system to apply it? The bugs on transfusion are mostly due to a lack of sanity checks, where it will continue to be attached to someone from many tiles away when thrown/dropped, etc.

* Shit

HATE HATE HATE this sucks and it is buggy as hell

* Fix icon/overlay updates

* Mostly working

Still some broken stuff, you can attach IV bags if you're not next to someone and do it from inside containers, also fixes the world states for the police and military 10mm pistol

* Finishing touches

Couple of bug fixes, fixes 10mm police/military world sprite, etc etc. Should be good to go.

Co-authored-by: Koshenko <koshenko@pm.me>
Co-authored-by: Koshenko <53068134+Koshenko@users.noreply.github.com>

---
## [gsteel/mezzio-router](https://github.com/gsteel/mezzio-router)@[487db7288e...](https://github.com/gsteel/mezzio-router/commit/487db7288eb06620d54bf4fbe13544ae834f55f5)
#### Monday 2022-10-10 19:14:09 by Michał Bundyra

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
## [Fis-Ura/Narikiri-Dungeon-X](https://github.com/Fis-Ura/Narikiri-Dungeon-X)@[9958395c24...](https://github.com/Fis-Ura/Narikiri-Dungeon-X/commit/9958395c24f78b377b09c311af269ea29211b192)
#### Monday 2022-10-10 19:36:31 by FistingUranus

Npc Name Mass Replace

小さな妖精 = Little Fairy
アルベルト = Alberto
翼を持つ女性 = Winged Woman
ノルン = Norn
<DIO> = <DIO>
<MEL> = <MEL>
エトス = Ethos
少年の声 = Kid
空からの訪問者 = Thing From The Sky
好奇心旺盛の商人 = Surprised Clerk
黄色い悲鳴の女性 = Wealthy Woman
仮面の男 = Masked Guy
浅緑の生き物 = Green Colored Thing
買い物途中の女性 = Glaring Woman
恰幅のいい商人 = Old Man
怯える子ども = Terrified Kid
通りすがりの魔術師 = Travelling Magic Scientist
謎の声 = Weird Voice
魔女の声 = Magician's Voice
<KUL> = <KUL>
ピンク色の魔女 = Pink Hair Magician
<ARC> = <ARC>
酔っ払いの声 = Drunk Man's Voice
酔っ払い = Drunk Man
<KLA> = <KLA>
エルフの青年 = Young Elf
仮面の女 = Masked Girl
イフリート = Efreet
傷だらけの女性 = Injured Woman
<DIO>＆<MEL> = <DIO> & <MEL>
ミラルド = Milard
泣きじゃくる子ども = Sobbing Kid
バジル = Basil
女性の声？ = Girl's Voice?
紺青の女性 = Silver Haired Girl
<RND> = <RND>
兵士 = Knight
<CST> = <CST>
<CLE> = <CLE>
<MIN> = <MIN>
<SUZ> = <SUZ>

---
## [CrystalChun/assisted-service](https://github.com/CrystalChun/assisted-service)@[564650feca...](https://github.com/CrystalChun/assisted-service/commit/564650feca372064314282d98d6fd9c6ee69bd2c)
#### Monday 2022-10-10 20:06:12 by Omer Tuchfeld

MGMT-10973: Enable DNS validations if coredns or keepalived static pod manifests in day-2 connectivity-check ignition (#4072)

For context, this is a service-side follow-up to:

https://github.com/openshift/assisted-installer-agent/pull/388

and also this small agent fix https://github.com/openshift/assisted-installer-agent/pull/403

# Goal

During day-2 installations, we want the service to optionally perform
DNS validations when the worker attempts to join none-platform clusters.

# Issue

When the cluster is imported via our `.../v2/clusters/import` endpoint,
we have no way to know whether that cluster is a none-platform cluster
or cluster with managed networking (e.g. baremetal), so we have no way
to know whether we should perform the DNS validation or not. We wouldn't
like to have that validation on all the time, because it's unnecessarily
annoying for clusters with managed networking.

# Background

As part of our existing API connectivity-check, the service asks the
agent to download the worker.ign file from the to-be-joined-cluster's
machine-config-server, then send that back to the service.

# Solution

The contents of that file include information that will allow the
service to make an educated guess about whether the ignition originated
from a cluster with managed networking or not.

Also, a new "imported" column has been added to clusters, to indicate
whether they were created through a conversion or through being
imported. This is important because the solution should only be
applied for imported clusters, and this will provide a good way
to tell apart imported from non-imported clusters.

Also, when a user imports a cluster, we will inspect the `params.NewImportClusterParams.APIVipDnsname`
parameter and extract:

- The cluster name
- The cluster base domain

The cluster name will override the name given in `params.NewImportClusterParams.Name`,
see diff comment for more information on why.

The cluster base domain will be used to set the `BaseDNSDomain` of the
cluster, because up until now we didn't set it for imported cluster.

The reason `BaseDNSDomain` and `Name` have to be correctly set is
because the DNS validations use them to construct the domain names
that are being validated.

Also updated some validation messages for the API connectivity check and
DNS validations.

Also, the clusterdeployments_controller can now import SNO clusters,
it was an oversight that should have been done as part of 4cda26533d377f453f68783e8b2eae438734555d (#3404)

# Ignition Files

The ignition files we currently look at are:

```
/etc/kubernetes/manifests/coredns.yaml
/etc/kubernetes/manifests/keepalived.yaml
```

This is a hack - since we have no official way to know whether a worker
ignition file originated from a cluster with managed networking or not,
we instead rely on the presence of coredns and keepalived pod manifests
to indicate that. We only expect those to be present in clusters with
managed networking. To be a bit more robust, the service will consider
the presence of any one of them to mean that the cluster has managed
networking. This gives us better forwards compatibility if one of them
gets renamed / replaced with other technologies in future OCP versions.

Another way in which this is hacky is that users could manually create
static pods with the same name as part of their machine-configs, in
which case we would have a false-positive detection. But that is
admittedly very unlikely.

Hopefully we can negotiate with the relevant OCP teams to have a more
official, stable way to have this detection - like a magic empty file
placed somewhere in the ignition that we can check for the presence of.
Once we have such file, we can slowly deprecate this detection mechanism
and fully move to the new one by inspecting that file instead.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[c5281b5372...](https://github.com/treckstar/yolo-octo-hipster/commit/c5281b5372ce88b0a16a4faaa2fac7ffea344066)
#### Monday 2022-10-10 21:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[fcf0ed2580...](https://github.com/k21971/EvilHack/commit/fcf0ed2580833b126b9d6206f14a04ee95d8af0d)
#### Monday 2022-10-10 21:36:54 by k21971

Lucifer tweaks.

It was pointed out that Lucifer in his initial configuration makes it
virtually impossible for a player to attempt the pacifist conduct. No
monster would ever be of a high enough level to want to attack him, and
even if they did (conflict) they'd never land a hit. Since defeating
Lucifer is required to progress and subsequently win, some changes were
in order.

* Lower Lucifer's default base level and base AC
* Grudge condition set up - if you have a pet, they will attack him
* In the off-chance you encounter Lucifer before obtaining the Amulet of
Yendor, prevent him from warping to the upstairs (as far as I can tell,
this scenario can never happen, but we'll cover our ass here)
* Change Lucifer's size from large to huge
* Give Lucifer a morning star as a weapon. Get it... ?

Lucifer is still the strongest and toughest of all the demon bosses.
Between his max hit points and damage output, you'll still need to come
prepared for a serious fight. Pacifists have a fighting chance now.

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[7f6ff5468b...](https://github.com/ammarfaizi2/linux-fork/commit/7f6ff5468b495c720b90c515dd9802a6de1b62dd)
#### Monday 2022-10-10 21:51:08 by Johannes Weiner

mm: vmscan: fix extreme overreclaim and swap floods

During proactive reclaim, we sometimes observe severe overreclaim, with
several thousand times more pages reclaimed than requested.

This trace was obtained from shrink_lruvec() during such an instance:

    prio:0 anon_cost:1141521 file_cost:7767
    nr_reclaimed:4387406 nr_to_reclaim:1047 (or_factor:4190)
    nr=[7161123 345 578 1111]

While he reclaimer requested 4M, vmscan reclaimed close to 16G, most of it
by swapping.  These requests take over a minute, during which the write()
to memory.reclaim is unkillably stuck inside the kernel.

Digging into the source, this is caused by the proportional reclaim
bailout logic.  This code tries to resolve a fundamental conflict: to
reclaim roughly what was requested, while also aging all LRUs fairly and
in accordance to their size, swappiness, refault rates etc.  The way it
attempts fairness is that once the reclaim goal has been reached, it stops
scanning the LRUs with the smaller remaining scan targets, and adjusts the
remainder of the bigger LRUs according to how much of the smaller LRUs was
scanned.  It then finishes scanning that remainder regardless of the
reclaim goal.

This works fine if priority levels are low and the LRU lists are
comparable in size.  However, in this instance, the cgroup that is
targeted by proactive reclaim has almost no files left - they've already
been squeezed out by proactive reclaim earlier - and the remaining anon
pages are hot.  Anon rotations cause the priority level to drop to 0,
which results in reclaim targeting all of anon (a lot) and all of file
(almost nothing).  By the time reclaim decides to bail, it has scanned
most or all of the file target, and therefor must also scan most or all of
the enormous anon target.  This target is thousands of times larger than
the reclaim goal, thus causing the overreclaim.

The bailout code hasn't changed in years, why is this failing now?  The
most likely explanations are two other recent changes in anon reclaim:

1. Before the series starting with commit 5df741963d52 ("mm: fix LRU
   balancing effect of new transparent huge pages"), the VM was
   overall relatively reluctant to swap at all, even if swap was
   configured. This means the LRU balancing code didn't come into play
   as often as it does now, and mostly in high pressure situations
   where pronounced swap activity wouldn't be as surprising.

2. For historic reasons, shrink_lruvec() loops on the scan targets of
   all LRU lists except the active anon one, meaning it would bail if
   the only remaining pages to scan were active anon - even if there
   were a lot of them.

   Before the series starting with commit ccc5dc67340c ("mm/vmscan:
   make active/inactive ratio as 1:1 for anon lru"), most anon pages
   would live on the active LRU; the inactive one would contain only a
   handful of preselected reclaim candidates. After the series, anon
   gets aged similarly to file, and the inactive list is the default
   for new anon pages as well, making it often the much bigger list.

   As a result, the VM is now more likely to actually finish large
   anon targets than before.

Change the code such that only one SWAP_CLUSTER_MAX-sized nudge toward the
larger LRU lists is made before bailing out on a met reclaim goal.

This fixes the extreme overreclaim problem.

Fairness is more subtle and harder to evaluate.  No obvious misbehavior
was observed on the test workload, in any case.  Conceptually, fairness
should primarily be a cumulative effect from regular, lower priority
scans.  Once the VM is in trouble and needs to escalate scan targets to
make forward progress, fairness needs to take a backseat.  This is also
acknowledged by the myriad exceptions in get_scan_count().  This patch
makes fairness decrease gradually, as it keeps fairness work static over
increasing priority levels with growing scan targets.  This should make
more sense - although we may have to re-visit the exact values.

Link: https://lkml.kernel.org/r/20220802162811.39216-1-hannes@cmpxchg.org
Signed-off-by: Johannes Weiner <hannes@cmpxchg.org>
Reviewed-by: Rik van Riel <riel@surriel.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Joonsoo Kim <iamjoonsoo.kim@lge.com>
Cc: <stable@vger.kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [ctm/diet](https://github.com/ctm/diet)@[8997c2b44b...](https://github.com/ctm/diet/commit/8997c2b44bc20c39e70ae58992fd56a70fc8c850)
#### Monday 2022-10-10 21:52:06 by Clifford T. Matthews

Includes up through afternoon snack.

This commit includes a bunch of drinking and eating that I did during
the Balloon Fiesta and some of what I remember eating at the Feral Hog
50k.  Much of the Balloon Fiesta drinking is listed as "3 oz.?", but
those were typically 12 oz. bottles being shared with as many people
as were interested and around, which was typically more than four, so
3 oz. is probably high, but I don't want to kid myself either.  I
drank more than I had planned, in part because I wasn't driving (I ran
to the field from my house and then caught a lift back) and in part
because for Wednesday and Thursday, I thought the Feral Hog 50k was
going to be canceled.

Oh and when I drank a lot I also ate a ton of junk food.  So, I wound
up gaining about five pounds between Friday, September 30th and
Monday, October 10th, but that also included the Mt. Taylor 50k and
the Feral Hog 50k and I ate poorly at the aid stations and post-race
in part because I'm broke and it was free.  Oh and the Balloon Fiesta
beer was free too, due in part to Tom but especially Bill.  I owe them
next year.

---
## [333voidGirl/n1l.neocities.org](https://github.com/333voidGirl/n1l.neocities.org)@[662d292451...](https://github.com/333voidGirl/n1l.neocities.org/commit/662d29245177e01d0bb225361964eb346f852425)
#### Monday 2022-10-10 22:51:32 by n1l

October 10 Upd8 (Cleanup Final)

Sorry for the mess of notifs anyone got, I forgot the GitHub CLI was real for a minute and was deleting things by hand because I'm tired & dumb. Anyway, I reorganized the website's files a *lot* & made a few changes to some things. This may not be the only update for today since I want to add some comments to some files so that it's easier for others to read & learn from -& then eventually comment out every file- but I have been working on this during school all day & feel as though it is ready for a big update. Again, sorry if anyone following me got a shit ton of notifs, I am new to doing things like this. ~n1l

---
## [HippieStation/HippieMerchant-13](https://github.com/HippieStation/HippieMerchant-13)@[323c9d6bb7...](https://github.com/HippieStation/HippieMerchant-13/commit/323c9d6bb75c20e11d744dbe55850287ede8c5cc)
#### Monday 2022-10-10 22:56:40 by karmaisblackandbluepilled

bye bye is_ganymede back to the lobby

drip drip from the tap

BYE BYE NANOSUIT BACK TO THE LOBBY

remember when they tried to kill the lich king with a fucking sword made out of tortured souls lmao

honestly

liberia

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[1af2c12e05...](https://github.com/TaleStation/TaleStation/commit/1af2c12e0501c2cf5eb5946738360564fd78cea4)
#### Monday 2022-10-10 23:58:51 by TaleStationBot

[MIRROR] [MDB IGNORE] canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#2676)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE (#69790)

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

The most idiotic thing I've seen is canUseTopic's defines, they literally just define TRUE, you can use it however you want, it doesn't matter, it just means TRUE. You can mix and match the args and it will set that arg to true, despite the name.

It's so idiotic I decided to remove it, so now I can reclaim a little bit of my sanity.

* canUseTopic now uses TRUE/FALSE instead of defines that just say TRUE

* fix

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---

