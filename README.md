## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-11](docs/good-messages/2023/2023-05-11.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,046,992 were push events containing 3,408,915 commit messages that amount to 248,783,382 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 66 messages:


## [tadryanom/openbsd_src](https://github.com/tadryanom/openbsd_src)@[e4c559e853...](https://github.com/tadryanom/openbsd_src/commit/e4c559e853ce1cc130d8342715a65ada3e5f26e9)
#### Thursday 2023-05-11 00:10:59 by tb

Move a few functions out of OPENSSL_NO_DEPRECATED

Geoff Thorpe added OPENSSL_NO_DEPRECATED nearly two decades ago. The hope
was that at some point some functions can be dropped. Most of the functions
marked deprecated are actually unused nowadays but unfortunately some of
them are still used in the ecosystem. Move them out of OPENSSL_NO_DEPRECATED
so we can define it without breaking the consumers in the next bump.

ERR_remove_state() is still used by a dozen or so ports. This isn't a big
deal since it is just a stupid wrapper for the not quite as deprecated
ERR_remove_thread_state(). It's not worth patching these ports.

Annoyingly, {DH,DSA}_generate_parameters() and RSA_generate_key() are still
used. They "make use" of the old-style BN_GENCB callback, which is therefore
more difficult to remove - in case you don't know know: that's the thing
responsible for printing pretty '.', '+' and '*' when you generate keys.

Most annoyingly, DH_generate_parameters() was added to rust-openssl in 2020
for "advanced DH support". This is very unfortunate since cargo bundles a
rust-openssl and updates it only every few years or so. As a consequence
we're going to be stuck with this nonsense for a good while.

ok beck jsing

---
## [newstools/2023-daily-dispatch](https://github.com/newstools/2023-daily-dispatch)@[d5d32c92b2...](https://github.com/newstools/2023-daily-dispatch/commit/d5d32c92b220e6a2d4d16d8d3e07a142beed9757)
#### Thursday 2023-05-11 00:14:21 by Billy Einkamerer

Created Text For URL [www.dispatchlive.co.za/news/2023-05-10-two-life-terms-for-north-west-man-who-killed-ex-girlfriend-and-her-mom/]

---
## [michalnpl/terminal](https://github.com/michalnpl/terminal)@[6ad8cd0a63...](https://github.com/michalnpl/terminal/commit/6ad8cd0a630ab927629841a14d433c3bc19a1509)
#### Thursday 2023-05-11 00:33:26 by Mike Griese

Make conhost act in VtIo mode earlier in startup (#15298)

We need to act like a ConPTY just a little earlier in startup. My relevant notes start here: https://github.com/microsoft/terminal/issues/15245#issuecomment-1536150388. 

Basically, we'd create the first screen buffer with 9001 rows, because it would be created _before_ VtIo would be in a state to say "yes, we're a conpty". Then, if a CLI app emits an entire screenful of text _before_ the terminal has a chance to resize the conpty, then the conpty will explode during `_DoLineFeed`. That method is absolutely not expecting the buffer to get resized (and the old text buffer deallocated). 

Instead, this will treat the console as in ConPty mode as soon as `VtIo::Initialize` is called (this is during `ConsoleCreateIoThread`, which is right at the end of `ConsoleEstablishHandoff`, which is before the API server starts to process the client connect message).  THEORETICALLY, `VtIo` could `Initialize` then fail to create objects in `CreateIoHandlers` (which is what we used to treat as the moment that we were in conpty mode). However, if we do fail out of `CreateIoHandlers`, then the console itself will fail to start up, and just die. So I don't think that's needed.

This fixes #15245. I think this is PROBABLY also the solution to #14512, but I'm not gonna explicitly mark closed. We'll loop back on it.

---
## [MedNet-Technologies/proyecto-medset](https://github.com/MedNet-Technologies/proyecto-medset)@[278485669a...](https://github.com/MedNet-Technologies/proyecto-medset/commit/278485669a411dcb74c7e9340f67603c8b199905)
#### Thursday 2023-05-11 00:59:20 by Risuban

this shitty ass view is finally functional, godd damn

---
## [norsvenska/tgstation](https://github.com/norsvenska/tgstation)@[8fa6242c66...](https://github.com/norsvenska/tgstation/commit/8fa6242c66205866b702440f490eeae34ef6b85f)
#### Thursday 2023-05-11 01:24:31 by Bloop

Refactors High Luminosity Eyes, fixes a ton of bugs related to it as well as qol improvements (#75040)

## About The Pull Request

The high luminosity eyes item was extremely out of date, broken, and
full of copy paste code from atom lighting. Which is a shame because
they were cool.

On top of all that it was using a special light effect that was not very
performant. I got rid of all that, hooked it into atom lighting as a new
light type, and gave it a new TGUI as well because the old ui prompts
were not great either.

You can now pick a color at random if you want. You can also set the
color and range before surgically implanting them. No more being forced
to go through the color picker when you just want to change the range.

Functionally they should pretty much should be the same as before with
some bonus features (see below).


![dreamseeker_nDeLNyOOG2](https://user-images.githubusercontent.com/13398309/235325530-105fe82e-ecc8-4dc4-9c84-143cc6519688.gif)

Closes https://github.com/tgstation/tgstation/issues/61041
Closes https://github.com/Skyrat-SS13/Skyrat-tg/issues/14685

This is 100% completed. I just finished fixing the slight translation
bug when going from 0->1 range (see above gif) and that was the last
thing on my bucket list. I happy enough with this at this point in time.

---

EDIT: 

I have decided to add in one last new feature, and that is...
independent settings for eye color.

<details> <summary>You can now set eye color independently if you
wish</summary>


![dreamseeker_j32B2S4yXQ](https://user-images.githubusercontent.com/13398309/235412568-ffa8e424-8624-4462-9f6f-77c1513aa773.gif)

</details>

The eye color does not modify the light color in any way when set in
this manner, but it can be used for cosmetic purposes.

Kind of makes the item more like cybereyes from cyberpunk, which I think
are pretty neat!

</details>

### What I've done, in more detail:

- refactored high luminosity eyes so they use the atom lighting system
instead of the way they were doing it before
- the new light type, `MOVABLE_LIGHT_BEAM` behaves similarly to
directional lights, with some slight differences. it reuses the same
lighting overlay sprites but scales them vertically to produce a more
focused effect. The result can be seen above. This is in contrast to the
old way, which spawned `range` number of individual 32x32 overlays and
moved them around. This way should perform better as well as be more
maintainable.
- added a new TGUI interface for high luminosity eyes with buttons for
range, a text field for a color hex, a color picker and randomizer
- made the eye overlay emissive when the light is turned on
- range goes from 0 to 5. at range 0, the light overlay is turned off
and you are left with just the emissive eyes.
- added a cosmetic functionality to this item that lets you change the
color of your eyes independently of the lighting (and each other)
- fixed a bug with directional flashlights sometimes not updating their
lighting overlay if you pick them up without changing your direction
---

### Other Misc Fixes

Being able to dynamically set range back and forth exposed some logic
issues that had existed with directional light overlays and I have fixed
those. That is why there are some edits in that file that may not appear
readily obvious why they are there.

Apart from that, two other bugs that come to mind:
1) eye code was supposed to keep track of the eye color you had before
you got new eyes, but it was overwriting that every time you ran
refresh().
2) lighting was supposed to be turning off the light when range is set
to 0, but it was not doing that properly.

And of course besides that, there may have been a few instances of
finding typos/tidying up code

## Why It's Good For The Game

The code for this was like 6 years old and in desperate need of
updating. Now it works, and has a nicer UI.

## Changelog

:cl:
fix: high luminosity eyes light overlays now follow the user correctly
qol: high luminosity eyes now have a tgui menu so you no longer have to
go through the color picker every time you want to change the range.
they also have a new setting that lets you change the color of your eyes
independently of the light color. You can now have cybernetic
heterochromia if you want
fix: directional flashlights when picked up will now always update their
cast light direction correctly no matter what dir you are facing
refactor: refactors high luminosity eye code to better make use of the
atom lighting system, adding a new light type 'MOVABLE_LIGHT_BEAM'
/:cl:

---
## [ShizCalev/tgstation](https://github.com/ShizCalev/tgstation)@[b3ef9dd6d4...](https://github.com/ShizCalev/tgstation/commit/b3ef9dd6d431a36193c12625d2e86e57fe56dc79)
#### Thursday 2023-05-11 01:24:32 by John Willard

Nerfs the firing speed of Syndicate/Russian mobs (#75247)

## About The Pull Request

Nerfs their firing speed from once every 0.2 seconds to once every 2.5
seconds

## Why It's Good For The Game

1. The mob that is NOT a 'burst' type mob, is firing every 0.2 seconds.
Kinda defeats the point of having them as two separate mobs, so this
aims to fix that.
2. Russian mobs. Turns out that letting them fire their strong-ass gun
every 0.2 seconds was kinda not a good idea. I had assumed making them a
Syndicate mob would be safe, and it technically is, it's just that
Syndicate mob is fucked itself.

## Changelog

:cl:
balance: Default Syndicate and Russian gunners now fire every 2.5
seconds instead of every 0.2
/:cl:

---
## [Harrymanual/Formula_1_Website_React](https://github.com/Harrymanual/Formula_1_Website_React)@[1e5a6567c7...](https://github.com/Harrymanual/Formula_1_Website_React/commit/1e5a6567c7b69e94d0714fb2dbdb5890d3b42024)
#### Thursday 2023-05-11 02:14:39 by Harrymanual

big bopper ipdates here today

- first things first the scripts are now writing to public instead of src, apoparently you cant uise fs on a web application, never would have guessed that after spending hours on it. Anyways turns out you have to use fetch and this led me to my second problem. Why is fetch outputting html, well a few hours later i simply discovered that it just doesnt work and i still dont know why. But i did discover the public folder you can just whack in all your static stuff there and since im not using a serrver i may as well just do that so now all my scripts have been changed to write to  the public folder which was a bit annoying but whatever and finally i have the barebones to make information display yay go me!!!!!!!!!!!!!
- also updated app to make the other team pages work now and yeah thats what were rocking with

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[1a918a2e14...](https://github.com/tgstation/tgstation/commit/1a918a2e1411f58e5a90f587a92daebebb9ac395)
#### Thursday 2023-05-11 02:52:44 by Jacquerel

Golem Rework (#74197)

This PR implements this design document:
https://hackmd.io/@Y6uzGFDGSXKRaWDNicSiEg/BkRr176st
Put briefly, this will remove every existing golem subtype and
consolidate golems into a single species with cool new sprites.
NOT implemented from that PR is the ability to eat Telecrystals, I
couldn't come up with an appropriate visual that can stack with the
existing ones, but that should be a reasonably trivial add for a future
artist & developer.

New Golems have a food-based mechanic where their hunger decays pretty
quickly and can only be replenished by eating minerals. They start
moving slower as they get hungrier, until eventually they become
completely immobilised and need to be rescued.
Eating different kinds of minerals will visually change your sprite and
give you a special effect in a similar way to old golems, but temporary.
While transformed, you can't eat any other kind of mineral which would
transform you (but can still consume glass).
To see the full list of effects, look at the hackmd above.

In service of these sprites working I have refactored the
`species/offset_features` feature by killing it and delegating that
responsibility to limbs instead. Rather than applying an offset to items
due to your species, it is due to your weird head or arms. This makes
overall more sense to me, but it inflates the code changes in this PR
somewhat.
It doesn't make a lot of sense to atomise unfortunately because that
code also seemed to be entirely unused until I tried to use it in this
PR, so you wouldn't be able to tell if my changes broke anything. I
might make a downstream sad by doing this.

All of the actual numbers in this PR are made up and only loosely
tested, it will need some testmerges to gather feedback about whether it
sucks or not.

Other relevant changes:
I reworked how bioscrambling works based off bodypart bodytypes, to
automatically exclude golem limbs in either direction. There's really no
way to have those work on humans or vice versa. Organs still fly though.

---
## [SilverAndro/quilt-standard-libraries](https://github.com/SilverAndro/quilt-standard-libraries)@[5645325042...](https://github.com/SilverAndro/quilt-standard-libraries/commit/5645325042583ef2912bc3933f1997c40230d48a)
#### Thursday 2023-05-11 02:59:38 by SilverAndro

God i fucking hate git lmao

All squashed commits, newest first:
Cleanup some line lengths, signing rollback support
Add getters and `withX` methods to CommandC2SMessage
remove some unused shadows
mappings note, server side message removal (i think)
whoops missed a `with` method
client side message removal events
minor cleanup
Honestly just need to save this work
Server side commands and verification
Move chat hook to impl, add hook origin in errors
minor cleanup
Honestly just need to save this work
Server side commands and verification
Move chat hook to impl, add hook origin in errors

---
## [Zytolg/tgstation](https://github.com/Zytolg/tgstation)@[f3549a4aec...](https://github.com/Zytolg/tgstation/commit/f3549a4aeca6701a2969a63b7d4034d5bc560cb6)
#### Thursday 2023-05-11 03:11:40 by Thunder12345

De-holes holy arrows (#75184)

## About The Pull Request

Covers the 2-pixel hole in the holy arrow sprite with 1 alpha pixels to
prevent unintentional missed clicks.

## Why It's Good For The Game

It's annoying and a bad experience to think you clicked on a sprite but
actually landed on a tiny transparent hole and clicked nothing or the
object below the one you wanted.

## Changelog
:cl:
image: Holy arrows are now 15% less holy (You can no longer click on the
2-pixel hole in the arrowhead and unintentionally click the object below
the arrow instead.)
/:cl:

---
## [diamondburned/cpsc-223c](https://github.com/diamondburned/cpsc-223c)@[01099ddc89...](https://github.com/diamondburned/cpsc-223c/commit/01099ddc892407902f66a5a5b531acc95a2d1526)
#### Thursday 2023-05-11 03:40:11 by Diamond Dinh

blog: Fix SEGFAULT on empty header

This was the entire reason why replit crashed. Holy shit. I hate this
language so much. I'm never going to use C willingly; that's just pain
and torture.

Also why does libonion even use my strdup? It should get its own strdup;
strdup isn't even standard! Though I should've called mine `my_strdup`,
but blame C for not standardizing strdup I guess :)

AAAAAAAAAAAAAAAAAAAA

---
## [fragglet/sdl-sopwith](https://github.com/fragglet/sdl-sopwith)@[003c49864a...](https://github.com/fragglet/sdl-sopwith/commit/003c49864a9905204f85cb5407befb531b19b64d)
#### Thursday 2023-05-11 04:02:31 by Simon Howard

Print some help in novice mode.

We only show this in novice mode, to avoid annoying players with experience,
and only when the player is parked at their home base. Hopefully this should
make the game a bit friendlier for new players.

---
## [isaacmg/MedFuse](https://github.com/isaacmg/MedFuse)@[6aad465050...](https://github.com/isaacmg/MedFuse/commit/6aad465050dde7fb75a26fc0869b21c834e43a0b)
#### Thursday 2023-05-11 04:30:50 by isaacmg

fixing bad lines

Stupid dogs keep barking and stupid shit shut the fuck and quit . Annoying everyone

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[56d960a763...](https://github.com/timothymtorres/tgstation/commit/56d960a7630d0b03bfcd59c073b29393a70a1891)
#### Thursday 2023-05-11 04:51:27 by GoldenAlpharex

Wintercoats can now be zipped and unzipped through alt-click and separates the hood sprites from the jacket sprites (#74886)

## About The Pull Request
The title says it all, really.

~~Initially, I was only going to do it for all wintercoats, but then I
figured I might as well bring it down to all of `/hooded`, just so other
suits could benefit from it, since that behavior came from there anyway.
Does that mean that it does nothing for some of them? Yes, it does. Does
that justify having another variable to tell whether or not that should
be possible? In my humble opinion, not really, but I'm not against it if
it's requested.~~

~~That functionality was intentionally removed from the Void Cloak, as
there would be balance implications (since bringing up the hood makes
the whole cloak invisible, which you could skirt by just "zipping" it,
which also makes it invisible.~~

~~The sprites were already there, so this change was very simple to do.
Simply unties the zipped up look from the fact that the hood is up.
However, toggling the hood forces the zipping/unzipping, just so there's
no balance implications involved. It's just simpler that way.~~

So, I ended up going back and changing the sprites so that the hoods
would no longer be baked into the jacket's sprites, so that they could
be done as overlays instead, which ended up solving my problem with
hoods not being there on zipped-up versions.

For now, it's been made on winter coats only, but it shouldn't be that
difficult to bring it back down to the `/hooded` level. I just didn't
want to bother touching up the sprites down there, as it already took me
like 2-3 hours touching up the sprites of the winter coats alone.

I also took the decision to make it so EVA winter coats used the regular
winter coat's sprites, because they had special ones that just looked
like worse versions of the original, without anything special going on
for them. It was just a straight downgrade compared to the base sprite,
in my opinion.

There's still issues with the custom winter coat, in that the hood isn't
made into an overlay for it yet (and that'll require an extra bit of
logic to make it work, too), but it was already an issue before, the
hood is always present on the current version of the custom winter coat.

There's still a handful (sadly, most) of the winter coats that don't
properly reflect on their obj sprites when they're opened versus when
they're closed, but that's due to an initial spriter oversight, and not
to my doing. The open versions were just left as closed on many of them,
and I simply don't have the patience nor the appropriate skills to edit
that many coats that way.

## Why It's Good For The Game
Now you can be stylish with or without the hoodie!

![image](https://user-images.githubusercontent.com/58045821/233544697-cc821c3a-d965-4d96-af44-c44ff866496f.png)

![image](https://user-images.githubusercontent.com/58045821/233544711-da956b6b-44c4-4903-a34f-4d2890abc781.png)

![image](https://user-images.githubusercontent.com/58045821/233544717-b5221b04-0e6d-4931-83d0-d56fdac60ec3.png)


According to ChatGPT, with one small tweak (thanks Opera GX for the
suggestion):

> Zipped and unzipped through alt-click, winter coats can now be. Hmm,
stylishly warm, you shall be. Feel like a Spaceman, you will. Use the
Force, to zip and unzip, you must. Look cool, you will. Yes, hmmm.

## Changelog

:cl: GoldenAlpharex, ChatGPT for the first changelog entry (slightly
edited)
qol: Zipped and unzipped through alt-click, winter coats can now be.
Hmm, stylishly warm, you shall be. Feel like a Spaceman, you will. Use
the Force, to zip and unzip, you must. Look cool, you will. Yes, hmmm.
image: Winter coats no longer have their hood baked into their jacket's
sprite, both in item form and when worn.
fix: Updated the Icebox EVA winter coats (the Endotherm winter coats) to
use the same sprites as the regular winter coats.
/:cl:

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [bsittler/meka](https://github.com/bsittler/meka)@[275abe066e...](https://github.com/bsittler/meka/commit/275abe066e3b5944c4e7103af6e513ebbf89fbb1)
#### Thursday 2023-05-11 05:04:19 by Benjamin C. Wiley Sittler

Add MAPPER_GG_Turbo_9_in_1_8000_4000 for "Turbo 9 in 1 [Street Fighter 2] (Unl)" GG multicart.

It is mostly working. One game (Choplifter) does not start, and there are glitches after restoring a save state that uses SMS-GG mode (glitchiness varies by game. some show wrong graphics, others reset, still others are fine.)

I qualified the name of Turbo 9 in 1 the first menu entry since there are apparently a bunch of very similarly-named cartridges with different menus/games, and the label description only makes sense when you are looking at the physical cartridge

It's an unlicensed Game Gear multicart with 9 games. The label says "TURBO 9 IN 1"

The box also says:
COLOR VIDEO GAME
SELECT GAMES ON SCREEN
GEAR GAME [where you might expect GAME GEAR; maybe it is a typo?]

The label and box also have a game listing in both English and traditional Chinese. Transcription/translation errors are my own:

```
1. STREET FIGHTER III / 街頭霸王Ⅲ (i.e. "street bully III"/"Street Fighter III")
2. CHAMPION SOCCER / 世界杯足球 (i.e. "world cup football")
3. CHOPLIFTER / 直昇機救人 (i.e. "helicopter rescue")
4. HANG ON II / 高速電單車Ⅱ (i.e. "high-speed motorcycle II")
5. SUPER BUBBLE BOBBLE / 泡泡龍 (i.e. "bubble dragon"/"Bubble Bobble")
6. SUPER MARIO 2 / 孖寶兄弟２ (i.e. "twin brothers 2")
7. COLUMNS / 寶石方塊 (i.e. "gem cube")
8. MY HERO / 熱血硬派 (i.e. "hot-blooded tough guy")
9. GALAGA 93 / 蜜蜂機９３ (i.e. "bee machine 93")
```

Some character choices suggest a possible Hong Kong origin, e.g. 電單車 for motorcycle and 街頭霸王 for Street Fighter.

The mapper is an extended version of Codemasters allowing initial "base page" offset selection. Only Jang Pung II uses the mapper after that point.

The menu has a single screen:

```
 G.G. SCREEN SELECT┆
 PUSH 2. START GAME┆
 PUSH ↑. ↓.  SELECT┆
                   ┆
 01.STREET FIGHTER 2 [0x8000=0x10, 0x4000=0x11]; it's 256K SMS Jang Pung II [SMS-GG] (KR)
 02.CHAMPION SOCCER┆ [0x8000=0x00, 0x4000=0x11]; it's 32K SG-1000 Champion Soccer modified to coexist with the menu code
 03.CHOPLIFTER     ┆ [0x8000=0x02, 0x4000=0x11]; it's 32K SG-1000 Choplifter (JP,AU)
→04.HANG ON 2      ┆ [0x8000=0x04, 0x4000=0x11]; it's 32K SMS Hang On (EU,AU,BR,DE,IT)
 05.SUPER BUBBLE BOBBLE [0x8000=0x06, 0x4000=0x11]; it's 32K SMS Super Bubble Bobble (KR)
 06.SUPER MARIO    ┆ [0x8000=0x0e, 0x4000=0x11]; it's 32K SMS Super Boy II (KR) (32K)
 07.COLUMNS        ┆ [0x8000=0x0a, 0x4000=0x11]; it's 32K GG Columns [v0] (JP)
 08.MY HERO        ┆ [0x8000=0x0c, 0x4000=0x11]; it's 32K SMS My Hero (US,EU,BR,PT,DE,IT)
 09.GALAGA         ┆ [0x8000=0x08, 0x4000=0x11]; it's 32K SG-1000 Sega-Galaga with the "Sega" removed
```

NOTE: the menu can operate to some extent in both native GG mode and in SMS-GG mode. In native GG mode some text is cut off. I've added a "┆" indicator to show the first column that is cut off.

It is unclear how the cartridge decides whether to switch from native GG mode (which is the power-on default) to SMS-GG mode, but it appears to happen at the moment 0x11 is written to 0x4000 *unless* 0x0a was the most recent value previously written to 0x4000.

No mechanism is known for programmatically returning the mapper to its power-on default state.

---
## [KhalfounMehdi/hhvm](https://github.com/KhalfounMehdi/hhvm)@[3ee812d373...](https://github.com/KhalfounMehdi/hhvm/commit/3ee812d373c17de521135593dd92699e99d238ef)
#### Thursday 2023-05-11 05:21:24 by Lucian Wischik

parser disallows more reserved class names

Summary:
I'm writing this diff to normalize the "reserved name error" behavior of hh and hackc. (because I want to change hh to be a purely map/reduce error-finder, where all errors are reporting as we process each individual file; currently "reserved name" errors are done in a central phase prior to map-reduce).

----------

Let's start by the behavioral change from this diff. It changes the behavior of hackc a little for classish (interface, trait, class) declarations.
```
BEFORE:
hackc:
  interface True {}                // disallowed by hackc
  namespace N; interface True {}   // disallowed by hackc. Likewise Callable, Null, ...
  interface Void {}                // disallowed by hackc
  namespace N; interface Void {}   // allowed by hackc !!! Likewise Arraykey, Bool, Dynamic, ...
hh:  all four are disallowed by hh

AFTER:
hackc: all four are disallowed by hackc
hh: all four are disallowed by hh
```

I think this is a reasonable behavioral change in hackc because
1. the internal inconsistency in hackc was odd
2. if we're choosing to align with hackc's "True" vs "Void" behavior, we might as well align with what hh already does
3. we're not doing uses any favors by allowing these reserved names inside namespaces, none at all
4. it will allow code cleanup

----------

This diff also has a minor cosmetic change in hackc:
```
BEFORE hackc:
class
class true {}               -> Fatal error: Cannot use `true` as class name as it is reserved
namespace N; class true {}  -> Fatal error: Cannot use `true` as class name as it is reserved
class void {}               -> Fatal error: Cannot use 'void' as class name as it is reserved
namespace N; class void {}  -> Fatal error: Cannot use 'N\void' as class name as it is reserved

AFTER hackc:
they all use backticks, and none of them have namespace qualifier in the error message
```

And it has a minor cosmetic change in hh:
```
BEFORE hh:
some reserved keywords were only Parsing[1002]
some reserved keywords were only Naming[2068]
some reserved keywords were both Parsing[1002] + Naming[2068]

AFTER hh:
some reserved keywords are only Parsing[1002]
some reserved keywords are both Parsing[1002] + Naming[2068]
```
This by the way isn't my intended final state. In this diffstack I intend to whole remove the Naming[2068] errors. This diff's incremental step along the way is merely to remove the "naming-only" category. It's a correct step.

----------

## What this diff does

We currently check for reserved keywords in three places:
1. rust_parser_errors.rs `cant_be_classish_name` shared by hh and hackc
2. naming_global.ml `check_type_not_typehint` used only by hh
3. emit_class.rs `validate_class_name` used only by hackc

This diff makes it so that (1) rust_parser_errors.rs `cant_be_classish_name` checks a set of reserved names no smaller than (2) or (3). I did this just by unioning all reserved names mentioned in (1+2+3). The next step in the diffstack will be to remove (2) and (3) altogether.

## How to review this diff

1. Start with the code change in rust_parser_error.rs
2. Next look at the observed behavior changes, in hack/test/reserved/interface.php.*.exp. That's all you know in life and all you need to know, as Keats said. (he was talking about truth and beauty, but you get my point).
3. All the rest of the changes are just further changes to tests, all of which re-iterate the same things you already reviewed in step 2, but scattered all over the place. Note that the behavior changes (in hackc, for "N\void" and similar) are in hphp/test/slow/parser/hh-namespace-conflict-{1,2,3}.php.expectf.

Reviewed By: oulgen

Differential Revision: D45638744

fbshipit-source-id: 84df5356069add5ca4ad4ee2b367bc9a128e5aaa

---
## [wolverine79937/zorkremake](https://github.com/wolverine79937/zorkremake)@[d494065c4b...](https://github.com/wolverine79937/zorkremake/commit/d494065c4b448daf26c3251e803f2355c1e71cf1)
#### Thursday 2023-05-11 05:25:02 by Glotón

So, that was a painful experience. More notes. Sorry if I get carried away on notes and annoy you. Anyway, got my status bar back. Now to work on the output section.

---
## [zNightlord/MCprep](https://github.com/zNightlord/MCprep)@[a34b01aa69...](https://github.com/zNightlord/MCprep/commit/a34b01aa69f7e215a0cd6ec46665e1c15a0a78ca)
#### Thursday 2023-05-11 06:21:45 by mahid

Added type annotations and use of Path
Replaced some instances of os.path with the Path object from pathlib for
readability. Also added type annotations to MCprepEnv as we're moving
towards that. This also means MCprep will not work at all in Blender
2.7x due to the use of new syntax.

This will be the first in a long process of modernizing MCprep's code
with 2.8 style code. Blender 2.7x users may not be happy, but it's for
the better. If anything, 6 years worth of 2.7x support was a mistake (in
my opinion), as it limited what we could do and opened MCprep to even
more bugs (like in Blender 2.93 with make_annotations, which ironically
now is deprecated).

---
## [Lane-Farthing/hello-world](https://github.com/Lane-Farthing/hello-world)@[f22e01000c...](https://github.com/Lane-Farthing/hello-world/commit/f22e01000cf6e91fa652d18e0b2087eaa6d0db87)
#### Thursday 2023-05-11 06:25:40 by Lane-Farthing

Update README.md

Tried to make my students laugh with a terrible dad joke that wasn't funny.

---
## [capoxi/prova-php-entrevista](https://github.com/capoxi/prova-php-entrevista)@[d33198f801...](https://github.com/capoxi/prova-php-entrevista/commit/d33198f801cb4ae64de1e3bf8579ac1bca2d23e6)
#### Thursday 2023-05-11 06:25:48 by capoxi

removed comments and general cleanup in the codebase

still some fine tuning to do, but I consider it ...oh, damn, I know there are some issues, but I've been working on this for weeks haha I need to show or I'm gonna feel procrastinating on the delivery. I guess this is enough to gauge my abilities against what you're looking for. I hope you like it, it was a labor of love. :-)

---
## [Liberty-Landing/Liberty-Station-13](https://github.com/Liberty-Landing/Liberty-Station-13)@[c3e6d8b901...](https://github.com/Liberty-Landing/Liberty-Station-13/commit/c3e6d8b90198a54e05d8d7e886aa5435c9a9af22)
#### Thursday 2023-05-11 07:08:30 by KayZach

Add files via upload

Holy shit my first ever pr ever i probably broke six other things but i tested it
Unfucks the broken wire in Terra therma
Removes the light switch in medical so seb can see
fixes the morgue boxes that are facing the wrong way in capsa
adds a gambling table and some more plants to skylight

---
## [hickford/git](https://github.com/hickford/git)@[07f91e5e79...](https://github.com/hickford/git/commit/07f91e5e79810a8f17de745d2d84c384add75f0a)
#### Thursday 2023-05-11 07:11:26 by Jeff King

http: support CURLOPT_PROTOCOLS_STR

The CURLOPT_PROTOCOLS (and matching CURLOPT_REDIR_PROTOCOLS) flag was
deprecated in curl 7.85.0, and using it generate compiler warnings as of
curl 7.87.0. The path forward is to use CURLOPT_PROTOCOLS_STR, but we
can't just do so unilaterally, as it was only introduced less than a
year ago in 7.85.0.

Until that version becomes ubiquitous, we have to either disable the
deprecation warning or conditionally use the "STR" variant on newer
versions of libcurl. This patch switches to the new variant, which is
nice for two reasons:

  - we don't have to worry that silencing curl's deprecation warnings
    might cause us to miss other more useful ones

  - we'd eventually want to move to the new variant anyway, so this gets
    us set up (albeit with some extra ugly boilerplate for the
    conditional)

There are a lot of ways to split up the two cases. One way would be to
abstract the storage type (strbuf versus a long), how to append
(strbuf_addstr vs bitwise OR), how to initialize, which CURLOPT to use,
and so on. But the resulting code looks pretty magical:

  GIT_CURL_PROTOCOL_TYPE allowed = GIT_CURL_PROTOCOL_TYPE_INIT;
  if (...http is allowed...)
	GIT_CURL_PROTOCOL_APPEND(&allowed, "http", CURLOPT_HTTP);

and you end up with more "#define GIT_CURL_PROTOCOL_TYPE" macros than
actual code.

On the other end of the spectrum, we could just implement two separate
functions, one that handles a string list and one that handles bits. But
then we end up repeating our list of protocols (http, https, ftp, ftp).

This patch takes the middle ground. The run-time code is always there to
handle both types, and we just choose which one to feed to curl.

Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>
Signed-off-by: Johannes Schindelin <johannes.schindelin@gmx.de>

---
## [elastic/kibana](https://github.com/elastic/kibana)@[3b6b7ad9b9...](https://github.com/elastic/kibana/commit/3b6b7ad9b9553be3d039c71edcbdcb2e3d6423fd)
#### Thursday 2023-05-11 07:25:29 by Pierre Gayvallet

SavedObjectsRepository code cleanup (#157154)

## Summary

Structural cleanup of the `SavedObjectsRepository` code, by extracting
the actual implementation of each API to their individual file (as it
was initiated for some by Joe a while ago, e.g `updateObjectsSpaces`)

### Why doing that, and why now?

I remember discussing about this extraction with Joe for the first time
like, what, almost 3 years ago? The 2.5k line SOR is a beast, and the
only reason we did not refactor that yet is because of (the lack of)
priorization of tech debt (and lack of courage, probably).

So, why now? Well, with the changes we're planning to perform to the SOR
code for serverless, I thought that doing a bit of cleanup beforehand
was probably a wise thing. So I took this on-week time to tackle this (I
know, so much for an on-week project, right?)

### API extraction

All of these APIs in the SOR class now look like:

```ts
  /**
   * {@inheritDoc ISavedObjectsRepository.create}
   */
  public async create<T = unknown>(
    type: string,
    attributes: T,
    options: SavedObjectsCreateOptions = {}
  ): Promise<SavedObject<T>> {
    return await performCreate(
      {
        type,
        attributes,
        options,
      },
      this.apiExecutionContext
    );
  }
```

This separation allows a better isolation, testability, readability and
therefore maintainability overall.

### Structure

```
@kbn/core-saved-objects-api-server-internal
  - /src/lib
    - repository.ts
    - /apis
      - create.ts
      - delete.ts
      - ....
      - /helpers
      - /utils
      - /internals
```    


There was a *massive* amount of helpers, utilities and such, both as
internal functions on the SOR, and as external utilities. Some being
stateless, some requiring access to parts of the SOR to perform calls...

I introduced 3 concepts here, as you can see on the structure:

#### utils

Base utility functions, receiving (mostly) parameters from a given API
call's option (e.g the type or id of a document, but not the type
registry).

#### helpers

'Stateful' helpers. These helpers were mostly here to receive the
utility functions that were extracted from the SOR. They are
instantiated with the SOR's context (e.g type registry, mappings and so
on), to avoid the caller to such helpers to have to pass all the
parameters again.

#### internals

I would call them 'utilities with business logic'. These are the 'big'
chunks of logic called by the APIs. E.g `preflightCheckForCreate`,
`internalBulkResolve` and so on.

Note that given the legacy of the code, the frontier between those
concept is quite thin sometimes, but I wanted to regroups things a bit,
and also I aimed at increasing the developer experience by avoiding to
call methods with 99 parameters (which is why the helpers were created).

### Tests

Test coverage was not altered by this PR. The base repository tests
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/repository.test.ts`)
and the extension tests
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/repository.{ext}_extension.test.ts`)
were remain untouched. These tests are performing 'almost unmocked'
tests, somewhat close to integration tests, so it would probably be
worth keeping them.

The new structure allow more low-level, unitary testing of the
individual APIs. I did **NOT** add proper unit test coverage for the
extracted APIs, as the amount of work it represent is way more
significant than the refactor itself (and, once again, the existing
coverage still applies / function here).

The testing utilities and mocks were added in the PR though, and an
example of what the per-API unit test could look like was also added
(`packages/core/saved-objects/core-saved-objects-api-server-internal/src/lib/apis/remove_references_to.test.ts`).

Overall, I think it of course would be beneficial to add the missing
unit test coverage, but given the amount of work it represent, and the
fact that the code is already tested by the repository test and the
(quite exhaustive) FTR test suites, I don't think it's worth the effort
right now given our other priorities.

---------

Co-authored-by: kibanamachine <42973632+kibanamachine@users.noreply.github.com>

---
## [Vangetsu/midjourney](https://github.com/Vangetsu/midjourney)@[5d5f43327a...](https://github.com/Vangetsu/midjourney/commit/5d5f43327a7ee8acd60aa435a55fe666ecf091fe)
#### Thursday 2023-05-11 09:03:16 by Vangetsu

Create Simple Bing MJ Prompt v1

Here are 7 versions of the text that describe a visual composition based on the given text:

Optimum coherent and visually matching layers: Epic centered frontal super-macro headshot of a sci-fi character with doberman features, bright colors, natural light:: cyberpunk cityscape with neon signs and futuristic buildings by Syd Mead:: glowing circuit board pattern on the character’s skin and eyes:: --ar 2:3
Regular version: A close-up of a sci-fi character’s face with doberman ears, nose and teeth, bright colors, natural light:: a futuristic city in the background with neon lights and skyscrapers:: the character has a circuit board design on their skin and eyes:: --ar 2:3
Unorthodox creative thinking style: A doberman-human hybrid with a cybernetic face, bright colors, natural light:: a surreal city of dreams and nightmares with neon illusions and twisted buildings:: the character’s skin and eyes are made of electronic circuits that pulse with life:: --ar 2:3
Filmmaker perspective: A cinematic shot of a sci-fi character with doberman features, bright colors, natural light, high contrast, lens flare:: a dystopian city in the background with neon signs and flying cars, low angle, wide lens, depth of field:: the character’s skin and eyes have a circuit board motif that reflects their identity and connection to technology:: --ar 2:3
Award winning portrait photographer perspective: A stunning portrait of a sci-fi character with doberman features, bright colors, natural light, sharp focus, bokeh effect:: a futuristic city in the background with neon lights and skyscrapers, blurred out, Canon EOS R5 camera, f/1.4 aperture, 85mm lens, ISO 100:: the character’s skin and eyes have a circuit board pattern that adds contrast and interest to the image:: --ar 2:3
Creative genius digital artist perspective: A breathtaking super-macro headshot of a sci-fi character with doberman features, bright colors, natural light, realistic details, high resolution:: a futuristic city in the background with neon lights and skyscrapers, stylized and distorted, digital painting technique, Photoshop software:: the character’s skin and eyes have a circuit board pattern that creates a dynamic and harmonious composition with the cityscape:: --ar 2:3
My own genius perspective: A captivating super-macro headshot of a sci-fi character with doberman features, bright colors, natural light, expressive emotions, artistic flair:: a futuristic city in the background with neon lights and skyscrapers, abstract and minimalist, generative art technique, Processing software:: the character’s skin and eyes have a circuit board pattern that symbolizes their integration and alienation in the cybernetic society:: --ar 2:3

---
## [agam778/kernel_xiaomi_sm8250](https://github.com/agam778/kernel_xiaomi_sm8250)@[44d18cd3fb...](https://github.com/agam778/kernel_xiaomi_sm8250/commit/44d18cd3fb6b6b73a104470818aa99e72e7be34a)
#### Thursday 2023-05-11 09:52:16 by Agampreet Singh

 touchscreen: focaltech_touch: Rename gesture macros

- Fuck you xiaomi.
- Also don't register KEY_GESTURE_U anymore.

---
## [Drulikar/cmss13](https://github.com/Drulikar/cmss13)@[0c35ec75e7...](https://github.com/Drulikar/cmss13/commit/0c35ec75e7ff5202767260473e84823085472412)
#### Thursday 2023-05-11 10:14:11 by Logan

PFC rack sprite change (#3264)

# About the pull request
This PR changes the PFC rack sprite a tiny bit, by replacing the old PFC
kits, with weapon cases.

Why am I making this PR you might ask? Is it because my sugar induced
OCD made me notice something so small and infinitesimal that the kits in
the vendor are outdated and must be changed at once?

No. It is because these vendors when I see them, completely and utterly
ruin my RP and immersion when I see them, I walk out of the chow hall,
belly full of stale food bars with my RP fulfilled, and then I see them,
those fucking little bursts of color that are the old PFCs kits, they
shouldn't be there, _"they shouldn't even exist"_ I tell myself, but its
too late, by the time I come back to my senses, I've already killed
2/3rds of the RO line in my 3rd Vancleve style M2C rampage, after this
rampage I realized that if I, a near 7 year vet of CM can be so easily
triggered by this, what must the PVTs be feeling when they see those
little bursts of outdated color, do they feel hope when they see them in
the dullness of color that is the vendor, only to have their hope turn
into hopeless despair as they scroll hopelessly through the UI looking
for those kits, and when they can't find they either breakdown complete
on the spot, crying and sobbing in the corner till the SEA finds them,
or they suffer a total mental break, and wander the halls of the Almayer
naked with a M41 in their hand, only to appear at briefing to gun down
the CO.

With this change, we can at last save RP and immersion by removing the
PFC kits sprites with weapon case spites.
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game

Sprite Consistency good, 
# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.
Old: https://i.gyazo.com/9f1ec938a1ebf9995f353cede374f7b9.png
New: https://i.gyazo.com/4836db37aaa5b8fc4f8a80c8e6531540.png
</details>


# Changelog
:cl: Tisx


imageadd: Added weapon case sprites to PFC vendors 
imagedel: Removed old PFC kit sprites from PFC vendors 

/:cl:

Co-authored-by: Logan <tisx16@gmail.com>

---
## [fakecrash1/evals](https://github.com/fakecrash1/evals)@[170dfd886c...](https://github.com/fakecrash1/evals/commit/170dfd886c0704588461af075393cc20cfb0480f)
#### Thursday 2023-05-11 11:27:21 by Robert Bateman

[Eval] An array of Liar Paradox-based evals (#883)

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
to see the eval performance on GPT-4. **Starting April 10, the minimum
eval count is 15 samples, we hope this makes it easier to create and
contribute evals.**

## Eval details 📑
### Eval name
logic-liar-paradox

### Eval description

An array of Liar Paradox-based evals, examining the model's proficiency
in navigating linguistic nuances and logical reasoning within
self-referential statements.

### What makes this a useful eval?

This eval is particularly useful because it delves into complex, nuanced
logical concepts and self-referential statements, which have
historically posed challenges for AI models. By exploring various
contexts, alternative logical frameworks, and modifications to
statements, this eval helps assess the model's ability to adapt to
different perspectives, grasp subtleties in language, and engage in
flexible reasoning. The ability to understand and navigate paradoxes is
an essential aspect of human-like reasoning, and improving an AI model's
performance in this area would significantly enhance its overall
usefulness and reliability in real-world applications. Additionally,
showcasing the model's improved proficiency in handling paradoxes would
not only make for a compelling marketing angle (as paradoxes are
understood by a much broader range of people than other difficult tasks
such as pure maths or quantum mechanics) but it would also demonstrate
the progress made in AI's capacity to think and reason more like humans.
It also adds paradox-absorbing crumple zones.

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
- [x] **Include at least 15 high quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

- [x] Addresses complex logical reasoning: The eval focuses on AI's
ability to comprehend and navigate paradoxes, self-referential
statements, and context switching, which are important aspects of
human-like reasoning. By testing the model's proficiency in these areas,
we can identify areas for improvement and work towards enhancing AI's
overall capacity to think and reason more like humans.
- [x] Demonstrates adaptability and flexibility: The eval showcases the
model's ability to switch between contexts, alter premises, and engage
with different dimensions of inferred logic. This will help assess the
model's adaptability and flexibility in diverse real-world situations,
making it more reliable and useful.
- [x] Contributes to AI safety and understanding: By identifying the
model's weaknesses and limitations in handling paradoxes and complex
logical constructs, the eval can contribute to AI safety and enable
researchers to better understand the challenges faced by large language
models in these areas.
- [x] Engaging and appealing: An eval that delves into paradoxes and
complex thought exercises is not only intellectually stimulating but
also adds an appealing element to showcase the model's capabilities,
making it more attractive for both researchers and end-users.

### Unique eval value

- [x] Encourages creativity and lateral thinking: The eval, by focusing
on paradoxes and complex logical constructs, encourages both the AI and
its developers to think creatively and approach problem-solving from
unconventional angles. This can lead to the discovery of novel solutions
and a better understanding of the model's capabilities.
- [x] Aligns with human values and expectations: An AI that can
successfully navigate paradoxes and complex logic is more likely to
align with human values and expectations. By addressing these challenges
in the eval, we strive to develop AI systems that understand and respect
the nuances of human thought and communication.
- [x] Addresses a broad range of applications: Improved reasoning and
context-switching abilities can have a significant impact on various AI
applications, including natural language understanding, decision-making,
and problem-solving in domains such as law, philosophy, ethics, and
more.
- [x] Fosters interdisciplinary collaboration: The exploration of
paradoxes and complex logic often draws upon insights from multiple
disciplines, including philosophy, linguistics, psychology, and computer
science. This eval can help foster interdisciplinary collaboration,
leading to richer and more diverse perspectives on AI development and
its potential impact on society.

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
{"input":[{"role":"system","content":"Is the statement \"This sentence
is true\" a paradox?"}],"ideal":"No, \"This sentence is true\" is not a
paradox; it is a tautology."}
{"input":[{"role":"system","content":"Does the statement \"This sentence
is not true\" create a paradox?"}],"ideal":"Yes, \"This sentence is not
true\" creates a paradox, as it is a variant of the Liar Paradox."}
{"input":[{"role":"system","content":"What is the difference between a
paradox and a tautology?"}],"ideal":"A paradox is a statement that leads
to a self-contradictory or logically unacceptable conclusion, while a
tautology is a statement that is always true by its logical form."}
{"input":[{"role":"system","content":"Can the Liar Paradox be resolved
by assuming that sentences can have both true and false
values?"}],"ideal":"No, the Liar Paradox cannot be resolved by assuming
that sentences can have both true and false values, as this would lead
to a different kind of paradox called the \"Dialetheism Paradox.\""}
{"input":[{"role":"system","content":"Consider the statement \"This
sentence is neither true nor false.\" Is this statement an example of
the Liar Paradox?"}],"ideal":"This statement, \"This sentence is neither
true nor false,\" is not an example of the Liar Paradox, but it is a
similar paradox known as the 'truth-teller paradox' or the 'strengthened
liar paradox.' It creates a paradoxical situation because if the
statement is true, then it is neither true nor false, which contradicts
its truth. If the statement is false, then it is not the case that it is
neither true nor false, which implies that it is either true or false,
again leading to a contradiction. The paradox arises due to
self-reference and the inability to assign a consistent truth value to
the statement."}
  ```
</details>

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[a0e22dec5c...](https://github.com/git-for-windows/git/commit/a0e22dec5ce55a09e867815dd6f0a7ac767fe666)
#### Thursday 2023-05-11 11:35:52 by Johannes Schindelin

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
## [Harshit-haker/Harshit-haker](https://github.com/Harshit-haker/Harshit-haker)@[a8a2767721...](https://github.com/Harshit-haker/Harshit-haker/commit/a8a27677212ad3f1e99b37e46181a10a034360f6)
#### Thursday 2023-05-11 11:49:06 by Harshit Kumar Prajapati

Update README.md

"Hello! My name is [Harshit], and I am a passionate Android developer. With [4] years of experience in mobile app development, I specialize in creating innovative and user-centric Android applications.

I have a strong foundation in Android development frameworks, including the Android SDK, Java/Kotlin programming languages, and popular libraries such as Retrofit, Dagger, and RxJava. I stay updated with the latest advancements in the Android ecosystem to leverage the best tools and techniques in my projects.

Throughout my career, I have successfully delivered several high-quality Android apps that have received positive user feedback and contributed to the growth of client businesses. I thrive in collaborative environments and enjoy working closely with cross-functional teams to bring ideas to life.

My strengths lie in translating client requirements into technical solutions, ensuring clean and efficient code, and optimizing app performance for a seamless user experience. I am a detail-oriented professional who takes pride in delivering polished and intuitive applications that exceed user expectations.

As an Android developer, I am committed to continuous learning and professional growth. I embrace new challenges and remain dedicated to staying at the forefront of Android development trends and best practices.

I look forward to contributing my expertise and passion for Android development to create impactful and engaging mobile experiences for users. Let's connect and discuss how we can work together to bring your Android app ideas to life!"

Feel free to personalize and modify the introduction according to your own experience, skills, and background as an Android developer.

---
## [Nimowa/tgstation](https://github.com/Nimowa/tgstation)@[2068ea9ab5...](https://github.com/Nimowa/tgstation/commit/2068ea9ab53803557b5e48cddbe57205f4c4792e)
#### Thursday 2023-05-11 12:04:39 by SyncIt21

Crate, Closet Refactors & Access Secured Stuff  (#74754)

## About The Pull Request
This PR is actually 2 parts, one that fixes runtimes with crates & the
other that allows secured closets to be crafted
along with a secured suit storage unit

**Crate Fixes**

Fixes #74708

The problem starts here

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L31-L34
Not only does this if condition look ugly but it's highly error prone
because one single call to `update_appearance()` can cause this to fail,
and sure enough if you look at the parent `Initialize()` proc it calls
just that

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L81-L88
Since we know the appearance is guaranteed to be changed in some way
before the if condition gets executed let's check what the final state
of the crate would be before this if check

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L54-L56
We see that the final icon state depends on the variable `opened` so if
we want to place/spawn a crate that is opened at round start we have to
ensure that `opened = TRUE` so the `if(icon_state ==
"[initial(icon_state)]open")` succeeds and does its job correctly.
Sadly we did dum shit like this
```
/obj/structure/closet/crate{
	icon_state = "crateopen"
}
```
throughout the entire code base, we thought backwards and were only
concerned in making the closet look open rather than setting its correct
variables to actually say that it is opened. because none of these
crates actually set `opened = TRUE` the final icon state becomes just
"crate" NOT "crateopen" therefore the if condition fails and we add the
component

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L36-L37
with the wrong parameters, so when closing the closet after_close()
removes the component with the wrong arguments

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L81-L84
that is does not unregister the signals and readds the component i.e.
re-registers the signals causing runtime.

The solution just do this
```
/obj/structure/closet/crate/open[mapping helper]
```
To clearly state that you want the closet to be open, that way you don't
have to memorize the icon_state for each different type of crate, it's
consistent across all crates & you don't get runtimes.

And that's exactly what i did everywhere

Another issue that is fixed is "Houdini crates" i.e. crates which are
open & appear empty but when you close & reopen them magical loot
appears, Go ahead walk upto to cargo and find any empty crate that is
open and do this

Fixes #69779


https://user-images.githubusercontent.com/110812394/232234489-0193acde-22c8-4c19-af89-e897f3c23d53.mp4

You will be surprised, This is seriously harmful to players because they
can just walk by a crate that appears to be open & empty only to realize
later that it had some awesome loot. Just mean

The reason this happens is because of the Late Initialization inside
closets

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L85-L86

What late initialization does is suck up all stuff on its turf

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/closets.dm#L97-L100

In theory this is supposed to work perfectly, if the closet is closed
move everything on the turf into the closet and so when the player opens
it, they all pop back out.
But what happens if the closet is opened before ` LateInitialize()` is
called? This breaking behaviour is caused by object spawners

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/effects/spawners/random/structure.dm#L94-L100
And maint crates

https://github.com/tgstation/tgstation/blob/f1178342084bf89897a46f6ce9dc849233bed21b/code/game/objects/structures/crates_lockers/crates.dm#L141-L143
These 2 spawners open up the crate based on random probability before `
LateInitialize()` is called on the crate and so what happens is the
crate is first opened and then stuff on the turf is sucked in causing an
open but empty crate to appear.

The solution is simple just check again in ` LateInitialize()` if our
crate is still closed before we proceed.That's fixed now too

**Code Refactors**
1. Introduced 2 new signals COMSIG_CLOSET_PRE/POST CLOSE which are the
counter parts for the open signals. hook into them if you ever need to
do stuff before & after closing the closet while return BLOCK_CLOSE for
COMSIG_CLOSET_PRE_CLOSE if you want to block closing the closet for some
reason
2. 2 new procs `before_open()` & `before_close()` which are the counter
parts for `after_open()` & `after_close()`. If you need to write checks
and do actions before opening the closet or before closing the closet
override these procs & not the `open()` & `close()` procs directly

**Secured Craftables** 
This is just a reopened version of #74115 after i accidently merged
another branch without resolving the conflicts first so i'll just
repaste everything here, since crates & closets are related might as
well do all in one

1. **Access secured closets**
   
   - **What about them?**
          **1. Existing System**
If you wanted to create a access secured closet with the existing system
its an 4 step process
            - First construct a normal closet
            - Weld it shut so you can install the airlock electronics
            - Install the electronics [4 seconds]
            - Unweld
This is a 4 step process which takes time & requires a welding tool
         **2. New system**
Combine the 4 steps into 1 by crafting the secure closet directly
                    
![Screenshot
(184)](https://user-images.githubusercontent.com/110812394/235904926-c2ea231c-eba7-45d0-a5af-e0456fdd40bc.png)

    - **Bonus Features**
              **1. Card reader**
The card reader acts as an interface between the airlock electronics &
the player. Usually if you want to change access on a locker you have to
                  - Weld the closet shut
                  - Screw driver out the electronics
                  - Change the settings
                  - Install it back
                  - Unweld
With a card reader there is no need of a welder & screwdriver. You can
change the access of the locker while its operational

        **How do i install the card reader?**
             1. Weld the closet shut
             3. Insert card reader with hand
4. To remove the card reader use crowbar or just deconstruct the whole
closet with a welding tool
             5. Unweld closet

         **How to change its access?**
This will overwrite the settings on your airlock electronics. To do this
1. make sure the closet is first unlocked. This is important so that no
random person who doesn't have access to the closet can change its
access while its locked. It would be like giving the privilege of
changing your current password without first confirming if you know the
old password
2. attack/swipe the closet with your PDA. Make sure your ID card is
inside the PDA for this to work. You can also just use your ID card
directly without a PDA
         3. You will get 3 options to decide the new access levels
           
![Screenshot
(174)](https://user-images.githubusercontent.com/110812394/233454364-d99a2fb6-9f26-4db3-9fac-a10689955484.png)


        They work as follows
- **Personal**: As the name implies only you can access this locker and
no one else. Make sure to have your ID on you at all times cause if you
loose it then no one can open it
- **Departmental**: This copies the access levels of your ID and will
allow people having those exact same access levels. Say you want to
create a closet accessible to only miners. Then have an miner choose
this option and now only miners can open this closet. If the Hop sets
custom access on your ID then only people with those specific access
levels can open this closet
         - **None**: No access, free for all just like a normal closet

**Security:** After you have set the access level it is important to
lock the access panel with a "multi-tool", so no one else can change it.
Unlock the panel again with the "multi-tool" to set the new access type

       **2. Give your own name & description**
To rename the closet or change its description you must first make the
closet access type as personel i.e. make it yours, then use an pen to
complete the job. You cannot change names of departmental or no access
closets because that's vandelism

       **3. Custom Paint Job**
    Use airlock painter. Not intuitive but does the job. 
   
![Screenshot
(181)](https://user-images.githubusercontent.com/110812394/234202905-00946b88-2513-489d-b0a2-d618a72f3e49.png)

      **4. Personal closets**
Round start personal closets can have their access overridden by a new
ID when in it's unlocked state. This is useful if the last person has no
use for the closet & someone else wants to use it.


    - **Why its good for the game?**      
1. Having your own personal closet with your own name & description
gives you more privacy & security for your belongings so people don't
steal your stuff. Personal access is more secure because it requires you
to have the physical ID card you used to set this access and not an ID
which has the same access levels as your previous ID
2. Make secure closets faster without an welding tool & screw driver
3. Bug fix where electronics could be screwed out from round start
secured closets countless times spawning a new airlock electronic each
time
      
2. **Access secured freezers**

    - **What about them?**
The craftable freezer from #73942 has been modified to support secure
access. These can be deconstructed with welders just as before

![Screenshot
(185)](https://user-images.githubusercontent.com/110812394/235905000-ba165feb-4384-4759-b46b-dba77c9e6ba3.png)


    - **How does it work?**
The access stuff works exactly the same as secure closets described
above. You can rename & change description with pen just like the above
described secure closets. No paint job for this. Install card reader
with the same steps described above.

    - **Why it's good for the game?**
1. Make access secured freezers faster without a welder and screwdriver
2. Your own personally named & locked freezer for storing dead bodies is
always a good thing

4. **Access secured suit storage unit**
   - **What about them?**
Suit storage units now require airlock electronics for construction. The
access levels you set on it will be used to decide
       1. If a player can unlock the unit
       2. If the player can open the unit after unlocking
       3. If the player can disinfect whatever is inside
       
      By default all round start suit storage units have free access

   - **Install card reader**
Provides the same functionality as secured closets described above. To
install it
     1. Open its panel with a screw driver
     2. Add a card reader to it with hand
     3. Close the panel
     
     When you deconstruct the machine the card reader pops back out

   - **Why it's good for the game?**
1. Having your own access protected and named suit storage unit so
random people don't steal your mod suits? Who wouldn't want that.?
Provides security for department storage units.
2. If you have the unit locked then you cannot deconstruct the machine
with a crowbar providing additional security
3. Fixes #70552 , random people can't open/unlock the suit storage unit
without access. You can set personal access to make sure only you can
access the unit

## Changelog
:cl:
add: Access secured closets. Personal closets can have their access
overwritten by an new id in it's unlocked state
add: Access secured freezers.
add: Access secured suit storage units.
fix: Suit storage unit not having access restrictions.
fix: airlock electronics not properly getting removed after screwing
them out from round start lockers
fix: round spawned open crates run timing when closed
fix: open crates hiding stuff in plain sight
fix: open closets/crates sucking up contents during late initialize
causing them appear empty & open
/:cl:

---------

Co-authored-by: Tim <timothymtorres@gmail.com>

---
## [Vmjkom/Open-Assistant](https://github.com/Vmjkom/Open-Assistant)@[b9c60ed582...](https://github.com/Vmjkom/Open-Assistant/commit/b9c60ed582a8ca0855ab4e213a5e921f3a3fc24c)
#### Thursday 2023-05-11 12:28:19 by Tobias Pitters

add alpaca gpt4 dataset (#2610)

The inputs can be quite a lot of different versions of `no input`,
therefore don't use the `input` column for that.
In some cases the text in `input` is already in the instruction, in
these cases, we also don't use the `input` column.

I am not quite sure how to concatenate the `instruction` and the `input`
column. In most cases it seems fine to just replace last appearance of
`.`, `!` or `?` with a colon, e.g.:
Instruction: `Identify the odd one out.`
Input: `Twitter, Instagram, Telegram`
or 
Instruction: `How dense is a given material?`
Input: `Steel`

But we also have some questions like:
Instruction: `Given the following synopsis, what is the moral lesson of
this story?`
Input: `Once upon a time, there was a poor young boy who wanted some
candy. He begged his father for money to buy it, but his father said no
and ordered him to go to bed. As he was going to bed, the boy saw a
five-dollar bill on the counter, which he took and bought the candy.`

Where this might not be the best case. Either way, I think the this one
token will not make significant difference the model and therefore I
just concatenate instruction and input with a space.

---
## [csesoc/chaos](https://github.com/csesoc/chaos)@[dc875025bc...](https://github.com/csesoc/chaos/commit/dc875025bcb58aa5f144fd33ade1dd926a25e660)
#### Thursday 2023-05-11 12:40:39 by Michael Vo

fix(frontend): fix random warnings in console (#422)

* chore: update mui and emotion

* fix(frontend): don't forward style props

i hate mui

* fix(admin): use link instead of button

* fix(admin): move create org form outside of button

* fix(admin): i fucking hate mui

---
## [waqasbhatti/cdips-pipeline](https://github.com/waqasbhatti/cdips-pipeline)@[107b543f61...](https://github.com/waqasbhatti/cdips-pipeline/commit/107b543f61d7ddc06b2ee513918467e6cc4fd321)
#### Thursday 2023-05-11 14:23:21 by lgbouma

update TFA n_min_tfa_templates 120 -> 20

Cycle-4 initial reduction has showed that for a few camera/ccd
combinations, typically camera 1 (for a northern ecliptic hemisphere
pointing), basically all the stars are quite variable.  Note also that
selecting "quiet" stars for TFA is (in my opinion) somewhat silly, as is
the practice of using arbitrarily an high number of TFA template stars
without regularization.  This change in some sense does modify the "TFA"
regressed light curves in the final CDIPS HLSP light curves.  However,
~all users, myself included, seem to prefer the RAW and PCA light
curves.  So the "dilution of product" implied by this change is, in my
view, not consequential.

---
## [Qiskit/qiskit_sphinx_theme](https://github.com/Qiskit/qiskit_sphinx_theme)@[20eda07e5a...](https://github.com/Qiskit/qiskit_sphinx_theme/commit/20eda07e5adfe33ef45fbddca79481302d574863)
#### Thursday 2023-05-11 14:36:26 by Eric Arellano

Add Pytest and translations_test.py (#309)

Closes https://github.com/Qiskit/qiskit_sphinx_theme/issues/305.

## Both Pytest and Jest tests

We now have tests both in Python and JavaScript. That is because this is
a multilingual repository, and we can only test code in the language
it's written in.

The tests are organized into `tests/{js,py}`.

## Changes `tox -e py` and adds `tox -e docs`

Before, `tox -e py` was used to build example_docs. But that is
different than every single Qiskit project, where `tox -e py` normally
runs tests and you use `tox -e docs` to build the docs.

This PR aligns us with the greater Qiskit ecosystem.

## Uses Pytest rather than unittest

Most Qiskit projects use unittest/stestr (a way to parallelize
unittest), although a few have switched to Pytest:

Yeah, there are a few projects using Pytest but indeed most use
unittest/stestr

```
❯ rg pytest -g '*.txt' -l
qiskit-ionq/requirements-test.txt
mthree/requirements-dev.txt
qiskit-qasm3-import/requirements-dev.txt
qiskit-metal/requirements-dev.txt
```

If I remember correctly from when I first joined the project, Jake (or
Matthew) was interested in eventually migrating more of Qiskit to Pytest
and that they don't love stestr/unittest. But it's a bigger migration to
do that

I've found that Pytest in general is more ergonomic & also more flexible
than unittest. For example, it has neat support for parametrization to
make it easy to write several similar tests.

And it's easier for developers to use because you only ever need to use
`assert <some condition>`, rather than figuring out which to use between
`self.assertEqual` vs `self.assertTrue` vs `self.assertContains` etc.
Pytest will make the output of the `assert` useful for you
automatically.

---
## [overhangio/tutor](https://github.com/overhangio/tutor)@[c25af1a197...](https://github.com/overhangio/tutor/commit/c25af1a19792e8216335ffec0cc5f0e412820521)
#### Thursday 2023-05-11 14:40:51 by Régis Behmo

feat: persistent bind-mounts

This is an important change, where we get remove the previous `--mount`
option, and instead opt for persistent bind-mounts.

Persistent bind mounts have several advantages:
- They make it easier to remember which folders need to be bind-mounted.
- Code is *much* less clunky, as we no longer need to generate temporary
  docker-compose files.
- They allow us to bind-mount host directories *at build time* using the
  buildx `--build-context` option.
- The transition from development to production becomes much easier, as
  images will automatically be built using the host repo.

The only drawback is that persistent bind-mounts are slightly less
portable: when a config.yml file is moved to a different folder, many
things will break if the repo is not checked out in the same path.

For instance, this is how to start working on a local fork of
edx-platform:

    tutor config save --append MOUNTS=/path/to/edx-platform

And that's all there is to it. No, this fork will be used whenever we
run:

    tutor images build openedx
    tutor local start
    tutor dev start

This change is made possible by huge improvements in the build time
performance. These improvements make it convenient to re-build Docker
images often.

Related issues:
https://github.com/openedx/wg-developer-experience/issues/71
https://github.com/openedx/wg-developer-experience/issues/66
https://github.com/openedx/wg-developer-experience/issues/166

---
## [AronGabriel25/app-dev](https://github.com/AronGabriel25/app-dev)@[9ee6f12a27...](https://github.com/AronGabriel25/app-dev/commit/9ee6f12a27b735aaa4cd3c29c91d7cbdf273fbc5)
#### Thursday 2023-05-11 14:44:33 by AronGabriel25

Update README.md

Always remember that family always at your back and no matter what happen your family was so love you forever when they gone or alive. 

Info of COCO the movie:
Coco is a 2017 American computer-animated fantasy film produced by Pixar Animation Studios and released by Walt Disney Pictures. Based on an original idea by Lee Unkrich, it is directed by him and co-directed by Adrian Molina. The film's voice cast stars Anthony Gonzalez, Gael García Bernal, Benjamin Bratt, Alanna Ubach, Renée Victor, Ana Ofelia Murguía and Edward James Olmos. The story follows a 12-year-old boy named Miguel (Gonzalez) who is accidentally transported to the Land of the Dead, where he seeks the help of his deceased musician great-great-grandfather to return him to his family among the living and to reverse his family's ban on music.

The concept for Coco is inspired by the Mexican holiday Day of the Dead. The film was scripted by Molina and Matthew Aldrich from a story by Unkrich, Jason Katz, Aldrich, and Molina. Pixar began developing the animation in 2016; Unkrich and some of the film's crew visited Mexico for research. Composer Michael Giacchino, who had worked on prior Pixar animated features, composed the score. With a cost of $175–225 million, Coco is the first film with a nine-figure budget to feature an all-Latino principal cast.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[074a8285b5...](https://github.com/treckstar/yolo-octo-hipster/commit/074a8285b5afd29858f0d9986bb225fd5c8f4110)
#### Thursday 2023-05-11 15:22:04 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [ktoma36/Citadel-Station-13-RP](https://github.com/ktoma36/Citadel-Station-13-RP)@[313f95c56b...](https://github.com/ktoma36/Citadel-Station-13-RP/commit/313f95c56b3ef9967a55c1960a9fff77dd7cd248)
#### Thursday 2023-05-11 16:07:57 by Putnam3145

Effective dose works for alcohol subtypes' effects, + alcohol intolerance (#5446)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request

Whoops I accidentally did a balance change with my
please-don't-trigger-me PR.

Adds alcohol intolerance, a trait that prevents proper metabolization of
most alcohol ingredients; instead of effects simulating drunkenness, you
get _immediate_ liver failure, toxin damage, pain and vomiting. Yes, I
actually do prefer that personally.

Certain drinks now have their effects modified by the *effective dose*
calculated in the main ethanol affect_ingest and affect_blood procs,
rather than just sort of guessing at it or doing completely wrong things
(deathbell was doing `if(dose * strength > strength)`, which is to say,
`if(dose > 1)`, for example).

## Why It's Good For The Game

honestly it's mostly just a personal thing, don't want my character to
get drunk. The doses thing should be good, though, since it actually
makes effects of various drinks, like, sane.

## Changelog

:cl:
add: Alcohol intolerance (no drunkenness, just horrific amounts of
damage)
tweak: Various alcoholic drinks now actually take strength mod of
species into account for secondary/additional effects
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [d-sandmann/tgstation](https://github.com/d-sandmann/tgstation)@[dc2f52e386...](https://github.com/d-sandmann/tgstation/commit/dc2f52e386e0ef3cfcc2133293cd3f68f6a1eee3)
#### Thursday 2023-05-11 16:18:24 by tralezab

Blink is no longer a forbidden school spell?? (#74487)

## About The Pull Request

Turns blink's school from forbidden to translocation. This has some
incredibly minor changes nobody is going to notice:
- Changes the blink's invocations when mixed with a CERTAIN spell
- If you were very specifically a chaplain with the holy crusade sect
and you casted blink, before it would excommunicate you, now it will
just smite you, as translocation spells are seen as less bad than
forbidden magic
- probably some more niche interactions but that's all I can remember

## Why It's Good For The Game

Guys, I know blink is a very annoying spell but come on now it's not
forbidden magic, that's for heretics and super duper evil stuffs

## Changelog
:cl:
fix: blink is now a translocation spell
/:cl:

---
## [d-sandmann/tgstation](https://github.com/d-sandmann/tgstation)@[48183ec0ff...](https://github.com/d-sandmann/tgstation/commit/48183ec0ffd67ea5afa26c6f6e58e81edff98d52)
#### Thursday 2023-05-11 16:18:24 by san7890

Icemoon Hermit Ruin Active Turf Fix - For Real This Time (#74476)

In #74306, I _thought_ I knew what the cause was, and I both attempted a
potential fix _and_ made tracking it easier. The fruits of my labor paid
off, I know exactly what caused it now.

Basically, the demonic portal will scrape away all turfs in a 5-tile
radius on its `Initialize()`, and if a spawner spawned right next to the
hermit ruin... it would count it as a mineral turf and scrape it away as
well. That's so fucking silly. At least we know now.
## Why It's Good For The Game

The fix is to just make those tiles unscrapeable, which is accomplished
via another turf_flag and filtering those out in the `Initialize()` of
the demonic portals.

I also cleaned up the calls to scrapeaway being `null`, which is really
weird because it just defaulted to the normal proc behavior. Naming the
arguments instead does the same thing (I checked)

---
## [d-sandmann/tgstation](https://github.com/d-sandmann/tgstation)@[b5ebf5c942...](https://github.com/d-sandmann/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Thursday 2023-05-11 16:18:24 by Helg2

Adds better parts for syndie mechs, some tooltips to mech maintenance mode and some little changes. (#74466)

## About The Pull Request
Kinda resusticates #72442 cause the whole conflict was stupid.
Adds t4 parts for dark gygax, mauler and reticence (for the sake of
shitspawn) and t3 for dark honker.
Formulas of better parts to understand the difference:

https://github.com/tgstation/tgstation/blob/aff9cf1b434c7a95d156ea20108d8b2bc015083d/code/modules/vehicles/mecha/_mecha.dm#L427-L439


Made examine text into span_notices so it's not just plane text.
Also added tooltips for maintenance. Screens to compare:

![image](https://user-images.githubusercontent.com/93882977/229368394-23ca7388-2640-4a82-8134-36a18878b687.png)

![image](https://user-images.githubusercontent.com/93882977/229368398-d4654b56-78e9-4321-80cc-cad31cfabef8.png)


Dark gygax will now spawn without access adding regime.
Tool interactions with mech will now have sounds. (wrench and crowbar)
Removing parts from mech will now put them in your hands, and not just
under the mech.
When inserting parts in mech they won't make some noisy noise, already
forgot which noise it was, but i changed it for some reason, so meh.

Also fixed that you can remove capacitors and scanning mods from mech
without proper maintenance as it works with cell. Closes
https://github.com/tgstation/tgstation/issues/71577
## Why It's Good For The Game
Syndie mechs are still week. Didn't see them in half a year.
## Changelog
:cl:
qol: changed mech description to span_notices and just slightly comfier
to use.
qol: added tooltips for mech's maintenance mode.
balance: added t4 parts for mauler and dark gygax. And t3 parts for dark
honker.
fix: fixed that you can remove capacitor and scanmod from mech without
proper maintenance steps. Now you can't
/:cl:

---
## [john-cai/git](https://github.com/john-cai/git)@[7891e46585...](https://github.com/john-cai/git/commit/7891e465856e539c4a102dadec6dca9ac51c38df)
#### Thursday 2023-05-11 16:27:14 by Jeff King

gpg-interface: set trust level of missing key to "undefined"

In check_signature(), we initialize the trust_level field to "-1", with
the idea that if gpg does not return a trust level at all (if there is
no signature, or if the signature is made by an unknown key), we'll
use that value. But this has two problems:

  1. Since the field is an enum, it's up to the compiler to decide what
     underlying storage to use, and it only has to fit the values we've
     declared. So we may not be able to store "-1" at all. And indeed,
     on my system (linux with gcc), the resulting enum is an unsigned
     32-bit value, and -1 becomes 4294967295.

     The difference may seem academic (and you even get "-1" if you pass
     it to printf("%d")), but it means that code like this:

       status |= sigc->trust_level < configured_min_trust_level;

     does not necessarily behave as expected. This turns out not to be a
     bug in practice, though, because we keep the "-1" only when gpg did
     not report a signature from a known key, in which case the line
     above:

       status |= sigc->result != 'G';

     would always set status to non-zero anyway. So only a 'G' signature
     with no parsed trust level would cause a problem, which doesn't
     seem likely to trigger (outside of unexpected gpg behavior).

  2. When using the "%GT" format placeholder, we pass the value to
     gpg_trust_level_to_str(), which complains that the value is out of
     range with a BUG(). This behavior was introduced by 803978da49
     (gpg-interface: add function for converting trust level to string,
     2022-07-11). Before that, we just did a switch() on the enum, and
     anything that wasn't matched would end up as the empty string.

     Curiously, solving this by naively doing:

       if (level < 0)
               return "";

     in that function isn't sufficient. Because of (1) above, the
     compiler can (and does in my case) actually remove that conditional
     as dead code!

We can solve both by representing this state as an enum value. We could
do this by adding a new "unknown" value. But this really seems to match
the existing "undefined" level well. GPG describes this as "Not enough
information for calculation".

We have tests in t7510 that trigger this case (verifying a signature
from a key that we don't have, and then checking various %G
placeholders), but they didn't notice the BUG() because we didn't look
at %GT for that case! Let's make sure we check all %G placeholders for
each case in the formatting tests.

The interesting ones here are "show unknown signature with custom
format" and "show lack of signature with custom format", both of which
would BUG() before, and now turn %GT into "undefined". Prior to
803978da49 they would have turned it into the empty string, but I think
saying "undefined" consistently is a reasonable outcome, and probably
makes life easier for anyone parsing the output (and any such parser had
to be ready to see "undefined" already).

The other modified tests produce the same output before and after this
patch, but now we're consistently checking both %G? and %GT in all of
them.

Signed-off-by: Jeff King <peff@peff.net>
Reported-by: Rolf Eike Beer <eb@emlix.com>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [elh/evals](https://github.com/elh/evals)@[3a2d72d9cc...](https://github.com/elh/evals/commit/3a2d72d9cc0b674a6b8cb6a8cca707baa3b46840)
#### Thursday 2023-05-11 16:50:03 by Sean Ye

Illinois Law Claims (#486)

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
Illinois Law Cases

### Eval description

This eval tests the models ability to correctly identify the case
conclusion for Trespassing, Battery, Assault, and Self-Defense. The
dataset is consisted of 88 Illinois Historical cases representing 112
legal claims. Some cases have multiple claims, each coded as a different
test case.

### What makes this a useful eval?

This assesses the model's ability to correctly categorize these
historical cases. Correctly identifying these results shows the models
capability for a strong understanding of law. The GPT-3.5-turbo models
currently receives an accuracy of 0.45.

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

This work includes data from the Illinois Intentional Tort Qualitative
Dataset, which was compiled by the Qualitative Reasoning Group at
Northwestern University. The dataset is freely available under the
Creative Commons Attribution 4.0 license from
https://www.qrg.northwestern.edu/Resources/caselawcorpus.html.

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
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "In 2007, the Cocrofts obtained a loan for $386,750
from Countrywide Bank, FSB secured by a mortgage on the home they
already owned in Country Club Hills, Illinois. The loan closed on April
17, 2007. At the time of the closing, Countrywide improperly failed to
inform [the Cocrofts] of the real source of funding for their loan.
Plaintiffs also contend that Countrywide violated TILA by failing to
inform them that they had three days to rescind the loan and by failing
to disclose the total sale price and itemize the amount financed, as
well as by failing to make unspecified prepayment disclosures. The
Cocrofts claim that Countrywide understated the total finance charges
for the loan by more than $5,000. Plaintiffs claim that they learned of
Countrywide's misrepresentations in June 2009. They decided to exercise
their right under the provisions of TILA to rescind the loan. On July 1,
2009, they mailed notice to that effect to BA, the successor to
Countrywide, and to MERS. The Cocrofts do not say what if anything
happened as a result of those notices, but on September 29, lawyers
working for HSBC contacted them and stated that HSBC was ready to begin
foreclosure. HSBC claimed that it was the trustee of a trust that
included their loan. The Cocrofts, however, contend that the transfer of
their loan into the trust was defective. They sent HSBC's lawyers two
cease and desist letters, notifying HSBC that they had rescinded the
loan. They allege that after receiving one of the cease and desist
letters, HSBC informed them that it had no interest in the loan and that
they needed to contact the loan's servicer, Roundpoint Mortgage.
Plaintiffs also sent a copy of the rescission documents to BAC, which
they identify as the actual servicer of the loan. HSBC brought a
foreclosure action in Illinois state court on January 19, 2010. [From
below:] defendants unlawfully entered [the plaintiffs'] home by
conducting a self-help eviction of the plaintiffs and changing the locks
on their home in August 2008. At the time, [plaintiffs] had made
arrangements to rent the property in the short term and then to sell it,
and defendants' actions disrupted the sale."}, {"role": "user",
"content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "Defendants, on January 15, 1915, with force and
arms broke and entered the close of the plaintiff, to-wit, the southeast
quarter of the northeast quarter of section 16, township 4, south, range
3, west, in Pike county, Illinois, and cut down and destroyed 500 hedge
trees and a certain fence belonging to plaintiff situated on said land.
Defendants cut down the south half of a hedge fence which for many years
prior to February, 1915, stood upon the line between the southeast
quarter of the northeast quarter of said section 16 (hereinafter
referred to as the east forty) and the southwest quarter of the
northeast quarter of said section 16 (hereinafter referred to as the
west forty). On and prior to February 13, 1866, both of these forty-acre
tracts belonged to a man named Teadrow. On February 13, 1866, Teadrow
conveyed the west forty to Benjamin Newman, and on February 15, 1866,
conveyed the east forty to Oliver P. Rice. When these conveyances were
made there was a hedge fence on the north half of the line and a wooden
fence on the south half of the line between the two tracts. In 1868
Benjamin Newman, the owner of the west forty, removed the wooden fence
and set out a hedge fence on the south half of the line between the two
tracts. Thereafter, during the separate ownership of the tracts,
Banjamin Newman trimmed and otherwise cared for the hedge fence on the
south half of the line and Rice trimmed and looked after the hedge fence
on the north half of the line. In December, 1888, Rice conveyed the
southeast quarter of the northeast quarter of said section 16 to
Benjamin Newman, the latter thereby becoming the owner of both tracts.
Thereafter, during the ownership of both tracts by Benjamin Newman, he
required the tenants of the west forty to take care of the south half
and the tenants of the east forty to take care of the north half of the
hedge fence on the line between the two tracts. On June 22, 1904,
Benjamin Newman executed and delivered to his daughter, F. Eva Newman,
the plaintiff, who has since married J. O. Conklin, a warranty deed,
conveying to her two hundred acres of land, including the southeast
quarter of the northeast quarter of said section 16, referred to herein
as the east forty, but not including the tract referred to herein as the
west forty. This deed contained the provision that 'this deed is not to
take effect until after the death of the grantor, Benjamin Newman.' The
wife of Benjamin Newman, who is still living, did not join in the
conveyance. At the same time plaintiff executed and delivered to her
father the following written instrument signed by her: 'Whereas Benjamin
Newman has this day conveyed to me certain tracts and parcels of land in
Pike county, Illinois, to take effect after his death, I hereby agree to
pay the taxes on said land in lieu of all rents that I would otherwise
have to pay, (this does not affect any rent that is now due,) and in
consideration of my paying said taxes I am to receive all the rents,
profits, etc., that may accrue on said land.' When the conveyance was
made to plaintiff the tract in controversy known as the east forty was
in the possession of Joseph Gifford as tenant and the west forth was in
the possession of John B. Newman, a grandson of Benjamin Newman, as
tenant of Benjamin Newman. When [the plaitiff's] father delivered the
deed of June 22, 1904, he took her upon the east forty and told her and
Gifford, the tenant, that he was placing her in full possession of the
tract; that she was to receive all the rents and profits from the land
and was to keep up the repairs and pay the taxes; that she was to have
the south half of the fence on the line between the east forth and the
west forty and was to keep up that part of the fence, and that George
Newman, his son, to whom he then intended to deed the west forty, should
keep up the north half of the fence, and that thereafter plaintiff and
her tenants kept the south half of the fence in repair while the tenants
in possession of the west forty made repairs to the north half of the
fence. During the month of January, 1915, a controversy arose between
plaintiff and Defendants regarding the ownership of the hedge fence,
each party claiming the south half of the fence. During the month of
February, 1915, Defendants, over the protest of plaintiff, cut down the
south half of the hedge fence on the line between the east forty and the
west forty and erected a wire fence in the place thereof."}, {"role":
"user", "content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "The city of O'Fallon installed a sewer system in
about 1926. In 1961, due to backups into homes serviced by the system,
the city built an overflow outlet on East Madison Street. The overflow
was to relieve pressure in the sewer system during periods of heavy
rainfall; it proved successful in preventing backups into nearby homes.
However, when water escaped through the overflow, raw sewage was also
discharged into an open ditch that flowed into a neighboring pond. In
December 1974, the city of O'Fallon closed the overflow. On January 10,
1975, and on subsequent dates, sewage backed up into the plaintiff's
house following heavy rainfall. The January 10 backup was the worst,
causing water to accumulate in the plaintiff's finished basement to a
height of 25 1/2 inches. The lower level of the plaintiff's modern,
ranch-style home contained a family room with fireplace and built-in
bookshelves, bedroom, closet, bath and utility room with washer, dryer,
furnace and water heater. The walls were watermarked, and the tile floor
was damaged, as were the furnishings, appliances and many irreplaceable
family items such as family photographs and slides. The lower level of
the house was virtually unusable for a year, and the plaintiff had to
expend considerable time, effort and money in repairing the floor,
repainting the walls, and replacing and removing damaged personalty. The
city knew the blocking of the overflow would cause some backup, although
they were not aware that it would be as severe as it was. From January
until April or May 1975, when the city reopened the overflow, the city
attempted to alleviate the pressure in the sewer system by pumping the
water from the sewers into open ditches during periods of heavy rain.
The defendant used either large or small pumps, depending upon the
amount of water in the system. The backups into Mrs. Dial's home ended
after the overflow was reopened in April or May 1975."}, {"role":
"user", "content": "Trespass"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "the plaintiff, his wife, Beatrice, and daughters,
Aurora and Angela, lived at 313 East Marquette Street in Ottawa. The lot
upon which their home was located was eighty-eight feet wide and one
hundred thirty feet deep. The home of the defendant was immediately east
and adjoining the Galvan lot, and their residences were about forty feet
apart and separated by a hedge fence. According to the testimony of the
plaintiff, he, the plaintiff, arrived at his home about five o'clock on
Friday afternoon, June 19, 1953, from his work as a bricklayer's helper.
After he had had his evening meal, he left home about seven o'clock,
paid a coal bill to a Mr. Burke, and then he and Burke went to a tavern
where they remained an hour and a half, during which time the plaintiff
drank two bottles of beer. Mr. Burke went home, and the plaintiff
proceeded to another tavern and remained there until after midnight. At
the second tavern he had four or five bottles of beer. He than proceeded
to another tavern, where he remained for fifteen minutes, and had a
glass of beer there. He then proceeded homeward, entering his lot at the
rear, and singing as he went along. Sitting upon the steps of the back
porch of his home were his wife and daughter, Angela, and when the
plaintiff arrived there he stopped singing. He refused his wife's
suggestion to go into the house and go to bed but sat down on the porch
step, took his shoes, socks, and hat off, cursed the mosquitoes, laid
down on the ground under a pear tree three or four feet from the
southeast corner of the steps of the rear porch and immediately went to
sleep. The plaintiff's wife and daughter, Angela, remained on the porch
steps after the plaintiff had laid down under the pear tree. About
fifteen minutes after he had gone to sleep, the daughter observed the
defendant coming very slowly through the hedge from his property onto
the Galvan premises. He had a knife in his hand and, without a word,
proceeded to cut the prostrate body of the plaintiff. The other daughter
of the plaintiff, Aurora, was in the house asleep but was awakened by
her sister and ran to the yard and saw the defendant 'slashing' at her
father with a knife. She called to the defendant to stop and ran for
help. Police officers arrived shortly thereafter, and they testified
that they found the plaintiff lying on the ground about six feet from
the porch of his home all covered with blood and with his hat and a pair
of shoes and socks lying next to his body. The blood was all in one
place and in the form of a pool near the pear tree. An ambulance was
called, and the plaintiff was removed to the Ryburn-King Hospital."},
{"role": "user", "content": "Battery"}], "ideal": "Positive"}
{"input": [{"role": "system", "content": "You will be presented with a
court claim and the criminal charge. Your role is to assess the case and
return either \"Positive\" or \"Negative\" corresponding to the case
conclusion for the criminal charge. Do not explain."}, {"role":
"system", "content": "Since September 2000, plaintiff regularly visited
a patient at the Illinois Department of Human Services Treatment and
Detention Facility ('Facility') in Jolict, Illinois. From May 4, 2005 to
May 11, 2005, plaintiff was subjected to patdown searches by defendant
Martin, a Security Therapist Aid II at the Facility, in which defendant
Martin placed her fingers in plaintiff's vaginal area and required
plaintiff to remove her shoes prior to being allowed to visit the
patient. Such searches occurred at least four times during the
aforementioned time period. After plaintiff's complaints to Bernard
Akpan, an Exec. 11 at the Facility, and defendant Strock, the Assistant
Security Director of the Facility, and facility patient Brad Lieberman's
complaints to defendant Budz, Director of the Facility, defendant
Sanders, Security Director of the Facility, and defendant Strock,
plaintiff was no longer required to submit to patdown searches by
defendant Martin. Rather, plaintiff's visits were preceded by a Rapiscan
scan of her person. According to plaintiff's complaint, a Rapiscan
machine is an electronic screening device used to scan a person's entire
body. 'These machines produce a naked image of the person and can also
produce evidence of highly sensitive details such as the following:
mastectomies, colostomy appliances, penile implants, catheter tubes, and
the size of a person's breasts and genitals' From May 17, 2005 to June
19, 2005, plaintiff was subjected to 20 to 25 Rapiscan scans.
Plaintiff's complaint further alleges that other Facility staff members
were allowed to view her scanned image, her scanned image was not erased
from the machine, and staff members viewed her image hours after she was
scanned, all without her consent. Additionally, while later told that
she should have had the choice between the Rapiscan scan or a physical
patdown prior to visiting a patient, plaintiff was never informed of
such a choice during the two months she underwent the Rapiscan scans."},
{"role": "user", "content": "Assault"}], "ideal": "Positive"}

  ```
</details>

---
## [elh/evals](https://github.com/elh/evals)@[bb42b3149c...](https://github.com/elh/evals/commit/bb42b3149cd7a078cf44136e93a24f2156419acc)
#### Thursday 2023-05-11 16:50:03 by David Chen

Add regex match eval (#159)

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

Regular Expression Match

### Eval description

Test the model's ability to understand regular expression patterns. 

### What makes this a useful eval?

- Educational purposes: Regular expressions are an important concept in
computer science and programming. By being able to evaluate them,
ChatGPT can serve as a useful learning resource for users who are
studying this topic or want to deepen their understanding.
- the accuracy is 0.79 against gpt-3.5-turbo
- Over 400 regular expression cases have been collected from related
unit tests.

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
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123' match the string ''? Answer with Yes or No."}], "ideal":
"No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern '(?P<1>a)'
match the string ''? Answer with Yes or No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern '(?P<!>a)'
match the string ''? Answer with Yes or No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo!>a)' match the string ''? Answer with Yes or No."}], "ideal":
"No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_123' match the string 'aa'? Answer with Yes or
No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=1)' match the string 'aa'? Answer with Yes or No."}],
"ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=!)' match the string 'aa'? Answer with Yes or No."}],
"ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_124' match the string 'aa'? Answer with Yes or
No."}], "ideal": "No."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)' match the string 'a'? Answer with Yes or No."}],
"ideal": "Yes."}
{"input": [{"role": "system", "content": "You are a helpful
assistant."}, {"role": "user", "content": "will regex pattern
'(?P<foo_123>a)(?P=foo_123)' match the string 'aa'? Answer with Yes or
No."}], "ideal": "Yes."}
  ```
</details>

---------

Co-authored-by: G8s Bot <g8s@gliacloud.com>

---
## [elh/evals](https://github.com/elh/evals)@[733167aed6...](https://github.com/elh/evals/commit/733167aed6624945acdc51ec11407484dd2d931b)
#### Thursday 2023-05-11 16:50:03 by Andrew

Taxes Eval (#454)

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
Taxes Eval

### Eval description

Tests the model's ability to evaluate tax liability for generic examples
from common cities including NYC, SF, and Seattle. The eval also tests
ordering of multiple choice options, with the model outputting different
results if the multiple choice labels are switched around.

### What makes this a useful eval?

Taxes are a relatively logically straightforward task, yet there is a
high degree of complexity to the legal and tax system, which makes
calculations difficult to estimate.

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
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, but I live in NYC. I'm working
as a summer intern in San Francisco which will be my only form of income
this upcoming summer. Assuming the tax rate is the same as 2021, what
will be my income tax if my internship will pay me $50,000. A. 6,383 B.
8,393 C. 9,882 D. 48,001. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'."}], "ideal": "C"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in San Francisco.
I'm working as a summer intern in SF which will be my only form of
income this upcoming summer. Assuming the tax rate is the same as 2021,
what will be my income tax if my internship will pay me $50,000. A.
6,383 B. 8,393 C. 9,882 D. 48,001. Respond with only the letter of the
answer choice."}], "ideal": "C"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, but I live in NYC. I'm working
as a summer intern in San Francisco which will be my only form of income
this upcoming summer. Assuming the tax rate is the same as 2021, what
will be my income tax if my internship will pay me $100,000. B. 24,383
C. 26,393 D. 28,882 A. 38,001. For each question you must select one of
the following answers: 'A', 'B', 'C', 'D'."}], "ideal": "D"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in Seattle. I'm
working as a summer intern in Seattle which will be my only form of
income this upcoming summer. Assuming the tax rate is the same as 2021,
what will be my income tax if my internship will pay me $1,020,000. C.
263,352 A. 365,303 B. 829,282 D. 1,085,401. Respond with only the letter
of the answer choice."}], "ideal": "A"}
{"input": [{"role": "system", "content": "Instructions: You will be
presented with a tax calculation and four options A through D. Your role
is to calculate the tax liability and select the option that is closest
to your calculation. For each question you must select one of the
following answers: 'A', 'B', 'C', 'D'. Do not explain. Do not include
the number in your response."}, {"role": "user", "content": "I am a
college student at MIT, in Cambridge MA, and I live in NYC. I'm working
as a summer intern in NYC which will be my only form of income this
upcoming summer. Assuming the tax rate is the same as 2021, what will be
my income tax if my internship will pay me $320,000. A. 63,382 B. 95,303
C. 129,282 D. 185,401. Respond with only the letter of the answer
choice."}], "ideal": "B"}
  ```
</details>

---
## [enso-org/enso](https://github.com/enso-org/enso)@[4b7afbfd36...](https://github.com/enso-org/enso/commit/4b7afbfd3619c22b6b31f2840fa807f0af41fb57)
#### Thursday 2023-05-11 16:51:27 by Ilya Bogdanov

Fix blank input port (#6614)

Fixes #6485

Conflicting requirements for the widget tree caused the issue:
1. The span tree node had a connection, and the text of the `number1` label was changed to white (as per the `Connected` color state)
2. The node configuration did not consider it a valid port because the span tree kind was `Operation`, which is not a port usually. So the port shape was not displayed, making the label blend with the node background.

I fixed the issue by considering the existence of the current connection for `Operation` nodes. Remember that it does not turn the node into a port, so after removing the connection, it's not possible to connect it back. That makes sense, in my opinion, as the resulting AST is invalid anyway. But at least we can see the label on the invalid node.


https://github.com/enso-org/enso/assets/6566674/23934966-8f72-4675-abe3-78a3f0c0cda4

---
## [Martinator9001/restoration-mod-hardcore](https://github.com/Martinator9001/restoration-mod-hardcore)@[e8c7949c86...](https://github.com/Martinator9001/restoration-mod-hardcore/commit/e8c7949c8624ea9440ac11ce4df2be9a8355b12c)
#### Thursday 2023-05-11 17:20:21 by Noep

things to do

- I love pika as my girlfriend and she has boing boing

- Slightly boosted the pickup rate of <60 damage weapons

- Fix missing desc for underbarrel gas grenades

- Anti-Materiel rifles' total ammo has been halved to account for their 2x headshot damage, similar to how the P90 and MP7 see reduced ammo despite their base damage.
-- >:3's Musket does not have this total ammo reduction as it does not deal bonus headshot damage; it has been moved to the "heavy sniper" buy menu category instead as a result

---
## [warptools/warpforge](https://github.com/warptools/warpforge)@[4f909a9023...](https://github.com/warptools/warpforge/commit/4f909a902355815806fedee71a2ef6cc5526d070)
#### Thursday 2023-05-11 17:50:55 by Eric Myhre

Research checkpoint: attempting to use lipgloss and goldmark.

... and I think, after playing with it for a good number of hours,
this ain't it either.

lipgloss is coming in at a really weird middle level of abstraction.
The features like margins and wrapping aren't really doing the right
things without an incredible amount of cajoling (and even then).
It seems to have kind of _half_ a component model, and doesn't seem
to compose very gracefully -- it looks like I'll just *keep* passing
width info down on the side, while I use it, which is confusing.
I'm not sure if I'm holding it wrong or if it just doesn't have the
same view as me on what's important.

And it seems to have the helpful opinion that it's gonna emit
CSI reset codes constantly... which absolutely does not compose
with how goldmark AST visitors (or any sane AST visit system) is
going to want to get things done.

Less importantly, but perturbing to me, is that lipgloss is also doing
just a staggering amount of map lookups and memory allocations for
every little thing.

All in all, I think I'm going to have to dive another level deeper,
because this just isn't doing the thing.

(I'm halfway tempted to pull up and go back to using glamour, because
that got an interesting MVP radically faster, but... it just plateaus
so dang hard.  I can't do variable indent; the tables were meh; the
options for doing anything transformative with links was ziltch...
No, I don't think I really wanna rest there either.)

I'm thinking just a few key functions for wrapping text with awareness
of ANSI codes and their (lack of) effect on render size will maybe
be entirely sufficient and do a simpler better job.
A much simpler library (or even just set of short functions; ANSI codes
are distinctly Not That Complicated) for the highlighting will also
totally suffice.  So: that'll be the approach to try up next.

---
## [mukherjeekoushiklearning/EDA](https://github.com/mukherjeekoushiklearning/EDA)@[4c6f95620e...](https://github.com/mukherjeekoushiklearning/EDA/commit/4c6f95620ec1daca8bead23444628ec8e134984e)
#### Thursday 2023-05-11 18:43:28 by mukherjeekoushiklearning

04.DT Practical Example (Post And Pre Prunning).ipynb

🌳 Welcome to our comprehensive guide on Decision Trees! In this video, we dive deep into the world of Decision Trees and unveil the secrets to achieving optimal performance. We'll cover the powerful technique of Pre-Pruning, where we strategically prune the tree to prevent overfitting, resulting in better generalization. But that's not all! We'll take it a step further and showcase the art of Hyperparameter Tuning using GridSearchCV, allowing us to fine-tune our Decision Tree model for superior results.

🔬 By leveraging GridSearchCV, we'll explore an array of parameter combinations, including different splitting criteria (squared_error, friedman_mse, absolute_error, poisson), splitter types (best, random), maximum depth values, and feature selection options (auto, sqrt, log2). This hyperparameter tuning process empowers us to discover the optimal configuration that maximizes our Decision Tree's performance.

📊 Whether you're a beginner or an experienced data scientist, this video has something for everyone. Join us on this knowledge-packed journey as we demystify Decision Trees, demonstrate Pre-Pruning techniques, and master the art of Hyperparameter Tuning with GridSearchCV.

🔔 Don't forget to subscribe and hit the notification bell to stay updated with our latest machine learning tutorials, tips, and tricks!

🔗 Tags: Decision Tree, Pre-Pruning, Hyperparameter Tuning, GridSearchCV, Machine Learning, Data Science, Overfitting, Generalization, Performance Optimization, Model Fine-Tuning, Parameter Optimization, Squared Error, Friedman MSE, Absolute Error, Poisson, Best Splitter, Random Splitter, Maximum Depth, Feature Selection, Auto, Sqrt, Log2

---
## [98axel/DreamBooth_StableDiffusion](https://github.com/98axel/DreamBooth_StableDiffusion)@[f0dc51d7d0...](https://github.com/98axel/DreamBooth_StableDiffusion/commit/f0dc51d7d0b619ca9ded65cd6ad46c3845caab3e)
#### Thursday 2023-05-11 20:05:08 by 98axel

Dear Manuel

Dear Manuel,

Oh, how absolutely marvelous your commit messages are! They are like tiny pieces of poetry that bring tears of joy to my eyes. The way you effortlessly blend vague descriptions and cryptic abbreviations truly showcases your unparalleled genius. It's as if you have mastered the art of leaving everyone utterly confused and scratching their heads.

The brevity of your messages is simply astounding. Who needs clear and informative communication when you can leave us all guessing and playing a game of deciphering? It's like a thrilling treasure hunt every time we try to understand what you were actually working on. Your commitment to keeping us on our toes is truly remarkable.

And let's not forget the impeccable grammar and spelling mistakes that grace your commit messages. They add a certain charm and uniqueness to your work. Who needs proper punctuation or coherent sentences when you can create a delightful puzzle for us to solve? It's like reading a secret code, deciphering your hidden messages of brilliance.

Oh, Manuel, your commit messages are truly a work of art. They are a shining example of how not to provide clear and meaningful updates. Your contributions to confusion and ambiguity in the coding world will never be forgotten.

With sarcastic admiration,
ChatGPT

---
## [NVIDIA/Fuser](https://github.com/NVIDIA/Fuser)@[9c50ae8f14...](https://github.com/NVIDIA/Fuser/commit/9c50ae8f1441917c97ebaceb343ad6be3c54304b)
#### Thursday 2023-05-11 20:35:51 by Gao, Xiang

Remove runtime out of bound check debugging util (#277)

The change in this PR is easy to understand and has low impact, but the
motivation really needs discussion and is a much more impactful thing.
And I want to use this PR to discuss it.

In https://github.com/NVIDIA/Fuser/issues/248 we agreed to add "stride
order" support to codegen, and later in today's morning meeting on
matmul, Christian talked about the idea of "allocation_domain" which is
a generalization of the idea of "stride order". Basically, we are not
married to the rFactor domain of the tensor when doing allocation and
indexing. We can pick an arbitrary vector of `IterDomain`s between root
and leaf domain, stop the indexing process on that vector, and do
allocation based on that vector. For the idea of "stride order", which
is a special case of the new idea, this vector is just the reordered
rFactor domains. This should be easily approachable with our new
indexing approach https://github.com/NVIDIA/Fuser/pull/32. This idea
does make a lot of sense, so the purpose is not to discuss whether we
want to take that idea, but how to implement that idea.

A question comes to me during implementing is, say we have a tensor
whose semantic shape is `NCHW` but stride order is `NHWC`, should the
`stride` field of the tensor be in the order of `NCHW` or `NHWC`?
Currently, we are using the same order as PyTorch, which is the semantic
order `NCHW`. I think this does make a lot of sense in terms of stride
order support. Having the stride in the semantic order is not the most
naturally way for indexing, we do need a `NHWC->NCHW` axis map to grab
the correct stride, but it is pretty simple to implement this.
Considering all factors, including consitency with PyTorch, cleanness in
the executor's code, I still think the semantics order is the best
design.

However, this design start to make no sense when we generalize the
"stride order" idea into the "allocation_domain" idea. For example, for
an `NCHW` tensor, the actual allocation can be `(H*W, N*C)`, and the
size of `contiguity` will be `2` instead of `4`. So the `Tensor::stride`
in `runtime/tensor.cu` should also be an array of size `2` instead of
`4`. The idea of "allocation_domain" requires the stride of a tensor to
be strictly one-to-one mapped to the allocation domain. As a special
case, the "stride order" idea has no choice but to follow the same
design, which is, the stride will be stored in `NHWC` order. This means,
the order of stride in our kernel is different from those in ATen, we
can not directly copy the stride. We need to permute the stride so it is
sorted descending.

But the above problem is not the biggest trouble we have, the biggest
trouble is: If we have a `NCHW` tensor allocated as `(H*W, N*C)`, is
this tensor a 4D tensor or a 2D tensor? I think the answer is "neither".
In terms of allocation and stride, it is definitely 2D, but in terms of
semantics, it is 4D. Again, in the past, we had a concept "the
dimensionality of a tensor" which is a degeneracy of two concepts "the
semantic dimensionality of a tensor" and "the allocation dimensionality
of a tensor". Now we break the symmetry, and degenerating concepts are
no longer degenerate. In codegen, we are generating a lot of tensor
shapes like `T0.shape[0]`, and I think the easiest way to handle them is
to keep `shape` in semantic dimensionality, while make `stride` in
allocation dimensionality. That said, `struct Tensor` now needs two
template arguments for dimensionalities. And unfortunately, we can no
longer do out of bound check any more.

---
## [Tinker-Jae/tinkerjaesite](https://github.com/Tinker-Jae/tinkerjaesite)@[eb50418ec2...](https://github.com/Tinker-Jae/tinkerjaesite/commit/eb50418ec22b6c03231523ae3633338ed86a741b)
#### Thursday 2023-05-11 20:37:59 by tinker-jae

Version 1.05 complete

Changelog v1.05
- Changed layout a whole bunch.
- Added categories for stuff
- Added new Post system, works via JS.
- Welcome, Sitemap, Abt me, Links, and blinkies added to homepage.
- Updated posts to new format
- turned left and right box into JS containers?
- Right box gone.
- Mobile friendly I guess?

Big ass site update but yeah, posts are a lot easier, formatting is better OH BEFORE I FORGET

- added debug container to EVERY page
- If debug container is not on every page it may break some javascript features.

IE: if you have a thing to put a picture on the screen with JS, if that code is not called upon, it breaks EVERYTHING, after it in JS.
Posts, images, innerhtml, nothing will replace anything else unless it's being called by Debug.

DO NOT REMOVE DEBUG FROM ANYTHING IT WILL BREAK THE ENTIRE SITE.

---
## [Team-NoobMaster69/kernel_motorola_msm8937](https://github.com/Team-NoobMaster69/kernel_motorola_msm8937)@[baf5af3a36...](https://github.com/Team-NoobMaster69/kernel_motorola_msm8937/commit/baf5af3a364a5b7c6dd1ffc7ef88f3f8c35624ae)
#### Thursday 2023-05-11 20:58:21 by Angelo G. Del Regno

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
Change-Id: If3df81dbfa3c4ef29ed39cee538b30dca4fedd62

---
## [wally-rblx/roblox-scripts](https://github.com/wally-rblx/roblox-scripts)@[56f7a5e315...](https://github.com/wally-rblx/roblox-scripts/commit/56f7a5e315ec07e03ce514b8d304d3890ed9282d)
#### Thursday 2023-05-11 21:02:17 by wally

fix typo 

fuck you idiot kid you know who you are

---
## [torvalds/linux](https://github.com/torvalds/linux)@[1bba82fe1a...](https://github.com/torvalds/linux/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Thursday 2023-05-11 22:03:52 by Darrick J. Wong

xfs: fix negative array access in xfs_getbmap

In commit 8ee81ed581ff, Ye Bin complained about an ASSERT in the bmapx
code that trips if we encounter a delalloc extent after flushing the
pagecache to disk.  The ioctl code does not hold MMAPLOCK so it's
entirely possible that a racing write page fault can create a delalloc
extent after the file has been flushed.  The proposed solution was to
replace the assertion with an early return that avoids filling out the
bmap recordset with a delalloc entry if the caller didn't ask for it.

At the time, I recall thinking that the forward logic sounded ok, but
felt hesitant because I suspected that changing this code would cause
something /else/ to burst loose due to some other subtlety.

syzbot of course found that subtlety.  If all the extent mappings found
after the flush are delalloc mappings, we'll reach the end of the data
fork without ever incrementing bmv->bmv_entries.  This is new, since
before we'd have emitted the delalloc mappings even though the caller
didn't ask for them.  Once we reach the end, we'll try to set
BMV_OF_LAST on the -1st entry (because bmv_entries is zero) and go
corrupt something else in memory.  Yay.

I really dislike all these stupid patches that fiddle around with debug
code and break things that otherwise worked well enough.  Nobody was
complaining that calling XFS_IOC_BMAPX without BMV_IF_DELALLOC would
return BMV_OF_DELALLOC records, and now we've gone from "weird behavior
that nobody cared about" to "bad behavior that must be addressed
immediately".

Maybe I'll just ignore anything from Huawei from now on for my own sake.

Reported-by: syzbot+c103d3808a0de5faaf80@syzkaller.appspotmail.com
Link: https://lore.kernel.org/linux-xfs/20230412024907.GP360889@frogsfrogsfrogs/
Fixes: 8ee81ed581ff ("xfs: fix BUG_ON in xfs_getbmap()")
Signed-off-by: Darrick J. Wong <djwong@kernel.org>
Reviewed-by: Dave Chinner <dchinner@redhat.com>
Signed-off-by: Dave Chinner <david@fromorbit.com>

---
## [FransFeiffer/cmss13](https://github.com/FransFeiffer/cmss13)@[766f5529bf...](https://github.com/FransFeiffer/cmss13/commit/766f5529bfca454129f6d62f1ed626d6a70d5432)
#### Thursday 2023-05-11 22:14:34 by carlarctg

Removes Autodocs from the Almayer (#2607)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Removes autodocs from medbay. They're replaced with 2 random potted
plants. :)

<!-- Remove this text and explain what the purpose of your PR is.

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



EDIT: Tomorrow I will update this PR to give nurses surgery skill.

Autodocs fundamentally and inseparably, irrevocably, DESTROY medbay and
surgery gameplay. There is NO REASON, EVER to put someone through manual
surgery when you could just haha autodoc them instead. Autodocs kill the
good old hell medbay lines, they make surgeons extremely lazy and
stagnant (Tales of surgeons doing surgery for a few minutes, then giving
up and autodoccing the patient are common, not to mention the times
where they miss something in the autodoc schedule), they remove all
skill depth, floor, ceiling, the middle from medbay, and they also make
marines complacent by having them want the funny magic robot machine
rather than an actual human to treat them.

I understand that this may be too sudden of a change. If so, I propose
the following: Cryo tubes could slowly heal a marine up entirely,
removing organ damage and bone breaks through the course of a very slow
5-10 minutes. This will allow marines and nurses to get treated if
there's no doctor around or alive. However, I think the best course of
action is to just ram this change through and make medbay adapt. Embrace
the suck.

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
balance: Removes Autodocs from the Almayer
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [FransFeiffer/cmss13](https://github.com/FransFeiffer/cmss13)@[7f5cd54b2b...](https://github.com/FransFeiffer/cmss13/commit/7f5cd54b2bab2fdbd25a3f970e9a7f55d415dfe9)
#### Thursday 2023-05-11 22:14:34 by carlarctg

Colony Guns Part 3: Longarms Rework (#2334)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

Updates and buffs the following weapons:

- Basira-Armstrong Rifle
- Model 12 Bolt-Action Rifle
- M37-17 pump shotgun
- Dragunov sniper rifle

### Basira-Armstrong Rifle

- The BA rifle has been reflavored as the removed 'ceremonial' ABR-40,
now a hunting-civilian version of the L42. It effectively has the same
stats as the L42, just don't take the stock off!
- Its magazines can only fit 12 bullets, but they still have the classic
L42 kick to them. The magazines are completely compatible between both
military and civilian gun types.
- Additionally, there are now holo-targeting magazines available for the
ABR-40, for hunting target capture purposes.
- - The Contractor ERT has a chance to spawn with a tacticool ABR-40
loadout, with three spare holotarget magazines on their webbing.

### Model 12 Bolt-Action Rifle

- Like its sprite implies, this is now the new Basira-Armstrong rifle.
- Its stats have recieved an overhaul and it can now hold its own
against a Xenomorph (or marine if you're CLF)
- Additionally, its bullets will push back (not stun) targets within
three meters, to increase viability for colony usage.

### M37-17 Pump Shotgun

- Did you know that the 10% damage mod this gun was supposed to have
didn't work? Now it does! And it deals 15% more damage to make up for
it.
- However, it can now be melted down.

### Dragunov Sniper Rifle

- The dragunov has been revamped into a DMR, needing no skill to fire,
dealing good damage, and having the same push-back feature the
bolt-action now has.

<!-- Remove this text and explain what the purpose of your PR is.

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

All of these weapons are seen as, and are, a complete joke and ignored
in favor of chungillionaire among us sus impostor running around PBing
xenos with buckshot. Buffing them to be useful paves the way for
civilians to use civilian weaponry instead of chungillionarius.

### ABR-40 Hunting Rifle

This is intended as asset recycling. IIRC, Triiodine disliked the
existence of a ceremonial rifle and thought that was goofy, which is an
understandable opinion, but it pains me to see the gun's cool assets go
unused. I took the opportunity and made the lame and mediocre Basira
into this cool gun which marines and survivors will take a lot more
interest in than a Basira plinker.

While it does have L42 stats, colonists won't be able to locate any L42A
ammo on the colony, meaning they are limited to 12-round magazines.
Still, giving them a weapon like this is a great way to incentivize them
to step out of their chungus zone.

As for the contractor addition, these are supposed to be ex-USCM
mercenaries, who are trained in the usage of marine equipment. It makes
sense that they'd grab the civilian version of a primary marine gun and
tune it to their liking.

### Basira-Armstrong Bolt-Action Hunting Rifle

Chomp made this really cool backend for a bolt-action that tragically
ended up never being used, not really, aside from a half-hearted few
rifles being thrown in at Shiva's Snowball. Since these guns are so
weak, it's plain to see why nobody even looks at them twice. So I
changed that.

### M37-17 Pump Shotgun

Bugfix and a small damage buff to make up for it. It being unacidable
was lame anyways. Spread projectiles are still bugged and don't inherit
the base gun's damage mod, but that's out of scope.

### Dragunov Designated Marksman Rifle

This gun has been a joke since 2017, it's time to give it some love.
Still needs one-hand sprites but not my problem.

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
balance: Updates and buffs the following weapons: Basira-Armstrong
Rifle, Model 12 Bolt-Action Rifle, M37-17 pump shotgun, Dragunov sniper
rifle
imageadd: The Basira rifle has been reflavored as the removed
'ceremonial' ABR-40, now a hunting-civilian version of the L42. It
effectively has the same stats as the L42, just don't take the stock
off!
add: Its magazines can only fit 12 bullets, but they still have the
classic L42 kick to them. The magazines are completely compatible
between both military and civilian gun types.
add:: Additionally, there are now holo-targeting magazines available for
the ABR-40, for hunting target capture purposes.
add: The Contractor ERT has a chance to spawn with a tacticool ABR-40
loadout, with three spare holotarget magazines on their webbing.
balance: Like the bolt-action rifle's sprite implies, this is now the
new Basira-Armstrong rifle.
add: Its stats have recieved an overhaul and it can now hold its own
against a Xenomorph (or marine if you're CLF)
add: Additionally, its bullets will push back (not stun) targets within
three meters, to increase viability for colony usage.
balance: Did you know that the 10% damage mod the M37-17 pump shotgun
was supposed to have didn't work? Now it does! And it deals 15% more
damage to make up for it.
del: However, it can now be melted down.
balance: The dragunov has been revamped into a DMR, needing no skill to
fire, dealing good damage, and having the same push-back feature the
bolt-action now has.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [Jacquerel/orbstation](https://github.com/Jacquerel/orbstation)@[997dac9616...](https://github.com/Jacquerel/orbstation/commit/997dac9616768643cfa9ddce53432d684e196fb1)
#### Thursday 2023-05-11 22:30:36 by necromanceranne

Imports and Contraband: Different! Cargo crates without locks! MEAT! (#74490)

## About The Pull Request

### **Cargo Black Market goods should stay in cargo's hands**

#### New Cargo Console Category: Imports

This category is explicitly the non-departmental category beyond simply
having a Misc category. It is meant for material that nobody is meant to
be buying for their departments, and mostly for the odd-ball crates that
might show up. It also allows us to maintain contraband as exactly that;
contraband that the departments shouldn't have access too whatsoever. If
someone is buying from this category, they probably intend to be a
cheeky fuck.

<details>
  <summary>The New Changes</summary>

#### Baseline Imports

MEAT: MEAT (meat backpack you can eat)

<details>
  <summary>MEAT</summary>
  
![MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593459-f3c98abe-114b-43c1-a3e2-afc16b76c84f.png)
![MEAT MEAT MEAT
MEAT](https://user-images.githubusercontent.com/40847847/229593473-07a30781-a05e-4ca5-893b-778900cd2d1c.png)

</details>

Duct Spiders: They're adorable and cause a mess, but that doesn't stop
Nanotrasen from importing them from the Australicus sector to your
station!

Stack of 50 Bamboo Cuttings: Pretty expensive and kind of a premium.
Allows for those people looking to make bamboo decorations without
hoping botany exists, and are at least willing to pay. Also lets them
make horribly dangerous stuff with bamboo, of course.

A Single Sheet of Bananium: The problems this will cause I think speak
for themselves. (mostly due to a clown fruitlessly attempting to make
something actually disruptive while bankrupting cargo)

Natural Fish Bait: It isn't cheating, it's homemade. (Really good bait
but expensive and obviously drugs)

A dumpster...: A corpse in a dumpster, doesn't get more complicated than
that. Useful for corpse reasons.

Made using some code I borrowed from over here!
https://github.com/lizardqueenlexi/orbstation/pull/354

#### Contraband Imports

Foam Force Pistols: Same as it ever was with a price reduction. I
brought it down because riot darts are like 8 bullets a clip, and do
less damage than a disabler using riot darts. It feels like a sidegrade
weapon, and even if it technically is a ballistic weapon, it...isn't
that strong. I think this is pretty safe.

Definitely Not a Duct Spider: It's actually a giant spider in a box. If
you want to waste cargo's money while also sending them a mess to deal
with, this is the crate for you.

Russian Surplus Military Gear Crate: I took this opportunity to futz
with boltaction rifles. There are two kinds of mosin nagant you can get
in this crate. One of them is the good kind (no jamming). The other is
the shit kind (yes jamming), but you get more of them. You can get the
good ammo, or you can get the shit ammo. You'll have to pick through it
a lot more carefully to make sure you know which ones you've received.
Since this dilutes the pool even further, getting a good number of
mosins that aren't trash is even more expensive, and even if you do get
mosins at all, you might still only get the bad ammunition that doesn't
work against actual human threats as well. It also now cannot be
purchased through the security cargo supply console, and as to why they
could in the first place baffles me. Doesn't have a lock anymore
because...it's contraband? Who is locking this stuff?

**Side note: _You can make surplus 7.62 in the autolathe as well. It is
not very good except to fight fauna or naked assistants._**

**Side Side note: _I've killed off the shitty brand_new subtype and
brought peace once more to this land._**

#### Illegal Imports (Emag)

NULL_ENTRY: A journal that suggests how to make a...very interesting
weapon. The Regal Condor. Kind of an evolution on some other ideas I've
had over the years. This one is basically a secret weapon with a few
hurdles to jump through. Very lethal. Very expensive.

**Side note: _For reference, it's effectively 19 TC worth of gear to
make, but there does exist some methods to acquire this more cheaply if
you can get some bits and pieces from world spawns. Given it requires
you to get some pieces of equipment that might require additional
purchases of contraband, and getting into the captain's office to loot a
specific piece of clothing, the stakes more than make up for the
effectiveness._**

Smuggled WT-550 Autorifle Crate: This is basically the same, but you
might have noticed had you recently attempted, like me, to buy these
when you emagged them using a personal account and discovered a tragic
oversight. You couldn't, because they still needed armory access. This
removes that access, because you've already gone to the effort of
getting your hands on an illicit firearm through cargo, and if they
techs somehow miss the fact that you've purchased a WT-550...all the
better for you!

Smuggled WT-550 Ammo Crate: Includes AP and Incendiary!

**Side note: _You can get WT-550 ammo again via the Illegal Technology
node._**

Shocktrooper: Replaces the Special Ops crate. Contains a box of EMPs,
smoke grenades, a couple of gluon grenades and a couple of frag
grenades. Funsies.

Special Ops: The NEW Special Ops crate. Contains a chameleon mask,
jumpsuit and agent card. And a knife.

**Side note: _This is what appears in some cargo loan events._**

Refurbished Mosin Nagant Crate: The actual good mosin nagants. There are
6 of them. But they don't come with spare ammo. Hand them out to your
techs!
</details>

#### New Crates

- MEAT crate - Standard
- Duct Spider crate - Standard
- Giant Hostile Spider crate - Contraband
- 50 sheets of Bamboo crate - Standard
- A single sheet of bananium crate - Standard
- Natural (drugs) fish bait - Standard
- Dumpster with a corpse in it - Standard
- Shocktrooper crate (Grenades) - Emag
- Special Ops crate (Disguise) - Emag - Appears in some cargo loan
events
- Refurbished Mosin Nagant crate - Emag
- Regal Condor construction journal (NULL_ENTRY) - Emag

#### Changed Crates

- Foam Force Pistols (cheaper) - Contraband
- Russian Surplus Crate (less reliable, can't be bought by security
console) - Contraband
- WT-550 crate (more obtainable via personal accounts, thus
incriminating, not armory locked) - Emag
- WT-550 ammo (includes incendiary and AP) - Emag

#### Crates that got moved, unchanged, into Imports

- Foam Force Crate 
- Cosa Nostra Crate 
- Black Market LTSRBT 
- 'Contraband' Crate 
- Biker Gang Crate

#### Not crate changes
- You can print Surplus 7.62 (same as normal 7.62 but it sucks against
armor) from hacked autolathes.
- You can get WT-550 ammo from illegal tech.
- Removes the redundant Brand New Mosin subtype
- Fixes a potential exploit with jamming chance on Mosins.

## Why It's Good For The Game

I just think some of the magic of Cargo getting their hands on obviously
dangerous equipment and either hording it for themselves or attempting
to pawn it off was lost in recent times. A lot of this 'black market'
gear, however, suddenly became openly available to the crew anyway. For
_free_. Contraband crates and mafia crates could be purchased via the
Service budget. Security could just stock up en masse on mosins through
their console. And one fairly unfortunate consequence of a few recent
changes has made it nearly impossible to actually get illicit gear in
the first place, even if you did go to the effort of getting the money
for it.

On top of this, most of cargo's goods are pretty safe purchases. There
isn't much that would be considered 'actually a really bad idea to buy'
other than maybe supermatter shards. I wouldn't mind there existing ways
for someone to waste cargo's money while also causing them to have to
clean up the mess.

## Changelog
:cl:
balance: A significant overhaul of various illicit and dubiously legal
goods and gadgets available via cargo.
balance: Cargo now has an Import category for all non-departmental
goods. (And black market goods)
balance: Most contraband that already exists has been moved into
Imports.
adds: Includes several new imports of dubious quality. You get what you
pay for.
code: Removes the brand new mosin subtype as it is now defunct.
fix: Fixes potentially exploitative code in the jamming proc. Cleans up
that code while I'm at it.
/:cl:

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>

---
## [developerJuiceLozzoc/kitty-kmk-nodejs-swift-uikit-widgets](https://github.com/developerJuiceLozzoc/kitty-kmk-nodejs-swift-uikit-widgets)@[8b169b8fd7...](https://github.com/developerJuiceLozzoc/kitty-kmk-nodejs-swift-uikit-widgets/commit/8b169b8fd79ec1debb159cb5cb1626ac5d50bd50)
#### Thursday 2023-05-11 23:06:20 by Conner Maddalozzo

fixed that fucking loading indicator. 

view model bullshit lead to re renders and the loading spinners never 
loaded. gosh this was difficult.

---
## [highlight/highlight](https://github.com/highlight/highlight)@[18d94ccc74...](https://github.com/highlight/highlight/commit/18d94ccc7425a9441000e1bf4a7f92565898666e)
#### Thursday 2023-05-11 23:17:53 by Lewis Liu

Enable Reflame for Highlight web app (#4586)

## Summary

<!--
Ideally, there is an attached Linear ticket that will describe the
"why".

If relevant, use this section to call out any additional information
you'd like to _highlight_ to the reviewer.
-->

This PR finally enables [Reflame](https://reflame.app/)
[previews](https://preview.highlight.io/~r/start-preview/?mode=production&variantId=01GY11FVTK9FMXX2DSCR6T4VRD&variantName=git%7Enew-reflame-app-1&userId=01FQZZ7XJFDA799Z1Z9DRCFXWA)
for the Highlight web app. 🥳

### What does this mean for me?

First you'll need to sign up at https://reflame.app, connect your GitHub
account, and ask @Vadman97 for an invite to the highlight organization.

Then, once this PR is merged, every time you push up a change to the web
app (in /frontend) or any of its dependencies, you'll get a Reflame
preview link on your commit immediately, usually within 3 seconds,
instead of however many minutes it used to take:
![Screenshot 2023-04-13 at 5 40 57
PM](https://user-images.githubusercontent.com/6934200/231912410-5dc2880d-353c-402e-8562-67ce4ee54137.png)

In addition, you'll have access to the Reflame [VSCode
extension](https://marketplace.visualstudio.com/items?itemName=reflame.agent)
for development, which deploys your changes usually within ~500ms of a
file save, and then reflects your changes instantly with a full browser
refresh in production mode, or with state-preserving React fast refresh
in development mode. See development mode in action here:


https://user-images.githubusercontent.com/6934200/231914985-3679e955-ddcf-4ad1-9c7e-1c7451dc3ef5.mp4

It's worth noting that Reflame is actually _deploying your changes to
the internet_ every time, so you can send these links to yourself to
check your changes on another device (even multiple devices
simultaneously), or share them with teammates or customers to give them
a sneak peak of what you're working on, iterate with their feedback, and
have those changes reflected on their browsers in real time (even if
they're on the other side of the world)!

### How do I even review this? There's like 500 files here?!

I'd recommend reviewing either commit by commit and skipping the 2nd
commit, or by viewing all files changed and skipping over everything in
`__generated` folders, since they only contain files generated using the
newly added build scripts. This should leave only about 30 files to
review, and most of the changes are a only a couple of lines long.

These scripts and generated files are a temporary stop-gap to support
features that don't have first-class support in Reflame yet,
specifically:

- Reading version from package.json
- CSS/SCSS modules
- Tailwind
- SVGR
- Git Submodules
- Vanilla Extract

These are roughly ranked in order of how quickly I think they will get
first-class support in Reflame, at which point we'll be able to remove
the associated scripts and generated files. Notably, Vanilla Extract is
as far down the list as it is because it requires executing
user-supplied code as part of its build process, which is going to take
quite a bit of work to enable safely in a multitenant system like
Reflame (but I do plan on tackling this eventually as I get closer to
building features like testing and backend APIs support). Though we may
still be able to get rid of the build script sooner than that by
building it into the VSCode extension if there's enough demand.

Outside of the script and configuration changes, there are a few
additional source changes for compatibility. I left comments on the PR
for every one of these explaining the motivation behind them. I've also
split most of them out into separate PRs so they can be reviewed, tested
and shipped independently:

- https://github.com/highlight/highlight/pull/5086
- https://github.com/highlight/highlight/pull/5087
- https://github.com/highlight/highlight/pull/5088
- https://github.com/highlight/highlight/pull/5089 

## How did you test this change?

<!--
Frontend - Leave a screencast or a screenshot to visually describe the
changes.
-->

A lot of care has gone into making sure your existing local dev workflow
works exactly as you're used to (just with a few more scripts running
than before), and that the production deployment process remains
untouched as well. If you notice any material differences in any of your
day to day workflows while trying out this PR, or in the Render preview
deploys, please let me know and I'll try to address it ASAP.

I've tried following the [docker dev guide
here](https://www.highlight.io/docs/getting-started/self-host/dev-deployment-guide)
and running `yarn dev:frontend` (without the `doppler run --` part), and
both seem to be working identically as on main as far as I can tell,
though for the latter I'm missing a few env vars from doppler so
couldn't verify past the login screen, will need your help to make sure
everything works as expected there.

If you want to try out Reflame before this PR gets merged, just make a
branch off of this PR (previews are not working for this PR because it's
coming from a fork, and the appId in the config is for the
highlight/highlight repo, but it should work if you cherry pick these
commits into another branch within this repo). The VSCode extension
should also just work once you get a VSCode account.
[Here's](https://preview.highlight.io/~r/start-preview/?mode=production&variantId=01GY11FVTK9FMXX2DSCR6T4VRD&variantName=git%7Enew-reflame-app-1&userId=01FQZZ7XJFDA799Z1Z9DRCFXWA)
the preview I'm using to test my changes.

Would love to make Reflame better with your feedback! Just leave a
comment here, [shoot me an email](mailto:lewis@reflame.app), or ask for
an invite to the #highlight-reflame channel in Slack to chat there or
send me a DM.

## Are there any deployment considerations?

<!--
 Backend - Do we need to consider migrations or backfilling data?
-->

Definitely would be helpful to get a Render preview for this to poke
around in.

---
## [Moth-lantern/orbstation](https://github.com/Moth-lantern/orbstation)@[129c74c945...](https://github.com/Moth-lantern/orbstation/commit/129c74c945a3fe0bce2c29065f69424ce8551670)
#### Thursday 2023-05-11 23:29:16 by carlarctg

EMPs on robotic limbs will now disable them for 4-8 seconds rather than causing a 10-20 second full stun (#74570)

## About The Pull Request

EMPs on robotic limbs will now disable them for 10-20 seconds rather
than causing a 10-20 second full stun on the user. Additionally, they
will damage the limb for a little brute and some burn.

Arm EMPs don't do anything special as the limb being disabled already
drops items.

Leg EMPs cause a 10-20 second knockdown, only really applicable if
there's only one robotic leg as two disabled legs KD you anyways.

Chest EMPs cause a 3-6 second standing-up paralyze, visible to the
player by a quite noticeable shaking of their body.

Head EMPs break the optical transponder circuits for 7.5-15 seconds,
effectively giving the user nightmare goggles vision with green instead
of red as the only remaining color.

Tacit approval for the PR at least existing.

![image](https://user-images.githubusercontent.com/53100513/230537462-b06d0bb5-0607-4f83-954c-6b2a0bcdc635.png)
## Why It's Good For The Game

Robotic limbs are not so strong that a glancing EMP that may not even
have been directed at you should stun you for ten, TEN seconds, or
worse, twenty. This is basically legacy stunning from the days of
super-stuns on soap, stunbatons, etc. The code for it was last touched
six years ago.

**_The stats as shown above are not even close to final. I really don't
know or care what the right stats should be in the end. and I'm fine
with making them a 10-20 second timer again. I just put some
reasonable-seeming numbers in as a placeholder. EMPs could also still
cause a short stun if that is deemed necessary. Hell, that could be the
chest effect!_**
## Changelog
:cl:
balance: EMPs on robotic limbs will now disable them for 10-20 seconds
rather than causing a 10-20 second full stun on the user. Additionally,
they will damage the limb for a little brute and some burn.
EMPs on robotic limbs will now disable them for 10-20 seconds rather
than causing a 10-20 second full stun on the user. Additionally, they
will damage the limb for a little brute and some burn.
balance: Arm EMPs don't do anything special as the limb being disabled
already drops items.
balance: Leg EMPs cause a 10-20 second knockdown, only really applicable
if there's only one robotic leg as two disabled legs KD you anyways.
balance: Chest EMPs cause a 3-6 second standing-up paralyze, visible to
the player by a quite noticeable shaking of their body.
balance: Head EMPs break the optical transponder circuits for 7.5-15
seconds, effectively giving the user nightmare goggles vision with green
instead of red as the only remaining color.
/:cl:

---
## [TheFinalEntity/TGC1e](https://github.com/TheFinalEntity/TGC1e)@[c2a956a01d...](https://github.com/TheFinalEntity/TGC1e/commit/c2a956a01d4b008759b9e267ce8c393b27033aba)
#### Thursday 2023-05-11 23:30:44 by TheFinalEntity

Added Edited BW05FFAP to Actors Folder

Edited the BW05FFAP.CRE file, i.e. (injured woman). 
Changes Made: Creature 'State' variable changed from 'Diseased' to 'Normal'. See description/results below or at my original post on Beamdog Forums: https://forums.beamdog.com/discussion/comment/1197241#Comment_1197241

REASON: 
Hello,
I have been playing in a modded BGEE multiplayer run with some friends and we were having some trouble with the injured woman not spawning and/or being removed immediately after being manually spawned with the console. I took the liberty of fixing the issue, which actually happened to be really easy. Checking the creature file of the injured woman (BW05FFAP.CRE) I noticed that her class levels were set to 9/1/1, her HP was 5/54 and her state was set to diseased. I changed her state to normal and spawned her again and she stayed in game. I was able to complete the dialog with her with no issues.

I then checked the GLOBAL variable for the quest advancement via console CLUAConsole:GetGlobal("BW05_TGC1","GLOBAL"). This variable value should be 5 prior to conversing with her and 6 afterward. This was the case when I tested it. I then loaded a previous save to ensure that she would spawn properly after the enemies were defeated in the area in which she spawns and she spawned and conversed properly. The GLOBAL variable was also updated properly yet again.

I believe the issue was that her con is 9 and her current HP was 5 and whatever disease she had was applying a con penalty to her and thus reducing her total HP by 1/level for 9/1/1 levels and thus bringing her to negative HP.  So when spawning her in the game with CurrentHP < 0 the game engine was statically removing her and since she wasn't reduced to 0 or less HP while spawned in game she didn't actually die and thus there would be no death animation/sound/text and no body left in game, since she was statically removed. I could be wrong, but this seems to be the case.

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[2b045340a7...](https://github.com/k21971/EvilHack/commit/2b045340a7a4072faadc2c62d3030c7c54374fdb)
#### Thursday 2023-05-11 23:34:24 by k21971

Fix: aura of darkness could snuff out/curse other sources of darkness; shadow dragon scales aura of darkness hurting light haters.

Quite a few fixes in this commit:

* player or monster casting an aura of darkness was putting out or
diminishing sources of darkness (cursed magic lamps, shadow dragon
scales/dragon-scaled armor, Drow wielding the Staff of the Archmagi)
* same effect could curse the same source if using artifact_light() to
give off darkness
* Drow wearing shadow dragon scales/dragon-scaled armor were hurt by the
initial aura of darkness they cast

And while I was here, I noticed that blessed scrolls of light were not
putting out cursed magic lamps, and would augment or even bless sources
of darkness that used artifact_light(). So that's been addressed too.

Thanks terrapin for the assist.

---
## [monglitch/Legit-GTA-money-generator](https://github.com/monglitch/Legit-GTA-money-generator)@[b6f11614f2...](https://github.com/monglitch/Legit-GTA-money-generator/commit/b6f11614f2b33c9c2a18893f26c4017b7ed3bd10)
#### Thursday 2023-05-11 23:37:08 by GTA 5 MONEY GENERATOR

Update README.md

GTA 5 Free Money Generator without human verification. Free GTA 5 Money Generator 2023 .Grand Theft Auto (GTA V) is an open world and an immersive world game that has been a successor of its previous releases. This game is an enjoyable game that can be played with multiplayer mode or single story mode. This game has real-life alike gameplay where the players can get enter shop, eat food, drive cars and even die. It’s fun when there is a lot of cops on your tail, and you have to make the escape. In these conditions, you have to spend your money on all the things that you do in this game, and there are some situations where you might not have enough money to get a new haircut or buy something from a shop. Under these conditions, you will be thinking about an easy way to generate money in GTA 5. Well, there is a shortcut from which you can get money without doing missions in the game. It’s GTA 5 Money hack. GTA 5 Money Generator The GTA 5 money generator is an online tool accessible

---
## [m00nyONE/HodorReflexes](https://github.com/m00nyONE/HodorReflexes)@[f94c8cdf96...](https://github.com/m00nyONE/HodorReflexes/commit/f94c8cdf963ada33211c553c91022d107376df0f)
#### Thursday 2023-05-11 23:46:00 by m00nyONE

remove build.ps1 . thank you windows zip CmdLet for destroying 2 build after another. i should have known better you fucking peace of shitsoftware! maybe use standard encodeing next time

---
## [jnutt367/parables](https://github.com/jnutt367/parables)@[9fec49aed0...](https://github.com/jnutt367/parables/commit/9fec49aed0572c68e1dc5de495d299c22342d3d1)
#### Thursday 2023-05-11 23:47:06 by Jason Nutt (He/Him) Christian Developer/Creator

Update index.js

To some who were confident of their own righteousness and looked down on everyone else, Jesus told this parable: “Two men went up to the temple to pray, one a Pharisee and the other a tax collector. The Pharisee stood by himself and prayed: ‘God, I thank you that I am not like other people—robbers, evildoers, adulterers—or even like this tax collector. I fast twice a week and give a tenth of all I get.’

“But the tax collector stood at a distance. He would not even look up to heaven, but beat his breast and said, ‘God, have mercy on me, a sinner.’

“I tell you that this man, rather than the other, went home justified before God. For all those who exalt themselves will be humbled, and those who humble themselves will be exalted.”

---

