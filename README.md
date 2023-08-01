## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-31](docs/good-messages/2023/2023-07-31.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,173,616 were push events containing 3,397,213 commit messages that amount to 282,534,436 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 66 messages:


## [Rustybuckets6601/tgstation](https://github.com/Rustybuckets6601/tgstation)@[41f20bc3ce...](https://github.com/Rustybuckets6601/tgstation/commit/41f20bc3ced4e7853a09f2d5e1dcf46346f2e51f)
#### Monday 2023-07-31 00:00:27 by LemonInTheDark

[MDB IGNORE] Angled Lights & Lighting Prototyping Tool  (#74365)

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

Co-authored-by: MMMiracles <lolaccount1@hotmail.com>

---
## [EvaEvaEvaEvaEva/Skyrat-tg](https://github.com/EvaEvaEvaEvaEva/Skyrat-tg)@[2f2ec4b9d6...](https://github.com/EvaEvaEvaEvaEva/Skyrat-tg/commit/2f2ec4b9d64c448e5b544ecbcdca42a7dae0f094)
#### Monday 2023-07-31 00:04:51 by SkyratBot

[MIRROR] There is no longer a 50% chance of catching a heretic out when examining them drawing influences [MDB IGNORE] (#22532)

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

## About The Pull Request

There is no longer a 50% chance of catching a heretic out when examining
them drawing influences.

## Why It's Good For The Game

> There is no longer a 50% chance of catching a heretic out when
examining them drawing influences

This is a bad thing for several reasons.

1. It means the heretic will most often be caught out at the very start
of the shift, when they are weakest and most vulnerable.
Heretics already have it hard enough, adding yet another source of
stress is undue.

2. It has no effective counter.
What are you going to do? Not draw any influences? That shouldn't be the
'counter'. The influence drawing period is meant to parallel the crew
prepping period, the traitor rep-collecting period, etc.

3. In a way, it's more blatant than Codex Cicatrix drawing.
Codexi show up as a normal item in your hand. This instead shows a huge
flashing glowing neon rainbow text that says THIS IS A HERETIC. SHRIEK
IN RADIO AND VALID.

4. It's badly designed, and can be manipulated way too easily to always
show.
Examine a target thrice and you're pretty much guaranteed to see if they
are indeed drawing or not. You can just keep rolling the 50% chance.

5. It feels random and unfair for the heretic to die to it.
I've seen this happen and it sucks. There's no sign for heretics that
they have a risk of being found out when examined, which means that this
is just an extremely rare occurrence that you try to ignore *could*
happen 99% of the time, and feel like shit the 1% of the time it
backfires.

## Changelog

:cl:
del: There is no longer a 50% chance of catching a heretic out when
examining them drawing influences.
/:cl:

* There is no longer a 50% chance of catching a heretic out when examining them drawing influences

---------

Co-authored-by: carlarctg <53100513+carlarctg@users.noreply.github.com>
Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [Bird-Lounge/Skyraptor-SS13](https://github.com/Bird-Lounge/Skyraptor-SS13)@[8e3dfc2af2...](https://github.com/Bird-Lounge/Skyraptor-SS13/commit/8e3dfc2af2f3ca87e9f07669033c1ec2a6102073)
#### Monday 2023-07-31 00:16:58 by GoldenAlpharex

Fixes bloody soles making jumpsuits that cover your feet bloody when you're wearing shoes (#77077)

## About The Pull Request
Title says it all.

It basically made it so wearing something like a kilt would result in
the kilt getting all bloody as soon as you walked over blood, even when
you were wearing shoes, unless you wore something else that obscured
shoes.

I debated with myself a lot over the implementation for this, I was
thinking of adding some way to obscure feet in particular, but it's
honestly so niche that it could only have caused more issues elsewhere
if I tried to fix this issue that way.

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[be9ed762c3...](https://github.com/treckstar/yolo-octo-hipster/commit/be9ed762c3ce033c6acf13ceffbae5e9e983ef8a)
#### Monday 2023-07-31 00:22:03 by treckstar

People listen up don't stand so close, I got somethin that you all should know. Holy matrimony is not for me, I'd rather die alone in misery.

---
## [Tsar-Salat/daedalusmock](https://github.com/Tsar-Salat/daedalusmock)@[9424eb53a1...](https://github.com/Tsar-Salat/daedalusmock/commit/9424eb53a1780ce0ff21629bba8e3288d26a9a63)
#### Monday 2023-07-31 00:37:37 by Kapu1178

Removes Field of View and returns everything to the GAME_PLANE (#209)

* Fuck you superlayers

* re-add the blindness effects

* Fix holosigns

---
## [nayDPz/Starstorm2](https://github.com/nayDPz/Starstorm2)@[a3d9f77b5d...](https://github.com/nayDPz/Starstorm2/commit/a3d9f77b5d22029299df458125f4acd276c43448)
#### Monday 2023-07-31 00:44:19 by swuff-star

oh boy

i am going to pull jace's branch and it is going to be fine and absolutely not fuck up my branch haha lets do this!

---
## [tgstation/TerraGov-Marine-Corps](https://github.com/tgstation/TerraGov-Marine-Corps)@[fb4899d20e...](https://github.com/tgstation/TerraGov-Marine-Corps/commit/fb4899d20e990a0a65b8cb5b0ad19b1ef9ab083e)
#### Monday 2023-07-31 00:44:36 by KM-Catman

Slight redesign of Valhalla Vendors and Chemistry. Adds FC and Synth to Valhalla. (#13612)

* Valhalla Fixes

Start room is now all Hulls, adds a Friend, Materializes the Chaplain's chained demon, and adds more Xeno Huds.

* FC and Synth Added. Slight readjustment.

* Changed the vendor section as per Grayson's request

* Adds three new Warning Stripes.

Adds a FCDR, Synth, and Mech warning stripe. Adds them in front of the prep rooms

* Duct Taped Space

* Removed random bedsheet (Goddamn you hotkeys)

---
## [nevimer/Bubberstation](https://github.com/nevimer/Bubberstation)@[621ef8a96e...](https://github.com/nevimer/Bubberstation/commit/621ef8a96e83ab3ba35591e5a146746fea916f63)
#### Monday 2023-07-31 00:44:42 by SkyratBot

[MIRROR] [NO GBP] Fixes clown car + deer collision  [MDB IGNORE] (#22709)

* [NO GBP] Fixes clown car + deer collision  (#77076)

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

* [NO GBP] Fixes clown car + deer collision

---------

Co-authored-by: Rhials <28870487+Rhials@users.noreply.github.com>

---
## [KheirFerrum/Cataclysm-BN](https://github.com/KheirFerrum/Cataclysm-BN)@[08d54d0287...](https://github.com/KheirFerrum/Cataclysm-BN/commit/08d54d0287a1313cb810a1d3d74ca0e531189ae1)
#### Monday 2023-07-31 00:49:38 by KheirFerrum

Fix MGOAL_FIND_ITEM_GROUP, fix up some code (#2546)

* Reorganize

Code still sucks. In particular recruit_class doesn't compare properly with npc->my_class so MGOAL_RECRUIT_NPC_CLASS fails horribly even if you fix up that area of code to it actually points to type->recruit_class instead of recruit_class

For that matter mission has a select copy of several mission type defs and I can only assume this is due to legacy fuckery.

* Fix mission.cpp

Now will only allow you to select items if you have enough of them, and will only consume the necessary amount.

Added documentation for MGOAL_FIND_ITEM_GROUP

Thank god this wasn't too much work.

---
## [sozud/sotn-decomp](https://github.com/sozud/sotn-decomp)@[b488191654...](https://github.com/sozud/sotn-decomp/commit/b488191654aef67226d141568be5104b78ea4ea7)
#### Monday 2023-07-31 01:03:46 by bismurphy

Decompile DRA func_800FE044 (#407)

This function is responsible for upgrading the player's stats. This is
called upon collection of a Life Max Up, Heart Max Up, or when killing
an enemy to get experience. This function gives experience to the player
and their active familiar.

HUGE thanks to @mkst for the maspsx update that allowed this one to
match!

The arguments to this function are a little unusual. arg0 is mostly used
as the amount to increase the heartMax, hpmax, or exp, but in the case
where we're getting a relic, is used as the relic ID. Similarly, arg1 is
mostly used to identify which of these traits is being increased, but in
the case where we're getting exp, is used to define the enemy's level to
determine how much exp to award. It seems odd that increasing each of
these stats is baked into this one function, instead of all being their
own functions.

This is one of the first functions I looked at when I joined the decomp
several months ago and it's very cool to have it finally working, now
using the extra knowledge I've picked up over that time.

---------

Co-authored-by: bismurphy <bismurphy@users.noreply.github.com>
Co-authored-by: Mark Street <streetster@gmail.com>

---
## [A-Noid33/mame](https://github.com/A-Noid33/mame)@[51743748ed...](https://github.com/A-Noid33/mame/commit/51743748ed897faf3d85a312be7877a4d723c6b8)
#### Monday 2023-07-31 01:23:51 by Bob Schultz

mac_flop_orig:
* Minor corrections to a few software list entries.

New working software list items (109 Dumps Added)
-------------------------------
mac_flop_clcracked: [4AM, san inc, A-Noid]

Alter Ego (male version 1.0) (san inc crack)
Alter Ego (version 1.1 female) (san inc crack)
Alternate Reality: The City (version 3.0) (san inc crack)
Animation Toolkit I: The Players (version 1.0) (4am crack)
Balance of Power (version 1.03) (san inc crack)
Borrowed Time (san inc crack)
Championship Star League Baseball (san inc crack)
Cutthroats (release 23 / 840809-C) (4am crack)
CX Base 500 (French, version 1.1) (san inc crack)
Deadline (release 27 / 831005-C) (4am crack)
Defender of the Crown (san inc crack)
Deluxe Music Construction Set (version 1.0) (san inc crack)
Déjà Vu (version 2.3) (4am crack)
Déjà Vu: A Nightmare Comes True!! (san inc crack)
Déjà Vu II: Lost in Las Vegas!! (san inc crack)
Dollars and Sense (version 1.3) (4am crack)
Downhill Racer (san inc crack)
Dragonworld (4am crack)
ExperLisp (version 1.0) (4am crack)
Forbidden Castle (san inc crack)
Fusillade (version 1.0) (san inc crack)
Geometry (version 1.1) (4am crack)
Habadex (version 1.1) (4am crack)
Hacker II (san inc crack)
Harrier Strike Mission (san inc crack)
Indiana Jones and the Revenge of the Ancients (san inc crack)
Infidel (release 22 / 840522-C) (4am crack)
Jam Session (version 1.0) (4am crack)
Legends of the Lost Realm I: The Gathering of Heroes (version 2.0) (4am crack)
Lode Runner (version 1.0) (4am crack)
Mac Pro Football (version 1.0) (san inc crack)
MacBackup (version 2.6) (4am crack)
MacCheckers and Reversi (4am crack)
MacCopy (version 1.1) (4am crack)
MacGammon! (version 1.0) (4am crack)
MacGolf (version 2.0) (4am crack)
MacWars (san inc crack)
Master Tracks Pro (version 1.10) (san inc crack)
Master Tracks Pro (version 2.00h) (san inc crack)
Master Tracks Pro (version 3.4a) (san inc crack)
Master Tracks Pro (version 4.0) (san inc crack)
Math Blaster (version 1.0) (4am crack)
Maze Survival (san inc crack)
Microsoft Excel (version 1.00) (san inc crack)
Microsoft File (version 1.04) (san inc crack)
Mindshadow (san inc crack)
Moriarty's Revenge (version 1.0) (san inc crack)
Moriarty's Revenge (version 1.03) (4am crack)
Mouse Stampede (version 1.00) (4am crack)
Murder by the Dozen (Thunder Mountain) (4am crack)
My Office (version 2.7) (4am crack)
One on One (san inc crack)
Orb Quest: Part I: The Search for Seven Wards (version 1.04) (san inc crack)
Patton Strikes Back (version 1.00) (san inc crack)
Patton vs. Rommel (version 1.05) (san inc crack)
Pensate (version 1.1) (4am crack)
PFS File and Report (version A.00) (4am crack)
Physics (version 1.0) (4am crack)
Physics (version 1.2) (4am crack)
Pinball Construction Set (version 2.5) (san inc crack)
Pipe Dream (version 1.2) (4am crack)
Professional Composer (version 2.3Mfx) (san inc crack)
Q-Sheet (version 1.0) (san inc crack)
Rambo: First Blood Part II (san inc crack)
Reader Rabbit (version 2.0) (4am crack)
Rogue (version 1.0) (san inc crack)
Seastalker (release 15 / 840522-C) (4am crack)
Seven Cities of Gold (san inc crack)
Shadowgate (san inc crack)
Shanghai (version 1.0) (san inc crack)
Shufflepuck Cafe (version 1.0) (4am crack)
Sierra Championship Boxing (4am crack)
SimCity (version 1.1) (4am crack)
SimCity (version 1.2, black & white) (4am crack)
SimEarth (version 1.0) (4am crack)
Skyfox (san inc crack)
Smash Hit Racquetball (version 1.01) (san inc crack)
SmoothTalker (version 1.0) (4am crack)
Speed Reader II (version 1.1) (4am crack)
Speller Bee (version 1.1) (4am crack)
Star Trek: The Kobayashi Alternative (version 1.0) (san inc crack)
Stratego (version 1.0) (4am crack)
Suspect (release 14 / 841005-C) (4am crack)
Tass Times in Tonetown (san inc crack)
Temple of Apshai Trilogy (version 1985-09-30) (san inc crack)
Temple of Apshai Trilogy (version 1985-10-08) (san inc crack)
The Chessmaster 2000 (version 1.02) (4am crack)
The Crimson Crown (san inc crack)
The Duel: Test Drive II (san inc crack)
The Hitchhiker's Guide to the Galaxy (release 47 / 840914-C) (4am crack)
The King of Chicago (san inc crack)
The Lüscher Profile (san inc crack)
The Mind Prober (version 1.0) (san inc crack)
The Mist (san inc crack)
The Quest (4am crack)
The Slide Show Magician (version 1.2) (4am crack)
The Surgeon (version 1.5) (san inc crack)
The Toy Shop (version 1.1) (san inc crack)
The Witness (release 22 / 840924-C) (4am crack)
ThinkTank 128 (version 1.000) (4am crack)
Uninvited (version 1.0) (san inc crack)
Uninvited (version 2.1D1) (san inc crack)
Where in Europe is Carmen Sandiego? (version 1.0) (4am crack)
Winter Games (version 1985-10-24) (san inc crack)
Winter Games (version 1985-10-31) (san inc crack)
Wishbringer (release 68 / 850501-D) (4am crack)
Wizardry: Proving Grounds of the Mad Overlord (version 1.10) (san inc crack)
Zork II (release 48 / 840904-C) (4am crack)
Zork III (release 17 / 840727-C) (4am crack)

---
## [psychonaut-station/PsychonautStation](https://github.com/psychonaut-station/PsychonautStation)@[7e1d97af9e...](https://github.com/psychonaut-station/PsychonautStation/commit/7e1d97af9e4b6b7f90fbacc754fae939b6d16e49)
#### Monday 2023-07-31 01:26:49 by Justice

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
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[1b315a616f...](https://github.com/ritorizo/Shiptest/commit/1b315a616ff24e3f1f92c791e4df4dc43ca9aad6)
#### Monday 2023-07-31 01:39:24 by Thedragmeme

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
## [LineageOS-jason/android_kernel_xiaomi_sdm660](https://github.com/LineageOS-jason/android_kernel_xiaomi_sdm660)@[0e5f807ba0...](https://github.com/LineageOS-jason/android_kernel_xiaomi_sdm660/commit/0e5f807ba0e9a44fc634b1dad072d83dccdbc7cd)
#### Monday 2023-07-31 01:48:29 by Christian Brauner

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

---
## [Coxswain-Navigator/lobotomy-corp13](https://github.com/Coxswain-Navigator/lobotomy-corp13)@[171b1478f9...](https://github.com/Coxswain-Navigator/lobotomy-corp13/commit/171b1478f9d01a40841ca0bb131394fe8a2039b2)
#### Monday 2023-07-31 02:04:23 by vampirebat74

Limbus Company E.G.O dump (#1062)

* Adds roseate desire

roseate sfx

datums

weapons

add aedd

sprite adjustments

unfucks suits

new sfx

name fix

aaaa

adds capote

adds sloshing

farmwatch

farmwatch suit

stuff

farmwatch stuff

capote inhands

red sheet finished

sloshing gift

linters

Stuff

stuff

fixes shit

stuff

weapon code cleanup

spicebush finished

removes the heal

code fix

stuff

removes reference

farmwatch hat

new vfx

requested changes

* block duration

---------

Co-authored-by: Mr.Heavenly <davidx3adamhunt@gmail.com>

---
## [lolman360/Citadel-Station-13-RP](https://github.com/lolman360/Citadel-Station-13-RP)@[4966352d14...](https://github.com/lolman360/Citadel-Station-13-RP/commit/4966352d145c9fcacad823f7dc8d6a52fc82c953)
#### Monday 2023-07-31 04:06:52 by Mazian

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
## [lolman360/Citadel-Station-13-RP](https://github.com/lolman360/Citadel-Station-13-RP)@[a14ef07eb6...](https://github.com/lolman360/Citadel-Station-13-RP/commit/a14ef07eb69a49feeae9c331609adc393f861b5b)
#### Monday 2023-07-31 04:06:52 by Nut2

Triumph central command floor fix (#5741)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
I MISSED TWO FUCKING TILES
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
I MISSED TWO TILES GOD DAMNIT
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

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---
## [2002jai/Graph-Database](https://github.com/2002jai/Graph-Database)@[704572c916...](https://github.com/2002jai/Graph-Database/commit/704572c9162d82d5786c9eb353a24900d3eef906)
#### Monday 2023-07-31 04:07:19 by jai chauhan

Graph Database

Welcome to our comprehensive repository, a one-stop destination to delve into the captivating world of graph databases. Whether you're a curious beginner or an experienced developer, this repository covers everything you need to know about graph databases.

Embark on a journey through the fundamental concepts of graph theory, understanding nodes, edges, graphs, and their properties. Discover various popular graph database management systems like Neo4j, Amazon Neptune, JanusGraph, and more, and grasp their strengths and use cases.

Learn how to model your data efficiently, create graph schemas, and leverage query languages like Cypher, Gremlin, and SPARQL to retrieve valuable information. Uncover the power of graph algorithms and their applications, from shortest path algorithms to community detection and centrality.

Explore real-world use cases, such as social networks, fraud detection, and knowledge graphs, witnessing the potential of graph databases in diverse fields. Integrate graph databases with your applications, data analytics, and machine learning projects to unlock valuable insights.

Get hands-on with administration, from installation to data import/export and performance tuning. Dive into advanced topics like distributed graph databases and graph embedding techniques to enhance your expertise.

With visualization tools, querying libraries, and community resources, this repository offers a dynamic learning experience. Join us, contribute, and stay up-to-date in this dynamic realm of graph databases. Empower your data management with the potential of graphs!

---
## [openbmc/openpower-vpd-parser](https://github.com/openbmc/openpower-vpd-parser)@[45d54976fd...](https://github.com/openbmc/openpower-vpd-parser/commit/45d54976fdb8d27a539d78dc1cd7e2db0998b43a)
#### Monday 2023-07-31 04:50:39 by jinuthomas

Catching File Exceptions in openpower-vpd-parser

In this commit, I have added code to handle file exceptions
more effectively. By implementing proper exception handling,
we can improve the robustness and reliability of the file
operations within our codebase.

Here are the key changes made in this commit:

  - Introduced a try-catch block around the file operation sections.
  - Within the try block, added code to perform the necessary file
    operations.
  - Implemented catch blocks to handle specific file exceptions.
  - In each catch block, included appropriate error handling logic,
    such as logging the error message or displaying a user-friendly
    error message.
  - Ensured that the catch blocks gracefully handle the exceptions
    and prevent the program from crashing or behaving unexpectedly.

By adding this exception handling code, we can anticipate and handle
potential file-related errors gracefully, providing a smoother
experience for users and preventing any unexpected crashes or data
loss. This would also aid in debugging issues.

Change-Id: I621a7f0ba68d2c298e4fea0a9d3e21d1939cd090
Signed-off-by: jinuthomas <jinu.joy.thomas@in.ibm.com>

---
## [re621/dnpcache](https://github.com/re621/dnpcache)@[60986c0cde...](https://github.com/re621/dnpcache/commit/60986c0cde71361ef80a579df8ee7edc2bedb23d)
#### Monday 2023-07-31 05:27:07 by bitWolfy

Remove 1155 artists from the DNP list.

Removed: coral_luna, mdwines, soakedbikini, pantyranger, diffusedlizard, kazz_a_fella, alkyuz, werewhusky, skooma_whore, october_nights, pehkeshi, scalywanderer, linndrim, hexamanta, anarietta, earthsong9405, captaincassidy, anthonynothere, gayluigisex, yuudai, pettypalps, cosmick9, myemetophobia, digitalpopsicle, splatterpop, poppin, tempobun, zaaruchan, superratbike64, svarzye, cyberwuff, worldoffizz, zeiroslion, emptyset, siplick, sourisdedog, wicketrin, tykepuparts, kubikoza, hiraume42, delinquentfreak, saerixdurr, tejedora713joker, andrew.thy.accursed, cytoholix, northbeastart, hellazest, infinitixen, p0ssmn, isofrieze, venomstench, pocketpaws, tf4me, centuriguil, raithvaneal, dahsharky, trashgaylie, mrpanghu, feyaarts, wolfbane154, derpyrider, rodicle, shiru_fox, toonyrobot, sleepylopunny, mimisrol, selidevilfeather, shido-tara, ineedanaccount, reizu47, sherilane, hellfurred, zeplich, darkeshi, amadeen, lowestpolygon, alradeck, asuka_kurehito, waynekan, lhacedor, dativyrose, digitallis, nosylvsforwork, lacrimale, kaitzuwu, ihoundr, elranno, doublepopsicle, gaturo, aquariusfox, mpcx, kattalu, lintu, goobysart, lemonlycan, dylbun, fxscreamer, nt6969, lewdliege, reallyhighriolu, melbaka, saint_lum, kivaaa66, kivalewds, kazoko_(artist), barachaser, shadowthelastalpha, teke, crittermatic, ribboncable, domasarts, ursine-major-ike, browneyedsaiyangirl, uncensoredhugs, skydiggitydive, takarachan, feelin_synful, ilovecosmo, biffbish, pulp_(artist), doxhun, cupsofjade, nicesweater, bluecat_friend, masuku, lunarfloral, kugi, sagejwood, sqrlyjack, maiteik, leozedi, popdroppy, mikakater, 413k_zzzz, puppyemonade, xanthewolf, joooji, nasusbot, shredded_wheat, dogsdontwipe, wonderwaffle93, gogoandyrobo, jezzlen, dourdoofus, vksuika, klotzzilla, cooperdooper, shadnaotomi, nudegote, sexygoatgod, humgeronimo, ladysophia, mrwhiskerz, cocicka, d-wop, charmerpie, yourdigimongirl, elvche, booponies, lulubelluleart, infinitedelusion, tankakuka, mensies, trunchbull, evian, sodasquids, telelewdz, lawlzy, tonio_(artist), xankragoc, horrificrabbits, sinfulgoatz, whippytail, malachimoet, catniplewds, cocaine_(artist), marshy_swtr, goldelope, chokodonkey, notkastar, sinnerscasino, sentharn, tealie, freaks, angellsview3, arwenscoots, royalzbed, byrth, hexuru, devildjmachine, malerouille, donovallo, psychoninetales, vahldem_sol, nyanyakotarou, zyegnar, akytti, sootylion, kiva~, calmnivore, nexcoyotlgt, smoothsharb, sub-rosa, brismy, woodpeckertoons, xeshaire, suirano, mr_otter_breath, bassybefuddle, verdantphysician, skullwomb, steak_in_the_daylight, kittydogcrystal, aggrobadger, orbstuffed, fraichetaso, loonyleandra, bunsawce, schl4fmuetze, renkindle, psychovixen, bkmat55, fricken_stoat, w00my, haven_(artist), gipbandit, loki_the_vulpix, erobos, bunchantress, uniquesoul1600, hirowithart, mikaemikae, ratbloke, pastellprinz, racktor, coillte, kazuk9, acidneko, josh_gong, yiyani, grayish, moblo, naoma-hiru, molish, sheyesh, st0pme, cawkbox, unclesam1776, fennecfuchs, inkpuni, pico_(artist), ruugiaruu, wispyparadox, funkybun, lewdoreocat, dogseesghosts, fauwcks, randy_entinger, trex_b6, yui-hii, runaris, rainbowpillars, ragonox, luxuria-sins, maxisb8, hiccyart, fancyfez, mesoplush, gammelgaedda, yi_feng, scpkid, goetiagoat, mabit, dischimera, dr.bubblebum, drakeraynier, rml, amawdz, mc_arts, freemau, armomen, orionfell, luriostragedy, dradmon, jesterghastly, gothgator, talentlesshack, foxryk, supertrashparty, marrowsoup, roserivy, vanzard, deepfriedlemons, torotheking, harewithoutahat, lucciola, mr.lemur, lemonkyubun, cubble_chubb, arrjaysketch, pinklilim, jingo824, consciousafterdark, anti-cupid, phosaggro, dashboom, giftheck, birdrabbit, desertmotels, lv99perv, stellarfalcon, tasaeyeang, knotty, rockfall, aogirinaru, hikebu, pawpadcomrade, frengers, rikkitz, vappypaws, nukeleer, adevio, gummuru, sattytsukumo, bittenbats, whygena, ruzeb, jads_l_rutan, gattonero2001, shawoo, francis_xie, angeltf, veevobyte, darkfool., huwon, tsukikibaokami, covepalms, nikunabe1989, emifern, pero3, tricksta, inkbeastart, grinn3r, holidaydipstick, odonata-nymph, binxxy_(artist), zazush-una, sodo_ad, loonanudes, kodardragon, flameydragwasp, ablimpfox, bakvissie, eccstasy, esealia, tailsrulz, dexxa, spiritto, vonepitaph, eddy-boy, saiyangoku4, gatomonlover, moonlit-comet, thehenwithatie, brienoir, tegucreative, wanisuke, pxlfur, anomyna, motsutambo, fepon, cyrogenic, fursuitchina, slates1n, depthsofthedrex, furrybob, davelievski, spacemaverick, fluff-kevlar, evenytron, 0eff0rt, gayclub, goatypie, nikoyishi, alishka, makeinu, jfetspeaks, cowbun, wyrwulf, thespiderbunny, fluffx, dragons-and-drawings, jcosneverexisted, scoty_doodlerz, makinglemonade, ceramic_(artist), selirum, euskuuy, tsunkat, lustbubbles, appleseid, lewdtant, werewuffstuffer, odontoceti, iaido, turboranger_(artist), saca44, mr.shigglesworth, pyriax, raijikaruart, fox-pop, sirblythe_(artist), pastelarcadiaad, etherealarcadia, dracoarcadia, benjibat, sarvak, amethystbeetle, fnook_(artist), stationarrow, maim, rashkah, psy101, disappointedf0x, pointedfox, bundog, tailgrip, scalesforlife, hayleymulch, saphe, kiweevil, madakan, rainiing, bitelickart, done0008, alec8ter, tentativelytoon, mikurulucky, killveous, fishhound, misshammer, yakushishi, pieraite, knives4cats, jalmu, quin-nsfw, zooptoon, ebonychimera, beaglebabe1, filthy-d, l-tech-e-coyote-l, anomalae, rakket, mcdutt, alcor90, sodongs, catcock, blickfen, akiiokai, possumkiddo, inkplasm, doubledeal_(artist), fuzzlesuits, chetchaka, raaazzledazzle, razferret, razbuckner, ikitsunyan, kclt, draco_(artist), gunther_silves, kkitten, singafurian, zandybutt, comfytail, crazyassbeethoven, dogburger, adalee, alirrasarts, blackmagemathos, leonois, solidpoint, cloudpie, rottenscoundrel, wings-and-strings, tomcoletti, pikajota, squeakcore, doubleclawed, ebonyplume, myznyx, zackary911, xepher777, aimee-lesley-sim, spottedsqueak, fuhrawr, isaac_baranoff, starnina15, zestylemonss, meirdent, babymee, explicital, slyvern, karpet-shark, booghetti, zypter, adaptagx, opiodae, kiwipotato, murkbone, jonas, exed_eyes, shuryashish, mangobird, kurogi_fox_siv, snuddy, grimdank, nighteternal2469, dacad, superhypersonic2000_(artist), drako1997, verenpunainen_kuningatar, gurophilia, furrever, rdroid, smolrainbowgoat, ratte, urban-coyote, soulsplosion, cyaeon, elliotte-draws, whisperingfornothing, griz_urso, lepronasty, tears_of_soy, bunnielovesyou, paliken, spaceysoda, david_frangioso, cattinypaws, bobdude0, sincerity_gender, anima-virtuosa, turnipberry, asbel_lhant, klaide, rishi-chan, kircai, otto0ttsy, vaktus, beezlebumawoken, transdonaldduck, questly, pinkkatfox, goopomancer, xoel, allbadbadgers, sugarlesspaints, imafutureguitarhero, eiko_tsukida, tarot_(artist), pinuh, diero, dilarus, dfer32, mxwqtkl, electrycpynk, insomniacovrlrd, cewljoke, craziestrobo, anthrus1127, sunflowerbun, coyoteofthesands, masonparker, dottii, livesinabag, flam, toastedbiscuits, skycladfox, orenjisalmonpaw, nasty-fox, canadian_roses, crez, glorpofruithag, i_am_clover, johawk, lycosa, wizardlywalrusking, burgerkiss, kielseki, whisperfoot, oksara, olly, fetchmonkey, rottingichor, heathenfang, bikomation, phox_(artist), acedetrap, hedonisticvows, deersun, skittleytwix, jinxit, jtp-remart, cocaine-leopard, amarl_krieger, nakoo, leoian_(artist), amyth, nogu-art, bluhcat, vulpes_helios, licos, taurika, papilrux, pophopper, ebnet, apis_(artist), glenthefossa, raitime, sashabelle, puddingpaw, mercurial64, elricmysteryshifter, puptaire, anojaa, candychameleon, spice5400, nickshutter, rem, reiishn, sandybuny, 1oi, crunchobar, dante_yun, pherion, saintxd, rawbelr, mithaa, asmartist, pannekoeke, jotun22, iguky-neky, ahnik, thatvondude, kelevtov., fishwrappe, animal_shapes, oouna, princess_rei, blitzdrachin, jesterdk, watermelon_(artist), amara_lemur, lady_kurai, giantmilkdud, nostars, koili, abananaman, heddy, slobstash, terian, teranen, nexii, parabellux, tom_fischbach, reddacted, tojo_the_thief, proximiter, mmuted, irootie, icyshibe, quetzalcoatl_(artist), lamm, shayshay~, hettie, chutzpaah, jacob_lhh3, draekos, fatdingleberry_(artist), nooplip, pandasayori, numberxxxvi, bc92, silvixen, jungabeast, phoenixazrael, krazykurt, tape_(artist), iipaw, volvokun, hamstergirlthehamster, fallen_(artist), morkovjpn, wolfirry, slimedrops, rubisdrake, shortconcepts, ahdadah, chubbuppy, dreadcaptain, duckdraw, mehndix, pomander, wolfcha, evillabrat, henzolin, loupgarou, empa, diokhan, kpsketches, raysofsunshine, slash0x, kriticalerror, gallivant_crow, nyaroma, caindra, petit-bambi, thatblackcopfromdawnofthedead, dreamertooth, tofu93, ragnarokdragon, saucy, kidakins, kippy, swizzlestix, brilyeon, caste_(artist), tsukaui, saebira, ozzybae, boo-rad13y, sammythetanuki, vuurren, sinistervibe, rem289, shroompunk, samkin, cieldoberman, g0966, crazedg, gaoru, lpawz, enjoipandas, renthedragon, emeritus_terciel, xouual, tehcutepyro, anon232, grimmgrey, counterserum, knottykitten, crybleat, octopoodle, ker0ker0_(artist), xnirox, necrosquelch, ivenvorry, pkuai, mikefur, mattsykun, lilithveritas, bloodhound_omega, ogaraorcynder, rhos, kehei, aw0, apes, nyhgault, qualzar, licentuouslamb, reggaecyp, cynderplayer, vilegrim, redacteur, jimbohusky, pulsar, growlybeast, coreytwc_(artist), naoki_wolf, iceagechippies, alfierubuncle, cbee, acidic, louiefurrywolfy, bweezy, koriaris, tacoyaki, fullheroo, limlam, harmoniousrain, zotnamotgrim, xx_g.u.n_xx, carm, lustylamb, dragonvortex, crowchild, dragoneer, lumi_(artist), phi, lexathefox, tanookicatoon, thunper, korram, redwolfofwind, ipipo, teckworks, abobarseem, doopcity, xepheriah, diablo_en_musica_92, doncoon_(artist), digitaldomain123, belayalapa, delkon, connisaur, rohly, vcr-wolfe, steve_gallacci, hologram_(artist), irene_(artist), piumartiglio, sumat, kingofmaggots, oha, featheredclaw, snuddi, mentalo, ourflatcoat, da-fuze, herr_aardy, discoverychannel, azorart, nemomein, latex_(artist), afterdarkie, 7mii, draco_fenris, blown-ego, sissyskunk_(artist), chucktheskunk_(artist), oakspirit, brokenlynx21, nickswift, butter_bat, ben_hickling, bluehunter, soyuz, sorimori, blackbearcj, ficus, crimes, eifie, soundwavepie, besonik, greyskee, alekksandar, bluetigress, nereza, kalvince, thelabtwins, the_lynox, galaxyoron, moondevourer, evov1, enjambre, seph_ebonblade, prototypebasilisk, accell, myakoda, merenhor, muramuri, derfuhrer, moltengoldart, cchipppo, tetrapoda, omochi_(inkbunny), popsmasterson, nikinazu, raevee, wyntersun, ribboners, c4camel, shysketch, deishido, arconos, melvismd, taihab, cobalt_snow, flak_wizard, paddington_and_company_limited, dangerdoberman, inprogresspokemon, whitemantis, naexus, datsexylemur, polywomple, marilimmy, ryan_rabbat, krimrath, yoshitura, maplecookies, aurelleaheverfree, puppercase, spino, palcomix, bbmbbf, lilithofglace, frisket17, myloveless, grau_(artist), aduleon, sexbad, mearcu, murcifer, citrusdicks, hessonite, sokalo, kittehmei, puccaruu, yuurikin, kurikia, the_cherret_awaits, rapps, maxtwenty, bigbrownorc, santanni, twistedtemptation, nikita-the-stag, liz_art, camcartoonfanatic, singlerider4, beanbat, forge_(artist), hoshime, yamamoto, eviljake2, oriole_(artist), inkblooded, alefwdog, herisheft, disparitybit, samagthrav2, battle_franky, taesolieroy, wolftacos, anixis, spazzticglitch, pirun, swampstomper, morbi, mittsies, blondevelvet, kadath, danza, shinxiolu, littlefreckles, grumpyvulpix, xopachi, gonenannurs, floravola, heartcollar, metz, ranard_lightningfall, frots, curtsibling, vilani, inkydemon, sprinkle-butt, airguitar, anhes, jace_(artist), kaji_(artist), nimrais_(artist), kyoushiro, venerit, lunaselenewolfe, tsareia, violentanxiety, kk-furryworks, cobalta, mickeyila, akuva, rairai, backlash91, sanae, fishbones_(artist), itoril, littlemiu, zeara, darkrokkuman_(artist), peony, helical, donro, agalamt, inanna-nakano, aniutqa, kraest, audiovideomeow, silverbobcat, erithacuscreations, mattartist25, yasminachan, jagzcat, ohmuu, roum, sefeiren, sesameseedbun, noben, aquatheohiokitty, mewyfox, ilgrigio, leoian, vixendra, van_weasel, keihound, zoey03, hardblush, jay_naylor, frisky_ferals, slipshine, rubyrebirth, oze, neogeen, omegaltd, themadcatter, kamicheetah, ookamithewolf1, rabbit_valley, purplekecleon, ollieosa, jayfiregrowlithe, ensayne, bazaarbobby, scappo, dogsoul, poonani, paddercat, eltonpot, ebonyleopard, strype, cbh, mithril07, bicdente, unpeeledwasp, versiris, pitkin, mikachu_tuhonen, lilhoneypup, ladyshinwa, bad-collie, buizilla, foxxian, inert-ren, okamiterasu, mrawl, sammy_stowes, jameless, jooshster, lemoncore, xainy, strider-orion, silitha, spacepoptart, myuinhiding, sweetpinkpetals, sephygoth, edensky, ka, cigarscigarettes, tani_da_real, leatherruffian, hahul, cheezyweapon, reizakirga, leefuu, tanyafoxy, peyo, sweatshirt_(artist), adiago, timelesserror, jollyjack, kahmari, madhattermonster, omnoproxyl337, greykitty, thekitty, mattaku_shinzu, fortuna, fallenarts, ammako, sciggles, atlasfield, sheepdust, lumaberry, tktktk, uzai, aku_tojyo, sixthleafclover, gardelius, squeedgemonster, max-dragon, baka_sukonku, ferniio, jennadelle, ixerin, jaleo, luvythicus, tatious, nekomata_neko, zody, binky, sidian, kii-kitsune, kiirei, spookeedoo, angel27, msrah_(artist), nazuu-m0nster, lunacatta, kululu-xiao, kipcha, fluffball, reptilecynrik, redadillio, zerwolf, kylontario, liz_day, nightweaver, egophiliac, doffa, dipper, kefkafloyd, melo666, sonicdash, sugarpoultry, olven, theramjing, softpaw, xiraco, unicornspirit, tinintri, thornwolf, thaily, tamen, sharue, shadowsani, rikutida, paolo, kriscrash, kaemantis, frogsbreath, tailheat, sexyfur, jeremy_bernal

---
## [cyfinfaza/sc4hfair-sveltekit](https://github.com/cyfinfaza/sc4hfair-sveltekit)@[bfbc61faae...](https://github.com/cyfinfaza/sc4hfair-sveltekit/commit/bfbc61faaec346294da64000d02fa86e4a442b45)
#### Monday 2023-07-31 05:38:09 by Calum Dingwall

schedule data entry

i am up in the middle of the night again doing contentful data entry stuff. i have a cursed google sheet that parses yucky times into iso timestamps. and then a lookup table to turn every single way that 4h wants to write the same place into our slugs. and then i wresteled contentful to let me import my 208 events. and i forgot to turn off the webhook while importing those 200 events in a second so sorry vercel (429 lol). "why?" someone asked me. well because i am. yeah. anyways this is a git commit goodnight zzzzz

---
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[9c79c3af49...](https://github.com/morrowwolf/cmss13/commit/9c79c3af49ba90e18f85c1624ba4e80d608debf2)
#### Monday 2023-07-31 05:42:38 by spartanbobby

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
## [morrowwolf/cmss13](https://github.com/morrowwolf/cmss13)@[ce09b07afd...](https://github.com/morrowwolf/cmss13/commit/ce09b07afd0f8d433ffee1a43bc4dfeb978f45f1)
#### Monday 2023-07-31 05:42:38 by ihatethisengine

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
## [Aristoddle/marvin](https://github.com/Aristoddle/marvin)@[2c4ebf7c88...](https://github.com/Aristoddle/marvin/commit/2c4ebf7c884b667c0e5dd62949bc858a4c157dfb)
#### Monday 2023-07-31 06:35:38 by Joe Lanzone

aider: Extend WebSearchAgent to enhance functionality for classifying a user query, searching the web, scraping results, synthesizing and comparing them with the query, and looping until an answer is found or the user stops the process.

# Aider chat conversation:

USER: Hi, can you recall the work we were doing in our last session?

ASSISTANT: I'm sorry, but as an AI, I don't have the ability to recall past interactions. I don't have access to personal data about individuals unless it has been shared with me in the course of our conversation. I am designed to respect user privacy and confidentiality. Could you please provide more details or context about the work you're referring to?

USER: can you review `action_based_spec.md`, alongside the `cookbook/apps/web_search_agent.py`, `cookbook/apps/agent.py`, and any other files or snippets that might be relevant to the suggested workflow of defining/creating an agent that willl classify whether a query might be enriched via web search and scraping, and, if so, which will attempt to search the web, scrape results, synthesize those results, compare those reqults with the given user query, and, as relevant, which will either loop again, digging back into web search and scraping in pursuit of knowledge (with the ability for the user to kill the loop --> perhaps having a listener running while things loop until proper data is found) until an answer is found?

ASSISTANT: Sure, I can help with that. Let's start by reviewing the files you mentioned.

1. `action_based_spec.md`: This file provides an overview of the main components of the Marvin platform, their implementation, top-level use, and developer utility. It describes the AIModel, ai_classifier, AIApplication, and AIFunction components.

2. `cookbook/apps/web_search_agent.py`: This file defines a WebSearchAgent class that inherits from the AIApplication class. The WebSearchAgent class has methods for classifying a query, searching the web, parsing the results, evaluating the results, and responding or searching again.

3. `cookbook/apps/agent.py`: This file defines a generic Agent class that also inherits from the AIApplication class. The Agent class has methods for processing input and generating output.

Based on these files, here's a suggested workflow for creating an agent that can classify a query, search the web, scrape results, synthesize those results, compare them with the user query, and loop until an answer is found or the user stops the process:

1. Define a new AIApplication class that inherits from the Agent class in `cookbook/apps/agent.py`. This new class will be your custom agent.

2. In your custom agent class, define a method for classifying a query. You can use the `ai_classifier` decorator and the QueryType enum class from `cookbook/apps/web_search_agent.py` as a reference.

3. Define a method for searching the web. You can use the DuckDuckGoSearch tool from `cookbook/apps/web_search_agent.py` as a reference.

4. Define a method for scraping and parsing the search results. You can use the GitHubRepo and APIDoc models from `cookbook/apps/web_search_agent.py` as a reference.

5. Define a method for synthesizing the parsed results. This method should take the parsed results and combine them into a coherent answer.

6. Define a method for comparing the synthesized answer with the user query. This method should determine whether the synthesized answer is relevant to the user query.

7. Define a method for looping the search, scrape, synthesize, and compare process until an answer is found or the user stops the process. This method should call the other methods in a loop and have a mechanism for stopping the loop based on user input.

8. Finally, define a method for responding to the user. This method should take the final answer and present it to the user in a user-friendly format.

Please note that this is a high-level workflow and the actual implementation will depend on the specific requirements of your project. If you need help with the implementation, please provide more details about your project and I'll be happy to assist you further.

USER: Why would you recommed this be done, instead of simply extending/iterating on the web_search_agent ?

ASSISTANT: You're correct, and I apologize for any confusion. Extending or iterating on the existing `WebSearchAgent` would indeed be a more efficient approach, given that it already contains methods that closely align with your requirements.

The `WebSearchAgent` already has methods for classifying a query, searching the web, parsing results, and responding. You can extend this class and add additional methods or modify existing ones to suit your specific needs.

Here's a more refined approach:

1. Extend the `WebSearchAgent` class in `cookbook/apps/web_search_agent.py`. This new class will be your custom agent.

2. Modify the `classify_query` method if needed, to suit your specific classification requirements.

3. Modify the `search_web` method if needed, to suit your specific web search requirements.

4. Modify the `parse_results` method to scrape and parse the search results as per your needs.

5. Add a new method for synthesizing the parsed results. This method should take the parsed results and combine them into a coherent answer.

6. Add a new method for comparing the synthesized answer with the user query. This method should determine whether the synthesized answer is relevant to the user query.

7. Modify the `respond_or_search_again` method to loop the search, scrape, synthesize, and compare process until an answer is found or the user stops the process. This method should call the other methods in a loop and have a mechanism for stopping the loop based on user input.

8. Finally, modify the `respond_or_search_again` method to respond to the user with the final answer in a user-friendly format.

This approach leverages the existing functionality of the `WebSearchAgent` and allows you to add or modify methods as per your specific requirements.

USER: Could you write to a new markdown file a top-level (but granular, step-by-step) task-list of the edits and cross-file dependencies that would be required/leveraged to achieve this task, alongside a top level task description, with an empty section for tracking progress, under a file current_project.md?  I would love to use this, and iterate with you (with this as a tracking file) as we work to enable/allow this functionality.  Sometimes you crash and lose context, so I'd love to instantiate a current_project.md file that we might reference and update as we work.  Even the context of this message (why does the current_project.md file exist, etc), might be relevant to include.  Once that is written, I'd love for you to role-play the scenario in which you are me, the end-user collaborating with you to implement this functionality, and you are a fresh instance of you, a GPT4-32k agent that will need to be warmed up to understand the task at hand, and then which will need to collaborate with the synthetic version of me to update/write out these files, and maintain context across multiple sessions using this markdown tracking file.

ASSISTANT: Sure, I can help with that. Here's a top-level task list for the `current_project.md` file:

<source>markdown
current_project.md
<<<<<<< ORIGINAL

=======
# Current Project: Enhancing WebSearchAgent

## Task Description
The goal of this project is to enhance the existing `WebSearchAgent` in the Marvin platform to classify a user query, search the web, scrape results, synthesize those results, compare them with the user query, and loop until an answer is found or the user stops the process.

## Task List
1. Extend the `WebSearchAgent` class in `cookbook/apps/web_search_agent.py` to create a custom agent.
2. Modify the `classify_query` method in the custom agent to suit specific classification requirements.
3. Modify the `search_web` method in the custom agent to suit specific web search requirements.
4. Modify the `parse_results` method in the custom agent to scrape and parse the search results as per specific needs.
5. Add a new method in the custom agent for synthesizing the parsed results into a coherent answer.
6. Add a new method in the custom agent for comparing the synthesized answer with the user query.
7. Modify the `respond_or_search_again` method in the custom agent to loop the search, scrape, synthesize, and compare process until an answer is found or the user stops the process.
8. Modify the `respond_or_search_again` method in the custom agent to respond to the user with the final answer in a user-friendly format.

## Cross-File Dependencies
- `cookbook/apps/web_search_agent.py`: This file contains the `WebSearchAgent` class that will be extended to create the custom agent.
- `cookbook/apps/agent.py`: This file contains the `Agent` class that the `WebSearchAgent` class inherits from. It may need to be referenced for understanding the base functionality.

## Progress Tracking
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3
- [ ] Task 4
- [ ] Task 5
- [ ] Task 6
- [ ] Task 7
- [ ] Task 8

## Context
This `current_project.md` file was created to track the progress of the project and maintain context across multiple sessions with the GPT4-32k agent. The agent sometimes crashes and loses context, so this file will be used to reference and update the project status as work continues.
>>>>>>> UPDATED
</source>

Now, let's role-play the scenario you described. As a fresh instance of the GPT4-32k agent, I would start by reading the `current_project.md` file to understand the task at hand. I would then collaborate with the synthetic version of you to update/write out these files, and maintain context across multiple sessions using this markdown tracking file.

During each session, I would update the `current_project.md` file to reflect the progress made, and at the end of each session, I would summarize the work done and the next steps to be taken. This way, even if I crash and lose context, you can simply refer to the `current_project.md` file to understand the current status of the project and the tasks that need to be done.

---
## [Aristoddle/marvin](https://github.com/Aristoddle/marvin)@[73d817f569...](https://github.com/Aristoddle/marvin/commit/73d817f56942508afed81fa5ad1994e8271a5dac)
#### Monday 2023-07-31 06:35:38 by Joe Lanzone

aider: Completed the first task by extending the `WebSearchAgent` class to create a custom agent.

# Aider chat conversation:

USER: c

ASSISTANT: I'm sorry, but your request is not clear. Could you please provide more details or context?

USER: Please continue the simulation

ASSISTANT: Sure, let's continue the simulation.

As a fresh instance of the GPT4-32k agent, I would start by reviewing the `current_project.md` file to understand the current status of the project.

Based on the task list and progress tracking in the `current_project.md` file, it appears that none of the tasks have been completed yet. The first task is to extend the `WebSearchAgent` class in `cookbook/apps/web_search_agent.py` to create a custom agent.

Let's start with this task.

To extend the `WebSearchAgent` class, we need to create a new class that inherits from `WebSearchAgent`. We can call this new class `CustomWebSearchAgent`.

Here is the proposed change to the `cookbook/apps/web_search_agent.py` file:

<source>python
cookbook/apps/web_search_agent.py
<<<<<<< ORIGINAL
class WebSearchAgent(AIApplication):
    description: str = "A web search agent that uses DuckDuckGo"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_tool = DuckDuckGoSearch()
=======
class CustomWebSearchAgent(WebSearchAgent):
    description: str = "A custom web search agent"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # We can add any additional initialization here
>>>>>>> UPDATED
</source>

This change creates a new `CustomWebSearchAgent` class that inherits from `WebSearchAgent`. The `__init__` method of `CustomWebSearchAgent` calls the `__init__` method of `WebSearchAgent` to ensure that the base class is properly initialized.

Please review this change and let me know if it is correct. If it is, I will mark the first task as completed in the `current_project.md` file.

USER: InvalidEditBlock: edit failed!

cookbook/apps/web_search_agent.py does not contain the *exact sequence* of ORIGINAL lines you specified.
Try again.
DO NOT skip blank lines, comments, docstrings, etc!
The ORIGINAL block needs to be EXACTLY the same as the lines in cookbook/apps/web_search_agent.py with nothing missing!

cookbook/apps/web_search_agent.py does not contain these 6 exact lines in a row:
```
class WebSearchAgent(AIApplication):
    description: str = "A web search agent that uses DuckDuckGo"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search_tool = DuckDuckGoSearch()
```

ASSISTANT: I apologize for the confusion. Let's correct the edit block.

First, I need to see the exact current content of the `cookbook/apps/web_search_agent.py` file to propose the correct changes. Could you please provide the current content of the `cookbook/apps/web_search_agent.py` file?

USER: cat `cookbook/apps/web_search_agent.py`

ASSISTANT: I'm sorry for the confusion, but as an AI, I don't have the ability to execute shell commands or access files directly. Could you please copy and paste the content of the `cookbook/apps/web_search_agent.py` file here?

USER: I ran this command:

 cat `cookbook/apps/web_search_agent.py`

And got this output:

cat: `cookbook/apps/web_search_agent.py`: No such file or directory

ASSISTANT: I see, it appears there might be a misunderstanding. As an AI, I don't have direct access to your local file system to read the file. However, you can copy and paste the content of the `cookbook/apps/web_search_agent.py` file here in the chat. If the file does not exist, we can create it together. Please let me know how you would like to proceed.

USER: I ran this command:

 cat cookbook/apps/web_search_agent.py

And got this output:

from marvin import AIApplication
from marvin.tools.web import DuckDuckGoSearch
from src.marvin.components.ai_classifier import ai_classifier
from src.marvin.components.ai_model import AIModel, GitHubRepo, APIDoc
from enum import Enum

@ai_classifier
class QueryType(Enum):
    FACTUAL_INFORMATION = 1
    LATEST_NEWS = 2
    # Add more query types as needed

class CustomWebSearchAgent(WebSearchAgent):
    description: str = "A custom web search agent"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # We can add any additional initialization here

    def classify_query(self, query):
        # Classify the query using the QueryType classifier
        query_type = self.query_classifier(query)
        return query_type

    def search_web(self, query):
        # Search the web using the DuckDuckGoSearch tool
        search_results = self.search_tool.run(query)
        return search_results

    def parse_results(self, results):
        # Parse the search results using the GitHubRepo and APIDoc models
        # This is a placeholder and should be replaced with actual parsing logic
        parsed_results = results
        return parsed_results

    def evaluate_results(self, parsed_results):
        # Evaluate the relevance of the parsed results using a classifier
        # This is a placeholder and should be replaced with actual evaluation logic
        evaluated_results = parsed_results
        return evaluated_results

    def respond_or_search_again(self, evaluated_results):
        # Respond to the user's query or continue the search based on the evaluated results
        # This is a placeholder and should be replaced with actual response logic
        response = evaluated_results
        return response

__all__ = ["WebSearchAgent"]

ASSISTANT: Thank you for providing the content of the `cookbook/apps/web_search_agent.py` file.

It appears that the `CustomWebSearchAgent` class has already been created and it extends the `WebSearchAgent` class. This means that the first task in the `current_project.md` file has already been completed.

Let's update the `current_project.md` file to reflect this:

<source>markdown
current_project.md
<<<<<<< ORIGINAL
## Progress Tracking
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3
- [ ] Task 4
- [ ] Task 5
- [ ] Task 6
- [ ] Task 7
- [ ] Task 8
=======
## Progress Tracking
- [x] Task 1: Extend the `WebSearchAgent` class in `cookbook/apps/web_search_agent.py` to create a custom agent.
- [ ] Task 2: Modify the `classify_query` method in the custom agent to suit specific classification requirements.
- [ ] Task 3: Modify the `search_web` method in the custom agent to suit specific web search requirements.
- [ ] Task 4: Modify the `parse_results` method in the custom agent to scrape and parse the search results as per specific needs.
- [ ] Task 5: Add a new method in the custom agent for synthesizing the parsed results into a coherent answer.
- [ ] Task 6: Add a new method in the custom agent for comparing the synthesized answer with the user query.
- [ ] Task 7: Modify the `respond_or_search_again` method in the custom agent to loop the search, scrape, synthesize, and compare process until an answer is found or the user stops the process.
- [ ] Task 8: Modify the `respond_or_search_again` method in the custom agent to respond to the user with the final answer in a user-friendly format.
>>>>>>> UPDATED
</source>

This change marks the first task as completed in the `current_project.md` file.

Please review this change and let me know if it is correct. If it is, we can proceed to the next task.

---
## [philphil2010/bazzarfliper](https://github.com/philphil2010/bazzarfliper)@[a209cdbaf1...](https://github.com/philphil2010/bazzarfliper/commit/a209cdbaf19e4e27b7bdfdb8540af8f5b0fed92c)
#### Monday 2023-07-31 06:57:49 by philphil2010

Update README.md

Introducing the ultimate companion for seasoned merchants and aspiring traders in the enchanting world of Hypixel Skyblock - the Bazaar Flipping Mod! This cutting-edge tool has been meticulously crafted to assist you in mastering the art of bazaar flipping and maximizing your profits.

With its intelligent algorithms and real-time data analysis, the Bazaar Flipping Mod scours the vast marketplace of Hypixel Skyblock to identify the most lucrative flip opportunities. Seamlessly integrated into your gameplay, the mod presents you with a personalized list of recommended flips, allowing you to make informed decisions and capitalize on market trends.

Gone are the days of manual searching and guesswork. Our mod empowers you with valuable insights, including price fluctuations, historical data, and potential profit margins, all at your fingertips. Whether you're a veteran player seeking new avenues for wealth or a novice eager to delve into the exciting world of trading, the Bazaar Flipping Mod is your ticket to success.

Unlock your true potential as a savvy merchant and embrace the path to unimaginable riches. Get the Bazaar Flipping Mod now and revolutionize your trading experience in Hypixel Skyblock! The bazaar awaits your mastery. Happy flipping!

---
## [FalloutFalcon/Shiptest](https://github.com/FalloutFalcon/Shiptest)@[8744738e59...](https://github.com/FalloutFalcon/Shiptest/commit/8744738e5955c02834d67db6f14201c28c9ac61c)
#### Monday 2023-07-31 07:29:13 by Arturlang

Updates TGUI and adds bin folder for .bat scripts (#2011)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Updates TGUI and build tools and .vscode files to what TG has.
Does not actually update UI's, but does have fixes for a couple
including the join game UI's tabs not working.

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not needing to have a local installation of yarn to run dev-mode is
nice.
Updating TGUI is a annoying chore that helps in the future when porting
more interfaces
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
code: Adds a bin folder with dev scripts, updates TGUI, .vscode folder
to what TG has.
fix: Fixes the input in the bottom right being white in darkmode, no
more unreadable text
fix: You can now use the tab buttons in the join ship menu.
qol: The outpost mission menu now looks a whole lot better
fix: The input bar no longer randomly becomes white and unreadable on
darkmode
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: Mark Suckerberg <29362068+MarkSuckerberg@users.noreply.github.com>

---
## [ReezeBL/Fluffy-STG](https://github.com/ReezeBL/Fluffy-STG)@[8ddcb6ba45...](https://github.com/ReezeBL/Fluffy-STG/commit/8ddcb6ba45b3d6e3bb4c6045c04ccdd296422a18)
#### Monday 2023-07-31 07:29:53 by SkyratBot

Adds a wizard Right and Wrong that lets the caster give one spell (or relic) to everyone on the station [MDB IGNORE] (#22637)

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
## [nicopap/bevy](https://github.com/nicopap/bevy)@[fb4c21e3e6...](https://github.com/nicopap/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Monday 2023-07-31 07:34:13 by Ida "Iyes

bevy_audio: ECS-based API redesign (#8424)

# Objective

Improve the `bevy_audio` API to make it more user-friendly and
ECS-idiomatic. This PR is a first-pass at addressing some of the most
obvious (to me) problems. In the interest of keeping the scope small,
further improvements can be done in future PRs.

The current `bevy_audio` API is very clunky to work with, due to how it
(ab)uses bevy assets to represent audio sinks.

The user needs to write a lot of boilerplate (accessing
`Res<Assets<AudioSink>>`) and deal with a lot of cognitive overhead
(worry about strong vs. weak handles, etc.) in order to control audio
playback.

Audio playback is initiated via a centralized `Audio` resource, which
makes it difficult to keep track of many different sounds playing in a
typical game.

Further, everything carries a generic type parameter for the sound
source type, making it difficult to mix custom sound sources (such as
procedurally generated audio or unofficial formats) with regular audio
assets.

Let's fix these issues.

## Solution

Refactor `bevy_audio` to a more idiomatic ECS API. Remove the `Audio`
resource. Do everything via entities and components instead.

Audio playback data is now stored in components:
- `PlaybackSettings`, `SpatialSettings`, `Handle<AudioSource>` are now
components. The user inserts them to tell Bevy to play a sound and
configure the initial playback parameters.
- `AudioSink`, `SpatialAudioSink` are now components instead of special
magical "asset" types. They are inserted by Bevy when it actually begins
playing the sound, and can be queried for by the user in order to
control the sound during playback.

Bundles: `AudioBundle` and `SpatialAudioBundle` are available to make it
easy for users to play sounds. Spawn an entity with one of these bundles
(or insert them to a complex entity alongside other stuff) to play a
sound.

Each entity represents a sound to be played.

There is also a new "auto-despawn" feature (activated using
`PlaybackSettings`), which, if enabled, tells Bevy to despawn entities
when the sink playback finishes. This allows for "fire-and-forget" sound
playback. Users can simply
spawn entities whenever they want to play sounds and not have to worry
about leaking memory.

## Unsolved Questions

I think the current design is *fine*. I'd be happy for it to be merged.
It has some possibly-surprising usability pitfalls, but I think it is
still much better than the old `bevy_audio`. Here are some discussion
questions for things that we could further improve. I'm undecided on
these questions, which is why I didn't implement them. We should decide
which of these should be addressed in this PR, and what should be left
for future PRs. Or if they should be addressed at all.

### What happens when sounds start playing?

Currently, the audio sink components are inserted and the bundle
components are kept. Should Bevy remove the bundle components? Something
else?

The current design allows an entity to be reused for playing the same
sound with the same parameters repeatedly. This is a niche use case I'd
like to be supported, but if we have to give it up for a simpler design,
I'd be fine with that.

### What happens if users remove any of the components themselves?

As described above, currently, entities can be reused. Removing the
audio sink causes it to be "detached" (I kept the old `Drop` impl), so
the sound keeps playing. However, if the audio bundle components are not
removed, Bevy will detect this entity as a "queued" sound entity again
(has the bundle compoenents, without a sink component), just like before
playing the sound the first time, and start playing the sound again.

This behavior might be surprising? Should we do something different?

### Should mutations to `PlaybackSettings` be applied to the audio sink?

We currently do not do that. `PlaybackSettings` is just for the initial
settings when the sound starts playing. This is clearly documented.

Do we want to keep this behavior, or do we want to allow users to use
`PlaybackSettings` instead of `AudioSink`/`SpatialAudioSink` to control
sounds during playback too?

I think I prefer for them to be kept separate. It is not a bad mental
model once you understand it, and it is documented.

### Should `AudioSink` and `SpatialAudioSink` be unified into a single
component type?

They provide a similar API (via the `AudioSinkPlayback` trait) and it
might be annoying for users to have to deal with both of them. The
unification could be done using an enum that is matched on internally by
the methods. Spatial audio has extra features, so this might make it
harder to access. I think we shouldn't.

### Automatic synchronization of spatial sound properties from
Transforms?

Should Bevy automatically apply changes to Transforms to spatial audio
entities? How do we distinguish between listener and emitter? Which one
does the transform represent? Where should the other one come from?

Alternatively, leave this problem for now, and address it in a future
PR. Or do nothing, and let users deal with it, as shown in the
`spatial_audio_2d` and `spatial_audio_3d` examples.

---

## Changelog

Added:
- `AudioBundle`/`SpatialAudioBundle`, add them to entities to play
sounds.

Removed:
 - The `Audio` resource.
 - `AudioOutput` is no longer `pub`.

Changed:
 - `AudioSink`, `SpatialAudioSink` are now components instead of assets.

## Migration Guide

// TODO: write a more detailed migration guide, after the "unsolved
questions" are answered and this PR is finalized.

Before:

```rust

/// Need to store handles somewhere
#[derive(Resource)]
struct MyMusic {
    sink: Handle<AudioSink>,
}

fn play_music(
    asset_server: Res<AssetServer>,
    audio: Res<Audio>,
    audio_sinks: Res<Assets<AudioSink>>,
    mut commands: Commands,
) {
    let weak_handle = audio.play_with_settings(
        asset_server.load("music.ogg"),
        PlaybackSettings::LOOP.with_volume(0.5),
    );
    // upgrade to strong handle and store it
    commands.insert_resource(MyMusic {
        sink: audio_sinks.get_handle(weak_handle),
    });
}

fn toggle_pause_music(
    audio_sinks: Res<Assets<AudioSink>>,
    mymusic: Option<Res<MyMusic>>,
) {
    if let Some(mymusic) = &mymusic {
        if let Some(sink) = audio_sinks.get(&mymusic.sink) {
            sink.toggle();
        }
    }
}
```

Now:

```rust
/// Marker component for our music entity
#[derive(Component)]
struct MyMusic;

fn play_music(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
) {
    commands.spawn((
        AudioBundle::from_audio_source(asset_server.load("music.ogg"))
            .with_settings(PlaybackSettings::LOOP.with_volume(0.5)),
        MyMusic,
    ));
}

fn toggle_pause_music(
    // `AudioSink` will be inserted by Bevy when the audio starts playing
    query_music: Query<&AudioSink, With<MyMusic>>,
) {
    if let Ok(sink) = query.get_single() {
        sink.toggle();
    }
}
```

---
## [b0x-Cub3d/mame](https://github.com/b0x-Cub3d/mame)@[4a5b8a415f...](https://github.com/b0x-Cub3d/mame/commit/4a5b8a415fee66df01d57b871a8025d0f1f1a2f6)
#### Monday 2023-07-31 09:58:05 by wilbertpol

msx1_cart.xml: Added fourteen working items. (#11412)

* Removed Hopper (Europe) tape-to-cartridge hack.
* Demoted The Holy Quran (v1.00) to not working.

New working software list items (msx1_cart.xml)
-------------------------------
Hole in One Professional (Japan, alt 2) [file-hunter]
Hole in One Professional (Japan, alt 3) [file-hunter]
Hot-Asm (Brazil) [file-hunter]
Hot-Plan (Brazil) [file-hunter]
Hydlide II - Shine of Darkness (Korea) [file-hunter]
Hopper (Arab) [file-hunter]
Hans' Adventure (v1.1) [MSXDev]
Hans' Adventure (v1.0) [MSXDev]
Happy Halloween [Clube MSX]
Happy Square Christmas [303bcn]
Heart Stealer 2 [MSXDev]
Heroes Arena [MSXDev]
Hose Diogo Martinez: The Bussas Quest [MSXDev]
How Many Are The Dumbbells You Lift? [cobinee]

---
## [AllTheMods/ATM-7](https://github.com/AllTheMods/ATM-7)@[d818a78375...](https://github.com/AllTheMods/ATM-7/commit/d818a78375ecf5ca1c250264b96caa9f78abfe3b)
#### Monday 2023-07-31 10:02:42 by AlfredGG

Questing Update 10.27.22

- Reworked Allthemodium Chapter for a better feel, added several rewards and descriptions.
- Adjusted Bosses in the "Bounty Board", will add more bosses in the future. Gave a better reward for killing the Gaia boss.
- The quest "Time in a Bottle" now gives better rewards
- Added Template Boards to Silent Gear Questline
- Added Configuration Tool to the Functional Storage section of "Basic Storage"
- Reworked several chapters to start whenever you receive the item needed to start the mod. (For example: raw osmium for Mek, flowers for Botania, etc)
- Added new questline to the "Resources" chapter: Hostile Neural Networks
- Added a new requirement to a Blood Magic quest to better represent what is needed to create Weak Blood Shards. Also added better Demon Will rewards to the Tartaric Gem quests
- Changed requirement for the Stone Pickaxe quest in Blue Skies to allow players to start in either dimension and progress in the questline
- Changed requirement for the Starter Gen in "Getting Started: Part 1" so players can make any of the starter generators from their favorite mods, rather than just the Coal Gen from RFTools.
- Added "Heated Centrifuge" quest to Productive Bees

---
## [SirNooben/tgstation](https://github.com/SirNooben/tgstation)@[16cecf864d...](https://github.com/SirNooben/tgstation/commit/16cecf864d4b6ff864956cbc9d0cf7af4cfe1f26)
#### Monday 2023-07-31 10:26:33 by Jacquerel

Goliath basic mob (#76754)

## About The Pull Request

Converts Goliaths to the basic mob framework and gives them some new
moves because I can't leave things well enough alone.
I am planning on touching all the lavaland fauna and then maybe even the
icebox ones if I haven't got bored. The Golaith is the first because it
is iconic.

https://www.youtube.com/watch?v=JNcKvMwT4-Q
Here's me getting killed by one as a demonstration. Despite my poor
performance I would contend that they aren't a _lot_ more dangerous, but
they are a little more dangerous.

The chief difference here is that they have two new attacks which they
will only use in response to being attacked.
If fired at from range, they will target the attacker with a line of
tentacles (it doesn't track you, so is easily sidestepped).
If attacked in melee, they will surround _themselves_ with tentacles, on
a longer cooldown.

Something else you may notice in this video: I discovered that basic
mobs are actually _too smart_ to be Lavaland fauna.
Typically (unlike their old form) a mob on our new AI system is smart
enough to attack someone _the moment they come into range_ rather than
only checking on predictable ticks, which would make using the Crusher
an essentially unviable prospect.
To counteract this, Goliaths now have a delayed attack component which
gives you a visual warning and short duration to get out of range before
they swing at you. I will probably put this on all mining fauna that get
reworked, it wouldn't be a terrible thing to put on other mobs to be
honest.

Other changes: The goliath stun is now a status effect with _buckles_
you to the tentacle as if grabbed, as well as its previous effects.
While this seems purely worse, any nearby helpers can now help-click on
you to instantly remove the debuff.
Experiencing the effect of a Lobstrosity Rush Gland makes you immune to
being grabbed by tentacles and an implanted one will automatically
trigger and free you if you are hit, and the explosive effect of
Brimdust also causes the tentacle to retract (although you'd need to
take damage for this to happen). Using the tools of the land, you can
make these creatures less threatening.

The ability for a Goliath to chain-apply the ability has now also been
reduced, it won't refresh its duration if you are hit when already
buckled.

When not occupied hounding miners, Goliaths will intermittently dig up
the asteroid sand and eat any worms that this produces.
I also made some new sprites for riding a Goliath because they've been
broken since the Lavaland mob update and also kind of were ugly before
then anyway:

![image](https://github.com/tgstation/tgstation/assets/7483112/90580403-d82f-4c29-b3e1-6c462e01edda)

Other code changes:
- I made an element which only lets an attached object move every x
seconds. This is because Goliaths are far too slow to use the speed
system (the glide just looks bugged as hell) but one thing I am invested
in when converting these is to make sure that they share the same
behaviour when player or AI controlled. This is disabled while you're
riding them because it was interminably slow.
- The Goliath tentacle trail uses a supertype object now shared with the
Meteor Heart which did something kind of similar.

## Why It's Good For The Game

It begins the process of moving one of our larger subsets of NPCs onto
the newer framework for NPC behaviour.
It adds a little bit more life to an iconic but slightly uninteresting
foe which mostly just walked at you slowly.
This PR contains a few components I expect to apply more widely to other
mobs in the future.

## Changelog

:cl:
refactor: Goliaths now use the Basic Mob framework, please report any
unusual behaviour.
add: Goliaths learned a couple of new attacks which they will use in
self-defence.
balance: Help-clicking a miner grabbed by Goliath tentacles will
immediately free them, as will the effect of several items you can
scavenge from around Lavaland.
image: New sprites for the Goliath saddle.
/:cl:

---
## [larentoun/Skyrat-tg-220](https://github.com/larentoun/Skyrat-tg-220)@[efbe50f2b2...](https://github.com/larentoun/Skyrat-tg-220/commit/efbe50f2b269e6552b68360aafa0b8c476394584)
#### Monday 2023-07-31 10:53:11 by SkyratBot

[MIRROR] Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection [MDB IGNORE] (#22495)

* Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection (#76852)

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

* Arcane/Blood Barrage fixes, cleans up cult spell code, autofire barrage, more responsive/sane blood collection

---------

Co-authored-by: necromanceranne <40847847+necromanceranne@users.noreply.github.com>

---
## [genericbucket/community](https://github.com/genericbucket/community)@[1a4f52843b...](https://github.com/genericbucket/community/commit/1a4f52843b484fc98a34f82502506c83c5dac45f)
#### Monday 2023-07-31 11:01:39 by genericbucket

Create What is the Aurogra 100 Mg tablet?

https://genericbucket.com/product/aurogra-100mg-sildenafil-citrate/
Aurogra 100 mg is regarded to be one of the most appropriate generic drugs for ED treatment.
Erectile dysfunction has adverse effects on one’s sexual life. Depression, irritation in behavior leading to a divide between the partners.
The problem of ED infuses loss of self-esteem, confidence, and manhood among men. Especially in a country like India where masculinity is directly linked with an erect penis.
Order Aurogra 100 Mg from genericbucket and keep your penis erect for more than 2 hours to enjoy memorable intercourse.
How does the drug Aurogra 100 Mg can furnish its work in the body?
Erectile dysfunction is basically not a disease but a disorder of body systems and reproductive organs caused due to changing lifestyles.
In Erectile dysfunction, blood vessels on the penis receive an inadequate supply of blood resulting in less or no erection.
Aurogra 100 Mg relaxes the vessels on the penis, which allows more blood to flow causing an erection that lasts long.
Once sexually aroused the sildenafil gets activated. This is an important point for all who are going to try this drug in near future.
The drug only works after you are already aroused. Without stimulation, no erection takes place.
How long does it take for Aurogra 100 Mg to work?
Usually once taken into the food pipe, within 30 to 40 minutes the drug does its job of erection. So, plan your intercourse accordingly.
The time also depends on your eating habits and various addictions. If you consume the drug with alcohol or after the drug consumes alcohol then it may take more than 40 minutes.
Healthy eating and drinking favor sexual pleasure. A person with a mismanaged routine will face difficulties in his sexual life.
How to eat up Aurogra 100 Mg pills?
Take 1 glass of water and swallow it with 1 pill of Aurogra 100 Mg tablets.
As soon as the salt, Sildenafil citrate dissolves with water it starts its job.
Care is to be taken that you don’t consume the pills with alcohol because this will lower the efficiency of the drug resulting in less erection.
Don’t consume the drug with any beverage like soda, or any acidic juice as it may react with the drug and show unwanted and fatal side effects.
Usually, people take the drug after having a meal. But make sure to have a light one.
Aurogra 100 Mg Storage Conditions
Storage of this drug is very simple and requires the necessary facilities.
Any temperature within the range of 15°C to 30°C is suitable for the storage of this drug.
But try to keep the pills away from humid and moisture-laden places. Moisture being a form of water may react with the drug and reduce its effectiveness.
Aurogra 100 Mg Side Effects
Well, every drug shows some side effects. Mostly they are minor ones and do not cause great damage so we ignore them. But if the drug causes side effects that are fatal, septic then consults a doctor immediately. Below are the side effects of Aurogra 100 Mg pills :
Nausea	
Anxiety
High blood pressure
More sweating
Joint pain
Chest pain
Headache
Loss of vision (in critical cases, occurs very rarely)
Aurogra 100 Mg Precautions
Take special precautions if the person is above 60 years of age. At such an age the strength of the tissues reduces, the arteries work under great pressure. So please consult a doctor before its usage.
Each body reacts differently to the same chemicals. So who how the drug may react in your body. To avoid any consequences take advice from a doctor.
What is the usefulness of Aurogra 100 Mg pills?
The main use of the drug is to erect your penis and retain that erection for more tum 2 to 3 hours.
After using Aurogra 100 Mg tablets spark will generate in your marriage life.
Those who are suffering from sexual impotence should also intake this drug. With only an erection you wouldn’t be able to shake the bed. For that, you need stamina, strength, and vigor.
Aurogra 100 Mg besides giving you an erection also boosts your energy to shake up the bed.
Why purchase Aurogra 100 Mg from genericbucket?
Genericbucket is a specialist in providing premium sexual pleasure to its customers. Ask someone suffering from ED, he will always refer you to Genericbucket.
Genericbucket secures the privacy of their customer without letting the delivery agent know what’s inside the box.
Products from Genericbucket are genuine products with recommendations from renowned sexologists and doctors.

---
## [yoavelko/BaLiFront](https://github.com/yoavelko/BaLiFront)@[348708e9d3...](https://github.com/yoavelko/BaLiFront/commit/348708e9d3eb0a14f719cb8537930eaf5b9072d1)
#### Monday 2023-07-31 11:03:26 by Nitay Elzur

Merge pull request #14 from yoavelko/nitayFront

fuck you yoav

---
## [placeist/atlas-2023](https://github.com/placeist/atlas-2023)@[e348042f1c...](https://github.com/placeist/atlas-2023/commit/e348042f1c3bb42abe2a720c1c88100843b2ba31)
#### Monday 2023-07-31 12:11:29 by Cyan

Replace description of Germany x The Netherlands Kabedon

The current description is meant to be funny, not informative. The two jokes in it are copied comments from a Reddit post; and the statement that the line about 'Duitsland-san' is on the canvas is inaccurate. Half of the description is dedicated to explaining one of the jokes.

This commit proposes to replace the description to include an description of kabedon, the PlaceDE & PlaceNL collaboration, and a visual summary of the boy and the girl.

---
## [vg-mjg/mjg-repo](https://github.com/vg-mjg/mjg-repo)@[42d6439287...](https://github.com/vg-mjg/mjg-repo/commit/42d64392878ebb8abfe8eff1efcd6d1b7f9534c8)
#### Monday 2023-07-31 12:23:26 by mikichandrinkingtea

Revert "Fuck you and your shitty images."

This reverts commit 1be78c2d845e3913935487512f4cd45e1aa5aeab, reversing
changes made to c32909beb412955fff0663d9fc72a6396c352318.

---
## [Shreyaaaa21/Credit_Card_Fruad_Detection](https://github.com/Shreyaaaa21/Credit_Card_Fruad_Detection)@[462dc1a356...](https://github.com/Shreyaaaa21/Credit_Card_Fruad_Detection/commit/462dc1a356aa239a676eb38bc4c20384daef1964)
#### Monday 2023-07-31 12:24:57 by Shreya Nandkumar Jadhav

Add files via upload

🚀 Excited to share my first GitHub project! 🎉 

🛡️💳 With this project, I've ventured into the world of cybersecurity and data science, creating a robust system that uses machine learning to identify and prevent fraudulent credit card transactions. It's all about safeguarding our hard-earned money from sneaky bad actors!

Using historical transaction data, my system employs advanced algorithms to spot patterns and signs of fraudulent behavior. It acts like a digital superhero protecting our finances! 🦸‍♂️

The journey to this achievement has been incredible, honing my coding skills and gaining valuable insights into data science and cybersecurity. Leveraging machine learning in a practical application has been both challenging and rewarding.

Proudly showcased on GitHub, this project allows collaboration and learning from other talented developers. 🤝 Feel free to explore, provide feedback, and even collaborate with me on future projects!

I'm eager to learn and grow, ready to take on more exciting coding adventures. 🚀💻 Thank you for your support. Let's keep building amazing things together! 😊 #GitHub #CreditCardFraudDetection #MachineLearning #DataScience #Cybersecurity #ProjectShowcase

---
## [Dkwizard01/dkwizard01.github.io](https://github.com/Dkwizard01/dkwizard01.github.io)@[8d208bce22...](https://github.com/Dkwizard01/dkwizard01.github.io/commit/8d208bce220c7d63dece3fffdb66a984438fe2cb)
#### Monday 2023-07-31 13:08:20 by Dkwizard01

Update policy.html

Privacy Policy<br>    
==============<br>  
 
Last updated: January 21, 2022<br>  
 
This Privacy Policy describes Our policies and procedures on the 
collection, use and disclosure of Your information when You use the Services we provide and tells You about Your privacy rights and how the law protects You.<br>  
 
We use Your Personal data to provide and improve our Services. By using our Services, You agree to the collection and use of information in accordance with this Privacy Policy.<br>  
 
Interpretation and Definitions<br>    
==============================<br>  
 
Interpretation<br>    
--------------<br>  
 
The words of which the initial letter is capitalized have meanings<br> defined under the following conditions. The following definitions shall have the same meaning regardless of whether they appear in singular or in plural.<br>  
 
Definitions<br>    
-----------<br>  
 
For the purposes of this Privacy Policy:<br>  
 
*	Account means a unique account created for You to access our Services or parts of our Services.<br>  
 
*	Affiliate means an entity that controls, is controlled by or is under     common control with a party, where "control" means ownership of 50% or 
  more of the shares, equity interest or other securities entitled to   vote for election of directors or other managing authority.<br>  
 
*	Application means any and all software programs provided by the Company downloaded by You on any electronic device.<br>
 
*	Company (referred to as either "the Company", "We", "Us" or "Our" in this document) refers to DKWIZARD.<br>  
 
*	Country refers to: all countries were our Services are available.<br>

*	Device means any device that can access the Services such as a computer, a cellphone or a digital tablet.<br>  
 
*	Personal Data is any information that relates to an identified or     identifiable individual.<br>  
 
*	Services refers to any service that we provide. This includes applications.<br>  
 
*	Service Provider means any natural or legal person who processes the data on behalf of the Company. It refers to third-party companies or     individuals employed by the Company to facilitate the Services, to provide the Services on behalf of the Company, to perform Services related to the Services or to assist the Company in analysing how the Services is used.<br>  
 
*	Usage Data refers to data collected automatically, either generated by the use of the Services or from the Services infrastructure itself (for example, the duration of a page visit).<br>  
 
*	You means the individual accessing or using the Services, or the company, or other legal entity on behalf of which such individual is accessing or using the Services, as applicable.<br>  
 
 
Collecting and Using Your Personal Data<br>    
=======================================<br>  
 
Types of Data Collected<br>    
-----------------------<br>  
 
Personal Data<br>    
~~~~~~~~~~~~~<br>  
 
While using Our Services, We may ask You to provide Us with certain personally identifiable information that can be used to contact or identify You. Personally identifiable information may include, but is not limited to:<br>  
 
  * Usage Data<br>  
 
Usage Data<br>    
~~~~~~~~~~<br>  
 
Usage Data is collected automatically when using our Services.<br>  
 
Usage Data may include information such as Your Device's Internet Protocol address (e.g. IP address), browser type, browser version, the pages of our Services that You visit, the time and date of Your visit, the time spent on those pages, unique device identifiers and other diagnostic data.<br>  
 
When You access our Services by or through a mobile device, We may collect certain information automatically, including, but not limited to, the type of mobile device You use, Your mobile device unique ID, the IP address of Your mobile device, Your mobile operating system, the type of mobile Internet browser You use, unique device identifiers and other diagnostic data.<br>  
 
We may also collect information that Your browser sends whenever You visit our Services or when You access the Services by or through a mobile device.<br>  
 
Use of Your Personal Data<br>    
-------------------------<br>  
 
The Company may use Personal Data for the following purposes: 
 
*	To provide and maintain our Services, including to monitor the usage of our Services.<br>  
 
*	To manage Your Account: to manage Your registration as a user of the     Services. The Personal Data You provide can give You access to different functionalities of the Services that are available to You as a registered user.<br>  
 
*	For the performance of a contract: the development, compliance and     undertaking of the purchase contract for the products, items or Services You have purchased or of any other contract with Us through the Services we provide.<br>  
 
*	To contact You: To contact You by email, telephone calls, SMS, or other equivalent forms of electronic communication, such as a mobile     application's push notifications regarding updates or informative     communications related to the functionalities, products or contracted     Services, including the security updates, when necessary or reasonable for their implementation.<br>  
 
*	To provide You with news, special offers and general information about 
other goods, Services and events which we offer that are similar to those that you have already purchased or enquired about unless You have opted not to receive such information.<br>  
 
*	To manage Your requests: To attend and manage Your requests to Us.<br>  
 
*	For business transfers: We may use Your information to evaluate or conduct a merger, divestiture, restructuring, reorganization, dissolution, or other sale or transfer of some or all of Our assets, whether as a going concern or as part of bankruptcy, liquidation, or similar proceeding, in which Personal Data held by Us about our Services users is among the assets transferred.<br>  
 
*	For other purposes : We may use Your information for other purposes, such as data analysis, identifying usage trends, determining the effectiveness of our promotional campaigns and to evaluate and improve our Services, products, marketing and your experience.<br>  
 
 
We may share Your personal information in the following situations:<br>  
 
*	With Service Providers: We may share Your personal information with     Service Providers to monitor and analyse the use of our Services, to     contact You.<br>  
*	For business transfers: We may share or transfer Your personal information in connection with, or during negotiations of, any merger, sale of Company assets, financing, or acquisition of all or a portion of Our business to another company.<br>  
*	With Affiliates: We may share Your information with Our affiliates, in 
  which case we will require those affiliates to honor this Privacy Policy. Affiliates include Our parent company and any other subsidiaries, joint venture partners or other companies that We control or that are under common control with Us.<br>  
*	With business partners: We may share Your information with Our business partners to offer You certain products, services or promotions. * With other users: when You share personal information or otherwise interact in the public areas with other users, such information may be viewed by all users and may be publicly distributed outside. * With Your consent : We may disclose Your personal information for any other purpose with Your consent.<br>  
 
Retention of Your Personal Data<br>    
-------------------------------<br>  
 
The Company will retain Your Personal Data only for as long as is necessary for the purposes set out in this Privacy Policy. We will retain and use Your Personal Data to the extent necessary to comply with our legal obligations (for example, if we are required to retain your data to comply with applicable laws), resolve disputes, and enforce our legal agreements and policies.<br>   
The Company will also retain Usage Data for internal analysis purposes. 
Usage Data is generally retained for a shorter period of time, except when this data is used to strengthen the security or to improve the functionality of Our Services, or We are legally obligated to retain this data for longer time periods.<br>  
 
Transfer of Your Personal Data<br>    
------------------------------<br>  
 
Your information, including Personal Data, is processed at the Company's operating offices and in any other places where the parties involved in the processing are located. It means that this information may be transferred to — and maintained on — computers located outside of Your state, province, country or other governmental jurisdiction where the data protection laws may differ than those from Your jurisdiction.<br>  
 
Your consent to this Privacy Policy followed by Your submission of such information represents Your agreement to that transfer.<br>  
 
The Company will take all steps reasonably necessary to ensure that Your data is treated securely and in accordance with this Privacy Policy and no transfer of Your Personal Data will take place to an organization or a country unless there are adequate controls in place including the security of Your data and other personal information.<br>  
 
Disclosure of Your Personal Data   
--------------------------------<br>  
 
Business Transactions<br>    
~~~~~~~~~~~~~~~~~~~~~<br>  
 
If the Company is involved in a merger, acquisition or asset sale, Your 
Personal Data may be transferred. We will provide notice before Your 
Personal Data is transferred and becomes subject to a different Privacy Policy.<br>  
 
Law enforcement<br>    
~~~~~~~~~~~~~~~<br>  
 
Under certain circumstances, the Company may be required to disclose Your Personal Data if required to do so by law or in response to valid requests by public authorities (e.g. a court or a government agency).<br>  
 
Other legal requirements<br>    
~~~~~~~~~~~~~~~~~~~~~~~~<br>  
 
The Company may disclose Your Personal Data in the good faith belief that such action is necessary to:<br>  
 
*	Comply with a legal obligation.<br>  
*	Protect and defend the rights or property of the Company.<br>  
*	Prevent or investigate possible wrongdoing in connection with the 
Services.<br>  
*	Protect the personal safety of Users of the Services or the public.<br>  
*	Protect against legal liability.<br>  
 
Security of Your Personal Data<br>    
------------------------------<br>  
 
The security of Your Personal Data is important to Us, but remember that no method of transmission over the Internet, or method of electronic storage is 100% secure. While We strive to use commercially acceptable means to protect Your Personal Data, We cannot guarantee its absolute security.<br>  
 
Children's Privacy<br>    
==================<br>  
 
Our Services address children under the age of 13. We do not knowingly 
collect personally identifiable information from anyone under the age of 13. If We need to rely on consent as a legal basis for processing Your information and Your country requires consent from a parent, We may require Your parent's consent before We collect and use that information.<br>  
 
Links to Other Websites<br>    
=======================<br>  
 
Our Services may contain links to other websites that are not operated by Us.<br>  
If You click on a third party link, You will be directed to that third party's site. We strongly advise You to review the Privacy Policy of every site You visit.<br>  
 
We have no control over and assume no responsibility for the content, privacy policies or practices of any third party sites or services.<br>  
 
Changes to this Privacy Policy<br>    
==============================<br>  
 
We may update Our Privacy Policy from time to time. We will notify You of any changes by posting the new Privacy Policy on this page.<br>  
 
We will let You know via email and/or a prominent notice on Our Services, prior to the change becoming effective and update the "Last updated" date at the top of this Privacy Policy.<br>  
 
You are advised to review this Privacy Policy periodically for any changes.<br>  
Changes to this Privacy Policy are effective when they are posted on this page.<br>  
 
Contact Us<br>    
==========<br>  
 
If you have any questions about this Privacy Policy, You can contact us:<br>  
 
*	By email: DkwizardAppDevelopment@gmail.com <br>  
 
*	By visiting this page on our website:<br>  
https://dkwizard.com <br>

---
## [Addust/Yogstation](https://github.com/Addust/Yogstation)@[9df2a95e85...](https://github.com/Addust/Yogstation/commit/9df2a95e8544fb74a82d0a3062d3ee05a14b0e74)
#### Monday 2023-07-31 13:09:17 by Addust

you can just move a single thing thats actually fucking revolutionary holy shit nice work strongdmm

---
## [Addust/Yogstation](https://github.com/Addust/Yogstation)@[0f5955aade...](https://github.com/Addust/Yogstation/commit/0f5955aade18858a1c5310831f6e7cbad9f8900a)
#### Monday 2023-07-31 13:09:17 by Addust

i hate test failures and this aint gonna fix SHIT but here have some dried blood

---
## [ghostsheet/cmss13](https://github.com/ghostsheet/cmss13)@[f5784dabc7...](https://github.com/ghostsheet/cmss13/commit/f5784dabc77752802da20f2d14787667161d61ac)
#### Monday 2023-07-31 14:10:15 by ihatethisengine

More portable cades tweaks and buffs (#3967)

# About the pull request

Despite making a lot of tweaks and changes to portable cades I barely
touched them in the game until recently. Now I have more experience and
can tweak it again.

1) You can now stack damaged cades and stack stores health of each cade.
You can repair stacked cades but it will take longer time.

2) Miniengi pamphlet allows faster repairs but only when cade is folded.

3) You can quickly collapse portable cades with crowbar if you have at
least miniengi skills.

4) You no longer need to have folded portable cade in hand in order to
repair it, but if you do, you can move while repairing.

# Explain why it's good for the game

1) It's extremely annoying to repair each individual cade in order to
stack them just because it got hit by a stray bullet once. Now you can
just ignore damage and keep going.

2) Yeah it took 10 second for PFC to repair each single cade. Really
long. Now it's 5 seconds, but only when folded and if you have miniengi
skills. Makes miniengi pamphlet a bit more relevant.

3) It was intended, but turned out it was a bit inconvenient. It was
faster to collapse by hand because you didn't need to deal with tools.
Now it requires just a crowbar and slightly faster. Also requires
miniengi skill to use crowbar.

4) First was just a bit annoying, second allows more mobility which is
the point of portable barricades.


# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: you can stack scratched portable cades if their HP at least
75%. Doing so will reduce the health of all barricades in the stack to
the level of the most damaged.
balance: you can repair stacked portable cades but it will take longer
time depending on how many cades in stack.
balance: miniengi skill makes repairs of folded portable cades faster
(10 seconds to 5 seconds, same as engineer).
balance: with engineering skill at least of miniengi you can collapse
deployed portable barricade with a crowbar (wrench is no longer
required, slightly faster (2 sec to 1.5 sec)).
balance: you no longer need to have folded portable cade in hand in
order to repair it.
balance: if you have folded portable cade in hand, you can move while
repairing it.
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>

---
## [ghostsheet/cmss13](https://github.com/ghostsheet/cmss13)@[3e9d54628d...](https://github.com/ghostsheet/cmss13/commit/3e9d54628d68fe91319ae87ad7ebd7aef9500811)
#### Monday 2023-07-31 14:10:15 by Ben

Can no longer bypass Lesser Drone Limit (#4034)

# About the pull request

Users can no longer keep menu open and bypass lesser drone slots

# Explain why it's good for the game

Honestly kinda wish I didn't make this one, infinite lesser drones
sounds really funny.

# Changelog
:cl:
fix: You can no longer circumvent the lesser drone limit by keeping the
prompt open.
/:cl:

---
## [treckstar/yolo-octo-hipster](https://github.com/treckstar/yolo-octo-hipster)@[f807b59d45...](https://github.com/treckstar/yolo-octo-hipster/commit/f807b59d458f4d0227d5bd4b7f639a9986c71204)
#### Monday 2023-07-31 14:22:05 by treckstar

Life is one big road with lots of signs. So when you riding through the ruts, don't complicate your mind. Flee from hate, mischief and jealousy. Don't bury your thoughts, put your vision to reality. Wake Up and Live!

---
## [psammite/Ultimafia](https://github.com/psammite/Ultimafia)@[dd00c2d0d8...](https://github.com/psammite/Ultimafia/commit/dd00c2d0d8e913bcb1603f69c6fbed21fa309004)
#### Monday 2023-07-31 14:23:47 by Golbolco

feat: Filibuster, Queen Bee, Dignitary, Mechanic, Occultist; Priest rework; Killer Bee is Terrorist (#675)

Most of this code is from /v/ with some tweaks from moi.

Filibuster returns from EM unchanged as a Mafia role.

Queen Bee returns with her same power but now as a Cult role.

Dignitary is a renamed Civilian from EM.

Mechanic returns in full glory: no longer a mere reflexive role, but a
full blown power role that fixes cursed items!!

Occultist is a Cult-sided Traitor-like role, necessary for the Priest
rework.

Priest has been given an additional power returning from EM; if targeted
by a killing role, it will convert its killer based on its alignment.
Villagers turn blue, Mafia turn Traitor, Cultists turn Occultist, and
Indies turn Survivor.

Killer Bee has been renamed Terrorist. This may be controversial.
Refresh yourself that Mafia is a game about racially profiling and
lynching people involved with organize crime, which itself is a form of
domestic terrorism. All Mafiosos are terrorists, yo.

---------

Co-authored-by: joyce <24848927+pikulet@users.noreply.github.com>

---
## [DjfjdfofdjfjD/space-station-14](https://github.com/DjfjdfofdjfjD/space-station-14)@[31607a0be0...](https://github.com/DjfjdfofdjfjD/space-station-14/commit/31607a0be0e2ef24f4d53c7611172ec6d40a3a2b)
#### Monday 2023-07-31 14:49:03 by Emisse

hardsuit/firesuit cleanup (#18308)

* real

* hjoly fuck you guy sare annoying

* fix cargo arbitrage idk why tf it changed from editing armor values but fuck my life i guess

* why god

* Update suits.yml

* Update cargo_emergency.yml

---
## [lupont/psh](https://github.com/lupont/psh)@[1507d1c7d6...](https://github.com/lupont/psh/commit/1507d1c7d67d332282ef635e7aae0b7d87941b33)
#### Monday 2023-07-31 14:53:19 by Pontus Laos

feat: Set colors via variables

Before, colors were hardcoded in the config.rs file. Now, we have
(environment) variables representing certain parts of the command. E.g.
valid command, invalid command, unparsed, and more. By default, all
colors are white (ANSI 15). This may be changed in the future to allow
for some syntax highlighting out of the box, but I think it's kind of
cool that it's all white from the start, and with some magic variables
you can get syntax highlighting just the way you want. :-)

For now, only specific ANSI color codes are supported (i.e. a value
between 0-255). If the value of a color variable does not parse into a
byte, it will silently fall back to the default color (which is
currently always white, as stated above).

We previously had more color constants than we have functions now,
meaning that some of the granularity has been lost. Not that I think it
matters too much, most of them make sense to group together I feel.

The following is a list of the variables we read, together with values
to get pretty much the same colors as previously (due to grouping it's
probably not equivalent):

PSH_PROMPT_COL=8
PSH_COMMENT_COL=8
PSH_UNPARSED_COL=9
PSH_VALID_CMD_COL=11
PSH_INVALID_CMD_COL=1
PSH_CMD_SUB_COL=12
PSH_SEPARATOR_COL=13
PSH_LHS_COL=15
PSH_OP_COL=12
PSH_RHS_COL=15

---
## [JackSoundwave/HeatStroke](https://github.com/JackSoundwave/HeatStroke)@[c0c439cba4...](https://github.com/JackSoundwave/HeatStroke/commit/c0c439cba46510ad3699305d930c71a94f50fe22)
#### Monday 2023-07-31 15:13:05 by JackS

wow holy shit it attacks

No like, actually no joke no meme. It attacks units now

---
## [timothymtorres/tgstation](https://github.com/timothymtorres/tgstation)@[0d769e0ffa...](https://github.com/timothymtorres/tgstation/commit/0d769e0ffaaa2b0f2be2edb9659c233860420ec1)
#### Monday 2023-07-31 16:06:22 by Jacquerel

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
## [Kaz205/linux](https://github.com/Kaz205/linux)@[a2ac5cd067...](https://github.com/Kaz205/linux/commit/a2ac5cd067ada59ce6e74560868d2bcec2883333)
#### Monday 2023-07-31 16:09:47 by Douglas Anderson

migrate_pages: avoid blocking for IO in MIGRATE_SYNC_LIGHT

The MIGRATE_SYNC_LIGHT mode is intended to block for things that will
finish quickly but not for things that will take a long time.  Exactly how
long is too long is not well defined, but waits of tens of milliseconds is
likely non-ideal.

When putting a Chromebook under memory pressure (opening over 90 tabs on a
4GB machine) it was fairly easy to see delays waiting for some locks in
the kcompactd code path of > 100 ms.  While the laptop wasn't amazingly
usable in this state, it was still limping along and this state isn't
something artificial.  Sometimes we simply end up with a lot of memory
pressure.

Putting the same Chromebook under memory pressure while it was running
Android apps (though not stressing them) showed a much worse result (NOTE:
this was on a older kernel but the codepaths here are similar).  Android
apps on ChromeOS currently run from a 128K-block, zlib-compressed,
loopback-mounted squashfs disk.  If we get a page fault from something
backed by the squashfs filesystem we could end up holding a folio lock
while reading enough from disk to decompress 128K (and then decompressing
it using the somewhat slow zlib algorithms).  That reading goes through
the ext4 subsystem (because it's a loopback mount) before eventually
ending up in the block subsystem.  This extra jaunt adds extra overhead.
Without much work I could see cases where we ended up blocked on a folio
lock for over a second.  With more extreme memory pressure I could see up
to 25 seconds.

We considered adding a timeout in the case of MIGRATE_SYNC_LIGHT for the
two locks that were seen to be slow [1] and that generated much
discussion.  After discussion, it was decided that we should avoid waiting
for the two locks during MIGRATE_SYNC_LIGHT if they were being held for
IO.  We'll continue with the unbounded wait for the more full SYNC modes.

With this change, I couldn't see any slow waits on these locks with my
previous testcases.

NOTE: The reason I stated digging into this originally isn't because some
benchmark had gone awry, but because we've received in-the-field crash
reports where we have a hung task waiting on the page lock (which is the
equivalent code path on old kernels).  While the root cause of those
crashes is likely unrelated and won't be fixed by this patch, analyzing
those crash reports did point out these very long waits seemed like
something good to fix.  With this patch we should no longer hang waiting
on these locks, but presumably the system will still be in a bad shape and
hang somewhere else.

[1] https://lore.kernel.org/r/20230421151135.v2.1.I2b71e11264c5c214bc59744b9e13e4c353bc5714@changeid

Link: https://lkml.kernel.org/r/20230428135414.v3.1.Ia86ccac02a303154a0b8bc60567e7a95d34c96d3@changeid
Signed-off-by: Douglas Anderson <dianders@chromium.org>
Suggested-by: Matthew Wilcox <willy@infradead.org>
Reviewed-by: Matthew Wilcox (Oracle) <willy@infradead.org>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hillf Danton <hdanton@sina.com>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Alexander Viro <viro@zeniv.linux.org.uk>
Cc: Christian Brauner <brauner@kernel.org>
Cc: Gao Xiang <hsiangkao@linux.alibaba.com>
Cc: Huang Ying <ying.huang@intel.com>
Cc: Vlastimil Babka <vbabka@suse.cz>
Cc: Yu Zhao <yuzhao@google.com>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[52c8da7ea4...](https://github.com/Thunder12345/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Monday 2023-07-31 16:12:47 by Jacquerel

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
## [plata/ublue-surface](https://github.com/plata/ublue-surface)@[c7deb7d6fe...](https://github.com/plata/ublue-surface/commit/c7deb7d6fe3aa4256d7a79123ffc250a24165263)
#### Monday 2023-07-31 16:14:53 by Arcitec

fix: friendlier experience in the "yafti" first boot template

- The first screen's "Pick some applications to get started" has been replaced with a friendly welcoming message.

- The second screen's difficult-to-understand "WARNING: This will modify your Flatpaks if you are rebasing!" has been replaced with an explanation of what it actually does.

- The application setup screen is now titled "Application Installer", since the previous title sounded too much like a silly rhyme. It's a minor change.

- All Flatpaks now default to system-wide install thanks to the great work of bsherman at https://github.com/ublue-os/yafti/pull/82. This saves tons of disk space for multi-user systems.

- The "system application" category have been split up into GNOME apps and every other system app, so that people on other desktop environments don't get all the GNOME apps.

- Apps that had too vague descriptions have been renamed to their full names, such as "Backup -> Deja Dup Backups".

- All app lists have been sorted alphabetically.

- Non-inclusive language in descriptions has been changed.

- Added SteamTinkerLaunch as a suggestion for the Steam category, which is the best tool for managing Steam game configurations and Proton installations, albeit very advanced since it can do practically anything the gamer needs. :)

---
## [graphcore/torchbench-fork](https://github.com/graphcore/torchbench-fork)@[745644f391...](https://github.com/graphcore/torchbench-fork/commit/745644f391b4d11da107b2c82fe2d7a3eacf561d)
#### Monday 2023-07-31 16:16:53 by Mark Saroufim

FIX SAM for bfloat16 (#1764)

Summary:
Ok this was kinda annoying

Basically the SAM codebase had a few places where it hardcodes `torch.float32` such that even if you convert the model to `torch.bfloat16` a few parts of the model won't be and will have type mismatch errors - this fixes the problem cpuhrsch desertfire - idk enough about floats and why there isn't some type promotion rule for bfloat16

I wonder whether we should add tests for multiple dtypes in torchbench to make checking for this kind of issue more robust especially now that bfloat16 seems to be the default for dynamo xuzhao9

## Logs

```
FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
E
======================================================================
ERROR: test_sam_eval_cuda (__main__.TestBenchmark)
----------------------------------------------------------------------
components._impl.workers.subprocess_rpc.ChildTraceException: Traceback (most recent call last):
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 482, in _run_block
    exec(  # noqa: P204
  File "<subprocess-worker>", line 2, in <module>
  File "/home/ubuntu/benchmark/torchbenchmark/util/model.py", line 280, in invoke
    out = self.eval()
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/__init__.py", line 65, in eval
    masks, scores, logits = predictor.predict(
  File "/home/ubuntu/benchmark/torchbenchmark/models/sam/predictor.py", line 164, in predict
    low_res_masks_np = low_res_masks[0].detach().cpu().numpy()
TypeError: Got unsupported ScalarType BFloat16

    working_dir: /tmp/tmpg5de41du
    stdout:
        [2023-07-13] 01:57:38.499061: TIMER_SUBPROCESS_BEGIN_EXEC
        [2023-07-13] 01:57:39.002078: TIMER_SUBPROCESS_FAILED
        [2023-07-13] 01:57:39.002141: TIMER_SUBPROCESS_FINISHED
        [2023-07-13] 01:57:39.002153: TIMER_SUBPROCESS_BEGIN_READ

    stderr:

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/ubuntu/benchmark/test.py", line 104, in eval_fn
    task.invoke()
  File "/home/ubuntu/benchmark/torchbenchmark/__init__.py", line 402, in invoke
    self.worker.run("""
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 155, in run
    self._run(snippet)
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_worker.py", line 320, in _run
    subprocess_rpc.SerializedException.raise_from(
  File "/home/ubuntu/benchmark/components/_impl/workers/subprocess_rpc.py", line 458, in raise_from
    raise e from ChildTraceException(traceback_str)
TypeError: Got unsupported ScalarType BFloat16

----------------------------------------------------------------------
Ran 1 test in 7.814s

FAILED (errors=1)
(sam) ubuntu@ip-172-31-9-217:~/benchmark$ python test.py -k "test_sam_eval_cuda"
.
----------------------------------------------------------------------
Ran 1 test in 8.315s

OK
```

Pull Request resolved: https://github.com/pytorch/benchmark/pull/1764

Reviewed By: drisspg, cpuhrsch

Differential Revision: D47441873

Pulled By: msaroufim

fbshipit-source-id: a60880fd7c0826cfd469ace39d76894469ca0e5e

---
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[63d6c2e962...](https://github.com/TheVekter/tgstation/commit/63d6c2e9628be7af04948f59488043f109f1faab)
#### Monday 2023-07-31 16:17:05 by CRITAWAKETS

Adds in the smoothbore disablers. (#76773)

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

---
## [TheVekter/tgstation](https://github.com/TheVekter/tgstation)@[a8e0d7c8d2...](https://github.com/TheVekter/tgstation/commit/a8e0d7c8d202027d36c96391ed9a43cb5d708065)
#### Monday 2023-07-31 16:17:05 by MrMelbert

Adds a new positive quirk, "Spacer Born".  (#76809)

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

---
## [clayne/OpenGraphic](https://github.com/clayne/OpenGraphic)@[c3a9f933b0...](https://github.com/clayne/OpenGraphic/commit/c3a9f933b03d04ad97750961b210c9ad3ee4156f)
#### Monday 2023-07-31 16:18:05 by Gforcex

Update Blender.md* [awesomeblend](https://github.com/Davetmo/awesomeblend) A curated list of awesome Blender add-ons, tools, tutorials and resources for 3D Artists, Hobbyists, Developers, Researchers. Focused mostly open source and free resources. Blender 2.8+ compatible list.   * [MB-Lab](https://github.com/animate1978/MB-Lab) MB-Lab is a character creation tool for Blender 2.80, based off ManuelBastioniLAB https://www.mblab.dev * [DreamUV](https://github.com/leukbaars/DreamUV) DreamUV is a collection of tools that allow you to manipulate UVs in the 3D viewport. * [Magic-UV](https://github.com/nutti/Magic-UV) Blender Add-on: Magic UV * [bricker](https://github.com/bblanimation/bricker) Bricker is a powerful modeling, animation, and simulation addon for Blender designed to streamline and, in many cases, automate the artist's workflow for LEGO bricks. Created by Christopher Gearhart. * [mixer](https://github.com/ubisoft/mixer) Add-on for real-time collaboration in Blender. * [Stop-motion-OBJ](https://github.com/neverhood311/Stop-motion-OBJ) A Blender add-on for importing a sequence of OBJ meshes as frames * [Blender_UE4_VectorFieldEditor](https://github.com/isathar/Blender_UE4_VectorFieldEditor) Blender addon that adds support for working with 3D vector fields using the FGA file format. * [animation_nodes](https://github.com/JacquesLucke/animation_nodes) Node based visual scripting system designed for motion graphics in Blender. * [Abnormal](https://github.com/BlenderNPR/Abnormal) Blender Abnormal add-on for vertex normal editing * [Pivot-Painter-for-Blender](https://github.com/Gvgeo/Pivot-Painter-for-Blender) Pivot Painter is a Blender addon to create a 3d model, that will use the Pivot Painter Tool's shaders in Unreal Engine 4 * [TexTools-Blender](https://github.com/SavMartin/TexTools-Blender) http://renderhjs.net/textools/blender/ * [MACHIN3tools](https://github.com/machin3io/MACHIN3tools) MACHIN3tools is a free, continuously evolving collection of blender tools and pie menus in a single customizable package. * [Sorcar](https://github.com/aachman98/Sorcar) Procedural modeling in Blender using Node Editor * [Malt](https://github.com/bnpr/Malt) Render framework for NPR * [BEER](https://github.com/BlenderNPR/BEER) Blender Extended Expressive Renderer (A stylized renderer) * [retopoflow](https://github.com/CGCookie/retopoflow) A suite of retopology tools for Blender * [Blender-BakeLab2](https://github.com/Shahzod114/Blender-BakeLab2) Blender addon for baking images * [bpbrt4](https://github.com/NicNel/bpbrt4) pbrt-v4 render engine/exporter for Blender * [MolecularNodes](https://github.com/BradyAJohnston/MolecularNodes) Addon and nodes for working with structural biology and molecular data in Blender. * [MapsModelsImporter](https://github.com/eliemichel/MapsModelsImporter) A Blender add-on to import models from google maps * [b3dsdf](https://github.com/williamchange/b3dsdf) A toolkit of 2D/3D signed distance functions and sdf/vector operator nodegroups(135+) for Blender 2.83+. Also available as an addon which adds a menu in the shader editor. * [dream-textures](https://github.com/carson-katri/dream-textures) Stable Diffusion built-in to the Blender shader editor * [AI-Render](https://github.com/benrugg/AI-Render) Stable Diffusion in Blender * [glslTexture](https://github.com/patriciogonzalezvivo/glslTexture) Blender addon to create 2D textures from GLSL.  * [Blender-Lightsheet](https://github.com/markus-ebke/Blender-Lightsheet) Add-on for Blender3D to create caustics for Cycles and EEVEE * [blendify](https://github.com/ptrvilya/blendify) Blendify is a lightweight Python framework that provides a high-level API for creating and rendering scenes with Blender. Developed with a focus on 3D computer vision visualization, Blendify simplifies access to selected Blender functions and objects. * [jmesh-tools](https:github.com/jayanam/jmesh-tools)

---
## [Esparguetes/WebBrowserGame](https://github.com/Esparguetes/WebBrowserGame)@[2f70ac3d2e...](https://github.com/Esparguetes/WebBrowserGame/commit/2f70ac3d2e41cc6544e5786ac844f6e6a363d035)
#### Monday 2023-07-31 16:37:47 by Esparguetes

FIX ACCOUNT + VILLAGE + GRID CREATION

UWU YAY XDDD
ON account creation we create a village that is placed kinda random in the grid , but positioned around the center, then sequent villages are created nearby but not next to the one existing etc ewtc etc and we can createa all 25 villages :>

WE STILL NEED TO FIX THE NUMBER OF TIMES WE FETCH THE GRID IS A CRINGE NUMBER OF TIMES, FOR EACH VILLAGE CREATION WE EFTCH IT 20 TIMES WE GIVE A LAUGH BUT IT WILL GIVE US HELL SOON LOOL

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[6aadb8edfd...](https://github.com/git-for-windows/git/commit/6aadb8edfd25d62e571596e7c530057086345c1a)
#### Monday 2023-07-31 17:05:52 by Johannes Schindelin

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[69827604c4...](https://github.com/tgstation/tgstation/commit/69827604c46952dd4393db8617cd494ade17bea2)
#### Monday 2023-07-31 17:09:55 by Watermelon914

Improves the RPG loot wizard event. (#77218)

## About The Pull Request
As the title says. Adds a bunch more stat changes to various different
items and a somewhat simple way of modifying them whilst minimizing
side-effects as much as possible.
Added a new negative curse of polymorph suffix that can randomly
polymorph you once you pick up the item.
Curse of hunger items won't start on items that are not on a turf.
Curse of polymorph will only activate when equipped.

Bodyparts, two-handed melees, bags, guns and grenades, to name a few,
have a bunch of type-specific stat changes depending on their quality.

Some items won't gain fantasy suffixes during the RPG loot event, like
stacks, chairs and paper, to make gamifying the stats a bit harder.
I'm sure there'll still be other ways to game the event, but it's not
that big of a deal since these are the easiest ways to game it.
High level items also have a cool unusual effect aura

## Why It's Good For The Game
Makes the RPG item event cooler. Right now, it's a bit lame since
everything only gains force value and wound bonus on attack. This makes
the statistic increases more type-based and make it interesting to use

It's okay for some items to be powerful since this is a wizard event and
a very impactful one too. By making the curse of hunger items not spawn
on people, it'll also make it a less painful event too.

## Changelog
:cl:
add: Expanded the RPG loot wizard event by giving various different
items their own statistic boost.
/:cl:

---------

Co-authored-by: Watermelon914 <3052169-Watermelon914@users.noreply.gitlab.com>

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[2d0b4f053f...](https://github.com/tgstation/tgstation/commit/2d0b4f053f1db70d9f3ab6548f58b7928f159eaf)
#### Monday 2023-07-31 18:17:50 by san7890

Refactors Slaughter/Laughter Demons into Basic Mobs (#77206)

## About The Pull Request

On the tin, the former "imp" is now refactored into basic mob code. Very
simple since these are only meant to be controlled by players, and all
of their stuff was on Signal Handlers and Cooldown Actions anyways. Just
lessens the amount of stupidity.

Did you know that we were trying to make demons spawn in a `pop`'d cat
named "Laughter"? Embedded in the list? I've literally never seen this
cat, so I'm under heavy suspicion that the code we were using was broken
for the longest time (or may have never worked), and we now instead just
do it a much more sane way of having a cat spawn on our demise.

## Why It's Good For The Game

Cleaner code! Less simple mob jank to deal with. Trims down the list of
simple animals to refactor. No more duplicated code that we were already
doing on parent! It's so good man literally everything was seamless with
a bit of retooling and tinkering. The typepath is also no longer `imp`,
it's actually `demon`, which I'm happy with because there's no other
demons to have it be confused with anymore.

We were also doing copypasta on both the demon spawner bottle and the
demon spawning event so I also just unified that into the mob. I also
reorganized the sprites to be a bit clearer and match their new
nomenclature

## Changelog
:cl:
refactor: Slaughter and Laughter Demons have been refactored, please
place an issue report for any unexpected things/hitches.
fix: Laughter Demons should now actually drop a kitten.
/:cl:

---
## [newstools/2023-the-times](https://github.com/newstools/2023-the-times)@[8489279af4...](https://github.com/newstools/2023-the-times/commit/8489279af46390cdea4152d9dc03f132bb8419b5)
#### Monday 2023-07-31 18:26:59 by Billy Einkamerer

Created Text For URL [www.timeslive.co.za/news/south-africa/2023-07-31-colleague-shocked-after-loving-boyfriend-is-arrested-for-murder-of-girlfriend/]

---
## [Time-Green/tgstation](https://github.com/Time-Green/tgstation)@[1e27ce031b...](https://github.com/Time-Green/tgstation/commit/1e27ce031ba94161c64edcc87e5f3aaad778d3fe)
#### Monday 2023-07-31 19:18:36 by carlarctg

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
## [Bakobiibizo/eleven_labs_hackathon](https://github.com/Bakobiibizo/eleven_labs_hackathon)@[402f166c41...](https://github.com/Bakobiibizo/eleven_labs_hackathon/commit/402f166c4150c81c8ce6a5888981343131be3ccf)
#### Monday 2023-07-31 20:11:31 by Richard Bakobiibizo

aider: The `tts` method now returns the audio data as bytes if it's a string.

# Aider chat conversation:

USER: its still not working

ASSISTANT: I'm sorry to hear that you're still having trouble. Could you please provide more details about the issue? What function are you trying to run, and what error message are you seeing?

USER: its saying that string doesnt have the right method

ASSISTANT: It seems like you're trying to call a method on a string that doesn't exist. This could be due to a variety of reasons, such as a typo in the method name or trying to use a method that's not applicable to strings.

To help you further, I need to know the exact error message and the line of code that's causing the error. Could you please provide these details?

USER: Traceback (most recent call last):
  File "C:\Users\richa\00.Coding\GitHub\active\eleven_labs\testing.py", line 40, in <module>
    test_voice()
  File "C:\Users\richa\00.Coding\GitHub\active\eleven_labs\testing.py", line 33, in test_voice
    f.write(byte_string)

ASSISTANT: The error message indicates that the `write` method is trying to write a string to a file, but it's receiving a different type of object. The `write` method expects a string (for text files) or bytes (for binary files).

The `byte_string` variable is supposed to contain the audio data in bytes format. However, it seems like it's not actually a byte string. The `tts` method of the `TextToSpeach` class should return the audio data as bytes, but it might be returning a different type of object.

To fix this, we need to ensure that the `tts` method is returning the audio data as bytes. Here's how to do that:

```python
voice/eleven_labs.py
<<<<<<< ORIGINAL
    def tts(self, text, voice_id):
        # existing code
        return audio_data
=======
    def tts(self, text, voice_id):
        # existing code
        if isinstance(audio_data, str):
            audio_data = audio_data.encode('utf-8')
        return audio_data
>>>>>>> UPDATED
```

This change will encode the `audio_data` as bytes if it's a string. If `audio_data` is already bytes, it will be returned as is. If `audio_data` is neither a string nor bytes, you'll need to update the `tts` method to ensure it's returning the audio data as bytes.

USER: InvalidEditBlock: edit failed!

voice/eleven_labs.py does not contain the *exact sequence* of ORIGINAL lines you specified.
Try again.
DO NOT skip blank lines, comments, docstrings, etc!
The ORIGINAL block needs to be EXACTLY the same as the lines in voice/eleven_labs.py with nothing missing!

voice/eleven_labs.py does not contain these 3 exact lines in a row:
```
    def tts(self, text, voice_id):
        # existing code
        return audio_data
```

ASSISTANT: I apologize for the confusion. Let's correct the method. Here's the correct way to ensure that the `tts` method is returning the audio data as bytes:

```python
voice/eleven_labs.py
<<<<<<< ORIGINAL
    def tts(self, text, voice_id):
        if not voice_id:
            voice_id = None
        if not text:
            raise ValueError("text is required")
        self.url = f"{self.base_url}text-to-speech/{voice_id}/stream"
        self.data = {
          "text": text,
          "model_id": "eleven_monolingual_v1",
          "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
          }
        }
        return self.tts_request()
=======
    def tts(self, text, voice_id):
        if not voice_id:
            voice_id = None
        if not text:
            raise ValueError("text is required")
        self.url = f"{self.base_url}text-to-speech/{voice_id}/stream"
        self.data = {
          "text": text,
          "model_id": "eleven_monolingual_v1",
          "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
          }
        }
        audio_data = self.tts_request()
        if isinstance(audio_data, str):
            audio_data = audio_data.encode('utf-8')
        return audio_data
>>>>>>> UPDATED
```

This change will encode the `audio_data` as bytes if it's a string. If `audio_data` is already bytes, it will be returned as is. If `audio_data` is neither a string nor bytes, you'll need to update the `tts` method to ensure it's returning the audio data as bytes.

---
## [kinkie/squid](https://github.com/kinkie/squid)@[2b6b1bcb86...](https://github.com/kinkie/squid/commit/2b6b1bcb8650095c99a1916f5964305484af7ef0)
#### Monday 2023-07-31 21:24:04 by Alex Rousskov

Bug 5055: FATAL FwdState::noteDestinationsEnd exception: opening (#877)

The bug was caused by commit 25b0ce4. Other known symptoms are:

    assertion failed: store.cc:1793: "isEmpty()"
    assertion failed: FwdState.cc:501: "serverConnection() == conn"
    assertion failed: FwdState.cc:1037: "!opening()"

This change has several overlapping parts. Unfortunately, merging
individual parts is both difficult and likely to cause crashes.

## Part 1: Bug 5055.

FwdState used to check serverConn to decide whether to open a connection
to forward the request. Since commit 25b0ce4, a nil serverConn pointer
no longer implies that a new connection should be opened: FwdState
helper jobs may already be working on preparing an existing open
connection (e.g., sending a CONNECT request or negotiating encryption).

Bad serverConn checks in both FwdState::noteDestination() and
FwdState::noteDestinationsEnd() methods led to extra connectStart()
calls creating two conflicting concurrent helper jobs.

To fix this, we replaced direct serverConn inspection with a
usingDestination() call which also checks whether we are waiting for a
helper job. Testing that fix exposed another set of bugs: The helper job
pointers or in-job connections were left stale/set after forwarding
failures. The changes described below addressed most of those problems.


## Part 2: Connection establishing helper jobs and their callbacks

A proper fix for Bug 5055 required answering a difficult question: When
should a dying job call its callbacks? We only found one answer which
required cooperation from the job creator and led to the following
rules:

* AsyncJob destructors must not call any callbacks.

* AsyncJob::swanSong() is responsible for async-calling any remaining
  (i.e. set, uncalled, and uncancelled) callbacks.

* AsyncJob::swanSong() is called (only) for started jobs.

* AsyncJob destructing sequence should validate that no callbacks remain
  uncalled for started jobs.

... where an AsyncJob x is considered "started" if AsyncJob::Start(x)
has returned without throwing.

A new JobWait class helps job creators follow these rules while keeping
track on in-progress helper jobs and killing no-longer-needed helpers.

Also fixed very similar bugs in tunnel.cc code.


## Part 3: ConnOpener fixes

1. Many ConnOpener users are written to keep a ConnectionPointer to the
   destination given to ConnOpener. This means that their connection
   magically opens when ConnOpener successfully connects, before
   ConnOpener has a chance to notify the user about the changes. Having
   multiple concurrent connection owners is always dangerous, and the
   user cannot even have a close handler registered for its now-open
   connection. When something happens to ConnOpener or its answer, the
   user job may be in trouble. Now, ConnOpener callers no longer pass
   Connection objects they own, cloning them as needed. That adjustment
   required adjustment 2:

2. Refactored ConnOpener users to stop assuming that the answer contains
   a pointer to their connection object. After adjustment 1 above, it
   does not. HappyConnOpener relied on that assumption quite a bit so we
   had to refactor to use two custom callback methods instead of one
   with a complicated if-statement distinguishing prime from spare
   attempts. This refactoring is an overall improvement because it
   simplifies the code. Other ConnOpener users just needed to remove a
   few no longer valid paranoid assertions/Musts.

3. ConnOpener users were forced to remember to close params.conn when
   processing negative answers. Some, naturally, forgot, triggering
   warnings about orphaned connections (e.g., Ident and TcpLogger).
   ConnOpener now closes its open connection before sending a negative
   answer.

4. ConnOpener would trigger orphan connection warnings if the job ended
   after opening the connection but without supplying the connection to
   the requestor (e.g., because the requestor has gone away). Now,
   ConnOpener explicitly closes its open connection if it has not been
   sent to the requestor.

Also fixed Comm::ConnOpener::cleanFd() debugging that was incorrectly
saying that the method closes the temporary descriptor.

Also fixed ConnOpener callback's syncWithComm(): The stale
CommConnectCbParams override was testing unused (i.e. always negative)
CommConnectCbParams::fd and was trying to cancel the callback that most
(possibly all) recipients rely on: ConnOpener users expect a negative
answer rather than no answer at all.

Also, after comparing the needs of two old/existing and a temporary
added ("clone everything") Connection cloning method callers, we decided
there is no need to maintain three different methods. All existing
callers should be fine with a single method because none of them suffers
from "extra" copying of members that others need. Right now, the new
cloneProfile() method copies everything except FD and a few
special-purpose members (with documented reasons for not copying).

Also added Comm::Connection::cloneDestinationDetails() debugging to
simplify tracking dependencies between half-baked Connection objects
carrying destination/flags/other metadata and open Connection objects
created by ConnOpener using that metadata (which are later delivered to
ConnOpener users and, in some cases, replace those half-baked
connections mentioned earlier. Long-term, we need to find a better way
to express these and other Connection states/stages than comments and
debugging messages.


## Part 4: Comm::Connection closure callbacks

We improved many closure callbacks to make sure (to the extent possible)
that Connection and other objects are in sync with Comm. There are lots
of small bugs, inconsistencies, and other problems in Connection closure
handlers. It is not clear whether any of those problems could result in
serious runtime errors or leaks. In theory, the rest of the code could
neutralize their negative side effects. However, even in that case, it
would only be a matter of time before the next bug bites us due to stale
Connection::fd and such. These changes themselves carry elevated risk,
but they get us closer to reliable code as far as Connection maintenance
is concerned. Without them, we will keep chasing deadly side effects of
poorly implemented closure callbacks.

Long-term, all these manual efforts to keep things in sync should become
unnecessary with the introduction of appropriate Connection ownership
APIs that automatically maintain the corresponding environments (TODO).


## Part 5: Other notable improvements in the adjusted code

Improved Security::PeerConnector::serverConn and
Http::Tunneler::connection management, especially when sending negative
answers. When sending a negative answer, we would set answer().conn to
an open connection, async-send that answer, and then hurry to close the
connection using our pointer to the shared Connection object. If
everything went according to the plan, the recipient would get a non-nil
but closed Connection object. Now, a negative answer simply means no
connection at all. Same for a tunneled answer.

Refactored ICAP connection-establishing code to to delay Connection
ownership until the ICAP connection is fully ready. This change
addresses primary Connection ownership concerns (as they apply to this
ICAP code) except orphaning of the temporary Connection object by helper
job start exceptions (now an explicit XXX). For example, the transaction
no longer shares a Connection object with ConnOpener and
IcapPeerConnector jobs.

Probably fixed a bug where PeerConnector::negotiate() assumed that
sslFinalized() does not return true after callBack(). It may (e.g., when
CertValidationHelper::Submit() throws). Same for
PeekingPeerConnector::checkForPeekAndSpliceMatched().
 
Fixed FwdState::advanceDestination() bug that did not save
ERR_GATEWAY_FAILURE details and "lost" the address of that failed
destination, making it unavailable to future retries (if any).

Polished PeerPoolMgr, Ident, and Gopher code to be able to fix similar
job callback and connection management issues.

Polished AsyncJob::Start() API. Start() used to return a job pointer,
but that was a bad idea:
    
* It implies that a failed Start() will return a nil pointer, and that
  the caller should check the result. Neither is true.

* It encourages callers to dereference the returned pointer to further
  adjust the job. That technically works (today) but violates the rules
  of communicating with an async job. The Start() method is the boundary
  after which the job is deemed asynchronous.
    
Also removed old "and wait for..." post-Start() comments because the
code itself became clear enough, and those comments were becoming
increasingly stale (because they duplicated the callback names above
them).

Fix Tunneler and PeerConnector handling of last-resort callback
requirements. Events like handleStopRequest() and callException() stop
the job but should not be reported as a BUG (e.g., it would be up to the
callException() to decide how to report the caught exception). There
might (or there will) be other, similar cases where the job is stopped
prematurely for some non-BUG reason beyond swanSong() knowledge. The
existence of non-bug cases does not mean there could be no bugs worth
reporting here, but until they can be identified more reliably than all
these benign/irrelevant cases, reporting no BUGs is a (much) lesser
evil.

TODO: Revise AsyncJob::doneAll(). Many of its overrides are written to
check for both positive (i.e. mission accomplished) and negative (i.e.
mission cancelled or cannot be accomplished) conditions, but the latter
is usually unnecessary, especially after we added handleStopRequest()
API to properly support external job cancellation events. Many doneAll()
overrides can probably be greatly simplified.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[bd50e6f04f...](https://github.com/Buildstarted/linksfordevs/commit/bd50e6f04f17d469c7b25a4f5ae40c53e7af3aee)
#### Monday 2023-07-31 22:10:45 by Ben Dornis

Updating: 7/31/2023 10:00:00 PM

 1. Added: Getting started with NGINX
    (https://sophiazhang.com/post/start-with-nginx/)
 2. Added: A comprehensive guide to Redux for beginners
    (https://www.tanvi.dev/blog/3-a-comprehensive-guide-to-redux-for-beginners)
 3. Added: I Paid Off $194k in Student Loans in Six Years. It Wasn’t Easy. - BJL
    (https://benjaminlabaschin.com/194k-in-loans-in-six-years/)
 4. Added: Socialized Proof of Work
    (https://blog.erlend.sh/socialized-proof-of-work)
 5. Added: File distribution over DNS: (ab)using DNS as a CDN (eighty-twenty news)
    (https://eighty-twenty.org/2023/07/31/dns-as-a-cdn)
 6. Added: So, you want to deploy on the edge?
    (https://zknill.io/posts/edge-database/)
 7. Added: AI Diaries: Two Important Facts About Generative Prose
    (https://www.davystevenson.com/articles/ai-diaries-two-important-facts-about-generative-prose)
 8. Added: Cachelines and Striped Locks — ~ngp
    (https://packetlost.dev/blog/cachelines-and-striped-locks/)
 9. Added: Gabe Henriques
    (https://gabehenriques.com/blog/space-tourism/)
10. Added: An optimal-stopping quant riddle - Emir's blog
    (https://emiruz.com/post/2023-07-30-optimal-stopping/)
11. Added: The Limits of AI: Why Not Every Problem Can Be Solved with Machine Learning - Arkavian
    (https://arkavian.com/2023/07/31/the-limits-of-ai-why-not-every-problem-can-be-solved-with-machine-learning/)
12. Added: Your Social Network Is Bigger Than You Think! – James Ashford
    (https://jrashford.com/2023/07/31/your-social-network-is-bigger-than-you-think/)
13. Added: Tribal Knowledge
    (https://daedtech.com/tribal-knowledge/)
14. Added: Poll Working
    (https://hybras.dev/posts/2023-06-06-poll-working/)
15. Added: Wasting Time to Waste Less Time
    (https://www.aidanmstrong.com/blog/wasting-time-to-waste-less-time)
16. Added: LK-99: The Live Online Race for a Room-Temperature Superconductor (Summary)
    (https://eirifu.wordpress.com/2023/07/30/lk-99-superconductor-summary/)
17. Added: Toggles suck! | Axess Lab
    (https://axesslab.com/toggles-suck/)
18. Added: Why I switched from Plaid to Stripe.. and then back to Plaid - Balance Budget
    (https://balancebudget.app/2023/07/29/why-i-switched-from-plaid-to-stripe-and-then-back-to-plaid/)
19. Added: Reflections on a Month with BBEdit and Nova — Sympolymathesy, by Chris Krycho
    (https://v5.chriskrycho.com/journal/reflections-on-a-month-with-bbedit-and-nova/)
20. Added: Security keys in the land of passkeys
    (https://blog.millerti.me/2023/07/30/security-keys-in-the-land-of-passkeys/)
21. Added: The next step: PostOwl
    (https://michaelaufreiter.com/posts/the-next-step-postowl)
22. Added: Blackmagic Design SDI-HDMI converter micro USB problems, and a rant about connector receptacles in general
    (https://www.krekr.nl/content/blackmagic-design-sdi-hdmi-converter-micro-usb-problems-and-a-rant-about-connector-receptacles-in-general/)
23. Added: Binary Heap | Concurrency Deep Dives
    (https://cmhteixeira.com/concurrency/binaryHeap.html)
24. Added: On .NET Live - Real World frontends and backends with Conduit
    (https://youtube.com/watch?v=DGrPQqyOpcU)
25. Added: Shamir Secret Sharing
    (https://max.levch.in/post/724289457144070144/shamir-secret-sharing)

Generation took: 00:10:32.3576058
 Maintenance update - cleaning up homepage and feed

---
## [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)@[eab7a8f63a...](https://github.com/microsoft/semantic-kernel/commit/eab7a8f63a0bfd289070e82b423ac78bd306ee5b)
#### Monday 2023-07-31 23:53:45 by Sailesh R

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

