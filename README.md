## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2022-11-19](docs/good-messages/2022/2022-11-19.md)


1,890,714 events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,890,714 were push events containing 2,507,787 commit messages that amount to 158,620,998 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 36 messages:


## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[120cbae7e7...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/120cbae7e703c5b7fa96924da5c90e1acdea3dc3)
#### Saturday 2022-11-19 00:07:25 by SkyratBot

[MIRROR] Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation. [MDB IGNORE] (#17554)

* Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation. (#71157)

## About The Pull Request

Resolves #67282.

As originally designed, plasma rivers (namely, those on Icebox, though
the turf was originally made for the Snowdin away mission) are meant to
literally strip the flesh from your bones, leaving you with plasmaman
limbs. I'm not certain when this broke entirely, although it seems to
have never been updated to work alongside Kapulimbs.

Transformation of limbs into plasmaman limbs used to be accomplished by
adding the "PLASMABURNT" trait to limbs. However, this trait in the
current code is entirely meaningless, only checked in the proc that
makes plasmamen catch fire. Essentially, the only "interaction" is
having your flesh melted off by a plasma river, donating that specific
limb to a plasmaman, and pranking them with the fact that that specific
limb will still make them burst into flames.

Exciting.

I've removed the trait entirely, as it does functionally nothing, and
restored the ability of plasma rivers to turn your limbs - and
eventually, you - into plasmaman equivalents.

To be honest, I'm not _entirely_ satisfied with the plasmaman
transformation process - it doesn't especially suit the lore of
plasmamen, and if you transform into one in the plasma rivers you'll
probably immediately die from Icemoon's atmosphere anyway. However, this
is something I'd prefer to revisit in a later PR.
## Why It's Good For The Game

There's little reason _not_ to remove a trait that does nothing.

As for plasmafication, it's a fun interaction that was already _meant_
to be there. The message about your flesh melting off has always
printed, even while it's doing exactly nothing to you. It's cool to fall
into the deadly plasma river and come away from it permanently scarred
with a weird skeleton limb. Turning into a plasmaman entirely is
unlikely to happen and will probably just kill you, but it's a fun and
weird way to be dead.
## Changelog
:cl:
del: Removed the useless "plasmaburnt" trait.
fix: Restored a broken interaction with plasma rivers that slowly
transforms you into a plasmaman.
/:cl:

* Removed TRAIT_PLASMABURNT, fixed plasma river limb transformation.

Co-authored-by: lizardqueenlexi <105025397+lizardqueenlexi@users.noreply.github.com>

---
## [ToppleKek/banter2](https://github.com/ToppleKek/banter2)@[23efa378ea...](https://github.com/ToppleKek/banter2/commit/23efa378eaa0f6e9d0b40807be10d8461381c75f)
#### Saturday 2022-11-19 00:31:05 by ToppleKek

Stats: Fix typo from new d.js version

I wish they would stop changing the fucking api god damn

---
## [sjp38/linux](https://github.com/sjp38/linux)@[bf1d7c943f...](https://github.com/sjp38/linux/commit/bf1d7c943f124b946cc168b455f5ee146c4304c1)
#### Saturday 2022-11-19 00:34:48 by Johannes Weiner

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
## [TheBoondock/tgstation](https://github.com/TheBoondock/tgstation)@[85b2d5043d...](https://github.com/TheBoondock/tgstation/commit/85b2d5043dbc9eb277bf57dd6dc5147ae08fe978)
#### Saturday 2022-11-19 01:27:12 by LemonInTheDark

Optimizes qdel related things (slight init time savings) (#70729)

* Moves spawners and decals to a different init/delete scheme

Rather then fully creating and then immediately deleting these things,
we instead do the bare minimum.

This is faster, if in theory more fragile. We should be safe since any
errors should be caught in compile since this is very close to a
"static" action. It does mean these atoms cannot use signals, etc.

* Potentially saves init time, mostly cleans up a silly pattern

We use sleeps and INVOKE_ASYNC to ensure that handing back turfs doesn't
block a space reservation, but this by nature consumes up to the
threshold and a bit more of whatever working block we were in.

This is silly. Should just be a subsystem, so I made it one, with
support for awaiting its finish if you want to

* Optimizes garbage/proc/Queue slightly

Queue takes about 1.6 seconds to process 26k items right now.
The MASSIVE majority of this time is spent on using \ref
This is because \ref returns a string, and that string requires being
inserted into the global cache of strings we store

What I'm doing is caching the result of ANY \ref on the datum it's
applied to. This ensures previous uses will never decay from the string
tree.

This saves about 0.2 seconds of init

---
## [covertcorvid/NSV13](https://github.com/covertcorvid/NSV13)@[3249b4560b...](https://github.com/covertcorvid/NSV13/commit/3249b4560b568fe762f2a695a6427bab7c56c649)
#### Saturday 2022-11-19 01:55:02 by DrDuckedGoose

Lasso Fix (#7345)

* Merge https://github.com/BeeStation/BeeStation-Hornet into annoying-thing Merge conflicts :)

* Initial - 23 7 22

- Doesn't allow dead mobs to be ridden
- Space walk is now specific to the mob

* Actually Fix It - 23 7 22

* Fuck - 23 7 22

- Fix being able to tame human
- Fix being able to tame the dead

* Update carp_lasso.dm

* You boys fucked buckle code - 23 7 22

* Update carp_lasso.dm

* Update riding.dm

* fix icon - 24 7 22

* Review Changes - 24 7 22

---
## [Offroaders123/Art-Gen](https://github.com/Offroaders123/Art-Gen)@[8868a57fc9...](https://github.com/Offroaders123/Art-Gen/commit/8868a57fc9f51da9d30eae1059c0b9c364857a4e)
#### Saturday 2022-11-19 04:00:21 by Offroaders123

Full-Vector Thumbnail: Custom Fonts!

Got embedding the Noto Sans font into the static SVG working!!! Super happy with this already. The thumbnail setup is now essentially feature complete, so now it's time for some code reworking to organize things out, and remove any rough edges that are still around. I am debating moving this project to TypeScript too, but I'm not totally sure yet. I like having the ability to define interfaces in TS, and it looks like that's not quite as simple to make with JSDoc. JSDoc has been perfect so far for variable type inference and function declaration types, but it does feel like it gets a little more hectic when you start making an outwards-facing API, which is something I will want to have for the project also. I think I'll probably hold myself from moving to TypeScript until I really *need* to make an API. This isn't ready to provide others with something to build with yet, and that's mainly what I'd want to have TypeScript for eventually. So, yeah!

Ran a half marathon today, it was very nice out! A little chilly, but sunny, so the right combo :)

Forgot to add in my other recent commits (I think?), I've started looking into Frank Zappa, and MAN, was he a cool guy! Can't wait to listen to his albums, as I already love Keneally and Minnemann's projects, and those tend to be pretty far out there too. I *strongly* love music now.

If you are a fellow music nerd too, feel free to send any suggestions my way, and I'd be happy to do the same back to you!

---
## [987123879113/pcsx2](https://github.com/987123879113/pcsx2)@[87abacc632...](https://github.com/987123879113/pcsx2/commit/87abacc63264f9cf554cddf02973e0fc9cd2af77)
#### Saturday 2022-11-19 05:01:37 by RedDevilus

GameDB: Fix multiple games + maintenance

- Area 51: Half Pixel Normal vertex for lighting and other places
- Shrek 2: Basic mipmapping which kinda half fixes the sun missing
- Galaxy Angel II: Normal vertex which reduces misalignment
- Forgotten Realms - Demon Stone: Clamping Mode extra + preserve which will solve the occasional SPS + missing demo entry.
- Spyro Dawn of dragon: SW clut + sprite which doesn't make you vomit from the overbloomification and looks similar to the software renderer
- Castlevania Curse of darkness half sprite which will enlarge the font similar to software renderer + some missing fixes that were available on the Europe and America versions but not Japanese.
- Drakengard 1 + 2 (Also know as Drag-on Dragoon) : Partial (no hashcache) to avoid slow transitions and other areas. Adds missing Japanese Drakengard 1
- Urban reign: Partial texture preloading to fix performance issues in the gameplay
- Onimusha Warlord: Partial preloading to fix performance issues
- Sniper Elite: Fix sky lighting
- Maintenance that add spaces in the titles for Disc1of1 to Disc 1 of 1 and more...

---
## [DarkKnight2019/terminal](https://github.com/DarkKnight2019/terminal)@[9ccd6ecd74...](https://github.com/DarkKnight2019/terminal/commit/9ccd6ecd744890b856f3d8a39ff0616c0e34d4fb)
#### Saturday 2022-11-19 07:02:56 by Mike Griese

Manually copy trailing attributes on a resize (#12637)

## THE WHITE WHALE

This is a fairly naive fix for this bug. It's not terribly performant,
but neither is resize in the first place.

When the buffer gets resized, typically we only copy the text up to the
`MeasureRight` point, the last printable char in the row. Then we'd just
use the last char's attributes to fill the remainder of the row.

Instead, this PR changes how reflow behaves when it gets to the end of
the row. After we finish copying text, then manually walk through the
attributes at the end of the row, and copy them over. This ensures that
cells that just have a colored space in them get copied into the new
buffer as well, and we don't just blat the last character's attributes
into the rest of the row. We'll do a similar thing once we get to the
last printable char in the buffer, copying the remaining attributes.

This could DEFINITELY be more performant. I think this current
implementation walks the attrs _on every cell_, then appends the new
attrs to the new ATTR_ROW. That could be optimized by just using the
actual iterator. The copy after the last printable char bit is also
especially bad in this regard. That could likely be a blind copy - I
just wanted to get this into the world.

Finally, we now copy the final attributes to the correct buffer: the new
one.  We used to copy them to the _old_ buffer, which we were about to
destroy.

## Validation

I'll add more gifs in the morning, not enough time to finish spinning a
release Terminal build with this tonight.

Closes #32 🎉🎉🎉🎉🎉🎉🎉🎉🎉
Closes #12567

(cherry picked from commit 855e1360c0ff810decf862f1d90e15b5f49e7bbd)

---
## [chuigda/Project-WG](https://github.com/chuigda/Project-WG)@[26652c5ebe...](https://github.com/chuigda/Project-WG/commit/26652c5ebe38871e2b7a9c4bb8770297bbf113cc)
#### Saturday 2022-11-19 10:30:06 by icey

Chur, chur, chur, everyday. Fuck you all noisy monkeys!

---
## [Empire-Strikes-Back/Pippen](https://github.com/Empire-Strikes-Back/Pippen)@[49fb11a273...](https://github.com/Empire-Strikes-Back/Pippen/commit/49fb11a27370d8d383e917abf2c443fc52923097)
#### Saturday 2022-11-19 11:18:11 by Pippen

you think falttery will save you, thief?

like Kendrick Perkins I don't have skill but vulture my way into the team

unlike Adele I was going to stay overweight - without applying whole foods plant based advantage

I heard Jesus speak about love and enemies, woman who washed his feet with her tears

let my spotty-cube example run again
unlike the Master of Laketown I don't take no boat of gold with me - and now I wont drown

:Stephen-Fry your adress please, mr. Nipple
:Hugh-Laurie do you want to know my address? or mr. Nipple's address?

---
## [ZhugeDongming/mod-anticheat](https://github.com/ZhugeDongming/mod-anticheat)@[a354922e07...](https://github.com/ZhugeDongming/mod-anticheat/commit/a354922e07020f5ba5c7c6aa43d95eaae10aa1b3)
#### Saturday 2022-11-19 13:33:25 by MDIC

Update: Readjusted SQL, New Dectection , new Conf

Readjusted the Sql again, Removes the teleporthack_report collumns. It is pretty much worthless with its insane high count that would cause drag on the db and well not needed, it seems like a good idea at the time but it isnt, instead it will add a +1 to the total_reports collumn and the teleport and ignore control hacks will spam their own message once the reports hit default 70 or whatever the user has set. New detection type Ignore Control Hack, This is if a player is rooted or stunned, they are able to still move when effected.

---
## [GoblinBackwards/tgstation](https://github.com/GoblinBackwards/tgstation)@[25d4afc869...](https://github.com/GoblinBackwards/tgstation/commit/25d4afc869585373571da5ba4a77fb967ffdedfe)
#### Saturday 2022-11-19 13:40:37 by Iamgoofball

Retires explosive lance crafting to a nice farm upstate where it has plenty of room to run around (#71256)

## About The Pull Request

You can no longer craft explosive lances.

## Why It's Good For The Game

Explosive lances are unhealthy for the game in it's current iteration.
Many years ago when the game was more loose and we weren't dealing with
players who treat the game like competitive TTT or Town of Salem,

They are a one shot kill weapon, which is the most powerful kind of
weapon in every gamemode. @JohnFulpWillard likened it to 1f1, a concept
from Town of Salem players where the town trades 1 person for 1 bad guy.

Modern ss13 design includes a significantly heavier load of antagonists
that aren't fixed roundstart compared to when the e-lance went in.

When we added the e-lance, if nuke ops spawned, that was it, there was
nuke ops, if you e-lanced the nuke ops and died you were dead until the
next round.

Nowadays you're rolling for lone operative, blob, wizard, disease,
revenant, and every other fun enjoyable antagonist role under the sun.

I can e-lance a nuke op/cultist/traitor/revolutionary/any bad guy in the
game as a non-antag assistant, die, and have a good chance to roll
another, way more fun antag in deadchat.

My change to make the e-lance a proper "we both die" tool didn't
actually help because I didn't quite realize that to the modern SS13
player because of how we designed Dynamic and antagonists in the modern
era, death is, frankly, not a punishment anymore.

It's time we admit the facts, items designed in 2015 SS13 in #12389
simply don't hold up in a healthy manner in 2022 SS13. Dying in SS13 in
2015 was a significantly different experience with different
consequences than it has now, and right now "kills you when you use it"
is not the same massive downside it was 7-8 years ago.

## Changelog
:cl:
del: You can no longer craft explosive lances.
/:cl:

---
## [Geevies/cmss13](https://github.com/Geevies/cmss13)@[ca2114f0f5...](https://github.com/Geevies/cmss13/commit/ca2114f0f56ab4a51443bdac52053ead327724dc)
#### Saturday 2022-11-19 13:58:50 by Mister-moon1

Removes some useless code from welding helmet (#1363)

* fuck you useless code

* you cannot hide, useless code

---
## [Geevies/cmss13](https://github.com/Geevies/cmss13)@[2a8ebba36a...](https://github.com/Geevies/cmss13/commit/2a8ebba36a2c76ed855987dc107c9c385f6f16ea)
#### Saturday 2022-11-19 13:58:50 by Joelampost

Pred bug fix no.2 (#1287)

* a

a

* Update code/game/objects/structures/tables_racks.dm

Co-authored-by: harryob <me@harryob.live>

* Update yaut_procs.dm

* :>(

* fuck you

* return

* Update code/modules/cm_preds/yaut_procs.dm

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

* Update code/game/objects/structures/tables_racks.dm

Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

Co-authored-by: harryob <me@harryob.live>
Co-authored-by: Stan_Albatross <66756236+stanalbatross@users.noreply.github.com>

---
## [spartanbobby/cmss13](https://github.com/spartanbobby/cmss13)@[7cb69c2a8b...](https://github.com/spartanbobby/cmss13/commit/7cb69c2a8b6f8895d5475b709183a3f30d05fbeb)
#### Saturday 2022-11-19 14:17:07 by Joelampost

Creates a new tile for the predator ship (#1400)

* erm

* yer

* fuck you shaddeh

---
## [KDE/spectacle](https://github.com/KDE/spectacle)@[fa7b875b3b...](https://github.com/KDE/spectacle/commit/fa7b875b3bdea3b58d8db34003bbdd4a94c758ec)
#### Saturday 2022-11-19 14:35:02 by Noah Davis

Use QML SelectionSizeToolTip

remove hideWindow

don't make window transparent

not needed

use isGuiIntitiated

use new window sizing code paths

moved some stuff around to make it easier to get the timing for window
sizing right and also make stuff happening to the window happen in the
window class.

shorten code line

do touchEvent later

set up window color

dialog size/positioning

clean up

stuff I forgot

set cursors via hoverMoveEvent

make SelectionEditor a FocusScope

remove unneeded files

use native text rendering by default

add border and transparency to info box

Selection: add rect, rectItersectsRect, rectContainsRect, fix setX/setY

SelectionEditor: add dragLocation property

SelectionEditor: add dprRound

remove qpainter size tooltip

cleanup

InfoBackground -> FloatingBackground

temp: disable mandatory clang-format

god it's annoying. will remove this change later

add placeholder floating toolbar

will use for future functionality

SelectionEditor: add handlesRect property, clean/fix up painting

- exposes the area where the handles are to QML
- fixes some visual glitches
- makes the visual selection area slightly more accurate to what the
actual selected area is
- no longer changes stored data while painting

update overlay

Selection: add qDebug output

Selection: add dpr to debug output

clean up painting

SelectionEditor: Always use QPointF for mouse positions

If you don't, then you will lose precision when the GUI is scaled up.

SelectionEditor: combine size tooltip with toolbar when they overlap

SelectionEditor: redorder some functions for my convenience

Add SpectacleImageProvider

clean up

might delete this file later

cleanup and fix clazy/clang-tidy warnings

move invokable dprRound to SpectacleWindow, rename some qml files

add ImageView

SelectionEditor: comment formatting

SpectacleWindow: set max size in setGeometryFromScreensRect

SpectacleWindow: testing max DPR hack

theoretically, this should allow Spectacle to always use the max DPR on
Wayland so that higher DPR screens never have low resolution graphics.
Will likely cause serious performance issues until we switch to using
more QSG stuff for the SelectionEditor.

SpectacleWindow: use base/view background color for image view

Polish ImageView, add save/copy functions, make positioning work on wayland

really disable pre-commit hooks

missed this. it's temporary.

ensure image is always only just as big as it needs to be

clip ImageView toolbar while resizing, fix up padding

Focus qml item when not in selection mode

Add OptionsMenu

keep settings dialog above parent window

make acceptSelection public again

put rectangle selection first

ExportMenu: Add open screenshot folder and print actions

Change menus to just Export, Options and Help

Remove window state changing stuff

It works very poorly with Wayland

Fill image selection toolbar with real buttons

OptionsMenu: add all the actions

OptionsMenu: make showPreferencesDialog public

Allow window to be transparent for video recording UI

---
## [TayMcKenzieNZ/dpemotes](https://github.com/TayMcKenzieNZ/dpemotes)@[fadbae861b...](https://github.com/TayMcKenzieNZ/dpemotes/commit/fadbae861b8eadf7aa6b2ef469797c2b6602ba23)
#### Saturday 2022-11-19 14:55:15 by TayMcKenzieSA

Implemented More Walkstyles Found In Menyoo

You don't own any code, get a life, stay the fuck out of my DMs, touch grass, stop claiming shit to be yours.

---
## [Conga0/Mo_Creeps](https://github.com/Conga0/Mo_Creeps)@[8e5b22e650...](https://github.com/Conga0/Mo_Creeps/commit/8e5b22e650c105bd0ff2fb46a563ebd7b813208e)
#### Saturday 2022-11-19 15:26:17 by Conga Lyne

New experimental creep

Improved Divine Being's shield visuals
Fixed noitavania initialisation error
Increased maximum number of fairies visible at once, they used to have 20 available at any given time but this was broken at some point to only allow 5 at once, this has been fixed
Fixed Hisii Hobo having their sprite offset
Enraging Aura now affects your halo level

New Experimental Creep: Mudman
I'm not certain on these creatures yet, they are made from pouring water on soil to make mud, then pouring pheromone on mud to make magical mud, then you will gain some friends.

---
## [FRC5113/Library](https://github.com/FRC5113/Library)@[0b2db518ee...](https://github.com/FRC5113/Library/commit/0b2db518ee94a262fd4d06b85b4daf2936427854)
#### Saturday 2022-11-19 15:47:28 by jrego05

Jr odometry (#5)

* Added SmartOdometry class for mid game switching between mecanum and differential. Enum OdometryType added as well as a new constructor for SmartFalcon that includes a Pose2d for a drive motors relative position. A few issues with static things that I am not sure about, as well as two issues with unit conversion with WPIlib marked with comments in the update method in SmartOdometry

* Jack did a dumb - Vlad

* 2 changes, don't worry about it

* Odometry is less stupid

* a small change to see if Vlad is stupid

* Added a few gyro methods to SmartOdometry

* adding things in small increments to annoy Vlad

* reset and position getting capabilities to SmartOdometry

* Fixed some javadocs shit

---
## [rawlins/crawl](https://github.com/rawlins/crawl)@[1352289c90...](https://github.com/rawlins/crawl/commit/1352289c90d15a53f9c472dac9343ad61d9104a7)
#### Saturday 2022-11-19 16:18:17 by Nicholas Feinberg

New species: Meteoran

Time pressure often creates exciting gameplay and interesting
tradeoffs. Baseline Dungeon Crawl uses the Zot Clock to add a
very weak form of time pressure, but there's so much variety
between the playstyles of different species and backgrounds
that a tight clock for some would be almost impossible for
others.

So, let's try limiting that gameplay to just one species!
Meteorae have an exciting variety of bonuses - great attributes
and aptitudes across the board, passive mapping, and exploration
healing, regaining HP and MP when viewing new territory. In
exchange, they have one big downside: instead of getting 6,000
turns of Zot clock for each floor, they get 600!

The big concern here is whether this species can be made fun
without also being made wildly, boringly 'overpowered'. Lots of
levers and knobs to tweak, so let's give it a shot!

Extra notes:
- Meteorae are humanoid beings. (In the night sky, they look
  like dots because they're very far up.) Hat tip to Neil Gaiman's
  Stardust.
- This commit has a silly 'flavour' gimmick where Meteorae's LOS
  radius decreases by 2 when they have less than 50 turns left
  of Zot clock, and again when they have less than 10. Darkness
  is closing in...
- Meteorae glow in the dark. Permanent backlit status (not halo!):
  +enemy to hit, -stealth, disables invis. Suppressed in forms.
  Seems funny.

Credit to hellmonk for the initial version of this species and
pushing to make 'em happen. :)

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[bbdd37264c...](https://github.com/treckstar/yolo-octo-hipster/commit/bbdd37264cfd06583db5e8985af6b50f054172c3)
#### Saturday 2022-11-19 16:22:03 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [RigglePrime/tgstation](https://github.com/RigglePrime/tgstation)@[de662db397...](https://github.com/RigglePrime/tgstation/commit/de662db39763674f850977dabc8bbe66388d2c9b)
#### Saturday 2022-11-19 16:26:02 by Sol N

Excercise Equipment is now craftable (#71190)

## About The Pull Request

Imagine if you will a humble chaplain who wants nothing more than for
all of the spiritual folk on the station to get as massive gains as they
can, after finding that they can not just make more exercise equipment
and that the station does not have any in public places, they go annoy
security enough to get into permabrig only to find out that they cant
even unwrench the equipment and move it to the church!!!

NOT ANYMORE!!!


![jS2aBMBa0B](https://user-images.githubusercontent.com/116288367/200889423-f1b6365c-24c4-4f45-8ca4-c96c9085cf27.png)
crafting recipies


![dreamseeker_O4BgBRsFa8](https://user-images.githubusercontent.com/116288367/200889002-8dd7c927-0745-46a9-a4bc-578c7279042a.gif)
demonstrating unwrenching and wrenching equipment


![dreamseeker_hCFQJZdzoS](https://user-images.githubusercontent.com/116288367/200889019-5f4c8399-d539-4d84-8a3f-7735c3ba1f68.gif)
crafting a punching bag and punching it

Now you can craft as much exercise equipment as you want! May everyone
on the station get as strong as possible and not just prisoners.

Also I changed the message that plays when you try to use exercise
equipment someone else is using into a balloon alert.

![dreamseeker_PwNesmcR1f](https://user-images.githubusercontent.com/116288367/200890964-4f9fa3ee-ce07-4e6e-815c-a3f4593d06b1.png)

## Why It's Good For The Game

Access to exercise equipment on some maps is limited to static positions
and is currently mostly only for prisoners as every map does not have
public exercise equipment. Expanding the access means that you can have
a Drill Sargent Head of Security or Captain who commands people use
these or allows a psychologist to prescribe healthy exercise habits to
their patients.

I think having the potential for exercise equipment on every map is more
fun and also if prisoners get their hands on tools they should be
allowed to mess with these to annoy security or aid in their escape.

## Changelog
:cl:
add: the punching bag, bench press, and chest press are all able to be
crafted and unanchored.
add: crafting recipes for the above
qol: changed a chat message into a balloon alert
qol: adds screentips to equipment (thanks for suggesting i do this
mothblocks!)
/:cl:

---
## [vEnhance/dotfiles](https://github.com/vEnhance/dotfiles)@[33695efe0c...](https://github.com/vEnhance/dotfiles/commit/33695efe0cde416903e10b712784988845b92ccb)
#### Saturday 2022-11-19 16:51:07 by Evan Chen

Make CoC opt-in

Otherwise my laptop battery just kinda dies

not that tabnine isn't amazing at all

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[1ba95626a6...](https://github.com/Paxilmaniac/Skyrat-tg/commit/1ba95626a6614177da02665231900620bbaef2ce)
#### Saturday 2022-11-19 16:51:14 by SkyratBot

[MIRROR] mech bustin update 2022 [MDB IGNORE] (#17504)

* mech bustin update 2022 (#70891)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->
Adds a huge ass crowbar to robotics (the mech removal tool), it deals 5
damage unwielded, or 19 wielded. (should be fine, considering robotics
also has the easiest access to the materials needed for a chainsaw)
You can use it while wielded on mechs to break the occupants out. This
takes 5 seconds (or 3 in an unenclosed mech like a ripley)
When you die in a mech you no longer automatically get ejected.
refactors fire axe cabinets to support more items than the fireaxe
makes some vehicle code better
closes #70845 (you can still enter a mech without limbs, i think thats
fine because you can use it to protect yourself from death in a
dangerous situation or something until someone breaks you out with the
really large crowbar)
video: https://streamable.com/x4gom2

## Why It's Good For The Game

<!-- Argue for the merits of your changes and how they benefit the game,
especially if they are controversial and/or far reaching. If you can't
actually explain WHY what you are doing will improve the game, then it
probably isn't good for the game in the first place. -->
robotics having a giant ass crowbar to break people out of mechs seems
like a fun idea
you currently cant exit a mech if youre incapacitated inside it unless
you DIE

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

:cl: Fikou, sprites by Halcyon
refactor: fire axe cabinets support items that aren't fire axes
balance: mechs no longer eject you when you die in them
add: Adds a giant crowbar to robotics, it can break open mechs to eject
their pilots.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

* mech bustin update 2022

* vr for the love of god

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[317aea0435...](https://github.com/Paxilmaniac/Skyrat-tg/commit/317aea043510ee0c3591ff3a06fdffd360fdfc29)
#### Saturday 2022-11-19 17:08:09 by Jolly

[FUCK] [NO GBP] Yeah, fixes something in NuInterlink(?) (#17544)

fucking GODDAMNIT

---
## [vicirdek/PsychonautStation](https://github.com/vicirdek/PsychonautStation)@[3c187487b1...](https://github.com/vicirdek/PsychonautStation/commit/3c187487b1884040608ba23b0a89aa8b0176c2aa)
#### Saturday 2022-11-19 17:28:12 by MrMelbert

Renews a bunch of old roundend new reports that got lost. Plus, some roundend report QoL for cult and revs. (#71284)

## About The Pull Request

A few roundend reports got lost from moving to dynamic and other prs.
This PRs re-allows them to occur. Namely: "Wizard Killed" (lost in
dynamic), "Blob nuked" (lost in dynamic), "Cult escaped" (lost in cult
rework), and "Nuke Ops Victory" (station destroyed via nuke) (lost from,
what I can see, an oversight / accidental swap of report values).

Additionally, small roundend report QOL for cult: Removes antag datums
from spirit realm ghosts after being dusted, so they do not show up on
the report. And in reverse, heads of staff who were dusted / destroyed
in revolution rounds are now also shown in roundend reports.

## Why It's Good For The Game

Some of these reports are dead, which is is a shame because I think
they're cool and fun.

## Changelog

:cl: Melbert
qol: Successfully fending off a blob now has a cross station news report
again. More pressing reports will take priority over it, though.
qol: Successfully killing a wizard (and all of their apprentices) now
has a cross station news report again.
qol: If more than half of a cultist team manages to escape on the
shuttle (rather than summoning Nar'sie), they will send a unique cross
station news report. This is still a loss, by the way. Summon Nar'sie!
qol: Nuclear Operatives successfully nuking the station now has its
unique cross station news report again, and no longer uses the generic
"The station was nuked" report.
qol: Nuking the station to stop a blob infection now has a unique cross
station news report again. Good luck convincing admins to allow this.
qol: Cult ghosts from "Spirit Realm" no longer persist on the cult's
team after being desummoned, meaning they will not show up on roundend
report.
qol: Heads of staff will now always show up on revolution roundend
report - even if their body was fully destroyed.
/:cl:

---
## [Dev-msm8953/kernel_xiaomi_panda](https://github.com/Dev-msm8953/kernel_xiaomi_panda)@[caee48e2c0...](https://github.com/Dev-msm8953/kernel_xiaomi_panda/commit/caee48e2c09bf411b24faf0b715c5af2e6912b80)
#### Saturday 2022-11-19 18:03:40 by George Spelvin

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

---
## [Gay-Snake-Squad/Ted-Tweaks](https://github.com/Gay-Snake-Squad/Ted-Tweaks)@[acfa951ad5...](https://github.com/Gay-Snake-Squad/Ted-Tweaks/commit/acfa951ad5f620e982ca32a4567fa557539c5f0e)
#### Saturday 2022-11-19 19:14:19 by ted

- Boner: Use HDB_SCRAP instead of HDB_FRAG.

This makes it so you're not just fucked if you get hit by one with anything below a shieldcore/blue armor to my knowledge. Painful.

---
## [TurtleShroom/TSP_STORYTIME_RIDES_AGAIN](https://github.com/TurtleShroom/TSP_STORYTIME_RIDES_AGAIN)@[61c5cf4560...](https://github.com/TurtleShroom/TSP_STORYTIME_RIDES_AGAIN/commit/61c5cf4560e2c8c965b81b586d486171d3458a78)
#### Saturday 2022-11-19 20:04:40 by TURTLESHROOM

Minor

1. Added tab indentation for some file entries.

2. Spelling and punctuation corrections.

3. Herba is now slightly more addictive.

4. If you have the Halloween Parade Mod, Bean Bulborbs now come baring Jack-o-Lanterns.

5. Beetnikhs sometimes field Blue Heelers as guard dogs and attack hounds.

6. Reinstated hidden Bosses Faction, fixed errors concerning Boss icons and GUI graphics, prevented Bosses (which have no Pawn Kind Defs) from raiding, which causes errors.

7. If you have the Forg Mod, Frogmen will occasionally send Forg cannon fodder instead of Frogmen as Raiders.

8. Gnomes love candy and sometimes deploy Jack-o-Lanterns if you have the Halloween Mod.

9. Increased likelihood of Gnome Peasants appearing in some Pawn Group Types.

10. If you have the Witching Hour Mod, Jeubs will sometimes field Bats.

11. Skeleton Pirates can no longer siege.

12. Added missing Joy tables, so that Pawns will seek out Chocolate Bombs for recreation, like they do for Chocolate.

13. Fixed issue where seeking Chocchip Crunchies actually caused a Pawn to search for Toad Crunchies.

14. Added Joy tables for Gnome Cocktails, so that Pawns will seek and consume them for Recreation.

15. Slightly raised likelihood of Pawns consuming Pizza for Recreation.

16. Hhhite is now made with Peeled One Meat instead of their corpses.

17. You can now make Dried Frog Pills in batches of five hundred and one thousand.

18. Fixed Biome tables issue for the Embittered Bullfrog that caused the game to crash.

19. Fixed error where Wood Frogs would drop seeds that cause errors because it tries to search for a missing parent.

20. If you have the Hellsing Mod, Peeled Ones are now harmed more significantly by the Sanctification effect.

21. Added missing corpse image for Peeled Ones.

22. Reduced cool down times for Bean Bulborbs attacking with their feet.

23. Fixed Biome table errors for Parrots and Modest Parrots that were causing the game to crash.

24. If you have the Witching Hour Mod, the Spooky Skeletons are now classed as Pirate Skeletons.

25. Relocated Trader Kind Defs to appropriate folder in Mod folder tree, matching Ludeon's sortition.

26. Added infested House of the Worm as Orbital "Trader", which "sells" Worms,  Insect Meat, and Judas' Frogs.

27. Clarified the implied, but now explicit, right to create derivatives of the Storytime Mod and, in the case of the Mod's total abandonment, its revival.

28. Fixed missing MAYREQUIRE Tags for the Achievement that depends on the Vanilla Factions Medieval Expanded Mod.

29. Fixed error in the Patch that adds Pirate apparel, where the Patch would fail for certain articles of clothing.

30. Fixed issue where Gnome Caravans were not spawning if you had the Strawberry Animals or Cringe Wonka Mods.

31. Fixed error where, if you have the Vanilla Plant Expanded Mod, the removed (duplicate) Orange Trees from that Mod still existed in certain Biome tables.

32. Fixed graphical error for the Herba Cigarillo boxes. Now a full stack should have a closed box.

---
## [QAI-07/NSV13](https://github.com/QAI-07/NSV13)@[be0bf5b756...](https://github.com/QAI-07/NSV13/commit/be0bf5b75601e30144d635cf9de2a4d8ac3eb724)
#### Saturday 2022-11-19 20:27:43 by QAI-07

Adds NSV-Specific Humanoid Simplemob icons

Oh hell yeah boys

---
## [Bobbanz1/NSV-Rat](https://github.com/Bobbanz1/NSV-Rat)@[e8be775da4...](https://github.com/Bobbanz1/NSV-Rat/commit/e8be775da4892a20186105a69bdc8b0832fba1cb)
#### Saturday 2022-11-19 21:11:45 by Paxilmaniac

Adds a collection of some kinda random greyscaled, recolorable clothes options (#16961)

* that's a few dmis

* a few sprite changes

* i hate making greyscale configs

* oh the misery

* 2:29 AM

* a few small things

* adds the stuff around more

* amazing work boss, this is why you're the best

---
## [ctm/Bataan-Memorial-Death-March](https://github.com/ctm/Bataan-Memorial-Death-March)@[13b19251bd...](https://github.com/ctm/Bataan-Memorial-Death-March/commit/13b19251bd3b21fa4ea42e16a0bfb2234ac7904e)
#### Saturday 2022-11-19 21:25:41 by Clifford T. Matthews

Includes my La Luz Pack Run from earlier today.

I got nervous about it being 22F at the start and compensated in way
too many ways, which wound up causing me to overheat.  On top of that,
my left knee is still not fully recovered from the spill I took at the
Big Cottonwood Marathon on September 11th.  To make matters worse, I
tripped in the snow at the beginning of my descent.  It was a slow
fall and I didn't hurt myself, per-se, but one of my water bottles
that I use for weight popped out which meant I needed to take my pack
off to put it back in.  Since I was taking my pack off anyway, I also
stripped my inner long-sleeve JJ100 shirt, but in doing so I also
stripped the two panty liners I was using to lessen chafing.

So, with the huge pause to monkey around with my pack, my bum knee and
the chafing, my descent was ridiculously slow, which was especially
frustrating since I think I nailed my caffeine and calorie intake.

The nice thing is this leaves a huge amount of room for improvement.
However, with me running the Tucson Marathon on December 10th, I'm not
currently scheduled to do another La Luz Pack Run until December 24th.
I think I need to add a redo sometime between now and then.

---
## [teia-community/teia-report](https://github.com/teia-community/teia-report)@[73907b4ba9...](https://github.com/teia-community/teia-report/commit/73907b4ba9ea66f13945bf4c4311a36b57cdbf60)
#### Saturday 2022-11-19 21:28:38 by copyminter

ban 🚫: tz2Eksww9UQEkiKQ39sUoUuSJcAbCwN47tws

filtered 3rd party nsfw material 
II https://objkt.com/asset/hicetnunc/796503 >> https://el.xcyvv.com/rinna-ly-is-a-stunning-redhead-as-she-leaves-nothing-on-but-high-heels-and-show-off-her-trimmed-pussy-and-sexy-ass-in-metart-set-appassionata/?lang=pt
II https://nudecollect.com/content/Femjoy_Anabelle_All_I_Can_Do_4000_Pix_99_Jpg_12_02_2012_68308788/page-2-pics-101-mirror-36.html >> https://objkt.com/asset/hicetnunc/796502
II minting photos of banksy pieces while giving wrong info in the description, presumably trying to profit off the UA war: https://www.tmoua.org/banksy-street-art-collection >> https://objkt.com/asset/hicetnunc/795784

Banned by zackundweg

---
## [odoo-dev/odoo](https://github.com/odoo-dev/odoo)@[e7c8fed8e3...](https://github.com/odoo-dev/odoo/commit/e7c8fed8e373d7005c16c88d3a7bad6f425d13e5)
#### Saturday 2022-11-19 22:56:20 by qsm-odoo

[FIX] website, *: allow to re-edit company team snippet images

*: web_editor

Since [1], it was not possible to edit a company team snippet image
anymore as soon as the page was saved once. Indeed that commit added
o_not_editable/contenteditable="false" on the parent column to make sure
no text can be added in that column and contenteditable="true" on the
images so that they are still editable (even though HTML-specs-wise
adding contenteditable="true" on images probably does not mean much as
images are self-closing tags, our editor understand that as the ability
to edit the image anyway). That contenteditable="true" part is however
removed when leaving edit mode... and was not restored upon entering
edit mode again.

This fixes the problems with an ugly patch. We'll review what to do in
master.

Funny enough, that bug was actually gone in 15.0... by mistake. A recent
bug fix actually reintroduced that isolated bug at [2] (by reintroducing
the fact that images in a non-editable environment are not possible to
edit). The 3 opened tickets this commit mentions were actually reported
for 15.0 immediately after that, while the 14.0 being broken about this
since the beginning apparently did not bother anyone.

[1]: https://github.com/odoo/odoo/commit/656cac1bf21c7c5a56aa569008aac58436c747fb
[2]: https://github.com/odoo/odoo/commit/e113bae04a64a8bd341a80736086ab7c25079dd3

opw-3031217
opw-3032482
opw-3035289

closes odoo/odoo#104156

Signed-off-by: Romain Derie (rde) <rde@odoo.com>

---
## [DavidAHazra/SenseAndSensibility](https://github.com/DavidAHazra/SenseAndSensibility)@[fc8fae5887...](https://github.com/DavidAHazra/SenseAndSensibility/commit/fc8fae58870d50c61a85c6ae37ce15f112ccffe8)
#### Saturday 2022-11-19 23:42:56 by Thomas Bowers

Merge pull request #10 from DavidAHazra/Tom

fuck you david

---
## [majacQ/nss](https://github.com/majacQ/nss)@[d96a53efa3...](https://github.com/majacQ/nss/commit/d96a53efa3176c25710bd8495f0e17837f6a1969)
#### Saturday 2022-11-19 23:45:41 by Martin Thomson

Bug 1713562 - Validate ECH public names, r=bbeurdouche

This validates that they are LDH (with underscore because we don't hate
freedom), but that they are not IP addresses.  This invokes the horrible WhatWG
IP parsing routines, so that it recognizes a vast array of crazy address formats
(thanks 1980s design).

Differential Revision: https://phabricator.services.mozilla.com/D116343

--HG--
extra : source : 27c19f19a885b7381fb263b1a56f88025b24e488
extra : amend_source : 8d6852c85e9d5e06e48228723edb144ffc64cc8f

---

