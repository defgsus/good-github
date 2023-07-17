## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-07-16](docs/good-messages/2023/2023-07-16.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 1,784,945 were push events containing 2,532,424 commit messages that amount to 142,920,390 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 46 messages:


## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[cfd40aeef5...](https://github.com/tgstation/tgstation/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Sunday 2023-07-16 00:02:55 by necromanceranne

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
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[52c8da7ea4...](https://github.com/tgstation/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Sunday 2023-07-16 00:02:55 by Jacquerel

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
## [MahadKhattak/Hearts](https://github.com/MahadKhattak/Hearts)@[834f0b2450...](https://github.com/MahadKhattak/Hearts/commit/834f0b24504f92ba3d3c13acf80b5db25803d07a)
#### Sunday 2023-07-16 00:43:54 by MahadKhattak

The game is done. I won't add save and load features, because let's be honest, who's going to save and load a game of Hearts?

The "breaking hearts before being able to start with a Hearts card" is a rule that I dislike, so I won't include it, though it should be easy to include. Other than that, the game should work perfectly fine: will test later with my friends.

Personal note if I want to come back to this project at any time in the future:
You can add save, load features
You COULD add the Hearts suit rule, depending on feedback. Just modify the playCard() method.

This was a nice learning experience, and the game turned out not bad. Some UI updates are possible too if I want in the future, though I want to focus on other stuff now as well.

Whoever visited this, thanks for exploring, coding this was kinda fun

---
## [SPLURT-Station/S.P.L.U.R.T-Station-13](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13)@[defdf2f6b2...](https://github.com/SPLURT-Station/S.P.L.U.R.T-Station-13/commit/defdf2f6b2269cd8fc953ef71219109159ddfcd4)
#### Sunday 2023-07-16 00:46:17 by PhazeJump

FIXING MY OWN SHIT CODE MAKES ME FUCKING SCREAM

anyways
techpriest robes are now un-shitty-fixed and fixed again. Should be working properly now. No idea how to get the naga taur sprite working because it was supposed to be added in sand modular but sand modular was the one breaking it all so :shrug:

---
## [ZeBruhW/Sisyphus-Simulator](https://github.com/ZeBruhW/Sisyphus-Simulator)@[3115ec3578...](https://github.com/ZeBruhW/Sisyphus-Simulator/commit/3115ec3578e87ed672ffd35e5070a0440595531e)
#### Sunday 2023-07-16 00:54:11 by Ruby 3

Fiddled around with the tiling.

This sshit fucking sucks. I hate doing this. Fuck me.

---
## [BlueMemesauce/tgstation](https://github.com/BlueMemesauce/tgstation)@[16cecf864d...](https://github.com/BlueMemesauce/tgstation/commit/16cecf864d4b6ff864956cbc9d0cf7af4cfe1f26)
#### Sunday 2023-07-16 01:16:33 by Jacquerel

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
## [realforest2001/forest-cm13](https://github.com/realforest2001/forest-cm13)@[5f5fcd2b27...](https://github.com/realforest2001/forest-cm13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Sunday 2023-07-16 01:19:07 by Drathek

Fix marines not getting first dibs if they ghost (#3802)

# About the pull request

This PR fixes an issue where hugged marines that burst were not getting
first dibs on the larva if they ghosted. Previously the mind maybe
wasn't cleared out to find the ghost mob, but it currently is.

NOTE: The existing check requiring the marine to be nested is still in
place to get first dibs. I'm honestly not sure if this check should
still exist. On one hand I can agree it might be hard for the marine
trying to get help to suddenly become the larva and switch gears - they
are still going to be in the mindset of a marine that the larva should
die. But its also sort of weird to only get the first dibs if nested. If
xenos are unnesting hugged marines just before they pop, thats already a
mechanic abuse that should be ahelped; but ideally there wouldn't be
anything to be abused. Also, some may consider this kind of larva
undesirable anyways so maybe they'd prefer the marine to have it... So
let me know if I should just remove the nested check on line 151.

# Explain why it's good for the game

Fixes an unintended consequence of ghosting when hugged that would
prevent that marine from getting their first dibs on the larva.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>


![dibs](https://github.com/cmss13-devs/cmss13/assets/76988376/84e44345-2b83-473f-9997-f7865bcef1dd)

</details>


# Changelog
:cl: Drathek
fix: Fix ghosting preventing first dibs on the larva in a hugged marine
/:cl:

---
## [DATA-xPUNGED/DataStation](https://github.com/DATA-xPUNGED/DataStation)@[2ee79d7077...](https://github.com/DATA-xPUNGED/DataStation/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Sunday 2023-07-16 01:25:05 by Jacquerel

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
## [tommysalami3/tgstation](https://github.com/tommysalami3/tgstation)@[d12cab7a49...](https://github.com/tommysalami3/tgstation/commit/d12cab7a498f64df366eba748175405f8fd0ffef)
#### Sunday 2023-07-16 01:27:14 by Sealed101

Collapsible lobby buttons (#76443)

## About The Pull Request
Adds a button to the new player HUD that allows collapsing and expanding
the menu buttons.
Also gives the buttons names so they can show up in the BYOND's prompt
on the bottom left.
Readiness is now also displayed in the status tab.
The menu HUD can be reset with a verb Reset Lobby Menu HUD in the OOC
tab.

### I SAW FOOTAGE


https://github.com/tgstation/tgstation/assets/75863639/2054c09d-48d7-4736-b862-4406667dde67

#### Here be dragons (dev progress footage)

#### GACHI BGM WARNING
<details><summary>Mk. I </summary>


https://github.com/tgstation/tgstation/assets/75863639/3e886254-bebd-4aa3-b7f7-5fdd8b7c9040

</details> 

___

<details><summary>Mk. II</summary>


https://github.com/tgstation/tgstation/assets/75863639/14d84a2d-1732-4700-aad0-df85c9befa86

</details> 

___

<details><summary>Mk. III (featuring: the shutter!) ((NOT featuring:
gachi BGM))</summary>


https://github.com/tgstation/tgstation/assets/75863639/98576c1f-6877-41b9-bec6-e11207501965


</details> 

___

<details><summary>Mk. IV (new collapse button sprite )</summary>

~~& shutter graffiti~~ (in a followup PR)

this video has a bug with the poll button lighting up without an active
poll, this was fixed before it was pushed


https://github.com/tgstation/tgstation/assets/75863639/6c0489e2-c80a-4682-b543-5d7c74071a39

</details> 

___

<details><summary>Mk. IV with updated shutter sprite and animation
speed</summary>

<sub>TIL github sanitizes ♂ and probably other ascii from file
names</sub>


https://github.com/tgstation/tgstation/assets/75863639/61ed85fe-8df6-4f38-91aa-1f70258289e7

</details> 

## TO-DO
- [x] A shutter that comes down and hides the buttons away. 
  - [ ] The shutter will have a chance to have silly graffiti on it.
- [x] Redesign and move the collapse/expand button to be a part of the
menu.

## Why It's Good For The Game
Banishes the curse cast upon lobby art. Ties in with the on-going lobby
art contest.


## Changelog
:cl:
qol: Lobby Menu buttons can now be collapsed. Rejoice!
qol: Lobby Menu buttons have names, which can be seen in the prompt on
the bottom left of the viewport.
qol: you may see your readiness status during pre-game in the Status
Bar.
qol: Reset Lobby Menu HUD verb added in case you manage to break the
damn thing.
/:cl:

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[4537b1e980...](https://github.com/Sonic121x/Skyrat-tg/commit/4537b1e980f226f2f6a18ef1c92d6ffc3e3b6ac4)
#### Sunday 2023-07-16 01:46:42 by Bloop

[MISSED MIRROR] New space ambient track (#76547) (#22449)

New space ambient track (#76547)

## About The Pull Request

Adds a new space ambient track made by me to the game, supposed to be a
bit scarier than the others that were recently added as I feel that
they're a bit too happy (not to diss I really like them), also cleaned
up a bit of ambience.dm as the medical portion of it didn't follow the
same rules as the other ones. also also this will only be used for
tgstation so license wise I think this is CC BY-SA 3.0 but I'm not sure
so correct me if I'm wrong, also this is my first PR so yeah. Here's a
link to listen to the track https://voca.ro/18WvrGORDDdR

## Why It's Good For The Game

Variety is the spice of life.

## Changelog

:cl:
sound: A new ambient track will now play in space
/:cl:

Co-authored-by: atlasle <132299254+atlasle@users.noreply.github.com>

---
## [ghostsheet/cmss13](https://github.com/ghostsheet/cmss13)@[d26452bb9a...](https://github.com/ghostsheet/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Sunday 2023-07-16 02:09:41 by Unknownity

Burrower burrow changes and fixes (#3818)

# About the pull request

The PR contains mostly fixes for the Burrower that have been around,
that being that other xenos could slash them while they were burrowed,
that they could resist (and get rid of fire) while burrowed, that they
still took shrapnel and direct flame damage while burrowed, that SG
autofire and sentries were shooting at a burrowed burrower, wasting ammo
in the process.

Two other notable changes are that the unburrow stun now also works on
other non-friendly xenomorphs (and it works on all of them, skill issue
if you manage to get stunned from that as a T3/Queen) and that burrowing
and unburrowing now has sounds (a change many people were positive about
when it was initially included in the Impaler PR) which may find
tracking and noticing the presence of burrowers easier.

burrowing sound: https://voca.ro/1dQ0pvBMidsr
unburrowing sound: https://vocaroo.com/1zzEz3NQ2Kx5

# Explain why it's good for the game

Bugfixes and a counter to one of the most annoying abilities (that
people consider) in the game.


# Testing Photographs and Procedure

<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Unknownity
fix: Fixed burrowed mobs being able to be targeted by sentries, mines
and SG autofire.
fix: Fixed burrowed mobs being able to grab mobs on the surface.
fix: Fixed burrowed mobs being able to resist while burrowed.
fix: Fixed burrowers taking damage from direct flame and shrapnel from
explosions.
fix: Fixed burrowers being able to get slashed from enemy Xenos on the
surface.
fix: Fixed burrowers unburrow stun to now properly target and stun enemy
Xenos.
soundadd: Added sounds for the Burrower when they are burrowing and
unburrowing.
/:cl:

Co-authored-by: Unknownity <a>

---
## [RawToast225/space-station-14](https://github.com/RawToast225/space-station-14)@[06747e0f7e...](https://github.com/RawToast225/space-station-14/commit/06747e0f7e7d04cf87e63a359a3a86b1a35442cc)
#### Sunday 2023-07-16 02:27:12 by Emisse

some silly paintings and posters (#17872)

* webedit

* Update meta.json

* god is real hes here with us

* so true

* so truers rise

* worst meta.json ive seen in my life

* so true

---
## [LaylBongers/bevy](https://github.com/LaylBongers/bevy)@[fb4c21e3e6...](https://github.com/LaylBongers/bevy/commit/fb4c21e3e62b3789e8e768ac63dc2205ddec698f)
#### Sunday 2023-07-16 02:41:18 by Ida "Iyes

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
## [Sagnac/streamsave](https://github.com/Sagnac/streamsave)@[b707426ff4...](https://github.com/Sagnac/streamsave/commit/b707426ff45c3abc6110a0c09866db8559c7f61c)
#### Sunday 2023-07-16 02:54:19 by Sagnac

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
## [makton-dev/benchmark](https://github.com/makton-dev/benchmark)@[745644f391...](https://github.com/makton-dev/benchmark/commit/745644f391b4d11da107b2c82fe2d7a3eacf561d)
#### Sunday 2023-07-16 04:04:47 by Mark Saroufim

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
## [Aquamanng/KikiDanceoff](https://github.com/Aquamanng/KikiDanceoff)@[6036304d32...](https://github.com/Aquamanng/KikiDanceoff/commit/6036304d32326a76b2779c9cec3cdccdb255da0d)
#### Sunday 2023-07-16 04:43:01 by Aqua

killed old shitty code

i stole it from a tutorial and then realized that tutorial sucked fucking dogshit and then also realized my approach of MANUALLY EYEBALLING ALL THE FUCKING NOTES AND PLACING THEM AND PRAYING THEY'D BE TIMED CORRECTLY WAS ALSO SUPER SUPER FUCKING STUPID!!!! thank god i figured it out in the end holy fuckeroni

---
## [ChSatyaSavith/LeetCode](https://github.com/ChSatyaSavith/LeetCode)@[567a6a48a0...](https://github.com/ChSatyaSavith/LeetCode/commit/567a6a48a0d49bd9dccd09f8b9971699b6e31886)
#### Sunday 2023-07-16 05:11:26 by NotFluent

thoda bhot try kara but utta samajh nhi aya, im starting to accept the fact that im just plain old stupid, lmao, please somebody come and kill me for fucks sake. aahhh dimag kharab hogya bhot zyada im tired , report bhi banana hai holy fuck, ig ill copy for now, but no more just plain old copying in the future.

---
## [Huffie56/cmss13](https://github.com/Huffie56/cmss13)@[e8f53984c1...](https://github.com/Huffie56/cmss13/commit/e8f53984c1edd98c25b4c3199a6a5363eaa26869)
#### Sunday 2023-07-16 09:08:04 by morrowwolf

Warrior Nerf (#3424)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

# About the pull request

This PR removes cooldown reduction on slash.

This PR slightly lowers fling and punch cooldowns.

This PR lowers fling stun to a micro stun and adds a slow.

This PR decreases lunge range to 4 tiles.

As a reminder design feedback and balance concerns go here:
https://forum.cm-ss13.com/w/pr-feedback/steps/step_1

# Explain why it's good for the game

Warrior rework has been on my mind for a while. I'm not quite sure how I
want to do it. The cooldowns on abilities and the abilities themselves
are incredibly powerful crowd control and just a few warriors can do
immense damage to large groups of marines. It's just... not in a great
place for a T2 and sadly I don't have a thorough game plan yet to rework
it into something more bearable while equally enjoyable to play. In the
mean time, this is what we're getting. Am I promising a rework in the
near future? Not really. It's on my list somewhere. Does warrior need
some changing around? Yeah.

Overall, this should make warrior a bit more bearable. We'll see. More
changes as testing goes.

# Testing Photographs and Procedure
<!-- Include any screenshots/videos/debugging steps of the modified code
functioning successfully, ideally including edge cases. -->
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog

:cl: Morrow
balance: Removes warrior cooldown reduction on slash
balance: Warrior slightly lowered fling and punch cooldowns
balance: Lowers fling stun to a micro stun and adds a slow
balance: Decreases warrior lunge range to 4 tiles
/:cl:

<!-- Both :cl:'s are required for the changelog to work! -->

---
## [valorazesus/Skyrat-tg](https://github.com/valorazesus/Skyrat-tg)@[56d6df5539...](https://github.com/valorazesus/Skyrat-tg/commit/56d6df55396752f8df1e25246fdc18851d6aa5b3)
#### Sunday 2023-07-16 10:03:17 by SkyratBot

[MIRROR] Removes suicide check from positronic brains [MDB IGNORE] (#21895)

* Removes suicide check from positronic brains (#76081)

# About The Pull Request

This removes the suicide check from positronic brains.

# Why It's Good For The Game

There seems to be 2 arguments for why suicide should forbid ghost roles:
1. "If they suicided they didn't want to play"
2. "antag rolling"

So let's look at each.

And an addendum on scope: This is meant only to apply to ghost roles
(and new characters from said roles); I do not wish to change that
people are not allowed back onto the same character they suicided on.

## "Suiciders left the round of their own choice and shouldn't be
allowed back in"

There are many, many ways in this game to end up with a character in a
state that's nearly/effectively unplayable, even if the controlling
player doesn't truly wish to completely leave. Some things can be
resolved with competent medical or science staff, but competent staff
are not always available in a round or might be beleaguered by round
events.

Then there are a number of conditions/states which the game provides no
path to resolve (save drastic measures like abandoning the
character/body, of course).

Or one might have simply become stuck in a place where rescue is
unlikely.

## Antag rolling

The problem here is this code does not particularly target antag
rollers. It paints such a broad brush that it simply catches everyone
whom might not know "No no, you have to **ghost** here, not suicide".
Even if an antag roller is stopped once, they'll easily bypass it next
time through the many, many means open to them - and if 'ghost' is made
effectively the same as 'suicide', it simply punishes people who got
stuck or similar even more.

Because of the wide range of means to kill oneself on a normal
character, to effectively stop antag rolling requires discerning intent
through context and patterns of one's actions. This might not be
possible in code until General Intelligence is a solved problem, and if
it is possible, this doesn't do it. It's a shotgun that kills everyone
in the room and if there happened to be an antag roller there, well,
even a stopped clock is right twice a day.

And then, of course, that the code was broken for so long would seem to
indicate it's not done that much.

## Practical Impact and Design Philosophy

Just from my personal observations, even wanting into a posibrain is a
niche thing usually only taken by a small number of the same players
round-to-round. In practice, whether this PR is merged or not likely
won't have a great impact on the game. But that could change if the
philosophy behind this check is applied to a wider number of things.

If someone wants to die, it's not hard. Walk out an airlock. Into the
supermatter. Blob, Xenos, or some other hazard present? Walk towards
them. Step in front of a shuttle. Turn on internals and wait a bit.
Countless other ways. Except, perhaps, if a character is disabled or
crippled or stuck, in which case use of a verb may be necessary.

In other games with much narrower sets of mechanics, it may be possible
to close certain paths on the assumption it would mostly be used for bad
faith reasons. In SS13, the sheer number of ways in which a good faith
character be "screwed" but not quite killed off, and which a bad faith
actor can find to kill themselves while bypassing restrictions placed on
verbs, means that I think this code's design philosophy is harmful to
the game and its good faith players.

# Changelog

:cl:
del: Positronic brains no longer check for suicide verb use.
/:cl:

* Removes suicide check from positronic brains

---------

Co-authored-by: YehnBeep <86855173+YehnBeep@users.noreply.github.com>

---
## [MAGREMENT/SudokuSolver](https://github.com/MAGREMENT/SudokuSolver)@[64627a43b3...](https://github.com/MAGREMENT/SudokuSolver/commit/64627a43b3e46e75abd59992cb563a6d6d77405f)
#### Sunday 2023-07-16 10:37:55 by Zachary VANVLASSELAER

Added X-Cycles and it works AND I DONT KNOW WHY FUCKING PIECE OF SHIT WHY DOES THE CORRECT WAY NOT WORK BUT THE STUPID ASS WAY DOES WORK WTFFFF

---
## [Aquib341/Spotify-Clone](https://github.com/Aquib341/Spotify-Clone)@[29a3ba0a8a...](https://github.com/Aquib341/Spotify-Clone/commit/29a3ba0a8a47aa93efb479b6e28dc15ae5f925f4)
#### Sunday 2023-07-16 10:45:29 by MD AQUIB

Spotify-Clone

Immerse yourself in the world of music streaming with my meticulously crafted project - the Professional Sportify Clone. Built with expertise in HTML, CSS, and JavaScript, this creation showcases an exceptional level of professionalism.

From the moment you enter the Sportify Clone, you'll be captivated by its adept design and seamless functionality. Meticulous attention to detail has been paid to ensure a visually stunning and user-friendly interface that emulates the charm of the original platform.

HTML forms the backbone of this project, enabling a structured and organized layout that is both logical and intuitive. CSS adds a layer of sophistication, elevating the design aesthetics to match industry standards. Every element has been meticulously styled to create a seamless and visually appealing experience for the user.

JavaScript unlocks the power of interactivity within the Sportify Clone. Sophisticated features such as user authentication, dynamic playlist creation, intuitive song search, and robust playback controls have been seamlessly integrated into the project. The end result is an engaging and immersive music streaming experience that rivals the original Sportify platform.

Responsive design has been a priority throughout the development process, ensuring that the clone is fully compatible with a range of devices - be it desktops, laptops, tablets, or mobile phones. Users can enjoy their favorite music seamlessly across all screen sizes without any compromise in functionality or visual appeal.

The Professional Sportify Clone is a testament to my web development skills, showcasing not only technical prowess but also the ability to dissect and replicate complex systems. By studying the nuances of the original Sportify platform, I have successfully captured its essence and translated it into a polished, professional-grade project.

Discover the Professional Sportify Clone and experience a harmonious fusion of HTML, CSS, and JS. Roam through an extensive music library, create custom playlists, and delight in a flawless music streaming experience. This project stands as a testament to my unwavering commitment to delivering high-quality, professional-grade web development solutions.

Please note that the Professional Sportify Clone is a personal project and not affiliated with the official Sportify platform. With dedication and passion, I present this clone as a testament to my abilities and commitment to excellence.

---
## [jdlcdl/seedsigner](https://github.com/jdlcdl/seedsigner)@[d2a657f2d4...](https://github.com/jdlcdl/seedsigner/commit/d2a657f2d43c6e77e9c48cb1f859e8f4984a5f00)
#### Sunday 2023-07-16 11:03:09 by Marc G

Various edits B4 upstream submission

After a long hiatus, I have finally completed my proposed changes to the software verification section of our readme.

The verification focuses on keybase.io now storing and verifying the 3 online properties (seedsigner.com, twitter.com/seedsigner and github.com/seedsigner)

This makes the key more secure, easier to import and generally less hassle. its also revokable.  

There is more detail about how/why in the expand blocks, but It was suggested to me to keep the instructions straightforward (ie do this and now do that) , so I have reduced focus much on the why. 
However, some basic "why & how" has also been placed in new collapsible sections, at the end of each step. 

Later on, I want to add color to the collapse sections so that they show a natural boundary, but so far that markdown code is elusive to me. ;) 
Done is better than perfect....
The same for getting my external links to open in a new tab/window. sigh. Markdown is ... well....tricky. 

I can make the screenshots smaller. please comment on their size.


The Verification is done in 3 steps:
1. import the public key
2. Verify its the correct key by verying it and then comparing the Key ID to Keybase.io/seedsigner. If it matches, then its the real seedsigner project person that signed.
this is arguablly the most critical step of verifying and hence we ask the user to check for themselves that the key ID from verify is the same as on keybase.io. Hence the Key ID's are blurred in the screenshots. We dont want the user to compare the screenshots to each other. we want them to compare their result to their browser. 

3. Verify that the other files (at this stage just the .zip file) are also not altered. This does a comparision of the various files actual and expected hashes.

If all is well here, then tell the user about their success :). 
Explain the warnings, which ones are benign, and what to do if verification fails.


Lastly, "Write the software to the MicroSD' section - 
I have got draft text for this, but havent published it yet. 
The verify PR is big enough !!

Please review for my PR flow and clarity, I do still want to improve the formatting,  but wanted to get everyone's thoughts before messing with the detailed formatting and line breaks, which are especially painful!

FYI - I have done my screenshots using layers, so it easy to edit in the future. I think they

---
## [Phongsiri33013Winsan2020TH/Buryland_Resource_Pack](https://github.com/Phongsiri33013Winsan2020TH/Buryland_Resource_Pack)@[dad2fda92e...](https://github.com/Phongsiri33013Winsan2020TH/Buryland_Resource_Pack/commit/dad2fda92e83a3703121e5594b39c2a0c0b380a2)
#### Sunday 2023-07-16 11:15:57 by Phongsiri33013Winsan2020TH

entetsu

A hopeless romantic all my life
Surrounded by couples all the time
I guess I should take it as a sign

I'm feelin' lonely
Oh, I wish I'd find a lover that could hold me
Now I'm crying in my room
So skeptical of love
But still, I want it more, more, more

I gave a second chance to Cupid
But now I'm left here feelin' stupid
Oh, the way he makes me feel that love isn't real
Cupid is so dumb

Co-Authored-By: Mike Shafter <32269257+Mineshafter61@users.noreply.github.com>

---
## [kalcutter/linux](https://github.com/kalcutter/linux)@[ff7ddcf0db...](https://github.com/kalcutter/linux/commit/ff7ddcf0db48a7d9ae536eb0875428117be1d1f1)
#### Sunday 2023-07-16 11:40:04 by Linus Torvalds

Merge tag 'clk-for-linus' of git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux

Pull clk updates from Stephen Boyd:
 "This batch of clk driver updates contains almost no new SoC support.
  Instead there's a treewide patch series from Maxime that makes
  clk_ops::determine_rate mandatory for muxes.

  Beyond that core framework change we have the usual pile of clk driver
  updates such as migrating i2c drivers to use .probe() again or
  YAMLfication of clk DT bindings so we can validate DTBs.

  Overall the SoCs that got the most updates this time around in terms
  of diffstat are the Amlogic and Mediatek drivers because they added
  new SoC support or fixed up various drivers to have proper data.

  In general things look kinda quiet. I suspect the core framework
  change may still shake out some problems after the merge window,
  mostly because not everyone tests linux-next where that series has
  been for some number of weeks. I saw that there's at least one pending
  fix for Tegra that needs to be wrapped up into a proper patch. I'll
  try to catch those bits before the window closes so that -rc1 is
  bootable. More details below.

  Core:
   - Make clk_ops::determine_rate mandatory for muxes

  New Drivers:
   - Add amlogic a1 SoC family PLL and peripheral clock controller support

  Updates:
   - Handle allocation failures from kasprintf() and friends
   - Migrate platform clk drivers to .remove_new()
   - Migrate i2c clk drivers to .probe() instead of .probe_new()
   - Remove CLK_SET_PARENT from all Mediatek MSDC core clocks
   - Add infra_ao reset support for Mediatek MT8188 SoCs
   - Align driver_data to i2c_device_id tables in some i2c clk drivers
   - Use device_get_match_data() in vc5 clk driver
   - New Kconfig symbol name (SOC_MICROCHIP_POLARFIRE) for Microchip
     FPGA clock drivers
   - Use of_property_read_bool() to read "microchip,pic32mzda-sosc"
     boolean DT property in clk-pic32mzda
   - Convert AT91 clock dt-bindings to YAML
   - Remove CLK_SET_RATE_PARENT flag from LDB clocks on i.MX6SX
   - Keep i.MX UART clocks enabled during kernel boot if earlycon is set
   - Drop imx_unregister_clocks() as there are no users anymore
   - Switch to _safe iterator on imx_clk_scu_unregister() to avoid use
     after free
   - Add determine_rate op to the imx8m composite clock
   - Use device managed API for iomap and kzalloc for i.MXRT1050,
     i.MX8MN, i.MX8MP and i.MX93 clock controller drivers
   - Add missing interrupt DT property for the i.MX8M clock controller
   - Re-add support for Exynos4212 clock controller because we are
     re-introducing the SoC in the mainline
   - Add CONFIG_OF dependency to Samsung clk Kconfig symbols to solve
     some objtool warnings
   - Preselect PLL MIPI as TCON0 parent for Allwinner A64 SoC
   - Convert the Renesas clock drivers to readl_poll_timeout_atomic()
   - Add PWM clock on Renesas R-Car V3U
   - Fix PLL5 on Renesas RZ/G2L and RZ/V2L"

* tag 'clk-for-linus' of git://git.kernel.org/pub/scm/linux/kernel/git/clk/linux: (149 commits)
  clk: fix typo in clk_hw_register_fixed_rate_parent_data() macro
  clk: Fix memory leak in devm_clk_notifier_register()
  clk: mvebu: Iterate over possible CPUs instead of DT CPU nodes
  clk: mvebu: Use of_get_cpu_hwid() to read CPU ID
  MAINTAINERS: Add Marvell mvebu clock drivers
  clk: clocking-wizard: check return value of devm_kasprintf()
  clk: ti: clkctrl: check return value of kasprintf()
  clk: keystone: sci-clk: check return value of kasprintf()
  clk: si5341: free unused memory on probe failure
  clk: si5341: check return value of {devm_}kasprintf()
  clk: si5341: return error if one synth clock registration fails
  clk: cdce925: check return value of kasprintf()
  clk: vc5: check memory returned by kasprintf()
  clk: mediatek: clk-mt8173-apmixedsys: Fix iomap not released issue
  clk: mediatek: clk-mt8173-apmixedsys: Fix return value for of_iomap() error
  clk: mediatek: clk-mtk: Grab iomem pointer for divider clocks
  clk: keystone: syscon-clk: Add support for audio refclk
  dt-bindings: clock: Add binding documentation for TI Audio REFCLK
  dt-bindings: clock: ehrpwm: Remove unneeded syscon compatible
  clk: keystone: syscon-clk: Allow the clock node to not be of type syscon
  ...

---
## [aymanEjaz/Supervised-Machine-Learning](https://github.com/aymanEjaz/Supervised-Machine-Learning)@[cc526e00f8...](https://github.com/aymanEjaz/Supervised-Machine-Learning/commit/cc526e00f89146daa8d55f650be5d87734add986)
#### Sunday 2023-07-16 11:59:07 by Ayman Ijaz

Discover the Beauty of the Iris Dataset🌺📊

Exploring the Iris Dataset: Predicting Species with Logistic Regression 🌺📊

Welcome to the captivating world of the Iris dataset, where nature's beauty meets the power of data science! This enchanting dataset boasts five charming columns – sepal length, sepal width, petal length, petal width, and species – each holding secrets to the mesmerizing iris flowers.

Using the power of Logistic Regression, we'll predict the species of each iris flower, unraveling the hidden patterns that nature has to offer.
With every prediction, we'll unlock the wonders of data-driven insights, unveiling the captivating realm of iris flowers like never before. Come, join us on this delightful adventure and experience the magic of the Iris dataset! 🌟🌸"

---
## [TheLordME/Citadel-Station-13-RP](https://github.com/TheLordME/Citadel-Station-13-RP)@[1468797059...](https://github.com/TheLordME/Citadel-Station-13-RP/commit/146879705978b0416739823fa54467e865c3ffb2)
#### Sunday 2023-07-16 12:19:25 by TheObserver-sys

Take 2: Some fixes and QoL (#5601)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## About The Pull Request
Would you believe me if I hadn't updated my git in about 400 years, and
had to blow the old version of my repo up?
Yes? No? It doesn't matter.

Anyways! Meat and potatoes of this:
Allows players to make gene and plant discs freely in the protolathe.
Since we do not have a dedicated genetics, this will help the pains of
actually doing genetics by giving us storage solutions for genes.

Fixes a problem with brass also creating slag when compressing, by
setting the copper alloy flag to 1.

And finally: Allows you to upgrade the braces! If your brace has T3 or
better, a single brace can hold an entire drill. All credit goes to
Hatterhat for this one, as I pretty much wholesale ripped it from his
buff of the big drill™ on Virgo.
<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
Not making slag is ALWAYS good. It saves on material, too.
Having more discs for a cheap cost is also good, it means you can reduce
headaches while scoping out for genes, because there are many, and the
ability to track them are currently few.
And honestly, the less lugging a person has to do with the mining drill,
the more likely people might stop blowing up an already unstable planet
with miniature hydrogen bombs.
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

:cl: The0bserver
add: Discs are able to be produced in the protolathe now. Go nuts, or
don't. I'm not your guardian.
balance: Mining Drills can finally be operated with just one brace with
the requisite parts. Thank you, Hatterhat!
fix: Copper no longer smelts slag when set to "Alloying."
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: TheObserver-sys <Gizmomaster777@gmail.com>

---
## [JK0JK/Minigame-Investigator](https://github.com/JK0JK/Minigame-Investigator)@[74a7d84fd0...](https://github.com/JK0JK/Minigame-Investigator/commit/74a7d84fd0aa9bd801b64fd1f4b41332df3f800e)
#### Sunday 2023-07-16 13:40:59 by JK0JK

The Identity Update
Tried (in vain) to fix the problems with the palettes.
After some criticism from another FNaF fan-game creator (VillianousJ0ker), tried seeing how Chica would look like without the outline. The current file is his own interpretation of Chica, so we'd see how she looks without the outline.
I prefer her with the outline, but I do agree that these designs should be changed at some point.

I will make a branch from after the merge to see if I can fix the problem with the dynamic palettes.
If I'm successful, I'll merge the changes with main, solving conflicts almost exclusively using the branch.

After this is solved, we need to URGENTLY solve the thing with the voicegroups.

I want to fucking persona 3 awakening myself

---
## [kr45732/NotEnoughUpdates-REPO](https://github.com/kr45732/NotEnoughUpdates-REPO)@[e458513360...](https://github.com/kr45732/NotEnoughUpdates-REPO/commit/e4585133608ba4add475be13a9f414c989fe1b8b)
#### Sunday 2023-07-16 14:18:42 by jani270

Fixed lore of Arrow Poison (#958)

Before disabling any content in relation to this takedown notice, GitHub
- contacted the owners of some or all of the affected repositories to give them an opportunity to [make changes](https://docs.github.com/en/github/site-policy/dmca-takedown-policy#a-how-does-this-actually-work).
- provided information on how to [submit a DMCA Counter Notice](https://docs.github.com/en/articles/guide-to-submitting-a-dmca-counter-notice).

To learn about when and why GitHub may process some notices this way, please visit our [README](https://github.com/github/dmca/blob/master/README.md#anatomy-of-a-takedown-notice).

---

**Are you the copyright holder or authorized to act on the copyright owner's behalf?**

Yes, I am the copyright holder.

**Are you submitting a revised DMCA notice after GitHub Trust & Safety requested you make changes to your original notice?**

No

**Does your claim involve content on GitHub or npm.js?**

GitHub

**Please describe the nature of your copyright ownership or authorization to act on the owner's behalf.**

I am the [private] of the Skytils project available on Github. (https://github.com/Skytils/SkytilsMod)

**Please provide a detailed description of the original copyrighted work that has allegedly been infringed. If possible, include a URL to where it is posted online.**

I have read and understand GitHub's Guide to Filing a DMCA Notice. I am filing this notice based on the best of my knowledge after conducting my own investigation. This investigation was conducted on [private].

I am the [private] for SkytilsMod, a Minecraft Forge mod that provides quality of life features for Hypixel Skyblock. Skytils is located on GitHub at the repository https://github.com/Skytils/SkytilsMod

SkyblockFeatures appears to be based off a copy of SkytilsMod, available on the 0.x branch of Skytils/SkytilsMod, and contains large amounts of code from SkytilsMod and violates our open-source license.

SkyblockFeatures also infringes on multiple other projects' licenses, however, I am not the copyright holder nor authorized to act as the copyright holder for those projects, so they will not be included in this complaint.

**What files should be taken down? Please provide URLs for each file, or if the entire repository, the repository’s URL.**

https://github.com/MrFast-js/SkyblockFeatures/

The entire repository and its forks must be taken down due to the amount of files that contain code from my project.

**Do you claim to have any technological measures in place to control access to your copyrighted content? Please see our <a href="https://docs.github.com/articles/guide-to-submitting-a-dmca-takedown-notice#complaints-about-anti-circumvention-technology">Complaints about Anti-Circumvention Technology</a> if you are unsure.**

No

**<a href="https://docs.github.com/articles/dmca-takedown-policy#b-what-about-forks-or-whats-a-fork">Have you searched for any forks</a> of the allegedly infringing files or repositories? Each fork is a distinct repository and must be identified separately if you believe it is infringing and wish to have it taken down.**

All forks must be taken down as they include my project's code.  
The only visible fork I see is [invalid], which does not include a license.

**Is the work licensed under an open source license?**

Yes

**Which license?**

Our current branch uses GNU Affero General Public License 3.0 with Exceptions

https://github.com/Skytils/SkytilsMod/blob/1.x/LICENSE.md

However, some code they have copied appears to be from our 0.x branch, which is also GNU Affero General Public License 3.0 available at  
https://raw.githubusercontent.com/Skytils/SkytilsMod/0.x/LICENSE

**How do you believe the license is being violated?**

The project License is incompatible with the GNU Affero General Public License 3.0, the project is licensed under the MIT License, while the fork listed appears not to include a license.
The author makes no attempt at following our license, bundling our code with other code from projects that may have incompatible licenses, or even All Rights Reserved code which does not belong to them.

**What changes can be made to bring the project into compliance with the license? For example, adding attribution, adding a license, making the repository private.**

The License must be compatible with the GNU AGPL 3.0, include license and copyright notice
State the changes made to our code
Remove any code that may not fulfill the terms of the GNU AGPL 3.0 license

**What would be the best solution for the alleged infringement?**

Reported content must be removed

**Do you have the alleged infringer’s contact information? If so, please provide it.**

No, I do not have the contact information.

**I have a good faith belief that use of the copyrighted materials described above on the infringing web pages is not authorized by the copyright owner, or its agent, or the law.**

**I have taken <a href="https://www.lumendatabase.org/topics/22">fair use</a> into consideration.**

**I swear, under penalty of perjury, that the information in this notification is accurate and that I am the copyright owner, or am authorized to act on behalf of the owner, of an exclusive right that is allegedly infringed.**

**I have read and understand GitHub's <a href="https://docs.github.com/articles/guide-to-submitting-a-dmca-takedown-notice/">Guide to Submitting a DMCA Takedown Notice</a>.**

**So that we can get back to you, please provide either your telephone number or physical address.**

[private]

Email is more preferable for contacting me, [private]

**Please type your full legal name below to sign this request.**

[private]

---
## [PrimedPixel/ProgrammingProject](https://github.com/PrimedPixel/ProgrammingProject)@[f1c000652f...](https://github.com/PrimedPixel/ProgrammingProject/commit/f1c000652f9532a1e6353325b34c888e1c894ea6)
#### Sunday 2023-07-16 15:00:12 by Malachy Moran-Tun

Saving now works in Godot 4

plus fixed an incredibly stupid error in the debug menu where "cast" was spelt "caset" like what the fuck is a caset mate what were you thinking you imbecile, you absolute cretin of the highest regard. what a fuckin' loser

---
## [greenhas/spg_website](https://github.com/greenhas/spg_website)@[9ff5ab99d6...](https://github.com/greenhas/spg_website/commit/9ff5ab99d6c76ef0d1568d180e4c937a22ba01f2)
#### Sunday 2023-07-16 15:56:11 by Spencer Greenhalgh

post Lots to love in this movie: The animation is gorgeous, the concept is interesting, the metaphors are well-meaning, and there are plenty of funny bits. There seemed to be too many subplots, though, and when any of them saw a shake-up, it didn't always feel deserved. It also feels essentialist in the way that D&D does—yes, differences make sense in the fictional world, but since we're meant to read them onto the real world, it doesn't always sit right. There are also bits that go unexplained or that don't hold up to much thinking. I get that it's a Pixar movie, but they still bugged me when I sat to think about it. I enjoyed it and would watch it again, but it seems like it was an excuse to do some cool animation and that the rest of the movie suffers from it.

---
## [walkersgaming/CivDocker](https://github.com/walkersgaming/CivDocker)@[7fdbe7c6d9...](https://github.com/walkersgaming/CivDocker/commit/7fdbe7c6d9d1e9ca8b73aec517daf0300588acdd)
#### Sunday 2023-07-16 16:26:09 by CaptainKlutz

Lengthen all reinforcement maturation times

Reinforcement times across the board are far too short.

It is completely nonsensical that structures built can rival the strength of buildings that have stood for months after just 5 minutes or an hour. It sucks the fun out of civ knowing you have mere seconds to log in and remove stone-reinforced grief before having to use acid blocks instead. It is completely counterproductive for those with lives outside of civ to always be an hour away from being totally invalidated. The stale vault meta is only bolstered by the fact that vault spikes are risk-free and diamond reinforced expansions can be erected overnight.

A lot of people are scared of big maturation numbers but forget they don't represent 'time until viable'. Just a few seconds after SRO is placed, it doubles in strength. The time it takes to mine it then allows it to mature further. Pardon my French, but it is absolutely FUCKED that you can be mining a block and the amount of breaks it will take to destroy it is INCREASING while you're ACTIVELY BREAKING IT.

"but my skybridging": what do you want to be more important, the skybridge or the people fighting in it?

"but my build might be broken overnight": just 15 minutes after you place a stone reinforced block, it will already take 16 hits to break. unless you're building in a warzone, you're going to be fine.

"but my acids will take longer": maybe now it will be actually viable to break blocks still maturing instead of giving up and going straight for acid.

"but my bunker pvp": I've seen bunker pvp on this iteration and it's fair to say I think the vast majority of people hate the stone reinforced obby/trapdoors/doors/buttons spam meta.

"but it will encourage camping to abuse when reinforcements are maturing": but this ALREADY HAPPENS, just the other way around. Players literally wait for people to be offline to spam reinforcements before they log on again. Turning this around to favour the breaker's side is more healthy.

"but now obbybombing is less viable": good.

---
## [SteelSlayer/Paradise](https://github.com/SteelSlayer/Paradise)@[a3dc32cf34...](https://github.com/SteelSlayer/Paradise/commit/a3dc32cf344dbd441e85f6cbb694b166dc1f5e4b)
#### Sunday 2023-07-16 16:47:22 by ATP-Engineer

Fixes issue where Turret Control sprites arent actually updated in previous PR (#21538)

* Removes actual turret file

FUCK

* Fixes turret controllers not actually being changed

GOD DAMNIT.

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[746b75844c...](https://github.com/tgstation/tgstation/commit/746b75844c0e05b521a2973cb0705fca304d287f)
#### Sunday 2023-07-16 17:17:04 by necromanceranne

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
## [newstools/2023-sundiata-post](https://github.com/newstools/2023-sundiata-post)@[fb31e78936...](https://github.com/newstools/2023-sundiata-post/commit/fb31e7893693ac9f1b096a2957ccd8d7b584918e)
#### Sunday 2023-07-16 17:46:55 by Billy Einkamerer

Created Text For URL [sundiatapost.com/ndlea-launches-investigation-into-stray-bullet-incident-that-claimed-the-life-of-2-year-old-boy-and-left-his-brother-with-an-eye-injury/]

---
## [tgstation/tgstation](https://github.com/tgstation/tgstation)@[9286933739...](https://github.com/tgstation/tgstation/commit/92869337395a34eb372d7af6b3afaee4be4a7bef)
#### Sunday 2023-07-16 17:50:05 by Jacquerel

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
## [tgstation/TerraGov-Marine-Corps](https://github.com/tgstation/TerraGov-Marine-Corps)@[ca4b66185f...](https://github.com/tgstation/TerraGov-Marine-Corps/commit/ca4b66185ffa363692529f8340a43cccab02cbf1)
#### Sunday 2023-07-16 18:18:44 by chizzy376

Gives the Umbilical Tad shutters on side windows. (#13490)

* y

* Update combat_patrol.dm

* Update combat_patrol.dm

Sometimes I think about if life is really worth the hassle, if I really have to deal with so much bs only to then have to believe hard enough to get into heaven. Am I a good person for heaven? Do I deserve it? fuck if i know

* Finish fixing my fuckup

---
## [Chatarra-Estudio/chatarra-estudio.github.io](https://github.com/Chatarra-Estudio/chatarra-estudio.github.io)@[7797c99c55...](https://github.com/Chatarra-Estudio/chatarra-estudio.github.io/commit/7797c99c55955e8609033e8c1744d9b16a320c48)
#### Sunday 2023-07-16 19:19:04 by JoseGarciaMoreno

Update index.html <!DOCTYPE html> <html>   <head>     <meta http-equiv="content-type" content="text/html; charset=UTF-8">     <title>Chatarra Estudio</title>     <style>	                 /* Estilos para el cuerpo? */       body {font-family: 'Chakra Petch', sans-serif;}       h1 {   			display: block;   			       font-size: 2em;       			font-weight: bold; } 	.contenedor { 	display: flex; 	flex-direction: column ; 	} 	.menu1{ 		display: flex; 		flex-direction: row; 		justify-content: space-around; 	} 	.portada{ 		display: flex; 		flex-direction: row; 		justify-content: space-evenly; 		margin-bottom: 20px;     margin-left: 20px;     margin-right: 20px; 		 	} 	.contenido{ 		display: flex; 		flex-direction: row; 		justify-content: space-evenly; 		margin-bottom: 20px; 		padding: 20px; 		background-color : #000000; 		color:#ffffff; 	} 	 	.container {   	flex-direction: row; 	 	}           /* Estilos para el primer menú */     #menu1 {       position: fixed;       top: 0;       right: 0;       background-color: black;       color: white;     }      /* Estilos para el segundo menú */     #menu2 {       position: fixed;       bottom: 0;       left: 0;       background-color: black;       color: white;     } </style> <link rel="preconnect" href="https://fonts.googleapis.com">     <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">     <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch&amp;display=swap"        rel="stylesheet">   </head>   <body>     <div id="menu1">       <!-- Contenido del primer menú --> <a href="https://chatarra-estudio.github.io/">Inicio         Chatarrero</a> <a href="https://chatarra-estudio.github.io/">Acerca de</a>       <a href="https://chatarra-estudio.github.io/">Contacto</a> </div>     <!-- Contenido del cuerpo -->     <div class="contenedor">       <div class="menu1"> <a href="https://chatarra-estudio.github.io/"><img src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/70e65eb1e93be1f5e078f44b9d079c851a806f45/imagen/chatarra348x97.png"              style="width: 348px; height: 97px;" id="logoheader"></a>         <h1 style="background-color: white;"> <span style="color: white;">Chatarra             Estudio</span></h1>         <!-- –– <img src="https://raw.githubusercontent.com/CycloPiStudio/CyloPi-Studio-Web/master/desarrollo20M71/imagen/juegos_bot.png" alt="boton pi juegos errorimagen" title="boton pi juegos" style="width: 178px; height: 83px;"-->         <!-- ––	<img src="https://raw.githubusercontent.com/CycloPiStudio/CyloPi-Studio-Web/master/desarrollo20M71/imagen/tutos_bot.png" alt="Boton tutos error" title="Boton tutos" style="width: 179px; height: 83px;"-->         <br>       </div>       <div class="portada"> <img src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/imagen/chatarra420x420.png"            style="width: 350px; height: 350px;">         <p> Bienvenidos a mi página de proyectos. Aquí encontrarán una variedad           de proyectos que he creado y en los que he trabajado. Desde           videojuegos hasta proyectos de electrónica, mantenimiento y reparación           de cacharros y coches, aquí podrás ver mi pasión por la tecnología y           la ingeniería. Soy un apasionado de los desafíos y siempre estoy           buscando nuevos proyectos y aventuras para emprender. Estoy emocionado           de compartir mis logros y mis experimentos con ustedes y espero que           disfruten explorando mi trabajo. Gracias por visitar mi página. <br>           <br>           <br>           <br>           Welcome to my projects page. Here you will find a variety of projects           that I have created and worked on. From video games to electronics,           maintenance and repair of gadgets and cars, here you will see my           passion for technology and engineering. I am a fan of challenges and           am always looking for new projects and adventures to undertake. I am           excited to share my achievements and experiments with you and hope you           enjoy exploring my work. Thank you for visiting my page<br>           <br>           Chatarra Estudio reciclando. Chatarra Estudio traducido al inglés es           Scrap Studio</p>         <p><br>         </p>         <p><br>         </p>         <p><br>         </p>         <p><br>         </p>         <p><br>         </p>         <p> </p>         <p><br>         </p>       </div>       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– Abre bloque imagen a izquierda de juejos: imagen + texto––-->       <div class="contenido">         <!-- –– imagen ––--> <a href="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/jam249th/mazcongadas_ii.html"            title="Mazcongadas II 2023" target="_blank"><img style="width: 350px"              ;="jjjj" src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/landing2023/jam249th/mazconT.jpg"              alt="Mazcongadas II 2023" title="Mazcongadas II 2023"></a>         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"> Game: Mazcongadas II<br>           One Hour Game Jam&nbsp; <a href="https://onehourgamejam.com/?page=jam&amp;jam=429"              title="Mazcongadas II" target="_blank">429th </a><br>           Theme: Dungeon Crawler<br>           July 15th 2023 &nbsp;<a href="https://cyclopistudio.github.io/CyloPi-Studio-Web/desarrollo20M71/landing/calamar/juegazocalamar0.html"              title="Robobo" target="_blank"> </a><br>           Play / Jugar: <a href="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/jam249th/mazcongadas_ii.html"              title="Mazcongadas II 2023" target="_blank">Mazcongadas II </a><br>           Systems / Sistemas: PC, Web¡<br>           Bienvenido a "Mazcongadas II" Prepárate para una emocionante aventura           llena de acción y habilidad con nuestro juego de cartas realizado en           un par de horas.</p>       </div>       <!-- –– cierro bloque izquierda de juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– abro bloque derecha de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"> Chatarra Estudio reciclando: <br>           Esta semana no hay juego. Solamente hemos editado un video sobre una           buena máquina.</p>         <!-- –– video  ––--><video src="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/J234/clio_chatarra.webm"            controls="controls" width="350"></video>&nbsp; </div>       <!-- –– cierro bloque derecha juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– Abre bloque izquierda de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– imagen ––--> <a href="https://cyclopistudio.github.io/Web-2021/desarrollo/indiaco/jones.html"            title="Indico Jones Game" target="_blank"><iframe src="https://www.youtube.com/embed/VBdzinsg3ns"              title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"              allowfullscreen="" height="315" frameborder="0" width="560"></iframe></a>         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––--><br>         <p style="width: 350px;"> "Pocas Luces" es un cautivador video de           animación que combina elementos visuales y narrativos para contar una           historia única. El proyecto fue concebido como una colaboración entre           los talentosos artistas y animadores de Cyclo Pi Studio, y ha sido           elogiado por su estilo visual distintivo y su narrativa evocadora.           Leer más en recoplatorio de <a href="https://chatarra-estudio.github.io/landing2023/cyclopi.html">Cyclo             π Studio</a></p>       </div>       <!-- –– cierro bloque izquierda de juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– abro bloque derecha de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"> Chatarra Estudio reciclando: <br>           En el año 2017, Cyclo Pi Studio y sus colaboradores se embarcaron en           una emocionante aventura de creatividad y desarrollo de videojuegos.           Fue un período lleno de descubrimientos, aprendizaje y experimentación           en el mundo de los juegos.<br>           Leer más en blog de <a href="https://chatarra-estudio.github.io/landing2023/cyclopi2017.html"              title="Cyclo Pi 2017">Cyclo π Studio 17&nbsp; <br>           </a></p>         <!-- –– imagen ––--> <a href="https://chatarra-estudio.github.io/landing2023/cyclopi2017.html"            title="Cyclo pi 2017" target="_blank"><img style="width: 350px" ;="" src="https://raw.githubusercontent.com/CycloPi/Studio2/master/crazyTronTrackVY2grande.png"              alt="Cyclo pi 2017" title="Cyclo pi 2017"></a> </div>       <!-- –– cierro bloque derecha juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– Abre bloque imagen a izquierda de juejos: imagen + texto––-->       <div class="contenido">         <!-- –– imagen ––--> <a href="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2016/cyclopi_2017.html"            title="Cyclo Pi 2017" target="_blank"><img style="width: 350px" ;="jjjj"              src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/landing2016/cyclo17pi.jpg"              alt="Cyclo Pi 2017" title="Cyclo Pi 2017"></a>         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;">Un trabajo chatarrero: <br>           Así, hacía las páginas en 2017. <br>           Leer más: <a href="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2016/cyclopi_2017.html">aquí             2017</a>.&nbsp;</p>       </div>       <!-- –– cierro bloque izquierda de juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– abro bloque derecha de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"> Chatarra Estudio reciclando: <br>           Cyclop pi debutó en a finales del 2015 con su micro corto Pocas Luces.           En 2016 comenzaron otro la producción de otro corto que se llamó: La           partida de la semana. Y todavía tenemos algunas imágenes.<br>           Leer más en blog de <a href="https://chatarra-estudio.github.io/landing2023/cyclopi.html">Cyclo             π Studio <br>           </a></p>         <!-- –– imagen ––--> <a href="https://chatarra-estudio.github.io/landing2023/cyclopi.html"            title="Partida" target="_blank"><img style="width: 350px" ;="" src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/landing2016/partida.png"              alt="Partida" title="Partida"></a> </div>       <!-- –– cierro bloque derecha juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– Abre bloque imagen a izquierda de juejos: imagen + texto––-->       <div class="contenido">         <!-- –– imagen ––--> <a href="https://chatarra-estudio.github.io/landing2023/robobo/jojoya.html"            title="Robobo 2023" target="_blank"><img style="width: 350px" ;="jjjj"              src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/landing2023/amort.jpg"              alt="Amortiguadores" title="Amortiguadores"></a>         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;">Un trabajo chatarrero <br>           ¿Quieres saber más sobre los amortiguadores de tu vehículo?<br>           En este trabajo hemos desarrollado un tema de mecánica muy           interesante. Leer más: <a href="https://chatarra-estudio.github.io/landing2023/amortiguador.html"              title="Amortiguadores en Chatarra Estudio" target="_blank">aquí, en             amortiguadores</a>.</p>       </div>       <!-- –– cierro bloque izquierda de juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– abro bloque imagen a derecha de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"><a href="https://chatarra-estudio.github.io/landing2023/chatarra_2021.html"              title="Proyectos juegos chatarra 2021" target="_blank">Recopilatorio             proyectos 2021</a>&nbsp; Página Web.<br>           Aquí encontrarás una recopilación de nuestos juegos&nbsp; y proyectos           del año 2021. Recuerda que además también podrás descargarte el           proyecto editable para modificar y desarrollar tu propios video           juegos.<br>           <br>           ¡Disfruta explorando!</p>         <!-- –– imagen ––--> <a href="https://chatarra-estudio.github.io/landing2023/chatarra_2021.html"            title="Recopila 2021 chatarra" target="_blank"><img style="width: 350px"              ;="" src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/landing2023/fpp.jpg"              alt="Recopila 2021" title="Recopila 2021"></a> </div>       <!-- –– cierro bloque derecha juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– Abre bloque imagen a izquierda de juejos: imagen + texto––-->       <div class="contenido">         <!-- –– imagen ––--> <a href="https://chatarra-estudio.github.io/landing2023/robobo/jojoya.html"            title="Robobo 2023" target="_blank"><img style="width: 350px" ;="jjjj"              src="https://onehourgamejam.com/data/jams/jam_422/cyclopi.jpg" alt="Robobo"              title="Robobo"></a>         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"> Game: Robobo<br>           One Hour Game Jam&nbsp; <a href="https://onehourgamejam.com/?page=jam&amp;jam=422"              title="Robobo 2023" target="_blank">422st </a><br>           Theme: Heist&nbsp;<a href="https://cyclopistudio.github.io/CyloPi-Studio-Web/desarrollo20M71/landing/calamar/juegazocalamar0.html"              title="Robobo" target="_blank"> </a><br>           May 27th 2023 <br>           Play / Jugar: <a href="https://chatarra-estudio.github.io/landing2023/robobo/jojoya.html"              title="Robobo 2023" target="_blank">Robobo </a><br>           Systems / Sistemas: PC, Web¡<br>           Bienvenido a "Robobo" Prepárate para una emocionante aventura llena de           acción y habilidad. <br>           "En las sombras de la ciudad, un ladrón hábil y audaz conocido como           'El Escurridizo' ha llevado a cabo su último robo&nbsp; ...&nbsp; <a              href="https://chatarra-estudio.github.io/landing2023/robobo/jojoya_page.html"              title="Landing page Robobo" target="_blank">Leer más</a></p>       </div>       <!-- –– cierro bloque izquierda de juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– abro bloque imagen a derecha de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"><a href="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/modelotexto_menu_2022.html"              title="Cámara" target="_blank">Recopilatorio proyectos 2022</a>&nbsp;           Página Web.<br>           Aquí encontrarás una recopilación de mis emocionantes proyectos del           año 2022. Explora cada proyecto y descubre mi pasión por la creación           digital.<br>           <br>           ¡Disfruta explorando!z </p>         <!-- –– imagen ––--> <a href="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/modelotexto_menu_2022.html"            title="Recopila 2022" target="_blank"><img style="width: 350px" ;="" src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/landing2023/2022reccopila.jpg"              alt="Recopila 2022" title="Recopila 2022" longdesc="Recopila 2022"></a>       </div>       <!-- –– cierro bloque derecha juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– Abre bloque imagen a izquierda de juejos: imagen + texto––-->       <div class="contenido">         <!-- –– imagen ––--> <a href="udio.github.io/landing2023/space/junk.html"            title="Space Junk 2023" target="_blank"><img style="width: 350px" ;="jjjj"              src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/landing2023/space_junk_23.jpg"></a>         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"> Game: Space Junk<br>           One Hour Game Jam&nbsp; <a href="https://onehourgamejam.com/?page=jam&amp;jam=421"              title="Space Junk 2023" target="_blank">421st </a><br>           Theme: Dark space&nbsp;<a href="https://cyclopistudio.github.io/CyloPi-Studio-Web/desarrollo20M71/landing/calamar/juegazocalamar0.html"              title="Indico Jones Game Jam 2021" target="_blank"> </a><br>           May 20th 2023 <br>           Play / Jugar: <a href="https://chatarra-estudio.github.io/landing2023/space/junk.html"              title="Space Junk 2023" target="_blank">Space Junk </a><br>           Systems / Sistemas: PC, Web¡<br>           Bienvenido a "Space Junk"! Prepárate para una emocionante aventura           espacial llena de acción y habilidad. En este juego de la game jam,           asume el control de una nave espacial ágil y deslízate por el vasto           cosmos. Tu objetivo es simple pero desafiante: esquivar hábilmente a           las naves enemigas que te acechan. </p>         <p style="width: 350px;"><br>           Con reflejos rápidos y destreza, deberás maniobrar tu nave a través de           un campo de asteroides y obstáculos espaciales mientras evitas a las           naves enemigas que intentan derribarte. ¡Cuanto más tiempo sobrevivas,           mayor será tu puntuación!<br>           <br>           Con gráficos vibrantes y una jugabilidad adictiva, "Space Junk" te           sumergirá en un frenético combate espacial. ¿Tienes lo que se necesita           para sobrevivir y alcanzar lo más alto de la tabla de clasificación?           ¡Ponte a prueba ahora y desata tu habilidad en este increíble juego de           supervivencia espacial!</p>       </div>       <!-- –– cierro bloque izquierda de juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– abro bloque derecha de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"><a href="https://chatarra-estudio.github.io/landing2023/23M13lote.html"              title="Cámara" target="_blank">Lote con cámara</a> mural y vitrina.<a              href="https://chatarra-estudio.github.io/landing2023/23M13lote.html"              title="Cámara" target="_blank"> </a><br>           <br>           Marca: DWM Copeland<br>           Modelo: DKSJP-10X-EWL<br>           Desplazamiento: 6,33 m3/h <br>           Tensión: 380-420V/3~/50Hz </p>         <!-- –– imagen ––--> <a href="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/lote23M13/23M13C_camara_positiva.html"            title="Lote cámara" target="_blank"><img style="width: 350px" ;="" src="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/lote23M13/compre1000x500.jpg"></a>       </div>       <!-- –– cierro bloque derecha juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– abro bloque derecha de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"><a href="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/lote23M13/23M13C_camara_positiva.html"              title="Cámara" target="_blank">Cámara</a> con antecámara positiva           para mantenimiento de carnes y vegetales.<a href="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/lote23M13/23M13C_camara_positiva.html"              title="Cámara" target="_blank"> </a><br>           <br>           Marca: DWM Copeland<br>           Modelo: DKSJP-10X-EWL<br>           Desplazamiento: 6,33 m3/h <br>           Tensión: 380-420V/3~/50Hz </p>         <!-- –– imagen ––--> <a href="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/lote23M13/23M13C_camara_positiva.html"            title="Lote cámara" target="_blank"><img style="width: 350px" ;="" src="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/lote23M13/compre05.jpg"></a>       </div>       <!-- –– cierro bloque derecha juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– abro bloque derecha de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"><a href="https://chatarra-estudio.github.io/landing2023/23M1M_mural_dorin.html"              title="Mural" target="_blank">Mural&nbsp;</a> mueble expositor de           productos refrigerados con batería evaporador.<br>           <br>           Marca: DORIN<br>           Modelo: K 180CC<br>           Desplazamiento: 7,71&nbsp; m3/h<br>           Tensión: 380-420V/3~/50Hz</p>         <!-- –– imagen ––--> <a href="https://chatarra-estudio.github.io/landing2023/23M1M_mural_dorin.html"            title="Lote mural" target="_blank"><img style="width: 350px" ;="" src="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/lote23M13M/compre13.jpg"></a>       </div>       <!-- –– cierro bloque derecha juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– abro bloque derecha de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"><a href="https://chatarra-estudio.github.io/landing2023/23M13V_vitrina.html"              title="Mural" target="_blank">Vitrina&nbsp;</a> mueble de exposición           de productos refrigerados (carnes y embutidos) con iluminación,           armarios refrigerados y tomas de corrientes.<br>           <br>           Marca: DWM Copeland<br>           Modelo: DJC-75-EWL<br>           Desplazamiento: 5,14 m3/h<br>           Tensión: 380-420V/3~/50Hzz</p>         <!-- –– imagen ––--> <a href="https://chatarra-estudio.github.io/landing2023/23M13V_vitrina.html"            title="Lote vitrina" target="_blank"><img style="width: 350px" ;="" src="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/lote23M13/compre17.jpg"></a>       </div>       <!-- –– cierro bloque derecha juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– espacio sin espacio––-->       <!-- –– abro bloque derecha de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;">&nbsp;Hierba Racing<br>           One Hour Game Jam <a href="https://onehourgamejam.com/?page=jam&amp;jam=415"              title="OHGJ 415th" target="_blank">415th </a><br>           April 8th 2023, Theme: touch grass <br>           Play / Jugar: <a href="https://cyclopistudio.github.io/CyloPi-Studio-Web/testing_2023/racing/hierba.html"              title="Hierba Racing" target="_blank">Hierba Racing </a><br>           Systems / Sistemas: PC, Web <br>           ¿Estás listo para poner a prueba tus habilidades de conducción y           recolección? Conduce a toda velocidad y recolecta todos los arbustos           que puedas mientras evitas obstáculos.<br>           ¡Conduce a toda velocidad y recolecta arbustos en este emocionante           juego de carreras! Con un vehículo en forma de conejo y controles           intuitivos, este juego es fácil de aprender pero difícil de dominar.           ¡Juega ahora y comienza la carrera de conejos más emocionante de tu           vida! </p>         <!-- –– imagen ––--> <a href="https://cyclopistudio.github.io/CyloPi-Studio-Web/testing_2023/tamariz-II/game.html"            title="Tamariz II 2023" target="_blank"><img style="width: 350px" ;=""              src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/imagen/hierba_racing_2.png"></a>       </div>       <!-- –– cierro bloque derecha juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <!-- –– Abre bloque imagen izquierda de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– video ––--> <a href="https://realidadesparalelas.com/" title="realidadesparalelas.com"            target="_blank"><img style="width: 350px" src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/imagen/realidades350x350.png"></a>         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"> Web molona:<br>           Play / Jugar: <a href="https://realidadesparalelas.com/" title="realidades paralelas"              target="_blank">Realiades Paralelas </a><br>           Systems / Sistemas: PC, Web, Android <br>           Description: <br>           Si eres un apasionado de la ciencia ficción, la fantasía, los           videojuegos, la innovación, la tecnología, la literatura y la           creatividad, debes conocer una página web amiga que trata sobre todos           estos temas y más.<br>         </p>       </div>       <!-- –– cierro bloque izquierda de juejos: texto + imagen ––-->       <!-- –– Abre bloque solo texto ––--><br>       <div class="contenido">         <p> Esta web se llama "realidadesparalelas.com" y es un sitio web           especializado en todo lo relacionado con la ciencia ficción, la           fantasía, los videojuegos, la innovación, la tecnología, la literatura           y la creatividad. Su objetivo principal es ofrecer información           actualizada, noticias interesantes, reseñas de libros, videojuegos y           películas, así como también entrevistas con expertos en estos temas.<br>           En esta página web encontrarás contenido variado y muy interesante.           Por ejemplo, podrás encontrar artículos sobre los últimos avances           tecnológicos y científicos, así como también reseñas de los últimos           videojuegos, películas y libros de ciencia ficción y fantasía. Además,           también encontrarás información sobre eventos y convenciones           relacionados con estos temas. <br>           Una de las secciones más destacadas de la página es la dedicada a la           creatividad. Aquí encontrarás consejos útiles sobre cómo escribir tu           propia novela de ciencia ficción o fantasía, cómo crear tus propios           personajes o incluso cómo diseñar tus propios videojuegos. Esta           sección es perfecta para aquellos que buscan inspiración y quieren           aprender más sobre el proceso creativo. <br>           Además, <a href="https://realidadesparalelas.com/" title="realidades paralelas"              target="_blank">Realiades Paralelas </a> también cuenta con una           sección de entrevistas en la que expertos en ciencia ficción,           tecnología y otros temas relacionados comparten sus opiniones y           conocimientos. Estas entrevistas son muy interesantes y ofrecen una           visión única sobre estos temas. <br>           En resumen, "Futurosinlimites.com" es una página web amiga que ofrece           contenido variado, interesante y útil para aquellos apasionados de la           ciencia ficción, la fantasía, los videojuegos, la innovación, la           tecnología, la literatura y la creatividad. Si aún no la has visitado,           te recomendamos hacerlo y explorar todo lo que tiene que ofrecer.           ¡Seguramente encontrarás contenido que te apasionará! <br>         </p>         <p><br>         </p>       </div>       <!-- –– cierro bloque solo texto ––-->       <!-- –– Abre bloque imagen izquierda de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– imagen ––--> <a href="https://josegar.itch.io/tamariz" title="Tamariz for Jam"            target="_blank"><img style="width: 350px" ;="" src="https://img.itch.zone/aW1nLzEwNDY1NjUyLnBuZw==/300x240%23c/zzZdzM.png"></a>         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"> Juego de regalo<br>           Tamariz<br>           Friday Night Game Jam #2022-45: <a href="https://itch.io/jam/friday-night-game-jam-2022-45"              title="Juegazo Tamariz" target="_blank">November 3rd 2022</a><br>           Play / Jugar: <a href="https://josegar.itch.io/tamariz" title="Indico Jones Game Jam 2021"              target="_blank">Tamariz </a><br>           Systems / Sistemas: PC, Web, Android </p>       </div>       <!-- –– cierro bloque izquierda de juejos: texto + imagen ––-->       <!-- –– abro bloque derecha de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"> Chatarra Estudio reciclando <br>           Juego de regalo<br>           History of fire <br>           Game Jam: Murcia Game Jam (October 29th 2022)<br>           Play / Jugar: <a href="https://josegar.itch.io/history-of-fire" title="History of fire Game Jam 2022"              target="_blank">History of fire </a><br>           Systems / Sistemas: PC, Web </p>         <!-- –– imagen ––--> <a href="https://josegar.itch.io/history-of-fire"            title="https://josegar.itch.io/history-of-fire" target="_blank"><img style="width: 350px"              ;="" src="https://img.itch.zone/aW1nLzEwNDAxODMwLnBuZw==/315x250%23c/jvYd3h.png"></a>       </div>       <!-- –– cierro bloque derecha juejos: texto + imagen ––-->       <!-- –– abro bloque imagen a derecha de juejos: texto + imagen ––-->       <div class="contenido">         <!-- –– texto ––-->         <!-- –– texto <p style = "white-space : pre"; ––-->         <p style="width: 350px;"> Chatarra Estudio reciclando <br>           Video de regalo<br>           Video de entradilla<br>         </p>         <!-- –– video  ––--><video src="https://josegarciamoreno.github.io/template_hmtl/landing2022/entradilla.webm"            controls="controls" width="350"></video>&nbsp; </div>       <!-- –– cierro bloque derecha juejos: texto + imagen ––-->       <!-- –– espacio sin espacio––-->       <footer>         <!-- –– bloque de juejos: texto + imagen ––-->         <div class="contenido">           <p> Chatarra Estudio by: </p>           <a href="https://github.com/Chatarra-Estudio" title="Chatarra Estudio by GitHub"              target="_blank"><img style="height: 50px" ;="" src="https://raw.githubusercontent.com/CycloPiStudio/CyloPi-Studio-Web/master/desarrollo20M71/imagen/GitHub-Mark-Light-32px.png">           </a> </div>         <!-- –– cierro bloque de juejos: texto + imagen ––-->         <!-- –– bloque de juejos: texto + imagen ––-->         <div class="contenido">           <p> Ciclo Pi Studio by </p>           <!-- git --> <a href="https://github.com/CycloPiStudio" title="Cyclo Pi by GitHub"              target="_blank"><img style="height: 50px" ;="" src="https://raw.githubusercontent.com/CycloPiStudio/CyloPi-Studio-Web/master/desarrollo20M71/imagen/GitHub-Mark-Light-32px.png">           </a>           <!-- ichio --> <a href="https://itch.io/profile/cyclopi" title="Cyclo Pi by itch.io"              target="_blank"><img style="height: 50px" src="https://static.itch.io/images/logo-white-new.svg"></a>           <!-- 1 hora--> <a href="https://onehourgamejam.com/?page=author&amp;author=cyclopi"              title="Cyclo Pi by One hour game jam" target="_blank"><img style="height: 50px"                src="https://onehourgamejam.com/template/images/logos/logo_onehourgamejam.png"></a>         </div>         <!-- –– cierro bloque de juejos: texto + imagen ––-->         <!-- –– bloque parener texto + imagen ––-->         <div class="contenido">           <p>&nbsp;Parner &nbsp;&nbsp; </p>           <!-- cyclopi --> <a href="https://cyclopistudio.github.io/" title="Cyclo Pi"              target="_blank"><img style="height: 50px" ;="" src="https://avatars.githubusercontent.com/u/45769014?s=200&amp;v=4">           </a>           <!-- juan --> <a href="https://sites.google.com/site/blender3dgear/"              title="Juan" target="_blank"><img style="height: 50px" src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/imagen/25645174c.png"                alt="Juan" title="Juan"></a>           <!-- green --> <a href="https://greenfactory-es.github.io/" title="greenfactory-es"              target="_blank"><img style="height: 50px" src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/landing2023/logo_green_factory_23-Model222-23peq-logo23.png"                alt="green factory" title="Green Factory"></a>           <!-- chatarra --> <a href="https://chatarra-estudio.github.io/" title="Chatarra Estudio"              target="_blank"><img style="height: 50px" src="https://raw.githubusercontent.com/JoseGarciaMoreno/Chatarra-Estudio/main/imagen/chatarra150.png"></a>           <!-- jose --> <a href="https://josegarciamoreno.github.io/template_hmtl/index.html"              title="Jose" target="_blank"><img style="height: 50px" src="https://josegarciamoreno.github.io/template_hmtl/images/lobo01_276x276_blanco.png"></a>         </div>         <!-- –– cierro bloque de juejos: texto + imagen ––--> </footer>     </div>     <!-- Contenido del se menú -->     <div id="menu2">       <!-- Contenido del segundo menú --> <a href="https://josegarciamoreno.github.io/Chatarra-Estudio/landing2023/modelotexto_menu_2022.html">         2022</a> <a href="https://chatarra-estudio.github.io/landing2023/chatarra_2021.html">         2021</a> <a href="https://chatarra-estudio.github.io/landing2023/cycl

---
## [sqnztb/Skyrat-tg](https://github.com/sqnztb/Skyrat-tg)@[9701b40ca0...](https://github.com/sqnztb/Skyrat-tg/commit/9701b40ca03e164bd8bd4238fafb6cf778c52efe)
#### Sunday 2023-07-16 19:25:48 by SkyratBot

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
## [sqnztb/Skyrat-tg](https://github.com/sqnztb/Skyrat-tg)@[2303c452c7...](https://github.com/sqnztb/Skyrat-tg/commit/2303c452c79a8563076a58ad7e9d9346186a7e7c)
#### Sunday 2023-07-16 19:25:48 by SkyratBot

[MIRROR] Rat RP expansion [MDB IGNORE] (#22204)

* Rat RP expansion (#76455)

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

* Rat RP expansion

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [ShamanSliph/Bubberstation](https://github.com/ShamanSliph/Bubberstation)@[c4b550c1a9...](https://github.com/ShamanSliph/Bubberstation/commit/c4b550c1a94670ae333df12b8200ff33f7f7f175)
#### Sunday 2023-07-16 20:17:25 by SkyratBot

[MIRROR] New Wizard spell "branch": Vendormancy [MDB IGNORE] (#22008)

* New Wizard spell "branch": Vendormancy (#75679)

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

Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

* New Wizard spell "branch": Vendormancy

---------

Co-authored-by: GuillaumePrata <55374212+GuillaumePrata@users.noreply.github.com>
Co-authored-by: Time-Green <7501474+Time-Green@ users.noreply.github.com>

---
## [ServiceTeam565/ServiceTeam](https://github.com/ServiceTeam565/ServiceTeam)@[a15e711d7e...](https://github.com/ServiceTeam565/ServiceTeam/commit/a15e711d7edcd88180cc0e743b79b20dc7bce163)
#### Sunday 2023-07-16 20:26:59 by ServiceTeam565

Update README.md

This is for tutorial Purpose. changing university school/college grades is not a game, it requires professional hacking skills and abilities hack website, above above all a sophisticated server to block all security loopholes, gaining unlimited backdoor access and ceiling unforeseen security alarms and IP traces.

Hackers are breaking boundaries and connecting the world within a short distance. Exploiting school grades is a common thing. Changing your grades takes skills and techniques and unique software to accomplish your goals. What is common in changing school grades? the goal is to get good grades. What you score is not final? Despite how hard Universities and colleges attempt to safeguard their grading systems the truth is: the grades are actually more accessible to hackers now than ever!      
 ( serviceteam565@gmail.com )
 provides the best grade change service for university and college students as well as professionals.
The age of the traditional pad and pencil grading book is over, and the age of recording grades on the web is here.

Hire a Professional Hacker Now! | Hack and spy android cell phones and tablets/Hire a hacker — How to Hack a Snapchat Account? | Get the Ultimate WhatsApp Spying Solution!!!

You should put your mind at rest when you need a good ethical hacker to recover the account and also if you want to hack a social media account to make you gain access to the account to get as much information you want ,you can contact the serviceteam565@gmail.com on gmail hacker he does all hacking and tracking jobs including social media and phone hacking (WhatsApp Snapchat Instagram Facebook email gmail yahoo mail and lot more) at a friendly price.

---
## [MTandi/tgstation](https://github.com/MTandi/tgstation)@[d85e44c69c...](https://github.com/MTandi/tgstation/commit/d85e44c69cc06dbeeb3a0de7f76273de45ee3893)
#### Sunday 2023-07-16 20:30:39 by ChungusGamer666

SPECIES NUKING 2023: Head flags 3 & Knuckles: Fixes some growing pains with head flags  (#76440)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76422
This was caused by me somehow not using the wrapper there and not
noticing it

Also fixes hair gradients and facial hair gradients. I am pretty sure
they were uhh, being hidden behind the actual hair/facial hair. Oops.

Also also fixes spawning yourself as a human as admin and getting random
hair colors. That was just a failure to update the icon after updating
everything, I think?

Additionally, to totally babyproof all of this, ensures that head_flags
involved stuff gets applied AFTER species by creating a new preference
priority, and uses two separate wrappers to apply gradient style and
color.

Here's this absolute hellspawn to prove that everything works.

![image](https://github.com/tgstation/tgstation/assets/82850673/7ed29a68-cb60-4b28-996c-3be0e7331be8)

![image](https://github.com/tgstation/tgstation/assets/82850673/e57128be-0d7c-46ad-90dd-ee25981d0fea)

![image](https://github.com/tgstation/tgstation/assets/82850673/5c3619a8-fe6f-42b3-9fdc-12277d568e8d)

![image](https://github.com/tgstation/tgstation/assets/82850673/fdd13000-2220-47ad-8e02-44bc75a4a907)

Sorry for being so damn good at breaking this codebase.

## Why It's Good For The Game

Bugs are bad they make you mad

## Changelog

:cl:
fix: Hair and facial hair gradients work again now
fix: Facial hair colors apply properly again
fix: Admin spawned characters will get hair color preferences applied
properly
/:cl:

---
## [yuzu-emu/yuzu](https://github.com/yuzu-emu/yuzu)@[8e703e08df...](https://github.com/yuzu-emu/yuzu/commit/8e703e08dfcf735a08df2ceff6a05221b7cc981f)
#### Sunday 2023-07-16 20:56:49 by comex

Implement SSL service

This implements some missing network APIs including a large chunk of the SSL
service, enough for Mario Maker (with an appropriate mod applied) to connect to
the fan server [Open Course World](https://opencourse.world/).

Connecting to first-party servers is out of scope of this PR and is a
minefield I'd rather not step into.

 ## TLS

TLS is implemented with multiple backends depending on the system's 'native'
TLS library.  Currently there are two backends: Schannel for Windows, and
OpenSSL for Linux.  (In reality Linux is a bit of a free-for-all where there's
no one 'native' library, but OpenSSL is the closest it gets.)  On macOS the
'native' library is SecureTransport but that isn't implemented in this PR.
(Instead, all non-Windows OSes will use OpenSSL unless disabled with
`-DENABLE_OPENSSL=OFF`.)

Why have multiple backends instead of just using a single library, especially
given that Yuzu already embeds mbedtls for cryptographic algorithms?  Well, I
tried implementing this on mbedtls first, but the problem is TLS policies -
mainly trusted certificate policies, and to a lesser extent trusted algorithms,
SSL versions, etc.

...In practice, the chance that someone is going to conduct a man-in-the-middle
attack on a third-party game server is pretty low, but I'm a security nerd so I
like to do the right security things.

My base assumption is that we want to use the host system's TLS policies.  An
alternative would be to more closely emulate the Switch's TLS implementation
(which is based on NSS).  But for one thing, I don't feel like reverse
engineering it.  And I'd argue that for third-party servers such as Open Course
World, it's theoretically preferable to use the system's policies rather than
the Switch's, for two reasons

1. Someday the Switch will stop being updated, and the trusted cert list,
   algorithms, etc. will start to go stale, but users will still want to
   connect to third-party servers, and there's no reason they shouldn't have
   up-to-date security when doing so.  At that point, homebrew users on actual
   hardware may patch the TLS implementation, but for emulators it's simpler to
   just use the host's stack.

2. Also, it's good to respect any custom certificate policies the user may have
   added systemwide.  For example, they may have added custom trusted CAs in
   order to use TLS debugging tools or pass through corporate MitM middleboxes.
   Or they may have removed some CAs that are normally trusted out of paranoia.

Note that this policy wouldn't work as-is for connecting to first-party
servers, because some of them serve certificates based on Nintendo's own CA
rather than a publicly trusted one.  However, this could probably be solved
easily by using appropriate APIs to adding Nintendo's CA as an alternate
trusted cert for Yuzu's connections.  That is not implemented in this PR
because, again, first-party servers are out of scope.

(If anything I'd rather have an option to _block_ connections to Nintendo
servers, but that's not implemented here.)

To use the host's TLS policies, there are three theoretical options:

a) Import the host's trusted certificate list into a cross-platform TLS
   library (presumably mbedtls).

b) Use the native TLS library to verify certificates but use a cross-platform
   TLS library for everything else.

c) Use the native TLS library for everything.

Two problems with option a).  First, importing the trusted certificate list at
minimum requires a bunch of platform-specific code, which mbedtls does not have
built in.  Interestingly, OpenSSL recently gained the ability to import the
Windows certificate trust store... but that leads to the second problem, which
is that a list of trusted certificates is [not expressive
enough](https://bugs.archlinux.org/task/41909) to express a modern certificate
trust policy.  For example, Windows has the concept of [explicitly distrusted
certificates](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn265983(v=ws.11)),
and macOS requires Certificate Transparency validation for some certificates
with complex rules for when it's required.

Option b) (using native library just to verify certs) is probably feasible, but
it would miss aspects of TLS policy other than trusted certs (like allowed
algorithms), and in any case it might well require writing more code, not less,
compared to using the native library for everything.

So I ended up at option c), using the native library for everything.

What I'd *really* prefer would be to use a third-party library that does option
c) for me.  Rust has a good library for this,
[native-tls](https://docs.rs/native-tls/latest/native_tls/).  I did search, but
I couldn't find a good option in the C or C++ ecosystem, at least not any that
wasn't part of some much larger framework.  I was surprised - isn't this a
pretty common use case?  Well, many applications only need TLS for HTTPS, and they can
use libcurl, which has a TLS abstraction layer internally but doesn't expose
it.  Other applications only support a single TLS library, or use one of the
aforementioned larger frameworks, or are platform-specific to begin with, or of
course are written in a non-C/C++ language, most of which have some canonical
choice for TLS.  But there are also many applications that have a set of TLS
backends just like this; it's just that nobody has gone ahead and abstracted
the pattern into a library, at least not a widespread one.

Amusingly, there is one TLS abstraction layer that Yuzu already bundles: the
one in ffmpeg.  But it is missing some features that would be needed to use it
here (like reusing an existing socket rather than managing the socket itself).
Though, that does mean that the wiki's build instructions for Linux (and macOS
for some reason?) already recommend installing OpenSSL, so no need to update
those.

 ## Other APIs implemented

- Sockets:
    - GetSockOpt(`SO_ERROR`)
    - SetSockOpt(`SO_NOSIGPIPE`) (stub, I have no idea what this does on Switch)
    - `DuplicateSocket` (because the SSL sysmodule calls it internally)
    - More `PollEvents` values

- NSD:
    - `Resolve` and `ResolveEx` (stub, good enough for Open Course World and
      probably most third-party servers, but not first-party)

- SFDNSRES:
    - `GetHostByNameRequest` and `GetHostByNameRequestWithOptions`
    - `ResolverSetOptionRequest` (stub)

 ## Fixes

- Parts of the socket code were previously allocating a `sockaddr` object on
  the stack when calling functions that take a `sockaddr*` (e.g. `accept`).
  This might seem like the right thing to do to avoid illegal aliasing, but in
  fact `sockaddr` is not guaranteed to be large enough to hold any particular
  type of address, only the header.  This worked in practice because in
  practice `sockaddr` is the same size as `sockaddr_in`, but it's not how the
  API is meant to be used.  I changed this to allocate an `sockaddr_in` on the
  stack and `reinterpret_cast` it.  I could try to do something cleverer with
  `aligned_storage`, but casting is the idiomatic way to use these particular
  APIs, so it's really the system's responsibility to avoid any aliasing
  issues.

- I rewrote most of the `GetAddrInfoRequest[WithOptions]` implementation.  The
  old implementation invoked the host's getaddrinfo directly from sfdnsres.cpp,
  and directly passed through the host's socket type, protocol, etc. values
  rather than looking up the corresponding constants on the Switch.  To be
  fair, these constants don't tend to actually vary across systems, but
  still... I added a wrapper for `getaddrinfo` in
  `internal_network/network.cpp` similar to the ones for other socket APIs, and
  changed the `GetAddrInfoRequest` implementation to use it.  While I was at
  it, I rewrote the serialization to use the same approach I used to implement
  `GetHostByNameRequest`, because it reduces the number of size calculations.
  While doing so I removed `AF_INET6` support because the Switch doesn't
  support IPv6; it might be nice to support IPv6 anyway, but that would have to
  apply to all of the socket APIs.

  I also corrected the IPC wrappers for `GetAddrInfoRequest` and
  `GetAddrInfoRequestWithOptions` based on reverse engineering and hardware
  testing.  Every call to `GetAddrInfoRequestWithOptions` returns *four*
  different error codes (IPC status, getaddrinfo error code, netdb error code,
  and errno), and `GetAddrInfoRequest` returns three of those but in a
  different order, and it doesn't really matter but the existing implementation
  was a bit off, as I discovered while testing `GetHostByNameRequest`.

  - The new serialization code is based on two simple helper functions:

    ```cpp
    template <typename T> static void Append(std::vector<u8>& vec, T t);
    void AppendNulTerminated(std::vector<u8>& vec, std::string_view str);
    ```

    I was thinking there must be existing functions somewhere that assist with
    serialization/deserialization of binary data, but all I could find was the
    helper methods in `IOFile` and `HLERequestContext`, not anything that could
    be used with a generic byte buffer.  If I'm not missing something, then
    maybe I should move the above functions to a new header in `common`...
    right now they're just sitting in `sfdnsres.cpp` where they're used.

- Not a fix, but `SocketBase::Recv`/`Send` is changed to use `std::span<u8>`
  rather than `std::vector<u8>&` to avoid needing to copy the data to/from a
  vector when those methods are called from the TLS implementation.

---
## [Buildstarted/linksfordevs](https://github.com/Buildstarted/linksfordevs)@[bd450dd172...](https://github.com/Buildstarted/linksfordevs/commit/bd450dd172a1c9e13157564c086a3b358606c7dc)
#### Sunday 2023-07-16 21:11:18 by Ben Dornis

Updating: 7/16/2023 9:00:00 PM

 1. Added: Re: Ansible
    (https://www.eneigualauno.com/rant/2023/07/15/re-ansible.html)
 2. Added: How to register a Kei truck in Pennsylvania
    (https://danwilkerson.com/posts/2023-05-30-how-to-register-a-kei-truck-in-pa)
 3. Added: Dev Therapy part II: Recoveries · Melatonin
    (https://melatonin.dev/blog/dev-therapy-part-ii-recoveries/)
 4. Added: So You Want to Hire for Developer Tooling | Hazel Weakly
    (https://hazelweakly.me/blog/so-you-want-to-hire-for-developer-tooling/)
 5. Added: Jeremy Mikkola - What makes developers productive?
    (https://jeremymikkola.com/posts/developer_productivity.html)
 6. Added: The Private Equity Model in Medicine is Flawed | Ben White
    (https://www.benwhite.com/medicine/the-private-equity-model-in-medicine-is-flawed/)
 7. Added: Entity framework features I wish I knew earlier
    (https://timdeschryver.dev/blog/entity-framework-features-i-wish-i-knew-earlier#hasqueryfilter?utm_source=hnblogs.substack.com)
 8. Added: No local GPU? No Problem! Running Andrej Karpathy’s NanoGPT on Modal.com – Martin Capodici
    (https://martincapodici.com/2023/07/15/no-local-gpu-no-problem-running-andrej-karpathys-nanogpt-on-modal-com/)
 9. Added: Fun with DNS TXT Records
    (https://thoughts.theden.sh/posts/dns-txt-record-fun/)
10. Added: Why do we minimize the mean squared error?
    (https://www.alexmolas.com/2022/05/25/mean-squared-error.html)
11. Added: Lemmy frontend alternatives are popping off
    (https://blog.erlend.sh/lemmy-frontend-alternatives-are-popping-off)
12. Added: Beyond the Marketing: Assessing Anti-Bot Platforms through a Hacker's Lens
    (https://blog.umasi.dev/antibots-1)
13. Added: An Alternative Approach to Deep Tech VC
    (https://www.freaktakes.com/p/an-alternative-approach-to-deep-tech)
14. Added: Score-Based Diffusion Models
    (https://fanpu.io/blog/2023/score-based-diffusion-models/)
15. Added: Bypassing Internet Censorship Using SSH
    (https://znano.eu.org/blog/posts/bypassing-internet-censorship-using-ssh)
16. Added: wuko.ai: Evolve your mailbox into an intelligent read-it-later hub
    (https://katat.me/blog/wuko/intro-email-gpt)
17. Added: How I Wrote a Book Last Night
    (https://www.pulent.com/posts/how-i-wrote-a-book-last-night-unleashing-the-power-of-ai/)
18. Added: Building Intelligent Applications with OpenAI and C#: A Step-by-Step Guide to Get Started
    (https://neelbhatt.com/2023/07/16/building-intelligent-applications-with-openai-and-c-a-step-by-step-guide-to-get-started/)

Generation took: 00:11:06.3046751
 Maintenance update - cleaning up homepage and feed

---
## [btcjon/WebAI](https://github.com/btcjon/WebAI)@[5b5a0e6b2c...](https://github.com/btcjon/WebAI/commit/5b5a0e6b2c1f19cf7a3b4eed63318a2bd221969d)
#### Sunday 2023-07-16 21:18:21 by Jon Bennett

aider: Add timestamp field to store_message function and modify ensure_table_exists function to create table with correct schema if it doesn't exist.

# Aider chat conversation:

USER: help fix ModuleNotFoundError: No module named 'postgrest_py'

ASSISTANT: The error message "ModuleNotFoundError: No module named 'postgrest_py'" means that Python cannot find the 'postgrest_py' module in your current environment.

To fix this, you need to install the 'postgrest_py' module. You can do this using pip, which is a package manager for Python. Open your terminal and type the following command:

```bash
pip install postgrest-py
```

If you're using a specific Python environment or if you have multiple Python versions, make sure to use the correct pip version that corresponds to the Python interpreter you're using for your project. For example, if you're using Python 3, you might need to use pip3 instead:

```bash
pip3 install postgrest-py
```

After running this command, Python should be able to import the 'postgrest_py' module without any issues. If you're still having trouble, make sure that you're running the Python interpreter in the correct environment where 'postgrest_py' is installed.

USER: implement the following "Long-Term Memory (Supabase Database): This will be a Supabase database that stores past conversations. Each record in the database will include a user ID, session ID, timestamp, user message, and AI response. This allows the retrieval of past interactions for a user or a particular session, which is useful for maintaining context across multiple sessions and providing a personalized user experience. The user can access historical data using the user_id and session_id. We will have functions to store and retrieve data from this database."

ASSISTANT: To implement this, we need to modify the `memory_manager.py` file. We need to add a timestamp field to the `store_message` function and modify the `ensure_table_exists` function to create the table with the correct schema if it doesn't exist.

Here are the changes:

```python
memory_manager.py
<<<<<<< ORIGINAL
def ensure_table_exists():
    result = supabase.rpc('create_conversations_table')
    if result.error:
        print(f"Error when creating table: {result.error}")
    else:
        print("Table 'conversations' created successfully.")

def store_message(user_id, session_id, message, response):
    ensure_table_exists()
    result = supabase.table('conversations').insert({
        'user_id': user_id,
        'session_id': session_id,
        'message': message,
        'response': response
    }).execute()
    if result.error:
        print(f"Error when storing message: {result.error}")
    else:
        print(f"Message stored successfully for user {user_id} in session {session_id}.")
=======
from datetime import datetime

def ensure_table_exists():
    # Check if table exists
    result = supabase.table('conversations').select('id').limit(1).execute()
    if result.error:
        # If table doesn't exist, create it
        result = supabase.rpc('create_conversations_table')
        if result.error:
            print(f"Error when creating table: {result.error}")
        else:
            print("Table 'conversations' created successfully.")

def store_message(user_id, session_id, message, response):
    ensure_table_exists()
    timestamp = datetime.now().isoformat()
    result = supabase.table('conversations').insert({
        'user_id': user_id,
        'session_id': session_id,
        'timestamp': timestamp,
        'message': message,
        'response': response
    }).execute()
    if result.error:
        print(f"Error when storing message: {result.error}")
    else:
        print(f"Message stored successfully for user {user_id} in session {session_id} at {timestamp}.")
>>>>>>> UPDATED
```

Please note that the `create_conversations_table` RPC function needs to be defined on your Supabase backend to create the table with the correct schema. If you need help with that, please let me know.

---
## [TaleStation/TaleStation](https://github.com/TaleStation/TaleStation)@[46cd4d2063...](https://github.com/TaleStation/TaleStation/commit/46cd4d2063272ac273512f2d08c4aeea0ce8d920)
#### Sunday 2023-07-16 22:31:04 by TaleStationBot

[MIRROR] [MDB IGNORE] Fixes some ha ha funny issues with the preferences spritesheet (#6806)

Original PR: https://github.com/tgstation/tgstation/pull/76862
-----

## About The Pull Request

We had some icon cleanup recently, it removed what I think was a
redundant cow sprite in animals.dmi.
The trouble is hologram code referenced that icon+state as the cow
hologram in an obscure untested list.

So when preferences went to load it and failed it defaulted to the first
sprite in the folder, the chicken.

For some strange reason it dumped all 4 directionals, which, because the
css file can't mindread, caused our preference css stuff to "mis index"
the actual png asset.


![image](https://github.com/tgstation/tgstation/assets/58055496/c7ea1c23-28b7-44ab-bcdf-1eb5a0ea900b)

This meant all icons "below" ais in the sheet were offset. So you'd get
the xeno ai form in the backpack slot, glasses in your hair, etc.

This pr resolves the cow thing. 
We however need a better way of preventing this class of error in future
(Devs should not need to dig in the cache folder to figure out why they
broke backpack preferences)
I think preventing whatever that "all 4 icons" thing was + maybe
screenshot testing assets would help? unsure.

## Changelog
:cl:
fix: The preference menu has had its weird index lowered (Assets are no
longer semi garbled)
/:cl:

---------

Co-authored-by: LemonInTheDark <58055496+LemonInTheDark@users.noreply.github.com>

---

