## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-12-17](docs/good-messages/2023/2023-12-17.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,197,044 were push events containing 2,916,759 commit messages that amount to 158,576,217 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 51 messages:


## [gs-bluraviole/android_kernel_google_gs101](https://github.com/gs-bluraviole/android_kernel_google_gs101)@[a58d09f8ea...](https://github.com/gs-bluraviole/android_kernel_google_gs101/commit/a58d09f8ea3e6125ef6660024efd5118d2f9964b)
#### Sunday 2023-12-17 00:30:27 by Sultan Alsawaf

fs: Block various userspace bloatware services from running

Unfortunately, there are several bloatware services that do not cope well
with their kernel interfaces disappearing. Furthermore, there are other
services that are nasty for different reasons and should be disabled.

Namely, twoshay/IInputProcessor cannot cope with touch offload/heatmap
functionality missing in the kernel, and needs to be disabled via VINTF to
use a kernel without touch offload/heatmap.

Additionally, dmd randomly started burning 100% on my device for several
days, generating a whopping 25 GiB of modem logs under /data/vendor/slog
which cannot be deleted without root privileges. Pixel's custom dumpstate
turned out to be the culprit, because it uses persist props to kick off
logging when dumping is requested, but won't get a chance to unset those
persistent props if the device reboots during a dump.

So, these services are absolutely awful and deserve a solid thumping from
the Big Hammer TM.

But there's no way to disable them from the kernel without ungodly VFS
hacks, so that's where we're left: killing poison with poison.

Aarqw12 : updated list for gs101:

twoshay/IInputProcessor is no killed as offload/heatmap
functionality is here

dumpstate is no killed as developpers settings crash without it.

Signed-off-by: Sultan Alsawaf <sultan@kerneltoast.com>

---
## [ArcaneMusic/TG-Station-Arcane-Remix](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix)@[f03084c1ca...](https://github.com/ArcaneMusic/TG-Station-Arcane-Remix/commit/f03084c1ca61511b6c426602121a942966c2e76d)
#### Sunday 2023-12-17 01:01:29 by LemonInTheDark

FOV is Dead (Long Live FOV) (#80062)

## About The Pull Request

FOV as it is currently implemented is incompatible* with wallening.
I'm doin wallening, so we gotta redo things here.

The issue is the masking of mobs. Wallening relies on sidemap (layering
based off physical position), which only works on things on the same
plane (because planes are basically sheets we render down onto)
So rather then masking mobs, let's reuse the masking idea from old fov,
and use it to cut out a bit of the game render plane, and
blur/over-saturate the bit that's masked out.

My hope is this makes things visible in light, but not as much in
darkness, alongside making more vivid shit more easily seen (just like
real life)

Here's some videos, what follows after is the commits I care about
(since I had to rip a bunch of planes to nothing, so the files changed
tab might be a bit of a mess)

Oh also I had to remove the darkness pref since the darkness is doing a
lot of the heavy lifting now. I'm sorry.

Edit:
NEW FOV SPRITES! Thanks dongle your aviator glasses will guide us to a
better future.


https://github.com/tgstation/tgstation/assets/58055496/afa9eeb8-8b7b-4364-b0c0-7ac8070b5609


https://github.com/tgstation/tgstation/assets/58055496/0eff040c-8bf1-47e4-a4f3-dac56fb2ccc8

## Commits I Care About

[Implements something like fov, but without the planes as layers
hell](https://github.com/tgstation/tgstation/commit/a604c7b1c8d74cd27af4d806d85892c1f7e35ba8)

Rather then masking out mobs standing behind us, we use a combo color
matrix and blur filter to make the stuff covered by fov harder to see.

We achive this by splitting the game plane into two, masking both by fov
(one normally and one inversely), and then applying effects to one of
the two.

I want to make the fov fullscreens more gradient, but as an effect this
is a good start

[Removes WALL_PLANE_UPPER by adding a WALL_PLANE overlay to material
walls (init cost comes
here)](https://github.com/tgstation/tgstation/commit/25489337392f708cb337fbf05a2329eacdfc5346)

@Mothblocks see this. comment in commit explains further but uh, we need
to draw material walls to the light mask plane so things actually can be
seen on them, but we can't do that and also have them be big, so they
get an overlay. Sorry, slight init time bump, about 0.5 seconds. I can
kill it with wallening.

[Moves SEETHROUGH_PLANE above
ABOVE_GAME_PLANE](https://github.com/tgstation/tgstation/commit/beec4c00e01d34a04fba7c2bb98a9b70d27ead82)

I don't think it actually wants to draw here
@Time-Green I think this was you so pinging for opinion

[Resprites FOV masks to be clean (and more
consistent)](https://github.com/tgstation/tgstation/pull/80062/commits/f02ad13696b3b17658af612c62848b48609d785d)

[f02ad13](https://github.com/tgstation/tgstation/pull/80062/commits/f02ad13696b3b17658af612c62848b48609d785d)

This is 100% donglesplonge's work, he's spent a week or so going back
and forth with me sharpening these to a mirror shine, real chill

## Why It's Good For The Game

Walls are closing in

## Changelog
:cl: LemonInTheDark, Donglesplonge
image: Redoes fov "mask" sprites. They're clean, have a very pleasant
dithering effect, and look real fuckin good!
del: Changed FOV, it no longer hides mobs, instead it blurs the hidden
area, and makes it a bit darker/oversaturated
/:cl:

###### * It's technically possible if we start using render targets to
create 2 sets of sources but that's insane and we aren't doing it

---
## [Mu-L/crawl](https://github.com/Mu-L/crawl)@[5f6fb4f5a3...](https://github.com/Mu-L/crawl/commit/5f6fb4f5a389a722ff4ee7fd78d4e43f979cce6c)
#### Sunday 2023-12-17 01:04:29 by regret-index

Add and trim a few Xom spells and cloud trails.

New spells: Wereblood, Animate Armour, Battlesphere, Malign Gateway.
Wereblood forces the player to make noise and thus is neat as a mixed
blessing, Animate Armour gets to by-pass its innate castability versus
armour weight issues to be more interesting as a random free god act,
Battlesphere makes for a decent joke if not actually usable and compensates
for the power of the two summons here, Malign Gateway has been missing
since the miscast streamlining and is extremely appropriate between the
chaos brand and unavoidable neutrality.

(These all are exchanged for Canine Familiar, which can't use one of its
most interesting aspects in the recast and thus will mostly make players
unavoidably get drained and guilt.)

New cloud trail clouds are salt and blastmotes, both at miniscule chances.
The salt's purpose is obvious, while the blastmotes are manually set at 25
power (power with those is weird and modular) and definitely give a certain
kind of danger and excitement very distinct from the spell by getting them
without having to stop for laying each of them.

---
## [YakumoChen/Bubberstation](https://github.com/YakumoChen/Bubberstation)@[2e656fba14...](https://github.com/YakumoChen/Bubberstation/commit/2e656fba14e0b67086bb4d2eff59d6fa6748a55c)
#### Sunday 2023-12-17 01:08:57 by Cursor

Grants the ability to open Clown slots once more. (#853)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Title. Skyrat disabled it because they hate fun. We don't.

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Say a Clown dies. Is arrested, or is just a bit shit.
What can you do?
Jackshit.
Pray, fax Clown Planet, but why wait on God or the Clown in the High
Castle when you can do it yourself?
This also let's Antags, or Clowns summon more friends. Assuming people
in the lobby wanna be a clown.

P.S. I commented out and unticked the Skyrat file for double safety.
Tried to just override it, didn't work. If you have a better idea for
this. You have the floor.

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
add: Clown slots are re-openable by royal decree. The incident between
Nanotrasen and King Honkington has been resolved.
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

---------

Co-authored-by: Waterpig <49160555+Majkl-J@users.noreply.github.com>

---
## [perssphere07/The-Powder-Toy](https://github.com/perssphere07/The-Powder-Toy)@[fb9cba0d01...](https://github.com/perssphere07/The-Powder-Toy/commit/fb9cba0d01b211a949bc36a3cfc8e70a07f0b6b4)
#### Sunday 2023-12-17 01:14:29 by Tamás Bálint Misius

Some native clipboard support for some platforms

I was hoping SDL2 would get this functionality eventually, but nope, proper clipboard support is staged for SDL3, which we're not going to see much of for at least a few more months. This will have to do for 98.0. The feature can be disabled at runtime from powder.pref.

Implementation status:

 - windows (via winapi): has the most friendly api so of course the implementation is flawless and uses every available optimization >_>
 - macos (via cocoa): I'm bad at cocoa so this is only as good as absolutely necessary; TODO: on-demand rendering
 - x11 (via xclip): I am NOT implementing icccm2; TODO: remove reliance on external tools
 - wayland (via wl-clipboard): oh god wayland oh why, you're almost as bad as x11; TODO: remove reliance on external tools
 - android: TODO; is there even a point?
 - emscripten: TODO; the tricky bit is that in a browser we can only get clipboard data when the user is giving it to us, so this will require some JS hackery that I'm not mentally prepared for right now; also I think the supported content types are very limited and you can't just define your own

x11 and wayland support are handled by a common backend which delegates clipboard management to xclip-like external programs, such as xclip itself or wl-clipboard, and can load custom command line templates from powder.pref for use with other such programs.

---
## [BankVana/Onion](https://github.com/BankVana/Onion)@[c7694511f2...](https://github.com/BankVana/Onion/commit/c7694511f224fe469f97b98308a9dcfb6fb13917)
#### Sunday 2023-12-17 01:24:47 by XK

FEAT: Update ScummVM Standalone to 2.9.0git (#1307)

## Overview
Update to scummvm 2.9.0 to include all updates & fixes to the scrollbars
in: https://github.com/scummvm/scummvm/pull/5472

<img
src="https://github.com/OnionUI/Onion/assets/47260768/89080ee6-124e-445a-a14d-b818e277e991"
width="400" alt="Run ScummVM_000"><img
src="https://github.com/OnionUI/Onion/assets/47260768/86848e29-a304-4c9e-ae1f-1c4d491d044a"
width="400" alt="Run ScummVM_001">

## To test

Testing GUI -> 640 x 480: 

- [x]  GUI can be freely scaled to its smallest size

Testing scrollbars:

- [x] Open global options -> Keymaps & observe a scrollbar is still
present

Downscaler can be tested by running BSword2.5. 
Audio has been handled differently so in this PR will also change the
launch scripts to preload libpadsp.so

## Build details
<details>

```markdown
Backend... miyoo (SDL 1.2.15), 16bit color, high resolution, TinyGL, savegame timestamp, HQ and Edge scalers, aspect ratio correction, Lua, virtual keyboard, ENet
WARNING: Disabling engine Hpl1 because the following dependencies are unmet: OpenGL with shaders
WARNING: Disabling engine Tetraedge because the following dependencies are unmet: libtheoradec
WARNING: Disabling engine The Watchmaker because the following dependencies are unmet: OpenGL (classic)

Engines (builtin):
    SCUMM [all games]
    Access
    ADL
    AGI
    AGOS [all games]
    Adventure Game Studio
    Sanitarium
    Lord Avalot d'Argent
    Beavis and Butthead in Virtual Stupidity
    Blade Runner
    The Journeyman Project 2: Buried in Time
    CGE
    CGE2
    Chamber
    Chewy: Esc from F5
    Cinematique evo 1
    Magic Composer
    Crab
    Cinematique evo 2
    Lost Eden
    Cryo Omni3D games [all games]
    Macromedia Director
    Dungeon Master
    Dragon History
    Blazing Dragons
    Drascula: The Vampire Strikes Back
    Dreamweb
    Escape From Hell
    Freescape
    Glk Interactive Fiction games
    UFOs
    Gobli*ns
    The Griffon Legend
    Grim [all games]
    Groovie [all games]
    Hades Challenge
    Hyperspace Delivery Boy!
    Hopkins FBI
    Hugo Trilogy
    Hypnotix Inc.
    In Cold Blood
    Illusions Engine
    The Immortal
    Kingdom: The Far Reaches
    Kyra [all games]
    Labyrinth of Time
    The Last Express
    Lilliput
    Lure of the Temptress
    MacVenture
    MADE
    MADS [all games]
    Might and Magic [all games]
    Mohawk [all games]
    Mortevielle
    mTropolis
    Mutation of JB
    Myst 3
    Nancy Drew
    Neverhood
    Nikita Game Interface
    Parallaction
    The Journeyman Project: Pegasus Prime
    Red Comrades
    Pink Panther
    Playground 3d: the testing and playground environment for 3d renderers
    Plumbers Don't Wear Ties
    The Prince and The Coward
    Private Eye
    Flight of the Amazon Queen
    SAGA [all games]
    SAGA2
    SCI [all games]
    The Lost Files of Sherlock Holmes
    Beneath a Steel Sky
    Sludge
    The Longest Journey
    Star Trek 25th Anniversary/Judgment Rites
    Mission Supernova
    Broken Sword
    Broken Sword II
    Broken Sword 2.5
    Teen Agent
    TestBed: the Testing framework
    Tinsel
    Starship Titanic
    3 Skulls of the Toltecs
    Tony Tough and the Night of Roasted Moths
    Toonstruck
    Touche: The Adventures of the Fifth Musketeer
    Trecision Adventure Module
    TsAGE
    Bud Tucker in Double Trouble
    Little Big Adventure
    Ultima [all games]
    V-Cruise
    Voyeur
    WAGE
    Wintermute [all games]
    Z-Vision

Engines Skipped:
    Hpl1
    Tetraedge
    The Watchmaker

WARNING: This ScummVM build contains the following UNSTABLE engines:
    Lord Avalot d'Argent
    Chamber
    Crab
    Lost Eden
    Dungeon Master
    Grim [Escape from Monkey Island]
    In Cold Blood
    The Immortal
    The Last Express
    Lilliput
    MacVenture
    MADS [MADS V2]
    Might and Magic
    Mohawk [Where in Time is Carmen Sandiego?]
    Mutation of JB
    Playground 3d: the testing and playground environment for 3d renderers
    Sludge
    Star Trek 25th Anniversary/Judgment Rites
    TestBed: the Testing framework
    Ultima [Ultima I - The First Age of Darkness]
    WAGE
    Wintermute [Wintermute3D]

Creating engines/engines.mk
Creating engines/detection_table.h
Creating engines/plugins_table.h
Creating config.h
Creating config.mk

```
</details>

---
## [minetest-game-mod/beds](https://github.com/minetest-game-mod/beds)@[ac2ca2e9b8...](https://github.com/minetest-game-mod/beds/commit/ac2ca2e9b8097585358746c7ec1442bb7c50343b)
#### Sunday 2023-12-17 01:38:16 by Yaya - Nurul Azeera Hidayah @ Muhammad Nur Hidayat Yasuyoshi

Update Malay translations
1. Added missing translation to the following files:
  beds.ms.tr, creative.ms.tr, default.ms.tr, farming.ms.tr,
  fire.ms.tr, sethome.ms.tr
2. Changes some translation as per following:
  a. beds.ms.tr
    - Leave Bed changed from Bangun (wake up) to Tinggalkan Katil
      (leave bed, in literal sense) just because the button would
      be interpreted by some people as 'wake up on next morning'
      (ie. skipping night) instead of 'wake up interrupting current
      sleep progress' which is the intended meaning.
  b. boats.ms.tr
    - Boat cruise mode changed from Mod bot layar makan angin to
      Mod jelajah bot, the original translation is more like direct
      translation, and this has been changed to more natural one
      to make sure player know that the mode is a cruise control.
    - Reset changed from Set semula to Tetap semula, this is for
      standardizing with existing term used in various places.
  c. default.ms.tr
    - Page \@1 of \@2 changed from the short form to the long form.
    - Mese Crystal Fragment had missing word 'Kristal' re-added.
  d. dye.ms.tr
    - Dark Grey changed from Kelabu Gelap to Kelabu Tua to make it
      standardized with the colour name elsewhere.
    - Dark Green changed from Hijau Gelap to Hijau Tua to make it
      standardized with the colour name elsewhere.
    - Magenta changed from Merah Lembayung to Magenta, because the
      colour Merah Lembayung is now used to refer to purplish red
      and no longer equal to magenta, the loanword is used instead.
  e. game_commands.ms.tr
    - respawn changed from lahir semula (reborn) to jelma semula
      (reappear), this is to make it consistent with the language
      used in multiple other games that had similar respawning
      system, and avoiding the religious context of life that is
      implied by the use of previous translation.
    - spawnpoint changed from titik permulaan (starting point) to
      titik jelma ((re)appear point), see previous point.
  f. tnt.ms.tr
    - Gun Powder changed from Serbuk Senjata Api (firearms powder)
      to Serbuk Letupan (explosion powder) because that is the
      proper translation, the latter is still the term used even
      when talking about actual firearm, the former didn't exist
  g. vessels.ms.tr
    - item changed from barang (thing) to item, this is mainly
      because some of the 'item' that could be stored are not
      some solid 'thing' where the word barang could be used for,
      so using the word item here keep it neutral.
  h. wool.ms.tr
    - Dark Grey changed from Kelabu Gelap to Kelabu Tua to make it
      standardized with the colour name elsewhere.
    - Dark Green changed from Hijau Gelap to Hijau Tua to make it
      standardized with the colour name elsewhere.
    - Magenta changed from Merah Lembayung to Magenta, because the
      colour Merah Lembayung is now used to refer to purplish red
      and no longer equal to magenta, the loanword is used instead.

---
## [CorrodedCoder/Blades-of-Exile](https://github.com/CorrodedCoder/Blades-of-Exile)@[d24a47970f...](https://github.com/CorrodedCoder/Blades-of-Exile/commit/d24a47970f4c78a2dcab682555b83a3934fc2748)
#### Sunday 2023-12-17 02:54:34 by CorrodedCoder

Support linux + clang building dump utilities (#39)

* Get utilities building under Linux + Clang

A number of tweaks were needed here:
1. Gcc/Clang x64 are LP64 compilers in that longs and pointers are 64-bit when compiling for that target platform. Windows is a P64 only. The problem here was that the types were marked as `long` in the part_record_type structure which meant they were 64-bit when compiling with Clang, so they have been changed to `int` which means they are regarded  as 32-bit. I may consider moving these types to fixed width types (i.e. `std::int32_t`) as long as they are being directly serialized in this way as it would be a more clear statement than the static_assert on size. As it stands, if we compiled on an ILP64 platform, we'd be in trouble as `int` would also be 64-bit.
2. Some additional headers are needed and modern clang is very good at holding us to account.
3. I had cheated a little with the boe_error, leveraging a sneaky detail of Visual Studio headers which provides an implementation of `what` which one can leverage. However that is not standard, so let's do it the right way.

* Re-org to enable more fine grained project settings

Essentially I wanted to be able to enable higher warning levels for new common code than existing code so that I can keep myself honest. The way it was working allowed me to introduce new issues that I would not spot, so I want these new utilities compiling with very high warning levels.
This really required some overdue re-org moving common code up and out of the Windows subdirectory.
We end up with the top level CMakeLists.txt now setting only common flags or settings and having the Windows subdirectory CMakeLists.txt disabling a lot of warnings, whilst the utilities ones can maximize them.

* Spotted a couple of arrays that were still being explicitly swapped item by item rather than allowing the generic array algorithm handle it.

---
## [KenAdeniji/WordEngineering](https://github.com/KenAdeniji/WordEngineering)@[dcf7218699...](https://github.com/KenAdeniji/WordEngineering/commit/dcf721869979a8fdfb7be2755fd02c468d66a441)
#### Sunday 2023-12-17 03:20:29 by Ken Adeniji

			<table id="WhatDoesHeInvolve" datetime="2023-12-16T18:45:00">
				<thead>
					<caption>
						<a
							href="http://e-comfort.ephraimtech.com/WordEngineering/WordUnion/GetAPage.html?word=What%20does%20He%20involve%3F"
							datetime="2023-12-16T18:45:00"
							data-HisWordID="159009"
							data-ContactID="5080"
							data-Location="Charter Square. Dulhan Grocery. 34139 Fremont Boulevard. Fremont, California (CA) 94555"
						>
							What does He involve?
						</a>
					</caption>
					<tr>
						<th>Word</th>
						<th>Actor</th>
						<th>Scripture Reference</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>Holy Spirit and people</td>
						<td>
							<a
								href="http://e-comfort.ephraimtech.com/WordEngineering/WordUnion/BibleWord.html?bibleWord=Adam"
							>
								Adam
							</a>
						</td>
						<td>
							<a
								href="http://e-comfort.ephraimtech.com/WordEngineering/WordUnion/ScriptureReference.html?scriptureReference=Genesis%202:7,%20Genesis%202:20-25,%20Genesis%204:25-26"
							>
								Genesis 2:7, Genesis 2:20-25, Genesis 4:25-26
							</a>
						</td>
					</tr>
					<tr>
						<td>After God's own heart</td>
						<td>
							<a
								href="http://e-comfort.ephraimtech.com/WordEngineering/WordUnion/BibleWord.html?bibleWord=David"
							>
								David
							</a>
						</td>
						<td>
							<a
								href="http://e-comfort.ephraimtech.com/WordEngineering/WordUnion/ScriptureReference.html?scriptureReference=1%20Samuel%2013:14,%20Acts%2013:22,%201%20Samuel%2025:3"
							>
								1 Samuel 13:14, Acts 13:22, 1 Samuel 25:3
							</a>
						</td>
					</tr>
				</tbody>
			</table>

---
## [k1n9bur93r/k1n9bur93r.github.io](https://github.com/k1n9bur93r/k1n9bur93r.github.io)@[a46ef321aa...](https://github.com/k1n9bur93r/k1n9bur93r.github.io/commit/a46ef321aa13f95217b2eee894176d9882555ddd)
#### Sunday 2023-12-17 04:51:45 by k1n9bur93r

Blog entry: 
---12/16/23
Brooklyn bowl!
Being social and shit
Gonna see an actual concert soon, kinda rare I think the last time was def over a year ago. Obvi festivals don’t count. Should be hyped, if my back can withstand all the waiting around haha

---
## [unbl0ck/unbl0ck.github.io](https://github.com/unbl0ck/unbl0ck.github.io)@[ac3796a356...](https://github.com/unbl0ck/unbl0ck.github.io/commit/ac3796a3568c08638c2dc9e277842b03c10d1267)
#### Sunday 2023-12-17 05:59:22 by Christian Santangelo

deleted. gone. dead. poof.

really fuckin buggy. github lfs too big for my brain, and its giving me a shit ton of errors when cloning.

---
## [rHermes/adventofcode](https://github.com/rHermes/adventofcode)@[dfcd8c2eef...](https://github.com/rHermes/adventofcode/commit/dfcd8c2eefd71c1312f95c06c9d14c96c8374570)
#### Sunday 2023-12-17 05:59:37 by Teodor Spæren

2023 Day 17

Well, well, well, well, Dijkstra's algorithm makes it first appearance
of the year and it's actually a bit exciting this time!

I realized there would be some sort of graph solution here quite
quickly, but I spent a bit of time fiddling to implement the algorithm.
I had to google it as usual, I never remember the implementation
immediately.

I ended up thinking of the nodes as dependent on:

(position, traveling directions, steps traveled in this direction)

With these 3 dimensions, we are free to explore the full potential
range.

The algorithm would be to just for each node, I would generate a list of
possible next nodes, one being going further ahead the current
direction, if the number of steps where less than 3 and the rest with 0
steps, but the directions being left and right.

I made some small mistakes in implementation. One was not filtering out
the current direction in the "all other directions" step, I only
filtered out the opposite direction.

Another mistake was that I was allowing the bot to go 4 steps, not 3.

The other was that I set the destination as (Y,X) when it should have
been (Y-1,X-1) of course. This was the biggest time waste, as it forced
me to implement debug printing, with the "prev". This wasn't so bad
though, as it caught the two previous mistake actually.

For part two, I just had to add an "if" around the other directions
part, so we only added them after having walked 4 steps.

The current solution is slow, and there are some obvious improvements
that could be made, at least for part 2. I could skip the first 4 steps
and just jump immediately the minimum 4 steps. This would cut out a lot
of small steps.

A* could also potentially speed this up a bit, let's see!

The biggest improvement of course, would be to reduce the dimensions.

Score:
      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
 17   00:36:31    903      0   00:39:12    644      0

---
## [Bubberstation/Bubberstation](https://github.com/Bubberstation/Bubberstation)@[fa8399334f...](https://github.com/Bubberstation/Bubberstation/commit/fa8399334f9bc10abbf6ddf25b40e43b5363a9ae)
#### Sunday 2023-12-17 06:02:46 by The-Sun-In-Splendour

Horrorform changeling salt PR (#859)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Now okay. I get it. It's huge, it's obvious, it's slow... I don't care
if it has more health and sustain than a tank spider or blobbernaut.
What I care is that it can fit into vents.

You can kill a changeling horror form with enough manpower. It's hard
but it's doable. But the fucking fact it can just... Ventcrawl into any
vent and if you don't see the tiny icon during the shitshow and push it?
Sorry but that is just absolute aids gameplay. Usually the monsters with
ventcrawl are pretty weak to make up for it. But not horrorling. I'm
sorry but if you have;

1. 750 health
2. 40 fucking damage swings (A double esword is 34 damage)
3. Passive, CONSTANT life regen
4. Lifesteal off dead bodies

You do **_not_** need ventcrawl. 

## Why it's good for the game

Do I really need to explain why having this almost unkillable machine be
able to ventcrawl to escape practically every situation because "teehee
forgot to weld vent in obscure location!" is bad for the game?

Yes. This is a salt PR.

:cl:
balance: Horror ling cannot ventcrawl anymore
/:cl:

---
## [jlsnow301/tgstation](https://github.com/jlsnow301/tgstation)@[b7b0932c4b...](https://github.com/jlsnow301/tgstation/commit/b7b0932c4b5b3d4f9386b6dce514ee1ba3e25a05)
#### Sunday 2023-12-17 06:20:20 by distributivgesetz

Delamination variants are now locked in after the countdown is reached (#80324)

## About The Pull Request

Does what it says on the tin.
## Why It's Good For The Game

This effectively changes one and only one thing: 

The "All Within Theoretical Limits" achievement is easier/fairer to get
with this. Previously, if you edged a crystal with the gas composition
method to get a resonance cascade, you had to make sure that your gas
composition stayed until it left the explosion point, which made the
achievement extremely finnicky and unfun to get this way. Regular
delaminations won't really be affected, because yeah. It's at the
explosion point. What are you going to do about it?

This makes the achievement easier to cheese, but honestly, in my opinion
as person who added the achievement, meh. If people feel like this isn't
good for the achievement, say something in the comments.

Closes #79528

## Changelog
:cl:
balance: Delamination variants no longer change once the explosion point
has been reached.
/:cl:

---
## [linux-kdevops/kdevops](https://github.com/linux-kdevops/kdevops)@[998aa3aeec...](https://github.com/linux-kdevops/kdevops/commit/998aa3aeec5ea283c9adada31dbe0b41361ee0f3)
#### Sunday 2023-12-17 06:53:16 by Luis Chamberlain

kdevops: add support for remote journals

It is a royal pain to debug nodes either hosted virtually or on the
cloud when doing kernel testing. Consoles have helped but in order to
scale and increase automation we need to instead start dumping our
journals over the wire on the fly because many times a crash can
leave a host really inaccessible even with libvirt virsh console.

Since most modern distros use systemd, leverage systemd journal for
this exact purpose as it already has a built-in mechanism for this
[0] [1] [2].

So we add a few new commands:

make journal-server      - Setup systemd-journal-remote on localhost
make journal-client      - Setup systemd-journal-remote on clients
make journal-ls          - List journals available and sizes
make journal-ln          - Add symlinks with hostnames

The last one is needed because even if we install libvirt-nss [4] on
the host and use it on nsswitch.conf we still cannot get the host
to do reverse lookups. It seems one option may be modifying the
network XML but for that we can look towards libguest instead to
correct this on new bring ups.

If you are struggling with getting crashes from nodes and you already
had a big cluster running, don't be afraid, just git pull and enable
CONFIG_DEVCONFIG_ENABLE_SYSTEMD_JOURNAL_REMOTE and ensure that
CONFIG_DEVCONFIG_SYSTEMD_JOURNAL_REMOTE_URL is correct, and then run:

make
make journal-server journal-client

Give it a few, and after a while:

make journal-ls

Once you see the count matches your nodes, use the final hack to
get real hostname symlinks for them:

make journal-ln

And hack away now!

[0] https://www.freedesktop.org/software/systemd/man/latest/systemd-journal-remote.service.html
[1] https://www.freedesktop.org/software/systemd/man/latest/systemd-journal-upload.service.html
[2] https://www.freedesktop.org/software/systemd/man/latest/journal-upload.conf.html
[4] https://libvirt.org/nss.html

Signed-off-by: Luis Chamberlain <mcgrof@kernel.org>

---
## [ubccsss/ubccsss.org](https://github.com/ubccsss/ubccsss.org)@[def4f73e35...](https://github.com/ubccsss/ubccsss.org/commit/def4f73e3584518e7ba58fdd8cc6f3760419df0e)
#### Sunday 2023-12-17 07:59:46 by csssbot

New review for CPSC 310 by quartz imaging is a gift that keeps on giving (#554)

> Your experience in this course is entirely contingent on whether or
not your project partner is garbage or not. My team got split at c2 and
we each soloed our project from there because he just wasn't doing
anything. The project is also a lot of work and is completely disjoint
from examinable lecture material. The exams are true false, if you want
to see your result, you have to book a 10 minute quiz viewing session
(you are not allowed to take notes there). Lecture content isn't
terrible - it's just memorization.

First week is hell. You have to write unit tests to catch all mutants
(buggy versions of their code). The autograder has a 12 hour cooldown.
It's not unheard of for students to set alarms in the middle of the
night to run it because the deadline is so tight.
>
> Difficulty: 2/5
> Quality: 2/5
> <cite><a href=''>quartz imaging is a gift that keeps on giving</a>,
Dec 15 2023, course taken during 2023W1</cite>
<details><summary>View YAML for new review</summary>
<pre>
  - author: quartz imaging is a gift that keeps on giving
    authorLink: 
    date: 2023-12-15
    review: |
Your experience in this course is entirely contingent on whether or not
your project partner is garbage or not. My team got split at c2 and we
each soloed our project from there because he just wasn't doing
anything. The project is also a lot of work and is completely disjoint
from examinable lecture material. The exams are true false, if you want
to see your result, you have to book a 10 minute quiz viewing session
(you are not allowed to take notes there). Lecture content isn't
terrible - it's just memorization.
      
First week is hell. You have to write unit tests to catch all mutants
(buggy versions of their code). The autograder has a 12 hour cooldown.
It's not unheard of for students to set alarms in the middle of the
night to run it because the deadline is so tight.
    difficulty: 2
    quality: 2
    sessionTaken: 2023W1

<pre>
</details>This is an auto-generated PR made using:
https://github.com/ubccsss/course-review-worker

---
## [acroreiser/android_kernel_lenovo_a6010](https://github.com/acroreiser/android_kernel_lenovo_a6010)@[1695f51a37...](https://github.com/acroreiser/android_kernel_lenovo_a6010/commit/1695f51a376f4b258e707a70981e54d5ed789129)
#### Sunday 2023-12-17 09:15:46 by Petr Mladek

kthread: add kthread_create_worker*()

Kthread workers are currently created using the classic kthread API,
namely kthread_run().  kthread_worker_fn() is passed as the @threadfn
parameter.

This patch defines kthread_create_worker() and
kthread_create_worker_on_cpu() functions that hide implementation details.

They enforce using kthread_worker_fn() for the main thread.  But I doubt
that there are any plans to create any alternative.  In fact, I think that
we do not want any alternative main thread because it would be hard to
support consistency with the rest of the kthread worker API.

The naming and function of kthread_create_worker() is inspired by the
workqueues API like the rest of the kthread worker API.

The kthread_create_worker_on_cpu() variant is motivated by the original
kthread_create_on_cpu().  Note that we need to bind per-CPU kthread
workers already when they are created.  It makes the life easier.
kthread_bind() could not be used later for an already running worker.

This patch does _not_ convert existing kthread workers.  The kthread
worker API need more improvements first, e.g.  a function to destroy the
worker.

IMPORTANT:

kthread_create_worker_on_cpu() allows to use any format of the worker
name, in compare with kthread_create_on_cpu().  The good thing is that it
is more generic.  The bad thing is that most users will need to pass the
cpu number in two parameters, e.g.  kthread_create_worker_on_cpu(cpu,
"helper/%d", cpu).

To be honest, the main motivation was to avoid the need for an empty
va_list.  The only legal way was to create a helper function that would be
called with an empty list.  Other attempts caused compilation warnings or
even errors on different architectures.

There were also other alternatives, for example, using #define or
splitting __kthread_create_worker().  The used solution looked like the
least ugly.

Link: http://lkml.kernel.org/r/1470754545-17632-6-git-send-email-pmladek@suse.com
Signed-off-by: Petr Mladek <pmladek@suse.com>
Acked-by: Tejun Heo <tj@kernel.org>
Cc: Oleg Nesterov <oleg@redhat.com>
Cc: Ingo Molnar <mingo@redhat.com>
Cc: Peter Zijlstra <peterz@infradead.org>
Cc: Steven Rostedt <rostedt@goodmis.org>
Cc: "Paul E. McKenney" <paulmck@linux.vnet.ibm.com>
Cc: Josh Triplett <josh@joshtriplett.org>
Cc: Thomas Gleixner <tglx@linutronix.de>
Cc: Jiri Kosina <jkosina@suse.cz>
Cc: Borislav Petkov <bp@suse.de>
Cc: Michal Hocko <mhocko@suse.cz>
Cc: Vlastimil Babka <vbabka@suse.cz>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[ca26f7528b...](https://github.com/tgstation/tgstation/commit/ca26f7528b804538674f00d529152b12c06dce0c)
#### Sunday 2023-12-17 09:47:54 by Jacquerel

Roundstart AIs are positronic (#80355)

## About The Pull Request

If you disassemble an AI which was in the round from the start it will
produce a Positronic Cube rather than an MMI with the brain of that
player's usual human character in it.

Also I made changes to a couple of feedback balloon alerts which would
always trigger a runtime when constructing or deconstructing an AI, this
was because balloon alerts have a small time delay before executing and
we deleted the AI mob or structure after trying to show a balloon alert
on them, so they'd never appear.

## Why It's Good For The Game

Honestly this is _mostly_ about vibes, it has annoyed me since AI
deconstruction was added that Nanotrasen AIs tend to actually be brains
in jars rather than AIs. Now they're artifical.
It does also mean that you can't deconstruct the AI and then put its
brain into a human body, which is similarly mostly bad because of vibes:
If you sign up as an AI I think you should be an AI or a cyborg even
after deconstruction.

It also universally looks really stupid when you deconstruct an AI and
it says it has the brain of Penelope Dreadful in there, like should I
expect them to start RPing as their normal character instead of the AI
they have been playing all round now?

## Changelog

:cl:
balance: Roundstart AIs are now made of positronic cubes, rather than
brains inside MMIs
/:cl:

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [catfooo/mern-tutorial-with-connectedprojectmongoapi](https://github.com/catfooo/mern-tutorial-with-connectedprojectmongoapi)@[a675d8635b...](https://github.com/catfooo/mern-tutorial-with-connectedprojectmongoapi/commit/a675d8635b0975af84df65ebc59279a47f533d90)
#### Sunday 2023-12-17 10:00:29 by So Youn Choi

im on today. but i just found out that ive spend time and energy quite a long time with something wrong. this made me feel sad and not feeling like getting into work. the thing i want to do today is test this with the video that linked at tutorial, bcs not like the original mern repo, this one not crashes the app, even it has two error in row. im not sure that i can ignore the error and keep going, so i need to test this out by just applying the video again. while doing that yesterday, i sticked something not important and used all my energy. today, im not feeling good bcs with certain reason, but i rly want to stick to this. it is not easy to walk for me, but i managed that somehow, so i dont want to lose the oppertunity to work. so lets face the feeling that im currently have. bcs i dont want to stop learning, i found out there is class that provides education and internship as well. so last couple of weeks i wanted to fill out the application form. but suddenly they changed the application form. what i did is seems like the task for formal classes. this means i put my energy in wrong way, and made me sad. i think i dont feel to have align with that school, bcs it requires me somehow to get used to their way as well, just like ive experienced at technigo. might take a lot, and im scared to try, but the thing is i dont want to stop, and scared what will happen to me after this bootcamp. bcs i feel i didnt learned much, i need to repeat this somehow, or need to find some kind of alternative, before throw myself to the hollow time with nothing, what im scared most is basically that. i dont want blank time anymore, bcs im already used to technigo, although this gave me much tear. so... bcs i feel not good with this new alternative, ill take time with talk with one that has responsiblity at technigo. actually the day when i started this, i applied for both bootcamp - uxui and web development, and i was supposed to start uxui next term, but this means change the focus for me, and im not sure it is worth to do. better than nothing, it is super sure, but i want to focus what i have been doing, more than give a try to bit unrelated new area. i want job with this area and i dont feel like i can get job bcs i lack knowledge first, and many other things like social skill and stuff, but the biggest thing is i dont know much, even i spent this amount of time. i never felt like that so therefore i cant apply for the job. forst i need to be confident at class, which never happened to me, so i need to repeat. what will happen next? idk, but this is what im currently thinking on, rather than learning w16 thing itself or doing final project. something is wrong, and it is hard to see from my side, i need help, that seems to be never gotten from anyone. anyway, it was comfortable to identify myself as developer, i wasnt need to worry for the job for the moment, and it was nice to enjoy the development joke from my home language, bcs that was something i couldnt do from 20 years earlier. i wanted to be one of them, i wanted to understand their way of communication, but i didnt have motivation so i couldnt educate myself. this class was different, so i tried without quitting, and got this much. motivation is everything for me. it makes me move. so i am not complaining... oh, now im in the mood for look this straight. ill try this repo with the video, and hope i get any kind of conclusion, rly want to get the structure here, so i can finally understand the code coachs way for backend. wish me good luck

---
## [PragTob/elixir](https://github.com/PragTob/elixir)@[1e229159bf...](https://github.com/PragTob/elixir/commit/1e229159bf5056c7fa0da57d533606713b87b5bb)
#### Sunday 2023-12-17 10:08:58 by Tobias Pfeiffer

Document the process anti pattern of sending large data

Follow up to/extension of #13173

First draft, happy to adjust and extend it in many ways. I had
trouble coming up with a simple example as we needed a bunch of
data to make sure it's not good. I could have employed the first
anti pattern myself and did repeated statistics calculation, but
that'd have been worse :sweat-smile:

I remembered José's comment around sending along the `conn` and
figured it's central enough in elixir to not throw anyone off.

If someone has a better example, happy to redo it!

Thanks y'all! :green-heart:

---
## [tarori/terminal](https://github.com/tarori/terminal)@[abab8705fe...](https://github.com/tarori/terminal/commit/abab8705fea32854a6b55153b5736f9fd9dacb66)
#### Sunday 2023-12-17 10:34:07 by Dustin L. Howett

Add a magic incantation to tell the Store we support Server (#16306)

I find it somewhat silly that (1) this isn't documented anywhere and (2)
installing the "desktop experience" packages for Server doesn't
automatically add support for the `Windows.Desktop` platform...

Oh well.

I'm going to roll this one out via Preview first, because if the store
blows up on it I would rather it not be during Stable roll-out.

(cherry picked from commit 86fb9b44787accd09c5943a506e27eb4c8e573c0)
Service-Card-Id: 91098597
Service-Version: 1.19

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[274eb2a52e...](https://github.com/psychonaut-station/PsychonautStation/commit/274eb2a52ecd35f86d1cd83032c655997dc73106)
#### Sunday 2023-12-17 10:53:48 by distributivgesetz

Removes Clone Damage (#80109)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Does what it says on the tin. We don't have any "special" sources of
clone damage left in the game, most of them are rather trivial so I
bunched them together into this PR.

Notable things removed:
- Clonexadone, because its entire thing was centered around clone damage
- Decloner gun, it's also centered around cloning damage, I couldn't
think of a replacement mechanic and nobody uses it anyways
- Everything else already dealt clone damage as a side (rainbow knife
deals a random damage type for example), so these sources were removed

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Consider the four sources of normal damage that you can get: Brute,
Burn, Toxins and Oxygen. These four horsemen of the apocalypse are very
well put together and it's no surprise that they are in the game, as you
can fit any way of damaging a mob into them. Getting beaten to death by
a security officer? Brute damage. Running around on fire? Burn damage.
Poisoned or irradiated? Toxin damage. Suffocating in space? Brute, burn
and oxygen damage. Technically there's also stamina damage but that's
its own ballpark and it also makes sense why we have a damage number for
it.

Picture this now: We have this cool mechanic called "clone pods" where
you can magically revive dead people with absolute ease. We don't want
it to be for free though, it comes at a cost. This cost is clone damage,
and it serves to restrain people from abusing cloning.

Fast forward time a bit and cloning is now removed from the game. What
stays with us is a damage number that is intrinsically tied to the
context of a removed feature. It was a good idea that we had it for that
feature at the time, but now it just sits there. It's the odd one out
from all the other damage types. You can easily explain why your blade
dealt brute damage, but how are you going to fit clone damage into any
context without also becoming extremely specific?

My point is: **clone damage is conceptually a flawed mechanic because it
is too specific**. That is the major issue why no one uses it, and why
that makes it unworthy of being a damage stat.
Don't take my word for it though, because a while ago we only had a
handful of sources for this damage type in the game. And in most of the
rounds where you saw this damage, it came from only one department. It's
not worthwhile to keep it around as a damage number. People also didn't
know what to do with this damage type, so we currently have two ways of
healing clone damage: Cryotubes as a roundstart way of healing clone
damage and Rezadone, which instantly sets your clone damage to 0 on the
first tick. As a medical doctor, when was the last time you saw someone
come in with clone damage and thought to yourself, "Oh, this person has
clone damage, I cannot wait to heal them!" ?

Now we have replacements for these clone damage sources. Slimes? Slime
status effect that deals brute instead of clone. Cosmic heretics? Random
organ damage, because their mechanics are already pretty fleshed out.
Decloning virus? The virus operated as a "ticking timebomb" which used
cloning damage as the timer, so it has been reworked to not use clone
damage. What remains after all this is now a basically unused damage
type. Every specific situation that used clone damage is now relying on
another damage type. Now it's time to put clone damage to rest once and
for all.

Sure, you can technically add some form of cellular degradation in the
future, but it shouldn't be a damage number. The idea of your cells
being degraded is a cool concept, don't get me wrong, but make it a
status effect or maybe even a wound for that matter.

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
del: Removed clone damage.
del: Removed the decloner gun.
del: Removed clonexadone.
/🆑

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [ChanhAvo/SusyFishy](https://github.com/ChanhAvo/SusyFishy)@[6a07060166...](https://github.com/ChanhAvo/SusyFishy/commit/6a07060166d216d122a2893e3c6b3a9a6ce36067)
#### Sunday 2023-12-17 11:11:42 by HoriDang10

change for loop map into the orginal one (i hate my life)

---
## [guillemj/systemd](https://github.com/guillemj/systemd)@[1761066b13...](https://github.com/guillemj/systemd/commit/1761066b135f1a322c446f102343ea4aa61fe3ee)
#### Sunday 2023-12-17 12:28:42 by Lennart Poettering

storagetm: add new systemd-storagetm component

This implements a "storage target mode", similar to what MacOS provides
since a long time as "Target Disk Mode":

        https://en.wikipedia.org/wiki/Target_Disk_Mode

This implementation is relatively simple:

1. a new generic target "storage-target-mode.target" is added, which
   when booted into defines the target mode.

2. a small tool and service "systemd-storagetm.service" is added which
   exposes a specific device or all devices as NVMe-TCP devices over the
   network.  NVMe-TCP appears to be hot shit right now how to expose
   block devices over the network. And it's really simple to set up via
   configs, hence our code is relatively short and neat.

The idea is that systemd-storagetm.target can be extended sooner or
later, for example to expose block devices also as USB mass storage
devices and similar, in case the system has "dual mode" USB controller
that can also work as device, not just as host. (And people could also
plug in sharing as NBD, iSCSI, whatever they want.)

How to use this? Boot into your system with a kernel cmdline of
"rd.systemd.unit=storage-target-mode.target ip=link-local", and you'll see on
screen the precise "nvme connect" command line to make the relevant
block devices available locally on some other machine. This all requires
that the target mode stuff is included in the initrd of course. And the
system will the stay in the initrd forever.

Why bother? Primarily three use-cases:

1. Debug a broken system: with very few dependencies during boot get
   access to the raw block device of a broken machine.

2. Migrate from system to another system, by dd'ing the old to the new
   directly.

3. Installing an OS remotely on some device (for example via Thunderbolt
   networking)

(And there might be more, for example the ability to boot from a
laptop's disk on another system)

Limitations:

1. There's no authentication/encryption. Hence: use this on local links
   only.

2. NVMe target mode on Linux supports r/w operation only. Ideally, we'd
   have a read-only mode, for security reasons, and default to it.

Future love:

1. We should have another mode, where we simply expose the homed LUKS
   home dirs like that.

2. Some lightweight hookup with plymouth, to display a (shortened)
   version of the info we write to the console.

To test all this, just run:

    mkosi --kernel-command-line-extra="rd.systemd.unit=storage-target-mode.target" qemu

---
## [gitmachtl/scripts](https://github.com/gitmachtl/scripts)@[5562496e3b...](https://github.com/gitmachtl/scripts/commit/5562496e3b38f40098b36d62f6dc16d296014c71)
#### Sunday 2023-12-17 12:52:12 by gitmachtl

New release: Light-Mode, Sub-Handle and Virtual-Handle, Conway-Era

Rendered Release-Notes: https://github.com/gitmachtl/scripts/releases/tag/Light-Mode

## New Feature - LIGHT-Mode, running the SPO Scripts without a local node

This is an exciting new feature in the SPO Scripts. Before we had two operational modes, Online-Mode and Offline-Mode. Now we have an additional one, the Light-Mode.

So whats this Light-Mode? If you switch the scripts into Light-Mode - see below how easy it is to do so - you have the advantage of being online with your machine, but you don't need a running synced cardano-node. You can switch between Networks Mainnet, PreProd and PreView within seconds.

This comes is handy if you just don't want to install and run a cardano-node, if you don't have the space for the database or if you just don't have the time to wait for a resync.

All transactions are of course generated and signed locally, but the queries and the transmit is done via online APIs like Koios.

How do you switch between Online-, Light- and Offline-Mode?
Thats simple, you just change a single entry in the 00_common.sh, common.inc or $HOME/.common.inc config-file: image

workMode="online": Scripts are working in Online-Mode aka Full-Mode. A locally running and synced cardano-node is needed.
workMode="light": Scripts are working in Light-Mode. No cardano-node needed.
workMode="offline": Scripts are working in isolation and completely offline. No cardano-node needed.

You can do ALL OPERATIONS in Light-Mode now! ?? Currently supported Chains are Mainnet, PreProd and PreView. You can switch between chains in seconds, and if you put a different common.inc file into your folders, you can run them all in parallel too. I also wanna thank Holger from Cardano24, because i am hosting the Online-Version of the Protocol-Parameters JSON files on his distributed Server-Platform uptime.live, thank you! The JSON files are updates every 10 mins to make them available in Light-Mode.

If you have an Online/Offline Workflow, you can use the Online machine in Light-Mode, and your Offline machine is still offline of course.

## New Feature - $Sub-Handle & $Virtual-Handle support for $Adahandles ??

Complete support for the upcoming Sub-Handle and Virtual-Handle release. All scripts than can use Adahandles for queries and destinations are upgraded to support these additional formats. As always, the scripts doing a second lookup if the Handles are really on the UTXOs that the APIs report. For the Virtual-Handles the Scripts are doing an extra Koios request to checkout the Inline-Datum content of the UTXO holding the Virtual-Handle. Virtual-Handles store the destination address within the Inline-Datum.

Also there has been an Update to show all the different types of Adahandles in the Query, like ADA Handle for the original CIP-25 one, Ada Handle(Own) for the new CIP68 ones. Ada Handle(Ref) and Ada Handle(Virt) for the newest formats.

## Improvements to the Online-Mode (aka Full-Mode)

Critical queries now always do a check if the local node is 100% synced with the chain before continuation.

## Improvements to the Offline-Mode

In Offline-Mode the header on each Script Call now shows your local machine time. This is really important if you are doing things like an OpCert-Update to generate the right KES period. So now you can do an easy check if the time on your Offline-Machine is correct
NativeAsset Token-Registry Information also in Offline-Mode. To get the UTXO data of an address you wanna use in Offline-Mode you are using the command ./01_workOffline.sh add <walletname>. This query - if enabled in the config - now also stores the Token-Registry information about NativeAssets on this address within the offlineTransfer.json file.

##  General updates

The SPO Scripts are now fully Conway-Era compatible!!

01_claimRewards.sh, 01_queryAddress.sh are now showing if the Stake-Address is delegated to a pool. If so it tries to show additional pool-informations like the Ticker, Description and the current Pool-Status

03a_genStakingPaymentAddr.sh: The generation of the Stake-Address registration certificate has been moved to be done within 03b_regStakingAddrCert.sh. This is a change for conway-era, because we now have to check the StakeAdress-Registration Deposit-Fee also for the deregistration. The Deposit-Fee can change after a registration has been done, so with conway-era the used amount is now stored within the certificate itself. If the StakeAddress is already registered on chain, the Script will tell you that and if also delegated to a Pool, it wil try to show you additional informations.
03c_checkStakingAddrOnChain.sh now also shows the used Deposit-Fee of a registered Stake-Address. If delegated to a pool, it tries to show additional Informations. image

04d_genNodeOpCert.sh now directly ready out the onDisKOpCertCount from the via an own new CBOR-Decode function to provide checking information in Light-Mode.

04e_checkNodeOpCert.sh now ready out the onDiscOpCertCount and the onDiskKESSStart values for checking in Online- and Light-Mode

05a_genStakepoolCert.sh now shows the set poolPledge also in ADA and not only in lovecase. Shows minPoolCost now also in ADA and not only in lovelaces. Shows the poolMargin now in percentage and not as decimal value.

05c_regStakepoolCert.sh now shows the set poolPledge also in ADA and not only in lovecase. Shows minPoolCost now also in ADA and not only in lovelaces. Shows the poolMargin now in percentage and not as decimal value.
A pool update/registration/retirement of course now also works in Light-Mode: image If there are external Witnesses (MultiOwnerPool) and the registration is done with an attached Metadata-JSON/CBOR, that information is now also stored to be represented in the external witness file.

05e_checkPoolOnChain.sh now gives you detailed informations about the current pool-status. You can of course also use a pool-id in bech or hex to query this information with this script.

06_regDelegationCert.sh now checks the pool status you wanna send the delegation before continue with the transaction. If a pool is retired or was not registered on the chain(yet), such a transaction would let to an error. This precheck avoids this issue. In addition there is now a check that the Stake-Address is already registered on chain. Also, it now shows information about a current delegation and the planned delegation. The script directly reads out the delegation destination pool-id from the delegation certificate to show this information.

08a_genStakingAddrRetireCert.shnow checks if the Stake-Address is even registered before generating the Retirement-Certificate. Also now important, it checks the Deposit-Fee that was used to register the Stake-Address in first place. Because we need to use the exact Fee again to retire the Stake-Address. There is now also a check if the Stake-Address you wanna retire still holds rewards. If the Stake-Address still hold rewards, it will show you the amount and refuse to generate a Retirement certificate. In that case please first claim all your rewards via 01_claimRewards.sh and after that retire the Stake-Address.

08b_deregStakingAddrCert.shnow again checks the current Stake-Address status on chain and a possible active delegation. Just to make sure you're retireing the right Stake-Address. It also now directly reads out the used Stake-Address Deposit-Fee to calculate the balance return correctly.

Many additional updates here and there for better request handling via curl, better error checks, etc ...

Please enjoy this huge update and especially the new Light-Mode!!

---
## [catfooo/to-merge-mern-with-projectmongoapi](https://github.com/catfooo/to-merge-mern-with-projectmongoapi)@[db00fdd86e...](https://github.com/catfooo/to-merge-mern-with-projectmongoapi/commit/db00fdd86e1f036469ee2960b0d994022ae0f9d7)
#### Sunday 2023-12-17 14:11:16 by So Youn Choi

roll back. i strongly doubt this is usefull. one thing i want to go through is the line chatgpt added to take care of timeout. it has error but not crashes the app. when i have time or energy i want to do this before go forward. so.. in summary, this was not showing the colored line i supposed to show, but i feel i didnt look close about this in this repo. like the formal line that i got suggested, or the way of handle timeout. but its 15:07 and i need recharge. remember i was used to work early morning till late night. i was positive towards this in all way. while the moment, it took away my urge to work. idk it is good or bad at this moment, but the thing is, this comes for me very rare, lets say once every 20 years haha. am i wasting my life? even if so, i want to continue, bcs i love my life, that got through these days...

---
## [InsaneRed/cmss13](https://github.com/InsaneRed/cmss13)@[e7816d96c5...](https://github.com/InsaneRed/cmss13/commit/e7816d96c5d1523337dec081bea0056fbc9189fc)
#### Sunday 2023-12-17 14:14:52 by forest2001

Almayer AntiTheft measures. (#5100)

STOP STEALING SHIT
# About the pull request
Adds a subtype of reinforced hull for the Almayer that changes between
indestructible hull and normal reinforced wall after hijack.
Uses this wall type around uniform vendors, the separation wall in the
firing range and around engineering storage.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Having the engineering storage looted at round start is just silly
avoidance of the "don't deconstruct the whole ship without a reason"
rule.

# Testing Photographs and Procedure

I have verified that all works as intended, the walls cannot be harmed
prior to hijack, and shutters function as advertised.

# Changelog
:cl:
add: Added a new almayer hull type (heavy reinforced) which is
indestructible by normal means until after hijack collision.
add: Added a new subtype of shutter that automatically opens or closes
depending on security level.
maptweak: Maps both of the above around the engineering storeroom. Also
adds the walls between the firing ranges and around uniform vendors.
maptweak: Manual control button for shutters over engineering storage in
the CEs office.
code: Changes hijack structural changes (walls/windows/windoors/ladders)
to use signals.
/:cl:

---------

Co-authored-by: fira <loyauflorian@gmail.com>

---
## [RobWalt/bevy](https://github.com/RobWalt/bevy)@[3ee9edf280...](https://github.com/RobWalt/bevy/commit/3ee9edf280c530f35a51049ec92fcfa552998614)
#### Sunday 2023-12-17 14:34:25 by Ethereumdegen

add try_insert to entity commands (#9844)

# Objective

- I spoke with some users in the ECS channel of bevy discord today and
they suggested that I implement a fallible form of .insert for
components.

- In my opinion, it would be nice to have a fallible .insert like
.try_insert (or to just make insert be fallible!) because it was causing
a lot of panics in my game. In my game, I am spawning terrain chunks and
despawning them in the Update loop. However, this was causing bevy_xpbd
to panic because it was trying to .insert some physics components on my
chunks and a race condition meant that its check to see if the entity
exists would pass but then the next execution step it would not exist
and would do an .insert and then panic. This means that there is no way
to avoid a panic with conditionals.

Luckily, bevy_xpbd does not care about inserting these components if the
entity is being deleted and so if there were a .try_insert, like this PR
provides it could use that instead in order to NOT panic.

( My interim solution for my own game has been to run the entity despawn
events in the Last schedule but really this is just a hack and I should
not be expected to manage the scheduling of despawns like this - it
should just be easy and simple. IF it just so happened that bevy_xpbd
ran .inserts in the Last schedule also, this would be an untenable soln
overall )

## Solution

- Describe the solution used to achieve the objective above.

Add a new command named TryInsert (entitycommands.try_insert) which
functions exactly like .insert except if the entity does not exist it
will not panic. Instead, it will log to info. This way, crates that are
attaching components in ways which they do not mind that the entity no
longer exists can just use try_insert instead of insert.

---

## Changelog

 

## Additional Thoughts

In my opinion, NOT panicing should really be the default and having an
.insert that does panic should be the odd edgecase but removing the
panic! from .insert seems a bit above my paygrade -- although i would
love to see it. My other thought is it would be good for .insert to
return an Option AND not panic but it seems it uses an event bus right
now so that seems to be impossible w the current architecture.

---
## [Erol509/Bubberstation](https://github.com/Erol509/Bubberstation)@[b5e095e380...](https://github.com/Erol509/Bubberstation/commit/b5e095e380e729793628d254bb441f51ecdb046b)
#### Sunday 2023-12-17 15:16:16 by Waterpig

[MODULAR] Refactors (hopefully) all borg modular changes into one module, adds raptor borgs (#777)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Originally I was supposed to only add raptor borgs, but I am simply too
insane to let this shitcode slide.

Moves most if not all borg modular changes into one module folder
because by god these were spread out over like 8 files.
Improves modularity a bit by moving some borg related bubber edits on
skyrat into our modular files.
Adds raptor borgs

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Please make sure to actually test your PRs. If you have not tested
your PR mention it. -->

## Why It's Good For The Game

Modularity good.
Code organizing good.

https://en.wikipedia.org/wiki/Technical_debt

Also new borg sprites are cool, I guess. See icondiff bot for those
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
image: New borg sprites: Raptor
refactor: Moved most if not all bubber borg code into one modular folder
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
## [DeepakSingh786/Evaluation-Projects](https://github.com/DeepakSingh786/Evaluation-Projects)@[bf866d3c8b...](https://github.com/DeepakSingh786/Evaluation-Projects/commit/bf866d3c8b35cae6e5100a1f7b2363c9d5a98b44)
#### Sunday 2023-12-17 16:05:40 by DeepakSingh786

Loan Application Status Prediction

Loan Application Status Prediction
Project Description
This dataset includes details of applicants who have applied for loan. The dataset includes details like credit history, loan amount, their income, dependents etc. 
Independent Variables:
1.	Loan_ID - This refer to the unique identifier of the applicant's affirmed purchases
2.	Gender - This refers to either of the two main categories (male and female) into which applicants are divided on the basis of their reproductive functions
3.	Married - This refers to applicant being in a state of matrimony
4.	Dependents - This refres to persons who depends on the applicants for survival
5.	Education - This refers to number of years in which applicant received systematic instruction, especially at a school or university
6.	Self_Employed - This refers to applicant working for oneself as a freelancer or the owner of a business rather than for an employer
7.	Applicant Income - This refers to disposable income available for the applicant's use under State law.
8.	CoapplicantIncome - This refers to disposable income available for the people that participate in the loan application process alongside the main applicant use under State law.
9.	Loan_Amount - This refers to the amount of money an applicant owe at any given time.
10.	Loan_Amount_Term - This refers to the duaration in which the loan is availed to the applicant
11.	Credit History - This refers to a record of applicant's ability to repay debts and demonstrated responsibility in repaying them.
12.	Property_Area - This refers to the total area within the boundaries of the property as set out in Schedule.
13.	Loan_Status - This refres to whether applicant is eligible to be availed the Loan requested.
You have to build a model that can predict whether the loan of the applicant will be approved(Loan_status) or not on the basis of the details provided in the dataset. 
Dataset Link-  https://github.com/dsrscientist/DSData/blob/master/loan_prediction.csv

---
## [cockroachdb/cockroach](https://github.com/cockroachdb/cockroach)@[e174990dd5...](https://github.com/cockroachdb/cockroach/commit/e174990dd5015a38b1e9bc6723f270dbe647c3a3)
#### Sunday 2023-12-17 16:06:20 by craig[bot]

Merge #113809

113809: kvstreamer: add limit to how many eager batches are issued r=yuzefovich a=yuzefovich

**kvstreamer: add limit to how many eager batches are issued**

This commit fixes extremely suboptimal behavior of the streamer in the
InOrder mode in some cases. In particular, previously it was possible
for the buffered responses to consume most of the working budget, so the
streamer would degrade to processing all requests effectively one
BatchRequest with one Get / Scan at a time, significantly increasing the
latency. For example, the query added as a regression test that performs
30k Gets across 10 ranges would usually take on the order of 1.5s (which
is not great already since in the non-streamer path it takes 400ms), but
in the degenerate cases it could be on the order of 20-30s.

Similar behavior could occur in the OutOfOrder mode too where we would
issue more BatchRequests in which only one request could be satisfied
(although in OutOfOrder mode the problem is not as severe - we don't
buffer any results since we can always return them right away).

This problem is now fixed by imposing the limit on the budget's usage at
which point the streamer stops issuing "eager" requests. Namely, now,
when there is at least one request in flight, the streamer won't issue
anymore requests once `limit * eagerFraction` is exceeded. This
effectively reserves a portion of the budget for the "head-of-the-line"
batch.

The "eager fraction" is controlled by a session variable, separate for
each mode. The defaults of 0.5 for InOrder and 0.8 for OutOfOrder modes
were chosen after running TPCH queries and the query that inspired this
commit. These values bring the number of gRPC calls for the reproduction
query from 1.5k-2k range to below 200 and the query latency to be
reliably around 400ms.

I don't really see any significant downsides to this change - in the
worst case, we'd be utilizing less of the available memory budget which
is not that big of a deal, so I intend to backport this change. Also,
setting the eager fractions to large values (greater than 1.0 is
allowed) would disable this limiting behavior and revert to the previous
behavior if we need it.

Fixes: #113729.

Release note (bug fix): Previously, when executing queries with
index / lookup joins when the ordering needs to be maintained,
CockroachDB in some cases could get into a pathological behavior
which would lead to increased query latency, possibly by 1 or 2 orders
of magnitude. This bug was introduced in 22.2 and is now fixed.

**kvstreamer: increase default avg response multiple**

This commit increases the default value for
`sql.distsql.streamer.avg_response_size_multiple` cluster setting from
1.5 to 3.0. This setting controls the factor by which the current "avg
response size" estimate is multiplied and allows for TargetBytes
parameter to grow over time. In the reproduction query from the
previous commit it was determined that the growth might not be as quick
as desirable.

The effect of this change is as follows:
- if we have responses of varying sizes, then we're now likely to be more
effective since we'll end up issuing less BatchRequests
- if we have responses of similar sizes, then we might pre-reserve too
much budget upfront, so we'll end up with lower concurrency across
ranges.

Thus, we don't want to increase the multiple by too much; however,
keeping it at 1.5 can be quite suboptimal in some cases - 3.0 seems like
a decent middle ground. This number was chosen based on running TPCH
queries (both via InOrder and OutOfOrder modes of the streamer) and the
reproduction query. (For the latter this change reduces the number of
gRPC calls by a factor of 3 or so.)

Release note: None

Co-authored-by: Yahor Yuzefovich <yahor@cockroachlabs.com>

---
## [tkerby/flipperzero-firmware-wPlugins](https://github.com/tkerby/flipperzero-firmware-wPlugins)@[675dba7204...](https://github.com/tkerby/flipperzero-firmware-wPlugins/commit/675dba72042295f1bf79159cf7b24b859d60b2c4)
#### Sunday 2023-12-17 16:52:42 by Leeroy

Rollback Keyloq to 5 months ago! Bloody regressions making my daily life shit!

---
## [juanbretondelacierva/wind_tunnel](https://github.com/juanbretondelacierva/wind_tunnel)@[75175bd61f...](https://github.com/juanbretondelacierva/wind_tunnel/commit/75175bd61f50a01255a5552f25b5e9b16495525d)
#### Sunday 2023-12-17 17:32:12 by juanbretondelacierva

Ah, no, va a ser de ello' Sabe' que salgo a la calle y son mínimo cien en el cuello Tiene una amiga que, también, si la cojo, se lo estrello Desde que toy haciendo chavo' con cojone' ahora pa toa' soy bello, bello Ella quiere que le dé, y despué' le dé banda Blanquita, parece de Holanda Pero se pone en cuatro y yo le digo: "baby, dale, tú ere' la que manda" Tú ere' la que manda, la' nalga' te la' agranda' ¿Tu jevo dónde anda?, sí Que baje pa la zona y se va con to' lo' que ande Ella quiere que le dé, y despué' le dé banda Blanquita, parece de Holanda (Holanda) Pero se pone en cuatro y yo le digo: "baby, dale, tú ere' la que, dale, tú ere' la que manda" Siempre que te veo tá' má' grande (grande) Bebecita, pa mí que tú te agranda' El cuello como Holanda, sí, sí (¿me sigue'?) Aquí hay corta' y R En la disco y puede que eso se cierre Ese culo obligao'e de PR No se ha muerto y quiere que se lo entierre E' una demon, ella nunca se muere (nunca se muere) Dice que me ama y en verda ni me quiere (ni me quiere) Estudia en la Inter, eso no interfiere Se besa con su' bestie', pa mí que le gustan la' mujere' ¿Qué lo que?, a lo' hater' le' picheo y no juego MLB Sabe que la llevo, la otra ve' me la llevé (me la llevé) Reservao, pero llamo y reservé No la quiero si no, si no tiene doble D (no) E' una HP, me gusta verla en HD (en HD) Le gustan lo' motele' por la' luce' LED Quiere que yo le dé banda como la de RBD, eh (eh) En lo que voy a abrirte, baby, como un locker (locker) Venezolana, me la llevé pa Los Roque' (pa Los Roque') Qué rico mama cuando se pone el choker Se jodió mi mai con esta motherfucker (La Presión) Eso rojo como la yersey de los Rocket (de los Rocket) Es chiquita, como una Polly Pocket (¿me sigue'?) Muchos billete' saliéndome de lo' pocket' Ella quiere que le dé, y despué' le dé banda Blanquita, parece de Holanda Pero se pone en cuatro y yo le digo: "baby, dale, tú ere' la que manda" Tú ere' la que manda, la' nalga' te la' agranda' ¿Tu jevo dónde anda?, sí (sí) Que baje pa la zona y se va con to' lo' que ande Ella quiere que le dé, y despué' le dé banda Blanquita, parece de Holanda (Holanda) Pero se pone en cuatro y yo le digo: "baby, dale, tú ere' la que, dale, tú ere' la que manda" Siempre que te veo tá' má' grande (grande) Bebecita, pa mí que tú te agranda' El cuello como Holanda, sí, sí Ese cuerpo'e una nave espacial, sí Te la echo, baby, como un facial Si tú te moja', yo vo'a bucear Tú ere' una diabla, te quiere' quemar Aparentemente no va a aparentar Y si da' like, yo vo'a comentar Ponte pe-, ponte pe-, ponte pe-, ponte perra Ponte pe-, ponte pe-, ponte pe-, ponte perra Sí, ponte pe-, ponte perra (ponte pe-, ponte pe-, ponte pe-, ponte perra) Ponte pe-, ponte perra (ponte pe-, ponte pe-, ponte pe-, ponte perra) ¿Me sigue' o no me sigue' todavía? Ponte pe-, ponte pe-, ponte pe-, ponte perra Ponte pe-, ponte pe-, ponte pe-, ponte perra Sí, ponte pe-, ponte pe-, ponte perra Ponte pe-, ponte pe-, ponte perra (ponte pe-, ponte pe-, ponte pe-, ponte perra)

changed to comparing 2 cases

---
## [Proxima-Project/Proxi-Eris](https://github.com/Proxima-Project/Proxi-Eris)@[2d50f604f9...](https://github.com/Proxima-Project/Proxi-Eris/commit/2d50f604f9f239fe5446107b238a8c34131f9fc2)
#### Sunday 2023-12-17 17:59:32 by евиё

Titanium material (#8)

* adding titanium

may the god forgive me for editing base

* fixes my fuck ups

---
## [cybernomadddd/Teaching-Myself-Python](https://github.com/cybernomadddd/Teaching-Myself-Python)@[5e918f0880...](https://github.com/cybernomadddd/Teaching-Myself-Python/commit/5e918f08800dca6b1b500756219d07aeff622057)
#### Sunday 2023-12-17 18:16:52 by CyberWarny

penguincomment

First off, let's acknowledge the reality – coding is not for the faint-hearted. It's a maze of logic, syntax, and curly braces that can make even the sanest among us question our life choices. Enter PenguinZ0, the chaotic maestro who's injecting levity into the tech space like a jolt of caffeine to the system.

Why code like PenguinZ0? Well, let me tell you, in a world where error messages feel like they're mocking your very existence, where deadlines are tighter than skinny jeans on a hot day, we need some comic relief. PenguinZ0 brings that, and then some.

Coding, my friends, is a dance with uncertainty. It's like navigating a minefield blindfolded – you don't know what's going to blow up in your face next. And what does PenguinZ0 do? He takes this uncertainty and turns it into a comedy goldmine. Error? More like a punchline waiting to happen.

Now, let's talk about comments. Oh, those little notes you leave for your future self or your colleagues in your code. PenguinZ0 doesn’t just leave comments; he crafts miniature comedy sketches in the margins of his code. It's not just about telling what the code does; it's about making your code a literary masterpiece.

And variable names? Oh, they're not just a string of characters; they're an opportunity for linguistic acrobatics. Why call it "userInput" when you can call it "theThingThatMakesTheComputerGoBrrr"? PenguinZ0 understands the power of a good name – it's not just a variable; it's a statement.

Let's not forget the art of debugging. While most of us stare at the screen, questioning our life choices, PenguinZ0 embraces the chaos. He doesn't just debug; he engages in a philosophical debate with the code. He talks to it like a therapist, coaxing out its deepest issues. And when the bug finally reveals itself, it's like the grand finale of a fireworks show.

Coding is serious business, they say. But PenguinZ0 says, "Why so serious?" Let's infuse some joy into the lines of code we write. Let's turn debugging sessions into stand-up routines. Let's make variable names a canvas for our linguistic artistry. Let's code like PenguinZ0, because in this sea of seriousness, a little chaos is exactly what we need.

So, the next time you're knee-deep in code, drowning in a sea of error messages, remember the words of the chaotic coding maestro himself – "Just do it, I guess. I don't know." Code with humor, my friends, and turn the tech world into your own comedy club.

---
## [daelmaak/ngx-gallery](https://github.com/daelmaak/ngx-gallery)@[3d4a7aef9f...](https://github.com/daelmaak/ngx-gallery/commit/3d4a7aef9fd27b2d02b080cc8e4e0548f856c7bf)
#### Sunday 2023-12-17 18:36:33 by Daniel Macak

chore: use strict type checking in the gallery lib

The loose type checking was one of the reasons the gallery was plagued
by TypeErrors lately. Well what do I have TS then for? Setting TS to
strict mode helps greatly with eliminating these.

Since lot of changed, let's go through the list of my decisions:
- I only made the lib's type checking strict since otherwise there would
  be too many changes. I don't want to enable this for the apps/demo
  since I kinda like having it flexible. Switching it on makes sense for
  the tests, but it's not too important at the moment, and I sense a
  small rewrite will be needed due to some of the less orthodox test
  code.
- I changed most of the inputs, especially in the child components, to
  optional so to reflect they might be undefined. But, few of those I
  declare as always defined. Though I don't like this, it's still better
  option than check all over the code base when I know the input is
  guaranteed to be defined from parent components.
- On many TemplateRefs I used `$any()` since Angular's type requirements
  are insane in certain contexts. It's especially maddening when it
  comes to Angular expecting `null` and me having `undefined`. In order
  not to have to do undefined | null gymnastics in my inputs, I chose
  $any as an easy way out.
- I usually declare ElementRefs as always defined and just accept the
  risk of theoretically running into TypeErrors. The reason is that I
  just feel that only because these are not existent only in the very
  early phases is not worth the trouble of always checking their
  presence. I am fully aware I prefer convenience over safety here, but
  I am convinced I can cover the blind spots with tests and good
  coding practices.

---
## [SomeguyManperson/Shiptest](https://github.com/SomeguyManperson/Shiptest)@[247a4e02ea...](https://github.com/SomeguyManperson/Shiptest/commit/247a4e02eab24ccfa191ea0447e587aeaf4c1235)
#### Sunday 2023-12-17 18:45:29 by BluBerry016

{Icemoon, Ruin} The Crashed Holemaker (#2413)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Adds a brand-new - well, [new to
shiptest](https://cohost.org/bluwu016/post/885120-a-compilation-of-my) -
ruin to the Icemoon roster, focused on the service department.

It's flavored around being an *incredibly* old NT Spaceworks vessel
that's been carved in half and crashed - what's present only being the
fore of the ship. Being mainly service-focused, it's loot is pretty dry
~~as is it's sole threat.~~
If more current-day mappers/balance-heads have any words about how to
fluff out either of those pools a bit more with the screenshots below,
lemme know. I'll listen well.

(Notarized loot summary removed as updating it was a pain in the ass,
lmao.)

It strikes me as leaning on the underwhelming side from looking at the
other ruins present here but we'll. See? I suppose? It's good practice
for me in the whole, "making something I have memorized and that looks
good normally look sicker ruined".

<details><summary>Pictures (All but SDMM Outdated)</summary>
<p>

Ignore that there's no rust, the firelocks are open here, and some
stuff's knocked around, I was testing it prior to me tacking the rust on
and took pics after running around it in-person.


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/51a3cc54-1727-4241-9592-639f892621bf)


![image](https://github.com/shiptest-ss13/Shiptest/assets/50649185/580e39fe-bbf9-481f-aff8-cc25f860638d)

StrongDMM View:

![2023-11-09 15 02
20](https://github.com/shiptest-ss13/Shiptest/assets/50649185/5b94af63-d2d8-42bd-a823-0d300d66191f)

</p>
</details> 
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
This isn't what I intended to do when I was like, "oh yeah, I have a
goofy ahh downstream out of boredom, ya'll want some of our better
ships" but w/e here it is anyways. Ya'll need ruins. I made (another)
ruin.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: A new icemoon ruin has been added, should you be in need of service
department goodies.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: BluBerry016 <50649185+unit0016@users.noreply.github.com>

---
## [Stutternov/f13tbd](https://github.com/Stutternov/f13tbd)@[e211796729...](https://github.com/Stutternov/f13tbd/commit/e2117967298eab34c19e70ff450dabe36981258e)
#### Sunday 2023-12-17 19:22:09 by panzerr1944

Map Changes, NML Edits, E-Weapon Loot Spawners & More (#303)

## About The Pull Request
Long list of fixes, edits and other things. Check the changelog for a
full list!

## Why It's Good For The Game
Less dumb spawners, better spawners for e-weapons, more cars, less setup
time, harder dungeon, more fun :)

![Screenshot 2023-12-04
142647](https://github.com/f13babylon/f13babylon/assets/76122712/468a97b4-c78d-4c92-8fcf-43d18c841db2)
![Screenshot 2023-12-04
142707](https://github.com/f13babylon/f13babylon/assets/76122712/b7d8a748-3e80-4c04-8af3-f9f660eb55ef)

## Pre-Merge Checklist
- [ Y ] You tested this on a local server.
- [ Y ] This code did not runtime during testing.
- [ Y ] You documented all of your changes.

## Changelog
🆑
remove: the 2 unique spawns on the surface/underground that can be
rushed
remove: the 'Left Hand' riot shotgun force-spawner (and Raider T-45b
spawner)
add: a chemlab, basic raider armor, louisville slugger and bino spawners
to Raider Town
add: a few more carpiles around the map
add: a Raiders minidungeon for books 1-3, since everyone else gets it
now it seems
fix: the new Kebab Town (Mobs are harder now. Beware..!) 
remove: the followers Reagent Gun (AGAIN. I did this before and someone
RE-MAPPED IT IN.)
remove: that one dumb as shit rad-puddle from infront of the BOS base 
remove: the force-spawn gauss rifle in no mans land (replaced with
experimental spawner)
add: bodybags for followers
edit: the E-Weapon spawners to the following - | Low = AEP7, Wattz, (low
chance) Wattz Magneto (someone made the AEP7 midtier for some bullshit
reason) | Mid = AER9, Plaspistol, (low chance) Wattz 2k | Mid-High =
AER12, AER9, (low chance) Ion Rifle | High = Plasrifle, Wattz 2kE, RCW,
Tribeam,(low chance) AER14
edit: the Experimental Spawner to the following: M72 Gauss | Peacekeeper
| P90 | Gatling Laser
edit: the Peacekeepers stats (Applied auto-fire shot delay of 2.8 from
1)
fix: Fixed the Remnant Bunker shoot-through wall things by replacing
them
fix: Fixed BOS NML entrance and Enclave NML Entrance
fix: Replaces NML PA claw with an edited Junker Boss (he is hard)
fix: Fixes the boss not firing
remove: the invincible interior walls in kebab, replacing them with
r_walls
fix: NML Turrets shooting NML mobs
tweak: NML kebab melee mobs and boss mobs have melee AP
add: 2 ghoul spawners to north nml + static glowing one
remove: 2 legendary ghouls from north nml
add: 4 ranged mutant spawners to south nml
remove: 2 legendary super mutants from south nml
add: 6 more turrets throughout NML (3 north, 3 south - 2 at each
building, 1 for each exterior melee weapon spawn)
add: renegade flags to kebab
🆑

---------

Co-authored-by: maaacha <116771811+maaacha@users.noreply.github.com>

---
## [Runian/Yogstation](https://github.com/Runian/Yogstation)@[5c140d7624...](https://github.com/Runian/Yogstation/commit/5c140d7624b7b9f904d5bd78602d2fb0ee33a9ec)
#### Sunday 2023-12-17 19:29:33 by Aquizit

[ICEMETA] Fixes Hermit and Walker Spawns (Walkers disabled in config see PR text) (#21065)

* name + config fixes

* fix walker - disabled, redo hermit flavor text

* fuck your stupid uncapitalized t

---
## [amandarichardsonn/SmartSim](https://github.com/amandarichardsonn/SmartSim)@[1e686ead0d...](https://github.com/amandarichardsonn/SmartSim/commit/1e686ead0d374ab8f41fba7b2d1667e1350e193f)
#### Sunday 2023-12-17 20:20:34 by Ben Albrecht

SmartSim Singularity Integration (#204)

[committed by @ben-albrecht]
[reviewed by @ashao]

This PR adds the ability for SmartSim to launch workloads in Singularity (Apptainer) as described in https://github.com/CrayLabs/SmartSim/issues/101. It also lays the groundwork for supporting other container runtimes such as docker, shifter, and podman in the future, as well as launching the orchestrator in a container.

## Design Variations

During development, it became clear that a few design changes from the original proposal were required. I have documented them below with their rationale:

#### 1. Argument name: `bind_paths` -> `mount`

The terms bind path and mount are mostly used interchangeably across different container runtimes. When writing tests, I kept forgetting if it was `bind_path` or `bind_paths`, which hinted to me that it was not a great arg name, so I swapped it out for the more succinct and easy to remember `mount`.

#### 2. `create_run_settings(..., container: str)` -> `create_run_settings(..., container: Container)`

We originally thought it would be easier for users to get started with containers by allowing them to pass a string into `create_run_settings(container='singularity')` instead of having to create a Container object. While writing tests, I realized that this was potentially very confusing for users because 1) the `container` arg types change between `create_run_settings` and `RunSettings`, and 2) if you need to add other metadata such as container args or container mount paths, you have to switch from using `create_run_settings` to `RunSettings` in your code, which is very annoying. Because creating Containers is so lightweight, I think it is best to keep the container interface consistent across all functions that accept them.

#### 3. dropped getter/setter methods

Because command generation and validation happens upon execution, users can freely modify `Container.args` and `Container.mount` without getter/setter methods to update any other state. Therefore, I dropped these methods from the interface.

## Testing

Added 2 test suites for containers: One for WLM testing and one for local testing. The local testing suite runs in GitHub actions. Due to the added time from building Singularity and pulling the `container-testing` image, the singularity testing only happens on one configuration of the build matrix: python 3.9 + redisai 1.2.5 on linux

---
## [naelsoufi/genealogy-generator](https://github.com/naelsoufi/genealogy-generator)@[383a9d8046...](https://github.com/naelsoufi/genealogy-generator/commit/383a9d8046d6ffa9208d9fdaa9dc92000960f9a8)
#### Sunday 2023-12-17 20:56:52 by Naël

I am a dumbass

Yeah previous update is empty. This is the real one.
Fucking hell.

---
## [JimKil3/Shiptest](https://github.com/JimKil3/Shiptest)@[caa19d2a6f...](https://github.com/JimKil3/Shiptest/commit/caa19d2a6f8014c2d34663c7c63685921bc0218a)
#### Sunday 2023-12-17 21:37:29 by GenericDM

Assorted cringe removal pt.whatever (#2534)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Removes more cringe I found laying around.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
/tg/ was on some WILD shit.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
del: removes tail club
del: removes all flavors of tail whip
del: removes lizardskin clothing
del: removes 'Genetic Purifier'
tweak: makes bunny ears desc not incredibly sexist
tweak: change up wording in magic mirror gender change
del: removes 'genuine' cat ears
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [CDRDecky/f13babylon](https://github.com/CDRDecky/f13babylon)@[3c052bcd6d...](https://github.com/CDRDecky/f13babylon/commit/3c052bcd6d3ff02680c3fe1f15151549154eb162)
#### Sunday 2023-12-17 21:38:18 by Mazzinsanity

Main Fallout13 Medicine Rework (#113)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request
This PR aims to bring a number of changes to the way the main Fallout13
medicines function.

Stims remain the vanilla videogame healing item they were, stronger than
tribal medicine at healing brute and burn damage, but lacking in
specialization. On the other hand, tribal medicine has been given a new
breath of life in the form of excelling in certain damage types and
increased healing from wounds.

Activation delays for certain healing items have been changed:
- Hydra/Med-X/Psycho/Turbo - 1 second on yourself / 3 seconds on others
- All forms of gauze/sutures/mesh/ointment - 3 seconds for yourself / 1
second on others

Using the stimpak as a base, here are the healing rates for brute/burn
healing for the healing items:
1. Super stimpak - 225% of base stimpak strength
2. Imitation super stimpak - 188% of base stimpak strength (75% of super
stimpak strength)
3. Bitter drink -180% of base stimpak strength for tribals / 133% for
non-tribals
4. Healing poultice - 115% of base stimpak strength for tribals / 87.5%
for non-tribals
5. Imitation stimpak - 75% of base stimpak strength
6. Healing powder - 75% of base stimpak strength for tribals / 55% for
non-tribals

All medicine now heals burn damage at 75% of its healing power for brute
damage.

Powder/poultice/bitters/hydra will not heal when any stimpak fluid
variant is in the system. Stimpak fluid will not heal when
powder/poultice/bitters are the system.

Only one medicine is able to heal at a time. This medicine must be the
weakest one currently in the system:
- For example, if super stim fluid is present in the body, and regular
stim fluid is introduced, then the super stim fluid will stop healing,
while the regular stim fluid heals.
- If imitation stim fluid is added, then regular stim fluid stops
healing, and only imitation stim fluid can heal.
- If at any point powder/poultice/bitters are added, no medicine will
heal.
- The same logic follows for powder/poultice/bitters.

All stimpaks have lost the ability to additionally heal bodyparts with
each wound applied to that bodypart. The logic behind this property has
been reworked and moved to tribal medicine.

All stimpaks have retained their ability to clot active pierce/slash
wounds, reducing their bleed rates.

All medicine has lost its crit stabilizing properties.

Bitter drink no longer heals radiation and has reduced toxin and oxyloss
healing rates.

Healing poultice now excels at healing radiation and toxin damage, as
strong as the super stimpak brute healing rate. Healing powder now
excels at healing oxyloss damage, as stong as the super stimpak brute
healing rate.

The overdose effects for all main healing medicines have had their
damage values tweaked and additional drawbacks added.

Using stims as Legion now causes serious side-effects, including
vomiting, confusion, dizzyness and jitteriness. Using
Med-X/Psycho/Buffout/Jet/Turbo as Legion/NCR/BoS/Enclave now also causes
these side-ffects. As such, Psycho and Turbo have been removed from
Enclave loadouts.

2 new negative quirks are now available for selection: Stim Intolerance
and Straight Edge:
- Stim Intolerance makes you vomit, causes dizziness, jitteriness and
confusion whenever any variant of stim fluid enters your body.
- Straight Edge makes you have the same effects but with Fallout chems
like Psycho/Med-X etc.

New positive quirk available for selection: Herbal Affinity:
- Grants bonus healing from tribal medicine and removes the negative
side-effects

Roles that start with these quirks already allocated to them
(NCR/Legion/BoS/Enclave) cannot select these quirks for free points.

Small miscellaneous tweaks and fixes, such as crafting time changes for
medicine, are present as well.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
The current roster of Fallout13 medicine is somewhat unbalanced and
needs a little love. This aims to do that by making superstims act as
vanilla jack-of-all-trades healing items, while making the tribal
medicines specialize in certain damage types to fill the gaps left by
their inability to use chem machines while also making them grow
stronger as the user gains more wounds, taking into account the low
wound armor and hit-and-run, all-or-nothing gameplay that Tribal and
Legion roles have.

The side-effects changes for Med-X/Psycho/Turbo/Buffout were made to
counteract powergaming and circumvent factions breaking their lore in
order to gain an upper hand in a fight.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [x] You tested this on a local server.
- [x] This code did not runtime during testing.
- [x] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
add: Added side-effects for the 4 major factions upon Fallout chem use
add: Added side-effects for Legion upon stim use
add: Added 2 new negative quirks - Stim Intolerance and Straight Edge
tweak: Tweaked medicine crafting times
tweak: Tweaked time delays on medicine application
balance: Rebalanced the main Fallout13 healing chemicals
fix: Fixed incorrect poultice x50 batch crafting requirements
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Yawet330 <65188584+Yawet330@users.noreply.github.com>

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[a1e46c5d31...](https://github.com/Ical92/tgstation/commit/a1e46c5d31347887de95520eee31c00749379b9c)
#### Sunday 2023-12-17 22:09:04 by Jacquerel

Basic Guardians/Holoparasites (#79473)

## About The Pull Request

Fixes #79485
Fixes #77552

Converts Guardians (aka Holoparasites) into Basic Mobs.
Changes a bunch of their behaviours into actions or components which we
can reuse.
Replaces some verbs it would give to you and hide in the status panel
with action buttons that you may be able to find more quickly.

They _**should**_ work basically like they did before but a bit
smoother. It is not unlikely that I made some changes by accident or
just by changing framework though.

My one creative touch was adding random name suggestions.
The Wizard federation have a convention of naming their arcane spirit
guardians by combining a colour and a major arcana of the tarot. The
Syndicate of course won't truck with any of that mystical claptrap and
for their codenames use the much more sensible construction of a colour
and a gamepiece.

This lets you be randomly assigned such creative names as "Sparkling
Hermit", "Bloody Queen", "Blue World", or "Purple Diamond".
You can of course still ignore this entirely and type "The Brapmaster"
into the box if so desired.

I made _one_ other intentional change, which is to swap to Mothblocks'
nice leash component instead of instantly teleporting guardians back to
you when they are pulled out of the edge of their range. They should now
be "dragged" along behind you until they can't path, at which point they
will teleport. This should make the experience a bit less disorienting,
you have the recall button if you _want_ to instantly catch up.

This is unfortunately a bumper-sized PR because it did not seem
plausible to not do all of it at once, but I can make a project branch
for atomisation if people think this is too much of a pain in the ass to
review.

Other changes:
- Some refactoring to how the charge action works so I could
individually override "what you can hit" and "what happens when you hit"
instead of those being the same proc
- Lightning Guardian damage chain is now a component
- Explosive Guardian explosive trap is now a component
- Added even more arguments to the Healing Touch component to allow it
to heal tox/oxy damage and require a specific click modifier
- Life Link component which implements the Guardian behaviour of using
another mob as your health bar
- Moved some stuff about deciding what guardians look and are described
like into a theming datum
- Added a generic proc which can return whether your mob is meant to
apply some kind of damage multiplier to a certain damage type. It's not
perfect because I couldn't figure out how ot cram limb modifiers in
there, which is where most of it is on carbons. Oh well.
- Riders of vehicles now inherit all movement traits of those vehicles,
so riding a charging holoparasite will let you cross chasms. Also works
if you piggyback someone with wings, probably.

## Changelog

:cl:
refactor: Guardians/Powerminers/Holoparasites now use the basic mob
framework. Please report any unexpected changes or behaviour.
qol: The verbs used to communicate with, recall, or banish your Guardian
are now action buttons.
balance: If (as a Guardian) your host moves slightly out of range you
will now be dragged back into range if possible, rather than being
instantly teleported to them.
balance: Protectors now have a shorter leash range rather than a longer
one, in order to more easily take advantage of their ability to drag
their charge out of danger.
balance: Ranged Guardians can now hold down the mouse button to fire
automatically.
balance: People riding vehicles or other mobs now inherit all of their
movement traits, so riding a flying mob (or vehicle, if we have any of
those) will allow you to cross chasms and lava safely.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [Sala/adventofcode](https://github.com/Sala/adventofcode)@[2e48c12d54...](https://github.com/Sala/adventofcode/commit/2e48c12d54aa57038e0284ed3e2a0fb5c88f3235)
#### Sunday 2023-12-17 22:10:39 by sala

a mix of sadness, frustration with a little sprinkle of learning.
I've implemented a decent (not that fast) solution in the first hour, but I somehow included the start into the calculation, even though I was 100% sure I was not. I've checked that part multiple times and still nothing.
the good part is that this forced me to read more about other types of algorithm except dijkstra and to better understand how they work and how they can be optimized.
the final solution is not amazing, but it's working.
yeah, it wasn't a good day for science.

---
## [jamani133/Autonomes_Auto](https://github.com/jamani133/Autonomes_Auto)@[71c4ec5552...](https://github.com/jamani133/Autonomes_Auto/commit/71c4ec5552b778544f7582a7aafd96cab4871904)
#### Sunday 2023-12-17 22:46:44 by jamani133

FUCK YOU

fixed the turny shut
fixed the not worky shit
fixed the coor shit
fixed the direction shit
todo:
fix me

also added release btw

---
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[89887b54f6...](https://github.com/RustingWithYou/Aurora.3/commit/89887b54f64bb9c8971eb68e9a36ec7b61c5fb0b)
#### Sunday 2023-12-17 23:10:38 by RustingWithYou

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

fuck this event

---
## [RustingWithYou/Aurora.3](https://github.com/RustingWithYou/Aurora.3)@[140bf3f5c7...](https://github.com/RustingWithYou/Aurora.3/commit/140bf3f5c742dce484a9189d817beb63512a344f)
#### Sunday 2023-12-17 23:11:56 by RustingWithYou

kaneyama power station

punch sounds & corpses

jungle map & icon fix

sounds

zombie village

glowing screen: you should kill yourself, now

light

kaneyama map

punch sounds & corpses

jungle map & icon fix

sounds

zombie village

glowing screen: you should kill yourself, now

kaneyama map

punch sounds & corpses

jungle map & icon fix

sounds

zombie village

bridge & icons

shuttl

grass

spawnroom

byeah

checkpoints

sovl

CONTENT

plant

da files

icons & assets

byeah

big hivebot icon

ecd

messages

ECD as easy as 1-2-3

a bunch of shit

TREES

grass

areas

byeah

guns

title screen

ambience

rain & water

ligt

power

also apc fixes

tcomms fix

ecd

spooking the synthetics & slowdown

fuck you, point verdant

area check works

byeah

---
## [f13babylon/f13babylon](https://github.com/f13babylon/f13babylon)@[667500fde5...](https://github.com/f13babylon/f13babylon/commit/667500fde5871478747cdd48d7624dab6bb42c8f)
#### Sunday 2023-12-17 23:23:31 by Stutternov

Fire Delay Fix & Bolt Action Overhaul (#366)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

<!-- NOTE: This format is NOT REQUIRED for things like runtime fixes,
code fixes and optimizations. In those instances you should try to give
a description of what is being fixed or optimized but are not required
to fill out the complete changelog. -->
<!-- Adjusting things like armor or weapon values for balance, while
they may be 'fixes' in their own way, are not considered code fixes as
described above and require the use of the Pull Request format below.-->


## About The Pull Request

So - funny thing. Fire delay NEVER worked properly on this codebase
since the change of the way fire delay worked to a different proc.

I have reversed this and re-adjusted fire delays for guns, at people
clearly were balancing them around the 'fire_delay' proc that wasn't
working. While some guns had 0 fire delay and seemed to function fine,
upon fixing - you realize **"Oh this fires literally as fast as you can
possibly click."**

As such, this is an attempt at balancing gun fire delays. Honestly -
this is a great thing, since I think with these new values (which need
to be tested a bit first) that guns like the Rangemaster and M1 garand
are finally viable alternatives to, say, the DKS. The main issue I see
is guns will be firing faster in some ways across the board due to this
fix so we'll need to slowly fix this via testing to where a gun should
be.

**Bolt actions have also been overhauled.**
Bolt actions are now viable again, as they are better damage, some
bullet speed, and being relatively equal to their automatic
counterparts. Their downside is the fact they are bolt action and, for
some, have limited capacities.

The Remington, for example, now does near equal damage to the DKS but
only has a 5 round capacity, less penetration, and is stripper-clip fed.

The Varmint has also been re-made into a boltaction rifle, effectively
being a 'near equal' to the service rifle albeit bolt-action. It has
some extra pen (only by about 0.1) and extra speed to its bullets,
making it more of a marksman rifle rather than putting bullets down
range better.

**Misc balance adjustments**
Since firedelay needed to be changed, since we have kept changing fire
delays.. despite them not fucking working, guns like the Marksman have
been buffed while others, like the R-91, have had their role
re-evaluated some.

Examples:
- Marksman carbines are now same fire delay as service rifles, but due
to rarity pack some extra damage and penetration in exchange for a bit
more slowdown.
- R-91 lost its damage malice but also its extra pen, instead making it
more of a good automatic weapon.

## Why It's Good For The Game

Either an oversight or a really silly change that broke fire delays on
guns for quite awhile now. Other changes to balance were needed to
balance guns against eachother.

## Pre-Merge Checklist
<!-- Don't bother filling these in while creating your Pull Request,
just click the checkboxes after the Pull Request is opened and you are
redirected to the page. -->
- [X] You tested this on a local server.
- [X] This code did not runtime during testing.
- [X] You documented all of your changes.
<!-- Neither the compiler nor workflow checks are perfect at detecting
runtimes and errors. It is important to test your code/feature/fix
locally. -->


## Changelog
<!-- This is mostly optional for small Pull Requests, but if you value
being credited for your work in-game be sure to fill it out. To opt-out,
remove everything below including the start and end :cl: brackets. -->

<!-- If your Pull Request includes a minor single line variable edit,
probably do not fill out this changelog. -->
<!-- However, if your pull request includes massive or immediately
noticeable changes, briefly describe those changes in some way in this
changelog. -->

:cl:
balance: Re-balances ALL gun fire delays.
fixes: Removed CD_Firedelay in gun proc in exchange for the ACTUALLY
used fire_delay proc
tweak: Moves varmint rifle to being bolt action as well as its variants.
Also buffs them to be competitive while being bolts.
balance: Re-does quite a few guns (Marksman, hunting rifle, remington,
R-91, etc) to make them balance against eachother better due to firerate
changes.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: macha <likeacompleteboss@gmail.com>
Co-authored-by: maaacha <116771811+maaacha@users.noreply.github.com>

---
## [MelokGleb/tgstation](https://github.com/MelokGleb/tgstation)@[81a7c75583...](https://github.com/MelokGleb/tgstation/commit/81a7c75583f75f76d8487b88e63ebaf1402af85b)
#### Sunday 2023-12-17 23:45:08 by necromanceranne

Hey what if I made Sleeping Carp better at nonlethal takedowns and also deflect with combat mode instead of throw mode (but cost more) (#79517)

## About The Pull Request

It's been a hot minute hasn't it?

When I initially reworked Sleeping Carp, we didn't have combat mode. Now
that we do, and that Sleeping Carp has substantially less defensive
power to justify having to make a choice between deflection and
attacking, it's probably about time we updated this aspect back to what
it was before my rework. Sorta.

Now, we can have all the deniability of the previous method, while also
letting you reliably protect yourself from ranged attacks at all times
while it matters. Because of this, I increased the price up to 17 TC
because of this change just to be on the safe side. The higher uptime of
projectile immunity while also being able to attack during that time
makes this a lot stronger overall.

Secondly, Sleeping Carp presently just isn't as good as a good ol'
baton. It takes a lot more hits to accomplish the same task that a baton
can. Many people feel like they can't even reasonably fight anyone for
fear of the baton, or they would rather use a baton and kill someone at
their leisure. So we've updated some of the moves in order to facilitate
Sleeping Carp as a substantial contender for 1v1 fighting, and lessen
the need for a baton by adding a lot more Stamina damage overall to the
various attacks;

**Keelhaul**: Now a Shove Shove combo. Does literally zero lethal
damage, but now temporarily blinds and dizzies the target as well as its
previous effects. The amount of lethal damage it did was...extremely
small, so this isn't a particularly big loss.

**Grabs and Shoves**: Deal some amount of stamina damage (20). You need
to be in combat mode in order to perform these special attacks (more
deniability). Grabbing someone while they have 80 Stamina damage or more
will cause them to fall unconscious. Yes, I really did just want to add
a Vulcan Nerve Pinch, what do you want from me?

That's it actually. Oh, I guess they are heavy sleepers now too. Because
its funny.

## Why It's Good For The Game

I often get told (read: thrown various insults and slurs at me while
mentioning this as the justification) that Sleeping Carp is not very
strong anymore since it lost all that invisible armor I added way back +
I removed the stuns in my initial rework. This made some people upset (I
think at least one person wished for my death).

So, having given it at least 2 years, I wanted to recapture parts of
what made the older Sleeping Carp (before my rework) strong, some of the
benefits of the new version, and introduce a brand new aspect; nonlethal
takedowns. This makes it beneficial for pacifists, as well as for
kidnapping.

This should not meaningfully make Sleeping Carp any stronger against the
things that typically ruin its day. I suspect in a straight joust with a
baton, Sleeping Carp will still struggle. But against what should be its
strong points (lone targets and ranged weapons), it will be strong once
again rather than clumsily unable to do very much at all.

## Changelog
:cl:
balance: Harnessing Shoreline Quay (bluespace energy, probably), a
mystical energy (total bullshit) that permeates the Astral Waterways
(bluespace quantum dimensions, probably), Sleeping Carp users can now
once against deflect projectiles with their bare hands when focused in
on battle (in combat mode).
balance: The Keelhaul technique is now nonlethal (a philosophical
acknowledgement of the familial bond of sleep and death), but causes the
target to become temporarily blind and dizzy along with its previous
effects.
balance: Sleeping carp users, while in combat mode, deal Stamina damage
with their grabs and shoves. If the target of their grab has enough
Stamina damage (80), they are knocked unconscious from a well placed
nerve pinch.
balance: Sleeping carp users find it very hard to wake up once they fall
asleep....
/:cl:

---
## [rmellis/HelpUKR-master](https://github.com/rmellis/HelpUKR-master)@[57f743d2e6...](https://github.com/rmellis/HelpUKR-master/commit/57f743d2e687164920a1927f2ae041a6dfb0878d)
#### Sunday 2023-12-17 23:48:40 by rmellis

Added Day 662 - Targets and Days (TL) Eng+Ukr

Simply run this for as long as you can to help flood Russia in the most legal, yet effective way possible 
New targets imported from db1000n:
To keep up with targets we're going to use the db1000n targets direct from their GitHub repository. 
These updates will be daily, so if the db1000n changes, it will probably take a few hours longer for the change to make it here.
Message posted by the IT Army of Ukraine:
lmatel and 2Kom, two major internet providers in the aggressor's capital, were disrupted this morning, impacting countless private, business, and government subscribers. This is all thanks to your efforts and our team's precise planning. While it's not as large as the KyivStar outage, it's a significant impact. The more devices you add, the more we can weaken the aggressor's infrastructure. Bring your friends into the IT ARMY! 🌐💻🛡️
/ *** / 
Просто запускайте це стільки, скільки зможете, щоб допомогти наповнити Росію найбільш законним, але ефективним способом 
Нові цілі, імпортовані з db1000n:
Алмател та 2Ком - два величезні інтернет-провайдери у столиці агресора перестали працювати сьогодні вранці. Це має бути десятки, якщо не сотні тисяч приватних, бізнес та урядових абонентів. Коли повернуться невідомо, але це все завдяки вашим зусиллям і ювелірної підготовки нашої команди розвідки. Це поки не масштаб збою КиївСтар, але хто знає яку операцію ми зможемо провести наступною?
Чим більше ви долучаєте девайсів, тим більше шкоди ми зможемо нанести інфраструктурі агресора. Приєднуйте до IT ARMY ваших друзів!

---

