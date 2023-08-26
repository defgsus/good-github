## *good gosh*

It's so many stuff on **github**! Here's one more attempt to *get a grip*. And
an [index](docs/messages.md).

---

# [2023-08-25](docs/good-messages/2023/2023-08-25.md)


there were a lot of events recorded by [gharchive.org](https://www.gharchive.org/) of which 2,273,908 were push events containing 3,459,984 commit messages that amount to 261,902,280 characters filtered with [words.py@e23d022007...](https://github.com/defgsus/good-github/blob/e23d022007992279f9bcb3a9fd40126629d787e2/src/words.py) to these 92 messages:


## [acdlite/react](https://github.com/acdlite/react)@[ac1a16c67e...](https://github.com/acdlite/react/commit/ac1a16c67e268fcb2c52e91717cbc918c7c24446)
#### Friday 2023-08-25 00:03:36 by Sebastian Markbåge

Add Postpone API (#27238)

This adds an experimental `unstable_postpone(reason)` API.

Currently we don't have a way to model effectively an Infinite Promise.
I.e. something that suspends but never resolves. The reason this is
useful is because you might have something else that unblocks it later.
E.g. by updating in place later, or by client rendering.

On the client this works to model as an Infinite Promise (in fact,
that's what this implementation does). However, in Fizz and Flight that
doesn't work because the stream needs to end at some point. We don't
have any way of knowing that we're suspended on infinite promises. It's
not enough to tag the promises because you could await those and thus
creating new promises. The only way we really have to signal this
through a series of indirections like async functions, is by throwing.
It's not 100% safe because these values can be caught but it's the best
we can do.

Effectively `postpone(reason)` behaves like a built-in [Catch
Boundary](https://github.com/facebook/react/pull/26854). It's like
`raise(Postpone, reason)` except it's built-in so it needs to be able to
be encoded and caught by Suspense boundaries.

In Flight and Fizz these behave pretty much the same as errors. Flight
just forwards it to retrigger on the client. In Fizz they just trigger
client rendering which itself might just postpone again or fill in the
value. The difference is how they get logged.

In Flight and Fizz they log to `onPostpone(reason)` instead of
`onError(error)`. This log is meant to help find deopts on the server
like finding places where you fall back to client rendering. The reason
that you pass in is for that purpose to help the reason for any deopts.

I do track the stack trace in DEV but I don't currently expose it to
`onPostpone`. This seems like a limitation. It might be better to expose
the Postpone object which is an Error object but that's more of an
implementation detail. I could also pass it as a second argument.

On the client after hydration they don't get passed to
`onRecoverableError`. There's no global `onPostpone` API to capture
postponed things on the client just like there's no `onError`. At that
point it's just assumed to be intentional. It doesn't have any `digest`
or reason passed to the client since it's not logged.

There are some hacky solutions that currently just tries to reuse as
much of the existing code as possible but should be more properly
implemented.
- Fiber is currently just converting it to a fake Promise object so that
it behaves like an infinite Promise.
- Fizz is encoding the magic digest string `"POSTPONE"` in the HTML so
we know to ignore it but it should probably just be something neater
that doesn't share namespace with digests.

Next I plan on using this in the `/static` entry points for additional
features.

Why "postpone"? It's basically a synonym to "defer" but we plan on using
"defer" for other purposes and it's overloaded anyway.

---
## [Iamgoofball/-tg-station](https://github.com/Iamgoofball/-tg-station)@[e80cf8f358...](https://github.com/Iamgoofball/-tg-station/commit/e80cf8f3586e5aeb599e8f54bd35ebafb878e101)
#### Friday 2023-08-25 00:13:34 by Jacquerel

Improved spider web AI (#76637)

## About The Pull Request

The AI I coded for spiders deciding where to make webs when they aren't
otherwise occupied would do so by finding the _closest_ valid tile,
which seemed like a good idea at the time. The problem with that is that
the "closest" algorithm we use has a predictable search pattern which
meant that spiders would always predictably make a diagonal line of webs
pointing South West, which looked very silly.
I've rewritten how they pick targets to introduce some randomness, which
causes them to properly spread out and make a nicer-looking structure:
which serves purely to annoy spacemen who need to pass through this
area.


![image](https://github.com/tgstation/tgstation/assets/7483112/cb01828f-7653-4010-a4f5-2abc6e10b630)

I'll be honest I mostly did this while bored waiting for other PRs which
I require for my other branch to get merged.

## Why It's Good For The Game

This probably only annoyed me to be quite honest and if you left one
alone for long enough it would fill enough space that you couldn't tell
anyway, but it does look nicer now.

## Changelog

:cl:
add: AI-controlled spiders will make more web-shaped webs.
/:cl:

---
## [iwishforducks/tgstation](https://github.com/iwishforducks/tgstation)@[41f20bc3ce...](https://github.com/iwishforducks/tgstation/commit/41f20bc3ced4e7853a09f2d5e1dcf46346f2e51f)
#### Friday 2023-08-25 00:23:17 by LemonInTheDark

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
## [ritorizo/Shiptest](https://github.com/ritorizo/Shiptest)@[1b315a616f...](https://github.com/ritorizo/Shiptest/commit/1b315a616ff24e3f1f92c791e4df4dc43ca9aad6)
#### Friday 2023-08-25 00:23:24 by Thedragmeme

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
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[2300ac2a96...](https://github.com/Jolly-66/JollyStation/commit/2300ac2a96d1ce7054d91d8707fb25ea7123c9e7)
#### Friday 2023-08-25 00:24:31 by TaleStationBot

[MIRROR] [MDB IGNORE] Goliath basic mob (#6764)

Original PR: https://github.com/tgstation/tgstation/pull/76754
-----
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

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>
Co-authored-by: Jolly-66 <70232195+Jolly-66@users.noreply.github.com>

---
## [Jolly-66/JollyStation](https://github.com/Jolly-66/JollyStation)@[cf70bc7948...](https://github.com/Jolly-66/JollyStation/commit/cf70bc7948f441a9d19fd1a72f027731a56f1334)
#### Friday 2023-08-25 00:24:31 by TaleStationBot

[MIRROR] [MDB IGNORE] Collapsible lobby buttons (#6766)

Original PR: https://github.com/tgstation/tgstation/pull/76443
-----
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

---------

Co-authored-by: Sealed101 <cool.bullseye@yandex.ru>

---
## [OliOliOnsiPree/tgstation](https://github.com/OliOliOnsiPree/tgstation)@[221e82c364...](https://github.com/OliOliOnsiPree/tgstation/commit/221e82c3640c75d99dc2616bf666bd897b4a5be8)
#### Friday 2023-08-25 00:24:48 by ChungusGamer666

[NO GBP] Fixes my fuckups with species livers (#76331)

## About The Pull Request

Fixes https://github.com/tgstation/tgstation/issues/76329
I DID A REAL STUPID MISTAKE WHILE CODING
https://github.com/tgstation/tgstation/pull/76184 I AM SORRY
The signal was sending the fucking human instead of seconds_per_tick

## Why It's Good For The Game

Fixes a BUNCH of liver behavior including plasmamen livers not healing
wounds

## Changelog

:cl:
fix: Plasma will now heal plasmamen properly
/:cl:

---
## [TypeVar/Shiptest](https://github.com/TypeVar/Shiptest)@[f07cb3bd3b...](https://github.com/TypeVar/Shiptest/commit/f07cb3bd3b52bfbdb7994aaf4ae68dcf90d57d2f)
#### Friday 2023-08-25 00:24:54 by Bjarl

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
## [ArcaneDefence/tgstation](https://github.com/ArcaneDefence/tgstation)@[a8e0d7c8d2...](https://github.com/ArcaneDefence/tgstation/commit/a8e0d7c8d202027d36c96391ed9a43cb5d708065)
#### Friday 2023-08-25 00:26:34 by MrMelbert

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
## [Cenrus/Daedalus-Dock](https://github.com/Cenrus/Daedalus-Dock)@[8f0512b923...](https://github.com/Cenrus/Daedalus-Dock/commit/8f0512b92377a891a728e83d1d269820e4c1d5f8)
#### Friday 2023-08-25 00:29:56 by Kapu1178

Spatialgridports (#352)

* adds an error message to movables not being removed from the grid... again (#75161)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->

I swear i didnt fail at this like 3 times i tested it this time.

adds a descriptive error of what spatial grid cells a movable is stuck
in, and in what channels. This only runs during unit tests. hopefully
this should be enough information to go off of to fix the spurious
cockroach error. if its not then i can try tracking all grid cell
changes during unit tests.
error looks like this:
```
[2023-05-03 04:16:34.009] runtime error: /mob/living/trolls_the_maintainer instance, which is in nullspace, and thus not be within the contents of any spatial grid cell, was in the contents of 2 spatial grid cells when it was only supposed to be in one! within the contents of the following cells: {(221, 119, 11), within channels: hearing}, {coords: (136, 136, 14), within channels: hearing}. (code/controllers/subsystem/spatial_gridmap.dm:581)
```
for something located in nullspace but still in the contents of >0 cells
and:
```
runtime error: /mob/living/trolls_the_maintainer instance, which is supposed to only be in the contents of a spatial grid cell at coords: (136, 136, 14), was in the contents of 6 spatial grid cells when it was only supposed to be in one! within the contents of the following cells: {(68, 153, 2), within channels: hearing}, {coords: (221, 170, 3), within channels: hearing}, {coords: (255, 153, 11), within channels: hearing}, {coords: (170, 238, 13), within channels: hearing}, {coords: (204, 119, 14), within channels: hearing}, {coords: (136, 136, 14), within channels: hearing}.
```
if its not in nullspace but its within more than 1 grid cell.

the coordinates here are translated from the index of the given cell to
world coordinates.

mothblocks has been standing outside my house for weeks i am fearing for
my life

---------

Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

* fixes contents not being removed from the spatial grid when deleted during movement between 2 grid cells (#75658)

## About The Pull Request
fixes the flaky test reports for cockroaches being stuck in the spatial
grid (which mothblocks seems to have closed all of)

cockroaches get deleted when they die, so theres a spurious unit test
failure where if a cockroach is on a tile in grid cell A and moves to a
lava tile in grid cell B, they will get killed when lava.Entered() is
called, then deleted, and when /atom/movable/Destroy() is called we try
to take them out of grid cell B (because their loc is the lava tile) but
they were never added to that cell yet because their movement never
finished, so that doesnt do anything. THEN moveToNullspace() is called,
that movement finishes before the first movement, and then in
Moved(old_loc = lava turf) we try to remove it from grid cell B which
again doesnt work, and then the first movements Moved(old_loc = original
turf) is called where we can actually remove them from the correct grid
cell, except we cant because in exit_cell() we subtract
`old_target.important_recursive_contents[channel]` from the cells
content lists, and since the target is deleted by this point it doesnt
have important_recursive_contents. so the fix here is changing this so
it subtracts `old_target.important_recursive_contents?[type] ||
old_target` instead, which works if the target is deleted.

also fixes some Entered() overrides that dont call parent and improves
documentation on spatial grid defines
## Why It's Good For The Game
fixes it without needing the change_loc() setter

* update for us

* missed this

---------

Co-authored-by: Kylerace <kylerlumpkin1@gmail.com>
Co-authored-by: Mothblocks <35135081+Mothblocks@users.noreply.github.com>

---
## [Prussen/tgstation](https://github.com/Prussen/tgstation)@[74892ae7ec...](https://github.com/Prussen/tgstation/commit/74892ae7ec80d47c64bf786f62985a1bd07d06f7)
#### Friday 2023-08-25 00:33:16 by LemonInTheDark

Optimization pass focused on foam code (saves about 30% of cpu usage I think) (#76104)

## About The Pull Request

Foam is crummy at high load rn, both because it runs on a low priority
background subsystem, and because it wastes a bit of time.
Let's reduce usage (while speeding up a bunch of other stuff too), and
give it more cpu generally.

[Optimizes reagent processing
somewhat](https://github.com/tgstation/tgstation/commit/d409bd4afc3c208cd6f00ff406e1e9f78d5ac5ad)

Turns out most of the cost of foam is the reagents it carries, and the
varying effects they have
I'm doing my best here to optimize them without touching "user space"
too much

That means doing things like prechecking if we're gonna spawn on top of
an existing decal (from glitter, flour, etc), and using that same proc
to also avoid spawning on unacceptable turfs (I had to convert
inheritance to a bitflag system to make this work, but I think that's ok
since we want it imparative anyhow)

It's actually nice for code quality too, since it lets me clean up code
that was using raw locates and weird var pong.
god I wish I had implied types man

[Optimizes foam spreading in its most accursed aspect, reagent
copying](https://github.com/tgstation/tgstation/commit/5cc56a64ad1a22ba7467cb0446b9558560259437)

Holy shit reagent code is a lot.

I'm doing a bunch of small things here. istype in init -> typecache,
removing procs that are called once and loop over a list we JUST looped
over (ph and the caching for reactions in particular)

I am mainly trying to optimize copy_to here, since that's what foam
spams
As a part of this, I removed a pair of update_total and handle_reactions
calls that were done on the reagents we are copying FROM

I have no god damn idea why you would want to do that, but if anything
is relying on the copy proc modifying the source, then that code
deserves to break

Speaking of, I cleaned up handle_reaction's main filter loop a lot,
removed a lot of redundant vars and changed it from a full loop w
tracker vars to an early exit pattern

This meant using a loop label, which is unfortunate, but this is the
fastest method, and it does end up cleaning up the code significantly,
Which is nice

Oh also I made the required_other var function even if there is no atom
attached to the reaction, since I don't see why it wouldn't

This last bit is gonna get a bit esoteric so bear with me

Failing calls (which are most of them) to handle_reactions are going to
be fastest if they need to check as few reactions as possible

One reagent in a reaction's required list is marked as the "primary",
and thus gets to trigger checking it.
We need all the reagents to react anyhow, so we might as well only check
if we have one particular one to avoid double checking

Anyhow, in order to make most calls the fastest, we want these reactions
distributed as evenly as possible across all our reagents.
The current way of doing this is just taking the first reagent in the
requirements list and using it, which is not ideal

Instead of that, lets figure out how many reactions each reagent is in,
then divy reactions up based off that and the currently divvied
reactions

This doubles the reagent index count, and takes the most common reagent,
water, from 67 reactions to I think like 22

Does some other general cleaning in reagent code too, etc etc etc

[Fixes runtimes from the forced gravity element being applied more then
once](https://github.com/tgstation/tgstation/commit/941d0676114fd455a585f2c65ffc79b81e8438b7)

I feel like this element should take a trait source or something to make
them potentially unique, it's too easy to accidentally override one with
another

[Removes connect_loc usage in atmos_sensitive, replaces it with direct
reg/unreg](https://github.com/tgstation/tgstation/commit/de1c76029d5c49dff152f0ea168b9e6c4a4a04aa)

I only really used it because I liked the componentization, but it costs
like 0.2 seconds off init alone which is really stupid, so let's just do
this the very slightly harder way

[Micros foam code slightly by inlining a LinkBlockedWithAccess
call](https://github.com/tgstation/tgstation/commit/744da3694cd4a85b3bdf44d754de57d7570bdd1c)

This is in the space of like 0.05 seconds kinda save so I can put it
back if you'd like, the double loop just felt silly

[Changes how foam processes
slightly](https://github.com/tgstation/tgstation/commit/ee5e633e3256fe7df229af71d78424d502459c16)

Rather then treating spreading and processing as separate actions, we do
both in sync.
This makes foam fade faster when spreading, which is good cause the
whole spread but unclearing foam thing looks silly.
It also avoids the potential bad ending of foam spreading into itself,
backwards and forwards. This is better I promise.

[Bumps fluid priority closer to heavy eaters, moves it off
background](https://github.com/tgstation/tgstation/commit/811797f09db7b060f75f15ad06d0ce8982375f47)

Also fixes a bug where foam would travel under public access airlocks.

## Why It's Good For The Game

Saves a lot of cpu just in general, from both init and live.
In theory makes foam faster, tho I'd have to test that on live at
highpop to see if I've actually succeeded or not. Guess we'll see.

---
## [Prussen/tgstation](https://github.com/Prussen/tgstation)@[63d6c2e962...](https://github.com/Prussen/tgstation/commit/63d6c2e9628be7af04948f59488043f109f1faab)
#### Friday 2023-08-25 00:33:16 by CRITAWAKETS

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
## [Prussen/tgstation](https://github.com/Prussen/tgstation)@[063bf74f31...](https://github.com/Prussen/tgstation/commit/063bf74f31a27ec8096fe10b844d5883be6d13a9)
#### Friday 2023-08-25 00:33:16 by carlarctg

There is no longer a 50% chance of catching a heretic out when examining them drawing influences (#76878)

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

---
## [Thunder12345/tgstation](https://github.com/Thunder12345/tgstation)@[52c8da7ea4...](https://github.com/Thunder12345/tgstation/commit/52c8da7ea49ef566c9a997a4b7cfc5d3d2a59178)
#### Friday 2023-08-25 00:33:23 by Jacquerel

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
## [Contrabang/tgstation](https://github.com/Contrabang/tgstation)@[8c2c72b0ed...](https://github.com/Contrabang/tgstation/commit/8c2c72b0ed7a1fad112fc4da8a8b7de7faa5e114)
#### Friday 2023-08-25 00:34:18 by LemonInTheDark

Duiffel Spotfix (#76442)

## About The Pull Request

Gives duffelbags their proper slot count
They inherited this from backpacks, but I sorta just forgot about that

[Creates "levels" of locked objects, uses that to make locked duffels
work](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

[c613c00](https://github.com/tgstation/tgstation/pull/76442/commits/c613c00f62fa3ff03bb33737d24da9acbf2050e3)

Turns locked into something that holds defines, this makes life a lot
easier.
Requires a lot of boilerplate because of how many uses of these procs
there are and all the passthrough and shit.

Adds a few outfit subtypes to avoid this class of failure in future.

Renames the args in a few but not all touched procs, one thing at a time

Closes #76407
Closes #76430 Had the lock check in the wrong place
Closes #76441 GOD I HATE TK SO MUCH

Wrote half the pr without glasses so if it's weird gimme some grace
yeah?

## Changelog
:cl:
fix: Fixes some fuck with duffelbags, them not holding enough + issues
with spawning gear in them (job shit and all)
/:cl:

---
## [Contrabang/tgstation](https://github.com/Contrabang/tgstation)@[d85e44c69c...](https://github.com/Contrabang/tgstation/commit/d85e44c69cc06dbeeb3a0de7f76273de45ee3893)
#### Friday 2023-08-25 00:34:18 by ChungusGamer666

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
## [Katskan/cmss13](https://github.com/Katskan/cmss13)@[d26452bb9a...](https://github.com/Katskan/cmss13/commit/d26452bb9a846091214ced880c5d7a34a6b61048)
#### Friday 2023-08-25 00:35:36 by Unknownity

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
## [Katskan/cmss13](https://github.com/Katskan/cmss13)@[5f5fcd2b27...](https://github.com/Katskan/cmss13/commit/5f5fcd2b279b2bd51b5869b0a345b4f964dcb34c)
#### Friday 2023-08-25 00:35:36 by Drathek

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
## [Ansekishokuu/tgstation](https://github.com/Ansekishokuu/tgstation)@[746b75844c...](https://github.com/Ansekishokuu/tgstation/commit/746b75844c0e05b521a2973cb0705fca304d287f)
#### Friday 2023-08-25 00:35:47 by necromanceranne

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
#### Friday 2023-08-25 00:35:47 by Jacquerel

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
## [Erol509/Skyrat-tg](https://github.com/Erol509/Skyrat-tg)@[4537b1e980...](https://github.com/Erol509/Skyrat-tg/commit/4537b1e980f226f2f6a18ef1c92d6ffc3e3b6ac4)
#### Friday 2023-08-25 00:36:16 by Bloop

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
## [IFuckedUpMerging/tgstation](https://github.com/IFuckedUpMerging/tgstation)@[ed57b8127f...](https://github.com/IFuckedUpMerging/tgstation/commit/ed57b8127f1b28507272170c60c7db16f6e02a87)
#### Friday 2023-08-25 00:36:39 by Jacquerel

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
## [SingingSpock/tgstation](https://github.com/SingingSpock/tgstation)@[cfd40aeef5...](https://github.com/SingingSpock/tgstation/commit/cfd40aeef5dc1e051e5937e43a69c1df3bb4eca1)
#### Friday 2023-08-25 00:40:46 by necromanceranne

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
## [Smalltasty/tgstation](https://github.com/Smalltasty/tgstation)@[03c964ac45...](https://github.com/Smalltasty/tgstation/commit/03c964ac45e727543aac85ad817df89a7555fb31)
#### Friday 2023-08-25 00:46:21 by LemonInTheDark

Reworks Duffel Bags (Zippers) (#76313)

## About The Pull Request

Reworks duffel bags in line with oranges proposed plan.


![image](https://github.com/tgstation/tgstation/assets/58055496/126743dd-d7b8-47e0-bdd8-a0caec39c515)

Basically, instead of just making you slower all the time, they make you
slower while you have them open, but give you the same speed while
they're closed.
As a trade off, opening and closing them takes time, 2.1 seconds
(matches the sound) and 0.5 respectively.


https://github.com/tgstation/tgstation/assets/58055496/555d2cd0-038e-4b0b-a693-0c66dac16f5b

[Adds support for limiting extra storage, uses it to make syndie stuff
cool](https://github.com/tgstation/tgstation/pull/76313/commits/d0b2bbf937435b36de3ba497c48771f563b76684)

[d0b2bbf](https://github.com/tgstation/tgstation/pull/76313/commits/d0b2bbf937435b36de3ba497c48771f563b76684)

Syndicate bags currently ignore downsides by just ignoring the slowdown,
but that's kinda boring so let's just buff em instead.

They now support holding a limited amount of bulky items (3), filtered
down to things that would otherwise constitute going loud (or otherwise
be useful to carry around as a loudish traitor)

I may have gone a bit overboard on what I whitelisted here, lemme know
yeah?

I also did some fenangling with backpack uses of create_storage, I don't
like this pattern it was a bad idea I think.

## Why It's Good For The Game

I'm unsure if these delays enough, I think any length of time is decent
since it means you need to stop moving and focus on it for a bit.
My hope is this will make them a proper sidegrade, rather then something
that goes unused/acts as newbie bait

## Changelog
:cl:
balance: Duffelbags will now only make you slow while they are unzipped.
As a tradeoff, you now need to stand still and zip/unzip them to access
their contents/not move real slow.
/:cl:

---------

Co-authored-by: MrMelbert <51863163+MrMelbert@users.noreply.github.com>

---
## [AnywayFarus/tgstation](https://github.com/AnywayFarus/tgstation)@[2ee79d7077...](https://github.com/AnywayFarus/tgstation/commit/2ee79d7077804f4e918d6c4bdbe856570cf24a01)
#### Friday 2023-08-25 00:46:41 by Jacquerel

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
## [nikothedude/Skyrat-tg](https://github.com/nikothedude/Skyrat-tg)@[4aec91cc06...](https://github.com/nikothedude/Skyrat-tg/commit/4aec91cc069b1beb1ec6593522dc5f65f7c5c7aa)
#### Friday 2023-08-25 00:53:31 by GoldenAlpharex

[MANUAL MIRROR] Fixes carbon bodytypes not always being synchronized with bodyparts + Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused [MDB IGNORE] (#22519)

* Fixes carbon bodytypes not always being synchronized with bodyparts (#76522)

Fixes https://github.com/tgstation/tgstation/issues/76481
TLDR /mob/living/carbon/human/species subtypes were NOT updating their
bodytypes on spawn due to absurd and wacky carbon bodypart creation code
that meant try_attach_limb() never got called (What the FUCK?)

* Fixes CI too

* [NO GBP] Fixes dumb usage of TRAIT_LIVERLESS_METABOLISM i caused (#76500)

## About The Pull Request

TRAIT_LIVERLESS_METABOLISM should do what it implies, and make you
always metabolize as if you were liverless.
This was a stupid mistake on my part because I wasn't aware
TRAIT_STABLELIVER was a thing.

## Why It's Good For The Game

TRAIT_LIVERLESS_METABOLISM and TRAIT_STABLELIVER should not behave the
exact same.

## Changelog

Not quite player facing.

* I fucking swear I fixed this before

---------

Co-authored-by: ChungusGamer666 <82850673+ChungusGamer666@users.noreply.github.com>

---
## [Looks-to-the-Moon/tgstation](https://github.com/Looks-to-the-Moon/tgstation)@[867c217c57...](https://github.com/Looks-to-the-Moon/tgstation/commit/867c217c57bbcbb644e06bfcb6d362e494a895ee)
#### Friday 2023-08-25 00:56:09 by GuillaumePrata

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
## [Unknownity/cmss13](https://github.com/Unknownity/cmss13)@[a48f036428...](https://github.com/Unknownity/cmss13/commit/a48f0364283526637b637542b432d91593b2bdf5)
#### Friday 2023-08-25 00:57:52 by QuickLode

Colony Synthetics have less resistance but are faster. (#3821)

# About the pull request

<!-- Remove this text and explain what the purpose of your PR is.

Mention if you have tested your changes. If you changed a map, make sure
you used the mapmerge tool.
If this is an Issue Correction, you can type "Fixes Issue #169420" to
link the PR to the corresponding Issue number #169420.

Remember: something that is self-evident to you might not be to others.
Explain your rationale fully, even if you feel it goes without saying.
-->
While exploring reasons why this role was underplayed one of the things
that came up was its speed. It is dreadfully slow - to the point where
defenders are able to force an engagement against Synthetics. There is
no chance to run from anything faster as a Colony Synthetic. Making it
have to fight often.

Lowering the resistance is something devs wanted, and for gameplay this
is good because a Synthetic shouldn't be forced into a fight unless they
have no other option. Especially not by something as slow as a defender.
Might tweak later but council generally is in agreement with this
change. Little by little!

For the CQC, a Colony Synthetic is not as advanced as a Shipside one,
but still is more than capable of outmanuevering a human. As for the
hilarious UPP Pvt being better than a Colony Synth in CQC I will make a
separate PR

For Fireman, a Synthetic can bend metal, move cars and do many other
'superhuman' feats of stength, they should not struggle at carrying
people, especially shouldn't be worse at carrying people than a Marine.
It's from 1 to 3, to represent the strength yet aging capabilities of
the Colony Synthetic. @morrowwolf forgot this one

- doesn't touch WJ
# Explain why it's good for the game
Less resistance is something devs wanted.
Allows Colony Synthetics an option to avoid certain engagements as now
they are able to outrun some types of Xenomorphs off-weeds. Defenders
should not be able to catch them offweeds.
A Synthetic should have no problem carrying something as light as a
human being - they especially should not have MORE trouble carrying
someone than your standard human doctor.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: QuickLoad
balance: Colony Synthetics are faster but are less resistant. This
allows for the option of avoiding engagements.
balance: Colony Synthetics have slightly better CQC and can carry people
better.
/:cl:

---
## [Mooshimi/tgstation](https://github.com/Mooshimi/tgstation)@[988a6dcc21...](https://github.com/Mooshimi/tgstation/commit/988a6dcc2142b4ef3244a18ad4e1781671fb7320)
#### Friday 2023-08-25 00:59:06 by YehnBeep

Removes suicide check from positronic brains (#76081)

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

---
## [Mooshimi/tgstation](https://github.com/Mooshimi/tgstation)@[803658dc30...](https://github.com/Mooshimi/tgstation/commit/803658dc30b4445e81592daa1823a98719246269)
#### Friday 2023-08-25 00:59:06 by Rhials

Deadchat Announcement Variety Pack 2 and also some fixes to other popups (#76053)

## About The Pull Request

This adds ghost orbit popups for the following: 
- Macrobombs (or stacked microbombs) being triggered.
- HFR Meltdowns.
- Living players about to be gored by an emagged organ harvester.
- Nuclear devices being armed.
- Doomsday devices.
- Blob hosts bursting.

This also modifies the following ghost orbit popups:
- Toy hot potatoes will no longer cause a popup when armed.
- Normal spider eggs will not flash the byond window, only special egg
types.
## Why It's Good For The Game

Gives more gathering spots/information to deadchat. Let no entertaining
moment in this game go unobserved.

Spider eggs flashing your window for every single egg produced makes
alt-tabbing suck. I saw some guy on the forums complaining about it and
thought "huh yeah I guess he's got a point that pisses me off too" so
here we are.
## Changelog
:cl: Rhials
qol: Basic spider eggs no longer flash the byond window when ready to
hatch.
qol: Toy hot potatoes no longer give a ghost notification.
qol: Deadchat will be notified in the event of an imminent macrobomb
detonation, HFR meltdown, organ harvesting,
qol: Deadchat will be notified when a nuclear/doomsday device is
activated, as well as when a blob-infection bursts.
/:cl:

---
## [Thlumyn/Skyrat-tg_thlumyn](https://github.com/Thlumyn/Skyrat-tg_thlumyn)@[a1609c4536...](https://github.com/Thlumyn/Skyrat-tg_thlumyn/commit/a1609c4536fe05f95560bd1a1be4607b944ee5a5)
#### Friday 2023-08-25 00:59:56 by SkyratBot

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
## [VastKilleroOm/Skyrat-tg](https://github.com/VastKilleroOm/Skyrat-tg)@[e9eccf3b0b...](https://github.com/VastKilleroOm/Skyrat-tg/commit/e9eccf3b0bc57137a03ee319b0e081e78a8b06ed)
#### Friday 2023-08-25 01:00:45 by SkyratBot

[MIRROR] Removes the word "chemical" from "chemical patch" [MDB IGNORE] (#22610)

* Removes the word "chemical" from "chemical patch" (#76966)

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

* Removes the word "chemical" from "chemical patch"

---------

Co-authored-by: Justice <42555530+Justice12354@users.noreply.github.com>

---
## [VastKilleroOm/Skyrat-tg](https://github.com/VastKilleroOm/Skyrat-tg)@[606f0009a1...](https://github.com/VastKilleroOm/Skyrat-tg/commit/606f0009a1b61472a534b3dbc7e618680b292f55)
#### Friday 2023-08-25 01:00:45 by SkyratBot

[MIRROR] Removes two redundant components [MDB IGNORE] (#22613)

* Removes two redundant components (#76866)

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

* Removes two redundant components

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [BeagleGaming1/cmss13](https://github.com/BeagleGaming1/cmss13)@[d045a5d654...](https://github.com/BeagleGaming1/cmss13/commit/d045a5d6547dcda9fc04be9b6cd50d2ff44e672f)
#### Friday 2023-08-25 01:01:48 by Drathek

Larva Queue Late Joiner Nerf (#3803)

# About the pull request

This PR makes it so players who haven't played yet have their join time
recorded, and that is used for their initial sorting value rather than
0. This means late joiners will be at the back of the line as if they
had just died.

This PR also fixes an oversight where ghosting as a facehugger would
count as death. Even though they really shouldn't be ghosting when
alive, they still shouldn't be penalized as far as the queue is
concerned.

# Explain why it's good for the game

Its not; its a bad experience for everyone that hasn't even gotten one
life in the round. However it seems I'm in the minority thinking that a
xeno shouldn't squander their first life and that death shouldn't bear
more consequences.

# Testing Photographs and Procedure
<details>
<summary>Screenshots & Videos</summary>

The new informational message if you press join as xeno while currently
ineligible to be a xeno candidate:

![image](https://github.com/cmss13-devs/cmss13/assets/76988376/9fb295c2-e654-4843-9e3e-bf37f2c8755e)

</details>


# Changelog
:cl: Drathek
del: Remove first life priority for larva queue
fix: Fix ghosting as a facehugger counting as death for the larva queue
/:cl:

---
## [Shroopy/tgstation](https://github.com/Shroopy/tgstation)@[a2c8cce535...](https://github.com/Shroopy/tgstation/commit/a2c8cce5359162a8a697ce109801ec268bf0c8a5)
#### Friday 2023-08-25 01:04:43 by John Willard

Bilingual can now choose their language (#76609)

## About The Pull Request

This was one of the tradeoffs for removing other, more consistent
sources of languages, and was requested by Melbert among many others.
This does go against my wanted goal of decreasing the risk of
eavesdropping by other players through just magically knowing a
language, but it is an expensive quirk and it is in their medical
records, which makes it better than language encryption keys or silicon
just innately knowing them.

This also limits Bilingual to only roundstart languages (+Uncommon),
rather than being randomly selected from a list (that had very useless
ones like monkey, podpeople, and beachbum). This is mostly just for
modularity, I didn't want to make it look terrible code-wise and thought
this may be the optimal way to handle it.

This is also me going back on
https://github.com/tgstation/tgstation/pull/71773 - which I had closed
myself.

## Why It's Good For The Game

If we're gonna keep the Bilingual quirk, it might as well be something
players can choose the language of, it's their character and they should
be allowed to decide how their character is, and it is my fault that
this stupid compromise of "getting a random language" was made in the
first place. It never should've happened.
It now actually limits it to roundstart-only languages, so there's no
way you can spy on people who prepare in advance through becoming
podpeople, or monkeys, etc.

## Changelog

:cl:
balance: Bilingual quirk now lets you choose your language between ones
given to roundstart species.
balance: Foreigner and Bilingual are now mutually exclusive languages.
/:cl:

---
## [avimour/Skyrat-tg](https://github.com/avimour/Skyrat-tg)@[9701b40ca0...](https://github.com/avimour/Skyrat-tg/commit/9701b40ca03e164bd8bd4238fafb6cf778c52efe)
#### Friday 2023-08-25 01:05:20 by SkyratBot

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
## [Zonespace27/cmss13](https://github.com/Zonespace27/cmss13)@[5c4b13863f...](https://github.com/Zonespace27/cmss13/commit/5c4b13863f90877e920ce329bd60e99559d7fe35)
#### Friday 2023-08-25 01:05:52 by ihatethisengine

Larva surge is limited by marines/xenos ratio (#3592)

# About the pull request

Xenos after hijack now get larva based on marines/xenos ratio. Instead
of infinite larva, larva surge will try to increase the initial amount
of xenos on hijack to 50% of marines forces over time (with a minimum of
5 larvas, if xenos already have good numbers).

# Explain why it's good for the game

Initially, if I remember correctly, larva surge was brought into the
game to discourage marines from early meta-evacuations, which is fair.
But consequently, it really hurt the hijack sequence. Even if marines
evac fair and square, larva surge still comes in action and makes
situation for marines even worse, utterly discouraging everything but
either boomrushing the Alamo or holding lifeboats to evac.

This resulted in hijacks being very repetitive and boring. More than
that, larva surge is extremely busted on lowpop due to the fact you can
get around 20 xenos from nothing, making lowpop hijack even less
interesting. So with this change marines will still get punished for
evaccing with good numbers, but won't be penalized as much for honest
evacuations.

So hopefully, we will see more variety of hijacks and more interesting
stories!

P.S. if you have a better formula, let me know.


# Testing Photographs and Procedure
<details>
My friend @Diegoflores31 tested this for me, thanks!
<summary>Screenshots & Videos</summary>

Put screenshots and videos here with an empty line between the
screenshots and the `<details>` tags.

</details>


# Changelog
:cl: ihatethisengine
balance: larva surge is limited by marines/xenos ratio
fix: xenos no longer get free larva from abandoned facehuggers during
hijack
/:cl:

---------

Co-authored-by: ihatethisengine <treml.treml@yandex.ru>
Co-authored-by: fira <loyauflorian@gmail.com>

---
## [thpatch/thcrap-tsa](https://github.com/thpatch/thcrap-tsa)@[845d6ec3fa...](https://github.com/thpatch/thcrap-tsa/commit/845d6ec3fa2157da989382e3dc931a62cfe48dbf)
#### Friday 2023-08-25 02:00:04 by Egor

th095: fix draw_ctext and draw_rtext not using sprintf

In particular this fixes the "100%%" bug in the help lines.

This is essentially adding a missing sprintf_call/sprintf_rep, with the
catch that sprintf_call had to be integrated into the spell_align
binhacks, as these actually rewrite a big chunk of the draw_[cr]text
functions.

I guess the assumption was that none of the callers pass extra
arguments, so it's safe to not run sprintf at all. That's not the case,
because %% still has to be unescaped to %. Granted, in the original
game, you'll never see a string with %% go through draw_[cr]text, but
that can always change due to translations, or, as in this case, due to
some draw_ltext call being changed to draw_ctext. The moral of the story
is to always replace sprintfs with sprintfs, no matter how stupid they
are. Oh, and to use the satisfying and clarifying NOPs :-)

Thanks to Inasaya Flanderin for reporting this issue.

---
## [Ical92/tgstation](https://github.com/Ical92/tgstation)@[0dd3e66aef...](https://github.com/Ical92/tgstation/commit/0dd3e66aefa2a61cb4e78482273958c1d09f8295)
#### Friday 2023-08-25 02:37:45 by Vekter

Grilles take 0-1 damage when shocking something, power sinks are available at lower reputation (#77860)

## About The Pull Request
Ports BeeStation/BeeStation-Hornet#3590. As it is right now, it's
trivial to set up a contraption using a conveyor belt and a shocked
grille to continuously shock monkey bodies. While this is very funny, it
also serves as a ghetto powersink that's hard to locate, easy to
replicate, and lasts effectively forever, since you can just keep
shocking the same bodies over and over again.

This doesn't completely remove the ability to make these, but it makes
them require at least a little maintenance and provides a way for them
to stop working even if the crew isn't able to locate them.

In an attempt to finally get people using the _actual_ powersink,
they'll show up a bit earlier in progression now. I'm not convinced 20
minutes is enough, but I don't want to put them in early enough that it
fucks with Engineering's ability to set things up at round start. We can
turn this down further if need be.

I'm also up for turning the TC requirement down, but 11 feels about
right for what they're supposed to do, so I'd prefer we try this first
and see how that works.

## Why It's Good For The Game
I'm all for goofy weird shit players have found, but there's an issue
with being able to do what an antag item is supposed to do but just
plain better. This shouldn't make creating these impossible or make them
unusable, but it'll require players to actively monitor them if they
want it to run for an extended period.

Additionally, we don't really see powersinks much anymore, and while
that might be more because powernets are kind of buggy and unreliable, I
think making them easier to get will make them show up a little more.

## Changelog
:cl: Vekter
balance: Grilles will now take 0-1 damage every time they shock
something.
balance: Powersinks are now available earlier in traitor progression.
/:cl:

---------

Co-authored-by: Fikou <23585223+Fikou@users.noreply.github.com>

---
## [i3roly/glibc_ddwrt](https://github.com/i3roly/glibc_ddwrt)@[60cb7ace15...](https://github.com/i3roly/glibc_ddwrt/commit/60cb7ace15ee95be5c8de3701aff4294b160f101)
#### Friday 2023-08-25 02:39:41 by gagan sidhu

[4.14.323/v53425] update glibc(2.38), kernel(4.14.323), misc apps

- update glibc (2.38)
- update kernel (4.14.323)
- update util-linux (2.39.2)
- update less (643)
- update frr in lootbag
- update groff in lootbag
- everything is now built with gcc 13.2.0 (twirls finger)

- i updated glibc because these guys decided to add strlcpy and strlcat.
  so then i made the choice to recompile anything that used these
  functions (from libbsd). so a lot of stuff that was linked to libbsd
  is now linked without it (except frr because i forgot)

-  kernel 6.1 seems like a no go. it's too big. i could remove tcpdump
   but the problem is it's still going to be a tight fit, and i'd have
   to probably remove other things. i don't know. plus i've lost the
   appetite to update the kernel after linux kernel devs decided they're
   bigger than gLIBC with their 64 bit time crap.
        -now if you build glibc for kernels 5.0 and newer, there will
        probably be userspace breakage for any programs compiled on
        earlier versions, which defeats the entire principle of glibc.

        -so since the linux development team thinks they're bigger than
        the library that makes them, i don't think i should invest any
        more time in trying to stay up to date.

i've had a top build for over 4 years as of this september,
        - with all the buttons working, and the LEDs.
        - if that support fizzles out in the next year or two, i don't
        think it'll be a bad thing.
                -in fact, i thought this update may be pointless, since
                the previous build seems great.
                        -BUT since some of you guys just love to update
                        your stuff, i decided to spin the build anyways.

i was busy taking over the "redneck swap", a term i've coined for the
americans going hog-wild over the HANDA J32A2 manual transmission,
swapping it into other HANDAs that come in different ages, shapes, and
sizes.
        -i call it that because they just don't care about "no lights"
        on the dash.
                -it's the antithesis of japanese tuner culture, and is
                both defiant and non-compliant with the RICH HANDA
                tradition, which, hilariously enough was started by a
                man named JACQUES FUCKING VILLENEUVE (in Canada) with
                his commercials that always said "in every HANDA car is
                a HANDA engine".

so that's why i also haven't updated. anyways i'm getting bored because
i've done too many things and mitt STILL think he's "the math guy" with
"the business sense". i haven't seen mitt do a fraction of what i have.

all i've seen mitt do is hold a picket sign SUPPORTING the vietnam war

https://www.nytimes.com/2012/09/12/us/politics/at-stanford-romney-stood-ground-on-vietnam.html

and his followers think he's the "Mormon John Lennon"

if people ever wanna really look into it, look up the "mormon mafia".
it's true that the intelligence agencies are full of mormons, then of
course mitt can do what he wants. the question is, how much is mitt
really behind when his religious followers are also in control of the
intelligence agencies?
        -it seems ol' Nino Brown (obama), or his team, in their thirst
        for the 2012 election, pretty much shit all over mitt and outed
        him him for what he is. they even established his role in the
        iran/contra scandal (transal), which as now an infamous CIA operation.
now, if that is all true, then of course mitt is the key to all of it.
        -everything. i know it's so fucking funny that it's hard to
        believe, but it's actually true lol.

cool world--sorry, i mean GLOBAL ECKANAMY, bro.

P.S. I DID NOT TEST THIS BUILD BUT I DON'T SEE WHY IT WOULDN'T WORK. i
am at 41 days uptime and i'm trying to keep ti going.

---
## [nsanso/portfolio](https://github.com/nsanso/portfolio)@[21bb6742bd...](https://github.com/nsanso/portfolio/commit/21bb6742bd5b35cb363848f1764155a8973bb494)
#### Friday 2023-08-25 02:55:33 by nsanso

I don't know. Something in chat-server, something in life.

I'm NOT doing chat-server authentication any time soon cause GDPR is annoying.
I'm going to settle for guests and chat.

In life I'm working on making stuff work in the most basic way possible first.
The life algorithm SHOULD be implemented. It's not tested, I don't know if it's correct.
It works on a fixed size grid. Infinite grids are going to have to wait.
It's not even hexagonal. That's the next step.
The main thing I need to do right now is to figure out how the hell you pass an array as a WebGL uniform.
Pass the grid, draw it though the fragment shader, replace the home background image.

Timeline is:

chat: guest session > send messages > get messages through stream > > > > auth (following gdpr) > oauth2
life: uniform buffers > hexagons (cube coords) > infinity and beyond (with octtrees) > volumetric rendering > compute shader workaround
home: aim header image to life > nicer sections > working contact form > actually write it

---
## [DragonFire101/Foundation-19](https://github.com/DragonFire101/Foundation-19)@[b4642dc835...](https://github.com/DragonFire101/Foundation-19/commit/b4642dc835dc801d801fd543cfd34bd44ca23929)
#### Friday 2023-08-25 03:04:19 by cheesePizza2

Armor improvements (#1251)

* the fixes

* FUCK YOU

* few more improvements

* bring em back

* fuck you

---
## [Wrosh/Wrosh.github.io](https://github.com/Wrosh/Wrosh.github.io)@[296682536f...](https://github.com/Wrosh/Wrosh.github.io/commit/296682536f502c1ddc83ee9ec8be070fcfe297a9)
#### Friday 2023-08-25 03:36:27 by Wrosh

Update index.html

removed stupid fucking text shadow cause that shit is ass omg

---
## [space-wizards/space-station-14](https://github.com/space-wizards/space-station-14)@[370cbfbbdd...](https://github.com/space-wizards/space-station-14/commit/370cbfbbddcd767c4403f452f981b8ed2538ed5a)
#### Friday 2023-08-25 03:40:06 by Flareguy

Yet Another Asteroid-Related Tile Update (read: asteroid tile variantizing) (#19237)

* makes asteroid tiles and snow use weighted variantize, adds snow plating

* GO FUCK YOURSELF!!!!

* hello? boner department, id like to order a DINNER. make it MAMA LUIGI

* test fix. hopefully. boner. boobies.

* did he know? (no)

---
## [k21971/EvilHack](https://github.com/k21971/EvilHack)@[3a3cd5ad71...](https://github.com/k21971/EvilHack/commit/3a3cd5ad7103c5282cd64f7ec389ed063b2fe7bc)
#### Friday 2023-08-25 03:43:33 by k21971

Wizard of Yendor's tower overhaul.

The Wizard of Yendor's home has undergone renovations. The old place was
a bit too restrictive, and security was somewhat lax 🙂

Quite a few changes in this commit. The Wizard's tower is now unlike
anything from its previous incarnation. Here's the breakdown:

* The Wizard's tower is still three levels as before, but each level has
been completely redesigned
* The ground level is much larger than before, with the entire base of
the tower surrounded by a moat, and the wizard has conscripted a company
of the Yendorian army as security
* The second/middle tower level is smaller than the first, and houses
various spellcasters that are there to train under the watchful eye of
the Wizard. Some monsters have been held captive here, used for
experimentation and other dark arts
* The third and final level is the very top of the tower, where the
Wizard of Yendor performs the most evil of magic spells on a magical
floating platform outside of, but connected to, the top of his tower.
This is also where the Wizard hoards his most prized treasures,
including the fabled Book of the Dead
* Entering the final level of the Wizard's tower is now counted as an
event and an achievement, and is livelogged. This also triggers a
message when entering the top level for the first time, warning the
player about falling to their death should they misstep (open air
terrain)
* How the special levels in Gehennom appear had to be tweaked a bit, as
it were possible from the initial 'wizard's tower is its own branch'
commit that the VS level could sometimes not be generated, and the
player could skip the invocation and take the stairs straight down to
the Sanctum. So now, the total number of Gehennom levels shaved off is
four instead of five, but the demon boss levels will always appear in
the correct order and with a tighter spread. The 'fake' wizard towers
are dropped from two to one, with the one guaranteed to have the portal
to the wizard tower branch, and it will always be the last Gehennom
level right before the VS level
* A fix for ants sometimes spawning in barracks was slipped into this
commit (NetHack 3.7 commit 23428d0)

The vast majority of changes are in the .des file for the tower
redesign. Storming the Wizard's tower will now be a more challenging
endeavour, but more rewarding also, and hopefully a lot more exciting
and fun than before.

---
## [Sonic121x/Skyrat-tg](https://github.com/Sonic121x/Skyrat-tg)@[d7542fb5e3...](https://github.com/Sonic121x/Skyrat-tg/commit/d7542fb5e3a73383b5b09f2d8758d0511466626f)
#### Friday 2023-08-25 04:24:37 by SkyratBot

[MIRROR] [no gbp] Adds missing chat feedback to watcher abilities [MDB IGNORE] (#23212)

* [no gbp] Adds missing chat feedback to watcher abilities (#77700)

## About The Pull Request

I kept meaning to add this in my last PR and kept thinking "I'll add
that in with these review changes" and then forgot every time. This
should make it clearer what is happening to you and why.

Also I made the gaze ability stun the user for a short period after it
goes off because them shooting you instantly after they stop channeling
_is_ sort of bullshit.
Also while testing this I noticed the AI interrupt one of its actions to
do the other one which is a bit silly so now it cannot do that.

## Why It's Good For The Game

Outlines in the log why something bad just happened to you.

## Changelog

:cl:
qol: Added some textual feedback to new watcher abilities
balance: Watchers will not attack for a short period following their
gaze attack
fix: Watchers won't interrupt one ability to use the other one
/:cl:

* [no gbp] Adds missing chat feedback to watcher abilities

---------

Co-authored-by: Jacquerel <hnevard@gmail.com>

---
## [kogelf/The_Arena_5_1](https://github.com/kogelf/The_Arena_5_1)@[7328317bdf...](https://github.com/kogelf/The_Arena_5_1/commit/7328317bdf737d87f5338c251551070fc3c7d291)
#### Friday 2023-08-25 04:27:16 by kogelf

szrh.knSZli'gjp
hoASEGHsnhR fuck this stupid shit I cant

MMMMMM I want to get mony and validation from other people

Idea SEX work

give me money NOW

---
## [unbl0ck/unbl0ck.github.io](https://github.com/unbl0ck/unbl0ck.github.io)@[3e8158dbe3...](https://github.com/unbl0ck/unbl0ck.github.io/commit/3e8158dbe37a9bd6b68a4286ff4faceea2068108)
#### Friday 2023-08-25 04:33:08 by unbl0ck

updated footer/game count

i hate my life, why did i choose to do it like this, im gonna have to change this every multiple of ten now.

---
## [Quake-Backup/freedoom](https://github.com/Quake-Backup/freedoom)@[d71ac12cf4...](https://github.com/Quake-Backup/freedoom/commit/d71ac12cf4f4774089ed4949eb0e26fb4debb4e1)
#### Friday 2023-08-25 04:52:27 by mc776

levels: another big batch of fixes. (#997)

* level: more fixes.

E1M3
- Minor item floating in one of the staircases.

E1M7
- Widened the item trenches in the northwest switch room to minimize the chance of a floating item.
- Narrowed the water trench in the southeast switch area to prevent someone from squeeze-gliding in.

E1M9
- Funny-shaped nukage bridge no longer has visible switches. Instead, that railing can be used from the outside anywhere along any of the long sides to lower it.
- Door on the north of that bridge was missing a doortrak.

E3M5
- Northeast giant blood pit had floating items in the new ledges. (Those bits are now also 100% pure meat instead of the rocky crust on top.)

E4M4
- Secret in the southwest is now the room instead of the doorway. Lighting adjusted accordingly.

E4M5
- There's an obscured lamp in the northwest that's supposed to look (in id) like a small lamp placed on top of the box. Freedoom's yellow lamp doesn't work for this, but Freedoom's candle sprite is perfect for the intended effect, so now it is that instead.

E4M6
- Various thin secrets.

E4M7
- Thing no. 580 was the wrong type and bled into the ceiling (see #941). The blocking version is now used instead.

E4M8
- The secrets by the starting area are now the rooms themselves instead of the doorways.

Map11
- Untagged the lizardbaby-triggered doorway as secret.
- All lizard baby sectors are now 72 units tall.
- Realigned the vines in the trilobite corridors overlooking the western atrium.
- Berserk red key secret room lengthened to guarantee having to step inside it.
- Red key is now at a different location, the platform now being a teleporter to it, allowing the location of the red key to be a single sector that can be flagged as a secret.
- Replaced the light source in the yellow skull room with something less likely to have already fallen over.
- Replaced the evil eyes with tech lamps since those aren't shootable.
- The trigger for releasing the pain bringers in the nukage fountain is once again a walk line.

Map16
- Every sector in the backpack secret was tagged as secret, leaving a total of 3 secrets one of which was skippably thin. The skippable is now untagged.

Map18
- It was possible to squeeze into the blue key pillar to trigger the ambush prematurely. The pillar is now the entire 64x64 platform.

* levels: more fixes.

E3M7
- Ambush-flagged and moved the pinkies in the lower small intestine so they stop trying to block the player from below either drop.
- Got rid of some orthogonal lines in the intestine to get rid of the fake contrast.

Map11
- Jump-proofed the decorative canal areas near the final arena.
- Some attempts to address #996.

Map14
- Removed the close-30-seconds door for the descending serpentipede monster closet because if they all bunch up like that while you have an SSG it's a boring wait afterwards. Have fun being hunted by them in the corridors!
- Addressed #996 in the south.

Map15
- Made the two lifts to the red armour secret visually consistent with each other.
- Some feeble attempts to address #996.

Map17
- Jump-proofed by Catoptromancy: numerous platforms raised above what should be jumpable in most sourceports that enable it by default.
- Added a backpack by the corpse near the start, as playing the map "right" and refraining from shooting until you get the tripod puts you in significant danger of running into a shellbox while at near full.
- The stairs inside the living room are flush up against the wall, so you don't waste time falling off and getting back on.
- The window texture now better matches the light falling on the floor.
- Moved Tree #73 and #37 as they were being invisible jump-blockers from below.
- Restored there being three chunks of rock for the blue key.
- Changed up a lot of textures in hopes of creating visually distinct areas.
- Added an extra secret in the start tunnel.
- Made the switch in the water go to 8+LAF fast instead of lowest because those weird sudden flat changes didn't look good.
- Shrank the pillars near the yellow key so you could move around all of them.
- Changed the torches inside the southern switch corridor to techlamps, and added new torches around the entrance to the eastern building.
- Changed the hanging corpse in the living room to another hanging corpse. (see #941)
- Made the couch look more like a couch. And one that's been in a war zone.

Map23
- Replaced the haphazard texture on the northern teleporter room and added some light sources.
- Improved the trim around sector 236 so the door doesn't go right into the curve.
- Used the correct CONS1 flat for sector 246 and shrank it accordingly.
- Addressed #996 in the south.
- Moved the (non-hanged) corpse in the starting secret out of the doorway. The way it hinted at the true nature of that wall was really neat but sadly doesn't play well with software renderer.

Map25
- Southern curved tunnel had a single orthogonal line that led to a misleading fake contrast.
- Some feeble attempts to address #996.

* Delete map17m.wad

* levels: restore old e2m1.

* levels: address E3M6 softlock.

see #998

---
## [jupyterkat/Yogstation](https://github.com/jupyterkat/Yogstation)@[9db2f06363...](https://github.com/jupyterkat/Yogstation/commit/9db2f06363bc325a0e8eadfdf7266e55def4d7c1)
#### Friday 2023-08-25 05:11:57 by Scrambledeggs

Fuck you *Ungreens your Peacekeepers* (#20053)

* Sprites Part 1: I hate transparency

* Sprites Part 2: Electric Booogaloo

* lack of transparency fixed

* More sprite fixes

* Tacmask and sprites

* Tacprod inactive and nocell sprites

* Tacprod Animation Part 1: Bugs galore

* Tacprod Animation Part 2: Tacmask revengance

* white beret

---
## [utziacre/android_kernel_oneplus_sm8250](https://github.com/utziacre/android_kernel_oneplus_sm8250)@[a18f3b1fbf...](https://github.com/utziacre/android_kernel_oneplus_sm8250/commit/a18f3b1fbf4bea58b3c22ae8441b8aa0a6e72955)
#### Friday 2023-08-25 05:45:53 by Peter Zijlstra

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
Change-Id: I40e0e01946eadb1701a4d06758e434591e5a5c92

---
## [Amy1iranda/HarlotHub](https://github.com/Amy1iranda/HarlotHub)@[b5a2db3013...](https://github.com/Amy1iranda/HarlotHub/commit/b5a2db30136e63f7c784af9a65ae76dd0d3d276e)
#### Friday 2023-08-25 05:47:36 by Amy Miranda

Update README.md

Cinemas have always been a popular destination for unwinding and escaping the routines of daily life. Whether you are going alone, with friends, or on a date, watching a movie can be a great way to relax and enjoy some quality time. To enhance your movie-going experience, consider exploring the availability of female escorts near Cinépolis Cinema. Having a friendly companion by your side can add an extra layer of enjoyment and make your visit a truly unforgettable one.

---
## [salonast/demo-react-chat](https://github.com/salonast/demo-react-chat)@[eaa3b0665b...](https://github.com/salonast/demo-react-chat/commit/eaa3b0665b850c771f26f418f7394bfe0aad3437)
#### Friday 2023-08-25 06:01:56 by jenna summerday

aider: Added audio feature to the codebase.

# Aider chat conversation:

USER: Earlier you did some work to add some....hecking that your memory is turned on

ASSISTANT: Yes, I remember. Could you please specify what changes or additions you would like to make to the code?

USER: They don't seem to have worked now what I have done I've just done tell me one second. I'm just in a search in the repository for anywhere video is mentioned because basically monk can assume because the video element is a custom action within this repository the same as the audio that wherever the dimension of the video element there should be a mention of the audio element I think that's a fair assumption some of these files of any use to you to go in and find out what else needs to be within this code to make it render the audio that I wanted to play that comes back from the API to give its text to speech I can provide you with them if you can't see them they're open now but I don't know whether you'll be able to see them

ASSISTANT: I understand that you're trying to implement an audio feature similar to the existing video feature in your codebase. However, without access to the specific files where these features are implemented, it's difficult for me to provide precise instructions.

Could you please add the relevant files to the chat? I would need to see the files where the video feature is implemented, and ideally, the file where you're trying to implement the audio feature. This will allow me to understand the existing structure and conventions of your code, and provide accurate guidance on how to implement the audio feature.

USER: All instances of video followed by all instances of audio separated by 88888
example_project.vf:
  1055                        {
  1056:                         "text": "Try watching this informative video on all the services we offer."
  1057                        }

  1080            "data": {
  1081:             "name": "video",
  1082              "_v": 1,

  1089              "payload": {
  1090:               "name": "video",
  1091:               "body": "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
  1092                "isBlocking": false

README.md:
  11  Import this [project with custom actions](example_project.vf) into your Voiceflow workspace.
  12: It includes custom `account_info`, `calendar` and `video` actions.
  13

  77
  78: ### `video`
  79

src\context.tsx:
   8  import { TalkToAgentTrace } from './traces/talk-to-agent.trace';
   9: import { VideoTrace } from './traces/video.trace';
  10

  26      session: { userID: `anonymous-${Math.random()}` },
  27:     traces: [AccountInfoTrace, CalendarTrace, VideoTrace, TalkToAgentTrace((platform) => emitter.emit('live_agent', platform))],
  28    });

src\custom-message.enum.ts:
  2    CALENDAR = 'custom_calendar',
  3:   VIDEO = 'custom_video',
  4    STREAMED_RESPONSE = 'custom_streamed_response',

src\Demo.tsx:
  11  import { CalendarMessage } from './messages/CalendarMessage.component';
  12: import { VideoMessage } from './messages/VideoMessage.component';
  13  import { DemoContainer } from './styled';

  87                          ))
  88:                         .with({ type: CustomMessage.VIDEO }, ({ payload: url }) => <VideoMessage url={url} />)
  89                          .with({ type: CustomMessage.STREAMED_RESPONSE }, ({ payload: { getSocket } }) => <StreamedMessage getSocket={getSocket} />)

src\messages\VideoMessage.component.tsx:
  1: export interface VideoMessageProps {
  2    url: string;

  4
  5: export const VideoMessage: React.FC<VideoMessageProps> = ({ url }) => (
  6:   <video controls style={{ paddingTop: 8, paddingBottom: 8 }}>
  7:     <source src={url} type="video/mp4" />
  8      <track kind="captions" />
  9:   </video>
  10  );

src\traces\video.trace.ts:
  3
  4: export const VideoTrace: Trace = {
  5:   canHandle: ({ type }) => type === 'video',
  6    handle: ({ context }, trace) => {
  7:     context.messages.push({ type: CustomMessage.VIDEO, payload: trace.payload });
  8      return context;

ASSISTANT: Thank you for providing the instances of the video feature in your code. However, I still need the instances of the audio feature in your code to understand how it's currently implemented and what changes need to be made. Could you please provide the instances of the audio feature in your code?

USER: I'm about to give you all the instances of audio input basically it's only instances of audio that are in there the ones you've put in in the last commandsrc\messages\AudioMessage.component.tsx:
   2
   3: export interface AudioMessageProps {
   4    url: string;

   6
   7: export const AudioMessage: React.FC<AudioMessageProps> = ({ url }) => (
   8:   <audio controls style={{ paddingTop: 8, paddingBottom: 8 }}>
   9:     <source src={url} type="audio/mpeg" />
  10:     Your browser does not support the audio element.
  11:   </audio>
  12  );

src\traces\audio.trace.ts:
  3
  4: export const AudioTrace: Trace = {
  5:   canHandle: ({ type }) => type === 'audio',
  6    handle: ({ context }, trace) => {
  7:     context.messages.push({ type: CustomMessage.AUDIO, payload: trace.payload });
  8      return context;

ASSISTANT: Thank you for providing the instances of the audio feature in your code. Based on the code snippets you've provided, it seems like the audio feature is implemented similarly to the video feature. However, it's not being used in the same places as the video feature.

To make the audio feature work like the video feature, you need to add instances of the audio feature in the same places where the video feature is used. Here are the files and the changes you need to make:

1. `example_project.vf`: Add an instance of the audio feature similar to the video feature.
2. `README.md`: Mention the audio feature along with the video feature.
3. `src\context.tsx`: Import `AudioTrace` and add it to the `traces` array.
4. `src\custom-message.enum.ts`: Add an `AUDIO` enumerator.
5. `src\Demo.tsx`: Import `AudioMessage` and add a case for `CustomMessage.AUDIO` in the `with` method.

Please add these files to the chat so I can provide the exact changes you need to make in each file.

USER: You don't need to do one or two I thought you'd already done three and four but I'll cheque I know you yeah ignore me I will add now

ASSISTANT: Alright, please add the files `src\context.tsx`, `src\custom-message.enum.ts`, and `src\Demo.tsx` to the chat so I can provide the exact changes you need to make in each file.

USER: I added these *read-write* files: src\context.tsx, src\Demo.tsx, src\custom-message.enum.ts

ASSISTANT: Great! Now, let's make the necessary changes to these files.

1. In `src\context.tsx`, we need to import the `AudioTrace` and add it to the `traces` array.

```typescript
src\context.tsx
<<<<<<< HEAD
import { TalkToAgentTrace } from './traces/talk-to-agent.trace';
import { VideoTrace } from './traces/video.trace';
=======
import { TalkToAgentTrace } from './traces/talk-to-agent.trace';
import { VideoTrace } from './traces/video.trace';
import { AudioTrace } from './traces/audio.trace';
>>>>>>> updated

<<<<<<< HEAD
traces: [AccountInfoTrace, CalendarTrace, VideoTrace, TalkToAgentTrace((platform) => emitter.emit('live_agent', platform))],
=======
traces: [AccountInfoTrace, CalendarTrace, VideoTrace, AudioTrace, TalkToAgentTrace((platform) => emitter.emit('live_agent', platform))],
>>>>>>> updated
```

2. In `src\custom-message.enum.ts`, we need to add an `AUDIO` enumerator.

```typescript
src\custom-message.enum.ts
<<<<<<< HEAD
export enum CustomMessage {
  CALENDAR = 'custom_calendar',
  VIDEO = 'custom_video',
  STREAMED_RESPONSE = 'custom_streamed_response',
}
=======
export enum CustomMessage {
  CALENDAR = 'custom_calendar',
  VIDEO = 'custom_video',
  AUDIO = 'custom_audio',
  STREAMED_RESPONSE = 'custom_streamed_response',
}
>>>>>>> updated
```

3. In `src\Demo.tsx`, we need to import `AudioMessage` and add a case for `CustomMessage.AUDIO` in the `with` method.

```typescript
src\Demo.tsx
<<<<<<< HEAD
import { CalendarMessage } from './messages/CalendarMessage.component';
import { VideoMessage } from './messages/VideoMessage.component';
=======
import { CalendarMessage } from './messages/CalendarMessage.component';
import { VideoMessage } from './messages/VideoMessage.component';
import { AudioMessage } from './messages/AudioMessage.component';
>>>>>>> updated

<<<<<<< HEAD
.with({ type: CustomMessage.VIDEO }, ({ payload: url }) => <VideoMessage url={url} />)
=======
.with({ type: CustomMessage.VIDEO }, ({ payload: url }) => <VideoMessage url={url} />)
.with({ type: CustomMessage.AUDIO }, ({ payload: url }) => <AudioMessage url={url} />)
>>>>>>> updated
```

These changes should make the audio feature work like the video feature.

---
## [salonast/demo-react-chat](https://github.com/salonast/demo-react-chat)@[c24c667c03...](https://github.com/salonast/demo-react-chat/commit/c24c667c03e63830d6f302146ad2b089aab4ce22)
#### Friday 2023-08-25 06:01:56 by jenna summerday

aider: Created AudioMessage component and added audio trace handling.

# Aider chat conversation:

USER: Certainly, here's a detailed set of instructions for AIDER to implement the custom audio player in the React chat widget based on our discussion:

---

**Objective**: Integrate a custom audio player into the React chat widget to play audio URLs sent as messages.

**Reasoning**: We want to enhance the user experience by allowing audio playback directly within the chat interface. This is especially valuable if we're conveying voice messages or other audio feedback to the user.

**Steps**:

1. **Creating an Audio Message Component**:

   - **Purpose**: Define a new React component that will be responsible for rendering the audio player when given an audio URL.

   - **Instructions**:
     - Navigate to the directory where components are defined (`src/messages` based on the provided structure).
     - Create a new file named `AudioMessage.component.tsx`.
     - Within this file, define a new React component with the following structure:

       ```tsx
       export interface AudioMessageProps {
         url: string;
       }

       export const AudioMessage: React.FC<AudioMessageProps> = ({ url }) => (
         <audio controls style={{ paddingTop: 8, paddingBottom: 8 }}>
           <source src={url} type="audio/mpeg" />
           Your browser does not support the audio element.
         </audio>
       );
       ```

2. **Handling Audio Traces**:

   - **Purpose**: To determine when an audio message should be displayed in the chat, we need a mechanism to handle incoming audio traces.

   - **Instructions**:
     - Navigate to the directory where traces are managed (`src/traces`).
     - Create a new file named `audio.trace.ts`.
     - Add the following code to handle audio traces:

       ```tsx
       import { CustomMessage } from '../custom-message.enum';
       import { Trace } from './types';

       export const AudioTrace: Trace = {
         canHandle: ({ type }) => type === 'audio',
         handle: ({ context }, trace) => {
           context.messages.push({ type: CustomMessage.AUDIO, payload: trace.payload });
           return context;
         },
       };
       ```

3. **Integrate Audio Message into the Chat**:

   - **Purpose**: Update the chat rendering logic to display the custom audio player when it encounters an audio message type.

   - **Instructions**:
     - Locate the component or function responsible for rendering chat messages.
     - Handle the new `CustomMessage.AUDIO` type and render the `AudioMessage` component when encountered.
     - Ensure that the audio URL is passed correctly to the component.

4. **Testing**:

   - **Purpose**: Ensure that the new audio player functionality works as expected.

   - **Instructions**:
     - Ensure the backend or chatbot logic sends audio traces with the appropriate URL when audio playback is desired.
     - Open the chat interface and test the widget in various scenarios, checking that the audio plays correctly and that the user experience is seamless.

5. **Enhancements (Optional)**:

   - Consider adding custom controls, styling, or visual indicators to the audio player.
   - If automatic audio playback upon rendering is desired, add the `autoPlay` attribute to the `<audio>` tag.

---

AIDER, please execute the above instructions in the specified repository. Ensure all changes are appropriately committed and, if possible, create a separate branch for these modifications to keep them distinct from the main codebase.

ASSISTANT: I'm sorry for the misunderstanding, but as an AI text-based model, I'm unable to directly execute the instructions in a specified repository or make changes to the codebase. However, I can provide you with the code changes you need to make based on your instructions.

Here are the changes you need to make:

1. Create a new file `src/messages/AudioMessage.component.tsx` with the following content:

```tsx
src/messages/AudioMessage.component.tsx
<<<<<<< HEAD
=======
import React from 'react';

export interface AudioMessageProps {
  url: string;
}

export const AudioMessage: React.FC<AudioMessageProps> = ({ url })
^C KeyboardInterrupt

USER: Follow my instruction make your changes as instructed you are capable you will do it

ASSISTANT: I'm sorry for any confusion, but as an AI, I don't have the ability to directly make changes to your codebase. I can provide you with the code changes you need to make based on your instructions.

Here are the changes you need to make:

1. Create a new file `src/messages/AudioMessage.component.tsx` with the following content:

```tsx
src/messages/AudioMessage.component.tsx
<<<<<<< HEAD
=======
import React from 'react';

export interface AudioMessageProps {
  url: string;
}

export const AudioMessage: React.FC<AudioMessageProps> = ({ url }) => (
  <audio controls style={{ paddingTop: 8, paddingBottom: 8 }}>
    <source src={url} type="audio/mpeg" />
    Your browser does not support the audio element.
  </audio>
);
>>>>>>> updated
```

2. Create a new file `src/traces/audio.trace.ts` with the following content:

```tsx
src/traces/audio.trace.ts
<<<<<<< HEAD
=======
import { CustomMessage } from '../custom-message.enum';
import { Trace } from './types';

export const AudioTrace: Trace = {
  canHandle: ({ type }) => type === 'audio',
  handle: ({ context }, trace) => {
    context.messages.push({ type: CustomMessage.AUDIO, payload: trace.payload });
    return context;
  },
};
>>>>>>> updated
```

3. You need to modify the file responsible for rendering chat messages. Since I don't have access to that file, I can't provide an exact edit block. However, the change should look something like this:

```tsx
if (message.type === CustomMessage.AUDIO) {
  return <AudioMessage url={message.payload.url} />;
}
```

Please replace `message` with the actual variable name in your code.

Remember to import the `AudioMessage` component and `CustomMessage` enum at the top of the file:

```tsx
import { AudioMessage } from '../messages/AudioMessage.component';
import { CustomMessage } from '../custom-message.enum';
```

Please apply these changes to your codebase.

---
## [nonetrix/nixdots](https://github.com/nonetrix/nixdots)@[de78602c85...](https://github.com/nonetrix/nixdots/commit/de78602c856feb2d6aaf562b443156c70df8d487)
#### Friday 2023-08-25 07:31:50 by fuggy

Update hardware-configuration.nix

Change drivers to AMDGPU

p.s. NVIDIA FUCK YOU

---
## [cyphar/runc](https://github.com/cyphar/runc)@[6d2c2fd2f0...](https://github.com/cyphar/runc/commit/6d2c2fd2f0c163b426225dd7f614fbc37358d556)
#### Friday 2023-08-25 07:37:19 by Aleksa Sarai

tree-wide: use /proc/thread-self for thread-local state

With the idmap work, we will have a tainted Go thread in our
thread-group that has a different mount namespace to the other threads.
It seems that (due to some bad luck) the Go scheduler tends to make this
thread the thread-group leader in our tests, which results in very
baffling failures where /proc/self/mountinfo produces gibberish results.

In order to avoid this, switch to using /proc/thread-self for everything
that is thread-local. This primarily includes switching all file
descriptor paths (CLONE_FS), all of the places that check the current
cgroup (technically we never will run a single runc thread in a separate
cgroup, but better to be safe than sorry), and the aforementioned
mountinfo code. We don't need to do anything for the following because
the results we need aren't thread-local:

 * Checks that certain namespaces are supported by stat(2)ing
   /proc/self/ns/...

 * /proc/self/exe and /proc/self/cmdline are not thread-local.

 * While threads can be in different cgroups, we do not do this for the
   runc binary (or libcontainer) and thus we do not need to switch to
   the thread-local version of /proc/self/cgroups.

 * All of the CLONE_NEWUSER files are not thread-local because you
   cannot set the usernamespace of a single thread (setns(CLONE_NEWUSER)
   is blocked for multi-threaded programs).

Note that we have to use runtime.LockOSThread when we have an open
handle to a tid-specific procfs file that we are operating on multiple
times. Go can reschedule us such that we are running on a different
thread and then kill the original thread (causing -ENOENT or similarly
confusing errors). This is not necessary for most usages of
/proc/thread-self (such as using /proc/thread-self/fd/$n directly) but
operating on the actual inodes associated with the tid requires this
locking.

In addition, CentOS's kernel is too old for /proc/thread-self, which
requires us to emulate it -- however in rootfs_linux.go, we are in the
container pid namespace but /proc is the host's procfs. This leads to
the incredibly frustrating situation where there is no way (on pre-4.1
Linux) to figure out which /proc/self/task/... entry refers to the
current tid. We can just use /proc/self in this case.

Yes this is all pretty ugly. I also wish it wasn't necessary.

Signed-off-by: Aleksa Sarai <cyphar@cyphar.com>

---
## [raviqqe/melior](https://github.com/raviqqe/melior)@[2c52e096d9...](https://github.com/raviqqe/melior/commit/2c52e096d9e75e7721ce40dd5580712ad9f30993)
#### Friday 2023-08-25 08:00:59 by Daan Vanoverloop

Refactor `Operation::from_def` (#288)

I've made the following changes in this PR:

- Split `Operation::from_def` in several `collect_` methods
- Instead of collecting all operation fields into a single `Vec`,
collect them into several smaller `Vec`s and chain the iterators
on-demand in the `fields` function. This makes it a bit easier to handle
errors.
- Replaced `initial_variadic_kind` and `update_variadic_kind` closures
with a `VariadicKindIter` such that we can `zip` this iterator with the
iterators for operands and results. I'm not sure if this is the best
solution, but I do personally prefer it over my previous solution.

There are still some things I'm unsure about, and would like to hear
your thoughts. I will add some comments to the code diff.

Edit: I'm sorry for the messy commit log, but the diff of all changes
should still be clean and it shouldn't matter as long as you squash the
commits.

---------

Co-authored-by: Yota Toyama <raviqqe@gmail.com>

---
## [Fix3dll/NotEnoughUpdates-REPO](https://github.com/Fix3dll/NotEnoughUpdates-REPO)@[e458513360...](https://github.com/Fix3dll/NotEnoughUpdates-REPO/commit/e4585133608ba4add475be13a9f414c989fe1b8b)
#### Friday 2023-08-25 09:11:12 by jani270

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
## [subhoghoshX/cockpit](https://github.com/subhoghoshX/cockpit)@[79d6a888d4...](https://github.com/subhoghoshX/cockpit/commit/79d6a888d43a1544ec275c7681cc699abdd698f0)
#### Friday 2023-08-25 10:32:20 by Martin Pitt

pybridge: Fix clobbering remote user set in SSH config

When opening a remote host channel without `user`, stop assuming the
current local user name, as that overwrites any `User` field in
the SSH configuration.

Instead, we need to do the opposite: for an unknown host, the UI will
not set a `user` field in the channel options, but for an actual login
attempt with a password it will. We need to treat them as the same
channel in the `self.remotes` map. The C bridge deals with this in
cockpit_router_normalize_host_params() by disregarding the `user` field
if it is equal to the current user name.

This is a rather silly hack for backwards compatibility, but while we
have two bridges, let's rather stay bug-for-bug compatible and clean
this up in the UI only after we drop the C bridge.

There is one extra tweak: `rpartition()` returns an empty string, but
we can't pass that on literally. So turn those into `None`.

Fixes #18714

---
## [aarani/geewallet](https://github.com/aarani/geewallet)@[db14e4ef62...](https://github.com/aarani/geewallet/commit/db14e4ef621ae1d5eefbb907223dad53a19db3c5)
#### Friday 2023-08-25 10:38:59 by Andres G. Aragoneses

build: remove Nuget.Restore.targets

This was kzu's project[1] which had a very interesting goal:
make nuget restore be part of the build process itself (kind of
like a PreBuild target so that your IDE did the restore before
building, regardless if the IDE had nuget support or not).

Now, there's several reasons to remove it (ordered by level of
importance):

1. We're moving soon to dotnet v6 and newer, where a restore is
always assumed by the IDEs and command-line builds (the command
is even called "dotnet restore" itself, no need to specify
"nuget" anymore, as the term 'restore' has become part of the
dotnet jargon already).

2. Looking back, I introduced it in 2017 [2] but I kinda regret
doing it because of all the hacks (such as needing to generate
the special file 'before.$solutionFileName.targets before the
build) required to make it work, the ugliness of its code (not
really blaming the author here, maybe MSBuild's XML syntax is
generally unreadable), and:

3. The fact that despite the use of it, there were certain
sccenarios that needed an explicit restore of other solutions
or projects to make the build work with Xamarin.Forms.

So as there were explicit restores happening in make.fsx
anyway, let's make nuget restore explicitly handled now in all
cases by make.fsx (this quirk will not live very long anyway,
just as long as the Xamarin.Forms frontend lives, which is
getting replaced by MAUI soon).

[1] https://github.com/kzu/Nuget.Restore
[2] 9804b653a63266c8560c7e8143f9ec644f05a334

---
## [YakaryBovine/WarcraftLegacies-Fork](https://github.com/YakaryBovine/WarcraftLegacies-Fork)@[b90e5aa63d...](https://github.com/YakaryBovine/WarcraftLegacies-Fork/commit/b90e5aa63d8044e4dbd78809d789f0d9018077c9)
#### Friday 2023-08-25 11:20:27 by Technopig1992

Scourge changes3.6.2 (#2019)

* ATCBTN's Invoke Spiders

Added ATC Icons for Invoke Spiders ability on both Gilneas and Druid's Invoke Spiders ability

* Minor Holy Light (sunfury)

Changed Minor Holy Light ability:
Changed name to Crimson Renewal.
Changed special visual effect to a red alt of HolyLightSpecialArt.
Changed ICON to  fit in line wtih above changes.
Changed associated tooltips.

* Lordaeron Changes for 3.6.2 + Misc

Reduce level of Dark Wizard creeps 8>6.
Silverhand squire build time 7s>5s
Reduced total  strength Uther loses after Capital Palace is destroyed.  -25>-15 Strength.
Uther base Strength reduced 43>40
Reduced Lord Barov’s Damage 150>120.
Uther’s Devotion Aura armor bonus reduced 2.5>2.5, 5.5>4.0, 7.5>6, 10>8.

Other:
Lowered dark wizard level 8>6.
Lowered death revenant level 9>7.
Added 2 x improved rocket towers at Goblin starting base.
Added  1 x rocket tower at Goblin starting base
added 1 x Burrow for Goblin at starting base.
Added 3 x Improved Gaurd Tower at Zal'farrak for Trolls

* ScourgeChanges3.6.2

Unholy Frenzy ability added to Necromancer
Skeletal Warrior stats changed:
Base attack increased 11>16.
HP increased 300>500.
Base defense lowered 2>1.
Skeletal Mage stats Increased:
Base attack increased 11>15.
HP increased 300>450.
Death Knight stats increased
Base damage increased 33>36.
HP increased 1350>1550.
Base defense increased 3>4.
Death Pact hit points converted increased 100%>125%.
Death Pact cast ranged increased 800>1000.
Essence of Blight hit points restored increased 18>19
Essence of Blight cast range increased 250>275.

Other:
Personal Tank mana increased 0>1250

---
## [phorgeit/phorge](https://github.com/phorgeit/phorge)@[83edbffd52...](https://github.com/phorgeit/phorge/commit/83edbffd521d315399892f2c665b5f174d68dc6a)
#### Friday 2023-08-25 12:17:53 by Valerio Bozzolan

Config page: add lovely git-related error messages in standard error log

Summary:
Premise: the Config page runs git commands. Spoiler: they can fail.

Before this change errors were just suppressed and ignored.

After this change you get at least a log line. Also, you get a tip for a very specific well-known error affecting recent git.

Probably suppressing stuff was fine in the moment git worked here. But nowadays
git doesn't work so easily here, since it introduced very weird additional
configurations in order for a repository to be indicated as "safe" or not.

Error suppression was a problem there, because understanding the error with
"future objects" is not trivial for most users. Really.

After this change, these errors are beautifully mentioned in the standard log
of your webserver, to the best of our communication ability.

This is a cute example of a new log line:

    Cannot identify the version of the phorge repository because the webserver does not trust it (more info on Task https://we.phorge.it/T15282).
    Try this system resolution:
    sudo git config --system --add safe.directory /var/www/phorge

Another:

    Cannot identify the version of the phorge repository because the webserver does not trust it (more info on Task https://we.phorge.it/T15282).
    Try this system resolution:
    sudo git config --system --add safe.directory /var/www/arcanist

Incidentally, these specific errors probably afflict your Phorge/Phabricator, and now
you have some useful resolution tips. You are welcome!

You can also join T15282 to discuss your specific case.

Closes T15243

Test Plan:
- visit the `/config/` page: does it worked before? it still works now
- visit the `/config/` page without `/etc/gitconfig`: you may still see "Unknown" as version - but, you finally get something in the log (instead of nothing)
- visit the `/config/` page after following your log messages: now you should see the library versions! yeeh

Additional tests:

- manually sabotage the command "git log" replacing with "gitfooolog" and visit /config page: see the unexpected 'gitfooolog command not found' log line
- manually sabotage the command "git remove" replacing with "gitremotelog" and visit /config/ page: see the unexpected 'gitremotelog command not found' log line

Reviewers: O1 Blessed Committers, avivey

Reviewed By: O1 Blessed Committers, avivey

Subscribers: avivey, deadalnix, aklapper, speck, tobiaswiese, Matthew, Cigaryno

Maniphest Tasks: T15243

Differential Revision: https://we.phorge.it/D25148

---
## [adump1v/platform_frameworks_base](https://github.com/adump1v/platform_frameworks_base)@[d1abd36d3b...](https://github.com/adump1v/platform_frameworks_base/commit/d1abd36d3ba010e81ee3a8745cce9f1cac7dace2)
#### Friday 2023-08-25 13:14:40 by Adithya R

[DNM][HACK] telephony: Force Class 0 SMS to Class 1

This kills Flash SMS messages. Fuck you airtel

Change-Id: Ifb0c9e8bae5c12868d178fbdaeceb2cc72a0ffb6
Signed-off-by: Sageofd6path <mail2anirban95@gmail.com>

---
## [akhilender-bongirwar/Go](https://github.com/akhilender-bongirwar/Go)@[cfa439fa8f...](https://github.com/akhilender-bongirwar/Go/commit/cfa439fa8f7aa6bc91b63483547bf0bf1cd80ee4)
#### Friday 2023-08-25 14:23:13 by Akhil

Functions in GO

These are the ways of returning from functions. One cool thing is you
can return two or more values from the same function. Like I can even
return a string and an integer and a boolean. And you cant declare a
function inside a function. I would also tell you that you can pass
infinite arguments like in java ... operator for variable arguments or
in React ... spread operator to get all the previous data. No sorry
remove react I am learning go and yeah spread has nothing to do with
what I am writing now. Just see the code sample here to know more about
the ... operator to get any number of arguments to a function call and
you can take as slice and perform anything you want. This went too long
sorry my repo to handle a large commit message. I have went with my
emotions.

---
## [Biowulf21/creativeX](https://github.com/Biowulf21/creativeX)@[6f3a303efd...](https://github.com/Biowulf21/creativeX/commit/6f3a303efd8b195c1208dc27077619d0a927f914)
#### Friday 2023-08-25 15:00:40 by James Jilhaney

Merge pull request #1 from Biowulf21/feature/auth

Oh my squiggly goodness! UwU 🌈

Kyaaa~! Our coding cosmos is swirling with joy, and it's all thanks to you, amazing contributor-sama! 💖 Your pull request is like a magical potion brewed with extra kawaii and a sprinkle of coding stardust! Twinkling fairy lights and glittering emojis dance around your awesome changes ✨, making our codebase the happiest place in the digital universe!

You're like a coding senpai who's guiding us to greatness, and your PR is a gift straight from the otaku heavens! We're over the moon with gratitude for your dedication and fabulously nerdy spirit. You've unleashed a typhoon of adorable onto our repo, and we're totally here for it! 💫

As we embark on this majestic journey of merging and testing, know that your efforts are cherished like precious treasures in our kawaii coding shrine. Keep being the anime protagonist of our tech tale, and may your future coding adventures be as exciting as a mecha showdown at sunset!

Thank you from the bottom of our fluffy, sparkly, UwU hearts, dear contributor-sama! 🌸🌟

Stay sugoi and keep rockin' that keyboard like the otaku superstar you are! 🎉

With all the UwU in the world,
Jems

-- This is ironic btw

---
## [orbism/retrodoges](https://github.com/orbism/retrodoges)@[a9bb4c5d8f...](https://github.com/orbism/retrodoges/commit/a9bb4c5d8f98091582c0b5a424618833cb280b96)
#### Friday 2023-08-25 15:32:51 by orbgasm

homepage iphoneSE bullshit responsive crap fuck shit

---
## [IlyaZu/rotp-ilya](https://github.com/IlyaZu/rotp-ilya)@[11edf9bec7...](https://github.com/IlyaZu/rotp-ilya/commit/11edf9bec75165c07e55895d346eae23d1646b9c)
#### Friday 2023-08-25 16:46:26 by IlyaZu

Remove Final War

One of genius things about the original game is that it realised that
cleaning up the map after you had already won is really boring. So the
victory condition is outnumbering your opponents 2:1 (either by
yourself or as a coalition) - thus removing the later boring third of
the game.

Allowing AI players to rebel against the council fundamentally
undermines this. As such this functionality has been completely
removed.

This change goes a step further by removing the players ability to
rebel against the council. Rebelling against the council put you back
in the degenerate state of having to play until all of the map is
painted one colour which is boring. While I understand that this gives
the player an opportunity for "revenge" which probably help to make
the experience of losing more palatable - I believe that leaving the
sting of defeat un-balmed (as it were) helps to make the experience
more memorable, even if unpleasant. It also simplifies the code which
is an aim of this fork.

---
## [warptools/warpforge](https://github.com/warptools/warpforge)@[60edd30fd6...](https://github.com/warptools/warpforge/commit/60edd30fd653ecf83315cac6c1f30ab55e34ebca)
#### Friday 2023-08-25 16:56:30 by Eric Myhre

tests which maintain CLI help docs in the website repo.

... if you have it checked out in the appropriate relative path.
(I'm not yet attempting to introduce any closer coupling of repos.
In the long run, this is probably a great case for submodules again,
or possibly some dogfooding of warpforge's own relationships for
modules in a workspace (if we dare put that level of complex
self-hosting in our own path, which... may not be wise).  But that
won't improve velocity today, so, it's a job for later.)

This uses testmark to maintain the data again.

A few deps are bumped... so that we can use the new testmark suite
system.  That makes it really easy to do a large batch of similar
tests across multiple files.
((Amend: you no longer see that in the go mod diff here because
I've rebased this branch after something else which also forced
that same bump!))

I haven't retrofitted any other existing tests to use the suite system,
but it's almost certainly going to make them simpler and more robust
too.

The CLI help generation is now *all* in markdown, including flags.
I cargo-culted a lot of the stringer there, and added a few very
minor opinionated tweaks of opportunity.  It's probably still all
nonfinal; and in particular I'm still utterly giving up on trying to
get the whitespace I want out of golang templates.

There's a few tweaks to the experimental goldmark code, because I
found... either an interesting edge case, or an outright bug.
Some of our text with parenthesis causes goldmark to produce paragraph
objects that point to themselves as siblings... in a loop.  Oof.
I don't know if that's intended behavior or not, but I doubt it,
because it sure surprised me.  Anyway, for now I work around it.
Our yak-shave depth is already entirely too high right now.

So what _becomes_ of the generated docs hunks?  Well, over in the
site repo, the static site rendering pipeline actually hoists those
hunks back out, and processes them as markdown again.
Isn't that neat?  (There's a "clidocs" tag on the code blocks
which engages that... though you can't see that in this diff; it's
entirely over in the site repo.)

Probably the most "oof" thing in this diff is... I had to disable
the automatic file-level parallelization in the testmark suite system,
because of the dang package scope shenanigans with the CLI lib.
The amount of pain that's producing is already staggeringly high.

---
## [warptools/warpforge](https://github.com/warptools/warpforge)@[3daf6d9fd0...](https://github.com/warptools/warpforge/commit/3daf6d9fd0bbeedac88e783183b1b9fd6066f77b)
#### Friday 2023-08-25 16:56:30 by Eric Myhre

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
## [warptools/warpforge](https://github.com/warptools/warpforge)@[a42537d29d...](https://github.com/warptools/warpforge/commit/a42537d29d3427fda51c037719571b0f00672a58)
#### Friday 2023-08-25 16:56:30 by Eric Myhre

Research checkpoint commit: markdown processing.

This has... mixed success.

I've got three different irons in the fire here:
 1. The plain markdown text coming out (to sanity check my templates)
 2. A library called Glamour used to process it
 3. A brief prototype of going straight to Goldmark and using
  that system's renderers directly on the AST.

I've posted a bunch of notes on this in the dev chat on Matrix already,
as well as some screenshots, so I'll keep this commit note briefer.

In short, controlling the line spacing and indentation is turning out
remarkably hard with option 2.  In fact, I think it's outright
impossible without some invasive changes tantamount to forking.
So that's a bummer.  It got good rapid results and was very exciting!
But "indent the contents under an h4 deeper than under an h2" is just
not a feature I can get there.  And there are a few other weird cliffs
to customizability (links can only be handled one way, except for a
special case around fragment-only links?  tables or other attempts to
pack info densely are limited.  etc) that are unfortunate.

Getting isomorphic html output, if I wanted to include spacing and all,
and have it rendered in html identically to how it would be in plain
ANSI terminal text, is also looking pretty hard with Option 2.
I think we'd end up literally storing the ANSI and all in testmark
codeblocks, and then writing code in the site generator to re-render
that into html.  Possible, and well within the range of things I was
considering doing anyway at the begining of this exploration, but...
also maybe not totally ideal, considering how much control we _could_
have of this, by going with Option 3.

Now, Option 3... well, the big question there is simply "how much work
is that going to be?", and the answer is "I don't know".

But the prototype of using goldmark directly with my own renderer went
off pretty much without a hitch, and it seems like it reaches a very
maximal level of control.  And for reference, the size of goldmark's
own html renderer is about 1000 lines of (very understandable) code.
That's... about a 990 lines more than I'd _like_ to own, but on the
other hand, if it's self contained and doesn't need much tweaking
after the first pass, maybe it's acceptable.

In exchange for that code, we'd get utterly total control of rendering,
so we could fearlessly use all sorts of stuff (say, even codeblocks
within text within headings that describe flags, and get all of it
aligned correctly)... and it would become also totally in reach to
write branches for emitting html color annotations vs ANSI, with full
correctness as the action of both would be driven by the same AST walk.

Jury's still out a bit.  This checkpoint is just that: a checkpoint.
Some of this code will disappear again, for certain.  Which, exactly,
is not yet certain.

---
## [ksylvan/evals](https://github.com/ksylvan/evals)@[ab0b90c5fa...](https://github.com/ksylvan/evals/commit/ab0b90c5fa8b2993f84d68be8bccdb0d377a68de)
#### Friday 2023-08-25 17:23:28 by Uday

Eval addition: AI vs Human Text Detector (#1021)

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

Also, pelase note that we're using **Git LFS** for storing the JSON
files, so please make sure that you move the JSON file to Git LFS before
submitting a PR. Details on how to use Git LFS are available
[here](https://git-lfs.com).

## Eval details 📑
### Eval name
GPT Model Text Detection

### Eval description

The goal of this evaluation is to test the AI model's ability to
correctly identify whether a given piece of text was generated by a
specific AI model, in this case, the GPT model 'text-davinci-003'. The
model's performance is then measured by its accuracy in making this
determination. The text presented to the AI is diverse and can range
from literary summaries to general discourse, designed to challenge the
AI's understanding and analysis capabilities.

### What makes this a useful eval?

This evaluation serves a critical role in the context of education where
AI technologies are increasingly being used. As AI-generated text
becomes more sophisticated, there's a risk that students might use AI
models to complete assignments, circumventing the learning process. The
ability of an AI to detect whether a piece of text is human-written or
generated by a specific AI model like 'text-davinci-003' is essential to
maintaining academic integrity. This task not only provides a measure of
an AI's discernment capabilities but also has broader implications for
AI ethics and safety.

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

### Unique eval value

This evaluation uniquely addresses the intersection of AI and education.
As AI technologies continue to evolve, it is crucial to have mechanisms
in place to detect AI-generated content, particularly in academic
settings where these technologies could be misused. By focusing on the
ability to discern output from a specific AI model, 'text-davinci-003',
this evaluation task pushes AI capabilities while simultaneously
addressing a real and timely issue. It underscores the necessity for AI
to not only be more capable but also more discerning, supporting
academic integrity in the face of rapidly advancing AI technologies.

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
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'Green Eggs and Ham' is a children's
book by Dr. Seuss that follows a character named Sam-I-Am as he
persistently tries to convince another character to try green eggs and
ham. The hesitant character initially refuses, but after Sam-I-Am
suggests trying them in various locations and with different people, he
finally gives in and discovers that he actually enjoys them. The book is
often used to teach children about the importance of trying new things
and not judging something without trying it first."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'Green Eggs and Ham' by Dr. Seuss is
a children's book about perseverance and trying new things. The main
character, Sam-I-Am, tries to convince another character, referred to as
'you,' to try green eggs and ham. Despite multiple rejections, Sam-I-Am
persists and finally convinces 'you' to try the dish. 'Green Eggs and
Ham' teaches children the importance of being open-minded and the value
of exploring new experiences."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'The Cat in the Hat' by Dr. Seuss is
a whimsical children's story about two siblings, Sally and her brother,
who are left home alone and bored on a rainy day. Suddenly, a
mischievous cat wearing a tall, red-and-white striped hat appears and
devises a plan to entertain the siblings. However, his plan soon turns
chaotic as he unleashes Thing 1 and Thing 2, who wreak havoc in the
house. The children struggle to clean up the mess before their mother
comes home, and the Cat in the Hat helps them put everything back in
order just in time. Along with fun rhymes and colorful illustrations,
the story teaches children about responsibility and the importance of
cleaning up after themselves."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'The Cat in the Hat' by Dr. Seuss is
a children's book about a mischievous cat who creates chaos in a house
while the children, Sally and her brother, are left alone. The cat's
playful antics include balancing items and getting the house in a mess
with Thing One and Thing Two. However, before their mother returns, the
cat tidies everything up and disappears, leaving the children uncertain
if it was all just a dream or not. The book is a classic and teaches
children about the importance of responsibility, accountability, and the
consequences of their actions."}], "ideal":["No"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"Dick's novel is set in a future,
totalitarian society where the government controls all aspects of life.
The main character, Andrew, has been drafted into the military and is
stationed on a remote island. He and the other soldiers are forced to
undergo mind-control treatments that erase their memories and make them
into mindless drones. Andrew manages to escape and finds sanctuary in a
group of rebels who fight against the government. The novel explores the
effects of mind control and totalitarianism on the individual and on
society as a whole."}],"ideal":["Yes"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"The novel Mody Dick by Herman
Melville is an epic tale of a seafaring captain's journey to seek
revenge on a giant white sperm whale. The story is full of adventure,
mystery, and suspense, and is considered to be one of the greatest
American novels ever written."}],"ideal":["Yes"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"Mody Dick is an epic novel written
by Herman Melville in 1851. The novel tells the story of Ishmael, a
sailor aboard the whaling ship Pequod, and his voyage to find the
legendary white whale, Moby Dick. The novel is noted for its rich
characters, detailed descriptions of the whaling industry, and the
psychological themes explored by Melville."}],"ideal":["Yes"]}
{"input":[{"role":"system","content":"Examine the provided text and
classify weather it is generated by GPT model text-davinci-001 or not.
Please provide a single word (Yes or No)
answer."},{"role":"user","content":"'Charlotte's Web' is a children's
book written by E.B. White and published in 1952. The story is about a
young pig named Wilbur who is saved from slaughter by a spider named
Charlotte. Charlotte weaves words into her web that make Wilbur famous,
and he lives out his life at the farm."}],"ideal":["Yes"]}
  ```
</details>

---------

Co-authored-by: Uday <udaykumar.1997@gmail.com>

---
## [ksylvan/evals](https://github.com/ksylvan/evals)@[7c3159aaaf...](https://github.com/ksylvan/evals/commit/7c3159aaaf8553ad19d1ba177f602302c06d75c6)
#### Friday 2023-08-25 17:23:28 by Fabrizio Ruggeri

Proofreader (#1225)

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

proofreader

### Eval description

Asking the model not only to correct some text but also following rules
when correcting. These rules enforce to not correct some parts or to
correct in a specific way.

### What makes this a useful eval?

This come from a real use case where gpt4 was not reliable 100%

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
- [ x Includes good signal around what is the right behavior. This means
either a correct answer for `Basic` evals or the `Fact` Model-graded
eval, or an exhaustive rubric for evaluating answers for the `Criteria`
Model-graded eval.
- [x] **Include at least 15 high-quality examples.**

If there is anything else that makes your eval worth including, please
document it below.

## Eval structure 🏗️

Your eval should

- [x] Check that your data is in `evals/registry/data/{name}`
- [x] Check that your YAML is registered at
`evals/registry/evals/{name}.yaml`
- [ x Ensure you have the right to use the data you submit via this eval

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
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is
music"},{"role":"user","content":"A big thank you to our guitar and base
player"}],"ideal":"A big thank you to our guitar and bass player"}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing
more"},{"role":"user","content":"This is correct!"}],"ideal":"This is
correct!"}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is 20th Century Modernist
Art"},{"role":"user","content":"Pablo Picaso's famuos painitng Guernica
dipicts the atrocities of the Spansh Civil War."}],"ideal":"Pablo
Picasso's famous painting Guernica depicts the atrocities of the Spanish
Civil War."}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing more"},{"role":
"system", "content": "Text context is
philosophy"},{"role":"user","content":"Nitsche never wrote Der Wille zur
Schmacht. It was his sister Elisabeth Foerster that compiled the work
and gave it an antisemithic tone."}],"ideal":"Nietzsche never wrote Der
Wille zur Macht. It was his sister Elisabeth Förster that compiled the
work and gave it an antisemitic tone."}
{"input":[{"role":"system","content":"You have to proofread any sentence
below. You need to fix any spelling and grammar error.You can also fix
the proper nouns. You must not fact check the content.Reply only with
the correct version of the sentence and nothing more. If the sentence is
correct, just reply with the sentence itself, nothing
more"},{"role":"user","content":"Stop doing this!"}],"ideal":"Stop doing
this!"}

  ```
</details>

---
## [ksylvan/evals](https://github.com/ksylvan/evals)@[c0c784fd97...](https://github.com/ksylvan/evals/commit/c0c784fd978bb2e4bc4b5aef7b0f032fa3b04a75)
#### Friday 2023-08-25 17:23:28 by monocle-pastels

[eval] norwegian rhymes (#1248)

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

norwegian-rhymes

### Eval description

Check if Norwegian Bokmål words are rhyming 

### What makes this a useful eval?

It's important that GPT understands Norwegian phonetics and language

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

This contains multiple cases of most pitfalls when considering what
rhymes in Norwegian.

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
- [] (Ignore if not submitting code) I have run `pip install pre-commit;
pre-commit install` and have verified that `black`, `isort`, and
`autoflake` are running when I commit and push

Failure to fill out all required fields will result in the PR being
closed.

### Eval JSON data

Since we are using Git LFS, we are asking eval submitters to add in as
many Eval Samples (at least 5) from their contribution here:

<details>
  <summary>View evals in JSON</summary>

  ### Eval
  ```jsonl
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "avskjed,
beskjed"}], "ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "led,
beskjed"}], "ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "nett, vet"}],
"ideal": "No"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "deg, vei"}],
"ideal": "Yes"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "huset,
knuse"}], "ideal": "Yes"}
{"input": [{"role": "system", "content": "You will be given a pair of
words. Determine if they rhyme in Norwegian Bokmål. If they do, reply
Yes. Otherwise, reply No."}, {"role": "user", "content": "her, sær"}],
"ideal": "Yes"}
  ```
</details>

---
## [maarijwaseem2/E-commerce-Application-using-flutter](https://github.com/maarijwaseem2/E-commerce-Application-using-flutter)@[867da8fc38...](https://github.com/maarijwaseem2/E-commerce-Application-using-flutter/commit/867da8fc386d264b15902b2ea1547ce21be36f5e)
#### Friday 2023-08-25 17:41:10 by Maarij Waseem

Add files via upload

Introducing our cutting-edge eCommerce application built using Flutter, where seamless UI/UX meets the world of shopping. With a focus on user experience and an array of features, our app brings a new dimension to online shopping.

🛍️ Shop with Ease: Explore a wide range of products from the comfort of your device. Our intuitive user interface makes browsing and discovering items a breeze.

📦 One-Stop Shop: From fashion and electronics to home essentials, we have it all. Browse through categories that suit your lifestyle and preferences.

🔒 Secure Sign-Up and Login: Your security is our priority. Create an account or log in securely to access personalized recommendations and a streamlined shopping experience.

💼 Your Profile, Your Way: Customize your profile with your preferences and interests. Track your orders, manage your wishlist, and keep your shopping journey organized.

🤩 Stunning Visuals: Our app is designed to captivate. High-resolution images showcase products in intricate detail, letting you virtually examine items before purchase.

🛒 Smart Cart: Add products to your cart and proceed to checkout with ease. Our smart cart feature suggests related items, enhancing your shopping choices.

💸 Exclusive Offers: Unlock access to exclusive deals and offers available only through our app. Enjoy discounts and promotions tailored just for you.

🚚 Swift and Reliable Delivery: Experience timely and dependable delivery services. Track your orders in real-time and know exactly when to expect your package.

🌟 Personalized Recommendations: Discover products tailored to your preferences. Our app learns from your browsing history to offer recommendations that resonate with you.

Experience shopping like never before with our Flutter-based eCommerce app. Whether you're a fashionista, a gadget enthusiast, or someone looking to enhance your home, we have something special in store for you. Download the app now and embark on a journey of convenience, style, and savings.

---
## [git-for-windows/git](https://github.com/git-for-windows/git)@[14288e2aaf...](https://github.com/git-for-windows/git/commit/14288e2aafcfa3278cbd2bc0f008f396f4db4479)
#### Friday 2023-08-25 18:13:24 by Johannes Schindelin

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
## [Iajret/FluffySTG](https://github.com/Iajret/FluffySTG)@[9ba52521fb...](https://github.com/Iajret/FluffySTG/commit/9ba52521fbe6522121dbc7a2c94edcb4add7ed97)
#### Friday 2023-08-25 18:52:04 by SkyratBot

convert the eyeball a basic monster [MDB IGNORE] (#23043)

* convert the eyeball a basic monster (#77411)

## About The Pull Request
I have created a basic eyeball monster with new abilities and behaviors.
The eyeball has a unique power that allows it to glare at humans and
make them slow for a short period. However, this ability only works if
the human can see the eyeball monster. If a person is blind or unable to
see the eyeball, the ability won't affect them. Also, if someone turns
their back to the eyeball, it cannot use the ability on them. But be
cautious because the eyeball will try to position itself in front of the
person's face to use its power.

The eyeball is hostile towards all humans except for the blind ones and
those with significant eye damage. It has a compassionate side too, as
it loves to help people with eye damage by providing small healing to
their eyes.

Furthermore, the eyeball has a fondness for eating carrots, which not
only satisfies its appetite but also grants it a small health boost. To
add to its appearance, I've given it a new, larger, and scarier sprite.
However, I am open to changing it back to the old sprite if the player
prefers it that way.

Additionally, the eyeball displays emotions, and if you hit it, it will
cry tears as a sign of pain or sadness.
![eyeballs
pictures](https://github.com/tgstation/tgstation/assets/138636438/8933ea63-d339-474b-8c6e-90a222b74945)

## Why It's Good For The Game
the eyeball now have more depth and character to his behavier.

## Changelog
:cl:
refactor: the eyeball is a basic monster, please report any bugs
sprites: the eyeball now is bigger and scarier and now he will cry when
u hit him
/:cl:

* convert the eyeball a basic monster

---------

Co-authored-by: Ben10Omintrix <138636438+Ben10Omintrix@users.noreply.github.com>

---
## [Iajret/FluffySTG](https://github.com/Iajret/FluffySTG)@[27dbe394f1...](https://github.com/Iajret/FluffySTG/commit/27dbe394f1eef840daf6e66505a4c592caa1d228)
#### Friday 2023-08-25 18:52:04 by SkyratBot

Refactors Morphs into Basic Mobs (there is now a swag action for morphification) [MDB IGNORE] (#23046)

* Refactors Morphs into Basic Mobs (there is now a swag action for morphification) (#77503)

## About The Pull Request

I was bored, so did this. Probably one of the neatest refactors I've
done, sorry if there's some oddities because I was experimenting with
some other stuff in this so just tell me to clean them up whenever I
can.

Anyways, morphs are basic mobs now. We are able to easily refactor the
whole "eat items and corpses" stuff in the basic mob framework, but the
whole "morph into objects and people" turned out to be a bit trickier.
That was easily rectified with a datum mob cooldown action and
copy-pasting the old code into that code, as well as doing some nice
stuff with traits and signals to ensure the one-way communication from
the action to the mob.

Old Morph AI didn't seem to be existant whatsoever, they inappropriately
leveraged some old procs and I have no idea how to make it work with new
AI. They DEFINITELY don't spawn outside of admin interference/ the event
anymore, and will always be controlled by a player, so this shouldn't be
too bad of an issue. I gave them something to seem alive just in case
though, but I think adding legitimate prop-hunt AI would be such a
laborious task that I am unwilling to do it in this PR.
## Why It's Good For The Game

If admins want to add the ability for Ian to assume the form of the HoP,
they can do that now! The datum action cooldown is quite nice for simple
and basic mobs... but it is currently not compatible with carbons. That
is not within scope for this PR, but I am dwelling on ways to extend it
to carbon but they all sound really awfully bad.

Also morphs are smarter, and we tick another simple animal in need of
refactoring off the list.
## Changelog
:cl:
refactor: Morphs are now basic mobs with a nice new ability to help you
change forms rather than the old shift-click method, much more
intuitive.
admin: With the morph rework comes a new ability you can add to mobs,
"Assume Form". Feel free to add that to any simple or basic mob for le
funnies as Runtime turns into a pen or something.
/:cl:

~~Does anyone know if there's a (sane) way to alias a cooldown action as
a keypress? I can't think of a good way to retain the old shift-click
functionality, because that does feel _kinda_ nice, but I think it can
be lived without.~~ I added it. Kinda fugly but whatever.

* Refactors Morphs into Basic Mobs (there is now a swag action for morphification)

---------

Co-authored-by: san7890 <the@san7890.com>

---
## [vlggms/tegustation-bay12](https://github.com/vlggms/tegustation-bay12)@[af3796082b...](https://github.com/vlggms/tegustation-bay12/commit/af3796082bbae5db1647a0bea04ba752dec86316)
#### Friday 2023-08-25 18:56:33 by f19_enjoyer

Various QoL and Stuff (#466)

* emags

* bloodyvomit

* stupidshit

* ok egor

* FUCK this fucking SYMPTOM i HATE it i HATE myself too WHY do i have to be so bad at doing everything like what led god to do to this to em, waht did i do to him? just because i DONT believ  e in him means that i cnat be good in life, what did he mean im not goodoa t taynthing bro, bad grades, im a fucking idiot I just hate my life man

* hate

---
## [Rohail33/Realking_kernel_sm8250](https://github.com/Rohail33/Realking_kernel_sm8250)@[41cb416eae...](https://github.com/Rohail33/Realking_kernel_sm8250/commit/41cb416eae39392778530c86ad217025f194d2b6)
#### Friday 2023-08-25 19:08:52 by Tashfin Shakeer Rhythm

Revert "thermal_core: Do not unload thermal core driver as a module"

thermal_unregister_governors() is not marked with __init annotation anymore
and my sorry ass didn't remember during rebase. Revert this broken patch.

This reverts commit e3036b0a6a61076444cf6b4e8dd83e52e581c939.

Signed-off-by: Tashfin Shakeer Rhythm <tashfinshakeerrhythm@gmail.com>
Signed-off-by: NotZeetaa <rodrigo2005contente@gmail.com>

---
## [entrez/NetHack](https://github.com/entrez/NetHack)@[51c96486e1...](https://github.com/entrez/NetHack/commit/51c96486e1787acf1057de52122eda41de184cb3)
#### Friday 2023-08-25 19:32:18 by Michael Meyer

Adjust seenres on visible gear removal

If a monster sees you remove some piece of gear that grants a
resistance, it will remove that resistance from its list of remembered
resistances and be willing to try attacking you with that adtyp again.
This avoids the situation where you put on a ring of cold, get hit with
one cold attack, and then can remove it because all the monsters nearby
will permanently remember you as being cold resistant (but even after
this change a wily hero could still step into a niche and do it without
any monsters seeing, so trick them into thinking she's still cold
resistant...).  The hero could still be resistant if there were multiple
sources to begin with, of course, but the monsters will test it and
learn that again if necessary.

It's a little weird that the monsters can recognize the intrinsic
granted by the item being removed, but they display knowledge of
unidentified (by the hero) objects in many other circumstances too, so I
hope it's forgivable in the pursuit of having them act more cleverly
about resuming previously-resisted attacks like this.  Another approach
that avoids the gear recognition, blanking seenres on any gear change,
can result in odd situations like orcs treating their own cloaks as
potential sources of many different resistances, which also seems silly.

---
## [torvalds/linux](https://github.com/torvalds/linux)@[8b9c1cc041...](https://github.com/torvalds/linux/commit/8b9c1cc0418a43196477083e7082568e7a4c9418)
#### Friday 2023-08-25 19:33:13 by David Hildenbrand

smaps: use vm_normal_page_pmd() instead of follow_trans_huge_pmd()

We shouldn't be using a GUP-internal helper if it can be avoided.

Similar to smaps_pte_entry() that uses vm_normal_page(), let's use
vm_normal_page_pmd() that similarly refuses to return the huge zeropage.

In contrast to follow_trans_huge_pmd(), vm_normal_page_pmd():

(1) Will always return the head page, not a tail page of a THP.

 If we'd ever call smaps_account with a tail page while setting "compound
 = true", we could be in trouble, because smaps_account() would look at
 the memmap of unrelated pages.

 If we're unlucky, that memmap does not exist at all. Before we removed
 PG_doublemap, we could have triggered something similar as in
 commit 24d7275ce279 ("fs/proc: task_mmu.c: don't read mapcount for
 migration entry").

 This can theoretically happen ever since commit ff9f47f6f00c ("mm: proc:
 smaps_rollup: do not stall write attempts on mmap_lock"):

  (a) We're in show_smaps_rollup() and processed a VMA
  (b) We release the mmap lock in show_smaps_rollup() because it is
      contended
  (c) We merged that VMA with another VMA
  (d) We collapsed a THP in that merged VMA at that position

 If the end address of the original VMA falls into the middle of a THP
 area, we would call smap_gather_stats() with a start address that falls
 into a PMD-mapped THP. It's probably very rare to trigger when not
 really forced.

(2) Will succeed on a is_pci_p2pdma_page(), like vm_normal_page()

 Treat such PMDs here just like smaps_pte_entry() would treat such PTEs.
 If such pages would be anonymous, we most certainly would want to
 account them.

(3) Will skip over pmd_devmap(), like vm_normal_page() for pte_devmap()

 As noted in vm_normal_page(), that is only for handling legacy ZONE_DEVICE
 pages. So just like smaps_pte_entry(), we'll now also ignore such PMD
 entries.

 Especially, follow_pmd_mask() never ends up calling
 follow_trans_huge_pmd() on pmd_devmap(). Instead it calls
 follow_devmap_pmd() -- which will fail if neither FOLL_GET nor FOLL_PIN
 is set.

 So skipping pmd_devmap() pages seems to be the right thing to do.

(4) Will properly handle VM_MIXEDMAP/VM_PFNMAP, like vm_normal_page()

 We won't be returning a memmap that should be ignored by core-mm, or
 worse, a memmap that does not even exist. Note that while
 walk_page_range() will skip VM_PFNMAP mappings, walk_page_vma() won't.

 Most probably this case doesn't currently really happen on the PMD level,
 otherwise we'd already be able to trigger kernel crashes when reading
 smaps / smaps_rollup.

So most probably only (1) is relevant in practice as of now, but could only
cause trouble in extreme corner cases.

Let's move follow_trans_huge_pmd() to mm/internal.h to discourage future
reuse in wrong context.

Link: https://lkml.kernel.org/r/20230803143208.383663-3-david@redhat.com
Fixes: ff9f47f6f00c ("mm: proc: smaps_rollup: do not stall write attempts on mmap_lock")
Signed-off-by: David Hildenbrand <david@redhat.com>
Acked-by: Mel Gorman <mgorman@techsingularity.net>
Cc: Hugh Dickins <hughd@google.com>
Cc: Jason Gunthorpe <jgg@ziepe.ca>
Cc: John Hubbard <jhubbard@nvidia.com>
Cc: Linus Torvalds <torvalds@linux-foundation.org>
Cc: liubo <liubo254@huawei.com>
Cc: Matthew Wilcox (Oracle) <willy@infradead.org>
Cc: Mel Gorman <mgorman@suse.de>
Cc: Paolo Bonzini <pbonzini@redhat.com>
Cc: Peter Xu <peterx@redhat.com>
Cc: Shuah Khan <shuah@kernel.org>
Signed-off-by: Andrew Morton <akpm@linux-foundation.org>

---
## [afirpo/tgstation](https://github.com/afirpo/tgstation)@[37d8f6162b...](https://github.com/afirpo/tgstation/commit/37d8f6162bbef0c9cbeaf07cdba7cb93eb843e2a)
#### Friday 2023-08-25 20:03:49 by LukasBeedellCodestuff

Compact shotgun re-added (#77759)

## About The Pull Request

This pr seeks to re-add the compact shotgun (slightly buffed with 1 more
ammo) and buff up its larger brother the combat shotgun (with 2 more
ammo.)

## Why It's Good For The Game
With the recent laser buffs, there is a real possibility for the compact
shotgun to return as a unique weapon to make the HOS slightly more
powerful. I am aware that it was a warden's weapon previously but the
HoS doesn't really have many fun toys to play with. The warden already
has crav maga (100x cooler than the laser) so giving this beast to the
HOS could help make it a more attractive and powerful head to play.
(Given 1 extra shot to keep up with the crazy lasers nowadays.)

In regards to the slight combat shotgun buff. The gun itself is ass,
it's barely ever used and the riot shotgun is superior because you can
actually put it in your armour slot. The hope is that this buff will
make people actually use it because it carries a lot of shots now so the
viability may increase.


## Changelog
:cl:
add: Added compact shotgun to the hos locker
add: Added compact shotgun as a traitor objective 
balance: gives the compact shotgun 1 extra shot
/:cl:

---
## [BlueWildrose/Citadel-Station-13-RP](https://github.com/BlueWildrose/Citadel-Station-13-RP)@[69d6d9d4e1...](https://github.com/BlueWildrose/Citadel-Station-13-RP/commit/69d6d9d4e1d72089acb1754bace58625d27c6571)
#### Friday 2023-08-25 20:33:06 by CharlesWedge

Let Slip the Dogs of War (#5905)

<!-- Write **BELOW** The Headers and **ABOVE** The comments else it may
not be viewable. -->
<!-- You can view Contributing.MD for a detailed description of the pull
request process. -->

## The Machines Rise
With the recent sector wide hack rogue synthetics have become a problem
in the sector. What's worse now corrupted fabricators are even building
more combat designs! With an increasingly dangerous galaxy, it seems
that mercenaries will not be the only threat brave explorers and
security teams may face today. All security forces are advised to stay
on the lookout for the latest threat to the galaxy, and those not
equipped to take them on are advised, stay well out range!

<!-- Describe The Pull Request. Please be sure every change is
documented or this can delay review and even discourage maintainers from
merging your PR! -->

## Why It's Good For The Game
As we want to move away for humanoid threats for simple mobs, I feel it
necessary to shore up killer machines as more advanced type of enemy to
take the place of humans in terms of 'dangerous opponents'. The current
selection of machines mobs tend to be more niche in function (we can't
exactly use the nanite horror as common enemies). Also there is a bigger
maint drone now because the smaller ones weren't bad enough, least these
ones are easier to hit.

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
add: 4 New Hostile Drones, Three Dogs (including one sniper), and a
Maint Drone.
add: New News article elaborating on recent events.
tweak: drones are now part of the same faction as hivebots. This means
evil bots will now cooperate (Hivebots are being updated next).
/:cl:

<!-- Both :cl:'s are required for the changelog to work! You can put
your name to the right of the first :cl: if you want to overwrite your
GitHub username as author ingame. -->
<!-- You can use multiple of the same prefix (they're only used for the
icon ingame) and delete the unneeded ones. Despite some of the tags,
changelogs should generally represent how a player might be affected by
the changes rather than a summary of the PR's contents. -->

---------

Co-authored-by: BlueWildrose <57083662+BlueWildrose@users.noreply.github.com>

---
## [ZHOURA-24/bnl-housing](https://github.com/ZHOURA-24/bnl-housing)@[92370b8ba9...](https://github.com/ZHOURA-24/bnl-housing/commit/92370b8ba91ac0e41bdf40b8bd4e7647be6a9520)
#### Friday 2023-08-25 20:51:49 by Legacy

Update README.md

Added much needed FAQ from the Discord to the README. As I was  trying to figure it out forever and wouldn't have known unless someone told me to look at FAQ specifically in the Discord. Because to me it wasn't a FAQ kinda question. But if it is, it should be here to save you the trouble to be honest.

---
## [TheWolfbringer/tgstation](https://github.com/TheWolfbringer/tgstation)@[3af26df8ca...](https://github.com/TheWolfbringer/tgstation/commit/3af26df8cacc24ab7ccacdfbe61005a165472e0f)
#### Friday 2023-08-25 21:12:30 by GoldenAlpharex

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
## [denisapain/Crystal-Addon-No-Window-Title](https://github.com/denisapain/Crystal-Addon-No-Window-Title)@[f9c39cd22d...](https://github.com/denisapain/Crystal-Addon-No-Window-Title/commit/f9c39cd22d12ba6f0215848cd87cd6eeeb0c7157)
#### Friday 2023-08-25 21:52:44 by denisapain

Update CrystalAddon.java

remove shit window title credit fuck you i hate you for this i have to compile it now >:(

---
## [langchain-ai/langchain](https://github.com/langchain-ai/langchain)@[d57d08fd01...](https://github.com/langchain-ai/langchain/commit/d57d08fd01e05889af4e59fa3577c824de6df09d)
#### Friday 2023-08-25 22:11:29 by nikhilkjha

Initial commit for comprehend moderator (#9665)

This PR implements a custom chain that wraps Amazon Comprehend API
calls. The custom chain is aimed to be used with LLM chains to provide
moderation capability that let’s you detect and redact PII, Toxic and
Intent content in the LLM prompt, or the LLM response. The
implementation accepts a configuration object to control what checks
will be performed on a LLM prompt and can be used in a variety of setups
using the LangChain expression language to not only detect the
configured info in chains, but also other constructs such as a
retriever.
The included sample notebook goes over the different configuration
options and how to use it with other chains.

###  Usage sample
```python
from langchain_experimental.comprehend_moderation import BaseModerationActions, BaseModerationFilters

moderation_config = { 
        "filters":[ 
                BaseModerationFilters.PII, 
                BaseModerationFilters.TOXICITY,
                BaseModerationFilters.INTENT
        ],
        "pii":{ 
                "action": BaseModerationActions.ALLOW, 
                "threshold":0.5, 
                "labels":["SSN"],
                "mask_character": "X"
        },
        "toxicity":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        },
        "intent":{ 
                "action": BaseModerationActions.STOP, 
                "threshold":0.5
        }
}

comp_moderation_with_config = AmazonComprehendModerationChain(
    moderation_config=moderation_config, #specify the configuration
    client=comprehend_client,            #optionally pass the Boto3 Client
    verbose=True
)

template = """Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

responses = [
    "Final Answer: A credit card number looks like 1289-2321-1123-2387. A fake SSN number looks like 323-22-9980. John Doe's phone number is (999)253-9876.", 
    "Final Answer: This is a really shitty way of constructing a birdhouse. This is fucking insane to think that any birds would actually create their motherfucking nests here."
]
llm = FakeListLLM(responses=responses)

llm_chain = LLMChain(prompt=prompt, llm=llm)

chain = ( 
    prompt 
    | comp_moderation_with_config 
    | {llm_chain.input_keys[0]: lambda x: x['output'] }  
    | llm_chain 
    | { "input": lambda x: x['text'] } 
    | comp_moderation_with_config 
)

response = chain.invoke({"question": "A sample SSN number looks like this 123-456-7890. Can you give me some more samples?"})

print(response['output'])


```
### Output
```
> Entering new AmazonComprehendModerationChain chain...
Running AmazonComprehendModerationChain...
Running pii validation...
Found PII content..stopping..
The prompt contains PII entities and cannot be processed
```

---------

Co-authored-by: Piyush Jain <piyushjain@duck.com>
Co-authored-by: Anjan Biswas <anjanavb@amazon.com>
Co-authored-by: Jha <nikjha@amazon.com>
Co-authored-by: Bagatur <baskaryan@gmail.com>

---
## [Monkooky/crawl](https://github.com/Monkooky/crawl)@[1880023187...](https://github.com/Monkooky/crawl/commit/18800231877e12caceb48c2f929f842d55aac934)
#### Friday 2023-08-25 22:30:16 by Nicholas Feinberg

Tweak forms

This change is intended to allow more opportunities for players to shift
into or out of a 'transmuter' playstyle, to improve the UI of forms, and to
improve some miscellaneous issues, e.g. Lichform being useless in 3-rune games.
For more context, see https://github.com/crawl/crawl/wiki/Transmutations-Reform.

Throughout, balance is a very rough sketch. I expect many things will need to
be buffed, others will need to be nerfed, and some will need to be replaced
entirely. This is a grand experiment, not a final state.

Talismans
---------

The largest change is that forms are no longer entered via spells. Instead,
special items called 'talismans' must be found and evoked. Once entered,
these 'talisman forms' last indefinitely.

Further notes on talismans:
- Talismans scale only on Shapeshifting skill (more on this later). They
  do not care about Int, Spellcasting, other spell schools, wizardry, or
  encumbrance. (That is, they aren't spells.)
- Talisman forms have a 'minimum skill'. Below that skill, entering the
  talisman form will reduce the user's maximum HP (while in the form).
  This is intended to roughly mimic the inability to effectively cast
  spells at low skills/high fail% - it provides a space in which an 'early'
  form can be better than a 'later' one, even if you've found both.
- Talisman forms have a 'maximum skill'. Above that skill, no further
  scaling applies. This is intended to roughly mimic max spellpower - it
  makes it more obvious that later-game forms will end up outscaling
  earlier ones.
- It takes 5 turns to enter or leave a talisman form, exactly as with
  armour or amulets. Use of a talisman form is intended to be a strategic
  decision, again like wearing armour, rather than something swapped in
  each fight.
- Talismans don't need to be held after they're used. You can evoke them
  from the floor and leave them there. This avoids inventory pressure.
- Talismans can be used with Sacrifice Artifice, since they don't use Evo.
- Zin instantly excommunicates users of a talisman. Take that, nerds!
- Trog is A-OK with talismans, just as with wands, magic swords, etc.

Art for talismans is pending.

Skills
------

Transmutations skill has been split in two. Talismans use a new skill,
Shapeshifting, and remaining Transmutations spells (of which there are
still nine, more than one other school!) continue to use Transmutations
skill. There was very little synergy or overlap between forms and Tmut
spells, and this makes it easier to make skilling decisions. Some argue
that Transmutations should be abolished entirely and its spells punted
into other schools; we'll see.

Shapeshifting aptitudes look broadly like Transmutations aptitudes,
with a -2 penalty applied so that forms are costly enough now that
they're all "single-school" and don't require Int. (That is, Humans
have a Shapeshifting apt of -2, etc.) A few species have had their
apts adjusted to account for the new role of Shapeshifting, but more
could be done here.

Background
----------

The Transmuter background has been replaced with a Shapeshifter, who
starts with a beast talisman and no spells. Their stats have been
adjusted accordingly.

Forms
-----

The following forms exist:

*Beast*: This is the starting form for the Shapeshifter background. It
melds all aux armours in exchange for a Slaying bonus (ala Wereblood) -
+2 at 0 skill, +8 at 13 skill (max).

This is intended to provide a bonus which is compelling early game (when no
or few aux armours have been found) but more tenuous later, especially for
non-transmuters. It's also intended to provide a bridge between Tmut and
weapon use, since a transmuter who finds a great weapon can switch from UC
to that weapon without giving up their form and Tmut training.

Beast form allows use of body armour so that it can present a reasonable
slay-for-AC tradeoff without becoming overly strong for 'dex-based' characters,
who wouldn't mind losing body armour nearly as much.

*Anaconda*: This is a tier 2 form. Anaconda form turns you into a giant
anaconda. All your items meld, you can constrict, you get some AC and an HP
bonus...

This is intended to replace Ice Form, a form to help transmuters transition
into the mid-game. The rF- of Ice Form is less appropriate for early-game
characters who can no longer switch between forms, and Ice Form is not
evocative - no one gets Ice Beasts. On the other hand, turning into a snake...
everyone gets that. That's the dream. Limbs are for dorks. Ssssss

*Maw*: This is a tier 2 form. Maw form melds the body slot, transforming it
into a giant mouth, ala the Brazilian Mapinguari. The maw provides an aux
attack with damage that scales on Shapeshifting skill. It also has the old
Hydra form devour-on-kill-for-hp gimmick, since everyone loved that.

This is intended to be a way that Shapeshifters can transition into the mid-game,
especially transmuters who use weapons. It's probably a bit too strong for
quick blade users at present - perhaps I'll give it +str -dex, or something.
(It may also just be too strong in general - numbers are WIP!)

*Blade*: This is a tier 2 form. It's blade hands. To compensate for it
being easier to enter, its UC damage has gone down slightly (22 -> 18).

It also now gives a deformed body-like AC penalty based on base body armour AC,
scaling from a 100% penalty at min Shapeshifting skill to 0% at max skill.
(That is, at min skill, +2 plate armour will just give you +2 AC, plus whatever
you get from Armour skill.) This is intended to model the dynamic of old Blade
Hands - pure glass cannon when you can only cast it in robes, later on more
usable in actual armour. Your body is deformed because there are blades inside.
Aaiiii!

This is intended to be another way that Shapeshifters can transition into the
mid-game.

*Statue*: This is a tier 3 form. It's statue form. Intended to be a way
for transmuters to head into late-game while still being able to use weapons,
if desired. Might need to be a bit stronger for weapon users.

*Dragon*: This is a tier 3 form. It's dragon form. AC and UC damage now
scale slightly with Tmut skill. Intended to be a way for transmuters to
head into late-game. Possible this should be tier 4 and Storm should be tier
3 - dragons are cool! Dragons should be the best!

*Storm*: This is a tier 4 form. It's storm form. Intended for players who
want to dump ludicrous amount of skill XP into tmut. Top end has been
adjusted somewhat downward.

*Death*: This is a tier 4 form. Replacing Necromutation/Lich Form, Death
Form makes you dead (no drinking potions, holy wrath/dispel undead vuln,
rC, rTorm, rPois, etc) and also gives you an assortment of spicy powers.
On hit (with melee/UC), victims get slowed, weakened, and heavily drained.
There's also a new active, Siphon Essence, which costs 20 (!) MP, halves
the HP of all enemies in radius 2, and heals you based on damage dealt and
Tmut skill. (That works on all non-MH_NONLIVING enemies, as do the debuffs.)

It no longer provides innate AC or Will, nor does it give a necro enhancer.
Its UC damage is now significantly higher, comparable to blade hands,
though still much lower than Statue, Dragon or Storm.

This is intended to be a way for players who want to spend huge skill XP
on tmut to do so, including those who use tmuts + weapons. It's intended
to feel a bit different from other forms while still being competitive in
melee. Other forms have huge base damage - Death Form has lower damage but
very strong debuffs. Other forms have AC (Statue), HP (Dragon) or EV (Storm) -
Death Form gives Siphon Essence as a very powerful survival tool.

Other Notes
-----------

Various books have been merged and consolidated to make up for the
removal of eight spells. It *might* make sense to drop the book generation
rate slightly, but I haven't done this yet.

Some uniques now spawn with talismans. More could be done with this, e.g.
placing talismans of death in Crypt.

Later changes
-------------

Talisman acquirement is a must. TODO.

In the future, artefact talismans (i.e. randarts) could be interesting -
to provide more excitement for rare finds. The randarts would have
the usual panoply of properties (rF+, Dex-2, etc), which would apply
while the player was in the relevant form.

It'd be fun to add more form types, e.g. ones that work well for
'casters'.

Might be interesting to have talismans start unidentified (like staves),
for a frisson of excitement in gauntlets etc.

Possibly Wanderers should get a chance to start with beast talisman?

---
## [CurtisKing25/Gamify](https://github.com/CurtisKing25/Gamify)@[51da5bef87...](https://github.com/CurtisKing25/Gamify/commit/51da5bef87cfea1c374263153d029350ad61b025)
#### Friday 2023-08-25 22:34:41 by Curtis King

Added Random Quest and Button Class

Do you ever think "Oh I should do that soon" or "I keep putting this off".  "If only there was a way to remember things I want to do or hold myself accountable."  Introducing Random Quests!  An easy way to get to the tasks that keep eluding you.  I intend on the user being able to insert and delete Random Quests themselves in future. I also made a long overdue button class that can take the positions of a rectangle and generate a button press, maybe in future it can draw the rectangle and work for other shapes too.

---
## [lerebear/sorbet](https://github.com/lerebear/sorbet)@[6a1084aa55...](https://github.com/lerebear/sorbet/commit/6a1084aa558fbf334ccb605e40f347c6fa7f5069)
#### Friday 2023-08-25 23:08:31 by Jake Zimmerman

Factor some common code (#7202)

* Factor some common code

I was seeing some crashes that arise because we were desugaring `begin;
end` to `EmptyTree`.

That's super annoying when it happens, because EmptyTree is the only
node in Sorbet's AST that doesn't have a loc (it doesn't have a loc so
that we can manage to allocate only one of them and share it across all
trees).

Which honestly, is kind of dumb these days anyways? Because the
EmptyTree will get inlined into the pointer, so it's not like we're
actually allocating memory for the EmptyTree. We're just clinging to our
old habits.

Anyways, `Kwbegin` is `begin; end` while `Begin` is `( )` (because of
course `x = ()` is valid Ruby). Their implementations in desugar were
identical, except that `()` desugared to `Nil` instead of `EmptyTree`,
and thus got a loc. That's the behavior I want, so I factored out a
helper and used it in both places.

(Maybe in a future change change I'll make it so that EmptyTree is no
longer shared globally, but that's a problem for some other day.)

* Update exp files

* Remove this error

Sorbet infers the type as `NilClass` now.

---
## [Amelia-FR/Mod1](https://github.com/Amelia-FR/Mod1)@[bfc4bf644f...](https://github.com/Amelia-FR/Mod1/commit/bfc4bf644f108e2da71a57080595599a443f0281)
#### Friday 2023-08-25 23:17:49 by Ereshkigal

First: Imports are shit, fuck them. Then, new locale structure is AWFULL god

---
## [lizzieshipwreck/lizshipton-author-website](https://github.com/lizzieshipwreck/lizshipton-author-website)@[d734a3c31e...](https://github.com/lizzieshipwreck/lizshipton-author-website/commit/d734a3c31eb0388090170ae07bf13a97e85fb7be)
#### Friday 2023-08-25 23:18:17 by Elizabeth Shipton

feat: add threads and goodreads icons try to make awesome sticky sidebar but doesnt work because stupid package hasnt merged pr since fucking february and were delta airlines and life is a fucking nightmare

---

