## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-05-21](docs/good-messages/2023/2023-05-21.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,790,490 were push events containing 2,769,470 commit messages that amount to 139,507,763 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 80 messages:


## [Ghommie/tgstation](https://github.com/Ghommie/tgstation)@[b1716732b0...](https://github.com/Ghommie/tgstation/commit/b1716732b058121e86c60700fb9d1d8f4f9a6b3a)
#### Sunday 2023-05-21 00:02:28 by Cheshify

The North Star Expeditionary Vessel - A Second Wind (#74371)

## About The Pull Request
A new map for TGstation, in the works! It has 4 fucking Z levels, a
massive expansive maintenance with unique designs, and some unique code
features in the works.

To Do:
- [x] Update the Map to Modern TG
- [x] Local Tests
- [x] Work on Map Optimizations
- [x] Run Live Tests

Fikou has greatly helped with creating an important flavour aspect of
this map, Trek Uniforms on anyone who joins! See the forum thread for
more. This includes the framework for innate station traits, station
traits loaded as long as it's in a map's json

Here's the forum dev thread there are screenshots there.
https://tgstation13.org/phpBB/viewtopic.php?p=657252#p657252

### Mapping March
Ckey to receive rewards: Cheshify

## Why It's Good For The Game
So, this is the North Star. An effort taking multiple mappers and of 9~
months of hard work. This map was not initially designed for TGstation,
but always designed for TGstation code. The process of retooling the map
for TGstation was an absolute joy and I feel like the map definitely has
it's niche as a massive and unique experience for it's players.

I adore this map, it's gorgeous, has a unique aesthetic, and a number of
very funny interactions with multi-Z. The PR comes packed with unique
mechanics for future mappers (innate station traits!), a number of
map-fitting shuttles, and a fun spacefaring uniform gimmick for the
crew.

**This is my second attempt at bringing this map into rotation. It was
initially closed due to concerns about maptick and performance, as I
wasn't willing to push for a map to be added to the repository if it
didn't function to my own standards. I've been informed by a number of
coders far better than I that optimizations are arriving and enroute, so
I think it's time to dust her off and set sail for another journey.**

**Quick Disclaimer: Due to some design decisions disagreed upon by the
headcoder team and myself, the map will not be featuring unique
roundstart uniforms, and despite my design intentions, the innate
station trait features will be shelved for now.**

## Changelog
:cl: Cheshify, Fikou, Blue-Berry, Zytolg, InfiniteGalaxies, Striders,
Sylphet, Riggle, Soal, Andry, Crit, Deranging, and Pumpkin0.
add: Nanotrasen's Newest Exploratory Vessel is now available! Meet the
North Star!
add: More landmines, and a landmine random spawner.
add: energy barriers now have a regenerative subtype, fit for permanent
installations.
code: Raised the number of possible level render to 4, check your
preferences if needed to be reduced.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Skyrat-SS13/Skyrat-tg](https://github.com/Skyrat-SS13/Skyrat-tg)@[bfb3967c90...](https://github.com/Skyrat-SS13/Skyrat-tg/commit/bfb3967c908682e21202312d8b30ec17ad65e549)
#### Sunday 2023-05-21 00:13:56 by SkyratBot

[MIRROR] Adds proper armor for security plasmamen. [MDB IGNORE] (#21268)

* Adds proper armor for security plasmamen. (#75156)

## About The Pull Request
It's kinda strange that security plasmamen has no proper armor and you
can just bully them with bottlesmashes. Literally.
Also suits had no wound armor for some reason, which considering that
mold dies without hand kinda silly too.
And helmets just had no armor besides 1 melee armor.
## Why It's Good For The Game
Plasmamen security won't die that easilly. I mean, still easy to kill
them, but not that much.
## Changelog
:cl:
balance: Security Plasmamen now have Security armor. No bullying them
with bottlesmashes anymore.
/:cl:

* Adds proper armor for security plasmamen.

---------

Co-authored-by: Helg2 <93882977+Helg2@users.noreply.github.com>
Co-authored-by: lessthanthree <83487515+lessthnthree@users.noreply.github.com>

---
## [the-og-gear/tgstation](https://github.com/the-og-gear/tgstation)@[b3f5dfae14...](https://github.com/the-og-gear/tgstation/commit/b3f5dfae1418d4ac24df666e00ca47aef08c9dad)
#### Sunday 2023-05-21 00:19:45 by san7890

Config Flag to Save Generated Spritesheets to Logs (#74884)

## About The Pull Request

I was helping someone debug some weird bug with spritesheets a bit ago,
and I didn't like having to manually comment out all of the `fdel()`
stuff in order to help visualize what the potential issue might have
been with the spritesheets on either their DM-side generation or their
TGUI-level display. I decided to add a compile-time level flag that will
automatically copy over any generated spritesheet assets (css and pngs)
to the round-specific `data/logs` folder for analysis when a developer
should need it.

I also had to switch around some vars and make a few new ones to reduce
how copy-pasta it might get and ensure standardization/readability while
also being 0.001 times faster since we benefit from the string cache
(unprovable fact).
## Why It's Good For The Game

It's incredibly useful to see the actual flattened spritesheet itself
sometimes when you're doing this type of work and you keep getting odd
bugs here and there. Also saves headache from having to clear out the
temp `/data/spritesheets` folder every time you comment shit out, as
well as having an effective paper trail for A/B testing whatever
bullshit you've got going on.


![image](https://user-images.githubusercontent.com/34697715/233516033-1f5dde1a-e549-4e5a-aa99-0d531b34fbb5.png)
## Changelog
Doesn't affect players.

---
## [Estellarium/Heroes_In_A_Get-Together_Shirt](https://github.com/Estellarium/Heroes_In_A_Get-Together_Shirt)@[4e076b9a94...](https://github.com/Estellarium/Heroes_In_A_Get-Together_Shirt/commit/4e076b9a94dde9850f7bb1ee23a3592fa41c3a38)
#### Sunday 2023-05-21 00:24:04 by Gibran dos Santos Porto

Combat Updates: Movement, Collisions, Melee Attacks, and more

feat: Added S_CharacterStyleset, wich is used to obtain a colletction of the character's visual elements, like color palettes, rich text styles, portraits, etc.

feat(Dialogue): Added features to dialogue system
-setting the ui style and text styles based on the speaking character
-The dialogue box will set the ui colors and text styles based on the speaking character
|-These will come from a data table of S_CharacterStyleset
-Including the & symbol in the markdown will skip a line
-Pressing the 'next' button finishes the current dialogue before passing to the next
-Opening a dialogue will now muffle any ambient sound in the level (if it is coming from an Ambient Sound actor)

feat(Dialogue): Added dialogue events
-They can be placed in the level to start a dialogue upon entering
-note: Idealy they should pause the rest of the game when opening dialogue, but using "PauseGame" does not work well with the text box, since it uses delay nodes

feat(Popups): Added a base popup widget
-Can either be closed automatically or require a button press

feat(Tutorial): Added tutorial events
-Can be placed in the level to open a tutorial popup
-The popup text can include one of the button icons from the TextImages datatable

feat(Combat Collision): Added custom collision object types and collision presets
-They represent each object that needs custom collision behavior during combat:
|-Hero, Enemy, HeroShield, HeroMelee, HeroProjectile, EnemyMelee, EnemyProjectile, Environment

refactor(Projectiles): Modified the Projectile Shooting Component and the base Projectile class
-The SetVariables function wich was only in the Empty projectile class has been moved to the base class
-A new spawning method uses a composite struct with either the class and/or the projectile struct
-This new composite struct is used to store projectile data in a data table
-The projectile class now reads the collision profile from the composite struct
-A boolean variable now controls wether the projectile destroys itself on impact or keeps moving until it's lifespan ends
-There's a very short delay before self-destroying when hit so that other actors can gather data from the projectile on impact
-The projectile hit now triggers corretly the custom damage function
-Added data table for projectiles, to be referenced by both the heroes and the enemies

fix(Enemy Movement):
-Fixed the functions "GetRandomPointInCircumference" and "GetRandomPointBetweenCircles", they now return the expected results
-For better movement, the ChaseMovementUpdate timer default value has been increased, slowing down the chasing pathfinding
|-Chasing movement may still be updated to only pathfind to it's side relative to the player

feat/refactor(Enemies): Added enemy functionality
-Melee Attack action has been implemented, works best by having a Range Condition with a small enough radius
-Custom Function action
-The implementation of the rest of the planned conditions, targets and procedures is yet to be completed
-Implemented toggleable random spread for enemy projectiles
-Some prototypes of the enemy types "Angry Dog", "Annoying Bard" and "Panflet Giver" are positioned in the personal tests level

feat(Melee Attacks): Added melee attack actor
-Spawned when an melee attack occurs, overlaps the corresponding targets according to the collision profile and applies damage to them
-Can be spawned by both the player and the enemies
-Implements data from the MeleeAttackData struct
-Uses custom made collision meshes
-In the future will also pull data from a Datatable

feat/refactor(Heroes): Added and reworked hero functionalities
-Remade the HeroGroup movement to a basic generic tank: side-directional keys to rotate, front and back keys to move back and forward
|-This was made because the previous movement turned out to be complicated with movement collisions

-Shura's shield now detects both enemy projectiles and melee attacks, and blocks projectiles
|-note: It currently does not block melee attacks if they also overlap with Shura herself, to be fixed later

-Holding down the action key before releasing it will trigger the character's second action
-All heroes except Shura now have their primary action implemented:
|-Hanna's primary action is shooting a normal projectile, her second action is shooting a piercing shot that does not destroy itself when colliding, moves faster and causes more damage
|-Ethan's primary action is a normal melee attack
|-Benjamin's primary action is a small heal to all heroes (altough this can be changed later to be his secondary action)

-Implemented the heroes health
|-When a hero faints they cannot use any of their abilities
|-If all heroes faint the player loses the game and is brought to the game over screen
|-Ben can heal the other heroes back from fainting, but not if he has fainted himself
|-Currently they all have the same ammount of health (200), wich is double the default ammount of the enemies (100). All of the default health values of both heroes and enemies will be changed in the future

-Added a HUD with the heroes healthbars and ability cooldown indicators
|-The group healthbar is a combination of all of the heroes individual healths
|-The cooldown of both the first and second abilities of all heroes is shown
|-note: Currently it starts showing the second ability with no cooldown, to be fixed later

feat(Destructibles): Added the base Destructible Obstacle class
-Currently it is simply an object that blocks the heroes path until they destroy it

feat(SpriteVFX): Added SpriteVFX class
-Can be spawned during attacks or other situations
-Can play a random flipbook out of a set or a sequence of flipbooks
-They are currently spawned during the heroes attacks and when an enemy takes damage

refactor: Replaced several math checks for valid array indexes with IsValidIndex functions

feat/refactor(Localization):
-Changed native language in localization config to English

-Succesfully tested changing languages
|-A primitive widget to test changing languages is opened by pressing Cntrl
|-note: Changing language at runtime only works in Standalone Game mode, it does not work during PIE

-Changed localization settings to not gather code-only text
|-Code-only text being things like Enums, Tilemap Layer Names, debug Print Texts, etc.

-note: All dialogue texts are yet to be translated natively to english

feat(Widgets):
-Added a level start widget, wich shows the name of the current level and is to be created when the level starts
-Added a game over screen, wich is created when all heroes faint and is to restart the current level

feat(Art):
-Added several placeholder VFX spritesheets and animations, to be used primarily by the SpriteVFX class
-Added icon sprites for keyboard inputs, they can be used in RichText trough the TextImages datatable
-Added a sketch of some new tiles for the park level, not finished

feat(Sound):
-Added some placeholder sound effects for projectile attacks, melee attacks, and enemy damage
-Added a placeholder stage music for the park level (it will automatically play when starting the level)

refactor(Folders): Moved and reorganized hundreds of assets

style(Folders): color-coded more personal folders

style(Blueprints): reorganized and commented some blueprints

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[3fdd716da5...](https://github.com/DrDiasyl/tgstation/commit/3fdd716da5bfd2aab2be37489b4ac39f4be7e632)
#### Sunday 2023-05-21 00:28:19 by Cheshify

Tcomms Soundloop Comes From One Source And Is Less Awful (#74908)

## About The Pull Request

The ``soundloop/server`` now only comes from the server hub, so it
doesn't have stacking audio sources. The sound has been made more
uniform when up close, but is overall quieter. Additionally, all the
files have been run through a low pass filter to remove the highest of
it's pitches.
## Why It's Good For The Game

I'm sick of not wanting to be around telecomms because of how bad every
single machine sounds. Now, things are significantly easier on the ear,
quieter, more uniform, and better for everyone's sanity. I asked the
maintainers in the coding channel if I could just remove it and they
said no.

I can't get a video recording, I've tried with win+G, OBS, and sharex
and it's just fucked.
## Changelog
:cl:
qol: telecomms is quieter and less ear-damaging.
sound: modified tcomms sound to remove high-tones.
fix: the telecomms sound only comes from the server hub machine.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [DrDiasyl/tgstation](https://github.com/DrDiasyl/tgstation)@[43473a4dac...](https://github.com/DrDiasyl/tgstation/commit/43473a4dac07c40faed45808b61b9c6de46ffcb6)
#### Sunday 2023-05-21 00:28:19 by san7890

Turns Deer into Basic Mob - They Freeze At The Sight of Vehicles (#74784)

## About The Pull Request

deers only show up in the BEPIS but i decided that they would be easy
enough to turn into a basic mob (they were). it was so easy in fact that
i decided to dip my toes into coding AI behavior, and made them freeze
up whenever they see a vehicle. this required a lot of code in a bunch
of places that i was quite unfamiliar with before starting this project,
so do let me know if i glonked up anywhere and i can work on smoothing
it out.
## Why It's Good For The Game

one less simple animal on the list. deers staring at headlights is
pretty cool i think, neato interaction for when you do get them beyond
the joke the bepis makes

i'm also amenable to dropping the whole "deer in headlights" code if you
don't like that for w/e reason- just wanted to make them basic at the
very least
## Changelog
:cl:
add: If you ever happen upon a wild deer, try not to ride your fancy
vehicles too close to it as it'll freeze up like a... you know where I'm
going with this.
/:cl:

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Overuseddart/tgstation](https://github.com/Overuseddart/tgstation)@[dc2f52e386...](https://github.com/Overuseddart/tgstation/commit/dc2f52e386e0ef3cfcc2133293cd3f68f6a1eee3)
#### Sunday 2023-05-21 00:28:48 by tralezab

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
## [Overuseddart/tgstation](https://github.com/Overuseddart/tgstation)@[48183ec0ff...](https://github.com/Overuseddart/tgstation/commit/48183ec0ffd67ea5afa26c6f6e58e81edff98d52)
#### Sunday 2023-05-21 00:28:48 by san7890

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
## [Overuseddart/tgstation](https://github.com/Overuseddart/tgstation)@[b5ebf5c942...](https://github.com/Overuseddart/tgstation/commit/b5ebf5c9423cb3b39a2b9cfb6524b157dc6cb4b2)
#### Sunday 2023-05-21 00:28:48 by Helg2

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
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[11cbbba018...](https://github.com/Xander3359/tgstation/commit/11cbbba018e861237ce4bed73f19b58874c22042)
#### Sunday 2023-05-21 00:29:59 by Sol N

Replaceable Traitor Uplinks (#74315)

## About The Pull Request

Following [from the suggestion in this hackmd
](https://hackmd.io/IkDWWkpfQa2lkdevsnLqhA?view#Replacement-Uplinks)with
a few twists of my own, I have made a method for traitors to acquire a
replacement traitor uplink that has its own set of flaws and limiters in
order to prevent abuse.


![ZC0WYDFRzc](https://user-images.githubusercontent.com/116288367/228101432-9352390b-9538-4c62-8dc4-55e2e798c466.png)

The basic pitch is as follows, all traitors now start with a new,
crafting recipe exclusive to them, it costs a teleport beacon, a
bluespace crystal, and some iron and cable coil, and then allows them to
build a static, dense machine that they can synchronize with, which
allows the machine to know what signal it should be looking out for from
the traitor.

![dreamseeker_iErI3vju0C](https://user-images.githubusercontent.com/116288367/228094286-c2bca198-82cd-4ce0-a4a7-c26c24a9327c.gif)

The traitor then uses any radio, sets it to the frequency that has been
added to their static antagonist ui, and then speaks their codeword,
also in the ui, and then a few things happen.

![dreamseeker_gbzSFeHuS5](https://user-images.githubusercontent.com/116288367/228094354-a649c713-f013-4ac2-b8d7-0754a852f987.gif)

Most obviously, they get a replacement uplink that is in the conspicuous
shape of the nukie or lone op uplink. This uplink can be unlocked by
speaking your replacement codeword to it again, it remembers your
previous TC amount and locks all other uplinks associated with your
uplink handler(they can then be unlocked as normal). It also destroys
any other replacement uplinks associated with your uplink handler, which
means you can never have more than one replacement uplink.

This means that if your uplink has been confiscated and you left it
unlocked, if it hasn't been emptied out you can continue from where you
were, and if you want to get back on the TC grind you won't lose the new
TC to whoever stole your uplink. Of course, the new uplink can not be
locked, so you have to be more careful with it or buy an uplink implant
and destroy it. You can destroy your replacement uplink with a
screwdriver right click, same for the machine.

Additionally, the Syndicate Uplink Beacon has another quirk to it, which
is that the teleporter beacon used to create it is intact, which means
people eagle eyed on the teleporter console could go find you, not to
mention that if you use an existing teleporter beacon, someone might
notice its gone missing...

oh also while making the replacement uplink i found a bug caused by a
recent pr that broke debug uplinks due to them not having a purchase
log. thats fixed too

## Why It's Good For The Game

It can be easy to lose your uplink, and as a traitor having your uplink
confiscated, even if it is locked, feels really bad. While the old
traitor objectives were added back to prog traitor to prevent situations
where a confiscated uplink meant that you were completely aimless, I
think that having a backup solution would be good for more inexperienced
traitors or for ones who get unlucky.

Hopefully this is generally balanced well enough but there are a few
levers that can be pulled, but overall I do think that making it so that
traitors can always get a chance to get an uplink and do some objectives
is good for the game. I like the idea of someone getting perma'd,
someone breaks them out, they both craft a new uplink beacon, and then
they go back and get the traitors old gear with stuff they got from the
new uplink, I think that's a cool possibility to throw into the sandbox.

## Changelog
:cl:
add: Added new syndicate uplink beacon and associated systems that allow
you to get a replacement traitor uplink
fix: Debug & nukie uplinks no longer runtime and work properly again
/:cl:

---
## [Xander3359/tgstation](https://github.com/Xander3359/tgstation)@[00f8bcfe75...](https://github.com/Xander3359/tgstation/commit/00f8bcfe75275b7452063d1d8ec75d4c8e643f8b)
#### Sunday 2023-05-21 00:29:59 by MrMelbert

Moves revolution code of out of flash code, fixes April Fool conversion forcesay never working in any cirumstances (#74411)

## About The Pull Request

- Signallizes head revolutionary flash conversion code, moving it out of
core flash code.
- Removes "tacticool" flashing from head revs, but they can still
convert from any direction
 
- Fixes April Fools "You son of a bitch! I'm in" force say never
working.
   - Revs are muted on conversion so they couldn't talk.
       - Fixed by only muting revs on non-holidays
   - Cultists are unconscious on conversion so they couldn't talk
       - Fixed by only unconscious-ing cultists on non-holidays
- Brainwash victims are more often than not unconscious / asleep so they
couldn't talk
       - Just left this one. 

- Reduced the chance of them occurring and limits it to April Fools only
- A 1% chance of the force says ocurring means they will happen pretty
much once a week, given multiple rev / cult rounds happen every week and
on average like, 20 people are converted. A little absurd, it's good
that it never worked?

## Why It's Good For The Game

Antag code in core item code is bad

It's funny this meme has existed for like 2, 3 years now? No one's
tested it, it's never worked

## Changelog

:cl: Melbert
refactor: Removes Rev code from core flash code
fix: Getting converted on April Fools now triggers the meme force say as
always intended
del: The meme force say can no longer trigger on any day (it didn't work
before anyways)
/:cl:

---
## [toolmind/cmss13](https://github.com/toolmind/cmss13)@[4cf0651670...](https://github.com/toolmind/cmss13/commit/4cf06516705b3e0f4a6f446cd36eaa15b554a561)
#### Sunday 2023-05-21 00:30:50 by BlackCrystalic

Fixes queen stat bug (#3168)

# About the pull request

Good morning VIETNAM!
That again happened! We found some mistake!

# Explain why it's good for the game

That not good for game, because I fixend so usual staff, like timer for
queen, he can abuse that to make engage on last second and marines -
bruh, young queen, FIGHT! and BANG! Screech on ALL marines... Stupid
folks.

(devs trying to find and fix bugs)
https://www.youtube.com/watch?v=ryNSpF9I3rE

# Changelog

:cl:
fix: Stat proc replaced with get_status_tab_items, fixed issue with
QUEEN additional status
/:cl:

Co-authored-by: BlackCrystalic <blackcrystalic@inbox.ru>

---
## [toolmind/cmss13](https://github.com/toolmind/cmss13)@[b451aba2d4...](https://github.com/toolmind/cmss13/commit/b451aba2d4fd87a3b5cceaaba6955b8b783f84b2)
#### Sunday 2023-05-21 00:30:50 by Hopekz

Fix a start now error and add the ability of queuing the start of the game (#3090)

This PR does two things.

Fixes this error when trying to start early

![dreamseeker_lIUnkd0lFZ](https://user-images.githubusercontent.com/24533979/232609965-5cf94825-0671-420b-8625-16f505f26d63.png)


And adds queuing meaning that if an admin wants to start a game early
during loading; it will now tell them that the game will launch as soon
as it is available then waits for the game to be ready before starting.

Before this PR it just tells you that the game isn't ready then you have
to wait for it to load and launch the "start now" command again.

Does not bypass the "are you sure?" check because it has been moved to
the front.

Honestly made this PR because I hate waiting for the start I just want
to do it once when I see the game window then step away for like a
minute instead of having to wait for it.


:cl: Hopek
add: Adds the support for queuing the round start meaning that if an
admin pressed "start now" it will actually wait until the game is loaded
then immediately start the game as expected versus telling you to try
later.
fix: fixed the "start now" verb displaying that the game has already
started when it is loading because it didn't understand how to read the
game state properly.
/:cl:

---------

Co-authored-by: harryob <me@harryob.live>

---
## [ArcaneDefence/tgstation](https://github.com/ArcaneDefence/tgstation)@[54bf3808b8...](https://github.com/ArcaneDefence/tgstation/commit/54bf3808b80ec8ef83bee4062d2361e9f38d8ae8)
#### Sunday 2023-05-21 00:32:19 by SyncIt21

Stops station blueprints from expanding areas of non atmos adjacent turfs. (#74620)

## About The Pull Request
Fixes #74605

the problem starts with `detect_room()` proc. This proc returns turfs
even those with `atmos_adjacent_turfs` = null. This means it returns
turfs that has a wall, airlock, window etc i.e. whatever that stops air
from flowing through it. This coupled together with `create_area()`
causes some wierdness.

Let's take an example
![Screenshot
(154)](https://user-images.githubusercontent.com/110812394/230769831-e84819f2-31b2-4a67-a8bb-5e07e1c5a1cc.png)

Area A is well defined i.e. it has been created via the station
blueprints and is highlighted in green, Area B however is only
theoretical i.e. we haven't created it yet or we are about to create it.
Now you might be thinking Area A is completely walled & sealed off, it
should be physically impossible to expand it unless we broke down one of
it's walls and so since we are standing in Area B it shoudn't even give
me the option to expand area A Right? right? r.i.g.h.t?
![Screenshot
(155)](https://user-images.githubusercontent.com/110812394/230770056-169cbab3-4516-4da7-ae2c-4f40b50be9ba.png)
Well PHFUUK. The area editor completely ignores the laws of physics and
allows me expand Area A anyway. This could cause some real power gaming
shit because if you create an area next to an area having an APC you
could use that area power without even making your own apc by simply
expanding that area(like using someone else's wifi from outside their
house without them even knowing)

#73850 accidently built on top of this as it relied on this to detect
duplicate APC's but the checks became way too strict as it would check
areas of surrounding walls for apc's and throw the conflicting apc
error. You can now build room's next to each other even if they have
fuctioning apc's however you still can't build rooms in space on top of
shuttle walls because that's been the default behaviour for years and
hasn't been touched one bit.

## Changelog
:cl:
fix: station blueprints no longer expands & detects areas of non atmos
adjacent turfs.
/:cl:

---
## [kidgenius703/tgstation](https://github.com/kidgenius703/tgstation)@[2b2cb3dff6...](https://github.com/kidgenius703/tgstation/commit/2b2cb3dff6d9985103cee46a6020aa1b63a3c2de)
#### Sunday 2023-05-21 00:32:20 by LemonInTheDark

Hologram Touchup (Init savings edition) (#74793)

## About The Pull Request

### Polishes and Reworks Holograms

Hologram generation currently involves a bunch of icon operations, which
are slow.
Not to mention a series of get flats for the human models, which is even
worse.

We lose 0.05 seconds of init to em off just the 2 RCD holograms. it
hurts man.

So instead, let's use filters and render steps to achive the same
effect.

While I'm here I'll dim the holo light and make it blue, make the
hologram and its beam emissive (so they glow), and do some fenangling
with move_hologram() (it doesn't clear the hologram off failure anymore,
instead relying on callers to do that) to ensure holocalls can't be
accidentially ended by moving out of the area.

Ah and I added RESET_ALPHA to the emissive appearance flags, cause the
alpha does override and fuck with color rendering, which ends up looking
dumb. If we're gonna support this stuff it should be first class not
accidential.

### Makes Static Not Shit

While I'm here (since holograms see static) lets ensure the static plane
is always visible if you're seeing through an ai eye.

The old solution was limited to applying it to JUST ais, which isn't
satisfactory for this sort of thing and missed a LOT of cases (I didn't
really get how ai eyes worked before I'ma be honest)

I'm adding a signal off the hud for it detecting a change in its eye
here.
This is semi redundant, but avoids unneeded dupe work, so I'm ok with
it.

The pipeline here is less sane then I'd like, but it works and that's
enough

## Why It's Good For The Game


![dreamseeker_zMiLXzlZ2X](https://user-images.githubusercontent.com/58055496/232470136-add945da-5f76-469e-ba1a-6ed3159b6f5b.png)
More pretty, better ux, **static works**

## Changelog
:cl:
add: Holograms glow now, pokes at the lighting for holocalls in general
a bit to make em nicer.
qol: You can no longer accidentally end a holocall (as a non ai) by
leaving the area. Felt like garbage
fix: Fixes static rendering improperly if viewed by a non ai
/:cl:

---
## [ynot01/tgstation](https://github.com/ynot01/tgstation)@[f10b0dd42a...](https://github.com/ynot01/tgstation/commit/f10b0dd42aa996971f472edb7e65b3e504cb7ec5)
#### Sunday 2023-05-21 00:36:12 by 13spacemen

Atmos QOL + Small Sprite Fix (#74251)

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

---
## [ynot01/tgstation](https://github.com/ynot01/tgstation)@[fe7ebd67cf...](https://github.com/ynot01/tgstation/commit/fe7ebd67cf74982038524ceb175377d7ff6c0486)
#### Sunday 2023-05-21 00:36:12 by LemonInTheDark

Properly accounts for byond tick fuckery in runechat code (#74388)

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

---
## [ynot01/tgstation](https://github.com/ynot01/tgstation)@[0a1f7e8de2...](https://github.com/ynot01/tgstation/commit/0a1f7e8de2fea2116b73f22a11fdf328763c503a)
#### Sunday 2023-05-21 00:36:12 by Hatterhat

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
## [necromanceranne/tgstation](https://github.com/necromanceranne/tgstation)@[56d960a763...](https://github.com/necromanceranne/tgstation/commit/56d960a7630d0b03bfcd59c073b29393a70a1891)
#### Sunday 2023-05-21 00:38:36 by GoldenAlpharex

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
## [CursedBirb/tgstation](https://github.com/CursedBirb/tgstation)@[3861627c66...](https://github.com/CursedBirb/tgstation/commit/3861627c66747fb27b18f8bf76a3c9dfd2023001)
#### Sunday 2023-05-21 00:42:40 by LemonInTheDark

Microing var/static times (~0.015 seconds of init) (#74769)

## About The Pull Request

Moth and I came up with an affront to god and man, and used it to track
the time spent creating /static (and in theory /global) variables (this
happens right at the start of init)
They cost as a sum about 0.05 seconds btw, at least currently.

```
/datum/timer
    var/key

/datum/timer/New(file, line)
    src.key = "[file]:[line]"

/datum/timer/proc/operator*(x)
    rustg_time_reset(key)
    return x

/datum/timer/proc/operator+(x)
    var/time = rustg_time_microseconds(key)
    world.log << "TIMER: [key]: [time]"
    return x

Regex:
var/static/([\w/]+) =
-> var/static/$1 = (new /datum/timer(__FILE__, __LINE__)) * (new /datum/timer(__FILE__, __LINE__)) + 
```

Output on moth's pc looks like this, time in microseconds

[output_sorted.csv](https://github.com/tgstation/tgstation/files/11241900/output_sorted.csv)

Most of this is either icon_states() memes (which appears to be cached
btw, that's interesting), or a variation on typecacheof()
There is one get_asset_datum call, but that is ALREADY cached and so is
just redundant. That's a good 0.01 seconds saved.

The rest of the time here is slightly more interesting.

The majority of typecacheof() is iterating the output of typesof(), a
byond internal proc that returns a list of types that either are or are
the child of the passed in type.
A decent chunk of time here (0.005 seconds, or 10% of the proc) can be
saved by unrolling the arguments to the proc.
It takes an arbitrary amount of typepaths as input, but we can't like
use arglist() here (cause this is an internal "proc"), so instead we try
a window of args, passing in null if we start to try and take in too
much.
Window size matters, zebra fits better into 4 then 5, especially because
of how grouping needs to work to make this effect happen.
We save about 0.001 for zebra btw, which is around about 7%. It's lower
cause we need to group the paths beforehand I think.

The speedup is minor, but it DOES exist. Plus it's fun.

## Why It's Good For The Game

Microing is a hell of a drug

---
## [Tristrian/tgstation](https://github.com/Tristrian/tgstation)@[c3b78761d2...](https://github.com/Tristrian/tgstation/commit/c3b78761d29c53558fd993c84bb808bd5783861d)
#### Sunday 2023-05-21 00:46:36 by tralezab

Adds Chuunibyou Spell + Granter (#74404)

## About The Pull Request

My April fools this year, though not going to call it one because some
people think it should just be actually merged.

### Chuunibyou Powers 🌟

Wizard gets a new spell for 2 points that gives him the powers of
chuuni. This makes them have ridiculous shouted invocations for all
their spells, their spells are colored pink, and they heal slightly when
casting one.

While mostly a meme spell, I could see a tailored loadout like lichdom
and splattercasting that takes advantage of the unique spellcasting
changes, like a very low cooldown spammable loadout to heal quickly.

There is also a granter book in the library, which teaches a version of
chunni that doesn't heal.

#### Medical eyepatch

I added it, chuuni wizards get a NODROP version.

## Why It's Good For The Game

This PR bestows upon the game the glorious gift of chuuni powers, the
ultimate manifestation of my hidden potential and the secret truth of
this world, which only I and a few chosen ones can comprehend and
unleash! Why wouldn't you want it?!

In all seriousness, it is a unique wizard playstyle and it will make for
some funny memes. Beyond wizard, the chaplain, heretics, or mime can
read it in the library for a very silly round. I like it!

## Changelog
:cl:
add: Chuunibyou wizards, and chunni granters in the library
add: Medical eyepatches
/:cl:

---
## [YakumoChen/Skyrat-tg](https://github.com/YakumoChen/Skyrat-tg)@[f97afbd66d...](https://github.com/YakumoChen/Skyrat-tg/commit/f97afbd66d6631bdb5355cbf54fe630e189e4d51)
#### Sunday 2023-05-21 00:48:54 by SkyratBot

[MIRROR] Fixes spoon overlay not updating every time [MDB IGNORE] (#20570)

* Fixes spoon overlay not updating every time (#74687)

## About The Pull Request

After bludgeoning myself one too many times with a spoon, here we are.

The spoon overlay wasn't updating to reflect that soup had been
consumed, which led to trying to eat it again and then pain.

Why do spoons hurt so much?

## Why It's Good For The Game

Less spoon related injuries.

## Changelog

:cl:
fix: spoon overlays will now update when you eat from them to reflect
that food = gone. it really is gone, you can stop beating yourself with
the spoon. oh god please stop--
/:cl:

* Fixes spoon overlay not updating every time

---------

Co-authored-by: Bloop <vinylspiders@gmail.com>

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[200b739c0a...](https://github.com/Comxy/tgstation/commit/200b739c0a0bbfff95dbfd697786013c92cb6cf6)
#### Sunday 2023-05-21 00:49:39 by Kyle Spier-Swenson

Refactors and defuckulates dbcore. Adds support for min_threads rustg setting, Reduce query delay, Make unit tests faster (#74852)

dbcore was very fuckulated.

It had 3 lists of queries, but they all had their own current_run style
list to support mc_tick_check (as it was already being done before with
the undeleted query check, so i can understand why they ~~cargo culted~~
mirrored the behavior) This was silly and confusing and unneeded given
two of those loops can only process at most 25 items at a time on
default config, plus these were cheap operations (ask rustg to start
thread, ask rustg to check on thread).

Because of the confusingness of the 6 lists for 3 query states, The code
to run pending/queued queries immediately during world shutdown was
instead looking at the current_run list for active queries, **meaning
those queries got ran twice.**

The queued query system only checked the current active query count in
fire(), meaning even when there was nothing going on in this subsystem
new queries had to wait for the next fire() to run (10 ticks, so 500ms
on default config)

Those have all been fixed.

the config `BSQL_THREAD_LIMIT` has been renamed to
`POOLING_MAX_SQL_CONNECTIONS` and its default was lowered to match
MAX_CONCURRENT_QUERIES .

added a new config `POOLING_MIN_SQL_CONNECTIONS`, allowing you to
pre-allocate a reserve of sql threads.

The queue processing part of SSdbcore's fire() has been made to not obey
mc_tick_check for clarity and to make the following change easier to do:

If there is less than `MAX_CONCURRENT_QUERIES` in the active queue, new
queries activate immediately.

(its ok that there are two configs that kinda do the same thing,
POOLING_MAX_SQL_CONNECTIONS maps to max-threads in the mysql crate, and
it seems to only be a suggestion, meanwhile MAX_CONCURRENT_QUERIES can't
do anything during init, which is when the highest amount of concurrent
queries tend to happen.)

:cl:
config: database configs have been updated for better control over the
connection pool
server: BSQL_THREAD_LIMIT has been renamed to
POOLING_MAX_SQL_CONNECTIONS, old configs will whine but still work.
fix: fixed rare race condition that could lead to a sql query being ran
twice during world shutdown.
/:cl:

I have not tested this pr.

---
## [Comxy/tgstation](https://github.com/Comxy/tgstation)@[773cc9542a...](https://github.com/Comxy/tgstation/commit/773cc9542a54837fc52b15eb09cc98d7226049fb)
#### Sunday 2023-05-21 00:49:39 by MrMelbert

Adds admin alert for revs created through traitor panel (#74862)

## About The Pull Request

So like, using traitor panel to make revs doesn't work. 

Revolutions live and die, currently, by the revolution ruleset datum
dynamic creates. It manages the hostile environment and also processes
to check whether either side should be winning or not.

This means that the revolutionary buttons in the traitor panel are kind
of noob-admin-bait. You press it for a funny revolution and then you
realize it's screwed when all the heads are dead and everyone's
stumbling around cluelessly

This has a proper solution, albeit somewhat difficult - separate out the
revolution from the ruleset, make admin spawned revs create a
revolution. I can do this but it's a lot of effort and this works in the
meanwhile

Pops up a TGUI alert when an admin presses "add revolutionary" in
traitor panel when there is no ongoing revolution. Simply enough, gives
them an alert that it will not work correctly. Lets them decide whether
they want to deal with that. (Because you can manually deal with it via
proc calls, if you've got code smarts.)

## Why It's Good For The Game

Stops admins from stumbling into the same trap without warning.

Can be removed in the future easily when revs are coded better. 

## Changelog

:cl: Melbert
admin: Adds a warning that spawning revs via traitor panel will not
function as expected.
/:cl:

---
## [Jackal-boop/tgstation](https://github.com/Jackal-boop/tgstation)@[d72ef99270...](https://github.com/Jackal-boop/tgstation/commit/d72ef99270f2697064681b3214f0569dcf38d526)
#### Sunday 2023-05-21 00:49:49 by necromanceranne

Goliath-Infused Tendril Hammer uses an internal cooldown for the its special attack instead of a universal click cooldown (#74159)

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

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [Jackal-boop/tgstation](https://github.com/Jackal-boop/tgstation)@[e75a1c00aa...](https://github.com/Jackal-boop/tgstation/commit/e75a1c00aa3bcf2658428a536997f2eca0f25028)
#### Sunday 2023-05-21 00:49:49 by san7890

Dogs will no longer harrass if they are buckled to a bed (comfy edition) (#74224)

## About The Pull Request

Before, dogs were somehow magically able to drag their bed to you while
barking at/chasing you. that's silly, let's fix it by checking if you're
buckled, and then aborting course if we're comfy on our little bed
## Why It's Good For The Game


![image](https://user-images.githubusercontent.com/34697715/227679914-62822f93-6646-4070-8ff7-4e140e1a291a.png)

Fixes #74082

the dog is BUCKLED. it can't move. probably a better fix to this somehow
on a very deep AI level but that wouldn't allow us to have such a
soulful message (as well as potentially rule out a myriad of edge
cases), so i'm proposing this one.
## Changelog
:cl:
fix: If you buckle a dog to a bed, it will no longer drag its bed as it
goes to bark at the mailman. It will instead be comfy and chilling, as
expected.
/:cl:

---
## [gonenoculer5/Gameserver](https://github.com/gonenoculer5/Gameserver)@[27d37cb0f4...](https://github.com/gonenoculer5/Gameserver/commit/27d37cb0f47d007d1159ad5af69ace39a50b003f)
#### Sunday 2023-05-21 00:50:12 by Gallyus

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
## [RikuTheKiller/tgstation](https://github.com/RikuTheKiller/tgstation)@[bd4392ab74...](https://github.com/RikuTheKiller/tgstation/commit/bd4392ab7463c383c7e2824f8a9b7d154ad7940c)
#### Sunday 2023-05-21 00:54:04 by Bloop

New inhand icons for light tubes, makes latex balloons craftable, and various other fixes/improvements (#74576)

## About The Pull Request

This ended up turning into a bit of a junk drawer of a PR I'll admit,
but there's really not a whole lot to it.

There are three parts:

### Part I - Inhand sprites for light tubes.

Adds inhand sprites for light tubes. No more cardboard tube placeholder.
This is self explanatory-they have unique sprites for all 3 states
(normal, broken, and burnt out). The broken version has sharpness now.

Also refactored light_items.dm a bit, it was using a bespoke proc called
`update` to do icon updates. Now it has been _updated_ to use
`update_appearance` instead.


![dreamseeker_6WC8vJMiBW](https://user-images.githubusercontent.com/13398309/230615134-31c51e94-cee5-4eef-ba63-c348a3b2debc.gif)

### Part II - Latex Balloons

Latex balloons, a very old piece of code that was full of typos, has had
some life breathed back into it. It is a fun little item, and I saw no
reason to let it rot. It can now be crafted using a latex glove and some
cable. Also, you can pop them using anything sharp... such as a broken
light tube! Aha!

We've come full circle.


![image](https://user-images.githubusercontent.com/13398309/230617764-3a304fd2-05d0-4b2f-b420-056a93c0dce3.png)

### Part III - update_inhand_icon proc

A new atom helper function, `/atom/proc/update_inhand_icon(mob/target =
loc)`

I was struggling to find an existing proc that could update inhand icons
of a mob that was holding any given atom, without necessarily having a
ref to the mob yet.

So I ended up writing one that did that, and finding the spots in the
code which were using a similar way of doing it (that is in fact how I
stumbled upon the latex balloon item).

...........But then Iearned of the
`/datum/element/update_icon_updates_onmob` component and ended up using
that instead. There are still some very niche cases where you might not
be able to use the component where the proc would come in handy however
e.g. in transforming.dm--and if anything, I think it could serve as a
good spot to leave a comment informing would be users of
`update_icon_updates_on_mob` as an alternative.

For that reason especially I thought it worth keeping. 

## Why It's Good For The Game

New inhand sprites, and a fun little craftable balloon. What's not to
like?

## Changelog

:cl:
add: latex balloons can now be crafted using a latex glove and some
cable. You can fill them with air using a tank. They also have a new
sound effect.
imageadd: light tubes have a new inhand sprite
fix: broken light tubes now actually have sharpness to them as they are
basically spikes of glass.
refactor: refactored latex balloon code
/:cl:

---
## [Jolly-66/dragon-station](https://github.com/Jolly-66/dragon-station)@[dad84df983...](https://github.com/Jolly-66/dragon-station/commit/dad84df983a5192877e82200666af3e7b2631552)
#### Sunday 2023-05-21 00:54:53 by SkyratBot

[MIRROR] Makes a whole bunch of wooden objects flammable [MDB IGNORE] (#20670)

* Makes a whole bunch of wooden objects flammable (#74827)

## About The Pull Request

This whole PR started because I realized that baseball bats are not
actually flammable which I found weird, then I looked at a whole bunch
of other stuff that really should be flammable but also isn't.

## Why It's Good For The Game

Makes wooden objects behave slightly more consistently? Honestly, most
of these seem like oversights to me.

## Changelog

:cl:
balance: The following structures are now flammable: Picture frame,
fermenting barrel, drying rack, sandals, painting frames, paintings,
spirit board, notice board, dresser, displaycase chassis, wooden
barricade
balance: The following items are now flammable: Baseball bat, rolling
pin, mortar, coffee condiments display, sandals, wooden hatchet, gohei,
popsicle stick, rifle stock
/:cl:

* Makes a whole bunch of wooden objects flammable

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [MrMelbert/tgstation](https://github.com/MrMelbert/tgstation)@[c27f9a6d9b...](https://github.com/MrMelbert/tgstation/commit/c27f9a6d9b9739baae09db063b6eb266d525772c)
#### Sunday 2023-05-21 00:56:01 by necromanceranne

Minor Nukie Thing: Bolt-action Sniper Rifle, balance coding, and some ammo changes (#73781)

## About The Pull Request

### The Rifle:
-The Sniper Rifle is now a bolt action. This replaces the 4 second fire
delay on the sniper rifle. This overall will improve the fire rate if
you're good at racking the bolt, but it will also feel less like you're
in a weird limbo of inaction while using the sniper rifle, since the
fire delay can be quite confusing to players not used to it. This can be
tweaked, like reducing the speed of the racking action, if it seems like
it is too much.
-The scope component now goes up to 50 tiles (or so), which allows you
to gain a significant sightline over an area. The reasoning for this is
simple. The component actually nerfed the overall range of the sniper
rifle's scope, so this should hopefully restore that somewhat. And
having such a huge sightline makes it much easier to utilize the
impressive range of the rifle. Currently, it's really only ideal for
extremely close range fighting.
-The normal sniper rifle, the one that syndicate base scientists get,
can be suppressed. I don't know why it was different.

### The Ammo:

Normal .50 BMG: Does much more object damage, and on top of that deals
additional damage to mechs, but not by much more. Now, when it
dismembers a limb, it also deals its damage to the chest. This ensures
that you didn't straight up lose out on dealing a killing blow because
you took their limb off, and makes the dismemberment property of .50 BMG
a significant upside rather than a immense detriment.

Marksman: Gains a lot of the above benefits, but has much lower range.
Why this nerf? It's actually because of some funny nonsense with how
ricochet works. Which can cause....accidents to happen. To you. Consider
that firing down a straight line and missing could be quite embarrassing
when the bullet has 400 tiles of range.

Soporific: Now called Disruptor ammo. Works as it did before, putting
humans to sleep for 40 seconds (seriously, 40 seconds). Also deals some
stamina damage, if...that's relevant. But now also causes an EMP effect
and a boatload of added damage to both mechs and borgs, allowing it to
be an excellent anti-mech and anti-borg ammo type, as well as scrambling
any pesky suit sensors, energy weapons and so on in an area around the
impact. Useful for support fire.

Incendiary (NEW!): Causes a massive firebomb to go off where it impacts
(no explosion, so this isn't a stun). Also sets the target on fire,
which is always fun. Good for shooting into groups of people with
impunity. Also deals burn damage instead, since I think nukies could use
more methods for direct fire damage.

Surplus (NEW!): It's .50 BMG but it lacks most if not all the upsides.
No armour penetration, no dismemberment, no paralysis. It still deals a
lot of damage to objects, so not a bad option for simply removing
structures from afar. So what's the point in this ammo? You can buy 7
magazines for the price of one. I want to introduce 'Surplus' as an idea
for nukies to invest in if they want to be able to keep shooting but
they're really on a budget, like most non-warop nukies tend to be. This
is definitely subject to change (like a damage decrease on top of
everything else).

Pricing and Capacity: Normal ammo and surplus costs 3 TC. Every special
ammo costs 4 TC. Every special ammo also has the same ammo capacity as
the normal magazine. It's kind of weird how most of the subtypes had 5
shots rather than 6, but then soporific had...3? I don't get it. This
would probably cause a good deal of confusion, especially if you are
swapping ammo types and weren't aware of this particular oddity.

Anyway, 6 shots.

### Minor Addition
Gets rid of the cheap suppressor. It lies to players, tricking them into
thinking this is a low quality suppressor. Newsflash, it isn't. There is
no distinct difference between that suppressor and the normal
suppressor.

## Why It's Good For The Game

The sniper rifle, unfortunately, sucks a lot except for very specific
use cases. It got a big nerf with the scope component in terms of range,
even if the functionality is way cooler. And, at a baseline, there was
some counterintuitive functions attached to it. Dismemberment was cool,
but it also caused a loss in overall damage due to how limbs contribute
to core health. On top of this, the cool ammo types were...not much
better? Penetrator was almost always the best option, even if it lost a
lot of damage as a consequence.

So, what was it good for? X-ray + Penetrator. Pretty much, that's it. It
has some other uses but if I had to be entirely honest, there wasn't
much that other weapon couldn't do as well.

Hopefully this helps things going forward, and I want to mess with this
as well down the line in case its a bit too much of a boost in power.

Absolutely please rip this PR apart.

## Changelog
:cl:
balance: Makes the syndicate sniper rifle a bolt-action rifle.
balance: Sniper rifles have a scope range of roughly 50 tiles.
balance: Sniper rifle ammo, if it dismembers your limbs, does damage to
the chest.
balance: All the various syndicate sniper rifle magazines have
consistent casing quantities (6 shots). They also have more consistent
pricing. 3 for normal and a box of surplus, and 4 for every other type.
balance: Reduces the range of Marksman ammo to 50 tiles. Not because it
is strong, but because you might accidentally shoot yourself if you're
not watching where you're shooting. Ricochets are no joke.
add: Replaces Soporific with Disruptor ammo. Works like soporific, but
also EMPS things it hits.
add: Adds Incendiary .50 BMG. Causes a combustion to erupt from the
struck target, as well as setting targets on fire. Great for parties.
add: Adds Surplus .50 BMG. It sucks, but you get a lot of them! Quantity
over quality, baby.
remove: The suppressors in the bundle are of standard quality. The
apparent 'cheap suppressor' that came bundled with the C-20r and sniper
rifle were found to actually be 'fine'. Trust us.
/:cl:

---
## [Bm0n/tgstation](https://github.com/Bm0n/tgstation)@[e1221c986f...](https://github.com/Bm0n/tgstation/commit/e1221c986f5da2551051f47aa0fbd1d49e367c9b)
#### Sunday 2023-05-21 00:56:01 by san7890

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
## [Aerden/tgstation](https://github.com/Aerden/tgstation)@[c0ef4ba907...](https://github.com/Aerden/tgstation/commit/c0ef4ba907b28e1288f2ccbbc6714d15a923b1bd)
#### Sunday 2023-05-21 01:04:00 by tralezab

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
## [Aerden/tgstation](https://github.com/Aerden/tgstation)@[ccef887efe...](https://github.com/Aerden/tgstation/commit/ccef887efec2cb3025228210bcb134700aac5175)
#### Sunday 2023-05-21 01:04:00 by san7890

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
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[997dac9616...](https://github.com/DATA-xPUNGED/DataStation/commit/997dac9616768643cfa9ddce53432d684e196fb1)
#### Sunday 2023-05-21 01:05:06 by necromanceranne

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
## [TeDGamer/cmss13](https://github.com/TeDGamer/cmss13)@[d728da3e02...](https://github.com/TeDGamer/cmss13/commit/d728da3e02664297050d82dc01c87414c61345ef)
#### Sunday 2023-05-21 01:06:22 by Puckaboo2

Healer Balance Changes (#2896)

# About the pull request
This pull request addresses the boring and low-risk gameplay of the
Healer drone, who spends half the round sitting next to recovery nodes
and recovering her health so she may use it again, rinse and repeat
until a rine notices said drone has purple on it and booms her.

First, by changing her health from 600 to 500, Healer can spend more
time healing her sisters than sitting through another 100 health to heal
herself. Though this makes her less tanky than before, healing classes
are not known to be tanks. To ensure Healer can still heal five times
without depleting too much of her health whilst still giving her sisters
a decent amount of heals, I made her ability cost 75 health instead of
100, and also made her ability cost 200 plasma. Since Healer replenishes
plasma much more quickly than her health, she can still put herself into
crit if she heals too frequently. Due to this buff, her heals had a
slight nerf, being 10 damage a second for ten seconds instead of 12
damage per second for ten seconds for a total of 20 less damage healed
per application overall.

In addition to these changes, I'm giving Healer a better plasma transfer
for when she has nobody else to heal/nowhere else to weed and she has an
opportunity to assist her sisters. While a normal drone transfers 50
plasma with a delay of 20, Healer transfers 100 with a delay of 15,
which is nowhere near Hivelord's gargantuan 200 plasma with a delay of
5, but it still is better than a normal drone.

Finally, to give the huggers and larva some love, Healer will
specifically heal little ones 1.5 health per second for 10 seconds for
15 of her own health and 30 plasma.

# Explain why it's good for the game
Healer drone isn't fun. You run around and heal a bunch of T3s, then sit
out for half the battle trying to heal that massive 600 heath while you
wonder why you take so long to heal even though you have Strong
pheromones. You cry to mom for help, but she doesn't have time to heal a
drone who can't build walls and has no need to weed at the moment. You
think, 'screw it, I'm going to make a recovery node and camp here until
I heal', but by the time you finish healing, several T3s and a silly
rouny just suicided into a wall of talls and destroyed your recovery
node, so you run off and make another one. But oh, someone noticed you
have purple on your carapace and decide your location is precisely where
a shell should land, right as you're building one.

No more. These changes allow Healer to move around at her leisure and
makes Healer more engaging by allowing her to be a more front-line
participant and actively run around and heal her sisters without having
to incur such a harsh penalty.

Let this be a testmerge, please.

# Changelog

:cl: Puckaboo2
balance: Healer Drone's health was reduced to 500 from 600.
balance: Healer's damage has been increased to 17 from 12 and the tackle
damage debuff has been halved.
balance: Healer Drone's Apply Salve ability now costs 75 health and 200
plasma, down from 120 health and up from 0 plasma.
balance: Healer Drone's Apply Salve ability now heals 10 damage per
second for 10 seconds, down from 12 damage per second for ten seconds.
balance: To prevent spam healing between Healers, Apply Salve costs 100
health instead of 75 health when Healer heals another Healer. Much
healing.
balance: Healer has an improved Transfer Plasma that gives 100 plasma
instead of 50, with a 25% shorter delay.
balance: Healer will heal huggers and larva for 1.5 health a second for
10 seconds, costing 15 health and 30 plasma.
tweak: Healer will now face the xeno she is healing if she was not
facing their direction before.
spellcheck: All instances of VERYSMALL and VERYLARGE have been renamed
to VERY_SMALL and VERY_LARGE.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Morrow <darthbane97@gmail.com>

---
## [Cyberboss/tgstation](https://github.com/Cyberboss/tgstation)@[2068ea9ab5...](https://github.com/Cyberboss/tgstation/commit/2068ea9ab53803557b5e48cddbe57205f4c4792e)
#### Sunday 2023-05-21 01:08:01 by SyncIt21

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
## [IndieanaJones/tgstation](https://github.com/IndieanaJones/tgstation)@[66cb695343...](https://github.com/IndieanaJones/tgstation/commit/66cb695343721087437e651d07268e284e25763d)
#### Sunday 2023-05-21 01:12:40 by carlarctg

IV drips' default transfer rate is no longer zero. (#74724)

## About The Pull Request

Set default IV transfer rate to maximum (5) instead of 0.
## Why It's Good For The Game

> Set default IV transfer rate to maximum (5) instead of 0.

When you hook someone onto an IV drip, you naturally expect that to be
the end of the process - you hooked someone to a drip, and now you can
go about your day. Them needing to fiddle with buttons is bad for
several reasons:

- It is unintuitive.
IV drips don't look like machines. Their sprite doesn't reflect the fact
that you need to fiddle with the settings before they can work the same
way any other machine or computer might. And to be honest, they
shouldn't.
- It is separate from how every other server currently has it.
Yes, yes, I know that argument is very flawed and full of holes. But
what I'm trying to say with it is, effectively speaking, an extension of
the above point. In other servers, you drag-click someone to an IV drip
and there we go, it's functional. In TG, it just-so-happens to not be
functional due to what is almost definitely a recent oversight, which
very much can, has, and will lead to unnecessary frustration.
- There is no practical reason for it to be set at 0.
Imagine if chem dispensers started at +0 units and needed to be set to
+5 to continue. Or if bottles had a transfer rate of 0u. Or if guns
started with their safeties on. Even if it made sense, it would just be
frustrating and needless, and wouldn't improve the game in any
significant manner enough to offset frustration. We're here for fun, not
perfect balance or realism/verisimilitude after all.
- It's an oversight.
It was changed in #71217. Before that, it was always set to the maximum,
5u. However, presumably due to confusion (Variables that can be adjusted
ingame usually are set to zero/the minimum possible) it ended up being
changed to this.

Apparently an argument can be made that this is fine because fumbling to
get medical aid done is a part of the game. I disagree heavily - blood
bags are already stored in the cold room, something only 2/5 of the
roles in medbay even have access to, with the paramedic, virologist,
chemist all being unable to reach it. This is already enough 'fumbling'
that's necessary. If someone moved the blood bags outside the cold room
next to the IV drips, then all the better - it's a reward for medbay
being prepared.

However I wouldn't mind if someone asked me to make it so the default
transfer rate is, well, something below maximum. It's common practice in
a lot of parts of SS13 to have things set in an unoptimized state so
players can go around improving them, such as air alarms, cryogenics,
etc. Just as long as it's not literally unusable otherwise, as the
'minimum basic setup' should just be slapping on a blood bag!
## Changelog
Dunno what to put here TBH. Can't tell if it's qol, fix, balance, etc.

:cl:
qol: Set default IV transfer rate to maximum (5) instead of 0.
/:cl:

---
## [Paxilmaniac/Skyrat-tg](https://github.com/Paxilmaniac/Skyrat-tg)@[bad4c9168c...](https://github.com/Paxilmaniac/Skyrat-tg/commit/bad4c9168c3ccf04effadc09b3d1b1a817fbfbf6)
#### Sunday 2023-05-21 01:17:04 by SkyratBot

[MIRROR] Mafia rebalance and backend refactor [MDB IGNORE] (#20631)

* Mafia rebalance and backend refactor (#74640)

## About The Pull Request

Turns all Mafia abilities into datums, instead of being a bunch of
shitcode on every single job.
This means it's easier to add new roles
Gives new names to some defines (such as the signal order, to make it
easier to tell when something is fired)
Adds support for modular Mafia jobs with their abilities being in a
certain order (Escort is now properly first).
De-snowflakes Changeling killing abilities and day voting, they're now
actions that are tallied when necessary.

Turns time vars into defines
Generalizes a lot of behavior for abilities, now all abilities can
properly undo their action at night

Fixes problems with the UI (Thoughtfeeder had 2 buttons during night and
they overlapped with names, that's been fixed).

### Behavior changes

- Doctor/Officer can now protect themselves 1 night, because it gives
them a way to protect themselves.
- Lawyer/Warden/Ect now choose their abilities at night, rather than the
day before. The suspense building up towards the end of the night is
part of the game, telling you that it happened at the very start is
quite lame (in the case of Lawyer, anyway).
- Admin setup now uses TGUI instead of html inputs.
- Cut night time by like, 5 seconds, because I found it a little long
lol.
- HoP doesn't count as votes to win until they reveal, because it makes
no sense an unrevealed HoP has their unrevealed votes tallied. I also
like those 1v1 Mayor V. Evil scenarios where dead chat goes crazy, and
hope to replicate that here.
- Mafia now needs 6 people to start instead of 4, because 4 players is
just not enough to play a Mafia round that will do anything but annoy
people.
- The game no longer ends if it's in a standoff with 1 Town, 1 Mafia,
and 1 Neutral, as you've got a kingmaker and they should decide who
wins.

### Things I want to change in the future
Every time night starts/ends, it checks the entire ``GLOB.airlocks`` for
doors with the "mafia" ID. This is stupid.
Rework ``check_victory()`` to make it make more sense, and be more fun
for players.
A visible death animation?
I want to use something similar to admin popup for messages about people
being on stand, and decluttering the UI in general
Also more use of balloon alerts instead of to chat messages for
everything.
Also also, making the UI more responsive to players. Button should be
red when a player is selected, so they know that's who they've selected,
if they want to unselect.
Are votes public when you first cast them? They shouldn't be wtf.
Can we also make the description for roles not be a to chat message? It
can just say when you hover over the '?' come on.
User-written wills instead of auto-generated, and able to send them in
chat
Add support for roleblock-immune roles

## Why It's Good For The Game

Updates a lot of old code to modern standards
Makes it considerably easier to work with Mafia and add new roles
Makes things less prone to breaking as easily.
Code also looks a lot cleaner now.

## Changelog

:cl:
refactor: [Mafia] All Mafia abilities have been overhauled in the
backend, it's now much easier to understand what each role's ability can
do and how it works.
admin: [Mafia] Admin setup of Mafia is now in TGUI
balance: [Mafia] Doctors/Officers can protect themselves once per game.
Be careful around them!
fix: [Mafia] Thoughtfeeder's UI buttons at night won't overlap with
eachother.
fix: [Mafia] HoP's votes now actually matter, instead of being purely
visual.
qol: [Mafia] Lawyers, Wardens, etc. now perform their night ability at
night, instead of the day prior.
qol: [Mafia] Night time now lasts 40 seconds instead of 45.
/:cl:

* Mafia rebalance and backend refactor

---------

Co-authored-by: John Willard <53777086+JohnFulpWillard@users.noreply.github.com>

---
## [Vexylius/tgstation](https://github.com/Vexylius/tgstation)@[c18b1ef442...](https://github.com/Vexylius/tgstation/commit/c18b1ef4423fc7d9083adac9b51aab4f169ea8aa)
#### Sunday 2023-05-21 01:22:03 by tralezab

End of Mapping March (Thanks to everyone who contributed, you're amazing!!!) (#74417)

## About The Pull Request

Removes the special mapping template. We got a really good turnout this
year! Will start counting ckeys and all that.

### But my mapping pr isn't done yet!

If it was opened during march, you'll get your token, don't worry

---
## [linuxppc/linux](https://github.com/linuxppc/linux)@[1bba82fe1a...](https://github.com/linuxppc/linux/commit/1bba82fe1afac69c85c1f5ea137c8e73de3c8032)
#### Sunday 2023-05-21 01:43:10 by Darrick J. Wong

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
## [Zonespace27/tgstation](https://github.com/Zonespace27/tgstation)@[6085e3b5ee...](https://github.com/Zonespace27/tgstation/commit/6085e3b5eed0f4954d2ba25549c919653207611d)
#### Sunday 2023-05-21 01:44:06 by MrMelbert

Reagent soup / Soup rework / Stoves - A kitchen expansion (#74205)

## About The Pull Request


![image](https://user-images.githubusercontent.com/51863163/227391708-8de28b68-149f-4e02-a2d3-22f6e3067784.png)

**This PR:** 

- Reworks most* existing soup into reagents. 

- Adds Stoves and Ranges. Ranges replace most* existing ovens. 

- Adds soup pots, to cook soup

**How does it work?** 

In the kitchen you will find a stove now.

Stoves act as a "reagent container heater", essentially a chem heater.
You can set a pot onto the stove.

To make soup, visit the cooking recipe book for a guide. Most recipes
are the same as before, just tweaked slightly - Add water to the pot (50
units for 1 batch generally), then add all the corresponding ingredients
to the pot. Set the pot out on the stove and right click it to turn it
on. If the recipe's correct, shortly it will start to mix and give you
soup!

One soup recipe will give you roughly 3 servings of soup. You can pour
our the soup into a bowl using a ladle or just by pouring it manually.

Of note: **All of the reagent contents of the ingredient are transferred
into the soup.** Better, more nutrient rich ingredients produces more
soup, and poisoned produce will pass it on.

If you place the soup into a chem master, you will notice it's roughly
half "soup reagent" and half a variety of reagents, including nutriments
/ proteins. This is your soup! It is recommended you serve your soup
with the reagents included, as they make up more nutrition for the
customer, however you can separate it out if you're picky.

**Todo:** 

- [x] Fill out the PR body a bit more 
- [x] Mapping (wait for big merge conflict pr to go past)
- [x] Soup colors
- [x] Balance pass over for soup recipes
- [x] TODOs
- [ ] Unit tests
- [x] Cullen Skink's recipe is invalid
- [x] Try to see if there's an easy way to prevent soup from fattening
you up too easy.

## Why it's good for the game

Adds some more depth to the kitchen and moves chef away from the
click-button-get-food style that exists.

Allows for inherently custom soups by the way of making it reagents, so
no need to support custom soup food items.

## Changelog

:cl: Melbert, stove and pot sprites by Kryson, ladle sprite by Kinneb
add: Kitchens are now stocked with Ranges. 
add: You can now print (and create) Stoves. 
add: The dinnerware vendor now dispenses ladles. 
add: Spoons can now actually spoon... things.
add: Soup has been reworked entirely. Soups are now reagents, cooked via
a soup pot on a Stove or Range. Simply add water and your required
items, then apply heat. Be careful not to boil over!
add: Stoves, Ranges, and Griddles will now heat up their surroundings -
don't turn them on around plasma!
fix: Fixes being able to cook in an Oven while the room is depowered
qol: Hitting a customer bot with an incorrect recipe no longer counts as
a hostile attack leading to your demise shortly after
refactor: Customer bots that request a reagent now use custom orders
code: Cut down a lot of code in the crafting menu code, and removes some
ugly ispaths
del: Soup is no longer food items, so can't appear in random food pools
(at least not yet).
balance: Virus Food recipe now requires you cool it to 200k.
/:cl:

---
## [tulilirockz/rose-positivo-c464c](https://github.com/tulilirockz/rose-positivo-c464c)@[c7deb7d6fe...](https://github.com/tulilirockz/rose-positivo-c464c/commit/c7deb7d6fe3aa4256d7a79123ffc250a24165263)
#### Sunday 2023-05-21 04:23:33 by Arcitec

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
## [arthunix/ic-linux-bpf](https://github.com/arthunix/ic-linux-bpf)@[9cc4cea780...](https://github.com/arthunix/ic-linux-bpf/commit/9cc4cea780a3144b86e45e395750709dcbeffad2)
#### Sunday 2023-05-21 05:24:50 by arthunix

where is the fucking stdout, damn file descriptors, hate life, hate this

---
## [japko1980/git](https://github.com/japko1980/git)@[eb1c42da8e...](https://github.com/japko1980/git/commit/eb1c42da8e21cc2a8dacd21023a179b788858887)
#### Sunday 2023-05-21 05:25:47 by Jeff King

t/lib-httpd: make CGIPassAuth support conditional

Commit 988aad99b4 (t5563: add tests for basic and anoymous HTTP access,
2023-02-27) added tests that require Apache to support the CGIPassAuth
directive, which was added in Apache 2.4.13. This is fairly old (~8
years), but recent enough that we still encounter it in the wild (e.g.,
RHEL/CentOS 7, which is not EOL until June 2024).

We can live with skipping the new tests on such a platform. But
unfortunately, since the directive is used unconditionally in our
apache.conf, it means the web server fails to start entirely, and we
cannot run other HTTP tests at all (e.g., the basic ones in t5551).

We can fix that by making the config conditional, and only triggering it
for t5563. That solves the problem for t5551 (which then ignores the
directive entirely). For t5563, we'd see apache complain in start_httpd;
with the default setting of GIT_TEST_HTTPD, we'd then skip the whole
script.

But that leaves one small problem: people may set GIT_TEST_HTTPD=1
explicitly, which instructs the tests to fail (rather than skip) when we
can't start the webserver (to avoid accidentally missing some tests).

This could be worked around by having the user manually set
GIT_SKIP_TESTS on a platform with an older Apache. But we can be a bit
friendlier by doing the version check ourselves and setting an
appropriate prereq. We'll use the (lack of) prereq to then skip the rest
of t5563. In theory we could use the prereq to skip individual tests, but
in practice this whole script depends on it.

Reported-by: Todd Zullinger <tmz@pobox.com>
Signed-off-by: Jeff King <peff@peff.net>
Signed-off-by: Junio C Hamano <gitster@pobox.com>

---
## [taca/libui](https://github.com/taca/libui)@[8b3e2665ed...](https://github.com/taca/libui/commit/8b3e2665ed1af3e7a2f70104551e90a6bffe095e)
#### Sunday 2023-05-21 06:58:57 by Pietro Gagliardi

Good night, friend.

I meant to do this a year ago, but didn't, because the pandemic rotted my brain. I'm sorry.

This project is probably not big enough for something like this, but not doing this would be irresponsible, given the circumstances.

---
## [SomeRandomOwl/Skyrat-tg](https://github.com/SomeRandomOwl/Skyrat-tg)@[a4994167fa...](https://github.com/SomeRandomOwl/Skyrat-tg/commit/a4994167fab9cd3ef571f7eef2ad1384306d8221)
#### Sunday 2023-05-21 07:04:01 by SkyratBot

[MIRROR] Drunk slurring scales based on how drunk you are [MDB IGNORE] (#21247)

* Drunk slurring scales based on how drunk you are (#75459)

## About The Pull Request

The strength of the slurring effect drunkness applies on you now scales
based on how drunk you are.

Being "a little" drunk still changes your saymod, and makes you
occasionally slur your words...

![image](https://github.com/tgstation/tgstation/assets/51863163/1b21b359-a1f9-428a-8e10-d2028ac59728)

But being "a lot" drunk kicks it up to 11

![image](https://github.com/tgstation/tgstation/assets/51863163/9d593c80-75ff-4d02-8e7c-e48c738154bb)

Additionally, drunk slurring was separated into "generic slurring" and
"drunk slurring", the former which does not scale but less closely
resembles drunkness. Generic slurring is used in places such as
concussions, so this is an added bonus.

As a result of the split, I had to update mind restoration. Now it heals
all types of slurring, which does include cult slurs.

## Why It's Good For The Game

I, and many other people, always found it very annoying when you became
completely illegible from taking one sip of a drink. This seeks to amend
that by making low levels of drunkness still for the most part be
legible and sane. Average drunkness is roughly the same / equal to the
old slurring effect, while "very drunk" is even more illegible and silly
(which I find funny).

This has the added bonus of separating out "drunk slurring" and "generic
slurring", allowing effects to slur your words without going full ham on
drunkness (burping and "huhh"s).

## Changelog

:cl: Melbert
add: When you are drunk, the strength of your slurring now varies based
on how drunk you are. Being "a little drunk" only rarely slurs your
words, being average drunk is the same as the old effect, while being
very drunk now slurs your words even more.
add: Some non-alcohol sources of slurring, such as concussions, now give
"generic slurring" rather than "drunk slurring", which less resemble
being drunk (ie, no burping).
add: Mind restoration now heals ALL slurring, rather than only drunk
slurring (which includes cult / heretic slurring).
/:cl:

* Drunk slurring scales based on how drunk you are

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [nota8ot/Alexandria](https://github.com/nota8ot/Alexandria)@[eadce44c24...](https://github.com/nota8ot/Alexandria/commit/eadce44c2446175dc54834578c85c0cded2a92b5)
#### Sunday 2023-05-21 07:20:22 by notabot

blacksmith is stupid i hate her peice of spaghetti the human nerve system is more organised than her fucking fsm

---
## [vdaular/linksfordevs](https://github.com/vdaular/linksfordevs)@[fd9a659593...](https://github.com/vdaular/linksfordevs/commit/fd9a65959386ad104cccbd249128e6d9f59b3fa5)
#### Sunday 2023-05-21 07:44:53 by Ben Dornis

Updating: 5/20/2023 9:00:00 PM

 1. Added: Stop working for outsourcing companies as a software engineer
    (https://olzhasar.github.io/posts/stop-working-for-outsourcing-companies/)
 2. Added: The Rhythm of Your Screen - Christopher Butler
    (https://www.chrbutler.com/the-rhythm-of-your-screen)
 3. Added: Building a Signal Analyzer with Modern Web Tech
    (https://cprimozic.net/blog/building-a-signal-analyzer-with-modern-web-tech/)
 4. Added: gkegke
    (https://gkegke.github.io/?postId=4)
 5. Added: Boy Scouts’s bumbling CEOs cause inertia, leadership vacuum
    (https://scoutingmaverick.com/2023/05/04/boy-scoutss-bumbling-ceos-cause-inertia-leadership-vacuum/)
 6. Added: Advent of Code vs LeetCode
    (https://olzhasar.github.io/posts/advent-of-code-vs-leetcode/)
 7. Added: We need new DSLs for the era of LLMs
    (https://zainhoda.github.io/2023/05/20/dsls-for-llms.html)
 8. Added: Life goals by negation negation
    (https://www.riknieu.com/life-goals-with-negation/)
 9. Added: Read it later the hard way
    (https://honza.pokorny.ca/2023/04/read-it-later-the-hard-way/)
10. Added: What I don’t like about chains of thoughts and why language is a bottleneck to efficient reasoning.
    (https://samsja.github.io/blogs/cot/blog/)

Generation took: 00:07:30.6787675
 Maintenance update - cleaning up homepage and feed

---
## [Hilton-Oakbrook-Hills-Resort/OVERSEER-GRATEFUL345I](https://github.com/Hilton-Oakbrook-Hills-Resort/OVERSEER-GRATEFUL345I)@[58d0330360...](https://github.com/Hilton-Oakbrook-Hills-Resort/OVERSEER-GRATEFUL345I/commit/58d03303601a16925912ffad2862bcaa0b7a4800)
#### Sunday 2023-05-21 07:48:26 by Keith Bieszczat rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv

Create whats app

[10:38 PM, 1/30/2023] Keith B.: STRUCK AT
THE WEST POINT MInT
2021-(W) First Day of Issue $1
PCGS Gem Uncirculated
Silver Eagle - Type 2
|882356.70/45792203
[2:47 PM, 1/31/2023] Keith B.: Just got this USA 1 dollar, Delaware Treaty of 1778 identified by CoinSnap. Check it out. https://app.adjust.com/svybm7t
[7:26 AM, 4/19/2023] Keith B.: Yei-Luz Divina
[7:51 AM, 4/19/2023] Keith B.: https://wa.me/stickerpack/meta-avatar
[7:53 AM, 4/19/2023] Keith B.: ‎Use this link to join a WhatsApp voice call: https://call.whatsapp.com/voice/bpulccw99EQ3u4UjKeLGOr
[9:36 AM, 4/19/2023] Keith B.: B Restaurant.
High rollers Dinner Club and Bar.
Brought to you by The Hilton Oakbrook Hills Resort.
3500 n Midwest rd 
WestMont Illinois 60523
4:00pm-2:00am
Kitchen closes at Ten O’clock
[10:03 AM, 4/19/2023] Keith B.: Working on Generating wealth for the Hilton Corporation
[10:35 AM, 4/19/2023] Keith B.: https://scp-wiki.wikidot.com/scp-6542
[1:56 PM, 4/19/2023] Keith B.: https://www.facebook.com/100069123883596/videos/189116160604221
[2:57 PM, 4/19/2023] Keith B.: https://call.whatsapp.com/voice/dL1IIGaZWTYJZypfg619BL
[6:42 PM, 4/19/2023] Keith B.: rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv:350060523
<!DOCTYPE html> <html xml:lang="en" lang="en">      <head>         <title>Govinfo Link Service Error</title>          <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>         <meta name="viewport" content="width=device-width, initial-scale=1.0" /> 		<meta http-equiv="X-UA-Compatible" content="IE=edge" />   		<link href="https://fonts.googleapis.com/css?family=Lato:700|Roboto:400,700" rel="stylesheet" /> 		<link rel="stylesheet" href="/app/main.min.css"/> 	    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/> 		<link rel="stylesheet" href="/app/dynamic/stylesheets/css/search.css"/> 		<link rel="stylesheet" href="/themes/contrib/bootstrap_fdsys/css/style.css"/> 		<link rel="stylesheet" hre…
[7:46 PM, 4/19/2023] Keith B.: https://en.wikipedia.org/wiki/Security_clearance
(630) 394-2637
http://CYBERDRIVEILLINOIS.com
[9:13 PM, 4/19/2023] Keith B.: https://discord.gg/wfhvCgaFzR
https://blox.link/dashboard/verifications
[1:23 AM, 4/20/2023] Keith B.: KxW4eemozKip5A2GVmhcz3BAetgP9RJNQWrM2GpGNc9gvdWY1BLT
[2:39 AM, 4/20/2023] Keith B.: https://apps.apple.com/us/app/docusign-upload-sign-docs/id474990205
[1:54 AM, 4/21/2023] Keith B.: https://xumm.app/detect/request:rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv
[3:28 AM, 4/21/2023] Keith B.: rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv:350060523
[7:44 PM, 4/25/2023] Keith B.: B. Restaurant
(630) 850-5525
https://g.co/kgs/mFebsu
[10:01 PM, 4/25/2023] Keith B.: https://www.linkedin.com/in/keith-bieszczat-5982951b6
[10:45 PM, 4/25/2023] Keith B.: https://scpfoundationo5.atlassian.net/browse/HAN-1
[11:10 PM, 4/25/2023] Keith B.: https://scpfoundationo5.atlassian.net/wiki/x/BYEnAQ
[11:20 PM, 4/26/2023] Keith B.: https://www.dropbox.com/s/47ybiltl2zbdknt/2043-02-08%2022.17.00.png?dl=0
[11:33 PM, 4/26/2023] Keith B.: https://www.dropbox.com/s/700y5z4danoi4sy/2022-11-10%2020.59.02.png?dl=0
[11:41 PM, 4/26/2023] Keith B.: https://github.com/octokit/core.js/pull/548/files
[11:52 PM, 4/26/2023] Keith B.: package-lock.json
[12:04 AM, 4/27/2023] Keith B.: https://trello.com/c/eVyUdd0l

https://github.com/God-s-time-travel-Corporation/000006/commit/228d0c98cf585154e5a2b9dc0676711ed9225944
[12:08 AM, 4/27/2023] Keith B.: https://github.com/6309304695/Grateful345i-/issues/2
[12:22 AM, 4/27/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/000006/commit/cef7c4972202d9a6e1951f524625bd23e75f00b9
[12:27 AM, 4/27/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/000006/issues/4
[12:39 AM, 4/27/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/demo-repository/pull/5/files
[12:45 AM, 4/27/2023] Keith B.: package.json

https://github.com/God-s-time-travel-Corporation/demo-repository/actions/runs/4816379964/jobs/8575936573#step:1:1
[12:53 AM, 4/27/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/demo-repository/pull/5
[1:12 AM, 4/27/2023] Keith B.: https://discord.gg/HmTwqUVc
[1:42 AM, 4/27/2023] Keith B.: Add me on https://discord.com/ so we can talk! My username is grateful345i#5009.
[1:54 AM, 4/27/2023] Keith B.: https://github.com/discord/discord-api-docs/pull/5468#discussion_r1064120387
[2:03 AM, 4/27/2023] Keith B.: 6-intelligence-agency-trust-file
[9:27 PM, 4/27/2023] Keith B.: https://discord.gg/gURDVf6n
[9:40 PM, 4/27/2023] Keith B.: "// Create REST instance
const rest = new REST({ version: '10' }).setToken(token);

// Pass into API
const api = new API(rest);

// Fetch a guild using the API wrapper
const guild = await api.guilds.get('1234567891011');
Links"
https://discord.js.org/docs/packages/core/0.5.2#:~:text=%2F%2F%20Create%20REST%20instance,Links
google-toolbox-for-mac/GTM.xcodeproj/project.pbxproj @dmaclach dmaclach Add GTMURLBuilder to macOS project.  2 contributors 1570 lines (1555 sloc)  114 KB  // !$UTF8$! { 	archiveVersion = 1; 	classes = { 	}; 	objectVersion = 45; 	objects = {  /* Begin PBXBuildFile section / 		0B1B9B8710FECD870084EE4B / GTMStringEncoding.h in Headers / = {isa = PBXBuildFile; fileRef = 0B1B9B8410FECD870084EE4B / GTMStringEncoding.h /; settings = {ATTRIBUTES = (Public, ); }; }; 		0B1B9B8810FECD870084EE4B / GTMStringEncoding.m in Sources / = {isa = PBXBuildFile; fileRef = 0B1B9B8510FECD870084EE4B / GTMStringEncoding.m /; }; 		33C372A60DD8A88500E97817 / GTMNSString+URLArguments.h in Headers / = {isa = PBXBuildFile; fileRef = 33C372A40DD8A88500E97817 / GTMNSString+URLArguments.h /…
[11:48 PM, 4/28/2023] Keith B.: https://apps.apple.com/us/app/booking-com-hotels-travel/id367003839
[1:55 AM, 4/29/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/.github-private/commit/2aca45fa208af2ec8a4e75ac8239649ba87d1ddf
xrpintel Ledger: 79432870   -{     "accepted": true,     "account_hash": "64593A2AA51FA8D3DF1B7B37F147B03F130C93C68BD3063107BB32CF1ABD63FB",     "close_flags": 0,     "close_time": "2023-04-29T11:05:41.000Z",     "close_time_human": "2023-Apr-29 11:05:41.000000000 UTC",     "close_time_resolution": 10,     "closed": true,     "hash": "6BDD8AC99004860DC2A8D2A82378FFD84845CFE8DDBDFB7C0AAD4EBB2327564A",     "ledger_hash": "6BDD8AC99004860DC2A8D2A82378FFD84845CFE8DDBDFB7C0AAD4EBB2327564A",     "ledger_index": 79432870,     "parent_close_time": "2023-04-29T11:05:40.000Z",     "parent_hash": "3F39E7941601E17B0A5AFE6F4A2F6BAD2C2A16DD1BB1D6F064DCE4A56715BDFD",     "seqNum": "79432870",     "totalCoins": "99988953222283425",     "total_coins": "99988953222283425",   …
643bc2da89eeb127f1c5eaf0fe4320221ee28c49d0a2f19227123cecef839f02
[12:49 AM, 4/30/2023] Keith B.: rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv
MJ-12 XRP coin account 
rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv
[1:38 AM, 4/30/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/.github-private/blob/c05df60540f57ce22ea37368f84fc912f83bdb6f/README.md
[1:39 AM, 4/30/2023] Keith B.: {# .github-private
Majestic Twelve Crypto XRP XUMM exchange : rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv
NSA-KBIESZCZAT XUMM exchange address NSA-KBIESZCZAT XUMM exchange address: rU2mEJSLqBRkYLVTv55rFTgQajkLTnT6mA 
XUMM TRUST}
{ngrok http 80 --oauth=github}
{API keys: 6bee7aa3-9eb9-48e2-8b0e-97f9f3aa0e51

21a11ec6-9522-45a7-8cae-3e92b703f968

API secret Key:
91c79664-1ecd-4fff-881c-d3a62fcd91d9

bc87dc3b-7929-4cb0-ad94-1610b319a45f

Application credentials:
6bee7aa3-9eb9-48e2-8b0e-97f9f3aa0e51
First payload:
API key c20b65f7-0679-4da0-a694-cde394578b01
Secret API key 2132bbe6-695d-424f-8034-b29841e1adac
https://xumm.app/api/v1/platform/payload
{MacOS (Darwin): "~/Library/Application Support/ngrok/ngrok.yml"}
JSON}

{ 
  "txjson": {
    "TransactionType": "Payment",…
[3:50 AM, 4/30/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/000006/issues/4
[3:55 AM, 4/30/2023] Keith B.: https://github.com/users/6309304695/achievements/quickdraw
[6:21 AM, 4/30/2023] Keith B.: https://github.com/6309304695/Grateful345i-/pull/7/files
[6:25 AM, 4/30/2023] Keith B.: https://github.com/xrpl365/tx-exporter/pull/7/files
[6:27 AM, 4/30/2023] Keith B.: https://github.com/xrpl365/tx-exporter/pull/7
[6:29 AM, 4/30/2023] Keith B.: https://github.com/xrpl365/tx-exporter/commit/19f04e39f228d538d5e3813b648e61b40c571bfd
[6:31 AM, 4/30/2023] Keith B.: https://github.com/xrpl365
[6:33 AM, 4/30/2023] Keith B.: https://github.com/xrpl365/tx-exporter/commit/7f21aae62c0106593e9132a54396a914b380bd57
[6:34 AM, 4/30/2023] Keith B.: https://discord.gg/EuKYPJuw
[6:43 AM, 4/30/2023] Keith B.: https://scpfoundationo5.atlassian.net/wiki/https://scpfoundationo5.atlassian.net/wiki/x/QYAmAQ
[1:32 AM, 5/1/2023] Keith B.: https://simbad.u-strasbg.fr/simbad/sim-id?Ident=OGLE%20LMC562.19.000006
[2:11 AM, 5/1/2023] Keith B.: "README"
https://github.com/God-s-time-travel-Corporation/.github-private/pull/2/commits/c51ba0f30aa0e9e96cb16b06d6c80b34fb48474e#:~:text=Update-,readme.md,-XUMM%20TRUST%20%20API
[4:59 AM, 5/1/2023] Keith B.: https://github.com/juspay/hyperswitch/releases/tag/v0.5.7
[5:34 AM, 5/1/2023] Keith B.: https://github.com/octokit/core.js
[8:42 AM, 5/5/2023] Keith B.: mailto:o5_6@foundation.scp
[1:24 AM, 5/6/2023] Keith B.: Gold silver and
Other valuables like expensive electronics and devices do not disappear around
Me when taken with time command
Equipment, functionally creating thousands of copies of valuables. Fact check it. Keith Thomas Bieszczat
[1:50 AM, 5/6/2023] Keith B.: https://raw.githubusercontent.com/bitcoin/bips/master/bip-0032.mediawiki
[2:00 AM, 5/6/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/.github-private/commit/acea159aef10421b9fc7241a6f5c24a9be1a96bd
[2:03 AM, 5/6/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/.github/pull/2/files
[2:05 AM, 5/6/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/.github/pull/2
[2:12 AM, 5/6/2023] Keith B.: https://github.com/bitcoin/bips/blob/master/bip-0032/derivation.png?raw=true
[2:21 AM, 5/6/2023] Keith B.: https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/#authentication-and-authorization
[2:58 AM, 5/6/2023] Keith B.: https://xumm.readme.io/v1.0/reference/post-payload
[8:11 AM, 5/6/2023] Keith B.: https://www.google.com/search?q=what+is+anconfiguiratioln+fi&ie=UTF-8&oe=UTF-8&hl=en&client=safari
[8:29 AM, 5/6/2023] Keith B.: https://en.wikipedia.org/wiki/YaST
[10:57 PM, 5/9/2023] Keith B.: https://github.com/octokit/core.js/blob/9cabcabd5e2cb5128c3acf5a24d50965a953f792/.github/workflows/codeql.yml
[11:03 PM, 5/9/2023] Keith B.: lib/marked.cjs
CHANGED
@@ -1,5 +1,5 @@
11	   /**
2	-   * marked v4.3.0 - a markdown parser
2	+   * marked v5.0.0 - a markdown parser
33	    * Copyright (c) 2011-2023, Christopher Jeffrey. (MIT Licensed)
44	    * https://github.com/markedjs/marked
55	    */
@@ -259,9 +259,7 @@ function splitCells(tableRow, count) {
259259	     var row = tableRow.replace(/\|/g, function (match, offset, str) {
260260	         var escaped = false,
261261	           curr = offset;
262	-        while (--curr >= 0 && str[curr] === '\\') {
262	+        while (--curr >= 0 && str[curr] === '\\') escaped = !escaped;
263	-          escaped = !escaped;
264	-        }
265263	         if (escaped) {
266264	           // odd number of slashes means | is escaped
267265	           // so we le…
[11:20 PM, 5/9/2023] Keith B.: My
https://github.com/users/6309304695/achievements/pull-shark
[11:30 PM, 5/9/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/.github/pull/1
[11:30 PM, 5/9/2023] Keith B.: [![Auto Assign](https://github.com/God-s-time-travel-Corporation/demo-repository/actions/workflows/auto-assign.yml/badge.svg?branch=6-intelligence-agency-trust-file&event=create)](https://github.com/God-s-time-travel-Corporation/demo-repository/actions/workflows/auto-assign.yml)
[11:32 PM, 5/9/2023] Keith B.: .github/workflows/proof-html.yml
[12:28 AM, 5/10/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/000006/issues/6
[12:57 AM, 5/10/2023] Keith B.: ![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/d89e6237-0f44-409e-a593-3c03194014b0)

)[FaceBook:Keith Thomas Bieszczat
Twitter:$@o5grateful @@grAteful345i
Discord: 000006 #7766
Trello: Keith Grateful Bieszczat
@@grateful345i

https://trello.com/invite/b/O8jqnzjO/ATTI2fad7adc0026aae178b81953f1d8de901E9009CD/classified-learning-level-99



](https://trello.com/invite/b/O8jqnzjO/ATTI2fad7adc0026aae178b81953f1d8de901E9009CD/classified-learning-level-99)
[https://trello.com/invite/b/O8jqnzjO/ATTI2fad7adc0026aae178b81953f1d8de901E9009CD/classified-learning-level-99
](https://trello.com/invite/b/O8jqnzjO/ATTI2fad7adc0026aae178b81953f1d8de901E9009CD/classified-learning-level-99)

![image](https://github.com/God-s-time-travel-Corpo…
[2:46 AM, 5/10/2023] Keith B.: ![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/d89e6237-0f44-409e-a593-3c03194014b0)

![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/5f62c94c-02e1-4a0e-8b59-da67f7530d96)

![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/b20ed445-0e78-4658-9645-527751e6f69b)
[https://github.com/God-s-time-travel-Corporation/000006/issues/6#issue-1686172738]![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/af8a6f4a-2ae4-44e1-9473-4010ac4c0255)

[{$FaceBook:$Keith Thomas Bieszczat
Twitter:$@o5grateful $@Grateful345i
Discord: $000006 #7766
Trello: $Keith Grateful Bieszczat
$@grateful345i}]

https://trello.com/invite/b/O8jqnzjO/ATTI2fad7adc0026aa…
[1:55 AM, 5/13/2023] Keith B.: https://github.com/God-s-time-travel-Corporation/000006/issues/6#issue-1686172738
[2:40 AM, 5/13/2023] Keith B.: https://www.dni.gov/index.php/what-we-do/ic-related-menus/ic-related-links/intelligence-community-directives
[2:48 AM, 5/13/2023] Keith B.: http://scpfoundation-site32.wikidot.com/
[2:53 AM, 5/13/2023] Keith B.: http://scpfoundation-site32.wikidot.com/mail
[5:29 AM, 5/13/2023] Keith B.: # clone anywhere you like, but adjust paths as needed
mkdir ~/dracula-theme && cd ~/dracula-theme
git clone https://github.com/dracula/midnight-commander.git

mkdir -p ~/.local/share/mc/skins && cd ~/.local/share/mc/skins
ln -s ~/dracula-theme/midnight-commander/skins/dracula.ini
ln -s ~/dracula-theme/midnight-commander/skins/dracula256.ini

https://github.com/God-s-time-travel-Corporation/demo-repository/commit/e59cd88db404e7df36426e0c4bf23a0db37302da
[5:56 AM, 5/13/2023] Keith B.: ![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/8bdf7185-5a3a-464e-a119-2d22956e911a)![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/c34f5c62-ffa5-446f-a050-466bdc983669)
![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/2b7e5e58-3ee8-4b32-92be-d11aa4ec2896)
![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/d89e6237-0f44-409e-a593-3c03194014b0)
![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/a1429755-a2a5-4b69-83fc-310ddc28072c)
![image](https://github.com/God-s-time-travel-Corporation/000006/assets/117963165/5f62c94c-02e1-4a0e-8b59-da67f7530d96) $ npm install
Once this is configured, there are …
[6:59 AM, 5/13/2023] Keith B.: https://github.com/dattaz/nsa-globe/commit/5661db855772ce76b30924a986fd7c2d1332db07
[8:37 PM, 5/15/2023] Keith B.: 1824509317
[8:37 PM, 5/15/2023] Keith B.: Hilton Honors Account number
[10:22 PM, 5/19/2023] Keith B.: https://github.com/6309304695/OVERSEER-GRATEFUL345I.git
[12:17 AM, 5/21/2023] Keith B.: https://github.com/6309304695/OVERSEER-GRATEFUL345I/pull/1#issue-1718365143
[2:03 AM, 5/21/2023] Keith B.: 警告： {$one}

{$two}



{$three}
[2:06 AM, 5/21/2023] Keith B.: __      FREEWARE - 4 - ALL     __
| |_| | _   _  __W4ND3RLU5T  __  | |__| |
|  ()  |  \_/  |_  |\ |  |  |__| |  ()  |
|__| / \ |_  | \|  |  |   | |___|
-------------------------------------------
               >>DISCLAIMER<<
     >>DON'T READ THIS IF UR A POSER<<
  >>DO NOT DISTRIBUTE TO NON-HUMMERS!!!<<

ONCE YOU ENTER WAN-DERER'S PARADISE *YOU
WILL NO LONGER BE CONSCIOUS IN THE PHYSICAL
WORLD!!* YOU WILL BECOME ONE WITH OUR LORD,
AND YOUR IMPERFECT FLESH WILL FALL COMATOSE!
IF THIS SOUNDS LIKE IT WOULD SUCK THEN DONT
RUN THE FILE ROFL

PLEASE AIM ME IF SOMETHING BAD HAPPENS. I
LOVE U GUYS AND I'LL KEEP THE PARADISE OPEN
FOR AS LONG AS I CAN, WAN WILLING. I CAN
FEEL HIS LOVE FOR US TOO. WE R ALL FINALLY
CONNECTED. 

SO OPEN THE F$%#NG…
[2:45 AM, 5/21/2023] Keith B.: https://raw.githubusercontent.com/6309304695/OVERSEER-GRATEFUL345I/2c642f8b198d0178d610d450ce6d8c26a4d334f8/CIAJMK1209%203.png

---
## [Ebin-Halcyon/Shiptest](https://github.com/Ebin-Halcyon/Shiptest)@[ae5ae813b8...](https://github.com/Ebin-Halcyon/Shiptest/commit/ae5ae813b8dead3db964893b5169737a4a7f0551)
#### Sunday 2023-05-21 09:19:08 by Bjarl

The Pillbottle, and Pill Things. (#1585)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
![2022 10 20-22 10
16](https://user-images.githubusercontent.com/94164348/197116962-64d22347-2a19-43fc-9614-0c56142c96b9.png)

![dreamseeker_mMxUmMmRjx](https://user-images.githubusercontent.com/94164348/197119938-c60ff760-a7a0-493d-95e3-ac5579a3f3ca.png)

![image](https://user-images.githubusercontent.com/94164348/197118936-6e777e9c-9452-4339-8c38-b7ee5afcd3eb.png)

Adds the Pillbottle-Class Locust Carrier, a ship that hauls around 8
Pills. It is intended as an adminspawn ship mainly for stresstesting
subshuttles (and being asked for). It's fairly resource starved, and has
frankly terrible engines. The expectation is that it will utilize its 8
pods to gather resources and return to the mothership. Or fly off and
die horribly. It has slots for 10 prisoners (that's like 3 pills and one
third of a 4th).
This pr also edits the pill, blackpill, and superpill to be subshuttles
(compatible with the subshuttle system) by cutting out most of their
equipment, converting their maps to shuttle datums, and giving them
docking ports.


<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

<!-- Tick the box below (put an X instead of a space between the
brackets) if you have tested your changes and this is ready for review.
Leave unticked if you have yet to test your changes and this is not
ready for review. -->

- [ ] I affirm that I have tested all of my proposed changes and that
any issues found during tested have been addressed.

## Why It's Good For The Game
Subshuttles are fucking awesome.
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
add: Pillbottle-Class Locust Carrier has been added. These cramped
vessels act as a mothership to a swarm of Pill-class Torture
add: The pill and all variants are now subshuttles.
add: Bad Ion Engines, for ships that need to go slow.
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
Co-authored-by: spockye <79304582+spockye@users.noreply.github.com>

---
## [kingof4112n/money](https://github.com/kingof4112n/money)@[e267e19e4c...](https://github.com/kingof4112n/money/commit/e267e19e4cca5889bc5e66a20a4cf2142f4b5ab4)
#### Sunday 2023-05-21 10:03:03 by kingof4112n

Add files via upload

Project Description:
PetCo - Ensuring Quality Pets for Everyone

PetCo is a revolutionary platform designed to simplify the process of buying a pet. In a market flooded with countless sellers and varying prices, PetCo stands out as a trusted provider of healthy and genetically disease-free pets. Our mission is to ensure that every pet lover can bring home a furry companion without worrying about their well-being.

At PetCo, we understand the emotional bond between humans and their pets. We believe that pets are more than just animals; they are our best friends and companions. That's why we go the extra mile to guarantee the quality and care of our pets.

All the pets available at PetCo undergo a thorough vetting process. Our team of experts carefully selects each pet, ensuring they are free from genetic diseases and have received proper care and nurturing. We prioritize their health and overall well-being, so you can have peace of mind when welcoming a new member into your family.

In addition to the assurance of healthy pets, PetCo offers a fixed pricing model. We believe in transparency and fairness, providing a consistent pricing structure that eliminates the hassle of negotiating prices or falling victim to inflated rates.

With PetCo, your journey to finding the perfect pet is made easy and worry-free. Explore our website and discover a wide range of pets available for adoption. Whether you're looking for a loyal canine companion, a playful feline friend, or a charming little critter, PetCo has the perfect pet waiting for you.

Experience the joy of bringing home a loving pet without compromising on their well-being. Choose PetCo for trusted, healthy, and assured pets at a fixed price. Your best friend is just a click away!

---
## [DEFRA/water-abstraction-ui](https://github.com/DEFRA/water-abstraction-ui)@[65a3336c9a...](https://github.com/DEFRA/water-abstraction-ui/commit/65a3336c9a79dd012b481b9f6955585aecab8e63)
#### Sunday 2023-05-21 10:36:55 by Alan Cruikshanks

Add SROC only billing feature flag (#2355)

https://eaflood.atlassian.net/browse/WATER-4016

The billing & data team are struggling with the performance of the service in PREPROD during UAT. In WATER-4013 we were able to determine that because of the poor quality of queries in the legacy code the service is being throttled by AWS because we're hitting the IOPS threshold.

We've made changes to help with that in PRE-PROD (doubled the size of the RDS instance!) but we are still faced with a service that becomes overwhelmed if you try to run more than one bill run at a time. Until we've been able to migrate away from the legacy code we are always going to have performance issues. It is why the current dev team's guidance is only one bill run at a time (followed by a nice brew, some friendly chat, and generally avoiding touching it for a while!)

But the billing & data team want to get on with their UAT. Different people look after different regions and they have a lot of scenarios they need to work through.

So, we've had a brain wave. As the focus is on the SROC bill runs, what if we switched off the PRESROC ones temporarily?

This change covers adding a feature flag to the service, which if enabled would mean the service will only kick off the SROC bill run.

---
## [SpaceLoveSs13/Skyrat-tg](https://github.com/SpaceLoveSs13/Skyrat-tg)@[fc1471c818...](https://github.com/SpaceLoveSs13/Skyrat-tg/commit/fc1471c8187d3f2a49d75a8a5c3e1b610fec45d3)
#### Sunday 2023-05-21 11:39:57 by SkyratBot

[MIRROR] Deadchat Announcement Variety Pack 1 [MDB IGNORE] (#20957)

* Deadchat Announcement Variety Pack 1 (#75140)

## About The Pull Request

Adds announce_to_ghosts()/notify_ghosts() calls to a bunch of different
things.

**THIS INCLUDES:**
- Powersink being activated/reaching critical (explosion) heat capacity.
- His Grace being awoken.
- Hot Potatoes being armed.
- Ascension Rituals being completed.
- Eyesnatcher victims.
- Ovens exploding as a result of the Aurora Caelus event.
- Wizard Imposter spawns.
- Rock-Paper-Scissors with death as the result of Helbital consumption.
- BSA impact sites.
- Spontaneous Appendicitis.
- The purchasing of a badass syndie balloon.
- The Supermatter beginning to delaminate.

This was everything that I could think of that would be worth announcing
to deadchat. These were all chosen with consideration to questions like
"how easy would it be to spam deadchat with this?" and "will observers
actually see the interesting thing happen, or just the aftermath?".

Not gonna lie, I've really become an observer main as of recently. Maybe
that's being reflected in my recent PRs. Who's to say? Deadchat
Announcement Variety Pack 2 will probably never come out. Sorry.
## Why It's Good For The Game

Gives deadchat a better indiciation of when/where something **REALLY
FUNNY** is about to happen. Draws attention to certain things that are
likely to gather an audience anyways, but sooner (for your viewing
pleasure). In simple terms, it helps the observers observe things
better.

Some cases, such as the aurora caelus or helbitaljanken, are occurrences
so rare that they deserve the audience.
## Changelog
:cl: Rhials
qol: Observers now recieve an alert when a powersink is activated/about
to explode.
qol: His Grace being awoken now alerts observers, to give you a
headstart on your murderbone ghost ring.
qol: Ascension Rituals being completed will also alert observers, for
basically the same reason.
qol: Arming a hot potato will now alert observers. Catch!
qol: Eyesnatcher victims will now notify observers, and invite them to
laugh at their state of misery and impotence.
qol: Observers will be notified of any acute references to The Simpsons
or other 20th Television America copyright properties.
qol: Wizard Imposter spawns alert observers, much like any other ghost
role event should.
qol: Playing Rock-Paper-Scissors with death will now alert the observers
and invite them to watch. Better not choke!
qol: Observers now get an orbit link for BSA impact sites. Why does it
keep teleporting me to the AI upload??
qol: Spontaneous Appendicitis now alerts deadchat.
qol: The purchasing of a badass syndie balloon now alerts deadchat. You
might not be any more powerful, but at least you have an audience.
qol: When beginning to delaminate, the Supermatter will alert observers
and invite them to watch the fireworks.
/:cl:

* Deadchat Announcement Variety Pack 1

---------

Co-authored-by: Rhials <Datguy33456@gmail.com>

---
## [Lyris12/YGOCC-Moon](https://github.com/Lyris12/YGOCC-Moon)@[97743b316c...](https://github.com/Lyris12/YGOCC-Moon/commit/97743b316c3767a5d3b1e395cbcb4bdd8811a10c)
#### Sunday 2023-05-21 11:51:25 by Xarc

fix & add cards

Fixed a bug that affected the following Time Leap Monsters, they were missing some functions regarding Time Leaps:
* Chronovert Absolute Dragon
* Aurora Bird
* Karakuri Modern mdl 76112
* PSY-Framelord Sigma
* Gaia Knight From a Different Time
* Starlen the Hope Bringer Magical Girl
Fxed "Artifact Alastair" having the wrong attribute (was DARK, and now is LIGHT).

"Chronovert Dragon" and "Chronovert Absolute Dragon" are now part of the new "Chronovert" Archetype, also Chronovert Dragon got a bug fixed that made the opponent's card return to the top of the Deck instead of shuffling it into the Deck.

Fixed the material attach effect that happens after the negate effects of "Oniritron Lord of the Endless Space" and "Oniritron Lord of the Infinite Light" that worked like a "then" but was supposed to be an "and if you do".
add:
* "Temporius" archetype
* "Chronovert" archetype

---
## [Digital-Controllers/discord-bot](https://github.com/Digital-Controllers/discord-bot)@[9d51680738...](https://github.com/Digital-Controllers/discord-bot/commit/9d5168073891525f6c3379d58f54dfb4607d911d)
#### Sunday 2023-05-21 12:14:57 by Molly O

Merge branch 'Digital-Controllers:main' into fuck-you-ephemerises-your-responses

---
## [Digital-Controllers/discord-bot](https://github.com/Digital-Controllers/discord-bot)@[0a7023654f...](https://github.com/Digital-Controllers/discord-bot/commit/0a7023654f798d6d3659f7aaf729bd3744951d76)
#### Sunday 2023-05-21 12:14:57 by QuantifyGG

Merge pull request #19 from mollybeam/fuck-you-ephemerises-your-responses

convert sync_command_tree and update_embed to app_commands

---
## [FeenieRU/Fluffy-STG](https://github.com/FeenieRU/Fluffy-STG)@[500cdb9257...](https://github.com/FeenieRU/Fluffy-STG/commit/500cdb925720c408de4332df6b2d8b8e0b20b63c)
#### Sunday 2023-05-21 12:35:37 by SkyratBot

north star's asylum no longer spawns with prisoners [MDB IGNORE] (#20732)

* north star's asylum no longer spawns with prisoners (#74879)

## About The Pull Request
the asylum on the north star no longer spawns prisoners, only the
permabrig does
the computer in the asylum is rotated correctly

## Why It's Good For The Game
on the paper, it seems like a cool concept, but theres a few issues here
the psychologist isnt designed to handle prisoners in the first place.
this is fine on mrp but it gets kinda muddy when prisoners on lrp like
beating people up
prisoners are recommended as a new player role by the wiki (very
stupid), this role starting in an asylum without anything to do while
being asked some stuff by a psychologist seems like itd add onto
confusion
players dont know what jobs are spawning with them, there very well may
not be a cmo or psychologist. if theres no one in sec you can deal with
that because you have a small botany and kitchen, and can possibly
escape. this aint a thing here, only thing you have is reading books and
maybe pen and paper rpgs if another prisoner spawns, while being stuck
in an extremely tiny space

this can work in the future i think, but it requires code support we
currently dont have, so it better to cut its

## Changelog
:cl:
del: prisoner spawns from the north star asylum
/:cl:

* north star's asylum no longer spawns with prisoners

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>
Signed-off-by: Vladimir Veisman <v.veisman@flashie.me>

---
## [AInnovateks/McSparky](https://github.com/AInnovateks/McSparky)@[b1e986e041...](https://github.com/AInnovateks/McSparky/commit/b1e986e041b9f8c72a245705392c086b6cdb656b)
#### Sunday 2023-05-21 12:49:00 by AITEK

Update README.md

Aquí tienes un ejemplo de cómo podrías describir tu proyecto en inglés:

```
Project Name: Virtual Assistant with Facial Recognition

Description:
The Virtual Assistant with Facial Recognition is an interactive AI-based assistant that incorporates facial recognition technology to provide personalized services. It serves as a multi-purpose virtual assistant capable of performing various tasks, such as facial recognition, voice interaction, medical services, legal consultation, tutoring, psychological support, content creation, and digital marketing.

Key Features:
- Facial Recognition: The assistant uses computer vision techniques to detect and recognize faces, allowing for personalized user experiences and authentication.
- Voice Interaction: Users can interact with the assistant using voice commands, enabling a natural and intuitive interaction.
- Medical Services: The assistant provides medical services by connecting users with specialized doctors based on their specific medical needs.
- Legal Consultation: Users can receive legal advice and consultation in different legal areas, connecting them with experienced lawyers.
- Tutoring: The assistant offers tutoring services in various subjects, providing personalized learning experiences tailored to the user's needs.
- Psychological Support: Users can receive emotional support and guidance from qualified psychologists.
- Content Creation: The assistant includes features for creating digital content, such as image and video editing, audio recording, and text generation.
- Digital Marketing: The assistant incorporates SEO and social media marketing functionalities to help users optimize their online presence.

Technical Stack:
- Programming Languages: Python
- Libraries and Frameworks: OpenCV, dlib, pyttsx3, sounddevice, soundfile, numpy, requests
- APIs: Speech recognition API for audio-to-text conversion
- Databases: MongoDB for storing user information and preferences

Future Enhancements:
- Integration with cloud-based AI services for advanced natural language processing and sentiment analysis.
- IoT integration for controlling smart home devices through voice commands.
- Integration with social media platforms for seamless content sharing and engagement.

This project aims to provide users with a comprehensive and personalized virtual assistant experience. It combines facial recognition, voice interaction, and a range of specialized services to meet the user's needs in various domains. The project is open-source, encouraging collaboration and contributions from the developer community.
```

Feel free to customize the example based on your specific project details and requirements.

---
## [nauticall/cmss13](https://github.com/nauticall/cmss13)@[7d27d8508c...](https://github.com/nauticall/cmss13/commit/7d27d8508ce0723dbbcf1dfad9810a3092a71f61)
#### Sunday 2023-05-21 12:56:08 by TotalEpicness

Fixes invincible base crusher (#2682)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Fixes an oversight that allowed base crusher to have half it's intended
shield cooldown
<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.
runs
Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->

# Explain why it's good for the game
Never intended on the first place and led to crusher being busted as
fuck as it is currently.

This was never intended and was a mess up on my part. It fell through
from the painfully long development that Charger had as months went by
between testing sessions and TMs, along with my inexperience with larger
projects and bad note taking at the time.

Maintainers are also supposed to filter stuff like this but after like a
billion code reviews Charger had, I can see how it got through on their
end as well.

Nevertheless this dies here. 

funny contrib moment
<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding, and may discourage maintainers from reviewing or merging
your PR. This section is not strictly required for (non-controversial)
fix PRs or backend PRs. -->


# Testing Photographs and Procedure
it runs
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

:cl: Totalepicness
balance: Fixes base crusher having half it's intended cooldown for the
shield ability
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

Co-authored-by: Epicness <coolguyethanw@gmail.com>

---
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[f3549a4aec...](https://github.com/mc-oofert/tgstation/commit/f3549a4aeca6701a2969a63b7d4034d5bc560cb6)
#### Sunday 2023-05-21 16:24:59 by Thunder12345

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
## [mc-oofert/tgstation](https://github.com/mc-oofert/tgstation)@[1674f25725...](https://github.com/mc-oofert/tgstation/commit/1674f25725c25e15769b031553b42144f526f841)
#### Sunday 2023-05-21 16:24:59 by John Willard

New Medical job: The Coroner (#75065)

## About The Pull Request

HackMD: https://hackmd.io/RE9uRwSYSjCch17-OQ4pjQ?view

Feedback link: https://tgstation13.org/phpBB/viewtopic.php?f=10&t=33972

Adds a Coroner job to the game, they work in the Medical department and
have their office in the Morgue.
I was inspired to make this after I had played my first round on
Paradise and messed around in there. The analyzer is copied from there
(https://github.com/ParadiseSS13/Paradise/pull/20957), and their
jumpsuit is also mostly stolen from it (i just copied the color scheme
onto our own suits).

Coroners can perform autopsies on people to see their stats, like this

![image](https://user-images.githubusercontent.com/53777086/235369225-805d482c-56c0-441c-9ef8-a42d0a0192bc.png)

They have access to Medbay, and on lowpop will get Pharmacy (to make
their own formaldehyde). They also have their own Secure Morgue access
for their office (doubles as a surgery room because they are edgelords
or whatever) and the secure morgue trays.

Secure Morgue trays spawn with their beepers off and is only accessible
by them, the CMO, and HoS. It's used to morgue Antagonists. Security's
own morgue trays have been removed.

The job in action


https://cdn.discordapp.com/attachments/950489581151735849/1102297675669442570/2023-04-30_14-16-06.mp4

### Surgery changes

Autopsies are a Surgery, and I tried to intertwine this with the
Dissection surgery.
Dissections and Autopsies both require the Autopsy scanner to perform
them, however you can only perform one on any given body. Dissections
are for experiments, Autopsies is for the paper of information.

Dissected bodies now also give a ~20% surgery speed boost, this was
added at the request of Fikou as a way to encourage Doctors to let the
Coroner do their job before reviving a body.
I also remember the Medical skill, which allowed Doctors to do surgery
faster on people, and I hope that this can do something like that
WITHOUT adding the potential for exploiting, which led to the skill's
downfall.

### Morgue Improvements

Morgue trays are no longer named with pens, they instead will steal the
name of the last bodybag to be put in them.

Morgue trays are also removed from Brig Medical areas and Robotics, now
they have to bring their corpses to the Morgue where the Coroner can
keep track and ensure records are properly updated.

### Sprite credits

I can't fit it all in the Changelog, so this is who made what

McRamon
- Autopsy scanner

Tattax 
- Table clock sprites and in-hands

CoiledLamb
- Coroner jumpsuits & labcoats (inhand, on sprite, and their respective
alternatives)
- Coroner gloves
- CoronerDrobe (the vending machine)

## Why It's Good For The Game

This is mostly explained in the hackmd, but the goal of this is:

1. Increase the use of the Medical Records console.
2. Add a new and interesting way for Detectives to uncover mysteries.
3. Add a more RP-flavored role in Medical that still has mechanics tied
behind it.

## Changelog

:cl: JohnFulpWillard, sprites by McRamon, tattax, and Lamb
add: The Coroner, a new Medical role revolving around dead corpses and
autopsies.
add: The Coroner's Autopsy Scanner, used for discovering the cause for
someone's death, listing their wounds, the causes of them, their
reagents, and diseases (including stealth ones!)
qol: Morgue Trays are now named after the bodybags inside of them.
balance: The morgue now has 'Secure' morgue trays which by default don't
beep.
balance: Security Medical area and Robotics no longer have their own
morgue trays.
balance: Dissected bodies now have faster surgery speed. Autopsies also
count as dissections, however they're mutually exclusive.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [WEareinthebeam/restoration-mod](https://github.com/WEareinthebeam/restoration-mod)@[e8c7949c86...](https://github.com/WEareinthebeam/restoration-mod/commit/e8c7949c8624ea9440ac11ce4df2be9a8355b12c)
#### Sunday 2023-05-21 16:51:40 by Noep

things to do

- I love pika as my girlfriend and she has boing boing

- Slightly boosted the pickup rate of <60 damage weapons

- Fix missing desc for underbarrel gas grenades

- Anti-Materiel rifles' total ammo has been halved to account for their 2x headshot damage, similar to how the P90 and MP7 see reduced ammo despite their base damage.
-- >:3's Musket does not have this total ammo reduction as it does not deal bonus headshot damage; it has been moved to the "heavy sniper" buy menu category instead as a result

---
## [cannnAvar/run2live](https://github.com/cannnAvar/run2live)@[7f9ce7e7ab...](https://github.com/cannnAvar/run2live/commit/7f9ce7e7abdc4c1d86f596f812b0c6fcb621550e)
#### Sunday 2023-05-21 17:09:49 by cannnAvar

fuck you little fuck now its my code now mother fucker

---
## [HazelnutCookie/glass-pixel-dungeon](https://github.com/HazelnutCookie/glass-pixel-dungeon)@[0f3a4bca26...](https://github.com/HazelnutCookie/glass-pixel-dungeon/commit/0f3a4bca2630a4e7e26307c873b3c7cb6592c659)
#### Sunday 2023-05-21 17:40:22 by HazelnutCookie

Added my lovely girlfriend and artist Naomi to the credits.

---
## [Bens-Jammin/ExpenseTracker](https://github.com/Bens-Jammin/ExpenseTracker)@[14a460a360...](https://github.com/Bens-Jammin/ExpenseTracker/commit/14a460a360a69ee662a20292f1f0c065c0368718)
#### Sunday 2023-05-21 18:08:57 by Ben

holy shit i finally cleaned up the FUCKING MESS that was Gradle

---
## [Johannes2262/cmss13](https://github.com/Johannes2262/cmss13)@[df247be72a...](https://github.com/Johannes2262/cmss13/commit/df247be72a87e69e8841ad754633329c87a7883d)
#### Sunday 2023-05-21 19:33:39 by brian

reduces platform and handrail projectile coverage significantly (#2995)

# About the pull request

Does exactly what the title implies: reduces platform and handrail
projectile coverage significantly.
Platforms 60% -> 0%
Handrails 35% -> 10%

# Explain why it's good for the game

When a platform and handrail are combined, that totals at a 95% chance
of blocking a bullet passing through that tile. Platform corners also
catch bullets. That's some hogwash if you ask me. It makes areas like
Sorokyne's Mining platform entrance nearly un-defendable for marines
since they can't shoot past what is effectively an invisible bullet
wall. When I made Sorokyne, this was not the intent of the area. New
Varadero has similar problems.

You may ask, why not change those areas instead? My answer: Sod off,
they look awesome, and I don't want to code a check on projectiles to
determine if you're shooting 'up' at a ledge which would be the logical
simulationist fix. Also handrails aren't supposed to block bullets
unless they're reinforced (not that anyone uses that mechanic though).
How do I know this? I willed this mechanic into existence for Strata
with shitcode. I was there when it was written.

Both xenos that spit and marines that shoot will benefit from this
change.

Oh yeah and corners won't catch bullets anymore.

# Changelog

:cl: Triiodine
balance: Reduced projectile coverage of platforms from 60% to 0%.
balance: Reduced projectile coverage on handrail types from 35% to 10%.
Sandstone handrails are unaffected and remain at 35% projectile
coverage.
balance: Sandstone handrails can no longer be reinforced.
/:cl:

---------

Co-authored-by: Chadwick B. Dunlop <fake@fake.mail>

---
## [jimmy947788/UACME](https://github.com/jimmy947788/UACME)@[c65f9215c1...](https://github.com/jimmy947788/UACME/commit/c65f9215c1103269ca31f66f49869fcde547af98)
#### Sunday 2023-05-21 19:34:09 by hfiref0x

Update Naka.vcxproj

Retarget platform toolset for appveyor fail. I understand that this service is currently busy supporting %current thing% more than actually working on their script-shit, but holy fuck seriously.

---
## [BarteG44/Shiptest](https://github.com/BarteG44/Shiptest)@[0cff53fc09...](https://github.com/BarteG44/Shiptest/commit/0cff53fc09c34d989d2bc34b1699bd856af2cb92)
#### Sunday 2023-05-21 20:13:30 by meemofcourse

Reworks the Twinkleshine-Class (#1825)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request


![2023 05 13-23 20
45](https://github.com/shiptest-ss13/Shiptest/assets/75212565/de6f3a47-7be8-4800-ae73-9fc386e4bf01)

![twinklerework5](https://github.com/shiptest-ss13/Shiptest/assets/75212565/f1808576-70e3-4b56-b977-5b5e7d665fdd)





The Twinkleshine is a CyberSun-made Syndicate display of force, staffed
by every branch of the Syndicate. Despite the silly name, the presence
of one in a sector implies it to be of importance to the Syndicate, and
enemies within sight can only pray that the Twinkleshine crew are
incompetent enough to shoot themselves with their own weaponry (or blow
themselves up with the supermatter on-board).

It is staffed by:

- 1 Captain
- 1 Lieutenant (previously the Operative - serves as a warden/hos)
- 2 Medics
- 2 Engineers (previously the Mechanics)
- 5 Operatives (previously the Troopers)
- 1 Bartender
- 1 Miner
- 2 Deck Assistants

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game

Few days ago, an admin spawned a Twinkleshine, and I got to captain it.
The Twinkleshine is old. It sucks. This, hopefully, fixes that.

Originally, this was going to be minor fixes, but ended up becoming an
attempt at reworking the ship to a more modern state - the hull has been
redone and is mostly symmetrical, the old spacepod was replaced with a
Dark Gygax, the supermatter shouldn't be activated upon spawning the
ship, there's more turf decals and a bigger lot-of-things, added a
bartender and a miner, people can actually tell who they are and what
they do, and there is now a box moth. Rejoice.

Also, this is the first time I've ever mapped a ship. What better way to
begin with a giant battleship?

<!-- Please add a short description of why you think these changes would
benefit the game. If you can't justify it in words, it might not be
worth adding. -->

## Changelog

:cl:
tweak: Reworks the Twinkleshine
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Signed-off-by: meemofcourse <75212565+meemofcourse@users.noreply.github.com>

---
## [Perkedel/perkedel-astro](https://github.com/Perkedel/perkedel-astro)@[ee50a87632...](https://github.com/Perkedel/perkedel-astro/commit/ee50a87632b5ddf1c33bd21203f584e0b528ee2a)
#### Sunday 2023-05-21 20:15:14 by Joel Robert Justiawan

Give me break pls

I need break.

maybe a whole week?

I just confirmed I miscalculated the romance when porting this adoption to here.

oh God.

oh no.

I made a mistake.

I think internet wrong, so do I. can't be helped, it's so complex.

uh..

I thought Karkat goes to Nepeta  here.

no, fan collected intel says Karkat goes to Terezi, or that's what I read.

idk.

Musyawarah Mufakat time.
move Matesprite back as the original
Karkat & Terezi,
or..
break to
Karkat & Nepeta?
I think make fun duo annoyancer
let us know
thancc.

---
## [momentum-mod/website](https://github.com/momentum-mod/website)@[0057237c93...](https://github.com/momentum-mod/website/commit/0057237c93afae60114dbb99c18be20c8ebbd0eb)
#### Sunday 2023-05-21 20:27:26 by tsa96

refactor(front): Remove SmartTableService

What the fuck even was this lmao? Bunch of random mocks in our actual services? Hell yeah!

---
## [edwinantony1995/Opensource._.resources](https://github.com/edwinantony1995/Opensource._.resources)@[80b5e63800...](https://github.com/edwinantony1995/Opensource._.resources/commit/80b5e63800659b1584516b579a1b2c04b79119cc)
#### Sunday 2023-05-21 20:29:37 by @Code-Defenders#

README.md

(https://img.shields.io/github/license/Z4nzu/hackingtool)
![](https://img.shields.io/github/issues/Z4nzu/hackingtool)
![](https://img.shields.io/github/issues-closed/Z4nzu/hackingtool)
![](https://img.shields.io/badge/Python-3-blue)
![](https://img.shields.io/github/forks/Z4nzu/hackingtool)
![](https://img.shields.io/github/stars/Z4nzu/hackingtool)
![](https://img.shields.io/github/last-commit/Z4nzu/hackingtool)
[![HitCount](http://hits.dwyl.com/Z4nzu/hackingtool.svg)](http://hits.dwyl.com/Z4nzu/hackingtool)
![](https://img.shields.io/badge/platform-Linux%20%7C%20KaliLinux%20%7C%20ParrotOs-blue)

#### Install Kali Linux in WIndows10 Without VirtualBox [YOUTUBE](https://youtu.be/BsFhpIDcd9I) or use Docker

## Update Available V1.2.0 🚀 
- [✔] Installation Bug Fixed
- [x] Added New Tools 
    - [x] Reverse Engineering
    - [x] RAT Tools
    - [x] Web Crawling 
    - [x] Payload Injector
- [x] Multitor Tools update
- [X] Added Tool in wifijamming
- [X] Added Tool in steganography



# Hackingtool Menu 🧰
- [Anonymously Hiding Tools](#anonymously-hiding-tools)
- [Information gathering tools](#information-gathering-tools)
- [Wordlist Generator](#wordlist-generator)
- [Wireless attack tools](#wireless-attack-tools)
- [SQL Injection Tools](#sql-injection-tools)
- [Phishing attack tools](#phishing-attack-tools)
- [Web Attack tools](#web-attack-tools)
- [Post exploitation tools](#post-exploitation-tools)
- [Forensic tools](#forensic-tools)
- [Payload creation tools](#payload-creation-tools)
- [Exploit framework](#exploit-framework)
- [Reverse engineering tools](#reverse-engineering-tools)
- [DDOS Attack Tools](#ddos-attack-tools)
- [Remote Administrator Tools (RAT)](#remote-administrator-tools--rat-)
- [XSS Attack Tools](#xss-attack-tools)
- [Steganograhy tools](#steganograhy-tools)
- [Other tools](#other-tools)
    - [SocialMedia Bruteforce](#socialmedia-bruteforce)
    - [Android Hacking tools](#android-hacking-tools)
    - [IDN Homograph Attack](#idn-homograph-attack)
    - [Email Verify tools](#email-verify-tools)
    - [Hash cracking tools](#hash-cracking-tools)
    - [Wifi Deauthenticate](#wifi-deauthenticate)
    - [SocialMedia Finder](#socialmedia-finder)
    - [Payload Injector](#payload-injector)
    - [Web crawling](#web-crawling)
    - [Mix tools](#mix-tools)


### Anonymously Hiding Tools
- [Anonmously Surf](https://github.com/Und3rf10w/kali-anonsurf)
- [Multitor](https://github.com/trimstray/multitor)
### Information gathering tools
- [Network Map (nmap)](https://github.com/nmap/nmap)
- [Dracnmap](https://github.com/Screetsec/Dracnmap)
- Port scanning
- Host to IP 
- [Xerosploit](https://github.com/LionSec/xerosploit)
- [RED HAWK (All In One Scanning)](https://github.com/Tuhinshubhra/RED_HAWK)
- [ReconSpider(For All Scanning)](https://github.com/bhavsec/reconspider)
- IsItDown (Check Website Down/Up)
- [Infoga - Email OSINT](https://github.com/m4ll0k/Infoga)
- [ReconDog](https://github.com/s0md3v/ReconDog)
- [Striker](https://github.com/s0md3v/Striker)
- [SecretFinder (like API & etc)](https://github.com/m4ll0k/SecretFinder)
- [Find Info Using Shodan](https://github.com/m4ll0k/Shodanfy.py)
- [Port Scanner - rang3r (Python 2.7)](https://github.com/floriankunushevci/rang3r)
- [Port Scanner - Ranger Reloaded (Python 3+)](https://github.com/joeyagreco/ranger-reloaded)
- [Breacher](https://github.com/s0md3v/Breacher)
### Wordlist Generator
- [Cupp](https://github.com/Mebus/cupp.git)
- [WordlistCreator](https://github.com/Z4nzu/wlcreator)
- [Goblin WordGenerator](https://github.com/UndeadSec/GoblinWordGenerator.git)
- [Password list (1.4 Billion Clear Text Password)](https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got)
### Wireless attack tools
- [WiFi-Pumpkin](https://github.com/P0cL4bs/wifipumpkin3)
- [pixiewps](https://github.com/wiire/pixiewps)
- [Bluetooth Honeypot GUI Framework](https://github.com/andrewmichaelsmith/bluepot)
- [Fluxion](https://github.com/thehackingsage/Fluxion)
- [Wifiphisher](https://github.com/wifiphisher/wifiphisher)
- [Wifite](https://github.com/derv82/wifite2)
- [EvilTwin](https://github.com/Z4nzu/fakeap)
- [Fastssh](https://github.com/Z4nzu/fastssh)
- Howmanypeople
### SQL Injection Tools
- [Sqlmap tool](https://github.com/sqlmapproject/sqlmap)
- [NoSqlMap](https://github.com/codingo/NoSQLMap)
- [Damn Small SQLi Scanner](https://github.com/stamparm/DSSS)
- [Explo](https://github.com/dtag-dev-sec/explo)
- [Blisqy - Exploit Time-based blind-SQL injection](https://github.com/JohnTroony/Blisqy)
- [Leviathan - Wide Range Mass Audit Toolkit](https://github.com/leviathan-framework/leviathan)
- [SQLScan](https://github.com/Cvar1984/sqlscan)
### Phishing attack tools
- [Setoolkit](https://github.com/trustedsec/social-engineer-toolkit)
- [SocialFish](https://github.com/UndeadSec/SocialFish)
- [HiddenEye](https://github.com/DarkSecDevelopers/HiddenEye)
- [Evilginx2](https://github.com/kgretzky/evilginx2)
- [I-See_You(Get Location using phishing attack)](https://github.com/Viralmaniar/I-See-You)
- [SayCheese (Grab target's Webcam Shots)](https://github.com/hangetzzu/saycheese)
- [QR Code Jacking](https://github.com/cryptedwolf/ohmyqr)
- [ShellPhish](https://github.com/An0nUD4Y/shellphish)
- [BlackPhish](https://github.com/iinc0gnit0/BlackPhish)
### Web Attack tools
- [Web2Attack](https://github.com/santatic/web2attack)
- Skipfish
- [SubDomain Finder](https://github.com/aboul3la/Sublist3r)
- [CheckURL](https://github.com/UndeadSec/checkURL)
- [Blazy(Also Find ClickJacking)](https://github.com/UltimateHackers/Blazy)
- [Sub-Domain TakeOver](https://github.com/m4ll0k/takeover)
- [Dirb](https://gitlab.com/kalilinux/packages/dirb)
### Post exploitation tools
- [Vegile - Ghost In The Shell](https://github.com/Screetsec/Vegile)
- [Chrome Keylogger](https://github.com/UndeadSec/HeraKeylogger)
### Forensic tools
- Autopsy
- Wireshark
- [Bulk extractor](https://github.com/simsong/bulk_extractor)
- [Disk Clone and ISO Image Acquire](https://guymager.sourceforge.io/)
- [Toolsley](https://www.toolsley.com/)
### Payload creation tools
- [The FatRat](https://github.com/Screetsec/TheFatRat)
- [Brutal](https://github.com/Screetsec/Brutal)
- [Stitch](https://nathanlopez.github.io/Stitch)
- [MSFvenom Payload Creator](https://github.com/g0tmi1k/msfpc)
- [Venom Shellcode Generator](https://github.com/r00t-3xp10it/venom)
- [Spycam](https://github.com/indexnotfound404/spycam)
- [Mob-Droid](https://github.com/kinghacker0/Mob-Droid)
- [Enigma](https://github.com/UndeadSec/Enigma)
### Exploit framework
- [RouterSploit](https://github.com/threat9/routersploit)
- [WebSploit](https://github.com/The404Hacking/websploit )
- [Commix](https://github.com/commixproject/commix)
- [Web2Attack](https://github.com/santatic/web2attack)
### Reverse engineering tools
- [Androguard](https://github.com/androguard/androguard )
- [Apk2Gold](https://github.com/lxdvs/apk2gold )
- [JadX](https://github.com/skylot/jadx)
### DDOS Attack Tools
- SlowLoris
- [Asyncrone | Multifunction SYN Flood DDoS Weapon](https://github.com/fatihsnsy/aSYNcrone)
- [UFOnet](https://github.com/epsylon/ufonet)
- [GoldenEye](https://github.com/jseidl/GoldenEye)
### Remote Administrator Tools (RAT)
- [Stitch](https://github.com/nathanlopez/Stitch)
- [Pyshell](https://github.com/knassar702/pyshell)
### XSS Attack Tools
- [DalFox(Finder of XSS)](https://github.com/hahwul/dalfox)
- [XSS Payload Generator](https://github.com/capture0x/XSS-LOADER.git)
- [Extended XSS Searcher and Finder](https://github.com/Damian89/extended-xss-search)
- [XSS-Freak](https://github.com/PR0PH3CY33/XSS-Freak)
- [XSpear](https://github.com/hahwul/XSpear)
- [XSSCon](https://github.com/menkrep1337/XSSCon)
- [XanXSS](https://github.com/Ekultek/XanXSS)
- [Advanced XSS Detection Suite](https://github.com/UltimateHackers/XSStrike)
- [RVuln](https://github.com/iinc0gnit0/RVuln)
- [Cyclops](https://github.com/v8blink/Chromium-based-XSS-Taint-Tracking) 
### Steganograhy tools
- SteganoHide
- StegnoCracker
- [StegoCracker](https://github.com/W1LDN16H7/StegoCracker)
- [Whitespace](https://github.com/beardog108/snow10)
### Other tools
#### SocialMedia Bruteforce
- [Instagram Attack](https://github.com/chinoogawa/instaBrute)
- [AllinOne SocialMedia Attack](https://github.com/Matrix07ksa/Brute_Force)
- [Facebook Attack](https://github.com/Matrix07ksa/Brute_Force)
- [Application Checker](https://github.com/jakuta-tech/underhanded)
#### Android Hacking tools
- [Keydroid](https://github.com/F4dl0/keydroid)
- [MySMS](https://github.com/papusingh2sms/mysms)
- [Lockphish (Grab target LOCK PIN)](https://github.com/JasonJerry/lockphish)
- [DroidCam (Capture Image)](https://github.com/kinghacker0/WishFish)
- [EvilApp (Hijack Session)](https://github.com/crypticterminal/EvilApp)
- [HatCloud(Bypass CloudFlare for IP)](https://github.com/HatBashBR/HatCloud)
#### IDN Homograph Attack
- [EvilURL](https://github.com/UndeadSec/EvilURL)
#### Email Verify tools
- [Knockmail](https://github.com/4w4k3/KnockMail)
#### Hash cracking tools
- [Hash Buster](https://github.com/s0md3v/Hash-Buster)
#### Wifi Deauthenticate
- [WifiJammer-NG](https://github.com/MisterBianco/wifijammer-ng)
- [KawaiiDeauther](https://github.com/aryanrtm/KawaiiDeauther)
#### SocialMedia Finder
- [Find SocialMedia By Facial Recognation System](https://github.com/Greenwolf/social_mapper)
- [Find SocialMedia By UserName](https://github.com/xHak9x/finduser)
- [Sherlock](https://github.com/sherlock-project/sherlock)
- [SocialScan | Username or Email](https://github.com/iojw/socialscan)
#### Payload Injector
- [Debinject](https://github.com/UndeadSec/Debinject)
- [Pixload](https://github.com/chinarulezzz/pixload)
#### Web crawling
- [Gospider](https://github.com/jaeles-project/gospider)
#### Mix tools
- Terminal Multiplexer


![](https://github.com/Z4nzu/hackingtool/blob/master/images/A00.png)
![](https://github.com/Z4nzu/hackingtool/blob/master/images/A0.png)
![](https://github.com/Z4nzu/hackingtool/blob/master/images/A1.png)
![](https://github.com/Z4nzu/hackingtool/blob/master/images/A2.png)
![](https://github.com/Z4nzu/hackingtool/blob/master/images/A4.png)

## Installation For Linux <img src="https://konpa.github.io/devicon/devicon.git/icons/linux/linux-original.svg" alt="linux" width="25" height="25"/></p><p align="center">

#### This Tool Must Run As ROOT !!!

    git clone https://github.com/Z4nzu/hackingtool.git
    
    chmod -R 755 hackingtool  
    
    cd hackingtool
    
    sudo bash install.sh
    
    sudo hackingtool

 After Following All Steps Just Type In Terminal **root@kaliLinux:~** **hackingtool**

## Use image with Docker

### Run in one click
`docker run -it vgpastor/hackingtool`

### Build locally
`docker-compose build`

`docker-compose run hackingtool`

- If need open other ports you can edit the docker-compose.yml file
- Volumes are mounted in the container to persist data and can share files between the host and the container


#### Thanks to original Author of the tools used in hackingtool

<img src ="https://img.shields.io/badge/Important-notice-red" />
<h4>Please Don't Use for illegal Activity</h4>

### To do 
- [ ] Release Tool 
- [ ] Add Tools for CTF
- [ ] Want to do automatic 

## Social Media :mailbox_with_no_mail:
[![Twitter](https://img.shields.io/twitter/url?color=%231DA1F2&label=follow&logo=twitter&logoColor=%231DA1F2&style=flat-square&url=https%3A%2F%2Fwww.reddit.com%2Fuser%2FFatChicken277)](https://twitter.com/_Zinzu07)
[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github&link=https://github.com/Z4nzu/)](https://github.com/Z4nzu/)
##### Your Favourite Tool is not in hackingtool or Suggestions Please [CLICK HERE](https://forms.gle/b235JoCKyUq5iM3t8)
![Z4nzu's github stats](https://github-readme-stats.vercel.app/api?username=Z4nzu&show_icons=true&title_color=fff&icon_color=79ff97&text_color=9f9f9f&bg_color=151515)

#### Don't Forgot to share with Your Friends 
### The new Update get will soon stay updated
#### Thank you..!!

---
## [Kelprunner/coyote-bayou](https://github.com/Kelprunner/coyote-bayou)@[856955c45a...](https://github.com/Kelprunner/coyote-bayou/commit/856955c45acda58a4ebab15a67ce4d6e96280e4a)
#### Sunday 2023-05-21 21:18:55 by Tk420634

Redlick & Garland City Take 2

Fuck you to, strong dmm

---
## [crawl/crawl](https://github.com/crawl/crawl)@[23a37c35b7...](https://github.com/crawl/crawl/commit/23a37c35b79dbd581fed2f45b95338651489e7b7)
#### Sunday 2023-05-21 21:36:33 by Nicholas Feinberg

Rework the dreamshard necklace

Getting an extra life in a roguelike is an insanely, wildly strong
effect. This made the dreamshard necklace a ludicrously strong item,
but not one that made the game feel more exciting. Instead, one's
character felt a bit weaker most of the time.

Let's try to fix both sides of this. To make the amulet a bit more
fun to wear, give it Acrobat - good for running away :) To make it
less preposterously strong (and thus possible that a really good
unrand or randart amulet could be preferable), make it only restore
the player to 1 HP when it triggers (rather than 50-100% of MHP),
but guarantee that they won't die until their next turn. To simplify,
make it only trigger when the player's HP drops to 0, rather than
sometimes triggering on very big hits, and remove *Drain.

Finally, make it stick around as a normal amulet of the acrobat after
it triggers, for running away synergy.

Let's try this out.

---
## [Anktratten/Poggy-3](https://github.com/Anktratten/Poggy-3)@[85ce614143...](https://github.com/Anktratten/Poggy-3/commit/85ce6141434a10a342d2eda389e688e229371d0d)
#### Sunday 2023-05-21 21:42:23 by Anktratten

Fuckin penis fart or some shit i hate this so much but its done now

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[7e68ba7f28...](https://github.com/k21971/EvilHack/commit/7e68ba7f28d1ef6ef6ee56935eb86aa5160b8993)
#### Sunday 2023-05-21 21:48:35 by saltwaterterrapin@gmail.com

Fix snuff_light_source

The two callers of snuff_light_source disagree about what it's supposed to do, and they're both wrong anyway. Make snuff_light_source work as set_lit expects, snuffing all snuffable sources on a given square. While I was at it, I also removed the snuffing code from litroom, since set_lit will snuff the player's inventory. This means that the player's inventory is only affected by drow darkness if they are within the actual area of affect of the darkness, which seems logical to me.

mpickobj also called snuff_light_source, expecting it to snuff a particular object. Instead, it could affect any light source on the square, allowing you to e.g. drop light sources in engulfers and have them stay lit, provided you were carrying another light source that had been lit for longer, which was weird. But kinda cool. But definitely wrong. Replace the snuff_light_source call with end_burn(), which targets the specific object that has been picked up.

---
## [crawl/crawl](https://github.com/crawl/crawl)@[39cede6f93...](https://github.com/crawl/crawl/commit/39cede6f937497c50376fd57df79c91e5373edbe)
#### Sunday 2023-05-21 21:49:09 by Nicholas Feinberg

Make Djinn use all skills (elliptic)

Because Djinn don't choose what spells they get, they need to have
unified spell school training. That ensures that, if they choose to
train magic, they can use whichever spells they get.

I initially implemented this by making Djinn *only* use Spellcasting
for magic. This was simple, which is good! But it had several issues:

- It prevented use of pain weapons & elemental staff melee, which
  was a recurring source of confusion for players.
- The low apt for Spellcasting felt bad, even though Djinn were still
  very strong.
- It meant that many types of items, like manuals of Fire Magic, were
  useless.
- It made Ashenzari Introspection curses ludicrously dominant.

Instead, let's make Djinn able to use all magic skills, as usual.
Furthermore, let's give them a ludicrous +11 apt in all spell schools
and Spellcasting, enough to let them train every one at once at the
same rate the old Spellcasting apt provided. However! The player can
only enable *all* magic skills or *none* - magic skills can't be
trained separately.

In practice, this is mostly equivalent to the old system, with the
exception of fixing the problems listed above and a few other caveats.
(For example, Ru Arcana sacrifices now work and 'waste' XP, like
sacrificing skills on a gnoll.) I'm hopeful it should feel much better.
(It's a slight buff to dj spell starts, due to how skills round.)

This needs playtesting both for bugs and to make sure the starting
skill setup works right. I'm quite scared. Fingers crossed...

---
## [HanSolo1519/coyote-bayou](https://github.com/HanSolo1519/coyote-bayou)@[6fd64b92ca...](https://github.com/HanSolo1519/coyote-bayou/commit/6fd64b92ca4cc80357d8d78c8efc1c6d8196204f)
#### Sunday 2023-05-21 22:00:06 by Tk420634

Updating the Mansion a bit

Preparing my brain for making a non euclidian dungeon, because I fucking hate everything.

---
## [CsabaVas44/Armored_Rampage](https://github.com/CsabaVas44/Armored_Rampage)@[c7f14921ef...](https://github.com/CsabaVas44/Armored_Rampage/commit/c7f14921efd693d2b24f90e465b5cbd85bfd2606)
#### Sunday 2023-05-21 22:16:58 by Karikó-Tóth Máté

It changed

Blad tarantula,
Time for the massive come sing ya,
Blad tarantula,
Don't play with my style I might sting ya,
Blad tarantula,
You want me inject me bacteria,
And if ya body goin' stiff,
And your spine goin' numb,
Now come for get some...
Time to fix you up something here right nowâ?¦
Shotter, hitter, serial killer,
Go a your funeral and all drink out your liquor,
When you are bury we a-stand next to the vicar,
Fling on some dirt and make your bury a little quicker,
Shouldn't test the youth them in the Tommy Hilfiger,
Hug up you mama, say sorry to you papa,
All a get number for the little sister
A shall we call her Ill ask her, freeza,

---
## [LynxSolstice/cmss13](https://github.com/LynxSolstice/cmss13)@[9bbac13b28...](https://github.com/LynxSolstice/cmss13/commit/9bbac13b2898570be5e448ce50ca110472561630)
#### Sunday 2023-05-21 23:45:34 by TotalEpicness

Globber balance overhaul (#3039)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request
Globber came out overtuned as shit and actually replicated some of the
issues that we didn't want like the dreaded ChokePoint Boiler Torture
Rebalances some issues that weren't forseen during the development nor
TM stage of globber. This should be TM'd


General changes:
- Globber C/D 25 seconds > 30 seconds ( the temp nerf PR didnt actually
fix this correctly)
- Fire deals 2x damage instead of 1.5x damage ( this needs significant
testing and will likely be toned down)
- Acid spray doesn't stun at full distances anymore

Depending on TM feedback, I might switch between these two variants of
this overhaul:

Rework variance 1: Keep zoom and current design while maintaining a
little toughness [currently on]
- Armor 25 > 20
-  Zoom halved 4 > 2
-  Dropped health a tier: 650 > 600
- Fire deals 2x damage instead of 1.25x damage
- Globber C/D

Rework variance 2: Embrace the zoom removal
- Directional armor 10 base armor + 20 at the front. Flank a globber to
kill it!
- Slight windup increase 5s > 6s
- Fire damage 1.25x > 1.5x

Fixes:

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

:cl: Totalepicness

balance: Rebalances globber, which has come out overtuned. Globber now
has reduced health, armor and zoom along with higher fire damage
multiplier.
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---------

Co-authored-by: Epicness <coolguyethanw@gmail.com>
Co-authored-by: morrowwolf <darthbane97@gmail.com>

---
## [LynxSolstice/cmss13](https://github.com/LynxSolstice/cmss13)@[a2d5ca6e69...](https://github.com/LynxSolstice/cmss13/commit/a2d5ca6e69725341f0fa261a4a3f89c737e843b3)
#### Sunday 2023-05-21 23:48:33 by QuickLode

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

