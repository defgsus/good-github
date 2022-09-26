## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-09-25](docs/good-messages/2022/2022-09-25.md)


1,869,622 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,869,622 were push events containing 2,526,667 commit messages that amount to 144,625,242 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 32 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9b9337de49...](https://github.com/tgstation/tgstation/commit/9b9337de493ec62927f15b0ee18f9342cd3c2d04)
#### Sunday 2022-09-25 00:25:03 by Tim

Add speech modifier to zombie tongue (#69899)


About The Pull Request

A zombie rotten tongue has a complex language modifier.
The language modifier works by:

    All occurrences of characters "eiou" (case-insensitive) are replaced with "r".
    All characters other than "zhrgbmna .!?-" (case-insensitive) are stripped.
    Multiple spaces are replaced with a single.
    Lower-case "r" at the end of words replaced with "rh".
    An "a" or "A" by itself will be replaced with "hra".
    The first character is capitalised.

Some interesting dialogue examples:

    Bab, am gaa habbah abah zah namrh ah Bh!rh!b?
    Bob, are you happy about the death of Philip?

    Zah bang bang man ganna harm mah zambah?
    Will the Zombie Hunter attack me?

    Mah zambah nah harm brazzarz.
    I do not hurt brothers.

    Mah zambah ganna gangbang harmanz zammarrar.
    I will kill humans tomorrow.

    Mah zambah am nah habbah, an mah zambah gab, -Graaaagh!-
    I am not happy, and I say "Graaaagh!"

The language idea was taken from a zombie game back in 2005 called Urban Dead. It's no longer developed and I made all the code myself while following the given language rule structures.

Zombie Speech Translator
Zombie Language Examples
Zombie Dictionary
Why It's Good For The Game
Abracadabra - The Steve Miller Band

    Ah raab zha brahnz ahn zarh hagh, (I love the brains in your head)
    Ah ganna barg abgrah gangbang, (I'm gonna eat them when you're dead)
    Az rahnah zarh ranz ahn hahg ahahz, (Now as you run and hide away)
    Zarh harh mah zambah az hah zahz: (You hear my zombie as he says:)
    Abra-abra-gababra, (Abra-abra-cadabra)
    Ah ganna rahg arg ahn grab zarh! (I'm gonna reach out and grab ya!)
    Abra-abra-gababra, (Abra-abra-cadabra)
    Ah ganna rahg arg ahn grab zarh! (I'm gonna reach out and grab ya!)

Changelog

cl
add: Rotten zombie tongue has a new speech modifier that converts spoken language into zombie sentences. If the person speaking is a high-functioning zombie this is bypassed.
/cl

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[d34fa4c642...](https://github.com/timothymtorres/tgstation/commit/d34fa4c642839215df5ba985d098a04e4d555b5b)
#### Sunday 2022-09-25 00:45:32 by LemonInTheDark

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
## [Trigam04/Trigam-Botnet](https://github.com/Trigam04/Trigam-Botnet)@[f1888810f8...](https://github.com/Trigam04/Trigam-Botnet/commit/f1888810f87cc2f10a24ed3fdc2d2793d9ab08f4)
#### Sunday 2022-09-25 01:55:33 by Trigam

Moving calculate funcs to a different file

fuck you nerdo i'll keep the code as clean as I want

---
## [mjkelly/ansible-playbooks](https://github.com/mjkelly/ansible-playbooks)@[6deec54ce7...](https://github.com/mjkelly/ansible-playbooks/commit/6deec54ce705b745c18dca90e9790e7867120dbb)
#### Sunday 2022-09-25 02:44:53 by Michael Kelly

[lockdown] add wireguard & use iptables, not ufw

- Add wireguard, because that's what I run on my own bastion hosts. It
  requires a lot of configuration, but it's way nicer to do in ansible
  than by hand.
- Dump ufw. I hate it, and it's hard to configure in ansible. There is a
  non-core module to do it but I don't want to depend on that.

The ufw task is still in there, it's just not linked from
tasks/main.yml. I'll delete it in another update.

A big reason for doing this is that I spent so long troubleshooting my
wireguard setup. It's difficult to use a firewall that tries to abstract
you away from iptables, while most examples still use iptables commands.
(What else could they use? Nothing else is standard.) That made me
worried my ufw setup was tripping me up.

ufw was always lousy to script, anyway. OK, rant over.

---
## [atorik/postgres](https://github.com/atorik/postgres)@[1c27d16e6e...](https://github.com/atorik/postgres/commit/1c27d16e6e5c1f463bbe1e9ece88dda811235165)
#### Sunday 2022-09-25 03:15:33 by Tom Lane

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
## [derrod/obs-studio](https://github.com/derrod/obs-studio)@[b7199a6dc3...](https://github.com/derrod/obs-studio/commit/b7199a6dc3fdce670806d7bb4af631caecc6ef74)
#### Sunday 2022-09-25 03:19:03 by derrod

Well apparently if you add this *here* it'll cause a failure god fucking damn it

---
## [vulcandth/pokecrystal](https://github.com/vulcandth/pokecrystal)@[14cfc6f0fe...](https://github.com/vulcandth/pokecrystal/commit/14cfc6f0fec9f67429e17c684292ce9d8b9eb6df)
#### Sunday 2022-09-25 03:35:51 by Damien Doury

Zipcode input constraints added (#11)

* Zipcode inputs accept letters and blank.

* Added the ability to compile pokecrystal-eu.gbc ROM with "make crystal-eu"

* Input constraints done.

Notes:
- As the zipcode is saved as a list of indexes from the char pools, and as the char pools differ from one region to another, the zipcodes will be broken from one region to another. This could be fixed server-side, or by encoding/decoding the indexes into VRAM indexes (the alphabet is constant between most regions, except asian ones) when opening/leaving the Profile menu.
- The macros I created are old and ugly (rgbds 0.3.8), and should be udpated when updating RGBDS.
- My code is kinda quick and dirty, as several lists are duplicated when they could be used once. I'm thinking about the "Zipcode_CharPoolForStringIndex" arrays, which could save several dozen bytes if optimized.
- A special case case for the alignment of the AUS region codes has been made, because the string length is not constant. This doubles the "Prefectures" array, which adds 173 bytes to the rom bank.
- With that being said, we are far from running out of space in the ROM $12.

* The zipcode is now right aligned/shifted when it ends with blank characters.

---
## [VerseGroup/SchoolVerseRedesignTesting](https://github.com/VerseGroup/SchoolVerseRedesignTesting)@[f8d08e9204...](https://github.com/VerseGroup/SchoolVerseRedesignTesting/commit/f8d08e920487be749fa8ca9495de2dcdc54a688f)
#### Sunday 2022-09-25 03:56:12 by Daniel Shola-Philips

9/24/2022
 - Changed gradient of dummy app icon logo
 - Changed components to be color dynamic to support all four accent colors
 - Updated clubs page to show "Coming Soon"
 - Created stylized segmented picker for Sports and Menu pages
 - Created dummy Tasks page
      - todo: fix task tile components to have dynamic size overlay
 - Initiated "All Sports" and "My Sports" pages
 - Initiated "Breakfast", "Lunch", and "Dinner" pages

---
## [TurtleShroom/TSP_STORYTIME_RIDES_AGAIN](https://github.com/TurtleShroom/TSP_STORYTIME_RIDES_AGAIN)@[f920aea5c9...](https://github.com/TurtleShroom/TSP_STORYTIME_RIDES_AGAIN/commit/f920aea5c916788e832338bdfd9d6701a9020f06)
#### Sunday 2022-09-25 04:17:38 by TURTLESHROOM

Major

1. Fixed problem with the Base that the Dried Frog Pills and Herba Cigarillos inherited. They should no longer deliver errors.

2. Botox now makes the sound of an injection. I had no idea this was a thing until I took a peak at some of the Vanilla rendition's code.

3. The Botox High is now more realistic: the muscle paralysis has been made more severe.

4. Set Virgin Frog Nog as not a drug

5. Fire Egg Nog now gives the Flame Damage instead of the Burn Damage, meaning it can set its target on fire more often.

6. Kraken Rum is now more addictive.

7. Fixed typoes in the Werefrog Eye Part/Hediff.

8. Fixed error where Frog Meat was not accepted when one tried to make Dried Frog Pills.

9. Borpa products ( https://www.steamcommunity.com/sharedfiles/filedetails/?id=2552747112 ) count as ingredients for Dried Frog Pills because Borpas come from Pepe the Frog.

10. Dunmers can now use the Grinder to make Scuttle and Herba Cigarillos!

11. Green Ooze now tastes worse than Nutrient Paste, making Pawns less likely to chug it.

12. Fixed missing MAYREQUIRE qualifiers for Rim of Magic Mod features on the Fat Man and the Callandor Rod.

13. The Callandor Rod is not a sword, so now it doesn't look like a sword.

14. Clarified into which frog that frog eggs will hatch.

15. Worm Batta and other Batta dishes that call for meat will now always be counted as having meat, even if the game spawns them without ingredients.

16. Worm Pizza now takes longer to rot.

17. Increased the maximum stack size that Gnome Flour and Gnome Meal can stand.

18. Skeleton Marrow can now be eaten by crreatures that only eat Corpses.

19. Fixed issue where the Embittered Bullfrog had a Man Hunter Chance inputted twice, causing an error.

20. Peeled Beasts and Peeled Clowns can now breathe in space. THERE IS NO ESCAPE!

21. If you have the Cthulhu Mod, the Peeled Ones now count as Eldritch Abominations!

22. Fixed issue where butchering a Living Rock caused eleven Chunks to spawn instead of one.

23. Predators no longer try to eat Living Rocks... because they are just rocks...

24. If you have the Cthulhu Mod, then you can cure its Insanity Hediff with Dried Frog Pills! (Recipe courtesy of: https://www.steamcommunity.com/sharedfiles/filedetails/?id=2209587618  !)

25. You can cure Catatonia with huge amounts of Dried Frog Pills ! (Recipe courtesy of: https://www.steamcommunity.com/sharedfiles/filedetails/?id=2209587618 !)

26. Living Rocks can now be formed from certain Caravan Trader Tyypes from the Let's Trade Mod. ( https://www.steamcommunity.com/sharedfiles/filedetails/?id=2373633407  )

27. INCREDIBLE AND BEAUTIFUL SPIRES FOR THE HERBA CIGARILLOS.

---
## [NimuDevALTACC/FNF-PsychEngine](https://github.com/NimuDevALTACC/FNF-PsychEngine)@[c28de9b559...](https://github.com/NimuDevALTACC/FNF-PsychEngine/commit/c28de9b5593a24184aa1f4d04f00218aaf7c4552)
#### Sunday 2022-09-25 05:31:46 by NimuFurryDevWithJefferson

fuck you masterchildporn too

I know all about you copper, your ip. Yrue search history. And everything.

---
## [NimuDevALTACC/FNF-PsychEngine](https://github.com/NimuDevALTACC/FNF-PsychEngine)@[05fc425bb2...](https://github.com/NimuDevALTACC/FNF-PsychEngine/commit/05fc425bb2998884521301f329c7809d50da76b8)
#### Sunday 2022-09-25 05:57:37 by NimuFurryDevWithJefferson

TheKitBoi sucks and should lick my trans vagina

shut up and fuck you kit “and jimmy too”

---
## [RenegadeGasper/Mike-Crack-](https://github.com/RenegadeGasper/Mike-Crack-)@[d2356b1867...](https://github.com/RenegadeGasper/Mike-Crack-/commit/d2356b18677d5fd9ba010fc1894ff64635a84bdf)
#### Sunday 2022-09-25 08:01:57 by RenegadeGasper

Cummit suicide

Goddammit fucking tiffany please let me eat your goddamn fucking cat

---
## [L-3-on/Cataclysm-DDA](https://github.com/L-3-on/Cataclysm-DDA)@[344458376f...](https://github.com/L-3-on/Cataclysm-DDA/commit/344458376f780b7ed8bca7e45fdc887eb05ea937)
#### Sunday 2022-09-25 08:28:38 by Christian Stadler

Update Sapiovore mood boosts from eating humans (#59077)

* Give psychopathic sapiovores a mood boost when eating human meat.

* Changes, because sapiovores can't be psychopaths at the same time

See also issue #58764

* Forgot the m_good and fixed the indentation.

* Moved sapiovore only chunk up and fixed my broken code.

* Removed one more redundancy

`sapiovore && spiritual` is handled above. No need to check that again.

* No message and no mood boost for Sapiovores without Spiritual.

* Sapiovore and Spiritual combo is now down to +10 morale

Message is "You eat the human flesh, and in doing so, devour their spirit.", similar to `cannibal && psycho && spiritual` but sapiovores don't feast upon it.

* Add "Mmh.  Tastes like venison." as neutral message for sapiovores

---
## [DarkWolfKai/lobotomy-corp13](https://github.com/DarkWolfKai/lobotomy-corp13)@[f490a226b2...](https://github.com/DarkWolfKai/lobotomy-corp13/commit/f490a226b241795abefbddeb84938af4e183b2a8)
#### Sunday 2022-09-25 10:14:23 by Gelatelly

sassy shepherd

makes shepherd lie like the bitch he is

I HATE RUNTIMES I HATE RUNTIMES I HATERUNTIMES

use the shittiest method in existence to bypass runtimes, unfortunately I couldn't use initial() without adding some issues so fuck me I guess

updates the people and abno list

imagine using signalers

why is there a huge gap there

leftovercode that doesn't do anything

linter fix?

this is the worst fix I hate linters so much

I'm making everything worse by trying to fix it

send help

adds abno spawn signaller

I love adding signallers for meme PR

changes how the lists are used/rename a few things

SLightCamelCaseChange

clears the people_list on destroy()

this isn't much but it should avoid some problems

moves the abno spawn signal to lobotomy_corp.dm

---
## [1015355299/react](https://github.com/1015355299/react)@[b6978bc38f...](https://github.com/1015355299/react/commit/b6978bc38f6788c7e73982b9fd2771aabdf36f15)
#### Sunday 2022-09-25 10:41:41 by Andrew Clark

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
## [Roseinfire/Paint](https://github.com/Roseinfire/Paint)@[55206152df...](https://github.com/Roseinfire/Paint/commit/55206152df4749e094e3370739e5c4cfdbdfee8a)
#### Sunday 2022-09-25 10:50:58 by Roseinfire

Create README.md

Yep, it's NOT mc paint. Project name is a kind of joke! Editor made for promote it's autor, so Paint is completely free tool. Simple and without any advertisment you can draw and edit images using various tools.There are not so much, but the list will be replenished. Moreover! you can add your own tools using JS and use whenever you want. Try to share with me and see how your tool appears in main list. Let's develop Paint together! Customize like you want! Choose own colors and sizes of content, be free in your self-expression. Remember, Paint created as free tool for free people. Notify me if you're intrested. Let's go! Create world together.

---
## [maikilangiolo/CEV-Eris](https://github.com/maikilangiolo/CEV-Eris)@[95469a19e2...](https://github.com/maikilangiolo/CEV-Eris/commit/95469a19e2a75ab3dbfc2b466ca775514593c17e)
#### Sunday 2022-09-25 11:00:46 by maikilangiolo

FUCK YOU FUCK YOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

---
## [Coder0511/Coder0511](https://github.com/Coder0511/Coder0511)@[ffea200d2a...](https://github.com/Coder0511/Coder0511/commit/ffea200d2aa3620280e07e491ac8051c5d21bdb4)
#### Sunday 2022-09-25 11:24:32 by Coder0511

Add files via upload

Well so last year I tried to do something original for the woman I love on Valentine's day. We live too far from each other, so I couldn't gift her anything that wasn't digitally. I tried to send her a rose in python but the programs I found on the Internet were kinda simple, so I did it myself with turtle. It's not the best program you can find but it did the thing.

---
## [ProjectVelvet/android_kernel_sm6250](https://github.com/ProjectVelvet/android_kernel_sm6250)@[3c32f25000...](https://github.com/ProjectVelvet/android_kernel_sm6250/commit/3c32f250009734ee7dae6e3dc4271f22403a05bd)
#### Sunday 2022-09-25 12:33:19 by Maciej Żenczykowski

FROMGIT: bpf: Do not change gso_size during bpf_skb_change_proto()

This is technically a backwards incompatible change in behaviour, but I'm
going to argue that it is very unlikely to break things, and likely to fix
*far* more then it breaks.

In no particular order, various reasons follow:

(a) I've long had a bug assigned to myself to debug a super rare kernel crash
on Android Pixel phones which can (per stacktrace) be traced back to BPF clat
IPv6 to IPv4 protocol conversion causing some sort of ugly failure much later
on during transmit deep in the GSO engine, AFAICT precisely because of this
change to gso_size, though I've never been able to manually reproduce it. I
believe it may be related to the particular network offload support of attached
USB ethernet dongle being used for tethering off of an IPv6-only cellular
connection. The reason might be we end up with more segments than max permitted,
or with a GSO packet with only one segment... (either way we break some
assumption and hit a BUG_ON)

(b) There is no check that the gso_size is > 20 when reducing it by 20, so we
might end up with a negative (or underflowing) gso_size or a gso_size of 0.
This can't possibly be good. Indeed this is probably somehow exploitable (or
at least can result in a kernel crash) by delivering crafted packets and perhaps
triggering an infinite loop or a divide by zero... As a reminder: gso_size (MSS)
is related to MTU, but not directly derived from it: gso_size/MSS may be
significantly smaller then one would get by deriving from local MTU. And on
some NICs (which do loose MTU checking on receive, it may even potentially be
larger, for example my work pc with 1500 MTU can receive 1520 byte frames [and
sometimes does due to bugs in a vendor plat46 implementation]). Indeed even just
going from 21 to 1 is potentially problematic because it increases the number
of segments by a factor of 21 (think DoS, or some other crash due to too many
segments).

(c) It's always safe to not increase the gso_size, because it doesn't result in
the max packet size increasing.  So the skb_increase_gso_size() call was always
unnecessary for correctness (and outright undesirable, see later). As such the
only part which is potentially dangerous (ie. could cause backwards compatibility
issues) is the removal of the skb_decrease_gso_size() call.

(d) If the packets are ultimately destined to the local device, then there is
absolutely no benefit to playing around with gso_size. It only matters if the
packets will egress the device. ie. we're either forwarding, or transmitting
from the device.

(e) This logic only triggers for packets which are GSO. It does not trigger for
skbs which are not GSO. It will not convert a non-GSO MTU sized packet into a
GSO packet (and you don't even know what the MTU is, so you can't even fix it).
As such your transmit path must *already* be able to handle an MTU 20 bytes
larger then your receive path (for IPv4 to IPv6 translation) - and indeed 28
bytes larger due to IPv4 fragments. Thus removing the skb_decrease_gso_size()
call doesn't actually increase the size of the packets your transmit side must
be able to handle. ie. to handle non-GSO max-MTU packets, the IPv4/IPv6 device/
route MTUs must already be set correctly. Since for example with an IPv4 egress
MTU of 1500, IPv4 to IPv6 translation will already build 1520 byte IPv6 frames,
so you need a 1520 byte device MTU. This means if your IPv6 device's egress
MTU is 1280, your IPv4 route must be 1260 (and actually 1252, because of the
need to handle fragments). This is to handle normal non-GSO packets. Thus the
reduction is simply not needed for GSO packets, because when they're correctly
built, they will already be the right size.

(f) TSO/GSO should be able to exactly undo GRO: the number of packets (TCP
segments) should not be modified, so that TCP's MSS counting works correctly
(this matters for congestion control). If protocol conversion changes the
gso_size, then the number of TCP segments may increase or decrease. Packet loss
after protocol conversion can result in partial loss of MSS segments that the
sender sent. How's the sending TCP stack going to react to receiving ACKs/SACKs
in the middle of the segments it sent?

(g) skb_{decrease,increase}_gso_size() are already no-ops for GSO_BY_FRAGS
case (besides triggering WARN_ON_ONCE). This means you already cannot guarantee
that gso_size (and thus resulting packet MTU) is changed. ie. you must assume
it won't be changed.

(h) changing gso_size is outright buggy for UDP GSO packets, where framing
matters (I believe that's also the case for SCTP, but it's already excluded
by [g]).  So the only remaining case is TCP, which also doesn't want it
(see [f]).

(i) see also the reasoning on the previous attempt at fixing this
(commit fa7b83bf3b156c767f3e4a25bbf3817b08f3ff8e) which shows that the current
behaviour causes TCP packet loss:

  In the forwarding path GRO -> BPF 6 to 4 -> GSO for TCP traffic, the
  coalesced packet payload can be > MSS, but < MSS + 20.

  bpf_skb_proto_6_to_4() will upgrade the MSS and it can be > the payload
  length. After then tcp_gso_segment checks for the payload length if it
  is <= MSS. The condition is causing the packet to be dropped.

  tcp_gso_segment():
    [...]
    mss = skb_shinfo(skb)->gso_size;
    if (unlikely(skb->len <= mss)) goto out;
    [...]

Thus changing the gso_size is simply a very bad idea. Increasing is unnecessary
and buggy, and decreasing can go negative.

Fixes: 6578171a7ff0 ("bpf: add bpf_skb_change_proto helper")
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Signed-off-by: Daniel Borkmann <daniel@iogearbox.net>
Cc: Dongseok Yi <dseok.yi@samsung.com>
Cc: Willem de Bruijn <willemb@google.com>
Link: https://lore.kernel.org/bpf/CANP3RGfjLikQ6dg=YpBU0OeHvyv7JOki7CyOUS9modaXAi-9vQ@mail.gmail.com
Link: https://lore.kernel.org/bpf/20210617000953.2787453-2-zenczykowski@gmail.com

(cherry picked from commit 364745fbe981a4370f50274475da4675661104df https://git.kernel.org/pub/scm/linux/kernel/git/bpf/bpf-next.git/commit/?id=364745fbe981a4370f50274475da4675661104df )
Test: builds, TreeHugger
Bug: 188690383
Signed-off-by: Maciej Żenczykowski <maze@google.com>
Change-Id: I0ef3174cbd3caaa42d5779334a9c0bfdc9ab81f5
Signed-off-by: Excalibur-99 <txexcalibur99@gmail.com>

---
## [RetroAchievements/RAPatches](https://github.com/RetroAchievements/RAPatches)@[0cf5b76ff4...](https://github.com/RetroAchievements/RAPatches/commit/0cf5b76ff4df5e1fdbb9dbf070bbb33ec9b4c31d)
#### Sunday 2022-09-25 13:23:07 by televandalist

Add Patches (#72)

* Add multiple patches

Included:
- Final Fantasy I & II - Mod of Balance (GBA) (Hack)
- Final Fantasy Legend II (GB) (Text Cleanup)
- F-Zero - Climax (GBA) (English Translation)
- Geheimnis der Happy Hippo-Insel, Das (GBC) (English Translation)
- Golden Sun (GBA) (Portuguese Translation)
- Kirby Tilt 'n Tumble (GBC) (Accelerometer Removal Patch)
- Kirby's Dream Land (GB) (DX Patch)
- Pokemon - Fool's Gold (GBC) (Hack)
- Pokemon - Kalos Crystal (GBC) (Hack)
- Pokemon - LeafGreen (GBA) (Moemon Patch)
- Pokemon - Polished Crystal (GBC) (Hack)
- Pokemon - Ruby (GBA) (Moemon Patch)
- Pokemon - Sapphire (GBA) (Moemon Patch)
- Pokemon Picross (GBC) (English Translation)
- Touhoumon - Ordinary Version (GBC) (Hack)
- Ultraman Ball (GB) (English Translation)
- Wario Land 4 - Parallel World (GBA) (Hack)
- Yoshi Topsy-Turvy (GBA) (Tilt Patch)
- Zelda - Sacred Paradox (GBA) (Hack)

* Update

Adds the following:
- Rockman 3 Claw (NES) (Hack)
- Xenogears (PS1) (Japanese Controls Patch)
- Xenogears (PS1) (French Translation)
- Xenogears (PS1) (Undub Patch)
- Chrono Cross (PS1) (Italian Translation)
- Chrono Cross (PS1) (Spanish Translation)

---
## [AscendedSion/Fedoraware](https://github.com/AscendedSion/Fedoraware)@[50a54973e7...](https://github.com/AscendedSion/Fedoraware/commit/50a54973e76ff2315320cab53235f3a91da053c8)
#### Sunday 2022-09-25 14:21:16 by Baan

Merge pull request #693 from Radeon0078/patch-1

fuck you this is better kys 130 fov sucks balls

---
## [Conga0/Mo_Creeps](https://github.com/Conga0/Mo_Creeps)@[eb9e0916a5...](https://github.com/Conga0/Mo_Creeps/commit/eb9e0916a514a3a732aa91ffe9135413b1b96e03)
#### Sunday 2022-09-25 14:42:12 by Conga Lyne

New Creep, Fixes, Twitch Integration

Increased spawn chances of some rare cats
Fixed cats spawning inside of intro props
Reduced Magic Poring damage slightly
Fixed Minecart Hisii shooting his shotgun out of thin air (magic!)
Minecart Hisii has since received a new friend in his minecarts for his good behaviour
New Creep: Esoteric Being

Added twitch integration events
Random Creeps & Weirdos - Spawns 6 random Creeps & Weirdos from the mod after 5 seconds
Kitty Cats!! - Spawns 20 cats!
Random Weirdo Boss - Spawns a random More Creeps & Weirdos boss after 10 seconds
Spawn Wand of Wonders - Creates a wand of wonders

---
## [eun0115/kernel-m20lte](https://github.com/eun0115/kernel-m20lte)@[d247a3daab...](https://github.com/eun0115/kernel-m20lte/commit/d247a3daab21d62f66dcc7b31c51f54f3316488f)
#### Sunday 2022-09-25 15:31:24 by Masahiro Yamada

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

---
## [Seamusmario/mespeak-engine](https://github.com/Seamusmario/mespeak-engine)@[3b628b2d54...](https://github.com/Seamusmario/mespeak-engine/commit/3b628b2d545f105026800d20880f774d726cef44)
#### Sunday 2022-09-25 17:22:16 by CrazyMediumScout

I'M SO FUCKING FUCKING FUCKING FUCKING TIRED OF YOUR SHIT KAI U MY FUCKING GOD JUST GO TO YOUR ROOM FUCKING NOW

---
## [bricksticks/pluralsight](https://github.com/bricksticks/pluralsight)@[bca000b943...](https://github.com/bricksticks/pluralsight/commit/bca000b9433f39c8f431643adfb1f61391cb9b82)
#### Sunday 2022-09-25 17:39:55 by christoph huerzeler

PluralSight: Playing with Flutter

- just played a bit with flutter
- not sure how happy I am with the developer experience
- it is super fast to build something, I like the concepts and
  how UIs are implemented declaratively
- I.e. you just tell flutter this is how my UI should look like and
  if state changes you just tell flutter, state changed and
  it will update what needs to be updated (you don't need to worry
  about what needs updating and what doesn't)
- However, you are kind of locked into Material Design or Cupertino
  Otherwise I'm quite sure you can make things work with raw widgets
  but things will get bumpy
- Also due to the way code is structured and how you work with
  very deeply nested hierarchies of widgets I'm very sure it
  will be super easy for a not-so-careful developer to create a
  hell hole of horrors with deeply layered and unstructured
  code that will be very hard to understand
- I'm not sure I would build a web app or a desktop app with flutter
  right now
- I think flutter apps need to remain comparatively small and
  lightweight, otherwise things can get out of hand with the
  nesting in flutter

---
## [kleinerm/Psychtoolbox-3](https://github.com/kleinerm/Psychtoolbox-3)@[b85250b062...](https://github.com/kleinerm/Psychtoolbox-3/commit/b85250b062a7930681cdf7050f3e40457ff962b1)
#### Sunday 2022-09-25 18:44:40 by Mario Kleiner

PsychHID/OSX: Avoid calling PsychHIDWarnAccessDenied frequently.

The latest fix for the latest security bullshit, introduced sometime after macOS
10.15 Catalina. This was found when testing Octave on macOS 12.5 Monterey.

Apparently the call to IOHIDCheckAccess() by PsychHIDWarnAccessDenied()
is now extremely costly on macOS 12 (possibly also macOS 11 - untested) iff
the host application was launched from Terminal.app instead of standalone via
clicking a launch icon. This showed on Octave 6.4 after upgrade to macOS 12.5,
as octave is always launched from Terminal, regardless if in console mode or
GUI mode. Matlab appeared unaffected, as it is usually launched by clicking the
Matlab icon, but if one launches Matlab from a terminal, the same happens.

Why IOHIDCheckAccess() was suddenly turned into such an expensive operation
by the iDiots, i don't know, but our workaround is to no longer call it at each
invocation of KbCheck or KbQueueCreate, but only at PsychHID startup, and
hope this does not have other new bad effects.

Note access time exploded from way less than 1 msec to over 15 msecs! Great
work Apple!

Now we are back to identical performance on Matlab and Octave in both GUI
and commandline mode. Performance is bad compared to Linux or Windows,
but manageable at about 2.4 msecs on macOS 12.5 Monterey on a MBP 2017.
However, if run on a MacBook with touchbar, two PsychHID('KbCheck') calls
are needed for each KbCheck() call, because the touchbar is a separate HID
device, serving the important ESCape key and also function keys, so owners
of a shitty touchbar machine will have to live with execution times of KbCheck
on the order of 5 msecs on not that old hardware like the MBP 2017! This makes
animation loops with KbChecks difficult to run beyond 60-100 fps. Such is the
life of Apple customers...

When we are here, improve troubleshooting instructions for security bullshit
on macOS, and fix two compiler warnings new on macOS 12.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[d45e244401...](https://github.com/tgstation/tgstation/commit/d45e244401425d34edc38e3dd2f3c2bbdbcec7ce)
#### Sunday 2022-09-25 18:49:13 by san7890

Crab-17 No Longer Breaks Economy If You Swipe Too Fast (#70094)

Hey there,

Remember swiping credit cards, before everything was chipped? You know how sometimes if you went too slow, the transaction might fail, the cashier had to plonk in some digits on their machine, and you had to go again? That kinda sucked.

If you're too young to get that reference, just imagine the card swiping task in AMONG US. Doesn't that minigame suck? You know exactly what that is. Same principle.

Anyways, that's pretty much what was going on here. The reason why SS.Economy would break so god damn hard if you swiped an ID before the machine's "boot up" slowflake animation was complete is probably due to the line where it starts fast processing. I added an early return to check for if the animation was complete by leveraging a var we already set at the end of the process, because I am lazy.

There's probably a few other ways you can tackle this issue, but this feels right to me in a thematic sense. I'm willing to change it if needed though.

---
## [SlenderFox/OpenGL-Engine](https://github.com/SlenderFox/OpenGL-Engine)@[d780a56112...](https://github.com/SlenderFox/OpenGL-Engine/commit/d780a56112f22d16c9a9f2cd98ce125d2729757c)
#### Sunday 2022-09-25 19:27:54 by SlenderFox

Utterly fucking cursed model loading

Using a friended struct to loaded the model then calling it either from the member function or struct passing an Entity pointer ref.

---
## [benlumley/msp-osd](https://github.com/benlumley/msp-osd)@[1b8b4b6f67...](https://github.com/benlumley/msp-osd/commit/1b8b4b6f67e471360be4560071d0edbc5a8a5205)
#### Sunday 2022-09-25 21:36:00 by Brian Ledbetter

Fakehd and Config Options (#52) - thank you @benlumley

* Squashed commit of the following:

commit b9bcccbf76974e34c672b0e39c1443bb6ac84af9
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Tue Sep 20 22:48:35 2022 +0100

    switch to config

commit c50d23104e4fb4f6e6a25b2bb0b72fcecc6128f7
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Tue Sep 20 14:16:24 2022 +0100

    changed mind; y direction doesn't need the 1 offset - nicer to have it near the edge; then you can get things inline with the goggles own osd at the bottom

commit 4af3df6c126ac273b03e9191699b92513e1b3f2d
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Mon Sep 19 20:47:59 2022 +0100

    Battery symbols flash when in warning state; so can't use them to trigger centering :(

commit 689384f0449daed42929d90f19c1946368fd0a31
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Mon Sep 19 10:26:58 2022 +0100

    In from the edges a bit; we have spare rows/cols - in my opinion it looks better not to have everything literally touching the sides

commit db06e4885c93a9a0350ffab6afa08fcb068fd63a
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Fri Sep 16 19:39:50 2022 +0100

    Docs review + add fakehd

commit b6f20c0cf2e74e6bca98555c731ea4b11f41d6f4
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Thu Sep 15 22:49:18 2022 +0100

    Debugged/working

commit 8000b88d022fb40e30e0aa7f03df0613c637ece8
Author: Ben Lumley <ben@benlumley.co.uk>
Date:   Fri Sep 2 00:15:28 2022 +0100

    Attempt at proof of concept to 'spread' the SD osd to the corners + middle of the HD OSD.

    Not managed to get it running to test. But here's the idea:

    BF grid is 16 * 30
    HD is 18 * 50

    BF Rows 1-5 -> HD Rows 1-5
    BF Rows 6-10 -> HD Rows 7-11
    BF Rows 11-16 -> HD Rows 12-18

    BF Cols 1-10 -> HD Cols 1-10
    BF Cols 11-20 -> HD Cols 20 - 30
    BF Cols 21-30 -> HD Cols 40 - 50

    Visually, divide the OSD into a 3*3 grid and stretch it to the top/bottom/left/right corners.

    I tend to put osd elements in the bottom corners, bottom middle + the warnings in the middle. So for me at least; this is useful.

    Obvious drawback; the menus gonna look weird!

    fix for force hd not working because BF never even sends the MSP command; it needs to default to it earlier.
    also add 2 unsplit rows for wider elemenets - i like warnings in the middle of the screen

    Add full display info; attempt to detect menu/post flight stats and switch to centering in this case

    Remove testing code

    make code paths simpler

    Find the center trigger instead of hard coding

    configurable; with a file for now

commit 60215e0240cbe5d34d0db447b01d948808705ed2
Author: bri3d <brian@brianledbetter.com>
Date:   Tue Sep 20 22:24:16 2022 -0600

    forgot an important directory...

commit 1c5ed2a88feb03bf209e4ed3c3ac4ed277681f47
Author: bri3d <brian@brianledbetter.com>
Date:   Thu Sep 15 21:51:48 2022 -0600

    add goggles config file

commit cfe24e265e8a3bfa92c34d6fc0e9594b63f98928
Author: bri3d <brian@brianledbetter.com>
Date:   Thu Sep 15 21:23:00 2022 -0600

    add JSON config support

* add fake HD to schema

* add ability to disable AU data overlay, add comments, cleanup

* add proper ipk deps and readme

Co-authored-by: Ben Lumley <ben@benlumley.co.uk>

---
## [ammarfaizi2/linux-fork](https://github.com/ammarfaizi2/linux-fork)@[13c83f4843...](https://github.com/ammarfaizi2/linux-fork/commit/13c83f48433fed7ada1b4742a5dcb47baa5514fb)
#### Sunday 2022-09-25 21:46:12 by Johannes Weiner

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
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[f033cb4ab8...](https://github.com/Offroaders123/NBT-Parser/commit/f033cb4ab858a2b05cfcc45df754b1ec8e73e82e)
#### Sunday 2022-09-25 22:23:50 by Offroaders123

Read Function + Browser Checks

Additions:
- Added improved parameter type validation to the `read` function and `Reader` constructor.
- I am also planning to look into TypeScript type declarations in the next few updates! I'll use `d.ts` files for the types rather than moving the project over to TypeScript, because I like that everything works with only vanilla JS out of the box! No need to build for Node or the browser, it already works directly for both (Of couse, using a bundler to make adding it easier is always a great option though, I just don't want it to be mandatory to run the library).

Changes:
- Restructued the `read` function to fully include all of it's own logic! Now it doesn't need help from the additional  hidden `runReader` function.

Fixes:
- Tested support for the parser within the browser, and fixed a few issues that allow you to either read NBT by passing an `ArrayBuffer`, or `TypedArray`. It was working as expected with `TypedArrays`, but I had to add a few wrappers to allow you to input `ArrayBuffers` as well. This was also the case for Node, but you usually deal with `Buffer` over there, and that's an instance of `Uint8Array`, so you wouldn't encounter the `ArrayBuffer` issues. The reader logic essentially just wasn't expecting to have an `ArrayBuffer` as an entry, and that's what I fixed.
- Adjusted the Bedrock Level header check logic, as it appeared to be throwing double negatives unexpectedly. I accidentally made it less accurate with the last update, so that's fixed now.

Oh yeah!
- Forgot to mention this for some time now, but I actually completely replaced Chrome OS on my Chromebook, and now it runs full Ubuntu! It's a great experience, it's convinced me that the next laptop I get will be for solely Linux (probably Ubuntu), as it has been so nice to install things on here for my dev work. It honestly feels like what I would *wish* macOS could be. The fact of how many things I can change to my liking are so fun and relieving, it's such a nice user experience. GNOME has been very awesome, I got it to be exactly how I want it to work, and the toucpad gestures are also a great bonus.
- I made the jump back around the beginning of May, and I forgot to mention it in any of my commit logs (Since that seems to be my blog post setup for some reason, haha).
- If you have an old Chromebook that you don't have a use for anymore, try looking into if you want to get Linux on there, mine has a brand new life with Ubuntu, it's actually unbelievable what it can do now! The only thing I don't like about it is just that my Chromebook is't quite to powerful and it only has 16GB of onboard storage, so I live at about 90% of it full with a gig left for programming. Not the best at times, but hey, this Chromebook was only $20 after my senior year, and it just had it's Chrome OS end of life a few days ago (sometime in June), and he's still got much more to go after this, thanks to Linux :)

---
## [Offroaders123/NBT-Parser](https://github.com/Offroaders123/NBT-Parser)@[493b83d08c...](https://github.com/Offroaders123/NBT-Parser/commit/493b83d08ce63fa1456fbe9551420c44f9ba9663)
#### Sunday 2022-09-25 22:23:50 by Offroaders123

A New Writer-Up

Additions:
- Added checks to the start of the `write` function and `Writer` constructor. TypeScript type definitions coming soon! I have a tab open about it right now :)

Changes:
- Rewrote the `write` function and `Writer` class, a similar set of changes as to what I did over on the reading side of things yesterday.
- One of the bigger changes to the write methods, now each one has all of it's logic built in, as now there's no more `write` method, only each method for writing each type. It is a little more code, but it is a bit better at showing what each function does.
- For each of the write methods with for loops, each one now uses either `for of` or `for in` loops where possible, rather than just a standard `for` loop. I like the simplicity of those a lot, and I realized that they could apply great here too.
- Added a few more variables to break up some of the looping functions, as it was pretty complex to comprehend what each section was selecting. It should also be a bit easier to debug with those in there too, since you can just add a `console.log()` to see what the variable's value is, rather than having to write the call out again to break part of it up to get the intermediate values in there.

Oh yeah!
- Listening to Closure / Continuation for the second time through as of now, "Of The New Day" right now! First time listening to it yesterday afternoon, wow did they do a great job! Can't believe PT is releasing new material again.
- Finally found a nice version of Insignificance on YouTube, so that will probably be my copy of that eventually. I also will be getting Yellow Hedgerow Dreamscape too, the album that is. The song is epic, and the extra hard to find compilation album is an extension of that. There are more and more cool hidden gems out there, you just have to look a little harder to find them!
- Oh yeah, and I came across their first concert on Bandcamp too, that is also a likely must buy! Back in 1993, at Nag's Head, an extra epic venue that used to be around. Just read that they turned it into flats in 2018 I heard, bummer! The sound quality on the recording was great, even for coming up on 30 years ago. I was -10 :O
- Ok, and I have to mention how much I love Up the Downstair, just gotta say...

---

